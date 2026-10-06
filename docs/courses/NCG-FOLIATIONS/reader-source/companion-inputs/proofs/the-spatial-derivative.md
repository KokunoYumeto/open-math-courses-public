# The spatial derivative

*Public domain (CC0).*

## Introduction

Consider a von Neumann algebra \(M\) acting on a Hilbert space \(H\), with commutant \(N=M'\). A weight on
\(M\) and a weight on \(N\) live on different algebras, so at first sight there is nothing to compare. Yet the
Hilbert space \(H\) is shared, and this lesson shows that a normal semifinite weight \(\varphi\) on \(M\) and a
faithful normal semifinite weight \(\psi\) on \(N\) determine a positive self-adjoint operator
\[
\frac{d\varphi}{d\psi}\quad\text{on } H,
\]
the *spatial derivative* of \(\varphi\) with respect to \(\psi\). Two cases show what to expect.

- If \(M=N=L^\infty(X,\mu)\) acts on \(L^2(X,\mu)\), \(\psi=\int\cdot\,g\,d\mu\) and \(\varphi=\int\cdot\,h\,d\mu\),
  then \(d\varphi/d\psi\) is multiplication by \(h/g\): an honest Radon–Nikodym derivative (Example 3.7).
- If \(M=B(H)\), so that \(N=\mathbb C1\), every normal semifinite weight on \(M\) has the form
  \(\operatorname{Tr}_S\), formally \(x\mapsto\operatorname{Tr}(S^{1/2}xS^{1/2})\), and \(d\varphi/d\psi\) is the density \(S\), up to the scalar
  \(\psi(1)\) (Example 3.5).

In general \(d\varphi/d\psi\) is neither affiliated with \(M\) nor with \(N\). Its imaginary powers implement both
modular groups at once:
\[
\Big(\frac{d\varphi}{d\psi}\Big)^{it}x\Big(\frac{d\varphi}{d\psi}\Big)^{-it}=\sigma^\varphi_t(x)\ (x\in M),\qquad
\Big(\frac{d\varphi}{d\psi}\Big)^{it}y\Big(\frac{d\varphi}{d\psi}\Big)^{-it}=\sigma^\psi_{-t}(y)\ (y\in N).
\]
The construction is short. A vector \(\xi\in H\) is \(\psi\)-bounded if \(y\mapsto y\xi\) is bounded for the GNS norm
of \(\psi\); each such vector gives an element \(\theta^\psi(\xi,\xi)\ge0\) of \(M\), and \(d\varphi/d\psi\) is the
operator of the closed quadratic form obtained from \(\xi\mapsto\varphi(\theta^\psi(\xi,\xi))\).

**What the lesson does.**

1. Sections 1 and 2 set up \(\psi\)-bounded vectors on an arbitrary module over \(N\), the ideal of \(M\) they
   generate, and lower semicontinuous quadratic forms.
2. Section 3 defines \(d\varphi/d\psi\), shows how to recover \(\varphi\) from it, and proves monotonicity and
   covariance. Section 4 realizes \(d\varphi/d\psi\) as a corner of a modular operator and proves the two modular
   formulas above.
3. Section 5 proves the chain rules in both variables, the inversion formula
   \(d\psi/d\varphi=(d\varphi/d\psi)^{-1}\), and the inequality
   \(|\langle\xi,\eta\rangle|^2\le\varphi(\theta^\psi(\xi,\xi))\,\psi(\theta^\varphi(\eta,\eta))\).
4. Section 6 characterizes the operators of the form \(d\varphi/d\psi\): a positive self-adjoint operator is of this
   form if and only if it is *homogeneous of degree \(-1\)*. As an application,
   \(\sigma^{\varphi_n}_t\to\sigma^\varphi_t\) when
   \(\varphi_n\) increases to \(\varphi\).
5. Section 7 constructs a faithful normal semifinite operator-valued weight \(\Psi^{-1}\) from \(B(H)\) to \(M\) with
   \(\varphi\circ\Psi^{-1}=\operatorname{Tr}\big((d\varphi/d\psi)\,\cdot\,\big)\), and shows every such
   operator-valued weight arises this way. Section 8 introduces the integral \(\int T\,d\psi\) of a positive operator
   homogeneous of degree \(-1\), and proves that for \(T\) homogeneous of degree \(-\tfrac12\) the operators
   \(T^*T\) and \(TT^*\) have the same integral.

The lessons "Square-integrable representations and random operators" and "Weights on random operators and formal
dimension" of this course use the spatial derivative, the operator-valued weight \(\Psi^{-1}\) (Section 7), and the
homogeneous operators of degrees \(-1\) and \(-\tfrac12\) (Sections 6 and 8).

**What is assumed.** We assume Tomita–Takesaki theory for weights, the Connes cocycle derivative, closed quadratic
forms, and operator-valued weights. The facts used are listed in "Results used from other lessons", with the
lesson that proves each. The course *Modular theory and weights* also contains a parallel treatment of the spatial
derivative itself, in the lessons Spatial comparison on an arbitrary representation,
Constructing spatial energy from finite observations, Adding spatial energies and changing the
reference weight, Spatial energy as a corner of a modular operator and
Recovering a weight from spatial energy; they can serve as further reading. The present lesson is
self-contained on its topic.

Basic references are [Connes 1980a], [Connes 1979] and [Connes 1994].

## Conventions

- Inner products are linear in the first variable. For \(\xi\in H\), \(\xi\xi^*\) is the rank-one operator
  \(\zeta\mapsto\langle\zeta,\xi\rangle\xi\).
- A *weight* on a von Neumann algebra \(A\) is a map \(A_+\to[0,\infty]\) that is additive and positively
  homogeneous; *normal* means \(\varphi(\sup_i x_i)=\sup_i\varphi(x_i)\) for bounded increasing nets. We write
  \(\mathfrak n_\varphi=\{x:\varphi(x^*x)<\infty\}\) and \(\mathfrak m_\varphi=\operatorname{span}\{x\in
  A_+:\varphi(x)<\infty\}\). *Fns* abbreviates "faithful normal semifinite". The support of a normal weight is
  \(s(\varphi)\).
- \(\sigma^\varphi\) is the modular automorphism group of an fns weight \(\varphi\), and \((D\varphi_2:D\varphi_1)_t\)
  the Connes cocycle derivative.
- Let \(T\) be positive and self-adjoint. For \(\zeta\in H\) we write
  \[
  \langle T\zeta,\zeta\rangle=\|T^{1/2}\zeta\|^2\ \text{ if }\zeta\in\operatorname{dom}T^{1/2},\qquad
  \langle T\zeta,\zeta\rangle=+\infty\ \text{ otherwise.}
  \]
  For positive self-adjoint \(S,T\) we write \(S\le T\) when \(\langle S\zeta,\zeta\rangle\le\langle
  T\zeta,\zeta\rangle\) for all \(\zeta\in H\). When \(\zeta\mapsto\langle T_1\zeta,\zeta\rangle+\langle
  T_2\zeta,\zeta\rangle\) is finite on a dense set, the positive self-adjoint operator of this closed form is the
  *form sum* \(T_1\dotplus T_2\).
- For a positive self-adjoint \(T\) and \(t\in\mathbb R\), \(T^{it}\) is defined by the functional calculus with the
  convention \(0^{it}=0\). So \(T^{it}\) is a partial isometry whose initial and final projection is the support
  \(s(T)\), the projection onto \((\ker T)^\perp\); \(T\) is *nonsingular* when \(s(T)=1\).
- \(\operatorname{Tr}_S\) is the normal weight on \(B(H)\) of density \(S\) (Background B6).

## Results used from other lessons

**(B1) Forms and positive operators.** (i) The map \(T\mapsto(\zeta\mapsto\|T^{1/2}\zeta\|^2,\
\operatorname{dom}T^{1/2})\) is a bijection from positive self-adjoint operators on \(H\) onto closed, densely
defined, positive quadratic forms on \(H\). A *core* of such a form is a subspace of \(\operatorname{dom}T^{1/2}\)
dense for the norm \((\|\zeta\|^2+\|T^{1/2}\zeta\|^2)^{1/2}\). (ii) For positive self-adjoint \(S,T\): \(S\le T\) iff
\((1+T)^{-1}\le(1+S)^{-1}\); for nonsingular \(S,T\): \(S\le T\) iff \(T^{-1}\le S^{-1}\). (iii) (Stone's theorem)
Every strongly continuous one-parameter group of unitaries is \(t\mapsto S^{it}\) for a unique positive nonsingular
\(S\); a closed subspace invariant under all \(S^{it}\) reduces \(S\). (i) is Recovering operators from energy forms,
§QF-03, with cores as in Closing energy domains and comparing resolvents,
§FC-05. The first equivalence in (ii) is §FC-06 there; for nonsingular \(S,T\) the
identity \((S^{-1}+\mu)^{-1}=\mu^{-1}-\mu^{-2}(S+\mu^{-1})^{-1}\) turns the resolvent criterion for \(T^{-1}\le S^{-1}\)
into the one for \(S\le T\). Stone's theorem is Analytic elements and strip arguments, Theorem 8.1(3).
If a closed subspace is invariant under all \(S^{it}\), it is invariant under their adjoints \(S^{-it}\), so its
projection \(P\) commutes with them; the restrictions to \(PH\) and \((1-P)H\) are strongly continuous unitary groups,
hence of the form \(S_1^{it}\) and \(S_2^{it}\), and uniqueness in Stone's theorem gives \(S=S_1\oplus S_2\).

**(B2) Normal weights.** Fix a von Neumann algebra \(A\). (i) Every normal weight on \(A\) is a sum
\(\sum_i\omega_i\) of positive normal functionals; in particular it is \(\sigma\)-weakly lower semicontinuous. (ii) If
\(A\) acts on a Hilbert space \(K\), every \(\omega\in A_*^+\) has the form \(\omega=\sum_n\langle\cdot\,\zeta_n,
\zeta_n\rangle\) with \(\sum_n\|\zeta_n\|^2<\infty\). (iii) A normal weight \(\varphi\) satisfies
\(\varphi(x)=\varphi(s x s)\) for \(x\in A_+\), \(s=s(\varphi)\); its restriction to \(sAs\) is faithful, and
semifinite if \(\varphi\) is. (iv) If \(\varphi\) is semifinite, \(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*\) is a
\(\sigma\)-weakly dense \(*\)-subalgebra, and by the Kaplansky density theorem it contains a net of contractions
converging \(\sigma\)-strongly\(^*\) to \(1\). (v) Every von Neumann algebra carries an fns weight. Lower
semicontinuity in (i) is Detecting normal weights by finite observations, §NW-11; for
the sum decomposition see [Haagerup 1975]. (ii): a normal positive functional is \(\sigma\)-strongly continuous (Compact
and trace-class operators, Theorem 9.1(ii)), so The double commutant theorem, Theorem
10.1 applies. (iii) is Finite domains, null directions, and support corners, §§WS-05 and
WS-06. (iv): by General weights: finite domains, GNS spaces, and normal
representations, §WG-008 there are positive contractions \(e_i\uparrow1\) with
\(\varphi(e_i)<\infty\); they lie in \(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*\), since \(e_i^2\le e_i\), and
\(e_ixe_i\to x\) \(\sigma\)-weakly. (v) is Weights and the Hilbert spaces of multiplication,
§WH-13.

**(B3) Modular theory.** Let \(\psi\) be an fns weight on \(N\), with GNS construction \((H_\psi,\pi_\psi,\eta_\psi)\):
\(\eta_\psi:\mathfrak n_\psi\to H_\psi\) is linear with dense range, \(\langle\eta_\psi(y),\eta_\psi(z)\rangle=
\psi(z^*y)\) and \(\pi_\psi(x)\eta_\psi(y)=\eta_\psi(xy)\). Let \(\Delta_\psi\), \(J_\psi\) be its modular operator and
conjugation; we identify \(N\) with \(\pi_\psi(N)\).
(i) \(\sigma^\psi_t(y)=\Delta_\psi^{it}y\Delta_\psi^{-it}\), \(\eta_\psi(\sigma^\psi_t(y))=\Delta_\psi^{it}\eta_\psi(y)\)
for \(y\in\mathfrak n_\psi\), \(\psi\circ\sigma^\psi_t=\psi\), and \(J_\psi NJ_\psi=N'\).
(ii) For \(y\in\mathfrak n_\psi\): \(y^*\in\mathfrak n_\psi\) iff \(\eta_\psi(y)\in\operatorname{dom}\Delta_\psi^{1/2}\),
and then \(\|\Delta_\psi^{1/2}\eta_\psi(y)\|^2=\psi(yy^*)\). The subspace \(\eta_\psi(\mathfrak n_\psi\cap\mathfrak
n_\psi^*)\) is a core for \(\Delta_\psi^{1/2}\).
(iii) The elements \(y\in N\) for which \(t\mapsto\sigma^\psi_t(y)\) extends to an entire function
\(w\mapsto\sigma^\psi_w(y)\) form a \(\sigma\)-weakly dense \(*\)-subalgebra \(N_0\), invariant under every
\(\sigma^\psi_t\). For \(y\in N_0\) and \(z\in\mathfrak n_\psi\) one has \(zy\in\mathfrak n_\psi\) and
\(\eta_\psi(zy)=J_\psi\sigma^\psi_{-i/2}(y^*)J_\psi\,\eta_\psi(z)\).
(iv) (Balanced weights.) Let \(\Theta\) be an fns weight on a von Neumann algebra \(P\) and \(f\in P\) a projection.
Then \(\sigma^\Theta_t(f)=f\) for all \(t\) iff \(\Theta(x)=\Theta(fxf)+\Theta((1-f)x(1-f))\) for all \(x\in P_+\); in
that case the restriction of \(\Theta\) to \(fPf\) is fns with modular group \(\sigma^\Theta_t|_{fPf}\). Conversely, if
\(\Theta_1,\Theta_2\) are fns weights on \(fPf\) and \((1-f)P(1-f)\), then \(\Theta_1\oplus\Theta_2:x\mapsto
\Theta_1(fxf)+\Theta_2((1-f)x(1-f))\) is an fns weight on \(P\) whose modular group fixes \(f\).
These are proved in the course *Modular theory and weights*. (i): The modular group and its analytic algebra,
§§MF-05–MF-06, with \(\pi_\psi(y)=\lambda_{\eta_\psi(y)}\). (ii): the left Hilbert algebra
of \(\psi\) is full (Weights and the Hilbert spaces of multiplication, §WH-11), so
\(\eta_\psi(\mathfrak n_\psi\cap\mathfrak n_\psi^*)\) is the set of left-bounded vectors in the domain of the closed involution
\(S=J_\psi\Delta_\psi^{1/2}\), which has the same domain and graph norm as \(\Delta_\psi^{1/2}\) (Closing an involution and
recovering its modular data, §TC-08), and
\(\|\Delta_\psi^{1/2}\eta_\psi(y)\|=\|\eta_\psi(y^*)\|\). (iii): §§MF-07–MF-09 of the lesson on the modular group, and
Analytic elements and strip arguments, Theorem 11.1(2) with
\(\sigma^\psi_{i/2}(y)^*=\sigma^\psi_{-i/2}(y^*)\) (Theorem 9.1(1) there). (iv): a projection fixed by \(\sigma^\Theta\) lies
in the centralizer, so \(\Theta\) is invariant under conjugation by the unitary \(2f-1\), and conversely; this is the
projection lemma and (CZ.32) of Fixed observations, density weights and modular time, §CZ-09, with
(CZ.18) of §CZ-05, and the reduction to \(fPf\) is in §CZ-09; the weight \(\Theta_1\oplus\Theta_2\) is fns by Spatial energy
as a corner of a modular operator, §SI-05, and it is invariant under conjugation by
\(2f-1\).

**(B4) The commutant weight.** Keep the notation of (B3) and let \(D(H_\psi,\psi)\) be the set of \(\xi\in H_\psi\)
for which \(\eta_\psi(y)\mapsto y\xi\) extends to a bounded operator \(R^\psi(\xi)\) (these are the right-bounded
vectors; \(R^\psi(\xi)\in N'\)). (i) There is a unique fns weight \(\psi'\) on \(N'\) such that \(R^\psi\) is a
bijection of \(D(H_\psi,\psi)\) onto \(\mathfrak n_{\psi'}\) with \(\psi'(R^\psi(\xi)^*R^\psi(\xi))=\|\xi\|^2\); it is
\(\psi'(x)=\psi(J_\psi xJ_\psi)\). Thus \(\eta_{\psi'}(R^\psi(\xi))=\xi\) is a GNS map for \(\psi'\) on \(H_\psi\); in
this realization \(\Delta_{\psi'}=\Delta_\psi^{-1}\), and \(\sigma^{\psi'}_t(x)=\Delta_\psi^{-it}x\Delta_\psi^{it}\).
(ii) A vector \(\zeta\in H_\psi\) satisfies \(\sup\{\|R^\psi(\xi)\zeta\|:\xi\in D(H_\psi,\psi),\|\xi\|\le1\}<\infty\) iff
\(\zeta=\eta_\psi(y)\) for some \(y\in\mathfrak n_\psi\); then \(R^\psi(\xi)\eta_\psi(y)=y\xi\). (i): Weights and the
Hilbert spaces of multiplication, §WH-12 constructs the weight on \(N'\) from the
right-bounded vectors, with finite ideal \(R^\psi(D(H_\psi,\psi))\) and the stated norm formula; it is the weight of the
opposite of the right Hilbert algebra, whose closed involution is \(F=S^*=J_\psi\Delta_\psi^{-1/2}\) (Closing an involution
and recovering its modular data, §TC-09), so its modular operator is \(\Delta_\psi^{-1}\) and
its modular group is \(\operatorname{Ad}\Delta_\psi^{-it}\) (The modular group and its analytic algebra,
§MF-06, for that algebra); and \(J_\psi R^\psi(\xi)J_\psi=\lambda_{J_\psi\xi}\) ((MF.21) of §MF-05
there, at \(t=0\)) gives \(\psi'(x)=\psi(J_\psi xJ_\psi)\). (ii): the left-bounded vectors are exactly \(\eta_\psi(\mathfrak
n_\psi)\) (§WH-11), and \(R^\psi(\xi)\eta_\psi(y)=\lambda_{\eta_\psi(y)}\xi=y\xi\) (§WH-04).

**(B5) The Connes cocycle.** Let \(\varphi_1,\varphi_2\) be fns weights on \(M\) and \(\Phi=\varphi_1\oplus\varphi_2\)
the balanced weight \(\sum x_{ij}\otimes e_{ij}\mapsto\varphi_1(x_{11})+\varphi_2(x_{22})\) on \(M\otimes M_2(\mathbb
C)\). There are unitaries \(u_t=(D\varphi_2:D\varphi_1)_t\in M\) with \(\sigma^\Phi_t(x\otimes e_{21})=u_t
\sigma^{\varphi_1}_t(x)\otimes e_{21}\). The map \(t\mapsto u_t\) is strongly continuous and \(u_{s+t}=u_s
\sigma^{\varphi_1}_s(u_t)\). (ii) Conversely, every strongly continuous family of unitaries \(u_t\in M\) with
\(u_{s+t}=u_s\sigma^{\varphi_1}_s(u_t)\) is \((D\varphi:D\varphi_1)\) for a unique fns weight \(\varphi\). In
particular, two fns weights with the same cocycle relative to \(\varphi_1\) are equal. (i) is Supported GNS
representations and the balanced cocycle, §§GC-03–GC-04 and Comparing supported weights
and transporting their cuts, §WC-02; (ii) is Reconstructing a weight from a modular
cocycle, §CX-10. See also [Connes 1973].

**(B6) Weights on \(B(H)\).** (i) For every positive self-adjoint \(S\) on \(H\) there is a unique normal weight
\(\operatorname{Tr}_S\) on \(B(H)\) with \(\operatorname{Tr}_S(\zeta\zeta^*)=\langle S\zeta,\zeta\rangle\) for all
\(\zeta\in H\); if \(x=\sum_k\zeta_k\zeta_k^*\) (a \(\sigma\)-weakly convergent sum) then
\(\operatorname{Tr}_S(x)=\sum_k\langle S\zeta_k,\zeta_k\rangle\). It is semifinite, and faithful iff \(S\) is
nonsingular. (ii) Every normal semifinite weight on \(B(H)\) is \(\operatorname{Tr}_S\) for a unique \(S\). (iii) For
nonsingular \(S\), \(\sigma^{\operatorname{Tr}_S}_t=\operatorname{Ad}S^{it}\); hence, applying (B5) on
\(B(H)\otimes M_2(\mathbb C)=B(H\oplus H)\) with \(\operatorname{Tr}_{S_1}\oplus\operatorname{Tr}_{S_2}=
\operatorname{Tr}_{S_1\oplus S_2}\), one gets \((D\operatorname{Tr}_{S_2}:D\operatorname{Tr}_{S_1})_t=
S_2^{it}S_1^{-it}\). (ii) and the existence and uniqueness in (i) are Recognizing a weight by its fixed density,
§PT-08, applied to the trace \(\operatorname{Tr}\), with \(\operatorname{Tr}_S\) its weight of
density \(S\): its value at \(\zeta\zeta^*\) is \(\sup_\varepsilon\|S_\varepsilon^{1/2}\zeta\|^2=\langle S\zeta,\zeta\rangle\);
normality, semifiniteness and the support are Fixed observations, density weights and modular time, §CZ-08.
(iii): \((D\operatorname{Tr}_S:D\operatorname{Tr})_t=S^{it}\) by §PT-04 of the first lesson, since \(\sigma^{\operatorname{Tr}}\) is
trivial (PT-08), and the chain rule (Changing reference for a weight cocycle, §CH-01)
gives the cocycle of two such weights.

**(B7) Operator-valued weights.** Let \(M\subset P\) be von Neumann algebras with the same unit. The extended
positive part \(\widehat M_+\) is the set of additive, positively homogeneous, lower semicontinuous maps
\(M_*^+\to[0,\infty]\); it contains \(M_+\), and \(m_1\le m_2\) means \(m_1(\omega)\le m_2(\omega)\) for all
\(\omega\). Every normal weight \(\varphi\) on \(M\) extends to a normal additive map \(\widehat M_+\to[0,\infty]\)
(if \(\varphi=\sum\omega_i\), then \(\varphi(m)=\sum m(\omega_i)\)). The *operator-valued weights* from \(P\) to \(M\) are
the additive, positively homogeneous maps \(E:P_+\to\widehat M_+\) with \(E(a^*xa)=a^*E(x)a\) for \(a\in M\); such an
\(E\) is *normal* if \(E(\sup x_i)=\sup E(x_i)\), and faithful and semifinite are defined as for weights. For normal
\(E\) and a normal weight \(\varphi\) on \(M\), \(\varphi\circ E\) is a normal weight on \(P\). (i) If \(E\) and \(\varphi\) are
fns, then \(\varphi\circ E\) is fns, \(\sigma^{\varphi\circ E}_t(x)=\sigma^\varphi_t(x)\) for \(x\in M\), and
\((D(\varphi_2\circ E):D(\varphi_1\circ E))_t=(D\varphi_2:D\varphi_1)_t\). (ii) (Haagerup's existence theorem) If
\(\varphi\) is fns on \(M\) and \(\chi\) is fns on \(P\) with \(\sigma^\chi_t(x)=\sigma^\varphi_t(x)\) for \(x\in M\),
there is a unique fns operator-valued weight \(E\) from \(P\) to \(M\) with \(\chi=\varphi\circ E\).
These are proved in the course *Modular theory and weights*: the extension of normal weights to the extended positive
part and the composition \(\varphi\circ E\) in Finite calculus and composition of operator-valued weights, §§OVW-02 and
OVW-04; (i) in Modular invariants of operator-valued weights,
§OM-01; (ii) in Compatible modular weights and the full positive cone,
§§OE-01–OE-06. See also [Haagerup 1979].

## 1. Modules over \(N\) and \(\psi\)-bounded vectors

A reference for this section and the next three is [Connes 1980a].

Throughout this section \(N\) is a von Neumann algebra and \(\psi\) an fns weight on \(N\), with GNS construction as
in (B3). An *\(N\)-module* is a Hilbert space \(H\) with a normal unital \(*\)-representation \(\pi\) of \(N\); we
write \(y\xi=\pi(y)\xi\). We write \(\mathcal L_N(H)=\pi(N)'\) and \(\operatorname{Hom}_N(H_1,H_2)\) for the bounded
\(N\)-linear maps between modules. The GNS space \(H_\psi\) is an \(N\)-module, and \(\mathcal L_N(H_\psi)=N'\) carries
the weight \(\psi'\) of (B4).

**Definition 1.1.** Let \(H\) be an \(N\)-module. A vector \(\xi\in H\) is *\(\psi\)-bounded* if there is \(C<\infty\)
with
\[
\|y\xi\|\le C\,\|\eta_\psi(y)\|=C\,\psi(y^*y)^{1/2}\qquad(y\in\mathfrak n_\psi). \tag{1.1}
\]
The set of \(\psi\)-bounded vectors is denoted \(D(H,\psi)\). For \(\xi\in D(H,\psi)\), \(R^\psi(\xi)\) is the bounded
operator \(H_\psi\to H\) with \(R^\psi(\xi)\eta_\psi(y)=y\xi\). For \(\xi,\eta\in D(H,\psi)\) we put
\[
\theta^\psi(\xi,\eta)=R^\psi(\xi)R^\psi(\eta)^*\in B(H).
\]

For \(H=H_\psi\) these are exactly the right-bounded vectors of (B4). The operator \(R^\psi(\xi)\) intertwines the
actions: \(R^\psi(\xi)x\eta_\psi(y)=xy\xi=xR^\psi(\xi)\eta_\psi(y)\), so \(R^\psi(\xi)\in\operatorname{Hom}_N(H_\psi,
H)\) and \(\theta^\psi(\xi,\eta)\in\mathcal L_N(H)\).

**Lemma 1.2.** Let \(H,H_2\) be \(N\)-modules and \(\xi,\eta\in D(H,\psi)\).

(a) \(D(H,\psi)\) is a subspace and \(R^\psi\) is linear. If \(A\in\operatorname{Hom}_N(H,H_2)\) then \(A\xi\in
D(H_2,\psi)\) and \(R^\psi(A\xi)=AR^\psi(\xi)\). In particular \(D(H,\psi)\) is invariant under \(\mathcal L_N(H)\),
and \(\theta^\psi(A\xi,B\eta)=A\,\theta^\psi(\xi,\eta)B^*\) for \(A,B\in\mathcal L_N(H)\).

(b) \(\xi\) lies in the closure of the range of \(R^\psi(\xi)\). In particular \(R^\psi(\xi)=0\) only for \(\xi=0\).

(c) For every \(\omega\in H\),
\[
\langle\theta^\psi(\xi,\xi)\omega,\omega\rangle=\sup\{|\langle y\xi,\omega\rangle|^2:\ y\in\mathfrak n_\psi,\
\psi(y^*y)\le1\}. \tag{1.2}
\]

(d) \(\theta^\psi\) is sesquilinear, \(\theta^\psi(\xi,\eta)^*=\theta^\psi(\eta,\xi)\), \(\theta^\psi(\xi,\xi)\ge0\), and
\(\theta^\psi(\xi+\eta,\xi+\eta)+\theta^\psi(\xi-\eta,\xi-\eta)=2\theta^\psi(\xi,\xi)+2\theta^\psi(\eta,\eta)\).

(e) Let \(y\in N_0\) be entire for \(\sigma^\psi\) (B3(iii)) and put \(\rho_\psi(y)=J_\psi\sigma^\psi_{-i/2}(y^*)
J_\psi\in N'\). Then \(\rho_\psi(y)\eta_\psi(z)=\eta_\psi(zy)\) for \(z\in\mathfrak n_\psi\), \(y\xi\in D(H,\psi)\),
and \(R^\psi(y\xi)=R^\psi(\xi)\rho_\psi(y)\).

*Proof.* (a) If \(\xi,\eta\) satisfy (1.1) with constants \(C,C'\), then \(\xi+\eta\) satisfies it with \(C+C'\); the
map \(\xi\mapsto R^\psi(\xi)\) is linear on the dense set \(\eta_\psi(\mathfrak n_\psi)\), hence linear. For \(A\) as
stated, \(\|yA\xi\|=\|Ay\xi\|\le\|A\|C\|\eta_\psi(y)\|\), and \(R^\psi(A\xi)\eta_\psi(y)=yA\xi=AR^\psi(\xi)
\eta_\psi(y)\). The formula for \(\theta^\psi\) follows: \(R^\psi(A\xi)R^\psi(B\eta)^*=AR^\psi(\xi)R^\psi(\eta)^*B^*\).

(b) By (B2)(iv) there is a net \((y_i)\) in \(\mathfrak n_\psi\) of contractions with \(y_i\to1\) strongly in every
normal representation. Then \(R^\psi(\xi)\eta_\psi(y_i)=y_i\xi\to\xi\).

(c) The left side is \(\|R^\psi(\xi)^*\omega\|^2\). The vectors \(\eta_\psi(y)\) with \(\psi(y^*y)\le1\) are dense in
the unit ball of \(H_\psi\), and \(\langle R^\psi(\xi)^*\omega,\eta_\psi(y)\rangle=\langle\omega,y\xi\rangle\).

(d) All claims follow from the linearity of \(R^\psi\).

(e) The first claim is (B3)(iii). Then \(\|zy\xi\|\le C\|\eta_\psi(zy)\|\le C\|\rho_\psi(y)\|\,\|\eta_\psi(z)\|\), so
\(y\xi\in D(H,\psi)\), and \(R^\psi(y\xi)\eta_\psi(z)=zy\xi=R^\psi(\xi)\eta_\psi(zy)=R^\psi(\xi)\rho_\psi(y)
\eta_\psi(z)\). \(\square\)

**Proposition 1.3.** For every \(N\)-module \(H\), \(D(H,\psi)\) is dense in \(H\).

*Proof.* The kernel of the representation \(\pi\) is \(N(1-c)\) for a central projection \(c\), and \(\pi\) restricts
to an isomorphism of \(Nc\) onto the von Neumann algebra \(\pi(N)\). The restriction of \(\psi\) to \(Nc\) is a
normal weight; by (B2)(i) and (B2)(ii), applied to \(\pi(N)\) on \(H\), there is a family \((\zeta_j)\) in \(H\) with
\(\psi(y)=\sum_j\langle y\zeta_j,\zeta_j\rangle\) for \(y\in(Nc)_+\). For \(y\in N\) we have \(y^*y\ge cy^*y\) and
\(\pi(y^*y)=\pi(cy^*y)\), hence
\[
\|y\zeta_j\|^2\le\sum_k\langle cy^*y\,\zeta_k,\zeta_k\rangle=\psi(cy^*y)\le\psi(y^*y).
\]
So every \(\zeta_j\) is \(\psi\)-bounded. Let \(E\) be the projection onto the closure of \(D(H,\psi)\). By Lemma
1.2(a) this closure is invariant under the \(*\)-algebra \(\mathcal L_N(H)\), so \(E\in\mathcal L_N(H)'=\pi(N)\), say
\(E=\pi(e)\) with \(e\le c\) a projection of \(Nc\). Since \(E\zeta_j=\zeta_j\),
\[
\psi(c-e)=\sum_j\langle\pi(c-e)\zeta_j,\zeta_j\rangle=\sum_j\langle(1-E)\zeta_j,\zeta_j\rangle=0.
\]
As \(\psi\) is faithful, \(e=c\) and \(E=\pi(c)=1\). \(\square\)

**Lemma 1.4.** Let \(H\) be an \(N\)-module.

(a) For \(\xi,\eta\in D(H,\psi)\), \(R^\psi(\eta)^*R^\psi(\xi)\in\mathfrak m_{\psi'}\) and
\(\psi'(R^\psi(\eta)^*R^\psi(\xi))=\langle\xi,\eta\rangle\). In particular \(\psi'(R^\psi(\xi)^*R^\psi(\xi))=
\|\xi\|^2\).

(b) Conversely, if \(b\in\operatorname{Hom}_N(H_\psi,H)\) and \(\psi'(b^*b)<\infty\), there is a unique \(\xi\in
D(H,\psi)\) with \(b=R^\psi(\xi)\).

*Proof.* (a) By polarization it suffices to treat \(\eta=\xi\). Let \(R^\psi(\xi)=v|R^\psi(\xi)|\) be the polar
decomposition; \(v\in\operatorname{Hom}_N(H_\psi,H)\) and \(vv^*\) is the projection onto the closure of the range of
\(R^\psi(\xi)\), so \(vv^*\xi=\xi\) by Lemma 1.2(b). By Lemma 1.2(a), \(v^*\xi\in D(H_\psi,\psi)\) and
\(R^\psi(v^*\xi)=v^*R^\psi(\xi)\). Hence
\[
R^\psi(\xi)^*R^\psi(\xi)=R^\psi(\xi)^*vv^*R^\psi(\xi)=R^\psi(v^*\xi)^*R^\psi(v^*\xi),
\]
and (B4)(i) gives \(\psi'(R^\psi(\xi)^*R^\psi(\xi))=\|v^*\xi\|^2=\|\xi\|^2\).

(b) Write \(b=v|b|\). Then \(|b|\in N'\) and \(\psi'(|b|^2)<\infty\), so \(|b|\in\mathfrak n_{\psi'}\) and, by (B4)(i),
\(|b|=R^\psi(\zeta)\) for some \(\zeta\in D(H_\psi,\psi)\). By Lemma 1.2(a), \(b=vR^\psi(\zeta)=R^\psi(v\zeta)\).
Uniqueness follows from Lemma 1.2(b). \(\square\)

**Proposition 1.5.** Fix an \(N\)-module \(H\), put \(M=\mathcal L_N(H)\), and write \(\mathcal J_\psi\) for the linear
span of the operators \(\theta^\psi(\xi,\eta)\), \(\xi,\eta\in D(H,\psi)\).

(a) There is a family \((\xi_\alpha)_{\alpha\in I}\) in \(D(H,\psi)\) such that the \(\theta^\psi(\xi_\alpha,\xi_\alpha)\)
are mutually orthogonal projections with \(\sum_\alpha\theta^\psi(\xi_\alpha,\xi_\alpha)=1\). We call such a family a
*\(\psi\)-basis* of \(H\).

(b) \(\mathcal J_\psi\) is a two-sided ideal in \(M\), closed under \(x\mapsto x^*\) and \(\sigma\)-weakly dense.

(c) Each positive element of \(\mathcal J_\psi\) has the form \(\sum_{i=1}^n\theta^\psi(\xi_i,\xi_i)\) with
\(\xi_i\in D(H,\psi)\) and \(n\) finite.

*Proof.* We first note a factorization. *If \(0\le A\le B\) in \(M\), there is \(C\in M\) with \(\|C\|\le1\) and
\(A=CBC^*\).* Indeed \(\|A^{1/2}h\|\le\|B^{1/2}h\|\), so \(B^{1/2}h\mapsto A^{1/2}h\) extends to a contraction \(C\) on
the closure of the range of \(B^{1/2}\); put \(C=0\) on its orthogonal complement. Every unitary \(u'\in M'\) leaves
both subspaces invariant and satisfies \(Cu'=u'C\) on them, so \(C\in M''=M\); and \(A^{1/2}=CB^{1/2}\) gives
\(A=CBC^*\).

(a) By Zorn's lemma choose a maximal family \((\xi_\alpha)\) in \(D(H,\psi)\) such that the
\(p_\alpha=\theta^\psi(\xi_\alpha,\xi_\alpha)\) are nonzero, mutually orthogonal projections, and let
\(p=\sum p_\alpha\in M\). Suppose \(p\ne1\). By Proposition 1.3 there is \(\xi\in D(H,\psi)\) with
\((1-p)\xi\ne0\). Then \(\xi'=(1-p)\xi\in D(H,\psi)\) and \(a=\theta^\psi(\xi',\xi')=(1-p)\theta^\psi(\xi,\xi)(1-p)\)
is nonzero by Lemma 1.2(b). Choose \(0<\delta<\|a\|\), let \(g=\chi_{[\delta,\infty)}(a)\ne0\), and let \(c=h(a)\in
M\) with \(h(\lambda)=\lambda^{-1/2}\) on \([\delta,\infty)\) and \(h=0\) elsewhere. Then \(\xi''=c\xi'\in D(H,\psi)\)
and \(\theta^\psi(\xi'',\xi'')=cac=g\), a nonzero projection below the support of \(a\), hence orthogonal to \(p\).
This contradicts maximality.

(b) By Lemma 1.2(a),(d), \(\mathcal J_\psi\) is a two-sided ideal stable under adjoints. For a \(\psi\)-basis let
\(e_F=\sum_{\alpha\in F}\theta^\psi(\xi_\alpha,\xi_\alpha)\) for finite \(F\subset I\). Then \(e_F\in\mathcal J_\psi\),
\(e_F\uparrow1\) strongly, and \(x=\lim_F xe_F\) with \(xe_F\in\mathcal J_\psi\) for every \(x\in M\).

(c) Let \(A=\sum_{i=1}^n\theta^\psi(\xi_i,\eta_i)\ge0\). Then \(A=\frac12(A+A^*)\) and, by Lemma 1.2(d),
\[
\theta^\psi(\xi,\eta)+\theta^\psi(\eta,\xi)=\tfrac12\big(\theta^\psi(\xi+\eta,\xi+\eta)-\theta^\psi(\xi-\eta,
\xi-\eta)\big)\le\tfrac12\theta^\psi(\xi+\eta,\xi+\eta).
\]
So \(0\le A\le B=\sum_i\theta^\psi(\zeta_i,\zeta_i)\) with \(\zeta_i=\frac12(\xi_i+\eta_i)\). With \(C\) from the
factorization, \(A=CBC^*=\sum_i\theta^\psi(C\zeta_i,C\zeta_i)\). \(\square\)

We write \(\mathcal J_\psi^+\) for the positive part of \(\mathcal J_\psi\).

**Remark 1.6 (modules that are not faithful).** If \(\pi\) has kernel \(N(1-c)\), then \(\pi(N)\cong Nc\) carries the
fns weight \(\psi_c=\psi|_{Nc}\), with \(\sigma^{\psi_c}_t=\sigma^\psi_t|_{Nc}\). A vector is \(\psi\)-bounded iff it is
\(\psi_c\)-bounded (since \(\pi(y)=\pi(yc)\) and \(\psi(y^*y)\ge\psi(cy^*y)\)), and \(\theta^\psi=\theta^{\psi_c}\), as
(1.2) shows. So whatever is proved below for a von Neumann algebra \(M\) on \(H\) with commutant \(N\) applies to
\(M=\mathcal L_N(H)\) for any \(N\)-module \(H\), with commutant \(\pi(N)\) and the weight \(\psi_c\).

## 2. Lower semicontinuous quadratic forms

**Definition 2.1.** Fix a dense subspace \(D\) of \(H\). A *positive form on \(D\)* is a map
\(q:D\to[0,\infty]\) with \(q(\lambda\xi)=|\lambda|^2q(\xi)\) and \(q(\xi+\eta)+q(\xi-\eta)=2q(\xi)+2q(\eta)\). Its
*domain* is \(D_q=\{\xi\in D:q(\xi)<\infty\}\). It is *lower semicontinuous* if \(q(\xi)\le\liminf q(\xi_n)\) whenever
\(\xi_n\to\xi\) in norm inside \(D\).

The parallelogram law gives \(q(\xi+\eta)\le2q(\xi)+2q(\eta)\), so \(D_q\) is a subspace, and on it \(q\) is the
quadratic form of a unique positive sesquilinear form (by polarization, the Jordan–von Neumann theorem).

**Lemma 2.2.** For a positive self-adjoint \(T\), the map \(\zeta\mapsto\langle T\zeta,\zeta\rangle\in[0,\infty]\) is
lower semicontinuous on \(H\).

*Proof.* With \(\mu_\zeta\) the spectral measure of \(T\) at \(\zeta\), monotone convergence gives \(\langle
T\zeta,\zeta\rangle=\int\lambda\,d\mu_\zeta=\sup_n\int\frac{\lambda}{1+\lambda/n}d\mu_\zeta=\sup_n\langle
T(1+T/n)^{-1}\zeta,\zeta\rangle\), a supremum of continuous functions. \(\square\)

**Proposition 2.3.** Let \(q\) be a positive form on a dense subspace \(D\), with \(D_q\) dense. The following are
equivalent.

(i) \(q\) is lower semicontinuous.

(ii) There is a positive self-adjoint \(S\) with \(\langle S\xi,\xi\rangle=q(\xi)\) for every \(\xi\in D\).

If they hold, the form \(q|_{D_q}\) is closable, and the positive self-adjoint operator \(T\) of its closure has these
properties:

(a) \(\langle T\xi,\xi\rangle=q(\xi)\) for every \(\xi\in D\), and \(D_q\) is a core for \(T^{1/2}\);

(b) if \(p\) is a positive form on \(H\), lower semicontinuous and equal to \(q\) on \(D_q\), then \(p(\zeta)\le\langle
T\zeta,\zeta\rangle\) for all \(\zeta\in H\). In particular, among the positive self-adjoint operators \(S\) with
\(\|S^{1/2}\xi\|^2=q(\xi)\) for all \(\xi\in D_q\), \(T\) is the largest.

*Proof.* (ii)\(\Rightarrow\)(i) is Lemma 2.2. Assume (i). *Closability:* let \(\xi_n\in D_q\), \(\xi_n\to0\), with
\(q(\xi_n-\xi_m)\to0\). Given \(\varepsilon>0\) pick \(m\) with \(q(\xi_n-\xi_m)<\varepsilon\) for \(n\ge m\). As
\(n\to\infty\), \(\xi_n-\xi_m\to-\xi_m\) inside \(D\), so \(q(\xi_m)\le\liminf_nq(\xi_n-\xi_m)\le\varepsilon\). Hence
\(q(\xi_m)\to0\), which is closability. Let \(\bar q\) be the closure and \(T\) its operator (B1)(i); by construction
\(D_q\) is a core for \(T^{1/2}\) and \(\langle T\xi,\xi\rangle=q(\xi)\) on \(D_q\).

(a) Let \(\xi\in D\setminus D_q\) and suppose \(\xi\in\operatorname{dom}T^{1/2}\). There are \(\xi_n\in D_q\),
\(\xi_n\to\xi\), with \(q(\xi_n)\to\|T^{1/2}\xi\|^2<\infty\), and lower semicontinuity gives \(q(\xi)<\infty\), a
contradiction. So \(\langle T\xi,\xi\rangle=\infty=q(\xi)\). This proves (a), hence (ii) with \(S=T\).

(b) If \(\zeta\notin\operatorname{dom}T^{1/2}\) there is nothing to prove. Otherwise pick \(\xi_n\in D_q\) converging
to \(\zeta\) for the graph norm of \(T^{1/2}\); then \(p(\zeta)\le\liminf p(\xi_n)=\lim q(\xi_n)=\langle
T\zeta,\zeta\rangle\). For the last claim apply this to \(p(\zeta)=\langle S\zeta,\zeta\rangle\), which is lower
semicontinuous by Lemma 2.2. \(\square\)

The next lemma produces cores from invariance under imaginary powers.

**Lemma 2.4.** Let \(S\) be positive, self-adjoint and nonsingular, and let \(D_0\subset\operatorname{dom}S^{1/2}\) be
a subspace, dense in \(H\), with \(S^{it}D_0\subset D_0\) for all \(t\). Then \(D_0\) is a core for \(S^{1/2}\).

*Proof.* Let \(\zeta\in\operatorname{dom}S^{1/2}\) be orthogonal to \(D_0\) for the graph inner product
\(\langle\zeta,\xi\rangle_1=\langle(1+S)^{1/2}\zeta,(1+S)^{1/2}\xi\rangle\). Fix \(\xi\in D_0\), let \(E\) be the
spectral measure of \(S\), and let \(\nu\) be the finite complex measure \(\nu(B)=\langle E(B)(1+S)^{1/2}\xi,
(1+S)^{1/2}\zeta\rangle\) on \((0,\infty)\) (\(E(\{0\})=0\) since \(S\) is nonsingular). Then
\(0=\langle S^{it}\xi,\zeta\rangle_1=\int\lambda^{it}d\nu(\lambda)\) for all \(t\). The image of \(\nu\) under
\(\lambda\mapsto\log\lambda\) is a finite measure on \(\mathbb R\) with vanishing Fourier transform, hence zero; so
\(\nu=0\), and \(\langle\xi,\zeta\rangle=\int(1+\lambda)^{-1}d\nu(\lambda)=0\). As \(D_0\) is dense in \(H\),
\(\zeta=0\). \(\square\)

## 3. Definition of the spatial derivative

From now on \(M\) is a von Neumann algebra on \(H\), \(N=M'\), and \(\psi\) is an fns weight on \(N\). We write
\(D=D(H,\psi)\), \(\theta=\theta^\psi\) and \(R=R^\psi\) when \(\psi\) is fixed. Since \(M=\mathcal L_N(H)\), Section 1
applies: \(D\) is dense and \(M\)-invariant, and \(\theta(\xi,\xi)\in M_+\). The situation is symmetric: \(N\) is a von
Neumann algebra on \(H\) with commutant \(M\), and every statement below has a mirror image with \((M,\varphi)\) and
\((N,\psi)\) exchanged.

**Lemma 3.1.** Let \(\varphi\) be a normal weight on \(M\) and put \(q_\varphi(\xi)=\varphi(\theta(\xi,\xi))\) for
\(\xi\in D\). Then \(q_\varphi\) is a positive form on \(D\), and it is lower semicontinuous. If \(\varphi\) is
semifinite, its domain is dense in \(H\).

*Proof.* Homogeneity and the parallelogram law follow from Lemma 1.2(d) and the additivity of \(\varphi\). By (B2)(i)
and (B2)(ii), \(\varphi=\sum_j\langle\cdot\,\zeta_j,\zeta_j\rangle\) for some family \((\zeta_j)\) in \(H\), and by
(1.2)
\[
q_\varphi(\xi)=\sum_j\sup\{|\langle y\xi,\zeta_j\rangle|^2:\ y\in\mathfrak n_\psi,\ \psi(y^*y)\le1\}.
\]
Each supremum of continuous functions of \(\xi\) is lower semicontinuous, and so is a sum of nonnegative lower
semicontinuous functions.

Let \(\varphi\) be semifinite, \(a\in\mathfrak n_\varphi^*\) and \(\xi\in D\). Then \(a\xi\in D\) and
\(\theta(a\xi,a\xi)=a\theta(\xi,\xi)a^*\le\|\theta(\xi,\xi)\|aa^*\), so \(q_\varphi(a\xi)<\infty\). By (B2)(iv) there
are contractions \(a_i\in\mathfrak n_\varphi^*\) with \(a_i\to1\) strongly, so \(a_i\xi\to\xi\); since \(D\) is dense,
so is \(D_{q_\varphi}\). \(\square\)

**Definition 3.2.** Let \(\varphi\) be a normal semifinite weight on \(M\). Its *spatial derivative*
\(d\varphi/d\psi\) with respect to \(\psi\) is the operator \(T\) that Proposition 2.3 attaches to the form
\(q_\varphi\) of Lemma 3.1; it is positive and self-adjoint.

By Proposition 2.3, \(T=d\varphi/d\psi\) is characterized by either of the following.

- \(\langle T\xi,\xi\rangle=\varphi(\theta(\xi,\xi))\) for all \(\xi\in D\) (values in \([0,\infty]\)), and
  \(D\cap\operatorname{dom}T^{1/2}\) is a core for \(T^{1/2}\).
- Among the positive self-adjoint operators \(S\) with \(\|S^{1/2}\xi\|^2=\varphi(\theta(\xi,\xi))\) whenever
  \(\xi\in D\) and the right side is finite, \(T\) is the largest.

If \(\varphi(1)<\infty\), then \(\varphi(\theta(\xi,\xi))\le\varphi(1)\|\theta(\xi,\xi)\|<\infty\), so \(D\subset
\operatorname{dom}T^{1/2}\) and \(D\) is a core. Clearly \(d(\lambda\varphi)/d\psi=\lambda\,d\varphi/d\psi\) for
\(\lambda>0\). Additivity in \(\varphi\) is Theorem 7.1(d).

**Proposition 3.3 (recovering the weight).** Let \(\varphi\) be a normal semifinite weight on \(M\),
\(T=d\varphi/d\psi\), and \((\xi_\alpha)\) a \(\psi\)-basis of \(H\). For every \(x\in M_+\),
\[
\varphi(x)=\sum_\alpha\langle Tx^{1/2}\xi_\alpha,x^{1/2}\xi_\alpha\rangle. \tag{3.1}
\]
In particular \(\varphi(1)=\sum_\alpha\langle T\xi_\alpha,\xi_\alpha\rangle\), and \(\varphi\) is determined by
\(d\varphi/d\psi\).

*Proof.* Take the projections \(e_F\) from the proof of Proposition 1.5(b); then \(x^{1/2}e_Fx^{1/2}\) increases
to \(x\). By normality
and Lemma 1.2(a),
\[
\varphi(x)=\sup_F\sum_{\alpha\in F}\varphi\big(\theta(x^{1/2}\xi_\alpha,x^{1/2}\xi_\alpha)\big)=
\sum_\alpha\langle Tx^{1/2}\xi_\alpha,x^{1/2}\xi_\alpha\rangle.\qquad\square
\]

**Proposition 3.4.** Let \(\varphi,\varphi_1,\varphi_2\) be normal semifinite weights on \(M\).

(a) \(\varphi_1\le\varphi_2\) iff \(d\varphi_1/d\psi\le d\varphi_2/d\psi\).

(b) For every invertible \(a\in M\), with \((a\varphi a^*)(x)=\varphi(a^*xa)\),
\[
\frac{d(a\varphi a^*)}{d\psi}=a\,\frac{d\varphi}{d\psi}\,a^*,
\]
where \(aTa^*\) denotes the positive self-adjoint operator \((T^{1/2}a^*)^*(T^{1/2}a^*)\).

*Proof.* (a) Let \(T_j=d\varphi_j/d\psi\). If \(\varphi_1\le\varphi_2\), the lower semicontinuous form
\(\zeta\mapsto\langle T_1\zeta,\zeta\rangle\) is \(\le\langle T_2\zeta,\zeta\rangle\) on \(D_{q_{\varphi_2}}\), which
is a core for \(T_2^{1/2}\). For \(\zeta\in\operatorname{dom}T_2^{1/2}\) take \(\xi_n\in D_{q_{\varphi_2}}\) converging
to \(\zeta\) in the graph norm; then \(\langle T_1\zeta,\zeta\rangle\le\liminf\langle T_1\xi_n,\xi_n\rangle\le
\lim\langle T_2\xi_n,\xi_n\rangle=\langle T_2\zeta,\zeta\rangle\). Conversely, if \(T_1\le T_2\), then (3.1) gives
\(\varphi_1(x)\le\varphi_2(x)\) for all \(x\in M_+\).

(b) The weight \(a\varphi a^*\) is normal, and semifinite because \(\mathfrak n_{a\varphi a^*}=\mathfrak
n_\varphi(a^*)^{-1}\). Let \(T=d\varphi/d\psi\). The operator \(T^{1/2}a^*\) is closed with dense domain
\((a^*)^{-1}\operatorname{dom}T^{1/2}\), and \(\langle aTa^*\zeta,\zeta\rangle=\langle Ta^*\zeta,a^*\zeta\rangle\). For
\(\xi\in D\), \(a^*\xi\in D\) and
\[
\langle Ta^*\xi,a^*\xi\rangle=\varphi(\theta(a^*\xi,a^*\xi))=\varphi(a^*\theta(\xi,\xi)a)=(a\varphi a^*)(\theta(\xi,
\xi)).
\]
Since \(a^*\) and \((a^*)^{-1}=(a^{-1})^*\) map \(D\) onto \(D\), the set \(D\cap\operatorname{dom}(T^{1/2}a^*)\) equals
\((a^*)^{-1}(D\cap\operatorname{dom}T^{1/2})\), and it is a core for \(T^{1/2}a^*\) because \(D\cap\operatorname{dom}
T^{1/2}\) is a core for \(T^{1/2}\) and \(a^*\) is a homeomorphism. By the first characterization after Definition
3.2, \(aTa^*=d(a\varphi a^*)/d\psi\). \(\square\)

**Example 3.5 (\(M=B(H)\)).** Here \(N=\mathbb C1\) and \(\psi(\lambda1)=c\lambda\) for some \(c>0\). The GNS space is
\(\mathbb C\) with \(\eta_\psi(\lambda)=c^{1/2}\lambda\), every vector is \(\psi\)-bounded, \(R(\xi)\mu=
c^{-1/2}\mu\xi\), and \(\theta(\xi,\xi)=c^{-1}\xi\xi^*\). For \(\varphi=\operatorname{Tr}_S\) (B6) we get
\(\varphi(\theta(\xi,\xi))=c^{-1}\langle S\xi,\xi\rangle\) for all \(\xi\in H\), so
\[
\frac{d\operatorname{Tr}_S}{d\psi}=\frac{S}{\psi(1)}.
\]
By (B6)(ii) this covers every normal semifinite weight on \(B(H)\).

**Example 3.6 (\(M=\mathbb C1\)).** Here \(N=B(H)\). Let \(K\) be positive, self-adjoint and nonsingular, and
\(\psi=\operatorname{Tr}_K\). Writing \(y^*y=\sum_j(y^*\varepsilon_j)(y^*\varepsilon_j)^*\) for an orthonormal basis
\((\varepsilon_j)\), (B6)(i) gives \(\psi(y^*y)=\sum_j\|K^{1/2}y^*\varepsilon_j\|^2=\|K^{1/2}y^*\|_2^2\), the square of
a Hilbert–Schmidt norm (\(+\infty\) unless \(K^{1/2}y^*\) is everywhere defined and Hilbert–Schmidt: if the sum is
finite, the closed operator \(K^{1/2}y^*\) is bounded on the span of the \(\varepsilon_j\), so it contains the bounded
closure of that restriction and is everywhere defined). We claim
\[
D(H,\psi)=\operatorname{dom}K^{-1/2},\qquad\theta(\xi,\xi)=\|K^{-1/2}\xi\|^2\,1. \tag{3.2}
\]
If \(\xi=K^{1/2}\xi'\) and \(y\in\mathfrak n_\psi\), then for unit \(\omega\), \(|\langle y\xi,\omega\rangle|=|\langle
\xi',K^{1/2}y^*\omega\rangle|\le\|\xi'\|\,\|K^{1/2}y^*\|_2\), so \(\xi\) is \(\psi\)-bounded. Conversely, if \(\xi\in
D(H,\psi)\), take \(y=\varepsilon\omega^*\) with \(\varepsilon\) a unit vector and \(\omega\in\operatorname{dom}
K^{1/2}\): then \(\|K^{1/2}y^*\|_2=\|K^{1/2}\omega\|\) and \(y\xi=\langle\xi,\omega\rangle\varepsilon\), so
\(|\langle\xi,\omega\rangle|\le C\|K^{1/2}\omega\|\). So the functional \(K^{1/2}\omega\mapsto\langle\omega,\xi\rangle\)
is bounded on the dense range of \(K^{1/2}\),
so there is \(\xi''\) with \(\langle\omega,\xi\rangle=\langle K^{1/2}\omega,\xi''\rangle\), which means
\(\xi''\in\operatorname{dom}K^{1/2}\) and \(K^{1/2}\xi''=\xi\). For \(\theta\), use (1.2): the estimate above gives
\(|\langle y\xi,\omega\rangle|^2\le\|\xi'\|^2\|\omega\|^2\) when \(\psi(y^*y)\le1\), and \(y^*=\zeta\omega^*/\|\omega\|\)
with \(\zeta\in\operatorname{dom}K^{1/2}\), \(\|K^{1/2}\zeta\|\le1\), gives \(|\langle y\xi,\omega\rangle|=|\langle\xi',
K^{1/2}\zeta\rangle|\,\|\omega\|\), whose supremum is \(\|\xi'\|\,\|\omega\|\). This proves (3.2). For
\(\varphi(\lambda1)=\mu\lambda\) with \(\mu>0\), the form \(\mu\|K^{-1/2}\xi\|^2\) on \(\operatorname{dom}K^{-1/2}\) is
closed, so
\[
\frac{d\varphi}{d\psi}=\mu K^{-1}.
\]
Here \(\sigma^\psi_t=\operatorname{Ad}K^{it}\), and \((\mu K^{-1})^{it}y(\mu K^{-1})^{-it}=\sigma^\psi_{-t}(y)\), in
accordance with Theorem 4.3 below.

**Example 3.7 (the abelian case).** Let \(\mu\) be a \(\sigma\)-finite measure on \(X\) and let \(M=N=L^\infty(X,\mu)\)
act on \(L^2(X,\mu)\) by multiplication. Let \(\psi(y)=\int yg\,d\mu\) and \(\varphi(x)=\int xh\,d\mu\) with \(0<g<\infty\)
and \(0\le h<\infty\) measurable; these are an fns and a normal semifinite weight. Then
\[
D=\{\xi:|\xi|^2\le C g\text{ a.e. for some }C\},\qquad\theta(\xi,\xi)=\frac{|\xi|^2}{g},\qquad
\frac{d\varphi}{d\psi}=\frac hg.
\]
If \(|\xi|^2\le Cg\) then \(\|y\xi\|^2=\int|y|^2|\xi|^2\le C\int|y|^2g\). Conversely, taking \(y=1_A\) with
\(\int_Ag\,d\mu<\infty\) in (1.1) gives \(\int_A|\xi|^2\le C^2\int_Ag\), and since the measure \(g\,d\mu\) is
\(\sigma\)-finite, \(|\xi|^2\le C^2g\) a.e. By the Cauchy–Schwarz inequality, \(|\int y\xi\bar\omega|^2\le\int|y|^2g\cdot
\int|\xi|^2|\omega|^2/g\), with near equality for \(y=\bar\xi\omega g^{-1}1_A\), \(A=\{|\omega|\le n,\ g\ge1/n\}\), \(n\)
large; so (1.2) gives \(\theta(\xi,\xi)=|\xi|^2/g\), and \(q_\varphi(\xi)=\int|\xi|^2h/g\). The form of multiplication
by \(m=h/g\) is \(\zeta\mapsto\int m|\zeta|^2\), and \(D_{q_\varphi}\) is a core for it: for \(\zeta\) in its domain,
\(\zeta1_{\{|\zeta|^2\le ng\}}\in D_{q_\varphi}\) converges to \(\zeta\) in the graph norm by dominated convergence.
Hence \(d\varphi/d\psi=h/g\).

## 4. The spatial derivative as a corner of a modular operator

In this section \(\varphi\) is an fns weight on \(M\). We realize \(H\) inside the GNS space of one fns weight, on a
larger algebra, that contains both \(\varphi\) and \(\psi\).

**Setup 4.1.** Let \(H^\sharp=H\oplus H_\psi\), an \(N\)-module with the diagonal action, and let \(P=\mathcal
L_N(H^\sharp)\). Let \(f,e\in P\) be the projections onto \(H\) and \(H_\psi\). In matrix form,
\[
fPf=M,\qquad ePe=\mathcal L_N(H_\psi)=N',\qquad fPe=\operatorname{Hom}_N(H_\psi,H).
\]
Let \(\Theta=\varphi\oplus\psi'\), that is \(\Theta(x)=\varphi(fxf)+\psi'(exe)\) for \(x\in P_+\), with \(\psi'\) as in
(B4). By (B3)(iv), \(\Theta\) is an fns weight on \(P\), \(\sigma^\Theta_t\) fixes \(f\) and \(e\), and
\(\sigma^\Theta_t\) restricts to \(\sigma^\varphi_t\) on \(M\) and to \(\sigma^{\psi'}_t=\operatorname{Ad}
\Delta_\psi^{-it}\) on \(N'\). Let \((H_\Theta,\eta_\Theta)\) be the GNS construction of \(\Theta\) and
\(\Delta_\Theta\) its modular operator.

**Lemma 4.2.** (a) \(R=R^\psi\) is a linear bijection of \(D=D(H,\psi)\) onto \(fPe\cap\mathfrak n_\Theta\), and
\(\Theta(R(\eta)^*R(\xi))=\langle\xi,\eta\rangle\).

(b) There is an isometry \(W:H\to H_\Theta\) with \(W\xi=\eta_\Theta(R(\xi))\) for \(\xi\in D\). Its range
\(\mathcal K\) is the closure of \(\eta_\Theta(fPe\cap\mathfrak n_\Theta)\) and reduces \(\Delta_\Theta\).

(c) \(S=W^*\Delta_\Theta W\) is a positive, self-adjoint, nonsingular operator on \(H\). Its imaginary powers
\(U_t=S^{it}\) satisfy \(U_tD=D\) and
\[
R(U_t\xi)=\sigma^\Theta_t(R(\xi))\qquad(\xi\in D,\ t\in\mathbb R). \tag{4.1}
\]

*Proof.* (a) For \(b\in fPe\), \(b^*b\in ePe\), so \(\Theta(b^*b)=\psi'(b^*b)\). Lemma 1.4 gives both the bijection
and the formula.

(b) By (a), \(\xi\mapsto\eta_\Theta(R(\xi))\) is a linear isometry on the dense subspace \(D\) (Proposition 1.3), and
extends to an isometry \(W\) whose range is the closure of \(\eta_\Theta(fPe\cap\mathfrak n_\Theta)\). Since
\(\sigma^\Theta_t\) fixes \(f,e\) and preserves \(\mathfrak n_\Theta\), and \(\Delta_\Theta^{it}\eta_\Theta(b)=
\eta_\Theta(\sigma^\Theta_t(b))\) (B3)(i), \(\mathcal K\) is invariant under all \(\Delta_\Theta^{it}\), hence reduces
\(\Delta_\Theta\) (B1)(iii).

(c) \(S\) is unitarily equivalent to the restriction of \(\Delta_\Theta\) to \(\mathcal K\), which is positive,
self-adjoint and nonsingular; and \(WS^{it}=\Delta_\Theta^{it}W\). For \(\xi\in D\), \(\sigma^\Theta_t(R(\xi))\in
fPe\cap\mathfrak n_\Theta\), so by (a) it equals \(R(\xi')\) for some \(\xi'\in D\), and
\(WS^{it}\xi=\eta_\Theta(\sigma^\Theta_t(R(\xi)))=W\xi'\). As \(W\) is injective, \(S^{it}\xi=\xi'\in D\), which is
(4.1); and \(S^{-it}\) maps \(D\) into \(D\) as well. \(\square\)

**Theorem 4.3.** Let \(\varphi\) be an fns weight on \(M\) and \(T=d\varphi/d\psi\). Then \(T=W^*\Delta_\Theta W\) with
\(W,\Theta\) as above. In particular \(T\) is nonsingular, \(T^{it}D=D\), \(R(T^{it}\xi)=\sigma^\Theta_t(R(\xi))\)
for \(\xi\in D\), and for all \(t\in\mathbb R\):
\[
T^{it}xT^{-it}=\sigma^\varphi_t(x)\quad(x\in M),\qquad T^{it}yT^{-it}=\sigma^\psi_{-t}(y)\quad(y\in N). \tag{4.2}
\]

*Proof.* Let \(S=W^*\Delta_\Theta W\).

*Step 1: \(\langle S\xi,\xi\rangle=\varphi(\theta(\xi,\xi))\) for \(\xi\in D\).* Since \(\mathcal K\) reduces
\(\Delta_\Theta\), \(\langle S\xi,\xi\rangle=\langle\Delta_\Theta W\xi,W\xi\rangle\) in the extended sense. Apply
(B3)(ii) to \(\Theta\) and \(R(\xi)\in\mathfrak n_\Theta\): if \(R(\xi)^*\in\mathfrak n_\Theta\), then
\(\|\Delta_\Theta^{1/2}\eta_\Theta(R(\xi))\|^2=\Theta(R(\xi)R(\xi)^*)\); if not, both sides are \(+\infty\). Finally
\(R(\xi)R(\xi)^*=\theta(\xi,\xi)\in fPf=M\), where \(\Theta=\varphi\).

*Step 2: \(S=T\).* By Step 1, \(D\cap\operatorname{dom}S^{1/2}=D_{q_\varphi}\), which is dense (Lemma 3.1) and invariant
under \(S^{it}\) (Lemma 4.2(c)). By Lemma 2.4 it is a core for \(S^{1/2}\). So the closed form of \(S\) is the closure
of \(q_\varphi|_{D_{q_\varphi}}\), that is \(S=T\).

*Step 3: the first formula in (4.2).* For \(x\in M\) and \(\xi\in D\), \(Wx\xi=\eta_\Theta(xR(\xi))=
\pi_\Theta(x)W\xi\). Hence \(WxW^*\) is the restriction of \(\pi_\Theta(x)\) to \(\mathcal K\), and
\[
T^{it}xT^{-it}=W^*\Delta_\Theta^{it}\pi_\Theta(x)\Delta_\Theta^{-it}W=W^*\pi_\Theta(\sigma^\Theta_t(x))W=
\sigma^\varphi_t(x).
\]

*Step 4: the second formula in (4.2).* Let \(y\in N_0\) be entire for \(\sigma^\psi\) and \(\xi\in D\). By Lemma
1.2(e), \(R(y\xi)=R(\xi)\rho_\psi(y)\) with \(\rho_\psi(y)\in N'=ePe\). By (B4)(i) and (B3)(i), for \(z\in\mathfrak
n_\psi\),
\[
\Delta_\psi^{-it}\rho_\psi(y)\Delta_\psi^{it}\eta_\psi(z)=\Delta_\psi^{-it}\eta_\psi(\sigma^\psi_t(z)y)=
\eta_\psi(z\sigma^\psi_{-t}(y))=\rho_\psi(\sigma^\psi_{-t}(y))\eta_\psi(z),
\]
so \(\sigma^\Theta_t(\rho_\psi(y))=\sigma^{\psi'}_t(\rho_\psi(y))=\rho_\psi(\sigma^\psi_{-t}(y))\). Using (4.1) twice,
\[
R(T^{it}y\xi)=\sigma^\Theta_t(R(\xi)\rho_\psi(y))=R(T^{it}\xi)\rho_\psi(\sigma^\psi_{-t}(y))=
R(\sigma^\psi_{-t}(y)T^{it}\xi).
\]
By Lemma 1.2(b), \(T^{it}y\xi=\sigma^\psi_{-t}(y)T^{it}\xi\) on the dense set \(D\), so \(T^{it}yT^{-it}=
\sigma^\psi_{-t}(y)\) for \(y\in N_0\). Both sides are \(\sigma\)-weakly continuous in \(y\) and \(N_0\) is
\(\sigma\)-weakly dense, so (4.2) holds for all \(y\in N\). \(\square\)

So \(d\varphi/d\psi\) is the corner, cut out by \(\mathcal K\), of the modular operator of the balanced weight
\(\varphi\oplus\psi'\). In the open courses this is the lesson "Spatial energy as a corner of a modular operator".

## 5. Corners, matrices, and the inversion formula

**Lemma 5.1 (corners and supports).** Let \(\varphi_1\) be an fns weight on \(M\) and \(e\in M\) a projection with
\(\sigma^{\varphi_1}_t(e)=e\) for all \(t\). Let \(T_1=d\varphi_1/d\psi\).

(a) \(T_1\) commutes with \(e\).

(b) \(\varphi=\varphi_1(e\,\cdot\,e)\) is a normal semifinite weight on \(M\) with support \(e\), and
\(d\varphi/d\psi=T_1e\).

(c) Every normal semifinite weight \(\varphi\) on \(M\) arises as in (b), with \(e=s(\varphi)\).

*Proof.* (a) By (4.2), \(T_1^{it}eT_1^{-it}=e\), so \(e\) commutes with all \(T_1^{it}\), hence with \(T_1\).

(b) By (B3)(iv) the restriction of \(\varphi_1\) to \(eMe\) is fns, and \(\varphi\) vanishes on \((1-e)M_+(1-e)\), so
\(\varphi\) is normal with support \(e\). It is semifinite: \(\mathfrak n_\varphi\) is a left ideal containing
\(\mathfrak n_{\varphi_1}\cap eMe\), which contains contractions converging strongly to \(e\) (B2)(iv), and it
contains \(1-e\); so its \(\sigma\)-weak closure contains \(x=\lim x(a_i+1-e)\) for all \(x\in M\).

For \(\xi\in D\) we have \(e\xi\in D\), \(e\theta(\xi,\xi)e=\theta(e\xi,e\xi)\) and \(\varphi_1(e\,\cdot\,e)=
\varphi\), hence
\[
q_\varphi(\xi)=\varphi_1(\theta(e\xi,e\xi))=\langle T_1e\xi,e\xi\rangle.
\]
The form \(p(\zeta)=\langle T_1e\zeta,e\zeta\rangle\) is lower semicontinuous and equals \(q_\varphi\) on \(D\), so
\(p\le\langle(d\varphi/d\psi)\zeta,\zeta\rangle\) by Proposition 2.3(b). Conversely let \(p(\zeta)<\infty\). Since
\(D_{q_{\varphi_1}}\) is a core for \(T_1^{1/2}\) there are \(\xi_n\in D_{q_{\varphi_1}}\) with \(\xi_n\to e\zeta\) and
\(T_1^{1/2}\xi_n\to T_1^{1/2}e\zeta\). Then \(e\xi_n\in D\), \(e\xi_n\to e\zeta\) and \(T_1^{1/2}e\xi_n=
eT_1^{1/2}\xi_n\to T_1^{1/2}e\zeta\). Choose \(d_n\in D\) with \(d_n\to\zeta\) and put \(\xi_n'=e\xi_n+(1-e)d_n\in D\).
Then \(\xi_n'\to\zeta\) and \(q_\varphi(\xi_n')=\|T_1^{1/2}e\xi_n\|^2\to p(\zeta)\), the sequence \((\xi_n')\) is Cauchy for \(q_\varphi\) (as \(q_\varphi(\xi_n'-\xi_m')=\|T_1^{1/2}e(\xi_n-\xi_m)\|^2\)), and so, by the construction of the
closure, \(\langle(d\varphi/d\psi)\zeta,\zeta\rangle\le p(\zeta)\). Hence \(d\varphi/d\psi\) and \(T_1e\) have the same
form and are equal.

(c) Let \(e=s(\varphi)\). By (B2)(iii), \(\varphi(x)=\varphi(exe)\) and \(\varphi|_{eMe}\) is fns. Choose an fns weight
\(\chi\) on \((1-e)M(1-e)\) (B2)(v) and put \(\varphi_1=\varphi|_{eMe}\oplus\chi\). By (B3)(iv) it is fns with
\(\sigma^{\varphi_1}_t(e)=e\), and \(\varphi_1(e\,\cdot\,e)=\varphi\). \(\square\)

**Corollary 5.2.** Let \(\varphi\) be a normal semifinite weight on \(M\), \(e=s(\varphi)\) and \(T=d\varphi/d\psi\).
Then \(s(T)=e\); in particular \(T\) is nonsingular iff \(\varphi\) is faithful. Moreover, for all \(t\),
\[
T^{it}y=\sigma^\psi_{-t}(y)T^{it}\quad(y\in N),\qquad T^{it}xT^{-it}=\sigma^{\varphi_e}_t(x)\quad(x\in eMe),
\]
where \(\varphi_e\) is the restriction of \(\varphi\) to \(eMe\).

*Proof.* Write \(\varphi=\varphi_1(e\,\cdot\,e)\) as in Lemma 5.1(c). Then \(T=T_1e\) with \(T_1\) nonsingular and
commuting with \(e\), so \(s(T)=e\) and \(T^{it}=T_1^{it}e\). Since \(e\in M\) commutes with \(N\), (4.2) gives
\(T^{it}y=T_1^{it}ye=\sigma^\psi_{-t}(y)T_1^{it}e\). For \(x\in eMe\), \(T^{it}xT^{-it}=\sigma^{\varphi_1}_t(x)=
\sigma^{\varphi_e}_t(x)\) by (B3)(iv). \(\square\)

**Lemma 5.3 (direct sums).** Let \(f\in M\) be a projection such that \(f\) and \(1-f\) both have central support
\(1\), so that \(y\mapsto yf\) and \(y\mapsto y(1-f)\) are isomorphisms of \(N\) onto the commutants of \(fMf\) on
\(fH\) and of \((1-f)M(1-f)\) on \((1-f)H\); through them we view \(\psi\) as a weight on these commutants. Let
\(\varphi_1,\varphi_2\) be fns weights on \(fMf\) and \((1-f)M(1-f)\), and \(\varphi=\varphi_1\oplus\varphi_2\). Then
\[
\text{(a)}\quad\frac{d\varphi}{d\psi}=\frac{d\varphi_1}{d\psi}\oplus\frac{d\varphi_2}{d\psi},\qquad\qquad
\text{(b)}\quad\frac{d\psi}{d\varphi}=\frac{d\psi}{d\varphi_1}\oplus\frac{d\psi}{d\varphi_2},
\]
with respect to \(H=fH\oplus(1-f)H\).

*Proof.* Write \(f_1=f\), \(f_2=1-f\), \(H_j=f_jH\).

(a) A vector \(\xi\in H_j\) is \(\psi\)-bounded in \(H_j\) iff it is so in \(H\), with the same \(R^\psi(\xi)\). Since
\(f_j\in M\), \(D=D(H_1,\psi)\oplus D(H_2,\psi)\). For \(\xi=\xi_1+\xi_2\) in \(D\), \(R(\xi)=R(\xi_1)+R(\xi_2)\) and
\(f_j\theta(\xi,\xi)f_j=\theta(\xi_j,\xi_j)\), so
\[
q_\varphi(\xi)=\varphi_1(\theta(\xi_1,\xi_1))+\varphi_2(\theta(\xi_2,\xi_2)).
\]
The closure of a direct sum of closable forms on \(D(H_1,\psi)\oplus D(H_2,\psi)\) is the direct sum of the closures.

(b) Here \(\varphi\) is the reference weight on the commutant of \(N\). *First, \(D(H,\varphi)=D(H_1,\varphi_1)\oplus
D(H_2,\varphi_2)\).* Let \(\zeta_j\in D(H_j,\varphi_j)\) with constants \(C_j\) and let \(x\in\mathfrak n_\varphi\).
The element \(|xf_j|=(f_jx^*xf_j)^{1/2}\) lies in \(f_jMf_j\) with \(\varphi_j(|xf_j|^2)=\varphi(f_jx^*xf_j)\le
\varphi(x^*x)\), since \(\varphi\) is balanced. Hence
\[
\|x(\zeta_1+\zeta_2)\|\le\sum_j\||xf_j|\zeta_j\|\le\sum_jC_j\varphi_j(|xf_j|^2)^{1/2}\le(C_1+C_2)\varphi(x^*x)^{1/2}.
\]
Conversely, if \(\zeta\in D(H,\varphi)\) with constant \(C\), then for \(x\in\mathfrak n_\varphi\),
\(\|xf_j\zeta\|\le C\varphi(f_jx^*xf_j)^{1/2}\le C\varphi(x^*x)^{1/2}\), so \(f_j\zeta\in D(H,\varphi)\), and taking
\(x=a\in\mathfrak n_{\varphi_j}\subset f_jMf_j\) shows \(f_j\zeta\in D(H_j,\varphi_j)\).

*Second, \(\theta^\varphi(\zeta,\zeta)=\theta^{\varphi_1}(\zeta_1,\zeta_1)+\theta^{\varphi_2}(\zeta_2,\zeta_2)\) as
elements of \(N\).* For \(x\in\mathfrak n_\varphi\) the vectors \(\eta_\varphi(xf_1)\), \(\eta_\varphi(xf_2)\) are
orthogonal, because \(\varphi(f_1x^*xf_2)=0\) for a balanced weight. Since \(R^\varphi(\zeta_j)\eta_\varphi(x)=
xf_j\zeta_j\) depends only on \(\eta_\varphi(xf_j)\), the operators \(R^\varphi(\zeta_1)\), \(R^\varphi(\zeta_2)\) have
orthogonal initial supports; so \(R^\varphi(\zeta_1)R^\varphi(\zeta_2)^*=0\) and \(\theta^\varphi(\zeta,\zeta)=
\theta^\varphi(\zeta_1,\zeta_1)+\theta^\varphi(\zeta_2,\zeta_2)\). Now compare \(y=\theta^\varphi(\zeta_1,\zeta_1)\)
(computed in \(H\)) with \(y'=\theta^{\varphi_1}(\zeta_1,\zeta_1)\) (computed in \(H_1\)); both lie in \(N\). For
\(\omega\in H_1\) and \(x\in\mathfrak n_\varphi\) we have \(\langle x\zeta_1,\omega\rangle=\langle f_1xf_1\zeta_1,
\omega\rangle\) and \(\varphi_1((f_1xf_1)^*(f_1xf_1))\le\varphi(f_1x^*xf_1)\le\varphi(x^*x)\), while every \(a\in
\mathfrak n_{\varphi_1}\) is an admissible \(x\). By (1.2), \(\langle y\omega,\omega\rangle=\langle y'\omega,
\omega\rangle\) for \(\omega\in H_1\), that is \(yf_1=y'f_1\), and \(y=y'\) because \(f_1\) has central support \(1\).
The same holds for \(\zeta_2\).

Hence \(\psi(\theta^\varphi(\zeta,\zeta))=\psi(\theta^{\varphi_1}(\zeta_1,\zeta_1))+\psi(\theta^{\varphi_2}(\zeta_2,
\zeta_2))\) on \(D(H,\varphi)=D(H_1,\varphi_1)\oplus D(H_2,\varphi_2)\), and we conclude as in (a). \(\square\)

**Theorem 5.4 (chain rules).** Let \(\varphi,\varphi_1,\varphi_2\) be fns weights on \(M\) and \(\psi,\psi_1,\psi_2\)
fns weights on \(N\). For all \(t\in\mathbb R\):
\[
\text{(a)}\quad\Big(\frac{d\varphi_2}{d\psi}\Big)^{it}=(D\varphi_2:D\varphi_1)_t\Big(\frac{d\varphi_1}{d\psi}
\Big)^{it},\qquad
\text{(b)}\quad\Big(\frac{d\varphi}{d\psi_2}\Big)^{it}=(D\psi_2:D\psi_1)_{-t}\Big(\frac{d\varphi}{d\psi_1}\Big)^{it}.
\]

*Proof.* (a) Let \(M\otimes M_2(\mathbb C)\) act on \(H\otimes\mathbb C^2=H\oplus H\); its commutant is \(N\otimes1\cong
N\), and \(f=1\otimes e_{11}\) and \(1-f\) have central support \(1\). Let \(\Phi=\varphi_1\oplus\varphi_2\). By Lemma
5.3(a), \(d\Phi/d\psi=T_1\oplus T_2\) with \(T_j=d\varphi_j/d\psi\). By (4.2) and (B5),
\[
T_2^{it}T_1^{-it}\otimes e_{21}=(T_1\oplus T_2)^{it}(1\otimes e_{21})(T_1\oplus T_2)^{-it}=\sigma^\Phi_t(1\otimes
e_{21})=(D\varphi_2:D\varphi_1)_t\otimes e_{21}.
\]
(b) Now let \(N\otimes M_2(\mathbb C)\) act on \(H\oplus H\), with commutant \(M\otimes1\cong M\) and fns weight
\(\Psi=\psi_1\oplus\psi_2\). Lemma 5.3(b), with the roles of the two algebras exchanged, gives \(d\varphi/d\Psi=
S_1\oplus S_2\) with \(S_j=d\varphi/d\psi_j\). The second formula in (4.2) gives
\[
S_2^{it}S_1^{-it}\otimes e_{21}=\sigma^\Psi_{-t}(1\otimes e_{21})=(D\psi_2:D\psi_1)_{-t}\otimes e_{21}.\qquad\square
\]

**Proposition 5.5 (the standard case).** Let \(H=H_\psi\), so that \(M=N'\), and let \(\psi'\) be the commutant weight
(B4). Then
\[
\frac{d\psi'}{d\psi}=\Delta_\psi^{-1},\qquad\frac{d\psi}{d\psi'}=\Delta_\psi.
\]

*Proof.* By definition \(D(H_\psi,\psi)\) consists of the right-bounded vectors, and \(\theta^\psi(\xi,\xi)=
R(\xi)R(\xi)^*\). Realize the GNS construction of \(\psi'\) on \(H_\psi\) by \(\eta_{\psi'}(R(\xi))=\xi\), with
\(\Delta_{\psi'}=\Delta_\psi^{-1}\) (B4)(i). By (B3)(ii) for \(\psi'\), \(\psi'(R(\xi)R(\xi)^*)=\langle\Delta_\psi^{-1}
\xi,\xi\rangle\) for all right-bounded \(\xi\), and those with finite value form a core for \(\Delta_\psi^{-1/2}\). So
\(d\psi'/d\psi=\Delta_\psi^{-1}\).

For the second formula the reference weight is \(\psi'\) on \(N'\). A vector \(\zeta\) is \(\psi'\)-bounded iff
\(\|R(\xi)\zeta\|\le C\|\xi\|\) for all right-bounded \(\xi\), that is (B4)(ii) iff \(\zeta=\eta_\psi(y)\) with
\(y\in\mathfrak n_\psi\). Then \(R^{\psi'}(\eta_\psi(y))\) maps \(\xi=\eta_{\psi'}(R(\xi))\) to \(R(\xi)\eta_\psi(y)=
y\xi\), so \(R^{\psi'}(\eta_\psi(y))=y\) and \(\theta^{\psi'}(\eta_\psi(y),\eta_\psi(y))=yy^*\). By (B3)(ii),
\(\psi(yy^*)=\langle\Delta_\psi\eta_\psi(y),\eta_\psi(y)\rangle\), and the vectors with finite value,
\(\eta_\psi(\mathfrak n_\psi\cap\mathfrak n_\psi^*)\), form a core for \(\Delta_\psi^{1/2}\). So \(d\psi/d\psi'=
\Delta_\psi\). \(\square\)

**Theorem 5.6 (inversion).** Let \(\varphi\) be an fns weight on \(M\) and \(\psi\) an fns weight on \(N\). Then
\[
\frac{d\psi}{d\varphi}=\Big(\frac{d\varphi}{d\psi}\Big)^{-1}.
\]

*Proof.* Write \(S_{\varphi,\psi}=d\varphi/d\psi\) and \(S'_{\varphi,\psi}=(d\psi/d\varphi)^{-1}\); both are positive
and nonsingular (Theorem 4.3 and its mirror image). Put \(z_t(\varphi,\psi)=S_{\varphi,\psi}^{-it}
{S'}_{\varphi,\psi}^{it}\).

*Step 1: \(z_t\) is central.* By (4.2), \(S^{it}\) implements \(\sigma^\varphi_t\) on \(M\) and \(\sigma^\psi_{-t}\) on
\(N\). The mirror image of (4.2) says that \((d\psi/d\varphi)^{is}\) implements \(\sigma^\psi_s\) on \(N\) and
\(\sigma^\varphi_{-s}\) on \(M\); with \(s=-t\), \({S'}^{it}\) implements \(\sigma^\varphi_t\) on \(M\) and
\(\sigma^\psi_{-t}\) on \(N\). So \(z_t\) commutes with \(M\) and \(N\): \(z_t\in M\cap N\), the centre.

*Step 2: \(z_t\) does not depend on \(\varphi\) or \(\psi\).* Let \(u_t=(D\varphi_2:D\varphi_1)_t\). By Theorem
5.4(a), \(S_{\varphi_2,\psi}^{it}=u_tS_{\varphi_1,\psi}^{it}\). The mirror image of Theorem 5.4(b) gives
\((d\psi/d\varphi_2)^{is}=u_{-s}(d\psi/d\varphi_1)^{is}\); with \(s=-t\) this is \({S'}^{it}_{\varphi_2,\psi}=
u_t{S'}^{it}_{\varphi_1,\psi}\). Hence
\[
z_t(\varphi_2,\psi)=S_{\varphi_1,\psi}^{-it}u_t^*u_t{S'}^{it}_{\varphi_1,\psi}=z_t(\varphi_1,\psi).
\]
Similarly let \(w_t=(D\psi_2:D\psi_1)_t\). Theorem 5.4(b) gives \(S_{\varphi,\psi_2}^{it}=w_{-t}S_{\varphi,
\psi_1}^{it}\), and the mirror image of Theorem 5.4(a) gives \((d\psi_2/d\varphi)^{is}=w_s(d\psi_1/d\varphi)^{is}\),
so \({S'}^{it}_{\varphi,\psi_2}=w_{-t}{S'}^{it}_{\varphi,\psi_1}\). Hence \(z_t(\varphi,\psi_2)=z_t(\varphi,\psi_1)\).
So \(z_t=z_t(H)\) depends only on the pair \(M,N\) acting on \(H\).

*Step 3: \(z_t(H_\psi)=1\).* In the standard case take \(\varphi=\psi'\). By Proposition 5.5, \(S=\Delta_\psi^{-1}\)
and \(S'=(\Delta_\psi)^{-1}\), so \(z_t=1\).

*Step 4: \(z_t(H)=1\).* Use Setup 4.1 with any fns \(\varphi_0\) on \(M\): \(H^\sharp=H\oplus H_\psi\),
\(P=\mathcal L_N(H^\sharp)\), \(\Theta=\varphi_0\oplus\psi'\). Since \(N\) acts faithfully on \(H\) and on \(H_\psi\),
the projections \(f\) and \(e=1-f\) have central support \(1\) in \(P\) (the centre of \(P\) is the centre of \(N\),
acting diagonally). By Lemma 5.3, \(d\Theta/d\psi=d\varphi_0/d\psi\oplus d\psi'/d\psi\) and \(d\psi/d\Theta=
d\psi/d\varphi_0\oplus d\psi/d\psi'\). Hence \(z_t(H^\sharp)=z_t(H)\oplus z_t(H_\psi)=z_t(H)\oplus1\). By Step 1,
\(z_t(H^\sharp)\) lies in the centre of \(P\), so it is \(c\oplus\pi_\psi(c)\) for some central \(c\in N\). Then
\(\pi_\psi(c)=1\) gives \(c=1\), and \(z_t(H)=c=1\).

So \(S^{it}={S'}^{it}\) for all \(t\), and \(S=S'\) (B1)(iii). \(\square\)

**Corollary 5.7.** Let \(\varphi\) be an fns weight on \(M\), \(\xi\in D(H,\psi)\) and \(\eta\in D(H,\varphi)\). Then,
with \(0\cdot\infty=0\),
\[
|\langle\xi,\eta\rangle|^2\le\varphi(\theta^\psi(\xi,\xi))\ \psi(\theta^\varphi(\eta,\eta)). \tag{5.1}
\]
Moreover, for fixed \(\xi\in D(H,\psi)\),
\[
\varphi(\theta^\psi(\xi,\xi))=\sup\{|\langle\xi,\eta\rangle|^2:\ \eta\in D(H,\varphi),\ \psi(\theta^\varphi(\eta,\eta))
\le1\}. \tag{5.2}
\]

*Proof.* Let \(T=d\varphi/d\psi\); by Theorem 5.6, \(T^{-1}=d\psi/d\varphi\). So \(\varphi(\theta^\psi(\xi,\xi))=
\langle T\xi,\xi\rangle\) and \(\psi(\theta^\varphi(\eta,\eta))=\langle T^{-1}\eta,\eta\rangle\). If both are finite,
the spectral theorem gives \(\langle\xi,\eta\rangle=\langle T^{1/2}\xi,T^{-1/2}\eta\rangle\), and (5.1) is the
Cauchy–Schwarz inequality. If one of them is \(0\), then \(\xi=0\) or \(\eta=0\), as \(T\) is nonsingular. Otherwise the
right side of (5.1) is \(+\infty\).

For (5.2), "\(\ge\)" is (5.1). Let \(\mathcal C=D(H,\varphi)\cap\operatorname{dom}T^{-1/2}\), a core for \(T^{-1/2}\) by
Definition 3.2 applied to \(d\psi/d\varphi\). The map \(T^{-1/2}\) is an isometry from \(\operatorname{dom}T^{-1/2}\)
onto \(\operatorname{dom}T^{1/2}\) for the graph norms, so \(T^{-1/2}\mathcal C\) is a core for \(T^{1/2}\). If
\(\xi\in\operatorname{dom}T^{1/2}\), then
\[
\sup_{\eta\in\mathcal C,\ \|T^{-1/2}\eta\|\le1}|\langle\xi,\eta\rangle|=\sup_{\eta\in\mathcal C,\ \|T^{-1/2}\eta\|\le1}
|\langle T^{1/2}\xi,T^{-1/2}\eta\rangle|=\|T^{1/2}\xi\|,
\]
because \(T^{-1/2}\mathcal C\) is dense in \(H\). If the supremum \(C\) is finite, then \(|\langle\xi,T^{1/2}\omega
\rangle|\le C\|\omega\|\) for \(\omega\) in the core \(T^{-1/2}\mathcal C\), hence for all
\(\omega\in\operatorname{dom}T^{1/2}\), and \(\xi\in\operatorname{dom}(T^{1/2})^*=\operatorname{dom}T^{1/2}\). So the
supremum is infinite when \(\xi\notin\operatorname{dom}T^{1/2}\). \(\square\)

## 6. Homogeneous operators of degree \(-1\)

A reference for this section is [Connes 1980a]; the monotone convergence result (Corollary 6.5) is also there.

**Definition 6.1.** Let \(H_1,H_2\) be \(N\)-modules, \(\alpha\in\mathbb R\), and \(T:H_1\to H_2\) a closed, densely
defined operator with polar decomposition \(T=u|T|\). Then \(T\) is *homogeneous of degree \(\alpha\)*
(with respect to \(\psi\)) if \(u\in\operatorname{Hom}_N(H_1,H_2)\) and
\[
|T|^{it}y=\sigma^\psi_{\alpha t}(y)\,|T|^{it}\qquad(y\in N,\ t\in\mathbb R). \tag{6.1}
\]

At \(t=0\), (6.1) says that \(s(|T|)=u^*u\) commutes with \(N\). By Remark 1.6 we may and do use the theory of Sections
3–5 for \(\mathcal L_N(H_j)\) on \(H_j\), whatever the kernel of the action. A positive self-adjoint \(T\) on \(H\) is
homogeneous of degree \(-1\) iff \(T^{it}\sigma^\psi_t(y)=yT^{it}\) for all \(y,t\).

**Theorem 6.2.** For positive self-adjoint \(T\) on \(H\), these three conditions are equivalent.

(1) \(T=d\varphi/d\psi\) for a normal semifinite weight \(\varphi\) on \(M\).

(2) \(T\) is homogeneous of degree \(-1\).

(3) \(D\cap\operatorname{dom}T^{1/2}\) is a core for \(T^{1/2}\), and for \(\xi_i,\xi'_j\in D\),
\[
\sum_{i=1}^n\theta(\xi_i,\xi_i)=\sum_{j=1}^m\theta(\xi'_j,\xi'_j)\ \Longrightarrow\ \sum_{i=1}^n\langle T\xi_i,
\xi_i\rangle=\sum_{j=1}^m\langle T\xi'_j,\xi'_j\rangle\quad\text{(in }[0,\infty]\text{)}.
\]

The weight \(\varphi\) in (1) is unique, given by (3.1), and it is faithful iff \(T\) is nonsingular.

The proof of (3)\(\Rightarrow\)(1) needs two lemmas.

**Lemma 6.3.** Let \(A_n,A\) be self-adjoint operators with \(\sup_n\|A_n\|<\infty\) and \(A_n\to A\) strongly. Then
\(g(A_n)\to g(A)\) strongly for every continuous function \(g\) on \(\mathbb R\).

*Proof.* Products of uniformly bounded strongly convergent sequences converge strongly, so \(p(A_n)\to p(A)\) for
polynomials \(p\). On a compact interval containing all spectra, approximate \(g\) uniformly by polynomials; the
errors are bounded in norm uniformly in \(n\). \(\square\)

The same holds for nets that are bounded in norm.

**Lemma 6.4 (extension to a normal weight).** Let \(\varphi_0:\mathcal J_\psi^+\to[0,\infty]\) be additive and
positively homogeneous, and assume

(L) for every bounded net \((a_i)\) in \(M\) converging strongly to \(a\in M\), and every \(y\in\mathcal J_\psi^+\),
\(\liminf_i\varphi_0(a_iya_i^*)\ge\varphi_0(aya^*)\).

Then \(\varphi(x)=\sup\{\varphi_0(y):y\in\mathcal J_\psi^+,\ y\le x\}\) is a normal weight on \(M\) extending
\(\varphi_0\).

*Proof.* If \(y'\le y\) in \(\mathcal J_\psi^+\), then \(y-y'\in\mathcal J_\psi^+\) and \(\varphi_0(y')\le\varphi_0(y)\);
so \(\varphi=\varphi_0\) on \(\mathcal J_\psi^+\). Clearly \(\varphi\) is monotone and positively homogeneous.

*Normality.* Let \(x_\beta\uparrow x\) in \(M_+\) and \(y\in\mathcal J_\psi^+\), \(y\le x\). By the factorization in the
proof of Proposition 1.5 there are contractions \(w_\beta\in M\) with \(x_\beta^{1/2}=w_\beta x^{1/2}\) and
\(w_\beta=0\) on \(\ker x\). Since \(x_\beta\to x\) strongly, Lemma 6.3 gives \(x_\beta^{1/2}\to x^{1/2}\) strongly, so
\(w_\beta\to1\) strongly on the range of \(x^{1/2}\), hence \(w_\beta\to s(x)\) strongly. Now \(w_\beta yw_\beta^*\in
\mathcal J_\psi^+\) and \(w_\beta yw_\beta^*\le w_\beta xw_\beta^*=x_\beta\), so by (L)
\[
\sup_\beta\varphi(x_\beta)\ge\liminf_\beta\varphi_0(w_\beta yw_\beta^*)\ge\varphi_0(s(x)ys(x))=\varphi_0(y),
\]
using \(s(x)ys(x)=y\) for \(0\le y\le x\). Taking the supremum over \(y\) gives \(\sup_\beta\varphi(x_\beta)=\varphi(x)\).

*Additivity.* Superadditivity is clear: if \(y_j\le x_j\) then \(y_1+y_2\le x_1+x_2\). For subadditivity let
\((\xi_\alpha)\) be a \(\psi\)-basis and \(e_F\) as in Proposition 1.5. The net \(y_F=x_1^{1/2}e_Fx_1^{1/2}+
x_2^{1/2}e_Fx_2^{1/2}\) lies in \(\mathcal J_\psi^+\) and increases to \(x_1+x_2\). By normality and additivity of
\(\varphi_0\),
\[
\varphi(x_1+x_2)=\sup_F\big(\varphi_0(x_1^{1/2}e_Fx_1^{1/2})+\varphi_0(x_2^{1/2}e_Fx_2^{1/2})\big)\le\varphi(x_1)+
\varphi(x_2).\qquad\square
\]

*Proof of Theorem 6.2.* (1)\(\Rightarrow\)(2) is Corollary 5.2.

(2)\(\Rightarrow\)(1). Let \(e=s(T)\). Taking \(t=0\) in (6.1) gives \(e\in N'=M\). Choose an fns weight \(\chi\) on
\(M\) with \(\sigma^\chi_t(e)=e\) (take \(\chi=\chi_1\oplus\chi_2\) with fns weights on \(eMe\) and \((1-e)M(1-e)\)),
and let \(T_\chi=d\chi/d\psi\). By Lemma 5.1(a), \(T_\chi\) commutes with \(e\). Let
\[
\tilde T=Te+T_\chi(1-e),
\]
a positive nonsingular operator with \(\tilde T^{it}=T^{it}+T_\chi^{it}(1-e)\). Both summands satisfy (6.1) with
\(\alpha=-1\) (for the second use (4.2) and \(1-e\in M\)), so \(\tilde T^{it}\sigma^\psi_t(y)\tilde T^{-it}=y\). Put
\(u_t=\tilde T^{it}T_\chi^{-it}\). Since \(T_\chi^{-it}y=\sigma^\psi_t(y)T_\chi^{-it}\),
\[
u_ty=\tilde T^{it}\sigma^\psi_t(y)T_\chi^{-it}=y\,u_t\qquad(y\in N),
\]
so \(u_t\) is a unitary of \(M\); \(t\mapsto u_t\) is strongly continuous, and
\(u_{s+t}=\tilde T^{is}u_tT_\chi^{-is}=u_s\,T_\chi^{is}u_tT_\chi^{-is}=u_s\sigma^\chi_s(u_t)\) by (4.2). By (B5)(ii)
there is an fns weight \(\tilde\varphi\) with \((D\tilde\varphi:D\chi)_t=u_t\), and Theorem 5.4(a) gives
\((d\tilde\varphi/d\psi)^{it}=u_tT_\chi^{it}=\tilde T^{it}\), so \(d\tilde\varphi/d\psi=\tilde T\) (B1)(iii). By
(4.2), \(\sigma^{\tilde\varphi}_t(e)=\tilde T^{it}e\tilde T^{-it}=e\). Lemma 5.1(b) applied to \(\tilde\varphi\) and
\(e\) gives a normal semifinite \(\varphi=\tilde\varphi(e\,\cdot\,e)\) with \(d\varphi/d\psi=\tilde Te=T\).

(1)\(\Rightarrow\)(3). \(D\cap\operatorname{dom}T^{1/2}=D_{q_\varphi}\) is a core, and \(\sum_i\langle T\xi_i,
\xi_i\rangle=\varphi(\sum_i\theta(\xi_i,\xi_i))\).

(3)\(\Rightarrow\)(1). By Proposition 1.5(c) and (3), \(\varphi_0(\sum_i\theta(\xi_i,\xi_i))=\sum_i\langle T\xi_i,
\xi_i\rangle\) is a well-defined map \(\mathcal J_\psi^+\to[0,\infty]\). It is additive, and positively homogeneous
because \(\lambda\theta(\xi,\xi)=\theta(\lambda^{1/2}\xi,\lambda^{1/2}\xi)\). It satisfies (L): if \(a_i\to a\)
strongly, then \(a_iya_i^*=\sum_k\theta(a_i\xi_k,a_i\xi_k)\), \(a_i\xi_k\to a\xi_k\) in norm, and Lemma 2.2 gives
\(\liminf_i\langle Ta_i\xi_k,a_i\xi_k\rangle\ge\langle Ta\xi_k,a\xi_k\rangle\). Lemma 6.4 yields a normal weight
\(\varphi\) on \(M\) with \(\varphi(\theta(\xi,\xi))=\langle T\xi,\xi\rangle\) for \(\xi\in D\).

\(\varphi\) is semifinite. For \(\xi\in D_0=D\cap\operatorname{dom}T^{1/2}\), \(\theta(\xi,\xi)^{1/2}\in\mathfrak
n_\varphi\), so the \(\sigma\)-weak closure \(Mp\) of the left ideal \(\mathfrak n_\varphi\) has \(p\) above the range
projection of \(\theta(\xi,\xi)\), which is the range projection of \(R(\xi)\) and contains \(\xi\) (Lemma 1.2(b)).
Since \(D_0\) is dense, \(p=1\).

So \(q_\varphi(\xi)=\langle T\xi,\xi\rangle\) on \(D\), and \(D_{q_\varphi}=D_0\) is a core for \(T^{1/2}\). Hence the
closure of \(q_\varphi|_{D_{q_\varphi}}\) is the form of \(T\), that is \(T=d\varphi/d\psi\).

Uniqueness follows from (3.1), and the last claim from Corollary 5.2. \(\square\)

**Corollary 6.5 (increasing sequences).** Let \(\varphi_1\le\varphi_2\le\cdots\) be fns weights on \(M\) such
that \(\varphi=\sup_n\varphi_n\) is semifinite. Let \(T_n=d\varphi_n/d\psi\) and \(T=d\varphi/d\psi\). Then
\(\langle T_n\zeta,\zeta\rangle\uparrow\langle T\zeta,\zeta\rangle\) for every \(\zeta\in H\),
\((1+T_n)^{-1}\to(1+T)^{-1}\) strongly, \(T_n^{it}\to T^{it}\) strongly, and for every \(t\):
\[
(D\varphi_n:D\varphi)_t\to1\ \ \text{strongly}^*,\qquad\sigma^{\varphi_n}_t\to\sigma^\varphi_t\ \text{ pointwise in
norm on }M_*,
\]
that is \(\|\omega\circ\sigma^{\varphi_n}_t-\omega\circ\sigma^\varphi_t\|\to0\) for every \(\omega\in M_*\).

*Proof.* \(\varphi\) is normal (a supremum of normal weights) and faithful (\(\varphi\ge\varphi_1\)). By Proposition
3.4(a), \(T_1\le T_2\le\dots\le T\), so by (B1)(ii) \(A_n=(1+T_n)^{-1}\) is a decreasing sequence of positive
contractions with \(A_n\ge(1+T)^{-1}\). It converges strongly to some \(A\) with \((1+T)^{-1}\le A\le A_n\). \(A\) is
injective since \((1+T)^{-1}\) is. If \(A\zeta=\zeta\), then \(\langle A_n\zeta,\zeta\rangle\ge\|\zeta\|^2\) forces
\(A_n\zeta=\zeta\), so \(T_n\zeta=0\) and \(\zeta=0\). Hence \(T'=A^{-1}-1\) is a positive self-adjoint nonsingular
operator with \((1+T')^{-1}=A\).

*\(T_n^{it}\to T'^{it}\) strongly.* Let \(g_t(\lambda)=((1-\lambda)/\lambda)^{it}\) for \(0<\lambda<1\), so that
\(T_n^{it}=g_t(A_n)\) and \(T'^{it}=g_t(A)\) (the spectral measures of \(A_n,A\) do not charge \(0\) or \(1\)). Fix
\(\zeta\) and \(\varepsilon>0\). Since \(A\) has no eigenvalue \(0\) or \(1\), there is \(\delta>0\) such that the
spectral projection of \(A\) for \([0,\delta]\cup[1-\delta,1]\) moves \(\zeta\) by less than \(\varepsilon\). Choose a
continuous \(h:[0,1]\to[0,1]\), equal to \(1\) on \([\delta,1-\delta]\) and to \(0\) near \(0\) and \(1\). Then
\(g_th\) is continuous on \([0,1]\), and
\[
\|g_t(A_n)\zeta-g_t(A)\zeta\|\le\|(g_th)(A_n)\zeta-(g_th)(A)\zeta\|+\|(1-h)(A_n)\zeta\|+\|(1-h)(A)\zeta\|.
\]
By Lemma 6.3 the first term tends to \(0\) and \(\|(1-h)(A_n)\zeta\|^2=\langle(1-h)^2(A_n)\zeta,\zeta\rangle\to
\langle(1-h)^2(A)\zeta,\zeta\rangle<\varepsilon^2\). So the limit superior is at most \(2\varepsilon\).

*\(T'=T\).* For \(y\in N\), \(T'^{it}\sigma^\psi_t(y)=\lim T_n^{it}\sigma^\psi_t(y)=\lim yT_n^{it}=yT'^{it}\), so
\(T'\) is homogeneous of degree \(-1\), and \(T'=d\varphi'/d\psi\) for a normal semifinite \(\varphi'\) (Theorem 6.2).
From \((1+T)^{-1}\le A\le A_n\) and (B1)(ii), \(T_n\le T'\le T\), so \(\varphi_n\le\varphi'\le\varphi\) by Proposition
3.4(a). Taking the supremum over \(n\), \(\varphi'=\varphi\), so \(T'=T\) and \(A=(1+T)^{-1}\).

*The forms.* \(p(\zeta)=\sup_n\langle T_n\zeta,\zeta\rangle\le\langle T\zeta,\zeta\rangle\) is lower semicontinuous and
finite on \(\operatorname{dom}T^{1/2}\), so by Proposition 2.3 (with \(D=H\)) it is the form of a positive
self-adjoint \(T''\) with \(T_n\le T''\le T\). Then \((1+T)^{-1}\le(1+T'')^{-1}\le A_n\), and letting \(n\to\infty\),
\((1+T'')^{-1}=(1+T)^{-1}\), so \(p\) is the form of \(T\).

*The cocycles and modular groups.* By Theorem 5.4(a), \((D\varphi_n:D\varphi)_t=T_n^{it}T^{-it}\to1\) strongly, and
its adjoint \(T^{it}T_n^{-it}\to1\) strongly since \(T_n^{-it}=T_n^{i(-t)}\to T^{-it}\). For a vector functional
\(\omega=\langle\cdot\,\zeta,\zeta'\rangle\) and \(\|x\|\le1\),
\[
|\omega(\sigma^{\varphi_n}_t(x))-\omega(\sigma^\varphi_t(x))|\le\|T_n^{-it}\zeta-T^{-it}\zeta\|\,\|\zeta'\|+
\|\zeta\|\,\|T_n^{-it}\zeta'-T^{-it}\zeta'\|,
\]
uniformly in \(x\). Every \(\omega\in M_*\) is a norm limit of finite sums of vector functionals (B2)(ii), and the maps
\(\omega\mapsto\omega\circ\sigma_t\) are isometries, so the convergence holds for all \(\omega\in M_*\). \(\square\)

## 7. The operator-valued weight \(\Psi^{-1}\)

A reference for this section is [Connes 1980a]; for operator-valued weights see [Haagerup 1979].

The spatial derivative turns a weight \(\varphi\) on \(M\) into the weight \(\operatorname{Tr}_{d\varphi/d\psi}\) on
\(B(H)\). This passage is itself given by one operator-valued weight from \(B(H)\) to \(M\), determined by \(\psi\).

**Theorem 7.1.** Let \(\psi\) be an fns weight on \(N\). There is exactly one fns operator-valued weight \(\Psi^{-1}\)
from \(B(H)\) to \(M\) with \(\varphi_0\circ\Psi^{-1}=\operatorname{Tr}_{d\varphi_0/d\psi}\) for some fns weight
\(\varphi_0\) on \(M\). It has the following properties.

(a) \(\varphi\circ\Psi^{-1}=\operatorname{Tr}_{d\varphi/d\psi}\) for every normal semifinite weight \(\varphi\) on
\(M\).

(b) \(\Psi^{-1}(\xi\xi^*)=\theta^\psi(\xi,\xi)\) for every \(\xi\in D(H,\psi)\).

(c) Every normal operator-valued weight \(E:B(H)_+\to\widehat M_+\) with \(E(\xi\xi^*)=\theta^\psi(\xi,\xi)\) for all
\(\xi\in D(H,\psi)\) satisfies \(E\le\Psi^{-1}\).

(d) If \(\varphi_1,\varphi_2\) are normal semifinite weights on \(M\) and \(\varphi_1+\varphi_2\) is semifinite, then
\[
\frac{d(\varphi_1+\varphi_2)}{d\psi}=\frac{d\varphi_1}{d\psi}\dotplus\frac{d\varphi_2}{d\psi}.
\]
In particular this holds when \(\varphi_1(1),\varphi_2(1)<\infty\).

*Proof.* *Existence.* Fix an fns weight \(\varphi_0\) on \(M\) and let \(T_0=d\varphi_0/d\psi\), nonsingular by
Theorem 4.3. The weight \(\operatorname{Tr}_{T_0}\) on \(B(H)\) is fns, and its modular group
\(\operatorname{Ad}T_0^{it}\) (B6)(iii) restricts to \(\sigma^{\varphi_0}\) on \(M\) by (4.2). By Haagerup's existence
theorem (B7)(ii) there is a unique fns operator-valued weight \(E\) with \(\varphi_0\circ E=\operatorname{Tr}_{T_0}\).

*(a) for faithful \(\varphi\).* Let \(T=d\varphi/d\psi\). By (B7)(i), \(\varphi\circ E\) is fns and
\((D(\varphi\circ E):D(\varphi_0\circ E))_t=(D\varphi:D\varphi_0)_t\), which equals \(T^{it}T_0^{-it}\) by Theorem
5.4(a), and hence equals \((D\operatorname{Tr}_T:D\operatorname{Tr}_{T_0})_t\) by (B6)(iii). Two fns weights with the
same cocycle relative to \(\varphi_0\circ E\) are equal (B5)(ii), so \(\varphi\circ E=\operatorname{Tr}_T\).

*Uniqueness.* If \(E'\) is fns with \(\varphi_0'\circ E'=\operatorname{Tr}_{d\varphi_0'/d\psi}\) for some fns
\(\varphi_0'\), then by the previous step \(\varphi_0'\circ E=\operatorname{Tr}_{d\varphi_0'/d\psi}=\varphi_0'\circ
E'\), and the uniqueness in (B7)(ii) gives \(E'=E\). We write \(\Psi^{-1}=E\).

*(a) in general.* By Lemma 5.1(c), \(\varphi=\varphi_1(e\,\cdot\,e)\) with \(\varphi_1\) fns, \(e=s(\varphi)\), and
\(d\varphi/d\psi=T_1e\) with \(T_1=d\varphi_1/d\psi\) commuting with \(e\). By bimodularity, \(\Psi^{-1}(exe)=
e\Psi^{-1}(x)e\), and writing \(\varphi_1=\sum_i\omega_i\) (B2)(i), \(\varphi(m)=\sum_im(e\omega_ie)=\varphi_1(eme)\) for
\(m\in\widehat M_+\). Hence, for \(\zeta\in H\),
\[
\varphi(\Psi^{-1}(\zeta\zeta^*))=\varphi_1(\Psi^{-1}(e\zeta\zeta^*e))=\langle T_1e\zeta,e\zeta\rangle=\Big\langle
\frac{d\varphi}{d\psi}\zeta,\zeta\Big\rangle.
\]
Both \(\varphi\circ\Psi^{-1}\) and \(\operatorname{Tr}_{d\varphi/d\psi}\) are normal weights on \(B(H)\), and every
\(x\in B(H)_+\) is a \(\sigma\)-weakly convergent sum of rank-one operators \(\zeta_k\zeta_k^*\) (for instance
\(\zeta_k=x^{1/2}\varepsilon_k\) for an orthonormal basis), so they are equal.

(b) Every \(\omega\in M_*^+\) is a normal semifinite weight, and by (a),
\(\omega(\Psi^{-1}(\xi\xi^*))=\langle(d\omega/d\psi)\xi,\xi\rangle=\omega(\theta(\xi,\xi))\) for \(\xi\in D\). Elements
of \(\widehat M_+\) are determined by their values on \(M_*^+\).

(c) Let \(\omega\in M_*^+\). The map \(p(\zeta)=\omega(E(\zeta\zeta^*))\) is a positive form on \(H\), and it is lower
semicontinuous because \(\omega\circ E\) is a normal weight on \(B(H)\), a sum of normal functionals (B2)(i), each
continuous in \(\zeta\). It equals \(q_\omega\) on \(D\). By Proposition 2.3(b), \(p(\zeta)\le\langle(d\omega/d\psi)
\zeta,\zeta\rangle=\omega(\Psi^{-1}(\zeta\zeta^*))\), using (a). So \(E(\zeta\zeta^*)\le\Psi^{-1}(\zeta\zeta^*)\) for
all \(\zeta\), and by normality \(E(x)\le\Psi^{-1}(x)\) for all \(x\in B(H)_+\).

(d) By (a) and the additivity of normal weights on \(\widehat M_+\),
\[
\Big\langle\frac{d(\varphi_1+\varphi_2)}{d\psi}\zeta,\zeta\Big\rangle=(\varphi_1+\varphi_2)(\Psi^{-1}(\zeta\zeta^*))=
\Big\langle\frac{d\varphi_1}{d\psi}\zeta,\zeta\Big\rangle+\Big\langle\frac{d\varphi_2}{d\psi}\zeta,\zeta\Big\rangle
\]
for every \(\zeta\in H\). The left side is the form of a positive self-adjoint operator, so the right side is too, and
the two operators coincide. Bounded weights are semifinite, and so is their sum. \(\square\)

Property (b) alone does not determine \(\Psi^{-1}\), even among fns operator-valued weights.

**Example 7.2.** Let \(H=\ell^2(\{1,2,3,\dots\})\), \(M=\mathbb C1\), \(N=B(H)\). Let \(B\) be the diagonal operator with
entries \(1+n^2\), with form \(b(\xi)=\sum_n(1+n^2)|\xi_n|^2\). The functional \(\ell(\xi)=\sum_n\xi_n\) is continuous
for the graph norm of \(B^{1/2}\), since \(|\ell(\xi)|^2\le b(\xi)\sum_n(1+n^2)^{-1}\), but not for the norm of
\(H\): the vector with \(k\) coordinates equal to \(1/k\) has norm \(k^{-1/2}\) and \(\ell=1\). So
\(D_0=\ker\ell\cap\operatorname{dom}B^{1/2}\) is closed for the graph norm and dense in \(H\) (the kernel of a
discontinuous functional on the dense subspace \(\operatorname{dom}B^{1/2}\)). Let \(A\) be the operator of the closed
form \(b|_{D_0}\); then \(A\ge B\ge1\), \(\operatorname{dom}A^{1/2}=D_0\), and \(A\ne B\).

Let \(\psi=\operatorname{Tr}_{A^{-1}}\). By Example 3.6, \(D(H,\psi)=\operatorname{dom}A^{1/2}=D_0\) and
\(\theta^\psi(\xi,\xi)=\|A^{1/2}\xi\|^2\). For \(M=\mathbb C1\), normal operator-valued weights from \(B(H)\) to \(M\)
are exactly the normal weights on \(B(H)\), and \(\Psi^{-1}=\operatorname{Tr}_A\) (Theorem 7.1(a) with
\(\varphi(\lambda1)=\lambda\) and Example
3.6). The fns weight \(E=\operatorname{Tr}_B\) also satisfies \(E(\xi\xi^*)=b(\xi)=\|A^{1/2}\xi\|^2=\theta^\psi(\xi,\xi)\)
for \(\xi\in D(H,\psi)\), but \(E(\varepsilon_1\varepsilon_1^*)=2<\infty=\Psi^{-1}(\varepsilon_1\varepsilon_1^*)\), where
\(\varepsilon_1\) is the first basis vector (\(\ell(\varepsilon_1)=1\)). By Theorem 7.3, \(E=\Psi_1^{-1}\) for
\(\psi_1=\operatorname{Tr}_{B^{-1}}\ne\psi\).

*Reference:* Part (a) of [Connes 1980a, Corollary 16] states that \(\Psi^{-1}\) is the unique normal operator-valued
weight satisfying (b); Example 7.2 shows that this fails, so we characterize \(\Psi^{-1}\) by (a), or as the largest one
satisfying (b), as in (c).

**Theorem 7.3.** Every fns operator-valued weight \(E\) from \(B(H)\) to \(M\) equals \(\Psi^{-1}\) for a unique fns
weight \(\psi\) on \(N\).

*Proof.* Fix an fns weight \(\varphi\) on \(M\). By (B7)(i), \(\varphi\circ E\) is fns on \(B(H)\), so by (B6)
\(\varphi\circ E=\operatorname{Tr}_S\) with \(S\) nonsingular, and \(S^{it}xS^{-it}=\sigma^\varphi_t(x)\) for \(x\in
M\). Hence \((S^{-1})^{it}x=\sigma^\varphi_{-t}(x)(S^{-1})^{it}\): \(S^{-1}\) is homogeneous of degree \(-1\) with
respect to \(\varphi\), for the von Neumann algebra \(N\) with commutant \(M\). By the mirror image of Theorem 6.2,
\(S^{-1}=d\psi/d\varphi\) for a normal semifinite weight \(\psi\) on \(N\), faithful since \(S^{-1}\) is nonsingular.
By Theorem 5.6, \(d\varphi/d\psi=S\), so \(\varphi\circ E=\operatorname{Tr}_{d\varphi/d\psi}\) and \(E=\Psi^{-1}\) by
the uniqueness in Theorem 7.1. If \(\Psi_1^{-1}=\Psi_2^{-1}\), then \(d\varphi/d\psi_1=d\varphi/d\psi_2\) by Theorem
7.1(a), hence \(d\psi_1/d\varphi=d\psi_2/d\varphi\) by Theorem 5.6, and \(\psi_1=\psi_2\) by the mirror image of
Proposition 3.3. \(\square\)

So \(\psi\mapsto\Psi^{-1}\) is a bijection from fns weights on \(M'\) onto fns operator-valued weights from \(B(H)\)
to \(M\), and \(d\varphi/d\psi\) is the density of the weight \(\varphi\circ\Psi^{-1}\) on \(B(H)\). Exercise 4 shows
that the bijection reverses order.

## 8. Integrable operators and the integral \(\int T\,d\psi\)

**Corollary 8.1.** For positive self-adjoint \(T\) on \(H\), the conditions below are equivalent.

(a) \(T=d\varphi/d\psi\) for some \(\varphi\in M_*^+\).

(b) \(T\) is homogeneous of degree \(-1\), and \(\sum_\alpha\langle T\xi_\alpha,\xi_\alpha\rangle<\infty\) for some
family \((\xi_\alpha)\) in \(D\) with \(\sum_\alpha\theta(\xi_\alpha,\xi_\alpha)=1\) (strongly).

(b') \(T\) is homogeneous of degree \(-1\), and \(\sum_\alpha\langle T\xi_\alpha,\xi_\alpha\rangle<\infty\) for every
family \((\xi_\alpha)\) in \(D\) with \(\sum_\alpha\theta(\xi_\alpha,\xi_\alpha)=1\) (strongly).

(c) \(D\) lies in \(\operatorname{dom}T^{1/2}\) and is a core for \(T^{1/2}\), and for some \(C<\infty\)
\[
\Big|\sum_{i=1}^n\langle T^{1/2}\xi_i,T^{1/2}\eta_i\rangle\Big|\le C\,\Big\|\sum_{i=1}^n\theta(\xi_i,\eta_i)\Big\|
\qquad(\xi_i,\eta_i\in D).
\]

In that case \(\varphi(1)=\sum_\alpha\langle T\xi_\alpha,\xi_\alpha\rangle\) for every family as in (b').

*Proof.* Let \((\xi_\alpha)\) be any family in \(D\) with \(\sum\theta(\xi_\alpha,\xi_\alpha)=1\). If \(T=d\varphi/d\psi\)
for a normal semifinite \(\varphi\), then the finite partial sums \(e_F\) increase to \(1\), and normality gives
\[
\varphi(1)=\sup_F\sum_{\alpha\in F}\varphi(\theta(\xi_\alpha,\xi_\alpha))=\sum_\alpha\langle T\xi_\alpha,
\xi_\alpha\rangle. \tag{8.1}
\]
With Theorem 6.2 this gives (a)\(\Leftrightarrow\)(b)\(\Leftrightarrow\)(b') and the last claim.

(a)\(\Rightarrow\)(c). As noted after Definition 3.2, \(D\subset\operatorname{dom}T^{1/2}\) and \(D\) is a core. By
polarization, \(\langle T^{1/2}\xi,T^{1/2}\eta\rangle=\varphi(\theta(\xi,\eta))\), where \(\varphi\) is extended
linearly to \(M\). So the left side of (c) is \(|\varphi(\sum_i\theta(\xi_i,\eta_i))|\le\varphi(1)\|\sum_i
\theta(\xi_i,\eta_i)\|\).

(c)\(\Rightarrow\)(a). Suppose \(\sum_i\theta(\xi_i,\xi_i)=\sum_j\theta(\xi'_j,\xi'_j)\). Apply (c) to the pairs
\((\xi_i,\xi_i)\) and \((-\xi'_j,\xi'_j)\): the right side is \(0\), so \(\sum_i\langle T\xi_i,\xi_i\rangle=\sum_j
\langle T\xi'_j,\xi'_j\rangle\). So (3) of Theorem 6.2 holds and \(T=d\varphi/d\psi\) for a normal semifinite
\(\varphi\) with \(\varphi(y)\le C\|y\|\) for \(y\in\mathcal J_\psi^+\). With a \(\psi\)-basis, (8.1) gives
\(\varphi(1)=\sup_F\varphi(e_F)\le C\). \(\square\)

**Definition 8.2.** A positive self-adjoint \(T\) on \(H\), homogeneous of degree \(-1\), is called
*\(\psi\)-integrable* if it satisfies the conditions of Corollary 8.1. For any positive \(T\) homogeneous of degree
\(-1\) we put
\[
\int T\,d\psi=\sum_\alpha\langle T\xi_\alpha,\xi_\alpha\rangle\in[0,\infty],
\]
for any family \((\xi_\alpha)\) in \(D\) with \(\sum\theta(\xi_\alpha,\xi_\alpha)=1\). By (8.1) this equals
\(\varphi(1)\) for the weight \(\varphi\) with \(T=d\varphi/d\psi\), and so does not depend on the family. By Remark
1.6 the definition applies to any \(N\)-module \(H\).

For instance, in Example 3.6 (\(M=\mathbb C\)) every positive \(T\) homogeneous of degree \(-1\) is \(\mu K^{-1}\), and
\(\int T\,d\psi=\mu\).

The next result compares an operator of degree \(-\tfrac12\) with its adjoint. It is the noncommutative form of the
identity \(\operatorname{Tr}(T^*T)=\operatorname{Tr}(TT^*)\).

**Corollary 8.3.** Let \(H_1,H_2\) be \(N\)-modules and \(T:H_1\to H_2\) closed, densely defined and homogeneous of
degree \(-\tfrac12\). Then \(T^*T\) and \(TT^*\) are homogeneous of degree \(-1\), and
\[
\int T^*T\,d\psi=\int TT^*\,d\psi.
\]
In particular \(T^*T\) is \(\psi\)-integrable iff \(TT^*\) is.

*Proof.* Let \(T=u|T|\), \(e_1=u^*u=s(|T|)\) and \(e_2=uu^*\); both commute with \(N\) (Definition 6.1 and the remark
after it). With \(t\) replaced by \(2t\), (6.1) gives \((T^*T)^{it}y=|T|^{2it}y=\sigma^\psi_{-t}(y)(T^*T)^{it}\). Next
\(|T^*|=u|T|u^*\), so \((TT^*)^{it}=u|T|^{2it}u^*\), and since \(u,u^*\) commute with \(N\),
\[
(TT^*)^{it}y=u|T|^{2it}yu^*=u\sigma^\psi_{-t}(y)|T|^{2it}u^*=\sigma^\psi_{-t}(y)(TT^*)^{it}.
\]
So both are homogeneous of degree \(-1\): \(T^*T=d\varphi_1/d\psi\) and \(TT^*=d\varphi_2/d\psi\) for normal semifinite
weights \(\varphi_j\) on \(\mathcal L_N(H_j)\) (Theorem 6.2), with supports \(e_1\), \(e_2\) (Corollary 5.2).

Apply Proposition 1.5(a) to the \(N\)-module \(e_1H_1\): there is a family \((\xi_\alpha)\) in \(D(e_1H_1,\psi)
\subset D(H_1,\psi)\) with \(\sum_\alpha\theta(\xi_\alpha,\xi_\alpha)=e_1\) (for \(\xi\in e_1H_1\), the operator
\(\theta(\xi,\xi)\) computed in \(H_1\) is the one computed in \(e_1H_1\), extended by \(0\)). By Lemma 1.2(a), \(u\xi_\alpha\in
D(H_2,\psi)\) and \(\sum_\alpha\theta(u\xi_\alpha,u\xi_\alpha)=ue_1u^*=e_2\). By normality, and since \(\varphi_j\)
vanishes on \(1-e_j\),
\[
\int T^*T\,d\psi=\varphi_1(e_1)=\sum_\alpha\langle T^*T\xi_\alpha,\xi_\alpha\rangle,\qquad\int TT^*\,d\psi=\varphi_2(e_2)
=\sum_\alpha\langle TT^*u\xi_\alpha,u\xi_\alpha\rangle.
\]
Finally \(u^*u\xi_\alpha=\xi_\alpha\), so \(u\xi_\alpha\in\operatorname{dom}|T^*|\) iff \(\xi_\alpha\in\operatorname{dom}
|T|\), and then \(\||T^*|u\xi_\alpha\|=\|u|T|\xi_\alpha\|=\||T|\xi_\alpha\|\). The two sums agree term by term. \(\square\)

In the same spirit one can consider, for \(1\le p<\infty\), the operators homogeneous of degree \(-1/p\) whose
\(p\)-th power of the modulus is integrable. They form noncommutative \(L^p\) spaces attached to \(M\) and \(\psi\); see
[Hilsum 1981].

## 9. Exercises

**Exercise 1 (scaling).** Show that \(d(\lambda\varphi)/d(\mu\psi)=(\lambda/\mu)\,d\varphi/d\psi\) for
\(\lambda,\mu>0\), and deduce \((D(\mu\psi):D\psi)_t=\mu^{it}\) from Theorem 5.4(b).

*Solution.* A vector is \(\mu\psi\)-bounded iff it is \(\psi\)-bounded. By (1.2), with \(\mu\psi(y^*y)\le1\) iff
\(\psi((\mu^{1/2}y)^*(\mu^{1/2}y))\le1\), we get \(\theta^{\mu\psi}(\xi,\xi)=\mu^{-1}\theta^\psi(\xi,\xi)\). So
\(q^{\mu\psi}_{\lambda\varphi}=(\lambda/\mu)q^\psi_\varphi\) on the same domain, and the closures scale the same way.
Taking \(\lambda=1\), Theorem 5.4(b) gives \((D(\mu\psi):D\psi)_{-t}=(\mu^{-1}T)^{it}T^{-it}=\mu^{-it}\), that is
\((D(\mu\psi):D\psi)_t=\mu^{it}\).

**Exercise 2 (covariance in the second variable).** For a unitary \(v\in N\) let \(\psi_v(y)=\psi(v^*yv)\). Show
directly from the definitions that \(D(H,\psi_v)=vD(H,\psi)\), that \(\theta^{\psi_v}(\xi,\xi)=\theta^\psi(v^*\xi,
v^*\xi)\), and that \(d\varphi/d\psi_v=v\,(d\varphi/d\psi)\,v^*\).

*Solution.* We have \(\mathfrak n_{\psi_v}=\mathfrak n_\psi v^*\), and \(y\mapsto yv\) maps \(\{\psi_v(y^*y)\le1\}\) onto
\(\{\psi(z^*z)\le1\}\). Since \(\|y\xi\|=\|(yv)(v^*\xi)\|\), \(\xi\) is \(\psi_v\)-bounded iff \(v^*\xi\) is
\(\psi\)-bounded. By (1.2), \(\langle\theta^{\psi_v}(\xi,\xi)\omega,\omega\rangle=\sup_{\psi(z^*z)\le1}|\langle
zv^*\xi,\omega\rangle|^2=\langle\theta^\psi(v^*\xi,v^*\xi)\omega,\omega\rangle\). So
\(q^{\psi_v}_\varphi(\xi)=q^\psi_\varphi(v^*\xi)=\langle Tv^*\xi,v^*\xi\rangle\) with \(T=d\varphi/d\psi\). The operator
\(vTv^*\) has form \(\zeta\mapsto\langle Tv^*\zeta,v^*\zeta\rangle\), and \(v(D(H,\psi)\cap\operatorname{dom}T^{1/2})\)
is a core for \((vTv^*)^{1/2}=vT^{1/2}v^*\). By Definition 3.2, \(d\varphi/d\psi_v=vTv^*\). (Compare with Theorem
5.4(b): \((D\psi_v:D\psi)_t=v\sigma^\psi_t(v^*)\), and \(v\sigma^\psi_{-t}(v^*)T^{it}=vT^{it}v^*\) by (4.2).)

**Exercise 3 (a tensor product).** Let \(H=H_0\otimes K\), \(M=B(H_0)\otimes1\), \(N=1\otimes B(K)\), and
\(\psi(1\otimes y)=\operatorname{Tr}_k(y)\) for a positive nonsingular \(k\) on \(K\). Show that
\(d(\operatorname{Tr}_S\otimes1)/d\psi=S\otimes k^{-1}\) for every positive self-adjoint \(S\) on \(H_0\), where
\((\operatorname{Tr}_S\otimes1)(x\otimes1)=\operatorname{Tr}_S(x)\).

*Solution.* Put \(T=S\otimes k^{-1}\); then \(T^{it}=S^{it}\otimes k^{-it}\) and \(T^{it}(1\otimes\sigma^\psi_t(y))=
S^{it}\otimes k^{-it}k^{it}yk^{-it}=(1\otimes y)T^{it}\), since \(\sigma^\psi_t=\operatorname{Ad}k^{it}\). So \(T\) is
homogeneous of degree \(-1\), and \(T=d\varphi/d\psi\) for a unique normal semifinite \(\varphi\) (Theorem 6.2). To
identify \(\varphi\) we use (3.1). Choose \(\eta\in\operatorname{dom}k^{-1/2}\) with \(\|k^{-1/2}\eta\|=1\) and an
orthonormal basis \((\zeta_j)\) of \(H_0\). By Example 3.6, \(\|(1\otimes y)(\zeta\otimes\eta)\|=\|\zeta\|\,\|y\eta\|\le
\|\zeta\|\,\psi(y^*y)^{1/2}\), so \(\zeta\otimes\eta\in D\). For \(\omega\in H\) let \(\omega_\zeta\in K\) be defined by
\(\langle\omega_\zeta,\kappa\rangle=\langle\omega,\zeta\otimes\kappa\rangle\); then \(\langle(1\otimes y)(\zeta\otimes
\eta),\omega\rangle=\langle y\eta,\omega_\zeta\rangle\), and (1.2) with Example 3.6 gives
\[
\langle\theta(\zeta\otimes\eta,\zeta\otimes\eta)\omega,\omega\rangle=\|k^{-1/2}\eta\|^2\|\omega_\zeta\|^2=
\langle(\zeta\zeta^*\otimes1)\omega,\omega\rangle.
\]
So \(\theta(\zeta_j\otimes\eta,\zeta_j\otimes\eta)=\zeta_j\zeta_j^*\otimes1\), and \((\zeta_j\otimes\eta)\) is a
\(\psi\)-basis. For \(x\in B(H_0)_+\), (3.1) gives
\[
\varphi(x\otimes1)=\sum_j\langle(S\otimes k^{-1})(x^{1/2}\zeta_j\otimes\eta),x^{1/2}\zeta_j\otimes\eta\rangle=
\sum_j\langle Sx^{1/2}\zeta_j,x^{1/2}\zeta_j\rangle\,\langle k^{-1}\eta,\eta\rangle=\operatorname{Tr}_S(x),
\]
using \(\langle(A\otimes B)(a\otimes b),a\otimes b\rangle=\langle Aa,a\rangle\langle Bb,b\rangle\) in \([0,\infty]\)
for positive \(A,B\) and nonzero \(a,b\), and (B6)(i) with \(x=\sum_j(x^{1/2}\zeta_j)(x^{1/2}\zeta_j)^*\).

**Exercise 4 (order reversal).** Let \(\psi_1,\psi_2\) be fns weights on \(N\). Show that \(\psi_1\le\psi_2\) iff
\(\Psi_2^{-1}\le\Psi_1^{-1}\).

*Solution.* Fix an fns weight \(\varphi\) on \(M\) and put \(S_j=d\varphi/d\psi_j\). By the mirror image of
Proposition 3.4(a) and Theorem 5.6, \(\psi_1\le\psi_2\) iff \(d\psi_1/d\varphi\le d\psi_2/d\varphi\) iff
\(S_1^{-1}\le S_2^{-1}\) iff \(S_2\le S_1\) (B1)(ii). The last condition is independent of \(\varphi\). If
\(\Psi_2^{-1}\le\Psi_1^{-1}\), then \(\operatorname{Tr}_{S_2}=\varphi\circ\Psi_2^{-1}\le\varphi\circ\Psi_1^{-1}=
\operatorname{Tr}_{S_1}\), and evaluating on rank-one operators gives \(S_2\le S_1\). Conversely, if \(\psi_1\le
\psi_2\), then \(d\omega/d\psi_2\le d\omega/d\psi_1\) for every \(\omega\in M_*^+\). For faithful \(\omega\) this is
the previous argument; in general write \(d\omega/d\psi_j=T_je\) as in Lemma 5.1, where \(T_j=d\omega_1/d\psi_j\) for an
fns \(\omega_1\) independent of \(j\). Then \(\omega(\Psi_2^{-1}(\zeta\zeta^*))=\langle T_2e\zeta,e\zeta\rangle\le
\langle T_1e\zeta,e\zeta\rangle=\omega(\Psi_1^{-1}(\zeta\zeta^*))\), and by normality \(\Psi_2^{-1}\le\Psi_1^{-1}\).

**Exercise 5 (degree \(-\tfrac12\) in the standard case).** In the situation of Proposition 5.5, show that
\(\Delta_\psi^{-1/2}\) is homogeneous of degree \(-\tfrac12\) on \(H_\psi\), and that \(\int\Delta_\psi^{-1}\,d\psi=
\psi(1)\).

*Solution.* By (B3)(i), \(\Delta_\psi^{-is/2}y=\sigma^\psi_{-s/2}(y)\Delta_\psi^{-is/2}\), which is (6.1) with
\(\alpha=-\tfrac12\) (and \(u=1\)). By Proposition 5.5, \(\Delta_\psi^{-1}=d\psi'/d\psi\), so
\(\int\Delta_\psi^{-1}d\psi=\psi'(1)=\psi(J_\psi1J_\psi)=\psi(1)\), using (B4)(i). Corollary 8.3 is trivial here, since
\(T=T^*\).

## References



- [Connes 1980a] A. Connes, On the spatial theory of von Neumann algebras, J. Functional Analysis 35 (1980), no. 2,
  153–164. Free at https://doi.org/10.1016/0022-1236(80)90002-6
- [Connes 1979] A. Connes, Sur la théorie non commutative de l'intégration, in: Algèbres d'opérateurs (Sém.,
  Les Plans-sur-Bex, 1978), Lecture Notes in Math. 725, Springer, Berlin, 1979, 19–143. Free at https://alainconnes.org/wp-content/uploads/ThNonComm.pdf
- [Connes 1973] A. Connes, Une classification des facteurs de type III, Ann. Sci. École Norm. Sup. (4) 6 (1973),
  133–252. https://doi.org/10.24033/asens.1247. Free at https://alainconnes.org/wp-content/uploads/classificationfacteurs.pdf
- [Connes 1994] A. Connes, Noncommutative geometry, Academic Press, San Diego, CA, 1994.
  https://alainconnes.org/publications/
- [Haagerup 1975] U. Haagerup, Normal weights on W\*-algebras, J. Functional Analysis 19 (1975), 302–317.
  https://doi.org/10.1016/0022-1236(75)90060-9. Free at https://doi.org/10.1016/0022-1236(75)90060-9
- [Haagerup 1979] U. Haagerup, Operator valued weights in von Neumann algebras I, J. Functional Analysis 32 (1979),
  175–206; II, J. Functional Analysis 33 (1979), 339–361. https://doi.org/10.1016/0022-1236(79)90053-3,
  https://doi.org/10.1016/0022-1236(79)90072-7. Free at https://doi.org/10.1016/0022-1236(79)90053-3
- [Hilsum 1981] M. Hilsum, Les espaces \(L^p\) d'une algèbre de von Neumann définies par la dérivée spatiale,
  J. Functional Analysis 40 (1981), 151–169. https://doi.org/10.1016/0022-1236(81)90065-3. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123681900653
