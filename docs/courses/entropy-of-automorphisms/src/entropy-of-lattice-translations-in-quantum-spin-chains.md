# Entropy of lattice translations in quantum spin chains

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. Section 0 was drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

## Introduction

A quantum spin chain is the infinite tensor product \(A=\bigotimes_{x\in\mathbb Z}M_q(\mathbb C)\), and the lattice
translation \(\theta\) shifts every site by one. A translation-invariant state \(\varphi\) carries two numbers that
measure disorder per lattice site. The first is static: the *mean entropy*
\[
s(\varphi)=\lim_{n\to\infty}\frac1n\,S\bigl(\varphi|_{A([0,n-1])}\bigr),
\]
the von Neumann entropy of a block divided by its length. The second is dynamical: the entropy \(h_\varphi(\theta)\)
of the automorphism \(\theta\) in the sense of the lesson "Dynamical entropy of C\*-algebras and von Neumann
algebras", which extends the Kolmogorov–Sinai entropy to states on noncommutative algebras. For a classical lattice
system (an abelian algebra) the two numbers coincide; this is the classical formula for the entropy of a stationary
process. The question of this lesson is whether they coincide for quantum spin chains.

The main results are these.

1. \(h_\varphi(\theta)\le s(\varphi)\) for every translation-invariant state (Section 3).
2. Equality holds under three conditions (Theorem 2.2, proved in Section 5): the state is faithful on its
   von Neumann algebra; it satisfies *modular locality*, which says that deep inside a long block the modular
   structure of the block agrees with that of the whole chain; and a *mutual information* condition, which says that
   a block shares little information, per site, with the far part of the chain to its right.
3. The equilibrium (KMS) state of a finite-range interaction is faithful and satisfies the mutual information
   condition at every temperature (Section 6). For such states \(h_\varphi(\theta)=s(\varphi)\) as soon as modular
   locality holds. We also explain, with an example, why a uniform clustering estimate for correlations is not by
   itself enough for this conclusion.
4. For interactions whose terms commute, modular locality holds exactly at every temperature, because the density
   matrix of a block is the Gibbs factor of its bulk times an operator living at its two ends (Section 7). Hence
   \(h_\varphi(\theta)=s(\varphi)\) for all such states.
5. For quasi-free states of lattice fermions with a smooth two-point function, the analogue of modular locality holds
   at every temperature, with a boundary layer whose width does not depend on the length of the block (Section 8).

The interest of the equality \(h_\varphi(\theta)=s(\varphi)\) is that the dynamical entropy, defined through all
possible finite-dimensional "coarse-grainings" of the algebra, is then the thermodynamic entropy density, a quantity
that can be computed. The difficulty is that the dynamical entropy is not the entropy of any fixed family of
subalgebras: it involves decompositions of the state, and in a non-abelian algebra a decomposition of the state on
one block disturbs its neighbours. Modular theory measures this disturbance.

**What is assumed.** We use the definitions and the Kolmogorov–Sinai theorem of the lessons "Entropy defect and
abelian models" and "Dynamical entropy of C\*-algebras and von Neumann algebras"; Section 1 restates exactly what is
used from them. We also use Tomita–Takesaki theory, KMS states, and elementary facts on the von Neumann entropy of
finite-dimensional states, listed in "Results used from other lessons" with the place where each is proved. Section 0 proves the facts
about equilibrium states that the later sections need: the dynamics of a finite-range interaction and its Gibbs limits,
uniqueness and uniform clustering of its KMS state in one dimension, and the densities and KMS property of quasi-free
states of fermions.

A basic reference is [Connes–Narnhofer–Thirring 1987].

**Conventions.** Logarithms are natural. \(\eta(t)=-t\log t\) for \(t\ge0\) (\(\eta(0)=0\)), and
\(\mathrm h(t)=\eta(t)+\eta(1-t)\) is the binary entropy. Inner products are linear in the first variable. An
*interval* is a set of consecutive integers; \(|\Lambda|\) is the number of elements of \(\Lambda\subset\mathbb Z\).
\(\|\cdot\|_1\) is the trace norm of operators on a Hilbert space.

## Results used from other lessons

**(B1) Entropy in finite dimensions.** Every finite-dimensional C\*-algebra \(D\) has a trace \(\operatorname{Tr}_D\)
taking the value \(1\) on minimal projections. Every state \(\omega\) has a unique density \(\rho_\omega\in D_+\)
with \(\omega=\operatorname{Tr}_D(\rho_\omega\,\cdot)\), and \(S(\omega)=\operatorname{Tr}_D\eta(\rho_\omega)\). For
states \(\omega,\omega'\) the relative entropy is \(D(\omega\|\omega')=\operatorname{Tr}_D\rho_\omega(\log\rho_\omega
-\log\rho_{\omega'})\) (\(+\infty\) unless the support of \(\rho_\omega\) is under that of \(\rho_{\omega'}\)); it does
not depend on the normalization of the trace. Then: (a) \(0\le S(\omega)\le\log\operatorname{Tr}_D(1)\); on
\(M_d(\mathbb C)\), \(S(\omega)\le\log d\). (b) \(D(\omega\|\omega')\ge0\), with equality only for
\(\omega=\omega'\) (Klein's inequality). (c) If \(D_0\subset D\) is a unital \(*\)-subalgebra,
\(D(\omega|_{D_0}\|\omega'|_{D_0})\le D(\omega\|\omega')\) (monotonicity of relative entropy). (d) For states
\(\omega\) on \(D_1\otimes D_2\) with restrictions \(\omega_1,\omega_2\):
\(S(\omega_1)+S(\omega_2)-S(\omega)=D(\omega\|\omega_1\otimes\omega_2)\ge0\) (subadditivity); if \(D_1,D_2\) are full
matrix algebras and \(\omega\) is pure, \(S(\omega_1)=S(\omega_2)\). (e) \(S\) is continuous on the state space.
Densities: AF-algebras, Section 2 and Lemma 10.2 and, in each summand, Compact and trace-class
operators, Section 6. The formula for \(D\) is Theorem 2.3 of Entropy defect and abelian
models, where \(D\) is defined for positive functionals; (a) is Lemma 3.2(c) there, (b) is Corollary
2.6(a), and (c) is Proposition 2.5(d). In (d), \(\log(\rho_1\otimes\rho_2)=\log\rho_1\otimes1+1\otimes\log\rho_2\) on the
supports, so Theorem 2.3 there gives the identity, and (b) gives the inequality. A pure state has a rank-one density
(Lemma 3.2(c) there), so it is the vector state of some \(\psi=\sum_{i,j}c_{ij}e_i\otimes f_j\); the densities of
\(\omega_1\) and \(\omega_2\) are then \(CC^*\) and \((C^*C)^{\mathsf T}\),
\(C=(c_{ij})\), which have the same nonzero eigenvalues with multiplicity, so \(S(\omega_1)=S(\omega_2)\) by Lemma 3.2(d)
there. (e) follows from (B2).

**(B2) Continuity of entropy.** If \(\omega,\omega'\) are states on \(M_d(\mathbb C)\) and
\(T=\frac12\|\rho_\omega-\rho_{\omega'}\|_1\), then \(|S(\omega)-S(\omega')|\le T\log(d-1)+\mathrm h(T)\) (the
Fannes–Audenaert inequality). Note that \(\|\rho_\omega-\rho_{\omega'}\|_1=\|\omega-\omega'\|\), the norm of the
functional. Proved in Operator convex functions and the continuity of entropy, Theorem 7.1,
for every \(T\in[0,1]\), with the cases of equality. See also [Audenaert 2007].

**(B3) Standard form.** Consider a von Neumann algebra \(M\) on \(H\) with a cyclic and separating vector \(\xi\), and
put \(\varphi=\langle\,\cdot\,\xi,\xi\rangle\). The operator \(x\xi\mapsto x^*\xi\) (\(x\in M\)) is closable; its closure
is \(S=J\Delta^{1/2}\) with \(J\) an antiunitary involution and \(\Delta\) positive, self-adjoint and injective. Then
\(J\xi=\xi\), \(JMJ=M'\), \(J\Delta^{1/2}J=\Delta^{-1/2}\), \(\Delta^{it}M\Delta^{-it}=M\), and
\(\sigma^\varphi_t(x)=\Delta^{it}x\Delta^{-it}\) is the modular group. Proved in the course *Modular theory and
weights*: The modular group and its analytic algebra, §MF-01 for the closure and its
polar decomposition, §MF-05 for \(JMJ=M'\), §MF-06 for \(\Delta^{it}M\Delta^{-it}=M\).

**(B4) Entire elements.** In the situation of (B3), if \(w\in M\) and \(t\mapsto\sigma^\varphi_t(w)\) extends to an
entire function \(z\mapsto\sigma^\varphi_z(w)\) with values in \(M\) (norm-continuous and holomorphic), then
\(w\xi\in D(\Delta^{-1/2})\) and \(\Delta^{-1/2}w\xi=\sigma^\varphi_{i/2}(w)\xi\). Products of entire elements are
entire and \(\sigma^\varphi_z(w_1w_2)=\sigma^\varphi_z(w_1)\sigma^\varphi_z(w_2)\). Proved in Analytic elements and
strip arguments, Theorem 9.1: part (2) for products, and part (4) with \(W_t=\Delta^{it}\), for which
\(W_{i/2}=\Delta^{-1/2}\) and \(W_{i/2}\xi=\xi\).

**(B5) KMS states.** Let \(\tau\) be a strongly continuous one-parameter group of automorphisms of a C\*-algebra
\(A\) and \(\beta>0\). If \(\varphi\) is a \((\tau,\beta)\)-KMS state (defined in Section 0.1), its GNS vector is
separating for \(\pi_\varphi(A)''\), and \(\sigma^\varphi_t(\pi_\varphi(x))=\pi_\varphi(\tau_{-\beta t}(x))\) for \(x\in A\).
Proved in Proposition 0.4, from From a C\*-modular condition to the GNS von Neumann algebra,
§KL-07.

**(B6) Dynamics of finite-range interactions.** Let \(\Phi=\Phi^*\in A([0,r])\) and, for a finite interval
\(\Lambda\), \(H_\Lambda=\sum_{j:[j,j+r]\subset\Lambda}\theta^j(\Phi)\). With \(\Lambda_L=[-L,L]\), the limit
\(\tau_t(x)=\lim_{L\to\infty}e^{itH_{\Lambda_L}}xe^{-itH_{\Lambda_L}}\) exists in norm for every \(x\in A\) and
defines a strongly continuous group of automorphisms commuting with \(\theta\). For \(\beta>0\) let \(\varphi_L\) be
the state \(\operatorname{Tr}(e^{-\beta H_{\Lambda_L}}\,\cdot\,)/\operatorname{Tr}(e^{-\beta H_{\Lambda_L}})\) on
\(A(\Lambda_L)\) tensored with the normalized trace on \(A(\mathbb Z\setminus\Lambda_L)\). Every weak\* limit point of
\((\varphi_L)_L\) is a \((\tau,\beta)\)-KMS state. Proved in Theorems 0.6 and 0.7; see also [Naaijkens, Sections 3.3 and
3.4].

**(B7) Uniqueness in one dimension.** For \(\Phi\) as in (B6) and every \(\beta>0\) there is exactly one
\((\tau,\beta)\)-KMS state. Proved in Theorem 0.10; the result is due to [Araki 1969].

**(B8) Uniform clustering in one dimension.** For \(\Phi\) as in (B6), \(\beta>0\) and the KMS state \(\varphi\) of
(B7): for every \(\eta>0\) there is \(p\in\mathbb N\) with
\(|\varphi(Q_1Q_2)-\varphi(Q_1)\varphi(Q_2)|\le\eta\|Q_1\|\|Q_2\|\) for all \(Q_1\in A((-\infty,-p])\) and
\(Q_2\in A([p,\infty))\). Proved in Theorem 0.13; the result is due to [Araki 1969].

**(B9) The CAR algebra.** Let \(K\) be a Hilbert space and \(\mathrm{CAR}(K)\) the C\*-algebra generated by elements
\(a^*(f)\), \(f\in K\), depending linearly on \(f\), with \(a(f)=a^*(f)^*\), \(\{a(f),a^*(g)\}=\langle g,f\rangle1\)
and \(\{a(f),a(g)\}=0\). (a) \(\|a^*(f)\|=\|f\|\). For a closed subspace \(K_1\), the C\*-subalgebra
\(\mathrm{CAR}(K_1)\) generated by \(a^*(f)\), \(f\in K_1\), is a copy of \(\mathrm{CAR}(K_1)\); if
\(\dim K_1=d<\infty\), it is isomorphic to \(M_{2^d}(\mathbb C)\) and each of its elements is a noncommutative
polynomial in the \(a(f),a^*(f)\), \(f\in K_1\). (b) For every operator \(0\le T\le1\) on \(K\) there is a unique state
\(\omega_T\) with
\(\omega_T(a^*(f_m)\cdots a^*(f_1)a(g_1)\cdots a(g_{m'}))=\delta_{mm'}\det(\langle Tf_i,g_j\rangle)_{i,j}\) (the
gauge-invariant quasi-free state); its restriction to \(\mathrm{CAR}(K_1)\) is \(\omega_{T_1}\) with
\(T_1=P_1TP_1|_{K_1}\). (c) If \(\dim K_1<\infty\) and \(0<T_1<1\), the density of \(\omega_{T_1}\) on
\(\mathrm{CAR}(K_1)\) is \(e^{-d\Gamma(h_1)}/\operatorname{Tr}e^{-d\Gamma(h_1)}\) with \(h_1=\log(T_1^{-1}-1)\) and
\(d\Gamma\) as in Section 8. (d) If \(\delta\le T\le1-\delta\) for some \(\delta>0\) and \(h=\log(T^{-1}-1)\), then
\(\omega_T\) is a \((\alpha,1)\)-KMS state for the Bogoliubov group \(\alpha_t(a^*(f))=a^*(e^{ith}f)\).
Parts (a) and (b) are proved in Fermions, Fock space and quasi-free
factors: the norm identity is (5) and the
finite-mode structure Theorem 2.1 and Corollary 2.2 there; existence and uniqueness of \(\omega_T\) are Theorem 4.1 (in
the notation there), and the restriction to \(\mathrm{CAR}(K_1)\) has the moments of \(\omega_{T_1}\), so it equals
\(\omega_{T_1}\) by uniqueness. Parts (c) and (d) are proved in Proposition 0.14 and Theorem 0.15; see also [Dereziński 2006, Sections 8.3 and 10].

## 0. Equilibrium states of spin chains and free fermions

This section proves (B5)–(B9). Sections 0.1–0.4 concern the quasi-local algebra \(A\) of Section 2.1 and a
finite-range interaction; Section 0.5 concerns the CAR algebra of (B9) and uses the second quantization of Section
8.1, whose Lemma 8.1 does not depend on this section.

### 0.1 KMS states

Let \(\gamma\) be a strongly continuous one-parameter group of \(*\)-automorphisms of a unital C\*-algebra \(B\),
\(\beta>0\), and \(S_\beta=\{z\in\mathbb C:0\le\operatorname{Im}z\le\beta\}\). An element \(y\) is *entire* if
\(t\mapsto\gamma_t(y)\) extends to a norm-entire function \(z\mapsto\gamma_z(y)\). A state \(\omega\) is a
*\((\gamma,\beta)\)-KMS state* if for all \(x,y\in B\) there is a bounded continuous function \(F_{x,y}\) on \(S_\beta\),
holomorphic in the interior, with
\[
F_{x,y}(t)=\omega(x\gamma_t(y)),\qquad F_{x,y}(t+i\beta)=\omega(\gamma_t(y)x)\qquad(t\in\mathbb R).
\tag{0.1}
\]
For \(\sigma_t=\gamma_{-\beta t}\) the functions \(G_{x,y}(z)=F_{y,x}(i\beta-\beta z)\) satisfy \(G_{x,y}(t)=\omega(\sigma_t(x)y)\)
and \(G_{x,y}(t+i)=\omega(y\sigma_t(x))\), so (0.1) is the modular condition of Analytic elements and strip
arguments, Definition 10.1 for
\(\sigma\); the change of variables is reversible, and \(\gamma\) and \(\sigma\) have the same entire elements, with
\(\gamma_z=\sigma_{-z/\beta}\). By the norm-continuous form of Theorem 9.1 of that lesson, stated after its Definition
10.1, the entire elements form a norm-dense unital \(*\)-subalgebra on which every \(\gamma_z\) is multiplicative, with
\(\gamma_{z+w}=\gamma_z\gamma_w\) and \(\gamma_z(y)^*=\gamma_{\bar z}(y^*)\); and \(z\mapsto\gamma_z(y)\) is bounded on
every horizontal strip of finite width (Theorem 5.2(5)
there).

**Lemma 0.1 (analytic form of the KMS condition).** (a) A \((\gamma,\beta)\)-KMS state \(\omega\) is \(\gamma\)-invariant,
and \(\omega(x\gamma_{i\beta}(y))=\omega(yx)\) for all \(x\in B\) and all entire \(y\).

(b) Let \(\mathcal D\) be a norm-dense linear subspace of entire elements with \(\gamma_t(\mathcal D)\subseteq\mathcal D\)
for real \(t\). If a state \(\omega\) satisfies \(\omega(x\gamma_{i\beta}(y))=\omega(yx)\) for all \(x\in B\) and
\(y\in\mathcal D\), then \(\omega\) is \((\gamma,\beta)\)-KMS, and \(|F_{x,y}|\le\|x\|\|y\|\) on \(S_\beta\).

**Proof.** (a) This is Analytic elements and strip arguments, Theorem
10.3(1) and (2), (i)⇒(ii),
for \(\sigma\): condition (ii) there, \(\omega(\sigma_i(x')y')=\omega(y'x')\), applied to the entire element
\(x'=\gamma_{i\beta}(y)\) and to \(y'=x\), reads \(\omega(yx)=\omega(x\gamma_{i\beta}(y))\).

(b) For \(y\in\mathcal D\) put \(F_{x,y}(z)=\omega(x\gamma_z(y))\). It is continuous on \(S_\beta\), holomorphic inside,
and bounded, since \(\|\gamma_{s+iu}(y)\|=\|\gamma_{iu}(y)\|\) is bounded for \(0\le u\le\beta\). Its values on the real
line are those of (0.1), and the hypothesis applied to \(\gamma_t(y)\in\mathcal D\) gives
\(F_{x,y}(t+i\beta)=\omega(x\gamma_{i\beta}(\gamma_t(y)))=\omega(\gamma_t(y)x)\). For arbitrary \(y\), choose
\(y_n\in\mathcal D\) converging to \(y\). On both boundary lines \(|F_{x,y_n}-F_{x,y_m}|\le\|x\|\,\|y_n-y_m\|\). A
bounded continuous function on a strip, holomorphic inside, is the Poisson integral of its boundary values, with a
positive kernel of total mass one (Lemma 10.6 and Corollary
10.8 there, rescaled from
height \(1\) to height \(\beta\)); so the same bound holds on all of \(S_\beta\). Hence \(F_{x,y_n}\) converges uniformly
on \(S_\beta\) to a bounded continuous function, holomorphic inside, with the boundary values (0.1), automorphisms
being isometric. The Poisson representation also gives \(|F_{x,y}|\le\|x\|\|y\|\). \(\square\)

**Lemma 0.2 (Gibbs states of a trace).** Let \(\operatorname{tr}\) be a tracial state of \(B\), \(H=H^*\in B\), and
\(\omega_H(x)=\operatorname{tr}(e^{-\beta H}x)/\operatorname{tr}(e^{-\beta H})\). Then \(\omega_H\) is a
\((\gamma,\beta)\)-KMS state for \(\gamma_t=\operatorname{Ad}e^{itH}\).

**Proof.** Put \(E=e^{-\beta H}\). Since \(E\ge e^{-\beta\|H\|}1\), \(\operatorname{tr}(E)>0\), and
\(\operatorname{tr}(Ex)=\operatorname{tr}(E^{1/2}xE^{1/2})\ge0\) for \(x\ge0\); so \(\omega_H\) is a state. Every \(y\) is
entire, with \(\gamma_z(y)=e^{izH}ye^{-izH}\), and the trace property gives
\(\operatorname{tr}(Ex\gamma_{i\beta}(y))=\operatorname{tr}(ExEyE^{-1})=\operatorname{tr}(xEy)=\operatorname{tr}(Eyx)\).
Lemma 0.1(b) applies with \(\mathcal D=B\). \(\square\)

**Lemma 0.3 (limits of KMS states).** Let \((\gamma^\lambda)\) be a net of strongly continuous one-parameter
automorphism groups of \(B\), and \(\gamma\) another, such that \(\gamma^\lambda_t(x)\to\gamma_t(x)\) in norm,
uniformly for \(t\) in compact sets, for every \(x\in B\). If \(\omega_\lambda\) is \((\gamma^\lambda,\beta)\)-KMS and
\(\omega_\lambda\to\omega\) weak\*, then \(\omega\) is \((\gamma,\beta)\)-KMS.

**Proof.** For \(r>0\) and \(x\in B\) let \(g_r(u)=\sqrt{r/\pi}\,e^{-ru^2}\),
\[
G^\lambda(z)=\int_{\mathbb R}g_r(u-z)\gamma^\lambda_u(x)\,du,\qquad G(z)=\int_{\mathbb R}g_r(u-z)\gamma_u(x)\,du,
\]
\(x^\lambda_r=G^\lambda(0)\) and \(x_r=G(0)\). By Analytic elements and strip arguments, Proposition
3.1(3),(4) and Theorem
5.2(6), \(x^\lambda_r\) and
\(x_r\) are entire for \(\gamma^\lambda\) and \(\gamma\), with \(\gamma^\lambda_z(x^\lambda_r)=G^\lambda(z)\) and
\(\gamma_z(x_r)=G(z)\), and \(x_r\to x\) in norm as \(r\to\infty\). For \(|z|\le R\),
\(|g_r(u-z)|\le\sqrt{r/\pi}\,e^{rR^2}e^{-ru^2/2}\); splitting the integrals at \(|u|=M\), with \(M\) large, and using the
uniform convergence on \([-M,M]\), we get \(G^\lambda(z)\to G(z)\) in norm, uniformly for \(|z|\le R\). By Lemma 0.1(a),
\(\omega_\lambda(aG^\lambda(i\beta))=\omega_\lambda(x^\lambda_ra)\) for \(a\in B\). Since
\(|\omega_\lambda(aG^\lambda(i\beta))-\omega(aG(i\beta))|\le\|a\|\|G^\lambda(i\beta)-G(i\beta)\|
+|(\omega_\lambda-\omega)(aG(i\beta))|\), and similarly on the right, \(\omega(a\gamma_{i\beta}(x_r))=\omega(x_ra)\). The
span \(\mathcal D\) of the \(x_r\) (\(x\in B\), \(r>0\)) is norm dense, consists of entire elements, and is
\(\gamma\)-invariant, as \(\gamma_t(x_r)=(\gamma_t(x))_r\). Lemma 0.1(b) applies. \(\square\)

**Proposition 0.4 (proof of (B5)).** Let \(\tau\) be a strongly continuous one-parameter automorphism group of a
C\*-algebra \(A\), not necessarily unital, and \(\varphi\) a \((\tau,\beta)\)-KMS state, defined by (0.1). Then
\(\mathcal N=\{a\in A:\varphi(a^*a)=0\}\) is the kernel of the GNS representation \(\pi_\varphi\), and the conclusions of
(B5) hold.

**Proof.** The entire elements are norm dense (Analytic elements and strip arguments, Proposition
3.1(4) and Theorem
5.2(6)), and \(\varphi\) is
\(\tau\)-invariant (From a C\*-modular condition to the GNS von Neumann algebra,
§KL-08, which needs no unit). For \(x\in A\) and entire \(y\), the strip function
\(F_{x,y}\) and \(z\mapsto\varphi(x\tau_z(y))\) agree on the real line, hence on \(S_\beta\) by the Schwarz reflection
principle and the identity theorem; at \(z=i\beta\), \(\varphi(x\tau_{i\beta}(y))=\varphi(yx)\). By the Cauchy–Schwarz
inequality \(|\varphi(a^*c)|^2\le\varphi(a^*a)\varphi(c^*c)\), \(\mathcal N\) is a closed left ideal. For \(a\in\mathcal N\)
and entire \(b\), \(\varphi(b^*a^*ab)=\varphi(a^*ab\,\tau_{i\beta}(b^*))=0\), the last step by the same inequality. So
\(ab\in\mathcal N\) for entire \(b\), and by density for all \(b\): \(\mathcal N\) is a two-sided ideal. If
\(a\in\mathcal N\), then \(\|\pi_\varphi(a)\pi_\varphi(b)\xi_\varphi\|^2=\varphi(b^*a^*ab)=0\) for all \(b\), so
\(\pi_\varphi(a)=0\) (the vectors \(\pi_\varphi(b)\xi_\varphi\) are dense); conversely
\(\varphi(a^*a)=\|\pi_\varphi(a)\xi_\varphi\|^2\). Invariance gives \(\tau_t(\mathcal N)=\mathcal N\), so the dynamics and the
strip functions (0.1) pass to \(A/\mathcal N\), where \(\varphi\) induces a faithful state with the same GNS
representation. For \(\alpha_t=\tau_{-\beta t}\) the condition (0.1) is the modular condition, and From a C\*-modular
condition to the GNS von Neumann algebra, §KL-07, applied to this faithful state,
gives a faithful normal state on \(\pi_\varphi(A)''\) that agrees with \(\varphi\) and has modular group
\(\pi_\varphi\circ\alpha_t\). It is the vector state of \(\xi_\varphi\), since both are normal and agree on
\(\pi_\varphi(A)\); so \(\xi_\varphi\) is separating. For a simple algebra, such as that of Section 2.1,
\(\mathcal N=0\). \(\square\)

### 0.2 Finite-range dynamics

Let \(A\) be the quasi-local algebra of Section 2.1, \(r\ge0\), \(\Phi=\Phi^*\in A([0,r])\), \(g=\|\Phi\|\) and
\(\Phi_j=\theta^j(\Phi)\in A([j,j+r])\). For a finite set \(\mathcal S\subset\mathbb Z\) put
\(H_{\mathcal S}=\sum_{j\in\mathcal S}\Phi_j\) and \(\alpha^{\mathcal S}_z(x)=e^{izH_{\mathcal S}}xe^{-izH_{\mathcal S}}\)
(\(z\in\mathbb C\)). For a finite interval \(\Lambda\), \(H_\Lambda\) of (B6) is \(H_{\mathcal S}\) with
\(\mathcal S=\{j:[j,j+r]\subseteq\Lambda\}\), and we write \(\alpha^\Lambda\) for \(\alpha^{\mathcal S}\). Put
\[
u_R=4rgR\,e^{2rgR},\qquad B_R(\ell)=\exp\bigl(2gR\ell+u_R\bigr)\qquad(R\ge0,\ \ell\ge1).
\tag{0.2}
\]

**Lemma 0.5 (locality estimates).** Let \(x\in A(I)\), where \(I=[a,b]\) is an interval with \(\ell\) points, and
\(I^{(m)}=[a-rm,b+rm]\). For every finite \(\mathcal S\) and \(R\ge0\),
\[
\sup_{|z|\le R}\|\alpha^{\mathcal S}_z(x)\|\le\|x\|B_R(\ell).
\tag{0.3}
\]
If two finite sets \(\mathcal S,\mathcal T\) contain the same indices \(j\) with \([j,j+r]\subseteq I^{(m)}\), then
\[
\sup_{|z|\le R}\|\alpha^{\mathcal S}_z(x)-\alpha^{\mathcal T}_z(x)\|\le2\|x\|e^{2gR\ell}\sum_{k>m}\frac{u_R^k}{k!}.
\tag{0.4}
\]

**Proof.** Expanding \(e^{z\operatorname{ad}(iH_{\mathcal S})}\),
\[
\alpha^{\mathcal S}_z(x)=\sum_{n\ge0}\frac{(iz)^n}{n!}\sum_{j_1,\dots,j_n\in\mathcal S}
[\Phi_{j_n},[\cdots,[\Phi_{j_1},x]\cdots]].
\tag{0.5}
\]
The \(k\)-th nested commutator lies in the algebra of the interval hull of \(I\cup[j_1,j_1+r]\cup\dots\cup[j_k,j_k+r]\),
and, as elements with disjoint supports commute, it vanishes unless every \([j_k,j_k+r]\) meets the hull of \(I\) and the
preceding intervals. Call the \(k\)-th step a *growth step* if \([j_k,j_k+r]\) is not contained in that hull \([u,v]\).
Then the interval contains \(u-1\) or \(v+1\) while meeting \([u,v]\), so \(j_k\in[u-r,u-1]\cup[v-r+1,v]\): at most
\(2r\) choices, and the hull grows by at most \(r\) points. After \(k\) growth steps the hull has at most \(\ell+rk\)
points, which bounds the number of choices at every other step. So at most \(\binom nk(2r)^k(\ell+rk)^{n-k}\) words of
length \(n\) with exactly \(k\) growth steps give nonzero terms, each of norm at most \((2g)^n\|x\|\). With \(n=k+m\),
\[
\sum_{n\ge0}\frac{R^n}{n!}\sum_{j_1,\dots,j_n}\|[\Phi_{j_n},[\cdots,[\Phi_{j_1},x]\cdots]]\|
\le\|x\|\sum_{k,m\ge0}\frac{(4rgR)^k}{k!}\,\frac{(2gR(\ell+rk))^m}{m!}
=\|x\|e^{2gR\ell}\sum_{k\ge0}\frac{u_R^k}{k!}=\|x\|B_R(\ell),
\]
which gives (0.3); the words with more than \(m\) growth steps contribute at most
\(\|x\|e^{2gR\ell}\sum_{k>m}u_R^k/k!\). A word with at most \(m\) growth steps uses only intervals contained in
\(I^{(m)}\), so these words are the same for \(\mathcal S\) and \(\mathcal T\), and (0.4) follows. For \(r=0\) there are
no growth steps and only \(k=0\) occurs. \(\square\)

**Theorem 0.6 (the dynamics; proof of (B6), first part).** (a) For every \(x\in A\) the limit
\(\tau_t(x)=\lim_{L\to\infty}e^{itH_{\Lambda_L}}xe^{-itH_{\Lambda_L}}\) exists in norm, uniformly for \(t\) in compact
sets. The maps \(\tau_t\) form a strongly continuous one-parameter group of automorphisms of \(A\), and
\(\tau_t\theta=\theta\tau_t\).

(b) Every \(x\in A(I)\), \(I\) a finite interval, is entire for \(\tau\): \(\tau_z(x)=\lim_L\alpha^{\Lambda_L}_z(x)\),
uniformly on compact sets of \(z\), and \(\sup_{|z|\le R}\|\tau_z(x)\|\le\|x\|B_R(|I|)\).

(c) Parts (a) and (b) hold, with the same bounds, when a fixed set of terms \(\Phi_j\) is removed from every \(H_{\Lambda_L}\), and when the intervals \(\Lambda_L\) are replaced by any sequence of finite intervals
containing every given finite interval from some index on. Keeping only the terms with \([j,j+r]\subseteq D\)
gives strongly continuous automorphism groups \(\alpha^-\) of \(A(D_-)\) and \(\alpha^+\) of \(A(D_+)\), where
\(D_-=(-\infty,0]\) and \(D_+=[1,\infty)\), whose local elements are entire with the same bounds.

**Proof.** Let \(x\in A(I)\). If \(\Lambda_L,\Lambda_{L'}\supseteq I^{(m)}\), (0.4) bounds
\(\sup_{|z|\le R}\|\alpha^{\Lambda_L}_z(x)-\alpha^{\Lambda_{L'}}_z(x)\|\) by a quantity that tends to \(0\) as
\(m\to\infty\). So \(\alpha^{\Lambda_L}_z(x)\) converges uniformly on compact sets to an entire function
\(F_x\), bounded by (0.3). For arbitrary \(x\in A\), local \(x_0\) and real \(t\),
\(\|\alpha^{\Lambda_L}_t(x)-\alpha^{\Lambda_{L'}}_t(x)\|\le2\|x-x_0\|+\|\alpha^{\Lambda_L}_t(x_0)-\alpha^{\Lambda_{L'}}_t(x_0)\|\),
so the limit \(\tau_t(x)\) exists uniformly for \(t\) in compact sets. Each \(\tau_t\) is a unital \(*\)-homomorphism and
an isometry, as a pointwise norm limit of automorphisms. From
\(\alpha^{\Lambda_L}_s\alpha^{\Lambda_L}_t(x)-\tau_s\tau_t(x)=\alpha^{\Lambda_L}_s\bigl(\alpha^{\Lambda_L}_t(x)-\tau_t(x)\bigr)
+\bigl(\alpha^{\Lambda_L}_s-\tau_s\bigr)(\tau_t(x))\) we get \(\tau_{s+t}=\tau_s\tau_t\); with \(\tau_0=\mathrm{id}\), each
\(\tau_t\) is an automorphism with inverse \(\tau_{-t}\). The orbits are uniform limits on compact sets of continuous
orbits, hence continuous. On the real line \(F_x(t)=\tau_t(x)\), which proves (b). Statement (c) follows from (0.4) in
the same way, since (0.3) and (0.4) hold for arbitrary finite sets of retained terms. Finally
\(\theta(H_{\Lambda_L})=H_{\Lambda_L+1}\), so \(\theta\alpha^{\Lambda_L}_t(x)=\alpha^{\Lambda_L+1}_t(\theta(x))\), and by (c)
the right side tends to \(\tau_t(\theta(x))\). \(\square\)

**Theorem 0.7 (Gibbs limits; proof of (B6), second part).** For \(\beta>0\), every weak\* limit point of the states
\(\varphi_L\) of (B6) is a \((\tau,\beta)\)-KMS state.

**Proof.** The normalized traces of the algebras \(A(\Lambda)\) are compatible with the embeddings, so they define a
tracial state \(\operatorname{tr}\) of \(A\) (positivity and the trace property pass to the norm closure). For \(a\in
A(\Lambda_L)\) and \(b\) supported outside \(\Lambda_L\), \(\operatorname{tr}(e^{-\beta H_{\Lambda_L}}ab)=
\operatorname{tr}(e^{-\beta H_{\Lambda_L}}a)\operatorname{tr}(b)\), so
\(\varphi_L(x)=\operatorname{tr}(e^{-\beta H_{\Lambda_L}}x)/\operatorname{tr}(e^{-\beta H_{\Lambda_L}})\) for all \(x\in A\).
By Lemma 0.2, \(\varphi_L\) is \((\alpha^{\Lambda_L},\beta)\)-KMS on all of \(A\). If \(\varphi\) is a weak\* limit point,
choose a subnet converging to it; Theorem 0.6(a) and Lemma 0.3 show that \(\varphi\) is \((\tau,\beta)\)-KMS. \(\square\)

### 0.3 Uniqueness

**Lemma 0.8.** Let \(\alpha\) be a strongly continuous one-parameter automorphism group of a unital C\*-algebra \(B\)
and \(\omega\) an \((\alpha,\beta)\)-KMS state. For every entire \(b\) and every \(X\ge0\),
\[
\omega(b^*Xb)\le\|\alpha_{-i\beta/2}(b)\|^2\,\omega(X).
\tag{0.6}
\]

**Proof.** Let \(H_\omega\) be the completion of \(B/\{a:\omega(a^*a)=0\}\) for \(\langle[a],[c]\rangle=\omega(c^*a)\), and
\(\pi\) the representation by left multiplication. For entire \(a\), put \(\mathcal J[a]=[\alpha_{i\beta/2}(a^*)]\). By
invariance (Lemma 0.1(a)) and uniqueness of analytic continuation, \(\omega(\alpha_z(c))=\omega(c)\) for entire \(c\) and
all \(z\); with Lemma 0.1(a) again,
\[
\|\mathcal J[a]\|^2=\omega\bigl(\alpha_{-i\beta/2}(a)\,\alpha_{i\beta/2}(a^*)\bigr)=\omega\bigl(a\,\alpha_{i\beta}(a^*)\bigr)
=\omega(a^*a).
\]
So \(\mathcal J\) is well defined and isometric on the dense subspace of classes of entire elements, it satisfies
\(\mathcal J^2=1\) there, and it extends to an antiunitary involution. For entire \(a,c\), direct substitution gives
\(\mathcal J\pi(c)\mathcal J[a]=[a\,\alpha_{i\beta/2}(c^*)]\). With \(c=\alpha_{-i\beta/2}(b)^*\) this is
\([ab]=\mathcal J\pi(\alpha_{-i\beta/2}(b)^*)\mathcal J[a]\), so
\(\omega(b^*a^*ab)\le\|\alpha_{-i\beta/2}(b)\|^2\omega(a^*a)\) for entire \(a\), and by density for all \(a\). Take
\(a=X^{1/2}\). \(\square\)

**Proposition 0.9 (bounded perturbations).** Let \(\alpha\) be a strongly continuous one-parameter automorphism group
of a unital C\*-algebra \(B\), let \(W=W^*\) be entire, and \(M_R=\sup_{|z|\le R}\|\alpha_z(W)\|\).

(a) There is a unique entire function \(U\) with \(U(0)=1\) and \(U'(z)=iU(z)\alpha_z(W)\). Every \(U(z)\) is invertible,
\(\max(\|U(z)\|,\|U(z)^{-1}\|)\le e^{RM_R}\) for \(|z|\le R\), \(U(t)\) is unitary for real \(t\), every \(U(w)\) is entire
with \(\alpha_z(U(w))=U(z)^{-1}U(z+w)\), and \(U(z)^*=U(\bar z)^{-1}\).

(b) \(\alpha^W_t(x)=U(t)\alpha_t(x)U(t)^*\) is a strongly continuous one-parameter automorphism group; every
\(\alpha\)-entire \(x\) is \(\alpha^W\)-entire, with \(\alpha^W_z(x)=U(z)\alpha_z(x)U(z)^{-1}\).

(c) If \(\omega\) is \((\alpha,\beta)\)-KMS and \(E=U(i\beta/2)\), then \(\omega^W(x)=\omega(E^*xE)/\omega(E^*E)\) is an
\((\alpha^W,\beta)\)-KMS state, and
\(\bigl(\|E\|\|E^{-1}\|\bigr)^{-2}\omega\le\omega^W\le\bigl(\|E\|\|E^{-1}\|\bigr)^2\omega\).

(d) For \(B=A\), \(\alpha\) one of the dynamics of Theorem 0.6, and \(W\) a finite sum of terms \(\pm\Phi_j\), \(\alpha^W_t(x)\)
is the limit of \(e^{it(H+W)}xe^{-it(H+W)}\) over the finite-volume Hamiltonians \(H\) defining \(\alpha\).

**Proof.** (a) The series
\[
U(z)=1+\sum_{n\ge1}(iz)^n\int_{0\le t_1\le\dots\le t_n\le1}\alpha_{zt_1}(W)\cdots\alpha_{zt_n}(W)\,dt_1\cdots dt_n
\]
has terms that are entire in \(z\) (differentiate under the integral) and of norm at most \((|z|M_R)^n/n!\) for
\(|z|\le R\), the simplex having volume \(1/n!\). So it converges locally uniformly to an entire solution, with
\(\|U(z)\|\le e^{RM_R}\). A difference of two solutions satisfies, after \(n\) iterations of the integral equation, a bound
\(C(RM_R)^n/n!\) on \(|z|\le R\), so it vanishes. The same construction solves \(V'=-i\alpha_z(W)V\), \(V(0)=1\); then
\((UV)'=0\), so \(UV=1\), and \(VU\) solves \(Y'=-i\alpha_z(W)Y+iY\alpha_z(W)\), \(Y(0)=1\), as does the constant \(1\), so
\(VU=1\). For real \(t\), \(U(t)U(t)^*\) has derivative \(0\), so \(U(t)\) is unitary. For real \(t\), both sides of
\(U(t+w)=U(t)\alpha_t(U(w))\) solve the equation in \(w\) with the same value at \(w=0\). For fixed \(w\), the entire
function \(z\mapsto U(z)^{-1}U(z+w)\) therefore equals \(\alpha_t(U(w))\) on the real line: \(U(w)\) is entire, with the
stated continuation. Finally \(z\mapsto U(\bar z)^*\) and \(z\mapsto U(z)^{-1}\) are entire and agree on the real line.

(b) The cocycle identity \(U(s+t)=U(s)\alpha_s(U(t))\) gives the group law, and continuity of \(U\) gives strong
continuity. For \(\alpha\)-entire \(x\), \(z\mapsto U(z)\alpha_z(x)U(z)^{-1}\) is entire and equals \(\alpha^W_t(x)\) for
real \(t\).

(c) Put \(s=i\beta/2\) and \(d=\omega(E^*E)\); \(d\ge\|E^{-1}\|^{-2}>0\). By (a), \(E^*=U(-s)^{-1}=\alpha_{-s}(E)\) and
\(E\alpha_s(E)=U(2s)\). Lemma 0.1(a) with the entire element \(E^*\) gives
\(\omega(E^*xE)=\omega(xE\alpha_{i\beta}(E^*))=\omega(xU(i\beta))\). For \(x\in B\) and \(\alpha\)-entire \(y\), by (b) and
Lemma 0.1(a),
\[
d\,\omega^W\bigl(x\alpha^W_{i\beta}(y)\bigr)=\omega\bigl(xU(i\beta)\alpha_{i\beta}(y)\bigr)=\omega\bigl(yxU(i\beta)\bigr)
=d\,\omega^W(yx).
\]
The \(\alpha\)-entire elements form a dense subspace that is invariant under every real \(\alpha^W_t\), as
\(\alpha^W_t(y)=U(t)\alpha_t(y)U(t)^{-1}\) is a product of entire elements; Lemma 0.1(b) shows that \(\omega^W\) is
\((\alpha^W,\beta)\)-KMS. For \(X\ge0\), Lemma 0.8 with \(b=E\) gives \(\omega(E^*XE)\le\|\alpha_{-s}(E)\|^2\omega(X)=
\|E\|^2\omega(X)\), and with \(b=E^{-1}\), applied to \(E^*XE\), where \(\alpha_{-s}(E^{-1})=(E^*)^{-1}\), it gives
\(\omega(X)\le\|E^{-1}\|^2\omega(E^*XE)\). With \(X=1\) these bound \(d\), and the comparison follows.

(d) For a finite-volume Hamiltonian \(H\) with dynamics \(\alpha^H\), \(U_H(z)=e^{iz(H+W)}e^{-izH}\) solves
\(U_H'=iU_H\alpha^H_z(W)\), \(U_H(0)=1\), so it is given by the series in (a) with \(\alpha^H\). By Theorem 0.6(b),(c),
\(\alpha^H_z(W)\to\alpha_z(W)\) uniformly on compact sets, with the uniform bounds (0.3); each term of the series
converges, and the factorial bounds dominate the tails. So \(U_H\to U\) uniformly on compact sets, and
\(e^{it(H+W)}xe^{-it(H+W)}=U_H(t)\alpha^H_t(x)U_H(t)^*\to\alpha^W_t(x)\). \(\square\)

**Theorem 0.10 (uniqueness; proof of (B7)).** For every \(\beta>0\) there is exactly one \((\tau,\beta)\)-KMS state
\(\varphi_\beta\). The states \(\varphi_L\) of (B6) converge to it weak\*, and \(\varphi_\beta\circ\theta=\varphi_\beta\).
Moreover, with \(C_\beta=\exp\bigl(4\beta rgB_{\beta/2}(r+1)\bigr)\) and \(\gamma_I\) the Gibbs state
\(\operatorname{Tr}(e^{-\beta H_I}\,\cdot\,)/\operatorname{Tr}(e^{-\beta H_I})\) of a finite interval \(I\),
\[
C_\beta^{-1}\gamma_I\le\varphi_\beta|_{A(I)}\le C_\beta\gamma_I.
\tag{0.7}
\]

**Proof.** A KMS state exists by Theorem 0.7 and weak\* compactness of the state space. Let \(\omega\) be any
\((\tau,\beta)\)-KMS state and \(I\) a finite interval. The set \(\mathcal B(I)\) of indices \(j\) with \([j,j+r]\)
meeting \(I\) but not contained in it has at most \(2r\) elements (as in the proof of Lemma 0.5); put
\(V_I=-\sum_{j\in\mathcal B(I)}\Phi_j\). For large \(\Lambda\), \(H_\Lambda+V_I=H_I+H'\) with \(H'\) supported outside
\(I\), so by Proposition 0.9(d) \(\tau^{V_I}_t(x)=e^{itH_I}xe^{-itH_I}\) for \(x\in A(I)\). By Proposition 0.9(c),
\(\omega^{V_I}\) is \((\tau^{V_I},\beta)\)-KMS, so its restriction to the invariant subalgebra \(A(I)\) is KMS for
\(\operatorname{Ad}e^{itH_I}\). Such a state \(\rho\) is \(\gamma_I\): diagonalize \(H_Ie_i=\lambda_ie_i\) with matrix
units \(e_{ij}\); then \(\operatorname{Ad}e^{itH_I}\) continues to \(e_{ij}\mapsto e^{iz(\lambda_i-\lambda_j)}e_{ij}\), and
Lemma 0.1(a) with \(x=e_{ii}\), \(y=e_{ij}\) gives \(\rho(e_{ij})=0\) for \(i\ne j\), and with \(x=e_{ji}\), \(y=e_{ij}\)
gives \(\rho(e_{ii})=e^{-\beta(\lambda_i-\lambda_j)}\rho(e_{jj})\). By Theorem 0.6(b) each \(\tau_z(\Phi_j)\) has norm at
most \(gB_R(r+1)\) for \(|z|\le R\), so \(\sup_{|z|\le\beta/2}\|\tau_z(V_I)\|\le2rgB_{\beta/2}(r+1)\), and by Proposition
0.9(a), \(\|E\|,\|E^{-1}\|\le\exp(\beta rgB_{\beta/2}(r+1))\). Proposition 0.9(c) now gives (0.7) for \(\omega\).

If \(\omega,\nu\) are two KMS states, (0.7) gives \(\omega(X)\ge C_\beta^{-2}\nu(X)\) for positive local \(X\), and, by
approximating \(X^{1/2}\) by local elements, for all \(X\in A_+\). Put \(c=\frac12C_\beta^{-2}\). Then
\(\rho=(\omega-c\nu)/(1-c)\) is a state, and it is KMS, the identities of Lemma 0.1 being linear in the state. If \(D\) is
the diameter of the set of KMS states in norm, \(\|\omega-\nu\|=(1-c)\|\rho-\nu\|\le(1-c)D\), so \(D\le(1-c)D\) and
\(D=0\). Every weak\* limit point of \((\varphi_L)\) is this state (Theorem 0.7); in the compact state space, a sequence
with a single limit point converges to it. As \(\theta\) commutes with \(\tau\), \(\varphi_\beta\circ\theta\) is KMS, hence
equal to \(\varphi_\beta\). \(\square\)

### 0.4 Uniform clustering

**Proposition 0.11 (half-chains).** For each half-line \(D\in\{D_-,D_+\}\), the group \(\alpha^\pm\) of Theorem
0.6(c) has exactly one \((\alpha^\pm,\beta)\)-KMS state \(\omega_\pm\). Let \(W_0=\sum_{j\le0<j+r}\Phi_j\), a sum of at
most \(r\) terms, and \(\alpha^0=\tau^{-W_0}\). Then \(\alpha^0_t(ab)=\alpha^-_t(a)\alpha^+_t(b)\) for \(a\in A(D_-)\),
\(b\in A(D_+)\); the product state \(\psi=\omega_-\otimes\omega_+\) is \((\alpha^0,\beta)\)-KMS; and there is an invertible
\(E\in A\) with
\[
\varphi_\beta(X)=\psi(E^*XE)/\psi(E^*E)\qquad(X\in A).
\tag{0.8}
\]

**Proof.** By Proposition 0.9(d), \(\alpha^0_t\) is the limit of the finite-volume dynamics of \(H_\Lambda-W_0\), which is
a sum of two commuting Hamiltonians supported in the two half-lines; this gives the factorization. By Proposition
0.9(c), \(\varphi_\beta^{-W_0}\) is \((\alpha^0,\beta)\)-KMS, and its restrictions to the invariant subalgebras
\(A(D_\pm)\) are KMS for \(\alpha^\pm\). Uniqueness on a half-line is proved as in Theorem 0.10: for a finite interval
\(I\subset D\), remove the at most \(2r\) retained terms that meet \(I\) without being contained in it; the bounds of
Theorem 0.6(b) hold for \(\alpha^\pm\), so every half-line KMS state satisfies (0.7), and the convexity argument applies.

The product state \(\psi\) exists: on a finite interval meeting both half-lines take the tensor product of the
restricted density matrices; these states are compatible and extend to \(A\), and
\(\psi(ab)=\omega_-(a)\omega_+(b)\). For \(a_\pm\in A(D_\pm)\) and \(\alpha^\pm\)-entire \(b_\pm\),
\[
\psi\bigl(a_-a_+\alpha^0_{i\beta}(b_-b_+)\bigr)=\omega_-\bigl(a_-\alpha^-_{i\beta}(b_-)\bigr)\,
\omega_+\bigl(a_+\alpha^+_{i\beta}(b_+)\bigr)=\omega_-(b_-a_-)\,\omega_+(b_+a_+)=\psi(b_-b_+a_-a_+).
\]
The products \(b_-b_+\) span a dense \(\alpha^0\)-invariant subspace of \(\alpha^0\)-entire elements, and the products
\(a_-a_+\) span a dense subspace; Lemma 0.1(b) shows that \(\psi\) is \((\alpha^0,\beta)\)-KMS. The element \(W_0\) is
\(\alpha^0\)-entire (Theorem 0.6(c)), and perturbing \(\alpha^0\) by \(W_0\) restores the finite-volume Hamiltonians
\(H_\Lambda\), hence \(\tau\) (Proposition 0.9(d)). By Proposition 0.9(c), \(\psi^{W_0}\) is \((\tau,\beta)\)-KMS, so it is
\(\varphi_\beta\) by Theorem 0.10; this is (0.8) with \(E\) the element \(U(i\beta/2)\) of Proposition 0.9 for \(\alpha^0\)
and \(W_0\). \(\square\)

**Lemma 0.12 (decorrelation from a receding tail).** Let \(\omega\) be \(\omega_-\) or \(\omega_+\), and let \(T_p\) be
\(A((-\infty,-p])\) or \(A([p,\infty))\) accordingly. For every \(a\) in the half-line algebra,
\[
m_p(a)=\sup\bigl\{|\omega(aQ)-\omega(a)\omega(Q)|:Q\in T_p,\ \|Q\|\le1\bigr\}\longrightarrow0\qquad(p\to\infty).
\tag{0.9}
\]

**Proof.** First, \(\sup\{\|[x,Q]\|:Q\in T_p,\ \|Q\|\le1\}\to0\) for every \(x\): it is \(0\) for large \(p\) when \(x\) is
local, and local elements are dense. Suppose that (0.9) fails over positive contractions: there are \(\varepsilon>0\),
\(p_n\to\infty\) and positive contractions \(T_n\in T_{p_n}\) with \(|\omega(aT_n)-\omega(a)\omega(T_n)|\ge\varepsilon\).
The positive functionals \(\rho_n(x)=\omega(T_n^{1/2}xT_n^{1/2})\) have norm \(\omega(T_n)\le1\). The half-line algebra is
separable, so the unit ball of its dual is weak\* metrizable and compact, and after passing to a subsequence
\(\rho_n\to\rho\) weak\*, with \(\rho\ge0\). By the first remark, applied to \(T_n^{1/2}\),
\(|\rho_n(x)-\omega(T_nx)|\le\|[x,T_n^{1/2}]\|\to0\) for each \(x\). For \(x\) arbitrary and \(y\) entire, Lemma 0.1(a)
gives \(\omega(T_nx\alpha_{i\beta}(y))=\omega(yT_nx)\), and \(|\omega(yT_nx)-\omega(T_nyx)|\le\|[y,T_n]\|\|x\|\to0\); in the
limit, \(\rho(x\alpha_{i\beta}(y))=\rho(yx)\). If \(\rho(1)>0\), Lemma 0.1(b) makes \(\rho/\rho(1)\) a KMS state, so
\(\rho=\rho(1)\omega\) by uniqueness; if \(\rho(1)=0\), then \(\rho=0\) and the same holds. Hence
\(\omega(aT_n)-\omega(a)\omega(T_n)=\rho_n(a)-\omega(a)\rho_n(1)+o(1)\to\rho(a)-\omega(a)\rho(1)=0\), a contradiction.
A contraction \(Q\in T_p\) is a combination \(Q_1-Q_2+iQ_3-iQ_4\) of four positive contractions in \(T_p\) (positive and
negative parts of its real and imaginary parts), so \(m_p(a)\) is at most four times the supremum over positive
contractions. \(\square\)

**Theorem 0.13 (uniform clustering; proof of (B8)).** For every \(\beta>0\) and \(\eta>0\) there is \(p\in\mathbb N\) such
that \(|\varphi_\beta(Q_1Q_2)-\varphi_\beta(Q_1)\varphi_\beta(Q_2)|\le\eta\|Q_1\|\|Q_2\|\) for all
\(Q_1\in A((-\infty,-p])\) and \(Q_2\in A([p,\infty))\).

**Proof.** Take \(E\) and \(\psi\) as in (0.8), and \(d=\psi(E^*E)>0\). For a local \(F\) put \(\varepsilon_F=\|E-F\|\),
\(a_F=\varepsilon_F(\|E\|+\|F\|)\) and \(d_F=\psi(F^*F)\). For \(\|X\|\le1\),
\(|\psi(E^*XE)-\psi(F^*XF)|\le a_F\), because \(E^*XE-F^*XF=(E-F)^*XE+F^*X(E-F)\); so \(|d-d_F|\le a_F\), and for
\(a_F<d\) the state \(\varphi_F=\psi(F^*\,\cdot\,F)/d_F\) satisfies \(\|\varphi_\beta-\varphi_F\|\le2a_F/d\). For two states
\(\mu,\nu\) and contractions \(Q_1,Q_2\), the covariances \(\mu(Q_1Q_2)-\mu(Q_1)\mu(Q_2)\) and
\(\nu(Q_1Q_2)-\nu(Q_1)\nu(Q_2)\) differ by at most \(3\|\mu-\nu\|\).

Given \(\eta>0\), choose a local \(F\), supported in \([-m,m]\), with \(\|\varphi_\beta-\varphi_F\|<\eta/6\). Write
\(F^*F=\sum_{j=1}^Na_jb_j\) with \(a_j\in A([-m,0])\) and \(b_j\in A([1,m])\); then
\(d_F=\sum_j\omega_-(a_j)\omega_+(b_j)\). For \(p>m\) and contractions \(Q_1\in A((-\infty,-p])\),
\(Q_2\in A([p,\infty))\), which commute with \(F\) and with the \(a_j,b_j\) of the other half,
\[
\varphi_F(Q_1Q_2)=\frac1{d_F}\sum_{j=1}^N\omega_-(a_jQ_1)\,\omega_+(b_jQ_2).
\]
With \(\ell=\omega_-(Q_1)\), \(v=\omega_+(Q_2)\) and \(e_p=\sum_j\bigl(m^-_p(a_j)\|b_j\|+\|a_j\|m^+_p(b_j)\bigr)\), where
\(m^\pm_p\) are the quantities (0.9) for \(\omega_\pm\), the identity
\(\omega_-(a_jQ_1)\omega_+(b_jQ_2)-\omega_-(a_j)\omega_+(b_j)\ell v=\bigl(\omega_-(a_jQ_1)-\omega_-(a_j)\ell\bigr)\omega_+(b_jQ_2)
+\omega_-(a_j)\ell\bigl(\omega_+(b_jQ_2)-\omega_+(b_j)v\bigr)\) gives \(|\varphi_F(Q_1Q_2)-\ell v|\le e_p/d_F\). Taking
\(Q_2=1\) or \(Q_1=1\) gives \(|\varphi_F(Q_1)-\ell|,|\varphi_F(Q_2)-v|\le e_p/d_F\), so the covariance of \(Q_1,Q_2\) for
\(\varphi_F\) is at most \(3e_p/d_F\). By Lemma 0.12, \(e_p\to0\); choose \(p>m\) with \(e_p/d_F<\eta/6\). Then the
covariance for \(\varphi_\beta\) is less than \(3\eta/6+3\eta/6=\eta\). For general \(Q_1,Q_2\) normalize. \(\square\)

### 0.5 Quasi-free states of fermions

We use the conventions of (B9). In Fermions, Fock space and quasi-free
factors inner products are
linear in the second variable; with \(\langle f,g\rangle_{\mathrm F}=\langle g,f\rangle\), reversing both lists of vectors
in its Theorem 4.1 and transposing the determinant gives the moment formula of (B9)(b), the two reversal signs
cancelling. That theorem gives existence and uniqueness of \(\omega_T\); the paragraph after it gives the restriction to
\(\mathrm{CAR}(K_1)\).

**Proposition 0.14 (proof of (B9)(c)).** Let \(\dim K_1=d<\infty\) and \(0<T_1<1\), with an orthonormal eigenbasis
\(e_1,\dots,e_d\) and eigenvalues \(p_j\). Then the density of \(\omega_{T_1}\) on \(\mathrm{CAR}(K_1)\cong M_{2^d}(\mathbb C)\)
is \(e^{-d\Gamma(h_1)}/\operatorname{Tr}e^{-d\Gamma(h_1)}\), \(h_1=\log(T_1^{-1}-1)\). Consequently, for a self-adjoint
operator \(k\) on \(K_1\), the quasi-free state with covariance \((1+e^k)^{-1}\) is KMS at inverse temperature \(1\) for
the group \(a^*(f)\mapsto a^*(e^{itk}f)\).

**Proof.** Put \(n_j=a^*(e_j)a(e_j)\). The CAR give \(n_j=n_j^*=n_j^2\) (as \(a^*(e_j)^2=0\)), and the \(n_j\) commute: moving
\(a(e_j)\) and \(a^*(e_j)\) past the two factors of \(n_i\) gives two signs that cancel. For \(I=\{i_1<\dots<i_k\}\),
reordering gives \(\prod_{j\in I}n_j=a^*(e_{i_k})\cdots a^*(e_{i_1})a(e_{i_1})\cdots a(e_{i_k})\), the \(k(k-1)/2\) signs
from moving the annihilators and the \(k(k-1)/2\) signs from reversing the creators cancelling; by (B9)(b),
\(\omega_{T_1}(\prod_{j\in I}n_j)=\det(\langle T_1e_{i_a},e_{i_b}\rangle)=\prod_{j\in I}p_j\). For \(S\subseteq\{1,\dots,d\}\)
put \(P_S=\prod_{j\in S}n_j\prod_{j\notin S}(1-n_j)\). These are mutually orthogonal projections with sum \(1\), and
expanding the factors \(1-n_j\),
\[
\omega_{T_1}(P_S)=\sum_{R\subseteq S^c}(-1)^{|R|}\prod_{j\in S\cup R}p_j=\prod_{j\in S}p_j\prod_{j\notin S}(1-p_j)>0.
\]
So the \(2^d\) projections \(P_S\) are nonzero, and they are minimal in \(M_{2^d}(\mathbb C)\). For real
\(\vartheta_1,\dots,\vartheta_d\), Lemma 8.1 with the finite-rank operator \(X=i\sum_j\vartheta_j\langle\,\cdot\,,e_j\rangle e_j\),
for which \(d\Gamma(X)=i\sum_j\vartheta_jn_j\), shows that \(V_\vartheta=e^{i\sum_j\vartheta_jn_j}\) implements the Bogoliubov
automorphism of the unitary \(e^X\), which commutes with \(T_1\); it preserves the moments of (B9)(b), so by uniqueness it
preserves \(\omega_{T_1}\), and the density \(\rho\) satisfies \(V_\vartheta^*\rho V_\vartheta=\rho\). Differentiating in each
\(\vartheta_j\) gives \([\rho,n_j]=0\), so \(\rho\) commutes with every \(P_S\) and, these being minimal,
\(\rho=\sum_S\omega_{T_1}(P_S)P_S\). On the other hand, with \(\epsilon_j=\log((1-p_j)/p_j)\),
\(h_1=\sum_j\epsilon_j\langle\,\cdot\,,e_j\rangle e_j\) and \(d\Gamma(h_1)=\sum_j\epsilon_jn_j\), which equals
\(\sum_{j\in S}\epsilon_j\) on the range of \(P_S\). Since \(1+e^{-\epsilon_j}=(1-p_j)^{-1}\), the normalized weight
\(e^{-\sum_{j\in S}\epsilon_j}/\prod_j(1+e^{-\epsilon_j})\) is \(\prod_{j\in S}p_j\prod_{j\notin S}(1-p_j)\), which proves the
formula. For the last statement, Lemma 8.1 with \(X=itk\) gives \(\operatorname{Ad}e^{itd\Gamma(k)}(a^*(f))=a^*(e^{itk}f)\),
and the state is the Gibbs state of \(H=d\Gamma(k)\) at \(\beta=1\), which is KMS by Lemma 0.2. \(\square\)

**Theorem 0.15 (proof of (B9)(d)).** Let \(\delta\le T\le1-\delta\) for some \(\delta>0\) and \(h=\log(T^{-1}-1)\). Then
\(\alpha_t(a^*(f))=a^*(e^{ith}f)\) defines a strongly continuous one-parameter automorphism group of \(\mathrm{CAR}(K)\),
and \(\omega_T\) is an \((\alpha,1)\)-KMS state. No separability of \(K\) is needed.

**Proof.** The operator \(h\) is bounded and self-adjoint, \(\|h\|\le\log((1-\delta)/\delta)\) for \(\delta\le\frac12\),
and \(T=(1+e^h)^{-1}\). The automorphisms \(\alpha_t\) are the Bogoliubov automorphisms of the unitaries \(e^{ith}\)
(Fermions, Fock space and quasi-free factors, Section
3, equation (8)), so they
form a group. By (B9)(a), \(\|\alpha_t(a^*(f))-\alpha_s(a^*(f))\|=\|(e^{ith}-e^{ish})f\|\to0\) as \(t\to s\); the same holds for
annihilators and then, by telescoping, for every polynomial, and by density of the polynomials \(\mathcal P\) in the
generators for every element. Each element of \(\mathcal P\) is entire, through
\[
\alpha_z(a^*(f))=a^*(e^{izh}f),\qquad\alpha_z(a(f))=a\bigl(e^{i\bar zh}f\bigr)=\sum_{k\ge0}\frac{(-iz)^k}{k!}a(h^kf),
\]
the conjugate in the second formula coming from the conjugate-linearity of \(a\); products and sums of these entire
functions are entire, and two expressions of the same polynomial give the same continuation, as they agree on the real
line. Each generator continuation has norm at most \(e^{|\operatorname{Im}z|\|h\|}\|f\|\).

Put \(M=\max(1,\|h\|)\). For finite Borel partitions of \([-M,M]\) of mesh \(\eta_n\to0\), let \(E_{n,j}\) be the nonzero
spectral projections of \(h\) of the parts, choose \(\lambda_{n,j}\) in the parts, and put
\(h_n=\sum_j\lambda_{n,j}E_{n,j}\), \(T_n=(1+e^{h_n})^{-1}\). Then \(\|h_n-h\|\le\eta_n\), \(\|T_n-T\|\le\eta_n/4\) (the function
\(s\mapsto(1+e^s)^{-1}\) has derivative at most \(1/4\) in absolute value), and
\(|e^{izs}-e^{izt}|\le|z||s-t|e^{|\operatorname{Im}z|M}\) for \(s,t\in[-M,M]\) gives \(e^{izh_n}\to e^{izh}\) in norm,
uniformly on compact sets of \(z\). Let \(\alpha^{(n)}\) be the group of \(h_n\). Telescoping products of generator
continuations gives \(\alpha^{(n)}_z(p)\to\alpha_z(p)\) for \(p\in\mathcal P\), uniformly on compact sets. Also
\(\omega_{T_n}\to\omega_T\) weak\*: the moments of (B9)(b) converge, every polynomial is a combination of normal-ordered
words by the CAR, and polynomials are dense.

Fix \(x,y\in\mathcal P\) and let \(f_1,\dots,f_k\) be the vectors appearing in them. The span \(K_n\) of the vectors
\(E_{n,j}f_l\) is finite-dimensional, contains every \(f_l\) (since \(\sum_jE_{n,j}=1\)), and consists of eigenvectors of
\(h_n\); so it reduces \(h_n\) and \(T_n\), \(x,y\in\mathrm{CAR}(K_n)\), this subalgebra is \(\alpha^{(n)}\)-invariant, and the
restriction of \(\omega_{T_n}\) is the quasi-free state with covariance \(T_n|_{K_n}=(1+e^{h_n|_{K_n}})^{-1}\). By
Proposition 0.14 and Lemma 0.1(a), \(\omega_{T_n}(x\alpha^{(n)}_i(y))=\omega_{T_n}(yx)\). Letting \(n\to\infty\),
\(\omega_T(x\alpha_i(y))=\omega_T(yx)\). By continuity in \(x\), this holds for all \(x\in\mathrm{CAR}(K)\) and
\(y\in\mathcal P\). The subspace \(\mathcal P\) is dense, consists of entire elements and is \(\alpha\)-invariant, so
Lemma 0.1(b) shows that \(\omega_T\) is \((\alpha,1)\)-KMS. \(\square\)

## 1. What is used from the lessons on dynamical entropy

This section restates the definitions and facts from the lessons "Entropy defect and abelian models" and "Dynamical
entropy of C\*-algebras and von Neumann algebras" that are used below. Nothing else from those lessons is needed.

**Entropy defect.** Fix a C\*-algebra \(A_0\) of finite dimension, a finite set \(X\) with \(B=C(X)\), a
probability measure \(\mu\) on \(X\) (a state of \(B\)), and a unital positive linear map \(\varrho:A_0\to B\)
(automatically completely positive, as \(B\) is abelian). For \(x\in X\) the functional \(\varrho_x=\mathrm{ev}_x\circ\varrho\) is a
state of \(A_0\), and \(\mu\circ\varrho=\sum_x\mu(x)\varrho_x\). Put
\[
\varepsilon_\mu(\varrho)=S(\mu\circ\varrho)-\sum_{x\in X}\mu(x)\,S(\varrho_x),\qquad
s_\mu(\varrho)=S(\mu)-\varepsilon_\mu(\varrho).
\tag{1.1}
\]
The number \(s_\mu(\varrho)\) is the *entropy defect* of \(\varrho\). (In those lessons \(\varepsilon_\mu(\varrho)\)
is introduced as the \(\mu\)-average of the relative entropies of the \(\varrho_x\) with respect to
\(\mu\circ\varrho\); for a finite-dimensional \(A_0\) this is the expression (1.1), which is all we use.)

**Abelian models and \(H_\varphi\).** Consider a unital C\*-algebra \(A\) with a state \(\varphi\), and unital
completely positive maps \(\gamma_j:A_j\to A\) (\(j=1,\dots,k\)) whose domains \(A_j\) are finite-dimensional
C\*-algebras. An
*abelian model* for \((A,\varphi,\gamma_1,\dots,\gamma_k)\) consists of a finite-dimensional abelian C\*-algebra
\(B\), a state \(\mu\) of \(B\), unital \(*\)-subalgebras \(B_1,\dots,B_k\subset B\), and a unital completely positive
map \(P:A\to B\) with \(\mu\circ P=\varphi\). For faithful \(\mu\) (the only case used below) let
\(E_j:B\to B_j\) be the \(\mu\)-preserving conditional expectation. The *entropy of the model* is
\[
S\bigl(\mu|_{B_1\vee\dots\vee B_k}\bigr)-\sum_{j=1}^k s_{\mu|_{B_j}}\bigl(E_j\circ P\circ\gamma_j\bigr),
\tag{1.2}
\]
and \(H_\varphi(\gamma_1,\dots,\gamma_k)\) is the supremum of (1.2) over all abelian models. A unital
\(*\)-subalgebra stands for its inclusion map.

The facts used are the following; the numbers in parentheses are those of the lesson "Dynamical entropy of
C\*-algebras and von Neumann algebras".

- **(R1)** \(H_\varphi(\gamma_1,\dots,\gamma_k)\) depends only on the set \(\{\gamma_1,\dots,\gamma_k\}\), and
  enlarging the set does not decrease it (Proposition 1.3(d),(e)).
- **(R2)** If \(\alpha\in\operatorname{Aut}(A)\) and \(\varphi\circ\alpha=\varphi\), then
  \(H_\varphi(\alpha\circ\gamma_1,\dots,\alpha\circ\gamma_k)=H_\varphi(\gamma_1,\dots,\gamma_k)\)
  (Proposition 1.3(c)).
- **(R3)** If a finite-dimensional subalgebra \(N\subset A\) contains the subalgebras \(N_1,\dots,N_k\), then
  \(H_\varphi(N_1,\dots,N_k)\le S(\varphi|_N)\) (Lemma 6.1).
- **(R4)** For \(\theta\in\operatorname{Aut}(A)\) with \(\varphi\circ\theta=\varphi\) and \(\gamma\) as above, the
  limit \(h_{\varphi,\theta}(\gamma)=\lim_{k\to\infty}\frac1kH_\varphi(\gamma,\theta\circ\gamma,\dots,
  \theta^{k-1}\circ\gamma)\) exists, and the *dynamical entropy* is \(h_\varphi(\theta)=\sup_\gamma
  h_{\varphi,\theta}(\gamma)\), over all unital completely positive maps \(\gamma\) into \(A\) whose domain is a
  finite-dimensional C\*-algebra (equivalently, a matrix algebra) (Lemma 2.1, Definition 2.2 and Lemma 1.4).
- **(R5)** (Kolmogorov–Sinai theorem for AF algebras.) If finite-dimensional unital subalgebras
  \(A_1\subset A_2\subset\cdots\) have norm-dense union in \(A\), then \(h_\varphi(\theta)=
  \lim_{n\to\infty}h_{\varphi,\theta}(A_n)\) (Corollary 3.4).

Here \(h_\varphi(\theta)\) is the entropy of \(\theta\) on the C\*-algebra \(A\); by Theorem 5.3 of that
lesson it equals the entropy of the extension of \(\theta\) to the von Neumann algebra \(\pi_\varphi(A)''\). We
shall not use the general lower estimates for \(H_\varphi(N_1,\dots,N_k)\) proved there (Theorem 8.3 and Corollary
8.5); Section 5 builds the abelian model it needs directly, which lets us keep track of every constant.

## 2. Quantum spin chains, mean entropy and the main theorem

### 2.1 The setting

Fix an integer \(q\ge2\). For a finite set \(\Lambda\subset\mathbb Z\) let
\(A(\Lambda)=\bigotimes_{x\in\Lambda}M_q(\mathbb C)\cong M_{q^{|\Lambda|}}(\mathbb C)\), and for
\(\Lambda\subset\Lambda'\) embed \(A(\Lambda)\subset A(\Lambda')\) by \(y\mapsto y\otimes1\). The quasi-local algebra
\(A\) is the norm closure of the union of the \(A(\Lambda)\); for an arbitrary \(\Lambda\subset\mathbb Z\),
\(A(\Lambda)\) is the closure of the union of the \(A(\Lambda_0)\), \(\Lambda_0\subset\Lambda\) finite. The algebras
of disjoint sets commute, and \(A(\Lambda_1\cup\Lambda_2)=A(\Lambda_1)\otimes A(\Lambda_2)\) for disjoint finite sets.
The algebra \(A\) is simple, so every nonzero representation of it is faithful. The *translation* \(\theta\) is the
automorphism of \(A\) that maps the copy of \(M_q(\mathbb C)\) at \(x\) identically onto the copy at \(x+1\); thus
\(\theta(A(\Lambda))=A(\Lambda+1)\).

For a state \(\varphi\) of \(A\) and a finite \(\Lambda\) write \(S_\varphi(\Lambda)=S(\varphi|_{A(\Lambda)})\), and
let \(\rho_\Lambda\) be the density of \(\varphi|_{A(\Lambda)}\). For disjoint finite \(\Lambda_1,\Lambda_2\) the
*mutual information* is
\[
\mathrm I_\varphi(\Lambda_1:\Lambda_2)=S_\varphi(\Lambda_1)+S_\varphi(\Lambda_2)-S_\varphi(\Lambda_1\cup\Lambda_2)
=D\bigl(\varphi|_{A(\Lambda_1\cup\Lambda_2)}\,\big\|\,\varphi|_{A(\Lambda_1)}\otimes\varphi|_{A(\Lambda_2)}\bigr)\ge0 .
\]
More generally, for commuting finite-dimensional unital subalgebras \(D_1\subset A(\Lambda_1)\),
\(D_2\subset A(\Lambda_2)\) we write \(\mathrm I_\varphi(D_1:D_2)=S(\varphi|_{D_1})+S(\varphi|_{D_2})-S(\varphi|_{D_1\vee
D_2})\); here \(D_1\vee D_2=D_1\otimes D_2\subset A(\Lambda_1)\otimes A(\Lambda_2)\), so by (B1)(c),(d)
\[
\mathrm I_\varphi(D_1:D_2)\le\mathrm I_\varphi(\Lambda_1:\Lambda_2).
\tag{2.1}
\]
Indeed the restriction of \(\varphi|_{A(\Lambda_1)}\otimes\varphi|_{A(\Lambda_2)}\) to \(D_1\otimes D_2\) is
\(\varphi|_{D_1}\otimes\varphi|_{D_2}\), and relative entropy decreases under restriction.

**Proposition 2.1 (mean entropy).** Let \(\varphi\) be a translation-invariant state and
\(a_n=S_\varphi([0,n-1])\) (\(a_0=0\)). Then \(a_{n+m}\le a_n+a_m\), the limit \(s(\varphi)=\lim_n a_n/n\) exists and
equals \(\inf_{n\ge1}a_n/n\), \(0\le s(\varphi)\le\log q\), and \(S_\varphi(\Lambda)\ge|\Lambda|\,s(\varphi)\) for every
finite interval \(\Lambda\).

**Proof.** By subadditivity (B1)(d) and translation invariance,
\(a_{n+m}\le S_\varphi([0,n-1])+S_\varphi([n,n+m-1])=a_n+a_m\). Fix \(m\ge1\) and write \(n=km+j\) with
\(0\le j<m\); then \(a_n\le ka_m+a_j\), so \(\limsup_n a_n/n\le a_m/m\). Hence
\(\limsup_na_n/n\le\inf_ma_m/m\le\liminf_na_n/n\). The bounds follow from \(0\le a_n\le n\log q\) (B1)(a). A finite
interval \(\Lambda\) is a translate of \([0,|\Lambda|-1]\), so \(S_\varphi(\Lambda)=a_{|\Lambda|}\ge|\Lambda|s(\varphi)\).
\(\square\)

### 2.2 The three conditions

Let \(\varphi\) be a translation-invariant state with GNS representation \((H,\pi,\xi)\) and
\(M=\pi(A)''\). We identify \(A\) with \(\pi(A)\).

**(F)** *Faithfulness:* \(\xi\) is separating for \(M\).

Under (F) every restriction \(\varphi|_{A(\Lambda)}\), \(\Lambda\) finite, is faithful (if \(\varphi(y^*y)=
\|y\xi\|^2=0\) then \(y=0\)), so \(\rho_\Lambda\) is invertible. The modular group of \(\varphi|_{A(\Lambda)}\) is
\(\sigma^{\varphi_\Lambda}_t(y)=\rho_\Lambda^{it}y\rho_\Lambda^{-it}\); it is entire in \(t\), and
\[
\sigma^{\varphi_\Lambda}_{-i/2}(y)=\rho_\Lambda^{1/2}\,y\,\rho_\Lambda^{-1/2}\qquad(y\in A(\Lambda)).
\]
The element \(\sigma^\varphi_{i/2}(w)\) of \(M\) used below is defined in Definition 4.1; for local elements that are
entire for \(\sigma^\varphi\) it is the value of the analytic continuation at \(i/2\) (Remark 4.2).

For integers \(n\ge1\) and \(N\ge0\) put
\[
J=[0,n-1],\qquad \widehat J=[-N,\,n-1+N],\qquad \psi=\varphi|_{A(\widehat J)} .
\tag{2.2}
\]

**(ML)** *Modular locality:* for every \(\varepsilon>0\) and every \(c>0\) there are integers \(n\ge1/c\) and
\(0\le N\le cn\) such that, with the notation (2.2), for every \(Q\in A(J)\) the element
\(\sigma^\psi_{-i/2}(Q)\) lies in the domain of \(\sigma^\varphi_{i/2}\) and
\[
\bigl\|\sigma^\varphi_{i/2}\bigl(\sigma^\psi_{-i/2}(Q)\bigr)-Q\bigr\|\le\varepsilon\|Q\|.
\tag{2.3}
\]

**(MI)** *Mutual information:* for every \(c>0\) there are integers \(g\ge0\) and \(\ell_0\ge1\) such that
\(\mathrm I_\varphi(\Lambda:F)\le c|\Lambda|\) for every interval \(\Lambda\) with \(|\Lambda|\ge\ell_0\) and every
finite \(F\subset[\max\Lambda+g+1,\infty)\).

If the modular group of \(\varphi\) left \(A(J)\) invariant, the left side of (2.3) would vanish for \(N=0\)
(Exercise 9.1). In general it does not, and (ML) asks that a boundary layer of relative width \(N/n\to0\) suffices to
make the two modular structures agree on \(A(J)\) up to \(\varepsilon\). Condition (MI) holds, for instance, when the
mutual information across any cut of the chain is bounded (take \(g=0\)); this is the case for Gibbs states
(Theorem 6.2).

**Theorem 2.2.** Let \(\varphi\) be a translation-invariant state of the spin chain.

- (a) \(h_\varphi(\theta)\le s(\varphi)\).
- (b) If \(\varphi\) satisfies (F), (ML) and (MI), then \(h_\varphi(\theta)=s(\varphi)\).

Part (a) is Theorem 3.1 and part (b) is Theorem 5.3.

*Reference:* [Connes–Narnhofer–Thirring 1987].

**Example 2.3 (product states).** Let \(\omega\) be a faithful state of \(M_q(\mathbb C)\) with density \(\rho\), and
\(\varphi=\omega^{\otimes\mathbb Z}\). Then \(s(\varphi)=S(\omega)\). Condition (MI) holds with \(g=0\) because
\(\mathrm I_\varphi(\Lambda_1:\Lambda_2)=0\). Condition (ML) holds with \(\varepsilon=0\) and \(N=0\) (Exercise 9.1, or
Theorem 7.3 with \(r=0\)). So \(h_\varphi(\theta)=S(\omega)\). For \(\omega=\frac1q\operatorname{Tr}\) this is the
value \(\log q\) of the noncommutative Bernoulli shift (Exercise 9.2) [Connes–Størmer 1975]. The equality
\(h_\varphi(\theta)=S(\omega)\) holds for every product state, faithful or not, by a direct argument with
maximal abelian subalgebras of the centralizer (Example 6.8 of the lesson "Dynamical entropy of C\*-algebras and von
Neumann algebras").

## 3. The upper bound

**Theorem 3.1.** For every translation-invariant state \(\varphi\), \(h_\varphi(\theta)\le s(\varphi)\).

**Proof.** The algebras \(A_L=A([-L,L])\), \(L\ge1\), increase and their union is dense, so by (R5)
\(h_\varphi(\theta)=\lim_Lh_{\varphi,\theta}(A_L)\). Fix \(L\). For every \(k\ge1\) the algebras
\(A_L,\theta(A_L),\dots,\theta^{k-1}(A_L)\) lie in \(A([-L,L+k-1])\), so by (R3) and translation invariance
\[
\frac1kH_\varphi\bigl(A_L,\theta(A_L),\dots,\theta^{k-1}(A_L)\bigr)\le\frac1kS_\varphi([-L,L+k-1])
=\frac{a_{2L+k}}{k}\xrightarrow[k\to\infty]{}s(\varphi),
\]
with \(a_n\) as in Proposition 2.1. Hence \(h_{\varphi,\theta}(A_L)\le s(\varphi)\) for every \(L\), and the claim
follows. \(\square\)

The upper bound uses nothing but the fact that the algebra generated by \(k\) consecutive translates of a block is a
slightly longer block. The lower bound needs an abelian model whose entropy is close to the entropy of long blocks,
and this is where modular theory enters.

## 4. Modular tools

Throughout this section \(M\) is a von Neumann algebra on \(H\) with a cyclic and separating vector \(\xi\),
\(\varphi=\langle\,\cdot\,\xi,\xi\rangle\), and \(J,\Delta\) are as in (B3).

**Definition 4.1.** Let \(w,z\in M\). We say that *\(w\) is in the domain of \(\sigma^\varphi_{i/2}\) and
\(\sigma^\varphi_{i/2}(w)=z\)* if \(w\xi\in D(\Delta^{-1/2})\) and \(\Delta^{-1/2}w\xi=z\xi\). Since \(\xi\) is
separating, \(z\) is determined by \(w\).

**Remark 4.2.** By (B4), if \(t\mapsto\sigma^\varphi_t(w)\) extends to an entire function, then \(w\) is in the
domain and \(\sigma^\varphi_{i/2}(w)\) is the value of that function at \(i/2\). For a full matrix algebra \(D\) with
a faithful state of density \(\rho\), in its standard form on the Hilbert–Schmidt space \(D\) with \(\xi=\rho^{1/2}\),
one has \(\Delta(y)=\rho y\rho^{-1}\) and \(\sigma_z(w)=\rho^{iz}w\rho^{-iz}\), so
\(\sigma_{i/2}(w)=\rho^{-1/2}w\rho^{1/2}\) and \(\sigma_{-i/2}(w)=\rho^{1/2}w\rho^{-1/2}\); this is the convention
of Section 2.2.

**Lemma 4.3.** If \(w\) is in the domain of \(\sigma^\varphi_{i/2}\) and \(z=\sigma^\varphi_{i/2}(w)\), then
\[
\varphi(aw)=\langle z\,Ja^*J\,\xi,\xi\rangle\qquad\text{for every }a\in M .
\]

**Proof.** For an antiunitary \(J\) one has \(\langle Ju,Jv\rangle=\langle v,u\rangle\), hence
\(\langle u,Jv\rangle=\langle v,Ju\rangle\). Since \(a\xi\in D(S)=D(\Delta^{1/2})\) and \(a^*\xi=J\Delta^{1/2}a\xi\),
\[
\varphi(aw)=\langle w\xi,a^*\xi\rangle=\langle w\xi,J\Delta^{1/2}a\xi\rangle=\langle\Delta^{1/2}a\xi,Jw\xi\rangle .
\]
From \(J\Delta^{1/2}J=\Delta^{-1/2}\) we get \(J\,D(\Delta^{-1/2})=D(\Delta^{1/2})\) and
\(\Delta^{1/2}Jw\xi=J\Delta^{-1/2}w\xi=Jz\xi\). As \(\Delta^{1/2}\) is self-adjoint,
\[
\varphi(aw)=\langle a\xi,\Delta^{1/2}Jw\xi\rangle=\langle a\xi,Jz\xi\rangle=\langle z\xi,Ja\xi\rangle
=\langle z\xi,JaJ\xi\rangle=\langle Ja^*J\,z\xi,\xi\rangle=\langle z\,Ja^*J\,\xi,\xi\rangle,
\]
using \(J\xi=\xi\), \((JaJ)^*=Ja^*J\), and \(Ja^*J\in M'\). \(\square\)

**Definition 4.4 (posterior functionals).** For \(a\in M_+\) define \(\omega_a(y)=\langle y\,JaJ\,\xi,\xi\rangle\),
\(y\in M\).

Since \(JaJ\) is a positive element of \(M'\), \(\omega_a(y)=\|y^{1/2}(JaJ)^{1/2}\xi\|^2\ge0\) for \(y\ge0\); so
\(\omega_a\) is a positive normal functional. Its mass is
\(\omega_a(1)=\langle Ja\xi,\xi\rangle=\langle Ja\xi,J\xi\rangle=\langle\xi,a\xi\rangle=\varphi(a)\). The map
\(a\mapsto\omega_a\) is additive and positively homogeneous, and \(\omega_1=\varphi\). Hence every finite partition
of unity \(1=\sum_ia_i\) by positive elements of \(M\) gives a decomposition \(\varphi=\sum_i\omega_{a_i}\) of
\(\varphi\) into positive functionals. (These are exactly the decompositions produced by positive elements of the
commutant \(M'=JMJ\).)

**Lemma 4.5 (posterior states on a block).** Let \(N\subset M\) be a unital \(*\)-subalgebra isomorphic to a full
matrix algebra, \(\psi=\varphi|_N\), and \(\rho\in N\) the density of \(\psi\) (invertible, as \(\xi\) is separating).
Let \(f\in N\) be a nonzero projection commuting with \(\rho\), and \(y\in N\) such that \(\sigma^\psi_{-i/2}(y)=
\rho^{1/2}y\rho^{-1/2}\) is in the domain of \(\sigma^\varphi_{i/2}\); put
\(z=\sigma^\varphi_{i/2}(\sigma^\psi_{-i/2}(y))\). Then
\[
\Bigl|\frac{\omega_f(y)}{\varphi(f)}-\frac{\psi(fy)}{\psi(f)}\Bigr|\le\|y-z\| .
\]
If moreover \(f\) is a minimal projection of \(N\), then \(\psi(fy)/\psi(f)=\operatorname{Tr}_N(fy)\), a pure state
of \(N\).

**Proof.** Note \(\varphi(f)=\psi(f)=\operatorname{Tr}_N(\rho f)>0\). Apply Lemma 4.3 with \(a=f\) and
\(w=\rho^{1/2}y\rho^{-1/2}\): \(\varphi(fw)=\omega_f(z)\). On the other hand, since \(f\) commutes with \(\rho\),
\[
\varphi(fw)=\operatorname{Tr}_N\bigl(\rho f\rho^{1/2}y\rho^{-1/2}\bigr)=\operatorname{Tr}_N\bigl(\rho^{1/2}f\rho^{1/2}y\bigr)
=\operatorname{Tr}_N(\rho fy)=\psi(fy).
\]
Hence \(\omega_f(y)-\psi(fy)=\omega_f(y-z)\), and \(|\omega_f(y-z)|\le\omega_f(1)\|y-z\|=\varphi(f)\|y-z\|\). If
\(f\) is minimal it has rank one, so \(\rho f=\lambda f\) with \(\lambda=\operatorname{Tr}_N(\rho f)=\psi(f)\), and
\(\psi(fy)=\lambda\operatorname{Tr}_N(fy)\). \(\square\)

Thus the posterior state attached to an eigenprojection \(f\) of the block density is the pure state
\(\operatorname{Tr}_N(f\,\cdot\,)\) up to an error controlled by (2.3). If the modular group of \(\varphi\) left \(N\)
invariant, the error would vanish; in general it is the defect of modular locality.

**Lemma 4.6 (invariant automorphisms).** Let \(\alpha\) be an automorphism of a C\*-algebra \(A\), \(\varphi\) a state
with \(\varphi\circ\alpha=\varphi\), and \((H,\pi,\xi)\) its GNS representation with \(\xi\) separating for
\(M=\pi(A)''\). There is a unitary \(U\) on \(H\) with \(U\pi(x)\xi=\pi(\alpha(x))\xi\) and
\(U\pi(x)U^*=\pi(\alpha(x))\), \(x\in A\). It satisfies \(UJ=JU\) and \(U\Delta U^*=\Delta\), and with
\(\bar\alpha=\operatorname{Ad}U\) on \(M\):
\[
\omega_{\bar\alpha(a)}\bigl(\bar\alpha(y)\bigr)=\omega_a(y)\qquad(a\in M_+,\ y\in M).
\]

**Proof.** \(\|\pi(\alpha(x))\xi\|^2=\varphi(\alpha(x^*x))=\|\pi(x)\xi\|^2\), and \(\pi(\alpha(A))\xi=\pi(A)\xi\) is
dense, so \(U\) extends to a unitary with \(U\xi=\xi\). For \(x,y\in A\),
\(U\pi(x)U^*\pi(\alpha(y))\xi=U\pi(xy)\xi=\pi(\alpha(x))\pi(\alpha(y))\xi\), which gives
\(U\pi(x)U^*=\pi(\alpha(x))\); hence \(\operatorname{Ad}U\) maps \(M\) onto \(M\). For \(x\in M\),
\(U S U^*(x\xi)=US(U^*xU\xi)=U U^*x^*U\xi=x^*\xi=S(x\xi)\). As \(U(M\xi)=M\xi\) and \(S\) is the closure of its
restriction to \(M\xi\), \(USU^*=S\). By uniqueness of the polar decomposition, \(UJU^*=J\) and
\(U\Delta^{1/2}U^*=\Delta^{1/2}\). Finally
\(\omega_{\bar\alpha(a)}(\bar\alpha(y))=\langle UyU^*\,JUaU^*J\,\xi,\xi\rangle=\langle U\,yJaJ\,U^*\xi,\xi\rangle
=\omega_a(y)\), since \(U^*\xi=\xi\). \(\square\)

## 5. The lower bound

### 5.1 Blocks, their centralizers and an abelian model

Throughout this section \(\varphi\) is translation invariant and satisfies (F). Fix \(n\ge1\), \(N\ge0\), and use the
notation (2.2). Put \(L=|\widehat J|=n+2N\), and let \(\rho\) be the density of \(\psi=\varphi|_{A(\widehat J)}\).

Choose an orthonormal basis of \((\mathbb C^q)^{\otimes L}\) consisting of eigenvectors of \(\rho\), and let
\(C_0\subset A(\widehat J)\) be the algebra of operators diagonal in this basis. It is maximal abelian in
\(A(\widehat J)\), it lies in the centralizer of \(\psi\) (it commutes with \(\rho\)), and it contains \(\rho\). Its
minimal projections \(f_a\), \(a\in X_0\), \(|X_0|=q^L\), have rank one. Because \(\rho\in C_0\) and
\(\operatorname{Tr}_{C_0}\) is the restriction of \(\operatorname{Tr}_{A(\widehat J)}\), the density of
\(\varphi|_{C_0}\) is \(\rho\) itself, so
\[
S(\varphi|_{C_0})=S(\psi).
\tag{5.1}
\]
Fix a gap \(g\ge0\) and put \(m=L+g\). For \(j\ge0\) let
\[
\widehat J_j=\widehat J+jm,\quad J_j=J+jm,\quad N_j=A(\widehat J_j),\quad M_j=A(J_j),\quad
C_j=\theta^{jm}(C_0),\quad f^{(j)}_a=\theta^{jm}(f_a).
\]
The intervals \(\widehat J_j\) are pairwise disjoint (since \(m\ge L\)), so the \(C_j\) commute. For \(k\ge1\) the
algebra \(C_{[0,k-1]}\) generated by \(C_0,\dots,C_{k-1}\) is abelian with minimal projections
\(f_x=f^{(0)}_{x_0}f^{(1)}_{x_1}\cdots f^{(k-1)}_{x_{k-1}}\), \(x\in X_0^k\), all nonzero (they are tensor products
of nonzero projections). The numbers \(\mu_k(x)=\varphi(f_x)\) are positive by (F) and sum to \(1\). We regard the
coordinates \(X_0,\dots,X_{k-1}\) as random variables with joint law \(\mu_k\). By translation invariance the law of
\((X_j,\dots,X_{j+l})\) equals that of \((X_0,\dots,X_l)\) (the process is *stationary*), and
\[
S(\varphi|_{C_{[0,k-1]}})=H(X_0,\dots,X_{k-1}),
\]
the Shannon entropy.

**Proposition 5.1 (the entropy of an abelian model).** Suppose that \(0<\varepsilon\le1\) and that for every
\(y\in A(J)\) the element \(\sigma^\psi_{-i/2}(y)\) is in the domain of \(\sigma^\varphi_{i/2}\) and
\(\|\sigma^\varphi_{i/2}(\sigma^\psi_{-i/2}(y))-y\|\le\varepsilon\|y\|\). Then for every \(k\ge1\)
\[
H_\varphi(M_0,M_1,\dots,M_{k-1})\ \ge\ S\bigl(\varphi|_{C_{[0,k-1]}}\bigr)-k\,\delta,\qquad
\delta=4N\log q+\tfrac{\varepsilon}{2}\,n\log q+\mathrm h(\varepsilon/2).
\tag{5.2}
\]

**Proof.** *Step 1: the model.* Identify \(B=C_{[0,k-1]}\) with \(C(X_0^k)\) (the point \(x\) corresponds to the
minimal projection \(f_x\)), let \(\mu=\mu_k\) and \(B_j=C_j\). With the posterior functionals of Definition 4.4
(computed in \(M=\pi(A)''\)) define
\[
P(y)(x)=\frac{\omega_{f_x}(y)}{\varphi(f_x)}\qquad(y\in A,\ x\in X_0^k).
\]
\(P\) is positive and unital (\(\omega_{f_x}(1)=\varphi(f_x)\)), hence completely positive since \(B\) is abelian, and
\(\mu\circ P=\sum_x\omega_{f_x}=\omega_{\sum_xf_x}=\omega_1=\varphi\). So \((B,\mu,(B_j),P)\) is an abelian model
for \((A,\varphi)\) and the inclusions of \(M_0,\dots,M_{k-1}\); its \(\mu\) is faithful and \(B_0\vee\dots\vee
B_{k-1}=B\).

*Step 2: the maps \(E_j\circ P\).* The conditional expectation \(E_j:B\to C_j\) averages over the coordinates other
than \(x_j\): \((E_jb)(a)=\sum_{x:x_j=a}\mu(x)b(x)/\mu_j(a)\) with \(\mu_j(a)=\varphi(f^{(j)}_a)\). Since
\(\sum_{x:x_j=a}f_x=f^{(j)}_a\) and \(a\mapsto\omega_a\) is additive,
\[
(E_j\circ P)(y)(a)=\frac{\omega_{f^{(j)}_a}(y)}{\varphi(f^{(j)}_a)}=:\omega^{(j)}_a(y).
\]
So \(\varrho_j=E_j\circ P|_{M_j}:M_j\to C_j\) has the states \((\varrho_j)_a=\omega^{(j)}_a|_{M_j}\), and
\(\mu_j\circ\varrho_j=\varphi|_{M_j}\).

*Step 3: the entropy defects.* By (1.1),
\[
s_{\mu_j}(\varrho_j)=S(\mu_j)-S(\varphi|_{M_j})+\sum_a\mu_j(a)\,S\bigl(\omega^{(j)}_a|_{M_j}\bigr).
\]
By translation invariance and (5.1), \(S(\mu_j)=S(\varphi|_{C_j})=S(\psi)\) and \(S(\varphi|_{M_j})=S_\varphi(J)\). By
Lemma 4.6 applied to \(\alpha=\theta^{jm}\), \(\omega^{(j)}_a\circ\theta^{jm}=\omega^{(0)}_a\) and
\(\mu_j(a)=\mu_0(a)\), so all \(k\) defects are equal to
\[
s_0=S(\psi)-S_\varphi(J)+\sum_a\mu_0(a)\,S\bigl(\omega^{(0)}_a|_{A(J)}\bigr).
\]
First, \(A(\widehat J)=A(J)\otimes A(\widehat J\setminus J)\) and \(|\widehat J\setminus J|=2N\), so by subadditivity
\(S(\psi)-S_\varphi(J)\le S_\varphi(\widehat J\setminus J)\le2N\log q\). Second, let
\(\tau_a=\operatorname{Tr}_{A(\widehat J)}(f_a\,\cdot\,)\), a pure state of \(A(\widehat J)\). By Lemma 4.5 (with
\(N=A(\widehat J)\) and \(f=f_a\)), \(|\omega^{(0)}_a(y)-\tau_a(y)|\le\varepsilon\|y\|\) for \(y\in A(J)\), i.e.
\(\|\omega^{(0)}_a|_{A(J)}-\tau_a|_{A(J)}\|\le\varepsilon\). By (B1)(d),
\(S(\tau_a|_{A(J)})=S(\tau_a|_{A(\widehat J\setminus J)})\le2N\log q\). By (B2) on \(A(J)\cong M_{q^n}(\mathbb C)\),
with \(T\le\varepsilon/2\le1/2\) and the fact that \(T\mapsto T\log(d-1)+\mathrm h(T)\) increases on \([0,1/2]\),
\[
S\bigl(\omega^{(0)}_a|_{A(J)}\bigr)\le2N\log q+\tfrac\varepsilon2\log(q^n-1)+\mathrm h(\varepsilon/2)
\le2N\log q+\tfrac\varepsilon2\,n\log q+\mathrm h(\varepsilon/2).
\]
Hence \(s_0\le\delta\).

*Step 4.* The entropy (1.2) of the model is \(S(\mu)-ks_0\ge S(\varphi|_{C_{[0,k-1]}})-k\delta\), and
\(H_\varphi(M_0,\dots,M_{k-1})\) is at least this. \(\square\)

The model uses one masa per block and the partition of unity \((f_x)\) of the commutant-side decomposition. When
\(\varphi\) is a product state the posterior states \(\omega^{(j)}_a\) are exactly the pure states \(\tau_a\), and the
only loss is the boundary term \(4N\log q\).

### 5.2 The block process

**Proposition 5.2.** Let \(\iota=\sup\{\mathrm I_\varphi(\widehat J:F):F\subset[\max\widehat J+g+1,\infty)\
\text{finite}\}\). Then for every \(k\ge1\)
\[
S\bigl(\varphi|_{C_{[0,k-1]}}\bigr)\ \ge\ k\bigl(S(\psi)-\iota\bigr).
\]

**Proof.** By the chain rule for Shannon entropy and stationarity,
\[
H(X_0,\dots,X_{k-1})=\sum_{j=0}^{k-1}H(X_j\mid X_{j+1},\dots,X_{k-1})=\sum_{l=0}^{k-1}H(X_0\mid X_1,\dots,X_l),
\]
where the term \(l=0\) is \(H(X_0)\); indeed \(H(X_j\mid X_{j+1},\dots,X_{k-1})=H(X_j,\dots,X_{k-1})-
H(X_{j+1},\dots,X_{k-1})\) and both entropies are unchanged by shifting the indices down by \(j\). For \(l\ge1\),
\(H(X_0\mid X_1,\dots,X_l)=H(X_0)-\mathrm I(X_0;X_1,\dots,X_l)\), and the classical mutual information is
\(\mathrm I_\varphi(C_0:C_{[1,l]})\). The algebra \(C_{[1,l]}\) lies in \(A(F_l)\) with
\(F_l=\bigcup_{j=1}^l\widehat J_j\subset[\min\widehat J+m,\infty)=[\max\widehat J+g+1,\infty)\), and
\(C_0\subset A(\widehat J)\). By (2.1), \(\mathrm I(X_0;X_1,\dots,X_l)\le\mathrm I_\varphi(\widehat J:F_l)\le\iota\).
So every term is at least \(H(X_0)-\iota\), and \(H(X_0)=S(\psi)\) by (5.1). \(\square\)

### 5.3 Proof of the main theorem

**Theorem 5.3.** If the translation-invariant state \(\varphi\) satisfies (F), (ML) and (MI), then
\(h_\varphi(\theta)\ge s(\varphi)\). With Theorem 3.1, \(h_\varphi(\theta)=s(\varphi)\).

**Proof.** *The estimate for fixed parameters.* Let \(n,N,g\) be given, with \(\varepsilon\in(0,1]\) as in
Proposition 5.1, and \(\iota\) as in Proposition 5.2. By definition (R4), \(h_\varphi(\theta)\ge
h_{\varphi,\theta}(A(J))\), and the limit defining \(h_{\varphi,\theta}(A(J))\) may be taken along the multiples
\(km\). The family \(M_0,\dots,M_{k-1}\), i.e. \(\theta^{jm}(A(J))\) for \(j<k\), is part of the family
\(\theta^i(A(J))\), \(0\le i\le km-1\). By (R1) and Propositions 5.1 and 5.2,
\[
\frac1{km}H_\varphi\bigl(A(J),\theta(A(J)),\dots,\theta^{km-1}(A(J))\bigr)\ \ge\ \frac1{km}H_\varphi(M_0,\dots,M_{k-1})
\ \ge\ \frac1m\bigl(S(\psi)-\iota-\delta\bigr).
\]
Letting \(k\to\infty\),
\[
h_\varphi(\theta)\ \ge\ \frac1m\bigl(S(\psi)-\iota-\delta\bigr).
\tag{5.3}
\]

*Choice of parameters.* Let \(0<c\le1\). By (MI) choose \(g\ge0\) and \(\ell_0\) for this \(c\). Put
\(\varepsilon=c\) and \(c'=\min\{c,1/\ell_0,c/\max(g,1)\}\). By (ML) with \(\varepsilon\) and \(c'\) there are
\(n\ge1/c'\) and \(N\le c'n\) for which the hypothesis of Proposition 5.1 holds. Then \(n\ge1/c\), \(n\ge\ell_0\),
\(n\ge g/c\) and \(N\le cn\). Since \(L=n+2N\ge\ell_0\), (MI) gives \(\iota\le cL\). Now estimate the three terms of
(5.3), using \(m=L+g\), \(L\ge n\) and Proposition 2.1:
\[
\frac{S(\psi)}m\ge\frac Lm\,s(\varphi)\ge\Bigl(1-\frac gn\Bigr)s(\varphi)\ge s(\varphi)-c\log q,\qquad
\frac\iota m\le\frac{cL}{m}\le c,
\]
\[
\frac\delta m\le\frac\delta n=\frac{4N}{n}\log q+\frac c2\log q+\frac{\mathrm h(c/2)}{n}\le4c\log q+\frac c2\log q+c .
\]
So \(h_\varphi(\theta)\ge s(\varphi)-c\,(2+\tfrac{11}{2}\log q)\). As \(c\) is arbitrary,
\(h_\varphi(\theta)\ge s(\varphi)\). \(\square\)

**Remark 5.4.** The order of the choices matters. The gap \(g\) is chosen first, from (MI) alone; the block length
\(n\) is chosen afterwards and may be as large as needed. This is why the ratio \(L/m=L/(L+g)\) tends to \(1\). A
mixing hypothesis whose gap had to grow with the block length would not give the full mean entropy; see
Section 6.2.

## 6. Gibbs states of finite-range interactions

### 6.1 Mutual information at every temperature

Let \(\Phi=\Phi^*\in A([0,r])\) with \(r\ge0\), \(\Phi_j=\theta^j(\Phi)\in A([j,j+r])\), and \(H_\Lambda\), \(\tau\),
\(\varphi_L\) as in (B6). For \(\beta>0\) let \(\varphi_\beta\) be the unique \((\tau,\beta)\)-KMS state (B7). By
weak\* compactness of the state space, (B6) and uniqueness, \(\varphi_L\to\varphi_\beta\) weak\*. Since \(\theta\)
commutes with \(\tau\), \(\varphi_\beta\circ\theta\) is again \((\tau,\beta)\)-KMS, so \(\varphi_\beta\) is
translation invariant.

**Lemma 6.1 (Gibbs variational bound).** Let \(D_1,D_2\) be full matrix algebras, \(H=H_1\otimes1+1\otimes H_2+W\)
with \(H_1,H_2,W\) self-adjoint, \(\beta\ge0\), and \(\omega\) the state with density
\(e^{-\beta H}/\operatorname{Tr}e^{-\beta H}\), with restrictions \(\omega_1,\omega_2\). Then
\[
\mathrm I_\omega(D_1:D_2)\le\beta\bigl((\omega_1\otimes\omega_2)(W)-\omega(W)\bigr)\le2\beta\|W\|.
\]

**Proof.** Let \(Z=\operatorname{Tr}e^{-\beta H}\). For any state \(\sigma\), \(D(\sigma\|\omega)=-S(\sigma)+
\beta\sigma(H)+\log Z\), which is \(\ge0\) by (B1)(b) and \(=0\) for \(\sigma=\omega\). Taking
\(\sigma=\omega_1\otimes\omega_2\) and subtracting the identity for \(\omega\),
\[
0\le-S(\omega_1)-S(\omega_2)+S(\omega)+\beta\bigl((\omega_1\otimes\omega_2)(H)-\omega(H)\bigr).
\]
The states \(\omega_1\otimes\omega_2\) and \(\omega\) agree on \(H_1\otimes1\) and \(1\otimes H_2\), so the last
bracket equals \((\omega_1\otimes\omega_2)(W)-\omega(W)\). \(\square\)

This bound on mutual information by the strength of the coupling across a cut is due to
[Wolf–Verstraete–Hastings–Cirac 2008].

**Theorem 6.2.** For every \(\beta>0\), the state \(\varphi_\beta\) satisfies (F), and for every \(a\in\mathbb Z\) and
all finite \(\Lambda_1\subset(-\infty,a]\), \(\Lambda_2\subset[a+1,\infty)\),
\[
\mathrm I_{\varphi_\beta}(\Lambda_1:\Lambda_2)\le2\beta r\|\Phi\|.
\]
In particular \(\varphi_\beta\) satisfies (MI) with \(g=0\).

**Proof.** (F) holds by (B5). Take \(L\) so large that \(\Lambda_1\cup\Lambda_2\subset\Lambda_L\) and
\(-L\le a<L\). Split \(\Lambda_L=\Lambda^-\sqcup\Lambda^+\) with \(\Lambda^-=[-L,a]\), \(\Lambda^+=[a+1,L]\). Then
\(H_{\Lambda_L}=H_{\Lambda^-}+H_{\Lambda^+}+W\), where \(W\) is the sum of the \(\Phi_j\) with \([j,j+r]\subset
\Lambda_L\) and \(j\le a<j+r\); there are at most \(r\) of them, so \(\|W\|\le r\|\Phi\|\). The restriction of
\(\varphi_L\) to \(A(\Lambda_L)\) is the Gibbs state of \(H_{\Lambda_L}\), so Lemma 6.1 and (2.1) give
\(\mathrm I_{\varphi_L}(\Lambda_1:\Lambda_2)\le\mathrm I_{\varphi_L}(\Lambda^-:\Lambda^+)\le2\beta r\|\Phi\|\). As
\(L\to\infty\), \(\varphi_L|_{A(\Lambda_1\cup\Lambda_2)}\to\varphi_\beta|_{A(\Lambda_1\cup\Lambda_2)}\) in the
finite-dimensional state space, and entropy is continuous (B1)(e); so the bound passes to \(\varphi_\beta\). For (MI)
take \(g=0\) and \(\ell_0\ge2\beta r\|\Phi\|/c\). \(\square\)

**Corollary 6.3.** If \(\varphi_\beta\) satisfies (ML), then \(h_{\varphi_\beta}(\theta)=s(\varphi_\beta)\).

**Proof.** Theorems 2.2 and 6.2. \(\square\)

*Reference:* [Connes–Narnhofer–Thirring 1987] states this for Gibbs states of finite-range interactions, with
(ML) in the following form: for every \(n\) and every \(\varepsilon>0\) there is \(N\) for which (2.3) holds, and
\(N/n\to0\) as \(n\to\infty\).

### 6.2 Uniform clustering is not enough

The Gibbs state also has uniformly decaying correlations between half-lines.

**Theorem 6.4 (uniform clustering).** For every \(\beta>0\) and \(\eta>0\) there is \(p\in\mathbb N\) such that
\(|\varphi_\beta(Q_1Q_2)-\varphi_\beta(Q_1)\varphi_\beta(Q_2)|\le\eta\|Q_1\|\|Q_2\|\) for all
\(Q_1\in A((-\infty,-p])\) and \(Q_2\in A([p,\infty))\).

This is (B8), proved in Theorem 0.13 by the perturbation theory of one-dimensional KMS states; the entropy theorem
does not use it. It is natural to try to control the block process of Section 5.2 by
Theorem 6.4 instead of (MI). The following example shows why this does not work directly: a covariance bound for
bounded observables does not bound the mutual information of blocks with many states.

**Example 6.5 (a hidden parity).** Let \(r\ge1\), \(G=\mathbb F_2^r\), \(d=2^r\). Let \(X\) and \(S\) be independent
and uniform on \(G\), let \(B=X\cdot S\) (the parity \(\sum_ix_is_i\) mod \(2\)), and \(Y=(S,B)\). Then:

- (a) \(\mathrm I(X;Y)=(1-d^{-1})\log2\);
- (b) \(|\mathbb E f(X)g(Y)-\mathbb Ef(X)\,\mathbb Eg(Y)|\le d^{-1/2}\) for all functions with \(|f|,|g|\le1\).

*Proof.* (a) \(H(Y\mid X)=H(S)=\log d\), since \(B\) is a function of \((X,S)\). Given \(S=s\neq0\), \(B\) is a
uniform bit; given \(S=0\), \(B=0\). So \(H(Y)=\log d+(1-d^{-1})\log2\), and \(\mathrm I(X;Y)=H(Y)-H(Y\mid X)\).
(b) Write \(g(s,b)=g_0(s)+g_1(s)(-1)^b\) with \(|g_1|\le1\), and \(\hat f(s)=\mathbb E f(X)(-1)^{X\cdot s}\). Then
\(\mathbb Ef(X)g(Y)=\mathbb Ef\,\mathbb Eg_0(S)+\mathbb E\,g_1(S)\hat f(S)\) and \(\mathbb Eg(Y)=\mathbb Eg_0(S)+
g_1(0)/d\). As \(\hat f(0)=\mathbb Ef\), the covariance is \(d^{-1}\sum_{s\neq0}g_1(s)\hat f(s)\), and by the
Cauchy–Schwarz inequality and Parseval's identity \(\sum_s|\hat f(s)|^2=\mathbb E|f|^2\le1\),
\(d^{-1}\sum_s|\hat f(s)|\le d^{-1}d^{1/2}=d^{-1/2}\). \(\square\)

So the covariances are uniformly of size \(d^{-1/2}\), exponentially small in the number \(r\) of bits of \(X\), while
the future variable \(Y\) carries a full bit about \(X\); with \(k\) independent masks the future carries about
\(k\) bits while the covariances stay below \(2^kd^{-1/2}\) (Exercise 9.4). In particular, conditioning on a value
of the future can move the law of \(X\) far from its marginal (here, to the uniform law on a half-space) even though
all covariances are tiny. What a covariance bound \(\eta\) does give is obtained by summing over the atoms: for the
block variable \(X_0\) with \(q^L\) values and any future variable \(Y\),
\(\sum_{a,y}|\mathbb P(X_0=a,Y=y)-\mathbb P(X_0=a)\mathbb P(Y=y)|\le q^L\eta\). Using this in Section 5.2 forces
\(\eta\lesssim q^{-L}\), hence a gap \(p\) that grows with the block length \(L\), and the argument of Theorem 5.3
then no longer gives the full mean entropy (Remark 5.4).

*Reference:* [Connes–Narnhofer–Thirring 1987] bounds the entropy of the block process using uniform clustering alone,
asserting that the law of a block given the far future is \(\eta\)-close to its marginal for every value of the
future; Example 6.5 shows that this does not follow from uniform clustering, so we use the mutual-information
condition, which Theorem 6.2 provides at every temperature.

## 7. Commuting interactions

In this section \(\Phi\) is as in Section 6 and, in addition, \([\Phi_i,\Phi_j]=0\) for all \(i,j\). Examples: every
classical interaction (\(\Phi\) diagonal in a fixed product basis, such as the Ising coupling
\(\sigma^z\otimes\sigma^z\), \(r=1\)); the cluster interaction \(\Phi=\sigma^z\otimes\sigma^x\otimes\sigma^z\)
(\(r=2\); the terms \(\Phi_j,\Phi_{j+1}\) anticommute at two sites and therefore commute); and, with \(r=0\), every
\(\Phi\in A(\{0\})\), whose KMS state is a product state.

**Lemma 7.1 (local form of the dynamics).** Let \(\Lambda_0\) be a finite interval and \(\mathcal J\) a finite set of
indices containing \(\mathcal J_0=\{j:[j,j+r]\cap\Lambda_0\neq\emptyset\}\); put \(H_{\mathcal J}=\sum_{j\in
\mathcal J}\Phi_j\). Then \(\tau_t(x)=e^{itH_{\mathcal J}}xe^{-itH_{\mathcal J}}\) for \(x\in A(\Lambda_0)\). Hence
every \(x\in A(\Lambda_0)\) is entire for \(\sigma^{\varphi_\beta}\), and
\[
\sigma^{\varphi_\beta}_{i/2}(x)=e^{\beta H_{\mathcal J}/2}\,x\,e^{-\beta H_{\mathcal J}/2}
\]
in the sense of Definition 4.1.

**Proof.** The terms \(\Phi_j\) with \(j\notin\mathcal J_0\) commute with \(x\) and with all other terms. So for
every finite \(\mathcal J'\supset\mathcal J_0\), \(e^{itH_{\mathcal J'}}xe^{-itH_{\mathcal J'}}=e^{itH_{\mathcal J_0}}
xe^{-itH_{\mathcal J_0}}\). Taking \(\mathcal J'=\{j:[j,j+r]\subset\Lambda_L\}\) for large \(L\) and passing to the
limit in (B6) gives the formula for \(\tau_t\), with \(\mathcal J_0\) and then with any \(\mathcal J\supset
\mathcal J_0\). By (B5), \(\sigma^{\varphi_\beta}_t(x)=\tau_{-\beta t}(x)=e^{-i\beta tH_{\mathcal J}}xe^{i\beta t
H_{\mathcal J}}\), which is entire in \(t\), with value \(e^{\beta H_{\mathcal J}/2}xe^{-\beta H_{\mathcal J}/2}\) at
\(t=i/2\). Apply (B4). \(\square\)

**Proposition 7.2 (block densities).** Let \(\widehat J=[a,b]\) be a finite interval,
\(C=[a+2r,b-2r]\) its core and \(E=\widehat J\setminus C\) its two edges (strips of width at most \(2r\)). Let
\(\mathcal D=\{j:[j,j+r]\subset[a+r,b-r]\}\) and \(H_{\mathrm{deep}}=\sum_{j\in\mathcal D}\Phi_j\). The density
\(\rho\) of \(\varphi_\beta|_{A(\widehat J)}\) is
\[
\rho=e^{-\beta H_{\mathrm{deep}}}\,K,
\]
where \(K\in A(E)\) is positive, invertible, and commutes with every \(\Phi_j\) such that \([j,j+r]\subset\widehat J\).
Consequently \(e^{\beta H_{\widehat J}/2}\rho\,e^{\beta H_{\widehat J}/2}=e^{\beta(H_{\widehat J}-H_{\mathrm{deep}})}K\)
lies in \(A(E)\): the block density is the Gibbs factor of the block times an operator carried by its two edges.

**Proof.** If \([j,j+r]\not\subset[a+r,b-r]\), then either \(j\le a+r-1\), so \([j,j+r]\subset(-\infty,a+2r-1]\),
or \(j+r\ge b-r+1\), so \([j,j+r]\subset[b-2r+1,\infty)\); in both cases \([j,j+r]\) misses \(C\). Take \(L\) large
and split \(H_{\Lambda_L}=H_{\mathrm{deep}}+H_{\mathrm{rest}}\), where \(H_{\mathrm{rest}}\in
A(\Lambda_L\setminus C)\) collects the other terms. All terms commute, so
\(e^{-\beta H_{\Lambda_L}}=e^{-\beta H_{\mathrm{deep}}}e^{-\beta H_{\mathrm{rest}}}\). Let
\(\operatorname{Tr}_{\Lambda_L\setminus\widehat J}\) be the partial trace \(A(\Lambda_L)\to A(\widehat J)\); it is an
\(A(\widehat J)\)-bimodule map and maps \(A(\Lambda_L\setminus C)=A(E)\otimes A(\Lambda_L\setminus\widehat J)\)
into \(A(E)\). Since \(H_{\mathrm{deep}}\in A(\widehat J)\), the density of \(\varphi_L|_{A(\widehat J)}\) is
\[
\rho_L=e^{-\beta H_{\mathrm{deep}}}K_L,\qquad
K_L=\operatorname{Tr}_{\Lambda_L\setminus\widehat J}\bigl(e^{-\beta H_{\mathrm{rest}}}\bigr)\big/
\operatorname{Tr}e^{-\beta H_{\Lambda_L}}\in A(E)_+ .
\]
If \([j,j+r]\subset\widehat J\), then \(\Phi_j\in A(\widehat J)\) commutes with \(e^{-\beta H_{\mathrm{rest}}}\), hence
with \(K_L\) by the bimodule property. As \(L\to\infty\), \(\rho_L\to\rho\), so
\(K_L=e^{\beta H_{\mathrm{deep}}}\rho_L\to e^{\beta H_{\mathrm{deep}}}\rho=:K\), which is positive, lies in \(A(E)\),
commutes with those \(\Phi_j\), and is invertible because \(\rho\) is (F). Finally
\(H_{\widehat J}-H_{\mathrm{deep}}\) is a sum of terms \(\Phi_j\) with \([j,j+r]\subset\widehat J\) missing \(C\), so
it lies in \(A(E)\), and all the operators involved commute. \(\square\)

**Theorem 7.3 (exact modular locality).** Let \(n\ge1\), \(N\ge2r\), and \(J,\widehat J,\psi\) as in (2.2), with
\(\varphi=\varphi_\beta\). For every \(Q\in A(J)\), \(\sigma^\psi_{-i/2}(Q)\) is in the domain of
\(\sigma^\varphi_{i/2}\) and
\[
\sigma^\varphi_{i/2}\bigl(\sigma^\psi_{-i/2}(Q)\bigr)=Q .
\]

**Proof.** With \(a=-N\), \(b=n-1+N\), the core \(C=[2r-N,n-1+N-2r]\) contains \(J\). By Proposition 7.2,
\(\rho^{1/2}=e^{-\beta H_{\mathrm{deep}}/2}K^{1/2}\) (commuting positive factors), and \(K^{\pm1/2}\in A(E)\)
commutes with \(Q\in A(C)\). So
\[
\sigma^\psi_{-i/2}(Q)=\rho^{1/2}Q\rho^{-1/2}=e^{-\beta H_{\mathrm{deep}}/2}\,Q\,e^{\beta H_{\mathrm{deep}}/2}.
\]
Let \(\mathcal J_0=\{j:[j,j+r]\cap J\neq\emptyset\}\). For \(j\in\mathcal J_0\), \([j,j+r]\subset[-r,n-1+r]\subset
[a+r,b-r]\), so \(\mathcal J_0\subset\mathcal D\). The deep terms outside \(\mathcal J_0\) commute with \(Q\) and with
\(H_{\mathcal J_0}\), so \(w:=\sigma^\psi_{-i/2}(Q)=e^{-\beta H_{\mathcal J_0}/2}Qe^{\beta H_{\mathcal J_0}/2}\in
A([-r,n-1+r])\). Apply Lemma 7.1 to \(w\) with \(\Lambda_0=[-r,n-1+r]\) and \(\mathcal J=\{j:[j,j+r]\cap\Lambda_0\neq
\emptyset\}\supset\mathcal J_0\). The terms \(\Phi_j\), \(j\in\mathcal J\setminus\mathcal J_0\), commute with \(Q\)
and with \(H_{\mathcal J_0}\), hence with \(w\); therefore
\(\sigma^\varphi_{i/2}(w)=e^{\beta H_{\mathcal J}/2}we^{-\beta H_{\mathcal J}/2}=e^{\beta H_{\mathcal J_0}/2}
we^{-\beta H_{\mathcal J_0}/2}=Q\). \(\square\)

**Corollary 7.4.** For a commuting finite-range interaction and every \(\beta>0\),
\(h_{\varphi_\beta}(\theta)=s(\varphi_\beta)\).

**Proof.** (ML) holds with \(N=2r\) for every \(n\) and every \(\varepsilon\) (Theorem 7.3), and \(2r/n\to0\).
Apply Corollary 6.3. \(\square\)

**Remark 7.5 (non-commuting interactions).** For a general finite-range interaction the block density no longer
splits as in Proposition 7.2. The expected picture is that at high temperature
\(\log\rho+\beta H_{\widehat J}\) is concentrated near the two edges up to small errors, which would give (ML) with
\(N\) independent of \(n\) for \(\beta\) below some threshold. Establishing this requires a convergent
high-temperature expansion of \(\log\rho\), which is not carried out in this lesson. What is easy is the domain
statement: in one dimension every local element is entire for \(\tau\) (Theorem 0.6(b)), so \(\sigma^\psi_{-i/2}(Q)\)
is always in the domain of \(\sigma^\varphi_{i/2}\); the difficulty is the size of (2.3). Section 8 carries out the
analogous estimate completely for quasi-free fermions, at every temperature.

## 8. Quasi-free fermions

### 8.1 Second quantization of trace-class operators

Let \(K\) be a Hilbert space and \(\mathrm{CAR}(K)\) as in (B9). For a trace-class operator \(X\) on \(K\) with
Schmidt decomposition \(X=\sum_is_i\langle\,\cdot\,,v_i\rangle u_i\) (\(s_i\ge0\), \(\sum_is_i=\|X\|_1\),
orthonormal families \((u_i),(v_i)\)) put
\[
d\Gamma(X)=\sum_is_i\,a^*(u_i)a(v_i)\in\mathrm{CAR}(K);
\]
the series converges in norm and \(\|d\Gamma(X)\|\le\|X\|_1\), since \(\|a^*(u)a(v)\|\le\|u\|\|v\|\). Since
\((u,v)\mapsto a^*(u)a(v)\) is linear in \(u\), antilinear in \(v\) and bounded, \(d\Gamma\) is the continuous linear
extension of \(\langle\,\cdot\,,v\rangle u\mapsto a^*(u)a(v)\) to the trace class; in particular it is linear, and
\(d\Gamma(X)^*=d\Gamma(X^*)\).

**Lemma 8.1.** For trace-class \(X\) and \(f\in K\),
\[
e^{d\Gamma(X)}a^*(f)e^{-d\Gamma(X)}=a^*(e^Xf),\qquad e^{d\Gamma(X)}a(f)e^{-d\Gamma(X)}=a\bigl(e^{-X^*}f\bigr),
\]
and for every \(Q\in\mathrm{CAR}(K)\),
\(\|e^{d\Gamma(X)}Qe^{-d\Gamma(X)}-Q\|\le(e^{2\|X\|_1}-1)\|Q\|\).

**Proof.** From \(\{a(v),a^*(f)\}=\langle f,v\rangle\) we get \([a^*(u)a(v),a^*(f)]=\langle f,v\rangle a^*(u)\), so
\([d\Gamma(X),a^*(f)]=a^*(Xf)\). Taking adjoints in the same identity for \(X^*\),
\([d\Gamma(X),a(f)]=-a(X^*f)=a(-X^*f)\). Iterating, \((\operatorname{ad}d\Gamma(X))^k\) maps \(a^*(f)\) to
\(a^*(X^kf)\) and \(a(f)\) to \(a((-X^*)^kf)\); summing \(e^{\operatorname{ad}D}=\operatorname{Ad}e^D\) (the
coefficients \(1/k!\) are real, so the antilinearity of \(a\) does no harm) gives the formulas. With
\(V=e^{d\Gamma(X)}\) and \(y=\|X\|_1\): \(\|V-1\|\le e^y-1\), \(\|V^{-1}\|\le e^y\), \(\|V^{-1}-1\|\le e^y-1\), and
\(VQV^{-1}-Q=(V-1)QV^{-1}+Q(V^{-1}-1)\). \(\square\)

### 8.2 Locality of the functional calculus under compression

Let \(\mathbb T=\mathbb R/2\pi\mathbb Z\). For \(r\in C^2(\mathbb T)\) let
\(\hat r(u)=\frac1{2\pi}\int_0^{2\pi}r(p)e^{-iup}\,dp\) and let \(L_r\) be the Laurent operator on
\(\ell^2(\mathbb Z)\), \((L_rf)(x)=\sum_y\hat r(x-y)f(y)\). The Fourier transform \(f\mapsto\sum_xf(x)e^{ixp}\)
carries \(L_r\) to multiplication by \(r\), so \(L_r\) is bounded, \(L_{\bar r}=L_r^*\), and for \(T=L_t\) with \(t\)
real and \(F\) holomorphic near the range of \(t\), \(F(T)=L_{F\circ t}\). For \(\Lambda\subset\mathbb Z\) let
\(P_\Lambda\) be the projection onto \(\ell^2(\Lambda)\), and \(\Lambda^c=\mathbb Z\setminus\Lambda\).

**Lemma 8.2 (off-diagonal trace norms).** Let \(r\in C^2(\mathbb T)\) and \(\kappa=\sup|r''|\). Then
\(|\hat r(u)|\le\kappa u^{-2}\) for \(u\neq0\). If \(J=[a,b]\) and \(\widehat J\supset[a-N,b+N]\) are finite intervals
with \(N\ge1\), then
\[
\|P_{\widehat J^c}L_rP_J\|_1\le2\sqrt3\,\kappa\,N^{-1/2}.
\]

**Proof.** Integrating by parts twice, \(\hat r(u)=-\frac1{2\pi u^2}\int_0^{2\pi}r''(p)e^{-iup}dp\). An operator
\(Y=YP_J\) is the sum of the rank-one operators \((Y\delta_y)\langle\,\cdot\,,\delta_y\rangle\), \(y\in J\), so
\(\|Y\|_1\le\sum_{y\in J}\|Y\delta_y\|\). For \(y\in J\) and \(x\notin\widehat J\), either \(y-x\ge y-a+N+1\) or
\(x-y\ge b-y+N+1\). Using \(\sum_{u\ge v+1}u^{-4}\le\int_v^\infty u^{-4}du=v^{-3}/3\) for \(v\ge1\),
\[
\|P_{\widehat J^c}L_r\delta_y\|\le\frac\kappa{\sqrt3}\Bigl((y-a+N)^{-3/2}+(b-y+N)^{-3/2}\Bigr).
\]
Summing over \(y\in J\), each of the two sums is at most \(\sum_{v\ge N}v^{-3/2}\le N^{-3/2}+2N^{-1/2}\le3N^{-1/2}\).
\(\square\)

**Lemma 8.3 (compressions).** Let \(t\in C^2(\mathbb T)\) be real with \(\delta\le t\le1-\delta\), where
\(0<\delta\le1/4\), and \(T=L_t\). Let \(\Omega=\mathbb C\setminus((-\infty,0]\cup[1,\infty))\) and \(F\) holomorphic
on \(\Omega\). For finite intervals \(J=[a,b]\) and \(\widehat J\supset[a-N,b+N]\), \(N\ge1\), let
\(T_{\widehat J}=P_{\widehat J}TP_{\widehat J}|_{\ell^2(\widehat J)}\) and extend \(F(T_{\widehat J})\) by \(0\) on
\(\ell^2(\widehat J^c)\). Then
\[
\bigl\|\bigl(F(T_{\widehat J})-F(T)\bigr)P_J\bigr\|_1\le C_FN^{-1/2},\qquad
C_F=2\sqrt3\Bigl(1+\frac2\delta\Bigr)\Bigl(\frac{4\sup|t''|}{\delta^2}+\frac{16\sup|t'|^2}{\delta^3}\Bigr)
\max_{\Gamma}|F|,
\]
where \(\Gamma\) is the circle \(|z-\frac12|=\frac12-\frac\delta2\). The constant does not depend on \(J\) or
\(\widehat J\).

**Proof.** The spectra of \(T\) and of \(T_{\widehat J}\) (a compression) lie in \([\delta,1-\delta]\). The circle
\(\Gamma\) lies in \(\Omega\), surrounds \([\delta,1-\delta]\), and has distance at least \(\delta/2\) from it; its
length is less than \(2\pi\cdot\frac12\). By the holomorphic functional calculus,
\(F(T_{\widehat J})-F(T)=\frac1{2\pi i}\oint_\Gamma F(z)\bigl(R^{\widehat J}_z-R_z\bigr)dz\), with
\(R_z=(z-T)^{-1}\) and \(R^{\widehat J}_z=(z-T_{\widehat J})^{-1}\) extended by \(0\). Write \(P=P_{\widehat J}\),
\(P^c=1-P\). From \(P=P(z-T)R_z\) and \(P(z-T)=(z-T_{\widehat J})P-PTP^c\) we get, applying \(R^{\widehat J}_z\),
\[
R^{\widehat J}_zP-PR_z=-R^{\widehat J}_zPTP^cR_z,\qquad\text{hence}\qquad
\bigl(R^{\widehat J}_z-R_z\bigr)P_J=-R^{\widehat J}_zPTP^cR_zP_J-P^cR_zP_J .
\]
So \(\|(R^{\widehat J}_z-R_z)P_J\|_1\le(1+2/\delta)\|P^cR_zP_J\|_1\), since \(\|R^{\widehat J}_z\|\le2/\delta\) and
\(\|T\|\le1\). Now \(R_z=L_{r_z}\) with \(r_z=(z-t)^{-1}\), and
\(r_z''=t''(z-t)^{-2}+2t'^2(z-t)^{-3}\) is bounded by \(4\sup|t''|/\delta^2+16\sup|t'|^2/\delta^3\), because
\(|z-t(p)|\ge\delta/2\). Lemma 8.2 bounds \(\|P^cR_zP_J\|_1\), and integrating over \(\Gamma\) gives the claim.
\(\square\)

**Lemma 8.4 (one implementer for two conditions).** Let \(K\) be a Hilbert space, \(K_1\subset K\) a
finite-dimensional subspace with inclusion \(\iota\) and projection \(P_1\), and \(R,S:K_1\to K\) linear maps with
\(\langle Rf,Sg\rangle=\langle f,g\rangle\) for \(f,g\in K_1\). Suppose \(e=\|S-\iota\|_1\le1/10\) and
\(x=\|R-\iota\|_1+6e\le1/2\). Then there is a trace-class operator \(X\) on \(K\) with \(\|X\|_1\le2x\),
\(e^Xf=Rf\) and \(e^{-X^*}f=Sf\) for all \(f\in K_1\).

**Proof.** Write \(S=\iota+E\), \(\|E\|_1=e\). Then \(S^*S=1+F\) on \(K_1\) with \(F=\iota^*E+E^*\iota+E^*E\),
\(\|F\|\le\|F\|_1\le2e+e^2\le0.21\), so \(S\) is injective and the projection onto \(S(K_1)\) is
\(P_S=S(1+F)^{-1}S^*\). With \((1+F)^{-1}=1+G\), \(\|G\|_1\le\|F\|_1/(1-\|F\|)\),
\[
P_S-P_1=\iota E^*+E\iota^*+EE^*+SGS^*,\qquad
\|P_S-P_1\|_1\le(2e+e^2)\Bigl(1+\frac{(1+e)^2}{1-2e-e^2}\Bigr)\le6e .
\]
Define \(Z=RP_1+(1-P_S)(1-P_1)\) (here \(RP_1\) means \(R\) composed with the projection \(K\to K_1\)). Then
\(Z-1=(R-\iota)P_1+(P_1-P_S)(1-P_1)\), so \(\|Z-1\|\le\|Z-1\|_1\le x\le1/2\). Hence \(Z\) is invertible,
\(X=\log Z=\sum_{k\ge1}(-1)^{k+1}(Z-1)^k/k\) is trace class with \(\|X\|_1\le x/(1-x)\le2x\), and \(e^X=Z\). For
\(f\in K_1\), \(Zf=Rf\). For \(f\in K_1\) and \(h\in K\),
\(\langle h,Z^*Sf\rangle=\langle RP_1h,Sf\rangle+\langle(1-P_S)(1-P_1)h,Sf\rangle=\langle P_1h,f\rangle+0=\langle
h,f\rangle\); so \(Z^*Sf=f\), i.e. \(Sf=(Z^*)^{-1}f=e^{-X^*}f\). \(\square\)

### 8.3 Modular locality for quasi-free states

Let \(K=\ell^2(\mathbb Z)\), and for \(\Lambda\subset\mathbb Z\) write \(\mathrm{CAR}(\Lambda)=
\mathrm{CAR}(\ell^2(\Lambda))\). Let \(t\in C^2(\mathbb T)\) be real with \(\delta\le t\le1-\delta\), \(0<\delta\le
1/4\), \(T=L_t\), and \(\omega=\omega_T\) the gauge-invariant quasi-free state (B9)(b). This covers the equilibrium
state at inverse temperature \(\beta\) of free lattice fermions whose one-particle Hamiltonian is the Laurent
operator of a real \(C^2\) symbol \(\epsilon\): there \(t=(1+e^{\beta\epsilon})^{-1}\), for every \(\beta\).

Put \(h=\log(T^{-1}-1)\) (bounded, self-adjoint). By (B9)(d) and (B5), \(\omega\) is faithful on its von Neumann
algebra and \(\sigma^\omega_t=\alpha_{-t}\), i.e. \(\sigma^\omega_t(a^*(g))=a^*(e^{-ith}g)\). For a finite interval
\(\widehat J\) let \(\psi=\omega|_{\mathrm{CAR}(\widehat J)}=\omega_{T_{\widehat J}}\) and
\(h_{\widehat J}=\log(T_{\widehat J}^{-1}-1)\) on \(\ell^2(\widehat J)\). By (B9)(c) the density of \(\psi\) is
proportional to \(e^{-d\Gamma(h_{\widehat J})}\). Let \(G(s)=(s/(1-s))^{1/2}\) and \(F=1/G\), both holomorphic on
\(\Omega\); then \(e^{h/2}=F(T)\), \(e^{-h/2}=G(T)\), and likewise for \(T_{\widehat J}\).

**Theorem 8.5 (modular locality for quasi-free states).** There is a constant \(C\) depending only on \(t\) such that
the following holds. Let \(n\ge1\), \(N\ge1\), \(J=[0,n-1]\), \(\widehat J=[-N,n-1+N]\), and suppose
\(CN^{-1/2}\le1/14\). Then for every \(Q\in\mathrm{CAR}(J)\) the element \(\sigma^\psi_{-i/2}(Q)\) is in the domain of
\(\sigma^\omega_{i/2}\) and
\[
\bigl\|\sigma^\omega_{i/2}\bigl(\sigma^\psi_{-i/2}(Q)\bigr)-Q\bigr\|\le\bigl(e^{28CN^{-1/2}}-1\bigr)\|Q\|.
\]
In particular, for every \(\varepsilon>0\) there is \(N_0\), independent of \(n\), such that (2.3) holds on
\(\mathrm{CAR}(J)\) for all \(n\) and all \(N\ge N_0\).

**Proof.** *Step 1: the two analytic continuations on generators.* By Lemma 8.1 with \(X=-h_{\widehat J}/2\), the map
\(\sigma^\psi_{-i/2}=\operatorname{Ad}\rho^{1/2}=\operatorname{Ad}e^{-d\Gamma(h_{\widehat J})/2}\) is multiplicative
and, for \(f\in\ell^2(J)\),
\[
\sigma^\psi_{-i/2}(a^*(f))=a^*\bigl(G(T_{\widehat J})f\bigr),\qquad\sigma^\psi_{-i/2}(a(f))=a\bigl(F(T_{\widehat J})f\bigr).
\]
For \(g\in K\), \(t\mapsto\sigma^\omega_t(a^*(g))=a^*(e^{-ith}g)\) extends to the entire function
\(z\mapsto a^*(e^{-izh}g)\), and \(t\mapsto\sigma^\omega_t(a(g))=a(e^{-ith}g)=\sum_k(it)^ka(h^kg)/k!\) extends to the
entire function \(z\mapsto\sum_k(iz)^ka(h^kg)/k!\). At \(z=i/2\) these are \(a^*(e^{h/2}g)=a^*(F(T)g)\) and
\(a(e^{-h/2}g)=a(G(T)g)\). By (B4), every noncommutative polynomial \(w\) in the \(a^\#(g)\) is in the domain of
\(\sigma^\omega_{i/2}\), and \(\sigma^\omega_{i/2}\) is multiplicative on such polynomials. By (B9)(a) every
\(Q\in\mathrm{CAR}(J)\) is a polynomial in the \(a^\#(f)\), \(f\in\ell^2(J)\), and so is \(\sigma^\psi_{-i/2}(Q)\), in
the \(a^\#(g)\), \(g\in\ell^2(\widehat J)\). Hence \(\Gamma(Q)=\sigma^\omega_{i/2}(\sigma^\psi_{-i/2}(Q))\) is
defined, linear and multiplicative in \(Q\), and determined by
\[
\Gamma(a^*(f))=a^*(Rf),\quad\Gamma(a(f))=a(Sf),\qquad R=F(T)G(T_{\widehat J})|_{\ell^2(J)},\quad
S=G(T)F(T_{\widehat J})|_{\ell^2(J)} .
\]
*Step 2: the one-particle estimate.* For \(f,g\in\ell^2(J)\),
\(\langle Rf,Sg\rangle=\langle G(T)F(T)G(T_{\widehat J})f,F(T_{\widehat J})g\rangle=\langle f,g\rangle\). Since
\(F(T)G(T)=1\), \(R-\iota=F(T)\bigl(G(T_{\widehat J})-G(T)\bigr)P_J\) and \(S-\iota=G(T)\bigl(F(T_{\widehat J})-F(T)
\bigr)P_J\). With \(\|F(T)\|,\|G(T)\|\le((1-\delta)/\delta)^{1/2}\) and Lemma 8.3,
\[
\|R-\iota\|_1\le CN^{-1/2},\qquad\|S-\iota\|_1\le CN^{-1/2},\qquad C=\Bigl(\frac{1-\delta}{\delta}\Bigr)^{1/2}
\max(C_F,C_G).
\]
*Step 3.* Since \(CN^{-1/2}\le1/14\), Lemma 8.4 applies with \(e\le CN^{-1/2}\le1/10\) and
\(x\le7CN^{-1/2}\le1/2\). It gives \(X\) with \(\|X\|_1\le2x\le
14CN^{-1/2}\), \(e^Xf=Rf\) and \(e^{-X^*}f=Sf\) on \(\ell^2(J)\). By Lemma 8.1, \(Q\mapsto e^{d\Gamma(X)}Qe^{-d\Gamma(X)}\)
agrees with \(\Gamma\) on the generators; both maps are linear and multiplicative, so they agree on
\(\mathrm{CAR}(J)\), and \(\|\Gamma(Q)-Q\|\le(e^{2\|X\|_1}-1)\|Q\|\le(e^{28CN^{-1/2}}-1)\|Q\|\). \(\square\)

**Remark 8.6.** The one-particle statement behind Theorem 8.5, that \(e^{h/2}e^{-h_{\widehat J}/2}-1\) restricted to
\(\ell^2(J)\) is small in trace norm when \(J\) is far from the complement of \(\widehat J\), is the fermionic form of
Proposition 7.2: the modular Hamiltonian of a block differs from that of the whole chain only near the edges of the
block, now up to a trace-norm error of order \(N^{-1/2}\), uniformly in the length of the block and at every
temperature. On the CAR algebra the local algebras of disjoint intervals anticommute in their odd parts instead of
commuting, so Section 5 does not apply verbatim to the translation of \(\mathrm{CAR}(\ell^2(\mathbb Z))\); the
entropy of quasi-free shifts has been computed by other means [Størmer–Voiculescu 1990].

## 9. Exercises

**Exercise 9.1 (invariant blocks).** (a) Let \(\varphi\) satisfy (F), \(N\subset M\) a finite-dimensional full
matrix subalgebra with \(\sigma^\varphi_t(N)=N\) for all \(t\), and \(\psi=\varphi|_N\). Show that for every
\(y\in N\), \(\sigma^\psi_{-i/2}(y)\) is in the domain of \(\sigma^\varphi_{i/2}\) and
\(\sigma^\varphi_{i/2}(\sigma^\psi_{-i/2}(y))=y\). (b) Deduce that for a product state \(\omega^{\otimes\mathbb Z}\)
with \(\omega\) faithful, (ML) holds with \(\varepsilon=0\) and \(N=0\).

*Solution.* (a) The restriction of \(\sigma^\varphi\) to \(N\) is a one-parameter group of automorphisms of \(N\) for
which \(\psi\) satisfies the modular KMS condition (the KMS functions for \(\varphi\) restrict to \(N\)). The KMS
condition determines the modular group, so \(\sigma^\varphi_t|_N=\sigma^\psi_t=\operatorname{Ad}\rho^{it}\). For
\(w=\rho^{1/2}y\rho^{-1/2}\in N\), \(t\mapsto\sigma^\varphi_t(w)=\rho^{it}w\rho^{-it}\) is entire with value
\(\rho^{-1/2}w\rho^{1/2}=y\) at \(i/2\); apply (B4). (b) Let \(\rho_\omega\) be the density of \(\omega\) and
\(\Phi=-\log\rho_\omega\in A(\{0\})\). Then \(\omega^{\otimes\mathbb Z}\) is the \((\tau,1)\)-KMS state of this
interaction with \(r=0\), whose dynamics is \(\tau_t=\bigotimes_x\operatorname{Ad}\rho_\omega^{-it}\) on local
elements; by (B5), \(\sigma^\varphi_t\) is the product of the \(\operatorname{Ad}\rho_\omega^{it}\), which leaves every
\(A(J)\) invariant. Apply (a) with \(N=A(J)\) and \(\widehat J=J\). (This is also Theorem 7.3 with \(r=0\).)

**Exercise 9.2 (the tracial state).** Let \(\mathrm{tr}\) be the tracial state of the chain. Show directly from
Propositions 5.1 and 5.2 that \(h_{\mathrm{tr}}(\theta)\ge\log q\), and conclude \(h_{\mathrm{tr}}(\theta)=\log q\).

*Solution.* The modular operator of a trace is \(1\), so \(\sigma^{\mathrm{tr}}_{i/2}(w)=w\) for all \(w\), and
\(\rho=q^{-n}1\), so \(\sigma^\psi_{-i/2}(y)=y\). Proposition 5.1 applies with \(N=0\) and any \(\varepsilon\in
(0,1]\); letting \(\varepsilon\to0\) (the left side of (5.2) does not depend on \(\varepsilon\)) gives
\(H_{\mathrm{tr}}(M_0,\dots,M_{k-1})\ge S(\mathrm{tr}|_{C_{[0,k-1]}})\). With \(g=0\) the mutual informations vanish
(the trace is a product state), so Proposition 5.2 gives \(S(\mathrm{tr}|_{C_{[0,k-1]}})\ge kn\log q\). By (5.3) with
\(m=n\), \(h_{\mathrm{tr}}(\theta)\ge\log q\). Theorem 3.1 and \(s(\mathrm{tr})=\log q\) give equality.

**Exercise 9.3 (two Ising spins).** Let \(D_1=D_2=M_2(\mathbb C)\), \(H=J_0\,\sigma^z\otimes\sigma^z\) with
\(J_0\in\mathbb R\), and \(\omega\) the Gibbs state at inverse temperature \(\beta\). Compute
\(\mathrm I_\omega(D_1:D_2)\) and verify the bound \(2\beta|J_0|\) of Lemma 6.1 directly.

*Solution.* \(\omega\) is diagonal in the product basis, with probability
\(p=(1+e^{2\beta J_0})^{-1}\) split equally between the two aligned configurations and \(1-p\) between the two
anti-aligned ones. Both marginals are uniform, so \(\mathrm I=2\log2-(\log2+\mathrm h(p))=\log2-\mathrm h(p)\). This is
the relative entropy of \((p,1-p)\) with respect to \((\frac12,\frac12)\), which is at most
\(\log\bigl(2\max(p,1-p)\bigr)=\log\bigl(2e^{2\beta|J_0|}/(1+e^{2\beta|J_0|})\bigr)\le2\beta|J_0|\). Here \(W=H\)
and \(\|W\|=|J_0|\). For small \(\beta\) the mutual information is of order \((\beta J_0)^2/2\), much smaller than the
bound.

**Exercise 9.4 (several hidden parities).** In Example 6.5 let \(S_1,\dots,S_k\) be independent uniform elements of
\(G\), independent of \(X\), and \(Y=(S_1,\dots,S_k,X\cdot S_1,\dots,X\cdot S_k)\). Show that
\(\mathrm I(X;Y)\ge k(1-2^{k-r})\log2\) and that all covariances of functions bounded by \(1\) are at most
\((2^k-1)d^{-1/2}\). Taking \(k=r/4\), conclude that \(\mathrm I(X;Y)/\log d\) stays bounded below while the
covariances tend to \(0\) as \(r\to\infty\).

*Solution.* Given \(S=(S_1,\dots,S_k)\), the vector \(B=(X\cdot S_i)_i\) is uniform on the image of the linear map
\(x\mapsto(x\cdot S_i)_i\), whose dimension is the rank of \(S_1,\dots,S_k\); and \(H(Y\mid X)=H(S)\). So
\(\mathrm I(X;Y)=H(B\mid S)=\mathbb E[\operatorname{rank}]\log2\). The rank is \(k\) unless some \(S_i\) lies in the
span of the previous ones, which has probability at most \(\sum_{i\le k}2^{i-1-r}\le2^{k-r}\); so
\(\mathbb E[\operatorname{rank}]\ge k(1-2^{k-r})\). For the covariance, expand \(g(s,b)=\sum_{U\subset\{1..k\}}
g_U(s)(-1)^{\sum_{i\in U}b_i}\) with \(|g_U|\le1\). With \(\sigma_U=\sum_{i\in U}S_i\),
\(\operatorname{Cov}(f(X),g(Y))=\sum_{U\neq\emptyset}\mathbb E\bigl[g_U(S)\hat f(\sigma_U)1_{\sigma_U\neq0}\bigr]\), and
for \(U\neq\emptyset\), \(\sigma_U\) is uniform on \(G\), so each term is at most
\(\mathbb E|\hat f(\sigma_U)|=d^{-1}\sum_s|\hat f(s)|\le d^{-1/2}\). With \(k=r/4\):
\(\mathrm I(X;Y)\ge\frac r4(1-2^{-3r/4})\log2\approx\frac14\log d\), while the covariances are at most
\(2^{r/4}2^{-r/2}=2^{-r/4}\).

## References



- [Connes–Narnhofer–Thirring 1987] A. Connes, H. Narnhofer and W. Thirring, Dynamical entropy of C* algebras and von
  Neumann algebras, Comm. Math. Phys. 112 (1987), no. 4, 691–719. Free at https://alainconnes.org/wp-content/uploads/entropy.pdf
- [Connes–Størmer 1975] A. Connes and E. Størmer, Entropy for automorphisms of II₁ von Neumann algebras, Acta Math.
  134 (1975), no. 3–4, 289–306. Free at https://doi.org/10.1007/BF02392105
- [Araki 1969] H. Araki, Gibbs states of a one dimensional quantum lattice, Comm. Math. Phys. 14 (1969), 120–157.
  https://doi.org/10.1007/BF01645134. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-14/issue-2/Gibbs-states-of-a-one-dimensional-quantum-lattice/cmp/1103841726.full
- [Audenaert 2007] K. M. R. Audenaert, A sharp continuity estimate for the von Neumann entropy, J. Phys. A 40 (2007),
  no. 28, 8127–8136. https://doi.org/10.1088/1751-8113/40/28/S18 Open preprint: https://arxiv.org/abs/quant-ph/0610146
- [Størmer–Voiculescu 1990] E. Størmer and D. Voiculescu, Entropy of Bogoliubov automorphisms of the canonical
  anticommutation relations, Comm. Math. Phys. 133 (1990), no. 3, 521–542. https://doi.org/10.1007/BF02097008. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-133/issue-3/Entropy-of-Bogoliubov-automorphisms-of-the-canonical-anticommutation-relations/cmp/1104201506.full
- [Wolf–Verstraete–Hastings–Cirac 2008] M. M. Wolf, F. Verstraete, M. B. Hastings and J. I. Cirac, Area laws in
  quantum systems: mutual information and correlations, Phys. Rev. Lett. 100 (2008), 070502.
  https://doi.org/10.1103/PhysRevLett.100.070502 Open preprint: https://arxiv.org/abs/0704.3906

- [Naaijkens] P. Naaijkens, *Quantum Spin Systems on Infinite Lattices*, lecture notes, extended and corrected 2016, arXiv:1311.2717; published as Lecture Notes in Physics 933, Springer, 2017. Free at https://arxiv.org/abs/1311.2717
- [Dereziński 2006] J. Dereziński, Introduction to representations of the canonical commutation and anticommutation relations, in *Large Coulomb Systems*, Lecture Notes in Physics 695, Springer, 2006; arXiv:math-ph/0511030. Free at https://arxiv.org/abs/math-ph/0511030
