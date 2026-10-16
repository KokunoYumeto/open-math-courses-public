# Finite Cayley formulas for prescribed profiles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson produces, for each prescribed band profile on the model space, an actual element of a matrix algebra over the group algebra of \(\Gamma\) that approximates it in the regular representation. The element is a finite word in *Cayley polynomials*: one polynomial for each incidence type, the sum of its weighted labels divided by \(q\). On a sheet, the part of such a polynomial along the sheet's own edges is the sampled weighted incidence, close to its mean by the simultaneous sampling; compressing to the disjoint domains loses little. What is left are the Cayley edges outside the domains, and they form a forest, so their contribution has norm at most a constant times \(\sqrt{|\mathcal S_{\rm wt}|}/q\), which the sharp alphabet bound makes small. This is where the margin \(\log|\mathcal S|<\log(q^2)\) carried through the whole construction is used [OpenAI-BCI, Section 8.3, Lemma 8.4].

- Cayley polynomials (Section 1).
- The residual forest (Section 2).
- Finite formulas for a profile family (Section 3).

The setting of [Carriers, trimming and constant extraction](carriers-trimming-and-constant-extraction.md) is in force: \(R(g)\), the sum \(\mathscr H_{\rm abs}\) of the sheets, the domains and the partial isometry \(U\), the carriers, the model space \(\mathscr K\) with \(\mathcal I\), the mean blocks \(V,W(f)\), the routes \(\mathcal R_k(f)\), the map \(\Psi_\nu\) and (3.2), (4.3) there. We use the matrix adjacency bound on a forest, Lemma 4.2 of [From the cover band to the Cayley projection](course:kadison-kaplansky-projections/from-the-cover-band-to-the-cayley-projection#4-an-element-of-the-group-algebra).

## 1. Cayley polynomials

By Proposition 1.1 of [Polynomial avoidance, norm tests and moments](polynomial-avoidance-norm-tests-and-moments.md), every positive old edge carries a refined label \(\sigma\) that determines its matrix weight \(W_\sigma\), from one finite set; the reverse edge carries \(W_\sigma^*\). The weights already contain the bounded factors \(q/q_{\tau,ik}\), and all types use the common normalizer \(q^{-1}\). For a type \(\tau\), let \(\mathcal S_\tau\) be its finite set of refined positive labels and define
\[
\begin{gathered}
C_\tau=q^{-1}\sum_{\sigma\in\mathcal S_\tau}W_\sigma\,R(\sigma)\\
\in M_m\bigl(R(\mathbb C[\Gamma])\bigr) .
\end{gathered}\tag{1.1}
\]
Private letters have coefficient zero.

**Lemma 1.1** (the sheet part of a Cayley polynomial). On a sheet \(Q\), the sum of the terms of \(C_\tau\) over the source edges of type \(\tau\) of \(Q\) is, in the sheet coordinates \(\ell^2(Q)=\ell^2(V(X))\otimes\ell^2(\mathsf H)\), the normalized weighted block \(\mathcal V_\tau\) of the sampled voltages and weights, from the \(\mathscr B\)-vertices to the \(\mathscr A\)-vertices, and its adjoint in the other direction.

*Proof.* By (1.1) of the previous lesson, \(R(\sigma)\) maps the coordinate \(ft_w\) of the \(\mathscr B\)-endpoint of an edge with label \(\sigma\) to \(fh_e^{-1}t_v\), which is \(\rho(h_e)\) in the deck coordinate, and the weight is \(W_\sigma\); summing over the source edges gives \(q^{-1}\sum_eE_{v_ew_e}\otimes W_e\otimes\rho(h_e)=\mathcal V_\tau\). \(\square\)

## 2. The residual forest

The polynomial \(C_\tau\), as an operator on \(\ell^2(\Gamma)\otimes\mathbb C^m\), has matrix entries along the formal Cayley edges \((g,\sigma)\), \(\sigma\in\mathcal S_\tau\). Split these edges into the *internal source edges*, edges of a sheet with both ends in its domain, and the rest. By Proposition 2.1 of [Cycle coordinates and disjoint domains](cycle-coordinates-and-disjoint-domains.md), every internal edge has a unique sheet, and the remaining edges form a forest. The remaining edges include Cayley chords that are not source edges and edges with unused weight labels, even with both ends in one domain: an edge leaves the remainder only when it is an edge of its own sheet inside that sheet's domain.

**Lemma 2.1** (the residual forest). Let \(\mathcal S_{\rm wt}\) be the finite weighted old alphabet. The part of \(C_\tau\) along the remaining edges has norm at most
\[
C\,\frac{\sqrt{|\mathcal S_{\rm wt}|}}q ,\tag{2.1}
\]
with \(C\) fixed before \(s\). By Proposition 1.1(3) of the lesson on polynomial avoidance,
\[
\begin{aligned}
&\frac{\sqrt{|\mathcal S_{\rm wt}|}}q\\
&\quad\le2^{-0.000025s+O(\log s)+O(1)}\\
&\quad\longrightarrow0 .
\end{aligned}\tag{2.2}
\]

*Proof.* A vertex of the Cayley graph has at most \(2|\mathcal S_{\rm wt}|\) edges with old weighted labels, and each normalized weight has norm at most \(C/q\). For the self-adjoint double of the directed block, the entries sit on the edges of the bipartite double cover of the forest, which is again a forest. Lemma 4.2 of [From the cover band to the Cayley projection](course:kadison-kaplansky-projections/from-the-cover-band-to-the-cayley-projection#4-an-element-of-the-group-algebra) bounds a self-adjoint operator supported on the edges of a forest of degree at most \(m_1\), with entries of norm at most \(w_1\), by \(2w_1\sqrt{m_1}\); here \(w_1\le C/q\) and \(m_1\le2|\mathcal S_{\rm wt}|\). \(\square\)

## 3. Finite formulas for a profile family

**Lemma 3.1** (finite formulas for a prescribed profile family; [OpenAI-BCI, Lemma 8.4]). Fix a finite collection of band profiles \(f=(f_{ik})_{|i-k|\le1}\) of the fixed families, a matrix size, and \(\eta>0\). The construction parameters can be chosen so that for every such profile there is a finite matrix element \(b_f\) over the right regular group algebra of \(\Gamma\) with
\[
\begin{gathered}
\bigl\|b_f-UD\mathcal If^{\rm mod}\mathcal I^*DU^*\bigr\|\\
<\eta ,
\end{gathered}\tag{3.1}
\]
simultaneously over all heights and sheets. Profiles may vanish on a prescribed parity pattern, on all positive heights, or at the initial height, with no height-dependent enlargement of the alphabet.

*Proof.* First choose \(k\) so that the term \(C_f\rho^{2k}\) of (4.3) of the previous lesson is small. Designate the finitely many cutoff and symbol blocks of \(V\) and \(W(f)\) as incidence types of Proposition 1.1 of the lesson on polynomial avoidance, which supplies the finite weight set.

*One factor.* For a type, the physical polynomial \(C_\tau\) and the operator \(\bigoplus_QUD_Q\mathcal V_{\tau,Q}D_QU^*\) (the sampled blocks compressed to the domains and placed in \(\ell^2(\Gamma)\)) differ exactly by the part of \(C_\tau\) along the remaining edges, by Lemma 1.1 and the disjointness of the domains; Lemma 2.1 bounds it. The sampled blocks differ from the mean blocks \(U_{\tau,ik}\otimes S_{\tau,ik}\) by at most the sampling accuracy in full norm, and compression to the domains and orthogonal summation over sheets do not increase this. So every factor of the word (4.2) of the previous lesson has a finite Cayley formula within a prescribed \(\theta\) of its image under \(\Psi_\nu\), once \(s\) is large.

*The word.* Let \(b_f\) be the same word (4.2) with every factor replaced by its Cayley formula. By (3.2) of the previous lesson, replacing the product of the compressed means by the compression of their product costs at most \(\delta_\nu^2\) times a fixed product of norms at each of the finitely many steps. Replacing each factor by its Cayley formula costs, by telescoping, at most \(r\theta(L+\theta)^{r-1}\) for a product of \(r\) factors of norm at most \(L\); the numbers \(r\) and \(L\) are fixed before the degree choice, so the sampling and forest errors can be made small enough. Choose \(s\) and then \(H_0\) to make the deletion term \(C_fk\sqrt{\varepsilon_{\rm del}}\) and the trimming term small. With (4.3) of the previous lesson this proves (3.1).

No physical projection selecting a height is used: each designated symbol has its prescribed value at every block, possibly zero. On a zero block the weights are zero while the voltages remain diffuse. A parity pattern or an exception at the initial height changes only this finite prescription and adds no labels indexed by the height. \(\square\)

## 4. Exercises

**Exercise 4.1.** Prove the telescoping bound: if \(\|A_j\|\le L\) and \(\|A_j-B_j\|\le\theta\) for \(j=1,\ldots,r\), then \(\|A_1\cdots A_r-B_1\cdots B_r\|\le r\theta(L+\theta)^{r-1}\).

**Exercise 4.2.** Why must the residual forest include Cayley edges whose two ends lie in one domain but which are not edges of that sheet?

**Exercise 4.3.** Compute \(\log_2\bigl(\sqrt{|\mathcal S_{\rm wt}|}/q\bigr)\) to leading order in \(s\) from \(\log_2|\mathcal S_{\rm wt}|=1.00005s+O(\log s)\) and \(\log_2q=0.50005s\).

## 5. Solutions

**4.1.** Telescoping gives
\[
\begin{gathered}
A_1\cdots A_r-B_1\cdots B_r\\
=\sum_{j=1}^rB_1\cdots B_{j-1}(A_j-B_j)A_{j+1}\cdots A_r ,
\end{gathered}
\]
and since \(\|B_j\|\le L+\theta\), each term has norm at most \((L+\theta)^{j-1}\theta L^{r-j}\le\theta(L+\theta)^{r-1}\).

**4.2.** The polynomial \(C_\tau\) acts along every Cayley edge with a label of \(\mathcal S_\tau\). A chord between two domain vertices of one sheet that is not a source edge of that sheet is not part of the sampled block \(\mathcal V_\tau\); its contribution must be estimated separately, and Proposition 2.1 of the lesson on cycle coordinates puts it in the forest.

**4.3.** \(\frac12\cdot1.00005s-0.50005s=-0.000025s\), up to \(O(\log s)\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Section 8.3, Lemma 8.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
