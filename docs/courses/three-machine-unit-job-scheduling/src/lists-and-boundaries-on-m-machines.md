# Lists and boundaries on m machines

*Written by Claude Opus 5.5 (Anthropic) on 24 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in three separate sessions, and this lesson was planned and written from it by Claude Opus 5.5 in two further sessions and checked and finished by Claude Opus 5.5 in another. Public domain (CC0).*

[Unit jobs on m machines](unit-jobs-on-m-machines.md) set up the construction of the hierarchy for slots of \(m\) jobs. Its Proposition 5.1 supplies nodes, centers, sides, walks, and children with edge data. This lesson gives every child its list of upsets and proves the invariants (I1)–(I3) for it.

The objects used here are taken unchanged from three three-machine lessons:

- the carry, pruning, injection and switch pair of [Carried and pruned lists](carried-and-pruned-lists.md);
- the sets \(H^*\) and \(G\) of [Changing direction](changing-direction.md);
- the exchange arguments of [Boundary invariants](boundary-invariants.md).

Those lessons were written with triples, so their proofs are given here in full for slots of \(m\) jobs. They use slots only as antichains, with one exception: the bound on the number of injections. There each surviving injection is witnessed by a different job of an \(m\)-job slot.

The numerical bounds therefore depend on \(m\). A list has at most \(m\) injection entries and at most \(m+2\) entries in all, and every entry has a formula with at most \(3m+7\) leaves. Only one entry of a list can need more than three leaves. For this reason the union of a list has a formula with at most
\[
A_m=6m+9
\]
leaves, a bound linear in \(m\). [Every fixed number of machines](every-fixed-number-of-machines.md) turns these bounds into global descriptions.

## 1. Carried and pruned lists

**The data.** Fix \(m\geq1\). Nodes, tags, lists, qualifiers, keys and the invariants are those of Section 1 of [Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md), for slots of \(m\) jobs.

A node \(W\) has a tag frame, boundaries \(a,b\) in that frame, and a list \(\mathcal K=(K_1,\ldots,K_\ell)\) of upsets of \(J\) in that frame. Its qualifier set is \(\mathcal Q(\mathcal K)=K_1\cup\cdots\cup K_\ell\), and its old high set is \(O=W\cap\mathcal Q(\mathcal K)\). A qualifier \(x\) has the key
\[
\operatorname{key}(x)=\bigl(\max\{i:x\in K_i\},\lambda(x)\bigr),
\]
ordered lexicographically, where \(\lambda\) is the rank in the tag frame. The node satisfies the following invariants.

- **(I1)** \(O\subseteq P_b\) and \(W\setminus O\subseteq D_a\).
- **(I2)** Every qualifier scheduled at or before \(a\) lies in \(\widehat P_a\).
- **(I3)** Replace the slots of \(W\) by any full schedule of \(W\). Let \(x\in W\setminus D_a\), and let \(y\) be a qualifier in the slot \(a\) with \(\operatorname{key}(x)<\operatorname{key}(y)\). Then exchanging \(x\) and \(y\) does not give a full schedule of \(J\).

A side of \(W\) has a working frame. On a side, the letters \(a,b\) denote the boundaries of \(W\) in that frame, and
\[
X=W\setminus D_a,\qquad Y=W\setminus P_b.
\]
The side has the following data:

- walk cutoffs \(S_0\subseteq\cdots\subseteq S_q=S_*\);
- the open part \(E\) between \(a\) and the center \(v\), normalized for the side's priority order;
- positions \(a=s_0\leq\cdots\leq s_q<s_{q+1}=v\).

A child \(W'\) on this side has edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\), and its tag is the working frame of the side. Ranks, cones, upsets and the words "before" and "after" refer to the working frame unless another frame is named.

The following facts are proved for \(m\)-job slots in Proposition 5.1 and Lemma 3.1(a) of *Unit jobs on m machines*. That proposition establishes Lemmas 1.1, 2.1, 3.1, 4.1 and 4.2 of *Centers, sides and edge cutoffs*.

- **(F1)** If \(x\) qualifies and \(x\prec y\), then \(y\) qualifies and \(\operatorname{key}(x)<\operatorname{key}(y)\).
- **(F2)** In either frame, \(X\subseteq P_b\) and \(Y\subseteq D_a\).
- **(F3)** *Same side.* \(W=S_0\mathbin{\dot\cup}O\mathbin{\dot\cup}Y\) with \(S_0=(W\setminus O)\cap P_b\). The priority order lists \(S_0\) by rank, then \(O\) by key, then \(Y\) by rank, and the jobs of \(O\) are promoted in key order.
  *Switched side.* \(S_0=\varnothing\). The order lists \(X\) by rank, then \(W\cap D_a\) by rank, and the jobs of \(X\) are promoted in rank order.
  *Both sides.* Every \(S_i\) is a prefix of the priority order with \(S_i\subseteq P_b\), and \(S_0\subseteq D_a\).
- **(F4)** For \(0\leq i<q\), both \(s_i\) and \(s_{i+1}\) separate \(S_i\) on \(E\). The position \(s_q\) separates \(S_q\) on \(E\), and \(v\) separates \(S_*\) on \(W\).
- **(F5)** The endpoint \(b'\) is a slot of \(W\), and \(a'\) is \(a\) or a slot of \(E\). Moreover \(W'\subseteq E\),
  \[
  \begin{gathered}
  W'\cap S\subseteq D_{a'}\cap P_b,\\
  W'\setminus S\subseteq P_{b'},
  \end{gathered}
  \]
  and the root has no switched-side child.
- **(F6)** Let \(c\) be a slot. Jobs of \(P_c\) lie strictly before \(c\), jobs of \(D_c\) lie strictly after \(c\), and no job of \(c\) lies in either cone.

**Standing hypothesis.** In Sections 1–4, \(W\) is a node such that \(W\) and all its ancestors carry lists of upsets and satisfy (I1)–(I3). "The current schedule" is the witnessing schedule of \(W\) after its center has been chosen and its sides have been normalized. Proposition 4.2 shows, by induction from the root, that the hypothesis holds at every node.

**Carrying and pruning.** For \(1\leq d\leq\ell\) and \(0\leq r\leq N+1\) put
\[
\begin{aligned}
&\operatorname{carry}_{d,r}(\mathcal K)\\
&\quad=\bigl(K_d\cap\{\lambda\geq r\},\\
&\qquad\quad K_{d+1},\ldots,K_\ell\bigr).
\end{aligned}
\]
To *prune* a list on \(W'\) means to delete every entry disjoint from \(W'\) and to keep the order of the others.

**The two updates.**

- *Same update.* If \(O\setminus S=\varnothing\), the *carry* is the empty list. Otherwise let \((d,r)\) be the least key of a job of \(O\setminus S\), and let the carry be \(\operatorname{carry}_{d,r}(\mathcal K)\). Append the *injection*
  \[
  I=D_a\setminus P_b
  \]
  as the last entry, and prune on \(W'\).
- *Switched update.* The old list is discarded. Let \(G\subseteq J\) be an upset of the working frame such that \(X\subseteq G\) and no job of \(G\) is scheduled at or before \(a\) in the current schedule. Lemma 3.3 constructs such a set. Let \(h\) be the least rank of a job of \(X\setminus S\), or \(h=N+1\) if \(X\subseteq S\). The new list is the *switch pair*
  \[
  \bigl(G\cap\{\lambda\geq h\},\ D_a\bigr),
  \]
  pruned on \(W'\).

**Runs.** A *run* is a chain of nodes along one branch of the hierarchy. It starts at the root or at a child created on a switched side, and it continues through children created on same sides. A same-side child has the tag of its parent, so all nodes of a run have the same tag, the *run's frame*.

The *initial entries* of a run are the root's entry \(J\), or the two entries of the switch pair that created its first node. An entry is *descended* from a set if it arises from that set by finitely many intersections with rank suffixes. An *injection entry* is an entry descended from an injection appended at an edge of the run.

**Proposition 1.1 (lists on m machines).** Let \(m\geq1\).

- (a) Let \(1\leq d\leq\ell\) and \(0\leq r\leq N+1\). The entries of \(\operatorname{carry}_{d,r}(\mathcal K)\) are upsets. Its qualifiers are exactly the qualifiers of \(\mathcal K\) whose key is at least \((d,r)\), and on them the new keys are ordered like the old keys.
- (b) Prune a list on \(W'\). Let \(x\in W'\) and \(y\in J\) be qualifiers of the pruned list such that the pruned key of \(x\) is smaller than the pruned key of \(y\). Then the key of \(x\) was smaller than the key of \(y\) before pruning.
- (c) Consider a same update, or a switched update built from an upset \(G\) as above. Before pruning:
  - every entry is an upset of \(J\) in the working frame;
  - the qualifiers in \(W\) are exactly the jobs of \(W\setminus S\);
  - on \(W\setminus S\) the key order is the side's priority order;
  - on a same side, the union of the carry meets \(W\) exactly in \(O\setminus S\), and the injection meets \(W\) exactly in \(Y\).

  After pruning on \(W'\), the qualifiers in \(W'\) are exactly the jobs of \(W'\setminus S\), and \(W'\) satisfies (I1) in its tag frame.
- (d) Every entry of the list of a node of a run is an initial entry of the run or an injection appended at an edge of the run, intersected with at most one rank suffix \(\{\lambda\geq r\}\) of the run's frame. Different entries of one list descend from different such sets.

*Proof.* (a) Let \(x\) be a qualifier of \(\mathcal K\) whose largest index is \(j\).

- If \(j>d\), the entry \(K_j\) is kept, so \(x\) qualifies.
- If \(j=d\), the job \(x\) lies in no kept entry except possibly the first, so it qualifies exactly when \(\lambda(x)\geq r\).
- If \(j<d\), it lies in no kept entry.

So the new qualifiers are those with \((j,\lambda(x))\geq(d,r)\). For each of them the entry that gives its largest index is kept, with the index lowered by \(d-1\). This shift is the same for all of them and the ranks are unchanged, so the order is preserved. A rank suffix is an upset, so \(K_d\cap\{\lambda\geq r\}\) is an upset.

(b) Use the indices before pruning. Let \(M(z)\) be the largest index of an entry containing \(z\), and \(R(z)\) the largest index of a kept entry containing \(z\). Every entry containing \(x\) meets \(W'\) and is kept, so \(R(x)=M(x)\). Also \(R(y)\leq M(y)\), and renumbering the kept entries preserves their order.

- If \(R(x)<R(y)\), then \(M(x)<M(y)\).
- If \(R(x)=R(y)\) and \(\lambda(x)<\lambda(y)\), then either \(M(x)<M(y)\), or \(M(x)=M(y)\) and the ranks decide.

In both cases the old key of \(x\) is smaller.

(c) *Same update.* The working frame is the tag frame of \(W\).

1. By (F3), \(S=S_0\cup(O\cap S)\), with \(S_0\cap O=\varnothing\), and \(O\cap S\) is an initial segment of \(O\) in key order. If \(O\setminus S\neq\varnothing\), it is therefore the set of jobs of \(O\) with key at least \((d,r)\).
2. A job of \(W\) that qualifies through the carry is an old qualifier, so it lies in \(O\), and by (a) its key is at least \((d,r)\). Hence the carry union meets \(W\) exactly in \(O\setminus S\), with the old key order. This also holds when the carry is empty.
3. By (F2), \(Y\subseteq D_a\), so \(W\cap I=(W\cap D_a)\setminus P_b=Y\).
4. The jobs of \(Y\) are not in \(O\subseteq P_b\), so none of them qualifies through the carry. Their largest index is that of the last entry, \(I\), and their keys therefore exceed the keys of all carried jobs.
5. By (F3), \(W=S_0\mathbin{\dot\cup}O\mathbin{\dot\cup}Y\), and \(Y\cap S=\varnothing\) because \(S\subseteq P_b\). So the qualifiers in \(W\) are \((O\setminus S)\cup Y=W\setminus S\).
6. Their keys list \(O\setminus S\) by old key and then \(Y\) by rank. This is the same-side priority order restricted to \(W\setminus S\).

The entries are upsets: carried entries by (a), and \(I=D_a\cap(J\setminus P_b)\) as the intersection of an upset with the complement of a downset.

*Switched update.* The cutoff \(S\) is a rank prefix of \(X\) by (F3), so
\[
X\setminus S=X\cap\{\lambda\geq h\}.
\]

1. The first entry contains \(X\setminus S\), because \(X\subseteq G\). It contains no job of \(S\), because \(S\subseteq X\) and the jobs of \(S\) have rank smaller than \(h\).
2. The jobs of \(X\) are not in \(D_a\). So within \(X\) the qualifiers are exactly \(X\setminus S\), each with largest index \(1\).
3. The second entry contains all of \(W\cap D_a=W\setminus X\). Its index \(2\) puts these jobs after \(X\setminus S\) in key order, whether or not they also lie in the first entry.
4. Hence the qualifiers in \(W\) are \((X\setminus S)\cup(W\setminus X)=W\setminus S\). They are ordered by rank within \(X\setminus S\) and then by rank within \(W\cap D_a\), which is the switched priority order restricted to \(W\setminus S\).

Both entries are upsets.

*After pruning.* Pruning does not change which jobs of \(W'\) qualify. Since \(W'\subseteq W\), the qualifiers in \(W'\) are \(W'\setminus S\), so the child's old high set is \(O'=W'\setminus S\). By (F5), \(O'\subseteq P_{b'}\) and \(W'\setminus O'=W'\cap S\subseteq D_{a'}\). This is (I1) for \(W'\), whose boundaries in its tag frame are \(a'\) and \(b'\).

(d) Induct along the run. The first list of a run consists of its initial entries, possibly pruned. A same update does three things to the entries of the parent: it keeps them unchanged, deletes them, or intersects one of them with a rank suffix of the run's frame. It also appends a new injection. Each kept entry keeps its origin, and the appended entry has a new origin, so different entries have different origins. All rank suffixes are in the run's frame, and
\[
\{\lambda\geq r\}\cap\{\lambda\geq r'\}=\{\lambda\geq\max(r,r')\},
\]
so one suffix suffices. \(\square\)

## 2. The length of a list

**Lemma 2.1 (at most m injections).** Let \(W'\) be a child of \(W\).

- (i) If \(W'\) is created by a same update, its pruned list has at most \(m\) injection entries.
- (ii) The pruned list of \(W'\) has at most \(m+2\) entries, of which at most two are initial entries.
- (iii) The list formed at a same update, before pruning, has at most \(m+3\) entries.
- (iv) A carry taken from the list of a node has at most \(m\) injection entries and at most two initial entries.

*Proof.* (i) **Disjointness inside \(W\).** Let \(K_1,K_2\) be two different injection entries of the list of \(W'\) before pruning. Their origins are injections appended at two different edges of the run, both on the branch through \(W\). One of these edges may be \(W\to W'\) itself.

Let \(U\to U'\) be the later of the two edges, and say it is the origin of \(K_2\). Then \(W\subseteq U\), and \(U\) is a node of the run. When the injection \(D_{a_U}\setminus P_{b_U}\) was appended, the entry from which \(K_1\) descends was an entry of the carry formed at \(U\to U'\). Here \(a_U,b_U\) are the boundaries of \(U\) in its tag frame, which is the working frame of that same edge.

By Proposition 1.1(c) applied at \(U\), the carry union meets \(U\) only in \(O_U\setminus S_U\). By (I1) for \(U\), this set lies in \(P_{b_U}\). The injection meets \(U\) only in \(U\setminus P_{b_U}\). After that edge, entries only shrink. Since \(W\subseteq U\), it follows that
\[
K_1\cap K_2\cap W=\varnothing.
\]

**A witness map.** Let \(\mathscr I\) be the set of injection entries that survive pruning on \(W'\). For \(K\in\mathscr I\), let \(x_K\) be the job of least rank in \(K\cap W'\), which is nonempty. The job \(x_K\) qualifies and lies in \(W'\), so it is high by Proposition 1.1(c), and \(x_K\in P_{b'}\) by (F5). Let \(f(K)\) be the job of least rank in the slot \(b'\) that is a successor of \(x_K\). This defines a map
\[
f:\mathscr I\to b'.
\]
Since \(K\) is an upset of all of \(J\), \(f(K)\in K\). Since \(b'\) is a slot of \(W\) by (F5), \(f(K)\in W\). If \(f(K_1)=f(K_2)\) for \(K_1\neq K_2\), that job would lie in \(K_1\cap K_2\cap W=\varnothing\). So \(f\) is injective, and
\[
|\mathscr I|\leq|b'|=m.
\]

(ii) A run has at most two initial entries, and by Proposition 1.1(d) different entries of a list have different origins. A child created by a switched update has only initial entries. A child created by a same update has at most two initial entries and, by (i), at most \(m\) injection entries.

(iv) The root's list has one entry, and the list of any other node satisfies (ii). A carry keeps a suffix of the list and intersects one entry with a rank suffix, which keeps its origin.

(iii) This follows from (iv) applied to the list of \(W\): a carry has at most \(m+2\) entries, and one injection is appended. \(\square\)

The argument uses that the entries are upsets of all of \(J\), because the witness \(f(K)\) lies in \(b'\), outside \(W'\). It also uses (I1) at earlier nodes of the run. It does not use any formula size.

## 3. Changing direction

**Lemma 3.1 (local flattening).** Suppose a run begins with a child created on a switched side of a node \(Q_0\). In the run's frame, let \(a_0\) be the boundary of \(Q_0\) before it, and let the initial entries be
\[
G_0\cap\{\lambda\geq h_0\},\qquad D_{a_0},
\]
where \(G_0\) is an upset with \(Q_0\setminus D_{a_0}\subseteq G_0\). Let \(U\subseteq Q_0\) be a node of the run. Suppose a carry formed at a same update out of \(U\) contains the entry descended from the first initial entry, in the form \(G_0\cap\{\lambda\geq k\}\). Then the union of the carried entries descended from the two initial entries agrees on \(U\) with the upset
\[
D_{a_0}\cup\{\lambda\geq k\}.
\]

*Proof.* Entries keep their order and new entries are appended last. So while the first initial entry is present, it is the first entry of every list. A carry with \(d\geq2\) would delete it, and deletions are permanent.

The first initial entry is present in the given carry. Hence every carry along the run up to this one had \(d=1\) and trimmed only the first entry. So the descendant of the second initial entry is in one of two states:

- it is still exactly \(D_{a_0}\); or
- it was deleted by pruning on a node of the run containing \(U\). Then \(D_{a_0}\) is disjoint from that node, and hence from \(U\).

On \(U\cap D_{a_0}\), the target set contains every job. In the first state the second entry selects every job there; in the second state \(U\cap D_{a_0}\) is empty.

On \(U\setminus D_{a_0}\), the target set selects the jobs with \(\lambda\geq k\). These jobs lie in \(Q_0\setminus D_{a_0}\subseteq G_0\), so the first entry also selects exactly the jobs with \(\lambda\geq k\), and the second entry selects none.

Both sets in \(D_{a_0}\cup\{\lambda\geq k\}\) are upsets. \(\square\)

The agreement holds on \(U\) only. Outside \(U\) the two sets may differ.

**Lemma 3.2 (short extension of an earlier low set).** Let \(U\to W\) be an edge with low cutoff \(H\subseteq U\) in its working frame, and let \(a_U,b_U\) be the boundaries of \(U\) in that frame. There is a downset \(H^*\) of \(J\) in that frame with
\[
H^*\cap U=H,
\]
described by a formula with at most \(3m+3\) leaves.

- On a switched side, \(H^*=(J\setminus D_{a_U})\cap\{\lambda\leq r\}\).
- On a same side, \(H^*=P_{b_U}\cap(J\setminus\Phi')\), where \(\Phi'\) is an upset that agrees on \(U\) with the union \(\Phi\) of the carry formed at the edge.

*Proof.* *Switched side.* By (F3), \(H\) is a rank prefix of \(U\setminus D_{a_U}\). Let \(r\) be the largest rank in \(H\), or \(r=0\) if \(H=\varnothing\). Then \(H^*\cap U\) is the set of jobs of \(U\setminus D_{a_U}\) with rank at most \(r\), which is \(H\). The set \(H^*\) is the intersection of two downsets and has two leaves.

*Same side.* By Proposition 1.1(c), \(\Phi\cap U=O_U\setminus H\). By (F3), \(U\cap P_{b_U}=S_0\mathbin{\dot\cup}O_U\) and \(H=S_0\cup(O_U\cap H)\). Hence
\[
H=(U\cap P_{b_U})\setminus\Phi .
\]

By Lemma 2.1(iv) the carry has at most \(m\) injection entries. By Proposition 1.1(d) each of them has the form
\[
D_{a_V}\cap(J\setminus P_{b_V})\cap\{\lambda\geq r\},
\]
with at most three leaves. The carried initial entries are replaced, on \(U\), by an upset with at most two leaves:

- *Run starting at the root.* The descendant of \(J\) is \(\{\lambda\geq r\}\), with one leaf.
- *Switched run, first initial entry carried.* Replace it, together with the second initial entry if that is carried, by \(D_{a_0}\cup\{\lambda\geq k\}\). By Lemma 3.1, applicable since \(U\subseteq Q_0\), this has the same intersection with \(U\).
- *Switched run, first initial entry not carried.* The only possible initial contribution is \(D_{a_0}\) with at most one rank suffix, with at most two leaves.
- *No initial entry carried.* Omit the initial contribution.

Let \(\Phi'\) be the union of these terms, or the constant \(\varnothing\) (one leaf) if the carry is empty. Then \(\Phi'\) is an upset, \(\Phi'\cap U=\Phi\cap U\), and \(\Phi'\) has at most \(3m+2\) leaves. The set \(H^*=P_{b_U}\cap(J\setminus\Phi')\) is the intersection of two downsets. It has at most \(3m+3\) leaves and satisfies \(H^*\cap U=(U\cap P_{b_U})\setminus\Phi=H\). \(\square\)

The formula of \(H^*\) contains cone tests of slots, virtual constants and rank tests, and no earlier switch entry. Lemma 2.1 of *Changing direction* bounded the same set by \(21\) leaves for \(m=3\); the present count gives \(12\).

**Lemma 3.3 (arrangement and the switch upset).** Suppose a switched side of \(W\) produces a nonempty child.

1. \(W\) is not the root. Let \(U\) be its parent. In the working frame of the switched side, the *current frame*, write \(a_-,b_-\) for the boundaries of \(U\), \(v_-\) for the center of \(U\), and \(a,b\) for the boundaries of \(W\). Then \(a\) is a slot, and
   \[
   a_-<v_-\leq a<b\leq b_- .
   \]
2. Let \(H\) be the low cutoff of the edge \(U\to W\) and \(H^*\) the set of Lemma 3.2 for that edge, and put
   \[
   \begin{aligned}
   G={}&D_{a_-}\cap(J\setminus\widehat P_a)\\
   &\cap(J\setminus\widehat P_{v_-})\cap H^*.
   \end{aligned}
   \]
   Then \(G\) is an upset of the current frame, \(X=W\setminus D_a\subseteq G\), and no job of \(G\) is scheduled at or before \(a\) in the current schedule.

Consequently the switch pair \((G\cap\{\lambda\geq h\},D_a)\) is defined, and none of its jobs is scheduled at or before \(a\).

*Proof.* **Part 1.** By (F5) the root has no switched-side child, so \(W\) is not the root.

The edge \(U\to W\) was taken in the *old frame*, the working frame of a side of \(U\). This is the tag frame of \(W\), and it is opposite to the current frame. In the old frame, \(W\) is the gap between the positions \(a'_{\mathrm{old}}=s_i\) and \(b'_{\mathrm{old}}=s_{i+1}\) of that side. These positions satisfy
\[
\begin{gathered}
a'_{\mathrm{old}}\geq(\text{old left boundary of }U),\\
a'_{\mathrm{old}}<b'_{\mathrm{old}}\leq v_-,
\end{gathered}
\]
and \(b'_{\mathrm{old}}\) is a slot by (F5). The old right boundary of \(U\) comes after \(v_-\).

Reversing time sends:

- the old right boundary of \(U\) to \(a_-\);
- \(b'_{\mathrm{old}}\) to \(a\);
- \(a'_{\mathrm{old}}\) to \(b\);
- the old left boundary of \(U\) to \(b_-\).

This gives the displayed inequalities.

**Part 2, \(G\) is an upset.** Its four factors are upsets of the current frame:

- \(D_{a_-}\) is a cone, or a constant if \(a_-\) is virtual;
- the complements of the weak predecessor cones \(\widehat P_a\) and \(\widehat P_{v_-}\) are upsets;
- \(H^*\) is a downset of the old frame, hence an upset of the current one.

**Part 2, \(X\subseteq G\).** Let \(x\in X\).

1. If \(x\) were high at the edge \(U\to W\), (F5) would put it in the old cone \(P_{b'_{\mathrm{old}}}\), which is the current \(D_a\), contradicting \(x\in X\). So \(x\in H\).
2. By (F3), \(H\) lies in the old \(P\)-cone of the old right boundary of \(U\), which is the current \(D_{a_-}\). So \(x\in D_{a_-}\).
3. The job \(x\) is scheduled strictly after \(a\), and \(v_-\leq a\). So by (F6), \(x\) lies in neither \(\widehat P_a\) nor \(\widehat P_{v_-}\).
4. Since \(x\in W\subseteq U\) and \(H^*\cap U=H\), we have \(x\in H^*\).

**Part 2, no job of \(G\) at or before \(a\).** Let \(z\in G\) be scheduled at or before \(a\).

*Locating \(z\) in \(U\).* Since \(z\in D_{a_-}\), it is strictly after \(a_-\) by (F6); if \(a_-\) is virtual, it is the virtual boundary before the first slot and this holds trivially. Since \(z\) is at or before \(a<b\leq b_-\), it is strictly before \(b_-\). The schedule restricted to the interval of \(U\) is a full schedule of \(U\), so \(z\in U\). Only at this point is \(H^*\cap U=H\) used, and it gives \(z\in H\). The edge cutoff \(H\) lies in the center cutoff \(S_*\) of its side of \(U\).

*Case: \(z\) at or before \(v_-\) in the current frame.* In the old frame, \(z\) is at or after \(v_-\).

- If \(z\) lies in \(v_-\), then \(z\in\widehat P_{v_-}\).
- Otherwise \(z\) is a low job after the old center. The old center separates \(S_*\) on \(U\) (F4), so \(z\) lies in the old \(D_{v_-}\), which is the current \(P_{v_-}\).

*Case: \(z\) strictly after \(v_-\) and at or before \(a\).* In the old frame, \(z\) is a job of \(U\) strictly before \(v_-\), hence in the open part of that side of \(U\). It is also at or after \(b'_{\mathrm{old}}\).

- If \(z\) lies in \(b'_{\mathrm{old}}\), the current slot \(a\), then \(z\in\widehat P_a\).
- Otherwise \(b'_{\mathrm{old}}=s_{i+1}\neq v_-\). By (F4), \(s_{i+1}\) separates \(H=S_i\) on that open part, so the low job \(z\), which lies after \(s_{i+1}\), is in the old \(D_{s_{i+1}}\). This is the current \(P_a\).

Every possibility contradicts \(z\in G\).

*The schedule used.* These separator facts were proved in the schedule of \(U\) after its sides were normalized. Since then, every change on this branch has taken place inside \(W\), strictly between \(a\) and \(b\). The job \(z\), the slots \(a\), \(v_-\), \(a_-\), and the sets \(H\) and \(H^*\) are therefore unchanged, and the facts hold in the current schedule.

**The consequence.** The first entry of the switch pair lies in \(G\). The second entry, \(D_a\), contains only jobs strictly after the slot \(a\), by (F6). \(\square\)

**Lemma 3.4 (entry sizes and unions).** Every entry of a list has a formula with at most \(3m+7\) leaves. More precisely:

- an injection entry has at most \(3\) leaves;
- the root entry, and the entry descended from the second initial entry of a switched run, have at most \(2\) leaves;
- the entry descended from the first initial entry of a switched run has at most \(3m+7\) leaves.

The union of the list of a node, or of a carry taken from it, has a formula with at most
\[
A_m=6m+9
\]
leaves. If the union is empty, the constant false is used, with one leaf.

*Proof.* The first two bounds follow from Proposition 1.1(d) and the definitions of \(I\), \(J\) and \(D_{a_0}\). By Lemma 3.2, the set \(G\) has at most \(3+(3m+3)=3m+6\) leaves, and the first entry of the switch pair adds one rank test. Further rank suffixes merge with that one (Proposition 1.1(d)), and a new run discards the old list, so formulas never nest.

By Proposition 1.1(d), different entries of a list have different origins. A list therefore contains at most one entry descended from each initial entry, and by Lemma 2.1 at most \(m\) injection entries. In a switched run the union has at most
\[
3m+(3m+7)+2=6m+9
\]
leaves. In a run starting at the root it has at most \(3m+1\). A carry consists of entries of the list, one of them trimmed by a rank suffix that merges with its existing suffix, so the same bound holds. \(\square\)

The bound of \(25\) leaves per entry in Lemma 4.1 of *Changing direction* rests on the count of five carry terms of four leaves each, which is specific to three machines. For \(m=3\) the present bounds are \(16\) leaves per entry and \(27\) per union, against the \(125\) of Lemma 4.1 of [Global descriptions and the running time](global-descriptions-and-the-running-time.md).

## 4. Boundary invariants

The preparatory reorderings of \(W\) (choosing the center and normalizing the sides) keep the invariants of \(W\), for three reasons:

- (I1) concerns the job set of \(W\) and fixed subsets of \(J\);
- (I2) concerns the jobs at or before \(a\) and the slot \(a\), none of which moves;
- (I3) quantifies over all full schedules of \(W\) placed in its slots.

**Proposition 4.1 ((I2) and (I3) for children).** Let \(W'\) be a child of \(W\) with edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\), carrying its pruned list. In the child's tag frame:

- **(I2)** Every qualifier scheduled at or before \(a'\) lies in \(\widehat P_{a'}\).
- **(I3)** Replace the slots of \(W'\) by any full schedule of \(W'\). Let \(x\in W'\setminus D_{a'}\), and let \(y\) be a qualifier in the slot \(a'\) whose child key is larger than that of \(x\). Then exchanging \(x\) and \(y\) does not give a full schedule of \(J\).

*Proof of (I2).* Pruning only removes qualifiers, so let \(z\) be a qualifier of the list before pruning, scheduled at or before \(a'\).

*Case 1: \(z\) strictly after \(a\).* Then \(a'\neq a\), so \(a'\) is a slot of \(E\), and \(z\in E\subseteq W\). By Proposition 1.1(c), \(z\) is high for \(S\).

- If \(z\) lies in \(a'\), then \(z\in\widehat P_{a'}\).
- Otherwise \(z\) is a high job before \(a'\). By (F4), \(a'=s_i\) with \(i\geq1\) separates \(S_i\) on \(E\), so condition (a) gives \(z\in P_{a'}\).

*Case 2: \(z\) at or before \(a\).*

**Reduction to the carry.** Here \(a\) is a slot. The injection \(I\subseteq D_a\) contains no job at or before \(a\) by (F6), and neither entry of a switch pair does, by Lemma 3.3. So the update is a same update and \(z\) qualifies through the carry. By Proposition 1.1(a), \(z\) is a qualifier of the list of \(W\), whose tag frame is the working frame. By (I2) for \(W\), there is a job \(y\) in the slot \(a\) with \(z=y\) or \(z\prec y\). The carry union is an upset, so \(y\) qualifies through the carry. By Proposition 1.1(a), the carry is nonempty and \(\operatorname{key}(y)\geq(d,r)\).

If \(a'=a\), then \(z\in\widehat P_{a'}\) and we are done. Assume \(a'>a\).

**The advances of the walk.** Consider every advance of the walk from \(a\) to \(s_i=a'\), including advances whose end positions are not marks. An advance during promotion \(j\leq i\) is an advance of the walk at the fixed cutoff \(L=S_j\cap E\) on the domain \(E\) (Lemma 3.3 of [Separators and the shared-cutoff walk](separators-and-the-shared-cutoff-walk.md), valid for \(m\)-job slots by Proposition 4.3 of *Unit jobs on m machines*).

The carry union meets \(W\) in \(O\setminus S_i\subseteq W\setminus S_j\). So every carry qualifier in \(E\) is high for every cutoff used. We show that each position reached is a slot containing a carry qualifier that is a successor of \(y\).

**The first advance.** It goes from \(a\) to the earliest slot \(t\) of \(E\) containing an exception \(x\) for \(S_j\) at \(a\): a job of \(S_j\cap E\) after \(a\) that is not in \(D_a\).

1. *Every predecessor \(w\in J\) of \(x\) is strictly before \(a\).* The job \(w\) is before \(t\).
   - If \(w\) lay in \(a\), then \(x\in D_a\).
   - If \(w\) lay strictly between \(a\) and \(t\), it would be a job of \(E\). It would lie in \(S_j\), because \(S_j\) is a prefix of an order extending \(\prec\) and \(x\in S_j\). Since \(t\) is the earliest slot with an exception, \(w\) is not an exception, so \(w\in D_a\) and again \(x\in D_a\).

   Both cases contradict the choice of \(x\).
2. *\(\operatorname{key}(x)<\operatorname{key}(y)\) in the list of \(W\).* Since \(x\in W\setminus D_a\), (I1) gives \(x\in O\). Since \(S_0\subseteq D_a\), we have \(x\notin S_0\). As \(x\in S_j\subseteq S_i\), the job \(x\) belongs to \(O\cap S_i\), the jobs of \(O\) promoted by stage \(i\). These are promoted in key order, so \(\operatorname{key}(x)<(d,r)\leq\operatorname{key}(y)\).
3. *The exchange is forbidden.* The current schedule of \(W\) is a full schedule of \(W\) in its slots (Lemma 2.2 of *Unit jobs on m machines*). The job \(x\) lies in \(W\setminus D_a\), and \(y\) is a qualifier in \(a\) with a larger key. So by (I3) for \(W\), exchanging \(x\) and \(y\) does not give a full schedule of \(J\).
4. *\(y\) has a successor at or before \(t\).* Suppose not, and exchange \(x\) and \(y\); each slot keeps \(m\) jobs. We check every relation involving a moved job.
   - The predecessors of \(x\) lie strictly before \(a\) by item 1, and its successors lie strictly after \(t\). So no job of \(a\), including \(y\), is comparable with \(x\).
   - The predecessors of \(y\) lie strictly before \(a\), and by assumption its successors lie strictly after \(t\). So no job of \(t\) is comparable with \(y\).
   - All other pairs keep their slots.

   The result would be a full schedule of \(J\), contradicting item 3. So \(y\) has a successor \(y_1\) strictly after \(a\) and at or before \(t\). This \(y_1\) lies in \(E\) and qualifies through the carry, because the carry union is an upset.
5. *A successor at \(t\).* If \(y_1\) lies in \(t\), we are done. Otherwise apply Lemma 3.1(2) of *Separators and the shared-cutoff walk* (Proposition 4.3 of *Unit jobs on m machines*) on the domain \(E\), with \(M=L=S_j\cap E\) and \(s=a\). Its hypotheses hold:
   - condition (a) at the boundary \(a\) is empty;
   - \(t\) is the earliest slot with an exception;
   - \(x\in L\);
   - \(y_1\) is a high job at a slot \(r\) of \(E\) with \(r<t\).

   The lemma gives a successor of \(y_1\) in the slot \(t\). It qualifies through the carry and succeeds \(y\).

**Later advances.** An advance from a slot \(s\) of \(E\) to a slot \(t'\), during promotion \(j'\leq i\), uses the cutoff \(L=S_{j'}\cap E\), and its exception lies in \(L\). The position \(s\) satisfies condition (a) for \(L\), for one of two reasons:

- \(s=s_{j'-1}\), which separates \(S_{j'-1}\) by (F4), and the high jobs for \(S_{j'}\) are among those for \(S_{j'-1}\);
- \(s\) is the target of an earlier advance at the same cutoff, which satisfies (a) by Lemma 3.1(3) of *Separators and the shared-cutoff walk*.

By the inductive claim, \(s\) contains a carry qualifier \(c\) with \(y\prec c\). Since \(c\) is high, Lemma 3.1(2) there, with \(M=L\), gives a successor of \(c\) in \(t'\). It qualifies through the carry.

**Conclusion.** By induction along the advances, the slot \(a'\) contains a successor of \(y\). Since \(z=y\) or \(z\prec y\), we get \(z\in P_{a'}\subseteq\widehat P_{a'}\). \(\square\)

*Proof of (I3).* By (I1) for the child (Proposition 1.1(c)), \(x\) is a qualifier, and \(x\in W'\). By Proposition 1.1(b), the key of \(x\) is smaller than that of \(y\) already before pruning.

*Case \(a'>a\).* The slot \(a'\) lies in \(E\), so \(x,y\in W\). Both qualify before pruning, so both lie in \(W\setminus S\), where the key order is the side's priority order (Proposition 1.1(c)). Hence \(x\) has better priority than \(y\).

The replacement of \(W'\) changes only slots of \(E\) strictly after \(a'\) and leaves a full schedule of \(E\). Suppose the exchange gave a full schedule of \(J\). Its slots in the interval of \(E\) would form a full schedule of \(E\). That schedule arises from the normalized one by reordering the slots after \(a'\) and then exchanging \(y\), in \(a'\), with the later job \(x\) of better priority. This contradicts Lemma 4.2 of *Unit jobs on m machines* with \(r=a'\).

*Case \(a'=a\), switched update.* The pruned entries lie in the switch pair. By Lemma 3.3 no qualifier lies in the slot \(a\), so there is no \(y\).

*Case \(a'=a\), same update.* We have \(x\notin D_a\) by hypothesis, and \(y\notin D_a\) by (F6). So neither lies in the injection, and both qualify through the carry entries alone. Their keys before pruning are their keys in the carry, and by Proposition 1.1(a) these compare like their keys in the list of \(W\). Moreover \(x\in W\setminus D_a\), and \(y\) is a qualifier of the list of \(W\) in \(a\). The preparatory reorderings of \(W\), followed by the replacement of \(W'\), form a full schedule of \(W\) in its slots. So (I3) for \(W\) forbids the exchange. \(\square\)

**Proposition 4.2 (validity on m machines).** Start from any full schedule of \(J\) on \(m\) machines.

- The construction is defined at every node.
- The root's list has one entry. Every other list is pruned and has at most \(m+2\) entries, each with a formula of at most \(3m+7\) leaves, and its union has a formula of at most \(6m+9\) leaves.
- Every node satisfies (I1)–(I3).
- Every branch has at most \(N/m\) nodes, and the tree is finite.

*Proof.* Induct from the root. Its list is \((J)\). Invariant (I1) holds by the virtual conventions, and (I2) and (I3) are empty (Section 1 of *Centers, sides and edge cutoffs*).

Let \(W\) be a node such that \(W\) and its ancestors satisfy the claims, which is the standing hypothesis. The preparatory reorderings keep the invariants of \(W\). Proposition 5.1 of *Unit jobs on m machines* supplies the center, the normalized sides, the walks and the children with their edge data.

A same update uses only the list of \(W\). A switched update uses the set \(G\) of Lemma 3.3, which is built from data that already exist:

- the edge \(U\to W\) and its cutoff;
- the carry formed at that edge;
- through Lemma 3.1, the initial entries of the run of \(U\).

For each child, the claims follow from the results above:

- Proposition 1.1(c) gives its qualifiers and (I1);
- Lemma 2.1 gives the length of its list, using only the qualifier identity, upsets, and (I1) at nodes of the run;
- Lemma 3.4 gives the sizes;
- Proposition 4.1 gives (I2) and (I3), using the invariants of \(W\).

No step uses a statement about a deeper node.

A child misses the center of its parent, so its number of slots is smaller than that of its parent. The root has \(N/m\) slots and every node has at least one, so a branch has at most \(N/m\) nodes. Every node has finitely many children, so the tree is finite. \(\square\)

## 5. Exercises

**5.1.** For \(m=3\), compute the bounds of Lemmas 3.2 and 3.4 and compare them with the bounds \(21\), \(25\) and \(125\) of *Changing direction* and *Global descriptions and the running time*. Which step of *Changing direction* is coarser?

**5.2.** Show that \((m+2)(3m+7)\) is also a valid bound for the union of a list. The count of Lemma 4.1 of *Global descriptions and the running time* gives a leaf budget \(2A+7\) when \(A\) bounds every list or carry union. The accounting of Proposition 5.1 there, with triples replaced by \(m\)-job slots, gives a running time \(N^{5mK+4m+1}\) for a budget \(K\). Compute the exponent obtained from \(A=(m+2)(3m+7)\), and compare it with the one obtained from \(A_m=6m+9\).

**5.3.** In the proof of Lemma 2.1, why must \(f(K)\) be taken in \(W\) and not in \(W'\)?

**5.4.** Why may the formula of \(H^*\) use the flattened set of Lemma 3.1, while the qualifier union in the global description of a child (Lemma 2.1 of *Global descriptions and the running time*) must be the union of the actual entries?

**5.5.** Show that a list contains at most one entry descended from a first switch entry, and that the formula of \(G\) never contains an earlier set \(G\).

## 6. Solutions

**5.1.** For \(m=3\), Lemma 3.2 gives \(3\cdot3+3=12\) leaves for \(H^*\). Lemma 3.4 gives \(3\cdot3+7=16\) leaves per entry and \(6\cdot3+9=27\) per union.

The coarser step is the count in Lemma 2.1 of *Changing direction*, which bounds five carry terms by four leaves each. In fact at most three of the terms are injection entries, with three leaves each, and Lemma 3.1 merges the two initial entries into a single term of two leaves; this gives \(11\) leaves for \(\Phi'\).

The count \(125\) of *Global descriptions and the running time* multiplies five entries by \(25\) leaves. Only the first switch entry can need more than three leaves.

**5.2.** By Lemma 2.1, a list has at most \(m+2\) entries, and by Lemma 3.4 each has at most \(3m+7\) leaves. Joining them by unions gives a formula with at most \((m+2)(3m+7)=3m^2+13m+14\) leaves.

With this \(A\), the budget is \(K=2A+7=6m^2+26m+35\), and the exponent is
\[
\begin{aligned}
&5mK+4m+1\\
&\quad=30m^3+130m^2+179m+1,
\end{aligned}
\]
which is cubic in \(m\). For \(m=3\) it equals \(2518\).

With \(A_m=6m+9\), the budget is \(K=12m+25\), and the exponent is
\[
\begin{aligned}
&5m(12m+25)+4m+1\\
&\quad=60m^2+129m+1,
\end{aligned}
\]
which is quadratic. For \(m=3\) it equals \(928\).

**5.3.** The slot \(b'\) lies in \(W\) but outside \(W'\), since \(W'\) consists of the slots strictly between \(a'\) and \(b'\). So \(f(K)\notin W'\). Disjointness of the injection entries is proved inside \(W\), which contains \(b'\). Disjointness inside \(W'\) alone would not show that \(f\) is injective.

**5.4.** In Lemma 3.3, \(H^*\) enters only after the factor \(D_{a_-}\) and the time bound \(b\leq b_-\) have placed the job inside \(U\). From then on only \(H^*\cap U=H\) is used, and the flattened set agrees with the carried entries on \(U\).

The high part of a child's global description must equal the qualifier set of the child's list on all of \(J\). Its converse direction uses (I2) for the child, which concerns qualifiers of the actual list wherever they are scheduled at or before \(a'\). The flattened set \(D_{a_0}\cup\{\lambda\geq k\}\) may contain jobs of high rank, scheduled before \(a'\) and outside \(U\), that are neither qualifiers nor members of \(\widehat P_{a'}\). Such a job would be selected wrongly.

**5.5.** By Proposition 1.1(d), the entries of a list descend from pairwise different initial entries or injections of their run. A run has at most one switch pair, and a new run discards the old list. So at most one entry descends from a first switch entry.

The formula of \(G\) consists of three cone tests and the formula of \(H^*\). By Lemma 3.2, \(H^*\) is either a cone test intersected with a rank test, or \(P_{b_U}\cap(J\setminus\Phi')\). The terms of \(\Phi'\) are of three kinds:

- injection entries, made of cones and one rank test;
- the flattened set \(D_{a_0}\cup\{\lambda\geq k\}\), or \(D_{a_0}\) with a rank test;
- a rank suffix, or the constant false.

None of these contains an earlier \(G\).

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
- The main argument of this lesson follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
