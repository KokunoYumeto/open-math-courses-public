# Path weights and backward counting

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[A finite expansion of a restricted CNF](a-finite-expansion-of-a-restricted-cnf.md) wrote a restricted CNF of width \(k\) as \(K\) plus a signed sum over paths of wide clauses. This lesson finishes the proof of the restriction bound (Lemma 1.1 of that lesson). Each path term is a positive weight times an *average* of CNFs of width at most \(b\); this gives the correlation inequality with the total weight \(W\). The expected total weight is then bounded by counting the paths *backwards* from a full random assignment. At each backward step the count is divided by the number of candidate clauses, which is why the number of clauses never enters.

Notation is that of the previous lesson: the clauses \(C_i\) with scopes \(E_i\), the restriction \((T,\rho)\), the indicators \(v_i\), the counts \(q\), \(a_U\), \(c_U\), the CNF \(K\), and paths \(P=(i_1,\ldots,i_j)\) with sets \(U_1\subseteq\cdots\subseteq U_j\).

## 1. A finite mixture

**Lemma 1.1 (marker mixture).** Let \(D_1,\ldots,D_a\) be an indexed family of clauses (repetitions and constant clauses allowed, \(a\geq0\)) and \(c\geq1\) an integer. Put the \(a\) clauses and \(c\) distinct markers in a uniformly random order, and let \(\Psi\) be the conjunction of the clauses placed before the first marker. If an assignment violates exactly \(w\) of the clauses, then \(\Psi\) holds there with probability
\[
\frac c{c+w}.
\]

*Proof.* \(\Psi\) holds exactly when no violated clause comes before the first marker, that is, when the first of the \(w+c\) objects consisting of the violated clauses and the markers is a marker. In a uniform order each of these objects is equally likely to come first. \(\square\)

The random conjunction \(\Psi\) is a CNF built from the given clauses, so if they have width at most \(b\), every outcome of \(\Psi\) does too.

## 2. Compatible paths

A path \(P=(i_1,\ldots,i_j)\) is *compatible* with \(\rho\) if the clauses \(C_{i_1},\ldots,C_{i_j}\) can be violated simultaneously at some point that agrees with \(\rho\) outside \(T\). Violating a clause prescribes its unique violating pattern on its scope, so a compatible path prescribes exactly one pattern \(\sigma_P\) on \(U_j\), the live part of the union of the selected scopes, and nothing elsewhere on \(T\). Let
\[
\mathcal Z_P=\{z\in\{0,1\}^T:z|_{U_j}=\sigma_P\}
\]
be this cylinder. Then \(v_{i_1}\cdots v_{i_j}=\mathbf 1_{\mathcal Z_P}\). For an incompatible path the product vanishes identically, and the path can be dropped from the expansion.

For a compatible path and \(1\leq h\leq j\), the count \(c_{U_h}\) is constant on \(\mathcal Z_P\): it counts violated clauses whose live variables lie in \(U_h\subseteq U_j\), and these are all fixed there. Denote this constant by \(c_h\); it is at least \(h\), by Lemma 3.1(c) of the previous lesson. Define the *weight*
\[
\omega(P)=\frac1{c_1c_2\cdots c_j}.
\]

## 3. Each term is a weighted average of narrow CNFs

**Lemma 3.1.** For a compatible path \(P\) of length \(j\) there is a random CNF \(J_P\), drawn from a finite probability space independent of everything else, such that every outcome of \(J_P\) lies in \(\mathcal C_b(T)\), and as functions on \(\{0,1\}^T\)
\[
K\,\frac{v_{i_1}\cdots v_{i_j}}{a_{U_1}\cdots a_{U_j}}=\omega(P)\,\mathbb E[J_P].
\]

*Proof.* On \(\mathcal Z_P\), split \(a_{U_h}=c_h+w_h\), where \(w_h=\sum_{i\in I_h}v_i\) counts the violated clauses in
\[
I_h=\{i:0<|E_i\cap(T\setminus U_h)|\leq b\}.
\]
Substitute \(\rho\) and the pattern \(\sigma_P\) into each clause \(C_i\) with \(i\in I_h\). The result is a clause on \(T\setminus U_j\) of width at most \(b\), since \(T\setminus U_j\subseteq T\setminus U_h\), or a constant clause; keep the indexing, repetitions and constants included. On \(\mathcal Z_P\), the clause \(C_i\) is violated exactly when its substituted version is, so \(w_h\) is the number of violated clauses in this indexed family.

For each \(h\), apply Lemma 1.1 to this family with \(c=c_h\), independently for different \(h\), and let \(J_P\) be the conjunction of the \(j\) resulting CNFs, of \(K\), and of the unit clauses prescribing \(\sigma_P\) on \(U_j\). True clauses can be dropped and a false clause makes \(J_P\) the false CNF; every outcome lies in \(\mathcal C_b(T)\), using \(b\geq1\) for the unit clauses. Off \(\mathcal Z_P\) both sides vanish. On \(\mathcal Z_P\), independence and Lemma 1.1 give
\[
\begin{aligned}
\mathbb E[J_P]&=K\prod_{h=1}^{j}\frac{c_h}{c_h+w_h}\\
&=\frac K{\omega(P)\,a_{U_1}\cdots a_{U_j}},
\end{aligned}
\]
which is the claim, since the numerator \(v_{i_1}\cdots v_{i_j}\) equals \(1\) there. \(\square\)

**Proof of the correlation inequality.** Put
\[
W_0=1,\qquad W_j=\sum_{P}\omega(P)\quad(j\geq1),
\]
the sum over compatible paths of length \(j\), and \(W=W(H,T,\rho)=\sum_{j\geq0}W_j\), a finite sum by Lemma 3.1(a) of the previous lesson. By Proposition 5.1 of the previous lesson and Lemma 3.1,
\[
H_{T,\rho}=K+\sum_{j\geq1}(-1)^j\sum_P\omega(P)\,\mathbb E[J_P].
\]
For any \(G:\{0,1\}^T\to\mathbb R\), take the correlation with \(G\) and exchange the finite averages. Every outcome of \(J_P\), and \(K\), lies in \(\mathcal C_b(T)\), so each correlation is at most \(\operatorname{corr}_b(G)\) in absolute value, and the triangle inequality gives \(|\mathbb E_zG(z)H_{T,\rho}(z)|\leq W\operatorname{corr}_b(G)\). The weights and the mixtures were chosen without reference to \(G\). \(\square\)

## 4. Reweighting by a full assignment

**Lemma 4.1.** Let \(y\) be a uniform point of \(\{0,1\}^d\), independent of \(T\), and let \(\rho\) be its restriction to \([d]\setminus T\). Then for \(j\geq1\)
\[
\mathbb E_{T,\rho}W_j=\mathbb E_{T,y}\Bigl[\sum_P2^{|U_j|}\prod_{h=1}^{j}\frac1{c_{U_h}(y)}\Bigr],
\]
the sum over paths \(P\in\mathcal P_j(T)\) whose clauses \(C_{i_1},\ldots,C_{i_j}\) are all violated at \(y\); here \(c_{U_h}(y)\) is evaluated at the live part of \(y\).

*Proof.* The pair \((T,\rho)\) has the law of a \(p\)-random restriction, and given \((T,\rho)\) the live part of \(y\) is uniform on \(\{0,1\}^T\). Fix \((T,\rho)\) and a path \(P\). If \(P\) is compatible, the live part of \(y\) lies in \(\mathcal Z_P\) with probability \(2^{-|U_j|}\), and on that event all the selected clauses are violated and \(c_{U_h}=c_h\). So the conditional expectation of \(2^{|U_j|}\mathbf 1[\text{all selected violated}]\prod_h1/c_{U_h}\) is exactly \(\omega(P)\). If \(P\) is incompatible, the indicator vanishes. Summing over paths and averaging over \((T,\rho)\) gives the identity. \(\square\)

The identity holds path by path, before any summation; it does not require compatibility or the counts \(c_{U_h}\) to be independent of the restriction.

## 5. Counting backwards

Fix \(y\). For \(R\subseteq[d]\) let \(V_R\) be the set of indices \(i\) such that \(C_i\) is violated at \(y\) and \(E_i\cap R=\varnothing\). For a path counted in Lemma 4.1 put \(D_h=U_h\setminus U_{h-1}\) and \(R_h=T\setminus U_h\), the live coordinates not yet prescribed. Then for \(1\leq h\leq j\):
\[
\begin{gathered}
i_h\in V_{R_h},\qquad D_h\subseteq E_{i_h},\qquad|D_h|>b,\\
R_{h-1}=R_h\cup D_h\ \text{(disjointly)},\\
c_{U_h}(y)=|V_{R_h}|.
\end{gathered}
\]
Indeed \(D_h=E_{i_h}\cap(T\setminus U_{h-1})\) has more than \(b\) elements, the scope of \(i_h\) misses \(T\setminus U_h\), and \(c_{U_h}\) counts the violated clauses whose scopes miss \(T\setminus U_h\).

So the pair \((T,P)\) is determined by the final set \(R_j\) and the *reverse choices* \((i_j,D_j),\ldots,(i_1,D_1)\): each choice recovers \(R_{h-1}=R_h\cup D_h\), and finally \(T=R_0\). Conversely, define a *reverse step* from any set \(R\) to be a choice of \(i\in V_R\) and of \(D\subseteq E_i\) with \(|D|>b\), leading to \(R\cup D\); since \(E_i\cap R=\varnothing\), the union is disjoint. Every counted pair \((T,P)\) gives a sequence of \(j\) reverse steps starting at \(R_j\), and different pairs give different sequences.

Put \(\alpha=2p/(1-p)\) and \(\pi(R)=p^{|R|}(1-p)^{d-|R|}\), the probability that the live set equals \(R\). Since \(T=R_j\cup U_j\) disjointly and the \(D_h\) partition \(U_j\),
\[
\pi(T)\,2^{|U_j|}\prod_{h=1}^{j}\frac1{c_{U_h}(y)}=\pi(R_j)\prod_{h=1}^{j}\frac{\alpha^{|D_h|}}{|V_{R_h}|}.
\]
The factor \(1/|V_{R_h}|\) belongs to the state \(R_h\) from which the reverse step is taken. Define \(F_0(R)=1\) and, for \(s\geq1\),
\[
\begin{aligned}
F_s(R)=\frac1{|V_R|}\sum_{i\in V_R}\,&\sum_{\substack{D\subseteq E_i\\|D|>b}}\alpha^{|D|}\\
&\times F_{s-1}(R\cup D)
\end{aligned}
\]
if \(V_R\neq\varnothing\), and \(F_s(R)=0\) otherwise: the total weight of all sequences of \(s\) reverse steps from \(R\).

**Lemma 5.1.** \(F_s(R)\leq\theta^s\) for every \(R\) and \(s\geq0\).

*Proof.* For each \(i\), since \(|E_i|\leq k\) and \(\binom e\ell\leq\binom k\ell\) for \(e\leq k\),
\[
\sum_{D\subseteq E_i,\,|D|>b}\alpha^{|D|}=\sum_{\ell=b+1}^{|E_i|}\binom{|E_i|}\ell\alpha^\ell\leq\theta .
\]
By induction \(F_{s-1}\leq\theta^{s-1}\), so \(F_s(R)\) is at most \(\theta^{s-1}\) times the *average* over \(i\in V_R\) of the left side, which is at most \(\theta\). \(\square\)

Averaging over \(i\in V_R\), rather than summing, is the decisive point: the number of violated clauses cancels against the reciprocal count that the paths carry.

**Proof of the expectation bound.** For fixed \(y\), the inner expectation over \(T\) in Lemma 4.1 is a sum over counted pairs \((T,P)\) of the left side of the weight identity. By the injective encoding it is at most
\[
\sum_{R\subseteq[d]}\pi(R)F_j(R)\leq\theta^j\sum_{R\subseteq[d]}\pi(R)=\theta^j ,
\]
since all weights are nonnegative and the actual reverse sequences are among those counted by \(F_j\). Averaging over \(y\) gives \(\mathbb EW_j\leq\theta^j\), and since \(\theta<1\),
\[
\mathbb EW=\sum_{j\geq0}\mathbb EW_j\leq\frac1{1-\theta} . \qquad\square
\]

This completes the proof of the restriction bound. If \(k\leq b\), there are no paths and \(W=1\); empty formulas, false clauses and empty live sets are covered by the same construction.

## 6. Exercises

**6.1.** Check Lemma 1.1 for two clauses and one marker by listing the six orders, for an assignment violating one of the two clauses.

**6.2.** Let \(H\) be a single clause of width \(k>b\). Show that \(W=2\) if \(|E_1\cap T|>b\) and \(\rho\) falsifies the literals of \(C_1\) outside \(T\), and \(W=1\) otherwise; compute \(\mathbb EW\). Compare with \(1/(1-\theta)\).

**6.3.** Where does the proof use that every path step adds *more than* \(b\) coordinates?

**6.4.** Why is the weight \(\omega(P)\) defined through the counts \(c_h\) of clauses with *no* live variables outside \(U_h\), and not through \(a_{U_h}\)?

**6.5.** Show that \(\binom k\ell\leq k^\ell/\ell!\), and deduce that \(\theta\leq\sum_{\ell>b}(k\alpha)^\ell/\ell!\).

## 7. Solutions

**6.1.** Let the clauses be \(D_1\) (violated) and \(D_2\) (satisfied), with marker \(\mu\). Of the six orders, \(\Psi\) holds when \(\mu\) precedes \(D_1\): the orders \(\mu D_1D_2\), \(\mu D_2D_1\) and \(D_2\mu D_1\). That is \(3/6=1/2=c/(c+w)\) with \(c=w=1\).

**6.2.** There is at most one path, \((1)\), and it exists exactly when \(|E_1\cap T|>b\); it is compatible exactly when \(\rho\) falsifies the literals of \(C_1\) outside \(T\). On its cylinder the only violated clause is \(C_1\), so \(c_1=1\) and \(\omega=1\). With \(\ell=|E_1\cap T|\) binomial,
\[
\mathbb EW=1+\sum_{\ell=b+1}^{k}\binom k\ell p^\ell\Bigl(\frac{1-p}2\Bigr)^{k-\ell} .
\]
Each term equals \(\binom k\ell\alpha^\ell\) times \(2^{-k}(1-p)^k\leq1\), so \(\mathbb EW\leq1+\theta\leq1/(1-\theta)\).

**6.3.** In Lemma 5.1: reverse steps only use sets \(D\) with \(|D|>b\), so only the terms with \(\ell>b\) occur, and their sum \(\theta\) is small. It also bounds the length of paths.

**6.4.** On the cylinder \(\mathcal Z_P\) the counts \(c_{U_h}\) are constants, while \(a_{U_h}\) still depends on the free coordinates through \(w_h\). Lemma 1.1 turns exactly the varying part \(c_h/(c_h+w_h)\) into an average of CNFs, leaving the constant \(1/c_h\) as weight.

**6.5.** \(\binom k\ell=k(k-1)\cdots(k-\ell+1)/\ell!\leq k^\ell/\ell!\). Hence \(\binom k\ell\alpha^\ell\leq(k\alpha)^\ell/\ell!\), and summing over \(\ell>b\) gives the bound. The last lesson, [The lower bound](the-lower-bound.md), uses it with \(k\alpha\) bounded.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
