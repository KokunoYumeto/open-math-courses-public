# Lifespans and the memory space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the model of [*Independent residue lines*](independent-residue-lines.md), every group prime \(p\) has its own random kernel line \(\ell_p\), uniformly distributed in \(\mathbb P^1(\mathbb F_p)\), and the moment factors into one expectation per prime. A prime in a list must have \(\ell_p\) equal to the line of the current position; a prime outside the lists is damped whenever \(\ell_p\) happens to equal that line. If a prime is in the lists, leaves them, and returns later, the probability \(1/(p+1)\) that \(\ell_p\) takes the required value is paid only once, while a naive step-by-step bound would pay it at every return. This lesson computes each prime's expectation exactly as a sum over *lifespans*, and then builds a Hilbert space with a *memory* of pending primes and their lines, on which the moment becomes a product of one operator per step. The memory carries a prime across the gap between two of its uses, so that the operator product reproduces the exact expectation.

**Prerequisites.** [*Physical states and good positions*](physical-states-and-good-positions.md), Sections 2–3; [*Independent residue lines*](independent-residue-lines.md), Sections 2 and 4.

We work at a fixed archimedean root \(\mathbf a\) of the model, with a fixed path datum: positions \(z_0=e_1,\dots,z_N=e_1\) in root coordinates, the lists at every visit, and the reorderings. Recall \(q_j\in\{\frac12,\frac14\}\), \(\eta_j=1-q_j\in\{\frac12,\frac34\}\), and write \(H_j(\ell)=\mathbf 1_{[z_j]_p=\ell}\) when the prime \(p\) is clear from context. Let \(p_{\min}=\exp(L^{a_1})\) be the smallest possible group prime.

## 1. The expectation of one prime

Put

\[
\begin{gathered}
b'_p=1-\frac1{p+1}\sum_{j=0}^N\eta_j,\\
\nu_i(p)=\frac1{V_i(p+1)b'_p}\quad(p\in\mathcal P_i).\quad(1.1)
\end{gathered}
\]

Since \(\sum_j\eta_j\le N+1\le L^{0.51}\) and \(p\ge p_{\min}\), \(b'_p=1+O(L^{0.51}/p)\) is positive and at most \(1\).

**Lemma 1.1 (a prime never in a list).** If \(A_p=\varnothing\), then

\[
\begin{aligned}
&\mathbb E\,\Phi_p(\ell_p)=b'_p\\
&\quad+\frac1{p+1}\sum_{0\le a<c\le N}\eta_a\eta_c\,\mathbf 1_{[z_a]_p=[z_c]_p}\\
&\quad\times\prod_{a<j<c}q_j^{\,\mathbf 1[[z_j]_p=[z_a]_p]}.\quad(1.2)
\end{aligned}
\]

**Proof.** Expand \(\Phi_p(\ell)=\prod_{j=0}^N(1-\eta_jH_j(\ell))\) as \(\sum_{\mathcal J}\prod_{j\in\mathcal J}(-\eta_jH_j(\ell))\) over subsets \(\mathcal J\) of the visits. Averaging over the \(p+1\) lines, the empty set gives \(1\) and each singleton \(\{j\}\) gives \(-\eta_j/(p+1)\); together they give \(b'_p\). For \(|\mathcal J|\ge2\), let \(a<c\) be its least and largest elements. The sum over all \(\mathcal J\) with these extremes is

\[
\begin{gathered}
\eta_a\eta_cH_a(\ell)H_c(\ell)\prod_{a<j<c}\bigl(1-\eta_jH_j(\ell)\bigr),
\end{gathered}
\]

because the inner elements are chosen freely. Averaging over \(\ell\), the product \(H_aH_c\) forces \(\ell=[z_a]_p=[z_c]_p\), which happens for exactly one line, and \(1-\eta_jH_j=q_j^{H_j}\). \(\square\)

**Lemma 1.2 (a prime in some list).** If \(A_p\ne\varnothing\), let \(a=\min A_p\) and \(c=\max A_p\). Then \(\mathbb E\,\Phi_p(\ell_p)=0\) unless all \([z_j]_p\), \(j\in A_p\), equal one line \(\lambda\), and in that case

\[
\begin{aligned}
&\mathbb E\,\Phi_p=\frac1{p+1}\prod_{\substack{a<j<c\\ j\notin A_p}}q_j^{H_j(\lambda)}\\
&\quad\times\Bigl(1-\sum_{h<a}\eta_hH_h(\lambda)\prod_{h<j<a}q_j^{H_j(\lambda)}\Bigr)\\
&\quad\times\Bigl(1-\sum_{h>c}\eta_hH_h(\lambda)\\
&\qquad\qquad\times\prod_{c<j<h}q_j^{H_j(\lambda)}\Bigr).\quad(1.3)
\end{aligned}
\]

**Proof.** The factors \(\mathbf 1_{[z_j]_p=\ell}\), \(j\in A_p\), force \(\ell=\lambda\), a single line, probability \(1/(p+1)\). The inactive visits between \(a\) and \(c\) keep their factors \(1-\eta_jH_j(\lambda)=q_j^{H_j(\lambda)}\). For the visits before \(a\), the telescoping identity

\[
\begin{gathered}
\prod_{j<a}(1-y_j)=1-\sum_{h<a}y_h\prod_{h<j<a}(1-y_j),
\end{gathered}
\]

valid for any numbers \(y_j\), applies with \(y_j=\eta_jH_j(\lambda)\); the visits after \(c\) are treated in the same way, in the reverse order. \(\square\)

**Lifespans.** Divide each expectation by \(b'_p\). Expanding the products (1.2) and (1.3), the factor of a prime becomes a sum over the following configurations, called **lifespans**:

- for a prime never in a list: no lifespan (term \(1\)), or an **orphan lifespan** from a visit \(a\) to a visit \(c>a\) with the same line, with the weight \(\eta_a\eta_c/((p+1)b'_p)\) times \(q_j\) for every visit strictly between \(a\) and \(c\) whose line is that line;
- for a prime in some list: one lifespan containing all its active visits, which may be extended by a **ghost endpoint** \(h<a\) and/or \(h'>c\) with the same line; the weight is \(1/((p+1)b'_p)\), times \(-\eta_h\) and \(-\eta_{h'}\) for the ghost endpoints present, times \(q_j\) for every inactive visit strictly inside the lifespan whose line is the line of the prime.

Inside a lifespan the prime keeps one line. A visit inside the lifespan at which the prime is not active is a **hit** if \([z_j]_p\) equals that line and a **miss** otherwise; only hits are damped. The two ghost endpoints of an orphan carry the signs \(-\eta_a\) and \(-\eta_c\), whose product is \(\eta_a\eta_c\).

**The run charge.** In the weight \(w\) of a datum, every label receives \(V_i^{-1}\) when it is born: the initial list entries through \(\prod_iV_i^{-M}\), and each new last slot of an edge through \(\prod_iV_i^{-1}\). A prime active at two consecutive visits is carried by a copied slot, because the cross-edge ban forbids the new labels of an edge to repeat a label of its source. An **active run** of \(p\) is a maximal interval of consecutive visits in \(A_p\). Hence a prime of group \(i\) with \(\varrho\) active runs is born \(\varrho\) times, and its total factor, before ghost signs and damping, is

\[
\begin{gathered}
\frac{V_i^{-\varrho}}{(p+1)b'_p}=\nu_i(p)\,V_i^{-(\varrho-1)} .\quad(1.4)
\end{gathered}
\]

The line probability is paid once per lifespan, not once per run. This is the feature the memory must reproduce.

## 2. Masses

**Lemma 2.1.** Let \(s_i=\sum_{p\in\mathcal P_i}\nu_i(p)\). Uniformly in the datum, for large \(x\),

\[
\begin{gathered}
\frac{\nu_i(p)}{\mu_i(p)}=1+O\Bigl(\frac{N+1}p\Bigr),\\
s_i=1+O\Bigl(\frac{N+1}{p_{\min}}\Bigr),\\
\max_{i,p}\nu_i(p)\le4e^{-L^{0.1}},\\
\prod_pb'_p\le1 .\quad(2.1)
\end{gathered}
\]

**Proof.** \(\nu_i(p)/\mu_i(p)=p/((p+1)b'_p)\) and \(b'_p=1+O((N+1)/p)\). Summing \(\mu_i(p)(1+O((N+1)/p))\) over \(p\in\mathcal P_i\) gives \(s_i\). The last two claims follow from \(\mu_i(p)\le2e^{-L^{0.1}}\) (Lemma 1.2 of Lesson 2) and \(0<b'_p\le1\). \(\square\)

## 3. The memory space

Fix \(\rho=3/4\); then \(0<\rho<1\) and \(\rho^2=9/16>\frac12\ge q_j\) for every \(j\).

**Particles.** A **memory particle** of group \(i\) is a pair \((p,\lambda)\) with \(p\in\mathcal P_i\) and \(\lambda\in\mathbb P^1(\mathbb F_p)\), its **anchor**. The particle space \(\mathcal X_i\) carries the measure \(\lambda_i(p,\lambda)=\nu_i(p)\): counting measure on anchors, not the uniform probability on lines. A particle **hits** a vector \(z\) if \(\lambda=[z]_p\).

**States and the Hilbert space.** Let \(\mathcal Z\) be the finite set of primitive \(z\) satisfying the tube and box conditions at the root \(\mathbf a\), with counting measure. An **active list** is an ordered \(M\)-tuple of primes of \(\mathcal P_i\) for every \(i\), with the measure \(\bigotimes_i\nu_i^{\otimes M}\); repetitions are allowed in this space, and distinctness is imposed by the operators. The **memory** of group \(i\) is a finite sequence of particles, considered up to order: functions on \(\mathcal X_i^k\) are symmetric, with the measure \(\lambda_i^{\otimes k}/k!\). The Hilbert space is

\[
\begin{gathered}
\mathscr H=\ell^2(\mathcal Z)\otimes L^2\Bigl(\bigotimes_i\nu_i^{\otimes M}\Bigr)\\
\otimes\bigotimes_{i=1}^K\Bigl(\bigoplus_{k\ge0}L^2_{\rm sym}\bigl(\mathcal X_i^k,\lambda_i^{\otimes k}/k!\bigr)\Bigr).\\
(3.1)
\end{gathered}
\]

**Operators by choices.** Each operation below is described by its *choices*: from an input state, a choice produces an output state and carries a coefficient, and choices of new prime values are integrated against \(\nu_i\). The operator acts on a test function \(\phi\) by \((O\phi)(s)\)\(=\sum_{\text{choices }c}\text{coef}(s,c)\,\phi(\text{out}(s,c))\). A product of operations is then a sum over histories of choices, and \(\langle\mathbf b,O_1\cdots O_n\mathbf b\rangle\) is the sum over histories that start and end in the support of \(\mathbf b\), where

\[
\begin{gathered}
\mathbf b=\mathbf 1\{z=e_1,\ \text{all memories empty}\},
\end{gathered}
\]

independent of the active lists. By Lemma 2.1, \(\|\mathbf b\|^2=\prod_is_i^M\)\(=\exp(O_K(M(N+1)/p_{\min}))\)\(=1+o(1)\).

**The ghost operation \(\mathcal G_j\)** at visit \(j\) leaves the position and the active lists unchanged. In every group independently it

1. chooses a subset of the particles hitting the current position \(z_j\) (by their indices) and deletes them, with coefficient \(-\eta_j/\rho\) for each;
2. multiplies by \(q_j/\rho^2\) for each hitting particle that is not deleted;
3. appends an ordered batch of \(l\ge0\) new particles, integrated with \(\nu_i^{\otimes l}/l!\), each anchored at the line of \(z_j\) modulo its prime, with coefficient \((-\eta_jV_i/\rho)^l\).

**The edge operation \(\mathcal E_j\)** from visit \(j\) to visit \(j+1\) keeps the slot symmetrizations, the geometric multiplier of (2.2) of Lesson 8 (or its reversed conjugate, according to the alternation of \(\mathcal A\) and \(\mathcal A^*\)) with the damping factor removed, and replaces the counting of new labels as follows. In every group:

1. multiply by \(\rho\) for every particle in memory that hits the source \(z\); copy the \(J\) shared slots; and either **store** the source's last slot, appending the particle \((p_{i,M},[z]_{p_{i,M}})\) to the memory, or drop it;
2. choose the target \(z'\) (counting measure) and fill the target's last slot either by **promoting** a particle of the memory, other than one stored on this edge, that hits \(z'\) (it is removed from the memory, with coefficient \(1/V_i\)), or by a fresh prime drawn with \(\nu_i\);
3. multiply by \(\rho\) for every particle remaining in memory, including those just stored, that hits \(z'\).

The edge then imposes the physical restrictions with the actual labels: distinct entries in each full list, the cross-edge ban, the pad dyad, the goodness of source and target, and the box conditions. Since the real root matrix has determinant one, the determinant entering the multiplier is \(\det(z,z')\).

The memory has no influence on the multiplier. It only records which primes may be promoted later, and it pays the factors \(\rho\) that, combined with the ghost operations, reproduce the damping.

## 4. The operator history

A **birth** is an initial list entry, a fresh last slot at an edge, or a ghost creation. A history has **globally distinct births** if all its births have different prime values.

**Theorem 4.1 (the operator identity).** At a fixed archimedean root, the model moment of the datum sum, divided by \(\prod_pb'_p\), equals the sum of the histories of

\[
\begin{gathered}
\langle\mathbf b,\ \mathcal G_0\mathcal E_0\mathcal G_1\mathcal E_1\cdots\mathcal E_{N-1}\mathcal G_N\,\mathbf b\rangle\quad(4.1)
\end{gathered}
\]

that have globally distinct births.

**Proof.** We match histories with globally distinct births to pairs consisting of a datum and a choice of lifespan for every prime, and compare weights.

*From histories to lifespans.* In a history, the positions and active lists at the visits form a datum. Fix a prime value \(p\). It is born at most once. A prime in a copied slot keeps its line: if \(p\mid D\), then \(p\mid\det(z,z')\), and since both vectors are primitive, \([z]_p=[z']_p\). When \(p\) leaves the lists it is dropped or stored; if it appears in a list again, it cannot be born again, so it is promoted from its stored particle, which requires the anchor to equal the line of the new position. Ghost creations and deletions occur only at visits whose line equals the anchor. So the history of \(p\) is exactly one lifespan of Section 1, or nothing, and all active lines of \(p\) agree.

*From lifespans to histories.* Conversely, given a datum and a lifespan for every prime compatible with it, the choices are determined: store the prime when it leaves a run that is not its last, promote it when it enters the next run, create a ghost at a ghost starting point, delete at a ghost end, and draw it freshly (or take it from the initial list) when its lifespan begins with an active visit. The factor \(1/l!\) in a ghost batch counts an unordered set of distinct new primes once.

*Weights.* At a pending visit that is a hit, the incoming edge pays \(\rho\) (step 3), the ghost operation pays \(q_j/\rho^2\), and the outgoing edge pays \(\rho\) (step 1):

\[
\begin{gathered}
\rho\cdot\frac{q_j}{\rho^2}\cdot\rho=q_j .\quad(4.2)
\end{gathered}
\]

A miss pays nothing. A ghost creation pays \(-\eta_jV_i/\rho\), and the outgoing edge pays \(\rho\) because the new particle hits its own visit; with the measure \(\nu_i(p)\) of the new prime this gives \(-\eta_jV_i\nu_i(p)=-\eta_j/((p+1)b'_p)\). A ghost deletion pays \(-\eta_j/\rho\), and the incoming edge has paid \(\rho\). An active birth has measure \(\nu_i(p)\), and each promotion pays \(1/V_i\). Comparing with (1.2)–(1.4): a lifespan with \(\varrho\) active runs and no ghosts gets \(\nu_i(p)V_i^{-(\varrho-1)}\); with a ghost start it gets \(-\eta_hV_i\nu_i(p)\cdot V_i^{-\varrho}\), because then all \(\varrho\) runs begin with a promotion; an orphan gets \(\eta_a\eta_c/((p+1)b'_p)\). In each case the line probability \(1/((p+1)b'_p)\) appears exactly once, and every damped hit inside the lifespan gives \(q_j\). At the visits \(0\) and \(N\) there are no unmatched factors: the memory is empty at both ends, so every particle is created after visit \(0\) begins and deleted before visit \(N\) ends.

Finally, the labels and their \(V_i^{-1}\) factors, the reorderings, the geometric multipliers and the archimedean restrictions are the same on both sides. Summing over histories and comparing with the product over primes of the lifespan sums, divided by \(\prod_pb'_p\), proves the theorem. \(\square\)

The two sides agree history by history; no claim is made that global distinctness is a property of individual states. It constrains whole histories, and [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md) restores it by an exact expansion. Lessons 13–15 bound the operators \(\mathcal G_j\) and \(\mathcal E_j\) on the space (3.1) with no distinctness condition at all.

## 5. Exercises

**12.1.** Verify (1.2) by hand when \(N=2\) and all three lines \([z_j]_p\) coincide.

**12.2.** Prove the telescoping identity \(\prod_{j<a}(1-y_j)\)\(=1-\sum_{h<a}y_h\prod_{h<j<a}(1-y_j)\).

**12.3.** A prime of group \(i\) is active at the visits \(1,2,5\) of a path with \(N=6\), with the line \(\lambda\) at these visits; among the other visits, \(\lambda\) is the line of the visits \(0,3,6\) only. List its lifespans, with their weights.

**12.4.** Show that \(\rho=3/4\) satisfies \(\rho^2>q_j\) for all \(j\), and that \(\rho=0.7\) does not.

**12.5.** Explain why a prime cannot be stored and promoted on the same edge, in terms of the cross-edge ban.

## 6. Solutions

**12.1.** With \(H_0=H_1=H_2=1\) at the common line and \(\Phi_p(\ell)=\prod_j(1-\eta_jH_j(\ell))\), the expectation is \(\frac1{p+1}(1-\eta_0)(1-\eta_1)(1-\eta_2)+\frac p{p+1}\). The right side of (1.2) is \(b'_p+\frac1{p+1}(\eta_0\eta_1+\eta_1\eta_2+\eta_0\eta_2(1-\eta_1))\). Expanding \((1-\eta_0)(1-\eta_1)(1-\eta_2)\) gives the same.

**12.2.** Induction on \(a\): if it holds for \(a\), multiply by \(1-y_a\); the new term \(-y_a\) appears with empty product, and the others acquire the factor \(1-y_a\).

**12.3.** Active runs \(\{1,2\}\) and \(\{5\}\), so \(\varrho=2\) and \(a=1\), \(c=5\). Visits \(3,4\) are inactive and inside; \(3\) is a hit and pays \(q_3\), \(4\) is a miss. Possible ghost starts: \(h=0\) (a hit); possible ghost ends: \(h'=6\). The four lifespans have weights \(\nu_i(p)V_i^{-1}q_3\) times \(1\), \(-\eta_0\), \(-\eta_6\), \(\eta_0\eta_6\).

**12.4.** \(q_j\le\frac12<\frac9{16}\). For \(\rho=0.7\), \(\rho^2=0.49<\frac12=q_0\).

**12.5.** A stored prime was the source's last slot; promoting it would make it the target's last slot, a new label equal to a source label, which the ban forbids.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Sections 4.1 and 4.2. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
- H. A. Helfgott and M. Radziwiłł, *Expansion, divisibility and parity*, arXiv:2103.06853 (2021), Sections 1.3, 1.5 and 5, treat centred prime-divisibility weights through walks labelled by primes. https://arxiv.org/abs/2103.06853
