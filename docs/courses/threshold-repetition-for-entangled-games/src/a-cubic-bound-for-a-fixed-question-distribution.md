# A cubic bound for a fixed question distribution

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 2.2 of [Entangled games and threshold repetition](entangled-games-and-threshold-repetition.md) without any external input: for a fixed question distribution \(\mu\), the probability of winning a fraction \(v+\delta\) of the repetitions decays at a rate proportional to \(\delta^3\). The vectors of [Conditioning on a tested set](conditioning-on-a-tested-set.md) depend on both players' questions. Within each connected component of the support of \(\mu\), adjacent question pairs share a one-question approximation, so each vector can be replaced by the vector of one fixed *root* pair, at a cost controlled along paths in the support. The root vectors define legal one-game strategies, which yields a conditioning estimate with square-root error, and the transfer of [From conditioning to a threshold bound](from-conditioning-to-a-threshold-bound.md) turns it into the cubic rate.

- Support components and component games (Section 1).
- A conditioning estimate through the components (Section 2).
- The cubic threshold bound (Section 3).

Notation is that of the earlier lessons.

## 1. Support components and component games

Let \(H=\{(x,y):\mu(x,y)>0\}\), joined into a graph by an edge between two pairs that share a question. For the connected components \(H_j\) put
\[
\begin{aligned}
&\lambda_j=\mu(H_j),\qquad\mu_j=\mu(\,\cdot\mid H_j),\\
&\mu_{j,\min}=\min_{z\in H_j}\mu_j(z),
\end{aligned}
\]
and \(\kappa_\mu=8\max_j(|H_j|-1)/\mu_{j,\min}\). This constant depends on the masses of \(\mu\), not only on its support; it is \(0\) when every component is a single pair.

**Lemma 1.1.** If \(\mu_X(x)>0\), all pairs of \(H\) with first entry \(x\) lie in one component; likewise for second entries.

*Proof.* Any two such pairs share the question \(x\), so they are adjacent. \(\square\)

So each player can determine the component from the local question alone. Let \(G_j\) be the game with question distribution \(\mu_j\) and the predicate of \(G\), and \(v_j=\omega^*(G_j)\).

**Lemma 1.2.** \(\sum_j\lambda_jv_j\le\omega^*(G)\).

*Proof.* Let \(\varepsilon>0\) and choose finite-dimensional strategies \(\mathcal S_j\) for the finitely many games \(G_j\) with success at least \(v_j-\varepsilon\). Let the players share the tensor product of the states of all \(\mathcal S_j\). On question \(x\), Alice determines the component \(j\) of \(x\) by Lemma 1.1 and applies her measurement of \(\mathcal S_j\) on the \(j\)-th factor; Bob does the same. On a pair of \(H_j\) both use \(\mathcal S_j\), so this strategy for \(G\) succeeds with probability \(\sum_j\lambda_j(\text{success of }\mathcal S_j)\ge\sum_j\lambda_jv_j-\varepsilon\). No supremum needs to be attained. \(\square\)

## 2. A conditioning estimate through the components

**Proposition 2.1** ([OpenAI-TR, Proposition 5.1]). For every finite-dimensional strategy for the \(k\)-fold repetition and every proper set \(C\) of coordinates with \(p=\Pr(E_C)>0\), with \(m=k-|C|\), \(\tau=\tau(C)\) and the average conditional win rate \(\bar s(C)\),
\[
\begin{aligned}
\bar s(C)&\le v+\sqrt{\frac{\log(1/p)}{2m}}\\
&\quad+4\sqrt{\kappa_\mu\tau}+2\kappa_\mu\tau .
\end{aligned} \tag{2.1}
\]
The bound does not depend on the dimension of the strategy or on \(k\).

*Proof.* *The inputs.* Use the construction of [Conditioning on a tested set](conditioning-on-a-tested-set.md) for \(C\), with the mode \(i\) restored in the notation. For a transcript \(r\) of mode \(i\) put \(w_{i,r}=w_i(r)/m\), and for a fresh pair \(z=(x,y)\) write \(\Psi_{i,z}^r=\Psi_{xy}^r\), with the local vectors \(\Psi_{i,x}^r,\Psi_{i,y}^r\) and the acceptance operators \(W_{i,r,z}\) of that lesson, \(0\preceq W_{i,r,z}\preceq I\). Let
\[
c_{i,r,z}=\|\Psi_{i,z}^r-\Psi_{i,x}^r\|^2+\|\Psi_{i,z}^r-\Psi_{i,y}^r\|^2 .
\]
Averaging (2.2) and (2.3) and Lemma 3.1 of that lesson over the modes gives
\[
\begin{aligned}
&\sum_{i,r,z}w_{i,r}\mu(z)\|\Psi_{i,z}^r\|^2=p,\\
&\sum_{i,r,z}w_{i,r}\mu(z)\,c_{i,r,z}\le2p\tau,\\
&\sum_{i,r,z}w_{i,r}\mu(z)\\
&\quad\cdot\langle\Psi_{i,z}^r,W_{i,r,z}\Psi_{i,z}^r\rangle=p\bar s,
\end{aligned} \tag{2.2}
\]
where \(\bar s=\bar s(C)\).

*Replacement by a root.* Choose a root \(\rho_j\in H_j\) in each component. Fix \(i,r\) and abbreviate \(\Psi_z=\Psi_{i,z}^r\) and \(c_z=c_{i,r,z}\). If \(z,z'\in H_j\) share the question \(y\), the common local vector \(\Psi_y\) gives
\[
\begin{aligned}
&\|\Psi_z-\Psi_{z'}\|^2\\
&\quad\le2\|\Psi_z-\Psi_y\|^2+2\|\Psi_y-\Psi_{z'}\|^2\\
&\quad\le2(c_z+c_{z'}),
\end{aligned}
\]
and likewise with \(\Psi_x\) if they share \(x\). A simple path from \(z\) to \(\rho_j\) in \(H_j\) has at most \(|H_j|-1\) edges, and each vertex lies on at most two of them. The Cauchy–Schwarz inequality along the path gives
\[
\begin{aligned}
&\|\Psi_z-\Psi_{\rho_j}\|^2\le4(|H_j|-1)\sum_{a\in H_j}c_a\\
&\quad\le\frac{4(|H_j|-1)}{\mu_{j,\min}}\sum_{a\in H_j}\mu_j(a)c_a .
\end{aligned}
\]
Define
\[
\begin{aligned}
&E_j=\sum_{i,r}\sum_{z\in H_j}w_{i,r}\mu_j(z)\|\Psi_{i,z}^r-\Psi_{i,\rho_j}^r\|^2,\\
&E=\sum_j\lambda_jE_j .
\end{aligned}
\]
Since \(\sum_z\mu_j(z)=1\), \(\lambda_j\mu_j(a)=\mu(a)\) and \(4(|H_j|-1)/\mu_{j,\min}\le\kappa_\mu/2\), the path estimate and (2.2) give
\[
\begin{aligned}
E&\le\frac{\kappa_\mu}2\sum_{i,r,a}w_{i,r}\mu(a)c_{i,r,a}\\
&\le\kappa_\mu p\tau .
\end{aligned} \tag{2.3}
\]

*Legal component strategies.* Put
\[
\begin{aligned}
P_j&=\sum_{i,r}\sum_{z\in H_j}w_{i,r}\mu_j(z)\|\Psi_{i,z}^r\|^2,\\
\widehat P_j&=\sum_{i,r}w_{i,r}\|\Psi_{i,\rho_j}^r\|^2,\\
T_j&=\sum_{i,r}\sum_{z\in H_j}w_{i,r}\mu_j(z)\\
&\qquad\cdot\langle\Psi_{i,z}^r,W_{i,r,z}\Psi_{i,z}^r\rangle,\\
\widehat T_j&=\sum_{i,r}\sum_{z\in H_j}w_{i,r}\mu_j(z)\\
&\qquad\cdot\langle\Psi_{i,\rho_j}^r,W_{i,r,z}\Psi_{i,\rho_j}^r\rangle .
\end{aligned}
\]
If \(\widehat P_j>0\), the vector
\[
\begin{aligned}
\Xi_j&=\widehat P_j^{-1/2}\sum_{i,r}\sqrt{w_{i,r}}\\
&\qquad\cdot|i,r\rangle_A\otimes|i,r\rangle_B\otimes\Psi_{i,\rho_j}^r
\end{aligned}
\]
is a unit vector in a finite-dimensional space, with flag registers \(|i,r\rangle\) held by both players. On question \(x\), Alice reads her register \((i,r)\) and applies the POVM \((\widetilde M_{r,x}^a)_a\) of mode \(i\) to her factor \(\mathcal K_A\); Bob does the same with \((\widetilde N_{r,y}^b)_b\). The state and the register distribution do not depend on the fresh questions, because the vectors are taken at the fixed root \(\rho_j\) and the weights do not involve the fresh pair; each measurement depends only on its own player's question. So this is a legal strategy for \(G_j\). The registers are perfectly correlated, so its success probability is \(\widehat T_j/\widehat P_j\). Hence, also when \(\widehat P_j=0\) (then \(\widehat T_j=0\)),
\[
\widehat T_j\le v_j\widehat P_j . \tag{2.4}
\]

*Comparison.* For vectors \(a,b\) and \(0\preceq W\preceq I\),
\[
\begin{aligned}
&\langle a,Wa\rangle-\langle b,Wb\rangle\\
&\quad=\langle a-b,Wa\rangle+\langle b,W(a-b)\rangle,
\end{aligned}
\]
so
\[
\begin{aligned}
&|\langle a,Wa\rangle-\langle b,Wb\rangle|\\
&\quad\le(\|a\|+\|b\|)\|a-b\| .
\end{aligned}
\]
With \(W=I\) or \(W=W_{i,r,z}\), the weighted Cauchy–Schwarz inequality gives
\[
\begin{aligned}
&|P_j-\widehat P_j|,\ |T_j-\widehat T_j|\le e_j,\\
&e_j:=\bigl(\sqrt{P_j}+\sqrt{\widehat P_j}\bigr)\sqrt{E_j} .
\end{aligned}
\]
Since \(\sum_j\lambda_jP_j=p\) by (2.2), the triangle inequality in the weighted direct sum of the spaces gives \(\sqrt{\widehat P}\le\sqrt p+\sqrt E\) for \(\widehat P=\sum_j\lambda_j\widehat P_j\), and another Cauchy–Schwarz inequality gives
\[
\begin{aligned}
\sum_j\lambda_je_j&\le\bigl(\sqrt p+\sqrt{\widehat P}\bigr)\sqrt E\\
&\le2\sqrt{pE}+E .
\end{aligned}
\]
By (2.4) and \(v_j\le1\), \(T_j\le\widehat T_j+e_j\le v_j\widehat P_j+e_j\le v_jP_j+2e_j\). Since \(\sum_j\lambda_jT_j=p\bar s\) by (2.2),
\[
\begin{aligned}
\bar s&\le\sum_j\widetilde\lambda_jv_j+4\sqrt{E/p}\\
&\quad+2E/p,
\end{aligned} \tag{2.5}
\]
where \(\widetilde\lambda_j=\lambda_jP_j/p\).

*The component weights.* Let \(J_i\) be the component of the fresh pair at mode \(i\). By (2.2) of the previous lesson, \(\lambda_jP_j=\frac1m\sum_i\Pr(E_C,\ J_i=j)\), so \(\widetilde\lambda\) is the average over \(i\) of the law of \(J_i\) given \(E_C\). The \(J_i\) are independent with law \(\lambda=(\lambda_j)\), so Lemma 4.1 of the previous lesson and convexity of total variation give \(\operatorname{TV}(\widetilde\lambda,\lambda)\le\sqrt{\log(1/p)/(2m)}\). Since \(0\le v_j\le1\),
\[
\begin{aligned}
\sum_j\widetilde\lambda_jv_j&\le\sum_j\lambda_jv_j+\operatorname{TV}(\widetilde\lambda,\lambda)\\
&\le v+\sqrt{\frac{\log(1/p)}{2m}},
\end{aligned}
\]
by Lemma 1.2. Substituting this and (2.3) into (2.5) proves (2.1). \(\square\)

For fixed \(\mu\) the error in (2.1) is \(O(\sqrt\tau+\tau)\), while (S) has error of order \(\tau^{1/4}\) with a universal constant. Where both apply, the smaller one may be used.

## 3. The cubic threshold bound

*Proof of Theorem 2.2 of [Entangled games and threshold repetition](entangled-games-and-threshold-repetition.md).* Since \(\log(1/p)\le m\tau\), Proposition 2.1 bounds the average conditional win rate by
\[
v+\sqrt{\tau/2}+4\sqrt{\kappa_\mu\tau}+2\kappa_\mu\tau .
\]
Let \(0<\delta<1-v\) and \(T=\delta^2/(1024(1+\kappa_\mu))\). If \(\tau(C)\le T\), the excess is at most
\[
\begin{aligned}
&\frac\delta{\sqrt{2048}}+\frac{4\delta}{32}+\frac{2\delta^2}{1024}\\
&\quad\le\frac\delta{32}+\frac\delta8+\frac\delta{512}=\frac{81\delta}{512}<\frac\delta4,
\end{aligned}
\]
using \(\kappa_\mu/(1+\kappa_\mu)\le1\) and \(\delta<1\). Also \(T\le\delta/4\). So the hypothesis (2.1) of Proposition 2.1 of [From conditioning to a threshold bound](from-conditioning-to-a-threshold-bound.md) holds, and that proposition gives the rate
\[
\begin{aligned}
&\frac{\delta T}{16(1+\log d)}=\frac{\delta^3}{c_\mu},\\
&c_\mu=16384(1+\kappa_\mu)(1+\log d) .\qquad\square
\end{aligned}
\]

## 4. Exercises

**4.1.** For the game of Exercise 5.2 of the first lesson, compute the rate of Theorem 2.2.

**4.2.** Let \(\mu\) be uniform on the pairs \((x,\sigma(x))\) for a bijection \(\sigma\). Show that \(\kappa_\mu=0\) and that (2.1) reads \(\bar s\le v+\sqrt{\log(1/p)/(2m)}\).

**4.3.** Prove that a simple path in a graph with \(n\) vertices has at most \(n-1\) edges and that each of its vertices lies on at most two of its edges. Deduce the factor \(4(|H_j|-1)\) in the path estimate.

**4.4.** Show that \(\operatorname{TV}(\widetilde\lambda,\lambda)\le\frac1m\sum_i\operatorname{TV}(P_i,\lambda)\) when \(\widetilde\lambda=\frac1m\sum_iP_i\).

**4.5.** In the strategy built from \(\Xi_j\), explain why it matters that the weights \(w_{i,r}\) do not depend on the fresh pair.

## 5. Solutions

**4.1.** \(d=4\) and \(\kappa_\mu=96\), so the rate is \(\delta^3/(16384\cdot97\cdot(1+\log4))\), about \(\delta^3/(3.8\cdot10^6)\).

**4.2.** Two different pairs \((x,\sigma(x))\) share no question, so every component is a single pair and \(\kappa_\mu=0\); the terms with \(\kappa_\mu\) vanish.

**4.3.** The \(n'\le n\) vertices of a simple path are distinct and consecutive vertices are joined, giving \(n'-1\) edges; an inner vertex lies on its two neighbouring edges and an end vertex on one. Along a path \(z_0,\dots,z_\ell\),
\[
\begin{aligned}
&\|\Psi_{z_0}-\Psi_{z_\ell}\|^2\le\ell\sum_t\|\Psi_{z_t}-\Psi_{z_{t+1}}\|^2\\
&\quad\le\ell\sum_t2(c_{z_t}+c_{z_{t+1}})\le4\ell\sum_ac_a .
\end{aligned}
\]

**4.4.** \(\operatorname{TV}\) is a norm distance, \(\frac12\|\cdot\|_1\), so \(\|\frac1m\sum_i(P_i-\lambda)\|_1\le\frac1m\sum_i\|P_i-\lambda\|_1\).

**4.5.** A strategy for one game must prepare its shared state before the questions are asked. If the weights depended on the fresh pair, \(\Xi_j\) would depend on the questions, and the players could not prepare it.

## References

- [OpenAI-TR] OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, OpenAI Math Release preprint, 25 September 2026, Proposition 5.1, Corollary 5.2. https://github.com/openai/math/tree/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
