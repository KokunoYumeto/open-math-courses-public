# Preparing infinite factors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For infinite factors the proof of strong stability works with *prepared pairs*: type III\(_1\) factors on one Hilbert space with a common cyclic separating vector and a common irreducible hyperfinite II\(_1\) subfactor whose left and right actions agree (Definition 5.1). This lesson shows that two close infinite factors on a separable space become a prepared pair after tensoring with one fixed factor \(D\) and moving the second algebra by a small unitary, with control of the completely bounded distance (Proposition 5.2). The fixed factor is an infinite tensor product of \(2\times2\) matrix algebras with two incommensurable ratios. Its centralizer is irreducible, and tensoring with it makes every factor of type III\(_1\) (Proposition 2.3). The subfactor comes from the programme's construction of an injective subalgebra in a type III\(_1\) factor (Proposition 3.1), and the common vector from the uniqueness of normal representations of type III factors (Lemma 4.1) [OpenAI-289, Section 6].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4 and 1.5, Corollary 3.2, Definition 4.1 and Corollary 4.3); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Theorem 3.1 and Lemma 5.1); the Tomita–Takesaki theorem for a faithful normal state (\(S=J\Delta^{1/2}\), \(JMJ=M'\), \(\Delta^{it}M\Delta^{-it}=M\)), [Modular time from a faithful normal state](course:OA-MOD/OA-MOD-FS); the [KMS characterization of the modular group](course:OA-MOD/OA-MOD-KM); the [fixed-point criterion](course:OA-MOD/OA-MOD-CZ#recognize-exactly-the-fixed-observations) (the centralizer \(P_\varphi=\{a:\varphi(ax)=\varphi(xa)\ \forall x\}\) of a faithful normal state is the fixed-point algebra of \(\sigma^\varphi\)); the [modular expectation theorem](course:OA-MOD/OA-MOD-ME#OA-MOD-ME-01); [cone vectors of normal positive functionals](course:OA-MOD/OA-MOD-SF#OA-MOD-SF-10) and the [standard form axioms](course:OA-MOD/OA-MOD-SF#OA-MOD-SF-05); for continuous cores, [the core trace](course:OA-FLOW/OA-FLOW-CORE#core-setting), the [factor criterion (F3)](course:OA-FLOW/OA-FLOW-L116#equation-f3), the [independence (MG10)](course:OA-FLOW/OA-FLOW-MG#equation-mg10) of the Connes spectrum \(\Gamma\) from the weight, the formula [(MT25)](course:OA-FLOW/OA-FLOW-MT#equation-mt25) \(S(P)=\{0\}\cup\exp\Gamma\) for type III factors with separable predual, and the definition [(HC1)](course:OA-FLOW/OA-FLOW-HC#equation-hc1) of type III\(_1\) as \(S(P)=[0,\infty)\); [Corollaries 4.2 and 7.4 of Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#4-commutants-of-semifinite-algebras) (\(P\) and \(P'\) have the same type; semifinite normal traces on a semifinite factor are proportional); Theorem 5.2 of [An injective subalgebra with the same core commutant](course:relative-bicentralizers-and-core-commutants/an-injective-subalgebra-with-the-same-core-commutant#5-the-theorem); [Theorem 1.6 of Uniqueness of the injective II₁ factor](course:injective-factors/uniqueness-of-the-injective-ii1-factor#1-the-setting-and-the-main-theorem) and its model of \(R\) as the closure of \(\bigcup_kM_2(\mathbb C)^{\otimes k}\); [injectivity as a norm-one projection](course:injective-factors/injective-von-neumann-algebras#2-injectivity-as-a-norm-one-projection); the facts on projections of countably decomposable type III factors, (B8) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons) (every nonzero projection is equivalent to \(1\)); Proposition 7.1 and [Corollary 11.5(2)](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#11-the-commutation-theorem-and-its-consequences) of the tensor product lesson; and [Kaplansky's density theorem](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07).

## 1. A fixed tensor factor

Fix
\[
\lambda=e^{-1},\qquad\mu=e^{-\sqrt2}.
\]
For \(0<\nu<1\) let \(\rho_\nu\) be the state of \(M_2(\mathbb C)\) with density \(h_\nu=(1+\nu)^{-1}\operatorname{diag}(1,\nu)\). Choose types \(\nu_1,\nu_2,\dots\in\{\lambda,\mu\}\), each occurring infinitely often. Site \(k\) is \(M_2(\mathbb C)\) acting by left multiplication on the Hilbert–Schmidt space \(M_2(\mathbb C)\) with the unit vector \(h_{\nu_k}^{1/2}\). Let \(K\) be the infinite tensor product of these Hilbert spaces along the unit vectors \(h_{\nu_k}^{1/2}\), \(\Omega_\rho\) the product vector, \(D_n\) the algebra of the first \(n\) sites (a copy of \(M_{2^n}(\mathbb C)\)), and \(D=(\bigcup_nD_n)''\). The vector state of \(\Omega_\rho\) on \(D\) is the product state \(\rho\).

The vector \(\Omega_\rho\) is cyclic for \(D\), because \(\{xh^{1/2}_\nu:x\in M_2(\mathbb C)\}\) is the whole site space, and likewise cyclic for the right multiplications on the sites, which commute with \(D\). So \(\Omega_\rho\) is cyclic and separating for \(D\), and \(\rho\) is a faithful normal state. With \(J\) the modular conjugation of \((D,\Omega_\rho)\), \(D'=JDJ\) is generated by the increasing finite-dimensional unital \(*\)-algebras \(JD_nJ\). On \(D_n\) the modular group of \(\rho\) is \(\operatorname{Ad}h_{(n)}^{it}\), with \(h_{(n)}=h_{\nu_1}\otimes\cdots\otimes h_{\nu_n}\), by the KMS characterization; for instance the off-diagonal matrix unit \(e_{12}\) at a site of type \(\nu\) satisfies
\[
\begin{aligned}
\sigma^\rho_t(e_{12})&=\nu^{-it}e_{12}\\
&=e^{-it\log\nu}e_{12}.\quad(1.1)
\end{aligned}
\]

**Lemma 1.1.** \(D_\rho'\cap D=\mathbb C1\). In particular \(D\) is a factor.

**Proof.** For two sites of the same type, the unitary of \(D_n\) exchanging them preserves \(\rho\), so it lies in the centralizer \(D_\rho\). Let \(x\in D_\rho'\cap D\) and \(a\in D_m\). By Kaplansky's density theorem choose \(x_j\in\bigcup_nD_n\) with \(\|x_j\|\le\|x\|\) and \(\|(x-x_j)\Omega_\rho\|\to0\); say \(x_j\in D_{n_j}\). A product \(w_j\) of exchanges of sites of equal type moves the first \(m\) sites to sites beyond \(n_j\); it lies in \(D_\rho\), so it commutes with \(x\) and preserves \(\rho\). For \(a_j=w_jaw_j^*\),
\[
\begin{gathered}
\rho(a_jx)=\rho(w_jaxw_j^*)=\rho(ax),\\
\rho(a_jx_j)=\rho(a)\rho(x_j),
\end{gathered}
\]
the second because \(a_j\) and \(x_j\) sit on disjoint sites of a product state. Also \(|\rho(a_jx)-\rho(a_jx_j)|\)\(\le\rho(aa^*)^{1/2}\|(x-x_j)\Omega_\rho\|\to0\) and \(\rho(x_j)\to\rho(x)\). Hence \(\rho(ax)=\rho(a)\rho(x)\), that is, \((x-\rho(x)1)\Omega_\rho\) is orthogonal to the dense set \(\bigcup_mD_m\Omega_\rho\). Since \(\Omega_\rho\) is separating, \(x=\rho(x)1\). \(\square\)

## 2. Continuous cores and type III₁

Let \(P\) be a von Neumann algebra on a Hilbert space \(H_P\), with a faithful normal state \(\psi\). On \(L^2(\mathbb R,H_P)\) put
\[
\begin{gathered}
(\pi(x)\xi)(t)=\sigma^\psi_{-t}(x)\xi(t),\\
(\lambda_s\xi)(t)=\xi(t-s),
\end{gathered}
\]
and let \(C(P,\psi)=(\pi(P)\cup\{\lambda_s\})''\), the *continuous core* (the crossed product by the modular group). From the course on flows of weights we use: \(C(P,\psi)\) carries a faithful normal semifinite trace \(\tau\) with \(\tau\circ\theta_s=e^{-s}\tau\), where the dual action \(\theta_s\) fixes \(\pi(P)\) and multiplies \(\lambda_t\) by \(e^{-ist}\) [core trace]; if \(P\) is a factor, \(C(P,\psi)\) is a factor exactly when the Connes spectrum \(\Gamma(\sigma^\psi)\) is \(\mathbb R\) [(F3)]; \(\Gamma(\sigma^\psi)\) does not depend on the faithful normal semifinite weight used [(MG10)]; and the Connes spectrum of the trivial action is \(\{0\}\), since it is contained in the spectrum.

**Lemma 2.1** (factorial cores). Let \(P\) be a factor with separable predual and \(\psi\) a faithful normal state. Then \(C(P,\psi)\) is a factor exactly when \(P\) is of type III\(_1\), and then \(C(P,\psi)\) is a factor of type II\(_\infty\).

**Proof.** If \(P\) is semifinite, with a faithful normal semifinite trace \(\tau_P\), then \(\sigma^{\tau_P}\) is trivial, so \(\Gamma(\sigma^\psi)=\Gamma(\sigma^{\tau_P})=\{0\}\) and \(C(P,\psi)\) is not a factor. If \(P\) is of type III, (MT25) gives \(S(P)=\{0\}\cup\exp\Gamma(\sigma^\psi)\), so \(\Gamma(\sigma^\psi)=\mathbb R\) exactly when \(S(P)=[0,\infty)\), that is, when \(P\) is of type III\(_1\).

Let \(C=C(P,\psi)\) be a factor, with the trace \(\tau\) scaled by \(\theta\). It is semifinite. If \(C\) were finite, \(\tau\) would be a multiple of the finite trace of \(C\) (Corollary 7.4 of the integration lesson), so \(\tau(1)<\infty\), and \(\tau(1)=\tau(\theta_s(1))=e^{-s}\tau(1)\) would force \(\tau(1)=0\). If \(C\) were of type I, it would have a minimal projection \(e\) with \(0<\tau(e)<\infty\); \(\theta_s(e)\) is again minimal, and minimal projections of a type I factor are equivalent, hence have equal trace, contradicting \(\tau(\theta_s(e))=e^{-s}\tau(e)\) for \(s\ne0\). So \(C\) is of type II\(_\infty\). \(\square\)

**Proposition 2.2.** For every factor \(A\) with separable predual, \(A\bar\otimes D\) is a factor of type III\(_1\).

**Proof.** Let \(\psi_A\) be a faithful normal state of \(A\), \(P=A\bar\otimes D\) and \(\psi=\psi_A\otimes\rho\). By the KMS characterization, \(\sigma^\psi\) acts on \(A\otimes1\) as \(\sigma^{\psi_A}\otimes\mathrm{id}\) and on \(1\otimes D\) as \(\mathrm{id}\otimes\sigma^\rho\). Let \(Z\) be central in \(C=C(P,\psi)\), represented on \(L^2(\mathbb R,H_P)\).

*A field of the algebra.* The Fourier transform in \(t\) turns \(\lambda_s\) into multiplication by \(e^{-is\zeta}\); these functions generate \(L^\infty(\mathbb R)\), whose commutant on \(L^2(\mathbb R,H_P)\) consists of the decomposable operators, multiplication by bounded measurable fields \(\zeta\mapsto a(\zeta)\in B(H_P)\) (Proposition 7.1 of the tensor product lesson). So \(Z\) is decomposable. The constant operators \(1\otimes P'\) commute with \(C\), hence with \(Z\), so \(a(\zeta)\in P\) almost everywhere. For \(y\) in \(1\otimes D_\rho\), \(\pi(y)\) is the constant operator \(y\), because \(\sigma^\psi\) fixes \(y\); so \(a(\zeta)\) commutes with \(1\otimes D_\rho\). By Proposition 7.1 and Corollary 11.5(2) of the tensor product lesson and Lemma 1.1,
\[
\begin{aligned}
a(\zeta)&\in(A\bar\otimes D)\cap\bigl(B(H_A)\bar\otimes D_\rho'\bigr)\\
&=A\bar\otimes(D\cap D_\rho')=A\otimes1 .
\end{aligned}
\]

*Invariance under a dense group.* Let \(e_{12}\) be the matrix unit at a site of type \(\nu\in\{\lambda,\mu\}\), as an element \(1\otimes e_{12}\) of \(P\). By (1.1), \(\pi(1\otimes e_{12})\) is \(1\otimes e_{12}\) times multiplication by \(e^{it\log\nu}\), which after Fourier transform is \(1\otimes e_{12}\) composed with the translation of the frequency by \(\log\nu\). Commutation of \(Z\) with it, and the fact that \(a(\zeta)\in A\otimes1\) commutes with \(1\otimes e_{12}\), give \((a(\zeta)-a(\zeta-\log\nu))(1\otimes e_{12})=0\), hence
\[
\begin{gathered}
a(\zeta)=a(\zeta-\log\lambda)=a(\zeta-\log\mu)\\
\text{almost everywhere}.
\end{gathered}
\]
The group generated by \(\log\lambda=-1\) and \(\log\mu=-\sqrt2\) is dense in \(\mathbb R\), since \(\sqrt2\) is irrational. Test the field on a countable dense set of pairs of vectors: each coefficient is a bounded function invariant under a dense group of translations; translation is continuous in \(L^1_{\rm loc}\), so the coefficient is invariant under all translations, and convolution with an approximate identity shows that it is almost everywhere constant. Hence \(Z\) is a constant \(a_0\otimes1\), \(a_0\in A\).

*Conclusion.* \(Z\) commutes with \(\pi(x\otimes1)\), which is the field \(t\mapsto\sigma^{\psi_A}_{-t}(x)\otimes1\); by strong continuity of the modular group, \(a_0\) commutes with \(x\). So \(a_0\in A\cap A'=\mathbb C1\), and \(C\) is a factor. Lemma 2.1 shows that \(P\) is of type III\(_1\). \(\square\)

## 3. Irreducible hyperfinite subfactors in type III₁ factors

**Proposition 3.1.** Let \(P\) be a type III\(_1\) factor with separable predual, acting on a separable Hilbert space. There are a faithful normal state \(\varphi\) on \(P\) and a hyperfinite II\(_1\) factor \(R=(\bigcup_jQ_j)''\), with increasing full matrix subalgebras \(Q_j\cong M_{2^j}(\mathbb C)\), such that
\[
R\subseteq P_\varphi,\qquad R'\cap P=\mathbb C1 .
\]

**Proof.** Theorem 5.2 of the lesson on core commutants, applied to the inclusion \(P\subseteq P\) with the identity expectation, gives a faithful normal state \(\varphi\) and an approximately finite-dimensional, hence injective, subalgebra \(P_0\subseteq P\) with \(\sigma^\varphi_t(P_0)=P_0\) and \((P_0)_\varphi'\cap P=\mathbb C1\), where \((P_0)_\varphi\) is the centralizer of \(\varphi|_{P_0}\). Put \(R=(P_0)_\varphi\). By the modular expectation theorem, the modular group of \(\varphi|_{P_0}\) is the restriction of \(\sigma^\varphi\), so by the fixed-point criterion \(R=P_0\cap P_\varphi\subseteq P_\varphi\).

The center of \(R\) lies in \(R'\cap P=\mathbb C1\), so \(R\) is a factor, and \(\varphi|_R\) is a faithful normal tracial state, so \(R\) is finite. It is not finite-dimensional: if it were, with matrix units \(e_{ij}\), the elements \(\sum_ie_{i1}ye_{1i}\), \(y\in e_{11}Pe_{11}\), would form a copy of the corner \(e_{11}Pe_{11}\) inside \(R'\cap P\), and a corner of a type III factor is not one-dimensional. So \(R\) is a II\(_1\) factor. It is injective: the modular expectation theorem, applied to \(\varphi|_{P_0}\) and its fixed-point algebra \(R\), gives a faithful normal conditional expectation \(P_0\to R\), and composing it with a norm-one projection of \(B(H)\) onto \(P_0\) gives a norm-one projection onto \(R\). By Theorem 1.6 of the uniqueness lesson, \(R\) is isomorphic to the closure of \(\bigcup_kM_2(\mathbb C)^{\otimes k}\); the isomorphism is normal, and the images \(Q_j\) of the algebras \(M_2(\mathbb C)^{\otimes j}\) generate \(R\). \(\square\)

## 4. Normal representations of type III factors

**Lemma 4.1.** Let \(P\) be a type III factor with separable predual and \(\pi\) a nonzero normal representation of \(P\) on a separable Hilbert space \(H\). Then \(\pi\) is unitarily equivalent to the standard representation. Consequently, for every faithful normal state \(\varphi\) of \(P\) there is a unit vector \(\Omega\in H\), cyclic and separating for \(\pi(P)\), with \(\varphi=\langle\pi(\cdot)\Omega,\Omega\rangle\).

**Proof.** Let \(P\) act standardly on \(L^2(P)\) with conjugation \(J\) and positive cone \(\mathcal P\). By Zorn's lemma \(H\) is an orthogonal sum of cyclic subspaces \([\pi(P)\xi_k]\), countably many since \(H\) is separable. For each \(k\), the normal positive functional \(\langle\pi(\cdot)\xi_k,\xi_k\rangle\) is \(\omega_{\eta_k}\) for a cone vector \(\eta_k\in\mathcal P\), and \(\pi(x)\xi_k\mapsto x\eta_k\) extends to a unitary from \([\pi(P)\xi_k]\) onto \([P\eta_k]\subseteq L^2(P)\) intertwining the actions. So \(\pi\) is equivalent to a subrepresentation of \(L^2(P)\otimes\ell^2\). The commutant \(P'=JPJ\) is a countably decomposable type III factor, hence properly infinite; as in Section 4 of [Close operator algebras](close-operator-algebras.md) it contains isometries \(s_k\) with orthogonal ranges summing to \(1\), and \(V(\xi\otimes\delta_k)=s_k\xi\) is a unitary from \(L^2(P)\otimes\ell^2\) onto \(L^2(P)\) with \(V(x\otimes1)=xV\). Hence \(\pi\) is equivalent to the subrepresentation on \(qL^2(P)\) for a nonzero projection \(q\in P'\). In \(P'\), \(q\) is equivalent to \(1\): an isometry \(w\in P'\) with \(ww^*=q\) is a unitary from \(L^2(P)\) onto \(qL^2(P)\) intertwining the actions.

For a faithful normal state \(\varphi\), let \(\xi_\varphi\in\mathcal P\) be its cone vector. It is separating because \(\varphi\) is faithful. Since \(J\xi_\varphi=\xi_\varphi\) and \(JPJ=P'\), the closures of \(P\xi_\varphi\) and \(P'\xi_\varphi\) are exchanged by \(J\); a vector separating for \(P\) is cyclic for \(P'\), so \(\xi_\varphi\) is also cyclic for \(P\). Transport \(\xi_\varphi\) to \(H\). \(\square\)

## 5. Prepared pairs

**Definition 5.1** (prepared pair). A *prepared pair* consists of type III\(_1\) factors \(M,N\subseteq B(H)\) on a separable Hilbert space, a unit vector \(\Omega\in H\) cyclic and separating for both, and a hyperfinite II\(_1\) factor \(R=(\bigcup_jR_j)''\subseteq M\cap N\), generated by increasing full matrix subalgebras \(R_j\), such that:

1. \(R'\cap M=R'\cap N=\mathbb C1\);
2. the vector state \(\varphi=\langle\cdot\,\Omega,\Omega\rangle\) centralizes \(R\) on \(M\) and on \(N\): \(R\subseteq M_\varphi\cap N_\varphi\);
3. \(J_MrJ_M=J_NrJ_N\) for every \(r\in R\), where \(J_M,J_N\) are the modular conjugations of \((M,\Omega)\) and \((N,\Omega)\).

If \(\varphi\) centralizes \(R\) on \(M\) and \(r\in R\), then \(r^*\) is fixed by \(\sigma^\varphi\), so \(\Delta_M^{it}r^*\Omega=r^*\Omega\) for all \(t\); hence \(r^*\Omega\) lies in the kernel of \(\log\Delta_M\) and \(\Delta_M^{1/2}r^*\Omega=r^*\Omega\). Since \(S_M(r^*\Omega)=r\Omega\), \(S_M=J_M\Delta_M^{1/2}\) and \(J_M\Omega=\Omega\),
\[
\begin{gathered}
r\Omega=J_Mr^*\Omega=J_Mr^*J_M\Omega\\
(r\in R).\quad(5.1)
\end{gathered}
\]

**Proposition 5.2** (preparing an infinite pair). Let \(M_0,N_0\subseteq B(H)\) be factors on a separable Hilbert space, \(M_0\) infinite, with \(d(M_0,N_0)<t<4\cdot10^{-9}\). There are unitaries \(u_0\in B(H)\) and \(v\in B(H\otimes K)\) with \(\|u_0-1\|+\|v-1\|\le3\cdot10^7t\) such that
\[
\begin{gathered}
M=M_0\bar\otimes D,\\
N=v\bigl((u_0N_0u_0^*)\bar\otimes D\bigr)v^*
\end{gathered}
\]
form a prepared pair and \(d_{\rm cb}(M,N)\le6\cdot10^7t\).

**Proof.** *A common infinite family of isometries.* \(M_0\) has separable predual, so it is countably decomposable, and an infinite factor is properly infinite; it contains an infinite family of isometries, which generates a copy \(S_0\) of \(B(\ell^2)\), an injective algebra. Since \(S_0\subset_tN_0\), Christensen's theorem gives a unitary \(u_0\) with \(\|u_0-1\|\le150t\) and \(S_0\subseteq u_0N_0u_0^*\). In particular \(N_0\) is infinite. By Lemma 1.5 and Corollary 4.3 of [Close operator algebras](close-operator-algebras.md), \(d_{\rm cb}(M_0,u_0N_0u_0^*)\)\(=d(M_0,u_0N_0u_0^*)<301t\). By Lemma 5.1(2) of the averaging lesson, applicable since \(D'\) is generated by the increasing algebras \(JD_nJ\),
\[
\begin{gathered}
d_{\rm cb}(M,N_1)<301t,\\
N_1=(u_0N_0u_0^*)\bar\otimes D .
\end{gathered}
\]
Both \(M\) and \(N_1\) are type III\(_1\) factors by Proposition 2.2.

*The subfactor and the vector.* Proposition 3.1 gives a faithful normal state \(\varphi\) of \(M\) and \(R=(\bigcup_jR_j)''\subseteq M_\varphi\) with \(R'\cap M=\mathbb C1\). By Lemma 4.1 there is a unit vector \(\Omega\in H\otimes K\), cyclic and separating for \(M\), with \(\varphi=\langle\cdot\,\Omega,\Omega\rangle\) on \(M\); no algebra is moved. By (5.1), \(r\Omega=J_Mr^*J_M\Omega\) for \(r\in R\). Put \(S=J_MRJ_M\subseteq M'\).

*Moving \(N_1\).* Since \(R\subseteq M\), \(R\subset_{301t}N_1\), and Christensen's theorem gives \(v_1\) with \(v_1Rv_1^*\subseteq N_1\) and \(\|v_1-1\|\le45150t\). Put \(N_2=v_1^*N_1v_1\supseteq R\); then \(d_{\rm cb}(M,N_2)\le90601t\), and Corollary 3.2 of [Close operator algebras](close-operator-algebras.md) gives \(d(M',N_2')\le181202t\). The algebra \(S\) is generated by the increasing finite-dimensional algebras \(J_MR_jJ_M\), so it is injective. So \(S\subset_{181203t}N_2'\), and Christensen's theorem gives a unitary \(v_2\in(S\cup N_2')''\) with \(v_2Sv_2^*\subseteq N_2'\) and \(\|v_2-1\|\le150\cdot181203t\). Both \(S\) and \(N_2'\) commute with \(R\), so \(v_2\in R'\). Put \(N=v_2^*N_2v_2\) and \(v=v_2^*v_1^*\). Then \(R\subseteq N\), \(S\subseteq N'\), \(\|v-1\|\le27225600t\), and
\[
\begin{aligned}
d_{\rm cb}(M,N)&\le90601t+2\cdot150\cdot181203t\\
&\le6\cdot10^7t .
\end{aligned}
\]
Also \(d(M',N')\le2d_{\rm cb}(M,N)<1/2\) and \(d(M,N)<1/2\), by the bound on \(t\).

*Irreducibility.* For \(x\in M\) let \(E_j(x)=\int_{\mathcal U(R_j)}uxu^*\,du\). Every weak operator cluster point of \(E_j(x)\) commutes with all \(R_j\), hence lies in \(R'\cap M=\mathbb C1\), and \(\varphi(E_j(x))=\varphi(x)\) because \(R\subseteq M_\varphi\); so \(E_j(x)\to\varphi(x)1\) weakly. Let \(p\in R'\cap N\) be a projection and choose \(x\in M_1\) with \(\|p-x\|<1/2\). Since \(E_j(p)=p\), \(\|E_j(x)-p\|\le\|x-p\|\), and in the limit \(\|\varphi(x)1-p\|<1/2\). A projection other than \(0,1\) has distance \(1/2\) from the scalars, so \(p\in\{0,1\}\) and \(R'\cap N=\mathbb C1\). The same argument in the commutants gives \(S'\cap N'=\mathbb C1\). It uses \(S'\cap M'=J_M(R'\cap M)J_M=\mathbb C1\) and the invariance of the vector state on \(M'\) under the unitaries \(s=J_MuJ_M\) of \(S\): by (5.1), \(s^*\Omega=u\Omega\), so \(\langle sx's^*\Omega,\Omega\rangle=\langle u^*x'u\Omega,\Omega\rangle=\langle x'\Omega,\Omega\rangle\) for \(x'\in M'\).

*The common vector.* Let \(p\) project onto the closure of \(N'\Omega\); then \(p\in N\). For \(r\in R\) and \(x'\in N'\), \(rx'\Omega=x'r\Omega=x'(J_Mr^*J_M)\Omega\in N'\Omega\), because \(J_Mr^*J_M\in S\subseteq N'\). So \(p\) commutes with \(R\), \(p\in R'\cap N\), and \(p=1\): \(\Omega\) is cyclic for \(N'\), hence separating for \(N\). Similarly the projection onto the closure of \(N\Omega\) lies in \(N'\) and commutes with \(S\), since \((J_MrJ_M)x\Omega=x\,r^*\Omega\) for \(x\in N\); it is \(1\), and \(\Omega\) is cyclic for \(N\).

*The centralizer and the right actions.* For a unitary \(u\in R\) and \(x\in N\), \(u^*\Omega=J_MuJ_M\Omega\) with \(J_MuJ_M\) a unitary of \(N'\), so \(\langle uxu^*\Omega,\Omega\rangle\)\(=\langle x\,J_MuJ_M\Omega,J_MuJ_M\Omega\rangle\)\(=\langle x\Omega,\Omega\rangle\). Thus \(\varphi\circ\operatorname{Ad}u=\varphi\) on \(N\), and \(R\subseteq N_\varphi\). By (5.1) for \(N\), \(J_NrJ_N\Omega=r^*\Omega=J_MrJ_M\Omega\); both operators lie in \(N'\), and \(\Omega\) is separating for \(N'\), so \(J_NrJ_N=J_MrJ_M\). Finally \(N=vN_1v^*\) is a type III\(_1\) factor. All conditions of Definition 5.1 hold. \(\square\)

## 6. Exercises

**Exercise 6.1.** Show that the subgroup of \(\mathbb R\) generated by \(1\) and \(\sqrt2\) is dense.

**Exercise 6.2.** Compute the modular operator of \((M_2(\mathbb C),\rho_\nu)\) on the Hilbert–Schmidt space with vector \(h_\nu^{1/2}\), and check (1.1).

**Exercise 6.3.** Show that a unitary \(u\) with \(\varphi(uxu^*)=\varphi(x)\) for all \(x\) lies in the centralizer \(P_\varphi\).

**Exercise 6.4.** In the proof of Lemma 4.1, check that \(V(\xi\otimes\delta_k)=s_k\xi\) is unitary and intertwines \(x\otimes1\) with \(x\).

**Exercise 6.5.** Let \(P\) be a factor and \(e\ne0\) a projection. Show that the corner \(ePe\) is one-dimensional exactly when \(e\) is a minimal projection, and conclude that corners of type III factors are not one-dimensional.

## 7. Solutions

**Solution 6.1.** A subgroup of \(\mathbb R\) is dense or of the form \(c\mathbb Z\). If \(1=mc\) and \(\sqrt2=m'c\) with integers \(m,m'\), then \(\sqrt2=m'/m\) is rational.

**Solution 6.2.** \(S(xh^{1/2})=x^*h^{1/2}=h^{1/2}\,(h^{-1/2}x^*h^{1/2})\); one checks \(J\xi=\xi^*\) and \(\Delta\xi=h\xi h^{-1}\). Then \(\sigma_t(x)=h^{it}xh^{-it}\), and \(h^{it}e_{12}h^{-it}=1^{it}\nu^{-it}e_{12}\).

**Solution 6.3.** Replace \(x\) by \(xu\): \(\varphi(ux)=\varphi(uxuu^*)=\varphi(xu)\).

**Solution 6.4.** \(\langle V(\xi\otimes\delta_k),V(\eta\otimes\delta_l)\rangle\)\(=\langle s_l^*s_k\xi,\eta\rangle=\delta_{kl}\langle\xi,\eta\rangle\), so \(V\) is isometric, and its range contains \(s_ks_k^*L^2(P)\) for every \(k\), whose sum is \(L^2(P)\). Since \(s_k\in P'\), \(V(x\xi\otimes\delta_k)=s_kx\xi=xs_k\xi\).

**Solution 6.5.** If \(ePe=\mathbb Ce\), then every subprojection of \(e\) in \(P\) is \(0\) or \(e\), so \(e\) is minimal; conversely a minimal projection of a factor has \(ePe=\mathbb Ce\). A type III factor has no minimal projections, since a minimal projection is abelian and finite.

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
