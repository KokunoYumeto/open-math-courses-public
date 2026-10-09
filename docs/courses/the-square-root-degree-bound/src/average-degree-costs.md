# Average degree costs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The amplification criterion of [A tagged report](a-tagged-report.md) requires a rule whose every output costs at most \(d\) coordinates. This lesson shows that a saving *on average* suffices: if a partition of \(\mathbb R^q\) with label costs \(\ell\in\{1,\dots,q\}\) retains more variance than its average cost, then ratios of retained variance to degree can again be made arbitrarily large (Theorem 2.2). The step that restores a uniform degree bound reports typical words of many independent labels and merges all other words into a single failure cell. Section 1 turns any event with a conditional variance saving into such a partition, and Section 3 applies the criterion to three events: the reporting event of the previous lesson, a weighted-mixture event, and the coarse report with a small-width parameter schedule. Notation and tools are those of [Linear Fourier coefficients and degree](linear-fourier-coefficients-and-degree.md) and [Asymptotically normal scores](asymptotically-normal-scores.md); \(\mathbf G=(G_1,\dots,G_q)\) has independent standard normal coordinates and \(S_G=\sum_iG_i\).

## 1. Refining the complement of one event

A *costed partition* is a measurable map \(\mathcal P:\mathbb R^q\to\mathcal L\) to a finite label set with costs \(\ell:\mathcal L\to\{1,\dots,q\}\) such that, on every product of finite subsets of \(\mathbb R\), the indicator of each cell \(\{\mathcal P=l\}\) is a finite linear combination of functions of at most \(\ell(l)\) coordinates. Put
\[
V=\operatorname{Var}\bigl(\mathbb E[S_G\mid\mathcal P(\mathbf G)]\bigr),\qquad c=\mathbb E\,\ell(\mathcal P(\mathbf G)).
\]

**Lemma 1.1** (Refinement). Let \(A\subseteq\mathbb R^q\) be a Borel set with Gaussian-null boundary, \(p_A=\Pr(\mathbf G\in A)>0\), \(r_A=\operatorname{Var}(S_G\mid\mathbf G\in A)<1\), whose indicator is, on every product of finite subsets, a finite linear combination of functions of at most \(q-1\) coordinates. Then there is a costed partition with the cell \(A\) of cost \(q-1\) and finitely many other cells of cost \(q\), all with Gaussian-null boundaries, such that \(V>c=q-p_A\).

*Proof.* Cut \([-M,M)\) into half-open intervals of length at most \(h\), add the two tails, and approximate a coordinate by the midpoint of its bounded interval and by \(0\) on the tails. For a standard normal coordinate the expected squared error is at most \(h^2+\mathbb E[G_1^2\mathbf 1_{\{|G_1|\ge M\}}]\). Let \(\widetilde S\) be the sum of the coordinate approximations; it is constant on the boxes of the product grid. Since \((\sum_ia_i)^2\le q\sum_ia_i^2\), we can choose \(M\) and then \(h\) so that \(\mathbb E(S_G-\widetilde S)^2<p_A(1-r_A)\). The cells are \(A\) and the intersections of \(A^c\) with the grid boxes; their boundaries lie in \(\partial A\) and finitely many hyperplanes. Cells of cost \(q\) need no condition. Conditional means minimize squared error on each cell, so
\[
\mathbb E\operatorname{Var}\bigl(S_G\mid\mathcal P(\mathbf G)\bigr)\le p_Ar_A+\mathbb E\bigl[\mathbf 1_{A^c}(S_G-\widetilde S)^2\bigr]<p_A,
\]
and \(V=q-\mathbb E\operatorname{Var}(S_G\mid\mathcal P)>q-p_A=c\). \(\square\)

## 2. Amplification from an average saving

**Lemma 2.1** (Transfer for a fixed partition). Let \(\mathcal P\) be a costed partition with Gaussian-null cell boundaries. Let \(Z_n\) be centered, variance-one, asymptotically standard normal, with finitely many values, \(\mathbf Z_n\) consist of \(q\) independent copies, \(S_n\) their sum, \(L_n=\mathcal P(\mathbf Z_n)\), \(V_n=\operatorname{Var}(\mathbb E[S_n\mid L_n])\) and \(c_n=\mathbb E\ell(L_n)\). Then \(\liminf_nV_n\ge V\), \(c_n\to c\), and \(\mathbb E|Z_n|\to\sqrt{2/\pi}\).

*Proof.* By Lemma 3.1 of [Asymptotically normal scores](asymptotically-normal-scores.md), for every cell \(E\), \(\Pr(\mathbf Z_n\in E)\to\gamma(E)\) and \(\mathbb E[S_n\mathbf 1_E(\mathbf Z_n)]\to\mathbb E[S_G\mathbf 1_E(\mathbf G)]\). Since \(S_n\) is centered, \(V_n=\sum_l\mathbb E[S_n\mathbf 1_{\{L_n=l\}}]^2/\Pr(L_n=l)\) over labels of positive probability; the terms for cells of positive Gaussian probability converge to their Gaussian values, and the others are nonnegative. The cost converges with the finitely many cell probabilities. The last claim is Lemma 2.1 there. \(\square\)

**Theorem 2.2** (Amplification from a mean cost advantage). If a costed partition with Gaussian-null cell boundaries has \(V>c\), then finite observations have arbitrarily large ratios \(v(F)/D\), and the main theorem holds; the final Boolean function is the sign of one score, with no further averaging.

*Proof.* Fix \(0<\delta<(V-c)/2\) and \(1<\lambda<(V-\delta)/(c+\delta)\). For a finite observation \(F\) with \(v=v(F)>0\), let \(Z=T_F/\sqrt v\), and let \(V_Z\), \(c_Z\) be the quantities of Lemma 2.1 for \(q\) independent copies of \(Z\). We keep the invariant
\[
V_Z>V-\delta,\qquad c_Z<c+\delta/2,\qquad\mathbb E|Z|>\tfrac12 . \tag{2.1}
\]
By Lemma 2.1, (2.1) holds eventually along any sequence of centered, variance-one, asymptotically standard normal finite-valued \(Z\). *Start:* \(F=H_N\) has \(v=D=N\), and \(H_N/\sqrt N\) is asymptotically standard normal (Theorem 1.1 there), so some \(N\) satisfies (2.1); the ratio is \(1\).

*Step.* Apply \(\mathcal P\) to the standardized scores of \(q\) independent copies of \(F\), obtaining a label \(L\). Its cells have \(\deg\mathbf 1_{\{L=l\}}\le D\ell(l)\), its score is \(T_L=\sqrt v\,\mathbb E[S_Z\mid L]\), and \(\tau^2=v(L)=vV_Z>0\). Take \(K\) independent copies \(L_1,\dots,L_K\), retain the label words with \(\sum_b\ell(l_b)\le K(c+\delta)\), and let \(F'_K\) report retained words exactly and a single failure label otherwise. Retained-word indicators are products of degree at most \(D'_K=DK(c+\delta)\), and the failure indicator is one minus their sum, so \(D'_K\) is a cell degree bound. The costs are bounded with mean \(c_Z<c+\delta/2\), so the failure probability \(\varepsilon_K\to0\) (Lemma 4.2 there).

Let \(U_K=\sum_bT_{L_b}\) and \(T'_K=\mathbb E[U_K\mid F'_K]\), the score of \(F'_K\). On retained words \(U_K\) is known exactly; on failure, the conditional mean predicts at least as well as \(0\). So
\[
\mathbb E(U_K-T'_K)^2\le\mathbb E[U_K^2\mathbf 1_{\mathrm{fail}}]\le(\mathbb EU_K^4)^{1/2}\varepsilon_K^{1/2}=o(K\tau^2),
\]
since \(\mathbb EU_K^4=K\mathbb ET_L^4+3K(K-1)\tau^4=O(K^2)\) for the fixed \(L\). Hence \(v(F'_K)=K\tau^2-\mathbb E(U_K-T'_K)^2\sim K\tau^2\). By the central limit theorem \(U_K/(\sqrt K\tau)\) is asymptotically standard normal; by Lemma 4.1 there, so are \(T'_K/(\sqrt K\tau)\) and \(T'_K/\sqrt{v(F'_K)}\). By Lemma 2.1, (2.1) holds for \(F'_K\) when \(K\) is large, and
\[
\frac{v(F'_K)}{D'_K}\longrightarrow\frac vD\cdot\frac{V_Z}{c+\delta}>\lambda\frac vD .
\]
*End.* After \(k\) steps with \(\lambda^k>4C^2\), the observation has \(v/D>4C^2\) and \(\mathbb E|T_F|>\frac12\sqrt v>C\sqrt D\); by Corollary 3.2 of [Linear Fourier coefficients and degree](linear-fourier-coefficients-and-degree.md), \(f=\operatorname{sign}(T_F)\) proves the theorem. \(\square\)

## 3. Three applications

**(a) The reporting event.** With \(q=m+1\) and the event \(A\) of the refined report with the design of Lemma 3.1 of [A tagged report](a-tagged-report.md): its boundary lies in finitely many hyperplanes, its indicator has cost \(m=q-1\) by (2.1) there, and \(d_A>0\) gives \(p_A>0\) and \(\operatorname{Var}(L\mid A)<1\). Lemma 1.1 and Theorem 2.2 give the main theorem again.

**(b) A weighted mixture.** For \(R>0\) put
\[
m=1+\bigl\lceil e^{R^2/4}\bigr\rceil,\qquad\Delta=\frac{2R}{m-1},\qquad h=e^{-3R^2/8},\qquad q=m+1 .
\]
Let \(\mathbf G=(G_0,\dots,G_m)\) and \(L=\sum_jG_j\). Cut \([-R,R)\) into \(m-1\) half-open bins \(B_1,\dots,B_{m-1}\) of length \(\Delta\), and let \(B_m=\mathbb R\setminus[-R,R)\). Let \(\pi_i,v_i,u_i\) be the probability, conditional mean and conditional variance of \(G_0\) on \(B_i\), and give leaf \(j\) the interval \(I_j=[v_j+1-h/2,\,v_j+1+h/2)\). The event \(A\) holds when, for the bin \(B_i\) containing \(g_0\), every leaf \(j\ne i\) lies in \(I_j\) and leaf \(i\) does not. As in (2.1) of the previous lesson,
\[
\mathbf 1_A(g)=\sum_{i=1}^m\mathbf 1_{B_i}(g_0)\prod_{j\ne i}\mathbf 1_{I_j}(g_j)-\prod_{j=1}^m\mathbf 1_{I_j}(g_j),
\]
a combination of functions of \(m=q-1\) coordinates, and the boundary of \(A\) lies in finitely many hyperplanes.

**Lemma 3.1** (The weighted mixture). For all large \(R\), \(p_A=\Pr(\mathbf G\in A)>0\) and \(\operatorname{Var}(L\mid\mathbf G\in A)<1\).

*Proof.* *Bin moments.* By symmetry \(v_m=0\); for \(i<m\), \(v_i\) lies in the closure of \(B_i\), so \(|v_i|\le R\) and \(u_i\le\Delta^2\). Since \(\int_R^\infty t^2\phi=R\phi(R)+\int_R^\infty\phi\) and \(\int_R^\infty\phi\le\phi(R)/R\), \(\pi_mu_m=O(Re^{-R^2/2})\). Also \(\sum_i\pi_iv_i=0\) and \(\sum_i\pi_iv_i^2=1-\sum_i\pi_iu_i=1-o(1)\), because \(\Delta^2\le4R^2e^{-R^2/2}\).

*Leaf moments.* Let \(\alpha_j,t_j,r_j\) be the probability, conditional mean and variance on \(I_j\). For large \(R\), \(0<\alpha_j\le h/\sqrt{2\pi}<\frac12\), \(|t_j-(v_j+1)|\le h/2\) and \(r_j\le h^2\). On \(I_j^c\) the conditional mean and variance are \(d_j=-\alpha_jt_j/(1-\alpha_j)\) and \(b_j=\frac{1-\alpha_jr_j}{1-\alpha_j}-\frac{\alpha_jt_j^2}{(1-\alpha_j)^2}\), from the total mean \(0\) and second moment \(1\).

*Mixture identity.* Put \(w_i=\pi_i(1-\alpha_i)/\alpha_i\), \(W=\sum_iw_i\), \(\omega_i=w_i/W\). By independence \(\Pr(A\cap\{G_0\in B_i\})=w_i\prod_j\alpha_j\), so \(p_A=W\prod_j\alpha_j>0\) and the conditional bin weights are \(\omega_i\). Given \(A\) and \(G_0\in B_i\), the coordinates are independent with the bin, interval and complement restrictions, so \(L\) has mean \(\sum_jt_j-1+e_i\), with \(e_i=v_i+1-t_i/(1-\alpha_i)=O(h(R+2))\), and variance \(u_i+\sum_jr_j+b_i-r_i\). The variance decomposition with the weights \(\omega_i\) gives
\[
W\bigl(1-\operatorname{Var}(L\mid A)\bigr)=\sum_iw_i(1-b_i+r_i)-\sum_iw_iu_i-W\sum_jr_j-W\operatorname{Var}_{\omega}(e_i).
\]

*The main term.* Substituting \(b_i\), \(w_i(1-b_i+r_i)=\pi_i\bigl(-1+r_i/\alpha_i+t_i^2/(1-\alpha_i)\bigr)\ge\pi_i(t_i^2-1)\), and \(\sum_i\pi_i(t_i^2-1)=\sum_i\pi_iv_i^2+2\sum_i\pi_iv_i+O(h(R+2))=1+o(1)\): because the leaf intervals are shifted by one, \(t_i^2-1\approx v_i^2+2v_i\), whose \(\pi\)-average is close to \(1\).

*The error terms.* For \(i<m\), with \(x=|v_i|\le R\), \(\pi_i\le\Delta\phi(\max\{0,x-\Delta\})\) and \(\alpha_i\ge h\phi(x+1+h)\), and \(\frac12\bigl((x+1+h)^2-\max\{0,x-\Delta\}^2\bigr)\le(1+h+\Delta)x+\frac{(1+h)^2}2\le3R\) for large \(R\); so \(w_i\le\frac\Delta he^{3R}\). For the tail bin, \(\alpha_m\ge h\phi(1+h)\), so \(w_m\le C\pi_m/h\). Hence \(W\le(2Re^{3R}+C)/h\). Then \(\sum_iw_iu_i\le W\Delta^2+C\pi_mu_m/h=O(R^3e^{3R-R^2/8})+O(Re^{-R^2/8})\), \(W\sum_jr_j\le Wmh^2=O((Re^{3R}+1)e^{-R^2/8})\), and \(W\operatorname{Var}_\omega(e_i)\le W\max_ie_i^2=O((Re^{3R}+1)(R+2)^2e^{-3R^2/8})\), all tending to \(0\). So \(W(1-\operatorname{Var}(L\mid A))\ge1+o(1)>0\). \(\square\)

These error terms are small only for large \(R\): to leading order the largest one, \(\sum_iw_iu_i\), is \(\frac{R^2}3e^{R+1/2-R^2/8}\), which is below \(\frac12\) only for \(R\) above about \(11.5\), where \(m>e^{33}\). With one such \(R\) fixed, Lemma 1.1 and Theorem 2.2 give the main theorem a third time.

**(c) The coarse report with small width.** For \(0<w<1\) put \(h=w^{2/3}\) and \(T=\sqrt{4\log(1/w)}\), so \(e^{-T^2/2}=w^2\). Let \(t_1<\dots<t_m\) be the points of \(h\mathbb Z\cap[-T,T]\), \(i_*\) the index of \(0\), \(I(t)\) the index of a nearest grid point for \(|t|\le T\) (smaller index on ties) and \(I(t)=i_*\) for \(|t|>T\), and \(A_j=[t_j+1-w/2,\,t_j+1+w/2]\). Apply the coarse report of Proposition 5.1 of [A tagged report](a-tagged-report.md) with central input \(t\), selector \(I\) and leaf intervals \(A_j\); for small \(w\), \(m\ge3\).

**Proposition 3.2.** For a centered variance-one input law \(U\) with finitely many values and \(q_j=\Pr(U\in A_j)\in(0,1)\), conditional means \(\mu_j\) and variances \(a_j\) on \(A_j\), \(Q=\prod_jq_j\), \(M_\mu=\sum_j\mu_j\) and \(S_a=\sum_ja_j\), the coarse report retains variance at least \(m+QH_w(U)\), where
\[
H_w(U)=1-\mathbb E_t\Bigl[\frac{(t+1-\mu_{I(t)})^2+S_a-a_{I(t)}}{q_{I(t)}}\Bigr],
\]
with \(t\) distributed as \(U\). For \(U=G\), \(H_w(G)\to1\) as \(w\downarrow0\). For a fixed small \(w\) with \(H_w(G)>\frac12\) and \(\eta=Q_G/4\), finite-valued centered variance-one asymptotically standard normal \(U_n\) satisfy \(Q_nH_w(U_n)>\eta\) for large \(n\), so the coarse report with this schedule satisfies the amplification criterion with \((r,d,\eta)=(m+1,m,Q_G/4)\).

*Proof.* *The gain of a predictor.* Predict by \(M_\mu-1\) on \(X\), by \(M_\mu\) on \(Y\), and by the reported sum on ordinary outputs. Fixing \(t\) with \(i=I(t)\), the event \(P\) has conditional probability \(Q/q_i\), and \(L-(M_\mu-1)\) has mean \(t+1-\mu_i\) and variance \(1+S_a-a_i\); on \(B\), the deficits for the two predictors are \(-Q(1+S_a)\) and \(-QS_a\). Subtracting the \(B\) part from the \(P\) part for \(X\) and adding the \(Y\) part cancels \(S_a\), and Proposition 5.1 there gives the bound \(m+QH_w(U)\).

*Gaussian limit.* \(q_j\le w/\sqrt{2\pi}\), \(|\mu_j-(t_j+1)|\le w/2\), and \(S_a\le mw^2=O(Tw^{4/3})\). For \(|t|\le T\) and \(z\in A_{I(t)}\), \(|z-t|\le1+h+w/2\le2\), so \(\log(\phi(t)/\phi(z))\le2|t|+2\) and \(\phi(t)/q_{I(t)}\le w^{-1}e^{2T+2}=O(w^{-7/6})\), as \(e^{2T}\) grows more slowly than every power of \(1/w\). The fallback interval centred at \(1\) has \(q_{i_*}\ge cw\). Hence \(\mathbb E[1/q_{I(G)}]=O(Tw^{-7/6})\), the variance term is \(O(mw^2Tw^{-7/6})=O(T^2w^{1/6})\), the central mismatch \(|t+1-\mu_{I(t)}|\le h+w/2\) contributes \(O(Tw^{-7/6}(h+w)^2)=O(Tw^{1/6})\), and the tails contribute \(O(w^{-1}(1+T)e^{-T^2/2})=O((1+T)w)\). So \(H_w(G)\to1\). The convergence is slow: to leading order \(1-H_w(G)\approx\bigl(\frac{h^2}{12}+\frac{2T}h\cdot\frac{w^2}{12}\bigr)\frac{e^{T+1/2}}w\), which is below \(\frac12\) only when \(\log(1/w)\) exceeds about \(48\).

*Transfer.* With \(w\) fixed, the finitely many interval probabilities, conditional means and variances of \(U_n\) converge to the Gaussian ones by Lemma 2.1 of [Asymptotically normal scores](asymptotically-normal-scores.md), and are eventually bounded away from \(0\) and \(1\). On each selector cell \(\{t:I(t)=i\}\), a finite union of intervals, the integrand is a polynomial of degree at most two in \(t\) with convergent coefficients, and the restricted moments \(\mathbb E[U_n^k\mathbf 1_{\{I(U_n)=i\}}]\), \(k\le2\), converge by the same lemma. Hence \(Q_nH_w(U_n)\to Q_GH_w(G)>Q_G/2\). The cost bound is that of the coarse report. \(\square\)

## 4. Exercises

**4.1.** In Theorem 2.2, why is the failure cell's degree bounded even though a failing word may contain many expensive labels?

**4.2.** Show that in Lemma 1.1 one cannot simply leave \(A^c\) as a single cell: compute \(V\) for the partition \(\{A,A^c\}\) and compare with \(q-p_A\).

**4.3.** In the weighted mixture, why does the conditional bin distribution use the weights \(\omega_i\propto\pi_i(1-\alpha_i)/\alpha_i\) rather than \(\pi_i\)?

## 5. Solutions

**4.1.** The failure indicator equals one minus the sum of the retained-word indicators, each of degree at most \(D'_K\); so its degree is at most \(D'_K\), whatever the degrees of the individual failing words.

**4.2.** Since \(\mathbb ES_G=0\), the two cells give \(V=\mathbb E[S_G\mathbf 1_A]^2/(p_A(1-p_A))=p_A\,\mathbb E[S_G\mid A]^2/(1-p_A)\). For the events of Section 3, \(p_A\) is a product of many small interval probabilities while \(\mathbb E[S_G\mid A]\) is about \(q-2\), so \(V\) is tiny compared with \(q-p_A>q-1\): almost all the variance of \(S_G\) would be unobserved. The refinement keeps the sum observed off \(A\) up to a small rounding error.

**4.3.** On \(A\) with \(G_0\in B_i\), leaf \(i\) must fail (probability \(1-\alpha_i\)) and all other leaves must pass (probability \(\prod_{j\ne i}\alpha_j=\prod_j\alpha_j/\alpha_i\)). So the joint probability is \(\pi_i\frac{1-\alpha_i}{\alpha_i}\prod_j\alpha_j\), and conditioning on \(A\) reweights the bins by \(\pi_i(1-\alpha_i)/\alpha_i\).

## References

- [OpenAI-SR] OpenAI, *Unbounded violations of the square-root degree bound*, OpenAI Math Release preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/paper.pdf
