# Dynamical entropy of C\*-algebras and von Neumann algebras

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. Public domain (CC0).*

## Introduction

Let \(T\) be a measure-preserving transformation of a probability space and \(\xi\) a finite partition. The entropy of
the common refinement of \(\xi,T^{-1}\xi,\dots,T^{-(n-1)}\xi\) grows at most linearly in \(n\), and its growth rate,
maximized over all finite partitions, is the Kolmogorov–Sinai entropy \(h(T)\). Two features make this invariant
useful. Its definition involves no choices. And the Kolmogorov–Sinai theorem computes it from any generating sequence
of partitions, so that in examples one never has to take the supremum.

This lesson builds the same invariant for an automorphism \(\theta\) of a unital C\*-algebra \(A\) that preserves a
state \(\varphi\), and for an automorphism of a von Neumann algebra preserving a normal state. A C\*-algebra need not
contain any nontrivial finite-dimensional subalgebra, so the role of a finite partition is played by a unital
completely positive map \(\gamma\colon D\to A\) from a finite-dimensional C\*-algebra \(D\). The static ingredient,
constructed in the lesson "Entropy defect and abelian models", is a number \(H_\varphi(\gamma_1,\dots,\gamma_n)\)
measuring the information that \(n\) such maps jointly extract from \(\varphi\). We define
\[
h_{\varphi,\theta}(\gamma)=\lim_{n\to\infty}\frac1n H_\varphi(\gamma,\theta\circ\gamma,\dots,\theta^{n-1}\circ\gamma),
\qquad h_\varphi(\theta)=\sup_\gamma h_{\varphi,\theta}(\gamma).
\]
The lesson proves the following.

1. For a nuclear C\*-algebra, \(h_\varphi(\theta)\) is the limit of \(h_{\varphi,\theta}(\tau_\lambda)\) along any
   completely positive approximation \(\tau_\lambda\circ\sigma_\lambda\to\mathrm{id}\) of the identity (Theorem 3.1).
   For an AF algebra it is the limit over finite-dimensional subalgebras \(A_1\subset A_2\subset\cdots\) with dense
   union (Corollary 3.4).
2. \(H_\varphi\) is continuous, uniformly in the number of maps, for the seminorm
   \(\|x\|_\varphi=\varphi(x^*x)^{1/2}\) (Theorem 4.4). This is much stronger than norm continuity.
3. For a unital C\*-algebra \(A\), \(h_\varphi(\theta)\) equals the entropy of the extension of \(\theta\) to the von
   Neumann algebra \(\pi_\varphi(A)''\) (Theorem 5.3). For a hyperfinite von Neumann algebra the entropy is the
   limit along any increasing chain of finite-dimensional subalgebras with dense union (Theorem 5.4).
4. Sections 6 to 8 estimate \(H_\varphi(N_1,\dots,N_k)\) for finite-dimensional subalgebras. There is always the
   upper bound \(S(\varphi|_N)\) when all \(N_j\) lie in a finite-dimensional \(N\) (Lemma 6.1). Equality holds when the
   \(N_j\) contain commuting maximal abelian subalgebras of the centralizer (Theorem 6.2, Corollary 6.4). A lower bound
   with explicit error terms holds when the subalgebras only nearly commute with the modular group (Theorem 8.3).

As an application we compute the entropy of the shift on an infinite tensor product of matrix algebras with a
product state: it is the entropy of the one-site state (Example 6.8). The lesson "Entropy of lattice translations in
quantum spin chains" uses Proposition 1.3, Corollary 3.4 and Lemma 6.1 to show that for Gibbs states of
one-dimensional spin chains the entropy of the lattice translation equals the mean entropy.

**What is assumed.** Section 1 recalls, with precise statements, what we use from the lesson "Entropy defect and
abelian models". The tracial theory of the lessons "Entropy of finite-dimensional subalgebras" and "The entropy of a
trace-preserving automorphism" motivates everything here but is not used in the proofs; for a trace the entropy of
this lesson is compared with the entropy of those lessons in [Connes–Narnhofer–Thirring 1987], and Example 6.8 recovers the value
\(\log n\) for the noncommutative Bernoulli shift. We use completely positive maps, the Kaplansky density theorem,
nuclear C\*-algebras and, from Section 5 on, Tomita–Takesaki theory. The background is listed below in "Results used from other lessons", with the place where each fact is proved.

Basic references are [Connes–Narnhofer–Thirring 1987] and [Connes 1994].

**Conventions.** All C\*-algebras have a unit and subalgebras contain the unit of the ambient algebra; "ucp" means
unital completely positive. We write \(M_d\) for the \(d\times d\) complex matrices with matrix units \(e_{ij}\). A
finite-dimensional C\*-algebra \(C\cong\bigoplus_q M_{n_q}\) carries the trace \(\mathrm{Tr}_C\) that takes the value
\(1\) on minimal projections. A state \(\omega\) of \(C\) has a density \(\rho_\omega\ge0\) with
\(\omega=\mathrm{Tr}_C(\rho_\omega\,\cdot\,)\), and its entropy is
\[
S(\omega)=\mathrm{Tr}_C\,\eta(\rho_\omega),\qquad \eta(t)=-t\log t,\ \eta(0)=0 .
\]
One has \(0\le S(\omega)\le\log\mathrm{Tr}_C(1)\le\log\dim C\). If \(C\) is abelian with minimal projections \(x\),
then \(S(\omega)=\sum_x\eta(\omega(x))\), the entropy of the probability vector \((\omega(x))_x\). For a subalgebra
\(N\) of an algebra \(A\) and a state \(\varphi\) of \(A\) we write \(\varphi|_N\) for the restriction. For a state
\(\varphi\) on \(A\) and \(x\in A\) we put \(\|x\|_\varphi=\varphi(x^*x)^{1/2}\), a seminorm with
\(\|x\|_\varphi\le\|x\|\). For linear maps \(\gamma,\gamma'\colon D\to A\),
\[
\|\gamma-\gamma'\|=\sup_{\|a\|\le1}\|\gamma(a)-\gamma'(a)\|,\qquad
\|\gamma-\gamma'\|_\varphi=\sup_{\|a\|\le1}\|\gamma(a)-\gamma'(a)\|_\varphi .
\]
\(\mathrm{Aut}(A,\varphi)\) denotes the automorphisms \(\theta\) of \(A\) with \(\varphi\circ\theta=\varphi\).

## Results used from other lessons

**(B1) Completely positive maps.** A ucp map \(T\) between C\*-algebras is contractive and satisfies the
Kadison–Schwarz inequality \(T(z)^*T(z)\le T(z^*z)\). A positive map into an abelian C\*-algebra is completely
positive. Compositions of completely positive maps are completely positive, and so are \(a\mapsto r^*\pi(a)r\) for a
\(\ast\)-homomorphism \(\pi\) and \(a\mapsto\omega(a)c\) for a state \(\omega\) and \(c\ge0\). If
\(\gamma\colon M_d\to C\) is completely positive, the matrix \([\gamma(e_{ij})]_{i,j}\in M_d(C)\) is positive.
Proved in Completely positive maps: contractivity and the Kadison–Schwarz inequality are Theorem
4.1(1)–(2), positive maps into abelian algebras are completely positive by Theorem 5.1(1) (which also covers states),
compositions are completely positive by definition, and \(a\mapsto r^*\pi(a)r\) by Theorem 6.1(1) and Example 6.4. The
last statement is Lemma 5.1 of Entropy defect and abelian models.

**(B2) Entropy of finite-dimensional states.** The entropy \(S\) is continuous and concave on the state space of a
C\*-algebra of finite dimension. If \(N\cong M_m\) and \(L\subset N\) is a unital subalgebra with \(L\cong M_{m'}\), then \(m'\)
divides \(m\), the relative commutant \(L^c=L'\cap N\) is isomorphic to \(M_{m/m'}\), and \(N\cong L\otimes L^c\) via
multiplication. For every state \(\omega\) of \(N\) one has subadditivity
\(S(\omega)\le S(\omega|_L)+S(\omega|_{L^c})\), and if \(\omega\) is pure then \(S(\omega|_L)=S(\omega|_{L^c})\).
For densities \(\rho,\rho'\) in a finite-dimensional C\*-algebra with \(\rho'\) invertible, Klein's inequality says
\(\mathrm{Tr}\,\rho(\log\rho-\log\rho')\ge\mathrm{Tr}(\rho-\rho')\). The splitting \(N\cong L\otimes L^c\) is
Projections and types of von Neumann algebras, Proposition 8.4, applied to a matrix unit of \(L\):
the relative commutant is the corner \(eNe\) at a minimal projection \(e\) of \(L\), a full matrix algebra, and the
\(m'\) equivalent projections of the matrix unit split the \(m\)-dimensional space into equal parts, so \(m'\) divides
\(m\). The entropy facts are proved in Entropy defect and abelian models: concavity is Lemma 3.2(b)
there; subadditivity follows from Theorem 2.3 there, because
\(S(\omega|_L)+S(\omega|_{L^c})-S(\omega)=D(\omega\|\omega|_L\otimes\omega|_{L^c})\), and Corollary 2.6(a), which also gives
Klein's inequality as the first estimate in its proof. A pure state is the vector state of some
\(\psi=\sum_{i,j}c_{ij}e_i\otimes f_j\) (its density has rank one, Lemma 3.2(c) there), and the two restrictions have the
densities \(CC^*\) and \((C^*C)^{\mathsf T}\), \(C=(c_{ij})\), with the same nonzero eigenvalues, so their entropies agree
(Lemma 3.2(d) there). Continuity: \(\omega\mapsto\rho_\omega\) is linear on a finite-dimensional space, and
\(\rho\mapsto\mathrm{Tr}\,\eta(\rho)\) is continuous because the continuous functional calculus is continuous in its
argument (C\*-algebras: continuous functional calculus, Theorem 6.1) and \(\eta\) is continuous on
\([0,1]\). A quantitative form for matrix algebras is the Fannes–Audenaert inequality, Operator convex functions and the
continuity of entropy, Theorem 7.1.

**(B3) Nuclear C\*-algebras.** If \(A\) is a unital nuclear C\*-algebra, there are a directed set \(\Lambda\), finite
dimensional C\*-algebras \(D_\lambda\) and ucp maps \(\sigma_\lambda\colon A\to D_\lambda\),
\(\tau_\lambda\colon D_\lambda\to A\) with \(\|\tau_\lambda\sigma_\lambda(a)-a\|\to0\) for every \(a\in A\); if \(A\) is
separable one can take \(\Lambda=\mathbb N\). If \(A\) is separable and nuclear and \(\pi\) is a representation on a
separable Hilbert space, then \(\pi(A)''\) is injective, hence hyperfinite. The C\*-algebra \(B(H)\), \(H\) infinite
dimensional, is not nuclear. The approximation property of a nuclear algebra, with a sequence in the separable case,
is Tensor positivity and nuclearity, Theorem 3.1; injectivity of
\(\pi(A)''\) is Nuclear biduals and extensions, Corollary 3.2;
an injective von Neumann algebra with separable predual is generated by an increasing sequence of finite-dimensional
subalgebras by Injective algebras and separable tracial envelopes, Theorem
3.1. For the last statement see
also [Connes 1976, Theorem 4.1].

**(B4) Density and normal states.** Consider a unital C\*-algebra \(A_0\subset B(H)\). Its strong closure is
\(A_0''\), and \(M_n(A_0)''=M_n(A_0'')\) in \(B(\mathbb C^n\otimes H)\). The Kaplansky density theorem: the unit ball
of \(A_0\) is dense in the unit ball of \(A_0''\) for the strong\* topology. Every normal state \(\varphi\) of a von
Neumann algebra \(M\subset B(H)\) has the form \(\varphi=\sum_n\langle\,\cdot\,\eta_n,\eta_n\rangle\) with
\(\sum_n\|\eta_n\|^2=1\). Proved in The double commutant theorem, Theorem 4.4, Kaplansky's
density theorem and its consequences, Theorem 7.1, and, since a normal state is \(\sigma\)-strongly
continuous (Compact and trace-class operators, Theorem 9.1(ii)), The double commutant theorem,
Theorem 10.1. For the matrix statement: an operator commuting with \(M_n(A_0)\) commutes with the
matrix units, so it is a diagonal operator \(\mathrm{diag}(t,\dots,t)\), and \(t\in A_0'\); and the operators commuting
with all \(\mathrm{diag}(t,\dots,t)\), \(t\in A_0'\), are the matrices with entries in \(A_0''\) by Projections and types of
von Neumann algebras, Lemma 8.2(1).

**(B5) Radon–Nikodym theorem in the commutant.** Let \(A_0\subset B(H)\) be a C\*-algebra, \(\xi\in H\), and \(\psi\)
a positive functional on \(A_0\) with \(\psi(a^*a)\le\langle a^*a\xi,\xi\rangle\) for all \(a\). Then there is
\(t\in A_0'\) with \(0\le t\le1\) and \(\psi(a)=\langle at\xi,\xi\rangle\) for all \(a\in A_0\). On the closure \(K\) of
\(A_0\xi\), which carries the GNS representation of \(\langle\,\cdot\,\xi,\xi\rangle\), this is Representations and positive
functionals, Lemma 8.1(3); take \(t=Tp\), where \(p\in A_0'\) is the projection onto \(K\) and \(T\) the
operator given there.

**(B6) Modular theory.** Fix a faithful normal state \(\varphi\) of a von Neumann algebra \(M\), with GNS space
\(H\) and cyclic separating vector \(\xi\). The closure \(S\) of \(x\xi\mapsto x^*\xi\) has polar
decomposition \(S=J\Delta^{1/2}\); \(J\) is a conjugate-linear isometry with \(J^2=1\), \(J\xi=\xi\) and
\(JMJ=M'\). The modular group \(\sigma^\varphi_t(x)=\Delta^{it}x\Delta^{-it}\) consists of automorphisms of \(M\) with
\(\varphi\circ\sigma^\varphi_t=\varphi\), and it is the only \(\sigma\)-weakly continuous one-parameter automorphism
group for which \(\varphi\) satisfies the KMS condition at inverse temperature \(1\). For real \(\alpha\) we say
\(x\in D(\sigma^\varphi_{i\alpha})\) if \(t\mapsto\sigma^\varphi_t(x)\) extends to a bounded \(\sigma\)-weakly
continuous function on the closed strip between \(\mathbb R\) and \(\mathbb R+i\alpha\), analytic inside; then
\(\sigma^\varphi_{i\alpha}(x)\) is its value at \(i\alpha\), and
\[
x\xi\in D(\Delta^{-\alpha})\quad\text{and}\quad \Delta^{-\alpha}x\xi=\sigma^\varphi_{i\alpha}(x)\xi .
\tag{0.1}
\]
The elements for which \(t\mapsto\sigma^\varphi_t(x)\) extends to an entire function are \(\sigma\)-weakly dense.
The centralizer \(M_\varphi=\{x:\sigma^\varphi_t(x)=x\ \forall t\}\) equals
\(\{x:\varphi(xy)=\varphi(yx)\ \forall y\in M\}\). If \(M\) is finite dimensional and
\(\varphi=\mathrm{Tr}_M(\rho\,\cdot\,)\), then \(\sigma^\varphi_z(x)=\rho^{iz}x\rho^{-iz}\) for all complex \(z\).
For faithful normal states \(\varphi,\psi\) on \(M,N\), the modular operator and conjugation of
\(\varphi\otimes\psi\) on \(M\bar\otimes N\) are \(\Delta_\varphi\otimes\Delta_\psi\) and \(J_\varphi\otimes J_\psi\).
These are proved in the course *Modular theory and weights*: \(JMJ=M'\) in The modular group and its analytic algebra,
§MF-05 and the modular group in §MF-06 there; uniqueness under the KMS condition in The
KMS boundary condition determines the modular group, §KM-05; the centralizer in Fixed
elements and changes of density, §CZ-05. Analytic elements: Analytic elements and
strip arguments, Theorem 9.1, whose part (4) with \(W_t=\Delta^{it}\) and \(W_{ia}\xi=\xi\) gives (0.1),
and whose part (3) gives density. In finite dimension \(\varphi=\mathrm{Tr}_M(\rho\,\cdot\,)\) has
\(\sigma^\varphi_t=\operatorname{Ad}\rho^{it}\) (Recognizing a weight by its fixed density, §PT-04,
since the modular group of the trace is trivial), and \(z\mapsto\rho^{iz}x\rho^{-iz}\) is the entire extension. The
tensor product: Infinite tensor products, Section 6,
where the case of two factors is proved first.

**(B7) Conditional expectations from modular invariance.** Suppose \(\varphi\) is a faithful normal state of \(M\)
and \(N\subset M\) is a von Neumann subalgebra with \(\sigma^\varphi_t(N)=N\) for all \(t\). Then the restriction of
\(\sigma^\varphi\) to \(N\) is the modular group of \(\varphi|_N\), and there is a unique normal conditional
expectation \(E\colon M\to N\) with \(\varphi\circ E=\varphi\). Proved in Conditional expectations from modular
invariance, §§ME-01, ME-08 and ME-10.

**(B8) Type III₁ factors.** Let \(M\) be a factor of type III₁ with separable predual. For faithful normal states
\(\varphi,\psi\) of \(M\) and \(\varepsilon>0\) there is a unitary \(u\in M\) with
\(\|\varphi(u\,\cdot\,u^*)-\psi\|<\varepsilon\) [Connes–Størmer 1978]. Let \(0<\lambda,\lambda'<1\) with
\(\log\lambda/\log\lambda'\) irrational, and let \(\varphi\) be the product state on the infinite tensor product
\(\bigotimes_{k\ge1}M_2\) whose factors alternate between the states with densities
\(\mathrm{diag}(\tfrac1{1+\lambda},\tfrac\lambda{1+\lambda})\) and
\(\mathrm{diag}(\tfrac1{1+\lambda'},\tfrac{\lambda'}{1+\lambda'})\). Then \(R=\pi_\varphi(\bigotimes M_2)''\) is a
hyperfinite factor of type III₁, the extension of \(\varphi\) is faithful, and its modular group acts on the local
algebra \(\bigotimes_{k\le p}M_2\) by \(\mathrm{Ad}(\rho_1^{it}\otimes\cdots\otimes\rho_p^{it})\), where \(\rho_k\) are
the one-site densities. The infinite tensor product is a factor with a faithful normal product state, and its
modular group acts on local algebras as stated: Infinite tensor products, Theorem 5.1, Proposition 5.2 and Theorem
6.1; it is hyperfinite because the local algebras
increase and generate it. For the transitivity statement see [Connes–Størmer 1978]; for the type see [Araki–Woods 1968].

## 1. The entropy of a family of completely positive maps

This section fixes notation and recalls what we use from the lesson "Entropy defect and abelian models". Throughout,
\(\varphi\) is a state of a unital C\*-algebra \(A\), \(D_1,\dots,D_n\) are finite-dimensional C\*-algebras and
\(\gamma_j\colon D_j\to A\) are ucp maps. When \(N\subset A\) is a finite-dimensional subalgebra, "\(N\)" as an
argument of \(H_\varphi\) stands for the inclusion map \(N\to A\).

**Definition 1.1.** An *abelian model* for \((A,\varphi,\gamma_1,\dots,\gamma_n)\) consists of a finite-dimensional
abelian C\*-algebra \(B\), a state \(\mu\) of \(B\), subalgebras \(B_1,\dots,B_n\subset B\), and a ucp map
\(P\colon A\to B\) with \(\mu\circ P=\varphi\). For every \(j\), \(E_j\colon B\to B_j\) denotes a \(\mu\)-preserving
conditional expectation and \(\rho_j=E_j\circ P\circ\gamma_j\colon D_j\to B_j\). The *entropy of the model* is
\[
S\big(\mu|_{B_1\vee\cdots\vee B_n}\big)-\sum_{j=1}^n s_{\mu}(\rho_j),
\]
where \(B_1\vee\cdots\vee B_n\) denotes the subalgebra that the \(B_j\) generate, and where for a ucp map
\(\rho\colon D\to C\) into an abelian algebra with minimal projections \(x\) the *entropy defect* is
\[
s_\mu(\rho)=S(\mu|_C)-S(\mu\circ\rho)+\sum_{x:\ \mu(x)>0}\mu(x)\,S(\rho_x),\qquad \rho(a)=\sum_x\rho_x(a)\,x .
\]
\(H_\varphi(\gamma_1,\dots,\gamma_n)\) is the supremum of the entropies of all abelian models.

These are Definitions 6.1 and 6.2 of the lesson "Entropy defect and abelian models", where the defect of \(\rho_j\) is
taken with respect to \(\mu|_{B_j}\), as in our formula for \(s_\mu\). That lesson writes the defect as
\(s_\mu(\rho)=S(\mu|_C)-\varepsilon_\mu(\rho)\) (its Definition 4.1), where \(\varepsilon_\mu(\rho)\) is the
\(\mu\)-average of the relative entropies of the states \(\rho_x\) with respect to \(\mu\circ\rho\); because
\(\sum_x\mu(x)\rho_x=\mu\circ\rho\), this average equals \(S(\mu\circ\rho)-\sum_x\mu(x)S(\rho_x)\) (its Theorem 4.5(a)),
and the two expressions for the defect agree. The value of \(E_j\) on minimal projections of \(B\) of measure zero is not
determined, but it plays no role, as the following unfolded form shows.

**The entropy of a model, unfolded.** Let \(Y\) be the set of minimal projections of \(B\). A positive unital map
into \(B\) is the same as a family of states: \(P(a)=\sum_{b\in Y}\omega_b(a)\,b\), and \(\mu\circ P=\varphi\) means
\[
\varphi=\sum_{b\in Y}\mu(b)\,\omega_b .
\tag{1.1}
\]
Each minimal projection \(x\) of \(B_j\) is the sum of the \(b\in Y\) below it, so \(B_j\) is the same as a partition
of \(Y\). For \(x\in X_j\), the set of minimal projections of \(B_j\), with \(\mu(x)>0\), put
\[
\varphi_{j,x}=\frac1{\mu(x)}\sum_{b\le x}\mu(b)\,\omega_b\circ\gamma_j ,
\]
a state of \(D_j\). Then \(\rho_j(a)=\sum_x\varphi_{j,x}(a)x\) up to terms of measure zero, and
\(\mu\circ\rho_j=\varphi\circ\gamma_j\). Hence the entropy of the model is
\[
\underbrace{S\big(\mu|_{\bigvee_j B_j}\big)-\sum_{j}S(\mu|_{B_j})}_{\le 0}
\;+\;\sum_{j}\underbrace{\Big(S(\varphi\circ\gamma_j)-\sum_{x\in X_j,\ \mu(x)>0}\mu(x)\,S(\varphi_{j,x})\Big)}_{=:\chi_j\in[0,\,S(\varphi\circ\gamma_j)]}.
\tag{1.2}
\]
This is Proposition 6.3 of the lesson "Entropy defect and abelian models". The first bracket is \(\le0\) by
subadditivity of classical entropy, and \(\chi_j\ge0\) by concavity of \(S\) (B2), since
\(\varphi\circ\gamma_j=\sum_x\mu(x)\varphi_{j,x}\). Formula (1.2) involves the states \(\omega_b\) only for
\(\mu(b)>0\). Conversely, any finite decomposition (1.1) of \(\varphi\) into states, together with \(n\) partitions of
the index set \(Y\), is an abelian model with \(B=\mathbb C^Y\). An abelian model does not involve the maps
\(\gamma_j\) at all; only its entropy depends on them.

We need one function that measures the uniform continuity of entropy. For an integer \(D\ge1\) and \(\varepsilon\ge0\)
let
\[
F_D(\varepsilon)=\sup\big\{|S(\omega)-S(\omega')|\ :\ \omega,\omega'\ \text{states of a C}^*\text{-algebra }C,\
\dim C\le D,\ \|\omega-\omega'\|\le\varepsilon\big\}.
\]

**Lemma 1.2.** \(F_D\) is nondecreasing, \(F_D\le\log D\), and \(F_D(\varepsilon)\to0\) as \(\varepsilon\to0\).

*Proof.* Monotonicity is clear, and \(F_D\le\log D\) because \(0\le S\le\log\dim C\). Up to isomorphism there are
finitely many C\*-algebras of dimension at most \(D\), and isomorphisms preserve both \(S\) and the norm distance of
states. For each of them the state space is compact and \(S\) is continuous on it (B2), hence uniformly continuous.
Taking the worst of finitely many moduli of continuity gives \(F_D(\varepsilon)\to0\). \(\square\)

For matrix algebras an explicit bound is the Fannes–Audenaert inequality (Operator convex functions and the
continuity of entropy, Theorem 7.1); we never need it.

**Proposition 1.3.** Let \(\gamma_j\colon D_j\to A\) be ucp, \(j=1,\dots,n\).

(a) \(0\le H_\varphi(\gamma_1,\dots,\gamma_n)\le\sum_jS(\varphi\circ\gamma_j)\le\sum_j\log\dim D_j\).

(b) *Monotonicity.* If \(\kappa_j\colon D_j'\to D_j\) are ucp, then
\(H_\varphi(\gamma_1\circ\kappa_1,\dots,\gamma_n\circ\kappa_n)\le H_\varphi(\gamma_1,\dots,\gamma_n)\).

(c) *Invariance.* If \(\kappa\colon A\to A\) is ucp with \(\varphi\circ\kappa=\varphi\), then
\(H_\varphi(\kappa\circ\gamma_1,\dots,\kappa\circ\gamma_n)\le H_\varphi(\gamma_1,\dots,\gamma_n)\), with equality
when \(\kappa\in\mathrm{Aut}(A,\varphi)\). More generally, if \(\sigma\colon A\to A'\) is a \(\ast\)-isomorphism, then
\(H_{\varphi\circ\sigma^{-1}}(\sigma\circ\gamma_1,\dots,\sigma\circ\gamma_n)=H_\varphi(\gamma_1,\dots,\gamma_n)\).

(d) *Repetition.* \(H_\varphi\) is unchanged by permuting the \(\gamma_j\), and
\(H_\varphi(\gamma_1,\dots,\gamma_n,\gamma_n)=H_\varphi(\gamma_1,\dots,\gamma_n)\).

(e) *Subadditivity.* For two families \(X=(\gamma_1,\dots,\gamma_k)\) and \(Y=(\gamma_{k+1},\dots,\gamma_n)\),
\(\max\{H_\varphi(X),H_\varphi(Y)\}\le H_\varphi(X,Y)\le H_\varphi(X)+H_\varphi(Y)\).

(f) *Norm continuity.* If \(\gamma_j'\colon D_j\to A\) are ucp, \(\dim D_j\le D\) and
\(\|\gamma_j-\gamma_j'\|\le\varepsilon\) for all \(j\), then
\(|H_\varphi(\gamma_1,\dots,\gamma_n)-H_\varphi(\gamma_1',\dots,\gamma_n')|\le2nF_D(\varepsilon)\).

(g) *Continuity of the defect.* If \(C\) is a finite-dimensional abelian C\*-algebra with a state \(\mu\), \(D_1\) a
C\*-algebra with \(\dim D_1\le D\), and \(\rho,\rho'\colon D_1\to C\) are ucp with \(\|\rho-\rho'\|\le\varepsilon\), then
\(|s_\mu(\rho)-s_\mu(\rho')|\le2F_D(\varepsilon)\).

*Proof.* Statements (b), (d) and the right inequality in (e) are Theorem 7.1(a), (c) and (d) of the lesson "Entropy
defect and abelian models". There, (b) rests on the monotonicity of relative entropy under ucp maps, (d) on its
Theorem 4.7 (the defect of a join), and the right inequality of (e) on the subadditivity of classical entropy. The
remaining statements follow directly from (1.2), and we give the arguments. Statement (a) is also Proposition 6.3
there, the first half of (c) is its Theorem 7.1(b), and (f), (g) are its Theorem 8.3 and Lemma 8.2 with an explicit
modulus in place of \(F_D\).

(a) The model \(B=\mathbb C\) has entropy \(0\). The upper bound is (1.2) with the signs noted there.

(c) If \((B,\mu,(B_j),P)\) is a model for \(\varphi\), then \((B,\mu,(B_j),P\circ\kappa)\) is a model for
\(\varphi\) as well, since \(\mu\circ P\circ\kappa=\varphi\circ\kappa=\varphi\). The entropy of the second model for
\((\gamma_j)\) equals the entropy of the first for \((\kappa\circ\gamma_j)\), because the states \(\varphi_{j,x}\) are
built from \(P\circ\kappa\circ\gamma_j\) in both cases. This gives the inequality. For an automorphism apply it also
to \(\kappa^{-1}\). For an isomorphism \(\sigma\), models \(P\) of \((A',\varphi\circ\sigma^{-1})\) correspond to models
\(P\circ\sigma\) of \((A,\varphi)\), again with the same states \(\varphi_{j,x}\).

(e), left inequality. A model for \(X\) becomes a model for \((X,Y)\) by putting \(B_j=\mathbb C\) for the indices of
\(Y\). These contribute \(\chi_j=S(\varphi\circ\gamma_j)-S(\varphi\circ\gamma_j)=0\) and do not change
\(\bigvee B_j\).

(g) By definition \(s_\mu(\rho)-s_\mu(\rho')=S(\mu\circ\rho')-S(\mu\circ\rho)+\sum_x\mu(x)\big(S(\rho_x)-S(\rho'_x)\big)\), and
\(\|\mu\circ\rho-\mu\circ\rho'\|\le\varepsilon\), \(\|\rho_x-\rho'_x\|\le\varepsilon\) for every \(x\).

(f) Fix a model. For \(\|a\|\le1\),
\(|\varphi_{j,x}(a)-\varphi'_{j,x}(a)|\le\mu(x)^{-1}\sum_{b\le x}\mu(b)|\omega_b(\gamma_j(a)-\gamma_j'(a))|\le\varepsilon\),
and likewise \(\|\varphi\circ\gamma_j-\varphi\circ\gamma_j'\|\le\varepsilon\). By (1.2) and the definition of
\(F_D\), the entropies of the model for \((\gamma_j)\) and for \((\gamma_j')\) differ by at most
\(\sum_j\big(F_D(\varepsilon)+\sum_x\mu(x)F_D(\varepsilon)\big)=2nF_D(\varepsilon)\). Take suprema. \(\square\)

The next lemma shows that matrix algebras suffice as domains.

**Lemma 1.4.** Let \(D=\bigoplus_{q}M_{n_q}\) sit block diagonally in \(M_m\), \(m=\sum_qn_q\), and let
\(E_D\colon M_m\to D\) be the compression to the diagonal blocks, a ucp map with \(E_D|_D=\mathrm{id}\). If
\(\gamma_1,\gamma_1'\colon D\to A\) are ucp, then
\(H_\varphi(\gamma_1\circ E_D,\gamma_2,\dots,\gamma_n)=H_\varphi(\gamma_1,\gamma_2,\dots,\gamma_n)\). Moreover
\(\|\gamma_1E_D-\gamma_1'E_D\|_\varphi\le\|\gamma_1-\gamma_1'\|_\varphi\) and the same for \(\|\cdot\|\).

*Proof.* By Proposition 1.3(b), \(H_\varphi(\gamma_1E_D,\dots)\le H_\varphi(\gamma_1,\dots)\), and
\(H_\varphi(\gamma_1,\dots)=H_\varphi(\gamma_1E_D\iota,\dots)\le H_\varphi(\gamma_1E_D,\dots)\) where
\(\iota\colon D\to M_m\) is the inclusion, since \(E_D\iota=\mathrm{id}_D\). The norm estimates hold because \(E_D\)
maps the unit ball into the unit ball. \(\square\)

## 2. The dynamical entropy

Let \(\theta\in\mathrm{Aut}(A,\varphi)\) and let \(\gamma\colon D\to A\) be ucp with \(D\) finite dimensional. Put
\[
a_n(\gamma)=H_\varphi(\gamma,\theta\circ\gamma,\dots,\theta^{n-1}\circ\gamma).
\]

**Lemma 2.1.** The sequence \(a_n(\gamma)\) is subadditive, and
\(\lim_n a_n(\gamma)/n=\inf_na_n(\gamma)/n\) exists and lies in \([0,S(\varphi\circ\gamma)]\).

*Proof.* By Proposition 1.3(e) and then (c) applied to the automorphism \(\theta^n\),
\[
a_{n+m}\le a_n+H_\varphi(\theta^n\gamma,\dots,\theta^{n+m-1}\gamma)=a_n+a_m .
\]
Fekete's lemma applies to a nonnegative subadditive sequence: fix \(k\) and write \(n=qk+r\) with \(0\le r<k\); then
\(a_n\le qa_k+a_r\), so \(\limsup_n a_n/n\le a_k/k\) for every \(k\), which forces
\(\lim a_n/n=\inf_k a_k/k\). Finally \(0\le a_1\le S(\varphi\circ\gamma)\) by Proposition 1.3(a). \(\square\)

**Definition 2.2.** The *entropy of \(\gamma\) under \(\theta\)* is
\(h_{\varphi,\theta}(\gamma)=\lim_na_n(\gamma)/n\). For a finite-dimensional subalgebra \(N\subset A\) we write
\(h_{\varphi,\theta}(N)\) for the entropy of the inclusion. The *dynamical entropy* of \(\theta\) is
\[
h_\varphi(\theta)=\sup\{h_{\varphi,\theta}(\gamma)\ :\ \gamma\colon D\to A\ \text{ucp},\ D\ \text{finite
dimensional}\}\in[0,\infty].
\]

By Lemma 1.4, applied to each of the maps \(\theta^i\circ\gamma\), one has \(h_{\varphi,\theta}(\gamma\circ E_D)=
h_{\varphi,\theta}(\gamma)\). So it makes no difference whether the supremum runs over all finite-dimensional domains
or over matrix algebras \(M_d\) only. The same remark applies to all the approximation theorems below.

**Proposition 2.3.** Let \(\theta\in\mathrm{Aut}(A,\varphi)\).

(a) If \(\kappa\colon D'\to D\) is ucp, then \(h_{\varphi,\theta}(\gamma\circ\kappa)\le h_{\varphi,\theta}(\gamma)\).
In particular, if \(\gamma\) takes values in a finite-dimensional subalgebra \(N\), then
\(h_{\varphi,\theta}(\gamma)\le h_{\varphi,\theta}(N)\), and \(N\subset N'\) implies
\(h_{\varphi,\theta}(N)\le h_{\varphi,\theta}(N')\).

(b) If \(\gamma,\gamma'\colon D\to A\) are ucp and \(\dim D\le d\), then
\(|h_{\varphi,\theta}(\gamma)-h_{\varphi,\theta}(\gamma')|\le2F_d(\|\gamma-\gamma'\|)\).

(c) *Covariance.* If \(\sigma\colon A\to A'\) is a \(\ast\)-isomorphism, then
\(h_{\varphi\circ\sigma^{-1}}(\sigma\theta\sigma^{-1})=h_\varphi(\theta)\). In particular
\(h_{\varphi\circ\sigma}(\sigma^{-1}\theta\sigma)=h_\varphi(\theta)\) for \(\sigma\in\mathrm{Aut}(A)\).

(d) If \(A\) is finite dimensional, then \(h_\varphi(\theta)=0\).

*Proof.* (a) Apply Proposition 1.3(b) with \(\kappa_j=\kappa\) to the family \((\theta^i\gamma)_i\). If
\(\gamma=\iota_N\circ\bar\gamma\) with \(\iota_N\) the inclusion, this gives the second statement, and
\(\iota_N=\iota_{N'}\circ(N\hookrightarrow N')\) the third.

(b) \(\|\theta^i\gamma-\theta^i\gamma'\|=\|\gamma-\gamma'\|\), so Proposition 1.3(f) gives
\(|a_n(\gamma)-a_n(\gamma')|\le2nF_d(\|\gamma-\gamma'\|)\). Divide by \(n\).

(c) \((\sigma\theta\sigma^{-1})^i\circ\sigma\gamma=\sigma\circ\theta^i\gamma\), so Proposition 1.3(c) gives
\(a_n\) equal for \((\varphi,\theta,\gamma)\) and \((\varphi\sigma^{-1},\sigma\theta\sigma^{-1},\sigma\gamma)\). As
\(\gamma\mapsto\sigma\gamma\) is a bijection between ucp maps into \(A\) and into \(A'\), the suprema agree.

(d) \(\theta^i\gamma=\mathrm{id}_A\circ(\theta^i\gamma)\), so by Proposition 1.3(b), (d) and (a),
\(a_n(\gamma)\le H_\varphi(\mathrm{id}_A,\dots,\mathrm{id}_A)=H_\varphi(\mathrm{id}_A)\le S(\varphi)\). Hence
\(a_n/n\to0\). \(\square\)

Part (d) is the reason why positive entropy needs an infinite system: finite quantum systems, like classical systems
with finitely many states, have zero entropy.

## 3. A Kolmogorov–Sinai theorem for nuclear C\*-algebras

The definition of \(h_\varphi(\theta)\) takes a supremum over all ucp maps from all finite-dimensional algebras. The
following theorem replaces it by a limit along any approximation of the identity of \(A\) through finite-dimensional
algebras. The approximating maps need not preserve \(\varphi\).

**Theorem 3.1.** Let \(\theta\in\mathrm{Aut}(A,\varphi)\). Let \((D_\lambda)_{\lambda\in\Lambda}\) be a net of
finite-dimensional C\*-algebras and \(\tau_\lambda\colon D_\lambda\to A\), \(\sigma_\lambda\colon A\to D_\lambda\) ucp
maps with \(\tau_\lambda\sigma_\lambda(a)\to a\) in norm for every \(a\in A\). Then
\[
h_\varphi(\theta)=\lim_\lambda h_{\varphi,\theta}(\tau_\lambda).
\]

*Proof.* Each \(h_{\varphi,\theta}(\tau_\lambda)\le h_\varphi(\theta)\) by definition, so it suffices to show
\(\liminf_\lambda h_{\varphi,\theta}(\tau_\lambda)\ge h_{\varphi,\theta}(\gamma)\) for every ucp
\(\gamma\colon D\to A\) with \(D\) finite dimensional. Put \(\gamma_\lambda=\tau_\lambda\sigma_\lambda\gamma\). Choose a
basis \(d_1,\dots,d_N\) of \(D\); there is \(c>0\) with \(\sum_k|t_k|\le c\) whenever \(\|\sum_kt_kd_k\|\le1\), as all
norms on \(D\) are equivalent. Then
\[
\varepsilon_\lambda:=\|\gamma_\lambda-\gamma\|\le c\max_k\|\tau_\lambda\sigma_\lambda(\gamma(d_k))-\gamma(d_k)\|\to0 .
\]
By Proposition 2.3(b), \(h_{\varphi,\theta}(\gamma)\le h_{\varphi,\theta}(\gamma_\lambda)+2F_{\dim D}(\varepsilon_\lambda)\),
and by Proposition 2.3(a) applied to \(\kappa=\sigma_\lambda\gamma\colon D\to D_\lambda\),
\(h_{\varphi,\theta}(\gamma_\lambda)=h_{\varphi,\theta}(\tau_\lambda\circ\kappa)\le h_{\varphi,\theta}(\tau_\lambda)\).
Since \(F_{\dim D}(\varepsilon_\lambda)\to0\) by Lemma 1.2, the claim follows. \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987].

**Corollary 3.2.** If \(A\) is nuclear, then for every \(\theta\in\mathrm{Aut}(A,\varphi)\) and every net as in
(B3), \(h_\varphi(\theta)=\lim_\lambda h_{\varphi,\theta}(\tau_\lambda)\). If moreover \(A\) is separable, the net can
be taken to be a sequence. \(\square\)

For AF algebras there is a simpler route, which works with inclusions of subalgebras and which we shall use again for
von Neumann algebras. It rests on a concrete description of ucp maps from matrix algebras.

**Lemma 3.3 (Choi columns).** Fix a state \(\omega\) of \(M_d\) and a unital C\*-algebra \(C\). For a
\(d\times d\) array \(c=(c_{ki})\) of elements of \(C\) put \(T_c=\sum_{k,i}c_{ki}^*c_{ki}\), and when \(T_c\le1\)
define
\[
\gamma_c(a)=\sum_{i,j,k}a_{ij}\,c_{ki}^*c_{kj}+\omega(a)(1-T_c),\qquad a=[a_{ij}]\in M_d .
\tag{3.1}
\]

(a) \(\gamma_c\) is a ucp map from \(M_d\) into the C\*-algebra generated by \(1\) and the \(c_{ki}\). Every ucp map
\(\gamma\colon M_d\to C\) is of the form \(\gamma=\gamma_v\) for an array \(v\) with \(T_v=1\).

(b) Let \(\mathrm{Col}(c)\in M_{d^2}(C)\) be the matrix whose first column lists the \(c_{ki}\) (in some fixed order)
and whose other entries are \(0\). Then \(\mathrm{Col}(c)^*\mathrm{Col}(c)=T_c\otimes e_{11}\), so \(T_c\le1\) if and
only if \(\|\mathrm{Col}(c)\|\le1\).

(c) If \(T_c,T_{c'}\le1\) and \(\|c_{ki}-c'_{ki}\|\le\delta\) for all \(k,i\), then
\(\|\gamma_c-\gamma_{c'}\|\le4d^3\delta\).

(d) Let \(C\subset B(H)\). If \(c\) and \((c^\lambda)\) are arrays with \(T_c\le1\), \(T_{c^\lambda}\le1\) and
\(c^\lambda_{ki}\to c_{ki}\) in the strong\* topology for all \(k,i\), then for every \(\zeta\in H\)
\[
\sup_{\|a\|\le1}\|(\gamma_{c^\lambda}(a)-\gamma_c(a))\zeta\|\to0 .
\]

*Proof.* (a) Let \(R_k\in M_{d,1}(C)\) be the column \((c_{k1},\dots,c_{kd})^{\mathsf T}\). Then
\(R_k^*(a\otimes1)R_k=\sum_{i,j}a_{ij}c_{ki}^*c_{kj}\), so the first term of (3.1) is a sum of maps
\(a\mapsto R_k^*(a\otimes1)R_k\), which are completely positive (B1). The second term is completely positive because
\(\omega\) is a state and \(1-T_c\ge0\). At \(a=1\) the sum is \(T_c+1-T_c=1\). Conversely, let \(\gamma\) be ucp. The
matrix \(X=[\gamma(e_{ij})]\) is positive (B1); let \(v=X^{1/2}\in M_d(C)\), viewed as the array \(v_{ki}\). Since
\(v\) is self-adjoint, \(\gamma(e_{ij})=X_{ij}=(v^*v)_{ij}=\sum_kv_{ki}^*v_{kj}\), and
\(T_v=\sum_iX_{ii}=\gamma(1)=1\). So \(\gamma=\gamma_v\).

(b) is matrix multiplication.

(c) Each \(\|c_{ki}\|\le1\), as \(c_{ki}^*c_{ki}\le T_c\le1\). Hence
\(\|c_{ki}^*c_{kj}-c'^*_{ki}c'_{kj}\|\le\|c_{ki}^*-c'^*_{ki}\|\|c_{kj}\|+\|c'_{ki}\|\|c_{kj}-c'_{kj}\|\le2\delta\),
and \(\|T_c-T_{c'}\|\le2d^2\delta\). For \(\|a\|\le1\) all \(|a_{ij}|\le1\) and \(|\omega(a)|\le1\), so
\(\|\gamma_c(a)-\gamma_{c'}(a)\|\le d^2\cdot2d\delta+2d^2\delta\le4d^3\delta\).

(d) For bounded nets, \(s_\lambda\to s\) and \(t_\lambda\to t\) strong\* imply \(s_\lambda^*t_\lambda\to s^*t\)
strongly: \((s_\lambda^*t_\lambda-s^*t)\zeta=s_\lambda^*(t_\lambda-t)\zeta+(s_\lambda^*-s^*)t\zeta\). Hence
\(\gamma_{c^\lambda}(e_{ij})\zeta\to\gamma_c(e_{ij})\zeta\) for all \(i,j\), and for \(\|a\|\le1\),
\(\|(\gamma_{c^\lambda}(a)-\gamma_c(a))\zeta\|\le\sum_{i,j}\|(\gamma_{c^\lambda}(e_{ij})-\gamma_c(e_{ij}))\zeta\|\).
\(\square\)

**Corollary 3.4 (AF algebras).** Let \((A_k)\) be an increasing net of finite-dimensional subalgebras of \(A\) whose
union is norm dense. Then for every state \(\varphi\) and \(\theta\in\mathrm{Aut}(A,\varphi)\),
\[
h_\varphi(\theta)=\lim_kh_{\varphi,\theta}(A_k)=\sup_kh_{\varphi,\theta}(A_k).
\]

*Proof.* The net \(h_{\varphi,\theta}(A_k)\) is nondecreasing by Proposition 2.3(a) and bounded by
\(h_\varphi(\theta)\). Let \(\gamma\colon M_d\to A\) be ucp (matrix algebras suffice by Lemma 1.4) and \(\eta>0\). By
Lemma 3.3(a), \(\gamma=\gamma_v\) with \(\|\mathrm{Col}(v)\|=1\). Since the union of the \(M_{d^2}(A_k)\) is dense in
\(M_{d^2}(A)\) and the net is increasing, there are \(k\) and \(Y\in M_{d^2}(A_k)\) with
\(\|Y-\mathrm{Col}(v)\|\le\eta\). Keep only the first column of \(Y\) and divide by \(1+\eta\): the result is
\(\mathrm{Col}(c)\) for an array \(c\) in \(A_k\) with \(\|\mathrm{Col}(c)\|\le1\) and entries within \(2\eta\) of
those of \(v\). By Lemma 3.3, \(\gamma_c\) is a ucp map into \(A_k\) with \(\|\gamma_c-\gamma\|\le8d^3\eta\). By
Proposition 2.3(b) and (a),
\[
h_{\varphi,\theta}(\gamma)\le h_{\varphi,\theta}(\gamma_c)+2F_{d^2}(8d^3\eta)\le
h_{\varphi,\theta}(A_k)+2F_{d^2}(8d^3\eta).
\]
Let \(\eta\to0\) and use Lemma 1.2. \(\square\)

One can also deduce Corollary 3.4 from Theorem 3.1: by the Arveson extension theorem the identity of \(A_k\) extends to
a ucp map \(A\to M_m\supset A_k\), and composing with the compression \(M_m\to A_k\) of Lemma 1.4 gives a ucp map
\(\sigma_k\colon A\to A_k\) that fixes \(A_k\); then, for every \(b\in A_k\), \(\|\sigma_k(a)-a\|\le\|\sigma_k(a-b)\|+\|b-a\|\le2\|a-b\|\), because a ucp map
is contractive and \(\sigma_k(b)=b\); so \(\|\sigma_k(a)-a\|\le2\,\mathrm{dist}(a,A_k)\to0\).
The value of Corollary 3.4 is that it computes an entropy defined by a supremum over all ucp maps through a single
increasing sequence of subalgebras. Example 6.8 below uses it to compute the entropy of shifts.

## 4. Continuity for the seminorm of the state

Proposition 1.3(f) controls \(H_\varphi\) when the maps move a little in norm. For von Neumann algebras this is useless,
because elements of a von Neumann algebra are approximated by elements of a dense subalgebra only in the strong
topology, that is, in the seminorms \(\|\cdot\|_\varphi\) of normal states. This section proves that \(H_\varphi\) is
continuous for \(\|\cdot\|_\varphi\), with a modulus that depends on the size of the domains but not on the number of
maps or on \(A\). A reference for this section is [Connes–Narnhofer–Thirring 1987].

Two ingredients are needed. The first is that an abelian model can be replaced, at a small and controlled cost, by a
model whose subalgebras \(B_j\) have a bounded number of minimal projections. The second is that for such small models
the entropy defect depends continuously on the map in the seminorm of \(\mu\).

We start with a classical fact. For finite sets \(X_1,\dots,X_n\) and a probability \(\nu\) on \(\prod_jX_j\) with
marginals \(\nu_j\), the *multi-information* is \(I(\nu)=\sum_jH(\nu_j)-H(\nu)\), where \(H\) is the Shannon entropy.

**Lemma 4.1.** Let \(f_j\colon X_j\to Z_j\) be maps and \(f=\prod_jf_j\). Then \(I(f_*\nu)\le I(\nu)\).

*Proof.* The *log-sum inequality* says that for \(p_1,\dots,p_r\ge0\) and \(q_1,\dots,q_r>0\),
\(\sum_lp_l\log(p_l/q_l)\ge p\log(p/q)\) with \(p=\sum p_l\), \(q=\sum q_l\): this is Jensen's inequality for the convex
function \(t\log t\) and the weights \(q_l/q\) at the points \(p_l/q_l\). For probabilities \(\alpha,\beta\) on a finite
set with \(\beta(y)>0\) whenever \(\alpha(y)>0\) put \(K(\alpha\|\beta)=\sum_y\alpha(y)\log(\alpha(y)/\beta(y))\).
Grouping the points of \(\prod X_j\) by their image under \(f\) and applying the log-sum inequality to each group gives
\(K(f_*\alpha\|f_*\beta)\le K(\alpha\|\beta)\). Now \(I(\nu)=K(\nu\|\nu_1\otimes\cdots\otimes\nu_n)\): indeed
\(\sum_y\nu(y)\log\nu(y)=-H(\nu)\) and \(-\sum_y\nu(y)\log\prod_j\nu_j(y_j)=\sum_jH(\nu_j)\). Since
\(f_*(\nu_1\otimes\cdots\otimes\nu_n)=f_{1*}\nu_1\otimes\cdots\otimes f_{n*}\nu_n\), and the \(f_{j*}\nu_j\) are the
marginals of \(f_*\nu\), the claim follows. \(\square\)

For \(\varepsilon>0\) let \(r(d,\varepsilon)\) be the least number of pieces into which the state space of \(M_d\)
can be cut so that each piece has norm diameter at most \(\varepsilon\). It is finite: cover the compact state space by
finitely many open balls of radius \(\varepsilon/2\) and make the cover disjoint. The *size* of a model
\((B,\mu,(B_j),P)\) is the largest number of minimal projections of the \(B_j\).

**Lemma 4.2.** Let \(\gamma_j\colon M_d\to A\) be ucp, \(j=1,\dots,n\), and \(\varepsilon>0\). For every abelian model
\((B,\mu,(B_j),P)\) of \((A,\varphi,(\gamma_j))\) there are subalgebras \(B_j'\subset B_j\) such that
\((B,\mu,(B_j'),P)\) has size at most \(r(d,\varepsilon)\) and entropy at least the entropy of the original model minus
\(nF_{d^2}(\varepsilon)\).

*Proof.* Use the notation of (1.2). Cut the state space of \(M_d\) into \(r=r(d,\varepsilon)\) disjoint sets
\(U_1,\dots,U_r\) of diameter at most \(\varepsilon\). For each \(j\) define \(\alpha_j\colon X_j\to\{1,\dots,r\}\) by
\(\alpha_j(x)=l\) if \(\varphi_{j,x}\in U_l\) (and \(\alpha_j(x)=1\) if \(\mu(x)=0\)). Let \(B_j'\subset B_j\) be spanned
by the projections \(q_{j,l}=\sum_{\alpha_j(x)=l}x\), \(l=1,\dots,r\). For \(\mu(q_{j,l})>0\) the new states are the
averages
\[
\varphi'_{j,l}=\sum_{\alpha_j(x)=l}\frac{\mu(x)}{\mu(q_{j,l})}\varphi_{j,x},
\]
because \(\varphi'_{j,l}\) is built from the \(b\le q_{j,l}\). All \(\varphi_{j,x}\) with \(\alpha_j(x)=l\) and
\(\mu(x)>0\) lie in \(U_l\), so \(\|\varphi'_{j,l}-\varphi_{j,x}\|\le\sum_{x'}\frac{\mu(x')}{\mu(q_{j,l})}\|\varphi_{j,x'}-\varphi_{j,x}\|\le\varepsilon\)
for each of them, and \(S(\varphi'_{j,l})\le S(\varphi_{j,x})+F_{d^2}(\varepsilon)\). Averaging over \(x\) with weights
\(\mu(x)\) gives \(\chi_j'\ge\chi_j-F_{d^2}(\varepsilon)\) for the terms \(\chi_j\) of (1.2).

It remains to see that the first bracket of (1.2) does not decrease. Let \(\nu\) be the probability on
\(\prod_jX_j\) with \(\nu(x_1,\dots,x_n)=\mu(x_1x_2\cdots x_n)\). The nonzero products \(x_1\cdots x_n\) are the minimal
projections of \(\bigvee_jB_j\), and \(\sum_{x_i,\,i\ne j}x_1\cdots x_n=x_j\), so the marginals of \(\nu\) are
\(\mu|_{B_j}\) and the first bracket of (1.2) equals \(-I(\nu)\). The same holds for the \(B'_j\), with \(\nu\) replaced by
\(f_*\nu\), \(f=\prod_j\alpha_j\), because \(q_{1,l_1}\cdots q_{n,l_n}=\sum_{\alpha(x)=l}x_1\cdots x_n\). By Lemma
4.1, \(-I(f_*\nu)\ge-I(\nu)\). \(\square\)

**Lemma 4.3.** Let \(C\) be an abelian C\*-algebra with \(\dim C\le r\), \(\mu\) a state of \(C\), and
\(\rho,\rho'\colon M_d\to C\) ucp maps with \(\|\rho-\rho'\|_\mu\le\varepsilon\le1\). Then
\[
|s_\mu(\rho)-s_\mu(\rho')|\le\delta(r,d,\varepsilon):=F_{d^2}(\varepsilon)+F_{d^2}(\sqrt\varepsilon)+r\varepsilon\log d,
\]
and \(\delta(r,d,\varepsilon)\to0\) as \(\varepsilon\to0\).

*Proof.* By definition \(s_\mu(\rho)-s_\mu(\rho')=S(\mu\circ\rho')-S(\mu\circ\rho)+\sum_x\mu(x)(S(\rho_x)-S(\rho'_x))\).
For \(\|a\|\le1\), the Cauchy–Schwarz inequality gives
\(|\mu(\rho(a)-\rho'(a))|\le\|\rho(a)-\rho'(a)\|_\mu\le\varepsilon\); so \(\|\mu\rho-\mu\rho'\|\le\varepsilon\) and
the first difference is at most \(F_{d^2}(\varepsilon)\). For a minimal projection \(x\),
\[
\mu(x)\,|\rho_x(a)-\rho'_x(a)|^2\le\sum_{y}\mu(y)|\rho_y(a)-\rho'_y(a)|^2=\|\rho(a)-\rho'(a)\|_\mu^2\le\varepsilon^2,
\]
so \(\|\rho_x-\rho'_x\|\le\varepsilon/\sqrt{\mu(x)}\). If \(\mu(x)\ge\varepsilon\), this is at most \(\sqrt\varepsilon\)
and \(|S(\rho_x)-S(\rho'_x)|\le F_{d^2}(\sqrt\varepsilon)\). If \(\mu(x)<\varepsilon\), we use
\(|S(\rho_x)-S(\rho'_x)|\le\log d\), both entropies lying in \([0,\log d]\); there are at most \(r\) such \(x\). Adding
up gives the bound, and it tends to \(0\) by Lemma 1.2. \(\square\)

**Theorem 4.4.** For every \(d\ge1\) and \(\alpha>0\) there is \(\varepsilon>0\) with the following property. For every
unital C\*-algebra \(A\), state \(\varphi\), integer \(n\) and ucp maps \(\gamma_j,\gamma_j'\colon M_d\to A\) with
\(\|\gamma_j-\gamma_j'\|_\varphi\le\varepsilon\) for \(j=1,\dots,n\),
\[
|H_\varphi(\gamma_1,\dots,\gamma_n)-H_\varphi(\gamma_1',\dots,\gamma_n')|\le n\alpha .
\]

*Proof.* Choose \(\varepsilon_0>0\) with \(F_{d^2}(\varepsilon_0)\le\alpha/2\), put \(r=r(d,\varepsilon_0)\), and choose
\(\varepsilon\in(0,1]\) with \(\delta(r,d,\varepsilon)\le\alpha/2\) (Lemmas 1.2 and 4.3). Let a model
\(\mathfrak M=(B,\mu,(B_j),P)\) be given, and let \(\mathfrak M'=(B,\mu,(B_j'),P)\) be the model of Lemma 4.2 for
\((\gamma_j)\) and \(\varepsilon_0\). Its entropy for \((\gamma_j)\) is at least that of \(\mathfrak M\) minus
\(n\alpha/2\).

Now compare the entropies of \(\mathfrak M'\) for \((\gamma_j)\) and for \((\gamma'_j)\). They differ only in the
defects of \(\rho_j=E_j'P\gamma_j\) and \(\rho'_j=E_j'P\gamma'_j\), where \(E'_j\colon B\to B_j'\) is
\(\mu\)-preserving. The map \(T=E'_jP\) is ucp with \(\mu\circ T=\varphi\), so by the Kadison–Schwarz inequality, for
\(\|a\|\le1\) and \(z=\gamma_j(a)-\gamma'_j(a)\),
\[
\|\rho_j(a)-\rho'_j(a)\|_\mu^2=\mu(T(z)^*T(z))\le\mu(T(z^*z))=\varphi(z^*z)\le\varepsilon^2 .
\]
As \(\dim B'_j\le r\), Lemma 4.3 gives \(|s_\mu(\rho_j)-s_\mu(\rho'_j)|\le\alpha/2\). Hence
\(H_\varphi(\gamma'_1,\dots,\gamma'_n)\ge\) entropy of \(\mathfrak M\) for \((\gamma_j)\) minus \(n\alpha\). Taking the
supremum over \(\mathfrak M\), and exchanging the roles of \(\gamma\) and \(\gamma'\), proves the theorem. \(\square\)

**Corollary 4.5.** Let \(d,\alpha,\varepsilon\) be as in Theorem 4.4.

(a) If \(\kappa_j\colon A\to A\) are ucp with \(\varphi\circ\kappa_j=\varphi\) and
\(\|\gamma_j-\gamma_j'\|_\varphi\le\varepsilon\), then
\(|H_\varphi(\kappa_1\gamma_1,\dots,\kappa_n\gamma_n)-H_\varphi(\kappa_1\gamma'_1,\dots,\kappa_n\gamma'_n)|\le n\alpha\).

(b) If \(\theta\in\mathrm{Aut}(A,\varphi)\) and \(\gamma,\gamma'\colon M_d\to A\) are ucp with
\(\|\gamma-\gamma'\|_\varphi\le\varepsilon\), then \(|h_{\varphi,\theta}(\gamma)-h_{\varphi,\theta}(\gamma')|\le\alpha\).

(c) Statements (a) and (b) and Theorem 4.4 hold for ucp maps from \(D=\bigoplus_qM_{n_q}\) in place of \(M_d\),
with \(d=\sum_qn_q\le\dim D\).

*Proof.* (a) By the Kadison–Schwarz inequality,
\(\|\kappa_j(z)\|_\varphi^2\le\varphi(\kappa_j(z^*z))=\|z\|_\varphi^2\), so
\(\|\kappa_j\gamma_j-\kappa_j\gamma'_j\|_\varphi\le\varepsilon\); apply Theorem 4.4. (b) Apply (a) with
\(\kappa_i=\theta^i\) to get \(|a_n(\gamma)-a_n(\gamma')|\le n\alpha\), and divide by \(n\). (c) Compose with the
compression \(E_D\colon M_d\to D\) of Lemma 1.4, which does not change \(H_\varphi\) and does not increase
\(\|\cdot\|_\varphi\)-distances. \(\square\)

The strength of Theorem 4.4 lies in its uniformity: the admissible \(\varepsilon\) does not depend on \(n\), so it
survives the division by \(n\) in (b). Exercise 2 shows that \(\|\gamma-\gamma'\|_\varphi\) can be small while
\(\|\gamma-\gamma'\|\) is as large as possible.

## 5. Von Neumann algebras

A von Neumann algebra \(M\) is in particular a unital C\*-algebra, so for a normal state \(\varphi\) and
\(\theta\in\mathrm{Aut}(M,\varphi)\) Definition 2.2 applies verbatim.

**Definition 5.1.** For a normal state \(\varphi\) of a von Neumann algebra \(M\) and
\(\theta\in\mathrm{Aut}(M,\varphi)\), \(h_\varphi(\theta)\) denotes the supremum of \(h_{\varphi,\theta}(\gamma)\)
over all ucp maps \(\gamma\) into \(M\) whose domains are finite-dimensional C\*-algebras (equivalently, matrix
algebras).

Nothing changes if one insists that the maps in abelian models be normal. Indeed, in (1.1) each
\(\mu(b)\omega_b\) is a positive functional dominated by the normal state \(\varphi\); by (B5) in the GNS
representation of \(\varphi\), \(\mu(b)\omega_b=\langle\pi_\varphi(\cdot)t_b\xi_\varphi,\xi_\varphi\rangle\) with
\(t_b\in\pi_\varphi(M)'\) positive, which is normal because \(\pi_\varphi\) is a normal representation. So
\(P\) is automatically normal. Maps from finite-dimensional algebras are automatically normal as well.

Theorem 3.1 does not apply to \(M\): as a C\*-algebra, a von Neumann algebra is in general not nuclear (B3). What
replaces norm approximation is strong approximation, which Theorem 4.4 is designed to handle.

**Lemma 5.2 (strong approximation).** Let \(A_0\) be a unital C\*-subalgebra of a von Neumann algebra
\(M\subset B(H)\) with \(A_0''=M\), and let \(\gamma\colon M_d\to M\) be ucp.

(a) There is a net of arrays \(c^\lambda\) in \(A_0\) with \(T_{c^\lambda}\le1\) such that the ucp maps
\(\gamma_\lambda=\gamma_{c^\lambda}\colon M_d\to A_0\) of (3.1) satisfy
\(\sup_{\|a\|\le1}\|(\gamma_\lambda(a)-\gamma(a))\zeta\|\to0\) for every \(\zeta\in H\). Consequently
\(\|\gamma_\lambda-\gamma\|_\varphi\to0\) for every normal state \(\varphi\) of \(M\).

(b) If \(A_0=\pi(A)\) for a unital \(\ast\)-homomorphism \(\pi\) from a unital C\*-algebra \(A\), one can moreover take
\(\gamma_\lambda=\pi\circ\tilde\gamma_\lambda\) with \(\tilde\gamma_\lambda\colon M_d\to A\) ucp.

*Proof.* (a) By Lemma 3.3(a), \(\gamma=\gamma_v\) for an array \(v\) in \(M\) with \(\|\mathrm{Col}(v)\|=1\). By (B4),
\(M_{d^2}(A_0)\) is strong\*-dense in \(M_{d^2}(M)\) with unit ball dense in the unit ball, so there is a net
\(Y_\lambda\) in the unit ball of \(M_{d^2}(A_0)\) converging strong\* to \(\mathrm{Col}(v)\). Let \(c^\lambda\) be the
array formed by the first column of \(Y_\lambda\). Then \(\mathrm{Col}(c^\lambda)=Y_\lambda(1\otimes e_{11})\) has norm
at most \(1\), so \(T_{c^\lambda}\le1\), and the entries converge strong\* to those of \(v\). Lemma 3.3(d) gives the
uniform strong convergence. For a normal state write \(\varphi=\sum_n\langle\cdot\,\zeta_n,\zeta_n\rangle\) as in (B4).
Then
\[
\|\gamma_\lambda-\gamma\|_\varphi^2\le\sum_n\sup_{\|a\|\le1}\|(\gamma_\lambda(a)-\gamma(a))\zeta_n\|^2 ,
\]
each term tends to \(0\) and is at most \(4\|\zeta_n\|^2\), so the sum tends to \(0\).

(b) Let \(C_\lambda=\mathrm{Col}(c^\lambda)\in M_{d^2}(\pi(A))\), of norm at most \(1\). The \(\ast\)-homomorphism
\(\pi_{d^2}\colon M_{d^2}(A)\to M_{d^2}(\pi(A))\) is onto; let \(W\) be any preimage of \(C_\lambda\), and replace it by
its first column, which is still a preimage. Let \(g\) be the continuous function on \([0,\infty)\) with \(g(t)=1\) for
\(t\le1\) and \(g(t)=t^{-1/2}\) for \(t\ge1\), and put \(W'=Wg(W^*W)\). Then
\(W'^*W'=(tg(t)^2)(W^*W)=\min(W^*W,1)\le1\), \(W'\) has only a first column, and
\(\pi_{d^2}(W')=C_\lambda g(C_\lambda^*C_\lambda)=C_\lambda\) because \(g=1\) on the spectrum of
\(C_\lambda^*C_\lambda\subset[0,1]\). So \(W'=\mathrm{Col}(\tilde c)\) for an array \(\tilde c\) in \(A\) with
\(T_{\tilde c}\le1\) and \(\pi(\tilde c_{ki})=c^\lambda_{ki}\). Put \(\tilde\gamma_\lambda=\gamma_{\tilde c}\); then
\(\pi\circ\tilde\gamma_\lambda=\gamma_{c^\lambda}\). \(\square\)

**From C\*-algebras to von Neumann algebras.** Fix a state \(\varphi\) of a unital C\*-algebra \(A\), an
automorphism \(\theta\in\mathrm{Aut}(A,\varphi)\), and the GNS triple \((\pi,H,\xi)\) of \(\varphi\). Put \(M=\pi(A)''\) and
\(\bar\varphi=\langle\cdot\,\xi,\xi\rangle\), a normal state of \(M\) with \(\bar\varphi\circ\pi=\varphi\). The formula
\(U\pi(a)\xi=\pi(\theta(a))\xi\) defines a unitary \(U\) (it is isometric because \(\varphi\circ\theta=\varphi\) and has
dense range because \(\theta\) is onto), with \(U\pi(a)U^*=\pi(\theta(a))\) and \(U\xi=\xi\). Hence
\(\bar\theta=\mathrm{Ad}\,U|_M\) is an automorphism of \(M\) with \(\bar\theta\circ\pi=\pi\circ\theta\) and
\(\bar\varphi\circ\bar\theta=\bar\varphi\).

**Theorem 5.3.** In this situation:

(a) \(H_{\bar\varphi}(\pi\gamma_1,\dots,\pi\gamma_n)=H_\varphi(\gamma_1,\dots,\gamma_n)\) for all ucp
\(\gamma_j\colon D_j\to A\);

(b) \(h_{\bar\varphi}(\bar\theta)=h_\varphi(\theta)\).

No nuclearity is needed. When \(A\) is separable and nuclear, \(M\) is hyperfinite (B3), so Theorem 5.4 below
computes both sides.

*Proof.* (a) If \((B,\mu,(B_j),Q)\) is a model for \((M,\bar\varphi)\), then \((B,\mu,(B_j),Q\circ\pi)\) is a model for
\((A,\varphi)\), and the states \(\varphi_{j,x}\) built from \(Q\pi\gamma_j\) are the same. Conversely let
\((B,\mu,(B_j),P)\) be a model for \((A,\varphi)\), with \(P=\sum_b\omega_b(\cdot)b\). For \(\mu(b)>0\),
\(\mu(b)\omega_b\le\varphi\). By the Cauchy–Schwarz inequality \(\omega_b\) vanishes on \(\ker\pi\), so it is a
functional on \(\pi(A)\), and by (B5) there is \(t_b\in\pi(A)'\), \(t_b\ge0\), with
\(\mu(b)\omega_b(a)=\langle\pi(a)t_b\xi,\xi\rangle\). Define normal states
\(\bar\omega_b(y)=\mu(b)^{-1}\langle yt_b\xi,\xi\rangle\) on \(M\) (positive because \(t_b\in M'\)), and
\(\bar\omega_b=\bar\varphi\) when \(\mu(b)=0\). Then \(\sum_{\mu(b)>0}t_b=1\): the operator \(t=\sum t_b\in\pi(A)'\)
satisfies \(\langle\pi(a)(t-1)\xi,\xi\rangle=0\) for all \(a\), so \(\langle(t-1)\xi,\pi(a)\xi\rangle=0\) for all \(a\),
whence \((t-1)\xi=0\); as \(\xi\) is cyclic for \(\pi(A)\), it is separating for \(\pi(A)'\), and \(t=1\). So
\(\bar P=\sum_b\bar\omega_b(\cdot)b\) is a model for \((M,\bar\varphi)\) with \(\bar P\circ\pi=P\) on all \(b\) with
\(\mu(b)>0\), and its states \(\varphi_{j,x}\) for \((\pi\gamma_j)\) are those of \(P\) for \((\gamma_j)\). By (1.2) the
two suprema coincide.

(b) Since \(\bar\theta^i\pi\gamma=\pi\theta^i\gamma\), part (a) gives
\(h_{\bar\varphi,\bar\theta}(\pi\gamma)=h_{\varphi,\theta}(\gamma)\), hence \(h_\varphi(\theta)\le h_{\bar\varphi}(\bar\theta)\).
Conversely, let \(\gamma\colon M_d\to M\) be ucp and \(\alpha>0\), and let \(\varepsilon\) be as in Theorem 4.4. By
Lemma 5.2(b) there is a ucp \(\tilde\gamma\colon M_d\to A\) with \(\|\pi\tilde\gamma-\gamma\|_{\bar\varphi}\le\varepsilon\).
By Corollary 4.5(b), \(h_{\bar\varphi,\bar\theta}(\gamma)\le h_{\bar\varphi,\bar\theta}(\pi\tilde\gamma)+\alpha=
h_{\varphi,\theta}(\tilde\gamma)+\alpha\le h_\varphi(\theta)+\alpha\). \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987], where \(A\) is assumed nuclear.

**Hyperfinite von Neumann algebras.** A von Neumann algebra is *hyperfinite* if it contains an increasing net of
finite-dimensional subalgebras whose union is weakly dense. For von Neumann algebras with separable predual one can
take a sequence.

**Theorem 5.4 (Kolmogorov–Sinai theorem for hyperfinite algebras).** Let \(\varphi\) be a normal state of a von
Neumann algebra \(M\), \(\theta\in\mathrm{Aut}(M,\varphi)\), and \((N_k)\) an increasing net of finite-dimensional
subalgebras of \(M\) whose union is weakly dense. Then
\[
h_\varphi(\theta)=\lim_kh_{\varphi,\theta}(N_k)=\sup_kh_{\varphi,\theta}(N_k).
\]

*Proof.* The net \(h_{\varphi,\theta}(N_k)\) is nondecreasing and bounded by \(h_\varphi(\theta)\) (Proposition
2.3(a)). Let \(\gamma\colon M_d\to M\) be ucp and \(\alpha>0\); let \(\varepsilon\) be as in Theorem 4.4. Represent
\(M\subset B(H)\) and let \(A_0\) be the norm closure of \(\bigcup_kN_k\), a unital C\*-algebra with \(A_0''=M\) by the
double commutant theorem. By Lemma 5.2(a) there is an array \(c\) in \(A_0\) with \(T_c\le1\) and
\(\|\gamma_c-\gamma\|_\varphi\le\varepsilon/2\). As in the proof of Corollary 3.4 there are \(k\) and an array \(c'\) in
\(N_k\) with \(T_{c'}\le1\) and \(\|\gamma_{c'}-\gamma_c\|\le\varepsilon/2\). Then \(\gamma_{c'}\) is a ucp map into
\(N_k\) with \(\|\gamma_{c'}-\gamma\|_\varphi\le\varepsilon\), and by Corollary 4.5(b) and Proposition 2.3(a),
\[
h_{\varphi,\theta}(\gamma)\le h_{\varphi,\theta}(\gamma_{c'})+\alpha\le h_{\varphi,\theta}(N_k)+\alpha .
\]
Since \(\alpha\) is arbitrary and matrix algebras suffice (Lemma 1.4), \(h_\varphi(\theta)\le\sup_kh_{\varphi,\theta}(N_k)\).
\(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987].

**Corollary 5.5.** If \(M\) is hyperfinite, \(h_\varphi(\theta)=\sup\{h_{\varphi,\theta}(N)\}\), the supremum over all
finite-dimensional subalgebras \(N\subset M\). \(\square\)

**Corollary 5.6.** Let \(A\) be a separable nuclear C\*-algebra, \(\varphi\) a state and
\(\theta\in\mathrm{Aut}(A,\varphi)\). With the notation of Theorem 5.3, for every chain \(N_1\subset N_2\subset\cdots\) of
finite-dimensional subalgebras of \(\pi_\varphi(A)''\) whose union is weakly dense,
\(h_\varphi(\theta)=\lim_kh_{\bar\varphi,\bar\theta}(N_k)\).

*Proof.* The GNS space of a state of a separable C\*-algebra is separable, so \(\pi_\varphi(A)''\) is hyperfinite by
(B3), and such sequences exist. Combine Theorems 5.3 and 5.4. \(\square\)

Separability and nuclearity serve only to produce such sequences: for any unital \(A\) and any increasing net of
finite-dimensional subalgebras of \(\pi_\varphi(A)''\) whose union is weakly dense, Theorems 5.3 and 5.4 give the same
formula.

The subalgebras \(N_k\) in Corollary 5.6 live in the von Neumann algebra and need not lie in \(A\). This is the form in
which the entropy of lattice translations is computed in the lesson "Entropy of lattice translations in quantum spin
chains": there the \(N_k\) are local algebras, and the difficulty is moved to estimating \(H_\varphi\) on them, which
is the subject of Sections 6 to 8.

**Proposition 5.7.** Let \(M,\varphi,\theta\) be as in Theorem 5.4, and suppose that \(\theta(N_k)=N_k\) for all
\(k\). Then \(h_\varphi(\theta)=0\).

*Proof.* Let \(\iota\) be the inclusion of \(N_k\) and \(\theta_k=\theta|_{N_k}\), an automorphism of \(N_k\). Then
\(\theta^i\iota=\iota\theta_k^i\), so by Proposition 1.3(b), (d) and (a),
\(a_n(\iota)\le H_\varphi(\iota,\dots,\iota)=H_\varphi(\iota)\le S(\varphi|_{N_k})\). Hence \(h_{\varphi,\theta}(N_k)=0\),
and Theorem 5.4 applies. \(\square\)

**Modular automorphisms.** Let now \(\varphi\) be faithful. Each modular automorphism \(\sigma^\varphi_t\) preserves
\(\varphi\), so \(h_\varphi(\sigma^\varphi_t)\) is defined.

**Proposition 5.8.** Suppose \(\varphi\) is a faithful normal state of \(M\) and \(\sigma\in\mathrm{Aut}(M)\). Then
\(\sigma^{\varphi\circ\sigma}_t=\sigma^{-1}\sigma^\varphi_t\sigma\), and consequently
\(h_{\varphi\circ\sigma}(\sigma^{\varphi\circ\sigma}_t)=h_\varphi(\sigma^\varphi_t)\) for all real \(t\). In particular
\(t\mapsto h_\varphi(\sigma^\varphi_t)\) depends only on the isomorphism class of the pair \((M,\varphi)\), and
\(h_{\varphi\circ\mathrm{Ad}u}(\sigma^{\varphi\circ\mathrm{Ad}u}_t)=h_\varphi(\sigma^\varphi_t)\) for unitaries
\(u\in M\).

*Proof.* The group \(\alpha_t=\sigma^{-1}\sigma^\varphi_t\sigma\) is \(\sigma\)-weakly continuous, as automorphisms
of von Neumann algebras are normal. For \(x,y\in M\) let \(F\) be the KMS function of \(\varphi\) for the pair
\(\sigma(y),\sigma(x)\): bounded and continuous on the strip \(0\le\mathrm{Im}\,z\le1\), analytic inside, with
\(F(t)=\varphi(\sigma^\varphi_t(\sigma(y))\sigma(x))=(\varphi\circ\sigma)(\alpha_t(y)x)\) and
\(F(t+i)=\varphi(\sigma(x)\sigma^\varphi_t(\sigma(y)))=(\varphi\circ\sigma)(x\alpha_t(y))\). So \(\varphi\circ\sigma\)
satisfies the KMS condition for \(\alpha\), and \(\alpha=\sigma^{\varphi\circ\sigma}\) by (B6). The equality of
entropies is Proposition 2.3(c). \(\square\)

**Remark 5.9 (discontinuity of the entropy).** Let \(R\) be the hyperfinite factor of type III₁ of (B8), \(F\) the set
of its faithful normal states with the norm topology, and \(f(\varphi)=h_\varphi(\sigma^\varphi_1)\in[0,\infty]\).

1. \(f\) vanishes on the product state \(\varphi\) of (B8): the modular group leaves every local algebra
   \(\bigotimes_{k\le p}M_2\) invariant, these algebras increase and have weakly dense union, and Proposition 5.7
   applies.
2. Either \(f\) is identically \(0\) on \(F\), or \(f\) is continuous at no point of \(F\). Indeed, by Proposition 5.8,
   \(f(\psi\circ\mathrm{Ad}u)=f(\psi)\) for unitaries \(u\), and by (B8) the orbit \(\{\psi\circ\mathrm{Ad}u\}\) of
   every \(\psi\in F\) is dense in \(F\). If \(f\) were continuous at \(\varphi_0\), choose \(u_n\) with
   \(\psi\circ\mathrm{Ad}u_n\to\varphi_0\); then \(f(\psi)=f(\psi\circ\mathrm{Ad}u_n)\to f(\varphi_0)\), so \(f\) would be
   constant, hence \(0\) by item 1.

It is asserted in [Connes–Narnhofer–Thirring 1987] that the entropy of modular automorphisms of hyperfinite III₁
factors takes every nonnegative value, which by item 2 would make \(f\) discontinuous everywhere. We do not prove
this here. What the argument does show is that no continuity of \(\varphi\mapsto h_\varphi(\sigma^\varphi_1)\) in the
norm topology can be expected unless the entropy of all modular automorphisms of \(R\) vanishes.

## 6. The upper bound, and abelian subalgebras in the centralizer

By Corollary 3.4 and Theorems 5.3 and 5.4, computing \(h_\varphi(\theta)\) comes down to computing, or estimating
from both sides, \(H_\varphi(N_1,\dots,N_k)\) for finite-dimensional subalgebras. This section gives the general upper
bound and the case of equality. Throughout, \(A\) is a unital C\*-algebra and \(\varphi\) a state.

**Lemma 6.1.** Let \(N\subset A\) be a subalgebra of finite dimension and \(N_1,\dots,N_k\subset N\) subalgebras. Then
\(H_\varphi(N_1,\dots,N_k)\le S(\varphi|_N)\). More generally \(H_\varphi(\gamma_1,\dots,\gamma_k)\le S(\varphi|_N)\)
for ucp maps \(\gamma_j\) with values in \(N\).

*Proof.* Write \(\gamma_j=\iota_N\circ\bar\gamma_j\) with \(\iota_N\) the inclusion. By Proposition 1.3(b), (d), (a),
\(H_\varphi(\gamma_1,\dots,\gamma_k)\le H_\varphi(\iota_N,\dots,\iota_N)=H_\varphi(\iota_N)\le S(\varphi|_N)\).
\(\square\)

For a lower bound one needs good abelian models. The natural candidates are built from abelian subalgebras, and they
work well when these subalgebras commute with the state in the following sense.

**Definition.** The *centralizer* of \(\varphi\) is \(A_\varphi=\{a\in A:\varphi(ab)=\varphi(ba)\ \forall b\in A\}\).

\(A_\varphi\) is a C\*-subalgebra: if \(a,a'\in A_\varphi\) then \(\varphi(aa'b)=\varphi(a'ba)=\varphi(baa')\), and
\(\varphi(a^*b)=\overline{\varphi(b^*a)}=\overline{\varphi(ab^*)}=\varphi(ba^*)\). It is all of \(A\) exactly when
\(\varphi\) is a trace. For a faithful normal state of a von Neumann algebra it is the fixed-point algebra
\(M_\varphi\) of the modular group (B6).

**Theorem 6.2.** Let \(C_1,\dots,C_n\) be pairwise commuting finite-dimensional abelian subalgebras of \(A\) contained in
\(A_\varphi\), and let \(C_0=C_1\vee\cdots\vee C_n\) be the (finite-dimensional, abelian) algebra they generate. Then
\[
H_\varphi(C_1,\dots,C_n)=S(\varphi|_{C_0}).
\]

*Proof.* The inequality \(\le\) is Lemma 6.1. For \(\ge\) we build an abelian model. Let \(Y\) be the set of minimal
projections \(e\) of \(C_0\) with \(\varphi(e)>0\). For \(e\in Y\) put \(\omega_e(a)=\varphi(ea)/\varphi(e)\). It is a
state: since \(e\in A_\varphi\), \(\varphi(ea^*a)=\varphi(e\cdot ea^*a)=\varphi(ea^*ae)\ge0\). Moreover
\(\sum_{e\in Y}\varphi(e)\omega_e=\varphi\), because for a minimal projection \(e\) with \(\varphi(e)=0\) the
Cauchy–Schwarz inequality gives \(|\varphi(ea)|^2\le\varphi(e)\varphi(a^*a)=0\), and the minimal projections of \(C_0\)
add up to \(1\). So (1.1) holds with \(\mu(e)=\varphi(e)\). Each \(e\in Y\) lies under exactly one minimal projection
\(x\) of \(C_j\); this defines a partition of \(Y\), that is, a subalgebra \(B_j\) of \(B=\mathbb C^Y\). Two different minimal projections of \(C_0\) differ in some component, so
\(\bigvee_jB_j=\mathbb C^Y\) and \(S(\mu|_{\bigvee B_j})=\sum_{e\in Y}\eta(\varphi(e))=S(\varphi|_{C_0})\); likewise
\(S(\mu|_{B_j})=S(\varphi|_{C_j})\). Finally, for \(x\) a minimal projection of \(C_j\) with \(\varphi(x)>0\) and
\(a\in C_j\),
\[
\varphi_{j,x}(a)=\frac1{\varphi(x)}\sum_{e\in Y,\ e\le x}\varphi(ea)=\frac{\varphi(xa)}{\varphi(x)}=a(x),
\]
where \(a(x)\) is the scalar with \(xa=a(x)x\). So \(\varphi_{j,x}\) is a pure state of the abelian algebra \(C_j\) and
\(S(\varphi_{j,x})=0\). By (1.2), the entropy of this model is
\(S(\varphi|_{C_0})-\sum_jS(\varphi|_{C_j})+\sum_jS(\varphi|_{C_j})=S(\varphi|_{C_0})\). \(\square\)

**Corollary 6.3 (tracial states).** If \(\varphi\) is a trace, then \(H_\varphi(C_1,\dots,C_n)=S(\varphi|_{C_0})\) for
all pairwise commuting finite-dimensional abelian subalgebras. \(\square\)

*Reference:* [Connes–Størmer 1975] for the corresponding statement about the entropy of the lesson "Entropy of
finite-dimensional subalgebras".

Corollary 6.3 fails for non-tracial states, already for one subalgebra: see Example 6.7. The next corollary is the
form of Theorem 6.2 used for non-abelian subalgebras.

**Corollary 6.4.** Let \(N_1,\dots,N_k\subset A\) be finite-dimensional subalgebras and \(C_j\subset N_j\cap A_\varphi\)
abelian subalgebras that commute pairwise. Let \(N\) be the C\*-algebra generated by \(N_1,\dots,N_k\), and assume that
\(C_0=C_1\vee\cdots\vee C_k\) is maximal abelian in \(N\). Then \(N\) is finite dimensional and
\[
H_\varphi(N_1,\dots,N_k)=S(\varphi|_N)=S(\varphi|_{C_0}).
\]

*Proof.* Let \(e\) be a minimal projection of \(C_0\) and \(y\in N\). For every minimal projection \(f\) of \(C_0\),
\(f\,eye=\delta_{ef}\,eye=eye\,f\), so \(eye\in C_0'\cap N=C_0\), hence \(eye\in\mathbb Ce\): each \(e\) is a minimal
projection of \(N\). For two of them \(e,f\), the space \(eNf\) has dimension at most one: if \(u,v\in eNf\) and
\(u\ne0\), then \(uu^*=\|u\|^2e\) and \(u^*v\in fNf=\mathbb Cf\), say \(u^*v=sf\), so
\(v=\|u\|^{-2}uu^*v=\|u\|^{-2}s\,u\). As \(N=\sum_{e,f}eNf\), \(N\) is finite dimensional.

Let \(\rho\) be the density of \(\varphi|_N\) with respect to \(\mathrm{Tr}_N\). For \(c\in C_0\subset A_\varphi\) and
\(y\in N\), \(\mathrm{Tr}_N(\rho cy)=\varphi(cy)=\varphi(yc)=\mathrm{Tr}_N(c\rho y)\), so \(\rho c=c\rho\) and
\(\rho\in C_0'\cap N=C_0\). The minimal projections of \(C_0\) are minimal in \(N\), so they have trace \(1\), and
\(S(\varphi|_N)=\sum_e\eta(\varphi(e))=S(\varphi|_{C_0})\). Now Lemma 6.1, Proposition 1.3(b) and Theorem 6.2 give
\(S(\varphi|_N)\ge H_\varphi(N_1,\dots,N_k)\ge H_\varphi(C_1,\dots,C_k)=S(\varphi|_{C_0})\). \(\square\)

**Corollary 6.5.** Suppose \(\varphi\) is a faithful normal state of a von Neumann algebra \(M\), and \(N\subset M\)
is a finite-dimensional subalgebra.

(a) If \(N\cap M_\varphi\) contains a maximal abelian subalgebra of \(N\), then \(H_\varphi(N)=S(\varphi|_N)\).

(b) If \(\sigma^\varphi_t(N)=N\) for all \(t\), then \(N\cap M_\varphi\) contains a maximal abelian subalgebra of \(N\),
and so \(H_\varphi(N)=S(\varphi|_N)\).

*Proof.* (a) is Corollary 6.4 with \(k=1\), since \(M_\varphi\) is the centralizer (B6). (b) Let
\(\varphi|_N=\mathrm{Tr}_N(\rho\,\cdot\,)\); \(\rho\) is invertible because \(\varphi\) is faithful. By (B7) and (B6),
\(\sigma^\varphi_t(y)=\rho^{it}y\rho^{-it}\) for \(y\in N\). Choose a maximal abelian subalgebra \(C\) of \(N\)
containing \(\rho\) (enlarge the abelian algebra generated by \(1\) and \(\rho\)). Every \(c\in C\) commutes with
\(\rho\), hence is fixed by \(\sigma^\varphi\), so \(C\subset M_\varphi\). Apply (a). \(\square\)

For a single subalgebra the entropy has a transparent description, which also measures the failure of equality.

**Proposition 6.6.** Let \(\gamma\colon D\to A\) be ucp with \(D\) finite dimensional. Then
\[
H_\varphi(\gamma)=S(\varphi\circ\gamma)-\delta_\varphi(\gamma),\qquad
\delta_\varphi(\gamma)=\inf\Big\{\sum_b\mu_bS(\omega_b\circ\gamma)\ :\ \varphi=\sum_b\mu_b\omega_b\Big\},
\]
the infimum over all finite decompositions of \(\varphi\) as a convex combination of states of \(A\). The function
\(\varphi\mapsto\delta_\varphi(\gamma)\) on the state space of \(A\) is the largest convex function below
\(\varphi\mapsto S(\varphi\circ\gamma)\). In particular \(\delta_\varphi(\gamma)\ge0\) is convex in \(\varphi\), the set
\(\{\varphi:\ \delta_\varphi(\gamma)=0\}\) is convex, and \(H_\varphi(\gamma)\) is concave in \(\varphi\). For a
finite-dimensional subalgebra \(N\), \(\delta_\varphi(N)=0\) whenever \(N\cap A_\varphi\) contains a maximal abelian
subalgebra of \(N\).

*Proof.* For \(n=1\), (1.2) reads \(S(\mu|_{B_1})-S(\mu|_{B_1})+S(\varphi\circ\gamma)-\sum_x\mu(x)S(\varphi_x\circ\gamma)\)
with \(\varphi_x=\mu(x)^{-1}\sum_{b\le x}\mu(b)\omega_b\), and \(\varphi=\sum_x\mu(x)\varphi_x\) is again a finite
decomposition into states. Conversely a decomposition \(\varphi=\sum_x\mu_x\varphi_x\) is a model with
\(B=B_1=\mathbb C^X\). This proves the formula. Let \(g(\varphi)\) denote the infimum. Taking the trivial decomposition,
\(g(\varphi)\le S(\varphi\circ\gamma)\). If \(\varphi=\lambda\varphi'+(1-\lambda)\varphi''\) and
\(\varphi'=\sum\mu'_b\omega'_b\), \(\varphi''=\sum\mu''_c\omega''_c\), then
\(\varphi=\sum\lambda\mu'_b\omega'_b+\sum(1-\lambda)\mu''_c\omega''_c\), so
\(g(\varphi)\le\lambda\sum\mu'_bS(\omega'_b\gamma)+(1-\lambda)\sum\mu''_cS(\omega''_c\gamma)\); taking infima,
\(g\) is convex. If \(f\) is convex and \(f\le S(\cdot\circ\gamma)\), then
\(f(\varphi)\le\sum\mu_bf(\omega_b)\le\sum\mu_bS(\omega_b\gamma)\) for every decomposition, so \(f\le g\). Concavity
of \(H_\varphi(\gamma)\) follows from the concavity of \(S\) (B2) and the convexity of \(\delta\). The last statement is
Corollary 6.4 with \(k=1\). \(\square\)

**Example 6.7 (a pure state).** Let \(A=M_2\), \(\varphi\) the pure state given by a unit vector \(v\), and \(C\) the
diagonal subalgebra for an orthonormal basis \(f_1,f_2\) with \(|\langle v,f_1\rangle|^2=p\in(0,1)\). A pure state has
only the trivial decompositions (if \(\varphi=\sum\mu_b\omega_b\) with \(\mu_b>0\), each \(\omega_b=\varphi\)), so
Proposition 6.6 gives \(\delta_\varphi(C)=S(\varphi|_C)\) and
\[
H_\varphi(C)=0<S(\varphi|_C)=\eta(p)+\eta(1-p).
\]
The same value \(0\) also follows from Lemma 6.1 with \(N=M_2\), as \(S(\varphi)=0\). Here \(C\not\subset A_\varphi\):
the centralizer of a vector state on \(M_2\) consists of the matrices commuting with the projection onto \(v\), and
the projection onto \(f_1\) does not. By contrast, for \(\gamma=\mathrm{id}_{M_2}\) and any state, a decomposition
into pure states along the eigenvectors of the density gives \(\delta_\varphi(\mathrm{id})=0\), so \(H_\varphi(M_2)=S(\varphi)\) (Exercise 5).

**Example 6.8 (shifts on infinite tensor products).** Let \(A=\bigotimes_{k\in\mathbb Z}M_n\) be the infinite tensor
product C\*-algebra, the norm closure of the increasing union of the local algebras \(N_I=\bigotimes_{k\in I}M_n\) for
finite intervals \(I\subset\mathbb Z\). Let \(\theta\) be the shift, \(\theta(N_I)=N_{I+1}\), let \(\omega\) be a state of
\(M_n\) with density \(\rho\), and let \(\varphi=\bigotimes_k\omega\) be the product state. Then \(\varphi\circ\theta=\varphi\)
and
\[
h_\varphi(\theta)=S(\omega).
\]
By Theorem 5.3 the same holds for the extension of \(\theta\) to \(\pi_\varphi(A)''\).

*Proof.* Choose a maximal abelian subalgebra \(C\subset M_n\) containing \(\rho\) and let \(C_I=\bigotimes_{k\in I}C\subset
N_I\). The density of \(\varphi|_{N_I}\) is \(\rho^{\otimes I}\in C_I\), so every \(c\in C_I\) satisfies
\(\varphi(cy)=\varphi(yc)\) for local \(y\), hence for all \(y\in A\) by continuity: \(C_I\subset A_\varphi\). Fix an
interval \(I\) of length \(p+1\) and \(m\ge1\). The algebras \(\theta^i(N_I)=N_{I+i}\), \(0\le i<m\), generate
\(N_{J}\) with \(J=I\cup(I+1)\cup\cdots\cup(I+m-1)\), an interval of length \(p+m\); the abelian algebras
\(\theta^i(C_I)=C_{I+i}\subset N_{I+i}\cap A_\varphi\) commute pairwise and generate \(C_J\), which is maximal abelian in \(N_J\) (its minimal projections are
tensor products of rank-one projections, hence rank one, and they add up to \(1\)). By Corollary 6.4,
\[
H_\varphi(N_I,\theta N_I,\dots,\theta^{m-1}N_I)=S(\varphi|_{N_J})=(p+m)S(\omega),
\]
since the entropy of \(\rho^{\otimes(p+m)}\) is \((p+m)S(\rho)\). Dividing by \(m\) and letting \(m\to\infty\),
\(h_{\varphi,\theta}(N_I)=S(\omega)\) for every interval \(I\). Corollary 3.4 with \(A_k=N_{[-k,k]}\) gives
\(h_\varphi(\theta)=S(\omega)\). \(\square\)

For the normalized trace \(\omega=\mathrm{tr}\) one gets \(\log n\), the entropy of the noncommutative Bernoulli shift
computed in the lesson "The entropy of a trace-preserving automorphism". For non-tracial \(\omega\) the product state
is not a trace, yet the entropy is still the entropy of the one-site state: what matters in the proof is only that
the abelian subalgebras \(C_I\) lie in the centralizer.

## 7. The adjoint of a state-preserving map and the entropy defect

In realistic examples the centralizer is often trivial, and Theorem 6.2 does not apply. There is still a canonical
candidate for the map \(P\) of an abelian model built on an abelian subalgebra \(C\subset M\): the adjoint of the
inclusion \(C\to M\) with respect to the state. Its entropy defect measures how far \(C\) is from commuting with the
state. In this section \(\varphi\) is a faithful normal state of a von Neumann algebra \(M\), and \((H,\xi,J,\Delta)\) are
the data of (B6).

**Lemma 7.1 (the symmetric form of a state).** For \(x,y\in M\) put
\(s_\varphi(x,y)=\langle\Delta^{1/2}x\xi,\,y^*\xi\rangle\). Then:

(i) \(s_\varphi(x,y)=\langle y\,Jx^*J\,\xi,\xi\rangle\); \(s_\varphi\) is bilinear and symmetric, and
\(s_\varphi(x,1)=\varphi(x)\).

(ii) If \(x\ge0\), then \(s_\varphi(x,\cdot)\) is a positive normal functional of norm \(\varphi(x)\); if
\(0\le x\le1\), then \(0\le s_\varphi(x,\cdot)\le\varphi\).

(iii) If \(s_\varphi(x,y)=0\) for all \(y\), then \(x=0\).

(iv) Every positive functional \(\psi\le\varphi\) on \(M\) equals \(s_\varphi(x,\cdot)\) for a unique \(x\in M\), and
\(0\le x\le1\).

(v) If \(x\in D(\sigma^\varphi_{-i/2})\), then \(s_\varphi(x,y)=\varphi(y\,\sigma^\varphi_{-i/2}(x))\). If
\(x\in M_\varphi\), then \(s_\varphi(x,y)=\varphi(yx)=\varphi(xy)\).

(vi) If \(M\) is finite dimensional and \(\varphi=\mathrm{Tr}_M(\rho\,\cdot\,)\), then
\(s_\varphi(x,y)=\mathrm{Tr}_M(\rho^{1/2}x\rho^{1/2}y)\). If \(M\) is abelian, \(s_\varphi(x,y)=\varphi(xy)\).

In the notation of [Connes–Narnhofer–Thirring 1987], \(s_\varphi(x,\cdot)=\varphi^{1/2}x\varphi^{1/2}\), as (vi)
suggests.

*Proof.* (i) \(\Delta^{1/2}x\xi=JSx\xi=Jx^*\xi=Jx^*J\xi\), so
\(s_\varphi(x,y)=\langle Jx^*J\xi,y^*\xi\rangle=\langle y\,Jx^*J\xi,\xi\rangle\). The map \(x\mapsto Jx^*J\) is linear
(two conjugate-linear steps and an involution). For symmetry use \(\langle J\alpha,\beta\rangle=\langle J\beta,\alpha\rangle\),
valid for a conjugate-linear isometric involution:
\(s_\varphi(x,y)=\langle Jx^*\xi,y^*\xi\rangle=\langle Jy^*\xi,x^*\xi\rangle=s_\varphi(y,x)\). Finally
\(s_\varphi(x,1)=\langle Jx^*\xi,J\xi\rangle=\langle\xi,x^*\xi\rangle=\varphi(x)\).

(ii) If \(x\ge0\), then \(JxJ\ge0\) lies in \(M'\), so \(s_\varphi(x,y^*y)=\langle JxJ\,y\xi,y\xi\rangle\ge0\), and the
functional is a vector functional, hence normal. Its norm is its value at \(1\), which is \(\varphi(x)\). If \(x\le1\),
apply this to \(1-x\) and use \(s_\varphi(1,\cdot)=\varphi\).

(iii) If \(\langle Jx^*J\xi,y^*\xi\rangle=0\) for all \(y\), then \(Jx^*J\xi=0\) since \(\xi\) is cyclic, so
\(x^*\xi=0\), and \(x=0\) since \(\xi\) is separating.

(iv) By (B5) there is \(t\in M'\) with \(0\le t\le1\) and \(\psi=\langle\cdot\,t\xi,\xi\rangle\). Since \(JM'J=M\),
\(t=JxJ\) with \(x\in M\), \(0\le x\le1\), and \(\psi=s_\varphi(x,\cdot)\) by (i). Uniqueness is (iii).

(v) By (0.1) with \(\alpha=-\tfrac12\), \(\Delta^{1/2}x\xi=\sigma^\varphi_{-i/2}(x)\xi\), so
\(s_\varphi(x,y)=\langle\sigma^\varphi_{-i/2}(x)\xi,y^*\xi\rangle=\varphi(y\sigma^\varphi_{-i/2}(x))\). For
\(x\in M_\varphi\) the constant function extends \(t\mapsto\sigma^\varphi_t(x)\), so \(\sigma^\varphi_{-i/2}(x)=x\), and
\(\varphi(yx)=\varphi(xy)\) by (B6).

(vi) Here \(\sigma^\varphi_z(x)=\rho^{iz}x\rho^{-iz}\) is entire, so by (v)
\(s_\varphi(x,y)=\mathrm{Tr}_M(\rho y\rho^{1/2}x\rho^{-1/2})=\mathrm{Tr}_M(\rho^{1/2}x\rho^{1/2}y)\). If \(M\) is
abelian, \(M_\varphi=M\) and (v) applies. \(\square\)

**Proposition 7.2 (the adjoint map).** Let \(\varphi_1,\varphi_2\) be faithful normal states of von Neumann algebras
\(M_1,M_2\), and \(\gamma\colon M_1\to M_2\) a ucp map with \(\varphi_2\circ\gamma=\varphi_1\). There is a unique linear
map \(\gamma^\dagger\colon M_2\to M_1\) with
\[
s_{\varphi_1}(\gamma^\dagger(x),y)=s_{\varphi_2}(x,\gamma(y))\qquad(x\in M_2,\ y\in M_1).
\tag{7.1}
\]

(a) \(\gamma^\dagger\) is ucp and \(\varphi_1\circ\gamma^\dagger=\varphi_2\).

(b) If \(\gamma'\colon M_0\to M_1\) is ucp with \(\varphi_1\circ\gamma'=\varphi_0\) (faithful normal), then
\((\gamma\circ\gamma')^\dagger=\gamma'^\dagger\circ\gamma^\dagger\). Moreover \(\gamma^{\dagger\dagger}=\gamma\).

(c) Suppose \(M_1\subset M_2\) is a von Neumann subalgebra with \(\sigma^{\varphi_2}_t(M_1)=M_1\) for all \(t\),
\(\varphi_1=\varphi_2|_{M_1}\), and \(\gamma\) is the inclusion map. Then \(\gamma^\dagger\) is the
\(\varphi_2\)-preserving conditional expectation of (B7).

*Proof.* *Existence and positivity.* Let \(0\le x\le1\) in \(M_2\). The functional \(y\mapsto s_{\varphi_2}(x,\gamma(y))\)
on \(M_1\) is positive (Lemma 7.1(ii) and positivity of \(\gamma\)) and at most \(\varphi_2\circ\gamma=\varphi_1\). By
Lemma 7.1(iv) it equals \(s_{\varphi_1}(x',\cdot)\) for a unique \(x'\) with \(0\le x'\le1\). Every \(x\in M_2\) is a
linear combination \(\sum_lc_lx_l\) of elements with \(0\le x_l\le1\); then
\(s_{\varphi_2}(x,\gamma(\cdot))=s_{\varphi_1}(\sum_lc_lx_l',\cdot)\). By Lemma 7.1(iii), \(\gamma^\dagger(x)=\sum_lc_lx_l'\)
is the only element satisfying (7.1), which shows that \(\gamma^\dagger\) is well defined, unique and linear. It maps
\([0,1]\) into \([0,1]\), hence is positive.

(a) By (7.1) and Lemma 7.1(i), \(s_{\varphi_1}(\gamma^\dagger(1),y)=s_{\varphi_2}(1,\gamma(y))=\varphi_2(\gamma(y))=
\varphi_1(y)=s_{\varphi_1}(1,y)\), so \(\gamma^\dagger(1)=1\); and
\(\varphi_1(\gamma^\dagger(x))=s_{\varphi_1}(\gamma^\dagger(x),1)=s_{\varphi_2}(x,1)=\varphi_2(x)\). For complete
positivity let \(\mathrm{tr}\) be the normalized trace on \(M_n\) and consider the ucp map
\(\gamma_n=\gamma\otimes\mathrm{id}\colon M_1\otimes M_n\to M_2\otimes M_n\), which satisfies
\((\varphi_2\otimes\mathrm{tr})\circ\gamma_n=\varphi_1\otimes\mathrm{tr}\). By (B6) the modular operator of
\(\varphi\otimes\mathrm{tr}\) is \(\Delta_\varphi\otimes1\) (the modular operator of a trace is \(1\)), whence
\(s_{\varphi\otimes\mathrm{tr}}(x\otimes a,y\otimes b)=s_\varphi(x,y)\,\mathrm{tr}(ab)\). Therefore
\[
s(x\otimes a,\gamma_n(y\otimes b))=s_{\varphi_2}(x,\gamma(y))\,\mathrm{tr}(ab)=s(\gamma^\dagger(x)\otimes a,y\otimes b),
\]
and by linearity \((\gamma_n)^\dagger=\gamma^\dagger\otimes\mathrm{id}\). The latter is positive by the first step
applied to \(\gamma_n\). So \(\gamma^\dagger\) is \(n\)-positive for every \(n\).

(b) \(s_{\varphi_0}(\gamma'^\dagger\gamma^\dagger x,y)=s_{\varphi_1}(\gamma^\dagger x,\gamma'y)=s_{\varphi_2}(x,\gamma\gamma'y)\),
and uniqueness gives the first formula. By (a), \(\gamma^\dagger\) is ucp and state preserving, so
\(\gamma^{\dagger\dagger}\) is defined, and by symmetry of \(s\),
\(s_{\varphi_2}(\gamma^{\dagger\dagger}y,x)=s_{\varphi_1}(y,\gamma^\dagger x)=s_{\varphi_1}(\gamma^\dagger x,y)=
s_{\varphi_2}(x,\gamma y)=s_{\varphi_2}(\gamma y,x)\) for all \(x\); so \(\gamma^{\dagger\dagger}=\gamma\).

(c) Let \(E\) be the conditional expectation. By (B7), \(\sigma^{\varphi_2}\) restricts to \(\sigma^{\varphi_1}\) on
\(M_1\). Let \(y\in M_1\) be entire for \(\sigma^{\varphi_1}\); then the same entire function extends
\(t\mapsto\sigma^{\varphi_2}_t(y)\), and \(y'=\sigma^{\varphi_2}_{-i/2}(y)=\sigma^{\varphi_1}_{-i/2}(y)\in M_1\). By
Lemma 7.1(v) and the properties of \(E\), for \(x\in M_2\),
\[
s_{\varphi_2}(x,y)=s_{\varphi_2}(y,x)=\varphi_2(xy')=\varphi_2(E(xy'))=\varphi_1(E(x)y')=s_{\varphi_1}(y,E(x))=
s_{\varphi_1}(E(x),y).
\]
Both ends are normal functionals of \(y\) (Lemma 7.1(i)), and entire elements are \(\sigma\)-weakly dense in \(M_1\)
(B6). Hence (7.1) holds with \(E(x)\) in place of \(\gamma^\dagger(x)\), and \(E=\gamma^\dagger\). \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987].

We now use the adjoint to build abelian models. Let \(C_1,\dots,C_n\subset M\) be pairwise commuting
finite-dimensional abelian subalgebras, \(C_0\) the algebra they generate, and \(\gamma_{C}\colon C\to M\) the inclusion
of a subalgebra \(C\), with adjoint taken for \(\varphi|_{C}\) and \(\varphi\).

**Proposition 7.3.** With \(\mu_j=\varphi|_{C_j}\),
\[
H_\varphi(C_1,\dots,C_n)\ge S(\varphi|_{C_0})-\sum_{j=1}^ns_{\mu_j}(\gamma_{C_j}^\dagger\circ\gamma_{C_j}).
\]

*Proof.* Take \(B=C_0\), \(\mu=\varphi|_{C_0}\) (faithful), \(B_j=C_j\) and \(P=\gamma_{C_0}^\dagger\). By Proposition
7.2(a), \(P\) is ucp with \(\mu\circ P=\varphi\), so this is an abelian model. On the abelian algebra \(C_0\),
\(s_\mu(x,y)=\mu(xy)\) (Lemma 7.1(vi)), so the adjoint of the inclusion \(i_j\colon C_j\to C_0\) is characterized by
\(\mu(i_j^\dagger(x)y)=\mu(xy)\) for \(y\in C_j\): it is the \(\mu\)-preserving conditional expectation \(E_j\). By
Proposition 7.2(b), \(E_jP=i_j^\dagger\gamma_{C_0}^\dagger=(\gamma_{C_0}i_j)^\dagger=\gamma_{C_j}^\dagger\), so
\(\rho_j=\gamma_{C_j}^\dagger\gamma_{C_j}\). Since \(\bigvee_jB_j=C_0\), the entropy of the model is the right-hand
side. \(\square\)

Concretely, if \(e\) runs over the minimal projections of \(C_0\), then \(\mu(e\,\gamma_{C_0}^\dagger(y))=
s_\varphi(y,e)\), so \(P(y)=\sum_e\varphi(e)^{-1}s_\varphi(e,y)\,e\): the model is the decomposition
\(\varphi=\sum_es_\varphi(e,\cdot)\) of \(\varphi\) into the positive functionals \(\varphi^{1/2}e\varphi^{1/2}\).

**Lemma 7.4.** Let \(C\subset M\) be a finite-dimensional abelian subalgebra with minimal projections
\(e_1,\dots,e_r\), \(\mu=\varphi|_C\), and put \(\mu_{ab}=s_\varphi(e_a,e_b)\ge0\), \(\mu_a=\varphi(e_a)\). Then
\(\sum_b\mu_{ab}=\mu_a\), \(\mu_{ab}=\mu_{ba}\), and
\[
s_\mu(\gamma_C^\dagger\circ\gamma_C)=\sum_{a,b}\eta(\mu_{ab})-\sum_a\eta(\mu_a).
\]

*Proof.* \(\mu_{ab}\ge0\) by Lemma 7.1(ii), \(\sum_b\mu_{ab}=s_\varphi(e_a,1)=\mu_a\), and symmetry is Lemma 7.1(i). Let
\(\rho=\gamma_C^\dagger\gamma_C\colon C\to C\). Then \(\mu\circ\rho=\varphi\circ\gamma_C=\mu\) by Proposition
7.2(a), so \(s_\mu(\rho)=\sum_b\mu_bS(\rho_b)\). The state \(\rho_b\) of \(C\) is
\(\rho_b(e_a)=\mu_b^{-1}\mu(e_b\rho(e_a))=\mu_b^{-1}s_\mu(\gamma_C^\dagger(e_a),e_b)=\mu_b^{-1}s_\varphi(e_a,e_b)=
\mu_{ab}/\mu_b\), using Lemma 7.1(vi) on \(C\) and (7.1). Hence
\(s_\mu(\rho)=\sum_b\mu_b\sum_a\eta(\mu_{ab}/\mu_b)=\sum_{a,b}\big(\eta(\mu_{ab})+\mu_{ab}\log\mu_b\big)=
\sum_{a,b}\eta(\mu_{ab})-\sum_b\eta(\mu_b)\). \(\square\)

So the defect vanishes when the matrix \((\mu_{ab})\) is diagonal, that is, when
\(s_\varphi(e_a,e_b)=0\) for \(a\ne b\). By Lemma 7.1(v) this happens when \(C\subset M_\varphi\): then
\(\mu_{ab}=\varphi(e_ae_b)=\delta_{ab}\mu_a\). Proposition 7.3 and Lemma 7.4 thus give a second proof of Theorem 6.2
for faithful normal states, and a quantitative lower bound in general:
\[
H_\varphi(C_1,\dots,C_n)\ge S(\varphi|_{C_0})-\sum_{j=1}^n\Big(\sum_{a,b}\eta(\mu^{(j)}_{ab})-\sum_a\eta(\mu^{(j)}_a)\Big).
\tag{7.2}
\]
Exercise 3 evaluates (7.2) on \(M_2\).

## 8. Subalgebras that nearly commute with the state

This section gives the lower bound needed for lattice systems. There the local algebras are not invariant under the
modular group, but, after shrinking them a little, the modular group moves them only slightly. We keep \(M\),
\(\varphi\) faithful normal, and the notation of Section 7.

**Lemma 8.1.** Consider a von Neumann subalgebra \(N\subset M\), with \(\psi=\varphi|_N\), inclusion
\(\gamma\colon N\to M\) and adjoint \(\gamma^\dagger\colon M\to N\).

(a) If \(x\in N\) and \(z\in M\) satisfy \(s_\varphi(z,y)=s_\psi(x,y)\) for all \(y\in N\), then \(\gamma^\dagger(z)=x\)
and \(\|\gamma^\dagger(x)-x\|\le\|x-z\|\).

(b) If \(x\in D(\sigma^\psi_{-i/2})\) and \(x'=\sigma^\psi_{-i/2}(x)\in D(\sigma^\varphi_{i/2})\), then
\(z=\sigma^\varphi_{i/2}(x')\) satisfies the hypothesis of (a). Hence
\[
\|\gamma^\dagger\gamma(x)-x\|\le\|\sigma^\varphi_{i/2}(\sigma^\psi_{-i/2}(x))-x\| .
\]
When \(N\) is finite dimensional with \(\psi=\mathrm{Tr}_N(\rho\,\cdot\,)\), every \(x\in N\) is in
\(D(\sigma^\psi_{-i/2})\) and \(\sigma^\psi_{-i/2}(x)=\rho^{1/2}x\rho^{-1/2}\).

*Proof.* (a) By (7.1), \(s_\psi(\gamma^\dagger(z),y)=s_\varphi(z,y)=s_\psi(x,y)\) for all \(y\in N\), so
\(\gamma^\dagger(z)=x\) by Lemma 7.1(iii). Hence \(\gamma^\dagger(x)-x=\gamma^\dagger(x-z)\), and \(\gamma^\dagger\) is
contractive, being ucp.

(b) By Lemma 7.1(v) for \((N,\psi)\), \(s_\psi(x,y)=\psi(yx')=\varphi(yx')\). By (0.1) with \(\alpha=\tfrac12\),
\(x'\xi\in D(\Delta^{-1/2})\) and \(\Delta^{-1/2}x'\xi=z\xi\); so \(\Delta^{1/2}z\xi=x'\xi\) and
\(s_\varphi(z,y)=\langle x'\xi,y^*\xi\rangle=\varphi(yx')\). The last sentence is (B6). \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987] states the inequality of (b). Its argument bounds
\(|s_\psi(\gamma^\dagger\gamma(x)-x,y)|\) by \(\|x-z\|\psi(y)\) for \(y\ge0\). By itself this controls only the
numerical radius of \(\gamma^\dagger\gamma(x)-x\), so it gives the norm bound only up to a factor \(2\) when \(x\) is not
self-adjoint; part (a) gives the bound as stated.

**Lemma 8.2.** Let \(N\cong M_m\), \(L\subset N\) a subalgebra with \(L\cong M_{m'}\), \(\varphi\) a faithful state of
\(N\), and \(C\) a maximal abelian subalgebra of \(N\) contained in the centralizer \(N_\varphi\). With the inclusions
\(\gamma_L\), \(\gamma_C\) and \(\mu=\varphi|_C\),
\[
s_\mu(\gamma_C^\dagger\circ\gamma_L)\le2\log(m/m')=\log(\dim N/\dim L).
\]

*Proof.* Let \(\rho\) be the density of \(\varphi\). Since \(C\subset N_\varphi\), \(\rho\) commutes with \(C\), so
\(\rho\in C'\cap N=C\). The minimal projections \(x\) of \(C\) are rank-one projections of \(N\), and \(\rho x=\lambda_xx\)
with \(\lambda_x=\varphi(x)>0\). As \(\sigma^\varphi_t(c)=\rho^{it}c\rho^{-it}=c\) for \(c\in C\), Proposition 7.2(c)
shows that \(\gamma_C^\dagger\) is the \(\varphi\)-preserving conditional expectation \(E_C\). Let
\(\alpha=\gamma_C^\dagger\gamma_L=E_C|_L\colon L\to C\). Then \(\mu\circ\alpha=\varphi|_L\), and for \(l\in L\),
\[
\alpha_x(l)=\frac{\mu(xE_C(l))}{\mu(x)}=\frac{\varphi(xl)}{\varphi(x)}=\frac{\mathrm{Tr}_N(\rho xl)}{\lambda_x}=\mathrm{Tr}_N(xl)=\omega_x(l),
\]
where \(\omega_x\) is the pure vector state of \(N\) given by the range of \(x\). Moreover
\(S(\mu)=\sum_x\eta(\lambda_x)=S(\varphi)\). Hence
\[
s_\mu(\alpha)=S(\varphi)-S(\varphi|_L)+\sum_x\lambda_x\,S(\omega_x|_L).
\]
By (B2), \(N\cong L\otimes L^c\) with \(L^c\cong M_{m/m'}\); subadditivity gives
\(S(\varphi)-S(\varphi|_L)\le S(\varphi|_{L^c})\le\log(m/m')\), and purity of \(\omega_x\) gives
\(S(\omega_x|_L)=S(\omega_x|_{L^c})\le\log(m/m')\). Adding up, \(s_\mu(\alpha)\le2\log(m/m')\). \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987], with the bound \(2\log(\dim N/\dim L)\).

**Theorem 8.3.** Suppose \(\varphi\) is a faithful normal state of \(M\). Let \(N_1,\dots,N_k\subset M\) be pairwise
commuting subalgebras, each isomorphic to \(M_m\), and \(L_j\subset N_j\) subalgebras isomorphic to \(M_{m'}\). Put
\(\varphi^j=\varphi|_{N_j}\) and assume that for some \(\varepsilon\ge0\) and all \(j\) and \(x\in L_j\), the element
\(\sigma^{\varphi^j}_{-i/2}(x)\) lies in \(D(\sigma^\varphi_{i/2})\) and
\[
\big\|\sigma^\varphi_{i/2}\big(\sigma^{\varphi^j}_{-i/2}(x)\big)-x\big\|\le\varepsilon\|x\| .
\tag{8.1}
\]
For each \(j\) let \(C_j\) be maximal among the abelian subalgebras of the centralizer of \(\varphi^j\) in \(N_j\),
and let \(C_0=C_1\vee\cdots\vee C_k\). Then
\[
H_\varphi(N_1,\dots,N_k)\ \ge\ H_\varphi(L_1,\dots,L_k)\ \ge\ S(\varphi|_{C_0})-2kF_{m'^2}(\varepsilon)-2k\log(m/m').
\]

*Proof.* The first inequality is Proposition 1.3(b). Let \(\rho_j\) be the density of \(\varphi^j\) and
\(Z_j=\{y\in N_j:y\rho_j=\rho_jy\}\) the centralizer of \(\varphi^j\) in \(N_j\). As \(\rho_j\) lies in the center of
\(Z_j\), the maximal abelian subalgebra \(C_j\) of \(Z_j\) contains \(\rho_j\); then \(C_j'\cap N_j\subset Z_j\), so
\(C_j'\cap N_j=C_j'\cap Z_j=C_j\), and \(C_j\) is maximal abelian in \(N_j\). The \(C_j\) commute pairwise because the
\(N_j\) do.

Take the abelian model \(B=C_0\), \(\mu=\varphi|_{C_0}\), \(B_j=C_j\), \(P=\gamma_{C_0}^\dagger\), as in the proof of
Proposition 7.3; for the family \((\gamma_{L_j})\) its maps are \(\alpha_j=\gamma_{C_j}^\dagger\gamma_{L_j}\), so
\[
H_\varphi(L_1,\dots,L_k)\ge S(\varphi|_{C_0})-\sum_js_{\mu_j}(\alpha_j),\qquad\mu_j=\varphi|_{C_j}.
\]
Let \(\gamma'_{C_j}\colon C_j\to N_j\) and \(\gamma'_{L_j}\colon L_j\to N_j\) be the inclusions into \(N_j\), with
adjoints taken for \(\varphi^j\). Since \(\gamma_{C_j}=\gamma_{N_j}\gamma'_{C_j}\), Proposition 7.2(b) gives
\(\alpha_j=\gamma'^\dagger_{C_j}\circ(\gamma_{N_j}^\dagger\gamma_{N_j})\circ\gamma'_{L_j}\). Compare it with
\(\alpha'_j=\gamma'^\dagger_{C_j}\circ\gamma'_{L_j}\), which involves only \(N_j\). By Lemma 8.1(b) and (8.1),
\(\|\gamma^\dagger_{N_j}\gamma_{N_j}(x)-x\|\le\varepsilon\|x\|\) for \(x\in L_j\), and \(\gamma'^\dagger_{C_j}\) is
contractive, so \(\|\alpha_j-\alpha'_j\|\le\varepsilon\). By Proposition 1.3(g),
\(s_{\mu_j}(\alpha_j)\le s_{\mu_j}(\alpha'_j)+2F_{m'^2}(\varepsilon)\), and by Lemma 8.2 applied in \(N_j\),
\(s_{\mu_j}(\alpha'_j)\le2\log(m/m')\). \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987].

**Corollary 8.4.** In the situation of Theorem 8.3, the algebra \(N\) generated by \(N_1,\dots,N_k\) is isomorphic to
\(N_1\otimes\cdots\otimes N_k\cong M_{m^k}\), \(C_0\) is maximal abelian in \(N\), \(S(\varphi|_{C_0})\ge S(\varphi|_N)\),
and
\[
S(\varphi|_N)\ \ge\ H_\varphi(N_1,\dots,N_k)\ \ge\ S(\varphi|_N)-2kF_{m'^2}(\varepsilon)-2k\log(m/m').
\]

*Proof.* The map \(y_1\otimes\cdots\otimes y_k\mapsto y_1\cdots y_k\) is a unital \(\ast\)-homomorphism from
\(N_1\otimes\cdots\otimes N_k\) onto \(N\), because the \(N_j\) commute; it is injective since
\(N_1\otimes\cdots\otimes N_k\cong M_{m^k}\) is simple. The minimal projections of \(C_0\) are the products
\(e_1\cdots e_k\) of minimal projections of the \(C_j\), which are rank one in \(N_j\); so they are rank one in \(N\),
and they add up to \(1\). If \(y\in N\) commutes with \(C_0\), then \(y=\sum_eeye\in C_0\); so \(C_0\) is maximal
abelian. Let \(E(y)=\sum_eeye\), the \(\mathrm{Tr}_N\)-preserving conditional expectation onto \(C_0\), and \(\rho\) the
density of \(\varphi|_N\), invertible since \(\varphi\) is faithful. The density of \(\varphi|_{C_0}\) with respect to
\(\mathrm{Tr}_{C_0}=\mathrm{Tr}_N|_{C_0}\) is \(E(\rho)\), and \(\mathrm{Tr}_N(\rho\log E(\rho))=\mathrm{Tr}_N(E(\rho)\log
E(\rho))\) because \(\log E(\rho)\in C_0\). Klein's inequality (B2) gives
\(S(\varphi|_{C_0})-S(\varphi|_N)=\mathrm{Tr}_N\rho(\log\rho-\log E(\rho))\ge\mathrm{Tr}_N(\rho-E(\rho))=0\). The
upper bound is Lemma 6.1, and the lower bound follows from Theorem 8.3. \(\square\)

**Corollary 8.5 (the two-sided estimate in the form used for lattice systems).** Let \(\theta\in\mathrm{Aut}(M,\varphi)\)
and let \(N\cong M_m\) be a subalgebra such that \(N,\theta^{p}(N),\theta^{2p}(N),\dots\) commute pairwise for some
\(p\ge1\). Let \(L\subset N\), \(L\cong M_{m'}\), and suppose (8.1) holds for \(N\), \(L\) and some \(\varepsilon\).
Then, with \(N^{(k)}\) the algebra generated by \(N,\theta^pN,\dots,\theta^{(k-1)p}N\),
\[
S(\varphi|_{N^{(k)}})\ge H_\varphi(N,\theta^pN,\dots,\theta^{(k-1)p}N)\ge S(\varphi|_{N^{(k)}})-2kF_{m'^2}(\varepsilon)-2k\log(m/m').
\]

*Proof.* Put \(\beta=\theta^{(j-1)p}\), \(N_j=\beta(N)\) and \(L_j=\beta(L)\). By Proposition 5.8 with
\(\varphi\circ\beta=\varphi\), \(\beta\sigma^\varphi_t=\sigma^\varphi_t\beta\); composing analytic extensions with the normal
automorphism \(\beta\) shows that \(\beta\) maps \(D(\sigma^\varphi_{i/2})\) onto itself and
\(\sigma^\varphi_{i/2}\beta=\beta\sigma^\varphi_{i/2}\) there. Since \(\beta|_N\) is an isomorphism of
\((N,\varphi|_N)\) onto \((N_j,\varphi|_{N_j})\), it carries the density of \(\varphi|_N\) to that of
\(\varphi|_{N_j}\), so \(\sigma^{\varphi|_{N_j}}_{-i/2}\beta=\beta\sigma^{\varphi|_N}_{-i/2}\) on \(N\) by (B6).
Hence (8.1) for \(N,L\) implies (8.1) for \(N_j,L_j\) with the same \(\varepsilon\), as \(\beta\) is isometric.
Apply Corollary 8.4. \(\square\)

## 9. Exercises

**Exercise 1.** Let \(\theta\in\mathrm{Aut}(A,\varphi)\) have finite order, \(\theta^q=\mathrm{id}\). Show that
\(h_\varphi(\theta)=0\).

*Solution.* The family \((\gamma,\theta\gamma,\dots,\theta^{n-1}\gamma)\) contains only the maps
\(\gamma,\dots,\theta^{q-1}\gamma\), repeated. By Proposition 1.3(d) and (a),
\(a_n(\gamma)=H_\varphi(\gamma,\dots,\theta^{q-1}\gamma)\le qS(\varphi\circ\gamma)\) for \(n\ge q\), so
\(a_n(\gamma)/n\to0\) for every \(\gamma\).

**Exercise 2.** Let \(A=L^\infty[0,1]\) with \(\varphi\) the Lebesgue integral, and for a measurable \(E\subset[0,1]\)
with \(0<|E|<1\) let \(\gamma_E\colon\mathbb C^2\to A\), \(\gamma_E(a_1,a_2)=a_11_E+a_21_{E^c}\). Show that
\(\|\gamma_E-\gamma_{E'}\|=2\) whenever \(E\triangle E'\) has positive measure, while
\(\|\gamma_E-\gamma_{E'}\|_\varphi=2\,|E\triangle E'|^{1/2}\). Compute \(H_\varphi(\gamma_E)\) and check that it is
continuous in the sense of Theorem 4.4 but not in the sense of Proposition 1.3(f).

*Solution.* \((\gamma_E-\gamma_{E'})(a)=(a_1-a_2)(1_E-1_{E'})\) and \(|1_E-1_{E'}|=1_{E\triangle E'}\). For
\(\|a\|\le1\), \(|a_1-a_2|\le2\), with equality at \(a=(1,-1)\). The sup norm of the difference is therefore \(2\) when
\(E\triangle E'\) is not null, and \(\|(\gamma_E-\gamma_{E'})(a)\|_\varphi^2=|a_1-a_2|^2|E\triangle E'|\). The map
\(\gamma_E\) is a \(\ast\)-isomorphism onto the subalgebra \(C_E\) spanned by \(1_E,1_{E^c}\), with inverse a
\(\ast\)-homomorphism; by Proposition 1.3(b) in both directions \(H_\varphi(\gamma_E)=H_\varphi(C_E)\), and by
Corollary 6.3 (\(\varphi\) is a trace) this is \(\eta(|E|)+\eta(1-|E|)\). This depends continuously on \(|E|\), and
\(\big||E|-|E'|\big|\le|E\triangle E'|\), in agreement with Theorem 4.4; the norm distance carries no information.

**Exercise 3.** Let \(A=M_2\), \(\varphi=\mathrm{Tr}(\rho\,\cdot\,)\) with \(\rho=\mathrm{diag}(\lambda,1-\lambda)\) in a
basis \(g_1,g_2\), \(0<\lambda<1\), and let \(C\) be the diagonal algebra of the basis
\(f_\pm=(g_1\pm g_2)/\sqrt2\), with minimal projections \(e_\pm\). Put \(c=\sqrt{\lambda(1-\lambda)}\) and
\(h_2(q)=\eta(q)+\eta(1-q)\).
(i) Compute \(\mu_{ab}=s_\varphi(e_a,e_b)\).
(ii) Show that the entropy defect of Lemma 7.4 equals \(h_2(\tfrac12+c)\).
(iii) Deduce \(\log2-h_2(\tfrac12+c)\le H_\varphi(C)\le\min\{\log2,\ h_2(\lambda)\}\), and discuss
\(\lambda=\tfrac12\) and \(\lambda\to1\).

*Solution.* (i) By Lemma 7.1(vi),
\(\mu_{ab}=\mathrm{Tr}(\rho^{1/2}e_a\rho^{1/2}e_b)=|\langle\rho^{1/2}f_a,f_b\rangle|^2\). With
\(\rho^{1/2}=\mathrm{diag}(\sqrt\lambda,\sqrt{1-\lambda})\) one finds
\(\langle\rho^{1/2}f_+,f_+\rangle=\langle\rho^{1/2}f_-,f_-\rangle=\tfrac12(\sqrt\lambda+\sqrt{1-\lambda})\) and
\(\langle\rho^{1/2}f_+,f_-\rangle=\tfrac12(\sqrt\lambda-\sqrt{1-\lambda})\). Hence
\(\mu_{++}=\mu_{--}=\tfrac14(1+2c)\), \(\mu_{+-}=\mu_{-+}=\tfrac14(1-2c)\), and \(\mu_\pm=\varphi(e_\pm)=\tfrac12\).
(ii) With \(q=\tfrac12+c\) the four numbers \(\mu_{ab}\) are \(\tfrac q2,\tfrac q2,\tfrac{1-q}2,\tfrac{1-q}2\), and
\(\eta(t/2)=\tfrac t2\log2+\tfrac12\eta(t)\). So \(\sum_{a,b}\eta(\mu_{ab})=\log2+h_2(q)\), while
\(\sum_a\eta(\mu_a)=\log2\). The difference is \(h_2(q)\).
(iii) The lower bound is (7.2) with \(n=1\), since \(S(\varphi|_C)=\log2\). The upper bounds are Lemma 6.1 with \(N=C\)
and with \(N=M_2\), where \(S(\varphi)=h_2(\lambda)\). For \(\lambda=\tfrac12\), \(c=\tfrac12\), \(q=1\), the defect is
\(0\) and \(H_\varphi(C)=\log2\), as Corollary 6.3 predicts for the trace. As \(\lambda\to1\), \(c\to0\), the lower bound
tends to \(\log2-\log2=0\) and the upper bound \(h_2(\lambda)\) tends to \(0\), in line with Example 6.7.

**Exercise 4.** In Example 6.8 show that \(h_\varphi(\theta^p)=|p|\,S(\omega)\) for every integer \(p\).

*Solution.* For \(p=0\), \(a_n(\gamma)=H_\varphi(\gamma)\) is bounded, so the entropy is \(0\). Let \(p\ge1\) and let \(I\)
be an interval of length \(l\ge p\). The intervals \(I,I+p,\dots,I+(m-1)p\) overlap or abut, so their union \(J\) is an
interval of length \(l+(m-1)p\). As in Example 6.8, the algebras \(\theta^{ip}(C_I)=C_{I+ip}\) lie in the centralizer,
commute and generate \(C_J\), which is maximal abelian in \(N_J\); and the \(\theta^{ip}(N_I)\) generate \(N_J\).
Corollary 6.4 gives \(H_\varphi(N_I,\theta^pN_I,\dots,\theta^{(m-1)p}N_I)=(l+(m-1)p)S(\omega)\), so
\(h_{\varphi,\theta^p}(N_I)=pS(\omega)\). Corollary 3.4 with the intervals \([-k,k]\), \(2k+1\ge p\), gives
\(h_\varphi(\theta^p)=pS(\omega)\). For \(p<0\), the flip \(\beta\) of \(A\) that sends the site \(k\) to \(-k\) is an
automorphism with \(\varphi\circ\beta=\varphi\) and \(\beta\theta^p\beta^{-1}=\theta^{-p}\); Proposition 2.3(c) gives
\(h_\varphi(\theta^p)=h_\varphi(\theta^{-p})=|p|S(\omega)\).

**Exercise 5.** Let \(A\) be finite dimensional. Show that \(H_\varphi(\mathrm{id}_A)=S(\varphi)\) for every state
\(\varphi\), and that \(H_\varphi(\mathrm{id}_A,\dots,\mathrm{id}_A)=S(\varphi)\) for any number of copies.

*Solution.* Write the density as \(\rho=\sum_k\lambda_kp_k\) with \(p_k\) pairwise orthogonal minimal projections of
\(A\) (diagonalize \(\rho\) in each block). The states \(\omega_k=\mathrm{Tr}_A(p_k\,\cdot\,)\) are pure, so
\(S(\omega_k)=0\), and \(\varphi=\sum_k\lambda_k\omega_k\). By Proposition 6.6, \(\delta_\varphi(\mathrm{id}_A)=0\) and
\(H_\varphi(\mathrm{id}_A)=S(\varphi)\). The second statement follows from Proposition 1.3(d).

## References



- [Connes 1976] A. Connes, *On the classification of von Neumann algebras and their automorphisms*, IHÉS preprint
  IHES/P/76/132, February 1976. Free at
  https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1976-1984/P_76_132/P_76_132_web.pdf
- [Connes 1994] A. Connes, *Noncommutative geometry*, Academic Press, San Diego, CA, 1994. Free at
  https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf
- [Connes–Narnhofer–Thirring 1987] A. Connes, H. Narnhofer and W. Thirring, Dynamical entropy of C\* algebras and von
  Neumann algebras, Comm. Math. Phys. 112 (1987), no. 4, 691–719. Free at https://alainconnes.org/wp-content/uploads/entropy.pdf
- [Connes–Størmer 1975] A. Connes and E. Størmer, Entropy for automorphisms of II₁ von Neumann algebras, Acta Math.
  134 (1975), no. 3–4, 289–306. Free at https://doi.org/10.1007/BF02392105
- [Connes–Størmer 1978] A. Connes and E. Størmer, Homogeneity of the state space of factors of type III₁, J.
  Functional Analysis 28 (1978), no. 2, 187–196. https://doi.org/10.1016/0022-1236(78)90085-X. Free at https://doi.org/10.1016/0022-1236(78)90085-x
- [Araki–Woods 1968] H. Araki and E. J. Woods, A classification of factors, Publ. Res. Inst. Math. Sci. Ser. A 4 (1968),
  51–130. Free at https://doi.org/10.2977/prims/1195195263
