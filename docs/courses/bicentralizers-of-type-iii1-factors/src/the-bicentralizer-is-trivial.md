# The bicentralizer of a type III₁ factor is trivial

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Connes asked whether the bicentralizer of every faithful normal state on a type III₁ factor with separable predual is trivial. This lesson proves that it is (Theorem 6.1). The argument assembles the earlier lessons. Suppose the bicentralizer \(\mathrm B\) of \(\varphi\) is not trivial. Then \(\mathrm B\) is its own bicentralizer and the restricted state has trivial centralizer; we show first that this forces \(\mathrm B\) to be a factor of type III₁ (Theorem 1.1). The bicentralizer flow of \(\mathrm B\) is trivial by the spectral rigidity theorem [OpenAI-recovery], so the sequences that scale the state by a factor \(\mu\) asymptotically commute with all of \(\mathrm B\): \(\mathrm B\) has *central eigen-isometries*. Marrakchi's method [Marrakchi, Sections 3, 4 and 6] turns such sequences into the elements required by Haagerup's criterion [AHHM, Theorem 7.2], which then makes the bicentralizer of \(\mathrm B\), that is \(\mathrm B\) itself, trivial. Marrakchi applied the method to factors absorbing the Araki–Woods factor \(R_\infty\) tensorially; here the central sequences come directly from the trivial flow, so no tensor absorption theorem is needed. The theorem is the application in [OpenAI-recovery] of its rigidity theorem; Houdayer and Marrakchi have announced an independent proof without the separability assumption [HM26].

We use all earlier lessons of this course: [Asymptotic centralizers of type III₁ factors](asymptotic-centralizers-of-type-iii1-factors.md) (Lemma 1.3, Proposition 4.1), [The bicentralizer](the-bicentralizer.md) (Proposition 1.3, Theorem 3.1), [The bicentralizer flow](the-bicentralizer-flow.md) (Corollary 3.2), [Spectral intertwining rigidity](spectral-intertwining-rigidity.md) (Lemma 3.4, Corollary 3.6), [Haagerup's criterion for a trivial bicentralizer](haagerups-criterion-for-a-trivial-bicentralizer.md) (Definition 1.1, Theorem 5.2) and [Strongly invariant states and approximate eigenstates](strongly-invariant-states.md) (Theorem 3.5, Lemma 4.2). Further inputs: the Connes spectrum \(\Gamma\), its definition (CS3) and the subgroup theorem CS-4 in [The real Connes spectrum](course:OA-FLOW/OA-FLOW-CS#OA-FLOW.CS.0); the identity (MG6), the corner restriction (MG9), the independence (MG10) of \(\Gamma\) from the weight, and the triviality of the modular group of a trace, in [The full weight spectral identity](course:OA-FLOW/OA-FLOW-MG#OA-FLOW.MG.1); the formula (MT25) \(S(M)=\{0\}\cup\exp\Gamma\) for type III factors with separable predual in [Zero in every modular spectrum and the type III spectral trichotomy](course:OA-FLOW/OA-FLOW-MT#OA-FLOW.MT.6); the definition of type III₁ and the Connes–Størmer theorem (HC1) in [Approximate unitary homogeneity of normal states](course:OA-FLOW/OA-FLOW-HC#equation-hc1); the center-valued trace of a finite von Neumann algebra in [Projection comparison and normal center-valued traces](course:OA-APPROX/projection-comparison-and-finite-traces#constructing-the-normal-center-valued-trace); the standard form facts (B3), (B4), (B6), (B8) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons) and CR-4, CR-6 of [All projection corners and canonical positive-functional vectors](course:OA-FLOW/OA-FLOW-CR#OA-FLOW.CR.4); the Tomita theorem for a faithful normal state, (FS.1)–(FS.2) of [Modular time from a faithful normal state](course:OA-MOD/OA-MOD-FS); and Theorems 2.2, 4.4 and 5.1 of [Tensor products of C\*-algebras and the minimal norm](course:tensor-products-of-operator-algebras/tensor-products-of-c-star-algebras-and-the-minimal-norm#5-factors-and-simple-algebras). A factor is of type III when it has no nonzero finite projection, and of type III₁ when moreover the intersection \(S(M)\) of the spectra of the modular operators of all faithful normal semifinite weights is \([0,\infty)\).

## 1. A trivial centralizer forces type III1

**Theorem 1.1.** Let \(B\ne\mathbb C1\) be a von Neumann algebra with separable predual and \(\psi\) a faithful normal state on \(B\) with \(B_\psi=\mathbb C1\). Then \(B\) is a factor of type III₁.

**Proof.** *Factor.* By (B6), \(B_\psi=\{x:\psi(xy)=\psi(yx)\ \forall y\}\), which contains the centre. So the centre is \(\mathbb C1\).

*The Connes spectrum is \(\mathbb R\).* The fixed-point algebra of \(\sigma^\psi\) is \(B_\psi=\mathbb C1\), whose only nonzero projection is \(1\); so by (CS3), \(\Gamma(\sigma^\psi)=\operatorname{Sp}(\sigma^\psi)\), and by CS-4 this is a closed subgroup of \(\mathbb R\). By (MG6), \(\operatorname{Sp}(\sigma^\psi)=\operatorname{Sp}(\log\Delta_\psi)\). A closed subgroup of \(\mathbb R\) is \(\{0\}\), \(a\mathbb Z\) with \(a>0\), or \(\mathbb R\). In the first two cases the spectrum of \(D=\log\Delta_\psi\) is countable; its spectral measure is carried by the spectrum, so \(H=\bigoplus_s1_{\{s\}}(D)H\) and \(D\) has pure point spectrum. Lemma 3.4 of the rigidity lesson then gives \(B=\mathbb C1\), which is excluded. Hence \(\Gamma(\sigma^\psi)=\mathbb R\).

*Type III.* Suppose \(e\in B\) is a nonzero finite projection. Then \(eBe\) is a finite von Neumann algebra ([Projections and types of von Neumann algebras, Lemma 6.2](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-09)) whose centre \(eZ(B)=\mathbb Ce\) is trivial (CR8 of [All projection corners](course:OA-FLOW/OA-FLOW-CR#OA-FLOW.CR.2)), so its center-valued trace is a faithful normal tracial state \(\tau\). If \(e\ne1\), let \(\chi=\psi((1-e)\,\cdot\,(1-e))/\psi(1-e)\) on \((1-e)B(1-e)\), and put
\[
\theta(y)=\tfrac12\tau(eye)+\tfrac12\chi\big((1-e)y(1-e)\big)\qquad(y\in B);
\]
if \(e=1\) put \(\theta=\tau\). Then \(\theta\) is a faithful normal state: \(\theta(y^*y)=0\) forces \(ye=0\) and \(y(1-e)=0\). Also \(\theta(ey)=\frac12\tau(eye)=\theta(ye)\), so \(e\in B_\theta\) by (B6), and \(e\) is fixed by \(\sigma^\theta\). By (MG9) the restriction of \(\sigma^\theta\) to \(eBe\) is the modular group of \(\theta|_{eBe}=\frac12\tau\), a trace, whose modular group is trivial (MG-5). The trivial action has spectrum \(\{0\}\), so by (CS3), \(\Gamma(\sigma^\theta)\subset\{0\}\). But \(B\) is a factor, and (MG10) gives \(\Gamma(\sigma^\theta)=\Gamma(\sigma^\psi)=\mathbb R\). This contradiction shows that \(B\) has no nonzero finite projection.

*Type III₁.* \(B\) is a type III factor with separable predual, so (MT25) gives \(S(B)=\{0\}\cup\exp\Gamma(\sigma^\psi)=[0,\infty)\). \(\square\)

Marrakchi and Vaes proved Theorem 1.1 through the continuous core [MV, Lemma 2.1]; the proof above uses the Connes spectrum instead.

## 2. Eigen-sequences: from the predual to vectors

Let \(N\) be a von Neumann algebra, \(\theta\) a faithful normal state, and \(\xi\) its vector in a standard form \((N,H,J,P)\); write \(\zeta d=Jd^*J\zeta\). For \(b\in N\) and \(\psi\in N_*\) we use \((b\psi)(y)=\psi(yb)\) and \((\psi b)(y)=\psi(by)\), as in the first lesson.

**Lemma 2.1.** Let \(\mu>0\) and let \((b_n)\) be a bounded sequence in \(N\) with \(\|b_n\theta-\mu\theta b_n\|\to0\). Then \(\|\xi b_n-\mu^{-1/2}b_n\xi\|\to0\).

**Proof.** Let \(\kappa=\mu^{-1}\), \(c=(1+\kappa)^{-1}\), \(R=M_2(N)\) acting on \(K=M_2(H)\) by left matrix multiplication, and
\[
\Theta(X)=c\,\theta(X_{11})+c\kappa\,\theta(X_{22}),\qquad\Omega=\begin{pmatrix}\sqrt c\,\xi&0\\0&\sqrt{c\kappa}\,\xi\end{pmatrix}.
\]
Then \(\Theta\) is a faithful normal state of \(R\) and \(\langle X\Omega,\Omega\rangle=\Theta(X)\); \(\Omega\) is cyclic and separating. The argument of (B4), applied to the cone vectors \(\sqrt c\,\xi\) and \(\sqrt{c\kappa}\,\xi\) of \(c\theta\) and \(c\kappa\theta\), shows that the modular conjugation of \(\Omega\) is \(\mathcal J\), \((\mathcal J\eta)_{ij}=J\eta_{ji}\). In the standard form of \(R\) built from \(\Theta\) on its GNS space \(K\) ([The positive cone of a standard representation, SF-05](course:OA-MOD/OA-MOD-SF#OA-MOD-SF-05)), whose conjugation is \(\mathcal J\), the vector of \(\Theta\) is \(\Omega\), and for a unitary \(U\in R\) the vector of \(U\Theta U^*\) is \(U\mathcal JU\mathcal J\Omega=U\Omega U^*\), where \(\zeta X=\mathcal JX^*\mathcal J\zeta\). By the inequalities (CR18) of CR-6 and by \(\|U\Omega U^*-\Omega\|=\|U\Omega-\Omega U\|\),
\[
\|U\Omega-\Omega U\|^2\le\|U\Theta U^*-\Theta\|=\|U\Theta-\Theta U\|\le2\|U\Omega-\Omega U\| .
\tag{2.1}
\]
Let \(\mathcal A\) (respectively \(\mathcal A_v\)) be the set of bounded sequences \((X_n)\) in \(R\) with \(\|X_n\Theta-\Theta X_n\|\to0\) (respectively \(\|X_n\Omega-\Omega X_n\|\to0\)). Both are unital \(C^*\)-subalgebras of \(\ell^\infty(R)\): for \(\mathcal A\) see Lemma 1.2 of the bicentralizer lesson; for \(\mathcal A_v\), \(XY\Omega-\Omega XY=X(Y\Omega-\Omega Y)+(X\Omega-\Omega X)Y\) and \(\mathcal J(X\Omega-\Omega X)=\Omega X^*-X^*\Omega\). By (2.1) they have the same unitaries, and a unital \(C^*\)-algebra is spanned by its unitaries; so \(\mathcal A=\mathcal A_v\).

Let \(W_n\in R\) have the single nonzero entry \((W_n)_{12}=b_n\). For \(X\in R\), \(\Theta(XW_n)=c\kappa\,\theta(X_{21}b_n)\) and \(\Theta(W_nX)=c\,\theta(b_nX_{21})\), so
\[
\|W_n\Theta-\Theta W_n\|=c\,\|\kappa\,b_n\theta-\theta b_n\|=c\kappa\,\|b_n\theta-\mu\theta b_n\|\to0 ,
\]
and \((W_n)\in\mathcal A=\mathcal A_v\). The only nonzero entry of \(W_n\Omega\) is \((1,2)\), equal to \(\sqrt{c\kappa}\,b_n\xi\); that of \(\Omega W_n=\mathcal JW_n^*\mathcal J\Omega\) is also \((1,2)\), equal to \(J(b_n^*\sqrt c\,\xi)=\sqrt c\,\xi b_n\). Hence \(\sqrt c\,\|\mu^{-1/2}b_n\xi-\xi b_n\|=\|W_n\Omega-\Omega W_n\|\to0\). \(\square\)

## 3. Central eigen-isometries

**Definition 3.1.** A countably decomposable factor \(N\) has *central eigen-isometries* if for every faithful normal state \(\theta\) on \(N\) and every \(\mu\ge1\) there is a sequence \((b_n)\) in \(N\) with
\[
\|b_n\|\le1,\qquad b_n^*b_n\to1\text{ strongly},\qquad\|b_n\theta-\mu\theta b_n\|\to0,\qquad b_na-ab_n\to0\ *\text{-strongly for every }a\in N .
\]

**Lemma 3.2.** Let \(N\) be a type III₁ factor with separable predual and \(\psi\) a faithful normal state. Suppose that for every \(\mu\ge1\) a sequence with the four properties of Definition 3.1 exists for \(\theta=\psi\). Then \(N\) has central eigen-isometries; indeed the same sequence works for every \(\theta\).

**Proof.** Let \(\theta\) be a faithful normal state, \((b_n)\) a sequence for \(\psi\) and \(\mu\), and \(\varepsilon>0\). By (HC1) there is a unitary \(u\) with \(\|u\psi u^*-\theta\|<\varepsilon\). Then
\[
\|b_n\theta-\mu\theta b_n\|\le(1+\mu)\varepsilon+\|b_n\,u\psi u^*-\mu\,u\psi u^*\,b_n\|,
\]
and \(b_n\,u\psi u^*-\mu\,u\psi u^*\,b_n=u\big(z_n\psi-\mu\psi z_n\big)u^*\) with \(z_n=u^*b_nu\). Write \(z_n=b_n+u^*(b_nu-ub_n)\). For \(w\in N\) and the vector \(\xi_\psi\) of \(\psi\), \(\|w\psi\|=\sup_{\|y\|\le1}|\langle w\xi_\psi,y^*\xi_\psi\rangle|\le\|w\xi_\psi\|\) and \(\|\psi w\|\le\|w^*\xi_\psi\|\). Since \(b_nu-ub_n\to0\) \(*\)-strongly, \(\limsup_n\|z_n\psi-\mu\psi z_n\|\le\limsup_n\|b_n\psi-\mu\psi b_n\|=0\). So \(\limsup_n\|b_n\theta-\mu\theta b_n\|\le(1+\mu)\varepsilon\) for every \(\varepsilon\). \(\square\)

**Proposition 3.3.** Let \(M\) be a type III₁ factor with separable predual, \(\varphi\) a faithful normal state, \(\mathrm B=\mathrm B(M,\varphi)\ne\mathbb C1\) and \(\psi=\varphi|_{\mathrm B}\). Then \(\mathrm B\) is a type III₁ factor with separable predual, \(\mathrm B(\mathrm B,\psi)=\mathrm B\), and \(\mathrm B\) has central eigen-isometries.

**Proof.** By Theorem 3.1 of the bicentralizer lesson, \(\mathrm B\) is a factor with separable predual, \(\psi\) is faithful with trivial centralizer, and \(\mathrm B(\mathrm B,\psi)=\mathrm B\). By Theorem 1.1 it is of type III₁. Let \(\mu\ge1\). Proposition 4.1 of the first lesson, applied to \((\mathrm B,\psi)\) with \(\lambda=\mu^{-1}\le1\) and \(m=1\), gives partial isometries \(v_n\in\mathrm B\) with \(\|v_n\psi-\mu^{-1}\psi v_n\|\to0\) and \(v_nv_n^*\to1\) \(*\)-strongly. By Corollary 3.2 of the flow lesson and Corollary 3.6 of the rigidity lesson (\(\beta^\varphi_{\mu^{-1}}=\mathrm{id}\)), \(v_na-av_n\to0\) \(*\)-strongly for every \(a\in\mathrm B\). Put \(b_n=v_n^*\). Then \(\|b_n\|\le1\), \(b_n^*b_n=v_nv_n^*\to1\), \(b_na-ab_n\to0\) \(*\)-strongly, and, taking adjoints of functionals (\(\|\omega^*\|=\|\omega\|\) with \(\omega^*(y)=\overline{\omega(y^*)}\)), \(\|b_n\psi-\mu\psi b_n\|=\mu\|v_n\psi-\mu^{-1}\psi v_n\|\to0\). Lemma 3.2 completes the proof. \(\square\)

## 4. Absorption

In this section \(N\) is a countably decomposable factor with central eigen-isometries, in standard form \((N,H,J,P)\); \(\theta\) is a faithful normal state with vector \(\xi\in P\), \(\Delta=\Delta_\theta\), and \(\rho(d)\zeta=\zeta d\), so \(\rho(N)=N'\). Let \(C\subset B(H)\) be the \(C^*\)-algebra generated by \(N\) and \(N'\); the products \(c\rho(d)\) span a dense \(*\)-subalgebra. By (FS.1), \(\xi d=\Delta^{1/2}d\xi\), \(J\log\Delta\,J=-\log\Delta\), and \(N\xi\) is a core for \(\Delta^{1/2}\), since \(S=J\Delta^{1/2}\) is the closure of \(d\xi\mapsto d^*\xi\). Let
\[
\mathcal C=\bigcap_{\varepsilon>0}\overline{\{\omega_{a\xi}:\ a\in N,\ \|a\xi\|=1,\ \|a\xi-\xi a\|\le\varepsilon\}}^{\,w^*}\subset S(B(H)).
\]

**Lemma 4.1.** Let \(\zeta\) be a unit vector in the domain of \(\log\Delta\) and \(\ell\in\mathbb R\) with \(\|(\log\Delta-\ell)\zeta\|\le\varepsilon_1\le\frac1{10}\), and let \(F\) be a finite subset of the unit ball of \(N\). There is \(a\in N\) with \(\|a\xi\|=1\), \(\|a\xi-\xi a\|\le15\varepsilon_1\), and \(|\omega_{a\xi}(c\rho(d))-\omega_\zeta(c\rho(d))|\le45\varepsilon_1\) for all \(c,d\in F\).

**Proof.** *Case \(\ell\ge0\).* Let \(\zeta'=1_{[\ell-1,\ell+1]}(\log\Delta)\zeta\). Then \(\|\zeta-\zeta'\|\le\varepsilon_1\), \(\zeta'\) is in the domain of \(\Delta^{1/2}\), and since \(|e^{t/2}-e^{\ell/2}|\le\frac12e^{(\ell+1)/2}|t-\ell|\) for \(|t-\ell|\le1\), \(\|(\Delta^{1/2}-e^{\ell/2})\zeta'\|\le\frac12e^{(\ell+1)/2}\varepsilon_1\). As \(N\xi\) is a core, choose \(y\in N\) with \(\|y\xi-\zeta'\|\le\varepsilon_1\) and \(\|\xi y-\Delta^{1/2}\zeta'\|=\|\Delta^{1/2}(y\xi-\zeta')\|\le\varepsilon_1\). Then \(\|y\xi-\zeta\|\le2\varepsilon_1\) and
\[
e^{-\ell/2}\|\xi y-e^{\ell/2}y\xi\|\le e^{-\ell/2}\varepsilon_1+\tfrac12e^{1/2}\varepsilon_1+\varepsilon_1\le3\varepsilon_1 .
\]
Let \(\mu=e^\ell\ge1\) and \((b_n)\) as in Definition 3.1 for \(\theta\) and \(\mu\). By Lemma 2.1, \(\|\xi b_n-\mu^{-1/2}b_n\xi\|\to0\). Put \(a_n=b_ny\). Since \((b_n\xi)y=b_n(\xi y)\) and \(\mu^{-1/2}e^{\ell/2}=1\),
\[
a_n\xi-\xi a_n=\mu^{-1/2}b_n\big(e^{\ell/2}y\xi-\xi y\big)-\big(\xi b_n-\mu^{-1/2}b_n\xi\big)y ,
\]
so \(\limsup_n\|a_n\xi-\xi a_n\|\le3\varepsilon_1\). Next, \(\rho(d)a_n\xi=b_n(y\xi d)\), so \(\omega_{a_n\xi}(c\rho(d))=\langle b_n^*cb_n(y\xi d),y\xi\rangle\). Since \(b_n^*cb_n-c=b_n^*(cb_n-b_nc)+(b_n^*b_n-1)c\to0\) weakly, \(\omega_{a_n\xi}(c\rho(d))\to\omega_{y\xi}(c\rho(d))\), and \(\|a_n\xi\|\to\|y\xi\|\in[1-2\varepsilon_1,1+2\varepsilon_1]\). Fix \(n\) so large that \(\|a_n\xi-\xi a_n\|\le4\varepsilon_1\), \(r=\|a_n\xi\|\in[1-3\varepsilon_1,1+3\varepsilon_1]\) and \(|\omega_{a_n\xi}(c\rho(d))-\omega_{y\xi}(c\rho(d))|\le\varepsilon_1\) for \(c,d\in F\), and put \(a=a_n/r\). Then \(\|a\xi-\xi a\|\le4\varepsilon_1/0.7\le6\varepsilon_1\). For vectors \(u,v\) and \(\|T\|\le1\), \(|\omega_u(T)-\omega_v(T)|\le(\|u\|+\|v\|)\|u-v\|\), and \(|\omega_{u/r}(T)-\omega_u(T)|\le|1-r^2|\) when \(\|u\|=r\). With \(T=c\rho(d)\), the three differences \(\omega_{a\xi}-\omega_{a_n\xi}\), \(\omega_{a_n\xi}-\omega_{y\xi}\), \(\omega_{y\xi}-\omega_\zeta\) are at most \(7\varepsilon_1\), \(\varepsilon_1\) and \(5\varepsilon_1\), so \(|\omega_{a\xi}(T)-\omega_\zeta(T)|\le13\varepsilon_1\).

*Case \(\ell<0\).* The vector \(J\zeta\) satisfies \(\|(\log\Delta+\ell)J\zeta\|=\|(\log\Delta-\ell)\zeta\|\le\varepsilon_1\), and \(\omega_{Jw}(c\rho(d))=\omega_w(d\rho(c))\) for every vector \(w\), because \(J\big(c\rho(d)\big)^*J=d\rho(c)\). The first case, applied to \(J\zeta\), \(-\ell\) and \(F\), gives \(\tilde a\) with \(\|\tilde a\xi\|=1\), \(\|\tilde a\xi-\xi\tilde a\|\le6\varepsilon_1\) and \(|\omega_{\tilde a\xi}(d\rho(c))-\omega_\zeta(c\rho(d))|\le13\varepsilon_1\). By (1.1) of Haagerup's criterion lesson, \(v=\tilde a^*\xi=J(\xi\tilde a)\), \(\|v\|=\|\xi\tilde a\|\in[1-6\varepsilon_1,1+6\varepsilon_1]\), and \(\|\tilde a^*\xi-\xi\tilde a^*\|=\|\tilde a\xi-\xi\tilde a\|\). Now \(\omega_v(c\rho(d))=\omega_{\xi\tilde a}(d\rho(c))\), which differs from \(\omega_{\tilde a\xi}(d\rho(c))\) by at most \((2+6\varepsilon_1)6\varepsilon_1\le16\varepsilon_1\). Put \(a=\tilde a^*/\|v\|\). Then \(\|a\xi-\xi a\|\le6\varepsilon_1/0.4=15\varepsilon_1\), and, as \(|1-\|v\|^2|\le16\varepsilon_1\), \(|\omega_{a\xi}(c\rho(d))-\omega_\zeta(c\rho(d))|\le16\varepsilon_1+16\varepsilon_1+13\varepsilon_1=45\varepsilon_1\). \(\square\)

**Lemma 4.2** (absorption; after [Marrakchi, Lemma 4.2]). For every \(\Psi_0\in\overline{\operatorname{conv}}\,\mathcal E(\log\Delta)\) there is \(\Psi'\in\overline{\operatorname{conv}}\,\mathcal C\) with \(\Psi'|_C=\Psi_0|_C\).

**Proof.** The set of \(\Psi_0\) with this property is convex, and it is weak\(^*\)-closed: if \(\Psi_\alpha\to\Psi_0\) with partners \(\Psi'_\alpha\), a weak\(^*\) cluster point of \((\Psi'_\alpha)\) is a partner of \(\Psi_0\). So it suffices to treat \(\Psi_0\in\mathcal E(\log\Delta)\), with unit vectors \(\zeta_i\) and reals \(\ell_i\) as in Definition 3.1 of the previous lesson. For a finite set \(F\) in the unit ball of \(N\) and \(\varepsilon\in(0,\frac1{10}]\), choose \(i\) with \(\|(\log\Delta-\ell_i)\zeta_i\|\le\varepsilon\) and \(|\omega_{\zeta_i}(c\rho(d))-\Psi_0(c\rho(d))|\le\varepsilon\) for \(c,d\in F\), and let \(a_{F,\varepsilon}\) be the element given by Lemma 4.1 for \(\zeta_i,\ell_i,F\) and \(\varepsilon_1=\varepsilon\). Order the pairs \((F,\varepsilon)\) by inclusion of \(F\) and decrease of \(\varepsilon\), and let \(\Psi'\) be a weak\(^*\) cluster point of \(\omega_{a_{F,\varepsilon}\xi}\). For each \(\varepsilon_0>0\), the vectors with \(15\varepsilon\le\varepsilon_0\) belong to the set defining \(\mathcal C\) at \(\varepsilon_0\), so \(\Psi'\in\mathcal C\). For \(c,d\) in the unit ball of \(N\), \(|\omega_{a_{F,\varepsilon}\xi}(c\rho(d))-\Psi_0(c\rho(d))|\le46\varepsilon\) once \(c,d\in F\); hence \(\Psi'(c\rho(d))=\Psi_0(c\rho(d))\), and \(\Psi'=\Psi_0\) on \(C\) by linearity and density. \(\square\)

## 5. Haagerup's condition from central eigen-isometries

**Theorem 5.1.** Let \(N\) be a countably decomposable factor of type III with central eigen-isometries. Then \(N\) satisfies Haagerup's condition with constant \(2\), and \(\mathrm B(N,\theta)=\mathbb C1\) for every faithful normal state \(\theta\) on \(N\).

**Proof.** Let \(\theta\) be a faithful normal state, \(\delta>0\), and \(x\in N\) with \(x\xi=\xi x^*\), \(\theta(x)=0\) and \(\theta(x^*x)=1\), in the notation of Section 4; by CR-4 these conditions mean the same in the GNS representation of \(\theta\).

*A binormal state.* By Theorem 5.1 of the tensor product lesson the product map \(N\odot N'\to B(H)\) is injective, so the norm of \(B(H)\) is a \(C^*\)-norm on \(N\odot N'\), and by Theorem 4.4 there it dominates the minimal norm. The product of the normal states \(\theta\) on \(N\) and \(\omega_\xi|_{N'}\) on \(N'\) is a state of \(N\otimes_{\min}N'\) (Theorem 2.2 there: it is a vector state in a tensor product of representations), so it extends by continuity to a state \(\Phi\) of \(C\) with
\[
\Phi(c\rho(d))=\theta(c)\,\langle\rho(d)\xi,\xi\rangle=\theta(c)\theta(d)\qquad(c,d\in N),
\]
using \(\langle\xi d,\xi\rangle=\langle J d^*\xi,\xi\rangle=\langle d\xi,\xi\rangle\). Its restrictions to \(N\) and \(N'\) are normal. With \(U_t=\Delta^{it}\), (FS.2) and \(J\Delta^{it}=\Delta^{it}J\) give \(U_tNU_t^*=N\) and \(U_t\rho(d)U_t^*=\rho(\sigma^\theta_t(d))\); since \(\theta\circ\sigma^\theta_t=\theta\), \(\Phi\) is invariant under \(\sigma_t=\operatorname{Ad}U_t\).

*Strong invariance.* Lemma 4.2 of the previous lesson gives a strongly \(\sigma\)-invariant state \(\Psi\) of \(B(H)\) extending \(\Phi\). With \(X=\log\Delta\), so that \(U_t=e^{itX}\), Theorem 3.5 there gives \(\Psi\in\overline{\operatorname{conv}}\,\mathcal E(\log\Delta)\). Lemma 4.2 gives \(\Psi'\in\overline{\operatorname{conv}}\,\mathcal C\) with \(\Psi'|_C=\Phi\).

*Evaluation.* Let \(T_1=(x-\rho(x^*))^*(x-\rho(x^*))\) and \(T_2=\rho(x^*)^*\rho(x^*)=\rho(x^*x)\), both in \(C\). Since \(\rho(x^*)^*=\rho(x)\) commutes with \(x\),
\[
T_1=x^*x-x^*\rho(x^*)-x\rho(x)+\rho(x^*x),\qquad\Phi(T_1)=1-\theta(x^*)^2-\theta(x)^2+1=2,\qquad\Phi(T_2)=1 .
\]
So \(\Psi'(T_1-T_2)=1\). The function \(\Phi''\mapsto\Phi''(T_1-T_2)\) is affine and weak\(^*\) continuous, so some \(\Phi''\in\mathcal C\) has \(\Phi''(T_1-T_2)>\frac34\). Let \(\varepsilon'>0\) with \(2\varepsilon'^2\le\delta\). By the definition of \(\mathcal C\) there is \(a\in N\) with \(\|a\xi\|=1\), \(\|a\xi-\xi a\|\le\varepsilon'\) and \(|\omega_{a\xi}(T_k)-\Phi''(T_k)|<\frac18\) for \(k=1,2\). Now \((x-\rho(x^*))a\xi=xa\xi-a\xi x^*=xa\xi-ax\xi\), because \(\xi x^*=x\xi\), and \(\rho(x^*)a\xi=a\xi x^*=ax\xi\). Hence
\[
\|xa-ax\|_\theta^2-\|ax\|_\theta^2=\omega_{a\xi}(T_1)-\omega_{a\xi}(T_2)>\tfrac12 .
\]
Therefore \(\|a\|_\theta^2+\|ax\|_\theta^2=1+\|ax\|_\theta^2<1+2\|ax\|_\theta^2<2\|xa-ax\|_\theta^2\), and \(\|a\xi-\xi a\|^2\le\varepsilon'^2<2\varepsilon'^2\|xa-ax\|_\theta^2\le\delta\|xa-ax\|_\theta^2\). This is Haagerup's condition with constant \(2\). Theorem 5.2 of Haagerup's criterion lesson applies, since \(N\) is a countably decomposable factor of type III. \(\square\)

## 6. The bicentralizer theorem

**Theorem 6.1.** Let \(M\) be a factor of type III₁ with separable predual. Then \(\mathrm B(M,\varphi)=\mathbb C1\) for every faithful normal state \(\varphi\) on \(M\).

**Proof.** Suppose \(\mathrm B=\mathrm B(M,\varphi)\ne\mathbb C1\) and let \(\psi=\varphi|_{\mathrm B}\). By Proposition 3.3, \(\mathrm B\) is a type III₁ factor with separable predual, hence countably decomposable and of type III, with central eigen-isometries, and \(\mathrm B(\mathrm B,\psi)=\mathrm B\). Theorem 5.1 gives \(\mathrm B(\mathrm B,\psi)=\mathbb C1\), so \(\mathrm B=\mathbb C1\), a contradiction. \(\square\)

**Corollary 6.2.** Let \(M\) be a factor of type III₁ with separable predual, \(\varphi\) a faithful normal state and \(\omega\) a free ultrafilter. Then \((M_{\varphi,\omega})'\cap M=\mathbb C1\) in \(M^\omega\), and the bicentralizer flow of \(M\) acts on \(\mathbb C1\).

**Proof.** By Proposition 1.3 of the bicentralizer lesson, \((M_{\varphi,\omega})'\cap M=\mathrm B(M,\varphi)\), which is \(\mathbb C1\) by Theorem 6.1. \(\square\)

In the language of the earlier lessons: every element of \(M\) that asymptotically commutes with all bounded sequences asymptotically commuting with \(\varphi\) is a scalar. The ergodicity of the bicentralizer flow, which Marrakchi proved in general [Marrakchi, Theorem D], is immediate here, since the flow acts on \(\mathbb C1\).

## 7. Exercises

**Exercise 7.1.** Let \(N\) be a II₁ factor with trace \(\tau\). Show that a bounded sequence \((b_n)\) with \(b_n^*b_n\to1\) strongly and \(\|b_n\tau-\mu\tau b_n\|\to0\) exists only for \(\mu=1\). Which hypothesis of Theorem 5.1 does a II₁ factor fail?

**Exercise 7.2.** Prove the converse of Lemma 2.1 directly: if \((b_n)\) is bounded and \(\|\xi b_n-\mu^{-1/2}b_n\xi\|\to0\), then \(\|b_n\theta-\mu\theta b_n\|\to0\). (Use Lemma 1.1 of the modular averaging lesson.)

**Exercise 7.3.** In Definition 3.1, show that one may equivalently ask, for every \(0<\lambda\le1\), for sequences \((v_n)\) with \(\|v_n\|\le1\), \(v_nv_n^*\to1\) strongly, \(\|v_n\theta-\lambda\theta v_n\|\to0\), and \(v_na-av_n\to0\) \(*\)-strongly for all \(a\).

**Exercise 7.4.** Let \(M\) be a type III₁ factor with separable predual and \(\varphi\) a faithful normal state. Using Theorem 6.1 and Proposition 1.3(4) of the bicentralizer lesson, show: for every \(a\in M\) with \(a\notin\mathbb C1\) there are \(\varepsilon>0\) and unitaries \(u_n\) with \(\|u_n\varphi u_n^*-\varphi\|\to0\) and \(\|u_n^*au_n-a\|_\varphi\ge\varepsilon\) for all \(n\).

## 8. Solutions

**7.1.** Evaluate at \(b_n^*\): \((b_n\tau)(b_n^*)=\tau(b_n^*b_n)\) and \((\tau b_n)(b_n^*)=\tau(b_nb_n^*)=\tau(b_n^*b_n)\). So \(|1-\mu|\,\tau(b_n^*b_n)\le\|b_n\tau-\mu\tau b_n\|\,\|b_n\|\to0\), while \(\tau(b_n^*b_n)\to1\) by normality. Hence \(\mu=1\). A II₁ factor is not of type III, and it has central eigen-isometries only in the trivial sense \(\mu=1\); Definition 3.1 asks for all \(\mu\ge1\).

**7.2.** Lemma 1.1 of the modular averaging lesson gives, for \(w\in N\) and real \(s\), \(\|\theta w-e^sw\theta\|\le(1+e^{s/2})\|(\Delta^{1/2}-e^{s/2})w\xi\|\). Take \(s=-\log\mu\) and \(w=b_n\): \(\Delta^{1/2}b_n\xi=\xi b_n\) and \(e^{s/2}=\mu^{-1/2}\), so \(\|\theta b_n-\mu^{-1}b_n\theta\|\to0\), which is \(\|b_n\theta-\mu\theta b_n\|\to0\) after multiplying by \(\mu\).

**7.3.** Pass between \(v_n\) and \(b_n=v_n^*\) with \(\mu=\lambda^{-1}\), as in the proof of Proposition 3.3: adjoints exchange \(v_nv_n^*\) and \(b_n^*b_n\), preserve \(*\)-strong convergence, and \(\|b_n\theta-\mu\theta b_n\|=\mu\|v_n\theta-\lambda\theta v_n\|\).

**7.4.** By Theorem 6.1, \(a\notin\mathrm B(M,\varphi)\). Condition (4) of Proposition 1.3 fails for \(a\): there is \(\varepsilon>0\) such that for every \(n\) some unitary \(u_n\) has \(\|[u_n,\varphi]\|<1/n\) and \(\|u_n^*au_n-a\|_\varphi\ge\varepsilon\); and \(\|u_n\varphi u_n^*-\varphi\|=\|[u_n,\varphi]\|\).

## References

- [OpenAI-recovery] OpenAI, Bounded recovery for modular spectral averages, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026
- [Marrakchi] A. Marrakchi, Full factors, bicentralizer flow and approximately inner automorphisms, Inventiones Mathematicae 222 (2020), 375–398. https://arxiv.org/abs/1811.10253
- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
- [MV] A. Marrakchi, S. Vaes, Ergodic states on type III₁ factors and ergodic actions, Journal für die reine und angewandte Mathematik 809 (2024), 247–260. https://arxiv.org/abs/2305.14217
- [HM26] C. Houdayer, A. Marrakchi, The classification of flows on II₁ factors and Connes' bicentralizer problem, preprint, 2026. https://arxiv.org/abs/2609.11462
