# Every fixed number of machines

*Written by Claude Opus 5.5 (Anthropic) on 24 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in three separate sessions, and this lesson was planned and written from it by Claude Opus 5.5 in two further sessions and checked and finished by Claude Opus 5.5 in another. Public domain (CC0).*

This lesson finishes the proof that for every fixed number \(m\) of identical machines the problem \(Pm\mid\mathrm{prec},p_j=1\mid C_{\max}\) is solvable in polynomial time. It builds on two lessons:

- [Unit jobs on m machines](unit-jobs-on-m-machines.md) redoes, for slots of \(m\) jobs, the foundations, the dynamic program, the separators and the centers.
- [Lists and boundaries on m machines](lists-and-boundaries-on-m-machines.md) carries the lists and the invariants (I1)–(I3) to \(m\) machines, with leaf counts linear in \(m\).

This lesson then does the following:

- describes every child and every mark by a formula of bounded size;
- proves the structure theorem with the leaf budget \(K_m=12m+25\);
- proves that the algorithm is correct;
- derives its running time, with an explicit exponent, which proves Theorem 1.1 of *Unit jobs on m machines*;
- treats inputs that give only the number of jobs, and the case of four machines;
- lists the places where the number three entered the course.

The arguments follow [Global descriptions and the running time](global-descriptions-and-the-running-time.md) step by step; what is new is the counting. The notation is that of the three lessons just named. In particular, \(J\) is the padded set of \(N=mT\) jobs, a slot is an \(m\)-element antichain, and
\[
A_m=6m+9.
\]

## 1. Global descriptions

Throughout this section, fix the following data:

- an integer \(m\geq1\);
- a node \(W\) of the construction of Proposition 4.2 of *Lists and boundaries on m machines*, with list \(\mathcal K\) and old high set \(O\);
- one side of \(W\), with its working frame, boundaries \(a,b\) in that frame, center \(v\) and open part \(E\);
- the walk cutoffs \(S_0\subseteq\cdots\subseteq S_q=S_*\) of that side and its positions \(s_0\leq\cdots\leq s_q<s_{q+1}=v\).

"Scheduled", "before" and "after" refer to the working frame and to the schedule of \(J\) after the preparatory reorderings of \(W\): the choice of the center and the normalization of both sides. The children of \(W\) are created in this schedule, and it is their witness.

**Lemma 1.1 (cutoff predicates).** For \(0\leq i\leq q\) define a set \(\widetilde S_i\subseteq J\) as follows.

- *Same side.* If \(O\subseteq S_i\), put \(\Phi_i=\varnothing\). Otherwise let \((d,r)\) be the least key of a job of \(O\setminus S_i\), and let \(\Phi_i\) be the union of the entries of \(\operatorname{carry}_{d,r}(\mathcal K)\). Put \(\widetilde S_i=P_b\setminus\Phi_i\).
- *Switched side.* Let \(r_i\) be the rank of the job promoted at the \(i\)-th promotion, and \(r_0=0\). Put
\[
\widetilde S_i=(J\setminus D_a)\cap\{\lambda\leq r_i\}.
\]

Then \(\widetilde S_i\cap W=S_i\), and \(\widetilde S_i\) is described by a formula with at most \(A_m+1=6m+10\) leaves.

*Proof.* *Same side.* By Proposition 1.1(a) of *Lists and boundaries on m machines*, \(\Phi_i\) consists of the qualifiers of \(\mathcal K\) whose key is at least \((d,r)\). The qualifiers lying in \(W\) form \(O\).

The jobs of \(O\) are promoted in key order (Lemma 3.1 of [Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md), valid on \(m\) machines by Proposition 5.1 of *Unit jobs on m machines*). Hence \(O\cap S_i\) is an initial segment of \(O\) in key order, and \(O\setminus S_i\) consists of the jobs of \(O\) with key at least \((d,r)\). So \(\Phi_i\cap W=O\setminus S_i\). This also holds when \(O\subseteq S_i\), since then both sides are empty.

By (I1), \(O\subseteq P_b\). Hence \(W\cap P_b\) is the disjoint union of \(S_0=(W\setminus O)\cap P_b\) and \(O\), and \(S_i=S_0\cup(O\cap S_i)\). The set \(\Phi_i\cap W\) lies in \(O\), so it misses \(S_0\). Therefore
\[
\begin{aligned}
\widetilde S_i\cap W
&=(S_0\cup O)\setminus(O\setminus S_i)\\
&=S_0\cup(O\cap S_i)=S_i.
\end{aligned}
\]

For the leaf count, consider the three possible forms of \(\Phi_i\).

- If \(\mathcal K\) is a pruned list, Lemma 3.4 of *Lists and boundaries on m machines* describes the union of a carry taken from it with at most \(A_m\) leaves.
- If \(W\) is the root, then \(\mathcal K=(J)\), so \(d=1\). The carry is \((J\cap\{\lambda\geq r\})\), whose union \(\{\lambda\geq r\}\) is one leaf.
- An empty union is the constant \(\varnothing\), one leaf.

The complement of \(\Phi_i\) has a formula of the same size (Lemma 3.1(b) of *Unit jobs on m machines*). Intersecting it with the atom \(P_b\) gives at most \(A_m+1\) leaves.

*Switched side.* The jobs of \(X=W\setminus D_a\) are promoted in increasing rank. Hence \(S_i\) consists of the \(i\) jobs of \(X\) of smallest rank, that is, \(S_i=X\cap\{\lambda\leq r_i\}\); for \(i=0\) this is empty, because ranks are at least \(1\). Also \(W\cap(J\setminus D_a)=X\), so \(\widetilde S_i\cap W=S_i\). The formula has two leaves, and \(2\leq A_m+1\). \(\square\)

The predicate \(\widetilde S_i\) agrees with \(S_i\) on \(W\) only. Nothing is claimed about it outside \(W\).

**Lemma 1.2 (a child as a global set).** Let \(W'\) be a child of \(W\) on this side, with edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\) and pruned list \(\mathcal K'\). The following are equalities of subsets of \(J\), in the working frame:
\[
\begin{aligned}
W'\setminus S&=\mathcal Q(\mathcal K')\cap P_{b'}\\
&\qquad\cap(J\setminus\widehat P_{a'}),
\end{aligned}
\]
\[
\begin{aligned}
W'\cap S&=D_{a'}\cap P_b\cap(J\setminus\widehat D_{b'})\\
&\qquad\cap(J\setminus\widehat D_v)\cap\widetilde S_i.
\end{aligned}
\]

*Proof.* By Proposition 5.1 of *Unit jobs on m machines*, \(b'\) is a genuine slot of \(W\), and \(a'\) is the boundary \(a\) or a slot of \(E\). The center \(v\) is a genuine slot.

*High part.* Let \(x\in W'\setminus S\).

- By Proposition 1.1(c) of *Lists and boundaries on m machines*, the qualifiers of \(\mathcal K'\) in \(W'\) are exactly the jobs of \(W'\setminus S\). So \(x\in\mathcal Q(\mathcal K')\).
- By Proposition 5.1 of *Unit jobs on m machines*, \(x\in P_{b'}\).
- The job \(x\) is scheduled strictly after \(a'\). It is therefore neither in the slot \(a'\) nor, by Lemma 3.1(a) of *Unit jobs on m machines*, in \(P_{a'}\). If \(a'\) is virtual, \(\widehat P_{a'}=\varnothing\). So \(x\notin\widehat P_{a'}\).

Conversely, let \(x\) belong to the right-hand side.

- Since \(x\in P_{b'}\) and \(b'\) is a slot, \(x\) is scheduled strictly before \(b'\) (Lemma 3.1(a) of *Unit jobs on m machines*).
- Suppose \(x\) were scheduled at or before \(a'\), which requires \(a'\) to be a slot. As a qualifier of \(\mathcal K'\), it would lie in \(\widehat P_{a'}\) by (I2) for the child (Proposition 4.1 of *Lists and boundaries on m machines*). This contradicts the last factor.
- So \(x\) lies strictly between \(a'\) and \(b'\), that is, \(x\in W'\).
- As a qualifier lying in \(W'\), \(x\) is in \(W'\setminus S\).

*Low part.* Let \(z\) belong to the right-hand side.

1. *Placement in \(W\).* Since \(z\in D_{a'}\), it is scheduled after \(a'\), hence after \(a\); at a virtual \(a'\) the cone \(D_{a'}=J\) imposes nothing. Since \(z\in P_b\), it is scheduled before \(b\); at a virtual \(b\), \(P_b=J\). So \(z\in W\).
2. *Low.* Only at this point is Lemma 1.1 used: \(z\in\widetilde S_i\cap W=S_i\).
3. *Placement in \(E\).* By Lemma 3.1 of *Centers, sides and edge cutoffs*, \(S_i\subseteq S_*\). If \(z\) were in the center, it would lie in \(\widehat D_v\). If it were after the center, it would be a low job for \(S_*\) after \(v\). The center separates \(S_*\) on the domain \(W\), so \(z\) would lie in \(D_v\). Both are excluded, so \(z\) is scheduled before \(v\), that is, \(z\in E\).
4. *Placement in \(W'\).* If \(b'=v\), step 3 shows that \(z\) is before \(b'\). Otherwise \(b'\) is a slot of \(E\) separating \(S_i\) on \(E\) (Lemma 4.1 of *Centers, sides and edge cutoffs*, via Proposition 5.1 of *Unit jobs on m machines*). A low job of \(E\) in the slot \(b'\) lies in \(\widehat D_{b'}\), and one after \(b'\) lies in \(D_{b'}\). Both are excluded, so \(z\) is scheduled strictly between \(a'\) and \(b'\).

Hence \(z\in W'\cap S\).

Conversely, let \(z\in W'\cap S\).

- By Proposition 5.1 of *Unit jobs on m machines*, \(z\in D_{a'}\cap P_b\).
- Since \(z\in W\cap S_i\), Lemma 1.1 gives \(z\in\widetilde S_i\).
- The job \(z\) is scheduled strictly before the slots \(b'\) and \(v\). By Lemma 3.1(a) of *Unit jobs on m machines* it lies in neither \(\widehat D_{b'}\) nor \(\widehat D_v\). \(\square\)

The union of the two right-hand sides is a global description of \(W'\). It contains no description of \(W\) or of any other ancestor. The localization in the low part is an order of reasoning: the positive tests place a job inside \(W\) before the predicate \(\widetilde S_i\) is used.

**Lemma 1.3 (marks).** Put
\[
H_*=\begin{cases}P_b&\text{same side},\\ J\setminus D_a&\text{switched side},\end{cases}
\]
and recall \(B_z(H)=P_z\cup(H\setminus\widehat D_z)\) from Lemma 1.2 of [Separators and the shared-cutoff walk](separators-and-the-shared-cutoff-walk.md). For a mark \(z\) of \(W\) on this side, define a formula \(F\) as follows:

- \(F=B_v(H_*)\) if \(z=v\);
- \(F=B_v(H_*)\cap B_z(\widetilde S_i)\) if \(z=s_i\) with \(i\geq1\).

If the working frame is the forward frame, the set of jobs of \(W\) scheduled before \(z\) in original time is \(W\cap F\). If the working frame is the backward frame, this set is \(W\cap\bigl((J\setminus F)\setminus z\bigr)\).

*Proof.* We have \(H_*\cap W=S_*\). On a same side this is the definition \(S_*=W\cap P_b\); on a switched side, \(S_*=X=W\cap(J\setminus D_a)\).

The center separates \(S_*\) on the domain \(W\). By Lemma 1.2 of *Separators and the shared-cutoff walk*, valid on \(m\) machines by Proposition 4.3 of *Unit jobs on m machines*, \(B_v(H_*)\cap W\) is the set of jobs of \(W\) before \(v\) in the working frame, which is \(E\).

Let \(z=s_i\) with \(i\geq1\) be a mark, so \(z\) is a slot of \(E\). By Lemma 4.1 of *Centers, sides and edge cutoffs*, \(z\) separates \(S_i\cap E\) on \(E\). Since \(\widetilde S_i\cap E=S_i\cap E\) (Lemma 1.1), the same separator lemma, with domain \(E\), shows that \(E\cap B_z(\widetilde S_i)\) is the set of jobs of \(E\) before \(z\). The jobs of \(W\) before \(z\) lie in \(E\), because \(z\) comes before \(v\). So \(W\cap F\) is the set of jobs of \(W\) before \(z\) in the working frame.

In the forward frame this is the required set. In the backward frame, \(W\) is the disjoint union of three parts:

- its working-frame prefix \(W\cap F\);
- the slot \(z\);
- its working-frame suffix, which is the original-time prefix.

Hence \(W\cap\bigl((J\setminus F)\setminus z\bigr)\) is the original-time prefix. The complement of \(F\) has a formula of the same size by Lemma 3.1(b) of *Unit jobs on m machines*, and membership in \(z\) is one atom. \(\square\)

The center is a mark of both sides. Either side's formula serves for it.

## 2. Counts and the structure theorem

**Lemma 2.1 (leaf counts).** Every child has a global description with at most \(2A_m+7=12m+25\) leaves. Every mark has a relative description with at most \(A_m+7=6m+16\) leaves. Every atom of these formulas is one of the following: a cone of a slot, a membership test in a slot, a constant (including the cones of a virtual boundary), or a rank test in one of the two frames.

*Proof.* Both counts use Lemma 3.4 of *Lists and boundaries on m machines*, which describes the union \(\mathcal Q(\mathcal K')\) of a pruned list with at most \(A_m\) leaves.

*Global descriptions (Lemma 1.2).*

- The high part has at most \(A_m+2\) leaves: the union \(\mathcal Q(\mathcal K')\), plus the atom \(P_{b'}\) and the complemented atom \(\widehat P_{a'}\).
- The low part has four one-leaf cone tests and \(\widetilde S_i\), which has at most \(A_m+1\) leaves by Lemma 1.1. So it has at most \(A_m+5\) leaves.

Their union has at most
\[
\begin{aligned}
(A_m+2)+(A_m+5)&=2A_m+7\\
&=12m+25
\end{aligned}
\]
leaves.

*Relative descriptions (Lemma 1.3).*

- \(B_v(H_*)\) has three leaves: \(P_v\), the one-leaf \(H_*\), and the complement of \(\widehat D_v\).
- \(B_z(\widetilde S_i)\) has at most \(1+(A_m+1)+1=A_m+3\) leaves.
- So \(F\) has at most \(A_m+6\) leaves, and the backward conversion adds one membership atom. This gives \(A_m+7=6m+16\).

*Atoms.* The atoms are the following.

- Cones of the slots \(a',b',v\) and cones of the boundaries \(a,b\). These are slots or virtual boundaries, and the cones of a virtual boundary are constants.
- The atoms of the list entries. These are cones of node boundaries and of centers (in \(G\), Lemma 3.3 of *Lists and boundaries on m machines*), membership in slots, and rank thresholds in the run's frame.
- Rank thresholds in the working frame. \(\square\)

**Theorem 2.2 (structure theorem on m machines).** Let \(m\geq1\). Every full schedule of \(J\) has a bounded-description hierarchy in the sense of Definition 3.3 of *Unit jobs on m machines* with budget
\[
K_m=12m+25.
\]
In this hierarchy:

- the root is described by the constant \(J\);
- every other node has a global description with at most \(12m+25\) leaves;
- every mark has a relative description with at most \(6m+16\) leaves.

These bounds do not depend on the depth of the node.

*Proof.* Start from the given full schedule and run the construction. By Proposition 4.2 of *Lists and boundaries on m machines*, it is defined at every node, every node satisfies (I1)–(I3), and the tree is finite. We verify the conditions of the definition.

- *Rescheduling is allowed.* At each node, the choice of the center and the normalization of the two open parts replace the slots of \(W\) by a full schedule of \(W\) (Lemma 2.2 of *Unit jobs on m machines*, applied to \(W\) and to each open part). This is the rescheduling the definition allows.
- *Marks and children.* The center is marked. By Proposition 5.1 of *Unit jobs on m machines*, the children are exactly the nonempty gaps between consecutive marks and between the boundaries and the nearest marks, and each child receives a copy of the current schedule.
- *Descriptions.* The root is \(J\), one leaf. Every other node is a child, globally described by Lemma 1.2. Every mark has the relative description of Lemma 1.3.
- *Bounds.* Lemma 2.1 bounds the global descriptions by \(12m+25\) leaves and the relative descriptions by \(6m+16\leq12m+25\) leaves. \(\square\)

No step of this proof uses \(m\geq3\). That hypothesis enters only when formulas are counted (Lemma 3.1(c) of *Unit jobs on m machines*).

## 3. The algorithm and its running time

**Theorem 3.1 (correctness).** Let \(m\geq1\) and \(K\geq12m+25\). The dynamic program of *Unit jobs on m machines*, §3, with budget \(K\), accepts \(J\) if and only if \(J\) has a full schedule, and in that case it returns one. Consequently, for \(1\leq T\leq n\) with \(n\leq mT\), it decides whether \(G\) has a schedule on \(m\) machines with makespan at most \(T\). After the padding jobs are deleted and the at most \(m\) remaining jobs of each slot are assigned to machines \(1,2,\ldots\) in the order of their identifiers, the returned schedule is such a schedule.

*Proof.* *Soundness.* If the program accepts, Proposition 3.2 of *Unit jobs on m machines* produces a full schedule of \(J\).

*Completeness.* Let \(J\) have a full schedule. By Theorem 2.2 it has a hierarchy with budget \(K_m\). A formula with at most \(K_m\) leaves has at most \(K\) leaves, so this is also a hierarchy with budget \(K\). By Lemma 3.4 of *Unit jobs on m machines*, the program accepts \(J\).

*The deadline.* By the padding lemma (Lemma 2.1 of *Unit jobs on m machines*), \(J\) has a full schedule exactly when a schedule of makespan at most \(T\) exists. Deleting the padding jobs leaves at most \(m\) jobs per slot, and distinct jobs of one slot receive distinct machines. \(\square\)

**Proposition 3.2 (running time of the program).** Let \(m\geq3\) and \(K\geq1\) be fixed, and let \(N\geq m\). The program, including the construction of the witness schedule, takes
\[
O_{m,K}\bigl(N^{5mK+4m+1}\bigr)
\]
steps of a deterministic multitape Turing machine. Its input is the table of \(\prec\) on \(J\) and the rank \(\lambda:J\to\{1,\ldots,N\}\).

*Proof.* *Counting.* By Lemma 3.1(c) of *Unit jobs on m machines*, there are at most \(B=K\,512^KN^{mK}\) formulas with at most \(K\) leaves. Hence:

- \(\mathcal F_K\) has at most \(B\) members;
- for a fixed \(W\), there are at most \(B\) candidate left parts \(L=W\cap[\![F]\!]\);
- there are at most \(N^m\) sets \(Z\) of \(m\) jobs;
- so for a fixed \(W\) there are at most \(S=BN^m\) candidate states. Repetitions only enlarge this count.

*Storage.* The tapes hold the following.

- The bit vector of every set of \(\mathcal F_K\): \(BN\) bits.
- An explicit schedule of every accepted set: at most \(N\) identifiers of \(O(\log N)\) bits each.
- For the current \(W\), one record per state. A record holds the three parts as \(N\)-bit vectors, a reachability bit, and the number of its predecessor record, with \(O(\log S)=O_{m,K}(\log N)\) bits. A record therefore has \(O_{m,K}(N)\) bits.

*Elementary operations.* Every operation is done by sequential scans.

- Fetching or updating a record costs \(O_{m,K}(SN)=O_{m,K}(BN^{m+1})\).
- Looking up an acceptance value compares an \(N\)-bit vector with the \(B\) stored ones, at cost \(O_{m,K}(BN^2)\).
- A compatibility test makes \(N^2\) lookups in the \(N\times N\) table, each a scan of \(O(N^2)\) cells, at cost \(O(N^4)\).

Since \(m\geq3\), both \(BN^2\) and \(N^4\) are at most \(BN^{m+1}\).

*Testing one ordered pair of states.* The test fetches both records, checks \(L\cup Z\subseteq L'\), forms \(L'\setminus(L\cup Z)\), looks up its acceptance value and updates a mark. It therefore costs \(O_{m,K}(BN^{m+1})\).

*Reachability.* Start from the initial states and make \(S\) passes over all \(S^2\) ordered pairs, marking a state whenever an already marked state has a transition to it. A reachable state is reached by a simple path with fewer than \(S\) transitions, so after \(S\) passes every reachable state is marked. Over all \(B\) sets the cost is
\[
\begin{aligned}
&O_{m,K}\bigl(B\cdot S\cdot S^2\cdot BN^{m+1}\bigr)\\
&\quad=O_{m,K}\bigl(B^5N^{4m+1}\bigr)\\
&\quad=O_{m,K}\bigl(N^{5mK+4m+1}\bigr).
\end{aligned}
\]

*Remaining work.* The remaining tasks and their costs are:

| Task | Cost |
|---|---|
| Generating and evaluating the formulas | \(O_{m,K}(BN^3)\) |
| Removing repeated bit vectors in pairs | \(O(B^2N)\) |
| Sorting the bit vectors by cardinality | \(O(B^2N)\) |
| Enumerating and testing the candidate states | \(O_{m,K}(BSN^4)\) |
| Following the predecessor records of a reached path | \(O_{m,K}(S^2N)\) |
| Copying the stored schedules of the pieces | \(O_{m,K}(BN^2\log N)\) per piece, at most \(N\) pieces |

Formulas are evaluated with \(O(mN^2)\) table lookups per leaf. A reached path has at most \(S\) records, and the pieces partition \(W\). All these costs are at most \(B^5N^{4m+1}\). \(\square\)

For \(m=3\) the bound is \(N^{15K+13}\), the bound of Proposition 5.1 of *Global descriptions and the running time*.

**Corollary 3.3 (proof of Theorem 1.1 of *Unit jobs on m machines*).** Let \(m\geq3\) be fixed, \(K=K_m=12m+25\), and
\[
\begin{aligned}
e&=5m(12m+25)+4m+1\\
&=60m^2+129m+1.
\end{aligned}
\]
Use the explicit encoding: the jobs \(1,\ldots,n\) and the arcs are listed with identifiers in binary, and \(T\) is given in binary. Let \(L\) be the input length. Then:

- a deadline decision with \(1\leq T<n\) takes \(O_m(N^e)\) steps, including reading the input;
- the decision for an arbitrary deadline, with a schedule returned if one exists, and the computation of a schedule of minimum makespan each take
\[
O_m\bigl((L+2)^{e+1}\bigr)
\]
steps, where \(e+1=60m^2+129m+2\).

*Proof.* The jobs are listed explicitly, so \(n\leq L\) and \(|E|\leq L\). Expanding \(5m(12m+25)+4m+1\) gives \(60m^2+129m+1\). The three branches of the decision are as follows.

1. *\(T<1\).* No map from the nonempty set \(V\) to \(\varnothing\) exists, so the algorithm rejects. Comparing \(T\) with \(1\) costs \(O(L)\).
2. *\(T\geq n\).* One job per slot in a topological order is a schedule of makespan \(n\leq T\), so the algorithm accepts and returns it. Comparing \(T\) with \(n\) costs \(O(L^2)\). The topological order is the one described in item (ii) below, computed on \(V\), at cost \(O(n^5\log n)=O(L^6)\).
3. *\(1\leq T<n\).* If \(n>mT\), the algorithm rejects. Otherwise it pads to \(N=mT\) jobs and runs the program. In this branch \(n\leq N\) and \(N=mT<mn\leq mL\).

*Preprocessing in branch 3.* Its cost is bounded independently of \(m\).

- (i) *Reading.* Copying the input to a work tape and computing \(n\) costs \(O(L^2)\).
- (ii) *The table of \(\prec\).* Store an \(N\times N\) bit matrix row by row on a tape; locating an entry with a binary counter costs \(O(N^2\log N)\).
  - Entering the at most \(L\) arcs costs \(O(L\cdot N^2\log N+L^2)\).
  - Transitive closure by Warshall's triple loop costs \(O(N^3\cdot N^2\log N)\).
  - The rank \(\lambda\), by the removal procedure of Lemma 1.2 of [Unit jobs on three machines](unit-jobs-on-three-machines.md) with the smallest identifier first, uses \(N\) rounds of \(N^2\) lookups each, at cost \(O(N^5\log N)\).
  - The padding jobs are isolated, so their rows and columns are zero.
- (iii) *Output.* Deleting the padding jobs and assigning machines costs \(O(N^2\log N)\).

With binary identifiers, \(L=O(n\log n+|E|\log n+\log T)\). Since \(|E|\leq n^2\), \(T<n\) and \(n\leq N\), this gives \(L=O(N^3)\).

*Total for branch 3.* The preprocessing costs \(O(L^2+LN^2\log N+N^5\log N)\), which is \(O(N^6)\). By Proposition 3.2 the program costs \(O_m(N^e)\). Since \(e\geq928>6\), the total is \(O_m(N^e)\). In terms of \(L\), since \(N\leq mL\) and \(m\) is fixed, this is \(O_m(L^e)\).

*The two tasks.*

- *Decision.* One deadline costs \(O_m(L^e)\) in every branch.
- *Optimization.* Try \(T=1,2,\ldots\) and stop at the first accepted deadline; \(T=n\) is always accepted, so at most \(n\leq L\) deadlines are tried. The first accepted deadline is the minimum makespan by Theorem 3.1. The returned schedule has at most \(n\) entries of \(O(\log n)\) bits, and writing it costs \(O(L^2)\). The total is \(O_m(L\cdot L^e)=O_m(L^{e+1})\).

Since \(L\leq L+2\), both tasks take \(O_m((L+2)^{e+1})\) steps. The constant in \(O_m\) depends only on \(m\), through \(K_m\) and \(512^{K_m}\). \(\square\)

For \(m=3\) the exponent is \(929\). Theorem 3.1 of *Unit jobs on three machines* gives \(150020\), from the coarser budget \(K=10000\).

**Proposition 3.4 (compact encoding).** Let \(m\geq3\) be fixed. Suppose the input gives \(n\geq1\) and \(T\) in binary and lists only the arcs. Let \(d\) be the number of jobs that occur in some arc. The following procedure decides in time polynomial in the input length whether a schedule on \(m\) machines with makespan at most \(T\) exists.

- Reject if \(T<1\) or \(n>mT\).
- Otherwise accept if \(T\geq d\).
- Otherwise, that is if \(T<d\), run the procedure of Corollary 3.3 on the explicitly listed graph on \(\{1,\ldots,n\}\); there \(N=mT<md\leq2m|E|\).

The proposition concerns the decision only. No output schedule of size polynomial in the compact input is claimed.

*Proof.* The rejections are correct: \(T<1\) admits no map, and \(T\) slots hold at most \(mT\) jobs.

Let \(T\geq d\). Run the \(d\) jobs that occur in arcs one per slot, in slots \(1,\ldots,d\), in a topological order of the graph they span; this respects every arc. The other \(n-d\) jobs are isolated. There are \(mT-d\geq n-d\) free positions in slots \(1,\ldots,T\), so the isolated jobs fit. Every slot has at most \(m\) jobs, so a schedule exists.

Let \(T<d\). Then \(n\leq mT<md\leq2m|E|\), since each arc has two endpoints. So the explicit graph on \(\{1,\ldots,n\}\), with every isolated job listed, has length polynomial in \(|E|\). By Corollary 3.3, the decision takes \(O_m(N^e)\) steps, and the explicit graph can be written in polynomial time.

The comparisons of binary numbers, the computation of \(d\) by scanning the arcs, and the construction of the topological order take polynomial time. \(\square\)

## 4. Four machines and what changed

**Corollary 4.1 (four machines).** Let \(m=4\).

- The program of *Unit jobs on m machines*, §3, with \(4\)-element slots and budget \(K_4=73\), accepts the padded set \(J\) exactly when a schedule of makespan at most \(T\) exists, and it returns one.
- The padded decision takes \(O(N^{1477})\) steps, and computing a schedule of minimum makespan takes \(O((L+2)^{1478})\) steps.

*Proof.* Apply Theorem 3.1 and Corollary 3.3 with \(m=4\). They give \(K_4=12\cdot4+25=73\) and
\[
\begin{aligned}
e&=60\cdot16+129\cdot4+1\\
&=1477.
\end{aligned}
\]

On four machines the lists behave as follows (Lemmas 2.1 and 3.4 of *Lists and boundaries on m machines*):

- a pruned list has at most four injection entries and at most six entries;
- an entry has at most \(19\) leaves;
- the union of a list has at most \(33\) leaves. \(\square\)

For four machines, the repository *scheduling-proof-exploration* of drbh (2026) adapts the Lean development of the three-machine theorem [drbh].

**Where three entered the course.** The three-machine lessons use the number three in the following places. Each is replaced by a statement proved for every \(m\).

1. *The definitions.* These are slots of three jobs, padding to \(3T\) jobs, triples in the atomic tests and in the states of the program, and the machine set \(\{1,2,3\}\) in Lemma 1.3 of *Unit jobs on three machines*. They are replaced by §§1–3 of *Unit jobs on m machines* and its Lemmas 1.2 and 2.1.
2. *Counting slots.* The bound \(\binom N3\leq N^3\) in Lemma 2.2 of [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md) is replaced by Lemma 3.1(c) of *Unit jobs on m machines*.
3. *The exchange.* The comparison of the smallest, middle and largest elements of a triple in Lemma 2.1 of *Separators and the shared-cutoff walk* is replaced by the order-statistics argument of Lemmas 4.1 and 4.2 of *Unit jobs on m machines*.
4. *List length.* The bound of three injections and five entries in Lemma 3.2 of [Carried and pruned lists](carried-and-pruned-lists.md) is replaced by \(m\) injections and \(m+2\) entries in Lemma 2.1 of *Lists and boundaries on m machines*. This is the only use of the slot size in the structural argument.
5. *Leaf counts.* The counts derived from the five-entry bound are the following:
   - Lemmas 2.1 and 4.1 of [Changing direction](changing-direction.md): \(21\) and \(25\) leaves;
   - Lemma 4.1 of *Global descriptions and the running time*: \(125\), \(257\) and \(132\) leaves;
   - Proposition 5.1 and Remark 5.2 there.

   They are replaced by Lemmas 3.2 and 3.4 of *Lists and boundaries on m machines* and by Lemmas 1.1 and 2.1, Proposition 3.2 and Proposition 3.4 of this lesson.

Every other statement of the course holds with "triple" read as "slot of \(m\) jobs", by the same proof.

So the three-machine proof extends to \(m\) machines with these substitutions:

| Three machines | \(m\) machines |
|---|---|
| triple | \(m\)-element antichain |
| padding to \(3T\) | padding to \(mT\) |
| at most three injections | at most \(m\) injections |
| at most five entries | at most \(m+2\) entries |

The leaf counts must be computed afresh. The bound \(25\) per entry in Lemma 4.1 of *Changing direction* was obtained from five terms of at most four leaves each. With \(m+2\) terms, the same reasoning gives \(4m+13\) leaves per entry, which exceeds \(25\) for \(m\geq4\). The finer count of Lemma 3.4 of *Lists and boundaries on m machines* shows the following:

- every entry except the first entry of a switch pair has at most three leaves;
- the first entry of a switch pair has at most \(3m+7\) leaves;
- the union of a list has at most \(6m+9\) leaves.

Consequently the budget \(K_m=12m+25\) is linear in \(m\), and the exponent \(e\) is quadratic in \(m\).

The proofs of the three lessons on \(m\) machines use only the earlier lessons of this course. The OpenAI preprint, the scope document of its Lean formalization and the four-machine repository of drbh are listed under References.

## 5. Exercises

**5.1.** Tabulate \(A_m\), \(K_m\), \(6m+16\), \(e\) and \(e+1\) for \(m=3,4,5,6\).

**5.2.** Using binary search over the deadline, as in Exercise 5.2 of *Unit jobs on three machines*, show that a schedule of minimum makespan on \(m\) machines can be computed in \(O_m(L^e\log L)\) steps for \(L\geq2\).

**5.3.** *Release dates.* Take eight jobs \(j_1,\ldots,j_8\) without precedence relations and four machines. Job \(j_8\) may not run in slot \(1\); the other jobs may run in any slot. Show that the two slots \(\{j_1,j_2,j_3,j_4\},\{j_5,j_6,j_7,j_8\}\) respect the release date. Then show that exchanging \(j_8\) with \(j_1\) gives two \(4\)-element antichains that respect all precedences but violate the release date. What does this say about extending Lemmas 2.2 and 4.2 of *Unit jobs on m machines* to release dates?

**5.4.** *Uniform machines.* Three machines have speeds \(1,1,2\), and a unit job takes time \(1/s\) on a machine of speed \(s\). Show that four independent unit jobs can all finish by time \(1\). Show that no schedule with unit slots of at most three jobs has makespan \(1\) for these jobs.

**5.5.** Explain why \(e\) is quadratic in \(m\). Why does Theorem 1.1 of *Unit jobs on m machines* give no bound polynomial in \(L\) when \(m\) is part of the input?

## 6. Solutions

**5.1.** Use \(A_m=6m+9\), \(K_m=2A_m+7\) and \(e=5mK_m+4m+1\).

| \(m\) | \(A_m\) | \(K_m\) | \(6m+16\) | \(e\) | \(e+1\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 61 | 34 | 928 | 929 |
| 4 | 33 | 73 | 40 | 1477 | 1478 |
| 5 | 39 | 85 | 46 | 2146 | 2147 |
| 6 | 45 | 97 | 52 | 2935 | 2936 |

For \(m=3\), \(e=5\cdot3\cdot61+13=928\). For \(m=6\), \(e=5\cdot6\cdot97+25=2935\).

**5.2.** A schedule with values in \(\{1,\ldots,T\}\) also has values in \(\{1,\ldots,T+1\}\), so feasibility is monotone in \(T\), and \(T=n\) is feasible.

Keep two numbers: \(\ell\), equal to \(0\) or an infeasible deadline, and \(h\), a feasible deadline together with a schedule for it. Start with \(\ell=0\) and with \(h=n\) and the topological-order schedule. While \(h-\ell>1\), test \(t=\lfloor(\ell+h)/2\rfloor\) and replace \(\ell\) or \(h\) by \(t\). After at most \(\lceil\log_2n\rceil\) tests, \(h\) is the least feasible deadline, and its stored schedule is optimal.

Every tested \(t\) satisfies \(t<n\), so each test costs \(O_m(L^e)\) by Corollary 3.3. Since \(n\leq L\), the total is \(O_m(L^e\log L)\).

**5.3.** In the first schedule, \(j_8\) runs in slot \(2\), so the release date is respected. After the exchange, the slots are \(\{j_8,j_2,j_3,j_4\}\) and \(\{j_1,j_5,j_6,j_7\}\). There are no precedence relations, so both are antichains of four jobs and every precedence is respected, but \(j_8\) runs in slot \(1\).

So a full schedule of an interval that respects precedence need not respect release dates. The analogue of Lemma 2.2 of *Unit jobs on m machines* in which full schedules must also respect release dates fails. In the same way, for a priority order in which \(j_8\) comes first, the exchange that Lemma 4.2 uses for a lexicographic comparison produces a schedule that is not admissible. Extending the method to release dates would need new replacement and exchange arguments.

**5.4.** Run one job on each machine of speed \(1\) during \([0,1)\), and two jobs one after the other on the machine of speed \(2\), during \([0,\tfrac12)\) and \([\tfrac12,1)\). All four jobs finish by time \(1\).

With unit slots of at most three jobs, makespan \(1\) allows one slot, which holds at most three of the four jobs. Lemma 1.2 of *Unit jobs on m machines* does not apply here, because it assumes that every job takes one unit of time on every machine.

**5.5.** By Proposition 3.2, \(e=5mK_m+4m+1\). The term \(5mK_m=60m^2+125m\) is a product of two factors linear in \(m\):

- each leaf of a formula may refer to any of up to \(N^m\) sets of \(m\) jobs;
- the number of leaves needed, \(K_m\), is itself linear in \(m\).

So the number of formulas is about \(N^{mK_m}\), and its fifth power enters the running time.

When \(m\) is part of the input, the exponent grows with the input. For \(m=n\), for example, it is of order \(n^2\), and \((L+2)^{e+1}\) is not bounded by any fixed power of \(L\). Moreover, *Unit jobs on three machines*, §3, recalls that the problem with \(m\) part of the input is NP-complete (Ullman, 1975). A running time polynomial in \(L\) uniformly in \(m\) would therefore imply \(\mathrm P=\mathrm{NP}\).

## References

- The main argument of this lesson follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 8 and 9. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026. It states and proves the three-machine case. It is named for credit; this lesson does not depend on it.
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/124.md. Context only.
- [drbh] drbh, *scheduling-proof-exploration*, GitHub repository, 2026: an adaptation of the Lean development of the three-machine theorem to four machines, which its README describes as an exploration. https://github.com/drbh/scheduling-proof-exploration
- J. D. Ullman (1975), NP-completeness when the number of machines is part of the input, is named for credit in Exercise 5.5.
