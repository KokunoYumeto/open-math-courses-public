# A quantity monotone along the heat flow

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the analytic core of Ehrhard's inequality (Theorem 2.1): if three functions \(f,g,h\) satisfy the pointwise inequality
\[
\begin{aligned}
&\lambda\Phi^{-1}(f(x))+\mu\Phi^{-1}(g(y))\\
&\quad\le\sigma\Phi^{-1}(h(\lambda x+\mu y))
\end{aligned}
\]
with room to spare after a little smoothing, then the same inequality holds for their Gaussian integrals. The proof follows Neeman and Paouris [NP]: the function \(J=\Phi(r\,\Xi)\) of the three smoothed functions, averaged by the heat semigroup of a pair of correlated Gaussian vectors, decreases in time. The heat semigroup, a time-dependent factor \(r(u)=R(\varepsilon+u)^{(1+\delta)/2}\) and an induction over short time steps replace the Ornstein–Uhlenbeck semigroup and the time change of [NP].

Notation and results on Gaussian heat semigroups are from [Gaussian heat semigroups and a gradient bound](gaussian-heat-semigroups-and-a-gradient-bound.md): \(Q^C_t\), \(Q_t\), \(\mathcal L_C\), \(\Gamma_C\), \(I=\varphi\circ\Phi^{-1}\), Propositions 1.2, 1.5 and 1.7, and Lemma 1.4.

## 1. The setting

Fix \(n\ge1\), \(\lambda\in(0,1)\), \(\mu=1-\lambda\) and \(\rho\in(-1,1)\). Points of \(\mathbf R^{2n}\) are written \((x,y)\) with \(x,y\in\mathbf R^n\). Let
\[
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad\hat C=C\otimes I_n,
\]
so that \(\hat C(a,b)=(a+\rho b,\rho a+b)\) for \(a,b\in\mathbf R^n\); \(\hat C\) is positive definite. Put
\[
\sigma^2=\lambda^2+\mu^2+2\lambda\mu\rho,
\]
which is positive (Exercise 2.1), and
\[
A=\begin{pmatrix}1&\rho&\lambda+\mu\rho\\\rho&1&\lambda\rho+\mu\\\lambda+\mu\rho&\lambda\rho+\mu&\sigma^2\end{pmatrix}.
\]
\(A\) is the covariance matrix of \((X_1,Y_1,\lambda X_1+\mu Y_1)\) for the first coordinates of a pair \((X,Y)\) with law \(\gamma_{\hat C}\); in matrix form \(A=MCM^{\mathsf T}\) with \(M=\bigl(\begin{smallmatrix}1&0\\0&1\\\lambda&\mu\end{smallmatrix}\bigr)\). For \(p=(p_1,p_2,p_3)\in(0,1)^3\) put
\[
\begin{aligned}
\Xi(p)={}&\lambda\Phi^{-1}(p_1)+\mu\Phi^{-1}(p_2)\\
&-\sigma\Phi^{-1}(p_3),
\end{aligned}
\]
and \(\theta=(\lambda,\mu,-\sigma)^{\mathsf T}\), \(\theta'=(1,1,\sigma^{-1})^{\mathsf T}\),
\[
\begin{aligned}
B&=\operatorname{diag}(\theta)\,A\,\operatorname{diag}(\theta),\\
E&=\frac{\operatorname{diag}(\lambda,\mu,\sigma)}{1+\sigma^{-1}} .
\end{aligned}
\]
For \(N>0\), \(\mathcal B_N=[\Phi(-N),\Phi(N)]^3\).

**Theorem 2.1** (after Neeman and Paouris). Let \(N>0\), \(0<\varepsilon<1\), and let \(f,g,h:\mathbf R^n\to[\Phi(-N),\Phi(N)]\) be measurable. For \(0\le u\le1-\varepsilon\) put
\[
\begin{aligned}
F_{1,u}(x,y)&=Q_{\varepsilon+u}f(x),\\
F_{2,u}(x,y)&=Q_{\varepsilon+u}g(y),\\
F_{3,u}(x,y)&=Q_{\sigma^2(\varepsilon+u)}h(\lambda x+\mu y),
\end{aligned}
\]
and \(F_u=(F_{1,u},F_{2,u},F_{3,u})\); put \(\bar f=\int f\,d\gamma_n\), \(\bar g=\int g\,d\gamma_n\) and \(\bar h_\sigma=\int h(\sigma w)\,d\gamma_n(w)\). If there is \(\varepsilon_1>0\) with \(\Xi(F_0(x,y))\le-\varepsilon_1\) for all \((x,y)\), then
\[
\Xi(\bar f,\bar g,\bar h_\sigma)<0 .
\]

At \(u=1-\varepsilon\) and \((x,y)=(0,0)\), \(F_u\) is the triple of integrals in the conclusion: \(Q_1f(0)=\int f\,d\gamma_n\) and \(Q_{\sigma^2}h(0)=\int h(\sigma w)\,d\gamma_n(w)\).

## 2. The function J

**Lemma 2.2.** Let \(r>0\) and \(J(p)=\Phi(r\,\Xi(p))\) on \((0,1)^3\). With \(u_i=\Phi^{-1}(p_i)\) and \(\mathcal I=\operatorname{diag}(I(p_1),I(p_2),I(p_3))\) and \(D_0=\operatorname{diag}(\lambda u_1,\mu u_2,-\sigma u_3)\),
\[
\nabla^2J=\varphi(r\Xi)\,\mathcal I^{-1}\bigl(rD_0-r^3\,\Xi\,\theta\theta^{\mathsf T}\bigr)\mathcal I^{-1},
\]
and, with \(\odot\) the entrywise product of matrices and \(D=\operatorname{diag}(\lambda u_1,\mu u_2,-\sigma^3u_3)\),
\[
\begin{aligned}
A\odot\nabla^2J&=r\,\varphi(r\Xi)\\
&\quad\cdot\mathcal I^{-1}\bigl(D-r^2\,\Xi\,B\bigr)\mathcal I^{-1}.
\end{aligned}
\]

*Proof.* \(du_i/dp_i=1/\varphi(u_i)=1/I(p_i)\) and \(\frac d{dp_i}(1/\varphi(u_i))=u_i/\varphi(u_i)^2\). Write \(\theta_i\) for the entries of \(\theta\), so that \(\partial_i\Xi=\theta_i/\varphi(u_i)\) and \(\partial_i\partial_j\Xi=0\) for \(i\ne j\). Since \(\varphi'(s)=-s\varphi(s)\),
\[
\begin{aligned}
\partial_iJ&=r\varphi(r\Xi)\,\frac{\theta_i}{\varphi(u_i)},\\
\frac{\partial_i\partial_jJ}{\varphi(r\Xi)}&=-\frac{r^3\Xi\,\theta_i\theta_j}{\varphi(u_i)\varphi(u_j)}\\
&\quad+[i=j]\,\frac{r\theta_iu_i}{\varphi(u_i)^2},
\end{aligned}
\]
where \([i=j]\) is \(1\) if \(i=j\) and \(0\) otherwise; this is the first formula. For diagonal matrices \(P,P'\), \(A\odot(PXP')=P(A\odot X)P'\). The diagonal of \(A\) is \((1,1,\sigma^2)\), so \(A\odot\operatorname{diag}(\lambda u_1,\mu u_2,-\sigma u_3)=D\), and \(A\odot\theta\theta^{\mathsf T}=\operatorname{diag}(\theta)A\operatorname{diag}(\theta)=B\). \(\square\)

**Lemma 2.3.** \(B\) is positive semidefinite of rank two, and its kernel is spanned by \(\theta'\). Moreover, for every \(p\),
\[
\theta'^{\mathsf T}D\,\theta'=\Xi(p),\qquad\theta'^{\mathsf T}E\,\theta'=1,
\]
and \(E\) is a diagonal matrix with entries in \((0,1]\).

*Proof.* \(A=MCM^{\mathsf T}\) with \(C\) positive definite and \(M\) of rank two, so \(A\) is positive semidefinite of rank two, and so is \(B\), which is congruent to \(A\) (the entries of \(\theta\) are nonzero). \(M^{\mathsf T}(\lambda,\mu,-1)^{\mathsf T}=0\), so \(A(\lambda,\mu,-1)^{\mathsf T}=0\), and \(\operatorname{diag}(\theta)\theta'=(\lambda,\mu,-1)^{\mathsf T}\) gives \(B\theta'=0\). Next, \(\theta'^{\mathsf T}D\theta'=\lambda u_1+\mu u_2-\sigma^3u_3/\sigma^2=\Xi\), and \(\theta'^{\mathsf T}E\theta'=(\lambda+\mu+\sigma^{-1})/(1+\sigma^{-1})=1\). The entries of \(E\) are \(\lambda/(1+\sigma^{-1})\), \(\mu/(1+\sigma^{-1})\) and \(\sigma^2/(1+\sigma)\), all in \((0,1]\) because \(\sigma\le1\) (Exercise 2.1). \(\square\)

## 3. A matrix inequality

**Lemma 2.4** (Neeman and Paouris). Let \(A_0\) be positive semidefinite and \(B_0\) symmetric, of the same size, and \(\delta_0>0\) with \(v^{\mathsf T}B_0v\ge\delta_0|v|^2\) for \(v\in\ker A_0\) and \(v^{\mathsf T}A_0v\ge\delta_0|v|^2\) for \(v\perp\ker A_0\). Then \(A_0+\eta B_0\) is positive semidefinite for
\[
0\le\eta\le\frac{\delta_0^2}{\|B_0\|^2+\delta_0\|B_0\|}.
\]

*Proof.* Write a vector as \(v+v'\) with \(v\in\ker A_0\) and \(v'\perp\ker A_0\), and put \(\beta=\|B_0\|\). Then
\[
\begin{aligned}
&(v+v')^{\mathsf T}(A_0+\eta B_0)(v+v')\\
&\quad\ge(\delta_0-\eta\beta)|v'|^2-2\eta\beta|v||v'|\\
&\qquad+\eta\delta_0|v|^2 .
\end{aligned}
\]
This quadratic form in \((|v|,|v'|)\) is nonnegative when \(\delta_0-\eta\beta\ge0\) and \(\eta^2\beta^2\le(\delta_0-\eta\beta)\eta\delta_0\), that is, when \(\eta(\beta^2+\delta_0\beta)\le\delta_0^2\); this condition implies the first. \(\square\)

**Lemma 2.5.** Let \(N_0>0\), \(\varepsilon_2>0\) and \(0<\delta\le1\). There is \(\eta_0>0\), depending on \(\lambda,\rho,N_0,\varepsilon_2,\delta\), such that for every \(p\in\mathcal B_{N_0}\) with \(\Xi(p)\le-\varepsilon_2\) and every \(r>0\) with \(r^2\ge1/\eta_0\),
\[
D-(1+\delta)\,\Xi\,E-r^2\,\Xi\,B\succeq0 .
\]

*Proof.* As \(-\Xi\ge\varepsilon_2\) and \(B\succeq0\), the matrix is at least \(r^2\bigl(\varepsilon_2B+r^{-2}B_0\bigr)\) with \(B_0=D-(1+\delta)\Xi E\). Apply Lemma 2.4 to \(A_0=\varepsilon_2B\), whose kernel is spanned by \(\theta'\) (Lemma 2.3). By Lemma 2.3, \(\theta'^{\mathsf T}B_0\theta'=\Xi-(1+\delta)\Xi=-\delta\Xi\ge\delta\varepsilon_2\), so \(v^{\mathsf T}B_0v\ge(\delta\varepsilon_2/|\theta'|^2)|v|^2\) on \(\ker A_0\); and \(v^{\mathsf T}A_0v\ge\varepsilon_2\beta_B|v|^2\) for \(v\perp\ker A_0\), where \(\beta_B>0\) is the smaller of the two positive eigenvalues of \(B\). On \(\mathcal B_{N_0}\), \(|u_i|\le N_0\), so \(\|D\|\le N_0\) and \(|\Xi|\le2N_0\); with \(\|E\|\le1\) and \(\delta\le1\), \(\|B_0\|\le5N_0\). So Lemma 2.4 applies with \(\delta_0=\min(\delta\varepsilon_2/|\theta'|^2,\varepsilon_2\beta_B)\) and \(\eta_0=\delta_0^2/(25N_0^2+5N_0\delta_0)\). \(\square\)

## 4. The derivative of the quantity

From here on, the notation is that of Theorem 2.1, with \(T=1-\varepsilon\). Fix \(\delta=\frac12\) and \(R>0\), and put
\[
\begin{aligned}
r(u)&=R\,(\varepsilon+u)^{(1+\delta)/2},\\
J_u(p)&=\Phi\bigl(r(u)\,\Xi(p)\bigr).
\end{aligned}
\]

**Lemma 2.6.** The functions \(F_u\) have the following properties, for \(u\in[0,T]\).

1. \(F_u\) takes values in \(\mathcal B_N\); its derivatives in \((x,y)\) of all orders and its derivative in \(u\) exist, are continuous and are bounded on \([0,T]\times\mathbf R^{2n}\).
2. \(\partial_uF_{i,u}=\mathcal L_{\hat C}F_{i,u}\) for \(i=1,2,3\).
3. \(\Gamma_{\hat C}(F_{i,u},F_{j,u})=A_{ij}\langle v_i,v_j\rangle\), where \(v_1=\nabla Q_{\varepsilon+u}f(x)\), \(v_2=\nabla Q_{\varepsilon+u}g(y)\), \(v_3=(\nabla Q_{\sigma^2(\varepsilon+u)}h)(\lambda x+\mu y)\), vectors in \(\mathbf R^n\).
4. \(|v_1|\le\frac{I(F_{1,u})}{\sqrt{\varepsilon+u}}\), \(|v_2|\le\frac{I(F_{2,u})}{\sqrt{\varepsilon+u}}\), \(|v_3|\le\frac{I(F_{3,u})}{\sigma\sqrt{\varepsilon+u}}\).

*Proof.* (1) \(Q_t\) maps functions with values in \([\Phi(-N),\Phi(N)]\) to such functions, and the other statements follow from Proposition 1.2, because the times \(\varepsilon+u\) and \(\sigma^2(\varepsilon+u)\) are at least \(\sigma^2\varepsilon>0\). (2) For \(F_{1,u}\), \(\mathcal L_{\hat C}\) acts on functions of \(x\) alone as \(\frac12\Delta_x\), and \(\partial_tQ_tf=\frac12\Delta Q_tf\) by Proposition 1.2(3); likewise for \(F_{2,u}\). For a \(C^2\) function \(k\) on \(\mathbf R^n\), the Hessian of \(k(\lambda x+\mu y)\) in \((x,y)\) has blocks \(\lambda^2\nabla^2k\), \(\lambda\mu\nabla^2k\), \(\mu^2\nabla^2k\), so
\[
\begin{aligned}
&\mathcal L_{\hat C}\bigl[k(\lambda x+\mu y)\bigr]\\
&\quad=\tfrac12(\lambda^2+2\rho\lambda\mu+\mu^2)\Delta k=\tfrac12\sigma^2\Delta k,
\end{aligned}
\]
evaluated at \(\lambda x+\mu y\); and \(\partial_uQ_{\sigma^2(\varepsilon+u)}h=\frac12\sigma^2\Delta Q_{\sigma^2(\varepsilon+u)}h\). (3) The gradients in \((x,y)\) are \((v_1,0)\), \((0,v_2)\) and \((\lambda v_3,\mu v_3)\), and \(\hat C\) maps them to \((v_1,\rho v_1)\), \((\rho v_2,v_2)\) and \(((\lambda+\rho\mu)v_3,(\rho\lambda+\mu)v_3)\); the inner products give the entries of \(A\). (4) Proposition 1.7, with \(t=\varepsilon+u\) and with \(t=\sigma^2(\varepsilon+u)\). \(\square\)

**Lemma 2.7.** Let \(\varepsilon_2>0\), let \(\eta_0\) be as in Lemma 2.5 with \(N_0=N\), this \(\varepsilon_2\) and \(\delta=\frac12\), and suppose \(r(u)^2\ge1/\eta_0\). At every \((u;x,y)\) with \(\Xi(F_u(x,y))\le-\varepsilon_2\),
\[
\partial_u\bigl(J_u\circ F_u\bigr)-\mathcal L_{\hat C}\bigl(J_u\circ F_u\bigr)\le0 .
\]

*Proof.* Write \(\Gamma_{ij}=\Gamma_{\hat C}(F_{i,u},F_{j,u})\). By Lemma 1.4 and Lemma 2.6(2), the left side equals
\[
(\partial_uJ_u)(F_u)-\frac12\sum_{i,j}\partial_i\partial_jJ_u(F_u)\,\Gamma_{ij}.
\]
Write \(v_{i,c}\) for the coordinates of \(v_i\) and \(w_c=(v_{1,c},v_{2,c},v_{3,c})^{\mathsf T}\), \(c=1,\dots,n\). By Lemma 2.6(3) and Lemma 2.2, with \(\tilde w_c=\mathcal I^{-1}w_c\) and \(r=r(u)\),
\[
\begin{aligned}
&\sum_{i,j}\partial_i\partial_jJ_u\,\Gamma_{ij}\\
&\quad=\sum_cw_c^{\mathsf T}(A\odot\nabla^2J_u)w_c\\
&\quad=r\varphi(r\Xi)\sum_c\tilde w_c^{\mathsf T}(D-r^2\Xi B)\tilde w_c .
\end{aligned}
\]
By Lemma 2.6(4),
\[
\begin{aligned}
\sum_c\tilde w_c^{\mathsf T}E\tilde w_c&=\sum_i\frac{E_{ii}|v_i|^2}{I(F_{i,u})^2}\\
&\le\frac\kappa{\varepsilon+u},
\end{aligned}
\]
with \(\kappa=(\lambda+\mu+\sigma\cdot\sigma^{-2})/(1+\sigma^{-1})=1\). Further \(\partial_uJ_u=r'(u)\,\Xi\,\varphi(r\Xi)\le0\), and a nonpositive number is at most its product with a number in \([0,1]\); so
\[
\begin{aligned}
(\partial_uJ_u)(F_u)&\le r'(u)\,\Xi\,\varphi(r\Xi)\\
&\quad\cdot(\varepsilon+u)\sum_c\tilde w_c^{\mathsf T}E\tilde w_c .
\end{aligned}
\]
Since \(2r'(u)(\varepsilon+u)=(1+\delta)r(u)\), the left side of the lemma is at most
\[
-\frac r2\varphi(r\Xi)\sum_c\tilde w_c^{\mathsf T}M\tilde w_c,
\]
where \(M=D-(1+\delta)\Xi E-r^2\Xi B\) is the matrix of Lemma 2.5; so it is at most \(0\). \(\square\)

## 5. Proof of Theorem 2.1

Let \(c_0=\varepsilon^{(1+\delta)/2}=r(0)/r(T)\) and \(\varepsilon_2=\frac12c_0\varepsilon_1\). Take \(\eta_0\) from Lemma 2.5 with \(N_0=N\) and these \(\varepsilon_2,\delta\), and choose \(R\) with \(R^2\varepsilon^{1+\delta}\ge1/\eta_0\); then \(r(u)^2\ge r(0)^2\ge1/\eta_0\) for all \(u\). Put \(H_u=J_u\circ F_u\). By Lemma 2.6(1), and because \(J_u(p)\) and its derivatives are continuous and bounded on \([0,T]\times\mathcal B_N\), the family \(H_u\) satisfies the hypotheses of Proposition 1.5 on every interval \([0,s]\subseteq[0,T]\).

*Step 1.* Suppose that for some \(s\in[0,T]\), \(\Xi(F_u)\le-\varepsilon_2\) everywhere for all \(u\in[0,s]\). Then \(\Xi(F_s)\le-2\varepsilon_2\) everywhere. Indeed, for fixed \((x,y)\), the function \(u\mapsto Q^{\hat C}_{s-u}H_u(x,y)\) on \([0,s]\) has the derivative \(Q^{\hat C}_{s-u}(\partial_uH_u-\mathcal L_{\hat C}H_u)(x,y)\le0\), by Proposition 1.5 and Lemma 2.7. Comparing its values at \(u=s\) and \(u=0\),
\[
\begin{aligned}
\Phi\bigl(r(s)\Xi(F_s(x,y))\bigr)&\le Q^{\hat C}_s\bigl(J_0\circ F_0\bigr)(x,y)\\
&\le\Phi\bigl(-r(0)\varepsilon_1\bigr),
\end{aligned}
\]
because \(\Xi(F_0)\le-\varepsilon_1\) everywhere. So \(\Xi(F_s)\le-\varepsilon_1r(0)/r(s)\le-\varepsilon_1c_0=-2\varepsilon_2\).

*Step 2.* \(\Xi\) is Lipschitz on \(\mathcal B_N\), since \((\Phi^{-1})'=1/I\le1/\varphi(N)\) on \([\Phi(-N),\Phi(N)]\), and \(\partial_uF_u\) is bounded (Lemma 2.6(1)). So there is \(\tau_0>0\) with \(|\Xi(F_u)-\Xi(F_{u'})|\le\varepsilon_2\) everywhere whenever \(|u-u'|\le\tau_0\).

*Step 3.* Let \(S\) be the set of \(s\in[0,T]\) such that \(\Xi(F_u)\le-\varepsilon_2\) everywhere for all \(u\in[0,s]\). Then \(0\in S\), because \(\varepsilon_2\le\varepsilon_1\). If \(s\in S\), then \(\Xi(F_s)\le-2\varepsilon_2\) by Step 1, so \(\Xi(F_u)\le-\varepsilon_2\) for \(u\in[s,s+\tau_0]\cap[0,T]\) by Step 2, and \(\min(s+\tau_0,T)\in S\). Hence \(T\in S\), and Step 1 with \(s=T\) gives \(\Xi(F_T(0,0))\le-2\varepsilon_2<0\). Since \(F_T(0,0)\) is the triple of integrals in the theorem, this proves Theorem 2.1. \(\square\)

The choice of the exponent in \(r(u)\) is explained by half-spaces (Exercise 2.2): for \(f=\mathbf 1_{\{x_1\le a\}}\), \(g=\mathbf 1_{\{y_1\le b\}}\) and \(h=\mathbf 1_{\{z_1\le c\}}\), \(\Xi(F_u)=(\lambda a+\mu b-c)/\sqrt{\varepsilon+u}\), so \(J_u(F_u)\) is constant in \(u\) for the exponent \(\frac12\). The larger exponent \(\frac{1+\delta}2\) leaves the margin \(-\delta\Xi\) on the kernel of \(B\) used in Lemma 2.5.

## 6. Exercises

**2.1** (easy). Show that \((\lambda-\mu)^2<\sigma^2<1\) for \(-1<\rho<1\), and that \(\sigma\to1\) as \(\rho\to1\).

**2.2** (easy). For \(f=\mathbf 1_{\{x_1\le a\}}\), \(g=\mathbf 1_{\{y_1\le b\}}\), \(h=\mathbf 1_{\{z_1\le c\}}\) on \(\mathbf R^n\), show that \(F_{1,u}(x,y)=\Phi((a-x_1)/\sqrt{\varepsilon+u})\), compute \(F_{2,u},F_{3,u}\), and show \(\Xi(F_u)=(\lambda a+\mu b-c)/\sqrt{\varepsilon+u}\).

**2.3** (medium). Let \(A_0=\operatorname{diag}(1,0)\) and \(B_0=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\). Show that \(A_0+\eta B_0\succeq0\) exactly for \(0\le\eta\le1\), and compute the bound of Lemma 2.4 for this pair.

**2.4** (easy). In the setting of Exercise 2.2, show that \(J_u(F_u)=\Phi\bigl(R(\varepsilon+u)^{\delta/2}(\lambda a+\mu b-c)\bigr)\). Deduce that \(J_u(F_u)\) does not depend on \((x,y)\), is nonincreasing in \(u\) when \(\lambda a+\mu b<c\), and would be constant in \(u\) for \(\delta=0\).

## 7. Solutions

**2.1.** \(\sigma^2-(\lambda-\mu)^2=2\lambda\mu(1+\rho)>0\), and \(1-\sigma^2=(\lambda+\mu)^2-\sigma^2\), which is \(2\lambda\mu(1-\rho)>0\). As \(\rho\to1\), \(\sigma^2\to(\lambda+\mu)^2=1\).

**2.2.** \(Q_tf(x)\) is the \(\gamma_n\)-measure of \(\{w:x_1+\sqrt t\,w_1\le a\}\), which is \(\Phi((a-x_1)/\sqrt t)\); likewise \(F_{2,u}=\Phi((b-y_1)/\sqrt{\varepsilon+u})\) and \(F_{3,u}=\Phi((c-\lambda x_1-\mu y_1)/(\sigma\sqrt{\varepsilon+u}))\). Then
\[
\begin{aligned}
\sqrt{\varepsilon+u}\;\Xi(F_u)&=\lambda(a-x_1)+\mu(b-y_1)\\
&\quad-(c-\lambda x_1-\mu y_1)\\
&=\lambda a+\mu b-c .
\end{aligned}
\]

**2.3.** \(A_0+\eta B_0=\bigl(\begin{smallmatrix}1&\eta\\\eta&\eta\end{smallmatrix}\bigr)\) has determinant \(\eta-\eta^2\) and trace \(1+\eta\), so it is positive semidefinite exactly for \(0\le\eta\le1\). Here \(\ker A_0\) is spanned by \(e_2\), \(e_2^{\mathsf T}B_0e_2=1\), \(e_1^{\mathsf T}A_0e_1=1\), so \(\delta_0=1\), and \(\|B_0\|=(1+\sqrt5)/2\); the bound is \(1/(\|B_0\|^2+\|B_0\|)\), which equals \(1/(2+\sqrt5)\approx0.236\).

**2.4.** By Exercise 2.2, \(\Xi(F_u)=(\lambda a+\mu b-c)(\varepsilon+u)^{-1/2}\), so \(r(u)\Xi(F_u)=R(\varepsilon+u)^{\delta/2}(\lambda a+\mu b-c)\), which does not involve \((x,y)\). If \(\lambda a+\mu b-c<0\), it decreases as \(u\) increases, and so does its image under \(\Phi\); for \(\delta=0\) it is constant.

## References

- [NP] J. Neeman and G. Paouris, *An interpolation proof of Ehrhard's inequality*, arXiv:1605.07233, Sections 2 and 4. https://arxiv.org/abs/1605.07233
