# Uniform smoothing of matching averages

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Partition the vertices of a complete graph into a fixed number \(\ell\) of cells and average a function of perfect matchings over the matchings with a prescribed number of edges inside each cell and between each pair of cells. This lesson proves that such averages are smooth in a strong sense: up to an error \(N^{-K}\) in the operator norm, they only see the part of the function spanned by products of a bounded number of edge indicators, uniformly in the cell sizes and in the prescribed counts, even when the prescribed table is very rare [OpenAI-PSD, Appendix A]. The low-degree part, in turn, is averaged by a single polynomial in the counts between the cells. The theorem is independent of the lower bound proved in [The lower bound for perfect matching](the-lower-bound-for-perfect-matching.md); it uses the same mechanism as [Averaging within a cell](averaging-within-a-cell.md), a bound on a fourth moment combined with a lower bound for the dimensions of the invariant subspaces.

- Tables and averaging operators (Section 1).
- Counting partitions, and the kernel (Section 2).
- The fourth moment (Section 3).
- Dimensions outside the edge-product span (Section 4).
- Proof of the theorem, and the polynomial (Section 5).

The representation theory of the symmetric group is used as proved in [The symmetric groups I: Young tableaux and Young symmetrizers](course:RT-FIN/young-tableaux-and-young-symmetrizers) and [The symmetric groups II: branching, Jucys–Murphy elements and Young's seminormal form](course:RT-FIN/branching-jucys-murphy-elements-and-youngs-seminormal-form).

## 1. Tables and averaging operators

Fix an integer \(\ell\ge1\). For even \(N\), let \(V\) be a fixed set of \(N\) vertices, let \(\mathcal X\) be the set of perfect matchings of the complete graph on \(V\), and let \(\mathcal Z\) be the set of ordered partitions \(Z=(Z_1,\ldots,Z_\ell)\) of \(V\) into cells of prescribed positive sizes \(s_1,\ldots,s_\ell\), with \(\sum_us_u=N\). Both sets carry the uniform probability measure. The *table* of a matching \(M\) at a partition \(Z\) consists of the numbers \(t_{uu}\) of edges of \(M\) inside \(Z_u\) and the numbers \(t_{uv}=t_{vu}\) of edges between \(Z_u\) and \(Z_v\), \(u\ne v\). A table \(t\) is *admissible* if its entries are nonnegative integers with
\[
\begin{gathered}2t_{uu}+\sum_{v\ne u}t_{uv}=s_u\\ (1\le u\le\ell).\end{gathered}\tag{1.1}
\]
Every table of a matching is admissible, since each vertex of \(Z_u\) lies in one edge. Conversely every admissible table occurs: in each cell \(Z_u\) reserve \(t_{uv}\) vertices for each \(v\ne u\), join the reserved vertices of \(Z_u\) and \(Z_v\) in pairs, and match the remaining \(2t_{uu}\) vertices of \(Z_u\) among themselves.

For an admissible table \(t\), define \(T_t\colon L^2(\mathcal X)\to L^2(\mathcal Z)\) by letting \((T_tf)(Z)\) be the average of \(f(M)\) over the matchings \(M\) with table \(t\) at \(Z\).
For an edge \(e\) let \(x_e(M)=\mathbf 1_{\{e\in M\}}\). Let \(\mathcal P_d\) be the span of the products of at most \(d\) edge indicators, including the constant \(1\), and \(\Pi_d\) the orthogonal projection of \(L^2(\mathcal X)\) onto \(\mathcal P_d\).

**Theorem 1.1** (uniform smoothing; [OpenAI-PSD, Theorem A.1]). For every \(\ell\ge1\) and \(K>0\) there are an integer \(d\ge1\) and \(N_0\) such that, for every even \(N\ge N_0\), all positive cell sizes summing to \(N\), and every admissible table \(t\),
\[
\|T_t(I-\Pi_d)\|_{\mathrm{op}}\le N^{-K}.
\tag{1.2}
\]
Moreover, for each fixed partition \(Z\) and function \(f\), the values \((T_t\Pi_df)(Z)\), as \(t\) runs over the admissible tables, are the values of one polynomial of total degree at most \(d\) in the counts \((t_{uv})_{u<v}\) between the cells.

The norm in (1.2) is the operator norm from \(L^2(\mathcal X)\) to \(L^2(\mathcal Z)\), so the error is measured on average over a uniform partition.

## 2. Counting partitions, and the kernel

Write \(h=N/2\) for the number of edges of a perfect matching.

**Lemma 2.1.** Let \(t\) be admissible.

1. For a fixed matching \(M\), the number of partitions \(Z\in\mathcal Z\) at which \(M\) has table \(t\) is
\[
\begin{gathered}D_t=\frac{h!}{\prod_{u\le v}t_{uv}!}\,2^{\sum_{u<v}t_{uv}},\\ \text{while }|\mathcal Z|=\frac{N!}{\prod_us_u!}.\end{gathered}
\]
2. Put \(p_t=D_t/|\mathcal Z|\). For a fixed \(M\), a uniform \(Z\) gives \(M\) the table \(t\) with probability \(p_t\); for a fixed \(Z\), a uniform \(M\) has table \(t\) at \(Z\) with probability \(p_t\).
3. \(T_t\) has the kernel \(\mathbf 1_{\{M\text{ has table }t\text{ at }Z\}}/p_t\): \((T_tf)(Z)=\mathbb E_M\bigl[\mathbf 1_{\{\cdots\}}f(M)\bigr]/p_t\).
4. The operator \(\mathcal A=T_t^*T_t\) on \(L^2(\mathcal X)\) is \((\mathcal Ag)(M)=\mathbb E_{M'}\kappa(M,M')g(M')\) with the symmetric kernel
\[
\kappa(M,M')=\frac{|\mathcal Z|}{D_t^2}\,J(M,M'),
\]
where \(J(M,M')\) is the number of partitions at which both \(M\) and \(M'\) have table \(t\). Moreover \(\operatorname{tr}(\mathcal A^2)=\mathbb E_{M,M'}\kappa(M,M')^2\) for independent uniform \(M,M'\).

*Proof.* (1) A partition with the required table is determined by assigning to each of the \(h\) edges of \(M\) a type \(\{u,v\}\), \(u\le v\), with \(t_{uv}\) edges of each type, in \(h!/\prod t_{uv}!\) ways, and by choosing, for each edge joining two different cells, which endpoint goes into which cell, in \(2^{\sum_{u<v}t_{uv}}\) ways. Condition (1.1) makes the cell sizes right. The formula for \(|\mathcal Z|\) is the multinomial coefficient.

(2) The first statement is part 1. Count the pairs \((M,Z)\) such that \(M\) has table \(t\) at \(Z\): this is \(|\mathcal X|D_t\). The permutations of \(V\) act transitively on \(\mathcal Z\) and preserve tables, so every \(Z\) belongs to the same number of these pairs, namely \(|\mathcal X|D_t/|\mathcal Z|=|\mathcal X|p_t\).

(3) By part 2, the average over the matchings with table \(t\) at \(Z\) is \(\mathbb E_M[\mathbf 1f]/p_t\).

(4) For functions \(f,g\) on \(\mathcal X\), part 3 gives
\[
\begin{aligned}\langle T_tf,T_tg\rangle&=\mathbb E_{M,M'}f(M)g(M')\\&\quad\cdot\frac{J(M,M')}{|\mathcal Z|\,p_t^2},\end{aligned}
\]
since a uniform \(Z\) gives both matchings the table \(t\) with probability \(J(M,M')/|\mathcal Z|\); this gives the kernel. As a matrix on the functions on \(\mathcal X\), \(\mathcal A\) has the entries \(\kappa(M,M')/|\mathcal X|\), and since \(\kappa\) is symmetric, \(\operatorname{tr}(\mathcal A^2)=|\mathcal X|^{-2}\sum_{M,M'}\kappa(M,M')^2\). \(\square\)

## 3. The fourth moment

For a probability vector or array \(q\), let \(\mathrm H(q)=-\sum_jq_j\log q_j\), with \(0\log0=0\). Put \(\pi_u=s_u/N\), \(\gamma_{uu}=2t_{uu}/N\) and \(\gamma_{uv}=t_{uv}/N\) for \(u\ne v\). The \(\ell\times\ell\) array \(\gamma\) is symmetric, has total sum one, and has row sums \(\pi_u\) by (1.1). Let
\[
a_\ell=\ell(\ell+1)+1,\qquad b_\ell=2a_\ell+\ell^2 .
\]

**Lemma 3.1.** Put \(R_0=0\) and \(R_j=\log j!-j\log j+j\) for \(j\ge1\). Then \(0\le R_j\le1+\log(j+1)\), and
\[
\begin{gathered}\log\frac{D_t^2}{|\mathcal Z|}\\=N\bigl(\mathrm H(\gamma)-\mathrm H(\pi)\bigr)+\Delta,\\ \Delta\ge-a_\ell(1+\log(N+1)).\end{gathered}\tag{3.1}
\]

*Proof.* For \(j\ge1\), comparing \(\log j!=\sum_{i\le j}\log i\) with integrals gives
\[
\begin{aligned}j\log j-j+1&=\int_1^j\log x\,dx\le\log j!\\&\le\int_1^{j+1}\log x\,dx ,\end{aligned}
\]
so \(R_j\ge1\) and
\[
\begin{aligned}R_j&\le(j+1)\log(j+1)-j\log j\\&=j\log(1+1/j)+\log(j+1)\\&\le1+\log(j+1).\end{aligned}
\]
 Insert \(\log j!=j\log j-j+R_j\) into \(2\log D_t-\log|\mathcal Z|\). The linear terms cancel, because \(\sum_{u\le v}t_{uv}=h\), \(2h=N\) and \(\sum_us_u=N\). The remainders give
\[
\Delta=2R_h-2\sum_{u\le v}R_{t_{uv}}-R_N+\sum_uR_{s_u}.
\]
The remaining terms are
\[
\begin{aligned}&2h\log h-2\sum_{u\le v}t_{uv}\log t_{uv}\\&\quad+2\log2\sum_{u<v}t_{uv}\\&\quad-N\log N+\sum_us_u\log s_u .\end{aligned}
\]
On the other hand, splitting each unordered pair \(u<v\) into the two ordered pairs \((u,v),(v,u)\),
\[
\begin{aligned}N\mathrm H(\gamma)&=-2\sum_{u\le v}t_{uv}\log t_{uv}\\&\quad-2\log2\sum_ut_{uu}+2h\log N,\\ N\mathrm H(\pi)&=-\sum_us_u\log s_u+N\log N .\end{aligned}
\]
The difference of the remaining terms and \(N(\mathrm H(\gamma)-\mathrm H(\pi))\) is \(2h\log h+2h\log2-2h\log N\), which equals \(2h\log(2h/N)=0\). Finally, \(R_h,R_{s_u}\ge0\), each \(t_{uv}\le N\), and there are \(\ell(\ell+1)/2\) pairs \(u\le v\), so \(\Delta\ge-(\ell(\ell+1)+1)(1+\log(N+1))\). \(\square\)

The union \(M\cup M'\) of two perfect matchings, with a common edge counted twice, is a disjoint union of cycles that alternate between edges of \(M\) and of \(M'\); a common edge forms a cycle of length two. Let \(c(M,M')\) be the number of these cycles.

**Lemma 3.2.** For all \(M,M'\in\mathcal X\),
\[
\kappa(M,M')\le e^{a_\ell}(N+1)^{a_\ell}\,\ell^{c(M,M')} .
\]

*Proof.* The matrix \(W_{uv}=\gamma_{uv}/\pi_u\) has nonnegative entries and row sums one. Orient each cycle of \(M\cup M'\); then every vertex is the tail of exactly one oriented edge. Give a coloring \(\chi\colon V\to[\ell]\) the weight
\[
\omega(\chi)=\prod_{\text{oriented edges }x\to x'}W_{\chi(x)\chi(x')} .
\]
For a cycle of length \(m\), the sum of the weights of the colorings of its vertices is \(\operatorname{tr}(W^m)\le\ell\), because \(W^m\) also has row sums one. So the sum of \(\omega(\chi)\) over all colorings is at most \(\ell^{c(M,M')}\).

A partition \(Z\) is a coloring with color classes of sizes \(s_u\). If both \(M\) and \(M'\) have table \(t\) at \(Z\), then the denominators of \(\omega\) give \(\prod_u\pi_u^{s_u}\), since each vertex is a tail once, and the two matchings together have \(2t_{uv}\) edges of each type \(\{u,v\}\), each contributing \(\gamma_{uv}=\gamma_{vu}\) whatever its orientation. Hence
\[
\omega(Z)=\frac{\prod_{u\le v}\gamma_{uv}^{2t_{uv}}}{\prod_u\pi_u^{s_u}}=e^{-N(\mathrm H(\gamma)-\mathrm H(\pi))},
\]
using \(N\mathrm H(\gamma)=-\sum_{u\le v}2t_{uv}\log\gamma_{uv}\) and \(N\mathrm H(\pi)=-\sum_us_u\log\pi_u\); a type with \(t_{uv}=0\) contributes no factor. So \(J(M,M')e^{-N(\mathrm H(\gamma)-\mathrm H(\pi))}\le\ell^{c(M,M')}\), and with Lemma 2.1(4) and (3.1),
\[
\begin{aligned}&\kappa(M,M')\le\ell^{c(M,M')}e^{-\Delta}\\&\quad\le\ell^{c(M,M')}e^{a_\ell(1+\log(N+1))}. \qquad\square\end{aligned}
\]

**Lemma 3.3.** For every \(M\in\mathcal X\), \(\mathbb E_{M'}\,\ell^{2c(M,M')}\le(h+1)^{\ell^2}\).

*Proof.* Put \(q=\ell^2\). The number \(q^{c(M,M')}\) counts the colorings of \(V\) with \(q\) colors that are constant on every edge of \(M\) and of \(M'\), that is, on every cycle. A coloring constant on the edges of \(M\) amounts to a coloring of the \(h\) edges of \(M\); if the colors occur \(j_1,\ldots,j_q\) times, there are \(h!/\prod_ij_i!\) such colorings, and their color classes of vertices have \(2j_1,\ldots,2j_q\) elements. A uniform \(M'\) has all its edges inside these classes with probability \(\prod_i(2j_i-1)!!/(2h-1)!!\), where \((-1)!!=1\). With \((2j-1)!!=(2j)!/(2^jj!)\),
\[
\frac{h!}{\prod_ij_i!}\cdot\frac{\prod_i(2j_i-1)!!}{(2h-1)!!}=\frac{\prod_i\binom{2j_i}{j_i}}{\binom{2h}h}\le1 :
\]
partition a set of \(2h\) elements into blocks of sizes \(2j_i\); the numerator counts only the \(h\)-element subsets that take \(j_i\) elements from each block. There are at most \((h+1)^q\) vectors \((j_1,\ldots,j_q)\), which proves the bound. \(\square\)

**Proposition 3.4** (the fourth moment; [OpenAI-PSD, Lemma A.2]). For every admissible table,
\[
\operatorname{tr}\bigl((T_t^*T_t)^2\bigr)\le e^{2a_\ell}(N+1)^{b_\ell}.
\]

*Proof.* By Lemma 2.1(4), Lemma 3.2 and Lemma 3.3,
\[
\begin{aligned}\operatorname{tr}(\mathcal A^2)&=\mathbb E_{M,M'}\kappa^2\\&\le e^{2a_\ell}(N+1)^{2a_\ell}(h+1)^{\ell^2}\\&\le e^{2a_\ell}(N+1)^{b_\ell}. \qquad\square\end{aligned}
\]

## 4. Dimensions outside the edge-product span

The group \(S_N\) of permutations of \(V\) acts on \(\mathcal X\) and \(\mathcal Z\), and by \((\sigma f)(M)=f(\sigma^{-1}M)\) by orthogonal operators on \(L^2(\mathcal X)\). It maps a product of edge indicators to a product of the same number of edge indicators, so \(\mathcal P_d\) and \(\mathcal P_d^\perp\) are invariant subspaces.

We use from the lessons on the symmetric group: the irreducible complex representations of \(S_m\) are the \(V_\lambda\), one for each partition \(\lambda\) of \(m\) (Theorem 4.3 of [The symmetric groups I](course:RT-FIN/young-tableaux-and-young-symmetrizers)); \(V_{\lambda'}\cong V_\lambda\otimes\operatorname{sgn}\) for the conjugate partition (Proposition 5.2 there); the restriction of \(V_\lambda\) to the subgroup \(S_{m-1}\) fixing \(m\) is the direct sum of the \(V_\mu\) over the diagrams \(\mu\) obtained by removing one corner box of \(\lambda\) (Theorem 4.2 of [The symmetric groups II](course:RT-FIN/branching-jucys-murphy-elements-and-youngs-seminormal-form)); and \(\dim V_\lambda=f^\lambda\), the number of standard tableaux of shape \(\lambda\) (Corollary 4.3 there). For the one-row diagram \((m)\), the column group of a tableau is trivial, so the Young symmetrizer is \(\sum_{g\in S_m}g\), which every \(g\) fixes; hence \(V_{(m)}\) is the trivial representation, and by the conjugation formula \(V_{(1^m)}\) is the sign representation. The branching rule and the dimension formula are also the starting point of the approach of Okounkov and Vershik [Vershik–Okounkov 2005].

**Lemma 4.1.** Let \(A\subseteq V\) have \(d\) elements, and let \(G\cong S_{N-d}\) be the group of permutations of \(V\) that fix every element of \(A\). Every \(G\)-invariant function on \(\mathcal X\) lies in \(\mathcal P_d\).

*Proof.* For \(M\in\mathcal X\), let \(M_A\) be the set of edges of \(M\) with both endpoints in \(A\). Two matchings \(M,M'\) with \(M_A=M'_A\) lie in one \(G\)-orbit: the vertices of \(A\) not covered by \(M_A\) are matched to vertices outside \(A\), in both matchings; a permutation in \(G\) can first send the outside partner in \(M\) of each such vertex to its outside partner in \(M'\), and then map the remaining outside edges of \(M\) onto those of \(M'\). As \(G\) preserves \(M_A\), the orbits are the sets \(\{M:M_A=F\}\) for the partial matchings \(F\) of \(A\). The indicator of such an orbit is
\[
\prod_{e\in F}x_e\prod_{e\subseteq A,\ e\notin F}(1-x_e).
\]
Expanding the product gives products of edge indicators of edges inside \(A\). A product containing two distinct edges with a common vertex vanishes on \(\mathcal X\), and the others involve at most \(d/2\) edges. So every orbit indicator, and hence every \(G\)-invariant function, lies in \(\mathcal P_d\). \(\square\)

**Lemma 4.2** (dimensions; [OpenAI-PSD, Lemma A.3]). Let \(d\ge1\) and \(N\ge4d^2\). Every irreducible subrepresentation of the complexification of \(\mathcal P_d^\perp\) has dimension at least
\[
c_dN^{d/2},\qquad c_d=\frac1{2^dd!}.
\]

*Proof.* Label \(V=[N]\) and let \(A=\{N-d+1,\ldots,N\}\), so that the group \(G\) of Lemma 4.1 is \(S_{N-d}\subseteq S_{N-d+1}\subseteq\cdots\subseteq S_N\). Let \(V_\lambda\) be an irreducible subrepresentation of \((\mathcal P_d^\perp)_{\mathbb C}\). Note that \(G\) acts by real operators, so the real and imaginary parts of a vector of \((\mathcal P_d^\perp)_{\mathbb C}\) that transforms by a real character of \(G\) are real functions in \(\mathcal P_d^\perp\) with the same transformation law.

*Long first row.* Suppose \(\lambda_1\ge N-d\). Remove the \(N-\lambda_1\le d\) boxes below the first row one corner at a time, then \(\lambda_1-(N-d)\) boxes of the first row. By the branching rule, applied \(d\) times, the restriction of \(V_\lambda\) to \(G\) contains \(V_{(N-d)}\), the trivial representation: \(V_\lambda\) contains a nonzero \(G\)-fixed vector. Its real or imaginary part is a nonzero real \(G\)-invariant function in \(\mathcal P_d^\perp\), which lies in \(\mathcal P_d\) by Lemma 4.1, a contradiction.

*Long first column.* Suppose \(\lambda'_1\ge N-d\). In the same way, the restriction of \(V_\lambda\) to \(G\) contains the sign representation of \(G\), so there is a nonzero real function \(g\) on \(\mathcal X\) with \(\sigma g=\operatorname{sgn}(\sigma)g\) for \(\sigma\in G\). Since \(N\ge4d^2>2d\), every matching \(M\) has an edge with both endpoints outside \(A\): at most \(d\) of the \(N-d\) outside vertices are matched into \(A\). The transposition \(\tau\in G\) of the endpoints of such an edge fixes \(M\), so \(g(M)=(\tau g)(M)=-g(M)\), and \(g(M)=0\) for every \(M\), a contradiction.

*The other diagrams.* So \(\lambda_1<N-d\) and \(\lambda'_1<N-d\). The diagram lies in a rectangle with \(\lambda'_1\) rows and \(\lambda_1\) columns, so \(\lambda_1\lambda'_1\ge N\). Since \(f^{\lambda'}=f^\lambda\) by the conjugation formula, we may replace \(\lambda\) by \(\lambda'\) and assume \(b=\lambda_1\ge\sqrt N\ge2d\). Below the first row there are \(N-b>d\) boxes; choose a partition \(\nu\) with \(d\) boxes whose diagram lies inside the part of \(\lambda\) below the first row, and let \(\eta\) be the diagram consisting of the first row of \(\lambda\) and \(\nu\) below it. As \(\nu_1\le d\), every box of \(\nu\) lies in one of the first \(d\) columns.

Put \(1,\ldots,d\) into the first \(d\) boxes of the first row. Choose a set \(S\) of \(d\) of the labels \(d+1,\ldots,b+d\), fill the boxes of \(\nu\) with \(S\) in the order of a fixed standard tableau of \(\nu\), and put the other labels increasingly into the rest of the first row. Rows increase; columns increase within \(\nu\), and each box of \(\nu\) lies below a box of the first row with a label at most \(d\). So these are \(\binom bd\) distinct standard tableaux of shape \(\eta\). Each extends to a standard tableau of shape \(\lambda\): add the boxes of \(\lambda\) outside \(\eta\) row by row from the top, each from left to right, with the labels \(b+d+1,\ldots,N\) in this order; every intermediate shape is a diagram, and each new label exceeds the labels above it and to its left. Hence, with \(b-i\ge b/2\) for \(i<d\),
\[
f^\lambda\ge\binom bd\ge\frac{(b/2)^d}{d!}\ge\frac{N^{d/2}}{2^dd!}. \qquad\square
\]

## 5. Proof of the theorem, and the polynomial

*Proof of (1.2).* A permutation \(\sigma\) of \(V\) preserves tables: \(\sigma M\) has table \(t\) at \(\sigma Z\) if \(M\) has it at \(Z\). Hence \(T_t\) intertwines the actions on \(L^2(\mathcal X)\) and \(L^2(\mathcal Z)\), and \(\mathcal A=T_t^*T_t\) commutes with \(S_N\). The projection \(Q=I-\Pi_d\) onto the invariant subspace \(\mathcal P_d^\perp\) commutes with \(S_N\) as well. The compression \(B=Q\mathcal AQ\), as an operator on \(\mathcal P_d^\perp\), is positive semidefinite and commutes with \(S_N\), and
\[
\begin{gathered}\operatorname{tr}(B^2)\le\operatorname{tr}(\mathcal A^2),\\ \|B\|_{\mathrm{op}}=\|T_tQ\|_{\mathrm{op}}^2 .\end{gathered}
\]
The first inequality holds because compression by an orthogonal projection does not increase the Frobenius norm (Lemma 1.1(5) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md)); the second is \(\|X^*X\|=\|X\|^2\) for \(X=T_tQ\).

If \(B\ne0\), the eigenspace of \(B\) for its largest eigenvalue \(\|B\|_{\mathrm{op}}\) is invariant, and its complexification contains an irreducible subrepresentation of \((\mathcal P_d^\perp)_{\mathbb C}\). By Lemma 4.2 this eigenvalue has multiplicity at least \(c_dN^{d/2}\), so with Proposition 3.4
\[
\begin{aligned}c_dN^{d/2}\,\|T_tQ\|_{\mathrm{op}}^4&\le\operatorname{tr}(B^2)\\&\le e^{2a_\ell}(N+1)^{b_\ell},\end{aligned}
\]
an inequality that also holds if \(B=0\). Choose \(d\) with \(d/2>b_\ell+4K\). Then \(e^{2a_\ell}(N+1)^{b_\ell}/(c_dN^{d/2})\le N^{-4K}\) for all large \(N\), uniformly in the cell sizes and the table, and (1.2) follows. \(\square\)

**Lemma 5.1** (containment). Fix a partition \(Z\), and let \(E'\) be a set of pairwise disjoint edges, with \(m_{uv}\) edges of type \(\{u,v\}\) (\(u\le v\)) and \(a_u=2m_{uu}+\sum_{v\ne u}m_{uv}\) endpoints in \(Z_u\). For an admissible table \(t\), the probability that a uniform matching with table \(t\) at \(Z\) contains \(E'\) is
\[
\frac{2^{\sum_um_{uu}}\prod_{u\le v}(t_{uv})_{m_{uv}}}{\prod_u(s_u)_{a_u}},
\tag{5.1}
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\) and \((x)_0=1\).

*Proof.* Let \(M_0\) have table \(t\) at \(Z\). The group \(\prod_uS_{Z_u}\) of permutations preserving every cell acts transitively on the matchings with table \(t\) at \(Z\) (as in Section 1), so \(\sigma M_0\) is uniform among them for a uniform \(\sigma\) in this group. Now \(E'\subseteq\sigma M_0\) means that \(\sigma^{-1}\), restricted to the endpoints of \(E'\), maps each edge of \(E'\) onto an edge of \(M_0\). This restriction is a uniform injection of the \(a_u\) endpoints in \(Z_u\) into \(Z_u\), for every \(u\); there are \(\prod_u(s_u)_{a_u}\) of them, a positive number as \(a_u\le s_u\). The good injections are obtained by assigning to the \(m_{uv}\) edges of type \(\{u,v\}\) distinct edges of \(M_0\) of that type, in \((t_{uv})_{m_{uv}}\) ways, and, for each edge inside a cell, one of its two orientations; an edge between two cells has its orientation forced. If \(t_{uv}<m_{uv}\) for some type, the falling factorial vanishes, as it should. \(\square\)

*Proof of the polynomial statement.* Since \(x_e^2=x_e\), and a product containing two distinct edges with a common vertex vanishes on \(\mathcal X\), the space \(\mathcal P_d\) is spanned by the products \(x_{E'}=\prod_{e\in E'}x_e\) over the sets \(E'\) of at most \(d\) pairwise disjoint edges. For such \(E'\), \((T_tx_{E'})(Z)\) is the probability (5.1). Its numerator is a polynomial of total degree \(|E'|\le d\) in the \(t_{uv}\), and by (1.1) each \(t_{uu}=\frac12(s_u-\sum_{v\ne u}t_{uv})\) is an affine function of the counts between the cells; the denominator is fixed by \(Z\). Write \(\Pi_df=\sum_{E'}c_{E'}x_{E'}\), an expansion that does not depend on \(t\). Then \((T_t\Pi_df)(Z)=\sum_{E'}c_{E'}(T_tx_{E'})(Z)\) is one polynomial of degree at most \(d\) in \((t_{uv})_{u<v}\) for all admissible \(t\). \(\square\)

For three cells, the table is determined by the three counts between the cells.

**Corollary 5.2** (three cells; [OpenAI-PSD, Corollary A.4]). For every \(K>0\) there are an integer \(d\ge1\) and \(N_0\) with the following property. Let \(N\ge N_0\) be even, and let \(a,b,c\) be positive integers with sum \(N\). For a uniform ordered partition into cells of sizes \(a,b,c\), prescribe \(x,y,z\) edges between the first and second, the first and third, and the second and third cells, where \(x,y,z\ge0\) and \(a-x-y\), \(b-x-z\), \(c-y-z\) are nonnegative even integers. Let \(T_{x,y,z}\) average functions on perfect matchings subject to these counts. Then \(\|T_{x,y,z}(I-\Pi_d)\|_{\mathrm{op}}\le N^{-K}\), uniformly in the sizes and the admissible triples, and for every fixed partition and function \(f\), the values \(T_{x,y,z}\Pi_df\) are given by one polynomial of total degree at most \(d\) in \((x,y,z)\).

*Proof.* Apply Theorem 1.1 with \(\ell=3\), \(t_{12}=x\), \(t_{13}=y\), \(t_{23}=z\), and the internal counts \((a-x-y)/2\), \((b-x-z)/2\), \((c-y-z)/2\). \(\square\)

## 6. Exercises

**6.1.** Let \(N=4\), \(\ell=2\), \(s=(2,2)\) and \(M=\{\{1,2\},\{3,4\}\}\). List the admissible tables and check the formula for \(D_t\) in Lemma 2.1 by counting partitions.

**6.2.** Show that a matrix \(W\) with nonnegative entries and row sums one satisfies \(\operatorname{tr}(W^m)\le\ell\) for every \(m\ge1\), where \(\ell\) is its size.

**6.3.** Check (5.1) for \(\ell=1\) and a single edge: a uniform perfect matching of \(N\) vertices contains a given edge with probability \(1/(N-1)\).

**6.4.** Show that for \(N=4\) the space \(\mathcal P_1\) consists of all functions on \(\mathcal X\).

**6.5.** Verify the identity \(\frac{h!}{\prod_ij_i!}\cdot\frac{\prod_i(2j_i-1)!!}{(2h-1)!!}=\prod_i\binom{2j_i}{j_i}\big/\binom{2h}h\) used in Lemma 3.3.

## 7. Solutions

**6.1.** Here \(h=2\) and the tables satisfy \(2t_{11}+t_{12}=2=2t_{22}+t_{12}\): either \(t_{11}=t_{22}=1\), \(t_{12}=0\), or \(t_{11}=t_{22}=0\), \(t_{12}=2\). The formula gives \(D_t=2!/(1!\,1!\,0!)=2\) for the first and \(D_t=2!/(0!\,0!\,2!)\cdot2^2=4\) for the second. Directly: of the \(\binom42=6\) partitions, \(Z_1=\{1,2\}\) and \(Z_1=\{3,4\}\) give the first table, and the four others put one endpoint of each edge into each cell. Indeed \(2+4=6=|\mathcal Z|\).

**6.2.** \(W^m\) has nonnegative entries and row sums one, so its diagonal entries are at most one, and its trace is at most \(\ell\).

**6.3.** Here \(m_{11}=1\), \(a_1=2\), \(s_1=N\) and \(t_{11}=h=N/2\). The formula gives \(2h/(N(N-1))=1/(N-1)\). Directly: the partner of one endpoint is uniform among the other \(N-1\) vertices.

**6.4.** The three perfect matchings of \(K_4\) are \(\{12,34\}\), \(\{13,24\}\) and \(\{14,23\}\). The indicator \(x_{12}\) is the indicator of the first, and similarly for the others, so the three indicator functions of single matchings lie in \(\mathcal P_1\) and span all functions on \(\mathcal X\).

**6.5.** Use \((2j-1)!!=(2j)!/(2^jj!)\) for each \(j_i\) and for \(h\). The powers of two cancel because \(\sum_ij_i=h\), and the left side becomes \(\frac{h!^2\prod_i(2j_i)!}{(2h)!\prod_ij_i!^2}\), which is the right side.

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Appendix A. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
- [Vershik–Okounkov 2005] A. M. Vershik, A. Yu. Okounkov, *A new approach to the representation theory of the symmetric groups. II*, J. Math. Sci. 131 (2005). https://arxiv.org/abs/math/0503040
