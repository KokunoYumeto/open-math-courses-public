# Centers, sides and edge cutoffs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson describes how the hierarchy of [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md) is built from a full schedule of \(J\). Each node is cut at a *center* slot. Each of the two sides of the center is then cut further at the positions of the shared-cutoff walk from [Separators and the shared-cutoff walk](separators-and-the-shared-cutoff-walk.md), run along a priority order chosen from the node's data. Every node also carries a short list of upward closed sets and satisfies three invariants. The next three lessons show how a child receives its own list and invariants; this lesson defines the data and proves the facts about the cut points.

## 1. Nodes, lists and invariants

A *node* is the job set \(W\) of an open interval of its witnessing full schedule of \(J\). It has a *tag*, one of the two frames, and in the tag frame its boundaries are \(a\) before \(W\) and \(b\) after \(W\); either may be virtual. The node carries a *list*
\[
\mathcal K=(K_1,\ldots,K_\ell)
\]
of upsets of \(J\) in the tag frame. Every entry is a fixed subset of \(J\), given by a formula whose cones belong to fixed triples of jobs; later changes of the schedule do not change it. The *qualifiers* are the jobs of \(\mathcal Q(\mathcal K)=K_1\cup\cdots\cup K_\ell\), and the *old high set* of the node is \(O=W\cap\mathcal Q(\mathcal K)\). A qualifier \(x\) has the *key*
\[
\operatorname{key}(x)=\bigl(\max\{i:x\in K_i\},\ \lambda(x)\bigr),
\]
compared lexicographically, where \(\lambda\) is the rank in the tag frame. The largest index matters, not the smallest; entries may overlap. Different qualifiers have different keys, because their ranks differ.

**Lemma 1.1.** If \(x\) is a qualifier and \(x\prec y\), then \(y\) is a qualifier and \(\operatorname{key}(x)<\operatorname{key}(y)\).

*Proof.* Every entry containing \(x\) is an upset and contains \(y\), so the largest index for \(y\) is at least that for \(x\). If they are equal, \(\lambda(x)<\lambda(y)\) decides. \(\square\)

The node satisfies three invariants, stated in its tag frame.

- **(I1)** \(O\subseteq P_b\) and \(W\setminus O\subseteq D_a\).
- **(I2)** Every qualifier scheduled at or before \(a\) lies in \(\widehat P_a\).
- **(I3)** Replace the slots of \(W\) by any full schedule of \(W\), leaving the rest of the schedule unchanged. Then no exchange of a job \(x\in W\setminus D_a\) with a qualifier \(y\) in the slot \(a\), where \(\operatorname{key}(x)<\operatorname{key}(y)\), gives a full schedule of \(J\).

By (I1), every job of \(W\setminus D_a\) is in \(O\), so its key is defined. If \(a\) is virtual, nothing is scheduled at or before it, and (I2) and (I3) say nothing. The first invariant concerns the jobs inside the interval. The second concerns qualifiers outside it, possibly far in the past. The third keeps the second true when the interval is later rearranged: a normalized schedule controls exchanges inside an interval, but not exchanges with the boundary slot, which lies outside.

**The root.** Its tag is the forward frame, both boundaries are virtual, and its list is \((J)\). Then \(O=J\subseteq P_b=J\) and \(W\setminus O=\varnothing\), so (I1) holds, and (I2) and (I3) are empty.

## 2. The center

In either frame, write \(a\) and \(b\) for the boundaries of \(W\) in that frame, and put
\[
X=W\setminus D_a,\qquad Y=W\setminus P_b.
\]

**Lemma 2.1 (cover).** In either frame,
\[
\begin{gathered}
W\subseteq D_a\cup P_b,\\
X\subseteq P_b,\qquad Y\subseteq D_a .
\end{gathered}
\]
The set \(X\) is a cutoff in \(W\), and \(W\setminus Y=W\cap P_b\) is a cutoff in \(W\).

*Proof.* In the tag frame, (I1) gives \(X\subseteq O\subseteq P_b\) and \(Y\subseteq W\setminus O\subseteq D_a\), and \(W=O\cup(W\setminus O)\subseteq P_b\cup D_a\). Passing to the other frame exchanges the roles of the boundaries and of the cones: the new left boundary is \(b\), whose new \(D\)-cone is the old \(P_b\), and the new \(P\)-cone of \(a\) is the old \(D_a\). So the three statements are the same statements with \(X\) and \(Y\) exchanged. Finally \(X=W\cap(J\setminus D_a)\) and \(W\cap P_b\) are intersections of \(W\) with downsets, which are cutoffs. \(\square\)

In the tag frame the set \(W\cap P_b\) is a cutoff in \(W\). By Corollary 3.4 of the third lesson, after replacing the schedule of \(W\) by another full schedule of \(W\) if necessary, some slot \(v\) of \(W\) is a separator at cutoff \(W\cap P_b\), with domain \(W\). Mark \(v\); it is the *center* of the node. At the root take for \(v\) the last slot, which separates \(J\) (Exercise 5.1 of the third lesson). From now on the center and the job sets on its two sides are fixed.

## 3. Two sides

The part of \(W\) before \(v\) in the tag frame and the part after \(v\) are treated alike: each is the part of \(W\) before \(v\) in a suitable *working frame*, the tag frame for the first and the opposite frame for the second. We call the side *same* if its working frame is the tag and *switched* otherwise. For a side, write \(a\) and \(b\) for the boundaries of \(W\) in its working frame, and let \(E\) be the set of jobs of \(W\) strictly between \(a\) and \(v\), the open interval \((a,v)\) in that frame. The center separates the *center cutoff* \(S_*\), with domain \(W\), in the working frame, where \(S_*=W\cap P_b\) for the same side and \(S_*=X=W\setminus D_a\) for the switched side. For the same side this is the choice of \(v\). For the switched side, the tag frame's \(W\cap P_b\) has complement \(W\setminus P_b\) in \(W\), and in the working frame this complement is \(W\setminus D_a=X\); Lemma 1.3 of the third lesson turns the separator into one for the complement.

**Priority orders.** Each side uses a priority order on all of \(W\), and a sequence of cutoffs obtained by *promoting* jobs from high to low one at a time:

- *Same side.* Put \(S_0=(W\setminus O)\cap P_b\). Order \(S_0\) by rank, then \(O\) by key, then \(Y\) by rank. Promote the jobs of \(O\) in key order.
- *Switched side.* Put \(S_0=\varnothing\). Order \(X\) by rank, then \(W\cap D_a\) by rank. Promote the jobs of \(X\) in rank order.

Here rank is the rank of the working frame, and keys are those of the node's list, which is in the tag frame, the working frame of the same side.

**Lemma 3.1.** On each side these are priority orders on \(W\). The promotions produce prefixes \(S_0\subseteq S_1\subseteq\cdots\subseteq S_q=S_*\) of the order, each \(S_i\) is contained in \(P_b\), and \(S_0\subseteq D_a\).

*Proof.* *Same side.* Since \(O\subseteq P_b\), the sets \(S_0\), \(O\) and \(Y\) partition \(W\). If \(w\prec x\) with \(x\in S_0\) and \(w\in W\), then \(w\in P_b\), as \(P_b\) is a downset, and \(w\notin O\), since otherwise \(x\) would be a qualifier; so \(S_0\) is a cutoff in \(W\). The set \(Y\) is the complement in \(W\) of the cutoff \(W\cap P_b\), so no job of \(Y\) precedes a job of \(S_0\cup O\). Inside \(O\) the key order extends \(\prec\) by Lemma 1.1, and rank extends \(\prec\) inside the other two groups. Hence the order extends \(\prec\). The cutoffs are \(S_0\) together with an initial segment of \(O\) in key order, they are prefixes, and \(S_q=S_0\cup O=W\cap P_b\). By (I1), \(S_0\subseteq W\setminus O\subseteq D_a\).

*Switched side.* \(X\) is a cutoff in \(W\) and \(W\cap D_a\) is its complement, so the order extends \(\prec\). The cutoffs are rank prefixes of \(X\), with \(S_q=X\subseteq P_b\) by Lemma 2.1. \(\square\)

**Normalizing the sides.** On each side, replace the schedule of \(E\) by a normalized full schedule of \(E\) for the restriction of the side's priority order, in the working frame. This keeps a full schedule of \(J\) (Lemma 2.2 of the first lesson), because \(E\) is the job set of an open interval. It keeps the center a separator, because the separator conditions only depend on which jobs lie on which side of \(v\). The two sides are disjoint intervals and are normalized independently, before any child is constructed.

## 4. The walk and the children

Work on one side, in its working frame, with the domain \(E\) and the priority order on \(W\) acting on \(E\) through restriction (the general setting of Lemma 3.3 of the third lesson). The boundary \(a\) is the position just before \(E\), and it separates \(S_0\) on \(E\): the low jobs of \(E\) lie in \(S_0\subseteq D_a\).

Put \(s_0=a\). For \(i=1,\ldots,q\), run the shared-cutoff walk for the promotion from \(S_{i-1}\) to \(S_i\), starting at \(s_{i-1}\), and let \(s_i\) be its *final* position. Put \(s_{q+1}=v\). The walk moves only forward and only to slots of \(E\), so
\[
a=s_0\leq s_1\leq\cdots\leq s_q<s_{q+1}=v.
\]
Some promoted jobs may lie outside \(E\), on the other side or in \(v\); such a promotion does not move the walk.

**Lemma 4.1.** For \(0\leq i\leq q\), the positions \(s_i\) and \(s_{i+1}\) both separate the cutoff \(S_i\) on \(E\); for \(i=q\) this means that \(s_q\) separates \(S_q\) and that every high job of \(E\) for \(S_q\) lies in \(P_v\).

*Proof.* By Lemma 3.3 of the third lesson, \(s_i\) separates \(S_{i-1}\) and \(S_i\) for \(1\leq i\leq q\), and \(s_0\) separates \(S_0\). So \(s_i\) and \(s_{i+1}\) separate \(S_i\) for \(i<q\). For \(i=q\), the center separates \(S_*=S_q\) on \(W\), and condition (a) on \(W\) includes all jobs of \(E\). \(\square\)

**Marks and children.** On each side, mark the positions \(s_1,\ldots,s_q\) that are slots of \(E\) (that is, different from \(a\)), in addition to the center. For every \(i\) with \(s_i<s_{i+1}\), the slots strictly between them form a *gap* with *edge data*
\[
a'=s_i,\qquad b'=s_{i+1},\qquad S=S_i,
\]
and if the gap \(W'\) is nonempty it becomes a *child*, tagged with the working frame of the side. Consecutive distinct positions are the endpoints of exactly one such step, so the children are exactly the nonempty open intervals between consecutive marks, and between the boundary \(a\) and the first mark, as required by the definition of a hierarchy.

**Lemma 4.2 (edge labels).** For a child \(W'\) with edge data \(a',b',S\): the right endpoint \(b'\) is a slot of \(W\) (in \(E\), or the center), and the left endpoint \(a'\) is \(a\) or a slot of \(E\). Moreover
\[
\begin{aligned}
W'\cap S&\subseteq D_{a'}\cap P_b,\\
W'\setminus S&\subseteq P_{b'}.
\end{aligned}
\]
The child does not contain the center, so it has fewer jobs than \(W\). At the root the switched side is empty.

*Proof.* The positions are \(a\) or slots of \(E\), and \(s_{q+1}=v\). The child lies in \(E\). Its low jobs are after \(a'\), which separates \(S\) on \(E\) by Lemma 4.1, so they lie in \(D_{a'}\); they lie in \(P_b\) because \(S\subseteq P_b\) (Lemma 3.1). Its high jobs are before \(b'\), which separates \(S\), so they lie in \(P_{b'}\). At the root the center is the last slot, and nothing follows it. \(\square\)

It remains to give every child a list that selects exactly its high jobs \(W'\setminus S\) and to prove (I1), (I2) and (I3) for it. This is done in the next three lessons by induction from the root downwards: when a child is constructed, the data of its parent and of all its ancestors already exist, and nothing about deeper nodes is used.

## 5. Exercises

**5.1.** Show that at the root the walk never moves: \(s_i=s_0\) for all \(i\). Deduce that the root has exactly one child, the set of all jobs before the last slot, with edge cutoff \(J\), so that all its jobs are low.

**5.2.** On a same side, show that no job of \(Y\) is ever promoted, so every job of \(Y\cap E\) is high at every edge of the side.

**5.3.** Why does the walk of a side start at the boundary \(a\), and not at the first slot of \(E\)?

**5.4.** Show that a position \(s_i\) equal to \(a\) is not a mark, and that every mark lies in \(W\).

**5.5.** Suppose a node has \(W\subseteq P_b\) in its tag frame. What are the center cutoffs of its two sides?

## 6. Solutions

**5.1.** At the root the boundary \(s_0\) is the virtual boundary before the first slot, whose cone \(D\) is all of \(J\). So no low job is ever an exception at \(s_0\), and every walk stops at once. The only step with \(s_i<s_{i+1}\) is the last one, from \(s_q=s_0\) to the center, with cutoff \(S_q=S_*=J\cap P_b=J\).

**5.2.** The same side promotes only jobs of \(O\), and \(Y\) is disjoint from \(O\) because \(O\subseteq P_b\). So \(Y\cap S_i=Y\cap S_0=\varnothing\), since \(S_0\subseteq P_b\).

**5.3.** The walk needs a starting position that separates \(S_0\) on \(E\). The boundary \(a\) does, because \(S_0\subseteq D_a\) (Lemma 3.1). The first slot of \(E\) need not: a low job after it need not lie above it. Starting at \(a\) also makes the gap between \(a\) and the first mark a child whose low jobs lie in \(D_a\), as Lemma 4.2 requires.

**5.4.** Only positions that are slots of \(E\) are marked, and \(E\subseteq W\); the center is a slot of \(W\).

**5.5.** For the same side \(S_*=W\cap P_b=W\). For the switched side, the working frame's left boundary is the tag frame's \(b\), whose cone \(D\) in the working frame is the tag frame's \(P_b\); so \(X=W\setminus P_b=\varnothing\) in tag-frame terms, and the switched side's cutoff is empty: every job of that side is high.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
