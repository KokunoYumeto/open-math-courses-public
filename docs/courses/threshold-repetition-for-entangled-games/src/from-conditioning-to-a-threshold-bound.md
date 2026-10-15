# From conditioning to a threshold bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the probabilistic half of threshold repetition. If the upper tail of the number of wins is not exponentially small, a few randomly sampled coordinates form a tested set \(C\) that is won with not too small probability, and given that \(C\) is won the other coordinates are won at a high average rate. A conditioning estimate, which bounds that rate in terms of the conditioning cost of \(C\), rules this out. The argument uses only the joint law of the win indicators, and turns any conditioning estimate into an exponential rate. With Song's estimate (S) it proves Theorem 2.1 of [Entangled games and threshold repetition](entangled-games-and-threshold-repetition.md); a last section derives two-sided error amplification.

- Selecting the tested coordinates (Section 1).
- The transfer from conditioning to threshold bounds (Section 2).
- The universal threshold bound (Section 3).
- Two-sided error amplification (Section 4).

Notation is that of the first lesson: \(G\) is a finite game with entangled value \(v<1\), \(d=|\mathcal A||\mathcal B|\ge1\), \(I_i\) are the win indicators of a strategy for the \(k\)-fold repetition, \(W=\sum_iI_i\), \(E_C\) is the event that every coordinate of \(C\) is won, \(p_C=\Pr(E_C)\), and \(\tau(C)\) is the conditioning cost.

## 1. Selecting the tested coordinates

**Lemma 1.1** (sampling the upper tail; [OpenAI-TR, Lemma 2.2]). Let \(I_1,\dots,I_k\) be arbitrary jointly distributed \(\{0,1\}\)-valued random variables, \(W=\sum_iI_i\). Let \(0<q_0<q<1\), \(0<\varepsilon<1\), and suppose \(p_H=\Pr(W\ge\lceil qk\rceil)>0\). Put
\[
\ell=\Bigl\lceil\frac{\log(4/(\varepsilon p_H))}{\log(q/q_0)}\Bigr\rceil .
\]
There is a set \(C\subseteq\{1,\dots,k\}\) with \(|C|\le\ell\) such that
\[
\begin{aligned}
&p_C\ge\tfrac12p_Hq^\ell,\\
&\Pr(W<q_0k\mid E_C)\le\varepsilon .
\end{aligned} \tag{1.1}
\]

*Proof.* Draw \(\ell\) indices independently and uniformly from \(\{1,\dots,k\}\), independently of the indicators, and let \(C\) be the set of drawn indices. For each outcome of the draw put
\[
\begin{aligned}
&a_C=\Pr(E_C),\\
&b_C=\Pr(E_C,\ W<q_0k),\\
&A=p_Hq^\ell .
\end{aligned}
\]
Given the indicators, each draw hits a won coordinate with probability \(W/k\), so the average over the draw is
\[
\begin{aligned}
\mathbb E_Ca_C&=\mathbb E\bigl[(W/k)^\ell\bigr]\\
&\ge\Pr(W\ge\lceil qk\rceil)\,q^\ell=A,\\
\mathbb E_Cb_C&=\mathbb E\bigl[(W/k)^\ell\mathbf 1_{\{W<q_0k\}}\bigr]\\
&\le q_0^\ell .
\end{aligned}
\]
By the choice of \(\ell\), \((q/q_0)^\ell\ge4/(\varepsilon p_H)\), that is, \(q_0^\ell\le\varepsilon A/4\). The outcomes with \(a_C<A/2\) contribute less than \(A/2\) to \(\mathbb E_Ca_C\), and those with \(b_C>\varepsilon a_C\) contribute at most \(\varepsilon^{-1}\mathbb E_Cb_C\le A/4\). So some outcome has \(a_C\ge A/2\) and \(b_C\le\varepsilon a_C\); its set \(C\) satisfies (1.1), since \(\Pr(W<q_0k\mid E_C)=b_C/a_C\). \(\square\)

## 2. The transfer from conditioning to threshold bounds

**Proposition 2.1** ([OpenAI-TR, Proposition 2.3]). Fix \(0<\delta<1-v\) and \(0<T\le\delta/4\). Suppose that for every \(k\ge1\), every finite-dimensional strategy for the \(k\)-fold repetition, and every proper subset \(C\) of the coordinates with \(p_C>0\),
\[
\begin{aligned}
&\tau(C)\le T\\
&\quad\Longrightarrow\ \bar s(C)\le v+\frac\delta4 .
\end{aligned} \tag{2.1}
\]
Then for every \(k\ge1\) and every finite-dimensional strategy,
\[
\begin{aligned}
&\Pr\bigl(W\ge\lceil(v+\delta)k\rceil\bigr)\\
&\quad\le e^{-ck},
\end{aligned} \tag{2.2}
\]
where \(c=\delta T/(16(1+\log d))\).
The same bound holds for the supremum over all strategies.

*Proof.* Put
\[
\begin{gathered}
q=v+\delta,\quad q_0=v+\frac\delta2,\quad\eta=\frac\delta{16},\\
r=\log\frac q{q_0},\quad R=\log\frac dq ,
\end{gathered}
\]
and let \(c\) be as in (2.2). Then \(0<q_0<q<1\), \(r>0\) and \(R>0\). Since \(r=-\log(1-\delta/(2q))\ge\delta/(2q)\) and \(q\le1\),
\[
\begin{aligned}
\frac cr&\le\frac{2qT}{16(1+\log d)}\\
&\le\frac T8\le\frac\eta2 .
\end{aligned} \tag{2.3}
\]
Since \(q\log(1/q)\le1/e<1\) and \(\delta<1\),
\[
\begin{aligned}
\delta\Bigl(1+\frac Rr\Bigr)&\le\delta+2q\log d+2q\log\frac1q\\
&\le3(1+\log d),
\end{aligned}
\]
so
\[
c\Bigl(1+\frac Rr\Bigr)\le\frac{3T}{16} . \tag{2.4}
\]

*Large repetition lengths.* Put \(t=1+\log(4/\eta)/r\) and \(B=\log2+Rt\), and choose \(k_0\) with \(t/k_0\le\eta/2\) and \(B/k_0\le T/16\). We show (2.2) for \(k\ge k_0\). Suppose instead that \(p_H=\Pr(W\ge\lceil qk\rceil)>e^{-ck}\), and apply Lemma 1.1 with \(\varepsilon=\eta\). Then
\[
\begin{aligned}
\ell&\le\frac{\log(4/\eta)+\log(1/p_H)}r+1\\
&\le\frac{ck}r+t\le\eta k,
\end{aligned}
\]
by (2.3) and the choice of \(k_0\); in particular \(C\) is a proper subset. On \(E_C\) the \(|C|\) tested coordinates are won, so \(W-|C|=\sum_{i\notin C}I_i\ge0\), and on \(\{W\ge q_0k\}\) also \(W-|C|\ge q_0k-|C|\ge0\), because \(|C|\le\eta k<q_0k\). By (1.1),
\[
\begin{aligned}
&\frac{\mathbb E[W-|C|\mid E_C]}{k-|C|}\ge(1-\eta)\frac{q_0-u}{1-u}\\
&\quad\ge(1-\eta)\frac{q_0-\eta}{1-\eta}=v+\frac{7\delta}{16},
\end{aligned}
\]
where \(u=|C|/k\le\eta\) and \(u\mapsto(q_0-u)/(1-u)\) is decreasing on \([0,1)\). The left side is \(\bar s(C)\).

On the other hand, \(p_C\ge\frac12p_Hq^\ell\) and \(|C|\le\ell\) give
\[
\begin{aligned}
&\log\frac1{p_C}+|C|\log d\\
&\quad\le\log\frac1{p_H}+\log2+\ell\log\frac1q+\ell\log d\\
&\quad\le ck+\log2+\ell R .
\end{aligned}
\]
With \(\ell\le ck/r+t\), the right side is at most \(ck(1+R/r)+B\), so by (2.4) and \(k-|C|\ge(1-\eta)k\),
\[
\begin{aligned}
\tau(C)&\le\frac{c(1+R/r)+B/k}{1-\eta}\\
&\le\frac{3T/16+T/16}{1-\eta}\\
&=\frac T{4(1-\eta)}<T .
\end{aligned}
\]
Now (2.1) bounds the average conditional win rate by \(v+\delta/4<v+7\delta/16\), a contradiction. So (2.2) holds for \(k\ge k_0\); the bound \(k_0\) depends only on \(\delta,T,v,d\), not on the strategy.

*All repetition lengths.* Fix any strategy for \(k\) coordinates and take \(N\) independent tensor copies of it, a strategy for \(Nk\) coordinates in which the blocks of \(k\) coordinates are independent (Exercise 5.5 of the first lesson). If every block has at least \(\lceil qk\rceil\) wins, the total is at least \(N\lceil qk\rceil\ge\lceil qNk\rceil\). Choosing \(N\) with \(Nk\ge k_0\), the first part gives \(p_H^N\le e^{-cNk}\), so \(p_H\le e^{-ck}\). The constants do not depend on the strategy or its dimension, so the bound passes to the supremum. \(\square\)

The proposition separates the probabilistic step from the analytic one: whatever budget \(T\) a conditioning estimate permits for the excess \(\delta/4\), the threshold rate is proportional to \(\delta T\). The selection of the tested set uses only the joint law of the win indicators.

## 3. The universal threshold bound

*Proof of Theorem 2.1 of [Entangled games and threshold repetition](entangled-games-and-threshold-repetition.md).* Let \(B_4\ge1\) be the constant of (S), and for \(0<\delta<1-v\) put
\[
T=\Bigl(\frac\delta{4B_4}\Bigr)^4 .
\]
Since \(B_4\ge1\) and \(0<\delta<1\), \(T\le\delta^4/256\le\delta/4<1\). If \(\tau(C)\le T\), then \(\tau(C)\le1\) and (S) bounds the average conditional win rate by \(v+B_4T^{1/4}=v+\delta/4\). So (2.1) holds, and Proposition 2.1 gives (2.2) with
\[
\frac{\delta T}{16(1+\log d)}=\frac{\delta^5}{16(4B_4)^4(1+\log d)} .
\]
This is (2.1) of the first lesson with \(\kappa_0=1/(16(4B_4)^4)\). \(\square\)

## 4. Two-sided error amplification

A threshold between two success levels amplifies both guarantees at once: tensor copies of a good one-game strategy win many coordinates, while every joint strategy for a game of low value wins few.

**Corollary 4.1** ([OpenAI-TR, Corollary 6.1]). Assume (S). Let \(G\) be a finite game and \(0\le s<c\le1\); put \(\Delta=c-s\), \(t=(c+s)/2\) and \(d=|\mathcal A||\mathcal B|\). For \(k\ge1\) let \(G_k\) be the game that samples \(k\) independent question pairs of \(G\), sends each player the string of its questions, and accepts exactly when \(W_k\ge\lceil tk\rceil\). Then
\[
\begin{aligned}
&\omega^*(G)\ge c\ \Longrightarrow\ \omega^*(G_k)\ge1-e^{-\Delta^2k/8},\\
&\omega^*(G)\le s\ \Longrightarrow\\
&\qquad\omega^*(G_k)\le\exp\Bigl(-\frac{\kappa_0(\Delta/2)^5}{1+\log d}\,k\Bigr).
\end{aligned}
\]

*Proof.* *Completeness.* By the definition of the value there is a finite-dimensional strategy for \(G\) with success \(s_1>c-\Delta/4=t+\Delta/4\). Its \(k\) tensor copies have independent win indicators with mean \(s_1\) (Exercise 5.5 of the first lesson). Since \(W_k\) is an integer, \(\{W_k<\lceil tk\rceil\}=\{W_k<tk\}\), and Hoeffding's inequality ([Concentration and the discrete cube](course:the-gaussian-moat-problem/concentration-and-the-discrete-cube), Theorem 2.2, applied to the variables \(-I_i\)) gives
\[
\begin{aligned}
&\Pr(W_k<tk)\\
&\quad\le\Pr\bigl(W_k-s_1k\le-(s_1-t)k\bigr)\\
&\quad\le e^{-2(s_1-t)^2k}\le e^{-\Delta^2k/8} .
\end{aligned}
\]
*Soundness.* Let \(v=\omega^*(G)\le s\) and \(\delta=t-v\). Then \(\delta\ge\Delta/2>0\), and \(\delta<1-v\) because \(t<1\). For every finite-dimensional strategy for \(G_k\), Theorem 2.1 of the first lesson at the threshold \(\lceil(v+\delta)k\rceil=\lceil tk\rceil\) bounds the success probability by \(\exp(-\kappa_0\delta^5k/(1+\log d))\), which is at most \(\exp(-\kappa_0(\Delta/2)^5k/(1+\log d))\); take the supremum. \(\square\)

The rate in the soundness bound may be replaced by the rate of Theorem 2.2 of the first lesson with \(\delta=\Delta/2\); that version does not use (S). For verifier families with inverse-polynomial gap \(\Delta\) and polynomial answer length, polynomially many repetitions make both errors exponentially small, keeping two players, one round and classical messages.

## 5. Exercises

**5.1.** In Lemma 1.1 let \(I_1=\dots=I_k\) be a single fair coin and \(q=3/4\), \(q_0=1/2\). Compute \(p_H\) and show that every nonempty \(C\) satisfies (1.1) with \(\Pr(W<q_0k\mid E_C)=0\).

**5.2.** Prove \(-\log(1-x)\ge x\) for \(0\le x<1\) and \(q\log(1/q)\le1/e\) for \(0<q\le1\).

**5.3.** Show that \(u\mapsto(q_0-u)/(1-u)\) is decreasing on \([0,1)\) when \(q_0<1\).

**5.4.** Explain why the proof of Proposition 2.1 cannot apply Lemma 1.1 with \(C\) equal to all coordinates, and where \(\ell\le\eta k\) is used.

**5.5.** Show that \(N\lceil qk\rceil\ge\lceil qNk\rceil\) for integers \(N,k\ge1\) and real \(q\).

## 6. Solutions

**5.1.** \(W\in\{0,k\}\), each with probability \(1/2\), so \(p_H=1/2\). For nonempty \(C\), \(E_C=\{W=k\}\), on which \(W\ge q_0k\); so the conditional probability is \(0\), and \(p_C=1/2\ge\frac12p_Hq^\ell\).

**5.2.** \(-\log(1-x)=\sum_{n\ge1}x^n/n\ge x\). The function \(q\log(1/q)\) has derivative \(\log(1/q)-1\), vanishing at \(q=1/e\), where its value \(1/e\) is the maximum.

**5.3.** The derivative is \((q_0-1)/(1-u)^2<0\).

**5.4.** If \(C\) were all coordinates, the average over \(i\notin C\) would be empty and \(\tau(C)\) undefined. The bound \(\ell\le\eta k<k\) makes \(C\) proper, gives \(k-|C|\ge(1-\eta)k\), and gives \(|C|<q_0k\) in the lower bound for the conditional win rate.

**5.5.** \(N\lceil qk\rceil\) is an integer at least \(Nqk\), hence at least \(\lceil qNk\rceil\).

## References

- [OpenAI-TR] OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, OpenAI Math Release preprint, 25 September 2026, Lemma 2.2, Propositions 2.3 and 2.4, Corollary 6.1. https://github.com/openai/math/tree/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
- [Son26] Z. Song, *Parallel Repetition for Entangled Games with Gap Exponent Three*, Electronic Colloquium on Computational Complexity, TR26-199 (2026), Lemma 4.4. https://eccc.weizmann.ac.il/report/2026/199/
