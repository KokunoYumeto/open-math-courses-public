# The estimate at the free edge

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lesson on the differentiated height equation led to a linear equation
\[
u_{tt}+A\,u_{ss}+B\,u_t+C\,u_s=f
\]
on a rectangle, in which the coefficient \(A\) changes its sign: the equation is elliptic where \(A>0\) and hyperbolic where \(A<0\). This lesson proves an estimate for the first derivatives of \(u\) by the mean squares of \(u\) and \(f\), on a rectangle with three edges in the elliptic region and a fourth edge, the *free edge*, at which nothing is assumed: \(A\) may be negative there, and no condition on \(u\) is imposed. What makes this possible is the structure of \(C\) found in that lesson, \(C=(l+1)A_s\) up to a multiple of \(A\), together with a sign condition on the derivatives of \(A\) where \(A\) is small.

- The identity obtained by multiplying the equation by \(m\,u_s+n\,u_t\) and integrating by parts (Lemma 2.1).
- With a weight that vanishes at the free edge, the resulting quadratic form is positive where \(A\) is negative or small (Proposition 3.1).
- Where \(A\) is positive, an elliptic estimate with a weaker weight (Proposition 4.1).
- The estimate (Theorem 5.1).

The lesson follows [OpenAI-I, Section 3, the lemma on the free cap edge], formulated for a general equation with these properties; all constants are tracked. It uses only integration by parts on a rectangle and the inequality \(2xy\le\delta x^2+y^2/\delta\).

## 1. The assumptions

Let \(T>0\), \(s_0<b\), and \(\Omega=[-T,T]\times[s_0,b]\) in the plane with the coordinates \(t,s\). Let \(d=b-s\), the distance to the edge \(s=b\), and \(d_{\max}=b-s_0\). Let \(A,B,C,f,u\) be smooth functions on a neighbourhood of \(\Omega\) with
\[
u_{tt}+A\,u_{ss}+B\,u_t+C\,u_s=f .
\]
We assume, with numbers \(l\ge0\), \(M_0\ge1\), \(0<T_1<T\), \(s_0<s_1<b\), \(\alpha_0>0\), \(0<\varepsilon\le1\), \(a_0>0\) and \(\theta_0>0\):

**(A1)** \(C=(l+1)A_s+A\omega\) with a continuous function \(\omega\), and \(|A|,|A_t|,|A_s|,|B|,|B_s|,|\omega|\le M_0\) on \(\Omega\).

**(A2)** \(A\ge\alpha_0\) at the points of \(\Omega\) with \(|t|\ge T_1\) or \(s\le s_1\).

**(A3)** \(16\,\varepsilon^2T^2M_0\le1\), and at the points of \(\Omega\) with \(|A|\le a_0\),
\[
\Theta:=-(l+\tfrac12)A_s+\tfrac\varepsilon2\,t\,A_t\ \ge\ \theta_0 .
\]

Assumption (A2) says that the equation is elliptic near the edges \(t=\pm T\) and \(s=s_0\). Nothing is assumed at the edge \(s=b\). Assumption (A3) concerns the curve where \(A\) changes its sign: across it, \(A\) decreases in the direction of increasing \(s\), or it increases in the direction away from \(t=0\).

Let \(\Omega_0=[-T_1,T_1]\times[s_1,b_0]\) with \(s_1<b_0<b\). We write \(\|w\|^2=\iint_\Omega w^2\,dt\,ds\) and \(|\nabla u|^2=u_t^2+u_s^2\).

## 2. The multiplier identity

**Lemma 2.1.** Let \(m,n\) be smooth functions on a neighbourhood of \(\Omega\) that vanish on the edge \(s=b\) and in a neighbourhood of the other three edges. Then
\[
\begin{gathered}
\iint_\Omega f\,(m\,u_s+n\,u_t)=\iint_\Omega Q[u],\\
Q[u]=Q_{tt}u_t^2+Q_{ss}u_s^2+Q_{ts}u_tu_s,
\end{gathered}
\]
where
\[
\begin{aligned}
Q_{tt}&=\tfrac12(m_s-n_t)+Bn,\\
Q_{ss}&=-\tfrac12(Am)_s+\tfrac12(An)_t+Cm,\\
Q_{ts}&=-m_t+Bm-(An)_s+Cn .
\end{aligned}
\]

**Proof.** The product \((u_{tt}+Au_{ss}+Bu_t+Cu_s)(mu_s+nu_t)\) is equal to
\[
\begin{aligned}
&Q_{tt}u_t^2+Q_{ss}u_s^2+Q_{ts}u_tu_s\\
&\quad+\partial_t\bigl(m\,u_tu_s+\tfrac12n\,u_t^2-\tfrac12An\,u_s^2\bigr)\\
&\quad+\partial_s\bigl(-\tfrac12m\,u_t^2+\tfrac12Am\,u_s^2+An\,u_su_t\bigr).
\end{aligned}
\]
This is checked by carrying out the differentiations: for example
\[
\begin{aligned}
u_{tt}\,m\,u_s&=\partial_t(mu_tu_s)-m_tu_tu_s\\
&\quad-\partial_s(\tfrac12mu_t^2)+\tfrac12m_su_t^2,\\
Au_{ss}\,n\,u_t&=\partial_s(Anu_su_t)-(An)_su_su_t\\
&\quad-\partial_t(\tfrac12Anu_s^2)+\tfrac12(An)_tu_s^2,
\end{aligned}
\]
and similarly for the other products. Integrate over \(\Omega\). The integrals of the two derivatives are integrals over the edges of expressions that contain \(m\) or \(n\) as a factor, and these vanish on all four edges. \(\blacksquare\)

## 3. Positivity where \(A\) is negative or small

Fix \(p=8\). Let \(\lambda>0\), to be chosen, and
\[
\begin{gathered}
I(t,s)=\int_0^tB(r,s)\,dr,\\
W=d^{\,p}\,e^{-\lambda s+I},\qquad H_0=\lambda+\frac pd .
\end{gathered}
\]
Then \(W_t=BW\) and \(W_s=-(H_0-I_s)W\), and \(|I_s|\le TM_0\). Let \(Q^W_{tt},Q^W_{ss},Q^W_{ts}\) be the functions of Lemma 2.1 for \(m=-W\) and \(n=\varepsilon tW\). A computation gives
\[
\begin{aligned}
Q^W_{tt}/W&=\tfrac12(H_0-I_s)-\tfrac\varepsilon2+\tfrac\varepsilon2tB,\\
Q^W_{ss}/W&=\Theta-\tfrac12H_0A+A\beta,\\
Q^W_{ts}/W&=\varepsilon t\,\bigl(lA_s+A\omega-AI_s+H_0A\bigr),
\end{aligned}
\]
with \(\beta=\tfrac12I_s+\tfrac\varepsilon2(1+tB)-\omega\). Indeed \(-m_t+Bm=W_t-BW=0\); \(-\tfrac12(Am)_s=\tfrac12A_sW-\tfrac12A(H_0-I_s)W\); \(\tfrac12(An)_t=\tfrac\varepsilon2(tA_t+A+tAB)W\); and \(Cm=-(l+1)A_sW-A\omega W\). The term \(-(l+1)A_s\) of \(C\), together with \(\tfrac12A_s\), gives the term \(-(l+\tfrac12)A_s\) of \(\Theta\). Put
\[
\begin{gathered}
\beta_0=M_0(T+1)+1,\\
c_J=M_0(l+M_0+TM_0),\\
\Theta_1=(l+1+T)M_0,
\end{gathered}
\]
so that \(|\beta|\le\beta_0\), \(|lA_s+A\omega-AI_s|\le c_J\) and \(|\Theta|\le\Theta_1\).

**Proposition 3.1.** Assume (A1) and (A3), and let \(\alpha_0>0\) be the number of (A2). Let
\[
\begin{gathered}
\lambda=\max\{\lambda_1,\lambda_2,\lambda_3,\lambda_4\},\\
\lambda_1=2+4TM_0,\qquad\lambda_2=8\beta_0,\\
\lambda_3=\frac{16T^2c_J^2}{\theta_0},\qquad\lambda_4=\frac{8(\Theta_1+\theta_0)}{a_0},
\end{gathered}
\]
and
\[
\begin{gathered}
c_1=\min\{\gamma_1,\gamma_2,\gamma_3\},\\
\gamma_1=\frac{a_0}{d_{\max}},\qquad\gamma_2=\frac{\alpha_0}{d_{\max}},\\
\gamma_3=\frac{\theta_0}{4(\lambda d_{\max}+p+d_{\max}\beta_0)}.
\end{gathered}
\]
Then at every point of \(\Omega\) with \(s<b\) and \(A\le c_1d\), and for all real \(\xi,\eta\),
\[
\begin{aligned}
&Q^W_{tt}\xi^2+Q^W_{ss}\eta^2+Q^W_{ts}\xi\eta\\
&\quad\ge c_2W(\xi^2+\eta^2),\\
&c_2=\min\bigl\{\tfrac\lambda8,\tfrac{\theta_0}2\bigr\}.
\end{aligned}
\]

**Proof.** Since \(H_0\ge\lambda\ge2+4TM_0\), we have \(Q^W_{tt}/W\ge\tfrac12H_0-\tfrac12(1+2TM_0)\ge\tfrac14H_0\). By \(|Q^W_{ts}\xi\eta|\le\tfrac12Q^W_{tt}\xi^2+(Q^W_{ts})^2\eta^2/(2Q^W_{tt})\), the quadratic form is at least
\[
\tfrac12Q^W_{tt}\,\xi^2+\Bigl(Q^W_{ss}-\frac{(Q^W_{ts})^2}{2Q^W_{tt}}\Bigr)\eta^2 .
\]
The first coefficient is at least \(\tfrac18H_0W\ge\tfrac\lambda8W\). For the second, \(|Q^W_{ts}|/W\le\varepsilon T(c_J+H_0|A|)\), so
\[
\begin{aligned}
\frac{(Q^W_{ts})^2}{2Q^W_{tt}W}&\le\frac{2\varepsilon^2T^2(c_J+H_0|A|)^2}{H_0}\\
&\le4\varepsilon^2T^2\Bigl(\frac{c_J^2}{H_0}+H_0A^2\Bigr).
\end{aligned}
\]
The first of these two terms is at most \(4T^2c_J^2/\lambda\le\tfrac14\theta_0\). By (A3) and \(|A|\le M_0\), the second is at most \(\tfrac14H_0|A|\). Hence
\[
\begin{aligned}
&\frac1W\Bigl(Q^W_{ss}-\frac{(Q^W_{ts})^2}{2Q^W_{tt}}\Bigr)\\
&\quad\ge\Theta-\tfrac12H_0A-\tfrac14H_0|A|\\
&\qquad-|A|\beta_0-\tfrac14\theta_0 .
\end{aligned}
\]
We show that the right side is at least \(\tfrac12\theta_0\) where \(A\le c_1d\).

*Where \(A\le0\).* The right side is \(\Theta+\tfrac14H_0|A|-|A|\beta_0-\tfrac14\theta_0\), and this is at least \(\Theta+\tfrac18H_0|A|-\tfrac14\theta_0\), because \(H_0\ge8\beta_0\). If \(|A|\le a_0\), then \(\Theta\ge\theta_0\) by (A3). If \(A<-a_0\), then \(\Theta+\tfrac18H_0|A|\ge-\Theta_1+\tfrac18\lambda a_0\ge\theta_0\). In both cases the right side is at least \(\tfrac34\theta_0\).

*Where \(0<A\le c_1d\).* Then \(A\le c_1d_{\max}\le a_0\), so \(\Theta\ge\theta_0\). Further \(H_0A\le c_1(\lambda d+p)\le c_1(\lambda d_{\max}+p)\) and \(A\beta_0\le c_1d_{\max}\beta_0\). The right side is at least
\[
\begin{aligned}
&\theta_0-\tfrac34c_1(\lambda d_{\max}+p)\\
&\quad-c_1d_{\max}\beta_0-\tfrac14\theta_0\ \ge\ \tfrac12\theta_0
\end{aligned}
\]
by the choice of \(c_1\). \(\blacksquare\)

The order of the choices is: \(\varepsilon\) in (A3), then \(\lambda\), then \(c_1\). Where \(A\) is definitely negative the term \(-\tfrac12H_0A\) is favourable and large; near the curve \(A=0\) the positivity comes from \(\Theta\); and on the side \(A>0\) the unfavourable term \(-\tfrac12H_0A\) is small only as long as \(A\le c_1d\), because \(H_0\) contains \(p/d\).

## 4. An elliptic estimate where \(A\) is positive

Let \(T_2=\tfrac12(T_1+T)\), \(T_3=\tfrac12(T_2+T)\), \(s_2=\tfrac12(s_0+s_1)\), \(s_3=\tfrac12(s_0+s_2)\). Fix smooth functions \(\zeta,\chi\) of \((t,s)\) with values in \([0,1]\), products of a function of \(t\) and a function of \(s\), such that

- \(\zeta=1\) where \(|t|\le T_1\) and \(s\ge s_1\), and \(\zeta=0\) where \(|t|\ge T_2\) or \(s\le s_2\);
- \(\chi=1\) where \(|t|\le T_2\) and \(s\ge s_2\), and \(\chi=0\) where \(|t|\ge T_3\) or \(s\le s_3\).

Let \(c_\zeta\) be a bound for the first derivatives of \(\zeta\) and \(\chi\); it depends only on \(T-T_1\) and \(s_1-s_0\). Fix a smooth function \(\varphi\) on \(\mathbb R\) with values in \([0,1]\), equal to \(0\) on \((-\infty,\tfrac12]\) and to \(1\) on \([1,\infty)\), with \(|\varphi'|\le3\).

**Proposition 4.1.** Assume (A1), and let \(c_1>0\). Let \(\Omega_e\) be the set of the points of \(\Omega\) with \(A\ge c_1d\) and \(\chi=1\). There is a constant \(C_e\), depending only on \(l,M_0,d_{\max},c_1,c_\zeta\), such that
\[
\iint_{\Omega_e}d^{\,p-1}\,|\nabla u|^2\le C_e\bigl(\|u\|^2+\|f\|^2\bigr).
\]

**Proof.** Let \(v=d^{\,p-2}\chi^2\,\varphi(A/(c_1d))^2\) for \(s<b\), and \(v=0\) on the edge \(s=b\). Where \(v>0\) we have \(A>\tfrac12c_1d\). The product \(-vu\,(u_{tt}+Au_{ss}+Bu_t+Cu_s)\) is equal to
\[
\begin{aligned}
&v\,(u_t^2+Au_s^2)+u\,(v_t-vB)\,u_t\\
&\quad+u\,((Av)_s-vC)\,u_s\\
&\quad-\partial_t(vuu_t)-\partial_s(vAuu_s).
\end{aligned}
\]
Integrate over \([-T,T]\times[s_0,b-\eta]\) and let \(\eta\to0\). The integrals of the two derivatives vanish in the limit: \(v=0\) near the three edges, and on the line \(s=b-\eta\) the function \(v\) is at most \(\eta^{p-2}\). So
\[
\begin{aligned}
&\iint v\,(u_t^2+Au_s^2)\\
&\quad=-\iint vuf-\iint u\,(v_t-vB)\,u_t\\
&\qquad-\iint u\,((Av)_s-vC)\,u_s .
\end{aligned}
\]
*Derivatives of \(v\).* Where \(\varphi'(A/(c_1d))\ne0\) we have \(A\le c_1d\). The derivatives of \(A/(c_1d)\) are \(A_t/(c_1d)\) and \(A_s/(c_1d)+A/(c_1d^2)\), so there they are at most \(M_0/(c_1d)\) and \((M_0/c_1+1)/d\) in absolute value. Since \(v\) is \(d^{\,p-2}\) times the square of \(\chi\varphi\),
\[
|v_t|+|v_s|\le c_3\sqrt v\;d^{(p-2)/2}\,(1+d^{-1}),
\]
with \(c_3\) depending on \(p,c_\zeta,M_0,c_1\); the derivative of \(d^{\,p-2}\) contributes \((p-2)v/d\le(p-2)\sqrt v\,d^{(p-2)/2}d^{-1}\).

*The error terms.* Where \(v>0\), using \(A>\tfrac12c_1d\), \(|C|\le(l+2)M_0^2\) and \(v\le d^{\,p-2}\),
\[
\begin{aligned}
&\frac{(v_t-vB)^2}v\\
&\quad\le2c_3^2d^{\,p-2}(1+d^{-1})^2+2M_0^2d^{\,p-2},\\
&\frac{((Av)_s-vC)^2}{Av}\\
&\quad\le\frac{3(A_s^2+C^2)\,v}A+\frac{3A\,v_s^2}v\\
&\quad\le\frac{6(l+3)^2M_0^4}{c_1}\,d^{\,p-3}\\
&\qquad+3M_0c_3^2\,d^{\,p-2}(1+d^{-1})^2 .
\end{aligned}
\]
Since \(p=8\), all these are bounded on \(\Omega\) by a constant \(c_4\) depending on \(l,M_0,d_{\max},c_1,c_3\). By the inequality \(2xy\le x^2+y^2\),
\[
\begin{aligned}
&\bigl|u\bigl((v_t-vB)u_t+((Av)_s-vC)u_s\bigr)\bigr|\\
&\quad\le\tfrac12v\,(u_t^2+Au_s^2)+c_4u^2 .
\end{aligned}
\]
Also \(|vuf|\le\tfrac12d_{\max}^{\,p-2}(u^2+f^2)\). Therefore
\[
\begin{aligned}
&\tfrac12\iint v\,(u_t^2+Au_s^2)\\
&\quad\le\bigl(c_4+\tfrac12d_{\max}^{\,p-2}\bigr)\bigl(\|u\|^2+\|f\|^2\bigr).
\end{aligned}
\]
Where \(\chi=1\) and \(A\ge c_1d\), we have \(v=d^{\,p-2}\ge d^{\,p-1}/d_{\max}\) and \(vA\ge c_1d^{\,p-1}\). \(\blacksquare\)

The weight \(d^{\,p-2}\) lets the ellipticity degenerate at the free edge at the rate \(A\ge c_1d\).

## 5. The estimate

**Theorem 5.1.** Assume (A1), (A2) and (A3), and let \(s_1<b_0<b\). There is a constant \(C_*\), depending only on the numbers \(l,M_0,T,T_1,s_0,s_1,b,b_0,\alpha_0,\varepsilon,a_0,\theta_0\), such that
\[
\iint_{\Omega_0}\bigl(u_t^2+u_s^2\bigr)\ \le\ C_*\iint_\Omega\bigl(u^2+f^2\bigr).
\]

**Proof.** Take \(\lambda,c_1,c_2\) from Proposition 3.1, and apply Lemma 2.1 with \(m=-\zeta W\) and \(n=\varepsilon t\zeta W\); they vanish at \(s=b\) because \(W\) does, and near the other edges because \(\zeta\) does. Differentiating the products shows that the functions of Lemma 2.1 are
\[
\begin{aligned}
Q_{tt}&=\zeta Q^W_{tt}-\tfrac12(\zeta_s+\varepsilon t\zeta_t)W,\\
Q_{ss}&=\zeta Q^W_{ss}+\tfrac12A(\zeta_s+\varepsilon t\zeta_t)W,\\
Q_{ts}&=\zeta Q^W_{ts}+(\zeta_t-\varepsilon tA\zeta_s)W .
\end{aligned}
\]
Let \(\Omega_-\) be the set of the points of \(\Omega\) with \(A<c_1d\) and \(\Omega_+\) the set of those with \(A\ge c_1d\). The derivatives of \(\zeta\) vanish outside the set where \(|t|\ge T_1\) or \(s\le s_1\); there \(A\ge\alpha_0\ge c_1d_{\max}\) by (A2) and the choice of \(c_1\). So the terms with derivatives of \(\zeta\) live in \(\Omega_+\). On \(\Omega\), \(W\le E_1d^{\,p}\) with \(E_1=e^{\lambda(|s_0|+|b|)+TM_0}\), and \(H_0W\le(\lambda d_{\max}+p)E_1d^{\,p-1}\). With the formulas of Section 3, all of \(|Q^W_{tt}|,|Q^W_{ss}|,|Q^W_{ts}|\) and the terms with derivatives of \(\zeta\) are at most \(c_5d^{\,p-1}\), with a constant \(c_5\) depending on the numbers of the statement. Lemma 2.1 and Proposition 3.1 give
\[
\begin{aligned}
&c_2\iint_{\Omega_-}\zeta W|\nabla u|^2\\
&\quad\le\iint_\Omega|f|\,\zeta W(1+T)|\nabla u|\\
&\qquad+3c_5\iint_{\Omega_+,\ \zeta>0}d^{\,p-1}|\nabla u|^2 .
\end{aligned}
\]
In the first integral on the right, the function \(|f|W(1+T)|\nabla u|\) is at most
\[
\begin{gathered}
\tfrac12c_2W|\nabla u|^2+\frac{(1+T)^2Wf^2}{2c_2}\quad\text{on }\Omega_-,\\
d^{\,p-1}|\nabla u|^2+\frac{(1+T)^2W^2f^2}{d^{\,p-1}}\quad\text{on }\Omega_+,
\end{gathered}
\]
where \(W^2/d^{\,p-1}\le E_1^2d_{\max}^{\,p+1}\). Since \(\chi=1\) where \(\zeta>0\), Proposition 4.1 bounds the integrals over \(\Omega_+\). So
\[
\tfrac12c_2\iint_{\Omega_-}\zeta W|\nabla u|^2\le c_6\bigl(\|u\|^2+\|f\|^2\bigr).
\]
On \(\Omega_0\) we have \(\zeta=\chi=1\), \(d\ge b-b_0\) and \(W\ge w_0=(b-b_0)^pe^{-\lambda(|s_0|+|b|)-TM_0}\). Hence
\[
\begin{aligned}
&\iint_{\Omega_0}|\nabla u|^2\\
&\quad\le\frac1{w_0}\iint_{\Omega_-}\zeta W|\nabla u|^2\\
&\qquad+(b-b_0)^{1-p}\iint_{\Omega_e}d^{\,p-1}|\nabla u|^2,
\end{aligned}
\]
and both terms are bounded by a constant times \(\|u\|^2+\|f\|^2\). \(\blacksquare\)

## 6. Exercises

**6.1.** Verify the formulas for \(Q^W_{tt}\), \(Q^W_{ss}\) and \(Q^W_{ts}\) of Section 3.

**6.2.** Let \(A=t^2-\tfrac14-s\) on \(\Omega=[-2,2]\times[-1,\tfrac12]\), so that the equation is elliptic below the parabola \(s=t^2-\tfrac14\) and hyperbolic above it, and let \(B=0\), \(C=(l+1)A_s=-(l+1)\). Show that (A1), (A2) and (A3) hold, with \(T_1=\tfrac32\), \(s_1=-\tfrac12\) and suitable numbers \(M_0,\alpha_0,\varepsilon,a_0,\theta_0\).

**6.3.** In the situation of Exercise 6.2, replace \(C\) by \(+(l+1)\). Which of the assumptions fails, and where does the proof of Proposition 3.1 break down?

**6.4.** Show that in Lemma 2.1 the assumption that \(m\) and \(n\) vanish on the edge \(s=b\) cannot simply be dropped: for \(A=-1\), \(B=C=0\), find the terms on the edge that appear, and say why they have no sign.

## 7. Solutions

**6.1.** With \(m=-W\): \(m_s=(H_0-I_s)W\) and \(m_t=-BW\). With \(n=\varepsilon tW\): \(n_t=\varepsilon W+\varepsilon tBW\). So
\[
\begin{aligned}
Q_{tt}&=\tfrac12(H_0-I_s)W-\tfrac\varepsilon2(1+tB)W\\
&\quad+\varepsilon tBW .
\end{aligned}
\]
Next,
\[
\begin{aligned}
-\tfrac12(Am)_s&=\tfrac12A_sW-\tfrac12A(H_0-I_s)W,\\
\tfrac12(An)_t&=\tfrac\varepsilon2(tA_t+A+tAB)W,
\end{aligned}
\]
and \(Cm=-CW\) with \(C=(l+1)A_s+A\omega\); the sum of the three is \(W\) times
\[
\begin{aligned}
&-(l+\tfrac12)A_s+\tfrac\varepsilon2tA_t-\tfrac12H_0A\\
&\quad+A\bigl(\tfrac12I_s+\tfrac\varepsilon2(1+tB)-\omega\bigr).
\end{aligned}
\]
Finally \(-m_t+Bm=0\), \(-(An)_s=-\varepsilon t(A_s-A(H_0-I_s))W\) and \(Cn=\varepsilon tCW\); the sum is \(\varepsilon tW\) times \(lA_s+A\omega+A(H_0-I_s)\).

**6.2.** (A1): \(\omega=0\), and \(|A|\le4-\tfrac14+1<5\), \(|A_t|=|2t|\le4\), \(A_s=-1\), so \(M_0=5\) works. (A2): for \(|t|\ge\tfrac32\), \(A\ge\tfrac94-\tfrac14-\tfrac12=\tfrac32\); for \(s\le-\tfrac12\), \(A\ge t^2+\tfrac14\ge\tfrac14\); so \(\alpha_0=\tfrac14\). (A3): \(\Theta=(l+\tfrac12)+\varepsilon t^2\ge l+\tfrac12\) at every point, so \(\theta_0=l+\tfrac12\) with any \(a_0\), for every \(\varepsilon\) with \(16\,\varepsilon^2\cdot4\cdot5\le1\), for example \(\varepsilon=\tfrac1{18}\).

**6.3.** For \(A=t^2-\tfrac14-s\) and \(C=+(l+1)=-(l+1)A_s\), the decomposition (A1) would need \(A\omega=2(l+1)\), and \(\omega\) is unbounded near the curve \(A=0\). In the proof, the term \(Cm\) then contributes \(-(l+1)W\) instead of \(+(l+1)W\) to \(Q^W_{ss}\), and \(Q^W_{ss}/W\) is \(-(l+\tfrac32)+\varepsilon t^2\) plus terms that vanish with \(A\): it is negative on the part of the curve \(A=0\) with \(t^2<(l+\tfrac32)/\varepsilon\). The sign of the first-order term across the curve decides.

**6.4.** For \(A=-1\), \(B=C=0\) the equation is the wave equation \(u_{tt}-u_{ss}=f\). The integral of \(\partial_s(-\tfrac12mu_t^2+\tfrac12Amu_s^2+Anu_su_t)\) contributes on \(s=b\) the integral over \(t\) of \(-\tfrac12m(u_t^2+u_s^2)-n\,u_su_t\). Since \(|u_su_t|\le\tfrac12(u_t^2+u_s^2)\), this has the sign of \(-m\) if \(|n|\le|m|\), and no sign otherwise; and \(u\) and its derivatives on that edge are not controlled by anything. In the hyperbolic region an edge can be free only if the multiplier is adapted to it. The weight \(d^{\,p}\) avoids the question by vanishing there.

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026
