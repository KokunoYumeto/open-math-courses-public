# Separators and the shared-cutoff walk

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The structural theorem of [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md) cuts a schedule at chosen slots. This lesson supplies the cut points. A *separator* is a slot such that every job before it that is "high" lies below the slot in the precedence order, and every job after it that is "low" lies above it. Such a slot gives a short description of the jobs scheduled before it. The main result, the *shared-cutoff walk*, shows that when the low set grows by one job at a time along a priority order, separators can be moved forward so that consecutive positions separate the *same* low set. The proofs use exchanges of two jobs in a lexicographically least schedule. Notation (frames, cones, upsets) is that of the second lesson.

## 1. Cutoffs and separators

Fix a frame and a full schedule of \(J\). A *domain* is the job set \(U\) of an open interval of the schedule. A *cutoff* in \(U\) is a set \(S\subseteq U\) that contains every predecessor in \(U\) of each of its members. Its jobs are *low*; the other jobs of \(U\) are *high*, and every successor in \(U\) of a high job is high.

**Definition 1.1.** Let \(S\) be a cutoff in a domain \(U\). A slot \(z\) of the domain is a *separator at cutoff* \(S\) if

- (a) every high job scheduled before \(z\) lies in \(P_z\), and
- (b) every low job scheduled after \(z\) lies in \(D_z\).

The boundary \(a\) just before the domain (a slot outside \(U\), or the virtual boundary) is a separator at cutoff \(S\) if every low job of \(U\) lies in \(D_a\); condition (a) is then empty.

Nothing is required of the jobs in the slot \(z\) itself. For a set \(H\subseteq J\) put
\[
B_z(H)=P_z\cup\bigl(H\setminus\widehat D_z\bigr).
\]

**Lemma 1.2 (the jobs before a separator).** Let the slot \(z\) of the domain \(U\) be a separator at cutoff \(S\), and let \(H\subseteq J\) satisfy \(H\cap U=S\). Then \(B_z(H)\cap U\) is the set of jobs of \(U\) scheduled before \(z\).

*Proof.* A job of \(U\) before \(z\) is either high, and then in \(P_z\) by (a), or low, and then in \(H\) and not in \(\widehat D_z\) (Lemma 1.1 of the second lesson). Conversely, a job of \(P_z\) is before \(z\). A job of \(U\cap H\setminus\widehat D_z\) is low; it is not in \(z\), since \(z\subseteq\widehat D_z\), and it is not after \(z\), since low jobs after \(z\) lie in \(D_z\) by (b). \(\square\)

The point of the lemma is that \(H\) may be any set that agrees with the cutoff on the domain. A cutoff that is hard to describe inside \(U\) can be replaced by a simpler global set.

**Lemma 1.3 (reversal).** A slot \(z\) of \(U\) is a separator at cutoff \(S\) in the forward frame if and only if it is a separator at cutoff \(U\setminus S\) in the backward frame.

*Proof.* The set \(U\setminus S\) contains every successor in \(U\) of its members, so it is a cutoff for the reversed order. In the backward frame, "before \(z\)" means after \(z\), and the backward \(D_z\) is the forward \(P_z\). So condition (b) backward for the low set \(U\setminus S\) says that every job of \(U\setminus S\) after \(z\) (forward: before \(z\)) lies in the forward \(P_z\), which is condition (a) forward for \(S\). In the same way (a) backward is (b) forward. \(\square\)

## 2. Lexicographically least schedules

A *priority order* on a domain \(U\) is a total order of \(U\) in which \(x\) comes before \(y\) whenever \(x\prec y\); a job earlier in it has *better* priority. A prefix of a priority order is a cutoff. Given a full schedule of \(U\), sort the jobs of each slot by priority and read the slots in time order; this gives a sequence of positions in the priority order. A full schedule of \(U\) is *normalized* if its sequence is lexicographically least among the sequences of all full schedules of \(U\). If \(U\) has a full schedule, a normalized one exists, since there are finitely many. Normalized schedules are used only to prove existence; the algorithm never computes them.

An *exchange* of two jobs in different slots moves each into the other's slot.

**Lemma 2.1 (no improving exchange).** Let a normalized full schedule of \(U\) be given and let \(r\) be a slot of \(U\). Reorder the slots of \(U\) strictly after \(r\) in any way that keeps a full schedule of \(U\). Then no job \(y\) at \(r\) can be exchanged with a job \(x\) of better priority scheduled after \(r\) so that the result is a full schedule of \(U\).

*Proof.* Suppose it could. The new schedule agrees with the normalized one before \(r\). At \(r\), one entry \(y\) of the sorted triple is replaced by \(x\) with a smaller position. Decreasing one element of a three-element set can only decrease each of its smallest, middle and largest elements, and it decreases their sum, so the sorted triple becomes lexicographically smaller. The new sequence is therefore lexicographically smaller than the normalized one, a contradiction. \(\square\)

With an empty reordering the lemma says that a normalized schedule admits no exchange that moves a better job into an earlier slot.

## 3. The walk

Fix a domain \(U\) with a normalized full schedule for a priority order. A *position* is a slot of \(U\) or the boundary \(a\) just before \(U\). For a position \(s\) and a cutoff \(L\), an *exception* is a low job of \(L\) scheduled after \(s\) that is not in \(D_s\); condition (b) at \(s\) says that there is none.

**Lemma 3.1 (one advance).** Let \(M\subseteq L\) be two prefixes of the priority order, and let the position \(s\) satisfy condition (a) for \(M\). Suppose there are exceptions for \(L\) at \(s\), let \(t\) be the earliest slot containing one, and let \(x\) be an exception at \(t\). If \(x\in M\), then

1. every predecessor of \(x\) in \(U\) is scheduled strictly before \(s\);
2. every job \(y\notin M\) scheduled at a slot \(r\) of \(U\) with \(s\leq r<t\) precedes some job at \(t\) that is not in \(M\);
3. the slot \(t\) satisfies condition (a) for \(M\).

*Proof.* (1) A predecessor \(w\in U\) of \(x\) lies in \(L\), because \(L\) is a cutoff, and it is scheduled before \(t\). If \(w\) were at \(s\), then \(x\in D_s\). If \(w\) were strictly between \(s\) and \(t\), then \(w\) would be a job of \(L\) after \(s\) at a slot earlier than \(t\); by the choice of \(t\) it is not an exception, so \(w\in D_s\) and again \(x\in D_s\). Both contradict the choice of \(x\).

(2) Suppose \(y\) has no successor in \(U\) at or before \(t\). Exchange \(x\) and \(y\). The job \(x\) moves to \(r\): its predecessors in \(U\) are before \(s\leq r\) by (1), predecessors outside \(U\) are before the whole domain, and its successors are after \(t>r\); a job \(w\) at \(r\) is not a predecessor of \(x\) by (1) and not a successor of \(x\), since it was scheduled before \(x\). The job \(y\) moves to \(t\): its predecessors were before \(r\), its successors in \(U\) are after \(t\) by assumption, and successors outside \(U\) are after the domain; a job \(w\) at \(t\) is not a successor of \(y\) by assumption and not a predecessor, since it was scheduled after \(y\). So the result is a full schedule of \(U\). But \(x\in M\) and \(y\notin M\), and \(M\) is a prefix, so \(x\) has better priority than \(y\), contradicting Lemma 2.1. Hence \(y\) has a successor \(y_1\in U\) at a slot \(r_1\) with \(r<r_1\leq t\), and \(y_1\notin M\) because \(M\) is a cutoff. If \(r_1<t\), repeat with \(y_1\). The slots increase strictly, so after finitely many steps we reach a job at \(t\) outside \(M\) that is a successor of \(y\).

(3) Let \(y\notin M\) be scheduled before \(t\). If it is at a slot \(r\geq s\) of \(U\), use (2). If it is before \(s\), then \(s\) is a slot (there are no jobs of \(U\) before the boundary), and condition (a) at \(s\) gives a job \(w\) at \(s\) with \(y\prec w\); then \(w\notin M\), and (2) applied to \(w\) gives a job at \(t\) above \(w\), hence above \(y\). So \(y\in P_t\). \(\square\)

**Lemma 3.2 (the walk at a fixed cutoff).** Let \(L\) be a prefix and let the position \(s\) satisfy condition (a) for \(L\). Advance repeatedly from the current position to the earliest slot containing an exception for \(L\), until there is none. The walk stops after finitely many advances at a separator for \(L\). It never moves backwards, and it does not move at all if \(s\) is already a separator.

*Proof.* Apply Lemma 3.1 with \(M=L\): every advance lands on a slot satisfying (a). The positions increase strictly, so the walk stops, and at the final position there is no exception, which is condition (b). \(\square\)

**Lemma 3.3 (shared-cutoff walk).** Let \(S\) and \(S^+=S\cup\{p\}\) be consecutive prefixes of the priority order, and let the position \(s\) be a separator at cutoff \(S\). Run the walk of Lemma 3.2 for \(L=S^+\) from \(s\). It stops at a position \(t\geq s\) that is a separator at both cutoffs \(S\) and \(S^+\).

*Proof.* Condition (a) for \(S^+\) holds at \(s\), because the high jobs for \(S^+\) are among those for \(S\). If there is no exception for \(S^+\) at \(s\), then \(s\) separates both cutoffs.

Otherwise, every job of \(S\) after \(s\) lies in \(D_s\) by condition (b) for \(S\), so the only exception is \(p\), and the first advance goes to the slot \(t_1\) of \(p\). By Lemma 3.1 with \(M=L=S^+\), the slot \(t_1\) satisfies (a) for \(S^+\). The high jobs for \(S\) before \(t_1\) are the high jobs for \(S^+\) before \(t_1\), because \(p\) itself is at \(t_1\); so \(t_1\) satisfies (a) for \(S\) as well.

Every later advance starts at a position at or after \(t_1\), so its exception is a job of \(S^+\) different from \(p\), that is, a job of \(S\). Lemma 3.1 with \(M=S\) and with \(M=S^+\) shows that each later target satisfies (a) for both cutoffs. At the final position there is no exception for \(S^+\), which gives condition (b) for \(S^+\) and therefore for the smaller cutoff \(S\). \(\square\)

The walk is needed in a slightly more general setting. Let the priority order be defined on a set \(W\supseteq U\), let \(U\) carry a full schedule normalized for the restricted order, and let the cutoffs be prefixes \(S\subseteq W\) of the order on \(W\), acting on \(U\) through \(S\cap U\). The restriction of a prefix to \(U\) is a prefix of the restricted order, so Lemma 3.3 applies to \(S\cap U\) and \(S^+\cap U\). If the promoted job \(p\) is not in \(U\), these two sets coincide and the walk does not move.

**Corollary 3.4 (separators exist after reordering).** Let \(U\) be the nonempty job set of an open interval, with a full schedule. For every cutoff \(S\) in \(U\) there is a full schedule of \(U\) in which some slot is a separator at cutoff \(S\).

*Proof.* Order \(S\) first and \(U\setminus S\) second, each by rank; since \(S\) is a cutoff, this is a priority order. Take a normalized full schedule of \(U\) for it. The first slot separates the empty cutoff: nothing is scheduled before it, and no job is low. Promote the jobs of \(S\) one at a time in priority order and apply Lemma 3.3 at each step. The final position is a slot that separates \(S\). \(\square\)

## 4. What the walk provides

In the construction of the next lesson, the low set of one side of an interval grows one job at a time, and the walk of Lemma 3.3 is run for every promotion. Only the *final* position of each promotion is kept. Two consecutive kept positions \(s_i\leq s_{i+1}\) both separate the same cutoff \(S_i\). For the jobs strictly between them this means: every low job lies in \(D_{s_i}\), above the left endpoint, and every high job lies in \(P_{s_{i+1}}\), below the right endpoint. This is the information that later turns into a global description of the gap.

## 5. Exercises

**5.1.** Show that the last slot of a full schedule of \(U\) is a separator at cutoff \(U\).

**5.2.** Show that a separator need not exist without reordering. Take two slots \(\{y,u,v\}\) and \(\{x,w,q\}\) without any precedence relations and the cutoff \(S=\{x\}\). Check that neither slot separates \(S\), and find a reordering in which one does.

**5.3.** Show that Lemma 3.1 needs normalization. Let the domain have the two slots \(\{y,u,v\}\) and \(\{x,w,q\}\), without relations, let \(x\) have the best priority and \(y\) the second best, and let the boundary before the domain be a slot \(a\) unrelated to all six jobs. Take \(L=M=\{x\}\) and \(s=a\). Find \(t\), and show that \(t\) does not satisfy condition (a). Which exchange improves the schedule?

**5.4.** In Lemma 1.2, why must the slot \(z\) be excluded through \(\widehat D_z\) rather than \(D_z\)?

**5.5.** Show that in Lemma 3.3 the final position can be strictly later than the slot of \(p\).

## 6. Solutions

**5.1.** Every job is low, so condition (a) concerns no job, and no job is scheduled after the last slot.

**5.2.** For the first slot, condition (b) asks \(x\in D_{\{y,u,v\}}\), which fails. For the second slot, condition (a) asks that the high jobs \(y,u,v\) lie in \(P_{\{x,w,q\}}\), which fails. After exchanging \(x\) and \(y\), the first slot \(\{x,u,v\}\) separates \(S\): nothing is before it, and no low job is after it.

**5.3.** The only exception for \(L=\{x\}\) at \(a\) is \(x\), so \(t\) is the second slot. Condition (a) at \(t\) asks \(y\in P_t\), which fails since there are no relations. Exchanging \(x\) and \(y\) gives the schedule \(\{x,u,v\},\{y,w,q\}\), whose sequence starts with a better position, so the given schedule was not normalized.

**5.4.** A low job in the slot \(z\) itself is in \(H\) but not before \(z\). It is not in \(D_z\), because the jobs of a slot are pairwise incomparable, so only the weak cone \(\widehat D_z\) removes it.

**5.5.** Let the boundary before the domain be a slot \(a=\{\alpha,\beta,\gamma\}\), and let the domain have the slots \(\{p,q,r\}\) and \(\{x,u,v\}\), with the relations \(\alpha\prec x\), \(p\prec u\), \(q\prec u\), \(r\prec v\) and no others. Every job of the first slot has a successor in the domain, so it cannot be in the last slot; the given schedule is the only full schedule of the domain and therefore normalized for the priority order \(x,p,q,r,u,v\). Take \(S=\{x\}\) and \(S^+=\{x,p\}\). The boundary \(a\) separates \(S\), since \(x\in D_a\). The walk for \(S^+\) finds the exception \(p\notin D_a\) and advances to the first slot. There \(x\) is a later low job not in \(D_{\{p,q,r\}}\), so it advances again, to the second slot, where it stops. The final position is later than the slot of \(p\), and it separates both cutoffs: \(p\prec u\), \(q\prec u\) and \(r\prec v\).

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
- [NSW] J. Nederlof, C. M. F. Swennenhuis and K. Węgrzycki, *A subexponential time algorithm for makespan scheduling of unit jobs with precedence constraints*, arXiv:2312.03495 (https://arxiv.org/abs/2312.03495); decompositions of schedules at selected slots go back to D. Dolev and M. K. Warmuth (1984), named for credit.
