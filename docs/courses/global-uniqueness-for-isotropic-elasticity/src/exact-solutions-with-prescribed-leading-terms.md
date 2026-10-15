# Exact solutions with prescribed leading terms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Solutions of \(Lu=0\) of the form \(u=e^{\tau\theta\cdot x}\bigl(a_0+O(\tau^{-1})\bigr)\), with a complex vector \(\theta\) satisfying \(\theta\cdot\theta=0\), are complex geometrical optics solutions, which Sylvester and Uhlmann introduced for the conductivity equation (see the introduction of [Tan–Liu 2023]). For the comparison of two elastic media, the actual divergence of the displacement matters as much as the displacement itself. This lesson shows that the leading pair \((a_0,b_0)\) of displacement and divergence satisfies a first-order transport equation on a three-dimensional space of vectors, and that every solution of it on a cylinder, in particular every frame of three solutions, is the leading pair of exact solutions, with control of the weighted first derivatives [OpenAI-EL, Section 4].

- The leading operators (Section 1).
- The constrained transport equation (Section 2).
- Exact solutions (Section 3).

We keep the notation of An augmented system and a Carleman estimate: one pair of moduli on \(\mathbb R^3\) from Lemma 3.1 of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md), constant outside \(B_r\); \(m,k,\ell\); the operators \(R,S,P\); a fixed nonzero \(\theta\in\mathbb C^3\) with \(\theta\cdot\theta=0\); \(D=D_\theta=\theta\cdot\nabla\), \(E_\tau=e^{\tau\theta\cdot x}\) and \(h=\tau^{-1}\). The frames and inhomogeneous solutions come from Lemmas 2.2 and 2.3 of [Planar transport equations](planar-transport-equations.md).

## 1. The leading operators

Since \(E_\tau^{-1}\partial_j(E_\tau f)=\partial_jf+\tau\theta_jf\) and \(\theta\cdot\theta=0\), we have \(E_\tau^{-1}\Delta(E_\tau f)=\Delta f+2\tau Df\), with no term in \(\tau^2\).

**Lemma 1.1** (conjugation; [OpenAI-EL, Section 4]). For smooth \(a\) (vector) and \(b\) (scalar),
\[
\begin{aligned}E_\tau^{-1}R(E_\tau a,E_\tau b)&=R(a,b)+\tau R^\theta(a,b),\\ E_\tau^{-1}S(E_\tau a,E_\tau b)&=S(a,b)+\tau S^\theta(a,b),\end{aligned}
\]
\[
E_\tau^{-1}P(E_\tau g)=Pg+\tau P^\theta g,
\]
where
\[
\begin{aligned}&R^\theta(a,b)=2m\,Da\\&\quad+(Dm)\,a\\&\quad+\theta\,(kb+\nabla m\cdot a),\\&S^\theta(a,b)=2\ell\,Db\\&\quad+2(Dk)\,b+4\nabla m\cdot Da\\&\quad+2(D\nabla m)\cdot a,\\&P^\theta g=2m\,Dg+(Dm)\,g .\end{aligned}\tag{1.1}
\]

*Proof.* Replace every derivative \(\partial_j\) in (1.1) of An augmented system and a Carleman estimate by \(\partial_j+\tau\theta_j\). In \(R\): \(m\Delta a_i\) gives \(2\tau m\,Da_i\); \(k\partial_ib\) gives \(\tau k\theta_ib\); \(C(a)_i=\sum_j(\partial_jm)(\partial_ja_i+\partial_ia_j)\) gives \(\tau\bigl((Dm)a_i+\theta_i\,\nabla m\cdot a\bigr)\); the term \((\partial_i\lambda)b\) gives nothing. In \(S\): \(\ell\Delta b\) gives \(2\tau\ell\,Db\); \(2\nabla k\cdot\nabla b\) gives \(2\tau(Dk)b\); \(2\nabla m\cdot\Delta a\) gives \(4\tau\nabla m\cdot Da\); \(2\sum_{i,j}(\partial_i\partial_jm)\partial_ia_j\) gives \(2\tau\sum_{i,j}\theta_i(\partial_i\partial_jm)a_j=2\tau(D\nabla m)\cdot a\). In \(P\): \(m\Delta g\) gives \(2\tau m\,Dg\) and \(\nabla m\cdot\nabla g\) gives \(\tau(Dm)g\). No product of two \(\tau\theta\) occurs except in \(\Delta\), where it is \(\tau^2\theta\cdot\theta=0\). \(\square\)

**Lemma 1.2** (compatibility; [OpenAI-EL, Section 4]). For all smooth \((a,b)\),
\[
\theta\cdot R^\theta(a,b)=P^\theta(\theta\cdot a),
\tag{1.2}
\]
\[
\begin{aligned}&\operatorname{div}R^\theta(a,b)+\theta\cdot R(a,b)\\&\qquad-S^\theta(a,b)\\&\quad=P(\theta\cdot a)\\&\qquad+P^\theta(\operatorname{div}a-b).\end{aligned}\tag{1.3}
\]

*Proof.* Apply the identity \(\operatorname{div}R(u,d)-S(u,d)=P(\operatorname{div}u-d)\) of Lemma 1.1 of An augmented system and a Carleman estimate to \(u=E_\tau a\), \(d=E_\tau b\), and multiply by \(E_\tau^{-1}\). By Lemma 1.1, and since \(E_\tau^{-1}\operatorname{div}(E_\tau w)=\operatorname{div}w+\tau\theta\cdot w\) and \(\operatorname{div}u-d=E_\tau(\operatorname{div}a-b+\tau\,\theta\cdot a)\),
\[
\begin{aligned}&\operatorname{div}R(a,b)-S(a,b)+\tau^2\,\theta\cdot R^\theta(a,b)\\&\qquad+\tau\bigl(\theta\cdot R(a,b)+\operatorname{div}R^\theta(a,b)\\&\qquad\qquad-S^\theta(a,b)\bigr)\\&=P(\operatorname{div}a-b)+\tau^2P^\theta(\theta\cdot a)\\&\qquad+\tau\bigl(P^\theta(\operatorname{div}a-b)+P(\theta\cdot a)\bigr).\end{aligned}
\]
Both sides are polynomials in \(\tau\) that agree for all \(\tau>0\), so their coefficients agree. The coefficients of \(\tau^2\) give (1.2) and those of \(\tau\) give (1.3). \(\square\)

For amplitudes \(a_0,a_1\),
\[
\begin{aligned}&E_\tau^{-1}\operatorname{div}\bigl(E_\tau(a_0+\tau^{-1}a_1)\bigr)\\&\quad=\tau\,\theta\cdot a_0+(\operatorname{div}a_0+\theta\cdot a_1)\\&\qquad+\tau^{-1}\operatorname{div}a_1 .\end{aligned}
\]
A divergence of order \(\tau^0\) requires \(\theta\cdot a_0=0\), and then its leading term contains \(\theta\cdot a_1\) as well as \(\operatorname{div}a_0\). The leading divergence is therefore an independent scalar \(b\), and the leading pair is \((a,b)\).

## 2. The constrained transport equation

Define the fixed complex vector spaces
\[
\begin{gathered}H_\theta=\{a\in\mathbb C^3:\theta\cdot a=0\},\\ \mathcal E_\theta=H_\theta\oplus\mathbb C .\end{gathered}\tag{2.1}
\]
\(H_\theta\) has dimension two and contains \(\theta\). The *constrained transport equation* for a smooth pair \((a,b)\) with values in \(\mathcal E_\theta\) is
\[
\begin{gathered}R^\theta(a,b)=0,\\ S^\theta(a,b)=0 .\end{gathered}\tag{2.2}
\]
If \(a\) takes values in \(H_\theta\), then \(\theta\cdot a=0\) identically, and (1.2) gives \(\theta\cdot R^\theta(a,b)=0\): \(R^\theta(a,b)\) takes values in \(H_\theta\). Also \(Da\) takes values in \(H_\theta\), because \(\theta\) is constant. So (2.2) is a system of three equations for three unknown functions, and its terms with derivatives are \(\bigl(2m\,Da,\ 2\ell\,Db+4\nabla m\cdot Da\bigr)\), with coefficient
\[
Q=\begin{pmatrix}2m\,\mathrm{Id}_{H_\theta}&0\\ 4\nabla m\cdot&2\ell\end{pmatrix}\quad\text{on }\mathcal E_\theta ,
\]
which is invertible because \(m,\ell>0\). Thus (2.2) expresses \(Q\,D(a,b)\) as a linear function of \(a\) and \(b\) with smooth coefficients.

Write \(\theta=\alpha+i\beta\) with \(|\alpha|=|\beta|=\rho_0>0\) and \(\alpha\perp\beta\), and let \((y_1,y_2,t)\) be the coordinates of \(x\) in the positively oriented orthonormal basis \(\alpha/\rho_0,\ \beta/\rho_0,\ \alpha\times\beta/\rho_0^2\). With \(z=y_1+iy_2\),
\[
D=\rho_0(\partial_{y_1}+i\partial_{y_2})=2\rho_0\,\partial_{\bar z},
\]
so \(D\) acts in the planes \(t=\text{const}\), and \(t\) is a parameter. Choosing a basis of \(\mathcal E_\theta\), the results of Section 2 of [Planar transport equations](planar-transport-equations.md) apply to (2.2), the equation divided by \(Q\), and to its inhomogeneous versions. For the cylinders we write \(D^2_R\times J=\{x:|y|<R,\ t\in J\}\).

## 3. Exact solutions

**Proposition 3.1** (exact solutions realizing a local transport frame; [OpenAI-EL, Proposition 4.3]). For every \(t_0\in(-2r,2r)\) there are an open interval \(J\subset(-2r,2r)\) containing \(t_0\) and three smooth solutions \((a_0^\nu,b_0^\nu)\), \(\nu=1,2,3\), of (2.2) on a neighbourhood of \(\overline{B_{5r}}\), with the following properties. At every point of \(D^2_{2r}\times J\) they form a basis of \(\mathcal E_\theta\). For each \(\nu\) and all sufficiently large \(\tau\) there is \(u^\nu_\tau\in C^\infty(B_{5r};\mathbb C^3)\) with \(Lu^\nu_\tau=0\) such that, for \(U^\nu_\tau=(u^\nu_\tau,\operatorname{div}u^\nu_\tau)\),
\[
\begin{gathered}E_\tau^{-1}U^\nu_\tau\longrightarrow(a_0^\nu,b_0^\nu)\\ \text{in }L^2(B_{4r}),\\ \|E_\tau^{-1}\nabla U^\nu_\tau\|_{L^2(B_{4r})}=O(\tau).\end{gathered}\tag{3.1}
\]

*Proof.* Fix an integer \(N\ge4\) and radii \(R_0>R_1>\cdots>R_N>5r\).

*The leading frame.* By Lemma 2.2 of [Planar transport equations](planar-transport-equations.md), applied to (2.2) on a disk larger than \(D^2_{R_0}\), there are an open interval \(I_0\Subset(-2r,2r)\) containing \(t_0\) and a smooth map \(\mathcal F(y,t):\mathbb C^3\to\mathcal E_\theta\), invertible at every point of \(D^2_{R_0}\times I_0\), whose columns solve (2.2). Choose an open interval \(J\ni t_0\) with \(\overline J\subset I_0\) and \(\chi\in C^\infty_c(I_0)\) with \(\chi=1\) on \(J\), and let \((a_0^\nu,b_0^\nu)\) be the columns of \(\chi(t)\mathcal F\), extended by zero in \(t\). As \(D\) does not differentiate in \(t\), they still solve (2.2), now on \(D^2_{R_0}\times\mathbb R\), which contains \(\overline{B_{5r}}\); they form a basis on \(D^2_{2r}\times J\), and they vanish for \(t\) outside the compact set \(K=\operatorname{supp}\chi\subset I_0\). Fix one column and omit \(\nu\).

*The recursion.* We construct smooth \((a_j,b_j)\) on \(D^2_{R_j}\times\mathbb R\), \(1\le j\le N\), vanishing for \(t\notin K\), with
\[
\begin{aligned}&R^\theta(a_j,b_j)\\&\quad=-R(a_{j-1},b_{j-1}),\\&S^\theta(a_j,b_j)\\&\quad=-S(a_{j-1},b_{j-1}),\\&\theta\cdot a_j=-q_{j-1},\end{aligned}\tag{3.2}
\]
where \(q_j=\operatorname{div}a_j-b_j\); put \(q_{-1}=0\). First we show that, once \((a_i,b_i)\) for \(i<j\) are constructed,
\[
\theta\cdot R(a_{j-1},b_{j-1})=P^\theta q_{j-1}.
\tag{3.3}
\]
By (1.3) applied to \((a_{j-1},b_{j-1})\), it suffices to show
\[
\begin{aligned}&P(\theta\cdot a_{j-1})+S^\theta(a_{j-1},b_{j-1})\\&\quad-\operatorname{div}R^\theta(a_{j-1},b_{j-1})=0 .\end{aligned}
\]
For \(j=1\) all three terms vanish, as \((a_0,b_0)\) solves (2.2) with values in \(\mathcal E_\theta\). For \(j\ge2\), (3.2) at the step \(j-1\) and the identity \(\operatorname{div}R-S=P(\operatorname{div}a-b)\) of Lemma 1.1 of An augmented system and a Carleman estimate give
\[
\begin{aligned}&S^\theta(a_{j-1},b_{j-1})-\operatorname{div}R^\theta(a_{j-1},b_{j-1})\\&\quad=\operatorname{div}R(a_{j-2},b_{j-2})-S(a_{j-2},b_{j-2})\\&\quad=Pq_{j-2},\end{aligned}
\]
while \(P(\theta\cdot a_{j-1})=-Pq_{j-2}\). This proves (3.3).

Now fix a constant \(n_\theta\in\mathbb C^3\) with \(\theta\cdot n_\theta=1\), and write \((a_j,b_j)=(-q_{j-1}n_\theta,0)+(a',b')\) with \((a',b')\) taking values in \(\mathcal E_\theta\). Then \(\theta\cdot a_j=-q_{j-1}\), and (3.2) becomes
\[
\begin{aligned}R^\theta(a',b')&=-R(a_{j-1},b_{j-1})\\&\quad+R^\theta(q_{j-1}n_\theta,0),\\ S^\theta(a',b')&=-S(a_{j-1},b_{j-1})\\&\quad+S^\theta(q_{j-1}n_\theta,0).\end{aligned}
\]
By (3.3) and (1.2), with \(\theta\cdot n_\theta=1\), the bilinear product of \(\theta\) with the first right side is \(-P^\theta q_{j-1}+P^\theta q_{j-1}=0\), so the first right side takes values in \(H_\theta\); the second is an arbitrary scalar. This is an inhomogeneous version of (2.2) on \(\mathcal E_\theta\), with smooth right side on \(D^2_{R_{j-1}}\times\mathbb R\) vanishing for \(t\notin K\). Lemma 2.3 of [Planar transport equations](planar-transport-equations.md), with the frame \(\mathcal F\), gives a smooth solution on \(D^2_{R_j}\times I_0\) vanishing for \(t\notin K\); extended by zero in \(t\), it is smooth on \(D^2_{R_j}\times\mathbb R\). This completes the induction, and all \((a_j,b_j)\) are smooth on a neighbourhood of \(\overline{B_{5r}}\).

*The truncated expansion.* Put \(a^{[N]}=\sum_{j=0}^N\tau^{-j}a_j\) and \(b^{[N]}=\sum_{j=0}^N\tau^{-j}b_j\). By Lemma 1.1 and (3.2), the sum telescopes:
\[
\begin{aligned}&E_\tau^{-1}R(E_\tau a^{[N]},E_\tau b^{[N]})\\&\ =\sum_{j=0}^N\tau^{-j}R(a_j,b_j)\\&\qquad+\sum_{j=0}^N\tau^{1-j}R^\theta(a_j,b_j)\\&\ =\tau^{-N}R(a_N,b_N).\end{aligned}\tag{3.4}
\]
Similarly \(E_\tau^{-1}\operatorname{div}(E_\tau a^{[N]})\) is \(\sum_j\tau^{-j}(\operatorname{div}a_j+\tau\,\theta\cdot a_j)\), and \(\theta\cdot a_0=0\), \(\theta\cdot a_j=-(\operatorname{div}a_{j-1}-b_{j-1})\), so
\[
\begin{aligned}&E_\tau^{-1}\operatorname{div}(E_\tau a^{[N]})\\&\quad=b^{[N]}+\tau^{-N}q_N .\end{aligned}\tag{3.5}
\]
As \(R(u,d)\) depends on \(d\) only through \(k\nabla d+(\nabla\lambda)d\), Lemma 1.1 of An augmented system and a Carleman estimate, (3.4) and (3.5) give the physical residual
\[
\begin{aligned}f_\tau&:=E_\tau^{-1}L(E_\tau a^{[N]})\\&=\tau^{-N}\bigl[R(a_N,b_N)\\&\qquad+k\nabla q_N+(\nabla\lambda)q_N\\&\qquad+\tau k\,\theta\,q_N\bigr],\end{aligned}\tag{3.6}
\]
a smooth function with \(\|f_\tau\|_{L^2(B_{5r})}=O(\tau^{1-N})\).

*The correction.* Corollary 4.1 of An augmented system and a Carleman estimate, on the ball \(B_{5r}\), gives \(r_\tau\in L^2(B_{5r};\mathbb C^3)\) with \(E_\tau^{-1}L(E_\tau r_\tau)=-f_\tau\) and \(\|r_\tau\|_{L^2(B_{5r})}=O(\tau^{1-N})\). By Lemma 5.1 of that lesson, \(r_\tau\) is smooth in \(B_{5r}\), and on \(B_{4r}\)
\[
\begin{aligned}&\sum_{j=0}^2h^j\|\nabla^jr_\tau\|_{L^2(B_{4r})}\\&\quad=O(\tau^{1-N}).\end{aligned}\tag{3.7}
\]
For the conjugated divergence \(d_\tau=E_\tau^{-1}\operatorname{div}(E_\tau r_\tau)=\operatorname{div}r_\tau+\tau\,\theta\cdot r_\tau\), (3.7) gives, with all norms taken in \(L^2(B_{4r})\),
\[
\begin{aligned}&\|d_\tau\|+h\|\nabla d_\tau\|\\&\quad\le C\tau\sum_{j=0}^2h^j\|\nabla^jr_\tau\|\\&\quad=O(\tau^{2-N}).\end{aligned}\tag{3.8}
\]

*The solution.* Put \(u_\tau=E_\tau(a^{[N]}+r_\tau)\). It is smooth on \(B_{5r}\), and \(E_\tau^{-1}Lu_\tau=f_\tau-f_\tau=0\). By (3.5), its physical pair satisfies
\[
\begin{aligned}\mathcal A_\tau&:=E_\tau^{-1}(u_\tau,\operatorname{div}u_\tau)\\&=\bigl(a^{[N]}+r_\tau,\ b^{[N]}+\tau^{-N}q_N+d_\tau\bigr).\end{aligned}
\]
The expansions \(a^{[N]},b^{[N]}\) converge to \(a_0,b_0\) uniformly with all derivatives on \(\overline{B_{4r}}\), and \(N\ge4\), so (3.7) and (3.8) give \(\mathcal A_\tau\to(a_0,b_0)\) in \(L^2(B_{4r})\) and \(\|\mathcal A_\tau\|_{L^2(B_{4r})}+h\|\nabla\mathcal A_\tau\|_{L^2(B_{4r})}=O(1)\). Finally \(E_\tau^{-1}\partial_j(E_\tau\mathcal A_\tau)=\partial_j\mathcal A_\tau+\tau\theta_j\mathcal A_\tau\), so
\[
\begin{aligned}&\|E_\tau^{-1}\nabla U_\tau\|_{L^2(B_{4r})}\\&\quad\le\tau\bigl(h\|\nabla\mathcal A_\tau\|+|\theta|\|\mathcal A_\tau\|\bigr)=O(\tau).\end{aligned}
\]
Repeating the construction for the three columns proves the proposition. \(\square\)

The expansion is taken to order \(N\ge4\) because the correction loses one power of \(\tau\) in the residual (3.6) and another in the divergence (3.8); with \(N\ge4\) both losses still leave a quantity that tends to zero.

## 4. Exercises

**4.1.** For constant moduli and \(\theta=(1,i,0)\), write the transport equation (2.2) explicitly and find its solutions that do not depend on \(t\).

**4.2.** Show that \(n_\theta=\overline\theta/(\theta\cdot\overline\theta)\) satisfies \(\theta\cdot n_\theta=1\), and that \(\mathbb C^3=H_\theta\oplus\mathbb Cn_\theta\).

**4.3.** Verify (1.2) directly from (1.1).

**4.4.** Show that the truncated displacement \(E_\tau a^{[N]}\) with \(N=0\) satisfies
\[
\begin{aligned}&E_\tau^{-1}L(E_\tau a_0)\\&\quad=R(a_0,b_0)+k\nabla q_0\\&\qquad+(\nabla\lambda)q_0+\tau k\theta q_0,\end{aligned}
\]
and explain why this is not small.

**4.5.** In the proof of Proposition 3.1, why is the cutoff \(\chi(t)\) harmless for the transport equation, and why is it useful?

## 5. Solutions

**4.1.** With \(\nabla m=\nabla k=0\), (2.2) reads \(2m\,Da+k\theta b=0\) and \(2\ell\,Db=0\), with \(D=\partial_{x_1}+i\partial_{x_2}=2\partial_{\bar z}\) for \(z=x_1+ix_2\). So \(b\) is holomorphic in \(z\) (for each \(x_3\)), and \(a\) satisfies \(2\partial_{\bar z}a=-\frac k{2m}\theta b\), solved for example by \(a=-\frac k{4m}\theta\,\bar z\,b+a^\circ\) with \(a^\circ\) holomorphic with values in \(H_\theta\). Note \(\theta\in H_\theta\), so \(a\) takes values in \(H_\theta\).

**4.2.** \(\theta\cdot\overline\theta=|\theta|^2>0\), so \(n_\theta\) is defined and \(\theta\cdot n_\theta=1\). Every \(v\) is \(\bigl(v-(\theta\cdot v)n_\theta\bigr)+(\theta\cdot v)n_\theta\), with the first term in \(H_\theta\); and \(n_\theta\notin H_\theta\).

**4.3.** By (1.1),
\[
\begin{aligned}\theta\cdot R^\theta(a,b)&=2m\,D(\theta\cdot a)+(Dm)(\theta\cdot a)\\&\quad+(\theta\cdot\theta)(kb+\nabla m\cdot a),\end{aligned}
\]
and \(\theta\cdot\theta=0\); this is \(P^\theta(\theta\cdot a)\).

**4.4.** For \(N=0\), (3.4) is \(E_\tau^{-1}R(E_\tau a_0,E_\tau b_0)=R(a_0,b_0)\) and (3.5) is \(E_\tau^{-1}\operatorname{div}(E_\tau a_0)=b_0+q_0\); the formula follows as in (3.6). The term \(\tau k\theta q_0\) grows with \(\tau\) unless \(q_0=\operatorname{div}a_0-b_0=0\), which (2.2) does not impose.

**4.5.** \(D\) does not differentiate in \(t\), so \(D(\chi(t)v)=\chi(t)Dv\), and the cut-off columns solve (2.2). The cutoff makes all amplitudes vanish for \(t\) outside a compact subset of \(I_0\), where the frame \(\mathcal F\) is defined, so that every amplitude is defined on all of \(D^2_{R_j}\times\mathbb R\supset\overline{B_{5r}}\).

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Tan–Liu 2023] X. Tan, G. Liu, *Determining Lamé coefficients by elastic Dirichlet-to-Neumann map on a Riemannian manifold*, Inverse Problems 39 (2023), no. 9, 095004. https://arxiv.org/abs/2211.06650
