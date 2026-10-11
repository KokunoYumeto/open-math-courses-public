# Changing direction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A child created on a switched side receives the switch pair of [Carried and pruned lists](carried-and-pruned-lists.md), built from an upset \(G\) that covers the parent's set \(X\) and avoids everything scheduled at or before the parent's boundary. This lesson constructs \(G\). The construction looks one step up, at the edge by which the parent was created, and needs a global description of that edge's low set. Done naively, such descriptions nest: the switch entry of one run would contain the switch entry of the previous run, and formulas would grow with the number of direction changes. The *flattening* lemma removes this history, and every entry of every list then has at most 25 leaves.

Notation is as before: \(W\) is a node, \(U\) its parent, and boundaries, cones and ranks refer to the frame named in each statement.

## 1. Flattening a run

Consider a run that began on a switched side of a node \(Q_0\). In the run's frame, let \(a_0\) be the boundary of \(Q_0\) before it, and let the run's initial entries be
\[
G_0\cap\{\lambda\geq h_0\},\qquad D_{a_0},
\]
where \(G_0\) is an upset with \(Q_0\setminus D_{a_0}\subseteq G_0\).

**Lemma 1.1 (local flattening).** Let \(U\subseteq Q_0\) be a node of this run, and suppose that a carry formed at a same update out of \(U\) still contains the entry descended from the first initial entry, in the form \(G_0\cap\{\lambda\geq k\}\). Then the union of the carried entries descended from the two initial entries agrees on \(U\) with the upset
\[
D_{a_0}\cup\{\lambda\geq k\}.
\]

*Proof.* A carry keeps a suffix of the list, starting at some index \(d\), and trims only entry \(d\). If \(d\) were the index of the second initial entry or a later one, the first would be discarded, permanently. So as long as the first initial entry survives, the second is never trimmed by a carry; it is either still present, unchanged, or it was deleted by pruning on some node of the run containing \(U\). In the second case \(D_{a_0}\) is disjoint from that node and hence from \(U\).

On \(U\cap D_{a_0}\), the second entry, when present, selects every job. The jobs of \(U\setminus D_{a_0}\) lie in \(Q_0\setminus D_{a_0}\subseteq G_0\), so on them the first entry selects exactly the jobs with \(\lambda\geq k\), and the second selects none. Hence on \(U\) the union is \(U\cap(D_{a_0}\cup\{\lambda\geq k\})\). Both sets in the union are upsets. \(\square\)

The flattened set agrees with the carried pair on \(U\) only; outside \(U\) the two may differ. That is all the next lemma needs.

## 2. A short extension of an earlier low set

**Lemma 2.1.** Let \(U\to W\) be an edge of the hierarchy, with low cutoff \(H\subseteq U\) in its working frame. There is a downset \(H^*\) of \(J\) in that frame with \(H^*\cap U=H\), described by a formula with at most \(21\) leaves.

*Proof.* Use the boundaries \(a_U\), \(b_U\) of \(U\) in the edge's working frame.

*The edge is on a switched side of \(U\).* Then \(H\) consists of the jobs of \(U\setminus D_{a_U}\) of rank at most \(r\), where \(r\) is the largest rank in \(H\) (or \(r=0\)). Take
\[
H^*=(J\setminus D_{a_U})\cap\{\lambda\leq r\},
\]
an intersection of two downsets, with two leaves.

*The edge is on a same side of \(U\).* Let \(\Phi\) be the union of the carry formed at this edge, before the injection. The carry's qualifiers in \(U\) are the unpromoted jobs of \(U\)'s old high set, and \(S_0\) is disjoint from the old high set, so
\[
H=(U\cap P_{b_U})\setminus\Phi .
\]
The carry comes from a pruned list, so it has at most five entries (Lemma 3.2 of the fifth lesson), each of the form described in Lemma 3.1 of the fifth lesson. If the run of \(U\) began at the root, every entry is the root entry or an injection, intersected with at most one rank suffix. If it began on a switched side, the only entry that may be complicated is the one descended from the first entry of the switch pair. If it is in the carry, replace it, together with the second entry of the pair if that is present, by the upset of Lemma 1.1; this changes \(\Phi\) outside \(U\) but not on \(U\). Now every term has at most four leaves: an injection with a rank suffix has three (\(D\), complement of \(P\), rank), the root entry with a rank suffix and the second switch entry with a rank suffix have at most two, and the flattened set has two. With at most five terms, the new union \(\Phi'\) has at most \(20\) leaves and \(\Phi'\cap U=\Phi\cap U\). Put
\[
H^*=P_{b_U}\cap(J\setminus\Phi'),
\]
a downset with at most \(21\) leaves and \(H^*\cap U=H\). An empty carry is the constant false. \(\square\)

## 3. The switch upset

Suppose a switched side of a node \(W\) produces a nonempty child. Then \(W\) is not the root (Lemma 4.2 of the fourth lesson). Let \(U\) be the parent of \(W\). The edge \(U\to W\) was taken in the tag frame of \(W\), which is opposite to the working frame of the current side. In the *current* frame write \(a_-,b_-\) for the boundaries of \(U\), \(v_-\) for the center of \(U\), and \(a,b\) for the boundaries of \(W\).

**Lemma 3.1 (the arrangement).** In the current frame, the boundary \(a\) is a slot, and the times satisfy
\[
a_-<v_-\leq a<b\leq b_-.
\]

*Proof.* In the old frame, \(W\) was a gap on the side of \(U\) before \(v_-\): its left endpoint \(a'\) and right endpoint \(b'\) satisfy \(a'\geq\) the left boundary of \(U\), \(b'\leq v_-\), and \(b'\) is a slot (Lemma 4.2 of the fourth lesson); the right boundary of \(U\) comes after \(v_-\). Reversing time turns the old right boundary of \(U\) into \(a_-\), the old \(b'\) into \(a\), the old \(a'\) into \(b\), and the old left boundary of \(U\) into \(b_-\). \(\square\)

The equality \(a=v_-\) occurs when \(W\) is the gap next to the center of \(U\).

Let \(H\) be the low cutoff of the edge \(U\to W\), a subset of \(U\), and \(H^*\) its extension from Lemma 2.1, a downset in the old frame and therefore an upset in the current one. Define
\[
G=D_{a_-}\cap(J\setminus\widehat P_a)\cap(J\setminus\widehat P_{v_-})\cap H^* .
\]

**Lemma 3.2.** In the current frame, \(G\) is an upset, \(X=W\setminus D_a\subseteq G\), and no job of \(G\) is scheduled at or before \(a\).

*Proof.* The four factors are upsets in the current frame: \(D_{a_-}\) is a cone, the complement of a weak predecessor cone is an upset, and \(H^*\) is one. So \(G\) is an upset.

Let \(x\in X\). At the edge \(U\to W\), if \(x\) had been high, Lemma 4.2 of the fourth lesson would put it in the old predecessor cone of the edge's right endpoint, which is the current \(a\); in the current frame that cone is \(D_a\), contradicting \(x\in X\). So \(x\in H\). Every edge cutoff lies in the old \(P\)-cone of the old right boundary of \(U\) (Lemma 3.1 of the fourth lesson), which is the current \(D_{a_-}\); so \(x\in D_{a_-}\). The job \(x\) is scheduled strictly after \(a\), hence strictly after \(v_-\), and by Lemma 1.1 of the second lesson it lies in neither \(\widehat P_a\) nor \(\widehat P_{v_-}\). Finally \(x\in W\subseteq U\) and \(H^*\cap U=H\), so \(x\in H^*\). Thus \(x\in G\).

Now let \(z\in G\) be scheduled at or before \(a\). Since \(z\in D_{a_-}\), it is scheduled strictly after \(a_-\), and it is strictly before \(b_-\) because \(a<b\leq b_-\). So \(z\in U\), and only now may we use \(H^*\cap U=H\): \(z\in H\). The edge cutoff \(H\) is contained in the center cutoff of its side of \(U\), and two separators of the old side apply.

- If \(z\) is scheduled at or before \(v_-\) in the current frame, it is at or after \(v_-\) in the old frame. If it is in \(v_-\), then \(z\in\widehat P_{v_-}\). Otherwise it is a low job after the old center, which separates the center cutoff, so it lies in the old \(D_{v_-}\), the current \(P_{v_-}\).
- If \(z\) is strictly after \(v_-\) and at or before \(a\), then in the old frame it lies on the old side, at or after the edge's right endpoint \(a\). That endpoint separates \(H\) on the side (Lemma 4.1 of the fourth lesson), so \(z\) is in the slot \(a\) or in the old \(D_a\), the current \(P_a\). Either way \(z\in\widehat P_a\).

Both contradict \(z\in G\).

These separator facts were established when the sides of \(U\) were normalized. Since then, every change of the schedule in this branch of the hierarchy has been inside \(W\): the choice of the center of \(W\) and the normalization of its sides. So the jobs at or before \(a\), the triples \(a\), \(v_-\), \(a_-\), and the fixed sets \(H\) and \(H^*\) are as they were, and the separator facts still hold in the current schedule. \(\square\)

So \(G\) has the three properties required in the fifth lesson, and the switch pair \((G\cap\{\lambda\geq h\},D_a)\) is defined.

## 4. The size of the entries

**Lemma 4.1.** Every entry of every list is described by a formula with at most \(25\) leaves, in particular fewer than \(40\).

*Proof.* The root entry, the injections and the second entries of switch pairs have at most three leaves including a rank suffix (Lemma 3.1 of the fifth lesson). The upset \(G\) has \(3+21=24\) leaves by Lemma 2.1, and the first entry of a switch pair adds one rank suffix. Later carries intersect an entry only with further rank suffixes of the same frame, which combine with the existing one into a single threshold. A new run discards the old list. \(\square\)

## 5. The order of the construction

The construction is an induction from the root downwards. When a child of \(W\) is formed, the data of \(W\) and of its ancestors exist. A same update uses only the list of \(W\). A switched update uses the edge \(U\to W\): its low set, the carry formed at it or the data of the switched side that produced it, and, through Lemma 1.1, the switch pair of the run of \(U\); all of these were constructed earlier. Lemma 3.2 gives the properties of \(G\), Lemma 2.1 of the fifth lesson the child's qualifiers and (I1), Lemma 3.2 of the fifth lesson the length of its list, and Lemma 4.1 the size of its entries. The length bound uses upward closure and the qualifier identity, not the size bound, and no step uses a statement about a deeper node. The remaining invariants (I2) and (I3) are proved in the next lesson.

## 6. Exercises

**6.1.** Explain why, without Lemma 1.1, the formula for \(H^*\) could grow with the number of direction changes along a branch of the hierarchy.

**6.2.** In Lemma 3.2, why is the factor \(D_{a_-}\) needed? Describe what could go wrong without it.

**6.3.** In Lemma 2.1, verify \(H^*\cap U=H\) for an edge on a switched side.

**6.4.** In Lemma 3.2, which case of the second part of the proof is empty when \(a=v_-\)?

**6.5.** Show that the second entry \(D_{a_0}\) of a switch pair is never trimmed by a carry while the first entry is present, by computing what \(\operatorname{carry}_{d,r}\) does for \(d=1\) and for \(d=2\).

## 7. Solutions

**6.1.** The first entry of a switch pair contains \(H^*\) for the edge above, and that \(H^*\) may contain the first entry of the previous run's switch pair, which contains the \(H^*\) of an earlier edge, and so on. Each direction change would add a layer. Lemma 1.1 replaces the old first entry by a two-leaf formula that agrees with it on the relevant node, so \(H^*\) never contains an earlier switch entry.

**6.2.** The set \(H^*\) agrees with \(H\) only on \(U\). Outside \(U\) it may contain jobs scheduled at or before \(a\), for instance jobs before \(a_-\) about which nothing is known. The factor \(D_{a_-}\) excludes everything at or before \(a_-\), so that a job of \(G\) at or before \(a\) is first located inside \(U\), where \(H^*\) is known to equal \(H\).

**6.3.** On a switched side of \(U\) the cutoffs are prefixes of \(U\setminus D_{a_U}\) in rank order. If \(r\) is the largest rank in \(H\), the jobs of \(U\setminus D_{a_U}\) with rank at most \(r\) are exactly those promoted so far, which is \(H\); and \(U\cap(J\setminus D_{a_U})\cap\{\lambda\leq r\}\) is that set.

**6.4.** The case of a job strictly after \(v_-\) and at or before \(a\): there is no such time when \(a=v_-\).

**6.5.** With \(d=1\), the carry is \((K_1\cap\{\lambda\geq r\},K_2,\ldots)\), so the second entry is kept unchanged. With \(d=2\), the first entry is discarded. So the second entry can be trimmed only by a carry with \(d=2\), after which the first entry is gone.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
