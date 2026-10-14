# Charts and reversible transport

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The walk of the course lives on finite sequences, and its labels are differences of basis vectors \(b_i\). The positions \(i\) are assigned to finitely many marked points of the real line by an increasing map, a *chart*. When a homeomorphism moves the marked points, the chart should change so that each moved point keeps its position. This lesson constructs a random chart whose law hardly depends on which points are looked at, and from it a reversible chain of charts in which such changes happen at almost every step.

- Charts of a finite ordered set, and a law on charts that treats all tuples of the same length alike (Lemma 1.1).
- Couplings (Lemmas 2.1 and 2.2).
- The reversible chain of charts (Proposition 3.1).

The lesson follows [OpenAI-M, Section 3]. It uses marked chains from [Markov type and the reduction to a finite walk](markov-type-and-the-reduction-to-a-finite-walk.md), and the minimax theorem and Ramsey's theorem from [Alignment of lists: patterns, minimax and Ramsey's theorem](course:large-independent-sets-in-three-colorable-graphs/alignment-of-lists-patterns-minimax-and-ramseys-theorem) (course *Large independent sets in three-colorable graphs*; Theorems 3.2 and 4.1 there).

## 1. A law on charts

Let \(\Lambda\) be a finite totally ordered set with \(\lambda\) elements. A *chart* with the bound \(B\) is a strictly increasing map
\[
C\colon\Lambda\to\{1,\dots,B\}.
\]
A *tuple* of \(\Lambda\) of the length \(m\) is a sequence \(A=(a_1<\dots<a_m)\) of elements of \(\Lambda\); then \(C(A)=(C(a_1),\dots,C(a_m))\) is an increasing sequence of \(m\) numbers in \(\{1,\dots,B\}\). Let \(\mathcal T_m\) be the set of these increasing sequences.

For two probability distributions \(\mu,\mu'\) on a finite set, the *total variation distance* is
\[
\operatorname{TV}(\mu,\mu')=\frac12\sum_x|\mu(x)-\mu'(x)| .
\]

**Lemma 1.1** ([OpenAI-M]). For every finite ordered set \(\Lambda\) and every \(\varepsilon>0\) there are a bound \(B\) and a probability distribution \(\nu\) on the charts with the bound \(B\) such that for any two tuples \(A,A'\) of \(\Lambda\) of the same length, the distributions of \(C(A)\) and \(C(A')\) for a chart \(C\) with the law \(\nu\) satisfy
\[
\operatorname{TV}\bigl(\operatorname{law}C(A),\ \operatorname{law}C(A')\bigr)<\varepsilon .
\]

**Proof.** *A game.* Let \((A_\rho,A'_\rho)\), \(\rho=1,\dots,R\), be all pairs of different tuples of the same length, and \(m_\rho\) their lengths. If \(R=0\) there is nothing to prove. Fix \(B\); it is chosen below. A *test* is a family \(\varphi=(\varphi_\rho)\) of functions \(\varphi_\rho:\mathcal T_{m_\rho}\to\{1,-1\}\). For a chart \(C\) and a test \(\varphi\) put
\[
\begin{aligned}
b(C,\varphi)={}&\sum_{\rho=1}^R\varphi_\rho(C(A_\rho))\\
&-\sum_{\rho=1}^R\varphi_\rho(C(A'_\rho)).
\end{aligned}
\]
There are finitely many charts and tests. By the minimax theorem,
\[
\begin{aligned}
&\min_\nu\max_\varphi\sum_C\nu_C\,b(C,\varphi)\\
&\qquad=\max_\kappa\min_C\sum_\varphi b(C,\varphi)\,\kappa_\varphi ,
\end{aligned}
\]
where \(\nu\) runs through the distributions on charts and \(\kappa\) through the distributions on tests.

*The left side.* For a distribution \(\nu\) let \(\mu_\rho\) and \(\mu'_\rho\) be the laws of \(C(A_\rho)\) and \(C(A'_\rho)\). Then
\[
\begin{aligned}
&\sum_C\nu_C\,b(C,\varphi)\\
&\quad=\sum_\rho\sum_x\varphi_\rho(x)\,\bigl(\mu_\rho(x)-\mu'_\rho(x)\bigr),
\end{aligned}
\]
and the maximum over the tests is \(\sum_\rho\sum_x|\mu_\rho(x)-\mu'_\rho(x)|\). So the left side is the minimum over \(\nu\) of
\[
2\sum_{\rho=1}^R\operatorname{TV}(\mu_\rho,\mu'_\rho).
\]

*The right side.* For a distribution \(\kappa\) on tests put \(\bar\varphi_\rho(x)=\sum_\varphi\kappa_\varphi\varphi_\rho(x)\in[-1,1]\). Then \(\sum_\varphi b(C,\varphi)\kappa_\varphi\) is the sum over \(\rho\) of the differences \(\bar\varphi_\rho(C(A_\rho))-\bar\varphi_\rho(C(A'_\rho))\). We show that for a suitable \(B\), which depends on \(\Lambda\) and \(\varepsilon\) only, for every family of functions \(\bar\varphi_\rho:\mathcal T_{m_\rho}\to[-1,1]\) there is a chart \(C\) with
\[
\sum_{\rho=1}^R\bigl|\bar\varphi_\rho(C(A_\rho))-\bar\varphi_\rho(C(A'_\rho))\bigr|\le\varepsilon .
\]
We refer to this inequality as (1.1). Then the right side is at most \(\varepsilon\), so there is \(\nu\) with \(2\sum_\rho\operatorname{TV}(\mu_\rho,\mu'_\rho)\le\varepsilon\), which proves the lemma.

*Ramsey.* Put \(\delta=\varepsilon/R\) and cut \([-1,1]\) into at most \(\lceil2/\delta\rceil+1\) intervals of a length of at most \(\delta\), called bins. For \(m=1,\dots,\lambda\), color the sets of \(m\) numbers in \(\{1,\dots,B\}\), read as increasing sequences \(x\in\mathcal T_m\), by the list of the bins of the values \(\bar\varphi_\rho(x)\) for the \(\rho\) with \(m_\rho=m\). The number of the colors is at most \(q=(\lceil2/\delta\rceil+1)^R\), whatever the functions are. With the numbers \(R_t(q,k)\) of Ramsey's theorem put
\[
\begin{gathered}
k_{\lambda+1}=\lambda,\\
k_m=R_m(q,k_{m+1})\quad\text{for }m=\lambda,\dots,1,\\
B=k_1 .
\end{gathered}
\]
Then there are sets \(\{1,\dots,B\}\supseteq H_1\supseteq H_2\supseteq\dots\supseteq H_\lambda\) such that \(H_m\) has \(k_{m+1}\) elements and all subsets of \(H_m\) with \(m\) elements have the same color. The set \(H=H_\lambda\) has \(\lambda\) elements, and for every \(m\) all its subsets with \(m\) elements have the same color. Let \(C\) be the increasing bijection from \(\Lambda\) onto \(H\). For every \(\rho\), the sequences \(C(A_\rho)\) and \(C(A'_\rho)\) are subsets of \(H\) with \(m_\rho\) elements, so the values of \(\bar\varphi_\rho\) on them lie in the same bin and differ by at most \(\delta\). This gives (1.1). \(\blacksquare\)

The uniform distribution on all charts does not have the property of the lemma (Exercise 4.2): under it the first point of \(\Lambda\) tends to get small numbers and the last point large ones. The law \(\nu\) must spread the charts over many scales, so that the position of a point says almost nothing about its rank in \(\Lambda\). The proof does not construct \(\nu\); it shows by the minimax theorem that a suitable mixture exists.

## 2. Couplings

A *coupling* of two probability distributions \(\mu\) on \(\Omega\) and \(\mu'\) on \(\Omega'\) is a distribution on \(\Omega\times\Omega'\) with the marginals \(\mu\) and \(\mu'\).

**Lemma 2.1.** Let \(\mu,\mu'\) be distributions on the same finite set \(\Omega\). There is a coupling \(\kappa\) of \(\mu\) and \(\mu'\) with
\[
\kappa\{(x,x):x\in\Omega\}=1-\operatorname{TV}(\mu,\mu').
\]

**Proof.** Put \(\mu_0(x)=\min\{\mu(x),\mu'(x)\}\). Since \(\min\{s,t\}=\tfrac12(s+t-|s-t|)\), the total mass of \(\mu_0\) is \(1-\theta\) with \(\theta=\operatorname{TV}(\mu,\mu')\). The functions \(\mu-\mu_0\) and \(\mu'-\mu_0\) are \(\ge0\) with the total mass \(\theta\) each. Put \(\kappa(x,x)=\mu_0(x)\) and, if \(\theta>0\), add \((\mu-\mu_0)(x)\,(\mu'-\mu_0)(y)/\theta\) at every pair \((x,y)\). The marginals are \(\mu\) and \(\mu'\). For every \(x\) one of \((\mu-\mu_0)(x)\), \((\mu'-\mu_0)(x)\) is \(0\), so the added mass on the diagonal is \(0\). \(\blacksquare\)

**Lemma 2.2.** Let \(\nu,\nu'\) be distributions on finite sets \(\Omega,\Omega'\), let \(\Psi:\Omega\to\Xi\) and \(\Psi':\Omega'\to\Xi'\) be maps, and \(\kappa\) a coupling of the law of \(\Psi\) under \(\nu\) and the law of \(\Psi'\) under \(\nu'\). Then there is a coupling of \(\nu\) and \(\nu'\) under which the pair \((\Psi,\Psi')\) has the law \(\kappa\).

**Proof.** Let \(p\) and \(p'\) be the laws of \(\Psi\) and \(\Psi'\). Give the pair \((\omega,\omega')\) the mass
\[
\kappa\bigl(\Psi(\omega),\Psi'(\omega')\bigr)\,\frac{\nu(\omega)}{p(\Psi(\omega))}\,\frac{\nu'(\omega')}{p'(\Psi'(\omega'))}
\]
if \(\nu(\omega)\nu'(\omega')>0\), and \(0\) otherwise. Summing over \(\omega'\) with a fixed value of \(\Psi'\) and then over this value gives \(\nu(\omega)\), because the first marginal of \(\kappa\) is \(p\). The same holds for the other marginal. Summing over all \((\omega,\omega')\) with given values \((\xi,\xi')\) of \((\Psi,\Psi')\) gives \(\kappa(\xi,\xi')\). \(\blacksquare\)

## 3. The chain of charts

**Proposition 3.1** (reversible transport; [OpenAI-M]). Let \(\Lambda\) be a finite ordered set. Let \(\mathcal S\) be a finite nonempty set with a map \(s\mapsto s^{-1}\) such that \((s^{-1})^{-1}=s\) and \(s^{-1}\ne s\). For every \(s\in\mathcal S\) let \(T_s:D_s\to D_{s^{-1}}\) be an order-preserving bijection between subsets of \(\Lambda\), with \(T_{s^{-1}}=T_s^{-1}\). Let \(\varepsilon>0\). Then there are a bound \(B\) and a finite stationary reversible marked chain with the following properties.

1. Its states are charts of \(\Lambda\) with the bound \(B\). Its edges are triples \((C,s,C')\) of a chart, an element of \(\mathcal S\) and a chart, which starts at \(C\), ends at \(C'\) and has the reverse \((C',s^{-1},C)\).
2. The letters \(s_1,s_2,\dots\) of the successive edges \(E_i=(C_{i-1},s_i,C_i)\) are independent and uniformly distributed in \(\mathcal S\).
3. Call an edge \((C,s,C')\) *good* if \(C'(a)=C(T_s(a))\) for all \(a\in D_s\). For every \(i\), the edge \(E_i\) is good with a probability of at least \(1-\varepsilon\).

**Proof.** *The law.* Let \(B\) and \(\nu\) be as in Lemma 1.1 for \(\Lambda\) and \(\varepsilon\).

*Couplings.* Fix \(s\). List the elements of \(D_s\) in increasing order as a tuple \(A\); then \(T_s(A)\), the tuple of their images, is a tuple of \(\Lambda\) of the same length, because \(T_s\) preserves the order. By Lemma 1.1 the laws of \(C(T_s(A))\) and of \(C'(A)\), for charts \(C,C'\) with the law \(\nu\), have a total variation distance less than \(\varepsilon\). By Lemmas 2.1 and 2.2 there is a coupling \(\lambda_s\) of \(\nu\) with \(\nu\) under which the pairs \((C,C')\) with \(C'(A)=C(T_s(A))\) have a mass larger than \(1-\varepsilon\). The condition \(C'(A)=C(T_s(A))\) says that \((C,s,C')\) is good. Choose such a coupling for one element of each pair \(\{s,s^{-1}\}\), and for the other put
\[
\lambda_{s^{-1}}(C,C')=\lambda_s(C',C).
\]
This is again a coupling of \(\nu\) with \(\nu\). The edge \((C,s^{-1},C')\) is good if \(C'(a)=C(T_s^{-1}(a))\) for all \(a\in D_{s^{-1}}\), that is, if \(C'(T_s(a'))=C(a')\) for all \(a'\in D_s\), that is, if \((C',s,C)\) is good. So \(\lambda_{s^{-1}}\) gives the mass \(>1-\varepsilon\) to the good pairs as well.

*The chain.* The states are the charts \(C\) with \(\nu(C)>0\). The edges are the triples \((C,s,C')\) with \(\lambda_s(C,C')>0\), with
\[
q(C,s,C')=\frac1{|\mathcal S|}\cdot\frac{\lambda_s(C,C')}{\nu(C)} .
\]
The sum of \(q\) over the edges that start at \(C\) is \(1\), because the first marginal of every \(\lambda_s\) is \(\nu\). The reverse of an edge is an edge, and
\[
\begin{aligned}
\nu(C)\,q(C,s,C')&=\frac{\lambda_s(C,C')}{|\mathcal S|}\\
&=\frac{\lambda_{s^{-1}}(C',C)}{|\mathcal S|}\\
&=\nu(C')\,q(C',s^{-1},C).
\end{aligned}
\]
So the marked chain is stationary and reversible for \(\nu\).

*Properties 2 and 3.* From a state \(C\), the chain chooses the edge \((C,s,C')\) with the probability \(q\): this is the same as choosing \(s\) uniformly in \(\mathcal S\), whatever \(C\) and the past are, and then \(C'\) with the probability \(\lambda_s(C,C')/\nu(C)\). So the letters are independent and uniform. Every edge \(E_i\) has the distribution \(\nu(C)q(C,s,C')=\lambda_s(C,C')/|\mathcal S|\), and the good edges have, for each \(s\), the mass \(>(1-\varepsilon)/|\mathcal S|\). \(\blacksquare\)

In a good step with the letter \(s\), a point \(a\in D_s\) has in the new chart the position that \(T_s(a)\) had in the old chart. If \(T_s\) comes from a map \(h_s\) of the line, this means: when the points are moved back by \(h_s\), the chart follows them. The price is the probability \(\varepsilon\) of a step that is not good; the reward is that the chain is reversible and that its letters are a sequence of independent uniform choices.

## 4. Exercises

**4.1.** Show that \(\operatorname{TV}(\mu,\mu')=\max_{F}(\mu(F)-\mu'(F))\), the maximum over all subsets \(F\), and that every coupling \(\kappa\) of \(\mu\) and \(\mu'\) has \(\kappa\{(x,x)\}\le1-\operatorname{TV}(\mu,\mu')\).

**4.2.** Let \(\Lambda=\{a_1<a_2\}\), and let \(C\) be uniformly distributed among all charts with the bound \(B\). Show that the total variation distance of the laws of \(C(a_1)\) and \(C(a_2)\) tends to \(\tfrac12\) for \(B\to\infty\).

**4.3.** For \(\Lambda=\{a_1<a_2\}\) give a law \(\nu\) on charts for which the laws of \(C(a_1)\) and \(C(a_2)\) have a total variation distance of \(\tfrac1{B-1}\).

**4.4.** Let \(h_s\), \(s\in\mathcal S\), be increasing bijections of the real line with \(h_{s^{-1}}=h_s^{-1}\), and \(\Lambda\) a finite subset of the line. Show that \(D_s=\{a\in\Lambda:h_s(a)\in\Lambda\}\) and \(T_s=h_s|_{D_s}\) satisfy the conditions of Proposition 3.1.

**4.5.** In the chain of Proposition 3.1, let \(n\ge1\). Show that all of \(E_1,\dots,E_n\) are good with a probability of at least \(1-n\varepsilon\), and that this event need not be independent of the letters.

## 5. Solutions

**4.1.** For a set \(F\), \(\mu(F)-\mu'(F)=\sum_{x\in F}(\mu(x)-\mu'(x))\) is largest for \(F=\{x:\mu(x)>\mu'(x)\}\), where it is the sum of the positive parts of \(\mu-\mu'\); this is half of \(\sum|\mu-\mu'|\), because the positive and the negative parts have the same sum. For a coupling, \(\kappa(x,x)\le\min\{\mu(x),\mu'(x)\}\), and the sum of the minima is \(1-\operatorname{TV}\).

**4.2.** There are \(\binom B2\) charts. \(C(a_1)=i\) for \(B-i\) of them and \(C(a_2)=i\) for \(i-1\) of them. So \(\operatorname{TV}=\tfrac12\sum_{i=1}^B|B-2i+1|/\binom B2\). The sum is about \(B^2/2\) and \(\binom B2\) is about \(B^2/2\); the quotient tends to \(1\), and the distance to \(\tfrac12\).

**4.3.** Let \(X\) be uniform in \(\{1,\dots,B-1\}\) and \(C(a_1)=X\), \(C(a_2)=X+1\). The laws are uniform on \(\{1,\dots,B-1\}\) and on \(\{2,\dots,B\}\); they differ at the two points \(1\) and \(B\) by \(\tfrac1{B-1}\) each, so the distance is \(\tfrac1{B-1}\).

**4.4.** \(h_s\) maps \(D_s\) bijectively onto \(\{b\in\Lambda:h_s^{-1}(b)\in\Lambda\}=D_{s^{-1}}\), it preserves the order, and its inverse on this set is \(h_{s^{-1}}\).

**4.5.** Each \(E_i\) fails to be good with a probability of at most \(\varepsilon\); the probability that one of \(n\) fails is at most \(n\varepsilon\). The probability of a good step may depend on the letter \(s\), since the couplings \(\lambda_s\) are different for different \(s\); only the bound \(\varepsilon\) is common.

## References

- [OpenAI-M] OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026
