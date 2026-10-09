# A tree of predicted outputs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

We keep the standing data of [Minimal invariant sets and diametral sequences](minimal-invariant-sets-and-diametral-sequences.md) and the point \(x\), the families \(\mathcal G\supseteq\mathcal H_m\) and the points \(b_j=R_j(x)\) of [Resolvents and an anchor point](resolvents-and-an-anchor-point.md). This lesson builds one infinite tree [OpenAI-K, Section 4]. Every node \(v\) carries a map \(G_v\in\mathcal G\), the point \(y_v=G_v(x)\), a positive weight, and, away from the root, a functional \(f_v\) of norm at most \(1\). The tree defines a nonlinear "evaluation": given points at the nodes of one level, each parent applies its map to the weighted average of its children's points, up to the root. In the lesson [Kirk's problem](kirks-problem.md), the points at the bottom level are replaced one at a time by a common point, and the functional \(f_v\) has to detect the resulting change of the root output when the block of leaves below \(v\) switches. The difficulty is that \(f_v\) must be chosen before the weights of \(v\) and its siblings are known. It is chosen to work for a whole compact family of *predicted* root outputs, parametrized by the possible weights (Section 2).

We use: Lemmas 3.1 and 3.3 of the first lesson; from the second lesson, Lemma 2.1, (2.2), Lemma 6.1 and Lemma 6.2; Lemma 1.2 of the first lesson (limits along \(\mathcal U\)) and Mazur's theorem.

## 1. Evaluation on an ordered tree

An *ordered tree* here has a root \(r\) and levels \(L_0=\{r\},L_1,L_2,\dots\), each finite and nonempty. Every node has a finite nonempty ordered list of children in the next level, and \(L_{k+1}\) is ordered by listing the children of the nodes of \(L_k\) in the order of their parents. Write \(\hat v\) for the parent of \(v\), \(p\prec v\) when \(p\) is a proper ancestor of \(v\), and \(p\preceq v\) when \(p\prec v\) or \(p=v\). For \(v\in L_k\) and \(N\ge k\), the set \(B_N(v)=\{s\in L_N:v\preceq s\}\) is a consecutive block of \(L_N\).

Each node \(v\) carries a map \(G_v\in\mathcal G\) and the point \(y_v=G_v(x)\in K\), with \(G_r=\mathrm{Id}\) and \(y_r=x\). Each nonroot node carries a weight \(\alpha_v>0\), and the weights of the children of every node sum to \(1\). The *path weights* are \(W_r=1\) and \(W_v=W_{\hat v}\alpha_v\).

If points \(H_v\in K\) are given at the children of a node \(u\), its *output* is
\[
H_u=G_u\Bigl(\sum_{\hat v=u}\alpha_vH_v\Bigr)\in K.\tag{1.1}
\]
For points \((H_v)_{v\in L_k}\) prescribed on one level, let \(\Phi_k((H_v)_{v\in L_k})\) be the root output obtained by applying (1.1) at all levels above \(L_k\); the maps of the nodes of \(L_k\) are not applied. So \(\Phi_0(H_r)=H_r\).

**Lemma 1.1.** (a) \(\sum_{v\in L_k}W_v=1\), and \(\sum_{s\in B_N(v)}W_s=W_v\).

(b) For outputs \((H_v)\) and \((H'_v)\) prescribed on \(L_k\),
\[
\bigl\|\Phi_k((H_v))-\Phi_k((H'_v))\bigr\|\le\sum_{v\in L_k}W_v\|H_v-H'_v\|.\tag{1.2}
\]

**Proof.** (a) The weights of the children of \(u\) sum to \(1\), so the path weights of the children of \(u\) sum to \(W_u\); induction on the level. (b) At a node \(u\), since \(G_u\) is nonexpansive, the difference of the outputs is at most \(\sum_{\hat v=u}\alpha_v\|H_v-H'_v\|\). Induction up the tree multiplies the weights along each path. \(\square\)

In particular, changing only the output at \(v\in L_k\) changes the root output by at most \(W_v\) times the change at \(v\), and the root changes by at most the largest change on the level.

## 2. Predicted root outputs

The tree is built level by level, and the nodes of a level \(k\ge1\) are chosen one at a time as *candidates*: parent by parent from left to right, and for each parent in the order of selection. Some candidates are later discarded. When a candidate \(v\) of level \(k\) is about to be chosen, all levels above \(k\) are complete, with their maps and weights. Let \(I_v\) be the list of the candidates of level \(k\) selected before \(v\), retained or discarded; for \(h\in I_v\) we know its point \(y_h\) and its parent \(\hat h\in L_{k-1}\). Put
\[
\Theta_v=\Bigl\{(\theta_h)_{h\in I_v}:\theta_h\ge0,\ \sum_{h\in I_v,\ \hat h=p}\theta_h\le1\ \text{ for every }p\in L_{k-1}\Bigr\},
\]
a compact subset of a finite-dimensional space (a single point if \(I_v\) is empty). For \(b\in K\), \(\theta\in\Theta_v\) and \(p\in L_{k-1}\) put
\[
a_{v,p}(b;\theta)=b+\sum_{h\in I_v,\ \hat h=p}\theta_h(y_h-b),\qquad Q_v(b;\theta)=\Phi_{k-1}\Bigl(\bigl(G_p(a_{v,p}(b;\theta))\bigr)_{p\in L_{k-1}}\Bigr).\tag{2.1}
\]
Each \(a_{v,p}(b;\theta)\) is a convex combination of \(b\) and points \(y_h\), so it lies in \(K\). The point \(Q_v(b;\theta)\) is the root output when, below each parent \(p\), the earlier candidates \(h\) have outputs \(y_h\) and weights \(\theta_h\), and all other children of \(p\) have the common output \(b\). It involves only the levels above \(k\), which are complete.

**Lemma 2.1.** \(\|Q_v(b;\theta)-Q_v(b;\eta)\|\le\sum_{h\in I_v}|\theta_h-\eta_h|\) for all \(b\in K\) and \(\theta,\eta\in\Theta_v\).

**Proof.** \(\|a_{v,p}(b;\theta)-a_{v,p}(b;\eta)\|\le\sum_{\hat h=p}|\theta_h-\eta_h|\,\|y_h-b\|\le\sum_{\hat h=p}|\theta_h-\eta_h|\), since \(\operatorname{diam}K=1\). Apply the nonexpansive maps \(G_p\) and (1.2), with \(W_p\le1\). \(\square\)

For \(\theta\in\Theta_v\) let
\[
Z_v(\theta)=\lim_{j\to\mathcal U}Q_v(b_j;\theta)\quad\text{(weak limit in }K\text{)},\qquad E_v=\{z_1,\dots,z_k\}\cup Z_v(\Theta_v).
\]

**Lemma 2.2.** \(\|Z_v(\theta)-Z_v(\eta)\|\le\sum_{h\in I_v}|\theta_h-\eta_h|\). Hence \(Z_v\) is norm continuous and \(E_v\) is a nonempty norm-compact subset of \(K\), determined before \(v\) is chosen.

**Proof.** The weak limit along \(\mathcal U\) of \(Q_v(b_j;\theta)-Q_v(b_j;\eta)\) is \(Z_v(\theta)-Z_v(\eta)\), since for every \(\ell\in X^*\) the real limits along \(\mathcal U\) are additive. The closed ball of radius \(\sum_h|\theta_h-\eta_h|\) about \(0\) is weakly closed and contains all these differences by Lemma 2.1, so it contains the limit. A continuous image of the compact set \(\Theta_v\) is compact. \(\square\)

The weak limit is taken of points already computed; no weak limit is passed through a nonlinear map.

## 3. The construction

**Proposition 3.1.** Under the standing assumptions there is an infinite ordered tree with maps, points and weights as in Section 1, and with numbers \(e_v>0\) and functionals \(f_v\in X^*\), \(\|f_v\|\le1\), at the nonroot nodes, such that:

(a) \(\sum_{v\neq r}e_v\le\frac1{128}\);

(b) with \(\tau_0=\frac12\) and \(\tau_k=2^{-k-1}\min\{e_u:u\in L_1\cup\dots\cup L_k\}\) for \(k\ge1\), every \(u\in L_k\) satisfies
\[
\Bigl\|\sum_{\hat v=u}\alpha_vy_v-x\Bigr\|\le\tau_k;\tag{3.1}
\]
(c) every nonroot node \(v\) satisfies
\[
\sum_{p\prec v}\|G_p(y_v)-y_v\|\le e_v,\qquad f_v(y_v-z)\ge1-e_v\quad(z\in E_v),\tag{3.2}
\]
where \(E_v\) is the set of Section 2, formed from the candidates selected before \(v\).

**Proof.** Number all candidate selections in the whole construction \(\ell=1,2,\dots\), discarded candidates included, and give the \(\ell\)-th candidate the number \(e_v=2^{-\ell-8}\) when it is about to be selected. The sum of all these numbers is at most \(2^{-8}\), which gives (a).

Suppose the levels \(L_0,\dots,L_{k-1}\) are complete and \(\tau_{k-1}\) is defined. Treat the parents \(u\in L_{k-1}\) from left to right. For \(u\), run the adaptive selection of Lemma 6.1 of the second lesson with tolerance \(\tau_{k-1}\); its successive choices are the candidates for the children of \(u\). Before each choice we prescribe the precision as follows. Let \(v\) be the next candidate, with its number \(e_v\). Form \(I_v\), \(\Theta_v\), \(Q_v\) and \(E_v\) as in Section 2. By Lemma 3.3 of the first lesson, there is \(\delta_v>0\) such that every \(y\in K\) with \(\|Ty-y\|\le\delta_v\) has \(f\in X^*\), \(\|f\|\le1\), with \(f(y-z)\ge1-e_v\) for all \(z\in E_v\). The ancestors of \(v\) are fixed, so \(C_v=\sum_{p\prec v}c_{G_p}\) is a finite number (Lemma 2.1 of the second lesson, \(c_{\mathrm{Id}}=0\)). Prescribe an integer \(m\) with \(\frac1m<\delta_v\) and \(\frac{C_v}m\le e_v\). The selection then chooses \(G_v\in\mathcal H_m\), and \(y_v=G_v(x)\) satisfies \(\|Ty_v-y_v\|\le\frac1m\) by (2.2) of the second lesson. Hence
\[
\sum_{p\prec v}\|G_p(y_v)-y_v\|\le\sum_{p\prec v}c_{G_p}\|Ty_v-y_v\|\le\frac{C_v}m\le e_v,
\]
and there is \(f_v\) as in (3.2); choose it.

The selection for \(u\) stops after finitely many candidates with convex coefficients as in (6.1) of the second lesson, with tolerance \(\tau_{k-1}\). Only now are these coefficients fixed. The candidates with coefficient \(0\) are discarded; the others, in their order of selection, are the children of \(u\), and their coefficients are their weights \(\alpha_v\). This gives (3.1) for \(u\). Discarded candidates stay in the lists \(I\) of later candidates, so nothing already chosen changes. When all parents in \(L_{k-1}\) are treated, the level \(L_k\) is complete, finite and nonempty, and \(\tau_k\) is defined. Continuing level by level constructs the tree. \(\square\)

The numbers \(e_v\) are *budgets*: the construction keeps every error committed at \(v\) below \(e_v\), and the budgets are summable.

## 4. Ideal cutoffs

When the level \(L_k\) is complete, every retained \(v\in L_k\) determines \(\theta^v\in\Theta_v\): \(\theta^v_h=\alpha_h\) if the earlier candidate \(h\) was retained, and \(\theta^v_h=0\) if it was discarded. The sums over a parent group are at most \(1\). Write \(h<_kv\) if \(h\) precedes \(v\) in \(L_k\); these are exactly the retained candidates of level \(k\) selected before \(v\). For \(b\in K\) define the *ideal cutoff* outputs on \(L_k\):
\[
\widetilde H^{v,b}_h=\begin{cases}y_h,&h<_kv,\\ b,&h=v\text{ or }v<_kh.\end{cases}
\]

**Lemma 4.1.** \(\Phi_k\bigl((\widetilde H^{v,b}_h)_{h\in L_k}\bigr)=Q_v(b;\theta^v)\).

**Proof.** For \(p\in L_{k-1}\),
\[
\sum_{\hat h=p}\alpha_h\widetilde H^{v,b}_h=\sum_{\hat h=p,\ h<_kv}\alpha_hy_h+\Bigl(1-\sum_{\hat h=p,\ h<_kv}\alpha_h\Bigr)b=a_{v,p}(b;\theta^v),
\]
because the weights of the children of \(p\) sum to \(1\) and the discarded candidates have \(\theta^v_h=0\). Applying \(G_p\) and then the evaluation above level \(k-1\) gives \(Q_v(b;\theta^v)\). \(\square\)

In a parent group before that of \(v\), every child has its point \(y_h\); in the group of \(v\), the earlier siblings have \(y_h\) and the remaining weight goes to \(b\); in every later group all outputs are \(b\), whatever its children and weights are. This is why the prediction \(Q_v\) could be formed before those later children and their weights existed: the compact set \(E_v\) covers all possible values of the parameter, and the actual one is \(\theta^v\).

## 5. Exercises

**Exercise 5.1** (easy). Show that the order of the children within a parent group and the order of the parent groups are both used in Lemma 4.1, and describe the ideal cutoff when \(v\) is the first node of \(L_k\) and when it is the last.

**Exercise 5.2** (easy). Show that \(\tau_k\le2^{-k-1}e_v\) for every \(v\in L_1\cup\dots\cup L_k\), and that \(\sum_{d\ge k}\tau_d\le2^{-k}\min\{e_u:u\in L_1\cup\dots\cup L_k\}\).

**Exercise 5.3** (medium). Explain why the functional \(f_v\) cannot simply be chosen after the weights of the siblings of \(v\) are fixed: which property of the adaptive selection would be lost?

## 6. Solutions

**5.1.** The ideal cutoff gives \(y_h\) exactly to the nodes preceding \(v\) in \(L_k\), which are the earlier siblings of \(v\) and all nodes in earlier parent groups. If \(v\) is the first node of \(L_k\), every output is \(b\), and \(Q_v(b;\theta^v)=\Phi_{k-1}((G_p(b))_p)\). If \(v\) is the last, every node before it keeps \(y_h\).

**5.2.** \(\tau_k=2^{-k-1}\min\{e_u\}\le2^{-k-1}e_v\). For \(d\ge k\), the minimum defining \(\tau_d\) is over a larger set, so \(\tau_d\le2^{-d-1}\min_{u\in L_1\cup\dots\cup L_k}e_u\), and \(\sum_{d\ge k}2^{-d-1}=2^{-k}\).

**5.3.** The compact detector (Lemma 3.3 of the first lesson) needs the set \(E\) to fix the precision \(\delta\), and the precision must be imposed when \(y_v\) is chosen; it cannot be increased afterwards. The actual parameter \(\theta^v\), and with it the point \(Z_v(\theta^v)\) that \(f_v\) must detect, depends on weights that are fixed only after \(v\) and its later siblings are chosen. Choosing \(f_v\) later does not help, since \(y_v\) is already fixed. Taking \(E_v\) to contain \(Z_v(\theta)\) for every \(\theta\in\Theta_v\) makes the precision independent of the future weights.

## References

- [OpenAI-K] OpenAI, *Fixed points of nonexpansive maps in reflexive Banach spaces*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/blob/main/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026
