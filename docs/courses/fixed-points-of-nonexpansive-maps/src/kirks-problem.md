# Kirk's problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of OpenAI's theorem [OpenAI-K, Section 5]:

**Theorem 4.1** (OpenAI). Let \(X\) be a real reflexive Banach space and \(C\subseteq X\) nonempty, closed, bounded and convex. Every nonexpansive map \(F:C\to C\) has a fixed point.

Assume the contrary, and keep the standing data of the previous lessons: the minimal set \(K\) of diameter \(1\), the map \(T\), the dense sequence \((z_i)\) and the space \(Y\) of [Minimal invariant sets and diametral sequences](minimal-invariant-sets-and-diametral-sequences.md); the point \(x\), the maps \(G\in\mathcal G\) with constants \(c_G\) and the points \(b_j\) of [Resolvents and an anchor point](resolvents-and-an-anchor-point.md); and the tree of [A tree of predicted outputs](a-tree-of-predicted-outputs.md) with its maps \(G_v\), points \(y_v\), weights \(\alpha_v\), path weights \(W_v\), budgets \(e_v\), functionals \(f_v\), sets \(E_v\), parameters \(\theta^v\), tolerances \(\tau_k\) and evaluations \(\Phi_k\).

Fix a depth \(N\). Give every leaf \(s\in L_N\) the output \(y_s\) and replace these outputs one at a time by a common point \(b\), from right to left, recomputing the tree. When the whole block of leaves below a node \(v\) has switched, the root output moves by a vector that \(f_v\) detects with almost full weight \(W_v\) (Lemma 2.1). The root differences of single leaf switches telescope over each block, so one normalized leaf difference \(d_s\) is detected by all the functionals on the path to \(s\) (Proposition 3.1). A compactness argument along an infinite branch then gives one vector of \(Y\) detected by all the functionals of the branch, while these functionals tend to \(0\) on \(Y\).

We use: Lemma 1.2 of the first lesson (limits along \(\mathcal U\)) and Lemma 2.1 there (weak compactness of \(B_Y\)); Lemma 6.2 of the second lesson; and from the third lesson Lemma 1.1, Lemma 2.2, Proposition 3.1 and Lemma 4.1.

## 1. The switching experiment

Fix \(N\ge1\), let \(\mathcal T_N=L_0\cup\dots\cup L_N\), and put \(M_k=\min\{e_v:v\in L_1\cup\dots\cup L_k\}\) for \(1\le k\le N\).

**Lemma 1.1** (a common point). There is \(b\in K\) such that
\[
f_v\bigl(y_v-Q_v(b;\theta^v)\bigr)\ge1-2e_v\quad(v\in\mathcal T_N\setminus\{r\}),\qquad D_N:=\sum_{u\in\mathcal T_N}\|G_u(b)-b\|\le M_N.\tag{1.1}
\]

**Proof.** For \(v\in\mathcal T_N\setminus\{r\}\) the point \(q_v=Z_v(\theta^v)\) lies in \(E_v\), so \(f_v(y_v-q_v)\ge1-e_v\) by (3.2) of the third lesson. Since \(q_v\) is the weak limit along \(\mathcal U\) of \(Q_v(b_j;\theta^v)\), the set of \(j\) with \(f_v(Q_v(b_j;\theta^v))<f_v(q_v)+e_v\) lies in \(\mathcal U\), and for these \(j\) the first inequality holds with \(b=b_j\). By Lemma 6.2 of the second lesson, \(\sum_{u\in\mathcal T_N}\|G_u(b_j)-b_j\|\le\frac1j\sum_uc_{G_u}\to0\), so the second inequality holds for all large \(j\). The finitely many sets of indices involved lie in \(\mathcal U\), so their intersection is not empty; take \(b=b_j\) for \(j\) in it. \(\square\)

Fix such a \(b\). Initially every leaf \(s\in L_N\) has output \(H_s=y_s\); all other outputs are computed by the rule (1.1) of the third lesson. Switch the leaf outputs to \(b\) one at a time, from the last leaf of \(L_N\) to the first, recomputing all outputs after each switch. All outputs lie in \(K\). For a nonroot \(v\in\mathcal T_N\), let \(U_v\) and \(V_v\) be the root outputs immediately before the first and immediately after the last switch of a leaf in the block \(B_N(v)\).

**Lemma 1.2** (unswitched subtrees). If no leaf below \(h\in L_k\) has switched, then
\[
\|H_h-y_h\|\le\varepsilon_{k,N}:=\sum_{d=k}^{N-1}\tau_d,
\]
and for \(k\ge1\), \(\varepsilon_{k,N}\le2^{-k}M_k\le e_v\) for every \(v\in L_k\).

**Proof.** For \(k=N\) both sides vanish. For \(h\in L_k\), \(k<N\), the outputs of its children are unswitched, and \(y_h=G_h(x)\), so
\[
\|H_h-y_h\|\le\Bigl\|\sum_{\hat u=h}\alpha_uH_u-x\Bigr\|\le\sum_{\hat u=h}\alpha_u\|H_u-y_u\|+\Bigl\|\sum_{\hat u=h}\alpha_uy_u-x\Bigr\|\le\varepsilon_{k+1,N}+\tau_k
\]
by induction and (3.1) of the third lesson. For \(d\ge k\ge1\), \(\tau_d\le2^{-d-1}M_k\), so \(\varepsilon_{k,N}\le2^{-k}M_k\), and \(M_k\le e_v\) for \(v\in L_k\). \(\square\)

**Lemma 1.3** (switched subtrees). If all leaves below \(h\) have switched, then \(\|H_h-b\|\le D_N\le M_N\).

**Proof.** At a node \(u\) of this subtree that is not a leaf, \(\|H_u-b\|\le\|G_u(\sum\alpha_wH_w)-G_u(b)\|+\|G_u(b)-b\|\le\sum_{\hat w=u}\alpha_w\|H_w-b\|+\|G_u(b)-b\|\), and \(H_s=b\) at the leaves. Induction gives \(\|H_h-b\|\le\sum_{h\preceq u,\ u\notin L_N}\frac{W_u}{W_h}\|G_u(b)-b\|\le D_N\), since \(W_u\le W_h\) for \(u\) below \(h\). \(\square\)

## 2. Detecting a block

**Lemma 2.1.** For every \(v\in L_k\), \(1\le k\le N\),
\[
\|U_v-y_v\|\le1-W_v+2e_v,\qquad\|V_v-Q_v(b;\theta^v)\|\le e_v,\qquad f_v(U_v-V_v)\ge W_v-5e_v.
\]

**Proof.** *Before the block switches*, no leaf below \(v\) has switched, so \(\|H_v-y_v\|\le e_v\) by Lemma 1.2. Let \(r=p_0,p_1,\dots,p_k=v\) be the path to \(v\). For \(i<k\), the outputs of the children of \(p_i\) and the point \(y_v\) lie in \(K\), which has diameter \(1\), so
\[
\|H_{p_i}-y_v\|\le\Bigl\|\sum_{\hat c=p_i}\alpha_cH_c-y_v\Bigr\|+\|G_{p_i}(y_v)-y_v\|\le\alpha_{p_{i+1}}\|H_{p_{i+1}}-y_v\|+(1-\alpha_{p_{i+1}})+\|G_{p_i}(y_v)-y_v\|.
\]
Unwinding from \(i=0\), and using \(\sum_{i<k}W_{p_i}(1-\alpha_{p_{i+1}})=\sum_{i<k}(W_{p_i}-W_{p_{i+1}})=1-W_v\) and (3.2) of the third lesson,
\[
\|U_v-y_v\|\le W_ve_v+(1-W_v)+\sum_{p\prec v}\|G_p(y_v)-y_v\|\le1-W_v+2e_v.
\]
*After the block switches*, the nodes \(h\in L_k\) preceding \(v\) are unswitched, so \(\|H_h-y_h\|\le e_v\) by Lemma 1.2, and the other nodes of \(L_k\) are fully switched, so \(\|H_h-b\|\le M_N\le e_v\) by Lemma 1.3. These outputs differ from the ideal cutoff \(\widetilde H^{v,b}\) by at most \(e_v\) at every node of \(L_k\). By (1.2) and Lemma 4.1 of the third lesson, \(\|V_v-Q_v(b;\theta^v)\|\le e_v\sum_hW_h=e_v\). Finally, by (1.1),
\[
f_v(U_v-V_v)\ge f_v\bigl(y_v-Q_v(b;\theta^v)\bigr)-\|U_v-y_v\|-\|V_v-Q_v(b;\theta^v)\|\ge(1-2e_v)-(1-W_v+2e_v)-e_v.\qquad\square
\]

## 3. A finite witness

**Proposition 3.1.** For every \(N\ge1\) there are a leaf \(s\in L_N\) and a vector \(d\in B_Y\) with \(f_v(d)\ge\frac12\) for every \(v\neq r\) with \(v\preceq s\).

**Proof.** For a leaf \(s\), only the output at \(s\) changes in its own switch, so by (1.2) of the third lesson \(\|U_s-V_s\|\le W_s\|y_s-b\|\le W_s\). Hence \(d_s=(U_s-V_s)/W_s\) lies in \(B_Y\): it is a multiple of a difference of two points of \(K\), of norm at most \(1\). The leaves of a block \(B_N(v)\) switch consecutively, so the root differences telescope: \(\sum_{s\in B_N(v)}W_sd_s=U_v-V_v\). With \(\sum_{s\in B_N(v)}W_s=W_v\) (Lemma 1.1 of the third lesson) and Lemma 2.1,
\[
\sum_{s\in B_N(v)}W_s\bigl(1-f_v(d_s)\bigr)=W_v-f_v(U_v-V_v)\le5e_v.
\]
Every term is nonnegative, since \(\|f_v\|\le1\) and \(\|d_s\|\le1\). Summing over all nonroot \(v\in\mathcal T_N\) and exchanging the finite sums,
\[
\sum_{s\in L_N}W_s\sum_{v\neq r,\ v\preceq s}\bigl(1-f_v(d_s)\bigr)\le5\sum_{v\neq r}e_v\le\frac5{128}.
\]
If some \(v\) on the path to \(s\) had \(f_v(d_s)<\frac12\), the inner sum for \(s\) would exceed \(\frac12\); so the leaves with this property have total weight less than \(\frac5{64}\). The leaf weights sum to \(1\), so some leaf \(s\) has \(f_v(d_s)\ge\frac12\) for all \(v\) on its path, and \(d=d_s\) works. \(\square\)

## 4. The theorem

**Proof of Theorem 4.1.** Call a node \(v\) *feasible* if some \(d\in B_Y\) satisfies \(f_u(d)\ge\frac12\) for all \(u\neq r\) with \(u\preceq v\). Ancestors of feasible nodes are feasible, and by Proposition 3.1 there are feasible nodes at every depth. Every node has finitely many children, so starting from the root we can repeatedly choose a child with feasible descendants at arbitrarily large depths. This gives a branch \(r,v_1,v_2,\dots\) with \(v_k\in L_k\) and every \(v_k\) feasible.

The sets \(C_k=\{d\in B_Y:f_{v_i}(d)\ge\frac12\text{ for }1\le i\le k\}\) are nonempty, weakly closed in the weakly compact set \(B_Y\), and decreasing; so some \(d\in B_Y\) has \(f_{v_k}(d)\ge\frac12\) for all \(k\).

On the other hand, the functionals \(f_{v_k}\) tend to \(0\) at every point of \(Y\). For fixed \(i,j\) and \(k\ge\max\{i,j\}\), the points \(z_i,z_j\) lie in \(E_{v_k}\), so by (3.2) of the third lesson and \(\operatorname{diam}K=1\),
\[
1-e_{v_k}\le f_{v_k}(y_{v_k}-z_i)\le1,\qquad1-e_{v_k}\le f_{v_k}(y_{v_k}-z_j)\le1,
\]
and \(|f_{v_k}(z_i-z_j)|\le e_{v_k}\), which tends to \(0\) because the budgets are summable. The differences \(z_i-z_j\) span a dense subspace of \(Y\), and \(\|f_{v_k}\|\le1\), so \(f_{v_k}(d')\to0\) for every \(d'\in Y\): for \(a\) in that span, \(|f_{v_k}(d')|\le\|d'-a\|+|f_{v_k}(a)|\). In particular \(f_{v_k}(d)\to0\), a contradiction. Hence no counterexample exists. \(\square\)

**Corollary 4.2.** Every reflexive Banach space has the fixed point property for nonexpansive maps. Equivalently, every nonexpansive self-map of a nonempty weakly compact convex subset of a reflexive Banach space has a fixed point.

**Proof.** The first statement is Theorem 4.1. A weakly compact set \(W\) is weakly closed, hence norm closed, and bounded: every \(\ell\in X^*\) is bounded on \(W\), so the functionals \(\ell\mapsto\ell(w)\), \(w\in W\), on the Banach space \(X^*\) are pointwise bounded, and the uniform boundedness principle ([Theorem 4.2 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-04)) bounds their norms \(\|w\|\). Conversely, closed bounded convex sets are weakly compact by Lemma 1.1 of the first lesson. \(\square\)

## 5. Remarks

(1) Theorem 4.1 contains the theorems of Browder and Göhde (uniformly convex spaces) and of Kirk (sets with normal structure, Theorem 3.2 of the first lesson). It concerns the given norm: a nonexpansive map for one norm need not be nonexpansive for an equivalent one.

(2) Reflexivity of the space cannot be replaced by weak compactness of the domain: Alspach constructed a weakly compact convex subset of \(L^1[0,1]\) with a fixed-point-free nonexpansive self-map [Al]. In the proof, reflexivity enters through Lemma 1.1 of the first lesson, for the domain and for the unit ball of \(Y\).

(3) Bruck's theorem on commuting families [Bru, Theorem 1] then shows that, for a reflexive space, the common fixed points of any commuting family of nonexpansive self-maps of \(C\) form a nonempty nonexpansive retract of \(C\) [OpenAI-K, Corollary 1.2]. Bruck's theorem is not proved in this course.

## 6. Exercises

**Exercise 6.1** (easy). Show that the fixed point set of a nonexpansive map \(F:C\to C\) is closed, and convex when \(X\) is strictly convex (\(\|a+b\|<\|a\|+\|b\|\) unless \(a,b\) are nonnegative multiples of one vector).

**Exercise 6.2** (easy). Use Exercise 7.3 of the second lesson to show that in \((\mathbb R^2,\|\cdot\|_\infty)\) the fixed point set of a nonexpansive self-map of a square need not be convex.

**Exercise 6.3** (medium). In Proposition 3.1, show more precisely that the leaves \(s\) with \(f_v(d_s)\ge1-\eta\) for all \(v\) on their path have total weight at least \(1-\frac{5}{128\eta}\), for every \(\eta>0\).

**Exercise 6.4** (medium). Where would the proof fail for the space \(c_0\) of Exercise 5.3 of the first lesson? Point to the first lemma that uses reflexivity.

## 7. Solutions

**6.1.** \(\{a:\|F(a)-a\|=0\}\) is closed by continuity. If \(F(a)=a\), \(F(c)=c\) and \(z=(1-\lambda)a+\lambda c\), then \(\|F(z)-a\|\le\lambda\|c-a\|\) and \(\|F(z)-c\|\le(1-\lambda)\|c-a\|\), and the sum of the two is at least \(\|c-a\|\). So both are equalities, and in a strictly convex space \(F(z)-a\) and \(c-F(z)\) are nonnegative multiples of one vector, which forces \(F(z)=z\).

**6.2.** The map \(T(a,b)=(a,|a|)\) fixes \((-1,1)\) and \((1,1)\) but not their midpoint.

**6.3.** If some \(v\) on the path to \(s\) has \(f_v(d_s)<1-\eta\), the inner sum for \(s\) exceeds \(\eta\). So these leaves have total weight less than \(\frac5{128\eta}\).

**6.4.** Lemma 1.1 of the first lesson fails: in \(c_0\) closed bounded convex sets need not be weakly compact (the set \(C\) of Exercise 5.3 there is not), so the reduction to a minimal invariant set breaks down at the first step.

## References

- [Al] D. E. Alspach, *A fixed point free nonexpansive map*, Proc. Amer. Math. Soc. 82 (1981), 423–424.
- [Bru] R. E. Bruck, *A common fixed point theorem for a commuting family of nonexpansive mappings*, Pacific J. Math. 53 (1974), 59–71. https://doi.org/10.2140/pjm.1974.53.59
- [OpenAI-K] OpenAI, *Fixed points of nonexpansive maps in reflexive Banach spaces*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 5. https://github.com/openai/math/blob/main/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026
