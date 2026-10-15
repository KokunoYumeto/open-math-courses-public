# Pure states, excision and peaking projections

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a Hilbert space \(H\), every nonzero irreducible representation of the algebra \(K(H)\) of compact operators is unitarily equivalent to the defining representation. In 1951 Naimark asked whether this property characterizes the algebras \(K(H)\). Akemann and Weaver gave a negative answer under Jensen's diamond principle [Akemann–Weaver 2004], and Calderón and Farah obtained a counterexample from a weakening of diamond [Calderón–Farah 2023]. This course presents a construction in ZFC alone, due to OpenAI [OpenAI-NA]: a unital, infinite-dimensional, simple C\(^*\)-algebra with a faithful tracial state whose nonzero irreducible representations are all unitarily equivalent. Tanaka gave another construction in ZFC [Tanaka 2026].

The construction adjoins unitaries, one at a time, each joining the equivalence class of one pure state to the class of another, while every other pure state keeps a unique extension and no other classes merge. This lesson collects the tools on states needed for that control.

- States, representations and the enveloping von Neumann algebra (Section 1).
- Unique extensions and peaking sequences (Section 2).
- Excision (Section 3).
- Inequivalent states and traces (Section 4).

The course continues with [Expectations from peaking projections](expectations-from-peaking-projections.md), [Reduced amalgamated free products of tracial algebras](reduced-amalgamated-free-products-of-tracial-algebras.md), [Reduced HNN adjunctions](reduced-hnn-adjunctions.md), [The bridge](the-bridge.md), [Closed subiterations and countable determination](closed-subiterations-and-countable-determination.md) and [The construction in ZFC](the-construction-in-zfc.md).

## 1. States, representations and the enveloping von Neumann algebra

All algebras and Hilbert spaces are complex. Unless stated otherwise, C\(^*\)-algebras are unital, and an inclusion \(B\subset C\) of C\(^*\)-algebras preserves the unit. A *state* of \(B\) is a positive linear functional \(h\) with \(h(1)=1\). It is *pure* if it is an extreme point of the set of states; by Proposition 8.4(3) and Theorem 8.3 of [Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), this is the notion of purity used there, and a state is pure exactly when its GNS representation is irreducible. A representation is *irreducible* if it is nonzero and its only closed invariant subspaces are \(\{0\}\) and the whole space.

We write \((\pi_h,H_h,\xi_h)\) for the GNS triple of a state \(h\) (Theorem 5.4 and Definition 5.6 of the GNS lesson): \(\xi_h\) is a cyclic unit vector and \(h(a)=\langle\pi_h(a)\xi_h,\xi_h\rangle\). Two pure states \(h,k\) are *equivalent*, written \(h\sim k\), if \(\pi_h\) and \(\pi_k\) are unitarily equivalent, and \([h]\) denotes the class of \(h\). For a unitary \(u\) we write \(\operatorname{Ad}(u)(a)=uau^*\).

**Lemma 1.1.** Let \(\pi\) be an irreducible representation of \(B\) on \(H\).

1. \(\pi(1)=1\), and every nonzero vector of \(H\) is cyclic for \(\pi\).
2. For a unit vector \(\zeta\in H\), the vector state \(\omega_\zeta(a)=\langle\pi(a)\zeta,\zeta\rangle\) is pure, and its GNS representation is unitarily equivalent to \(\pi\). Two pure states are equivalent exactly when they are vector states of one irreducible representation.

*Proof.* (1) \(\pi(1)\) is a projection commuting with \(\pi(B)\), so its range is a closed invariant subspace. It is nonzero, since \(\pi(a)=\pi(1)\pi(a)\) and \(\pi\ne0\). Hence \(\pi(1)=1\). For \(\zeta\ne0\), the closure of \(\pi(B)\zeta\) is invariant and contains \(\zeta=\pi(1)\zeta\), so it is \(H\).

(2) By (1), \(\zeta\) is a cyclic unit vector, and Theorem 5.5 of the GNS lesson gives a unitary \(U\colon H_{\omega_\zeta}\to H\) with \(U\pi_{\omega_\zeta}(a)=\pi(a)U\). So \(\pi_{\omega_\zeta}\) is irreducible and \(\omega_\zeta\) is pure. If \(h\sim k\) through a unitary \(V\colon H_k\to H_h\) with \(V\pi_k(a)=\pi_h(a)V\), then \(k\) is the vector state of \(V\xi_k\) in \(\pi_h\). Conversely, vector states of one irreducible representation have GNS representations equivalent to it. \(\square\)

*The enveloping von Neumann algebra.* Let \(B^{**}\) be the enveloping von Neumann algebra of \(B\), realized by the universal representation on a Hilbert space \(H_u\) (Theorem 3.3 of [The universal enveloping von Neumann algebra of a C\(^*\)-algebra and W\(^*\)-algebras](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras)). The algebra \(B\) is \(\sigma\)-weakly dense in \(B^{**}\), and multiplication is separately \(\sigma\)-weakly continuous. Every \(f\in B^*\) has a unique normal extension \(\hat f\) to \(B^{**}\), and every representation \(\pi\) of \(B\) has a unique normal extension \(\bar\pi\colon B^{**}\to B(H)\), a normal \(*\)-homomorphism (Lemma 2.1(2) of the enveloping lesson). For vectors \(\zeta,\eta\), the normal extension of \(a\mapsto\langle\pi(a)\zeta,\eta\rangle\) is \(X\mapsto\langle\bar\pi(X)\zeta,\eta\rangle\): both are normal and agree on the dense subalgebra \(B\). A bounded net that converges strongly in \(B^{**}\) also converges \(\sigma\)-weakly, so normal functionals respect such limits.

For a state \(h\), the normal state \(\hat h\) has a support \(r_h=s(\hat h)\), a projection of \(B^{**}\) (Lemma 11.1 of the enveloping lesson). It is the least projection \(r\in B^{**}\) with \(\hat h(r)=1\), and \(\hat h(X)=\hat h(r_hXr_h)\) for \(X\in B^{**}\).

A *tracial algebra* is a pair \((B,\tau)\) of a C\(^*\)-algebra and a faithful tracial state: \(\tau(ab)=\tau(ba)\), and \(\tau(a^*a)=0\) only for \(a=0\).

**Lemma 1.2.** The normal extension \(\hat\tau\) of a tracial state \(\tau\) is tracial on \(B^{**}\).

*Proof.* For fixed \(a\in B\), the maps \(X\mapsto\hat\tau(aX)\) and \(X\mapsto\hat\tau(Xa)\) are \(\sigma\)-weakly continuous and agree on \(B\), hence on \(B^{**}\). For fixed \(Y\in B^{**}\), the maps \(X\mapsto\hat\tau(XY)\) and \(X\mapsto\hat\tau(YX)\) are \(\sigma\)-weakly continuous and, by the first step, agree on \(B\); hence they agree on \(B^{**}\). \(\square\)

We write \(\tau\) also for \(\hat\tau\). For an inclusion \(B\subset C\) we shall use the property

> (U) every pure state of \(B\) has exactly one state extension to \(C\).

Uniqueness is among all states of \(C\). Existence holds for every state: a state of \(B\) extends to a state of \(C\) by Proposition 7.1a of the GNS lesson.

## 2. Unique extensions and peaking sequences

**Lemma 2.1.** If a pure state \(h\) of \(B\) has exactly one state extension \(\tilde h\) to \(C\supset B\), then \(\tilde h\) is pure.

*Proof.* Let \(\tilde h=tk_1+(1-t)k_2\) with states \(k_i\) of \(C\) and \(0<t<1\). Restricting to \(B\) and using purity of \(h\) gives \(k_i|_B=h\). Both \(k_i\) extend \(h\), so \(k_1=k_2=\tilde h\). \(\square\)

**Lemma 2.2** ([OpenAI-NA, Lemma 2.2]). Let \(h\) be a pure state of \(B\) and \(\eta\in H_h\) a unit vector. There is a unitary \(u\in B\) with \(\pi_h(u)\xi_h=\eta\). Consequently, if \(k\sim h\), there is a unitary \(u\in B\) with \(k=h\circ\operatorname{Ad}(u^*)\). If moreover \(h\) and \(k\) have unique state extensions \(\tilde h\) and \(\tilde k\) to \(C\supset B\), then \(\tilde k=\tilde h\circ\operatorname{Ad}(u^*)\) and \(\tilde h\sim\tilde k\).

*Proof.* Write \(\xi=\xi_h\) and \(\pi=\pi_h\). If \(\eta=\lambda\xi\) with \(|\lambda|=1\), take \(u=\lambda1\). Otherwise let \(e\) be the projection onto the two-dimensional span of \(\xi\) and \(\eta\), and choose a unitary \(w\) of \(eH_h\) with \(w\xi=\eta\). By the spectral theorem in finite dimension, \(w=e^{i\beta}\) for a self-adjoint operator \(\beta\) of \(eH_h\). Let \(b\in B(H_h)\) act as \(\beta\) on \(eH_h\) and as \(0\) on \((1-e)H_h\). The algebra \(\pi(B)\) is irreducible, and Kadison's transitivity theorem in its self-adjoint form (Theorem 11.1(2) of [Kaplansky's density theorem and its consequences](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences)) gives a self-adjoint element of \(\pi(B)\) agreeing with \(b\) on \(eH_h\). It is \(\pi(a)\) for some \(a\in B\), and replacing \(a\) by \((a+a^*)/2\) we may take \(a\) self-adjoint. As \(\pi(a)\) is self-adjoint and maps \(eH_h\) into itself, \(eH_h\) reduces \(\pi(a)\), which acts there as \(\beta\). Put \(u=e^{ia}\), a unitary of \(B\). Then \(\pi(u)=e^{i\pi(a)}\) acts on \(eH_h\) as \(w\), so \(\pi(u)\xi=\eta\).

If \(k\sim h\), Lemma 1.1(2) realizes \(k\) as the vector state of a unit vector \(\eta\in H_h\). With \(u\) as above, \(k(a)=\langle\pi(a)\pi(u)\xi,\pi(u)\xi\rangle=h(u^*au)\), that is \(k=h\circ\operatorname{Ad}(u^*)\). Finally \(\tilde h\circ\operatorname{Ad}(u^*)\) is a state of \(C\) extending \(k\), so it equals \(\tilde k\). It is the vector state of \(\pi_{\tilde h}(u)\xi_{\tilde h}\) in the irreducible representation \(\pi_{\tilde h}\) (Lemma 2.1), so \(\tilde k\sim\tilde h\) by Lemma 1.1(2). \(\square\)

**Definition 2.3.** A decreasing sequence of projections \((P_n)_{n\ge0}\) of \(B\) *peaks to* a state \(h\) if \(h\) is the only state of \(B\) with \(h(P_n)=1\) for every \(n\). We then call \((P_n)\) a *peaking sequence* for \(h\).

**Lemma 2.4.** A state to which a decreasing sequence of projections peaks is pure.

*Proof.* Let \(h=tk_1+(1-t)k_2\) with states \(k_i\) and \(0<t<1\). From \(1=h(P_n)=tk_1(P_n)+(1-t)k_2(P_n)\) and \(k_i(P_n)\le1\) we get \(k_i(P_n)=1\) for every \(n\), so \(k_1=k_2=h\). \(\square\)

**Lemma 2.5** (peaking under restriction; [OpenAI-NA, Lemma 2.3]). Let \(B\subset C\), and let \((P_n)\) be a decreasing sequence of projections of \(B\) that peaks to a state \(H\) of \(C\). Then \((P_n)\) peaks to \(h=H|_B\) in \(B\), and \(H\) is the only state extension of \(h\) to \(C\).

*Proof.* Let \(k\) be a state of \(B\) with \(k(P_n)=1\) for every \(n\), and extend it to a state \(K\) of \(C\). Then \(K(P_n)=1\) for every \(n\), so \(K=H\) and \(k=h\). Every extension of \(h\) to \(C\) takes the value one on every \(P_n\), so it equals \(H\). \(\square\)

## 3. Excision

**Lemma 3.1** (fixed vectors). Let \(\psi\) be a state of \(B\) and \(x\in B\) with \(0\le x\le1\) and \(\psi(x)=1\). Then \(\pi_\psi(x)\xi_\psi=\xi_\psi\), and \(\psi(xa)=\psi(ax)=\psi(a)\) for every \(a\in B\). The same holds for \(X\in B^{**}\) with \(0\le X\le1\) and \(\hat\psi(X)=1\): then \(\bar\pi_\psi(X)\xi_\psi=\xi_\psi\).

*Proof.* From \(0\le x\le1\) we get \((1-x)^2\le1-x\) by the functional calculus, so
\[
\begin{aligned}\|(1-\pi_\psi(x))\xi_\psi\|^2&=\psi\bigl((1-x)^2\bigr)\\&\le\psi(1-x)=0 .\end{aligned}
\]
Then \(\psi(xa)=\langle\pi_\psi(a)\xi_\psi,\pi_\psi(x)\xi_\psi\rangle=\psi(a)\), and \(\psi(ax)=\psi(a)\) in the same way. The computation with \(\bar\pi_\psi\) and \(\hat\psi(X)=\langle\bar\pi_\psi(X)\xi_\psi,\xi_\psi\rangle\) gives the last claim. \(\square\)

**Theorem 3.2** (decreasing excision; [OpenAI-NA, Lemma 2.4]). Let \(h\) be a pure state of \(B\). There is a decreasing net \((x_\lambda)\) of elements of \(B\) with \(0\le x_\lambda\le1\) and \(h(x_\lambda)=1\), converging strongly in \(B^{**}\) to \(r_h\), such that
\[
\begin{gathered}\|x_\lambda(a-h(a)1)x_\lambda\|\\\longrightarrow0\quad(a\in B).\end{gathered}\tag{3.1}
\]
Moreover \(r_h\) is a minimal projection of \(B^{**}\), and \(r_hXr_h=\hat h(X)\,r_h\) for every \(X\in B^{**}\).

*Proof.* *Step 1: an ideal.* Let \(L=\{a\in B:h(a^*a)=0\}\), a closed left ideal (Lemma 3.3 of the GNS lesson), and \(N=L\cap L^*\), a C\(^*\)-subalgebra of \(B\), possibly without unit. By the Cauchy–Schwarz inequality (Proposition 3.2 there), \(|h(a)|^2\le h(a^*a)\), so \(h\) vanishes on \(L\). If \(a\in L\), then \(a^*a\in N\): indeed \((a^*a)^2=a^*(aa^*)a\le\|a\|^2a^*a\) by Proposition 8.5(3) of [C\(^*\)-algebras: continuous functional calculus, automatic continuity, positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones), so \(h((a^*a)^2)\le\|a\|^2h(a^*a)=0\).

*Step 2: \(h\) is the only state annihilating \(N\).* By Proposition 7.3 of the enveloping lesson, \(a\mapsto\pi_h(a)\xi_h\) maps \(B\) onto \(H_h\) with kernel \(L\), and \(\|\pi_h(a)\xi_h\|\) is the quotient norm \(\|a+L\|\). Let \(k\) be a state with \(k(N)=0\). For \(l\in L\), \(\|\pi_k(l)\xi_k\|^2=k(l^*l)=0\), since \(l^*l\in N\). Hence, for \(a\in B\) and \(l\in L\),
\[
\|\pi_k(a)\xi_k\|=\|\pi_k(a-l)\xi_k\|\le\|a-l\|,
\]
so \(\|\pi_k(a)\xi_k\|\le\|\pi_h(a)\xi_h\|\). Therefore \(T\pi_h(a)\xi_h=\pi_k(a)\xi_k\) defines a contraction \(T\colon H_h\to H_k\), and \(T\pi_h(b)=\pi_k(b)T\) for \(b\in B\). Then \(T^*T\) commutes with \(\pi_h(B)\), so \(T^*T=c1\) by Lemma 7.2 of the enveloping lesson, with \(c=\|T\xi_h\|^2=\|\xi_k\|^2=1\). So \(k(a)=\langle T\pi_h(a)\xi_h,T\xi_h\rangle=h(a)\).

*Step 3: the net.* The positive part \(N_+\) is upward directed by the order, since \(s,s'\le s+s'\). For \(s\in N_+\) put
\[
\begin{gathered}e_s=s(1+s)^{-1},\\x_s=1-e_s=(1+s)^{-1}.\end{gathered}
\]
The function \(t\mapsto t/(1+t)\) vanishes at \(0\), so \(e_s\in N\) (Theorem 5.3 of the C\(^*\)-algebra lesson), and \(0\le x_s\le1\). If \(s\le s'\), then \(1+s\le1+s'\), and Proposition 8.5(7) there gives \(x_{s'}\le x_s\): the net \((x_s)\) decreases. As \(e_s\in N\subset L\), \(h(x_s)=1\). For \(b\in N\) and \(m\ge1\), every \(s\ge m(bb^*+b^*b)\) satisfies
\[
\begin{aligned}\|x_sb\|^2&=\|x_sbb^*x_s\|\\&\le\frac1m\|x_ssx_s\|\le\frac1{4m},\end{aligned}
\]
because \(bb^*\le s/m\) and \(x_ssx_s=s(1+s)^{-2}\) has spectrum in \([0,\frac14]\). In the same way \(\|bx_s\|^2=\|x_sb^*bx_s\|\le1/(4m)\). Hence
\[
\begin{gathered}\|x_sb\|\to0,\quad\|bx_s\|\to0\\ (b\in N).\end{gathered}\tag{3.2}
\]

*Step 4: the support.* By Vigier's theorem (Theorem 1.3 of the Kaplansky lesson), \((e_s)\) converges strongly in \(B^{**}\) to an element \(q\), and \(x_s\to1-q\). For \(b\in N\), (3.2) gives \(qb=b\): \(e_sb\to b\) in norm and \(e_sb\to qb\) strongly. Taking \(b=e_s\) gives \(qe_s=e_s\), and letting \(s\) grow gives \(q^2=q\). So \(q\) is a projection, and so is \(r=1-q\). By normality, \(\hat h(r)=\lim_sh(x_s)=1\).

Let \(\psi\) be a normal state of \(B^{**}\) with \(\psi(r)=1\). Then \(\psi(q)=0\), and for \(b\in N\) the Cauchy–Schwarz inequality gives \(|\psi(b)|^2=|\psi(qb)|^2\le\psi(q)\psi(b^*b)=0\). So \(\psi|_B\) is a state annihilating \(N\); it equals \(h\) by Step 2, and \(\psi=\hat h\) by density. In particular, for every unit vector \(\zeta\in rH_u\), the normal state \(X\mapsto\langle X\zeta,\zeta\rangle\) equals \(\hat h\). Let \(Y\in rB^{**}r\) be self-adjoint and \(Z=Y-\hat h(Y)r\). Then \(Z=rZr\), and \(\langle Z\zeta,\zeta\rangle=0\) for every unit \(\zeta\in rH_u\), hence for every \(\zeta\in H_u\). So \(Z=0\). Splitting into real and imaginary parts, \(rB^{**}r=\mathbb Cr\), and \(r\ne0\) is a minimal projection. Since \(\hat h(r)=1\), \(r_h\le r\), and \(r_h\ne0\); minimality gives \(r_h=r\). Finally \(r_hXr_h\) is a multiple \(c\,r_h\), and applying \(\hat h\) gives \(c=\hat h(r_hXr_h)=\hat h(X)\).

*Step 5: excision.* Let \(a\) be self-adjoint, and suppose (3.1) fails for \(a\). Then there are \(\varepsilon>0\) and a cofinal set \(\Lambda'\) of indices with \(\|x_s(a-h(a)1)x_s\|\ge\varepsilon\) for \(s\in\Lambda'\). A self-adjoint element \(y\) has a point \(\lambda\) of its spectrum with \(|\lambda|=\|y\|\) (Theorem 1.3 of the C\(^*\)-algebra lesson); evaluation at \(\lambda\) is a state of \(C^*(1,y)\), and it extends to a state of \(B\). So for \(s\in\Lambda'\) there are states \(\rho_s\) of \(B\) with \(|\rho_s(x_s(a-h(a)1)x_s)|\ge\varepsilon\). The positive functionals \(\varphi_s(c)=\rho_s(x_scx_s)\) have norm at most one, and they have a weak\(^*\) cluster point \(\varphi\) along \(\Lambda'\) (Proposition 8.4(1) of the GNS lesson). For \(b\in N\), \(|\varphi_s(b)|\le\|x_sb\|\to0\), so \(\varphi(N)=0\). If \(\varphi\ne0\), then \(\varphi/\varphi(1)\) is a state annihilating \(N\), hence \(\varphi=\varphi(1)h\). In both cases \(\varphi(a-h(a)1)=0\), which contradicts \(|\varphi(a-h(a)1)|\ge\varepsilon\). For arbitrary \(a\), apply this to its real and imaginary parts. \(\square\)

The existence of a decreasing net with (3.1) is due to Akemann, Anderson and Pedersen; it is recalled before Lemma 1 of [Akemann–Weaver 2004].

**Lemma 3.3** (projection excision; [OpenAI-NA, Lemma 2.5]). Let \((P_n)\) be a decreasing sequence of projections of \(B\) that peaks to \(h\). Then \(P_n\to r_h\) strongly in \(B^{**}\), and
\[
\|P_n(a-h(a)1)P_n\|\longrightarrow0\qquad(a\in B).
\]
If \(h(a)=0\), then \(\|P_naP_t\|\to0\) as \(\min(n,t)\to\infty\).

*Proof.* The state \(h\) is pure by Lemma 2.4. Let \(P\) be the strong limit of \((P_n)\) in \(B^{**}\), the infimum of the \(P_n\) (Corollary 1.4 of the Kaplansky lesson). A normal state \(\psi\) of \(B^{**}\) satisfies \(\psi(P)=1\) exactly when \(\psi(P_n)=1\) for every \(n\), since \(P\le P_n\) and \(\psi(P)=\lim_n\psi(P_n)\); this happens exactly when \(\psi|_B=h\), that is \(\psi=\hat h\). By normality \(\hat h(P)=\lim_nh(P_n)=1\), so \(P\ne0\), and the argument of Step 4 above shows \(PB^{**}P=\mathbb CP\). So \(P\) is minimal, and \(r_h\le P\) gives \(r_h=P\).

For the excision, let \(\rho_n\) be states of \(B\) and let \(\varphi\) be a weak\(^*\) cluster point of the functionals \(c\mapsto\rho_n(P_ncP_n)\). For \(n\ge m\), \(P_n(1-P_m)P_n=0\), so \(\varphi(1-P_m)=0\) for every \(m\). If \(\varphi\ne0\), then \(\varphi/\varphi(1)\) is a state taking the value one on every \(P_m\), so it is \(h\). In every case \(\varphi(a-h(a)1)=0\), and Step 5 above gives the excision. For the last assertion put \(q=\min(n,t)\). Then \(P_naP_t=P_nP_qaP_qP_t\), so \(\|P_naP_t\|\le\|P_qaP_q\|\to0\). \(\square\)

## 4. Inequivalent states and traces

Excision also separates inequivalent pure states in norm.

**Lemma 4.1** (cross-excision; [OpenAI-NA, Lemma 2.6], [Akemann–Weaver 2004, Lemma 1]). Let \(h\not\sim k\) be pure states of \(B\). Let \((x_\lambda)\) be a net as in Theorem 3.2 for \(h\), or a peaking sequence for \(h\), and let \((y_\nu)\) be such a net or sequence for \(k\). Then, for every \(a\in B\),
\[
\|x_\lambda ay_\nu\|\longrightarrow0
\]
on the product of the two directed sets.

*Proof.* First, \(\bar\pi_h(r_k)=0\). Otherwise let \(\zeta\) be a unit vector in the range of \(\bar\pi_h(r_k)\). By Theorem 3.2 for \(k\), \(r_kar_k=k(a)r_k\), so
\[
\begin{aligned}\langle\pi_h(a)\zeta,\zeta\rangle&=\langle\bar\pi_h(r_kar_k)\zeta,\zeta\rangle\\&=k(a)\qquad(a\in B).\end{aligned}
\]
Thus \(k\) is a vector state of \(\pi_h\), and \(k\sim h\) by Lemma 1.1(2), a contradiction.

By Theorem 3.2 and Lemma 3.3, \(y_\nu\to r_k\) strongly, so by normality
\[
\begin{gathered}h(ay_\nu a^*)\longrightarrow\\\langle\bar\pi_h(r_k)\pi_h(a^*)\xi_h,\pi_h(a^*)\xi_h\rangle=0 ,\end{gathered}
\]
and the convergence is decreasing. Given \(\varepsilon>0\), choose \(\nu_0\) with \(h(ay_{\nu_0}a^*)<\varepsilon\). For \(\nu\ge\nu_0\) we have \(y_\nu^2\le y_\nu\le y_{\nu_0}\), so with \(c=ay_{\nu_0}a^*\),
\[
\begin{aligned}
\|x_\lambda ay_\nu\|^2&=\|x_\lambda ay_\nu^2a^*x_\lambda\|\le\|x_\lambda cx_\lambda\|\\
&\le h(c)+\|x_\lambda(c-h(c)1)x_\lambda\| .
\end{aligned}
\]
By (3.1), or by Lemma 3.3, there is \(\lambda_0\) with \(\|x_\lambda(c-h(c)1)x_\lambda\|<\varepsilon\) for \(\lambda\ge\lambda_0\). Then \(\|x_\lambda ay_\nu\|^2<2\varepsilon\) for all \(\lambda\ge\lambda_0\) and \(\nu\ge\nu_0\). \(\square\)

**Lemma 4.2** (trace-null supports; [OpenAI-NA, Lemma 2.7]). Suppose that \(B\) has no finite-dimensional irreducible representation, and let \(\tau\) be a tracial state of \(B\). Then \(\tau(r_h)=0\) for every pure state \(h\) of \(B\).

*Proof.* The space \(H_h\) is infinite-dimensional, since \(\pi_h\) is irreducible. Choose an orthonormal sequence \((\eta_j)\) in \(H_h\), and by Lemma 2.2 unitaries \(u_j\in B\) with \(\pi_h(u_j)\xi_h=\eta_j\). The projections \(u_jr_hu_j^*\) of \(B^{**}\) are pairwise orthogonal: by Theorem 3.2,
\[
\begin{aligned}r_hu_i^*u_jr_h&=h(u_i^*u_j)\,r_h\\&=\langle\eta_j,\eta_i\rangle\,r_h=0\qquad(i\ne j).\end{aligned}
\]
Each has trace \(\tau(r_h)\) by Lemma 1.2. The sum of the first \(m\) of them is a projection, so \(m\,\tau(r_h)\le1\) for every \(m\), and \(\tau(r_h)=0\). \(\square\)

## 5. Exercises

**5.1.** Let \(B=M_n(\mathbb C)\) and \(h(a)=\langle a\xi,\xi\rangle\) for a unit vector \(\xi\in\mathbb C^n\). Show that \(r_h\) is the projection onto \(\mathbb C\xi\), and that the constant net \(x_\lambda=r_h\) satisfies (3.1).

**5.2.** Let \(B=C(\mathbb N_0\cup\{\infty\})\), the continuous functions on the one-point compactification of \(\mathbb N_0\), and let \(P_n\) be the indicator function of \(\{n,n+1,\ldots\}\cup\{\infty\}\). Show that \((P_n)\) peaks to evaluation at \(\infty\).

**5.3.** Show that property (U) fails for the inclusion \(\mathbb C1\subset\mathbb C^2\).

**5.4.** Let \(B=M_n(\mathbb C)\) with its normalized trace \(\tau\) and \(h\) as in Exercise 5.1. Compute \(\tau(r_h)\), and explain why Lemma 4.2 does not apply.

**5.5.** In \(M_2(\mathbb C)\), let \(h\) and \(k\) be the vector states of the two standard basis vectors. Show that \(h\sim k\), and find \(a\) with \(\|r_har_k\|=1\). Which hypothesis of Lemma 4.1 fails?

## 6. Solutions

**5.1.** A finite-dimensional C\(^*\)-algebra is a von Neumann algebra in each of its representations, and \(B^{**}=B\). Let \(p\) be the projection onto \(\mathbb C\xi\). Then \(h(p)=1\), and a projection \(r\) with \(h(r)=\|r\xi\|^2=1\) satisfies \(r\xi=\xi\), so \(p\le r\). Hence \(r_h=p\). For every \(a\), \(pap=\langle a\xi,\xi\rangle p=h(a)p\), so \(p(a-h(a)1)p=0\).

**5.2.** Evaluation \(\delta_\infty\) at \(\infty\) takes the value one on every \(P_n\). A state of \(C(\mathbb N_0\cup\{\infty\})\) is integration against a probability measure \(\mu\) (Riesz representation). If \(\mu(\{n,n+1,\ldots\}\cup\{\infty\})=1\) for every \(n\), then \(\mu(\{j\})=0\) for every \(j\in\mathbb N_0\), so \(\mu=\delta_\infty\).

**5.3.** The only state of \(\mathbb C1\) is \(\lambda1\mapsto\lambda\), which is pure. Its extensions to \(\mathbb C^2\) are the states \((x,y)\mapsto tx+(1-t)y\) with \(0\le t\le1\), infinitely many.

**5.4.** By Exercise 5.1, \(r_h\) is a projection of rank one, so \(\tau(r_h)=1/n\ne0\). The algebra \(M_n(\mathbb C)\) has a finite-dimensional irreducible representation, the identity representation on \(\mathbb C^n\).

**5.5.** Both are vector states of the identity representation, which is irreducible, so \(h\sim k\) by Lemma 1.1(2). Here \(r_h=e_{11}\) and \(r_k=e_{22}\), and \(a=e_{12}\) gives \(r_har_k=e_{12}\), of norm one. The hypothesis \(h\not\sim k\) fails.

## References

- [OpenAI-NA] OpenAI, *A counterexample to Naimark's problem in ZFC*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026
- [Akemann–Weaver 2004] C. Akemann, N. Weaver, *Consistency of a counterexample to Naimark's problem*, Proc. Natl. Acad. Sci. USA 101 (2004). https://arxiv.org/abs/math/0312135
- [Calderón–Farah 2023] D. Calderón, I. Farah, *Can you take Akemann–Weaver's \(\diamondsuit_{\aleph_1}\) away?*, J. Funct. Anal. 285 (2023). https://arxiv.org/abs/2006.06886
- [Tanaka 2026] R. Tanaka, *A separably representable counterexample to Naimark's problem in ZFC*, preprint, 2026. https://arxiv.org/abs/2609.26930
