# Norm sheets and exact Gaussian smoothing

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The global Whittaker function of the cubic theta representation factors, by [*Cubic theta and its Whittaker coefficients*](cubic-theta-and-its-whittaker-coefficients.md), into the exterior spherical values, which produce the coefficient of \(B_m(Z)\), and a component at the places of \(S\). This lesson chooses that component and controls it. At the finite places of \(S\) it is the indicator of a small subgroup; at the complex places it is a Bessel function \(K_{1/3}\), multiplied by a power of the norm and an angular character. Integrated over the set of \(y\in F_S^\times\) of fixed norm \(u\), a **norm sheet**, it becomes a one-variable profile with rapid decay at both ends. A kernel constructed from the Mellin transform of this profile turns it exactly into the Gaussian \(P_G\) of the coefficient family.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Sections 1 and 3; [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), Lemma 6.1; [*Cubic theta and its Whittaker coefficients*](cubic-theta-and-its-whittaker-coefficients.md), N1, (1.2), (2.1) and Lemma 3.1; [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Lemma 2.1; [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03), Theorem 1.2 and Corollary 4.1.

## 1. Bessel integrals

For real \(\nu\) and \(x>0\) put
\[
\begin{aligned}
&K_\nu(x)=\frac12\int_0^\infty s^{\nu-1}\\
&\qquad\times\exp\Bigl(-\frac x2\bigl(s+s^{-1}\bigr)\Bigr)\,ds .\quad(1.1)
\end{aligned}
\]
The substitution \(s\mapsto s^{-1}\) gives \(K_{-\nu}=K_\nu\), and \(s=e^\tau\) gives \(K_\nu(x)=\int_0^\infty e^{-x\cosh\tau}\cosh(\nu\tau)\,d\tau\), the usual integral form of the modified Bessel function of the second kind [DLMF, §10.32].

**Lemma 1.1.** Let \(\nu>0\).

1. For real \(\nu'\) and \(a,b>0\),
\[
\begin{aligned}
&\int_0^\infty t^{\nu'-1}e^{-at-b/t}\,dt\\
&\quad =2\Bigl(\frac ba\Bigr)^{\nu'/2}K_{\nu'}\bigl(2\sqrt{ab}\bigr).\quad(1.2)
\end{aligned}
\]
2. For \(c>0\) and complex \(\mu\) with \(\operatorname{Re}\mu>\nu\),
\[
\begin{aligned}
&\int_0^\infty x^{\mu-1}K_\nu(cx)\,dx\\
&\quad =2^{\mu-2}c^{-\mu}\,\Gamma\Bigl(\frac{\mu-\nu}2\Bigr)\\
&\qquad \Gamma\Bigl(\frac{\mu+\nu}2\Bigr).\quad(1.3)
\end{aligned}
\]
3. \(K_\nu\) is positive, \(K_\nu(x)\le2^{\nu-1}\Gamma(\nu)x^{-\nu}\), \(x^\nu K_\nu(x)\to2^{\nu-1}\Gamma(\nu)\) as \(x\to0^+\), and \(K_\nu(x)\le e^{1-x}K_\nu(1)\) for \(x\ge1\).

*Proof.* (1) The substitution \(t=\sqrt{b/a}\,s\) turns \(at+b/t\) into \(\sqrt{ab}\,(s+s^{-1})\) and the integral into \((b/a)^{\nu'/2}\int_0^\infty s^{\nu'-1}e^{-\sqrt{ab}(s+s^{-1})}\,ds\), which is (1.2) by (1.1).

(3) The substitution \(s=2u/x\) in (1.1) gives
\[
\begin{aligned}
K_\nu(x)&=\frac12\Bigl(\frac2x\Bigr)^\nu\int_0^\infty u^{\nu-1}\\
&\quad e^{-u-x^2/(4u)}\,du .
\end{aligned}
\]
The integral is at most \(\Gamma(\nu)\) and increases to \(\Gamma(\nu)\) as \(x\to0^+\), by monotone convergence. For \(x\ge1\), \(s+s^{-1}\ge2\) gives \(\frac x2(s+s^{-1})\ge(x-1)+\frac12(s+s^{-1})\), hence the last bound.

(2) Formula (1.2) with \(\nu'=-\nu\), \(a=1\), \(b=c^2x^2/4\), together with \(K_{-\nu}=K_\nu\), gives
\[
\begin{aligned}
K_\nu(cx)&=\frac12\Bigl(\frac{cx}2\Bigr)^\nu\int_0^\infty t^{-\nu-1}\\
&\quad e^{-t-c^2x^2/(4t)}\,dt .
\end{aligned}
\]
Insert this into the left side of (1.3). For real \(\mu>\nu\) Tonelli's theorem allows the interchange, and for complex \(\mu\) the absolute integrand is the one for \(\operatorname{Re}\mu\). The substitution \(y=c^2x^2/(4t)\) gives
\[
\begin{aligned}
&\int_0^\infty x^{\mu+\nu-1}e^{-c^2x^2/(4t)}\,dx=2^{\mu+\nu-1}\\
&\qquad c^{-\mu-\nu}\,t^{(\mu+\nu)/2}\,\Gamma\Bigl(\frac{\mu+\nu}2\Bigr),
\end{aligned}
\]
and the remaining integral \(\int_0^\infty t^{(\mu-\nu)/2-1}e^{-t}\,dt\) is \(\Gamma(\frac{\mu-\nu}2)\). The constants combine to \(\frac12\cdot2^{-\nu}c^\nu\cdot2^{\mu+\nu-1}c^{-\mu-\nu}=2^{\mu-2}c^{-\mu}\). \(\square\)

## 2. The Whittaker function at a complex place

Let \(v\) be a complex place. Every nontrivial character of the additive group \(\mathbb C\) has the form \(z\mapsto e^{i\operatorname{Re}(\alpha z)}\) with \(\alpha\ne0\); rotating the coordinate, \(\psi_v(z)=e^{ic_v\operatorname{Re}z}\) with \(c_v>0\). The rotation multiplies the angular characters below by constants of absolute value one, which are absorbed when vectors are scaled in Section 4. Write \(|y|_v\) for the square of the ordinary modulus, \(\varrho=|y|_v^{1/2}\), and \(\mathcal D_vf(y)=\frac d{dt}f(e^{t/2}y)\big|_{t=0}\), so that \(|e^{t/2}y|_v=e^t|y|_v\).

By N1(3), \(\Theta_v\) is the spherical principal series of \(\mathrm{PGL}_2(\mathbb C)\) with normalized characters \((|\cdot|_v^{1/6},|\cdot|_v^{-1/6})\), and it has a one-dimensional space of Whittaker functionals. Put \(\nu_0=\frac12+\frac16=\frac23\). The spherical section is
\[
f^\circ(g)=\Bigl(\frac{|\det g|}{|g_{21}|^2+|g_{22}|^2}\Bigr)^{2\nu_0},
\]
with ordinary moduli. It is invariant under scalars, under the unitary group on the right and under \(n(x)\) on the left, and on \(g=n(x)a(y)k\) it equals \(|y|^{2\nu_0}=|y|_v^{2/3}\), the normalized inducing law. Since \(wn(x)a(y)=\begin{pmatrix}0&1\\y&x\end{pmatrix}\),
\[
f^\circ(wn(x)a(y))=\varrho^{2\nu_0}(\varrho^2+|x|^2)^{-2\nu_0}.
\]

**Lemma 2.1** ([OpenAI-029, (5.7), (5.11), (5.12)]). The spherical Whittaker function of \(\Theta_v\) is a nonzero constant times \(|y|_v^{1/2}K_{1/3}(c_v|y|_v^{1/2})\). Suitable first Lie derivatives of the spherical vector, for \(m\in\{1,-1\}\), have Whittaker functions
\[
\begin{gathered}
\begin{aligned}
W_{v,m}(a(y))&=|y|_v\,\omega_m(y)\\
&\quad \,K_{1/3}\bigl(c_v|y|_v^{1/2}\bigr),
\end{aligned}\\
\omega_m(y)=\bigl(y/|y|_v^{1/2}\bigr)^m .\quad(2.1)
\end{gathered}
\]
For every fixed finite list of these vectors and their rotations by fixed elements of the maximal compact subgroup, every integer \(j\ge0\) and every \(A>0\),
\[
\begin{aligned}
&|\mathcal D_v^jW(a(y))|\\
&\quad \le C_{A,j}\min\bigl(|y|_v^{1/3},|y|_v^{-A}\bigr).\quad(2.2)
\end{aligned}
\]

*Proof.* The Jacquet integral \(\int f^\circ(wn(x)a(y))\overline{\psi_v(x)}\,dx\) converges absolutely because \(4\nu_0>2\), and it is a nonzero Whittaker functional evaluated on \(\pi(a(y))f^\circ\); by uniqueness every Whittaker function of the spherical vector is a multiple of it. With \(R^{-\nu}=\Gamma(\nu)^{-1}\int_0^\infty t^{\nu-1}e^{-tR}\,dt\) for \(R,\nu>0\) and the Gaussian integral \(\int_{\mathbb R^2}e^{-icx_1-t|x|^2}\,dx=\frac\pi te^{-c^2/(4t)}\),
\[
\begin{aligned}
&\varrho^{2\nu_0}\int_{\mathbb R^2}\frac{e^{-ic_vx_1}\,dx}{(\varrho^2+|x|^2)^{2\nu_0}}=\frac{\pi\varrho^{2\nu_0}}{\Gamma(2\nu_0)}\\
&\qquad \int_0^\infty t^{2\nu_0-2}e^{-t\varrho^2-c_v^2/(4t)}\,dt\\
&\quad =c_v'\,\varrho K_{1/3}(c_v\varrho),
\end{aligned}
\]
with \(c_v'=2\pi(c_v/2)^{1/3}/\Gamma(4/3)\), by (1.2) with \(\nu'=2\nu_0-1=1/3\), \(a=\varrho^2\), \(b=c_v^2/4\). The interchange is absolute: without the phase the Gaussian integral leaves \(\pi t^{2\nu_0-2}e^{-t\varrho^2}\), and \(2\nu_0-2=-2/3>-1\).

By (2.1) of Lesson 6, \(a(y)n(z)=n(yz)a(y)\), so \(W_{\pi(n(z))\varphi}(a(y))=\psi_v(yz)W_\varphi(a(y))\). Differentiating in the two real directions of \(z\) at \(0\) and taking complex combinations multiplies the spherical Whittaker function by \(y\) or by \(\bar y\). Since \(y\varrho=|y|_v\,\omega_1(y)\) and \(\bar y\varrho=|y|_v\,\omega_{-1}(y)\), this gives (2.1) after scaling.

For the bounds, a rotation of a first Lie derivative of the spherical vector is another first Lie derivative, since \(\pi(k)d\pi(X)=d\pi(\operatorname{Ad}(k)X)\pi(k)\) and the spherical vector is fixed. The operator \(\mathcal D_v\) on Whittaker functions is right differentiation by \(\operatorname{diag}(\frac12,0)\). Right differentiation of \(f^\circ\) by any element of the Lie algebra multiplies it by a real-rational function of the bottom row \((y,x)\) that is homogeneous of degree \(0\) and smooth away from \(0\), hence bounded, and this class of functions is stable under further right differentiation. So the Whittaker function of \(\mathcal D_v^j\) applied to any listed vector is the Jacquet integral of \(f^\circ(wn(x)a(y))R(y,x)\) with such an \(R\). After \(h\) derivatives in \(x_1\) this integrand is bounded by \(C_h\varrho^{2\nu_0}(\varrho^2+|x|^2)^{-2\nu_0-h/2}\). With \(h=0\) the integral of this bound is \(C\varrho^{2-2\nu_0}=C|y|_v^{1/3}\). For \(\varrho\ge1\), integrating by parts \(h\) times against \(e^{-ic_vx_1}\) gives \(O(\varrho^{2-2\nu_0-h})\). Taking \(h\) large proves (2.2). \(\square\)

## 3. Bounds at the finite places of S

**Lemma 3.1** ([OpenAI-029, (5.13)]). Let \(v\) be a finite place, \(\varphi\) a smooth vector of \(\Theta_v\) and \(\lambda_v\) a Whittaker functional, and put \(W_\varphi(y)=\lambda_v(\pi(a(y))\varphi)\). For every \(\delta<1/3\),
\[
\begin{gathered}
W_\varphi(y)=0\quad(|y|_v>C_\varphi),\\
\begin{aligned}
|W_\varphi(y)|&\le C_{\varphi,\delta}|y|_v^\delta\quad(|y|_v\le1).
\end{aligned}\quad(3.1)
\end{gathered}
\]

*Proof.* Let \(J\) be an open additive subgroup with \(n(J)\) fixing \(\varphi\). For \(x\in J\), \(W_\varphi(y)=\lambda_v(\pi(a(y))\pi(n(x))\varphi)\)\(=\psi_v(yx)W_\varphi(y)\); for large \(|y|_v\) some \(x\in J\) has \(\psi_v(yx)\ne1\), so \(W_\varphi(y)=0\).

For small \(|y|_v\), let \(z=a(\varpi_v^3)\), central in the covering torus. It normalizes the unipotent radical, so it acts on the ordinary Jacquet module, which is finite dimensional; by N1(4) its eigenvalues have absolute values \(q_v^{-1}\) and \(q_v^{-2}\). Let \(P\) be the characteristic polynomial of this action. By the Cayley–Hamilton theorem, \(P(\pi(z))\varphi=\sum_i(\pi(n(x_i))-1)\varphi_i\) for finitely many \(x_i,\varphi_i\). Apply \(\lambda_v\circ\pi(a(y))\): the right side vanishes once \(|y|_v\) is small enough that \(\psi_v(yx_i)=1\) for all \(i\). By (1.2) of Lesson 6 the cocycle of \(a(y)\) and \(a(\varpi_v^3)\) is \((y,\varpi_v^3)_{3,v}^2=1\), so the left side is \(P(E)W_\varphi(y)\) with \(EW_\varphi(y)=W_\varphi(y\varpi_v^3)\). An open subgroup of units consisting of cubes fixes \(\varphi\) and has trivial cocycle with every \(a(y)\), so \(W_\varphi\) is constant on its cosets. On each set \(\{u\varpi_v^{j+3k}:k\ge0\}\), with \(j\) and the coset of \(u\) fixed, the sequence of values satisfies the linear recurrence with characteristic polynomial \(P\) for large \(k\), so it is a sum of polynomials in \(k\) times \(k\)th powers of roots of \(P\). Since \(|y|_v=q_v^{-j-3k}\) and the roots have absolute values \(q_v^{-1}\) and \(q_v^{-2}\), this gives (3.1); the finitely many remaining shells with \(|y|_v\le1\) carry finitely many values. \(\square\)

The same conclusions hold for the finite sums of products of local functions at \(S\) that occur in Lemma 3.1 of Lesson 6.

## 4. A finite torus cutoff and the choice at S

**Lemma 4.1** (finite torus cutoff [OpenAI-029, Lemma 5.3]). Let \(S_f\) be a finite set of finite places and \(\lambda_f\ne0\) a Whittaker functional, with character \(\prod_{v\in S_f}\psi_v\), on a smooth representation of the product of the local covers. Put \(W_\varphi(y)=\lambda_f(\pi(a(y))\varphi)\) for \(y\in\prod_{v\in S_f}F_v^\times\). For every open subgroup \(H_f\) of \(\prod_{v\in S_f}\mathcal O_v^\times\) there are a compact open product subgroup \(U\subseteq H_f\) and a smooth vector \(\varphi_U\) with \(W_{\varphi_U}=\mathbf 1_U\).

*Proof.* Choose \(\varphi\) with \(\lambda_f(\varphi)\ne0\). The function \(W_\varphi\) is locally constant near \(1\); choose a product \(U\subseteq H_f\) of groups \(1+\mathfrak p_v^{m_v}\) on which it equals \(\lambda_f(\varphi)\). The function \(\mathbf 1_U\) is a Schwartz–Bruhat function on \(\prod_{v\in S_f}F_v\), so by Fourier inversion there is a Schwartz–Bruhat function \(\beta\) with \(\int\beta(t)\prod_v\psi_v(y_vt_v)\,dt=\mathbf 1_U(y)\). The vector \(\varphi'=\int\beta(t)\pi(n(t))\varphi\,dt\) is a finite combination of translates of \(\varphi\), and \(W_{\varphi'}(y)\)\(=W_\varphi(y)\int\beta(t)\prod_v\psi_v(y_vt_v)\,dt\)\(=\lambda_f(\varphi)\mathbf 1_U(y)\). Put \(\varphi_U=\varphi'/\lambda_f(\varphi)\). \(\square\)

*The choice.* Let \(\mathscr L\) be a fixed finite family of smooth unitary characters \(\mathcal L_S\) of \(F_S^\times\), each radially trivial at the complex places with angular component \(\omega_{m_v}\), \(m_v\in\{1,-1\}\), at each complex place \(v\). By Lemma 6.1 of [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), \(L_S\) has this form; so does its product with any character of the finite group \(\mathcal V=F_S^\times/F_S^{\times6}\), whose complex components are trivial. Factor the global functional at the complex places and apply Lemma 4.1 at the finite places of \(S\), with an open subgroup contained in the sixth powers and in the kernels of the finite components of all \(\mathcal L_S\in\mathscr L\); this gives one subgroup \(U=\prod_{v\in S_f}U_v\). At each complex place choose the derivative vector of the angular type of \(\mathcal L_S\). Scaling the vectors, the resulting \(S\)-Whittaker function is
\[
\begin{aligned}
W_{S,\mathcal L_S}(a(y))&=\mathbf 1_U(y_f)\prod_{v\mid\infty}|y_v|_v\\
&\quad \,\omega_{m_v}(y_v)\\
&\quad \,K_{1/3}\bigl(c_v|y_v|_v^{1/2}\bigr).\quad(4.1)
\end{aligned}
\]
In particular \(\mathcal L_S(y)^{-1}W_{S,\mathcal L_S}(a(y))\) is the same function \(\mathbf 1_U(y_f)\prod_v|y_v|_vK_{1/3}(c_v|y_v|_v^{1/2})\) for every member of the family.

## 5. Integration on norm sheets

Recall that \(F\) has \(r\) complex places and that \(F_S^1\) is the kernel of \(|\cdot|_S\) on \(F_S^\times\). For \(u>0\) the **norm sheet** \(X_u=\{y\in F_S^\times:|y|_S=u\}\) is the coset \(\ell_uF_S^1\), with \(\ell_u\) as in Section 3 of [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md). Give \(F_S^\times\) the product of the local multiplicative Haar measures; at a complex place this is a constant times \(dt/t\) times angle measure of mass one, with \(t=|y_v|_v\). Since \(u\mapsto\ell_u\) is a continuous homomorphism splitting \(|\cdot|_S\), there is a Haar measure on \(F_S^1\) such that, with its translate to \(X_u\) by \(\ell_u\),
\[
\begin{aligned}
&\int_{F_S^\times}f(y)\,d^\times y\\
&\quad =\int_0^\infty\int_{X_u}f(y)\,d_u^\times y\,\frac{du}u .\quad(5.1)
\end{aligned}
\]
By invariance the translated measure on \(X_u\) does not depend on the representative \(\ell_u\).

**Lemma 5.1** (norm-sheet profiles [OpenAI-029, Lemma 5.4]). Let \(\mathcal I\) be a finite index set and, for \(\kappa\in\mathcal I\), let \(f_\kappa(y)=\sum_{\ell=1}^{L_\kappa}\prod_{v\in S}f_{\kappa,\ell,v}(y_v)\). Assume, for one \(\delta>0\):

- (a) at a finite \(v\), \(f_{\kappa,\ell,v}\) is locally constant, vanishes for \(|y_v|_v>C_v\), and is \(O(|y_v|_v^\delta)\) for \(|y_v|_v\le1\);
- (b) at a complex \(v\), the factor is smooth and \(|\mathcal D_v^jf_{\kappa,\ell,v}(y_v)|\)\(\le C_{A,j}\min(|y_v|_v^\delta,|y_v|_v^{-A})\) for all \(j\ge0\), \(A>0\).

Put \(H_\kappa(u)=\int_{X_u}f_\kappa\,d_u^\times y\) and \(D=u\frac d{du}\). Fix a complex place \(v_0\) and define
\[
\begin{aligned}
H_{\kappa,j}^{\mathrm{abs}}(u)&=\sum_{\ell}\int_{X_u}|\mathcal D_{v_0}^jf_{\kappa,\ell,v_0}(y_{v_0})|\\
&\quad \prod_{v\ne v_0}|f_{\kappa,\ell,v}(y_v)|\,d_u^\times y .
\end{aligned}
\]
Then \(H_\kappa\) is smooth, and for \(j\ge0\) and \(\sigma>-\delta\),
\[
\begin{gathered}
\begin{aligned}
|D^jH_\kappa(u)|&\le H_{\kappa,j}^{\mathrm{abs}}(u)\\
&\le C_{\sigma,j}u^{-\sigma}
\end{aligned}\\
(u>0);\quad(5.2)
\end{gathered}
\]
in particular, for \(0<\alpha<\delta\) and every \(A>0\), \(|D^jH_\kappa(u)|+H_{\kappa,j}^{\mathrm{abs}}(u)\)\(\le C_{A,j}\min(u^\alpha,u^{-A})\). The same holds after multiplying each \(f_\kappa\) by a fixed smooth unitary character of \(F_S^\times\) and by a function of the class of \(y\) in \(\mathcal V\).

Let \(\mathcal K\colon(0,\infty)\to\mathbb C\) have all absolute moments \(M_\beta(\mathcal K)=\int_0^\infty|\mathcal K(T)|T^\beta\,\frac{dT}T\) finite. Then \(\int_0^\infty\mathcal K(T)H_\kappa(uT^{\pm1})\,\frac{dT}T\) and their absolute majorants obey the same two-ended bound, and for \(x_i>0\), complex \(a_i\), \(\kappa_i\in\mathcal I\), \(\tau\in\{1,-1\}\) and \(\sigma>-\delta\),
\[
\begin{aligned}
&\int_0^\infty|\mathcal K(T)|\sum_i|a_i|\\
&\qquad \,H^{\mathrm{abs}}_{\kappa_i,0}(ux_iT^\tau)\,\frac{dT}T\le C_{\sigma,0}\,u^{-\sigma}\\
&\qquad M_{-\tau\sigma}(\mathcal K)\sum_i|a_i|x_i^{-\sigma}.\quad(5.3)
\end{aligned}
\]

*Proof.* At a finite place, (a) gives \(\int|f_{\kappa,\ell,v}(y)||y|_v^\sigma\,d^\times y<\infty\) for \(\sigma>-\delta\): on the shell \(|y|_v=q_v^{-k}\) the integrand is \(O(q_v^{-k(\delta+\sigma)})\) for \(k\ge0\), and only finitely many shells with \(k<0\) meet the support. At a complex place, (b) gives \(\int|f_{\kappa,\ell,v}||y|_v^\sigma\,d^\times y<\infty\) and \(\sup|y|_v^\sigma|\mathcal D_v^jf_{\kappa,\ell,v}|<\infty\). On \(X_u\) use \(t_{v_0}=|y_{v_0}|_{v_0}=u\prod_{v\ne v_0}|y_v|_v^{-1}\) as the dependent norm. By (5.1), up to a constant factor, the sheet measure is angle measure at \(v_0\) times the multiplicative measures at the other places, because \(dt_{v_0}/t_{v_0}=du/u\) when the other coordinates are fixed. Multiply the absolute integrand by \(u^\sigma=\prod_v|y_v|_v^\sigma\), take the weighted supremum at \(v_0\) and the weighted integrals elsewhere: this gives the second inequality in (5.2). In this parametrization \(D\) differentiates only the \(v_0\)-factor, as \(\mathcal D_{v_0}\), and the majorants, uniform for \(u\) in compact sets, justify differentiating under the integral; this gives the first inequality. Taking \(\sigma=-\alpha\) and \(\sigma=A\) gives the two-ended bound.

A function on the finite group \(\mathcal V\) is a finite combination of products of local class indicators, because the sixth-power quotient is trivial at complex places and finite at finite places; local class indicators at finite places are locally constant and bounded. A unitary character factors over \(S\); its finite components are locally constant of absolute value one, and its complex components have the form \(|y|_v^{i\tau}\omega_m(y)\), so \(\mathcal D_v\) applied to their products with \(f\) only adds the term \(i\tau f\). For the convolutions, apply the bounds with \(\sigma=-\alpha\) or \(\sigma=A\) under the \(T\)-integral, and (5.3) follows from (5.2) by Tonelli's theorem and the definition of the moments. \(\square\)

**Corollary 5.2** ([OpenAI-029, (5.19)]). If \(\rho\in C_c^\infty(\mathbb R)\) is fixed and \(\Phi_\kappa(u)=\int_0^\infty\mathcal K(T)H_\kappa(u/T)\,dT/T\), then
\[
\begin{aligned}
&\bigl\|\widehat{\rho(t)\Phi_\kappa(ue^t)}\bigr\|_{L^1(\mathbb R)}\\
&\quad \le C_{A,\rho}\min(u^\alpha,u^{-A}),\quad(5.4)
\end{aligned}
\]
the Fourier transform being taken in \(t\).

*Proof.* For a function \(g\) supported in a fixed compact interval, \(|\widehat g(\xi)|\le\|g\|_{L^1}\) and \(|\widehat g(\xi)|\le\xi^{-2}\|g''\|_{L^1}\), so \(\|\widehat g\|_{L^1}\) is at most a constant times the suprema of \(|g|\) and \(|g''|\). For \(g(t)=\rho(t)\Phi_\kappa(ue^t)\) these involve \((D^j\Phi_\kappa)(ue^t)\) with \(j\le2\) and \(ue^t\asymp u\), which Lemma 5.1 bounds by \(C_A\min(u^\alpha,u^{-A})\). \(\square\)

Fourier inversion with \(t=\log x-\log y\), for \(x\) and \(y\) in fixed ratio intervals, therefore separates two norm variables at a bounded \(L^1\) cost while keeping any power saving for large \(u\).

## 6. Exact Gaussian smoothing

For the function (4.1) the angular characters cancel against \(\mathcal L_S^{-1}\). Define the radial profile
\[
\begin{aligned}
V(u)&=\int_{X_u}\mathbf 1_U(y_f)\prod_{v\mid\infty}|y_v|_v\\
&\quad K_{1/3}\bigl(c_v|y_v|_v^{1/2}\bigr)\,d_u^\times y .\quad(6.1)
\end{aligned}
\]
It is positive, and by Lemmas 2.1 and 5.1 (with \(\delta=1/3\)) it satisfies the two-ended bounds. In this section \(\widehat f(s)=\int_0^\infty f(u)u^s\,du/u\).

**Lemma 6.1** (exact Gaussian smoothing [OpenAI-029, Lemma 5.5]). There are constants \(C_0,A_0>0\) with
\[
\begin{gathered}
\widehat V(s)=C_0A_0^s\bigl[\Gamma(s+\tfrac56)\Gamma(s+\tfrac76)\bigr]^r\\
(\operatorname{Re}s>-\tfrac56).\quad(6.2)
\end{gathered}
\]
There is a smooth \(\mathcal K\colon(0,\infty)\to\mathbb C\) with \(|(T\partial_T)^j\mathcal K(T)|\le C_{N,j}\min(T^N,T^{-N})\) for all \(N,j\), with \(\widehat{\mathcal K}(-s)=e^{s^2}/\widehat V(s)\), and
\[
\begin{gathered}
\begin{aligned}
&\int_0^\infty\mathcal K(T)\,V(uT)\,\frac{dT}T\\
&\quad =P_G(u)
\end{aligned}\\
(u>0).\quad(6.3)
\end{gathered}
\]

*Proof.* By (5.1) and Tonelli's theorem, \(\widehat V(s)=\int_{F_S^\times}\mathbf 1_U(y_f)\prod_v|y_v|_v\)\(K_{1/3}(c_v|y_v|_v^{1/2})\,|y|_S^s\,d^\times y\) is the product of local Mellin integrals. A finite factor is the volume of \(U_v\), on which \(|y_v|_v=1\). At a complex place, with \(t=|y_v|_v\) and \(t=x^2\),
\[
\begin{aligned}
&\int_0^\infty t^{s+1}K_{1/3}(c_v\sqrt t)\,\frac{dt}t\\
&\quad =2\int_0^\infty x^{2s+1}K_{1/3}(c_vx)\,dx\\
&\quad =2^{2s+1}c_v^{-2s-2}\,\Gamma(s+\tfrac56)\\
&\qquad \Gamma(s+\tfrac76),
\end{aligned}
\]
by (1.3) with \(\mu=2s+2\) and \(\nu=1/3\), valid for \(\operatorname{Re}s>-5/6\); the angle integrals change only constants. This is (6.2), with \(A_0=\prod_{v\mid\infty}4c_v^{-2}\).

Put \(\mathcal R_V(s)=e^{s^2}/\widehat V(s)=C_0^{-1}A_0^{-s}\)\(e^{s^2}[\Gamma(s+\frac56)\Gamma(s+\frac76)]^{-r}\). The reciprocal of the Gamma function is entire (Theorem 1.2 of [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03)), so \(\mathcal R_V\) is entire. On every closed vertical strip, Corollary 4.1 there gives \(|\mathcal R_V(\sigma+it)|\le C(1+|t|)^Ce^{-t^2+\pi r|t|}\), also after multiplying by any fixed power of \(s\). Define
\[
\mathcal K(T)=\frac1{2\pi i}\int_{(\sigma)}\mathcal R_V(s)T^s\,ds ;
\]
the integral converges absolutely and does not depend on \(\sigma\), since the horizontal sides of rectangles tend to \(0\) by the Gaussian decay. Differentiation in \(\log T\) inserts powers of \(s\); taking \(\sigma=N\) for \(T\le1\) and \(\sigma=-N\) for \(T\ge1\) gives the bounds. On a vertical line, \(T^{-\sigma}\mathcal K(T)\) is the inverse Fourier transform in \(\log T\) of \(t\mapsto\mathcal R_V(\sigma+it)\), so Fourier inversion gives \(\widehat{\mathcal K}(-s)=\mathcal R_V(s)\) there, and everywhere by analyticity. On a line \(\sigma>0\), \(\int|\mathcal K(T)|T^{-\sigma}\,dT/T<\infty\) and \(\int V(u)u^\sigma\,du/u<\infty\), so by Fubini's theorem the Mellin transform of the left side of (6.3) is \(\widehat V(s)\widehat{\mathcal K}(-s)=e^{s^2}\). By Lemma 2.1 of Lesson 5, \(P_G\) has the same transform, and Mellin inversion proves (6.3). \(\square\)

After the Weyl element of Lesson 9 the norm variable is inverted; the same kernel then produces the profiles \(\Phi_\kappa(u)=\int\mathcal K(T)H_\kappa(u/T)\,dT/T\), which obey the bounds of Lemma 5.1 and Corollary 5.2 for every fixed finite family of rotated profiles.

## 7. Exercises

**7.1.** Verify the matrix identity \(wn(x)a(y)=\begin{pmatrix}0&1\\y&x\end{pmatrix}\) and compute \(f^\circ\) on it.

**7.2.** Using Lemma 1.1(3), show that the Mellin integral of a complex factor in Lemma 6.1 converges exactly for \(\operatorname{Re}s>-5/6\).

**7.3.** Show that \(\mathcal K\) is real valued.

**7.4.** In Lemma 5.1 with one complex place and no finite places, show that \(H_\kappa(u)\) is the angular average of \(f_\kappa\) on the circle \(|y|_v=u\).

**7.5.** Show that \(K_{1/2}(x)=\sqrt{\pi/(2x)}\,e^{-x}\), and check (1.3) for \(\nu=1/2\).

## 8. Solutions

**7.1.** \(n(x)a(y)=\begin{pmatrix}y&x\\0&1\end{pmatrix}\), and multiplying by \(w\) on the left swaps the rows. Then \(|\det|=|y|\) and the bottom row is \((y,x)\), so \(f^\circ=(|y|/(|y|^2+|x|^2))^{4/3}\)\(=\varrho^{4/3}(\varrho^2+|x|^2)^{-4/3}\) with \(\varrho=|y|\).

**7.2.** Near \(t=0\), Lemma 1.1(3) gives \(|t^{s+1}K_{1/3}(c\sqrt t)|\asymp t^{\operatorname{Re}s+5/6}\), integrable against \(dt/t\) near \(0\) exactly when \(\operatorname{Re}s+5/6>0\). For \(t\ge c^{-2}\), the bound \(K_{1/3}(c\sqrt t)\le e^{1-c\sqrt t}K_{1/3}(1)\) makes every power integrable.

**7.3.** \(\overline{\mathcal R_V(\bar s)}=\mathcal R_V(s)\) because \(C_0,A_0>0\) and the Gamma function is real on the real axis. Hence \(\overline{\mathcal K(T)}\)\(=\frac1{2\pi}\int\overline{\mathcal R_V(\sigma+it)}\,T^{\sigma-it}\,dt\)\(=\frac1{2\pi}\int\mathcal R_V(\sigma-it)\,T^{\sigma-it}\,dt=\mathcal K(T)\).

**7.4.** With one place, \(X_u\) is the circle \(|y|_v=u\), and its measure is the translate of angle measure of mass one.

**7.5.** By the representation in the proof of Lemma 1.1(3), \(K_{1/2}(x)=\frac12(2/x)^{1/2}\int_0^\infty u^{-1/2}\)\(e^{-u-x^2/(4u)}\,du\). With \(u=w^2\) and \(a=x/2\), the integral is \(2e^{-x}\int_0^\infty e^{-(w-a/w)^2}\,dw\). The substitution \(w\mapsto a/w\) shows that this last integral also equals \(\int_0^\infty e^{-(w-a/w)^2}a\,w^{-2}\,dw\); adding the two forms and putting \(z=w-a/w\) gives twice it equal to \(\int_{\mathbb R}e^{-z^2}\,dz=\sqrt\pi\). So \(K_{1/2}(x)=\sqrt{\pi/(2x)}\,e^{-x}\). Then
\[
\begin{aligned}
&\int_0^\infty x^{\mu-1}K_{1/2}(cx)\,dx\\
&\quad =\sqrt{\frac\pi{2c}}\int_0^\infty x^{\mu-3/2}e^{-cx}\,dx\\
&\quad =\sqrt{\frac\pi2}\,\Gamma(\mu-\tfrac12)\,c^{-\mu}.
\end{aligned}
\]
The duplication formula \(\Gamma(z)\Gamma(z+\frac12)=2^{1-2z}\sqrt\pi\,\Gamma(2z)\) with \(z=\frac\mu2-\frac14\) turns the right side of (1.3) into \(2^{\mu-2}c^{-\mu}\cdot2^{3/2-\mu}\sqrt\pi\,\Gamma(\mu-\frac12)\), the same expression.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [KP] D. A. Kazhdan and S. J. Patterson, *Metaplectic forms*, Publ. Math. IHÉS 59 (1984), 35–142, Theorem I.2.9 and Theorems I.6.4–I.6.5. http://www.numdam.org/item/PMIHES_1984__59__35_0/
- [DLMF] *NIST Digital Library of Mathematical Functions*, §10.32 (integral representations of modified Bessel functions). https://dlmf.nist.gov/10.32
