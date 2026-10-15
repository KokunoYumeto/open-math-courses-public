# Closedness of the density part and the proof

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the closedness theorem of [Densities and planar tangent measures](densities-and-planar-tangent-measures.md) (Theorem 1.1 there) and then the main theorem of the course. The positive-density part \(\mathbf 1_EP\) is approached by currents \(b(f_r)P\), where \(f_r\) is a smoothed density at scale \(r\). Closedness of \(T=P+Q\) moves the derivative of the cutoff onto the current; against \(Q\) its size is controlled by square integrability, and against \(P\) only its derivative along the complex line of the current matters. Closedness of \(T\) converts that tangential derivative into normal derivatives paired with mixed forms. The normal derivatives are controlled by the transverse moment, which is \(o(r)\) in the mean, and the mixed forms by the angular bound, which is \(O(r^2)\); the product beats the normalization \(r^{-3}\).

- Density cutoffs; the density vanishes almost everywhere for the volume (Lemmas 1.1 and 1.2).
- The error from the square integrable correction (Lemma 2.1).
- Tangential derivatives of the cutoffs (Lemma 3.1, Proposition 3.2).
- Proof of the closedness theorem (Section 4).
- The final pairing and the proof of the main theorem (Theorem 5.1).

The lesson follows [OpenAI-TC, Sections 6 and 7]. The hypotheses and notation of Theorem 1.1 of the previous lesson are in force until Section 5: \(\lambda\), \(\mu\), the polarization \(A\), \(Q\), \(T=P+Q\), \(\sigma=\mu+|Q|\,dV\), the angular integral \(\mathcal I_r\le Cr^4\) and the transverse moment \(\mathcal N_r=o(r^2)\) of Proposition 4.1 there. \(M_r(x)=\mu(B_r(x))\).

## 1. Density cutoffs

Fix a smooth nonincreasing function \(h\colon[0,\infty)\to[0,\infty)\), positive at \(0\) and zero on \([\frac12,\infty)\), and put \(H(t)=h(t^2)\). For \(0<r<\rho_0\) let
\[
f_r(x)=r^{-2}\int_Xh\Bigl(\frac{d(x,y)^2}{r^2}\Bigr)d\mu(y) .
\]

**Lemma 1.1.** (1) \(f_r\) is smooth and \(0\le f_r\le C\). (2) \(f_r(x)\to c_h\theta(x)\) for every \(x\), where \(c_h=\int_0^1h(u)\,du>0\); in particular \(\theta\) is Borel. (3) \(|df_r(x)|\le Cr^{-3}M_r(x)\). (4) For \(x,y\) with \(d(x,y)<4\rho_0\) and \(v\in T_xX\),
\[
d_x\bigl[d(x,y)^2\bigr](v)=-2\langle z_x(y),v\rangle .
\]

*Proof.* (4) The squared distance is smooth on \(\{d<4\rho_0\}\), and the minimizing geodesic from \(x\) to \(y\) is \(t\mapsto\exp_x(tz_x(y))\), \(0\le t\le1\), depending smoothly on \(x\) and \(y\) (Theorems B.3 and B.5 of [Riemannian connections and convex neighbourhoods](course:DG-FND/riemannian-connections-and-convex-neighbourhoods)). Its energy is \(\frac12d(x,y)^2\). Moving the initial point along \(v\) with the end point fixed, the first variation formula (Theorem A.3 of [Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem)) gives the derivative \(-\langle\dot\gamma(0),v\rangle\) for the energy, and \(\dot\gamma(0)=z_x(y)\).

(1) The integrand vanishes unless \(d(x,y)<r/\sqrt2\), where it is smooth in \(x\); \(\mu\) is finite. Also \(f_r\le h(0)r^{-2}M_r(x)\le C\) by quadratic growth.

(2) \(H\) is nonincreasing with \(H(1)=0\), so \(H(d/r)=\int_0^1(-H'(\tau))\mathbf 1_{\{d<r\tau\}}\,d\tau\), and by Fubini's theorem
\[
f_r(x)=\int_0^1(-H'(\tau))\,r^{-2}M_{r\tau}(x)\,d\tau .
\]
Here \(r^{-2}M_{r\tau}(x)=\tau^2(r\tau)^{-2}M_{r\tau}(x)\to\tau^2\theta(x)\), dominated by \(C\tau^2\). The limit is \(c_h\theta(x)\), because integration by parts gives \(\int_0^1(-H')\tau^2\,d\tau=\int_0^12\tau H(\tau)\,d\tau=c_h\).

(3) By (4), \(|d_x[d(x,y)^2]|=2d(x,y)\le2r\) on the support, so \(|df_r(x)|\le r^{-4}\sup|h'|\,2r\,M_r(x)\). \(\blacksquare\)

**Lemma 1.2** ([OpenAI-TC, (6.2)]). \(\theta(x)=0\) for almost every \(x\) with respect to the volume.

*Proof.* Let \(E_k=\{\theta>1/k\}\), a Borel set. Fix a chart and a compact set \(K\) inside it, and use Lebesgue measure \(\mathcal L\) of the chart. Every point \(x\in E_k\cap K\) is the centre of arbitrarily small coordinate balls \(B\) of radius \(s\) with \(\mu(B)\ge c\,s^2/k\), since \(B\) contains a geodesic ball of radius \(s/C\) and \(\mu(B_\rho(x))\ge\rho^2/(2k)\) for small \(\rho\). Fix \(\delta>0\) and use only such balls of radius less than \(\delta\). By Theorem 4.1 of [Besicovitch's covering theorem and the differentiation of Radon measures](course:measurable-fields-and-direct-integrals/besicovitch-s-covering-theorem-and-the-differentiation-of-radon-measures), applied to \(\mathcal L\), there are countably many disjoint such balls \(B_i\), of radii \(s_i\), covering \(\mathcal L\)-almost all of \(E_k\cap K\). Then
\[
\begin{aligned}
\mathcal L^*(E_k\cap K)&\le\sum_iCs_i^4\le C\delta^2\sum_is_i^2\\
&\le Ck\delta^2\sum_i\mu(B_i)\le Ck\delta^2 .
\end{aligned}
\]
Letting \(\delta\to0\), \(E_k\cap K\) is null. Countably many \(k\), \(K\) and charts cover \(\{\theta>0\}\). \(\blacksquare\)

## 2. The error from the correction

**Lemma 2.1** ([OpenAI-TC, (6.3), (6.4)]). As \(r\to0\),
\[
\begin{gathered}
r^{-3}\int_X|Q|\,M_r\,dV\longrightarrow0,\\
\int_X|Q|\,|df_r|\,dV\longrightarrow0 .
\end{gathered}
\]

*Proof.* By Cauchy–Schwarz,
\[
\begin{aligned}
r^{-3}\int|Q|M_r&\le\Bigl(\int|Q|^2r^{-2}M_r\Bigr)^{1/2}\\
&\quad\times\Bigl(\int r^{-4}M_r\Bigr)^{1/2} .
\end{aligned}
\]
By Fubini's theorem, \(\int_XM_r\,dV=\int_X\mathrm{vol}(B_r(y))\,d\mu(y)\le Cr^4\), so the second factor is bounded. In the first, \(r^{-2}M_r\le C\), and \(r^{-2}M_r\to\theta=0\) almost everywhere by Lemma 1.2; dominated convergence with \(|Q|^2\in L^1\) gives zero. The second claim follows from Lemma 1.1(3). \(\blacksquare\)

## 3. Tangential derivatives

**Lemma 3.1** (coordinate and transported forms). Let \(z\) be normal coordinates at \(x\) with respect to an orthonormal basis \(e_1,\dots,e_4\) of \(T_xX\), with dual basis \(e^1,\dots,e^4\), and let \(\tau_{xy}\) be parallel transport along the radial geodesic from \(x\) to \(y\). Write \(dz^{ij}=dz^i\wedge dz^j\) and \(e^{ij}=e^i\wedge e^j\). Then at \(y\), with \(|z|=d(x,y)<4\rho_0\),
\[
dz^{ij}=\tau_{xy}e^{ij}+O(|z|^2) ,
\]
uniformly in \(x\). Consequently, for \(m\in\mathscr C_y\), \(dz^{ij}(m)=\langle e^{ij},\tau_{yx}m\rangle+O(|z|^2)\).

*Proof.* \(\partial_{z_i}|_y=(d\exp_x)_z(e_i)=J(1)\) for the Jacobi field \(J\) along \(\gamma(t)=\exp_x(tz)\) with \(J(0)=0\), \(J'(0)=e_i\) (Theorems A.1 and B.2 of the lesson on Jacobi fields). In a parallel orthonormal frame along \(\gamma\), \(J''=-R(J,\dot\gamma)\dot\gamma\) and \(|\dot\gamma|=|z|\), so \(u(t)=J(t)-te_i\) satisfies \(u(0)=u'(0)=0\) and \(|u''|\le C|z|^2(|u|+t)\). For \(|z|\) small this gives \(|u(t)|\le C|z|^2\) on \([0,1]\). Thus \(\tau_{yx}\circ(d\exp_x)_z=\mathrm{id}+O(|z|^2)\), and inverting, the coordinate covectors are \(dz^i|_y=e^i\circ\tau_{yx}+O(|z|^2)\). Products give the claim for two-forms, and transport is an isometry. \(\blacksquare\)

**Proposition 3.2** ([OpenAI-TC, (6.5)]). Write \(|df_r(x)|_{L_\ell}\) for the norm of the restriction of \(df_r(x)\) to the plane \(L_\ell\). Then
\[
\int_{\mathscr C}|df_r(x)|_{L_\ell}\,d\lambda(x,\ell)\longrightarrow0 .
\]

*Proof.* Fix \((x,\ell)\), an orthonormal basis \(e_1,e_2\) of \(L_\ell\) with \(\ell=e_1\wedge e_2\), and \(e_3,e_4\) spanning \(L_\ell^\perp\). Let \(z=z_x\) be the corresponding normal coordinates and \(h_r(z)=h(|z|^2/r^2)\), a smooth function supported in \(B_r(x)\). For \(y\in B_r(x)\) and \(m\in\mathscr C_y\) put
\[
\delta=|\ell-\tau_{yx}m|,\qquad z^\perp=\mathrm{pr}_{L_\ell^\perp}z_x(y) .
\]

*The tangential derivative as a current.* By Lemma 1.1(4), for \(i=1,2\),
\[
df_r(x)e_i=-r^{-2}\int\partial_{z_i}h_r\,d\mu(y) .
\]
By Lemma 3.1, \(dz^{12}(m)=\langle\ell,\tau_{yx}m\rangle+O(r^2)\), and \(\langle\ell,\tau_{yx}m\rangle=1-\frac12\delta^2\). Since \(|\partial h_r|\le C/r\),
\[
\begin{aligned}
&\Bigl|df_r(x)e_i+r^{-2}T\bigl(\partial_{z_i}h_r\,dz^{12}\bigr)\Bigr|\\
&\quad\le Cr^{-3}\int_{\{d(x,y)<r\}}(\delta^2+r^2)\,d\lambda(y,m)\\
&\qquad+Cr^{-3}\int_{B_r(x)}|Q|\,dV .
\end{aligned}
\]
Integrated against \(\lambda(x,\ell)\), the right side is at most \(Cr^{-3}\mathcal I_r+Cr^{-1}\int M_r\,d\mu\) plus \(Cr^{-3}\int|Q|M_r\,dV\), which tends to zero by the angular bound, quadratic growth and Lemma 2.1.

*Closure moves the derivative off the plane.* The one-forms \(h_r\,dz^1\) and \(h_r\,dz^2\) are smooth with compact support in the chart, and \(T\) is closed. Since \(d(dz^j)=0\),
\[
\begin{aligned}
T(\partial_1h_r\,dz^{12})&=-\sum_{a=3,4}T(\partial_ah_r\,dz^{a2}),\\
T(\partial_2h_r\,dz^{12})&=\sum_{a=3,4}T(\partial_ah_r\,dz^{a1}) .
\end{aligned}
\]
For \(a=3,4\), \(|\partial_ah_r|=2r^{-2}|h'|\,|z_a|\le Cr^{-1}|z^\perp|/r\). By Lemma 3.1, and since \(e^{aj}\) is orthogonal to \(\ell\) for \(j=1,2\),
\[
\begin{aligned}
|dz^{aj}(m)|&\le|\langle e^{aj},\tau_{yx}m-\ell\rangle|+Cr^2\\
&\le\delta+Cr^2 .
\end{aligned}
\]
Hence, with the outer factor \(r^{-2}\), the four terms are at most
\[
\begin{aligned}
&Cr^{-3}\int_{\{d<r\}}\delta\,\frac{|z^\perp|}r\,d\lambda(y,m)\\
&\quad+Cr^{-1}M_r(x)+Cr^{-3}\int_{B_r(x)}|Q|\,dV .
\end{aligned}
\]
After integration against \(\lambda(x,\ell)\), the last two terms tend to zero by quadratic growth and Lemma 2.1. By Cauchy–Schwarz the first is at most
\[
\begin{aligned}
Cr^{-3}\,\mathcal I_r^{1/2}\,\mathcal N_r^{1/2}&=r^{-3}\,O(r^2)\,o(r)\\
&=o(1) ,
\end{aligned}
\]
because the square of \(|z^\perp|/r\), integrated over \(\lambda(y,m)\) and \(\lambda(x,\ell)\) on \(\{d<r\}\), is exactly \(\mathcal N_r\): it does not depend on \(m\). Since \(|df_r(x)|_{L_\ell}\le|df_r(x)e_1|+|df_r(x)e_2|\), the proposition follows. \(\blacksquare\)

All derivatives were taken at the fixed centre \(x\) in a fixed chart; no derivative of a frame that depends on the centre occurs.

## 4. Proof of the closedness theorem

*Proof of Theorem 1.1 of [Densities and planar tangent measures](densities-and-planar-tangent-measures.md).* The density exists by Proposition 2.1 there. Let \(b\colon\mathbb R\to\mathbb R\) be smooth with \(b(0)=0\); on the bounded range of the \(f_r\), \(b\) and \(b'\) are bounded.

*Limits.* For a smooth form \(\alpha\),
\[
\begin{aligned}
T(b(f_r)\alpha)&=\int b(f_r)\langle\alpha,A\rangle\,d\mu\\
&\quad+\int b(f_r)\langle\alpha,Q\rangle\,dV .
\end{aligned}
\]
By Lemma 1.1(2) and dominated convergence, this tends to \(\int b(c_h\theta)\langle\alpha,A\rangle\,d\mu\): the second integral tends to \(\int b(c_h\theta)\langle\alpha,Q\rangle\,dV\), which is zero because \(\theta=0\) almost everywhere (Lemma 1.2) and \(b(0)=0\). So the currents \(b(f_r)T\) converge to \(b(c_h\theta)P\).

*Closedness.* For a smooth one-form \(\eta\), \(d(b(f_r)\eta)=b(f_r)\,d\eta+b'(f_r)\,df_r\wedge\eta\), and \(T\) is closed, so
\[
T(b(f_r)\,d\eta)=-T\bigl(b'(f_r)\,df_r\wedge\eta\bigr) .
\]
The \(Q\) part is at most \(C\|\eta\|_\infty\int|Q||df_r|\,dV\to0\) by Lemma 2.1. In the \(P\) part, for \(\ell=e_1\wedge e_2\), \((df_r\wedge\eta)(\ell)\) equals \(df_r(e_1)\eta(e_2)-df_r(e_2)\eta(e_1)\), so it is at most \(C\|\eta\|_\infty\int|df_r(x)|_{L_\ell}\,d\lambda\to0\) by Proposition 3.2. Hence \(b(c_h\theta)P\) annihilates \(d\eta\): it is closed.

*The indicator.* Take \(b_n(s)=1-e^{-ns}\). Since \(\theta\ge0\), \(0\le b_n(c_h\theta)\le1\) and \(b_n(c_h\theta)\to\mathbf 1_E\) pointwise. Dominated convergence gives \(b_n(c_h\theta)P\to\mathbf 1_EP\) as currents, and closedness passes to the limit. The limits are taken one after the other: \(r\to0\) for each fixed \(n\), then \(n\to\infty\); no bound on \(b_n'\) uniform in \(n\) is needed. \(\blacksquare\)

## 5. The final pairing

**Theorem 5.1** (Theorem 2.1 of [Taming, compatibility and a separating current](taming-compatibility-and-a-separating-current.md); [OpenAI-TC, Theorem 1.1]). Assume the hypothesis (HK) of [Regularization and angular control](regularization-and-angular-control.md). Let \(J\) be a smooth almost complex structure on a closed connected four-manifold \(X\). If a closed two-form tames \(J\), then a closed two-form is compatible with \(J\).

*Proof.* Let \(\omega\) be a closed form taming \(J\), and suppose that no closed form is compatible with \(J\). Proposition 5.1 of the first lesson gives \(P\), \(Q\), \(T\), \(\lambda\) and \(\mu\). The hypotheses of Theorem 1.1 of the previous lesson hold: \(Q\) is anti-invariant, \(T\) is closed, \(\mu\) has quadratic growth by Proposition 4.1 of [Quadratic mass growth](quadratic-mass-growth.md), and \(Q\in L^2\) with \(\mathcal I_r\le Cr^4\) by Proposition 6.1 of the third lesson. So \(P_E=\mathbf 1_EP\) is closed, with \(E=\{\theta>0\}\).

Let \(P'=\mathbf 1_{X\setminus E}P\), the subcurrent of the measure \(\lambda'=\mathbf 1_{\pi^{-1}(X\setminus E)}\lambda\le\lambda\), with projection \(\mu'=\mathbf 1_{X\setminus E}\mu\), and
\[
T'=P'+Q=T-P_E ,
\]
a closed current in \(H^{-4}\). We pair \(T\) with \(T'\) instead of with itself: the second positive factor now lives on points of zero density, and there the negative error in the pairing disappears.

*The negative error vanishes.* For \(y\notin E\),
\[
r^{-2}\int_X\Bigl(1+\frac{d(x,y)}r\Bigr)^{-6}d\mu(x)\longrightarrow0 .
\]
Indeed, the ball \(B_r(y)\) contributes at most \(r^{-2}\mu(B_r(y))\to\theta(y)=0\); the shell \(2^jr\le d<2^{j+1}r\) contributes at most \(4^{j+1}2^{-6j}(2^{j+1}r)^{-2}\mu(B_{2^{j+1}r}(y))\), which tends to zero for each \(j\) and is at most \(C2^{-4j}\) by quadratic growth. These bounds are uniform in \(y\), so dominated convergence against \(\mu'\), which lives on \(X\setminus E\), shows that the negative term of Lemma 4.2(3) of the third lesson tends to zero. Discarding its nonnegative angular term,
\[
\liminf_{r\to0}\langle S_rP,*S_rP'\rangle\ge0 .
\]

*The correction vanishes.* Lemma 2.1 of the third lesson, applied to the closed current \(T'\), gives
\[
\begin{aligned}
0&=\langle S_rP,*S_rP'\rangle+\langle S_rP,*S_rQ\rangle\\
&\quad+\langle S_rQ,*S_rP'\rangle+\|S_rQ\|^2 .
\end{aligned}
\]
The two middle terms tend to zero by Proposition 6.1 of the third lesson, applied once to \(P\) and once to \(P'\), since \(\langle S_rQ,*S_rP'\rangle=\langle S_rP',*S_rQ\rangle\). Also \(S_rQ\to Q\) in \(L^2\). Therefore \(\|Q\|^2=-\lim_{r\to0}\langle S_rP,*S_rP'\rangle\le0\), and \(Q=0\).

*Contradiction.* Now \(T=P\), so \(P\) annihilates every closed form, in particular \(\omega\). But \(\omega_x(\ell)=\omega(v,Jv)>0\) for \(\ell=v\wedge Jv\in\mathscr C_x\), so \(\omega\) has a positive minimum \(m\) on the compact set \(\mathscr C\), and \(P(\omega)=\int\omega_x(\ell)\,d\lambda\ge m\). This contradiction shows that the positive definite invariant forms meet the closed invariant forms; a form in the intersection is closed and compatible with \(J\). \(\blacksquare\)

The theorem is proved in the programme from the named hypothesis (HK) on the heat kernel, which enters only through the kernel of \(S_r^2\) (Lemma 3.1 of the third lesson). The argument also proves Theorem 1.1 of the previous lesson in its general form: for a positive current with an anti-invariant square integrable correction making it closed, quadratic growth and the angular bound alone imply that its positive-density part is closed.

## 6. Exercises

**6.1.** Check that \(\int_0^1(-H'(\tau))\tau^2\,d\tau=\int_0^1h(u)\,du\) for \(H(\tau)=h(\tau^2)\) with \(h=0\) on \([\frac12,\infty)\).

**6.2.** Let \(\Sigma\) be a closed embedded surface and \(P\) the current of integration over \(\Sigma\), \(P(\alpha)=\int_\Sigma\alpha\). Show that \(P\) is closed, but that \(\mathbf 1_UP\) is not closed for an open ball \(U\) whose boundary sphere meets \(\Sigma\) transversally. Why does this not contradict Theorem 1.1 of the previous lesson?

**6.3.** For \(\ell=e_1\wedge e_2\) and a unit bivector \(m'\), show that \(|\langle e^3\wedge e^1,m'\rangle|\le|\ell-m'|\).

**6.4.** Where in the proof of Theorem 5.1 is it used that \(\omega\) is closed, and where that it tames \(J\)?

**6.5.** Show that the conclusion \(Q=0\) cannot be obtained by pairing \(T\) with itself: Lemma 4.2 of the third lesson only bounds the negative term by a constant, and that constant need not tend to zero when \(\mu\) has points of positive density.

## 7. Solutions

**6.1.** Integration by parts: \(\int_0^1(-H')\tau^2=[-H\tau^2]_0^1+\int_0^12\tau H(\tau)\,d\tau\). The boundary term vanishes since \(H(1)=0\), and the substitution \(u=\tau^2\) gives \(\int_0^1h(u)\,du\).

**6.2.** \(P(d\beta)=\int_\Sigma d\beta=0\) by Stokes' theorem, since \(\Sigma\) has no boundary. For the ball, \(\mathbf 1_UP(d\beta)=\int_{\Sigma\cap U}d\beta=\int_{\partial(\Sigma\cap U)}\beta\), and the curve \(\Sigma\cap\partial U\) carries a one-form \(\beta\) with nonzero integral. Theorem 1.1 restricts to the set where the density is positive, which for \(P\) is all of \(\Sigma\), so \(\mathbf 1_EP=P\); it says nothing about restrictions to arbitrary sets. (If \(\Sigma\) is not \(J\)-complex, \(P\) is also not of the form \(\int\alpha(\ell)\,d\lambda\).)

**6.3.** \(e^3\wedge e^1\) is a unit form orthogonal to \(\ell=e_1\wedge e_2\), so \(\langle e^3\wedge e^1,m'\rangle=\langle e^3\wedge e^1,m'-\ell\rangle\), which is at most \(|m'-\ell|\) by Cauchy–Schwarz.

**6.4.** Closedness of \(\omega\) is used only at the end, in \(P(\omega)=T(\omega)=0\). Taming is used for \(P(\omega)>0\). Without closedness, the current \(P\) could not see \(\omega\); without taming, \(P(\omega)\) could vanish.

**6.5.** With \(P'=P\), the negative term \(Cr^{-2}\iint(1+d/r)^{-6}\,d\mu\,d\mu\) is bounded by quadratic growth, but at a point of positive density \(r^{-2}\int(1+d/r)^{-6}d\mu\) tends to a positive multiple of \(\theta\). So the expansion only gives \(\|Q\|^2\le C\), the bound of Proposition 6.1 of the third lesson. Removing \(P_E\) from the second factor, which the closedness theorem allows, makes the negative term vanish.

## References

- [OpenAI-TC] OpenAI, *Taming implies compatibility on four-manifolds*, OpenAI Math Release preprint, 6 October 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026
