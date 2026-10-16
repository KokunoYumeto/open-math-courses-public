# Expansion and the sequential law

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The permutation tables of the tower are now chosen. Two things are needed from one probability law on all tables. Every auxiliary incidence must *expand*: its normalized incidence operator, restricted to functions of mean zero, must have norm at most a fixed \(\rho<1\), for all heights at once. And the law must stay close to independent uniform tables at each step: conditioning on the expansion of the current incidence may raise the probability of a joint test of \(k\) current tables by at most \(e^{\varepsilon_sk}\) with \(\varepsilon_s\to0\). The pruning lessons need the second property. Both come from a Fourier bound on the mean incidence, a concentration bound for each cut, and the local lemma with its conditional form [OpenAI-BCI, Section 3].

- The current matching variables (Section 1).
- The mean incidence (Section 2).
- Cuts (Section 3).
- The local lemma and a conditioning bound (Section 4).
- From cuts to a gap (Section 5).
- The sequential law (Section 6).

The notation of [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md) and [Auxiliary incidences, deletions and recovery](auxiliary-incidences-deletions-and-recovery.md) is in force. We use two results of the course [A torsion-free counterexample to the Kadison–Kaplansky conjecture](course:kadison-kaplansky-projections/the-conjecture-and-scalar-compression): the exponential moment bound for sampling with or without replacement, Lemma 5.1 of [Streams, slots and slot evaluations](course:kadison-kaplansky-projections/streams-slots-and-slot-evaluations#5-concentration-for-sampling-with-and-without-replacement), and the conditional Fourier estimate, Lemma 2.1 of [The mean incidence and its gap](course:kadison-kaplansky-projections/the-mean-incidence-and-its-gap#2-a-conditional-fourier-estimate).

## 0. The choice of b

Put \(\theta=2^{1-b}\), and fix the integer \(b\) once and for all so large that
\[
\eta:=\sqrt{5\theta}<\tfrac35 .\tag{0.1}
\]
For example \(b=5\) gives \(\theta=1/16\) and \(\eta=\sqrt5/4<0.56\).

Throughout Sections 1 to 5 fix a family occurrence at a marked cutoff, all tables at earlier source indices, and one extra slice. Only the tables of the current marked index are random, and the *reference law* makes them independent uniform permutations. Write \(A,B\) for the two endpoint spaces of the slice, at the common cutoff, and for functions on them define, with sums over slots (parallel edges counted separately),
\[
\begin{gathered}
(Nf)(a)=\frac1d\sum_{e:\,e^-=a}f(e^+),\\
(N^*g)(b')=\frac1D\sum_{e:\,e^+=b'}g(e^-).
\end{gathered}
\]
Averages on \(A\) and \(B\) are probability averages. Since \(d|A|=D|B|\), these are adjoint contractions that fix constants. Let \(\mathsf M=\mathbb EN\), the expectation over the current tables; \(\mathsf M\) has the same properties.

## 1. The current matching variables

**Lemma 1.1** (fresh matching coordinates; [OpenAI-BCI, Lemma 3.1]). Under the reference law, the auxiliary incidence of the fixed occurrence and slice is given by independent uniform perfect matchings between pairs of *clusters* of \(2^t\) slot incidences, one pair of clusters for each key of a current table. Every edge between two matched clusters is possible, different keys have disjoint clusters, and no table of a later index affects the incidence.

*Proof.* Suppose the marked block is a \(B\)-block; the other case exchanges the sides. Fix the serial number, the label head and all raw input blocks before the marked index; with the slot names this fixes the key of the current table. By Lemma 1.1 of the previous lesson, the remaining coordinates of a \(B\)-endpoint are the \(t\) raw bits of its last input block (the known correction only translates them), and those of an \(A\)-endpoint are the corresponding \(t\) bits of its evaluation; all other coordinates are determined. The current table, forced on by the auxiliary prescription, is an arbitrary bijection of \(\mathbb F_2^t\) between these two sets of \(2^t\) slot incidences, and under the reference law it is uniform. Distinct keys give disjoint sets. Later tables act beyond the common support and are identities there (Lemma 1.1 of the previous lesson). \(\square\)

## 2. The mean incidence

Let \(P^A_h\) be the conditional expectation (on the probability space \(A\)) onto functions of the first \(r+hs\) bits of both raw \(A\)-streams, and \(P^B_j\) the conditional expectation onto functions of the first \(js\) bits of both raw \(B\)-streams. Padded coordinates are constant zero, so both filtrations end at the identity, and \(P^B_0=C_B\) is the projection onto constants; write \(C_A\) for the projection onto constants on \(A\).

**Prefix data.** For a fixed \(A\)-slot, a function in the range of \(P^B_j\) evaluated at the neighbor depends only on
\[
\begin{gathered}
u_A[0,r+(j-1)s)\\
\text{and}\quad Q_A[0,r+js),
\end{gathered}\tag{2.1}
\]
where \(Q_A\) is the corrected evaluation. Indeed, the first \(r\) bits of \(Q_A\) give the label head; inverting the triangular transformations block by block gives \(u_B\) through \(B_j\), using \(Q_A\) through position \(r+js\) and keys made of earlier raw blocks; and the second edge equation gives \(v_B\) through \(js\), using \(u_A\) only through \(A_{j-1}\). In the same way, for a fixed \(B\)-slot a function in the range of \(P^A_h\) evaluated at the neighbor depends only on
\[
\begin{gathered}
u_B[0,hs)\\
\text{and}\quad Q_B[0,(h+1)s),
\end{gathered}\tag{2.2}
\]
the bucket being part of the slot. These statements hold for the corrected coordinates as well: the extra bits are fixed in the slice, every gate of a correction ends before both coupled blocks, the current gate is forced open, and beyond the cutoff the identity rules apply. Since every evaluation block depends on its input block only through the block-diagonal term, (2.1) and (2.2) give
\[
\begin{gathered}
\operatorname{ran}(\mathsf MP^B_j)\subseteq\operatorname{ran}P^A_j,\\
\operatorname{ran}(\mathsf M^*P^A_h)\subseteq\operatorname{ran}P^B_{h+1},
\end{gathered}\tag{2.3}
\]
for every realization of the tables and hence for \(\mathsf M\).

**Lemma 2.1** (one new block). If the blocks involved are full,
\[
\begin{gathered}
\|(1-P^A_{j-1})\mathsf MP^B_j\|^2\le\theta,\\
\|(1-P^B_h)\mathsf M^*P^A_h\|^2\le\theta .
\end{gathered}\tag{2.4}
\]

*Proof.* Let \(g\) be in the range of \(P^B_j\). By (2.1), for an \(A\)-state with prefix data \(C\) (both raw \(A\)-streams through \(r+(j-1)s\)), the value \((\mathsf Mg)(a)\) has the form
\[
\frac1d\sum_{\nu}f_\nu(C,\,V+K_\nu U+o_\nu),
\]
the sum over the \(d\) slot names \(\nu\) of the slice, where \(U\) is the raw input block \(A_j\), \(V\) the raw evaluation block of index \(2j\), \(o_\nu\) the known offset, and \(f_\nu\) contains the average over the current tables. The direct dependence of the neighbor's data on \(u_A\) stops before \(A_j\), and the coefficient of an \(A\)-name does not depend on the bucket. For a uniform \(A\)-state, \(C,U,V\) are independent and \(U,V\) uniform. By Lemma 3.1 of [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md), every value of \(\zeta\circ K_\nu\), for a nonzero functional \(\zeta\), is taken by at most \(\theta d\) names. The conditional Fourier estimate (Lemma 2.1 of [The mean incidence and its gap](course:kadison-kaplansky-projections/the-mean-incidence-and-its-gap#2-a-conditional-fourier-estimate)) gives
\[
\begin{gathered}
\|(1-P^A_{j-1})\mathsf Mg\|^2\\
\le\theta\,\mathbb E\Bigl[\frac1d\sum_\nu2^{-s}\sum_z|f_\nu(C,z)|^2\Bigr] .
\end{gathered}
\]
The right side is at most \(\theta\|g\|^2\): a uniform \(A\)-state with a uniform slot has a uniform \(B\)-neighbor, since the incidence is biregular, so the slot average of \(|g|^2\) at the neighbor is \(\|g\|^2\); averaging over the current tables inside \(f_\nu\) only decreases it, by Jensen's inequality; and \(V\) makes the evaluation argument uniform given everything else. The second bound is proved in the same way with the next \(B\)-input and evaluation blocks; the slot fixes the bucket, and the coefficient of a \(B\)-name involves no unknown part of the head. \(\square\)

**Lemma 2.2** (the conditional mean; [OpenAI-BCI, Lemma 3.3]). For every history of earlier tables, every marked cutoff and every extra slice,
\[
\|\mathsf M:\mathbf1_B^\perp\to\mathbf1_A^\perp\|\le\eta=\sqrt{5\theta}<\tfrac35 .
\]
The same bound holds for the complete adjacent-height incidence, with all extra values.

*Proof.* *Full blocks.* Put \(E^A_0=P^A_0-C_A\), \(E^A_h=P^A_h-P^A_{h-1}\) for \(h\ge1\), and \(E^B_j=P^B_j-P^B_{j-1}\) for \(j\ge1\). By (2.3), \(E^A_h\mathsf ME^B_j=0\) unless \(h\le j\le h+1\). The *band* \(j=h\) is bounded by the first estimate of (2.4), and the band \(j=h+1\) by the adjoint of the second. Within one band the input spaces are mutually orthogonal, and so are the output spaces, so each band has norm at most \(\sqrt\theta\), and their sum at most \(2\sqrt\theta\).

*The terminal block.* Suppose the last active input block is a \(B\)-block; in the notation of Lemma 1.1 of the lesson on streams, \(\ell_A=r+ns\), \(\ell_B=ns+t\), \(|v_A|=r+ns+t\) and \(|v_B|=(n+1)s\). For the differences \(E^B_j\) with \(1\le j\le n\), all blocks used in both bands are full, so
\[
\|\mathsf M(P^B_n-C_B)\|\le2\sqrt\theta .\tag{2.5}
\]
Now fix a \(B\)-slot. Inversion through the preceding blocks determines all of \(u_A\) and all but the last \(t\) bits of \(v_A\) from \(u_B[0,ns)\) and \(Q_B[0,(n+1)s)\). The last \(t\) bits of \(Q_A\) are the output of the current prefix table, whose key consists of the label and earlier raw blocks; averaged over that uniform table they are uniform, whatever its argument is. The term \(K_\nu u_A\) ends at position \(r+ns\), so these are exactly the remaining \(t\) bits of \(v_A\), up to a known correction. After this average, \((\mathsf M^*f)(b')\) does not depend separately on the last \(t\) raw bits of \(u_B\): given \(P^B_n\), it is a function of \(V+K_\nu U+o_\nu\) with \(U\in\mathbb F_2^t\) these bits and \(V\in\mathbb F_2^s\) the last evaluation block. The Fourier estimate, with the multiplicity bound for prefixes of length \(t\ge b\), gives
\[
\|(1-P^B_n)\mathsf M^*\|^2\le\theta .
\]
For \(f\) orthogonal to the constants on \(A\), \(C_B\mathsf M^*f=0\), so \(P^B_n\mathsf M^*f=(P^B_n-C_B)\mathsf M^*f\), whose norm is at most \(2\sqrt\theta\|f\|\) by the adjoint of (2.5). The two components are orthogonal, so \(\|\mathsf M^*f\|^2\le(4\theta+\theta)\|f\|^2=5\theta\|f\|^2\).

If the last active input block is an \(A\)-block, then \(\ell_B=(n+1)s\), \(\ell_A=r+ns+t\), \(|v_A|=r+(n+1)s\) and \(|v_B|=(n+1)s+t\). The band argument gives \(\|\mathsf M^*(P^A_n-C_A)\|\le2\sqrt\theta\); the current table averages the last \(t\) bits of \(Q_B\), where \(K_\nu u_B\) vanishes; and the same argument gives \(\|(1-P^A_n)\mathsf M\|^2\le\theta\) and the bound. Both cases include \(t=s\), and the initial block \(A_0\) is never terminal because the tower starts after many complete blocks.

*All extra slices.* If the larger endpoint is on side \(A\), its space is the slice space times \(\mathbb F_2^b\), and the complete operator has components \(\mathsf M_e\), one for each extra value; for \(f\) orthogonal to the constants on \(B\), \(\|\mathsf Mf\|^2=\mathbb E_e\|\mathsf M_ef\|^2\le\eta^2\|f\|^2\). If the larger endpoint is on side \(B\), write an input as \(f_e=c_e+f^0_e\) with constants \(c_e\) and \(f_e^0\) of mean zero; mean zero of \(f\) gives \(\mathbb E_ec_e=0\), so \(\mathsf Mf=\mathbb E_e\mathsf M_ef^0_e\), and Jensen's inequality gives \(\|\mathsf Mf\|^2\le\mathbb E_e\eta^2\|f_e^0\|^2\le\eta^2\|f\|^2\). \(\square\)

## 3. Cuts

Return to one slice. Give every vertex its degree, \(\deg=d\) on \(A\) and \(\deg=D\) on \(B\), put \(\operatorname{vol}(S)=\sum_{v\in S}\deg(v)\) for a set \(S\) of vertices of \(A\sqcup B\), let \(V_0=2d|A|\) be the total volume, and let \(c(S)\) be the number of edges between \(S\) and its complement, with multiplicity.

**Lemma 3.1** (mean cut). If \(\operatorname{vol}(S)\le V_0/2\), then
\[
\begin{aligned}
&\mathbb E\,c(S)\\
&\quad\ge(1-\eta)\operatorname{vol}(S)\Bigl(1-\frac{\operatorname{vol}(S)}{V_0}\Bigr)\\
&\quad\ge\tfrac15\operatorname{vol}(S).
\end{aligned}
\]

*Proof.* Let \(P\) be the random walk operator on \(A\sqcup B\), equal to \(N\) on functions on \(B\) and \(N^*\) on functions on \(A\), and let \(\langle f,g\rangle=\sum_v\deg(v)f(v)\overline{g(v)}\). Then \(\langle\mathbf1_S,P\mathbf1_S\rangle\) counts edges with both ends in \(S\) twice, so \(c(S)=\operatorname{vol}(S)-\langle\mathbf1_S,P\mathbf1_S\rangle\). With respect to \(\langle\cdot,\cdot\rangle\), \(\mathbb EP\) is self-adjoint, fixes \(\mathbf1\), and on the orthogonal complement of \(\mathbf1\) its quadratic form is at most \(\eta\) times the norm squared: on functions of mean zero on each side it acts by the off-diagonal blocks \(\mathsf M,\mathsf M^*\) of norm at most \(\eta\) (Lemma 2.2), and on the function equal to \(1\) on \(A\) and \(-1\) on \(B\), which is orthogonal to those, it is \(-1\). Write \(\mathbf1_S=\frac{\operatorname{vol}(S)}{V_0}\mathbf1+g\) with \(g\perp\mathbf1\); then \(\|g\|^2=\operatorname{vol}(S)-\operatorname{vol}(S)^2/V_0\), and
\[
\begin{gathered}
\mathbb E\,c(S)\ge\operatorname{vol}(S)-\frac{\operatorname{vol}(S)^2}{V_0}-\eta\|g\|^2\\
=(1-\eta)\|g\|^2 .
\end{gathered}
\]
For \(\operatorname{vol}(S)\le V_0/2\) and \(\eta<3/5\) this is at least \(\frac25\cdot\frac12\operatorname{vol}(S)\). \(\square\)

**Lemma 3.2** (tail of a cut). If \(\operatorname{vol}(S)\le V_0/2\), then, with \(d_{\min}=\min\{d,D\}=d\) and \(c_0=10^{-3}\),
\[
\begin{gathered}
\mathbb P\{c(S)<0.05\operatorname{vol}(S)\}\\
\le e^{-0.01125\operatorname{vol}(S)}\le e^{-c_0d_{\min}|S|} .
\end{gathered}
\]

*Proof.* For a current table \(a\), with clusters of size \(n_a=2^t\), let \(u_a\) and \(v_a\) be the numbers of its \(A\)-slot and \(B\)-slot incidences belonging to vertices of \(S\), and \(Z_a\) the number of its matched pairs with both ends in \(S\). By Lemma 1.1 the images of the \(u_a\) incidences form a uniform \(u_a\)-subset of the cluster on the other side, so \(Z_a\) is the number of ones in \(u_a\) draws without replacement from a list with \(v_a\) ones and \(n_a-v_a\) zeros; by Lemma 5.1 of [Streams, slots and slot evaluations](course:kadison-kaplansky-projections/streams-slots-and-slot-evaluations#5-concentration-for-sampling-with-and-without-replacement), \(\mathbb Ee^{\lambda(Z_a-\mathbb EZ_a)}\le e^{\lambda^2u_a/8}\). The \(Z_a\) are independent, \(\sum_au_a\le\operatorname{vol}(S)\), and \(c(S)=\operatorname{vol}(S)-2\sum_aZ_a\). If \(c(S)<0.05\operatorname{vol}(S)\), then by Lemma 3.1
\[
\begin{gathered}
\textstyle\sum_aZ_a-\mathbb E\sum_aZ_a\\
>0.475\operatorname{vol}(S)-0.4\operatorname{vol}(S)=0.075\operatorname{vol}(S).
\end{gathered}
\]
The exponential Markov inequality with \(\lambda=0.3\) bounds the probability by \(e^{(-0.0225+0.01125)\operatorname{vol}(S)}\). Finally \(\operatorname{vol}(S)\ge d|S|\). \(\square\)

## 4. The local lemma and a conditioning bound

Join two vertices of \(A\sqcup B\) when some choice of a current table could join them by an edge; this is the *possible graph*. A cluster has at most \(2^s\) incidences and a vertex at most \(T2^bD\) slots, so its maximum degree \(\Delta\) satisfies \(\Delta\le2^{Cs}\), with \(C\) depending only on \(T\) and \(b\); each current table meets at most \(2^{Cs}\) vertices, and each vertex meets at most \(2^{Cs}\) tables. For every nonempty set \(S\), connected in the possible graph, with \(\operatorname{vol}(S)\le V_0/2\), let \(\mathcal A_S\) be the *cut failure* \(c(S)<0.05\operatorname{vol}(S)\). Avoiding these events suffices: a set of volume at most \(V_0/2\) is the disjoint union of its components in the possible graph, no edge joins two components, and both volume and \(c\) are additive over them.

**Lemma 4.1** (local lemma with conditioning). Let \(\mathcal A_1,\ldots,\mathcal A_n\) be events, and let a graph on \(\{1,\ldots,n\}\) be such that each \(\mathcal A_i\) is independent of the family of all \(\mathcal A_j\) with \(j\ne i\) not adjacent to \(i\). Suppose \(0\le x_i<1\) and
\[
\begin{gathered}
\mathbb P(\mathcal A_i)\le x_i\prod_{j\sim i}(1-x_j)\\
\text{for all }i.
\end{gathered}\tag{4.1}
\]
Then for every set \(J\) of indices with \(i\notin J\), \(\mathbb P(\bigcap_J\mathcal A_j^c)>0\) and \(\mathbb P(\mathcal A_i\mid\bigcap_J\mathcal A_j^c)\le x_i\). If \(\mathcal B\) is an event independent of the family of all \(\mathcal A_j\) with \(j\notin J_1\), then
\[
\mathbb P\Bigl(\mathcal B\Bigm|\bigcap_{j}\mathcal A_j^c\Bigr)\le\mathbb P(\mathcal B)\prod_{j\in J_1}(1-x_j)^{-1} .
\]

*Proof.* The first two assertions are proved together by induction on \(|J|\); for \(J=\emptyset\) they hold by (4.1). Split \(J\) into the neighbors \(J_1'\) of \(i\) and the rest \(J_2'\). If \(J_1'\) is empty, independence gives \(\mathbb P(\mathcal A_i\mid\bigcap_J\mathcal A^c)=\mathbb P(\mathcal A_i)\le x_i\). Otherwise
\[
\begin{gathered}
\mathbb P\Bigl(\mathcal A_i\Bigm|\bigcap_J\mathcal A^c\Bigr)\le\frac{\mathbb P(\mathcal A_i\mid\bigcap_{J_2'}\mathcal A^c)}{\mathbb P(\bigcap_{J_1'}\mathcal A^c\mid\bigcap_{J_2'}\mathcal A^c)}\\
=\frac{\mathbb P(\mathcal A_i)}{\mathbb P(\bigcap_{J_1'}\mathcal A^c\mid\bigcap_{J_2'}\mathcal A^c)} .
\end{gathered}
\]
Writing \(J_1'=\{j_1,\ldots,j_m\}\), the denominator is \(\prod_l\bigl(1-\mathbb P(\mathcal A_{j_l}\mid\bigcap_{J_2'}\mathcal A^c\cap\bigcap_{l'<l}\mathcal A_{j_{l'}}^c)\bigr)\), each conditioning on fewer than \(|J|\) events, so by induction it is at least \(\prod_{j\sim i}(1-x_j)>0\), and (4.1) gives the bound \(x_i\). The same product, step by step, shows \(\mathbb P(\bigcap_J\mathcal A^c)\ge\prod_J(1-x_j)>0\).

For \(\mathcal B\), let \(J_2\) be the complement of \(J_1\). By independence
\[
\begin{gathered}
\mathbb P\Bigl(\mathcal B\Bigm|\bigcap\mathcal A^c\Bigr)\le\frac{\mathbb P(\mathcal B\mid\bigcap_{J_2}\mathcal A^c)}{\mathbb P(\bigcap_{J_1}\mathcal A^c\mid\bigcap_{J_2}\mathcal A^c)}\\
=\frac{\mathbb P(\mathcal B)}{\mathbb P(\bigcap_{J_1}\mathcal A^c\mid\bigcap_{J_2}\mathcal A^c)},
\end{gathered}
\]
and the product rule with the first part bounds the denominator below by \(\prod_{J_1}(1-x_j)\). \(\square\)

The asymmetric local lemma is due to Erdős and Lovász [EL]; the conditional bound for an additional event is the estimate of Haeupler, Saha and Srinivasan [HSS, Theorem 2.1], proved above in the form needed here.

**Proposition 4.2** (expanding tables with a conditioning bound). For large \(s\), uniformly in the height and in the earlier tables, the cut failures of the fixed occurrence and slice can all be avoided simultaneously with positive probability under the reference law. Moreover there is \(\varepsilon_s\to0\), independent of the height and of the earlier history, such that for every event \(\mathcal B\) determined by \(k\) specified current tables, and every nonnegative function \(F\) of \(k\) specified current tables,
\[
\begin{aligned}
&\mathbb P(\mathcal B\mid\text{no cut failure})\\
&\qquad\le e^{\varepsilon_sk}\,\mathbb P(\mathcal B),\\
&\mathbb E(F\mid\text{no cut failure})\\
&\qquad\le e^{\varepsilon_sk}\,\mathbb E F .
\end{aligned}\tag{4.2}
\]

*Proof.* An event \(\mathcal A_S\) depends only on the tables meeting \(S\). Join two events when their sets of tables meet; events with disjoint tables are independent, jointly with any family of events using other tables. If the table sets of \(\mathcal A_S\) and \(\mathcal A_{S'}\) meet, some vertex of \(S'\) is within distance two of \(S\) in the possible graph. A connected \(j\)-set containing a given vertex is determined by a walk of length \(2(j-1)\) along a depth-first traversal of a spanning tree chosen by fixed orders, so there are at most \(\Delta^{2(j-1)}\) of them. Hence the number of neighbors of \(\mathcal A_S\) indexed by \(j\)-sets is at most \(|S|\Delta^{2j+C_1}\) for an absolute \(C_1\).

Put \(x_S=\exp(-c_0d|S|/2)\). Then
\[
\begin{gathered}
\sum_{S'\sim S}x_{S'}\le|S|\sum_{j\ge1}\Delta^{2j+C_1}e^{-c_0dj/2}\\
=|S|\,\delta_s,
\end{gathered}
\]
and \(\delta_s\to0\) because \(\log\Delta=O(s)\) while \(d=2^{.40005s}\). For large \(s\), all \(x_S\le\frac12\) and \(2\delta_s\le c_0d/2\); since \(\log(1-x)\ge-2x\) for \(0\le x\le\frac12\),
\[
\begin{gathered}
x_S\prod_{S'\sim S}(1-x_{S'})\ge e^{-c_0d|S|/2-2\delta_s|S|}\\
\ge e^{-c_0d|S|}\ge\mathbb P(\mathcal A_S)
\end{gathered}
\]
by Lemma 3.2. There are finitely many events, and Lemma 4.1 gives positive probability of avoiding all of them.

For \(\mathcal B\) determined by \(k\) tables, let \(J_1\) be the cut failures that share one of these tables; \(\mathcal B\) is independent of the family of the others. Each table meets at most \(2^{Cs}\) vertices, so
\[
\begin{aligned}
\sum_{S\in J_1}x_S&\le k\,2^{Cs}\sum_{j\ge1}\Delta^{2j+C_1}e^{-c_0dj/2}\\
&=:k\,\varepsilon_s/2,
\end{aligned}
\]
and \(\varepsilon_s\to0\). Lemma 4.1 and \(\prod(1-x)^{-1}\le e^{2\sum x}\) give (4.2) for \(\mathcal B\), and for \(F\) by integrating over its level sets. \(\square\)

The bound (4.2) concerns a joint test of current tables. It does not bound the conditional law of one table entry after other entries of the same table have been prescribed.

## 5. From cuts to a gap

**Lemma 5.1** (Cheeger bound). Let a finite bipartite multigraph on \(A\sqcup B\) be biregular with degrees \(d\) on \(A\) and \(D\) on \(B\), so that \(d|A|=D|B|\), and suppose that \(c(S)\ge0.05\operatorname{vol}(S)\) for every set \(S\) with \(\operatorname{vol}(S)\le V_0/2\). Then its normalized incidence operator \(N\) satisfies
\[
\begin{gathered}
\|N:\mathbf1_B^\perp\to\mathbf1_A^\perp\|\le\rho,\\
\rho:=1-\frac{0.05^2}2\\
=1-\frac1{800} .
\end{gathered}\tag{5.1}
\]

*Proof.* For a function \(w\ge0\) whose support has volume at most \(V_0/2\), every level set \(\{w^2>\tau\}\) has volume at most \(V_0/2\), and an edge \(xy\) crosses it exactly for \(\tau\) between \(w(x)^2\) and \(w(y)^2\). Integrating the cut bound over \(\tau\),
\[
\begin{aligned}
&\sum_{\text{edges }xy}|w(x)^2-w(y)^2|\\
&\qquad=\int_0^\infty c(\{w^2>\tau\})\,d\tau\\
&\qquad\ge0.05\sum_v\deg(v)w(v)^2 .
\end{aligned}
\]
By the Cauchy–Schwarz inequality and the bound of \(\sum_{xy}(w(x)+w(y))^2\) by \(2\sum_v\deg(v)w(v)^2\), the left side is at most \(\bigl(\mathcal E(w)\cdot2\sum_v\deg(v)w(v)^2\bigr)^{1/2}\), where \(\mathcal E(w)=\sum_{xy}(w(x)-w(y))^2\). So \(\mathcal E(w)\ge\frac{0.05^2}2\sum_v\deg(v)w(v)^2\).

Let \(f\) be real with \(\sum_v\deg(v)f(v)=0\), and let \(m\) be a weighted median, so that \(\{f>m\}\) and \(\{f<m\}\) have volume at most \(V_0/2\). Applied to \(w_\pm=(\pm(f-m))_+\), and since on every edge the energies of \(w_+\) and \(w_-\) add up to at most that of \(f\),
\[
\begin{gathered}
\mathcal E(f)\ge\tfrac{0.05^2}2\sum_v\deg(v)(f(v)-m)^2\\
\ge\tfrac{0.05^2}2\sum_v\deg(v)f(v)^2 ,
\end{gathered}
\]
the last step because \(f\) has weighted mean zero. Apply this to real and imaginary parts. In the degree inner product, \(\mathcal E(f)=\langle f,f\rangle-\langle f,Pf\rangle\) for the walk operator \(P\) of Lemma 3.1, so \(\langle f,Pf\rangle\le\rho\langle f,f\rangle\) for \(f\perp\mathbf1\). The operator \(P\) is self-adjoint with off-diagonal blocks \(N,N^*\); conjugation by \(\operatorname{diag}(1,-1)\) changes its sign, so its spectrum on functions of mean zero on each side is symmetric, and its largest value there is \(\|N:\mathbf1_B^\perp\to\mathbf1_A^\perp\|\). Functions of mean zero on each side are orthogonal to \(\mathbf1\), which gives (5.1). \(\square\)

## 6. The sequential law

**Proposition 6.1** (sequential selection; [OpenAI-BCI, Proposition 3.4]). There is a probability law on all permutation tables such that every auxiliary incidence, at every height and in every extra slice, and also with all extra values together, has norm at most \(\rho\) from \(\mathbf1_B^\perp\) to \(\mathbf1_A^\perp\). At each source index, conditionally on all earlier tables, every joint test of \(k\) specified current tables has probability at most \(e^{\varepsilon_sk}\) times its probability under independent uniform current tables, with \(\varepsilon_s\to0\) uniformly in the history and the height. When a test whose tables and arguments are determined by earlier tables is evaluated, its probability is governed by this current kernel alone.

*Proof.* In each family order the source indices increasingly, and interleave the finitely many families by source index and a fixed order of families. At an unmarked index choose the active tables independently and uniformly. At a marked index choose them from the reference law conditioned on avoiding all cut failures of that occurrence, separately in each extra slice; Proposition 4.2 shows that this conditional law exists for every earlier history and satisfies (4.2). Different families use different tables, and at one source index a family has at most one marked occurrence (marks are \(K\) indices apart), so grouping the families at one index multiplies the bounds, with \(k\) the total number of tested tables. Indices with prescribed identities have no random variables.

Each step has finitely many outcomes, so one can realize the steps successively by independent uniform numbers in \([0,1]\), choosing outcomes by consecutive intervals of their conditional probabilities; this defines the law on the infinite sequence of steps. A later step never changes an earlier incidence: tables of later indices act as identities on the padded streams of earlier occurrences (Lemma 1.1 of the previous lesson). So the expansion of every incidence persists, and Lemma 5.1, together with the passage from slices to all extra values in the proof of Lemma 2.2, gives the bound \(\rho\). A test whose tables and arguments are determined by earlier steps is evaluated at its own step, where only the current kernel acts, and all later conditional laws integrate to one. \(\square\)

## 7. Exercises

**Exercise 7.1.** Check that \(b=5\) satisfies (0.1), and find the least \(b\) that does.

**Exercise 7.2.** Show that \(\mathbb EZ_a=u_av_a/n_a\) in the proof of Lemma 3.2, and that \(\sum_a\mathbb EZ_a=\frac12(\operatorname{vol}(S)-\mathbb Ec(S))\).

**Exercise 7.3.** Suppose \(Nf\) is the constant average of \(f\) over \(B\) for every \(f\), as for a biregular multigraph in which every vertex of \(A\) has the same number of edges to every vertex of \(B\). Let \(S\) contain fractions \(\alpha_A\) of \(A\) and \(\alpha_B\) of \(B\). Compute \(c(S)\), and compare it with the bound of Lemma 3.1 for \(\eta=0\).

**Exercise 7.4.** Explain why (4.2) cannot be applied to "the last unknown entry of a table, given its other entries".

## 8. Solutions

**7.1.** \(b=5\): \(\theta=1/16\), \(5\theta=5/16\), \(\eta=0.559\ldots<0.6\). For \(b=4\): \(\theta=1/8\), \(5\theta=0.625\), \(\eta=0.79\ldots\). So \(b=5\) is the least.

**7.2.** Each of the \(u_a\) incidences is matched to a uniform element of the other cluster, which lies in \(S\) with probability \(v_a/n_a\). Every edge with both ends in \(S\) is a matched pair of exactly one table, so \(2\sum_aZ_a=\operatorname{vol}(S)-c(S)\); take expectations.

**7.3.** Here \(N\) vanishes on functions of mean zero, so \(\eta=0\). The edges with both ends in \(S\) number \(d|S\cap A|\alpha_B=\frac{V_0}2\alpha_A\alpha_B\), and \(\operatorname{vol}(S)=\frac{V_0}2(\alpha_A+\alpha_B)\). Hence
\[
c(S)=\tfrac{V_0}2(\alpha_A+\alpha_B)-V_0\alpha_A\alpha_B .
\]
The bound of Lemma 3.1 is \(\operatorname{vol}(S)(1-\operatorname{vol}(S)/V_0)\), which equals \(\frac{V_0}2(\alpha_A+\alpha_B)(1-\frac{\alpha_A+\alpha_B}2)\), and the difference is \(\frac{V_0}4(\alpha_A-\alpha_B)^2\ge0\). So the bound is attained exactly when \(\alpha_A=\alpha_B\).

**7.4.** Once the other \(2^t-1\) entries of a permutation are prescribed, the last entry is determined, so its conditional law is a point mass, not close to uniform. Proposition 4.2 compares the law of whole tables with the uniform law, through events of the form "the tables lie in a set"; prescribing entries one at a time changes the reference probabilities themselves.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Section 3, Lemmas 3.1-3.3, Proposition 3.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [EL] P. Erdős and L. Lovász, *Problems and results on 3-chromatic hypergraphs and some related questions*, in Infinite and Finite Sets, Colloq. Math. Soc. János Bolyai 10 (1975), 609-627, Section 2. https://users.renyi.hu/~p_erdos/1975-34.pdf
- [HSS] B. Haeupler, B. Saha and A. Srinivasan, *New constructive aspects of the Lovász local lemma*, J. ACM 58 (2011), Theorem 2.1; arXiv:1001.1231. https://arxiv.org/abs/1001.1231
- [MT] R. A. Moser and G. Tardos, *A constructive proof of the general Lovász local lemma*, J. ACM 57 (2010), Theorem 1.1; arXiv:0903.0544. https://arxiv.org/abs/0903.0544
