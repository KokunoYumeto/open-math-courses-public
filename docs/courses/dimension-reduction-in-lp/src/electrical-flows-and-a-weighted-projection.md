# Electrical flows and a weighted projection

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Both constructions of the upper bound produce random vectors that are close to the space \(V\) of normalized gradients of [Weighted moments and sampling](weighted-moments-and-sampling.md) and then project them onto \(V\). For the size bound \(\|F\|_\infty\le K\) to survive, the projection must have small absolute row sums. This lesson proves that, for every weighting of the pairs, a suitable reweighting gives an orthogonal projection onto \(V\) whose absolute row sums are at most \(4\log(2n)\) (Lemma 2.1) [OpenAI-LP, Section 4]. The key input is a bound for electrical flows due to Gurel-Gurevich, Nachmias and Sachdeva [GGNS], which improved an earlier bound \(O(\log^2n)\) of Schild, Rao and Srivastava [SRS]; we prove it by their heat-kernel and entropy method (Lemma 1.3).

For a matrix \(T\), \(|T|\) denotes the matrix of absolute values of its entries, and \(\|T\|_{2\to2}\) its operator norm on Euclidean space.

## 1. Electrical flows

Let \(G\) be a connected graph on \(n\ge2\) vertices without loops (parallel edges are allowed), with each edge \(e\) oriented from one end to the other, and let \(B\) be its incidence matrix: the row of \(e=(i\to j)\) has \(1\) in column \(i\), \(-1\) in column \(j\), and \(0\) elsewhere. Let \(c_e>0\) be conductances, \(C=\operatorname{diag}(c_e)\), and let \(Q\) be the Euclidean orthogonal projection of \(\mathbb R^{E(G)}\) onto the image of \(C^{1/2}B\). The entry \(Q_{ef}\) is, up to the factors \(\sqrt{c_e},\sqrt{c_f}\), the current through \(e\) when a unit current enters at one end of \(f\) and leaves at the other; that is why \(Q\) describes electrical flows.

**Lemma 1.1.** For every real matrix \(A\), the orthogonal projection onto the image of \(A\) equals \(\int_0^\infty Ae^{-tA^{\mathsf T}A}A^{\mathsf T}\,dt\).

**Proof.** Write \(A=\sum_k s_k\,u_kv_k^{\mathsf T}\) with orthonormal families \((u_k)\), \((v_k)\) and singular values \(s_k>0\). Then \(Ae^{-tA^{\mathsf T}A}A^{\mathsf T}=\sum_ks_k^2e^{-ts_k^2}u_ku_k^{\mathsf T}\), and \(\int_0^\infty s^2e^{-ts^2}\,dt=1\) for \(s>0\). So the integral is \(\sum_ku_ku_k^{\mathsf T}\), the projection onto the span of the \(u_k\), which is the image of \(A\). \(\square\)

**Lemma 1.2** (heat kernel). Let \(\mu\) be a probability vector on the vertices with positive entries, \(M=\operatorname{diag}(\mu_i)\), \(L=B^{\mathsf T}CB\) and \(K_s=e^{-sM^{-1}L}M^{-1}\) for \(s\ge0\). Then \(K_s=M^{-1/2}e^{-sS}M^{-1/2}\) with the symmetric matrix \(S=M^{-1/2}LM^{-1/2}\); \(K_{2s}=K_sMK_s\); for a vertex \(v\) the vector \(h_s=K_s\mathbf e_v\) has positive entries for \(s>0\), \(\mu^{\mathsf T}h_s=1\), \(h_0=\mu_v^{-1}\mathbf e_v\), and \(h_s\to\mathbf 1\) as \(s\to\infty\).

**Proof.** Since \(M^{-1}L=M^{-1/2}SM^{1/2}\), we have \(e^{-sM^{-1}L}=M^{-1/2}e^{-sS}M^{1/2}\), which gives the first formula, and then \(K_sMK_s=M^{-1/2}e^{-2sS}M^{-1/2}=K_{2s}\). The off-diagonal entries of \(-M^{-1}L\) are \(\mu_i^{-1}\sum_{e\text{ joins }i,j}c_e\ge0\), positive exactly for adjacent vertices. For \(\kappa\) large, \(N=\kappa I-M^{-1}L\) has nonnegative entries and positive diagonal, so by connectivity \(N^k\) has positive entries for \(k\ge n\), and \(e^{-sM^{-1}L}=e^{-s\kappa}\sum_ks^kN^k/k!\) has positive entries for \(s>0\); hence so does \(h_s=\mu_v^{-1}e^{-sM^{-1}L}\mathbf e_v\). Since \(\mathbf 1^{\mathsf T}L=0\), \(\frac d{ds}\mu^{\mathsf T}h_s=-\mathbf 1^{\mathsf T}Lh_s=0\), and \(\mu^{\mathsf T}h_0=1\). Finally, \(S\succeq0\) and its kernel is spanned by the unit vector \(M^{1/2}\mathbf 1\) (the kernel of \(L\) consists of the constants, by connectivity), so \(e^{-sS}\to M^{1/2}\mathbf 1\mathbf 1^{\mathsf T}M^{1/2}\) and \(K_s\to\mathbf 1\mathbf 1^{\mathsf T}\). \(\square\)

**Lemma 1.3** (localization of electrical flows; Gurel-Gurevich, Nachmias and Sachdeva). \(\bigl\|\,|Q|\,\bigr\|_{2\to2}\le2\log n\).

**Proof.** Since \(|Q|\) is symmetric with nonnegative entries, \(|x^{\mathsf T}|Q|x|\le|x|^{\mathsf T}|Q|\,|x|\), so it suffices to show \(w^{\mathsf T}|Q|w\le2\log n\,|w|^2\) for vectors \(w\) with positive entries; vectors with nonnegative entries follow by continuity. Fix such a \(w\), let \(\mu_i=\sum_{e\ni i}w_e^2/(2|w|^2)\), a probability vector with positive entries since every vertex lies on an edge, and use the notation of Lemma 1.2.

*Heat-kernel formula.* With \(A=C^{1/2}BM^{-1/2}\) we have \(A^{\mathsf T}A=S\), \(Ae^{-tS}A^{\mathsf T}=C^{1/2}BK_tB^{\mathsf T}C^{1/2}\), and the image of \(A\) is that of \(C^{1/2}B\). By Lemma 1.1, the substitution \(t=2s\), and \(K_{2s}=K_sMK_s=\sum_v\mu_vK_s\mathbf e_v\mathbf e_v^{\mathsf T}K_s\),
\[
Q=2\int_0^\infty\sum_v\mu_v\bigl(C^{1/2}BK_s\mathbf e_v\bigr)\bigl(C^{1/2}BK_s\mathbf e_v\bigr)^{\mathsf T}ds,\qquad w^{\mathsf T}|Q|w\le2\sum_v\mu_v\int_0^\infty\bigl(w^{\mathsf T}C^{1/2}|Bh_s|\bigr)^2ds,
\]
where \(h_s=K_s\mathbf e_v\) depends on \(v\).

*Entropy.* For a vector \(h\) with positive entries let \(\mathcal I(h)=\sum_{e=(i\to j)}c_e\bigl(h_i-h_j\bigr)\bigl(\log h_i-\log h_j\bigr)=h^{\mathsf T}L\log h\ge0\). Since \(\frac d{ds}h_s=-M^{-1}Lh_s\) and \(\mathbf 1^{\mathsf T}L=0\),
\[
\frac d{ds}\sum_i\mu_ih_s(i)\log h_s(i)=-\sum_i(Lh_s)_i\bigl(\log h_s(i)+1\bigr)=-\mathcal I(h_s)\qquad(s>0).
\]
As \(s\to0\) the entropy tends to \(\mu_v\cdot\mu_v^{-1}\log\mu_v^{-1}=\log(1/\mu_v)\) (with \(0\log0=0\)), and as \(s\to\infty\) it tends to \(0\). So \(\int_0^\infty\mathcal I(h_s)\,ds=\log(1/\mu_v)\).

*Cauchy–Schwarz.* For \(a,b>0\), \(\frac{a-b}{\log a-\log b}=\int_0^1a^ub^{1-u}\,du\le\frac{a+b}2\) (read as \(a\) when \(a=b\)). Hence, for each edge \(e=(i\to j)\), \(\sqrt{c_e}|h_i-h_j|\le\sqrt{c_e(h_i-h_j)(\log h_i-\log h_j)}\sqrt{(h_i+h_j)/2}\), and by the Cauchy–Schwarz inequality
\[
\bigl(w^{\mathsf T}C^{1/2}|Bh_s|\bigr)^2\le\mathcal I(h_s)\sum_{e=(i\to j)}w_e^2\frac{h_s(i)+h_s(j)}2=\mathcal I(h_s)\,|w|^2\sum_i\mu_ih_s(i)=\mathcal I(h_s)\,|w|^2 .
\]

*Conclusion.* Combining, \(w^{\mathsf T}|Q|w\le2|w|^2\sum_v\mu_v\log(1/\mu_v)\le2|w|^2\log n\), since the entropy of a probability vector on \(n\) points is at most \(\log n\). \(\square\)

## 2. A projection with small row sums

Return to the points \(x_1,\dots,x_n\) of [Weighted moments and sampling](weighted-moments-and-sampling.md), the oriented pairs \(E\), the distances \(\delta_e\) and the space \(V\). For a probability vector \(\sigma\) on \(E\) with positive entries, let \(P(\sigma)\) be the orthogonal projection onto \(V\) with respect to \(\|\cdot\|_{2,\sigma}\), and let \(R_e(\sigma)=\sum_f|P(\sigma)_{ef}|\) be its absolute row sums. Put
\[
H=4\log(2n).
\]

**Lemma 2.1** (weighted projection; OpenAI). For every probability vector \(\lambda\) on \(E\) with positive entries there is a probability vector \(\sigma\) with \(\sigma_e\ge\lambda_e/2\) for all \(e\) such that \(R_e(\sigma)\le H\) for every \(e\). In particular \(\|P(\sigma)f\|_\infty\le H\|f\|_\infty\) for every \(f\), and \(P(\sigma)\) and \(I-P(\sigma)\) do not increase \(\|\cdot\|_{2,\sigma}\).

**Proof.** Let \(D_\sigma=\operatorname{diag}(\sqrt{\sigma_e})\). The map \(D_\sigma\) is an isometry from \((\mathbb R^E,\|\cdot\|_{2,\sigma})\) to Euclidean space, so \(Q(\sigma)=D_\sigma P(\sigma)D_\sigma^{-1}\) is the Euclidean orthogonal projection onto \(D_\sigma V\). Since \(V\) is the image of \(\operatorname{diag}(\delta_e^{-1})B\) for the incidence matrix \(B\) of the complete graph on the \(n\) points, \(D_\sigma V\) is the image of \(C_\sigma^{1/2}B\) with \(C_\sigma=\operatorname{diag}(\sigma_e/\delta_e^2)\). From \(Q(\sigma)_{ef}=\sqrt{\sigma_e}P(\sigma)_{ef}/\sqrt{\sigma_f}\) we get \(\bigl(|Q(\sigma)|\sqrt\sigma\bigr)_e=\sqrt{\sigma_e}R_e(\sigma)\), so Lemma 1.3 and \(|\sqrt\sigma|=1\) give
\[
\sum_e\sigma_eR_e(\sigma)^2=\bigl|\,|Q(\sigma)|\sqrt\sigma\,\bigr|^2\le(2\log n)^2 .\tag{2.1}
\]
The set \(\Sigma=\{\sigma:\sum_e\sigma_e=1,\ \sigma_e\ge\lambda_e/2\}\) is compact, convex and nonempty. On \(\Sigma\), \(P(\sigma)\) depends continuously on \(\sigma\): if the columns of a matrix \(Y\) form a basis of \(V\), then \(P(\sigma)=Y\bigl(Y^{\mathsf T}D_\sigma^2Y\bigr)^{-1}Y^{\mathsf T}D_\sigma^2\). Let
\[
u_e(\sigma)=\frac{\sigma_eR_e(\sigma)^2}{2(2\log n)^2},\qquad\Phi_e(\sigma)=u_e(\sigma)+\Bigl(1-\sum_fu_f(\sigma)\Bigr)\lambda_e .
\]
By (2.1), \(\sum_fu_f\le\frac12\), so \(\Phi\) is a continuous map of \(\Sigma\) into itself. By Brouwer's theorem for compact convex sets (Corollary 1.2 of [Lebesgue's covering theorem and the dimension of cubes](course:index-theory-of-elliptic-operators/lebesgue-s-covering-theorem-and-the-dimension-of-cubes#1-fixed-points-on-compact-convex-sets)), \(\Phi\) has a fixed point \(\sigma\). There \(u_e(\sigma)\le\Phi_e(\sigma)=\sigma_e\), and since \(\sigma_e>0\), \(R_e(\sigma)\le2\sqrt2\log n\le H\). The remaining statements follow because the largest absolute row sum is the norm on \(\ell_\infty\), and orthogonal projections do not increase the norm. \(\square\)

The constructions use this lemma as follows: given \(\lambda\), take \(\sigma\) and \(P=P(\sigma)\) from Lemma 2.1, and construct \(F\in V\) with \(\sum_e\sigma_e\bigl|\mathbb E|F_e|^p-b\bigr|\le\frac12\eta b\); since \(\lambda\le2\sigma\), this gives (3.1) of [Weighted moments and sampling](weighted-moments-and-sampling.md).

## 3. Exercises

**Exercise 3.1** (easy). For the path with two vertices and one edge of conductance \(c\), compute \(Q\) and check Lemma 1.3.

**Exercise 3.2** (easy). Show that \(\frac{a-b}{\log a-\log b}=\int_0^1a^ub^{1-u}\,du\) and that this is at most \(\frac{a+b}2\).

**Exercise 3.3** (medium). For the cycle with \(n\) vertices and unit conductances, show that \(Q=I-\frac1n\mathbf 1\mathbf 1^{\mathsf T}\) (with all edges oriented around the cycle), and compute \(\|\,|Q|\,\|_{2\to2}\). Compare with \(2\log n\).

**Exercise 3.4** (medium). Show that without the reweighting, the absolute row sums of a weighted projection onto \(V\) can be large: explain why (2.1) alone only bounds a weighted average of the squared row sums.

## 4. Solutions

**3.1.** \(C^{1/2}B=\sqrt c\,(1,-1)\), whose image is \(\mathbb R\), so \(Q=(1)\) and \(\|\,|Q|\,\|=1\le2\log2\).

**3.2.** \(\int_0^1a^ub^{1-u}\,du=b\int_0^1(a/b)^u\,du=b\frac{a/b-1}{\log(a/b)}\). By the inequality of weighted arithmetic and geometric means, \(a^ub^{1-u}\le ua+(1-u)b\), whose integral is \(\frac{a+b}2\).

**3.3.** The image of \(B\) consists of the edge vectors with zero sum around the cycle, since a vector \(f\) is a gradient \(f_k=z_k-z_{k+1}\) exactly when \(\sum_kf_k=0\). So \(Q\) is the projection onto \(\mathbf 1^\perp\), namely \(I-\frac1n\mathbf 1\mathbf 1^{\mathsf T}\). Its absolute value has diagonal \(1-\frac1n\) and off-diagonal \(\frac1n\), so \(\|\,|Q|\,\|=|Q|\mathbf 1/\mathbf 1=2-\frac2n\), well below \(2\log n\) for large \(n\).

**3.4.** (2.1) gives \(\sum_e\sigma_eR_e^2\le(2\log n)^2\); a pair \(e\) with tiny weight \(\sigma_e\) can have \(R_e\) of order \((\log n)/\sqrt{\sigma_e}\). The fixed point of Lemma 2.1 increases the weight of pairs with large row sums until \(\sigma_eR_e^2\) is at most a constant times \(\sigma_e(\log n)^2\).

## References

- [OpenAI-LP] OpenAI, *Subpolynomial dimension reduction in L_p*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026
- [GGNS] O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A tight bound on localization of electrical flows*, 2026. https://arxiv.org/abs/2605.24130
- [SRS] A. Schild, S. Rao and N. Srivastava, *Localization of electrical flows*, SODA 2018. https://arxiv.org/abs/1708.01632
