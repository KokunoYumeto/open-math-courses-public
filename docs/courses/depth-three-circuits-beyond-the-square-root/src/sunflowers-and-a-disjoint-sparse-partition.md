# Sunflowers and a disjoint sparse partition

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A CNF whose clauses have width at most \(b\) can still have about \(m^b\) clauses on \(m\) variables. This lesson proves that every such CNF is a sum of at most \(2^{\eta m}\) CNFs of the same width with *disjoint* satisfying sets, each with only a constant times \(m\) clauses. The constant \(\eta>0\) can be taken as small as one likes. In the course [Depth-three circuits and the square-root barrier](depth-three-circuits-and-the-square-root-barrier.md) this is the second structural step: there are few CNFs with linearly many clauses, so a probabilistic argument can control all of them at once, and disjointness lets the bounds for the pieces be added.

The method is the sparsification of Impagliazzo, Paturi and Zane, in the disjoint form described by Dell, Husfeldt, Marx, Taslaman and Wahlén. The lesson is self-contained and does not use the two previous lessons.

## 1. The statement

**Lemma 1.1 (sparse partition).** For every integer \(b\geq1\) and real \(\eta>0\) there is a positive integer \(M=M(b,\eta)\) with the following property. Every CNF \(H\) of width at most \(b\) on \(m\geq1\) variables can be written pointwise as
\[
H=\sum_{a=1}^{q}H_a,\qquad q\leq2^{\eta m},
\]
where each \(H_a\) is a CNF of width at most \(b\) with at most \(Mm\) clauses, and the satisfying sets of the \(H_a\) are pairwise disjoint. For \(H=0\) the empty sum is allowed.

Here a CNF is identified with its \(0/1\) indicator, as in the first lesson, and the sum is a sum of indicators.

## 2. Sunflowers

A *sunflower* with \(r\) members is a collection of \(r\) distinct sets whose pairwise intersections all equal one set \(C\), its *core*. The sets with the core removed are its *petals*; they are pairwise disjoint.

**Lemma 2.1 (Erdős and Rado).** Let \(s\geq0\) and \(r\geq2\) be integers. A family of more than \(s!\,(r-1)^s\) distinct sets of size \(s\) contains a sunflower with \(r\) members.

*Proof.* Induction on \(s\). For \(s=0\) there is only one set of size \(0\), so no family has more than \(1\) member and there is nothing to prove. Let \(s\geq1\). Take a maximal subfamily of pairwise disjoint members. If it has at least \(r\) members, \(r\) of them form a sunflower with empty core. Otherwise it has at most \(r-1\) members, and their union \(U\) has at most \(s(r-1)\) elements. By maximality every member of the family meets \(U\). So some element \(x\in U\) lies in more than
\[
\frac{s!\,(r-1)^s}{s(r-1)}=(s-1)!\,(r-1)^{s-1}
\]
members. Remove \(x\) from each of these members: the results are distinct sets of size \(s-1\), so by induction \(r\) of them form a sunflower. Putting \(x\) back gives a sunflower in the family. \(\square\)

## 3. Branching on a sunflower

From now on a clause is a set of literals, over \(m\) variables, so there are \(2m\) literals. Normalize the given CNF: remove clauses that contain a variable together with its negation, remove repetitions, and remove every clause that contains another clause as a proper subset (it is implied by the smaller one). If the empty clause is left, \(H=0\) and the empty sum serves. Otherwise the clauses are nonempty and form an *antichain*: none contains another. The empty antichain is allowed; it is the constant true function.

Fix integers \(r_2,\ldots,r_b\geq2\); their values are chosen in Section 6. A sunflower is *eligible at size \(i\)* if it consists of \(r_i\) clauses of size \(i\) and its core is nonempty. Sets here are sets of literals: two disjoint petals may contain opposite literals of the same variable.

A *state* consists of an antichain of clauses, the *active* clauses, and a conjunction of unit clauses, the *side condition*, which starts empty. The side condition is never used to choose sunflowers or to delete active clauses. As long as an eligible sunflower exists among the active clauses, choose one of the *smallest possible size* \(i\), by some fixed rule, and write its members as
\[
C\cup P_1,\ \ldots,\ C\cup P_{r_i}.
\]
The core \(C\) is nonempty by eligibility. The petals are pairwise disjoint and of equal size; they are nonempty, because an empty petal would make one member equal to \(C\), and then all members, having the same size, would equal \(C\). The state has two successors.

- **Branch 0.** Insert the clause \(C\) among the active clauses.
- **Branch 1.** Insert the clauses \(P_1,\ldots,P_{r_i}\) among the active clauses, and add to the side condition that every literal of \(C\) is false.

In both branches, afterwards delete every active clause that properly contains an inserted clause. All inserted clauses have size less than \(i\), so the width never grows.

**Lemma 3.1.** (a) No active clause is contained in or equal to an inserted clause; so every inserted clause is new, stays active after the step, and the new active family is an antichain. (b) Let \(F\) be the conjunction of the active clauses before the step and \(F_0,F_1\) the conjunctions after branch \(0\) and branch \(1\). Then
\[
F=F_0+\mathbf 1[C\text{ is false}]\,F_1,
\]
and the two terms on the right have disjoint supports.

*Proof.* (a) An inserted clause \(D\) is a proper subset of an active clause \(A\): the core is a proper subset of \(C\cup P_1\), and \(P_j\) is a proper subset of \(C\cup P_j\) because \(C\neq\varnothing\). An active clause \(B\subseteq D\) would be a proper subset of \(A\), which the antichain property forbids. The petals inserted together are distinct sets of the same size, so none contains another. After the deletion no old clause contains an inserted one, so the family is an antichain.

(b) Deleting a clause that contains another clause of the family does not change the conjunction. So \(F_0=F\cdot\mathbf 1[C\text{ true}]\) and \(F_1=F\cdot\prod_j\mathbf 1[P_j\text{ true}]\). Where \(C\) is true, \(F_0=F\) and the second term vanishes. Where \(C\) is false, \(F_0=0\), and \(F=1\) forces every clause \(C\cup P_j\), hence every \(P_j\), to be true, so \(F=F_1\) there. \(\square\)

Multiply the identity by the side condition \(\Sigma\) of the state. The function of the state is \(\Sigma F\), and the functions of its two successors are \(\Sigma F_0\) and \(\Sigma\cdot\mathbf 1[C\text{ false}]\cdot F_1\). So the function of a state is the sum of the functions of its successors, with disjoint supports. The states form a binary tree. If the tree is finite, the function \(H\) of the root is the sum of the functions of the leaves, with pairwise disjoint supports. A leaf is a state with no eligible sunflower.

## 4. Occurrence bounds

Put \(e_1=1\) and, for \(2\leq i\leq b\),
\[
e_i=(i-1)!\,(r_i-1)^{i-1}.
\]

**Lemma 4.1.** If the active clauses of size \(i\) contain no eligible sunflower, every literal lies in at most \(e_i\) of them.

*Proof.* For \(i=1\) the clauses are distinct sets of size one. Let \(i\geq2\) and fix a literal. Remove it from the active clauses of size \(i\) that contain it. If there were more than \(e_i\) of them, Lemma 2.1 with \(s=i-1\) and \(r=r_i\) would give a sunflower among the resulting sets; putting the literal back gives \(r_i\) clauses of size \(i\) forming a sunflower whose core contains the literal, an eligible sunflower. \(\square\)

Call an active clause *added* if it was inserted in some step, as opposed to belonging to the original family.

**Lemma 4.2.** At every state, for every size \(u\) and every literal, at most \(e_u+1\) added active clauses of size \(u\) contain the literal.

*Proof.* At the root there are no added clauses. A step raises the count only if it inserts clauses of size \(u\). Such a step processes a sunflower of some size \(i>u\), and by the smallest-size rule there is then no eligible sunflower at size \(u\). By Lemma 4.1 the literal lies in at most \(e_u\) active clauses of size \(u\), added or not, before the insertion. The step inserts one core or pairwise disjoint petals, so it adds at most one clause containing the literal. Deletions only lower the count. \(\square\)

The original family need not satisfy any such bound; it may contain a literal in a huge number of clauses. The steps repair this gradually.

## 5. Insertion budgets and termination

Follow any finite path of steps from the root, and let \(N_u\) be the number of clauses of size \(u\) inserted along it, each petal counted separately.

**Lemma 5.1.** \(N_u\leq(e_u+1)\bigl(2m+\sum_{v<u}N_v\bigr)\).

*Proof.* Every inserted clause of size \(u\) is either still active at the end of the path or was deleted along it. *Survivors:* each is nonempty and so contains one of the \(2m\) literals, and by Lemma 4.2 each literal lies in at most \(e_u+1\) of them; there are at most \(2m(e_u+1)\). *Deleted:* an added clause of size \(u\) is deleted only because it properly contains a clause \(D\) inserted in that step, of some size \(v<u\); charge the deletion to one such \(D\). A clause \(D\) receives at most \(e_u+1\) charges: pick a literal of \(D\); every clause charged to \(D\) contains it, and by Lemma 4.2, just before \(D\) was inserted, at most \(e_u+1\) added active clauses of size \(u\) contained that literal. So there are at most \((e_u+1)\sum_{v<u}N_v\) deletions. \(\square\)

Define positive integers by \(D_1=4\) and, for \(2\leq i\leq b\),
\[
D_i=(e_i+1)\Bigl(2+\sum_{u<i}D_u\Bigr).
\]
The formula also gives \(D_1=(e_1+1)\cdot2=4\). By induction on \(u\), Lemma 5.1 yields
\[
N_u\leq D_um.
\]
These bounds hold along every finite path. Each step inserts at least one clause, of size less than \(b\). So a path has at most \(m\sum_{u<b}D_u\) steps, and the tree is finite.

For \(2\leq i\leq b\) put \(F_i=\sum_{u<i}D_u\). A step that processes size \(i\) inserts at least one clause of size less than \(i\), and on branch \(1\) it inserts exactly \(r_i\) of them. Along any path at most \(F_im\) clauses of size less than \(i\) are inserted in all. Hence, along any path, at most \(F_im\) steps process size \(i\), and at most \(F_im/r_i\) of them take branch \(1\).

## 6. Counting the leaves

**Lemma 6.1.** For an integer \(N\geq0\) and \(0<x\leq\frac12\), the number of binary strings of length \(N\) with at most \(Nx\) ones is at most \(2^{Nh(x)}\), where \(h(x)=-x\log_2x-(1-x)\log_2(1-x)\).

*Proof.* Give each position the value \(1\) with probability \(x\), independently. A string with \(j\leq Nx\) ones has probability
\[
\begin{aligned}
x^j(1-x)^{N-j}&=(1-x)^N\Bigl(\frac x{1-x}\Bigr)^{j}\\
&\geq(1-x)^N\Bigl(\frac x{1-x}\Bigr)^{Nx}\\
&=2^{-Nh(x)},
\end{aligned}
\]
because \(x/(1-x)\leq1\). The probabilities of these strings add up to at most \(1\). \(\square\)

For a leaf and each \(i=2,\ldots,b\), write down in order the branches (\(0\) or \(1\)) taken at the steps that processed size \(i\) on the way to the leaf, and pad with zeros to length \(F_im\). By Section 5 this string has at most \(F_im/r_i\) ones. The \(b-1\) strings determine the leaf. Indeed two different leaves are reached by paths that first differ at some step; up to that step the states agree, so the same sunflower is chosen, of the same size \(i\), at the same position of the string for \(i\), and the two strings differ there. By Lemma 6.1 with \(x=1/r_i\leq\frac12\),
\[
\#\{\text{leaves}\}\leq\prod_{i=2}^{b}2^{mF_ih(1/r_i)}.
\]
Now choose the thresholds. The number \(F_i\) depends only on \(r_2,\ldots,r_{i-1}\), because it involves only \(D_u\) and \(e_u\) with \(u<i\). Since \(h(1/r)\to0\) as \(r\to\infty\), we can choose \(r_2,r_3,\ldots,r_b\) one after another so that
\[
F_ih(1/r_i)\leq\frac\eta b\qquad(2\leq i\leq b).
\]
Then the number of leaves is at most \(2^{\eta m(b-1)/b}\leq2^{\eta m}\). An explicit choice is given in Exercise 8.4.

## 7. The leaves are sparse

At a leaf there is no eligible sunflower at any size. By Lemma 4.1 every literal lies in at most \(e_i\) active clauses of size \(i\); each such clause contains a literal, so there are at most \(2me_i\) of them. The side condition consists of at most \(2m\) different unit clauses. The function of the leaf is the conjunction of both: a CNF of width at most \(b\) with at most \(Mm\) clauses, where
\[
M=2+2\sum_{i=1}^{b}e_i.
\]
A leaf whose side condition is contradictory has the zero function and can be dropped.

**Proof of Lemma 1.1.** By Section 3 the function \(H\) is the sum of the functions of the leaves, with pairwise disjoint supports. By Section 6 there are at most \(2^{\eta m}\) leaves, and by the count above each is a CNF of width at most \(b\) with at most \(Mm\) clauses. All constants depend only on \(b\) and \(\eta\). For \(b=1\) there is no branching: the single leaf is the normalized CNF itself, with at most \(2m\leq4m\) unit clauses. \(\square\)

## 8. Exercises

**8.1.** Find a family of \((r-1)^s\) sets of size \(s\) that contains no sunflower with \(r\) members. So Lemma 2.1 is sharp up to the factor \(s!\).

**8.2.** Let \(H\) be the CNF with the three clauses \(\{x,y\},\{x,z\},\{x,w\}\) and take \(r_2=3\). Carry out the branching step and verify the identity of Lemma 3.1(b).

**8.3.** Why does the side condition have to be kept apart from the active clauses? What would go wrong in Lemma 5.1 if the unit clauses of the side condition were allowed to delete active clauses?

**8.4.** Show \(h(2^{-q})\leq(q+2)2^{-q}\) for integers \(q\geq1\), and conclude that \(r_i=2^{q_i}\) works in Section 6 when \(q_i\) is the least integer with \(F_i(q_i+2)2^{-q_i}\leq\eta/b\).

**8.5.** Compute \(e_i\), \(D_i\) and \(M\) for \(b=2\) in terms of \(r_2\).

**8.6.** Show that the pieces \(H_a\) need not be satisfiable by exhibiting a step in which branch \(1\) has an unsatisfiable active family.

## 9. Solutions

**8.1.** Take \(s\) pairwise disjoint sets \(A_1,\ldots,A_s\) of size \(r-1\) and all sets that contain exactly one element of each \(A_t\). Suppose \(r\) of them form a sunflower. In each \(A_t\) they use at most \(r-1\) different elements, so two members share their element of \(A_t\); this element lies in the core, hence in all members. So all members agree in every \(A_t\) and are equal, a contradiction.

**8.2.** The three clauses form a sunflower with core \(\{x\}\) and petals \(\{y\},\{z\},\{w\}\). Branch \(0\) inserts \(\{x\}\) and deletes the three clauses: \(F_0=x\). Branch \(1\) inserts \(\{y\},\{z\},\{w\}\), deletes the three clauses, and records that \(x\) is false: its function is \(\bar x\,yzw\). And \(H=x\vee(y\wedge z\wedge w)=x+\bar x\,yzw\).

**8.3.** Lemma 5.1 charges every deletion of an added clause to an inserted *active* clause, and Lemma 4.2 limits the charges received by each. A unit clause of the side condition is a statement that a literal is false, that is, the opposite literal as a clause; if it deleted active clauses containing that opposite literal, these deletions would have to be charged too, and the side condition would enter the occurrence counts. Keeping it apart keeps the accounting to active insertions only. The price is that leaves may carry redundant or contradictory conditions, which does no harm.

**8.4.** For \(0<x<1\) the function \(\varphi(x)=x+(1-x)\ln(1-x)\) has \(\varphi(0)=0\) and \(\varphi'(x)=-\ln(1-x)\geq0\), so \(-(1-x)\ln(1-x)\leq x\), that is, \(-(1-x)\log_2(1-x)\leq x\log_2e\). Hence \(h(x)\leq x(\log_2(1/x)+\log_2e)\), and with \(x=2^{-q}\) and \(\log_2e<2\) this is less than \((q+2)2^{-q}\). So \(F_ih(1/r_i)\leq F_i(q_i+2)2^{-q_i}\leq\eta/b\); such a \(q_i\) exists because \((q+2)2^{-q}\to0\).

**8.5.** \(e_1=1\), \(e_2=r_2-1\); \(D_1=4\), \(D_2=r_2(2+4)=6r_2\); \(M=2+2(1+r_2-1)=2+2r_2\). Also \(F_2=D_1=4\), so \(r_2\) must satisfy \(4h(1/r_2)\leq\eta/2\).

**8.6.** Take the clauses \(\{x,y\},\{x,\bar y\},\{x,z\}\) with \(r_2=3\). Branch \(1\) inserts the petals \(\{y\},\{\bar y\},\{z\}\), whose conjunction is unsatisfiable. The identity still holds: \(H=x\) and the second term is zero.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
- P. Erdős and R. Rado (1960, the sunflower lemma), R. Impagliazzo, R. Paturi and F. Zane (2001, sparsification), and H. Dell, T. Husfeldt, D. Marx, N. Taslaman and M. Wahlén (2014, the disjoint form) are named for credit; the lesson proves what it uses.
