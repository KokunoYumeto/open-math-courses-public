# A positive statistic and its binary-tree transfers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The last part of the proof of Theorem 5.1 of Lesson 1 begins here. All the preparatory results are in place: square-root sizes and collision stability (Lesson 2), mixed flatness of the normalized transforms \(g_p\) (Lesson 9), a large supply of primes whose transforms have \(L^1\) norm bounded below (Lesson 10), and the finite-field tree comparison (Lessons 12–13). This lesson builds a nonnegative statistic from the nonsparse transforms. A *giant* prime from a well-chosen cell is combined with bulk primes, *spectator* primes and cells of medium primes, and the statistic is forced to be large by collision stability (Section 2). Poisson summation turns it into an amplitude \(\eta_0\) with \(|\eta_0|\ge e^{-B_*m}\) (Proposition 3.1). The transfers of Lessons 7–9 then produce amplitudes \(\eta_1,\dots,\eta_k\) with
\[
e^{-c_g}|\eta_{j-1}|^2\le\mathcal D_j+\eta_j
\]
(Proposition 5.1), and the lesson ends with the two *comparison estimates* (Proposition 6.1) that Lessons 15–17 prove and Lesson 18 uses.

The architecture is that of Lessons 7–8, with two changes. The transforms carry no multiplicative-character phase, so the anchors of Lesson 9 are replaced by a common list of spectator primes, at which the finite-field tree comparison compares histories. And only the giant prime of each pivot is extended to the integers; the other pivot primes keep their prime priors.

**Prerequisites.** [*Square-root bounds and collision stability*](square-root-bounds-and-collision-stability.md), Lemma 4.1; [*Anchor codes and decorrelation of higher characters*](anchor-codes-and-decorrelation-of-higher-characters.md), Theorem 6.1; [*A tensor budget and a contracting kernel*](a-tensor-budget-and-a-contracting-kernel.md), Theorem 1.1; [*Templates, transfers and frequency histories*](templates-transfers-and-frequency-histories.md), Sections 2–4.

All parameters in this lesson are new; in particular \(L,k,m\) are not the parameters of Lessons 7–11.

## 1. Scales, cells and priors

Let \(L\to\infty\). The *depth* \(k\) is a large fixed integer, chosen before \(L\) tends to infinity. Put
\[
\begin{gathered}
h=e^{0.01L},\\
z=k^4,\\
m=2\lfloor zL/2\rfloor,\\
r_j=2^{j-1}\quad(1\le j\le k).
\end{gathered}
\]
The notation \(o_k(m)\) and \(O_k(1)\) allows dependence on everything fixed before \(L\). In bounds of the form \(Cm\) or \(C2^lm\), however, \(C\) is independent of \(k\) and of the gap constants \(B_s,B_D,B_z\) introduced next, once \(k\) and then \(L\) are large. Lesson 18 fixes the order in which these constants are chosen. Define
\[
\begin{aligned}
\Delta_0&=(B_s+8\log z)\,m,\\
\Delta_j&=r_j\bigl(B_D+B_z\log z+0.4\log r_j\bigr)m\\
&\qquad(1\le j\le k),\\
E_l&=\Delta_0+\sum_{j=1}^l\Delta_j+2^l\sqrt m,\quad V_l=e^{E_l}\\
&\qquad(0\le l\le k).\quad(1.1)
\end{aligned}
\]
So \(\log V_l=O_k(m)\), and every frequency used below is smaller than every sampled prime: the smallest prime range has lower endpoint \(\exp(\exp(0.0005L))\).

**Log-cell priors.** Fix a nonnegative smooth function \(\varphi\) supported in \([-1,1]\) with \(\sum_{n\in\mathbb Z}\varphi(t-n)=1\) for all real \(t\); then \(0\le\varphi\le1\) and \(\int\varphi=1\). For a centre \(c\), the *log-cell prior* is the probability measure on primes proportional to \(\varphi(\log p-c)/p\). Except for the giant prior defined below, all priors omit a fixed set \(\mathcal E_L\) of at most two prime values, chosen in Lesson 15. For the centres used here, the prime number theorem and partial summation give
\[
\begin{gathered}
Z_c=\sum_{p\notin\mathcal E_L}\frac{\varphi(\log p-c)}p\sim\frac1c,\\
\sum_p\frac{\log p}p\varphi(\log p-c)=1+o(1),
\end{gathered}
\]
uniformly, with or without the deletion.

**The giant block.** Call a prime *favourable* if \(\frac13\le\sigma_p\le\frac23\) and \(\gamma_p\ge\delta_0\), with \(\delta_0\) from Theorem 1.1 of Lesson 10.

**Lemma 1.1.** For large \(L\) there is a block \([G_0,G_0+h]\) of values of \(\log p\), inside \([e^{0.05L},e^{0.9L}]\), on which the favourable primes have \((\log p)/p\)-weight at least \(c_0h\), for a fixed \(c_0>0\).

*Proof.* Partition \([e^{0.05L},e^{0.9L}]\) into blocks of length \(h\) and two end pieces. On each block \(\log p\) varies by a relative \(o(1)\), uniformly. If every block had favourable weight at most \(ch\), then dividing by the left endpoint and summing would give favourable harmonic weight at most \((0.85c+o(1))L\); Mertens' estimate makes the end pieces negligible. For a small fixed \(c\) this contradicts Theorem 1.1 of Lesson 10. \(\square\)

Set
\[
\begin{gathered}
\log X=2G_0+2^{k+1}h,\\
A'=A\cap[X^{9/10},X].\quad(1.2)
\end{gathered}
\]
The block lies below the prime cutoff of collision stability for the uniform measure on \(A'\): \(\log\sqrt X=G_0+2^kh\), while the block ends at \(G_0+h\), and the cutoff loses only \(O(\log\log X)=O(L)\).

**Phase-free tests.** Recall \(F_p\) and \(g_p\) from (6.1) of Lesson 9, with \(F_p(x)=p^{-1/2}\sum_bg_p(b)e_p(bx)\). For a favourable prime put
\[
\widetilde g_p(b)=
\begin{cases}g_p(b)/|g_p(b)|,&g_p(b)\ne0,\\0,&g_p(b)=0,\end{cases}
\]
and \(\widetilde g_p=0\) at all other primes. Let \(\widetilde F_p(x)=p^{-1/2}\sum_b\widetilde g_p(b)e_p(bx)\). Since \(g_p(-b)=\overline{g_p(b)}\), \(\widetilde F_p\) is real; also \(\mathbb E\widetilde F_p=0\) and \(\mathbb E|\widetilde F_p|^2=\mathbb E_b|\widetilde g_p(b)|^2\le1\). For a favourable prime, writing \(\mathbf 1_{S_p}=\sigma_p+\sqrt{\sigma_p(1-\sigma_p)}F_p\) and using Parseval,
\[
\begin{aligned}
&\mathbb E_{x\in S_p}\widetilde F_p(x)\\
&\quad =\sqrt{\frac{1-\sigma_p}{\sigma_p}}\cdot\frac1p\sum_b|g_p(b)|\\
&\quad \ge\frac{\delta_0}{\sqrt2}.\quad(1.3)
\end{aligned}
\]

**Lemma 1.2** (the giant cell [OpenAI-013, (7.2)]). There is an integer centre \(G\), with the support of its log cell inside \([G_0,G_0+h]\), such that
\[
\begin{aligned}
&\mathbb E_{\substack{p\ \text{in the cell at}\ G\\a\in A'}}\widetilde F_p(a)\\
&\quad \ge c_1>0,\quad(1.4)
\end{aligned}
\]
where the giant prior includes all primes of the cell.

*Proof.* Let \(\mu_p\) be the image modulo \(p\) of the uniform measure on \(A'\). By Cauchy–Schwarz and \(\sum_x|\widetilde F_p(x)|^2\le p\),
\[
\begin{aligned}
&\Bigl|\sum_x\bigl(\mu_p(x)-U_{S_p}(x)\bigr)\widetilde F_p(x)\Bigr|^2\\
&\quad \le p\,\|\mu_p-U_{S_p}\|_2^2 .
\end{aligned}
\]
By Lemma 4.1 of Lesson 2 (with Lemma 5.1 there), the \((\log p)/p\)-weighted sum of these squared errors is \(O(\log\log X)=O(L)\). The block has total weight \(O(h)\), so by Cauchy–Schwarz the weighted sum of the absolute errors over the block is \(O(\sqrt{Lh})=o(h)\). By (1.3) and Lemma 1.1 the favourable uniform means have weighted sum at least \(c_0\delta_0h/\sqrt2\), and \(\widetilde F_p=0\) at the other primes. Partition by the translates \(\varphi(\log p-n)\), discarding bounded-width end strips; some cell then has a positive weighted empirical mean, bounded below by a fixed constant. In a cell \(\log p\) has relative variation \(o(1)\), so replacing \((\log p)/p\) by \(1/p\) keeps the conclusion. \(\square\)

Fix this \(G\), and put
\[
\begin{gathered}
Z_G=\sum_p\frac{\varphi(\log p-G)}p,\\
\mu_G(p)=\frac{\varphi(\log p-G)}{pZ_G},\\
c_g=\log Z_G^{-1}.\quad(1.5)
\end{gathered}
\]
Then \(Z_G\sim G^{-1}\) and \(c_g=\log G+O(1)\le0.91L\) for large \(L\), with a coefficient independent of the gap constants and of \(k\).

## 2. Half-lists and the positive statistic

A *half-list* consists of the following independent positions:

1. one *giant*, with prior \(\mu_G\) and test \(\widetilde F_p\);
2. \(m/2\) *bulk* positions, with the common prior proportional to \(1/p\) on \(0.004L\le\log\log p\le0.006L\), omitting \(\mathcal E_L\);
3. \(m/2\) *spectator* positions, with the common prior proportional to \(1/p\) on a subset of \(0.0005L\le\log\log p\le0.001L\) of harmonic mass \(\gg L\), omitting \(\mathcal E_L\), on which the conclusions (6.2) of Lesson 9 hold uniformly with a bound tending to zero;
4. three *top* positions and, for each \(j=1,\dots,k\), two *compensation* positions of *type* \(j\), with cell priors chosen below.

Every position other than the giant uses the exact test \(F_p\). The spectator subset exists by Theorem 6.1 of Lesson 9, with a threshold tending to zero slowly enough. The bulk and spectator normalizing masses lie between fixed positive multiples of \(L\).

**Sum bins.** Let \(S_b,S_d\) be the sums of \(\log p\) over the bulk and the spectator positions of a half-list. Include in its weight the factors \(\varphi(S_b-t_b)\varphi(S_d-t_d)\); these are weights, not conditionings of the priors. Choose integer centres \(t_b,t_d\) such that, for each of the two groups, the expectation of its cutoff times the indicator that all its positions are balanced is at least \(e^{-Cm}\). This is possible: by the partition of unity, these expectations sum over all centres to the probability that all positions of the group are balanced, which is at least \(2^{-m/2}\) for large \(L\) by collision stability, and only \(e^{O(L)+O(\log m)}\) centres are relevant. In particular \(t_b,t_d=o_k(h)\).

**Targets.** Call the bulk and top positions *protected*. For the full list of two half-lists, define the target \(J\) for the protected positions and the target \(w_j\) for compensation type \(j\) by
\[
\begin{gathered}
\begin{aligned}
J&=2^{-k}\Bigl(\log X-2G-2t_d\\
&\qquad+\Delta_0+\sum_{j=1}^k\Delta_j\Bigr),
\end{aligned}\\
w_j=J+\sum_{i>j}w_i-\frac{\Delta_j}{r_j},\quad(2.1)
\end{gathered}
\]
the second successively for \(j=k,k-1,\dots,1\). Then \(J\asymp h\), \(w_j=(2^{k-j}+o_k(1))J\), and
\[
J+\sum_{j=1}^kw_j=2^kJ-\sum_{j=1}^k\Delta_j .
\]
(The last identity follows from \(\sum_{i\ge j}w_i=J+2\sum_{i>j}w_i-\Delta_j/r_j\) by induction.)

**Centres.** Choose the three top centres in a small relative neighbourhood of \((J-2t_b)/6\), with sum \((J-2t_b)/2+O(1)\), and the two type-\(j\) centres near \(w_j/4\), with sum \(w_j/2+O(1)\). Relative radius \(0.03\) keeps the types, the tops, the bulk, the spectators and the giants in pairwise disjoint prime ranges. All centres can be chosen so that balanced primes form a fixed positive fraction of each cell prior. Indeed, these primes lie below the collision cutoff, a cell in which a fixed fraction is unbalanced contributes a fixed amount to the imbalance term of (4.1) of Lesson 2, and so only \(O(L)\) integer centres can fail, against neighbourhoods of length \(\asymp h\). For a prescribed rounded pair sum, exclude a bad centre and its reflection about the sum. For the triple, choose the first two centres in slightly smaller neighbourhoods; only an \(O(L/h)\) fraction of pairs has a bad third centre. On the bulk cutoff, the protected log sum of each half-list is \(J/2+O(1)\).

**The statistic.** Let \(T(n)\) be the expectation over one half-list of the product of all its tests at \(n\), times its two cutoffs. For \(a\in A'\) and every nongiant prime of the list, \(a\bmod p\in S_p\), so the exact test equals \(F_p(a)=\sqrt{(1-\sigma_p)/\sigma_p}>0\), independently of \(a\). So the expectation of the nongiant tests and the cutoffs is a positive number \(c_L\), independent of \(a\), and \(c_L\ge e^{-Cm}\): restrict every nongiant position to balanced primes, where each value is at least \(2^{-1/2}\), and use the bin and cell choices. Thus
\[
T(a)=c_L\,\mathbb E_{p\sim\mu_G}\widetilde F_p(a)\qquad(a\in A').
\]
Take the weight \(\psi\) of Section 3 of Lesson 3. The tests are real, so \(T(n)^2\ge0\), and Jensen's inequality, (1.4) and \(|A'|\gg\sqrt X/(\log X)^3\) give
\[
\begin{aligned}
I&:=\sum_{n\in\mathbb Z}\psi(n/X)\,T(n)^2\\
&\ge\sqrt X\,e^{-Cm}.\quad(2.2)
\end{aligned}
\]
The logarithmic loss in \(|A'|\) is absorbed because \(\log\log X=O(L)\) and \(m\asymp k^4L\). The argument uses the mean of the giant test and Jensen's inequality, not a pointwise sign of the giant test.

## 3. Repeated primes and the first amplitude

Expand \(T(n)^2\) with two independent half-lists, and let \(M\) be the product of all positions, with multiplicity. On the cutoff support,
\[
\begin{aligned}
\log M&=2G+2t_d+J+\sum_{j=1}^kw_j\\
&\quad +O_k(1)\\
&=\log X+\Delta_0+O_k(1).\quad(3.1)
\end{aligned}
\]

**Repeated primes.** Consider a tuple with a repeated prime, and let \(Q\) be the product of its distinct primes; then \(Q\ll_kXe^{\Delta_0}/\exp(\exp(0.0005L))\)\(=o(X)\). The product of the tests has period \(Q\), and the compact support of \(\widehat\psi\) makes its smoothed sum exactly \(X\widehat\psi(0)\) times its mean over a period. The mean vanishes if some prime occurs exactly once, since every test has mean zero. If a prime occurs \(e\ge2\) times, its local contribution to the absolute mean is at most \(p^{e/2-1}\): every test has probability \(L^2\) norm at most \(1\), hence supremum at most \(\sqrt p\); apply Cauchy–Schwarz to two factors and the supremum bound to the others. This covers different roles at one prime as well.

A prescribed ordered tuple has prior weight at most \(M^{-1}L^{-2m}\exp(Cm+O_k(1))\): the \(2m\) bulk and spectator positions have normalizations \(O(1/L)\), and the \(4k+8\) cell positions together cost \(\exp(O(kL)+O_k(1))\), which is \(\exp(Cm)\) with \(C\) independent of large \(k\) since \(m\asymp k^4L\). Since \(\prod_{p\mid Q}p^{e_p/2-1}=M^{1/2}/Q\) and \(M^{1/2}\ge X^{1/2}e^{\Delta_0/2-O_k(1)}\), the tuples in which every prime occurs at least twice contribute at most
\[
\begin{aligned}
&\sqrt X\exp\bigl(-\tfrac12\Delta_0+Cm+O_k(1)\bigr)L^{-2m}\\
&\quad \sum_{\text{tuples}}\frac1{\prod_{p\ \text{distinct}}p}.
\end{aligned}
\]
With \(b=2m+4k+8\) positions and all prime ranges of harmonic mass \(O(L)\), assigning the positions to \(i\) distinct primes gives \(\sum_{\text{tuples}}\le\sum_{i\le b}i^b(CL)^i/i!\le b^be^{CL}\). So the repeated-prime contribution is at most
\[
\begin{aligned}
&\sqrt X\exp\Bigl(-\frac{\Delta_0}2+(2\log z+C)m\\
&\quad +o_k(m)\Bigr),
\end{aligned}
\]
which is negligible against (2.2) once \(B_s\) is large; the required size of \(B_s\) does not depend on the later gap constants or on large \(k\).

**Proposition 3.1** ([OpenAI-013, (7.6)]). Let \(\eta_0\) be the contribution of the tuples with all positions distinct, divided by \(\sqrt X\). Then
\[
|\eta_0|\ge e^{-B_*m},
\tag{3.2}
\]
for a fixed \(B_*\) independent of \(B_D\), \(B_z\) and \(k\), the same for all sufficiently large admissible \(B_s\). \(\square\)

## 4. Templates, coefficients and support conventions

**The outside list.** Keep the \(m\) spectator positions of the two half-lists, with their original roles, as one *outside list* \(\mathbf d\), and write \(d\) for their product. This list is never duplicated. All other positions form the ordered regular template \(\mathcal I_0\); its two giants are labelled \(+\) and \(-\).

**The steps.** At step \(j\), split \(\mathcal I_{j-1}\) into the pivot and the remaining template \(H\). The pivot product is \(P=pu\), where \(p\) is the \(+\) giant and \(\mathbf u\) is the ordered list of all current compensation positions of type \(j\), with product \(u\). Only the giant \(p\) is extended to the positive integers; the entries of \(\mathbf u\) keep their prime priors. So \(H\) contains the other giant, all protected positions, and all positions of types \(i>j\). Form \(\mathcal I_j=(H_+,H_-)\) from two copies of \(H\), labelling their giants \(+\) and \(-\). Sampled templates use independent copies of the priors. Before step \(j\) there are \(r_j\) copies of the protected list of two half-lists and \(r_j\) copies of each type not yet removed; in particular \(\mathbf u\) has \(4r_j\) positions. On the inherited bins,
\[
\begin{gathered}
\log u=r_jw_j+O_k(1),\\
\log H=T_H+O_k(1),\\
\begin{aligned}
T_H&=G+r_j\Bigl(J+\sum_{i>j}w_i\Bigr)\\
&=G+r_jw_j+\Delta_j .
\end{aligned}\quad(4.1)
\end{gathered}
\]

**Regular transforms.** For a product \(R\) of distinct actual prime values of the template, put
\[
G_R(b)=\prod_{\ell\mid R}g^{\rm reg}_\ell\bigl(b/(R/\ell)\bmod\ell\bigr),
\]
where \(g^{\rm reg}_\ell=\widetilde g_\ell\) at a giant and \(g^{\rm reg}_\ell=g_\ell\) at every other regular position; fractions have unit denominators. It is used only on pairwise coprime support and is set to zero elsewhere. The amplitudes have the form
\[
\begin{gathered}
\begin{aligned}
\eta_l&=\mathbb E_{\mathbf d,\mathcal I_l}\sum_{0<|s|\le V_l}G_R(s/d)\\
&\quad \,A_l(s),
\end{aligned}\\
R=\prod\mathcal I_l .\quad(4.2)
\end{gathered}
\]
The factor \(G_R(s/d)\) depends on the prime values of the template and on their product, so it does not change when the bulk values are rearranged among the bulk positions. The *coefficient* \(A_l\) contains the spectator factors and every weight and support condition that depends on the arrangement. Unlike \(G_R\), it is also defined when its two giant entries are arbitrary positive integers.

**Histories and support.** A history of depth \(l\) is a full binary tree of depth \(l\), with leaves at level \(0\) and a nonzero integer frequency of absolute value at most \(V_i\) at each node of level \(i\). At every state of a history require pairwise coprimality of all its current slots and of the outside list \(\mathbf d\). Require also that its two current giant values be units modulo *every* frequency at that node or below it. These conditions can always be added at an actual top, because actual giant primes exceed all frequencies; once added, they are kept when a giant is extended to the integers. They are imposed termwise on complete histories, cross-branch frequency tests included. A newly inserted pivot is a current giant in its child states, so it is subject to their subtree tests. A failed condition gives zero.

**Level zero.** On this support put
\[
\begin{aligned}
&A_0(s)=\Bigl(\frac X{dR}\Bigr)^{1/2}\widehat\psi\Bigl(-\frac{sX}{dR}\Bigr)\\
&\quad\prod_{\text{halves}}\varphi(S_b-t_b)\varphi(S_d-t_d)\\
&\quad\prod_{q\mid d}g_q\bigl(s/((d/q)R)\bmod q\bigr),\quad(4.3)
\end{aligned}
\]
and zero elsewhere; the spectator bins use the original roles. Then (4.2) with \(l=0\) is the distinct-tuple Poisson formula: writing every test as \(p^{-1/2}\sum_bg(b)e_p(bx)\), the Chinese remainder theorem combines the local frequencies into one frequency \(s\) modulo \(dR\), with local value \(s/((dR)/p)\) at \(p\); the inverse expansions contribute \((dR)^{-1/2}\), and Poisson summation followed by division by \(\sqrt X\) gives \(\sqrt{X/(dR)}\,\widehat\psi(-sX/(dR))\). The zero frequency vanishes because \(g_p(0)=0\). On the cutoffs \(dR/X=e^{\Delta_0+O_k(1)}\), so the term \(2^0\sqrt m\) in \(E_0\) accommodates the support of \(\widehat\psi\).

**The recursion.** For \(j\ge1\), a current state is \(\mathcal I_j=(H_+,H_-)\) with root frequency \(s\). Sum over \(0<|v|,|w|\le V_{j-1}\), sample the type-\(j\) vector \(\mathbf u\) from its priors, and restore the pivot by
\[
p=\frac{vH_--wH_+}{su},
\tag{4.4}
\]
retaining it only if it is a positive integer. The two child states are copies of \(\mathcal I_{j-1}\) with entries \((p,\mathbf u,H_+)\) and \((p,\mathbf u,H_-)\) in their roles; their giant pairs, in order, are the inserted \(p\) and the giant of \(H_+\), respectively \(H_-\). Keep the same \(\mathbf d\). Then
\[
\begin{aligned}
&A_j(s;\mathbf d,H_+,H_-)\\
&\quad =\sum_{\substack{0<|v|\le V_{j-1}\\0<|w|\le V_{j-1}}}\mathbb E_{\mathbf u}\Bigl[u\,\varphi(\log p-G)\\
&\qquad \,A_{j-1}(v;\mathbf d,p,\mathbf u,H_+)\\
&\qquad \,\overline{A_{j-1}(w;\mathbf d,p,\mathbf u,H_-)}\Bigr],\quad(4.5)
\end{aligned}
\]
interpreted termwise after expanding the two child histories, and zero unless (4.4) and all support conditions hold. The internal samples of the two children are independent; only \(\mathbf u\) at the present node is shared. No transform is attached to an integer giant.

## 5. The exact transfer and its diagonal

Fix \(\mathbf d,p,\mathbf u\) at step \(j\), put \(P=pu\), and group the terms of \(\eta_{j-1}\) by \(t\equiv v/H\pmod P\). On prime support, \(G_{PH}(v/d)=G_P(t/d)\,G_H(v/(Pd))\). Let
\[
B_t=\mathbb E_H\sum_{\substack{0<|v|\le V_{j-1}\\v/H\equiv t\ (P)}}G_H\bigl(v/(Pd)\bigr)A_{j-1}(v),
\]
with all inherited conditions. The extracted row satisfies \(\sum_{t\bmod P}|G_P(t/d)|^2\le P\), by the Chinese remainder theorem and the bounds \(\mathbb E|g_\ell|^2=1\), \(\mathbb E|\widetilde g_p|^2\le1\). Cauchy–Schwarz in \(t\), then Jensen's inequality over the outer probability measures, give \(|\eta_{j-1}|^2\le\mathbb E_{\mathbf d,p,\mathbf u}P\sum_t|B_t|^2\). The quantity \(B_t\) contains no transform of the pivot giant \(p\), so it is defined by the same formulas for any positive integer \(p\). By (1.5), \(p\,\mu_G(p)=e^{c_g}\varphi(\log p-G)\) at primes, and extending the nonnegative sum to all positive integers,
\[
\begin{aligned}
|\eta_{j-1}|^2&\le e^{c_g}\,\mathbb E_{\mathbf d,\mathbf u}\sum_{p\ge1}u\,\varphi(\log p-G)\\
&\qquad\sum_{t\bmod pu}|B_t|^2 .\quad(5.1)
\end{aligned}
\]

Expand the square with independent \(H_+,H_-\) and child frequencies \(v,w\). The terms with \(vH_-=wH_+\) form the *diagonal* \(\mathcal D_j\). For every other term the congruence of the two residues defines the nonzero integer \(s=(vH_--wH_+)/(pu)\), so the substitution is exactly (4.4), one-to-one, with \(p\) any positive integer in its cell. By (1.1) and (4.1), \(\log|s|\le E_{j-1}+\Delta_j+O_k(1)<E_j\), with margin \(2^{j-1}\sqrt m\to\infty\).

On such a term, \(H_+\) and \(H_-\) share no prime: a common prime \(\ell\) would divide \(spu\), be coprime to \(pu\), hence divide \(s\), but \(\ell>|s|\). At primes of \(H_+\) and of \(H_-\), (4.4) gives \(v/P\equiv s/H_-\) and \(-w/P\equiv s/H_+\). The tests are real, so \(g^{\rm reg}_\ell(-b)=\overline{g^{\rm reg}_\ell(b)}\), and the two regular transforms combine into \(G_{H_+H_-}(s/d)\). The remaining weights, histories and the inserted pivot are exactly the recursive definition (4.5). The giant-frequency conditions at the new top hold automatically, since its giants are actual primes. So the off-diagonal part of (5.1), before the factor \(e^{c_g}\), is exactly \(\eta_j\).

**Proposition 5.1** (the transfer [OpenAI-013, (7.13)]). For \(1\le j\le k\),
\[
e^{-c_g}|\eta_{j-1}|^2\le\mathcal D_j+\eta_j,
\tag{5.2}
\]
where the diagonal \(\mathcal D_j\) is nonnegative, and \(\eta_j\) is real.

*Proof of nonnegativity.* On the diagonal every prime of \(H_\pm\) exceeds the frequencies, so \(vH_-=wH_+\) forces \(H_+=H_-\) as products and \(v=w\). Group the terms by this common product and frequency *before* expanding the square: each group is \(|G_H(v/(pud))|^2\) times the squared modulus of the prior-weighted sum of the coefficients over the arrangements with that product. The common factor does not depend on the arrangement: each prime uses the same local transform in every arrangement, and the single giant of \(H\) is fixed by its separate range. The extended sum is a sum of squared moduli, so \(\eta_j\) is real. \(\square\)

**Normalizing the diagonal.** Drop the bounded giant factor from the nonnegative diagonal. The remaining transform factor is
\[
\begin{aligned}
\mathcal G&=\prod_{\ell\mid H_{\rm sm}}\Bigl|g_\ell\bigl(v/(pud(H/\ell))\\
&\quad \bmod\ell\bigr)\Bigr|^2,\quad(5.3)
\end{aligned}
\]
where \(H_{\rm sm}\) consists of the small slots of \(H\). Expand by the bijections matching the slots of the two copies of \(H\); this counts every ordered counterpart once, since the primes of a valid \(H\) are distinct. Only matches within one prime band occur; the giant matches itself and bulk positions match bulk positions. Fix a first ordered \(H\). A prescribed counterpart ordering has point probability \(C_H/H\) times its smooth cell factors and role indicators, with
\[
\begin{aligned}
C_H&\le L^{-r_jm}\exp\bigl(Cr_jm\\
&\quad +O_k(1)\bigr),\quad(5.4)
\end{aligned}
\]
since there are \(r_jm\) bulk positions and \(O(kr_j)\) cell positions, whose normalizations cost \(\exp(O(kr_jL))\le\exp(Cr_jm)\). On the common support, (4.1) allows extracting \(C_He^{-T_H}\), leaving \(e^{T_H}/H=O_k(1)\). Normalize the *external integer measure* by
\[
\begin{aligned}
&\int f\,d\mu_{\rm ext}=e^{-G}\\
&\qquad \sum_{p\ge1}\varphi(\log p-G)\\
&\qquad f(p),\quad(5.5)
\end{aligned}
\]
of bounded total mass. Extracting \(e^G\) from it and \(e^{r_jw_j}\) from \(u\) leaves the scalar \(C_He^{-\Delta_j}\), and the remaining factor
\[
\begin{aligned}
K_{\rm ar}&=\frac{e^{T_H}}H\cdot\frac u{e^{r_jw_j}}\\
&\quad \prod_{\text{counterpart cells}}\varphi(\log p_i-c_i)
\end{aligned}
\]
is \(O_k(1)\) on the common support. The counterpart role indicators are kept as zero conventions.

## 6. The comparison estimates

At level \(l\) put \(r=2^l\). The coefficient \(A_l\) has \(r\) bottom leaves, each carrying the \(m\) bulk positions of the initial full list, and its \(m\) spectator positions are shared by all leaves. There are two outer environments, both with the priors, the integer extension, the coefficients and the support conventions above.

- **(a) The final environment.** \(l=k\), the list \(\mathcal I_k\) with its actual prime priors, and \(\mathcal G=1\), \(K_{\rm ar}=1\). A pair of *assignments* may permute all \(rm\) bulk values among their labelled positions; the other positions and \(\mathbf d\) are common.
- **(b) The diagonal environment of step \(j\).** \(l=j-1\). The current \(+\) giant \(p\) has the external measure (5.5); all other current slots, including the type-\(j\) vector \(\mathbf u\), have their prime priors. \(\mathcal G\) is (5.3) with \(v=s\), with the zero convention on invalid top support. In a pair of assignments, the first uses the ordered \(H\) and the second a prescribed same-band matching of its slots, with \(p,\mathbf u,\mathbf d\) unchanged; the factor \(K_{\rm ar}\) is included, with the counterpart role indicators. For the norm of a single assignment, \(K_{\rm ar}\) is omitted.

The expectation in (b) includes the bounded-mass measure (5.5), which need not be a probability measure. All root-frequency sums are over \(0<|s|\le V_l\).

**The overlap graph.** For a pair of assignments, form the bipartite multigraph whose two vertex sets are the \(r\) bottom leaves of each assignment; each bulk variable is an edge joining the leaf containing it in the first assignment to the leaf containing it in the second. Every vertex has degree \(m\). The graph depends only on the slot assignments, not on the sampled values or the histories.

**Proposition 6.1** (comparison estimates [OpenAI-013, Proposition 7.1]). In either environment, uniformly over the indicated assignments: for one assignment,
\[
\begin{aligned}
&\mathbb E\sum_{0<|s|\le V_l}\mathcal G\\
&\qquad \,|A_l(s)|^2\\
&\quad \le\exp\bigl(r(\Delta_0+Cm)\\
&\qquad +o_k(m)\bigr),\quad(6.1)
\end{aligned}
\]
with \(C\) independent of large \(k\) and of the gap constants; and for a pair of assignments with \(l\ge2\) whose overlap graph has at most \(3r/4\) connected components,
\[
\begin{aligned}
&\Bigl|\mathbb E\sum_{0<|s|\le V_l}\mathcal G\,K_{\rm ar}\,A^{(1)}_l(s)\\
&\qquad \,\overline{A^{(2)}_l(s)}\Bigr|\le\exp(-\omega_k(m)),\quad(6.2)
\end{aligned}
\]
where \(\omega_k(m)/m\to\infty\) as \(L\to\infty\) for every fixed choice of the other parameters.

The coprimality and giant-frequency conditions are part of the definitions, used in the proof, not additional conclusions. The outside list is never resampled, within a coefficient or between the two coefficients of a pair. The two coefficients have independent internal samples; within one coefficient, a sample at a node is shared by its two children, as in (4.5). Coincidences among independently sampled internal primes are allowed when the support permits them; Lesson 15 sums their equality patterns explicitly.

Lessons 15–17 prove Proposition 6.1. The mechanism of (6.2) is the spectators: at a spectator prime the coefficient \(A_l\) reduces to a diagram of Lesson 12, and when few components connect the leaves of the two assignments, the tree comparison of Lessons 12–13 makes the correlation at each spectator small; the \(m\) spectators are independent, so the bound is raised to the power \(m\).

## 7. Exercises

**7.1.** Show that a smooth nonnegative \(\varphi\) supported in \([-1,1]\) with \(\sum_n\varphi(t-n)=1\) exists, and that it satisfies \(\int\varphi=1\).

**7.2.** Verify \(J+\sum_jw_j=2^kJ-\sum_j\Delta_j\) from (2.1), and \(w_j=(2^{k-j}+o_k(1))J\).

**7.3.** Verify (3.1) from (2.1) and the bins.

**7.4.** Show that \(\sum_{t\bmod P}|G_P(t/d)|^2\le P\) for squarefree \(P\) coprime to \(d\), given \(\mathbb E_x|g^{\rm reg}_\ell(x)|^2\le1\) at each \(\ell\mid P\).

## 8. Solutions

**7.1.** Take a smooth \(\theta\ge0\) supported in \([-1,1]\), positive on \([-\frac12,\frac12]\). Then \(\Theta(t)=\sum_n\theta(t-n)\) is smooth, periodic and positive, and \(\varphi=\theta/\Theta\) works. Integrating \(\sum_n\varphi(t-n)=1\) over \([0,1]\) gives \(\int_{\mathbb R}\varphi=1\).

**7.2.** Let \(S_j=\sum_{i\ge j}w_i\). Then \(S_j=w_j+S_{j+1}=J+2S_{j+1}-\Delta_j/r_j\), with \(S_{k+1}=0\), so \(S_1=\sum_j2^{j-1}(J-\Delta_j/r_j)\)\(=(2^k-1)J-\sum_j\Delta_j\), using \(r_j=2^{j-1}\). For the asymptotic, \(\Delta_j=O_k(L)=o(J)\), and \(w_j=J(1+\sum_{i>j}2^{k-i})+o(J)\)\(=2^{k-j}J+o(J)\) by downward induction.

**7.3.** The two giants contribute \(2G+O(1)\), the two spectator groups \(2t_d+O(1)\), the protected positions of the two halves \(J+O(1)\), and the compensation positions of type \(j\) \(w_j+O(1)\). By (2.1), \(2G+2t_d+J+\sum w_j\)\(=2G+2t_d+2^kJ-\sum\Delta_j\)\(=\log X+\Delta_0\).

**7.4.** By the Chinese remainder theorem, as \(t\) runs modulo \(P\), the residues \(t/(d(P/\ell))\bmod\ell\) run independently over \(\mathbb F_\ell\), since \(d(P/\ell)\) is a unit modulo \(\ell\). So the sum factors as \(\prod_{\ell\mid P}\sum_{x\in\mathbb F_\ell}|g^{\rm reg}_\ell(x)|^2\le\prod_\ell\ell=P\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 7: scales and prime priors, (7.1)–(7.2), the initial lists and positive statistic (7.4)–(7.5), repeated primes (7.6), templates and coefficients (7.7)–(7.11), the exact transfer and its diagonal (7.12)–(7.14), and Proposition 7.1. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
