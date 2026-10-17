# A matrix energy and a trace inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the two finite-dimensional facts behind Theorem A of [Dyadic triangles and the main estimate](dyadic-triangles-and-the-main-estimate.md). The first concerns the energy \(\Phi(P)=\operatorname{tr}(P^{3/2})\) of a positive semidefinite matrix: its second derivative \(b_P\) decreases by at most the factor \(a^{-1/2}\) when \(P\) is replaced by a matrix at most \(a\) times as large (Lemma 2.3), and this gives a midpoint gap (Corollary 2.4). The second is a bound for the trace of a cyclic product of three matrices and three symmetric contractions by these second derivatives, with a constant independent of the dimensions (Proposition 2.5). Both are due to OpenAI [OpenAI-M, Sections 2 and 3], [OpenAI-D, Sections 2 and 3].

All matrices are real, and \(X^{\mathsf T}\) is the transpose. For symmetric matrices, \(X\le Y\) means that \(Y-X\) is positive semidefinite. \(\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)\) is the Hilbert–Schmidt inner product and \(\|X\|\) the operator norm.

## 1. The energy and its Hessian

For a positive semidefinite matrix \(P\) put
\[
\begin{aligned}
\Phi(P)&=\operatorname{tr}(P^{3/2}),\\
\operatorname{supp}P&=(\ker P)^\perp .
\end{aligned}
\]
\(\Phi\) is continuous, because the eigenvalues of \(P\) depend continuously on \(P\). A symmetric matrix \(K\) is *supported on* \(P\) if \(K\) vanishes on \(\ker P\); then its range lies in \(\operatorname{supp}P\) as well. For such \(K\) put
\[
b_P(K)=\frac32\sum_{i,j}\frac{K_{ij}^2}{\sqrt{p_i}+\sqrt{p_j}},
\]
where \(p_i>0\) are the eigenvalues of \(P\) on \(\operatorname{supp}P\) and \(K_{ij}\) are the entries of \(K\) in an orthonormal eigenbasis of \(\operatorname{supp}P\); \(b_0(0)=0\). Simultaneous orthogonal conjugation of \(P\) and \(K\), and extension of both by zero to a larger space, change neither \(\Phi\) nor \(b\). For a matrix \(B\), \(\mathcal L_B(X)=BX+XB\) on the space of all matrices.

**Lemma 2.1** (Hessian). Let \(V\) be a subspace. On the set of positive semidefinite \(P\) with \(\operatorname{supp}P=V\), viewed as positive definite matrices on \(V\), \(\Phi\) is smooth, and for symmetric \(K\) supported on \(V\)
\[
\begin{aligned}
d\Phi_P(K)&=\tfrac32\operatorname{tr}(\sqrt P\,K),\\
d^2\Phi_P(K,K)&=b_P(K)=\tfrac32\langle K,\mathcal L_{\sqrt P}^{-1}K\rangle .
\end{aligned}
\]
In particular \(\Phi\) is convex on the positive semidefinite matrices.

*Proof.* Work on \(V\) and put \(B=\sqrt P\). The derivative of \(X\mapsto X^2\) at \(B\) is \(\mathcal L_B\); in an eigenbasis of \(P\), \(\mathcal L_B\) multiplies the entry \((i,j)\) by \(\sqrt{p_i}+\sqrt{p_j}>0\), so it is invertible. By the inverse function theorem, squaring has a smooth local inverse near \(B\), which agrees with the positive square root because squaring is injective on positive definite matrices and the positive square root is continuous. Its derivative \(X\) in the direction \(K\) solves \(BX+XB=K\). Since \(\operatorname{tr}(B^2X)=\operatorname{tr}(BXB)\),
\[
\begin{aligned}
d\Phi_P(K)&=3\operatorname{tr}(B^2X)\\
&=\tfrac32\operatorname{tr}\bigl(B(BX+XB)\bigr)\\
&=\tfrac32\operatorname{tr}(BK).
\end{aligned}
\]
Differentiating once more, \(d^2\Phi_P(K,K)=\frac32\operatorname{tr}(XK)\) with \(X=\mathcal L_B^{-1}K\); in the eigenbasis, \(X_{ij}=K_{ij}/(\sqrt{p_i}+\sqrt{p_j})\), so this is \(b_P(K)\ge0\). For positive semidefinite \(P_0,P_1\) and \(\eta>0\), the matrices \((1-t)P_0+tP_1+\eta I\) are positive definite, so \(t\mapsto\Phi((1-t)P_0+tP_1+\eta I)\) is convex on \([0,1]\); letting \(\eta\to0\) proves convexity of \(\Phi\). \(\square\)

## 2. Order comparison

**Lemma 2.2.** Let \(0<X\le Y\) be positive definite. Then \(Y^{-1}\le X^{-1}\) and \(\sqrt X\le\sqrt Y\). The first statement holds for positive definite self-adjoint operators on any finite-dimensional inner product space.

*Proof.* Conjugation preserves the order, so \(I\le X^{-1/2}YX^{-1/2}\); the inverse of a positive definite matrix that is at least \(I\) is at most \(I\), so \(X^{1/2}Y^{-1}X^{1/2}\le I\), and conjugating back gives \(Y^{-1}\le X^{-1}\). For \(x>0\), the substitution \(t=xs^2\) gives \(\int_0^\infty t^{-1/2}(x+t)^{-1}\,dt=\pi/\sqrt x\), hence
\[
\sqrt x=\frac1\pi\int_0^\infty\Bigl(1-\frac t{x+t}\Bigr)\frac{dt}{\sqrt t},
\]
and applying this to the eigenvalues,
\[
\sqrt X=\frac1\pi\int_0^\infty\bigl(I-t(X+tI)^{-1}\bigr)\frac{dt}{\sqrt t}.
\]
Since \((X+tI)^{-1}\ge(Y+tI)^{-1}\) by the first statement, the integrand for \(X\) is at most the one for \(Y\). \(\square\)

**Lemma 2.3** (order comparison). Let \(P,Q\) be positive semidefinite, \(a\ge1\) and \(P\le aQ\). Then every symmetric \(K\) supported on \(P\) is supported on \(Q\), and
\[
b_P(K)\ge a^{-1/2}\,b_Q(K).
\]

*Proof.* If \(Qx=0\), then \(0\le\langle Px,x\rangle\le a\langle Qx,x\rangle=0\), so \(Px=0\); thus \(\ker Q\subseteq\ker P\), which gives the first statement.

Suppose first that \(P\) and \(Q\) are positive definite. By Lemma 2.2, \(\sqrt P\le\sqrt{aQ}=\sqrt a\sqrt Q\). For a positive semidefinite \(A\), the quadratic form of \(\mathcal L_A\) is \(\langle X,\mathcal L_AX\rangle=\operatorname{tr}(X^{\mathsf T}AX)+\operatorname{tr}(XAX^{\mathsf T})\), which is nonnegative and increasing in \(A\). Hence \(\mathcal L_{\sqrt P}\le\sqrt a\,\mathcal L_{\sqrt Q}\) as operators on the space of matrices, and by Lemma 2.2, \(\mathcal L_{\sqrt P}^{-1}\ge a^{-1/2}\mathcal L_{\sqrt Q}^{-1}\). The formula \(b_P(K)=\frac32\langle K,\mathcal L_{\sqrt P}^{-1}K\rangle\) of Lemma 2.1 gives the inequality.

In general, \(P+\eta I\le a(Q+\eta I)\) for \(\eta>0\), as \(a\ge1\). In an eigenbasis of \(P\) on the whole space, the entries of \(K\) in rows or columns belonging to \(\ker P\) vanish, so \(b_{P+\eta I}(K)\to b_P(K)\) as \(\eta\to0\); likewise \(b_{Q+\eta I}(K)\to b_Q(K)\), since \(K\) is supported on \(Q\). \(\square\)

**Corollary 2.4** (midpoint gap). Let \(T\) be positive semidefinite and \(U\) symmetric with \(-T\le U\le T\). Then \(U\) is supported on \(T\), and
\[
\begin{aligned}
&\frac{\Phi(T+U)+\Phi(T-U)}2-\Phi(T)\\
&\quad\ge\frac{b_T(U)}{2\sqrt2}.
\end{aligned}
\]

*Proof.* If \(Tx=0\), the positive semidefinite matrices \(T\pm U\) have quadratic forms vanishing at \(x\), so \((T\pm U)x=0\) and \(Ux=0\). If \(T=0\), all terms vanish. For \(|t|<1\),
\[
(1-|t|)T\le T+tU\le(1+|t|)T\le2T,
\]
so \(T+tU\) is positive semidefinite with the same kernel as \(T\). By Lemmas 2.1 and 2.3 (with \(a=2\)), \(f(t)=\Phi(T+tU)\) has \(f''(t)=b_{T+tU}(U)\ge2^{-1/2}b_T(U)\) on \((-1,1)\). So \(f(t)-b_T(U)t^2/(2\sqrt2)\) is convex on \((-1,1)\) and continuous on \([-1,1]\), and its midpoint inequality at \(\pm1\) is the claim. \(\square\)

## 3. A triangular trace estimate

Let \(H_0,H_1,H_2\) be finite-dimensional real inner product spaces, indices modulo \(3\), and \(W_v:H_{v+1}\to H_v\) linear maps. The *row star* at \(v\) is the map \(R_v=[\,W_v\ \ W_{v-1}^{\mathsf T}\,]\) from \(H_{v+1}\oplus H_{v-1}\) to \(H_v\), and \(T_v=R_v^{\mathsf T}R_v\).
The matrices \(R_v^{\mathsf T}R_v\) and \(R_vR_v^{\mathsf T}\) have the same nonzero eigenvalues with multiplicities, so they have the same energy \(\Phi\).

**Proposition 2.5** (mixed trace estimate). Let \(D_v\) be symmetric on \(H_v\) with \(\|D_v\|\le1\), and \(U_v=R_v^{\mathsf T}D_vR_v\). Then \(U_v\) is supported on \(T_v\), and
\[
\begin{aligned}
&\bigl|\operatorname{tr}(D_0W_0D_1W_1D_2W_2)\bigr|\\
&\quad\le\frac53\sum_{v=0}^2b_{T_v}(U_v).
\end{aligned}
\]

*Proof.* \(\ker T_v=\ker R_v\), and \(U_v\) vanishes there.

*A common quadratic form.* On \(H=H_0\oplus H_1\oplus H_2\) let
\[
M=\begin{pmatrix}0&W_0&W_2^{\mathsf T}\\W_0^{\mathsf T}&0&W_1\\W_2&W_1^{\mathsf T}&0\end{pmatrix}
\]
and \(D=\operatorname{diag}(D_0,D_1,D_2)\), both symmetric, with \(\|D\|\le1\). Let \(P_v\) be the orthogonal projection onto \(H_v\), and \(A_v=MP_vM\), \(K_v=MP_vDM\). The only nonzero block row of \(P_vM\) is \(R_v\), with its blocks placed according to the vertices, so after a permutation of blocks and extension by zero, \(A_v\) is \(T_v\) and \(K_v\) is \(U_v\). As \(P_vD=DP_v\), \(K_v\) is symmetric, and
\[
\begin{aligned}
0\le A_v&\le\sum_uA_u=M^2,\\
\sum_vK_v&=MDM .
\end{aligned}
\]
By Lemma 2.3 with \(a=1\), and since \(b_{M^2}\) is a positive semidefinite quadratic form, for which \(b(K_0+K_1+K_2)\le3\sum_vb(K_v)\),
\[
\begin{aligned}
&\mathcal E:=\sum_vb_{T_v}(U_v)=\sum_vb_{A_v}(K_v)\\
&\quad\ge\sum_vb_{M^2}(K_v)\ge\tfrac13b_{M^2}(MDM).
\end{aligned}
\]

*The cubic trace.* Choose an orthonormal eigenbasis of \(M\) with eigenvalues \(m_i\), ordered so that \(q_i=|m_i|\) is nonincreasing, and write \(D_{ij}\) for the entries of \(D\) in it. Then \((MDM)_{ij}=m_im_jD_{ij}\), and the square roots of the eigenvalues of \(M^2\) are the \(q_i\), so
\[
\mathcal E\ge\frac12Q,\qquad Q=\sum_{q_i+q_j>0}\frac{q_i^2q_j^2}{q_i+q_j}D_{ij}^2 .
\]
Put \(A_i=q_i^3D_{ii}^2\), \(E_i=q_i\sum_{j>i}q_j^2D_{ij}^2\), \(A=\sum_iA_i\) and \(E=\sum_iE_i\). The diagonal terms of \(Q\) add up to \(A/2\), and for \(i<j\) the two terms \((i,j)\), \((j,i)\) add up to \(2q_i^2q_j^2D_{ij}^2/(q_i+q_j)\ge q_iq_j^2D_{ij}^2\), because \(q_i\ge q_j\); so \(Q\ge A/2+E\).

Expand
\[
\operatorname{tr}\bigl((DM)^3\bigr)=\sum_{i,j,k}m_im_jm_kD_{ij}D_{jk}D_{ki},
\]
and sort the terms by the smallest index \(i\) among \(\{i,j,k\}\) and the number of times it occurs.

- *Once.* The three positions of \(i\) contribute equally, giving \(3m_i\sum_{j,k>i}x_jD_{jk}x_k\) with \(x_j=m_jD_{ji}\). The compression of \(D\) to the indices larger than \(i\) is a contraction, so this is at most \(3q_i\sum_{j>i}m_j^2D_{ij}^2=3E_i\) in absolute value.
- *Twice.* The contribution is \(3m_i^2D_{ii}\sum_{j>i}m_jD_{ij}^2\). The rows of \(D\) have norm at most \(1\), so by the Cauchy–Schwarz inequality its absolute value is at most \(3q_i^2|D_{ii}|(\sum_{j>i}q_j^2D_{ij}^2)^{1/2}\), which is \(3\sqrt{A_iE_i}\).
- *Three times.* \(|m_i^3D_{ii}^3|\le A_i\), as \(|D_{ii}|\le1\).

Summing, and using \(\sum_i\sqrt{A_iE_i}\le\sqrt{AE}\le(A+E)/2\),
\[
\begin{aligned}
\bigl|\operatorname{tr}((DM)^3)\bigr|&\le A+3E+3\sqrt{AE}\\
&\le\tfrac52A+\tfrac92E\le5Q .
\end{aligned}
\]

*Back to the triangle.* \(M\) has zero diagonal blocks, so a nonzero term of \(\operatorname{tr}((DM)^3)\) in block form runs once around the triangle of vertices. The three starting vertices in one direction give \(\tau=\operatorname{tr}(D_0W_0D_1W_1D_2W_2)\) each, by cyclicity of the trace, and the other direction gives the trace of the transpose, again \(\tau\). So \(\operatorname{tr}((DM)^3)=6\tau\), and \(6|\tau|\le5Q\le10\mathcal E\). \(\square\)

The constant does not depend on the dimensions of \(H_0,H_1,H_2\); this is what allows arbitrarily fine step functions in [Energy increase and telescoping](energy-increase-and-telescoping.md).

## 4. Exercises

**2.1** (easy). For positive definite \(P=\operatorname{diag}(p_1,p_2)\) and \(K=\operatorname{diag}(k_1,k_2)\), compute \(\frac{d^2}{dt^2}\Phi(P+tK)\) at \(t=0\) directly and compare with \(b_P(K)\).

**2.2** (easy). Show that \(\Phi(T)\le(\operatorname{tr}T)^{3/2}\) for positive semidefinite \(T\).

**2.3** (medium). Show that \(X\mapsto X^2\) is not monotone: for \(X=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)\) and \(Y=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)\), \(0\le X\le Y\) but \(X^2\not\le Y^2\).

**2.4** (medium). Let \(H_0,H_1,H_2\) be one-dimensional, \(W_v=(w_v)\) and \(D_v=(d_v)\) with \(|d_v|\le1\). Show that \(b_{T_v}(U_v)=\frac34d_v^2(w_v^2+w_{v-1}^2)^{3/2}\), and check Proposition 2.5 for \(w_v=d_v=1\).

## 5. Solutions

**2.1.** \(\Phi(P+tK)\) is \((p_1+tk_1)^{3/2}+(p_2+tk_2)^{3/2}\), with second derivative \(\frac34(k_1^2p_1^{-1/2}+k_2^2p_2^{-1/2})\) at \(0\). The formula gives \(b_P(K)=\frac32\bigl(k_1^2/(2\sqrt{p_1})+k_2^2/(2\sqrt{p_2})\bigr)\), the same.

**2.2.** With eigenvalues \(t_i\ge0\) and \(s=\sum_it_i>0\), since \(t_i/s\le1\),
\[
\begin{aligned}
\sum_it_i^{3/2}&=s^{3/2}\sum_i(t_i/s)^{3/2}\\
&\le s^{3/2}\sum_it_i/s=s^{3/2}.
\end{aligned}
\]

**2.3.** \(Y-X=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)\ge0\), and \(Y^2-X^2=\bigl(\begin{smallmatrix}4&3\\3&2\end{smallmatrix}\bigr)\) has determinant \(-1<0\).

**2.4.** \(R_v=(w_v,w_{v-1})\), so \(T_v=R_v^{\mathsf T}R_v\) has the single positive eigenvalue \(t_v=w_v^2+w_{v-1}^2\) with unit eigenvector \(R_v^{\mathsf T}/\sqrt{t_v}\), and \(U_v=d_vT_v\) has the entry \(d_vt_v\) there. So \(b_{T_v}(U_v)=\frac32d_v^2t_v^2/(2\sqrt{t_v})=\frac34d_v^2t_v^{3/2}\). For \(w_v=d_v=1\), \(\tau=1\) and \(\frac53\sum_vb_{T_v}(U_v)=\frac53\cdot3\cdot\frac34\cdot2^{3/2}\), which is \(15/\sqrt2\approx10.6\).

## References

- [OpenAI-D] OpenAI, *An \(L^3\) bound for the dyadic triangular Hilbert form*, OpenAI Math Release preprint, 5 October 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026
- [OpenAI-M] OpenAI, *The maximal triangular Hilbert transform at the symmetric point*, OpenAI Math Release preprint, 24 September 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026
