# Uniform decay and the characterization

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the decay theorem of [Type, cotype and K-convexity](type-cotype-and-k-convexity.md) (Theorem 2.3 there). Iterating the growth lemma of [Growth from a slow decrease](growth-from-a-slow-decrease.md) against the fixed bound \(D_T2^{-n/2}\) of a finite-rank operator shows that slow decrease is impossible beyond an index that depends only on the cotype data; so Walsh norms of finite-rank operators, and of their norm limits, decay uniformly (Theorem 1.1). The approximation property then transfers this decay to the identity of the space, through a compact map whose domain keeps a controlled cotype estimate on its dual (Lemma 2.1). A last section derives a consequence for tensor norms from two further results of the literature.

- Uniform decay for finite-rank operators (Theorem 1.1).
- A compact domain with controlled dual moments (Lemma 2.1).
- Proof of the decay theorem (Section 3).
- Grothendieck pairs (Section 4).

The lesson follows [OpenAI-CC, Sections 4.2, 5 and 6]. Notation is that of [Walsh norms and moment lifts](walsh-norms-and-moment-lifts.md).

## 1. Uniform decay for finite-rank operators

**Theorem 1.1** (uniform decay; [OpenAI-CC, Theorem 4.3]). Fix \(m,D_g,D_f\) as in Lemma 2.1 of the previous lesson, with its constant \(c_1\). There is an integer \(n_0\), depending only on \(m,D_g,D_f\), such that every finite-rank \(T\colon G\to F\) with \(c_m(G^*)\le D_g\) and \(c_m(F)\le D_f\) satisfies
for \(n\ge n_0\),
\[
w_n(T)\le\tfrac12w_{n-2m}(T). \tag{1.1}
\]
Consequently there are numbers \(\rho_N\to0\), independent of \(G,F,T\), with
\[
w_N(T)\le\rho_N\|T\| . \tag{1.2}
\]
Both bounds hold for every \(T\colon G\to F\) that is an operator-norm limit of finite-rank maps, under the same hypotheses on \(G^*\) and \(F\).

*Proof.* Choose an integer \(K>\log_2(1/c_1)\) and put \(n_0=4m(K+2)+2\). Let \(T\ne0\) have finite rank, and suppose that \(w_{n-2m}(T)\le2w_n(T)\) for some \(n\ge n_0\). By the growth lemma, \(w_{2n-4m}(T)\ge c_1w_n(T)\), and by monotonicity this lower bound holds on the whole interval \([n,2n-4m]\). Let \(a_n=\lceil3n/2\rceil\). The \(K\) consecutive blocks
\[
\begin{gathered}
[a_n+2m(j-1),\,a_n+2mj],\\
1\le j\le K,
\end{gathered}
\]
lie in this interval, because \(2n-a_n=\lfloor n/2\rfloor\ge2mK+4m+1\). The ratios of Walsh norms at the endpoints of the blocks multiply to
\[
\frac{w_{a_n}(T)}{w_{a_n+2mK}(T)}\le\frac1{c_1}<2^K,
\]
so for one right endpoint \(t\),
\[
\begin{gathered}
w_{t-2m}(T)\le2w_t(T),\qquad t\ge\tfrac32n,\\
w_t(T)\ge c_1w_n(T).
\end{gathered}
\]
Repeat the argument at \(t\ge n_0\). Each application of the growth lemma is a statement about the same \(T\). This gives indices \(n_j\ge(3/2)^jn\) with \(w_{n_j}(T)\ge c_1^jw_n(T)>0\). By Lemma 1.1(3) of [Walsh norms and moment lifts](walsh-norms-and-moment-lifts.md), for this fixed operator,
\[
\begin{aligned}
0<w_n(T)&\le D_Tc_1^{-j}2^{-n_j/2}\\
&\le D_Tc_1^{-j}2^{-(3/2)^jn/2},
\end{aligned}
\]
which tends to \(0\) as \(j\to\infty\): a contradiction. So (1.1) holds, even strictly, for nonzero finite-rank \(T\), and trivially for \(T=0\).

Iterating (1.1) from \(N\) downwards gives (1.2) with \(\rho_N=1\) for \(N<n_0\) and \(\rho_N=2^{-\lfloor(N-n_0)/(2m)\rfloor}\) for \(N\ge n_0\). If finite-rank \(T_j\) converge to \(T\) in operator norm, then \(w_s(T_j)\to w_s(T)\) for every \(s\) by Lemma 1.1(4) there, and \(\|T_j\|\to\|T\|\); both estimates pass to the limit. \(\blacksquare\)

The constant \(D_T\) depends on the rank of \(T\), but it is used only to exclude an infinite sequence of slow decreases for one fixed operator; \(n_0\) and \(\rho_N\) depend only on \(m,D_g,D_f\).

## 2. A compact domain with controlled dual moments

**Lemma 2.1** ([OpenAI-CC, Lemma 5.1]). Let \(m\ge1\), \(\Delta\ge1\), and let \(X\) be a Banach space with \(c_m(X^*)\le\Delta\). For every nonzero finite-dimensional subspace \(E\subseteq X\) there are a Banach space \(G\), an injective compact operator \(J\colon G\to X\) and a contraction \(\iota\colon E\to G\) with
\[
\begin{gathered}
J\iota x=x\ (x\in E),\\
\|J\|\le2,\\
c_m(G^*)\le12\Delta .
\end{gathered} \tag{2.1}
\]

*Proof.* *Finite-dimensional enlargements.* We construct finite-dimensional subspaces \(E=E_0\subseteq E_1\subseteq\cdots\subseteq X\) such that every \(z=(z_i)_{i=1}^m\in\ell_2^m(E_l)\) has a lift \(H\colon\{-1,1\}^m\to E_{l+1}\) with
\[
\begin{gathered}
\mathbb E_\varepsilon\varepsilon_iH(\varepsilon)=z_i,\\
\|H\|_{L_2(E_{l+1})}\le3\Delta\|z\|_{\ell_2^m(E_l)} .
\end{gathered} \tag{2.2}
\]
First, in \(X\): the moment map \(U\colon L_2(\{-1,1\}^m;X)\to\ell_2^m(X)\), \(UH=(\mathbb E_\varepsilon\varepsilon_iH(\varepsilon))_i\), has the bounded right inverse \((z_i)\mapsto\sum_i\varepsilon_iz_i\), and its adjoint satisfies \(\|U^*(\theta_i)\|_{L_2(X^*)}=(\mathbb E\|\sum_i\varepsilon_i\theta_i\|^2)^{1/2}\), which is at least \(\Delta^{-1}\|(\theta_i)\|\). By Lemma 3.1 of [Walsh norms and moment lifts](walsh-norms-and-moment-lifts.md), every unit tuple has a lift of norm at most \(2\Delta\). Given \(E_l\), take a finite \(\eta\)-net of the unit sphere of \(\ell_2^m(E_l)\), with \(0<\eta\le\min(1/2,\Delta/\sqrt m)\) (the sphere is compact), choose such a lift for each net point, and let \(E_{l+1}\) be spanned by \(E_l\) and the finitely many values of these lifts. For a unit tuple \(z\), choose a net point \(v\) with \(\|z-v\|\le\eta\) and add \(\sum_i\varepsilon_i(z_i-v_i)\) to its lift. This corrects the moments exactly, keeps the values in \(E_{l+1}\), and adds at most \(\sqrt m\,\|z-v\|\le\Delta\) to the norm. Scaling, and the zero lift, give (2.2).

*The compact map.* Let \(\mathcal H=(\bigoplus_{l\ge0}E_l)_{\ell_2}\) and \(j(z)=\sum_{l\ge0}2^{-l}z_l\). By the Cauchy–Schwarz inequality the series converges absolutely and \(\|j\|\le(\sum_l4^{-l})^{1/2}<2\); the same estimate on the tails shows that the finite-rank truncations converge to \(j\) in operator norm, so \(j\) is compact (the image of the unit ball is within \(\varepsilon\) of a bounded subset of a finite-dimensional space, for every \(\varepsilon\)). Let \(G=\mathcal H/\ker j\), with quotient map \(Q\), and \(JQ=j\). Then \(G\) is a Banach space, \(J\) is injective, and \(\|J\|\le\|j\|<2\). Every element of the unit ball of \(G\) has a representative of norm less than \(2\), so \(J(B_G)\subseteq j(2B_{\mathcal H})\) is relatively compact, and \(J\) is compact. Put \(\iota(x)=Q(x,0,0,\dots)\); it is a contraction with \(J\iota x=x\).

*Dual moments from a weighted shift.* Since the \(E_l\) are nested, \(R(z_0,z_1,\dots)=(0,2z_0,2z_1,\dots)\) is a bounded map of \(\mathcal H\), and \(jR=j\); hence \(QR=Q\). For \(g_1,\dots,g_m\in G\) choose representatives \(z^i\) with \(Qz^i=g_i\) and \(\|z^i\|\le2\|g_i\|\) (\(z^i=0\) if \(g_i=0\)). Apply (2.2) at each level \(l\) to the tuple \((z^i_l)_i\), obtaining \(H_l\), and put
\[
\widetilde H(\varepsilon)=(0,2H_0(\varepsilon),2H_1(\varepsilon),\dots).
\]
Summing the squared estimates,
\[
\begin{aligned}
\|\widetilde H\|_{L_2(\mathcal H)}&\le6\Delta\Bigl(\sum_i\|z^i\|^2\Bigr)^{1/2}\\
&\le12\Delta\Bigl(\sum_i\|g_i\|^2\Bigr)^{1/2};
\end{aligned}
\]
as every point of the cube has positive mass, \(\widetilde H(\varepsilon)\in\mathcal H\) for every \(\varepsilon\). Its \(i\)-th moment is \(Rz^i\), so \(\mathbb E_\varepsilon\varepsilon_iQ\widetilde H(\varepsilon)=QRz^i=g_i\). For \(\theta_1,\dots,\theta_m\in G^*\),
\[
\begin{aligned}
&\Bigl|\sum_i\theta_i(g_i)\Bigr|\\
&\quad=\Bigl|\mathbb E_\varepsilon\Bigl\langle Q\widetilde H(\varepsilon),\sum_i\varepsilon_i\theta_i\Bigr\rangle\Bigr|\\
&\quad\le12\Delta\Bigl(\sum_i\|g_i\|^2\Bigr)^{1/2}\\
&\qquad\cdot\Bigl\|\sum_i\varepsilon_i\theta_i\Bigr\|_{L_2(G^*)} .
\end{aligned}
\]
The supremum over \(\sum_i\|g_i\|^2\le1\) is \((\sum_i\|\theta_i\|^2)^{1/2}\), so \(c_m(G^*)\le12\Delta\). \(\blacksquare\)

The quotient \(E^*\) of \(X^*\) need not inherit the cotype estimate of \(X^*\); this is why \(E\) is enlarged before the compact map is built.

## 3. Proof of the decay theorem

*Proof of Theorem 2.3 of [Type, cotype and K-convexity](type-cotype-and-k-convexity.md).* Let \(X\) have the approximation property, \(C_q(X)\le C_F\) and \(C_r(X^*)\le C_Y\), with \(q,r\in[2,\infty)\) and \(C_F,C_Y\ge1\). For an integer \(m\) put
\[
\begin{gathered}
D_f=C_Fm^{1/2-1/q},\\
\Delta=C_Ym^{1/2-1/r},\qquad D_g=12\Delta .
\end{gathered}
\]
By (2.2) of [Walsh norms and moment lifts](walsh-norms-and-moment-lifts.md), \(c_m(X)\le D_f\) and \(c_m(X^*)\le\Delta\). The lift parameters (3.1) there satisfy
\[
ma=\frac{m^{1/r}}{576\,C_Y},\qquad mb=\frac{m^{1/q}}{48\,C_F}.
\]
These positive powers of \(m\) eventually exceed every fixed multiple of \((\log m)^3\), so for one fixed large \(m\) the hypotheses of the coefficient lemma hold: \(4\le d=\lceil2\log_2m\rceil<m\) and \(\min(ma,mb)\ge80d(d+1)^2\). Let \(\rho_N\) be given by Theorem 1.1 for \(m,D_g,D_f\). These choices do not depend on any subspace or approximating operator below.

*Decay for the identity.* We show \(w_N(\mathrm{Id}_X)\le2\rho_N\). Let \(x=(x_u)_{u\in V_N}\in L_2(V_N;X)\) be nonzero, and \(E=\operatorname{span}\{x_u\}\). Lemma 2.1 gives \(J\colon G\to X\) and \(\iota\colon E\to G\). The set \(M=\overline{J(B_G)}\) is compact, and the approximation property gives finite-rank \(S_j\colon X\to X\) with \(\sup_{y\in M}\|S_jy-y\|<1/j\); then \(\|S_jJ-J\|\le1/j\). So \(J\) is an operator-norm limit of finite-rank maps; no bound on \(\|S_j\|\) is needed. Since \(c_m(G^*)\le D_g\) and \(c_m(X)\le D_f\), Theorem 1.1 gives \(w_N(J)\le\rho_N\|J\|\le2\rho_N\). The family \(z_u=\iota(x_u)\) has \(\|z\|_{L_2(G)}\le\|x\|_{L_2(X)}\) and \(Jz_u=x_u\), so
\[
\|W^{\mathrm{Id}_X}_Nx\|=\|W^J_Nz\|\le2\rho_N\|x\| .
\]

Since \(\rho_N\to0\), \(w_N(\mathrm{Id}_X)\to0\), and Lemma 4.1 of [Type, cotype and K-convexity](type-cotype-and-k-convexity.md) shows that \(X\) does not contain the spaces \(\ell_1^n\) uniformly. \(\blacksquare\)

With Hypothesis (P) of the first lesson, this proves the converse implication of Theorem 2.1 there, and Corollary 2.2.

## 4. Grothendieck pairs

For normed spaces \(E,F\) and a tensor \(t\in E\otimes F\), the injective and projective norms are
\[
\begin{aligned}
\|t\|_\varepsilon&=\sup|(x^*\otimes y^*)(t)|,\\
\|t\|_\pi&=\inf\Bigl\{\sum_i\|x_i\|\|y_i\|:\\
&\qquad t=\sum_ix_i\otimes y_i\Bigr\},
\end{aligned}
\]
the supremum over \(x^*\in B_{E^*}\) and \(y^*\in B_{F^*}\), with completions \(E\widehat\otimes_\varepsilon F\) and \(E\widehat\otimes_\pi F\). Both have the *metric mapping property*: \(\|(S\otimes T)t\|\le\|S\|\|T\|\|t\|\) for bounded \(S,T\) ([Tensor products of Banach and Hilbert spaces, Jordan homomorphisms and isometries of C\*-algebras](course:tensor-products-of-operator-algebras/tensor-products-of-banach-and-hilbert-spaces-jordan-homomorphisms-and-isometries-of-c-star), Proposition 2.4).

Let \(\mathcal E=(E_n)_{n\ge1}\) be real Banach spaces with \(\dim E_n=n\). Following [GMR, Definition 1.2], \((\mathcal E,F)\) is a *Grothendieck pair* if there is \(C<\infty\) such that, for all \(m,n\) and all \(A\colon E_m\to E_n^*\), the map \(A\otimes\mathrm{Id}_F\) extends to an operator \(E_m\widehat\otimes_\varepsilon F\to E_n^*\widehat\otimes_\pi F\) of norm at most \(C\|A\|\).

**Hypothesis (GMR)** (Gupta–Misra–Ray, [GMR, Theorem 1.3]). If \((\mathcal E,F)\) is a Grothendieck pair, then \(F\) and \(F^*\) have finite cotype.

**Hypothesis (FTJ)** (Figiel–Tomczak-Jaegermann, in the form of [Pis84, Theorem 4]). For an infinite-dimensional \(K\)-convex space \(F\) there is \(D<\infty\) such that for every \(d\) there are \(U_d\colon\ell_2^d\to F\) and \(V_d\colon F\to\ell_2^d\) with \(V_dU_d=\mathrm{Id}\) and \(\|U_d\|\|V_d\|\le D\).

**Corollary 4.1** ([OpenAI-CC, Corollary 6.1]). Assume (P), (GMR) and (FTJ). If \((\mathcal E,F)\) is a Grothendieck pair and \(F\) is infinite-dimensional with the approximation property, then \((\mathcal E,\ell_2)\) is a Grothendieck pair.

*Proof.* By (GMR), \(F\) and \(F^*\) have finite cotype; by Theorem 2.1 of the first lesson (which uses (P)), \(F\) is \(K\)-convex. Take \(U_d,V_d\) from (FTJ). By the metric mapping property and the factorization
\[
\begin{aligned}
A\otimes\mathrm{Id}_{\ell_2^d}=(\mathrm{Id}_{E_n^*}\otimes V_d)&(A\otimes\mathrm{Id}_F)\\
&(\mathrm{Id}_{E_m}\otimes U_d),
\end{aligned}
\]
the corresponding map with \(\ell_2^d\) in place of \(F\) has norm at most \(CD\|A\|\), uniformly in \(d,m,n,A\). Every tensor in \(E_m\otimes\ell_2\) has its second coordinates in a finite-dimensional subspace \(H\subseteq\ell_2\); the inclusion of \(H\) and the orthogonal projection onto \(H\) have norm one, so by the metric mapping property both tensor norms of tensors in \(E_m\otimes H\) agree with those computed in \(E_m\otimes\ell_2\). The estimate for \(\ell_2^d\) therefore holds on \(E_m\otimes\ell_2\) and extends to the completion. \(\blacksquare\)

The corollary gives Pisier's conjecture [GMR, Conjecture 1.4] with the approximation property in place of the bounded approximation property.

## 5. Exercises

**5.1.** In the proof of Theorem 1.1, check that \(2n-\lceil3n/2\rceil=\lfloor n/2\rfloor\) and that \(\lfloor n/2\rfloor\ge2mK+4m+1\) for \(n\ge n_0\).

**5.2.** Show that a norm limit of finite-rank operators between Banach spaces is compact.

**5.3.** Show that \(jR=j\) in Lemma 2.1.

**5.4.** Why does the proof of the decay theorem not need a bound on \(\|S_j\|\)?

**5.5.** Show that for \(t=x\otimes y\), \(\|t\|_\varepsilon=\|t\|_\pi=\|x\|\|y\|\).

## 6. Solutions

**5.1.** \(\lceil3n/2\rceil+\lfloor n/2\rfloor=2n\). For \(n\ge4m(K+2)+2\), \(\lfloor n/2\rfloor\ge2m(K+2)+1\).

**5.2.** If \(\|T-T_j\|<\varepsilon\) with \(T_j\) of finite rank, the image of the unit ball under \(T\) lies within \(\varepsilon\) of the bounded set \(T_j(B)\) in a finite-dimensional space, which is covered by finitely many \(\varepsilon\)-balls; so \(T(B)\) is totally bounded.

**5.3.** \(jR(z)=\sum_{l\ge1}2^{-l}\cdot2z_{l-1}\), which is \(\sum_{l\ge0}2^{-l}z_l=j(z)\).

**5.4.** Only the composites \(S_jJ\) must converge in operator norm; this follows from uniform convergence of \(S_j\) on the compact set \(\overline{J(B_G)}\).

**5.5.** \(\|t\|_\pi\le\|x\|\|y\|\) from the representation \(t=x\otimes y\); \(\|t\|_\varepsilon\ge\|x\|\|y\|\) from norming functionals (Hahn–Banach); and \(\|t\|_\varepsilon\le\|t\|_\pi\) for every tensor.

## References

- [OpenAI-CC] OpenAI, *The cotype–cotype conjecture under the approximation property*, OpenAI Math Release preprint, 23 September 2026, Sections 4.2, 5 and 6. https://github.com/openai/math/tree/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026
- [GMR] R. Gupta, G. Misra and S. K. Ray, *On variants of the Grothendieck inequality and estimates on tensor product norms*, arXiv:2305.13270v2, Definition 1.2, Theorem 1.3, Conjecture 1.4. https://arxiv.org/abs/2305.13270
- [Pis84] G. Pisier, *Finite rank projections on Banach spaces and a conjecture of Grothendieck*, Proceedings of the International Congress of Mathematicians (Warsaw, 1983), Vol. 2, 1027–1039, Theorem 4. https://www.imj-prg.fr/wp-content/uploads/2020/prix/pisier1983.pdf
