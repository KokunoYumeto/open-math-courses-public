# Comparing supported weights and transporting their cuts

**Self-checked by the writing AI.**

Normal semifinite weights can have different supports, so comparison cannot be phrased only with unitary cocycles. This lesson keeps the support projections visible. It proves the partial-isometry cocycle formula, converts comparison of weights into comparison of projections in a balanced centralizer, proves the resulting Cantor–Bernstein theorem, characterizes strict semifiniteness, and records the two transport mechanisms needed later: lacunary centralizers and faithful conditional expectations.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, Chapter XII, §4, the opening convention, Definition 4.1, Proposition 4.2, Lemma 4.3, Definition 4.6, Lemma 4.7(i), Lemma 4.9, Lemma 4.13, and footnote 6. The arguments below are independently written and use the course's support, spatial derivative, centralizer, density, and modular-expectation results. The type-dependent input in the application after WC-07 remains an explicit OA-FLOW prerequisite.

## Support corners, cuts, and the comparison relation

Let \(M\) be a von Neumann algebra and let \(\varphi\) be a normal semifinite weight. Put \(p=s(\varphi)\). For every \(x\in M_+\), the support theorem gives

\[
 \varphi(x)=\varphi(pxp).
 \tag{WC.1}
\]

and makes the restriction \(\varphi^p=\varphi|_{pMp}\) normal, semifinite, and faithful. Every modular object attached to a possibly nonfaithful \(\varphi\) in this lesson means the corresponding object for \(\varphi^p\) on \(pMp\). In particular,

\[
 M_\varphi=(pMp)_{\varphi^p}.
 \tag{WC.2}
\]

For \(e\in\operatorname{Proj}(M_\varphi)\), define the **centralizer cut** \(\varphi_e\) on \(M_+\) by

\[
 \varphi_e(x)=\varphi(exe).
 \tag{WC.3}
\]

The centralizer-corner theorem and corner lifting show that \(\varphi_e\) is normal semifinite and has support exactly \(e\).

If \(u\in M\) is a partial isometry, \(u^*u=s(\alpha)\), \(uu^*=s(\beta)\), and, for every \(x\in M_+\),

\[
 \alpha(x)=\beta(uxu^*),
 \tag{WC.4}
\]

write \(\alpha\sim\beta\). Write \(\alpha\precsim\beta\) when \(\alpha\sim\beta_e\) for some \(e\in\operatorname{Proj}(M_\beta)\). Thus a **subweight** here always means a centralizer projection cut, possibly transported by a partial isometry.

This is stronger than pointwise domination. For example, on \(\mathbb C^2\) let \(\tau(a,b)=a+b\). Every centralizer cut of \(\tau\) has coordinate coefficients in \(\{0,1\}\), whereas \(\tfrac12\tau\leq\tau\) has coefficients \((1/2,1/2)\). Hence pointwise smaller weights need not be subweights in the sense of (WC.3)–(WC.4).

## The supported cocycle against a faithful reference

Let \(\theta\) be normal semifinite with support \(p\), and let \(\psi\) be normal semifinite and faithful. There is a unique intrinsic sigma-strong* continuous family \((u_t)_{t\in\mathbb R}\) in \(M\), defined by

\[
 u_t=[D\theta:D\psi]_t,
 \tag{WC.5}
\]

with

\[
 \begin{aligned}
 u_tu_t^*&=p,\\
 u_t^*u_t&=\sigma_t^\psi(p),\\
 u_{s+t}&=u_s\sigma_s^\psi(u_t).
 \end{aligned}
 \tag{WC.6}
\]

For every \(x\in M\), it also satisfies the supported intertwining identity

\[
 u_t\sigma_t^\psi(x)u_t^*=\sigma_t^{\theta^p}(pxp).
 \tag{WC.7}
\]

To construct it, represent \(M\) faithfully on \(H\), choose a normal semifinite faithful weight \(\kappa\) on \(M'\), and write

\[
 A=\frac{d\theta}{d\kappa},\qquad
 B=\frac{d\psi}{d\kappa}.
\]

By support reduction, \(A\) is injective on \(pH\); its imaginary powers are extended by zero on \((1-p)H\). Put

\[
 u_t=A^{it}B^{-it}.
 \tag{WC.8}
\]

The two factors are bounded, and their strong* continuity proves continuity of \(u\). The final projection is \(p\), while

\[
 u_t^*u_t=B^{it}pB^{-it}=\sigma_t^\psi(p).
\]

The spatial implementation formulas give (WC.7). Inserting \(B^{-is}B^{is}\) and using that \(B^{is}\) implements \(\sigma_s^\psi\) gives the cocycle identity in (WC.6); no product of unbounded operators is used.

For intrinsicness, put \(\Theta=\theta\oplus\psi\) on \(M_2(M)\). The direct spatial derivative is \(A\oplus B\), including the zero extension of the first summand. Therefore

\[
 \sigma_t^\Theta(p\otimes e_{12})
 =u_t\otimes e_{12}.
 \tag{WC.9}
\]

The left side is determined by the intrinsic modular group of \(\Theta\). It is independent of \(\kappa\) and of the chosen faithful representation. Formula (WC.9) is consequently an intrinsic definition of (WC.5). The supported inverse theorem proves the converse: a family satisfying the support and cocycle laws determines exactly one normal semifinite numerator.

## The balanced centralizer records every comparison

Let \(\varphi_1,\varphi_2\) be normal semifinite weights, let \(\psi\) be normal semifinite and faithful, and put \(P=M_2(M)\). Define

\[
 \begin{aligned}
 \Phi&=\varphi_1\oplus\varphi_2\quad\text{on }P,\\
 p_j&=s(\varphi_j).
 \end{aligned}
 \tag{WC.10}
\]

The centralizer \(P_\Phi\) is understood in the support corner
\((p_1\otimes e_{11}+p_2\otimes e_{22})P(p_1\otimes e_{11}+p_2\otimes e_{22})\).

Let \(w\in M\) be a partial isometry with

\[
 \begin{aligned}
 w^*w&=p_2,\qquad q=ww^*,\\
 q&\in\operatorname{Proj}(M_{\varphi_1}).
 \end{aligned}
 \tag{WC.11}
\]

Define \((\varphi_1)_w(x)=\varphi_1(wxw^*)\). The following conditions are equivalent:

1. \(\varphi_2=(\varphi_1)_w\);
2. \(w\otimes e_{12}\in P_\Phi\);
3. for every \(t\in\mathbb R\),

   \[
   \begin{aligned}
   [D\varphi_2:D\psi]_t
   &=w^*[D\varphi_1:D\psi]_t\\
   &\qquad{}\cdot\sigma_t^\psi(w).
   \end{aligned}
   \tag{WC.12}
   \]

Here is a proof retaining the support placements. Use the same commutant reference \(\kappa\) and write \(A_j=d\varphi_j/d\kappa\), \(B=d\psi/d\kappa\). Since \(q\in M_{\varphi_1}\), it reduces \(A_1\). On \(p_2H\), transport of the coefficient form through the corner isomorphism \(x\mapsto wxw^*\) gives

\[
 \frac{d(\varphi_1)_w}{d\kappa}=w^*A_1w.
 \tag{WC.13}
\]

Consequently condition 1 implies

\[
 A_2^{it}=w^*A_1^{it}w.
\]

Multiplication on the right by \(B^{-it}\) gives (WC.12), because

\[
 w^*A_1^{it}wB^{-it}
 =w^*A_1^{it}B^{-it}\,B^{it}wB^{-it}.
\]

Conversely, (WC.12) multiplied on the right by \(B^{it}\) gives equality of the supported imaginary-power groups. Spectral uniqueness gives (WC.13) with \(A_2\) on the left, and spatial recovery gives condition 1.

Write \(u_{j,t}=[D\varphi_j:D\psi]_t\) and \(z=w\otimes e_{12}\). The derivative of the balanced weight is \(A_1\oplus A_2\). Hence, with \(v_t\) denoting the coefficient in the first row,

\[
 \begin{aligned}
 v_t&=u_{1,t}\sigma_t^\psi(w)u_{2,t}^*,\\
 \sigma_t^\Phi(z)&=v_t\otimes e_{12}.
 \end{aligned}
 \tag{WC.14}
\]

The matrix element is fixed by \(\sigma^\Phi\) exactly when (WC.12) holds. This proves all three equivalences.

Inside \(P_\Phi\), two projection consequences now follow without further modular computation:

\[
 \begin{aligned}
 \varphi_2\precsim\varphi_1
 &\Longleftrightarrow\\
 p_2\otimes e_{22}&\precsim p_1\otimes e_{11},
 \end{aligned}
 \tag{WC.15}
\]

and

\[
 \begin{aligned}
 \varphi_1\sim\varphi_2
 &\Longleftrightarrow\\
 p_1\otimes e_{11}&\sim p_2\otimes e_{22}.
 \end{aligned}
 \tag{WC.16}
\]

Indeed, a partial isometry in the indicated off-diagonal corner is uniquely \(w\otimes e_{12}\), and WC.11–14 identify precisely when it belongs to the balanced centralizer.

There is also a coordinate-free version of the cut-transport clause. Let \(q_i\in\operatorname{Proj}(M_{\varphi_1})\), and choose partial isometries \(v_i\) with \(v_iv_i^*=q_i\). Put

\[
 \theta_i(x)=\varphi_1(v_i x v_i^*).
\]

Then, with the comparison on the right taken in \(M_{\varphi_1}\),

\[
 \theta_1\precsim\theta_2\quad\Longleftrightarrow\quad q_1\precsim q_2.
 \tag{WC.17}
\]

For the forward direction, transport the comparison partial isometry by \(v_2(\cdot)v_1^*\). For the reverse direction, if \(a^*a=q_1\) and \(aa^*\leq q_2\), then \(v_2^*av_1\) transports the corresponding cut of \(\theta_2\) onto \(\theta_1\). Centralizer cyclicity from Recognize exactly the fixed observations verifies the weight equality, including infinite values.

The symmetric initial/final placement in (WC.17) is deliberate. The printed XII.4.3(iv) displays \(u^*u\) for one centralizer projection and \(vv^*\) for the other, while the surrounding definition and XII.4.3(i) require the centralizer projections to be the ranges of both transporters, or equivalently the initial projections of both adjoint transporters. Equation (WC.17) is invariant under that choice and is the typed statement proved here.

## Cantor–Bernstein for normal semifinite weights

**Foundation input.** Schröder–Bernstein for projections, TY Proposition 5.1, states that mutual Murray–von Neumann subequivalence of projections in any von Neumann algebra implies equivalence. The foundation lesson retains statement ownership. We retain the following alternative shift proof to exhibit the partial isometry used in the weight application.

**Alternative proof of the projection lemma.** Let \(e,f\) be projections in a von Neumann algebra \(N\), and suppose \(e\precsim f\) and \(f\precsim e\). Choose partial isometries \(a,b\in N\) with

\[
 \begin{aligned}
 a^*a&=e,\qquad aa^*\leq f,\\
 b^*b&=f,\qquad bb^*\leq e.
 \end{aligned}
 \tag{WC.18}
\]

Set \(s=ba\), an isometry from \(e\) into \(e\), and let

\[
 \begin{aligned}
 r_0&=e-bb^*,\\
 r_n&=s^nr_0s^{*n},\\
 r&=\sum_{n\geq0}r_n.
 \end{aligned}
 \tag{WC.19}
\]

The projections \(r_n\) are mutually orthogonal because \(r_0\perp ss^*\). Their strong sum belongs to \(N\), and

\[
 srs^*=r-r_0.
 \tag{WC.20}
\]

Since \(r_0b=0\), equation (WC.20) gives

\[
 \begin{aligned}
 b^*rb&=b^*(r-r_0)b\\
 &=ara^*.
 \end{aligned}
 \tag{WC.21}
\]

Now

\[
 c=ar+b^*(e-r)
 \tag{WC.22}
\]

has orthogonal initial pieces \(r,e-r\). Its final pieces are also orthogonal, and (WC.21) shows that they sum to \(f\). Thus \(c^*c=e\), \(cc^*=f\), proving \(e\sim f\).

Apply this lemma in \(P_\Phi\). If \(\varphi_1\precsim\varphi_2\) and \(\varphi_2\precsim\varphi_1\), formula (WC.15) gives both projection subequivalences between \(p_1\otimes e_{11}\) and \(p_2\otimes e_{22}\). The projection lemma and (WC.16) yield

\[
 \boxed{\ \varphi_1\sim\varphi_2\ }.
 \tag{WC.23}
\]

This includes the zero weight: its support is zero, and mutual subequivalence then forces both supports to vanish.

## Strict semifiniteness is semifiniteness on the centralizer

Call a normal semifinite weight \(\varphi\) **strictly semifinite** when

\[
 \varphi=\sum_{i\in I}\omega_i
 \tag{WC.24}
\]

for bounded normal positive functionals \(\omega_i\) whose supports are pairwise orthogonal. The sum is the pointwise supremum over finite subsets of \(I\). On an algebra with separable predual the nonzero family is automatically countable, but the proof does not require that reduction.

**Theorem.** A normal semifinite weight \(\varphi\) is strictly semifinite if and only if its restriction to \(M_\varphi\) is semifinite.

Suppose first that (WC.24) holds and put \(e_i=s(\omega_i)\). Orthogonality gives

\[
 \begin{aligned}
 \varphi(x)&=\sum_i\varphi(e_i x e_i),\\
 \omega_i&=\varphi_{e_i}.
 \end{aligned}
 \tag{WC.25}
\]

Conjugation by the sign unitary \(2e_i-p\) in the support corner preserves every term of the sum. The projection criterion Justify spectral restriction before using it gives \(e_i\in M_\varphi\). Moreover \(\varphi(e_i)=\|\omega_i\|<\infty\), and the finite sums \(e_F=\sum_{i\in F}e_i\) increase strongly to \(p\). For bounded \(x\in(M_\varphi)_+\), the net \(x^{1/2}e_Fx^{1/2}\) increases strongly to \(x\). Centralizer cyclicity identifies its weight with \(\varphi(e_Fxe_F)\), which is at most \(\|x\|\varphi(e_F)<\infty\). Thus finite positive elements are order dense in the centralizer, and \(\varphi|_{M_\varphi}\) is semifinite.

Conversely suppose \(\tau=\varphi|_{M_\varphi}\) is semifinite. It is a faithful normal semifinite trace on the support algebra. Choose, by the maximal principle, a maximal orthogonal family \((e_i)\) of nonzero projections in \(M_\varphi\) with \(\tau(e_i)<\infty\). If \(p-\sum_i e_i\) were nonzero, semifiniteness of \(\tau\) would produce another nonzero finite projection under it, contradicting maximality. Hence \(\sum_i e_i=p\). Each

\[
 \omega_i(x)=\varphi(e_i x e_i)
 \tag{WC.26}
\]

is bounded and normal, with support \(e_i\). Centralizer cyclicity and normality give, for \(x\in M_+\),

\[
 \begin{aligned}
 \varphi(x)&=\sup_{F\Subset I}\varphi(e_Fxe_F)\\
 &=\sup_{F\Subset I}\sum_{i\in F}\omega_i(x).
 \end{aligned}
 \tag{WC.27}
\]

Thus (WC.24) holds. This proof also shows why an arbitrary orthogonal decomposition of the identity is insufficient: the pieces must have finite \(\varphi\)-mass and lie in the centralizer.

## A lacunary functional carries ambient maximal abelian algebras

Let \(\omega\in M_*^+\) be faithful. For a compact interval \(K\subset\mathbb R\), write \(M^\omega(K)\) for the Arveson spectral subspace of the modular action \(\sigma^\omega\). Call \(\omega\) **lacunary** when there is \(\delta>0\) such that

\[
 M^\omega([ -\delta,\delta])=M_\omega.
 \tag{WC.28}
\]

**Spectral inputs.** Use the positive Fourier convention \(f(s)=\int k(t)e^{its}\,dt\) and \(\alpha_f y=\int k(t)\alpha_t(y)\,dt\), with \(\alpha=\sigma^\omega\). The exact action-spectral inputs are the filter law, weak-star approximation, local cutoffs and closed-space criterion in OA-FLOW lesson 17, equations S4–S6, S9 and S13–S16; lesson 78, compact cutoff L3 and localization sandwich L6; and lesson 84, adjoint reflection A4 and product-frequency inclusion A9–A10. General action spectral calculus retains OA-FLOW ownership. The Hilbert-space measure and modular domains below use SK04–07, TC07–08 and TC10, the finite-domain involution, and the GNS modular implementation.

We use the following localized spanning fact. If \(C\subseteq M\) is a sigma-weakly closed subspace invariant under \(\sigma^\omega\), then, as \(a\in\mathbb R\) and \(\varepsilon>0\) vary, \(C\) is the sigma-weak closed span of

\[
 C\cap M^\omega([a-\varepsilon,a+\varepsilon]).
 \tag{WC.29}
\]

Indeed, every filter preserves \(C\): normal functionals vanishing on \(C\) annihilate its orbit integral. S9 approximates an element weak-star by its filtered orbit; the norm density of compactly supported Fourier functions and the filter bound S5 permit compact Fourier support. Cover that support by finitely many intervals of the prescribed radius. The local cutoffs of lesson 17 give functions \(c_j\) supported in those intervals and equal to one on smaller neighborhoods covering the compact set. The finite assembly \(q_1=c_1\), \(q_j=c_j\prod_{l<j}(1-c_l)\) has sum one on the support. Expanding the products keeps every \(q_j\) in the Fourier algebra even though its constant unit need not belong to that algebra. Thus \(f=\sum_jfq_j\), and S16 puts each filtered term in the required band. These are weak-star limits; no norm continuity of an arbitrary operator orbit or Hilbert-space separability is assumed. L3 fixes a vector with compact spectrum, and L6 supplies the corresponding passage between closed spectral spaces and open localization.

Let \(A\) be maximal abelian in \(M_\omega\), and put \(C=A'\cap M\). Since \(A\) is fixed pointwise, \(C\) is invariant. Take

\[
 x\in C\cap M^\omega([a-\delta/2,a+\delta/2]).
 \]

By A4 and A10, both \(x^*x\) and \(xx^*\) have spectrum in \([ -\delta,\delta]\), hence belong to \(C\cap M_\omega=A\). Their support projections \(p=s(x^*x)\) and \(q=s(xx^*)\) also belong to \(A\). Since \(x\in A'\), the identities \(xp=x\) and \(qx=x\) imply \(px=x\) and \(xq=x\). The first implies \(q\leq p\), and the second implies \(p\leq q\), so \(p=q\). In the polar decomposition \(x=v|x|\), the partial isometry lies in the von Neumann algebra \(C\), is unitary on \(pH\), and commutes with \(|x|\in A\). It follows that \(xx^*=x^*x\): \(x\) is normal.

We justify the spectral measure and its imaginary-time moment directly. Since \(\omega\) is bounded, its GNS map is defined on all of \(M\) and has \(\|\Lambda_\omega(y)\|\leq\omega(1)^{1/2}\|y\|\), by WG006. Put \(\xi=\Lambda_\omega(x)\), \(B=\log\Delta_\omega\) and \(U_t=e^{itB}=\Delta_\omega^{it}\). SK07 gives the actual self-adjoint logarithm, and MF06 gives \(U_t\Lambda_\omega(y)=\Lambda_\omega(\alpha_t(y))\). For every Fourier filter,

\[
 \Lambda_\omega(\alpha_f x)=f(B)\xi.
 \tag{WC.43}
\]

To prove this identity, pair the left side with \(\Lambda_\omega(y)\). The resulting normal functional \(\omega(y^*\,\cdot\,)\) passes through the weak-star integral. MF06 identifies its integrand with the coefficient of \(U_t\xi\). The spectral theorem and scalar Fubini identify the norm-integrable vector \(\int k(t)U_t\xi\,dt\) with \(f(B)\xi\). Density of the GNS vectors proves (WC.43); no integral is passed formally through an unbounded GNS map.

Let \(E_B\) be the spectral resolution of \(B\), and put \(K=[a-\delta/2,a+\delta/2]\). The finite positive measures

\[
 \begin{gathered}
 \mu_x(D)=\|E_B(D)\xi\|^2,\\
 \nu_x(D)=\mu_x(-D)
 \end{gathered}
 \tag{WC.44}
\]

are defined for Borel \(D\subseteq\mathbb R\). The measure \(\mu_x\) is supported in \(K\). In fact, for each compact set \(L\subseteq\mathbb R\setminus K\), choose a Fourier cutoff \(c\) equal to one near \(L\) and supported off \(K\). S14 gives \(\alpha_c x=0\), and (WC.43) gives \(c(B)\xi=0\). SK04–05 imply \(\mu_x(L)=0\). The compact sets \(\{s:|s|\leq n,\ d(s,K)\geq1/n\}\) cover the complement, so it has zero measure. This countability concerns the scalar real line, not the Hilbert space. Consequently \(\nu_x\) is supported in \(-K\).

The entire function

\[
 \begin{aligned}
 F(z)&=\int_K e^{-izs}\,d\mu_x(s)\\
 &=\int_{-K}e^{izs}\,d\nu_x(s)
 \end{aligned}
 \tag{WC.45}
\]

is well defined because the measures have compact support. On the real axis its first integral equals \(\langle\xi,U_t\xi\rangle\), with the linear-first convention, so it is positive definite and equals \(\omega(\alpha_t(x^*)x)\). Every \(\Lambda_\omega(y)\) is in the initial involution domain, with \(S\Lambda_\omega(y)=\Lambda_\omega(y^*)\), by WH10. TC07–08 give \(D(S)=D(\Delta_\omega^{1/2})\) and \(S=J\Delta_\omega^{1/2}\); TC10 gives \(JU_t=U_tJ\). Put \(\eta=\Delta_\omega^{1/2}\xi\) and \(\zeta=S\xi\). Therefore

\[
 \begin{aligned}
 F(t+i)&=\langle\eta,U_t\eta\rangle\\
 &=\langle U_t\zeta,\zeta\rangle.
 \end{aligned}
 \tag{WC.46}
\]

The second pairing is \(\omega(x\alpha_t(x^*))\). Thus this same function has the KMS boundary values

\[
 \begin{aligned}
 F(t)&=\omega(\sigma_t^\omega(x^*)x),\\
 F(t+i)&=\omega(x\sigma_t^\omega(x^*)).
 \end{aligned}
 \tag{WC.30}
\]

In particular its imaginary-time moment and real value are

\[
 \begin{aligned}
 F(i)&=\|\Delta_\omega^{1/2}\xi\|^2\\
 &=\|S\xi\|^2=\omega(xx^*),\\
 F(0)&=\|\xi\|^2=\omega(x^*x).
 \end{aligned}
 \tag{WC.47}
\]

The representing positive measure \(\nu_x\) is supported in \([ -a-\delta/2,-a+\delta/2]\). Consequently, if \(a>\delta\),

\[
 F(i)\geq e^{a-\delta/2}F(0).
 \tag{WC.31}
\]

Normality of \(x\) gives \(F(i)=F(0)\). Since the scalar factor in (WC.31) exceeds one, faithfulness forces \(x=0\). Applying the same argument to \(x^*\), with A4, removes intervals centered below \(-\delta\).

To pass from bands to all of \(C\), take any compactly supported Fourier function \(f\) whose support misses \([ -\delta,\delta]\). Cover its compact support by intervals of radius \(\delta/2\) centered at points with \(|a|>\delta\), and use the finite assembly above. Every corresponding filtered term belongs to \(C\), lies in one of the bands just shown to vanish, and is therefore zero. Hence \(\alpha_f y=0\) for every \(y\in C\). The exact closed-space criterion S14 now gives \(C\subseteq M^\omega([ -\delta,\delta])=M_\omega\). This argument avoids enlarging the final spectral set when taking a closed span of bands. Hence

\[
 A'\cap M=A'\cap M_\omega=A.
 \tag{WC.32}
\]

Thus every maximal abelian subalgebra of \(M_\omega\) is already maximal abelian in \(M\). In particular,

\[
 M_\omega'\cap M=\mathcal Z(M_\omega),
 \tag{WC.33}
\]

because an element commuting with \(M_\omega\) commutes with \(A\), hence lies in \(A\subseteq M_\omega\). The zero algebra case is immediate. These are proofs relative to the exact named spectral and modular inputs.

## Centralizer inclusion and a central affiliated density

Let \(\varphi,\psi\) be normal semifinite faithful weights and assume

\[
 M_\varphi'\cap M=\mathcal Z(M_\varphi).
 \tag{WC.34}
\]

Then the following are equivalent:

1. \(M_\varphi\subseteq M_\psi\);
2. there is a positive nonsingular self-adjoint operator \(h\), affiliated with \(\mathcal Z(M_\varphi)\), such that

   \[
   \psi=\varphi_h.
   \tag{WC.35}
   \]

Condition 2 implies condition 1 by the modular formula Recover modular time on the support: \(h^{it}\) is central in \(M_\varphi\), so the perturbed modular group fixes every element of \(M_\varphi\).

Conversely put \(u_t=[D\psi:D\varphi]_t\). If \(x\in M_\varphi\), then condition 1 and the cocycle intertwining identity give

\[
 x=\sigma_t^\psi(x)=u_t x u_t^*.
\]

Thus \(u_t\in M_\varphi'\cap M=\mathcal Z(M_\varphi)\). In particular \(\sigma_s^\varphi(u_t)=u_t\), so the cocycle law becomes the ordinary group law \(u_{s+t}=u_su_t\). The strongly continuous group has the form \(u_t=h^{it}\) for a unique positive nonsingular self-adjoint \(h\) affiliated with \(\mathcal Z(M_\varphi)\). The fixed-density theorem gives (WC.35).

For a separable factor of type \(\mathrm{III}_\lambda\), \(0\leq\lambda<1\), and a faithful strictly semifinite \(\varphi\), the type-dependent centralizer-MASA theorem supplies (WC.34). Under that explicit prerequisite, (WC.35) is exactly the centralizer-inclusion criterion for faithful strictly semifinite weights. Construction of that MASA in the type \(\mathrm{III}_0\) case uses flow and spectral invariants owned by OA-FLOW; it is not inferred here from strict semifiniteness alone.

## Faithful expectations preserve support, comparison, and orthogonal sums

Let \(Q\subseteq P\) be von Neumann algebras with the same identity, and let

\[
 E:P\longrightarrow Q
\]

be a faithful normal conditional expectation. For any normal semifinite weight \(\eta\) on \(Q\), write \(\widetilde{\eta}=\eta\circ E\). Let \(\rho\) be such a weight, not necessarily faithful, and put \(e=s(\rho)\).

First, \(\widetilde{\rho}\) is normal semifinite and

\[
 s(\widetilde{\rho})=e.
 \tag{WC.36}
\]

Normality is immediate from increasing positive nets. For semifiniteness choose positive contractions \(d_i\) in the finite domain of \(\rho\) with \(d_i\to1\) strongly. For \(x\in P\), put \(y_i=xd_i\) and \(a_i=d_iE(x^*x)d_i\). Bimodularity gives

\[
 \begin{aligned}
 \widetilde{\rho}(y_i^*y_i)&=\rho(a_i),\\
 \rho(a_i)&\leq\|x\|^2\rho(d_i^2),\\
 \|x\|^2\rho(d_i^2)&<\infty.
 \end{aligned}
 \tag{WC.37}
\]

The elements \(d_i x d_i\) therefore lie in the finite linear domain and converge strongly to \(x\). This proves semifiniteness. Equation (WC.1) and bimodularity give, for \(x\in P_+\),

\[
 \widetilde{\rho}(x)=\widetilde{\rho}(exe).
\]

On \(ePe\), faithfulness of \(E\) and of \(\rho|_{eQe}\) makes \(\widetilde{\rho}\) faithful. Hence its support is exactly \(e\).

Second, comparison is preserved:

\[
 \begin{aligned}
 \rho_1\precsim\rho_2
 &\Longrightarrow\\
 \widetilde{\rho_1}&\precsim\widetilde{\rho_2}.
 \end{aligned}
 \tag{WC.38}
\]

To see the centralizer placement, restrict to the support of \(\rho_2\). The expectation remains faithful and normal on that corner, and the modular expectation theorem gives

\[
 \left.\sigma_t^{\widetilde{\rho_2}}\right|_{s(\rho_2)Qs(\rho_2)}
 =\sigma_t^{\rho_2}.
 \tag{WC.39}
\]

Thus every centralizer projection used in a cut of \(\rho_2\) is also a centralizer projection for the composite. If a partial isometry \(w\in Q\) implements the transported cut, put \(b_x=wE(x)w^*\) for \(x\in P_+\). Bimodularity gives

\[
 \widetilde{\rho_2}(wxw^*)=\rho_2(b_x).
 \tag{WC.40}
\]

This is the corresponding transported cut of \(\rho_2\circ E\), proving (WC.38).

Finally, let \((\rho_n)_{n\geq1}\) have pairwise orthogonal supports and put \(\rho_\Sigma=\sum_{n\geq1}\rho_n\). Formula (WC.36) keeps those supports pairwise orthogonal after composition, and for every \(x\in P_+\),

\[
 \begin{aligned}
 \sum_{n\geq1}\widetilde{\rho_n}(x)
 &=\sum_{n\geq1}\rho_n(E(x))\\
 &=\rho_\Sigma(E(x)).
 \end{aligned}
 \tag{WC.41}
\]

Therefore

\[
 \sum_{n\geq1}\widetilde{\rho_n}=\rho_\Sigma\circ E.
 \tag{WC.42}
\]

This expectation theorem is valid for general von Neumann algebras; no separability or factor assumption is used.

## Scope and ownership

WC-01–08 establish the scalar-weight comparison and transport statements relative to the displayed prerequisites. The type-dependent centralizer-MASA input used after (WC.34) remains an external OA-FLOW contract. Crossed products, dual actions, dual weights, flow classification, and action cohomology are outside this lesson.

## References

- M. Takesaki, *Theory of Operator Algebras II*, Springer, 2003, Chapter XII, §4.
- A. Connes, “Une classification des facteurs de type III,” *Annales scientifiques de l’École Normale Supérieure* 6 (1973), 133–252. [Open article](https://numdam.org/articles/10.24033/asens.1247/).
