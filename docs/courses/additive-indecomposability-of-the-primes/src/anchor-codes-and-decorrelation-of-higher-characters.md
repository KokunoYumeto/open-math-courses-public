# Anchor codes and decorrelation of higher characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the two remaining estimates for Theorem 1.1 of Lesson 7 and derives the mixed flatness of the normalized Fourier transforms of the supports \(S_p\) (Theorem 6.1), the form in which Lessons 3–9 are used later. Two estimates remain. The diagonal terms \(\mathcal D_j\) of the transfers must be small, so that the lower bound \(|\eta_0|\ge e^{-B_0m}\) survives \(k\) transfers. And at the last level, rearranging the bulk variables among the \(2^k\) copies of the word must produce nearly orthogonal terms, which forces \(\eta_k\) to be small. Both rest on one mechanism. Every copy of a bulk slot carries a *code*, read off from its exponents towards the anchors. When two terms place the same bulk prime in slots with different codes, the quotient of their phases contains the square of a character of order greater than \(2\), evaluated in one direction only between a short and a long prime. Such a one-sided interaction averages out (Lemma 1.2).

**Prerequisites.** [*Templates, transfers and frequency histories*](templates-transfers-and-frequency-histories.md); [*A biased block and an amplified moment*](a-biased-block-and-an-amplified-moment.md), Corollary 1.2; [*Square-root bounds and collision stability*](square-root-bounds-and-collision-stability.md), Lemma 4.1.

The notation of Lessons 7 and 8 is in force.

## 1. One-sided interactions

**Lemma 1.1** (zeros of polynomials under independent sampling). Let \(N\) be a nonzero polynomial of total degree at most \(D\) in independent random variables \(x_1,\dots,x_n\), each taking any single value with probability at most \(\alpha\). Then \(\Pr(N(x_1,\dots,x_n)=0)\le D\alpha\).

*Proof.* Induct on \(n\); for \(n=0\), \(N\) is a nonzero constant. Write \(N=\sum_{i\le d}c_i(x_1,\dots,x_{n-1})x_n^i\) with \(c_d\ne0\), of total degree at most \(D-d\). By induction \(\Pr(c_d=0)\le(D-d)\alpha\). If \(c_d\ne0\), \(N\) is a nonzero polynomial of degree \(d\) in \(x_n\), with at most \(d\) roots, and \(x_n\) is independent of the other variables, so the conditional probability of a root is at most \(d\alpha\). \(\square\)

This is the classical argument of Schwartz and Zippel, here for arbitrary independent laws with a bound on the largest atom.

We compare two terms in one of the following two settings.

- **(a)** Two terms of the final amplitude \(\eta_k\) whose top lists differ by a rearrangement of the bulk variables among the bulk slots, with the same root frequency.
- **(b)** Two terms of the diagonal \(\mathcal D_j\): a fixed positive integer \(P\) in place of the pivot, a common root frequency \(v=w\), and a fixed matching that identifies the primes of \(H_L\) with those of \(H_R\), while \(Y\) is shared.

Fix every frequency of both histories and the rearrangement or matching. In setting (b) only the variables of \(H_L\) and \(Y\) are sampled; the matched counterpart's prior weight is extracted separately below. In both settings the two terms use the same set of primes and the same root frequency, and the additive phase \(A_{\mathcal I}\) of (2.1) of Lesson 8 depends only on these. So the additive phases cancel in the quotient \(\Theta^{(1)}\overline{\Theta^{(2)}}\). On the diagonal, the removed pivot factors are removed on both sides, with the same \(P\).

**Lemma 1.2** (one-sided interactions [OpenAI-013, (4.11)]). Suppose that the quotient phase contains, between a *short* prime \(q\) and a *long* prime \(p\) whose level ranges are separated by \(\gg L\), a factor \(\xi_q(p)\) with \(\xi_q\) a nonprincipal character modulo \(q\), and no factor in the reverse direction between this pair. Then the weighted expectation of the product of the two terms is
\[
O\bigl(\exp(-c_2e^{\alpha L})\bigr)
\tag{1.1}
\]
for some \(c_2>0\), uniformly in the fixed data. Bounded unary restrictions coming from the counterpart priors are permitted, and so is the factor \(e^{T_j+\Delta_j}/H_L\) on the range (2.2) of Lesson 8. The bound (1.1) can be summed over all histories and matchings of fixed depth, whose number is at most \(\exp(\mathrm{poly}_k(m))\).

*Proof.* *Large coprimality conditions.* At the top, the atoms must be pairwise coprime, internally distinct where required, and coprime to the external integer when there is one. At a lower node, the inserted pivot \(P=(vH_R-wH_L)/s\) is automatically coprime to each atom of \(H_L\) and \(H_R\): a common prime factor with an atom of \(H_L\) would divide \(vH_R\), but \(H_R\) is coprime to \(H_L\), and the factor does not divide \(v\), by size for actual primes and by the retained frequency conditions for earlier pivots. An inserted pivot always occupies an active pivot position, so it lies in one of \(H_L,H_R\) at every later step, never in \(Y\). So the slots of \(Y\) carry actual primes, and the only large coprimality conditions that are not automatic are between a reconstructed pivot and the actual primes of its \(Y\), together with the top conditions.

*Removing them.* Express each reconstructed integer by repeated substitution of (3.2) of Lesson 8. Clearing denominators, which are products of frequencies, its numerator is a polynomial in the independent actual prime variables of \(H_L\) and \(Y\); in setting (b) a matched prime is one variable. For fixed \(k\), the degrees are bounded by a polynomial in \(m\), and the absolute values have logarithm at most \(\exp(O_k(L))\), also after setting a variable to zero. For a required coprimality with a prime variable \(x\), set \(x=0\) in the numerator. If the result vanishes identically, \(x\) divides the numerator for every assignment, the denominator is a unit modulo \(x\), and the condition fails identically: the pair of histories contributes nothing. Otherwise, by Lemma 1.1 the evaluation vanishes with probability at most its degree times the largest point mass, which is at most \(\exp(-ce^{\alpha L})\) for every prime prior here; the priors with internal restrictions are dominated by the unrestricted ones. On a nonzero evaluation there are at most \(\exp(O_k(L))\) prime divisors, and \(x\) is independent of the evaluation, so \(x\) divides it with probability at most \(\exp(O_k(L)-ce^{\alpha L})\). The same argument handles collisions at the top and coprimality with the external integer. All these failures are negligible even after multiplication by \(\exp(\mathrm{poly}_k(m))\). The removal is made after the additive phases have cancelled, so on the enlarged domain the multiplicative factors may take any bounded value at nonunits.

*The remaining conditions.* The integrality and small-frequency gcd conditions are congruences modulo an integer \(Q_*=\exp(O_k(m))\) whose prime factors divide the frequencies, so every actual prime is coprime to \(Q_*\). The other conditions are polynomial inequalities after the substitutions: product ranges, pivot ranges, positivity and the word bins. Fix all variables except \(p\), and fix \(q\). On a dyadic interval for \(p\), cut at the boundary points of these inequalities and at the critical points of the polynomial arguments of the smooth factors; there are at most \(\mathrm{poly}_k(m)\) cuts, and on each piece the arguments are monotone. The level-zero weights \((X/M)^{1/2}\widehat\psi(vX/M)\) on their ranges, their products, and the factor \(e^{T_j+\Delta_j}/H_L\) then have supremum and total variation at most \(\exp(\mathrm{poly}_k(m))\) as functions of \(p\), in every residue class modulo \(Q_*\).

*The character sum.* With the other variables fixed, the expectation has the form
\[
\begin{gathered}
\mathbb E_p\,\mathbb E_q\,U(p)\,V(q)\,\xi_q(p)\,W(p,q),\\
|U|,|V|\le1,
\end{gathered}
\]
with the congruence conditions included in \(W\). By Cauchy–Schwarz in \(p\) the factor \(U\) disappears, and the nonnegative square can be extended from the prior of \(p\) to all integers \(n\) in its range, with weight \(e^{CL}/n\). Expand the square in \(q,q'\). The terms \(q=q'\) contribute at most the largest point mass of the short prior times \(\exp(\mathrm{poly}_k(m))\). For \(q\ne q'\), \(n\mapsto\xi_q(n)\overline{\xi_{q'}(n)}\) is a nonprincipal character modulo \(qq'\), so it has mean zero over every complete period, also along a progression of step \(Q_*\), because \(Q_*\) is coprime to \(qq'\). Over a progression in a dyadic interval \([b,2b]\), partial summation against a weight of supremum and variation \(\exp(\mathrm{poly}_k(m))/b\) bounds the sum by \(qq'\exp(\mathrm{poly}_k(m))/b\), and summing the \(Q_*\) classes gives
\[
\exp(\mathrm{poly}_k(m))\,\frac{Q_*\,qq'}b .
\]
Since the levels are separated by \(\gg L\), \(\log b\ge e^{c'L}\log q\), while \(\log Q_*=O_k(L)\) and \(\log b\ge e^{\alpha L}\). So this is at most \(\exp(-\frac12e^{\alpha L})\), and there are \(e^{O(L)}\) dyadic intervals. Taking square roots proves (1.1). \(\square\)

## 2. Anchor codes

An active bulk slot at level \(l\) has a *path* \(t=(t_1,\dots,t_l)\in\{1,-1\}^l\), the copy signs of the transfers that produced it. Write
\[
e_0=1,\qquad e_j=\prod_{h\le j}t_h,\qquad\varepsilon(t)=e_l,
\]
so \(\varepsilon(t)\) is the regular sign of Lesson 8. For an anchor clone \(y\) created at one of the first \(l\) steps, its *code coordinate* at the slot is
\[
c_y(t)=\frac{b_{yi}}{\varepsilon(t)},
\]
where \(i\) is a bulk slot with path \(t\). All bulk slots of one active word are treated alike by the update rule, so the coordinate depends only on the path. The *code* of the path is the vector of all these coordinates.

**Lemma 2.1** (anchor codes [OpenAI-013, (4.12)]). Let \(a\) be an anchor reserved for step \(j\). Its two clones \(a^+,a^-\) have, at a bulk path \(t\) of length at least \(j\),
\[
\begin{aligned}
&\bigl(c_{a^+}(t),c_{a^-}(t)\bigr)\\
&\quad=\begin{cases}
(1,\,-1/e_{j-1}),&t_j=1,\\
(-1/e_{j-1},\,1),&t_j=-1,
\end{cases}
\end{aligned}
\]
and these coordinates do not change at later steps. The small and the big anchor of step \(j\) have the same coordinates. Consequently every code occurs on at most two paths, and the code together with the final sign \(\varepsilon(t)\) determines the path.

*Proof.* At level zero all exponents are \(1\). Until step \(j\) the anchor is outside, and by (3.3) of Lesson 8 each transfer multiplies its row towards a bulk slot by the copy sign of the target; so before step \(j\), \(b_{ai}=e_{j-1}\) for a bulk slot \(i\) of path \((t_1,\dots,t_{j-1})\). The active pivot of type \(K_j\) has always been kept in the copy \(H^+\), so the anchor's column into it is \(b_{aP}=1\). At step \(j\) the anchor lies in \(H\), and (3.3) gives, for the new bulk slot \(i^{t_j}\),
\[
\begin{gathered}
b_{a^+i^+}=e_{j-1},\\
b_{a^+i^-}=b_{aP}=1,\\
b_{a^-i^-}=-e_{j-1},\\
b_{a^-i^+}=-b_{aP}=-1.
\end{gathered}
\]
Dividing by \(\varepsilon=e_{j-1}t_j\) gives the stated pairs. Afterwards the clones are outside, and each transfer multiplies both \(b_{yi}\) and \(\varepsilon_i\) by the same sign, so the coordinates are fixed. The two anchors of step \(j\) follow identical rules.

The pair is \((1,1)\) exactly when \(e_{j-1}=-1\), and is \((1,-1)\) or \((-1,1)\) when \(e_{j-1}=1\). So the anchors of step \(j\) determine \(e_{j-1}\), and all anchors of steps \(1,\dots,l\) determine \(e_0,\dots,e_{l-1}\), hence \(t_1,\dots,t_{l-1}\). Only \(t_l\) may remain undetermined, and it is fixed by \(\varepsilon(t)=e_l\). \(\square\)

## 3. The diagonal bound

Consider the diagonal \(\mathcal D_j\) of step \(j\); put \(l=j-1\) and \(r=2^l\). As noted after Proposition 3.2 of Lesson 8, its terms have \(H_L=H_R\) as integers and \(v=w\). Within each branch the primes are distinct, so equality of the products gives a unique matching of the slots of \(H_L\) with those of \(H_R\) carrying the same primes; sum over these matchings. Bulk slots can only match bulk slots, because the bulk level range is separated from every other role in \(H\), and matched bulk slots have the same character rule.

**Normalization.** For a fixed assignment of \(H_L\), the prior weight of a prescribed matched counterpart is \(C_H/H_L\) times its role and distinctness indicators, where
\[
\begin{aligned}
C_H&\le L^{-rm}\exp\bigl(Crm+O_k(1)\bigr)\\
&:\quad(3.1)
\end{aligned}
\]
there are \(rm\) bulk priors with normalization \(O(1/L)\), \(r\) top priors with bounded normalization, and \(O(n_c)\) cell priors costing at most \(e^{Cn_cL}\). Before summing over the external integer \(P\), extract \(C_He^{-T_j-\Delta_j}\). The remaining ratio \(e^{T_j+\Delta_j}/H_L\) is bounded on (2.2) of Lesson 8. There are at most \(e^{T_j+O_k(1)}\) values of \(P\), which cancels the factor \(e^{-T_j}\). Extracting the normalization first avoids multiplying a small uniform error by the doubly exponential number of \(P\).

**Code-changing matchings.** Suppose a matching sends a bulk slot of \(H_L\), of path \(t\), to a bulk slot of \(H_R\) of path \(t'\) with a different code. Choose an anchor \(y\) of an earlier step whose coordinates differ: \(c'=-c\), with \(c=c_y(t)\), \(c'=c_y(t')\). The anchor is in the shared list \(Y\). Let \(p\) be the bulk prime and \(q\) the anchor prime, and \(\varepsilon,\varepsilon'\) the signs of the two paths. In the quotient phase, the exponent of the anchor's character at \(p\) is \(\varepsilon c-\varepsilon'c'\), and the exponent of the bulk character \(\chi^{(p)}\) at \(q\) is \(\varepsilon-\varepsilon'\).

- If \(\varepsilon=\varepsilon'\), the exponents are \((\pm2,0)\). Take \(y\) to be the *small* anchor of that step; it lies below the bulk range. The interaction is \(\lambda_y(p)^{\pm2}\), one-sided from the short prime \(q\) to the long prime \(p\).
- If \(\varepsilon\ne\varepsilon'\), the exponents are \((0,\pm2)\). Take the *big* anchor of the same step; it lies above the bulk range. The interaction is \(\chi^{(p)}(q)^{\pm2}\), one-sided from the short prime \(p\) to the long prime \(q\).

Lemma 2.1 guarantees that the small and big anchors have the same codes, so both choices are available. In either case the character squared is nonprincipal, because every character used has order greater than \(2\). All other factors are unary once the other variables are fixed. By Lemma 1.2, summed over \(P\), matchings and histories with the normalization above, the code-changing matchings contribute a negligible amount.

**Code-preserving matchings.** By Lemma 2.1 a bulk slot has at most \(2m\) possible counterparts of the same code: at most two paths share its code, each with \(m\) bulk positions. The other slots are boundedly many for fixed \(k\). So there are at most \((2m)^{rm}e^{O_k(1)}\) code-preserving matchings. Fix \(P\) and such a matching. For each common root frequency, Lemma 4.1 of Lesson 8 leaves at most one valid history on each branch. Bound the phases by \(1\) and use \(2|W_lW'_l|\le|W_l|^2+|W'_l|^2\) on the common support. In each of the two terms, bound the prior weight of the other branch by \(C_H\exp(-T_j-\Delta_j+O_k(1))\) and keep the square branch's own priors; Proposition 5.1 of Lesson 8, in its fixed-external version, bounds the frequency sum by \(\exp(Crm+o_k(m))\). Summing over \(P\) and the matchings, and using \(m/L=z+o(1)\),

**Proposition 3.1** (the diagonal [OpenAI-013, (4.13)]). For \(1\le j\le k\) and \(r=2^{j-1}\),
\[
\begin{aligned}
|\mathcal D_j|&\le\exp\bigl(-\Delta_j+rm(\log z+C)\\
&\quad +o_k(m)\bigr)\\
&\quad +O\bigl(\exp(-c_2e^{\alpha L}/2)\bigr),
\end{aligned}
\]
with \(C\) independent of \(k\) and \(B_D\). \(\square\)

## 4. The amplitude induction

The constants are chosen in this order. The constant \(B_0\) of Proposition 6.1 of Lesson 7 does not depend on \(B_D\) or \(k\).

1. Choose \(B_1>B_0+2\).
2. Choose \(B_D\) so large that the repeated-prime estimate of Lesson 7 holds and the main term of Proposition 3.1 is at most \(\frac12e^{-d_j}e^{-2B_1rm}\) whenever \(d_j\le m\). This is possible uniformly in \(k\): the main term has exponent \(-\Delta_j+rm(\log z+C)\)\(\le-rm(B_D+19\log z-C)\).
3. Increase \(K_0\) so that \(\sum_{j\le k}d_j\le Cn_cL+O_k(1)<m\) for large \(L\); this follows from \(n_c/z\ll ke^{-\epsilon k}\).

**Proposition 4.1** ([OpenAI-013, (4.14)]). For large \(L\),
\[
|\eta_l|\ge\exp\bigl(-B_1\,2^lm\bigr)\qquad(0\le l\le k).
\]

*Proof.* If \(|\eta_{j-1}|\ge e^{-B_1rm}\) with \(r=2^{j-1}\), Proposition 3.2 of Lesson 8 and Proposition 3.1 give
\[
\eta_j\ge e^{-d_j}|\eta_{j-1}|^2-|\mathcal D_j|\ge\tfrac12e^{-d_j}|\eta_{j-1}|^2 .
\]
Put \(\mathfrak a_j=-2^{-j}m^{-1}\log|\eta_j|\). Then \(\mathfrak a_j\le\mathfrak a_{j-1}+(d_j+\log2)/(2^jm)\), so
\[
\begin{aligned}
\mathfrak a_j&\le B_0+\sum_{h\le j}\frac{d_h+\log2}{2^hm}\\
&\le B_0+1+o_k(1)<B_1,
\end{aligned}
\]
which is the induction hypothesis at the next step. Proposition 6.1 of Lesson 7 starts the induction. \(\square\)

## 5. The final permutation comparison

At level \(k\) put \(r=2^k\). For each of the \(m\) bulk positions of the word, permute its \(r\) variables, one in each active word, among the paths with the same final sign. There are \(r/2\) paths of each sign, so there are
\[
J_*=\bigl((r/2)!^2\bigr)^m
\]
such *reassignments*. The bulk priors are identical and independent, so every reassignment preserves the joint law. The bins and all other conditions are part of the integrand; they never conditioned the priors.

Let \(\mu\) be the product of the priors of the final list with counting measure on \(0<|s|\le V_k\); its total mass is at most \(2V_k\). For a reassignment \(\pi\), let \(\Phi_\pi\) be the sum over internal histories of the final term with the bulk variables placed by \(\pi\). Invariance of the priors gives \(\int\Phi_\pi\,d\mu=\eta_k\). By Lemma 4.1 and Proposition 5.1 of Lesson 8,
\[
\|\Phi_\pi\|_{L^2(\mu)}^2\le\exp\bigl(Crm+o_k(m)\bigr).
\]
If \(\pi\ne\rho\), some bulk variable occupies different paths of the same final sign under \(\pi\) and \(\rho\); by Lemma 2.1 these paths have different codes, and the first case of Section 3, with a small anchor, gives a one-sided square-character interaction. The additive phases cancel, since both terms use the same primes, root frequency and centres. Lemma 1.2, summed over the frequency data, gives
\[
|\langle\Phi_\pi,\Phi_\rho\rangle_{L^2(\mu)}|\ll\exp(-c_2e^{\alpha L}).
\]
Let \(\overline\Phi=J_*^{-1}\sum_\pi\Phi_\pi\). Then \(\int\overline\Phi\,d\mu=\eta_k\), and Cauchy–Schwarz against the constant function \(1\) gives
\[
\begin{aligned}
|\eta_k|^2&\le2V_k\|\overline\Phi\|^2\\
&\le2V_k\Bigl(\frac{\exp(Crm+o_k(m))}{J_*}\\
&\quad +O\bigl(\exp(-c_2e^{\alpha L})\bigr)\Bigr).\quad(5.1)
\end{aligned}
\]

**Completion of the proof of Theorem 1.1 of Lesson 7.** By Stirling's formula, \(\log J_*=2m\log((r/2)!)\)\(\ge rm(k\log2-C)\). By (5.1) of Lesson 7, \(\log V_k=E_k\)\(=rm(B_D+20\log z)+o_k(m)\), and \(20\log z=60\epsilon k\). Since \(\log2-60\epsilon>0\), a large \(K_0\), chosen after \(B_D\) and \(B_1\), makes the first term on the right of (5.1) at most \(\exp(-(2B_1+1)rm)\). The second term, with its factor \(2V_k=\exp(O_k(m))\), is smaller than \(\exp(-Crm)\) for every fixed \(C\) once \(L\) is large. So \(|\eta_k|^2<\exp(-2B_1rm)\), contradicting Proposition 4.1 with \(l=k\). This contradiction proves Theorem 1.1 of Lesson 7. \(\square\)

## 6. Mixed flatness

For the balanced-transform form used in the rest of the course, define for every prime \(p\)
\[
\begin{gathered}
F_p(x)=\frac{\mathbf 1_{S_p}(x)-\sigma_p}{\sqrt{\sigma_p(1-\sigma_p)}},\\
\begin{aligned}
g_p(v)&=\sqrt p\;\mathbb E_{x\in\mathbb F_p}F_p(x)\\
&\quad \,e_p(-vx).
\end{aligned}\quad(6.1)
\end{gathered}
\]
Then \(\mathbb E_xF_p(x)=0\), \(\mathbb E_x|F_p(x)|^2=1\), \(g_p(0)=0\), \(\frac1p\sum_v|g_p(v)|^2=1\) by Parseval, and \(g_p(-v)=\overline{g_p(v)}\).

**Theorem 6.1** (mixed flatness [OpenAI-013, Corollary 4.2]). Let \(0<\alpha<\beta\) be fixed. Outside a set of primes of harmonic mass \(o(L)\) in the band \(\alpha L\le\log\log p\le\beta L\), uniformly,
\[
\begin{gathered}
\sigma_p=\tfrac12+o(1),\\
\begin{aligned}
&\max_{\substack{a\in\mathbb F_p\\\lambda}}\Bigl|\mathbb E_{v\in\mathbb F_p}g_p(v)\,\lambda(v)\\
&\qquad \,e_p(av)\Bigr|=o(1),
\end{aligned}\quad(6.2)
\end{gathered}
\]
where \(\lambda\) runs over all multiplicative characters of \(\mathbb F_p\), including the principal one, extended by zero at zero.

*Proof.* *Balance.* Apply Lemma 4.1 of Lesson 2 with \(\log X=\exp((\beta+1)L)\); its prime cutoff contains the whole band. Dividing its imbalance term by \(\log p\ge e^{\alpha L}\) gives
\[
\begin{aligned}
&\sum_{\alpha L\le\log\log p\le\beta L}\frac1p\Bigl(\frac1{\sigma_p}+\frac1{1-\sigma_p}\\
&\qquad -4\Bigr)\ll Le^{-\alpha L},
\end{aligned}
\]
and the bracket is at least \(16(\sigma_p-\frac12)^2\) by (4.3) of Lesson 2.

*Nonprincipal characters.* For a nonprincipal \(\lambda\), \(\sum_v\lambda(v)e_p(vw)=\overline\lambda(w)\tau(\lambda)\) for every \(w\), so
\[
\begin{aligned}
&\mathbb E_vg_p(v)\lambda(v)e_p(av)\\
&\quad =\frac{\tau(\lambda)}{p^{3/2}}\sum_xF_p(x)\overline\lambda(a-x)\\
&\quad =\frac{\tau(\lambda)}{\sqrt p}\,\overline\lambda(-1)\,\frac{\sigma_p}{\sqrt{\sigma_p(1-\sigma_p)}}\\
&\qquad \;\mathbb E_{x\in S_p}\overline\lambda(x-a).
\end{aligned}
\]
The constant part of \(F_p\) disappears because the complete sum of \(\overline\lambda(a-x)\) is zero. The first two factors have modulus \(1\), and the third is bounded on balanced primes. For quadratic \(\lambda\), Corollary 1.2 of Lesson 3 shows that the maximal translated bias tends to zero in harmonic probability on the band; for \(\lambda\) of order greater than \(2\), so is \(\overline\lambda\), and Theorem 1.1 of Lesson 7 gives the same, with the maximum over the character inside.

*The principal character.* Since \(g_p(0)=0\), additive inversion gives \(\mathbb E_vg_p(v)e_p(av)=p^{-1/2}F_p(a)\), which tends to zero uniformly on balanced primes.

*Conclusion.* Choose thresholds tending to zero slowly enough in the balance and bias estimates; by Markov's inequality, the primes failing either have harmonic mass \(o(L)\). \(\square\)

Theorem 6.1 says that, for most primes, the normalized transform \(g_p\) correlates with no product \(\lambda(v)e_p(av)\) of a multiplicative and an additive character. Lessons 12–18 use it together with the \(L^2\) normalization of \(g_p\), the lower bound for its \(L^1\) norm proved in Lessons 10 and 11, and collision stability; no pointwise bound on \(g_p\) beyond the trivial \(|g_p|\le\sqrt p\) is used.

## 7. Exercises

**7.1.** Show that the bound of Lemma 1.1 is sharp: give a polynomial of degree \(D\) in one variable, uniform on a set of \(1/\alpha\) values, with \(\Pr(N=0)=D\alpha\).

**7.2.** For \(l=2\), list the four paths, their final signs, and the codes given by the anchors of step \(1\) and step \(2\). Check that the two paths with the same code have opposite final signs.

**7.3.** Let \(\chi\) be a character of \(\mathbb F_q^\times\) of order \(3\). Show that \(\chi^2\) is nonprincipal and that \(\chi^{-2}=\chi\). What goes wrong in Section 3 for a quadratic \(\chi\)?

**7.4.** In the proof of Theorem 6.1, verify that \(\mathbb E_vg_p(v)e_p(av)=p^{-1/2}F_p(a)\).

## 8. Solutions

**7.1.** Let \(x\) be uniform on \(\{1,\dots,1/\alpha\}\) (with \(1/\alpha\) an integer at least \(D\)) and \(N(x)=(x-1)(x-2)\cdots(x-D)\). Then \(\Pr(N=0)=D\alpha\).

**7.2.** By Lemma 2.1, the anchors of step \(1\) have \(e_0=1\) and pair \((1,-1)\) for \(t_1=1\), \((-1,1)\) for \(t_1=-1\). The anchors of step \(2\) have pair \((1,-1/e_1)\) for \(t_2=1\) and \((-1/e_1,1)\) for \(t_2=-1\). Paths: \((1,1)\): \(\varepsilon=1\), codes \((1,-1;1,-1)\). \((1,-1)\): \(\varepsilon=-1\), codes \((1,-1;-1,1)\). \((-1,1)\): \(\varepsilon=-1\), \(e_1=-1\), codes \((-1,1;1,1)\). \((-1,-1)\): \(\varepsilon=1\), codes \((-1,1;1,1)\). The paths \((-1,1)\) and \((-1,-1)\) share a code and have opposite final signs.

**7.3.** \(\chi^2\) has order \(3\), so it is nonprincipal, and \(\chi^{-2}=\chi^{3-2}=\chi\). For a quadratic \(\chi\), \(\chi^2\) is principal, so the one-sided interactions of Section 3 carry no cancellation; the quadratic case needs the separate argument of Lessons 3–6.

**7.4.** \(\mathbb E_vg_p(v)e_p(av)\)\(=\sqrt p\,\mathbb E_xF_p(x)\,\mathbb E_ve_p(v(a-x))\)\(=\sqrt p\cdot\frac1pF_p(a)\), since \(\mathbb E_ve_p(v(a-x))\) is \(1\) for \(x=a\) and \(0\) otherwise.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 4: cancellation for a one-sided character interaction, anchor codes and the diagonal bound, (4.13), the amplitude induction, the final permutation comparison, and Corollary 4.2. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
