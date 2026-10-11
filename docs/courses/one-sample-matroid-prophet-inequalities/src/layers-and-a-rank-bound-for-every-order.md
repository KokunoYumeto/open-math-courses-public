# Layers and a rank bound for every order

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

With the paths of [Density expansions and paths of flats](density-expansions-and-paths-of-flats.md) in hand, this lesson completes the main rule: every arriving candidate is assigned to a *layer*, the difference between two flats of the final path two steps of auxiliary time apart, and is accepted greedily within its layer. Nesting of the flats makes the accepted set independent for every arrival order. Two deterministic estimates follow: a lower bound on the number of acceptances that holds simultaneously for all orders, and a comparison between the final path and a group's own nominal path that charges all later enlargements to a single budget. The remaining lessons show that the quantity appearing in these estimates is large on average.

Notation is that of the previous lessons: the masks \(H,D,C,T\), the candidates, the listed groups \(G_1,\ldots,G_m\) of [Rounding, a maximum rule and candidates](rounding-a-maximum-rule-and-candidates.md), the paths \(X_h\), \(F_h\), the final path \(\widehat F=F_m\), and the nominal births \(b_h(e)\).

## 1. The online decisions

Recall the fair parity \(\varepsilon\in\{0,1\}\) of the main rule. The *layers* are the intervals \((b-2,b]\) of auxiliary time with \(b\equiv\varepsilon\pmod2\); the layer with endpoint \(b\) has *base* \(\widehat F(b-2)\). For each such \(b\) the rule keeps a set \(A_b\), initially empty. If \(m=0\), it rejects every label. Otherwise, at the arrival of a label \(e\) with weight \(w_e\):

1. Reject \(e\) if it is sacrificed (\(e\in H\cup D\cup C\)), if it is not a candidate, or if its rounded weight is not the weight of a listed group. Otherwise let \(h\) be its listed group.
2. Let \(b=b_h(e)\) be its nominal birth. Reject \(e\) unless
\[
\begin{gathered}
e\in T,\quad b\geq a_h+2,\\
b\equiv\varepsilon\pmod2,\\
e\notin\widehat F(b-2).
\end{gathered}\tag{1.1}
\]
A label passing these tests is *eligible* for the layer \((b-2,b]\).
3. Accept the eligible label \(e\) exactly when \(\operatorname{rk}(\{e\}\mid\widehat F(b-2)+A_b)=1\), and then add it to \(A_b\).

By Lemma 2.1(d) of the third lesson, the condition \(b\geq a_h+2\) excludes exactly the labels born at the activation time \(a_h\), those inside \(Q_h(L)\); for every remaining birth the group's expansion is enabled at the base time \(b-2\geq a_h\). The decisions use the revealed weights, the arriving label and its weight, the seed and the earlier decisions, and nothing else.

**Lemma 1.1 (feasibility).** For every seed and every order, the set accepted by the main rule is independent after every arrival.

*Proof.* An eligible label at endpoint \(b\) lies in \(X_h(b)\subseteq\widehat F(b)\) (Lemma 2.1 of the third lesson), so at every moment \(A_b\subseteq\widehat F(b)\), and \(A_b\) is independent over \(\widehat F(b-2)\) because each addition raises the rank of \(\widehat F(b-2)+A_b\) by one. Let \(b_1<b_2<\cdots\) be the endpoints of the chosen parity with \(A_b\neq\varnothing\). Since \(\widehat F\) is increasing, \(A_{b_1}\cup\cdots\cup A_{b_{i-1}}\subseteq\widehat F(b_{i-1})\subseteq\widehat F(b_i-2)\). By the decrease of conditional rank,
\[
\begin{aligned}
&\operatorname{rk}\bigl(A_{b_i}\bigm|A_{b_1}\cup\cdots\cup A_{b_{i-1}}\bigr)\\
&\quad\geq\operatorname{rk}\bigl(A_{b_i}\bigm|\widehat F(b_i-2)\bigr)=|A_{b_i}|,
\end{aligned}
\]
and induction over \(i\) shows that the union is independent. This holds at every moment, whatever the interleaving of arrivals from different layers. \(\square\)

The rule is measurable: the masks are drawn before the arrivals, every density expansion is a maximum over the finitely many flats, by Lemma 2.1 of the third lesson only the times \(a_m-1\leq k\leq0\) matter, rounding has countably many measurable level sets, and all remaining steps are finitely many rank tests and set operations with fixed tie rules. The maximum rule is measurable for the same reasons.

## 2. Competition sets and layer statistics

Lighter labels can fill a layer before a heavier label arrives. The *competition set* of group \(h\) at endpoint \(b\) collects every lighter label that could be eligible for that layer: \(K_{h,b}\) is the set of labels \(e\in T_j\) with \(j<h\) and \(e\in X_j(b)\setminus X_j(b-1)\).
It consists of test-positive labels of lighter listed groups born at \(b\) on their own nominal paths, sacrificed or not, and \(K_{h,b}\subseteq F_{h-1}(b)\), since \(X_j(b)\subseteq F_j(b)\subseteq F_{h-1}(b)\) for \(j<h\). It depends on the masks of the lighter groups only.

For a listed group \(h\) let
\(\mathfrak B_h\) be the set of its *valid endpoints*, the integers \(b\) with \(a_h+2\leq b\leq0\) and \(b\equiv\varepsilon\pmod2\). For \(b\in\mathfrak B_h\) define the *birth set* \(P_{h,b}=G_h\cap(X_h(b)\setminus X_h(b-1))\), and with \(O=D\cup C\) its unrevealed part \(S_{h,b}=P_{h,b}\setminus O\). The labels of \(S_{h,b}\) are candidates of group \(h\) outside \(H\cup D\cup C\), born at a valid endpoint. Write \(\widehat\Omega_b=\widehat F(b-2)\cup K_{h,b}\) and \(\Omega_b=X_h(b-2)\cup K_{h,b}\) for the *final* and the *nominal base* of the layer (the dependence on \(h\) is not shown), and let sums over \(b\) run over \(\mathfrak B_h\). Define the two statistics
\[
\lambda_h=\sum_b\operatorname{rk}\bigl(T_h\cap S_{h,b}\bigm|\widehat\Omega_b\bigr)
\]
and
\[
z_h=\sum_b\operatorname{rk}\bigl(S_{h,b}\bigm|\Omega_b\bigr).\tag{2.1}
\]
Both depend on the seed but not on the arrival order. The statistic \(z_h\) uses the group's own nominal path and ignores the test mask \(T_h\); the eighth lesson shows that it is large in expectation. The statistic \(\lambda_h\) is what the next lemma converts into acceptances.

## 3. Acceptances in every order

For a listed group \(h\) and an order \(\pi\) let \(N_{\geq h}(\pi)\) be the number of accepted labels whose rounded weight is at least the weight of \(G_h\).

**Lemma 3.1 (order-uniform rank bound).** For every seed and every order \(\pi\), \(N_{\geq h}(\pi)\geq\lambda_h\).

*Proof.* Fix \(b\in\mathfrak B_h\), put \(F=\widehat F(b-2)\), and let \(E_b\) be the set of labels eligible for the layer \((b-2,b]\). The acceptances in this layer are exactly the greedy scan of Lemma 1.4 of the first lesson, applied to \(E_b\) over \(F\) in the order of arrival; other layers do not affect it. So the final set \(A_b\) is independent over \(F\) and \(E_b\subseteq\operatorname{cl}(F\cup A_b)\). Split \(A_b=L_b\sqcup H_b\), where \(L_b\) consists of the labels of rounded weight smaller than the weight of \(G_h\). Since \(A_b\) is independent over \(F\), \(H_b\) is independent over \(F\cup L_b\), and since \(F\cup A_b\) spans \(E_b\),
\[
\begin{aligned}
|H_b|&=\operatorname{rk}(H_b\mid F+L_b)\\
&=\operatorname{rk}(E_b\mid F+L_b).
\end{aligned}
\]
Every label of \(T_h\cap S_{h,b}\) outside \(F\) is eligible for this layer: it is an unsacrificed candidate of the listed group \(h\), test-positive, born at \(b\) with \(b\in\mathfrak B_h\). Labels inside \(F\) contribute no conditional rank over \(F\). Every label of \(L_b\) is test-positive, belongs to a lighter listed group \(j<h\), and is born at \(b\) on \(X_j\); so \(L_b\subseteq K_{h,b}\). By the decrease of conditional rank,
\[
\begin{aligned}
|H_b|&\geq\operatorname{rk}\bigl(T_h\cap S_{h,b}\bigm|F+L_b\bigr)\\
&\geq\operatorname{rk}\bigl(T_h\cap S_{h,b}\bigm|F+K_{h,b}\bigr).
\end{aligned}
\]
The sets \(H_b\) for different \(b\) are disjoint and consist of accepted labels of weight at least that of \(G_h\). Summing over \(b\in\mathfrak B_h\) proves the lemma. \(\square\)

The bound holds for every order *simultaneously*: \(\lambda_h\) is computed from the seed alone. Enlarging the competition set to all lighter test-positive labels born at \(b\), including sacrificed ones that will never be accepted, only weakens the bound.

## 4. One budget for later enlargements

The final path \(\widehat F\) is larger than the nominal path \(X_h\), because heavier groups add their own expansions and guards, and \(h\) adds its guards. Enlarging a base can only lower conditional rank. The next lemma bounds the total loss over all layers by one budget.

**Lemma 4.1 (telescoping rank cost).** For every listed group \(h\),
\[
\begin{aligned}
&\sum_b\operatorname{rk}\bigl(S_{h,b}\bigm|\widehat\Omega_b\bigr)\\
&\quad\geq z_h-c_h,
\end{aligned}\tag{4.1}
\]
where \(c_h=|C_h|+\sum_{j>h}\bigl(|C_j|+|D_j|/\kappa\bigr)\).

*Proof.* Let \(J_j\) be the generators of Lemma 3.1 of the third lesson, and put
\[
J=C_h\cup\bigcup_{j>h}\bigl(C_j\cup J_j\bigr),\qquad|J|\leq c_h.
\]
First, for every \(k\),
\[
\begin{aligned}
X_h(k)&\subseteq\widehat F(k)\\
&\subseteq\operatorname{cl}\bigl(X_h(k)+J\bigr).
\end{aligned}\tag{4.2}
\]
The first inclusion is Lemma 2.1 of the third lesson. For the second, \(F_h(k)\subseteq\operatorname{cl}(X_h(k)+C_h)\); and if \(F_{j-1}(k)\subseteq\operatorname{cl}(X_h(k)+J)\) for some \(j>h\), then \(X_j(k)=\operatorname{cl}(F_{j-1}(k)+J_j(k))\) and \(F_j(k)\subseteq\operatorname{cl}(X_j(k)+C_j)\) lie in \(\operatorname{cl}(X_h(k)+J)\) too. Induction up to \(j=m\) gives (4.2).

Fix \(b\in\mathfrak B_h\) and abbreviate \(A=\Omega_b\) and \(S=S_{h,b}\). By (4.2), \(A\subseteq\widehat\Omega_b\subseteq\operatorname{cl}(A\cup J)\), so
\[
\operatorname{rk}(S\mid\widehat\Omega_b)\geq\operatorname{rk}(S\mid A\cup J).
\]
Expanding both sides into ranks of unions gives the exchange identity
\[
\begin{aligned}
&\operatorname{rk}(S\mid A)-\operatorname{rk}(S\mid A\cup J)\\
&\quad=\operatorname{rk}(J\mid A)-\operatorname{rk}(J\mid A\cup S).
\end{aligned}
\]
Now \(X_h(b-2)\subseteq A\) and \(A\cup S\subseteq X_h(b)\), because \(K_{h,b}\subseteq F_{h-1}(b)\subseteq X_h(b)\) and \(S\subseteq P_{h,b}\subseteq X_h(b)\). The decrease of conditional rank gives
\[
\begin{aligned}
&\operatorname{rk}(S\mid A)-\operatorname{rk}(S\mid A\cup J)\\
&\quad\leq\operatorname{rk}\bigl(J\bigm|X_h(b-2)\bigr)-\operatorname{rk}\bigl(J\bigm|X_h(b)\bigr).
\end{aligned}
\]
The endpoints of \(\mathfrak B_h\) are consecutive integers of one parity, so the right sides telescope when summed over \(b\in\mathfrak B_h\): the total is at most \(\operatorname{rk}(J)\leq|J|\leq c_h\). Summing the loss bounds, and recalling the definition (2.1) of \(z_h\), proves (4.1). \(\square\)

No independence of \(J\) and no separate budget per layer is needed: one set of at most \(c_h\) labels pays for every enlargement at every time. In expectation \(c_h\) is small: the guard masks have rate \(t\), and the density generators of heavier groups cost a factor \(1/\kappa\) of their revealed labels.

## 5. Exercises

**5.1.** Show that an eligible label for the layer \((b-2,b]\) lies in \(\widehat F(b)\setminus\widehat F(b-2)\), and that two layers of the chosen parity never share an eligible label.

**5.2.** In the uniform matroid of rank two on labels \(x,y,z\), suppose \(\widehat F(b-2)=L=\varnothing\), \(\widehat F(b)=\{x,y,z\}\), and all three labels are eligible for the layer \((b-2,b]\). Which labels are accepted when they arrive in the order \(z,x,y\)? Compare with Lemma 1.4 of the first lesson.

**5.3.** Prove the exchange identity used in the proof of Lemma 4.1.

**5.4.** Why does Lemma 3.1 count only labels of weight at least that of \(G_h\), and why is it harmless that \(K_{h,b}\) contains sacrificed labels?

**5.5.** Describe a situation in which \(\lambda_h=0\) although a label of group \(h\) is accepted in every order.

## 6. Solutions

**5.1.** An eligible label \(e\) of group \(h\) born at \(b\) lies in \(X_h(b)\subseteq\widehat F(b)\), and (1.1) demands \(e\notin\widehat F(b-2)\). Its nominal birth determines its layer uniquely.

**5.2.** The base is empty and the rank is two. The label \(z\) is accepted, \(x\) is accepted (\(\{z,x\}\) is independent), and \(y\) is rejected, being spanned by \(\{z,x\}\). Two labels are accepted, the rank of the eligible set over the base, as Lemma 1.4 of the first lesson predicts for every order.

**5.3.** Both sides equal
\[
\begin{aligned}
&\operatorname{rk}(S\cup A)+\operatorname{rk}(J\cup A)\\
&\quad-\operatorname{rk}(A)-\operatorname{rk}(S\cup J\cup A).
\end{aligned}
\]

**5.4.** Lighter accepted labels in the same layer may block the labels of group \(h\); the bound keeps those blockers on the conditioning side and counts only the heavier acceptances \(H_b\). The competition set is used only as a conditioning set, and a larger conditioning set gives a smaller conditional rank; so including labels that never arrive as eligible makes the bound weaker, never false.

**5.5.** Suppose that, for the only valid endpoint \(b\) with \(T_h\cap S_{h,b}\neq\varnothing\), this set is a single label \(y\notin\widehat F(b-2)\), and that \(K_{h,b}\) contains a label \(x\) of a lighter group with \(\operatorname{rk}\{x,y\}=1\) which is sacrificed, say \(x\in D\). Then \(y\in\operatorname{cl}(K_{h,b})\), so \(\lambda_h=0\). But \(x\) is never eligible; if \(y\notin\operatorname{cl}(\widehat F(b-2)\cup(E_b\setminus\{y\}))\), where \(E_b\) is the eligible set of the layer, then \(y\) is accepted at its arrival in every order. The bound treats every potential competitor as present.

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 6. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
- [FSZ] M. Feldman, O. Svensson and R. Zenklusen, *A simple O(log log(rank))-competitive algorithm for the matroid secretary problem*, arXiv:1404.4473 (https://arxiv.org/abs/1404.4473); their Section 3 also selects greedily in alternating restrictions and contractions of nested flats.
