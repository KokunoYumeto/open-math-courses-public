# The two relative products

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(N\subset M\) be an inclusion with expectation, \(N\) a factor of type III₁, and \(\mathrm B\) the relative bicentralizer of a faithful normal state \(\varphi\) of \(N\). Elements of \(N\) and of \(\mathrm B\) can be multiplied in two orders, and on vectors both products are isometric: \(\|xa\Omega\|=\|ax\Omega\|=\|x\Omega\|\,\|a\Omega\|\) (Proposition 2.2). This gives two isometries \(R\) and \(L\) from \(L^2(N)\otimes L^2(\mathrm B)\) into \(L^2(M)\), and a contraction \(U=L^*R\) comparing them. On an element \(x\) of \(N\) that is a modular eigenoperator of frequency \(h\), one has \(xa=\gamma_h(a)x\), and \(U\) acts as the flow \(\gamma_h\) on the second factor (Proposition 2.3). The following lessons prove that in general \(U\) equals the unitary \(D=\exp(iX\otimes Y)\), where \(X\) generates the modular group of \(\varphi\) and \(Y\) the relative bicentralizer flow. This is the central identity of OpenAI's proof that expected inclusions have amenable subalgebras preserving core commutants [OAI, Section 4 and Theorem 6.2].

This lesson sets up \(U\), \(D\) and their products along words with interspersed flow shifts, and constructs, for each word, a unital completely positive map \(Z\) from \(B(L^2(M))\) to the bounded operators on a tensor power of \(L^2(N)\) [OAI, Lemma 5.2]. Its coefficients reproduce the matrix coefficients of the word. Its marginals are those of \(\varphi\). It transports the modular operator of \(M\) to the total modular energy of the tensor power. The next lesson feeds the states \(\langle Z(\cdot)\xi,\xi\rangle\) into the binormal identity.

We use: Corollary 2.6 and Theorem 2.3 of [The relative bicentralizer](the-relative-bicentralizer.md); Theorem 3.1 and formula (3.2) of [Transition isomorphisms and the relative flow](transition-isomorphisms-and-the-relative-flow.md); Section 1 of [Binormal states and the relative bicentralizer](binormal-states-and-the-relative-bicentralizer.md); Theorem 4.1, formula (4.1) and Corollary 1.3 of [Spectral shift maps](spectral-shift-maps.md); Lemma 1.2 of [Modular averaging and bounded recovery](course:bicentralizers-of-type-iii1-factors/modular-averaging-and-bounded-recovery#1-notation-and-two-modular-estimates); Stone's theorem, Section 8 of [Analytic elements and strip arguments](course:analytic-elements-strips-and-kms/analytic-elements-and-strip-arguments#8-unitary-groups-spectral-form-stone-s-theorem-cores-and-analytic-vectors); Fourier uniqueness on \(L^1(\mathbb R)\), FF-2 of [Fourier and closed-form foundations for the state core](course:OA-FLOW/OA-FLOW-FF#OA-FLOW.FF.2); and the Stone–Weierstrass theorem, [Function algebras and uniform approximation](course:foundations-of-von-neumann-algebras/support/function-algebras#OA-FND-SW-01).

## 1. Setting

Throughout, \(N\) is a factor of type III₁ with separable predual, \(N\subset M\) with the same unit, \(M\) with separable predual, \(E\colon M\to N\) a faithful normal conditional expectation, \(\varphi\) a faithful normal state on \(N\) and \(\bar\varphi=\varphi\circ E\). Let \(\mathcal H=L^2(M,\bar\varphi)\) with cyclic and separating vector \(\Omega\) (the vector \(\xi\) of the previous lessons), modular operator \(\Delta\), \(\mathcal X=\log\Delta\), \(\sigma_t=\sigma^{\bar\varphi}_t\), \(\rho(b)=Jb^*J\), and \(e_N\) the Jones projection. Elements of \(M\) act on \(\mathcal H\) on the left. Write \(\mathrm B=\mathrm B(N\subset M,\varphi)\), \(E_{\mathrm B}\) for its \(\bar\varphi\)-preserving expectation, and \(\gamma_s=\gamma^\varphi_s\) for the relative bicentralizer flow. For each \(q\in\mathbb R\) we fix a map \(\theta_q\) as in Theorem 4.1 of the lesson on spectral shift maps. Two consequences of the first lesson are used constantly: by its Corollary 2.6,
\[
E(b)=\bar\varphi(b)1\quad(b\in\mathrm B),\qquad E_{\mathrm B}(x)=\varphi(x)1\quad(x\in N),
\tag{1.1}
\]
and therefore, by Theorem 4.1(2) of the lesson on spectral shift maps,
\[
\theta_q(x)=\gamma_q(E_{\mathrm B}(x))=\varphi(x)1\qquad(x\in N,\ q\in\mathbb R).
\tag{1.2}
\]

Let \(H\) be the closure of \(N\Omega\) and \(K\) the closure of \(\mathrm B\Omega\) in \(\mathcal H\). Since \(\sigma_t(N)=N\) and \(\sigma_t(\mathrm B)=\mathrm B\) (formula (1.1) and Theorem 2.3 of the first lesson), and \(\Delta^{it}y\Omega=\sigma_t(y)\Omega\), the unitaries \(\Delta^{it}\) leave \(H\) and \(K\) invariant. Let \(X\) be the self-adjoint generator of the restriction of \(\Delta^{it}\) to \(H\), so that \(e^{itX}x\Omega=\sigma_t(x)\Omega\) for \(x\in N\), and write \(\Delta_K^{it}\) for the restriction of \(\Delta^{it}\) to \(K\).

**Lemma 1.1.** There is a strongly continuous unitary group \((W_s)_{s\in\mathbb R}\) on \(K\) with \(W_sa\Omega=\gamma_s(a)\Omega\) for \(a\in\mathrm B\). It commutes with \(\Delta_K^{it}\). Write \(W_s=e^{isY}\) with \(Y\) self-adjoint on \(K\).

**Proof.** By Theorem 3.1(3) of the lesson on the relative flow, \(\gamma_s\) preserves \(\bar\varphi\) on \(\mathrm B\), so \(a\Omega\mapsto\gamma_s(a)\Omega\) is isometric and extends to an isometry \(W_s\) of \(K\). The group law \(\gamma_s\gamma_{s'}=\gamma_{s+s'}\) gives \(W_sW_{s'}=W_{s+s'}\) and \(W_0=1\), so each \(W_s\) is unitary. By Theorem 3.1(4) there, \(\|W_sa\Omega-a\Omega\|=\|\gamma_s(a)-a\|_{\bar\varphi}\to0\) as \(s\to0\), and the \(W_s\) are uniformly bounded, so the group is strongly continuous. By Theorem 3.1(6) there, \(\gamma_s\sigma_t=\sigma_t\gamma_s\) on \(\mathrm B\), hence \(W_s\Delta^{it}a\Omega=\Delta^{it}W_sa\Omega\). Stone's theorem gives \(Y\). \(\square\)

## 2. Two isometries and their comparison

**Proposition 2.2.** The maps
\[
R(x\Omega\otimes a\Omega)=xa\Omega,\qquad L(x\Omega\otimes a\Omega)=ax\Omega\qquad(x\in N,\ a\in\mathrm B)
\]
extend to isometries \(R,L\colon H\otimes K\to\mathcal H\).

**Proof.** The vector \(x\Omega\) determines \(x\), because \(\Omega\) is separating, so both formulas are bilinear in \((x\Omega,a\Omega)\) and define linear maps on the algebraic tensor product \(N\Omega\odot\mathrm B\Omega\), which is dense in \(H\otimes K\). For \(x,y\in N\) and \(a,b\in\mathrm B\), \(E_{\mathrm B}\) is \(\mathrm B\)-bimodular and \(E\) is \(N\)-bimodular, so by (1.1)
\[
\langle xa\Omega,yb\Omega\rangle=\bar\varphi\big(b^*E_{\mathrm B}(y^*x)a\big)=\varphi(y^*x)\bar\varphi(b^*a),\qquad
\langle ax\Omega,by\Omega\rangle=\varphi\big(y^*E(b^*a)x\big)=\varphi(y^*x)\bar\varphi(b^*a).
\]
Both equal \(\langle x\Omega\otimes a\Omega,y\Omega\otimes b\Omega\rangle\). By sesquilinearity both maps preserve inner products on the algebraic tensor product, and they extend by continuity. \(\square\)

Define the contraction \(U\) and the unitary \(D\) on \(H\otimes K\) by
\[
U=L^*R,\qquad D=\exp(iX\otimes Y),
\]
where \(D\) is defined by the joint spectral measure of the commuting self-adjoint operators \(X\otimes1\) and \(1\otimes Y\). By Lemma 1.1, \(D\) commutes with \(1\otimes\Delta_K^{it}\) and with \(e^{itX}\otimes1\). Since \(L\) is isometric,
\[
\langle U(x\Omega\otimes a\Omega),y\Omega\otimes b\Omega\rangle=\langle xa\Omega,by\Omega\rangle=\bar\varphi(y^*b^*xa)\qquad(x,y\in N,\ a,b\in\mathrm B).
\tag{2.1}
\]
Moreover, for \(\zeta\in K\),
\[
\langle U(x\Omega\otimes\zeta),y\Omega\otimes b\Omega\rangle=\langle\zeta,E_{\mathrm B}(x^*by)\Omega\rangle .
\tag{2.2}
\]
Indeed, for \(\zeta=a\Omega\), (2.1) and the bimodule property of \(E_{\mathrm B}\) give \(\bar\varphi(y^*b^*xa)=\bar\varphi(E_{\mathrm B}(y^*b^*x)a)=\langle a\Omega,E_{\mathrm B}(x^*by)\Omega\rangle\); both sides of (2.2) are continuous in \(\zeta\).

**Proposition 2.3** (exact eigenoperators). Let \(x\in N\) and \(h\in\mathbb R\) with \(\sigma_t(x)=e^{ith}x\) for all \(t\). Then \(U(x\Omega\otimes\zeta)=x\Omega\otimes W_h\zeta=D(x\Omega\otimes\zeta)\) for every \(\zeta\in K\).

**Proof.** By Corollary 1.3 of the lesson on spectral shift maps, \(x\varphi=e^{-h}\varphi x\), and by Theorem 3.1(2) of the lesson on the relative flow, \(xa=\beta^\varphi_{e^{-h}}(a)x=\gamma_h(a)x\) for \(a\in\mathrm B\). Hence \(R(x\Omega\otimes a\Omega)=\gamma_h(a)x\Omega=L(x\Omega\otimes W_ha\Omega)\), and since \(L^*L=1\), \(U(x\Omega\otimes a\Omega)=x\Omega\otimes W_ha\Omega\). Both sides are continuous in \(\zeta\in K\). Finally \(e^{itX}x\Omega=e^{ith}x\Omega\), so \(x\Omega\) is an eigenvector of \(X\) for the eigenvalue \(h\), and \(D(x\Omega\otimes\zeta)=x\Omega\otimes e^{ihY}\zeta\). \(\square\)

## 3. Words

For \(n\ge1\) we work on \(H^{\otimes n}\otimes K\). Let \(X_j\), \(U_j\), \(D_j\) denote \(X\), \(U\), \(D\) acting on the \(j\)-th copy of \(H\) (together with \(K\) for \(U_j,D_j\)), and \(W_s\) act on \(K\). Put \(S_n=\sum_{j=1}^nX_j\), the total modular generator on \(H^{\otimes n}\). For real numbers \(d_0,\ldots,d_n\) define
\[
C=W_{d_n}U_nW_{d_{n-1}}U_{n-1}\cdots W_{d_1}U_1W_{d_0},\qquad D_{\mathrm{all}}=W_d\exp(iS_n\otimes Y),\qquad d=\sum_{j=0}^nd_j .
\tag{3.1}
\]

**Lemma 3.1.** The operators \(D_j\) commute with each other and with every \(W_s\), and \(D_n\cdots D_1=\exp(iS_n\otimes Y)\). Consequently, replacing every \(U_j\) in \(C\) by \(D_j\) gives \(D_{\mathrm{all}}\). The word \(C\) is a contraction.

**Proof.** All \(D_j\) and \(W_s\) are bounded Borel functions of the commuting self-adjoint operators \(X_1,\ldots,X_n\) and \(Y\), so they commute, and the functional calculus gives \(\prod_je^{iX_j\otimes Y}=e^{i(\sum_jX_j)\otimes Y}\). \(\square\)

For \(x,y\in N\) define \(U_{x,y}\in B(K)\) by \(\langle U_{x,y}\zeta,\zeta'\rangle=\langle U(x\Omega\otimes\zeta),y\Omega\otimes\zeta'\rangle\). By (2.2),
\[
U_{x,y}^*b\Omega=E_{\mathrm B}(x^*by)\Omega\qquad(b\in\mathrm B).
\tag{3.2}
\]

**Lemma 3.2** (matrix coefficients of words). For \(x_j,y_j\in N\) and \(\zeta,\zeta'\in K\),
\[
\Big\langle C\Big(\bigotimes_jx_j\Omega\otimes\zeta\Big),\bigotimes_jy_j\Omega\otimes\zeta'\Big\rangle=\big\langle W_{d_n}U_{x_n,y_n}W_{d_{n-1}}\cdots U_{x_1,y_1}W_{d_0}\zeta,\zeta'\big\rangle .
\]

**Proof.** For an operator \(A\) on \(H\otimes K\) and \(x,y\in H\) let \(A_{x,y}\in B(K)\) be given by \(\langle A_{x,y}\zeta,\zeta'\rangle=\langle A(x\otimes\zeta),y\otimes\zeta'\rangle\). If \((e_k)\) is an orthonormal basis of \(H\), then \(A(x\otimes\zeta)=\sum_ke_k\otimes A_{x,e_k}\zeta\). We prove by induction on \(n\) that for operators \(A_j\) acting on the \(j\)-th copy of \(H\) and on \(K\), and \(B_j\in B(K)\),
\[
\big\langle B_nA_n\cdots B_1A_1B_0\big(\textstyle\bigotimes_jx_j\otimes\zeta\big),\bigotimes_jy_j\otimes\zeta'\big\rangle=\big\langle B_n(A_n)_{x_n,y_n}\cdots B_1(A_1)_{x_1,y_1}B_0\zeta,\zeta'\big\rangle .
\]
For \(n=1\) this is the definition. For the inductive step write \(B_1A_1B_0(x_1\otimes\zeta)=\sum_ke_k\otimes\zeta_k\) with \(\zeta_k=B_1(A_1)_{x_1,e_k}B_0\zeta\). The remaining operators do not act on the first copy of \(H\), so the left side equals \(\sum_k\langle e_k,y_1\rangle\) times the corresponding expression for \(n-1\) positions with \(\zeta_k\) in place of \(\zeta\). By the inductive hypothesis and \(\sum_k\langle e_k,y_1\rangle\zeta_k=B_1(A_1)_{x_1,y_1}B_0\zeta\), the formula follows. Apply it with \(A_j=U_j\), \(B_j=W_{d_j}\). \(\square\)

## 4. The iterated kernel

Fix \(n\ge1\) and \(d_0,\ldots,d_n\in\mathbb R\). For \(T\in B(\mathcal H)\) and label tuples \(\mathbf x=(x_1,\ldots,x_n)\), \(\mathbf y=(y_1,\ldots,y_n)\) in \(N^n\), define operators \(T_j=T_j^{\mathbf x,\mathbf y}\) backwards by
\[
T_n=\theta_{-d_n}(T),\qquad T_{j-1}=\theta_{-d_{j-1}}\big(y_j^*T_jx_j\big)\quad(j=n,\ldots,1),
\]
and put \(\kappa_T(\mathbf x,\mathbf y)=\langle T_0\Omega,\Omega\rangle\). Write \(\mathbf x\Omega=\bigotimes_jx_j\Omega\in H^{\otimes n}\).

**Proposition 4.1** (the iterated kernel). There is a unique unital completely positive map \(Z\colon B(\mathcal H)\to B(H^{\otimes n})\) with \(\langle Z(T)\mathbf x\Omega,\mathbf y\Omega\rangle=\kappa_T(\mathbf x,\mathbf y)\) for all label tuples. It satisfies:

1. \(Z(a)=Z(\rho(a))=\bar\varphi(a)1\) for \(a\in M\), and \(Z(e_N)=1\);
2. \(Z(\Delta^{it})=e^{it(S_n+d)}\) for \(t\in\mathbb R\);
3. \(Z(f(\mathcal X))=f(S_n+d)\) for \(f\in C_0(\mathbb R)\);
4. for \(b\in\mathrm B\), \(a\in\mathrm B\) entire analytic for \(\sigma\), \(a_+=\sigma_{i/2}(a)\), and \(\xi,\xi'\in H^{\otimes n}\),
\[
\langle Z(b^*\rho(a_+))\xi,\xi'\rangle=\langle C(\xi\otimes a\Omega),\xi'\otimes b\Omega\rangle .
\]

The map \(Z\) depends on \(n\), on \(d_0,\ldots,d_n\) and on the chosen maps \(\theta_q\); it need not be normal. The proof occupies the rest of this section.

**Construction.** *Positivity.* Let \(\mathbf x^1,\ldots,\mathbf x^p\in N^n\), \(m\ge1\) and \(\mathbf T=(T_{kl})\in M_m(B(\mathcal H))\) positive. Consider operator matrices indexed by pairs \((k,\beta)\), \(1\le k\le m\), \(1\le\beta\le p\). Put \(\mathbf T^{(n)}=\big(\theta_{-d_n}(T_{kl})\big)_{(k,\beta),(l,\alpha)}\), and recursively
\[
\mathbf T^{(j-1)}=\theta_{-d_{j-1}}^{(mp)}\big(\mathbf X_j^*\mathbf T^{(j)}\mathbf X_j\big),\qquad\mathbf X_j=\operatorname{diag}\big(x_j^\alpha\big)_{(l,\alpha)},
\]
where \(\theta^{(mp)}\) applies \(\theta\) entrywise. The entry \(((k,\beta),(l,\alpha))\) of \(\mathbf T^{(0)}\) is \((T_{kl})_0^{\mathbf x^\alpha,\mathbf x^\beta}\). The matrix \(\mathbf T^{(n)}\) is positive: for vectors \(w_{(l,\alpha)}\), its quadratic form is that of the positive matrix \(\theta^{(m)}_{-d_n}(\mathbf T)\) at the vectors \(\sum_\alpha w_{(l,\alpha)}\). Conjugation and the completely positive maps \(\theta\) preserve positivity, so \(\mathbf T^{(0)}\ge0\), and therefore, for scalars \(c_{l\alpha}\),
\[
\sum_{k,l}\sum_{\alpha,\beta}\overline{c_{k\beta}}\,c_{l\alpha}\,\kappa_{T_{kl}}(\mathbf x^\alpha,\mathbf x^\beta)\ \ge\ 0 .
\tag{4.1}
\]

*The Gram kernel.* For \(T=1\), \(T_n=1\) and by (1.2) \(T_{j-1}=\theta_{-d_{j-1}}(y_j^*T_jx_j)\) is a scalar multiple of \(1\) at every step, so \(\kappa_1(\mathbf x,\mathbf y)=\prod_j\varphi(y_j^*x_j)=\langle\mathbf x\Omega,\mathbf y\Omega\rangle\).

*The operator.* Let \(V\) be the vector space of formal finite linear combinations of label tuples, with the canonical linear map \(\iota\colon V\to H^{\otimes n}\), \(\iota(\mathbf x)=\mathbf x\Omega\), whose range is the dense algebraic tensor product of copies of \(N\Omega\). Extend \(\kappa_T\) sesquilinearly to \(V\times V\). For \(0\le T\), (4.1) with \(m=1\) applied to \(T\) and to \(\|T\|-T\), together with the Gram kernel, gives \(0\le\kappa_T(v,v)\le\|T\|\,\|\iota(v)\|^2\). If \(\iota(v)=0\), then \(\kappa_T(v,v)=0\), and the Cauchy–Schwarz inequality for the positive form \(\kappa_T\) gives \(\kappa_T(v,w)=0\) for all \(w\). So \(\kappa_T\) factors through \(\iota\) and is bounded by \(\|T\|\). Writing a general \(T\) as a combination of four positive operators of norm at most \(\|T\|\), we obtain a bounded operator \(Z(T)\) on \(H^{\otimes n}\) with \(\langle Z(T)\iota(v),\iota(w)\rangle=\kappa_T(v,w)\). The map \(Z\) is linear, \(Z(1)=1\), and (4.1) for general \(m\) says that \(Z\) is completely positive on the dense subspace \(\iota(V)\), hence everywhere by continuity. Uniqueness is clear.

**Proof of (1).** Let \(a\in M\). Then \(T_n=\theta_{-d_n}(a)=\gamma_{-d_n}(E_{\mathrm B}(a))\in\mathrm B\) and \(\bar\varphi(T_n)=\bar\varphi(a)\). If \(T_j\in\mathrm B\), then \(T_{j-1}=\gamma_{-d_{j-1}}(E_{\mathrm B}(y_j^*T_jx_j))\in\mathrm B\), and by (1.1)
\[
\bar\varphi(T_{j-1})=\bar\varphi(y_j^*T_jx_j)=\varphi\big(y_j^*E(T_j)x_j\big)=\bar\varphi(T_j)\,\varphi(y_j^*x_j).
\]
Hence \(\kappa_a(\mathbf x,\mathbf y)=\bar\varphi(T_0)=\bar\varphi(a)\prod_j\varphi(y_j^*x_j)\), that is \(Z(a)=\bar\varphi(a)1\). For \(\rho(c)\), \(c\in M\): \(\rho(c)\) commutes with \(N\), and by Theorem 4.1(3) of the lesson on spectral shift maps \(\theta_q(T\rho(c))=\theta_q(T)\rho(c)\). Inductively \(T_j=\big(\prod_{i>j}\varphi(y_i^*x_i)\big)\rho(c)\), using (1.2), and \(\langle\rho(c)\Omega,\Omega\rangle=\bar\varphi(c)\). For \(e_N\), which commutes with \(N\) and is fixed by every \(\theta_q\), the same computation with Theorem 4.1(3) gives \(T_0=\prod_j\varphi(y_j^*x_j)\,e_N\), and \(e_N\Omega=\Omega\).

**Proof of (2).** By formula (4.1) of the lesson on spectral shift maps, \(\theta_{-q}(T\Delta^{it})=e^{itq}\theta_{-q}(T)\Delta^{it}\). Put \(T=\Delta^{it}\). Then \(T_n=e^{itd_n}\Delta^{it}\). If \(T_j=c_j\Delta^{it}\) with \(c_j\in\mathbb C\), then \(y_j^*T_jx_j=c_jy_j^*\sigma_t(x_j)\Delta^{it}\), and by (1.2)
\[
T_{j-1}=c_je^{itd_{j-1}}\theta_{-d_{j-1}}\big(y_j^*\sigma_t(x_j)\big)\Delta^{it}=c_je^{itd_{j-1}}\varphi\big(y_j^*\sigma_t(x_j)\big)\Delta^{it}.
\]
Since \(\Delta^{it}\Omega=\Omega\), \(\kappa_{\Delta^{it}}(\mathbf x,\mathbf y)=e^{itd}\prod_j\varphi(y_j^*\sigma_t(x_j))=e^{itd}\prod_j\langle e^{itX}x_j\Omega,y_j\Omega\rangle=\langle e^{it(S_n+d)}\mathbf x\Omega,\mathbf y\Omega\rangle\).

**Proof of (3).** A nonnormal map need not preserve the integral \(f(\mathcal X)=\int h(t)\Delta^{it}dt\), so (2) does not imply (3) directly. We show that the states \(\langle Z(\cdot)\xi,\xi\rangle\) see only a bounded part of the spectrum of \(\mathcal X\) when \(\xi\) has band-limited labels.

*Band-limited elements.* Let \(L>0\). Call \(x\in M\) *band-limited with bound \(L\)* if \(x=\int k(t)\sigma_t(y)\,dt\) for some \(y\in M\) and some \(k\in L^1(\mathbb R)\) whose transform \(\hat k(u)=\int k(t)e^{itu}dt\) vanishes for \(|u|>L\). For a Borel set \(J\subset\mathbb R\) write \(E_{\mathcal X}(J)\) for the spectral projection of \(\mathcal X\) and \(J^L=\{u:\operatorname{dist}(u,J)\le L\}\).

**Lemma 4.2** (spectral transfer). If \(x\) is band-limited with bound \(L\) and \(J\) is an open interval, then \(xE_{\mathcal X}(J)\mathcal H\subset E_{\mathcal X}(J^L)\mathcal H\). In particular \(x\Omega\in E_{\mathcal X}([-L,L])\mathcal H\).

**Proof.** Let \(a,b\in L^1(\mathbb R)\) and write \(\hat a(\mathcal X)=\int a(r)\Delta^{ir}dr\), \(\hat b(\mathcal X)=\int b(r)\Delta^{ir}dr\). For vectors \(\eta,\zeta\), the function \(G(\alpha,\beta)=\langle\Delta^{i\alpha}y\Delta^{i\beta}\eta,\zeta\rangle\) is bounded and continuous, and \(\Delta^{ir}\sigma_t(y)\Delta^{ir'}=\Delta^{i(r+t)}y\Delta^{i(r'-t)}\). By Fubini's theorem and the substitution \(\alpha=r+t\), \(\beta=r'-t\),
\[
\langle\hat a(\mathcal X)x\hat b(\mathcal X)\eta,\zeta\rangle=\iiint a(r)b(r')k(t)G(r+t,r'-t)\,dt\,dr\,dr'=\iint c(\alpha,\beta)G(\alpha,\beta)\,d\alpha\,d\beta,
\]
with \(c(\alpha,\beta)=\int a(\alpha-t)b(\beta+t)k(t)\,dt\), an element of \(L^1(\mathbb R^2)\). Its transform is
\[
\hat c(u,v)=\iint c(\alpha,\beta)e^{iu\alpha+iv\beta}d\alpha\,d\beta=\hat a(u)\,\hat b(v)\,\hat k(u-v).
\]
Suppose \(\hat a(u)\hat b(v)=0\) whenever \(|u-v|\le L\). Then \(\hat c\equiv0\). For almost every \(\beta\), \(c(\cdot,\beta)\in L^1\), and \(F(u,\beta)=\int c(\alpha,\beta)e^{iu\alpha}d\alpha\) is continuous in \(u\); for each \(u\), \(\beta\mapsto F(u,\beta)\) is integrable with vanishing Fourier transform, hence zero almost everywhere by Fourier uniqueness. Taking \(u\) rational and using continuity, \(F(\cdot,\beta)\equiv0\) for almost every \(\beta\), so \(c=0\) almost everywhere by Fourier uniqueness again. Hence \(\hat a(\mathcal X)x\hat b(\mathcal X)=0\).

Now let \(J'=\mathbb R\setminus J^L\), an open set, and choose \(\hat a_m\in C_c^\infty(J')\), \(\hat b_m\in C_c^\infty(J)\) with values in \([0,1]\), increasing pointwise to \(1_{J'}\) and \(1_J\); their inverse Fourier transforms are integrable. If \(u\in J'\) and \(v\in J\), then \(|u-v|>L\). So \(\hat a_m(\mathcal X)x\hat b_m(\mathcal X)=0\), and letting \(m\to\infty\) strongly, \(E_{\mathcal X}(J')xE_{\mathcal X}(J)=0\). For the last statement, \(\Omega\in E_{\mathcal X}((-\varepsilon,\varepsilon))\mathcal H\) for every \(\varepsilon>0\), so \(x\Omega\in E_{\mathcal X}([-L-\varepsilon,L+\varepsilon])\mathcal H\) for every \(\varepsilon\). \(\square\)

Band-limited elements of \(N\) give dense vectors in \(H\): choose \(f_1\in C_c^\infty(\mathbb R)\) with \(0\le f_1\le1\), \(f_1(0)=1\) and \(f_1=0\) outside \([-1,1]\), let \(k_1\) be its integrable inverse Fourier transform, and \(k_L(t)=Lk_1(Lt)\), so that \(\hat k_L(u)=f_1(u/L)\). For \(y\in N\), \(y_L=\int k_L(t)\sigma_t(y)\,dt\) lies in \(N\), because \(N\) is \(\sigma\)-weakly closed and \(\sigma\)-invariant, and it is band-limited with bound \(L\). By Lemma 1.2 of the modular averaging lesson, \(y_L\Omega=f_1(\mathcal X/L)y\Omega\to y\Omega\) as \(L\to\infty\). Hence the span \(V_{\mathrm{bl}}\) of the vectors \(\mathbf x\Omega\) with band-limited labels is dense in \(H^{\otimes n}\).

*The multiplicative domain.* By formula (4.1) of the lesson on spectral shift maps, for \(g\in C_0(\mathbb R)\) and \(T\in B(\mathcal H)\),
\[
\theta_{-q}(Tg(\mathcal X))=\theta_{-q}(T)\,g(\mathcal X+q).
\tag{4.2}
\]
Say that an operator \(T\) *annihilates* an open interval \(I\) if \(TE_{\mathcal X}(I)=0\). If \(T\) annihilates \(I\), then \(Tg(\mathcal X)=0\) for \(g\in C_c(I)\), so by (4.2) \(\theta_{-q}(T)g(\mathcal X+q)=0\); the ranges of the operators \(g(\mathcal X+q)\), \(g\in C_c(I)\), span a dense subspace of \(E_{\mathcal X}(I-q)\mathcal H\), so \(\theta_{-q}(T)\) annihilates \(I-q\). If \(T\) annihilates \(I=(c-r,c+r)\), \(x\) is band-limited with bound \(L<r\), and \(y\in M\), then \(y^*Tx\) annihilates \(I'=(c-r+L,c+r-L)\): every open interval \(J\) with \(\overline J\subset I'\) has \(J^L\subset I\), so Lemma 4.2 gives \(y^*TxE_{\mathcal X}(J)=y^*TE_{\mathcal X}(J^L)xE_{\mathcal X}(J)=0\), and an increasing sequence of such \(J\) exhausts \(I'\).

*Cutting the spectrum.* Let \(\mathbf x^1,\ldots,\mathbf x^p\) be label tuples whose entries are band-limited, with bounds whose sums over \(j\) are at most \(\Lambda\), and let \(R>\Lambda+|d|\). Let \(A=E_{\mathcal X}(\mathbb R\setminus[-R,R])\), which annihilates \((-R,R)\). Following the recursion for \(\kappa_A(\mathbf x^\alpha,\mathbf x^\beta)\), the two rules above show that \(A_j\) annihilates an open interval obtained from \((-R,R)\) by translating by \(-d_n,\ldots,-d_j\) and shrinking by the bounds of the labels \(x_n^\alpha,\ldots,x_{j+1}^\alpha\) on each side. At the end \(A_0\) annihilates an interval containing \((-R+\Lambda-d,\,R-\Lambda-d)\ni0\), hence \(A_0\Omega=0\) because \(\Omega\in E_{\mathcal X}(\{0\})\mathcal H\). So \(\kappa_A(\mathbf x^\alpha,\mathbf x^\beta)=0\) for all \(\alpha,\beta\).

*Conclusion.* Let \(\xi=\sum_\alpha c_\alpha\mathbf x^\alpha\Omega\in V_{\mathrm{bl}}\) and \(\Phi_\xi(T)=\langle Z(T)\xi,\xi\rangle\), a positive functional. With \(P_R=E_{\mathcal X}([-R,R])\), we have shown \(\Phi_\xi(1-P_R)=0\), so \(\Phi_\xi(T)=\Phi_\xi(P_RTP_R)\) for all \(T\) by the Cauchy–Schwarz inequality. By Lemma 4.2 each \(x_j^\alpha\Omega\) lies in the spectral subspace of \(X\) for an interval \([-L_j^\alpha,L_j^\alpha]\), so \(\xi\) lies in the spectral subspace of \(S_n+d\) for \([-R,R]\). Let \(f\in C_0(\mathbb R)\) and \(\varepsilon>0\). By the Stone–Weierstrass theorem there is a finite linear combination \(g\) of the functions \(u\mapsto e^{itu}\) with \(|f-g|\le\varepsilon\) on \([-R,R]\). Then
\[
|\Phi_\xi(f(\mathcal X))-\Phi_\xi(g(\mathcal X))|=|\Phi_\xi(P_R(f-g)(\mathcal X)P_R)|\le\varepsilon\|\xi\|^2,\qquad|\langle(f-g)(S_n+d)\xi,\xi\rangle|\le\varepsilon\|\xi\|^2,
\]
and \(\Phi_\xi(g(\mathcal X))=\langle g(S_n+d)\xi,\xi\rangle\) by (2). Hence \(\langle Z(f(\mathcal X))\xi,\xi\rangle=\langle f(S_n+d)\xi,\xi\rangle\) on \(V_{\mathrm{bl}}\); polarization and continuity give (3).

**Proof of (4).** By (1.1) of the lesson on binormal states, \(\rho(a_+)\Omega=a\Omega\). Let \(\mathbf x,\mathbf y\) be label tuples, and define \(c_n=\gamma_{-d_n}(b^*)\) and \(c_{j-1}=\gamma_{-d_{j-1}}(E_{\mathrm B}(y_j^*c_jx_j))\), elements of \(\mathrm B\). For \(T=b^*\rho(a_+)\), Theorem 4.1(2),(3) of the lesson on spectral shift maps give \(T_n=\theta_{-d_n}(b^*)\rho(a_+)=c_n\rho(a_+)\), and, since \(\rho(a_+)\) commutes with \(N\), inductively \(T_{j-1}=\theta_{-d_{j-1}}(y_j^*c_jx_j)\rho(a_+)=c_{j-1}\rho(a_+)\). Hence \(\kappa_T(\mathbf x,\mathbf y)=\langle c_0\rho(a_+)\Omega,\Omega\rangle=\bar\varphi(c_0a)\).

On the other side, Lemma 3.2 gives \(\langle C(\mathbf x\Omega\otimes a\Omega),\mathbf y\Omega\otimes b\Omega\rangle=\langle a\Omega,W_{-d_0}U^*_{x_1,y_1}\cdots U^*_{x_n,y_n}W_{-d_n}b\Omega\rangle\). Now \(W_{-d_n}b\Omega=\gamma_{-d_n}(b)\Omega=c_n^*\Omega\), and if the vector at some stage is \(c_j^*\Omega\), then (3.2) gives \(U^*_{x_j,y_j}c_j^*\Omega=E_{\mathrm B}(x_j^*c_j^*y_j)\Omega=E_{\mathrm B}(y_j^*c_jx_j)^*\Omega\), and \(W_{-d_{j-1}}\) turns it into \(c_{j-1}^*\Omega\). The result is \(\langle a\Omega,c_0^*\Omega\rangle=\bar\varphi(c_0a)\). Both sides of (4) are bounded sesquilinear forms in \((\xi,\xi')\) that agree on simple tensors, so they agree everywhere. \(\square\)

Statement (4) is the bridge to the binormal identity: for \(b=a\), its left side is the value at \(a^*\rho(a_+)\) of a state with the marginals of \(\bar\varphi\), and the binormal identity evaluates such values as \(\|a\Omega\|^2\).

## 5. Exercises

**Exercise 5.1.** Show that \(R(H\otimes K)\) is the closure of \(N\mathrm B\Omega\), that it contains \(\Omega\), and that it is invariant under left multiplication by \(N\). State and prove the corresponding facts for \(L(H\otimes K)\) and \(\mathrm B\).

**Exercise 5.2.** Show that \(U\) commutes with \(e^{itX}\otimes\Delta_K^{it}\) for every \(t\in\mathbb R\).

**Exercise 5.3.** Let \(n=1\) and \(d_0=d_1=0\). Show that \(\langle Z(a\rho(c))x\Omega,y\Omega\rangle=\langle E_{\mathrm B}(y^*E_{\mathrm B}(a)x)\rho(c)\Omega,\Omega\rangle\) for \(a,c\in M\) and \(x,y\in N\), and deduce \(Z(a)=\bar\varphi(a)1\) directly.

**Exercise 5.4.** Let \(x\in M\) be band-limited with bound \(L\). Show that \(x^*\) is band-limited with bound \(L\), and that \(E_{\mathcal X}(J')xE_{\mathcal X}(J)=0\) whenever \(J,J'\) are Borel sets at distance greater than \(L\).

## 6. Solutions

**5.1.** The range of an isometry is closed, and \(R\) maps the dense subspace \(N\Omega\odot\mathrm B\Omega\) onto the span of \(N\mathrm B\Omega\); so \(R(H\otimes K)\) is the closure of that span. It contains \(R(\Omega\otimes\Omega)=\Omega\). For \(y\in N\), \(yR(x\Omega\otimes a\Omega)=yxa\Omega=R(yx\Omega\otimes a\Omega)\), so the range is invariant under \(y\) by continuity. In the same way \(L(H\otimes K)\) is the closure of the span of \(\mathrm BN\Omega\), contains \(\Omega\), and is invariant under left multiplication by \(\mathrm B\), because \(bL(x\Omega\otimes a\Omega)=L(x\Omega\otimes ba\Omega)\).

**5.2.** By (2.1), \(\langle U(e^{itX}x\Omega\otimes\Delta_K^{it}a\Omega),y\Omega\otimes b\Omega\rangle=\bar\varphi(y^*b^*\sigma_t(x)\sigma_t(a))\). Since \(\bar\varphi\circ\sigma_t=\bar\varphi\), this equals \(\bar\varphi(\sigma_{-t}(y)^*\sigma_{-t}(b)^*xa)=\langle U(x\Omega\otimes a\Omega),e^{-itX}y\Omega\otimes\Delta_K^{-it}b\Omega\rangle\).

**5.3.** Here \(\theta_0(a)=\gamma_0(E_{\mathrm B}(a))=E_{\mathrm B}(a)\) for \(a\in M\), and \(\theta_0\) is a right module map over \(\rho(M)\). For \(T=a\rho(c)\): \(T_1=\theta_0(a)\rho(c)=E_{\mathrm B}(a)\rho(c)\), and since \(\rho(c)\) commutes with \(N\), \(T_0=\theta_0(y^*E_{\mathrm B}(a)x)\rho(c)=E_{\mathrm B}(y^*E_{\mathrm B}(a)x)\rho(c)\). This is the formula. For \(c=1\) it gives \(\bar\varphi(y^*E_{\mathrm B}(a)x)=\varphi\big(y^*E(E_{\mathrm B}(a))x\big)=\bar\varphi(a)\varphi(y^*x)\) by (1.1), which is \(\langle\bar\varphi(a)x\Omega,y\Omega\rangle\).

**5.4.** \(x^*=\int\overline{k(t)}\sigma_t(y^*)dt\) and \(\widehat{\bar k}(u)=\overline{\hat k(-u)}\) vanishes for \(|u|>L\). Let \(J,J'\) be Borel sets at distance \(L+3\delta\) with \(\delta>0\), and let \(J_\delta,J'_\delta\) be their open \(\delta\)-neighbourhoods, at distance at least \(L+\delta\). The first part of the proof of Lemma 4.2, with \(\hat a_m\in C_c^\infty(J'_\delta)\) and \(\hat b_m\in C_c^\infty(J_\delta)\) increasing to the indicator functions, gives \(E_{\mathcal X}(J'_\delta)xE_{\mathcal X}(J_\delta)=0\). Multiply by \(E_{\mathcal X}(J')\) on the left and \(E_{\mathcal X}(J)\) on the right.

## References

- [OAI] OpenAI, Expected amenable subalgebras preserving core commutants (September 23, 2026), OpenAI Math Release preprint. https://github.com/openai/math/blob/main/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf
