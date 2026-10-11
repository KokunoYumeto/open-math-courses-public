# Unit jobs on three machines

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite set of jobs has to be run on three identical machines. Every job takes one unit of time, and some pairs of jobs are related by precedence: the first job must be finished before the second one starts. How soon can all jobs be finished? This course proves OpenAI's theorem (2026) that a deterministic algorithm finds a shortest schedule in polynomial time. The complexity of this problem had been open since the 1970s. This lesson states the problem precisely, replaces it by an equivalent problem about *full schedules*, proves two elementary facts used throughout, and outlines the proof.

## 1. Schedules

The input is a finite directed acyclic graph \(G=(V,E)\) with \(V=\{1,\ldots,n\}\), \(n\geq1\), listed explicitly. Its vertices are the *jobs*; an arc \((u,v)\in E\) says that \(u\) must be finished before \(v\) starts. Time is divided into *slots*: slot \(t\) is the interval \([t-1,t)\). A *schedule with deadline* \(T\) is a map
\[
\tau:V\to\{1,\ldots,T\}
\]
that takes every value at most three times and satisfies \(\tau(u)<\tau(v)\) for every arc \((u,v)\). Job \(v\) runs during slot \(\tau(v)\); the at most three jobs of a slot are given to different machines. The *makespan* of \(\tau\) is \(\max_v\tau(v)\), the time at which the last job is finished. In the standard notation for scheduling problems this is the problem \(P3\mid\mathrm{prec},p_j=1\mid C_{\max}\): three identical parallel machines, precedence constraints, unit processing times, and the makespan to be minimized.

Write \(x\prec y\) if \(G\) contains a directed path of positive length from \(x\) to \(y\). Since \(G\) is acyclic, \(x\prec x\) never holds, and \(\prec\) is transitive: it is a *strict partial order* on \(V\). We say that \(x\) is a *predecessor* of \(y\), and \(y\) a *successor* of \(x\). Two jobs are *comparable* if one precedes the other; a set of pairwise incomparable jobs is an *antichain*.

**Lemma 1.1.** A map \(\tau:V\to\mathbb Z\) satisfies \(\tau(u)<\tau(v)\) for every arc \((u,v)\) if and only if \(\tau(x)<\tau(y)\) whenever \(x\prec y\).

*Proof.* Every arc is a path of length one. Conversely, along a path \(x=x_0,x_1,\ldots,x_k=y\) with \(k\geq1\) the values \(\tau(x_0)<\tau(x_1)<\cdots<\tau(x_k)\) increase. \(\square\)

In particular the jobs of one slot form an antichain. From now on precedence always means the transitive order \(\prec\). When we restrict attention to a subset of the jobs, we restrict this order; two jobs of the subset may be related through a path that leaves the subset.

**Lemma 1.2 (linear extensions).** Let \(\prec\) be a strict partial order on a finite set \(A\). Remove from \(A\) one element at a time, each time an element that has no predecessor among the elements not yet removed. This is always possible, and listing the elements in the order of removal gives a total order of \(A\) in which \(x\) comes before \(y\) whenever \(x\prec y\).

*Proof.* A nonempty finite set \(B\) has an element without a predecessor in \(B\): otherwise, starting anywhere and repeatedly choosing a predecessor, we would revisit some element \(b\), and transitivity would give \(b\prec b\). If \(x\prec y\), then \(y\) has a predecessor among the remaining elements as long as \(x\) has not been removed, so \(x\) is removed first. \(\square\)

A total order with this property is a *linear extension* of \(\prec\). Applied to the reachability order of an acyclic graph it is a *topological order*. Scheduling the jobs one per slot in a topological order gives a schedule of makespan \(n\), so the optimal makespan lies between \(1\) and \(n\).

**Lemma 1.3 (integer start times suffice).** Suppose every job \(v\) is given a real start time \(s_v\geq0\) and a machine \(\mu(v)\in\{1,2,3\}\), such that two jobs on the same machine run during disjoint intervals \([s_u,s_u+1)\) and \([s_v,s_v+1)\), and \(s_u+1\leq s_v\) for every arc \((u,v)\). Then there is a schedule \(\tau\) whose makespan is at most \(\max_v(s_v+1)\).

*Proof.* On each machine, order its jobs by start time; consecutive jobs \(u,v\) on a machine satisfy \(s_u+1\leq s_v\). Let \(H\) be the graph on \(V\) whose arcs are the arcs of \(G\) and the pairs of consecutive jobs on a machine. Along every arc of \(H\) the start time increases by at least one, so \(H\) is acyclic. Process the jobs in a topological order of \(H\) (Lemma 1.2) and put
\[
s'_v=\max\Bigl(\{0\}\cup\{s'_u+1:(u,v)\in H\}\Bigr).
\]
By induction along this order, \(s'_v\) is an integer and \(s'_v\leq s_v\): for an arc \((u,v)\) of \(H\) we have \(s'_u+1\leq s_u+1\leq s_v\). The new start times still satisfy \(s'_u+1\leq s'_v\) along the arcs of \(H\), so jobs on one machine do not overlap, and every arc of \(G\) is respected. Put \(\tau(v)=s'_v+1\). A slot contains at most one job of each machine, hence at most three jobs, and \(\tau\) respects the arcs of \(G\). Its makespan is \(\max_v(s'_v+1)\leq\max_v(s_v+1)\). \(\square\)

So allowing arbitrary real start times would not shorten the optimum, and the discrete formulation loses nothing.

## 2. Full schedules

The algorithm decides, for a given *deadline* \(T\) with \(1\leq T\leq n\), whether a schedule with makespan at most \(T\) exists. It is convenient to fill every slot.

If \(n>3T\), no schedule exists, since \(T\) slots hold at most \(3T\) jobs. Otherwise add \(3T-n\) new *isolated* jobs, related to no other job, and let \(J\) be the resulting set of
\[
N=|J|=3T
\]
jobs, still ordered by \(\prec\). For a set \(W\subseteq J\), a *full schedule* of \(W\) is a sequence of pairwise disjoint three-element antichains, called *triples*, whose union is \(W\), such that the triple containing \(x\) comes strictly before the triple containing \(y\) whenever \(x\prec y\). A full schedule of \(W\) has exactly \(|W|/3\) triples; the empty set has the empty full schedule.

**Lemma 2.1 (padding).** There is a schedule of \(G\) with makespan at most \(T\) if and only if \(J\) has a full schedule. The padded set has \(N\leq3n\) jobs.

*Proof.* A schedule of makespan at most \(T\), viewed with \(T\) slots, has \(3T-n\) unused machine positions; put the isolated jobs there. Every slot now holds three pairwise incomparable jobs (Lemma 1.1), and the slots in order form a full schedule. Conversely, deleting the isolated jobs from a full schedule of \(J\) leaves a schedule of \(G\) with at most \(T\) slots. Finally \(N=3T\leq3n\) because \(T\leq n\). \(\square\)

From now on we work with one fixed full schedule at a time. Its slots are identified with their triples. For two slots \(a\) and \(b\) with \(a\) before \(b\), the *open interval* \((a,b)\) consists of the slots strictly between them, and the same letter will denote the set of jobs in those slots. We also allow two *virtual* boundaries, one before the first slot and one after the last, so that every set of consecutive slots is an open interval.

**Lemma 2.2 (reordering an open interval).** Let a full schedule of \(J\) be given, and let \(W\) be the job set of an open interval \((a,b)\). Replace the slots of \((a,b)\) by the slots of any full schedule of \(W\), in its order. The result is again a full schedule of \(J\).

*Proof.* The new sequence still consists of disjoint antichain triples with union \(J\). Let \(x\prec y\). If both jobs are in \(W\), the new schedule of \(W\) puts \(x\) first. If neither is in \(W\), nothing changed for them. Suppose \(x\notin W\) and \(y\in W\). In the old schedule \(x\) came before \(y\), so \(x\) is at or before \(a\); it still is, and \(y\) is still strictly after \(a\). The case \(x\in W\), \(y\notin W\) is symmetric: \(y\) is at or after \(b\). \(\square\)

The lemma is what makes a recursive search possible: once some slots of a schedule are fixed, the job sets between them can be scheduled independently of each other.

## 3. The theorem

**Theorem 3.1 (OpenAI, 2026).** There is a deterministic algorithm with the following properties. Its input is an explicitly listed finite directed acyclic graph on \(n\geq1\) unit jobs, and possibly an integer deadline \(1\leq T\leq n\). With a deadline, it decides whether a schedule on three identical machines with makespan at most \(T\) exists, and returns one if so. Without a deadline, it returns a schedule of minimum makespan. On a deterministic multitape Turing machine both tasks take
\[
O\bigl((L+2)^{150020}\bigr)
\]
steps, where \(L\) is the length of the input in binary.

The exponent is enormous, and the theorem makes no practical claim. Its content is that the problem is solvable in polynomial time. The last lesson shows where the exponent comes from and how it can be lowered somewhat; nothing in the proof tries to make it small.

**What was known.** For two machines the problem was solved by Fujii, Kasami and Ninomiya (1969), and Coffman and Graham (1972) gave an optimal list-scheduling rule. When the number of machines is part of the input, the problem is NP-complete (Ullman, 1975). Garey and Johnson (1979) listed the case of three machines among the open problems of their book on NP-completeness. Polynomial algorithms were found for special precedence orders: Garey, Johnson, Tarjan and Yannakakis (1983) for opposing forests, and Dolev and Warmuth (1984) for precedence graphs of bounded height. For general orders, Nederlof, Swennenhuis and Węgrzycki gave an exact algorithm with running time \((1+\frac nm)^{O(\sqrt{nm})}\) on \(m\) machines, subexponential for three machines. Approximation schemes with running times close to polynomial were found by Levey and Rothvoß, Garg, Li, and Das and Wiese. OpenAI's argument starts from the viewpoint of Dolev–Warmuth and Nederlof–Swennenhuis–Węgrzycki, which decomposes a schedule at selected slots, and proves directly that a decomposition exists in which every piece has a short description. The course does not use any of these earlier results.

## 4. The plan

**The finite search** (second lesson, [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md)). Fix a linear extension of \(\prec\). Consider Boolean formulas with a bounded number of leaves, built from tests of the form: the rank of a job is at most \(k\); a job belongs to a given triple; a job precedes, or follows, some job of a given triple. Each formula describes a subset of \(J\), and since the bound on the size is fixed, there are only polynomially many described sets. A dynamic program decides for every described set \(W\), in order of size, whether \(W\) has a full schedule: it looks for a sequence of triples that splits \(W\) into smaller described pieces that are already known to have full schedules. Everything it accepts really has a full schedule. It accepts \(J\) whenever \(J\) has a full schedule, provided a structural theorem holds: every full schedule can be cut recursively, at chosen slots, into intervals that all have short descriptions, *however deep the recursion goes*.

**The structural theorem** (lessons three to eight). A schedule is cut at a *center* slot and then, on each side, at slots chosen by a walk through a priority order. The walk produces *separators*: slots before which every job of a certain high set lies below the slot in the precedence order, and after which every job of the complementary low set lies above it ([Separators and the shared-cutoff walk](separators-and-the-shared-cutoff-walk.md)). Consecutive cut points separate the same low set, which describes the piece between them through cones of its two boundary triples ([Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md)). Naive descriptions would grow with the depth of the recursion. They are kept short by short lists of upward closed sets carried from parent to child ([Carried and pruned lists](carried-and-pruned-lists.md), [Changing direction](changing-direction.md)), by two invariants that control jobs outside each interval ([Boundary invariants](boundary-invariants.md)), and by a final count of formula sizes ([Global descriptions and the running time](global-descriptions-and-the-running-time.md)). The machine count also enters the bound on these lists: at most three of the carried sets can survive in a child, because each of them must contain a different job of the child's boundary triple.

## 5. Exercises

**5.1.** Five jobs \(s_1,s_2,s_3,s_4,t\) with \(s_i\prec t\) for all \(i\) are to be scheduled on three machines. Show that the optimal makespan is \(3\), while the longest chain has two jobs and \(\lceil5/3\rceil=2\).

**5.2.** Show that if a schedule with makespan at most \(T\) exists, then one with makespan at most \(T+1\) exists, and deduce that the optimal makespan can be found with at most \(\lceil\log_2n\rceil+1\) calls of the deadline decision.

**5.3.** Show that Lemma 2.2 fails for a set of slots that is not contiguous: give a full schedule with three slots in which exchanging the jobs of the first and the third slot is not a full schedule, although each slot stays an antichain.

**5.4.** In the proof of Lemma 1.3, why is it necessary to add the arcs between consecutive jobs on one machine to \(H\), instead of setting \(s'_v\) from the arcs of \(G\) alone?

**5.5.** Let \(A\) be finite with a strict partial order. Show that every linear extension of \(\prec\) arises from the removal procedure of Lemma 1.2 for a suitable choice of the removed elements.

## 6. Solutions

**5.1.** At most three of the \(s_i\) fit in slot \(1\), so some \(s_i\) runs in slot \(2\) or later and \(t\) runs in slot \(3\) or later. The schedule \(s_1,s_2,s_3\mid s_4\mid t\) has makespan \(3\). A chain has at most two jobs, since the \(s_i\) are pairwise incomparable.

**5.2.** A schedule with values in \(\{1,\ldots,T\}\) also has values in \(\{1,\ldots,T+1\}\). So feasibility is monotone in \(T\), every deadline \(T\geq n\) is feasible, and binary search over \(\{1,\ldots,n\}\) finds the least feasible deadline with at most \(\lceil\log_2n\rceil+1\) calls; the last successful call returns an optimal schedule.

**5.3.** Take jobs \(1,\ldots,9\) with \(1\prec4\prec7\) and no other relations, and the full schedule \(\{1,2,3\},\{4,5,6\},\{7,8,9\}\). Exchanging the first and the third slot gives \(\{7,8,9\},\{4,5,6\},\{1,2,3\}\), which puts \(7\) before \(4\). Each slot is still an antichain.

**5.4.** Without those arcs, two jobs of one machine could receive the same integer start time, and a slot could receive four jobs. For example, four pairwise incomparable jobs at start times \(0,\tfrac12,1,\tfrac32\) on machines \(1,2,1,2\) would all receive start time \(0\).

**5.5.** Let \(x_1,\ldots,x_m\) be a linear extension. When \(x_1,\ldots,x_{i-1}\) have been removed, \(x_i\) has no predecessor among the remaining elements, since every predecessor of \(x_i\) comes earlier in the list. So removing \(x_1,x_2,\ldots\) in turn is allowed.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/124.md
- [NSW] J. Nederlof, C. M. F. Swennenhuis and K. Węgrzycki, *A subexponential time algorithm for makespan scheduling of unit jobs with precedence constraints*, arXiv:2312.03495 (https://arxiv.org/abs/2312.03495).
- [LR] E. Levey and T. Rothvoss, *A (1+ε)-approximation for makespan scheduling with precedence constraints using LP hierarchies*, arXiv:1509.07808 (https://arxiv.org/abs/1509.07808).
- [Garg] S. Garg, *Quasi-PTAS for scheduling with precedences using LP hierarchies*, arXiv:1708.04369 (https://arxiv.org/abs/1708.04369).
- [Li] S. Li, *Towards PTAS for precedence constrained scheduling via combinatorial algorithms*, arXiv:2004.01231 (https://arxiv.org/abs/2004.01231).
- [DW22] S. Das and A. Wiese, *A simpler QPTAS for scheduling jobs with precedence constraints*, arXiv:2501.09091 (https://arxiv.org/abs/2501.09091).
- R. L. Graham, E. L. Lawler, J. K. Lenstra and A. H. G. Rinnooy Kan, *Optimization and approximation in deterministic sequencing and scheduling: a survey* (1979), introduces the three-field notation. https://ir.cwi.nl/pub/18052
- M. Fujii, T. Kasami and K. Ninomiya (1969), E. G. Coffman and R. L. Graham (1972), J. D. Ullman (1975), M. R. Garey and D. S. Johnson (1979), M. R. Garey, D. S. Johnson, R. E. Tarjan and M. Yannakakis (1983), and D. Dolev and M. K. Warmuth (1984) are named for credit; the course does not use their results.
