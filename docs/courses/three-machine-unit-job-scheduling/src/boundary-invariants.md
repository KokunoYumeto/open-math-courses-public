# Boundary invariants

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Every node carries three invariants, introduced in [Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md). The first, which places the old high jobs below the right boundary and the others above the left boundary, was proved for every child in [Carried and pruned lists](carried-and-pruned-lists.md). This lesson proves the other two for every child. (I2) keeps qualifiers that are scheduled at or before the left boundary below that boundary in the precedence order, however far in the past they lie. (I3) forbids certain exchanges with the boundary slot after *any* later rearrangement of the interval. The proof of (I2) for a child uses (I3) for the parent, and the proof of (I3) for a child uses (I3) for the parent; neither uses anything about deeper nodes.

Fix a node \(W\) with boundaries \(a,b\), a side with working frame and normalized open part \(E\), and a child \(W'\) on that side with edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\). All notions refer to the working frame, which is the child's tag. For a same side it is also the tag of \(W\).

## 1. Preparatory reorderings

Before its children are formed, the schedule of \(W\) is changed: a full schedule of \(W\) is chosen so that the center is a separator, and the two sides are normalized. These changes keep the invariants of \(W\). (I1) concerns the job set of \(W\), which does not change. (I2) concerns jobs at or before \(a\) and the triple \(a\), which do not move. (I3) quantifies over all full schedules of \(W\) placed in its slots.

## 2. Distant qualifiers

**Lemma 2.1 ((I2) for the child).** Every qualifier of the child's list scheduled at or before \(a'\) lies in \(\widehat P_{a'}\).

*Proof.* Pruning only removes qualifiers, so it suffices to consider the list before pruning. Let \(z\) be one of its qualifiers, scheduled at or before \(a'\).

*Case \(z\) after \(a\).* Then \(z\) lies in \(E\), at or before \(a'\), and \(a'\) is a slot of \(E\). By Lemma 2.1 of the fifth lesson, \(z\) is high at the edge cutoff \(S\). If \(z\) is in the slot \(a'\), then \(z\in\widehat P_{a'}\). Otherwise \(z\) is a high job before \(a'\), which separates \(S\) on \(E\), so \(z\in P_{a'}\).

*Case \(z\) at or before \(a\).* The injection \(D_a\setminus P_b\) and the two entries of a switch pair contain no job scheduled at or before \(a\) (Lemma 1.1 of the second lesson and Lemma 3.2 of the sixth lesson). So the update is a same update and \(z\) qualifies through the carry. The carry's qualifiers are qualifiers of the list of \(W\) (Lemma 1.1 of the fifth lesson), so (I2) for \(W\) gives a job \(y\) in the slot \(a\) with \(z=y\) or \(z\prec y\). The union of the carry is an upset, so \(y\) also qualifies through the carry; in particular \(a\) is a slot. If \(a'=a\), then \(z\in\widehat P_{a'}\).

Suppose \(a'>a\). Follow every advance of the walk from \(a\) up to the position \(s_i=a'\), including advances whose end positions were not kept as marks. Each advance happens during some promotion \(j\leq i\) and uses the cutoff \(S_j\subseteq S_i\). The carry selects in \(W\) exactly the jobs of \(O\setminus S_i\), so every carry qualifier in \(E\) is high at every one of these advances.

*The first advance.* It leaves \(a\) for the slot \(t\) of an exception \(x\), during promotion \(j\).

1. Every predecessor of \(x\) in \(J\) is scheduled strictly before \(a\). Indeed, it is scheduled before \(t\). If it were in \(a\), then \(x\in D_a\). If it were strictly between \(a\) and \(t\), it would be a job of \(E\) in the cutoff \(S_j\), scheduled before the earliest exception, hence in \(D_a\), and again \(x\in D_a\). But an exception at \(a\) is not in \(D_a\).
2. The key of \(x\) is smaller than the key of \(y\). Indeed, \(x\in W\setminus D_a\), so \(x\in O\) by (I1), and \(x\notin S_0\subseteq D_a\); as \(x\in S_j\subseteq S_i\), it was promoted by stage \(i\), and the jobs of \(O\) are promoted in key order. So its key is smaller than the least unpromoted key \((d,r)\), while the carry qualifier \(y\) has key at least \((d,r)\) (Lemma 1.1 of the fifth lesson).
3. By (I3) for \(W\), applied to the current schedule of \(W\), exchanging \(x\) and \(y\) does not give a full schedule of \(J\).
4. If \(y\) had no successor scheduled at or before \(t\), the exchange would give one. The job \(x\) moves into the slot \(a\): its predecessors are before \(a\), its successors after \(t\), and no job of \(a\) is a predecessor of \(x\) (as \(x\notin D_a\)) or a successor of \(x\) (it is scheduled earlier). The job \(y\) moves to \(t\): its predecessors are before \(a\), its successors after \(t\) by assumption, and no job at \(t\) is a successor of \(y\) (by assumption) or a predecessor (it is scheduled later). So \(y\) has a successor \(y_1\) scheduled after \(a\) and at or before \(t\), in \(E\), and \(y_1\) qualifies through the carry.
5. Every carry qualifier \(c\) scheduled strictly between \(a\) and \(t\) has a successor at or before \(t\). Otherwise exchanging \(c\) and \(x\) inside \(E\) gives a full schedule of \(E\), as in Lemma 3.1 of the third lesson, with \(x\in S_j\) of better priority than the high job \(c\), contradicting Lemma 2.1 of the third lesson. The successor qualifies through the carry.

Following successors from \(y\) through items 4 and 5, with strictly increasing times, reaches a carry qualifier at \(t\) above \(y\). It is not \(x\), which is low.

*Later advances.* An advance from a slot \(s\) of \(E\) to a slot \(t'\) uses a cutoff \(S_j\) that contains its exception, and Lemma 3.1 of the third lesson (part 2, with \(M=L=S_j\)) shows that every job outside \(S_j\) at \(s\) precedes a job at \(t'\) outside \(S_j\). A carry qualifier at \(s\) is such a job, and its successor at \(t'\) again qualifies through the carry.

By induction along the advances, \(y\) precedes a job in the slot \(a'\). Hence \(z\in\widehat P_{a'}\). \(\square\)

## 3. Exchanges after reordering

**Lemma 3.1 ((I3) for the child).** Replace the slots of \(W'\) by any full schedule of \(W'\). Then no exchange of a job \(x\in W'\setminus D_{a'}\) with a qualifier \(y\) of the child's pruned list in the slot \(a'\), where the child's key of \(x\) is smaller than that of \(y\), gives a full schedule of \(J\).

*Proof.* By (I1) for the child, \(x\) is a qualifier, and by Lemma 1.2 of the fifth lesson the key of \(x\) is smaller than that of \(y\) already in the list before pruning.

*Case \(a'>a\).* Both \(x\) and \(y\) lie in \(E\), and both are high at \(S\) (Lemma 2.1 of the fifth lesson). On \(W\setminus S\) the new keys are ordered like the side's priority order, so \(x\) has better priority than \(y\). The reordering of \(W'\) changes only slots strictly after \(a'\). If the exchange gave a full schedule of \(J\), its slots in \(E\) would form a full schedule of \(E\) that contradicts Lemma 2.1 of the third lesson, with \(r=a'\).

*Case \(a'=a\).* On a switched side there is no qualifier in \(a\) at all (Lemma 3.2 of the sixth lesson). On a same side, \(x\notin D_a\) and \(y\notin D_a\), because no job of a slot lies in its own cone; so neither lies in the injection, and both qualify through the carry. By Lemma 1.1 of the fifth lesson their keys in \(W\)'s list compare in the same way. Moreover \(x\in W\setminus D_a\) and \(y\) is a qualifier of \(W\)'s list in \(a\). The preparatory reorderings of \(W\) followed by the given reordering of \(W'\) form a full schedule of \(W\) in its slots, and (I3) for \(W\) forbids the exchange. \(\square\)

## 4. The construction is valid

**Proposition 4.1.** Starting from any full schedule of \(J\), the construction of the fourth to seventh lessons is defined at every node. Every list has at most five entries, each with at most \(25\) leaves, and every node satisfies (I1), (I2) and (I3). Every branch of the hierarchy is finite.

*Proof.* By induction from the root, whose data were given in the fourth lesson. Given a node whose ancestors and own data are valid, the center and the normalized sides exist (Corollary 3.4 of the third lesson and Lemma 2.2 of the first lesson), and the walk defines the children with their edge data (Lemma 4.2 of the fourth lesson). The child's list is defined by a same update or by a switched update with the upset of Lemma 3.2 of the sixth lesson, built from earlier data only. Lemma 2.1 of the fifth lesson gives (I1), Lemma 3.2 of the fifth lesson the length, Lemma 4.1 of the sixth lesson the size, and Lemmas 2.1 and 3.1 above give (I2) and (I3). Every child misses the center of its parent, so job sets shrink strictly along a branch. \(\square\)

## 5. Exercises

**5.1.** In the proof of Lemma 2.1, why can the first advance not be handled by Lemma 2.1 of the third lesson, as the later ones are?

**5.2.** Why does the proof follow every advance of the walk, including those whose end positions were not kept as marks?

**5.3.** In the case \(a'>a\) of Lemma 3.1, why is the qualifier \(y\) in \(a'\) a high job of \(E\)?

**5.4.** In the second case of Lemma 2.1, why can \(z\) not qualify through the switch pair of a switched update?

**5.5.** Show that (I2) for a node already implies the following: a qualifier scheduled at or before \(a\) that is not in the slot \(a\) is a predecessor of some job in \(a\). Why is this the form in which (I2) is used for the child's global description in the next lesson?

## 6. Solutions

**5.1.** The first advance compares the exception \(x\) with a job \(y\) in the boundary slot \(a\), which lies outside \(E\). Normalization of \(E\) only controls exchanges between two jobs of \(E\). The exchange with the boundary is controlled by (I3) for the parent instead.

**5.2.** A carry qualifier's successor at the next kept position is obtained by following one advance at a time; at each intermediate position the chain passes through a job in that slot. Skipping intermediate positions would skip the slots through which the chain runs.

**5.3.** The slot \(a'\) lies in \(E\subseteq W\), and the qualifiers in \(W\) of the list before pruning are exactly the jobs of \(W\setminus S\) (Lemma 2.1 of the fifth lesson). A qualifier of the pruned list is a qualifier before pruning.

**5.4.** The second entry \(D_a\) contains only jobs scheduled strictly after \(a\), and the first entry is contained in \(G\), which contains no job scheduled at or before \(a\) by Lemma 3.2 of the sixth lesson.

**5.5.** \(\widehat P_a=P_a\cup a\), so a qualifier outside the slot \(a\) lies in \(P_a\). The global description of a child selects its high jobs as qualifiers below \(b'\) that are not in \(\widehat P_{a'}\); (I2) guarantees that this test removes every qualifier at or before \(a'\), so that the description does not pick up qualifiers from the distant past.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
