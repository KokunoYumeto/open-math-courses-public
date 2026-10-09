# Contracting averages and sparse assignments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson extracts from the nonamenability of a countable group \(G\) a combinatorial structure on which the construction of the course rests [OpenAI-U, Section 3]. Fix a finite set \(S\subseteq G\) whose right translation average has norm \(\rho<1\) on \(\ell^2(G)\) (Lemma 1.2), list the \(n=d^\ell\) products of \(\ell\) elements of \(S\), \(d=|S|\), and draw an edge from each \(x\in G\) to each \(xs_i\). Every vertex is then the start of \(n\) edges and the end of \(n\) edges. Proposition 3.2 assigns each edge to one of its two endpoints so that every vertex receives at most \(r=\lceil n\rho^\ell\rceil\) edges, a vanishing fraction of the \(n\) edges at it. The proof checks Hall's condition through the operator norm of the average and passes from finite to countable families by a compactness argument.

We use Theorem 5.1 of [Means, Følner sets, and regular representations](course:OA-ERGODIC/reader/means-folner-sets-and-regular-representations#5-almost-invariant-vectors): a countable group is amenable exactly when \(\ell^2\) of the group has unit vectors \(\xi_n\) with \(\|\lambda_s\xi_n-\xi_n\|\to0\) for every \(s\), where \((\lambda_s\xi)(x)=\xi(s^{-1}x)\). Notation and the overall plan are those of [Uniformly bounded representations](uniformly-bounded-representations.md).

## 1. A contracting average

Let \(G\) be a countable group. Right translation \((R_tf)(x)=f(xt)\) is a unitary operator on \(\ell^2(G)\), and \(R_sR_t=R_{st}\), because \((R_sR_tf)(x)=(R_tf)(xs)=f(xst)\). For a finite nonempty \(S\subseteq G\) with \(d=|S|\) put
\[
A_S=\frac1d\sum_{t\in S}R_t,\qquad\|A_S\|\le1.
\]

**Lemma 1.1.** For a unit vector \(f\in\ell^2(G)\),
\[
\|A_Sf\|^2=1-\frac1{2d^2}\sum_{t,t'\in S}\|R_tf-R_{t'}f\|^2.
\]

**Proof.** \(\|R_tf-R_{t'}f\|^2=2-2\operatorname{Re}\langle R_tf,R_{t'}f\rangle\), and \(d^2\|A_Sf\|^2=\sum_{t,t'}\langle R_tf,R_{t'}f\rangle\) is real, so it equals \(\sum_{t,t'}\bigl(1-\frac12\|R_tf-R_{t'}f\|^2\bigr)\). \(\square\)

**Lemma 1.2** (contracting average). If \(G\) is countable and not amenable, there are a finite set \(S\subseteq G\) with \(e\in S\) and \(d=|S|\ge2\), and a number \(0<\rho<1\), such that \(\|A_S\|\le\rho\).

**Proof.** Suppose that \(\|A_S\|=1\) for every finite \(S\) containing \(e\). Let \(K\subseteq G\) be finite and \(\varepsilon>0\); put \(S=K\cup\{e\}\) and \(d=|S|\). Choose a unit vector \(f\) with \(\|A_Sf\|^2>1-\varepsilon^2/(2d^2)\). By Lemma 1.1, with \(t'=e\), every \(t\in K\) satisfies \(\|R_tf-f\|^2\le2d^2(1-\|A_Sf\|^2)<\varepsilon^2\).

Let \((Jf)(x)=f(x^{-1})\). Then \(J\) is unitary, \(J^2=1\), and \(JR_tJ=\lambda_t\), since \((JR_tJf)(x)=(Jf)(x^{-1}t)=f(t^{-1}x)\). So \(\xi=Jf\) is a unit vector with \(\|\lambda_t\xi-\xi\|=\|R_tf-f\|<\varepsilon\) for \(t\in K\). Enumerate \(G=\{g_1,g_2,\dots\}\) and apply this to \(K=\{g_1,\dots,g_m\}\) and \(\varepsilon=1/m\): the resulting unit vectors \(\xi_m\) satisfy \(\|\lambda_s\xi_m-\xi_m\|\to0\) for every \(s\in G\). By Theorem 5.1 of the lesson on means and Følner sets, \(G\) is amenable, a contradiction. So some \(A_S\) with \(e\in S\) has norm less than \(1\); choose \(\rho\) between that norm and \(1\). Since \(A_{\{e\}}=1\), the set has at least two elements. \(\square\)

The converse also holds (Exercise 6.1). The lemma is a form of Kesten's criterion: the random walk that multiplies by a uniformly chosen element of \(S\) returns with exponentially small probability.

## 2. Hall's theorem and its countable form

Let \(X\) and \(Y\) be sets and let \(N(x)\subseteq Y\) be given for each \(x\in X\). For \(F\subseteq X\) write \(N(F)=\bigcup_{x\in F}N(x)\). A *matching* is an injective map \(\varphi\) from a subset of \(X\) to \(Y\) with \(\varphi(x)\in N(x)\).

**Lemma 2.1** (Hall). Let \(X\) be finite and suppose \(|N(F)|\ge|F|\) for every \(F\subseteq X\). Then there is a matching defined on all of \(X\).

**Proof.** Let \(\varphi\), defined on \(X'\subseteq X\), be a matching with \(|X'|\) as large as possible, and suppose some \(x_0\in X\setminus X'\) exists. An *alternating path* is a sequence \(x_0,y_1,x_1,y_2,\dots,x_{m-1},y_m\), \(m\ge1\), with distinct \(x_i\in X\) and distinct \(y_i\in Y\), such that \(y_i\in N(x_{i-1})\) for \(1\le i\le m\) and \(\varphi(x_i)=y_i\) for \(1\le i<m\). If the last point \(y_m\) of some alternating path is not a value of \(\varphi\), redefine \(\varphi(x_{i-1})=y_i\) for \(1\le i\le m\) and keep the other values. The result is injective, because \(y_1,\dots,y_{m-1}\) were values only at \(x_1,\dots,x_{m-1}\) and \(y_m\) was not a value, and it is defined on \(X'\cup\{x_0\}\), contradicting maximality. Hence the set \(R_Y\) of last points of alternating paths lies in \(\varphi(X')\).

Put \(R_X=\{x_0\}\cup\varphi^{-1}(R_Y)\). We claim \(N(R_X)\subseteq R_Y\). Let \(x\in R_X\) and \(y\in N(x)\). If \(x=x_0\), the sequence \(x_0,y\) is an alternating path. Otherwise \(x=\varphi^{-1}(y_m)\) for the last point \(y_m\) of an alternating path \(P\). If \(y=y_j\) for some \(j\), the part of \(P\) ending at \(y_j\) is an alternating path. If not, \(x\) differs from \(x_0\notin X'\) and from \(x_1,\dots,x_{m-1}\), whose values \(y_1,\dots,y_{m-1}\) differ from \(y_m\); so \(P\) followed by \(x,y\) is an alternating path. In both cases \(y\in R_Y\). Finally \(\varphi^{-1}\) maps \(R_Y\) injectively into \(R_X\setminus\{x_0\}\). So \(|N(R_X)|\le|R_Y|\le|R_X|-1\), contradicting the hypothesis. \(\square\)

**Lemma 2.2** (countable form). Let \(X\) be countable, let every \(N(x)\) be finite, and suppose \(|N(F)|\ge|F|\) for every finite \(F\subseteq X\). Then there is a matching defined on all of \(X\).

**Proof.** If \(X\) is finite this is Lemma 2.1. Otherwise enumerate \(X=\{x_1,x_2,\dots\}\) and let \(\mathcal A_m\) be the set of matchings defined on \(\{x_1,\dots,x_m\}\), with \(\mathcal A_0=\{\varnothing\}\). Each \(\mathcal A_m\) is finite, because the \(N(x_i)\) are finite, and nonempty by Lemma 2.1. Restriction maps \(\mathcal A_{m+1}\) to \(\mathcal A_m\). Call \(\alpha\in\mathcal A_m\) *extendable* if for every \(m'\ge m\) some element of \(\mathcal A_{m'}\) restricts to \(\alpha\). The empty matching is extendable. If \(\alpha\in\mathcal A_m\) is extendable, so is one of its finitely many extensions \(\beta\in\mathcal A_{m+1}\): otherwise each \(\beta\) fails at some level \(m_\beta\), and an element of \(\mathcal A_{m'}\), \(m'=\max_\beta m_\beta\), restricting to \(\alpha\) would restrict at level \(m+1\) to some \(\beta\) and show that \(\beta\) extends to level \(m_\beta\). Choosing extendable extensions step by step gives matchings \(\alpha_m\in\mathcal A_m\), each extending the previous one. Their union is defined on \(X\), and it is injective because any two points lie in the domain of one \(\alpha_m\). \(\square\)

Finiteness of the sets \(N(x)\) cannot be dropped (Exercise 6.3).

## 3. Sparse assignments

Fix a countable nonamenable group \(G\) and \(S,d,\rho\) as in Lemma 1.2. For \(\ell\ge1\) enumerate the words \((t_1,\dots,t_\ell)\in S^\ell\) as \(w_1,\dots,w_n\), \(n=d^\ell\), and let \(s_i=t_1t_2\cdots t_\ell\) be the product of the word \(w_i\). Different indices may give the same element of \(G\); we keep the indices apart. Put \([n]=\{1,\dots,n\}\) and
\[
r=\lceil n\rho^\ell\rceil.
\]
We think of \((x,i)\in G\times[n]\) as an edge from the *row* \(x\) to the *column* \(xs_i\).

**Lemma 3.1** (edge count). For finite \(U,V\subseteq G\),
\[
\#\{(x,i)\in U\times[n]:xs_i\in V\}\le n\rho^\ell\sqrt{|U|\,|V|}.
\]

**Proof.** Since \(R_{s_i}=R_{t_1}\cdots R_{t_\ell}\) for \(w_i=(t_1,\dots,t_\ell)\), expanding the product gives \(\sum_{i=1}^nR_{s_i}=\bigl(\sum_{t\in S}R_t\bigr)^\ell=(dA_S)^\ell\), of norm at most \(n\rho^\ell\). The left side of the claim is
\[
\sum_{i=1}^n\sum_{x\in U}\mathbf1_V(xs_i)=\Bigl\langle\sum_{i=1}^nR_{s_i}\mathbf1_V,\ \mathbf1_U\Bigr\rangle\le n\rho^\ell\,\|\mathbf1_V\|\,\|\mathbf1_U\|.\qquad\square
\]

**Proposition 3.2** (sparse assignment). There is a function \(a:G\times[n]\to\{0,1\}\) with
\[
\#\{i:a(x,i)=1\}\le r\quad(x\in G),\qquad\#\{i:a(ys_i^{-1},i)=0\}\le r\quad(y\in G).\tag{3.1}
\]

**Proof.** Give every row and every column \(r\) *slots*: let \(Y=\{\mathrm{row},\mathrm{col}\}\times G\times[r]\), and for an edge \((x,i)\) let \(N(x,i)\) consist of the \(r\) slots \((\mathrm{row},x,q)\) of its row and the \(r\) slots \((\mathrm{col},xs_i,q)\) of its column. Let \(F\subseteq G\times[n]\) be finite, with set of rows \(U\) and set of columns \(V\). Then \(|N(F)|=r(|U|+|V|)\), while Lemma 3.1 gives
\[
|F|\le n\rho^\ell\sqrt{|U|\,|V|}\le r\cdot\tfrac12(|U|+|V|)\le|N(F)|.
\]
The set \(G\times[n]\) is countable, so Lemma 2.2 gives an injective \(\varphi\) on \(G\times[n]\) with \(\varphi(x,i)\in N(x,i)\). Put \(a(x,i)=1\) if \(\varphi(x,i)\) is a row slot and \(a(x,i)=0\) if it is a column slot. The edges \((x,i)\) with \(a(x,i)=1\) are sent injectively into the \(r\) slots of the row \(x\). The edges ending at a column \(y\) are the pairs \((ys_i^{-1},i)\), one for each \(i\in[n]\), and those with \(a(ys_i^{-1},i)=0\) are sent injectively into the \(r\) slots of the column \(y\). This proves (3.1). \(\square\)

The two bounds in (3.1) concern indexed edges: when \(s_i=s_j\) for \(i\neq j\), the edges \((x,i)\) and \((x,j)\) join the same row and column and count separately. When \(s_i=e\), the edge \((x,i)\) joins the row \(x\) to the column \(x\), which are different vertices of the bipartite structure.

**Corollary 3.3.** \(r/n\le\rho^\ell+1/n\), and \(\frac rn\log(2n)\to0\) as \(\ell\to\infty\).

**Proof.** \(r\le n\rho^\ell+1\), and \(\log(2n)=\log2+\ell\log d\). Both \(\rho^\ell\ell\) and \(\ell/d^\ell\) tend to \(0\). \(\square\)

## 4. What the assignment gives

Every row \(x\) is the start of the \(n\) edges \((x,i)\), and every column \(y\) is the end of the \(n\) edges \((ys_i^{-1},i)\). Proposition 3.2 says that each vertex keeps at most \(r\) of its edges, and the other endpoint keeps the rest: a row keeps few of the edges starting at it, and a column keeps few of the edges ending at it. Compare the assignment \(a\) with its left translate \(a(g^{-1}\cdot,\cdot)\). At a row \(x\), the edges whose assignment differs are among those kept by the row \(x\) under one of the two assignments, at most \(2r\) of them; at a column \(y\), they are among those kept by the column \(y\) under one of the two assignments, again at most \(2r\). The lesson [Random sign frames and masked operators](random-sign-frames-and-masked-operators.md) converts these counts into operator norm bounds.

## 5. Remarks

The construction uses only Lemma 3.1, an estimate of edge numbers between finite sets of rows and columns, and the counting in Hall's theorem. The assignment plays the role of the splitting of a Littlewood-type kernel into a part with summable rows and a part with summable columns, which Epstein and Monod, following Bożejko and Fendler, use to build bounded commutators [EM, Propositions 2.3–2.4]; see [OpenAI-U, Introduction].

## 6. Exercises

**Exercise 6.1** (easy). Prove the converse of Lemma 1.2: if some \(A_S\), with \(S\) finite and \(e\in S\), has norm less than \(1\), then \(G\) is not amenable.

**Exercise 6.2** (easy). Show that the hypothesis of Lemma 2.1 cannot be weakened to \(|N(x)|\ge1\) for every \(x\): give \(X\), \(Y\) and \(N\) with nonempty \(N(x)\) and no matching on all of \(X\).

**Exercise 6.3** (medium). Let \(X=\{x_0,x_1,x_2,\dots\}\), \(Y=\{1,2,3,\dots\}\), \(N(x_0)=Y\) and \(N(x_j)=\{j\}\) for \(j\ge1\). Show that \(|N(F)|\ge|F|\) for every finite \(F\subseteq X\) but that no matching is defined on all of \(X\).

**Exercise 6.4** (easy). In the group \(\mathbb Z\), written additively, with \(S=\{0,1\}\) and \(\ell=2\), list \(s_1,\dots,s_4\), and check \(\sum_iR_{s_i}=(R_0+R_1)^2\). Why does Lemma 1.2 not apply to \(\mathbb Z\)?

## 7. Solutions

**6.1.** Suppose \(G\) is amenable. By Theorem 5.1 of the lesson on means and Følner sets there are unit vectors \(\xi_m\) with \(\|\lambda_t\xi_m-\xi_m\|\to0\) for every \(t\). Then \(f_m=J\xi_m\) satisfies \(\|R_tf_m-f_m\|\to0\) for \(t\in S\), and by Lemma 1.1, \(\|A_Sf_m\|\to1\). So \(\|A_S\|=1\).

**6.2.** \(X=\{x_1,x_2\}\), \(Y=\{y\}\), \(N(x_1)=N(x_2)=\{y\}\): here \(|N(X)|=1<2\).

**6.3.** If \(F\) contains \(x_0\), then \(N(F)=Y\) is infinite. Otherwise \(N(F)=\{j:x_j\in F\}\) has \(|F|\) elements. A matching on \(X\) would map each \(x_j\), \(j\ge1\), to \(j\), leaving no value for \(x_0\).

**6.4.** The words \((0,0),(0,1),(1,0),(1,1)\) give \(s_1=0\), \(s_2=1\), \(s_3=1\), \(s_4=2\), and \((R_0+R_1)^2=R_0+2R_1+R_2=\sum_iR_{s_i}\); the element \(1\) occurs with multiplicity two. The group \(\mathbb Z\) is amenable, so by Exercise 6.1 every \(A_S\) has norm \(1\).

## References

- [EM] I. Epstein and N. Monod, *Nonunitarizable representations and random forests*, Int. Math. Res. Not. IMRN 2009; arXiv:0811.3422. https://arxiv.org/abs/0811.3422
- [OpenAI-U] OpenAI, *Unitarizability implies amenability for discrete groups*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
