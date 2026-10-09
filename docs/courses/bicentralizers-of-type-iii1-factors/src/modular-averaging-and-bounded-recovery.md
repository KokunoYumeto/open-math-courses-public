# Modular averaging and bounded recovery

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\varphi\) be a faithful normal state on a von Neumann algebra \(M\), with standard vector \(\xi\) and modular operator \(\Delta\). A vector of \(L^2(M)\) whose spectral measure for \(\log\Delta\) sits near a point \(s\) behaves like an approximate eigenvector, and the elements \(w\in M\) with \(w\xi\) of this kind almost satisfy \(\varphi w=e^sw\varphi\). The difficulty is that such vectors \(w\xi\) need not come from elements \(w\) of bounded norm. This lesson proves the bounded recovery theorem of [OpenAI-recovery]: when the centralizer of \(\varphi\) is trivial, a positive averaged quantity \(\|TU_th\|^2\) on narrow spectral bands, for any bounded operator \(T\), is already witnessed by elements of \(M\) of uniformly bounded norm with spectral support in comparable bands. The proof averages along the modular group, uses random phases to control fourth moments, truncates in the polar decomposition as Haagerup and Musat do [HM], and restores the spectral band with a Fourier filter.

We use the standard form and the results (B3)–(B6) listed in [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons): the natural vector \(\xi\) of \(\varphi\), the modular conjugation \(J\), the Tomita operator \(S=J\Delta^{1/2}\) with \(S(a\xi)=a^*\xi\), the smoothing \(\sigma_f(x)=\int f(t)\sigma_t(x)\,dt\) with \(\sigma_f(x)\xi=\int f(t)\Delta^{it}x\xi\,dt\) for \(f\in L^1(\mathbb R)\), and the characterization of the centralizer \(M_\varphi\). We also use the spectral calculus of a self-adjoint operator, and Fourier inversion for smooth compactly supported functions.

## 1. Notation and two modular estimates

Let \(M\) be a von Neumann algebra with a faithful normal state \(\varphi\), \(H=L^2(M)\) its standard Hilbert space, \(\xi\) the vector of \(\varphi\) in the natural cone, \(\sigma_t=\sigma^\varphi_t\), and
\[
D=\log\Delta,\qquad U_t=e^{itD}=\Delta^{it},\qquad L(a)h=ah,\qquad R(a)h=ha=Ja^*Jh .
\]
\(L\) is a representation and \(R\) an anti-representation of \(M\), and their ranges commute. Inner products are linear in the first variable. For a closed set \(K\subset\mathbb R\), a vector \(h\) has *\(D\)-spectral support in \(K\)* if \(1_K(D)h=h\). We have
\[
U_t(a\xi)=\sigma_t(a)\xi,\qquad e^{D/2}a\xi=\xi a,\qquad\|a^*\xi\|=\|\xi a\| .
\tag{1.1}
\]
Indeed \(a\xi\) lies in the domain of \(S=J\Delta^{1/2}\), so \(\Delta^{1/2}a\xi=JSa\xi=Ja^*\xi=Ja^*J\xi=\xi a\), and \(\|a^*\xi\|=\|Ja^*\xi\|\).

**Lemma 1.1** (spectral localization controls the predual). For \(w\in M\) and \(s\in\mathbb R\),
\[
\|\varphi w-e^sw\varphi\|\le(1+e^{s/2})\,\|(e^{D/2}-e^{s/2})w\xi\| .
\]
If \((w_n)\) is bounded and \(w_n\xi\) has \(D\)-spectral support in \([s-d_n,s+d_n]\) with \(d_n\to0\), then \(\|\varphi w_n-e^sw_n\varphi\|\to0\).

**Proof.** Put \(c=e^{s/2}\) and \(\eta=\xi w-cw\xi=(e^{D/2}-c)w\xi\). Since \(J(\xi w)=w^*\xi\) and \(J(w\xi)=\xi w^*\), we get \(J\eta=w^*\xi-c\,\xi w^*\). For \(y\in M\),
\[
(\varphi w)(y)=\varphi(wy)=\langle y\xi,w^*\xi\rangle=c\langle y\xi,\xi w^*\rangle+\langle y\xi,J\eta\rangle .
\]
Since \(R(w^*)^*=R(w)\) commutes with \(L(y)\), \(\langle y\xi,\xi w^*\rangle=\langle y(\xi w),\xi\rangle=c\,\varphi(yw)+\langle y\eta,\xi\rangle\). Hence \(|\varphi(wy)-c^2\varphi(yw)|\le(1+c)\|\eta\|\,\|y\|\), and \(c^2\varphi(yw)=e^s(w\varphi)(y)\). The last statement follows from \(\|(e^{D/2}-c)w_n\xi\|\le\sup_{|u-s|\le d_n}|e^{u/2}-c|\,\|w_n\xi\|\). \(\square\)

**Lemma 1.2** (smooth spectral localization). Let \(f\in C_c^\infty(\mathbb R)\) and \(g\in L^1(\mathbb R)\) with \(f(u)=\int g(t)e^{itu}\,dt\). For \(y\in M\), \(y_f=\int g(t)\sigma_t(y)\,dt\) lies in \(M\), \(\|y_f\|\le\|g\|_1\|y\|\), and \(y_f\xi=f(D)y\xi\). If \(a\in M\) and \(a\xi\) has compact \(D\)-spectral support, there is \(a^\flat\in M\) with \(a\xi=\xi a^\flat\).

**Proof.** The first statements are (B6) and the spectral theorem: \(\int g(t)U_t\,dt=f(D)\). If \(a\xi\) has spectral support in the compact set \(K\), choose \(f\in C_c^\infty(\mathbb R)\) equal to \(e^{-u/2}\) on a neighbourhood of \(K\); its inverse Fourier transform is integrable. Put \(a^\flat=a_f\). Then, by (1.1), \(\xi a^\flat=e^{D/2}a^\flat\xi=e^{D/2}f(D)a\xi=a\xi\), since \(e^{u/2}f(u)=1\) on \(K\). \(\square\)

The same construction works for any \(u\)-continuous action \(b\) of \(\mathbb R\) by \(\varphi\)-preserving automorphisms, with the unitary group \(V_s(a\xi)=b_s(a)\xi\) in place of \(U\): for \(g\in L^1\), \(\int g(s)b_s(y)\,ds\) is the element of \(M=(M_*)^*\) given by \(\rho\mapsto\int g(s)\rho(b_s(y))\,ds\), and its vector is \(\int g(s)V_sy\xi\,ds\).

## 2. Ergodic averages

**Lemma 2.1** (mean ergodic theorem). Let \((W_t)\) be a strongly continuous unitary group on a Hilbert space, \(P\) the projection onto its fixed vectors, and \(\mu_k\) the uniform probability measure on \([-k,k]\). Then \(\int W_t\eta\,d\mu_k(t)\to P\eta\) for every \(\eta\).

**Proof.** If \(\eta\) is orthogonal to every \(W_u\zeta-\zeta\), then \(W_{-u}\eta=\eta\) for all \(u\); so the fixed space \(F\) and the closed span of the vectors \(W_u\zeta-\zeta\) are orthogonal complements. On \(F\) the averages are the identity. For \(\eta=W_u\zeta-\zeta\), the average is the difference of the averages of \(W_t\zeta\) over \([-k+u,k+u]\) and \([-k,k]\), of norm at most \(|u|\|\zeta\|/k\). The averages are contractions, so they tend to \(0\) on the closed span. \(\square\)

From now on we assume that \(\varphi\) is *ergodic*: \(M_\varphi=\mathbb C1\).

**Lemma 2.2.** For \(y\in M\) and \(\psi\in M_*\),
\[
\int\sigma_t(y)\xi\,d\mu_k(t)\to\varphi(y)\xi\ \text{ in }H,\qquad\int\psi\circ\sigma_{-t}\,d\mu_k(t)\to\psi(1)\varphi\ \text{ in }M_* .
\]

**Proof.** Put \(Y_k=\int\sigma_t(y)\,d\mu_k(t)\in M\); then \(\|Y_k\|\le\|y\|\), and \(Y_k\xi\) converges in norm by Lemma 2.1. For fixed \(u\), \(\|\sigma_u(Y_k)-Y_k\|\le|u|\,\|y\|/k\). If \(Y\) is a \(\sigma\)-weak cluster point of \((Y_k)\), then \(\sigma_u(Y)=Y\) for all \(u\), so \(Y\in M_\varphi\), and \(Y=\varphi(Y)1=\varphi(y)1\), since \(\varphi(Y_k)=\varphi(y)\). The norm limit of \(Y_k\xi\) is the weak limit along the corresponding subnet, \(\varphi(y)\xi\).

For the second statement, \(t\mapsto\psi\circ\sigma_{-t}\) is norm continuous: for \(\psi=\langle\,\cdot\,\eta,\eta\rangle\), \(\psi\circ\sigma_{-t}=\langle\,\cdot\,U_t\eta,U_t\eta\rangle\), and every normal functional is a combination of such. So the averages are Bochner integrals and contractions of \(M_*\). Let \(\mathcal N\) be the closed span of the functionals \(\rho\circ\sigma_u-\rho\). An element \(x\in M\) annihilating \(\mathcal N\) satisfies \(\rho(\sigma_u(x))=\rho(x)\) for all \(\rho,u\), so \(x\in M_\varphi=\mathbb C1\). By the Hahn–Banach theorem, \(\mathcal N=\{\psi:\psi(1)=0\}\). On each \(\rho\circ\sigma_u-\rho\) the averages have norm at most \(|u|\|\rho\|/k\), so they tend to \(0\) on \(\mathcal N\); they fix \(\varphi\). Apply this to \(\psi-\psi(1)\varphi\). \(\square\)

Fix a free ultrafilter \(\omega\) on \(\mathbb N\). For a bounded continuous function \(f\) on \(\mathbb R\) put
\[
m_tf(t)=\lim_{k\to\omega}\int f\,d\mu_k .
\]
This is a positive normalized linear functional, invariant under translations (the averages of \(f(\cdot+u)\) and \(f\) differ by at most \(|u|\|f\|_\infty/k\)) and under \(t\mapsto-t\). For a bounded continuous \(F\colon\mathbb R\to H\) put \(\|F\|_{\mathrm{av}}=(m_t\|F(t)\|^2)^{1/2}\). By Minkowski's inequality in \(L^2(\mu_k;H)\), \(\|\cdot\|_{\mathrm{av}}\) is a seminorm.

**Lemma 2.3** (operator averaging). For \(S\in B(H)\) let \(P(S)\in B(H)\) be defined by \(\langle P(S)h,k\rangle=m_t\langle U_t^*SU_th,k\rangle\). Then \(P\) is a positive unital contraction, \(P(S)\) commutes with every spectral projection of \(D\), and
\[
P(L(a))=\varphi(a)1\quad(a\in M),\qquad\|t\mapsto SU_th\|_{\mathrm{av}}^2=\langle P(S^*S)h,h\rangle .
\]

**Proof.** The form is bounded by \(\|S\|\|h\|\|k\|\), and positivity and \(P(1)=1\) are clear. Translation invariance of \(m\) gives \(U_u^*P(S)U_u=P(S)\), so \(P(S)\) commutes with the unitary group \(U\) and hence with the spectral projections of \(D\). Since \(U_t^*L(a)U_t=L(\sigma_{-t}(a))\), \(P(L(a))\) is the weak operator limit along \(\omega\) of \(L(Y_k)\), \(Y_k=\int\sigma_{-t}(a)\,d\mu_k(t)\); the \(\sigma\)-weak limit \(Y\) of \(Y_k\) along \(\omega\) is \(\sigma\)-invariant, as in Lemma 2.2, hence \(Y=\varphi(a)1\). The last identity is the definition of \(P(S^*S)\). \(\square\)

## 3. Bounded recovery

**Theorem 3.1** (bounded recovery). Let \(M\) be a von Neumann algebra with a faithful normal state \(\varphi\) such that \(M_\varphi=\mathbb C1\). Let \(T\in B(H)\), \(s\in\mathbb R\), \(\delta_n>0\) with \(\delta_n\to0\), and \(h_n\in H\) unit vectors with \(D\)-spectral support in \([s-\delta_n,s+\delta_n]\). If
\[
\limsup_{n\to\infty}m_t\|TU_th_n\|^2>0,
\]
then there are a subsequence \((n_j)\), elements \(v_j\in M\), and constants \(C_*<\infty\), \(\eta>0\) with
\[
\|v_j\|\le C_*,\qquad\|Tv_j\xi\|\ge\eta,\qquad v_j\xi\ \text{has \(D\)-spectral support in }[s-4\delta_{n_j},s+4\delta_{n_j}] .
\]

**Proof.** *Filters.* Choose \(f_0\in C_c^\infty(\mathbb R)\) with \(0\le f_0\le1\), \(f_0=1\) on \([-1,1]\) and support in \([-2,2]\), and \(g_0\in L^1\) with \(f_0(u)=\int g_0(t)e^{itu}\,dt\). For \(\rho>0\) put \(f_\rho(u)=f_0((u-s)/\rho)\) and \(g_\rho(t)=\rho e^{-ist}g_0(\rho t)\). The substitution \(t\mapsto t/\rho\) gives \(f_\rho(u)=\int g_\rho(t)e^{itu}\,dt\) and \(\|g_\rho\|_1=\|g_0\|_1=:C_1\). By Lemma 1.2, \(\mathcal F_\rho(x)=\int g_\rho(t)\sigma_t(x)\,dt\) satisfies
\[
\mathcal F_\rho(x)\in M,\qquad\|\mathcal F_\rho(x)\|\le C_1\|x\|,\qquad\mathcal F_\rho(x)\xi=f_\rho(D)x\xi ,
\]
and \(\mathcal F_\rho(x)\xi\) has spectral support in \([s-2\rho,s+2\rho]\).

*Bounded representatives.* Passing to a subsequence, there is \(\gamma>0\) with \(m_t\|TU_th_n\|^2\ge4\gamma\) for all \(n\). Choose \(x_n\in M\) with \(x_n\xi\) close to \(h_n\). Since \(f_{\delta_n}(D)\) is a contraction fixing \(h_n\), the vectors \(\mathcal F_{\delta_n}(x_n)\xi=f_{\delta_n}(D)x_n\xi\) are at least as close to \(h_n\). Normalizing, we obtain \(y_n\in M\) with \(\|y_n\xi\|=1\), \(\|y_n\xi-h_n\|\to0\), and spectral support in \([s-d_n,s+d_n]\), \(d_n=2\delta_n\). Since \(\big|\|t\mapsto TU_ty_n\xi\|_{\mathrm{av}}-\|t\mapsto TU_th_n\|_{\mathrm{av}}\big|\le\|T\|\|y_n\xi-h_n\|\), we may assume \(m_t\|TU_ty_n\xi\|^2\ge2\gamma\) and \(d_n\le1\) for all \(n\). By (1.1),
\[
\varphi(y_n^*y_n)=1,\qquad\varphi(y_ny_n^*)=\|e^{D/2}y_n\xi\|^2\le e^{s+1}.
\]
No bound on \(\|y_n\|\) is available.

*Averaging with \(n\) fixed.* Fix \(n\), write \(y=y_n\) and \(z_t=\sigma_t(y)\), and put
\[
A_k=\int z_t^*z_t\,d\mu_k(t),\qquad B_k=\int z_tz_t^*\,d\mu_k(t),\qquad\psi(x)=\varphi(y^*xy),\qquad\psi_k=\int\psi\circ\sigma_{-t}\,d\mu_k(t).
\]
Then \(\psi\) is a normal state and \(\psi_k(x)=\int\varphi(z_t^*xz_t)\,d\mu_k(t)\), since \(\varphi\circ\sigma_t=\varphi\). By Lemma 2.2, \(A_k\xi\to\xi\) and \(\|\psi_k-\varphi\|\to0\); so \(\varphi(A_k^2)=\|A_k\xi\|^2\to1\). Also \(\|B_k\|\le\|y\|^2\) and \(\varphi(B_k)=\varphi(yy^*)\le e^{s+1}\), so \(\psi_k(B_k)\le\varphi(B_k)+\|\psi_k-\varphi\|\|y\|^2\). For all large \(k\),
\[
\varphi(A_k^2)+\psi_k(B_k)\le3+e^{s+1}.
\]
Since \(m_t\|Tz_t\xi\|^2=m_t\|TU_ty\xi\|^2\ge2\gamma\), the set of \(k\) with \(\int\|Tz_t\xi\|^2\,d\mu_k>\tfrac32\gamma\) belongs to \(\omega\), hence contains arbitrarily large \(k\). Fix one such \(k\) satisfying the moment bound.

*Discretization.* The map \(t\mapsto z_t\) is bounded and \(*\)-strongly continuous, so \(t\mapsto\|Tz_t\xi\|^2\) and \((t,u)\mapsto\varphi(z_t^*z_tz_u^*z_u)\), \((t,u)\mapsto\varphi(z_t^*z_uz_u^*z_t)\) are continuous. Their integrals over \([-k,k]\), resp. \([-k,k]^2\), against \(\mu_k\), resp. \(\mu_k\otimes\mu_k\), are \(\int\|Tz_t\xi\|^2d\mu_k\), \(\varphi(A_k^2)\) and \(\psi_k(B_k)\). Riemann sums for a fine partition of \([-k,k]\) give times \(t_i\) and weights \(p_i\ge0\), \(\sum_ip_i=1\), such that with \(z_i=\sigma_{t_i}(y)\), \(A=\sum_ip_iz_i^*z_i\) and \(B=\sum_ip_iz_iz_i^*\),
\[
\sum_ip_i\|Tz_i\xi\|^2\ge\gamma,\qquad\varphi(A^2)+\sum_ip_i\varphi(z_i^*Bz_i)\le C:=4+e^{s+1}.
\]
The constants \(\gamma\) and \(C\) do not depend on \(n\).

*Random phases.* Let \(\epsilon_i\) be independent random variables, uniformly distributed on the unit circle, and \(z=\sum_i\sqrt{p_i}\,\epsilon_iz_i\). Each \(z_i\xi=U_{t_i}y\xi\) has spectral support in \([s-d_n,s+d_n]\), hence so does \(z\xi\). Since \(\mathbb E(\epsilon_i\overline{\epsilon_j})=\delta_{ij}\),
\[
\mathbb E\|Tz\xi\|^2=\sum_ip_i\|Tz_i\xi\|^2\ge\gamma .
\]
Expanding \((z^*z)^2=\sum_{i,j,k,l}\sqrt{p_ip_jp_kp_l}\,\overline{\epsilon_i}\epsilon_j\overline{\epsilon_k}\epsilon_l\,z_i^*z_jz_k^*z_l\), the expectation of the product of phases is \(1\) when \((i,k)\) is a rearrangement of \((j,l)\), that is when \(i=j,k=l\) or \(i=l,k=j\), and \(0\) otherwise; the two cases overlap exactly when all four indices agree. Hence
\[
\mathbb E(z^*z)^2=A^2+\sum_ip_iz_i^*Bz_i-\sum_ip_i^2(z_i^*z_i)^2\le A^2+\sum_ip_iz_i^*Bz_i ,
\]
and \(\mathbb E\varphi((z^*z)^2)\le C\).

*Truncation.* For \(K>0\) let \(z=u|z|\) be the polar decomposition and \(z^{[K]}=u\min(|z|,K)\), so \(\|z^{[K]}\|\le K\). Then \(z-z^{[K]}=u(|z|-K)_+\), and since \((r-K)_+^2\le r^4/K^2\) for \(r\ge0\),
\[
\mathbb E\|(z-z^{[K]})\xi\|^2=\mathbb E\varphi((|z|-K)_+^2)\le K^{-2}\mathbb E\varphi(|z|^4)\le CK^{-2}.
\]

*Restoring the band.* Put \(v=\mathcal F_{d_n}(z^{[K]})\). Then \(\|v\|\le C_1K\), \(v\xi=f_{d_n}(D)z^{[K]}\xi\) has spectral support in \([s-2d_n,s+2d_n]\), and since \(f_{d_n}(D)\) fixes \(z\xi\) and is a contraction, \(\|v\xi-z\xi\|\le\|(z^{[K]}-z)\xi\|\). By Minkowski's inequality for square-integrable random vectors,
\[
\big(\mathbb E\|Tv\xi\|^2\big)^{1/2}\ge\big(\mathbb E\|Tz\xi\|^2\big)^{1/2}-\|T\|\big(\mathbb E\|(v-z)\xi\|^2\big)^{1/2}\ge\sqrt\gamma-\|T\|\sqrt C/K .
\]
The hypothesis forces \(T\ne0\). Fix \(K=2\|T\|\sqrt{C/\gamma}\), independent of \(n\); then \(\mathbb E\|Tv\xi\|^2\ge\gamma/4\).

*Selection.* \(z\) depends continuously, in norm, on the phases \((\epsilon_i)\) in the compact torus, and \(z^{[K]}=z\,q_K(z^*z)\) with \(q_K(r)=\min(1,K/\sqrt r)\), \(q_K(0)=1\), continuous on \([0,\infty)\); so \(z^{[K]}\), and then \(\|Tv\xi\|^2\), depend continuously on the phases. Choose phases where \(\|Tv\xi\|^2\) attains its maximum, which is at least its expectation, and call the resulting element \(v_n\). Then \(\|v_n\|\le C_1K\), \(\|Tv_n\xi\|\ge\sqrt\gamma/2\), and \(v_n\xi\) has spectral support in \([s-2d_n,s+2d_n]=[s-4\delta_n,s+4\delta_n]\). This proves the theorem with \(C_*=C_1K\) and \(\eta=\sqrt\gamma/2\). \(\square\)

The averaging time \(k\) and the finite family \((z_i)\) depend on \(n\), but the moment constant \(C\), the cutoff \(K\) and the filter norm \(C_1\) do not; this is what makes the output uniformly bounded.

## 4. Exercises

**Exercise 4.1.** Let \(M=M_2(\mathbb C)\) and \(\varphi=\operatorname{Tr}(\rho\,\cdot\,)\) with \(\rho=\operatorname{diag}(\lambda/(1+\lambda),1/(1+\lambda))\). Compute \(\varphi w-e^sw\varphi\) for \(w=e_{12}\), and find the \(s\) for which it vanishes. Compare with Lemma 1.1.

**Exercise 4.2.** Show that if \(M_\varphi=\mathbb C1\), then the fixed vectors of \(U\) are the multiples of \(\xi\). (Use Lemma 2.2.)

**Exercise 4.3.** Verify the identity \(\mathbb E(z^*z)^2=A^2+\sum_ip_iz_i^*Bz_i-\sum_ip_i^2(z_i^*z_i)^2\) for two indices by direct expansion.

**Exercise 4.4.** Show that \((r-K)_+^2\le r^4/K^2\) for all \(r\ge0\) and \(K>0\).

## 5. Solutions

**4.1.** \((\varphi w)(y)=\operatorname{Tr}(\rho e_{12}y)\) and \((w\varphi)(y)=\operatorname{Tr}(\rho ye_{12})=\operatorname{Tr}(e_{12}\rho y)\). Since \(\rho e_{12}=\rho_1e_{12}\) and \(e_{12}\rho=\rho_2e_{12}\), \(\varphi w-e^sw\varphi=(\rho_1-e^s\rho_2)\operatorname{Tr}(e_{12}\,\cdot\,)\), which vanishes exactly when \(e^s=\rho_1/\rho_2=\lambda\). Correspondingly, \(e_{12}\xi\) is an eigenvector of \(\Delta\) with eigenvalue \(\rho_1/\rho_2=\lambda\), so its \(D\)-spectral support is \(\{\log\lambda\}\).

**4.2.** If \(U_t\eta=\eta\) for all \(t\), approximate \(\eta\) by \(y\xi\), \(y\in M\). By Lemma 2.1 and Lemma 2.2, \(\eta=P\eta\) is the limit of \(Py\xi=\lim_k\int\sigma_t(y)\xi\,d\mu_k=\varphi(y)\xi\), a multiple of \(\xi\).

**4.3.** With \(z=a\epsilon_1z_1+b\epsilon_2z_2\), \(a=\sqrt{p_1}\), \(b=\sqrt{p_2}\), the terms of \((z^*z)^2\) surviving the expectation are \(a^4(z_1^*z_1)^2+b^4(z_2^*z_2)^2+a^2b^2(z_1^*z_1z_2^*z_2+z_2^*z_2z_1^*z_1+z_1^*z_2z_2^*z_1+z_2^*z_1z_1^*z_2)\). The right side equals \(A^2=p_1^2(z_1^*z_1)^2+p_2^2(z_2^*z_2)^2+p_1p_2(z_1^*z_1z_2^*z_2+z_2^*z_2z_1^*z_1)\), plus \(\sum_ip_iz_i^*Bz_i=p_1^2(z_1^*z_1)^2+p_1p_2z_1^*z_2z_2^*z_1+p_2p_1z_2^*z_1z_1^*z_2+p_2^2(z_2^*z_2)^2\), minus \(p_1^2(z_1^*z_1)^2+p_2^2(z_2^*z_2)^2\). They agree.

**4.4.** If \(r\le K\), the left side is \(0\). If \(r>K\), then \((r-K)^2\le r^2\le r^4/K^2\).

## References

- [OpenAI-recovery] OpenAI, Bounded recovery for modular spectral averages, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026
- [HM] U. Haagerup, M. Musat, On the best constants in noncommutative Khintchine-type inequalities, preprint. https://arxiv.org/abs/math/0611160
