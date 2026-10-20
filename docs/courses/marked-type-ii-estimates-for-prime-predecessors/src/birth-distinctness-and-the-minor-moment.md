# Birth distinctness and the minor moment

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The operator identity of [*Lifespans and the memory space*](lifespans-and-the-memory-space.md) holds for histories in which all prime labels are born with distinct values, while the norm bounds of the last three lessons hold for the operators without that restriction. This lesson connects the two. The indicator of distinct births is expanded exactly as an alternating sum over systems of equality constraints between birth values, graded by their *rank*, the number of independent equalities. A system of high rank forces many births to take prescribed values, each costing a factor at most \(e^{-L^{0.1}}\), and this beats the absolute size of the history sum. A system of low rank is written by circle orthogonality as an average of phases attached to the births; the phases modify at most twice as many steps as the rank, and every other step keeps its contraction \(L^{-G}\). This proves the bound for the moment required in [*From the moment to the pairing*](from-the-moment-to-the-pairing.md). The lesson ends by removing the good-state projections and assembling the minor estimate of [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md).

**Prerequisites.** [*Lifespans and the memory space*](lifespans-and-the-memory-space.md), Theorem 4.1; [*Truncation, adjoints and absolute bounds*](truncation-adjoints-and-absolute-bounds.md), Lemmas 1.1, 2.1, 3.1 and 4.1; [*Dirty edges*](dirty-edges.md), Theorem 4.1; [*Independent residue lines*](independent-residue-lines.md), Theorem 4.1; [*Physical states and good positions*](physical-states-and-good-positions.md), Lemma 3.2 and Corollary 5.2; [*From the moment to the pairing*](from-the-moment-to-the-pairing.md), Proposition 3.1.

Throughout, the archimedean root is fixed until Section 3, and \(\Delta=\max_{i,p}\nu_i(p)\le4e^{-L^{0.1}}\) (Lemma 2.1 of Lesson 12).

## 1. Birth addresses and the cycle identity

**Addresses.** A **birth address** is one of the following positions in a history of (4.1) of Lesson 12, with operators truncated by \(\Pi_B\): one of the \(KM\) slots of the initial lists; one of the \(K\) last slots of the target of an edge (before the final reordering of that edge); or one of the \(B\) ordered places of the new batch of a ghost operation in one group. Since \(\Pi_B\) bounds every batch by \(B\), these cover all births. An address is **performed** in a history if a birth happens there: an initial slot always, an edge slot if it is filled by a fresh prime (not by a promotion), and a batch place if the batch is at least that long. The number of addresses is

\[
\begin{gathered}
Q_b=KM+KN+K(N+1)B\\
\le L^{3}\quad(1.1)
\end{gathered}
\]

for large \(x\). Order the addresses chronologically, with a fixed order inside each operation.

**Lemma 1.1 (the cycle identity).** For a finite set \(\mathcal B\) of addresses, a set of performed addresses and an assignment of prime values to them,

\[
\begin{aligned}
&\mathbf 1\{\text{performed values distinct}\}\\
&\quad=\sum_{\mathcal C}\prod_{C\in\mathcal C}(-1)^{|C|-1}(|C|-1)!\\
&\qquad\times\mathbf 1_{E_C},\quad(1.2)
\end{aligned}
\]

where \(\mathcal C\) runs over the collections of pairwise disjoint subsets of \(\mathcal B\) with at least two elements each, and \(E_C\) is the event that every address of \(C\) is performed and all have the same value.

**Proof.** Consider the permutations \(\pi\) of \(\mathcal B\) that fix every unperformed address and preserve the values. Their signs add up to \(\prod\) over the classes of equal value of \(\sum_{\pi\in\mathrm{Sym}(\text{class})}\operatorname{sgn}\pi\), which is \(1\) if every class is a singleton and \(0\) otherwise. On the other hand, group the permutations by the supports \(\mathcal C\) of their nontrivial cycles: a cycle on \(C\) has sign \((-1)^{|C|-1}\), there are \((|C|-1)!\) cyclic orders on \(C\), and such a permutation is admissible exactly when all the events \(E_C\) hold. \(\square\)

The **rank** of \(\mathcal C\) is \(r(\mathcal C)=\sum_{C\in\mathcal C}(|C|-1)\). A collection of rank \(r\) involves at most \(2r\) addresses, and the sum of the coefficients \(\prod(|C|-1)!\) over all collections of rank \(r\) is the number of permutations of \(\mathcal B\) that are products of \(r\) and no fewer transpositions; since an ordered list of \(r\) transpositions determines such a permutation,

\[
\begin{gathered}
\sum_{r(\mathcal C)=r}\prod_{C\in\mathcal C}(|C|-1)!\le Q_b^{2r}.\quad(1.3)
\end{gathered}
\]

## 2. Bounds by rank

Inserting (1.2) into the truncated history sum with globally distinct births writes it as \(\sum_{\mathcal C}c_{\mathcal C}\Sigma(\mathcal C)\), where \(c_{\mathcal C}=\prod(-1)^{|C|-1}(|C|-1)!\) and \(\Sigma(\mathcal C)\) is the history sum of \(\langle\mathbf b,\mathcal G_0\mathcal E_0\cdots\mathcal E_{N-1}\mathcal G_N\mathbf b\rangle\) on \(\mathscr H_B\) with the indicators \(\mathbf 1_{E_C}\) inserted and *no other distinctness condition*.

**Lemma 2.1 (absolute bound).** There is \(C_1=C_1(K,A_0)\) such that for every collection of rank \(r\),

\[
\begin{gathered}
\sum_{\text{histories}}|\text{weight}|\prod_{C\in\mathcal C}\mathbf 1_{E_C}\\
\le L^{C_1(N+1)}(8\Delta)^r .\quad(2.1)
\end{gathered}
\]

**Proof.** In each block \(C\) call its earliest address the pivot. On \(E_C\), every other address of \(C\) is performed with the value of the pivot, which is already determined when that address is reached. Drop all other requirements of \(E_C\), and drop the requirement that the history ends at \(\mathbf b\), using \(\mathbf b\le h=8^{k_{\rm tot}}\) at the end and \(h=1\) at the start. Then the absolute sum is at most \(\int\mathbf b\,d\mu\) (with the prescribed initial values) times the product over the operations of their weighted row sums with the prescribed values. A prescribed fresh value has measure at most \(\Delta\) instead of a total mass \(s_i\le2\). For an edge with \(s\) prescribed values the crude bound with fixed values (Lemma 4.1 of Lesson 13) gives \(L^{C_e}\Delta^s\). For a ghost operation with \(s\) prescribed batch places, the creation part of the row sum becomes, with \(c=v_0\eta_jV_i/\rho\le8\),

\[
\begin{gathered}
\sum_{l\ge s}\frac{c^l\Delta^ss_i^{\,l-s}}{l!}\le(c\Delta)^s\sum_{m\ge0}\frac{(cs_i)^m}{m!}\\
\le(8\Delta)^se^{9},
\end{gathered}
\]

and deletions and survivals contribute at most \(1\) as in Lemma 3.1 of Lesson 13. Each prescribed initial slot contributes \(\Delta\). The number of prescribed values is \(\sum_C(|C|-1)=r\). Multiplying over the \(N\) edges and \(N+1\) ghost operations gives (2.1) with \(L^{C_1}\ge e^{9K}L^{C_e}\). \(\square\)

**Lemma 2.2 (high ranks).** Let \(r_0=\lceil C'N\log L/L^{0.1}\rceil\) with \(C'=2(C_1+E_0+4)\). For large \(x\),

\[
\begin{gathered}
\sum_{r(\mathcal C)\ge r_0}|c_{\mathcal C}\,\Sigma(\mathcal C)|\le L^{-(E_0+2)N}.\quad(2.2)
\end{gathered}
\]

**Proof.** By (1.3) and (2.1), the left side is at most \(L^{C_1(N+1)}\sum_{r\ge r_0}(8Q_b^2\Delta)^r\). Since \(8Q_b^2\Delta\le32L^6e^{-L^{0.1}}\le e^{-L^{0.1}/2}\), the series is at most \(2e^{-r_0L^{0.1}/2}\le2L^{-C'N/2}=2L^{-(C_1+E_0+4)N}\). \(\square\)

For a block \(C=\{a_0,a_1,\dots,a_s\}\) with pivot \(a_0\), circle orthogonality gives

\[
\begin{gathered}
\mathbf 1_{E_C}=\Bigl(\prod_{a\in C}\mathbf 1_{a\ \text{performed}}\Bigr)\\
\times\int_{\mathbb T^s}\prod_{h=1}^se\bigl(\theta_h(p_{a_h}-p_{a_0})\bigr)\,d\theta,\\
(2.3)
\end{gathered}
\]

where \(p_a\) is the value born at \(a\). For fixed \(\theta\), each factor is attached to the operation in which its birth happens: the address \(a_h\) receives \(\mathbf 1_{\rm performed}\,e(\theta_hp_{a_h})\), and the pivot receives \(\mathbf 1_{\rm performed}\,e(-p_{a_0}\sum_h\theta_h)\). These are **local multipliers** of modulus at most \(1\).

**Lemma 2.3 (modified operations).** For fixed \(\theta\), an operation carrying local multipliers has norm at most \(e^{9K}\) if it is a ghost operation and at most \(L^{C_e}\) if it is an edge; the initial vector multiplied by its local multipliers has norm \(\|\mathbf b\|\).

**Proof.** The multiplier at an edge address depends only on whether that slot is filled freshly and on the fresh value; it does not depend on which old particle is promoted. It therefore commutes with reordering the old particles, the modified edge maps symmetric functions of the memory to symmetric functions, and its weighted row and column sums are dominated by those of Lemma 4.1 of Lesson 13. The multiplier at a batch place depends on the coordinate of the ordered batch at that place. The rest of the history, as a function of the state after the ghost operation, is symmetric in the memory particles, because all later operations, with their own multipliers, preserve symmetric functions; working backwards from the end of the history, this holds at every step. Hence averaging the multiplier over the reorderings of the new batch does not change the history sum. The averaged multiplier has modulus at most \(1\) and is symmetric, so the modified ghost operation acts on symmetric functions, keeps its factor \(1/l!\), and is dominated by the absolute sums of Lemma 3.1 of Lesson 13. The initial multipliers are functions of the initial lists of modulus at most \(1\). \(\square\)

**Lemma 2.4 (low ranks).** Let \(G=E_0+4\) and suppose \(\|\mathcal E_j\|\le L^{-G}\) on \(\mathscr H_B\) for every \(j\). For large \(x\),

\[
\begin{gathered}
\sum_{r(\mathcal C)<r_0}|c_{\mathcal C}\,\Sigma(\mathcal C)|\le L^{-(E_0+3)N}.\quad(2.4)
\end{gathered}
\]

**Proof.** Fix \(\mathcal C\) of rank \(r<r_0\) and \(\theta\). The multipliers modify at most \(2r\) operations. Bound the matrix element by the product of norms: modified edges by \(L^{C_e}\), all ghost operations by \(e^{9K}\), unmodified edges by \(L^{-G}\), and the two end vectors by \(\|\mathbf b\|\le2\). This gives \(4e^{9K(N+1)}L^{-G(N-2r)}L^{2rC_e}\), and integrating over \(\theta\in\mathbb T^r\) does not increase it. By (1.3),

\[
\begin{aligned}
&\sum_{r<r_0}Q_b^{2r}\cdot4e^{9K(N+1)}L^{-G(N-2r)+2rC_e}\\
&\quad\le4e^{9K(N+1)}L^{-GN}\bigl(L^{6+2G+2C_e}\bigr)^{r_0}\\
&\qquad\times r_0 .
\end{aligned}
\]

Here \(e^{9K(N+1)}=L^{9K(N+1)/\log L}\) and \((L^{6+2G+2C_e})^{r_0}r_0\) are \(L^{o(N)}\), because \(r_0=O(N\log L/L^{0.1})\). So the sum is \(L^{-GN+o(N)}\le L^{-(E_0+3)N}\) for large \(x\). \(\square\)

The constant \(C_e(K,A_0)\), which contains the factor \(B^K\), is paid on only \(2r=o(N)\) steps; this is why it does not affect the choice of \(K\).

## 3. The minor moment

**Theorem 3.1 (the minor moment).** Fix \(E_0>0\). If \(A_0\ge E_0+7\) and \(K\ge200(E_0+7)\), then for large \(x\), every pad dyad \(d_0\) and every \(Y\) in (2.1) of Lesson 7,

\[
\begin{gathered}
\mathfrak m=\sum_P\langle\mathbf u_P,(\mathcal A\mathcal A^*)^R\mathbf u_P\rangle\\
\le UV\,L^{-E_0N}.\quad(3.1)
\end{gathered}
\]

**Proof.** Put \(G=E_0+4\). Then \(A_0\ge G+3\) and \(0.005K\ge E_0+7>G+2\), so Theorem 4.1 of Lesson 15 gives \(\|\mathcal E_j\|\le L^{-G}\) on \(\mathscr H_B\). By Theorem 4.1 of Lesson 11, \(\mathfrak m/UV\) equals \(\zeta(2)^{-1}\int_{Q_0}\mathfrak m(\mathbf a)\,d\mathbf a\) up to \(O(L^{-AN})\). By Theorem 4.1 of Lesson 12, \(\mathfrak m(\mathbf a)\) is \(\prod_pb'_p\le1\) times the history sum with globally distinct births. By Lemma 1.1 of Lesson 13, inserting \(\Pi_B\) costs \(O(L^{-AN})\). By (1.2) and Lemmas 2.2 and 2.4, the truncated sum is at most \(L^{-(E_0+2)N}+L^{-(E_0+3)N}\) in modulus. Since \(Q_0\) has volume \(15\) and \(\mathfrak m\ge0\), (3.1) follows for large \(x\). \(\square\)

## 4. Removing goodness and the minor estimate

**Lemma 4.1 (good-state projections).** For every fixed \(A\), \(|\langle f,\mathcal Tg\rangle-\langle f,\mathcal Ag\rangle|\ll UV\,L^{-A}\).

**Proof.** Since \(\mathcal Sf=f\), \(\mathcal Sg=g\), and \(\mathcal G\) commutes with \(\mathcal S\),

\[
\begin{aligned}
&\langle f,\mathcal Tg\rangle-\langle f,\mathcal Ag\rangle\\
&\quad=\langle(1-\mathcal G)f,\mathcal Tg\rangle\\
&\qquad+\langle\mathcal Gf,\mathcal T(1-\mathcal G)g\rangle .
\end{aligned}
\]

Consider the first term; the second is the same with the reversed edge and the root at the target. Bound \(|f|,|g|\le L^{2C}\). The remaining absolute sum over pairs of states joined by an edge, with a bad source, is a path sum with one edge, rooted at the source position. By Theorem 4.1 of Lesson 11, in the variant with absolute weights and the indicator of a failing test, it equals \(UV/\zeta(2)\) times the integral of its model value, up to \(O(UVL^{-A})\). In the model, a prime that is in one of the two lists must have its random line equal to the line of its visit, with probability \(1/(p+1)\); by the ban the two lists contain \(M+1\) distinct primes in each group, with measure \(\prod_iV_i^{-(M+1)}\), so the sum over the lists of these probabilities is at most

\[
\begin{gathered}
\prod_{i=1}^K\Bigl(\sum_{p\in\mathcal P_i}\frac1{V_i(p+1)}\Bigr)^{M+1}\le1,
\end{gathered}
\]

and the damping is at most \(1\). For fixed lists there are at most \(17\) raw targets, and \(O(Y)\) comparison targets with multiplier \(O(L^{3A_0}/Y)\). The source is the root, so its ratio is \(a_3\), and by Lemma 3.2 of Lesson 8 the set of \(a_3\) at which it fails a test has measure at most \(e^{-cL^{0.1}}\), for every fixed lists and every \(a_1,a_2\). Hence the model integral is \(O(L^{3A_0}e^{-cL^{0.1}})\), and the first term is \(O(UVL^{4C+3A_0}e^{-cL^{0.1}}+UVL^{-A})\). \(\square\)

**Theorem 4.2 (the minor estimate).** Let \(D_1>0\), \(E_0=D_1+4C+2\), \(A_0\ge E_0+7\) and \(K\ge200(E_0+7)\). Then, for large \(x\) and every \(Y\) in (2.1) of Lesson 7,

\[
\begin{gathered}
|\mathcal Q_Y^{\rm min}|\ll XY\,L^{-D_1}.\quad(4.1)
\end{gathered}
\]

**Proof.** By Corollary 5.2 of Lesson 8, \(\mathcal Q_Y^{\rm min}=\sum_{d_0}\langle f,\mathcal Tg\rangle/d_0+O(XYL^{-D_1})\), the sum over at most \(3KL^{0.21}\) pad dyads. For each dyad, Lemma 4.1, Proposition 3.1 of Lesson 9 and Theorem 3.1 give

\[
\begin{gathered}
|\langle f,\mathcal Tg\rangle|\le C_{\rm abs}UV\,L^{4C-E_0}\\
+O(UVL^{-A}),
\end{gathered}
\]

and \(UV=d_0YX\). Dividing by \(d_0\) and summing over the dyads gives \(O(XYL^{0.21+4C-E_0})=O(XYL^{-D_1})\). \(\square\)

## 5. Exercises

**16.1.** Verify (1.2) for three addresses, all performed, with values \((5,5,7)\) and with values \((5,5,5)\).

**16.2.** Show that a collection \(\mathcal C\) of rank \(r\) involves at most \(2r\) addresses, with equality exactly when all blocks have two elements.

**16.3.** Count the permutations of \(\{1,2,3\}\) of rank \(1\) and of rank \(2\), and compare with the bound \(Q_b^{2r}\) with \(Q_b=3\).

**16.4.** Show that the sum over \(r\ge r_0\) in Lemma 2.2 is dominated by its first term, and explain why a union bound over a single repeated prime would not suffice.

**16.5.** In the proof of Lemma 4.1, explain why the bound of the model sum over the lists by \(1\) does not lose any factor depending on \(K\) or \(M\).

## 6. Solutions

**16.1.** The collections are \(\varnothing\), the three pairs, and the triple. With values \((5,5,7)\), only \(\varnothing\) (coefficient \(1\)) and the pair \(\{1,2\}\) (coefficient \(-1\)) have their events satisfied, giving \(0\): the values are not distinct. With \((5,5,5)\): \(1-3+2\cdot1=0\), since the triple has coefficient \((-1)^2\cdot2!=2\).

**16.2.** A block \(C\) has \(|C|\le2(|C|-1)\) elements, with equality iff \(|C|=2\). Summing over the blocks gives the claim.

**16.3.** Rank \(1\): the three transpositions. Rank \(2\): the two \(3\)-cycles. The bound gives \(9\) and \(81\).

**16.4.** The ratio of consecutive terms is \(8Q_b^2\Delta\le e^{-L^{0.1}/2}<\frac12\). A union bound over one repeated value gains a single factor \(\Delta\), while the absolute size of the history sum is \(L^{C_1(N+1)}\), far larger than \(\Delta^{-1}\); one needs about \(N\log L/L^{0.1}\) independent coincidences before the atoms win.

**16.5.** Each prime of the union of the two lists contributes \(1/(V_i(p+1))\), and \(\sum_{p\in\mathcal P_i}1/(V_i(p+1))\le\sum_p1/(V_ip)=1\). So each of the \(K(M+1)\) factors is at most \(1\); there is no factorial or combinatorial loss, because the lists are ordered and their measure is the product of the harmonic weights.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Sections 4.8 and 4.9. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
