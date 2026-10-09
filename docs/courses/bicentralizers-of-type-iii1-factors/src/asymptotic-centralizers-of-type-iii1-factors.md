# Asymptotic centralizers of type III₁ factors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\varphi\) be a faithful normal state on a von Neumann algebra \(M\). Bounded sequences that commute with \(\varphi\) ever more closely form, modulo the sequences tending to zero, a finite von Neumann algebra \(M_{\varphi,\omega}\). For a type III₁ factor \(M\) the centralizer \(M_\varphi\) itself can be trivial, but \(M_{\varphi,\omega}\) is always large: this lesson proves that it is a II₁ factor. Ando and Haagerup proved that the whole centralizer of the ultrapower state in the Ocneanu ultrapower is a II₁ factor [Ando–Haagerup]; \(M_{\varphi,\omega}\) lies in that centralizer, and the argument below proves its factoriality directly with sequences. The tool is the Connes–Størmer transitivity theorem, which says that in a type III₁ factor any normal state can be moved arbitrarily close to any other by a unitary. The same tool gives unitaries in the ultrapower that conjugate one ultrapower state exactly onto another, and partial isometries that scale the ultrapower state by a prescribed factor. These are the inputs for the bicentralizer and its flow in the next two lessons.

We use the conventions of Section 1, Lemmas 1.1, 1.3 and 1.4, Theorem 5.1, and the results (B3), (B6) and (B8) listed under "Results used from other lessons" in [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#5-sequences-asymptotically-commuting-with-a-state); the Ocneanu ultrapower \(M^\omega\) and its state \(\varphi^\omega\) from Sections 1–4 of [Multiplier ultraproducts and normal embeddings](course:OA-APPROX/multiplier-ultraproducts-and-normal-embeddings#3-completeness-on-two-cyclic-vectors); and the Connes–Størmer transitivity theorem in the form (HC1) of [Approximate unitary homogeneity of normal states](course:OA-FLOW/OA-FLOW-HC#equation-hc1).

## 1. Sequences in the ultrapower

Throughout, \(M\) is a countably decomposable von Neumann algebra, \(\varphi\) a faithful normal state on \(M\), \(\xi\) its vector in the standard form, and \(\omega\) a free ultrafilter on \(\mathbb N\). For \(x\in M\) and \(\psi\in M_*\) we use the bimodule notation
\[
(x\psi)(y)=\psi(yx),\qquad(\psi x)(y)=\psi(xy),\qquad[x,\psi]=x\psi-\psi x,
\]
so that \((a\psi a^*)(y)=\psi(a^*ya)\). For a unitary \(u\), \(u\psi u^*-\psi=[u,\psi]u^*\), hence
\[
\|u\psi u^*-\psi\|=\|[u,\psi]\| .
\tag{1.1}
\]
We write \(\|x\|_\varphi=\varphi(x^*x)^{1/2}\) and \(\|x\|_\varphi^\sharp=(\|x\|_\varphi^2+\|x^*\|_\varphi^2)^{1/2}\). By Lemma 1.3 of the ultraproduct lesson, a bounded sequence tends to \(0\) \(*\)-strongly along \(\omega\) exactly when \(\lim_\omega\|x_n\|^\sharp_\varphi=0\), and the same holds with any other faithful normal state in place of \(\varphi\).

Let \(I_\omega\) be the set of bounded sequences tending to \(0\) \(*\)-strongly along \(\omega\), \(N_\omega\) its multiplier algebra (the bounded sequences \(a\) with \(aI_\omega\cup I_\omega a\subset I_\omega\)), and \(M^\omega=N_\omega/I_\omega\) the Ocneanu ultrapower. It is a von Neumann algebra, the ultrapower state \(\varphi^\omega([x_n])=\lim_\omega\varphi(x_n)\) is faithful and normal, and the constant sequences give a normal copy of \(M\) in \(M^\omega\), with which we identify \(M\). The algebras \(I_\omega\), \(N_\omega\), \(M^\omega\) do not depend on \(\varphi\); for every faithful normal state \(\psi\) the formula \(\psi^\omega([x_n])=\lim_\omega\psi(x_n)\) defines a faithful normal state of \(M^\omega\). Let
\[
A_{\varphi,\omega}=\{(x_n)\in\ell^\infty(M):\ \lim_{n\to\omega}\|[x_n,\varphi]\|=0\},\qquad M_{\varphi,\omega}=A_{\varphi,\omega}/I_\omega .
\]
By Theorem 5.1 of the ultraproduct lesson, \(A_{\varphi,\omega}\) is a norm-closed \(*\)-algebra containing \(I_\omega\) as a two-sided ideal, and \(M_{\varphi,\omega}\) is a finite von Neumann algebra with faithful normal tracial state \(\tau_{\varphi,\omega}([x_n])=\lim_\omega\varphi(x_n)\).

**Lemma 1.1.**

1. \(A_{\varphi,\omega}\subset N_\omega\), and the inclusion induces an injective unital \(*\)-homomorphism \(M_{\varphi,\omega}\to M^\omega\) with \(\varphi^\omega=\tau_{\varphi,\omega}\) on \(M_{\varphi,\omega}\). We identify \(M_{\varphi,\omega}\) with its image: the elements of \(M^\omega\) with a representative in \(A_{\varphi,\omega}\).
2. Every \(X\in M_{\varphi,\omega}\) satisfies \(X\varphi^\omega=\varphi^\omega X\).
3. If \((x_n)\in A_{\varphi,\omega}\) is self-adjoint, \(\|x_n\|\le C\), and \(f\) is continuous on \([-C,C]\), then \((f(x_n))\in A_{\varphi,\omega}\), and it represents \(f(X)\), where \(X=[x_n]\).
4. Every projection of \(M_{\varphi,\omega}\) has a representative \((p_n)\in A_{\varphi,\omega}\) consisting of projections.

**Proof.** (1) If \(X\in A_{\varphi,\omega}\) and \(Z\in I_\omega\), then \(XZ,ZX\in I_\omega\), because \(I_\omega\) is an ideal of \(A_{\varphi,\omega}\); this is the definition of \(X\in N_\omega\). The kernel of \(A_{\varphi,\omega}\to M^\omega\) is \(A_{\varphi,\omega}\cap I_\omega=I_\omega\), and both states are the limit of \(\varphi(x_n)\).

(2) For \(Y=[y_n]\in M^\omega\), \((X\varphi^\omega-\varphi^\omega X)(Y)=\lim_\omega[x_n,\varphi](y_n)\), and \(|[x_n,\varphi](y_n)|\le\|[x_n,\varphi]\|\,\|y_n\|\to_\omega0\).

(3) For a polynomial \(p\), \((p(x_n))\in A_{\varphi,\omega}\) by the power bound of Lemma 1.1(d) of the ultraproduct lesson, and it represents \(p(X)\) because the quotient map is a \(*\)-homomorphism. Choose polynomials \(p_j\to f\) uniformly on \([-C,C]\). Then \(\|[f(x_n),\varphi]\|\le\|[p_j(x_n),\varphi]\|+2\|f-p_j\|_\infty\), so \(\lim_\omega\|[f(x_n),\varphi]\|\le2\|f-p_j\|_\infty\) for every \(j\), and \((f(x_n))\in A_{\varphi,\omega}\). Its class \(Y\) satisfies \(\|Y-p_j(X)\|\le\sup_n\|f(x_n)-p_j(x_n)\|\le\|f-p_j\|_\infty\), and \(\|f(X)-p_j(X)\|\le\|f-p_j\|_\infty\) since \(\operatorname{Sp}X\subset[-C,C]\). Hence \(Y=f(X)\).

(4) Let \(P\) be a projection with representative \((y_n)\). The self-adjoint parts \((y_n+y_n^*)/2\) also represent \(P\); applying (3) with \(g(t)=\min(\max(t,0),1)\) gives a representative \((x_n)\) with \(0\le x_n\le1\), since \(g(P)=P\). Let \(p_n=1_{[1/2,1]}(x_n)\). On \([0,1]\), \(|t-1_{[1/2,1]}(t)|\le2(t-t^2)\): for \(t<\tfrac12\) the left side is \(t\le2t(1-t)\), and for \(t\ge\tfrac12\) it is \(1-t\le2t(1-t)\). By functional calculus \((x_n-p_n)^2\le4(x_n-x_n^2)^2\), so \(\|x_n-p_n\|_\varphi\le2\|x_n-x_n^2\|_\varphi\). The class of \((x_n-x_n^2)\) is \(P-P^2=0\), so \(\|x_n-x_n^2\|_\varphi\to_\omega0\). As \(x_n-p_n\) is self-adjoint, \(x_n-p_n\to0\) \(*\)-strongly along \(\omega\). By Theorem 5.1(2) of the ultraproduct lesson, \((p_n)\in A_{\varphi,\omega}\), and it represents \(P\). \(\square\)

**Lemma 1.2** (asymptotic eigenoperators). Let \(\lambda>0\) and let \((v_n)\) be a bounded sequence with \(\lim_\omega\|v_n\varphi-\lambda\varphi v_n\|=0\). Then \((v_n)\in N_\omega\), and \(V=[v_n]\in M^\omega\) satisfies \(V\varphi^\omega=\lambda\varphi^\omega V\).

**Proof.** Let \(\|v_n\|\le C\), \(\delta_n=\|v_n\varphi-\lambda\varphi v_n\|\), and \(z\in I_\omega\) with \(\|z_n\|\le K\). We show that the four quantities \(\|v_nz_n\|_\varphi\), \(\|(v_nz_n)^*\|_\varphi\), \(\|z_nv_n\|_\varphi\), \(\|(z_nv_n)^*\|_\varphi\) tend to \(0\) along \(\omega\). The first is at most \(C\|z_n\|_\varphi\) and the last at most \(C\|z_n^*\|_\varphi\). For the second, put \(a_n=z_nz_n^*\). Since \(\varphi v_n=\lambda^{-1}v_n\varphi-\lambda^{-1}(v_n\varphi-\lambda\varphi v_n)\),
\[
\varphi(v_na_nv_n^*)=(\varphi v_n)(a_nv_n^*)=\lambda^{-1}\varphi(a_nv_n^*v_n)+R_n,\qquad|R_n|\le\lambda^{-1}\delta_nK^2C,
\]
and \(|\varphi(a_nv_n^*v_n)|=|\langle v_n^*v_n\xi,a_n\xi\rangle|\le C^2\|a_n\xi\|\le C^2K\|z_n^*\|_\varphi\). For the third, put \(b_n=z_n^*z_n\); then
\[
\varphi(v_n^*b_nv_n)=(v_n\varphi)(v_n^*b_n)=\lambda\varphi(v_nv_n^*b_n)+R_n',\qquad|R_n'|\le\delta_nCK^2,
\]
and \(|\varphi(v_nv_n^*b_n)|\le C^2\|b_n\xi\|\le C^2K\|z_n\|_\varphi\). All four quantities tend to \(0\), so \(vz,zv\in I_\omega\) and \(v\in N_\omega\). Finally, for \(Y=[y_n]\in M^\omega\),
\[
(V\varphi^\omega-\lambda\varphi^\omega V)(Y)=\lim_\omega(v_n\varphi-\lambda\varphi v_n)(y_n)=0 .\qquad\square
\]

**Lemma 1.3** (unitaries conjugating states). Let \(\psi\) be a faithful normal state on \(M\) and \((u_n)\) unitaries with \(\lim_\omega\|u_n\varphi u_n^*-\psi\|=0\). Then \((u_n)\in N_\omega\), and \(U=[u_n]\) is a unitary of \(M^\omega\) with \(U\varphi^\omega U^*=\psi^\omega\).

**Proof.** Let \(z\in I_\omega\), \(\|z_n\|\le K\). First, \(\|u_nz_n\|_\varphi=\|z_n\|_\varphi\) and \(\|(z_nu_n)^*\|_\varphi=\|z_n^*\|_\varphi\) tend to \(0\). Next,
\[
\|z_nu_n\|_\varphi^2=(u_n\varphi u_n^*)(z_n^*z_n)\le\psi(z_n^*z_n)+K^2\|u_n\varphi u_n^*-\psi\|,
\]
and \(\psi(z_n^*z_n)\to_\omega0\) because \(z_n\to0\) strongly along \(\omega\) and \(\psi\) is normal. Finally, put \(b_n=z_n^*u_n^*\). With \((u^*\psi u)(y)=\psi(uyu^*)\),
\[
\psi(b_n^*b_n)=(u_n^*\psi u_n)(z_nz_n^*)\le\varphi(z_nz_n^*)+K^2\|u_n^*\psi u_n-\varphi\|,
\]
and \(\|u_n^*\psi u_n-\varphi\|=\|\psi-u_n\varphi u_n^*\|\). So \(\psi(b_n^*b_n)\to_\omega0\); since \(\psi\) is faithful, \(b_n\to0\) strongly along \(\omega\) by Lemma 1.3 of the ultraproduct lesson, and \(\|(u_nz_n)^*\|_\varphi^2=\varphi(b_n^*b_n)\to_\omega0\). Hence \(uz,zu\in I_\omega\), \(u\in N_\omega\), and \(U\) is unitary. For \(Y=[y_n]\),
\[
(U\varphi^\omega U^*)(Y)=\lim_\omega\varphi(u_n^*y_nu_n)=\lim_\omega(u_n\varphi u_n^*)(y_n)=\lim_\omega\psi(y_n)=\psi^\omega(Y).\qquad\square
\]

## 2. Approximate conjugacy in type III1 factors

From now on \(M\) is a factor of type III₁ with separable predual. By definition it is a factor of type III, so by (B8) every nonzero projection \(e\in M\) is equivalent to \(1\), and \(eMe\cong M\). In particular \(eMe\) is again a type III₁ factor with separable predual.

**Lemma 2.1** (approximately central projections). Let \(\psi\) be a faithful normal state on \(M\), \(\lambda\in[0,1]\) and \(\varepsilon>0\). There is a projection \(e\in M\) with \(\|[e,\psi]\|<\varepsilon\) and \(|\psi(e)-\lambda|<\varepsilon\).

**Proof.** For \(\lambda\in\{0,1\}\) take \(e=\lambda1\). Otherwise choose a projection \(e_0\ne0,1\), and isometries \(w_1,w_2\) with \(w_1w_1^*=e_0\), \(w_2w_2^*=1-e_0\). The normal state
\[
\theta(x)=\lambda\psi(w_1^*xw_1)+(1-\lambda)\psi(w_2^*xw_2)
\]
satisfies \(\theta(ye_0)=\lambda\psi(w_1^*yw_1)=\theta(e_0y)\) for all \(y\), since \(e_0w_1=w_1\), \(e_0w_2=0\), \(w_1^*e_0=w_1^*\), \(w_2^*e_0=0\). So \([e_0,\theta]=0\) and \(\theta(e_0)=\lambda\). By (HC1) there is a unitary \(u\) with \(\|u\theta u^*-\psi\|<\varepsilon/2\). Put \(e=ue_0u^*\). Then \([e,u\theta u^*]=u[e_0,\theta]u^*=0\), so
\[
\|[e,\psi]\|=\|[e,\psi-u\theta u^*]\|\le2\|\psi-u\theta u^*\|<\varepsilon,
\]
and \(|\psi(e)-\lambda|=|\psi(e)-(u\theta u^*)(e)|<\varepsilon/2\). \(\square\)

**Lemma 2.2** (partial isometries between states). Let \(p,q\in M\) be nonzero projections, \(\chi_1,\chi_2\) normal states with \(\chi_1(p)=\chi_2(q)=1\), and \(0<\varepsilon<1\). There is a partial isometry \(v\in M\) with \(v^*v\le p\), \(vv^*\le q\),
\[
\chi_1(p-v^*v)\le\varepsilon,\qquad\chi_2(q-vv^*)\le\varepsilon,\qquad\|v\chi_1v^*-\chi_2\|\le5\sqrt\varepsilon,\qquad\|v\chi_1-\chi_2v\|\le6\sqrt\varepsilon .
\]

**Proof.** By (B3), \(\chi_1=\langle\,\cdot\,\eta,\eta\rangle\) for a unit vector \(\eta\) in the standard form; \(\|(1-p)\eta\|^2=\chi_1(1-p)=0\), so \(\eta=p\eta\). By (HC1) choose a unitary \(u\) with \(\|u\chi_1u^*-\chi_2\|\le\varepsilon\). Let \(y=qup\) and \(y=v|y|\) its polar decomposition. Since \(y=yp\) and \(y=qy\), \(v^*v\) (the support of \(|y|\)) lies under \(p\) and \(vv^*\) under \(q\). As \(\|y\|\le1\), \(|y|^2\le v^*v\) and \(|y^*|^2\le vv^*\). Hence
\[
\chi_1(p-v^*v)\le\chi_1(p-pu^*qup)=1-(u\chi_1u^*)(q)\le1-\chi_2(q)+\varepsilon=\varepsilon,
\]
\[
\chi_2(q-vv^*)\le\chi_2(q-qupu^*q)=1-\chi_2(upu^*)\le1-(u\chi_1u^*)(upu^*)+\varepsilon=1-\chi_1(p)+\varepsilon=\varepsilon .
\]
Next, \(v\chi_1v^*\) and \(u\chi_1u^*\) are the vector functionals of \(v\eta\) and \(u\eta\), and for vectors \(\zeta,\zeta'\), \(\|\langle\,\cdot\,\zeta,\zeta\rangle-\langle\,\cdot\,\zeta',\zeta'\rangle\|\le\|\zeta-\zeta'\|(\|\zeta\|+\|\zeta'\|)\). Since \(u\eta=up\eta=v|y|\eta+(1-q)u\eta\) and \(v\eta=vp\eta\),
\[
v\eta-u\eta=v(p-|y|)\eta-(1-q)u\eta .
\]
The element \(T=|y|\) of \(pMp\) satisfies \(0\le T\le p\), so \((p-T)^2=p-2T+T^2\le p-T^2\) and \(\|(p-T)\eta\|^2\le\chi_1(p-|y|^2)\le\varepsilon\). Also \(\|(1-q)u\eta\|^2=(u\chi_1u^*)(1-q)\le\chi_2(1-q)+\varepsilon=\varepsilon\). So \(\|v\eta-u\eta\|\le2\sqrt\varepsilon\), \(\|v\chi_1v^*-u\chi_1u^*\|\le4\sqrt\varepsilon\), and \(\|v\chi_1v^*-\chi_2\|\le4\sqrt\varepsilon+\varepsilon\le5\sqrt\varepsilon\). Finally, for \(x\in M\),
\[
(v\chi_1)(x)-((v\chi_1v^*)v)(x)=\chi_1(xv)-\chi_1(v^*vxv)=\langle xv\eta,(p-v^*v)\eta\rangle,
\]
whose absolute value is at most \(\|x\|\chi_1(p-v^*v)^{1/2}\le\|x\|\sqrt\varepsilon\). With \(\|(v\chi_1v^*-\chi_2)v\|\le5\sqrt\varepsilon\) this gives \(\|v\chi_1-\chi_2v\|\le6\sqrt\varepsilon\). \(\square\)

**Lemma 2.3** (cutting down to a corner). Let \(f\in M\) be a nonzero projection, \(N=fMf\), and \(\psi=\varphi|_N/\varphi(f)\), a faithful normal state of \(N\).

1. For every projection \(q\le f\), \(\|[q,\varphi]\|\le\varphi(f)\,\|[q,\psi]\|_{N_*}+2\|[f,\varphi]\|\).
2. For \(0\le\lambda\le\varphi(f)\) and \(\varepsilon>0\) there is a projection \(q\le f\) with \(\|[q,\varphi]\|<\varepsilon+2\|[f,\varphi]\|\) and \(|\varphi(q)-\lambda|<\varepsilon\).

**Proof.** (1) Since \(q=qf=fq\), writing \(\varphi=f\varphi f+f\varphi(1-f)+(1-f)\varphi f+(1-f)\varphi(1-f)\) gives
\[
[q,\varphi]=[q,f\varphi f]+qf\varphi(1-f)-(1-f)\varphi fq .
\]
Here \(f\varphi(1-f)=f[f,\varphi]\) and \((1-f)\varphi f=-[f,\varphi]f\), so the last two terms have norm at most \(\|[f,\varphi]\|\) each. For \(x\in M\), \([q,f\varphi f](x)=\varphi(fxfq)-\varphi(qfxf)=\varphi(f)\,[q,\psi](fxf)\), so \(\|[q,f\varphi f]\|\le\varphi(f)\|[q,\psi]\|_{N_*}\).

(2) \(N\) is a type III₁ factor with separable predual. Lemma 2.1 in \(N\), with \(\lambda/\varphi(f)\) and \(\varepsilon/\varphi(f)\), gives a projection \(q\in N\) with \(\|[q,\psi]\|<\varepsilon/\varphi(f)\) and \(|\psi(q)-\lambda/\varphi(f)|<\varepsilon/\varphi(f)\). Part (1) and \(\varphi(q)=\varphi(f)\psi(q)\) finish the proof. \(\square\)

## 3. The asymptotic centralizer is a II1 factor

**Theorem 3.1.** Let \(M\) be a type III₁ factor with separable predual and \(\varphi\) a faithful normal state. For every free ultrafilter \(\omega\), \(M_{\varphi,\omega}\) is a factor of type II₁.

**Proof.** Write \(\tau=\tau_{\varphi,\omega}\). *Factoriality.* Suppose the centre of the finite von Neumann algebra \(M_{\varphi,\omega}\) contains a projection \(P\ne0,1\). Then \(0<\tau(P)<1\), and replacing \(P\) by \(1-P\) we may assume \(s=\tau(P)\le\tfrac12\). By Lemma 1.1(4), \(P\) has a representative of projections \((p_n)\in A_{\varphi,\omega}\); then \(s_n=\varphi(p_n)\to_\omega s\).

Let \(\lambda_n=\min(s_n,1-s_n)\). For the \(n\) with \(s_n<1\), Lemma 2.3(2) with \(f=1-p_n\), \(\lambda=\lambda_n\) and \(\varepsilon=1/n\) gives a projection \(q_n\le1-p_n\) with
\[
\|[q_n,\varphi]\|<1/n+2\|[p_n,\varphi]\|,\qquad|\varphi(q_n)-\lambda_n|<1/n ;
\]
for the other \(n\) put \(q_n=0\). Since \(s\le\tfrac12\), \(\lambda_n\to_\omega s\) and \(\varphi(q_n)\to_\omega s\), so \((q_n)\in A_{\varphi,\omega}\) and \(Q=[q_n]\) satisfies \(\tau(Q)=s>0\) and \(Q\le1-P\).

The set \(B=\{n:s_n>0,\ \varphi(q_n)>0\}\) belongs to \(\omega\). For \(n\in B\) apply Lemma 2.2 to \(p=p_n\), \(q=q_n\), \(\chi_1=p_n\varphi p_n/s_n\), \(\chi_2=q_n\varphi q_n/\varphi(q_n)\) and \(\varepsilon=1/(n+1)\), obtaining a partial isometry \(v_n\); for \(n\notin B\) put \(v_n=0\). For \(n\in B\), since \(v_n=v_np_n=q_nv_n\),
\[
\|v_n\varphi-v_n(p_n\varphi p_n)\|=\|v_np_n\varphi(1-p_n)\|\le\|[p_n,\varphi]\|,\qquad
\|\varphi v_n-(q_n\varphi q_n)v_n\|=\|(1-q_n)\varphi q_nv_n\|\le\|[q_n,\varphi]\|,
\]
and
\[
v_n(p_n\varphi p_n)-(q_n\varphi q_n)v_n=s_n(v_n\chi_1-\chi_2v_n)+(s_n-\varphi(q_n))\chi_2v_n
\]
has norm at most \(6(n+1)^{-1/2}+|s_n-\varphi(q_n)|\). All these bounds tend to \(0\) along \(\omega\), so \((v_n)\in A_{\varphi,\omega}\). Moreover \(p_n-v_n^*v_n\) is a projection in \(p_nMp_n\) with \(\varphi(p_n-v_n^*v_n)=s_n\chi_1(p_n-v_n^*v_n)\le s_n/(n+1)\), so \(p_n-v_n^*v_n\to0\) \(*\)-strongly along \(\omega\); likewise \(q_n-v_nv_n^*\to0\). Hence \(V=[v_n]\in M_{\varphi,\omega}\) satisfies \(V^*V=P\) and \(VV^*=Q\).

Since \(P\) is central, \(Q=V(V^*V)V^*=VPV^*=PVV^*=PQ\). But \(Q\le1-P\) gives \(PQ=P(1-P)Q=0\). So \(Q=0\), contradicting \(\tau(Q)>0\). Hence \(M_{\varphi,\omega}\) is a factor.

*Type.* For \(\lambda\in[0,1]\), Lemma 2.1 with \(\psi=\varphi\) and \(\varepsilon=1/n\) gives projections \(e_n\) with \(\|[e_n,\varphi]\|<1/n\) and \(|\varphi(e_n)-\lambda|<1/n\); their class is a projection of trace \(\lambda\). By (B8) a finite factor is of type I\(_n\) or II₁, and the trace of a projection in \(M_n(\mathbb C)\) is a multiple of \(1/n\). So \(M_{\varphi,\omega}\) is of type II₁. \(\square\)

## 4. Approximate eigenoperators

**Proposition 4.1.** Let \(M\) be a type III₁ factor with separable predual, \(\varphi\) a faithful normal state, \(\lambda>0\), and \(m\) an integer with \(m\ge\max(1,\lambda)\). There are partial isometries \(v_{k,n}\in M\) (\(1\le k\le m\), \(n\ge1\)) such that, as \(n\to\infty\),
\[
\|v_{k,n}\varphi-\lambda\varphi v_{k,n}\|\to0\quad(1\le k\le m),\qquad\sum_{k=1}^mv_{k,n}v_{k,n}^*\to1\ \ *\text{-strongly}.
\]
Consequently, for every free ultrafilter \(\omega\), the classes \(V_k=[v_{k,n}]_n\in M^\omega\) satisfy \(V_k\varphi^\omega=\lambda\varphi^\omega V_k\) and \(\sum_kV_kV_k^*=1\).

**Proof.** *Claim: for every \(\eta>0\) and every integer \(m\ge1\) there are projections \(p_1,\ldots,p_m\) with \(\sum_kp_k=1\), \(\|[p_k,\varphi]\|<\eta\) and \(|\varphi(p_k)-1/m|<\eta\).* This holds for \(m=1\), and for every type III₁ factor with separable predual and faithful normal state. Suppose it holds for \(m-1\). By Lemma 2.1 choose \(p_1\) with \(\|[p_1,\varphi]\|<\eta/3\) and \(|\varphi(p_1)-1/m|<\eta/3\); we may take \(\eta<1/m\), so \(f=1-p_1\ne0\). Apply the claim for \(m-1\) in \(N=fMf\) with \(\psi=\varphi|_N/\varphi(f)\) and tolerance \(\eta/3\), giving \(p_2,\ldots,p_m\) with sum \(f\). By Lemma 2.3(1), \(\|[p_k,\varphi]\|<\eta/3+2\eta/3=\eta\). Also \(\varphi(p_k)=\varphi(f)\psi(p_k)\) with \(|\varphi(f)-(1-1/m)|<\eta/3\) and \(|\psi(p_k)-1/(m-1)|<\eta/3\), so \(|\varphi(p_k)-1/m|<\eta/3+(1-1/m)\eta/3+\eta^2/9<\eta\).

Fix \(n\) and \(\eta=\varepsilon=\min(1,\lambda)/(4mn)\), and take \(p_1,\ldots,p_m\) as in the claim; then \(\varphi(p_k)>3/(4m)\) and \(\varphi(q_k)>3\lambda/(4m)\) below, so all these projections are nonzero. By Lemma 2.1 choose projections \(q_k\) with \(\|[q_k,\varphi]\|<\eta\) and \(|\varphi(q_k)-\lambda/m|<\eta\); note \(\lambda/m\le1\). Lemma 2.2, applied to \(q_k,p_k\), \(\chi_1=q_k\varphi q_k/\varphi(q_k)\), \(\chi_2=p_k\varphi p_k/\varphi(p_k)\), gives partial isometries \(v_k\) with \(v_k^*v_k\le q_k\), \(v_kv_k^*\le p_k\), \(\chi_2(p_k-v_kv_k^*)\le\varepsilon\) and \(\|v_k\chi_1-\chi_2v_k\|\le6\sqrt\varepsilon\). As in the proof of Theorem 3.1,
\[
\|v_k\varphi-\lambda\varphi v_k\|\le\|[q_k,\varphi]\|+6\sqrt\varepsilon+\frac{\varphi(q_k)}{\varphi(p_k)}\|[p_k,\varphi]\|+\Big|\frac{\varphi(q_k)}{\varphi(p_k)}-\lambda\Big| ,
\]
which tends to \(0\) as \(n\to\infty\). Further, \(1-\sum_kv_kv_k^*=\sum_k(p_k-v_kv_k^*)\) is a projection with \(\varphi\)-value at most \(\sum_k\varphi(p_k)\varepsilon\le2\varepsilon\), so it tends to \(0\) \(*\)-strongly. Writing \(v_{k,n}\) for these \(v_k\) proves the first part. The second follows from Lemma 1.2, since a sequence converging \(*\)-strongly converges along every \(\omega\). \(\square\)

**Corollary 4.2.** Let \(M\) be a type III₁ factor with separable predual and \(\varphi,\psi\) faithful normal states. There are unitaries \(u_n\in M\) with \(\|u_n\varphi u_n^*-\psi\|\to0\), and for every free ultrafilter \(\omega\) their class \(U\in M^\omega\) is a unitary with \(U\varphi^\omega U^*=\psi^\omega\).

**Proof.** (HC1) gives the \(u_n\), and Lemma 1.3 the rest. \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that if \(v\in M\) satisfies \(v\varphi=\lambda\varphi v\) exactly, then \(\varphi(v^*v)=\lambda\varphi(vv^*)\). Deduce that a coisometry with this property exists only if \(\lambda\le1\).

**Exercise 5.2.** Show that the constant sequences in \(A_{\varphi,\omega}\) are exactly the constants from \(M_\varphi\), and deduce from Theorem 3.1 that, for \(M\) of type III₁ with separable predual, an element of \(M_\varphi\) commuting with every element of \(M_{\varphi,\omega}\) is a scalar.

**Exercise 5.3.** Let \(M=B(\ell^2(\mathbb N))\) and \(\varphi=\operatorname{Tr}(\rho\,\cdot\,)\) with \(\rho\) diagonal with entries \(2^{-k}\), \(k\ge1\). Using Theorem 6.6(2) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#6-almost-commuting-with-varphi-means-almost-fixed-by-the-modular-group), show that \(M_{\varphi,\omega}\) is abelian and not \(\mathbb C\). So Theorem 3.1 needs the type III₁ hypothesis.

**Exercise 5.4.** In the proof of Lemma 2.1, check that the state \(\theta\) is faithful when \(0<\lambda<1\).

## 6. Solutions

**5.1.** Apply both sides of \(v\varphi=\lambda\varphi v\) to \(v^*\): \(\varphi(v^*v)=(v\varphi)(v^*)=\lambda(\varphi v)(v^*)=\lambda\varphi(vv^*)\). If \(vv^*=1\), then \(\lambda=\varphi(v^*v)\le1\).

**5.2.** A constant sequence \((a)\) lies in \(A_{\varphi,\omega}\) exactly when \([a,\varphi]=0\), that is \(a\in M_\varphi\), by (B6). If \(a\in M_\varphi\) commutes with \(M_{\varphi,\omega}\), its class lies in the centre of the factor \(M_{\varphi,\omega}\), so it equals \(c1\) for a scalar \(c\); then \(\|a-c\|_\varphi=0\) and \(a=c\).

**5.3.** \(\Delta_\varphi\) has eigenvalues \(2^{j-k}\), so its spectrum is \(\{2^m:m\in\mathbb Z\}\cup\{0\}\), in which \(1\) is isolated. By Theorem 6.6(2) there, every element of \(M_{\varphi,\omega}\) is represented by a sequence in \(M_\varphi\), the diagonal operators, which form an abelian algebra; so \(M_{\varphi,\omega}\) is abelian. The constant class of the first diagonal matrix unit is a projection of trace \(1/2\), so \(M_{\varphi,\omega}\ne\mathbb C\).

**5.4.** If \(x\ge0\) and \(\theta(x)=0\), then \(\psi(w_i^*xw_i)=0\), so \(x^{1/2}w_i=0\) since \(\psi\) is faithful. Then \(x^{1/2}=x^{1/2}(w_1w_1^*+w_2w_2^*)=0\).

## References

- [Ando–Haagerup] H. Ando, U. Haagerup, Ultraproducts of von Neumann algebras, Journal of Functional Analysis 266 (2014), 6842–6913. https://arxiv.org/abs/1212.5457
- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
