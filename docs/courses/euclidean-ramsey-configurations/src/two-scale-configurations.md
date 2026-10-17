# Two-scale configurations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The weights of [A finite lattice identity](a-finite-lattice-identity.md) split into a positive and a negative part with the same evaluation values at every point of the set. Read as two lists of affine functions, they give two configurations whose corresponding points have the same coordinates in different orders. Their gradient Gram matrices differ by the identity, but the negative one is not yet small. This lesson makes it as small as desired, while keeping every cancellation exact: the weights are smoothed by a Gaussian average, discretized on a fine lattice, and finally made rational. The result is the following pair of configurations, at scales one and \(q\), with \(q>0\) as small as desired.

**Theorem 3.1** (two-scale configurations). Assume the tensor condition for \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\), with \(s\ge2\) and affine span \(\mathbb R^d\). For every \(\eta>0\) there are an integer \(\ell\ge1\) and vectors \(f_i,g_i\in\mathbb R^\ell\) such that, with \(q=\eta/(1+\eta)\),
\[
\begin{gathered}
\|f_i-f_j\|^2=\|a_i-a_j\|^2,\\
\|g_i-g_j\|^2=q\|a_i-a_j\|^2
\end{gathered}
\]
for all \(i,j\), and each \(g_i\) is obtained from \(f_i\) by permuting its coordinates.

So \((f_i)\) is a congruent copy of \(A\), \((g_i)\) is a copy of \(A\) scaled by \(\sqrt q\), and the coordinates of corresponding points agree as multisets. The proof is in Section 3. The notation of the previous lesson is kept: the basis \(w_1,\dots,w_k\), the rational symmetric matrix \(C\) with \(UCU^{\mathsf T}=I_d\), the lattice \(\Gamma=\mathbb Z^k\), the evaluation lattices \(\Lambda_i\), and the weights \(\nu\) of its Lemma 2.1.

For a real symmetric \(k\times k\) matrix \(C\) write
\[
D_C=\frac12\sum_{j,l=1}^kC_{jl}\,\partial_j\partial_l,
\]
and for a real number \(r\) let \(r_+=\max\{r,0\}\) and \(r_-=\max\{-r,0\}\). The map \(r\mapsto r_-\) is \(1\)-Lipschitz.

## 1. A smooth function with small negative curvature

*Integrals over \(\mathbb R^k\).* All integrals in this lesson are Riemann integrals of continuous functions. If \(f\) is continuous on \(\mathbb R^k\) and \(|f(x)|\le p(\|x\|)e^{-c\|x\|^2}\) for a polynomial \(p\) and some \(c>0\), put
\[
\int_{\mathbb R^k}f=\lim_{R\to\infty}\int_{[-R,R]^k}f ;
\]
the limit exists, because the integral of \(|f|\) over \([-R',R']^k\setminus[-R,R]^k\) tends to zero as \(R'>R\to\infty\). For such functions, Fubini's theorem and the linear change of variables, for \(\det M\ne0\),
\[
\begin{aligned}
&\int_{\mathbb R^k}f(x)\,dx\\
&\quad=|\det M|\int_{\mathbb R^k}f(My)\,dy ,
\end{aligned}
\]
follow from their versions for cubes and their images, Theorems 10.2.2 and 10.7.2 of [Lebl]: the image of a large cube under \(M\) contains a cube and lies in another, both of comparable size, and the integrals over the differences tend to zero. Derivatives of \(\int_0^1g(x,t)\,dt\) with respect to \(x\) may be taken under the integral sign when the partial derivatives of \(g\) are continuous [Lebl, Theorem 9.1.1]. For a continuous \(f\) with compact support, the lattice sums \(n^{-k}\sum_{\lambda\in\mathbb Z^k}f(\lambda/n)\) tend to \(\int f\): they lie between the lower and the upper Darboux sums of \(f\) for the cubes of side \(1/n\), and the difference of these sums tends to zero by uniform continuity, as in the proof of [Lebl, Theorem 10.1.15].

**Lemma 1.1.** Let \(C\) be a real symmetric \(k\times k\) matrix and \(U\) a real \(d\times k\) matrix with \(UCU^{\mathsf T}=I_d\). For every \(\eta>0\) there is a nonnegative smooth function \(b\) on \(\mathbb R^k\) with compact support such that \(\int b>0\) and
\[
\int_{\mathbb R^k}(D_Cb)_-(x)\,\|Ux\|^2\,dx<\eta\int_{\mathbb R^k}b .
\]

*Proof.* *Two covariance matrices.* Since \(UCU^{\mathsf T}=I_d\), \(U\) has rank \(d\). Let \(H\) be the image of \(U^{\mathsf T}\) and \(V=\ker U\), so \(\mathbb R^k=H\oplus V\) orthogonally, with orthogonal projections \(P_H,P_V\). The quadratic form of \(C\) is positive definite on \(H\): for \(h=U^{\mathsf T}y\ne0\), \(h^{\mathsf T}Ch=y^{\mathsf T}UCU^{\mathsf T}y=\|y\|^2>0\). Choose \(\epsilon>0\) with \(\epsilon\,\mathrm{tr}(UU^{\mathsf T})<\eta/8\), and put \(S=\epsilon P_H+LP_V\) with \(L>0\) to be chosen. In orthonormal coordinates adapted to \(H\oplus V\),
\[
\begin{gathered}
S+C=\begin{pmatrix}A_0&B_0\\B_0^{\mathsf T}&C_{VV}+LI\end{pmatrix},\\
A_0=C_{HH}+\epsilon I ,
\end{gathered}
\]
where \(A_0\) is positive definite. For \(L\) large, the Schur complement \(C_{VV}+LI-B_0^{\mathsf T}A_0^{-1}B_0\) is positive definite, and then so is \(S+C\); if \(V=0\) there is nothing to choose. The matrix \(S\) is positive definite, and since \(UP_V=0\) and \(UP_H=U\),
\[
\mathrm{tr}(USU^{\mathsf T})=\epsilon\,\mathrm{tr}(UU^{\mathsf T})<\frac\eta8 .
\]
For \(0\le t\le1\) the matrix \(Q_t=S+tC=(1-t)S+t(S+C)\) is positive definite, and its eigenvalues lie in a fixed compact subinterval of \((0,\infty)\).

*Gaussian densities.* Let \(\omega=\int_{\mathbb R}e^{-t^2/2}\,dt>0\); its value \(\sqrt{2\pi}\) is not needed. For positive definite \(Q\) let
\[
\phi_Q(x)=\frac{\exp(-\frac12x^{\mathsf T}Q^{-1}x)}{\omega^k(\det Q)^{1/2}} .
\]
Write \(Q=MM^{\mathsf T}\) with \(M\) invertible, for instance \(M=O\Delta^{1/2}\) if \(Q=O\Delta O^{\mathsf T}\) with \(O\) orthogonal and \(\Delta\) diagonal. The substitution \(x=My\) has \(x^{\mathsf T}Q^{-1}x=\|y\|^2\) and \(|\det M|=(\det Q)^{1/2}\), so for continuous \(g\) of polynomial growth
\[
\begin{aligned}
&\int\phi_Q(x)g(x)\,dx\\
&\quad=\omega^{-k}\int e^{-\|y\|^2/2}g(My)\,dy .
\end{aligned}
\]
With Fubini's theorem, \(\int te^{-t^2/2}dt=0\) and \(\int t^2e^{-t^2/2}dt=\omega\) (integration by parts), this gives
\[
\begin{gathered}
\int\phi_Q=1,\\
\int\phi_Q(x)\,xx^{\mathsf T}dx=MM^{\mathsf T}=Q .
\end{gathered}
\]
Differentiation gives
\[
\begin{aligned}
\partial_j\partial_l\phi_Q={}&\bigl((Q^{-1}x)_j(Q^{-1}x)_l\\
&-(Q^{-1})_{jl}\bigr)\phi_Q ,
\end{aligned}
\]
and, using \(\frac d{dt}\log\det Q_t=\mathrm{tr}(Q_t^{-1}C)\) and \(\frac d{dt}Q_t^{-1}=-Q_t^{-1}CQ_t^{-1}\),
\[
\begin{aligned}
\frac d{dt}\phi_{Q_t}&=\frac12\bigl(x^{\mathsf T}Q_t^{-1}CQ_t^{-1}x\\
&\qquad-\mathrm{tr}(Q_t^{-1}C)\bigr)\phi_{Q_t}\\
&=D_C\phi_{Q_t}.
\end{aligned}
\]
No positivity of \(C\) is needed here. Put
\[
b_*(x)=\int_0^1\phi_{Q_t}(x)\,dt .
\]
The densities \(\phi_{Q_t}\) and all their derivatives are bounded by a polynomial times \(e^{-c\|x\|^2}\), with \(c>0\) and the polynomial independent of \(t\). So \(b_*\) is a nonnegative smooth function, of integral one by Fubini's theorem, whose derivatives decay faster than any power, and differentiation under the integral gives
\[
D_Cb_*=\int_0^1\frac d{dt}\phi_{Q_t}\,dt=\phi_{S+C}-\phi_S .
\]
Since both densities are nonnegative, \((\phi_{S+C}-\phi_S)_-\le\phi_S\). Since \(\|Ux\|^2=\mathrm{tr}(Uxx^{\mathsf T}U^{\mathsf T})\), the second moments give \(\int\phi_S(x)\|Ux\|^2dx=\mathrm{tr}(USU^{\mathsf T})\). Hence
\[
\begin{aligned}
&\int(D_Cb_*)_-(x)\|Ux\|^2dx\\
&\quad\le\mathrm{tr}(USU^{\mathsf T})<\frac\eta8 .
\end{aligned}
\]

*Compact support.* Let \(\chi\) be smooth with \(0\le\chi\le1\), equal to one on the unit ball and zero outside the ball of radius two, put \(\chi_R(x)=\chi(x/R)\) and \(b_R=\chi_Rb_*\). Then \(\int b_R\to1\) as \(R\to\infty\). Since \(C\) is symmetric,
\[
\begin{aligned}
D_Cb_R={}&\chi_RD_Cb_*+\sum_{j,l}C_{jl}(\partial_j\chi_R)(\partial_lb_*)\\
&+b_*D_C\chi_R .
\end{aligned}
\]
The derivatives of \(\chi_R\) are bounded by constants times \(R^{-1}\) and \(R^{-2}\) and vanish outside \(R\le\|x\|\le2R\). By the rapid decay of \(b_*\) and its derivatives,
\[
\int|D_Cb_R-D_Cb_*|(x)\,\|Ux\|^2dx\to0 .
\]
Since \(r\mapsto r_-\) is \(1\)-Lipschitz, the integrals of \((D_Cb_R)_-\|Ux\|^2\) converge to that of \((D_Cb_*)_-\|Ux\|^2\). Choose \(R\) with \(\int b_R>\frac12\) and with the difference of the two integrals below \(\eta/8\). Then
\[
\int(D_Cb_R)_-\|Ux\|^2<\frac\eta4<\eta\int b_R ,
\]
and \(b=b_R\) has the required properties. \(\square\)

## 2. Rational weights at a fine scale

For finitely supported functions \(\nu,d\) on \(\Gamma\), the convolution is \((\nu*d)(\lambda)=\sum_\gamma\nu(\gamma)d(\lambda-\gamma)\).

**Lemma 2.1.** Let \(\nu:\Gamma\to\mathbb Q\) be finitely supported with zero pushforward to every \(\Gamma/\Lambda_i\), with \(\sum\nu(\gamma)=0\), \(\sum\nu(\gamma)\gamma=0\) and \(\sum\nu(\gamma)\gamma\gamma^{\mathsf T}=C\), and let \(UCU^{\mathsf T}=I_d\). For every \(\eta>0\) there are an integer \(n\ge1\), a finitely supported \(\mu:\Gamma\to\mathbb Q\) with zero pushforward to every \(\Gamma/\Lambda_i\), and a rational \(\zeta>0\) such that
\[
\begin{gathered}
\sum_\lambda\mu(\lambda)\frac\lambda n\frac{\lambda^{\mathsf T}}n=\zeta C,\\
\sum_\lambda\mu(\lambda)_-\Bigl\|U\frac\lambda n\Bigr\|^2<\eta\zeta .
\end{gathered}
\]

*Proof.* *Convolution keeps the cancellations.* For any finitely supported real \(d\), the pushforward of \(\nu*d\) to \(\Gamma/\Lambda_i\) is zero: summing \((\nu*d)(\lambda)\) over a coset \(q\) gives \(\sum_\gamma\nu(\gamma)\sum_{\beta\in q-\gamma}d(\beta)\), the inner sum depends only on the coset of \(\gamma\), and the sum of \(\nu\) over each coset vanishes. Substituting \(\lambda=\beta+\gamma\), the zeroth and first moments of \(\nu\) give
\[
\begin{gathered}
\sum_\lambda(\nu*d)(\lambda)=0,\\
\sum_\lambda(\nu*d)(\lambda)\lambda\lambda^{\mathsf T}=\Bigl(\sum_\beta d(\beta)\Bigr)C,
\end{gathered}
\]
because the terms with \(\beta\beta^{\mathsf T}\), \(\beta\gamma^{\mathsf T}\) and \(\gamma\beta^{\mathsf T}\) vanish after summing over \(\gamma\).

*A discretized smooth function.* Take \(b\) from Lemma 1.1 and, for \(n\ge1\), put
\[
\begin{gathered}
d_n(\lambda)=n^{2-k}b(\lambda/n),\qquad\mu_n=\nu*d_n,\\
\zeta_n=n^{-2}\sum_\lambda d_n(\lambda).
\end{gathered}
\]
Then \(\zeta_n=n^{-k}\sum_\lambda b(\lambda/n)\to\int b>0\), a Riemann sum, and the identity above gives exactly \(\sum_\lambda\mu_n(\lambda)\frac\lambda n\frac{\lambda^{\mathsf T}}n=\zeta_nC\).

*Taylor expansion.* For \(x=\lambda/n\),
\[
n^k\mu_n(\lambda)=n^2\sum_\gamma\nu(\gamma)\,b\Bigl(x-\frac\gamma n\Bigr).
\]
Expand \(\tau\mapsto b(x-\tau\gamma/n)\) on \([0,1]\) to second order by Taylor's theorem [Lebl, Theorem 4.3.2]; the remainder is bounded by \(\|\gamma/n\|^3\) times a constant that depends only on the third derivatives of \(b\). The zeroth and first moments of \(\nu\) remove the constant and linear terms, and the second moment gives \(D_Cb(x)\), so
\[
n^k\mu_n(\lambda)=D_Cb(\lambda/n)+O(n^{-1}),
\]
uniformly in \(\lambda\), since \(\sum_\gamma|\nu(\gamma)|\|\gamma\|^3\) is finite. For \(n\ge1\), both \(\mu_n(\lambda)\) and \(D_Cb(\lambda/n)\) vanish unless \(\lambda/n\) lies in a fixed ball, which contains \(O(n^k)\) points of \(\frac1n\Gamma\) and on which \(\|Ux\|^2\) is bounded. By the Lipschitz property of \(r\mapsto r_-\),
\[
\begin{aligned}
&\Bigl|\sum_\lambda\mu_n(\lambda)_-\Bigl\|U\frac\lambda n\Bigr\|^2\\
&\quad-n^{-k}\sum_\lambda\bigl(D_Cb(\lambda/n)\bigr)_-\Bigl\|U\frac\lambda n\Bigr\|^2\Bigr|\\
&\quad=O(n^{-1}).
\end{aligned}
\]
The second sum is a Riemann sum of a continuous function with compact support, so
\[
\begin{aligned}
&\sum_\lambda\mu_n(\lambda)_-\Bigl\|U\frac\lambda n\Bigr\|^2\\
&\quad\to\int(D_Cb)_-\|Ux\|^2<\eta\int b .
\end{aligned}
\]
Fix \(n\) so large that \(\zeta_n>0\) and \(\sum\mu_n(\lambda)_-\|U\lambda/n\|^2<\eta\zeta_n\).

*Rational coefficients.* Let \(E\subset\Gamma\) be a finite set containing the support of \(d_n\). On the space \(\mathbb R^E\) of functions \(d\) supported in \(E\), the maps \(d\mapsto\nu*d\) and \(d\mapsto\zeta(d)=n^{-2}\sum d\) are linear, and \(d\mapsto\sum_\lambda(\nu*d)(\lambda)_-\|U\lambda/n\|^2\) is continuous; the sum runs over the finite set \(\mathrm{supp}\,\nu+E\). The two strict inequalities hold at \(d_n\), hence on a neighbourhood of \(d_n\). Choose a rational \(d\) in it and put \(\mu=\nu*d\) and \(\zeta=\zeta(d)\). They are rational, \(\mu\) has zero pushforwards, and the identity of the first paragraph gives the exact second moment. \(\square\)

## 3. Proof of Theorem 3.1

Take \(\nu\) from Lemma 2.1 of the previous lesson and \(n,\mu,\zeta\) from Lemma 2.1 above. Choose a positive integer \(M\) with \(M\mu(\lambda)\in\mathbb Z\) for every \(\lambda\). Form two finite lists of affine functions in \(W\): the *positive list* contains \(M\mu(\lambda)_+\) copies of \(w(\lambda/n)\), and the *negative list* \(M\mu(\lambda)_-\) copies, for every \(\lambda\). The total weight of \(\mu\) is zero, so the lists have the same length.

*Equal values.* Fix \(i\) and a real number \(x\). The \(\lambda\) with \(e_i(w(\lambda/n))=x\) form a coset of \(\Lambda_i\) or the empty set, because \(e_i(w(\lambda/n))=e_i(w(\lambda))/n\). The pushforward of \(\mu\) to \(\Gamma/\Lambda_i\) is zero, so the positive and the negative parts of \(\mu\) have equal sums on this set. Hence the value \(x\) occurs equally often among the evaluations at \(a_i\) of the two lists.

*Gram matrices.* Divide every function in both lists by \(\sqrt{\zeta M}\). The function \(w(\lambda/n)\) has gradient \(U\lambda/n\), so the gradient Gram matrices of the two lists are
\[
B_\pm=\frac1\zeta\sum_\lambda\mu(\lambda)_\pm\Bigl(U\frac\lambda n\Bigr)\Bigl(U\frac\lambda n\Bigr)^{\mathsf T}.
\]
By Lemma 2.1, \(B_+-B_-=\frac1\zeta U(\zeta C)U^{\mathsf T}=I_d\) and \(\mathrm{tr}\,B_-<\eta\). The matrix \(B_-\) is positive semidefinite, so its eigenvalues are at most its trace, and \(P=\eta I_d-B_-\) is positive semidefinite. Choose vectors \(\rho_1,\dots,\rho_d\) with \(\sum_j\rho_j\rho_j^{\mathsf T}=P\), for example the columns of \(P^{1/2}\), and append the same functions \((0,\rho_j)\) to both lists. The Gram matrices become \((1+\eta)I_d\) and \(\eta I_d\), and the appended functions add the same values to both lists. Finally divide every function in both lists by \(\sqrt{1+\eta}\); the Gram matrices become \(I_d\) and \(qI_d\).

*The vectors.* Let \(f_i\) be the vector of values at \(a_i\) of the functions of the positive list, and \(g_i\) that of the negative list, each list in a fixed order. By the second paragraph, \(g_i\) is a permutation of the coordinates of \(f_i\). For an affine function \((v,u)\), the difference of its values at \(a_i\) and \(a_j\) is \((a_i-a_j)\cdot u\). Summing the squares over a list with gradient Gram matrix \(I_d\), respectively \(qI_d\), gives
\[
\begin{gathered}
\|f_i-f_j\|^2=\|a_i-a_j\|^2,\\
\|g_i-g_j\|^2=q\|a_i-a_j\|^2 .\qquad\square
\end{gathered}
\]

## 4. Exercises

**4.1** (easy). For \(k=1\) and \(Q_t=s+tc\), check directly that \(\frac d{dt}\phi_{Q_t}=\frac c2\phi_{Q_t}''\).

**4.2** (easy). Show that \((a-b)_-\le b\) for real \(a,b\ge0\), and that \(|r_--r'_-|\le|r-r'|\).

**4.3** (medium). In the proof of Theorem 3.1, why is it essential that the functions \((0,\rho_j)\) are appended to both lists, rather than only to the positive one?

**4.4** (medium). Show that in Theorem 3.1 the vectors \(f_i\) cannot all be equal to the vectors \(g_i\) after a permutation that does not depend on \(i\), unless \(q=1\).

## 5. Solutions

**4.1.** With \(Q=s+tc\) and \(\omega\) as in Section 1, \(\phi=\omega^{-1}Q^{-1/2}e^{-x^2/(2Q)}\), so \(\partial_Q\phi=\bigl(-\frac1{2Q}+\frac{x^2}{2Q^2}\bigr)\phi\) and \(\phi''=\bigl(\frac{x^2}{Q^2}-\frac1Q\bigr)\phi\). Hence \(\frac d{dt}\phi=c\,\partial_Q\phi=\frac c2\phi''\).

**4.2.** If \(a\ge b\), the left side is zero. Otherwise it is \(b-a\le b\). The map \(r\mapsto r_-=\max\{-r,0\}\) is a maximum of two \(1\)-Lipschitz functions.

**4.3.** The permutation property compares the two lists value by value at each point. Functions appended to only one list would add values at \(a_i\) that have no partner in the other list, and the coordinate multisets of \(f_i\) and \(g_i\) would differ.

**4.4.** If \(g_i=\pi f_i\) for one coordinate permutation \(\pi\) and every \(i\), then \(\|g_i-g_j\|=\|\pi(f_i-f_j)\|=\|f_i-f_j\|\), so \(q\|a_i-a_j\|^2=\|a_i-a_j\|^2\) for \(i\ne j\), which forces \(q=1\). The permutations in the lemma depend on \(i\), and that is what makes two different scales possible.

## References

- [Lebl] J. Lebl, *Basic Analysis I & II*, version 6.3, Theorem 4.3.2 (Taylor's theorem), Theorem 9.1.1 (Leibniz integral rule), Theorem 10.1.15, Theorem 10.2.2 (Fubini) and Theorem 10.7.2 (change of variables); the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/html/sec_taylor.html#thm_taylor, https://www.jirka.org/ra/html/sec_diffunderint.html#sec_diffunderint-6, https://www.jirka.org/ra/html/sec_mvchangeofvars.html#sec_mvchangeofvars-8
- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
