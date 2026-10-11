# Descriptions and a dynamic program

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the algorithm of OpenAI's theorem. It searches a fixed, polynomially large family of job sets, each given by a short Boolean formula, and decides for each of them whether it has a full schedule. Everything the search accepts really has a full schedule. Whether it also accepts every schedulable instance is reduced to a structural statement about schedules, the *bounded-description hierarchy*, which the rest of the course proves. The setting is that of [Unit jobs on three machines](unit-jobs-on-three-machines.md): a padded set \(J\) of \(N=3T\) jobs with a strict partial order \(\prec\), and full schedules made of antichain triples.

## 1. Frames and cones

The order \(\prec\) on \(J\) can be computed from the graph by a search from every vertex, in time polynomial in the input. Fix the linear extension of \(\prec\) obtained by removing, at each step, the remaining job without a remaining predecessor that has the smallest identifier (Lemma 1.2 of the first lesson), and let
\[
\lambda:J\to\{1,\ldots,N\}
\]
be the position of a job in it, its *rank*. If \(x\prec y\), then \(\lambda(x)<\lambda(y)\).

Many arguments run in two directions. The *forward frame* uses \(\prec\), the given direction of time, and \(\lambda\). The *backward frame* uses the reversed order (\(x\) precedes \(y\) backward when \(y\prec x\)), reversed time (slot \(t\) of a schedule with \(T\) slots becomes slot \(T+1-t\)), and the rank \(N+1-\lambda\), which is a linear extension of the reversed order. Reading a full schedule backwards gives a full schedule for the reversed order. Unless a frame is named, every notion in an argument (earlier, predecessor, rank) refers to its working frame.

For a set \(a\) of three jobs, usually the triple of a slot, define its *cones*
\[
\begin{aligned}
D_a&=\{x\in J:y\prec x\text{ for some }y\in a\},\\
P_a&=\{x\in J:x\prec y\text{ for some }y\in a\},
\end{aligned}
\]
and the *weak cones* \(\widehat D_a=D_a\cup a\) and \(\widehat P_a=P_a\cup a\). Reversing the frame exchanges \(D_a\) with \(P_a\), and \(\widehat D_a\) with \(\widehat P_a\).

A set \(U\subseteq J\) is an *upset* if \(x\in U\) and \(x\prec y\) imply \(y\in U\), and a *downset* if \(y\in U\) and \(x\prec y\) imply \(x\in U\). The complement of an upset is a downset, unions and intersections of upsets are upsets, and reversing the frame turns upsets into downsets. The cones \(D_a\) and \(\widehat D_a\) are upsets, since \(\prec\) is transitive; \(P_a\) and \(\widehat P_a\) are downsets. A rank suffix \(\{\lambda\geq k\}\) is an upset and a rank prefix \(\{\lambda\leq k\}\) is a downset, because \(\lambda\) increases along \(\prec\).

Intervals of a schedule may have a virtual boundary before the first or after the last slot. A virtual boundary has no jobs, and its cones are constants chosen to agree with the following lemma: at the virtual boundary before the first slot, \(D=\widehat D=J\) and \(P=\widehat P=\varnothing\); at the virtual boundary after the last slot, \(D=\widehat D=\varnothing\) and \(P=\widehat P=J\). In the backward frame the two virtual boundaries exchange their roles, consistently with the exchange of \(D\) and \(P\).

**Lemma 1.1 (cones and time).** In a full schedule, let \(a\) be a slot. Every job of \(P_a\) is scheduled strictly before \(a\), every job of \(D_a\) strictly after \(a\), and the jobs of \(a\) lie in neither cone. A job scheduled at or before \(a\) does not lie in \(D_a\); a job scheduled at or after \(a\) does not lie in \(P_a\).

*Proof.* If \(x\prec y\) with \(y\in a\), then \(x\) is in an earlier triple than \(y\); similarly for \(D_a\). A job of \(a\) is incomparable with the other jobs of \(a\), and \(y\prec y\) never holds. The last sentence restates the first. \(\square\)

Cone membership is a statement about the order on all of \(J\), not about time. A job that is scheduled before \(a\) need not lie in \(P_a\). The construction in later lessons keeps track of exactly when the two coincide.

## 2. A finite family of descriptions

The *atomic tests* are the following subsets of \(J\), in either frame:

- the constants \(J\) and \(\varnothing\) (true and false);
- the rank thresholds \(\{\lambda\leq k\}\) and \(\{\lambda\geq k\}\) for \(0\leq k\leq N+1\);
- for every set \(a\) of three jobs, membership in \(a\) and membership in each of the cones \(P_a\), \(D_a\), \(\widehat P_a\), \(\widehat D_a\).

A *formula* is a binary tree whose leaves are atomic tests or complements of atomic tests and whose inner nodes are labelled \(\wedge\) or \(\vee\), read as intersection and union. Its *size* is its number of leaves, and \([\![F]\!]\subseteq J\) is the set it describes. Fix the constant
\[
K=10000.
\]
Let \(\mathcal F\) be the family of sets described by formulas of size at most \(K\). A set \(W\) has a *global description* if \(W\in\mathcal F\). A subset \(L\subseteq W\) has a *relative description inside* \(W\) if \(L=W\cap[\![F]\!]\) for some formula \(F\) of size at most \(K\).

**Lemma 2.1 (complements).** For every formula \(F\) there is a formula of the same size describing \(J\setminus[\![F]\!]\).

*Proof.* Replace every leaf by its complement and exchange \(\wedge\) and \(\vee\) at every inner node. By De Morgan's laws, induction on the tree shows that the new formula describes the complement. \(\square\)

**Lemma 2.2 (the family is polynomial).** The number of formulas of size at most \(K\) is at most \(C_KN^{3K}\), where \(C_K\) depends only on \(K\). The sets in \(\mathcal F\) can be listed, as bit vectors of length \(N\), by a deterministic procedure whose running time is bounded by a polynomial in \(N\).

*Proof.* There are \(\binom N3\leq N^3\) sets of three jobs, so the number of possible leaves, counting complements and both frames, is at most \(c\,N^3\) for an absolute constant \(c\) and all \(N\geq3\). A binary tree with \(\ell\) leaves has \(\ell-1\) inner nodes, and there are at most \(4^{\ell}\) tree shapes with \(\ell\) leaves. So there are at most \(4^\ell\cdot2^{\ell-1}\cdot(cN^3)^\ell\) formulas of size \(\ell\), and summing over \(\ell\leq K\) gives at most \(C_KN^{3K}\). The procedure lists all of them, evaluates each leaf on each job from the table of \(\prec\), combines along the tree, and finally removes repeated bit vectors by comparing them in pairs. Each step is polynomial in \(N\) for fixed \(K\). \(\square\)

Since \(N\leq3n\), the family has polynomially many members. The constant \(K\) is far larger than needed: the structural theorem below produces formulas of fewer than \(500\) leaves.

## 3. The dynamic program

The program assigns to every \(W\in\mathcal F\), in order of increasing size, an *acceptance value* \(\mathsf A(W)\in\{\text{true},\text{false}\}\). By convention \(\mathsf A(U)\) is false for every \(U\notin\mathcal F\). Put \(\mathsf A(\varnothing)=\text{true}\), and \(\mathsf A(W)=\text{false}\) when \(|W|\) is not divisible by three.

For a nonempty \(W\in\mathcal F\), a *state* is a decomposition \(W=L\cup Z\cup R\) into disjoint parts such that

- \(Z\) is an antichain of three jobs;
- \(L\) has a relative description inside \(W\);
- the parts are *compatible*: no job of \(Z\cup R\) precedes a job of \(L\), and no job of \(R\) precedes a job of \(Z\).

A state is *initial* if \(\mathsf A(L)\) is true and *final* if \(\mathsf A(R)\) is true. There is a *transition* from \((L,Z,R)\) to \((L',Z',R')\) when
\[
\begin{gathered}
L\cup Z\subseteq L'\quad\text{and}\\
\mathsf A\bigl(L'\setminus(L\cup Z)\bigr)\text{ is true}.
\end{gathered}
\]
All acceptance values consulted belong to sets smaller than \(W\), since each misses at least the three jobs of a state's \(Z\). Set \(\mathsf A(W)\) to true when some initial state reaches some final state through transitions; a single state that is both initial and final counts. The deadline is accepted when \(\mathsf A(J)\) is true.

**Proposition 3.1 (soundness).** If \(\mathsf A(W)\) is true, then \(W\) has a full schedule, and one can be produced along the computation.

*Proof.* By induction on \(|W|\); the empty set has the empty schedule. Let \((L_1,Z_1,R_1),\ldots,(L_k,Z_k,R_k)\) be states forming a path from an initial to a final state. Put
\[
\begin{aligned}
A_0&=L_1,\qquad A_k=R_k,\\
A_i&=L_{i+1}\setminus(L_i\cup Z_i)\quad(1\leq i<k).
\end{aligned}
\]
Since \(L_i\cup Z_i\subseteq L_{i+1}\) and the parts of each state are disjoint, induction on \(i\) shows \(L_{i+1}=A_0\cup Z_1\cup A_1\cup\cdots\cup Z_i\cup A_i\), and therefore
\[
W=A_0\cup Z_1\cup A_1\cup Z_2\cup\cdots\cup Z_k\cup A_k,
\]
a disjoint union in this order. Every \(A_i\) is accepted (it is the left part of an initial state, a set consulted by a transition, or the right part of a final state) and smaller than \(W\), so by induction it has a full schedule. Concatenate these schedules and the triples \(Z_i\) in the displayed order.

The result is a sequence of disjoint antichain triples with union \(W\). Suppose that a job \(y\) of some piece \(Q'\) precedes a job \(x\) of an earlier piece \(Q\) in the displayed order. If \(Q'=Z_j\), then \(Q\) is contained in \(L_j\) and the state \((L_j,Z_j,R_j)\) has a job of \(Z_j\) preceding a job of \(L_j\). If \(Q'=A_j\) with \(j\geq1\), then \(A_j\subseteq R_j\) and \(Q\subseteq L_j\cup Z_j\), and a job of \(R_j\) precedes a job of \(L_j\cup Z_j\). Both contradict compatibility. Within one piece, order is respected by the piece's schedule. So the concatenation is a full schedule of \(W\).

To produce it, record for every state the state from which it was first reached, or mark it as initial. From a reached final state, follow these records back to an initial state, and concatenate the stored schedules of the pieces with the triples. Store the result as the schedule of \(W\). \(\square\)

## 4. Hierarchies

Completeness rests on the following structure. Throughout, a node carries a *witnessing* full schedule of all of \(J\), and the node's job set is the job set of an open interval of that schedule.

**Definition 4.1.** A *bounded-description hierarchy* for a full schedule of \(J\) is a rooted tree of nodes built as follows.

1. The root is the whole schedule, between the two virtual boundaries; its job set is \(J\).
2. At a node with nonempty job set \(W\), the slots of \(W\) may first be replaced by any full schedule of \(W\) (by Lemma 2.2 of the first lesson the whole schedule stays full). Then at least one slot of \(W\) is *marked*. The *children* are the nonempty open intervals between consecutive marks, and between each boundary of the node and the nearest mark. Each child receives its own copy of the current schedule of \(J\) as its witness, and later changes inside one child do not affect its siblings.
3. Every node's job set has a global description.
4. For every mark \(z\) of a node \(W\), the set of jobs of \(W\) scheduled before \(z\) has a relative description inside \(W\).

The copies in item 2 are a bookkeeping device. A child only ever reorders its own slots, and the dynamic program sees nothing but job sets.

**Lemma 4.2.** If a full schedule of \(J\) has a bounded-description hierarchy, the dynamic program accepts \(J\).

*Proof.* We show by induction on \(|W|\) that \(\mathsf A(W)\) is true for the job set \(W\) of every node. If \(W\) is empty this holds by definition; otherwise \(W\in\mathcal F\) by item 3. Let \(z_1,\ldots,z_k\) be the marks of \(W\) in time order, in the schedule current when they were chosen, and let \(L_i\) be the set of jobs of \(W\) before \(z_i\) and \(R_i\) the set after it. Each \((L_i,z_i,R_i)\) is a state: \(z_i\) is an antichain triple, \(L_i\) has a relative description by item 4, and compatibility holds because the schedule respects \(\prec\). The set \(L_1\) is empty or the first child, \(R_k\) is empty or the last child, and \(L_{i+1}\setminus(L_i\cup z_i)\) is empty or the child between \(z_i\) and \(z_{i+1}\). Children are nodes with fewer jobs, because each node has a mark, so all these sets are accepted by induction. Hence \((L_1,z_1,R_1)\) is initial, consecutive states are joined by transitions, and \((L_k,z_k,R_k)\) is final, so \(\mathsf A(W)\) is true. The root gives \(\mathsf A(J)\). \(\square\)

**Theorem 4.3 (structure).** Every full schedule of \(J\) has a bounded-description hierarchy. Moreover, all the global and relative descriptions it uses have fewer than \(500\) leaves.

The proof occupies the next six lessons, ending in [Global descriptions and the running time](global-descriptions-and-the-running-time.md).

**Proof of Theorem 3.1 of the first lesson, assuming Theorem 4.3.** For a deadline \(T\): if \(n>3T\), reject. Otherwise pad to \(J\) and run the dynamic program. If \(J\) has a full schedule, Theorem 4.3 and Lemma 4.2 show that \(\mathsf A(J)\) is true; conversely, if \(\mathsf A(J)\) is true, Proposition 3.1 produces a full schedule. By the padding lemma (Lemma 2.1 of the first lesson), \(\mathsf A(J)\) is true exactly when a schedule with makespan at most \(T\) exists. Remove the isolated padding jobs from the full schedule and give the at most three jobs of each slot to different machines. For the minimum makespan, try \(T=1,2,\ldots,n\) and stop at the first accepted deadline; \(T=n\) is always accepted. The running time is bounded in the last lesson. \(\square\)

## 5. Exercises

**5.1.** Show that every atomic test of the backward frame describes the same set as an atomic test of the forward frame. Why is it still convenient to allow both?

**5.2.** Suppose the family \(\mathcal F\) were replaced by the family of *all* subsets of \(J\). Show that the program would then accept exactly the sets that have full schedules.

**5.3.** In the proof of Proposition 3.1, why does every \(A_i\) have fewer jobs than \(W\)?

**5.4.** Show that the compatibility condition of a state is needed for soundness. Let \(W\) consist of six jobs \(a,b,x,y,z,w\) whose only relations are \(b\prec x\), \(b\prec y\), \(a\prec z\) and \(a\prec w\). Show that \(W\) has no full schedule, although \(W=L\cup Z\) with \(L=\{a,x,y\}\) and \(Z=\{b,z,w\}\) two antichains. What would the program do with the decomposition \((L,Z,\varnothing)\) if compatibility were not required?

**5.5.** Give a full schedule and a slot \(a\) such that some job scheduled before \(a\) is not in \(P_a\).

## 6. Solutions

**5.1.** In the backward frame the rank is \(N+1-\lambda\), so the threshold \(\{N+1-\lambda\leq k\}\) is the forward threshold \(\{\lambda\geq N+1-k\}\), and similarly for the other inequality. The backward cones of \(a\) are the forward cones with \(D\) and \(P\) exchanged. Allowing both frames lets the construction write every formula in its working frame without translating it.

**5.2.** Soundness does not depend on the family. If \(W\) has a full schedule with first triple \(Z\), then \(W\setminus Z\) has a full schedule, so by induction on \(|W|\) it is accepted, and \((\varnothing,Z,W\setminus Z)\) is a state, initial because \(\mathsf A(\varnothing)\) is true and final because \(\mathsf A(W\setminus Z)\) is true.

**5.3.** Every \(A_i\) is disjoint from \(Z_1\), which has three jobs, and a path contains at least one state.

**5.4.** The first triple of a full schedule consists of jobs without predecessors in \(W\), and only \(a\) and \(b\) have none; so there is no full schedule. The job \(a\) is related only to \(z\) and \(w\), and \(b\) only to \(x\) and \(y\), so \(L\) and \(Z\) are antichains. The set \(L\) is a triple, described by a membership test, and its one-triple schedule makes \(\mathsf A(L)\) true. Without the compatibility condition, \((L,Z,\varnothing)\) would be a state that is both initial and final, and the program would accept \(W\). Compatibility rejects it, because \(b\in Z\) precedes \(x\in L\).

**5.5.** Take two slots \(\{1,2,3\}\) and \(\{4,5,6\}\) with no relations at all, and \(a=\{4,5,6\}\). The jobs \(1,2,3\) are scheduled before \(a\), but \(P_a=\varnothing\).

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
