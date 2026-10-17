# The bound on a smooth convex domain

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the complete Crouzeix inequality, Theorem A of [The numerical range and the Crouzeix inequality](the-numerical-range-and-the-crouzeix-inequality.md). For a matrix \(A\) whose numerical range lies in a smooth convex domain \(\Omega\), substituting \(A\) into the Faber expansion of [Faber polynomials and a positive kernel](faber-polynomials-and-a-positive-kernel.md) gives the matrix function
\[
\begin{aligned}
R(\lambda)&=q(\lambda)\bigl(h(\lambda)I-A\bigr)^{-1}\\
&=\sum_{k\ge0}b_k(A)\lambda^{-k}
\end{aligned}
\]
on the unit circle, and its Hermitian part \(R+R^*\) is positive semidefinite (Theorem 5.1). Compressing this positive field with the singular vectors of \(F[A]\), and applying the coefficient estimate to the products \(FG\) and \(GF\) in both orders, gives \(\|F[A]\|\le2\) when \(\|F\|\le1\) on \(\partial\Omega\) (Theorem B). Theorem A follows by shrinking the domains of [Smooth convex neighbourhoods](smooth-convex-neighbourhoods.md) to the numerical range. The argument is OpenAI's [OpenAI-DC, Sections 3 and 4]. The field \(R+R^*\) is the double-layer kernel of the numerical range used by Delyon and Delyon [DD] and by Crouzeix and Palencia [CP].

**Setting.** \(\Omega\), \(h\), \(c\), \(\kappa\), \(r_0\), \(q\), \(b_k\) and \(s_{kj}\) are as in [Faber polynomials and a positive kernel](faber-polynomials-and-a-positive-kernel.md), and \(A\in M_n(\mathbf C)\) satisfies \(W(A)\subset\Omega\). For a polynomial \(P(z)=\sum_kB_kz^k\) with \(B_k\in M_m(\mathbf C)\), \(P[A]=\sum_kA^k\otimes B_k\) as in the first lesson. \(\|\cdot\|\) is the operator norm and \(\|\cdot\|_2\) the Hilbert–Schmidt norm, \(d\tau(e^{it})=dt/2\pi\), and for a matrix polynomial \(H\)
\[
\|H\|_\partial^2=\int_{\mathbf T}\|H(h(\mu))\|_2^2\,d\tau(\mu).
\]

## 1. The resolvent

**Theorem 5.1** (OpenAI). For \(|\lambda|\ge1\), \(h(\lambda)I-A\) is invertible. The function \(R(\lambda)=q(\lambda)(h(\lambda)I-A)^{-1}\) satisfies, for \(\lambda\in\mathbf T\),
\[
\begin{aligned}
R(\lambda)&=\sum_{k\ge0}b_k(A)\lambda^{-k},\\
R(\lambda)+R(\lambda)^*&\succeq0,
\end{aligned}
\]
and there are \(C<\infty\) and \(0<\theta<1\) with \(\|b_k(A)\|\le C\theta^k\) for all \(k\). In particular
\[
\int_{\mathbf T}R\,d\tau=I,\qquad\int_{\mathbf T}(R+R^*)\,d\tau=2I.
\]

*Proof.* Every eigenvalue of \(A\) lies in \(W(A)\subset\Omega\), while \(h\) maps \(\{|\lambda|\ge1\}\) into \(\mathbf C\setminus\Omega\) (Theorem 3.7 of [An exterior conformal coordinate](an-exterior-conformal-coordinate.md)). Since \(h\) is injective, at most \(n\) points \(\lambda\) of the collar \(\{|\lambda|>r_0\}\) have \(h(\lambda)\) in the spectrum, all with \(|\lambda|<1\). Choose \(r_A\in(r_0,1)\) larger than their moduli. Then \(\det(h(\lambda)I-A)\ne0\) for \(|\lambda|>r_A\).

In the variable \(u=1/\lambda\), \(h=(c+u\kappa(u))/u\) and \(q=(c-u^2\kappa'(u))/u\), so
\[
R(1/u)=\bigl(c-u^2\kappa'(u)\bigr)D_A(u)^{-1},
\]
where
\[
\begin{aligned}
D_A(u)&=cI+u\bigl(\kappa(u)I-A\bigr)\\
&=cI+(\kappa_0I-A)u\\
&\quad+\sum_{j\ge1}\kappa_ju^{j+1}I.
\end{aligned}
\]
Since \(\det D_A(u)=u^n\det(h(1/u)I-A)\) for \(u\ne0\) and \(\det D_A(0)=c^n\), Cramer's rule shows that \(R(1/u)\) is holomorphic, entry by entry, on \(\{|u|<1/r_A\}\), including \(u=0\), where it equals \(I\). Let \(\sum_kB_ku^k\) be its Taylor expansion. Multiplying out
\[
D_A(u)\sum_{k\ge0}B_ku^k=\bigl(c-u^2\kappa'(u)\bigr)I
\]
and comparing coefficients gives \(B_0=I\) and the recursion of Proposition 4.1 of [Faber polynomials and a positive kernel](faber-polynomials-and-a-positive-kernel.md) with \(z\) replaced by \(A\). So \(B_k=b_k(A)\) by induction.

Choose \(\theta\in(r_A,1)\) and let \(C=\max_{|u|=1/\theta}\|R(1/u)\|\). For unit vectors \(x,y\), the Taylor coefficients of \(x^*R(1/u)y\) are \(x^*b_k(A)y\), and the Cauchy estimates (Theorem 3.3.8 of Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50)) give \(|x^*b_k(A)y|\le C\theta^k\). So \(\|b_k(A)\|\le C\theta^k\), the series converges absolutely and uniformly on \(\mathbf T\), and integrating term by term gives \(\int R\,d\tau=b_0(A)=I\).

For \(\lambda\in\mathbf T\) put \(B=h(\lambda)I-A\), so \(R=qB^{-1}\). Then
\[
B^*(R+R^*)B=qB^*+\bar qB,
\]
and for every unit vector \(v\),
\[
\begin{aligned}
&v^*(qB^*+\bar qB)v=2\operatorname{Re}\bigl(\bar q\,v^*Bv\bigr)\\
&\quad=2\operatorname{Re}\Bigl(\overline{q(\lambda)}\bigl(h(\lambda)-v^*Av\bigr)\Bigr)\ge0
\end{aligned}
\]
by the support inequality, because \(v^*Av\in W(A)\subset\overline\Omega\). As \(B\) is invertible, \(R+R^*\succeq0\). \(\square\)

## 2. The bound on a smooth convex domain

**Theorem B** (OpenAI). Let \(\Omega\) be a smooth convex domain and \(A\in M_n(\mathbf C)\) with \(W(A)\subset\Omega\). For every polynomial \(F\) with coefficients in \(M_m(\mathbf C)\) such that \(\|F(z)\|\le1\) for \(z\in\partial\Omega\),
\[
\|F[A]\|\le2 .
\]

*Proof.* Put \(\gamma=\|F[A]\|\) and suppose \(\gamma>0\). Choose a unit vector \(x\in\mathbf C^n\otimes\mathbf C^m\) with \(\|F[A]x\|=\gamma\) and put \(y=F[A]x/\gamma\). Then \(x\) maximizes \(v\mapsto v^*F[A]^*F[A]v\) on unit vectors, so it is an eigenvector of \(F[A]^*F[A]\) for the eigenvalue \(\gamma^2\), and
\[
F[A]x=\gamma y,\qquad F[A]^*y=\gamma x .
\]
Let \(e_1,\dots,e_m\) be the standard basis of \(\mathbf C^m\), and write \(x=\sum_iXe_i\otimes e_i\) and \(y=\sum_iYe_i\otimes e_i\) with \(n\times m\) matrices \(X,Y\); then \(\|X\|_2=\|Y\|_2=1\). Define \(m\times m\) matrix functions on \(\mathbf T\):
\[
\begin{aligned}
P&=X^*RX,&Q&=Y^*RY,\\
M&=Y^*RX,&L&=X^*RY.
\end{aligned}
\]
Their coefficients of \(\lambda^{-k}\) are \(P_k=X^*b_k(A)X\), and similarly \(Q_k\), \(M_k\), \(L_k\). Since \(b_0(A)=I\), \(P_0=X^*X\) and \(Q_0=Y^*Y\) are Hermitian and \(L_0^*=M_0\). Put
\[
a^2=\sum_{k\ge0}\|M_k\|_2^2 ,
\]
which is finite because \(\|M_k\|_2\le\|Y\|\,\|b_k(A)\|\,\|X\|_2\le C\theta^k\).

*Step 1: pairings.* Let \(G=\sum_{k=0}^Nb_kC_k\) with \(C_k\in M_m(\mathbf C)\). Then \(G[A]=\sum_kb_k(A)\otimes C_k\). With the columns \(x_j=Xe_j\) and \(y_i=Ye_i\), so that \(x=\sum_jx_j\otimes e_j\) and \(y=\sum_iy_i\otimes e_i\),
\[
\begin{aligned}
&(y_i\otimes e_i)^*\bigl(b_k(A)\otimes C_k\bigr)(x_j\otimes e_j)\\
&\quad=\bigl(y_i^*b_k(A)x_j\bigr)\bigl(e_i^*C_ke_j\bigr)\\
&\quad=(M_k)_{ij}(C_k)_{ij},
\end{aligned}
\]
so
\[
\begin{aligned}
y^*G[A]x&=\sum_k\sum_{i,j}(M_k)_{ij}(C_k)_{ij},\\
x^*G[A]x&=\sum_k\sum_{i,j}(P_k)_{ij}(C_k)_{ij},\\
y^*G[A]y&=\sum_k\sum_{i,j}(Q_k)_{ij}(C_k)_{ij}.
\end{aligned}
\]
By the Cauchy–Schwarz inequality,
\[
|y^*G[A]x|\le a\Bigl(\sum_k\|C_k\|_2^2\Bigr)^{1/2}.
\]
For \(G=F\) the left side is \(y^*F[A]x=\gamma>0\), so \(a>0\).

*Step 2: the two ordered tests.* For a polynomial \(G\) with coefficients in \(M_m(\mathbf C)\), \((FG)[A]=F[A]G[A]\) and \((GF)[A]=G[A]F[A]\) (Section 2 of the first lesson), so
\[
\begin{aligned}
y^*(FG)[A]x&=\gamma\,x^*G[A]x,\\
y^*(GF)[A]x&=\gamma\,y^*G[A]y .
\end{aligned}
\]
Expand \(FG=\sum_kb_kU_k\) and \(GF=\sum_kb_kV_k\) (Proposition 4.1). On \(\partial\Omega=h(\mathbf T)\), \(\|F(z)G(z)\|_2\le\|F(z)\|\,\|G(z)\|_2\), which is at most \(\|G(z)\|_2\). With Step 1 and the lower inequality of the coefficient estimate (Proposition 4.6), this gives
\[
\begin{aligned}
\gamma|x^*G[A]x|&\le a\Bigl(\sum_k\|U_k\|_2^2\Bigr)^{1/2}\\
&\le a\|FG\|_\partial\le a\|G\|_\partial,
\end{aligned}
\]
and in the same way, with \(\|G(z)F(z)\|_2\le\|G(z)\|_2\|F(z)\|\), \(\gamma|y^*G[A]y|\le a\|G\|_\partial\). For \(G=\sum_kb_kC_k\) put
\[
\mathcal N(G)^2=\|C_0\|_2^2+2\sum_{k\ge1}\|C_k\|_2^2 .
\]
The upper inequality of Proposition 4.6 gives
\[
\max\bigl(|x^*G[A]x|,|y^*G[A]y|\bigr)\le\frac a\gamma\,\mathcal N(G).
\]

*Step 3: weighted bounds for \(P\) and \(Q\).* For \(N\ge1\) put \(d_N=\|P_0\|_2^2+\frac12\sum_{k=1}^N\|P_k\|_2^2\), and test Step 2 with \(C_0=\overline{P_0}\), \(C_k=\overline{P_k}/2\) for \(1\le k\le N\) (entrywise conjugates) and \(C_k=0\) otherwise. By Step 1, \(x^*G[A]x=d_N\), and \(\mathcal N(G)^2=\|C_0\|_2^2+2\sum_k\|C_k\|_2^2=d_N\). So \(d_N\le(a/\gamma)\sqrt{d_N}\), that is \(d_N\le a^2/\gamma^2\). Letting \(N\to\infty\), and arguing in the same way with \(Q\),
\[
\begin{aligned}
\|P_0\|_2^2+\tfrac12\sum_{k\ge1}\|P_k\|_2^2&\le a^2/\gamma^2,\\
\|Q_0\|_2^2+\tfrac12\sum_{k\ge1}\|Q_k\|_2^2&\le a^2/\gamma^2.
\end{aligned}
\]

*Step 4: boundary norms.* On \(\mathbf T\), \(P^*=\sum_kP_k^*\lambda^k\), so \(P+P^*\) has constant term \(2P_0\) and the coefficients \(P_k\), \(P_k^*\) at \(\lambda^{-k}\), \(\lambda^k\) for \(k\ge1\). Parseval's identity (Lemma 4.5) and Step 3 give
\[
\begin{aligned}
&\int_{\mathbf T}\|P+P^*\|_2^2\,d\tau\\
&\quad=4\|P_0\|_2^2+2\sum_{k\ge1}\|P_k\|_2^2\le\frac{4a^2}{\gamma^2},
\end{aligned}
\]
and the same bound for \(Q+Q^*\). The function \(M+L^*\) has constant term \(M_0+L_0^*=2M_0\) and the coefficients \(M_k\), \(L_k^*\) at \(\lambda^{-k}\), \(\lambda^k\), so
\[
\begin{aligned}
&\int_{\mathbf T}\|M+L^*\|_2^2\,d\tau\\
&\quad=4\|M_0\|_2^2+\sum_{k\ge1}\bigl(\|M_k\|_2^2+\|L_k\|_2^2\bigr)\\
&\quad\ge a^2 .
\end{aligned}
\]

*Step 5: a positive block matrix.* By Theorem 5.1, the \(2m\times2m\) matrix
\[
\begin{aligned}
\Delta&=\begin{pmatrix}X&Y\end{pmatrix}^*(R+R^*)\begin{pmatrix}X&Y\end{pmatrix}\\
&=\begin{pmatrix}P+P^*&L+M^*\\M+L^*&Q+Q^*\end{pmatrix}
\end{aligned}
\]
is positive semidefinite at every point of \(\mathbf T\), and so is \(J\Delta J\) for \(J=\operatorname{diag}(I_m,-I_m)\). Hence
\[
0\le\operatorname{tr}\bigl(\Delta^{1/2}J\Delta J\Delta^{1/2}\bigr)=\operatorname{tr}(\Delta J\Delta J).
\]
For a Hermitian block matrix with diagonal blocks \(D_1,D_2\) and lower block \(E\), \(\operatorname{tr}(\Delta J\Delta J)=\operatorname{tr}D_1^2+\operatorname{tr}D_2^2-2\operatorname{tr}(E^*E)\). So, pointwise on \(\mathbf T\),
\[
\begin{aligned}
2\|M+L^*\|_2^2&\le\|P+P^*\|_2^2\\
&\quad+\|Q+Q^*\|_2^2 .
\end{aligned}
\]
Integrating and using Step 4,
\[
2a^2\le\frac{8a^2}{\gamma^2}.
\]
Since \(a>0\), \(\gamma\le2\). \(\square\)

The proof uses the two products \(FG\) and \(GF\) and never commutes coefficients of \(F\) and \(G\); this is why the bound holds for matrix coefficients of every size \(m\). Convexity of \(\Omega\) enters twice, both times through the support inequality: in the positivity of the kernel behind Proposition 4.6, and in \(R+R^*\succeq0\).

## 3. Proof of Theorem A

Let \(A\in M_n(\mathbf C)\) and let \(P\) be a polynomial with coefficients in \(M_m(\mathbf C)\). The numerical range \(K=W(A)\) is compact and convex (Section 1 of the first lesson). For \(0<\delta<1\), the domain \(\Omega_\delta\) of [Smooth convex neighbourhoods](smooth-convex-neighbourhoods.md) is a smooth convex domain containing \(K\) (Lemma 2.1 and Proposition 2.3 there). If \(P\) vanishes on the infinite set \(\partial\Omega_\delta\), every entry of \(P\) is the zero polynomial and there is nothing to prove. Otherwise Theorem B, applied to \(P\) divided by \(\max_{\partial\Omega_\delta}\|P\|\), gives
\[
\|P[A]\|\le2\max_{\partial\Omega_\delta}\|P\|\le2\max_{\overline\Omega_\delta}\|P\|.
\]
All the sets \(\overline\Omega_\delta\) lie in one rectangle \(Q\) (Lemma 2.1(1)), on which \(z\mapsto\|P(z)\|\) is uniformly continuous, with modulus of continuity \(\omega\). Every point of \(\overline\Omega_\delta\) has distance at most \(\varepsilon_\delta=\delta(1+\operatorname{diam}K)/(1-\delta)\) from \(K\) (Lemma 2.1(4)), so
\[
\max_{\overline\Omega_\delta}\|P\|\le\max_K\|P\|+\omega(\varepsilon_\delta),
\]
and \(\omega(\varepsilon_\delta)\to0\) as \(\delta\to0\). Hence \(\|P[A]\|\le2\max_{W(A)}\|P\|\). The example of Section 3 of the first lesson shows that the constant \(2\) cannot be lowered. \(\square\)

## 4. Exercises

**5.1** (easy). Show that the hypothesis \(W(A)\subset\Omega\) in Theorem B cannot be replaced by the condition that the spectrum of \(A\) lies in \(\Omega\).

**5.2** (easy). Show that \(\|b_k(A)\|\le2\) for every \(k\ge1\) when \(W(A)\subset\Omega\). (This bound is due to Beckermann; see [BC].)

**5.3** (medium). For scalar coefficients \(c_0,\dots,c_N\), put \(G=\sum_kc_kb_k\) and \(g(\lambda)=\sum_kc_k\lambda^k\). Show that \(G(A)=\int_{\mathbf T}(R+R^*)g\,d\tau-c_0I\), and deduce \(\|G(A)+c_0I\|\le2\max_{\mathbf T}|g|\).

**5.4** (medium). For the ellipse \(h(\lambda)=\lambda+a/\lambda\) with \(0<a<1\) and \(A=0\in M_1(\mathbf C)\), compute \(R(\lambda)\), check \(R+R^*\ge0\) on \(\mathbf T\) directly, and deduce \(b_{2j}(0)=2(-a)^j\) and \(b_{2j+1}(0)=0\) for \(j\ge1\).

## 5. Solutions

**5.1.** For \(t>2\), \(A=\bigl(\begin{smallmatrix}0&t\\0&0\end{smallmatrix}\bigr)\) has spectrum \(\{0\}\subset\mathbf D\), and \(F(z)=z\) satisfies \(|F|=1\) on \(\partial\mathbf D\), but \(\|F[A]\|=t>2\). (Its numerical range is the disc of radius \(t/2>1\), Exercise 1.1 of the first lesson.)

**5.2.** For \(k\ge1\), \(\int_{\mathbf T}R\lambda^kd\tau=b_k(A)\) and \(\int_{\mathbf T}R^*\lambda^kd\tau=\sum_jb_j(A)^*\int\lambda^{j+k}d\tau=0\), so \(b_k(A)=\int(R+R^*)\lambda^kd\tau\). For unit vectors \(x,y\) put \(f_x=x^*(R+R^*)x\) and \(f_y=y^*(R+R^*)y\); these are nonnegative functions on \(\mathbf T\) with integral \(2\), because \(\int(R+R^*)\,d\tau=2I\). The Cauchy–Schwarz inequality for the positive semidefinite form \(R+R^*\) gives
\[
|y^*b_k(A)x|\le\int_{\mathbf T}f_y^{1/2}f_x^{1/2}\,d\tau,
\]
and by the Cauchy–Schwarz inequality for the integral, the right side is at most \((\int f_y\,d\tau)^{1/2}(\int f_x\,d\tau)^{1/2}=2\).

**5.3.** As in 5.2, \(\int R\lambda^kd\tau=b_k(A)\) for \(k\ge0\), \(\int R^*\lambda^kd\tau=0\) for \(k\ge1\) and \(\int R^*d\tau=I\). So \(\int(R+R^*)g\,d\tau=G(A)+c_0I\). For unit \(x,y\), with \(f_x\) and \(f_y\) as in 5.2,
\[
\begin{aligned}
&|y^*(G(A)+c_0I)x|\\
&\quad\le\max_{\mathbf T}|g|\int_{\mathbf T}f_y^{1/2}f_x^{1/2}\,d\tau\le2\max_{\mathbf T}|g| .
\end{aligned}
\]

**5.4.** Here \(0\in\Omega\), \(W(A)=\{0\}\), and
\[
R(\lambda)=\frac{q(\lambda)}{h(\lambda)}=\frac{\lambda-a/\lambda}{\lambda+a/\lambda}=\frac{\lambda^2-a}{\lambda^2+a}.
\]
With \(w=\lambda^2\in\mathbf T\),
\[
\begin{aligned}
\operatorname{Re}\frac{w-a}{w+a}&=\frac{\operatorname{Re}\bigl((w-a)(\bar w+a)\bigr)}{|w+a|^2}\\
&=\frac{1-a^2}{|w+a|^2}>0 .
\end{aligned}
\]
Expanding in \(\lambda^{-1}\),
\[
\frac{1-a\lambda^{-2}}{1+a\lambda^{-2}}=1+2\sum_{j\ge1}(-a)^j\lambda^{-2j},
\]
and the coefficients are \(b_k(0)\) by Theorem 5.1. For example \(b_2(0)=-2a\), in agreement with \(b_2(z)=z^2-2a\).

## References

- [OpenAI-DC] OpenAI, *A direct proof of the complete Crouzeix inequality*, OpenAI Math Release preprint, 26 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
- [DD] B. Delyon and F. Delyon, *Generalization of von Neumann's spectral sets and integral representation of operators*, Bulletin de la Société Mathématique de France 127 (1999), 25–41. https://www.numdam.org/item/?id=BSMF_1999__127_1_25_0
- [CP] M. Crouzeix and C. Palencia, *The numerical range is a \((1+\sqrt2)\)-spectral set*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 649–655; arXiv:1702.00668. https://arxiv.org/abs/1702.00668
- [BC] B. Beckermann and M. Crouzeix, *Faber polynomials of matrices for non-convex sets*, Jaen Journal on Approximation 6 (2014), 219–231; arXiv:1310.1356. https://arxiv.org/abs/1310.1356
