# Signed Poisson sums and exponents below two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the upper bound of Theorem 5.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) for \(1<p<2\), following [OpenAI-LP, Sections 5 and 6]. It introduces a measure \(\nu\) under which every normalized increment of the points has the same distribution of sizes (Section 1), random sums over its points with random signs (Section 2), and, for \(p<2\), a random normalized gradient \(Y\) whose coordinates all have one heavy-tailed law (Section 3). Clipping \(Y\) and projecting back onto \(V\) with the projection of [Electrical flows and a weighted projection](electrical-flows-and-a-weighted-projection.md) gives the random gradient required by Lemma 3.1 of [Weighted moments and sampling](weighted-moments-and-sampling.md) (Section 4). Symmetric \(p\)-stable laws and their projections have earlier uses in geometry and algorithms (Indyk); here everything needed is proved.

We keep the notation of the previous lessons: points \(x_1,\dots,x_n\in\ell_p^m\), oriented pairs \(E\), distances \(\delta_e\), normalized gradients \(V\), and \(H=4\log(2n)\). Facts about characteristic functions are from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): a real random variable is determined in law by its characteristic function \(\theta\mapsto\mathbb Ee^{i\theta X}\) ([Fremlin, *Measure Theory*, Volume 2, Corollary 285M](https://www1.essex.ac.uk/maths/people/fremlin/cont28.htm)), and the characteristic function of a sum of independent variables is the product of theirs.

## 1. Homogeneous increments

Let \(\Omega=(0,\infty)\times\{1,\dots,m\}\) carry the measure \(\nu\) that is \(p\,r^{-p-1}\,dr\) on each copy of \((0,\infty)\). For \(e=ij\) let \(g_e(t)=\bigl(x_i(t)-x_j(t)\bigr)/\delta_e\), where \(x_i(t)\) is the \(t\)-th coordinate of \(x_i\), and
\[
v_e(r,t)=r\,g_e(t).
\]
For every \((r,t)\), \(v(r,t)=(v_e(r,t))_e\) lies in \(V\): it is the normalized gradient of the labels \(z_i=r\,x_i(t)\).

**Lemma 1.1.** For every pair \(e\) and \(a>0\), \(\nu(|v_e|>a)=a^{-p}\). More generally, for every Borel \(\phi\colon(0,\infty)\to[0,\infty]\),
\[
\int_{\{v_e\neq0\}}\phi(|v_e|)\,d\nu=p\int_0^\infty\phi(u)\,u^{-p-1}\,du .\tag{1.1}
\]
In particular \(\nu(\max_e|v_e|>a)\le|E|a^{-p}\).

**Proof.** On the copy \(t\) with \(g_e(t)\neq0\), substitute \(u=r|g_e(t)|\): the integral becomes \(|g_e(t)|^p\,p\int_0^\infty\phi(u)u^{-p-1}\,du\), and \(\sum_t|g_e(t)|^p=\|x_i-x_j\|_p^p/\delta_e^p=1\). Take \(\phi=\mathbf 1_{(a,\infty)}\) for the first statement. \(\square\)

So every coordinate of \(v\) has the same "law of sizes" under \(\nu\), although \(\nu\) is an infinite measure: it has finite second moment near \(0\) only when \(p<2\), and near infinity only when \(p>2\).

## 2. Signed Poisson sums

Let \(R\subseteq\Omega\) be measurable with \(0<\nu(R)=M<\infty\), and let \(h\) be a measurable map from \(\Omega\) to some \(\mathbb R^k\). The *signed Poisson sum* of \(h\) on \(R\) is
\[
S=\sum_{j=1}^N\varepsilon_jh(\omega_j),
\]
where \(N\) has the Poisson law of mean \(M\), the \(\omega_j\) have law \(\nu|_R/M\), the \(\varepsilon_j\) are uniform signs, and all these are independent; for \(M=0\) put \(S=0\). If \(h\) takes values in \(V\), so does \(S\).

**Lemma 2.1** (splitting). If \(R=R_1\cup R_2\) is a disjoint union, the signed Poisson sum of \(h\) on \(R\) has the law of the sum of independent signed Poisson sums of \(h\) on \(R_1\) and on \(R_2\).

**Proof.** Let \(N_1\) and \(N_2\) count the \(j\le N\) with \(\omega_j\in R_1\) and \(\omega_j\in R_2\), and \(p_k=\nu(R_k)/M\). Then \(\mathbb Es^{N_1}t^{N_2}=\mathbb E(sp_1+tp_2)^N=e^{\nu(R_1)(s-1)}e^{\nu(R_2)(t-1)}\), so \(N_1,N_2\) are independent Poisson variables of means \(\nu(R_1),\nu(R_2)\). Given \(N_1\) and \(N_2\), the points in \(R_k\) are independent with law \(\nu|_{R_k}/\nu(R_k)\), independent of the other part and of the signs. \(\square\)

**Lemma 2.2** (formulas). For a real \(h\) and its signed Poisson sum \(S\) on a region \(R\) of finite measure,
\[
\mathbb Ee^{i\theta S}=\exp\Bigl(\int_R\bigl(\cos(\theta h)-1\bigr)\,d\nu\Bigr).
\]
If \(h\) is bounded on \(R\), then also \(\mathbb Ee^{\theta S}=\exp\bigl(\int_R(\cosh(\theta h)-1)\,d\nu\bigr)\), \(\mathbb ES=0\) and \(\mathbb ES^2=\int_Rh^2\,d\nu\).

**Proof.** Given \(N\), \(S\) is a sum of \(N\) independent copies of \(\varepsilon h(\omega)\), whose characteristic function is \(\frac1M\int_R\cos(\theta h)\,d\nu\); and \(\mathbb Ez^N=e^{M(z-1)}\). The other formulas are obtained in the same way. \(\square\)

## 3. A heavy-tailed marginal

Let \(1<p<2\). Sample \(v\) on the region \(\{\|v\|_\infty>1\}\), of measure at most \(|E|\), and, independently, on each region \(A_k=\{2^{-k-1}<\|v\|_\infty\le2^{-k}\}\), \(k\ge0\), of measure at most \(|E|2^{p(k+1)}\); let \(Y^{(\infty)}\) and \(Y^{(k)}\) be these signed Poisson sums, all with values in \(V\). The \(Y^{(k)}\) are independent and centered, and for each pair \(e\)
\[
\sum_{k\ge0}\mathbb E|Y^{(k)}_e|^2=\int_{\{0<\|v\|_\infty\le1\}}|v_e|^2\,d\nu\le\int_{\{0<|v_e|\le1\}}|v_e|^2\,d\nu=\frac p{2-p},
\]
by Lemma 2.2 and (1.1). So \(\sum_kY^{(k)}\) converges in mean square, and
\[
Y=Y^{(\infty)}+\sum_{k\ge0}Y^{(k)}\in V
\]
almost surely, \(V\) being closed.

**Lemma 3.1** (one law for all pairs; OpenAI). For every pair \(e\) and real \(\theta\),
\[
\mathbb Ee^{i\theta Y_e}=\exp\Bigl(p\int_0^\infty\bigl(\cos(\theta u)-1\bigr)u^{-p-1}\,du\Bigr).
\]
Hence all \(Y_e\) have the same law \(\mu_p\), which depends only on \(p\).

**Proof.** By independence and Lemma 2.2, the partial sums \(Y^{(\infty)}_e+\sum_{k<K}Y^{(k)}_e\) have characteristic function \(\exp\bigl(\int_{\{\|v\|_\infty>2^{-K}\}}(\cos(\theta v_e)-1)\,d\nu\bigr)\). They converge to \(Y_e\) in mean square, hence their characteristic functions converge, since \(|\mathbb Ee^{i\theta X}-\mathbb Ee^{i\theta X'}|\le|\theta|\,\mathbb E|X-X'|\). The exponents converge because \(|\cos(\theta v_e)-1|\le\theta^2v_e^2/2\) is integrable on \(\{0<\|v\|_\infty\le1\}\). This gives \(\exp\bigl(\int_{\{v_e\neq0\}}(\cos(\theta v_e)-1)\,d\nu\bigr)\), and (1.1) with the evenness of the cosine gives the formula; the integral converges because its integrand is \(O(u^{1-p})\) near \(0\) and \(O(u^{-p-1})\) at infinity. The characteristic function determines the law. \(\square\)

**Lemma 3.2** (tails). There are \(0<c_p\le C_p\) such that \(c_pa^{-p}\le\mu_p\bigl(\{y:|y|>a\}\bigr)\le C_pa^{-p}\) for \(a\ge1\).

**Proof.** Fix \(e\) and \(a\ge1\). Let \(B\) be the signed Poisson sum of \(v_e\) on \(\{|v_e|>a\}\), a region of measure \(a^{-p}\), and let \(S\), independent of \(B\), be the mean-square limit of independent signed Poisson sums of \(v_e\) on the regions \(\{2^{-k-1}a<|v_e|\le2^{-k}a\}\), \(k\ge0\). As in Lemma 3.1, \(B+S\) has the characteristic function of \(Y_e\), so it has law \(\mu_p\). By Lemma 2.2 and (1.1), \(\mathbb ES^2=\int_{\{0<|v_e|\le a\}}v_e^2\,d\nu=\frac p{2-p}a^{2-p}\). If \(N_a\) is the number of terms of \(B\), then
\[
\mathbb P(|B+S|>a)\le\mathbb P(N_a\ge1)+\mathbb P(|S|>a)\le a^{-p}+\frac p{2-p}a^{-p}
\]
by Chebyshev's inequality. Conversely, on the event \(N_a=1\), let \(\pm u\) be the single term, with \(u>a\). For each value \(s\) of \(S\), at least one of \(|s+u|\) and \(|s-u|\) exceeds \(a\), and the sign is uniform and independent of \(S\) and \(u\); so \(\mathbb P(|B+S|>a)\ge\frac12\mathbb P(N_a=1)=\frac12a^{-p}e^{-a^{-p}}\ge\frac1{2e}a^{-p}\). \(\square\)

## 4. Clipping and projection

Let \(\lambda\) be a probability vector on \(E\) with positive entries, and take \(\sigma\ge\lambda/2\) and \(P=P(\sigma)\) from Lemma 2.1 of [Electrical flows and a weighted projection](electrical-flows-and-a-weighted-projection.md). For \(T>1\) let \([Y]_T\) be \(Y\) with each coordinate clipped to \([-T,T]\), and
\[
F=P[Y]_T .
\]
Then \(F\in V\) and \(\|F\|_\infty\le HT\).

**Lemma 4.1.** For every pair \(e\) and every \(T>1\),
\[
\mathbb E|Y_e-F_e|\le C_pHT^{1-p},\qquad\sum_e\sigma_e\,\mathbb E|F_e|^2\le C_pT^{2-p}.
\]

**Proof.** Since \(Y\in V\), \(Y=PY\), so \(Y-F=P(Y-[Y]_T)\) and \(|Y_e-F_e|\le\sum_f|P_{ef}|(|Y_f|-T)_+\). By Lemma 3.2, \(\mathbb E(|Y_f|-T)_+=\int_T^\infty\mathbb P(|Y_f|>s)\,ds\le C_pT^{1-p}\), and the row sums of \(P\) are at most \(H\). For the second bound, \(P\) does not increase \(\|\cdot\|_{2,\sigma}\), so \(\sum_e\sigma_e|F_e|^2\le\sum_e\sigma_e\min\{|Y_e|,T\}^2\) pointwise, and \(\mathbb E\min\{|Y_e|,T\}^2=\int_0^T2s\,\mathbb P(|Y_e|>s)\,ds\le1+C_p\int_1^T2s^{1-p}\,ds\le C_pT^{2-p}\). \(\square\)

**Proposition 4.2** (OpenAI). Let \(1<p<2\) and \(0<\eta<\frac16\). There are \(A\ge1\) and \(n_0\), depending only on \(p\) and \(\eta\), such that for \(n\ge n_0\), with
\[
T=\exp\bigl(AH^{2-p}\bigr),\qquad K=HT,\qquad b=\int\min\{|y|,T/H\}^p\,d\mu_p(y),
\]
we have \(b\ge1\), \(\log K\le C_{p,\eta}(\log n)^{2-p}\), and for every \(n\) distinct points of every \(\ell_p^m\) and every \(\lambda\), the gradient \(F\) above satisfies (3.1) of [Weighted moments and sampling](weighted-moments-and-sampling.md).

**Proof.** Let \(a=T/H\), assume \(a\ge2\), and write \(h_a(t)=\min\{|t|,a\}^p\), so that \(b=\mathbb Eh_a(Y_e)\) for every \(e\) by Lemma 3.1. By Lemma 3.2,
\[
b=\int_0^ap\,t^{p-1}\,\mathbb P(|Y_e|>t)\,dt\ge p\,c_p\log a .
\]
The function \(h_a\) is \(pa^{p-1}\)-Lipschitz, so by Lemma 4.1
\[
\bigl|\mathbb Eh_a(F_e)-b\bigr|\le pa^{p-1}C_pHT^{1-p}=C_pH^{2-p}\qquad(e\in E).
\]
Since \(p<2\), \(0\le|t|^p-h_a(t)\le a^{p-2}t^2\) for all real \(t\), so by Lemma 4.1
\[
\sum_e\sigma_e\,\mathbb E\bigl(|F_e|^p-h_a(F_e)\bigr)\le a^{p-2}C_pT^{2-p}=C_pH^{2-p}.
\]
Together, \(\sum_e\sigma_e\bigl|\mathbb E|F_e|^p-b\bigr|\le C_pH^{2-p}\). Now \(\log a=AH^{2-p}-\log H\ge\frac A2H^{2-p}\) for large \(n\), because \(H\to\infty\) and \(\log H\) is small compared with \(H^{2-p}\); so \(b\ge\frac{pc_pA}2H^{2-p}\ge1\) and \(a\ge2\) for \(n\ge n_0\). Choosing \(A\ge4C_p/(\eta pc_p)\) gives \(\sum_e\sigma_e|\mathbb E|F_e|^p-b|\le\frac12\eta b\), hence (3.1) since \(\lambda\le2\sigma\). Finally \(\log K=\log H+AH^{2-p}\le C_{p,\eta}(\log n)^{2-p}\). The numbers \(b\) and \(K\) depend only on \(p\), \(\eta\) and \(n\). \(\square\)

By Proposition 4.1 of [Weighted moments and sampling](weighted-moments-and-sampling.md), this proves the upper bound \(d_p(n,D)\le\exp\bigl(C_{p,D}(\log n)^{2-p}\bigr)\) of Theorem 5.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) for \(1<p<2\).

## 5. Exercises

**Exercise 5.1** (easy). For \(m=1\), check \(\nu(|v_e|>a)=a^{-p}\) directly.

**Exercise 5.2** (easy). Show that \(\mathbb E|Y_e|^2=\infty\) for \(1<p<2\), so that the second-moment bound of Lemma 4.1 needs the clipping.

**Exercise 5.3** (medium). Show that \(\mu_p\) is the symmetric \(p\)-stable law: its characteristic function is \(e^{-\kappa_p|\theta|^p}\) with \(\kappa_p=p\int_0^\infty(1-\cos u)u^{-p-1}\,du\in(0,\infty)\).

**Exercise 5.4** (medium). Where in the proof of Proposition 4.2 is \(p<2\) used, and where \(p>1\)?

## 6. Solutions

**5.1.** With one coordinate, \(|g_e(1)|=1\), so \(\nu(|v_e|>a)=\int_a^\infty pr^{-p-1}\,dr=a^{-p}\).

**5.2.** By Lemma 3.2, \(\mathbb E|Y_e|^2=\int_0^\infty2s\,\mathbb P(|Y_e|>s)\,ds\ge c_p\int_1^\infty2s^{1-p}\,ds=\infty\).

**5.3.** For \(\theta\neq0\), substitute \(u'=|\theta|u\) in \(p\int_0^\infty(\cos(\theta u)-1)u^{-p-1}\,du\): it becomes \(-|\theta|^p\,p\int_0^\infty(1-\cos u')u'^{-p-1}\,du'\). The integral converges at \(0\) because \(1-\cos u'\le u'^2/2\) and \(p<2\), and at infinity because \(p>0\); it is positive.

**5.4.** \(p>1\) makes \(\mathbb E(|Y_f|-T)_+\) finite and of order \(T^{1-p}\) (the first bound of Lemma 4.1). \(p<2\) is used for the finite second moment of the small terms (\(\int_0^1u^{1-p}\,du<\infty\)), for \(\mathbb E\min\{|Y|,T\}^2\le C_pT^{2-p}\), and for the inequality \(|t|^p-h_a(t)\le a^{p-2}t^2\).

## References

- [OpenAI-LP] OpenAI, *Subpolynomial dimension reduction in L_p*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, author's edition. https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
