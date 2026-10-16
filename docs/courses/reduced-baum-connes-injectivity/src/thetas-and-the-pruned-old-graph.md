# Thetas and the pruned old graph

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The second deletion removes all short bicycles. In the graph \(X^{(1)}\), which has no short cycles, a short bicycle must be a *theta*: two branch vertices joined by three paths. For a theta, the terminal tests alone give about \(se/2\) bits of constraints against about \(se\) bits of labels, which is not enough. The extra saving comes from the third incident evaluation at each branch vertex, which must be compatible with the other two at every full block: one relation of \(s\) bits per block. Arranged so that these tests use other source updates than the terminal ones, and so that the two branch vertices do not share tables, they give about \(0.64H\) more bits. Together with the theorem that \(\mathsf H\)-laws use a bicycle four times, the pruned graph then has no short closed paths that are laws [OpenAI-BCI, Sections 4.6-4.8, Lemmas 4.10-4.12, Proposition 4.14].

- Short bicycles are thetas (Section 1).
- Keys in a surviving theta (Section 2).
- The branch relations (Section 3).
- The count of thetas (Section 4).
- The pruned old graph (Section 5).

The notation of [Coherent returns, reconstruction and accumulated rank](coherent-returns-reconstruction-and-accumulated-rank.md) and [Terminal compatibility, key separation and base girth](terminal-compatibility-key-separation-and-base-girth.md) is in force, with \(a=b/\log q\le10^{-6}\), \(m_i=H_i/\log q\), and \(s/b\), \(H_0/s\) large.

## 1. Short bicycles are thetas

**Lemma 1.1.** Let \(B\) be a bicycle in \(X^{(1)}\) with \(e<1.52m_i\) edges and a vertex of height \(i\). Then \(B\) is a theta, \(e>0.9m_i\), its shortest branch has fewer than \(0.51m_i\) edges, and any two of its vertices are joined in \(B\) by a path of fewer than \(0.76m_i\) edges.

*Proof.* Scales vary by at most \(b\) per edge, so every vertex \(v\) of \(B\) has \(m(v)\ge m_i-ae\ge(1-1.52a)m_i\). By Lemma 3.1 of [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md), a figure-eight or a barbell contains two edge-disjoint cycles; each is a cyclically reduced closed path, of length greater than \(0.93m(v)\) at its vertices by Lemma 4.2 of the previous lesson. Their total length would exceed \(1.86(1-1.52a)m_i>1.52m_i\), which is impossible; so \(B\) is a theta. Two of its branches form a cycle, so \(e>0.93(1-1.52a)m_i>0.9m_i\). Its shortest branch has at most \(e/3<0.51m_i\) edges. A theta is \(2\)-edge-connected, so two vertices are joined by two edge-disjoint paths in \(B\), of total length at most \(e\); the shorter has at most \(e/2<0.76m_i\) edges. \(\square\)

## 2. Keys in a surviving theta

**Lemma 2.1** (terminal keys in a surviving theta; [OpenAI-BCI, Lemma 4.10]). Let a theta in \(X^{(1)}\) have \(e<1.52m_i\) edges and a vertex of height \(i\), and put \(H=H_i\). At every source update the terminal keys used at its distinct vertices are distinct. If its two branch vertices lie on the same side, they cannot share a key at an update of aligned depth beyond \(0.65H\), apart from a fixed number of initial and final blocks, which are omitted below.

*Proof.* A repeated terminal key at two receivers gives, by Lemma 2.1 of the previous lesson, agreement of the receivers to an available depth of at least \(H-be-8s\), and the receivers lie on one side. Join them by a shortest path in the theta; by Lemma 1.1 it has fewer than \(0.76m_i\) edges and lies in an interior band. Its coherent threshold is at most
\[
\Bigl(\frac{0.76}{2\cdot0.50005}+0.05\Bigr)H<0.81H ,
\]
far below the available agreement depth once \(b/s\) is small and \(H_0/s\) large. So the path is a coherent return in \(X^{(1)}\subseteq X^{\rm good}\); it contains a minimal one, whose vertices were deleted, a contradiction.

For a key shared by the two branch triples at an update of aligned depth at least \(0.65H\), the last assertion of Lemma 2.1 of the previous lesson identifies the preceding complete prefixes of the two branch vertices, to depth at least \(0.65H-4s\). Their shortest branch has fewer than \(0.51m_i\) edges, with coherent threshold below \((0.51/1.0001+0.05)H<0.56H\). The same contradiction follows. Equality of the unordered triples would in particular give a shared key. \(\square\)

## 3. The branch relations

At a branch vertex, with three incident slots of coefficients \(c_1,c_2,c_3\) (pairwise distinct), the three corrected evaluations of a full ordinary block, with their known offsets moved to the right sides, are \(E_k=v+c_ku\) for the same \((u,v)\). They satisfy
\[
\begin{gathered}
(c_2-c_3)E_1+(c_3-c_1)E_2\\
+(c_1-c_2)E_3=0 .
\end{gathered}\tag{3.1}
\]
Indeed the coefficients of \(v\) sum to zero and those of \(u\) give
\[
\begin{gathered}
c_1c_2-c_1c_3+c_2c_3\\
{}-c_2c_1+c_3c_1-c_3c_2=0 .
\end{gathered}
\]
Conversely, three values satisfying (3.1) arise from a unique \((u,v)\), determined by \(E_1,E_2\).

**Lemma 3.1** (ranks at the branch vertices; [OpenAI-BCI, Lemma 4.11]). In an ordinary full block with three open gates, one branch relation (3.1) has \(\mathbb P_{\rm prod}\)-probability \(2^{-s}\). If two branch vertices on one side have different unordered triples of keys at the same update, their two relations have joint probability \(2^{-2s}\). If the triples coincide, one relation may always be charged.

*Proof.* The three slots of one branch vertex have different labels, hence different keys, so the three new table values at their known arguments are independent and uniform on \(\mathbb F_{2^s}\). Solving (3.1) for one of them, with its nonzero coefficient, shows that the relation holds with probability \(2^{-s}\). Two distinct three-element sets of keys each contain a key not in the other. Condition on all other whole tables, leaving these two *exclusive* tables unexposed. Each is used at one known argument in its own relation, with a nonzero coefficient, and does not occur in the other relation; so the joint probability is \(2^{-2s}\). Other formal queries to the same tables are not prescribed and are integrated out. With equal triples, one of the two (equivalent) relations is kept. \(\square\)

**Separating branch tests from terminal tests.** All terminal updates of a fixed theta lie in the source-index interval
\[
\Bigl[\Bigl\lfloor\frac{H-be}s\Bigr\rfloor-4,\ \Bigl\lceil\frac{H+be}s\Bigr\rceil+2\Bigr],
\]
since the common incidence scales lie between \(H-be-b\) and \(H+be\), and a terminal test of an incidence with common scale \(\kappa s+t\) is at index \(\kappa-1\) or \(\kappa\) (proof of Lemma 2.1 of the previous lesson). This interval has at most \(9+2be/s\) indices. Enlarge it by ten indices at each end and charge no branch relation there. Also omit the first ten source indices, and every marked block and every block of a deterministic identity zone after a mark, at a slot of a branch vertex. These omissions are fixed by the pattern and the mark positions. So a terminal test and a branch test never use the same source update.

The marks are \(K=2\cdot10^6b\) indices apart, so over the six slot sequences of the two branch vertices, separately for each parity, the omitted deterministic blocks cost less than \(0.001H+O(s+be)\) bits. A vertex survives the gate deletions only if, in each slot sequence and each parity, fewer than a fraction \(0.005\) of the blocks are unavailable (Lemma 2.1 of [Auxiliary incidences, deletions and recovery](auxiliary-incidences-deletions-and-recovery.md)); so closed gates at the three slots of each branch vertex cost at most \(0.015H+O(s+be)\) bits. The normalization by parity matters: a bound on all interleaved indices together would allow twice this loss.

**The charging rule.** Before aligned depth \(0.65H\), charge only one branch vertex: if the branch vertices lie on opposite sides, the first chosen one; if they lie on one side with equal triples, either; with different triples, one or both. After depth \(0.65H\), charge both branch vertices at every update with open gates, rejecting predictably any pattern that would share a key there; by Lemma 2.1 no actual theta is rejected. All choices are determined by \(\mathcal F_{<t}\). A branch vertex has \(H/(2s)+O(1+be/s)\) full updates before the terminal band, so one vertex before \(0.65H\) and two afterwards give at least \(0.675H-O(s+be)\) bits, since \((0.65/2+0.35)H=0.675H\). With Lemmas 2.1 and 3.1 and the two omission budgets,
\[
\begin{gathered}
R_{\rm branch}\ge0.675H\\
{}-0.015H-0.001H\\
{}-10^4(s+be)>0.64H .
\end{gathered}\tag{3.2}
\]

**Terminal tests.** Choose two slots at every vertex of the theta. By Lemma 2.1 their keys are distinct, and the gate conditions of the surviving slots make the required gates open. Pair adjacent internal vertices on each branch by (1.1) of the previous lesson; at most six vertices (the two branch vertices and one leftover on each branch) are unpaired. The theta has \(e-1\) vertices, so Lemma 1.1 of the previous lesson gives
\[
R_{\rm term}\ge\frac{se}2-100(s+be).\tag{3.3}
\]
Terminal updates are excluded from branch charges, so the two contributions add up in time under Lemma 4.1 of [Coherent returns, reconstruction and accumulated rank](coherent-returns-reconstruction-and-accumulated-rank.md). Exclusivity of key triples was used only within one update.

## 4. The count of thetas

**Lemma 4.1** (expected number of thetas; [OpenAI-BCI, Lemma 4.12]). For large \(s/b\) and then large \(H_0/s\), the expected number of rooted bicycles in \(X^{(1)}\) with fewer than \(1.52m_i\) edges and root on either side at height \(i\) is at most
\[
2^{0.89H_i} .
\]

*Proof.* By Lemma 1.1 only thetas with \(0.9m_i<e<1.52m_i\) occur. For fixed \(e\), choose the three ordered branch lengths (fewer than \((e+1)^2\) choices), the oriented position of the root (at most \(2e\)), the side (two) and which branch comes first (finitely many): at most \(100(e+1)^4\) choices. Orient the edges for enumeration and choose at most \(L_s^e\) label and height patterns; assigning heights along a spanning tree determines the others, and an inconsistent edge rejects the pattern. By Lemma 3.1 of the lesson on coherent returns, a theta pattern has at most one realization and no free bits. Every actual theta in \(X^{(1)}\) passes the predictable key and gate rejections and has the accumulated ranks (3.2) and (3.3). The tables charged number at most \(2(e-1)\) for terminal tests and six per branch update, \(O(H_i/s)=O(e)\) since \(e>0.9m_i\); \(20e\) suffices after the omitted initial updates. Lemma 4.1 of the lesson on coherent returns bounds the probability by
\[
e^{20\varepsilon_se}\,2^{-se/2-0.64H_i+100(s+be)} .
\]
Summing over the patterns, the exponent is at most
\[
(1.001-0.5)se-0.64H_i+10^5(s+be).
\]
For \(e<1.52H_i/(0.50005s)\) the coefficient of \(H_i\) is at most
\[
\begin{aligned}
\frac{0.501\cdot1.52}{0.50005}-0.64&=0.88288\ldots\\
&<0.883 ,
\end{aligned}
\]
and the error terms and the sum over \(e\) fit below \(0.007H_i\). Embeddedness and survival in \(X^{(1)}\) are conditions on the final reconstruction, not on any current table law. \(\square\)

Delete from \(X^{(1)}\) every vertex of every bicycle with fewer than \(1.52m_i\) edges for one of its vertices of height \(i\), and call the induced graph \(X_{\rm old}\).

## 5. The pruned old graph

**Proposition 5.1** (pruned old graph; [OpenAI-BCI, Proposition 4.14]). Given \(\varepsilon>0\), the parameters and the tables can be chosen so that the two deletions of the pruning lessons remove less than a fraction \(\varepsilon\) of every \(\mathscr A_i\) and every \(\mathscr B_i\), and in the induced graph \(X_{\rm old}\):

1. the folded labelling, the padded-prefix recovery and the global uniqueness of long words (Lemma 3.1 and Proposition 5.1 of [Auxiliary incidences, deletions and recovery](auxiliary-incidences-deletions-and-recovery.md)) remain valid;
2. every nonempty cyclically reduced closed path based at height \(i\) has more than \(0.93m_i\) edges;
3. every bicycle containing a vertex of height \(i\) has at least \(1.52m_i\) edges;
4. every nonempty cyclically reduced closed path based at height \(i\) with at most \(6.04m_i\) edges is not a law in independent edge variables in \(\mathsf H\).

The expansion of the undeleted auxiliary incidences (Proposition 6.1 of [Expansion and the sequential law](expansion-and-the-sequential-law.md)) holds at the same time, and the degrees do not depend on the height.

*Proof.* For a realization of the tables, let \(Z^A_i,Z^B_i\) be the fractions of \(\mathscr A_i,\mathscr B_i\) removed by the two deletions. A counted object of length \(\ell\) rooted at height \(j\) meets layer \(i\) only if \(|i-j|\le\ell\), and \(\ell\le4H_j/s\) (coherent returns have \(p\le2H_j/s\), thetas \(e<1.52H_j/(0.50005s)\)). Since \(H_j=H_i+b(j-i)\) and \(s\ge20b\), this gives \(|i-j|\le5H_i/s\) and \(|H_j-H_i|\le5bH_i/s\), and the object has at most \(5H_i/s+1\) vertices. Lemma 4.1 of the previous lesson and Lemma 4.1 above, summed over at most \(10H_i/s+1\) root layers and the lengths, and divided by \(|\mathscr B_i|=2^{H_i}\) or \(|\mathscr A_i|\ge2^{H_i}\), give
\[
\mathbb E(Z^A_i+Z^B_i)\le2^{-0.01H_i} :
\]
the larger bound contributes \(2^{-0.025H_i+0.975\cdot5bH_i/s}\) times a polynomial in \(H_i\), and for small \(b/s\) and large \(H_0\) this is at most \(2^{-0.01H_i}\). As \(H_i=H_0+bi\),
\[
\sum_{i\ge0}\mathbb E(Z^A_i+Z^B_i)\le\frac{2^{-0.01H_0}}{1-2^{-0.01b}} ,
\]
which is less than \(\varepsilon/2\) for large \(H_0\). By Markov's inequality, with positive probability \(\sum_i(Z^A_i+Z^B_i)<\varepsilon\), and then each fraction is below \(\varepsilon\). Every realization in the support of the sequential law has the expansion property, so choose one in this event; the gate and separation deletions are separately small by Proposition 5.1 of the lesson on auxiliary incidences.

(1) Passing to an induced subgraph keeps foldedness, and a word that occurred at most once still occurs at most once; recovery along paths of the subgraph is recovery along paths of \(X^{\rm good}\). (2) is Lemma 4.2 of the previous lesson, since \(X_{\rm old}\subseteq X^{(1)}\). (3) is the definition of the second deletion: a bicycle of \(X_{\rm old}\) is a bicycle of \(X^{(1)}\), and if it had fewer than \(1.52m_i\) edges for a vertex of height \(i\), its vertices would have been deleted.

(4) Let \(W\) be a nonempty cyclically reduced closed path of length \(L\le6.04m_i\) based at height \(i\). Every vertex \(v\) of its support has \(m(v)\ge m_i-aL\ge(1-6.04a)m_i\). If \(W\) were an \(\mathsf H\)-law, Theorem 4.1 of [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md) would give a bicycle \(B\) in its support with \(L\ge4|E(B)|\). By (3) at a vertex of \(B\), \(|E(B)|\ge1.52(1-6.04a)m_i\), hence
\[
L\ge6.08(1-6.04a)m_i>6.04m_i ,
\]
since \(a\le10^{-6}\); a contradiction. The edge variables are independent for different underlying edges, and a reverse traversal uses the inverse of the same variable, as in that theorem. \(\square\)

## 6. Exercises

**Exercise 6.1.** Verify the identity (3.1) and show that, for pairwise distinct \(c_1,c_2,c_3\), three values \(E_1,E_2,E_3\) satisfy (3.1) if and only if they are evaluations \(v+c_ku\) of one pair \((u,v)\).

**Exercise 6.2.** Compute the coefficient \(0.501\cdot1.52/0.50005-0.64\), and find the largest bicycle bound \(\beta\) (in place of \(1.52\)) for which the same estimate stays below \(0.95\).

**Exercise 6.3.** Why can the branch relations at the two branch vertices not simply be charged at every update, from the start of the streams?

**Exercise 6.4.** Show that the conclusion of Proposition 5.1(4) holds with \(6.04\) replaced by any \(\gamma<6.08\), for \(a\) small enough depending on \(\gamma\).

## 7. Solutions

**6.1.** The coefficients of \(v\) are \((c_2-c_3)+(c_3-c_1)+(c_1-c_2)=0\); those of \(u\) are
\[
\begin{gathered}
(c_2-c_3)c_1+(c_3-c_1)c_2\\
{}+(c_1-c_2)c_3=0 .
\end{gathered}
\]
Conversely, given \(E_1,E_2\), the pair \(u=(c_1-c_2)^{-1}(E_1-E_2)\), \(v=E_1-c_1u\) is the unique solution of the first two equations, and (3.1) then says \((c_1-c_2)(E_3-v-c_3u)=0\).

**6.2.** \(0.501\cdot1.52=0.76152\), divided by \(0.50005\) gives \(1.52289\ldots\), minus \(0.64\) gives \(0.88289\ldots\). The condition \(0.501\beta/0.50005-0.64<0.95\) gives \(\beta<1.5869\ldots\).

**6.3.** At early updates the two branch vertices may share a key: a shared key identifies their prefixes only to the depth of that update, too small to produce a coherent return between them. Then the two relations may involve the same table, and their joint probability need not be \(2^{-2s}\). Beyond depth \(0.65H\) Lemma 2.1 excludes shared keys.

**6.4.** The argument gives \(L\ge6.08(1-\gamma a)m_i\), which exceeds \(\gamma m_i\) as soon as \(a<(6.08-\gamma)/(6.08\gamma)\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 4.6-4.8, Lemmas 4.10-4.13, Proposition 4.14. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
