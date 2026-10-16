# Polynomial avoidance, norm tests and moments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The voltages and weights are now drawn, independently over the edges of the pruned old graph, from the laws of [The Fourier envelope and the product sampler](the-fourier-envelope-and-the-product-sampler.md). One choice must do two things at once. Its voltages must make every short closed walk of the base graph lift to an open walk of the covering graph: a short closed walk is not an \(\mathsf H\)-law by the pruning, so its holonomy is a nonzero polynomial in the independent horizontal coordinates, and the small atoms of their law make it rarely trivial. And every weighted incidence block must be close, in the full operator norm on \(\ell^2(\mathsf H)\), to its mean, a prescribed spread Bott symbol: a finite Heisenberg box reduces the full norm to a finite matrix, and a high centered moment, counted with the girth of the base graph, controls that matrix. The failure probabilities are summable over all heights [OpenAI-BCI, Sections 5.2 and 5.5-5.8, Proposition 5.2, Lemmas 5.5-5.9].

- The weighted incidence blocks (Section 1).
- Polynomial avoidance (Section 2).
- Finite tests for the regular norm (Section 3).
- Support rank and centered moments (Section 4).
- The simultaneous choice (Section 5).

The setting of [Thetas and the pruned old graph](thetas-and-the-pruned-old-graph.md) is in force: the pruned graph \(X_{\rm old}\) with its properties (Proposition 5.1 there), \(m_i=H_i/\log q\), \(a=b/\log q\le10^{-6}\). We use Lemma 2.1 of [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md) (coordinates of a word) and the count of walks without singleton edges, Lemma 3.1 of [Girth and centered moments](course:kadison-kaplansky-projections/girth-and-centered-moments#3-walks-without-singleton-edges).

## 1. The weighted incidence blocks

Fix a finite set of incidence types. Before deletion, a type between \(\mathscr A_i\) and \(\mathscr B_k\), \(|i-k|\le1\), is biregular with degrees \(d_{\tau,ik},D_{\tau,ik}\); put \(q_{\tau,ik}=(d_{\tau,ik}D_{\tau,ik})^{1/2}\), and let \(U_{\tau,ik}:\ell^2(\mathscr B_k)\to\ell^2(\mathscr A_i)\) be its incidence matrix restricted to the surviving vertices, divided by \(q_{\tau,ik}\). There are constants \(c_*,C_*\), independent of the height and of large \(s\), with
\[
\begin{gathered}
c_*d\le d_{\tau,ik}\le C_*d,\\
c_*D\le D_{\tau,ik}\le C_*D,\\
c_*q\le q_{\tau,ik}\le C_*q .
\end{gathered}\tag{1.1}
\]
Since \(U_{\tau,ik}\) is a compression of a normalized biregular incidence, \(\|U_{\tau,ik}\|\le1\). The surviving base graph has maximum degree at most \(C_*D\).

**Conventions.** The right regular representation is \(\rho(h)\delta_f=\delta_{fh^{-1}}\); the unitary \(\mathcal I\delta_g=\delta_{g^{-1}}\) carries \(\lambda(h)\) to \(\rho(h)\), so all statements hold in either representation. A positive old edge \(e\) runs from \(A_v\) to \(B_w\), and its voltage \(h_e\in\mathsf H\) lifts it to the edges \((v,f)\to(w,fh_e)\) of the covering graph; the reverse edge carries \(h_e^{-1}\). An edge \(e\) also carries a matrix weight \(W_e\in M_\ell(\mathbb C)\), and its reverse the weight \(W_e^*\). The *normalized weighted block* of a type is
\[
\mathcal V_{\tau,ik}=q^{-1}\sum_eE_{v_ew_e}\otimes W_e\otimes\rho(h_e),
\]
the sum over the surviving edges of the type between \(\mathscr A_i\) and \(\mathscr B_k\), as an operator from \(\ell^2(\mathscr B_k)\otimes\mathbb C^\ell\otimes\ell^2(\mathsf H)\) to the corresponding space over \(\mathscr A_i\). With the forward voltage convention, \(\rho(h_e)\delta_f=\delta_{fh_e^{-1}}\) sends the lift \((w,f)\) to \((v,fh_e^{-1})\), its neighbor across \(e\). The common denominator \(q\) is used for all types.

**Proposition 1.1** (simultaneously sampled symbols; [OpenAI-BCI, Proposition 5.2]). Fix \(b\), a matrix size \(\ell\), an accuracy \(\eta>0\), and a finite list of profiles with height selections as in Section 3 of [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md), including cutoffs, parity selections, the initial height and finite meshes of the rescaling and rotation paths; allot an incidence type to each required same-height or adjacent-height symbol \(S_{\tau,ik}=T_if_{\tau,ik}T_k^*\). For large \(s\) and then large initial height, the surviving base graph admits voltages on all edges and weights from one finite set such that:

1. the covering graph has no nonempty cyclically reduced closed walk of length at most \(6.03m_i\) based at an old vertex of height \(i\);
2. at every height and for every type,
\[
\|\mathcal V_{\tau,ik}-U_{\tau,ik}\otimes S_{\tau,ik}\|\le\eta ,
\]
in the full operator norm, where the tensor product means that every scalar incidence entry multiplies the same matrix convolution operator;
3. the weights come from one finite set independent of the height; appending its index to the labels keeps the uniqueness properties of the labelled graph, and the refined alphabet \(\mathcal A\) satisfies
\[
\begin{aligned}
\log_2|\mathcal A|&\le1.00005s+O(\log s)\\
&\quad+O(1)<\log_2(q^2)
\end{aligned}
\]
for large \(s\), the \(O(1)\) depending on \(b\), \(\eta\) and the profiles. Edges of weight zero remain edges of the covering graph.

The proof occupies the rest of this lesson.

## 2. Polynomial avoidance

**Lemma 2.1** (zeros at random points with small atoms). Let \(X_1,\ldots,X_r\) be independent real random variables, each with all atoms of probability at most \(\kappa\), and let \(P\) be a nonzero real polynomial of total degree at most \(d'\). Then \(\mathbb P(P(X_1,\ldots,X_r)=0)\le d'\kappa\).

*Proof.* Induct on the number of variables that occur in \(P\); variables not occurring are discarded, and a nonzero constant never vanishes. Write \(P=\sum_{m\le e}P_m(X_1,\ldots,X_{r-1})X_r^m\) with \(P_e\ne0\), of degree at most \(d'-e\). By induction \(P_e\) vanishes with probability at most \((d'-e)\kappa\). Conditionally on the other variables with \(P_e\ne0\), \(P\) is a nonzero polynomial of degree \(e\) in \(X_r\), with at most \(e\) roots, each taken with probability at most \(\kappa\). \(\square\)

This is a version, with small atoms in place of uniform laws, of the polynomial zero bound proved as Lemma 1.1 of [Girth and centered moments](course:kadison-kaplansky-projections/girth-and-centered-moments#1-zeros-of-polynomials-at-random-points) for uniform variables on finite sets.

**Lemma 2.2** (polynomial avoidance; [OpenAI-BCI, Lemma 5.5]). Draw independent pairs \((W_e,h_e)\) for the unoriented edges, from the laws of Lemma 4.1 of [The Fourier envelope and the product sampler](the-fourier-envelope-and-the-product-sampler.md). For a fixed closed base walk whose word in the edge variables is not an \(\mathsf H\)-law, the probability that its holonomy (the ordered product of the voltages along it, with inverses on reverse traversals) is the identity is at most
\[
C_b\,2^{-50H_{\min}},
\]
where \(H_{\min}\) is the least scale of an edge of the walk. The weights play no role, including zero weights.

*Proof.* Write \(h_e=(n_e,l_e,c_e)\) in normal form. By Lemma 2.1 of the lesson on the Heisenberg group, the horizontal coordinates of the holonomy are \(\sum_ea_en_e\) and \(\sum_ea_el_e\), with the signed occurrence counts \(a_e\). If some \(a_e\ne0\), one of these linear polynomials is nonzero. If all \(a_e\) vanish, the central coordinate is a polynomial \(Q\) of degree at most two in the \(n_e,l_e\), not involving the \(c_e\), and \(Q\ne0\) because the word is not a law. In both cases a nonzero polynomial of degree at most two in the independent variables \(n_e,l_e\) must vanish. Their atoms are \(O_b(J/N)=O_b(2^{-150H})\) and \(O_b(J^{-1})=O_b(2^{-50H})\) at an edge of scale \(H\), by (4.1) of the previous lesson. Lemma 2.1 gives the bound. No conditioning on central coordinates or weights occurs. \(\square\)

## 3. Finite tests for the regular norm

**Lemma 3.1** (Heisenberg boxes and the regular norm; [OpenAI-BCI, Lemma 5.6]). Let \(a_0,B>0\) be fixed. For \(H\ge1\) there is a finite set \(\mathcal B_H\subset\mathsf H\) with \(|\mathcal B_H|\le2^{K_0H}\), \(K_0\) depending only on \(a_0,B\), such that
\[
\begin{gathered}
\frac{|\mathcal B_H\,\triangle\,v\mathcal B_H|}{|\mathcal B_H|}\le C2^{-BH}\quad\text{and}\\
\frac{|\mathcal B_H\,\triangle\,\mathcal B_Hv|}{|\mathcal B_H|}\le C2^{-BH}
\end{gathered}
\]
for every \(v\) whose coordinates and those of \(v^{-1}\) are bounded by \(2^{a_0H}\). Let \(A\) be a self-adjoint finite matrix, with any fixed matrix amplification, whose entries are finite sums \(\sum_gc_g\lambda(g)\) supported on such elements, and let \(R\) bound the sums of the norms of the coefficients in each row and each column. If \(Q_H\) is the multiplication by the indicator of \(\mathcal B_H\) on \(\ell^2(\mathsf H)\), then
\[
\begin{gathered}
\|Q_HAQ_H\|\le\|A\|\\
\le\|Q_HAQ_H\|+C2^{-BH}R .
\end{gathered}\tag{3.1}
\]
The same holds for rectangular matrices after self-adjoint doubling.

*Proof.* Let \(\mathcal B(T)=\{x^ny^lz^c:|n|,|l|\le T,\ |c|\le T^2\}\). If \(v\) has coordinates bounded by \(R_0\le T\), multiplying by \(v\) on either side changes the horizontal coordinates by at most \(R_0\) and the central one by at most \(R_0+R_0T\), by the multiplication law (1.2) of the lesson on the Heisenberg group. Points outside boundary strips of these widths stay in the box, so the symmetric differences are at most a fraction \(CR_0/T\) (multiplication is a bijection, which accounts for both directions). Take \(T=\lceil2^{(a_0+B+2)H}\rceil\); the box has \((2T+1)^2(2T^2+1)=2^{O(H)}\) elements.

For the norm, let \(Q_t\) be the multiplication by the indicator of \(\mathcal B_Ht\). Right translation commutes with left convolution, so every \(Q_tAQ_t\) has the norm of \(Q_HAQ_H\). For finitely supported \(\xi\), \(\sum_t\|Q_t\xi\|^2=|\mathcal B_H|\|\xi\|^2\). The average \(|\mathcal B_H|^{-1}\sum_t\langle AQ_t\xi,Q_t\xi\rangle\) is the quadratic form of the operator \(\tilde A\) obtained from \(A\) by multiplying each coefficient \(c_g\) by \(|\mathcal B_H\cap g^{-1}\mathcal B_H|/|\mathcal B_H|\), a number within \(C2^{-BH}\) of \(1\); its absolute value is at most \(\|Q_HAQ_H\|\|\xi\|^2\), so \(\|\tilde A\|\le\|Q_HAQ_H\|\). By the Schur test applied to the norms of the coefficient differences, \(\|A-\tilde A\|\le C2^{-BH}R\). Nothing here separates the coordinates of the matrix amplification. \(\square\)

## 4. Support rank and centered moments

**Lemma 4.1** (length versus cycle rank; [OpenAI-BCI, Lemma 5.7]). Let \(S\) be a finite connected graph with at most \(Kg\) edges and girth greater than \(g\). Then
\[
\dim H_1(S;\mathbb Q)\le\max\{1,\lceil20K\rceil\}^2 .
\]

*Proof.* Regard \(S\) as a metric graph with unit edges, put \(a'=g/10\), and choose a maximal \(a'\)-separated set \(P\) of points of \(S\) in the path metric; it is an \(a'\)-net. If \(|P|\ge2\), the open balls of radius \(a'/2\) around its points are disjoint, and each contains a path interval of length \(a'/2\) towards another net point, so \(|P|a'/2\le Kg\) and \(|P|\le\lceil20K\rceil\). Join two net points at distance at most \(3a'\) by an edge of an abstract graph \(L\), mapped to a shortest path of \(S\). This map is onto on first homology: subdivide a closed path of \(S\) into pieces of length at most \(a'\), choose net points within \(a'\) of the subdivision points, and replace each piece with its two connectors by the corresponding edge of \(L\); the difference is a closed path of length at most \(6a'<g\), which is null-homotopic, since cancelling backtracks in a nontrivial closed path leaves a simple cycle of at most the same length. So \(\dim H_1(S)\le\dim H_1(L)\le|E(L)|\), and \(|E(L)|\le|P|^2\). \(\square\)

**Lemma 4.2** (centered block concentration; [OpenAI-BCI, Lemma 5.9]). Fix a type and one of its blocks \((i,k)\), and assign independent samples of Lemma 4.1 of the previous lesson to its unoriented edges. Let
\[
\begin{aligned}
X_{ik}=\sum_eE_{v_ew_e}\otimes\bigl(&W_e\rho(h_e)\\
&-\mathbb E[W_e\rho(h_e)]\bigr)
\end{aligned}
\]
be the unnormalized centered block. For every \(\eta>0\), with the constants chosen in the order below,
\[
\begin{gathered}
\mathbb P\bigl\{\|X_{ik}\|>\eta\,q_{\tau,ik}\bigr\}\\
\le2^{-6H_i},
\end{gathered}\tag{4.1}
\]
uniformly in the height, under the independent law and without conditioning on any girth event.

*Proof.* An edge entry has norm at most \(2M_\eta\). Doubling the block off the diagonal makes it self-adjoint, with row and column coefficient sums at most \(C_*M_\eta D\). Require \(H_0\ge s\); then \(D\le2^{0.60005H_i}\) and \(|\mathscr A_i|\le2^{1.2H_i}\), and after raising \(H_0\) to absorb constants, the coefficient sums are at most \(2^{2H_i}\) and the number of base and matrix indices at most \(2^{3H_i}\). By Lemma 4.1 of the previous lesson all voltages and their inverses have coordinates at most \(2^{a_0H_i}\). Apply Lemma 3.1 with an exponent \(B>4\): the error \(C2^{-BH_i}2^{2H_i}\) tends to zero exponentially, and the compression \(\widehat X\) of the doubled block to the box has total dimension at most \(2^{K_1H_i}\) with a fixed \(K_1\). Raise \(H_0\) so that the box error is at most \(\eta q_{\tau,ik}/2\); this does not change \(K_1\).

Fix \(C>2(K_1+6)\) and put \(h=\lceil CH_i/\log_2d\rceil\). A walk of length \(2h\) without singleton edges uses at most \(h\) base edges, all in the two fixed layers of the block, whose base girth is at least \(0.9H_i/\log_2q\) by Proposition 5.1(2) of the lesson on thetas and the pruned old graph (adjacent scales differ by \(b\)). Since \(\log_2q/\log_2d<1.25\), the support has at most \(2C\) times the girth in edges, and Lemma 4.1 bounds its cycle rank by a number \(R_C\) depending only on \(C\).

Expand \(\mathbb E\operatorname{Tr}(\widehat X^{2h})\) over closed walks of base vertices and edges. A term with an edge occurring exactly once has expectation zero: conditionally on the other edges it is a fixed left factor, one centered entry or its adjoint, and a fixed right factor, and compression does not affect this. Every other term has trace at most the dimension times \((2M_\eta)^{2h}\). By Lemma 3.1 of [Girth and centered moments](course:kadison-kaplansky-projections/girth-and-centered-moments#3-walks-without-singleton-edges), with \(\Delta\le C_*D\) and cycle rank at most \(R_C\),
\[
\mathbb E\operatorname{Tr}(\widehat X^{2h})\le2^{K_1H_i}(C_1D)^h ,
\]
with \(C_1\) fixed after \(C\) and the coefficient data, before \(s\). For self-adjoint \(\widehat X\), \(\|\widehat X\|^{2h}\le\operatorname{Tr}(\widehat X^{2h})\). Markov's inequality and (1.1) give
\[
\mathbb P\bigl\{\|X_{ik}\|>\eta q_{\tau,ik}\bigr\}\le2^{K_1H_i}\Bigl(\frac{C_2}{\eta^2d}\Bigr)^h .
\]
Choose \(s\) so large that \(C_2/\eta^2\le d^{1/2}\); then the bound is at most \(2^{(K_1-C/2)H_i}\le2^{-6H_i}\). The dependence of \(C_2\) on \(C\) is harmless, since \(s\) is chosen after both. \(\square\)

## 5. The simultaneous choice

*Proof of Proposition 1.1.* For a block put \(a_{\tau,ik}=q/q_{\tau,ik}\), a number in a fixed compact subinterval of \((0,\infty)\) by (1.1). Apply Lemma 4.1 of the previous lesson to the symbol \(a_{\tau,ik}S_{\tau,ik}\), with smaller tolerances; multiplying the profile family by bounded scalars keeps all estimates uniform. Within a block, draw the same law at every edge, independently over all unoriented edges. The mean of the block is
\[
\frac{q_{\tau,ik}}q\,U_{\tau,ik}\otimes\mathbb E[W_e\rho(h_e)] ,
\]
whose distance from \(U_{\tau,ik}\otimes S_{\tau,ik}\) is a fixed constant times the allotted one-norm error, since \(\|U_{\tau,ik}\|\le1\) and \(\|\cdot\|\le\|\cdot\|_1\). Lemma 4.2, with its tolerance reduced by the factor \(C_*\ge q_{\tau,ik}/q\), controls the fluctuation \(q^{-1}X_{ik}\). The common denominator \(q\) avoids recovering an unbounded height from a label.

*Girth.* A nonempty cyclically reduced closed walk in the covering graph projects to a cyclically nonbacktracking closed walk of the base with trivial holonomy. Test all such base walks of length at most \(\lceil6.03m_i\rceil\) from height \(i\); for large \(m_i\) this is less than \(6.04m_i\), so by Proposition 5.1(4) of the lesson on thetas each is a non-law. Along such a walk \(H_{\min}\ge H_i-b\lceil6.03m_i\rceil\ge(1-7a)H_i\), and Lemma 2.2 bounds the probability of trivial holonomy by \(2^{-40H_i}\) for \(a\le10^{-6}\) and large \(H_0\). The number of rooted walks is at most
\[
(|\mathscr A_i|+|\mathscr B_i|)\sum_{m\le\lceil6.03m_i\rceil}(C_*D)^m\le2^{9H_i}
\]
for large \(s\) and \(H_0/s\), because \(1+6.03\cdot0.60005/0.50005<8.24\). So the girth failure at height \(i\) has probability at most \(2^{-31H_i}\). Every edge counts, including edges of weight zero. Triviality of the holonomy does not depend on the starting point in the fiber, so no union over the infinite fiber is needed.

*All heights.* There are finitely many blocks at each height, and \(H_i=H_0+bi\), so the sum over all heights of the norm failures (4.1) and the girth failures is less than one for large \(H_0\). To obtain one assignment without an infinite product measure: enumerate all the block inequalities and walk tests; each involves finitely many edges, and by the summed bound any finite list of them has a satisfying assignment. Each edge has finitely many possible pairs (voltage, weight). Choosing successively subsequences of satisfying assignments that stabilize at the first edge, the second, and so on, the diagonal assignment satisfies every condition, since each involves finitely many edges.

*The alphabet.* Append to every positive label the index of its weight in the finite set, the reverse label carrying the adjoint weight. Equal refined words have equal original words, so uniqueness persists. The original label count is \(d2^r=2^{1.00005s}\) times factors \(O(\log s)\) and \(O(1)\) in the logarithm; the types, the weight set and the extras contribute factors independent of the height, and \(\log_2(q^2)=1.0001s\). Large voltage coordinates are edge data, not letters. \(\square\)

The proof gives more precisely \(\sqrt{|\mathcal A|}/q\le2^{-0.000025s+O(\log s)+O(1)}\), the margin used for the residual forest in the lesson [Finite Cayley formulas for prescribed profiles](finite-cayley-formulas-for-prescribed-profiles.md).

## 6. Exercises

**Exercise 6.1.** Show that Lemma 2.1 is sharp for \(d'=1\): give a variable with an atom of mass \(\kappa\) and a linear polynomial vanishing with probability \(\kappa\).

**Exercise 6.2.** In Lemma 3.1, why are the boxes chosen with central range \(T^2\) rather than \(T\)?

**Exercise 6.3.** Check the exponent \(1+6.03\cdot0.60005/0.50005\).

**Exercise 6.4.** In Lemma 4.2, why is the girth of the *base* graph used, and not the girth of the covering graph?

## 7. Solutions

**6.1.** Let \(X\) take the value \(0\) with probability \(\kappa\); then \(P(X)=X\) vanishes with probability \(\kappa\).

**6.2.** Multiplying \(x^ny^lz^c\) by an element with coordinates up to \(R_0\) changes \(c\) by up to \(R_0+R_0|l|\), and \(|l|\) ranges up to \(T\). With central range \(T^2\), the relative width of the boundary strip in \(c\) is \(O(R_0T/T^2)=O(R_0/T)\), as in the horizontal directions; with range \(T\) it would not be small.

**6.3.** \(0.60005/0.50005=1.19998\ldots\), times \(6.03\) gives \(7.2359\ldots\), plus \(1\) gives \(8.2359\ldots<8.24\).

**6.4.** The moment bound counts walks in the base graph whose edges each occur at least twice; their supports are subgraphs of the base graph, and their cycle rank is controlled by its girth, which the pruning provides independently of the voltages. The girth of the covering graph is only established by the same random choice, so using it would condition the law.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 5.2 and 5.5-5.8, Proposition 5.2, Lemmas 5.5-5.9. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
