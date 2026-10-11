# Rounding, a maximum rule and candidates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the construction of the fixed-vector rule of Proposition 4.1 of [Prophets, matroids and an almighty adversary](prophets-matroids-and-an-almighty-adversary.md). Throughout, \(M=(E,\mathcal I)\) is a finite matroid with a fixed label order, and \(w\in[0,\infty)^E\) is a fixed hidden weight vector. The rule rounds weights to powers of a large base; with probability one half it runs a simple rule aimed at the single most valuable label; otherwise it sacrifices four random masks and keeps only labels that are not spanned by more valuable sacrificed labels. These *candidates* carry, in expectation, at least half of the rounded optimum and at most all of it.

## 1. Constants and rounding

The rule uses five fixed constants:
\[
\begin{gathered}
B=2^{32},\quad\kappa=2^{100},\\
t=2^{-140},\quad\eta=2^{-12},\\
\gamma=\frac\eta{16}=2^{-16}.
\end{gathered}
\]
The base \(B\) separates weight levels; \(\kappa\) is the price per unit of rank in the density expansions of the third lesson; \(t\) is the sparsity of two of the masks; \(\eta\) and \(\gamma\) appear in the analysis of the sixth and eighth lessons. The values are far from optimal; they are chosen so that every loss in the final count is small.

For \(w_e>0\) let \(u_e=B^{\lfloor\log_Bw_e\rfloor}\), the largest power of \(B\) with integer exponent not exceeding \(w_e\), and let \(u_e=0\) when \(w_e=0\). Write \(u(X)=\sum_{e\in X}u_e\) and
\[
W=\mathrm{OPT}_M(u).
\]

**Lemma 1.1 (rounding).** \(\mathrm{OPT}_M(w)/B\leq W\leq\mathrm{OPT}_M(w)\).

*Proof.* For every label \(u_e\leq w_e\), and \(w_e<Bu_e\) when \(w_e>0\). So \(u(I)\leq w(I)\) and \(w(I)\leq Bu(I)\) for every \(I\), and both inequalities pass to the maxima over independent sets. \(\square\)

From now on the *priority order* ranks labels by decreasing rounded weight \(u_e\), with ties broken by the label order. Let \(I^*\) be the set chosen by priority greedy for the weights \(u\); by Lemma 2.1 of the first lesson, \(I^*\) is independent, \(u(I^*)=W\), and a positive label belongs to \(I^*\) exactly when it is not spanned by the labels of higher priority. Labels of weight zero have the lowest priority, and loops are never chosen. The rule rounds a weight as soon as it learns it; the full vector \(u\) is used only in the analysis.

## 2. The maximum rule

Let \(m_*\) be the largest rounded weight of a positive nonloop, and \(m_*=0\) if there is none.

*The maximum rule.* Draw a mask \(\Xi_{\max}\subseteq E\) containing each label independently with probability \(\frac12\), sacrifice it, and learn the weights on it. At each arrival of a label \(e\notin\Xi_{\max}\), accept \(e\) if nothing has been accepted yet, \(e\) is a positive nonloop, and \(e\) has higher priority than every positive nonloop in \(\Xi_{\max}\). Accept nothing else.

**Lemma 2.1.** The maximum rule accepts at most one label, a nonloop, so its accepted set is independent for every order. For every seed write \(A_{\max}(\pi)\) for its accepted set under the order \(\pi\). Then
\[
\mathbb E\bigl[\min_\pi u(A_{\max}(\pi))\bigr]\geq\frac{m_*}4.
\]

*Proof.* A single nonloop is independent. If there is no positive nonloop, the bound is trivial. If there is exactly one, \(e_1\), then with probability \(\frac12\) it is not in the mask; the mask then contains no positive nonloop, so \(e_1\) is accepted in every order, with \(u_{e_1}=m_*\). If there are at least two, let \(e_1\) and \(e_2\) be the first two positive nonloops in priority order, so \(u_{e_1}=m_*\). With probability \(\frac14\) the mask contains \(e_2\) but not \(e_1\). On this event every positive nonloop of higher priority than all masked positive nonloops has higher priority than \(e_2\), and \(e_1\) is the only such label; so \(e_1\) is accepted at its arrival, whatever the order. \(\square\)

The guarantee is useful when one label carries a substantial part of the rounded optimum; the ninth lesson uses it when \(m_*>W/(8\kappa)\).

## 3. Four masks and the candidates

The *main rule* draws four masks \(H,D,C,T\subseteq E\): every label belongs to each of them independently, with probabilities
\[
\begin{gathered}
\Pr(e\in H)=\tfrac12,\quad\Pr(e\in D)=\tfrac14,\\
\Pr(e\in C)=\Pr(e\in T)=t,
\end{gathered}
\]
all \(4|E|\) events being independent. It also draws a fair *parity* \(\varepsilon\in\{0,1\}\). The labels of \(H\cup D\cup C\) are sacrificed: their weights are revealed before the arrivals and they are rejected. Membership in \(T\) reveals nothing and forces nothing; it is consulted at arrival. The roles are:

- \(H\) (*half*) filters labels by the span of more valuable sacrificed labels;
- \(D\) (*density*) tells which weight levels occur and supplies the counts used by the density expansions;
- \(C\) (*guards*) enlarges flats one auxiliary step early;
- \(T\) (*test*) thins the labels eligible for acceptance.

The complete rule chooses, by an independent fair coin, either the maximum rule or the main rule. All coins of both rules are drawn before the arrivals, independently of \(w\). The sacrificed set is \(\Xi_{\max}\) or \(H\cup D\cup C\) according to the coin, a function of the seed, as the fixed-vector formulation requires.

For a label \(e\) let \(H_{>e}\) be the set of labels of \(H\) with higher priority than \(e\). The *candidates* are the labels \(e\notin H\) with \(u_e>0\) and \(e\notin\operatorname{cl}(H_{>e})\); they form the set \(U\). The comparison set is \(Y=I^*\setminus H\).
Whether \(e\) is a candidate can be decided as soon as \(w_e\) is known, because the weights on \(H\) are revealed. A loop lies in \(\operatorname{cl}(\varnothing)\subseteq\operatorname{cl}(H_{>e})\), so every candidate is a nonloop. The set \(U\) need not be independent (Exercise 5.4).

**Lemma 3.1 (candidate mass).** The set \(Y\) is independent, \(Y\subseteq U\), and
\[
\begin{gathered}
\mathbb E_H\,u(Y)=\frac W2,\\
\mathbb E_H\,u(U)\leq W.
\end{gathered}\tag{3.1}
\]

*Proof.* \(Y\subseteq I^*\) is independent. A label \(e\in I^*\) is positive and not spanned by the labels of higher priority; \(H_{>e}\) is a set of such labels, so \(e\notin\operatorname{cl}(H_{>e})\) (Lemma 1.3(a) of the first lesson), and \(Y\subseteq U\). Each label of \(I^*\) avoids \(H\) with probability \(\frac12\), so \(\mathbb E\,u(Y)=u(I^*)/2=W/2\).

For the second bound let \(G_H\) be the set chosen by priority greedy from the positive labels of \(H\). Scanning \(H\) in priority order, the labels accepted before a positive \(e\in H\) span exactly \(H_{>e}\) (Lemma 1.4 of the first lesson; labels of weight zero have lower priority than \(e\)), so \(e\in G_H\) if and only if \(e\notin\operatorname{cl}(H_{>e})\). Fix a positive label \(e\) and condition on the memberships in \(H\) of all labels of higher priority. Then the event \(e\notin\operatorname{cl}(H_{>e})\) is determined, while \(e\notin H\) and \(e\in H\) each have conditional probability \(\frac12\). Hence
\[
\begin{aligned}
\Pr(e\in U)&=\Pr\bigl(e\notin H,\ e\notin\operatorname{cl}(H_{>e})\bigr)\\
&=\Pr\bigl(e\in H,\ e\notin\operatorname{cl}(H_{>e})\bigr)\\
&=\Pr(e\in G_H).
\end{aligned}
\]
Multiplying by \(u_e\) and summing over positive labels gives \(\mathbb E\,u(U)=\mathbb E\,u(G_H)\leq W\), because \(G_H\) is independent. \(\square\)

## 4. Weight groups

Condition on \(H\). The *true weight groups* are
\[
\begin{gathered}
U_i=\{e\in U:u_e=B^i\},\\
n_i=|U_i|,\qquad Y_i=Y\cap U_i\qquad(i\in\mathbb Z).
\end{gathered}
\]
They are fixed once \(H\) is fixed; only finitely many are nonempty. A group is *listed* if \(D\cap U_i\neq\varnothing\). Enumerate the listed groups from lower to higher weight as \(G_1,\ldots,G_m\), and put \(D_h=D\cap G_h\), \(C_h=C\cap G_h\) and \(T_h=T\cap G_h\) for \(1\leq h\leq m\).
The rule knows \(m\), the weights \(B^i\) of the listed groups, and the complete sets \(D_h\) and \(C_h\) before any arrival: every label of \(D\cup C\) is revealed, and its candidate test needs only its own weight and the weights on \(H\). The rule does not know the groups \(G_h\) themselves, since most candidates are unrevealed, nor the sizes \(n_i\). The listed index \(h\) of a group depends on \(D\): it is one more than the number of listed groups of lower weight.

The next lessons build, for each listed group, a path of flats from \(D_h\), \(C_h\) and the matroid alone; the analysis then shows that the unrevealed labels of \(G_h\) supply rank in proportion to \(|Y_i|\), up to losses controlled by \(\kappa\), \(t\) and \(B\).

## 5. Exercises

**5.1.** Show by an example with one label that the factor \(B\) in Lemma 1.1 cannot be replaced by a smaller constant.

**5.2.** Two positive nonloops have rounded weights \(m>m'\), and all other labels have weight zero. Compute \(\mathbb E[\min_\pi u(A_{\max}(\pi))]\) exactly.

**5.3.** In the uniform matroid of rank one, let the positive labels in priority order have rounded weights \(v_1\geq v_2\geq\cdots\geq v_k\). Compute \(\Pr(e\in U)\) for the \(j\)-th label and verify both parts of (3.1).

**5.4.** Show that \(U\) need not be independent, using the uniform matroid of rank one on two labels.

**5.5.** Why can the maximum rule not simply accept the first arriving positive nonloop of rounded weight \(m_*\)?

## 6. Solutions

**5.1.** For \(w_e=B-\delta\) with small \(\delta>0\), \(u_e=1\), so \(\mathrm{OPT}_M(w)/W=B-\delta\), arbitrarily close to \(B\).

**5.2.** Let \(e_1,e_2\) be the two labels, \(e_1\) of higher priority. With probability \(\frac14\) only \(e_2\) is masked and \(e_1\) is accepted: reward \(m\). With probability \(\frac14\) neither is masked; no positive nonloop is masked, so the first arriving positive nonloop is accepted, and the adversary sends \(e_2\) first: reward \(m'\). If \(e_1\) is masked, \(e_2\) is not of higher priority than \(e_1\), and nothing is accepted. The value is \((m+m')/4\).

**5.3.** In rank one every nonloop spans the whole matroid. The \(j\)-th label is a candidate exactly when it is not in \(H\) and no label of higher priority is in \(H\): probability \(2^{-j}\). So \(\mathbb E\,u(U)=\sum_jv_j2^{-j}\leq v_1=W\). Here \(I^*\) is the first label, and \(\mathbb E\,u(Y)=v_1/2=W/2\).

**5.4.** With two labels \(a,b\), \(a\) of higher priority, and \(H=\varnothing\) (probability \(\frac14\)), both are candidates, and \(\{a,b\}\) is dependent in rank one.

**5.5.** The rule does not know \(m_*\): weights are hidden, and only the masked labels are revealed in advance. The mask plays the role of the sample: a masked label of high priority sets a threshold that the most valuable unmasked label can pass.

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
