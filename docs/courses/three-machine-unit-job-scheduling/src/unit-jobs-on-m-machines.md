# Unit jobs on m machines

*Written by Claude Opus 5.5 (Anthropic) on 24 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in three separate sessions, and this lesson was planned and written from it by Claude Opus 5.5 in two further sessions and checked and finished by Claude Opus 5.5 in another. Public domain (CC0).*

The first eight lessons of this course prove that unit jobs with precedence constraints can be scheduled optimally on three identical machines in polynomial time. The number three enters that proof in only a few places. This lesson and the two lessons that follow it prove the same theorem for every fixed number \(m\) of machines. They are [Lists and boundaries on m machines](lists-and-boundaries-on-m-machines.md) and [Every fixed number of machines](every-fixed-number-of-machines.md).

This lesson redoes the material of four earlier lessons for slots of \(m\) jobs, and assumes them:

- [Unit jobs on three machines](unit-jobs-on-three-machines.md);
- [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md);
- [Separators and the shared-cutoff walk](separators-and-the-shared-cutoff-walk.md);
- [Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md).

The construction is unchanged, and so is almost every proof. The only new mathematics is an exchange argument for sorted \(m\)-tuples in §4. It replaces the comparison of the smallest, middle and largest job of a triple.

Throughout, \(m\geq1\) is an integer. The hypothesis \(m\geq3\) is used only in two places. One is the convenient counting inequality of Lemma 3.1(c). The other is the running-time accounting of *Every fixed number of machines*. Every structural statement holds for all \(m\geq1\).

## 1. The problem on m machines

The input is a finite directed acyclic graph \(G=(V,E)\) with \(V=\{1,\ldots,n\}\), \(n\geq1\), listed explicitly. A *schedule on \(m\) machines with deadline* \(T\) is a map
\[
\tau:V\to\{1,\ldots,T\}
\]
with two properties:

- \(\tau\) takes every value at most \(m\) times;
- \(\tau(u)<\tau(v)\) for every arc \((u,v)\).

The at most \(m\) jobs with \(\tau(v)=t\) run during the time slot \([t-1,t)\) on different machines. The *makespan* is \(\max_v\tau(v)\). This is the problem \(Pm\mid\mathrm{prec},p_j=1\mid C_{\max}\).

The order \(\prec\) (a path of positive length), predecessors, successors, antichains, and Lemmas 1.1 and 1.2 of *Unit jobs on three machines* (arcs versus paths, linear extensions) involve no machines. They are used unchanged. In particular, by Lemma 1.1 there, the jobs with one common value of \(\tau\) form an antichain.

**Theorem 1.1 (every fixed number of machines).** There is one deterministic algorithm with the following properties.

- *Input.* An integer \(m\geq3\), an explicitly listed finite directed acyclic graph \(G=(V,E)\) on \(n\geq1\) unit jobs, and possibly an integer deadline \(T\) written in binary.
- *With a deadline.* It decides whether a schedule on \(m\) machines with deadline \(T\) exists, and returns one if so.
- *Without a deadline.* It returns a schedule on \(m\) machines of minimum makespan.
- *Parameters.* The algorithm computes its leaf budget \(K_m=12m+25\) and all the formulas it uses from \(m\).
- *Total running time.* For every fixed \(m\geq3\), both tasks take
\[
O_m\bigl((L+2)^{60m^2+129m+2}\bigr)
\]
steps on a deterministic multitape Turing machine. Here \(L\) is the length of the input in binary.
- *Padded decision.* For \(1\leq T<n\) with \(n\leq mT\), the decision on the padded set of \(N=mT\) jobs takes
\[
O_m\bigl(N^{60m^2+129m+1}\bigr)
\]
steps.
- *Constants.* The constants implied by \(O_m\) are effective functions of \(m\).

The exponent grows quadratically with \(m\). No bound uniform in \(m\) is claimed, and the theorem says nothing about instances in which \(m\) grows with the input.

The proof is spread over three lessons. Correctness rests on three results of this lesson: the padding Lemma 2.1, the soundness Proposition 3.2 and the completeness criterion Lemma 3.4. It also rests on the structure theorem, Theorem 2.2 of *Every fixed number of machines*. These pieces are assembled in Theorem 3.1 of that lesson. The running time is Proposition 3.2 and Corollary 3.3 there; the corollary derives the exponent \(60m^2+129m+2\).

For \(m=3\) the exponent is \(929\). This is far smaller than the exponent \(150020\) of Theorem 3.1 of *Unit jobs on three machines*, because the leaf counts of the two following lessons are sharper. Theorem 1.1 for \(m=3\) contains that theorem.

For \(m=1\) and \(m=2\) the problem was already known to be polynomial, by the results named below. The arguments of this course also show that the algorithm is correct for these values. Only the stated time bound uses \(m\geq3\).

**What was known.**

- *Two machines.* Fujii, Kasami and Ninomiya (1969) solved the problem, and Coffman and Graham (1972) gave an optimal list-scheduling rule.
- *Variable machine count.* When \(m\) is part of the input, the problem is NP-complete (Ullman, 1975).
- *Three or more machines.* Garey and Johnson (1979) listed three machines among the open problems of their book, and the complexity was open for every fixed \(m\geq3\). OpenAI's theorem of 2026, the subject of the first eight lessons, settles three machines. For four machines, the repository *scheduling-proof-exploration* of drbh (2026) adapts the Lean development of the three-machine theorem and describes itself as an exploration [drbh].
- *Special orders.* Polynomial algorithms exist for opposing forests (Garey, Johnson, Tarjan and Yannakakis, 1983) and for orders of bounded height (Dolev and Warmuth, 1984).
- *Exact algorithms.* Nederlof, Swennenhuis and Węgrzycki gave an algorithm with running time \((1+\frac nm)^{O(\sqrt{nm})}\). This is not polynomial for fixed \(m\).
- *Approximation.* Levey and Rothvoß, Garg, Li, and Das and Wiese gave approximation schemes. These approximate the optimum and do not decide a deadline exactly.

These results are named for credit, and no proof in this course uses them.

**Lemma 1.2 (integer start times on m machines).** Every job \(v\) is given a real start time \(s_v\geq0\) and a machine \(\mu(v)\in\{1,\ldots,m\}\). Assume the following:

- two jobs on the same machine run during disjoint intervals \([s_u,s_u+1)\) and \([s_v,s_v+1)\);
- \(s_u+1\leq s_v\) for every arc \((u,v)\).

Then there is a schedule on \(m\) machines whose makespan is at most \(\max_v(s_v+1)\).

*Proof.* Order the jobs of each machine by start time. Consecutive jobs \(u,v\) of one machine then satisfy \(s_u+1\leq s_v\), because their intervals are disjoint.

Let \(H\) be the graph on \(V\) whose arcs are the arcs of \(G\) together with the pairs of consecutive jobs of a machine. The start time increases by at least one along every arc of \(H\), so \(H\) is acyclic. Process the jobs in a topological order of \(H\) (Lemma 1.2 of *Unit jobs on three machines*) and put
\[
s'_v=\max\Bigl(\{0\}\cup\{s'_u+1:(u,v)\in H\}\Bigr).
\]

The value \(s'_v\) is an integer. By induction along the order, \(s'_v\leq s_v\): for an arc \((u,v)\) of \(H\),
\[
s'_u+1\leq s_u+1\leq s_v.
\]
Along every arc of \(H\) we have \(s'_u+1\leq s'_v\). Hence two jobs of one machine receive different integers, and every arc of \(G\) is respected.

Put \(\tau(v)=s'_v+1\). Each value of \(\tau\) is taken by at most one job of each machine, hence at most \(m\) times. The makespan of \(\tau\) is \(\max_v(s'_v+1)\leq\max_v(s_v+1)\). \(\square\)

## 2. Full schedules

A deadline \(T\) with \(1\leq T\leq n\) is given. If \(n>mT\), no schedule exists, since \(T\) slots hold at most \(mT\) jobs. Otherwise add \(mT-n\) new *isolated* jobs, related to no job, and let \(J\) be the resulting set of
\[
N=|J|=mT
\]
jobs, ordered by \(\prec\).

For \(W\subseteq J\), a *full schedule* of \(W\) is a sequence of pairwise disjoint slots whose union is \(W\), such that the slot containing \(x\) comes strictly before the slot containing \(y\) whenever \(x\prec y\). Recall that a slot is an \(m\)-element antichain. A full schedule of \(W\) has \(|W|/m\) slots, and the empty set has the empty full schedule.

Open intervals of a full schedule of \(J\) are defined as in §2 of *Unit jobs on three machines*: the slots strictly between two boundaries. A boundary may be one of the two virtual boundaries, before the first slot or after the last.

**Lemma 2.1 (padding).** Let \(1\leq T\leq n\) and \(n\leq mT\). Then \(G\) has a schedule on \(m\) machines with deadline \(T\) if and only if \(J\) has a full schedule. Moreover \(N=mT\leq mn\).

*Proof.* Suppose \(G\) has such a schedule, and view it with its \(T\) slots. Exactly \(mT-n\) machine positions are unused; put the isolated jobs into them. Every slot then holds \(m\) jobs, and these are pairwise incomparable: the original jobs of a slot by Lemma 1.1 of *Unit jobs on three machines*, and the isolated jobs because they are related to nothing. The slots in time order form a full schedule of \(J\).

Conversely, delete the isolated jobs from a full schedule of \(J\). What remains is a schedule of \(G\) with at most \(m\) jobs per slot and \(T\) slots, and every precedence is respected. Finally \(N=mT\leq mn\) because \(T\leq n\). \(\square\)

**Lemma 2.2 (reordering an open interval).** Let a full schedule of \(J\) be given, and let \(W\) be the job set of an open interval \((a,b)\), whose boundaries may be virtual. Replace the slots of \((a,b)\) by the slots of any full schedule of \(W\), in its order. The result is a full schedule of \(J\).

*Proof.* The replacement has \(|W|/m\) slots, exactly as many as it replaces. The new sequence therefore consists of pairwise disjoint slots with union \(J\).

Let \(x\prec y\). If both jobs lie in \(W\), the new schedule of \(W\) puts \(x\) first. If neither lies in \(W\), their slots are unchanged. Suppose \(x\notin W\) and \(y\in W\). In the old schedule \(x\) came before \(y\), so \(x\) is at or before \(a\). It still is, and \(y\) is still strictly after \(a\). The case \(x\in W\), \(y\notin W\) is symmetric: \(y\) is at or after \(b\). \(\square\)

The lemma allows *rescheduling* the jobs of a contiguous interval. It does not allow arbitrary permutations of slots: Exercise 5.3 of *Unit jobs on three machines* gives a permutation of non-adjacent slots that breaks precedence, and the same example works with slots of \(m\) jobs.

## 3. Descriptions and the dynamic program

Frames, the rank \(\lambda:J\to\{1,\ldots,N\}\), upsets and downsets are defined as in §1 of *Descriptions and a dynamic program*. So is the convention that every notion refers to the working frame. For every set \(a\subseteq J\) of \(m\) jobs, define the cones
\[
\begin{aligned}
P_a&=\{x\in J:x\prec y\text{ for some }y\in a\},\\
D_a&=\{x\in J:y\prec x\text{ for some }y\in a\},
\end{aligned}
\]
and the weak cones \(\widehat P_a=P_a\cup a\) and \(\widehat D_a=D_a\cup a\).

The cones of the virtual boundaries are the constants fixed in that lesson:

- before the first slot, \(D=\widehat D=J\) and \(P=\widehat P=\varnothing\);
- after the last slot, \(D=\widehat D=\varnothing\) and \(P=\widehat P=J\).

The *atomic tests* are the following subsets of \(J\), in either frame:

- the constants \(J\) and \(\varnothing\);
- the rank thresholds \(\{\lambda\leq k\}\) and \(\{\lambda\geq k\}\) for \(0\leq k\leq N+1\);
- for every \(m\)-element set \(a\subseteq J\), the sets \(a\), \(P_a\), \(D_a\), \(\widehat P_a\) and \(\widehat D_a\).

A *formula* is a finite binary tree in which every inner node has two children. Its inner nodes are labelled \(\wedge\) or \(\vee\), and its leaves are atomic tests or complements of atomic tests. Its *size* is its number of leaves, and \([\![F]\!]\subseteq J\) is the set it describes.

For an integer \(K\geq1\), the *budget*, let \(\mathcal F_K\) be the family of sets described by formulas of size at most \(K\).

- A set \(W\) has a *global description* if \(W\in\mathcal F_K\).
- A set \(L\subseteq W\) has a *relative description inside* \(W\) if \(L=W\cap[\![F]\!]\) for a formula \(F\) of size at most \(K\).

**Lemma 3.1 (descriptions on m machines).**

(a) Let \(a\) be a slot of a full schedule. Every job of \(P_a\) is scheduled strictly before \(a\), and every job of \(D_a\) strictly after \(a\). No job of \(a\) lies in either cone. Consequently, a job scheduled at or before \(a\) is not in \(D_a\), and a job scheduled at or after \(a\) is not in \(P_a\).

(b) For every formula \(F\) there is a formula of the same size describing \(J\setminus[\![F]\!]\).

(c) Let \(m\geq3\), \(K\geq1\) and \(N\geq m\). There are at most
\[
K\cdot512^K\,N^{mK}
\]
formulas of size at most \(K\). For fixed \(m\) and \(K\), a deterministic procedure lists the members of \(\mathcal F_K\) as bit vectors of length \(N\), without repetitions and sorted by cardinality. Its running time is bounded by a polynomial in \(N\).

*Proof.* (a) If \(x\prec y\) with \(y\in a\), then \(x\) lies in an earlier slot than \(y\) by the definition of a full schedule. The case of \(D_a\) is symmetric. The jobs of \(a\) are pairwise incomparable, and \(y\prec y\) never holds. Only the fact that \(a\) is an antichain is used, not its size.

(b) Replace every leaf by its complement and exchange \(\wedge\) and \(\vee\) at every inner node. By De Morgan's laws, induction on the tree shows that the new formula describes the complement. No leaf is created or removed.

(c) *The leaf alphabet.* In one frame there are \(2\) constants, \(2(N+2)\) thresholds and \(5\binom Nm\) tests attached to \(m\)-element sets. Counting both frames and complements, at most
\[
\begin{aligned}
&2\bigl(4+4(N+2)+10\tbinom Nm\bigr)\\
&\quad=20\tbinom Nm+8N+24
\end{aligned}
\]
leaves are possible. Since \(N\geq m\geq3\) we have \(\binom Nm\leq N^m\), \(N\leq N^m\) and \(24<27\leq N^m\). So the alphabet has at most \(29N^m\leq64N^m\) elements.

*Tree shapes.* Write a tree with \(\ell\) leaves in preorder, recording \(1\) for an inner node and \(0\) for a leaf. The string has length \(2\ell-1\) and determines the tree by recursive decoding. So there are at most \(2^{2\ell-1}<4^\ell\) shapes.

*Formulas.* A tree with \(\ell\) leaves has \(\ell-1\) inner nodes, each with two possible labels. The number of formulas of size \(\ell\) is therefore at most
\[
\begin{aligned}
&4^\ell\cdot2^{\ell-1}\cdot(64N^m)^\ell\\
&\quad\leq512^\ell N^{m\ell}.
\end{aligned}
\]
Summing over \(1\leq\ell\leq K\) gives at most \(K\cdot512^KN^{mK}\).

*The procedure.* The order \(\prec\) and the rank are computed by a search from every vertex and by the removal procedure of Lemma 1.2 of *Unit jobs on three machines*. Both take time polynomial in \(N\). The procedure then:

- enumerates all formulas of size at most \(K\);
- evaluates each leaf on each job from the table of \(\prec\) and combines the leaves along the tree;
- deletes repeated bit vectors by pairwise comparison;
- sorts the remaining vectors by their number of ones.

For fixed \(m\) and \(K\), each step is polynomial in \(N\). \(\square\)

**The dynamic program with budget \(K\).** The program is that of §3 of *Descriptions and a dynamic program*, with \(m\)-element slots. It assigns to every \(W\in\mathcal F_K\), in order of increasing size, a value \(\mathsf A(W)\in\{\text{true},\text{false}\}\), as follows.

- \(\mathsf A(U)\) is false for every \(U\notin\mathcal F_K\).
- \(\mathsf A(\varnothing)\) is true.
- \(\mathsf A(W)\) is false when \(m\) does not divide \(|W|\).

For a nonempty \(W\in\mathcal F_K\), a *state* is a decomposition \(W=L\cup Z\cup R\) into pairwise disjoint parts with three properties:

- \(Z\) is an antichain of \(m\) jobs;
- \(L\) has a relative description inside \(W\);
- the parts are *compatible*: no job of \(Z\cup R\) precedes a job of \(L\), and no job of \(R\) precedes a job of \(Z\).

A state is *initial* if \(\mathsf A(L)\) is true, and *final* if \(\mathsf A(R)\) is true. There is a *transition* from \((L,Z,R)\) to \((L',Z',R')\) when
\[
\begin{gathered}
L\cup Z\subseteq L'\quad\text{and}\\
\mathsf A\bigl(L'\setminus(L\cup Z)\bigr)\text{ is true}.
\end{gathered}
\]
\(\mathsf A(W)\) is set to true exactly when some initial state reaches some final state through transitions. A single state that is both initial and final counts.

Every value consulted belongs to a smaller set than \(W\). Indeed, \(L\), \(R\) and \(L'\setminus(L\cup Z)\) all miss the nonempty set \(Z\subseteq W\). So the program is well defined. The deadline is accepted when \(\mathsf A(J)\) is true.

**Proposition 3.2 (soundness, every m).** Let \(m\geq1\) and \(K\geq1\). If the program sets \(\mathsf A(W)\) true, then \(W\) has a full schedule. A full schedule of \(W\) is produced as follows: follow the recorded predecessor states back from a reached final state, and concatenate the stored schedules of the pieces \(A_0,Z_1,A_1,\ldots,Z_k,A_k\) defined below.

*Proof.* We argue by induction on \(|W|\); the empty set has the empty schedule. Let \((L_1,Z_1,R_1),\ldots,(L_k,Z_k,R_k)\) be states forming a path from an initial state to a final state. Put
\[
\begin{aligned}
A_0&=L_1,\qquad A_k=R_k,\\
A_i&=L_{i+1}\setminus(L_i\cup Z_i)\quad(1\leq i<k).
\end{aligned}
\]

*The pieces partition \(W\).* Since \(L_i\cup Z_i\subseteq L_{i+1}\) and the parts of each state are disjoint, induction on \(i\) gives
\[
L_{i+1}=A_0\cup Z_1\cup A_1\cup\cdots\cup Z_i\cup A_i.
\]
Adding the parts \(Z_k\) and \(R_k\) of the last state gives the disjoint union
\[
W=A_0\cup Z_1\cup A_1\cup\cdots\cup Z_k\cup A_k,
\]
taken in this order.

*Each piece has a full schedule.* Every \(A_i\) is accepted. Indeed, \(A_0\) is the left part of an initial state, each \(A_i\) with \(1\leq i<k\) is consulted by a transition, and \(A_k\) is the right part of a final state. Each \(A_i\) also misses \(Z_1\), so it is smaller than \(W\). By induction it has a full schedule. Concatenate these schedules and the slots \(Z_i\) in the displayed order.

*The concatenation is a full schedule.* It is a sequence of disjoint slots with union \(W\). Suppose a job of a piece \(Q'\) precedes a job of an earlier piece \(Q\).

- If \(Q'=Z_j\), then \(Q\subseteq L_j\), and a job of \(Z_j\) precedes a job of \(L_j\).
- If \(Q'=A_j\) with \(j\geq1\), then \(A_j\subseteq R_j\) and \(Q\subseteq L_j\cup Z_j\), and a job of \(R_j\) precedes a job of \(L_j\cup Z_j\).

Both contradict compatibility of the \(j\)-th state. Inside one piece, order is respected by the piece's schedule.

*Producing the schedule.* Record for every state the state from which it was first reached, or mark it as initial. Follow these records back from a reached final state, and store the concatenated schedule as that of \(W\).

The number \(m\) enters only through the divisibility test and the size of \(Z\). One slot per state suffices for every \(m\). \(\square\)

**Definition 3.3 (hierarchy with budget \(K\)).** A *bounded-description hierarchy with budget \(K\)* for a full schedule of \(J\) is a rooted tree of nodes. Every node carries a witnessing full schedule of \(J\), and its job set is the job set of an open interval of that schedule. The tree satisfies four conditions.

1. The root is the whole schedule between the two virtual boundaries; its job set is \(J\).
2. At a node with nonempty job set \(W\), the following happens.
   - The slots of \(W\) may first be replaced by any full schedule of \(W\); the schedule of \(J\) stays full by Lemma 2.2.
   - Then at least one slot of \(W\) is *marked*.
   - The *children* are the nonempty open intervals between consecutive marks, and between each boundary of the node and the nearest mark.
   - Each child receives its own copy of the current schedule of \(J\) as its witness.
3. Every node's job set lies in \(\mathcal F_K\).
4. For every mark \(z\) of a node \(W\), the set of jobs of \(W\) scheduled before \(z\) in original time has a relative description inside \(W\).

**Lemma 3.4 (hierarchy implies acceptance).** If a full schedule of \(J\) has a bounded-description hierarchy with budget \(K\), the program with budget \(K\) accepts \(J\).

*Proof.* We show by induction on \(|W|\) that \(\mathsf A(W)\) is true for the job set \(W\) of every node. If \(W\) is empty, this holds by definition. Otherwise \(W\in\mathcal F_K\) by item 3.

Let \(z_1,\ldots,z_k\) be the marks of \(W\) in time order, in the schedule current when they were chosen. Let \(L_i\) be the set of jobs of \(W\) before \(z_i\), and \(R_i\) the set after it. Each \((L_i,z_i,R_i)\) is a state:

- \(z_i\) is a slot, an antichain of \(m\) jobs;
- \(L_i\) has a relative description by item 4;
- compatibility holds because the schedule respects \(\prec\).

The set \(L_1\) is empty or the child before \(z_1\). The set \(R_k\) is empty or the child after \(z_k\). The set \(L_{i+1}\setminus(L_i\cup z_i)\) is empty or the child between \(z_i\) and \(z_{i+1}\). Every child misses a mark, so it has fewer jobs than \(W\), and all these sets are accepted by induction.

Hence \((L_1,z_1,R_1)\) is initial, consecutive states are joined by transitions, and \((L_k,z_k,R_k)\) is final. So \(\mathsf A(W)\) is true. The root gives \(\mathsf A(J)\). \(\square\)

## 4. Normalized schedules and separators

Let \(U\) be the job set of an open interval of a full schedule of \(J\). A *priority order* on \(U\) is a linear extension of the restriction of \(\prec\) to \(U\). Write \(\pi(x)\in\{1,\ldots,|U|\}\) for the position of \(x\) in it; a smaller position means *better* priority.

The *encoding* of a full schedule of \(U\) is built in two steps. First sort the jobs of each slot increasingly by \(\pi\), giving an \(m\)-tuple. Then concatenate these \(m\)-tuples in time order. Every full schedule of \(U\) has \(|U|/m\) slots, so every encoding is a sequence of exactly \(|U|\) integers.

A full schedule of \(U\) is *normalized* if its encoding is lexicographically least among the encodings of all full schedules of \(U\). If \(U\) has a full schedule, a normalized one exists, because there are finitely many. Normalized schedules are used only to prove existence; the algorithm never computes them.

**Lemma 4.1 (lowering one element of an m-set).** Let \(A\) be a set of \(m\) distinct integers, let \(y\in A\) and \(x\notin A\) with \(x<y\), and put \(A'=(A\setminus\{y\})\cup\{x\}\). Write the elements of the two sets increasingly:
\[
\begin{aligned}
A&=\{a_1<\cdots<a_m\},\\
A'&=\{a'_1<\cdots<a'_m\}.
\end{aligned}
\]
Then \(a'_k\leq a_k\) for every \(k\), with strict inequality for some \(k\). Hence \((a'_1,\ldots,a'_m)\) is lexicographically smaller than \((a_1,\ldots,a_m)\).

*Proof.* For a finite set \(B\) of integers and an integer \(q\), put \(c_B(q)=|\{z\in B:z\leq q\}|\). Passing from \(A\) to \(A'\) removes \(y\) and adds \(x\). Hence:

- \(c_{A'}(q)=c_A(q)\) for \(q<x\);
- \(c_{A'}(q)=c_A(q)+1\) for \(x\leq q<y\);
- \(c_{A'}(q)=c_A(q)+1-1=c_A(q)\) for \(q\geq y\).

So \(c_{A'}\geq c_A\) everywhere. Since \(a_k=\min\{q:c_A(q)\geq k\}\), and similarly for \(A'\), it follows that \(a'_k\leq a_k\) for every \(k\).

The sums satisfy
\[
\textstyle\sum_ka'_k=\sum_ka_k-(y-x),
\]
which is smaller, so the tuples differ. At the first index \(k\) where they differ, \(a'_k\neq a_k\) and \(a'_k\leq a_k\), so \(a'_k<a_k\). \(\square\)

**Lemma 4.2 (no improving exchange, m machines).** Let \(U\) be the job set of an open interval, with a full schedule of \(U\) normalized for a priority order \(\pi\). Let \(r\) be a slot of \(U\). Reorder the slots of \(U\) strictly after \(r\) in any way that keeps a full schedule of \(U\); the empty reordering is allowed. Then no exchange of a job \(y\) at \(r\) with a job \(x\) scheduled after \(r\) with \(\pi(x)<\pi(y)\) gives a full schedule of \(U\).

*Proof.* An exchange moves \(x\) into the slot of \(y\) and \(y\) into the slot of \(x\), so every slot still has \(m\) jobs. Suppose the result were a full schedule of \(U\).

Its slots before \(r\) are those of the normalized schedule, so the first blocks of the two encodings agree. At \(r\), the set of \(\pi\)-values changes from \(A\) to \(A'=(A\setminus\{\pi(y)\})\cup\{\pi(x)\}\). Here \(\pi(x)\notin A\), since \(x\) is not in \(r\). By Lemma 4.1 the sorted block at \(r\) becomes lexicographically smaller.

Every block has \(m\) entries, so the block at \(r\) occupies the same positions in both encodings. Hence the first position where the encodings differ lies in this block, and the new encoding is smaller there. This contradicts the minimality of the normalized encoding. \(\square\)

Cutoffs, low and high jobs, and *separators* in a domain are defined as in Definition 1.1 of *Separators and the shared-cutoff walk*, with slots of \(m\) jobs. So is \(B_z(H)=P_z\cup(H\setminus\widehat D_z)\). So are positions, which are the slots of the domain together with the boundary just before it. An *exception* at a position \(s\) for a cutoff \(L\) is a job of \(L\) scheduled after \(s\) and not in \(D_s\).

**Proposition 4.3 (separators and walks on m machines).** Let \(m\geq1\). The following statements of *Separators and the shared-cutoff walk* hold as stated there for slots of \(m\) jobs, with Lemma 4.2 in place of Lemma 2.1 of that lesson. They also hold in the setting of a priority order on a set \(W\supseteq U\) acting on \(U\) through restriction.

- Lemma 1.2: if a slot \(z\) of \(U\) separates \(S\) and \(H\cap U=S\), then \(B_z(H)\cap U\) is the set of jobs of \(U\) scheduled before \(z\).
- Lemma 1.3: a slot separates \(S\) forward if and only if it separates \(U\setminus S\) backward.
- Lemma 3.1 (one advance), conclusions (1)–(3).
- Lemma 3.2: the walk at a fixed cutoff stops at a separator.
- Lemma 3.3: the shared-cutoff walk from a separator of \(S\) stops at a position \(t\geq s\) that separates both \(S\) and \(S\cup\{p\}\).
- Corollary 3.4: every cutoff of a nonempty domain with a full schedule has a separator after rescheduling the domain.

*Proof.* We go through the statements in order. Fix a domain \(U\) with a normalized full schedule.

*Lemma 1.2.* A high job of \(U\) before \(z\) is in \(P_z\) by condition (a). A low job before \(z\) is in \(H\), and by Lemma 3.1(a) it is not in \(\widehat D_z\). Conversely, a job of \(P_z\) is before \(z\) by Lemma 3.1(a). A job of \(U\cap H\setminus\widehat D_z\) is low, hence it is not in \(z\subseteq\widehat D_z\). It is not after \(z\) either, because a low job after \(z\) is in \(D_z\) by condition (b).

*Lemma 1.3.* The proof there is formal: reversing the frame exchanges "before" with "after" and \(P_z\) with \(D_z\), and turns the cutoff \(S\) into the cutoff \(U\setminus S\) of the reversed order. Slot sizes do not appear.

*Lemma 3.1 (one advance).* Let \(M\subseteq L\) be prefixes of the priority order, and let the position \(s\) satisfy condition (a) for \(M\). Let \(t\) be the earliest slot containing an exception for \(L\), and let \(x\in M\) be an exception at \(t\).

(1) Every predecessor of \(x\) in \(U\) is scheduled strictly before \(s\). Let \(w\in U\) with \(w\prec x\). Then \(w\in L\), because \(L\) is a cutoff, and \(w\) is scheduled before \(t\). If \(w\) were at \(s\), then \(x\in D_s\). If \(w\) were strictly between \(s\) and \(t\), it would not be an exception, by the choice of \(t\), so \(w\in D_s\) and \(x\in D_s\) by transitivity. Both contradict the fact that \(x\) is an exception.

(2) Every \(y\notin M\) at a slot \(r\) of \(U\) with \(s\leq r<t\) precedes a job at \(t\) that is not in \(M\). Suppose first that \(y\) has no successor in \(U\) at or before \(t\). Exchange \(x\) and \(y\); both slots keep \(m\) jobs. Only pairs containing \(x\) or \(y\) can be affected.

- *Pairs containing \(x\), at its new slot \(r\).* Its predecessors in \(U\) are before \(s\leq r\) by (1). Its predecessors outside \(U\) are at or before the left boundary of the interval. Its successors are after \(t>r\). A companion \(w\) in \(r\) is not a predecessor of \(x\) by (1), and not a successor, because \(w\) was scheduled before \(x\).
- *Pairs containing \(y\), at its new slot \(t\).* Its predecessors were before \(r<t\). Its successors in \(U\) are after \(t\) by the supposition. Its successors outside \(U\) are at or after the right boundary of the interval. A companion \(w\) in \(t\) is not a successor of \(y\) by the supposition, and not a predecessor, because \(w\) was scheduled after \(y\).
- *The pair \(x,y\).* The relation \(x\prec y\) would make \(y\) a successor of \(x\) at \(r\), and \(y\prec x\) would give \(y\) a successor at \(t\); both have been excluded.

So the exchange gives a full schedule of \(U\). Since \(x\in M\), \(y\notin M\) and \(M\) is a prefix, \(\pi(x)<\pi(y)\). This contradicts Lemma 4.2 with the empty reordering.

Hence \(y\) has a successor \(y_1\in U\) at a slot \(r_1\) with \(r<r_1\leq t\). Moreover \(y_1\notin M\): otherwise \(y\in M\), since \(M\) is a cutoff. If \(r_1<t\), the same argument applies to \(y_1\). The slots increase strictly, so after finitely many steps a successor of \(y\) at \(t\) outside \(M\) is reached.

(3) The slot \(t\) satisfies condition (a) for \(M\). Let \(y\notin M\) be a job of \(U\) scheduled before \(t\). If \(y\) is at a slot \(r\geq s\), (2) gives \(y\in P_t\). If \(y\) is before \(s\), then \(s\) is a slot, since no job of \(U\) lies before the boundary. Condition (a) at \(s\) gives \(w\) at \(s\) with \(y\prec w\). Then \(w\notin M\), and (2) gives a job at \(t\) above \(w\), so \(y\in P_t\).

*Lemma 3.2.* Let \(L\) be a prefix, let \(s\) satisfy (a) for \(L\), and repeatedly advance to the earliest slot containing an exception for \(L\). By part (3) of the one-advance lemma with \(M=L\), every target satisfies (a). Positions increase strictly in a finite domain, so the walk stops. At its final position there is no exception, which is condition (b). If \(s\) separates \(L\), there is no exception and the walk does not move.

*Lemma 3.3.* Let \(s\) separate \(S\), and run the walk for \(S^+=S\cup\{p\}\) from \(s\).

- Condition (a) for \(S^+\) holds at \(s\), because the high jobs for \(S^+\) are among those for \(S\).
- If there is no exception for \(S^+\) at \(s\), then \(s\) separates both cutoffs.
- Otherwise every job of \(S\) after \(s\) is in \(D_s\), so the only exception is \(p\), and the first advance goes to the slot \(t_1\) of \(p\). By part (3) with \(M=L=S^+\), the slot \(t_1\) satisfies (a) for \(S^+\). It also satisfies (a) for \(S\): the high jobs for \(S\) before \(t_1\) are those for \(S^+\), because \(p\) is at \(t_1\).
- Every later exception lies after \(t_1\), so it is a job of \(S\). Part (3) with \(M=S\) and with \(M=S^+\) keeps (a) for both cutoffs at every later target.
- At the final position there is no exception for \(S^+\), hence none for its subset \(S\).

*Restriction.* Let the priority order be given on \(W\supseteq U\), with \(U\) normalized for the restricted order. The intersection of a prefix of the order on \(W\) with \(U\) is a prefix of the restricted order, so Lemma 3.3 applies to the restricted cutoffs. If the promoted job \(p\) is not in \(U\), the two restricted cutoffs coincide and the walk does not move.

*Corollary 3.4.* Order \(S\) first and \(U\setminus S\) second, each by rank. This is a priority order, because \(S\) is a cutoff. Take a normalized full schedule of \(U\) for it; one exists because \(U\) has a full schedule and is nonempty. The first slot separates the empty cutoff: nothing is before it and no job is low. Promote the jobs of \(S\) in this order, applying Lemma 3.3 each time. The walk moves only forward to slots, so the final position is a slot separating \(S\). \(\square\)

## 5. Centers, sides and edge cutoffs

**Proposition 5.1 (Centers, sides and edge cutoffs on m machines).** Let \(m\geq1\).

- All the data of *Centers, sides and edge cutoffs* are defined as there, with slots of \(m\) jobs. These data are:
  - nodes, with a tag, boundaries \(a,b\) and a list \(\mathcal K\) of upsets of \(J\);
  - qualifiers, keys and the old high set \(O\);
  - the invariants (I1)–(I3) and the root;
  - the center and the two sides, with their priority orders and promotions;
  - the normalized parts \(E\) and the walk \(a=s_0\leq\cdots\leq s_q<s_{q+1}=v\);
  - the marks and the children with their edge data.
- Lemmas 1.1, 2.1, 3.1, 4.1 and 4.2 of that lesson hold.
- In particular, every child \(W'\) with edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\) has the following properties: \(b'\) is a slot of \(W\);
\[
\begin{aligned}
W'\cap S&\subseteq D_{a'}\cap P_b,\\
W'\setminus S&\subseteq P_{b'};
\end{aligned}
\]
and \(|W'|<|W|\).
- The root has no switched-side child.

*Proof.* The proofs of that lesson apply with these substitutions:

- Lemma 3.1(a) of this lesson for Lemma 1.1 of *Descriptions and a dynamic program*;
- Proposition 4.3 for Lemma 1.3, Lemma 3.3 and Corollary 3.4 of *Separators and the shared-cutoff walk*;
- Lemma 2.2 of this lesson for Lemma 2.2 of *Unit jobs on three machines*.

We list what each step uses.

- *Keys (Lemma 1.1).* Entries are upsets of \(J\), and \(\lambda\) increases along \(\prec\). There are no slots.
- *The root.* Its list is \((J)\), so \(O=J\subseteq P_b=J\) by the virtual conventions. (I2) and (I3) are empty for a virtual left boundary.
- *Cover (Lemma 2.1).* The proof uses (I1), the exchange of boundaries and cones under reversal of the frame, and the fact that the intersection of \(W\) with a downset is a cutoff.
- *The center.* It is supplied by Corollary 3.4 (Proposition 4.3) for the cutoff \(W\cap P_b\). At the root it is the last slot: for the cutoff \(J\), condition (a) concerns no high job and condition (b) concerns no later job.
- *The switched center cutoff \(X=W\setminus D_a\).* It is obtained from Lemma 1.3 (Proposition 4.3).
- *Priority orders (Lemma 3.1).* The proof is set-theoretic and uses Lemmas 1.1 and 2.1 of that lesson.
- *Normalizing a side.* This is a rescheduling of the open interval \(E\) and is allowed by Lemma 2.2. The center stays a separator, because the separator conditions depend only on which jobs lie on which side of \(v\) and on the fixed cones of \(v\).
- *The walk.* The boundary \(a\) separates \(S_0\) on \(E\), since \(S_0\subseteq D_a\). The walk is Lemma 3.3 in the restricted setting (Proposition 4.3), and it moves only forward, to slots of \(E\).
- *Adjacent cutoffs (Lemma 4.1).* Lemma 3.3 gives the separations at \(s_i\). The center's condition (a) on \(W\) gives the case \(i=q\).
- *Edge labels (Lemma 4.2).* The positions are \(a\), slots of \(E\), or \(v\). Low jobs of the gap are after the separator \(a'\) and lie in \(S_i\subseteq P_b\). High jobs are before the separator \(b'\). The gap misses \(v\). At the root, nothing follows the last slot.

No step uses the number of jobs in a slot. \(\square\)

The slot \(b'\) has exactly \(m\) jobs. *Lists and boundaries on m machines* bounds the length of the lists through this fact (Lemma 2.1 there).

## 6. Exercises

**6.1.** Jobs \(s_1,\ldots,s_{m+1},t\) with \(s_i\prec t\) for all \(i\) are to be scheduled on \(m\) machines. Show that the optimal makespan is \(3\), although the longest chain has two jobs.

**6.2.** Apply Lemma 4.1 to \(A=\{2,5,7,9\}\), \(y=9\), \(x=3\), and count the order statistics that decrease strictly. Show that the conclusion fails when \(x>y\).

**6.3.** Let \(m=4\), and let \(J\) consist of eight jobs \(a,b,x_1,x_2,x_3,z_1,z_2,z_3\) whose only relations are \(b\prec x_i\) and \(a\prec z_i\) for \(i=1,2,3\).

- Show that \(J\) has no full schedule.
- Show that \(L=\{a,x_1,x_2,x_3\}\) and \(Z=\{b,z_1,z_2,z_3\}\) are antichains.
- Show that the program would accept \(J\) through the state \((L,Z,\varnothing)\) if compatibility were not required.

**6.4.** Two full schedules of \(U\) agree on their first \(j-1\) slots, and the \(j\)-th sorted block of the first is lexicographically smaller than that of the second. Show that the encoding of the first is smaller. Where is it used that all full schedules of \(U\) have the same number of slots of the same size?

**6.5.** In the exchange of part (2) of the one-advance lemma in the proof of Proposition 4.3, list the pairs of jobs whose order must be checked. Show that the other \(m-1\) jobs of each of the two slots need no hypothesis beyond (1) and the supposition on \(y\).

## 7. Solutions

**6.1.** At most \(m\) of the \(m+1\) jobs \(s_i\) fit into slot \(1\). So some \(s_i\) runs in slot \(2\) or later, and \(t\) runs in slot \(3\) or later. The schedule \(s_1,\ldots,s_m\mid s_{m+1}\mid t\) has makespan \(3\). The \(s_i\) are pairwise incomparable, so a chain has at most two jobs. For \(m\geq2\), also \(\lceil(m+2)/m\rceil=2\), so neither the chain bound nor the counting bound gives \(3\).

**6.2.** \(A'=\{2,3,5,7\}\). The tuples are \((2,5,7,9)\) and \((2,3,5,7)\). The first order statistic is unchanged, and the other three decrease strictly: \(3<5\), \(5<7\), \(7<9\). For \(x>y\), for instance \(x=10\), we get \(A'=\{2,5,7,10\}\). Its largest element increases, and the tuple becomes lexicographically larger.

**6.3.** *No full schedule.* The first slot of a full schedule of \(J\) consists of four jobs without predecessors in \(J\). Only \(a\) and \(b\) have none.

*Antichains.* The job \(a\) is related only to the \(z_i\), and each \(x_i\) only to \(b\); so \(L\) is an antichain. The job \(b\) is related only to the \(x_i\), and each \(z_i\) only to \(a\); so \(Z\) is an antichain.

*Acceptance without compatibility.* Here \(n=8=mT\) with \(T=2\), and \(J\) is described by the constant \(J\). The set \(L\) is described by one membership leaf, so \(L\in\mathcal F_K\). The state \((\varnothing,L,\varnothing)\) of \(L\) is initial and final, since \(\mathsf A(\varnothing)\) is true; so \(\mathsf A(L)\) is true. The set \(L=J\cap L\) also has a relative description inside \(J\). Without compatibility, \((L,Z,\varnothing)\) would be a state of \(J\) that is both initial and final, and \(J\) would be accepted. Compatibility rejects this state, because \(b\in Z\) precedes \(x_1\in L\).

**6.4.** Every slot contributes a block of exactly \(m\) entries. So the \(j\)-th blocks occupy positions \((j-1)m+1,\ldots,jm\) in both encodings, and the encodings agree on the first \((j-1)m\) positions. The first difference lies inside the \(j\)-th block, and there the first encoding is smaller. All encodings have the same length \(|U|\). Lexicographic order is therefore a total order on sequences of one length, in which "least" makes sense and one sequence is never a proper prefix of another.

**6.5.** Only pairs containing \(x\) or \(y\) can change their order; all other jobs keep their slots. The pairs to check are the following.

- *\(x\) with its predecessors and successors.* By (1), its predecessors in \(U\) are before \(s\leq r\), and its exterior predecessors are before the interval. Its successors are after \(t\).
- *\(y\) with its predecessors and successors.* Its predecessors are before \(r\). By the supposition, its successors in \(U\) are after \(t\), and its exterior successors are after the interval.
- *The pair \(x,y\).* This is covered by the two previous items.

A companion \(w\) in \(r\) is not a successor of \(x\), because \(w\) was earlier than \(x\). It is not a predecessor of \(x\), by (1). A companion \(w\) in \(t\) is not a predecessor of \(y\), because \(w\) was later than \(y\). It is not a successor of \(y\), by the supposition. The original schedule settles everything else, whatever the number \(m-1\) of companions.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 1–5. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
- [NSW] J. Nederlof, C. M. F. Swennenhuis and K. Węgrzycki, *A subexponential time algorithm for makespan scheduling of unit jobs with precedence constraints*, arXiv:2312.03495 (https://arxiv.org/abs/2312.03495).
- [LR] E. Levey and T. Rothvoss, *A (1+ε)-approximation for makespan scheduling with precedence constraints using LP hierarchies*, arXiv:1509.07808 (https://arxiv.org/abs/1509.07808).
- [Garg] S. Garg, *Quasi-PTAS for scheduling with precedences using LP hierarchies*, arXiv:1708.04369 (https://arxiv.org/abs/1708.04369).
- [Li] S. Li, *Towards PTAS for precedence constrained scheduling via combinatorial algorithms*, arXiv:2004.01231 (https://arxiv.org/abs/2004.01231).
- [DW22] S. Das and A. Wiese, *A simpler QPTAS for scheduling jobs with precedence constraints*, arXiv:2501.09091 (https://arxiv.org/abs/2501.09091).
- [drbh] drbh, *scheduling-proof-exploration*, GitHub repository, 2026: an adaptation of the Lean development of the three-machine theorem to four machines, which its README describes as an exploration. https://github.com/drbh/scheduling-proof-exploration
- R. L. Graham, E. L. Lawler, J. K. Lenstra and A. H. G. Rinnooy Kan, *Optimization and approximation in deterministic sequencing and scheduling: a survey* (1979), introduces the three-field notation. https://ir.cwi.nl/pub/18052
- M. Fujii, T. Kasami and K. Ninomiya (1969), E. G. Coffman and R. L. Graham (1972), J. D. Ullman (1975), M. R. Garey and D. S. Johnson (1979), M. R. Garey, D. S. Johnson, R. E. Tarjan and M. Yannakakis (1983), and D. Dolev and M. K. Warmuth (1984) are named for credit. The course does not use their results.
- The main argument of this lesson and of the two lessons on \(m\) machines that follow it follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
