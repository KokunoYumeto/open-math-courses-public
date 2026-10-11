# Reverse exposure and safe samples

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A label of a heavy group can be blocked in its layer by lighter labels. This lesson shows that a constant fraction of the revealed labels of a group are *safe*: born at a valid endpoint and not captured by the density expansion of the layer's base together with all lighter competitors. The guards of [Density expansions and paths of flats](density-expansions-and-paths-of-flats.md) provide the protection. To analyse them, the guard bits are read backwards in auxiliary time. The certificate bound of [Disjoint certificates](disjoint-certificates.md) shows that a label usually leaves its nominal path at a step where its chance of leaving is not small. A second, *hybrid* transition, using the test bits of the departing labels, turns this into safety.

Throughout this lesson \(H\) and \(D\) are fixed. So the candidates, the listed groups \(G_1,\ldots,G_m\), the sets \(D_j\), the comparison set \(Y\) of [Rounding, a maximum rule and candidates](rounding-a-maximum-rule-and-candidates.md), and every density map \(Q_j\) are fixed. We also fix a listed group \(h\). The randomness is in the guard mask \(C\), the test mask \(T\) and the parity \(\varepsilon\), all independent with the laws of the second lesson. Probabilities and expectations are conditional on \(H,D\). The guard mask is drawn before the arrivals and may be known to the adversary; reading it backwards is only a way of computing probabilities.

## 1. The safe count

Recall the competition sets \(K_{h,b}\) of [Layers and a rank bound for every order](layers-and-a-rank-bound-for-every-order.md). Let \(\sigma_h\) be the number of labels \(d\in D_h\cap Y\) whose nominal birth \(b=b_h(d)\) satisfies
\[
\begin{gathered}
a_h+2\leq b\leq0,\quad b\equiv\varepsilon\pmod2,\\
d\notin Q_h\bigl(F_{h-1}(b-2)+K_{h,b}\bigr).
\end{gathered}
\]
A label counted here is *safe*. The rule does not compute \(\sigma_h\); it is a quantity of the analysis, used in the eighth lesson. The aim of this lesson is:

**Lemma 1.1 (safe samples).** For every listed group \(h\),
\[
\mathbb E[\sigma_h\mid H,D]\geq\frac\eta4|D_h\cap Y|-\frac{|D_h|}\kappa.
\]

## 2. The reverse computation

Let \(G=G_1\cup\cdots\cup G_h\). For a time \(k<0\), a *state* \(S=(S_1,\ldots,S_h)\) of flats and a bit vector \(c\in\{0,1\}^G\), identified as in the fifth lesson with the set of its ones, define the one-step map \(\mathcal G_k(c,S)=(N_1,\ldots,N_h)\) by setting, for \(1\leq j\leq h\),
\[
\begin{aligned}
\Phi_0&=F_0(k),\\
N_j&=Q_{j,k}(\Phi_{j-1}),\\
\Phi_j&=\operatorname{cl}\bigl(N_j+(c\cap G_j\cap S_j)\bigr).
\end{aligned}
\]
Write \(X(k)=(X_1(k),\ldots,X_h(k))\) and compare states coordinatewise.

**Lemma 2.1.** (a) If \(k\leq k'\), \(S\subseteq S'\) and \(c\leq c'\), then \(\mathcal G_k(c,S)\subseteq\mathcal G_{k'}(c',S')\).

(b) \(X(k)=\mathcal G_k(C,X(k+1))\) for every \(k<0\), where \(C\) is read as its indicator vector.

(c) For the actual state \(S=X(k+1)\) and every \(c\), the output satisfies \(N_j\subseteq S_j\) for all \(j\).

*Proof.* (a) By induction on \(j\): \(\Phi_0=F_0(k)\subseteq F_0(k')\), the maps \(Q_{j,k}\) increase in \(k\) and in their argument, and the adjoined sets grow with \(S\) and \(c\).

(b) By induction on \(j\), \(\Phi_{j-1}=F_{j-1}(k)\), so \(N_j=Q_{j,k}(F_{j-1}(k))=X_j(k)\) and \(\Phi_j=\operatorname{cl}(X_j(k)+\Gamma_j(k))=F_j(k)\).

(c) By induction, \(\Phi_{j-1}\subseteq F_{j-1}(k+1)\): this holds for \(j=1\); then \(N_j\subseteq Q_{j,k+1}(F_{j-1}(k+1))\), which is \(X_j(k+1)=S_j\); and \(\Phi_j\), the closure of subsets of the flat \(S_j\), lies in \(S_j\subseteq F_j(k+1)\). \(\square\)

*The reverse computation.* Start from \(X(0)=(E,\ldots,E)\) and compute \(X(-1),X(-2),\ldots,X(a_h-1)\) by Lemma 2.1(b), reading guard bits only when needed. At the step computing \(X(k)\) from \(S=X(k+1)\), for \(j=1,\ldots,h\) in turn: compute \(N_j\) from \(\Phi_{j-1}\), then read the bits of \(C\) on \(G_j\cap(S_j\setminus N_j)\) in label order. The bits on \(G_j\cap N_j\) are not needed, since those labels already lie in \(N_j\). The set of coordinates read for group \(j\) is decided before any of them is read, from the bits of lighter groups read at this step. Since \(N_j=X_j(k)\), the coordinates read are the labels of \(G_j\) born at time \(k+1\); so each guard bit is read at most once, at the step where its label leaves its nominal path in reverse.

For \(b\leq0\) let \(\mathcal H_b\) be the \(\sigma\)-field of the transcript of the steps computing \(X(-1),\ldots,X(b)\); it determines \(X(b)\), and \(\mathcal H_b\subseteq\mathcal H_{b-1}\). The unread bits after this transcript are those on \(\bigcup_{j\leq h}G_j\cap X_j(b)\). By Lemma 1.1 of the fifth lesson they are, conditionally on \(\mathcal H_b\), independent with rate \(t\). Consequently, conditionally on \(\mathcal H_b\), the next state \(X(b-1)\) has the law of \(\mathcal G_{b-1}(\xi,X(b))\), where \(\xi\) is a vector of independent rate-\(t\) bits on \(G\): only the bits on \(G_j\cap X_j(b)\) enter, and those are fresh.

*Exit probabilities.* Fix a nonloop \(d\in G_h\). It lies in \(X_h(0)=E\) and not in \(X_h(a_h-1)=L\), so it leaves the nominal path at exactly one step: \(d\in X_h(b)\setminus X_h(b-1)\) for \(b=b_h(d)\). For \(a_h\leq b\leq0\) write \(\chi_b=\mathbf 1\{d\in X_h(b)\}\); let \(p_b=0\) if \(d\notin X_h(b)\), and otherwise
\[
p_b=\Pr\bigl(d\notin X_h(b-1)\bigm|\mathcal H_b\bigr).
\]
Then \(p_b\) is \(\mathcal H_b\)-measurable, and \(\mathbb E[\chi_bp_b]\) is the probability that \(d\) leaves at the step from \(b\) to \(b-1\).

**Lemma 2.2 (monotone exit probabilities).** On the event \(d\in X_h(b-1)\), \(p_{b-1}\geq p_b\).

*Proof.* With \(\xi\) fresh, \(p_b=\Pr(d\notin\mathcal G_{b-1}(\xi,X(b))_h)\) and \(p_{b-1}=\Pr(d\notin\mathcal G_{b-2}(\xi,X(b-1))_h)\), the probabilities being over \(\xi\) with the states fixed. Since \(X(b-1)\subseteq X(b)\), Lemma 2.1(a) gives \(\mathcal G_{b-2}(\xi,X(b-1))\subseteq\mathcal G_{b-1}(\xi,X(b))\) for every \(\xi\), so \(d\) is missing from the smaller output whenever it is missing from the larger one. \(\square\)

So, read backwards in time, the chance that \(d\) leaves at the next step never decreases while \(d\) remains.

## 3. Exit mass

**Lemma 3.1 (exit mass).** For every nonloop \(d\in G_h\), the probability that \(d\) leaves at a step with \(p_b<\eta\) is less than \(\frac12\), and
\[
\sum_{b=a_h}^0\mathbb E\bigl[\chi_b\,p_b^2\bigr]\geq\frac\eta2.\tag{3.1}
\]

*Proof.* Fix \(p_0\in(0,1]\) and consider the steps \(b\) with \(d\in X_h(b)\) and \(p_b\in[p_0,2p_0)\). By Lemma 2.2 they form a run of consecutive steps, possibly empty, and whether a step is the first of the run is decided by the transcript before it. Condition on such a first step \(b_0\) and on \(\mathcal H_{b_0}\); write \(S^0=X(b_0)\) and \(k_0=b_0-1\). Let \(V_0=\bigcup_jG_j\cap S^0_j\), the coordinates still unread, and consider the event on bit vectors \(c\) on \(V_0\)
\[
\mathcal A=\bigl\{c:\ d\in\mathcal G_{k_0}(c,S^0)_h\bigr\}.
\]
By Lemma 2.1(a) it is increasing, and its failure probability is \(p_{b_0}\geq p_0>0\).

Treat the reads of each step of the run as one transaction of an adaptive procedure on \(V_0\); every later read lies in \(V_0\), because the states only shrink. Call a step of the run successful if \(d\) does not leave there. We claim that at a successful step the bits read at that step with value one, a set \(I\), form a positive certificate for \(\mathcal A\). Let \(S=X(b)\subseteq S^0\) be the actual incoming state and \(k=b-1\leq k_0\), and let \(c^I\) be the vector equal to one exactly on \(I\). Then \(\mathcal G_k(c^I,S)\) equals the actual output \(X(b-1)\): by induction on \(j\) the flats \(\Phi_j\) coincide, since the positive guards of \(G_j\cap S_j\) outside \(N_j\) were read at this step and belong to \(I\), positive guards inside \(N_j\) change no closure, and \(c^I\) has no other ones in \(G_j\cap S_j\). By Lemma 2.1(a), \(\mathcal G_k(c^I,S)\subseteq\mathcal G_{k_0}(c^I,S^0)\). So if \(d\) stays at this step, then \(d\in\mathcal G_{k_0}(c^I,S^0)_h\), that is, \(I\in\mathcal A\). The comparison uses the step's own incoming state; no earlier state is recomputed.

By Lemma 2.1 of the fifth lesson, conditionally on \(\mathcal H_{b_0}\) the expected number of successful steps in the run is at most \(\log(1/p_{b_0})\leq\log(1/p_0)\). The run contains at most one step at which \(d\) leaves. Hence the expected number of steps with \(d\in X_h(b)\) and \(p_b\in[p_0,2p_0)\) is at most \(\log(1/p_0)+1\), and the probability that \(d\) leaves at such a step, the expected sum of \(p_b\) over them, is at most
\[
2p_0\Bigl(\log\frac1{p_0}+1\Bigr).
\]
The bands \([2^{-\ell-1},2^{-\ell})\), \(\ell\geq12\), cover \((0,\eta)\). With \(p_0=2^{-\ell-1}\) and the sums \(\sum_{\ell\geq12}2^{-\ell}=2^{-11}\) and \(\sum_{\ell\geq12}(\ell+1)2^{-\ell}=14\cdot2^{-11}\),
\[
\begin{aligned}
&\sum_{\ell\geq12}2^{-\ell}\bigl((\ell+1)\log2+1\bigr)\\
&\quad=2^{-11}\bigl(14\log2+1\bigr)<\tfrac12.
\end{aligned}
\]
Leaving at a step with \(p_b=0\) has probability zero. This proves the first claim. Hence \(d\) leaves at a step with \(p_b\geq\eta\) with probability more than \(\frac12\); at such steps \(p_b^2\geq\eta p_b\), and summing \(\mathbb E[\chi_bp_b\mathbf 1\{p_b\geq\eta\}]\) over the steps gives (3.1). \(\square\)

## 4. The hybrid transition

Fix an endpoint \(b\) with \(a_h+2\leq b\leq0\) and a transcript \(\mathcal H_b\). Perform the ordinary step from \(S=X(b)\) to \(S'=X(b-1)\), which produces \(\mathcal H_{b-1}\). Define *hybrid bits* \(\widetilde c\) on the coordinates \(G_j\cap S_j\), \(j\leq h\):
\[
\widetilde c_e=\begin{cases}\mathbf 1\{e\in C\},&e\in G_j\cap S'_j,\\ \mathbf 1\{e\in T\},&e\in G_j\cap(S_j\setminus S'_j).\end{cases}
\]
The first line concerns the *staying* labels, whose guard bits the ordinary step did not read; the second concerns the *departing* labels, whose guard bits it did read. Let \(\widetilde N=\mathcal G_{b-1}(\widetilde c,S)\), with intermediate flats \(\widetilde\Phi_j\). The hybrid step starts from the same state as the ordinary one, but uses the test bits of the labels that the ordinary step removed. Let \(\mathcal D_b\) be the *double exit* event that \(d\in X_h(b)\), \(d\notin X_h(b-1)\) and \(d\notin\widetilde N_h\).

**Lemma 4.1 (same law).** Conditionally on \(\mathcal H_{b-1}\), the hybrid bits are independent with rate \(t\). Consequently, on \(\{d\in X_h(b)\}\),
\[
\begin{gathered}
\Pr\bigl(d\notin\widetilde N_h\bigm|\mathcal H_{b-1}\bigr)=p_b,\\
\Pr(\mathcal D_b\mid\mathcal H_b)=p_b^2.
\end{gathered}
\]

*Proof.* Given \(\mathcal H_{b-1}\), the split of the coordinates into staying and departing labels is fixed. The guard bits of staying labels are unread, hence fresh by Lemma 1.1 of the fifth lesson. No test bit occurs in the transcript, and the test mask is independent of \(C\), \(H\), \(D\) and the parity; so the test bits of departing labels are fresh as well, and independent of the guard bits. Both masks have the same rate \(t\); this is essential, since the hybrid bits must have exactly the law of fresh guard bits. Thus \(\widetilde N\) has, given \(\mathcal H_{b-1}\), the law of \(\mathcal G_{b-1}(\xi,X(b))\) with \(\xi\) fresh, which gives the first identity. For the second, the event \(\{d\notin X_h(b-1)\}\) is \(\mathcal H_{b-1}\)-measurable, so by the tower property the probability equals \(\mathbb E[\chi_b\mathbf 1\{d\notin X_h(b-1)\}\,p_b\mid\mathcal H_b]\), and \(p_b\) is \(\mathcal H_b\)-measurable with \(\mathbb E[\mathbf 1\{d\notin X_h(b-1)\}\mid\mathcal H_b]=p_b\) on \(\{d\in X_h(b)\}\). \(\square\)

The same test mask is used for every endpoint; the lemma concerns one endpoint at a time, and no independence between different endpoints is needed.

**Lemma 4.2 (containment).** For every realization of \(C\) and \(T\),
\[
Q_h\bigl(F_{h-1}(b-2)+K_{h,b}\bigr)\subseteq\widetilde N_h.
\]

*Proof.* We show by induction on \(j=0,\ldots,h-1\) that \(\widetilde\Phi_j\) contains \(F_j(b-2)\) and the sets \(T_i\cap(X_i(b)\setminus X_i(b-1))\) for \(i\leq j\). For \(j=0\), \(\widetilde\Phi_0=F_0(b-1)\supseteq F_0(b-2)\). For \(1\leq j\leq h-1\), monotonicity of the enabled expansions gives
\[
\begin{aligned}
\widetilde N_j&=Q_{j,b-1}(\widetilde\Phi_{j-1})\\
&\supseteq Q_{j,b-2}\bigl(F_{j-1}(b-2)\bigr)=X_j(b-2),
\end{aligned}
\]
and \(\widetilde N_j\supseteq\widetilde\Phi_{j-1}\) keeps the earlier test sets. The hybrid bits equal to one on \(G_j\cap S_j\) include \(C_j\cap X_j(b-1)\), the staying guards, and \(T_j\cap(X_j(b)\setminus X_j(b-1))\), the departing test-positive labels. Hence \(\widetilde\Phi_j\) contains \(\operatorname{cl}(X_j(b-2)+\Gamma_j(b-2))\), which is \(F_j(b-2)\); and \(\widetilde\Phi_j\) contains the new test set. At \(j=h-1\) this gives \(\widetilde\Phi_{h-1}\supseteq F_{h-1}(b-2)\cup K_{h,b}\). Since \(b-1\geq a_h\), the expansion \(Q_{h,b-1}=Q_h\) is enabled, and \(\widetilde N_h=Q_h(\widetilde\Phi_{h-1})\), which contains \(Q_h(F_{h-1}(b-2)+K_{h,b})\). \(\square\)

The hybrid step thus contains every lighter competitor that could be eligible at endpoint \(b\), together with the base flat of the layer. If the ordinary step removes \(d\), its nominal birth is \(b\); if the hybrid step also misses \(d\), Lemma 4.2 shows that \(d\) is safe at \(b\), apart from the parity. Write \(\mathrm{Safe}_b\) for the event that \(b_h(d)=b\) and \(d\notin Q_h(F_{h-1}(b-2)+K_{h,b})\). With Lemma 4.1, for \(a_h+2\leq b\leq0\),
\[
\Pr(\mathrm{Safe}_b)\geq\mathbb E\bigl[\chi_b\,p_b^2\bigr].\tag{4.1}
\]
For a fixed \(d\) the events \(\mathrm{Safe}_b\) are disjoint for different \(b\).

## 5. Proof of the safe-sample bound

*Proof of Lemma 1.1.* Let \(d\in D_h\cap Y\); it is a nonloop of \(G_h\). Sum (4.1) over \(a_h+2\leq b\leq0\) and compare with (3.1). Two steps are missing from the sum. At \(b=a_h+1\), \(p_b=0\) whenever \(d\in X_h(a_h+1)\), because \(X_h(a_h)=X_h(a_h+1)=Q_h(L)\) is determined by \(H,D\) (Lemma 2.1(d) of the third lesson). At \(b=a_h\), using \(p^2\leq p\),
\[
\begin{aligned}
\mathbb E\bigl[\chi_{a_h}p_{a_h}^2\bigr]&\leq\Pr\bigl(b_h(d)=a_h\bigr)\\
&=\mathbf 1\{d\in Q_h(L)\}.
\end{aligned}
\]
So the probability that \(d\) is safe at its birth, apart from the parity condition, is at least \(\frac\eta2-\mathbf 1\{d\in Q_h(L)\}\). Summing over \(d\in D_h\cap Y\) and using that \(Y\) is independent, so that \(|D_h\cap Y\cap Q_h(L)|\leq\operatorname{rk}(Q_h(L))\), which is at most \(|D_h|/\kappa\) by Lemma 3.1 of the third lesson, the expected number of such labels is at least \(\frac\eta2|D_h\cap Y|-|D_h|/\kappa\). These events do not involve the parity, which is independent of \(C\) and \(T\); each such label has the chosen parity with probability \(\frac12\). Hence
\[
\mathbb E[\sigma_h\mid H,D]\geq\frac\eta4|D_h\cap Y|-\frac{|D_h|}{2\kappa},
\]
which is stronger than the claim. \(\square\)

## 6. Exercises

**6.1.** Show that during the reverse computation the guard bit of a label \(e\in G_j\) is read exactly at the step computing \(X(b_j(e)-1)\), provided \(b_j(e)\geq a_h\).

**6.2.** Verify \(\sum_{\ell\geq12}(\ell+1)2^{-\ell}=14\cdot2^{-11}\) and estimate \(2^{-11}(14\log2+1)\) numerically.

**6.3.** Suppose the guard mask were empty. Show that every \(p_b\) is \(0\) or \(1\), and that every \(d\in G_h\) born at some \(b\geq a_h+2\) satisfies \(d\notin Q_h(F_{h-1}(b-2))\).

**6.4.** Show that, conditionally on \(\mathcal H_b\), the hybrid output \(\widetilde N\) and the ordinary output \(X(b-1)\) are independent with the same law.

**6.5.** Where do the proofs of this lesson use \(b-1\geq a_h\), and where \(b\geq a_h+2\)?

## 7. Solutions

**6.1.** At the step computing \(X(k)\) the coordinates read for group \(j\) are \(G_j\cap(X_j(k+1)\setminus X_j(k))\), the labels of \(G_j\) born at \(k+1\). So the bit of \(e\) is read when \(k+1=b_j(e)\), and at no other step. The computation stops after \(X(a_h-1)\), so labels born at \(a_h\) or later are read.

**6.2.** The identity \(\sum_{\ell\geq L}\ell x^\ell=x^L\frac{L-(L-1)x}{(1-x)^2}\) at \(x=\frac12\), \(L=12\) gives \(13\cdot2^{-11}\); add \(\sum_{\ell\geq12}2^{-\ell}=2^{-11}\). Numerically \(2^{-11}(14\cdot0.6931+1)\approx2^{-11}\cdot10.70\), about \(0.0052\).

**6.3.** With no guards the paths do not depend on random bits, so given \(H,D\) every exit is certain at the birth step: \(p_b=1\) there and \(p_b=0\) before. A label born at \(b\) lies outside \(X_h(b-1)\), which contains \(X_h(b-2)=Q_h(F_{h-1}(b-2))\) since \(b-2\geq a_h\). (Without the test mask nothing would be eligible, so the rule needs \(T\); the guards are what makes leaving random.)

**6.4.** Given \(\mathcal H_{b-1}\), the law of \(\widetilde N\) is that of \(\mathcal G_{b-1}(\xi,X(b))\), which depends only on \(\mathcal H_b\). So \(\widetilde N\) is conditionally independent of \(\mathcal H_{b-1}\), hence of \(X(b-1)\), given \(\mathcal H_b\); and its conditional law is that of the ordinary step.

**6.5.** Lemma 4.2 needs the focal expansion enabled at time \(b-1\), that is, \(b-1\geq a_h\). The lower bound \(b\geq a_h+2\) excludes the activation birth \(a_h\), whose labels lie in \(Q_h(L)\) and are paid for by the generator budget; a birth at \(a_h+1\) is impossible. In the eighth lesson \(b-2\geq a_h\) is used again, to identify \(X_h(b-2)\) with \(Q_h(F_{h-1}(b-2))\).

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
