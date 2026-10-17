# Gaussian heat semigroups and a gradient bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Ehrhard's inequality is the Gaussian analogue of the Brunn–Minkowski inequality. Write \(\gamma_n\) for the standard Gaussian measure on \(\mathbf R^n\), \(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\), and \(\Phi(x)=\int_{-\infty}^x\varphi\), an increasing bijection of \(\mathbf R\) onto \((0,1)\); put \(\Phi^{-1}(0)=-\infty\) and \(\Phi^{-1}(1)=+\infty\).

## The theorem

**Theorem A** (Ehrhard). Let \(K,L\subseteq\mathbf R^n\) be closed convex sets with \(\gamma_n(K),\gamma_n(L)\in(0,1)\), and \(0\le\lambda\le1\). Then
\[
\begin{aligned}
&\Phi^{-1}\bigl(\gamma_n(\lambda K+(1-\lambda)L)\bigr)\\
&\quad\ge\lambda\,\Phi^{-1}(\gamma_n(K))\\
&\qquad+(1-\lambda)\,\Phi^{-1}(\gamma_n(L)).
\end{aligned}
\]

Ehrhard proved it with a Gaussian symmetrization [E]; Latała extended it to the case in which only one of the sets is convex, and Borell to arbitrary Borel sets. For parallel half-spaces \(\{\langle e,x\rangle\le a\}\) and \(\{\langle e,x\rangle\le b\}\), with \(|e|=1\), both sides equal \(\lambda a+(1-\lambda)b\). The left side can be \(+\infty\): for the half-planes \(\{x_1\le0\}\) and \(\{x_1\ge0\}\) and \(0<\lambda<1\), \(\lambda K+(1-\lambda)L=\mathbf R^n\).

This course proves Theorem A by the interpolation method of Neeman and Paouris [NP]: a quantity built from the three functions \(\mathbf 1_K\), \(\mathbf 1_L\) and \(\mathbf 1_{\lambda K+(1-\lambda)L}\), smoothed by Gaussian semigroups, is monotone in time. The course uses the heat semigroup in place of the Ornstein–Uhlenbeck semigroup of [NP], proves the gradient bound it needs from an elementary rearrangement argument, and carries out the approximation steps for convex sets. van Handel gave another proof, by a stochastic game [vH].

**The course.**

1. This lesson: Gaussian heat semigroups, their smoothing and the heat equation, a moving function under the semigroup, and the gradient bound \(|\nabla Q_tf|\le t^{-1/2}I(Q_tf)\).
2. [A quantity monotone along the heat flow](a-quantity-monotone-along-the-heat-flow.md): the function \(J=\Phi(r\Xi)\), a matrix inequality, and the monotonicity theorem.
3. [Ehrhard's inequality for convex sets](ehrhards-inequality-for-convex-sets.md): from smooth functions to convex sets, and the proof of Theorem A.

**What the course assumes.** Multivariable calculus and linear algebra (positive semidefinite matrices); measure and integration as in Fremlin's *Measure Theory* in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), cited by number: the dominated convergence theorem (123C), differentiating through an integral (123D), Fubini's theorem (252B), and the linear change of variables (263A).

## 1. Notation

Let \(C\) be a positive definite symmetric \(d\times d\) matrix. The Gaussian measure \(\gamma_C\) on \(\mathbf R^d\) has density
\[
g_C(w)=\frac{e^{-\langle w,C^{-1}w\rangle/2}}{(2\pi)^{d/2}(\det C)^{1/2}},
\]
and \(\gamma_d=\gamma_{I_d}\). For a bounded measurable \(F:\mathbf R^d\to\mathbf R\) and \(t\ge0\) put
\[
Q^C_tF(z)=\int F(z+\sqrt t\,w)\,d\gamma_C(w),
\]
and \(Q_t=Q^{I_d}_t\). For \(t>0\), the change of variables \(y=z+\sqrt t\,w\) (263A) gives
\[
Q^C_tF(z)=\int F(y)\,g_{tC}(y-z)\,dy .
\]
If \(C=\sigma^2I_d\), then \(Q^C_t=Q_{\sigma^2t}\). For \(H\in C^2(\mathbf R^d)\) put
\[
\begin{aligned}
\mathcal L_CH&=\frac12\sum_{i,j}C_{ij}\,\partial_i\partial_jH,\\
\Gamma_C(H_1,H_2)&=\langle\nabla H_1,C\nabla H_2\rangle .
\end{aligned}
\]
\(C^2_b(\mathbf R^d)\) is the space of twice continuously differentiable functions that are bounded with bounded first and second derivatives. Finally, \(I(p)=\varphi(\Phi^{-1}(p))\) for \(0<p<1\) and \(I(0)=I(1)=0\); \(I\) is continuous on \([0,1]\) and \(I(1-p)=I(p)\).

## 2. Gaussian integration by parts

**Lemma 1.1.** Let \(\psi\in C^1(\mathbf R^d)\) satisfy \(|\psi(w)|+|\nabla\psi(w)|\le ae^{b|w|}\) for some constants \(a,b\). Then, for each \(i\),
\[
\int w_i\,\psi(w)\,d\gamma_C(w)=\sum_jC_{ij}\int\partial_j\psi\,d\gamma_C .
\]

*Proof.* \(\partial_jg_C(w)=-(C^{-1}w)_j\,g_C(w)\). Integrating by parts in the variable \(w_j\), with Fubini's theorem (252B) for the other variables and no boundary terms because of the Gaussian decay,
\[
\begin{aligned}
\int\partial_j\psi\,g_C\,dw&=-\int\psi\,\partial_jg_C\,dw\\
&=\int(C^{-1}w)_j\,\psi\,g_C\,dw .
\end{aligned}
\]
Multiply by \(C_{ij}\) and sum over \(j\); \(\sum_jC_{ij}(C^{-1}w)_j=w_i\). \(\square\)

## 3. Smoothing and the heat equation

**Proposition 1.2.** Let \(F\) be bounded and measurable. On \((0,\infty)\times\mathbf R^d\), the function \((t,z)\mapsto Q^C_tF(z)\) has continuous partial derivatives of all orders in \(z\) and a continuous derivative in \(t\), and:

1. every derivative \(\partial^\alpha_zQ^C_tF\) is bounded by \(c_\alpha t^{-|\alpha|/2}\sup|F|\), with \(c_\alpha\) depending only on \(\alpha\) and \(C\);
2. \(\nabla Q^C_tF(z)\) is \(t^{-1/2}\) times the integral of \(F(z+\sqrt t\,w)\,C^{-1}w\) against \(\gamma_C(w)\);
3. \(\partial_tQ^C_tF=\mathcal L_CQ^C_tF\).

*Proof.* For \(t>0\), \(k(t,z,y)=g_{tC}(y-z)\) is infinitely differentiable in \((t,z)\). Each derivative \(\partial_t^a\partial^\alpha_zk\) is a polynomial in \(y-z\), \(t^{-1/2}\) and the entries of \(C^{-1}\) times \(k\); on a set \(\{t_0\le t\le t_1,\ |z|\le z_1\}\) it is bounded by a polynomial in \(|y|\) times \(e^{-c|y|^2}\) for some \(c>0\), which is integrable. So all these derivatives may be taken under the integral sign (123D), and they are continuous by dominated convergence (123C). For the bound in (1), \(\partial^\alpha_zk(t,z,y)=t^{-|\alpha|/2}P_\alpha((y-z)/\sqrt t)\,k\) with a polynomial \(P_\alpha\), and the substitution \(y=z+\sqrt t\,w\) gives \(|\partial^\alpha_zQ^C_tF(z)|\le\sup|F|\,t^{-|\alpha|/2}\int|P_\alpha|\,d\gamma_C\). For (2), \(\nabla_zk=t^{-1}C^{-1}(y-z)\,k\). For (3), with \(v=y-z\),
\[
\partial_t\log g_{tC}(v)=-\frac d{2t}+\frac{\langle v,C^{-1}v\rangle}{2t^2},
\]
and, with \(c_i=(C^{-1}v)_i\),
\[
\frac{\partial_i\partial_jg_{tC}(v)}{g_{tC}(v)}=\frac{c_ic_j}{t^2}-\frac{(C^{-1})_{ij}}t ,
\]
so \(\frac12\sum_{i,j}C_{ij}\partial_i\partial_jg_{tC}=\partial_tg_{tC}\); since \(\partial_{z_i}\partial_{z_j}k=(\partial_i\partial_jg_{tC})(y-z)\), integrating against \(F(y)\) gives (3). \(\square\)

**Proposition 1.3.** Let \(H\in C^2_b(\mathbf R^d)\). For every \(z\), \(\tau\mapsto Q^C_\tau H(z)\) is continuously differentiable on \([0,\infty)\) with derivative \(Q^C_\tau(\mathcal L_CH)(z)\). In particular \(|Q^C_\tau H(z)-H(z)|\le\tau\sup|\mathcal L_CH|\).

*Proof.* For \(\tau\ge\tau_0>0\), the derivative of \(H(z+\sqrt\tau\,w)\) in \(\tau\) is \(\langle\nabla H(z+\sqrt\tau\,w),w\rangle/(2\sqrt\tau)\), bounded by \(\sup|\nabla H|\,|w|/(2\sqrt{\tau_0})\). By 123D and Lemma 1.1 with \(\psi(w)=\partial_iH(z+\sqrt\tau\,w)\), \(\partial_j\psi=\sqrt\tau\,\partial_j\partial_iH(z+\sqrt\tau\,w)\),
\[
\begin{aligned}
\frac d{d\tau}Q^C_\tau H(z)&=\frac12\sum_{i,j}C_{ij}\,Q^C_\tau(\partial_i\partial_jH)(z)\\
&=Q^C_\tau(\mathcal L_CH)(z),
\end{aligned}
\]
the factors \(\sqrt\tau\) cancelling.
The right side is continuous on \([0,\infty)\) by dominated convergence, because \(\mathcal L_CH\) is bounded and continuous, and \(\tau\mapsto Q^C_\tau H(z)\) is continuous at \(0\) for the same reason. By the mean value theorem, the derivative at \(0\) exists and equals \(\mathcal L_CH(z)\), and the bound follows. \(\square\)

## 4. A moving function under the semigroup

**Lemma 1.4** (chain rule). Let \(U\subseteq\mathbf R^k\) be open, \(\Psi\in C^2(U)\), and \(F=(F_1,\dots,F_k)\in C^2(\mathbf R^d,U)\). Then
\[
\begin{aligned}
\mathcal L_C(\Psi\circ F)={}&\sum_i\Psi_i\,\mathcal L_CF_i\\
&+\frac12\sum_{i,j}\Psi_{ij}\,\Gamma_C(F_i,F_j),
\end{aligned}
\]
where \(\Psi_i=\partial_i\Psi(F)\) and \(\Psi_{ij}=\partial_i\partial_j\Psi(F)\).

*Proof.* \(\partial_a(\Psi\circ F)=\sum_i\Psi_i\,\partial_aF_i\), and
\[
\begin{aligned}
\partial_b\partial_a(\Psi\circ F)={}&\sum_i\Psi_i\,\partial_b\partial_aF_i\\
&+\sum_{i,j}\Psi_{ij}\,\partial_aF_i\,\partial_bF_j .
\end{aligned}
\]
Multiply by \(\frac12C_{ab}\) and sum over \(a,b\). \(\square\)

**Proposition 1.5.** Let \(0\le a<b\), and let \(H\) be a function on \([a,b]\times\mathbf R^d\), written \(H_u(z)\), such that \(H_u\in C^2_b(\mathbf R^d)\) for each \(u\), and \(\partial_uH_u\), \(\nabla H_u\) and \(\nabla^2H_u\) exist, are continuous on \([a,b]\times\mathbf R^d\) and are bounded there. Then for every \(z\), \(u\mapsto Q^C_{b-u}H_u(z)\) is continuously differentiable on \([a,b]\), with derivative
\[
\begin{aligned}
&\frac d{du}Q^C_{b-u}H_u(z)\\
&\quad=Q^C_{b-u}\bigl(\partial_uH_u-\mathcal L_CH_u\bigr)(z).
\end{aligned}
\]

*Proof.* For \(u\) and \(u+\eta\) in \([a,b]\),
\[
\begin{aligned}
&Q^C_{b-u-\eta}H_{u+\eta}-Q^C_{b-u}H_u\\
&\quad=Q^C_{b-u-\eta}(H_{u+\eta}-H_u)\\
&\qquad+\bigl(Q^C_{b-u-\eta}H_u-Q^C_{b-u}H_u\bigr).
\end{aligned}
\]
By the mean value theorem, \((H_{u+\eta}-H_u)(y)/\eta\) is bounded by \(\sup|\partial_uH|\) and tends to \(\partial_uH_u(y)\), locally uniformly in \(y\) by the uniform continuity of \(\partial_uH\) on compact sets. So the first term divided by \(\eta\), which is the integral of \((H_{u+\eta}-H_u)(z+\sqrt{b-u-\eta}\,w)/\eta\) against \(\gamma_C\), tends to \(Q^C_{b-u}(\partial_uH_u)(z)\) by dominated convergence. The second term divided by \(\eta\) tends to \(-Q^C_{b-u}(\mathcal L_CH_u)(z)\) by Proposition 1.3. The derivative \(Q^C_{b-u}(\partial_uH_u-\mathcal L_CH_u)(z)\) is continuous in \(u\), again by dominated convergence. \(\square\)

## 5. The gradient bound

**Lemma 1.6** (rearrangement). Let \(G:\mathbf R\to[0,1]\) be measurable and \(p=\int G\,d\gamma_1\). Then
\[
\int s\,G(s)\,d\gamma_1(s)\le I(p).
\]

*Proof.* If \(p=0\) or \(p=1\), then \(G=0\) or \(G=1\) almost everywhere and both sides are \(0\). Otherwise let \(a=\Phi^{-1}(1-p)\), so that \(\gamma_1((a,\infty))=p\), and put \(G'=G-\mathbf 1_{(a,\infty)}\), so that \(\int G'\,d\gamma_1=0\). Then
\[
\int s\,G'\,d\gamma_1=\int(s-a)\,G'\,d\gamma_1\le0,
\]
because the integrand is at most \(0\) both for \(s>a\) (where \(G-1\le0\)) and for \(s\le a\) (where \(G\ge0\)). Finally \(\int_a^\infty s\varphi(s)\,ds=\varphi(a)=I(1-p)=I(p)\). \(\square\)

**Proposition 1.7** (gradient bound). Let \(f:\mathbf R^n\to[0,1]\) be measurable and \(t>0\). Then for every \(z\in\mathbf R^n\)
\[
|\nabla Q_tf(z)|\le t^{-1/2}\,I\bigl(Q_tf(z)\bigr).
\]

*Proof.* Let \(e\) be a unit vector and \(O\) an orthogonal matrix with \(Oe_1=e\). By Proposition 1.2(2) with \(C=I_n\), and the change of variables \(w=Ow'\) (263A), under which \(\gamma_n\) is invariant,
\[
\begin{aligned}
&\langle\nabla Q_tf(z),e\rangle\\
&\quad=t^{-1/2}\int f(z+\sqrt t\,Ow')\,w'_1\,d\gamma_n(w').
\end{aligned}
\]
By Fubini's theorem this is \(t^{-1/2}\int s\,G(s)\,d\gamma_1(s)\), where \(G(s)=\int f(z+\sqrt t\,O(s,w''))\,d\gamma_{n-1}(w'')\) takes values in \([0,1]\) and \(\int G\,d\gamma_1=Q_tf(z)\). By Lemma 1.6, \(\langle\nabla Q_tf(z),e\rangle\le t^{-1/2}I(Q_tf(z))\). Taking \(e\) in the direction of \(\nabla Q_tf(z)\) proves the bound. \(\square\)

For \(f=\mathbf 1_{\{x_1\le a\}}\), \(Q_tf(z)=\Phi((a-z_1)/\sqrt t)\) and \(|\nabla Q_tf(z)|=t^{-1/2}\varphi((a-z_1)/\sqrt t)\), which is \(t^{-1/2}I(Q_tf(z))\): the bound is attained by half-spaces. Applied with \(t\) replaced by \(\sigma^2t\), Proposition 1.7 gives \(|\nabla Q_{\sigma^2t}f|\le(\sigma^2t)^{-1/2}I(Q_{\sigma^2t}f)\).

## 6. Exercises

**1.1** (easy). Show that \(I\) is concave on \([0,1]\), with \(I'(p)=-\Phi^{-1}(p)\) and \(I(p)I''(p)=-1\) for \(0<p<1\).

**1.2** (easy). Show that \(Q^C_t\) maps functions with values in an interval \([\alpha,\beta]\) to functions with values in \([\alpha,\beta]\), and that \(\int Q^C_tF\,d\gamma_C\) need not equal \(\int F\,d\gamma_C\) for the heat semigroup (compare \(F=\mathbf 1_{[-1,1]}\) on \(\mathbf R\)).

**1.3** (medium). Show that \(Q^C_sQ^C_t=Q^C_{s+t}\) for \(s,t\ge0\). (Hint: compute \(g_{sC}*g_{tC}\) by completing the square, or by Fourier transforms.)

**1.4** (medium). Let \(f=\mathbf 1_{[a,b]}\) on \(\mathbf R\) with \(a<b\). Verify Proposition 1.7 directly: with \(\alpha=(a-z)/\sqrt t<\beta=(b-z)/\sqrt t\), show \(|\varphi(\alpha)-\varphi(\beta)|\le I(\Phi(\beta)-\Phi(\alpha))\).

## 7. Solutions

**1.1.** With \(x=\Phi^{-1}(p)\), \(dx/dp=1/\varphi(x)\) and \(I=\varphi(x)\), so \(I'(p)=\varphi'(x)/\varphi(x)=-x\) and \(I''(p)=-1/\varphi(x)=-1/I(p)<0\). Continuity at \(0\) and \(1\) gives concavity on \([0,1]\).

**1.2.** \(\gamma_C\) is a probability measure, so \(Q^C_tF(z)\) is an average of values of \(F\). For \(F=\mathbf 1_{[-1,1]}\) and \(C=1\), \(\int Q_tF\,d\gamma_1\) is the probability that \(|X+\sqrt t\,W|\le1\) for independent standard Gaussian \(X,W\); as \(X+\sqrt t\,W\) is centred Gaussian with variance \(1+t\) (Exercise 1.3), this is \(\gamma_1([-a,a])\) with \(a=(1+t)^{-1/2}\), which is smaller than \(\gamma_1([-1,1])\) for \(t>0\).

**1.3.** Write \(\langle a,b\rangle_C=\langle a,C^{-1}b\rangle\). The exponent of \(g_{sC}(y)g_{tC}(x-y)\) is \(-\frac12\) times
\[
\frac{\langle y,y\rangle_C}s+\frac{\langle x-y,x-y\rangle_C}t ,
\]
and completing the square in \(y\), with \(y_0=\frac s{s+t}x\), turns this into
\[
\frac{s+t}{st}\langle y-y_0,y-y_0\rangle_C+\frac{\langle x,x\rangle_C}{s+t} .
\]
Integrating in \(y\) gives \(g_{sC}*g_{tC}=g_{(s+t)C}\). Since \(Q^C_tF(z+y)=\int F(z+x)\,g_{tC}(x-y)\,dx\), Fubini's theorem gives
\[
\begin{aligned}
&Q^C_sQ^C_tF(z)\\
&\quad=\int F(z+x)\,(g_{sC}*g_{tC})(x)\,dx\\
&\quad=Q^C_{s+t}F(z).
\end{aligned}
\]

**1.4.** \(Q_tf(z)=\Phi(\beta)-\Phi(\alpha)=p\) and \((Q_tf)'(z)=t^{-1/2}(\varphi(\alpha)-\varphi(\beta))\). By Lemma 1.6 applied to \(G=\mathbf 1_{[\alpha,\beta]}\) and to \(G(s)=\mathbf 1_{[\alpha,\beta]}(-s)\), \(\pm\int_\alpha^\beta s\varphi(s)\,ds=\pm(\varphi(\alpha)-\varphi(\beta))\le I(p)\).

## References

- [E] A. Ehrhard, *Symétrisation dans l'espace de Gauss*, Mathematica Scandinavica 53 (1983), 281–301. https://journals.msp.org/mscand/article/view/1636
- [NP] J. Neeman and G. Paouris, *An interpolation proof of Ehrhard's inequality*, arXiv:1605.07233. https://arxiv.org/abs/1605.07233
- [vH] R. van Handel, *The Borell–Ehrhard game*, Probability Theory and Related Fields 170 (2018), 555–585; arXiv:1605.00285. https://arxiv.org/abs/1605.00285
- D. H. Fremlin, *Measure Theory*, volumes 1 and 2, in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10).
