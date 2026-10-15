# Entangled games and threshold repetition

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a two-player game a referee asks each player a question and accepts or rejects their answers; the players may share an entangled quantum state but cannot communicate. When the game is repeated \(k\) times in parallel, the players see all their questions at once and may coordinate their answers across the repetitions. Parallel repetition asks how fast their chance of winning every repetition decays; *threshold* repetition asks how fast their chance of winning more than a fraction \(v+\delta\) of the repetitions decays, where \(v\) is the value of one game.

This course proves the theorems of [OpenAI-TR]: for every finite game, the probability of winning at least a fraction \(v+\delta\) of \(k\) repetitions decays exponentially in \(k\), uniformly over all finite-dimensional entangled strategies. A universal rate proportional to \(\delta^5\) rests on a conditioning estimate of Song, which is a named hypothesis of the course; a rate proportional to \(\delta^3\), with a constant that depends on the question distribution, is proved in full.

This lesson defines games, strategies and repetition, states the theorems and the named hypothesis, and proves that a single coordinate of a repeated strategy is won with probability at most the value.

- Games, strategies and repetition (Section 1).
- The theorems (Section 2).
- One coordinate at a time (Section 3).
- The plan of the proofs (Section 4).

## 1. Games, strategies and repetition

A *finite two-player one-round game* \(G\) consists of nonempty finite question sets \(\mathcal X,\mathcal Y\), nonempty finite answer sets \(\mathcal A,\mathcal B\), a probability distribution \(\mu\) on \(\mathcal X\times\mathcal Y\), and a predicate \(V\colon\mathcal X\times\mathcal Y\times\mathcal A\times\mathcal B\to\{0,1\}\). The referee samples \((x,y)\) from \(\mu\), sends \(x\) to Alice and \(y\) to Bob, and accepts the answers \((a,b)\) when \(V(x,y,a,b)=1\). The distribution \(\mu\) may be correlated and may have zero entries. We put \(d=|\mathcal A||\mathcal B|\); all logarithms are natural.

Hilbert spaces are complex and finite-dimensional. An operator \(T\) is *positive*, \(T\succeq0\), if it is self-adjoint with nonnegative spectrum, and \(S\preceq T\) means \(T-S\succeq0\). A *POVM* with outcomes in a finite set \(\mathcal A\) is a family of positive operators \((M^a)_{a\in\mathcal A}\) with \(\sum_aM^a=I\). A *finite-dimensional entangled strategy* for \(G\) consists of spaces \(\mathcal H_A,\mathcal H_B\), a unit vector \(\psi\in\mathcal H_A\otimes\mathcal H_B\), and POVMs \((M_x^a)_a\) on \(\mathcal H_A\) for each \(x\in\mathcal X\) and \((N_y^b)_b\) on \(\mathcal H_B\) for each \(y\in\mathcal Y\). Its success probability is
\[
\begin{aligned}
&\sum_{x,y,a,b}\mu(x,y)V(x,y,a,b)\\
&\qquad\cdot\langle\psi,(M_x^a\otimes N_y^b)\psi\rangle .
\end{aligned}
\]
Each \(\langle\psi,(M_x^a\otimes N_y^b)\psi\rangle\) is nonnegative and they sum to \(1\) over \((a,b)\), so for fixed \((x,y)\) they form the law of the answers. The *entangled value* \(\omega^*(G)\) is the supremum of the success probability over all finite dimensions and all such strategies; it need not be attained. A mixed shared state can be replaced by a purification on a larger finite-dimensional space, so pure states lose nothing.

With one-dimensional spaces the POVMs are probability vectors, so every pair of deterministic answer functions is a strategy; in particular \(\omega^*(G)\) is at least the success probability of every deterministic strategy.

In the *\(k\)-fold repetition* the referee samples \((X_1,Y_1),\dots,(X_k,Y_k)\) independently from \(\mu\) and sends Alice the string \(\mathbf X=(X_1,\dots,X_k)\) and Bob the string \(\mathbf Y\). A strategy consists of a unit vector \(\psi\) and POVMs \((M_{\mathbf x}^{\mathbf a})_{\mathbf a\in\mathcal A^k}\) and \((N_{\mathbf y}^{\mathbf b})_{\mathbf b\in\mathcal B^k}\), one for each question string; the answers in different coordinates may depend on all questions. Write
\[
I_i=V(X_i,Y_i,A_i,B_i),\qquad W_k=\sum_{i=1}^kI_i,
\]
for the win indicator of coordinate \(i\) and the number of wins. The indicators need not be independent.

## 2. The theorems

**Theorem 2.1** ([OpenAI-TR, Theorem 1.1]). Assume (S) below. There is a universal constant \(\kappa_0>0\) such that the following holds. Let \(G\) be a finite two-player one-round game with entangled value \(v=\omega^*(G)<1\). For every \(0<\delta<1-v\), every integer \(k\ge1\), and every finite-dimensional strategy for the \(k\)-fold repetition,
\[
\begin{aligned}
&\Pr\bigl[W_k\ge\lceil(v+\delta)k\rceil\bigr]\\
&\quad\le\exp\Bigl(-\frac{\kappa_0\delta^5}{1+\log d}\,k\Bigr).
\end{aligned} \tag{2.1}
\]
The same bound holds for the supremum over all such strategies.

The rate does not depend on the question sets, on \(\mu\), or on the dimension of the strategy. The second theorem keeps track of the question distribution. Let \(H=\{(x,y):\mu(x,y)>0\}\), and join two pairs of \(H\) by an edge when they share a question (the same \(x\) or the same \(y\)). For the connected components \(H_j\) of this graph put \(\mu_j=\mu(\,\cdot\mid H_j)\), \(\mu_{j,\min}=\min_{z\in H_j}\mu_j(z)\), and
\[
\kappa_\mu=8\max_j\frac{|H_j|-1}{\mu_{j,\min}} ;
\]
a component with one element contributes \(0\).

**Theorem 2.2** ([OpenAI-TR, Corollary 5.2]). Under the hypotheses of Theorem 2.1, without assuming (S), for every \(0<\delta<1-v\), every \(k\ge1\) and every finite-dimensional strategy,
\[
\begin{aligned}
&\Pr\bigl[W_k\ge\lceil(v+\delta)k\rceil\bigr]\\
&\quad\le\exp\bigl(-\delta^3k/c_\mu\bigr),
\end{aligned} \tag{2.2}
\]
where \(c_\mu=16384(1+\kappa_\mu)(1+\log d)\).

Both bounds apply to the same strategy, so the larger rate may be used. Theorem 2.2 is proved in full in [A cubic bound for a fixed question distribution](a-cubic-bound-for-a-fixed-question-distribution.md); Theorem 2.1 is proved in [From conditioning to a threshold bound](from-conditioning-to-a-threshold-bound.md) from the following estimate.

For a strategy for the \(k\)-fold repetition and a set \(C\subseteq\{1,\dots,k\}\) of *tested* coordinates, let
\[
\begin{aligned}
&E_C=\{I_i=1\text{ for every }i\in C\},\\
&p_C=\Pr(E_C).
\end{aligned}
\]
For \(C\ne\{1,\dots,k\}\) with \(p_C>0\), its *conditioning cost* and the *average conditional win rate outside \(C\)* are
\[
\begin{aligned}
\tau(C)&=\frac{\log(1/p_C)+|C|\log d}{k-|C|},\\
\bar s(C)&=\frac1{k-|C|}\sum_{i\notin C}\Pr(I_i=1\mid E_C) .
\end{aligned}
\]

**(S) Song's conditioning estimate** ([Son26, Definition 4.3 and Lemma 4.4]). There is a universal constant \(B_4\ge1\) such that for every finite game \(G\) with \(v=\omega^*(G)<1\), every \(k\ge1\), every finite-dimensional strategy for the \(k\)-fold repetition, and every proper subset \(C\) with \(p_C>0\) and \(\tau(C)\le1\),
\[
\bar s(C)\le v+B_4\,\tau(C)^{1/4}.
\]

Song proves (S) with a smooth version of quantum correlated sampling, using three lemmas of Chapter 6 of [OpenAI-TA] as inputs. These ingredients are not developed in the programme, so (S) is a named hypothesis; the course proves its weaker analogue with constants depending on \(\mu\), which yields Theorem 2.2.

The event that every coordinate is won is contained in the threshold event of (2.1) whenever \(v+\delta\le1\), so threshold bounds imply bounds for winning every coordinate. For classical strategies exponential decay of the probability of winning every coordinate was proved by Raz and given an information-theoretic proof by Holenstein; for entangled strategies it was first established for special classes of games, and Chapter 6 of [OpenAI-TA] proved it for every finite game, with a rate later improved by Song [Son26, Section 1]. When the referee exchanges quantum messages with the players, parallel repetition can behave differently: Bhattacharyya, Mančinska and Zhao give a one-round game with quantum messages whose value without shared entanglement is less than one, while the value of its \(n\)-fold parallel repetition is one for every \(n\ge2\); with shared entanglement and at most three messages, they show that parallel repetition does not increase the value [BMZ].

## 3. One coordinate at a time

**Lemma 3.1** ([OpenAI-TR, Lemma 2.1]). For every finite-dimensional strategy for the \(k\)-fold repetition of \(G\) and every coordinate \(i\), \(\mathbb EI_i\le\omega^*(G)\); hence \(\mathbb EW_k\le k\,\omega^*(G)\). If \(\omega^*(G)=0\), every coordinate is lost almost surely.

*Proof.* Fix \(i\) and fix questions \((x_j,y_j)\) for the coordinates \(j\ne i\). The following is a strategy for one copy of \(G\) on the same shared state: on question \(x\), Alice inserts \(x\) at coordinate \(i\) of the string with the fixed entries \(x_j\), measures the corresponding POVM of the repeated strategy, and answers with coordinate \(i\) of the outcome; Bob does the same with \(y\). Coarse-graining a POVM over the other coordinates gives a POVM, so this is a legal strategy, and its success probability is the conditional probability that coordinate \(i\) is won given the fixed questions. It is at most \(\omega^*(G)\). Averaging over the fixed questions, which have law \(\mu^{\otimes(k-1)}\) and are independent of \((X_i,Y_i)\), gives \(\mathbb EI_i\le\omega^*(G)\). Summing over \(i\) gives the second claim. If \(\omega^*(G)=0\), each nonnegative \(I_i\) has expectation \(0\). \(\square\)

So the expected fraction of wins is at most \(v\); the theorems say that exceeding it by \(\delta\) is exponentially unlikely, even though the wins in different coordinates may be strongly correlated.

## 4. The plan of the proofs

Both theorems follow one pattern. If the upper tail \(\Pr[W_k\ge\lceil(v+\delta)k\rceil]\) is not exponentially small, sampling a short list of coordinates finds a tested set \(C\) whose conditioning cost \(\tau(C)\) is small, while the average conditional win rate outside \(C\), given that all of \(C\) is won, is at least \(v+7\delta/16\). A *conditioning estimate* forbids this: it bounds that conditional win rate by \(v\) plus a function of \(\tau(C)\) that is small when \(\tau(C)\) is small. With the fourth-root error of (S) this gives the rate \(\delta^5\); with the square-root error proved in this course for a fixed question distribution it gives \(\delta^3\).

1. [From conditioning to a threshold bound](from-conditioning-to-a-threshold-bound.md) proves this transfer for any conditioning estimate, deduces Theorem 2.1 from (S), and derives two-sided error amplification.
2. [A common purification of effects](a-common-purification-of-effects.md) represents positive contractions by maps into one common Hilbert space, so that averaging over a question moves the represented vectors by at most an operator entropy gap, and transports answer measurements to these representations.
3. [Conditioning on a tested set](conditioning-on-a-tested-set.md) builds, for each untested coordinate, vectors and local measurements that reproduce the conditional answers exactly, and bounds by an entropy telescope how much these vectors depend on the other player's question.
4. [A cubic bound for a fixed question distribution](a-cubic-bound-for-a-fixed-question-distribution.md) replaces these vectors by one reference vector on each component of the question support, obtains legal one-game strategies, proves a conditioning estimate with square-root error, and concludes Theorem 2.2.

## 5. Exercises

**5.1.** Show that the event that all \(k\) coordinates are won is contained in \(\{W_k\ge\lceil(v+\delta)k\rceil\}\) for \(0<\delta\le1-v\).

**5.2.** Let \(G\) have \(\mathcal X=\mathcal Y=\mathcal A=\mathcal B=\{0,1\}\), \(\mu\) uniform, and \(V=1\) exactly when \(a\oplus b=xy\) (the CHSH game). Compute \(d\), the graph of \(H\) and \(\kappa_\mu\).

**5.3.** For the game of Exercise 5.2, show that a deterministic strategy wins with probability at most \(3/4\), and that \(3/4\) is attained.

**5.4.** Let \(\rho\) be a positive operator of trace one on \(\mathcal H_A\otimes\mathcal H_B\). Write \(\rho=\sum_j\lambda_j|\phi_j\rangle\langle\phi_j|\) and give a unit vector \(\psi\) in \(\mathcal H_A\otimes\mathbb C^n\otimes\mathcal H_B\) whose measurement statistics for operators \(M\otimes I\otimes N\) equal those of \(\rho\).

**5.5.** Let a one-game strategy have success probability \(s\). Show that its \(k\) tensor copies form a strategy for the \(k\)-fold repetition with \(\mathbb EI_i=s\) for every \(i\), and that the indicators \(I_1,\dots,I_k\) are then independent.

## 6. Solutions

**5.1.** On that event \(W_k=k\ge(v+\delta)k\), and \(k\) is an integer, so \(k\ge\lceil(v+\delta)k\rceil\).

**5.2.** \(d=4\). Every pair has positive probability, and any two pairs share a coordinate or are joined through a pair sharing one with each, so \(H\) is connected with \(|H|=4\) and \(\mu_{\min}=1/4\); hence \(\kappa_\mu=8\cdot3/(1/4)=96\).

**5.3.** A deterministic strategy is \(a=f(x)\), \(b=g(y)\). The bit \(f(x)\oplus g(y)\oplus xy\) is \(0\) exactly when the pair \((x,y)\) is won. The sum modulo \(2\) of these four bits is \(1\), since each \(f(x)\) and each \(g(y)\) occurs twice and \(xy=1\) once; so at least one pair is lost. The constant answers \(a=b=0\) win exactly when \(xy=0\), three of four pairs.

**5.4.** Take \(\psi=\sum_j\sqrt{\lambda_j}\,\phi_j\otimes e_j\), with the auxiliary factor \(\mathbb C^n\) placed next to \(\mathcal H_A\) and given to Alice. Then \(\langle\psi,(M\otimes I\otimes N)\psi\rangle\) equals \(\sum_j\lambda_j\langle\phi_j,(M\otimes N)\phi_j\rangle\), which is \(\operatorname{tr}(\rho\,M\otimes N)\).

**5.5.** Use the state \(\psi^{\otimes k}\), regrouped as a vector in \(\mathcal H_A^{\otimes k}\otimes\mathcal H_B^{\otimes k}\), and the product POVMs \(M_{x_1}^{a_1}\otimes\cdots\otimes M_{x_k}^{a_k}\) and \(N_{y_1}^{b_1}\otimes\cdots\otimes N_{y_k}^{b_k}\). The joint law of all questions and answers is then the product of \(k\) copies of the one-game law, so the pairs \((X_i,Y_i,A_i,B_i)\) are independent, each with the one-game law; hence the \(I_i\) are independent with mean \(s\).

## References

- [OpenAI-TR] OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, OpenAI Math Release preprint, 25 September 2026, Theorem 1.1, Lemma 2.1, Corollary 5.2. https://github.com/openai/math/tree/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
- [OpenAI-TA] OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, report, updated 6 August 2026, Chapter 6 (Quantum parallel repetition). https://cdn.openai.com/pdf/ten-proofs-oai.pdf
- [Son26] Z. Song, *Parallel Repetition for Entangled Games with Gap Exponent Three*, Electronic Colloquium on Computational Complexity, TR26-199 (2026), Section 1, Definition 4.3, Lemma 4.4. https://eccc.weizmann.ac.il/report/2026/199/
- [BMZ] A. Bhattacharyya, L. Mančinska and Y. Zhao, *Quantum interaction can superactivate cheating under parallel repetition*, arXiv:2609.31223 (September 2026). https://arxiv.org/abs/2609.31223
