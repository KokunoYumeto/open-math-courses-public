# Pushforward measures and logarithmic sampling

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

When several inputs have the same output, changing coordinates also changes how frequently the outputs are seen. A uniform choice of inputs need not produce a uniform choice of outputs. This elementary fact becomes important when a statement concerns “most” starting points of a dynamical system.

We develop the rule for transporting probability through a map, prove a quantitative comparison principle, and apply both to the odd-part projection of positive integers. Uniform sampling and logarithmic sampling behave differently under this projection. An exact calculation will explain that difference and transfer upper and lower logarithmic densities without assuming that a density limit exists.

We assume finite sums, inequalities, elementary limits, and the integral of \(1/t\). A short section explains the only infinite-sum rearrangement needed later. [Return maps and exact changes of clock](NT-COLLATZ-01.md), Lemma 1, proves the unique factorization \(n=2^a m\) used here. Basic references for the application are Tao's treatment of logarithmic sampling and Syracuse iteration, and Terras's treatment of density for the shortened map. All transport and density comparisons used in this lesson are proved below.

## Counting entire fibres

On a finite or countable set \(X\), a probability mass function is a function \(\mu:X\to[0,1]\) with \(\sum_{x\in X}\mu(x)=1\). The probability of a subset \(E\) is \(\mu(E)=\sum_{x\in E}\mu(x)\). For nonnegative terms, the sum over any countable set means the supremum of the sums over its finite subsets.

If \(f:X\to Y\), define the **pushforward** by

\[
(f_*\mu)(y)=\sum_{x:f(x)=y}\mu(x).
\]

Thus all the mass in the fibre \(f^{-1}(\{y\})\) is assigned to \(y\). The fibres partition \(X\), so the total mass remains 1, and

\[
(f_*\mu)(E)=\mu(f^{-1}(E)).
\]

Here is the justification for regrouping a countable nonnegative sum. Each finite collection of terms from finitely many fibres is a finite subset of \(X\), so its sum is at most the total sum on \(X\). Conversely, any finite subset of \(X\) meets finitely many fibres and is included in the corresponding fibre sums. Taking suprema in both directions proves equality. This reasoning also applies to nonnegative sums indexed by pairs.

A summable signed mass function \(\lambda\) satisfies \(\sum_x|\lambda(x)|<\infty\). Its positive and negative parts, \(\max(\lambda,0)\) and \(\max(-\lambda,0)\), are nonnegative summable functions. Subtracting their separately valid regroupings justifies every signed regrouping below.

**Proposition 1 (Composition and contraction).** For maps \(f:X\to Y\) and \(g:Y\to Z\),

\[
(g\circ f)_*\lambda=g_*(f_*\lambda),\qquad
\|f_*\lambda\|_1\leq\|\lambda\|_1,
\quad\|\lambda\|_1=\sum_x|\lambda(x)|.
\]

**Proof.** The fibre of \(g\circ f\) over \(z\) is the disjoint union of the fibres of \(f\) over all \(y\) with \(g(y)=z\). The regrouping just proved gives composition. For contraction, apply the triangle inequality in each fibre and then sum:

\[
\sum_y\left|\sum_{x:f(x)=y}\lambda(x)\right|
\leq\sum_y\sum_{x:f(x)=y}|\lambda(x)|
=\sum_x|\lambda(x)|.
\]

All sums on the right are finite in total. ∎

In particular, applying the same map to two probability laws cannot increase their \(\ell^1\) distance. This statement concerns the entire distribution, not just one event.

## Two ways to measure the difference between laws

For probabilities \(\mu,\nu\) on the same countable set, put

\[
d(\mu,\nu)=\sup_{E\subseteq X}|\mu(E)-\nu(E)|.
\]

**Lemma 2 (Event distance).**

\[
d(\mu,\nu)=\frac12\sum_x|\mu(x)-\nu(x)|.
\]

**Proof.** Write \(\lambda=\mu-\nu\). Its total mass is zero, so the sum of its positive terms equals the absolute value of the sum of its negative terms; call the common value \(P\). Every event sum lies between \(-P\) and \(P\). Taking \(E=\{x:\lambda(x)>0\}\) attains \(P\), whereas \(\|\lambda\|_1=2P\). ∎

We keep both quantities explicit. In particular, Tao's total-variation convention in equation (1.9) of his paper is the full \(\ell^1\) sum; the event distance here is half that sum. No estimate below relies on silently changing this factor.

## A projection that does not preserve uniform sampling

Let \(\mathcal O\) denote the positive odd integers. The odd-part map is

\[
\pi:\mathbb N_+\to\mathcal O,\qquad
\pi(n)=n/2^{\nu_2(n)}.
\]

Its fibre at \(m\in\mathcal O\) is \(\{m,2m,4m,\ldots\}\). For a uniform start among \(1,\ldots,8\), these fibres have sizes 4, 2, 1 and 1 at \(m=1,3,5,7\), respectively. The output probabilities are therefore \(1/2,1/4,1/8,1/8\), not four equal weights.

This discrepancy does not disappear uniformly over events as the cutoff grows. Put \(X=4M\) and take the event

\[
E_X=\{m\text{ odd}:X/2<m\leq X\}.
\]

There are \(M\) such odd integers. Each has just one preimage up to \(X\), so the odd part of a uniform start assigns \(E_X\) probability \(1/4\). Uniform sampling among the \(2M\) odd integers up to \(X\) assigns it probability \(1/2\). Their event distance is at least \(1/4\) for every positive integer \(M\). This identifies the precise sampling obstruction rather than merely noting that two formulas differ.

## Logarithmic weights

For an integer \(X\geq1\), set

\[
H(X)=\sum_{n=1}^X\frac1n,\qquad
H_o(X)=\sum_{\substack{1\leq m\leq X\\m\text{ odd}}}\frac1m,
\qquad H(0)=H_o(0)=0.
\]

The **logarithmic law** and its relative odd version are

\[
\rho_X(n)=\frac1{nH(X)}\quad(1\leq n\leq X),
\qquad
\rho_X^o(m)=\frac1{mH_o(X)}\quad(m\leq X\text{ odd}),
\]

and zero elsewhere. These are probability laws because their denominators are exactly the sums of their weights.

The decreasing function \(1/t\) gives

\[
\log(X+1)\leq H(X)\leq1+\log X.
\]

For the first inequality compare \(1/n\) with the integral over \([n,n+1]\). For the second, separate \(n=1\) and compare \(1/n\) with the integral over \([n-1,n]\). Separating even terms gives the exact identity

\[
H_o(X)=H(X)-\frac12H(\lfloor X/2\rfloor).
\]

It follows that \(H(X)=\log X+O(1)\), \(H_o(X)=\tfrac12\log X+O(1)\), and \(H_o(X)/H(X)\to1/2\). Here \(O(1)\) means bounded in absolute value by a constant independent of sufficiently large \(X\).

The reason for considering reciprocal weights is visible on a single fibre: replacing \(m\) by \(2^a m\) multiplies its weight by exactly \(2^{-a}\). Summing these weights is a geometric-series calculation.

## Exact comparison at a finite cutoff

For each odd \(m\leq X\), let \(j_m\geq0\) be the unique integer such that

\[
2^{j_m}m\leq X<2^{j_m+1}m.
\]

The fibre mass is

\[
(\pi_*\rho_X)(m)
=\frac{1+1/2+\cdots+2^{-j_m}}{mH(X)}
=\frac{2-2^{-j_m}}{mH(X)}.
\]

The finite geometric sum follows by subtracting half the sum from the sum itself. The term \(2^{-j_m}\) records the cutoff; we retain it throughout the comparison.

**Theorem 3 (Logarithmic sampling through odd parts).** For every integer \(X\geq1\),

\[
d(\pi_*\rho_X,\rho_X^o)
\leq\frac{H(X)-H(\lfloor X/2\rfloor)}{H(X)}.
\]

Consequently \(\|\pi_*\rho_X-\rho_X^o\|_1=O(1/\log X)\) as \(X\to\infty\).

**Proof.** For \(E\subseteq\mathcal O\), define

\[
B_E=\sum_{\substack{m\leq X\\m\in E}}\frac1m,
\qquad D_E=\sum_{\substack{m\leq X\\m\in E}}\frac{2^{-j_m}}m,
\qquad D=D_{\mathcal O}.
\]

Summing the exact fibre weights before division by \(H(X)\) yields

\[
H(X)=2H_o(X)-D.
\]

Combining this with the even-term identity gives \(D=H(X)-H(\lfloor X/2\rfloor)\). Set \(q=B_E/H_o(X)\), which lies in \([0,1]\). Then

\[
(\pi_*\rho_X)(E)-\rho_X^o(E)
=\frac{2B_E-D_E}{H(X)}-q
=\frac{qD-D_E}{H(X)}.
\]

Both \(qD\) and \(D_E\) lie in \([0,D]\), so the absolute difference is at most \(D/H(X)\), uniformly over \(E\). Taking the supremum proves the displayed bound.

The numerator stays bounded. More precisely, with \(M=\lfloor X/2\rfloor\geq1\), integral comparison on the tail gives

\[
\log\frac{X+1}{M+1}
\leq H(X)-H(M)\leq\log\frac XM.
\]

Both bounds tend to \(\log2\). Since \(H(X)\geq\log(X+1)\), Lemma 2 proves the asserted \(\ell^1\) rate. ∎

Unlike the uniform-sampling example, the discrepancy now tends to zero for every event at once. The theorem quantifies the endpoint loss in summing truncated fibres.

## Density without assuming a limit

For a set \(B\subseteq\mathbb N_+\), define its upper and lower logarithmic densities by

\[
\overline\delta_{\log}(B)=\limsup_{X\to\infty}\rho_X(B),
\qquad
\underline\delta_{\log}(B)=\liminf_{X\to\infty}\rho_X(B).
\]

For a bounded sequence \(u_X\), the upper limit is the limit of the decreasing tail suprema \(\sup_{X\geq M}u_X\); the lower limit is the limit of the increasing tail infima. These limits exist by completeness of the real numbers. When they agree, their common value is the logarithmic density. Relative odd densities use \(\rho_X^o\) in place of \(\rho_X\).

**Corollary 4.** For every \(E\subseteq\mathcal O\), the upper and lower logarithmic densities of \(\pi^{-1}(E)\) equal, respectively, the relative odd upper and lower logarithmic densities of \(E\).

**Proof.** Theorem 3 bounds \(|\rho_X(\pi^{-1}(E))-\rho_X^o(E)|\) by a quantity tending to zero. If two bounded sequences differ by a term tending to zero, then for every \(\varepsilon>0\) their sufficiently late tail suprema and infima differ by at most \(\varepsilon\). Passing first to tail limits and then to \(\varepsilon\downarrow0\) proves equality of both pairs. ∎

Relative odd density has denominator \(H_o(X)\), not \(H(X)\). When the relative odd density is \(d\), the logarithmic density of \(E\) as a subset of all integers is \(d/2\), since \(\rho_X(E)=\rho_X^o(E)H_o(X)/H(X)\).

For a further exact check, fix \(a\geq0\). Substitution \(n=2^a m\) gives

\[
\sum_{\substack{n\leq X\\\nu_2(n)=a}}\frac1n
=2^{-a}H_o(\lfloor X/2^a\rfloor).
\]

Its logarithmic density is \(2^{-a-1}\), by the harmonic estimates for fixed \(a\). The tail has the exact weight

\[
\sum_{\substack{n\leq X\\\nu_2(n)>A}}\frac1n
=2^{-A-1}H(\lfloor X/2^{A+1}\rfloor),
\]

because it consists of all multiples of \(2^{A+1}\). After division by \(H(X)\), it is at most \(2^{-A-1}\). Thus arbitrarily large initial powers of two can be controlled uniformly in the cutoff, without exchanging an infinite sum with a density limit.

## Applying the comparison to orbit minima

In the preceding return-map lesson we proved

\[
C_{\min}(n)=S_{\min}(\pi(n)),
\]

where \(C\) is the ordinary Collatz map and \(S\) its odd-return map. For a fixed bound \(K\), let \(E_K=\{m\in\mathcal O:S_{\min}(m)\leq K\}\). Then

\[
\{n:C_{\min}(n)\leq K\}=\pi^{-1}(E_K).
\]

Corollary 4 transfers the two upper densities and the two lower densities exactly. The dynamical identity identifies the event; Theorem 3 supplies the probability comparison. This is why a change of clock alone was insufficient for a statement about “most” starting integers.

## Exercises with solutions

**Exercise 1.** A uniform point is chosen from \(\{a,b,c,d,e\}\). A map sends \(a,b,c\) to 0 and \(d,e\) to 1. Compute the pushforward and its event distance from the uniform law on \(\{0,1\}\).

**Solution.** The fibre masses are \(3/5\) and \(2/5\). The pointwise differences from \(1/2,1/2\) are \(1/10,-1/10\); thus the event distance is \(1/10\), and the \(\ell^1\) distance is \(1/5\).

**Exercise 2.** For \(X=4\), compute both odd-part logarithmic laws and the bound in Theorem 3.

**Solution.** We have \(H(4)=25/12\) and \(H_o(4)=4/3\). The projected law on \(\{1,3\}\) is \((21/25,4/25)\), whereas the relative odd law is \((3/4,1/4)\). Their event distance is \(9/100\). The theorem's upper bound is \((H(4)-H(2))/H(4)=7/25\). It is an upper bound, not an equality claim.

**Exercise 3.** Suppose \(f_*\mu=f_*\nu\). Must \(\mu=\nu\)? Identify exactly the information lost for summable signed measures.

**Solution.** Not necessarily: two different point masses at points in the same fibre have equal pushforwards. In general \(f_*\lambda=0\) if and only if the sum of \(\lambda\) on every fibre is zero, directly from the definition. Thus the kernel consists exactly of these fibrewise cancellations.

**Exercise 4.** Show that a set of relative odd logarithmic density 1 has logarithmic density \(1/2\) among all integers, while its full odd-part preimage has logarithmic density 1.

**Solution.** The first assertion follows by multiplying the relative odd probabilities by \(H_o(X)/H(X)\to1/2\). The second is Corollary 4. These sets differ: one retains only odd integers; the other includes every power-of-two multiple of each retained odd integer.

## What carries forward

A deterministic map transports mass by summing over fibres. Once that mass is calculated, probability comparisons become inequalities between explicit sums. The lesson's logarithmic example is useful because its fibre weights form a geometric series and the truncation error is controlled uniformly over events.

[First passage and transport across scales](NT-COLLATZ-04.md) uses the same pushforward and contraction principles for a different map: the first point at which an orbit enters a target set. That map also forgets information, and its fibres will again identify exactly what is forgotten.

## References

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), Definition 1.2, §1.2 and equation (1.9). These locate logarithmic sampling, the odd-part relation and the convention for probability distance.

Riho Terras, *A stopping time problem on the positive integers*, Acta Arithmetica **30** (1976), 241–252. [DOI: 10.4064/aa-30-3-241-252](https://doi.org/10.4064/aa-30-3-241-252). Historical context for density statements about the shortened iteration; no stopping-time theorem is assumed in this lesson.
