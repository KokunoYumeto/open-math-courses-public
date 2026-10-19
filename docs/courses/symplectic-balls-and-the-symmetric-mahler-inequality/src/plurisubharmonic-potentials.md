# Plurisubharmonic potentials

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On an open subset of \(\mathbf C^n\), a real function \(\varphi\) determines the two-form \(dd^c\varphi\). When \(\varphi\) is plurisubharmonic, the form \(dd^c(|z|^2+\varphi)\) is symplectic, and the balls of the next lesson are found in such forms. This lesson proves the facts about these potentials that the course uses: their behaviour under holomorphic maps and on complex lines (Lemmas 3.1 to 3.3), the potentials \(|f|^2\) and \(\log|f|^2\) of holomorphic maps (Lemma 3.5), a smooth maximum (Lemma 3.7), and radial potentials (Lemma 3.9). The conventions follow [OpenAI-SB, Section 2]. Forms, pullbacks and exterior derivatives are those of [Forms, flows and Moser's method](forms-flows-and-moser-s-method.md).

## 1. The operator \(d^c\)

Identify \(\mathbf C^n\) with \(\mathbf R^{2n}\) by writing \(z=u+ix\) with \(u,x\in\mathbf R^n\). Multiplication by \(i\) acts on real tangent vectors by \(\partial_{u_j}\mapsto\partial_{x_j}\) and \(\partial_{x_j}\mapsto-\partial_{u_j}\). A map \(G\) from an open subset of \(\mathbf C^n\) to \(\mathbf C^{n'}\) is *holomorphic* if it is smooth and its derivative is complex-linear at every point, \(DG(iX)=i\,DG(X)\). For \(n=n'=1\) these are the holomorphic functions of one variable, which are infinitely differentiable by Theorem 3.3.3 of Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50); compositions of holomorphic maps are holomorphic.

For a smooth real function \(\varphi\), define the one-form \(d^c\varphi\) and the two-form \(dd^c\varphi\) by
\[
\begin{aligned}
d^c\varphi(X)&=-\tfrac14\,d\varphi(iX),\\
dd^c\varphi&=d(d^c\varphi).
\end{aligned}
\]
In coordinates,
\[
d^c\varphi=\tfrac14\sum_j\bigl(\partial_{u_j}\varphi\,dx_j-\partial_{x_j}\varphi\,du_j\bigr).
\]
For \(\varphi=|z|^2\) this gives the standard primitive and form
\[
\begin{aligned}
\lambda_0&=d^c|z|^2=\tfrac12\sum_j(u_j\,dx_j-x_j\,du_j),\\
\omega_0&=dd^c|z|^2=\sum_jdu_j\wedge dx_j.
\end{aligned}
\]
With \((q,p)=(u,x)\) this is the standard symplectic form of the first lesson, and \(B^{2n}(c)=\{z:\pi|z|^2<c\}\). Every \(dd^c\varphi\) is closed (Exercise 2.1), and \(d^c(\psi\circ\varphi)=\psi'(\varphi)\,d^c\varphi\) for a smooth function \(\psi\) of one real variable, by the chain rule.

**Lemma 3.1.** Let \(G\) be holomorphic and \(\varphi\) smooth on the target. Then \(G^*(d^c\varphi)=d^c(\varphi\circ G)\) and \(G^*(dd^c\varphi)=dd^c(\varphi\circ G)\).

**Proof.** For a tangent vector \(X\), \((G^*d^c\varphi)(X)=d^c\varphi(DG(X))\), which is \(-\frac14d\varphi(i\,DG(X))\), and \(i\,DG(X)=DG(iX)\), so this equals \(-\frac14d(\varphi\circ G)(iX)\). The second identity follows by Lemma 2.1(b). \(\square\)

**Lemma 3.2.** In one variable \(\zeta=s+it\), \(dd^ch=\frac14\Delta h\,ds\wedge dt\) for every smooth real \(h\). If \(\phi\) is holomorphic, then \(\Delta|\phi|^2=4|\phi'|^2\) and \(dd^c|\phi|^2=|\phi'|^2\,ds\wedge dt\).

**Proof.** \(d^ch=\frac14(h_s\,dt-h_t\,ds)\), and \(d\) of this is \(\frac14(h_{ss}+h_{tt})\,ds\wedge dt\). For \(\phi=a+ib\), the functions \(a,b\) are harmonic and satisfy \(|\nabla a|^2=|\nabla b|^2=|\phi'|^2\) by the Cauchy–Riemann equations; so \(\Delta(a^2+b^2)=2|\nabla a|^2+2|\nabla b|^2=4|\phi'|^2\). \(\square\)

**Lemma 3.3** (complex lines). For a smooth real function \(\varphi\) near \(z\in\mathbf C^n\) and \(X\in\mathbf C^n\),
\[
dd^c\varphi(z)(X,iX)=\tfrac14\,\Delta_\zeta\,\varphi(z+\zeta X)\big|_{\zeta=0},
\]
the Laplacian taken in the complex variable \(\zeta\).

**Proof.** Apply Lemma 3.1 to the holomorphic map \(G(\zeta)=z+\zeta X\) and Lemma 3.2 to \(\varphi\circ G\). At \(\zeta=0\) the vectors \(\partial_s\), \(\partial_t\) are mapped to \(X\) and \(iX\). \(\square\)

## 2. Plurisubharmonic functions

A smooth real function \(\varphi\) on an open set of \(\mathbf C^n\) is *plurisubharmonic* if \(dd^c\varphi(X,iX)\ge0\) for all points and all tangent vectors \(X\), that is, if its restrictions to complex lines are subharmonic in the sense \(\Delta_\zeta\varphi(z+\zeta X)\ge0\).

**Lemma 3.4.** If \(\varphi\) is plurisubharmonic, then \(\omega=dd^c(|z|^2+\varphi)\) is a symplectic form with \(\omega(X,iX)\ge|X|^2\).

**Proof.** The form is closed. For \(X=(a,b)\) in the coordinates \((u,x)\), \(iX=(-b,a)\) and \(\omega_0(X,iX)=|a|^2+|b|^2=|X|^2\). Hence \(\omega(X,iX)\ge|X|^2\), and \(\omega(X,\cdot)=0\) forces \(X=0\). \(\square\)

For holomorphic functions of one variable we use the operators \(\partial_\zeta=\frac12(\partial_s-i\partial_t)\) and \(\partial_{\bar\zeta}=\frac12(\partial_s+i\partial_t)\), for which \(\Delta=4\partial_\zeta\partial_{\bar\zeta}\), \(\partial_{\bar\zeta}h=0\) and \(\partial_\zeta h=h'\) if \(h\) is holomorphic, and \(\partial_{\bar\zeta}\bar h=\overline{h'}\).

**Lemma 3.5.** Let \(f=(f_1,\dots,f_m)\) be holomorphic on an open set \(\Omega\subseteq\mathbf C^n\) and \(\tau=|f|^2=\sum_j|f_j|^2\). Then, with \(df(X)\in\mathbf C^m\) the derivative of \(f\) along \(X\),
\[
dd^c\tau(X,iX)=|df(X)|^2\ge0,
\]
and, where \(f\ne0\),
\[
\begin{aligned}
&dd^c\log\tau(X,iX)\\
&\quad=\frac{|f|^2|df(X)|^2-\bigl|\sum_j\overline{f_j}\,df_j(X)\bigr|^2}{|f|^4}\\
&\quad\ge0.
\end{aligned}
\]
So \(\tau\) is plurisubharmonic, and so is \(\log\tau\) where \(f\) has no zero.

**Proof.** Fix \(z\), \(X\) and put \(h(\zeta)=f(z+\zeta X)\), a holomorphic map of one variable with \(h'(0)=df(X)\). By Lemma 3.3 we need \(\frac14\Delta\) of \(|h|^2\) and of \(\log|h|^2\) at \(0\). First \(\partial_{\bar\zeta}|h|^2=\sum_jh_j\overline{h_j'}\) and \(\partial_\zeta\partial_{\bar\zeta}|h|^2=|h'|^2\). Next
\[
\begin{aligned}
\partial_{\bar\zeta}\log|h|^2&=\frac{\sum_jh_j\overline{h_j'}}{|h|^2},\\
\partial_\zeta\partial_{\bar\zeta}\log|h|^2&=\frac{|h'|^2}{|h|^2}-\frac{\bigl|\sum_jh_j\overline{h_j'}\bigr|^2}{|h|^4}.
\end{aligned}
\]
The numerator \(|h|^2|h'|^2-|\sum_j\overline{h_j}h_j'|^2\) is nonnegative by the Cauchy–Schwarz inequality. \(\square\)

**Lemma 3.6.** Let \(\Gamma\) be a smooth function on an open subset of \(\mathbf R^N\) that is convex and nondecreasing in each argument, and let \(h_1,\dots,h_N\) be plurisubharmonic with \((h_1,\dots,h_N)\) in the domain of \(\Gamma\). Then \(\Gamma(h_1,\dots,h_N)\) is plurisubharmonic.

**Proof.** On a complex line, with the subscripts of \(\Gamma\) denoting partial derivatives and \(\nabla\) the gradient in \((s,t)\),
\[
\begin{aligned}
\Delta\,\Gamma(h)&=\sum_j\Gamma_j\,\Delta h_j\\
&\quad+\sum_{i,j}\Gamma_{ij}\,\langle\nabla h_i,\nabla h_j\rangle.
\end{aligned}
\]
The first sum is nonnegative because \(\Gamma_j\ge0\) and \(\Delta h_j\ge0\); the second is the sum over the two real directions of a quadratic form in the positive semidefinite Hessian of \(\Gamma\). \(\square\)

**Lemma 3.7** (smooth maximum). Let \(\vartheta\) be a smooth even nonnegative function supported in \((-1,1)\) with \(\int\vartheta=1\), and put
\[
\begin{aligned}
\rho(s)&=\int_{\mathbf R}|s-t|\,\vartheta(t)\,dt,\\
\operatorname{rmax}(h,p)&=\tfrac12\bigl(h+p+\rho(h-p)\bigr).
\end{aligned}
\]
Then \(\rho\) is smooth and convex, \(|\rho'|\le1\), and \(\rho(s)=|s|\) for \(|s|\ge1\). Hence \(\operatorname{rmax}\) is smooth, convex, nondecreasing in each argument, and equal to \(\max(h,p)\) when \(|h-p|\ge1\).

**Proof.** Splitting the integral at \(t=s\) gives \(\rho'(s)=2\Theta(s)-1\) with \(\Theta(s)=\int_{-\infty}^s\vartheta\), a smooth function with values in \([0,1]\); so \(\rho\) is smooth, \(|\rho'|\le1\), and \(\rho''=2\vartheta\ge0\). For \(s\ge1\), \(|s-t|=s-t\) on the support of \(\vartheta\), and \(\int t\vartheta(t)\,dt=0\) by evenness, so \(\rho(s)=s\); likewise \(\rho(s)=-s\) for \(s\le-1\). The partial derivatives of \(\operatorname{rmax}\) are \(\frac12(1\pm\rho'(h-p))\ge0\), and convexity is inherited from \(\rho\). \(\square\)

## 3. Two explicit potentials

**Lemma 3.8.** Let \(b\in\mathbf R^n\), \(\ell(z)=\sum_jb_jz_j\), and let \(\phi\) be holomorphic on an open set \(D\subseteq\mathbf C\) with coordinate \(\zeta=v+it\). On \(\{z:\ell(z)\in D\}\),
\[
\begin{aligned}
&dd^c|\phi\circ\ell|^2\\
&\quad=|\phi'(\ell(z))|^2\;d\langle b,u\rangle\wedge d\langle b,x\rangle.
\end{aligned}
\]

**Proof.** The map \(\ell\) is complex-linear, hence holomorphic, and \(\ell(z)=\langle b,u\rangle+i\langle b,x\rangle\) because \(b\) is real. By Lemmas 3.1 and 3.2, \(dd^c|\phi\circ\ell|^2=\ell^*(|\phi'|^2\,dv\wedge dt)\), and \(\ell^*dv=d\langle b,u\rangle\), \(\ell^*dt=d\langle b,x\rangle\). \(\square\)

**Lemma 3.9** (radial potentials). Let \(r>0\) and let \(\Psi\) be smooth on an open interval containing \([0,r^2]\), with \(\Psi'>0\) and \(\frac d{dt}\bigl(t\Psi'(t)\bigr)>0\) there. Put \(R(z)=\sqrt{\Psi'(|z|^2)}\,z\) on \(B_r=\{|z|<r\}\). Then \(R^*\lambda_0=d^c\Psi(|z|^2)\) and \(R^*\omega_0=dd^c\Psi(|z|^2)\), and \(R\) is a diffeomorphism of \(B_r\) onto the ball \(B^{2n}(\pi r^2\Psi'(r^2))\).

**Proof.** Write \(R=\varrho z\) with \(\varrho=\sqrt{\Psi'(|z|^2)}\). Then
\[
\begin{aligned}
R^*\lambda_0&=\tfrac12\sum_j\bigl(\varrho u_j\,d(\varrho x_j)\\
&\qquad-\varrho x_j\,d(\varrho u_j)\bigr)=\varrho^2\lambda_0,
\end{aligned}
\]
the terms containing \(d\varrho\) cancelling, and \(\varrho^2\lambda_0=\Psi'(|z|^2)\,d^c|z|^2=d^c\Psi(|z|^2)\). Lemma 2.1(b) gives \(R^*\omega_0=d(R^*\lambda_0)=dd^c\Psi(|z|^2)\). The map \(R\) is smooth, also at \(0\), and maps the sphere \(|z|=\sqrt t\) onto the sphere of squared radius \(t\Psi'(t)\), which increases strictly from \(0\) to \(r^2\Psi'(r^2)\); so \(R\) is a bijection of \(B_r\) onto that ball. Its derivative at \(z\ne0\) is multiplication by \(\varrho\) on vectors orthogonal to \(z\) and by \(\frac d{d\sqrt t}\sqrt{t\Psi'(t)}>0\) in the direction of \(z\), and \(DR(0)=\sqrt{\Psi'(0)}\,I\); by Lemma 2.2, \(R\) is a diffeomorphism. \(\square\)

## 4. Exercises

**3.1** (easy). Compute \(d^c\varphi\) and \(dd^c\varphi\) for \(\varphi=|z_1|^2\) on \(\mathbf C^2\), and check Lemma 3.3 for it.

**3.2** (easy). Show that \(\log(|z|^2+\delta)\) is plurisubharmonic on \(\mathbf C^n\) for \(\delta>0\), using Lemma 3.5.

**3.3** (medium). Show that \((\operatorname{Re}z_1)^2\) and \(\operatorname{Re}(z_1^2)\) are plurisubharmonic on \(\mathbf C^n\), and that \(-(\operatorname{Re}z_1)^2\) is not.

**3.4** (easy). For \(\Psi(t)=t+\mu\log(t+\delta)\) with \(\mu,\delta>0\), check the hypotheses of Lemma 3.9 on every interval \([0,r^2]\).

## 5. Solutions

**3.1.** \(d^c\varphi=\frac12(u_1\,dx_1-x_1\,du_1)\) and \(dd^c\varphi=du_1\wedge dx_1\). For \(X=(X_1,X_2)\), \(dd^c\varphi(X,iX)=|X_1|^2\), and \(\varphi(z+\zeta X)=|z_1+\zeta X_1|^2\) has Laplacian \(4|X_1|^2\) in \(\zeta\).

**3.2.** \(|z|^2+\delta=|f|^2\) for the holomorphic map \(f=(\sqrt\delta,z_1,\dots,z_n)\), which has no zero.

**3.3.** For \(\varphi=(\operatorname{Re}z_1)^2=u_1^2\), the restriction to a complex line is \(\bigl(\operatorname{Re}(z_1+\zeta X_1)\bigr)^2\), the square of a real-linear function of \(\zeta\) with gradient of length \(|X_1|\); its Laplacian is \(2|X_1|^2\ge0\). The restriction of \(\operatorname{Re}(z_1^2)\) is the real part of a holomorphic function of \(\zeta\), hence harmonic, so \(dd^c\operatorname{Re}(z_1^2)=0\). The restrictions of \(-u_1^2\) have Laplacian \(-2|X_1|^2<0\) when \(X_1\ne0\).

**3.4.** \(\Psi'(t)=1+\mu/(t+\delta)>0\) and \(\frac d{dt}(t\Psi'(t))=1+\mu\delta/(t+\delta)^2>0\) on \((-\delta,\infty)\).

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
