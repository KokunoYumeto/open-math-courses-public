# A spreading norm with contractive merging

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the first of the two main statements: a real Banach space \(X\) that is not superreflexive carries a norm \(N\) on finite sequences that does not change when zeros are inserted, does not increase when neighbouring entries are added up, and whose finite pieces embed in \(X\) almost isometrically. The starting point is a space \(Y\) that is finitely representable in \(X\) and not reflexive. A vector of the bidual that is far from \(Y\) gives a triangular array of vectors and functionals; Ramsey's theorem makes the norms of their combinations independent of the positions; an average over finer and finer subdivisions gives the behaviour under merging.

- A vector of the bidual far from \(Y\), and two consequences of the Hahn–Banach theorem (Lemmas 1.1 and 1.2).
- Triangular arrays and the estimate by partial sums (Lemma 2.1).
- The spreading limit \(N_0\) (Proposition 3.1).
- Subdivisions and the norm \(N\) (Lemmas 4.1 and 4.2).
- Merging (Lemmas 5.1 and 5.2), and the ordered norm (Theorem 5.3).

The lesson follows [OpenAI-M, Appendix A], which adapts a construction of Brunel and Sucheston. It uses the definitions of [Markov type and the reduction to a finite walk](markov-type-and-the-reduction-to-a-finite-walk.md), the Hahn–Banach theorem and the bidual ([Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20), core course), and two results of [Alignment of lists: patterns, minimax and Ramsey's theorem](course:large-independent-sets-in-three-colorable-graphs/alignment-of-lists-patterns-minimax-and-ramseys-theorem) (course *Large independent sets in three-colorable graphs*): Lemma 3.1 there on a closed convex set that does not contain \(0\), and Ramsey's theorem (Theorem 4.1 there).

## 1. A vector far from \(Y\)

Let \(Y\) be a real Banach space, \(Y^*\) its dual and \(Y^{**}\) its bidual. An element \(y\in Y\) is also an element of \(Y^{**}\), by \(y(f)=f(y)\); this embedding preserves the norm. Let \(Y\) be not reflexive: \(Y\) is a closed subspace of \(Y^{**}\) and not all of it. Fix a number \(d\) with \(0<d<1\). There is \(v\in Y^{**}\) with
\[
\|v\|\le1,\qquad\operatorname{dist}(v,Y)>d .
\]
Indeed, take \(w\in Y^{**}\) outside \(Y\); its distance \(\delta\) to \(Y\) is positive. Choose \(y\in Y\) with \(\|w-y\|<\delta/d\) and put \(v=(w-y)/\|w-y\|\).

For a subspace \(E\subseteq Y\) let \(E^\perp\) be the set of the \(f\in Y^*\) that vanish on \(E\).

**Lemma 1.1.** Let \(E\subseteq Y\) be a subspace of finite dimension and \(w\in Y^{**}\). Then
\[
\begin{aligned}
&\sup\{\,|w(f)|:\ f\in E^\perp,\ \|f\|\le1\,\}\\
&\qquad=\operatorname{dist}(w,E).
\end{aligned}
\]

**Proof.** Let \(\sigma\) be the supremum. For \(e\in E\) and \(f\in E^\perp\) we have \(w(f)=(w-e)(f)\), so \(|w(f)|\le\|w-e\|\,\|f\|\); hence \(\sigma\le\operatorname{dist}(w,E)\).

For the other inequality, the restriction of \(w\) to the subspace \(E^\perp\) of \(Y^*\) is a functional of norm \(\sigma\). By the Hahn–Banach theorem it extends to \(\tilde w\in Y^{**}\) with \(\|\tilde w\|=\sigma\). The element \(w-\tilde w\) vanishes on \(E^\perp\). We show that it lies in \(E\); then \(\operatorname{dist}(w,E)\le\|\tilde w\|=\sigma\). Let \(e_1,\dots,e_k\) be a basis of \(E\), and \(f_1,\dots,f_k\in Y^*\) with \(f_i(e_j)=1\) for \(i=j\) and \(0\) otherwise (they exist by the Hahn–Banach theorem). For \(f\in Y^*\) the functional \(f-\sum_jf(e_j)f_j\) lies in \(E^\perp\). So for \(u=w-\tilde w\),
\[
\begin{aligned}
u(f)&=\sum_jf(e_j)\,u(f_j)\\
&=f\Bigl(\sum_ju(f_j)\,e_j\Bigr),
\end{aligned}
\]
that is, \(u=\sum_ju(f_j)e_j\in E\). \(\blacksquare\)

**Lemma 1.2** (a finite form of Goldstine's theorem). Let \(w\in Y^{**}\) with \(\|w\|\le1\), let \(f_1,\dots,f_i\in Y^*\) and \(\varepsilon>0\). There is \(y\in Y\) with \(\|y\|\le1\) and \(|f_h(y)-w(f_h)|\le\varepsilon\) for \(h=1,\dots,i\).

**Proof.** Let \(C\subseteq\mathbb R^i\) be the set of the points \((f_1(y),\dots,f_i(y))\) with \(\|y\|\le1\); it is convex. Let \(\pi_0=(w(f_1),\dots,w(f_i))\). If \(\pi_0\) is not in the closure \(\overline C\), the set \(\overline C-\pi_0\) is closed, convex and does not contain \(0\). By the lemma on such sets there is \(c\in\mathbb R^i\) with \(\langle c,x-\pi_0\rangle\ge|c|^2>0\) for all \(x\in C\). With \(f=\sum_hc_hf_h\) this says \(f(y)\ge w(f)+|c|^2\) for all \(\|y\|\le1\). The infimum of \(f(y)\) over these \(y\) is \(-\|f\|\), and \(w(f)\ge-\|f\|\). This is a contradiction. So \(\pi_0\in\overline C\). \(\blacksquare\)

## 2. Triangular arrays

**Lemma 2.1.** Let \(Y\), \(d\) and \(v\) be as in Section 1. For every integer \(M\ge1\) there are \(z_1,\dots,z_M\in Y\) with \(\|z_i\|\le1\) such that for all \(m\), all indices \(i_1<\dots<i_m\) and all real \(a_1,\dots,a_m\)
\[
\begin{aligned}
&d\max_{1\le j\le m}\Bigl|\sum_{h=1}^ja_h\Bigr|-\frac1M\sum_{h=1}^m|a_h|\\
&\qquad\le\Bigl\|\sum_{h=1}^ma_hz_{i_h}\Bigr\|\ \le\ \sum_{h=1}^m|a_h| .
\end{aligned}
\]

**Proof.** *The array.* We construct \(y_1,\dots,y_M\in Y\) and \(f_1,\dots,f_M\in Y^*\), all of norm at most \(1\), with
\[
\begin{gathered}
f_i(y_j)=0\quad\text{for }j<i,\\
|f_i(y_j)-d|\le\frac1M\quad\text{for }j\ge i.
\end{gathered}
\]
Let \(y_1,\dots,y_{i-1}\) and \(f_1,\dots,f_{i-1}\) be constructed, and \(E\) the span of \(y_1,\dots,y_{i-1}\). By Lemma 1.1,
\[
\begin{aligned}
&\sup\{|v(f)|:f\in E^\perp,\|f\|\le1\}\\
&\qquad=\operatorname{dist}(v,E)\ge\operatorname{dist}(v,Y)>d .
\end{aligned}
\]
So there is \(f\in E^\perp\) with \(\|f\|\le1\) and \(|v(f)|>d\); a multiple \(f_i\) of \(f\) with a factor of absolute value less than \(1\) has \(v(f_i)=d\). By Lemma 1.2 there is \(y_i\) with \(\|y_i\|\le1\) and \(|f_h(y_i)-v(f_h)|\le\tfrac1M\) for \(h\le i\); here \(v(f_h)=d\). Since \(f_i\in E^\perp\), \(f_i(y_j)=0\) for \(j<i\).

*The estimate.* Put \(z_i=y_{M+1-i}\) and \(g_i=f_{M+1-i}\). Then \(g_i(z_j)=0\) for \(j>i\) and \(|g_i(z_j)-d|\le\tfrac1M\) for \(j\le i\). For indices \(i_1<\dots<i_m\) and \(1\le j\le m\), the functional \(g_{i_j}\) vanishes on \(z_{i_h}\) for \(h>j\) and is \(d\) up to \(\tfrac1M\) on \(z_{i_h}\) for \(h\le j\). So
\[
\begin{aligned}
\Bigl\|\sum_ha_hz_{i_h}\Bigr\|&\ge\Bigl|g_{i_j}\Bigl(\sum_ha_hz_{i_h}\Bigr)\Bigr|\\
&\ge d\,\Bigl|\sum_{h\le j}a_h\Bigr|-\frac1M\sum_h|a_h| .
\end{aligned}
\]
The upper bound holds because \(\|z_i\|\le1\). \(\blacksquare\)

So in a space that is not reflexive there are, for every length, sequences of vectors of norm at most \(1\) for which the norm of a combination controls all partial sums of the coefficients, taken in the order of the sequence.

## 3. The spreading limit

**Proposition 3.1.** Let \(Y\) be a real Banach space that is not reflexive, and \(0<d<1\). There is a norm \(N_0\) on \(c_{00}\) with the following properties.

1. \(N_0\) is spreading invariant.
2. \(d\max_j\bigl|\sum_{i\le j}a_i\bigr|\le N_0(a)\le\sum_i|a_i|\) for all \(a\); in particular \(N_0(a)\ge\tfrac d2\max_i|a_i|\).
3. For every \(m\) and every \(\eta>0\) there is an injective linear map from \(\mathbb R^m\) with the norm \(N_0\) into \(Y\) of distortion less than \(1+\eta\).

**Proof.** *Homogeneous tuples.* Fix \(k\ge1\). Let \(\mathcal A_k\) be the finite set of the arrays \((a_1,\dots,a_m)\) with \(m\le k\) whose entries are multiples of \(\tfrac1k\) of absolute value at most \(k\). Let \(M\ge k^3\), and \(z_1,\dots,z_M\) as in Lemma 2.1. Give every set of \(k\) indices \(i_1<\dots<i_k\) in \(\{1,\dots,M\}\) as its color the list of the integers
\[
\Bigl\lfloor k\,\Bigl\|\sum_{h=1}^ma_hz_{i_h}\Bigr\|\Bigr\rfloor,\qquad(a_1,\dots,a_m)\in\mathcal A_k .
\]
These integers lie between \(0\) and \(k^3\), so the number of the colors is bounded independently of \(M\). By Ramsey's theorem, for \(M\) large enough there is a set \(H\) of \(2k\) indices all of whose subsets with \(k\) elements have the same color. Let \(x^{(k)}_1,\dots,x^{(k)}_k\) be the vectors \(z_i\) for the first \(k\) elements of \(H\), in increasing order. Every \(m\) of these first \(k\) elements, with \(m\le k\), are the first \(m\) elements of a subset of \(H\) with \(k\) elements: add the last \(k-m\) elements of \(H\). So for \(a\in\mathcal A_k\) of the length \(m\) and any two increasing choices \(j_1<\dots<j_m\) and \(j'_1<\dots<j'_m\) in \(\{1,\dots,k\}\),
the two norms
\[
\Bigl\|\sum_ha_hx^{(k)}_{j_h}\Bigr\|\qquad\text{and}\qquad\Bigl\|\sum_ha_hx^{(k)}_{j'_h}\Bigr\|
\]
differ by at most \(\tfrac1k\). We refer to this statement as (3.1).

*The limit.* For an array \(a\) of the length \(m\le k\) put \(\nu_k(a)=\|\sum_{i\le m}a_ix^{(k)}_i\|\). By Lemma 2.1, with \(M\ge k^3\),
\[
\begin{aligned}
d\max_j\Bigl|\sum_{i\le j}a_i\Bigr|-\frac1{k^3}\sum_i|a_i|&\le\nu_k(a)\\
&\le\sum_i|a_i| ,
\end{aligned}
\]
and \(|\nu_k(a)-\nu_k(a')|\le\sum_i|a_i-a'_i|\). We refer to the two bounds for \(\nu_k(a)\) as (3.2). Consider the numbers \(k=l!\). Every array with rational entries lies in \(\mathcal A_{l!}\) for all large \(l\). There are countably many such arrays, and the sequences \(\nu_{l!}(a)\) are bounded. By the diagonal argument there are \(l_1<l_2<\dots\) such that \(\nu_{l_r!}(a)\) converges for every array \(a\) with rational entries. Since all \(\nu_k\) satisfy the same estimate \(|\nu_k(a)-\nu_k(a')|\le\sum|a_i-a'_i|\), the sequence converges for every real array, and uniformly on bounded sets of arrays of a fixed length. Let \(N_0(a)\) be the limit.

*Properties.* \(N_0\) is a seminorm, as a limit of seminorms on each \(\mathbb R^m\); appending zeros to an array does not change \(\nu_k\), so \(N_0\) is defined on \(c_{00}\). Property 2 follows from (3.2); the last part holds because every \(a_i\) is the difference of two partial sums. So \(N_0\) is a norm. For a rational array \(a\) and indices \(k_1<\dots<k_m\), (3.1) says that \(\nu_k\) of \(a\) and of the array with the entries \(a_i\) at the places \(k_i\) differ by at most \(\tfrac1k\), for the large \(k\) of the sequence. So \(N_0\) is spreading invariant on rational arrays, and by continuity on all.

*Embeddings.* Fix \(m\). The maps \(T_r:a\mapsto\sum_{i\le m}a_ix^{(l_r!)}_i\) from \(\mathbb R^m\) to \(Y\) satisfy \(\|T_ra\|\to N_0(a)\) uniformly on the set \(\{N_0(a)=1\}\), which is bounded by property 2. So \(1-\eta'\le\|T_ra\|\le1+\eta'\) on this set for large \(r\), and the distortion of \(T_r\) tends to \(1\). \(\blacksquare\)

## 4. Subdivisions

For an array \(a=(a_1,\dots,a_m)\) and positive integers \(\mathbf J=(J_1,\dots,J_m)\) let \(F_{\mathbf J}a\) be the array in which every \(a_i\) is replaced by \(J_i\) entries \(a_i/J_i\). Write \(F_J\) if all \(J_i\) are equal to \(J\). The sums of the blocks of \(F_{\mathbf J}a\) are the entries of \(a\).

**Lemma 4.1.** Let \(N_0\) be a spreading invariant norm on \(c_{00}\). If \(J_i\le M_i\) for all \(i\), then \(N_0(F_{\mathbf M}a)\le N_0(F_{\mathbf J}a)\).

**Proof.** In the block \(i\), of the length \(M_i\), choose a set of \(J_i\) places uniformly at random, put \(a_i/J_i\) at these places and \(0\) at the others. Every array that arises is \(F_{\mathbf J}a\) with zeros inserted, so its norm is \(N_0(F_{\mathbf J}a)\). The mean of these arrays has the entry \(\tfrac{J_i}{M_i}\cdot\tfrac{a_i}{J_i}=\tfrac{a_i}{M_i}\) at every place of the block \(i\): it is \(F_{\mathbf M}a\). A norm of a mean is at most the mean of the norms. \(\blacksquare\)

So \(J\mapsto N_0(F_Ja)\) does not increase, and we may define
\[
N(a)=\lim_{J\to\infty}N_0(F_Ja).
\]

**Lemma 4.2.** Let \(N_0\) be as in Proposition 3.1. Then \(N\) is a spreading invariant norm on \(c_{00}\) with
\[
d\max_j\Bigl|\sum_{i\le j}a_i\Bigr|\le N(a)\le\sum_i|a_i| ,
\]
and for every \(m\) and \(\eta>0\) there is \(J\) such that \(F_J\) is a linear map from \(\mathbb R^m\) with the norm \(N\) into \(\mathbb R^{mJ}\) with the norm \(N_0\) of distortion less than \(1+\eta\).

**Proof.** \(F_J\) is linear, so \(a\mapsto N_0(F_Ja)\) is a seminorm, and so is the limit. The partial sums of \(a\) occur among the partial sums of \(F_Ja\), at the ends of the blocks, and \(\sum|a_i|\) does not change under \(F_J\); so the bounds of Proposition 3.1 hold for \(N_0(F_Ja)\) and for \(N\). In particular \(N\) is a norm. If zeros are inserted into \(a\), then \(F_J\) of the new array is \(F_Ja\) with zeros inserted; so \(N\) is spreading invariant.

The functions \(a\mapsto N_0(F_Ja)\) on \(\mathbb R^m\) satisfy the same estimate \(|N_0(F_Ja)-N_0(F_Ja')|\le\sum|a_i-a'_i|\) and converge at every point; so they converge uniformly on the bounded set \(\{N(a)=1\}\). Hence \(1\le N_0(F_Ja)\le1+\eta\) on this set for large \(J\). \(\blacksquare\)

## 5. Merging

In this section \(N_0\) and \(N\) are as in Lemma 4.2.

**Lemma 5.1.** \(N(F_{\mathbf J}a)=N(a)\) for all arrays \(a\) and all \(\mathbf J\).

**Proof.** Let \(J_-\) and \(J_+\) be the smallest and the largest of the \(J_i\). The array \(F_rF_{\mathbf J}a\) is \(F_{r\mathbf J}a\), with the multiplicities \(rJ_i\). By Lemma 4.1,
\[
N_0(F_{rJ_+}a)\le N_0(F_rF_{\mathbf J}a)\le N_0(F_{rJ_-}a).
\]
For \(r\to\infty\) the outer terms tend to \(N(a)\) and the middle term to \(N(F_{\mathbf J}a)\). \(\blacksquare\)

**Lemma 5.2.** If two adjacent entries of an array are both \(\ge0\) or both \(\le0\), replacing them by their sum does not change \(N\).

**Proof.** If one of the two is \(0\), this is spreading invariance. Let \(a_i,a_{i+1}\) be both positive (the negative case is the same), and first let \(a_i/a_{i+1}=P/Q\) with positive integers \(P,Q\). Then \(a_i/P=a_{i+1}/Q=(a_i+a_{i+1})/(P+Q)\). So subdividing \(a_i\) into \(P\) and \(a_{i+1}\) into \(Q\) equal parts gives the same array as subdividing the merged entry into \(P+Q\) equal parts, and Lemma 5.1 gives the claim. For a general ratio, approximate \(a_{i+1}\) by numbers with a rational ratio to \(a_i\), and use \(|N(a)-N(a')|\le\sum|a_i-a'_i|\). \(\blacksquare\)

**Theorem 5.3** (the ordered norm; [OpenAI-M], after Brunel and Sucheston). Assume (JE). Let \(X\) be a real Banach space that is not superreflexive. Then there is a norm \(N\) on \(c_{00}\) such that:

1. \(N\) is spreading invariant;
2. \(N\) has contractive merging;
3. for every \(m\) and every \(\eta>0\) there is an injective linear map from \(\mathbb R^m\) with the norm \(N\) into \(X\) of distortion less than \(1+\eta\).

This is Proposition 4.1 of the first lesson.

**Proof.** By (JE) there is a Banach space \(Y\) that is finitely representable in \(X\) and not reflexive. Let \(N_0\) be the norm of Proposition 3.1 for \(Y\) and \(d=\tfrac12\), and \(N\) the norm of Lemma 4.2. Property 1 is in Lemma 4.2.

*Property 3.* Let \(\eta>0\). By Lemma 4.2, \(\mathbb R^m\) with \(N\) maps into \(\mathbb R^{mJ}\) with \(N_0\) with distortion less than \(1+\eta\). By Proposition 3.1 this space maps into \(Y\) with distortion less than \(1+\eta\). The image is a subspace of finite dimension of \(Y\), and it maps into \(X\) with distortion less than \(1+\eta\). The composition has a distortion less than \((1+\eta)^3\).

*Property 2.* Fix an array, a place \(i\), and all entries except \(a_i,a_{i+1}\). For a real number \(s\ne0\) consider the function
\[
\varphi(t)=N(\dots,\,t,\,s-t,\,\dots)
\]
of the real variable \(t\). It is convex, as a norm of an expression that is affine in \(t\). For \(t\) between \(0\) and \(s\) the entries \(t\) and \(s-t\) have the same sign, and by Lemma 5.2, \(\varphi(t)=N(\dots,s,\dots)=:c_0\). A convex function that has the value \(c_0\) on an interval \([t_1,t_2]\) with \(t_1<t_2\) is \(\ge c_0\) everywhere: for \(t>t_2\), the point \(t_2\) is \(\lambda t_1+(1-\lambda)t\) with \(0<\lambda<1\), so \(c_0\le\lambda c_0+(1-\lambda)\varphi(t)\), that is \(\varphi(t)\ge c_0\); the same for \(t<t_1\). With \(t=a_i\) and \(s=a_i+a_{i+1}\) this is
\[
\begin{aligned}
&N(\dots,a_i,a_{i+1},\dots)\\
&\qquad\ge N(\dots,a_i+a_{i+1},\dots).
\end{aligned}
\]
For \(a_i+a_{i+1}=0\) apply this to \(a_{i+1}+\epsilon\) and let \(\epsilon\to0\). \(\blacksquare\)

**What the norm remembers.** By Lemma 4.2, \(N(a)\ge\tfrac12\max_j|a_1+\dots+a_j|\). So the array \((1,1,\dots,1)\) with \(m\) entries has a norm of at least \(m/2\), while by contractive merging the array \((1,-1,1,-1,\dots)\) has a norm of at least \(N(1,-1)\) and at most \(m\). The order of the entries matters. This is the trace that the missing reflexivity leaves: in the proof, the positions of an array were places in a sequence of vectors that converges, in a weak sense, to a point outside the space.

## 6. Exercises

**6.1.** Let \(Y=c_0\), the space of the real sequences that tend to \(0\), with the maximum norm. Its bidual is the space of all bounded sequences. Let \(v=(1,1,1,\dots)\). Show \(\operatorname{dist}(v,Y)=1\), and give vectors \(y_j\) and functionals \(f_i\) of norm \(1\) with \(f_i(y_j)=1\) for \(j\ge i\) and \(0\) for \(j<i\).

**6.2.** For the vectors of Exercise 6.1 and \(z_i=y_{M+1-i}\), compute \(\|\sum_ha_hz_{i_h}\|\) for \(i_1<\dots<i_m\).

**6.3.** Show that the norm \(\sum_i|a_i|\) on \(c_{00}\) is spreading invariant and has contractive merging, and that the norm \((\sum_ia_i^2)^{1/2}\) is spreading invariant and has no contractive merging.

**6.4.** Let \(N_0(a)=(\sum_ia_i^2)^{1/2}\). Compute \(N_0(F_Ja)\) and the limit \(N(a)\). Why is this no contradiction to Lemma 4.2?

**6.5.** In the proof of Proposition 3.1, why does one application of Ramsey's theorem to sets of \(k\) indices control the combinations of all lengths \(m\le k\)?

## 7. Solutions

**6.1.** For \(y\in c_0\) the entries of \(v-y\) tend to \(1\), so \(\|v-y\|\ge1\); and \(\|v-0\|=1\). Let \(y_j=(1,\dots,1,0,0,\dots)\) with \(j\) ones, and \(f_i\) the functional that takes the entry number \(i\). Then \(f_i(y_j)=1\) if \(j\ge i\) and \(0\) if \(j<i\).

**6.2.** \(z_{i_h}\) has ones at the first \(M+1-i_h\) places. The entry of \(\sum_ha_hz_{i_h}\) at a place \(q\) is the sum of the \(a_h\) with \(M+1-i_h\ge q\), that is of \(a_1,\dots,a_j\) for the largest \(j\) with \(i_j\le M+1-q\). So the norm is \(\max_j|a_1+\dots+a_j|\): here the limit norm \(N_0\) is the norm of Exercise 5.5 of the first lesson, and it is equal to \(N\).

**6.3.** Both norms do not see zeros. \(|a_i+a_{i+1}|\le|a_i|+|a_{i+1}|\) gives contractive merging for the first. For the second, \((1,1)\) has the norm \(\sqrt2\) and the merged array \((2)\) has the norm \(2\).

**6.4.** \(F_Ja\) has \(J\) entries \(a_i/J\) for every \(i\), so \(N_0(F_Ja)^2=\sum_iJ\cdot a_i^2/J^2\), and \(N_0(F_Ja)=J^{-1/2}(\sum_ia_i^2)^{1/2}\). So \(N(a)=0\). Lemma 4.2 assumes the lower bound of Proposition 3.1 by the partial sums, which the Euclidean norm does not satisfy: \((1,1,\dots,1)\) with \(m\) entries has the Euclidean norm \(\sqrt m\), not at least \(dm\).

**6.5.** Every \(m\) of the first \(k\) elements of the homogeneous set \(H\) are the first \(m\) elements of a subset of \(H\) with \(k\) elements, and the color of a subset contains the rounded norms of the combinations of its first \(m\) elements, for every \(m\le k\). The set \(H\) has \(2k\) elements so that there are always enough larger elements to add.

## References

- [OpenAI-M] OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, OpenAI Math Release preprint, 23 September 2026, Appendix A. https://github.com/openai/math/tree/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026
