# A finite expansion of a restricted CNF

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The first structural step of the proof outlined in [Depth-three circuits and the square-root barrier](depth-three-circuits-and-the-square-root-barrier.md) compares a CNF of large width \(k\) with CNFs of a small width \(b\). After a random restriction, some clauses keep more than \(b\) live variables, and their number is not bounded. This lesson writes the restricted CNF *exactly* as a finite signed combination of terms indexed by *paths*: sequences of clauses that are wide when chosen. The next lesson, [Path weights and backward counting](path-weights-and-backward-counting.md), shows that each term is a positive multiple of an average of width-\(b\) CNFs, and that the total weight has bounded expectation, independently of the number of clauses.

## 1. The restriction bound

Notation is that of the first lesson: \(\mathcal C_b(T)\) is the set of CNFs on \(\{0,1\}^T\) with clauses of width at most \(b\), and \(\operatorname{corr}_b(G)=\max_{J\in\mathcal C_b(T)}|\mathbb E_zG(z)J(z)|\).

**Lemma 1.1 (restriction bound).** Let \(k\geq0\) and \(b\geq1\) be integers, \(H\) a CNF of width at most \(k\) on \([d]\), and \(0<p<1\). Let \((T,\rho)\) be a \(p\)-random restriction, and suppose
\[
\theta=\sum_{\ell=b+1}^{k}\binom k\ell\Bigl(\frac{2p}{1-p}\Bigr)^{\ell}<1
\]
(an empty sum is \(0\)). Then there are numbers \(W(H,T,\rho)\geq0\), depending only on \(H\) and the restriction, with
\[
\mathbb E_{T,\rho}W(H,T,\rho)\leq\frac1{1-\theta},
\]
such that for every function \(G:\{0,1\}^T\to\mathbb R\),
\[
\bigl|\mathbb E_z\,G\,H_{T,\rho}\bigr|\leq W(H,T,\rho)\operatorname{corr}_b(G).
\]

The same numbers \(W\) serve for all \(G\) at once. The number of clauses of \(H\) does not appear anywhere. This lesson proves the exact expansion behind the lemma (Proposition 5.1); the next lesson defines \(W\) and proves both inequalities.

## 2. Easy and hard clauses

Remove from \(H\) all clauses that are always true. List the remaining clauses as \(C_1,\ldots,C_N\), keeping repetitions as separate indices. Let \(E_i\subseteq[d]\) be the scope of \(C_i\); so \(|E_i|\leq k\), and \(C_i\) is violated by exactly one pattern on \(E_i\). The false clause has \(E_i=\varnothing\).

Fix a restriction \((T,\rho)\). For \(z\in\{0,1\}^T\) let \(v_i(z)\in\{0,1\}\) indicate that \(C_i\) is violated at the point given by \(\rho\) outside \(T\) and by \(z\) on \(T\), and put \(q=\sum_iv_i\), the number of violated clauses. Then \(H_{T,\rho}=\mathbf 1[q=0]\). For a set \(U\subseteq T\), call the index \(i\) *easy at* \(U\) if \(|E_i\cap(T\setminus U)|\leq b\), and *hard at* \(U\) otherwise, and put
\[
\begin{gathered}
a_U=\sum_{i\text{ easy at }U}v_i,\\
c_U=\sum_{i:\,E_i\cap(T\setminus U)=\varnothing}v_i .
\end{gathered}
\]
Here \(U\) stands for coordinates whose values will be prescribed: an easy clause has at most \(b\) live variables outside \(U\), and the clauses counted by \(c_U\) have none. The classification depends only on the scopes, not on \(z\), and \(c_U\leq a_U\).

Let \(K=\mathbf 1[a_\varnothing=0]\). It is the conjunction of the clauses easy at \(\varnothing\), with \(\rho\) substituted; each has at most \(b\) live variables, so \(K\in\mathcal C_b(T)\).

Compare \(K\) with \(H_{T,\rho}\). Where \(K=0\), an easy clause is violated, so \(q>0\) and \(H_{T,\rho}=0\). Where \(q=0\), both equal \(1\). The only discrepancy is on the set where \(K=1\) and \(q>0\): there \(K-H_{T,\rho}=1\), and every violated clause is hard at \(\varnothing\), so
\[
1=\sum_{i\text{ hard at }\varnothing}\frac{v_i}q .
\]
The expansion below rewrites this unit, replacing the common denominator \(q\) step by step with counts of easy clauses.

## 3. Paths of wide clauses

A *path* of length \(j\geq1\) is a sequence \(P=(i_1,\ldots,i_j)\) of indices together with sets \(U_0=\varnothing\subseteq U_1\subseteq\cdots\subseteq U_j\subseteq T\) such that
\[
\begin{gathered}
i_h\text{ is hard at }U_{h-1},\\
U_h=U_{h-1}\cup(E_{i_h}\cap T)\qquad(1\leq h\leq j).
\end{gathered}
\]
The sets \(U_h\) are determined by the indices. Write \(\mathcal P_j(T)\) for the set of paths of length \(j\).

**Lemma 3.1.** (a) Each step adds at least \(b+1\) coordinates to \(U\), so every path has length at most \(L=\lfloor|T|/(b+1)\rfloor\). (b) The indices of a path are distinct, and \(i_1,\ldots,i_h\) are easy at \(U_h\) and at every later \(U\). (c) If all the clauses \(C_{i_1},\ldots,C_{i_j}\) are violated at \(z\), then \(a_{U_h}(z)\geq c_{U_h}(z)\geq h\) for \(1\leq h\leq j\).

*Proof.* (a) Since \(i_h\) is hard at \(U_{h-1}\), the set \(E_{i_h}\cap(T\setminus U_{h-1})\) has more than \(b\) elements, and all of them are added. (b) After step \(h\), \(E_{i_h}\cap T\subseteq U_h\), so \(E_{i_h}\cap(T\setminus U)=\varnothing\) for every later \(U\); such an index is easy and cannot be chosen again. (c) The indices \(i_1,\ldots,i_h\) are violated and their scopes miss \(T\setminus U_h\), so they are counted in \(c_{U_h}\). \(\square\)

## 4. Peeling off one step

A *path fraction* is a quotient whose numerator is a product of violation indicators; it is defined to be \(0\) wherever the numerator vanishes. In all fractions below the denominators are positive on the support of the numerator, by Lemma 3.1(c) and because \(q\geq1\) where some clause is violated.

Work at a point with \(K=1\) and \(q>0\). For a path \(P=(i_1,\ldots,i_j)\) put
\[
\begin{aligned}
r_P&=\frac{v_{i_1}\cdots v_{i_j}}{q\;a_{U_1}\cdots a_{U_{j-1}}},\\
t_P&=\frac{v_{i_1}\cdots v_{i_j}}{a_{U_1}\cdots a_{U_j}}.
\end{aligned}
\]
The term \(t_P\) is \(r_P\) with the last factor \(q\) of its denominator replaced by \(a_{U_j}\). For an index \(i\) hard at \(U_j\), write \(Pi\) for the path extended by \(i\).

**Lemma 4.1 (peeling).** For every path \(P\) of length \(j\),
\[
r_P=t_P-\sum_{i\text{ hard at }U_j}r_{Pi}.
\]

*Proof.* Off the support of \(v_{i_1}\cdots v_{i_j}\) all terms vanish. On it, every violated clause is easy or hard at \(U_j\), so \(q=a_{U_j}+\sum_{i\text{ hard at }U_j}v_i\), and
\[
\begin{aligned}
\sum_{i\text{ hard at }U_j}r_{Pi}&=t_P\,\frac{q-a_{U_j}}q\\
&=t_P-t_P\frac{a_{U_j}}q\\
&=t_P-r_P. \qquad\square
\end{aligned}
\]

## 5. The expansion

**Proposition 5.1 (finite expansion).** As functions on \(\{0,1\}^T\),
\[
\begin{gathered}
H_{T,\rho}=K+K\sum_{j=1}^{L}(-1)^j\tau_j,\\
\tau_j=\sum_{P\in\mathcal P_j(T)}\frac{v_{i_1}\cdots v_{i_j}}{a_{U_1}\cdots a_{U_j}} .
\end{gathered}
\]

*Proof.* Where \(K=0\), both sides vanish. Where \(K=1\) and \(q=0\), every numerator vanishes and both sides equal \(1\). Fix a point with \(K=1\) and \(q>0\). The paths of length one are the single indices hard at \(\varnothing\), so the display at the end of Section 2 says \(\sum_{P\in\mathcal P_1(T)}r_P=1\). Applying Lemma 4.1 to every path of length \(j\) and summing turns \(\sum_{\mathcal P_j}r_P\) into \(\sum_{\mathcal P_j}t_P-\sum_{\mathcal P_{j+1}}r_P\), because every path of length \(j+1\) arises exactly once as an extension. By induction on \(s\),
\[
\begin{aligned}
0=1&+\sum_{j=1}^{s}(-1)^j\sum_{\mathcal P_j(T)}t_P\\
&+(-1)^{s+1}\sum_{\mathcal P_{s+1}(T)}r_P
\end{aligned}
\]
for \(0\leq s\leq L\). For \(s=L\) the last sum is empty, by Lemma 3.1(a). So \(\sum_{j=1}^L(-1)^j\sum_{\mathcal P_j}t_P=-1\), and the right side of the proposition is \(1-1=0=H_{T,\rho}\). \(\square\)

Everything here is a finite identity between functions on a finite cube; no series and no convergence are involved. The number of paths may be enormous when \(H\) has many clauses. The next lesson controls the *sum of their weights* instead of their number.

## 6. Exercises

**6.1.** Let \(H\) consist of a single clause of width \(k>b\), and let \(T=[d]\). List the paths and check Proposition 5.1 directly.

**6.2.** Let \(H\) consist of two clauses with disjoint scopes of width \(k>b\), and \(T=[d]\). List the four paths and check the expansion at a point violating both clauses and at a point violating only the first.

**6.3.** Show that if \(k\leq b\), there are no paths and Proposition 5.1 says \(H_{T,\rho}=K\).

**6.4.** In Lemma 4.1, why is it important that \(a_{U_j}\) counts *all* violated clauses easy at \(U_j\), including those not on the path?

**6.5.** Show that a repeated clause (two indices with the same clause) causes no difficulty in the expansion.

## 7. Solutions

**6.1.** The clause is hard at \(\varnothing\), so \(K=1\). The only path is \((1)\), with \(U_1=E_1\); at \(U_1\) the clause is easy, so \(a_{U_1}=v_1\) and the term is \(v_1/v_1=v_1\) (zero where \(v_1=0\)). The expansion gives \(1-v_1\), which is the clause.

**6.2.** Paths: \((1)\), \((2)\), \((1,2)\), \((2,1)\). Where both clauses are violated, \(a_{U_1}=1\) after the first step and \(a_{U_2}=2\) after the second, so the terms are \(1,1,\frac12,\frac12\) and the expansion gives \(1-(1+1)+(\frac12+\frac12)=0\). Where only the first is violated, only \((1)\) has a nonzero numerator, with value \(1\), and the expansion gives \(1-1=0\). Both agree with \(H=0\).

**6.3.** Every clause has at most \(k\leq b\) live variables, so every index is easy at \(\varnothing\) and no first step exists. Then \(H_{T,\rho}=\mathbf 1[q=0]=\mathbf 1[a_\varnothing=0]=K\).

**6.4.** The identity \(q=a_{U_j}+\sum_{i\text{ hard at }U_j}v_i\) needs every violated clause to be counted on exactly one side; a violated easy clause that is not on the path still contributes to \(q\).

**6.5.** Repeated clauses are separate indices with equal scopes. They appear separately in \(q\), \(a_U\) and \(c_U\), and in separate paths; every identity above is a statement about indices, so multiplicities are carried consistently.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
