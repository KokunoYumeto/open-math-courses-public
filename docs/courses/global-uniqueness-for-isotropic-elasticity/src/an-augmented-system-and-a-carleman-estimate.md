# An augmented system and a Carleman estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Lamé operator couples the components of the displacement through \(\nabla\operatorname{div}u\), so its principal part is not a multiple of the identity. Adjoining the divergence as a fourth unknown \(d\) gives a system whose principal part, after normalization, is the Laplacian on each of the four components; this goes back to Weck's work on unique continuation for the Lamé system (see the account in [Imanuvilov–Yamamoto 2004, Section 1]), and the identities used here keep \(d\) independent of \(u\), with an exact formula for the defect \(\operatorname{div}u-d\) [OpenAI-EL, Section 3]. For the Laplacian there are Carleman estimates with linear weights. With the complex phase \(e^{\tau\theta\cdot x}\), where \(\theta\cdot\theta=0\), they give an estimate that is uniform as \(\tau\to\infty\), and by duality the solvability of the elastic equation with this phase.

- The augmented system (Section 1).
- Semiclassical Sobolev norms (Section 2).
- A Carleman estimate (Section 3).
- Solvability with an exponential phase (Section 4).
- Interior estimates at the scale \(1/\tau\) (Section 5).

We use the Fourier transform \(\widehat v(\xi)=\int e^{-ix\cdot\xi}v(x)\,dx\) and Plancherel's identity \(\|\widehat v\|_{L^2}^2=(2\pi)^3\|v\|_{L^2}^2\), with its polarized form \(\int f\,\overline g\,dx=(2\pi)^{-3}\int\widehat f\,\overline{\widehat g}\,d\xi\), from Sections 1, 2 and 7 of [Fourier transforms, finite spectra and convex separation](course:elliptic-operators-and-boundary-problems/prerequisite-bridges), and the Riesz–Fréchet theorem and orthogonal projections onto closed subspaces of a Hilbert space from the core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20) (Erdman, *Functional Analysis and Operator Algebras: An Introduction*, Section 4.4 and [Theorem 4.5.2](https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf)). The two pairs of moduli are the extensions of Lemma 3.1 of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md); in Sections 1 to 5 we work with one of them and omit the index.

## 1. The augmented system

Put
\[
\begin{gathered}m=\mu,\qquad k=\lambda+\mu,\\ \ell=\lambda+2\mu=k+m .\end{gathered}
\]
The positivity conditions give \(m>0\), \(k>m/3\) and \(\ell>\frac43m\) on \(\mathbb R^3\). For an independent pair \(U=(u,d)\) of a vector field \(u\) and a scalar \(d\), define
\[
\begin{aligned}&R(u,d)_i=m\Delta u_i+k\,\partial_id\\&\quad+C(u)_i+(\partial_i\lambda)\,d,\\&S(u,d)=\ell\Delta d+2\nabla k\cdot\nabla d\\&\quad+2\nabla m\cdot\Delta u+(\Delta\lambda)\,d\\&\quad+2\sum_{i,j}(\partial_i\partial_jm)\,\partial_iu_j,\end{aligned}\tag{1.1}
\]
where \(C(u)_i=\sum_j(\partial_jm)(\partial_ju_i+\partial_iu_j)\), and the scalar operator \(P=m\Delta+\nabla m\cdot\nabla\).

**Lemma 1.1** ([OpenAI-EL, Lemma 3.1]). For every smooth pair \((u,d)\),
\[
\begin{gathered}Lu=R(u,\operatorname{div}u),\\ \operatorname{div}R(u,d)-S(u,d)\\ =P(\operatorname{div}u-d).\end{gathered}\tag{1.2}
\]
In particular, \(Lu=0\) implies \(R(u,\operatorname{div}u)=0\) and \(S(u,\operatorname{div}u)=0\).

*Proof.* With \(v=\operatorname{div}u\),
\[
\begin{aligned}(Lu)_i&=\partial_i(\lambda v)\\&\quad+\sum_j\partial_j\bigl(m(\partial_ju_i+\partial_iu_j)\bigr)\\&=(\partial_i\lambda)v+\lambda\partial_iv+C(u)_i\\&\quad+m\Delta u_i+m\partial_iv,\end{aligned}
\]
which is \(R(u,v)_i\) because \(\lambda+m=k\). For the second identity, differentiate term by term:
\[
\begin{aligned}\sum_i\partial_i(m\Delta u_i)&=\nabla m\cdot\Delta u+m\Delta v,\\ \sum_i\partial_i(k\,\partial_id)&=\nabla k\cdot\nabla d+k\Delta d,\\ \sum_i\partial_iC(u)_i&=2\sum_{i,j}(\partial_i\partial_jm)\,\partial_iu_j\\&\quad+\nabla m\cdot\nabla v+\nabla m\cdot\Delta u,\\ \sum_i\partial_i\bigl((\partial_i\lambda)d\bigr)&=(\Delta\lambda)\,d+\nabla\lambda\cdot\nabla d .\end{aligned}
\]
Adding and subtracting \(S(u,d)\) leaves \(m\Delta v+\nabla m\cdot\nabla v\) plus \((k-\ell)\Delta d+(\nabla\lambda-\nabla k)\cdot\nabla d\), and \(k-\ell=-m\), \(\lambda-k=-m\). So the difference is \(m\Delta(v-d)+\nabla m\cdot\nabla(v-d)\), that is, \(P(v-d)\). If \(Lu=0\), then \(R(u,v)=0\), and the second identity with \(d=v\) gives \(S(u,v)=0\). \(\square\)

**Lemma 1.2** (the normalized augmented operator; [OpenAI-EL, Lemma 3.1]). The operator
\[
\begin{aligned}&\mathcal LU=\Bigl(m^{-1}R(u,d),\\&\quad\ell^{-1}\bigl(S(u,d)\\&\quad-2m^{-1}\nabla m\cdot R(u,d)\bigr)\Bigr)\end{aligned}\tag{1.3}
\]
has the form \(\mathcal L=\Delta\,\mathrm{Id}_4+\sum_{j=1}^3A_j(x)\partial_j+A_0(x)\) with \(A_j\in C^\infty(\mathbb R^3;\mathbb C^{4\times4})\). For the two pairs, \(\mathcal L_1-\mathcal L_2\) is an operator of order at most one whose coefficients have support in \(\overline\Omega\).

*Proof.* \(m^{-1}R(u,d)\) is \(\Delta u+(k/m)\nabla d\) plus \(m^{-1}C(u)+m^{-1}(\nabla\lambda)d\). In the scalar numerator the terms \(2\nabla m\cdot\Delta u\) cancel:
\[
\begin{aligned}&S-2m^{-1}\nabla m\cdot R\\&\quad=\ell\Delta d+\bigl(2\nabla k-2km^{-1}\nabla m\bigr)\cdot\nabla d\\&\qquad+2\sum_{i,j}(\partial_i\partial_jm)\,\partial_iu_j\\&\qquad-2m^{-1}\nabla m\cdot C(u)\\&\qquad+\bigl(\Delta\lambda-2m^{-1}\nabla m\cdot\nabla\lambda\bigr)d .\end{aligned}
\]
After division by \(\ell\), the only second derivatives are \(\Delta u\) and \(\Delta d\). The coefficients of \(\mathcal L_1-\mathcal L_2\) are built from the moduli and their derivatives, which agree on the open set \(\mathbb R^3\setminus\overline\Omega\); so they vanish there. \(\square\)

## 2. Semiclassical Sobolev norms

For \(h>0\), \(s\in\{-1,0,1\}\) and a test function \(v\in C^\infty_c(\mathbb R^3;\mathbb C^N)\) put
\[
\begin{aligned}\|v\|_{H^s_h}^2&=(2\pi)^{-3}\int_{\mathbb R^3}(1+h^2|\xi|^2)^s\\&\qquad\times|\widehat v(\xi)|^2\,d\xi ,\end{aligned}
\]
summing over components. By Plancherel, \(\|v\|_{H^0_h}=\|v\|_{L^2}\) and \(\|v\|_{H^1_h}^2=\|v\|_{L^2}^2+h^2\|\nabla v\|_{L^2}^2\). For Schwartz functions the same formula defines the norms, and the polarized Plancherel identity with Cauchy–Schwarz gives \(|\int F\,\overline v\,dx|\le\|F\|_{H^{-1}_h}\|v\|_{H^1_h}\). Taking \(\widehat v=\widehat F/(1+h^2|\xi|^2)\), a Schwartz function, shows, with the supremum taken over Schwartz functions \(v\),
\[
\begin{aligned}&\|F\|_{H^{-1}_h}\\&\quad=\sup_{\|v\|_{H^1_h}\le1}\Bigl|\int F\,\overline v\,dx\Bigr| .\end{aligned}\tag{2.1}
\]

**Lemma 2.1** (multipliers). Let \(0<h\le1\) and \(F,v\in C^\infty_c(\mathbb R^3)\).

1. \(\|F\|_{H^{-1}_h}\le\|F\|_{L^2}\le\|F\|_{H^1_h}\) and \(\|\partial_jF\|_{H^{-1}_h}\le h^{-1}\|F\|_{L^2}\).
2. For \(a\in C^\infty(\mathbb R^3)\) with bounded first derivatives and bounded values, \(\|av\|_{H^1_h}\le C_a\|v\|_{H^1_h}\) and \(\|aF\|_{H^{-1}_h}\le C_a\|F\|_{H^{-1}_h}\), with \(C_a\) independent of \(h\).
3. For \(\gamma\in\mathbb R^3\), multiplication by \(e^{i\gamma\cdot x/h}\) changes the \(H^{\pm1}_h\) norms by at most the factor \(\bigl(2(1+|\gamma|^2)\bigr)^{1/2}\).

*Proof.* (1) The weights satisfy \((1+h^2|\xi|^2)^{-1}\le1\le1+h^2|\xi|^2\) and \(\xi_j^2/(1+h^2|\xi|^2)\le h^{-2}\), and \(\widehat{\partial_jF}=i\xi_j\widehat F\). (2) The product rule gives
\[
\begin{aligned}&\|av\|^2+h^2\|\nabla(av)\|^2\\&\quad\le2\sup|a|^2\bigl(\|v\|^2+h^2\|\nabla v\|^2\bigr)\\&\qquad+2h^2\sup|\nabla a|^2\,\|v\|^2,\end{aligned}
\]
which proves the first bound, also for Schwartz \(v\). For the second, \(|\int aF\,\overline v|=|\int F\,\overline{\overline av}|\), which is at most \(\|F\|_{H^{-1}_h}\|\overline av\|_{H^1_h}\le C_a\|F\|_{H^{-1}_h}\|v\|_{H^1_h}\), and (2.1) applies. (3) The Fourier transform of \(e^{i\gamma\cdot x/h}v\) is \(\widehat v(\xi-\gamma/h)\), so the new norm has the weight \((1+|h\xi+\gamma|^2)^{\pm1}\) in place of \((1+h^2|\xi|^2)^{\pm1}\). For vectors \(p,q\), \(1+|p+q|^2\le1+2|p|^2+2|q|^2\), which is at most \(2(1+|q|^2)(1+|p|^2)\), and the same with \(-q\); applying this with \(p=h\xi\) and \(q=\pm\gamma\) compares the two weights in both directions. \(\square\)

## 3. A Carleman estimate

A real linear function \(\varphi(x)=\gamma\cdot x\) with \(\gamma\ne0\) is a limiting Carleman weight for the Laplacian, in the sense used by Salo and Tzou, which goes back to Kenig, Sjöstrand and Uhlmann; this is the case of the following estimate used here.

**Hypothesis (CE)** (a Carleman estimate with a convexified linear weight; [Salo–Tzou 2009, Lemma 2.1], with \(s=-1\)). Let \(B\subset\mathbb R^3\) be a bounded open set, \(N\ge1\), \(\gamma\in\mathbb R^3\setminus\{0\}\), \(\varphi(x)=\gamma\cdot x\), and \(\varphi_\varepsilon=\varphi+\frac h{2\varepsilon}\varphi^2\). There are \(\varepsilon_0>0\) and \(C>0\), and for each \(0<\varepsilon\le\varepsilon_0\) a number \(h_0(\varepsilon)>0\), such that
\[
\frac h{\sqrt\varepsilon}\|v\|_{H^1_h}\le C\,\bigl\|e^{\varphi_\varepsilon/h}h^2\Delta\,e^{-\varphi_\varepsilon/h}v\bigr\|_{H^{-1}_h}
\]
for all \(0<h\le h_0(\varepsilon)\) and \(v\in C^\infty_c(B;\mathbb C^N)\).

Salo and Tzou state the estimate for \(-h^2\Delta\), which has the same norm, with the norms \(\|\langle hD\rangle^sv\|_{L^2}\), which are ours, and with the full gain of two derivatives for every real \(s\); the constant \(C\) does not depend on \(\varepsilon\).

Fix a nonzero \(\theta\in\mathbb C^3\) with \(\theta\cdot\theta=0\), and write
\[
\begin{gathered}D_\theta=\theta\cdot\nabla,\\ E_\tau(x)=e^{\tau\theta\cdot x},\quad h=\tau^{-1}.\end{gathered}\tag{3.1}
\]
Writing \(\theta=\alpha+i\beta\) with \(\alpha,\beta\in\mathbb R^3\), the condition \(\theta\cdot\theta=0\) says \(|\alpha|=|\beta|\) and \(\alpha\cdot\beta=0\); so \(\alpha\ne0\). Constants below may depend on the moduli, the ball and \(\theta\), but not on \(\tau\).

**Proposition 3.1** (supported Carleman estimate; [OpenAI-EL, Proposition 3.2]). Let \(B\) be a bounded ball. There are \(C,h_1>0\) such that for \(0<h\le h_1\) and \(U\in C^\infty_c(B;\mathbb C^4)\),
\[
\begin{aligned}&\|E_\tau^{-1}U\|_{H^1_h}\\&\quad\le C\,h\,\|E_\tau^{-1}\mathcal LU\|_{H^{-1}_h}.\end{aligned}\tag{3.2}
\]

*Proof.* Put \(\varphi(x)=-\alpha\cdot x\), so that \(E_\tau^{-1}=e^{\varphi/h}e^{-i\beta\cdot x/h}\), and let \(\varepsilon_0,C,h_0\) be as in Hypothesis (CE) for \(\gamma=-\alpha\), \(N=4\).

*The lower-order terms.* For \(v\in C^\infty_c(B;\mathbb C^4)\) and \(h\le\varepsilon\le\varepsilon_0\), Lemma 1.2 gives
\[
\begin{aligned}&e^{\varphi_\varepsilon/h}h^2\mathcal L\,e^{-\varphi_\varepsilon/h}v\\&\quad=e^{\varphi_\varepsilon/h}h^2\Delta\,e^{-\varphi_\varepsilon/h}v\\&\qquad+h\sum_jA_j\bigl(h\partial_jv-(\partial_j\varphi_\varepsilon)v\bigr)\\&\qquad+h^2A_0v .\end{aligned}
\]
On \(\overline B\), \(\partial_j\varphi_\varepsilon=(1+h\varphi/\varepsilon)\partial_j\varphi\) is bounded independently of \(h\le\varepsilon\). By Lemma 2.1(1), the last two terms have \(H^{-1}_h\) norm at most \(C_1h\|v\|_{H^1_h}\), with \(C_1\) independent of \(\varepsilon\) and \(h\).

*Absorption.* Choose \(\varepsilon\le\varepsilon_0\) with \(CC_1\le\frac1{2\sqrt\varepsilon}\), and let \(h\le\min(\varepsilon,h_0(\varepsilon))\). Hypothesis (CE) and the bound above give
\[
\begin{aligned}&\frac h{\sqrt\varepsilon}\|v\|_{H^1_h}\\&\quad\le C\bigl\|e^{\varphi_\varepsilon/h}h^2\mathcal L\,e^{-\varphi_\varepsilon/h}v\bigr\|_{H^{-1}_h}\\&\qquad+\frac h{2\sqrt\varepsilon}\|v\|_{H^1_h},\end{aligned}
\]
so with \(v=e^{\varphi_\varepsilon/h}U\),
\[
\|e^{\varphi_\varepsilon/h}U\|_{H^1_h}\le2C\sqrt\varepsilon\,h\,\|e^{\varphi_\varepsilon/h}\mathcal LU\|_{H^{-1}_h}.
\]

*Removing the convexification.* Now \(\varepsilon\) is fixed, and \(e^{\varphi_\varepsilon/h}=e^{\varphi/h}e^{\varphi^2/(2\varepsilon)}\). All functions involved are supported in \(\overline B\), where multiplication by \(e^{\pm\varphi^2/(2\varepsilon)}\) agrees with multiplication by \(\zeta e^{\pm\varphi^2/(2\varepsilon)}\) for a fixed \(\zeta\in C^\infty_c(\mathbb R^3)\) equal to one near \(\overline B\). By Lemma 2.1(2) these multipliers are bounded on \(H^{\pm1}_h\) uniformly in \(h\), so
\[
\|e^{\varphi/h}U\|_{H^1_h}\le C'h\,\|e^{\varphi/h}\mathcal LU\|_{H^{-1}_h}.
\]

*Removing the oscillation.* Multiplication by \(e^{-i\beta\cdot x/h}\) changes both norms by bounded factors (Lemma 2.1(3)), and \(E_\tau^{-1}=e^{\varphi/h}e^{-i\beta\cdot x/h}\). This gives (3.2). \(\square\)

## 4. Solvability with an exponential phase

We use the Hermitian inner product \((f,g)=\int f\cdot\overline g\,dx\) on \(L^2(B;\mathbb C^3)\). For the moduli on \(\mathbb R^3\), let \(A_\theta=E_\tau^{-1}L\,E_\tau\), a differential operator with smooth coefficients. Since \(L\) has real coefficients and \(\int(Lw)\cdot v=\int w\cdot(Lv)\) for test functions (by (2.2) of [The displacement-to-traction map](the-displacement-to-traction-map.md), applied twice), the formal adjoint of \(A_\theta\) for \((\cdot,\cdot)\) is
\[
A_\theta^*=e^{\tau\overline\theta\cdot x}L\,e^{-\tau\overline\theta\cdot x}=A_{-\overline\theta},
\]
and \(-\overline\theta\) is again a nonzero null vector.

**Corollary 4.1** ([OpenAI-EL, Corollary 3.3]). Let \(B\) be a bounded ball. There are \(C,h_1>0\) such that for \(0<h\le h_1\):

1. \(\|E_\tau^{-1}w\|_{L^2(B)}\le C\|E_\tau^{-1}Lw\|_{L^2(B)}\) for every \(w\in C^\infty_c(B;\mathbb C^3)\);
2. for every \(f\in L^2(B;\mathbb C^3)\) there is \(z\in L^2(B;\mathbb C^3)\) with \(A_\theta z=f\) in the sense of distributions on \(B\) and \(\|z\|_{L^2(B)}\le C\|f\|_{L^2(B)}\).

*Proof.* (1) Apply Proposition 3.1 to \(U=(w,\operatorname{div}w)\). By Lemma 1.1, \(R(w,\operatorname{div}w)=Lw\) and \(S(w,\operatorname{div}w)=\operatorname{div}(Lw)\), so the two components of \(\mathcal LU\) are \(m^{-1}Lw\) and \(\ell^{-1}(\operatorname{div}(Lw)-2m^{-1}\nabla m\cdot Lw)\). With \(F=E_\tau^{-1}Lw\in C^\infty_c(B)\),
\[
E_\tau^{-1}\operatorname{div}(Lw)=\operatorname{div}F+\tau\,\theta\cdot F .
\]
By Lemma 2.1(1) and (2), with the multipliers \(m^{-1},\ell^{-1},\ell^{-1}m^{-1}\partial_jm\) cut off near \(\overline B\), \(\|E_\tau^{-1}\mathcal LU\|_{H^{-1}_h}\le C h^{-1}\|F\|_{L^2}\), using \(\tau=h^{-1}\). The \(u\)-component of the left side of (3.2) dominates \(\|E_\tau^{-1}w\|_{L^2}\), which proves (1).

(2) Substituting \(w=E_\tau v\) in (1) gives \(\|v\|_{L^2}\le C\|A_\theta v\|_{L^2}\) for \(v\in C^\infty_c(B)\), and the same holds for \(A_{-\overline\theta}=A_\theta^*\), possibly with a larger \(C\) and a smaller \(h_1\). On the subspace \(M=\{A_\theta^*v:v\in C^\infty_c(B;\mathbb C^3)\}\) of \(L^2(B;\mathbb C^3)\) define \(\ell(A_\theta^*v)=(v,f)\). This is well defined, because \(A_\theta^*v=0\) forces \(v=0\), linear, and bounded: \(|(v,f)|\le\|v\|\|f\|\le C\|A_\theta^*v\|\|f\|\). Extend \(\ell\) by continuity to the closure of \(M\) and by zero on its orthogonal complement; this is a bounded functional on \(L^2(B)\) of norm at most \(C\|f\|\). By the Riesz–Fréchet theorem it is \(g\mapsto(g,z)\) with \(\|z\|\le C\|f\|\). Then \((z,A_\theta^*v)=\overline{(A_\theta^*v,z)}=\overline{(v,f)}=(f,v)\) for every test function \(v\), which says \(A_\theta z=f\) in the sense of distributions. \(\square\)

## 5. Interior estimates at the scale 1/τ

**Lemma 5.1** (scaled interior estimate; [OpenAI-EL, Lemma 3.4]). Let \(B'\Subset B\) be balls. There are \(h_{B'},C_{B'}>0\) such that, whenever \(0<h<h_{B'}\) and \(z,f\in L^2(B;\mathbb C^3)\) satisfy \(A_\theta z=f\) in the sense of distributions on \(B\),
\[
\begin{aligned}&\sum_{j=0}^2h^j\|\nabla^jz\|_{L^2(B')}\\&\quad\le C_{B'}\bigl(\|z\|_{L^2(B)}\\&\qquad+h^2\|f\|_{L^2(B)}\bigr).\end{aligned}\tag{5.1}
\]
If \(f\) is smooth, then \(z\) is smooth in \(B\).

*Proof.* \(A_\theta\) has the principal part of \(L\), which is invertible (Section 4 of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md)); so Hypothesis (ER)(1) of that lesson gives \(z\in H^2_{\mathrm{loc}}(B)\), and \(z\in C^\infty(B)\) when \(f\) is smooth.

*Rescaling.* Conjugation replaces \(\partial_j\) by \(\partial_j+\tau\theta_j\). So \(A_\theta=L+\tau L^{(1)}+\tau^2L^{(0)}\), where \(L^{(1)}\) is a first-order operator and \(L^{(0)}\) a multiplication operator, with smooth coefficients built from the moduli, their first derivatives and \(\theta\). Fix a ball \(B''\) with \(B'\Subset B''\Subset B\). For \(x_0\in\overline{B''}\) and \(h\) with \(B(x_0,2h)\subset B\), put \(z_{x_0}(y)=z(x_0+hy)\) for \(|y|<2\). Since \(\partial_x=h^{-1}\partial_y\) and \(h\tau=1\),
\[
\bigl(h^2A_\theta z\bigr)(x_0+hy)=P_{x_0,h}z_{x_0}(y),
\]
where \(P_{x_0,h}\) is the Lamé operator in \(y\) with the moduli \(\lambda(x_0+hy),\mu(x_0+hy)\), plus the first-order part of \(L^{(1)}\) with its coefficients at \(x_0+hy\), plus multiplication by the values at \(x_0+hy\) of \(L^{(0)}\), plus terms carrying a factor \(h\). All coefficients and their \(y\)-derivatives are continuous in \((y,x_0,h)\in\overline{B(0,2)}\times\overline{B''}\times[0,h_0]\), including \(h=0\), and the principal symbol, that of the Lamé operator with the moduli at \(x_0+hy\), is invertible. Hypothesis (ER)(2) with \(K=\overline{B''}\times[0,h_0]\) gives
\[
\begin{aligned}&\|z_{x_0}\|_{H^2(B(0,1))}\\&\quad\le C\bigl(\|z_{x_0}\|_{L^2(B(0,2))}\\&\qquad+h^2\|f(x_0+h\,\cdot)\|_{L^2(B(0,2))}\bigr).\end{aligned}
\]
Changing variables back, with \(dx=h^3dy\) and \(\nabla_y=h\nabla_x\), multiplies every term by \(h^{-3/2}\), so
\[
\begin{aligned}&\sum_{j=0}^2h^j\|\nabla^jz\|_{L^2(B(x_0,h))}\\&\quad\le C\bigl(\|z\|_{L^2(B(x_0,2h))}\\&\qquad+h^2\|f\|_{L^2(B(x_0,2h))}\bigr).\end{aligned}
\]

*Summing.* Let \(h<h_{B'}\), where \(h_{B'}\) is the smallest of \(h_0\), \(\operatorname{dist}(B',\partial B'')\) and \(\tfrac12\operatorname{dist}(B'',\partial B)\), and let \(x_0\) run through the points of the lattice \((h/2)\mathbb Z^3\) within distance \(h\) of \(\overline{B'}\). These points lie in \(\overline{B''}\), the balls \(B(x_0,h)\) cover \(B'\), and the doubled balls lie in \(B\). Each point of \(\mathbb R^3\) lies in at most \(9^3\) of the doubled balls, the number of lattice points of spacing \(h/2\) in a ball of radius \(2h\) being at most \(9^3\). Squaring and summing the local estimates proves (5.1). \(\square\)

## 6. Exercises

**6.1.** For constant moduli compute \(R(u,d)\), \(S(u,d)\) and \(\mathcal LU\).

**6.2.** Show that a nonzero \(\theta\in\mathbb C^3\) with \(\theta\cdot\theta=0\) has \(|\operatorname{Re}\theta|=|\operatorname{Im}\theta|>0\) and \(\operatorname{Re}\theta\perp\operatorname{Im}\theta\), and give an example.

**6.3.** For \(\theta\) as in Exercise 6.2 and a smooth function \(a\), show that \(\Delta(E_\tau a)=E_\tau(\Delta a+2\tau D_\theta a)\).

**6.4.** Verify the formula \(A_\theta^*=A_{-\overline\theta}\) for \(L=\Delta\) (a single component) directly.

**6.5.** In Lemma 2.1(3), compute the factor for \(\gamma=0\), and explain why some factor is needed for \(\gamma\ne0\).

## 7. Solutions

**6.1.** With \(\nabla m=\nabla k=\nabla\lambda=0\): \(R(u,d)=m\Delta u+k\nabla d\), \(S(u,d)=\ell\Delta d\), \(P=m\Delta\), and \(\mathcal LU=(\Delta u+(k/m)\nabla d,\ \Delta d)\).

**6.2.** \(\theta\cdot\theta=|\alpha|^2-|\beta|^2+2i\,\alpha\cdot\beta\) for \(\theta=\alpha+i\beta\). It vanishes exactly when \(|\alpha|=|\beta|\) and \(\alpha\cdot\beta=0\); if \(\theta\ne0\), both lengths are positive. Example: \(\theta=(1,i,0)\).

**6.3.** \(\partial_j(E_\tau a)=E_\tau(\partial_ja+\tau\theta_ja)\), and once more \(\partial_j^2(E_\tau a)=E_\tau(\partial_j^2a+2\tau\theta_j\partial_ja+\tau^2\theta_j^2a)\). Summing over \(j\), the last term gives \(\tau^2(\theta\cdot\theta)a=0\).

**6.4.** For test functions \(v,w\), two integrations by parts give
\[
\begin{aligned}(A_\theta v,w)&=\int\Delta(e^{\tau\theta\cdot x}v)\,e^{-\tau\theta\cdot x}\overline w\,dx\\&=\int v\,e^{\tau\theta\cdot x}\Delta(e^{-\tau\theta\cdot x}\overline w)\,dx .\end{aligned}
\]
The function \(e^{\tau\theta\cdot x}\Delta(e^{-\tau\theta\cdot x}\overline w)\) is the complex conjugate of \(e^{\tau\overline\theta\cdot x}\Delta(e^{-\tau\overline\theta\cdot x}w)\). So \((A_\theta v,w)=(v,A_{-\overline\theta}w)\), since \(A_{-\overline\theta}=e^{\tau\overline\theta\cdot x}\Delta\,e^{-\tau\overline\theta\cdot x}\) for \(L=\Delta\).

**6.5.** For \(\gamma=0\) the multiplier is one and the norms are unchanged; the bound gives the factor \(\sqrt2\), which is not sharp. For \(\gamma\ne0\), the function \(v\) whose Fourier transform is concentrated near \(\xi=-\gamma/h\) has \(H^1_h\) norm about \(\sqrt{1+|\gamma|^2}\,\|v\|\), while the modulated function is concentrated near \(\xi=0\) and has norm about \(\|v\|\); so the norm can change by a factor comparable to \(\sqrt{1+|\gamma|^2}\).

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Imanuvilov–Yamamoto 2004] O. Yu. Imanuvilov, M. Yamamoto, *Carleman estimate for a stationary isotropic Lamé system and the applications*, Appl. Anal. 83 (2004), no. 3, 243–270. https://www.ms.u-tokyo.ac.jp/preprint/pdf/2003-19.pdf
- [Salo–Tzou 2009] M. Salo, L. Tzou, *Carleman estimates and inverse problems for Dirac operators*, Math. Ann. 344 (2009), no. 1, 161–184. https://arxiv.org/abs/0709.2282
