# Binormal states and the relative bicentralizer

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M\) act standardly on \(H=L^2(M)\). A state \(\Phi\) of \(B(H)\) is *binormal* if its restrictions to \(M\) and to \(M'\) are normal. Such a state need not be normal. Marrakchi proved that a binormal state is the vector state of a vector in the \(L^2\) space of an ultrapower of \(A\mathbin{\bar\otimes}M\), with \(A\) abelian, when \(M\) is finite or semifinite, and for general \(M\) when the state is concentrated at the point \(1\) of the spectrum of a relative modular operator [M1, Theorems 2.1, 2.4 and 2.9]. For an inclusion \(N\subset M\) with expectation this yields the identity
\[
\Phi(a\rho(b))=\langle a\xi b,\xi\rangle\qquad(a\in\mathrm B(N\subset M,\varphi),\ b\in M)
\]
for every state \(\Phi\) with the two marginals of \(\bar\varphi=\varphi\circ E\) that lives on \(L^2(N)\) and at modular energy zero [M2, Lemma 2.1]. Elements of the relative bicentralizer cannot tell such a state apart from the vector state of \(\xi\). The identity is the analytic input of the last lessons of this course.

The proof given here replaces ultrapowers by sequences of vectors in finite direct sums of copies of \(H\). Section 2 treats a finite von Neumann algebra in its trace representation: a normal state whose two marginals are dominated by a multiple of the trace is a sum of vector states of bounded elements, and mixing these with independent random cube roots of unity keeps a fourth moment bounded. Section 3 shows that a corner of the continuous core of \(M\), cut down by a projection of the commutant, is a finite von Neumann algebra in its trace representation. Section 4 moves a binormal state at modular energy zero into that corner and brings the resulting vectors back to \(H\). Section 5 proves the identity. No assumption on the type of \(N\) is needed.

We use: Theorem 2.3, Lemma 2.4 (uniform modulus) and formula (1.1) of [The relative bicentralizer](the-relative-bicentralizer.md); the regular model of the continuous core, its corner traces and the antiunitary \(\mathcal J\), Sections 2–3 and formulas (C3), (C5), (C7) and (C11) of [The faithful-state core](course:OA-FLOW/OA-FLOW-L159#OA-FLOW.FSCORE.CORNERS.heading); the commutant theorem (CCM2) of [The normal crossed-product commutant](course:OA-FLOW/OA-FLOW-CCM#ccm0-the-exact-statement-and-the-two-concrete-models); Theorem 5.8 (reduced and induced algebras) and Proposition 9.2 (cyclic and separating vectors) of [The double commutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-04); normal states of \(B(K)\) as positive trace-class operators, [Compact and trace-class operators](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies); densities of normal positive functionals for a finite trace and the trace calculus on measurable operators, Facts 2.3(g), 2.4, 2.5(d) and 2.6(b) of [Measurable operators for a trace](course:traces-and-noncommutative-integration/measurable-operators-for-a-trace-examples-convergence-and-the-commutant#2-results-used-from-other-lessons); the Powers–Størmer inequality \(\|D_1^{1/2}-D_2^{1/2}\|_2^2\le\|D_1-D_2\|_1\), Lemma 3.3 of [Strongly invariant states and approximate eigenstates](course:bicentralizers-of-type-iii1-factors/strongly-invariant-states#3-approximate-eigenstates); Lemmas 1.1 and 1.2 and formula (1.1) of [Modular averaging and bounded recovery](course:bicentralizers-of-type-iii1-factors/modular-averaging-and-bounded-recovery#1-notation-and-two-modular-estimates); (B6) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); Theorem 9.1(3),(4) of [Analytic elements and strip arguments](course:analytic-elements-strips-and-kms/analytic-elements-and-strip-arguments#9-entire-elements-of-automorphism-groups-of-von-neumann-algebras); and Mazur's theorem and the Hahn–Banach separation theorem, [Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian).

## 1. Conventions

For a von Neumann algebra \(M\) with a faithful normal state \(\psi\) we use its GNS space \(H\) with cyclic and separating vector \(\xi\), modular conjugation \(J\) and modular operator \(\Delta\), and put
\[
X=\log\Delta,\qquad\rho(b)=Jb^*J\quad(b\in M),\qquad h\,b=\rho(b)h\quad(h\in H).
\]
So \(\rho\) is an anti-isomorphism of \(M\) onto \(M'\): \(\rho(b)\rho(c)=\rho(cb)\) and \(\rho(b)^*=\rho(b^*)\). By formula (1.1) of the modular averaging lesson, \(e^{X/2}a\xi=\xi a\) for \(a\in M\), and \(\langle\xi b,\xi\rangle=\psi(b)\). If \(a\) is entire analytic for \(\sigma^\psi\), put \(a_+=\sigma^\psi_{i/2}(a)\). Theorem 9.1(4) of the analytic elements lesson, with \(W_t=\Delta^{it}\) and \(\Delta^{-1/2}\xi=\xi\), gives \(\Delta^{-1/2}a\xi=a_+\xi\), hence
\[
\xi a_+=\Delta^{1/2}a_+\xi=a\xi .
\tag{1.1}
\]
A state \(\Phi\) of \(B(H)\) is *binormal* if \(\Phi|_M\) and \(\Phi|_{M'}\) are normal, that is, if \(b\mapsto\Phi(b)\) and \(b\mapsto\Phi(\rho(b))\) are normal on \(M\).

For a finite set \(F\) we write \(\Omega_F=(\mathbb Z/3)^F\) with the uniform probability \(\mu_F\), \(A_F=\ell^\infty(\Omega_F)\) acting on \(L^2(\Omega_F,\mu_F)\) by multiplication, and \(u_j\in A_F\) (\(j\in F\)) for the coordinate functions \(u_j(\omega)=e^{2\pi i\omega_j/3}\). For a Hilbert space \(K\), \(L^2(\Omega_F,\mu_F)\otimes K\) is the space of functions \(\zeta\colon\Omega_F\to K\) with \(\|\zeta\|^2=\sum_\omega\mu_F(\omega)\|\zeta(\omega)\|^2\). For a von Neumann algebra \(P\) on \(K\), \(A_F\otimes P\) is the von Neumann algebra of functions \(\Omega_F\to P\), acting pointwise, and an operator \(T\) on \(K\) acts as \(1\otimes T\), pointwise. The coordinates are independent and uniformly distributed on the cube roots of unity, so
\[
\int\overline{u_j}\,u_k\,d\mu_F=\delta_{jk},\qquad
\int\overline{u_j}\,u_k\,\overline{u_l}\,u_m\,d\mu_F=\begin{cases}1&\text{if }\{k,m\}=\{j,l\}\text{ as multisets},\\0&\text{otherwise}.\end{cases}
\tag{1.2}
\]
Indeed the integrand is \(\prod_ie^{2\pi i c_i\omega_i/3}\) with \(c=e_k+e_m-e_j-e_l\in\mathbb Z^F\), whose coordinates lie in \(\{-2,\ldots,2\}\); its integral is \(1\) if every \(c_i\) is divisible by \(3\), that is \(c=0\), and \(0\) otherwise.

## 2. The tracial case

Throughout this section \(Q\) is a von Neumann algebra on a Hilbert space \(K\) with a faithful normal tracial state \(\tau\), \(\eta\in K\) is a unit vector, cyclic and separating for \(Q\), with \(\tau(x)=\langle x\eta,\eta\rangle\), and \(J\) is an antiunitary involution of \(K\) with
\[
Jx\eta=x^*\eta\quad(x\in Q),\qquad Q'=JQJ .
\]
Then \(\rho(b)=Jb^*J\) satisfies \(\rho(b)x\eta=Jb^*x^*\eta=xb\eta\), and \(\rho\) is an order-preserving normal anti-isomorphism of \(Q\) onto \(Q'\). A state \(\Psi\) of \(B(K)\) is *binormal* if \(\Psi|_Q\) and \(\Psi\circ\rho\) are normal on \(Q\). Densities of normal positive functionals on \(Q\) with respect to \(\tau\) lie in \(L^1(Q,\tau)_+\) (Fact 2.6(b) of the measurable operators lesson).

**Proposition 2.1** (dominated marginals). Let \(D\) be a positive trace-class operator on \(K\) such that
\[
\operatorname{Tr}(Dy)\le\kappa\tau(y)\quad\text{and}\quad\operatorname{Tr}(D\rho(y))\le\kappa\tau(y)\qquad(y\in Q_+).
\]
Let \((e_j)_{j\in\mathcal I}\) be an orthonormal basis of \(K\) and \(a_j=D^{1/2}e_j\). There are \(x_j\in Q\) with \(a_j=x_j\eta\), \(\sum_jx_jx_j^*\le\kappa\) and \(\sum_jx_j^*x_j\le\kappa\), the sums converging strongly.

**Proof.** For \(y\in Q\), \(\sum_j\|ya_j\|^2=\operatorname{Tr}(D^{1/2}y^*yD^{1/2})=\operatorname{Tr}(Dy^*y)\le\kappa\|y\eta\|^2\). So \(y\eta\mapsto(ya_j)_j\) extends to an operator \(T\colon K\to K\otimes\ell^2(\mathcal I)\) of norm at most \(\sqrt\kappa\). Its components \(T_j\colon y\eta\mapsto ya_j\) satisfy \(T_jzy\eta=zT_jy\eta\) for \(z\in Q\), so \(T_j\in Q'=\rho(Q)\): \(T_j=\rho(x_j)\) with \(x_j\in Q\), and \(a_j=T_j\eta=\rho(x_j)\eta=x_j\eta\). Since \(\sum_jT_j^*T_j=T^*T\le\kappa\) and \(T_j^*T_j=\rho(x_j^*)\rho(x_j)=\rho(x_jx_j^*)\), and \(\rho\) is an order-preserving normal anti-isomorphism, \(\sum_jx_jx_j^*\le\kappa\). For the other sum, \(\rho(y)a_j=x_jy\eta\). So for every finite set \(F\subset\mathcal I\), \(S_F=\sum_{j\in F}x_j^*x_j\) and \(y\in Q\),
\[
\tau(y^*S_Fy)=\sum_{j\in F}\|x_jy\eta\|^2\le\operatorname{Tr}\big(D\rho(y)^*\rho(y)\big)=\operatorname{Tr}(D\rho(yy^*))\le\kappa\tau(yy^*)=\kappa\tau(y^*y).
\]
If \(e\) is the spectral projection of \(S_F\) for \((\lambda,\infty)\) with \(\lambda>\kappa\), taking \(y=e\) gives \(\lambda\tau(e)\le\tau(eS_Fe)\le\kappa\tau(e)\), so \(\tau(e)=0\) and \(e=0\). Hence \(S_F\le\kappa\) for every \(F\). \(\square\)

**Lemma 2.2** (fourth moment). Let \(F\) be finite and \(x_j\in Q\) (\(j\in F\)) with \(\sum_jx_jx_j^*\le\kappa\) and \(\sum_jx_j^*x_j\le\kappa\). Then \(Y=\sum_{j\in F}u_j\otimes x_j\in A_F\otimes Q\) satisfies \((\mu_F\otimes\tau)(|Y|^4)\le2\kappa^2\). Consequently, for \(c>0\), the element \(Y_c=Y1_{[0,c]}(|Y|)\) has \(\|Y_c\|\le c\) and \((\mu_F\otimes\tau)((Y-Y_c)^*(Y-Y_c))\le2\kappa^2/c^2\).

**Proof.** \(|Y|^4=\sum_{j,k,l,m}\overline{u_j}u_k\overline{u_l}u_m\otimes x_j^*x_kx_l^*x_m\). By (1.2) only the terms with \(k=j,m=l\) or \(k=l,m=j\) survive, and the terms with \(j=k=l=m\) belong to both:
\[
(\mu_F\otimes\tau)(|Y|^4)=\sum_{j,l}\tau(x_j^*x_jx_l^*x_l)+\sum_{j,l}\tau(x_j^*x_lx_l^*x_j)-\sum_j\tau(x_j^*x_jx_j^*x_j).
\]
The subtracted terms are nonnegative. With \(S=\sum_jx_j^*x_j\le\kappa\), the first sum is \(\tau(S^2)\le\kappa\tau(S)\le\kappa^2\). The second is \(\tau\big(\sum_jx_j^*R\,x_j\big)\) with \(R=\sum_lx_lx_l^*\le\kappa\), hence at most \(\kappa\tau(S)\le\kappa^2\). Write \(Y=V|Y|\) (polar decomposition). Then \(Y_c=V|Y|1_{[0,c]}(|Y|)\) has norm at most \(c\), and \((Y-Y_c)^*(Y-Y_c)=|Y|^21_{(c,\infty)}(|Y|)\le|Y|^4/c^2\). \(\square\)

**Lemma 2.3** (uniform cut). Let \(h\in L^1(Q,\tau)_+\) and \(c>0\). For every projection \(e\in Q\),
\[
\tau(he)\le c\,\tau(e)+\tau\big(h1_{(c,\infty)}(h)\big).
\]

**Proof.** Write \(h=h_1+h_2\) with \(h_1=h1_{[0,c]}(h)\in Q\), \(0\le h_1\le c\), and \(h_2=h1_{(c,\infty)}(h)\ge0\). By Facts 2.4(b) and 2.6(b) of the measurable operators lesson, \(\tau(h_1e)=\tau(eh_1e)\le c\,\tau(e)\) and \(\tau(h_2e)=\tau(h_2^{1/2}eh_2^{1/2})\le\tau(h_2)\), the last because \(h_2^{1/2}eh_2^{1/2}\le h_2\). \(\square\)

**Theorem 2.4** (binormal states of a finite algebra). Let \(\Psi\) be a binormal state of \(B(K)\) and \(\mathcal T\subset B(K)\) a countable set. There are finite sets \(F_n\) and vectors \(X_n\in L^2(\Omega_{F_n},\mu_{F_n})\otimes K\) such that:

1. \(\langle(1\otimes T)X_n,X_n\rangle\to\Psi(T)\) for every \(T\in\mathcal T\);
2. for every \(\varepsilon>0\) there are \(c>0\) and \(n_0\) such that for every \(n\ge n_0\) some \(Y_n\in A_{F_n}\otimes Q\) satisfies \(\|Y_n\|\le c\) and \(\|X_n-Y_n(1\otimes\eta)\|\le\varepsilon\).

**Proof.** *Normal approximants.* Enumerate \(\mathcal T=\{T_1,T_2,\ldots\}\). Normal states are weak\(^*\)-dense in the state space of \(B(K)\). Otherwise the separation theorem, applied in \(B(K)^*\) with its weak\(^*\) topology, gives a self-adjoint \(T\in B(K)\) with \(\Psi(T)>\sup\omega(T)\) over the normal states \(\omega\); but that supremum is \(\max\operatorname{Sp}T\), which is at least \(\Psi(T)\). For each \(n\), consider the convex set \(\mathcal S_n\subset Q_*\oplus Q_*\oplus\mathbb C^n\) of the triples
\[
\big(\Psi'|_Q-\Psi|_Q,\ \Psi'\circ\rho-\Psi\circ\rho,\ (\Psi'(T_k)-\Psi(T_k))_{k\le n}\big),\qquad\Psi'\text{ a normal state of }B(K).
\]
Along a net of normal states converging weak\(^*\) to \(\Psi\), these triples tend to \(0\) in the weak topology of the Banach space \(Q_*\oplus Q_*\oplus\mathbb C^n\), whose dual is \(Q\oplus Q\oplus\mathbb C^n\). By Mazur's theorem, \(0\) lies in the norm closure of \(\mathcal S_n\): there is a normal state \(\Psi_n\) whose triple has all three components of norm less than \(1/n\).

*The vectors.* Let \(D_n\) be the density of \(\Psi_n\), \((e_j)_{j\in\mathcal I}\) an orthonormal basis of \(K\), and \(b_{n,j}=D_n^{1/2}e_j\). Since \(\sum_j\|b_{n,j}\|^2=\operatorname{Tr}D_n=1\), there is a finite set \(F_n\subset\mathcal I\) with \(\sum_{j\notin F_n}\|b_{n,j}\|^2\le1/n\). Put \(X_n=\sum_{j\in F_n}u_j\otimes b_{n,j}\). By (1.2),
\[
\langle(1\otimes T)X_n,X_n\rangle=\sum_{j\in F_n}\langle Tb_{n,j},b_{n,j}\rangle=\operatorname{Tr}(D_nT)-\sum_{j\notin F_n}\langle Tb_{n,j},b_{n,j}\rangle ,
\]
which differs from \(\Psi_n(T)\) by at most \(\|T\|/n\). Since \(|\Psi_n(T_k)-\Psi(T_k)|<1/n\) for \(k\le n\), this proves (1).

*Densities of the marginals.* Write \(\Psi|_Q=\tau(h\,\cdot)\), \(\Psi\circ\rho=\tau(k\,\cdot)\), \(\Psi_n|_Q=\tau(h_n\,\cdot)\) and \(\Psi_n\circ\rho=\tau(k_n\,\cdot)\) with densities in \(L^1(Q,\tau)_+\). Then \(\|h_n-h\|_1<1/n\), \(\|k_n-k\|_1<1/n\), and \(\tau(h_n)=\tau(k_n)=1\).

*Proof of (2).* Let \(\varepsilon\in(0,1]\) and \(\theta=\varepsilon^4/100\). By Fact 2.4(a), \(\tau(h1_{(c,\infty)}(h))\to0\) as \(c\to\infty\), and likewise for \(k\); choose \(c_0\) with \(\tau(h1_{(c_0,\infty)}(h))+\tau(k1_{(c_0,\infty)}(k))\le\theta/4\). Put \(\kappa=8c_0/\theta+1\), and let \(n_0\ge8/\theta\). For \(n\ge n_0\) let \(E_n=1_{(\kappa,\infty)}(h_n)\), \(E'_n=1_{(\kappa,\infty)}(k_n)\) and \(q_n=(1-E_n)\rho(1-E_n')\), a projection since \(Q\) and \(\rho(Q)\) commute. By the Markov estimate (Fact 2.5(d)), \(\tau(E_n)\le\tau(h_n)/\kappa=1/\kappa\), so Lemma 2.3 gives
\[
\tau(h_nE_n)\le\|h_n-h\|_1+\tau(hE_n)\le\tfrac1n+\tfrac{c_0}\kappa+\tau\big(h1_{(c_0,\infty)}(h)\big),
\]
and the same holds with \(k_n,E'_n,k\). Since \(1-q_n\le E_n+\rho(E_n')\), \(\Psi_n(E_n)=\tau(h_nE_n)\) and \(\Psi_n(\rho(E'_n))=\tau(k_nE'_n)\),
\[
\Psi_n(1-q_n)\le\tfrac2n+\tfrac{2c_0}\kappa+\tfrac\theta4<\tfrac\theta4+\tfrac\theta4+\tfrac\theta4<\theta .
\]
For \(y\in Q_+\), the projection \(\rho(1-E'_n)\) commutes with \((1-E_n)y(1-E_n)\), so \(q_nyq_n\le(1-E_n)y(1-E_n)\). Since \(1-E_n\) commutes with \(h_n\) and \(0\le h_n(1-E_n)\le\kappa\),
\[
\Psi_n(q_nyq_n)\le\tau\big(h_n(1-E_n)y(1-E_n)\big)=\tau\big(h_n(1-E_n)\,y\big)\le\kappa\tau(y).
\]
In the same way, using \(\rho(1-E'_n)\rho(y)\rho(1-E'_n)=\rho\big((1-E'_n)y(1-E'_n)\big)\), we get \(\Psi_n(q_n\rho(y)q_n)\le\kappa\tau(y)\). Apply Proposition 2.1 to the density \(D'_n=q_nD_nq_n\) of \(\Psi_n(q_n\,\cdot\,q_n)\): \(a_{n,j}=D_n'^{1/2}e_j=x_{n,j}\eta\) with \(\sum_jx_{n,j}x_{n,j}^*\le\kappa\) and \(\sum_jx_{n,j}^*x_{n,j}\le\kappa\). For every state \(\omega\) and projection \(q\), \(\|\omega-\omega(q\,\cdot\,q)\|\le2\omega(1-q)^{1/2}\) by the Cauchy–Schwarz inequality. With the Powers–Størmer inequality and (1.2) this gives
\[
\Big\|X_n-\sum_{j\in F_n}u_j\otimes a_{n,j}\Big\|^2=\sum_{j\in F_n}\|b_{n,j}-a_{n,j}\|^2\le\|D_n^{1/2}-D_n'^{1/2}\|_2^2\le\|D_n-D'_n\|_1\le2\theta^{1/2}=\varepsilon^2/5 .
\]
Here \(\sum_{j\in F_n}u_j\otimes a_{n,j}=Y'_n(1\otimes\eta)\) with \(Y'_n=\sum_{j\in F_n}u_j\otimes x_{n,j}\). Lemma 2.2 with \(c=2\sqrt2\,\kappa/\varepsilon\) gives \(Y_n=Y'_{n,c}\) with \(\|Y_n\|\le c\) and \(\|(Y'_n-Y_n)(1\otimes\eta)\|^2=(\mu_{F_n}\otimes\tau)((Y'_n-Y_n)^*(Y'_n-Y_n))\le\varepsilon^2/4\). Hence \(\|X_n-Y_n(1\otimes\eta)\|\le\varepsilon/\sqrt5+\varepsilon/2\le\varepsilon\). The constants \(c\) and \(n_0\) depend only on \(\varepsilon\), \(h\) and \(k\). \(\square\)

## 3. A corner of the continuous core

Let \(M\) be a von Neumann algebra with separable predual and a faithful normal state \(\psi\), in its GNS representation on \(H\) with the notation of Section 1. Following the faithful-state core lesson, let \(\mathcal H=L^2(\mathbb R,H)=L^2(\mathbb R)\otimes H\), with the Fourier transform \((\mathcal Ff)(r)=(2\pi)^{-1/2}\int e^{irs}f(s)\,ds\) on the first factor, and as in (C3)
\[
(\pi(x)f)(s)=\sigma_{-s}(x)f(s),\qquad(\lambda(t)f)(s)=f(s-t),\qquad C=\{\pi(M),\lambda(\mathbb R)\}'' .
\]
Then \(\lambda(t)=e^{itP}\) with \(P=\mathcal F^{-1}M_r\mathcal F\), and \(e_I=1_I(P)\in C\) for an interval \(I\). By (C5), the constant operators \(1\otimes y'\) with \(y'\in M'\) and the unitaries \((V_tf)(s)=\Delta^{it}f(s+t)\) commute with \(C\). The antiunitary involution \((\mathcal Jf)(s)=\Delta^{-is}Jf(-s)\) is defined there as well. Write \(\hat X=1\otimes X\); it commutes with \(P\), and functions of the pair \((P,\hat X)\) are defined by their joint spectral measure on \(\mathbb R^2\). For a bounded interval \(I\), (C7) defines \(b_I(r)=e^{-r/2}1_I(r)\) and the vector \(\eta_I=\mathcal F^{-1}((2\pi)^{-1/2}b_I\,\xi)\), which has the form \(\eta_I=g_I\otimes\xi\) with \(g_I=(2\pi)^{-1/2}\mathcal F^{-1}b_I\in L^2(\mathbb R)\). By Section 3 of that lesson, \(T_I(a)=\langle a\eta_I,\eta_I\rangle\) is a faithful normal finite trace on \(e_ICe_I\), and by (C11)
\[
\mathcal Ja\eta_I=a^*\eta_I\qquad(a\in e_ICe_I).
\tag{3.1}
\]
Formula (C11) is proved there for the linear span \(\mathcal V_I\) of the compressed generators \(e_I\pi(x)\lambda(t)e_I\), which is \(*\)-closed and ultraweakly dense in \(e_ICe_I\). It extends to all of \(e_ICe_I\): if \(a_\alpha\in\mathcal V_I\) converges ultraweakly to \(a\), then \(a_\alpha\eta_I\to a\eta_I\) and \(a_\alpha^*\eta_I\to a^*\eta_I\) weakly, and \(\langle\mathcal Ja_\alpha\eta_I,v\rangle=\overline{\langle a_\alpha\eta_I,\mathcal Jv\rangle}\) for every vector \(v\). Since \(e_I\eta_I=\eta_I\), (3.1) gives \(\mathcal J\eta_I=\eta_I\).

**Lemma 3.1.** For \(x\in M\) and \(t\in\mathbb R\),
\[
\mathcal J\pi(x)\mathcal J=1\otimes JxJ,\qquad\mathcal J\lambda(t)\mathcal J=V_t=e^{it(\hat X-P)} .
\]
Consequently \(\mathcal JC\mathcal J=C'\), and \(\mathcal Je_I\mathcal J=1_I(P-\hat X)\), the spectral projection of the pair \((P,\hat X)\) for \(\{(r,x):r-x\in I\}\).

**Proof.** Put \(g=\pi(x)\mathcal Jf\), so \(g(u)=\sigma_{-u}(x)\Delta^{-iu}Jf(-u)\). Using \(J\Delta^{is}=\Delta^{is}J\) and \(\sigma_s(x)\Delta^{is}=\Delta^{is}x\),
\[
(\mathcal Jg)(s)=\Delta^{-is}J\sigma_s(x)\Delta^{is}Jf(s)=\Delta^{-is}J\Delta^{is}xJf(s)=JxJf(s).
\]
Next \(g=\lambda(t)\mathcal Jf\) has \(g(u)=\Delta^{-i(u-t)}Jf(t-u)\), and
\[
(\mathcal Jg)(s)=\Delta^{-is}J\Delta^{i(s+t)}Jf(s+t)=\Delta^{it}f(s+t)=(V_tf)(s).
\]
Also \((V_tf)(s)=\Delta^{it}(\lambda(-t)f)(s)\), so \(V_t=e^{it\hat X}e^{-itP}=e^{it(\hat X-P)}\). Conjugation by \(\mathcal J\) is a conjugate-linear \(*\)-automorphism of \(B(\mathcal H)\) that preserves the weak operator topology and commutants. Hence \(\mathcal JC\mathcal J\) is the von Neumann algebra generated by the constants \(1\otimes JMJ=1\otimes M'\) and the \(V_t\). This is \(C'\) by the commutant theorem (CCM2), applied with \(G=\mathbb R\), \(U_s=\Delta^{is}\) and \(\alpha=\sigma^\psi\): its right generators are \((\rho_sf)(t)=U_sf(t+s)=(V_sf)(t)\). Finally \(\mathcal J\) is antiunitary, so \(\mathcal Je^{itP}\mathcal J=e^{-itB}\) with \(B=\mathcal JP\mathcal J\) self-adjoint. Comparing with \(e^{it(\hat X-P)}\) for all \(t\) gives \(B=P-\hat X\) by uniqueness of generators, and \(\mathcal J1_I(P)\mathcal J=1_I(B)\). \(\square\)

Fix a bounded open interval \(I\) and put
\[
e=e_I\in C,\qquad e'=\mathcal Je\mathcal J\in C',\qquad p=ee',\qquad K_0=p\mathcal H .
\]
Since \(e'\eta_I=\mathcal Je\mathcal J\eta_I=\mathcal Je\eta_I=\mathcal J\eta_I=\eta_I\), the vector \(\eta_I\) lies in \(K_0\). Every \(a\in eCe\) commutes with \(e\) and with \(e'\in C'\), hence with \(p\), and maps \(K_0\) into itself. Let \(Q_0=\{a|_{K_0}:a\in eCe\}\), \(\eta_0=\eta_I/\|\eta_I\|\) and \(\mathcal J_0=\mathcal J|_{K_0}\).

**Lemma 3.2** (the corner in its trace representation). The restriction \(a\mapsto a|_{K_0}\) is a \(*\)-isomorphism of \(eCe\) onto \(Q_0\), and \(Q_0\) is a von Neumann algebra on \(K_0\). With \(\tau_0(b)=\langle b\eta_0,\eta_0\rangle\), the data \((Q_0,K_0,\tau_0,\eta_0,\mathcal J_0)\) satisfy the hypotheses of Section 2: \(\tau_0\) is a faithful normal tracial state, \(\eta_0\) is cyclic and separating for \(Q_0\), \(\mathcal J_0\) is an antiunitary involution of \(K_0\), \(\mathcal J_0b\eta_0=b^*\eta_0\) and \(Q_0'=\mathcal J_0Q_0\mathcal J_0\).

**Proof.** The projections \(e\) and \(e'\) commute, and \(\mathcal Jp\mathcal J=e'e=p\), so \(\mathcal JK_0=K_0\). By Theorem 5.8(2),(3) of the double commutant lesson, the reduced algebra \(C_e=\{a|_{e\mathcal H}:a\in eCe\}\) is a von Neumann algebra on \(e\mathcal H\) with commutant \((C')_e=\{y'|_{e\mathcal H}:y'\in C'\}\), which contains the projection \(e'|_{e\mathcal H}\). Applying the same theorem to this projection of the commutant of \(C_e\), the algebra \(Q_0\) of restrictions to \(K_0\) is a von Neumann algebra whose commutant is
\[
\{e'y'e'|_{K_0}:y'\in C'\}=\{\mathcal Jeye\mathcal J|_{K_0}:y\in C\}=\mathcal J_0Q_0\mathcal J_0 ,
\]
by Lemma 3.1. If \(a\in eCe\) and \(a|_{K_0}=0\), then \(T_I(a^*a)=\|a\eta_I\|^2=0\), so \(a=0\); thus restriction is a \(*\)-isomorphism. The same computation shows that \(\tau_0\), which is \(T_I/T_I(e)\) transported to \(Q_0\), is a faithful normal tracial state. Equation (3.1) gives \(\mathcal J_0b\eta_0=b^*\eta_0\) for \(b\in Q_0\). If \(\mathcal J_0b\mathcal J_0\eta_0=0\) for some \(b\in Q_0\), then \(b^*\eta_0=\mathcal J_0b\eta_0=0\), so \(\tau_0(bb^*)=0\) and \(b=0\). Thus \(\eta_0\) is separating for \(Q_0'\), hence cyclic for \(Q_0\) by Proposition 9.2 of the double commutant lesson. It is separating for \(Q_0\) because \(\tau_0\) is faithful. \(\square\)

## 4. States at modular energy zero

**Proposition 4.1.** Let \(\Phi\) be a binormal state of \(B(H)\) with \(\Phi(g(X))=g(0)\) for every bounded continuous function \(g\) on \(\mathbb R\). Let \(I=(-1,1)\) in the construction of Section 3, and let \(f\in L^2(\mathbb R)\) be a unit vector whose Fourier transform \(\mathcal Ff\) vanishes outside \([-\frac12,\frac12]\). Let \(W\colon H\to\mathcal H\), \(Wh=f\otimes h\), and \(\tilde\Phi(Z)=\Phi(W^*ZW)\) for \(Z\in B(\mathcal H)\). Then \(\tilde\Phi(p)=1\), and the state \(\Psi(T)=\tilde\Phi(T\oplus0)\) of \(B(K_0)\), where \(T\oplus0\) is \(T\) extended by \(0\) on \(K_0^\perp\), is binormal for \(Q_0\).

**Proof.** \(W^*(S\otimes T)W=\langle Sf,f\rangle T\). First \(W^*eW=\|1_I(P)f\|^2=\int_I|\mathcal Ff|^2=1\). For \(e'=1_I(P-\hat X)\) and \(h\in H\), with \(\nu_h\) the spectral measure of \(X\) at \(h\),
\[
\langle e'Wh,Wh\rangle=\iint1_I(r-x)\,|(\mathcal Ff)(r)|^2\,dr\,d\nu_h(x),
\]
so \(W^*e'W=G(X)\) with \(G(x)=\int1_I(r-x)|(\mathcal Ff)(r)|^2dr\). The function \(G\) takes values in \([0,1]\), is continuous by dominated convergence (the endpoints of \(I+x\) form a null set), and \(G(0)=1\). Hence \(\tilde\Phi(e)=\tilde\Phi(e')=1\), and \(\tilde\Phi(p)=1\) since \(1-p\le(1-e)+(1-e')\). By the Cauchy–Schwarz inequality \(\tilde\Phi(Z)=\tilde\Phi(pZp)\) for all \(Z\), so \(\Psi\) is a state.

*Normality on \(C\).* For \(y'\in M'\), \(Wy'=(1\otimes y')W\). If \(Z\) commutes with \(1\otimes M'\), then \(W^*ZW\) commutes with \(M'\), so it lies in \(M\). As \(C\) commutes with \(1\otimes M'\), \(\tilde\Phi|_C=\Phi|_M\circ W^*(\cdot)W\) is normal.

*Normality on \(C'\).* Let \(U\) be the unitary \((Uf)(s)=\Delta^{-is}f(s)\). Then \(W^*UW=\int|f(s)|^2\Delta^{-is}ds=G_2(X)\) with \(G_2(x)=\int|f(s)|^2e^{-isx}ds\), bounded and continuous with \(G_2(0)=1\), so \(\tilde\Phi(U)=1\). For a state this gives \(\tilde\Phi((1-U)^*(1-U))=2-2\operatorname{Re}\tilde\Phi(U)=0\), and the Cauchy–Schwarz inequality gives \(\tilde\Phi(U^*ZU)=\tilde\Phi(Z)\) for all \(Z\). Now \(U^*(1\otimes y')U\) acts by \(s\mapsto\Delta^{is}y'\Delta^{-is}\in M'\), and \(U^*V_tU=\lambda(-t)\), because \((V_tUf)(s)=\Delta^{it}\Delta^{-i(s+t)}f(s+t)=\Delta^{-is}f(s+t)\). Both commute with \(1\otimes M\). Since \(C'\) is generated by these operators (Lemma 3.1), \(U^*C'U\) commutes with \(1\otimes M\), and as before \(W^*U^*C'UW\subset M'\). Hence \(\tilde\Phi|_{C'}=\Phi|_{M'}\circ W^*U^*(\cdot)UW\) is normal.

*The corner.* For \(a\in eCe\), \(a|_{K_0}\oplus0=ap\), so \(\Psi(a|_{K_0})=\tilde\Phi(ap)=\tilde\Phi(a)\), normal in \(a\). The inverse of the restriction map in Lemma 3.2 is a \(*\)-isomorphism of von Neumann algebras; it preserves the order, hence suprema of bounded increasing nets, so it is normal, and \(\Psi|_{Q_0}\) is normal. For \(b=a|_{K_0}\), \(\mathcal J_0b^*\mathcal J_0=(\mathcal Ja^*\mathcal J)|_{K_0}\), where \(\mathcal Ja^*\mathcal J\in C'\) commutes with \(p\). So \(\Psi(\mathcal J_0b^*\mathcal J_0)=\tilde\Phi(\mathcal Ja^*\mathcal J)\), and \(a\mapsto\mathcal Ja^*\mathcal J\) is a linear normal map of \(C\) onto \(C'\). \(\square\)

**Theorem 4.2** (bounded approximating vectors). Let \(\Phi\) be as in Proposition 4.1, and \(\mathcal T\subset B(H)\) a countable set. There are finite sets \(F_n\) and vectors \(\eta_n\in L^2(\Omega_{F_n},\mu_{F_n})\otimes H\) such that:

1. \(\langle(1\otimes T)\eta_n,\eta_n\rangle\to\Phi(T)\) for every \(T\in\mathcal T\);
2. for every \(\varepsilon>0\) there are \(c>0\) and \(n_0\) such that for every \(n\ge n_0\) some \(y_n\in A_{F_n}\otimes M\) satisfies \(\|y_n\|\le c\) and \(\|\eta_n-y_n(1\otimes\xi)\|\le\varepsilon\).

**Proof.** Let \(p_f\) be the projection onto \(\mathbb Cf\). Apply Theorem 2.4 to \(Q_0\) on \(K_0\) (Lemma 3.2), the binormal state \(\Psi\) of Proposition 4.1, and the countable set of operators \(p(p_f\otimes T)p|_{K_0}\), \(T\in\mathcal T\). We obtain vectors \(X_n\in L^2(\Omega_{F_n})\otimes K_0\). Put \(\eta_n=(1\otimes W^*)X_n\). Since \(WTW^*=p_f\otimes T\), \(X_n\) takes values in \(K_0\), and \(\tilde\Phi(Z)=\tilde\Phi(pZp)\),
\[
\langle(1\otimes T)\eta_n,\eta_n\rangle=\langle(1\otimes p(p_f\otimes T)p)X_n,X_n\rangle\to\tilde\Phi(p(p_f\otimes T)p)=\tilde\Phi(p_f\otimes T)=\Phi(T).
\]
For (2), Theorem 2.4 gives \(Y_n\in A_{F_n}\otimes Q_0\) with \(\|Y_n\|\le c\) and \(\|X_n-Y_n(1\otimes\eta_0)\|\le\varepsilon\) for \(n\ge n_0\). Let \(\tilde Y_n\in A_{F_n}\otimes eCe\) be the element whose values restrict to those of \(Y_n\) (Lemma 3.2); \(\|\tilde Y_n\|=\|Y_n\|\). Write \(\eta_0=g_0\otimes\xi\) with \(g_0=g_I/\|\eta_I\|\), a unit vector of \(L^2(\mathbb R)\), let \(W_0h=g_0\otimes h\), and put
\[
y_n=(1\otimes W^*)\tilde Y_n(1\otimes W_0).
\]
Then \(\|y_n\|\le c\), and \(y_n(1\otimes\xi)=(1\otimes W^*)Y_n(1\otimes\eta_0)\), so \(\|\eta_n-y_n(1\otimes\xi)\|\le\|X_n-Y_n(1\otimes\eta_0)\|\le\varepsilon\). Finally each value \(y_n(\omega)=W^*\tilde Y_n(\omega)W_0\) commutes with \(M'\): \(\tilde Y_n(\omega)\in C\) commutes with \(1\otimes M'\), and \(W\), \(W_0\) intertwine \(M'\) with \(1\otimes M'\). So \(y_n(\omega)\in M\). \(\square\)

## 5. The binormal identity

Now let \(N\subset M\) be an inclusion of von Neumann algebras with a faithful normal conditional expectation \(E\colon M\to N\), \(M\) with separable predual, \(\varphi\) a faithful normal state on \(N\), and \(\psi=\bar\varphi=\varphi\circ E\), with the notation of Section 1; \(\xi\) is the vector \(\bar\xi\) of the first lesson. Let \(e_N\) be the projection onto the closure of \(N\xi\). Then \(e_Ny\xi=E(y)\xi\) for \(y\in M\), because \(\langle y\xi-E(y)\xi,n\xi\rangle=\bar\varphi(n^*y)-\varphi(n^*E(y))=0\) for \(n\in N\) by the bimodule property of \(E\).

**Theorem 5.1** (Marrakchi). Let \(\Phi\) be a state of \(B(H)\) such that

- \(\Phi(y)=\Phi(\rho(y))=\bar\varphi(y)\) for every \(y\in M\);
- \(\Phi(e_N)=1\);
- \(\Phi(g(X))=g(0)\) for every \(g\in C_0(\mathbb R)\).

Then
\[
\Phi(a\rho(b))=\langle a\xi b,\xi\rangle\qquad(a\in\mathrm B(N\subset M,\varphi),\ b\in M).
\]

**Proof.** *Step 0.* The third hypothesis holds for every bounded continuous \(g\). Choose \(g_0\in C_c(\mathbb R)\) with \(0\le g_0\le1\) and \(g_0(0)=1\). Then \(\Phi(1-g_0(X))=0\), so \(\Phi(Z(1-g_0(X)))=0\) for all \(Z\) by the Cauchy–Schwarz inequality, and \(\Phi(g(X))=\Phi(g(X)g_0(X))=(gg_0)(0)=g(0)\), since \(gg_0\in C_0(\mathbb R)\). In particular \(\Phi\) satisfies the hypotheses of Proposition 4.1 and Theorem 4.2.

*Step 1: reduction to analytic \(a\).* Write \(\mathrm B=\mathrm B(N\subset M,\varphi)\); it is a \(\sigma^{\bar\varphi}\)-invariant von Neumann subalgebra of \(M\) (Theorem 2.3 of the first lesson). For \(a\in\mathrm B\) and the Gaussian kernels \(g_k(t)=\sqrt{k/\pi}\,e^{-kt^2}\), the elements \(a_k=\int g_k(t)\sigma^{\bar\varphi}_t(a)\,dt\) lie in \(\mathrm B\), an ultraweakly closed subspace containing every \(\sigma^{\bar\varphi}_t(a)\), and they are entire analytic by Theorem 9.1(3) of the analytic elements lesson. By (B6) and the spectral theorem, \(a_k\xi=\hat g_k(X)a\xi\to a\xi\), where \(\hat g_k(x)=e^{-x^2/4k}\). The right-hand side of the identity is continuous along this sequence, since \(\langle a_k\xi b,\xi\rangle=\langle\rho(b)a_k\xi,\xi\rangle\). So is the left-hand side: by the Cauchy–Schwarz inequality and the first hypothesis,
\[
|\Phi((a_k-a)\rho(b))|=|\Phi(\rho(b)(a_k-a))|\le\|b\|\,\Phi\big((a_k-a)^*(a_k-a)\big)^{1/2}=\|b\|\,\|(a_k-a)\xi\| .
\]
So it suffices to treat entire analytic \(a\in\mathrm B\).

*Step 2: what must be shown.* For entire analytic \(a\in\mathrm B\) put \(D_a=a-\rho(a_+)\in B(H)\). Suppose \(\Phi(D_a^*D_a)=0\). Then for \(b\in M\), by the Cauchy–Schwarz inequality, the first hypothesis and (1.1),
\[
\Phi(a\rho(b))=\Phi(\rho(b)a)=\Phi(\rho(b)\rho(a_+))=\Phi(\rho(a_+b))=\bar\varphi(a_+b)=\langle\rho(a_+b)\xi,\xi\rangle=\langle\rho(b)\rho(a_+)\xi,\xi\rangle=\langle\rho(b)a\xi,\xi\rangle ,
\]
which is the claim. We prove \(\Phi(D_a^*D_a)=0\).

*Step 3: approximating vectors.* Let \(\mathcal T\) consist of \(1\), \(D_a^*D_a\), \(e_N\) and the operators \(g_m(X)\) with \(g_m(x)=\min(1,m|x|)\), \(m\ge1\). Theorem 4.2 gives vectors \(\eta_n\) with \(\|\eta_n\|\to1\), \(\langle(1\otimes e_N)\eta_n,\eta_n\rangle\to1\), \(\langle(1\otimes g_m(X))\eta_n,\eta_n\rangle\to0\) for every \(m\), and \(\|(1\otimes D_a)\eta_n\|^2\to\Phi(D_a^*D_a)\). Consequently \(\|\eta_n-(1\otimes e_N)\eta_n\|^2=\|\eta_n\|^2-\langle(1\otimes e_N)\eta_n,\eta_n\rangle\to0\). If \(\nu_n\) denotes the spectral measure of \(1\otimes X\) at \(\eta_n\), then \(\nu_n(\{|x|\ge1/m\})\to0\) for every \(m\), because \(1_{\{|x|\ge1/m\}}\le g_m\).

Fix \(\varepsilon>0\), and let \(c\), \(n_0\) and \(y_n\in A_{F_n}\otimes M\) be as in Theorem 4.2(2). Choose once and for all \(f_1\in C_c^\infty(\mathbb R)\) with \(0\le f_1\le1\), \(f_1(0)=1\) and \(f_1=0\) outside \([-1,1]\), and let \(k_1\in L^1(\mathbb R)\) with \(f_1(u)=\int k_1(t)e^{itu}dt\); put \(C_0=\|k_1\|_1\). For \(\delta\in(0,1]\) let \(k_\delta(t)=\delta k_1(\delta t)\), so that \(f_\delta(u):=\int k_\delta(t)e^{itu}dt=f_1(u/\delta)\) and \(\|k_\delta\|_1=C_0\). Define \(z_n\in A_{F_n}\otimes N\) by
\[
z_n(\omega)=\int k_\delta(t)\,\sigma^{\bar\varphi}_t\big(E(y_n(\omega))\big)\,dt\qquad(\omega\in\Omega_{F_n}).
\]
Each \(z_n(\omega)\) lies in \(N\), because \(\sigma^{\bar\varphi}_t(N)=N\) by (1.1) of the first lesson. By Lemma 1.2 of the modular averaging lesson, applied to \((M,\bar\varphi)\), \(\|z_n(\omega)\|\le C_0c\) and \(z_n(\omega)\xi=f_\delta(X)E(y_n(\omega))\xi=f_\delta(X)e_Ny_n(\omega)\xi\).

*Step 4: the vectors are close.* Since
\[
\eta_n-z_n(1\otimes\xi)=(1-f_\delta(X))\eta_n+f_\delta(X)(1-e_N)\eta_n+f_\delta(X)e_N\big(\eta_n-y_n(1\otimes\xi)\big),
\]
with all operators acting on the second factor, and \(\|f_\delta(X)\|\le1\), for \(n\ge n_0\)
\[
\|\eta_n-z_n(1\otimes\xi)\|\le\|(1-f_\delta(X))\eta_n\|+\|(1-e_N)\eta_n\|+\varepsilon .
\]
The middle term tends to \(0\). For the first, for every \(m\),
\[
\|(1-f_\delta(X))\eta_n\|^2=\int|1-f_\delta(x)|^2d\nu_n(x)\le\sup_{|x|\le1/m}|1-f_\delta(x)|^2\,\|\eta_n\|^2+\nu_n(\{|x|\ge1/m\}),
\]
whose limit superior in \(n\) is at most \(\sup_{|x|\le1/m}|1-f_\delta(x)|^2\), which tends to \(0\) as \(m\to\infty\). Hence \(\limsup_n\|\eta_n-z_n(1\otimes\xi)\|\le\varepsilon\).

*Step 5: the commutators are small.* Let \(w\in N\) be one of the \(z_n(\omega)\). Its vector \(w\xi\) has \(X\)-spectral support in \([-\delta,\delta]\). Restriction of functionals from \(M\) to \(N\) does not increase norms, and \([w,\bar\varphi]|_N=[w,\varphi]\). So Lemma 1.1 of the modular averaging lesson, in \((M,\bar\varphi)\) with \(s=0\), gives
\[
\|[w,\varphi]\|\le\|[w,\bar\varphi]\|\le2\|(\Delta^{1/2}-1)w\xi\|\le2(e^{\delta/2}-1)\|w\xi\|\le2(e^{\delta/2}-1)C_0c .
\]
For \(t>0\) let \(\epsilon_a(t)\) be the supremum of \(\|[a,v]\|^\sharp_{\bar\varphi}\) over the contractions \(v\in N\) with \(\|[v,\varphi]\|\le t\). By Lemma 2.4 of the first lesson, \(\epsilon_a(t)\to0\) as \(t\to0\). Applied to \(v=w/(C_0c)\), this gives
\[
\|[a,w]\xi\|\le\|[a,w]\|^\sharp_{\bar\varphi}\le r_\delta:=C_0c\,\epsilon_a\big(2(e^{\delta/2}-1)\big).
\]
Since \(\rho(a_+)\) commutes with \(w\) and \(\rho(a_+)\xi=\xi a_+=a\xi\) by (1.1), \(D_aw\xi=aw\xi-wa\xi=[a,w]\xi\). Hence
\[
\|(1\otimes D_a)z_n(1\otimes\xi)\|^2=\sum_\omega\mu_{F_n}(\omega)\|[a,z_n(\omega)]\xi\|^2\le r_\delta^2 .
\]

*Step 6: conclusion.* By Steps 3–5,
\[
\Phi(D_a^*D_a)=\lim_n\|(1\otimes D_a)\eta_n\|^2\le\Big(\|D_a\|\limsup_n\|\eta_n-z_n(1\otimes\xi)\|+r_\delta\Big)^2\le\big(\|D_a\|\varepsilon+r_\delta\big)^2 .
\]
For fixed \(\varepsilon\), hence fixed \(c\), \(r_\delta\to0\) as \(\delta\to0\); then let \(\varepsilon\to0\). So \(\Phi(D_a^*D_a)=0\). \(\square\)

**Remark 5.2.** In [M2] the identity is stated for \(N\) of type III₁ and \(a,b\in\mathrm B(N\subset M,\varphi)\). The proof above uses no assumption on the type of \(N\) and allows every \(b\in M\). It assumes that \(M\) has separable predual, through the faithful-state core lesson.

**Remark 5.3.** For entire analytic \(a\in\mathrm B(N\subset M,\varphi)\), the proof shows \(\Phi(D_a^*D_a)=0\) with \(D_a=a-\rho(a_+)\). By the Cauchy–Schwarz inequality, \(\Phi(Za)=\Phi(Z\rho(a_+))\) for every \(Z\in B(H)\).

## 6. Exercises

**Exercise 6.1.** Show that the vector state of \(\xi\) satisfies the hypotheses of Theorem 5.1, and check its conclusion directly.

**Exercise 6.2.** Show that (1.2) fails for independent uniform signs \(\pm1\) in place of cube roots of unity, and that the fourth-moment bound of Lemma 2.2 still holds for signs with the constant \(3\kappa^2\).

**Exercise 6.3.** In the setting of Section 2, let \(x\in Q\) be nonzero and \(\Psi(T)=\langle Tx\eta,x\eta\rangle/\tau(x^*x)\). Compute the densities of the two marginals of \(\Psi\) and find the smallest \(\kappa\) for which Proposition 2.1 applies.

**Exercise 6.4.** Show that a state \(\Phi\) of \(B(H)\) with \(\Phi(g(X))=g(0)\) for all \(g\in C_0(\mathbb R)\) satisfies \(\Phi(\Delta^{it}Z\Delta^{-it})=\Phi(Z)\) for all \(Z\in B(H)\) and \(t\in\mathbb R\).

## 7. Solutions

**6.1.** \(\langle y\xi,\xi\rangle=\langle\rho(y)\xi,\xi\rangle=\bar\varphi(y)\), \(e_N\xi=\xi\), and \(X\xi=0\) gives \(\langle g(X)\xi,\xi\rangle=g(0)\). The conclusion reads \(\langle a\rho(b)\xi,\xi\rangle=\langle\rho(b)a\xi,\xi\rangle\), which holds because \(a\) and \(\rho(b)\) commute.

**6.2.** For signs \(\varepsilon_j\), \(\int\varepsilon_j\varepsilon_k\varepsilon_l\varepsilon_m=1\) exactly when every index occurs an even number of times. For \(j\ne k\) this includes \((j,k,l,m)=(j,k,j,k)\), for which (1.2) gives \(0\). The fourth moment of \(Y=\sum_j\varepsilon_j\otimes x_j\) is the sum over the three pairings \(\{k=j,m=l\}\), \(\{k=l,m=j\}\) and \(\{l=j,m=k\}\), minus twice the diagonal sum \(\sum_j\tau(x_j^*x_jx_j^*x_j)\ge0\), since the diagonal lies in all three. The first two pairings contribute at most \(\kappa^2\) each, as in Lemma 2.2. The third contributes \(\sum_{j,k}\tau(x_j^*x_kx_j^*x_k)=\sum_{j,k}\tau\big((x_k^*x_j)^*(x_j^*x_k)\big)\), of modulus at most
\[
\Big(\sum_{j,k}\tau(x_j^*x_kx_k^*x_j)\Big)^{1/2}\Big(\sum_{j,k}\tau(x_k^*x_jx_j^*x_k)\Big)^{1/2}\le\kappa^2
\]
by the Cauchy–Schwarz inequality for \(\tau\) and the bound for the second pairing. So the fourth moment is at most \(3\kappa^2\).

**6.3.** \(\Psi(y)=\tau(x^*yx)/\tau(x^*x)=\tau(xx^*y)/\tau(x^*x)\), and \(\Psi(\rho(y))=\langle xy\eta,x\eta\rangle/\tau(x^*x)=\tau(x^*xy)/\tau(x^*x)\). The densities are \(xx^*/\tau(x^*x)\) and \(x^*x/\tau(x^*x)\). For \(h\in Q_+\), \(\tau(hy)\le\kappa\tau(y)\) for all \(y\in Q_+\) exactly when \(h\le\kappa\): test on spectral projections of \(h\). Since \(\|xx^*\|=\|x^*x\|=\|x\|^2\), the smallest admissible constant is \(\kappa=\|x\|^2/\tau(x^*x)\).

**6.4.** By Step 0 of the proof of Theorem 5.1, \(\Phi(g(X))=g(0)\) for the bounded continuous function \(g(x)=e^{itx}\), so \(\Phi(\Delta^{it})=1\). Then \(\Phi((1-\Delta^{it})^*(1-\Delta^{it}))=0\), and the Cauchy–Schwarz inequality gives \(\Phi(\Delta^{it}Z\Delta^{-it})=\Phi(Z)\).

## References

- [M1] A. Marrakchi, Kadison's problem for type III subfactors and the bicentralizer conjecture, Inventiones Mathematicae 239 (2025), 79–163. https://arxiv.org/abs/2308.15163
- [M2] A. Marrakchi, Kadison's problem and ergodicity of the bicentralizer flow (2026). https://arxiv.org/abs/2606.23636
