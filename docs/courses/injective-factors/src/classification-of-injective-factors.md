# Classification of injective factors

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. The example after Corollary 6.5 was supplied by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked by Claude Opus 5.5, October 2026. Public domain (CC0).*

## Introduction

A von Neumann algebra \(M\subset B(H)\) is *injective* when there is a projection of norm one from \(B(H)\) onto
\(M\). The previous lesson, "Uniqueness of the injective II₁ factor", proved that every injective II₁ factor with
separable predual is isomorphic to the hyperfinite factor \(R\). This lesson draws the consequences. We prove:

1. there is one injective factor of type II∞, \(R_{0,1}=R\mathbin{\bar\otimes}B(\ell^2)\) (Section 4);
2. for each \(\lambda\in\,]0,1[\) there is one injective factor of type III\(_\lambda\), the Powers factor
   \(R_\lambda\) (Section 8);
3. each injective type III₀ factor is a Krieger factor, and so the flow of weights classifies the injective type III₀
   factors (Section 9);
4. each injective type III₁ factor is semidiscrete and approximately finite dimensional (Section 10);
5. for factors with separable predual, approximate finite dimensionality, injectivity, semidiscreteness and property
   P are the same property (Section 11).

Along the way we describe all injective semifinite von Neumann algebras with separable predual (Section 6), prove a
bicommutant theorem for subalgebras of \(R\) (Section 7), and give applications to groups: the group von Neumann
algebra of an ICC group is \(R\) exactly when the group is amenable (Section 5), the regular representation of a
second countable connected group generates only the factors \(R_{0,1}\) and type I factors (Section 6), and every
representation of a connected or an amenable group generates an approximately finite-dimensional algebra (Section 11).

These results matter because they turn one hard theorem (the II₁ case) into a complete picture of the injective
factors other than type III₁. The method is always the same: a structure theorem writes the factor as a crossed
product of a semifinite algebra, injectivity passes to the semifinite part, the semifinite part is identified with
\(R\) or \(R_{0,1}\), and a classification of the crossing automorphisms finishes the job.

**What is assumed.** From this course we use the lessons "Injective von Neumann algebras" and "Uniqueness of the
injective II₁ factor"; Section 1 restates exactly what we take from them. From Course 1 we use one lemma of the lesson
"Full factors without almost periodic weights", also restated in Section 1. The discrete decompositions of type III
factors, the theory of Krieger factors and the flow of weights, and the classification of trace-scaling
automorphisms of \(R_{0,1}\) are used without proof; they are stated precisely in "Results used from other lessons", with the lessons that prove the
standard facts. Standard
material is taught in other lessons of this programme:
"Completely positive maps", "Projections and types of von Neumann algebras", "Traces on von Neumann algebras",
"Conditional expectations from modular invariance", "Measurable fields of Hilbert spaces and their direct integrals",
"Decomposable operators and the diagonal algebra", "The Effros Borel structure", "Polish spaces and standard Borel
spaces", "Spatial tensor products of von Neumann algebras" and "Haar measure on locally compact groups".

Basic references are [Connes 1976], [Connes 1973], [Connes 1994], [Haagerup 1987] and [Anantharaman–Popa].

**Conventions.** All Hilbert spaces are separable unless said otherwise, and all von Neumann algebras have separable
predual. A subalgebra of a von Neumann algebra contains its unit unless said otherwise. \(\mathcal U(M)\) is the unitary
group of \(M\), \(Z(M)\) its centre. \(M_n=M_n(\mathbb C)\), and \(M_\infty=B(\ell^2)\). For a faithful normal state
\(\varphi\) we write \(\|x\|_\varphi=\varphi(x^*x)^{1/2}\); for a finite algebra with a faithful normal tracial state
\(\tau\) we write \(\|x\|_2=\tau(x^*x)^{1/2}\).

## Results used from other lessons

**(B1) Completely positive maps.** A unital completely positive (ucp) map has norm one and satisfies the
Kadison–Schwarz inequality \(\Phi(x)^*\Phi(x)\le\Phi(x^*x)\). *Arveson's extension theorem:* if \(S\subset A\) is an
operator system in a unital C\*-algebra \(A\), every completely positive map \(S\to M_n\) extends to a completely
positive map \(A\to M_n\) with the same value at \(1\). *Tomiyama's theorem:* a projection of norm one \(E\) from a
C\*-algebra \(A\) onto a C\*-subalgebra \(B\) is completely positive and \(B\)-bimodular, \(E(bxb')=bE(x)b'\). Every
unital finite-dimensional C\*-algebra \(D\) embeds unitally in some \(M_n\), and there is a ucp projection of
\(M_n\) onto \(D\). The norm and the Kadison–Schwarz inequality: Completely positive maps, Theorem
4.1. Arveson's theorem: Completely positive finite models, Theorem
2.3. Tomiyama's theorem: Injective von Neumann algebras,
(B3). A finite-dimensional C\*-algebra is a finite sum of matrix algebras (AF-algebras,
Section 2), hence a unital subalgebra of some \(M_n\), and a completely positive contraction of
\(M_n\) onto \(D\) fixing \(D\) is Completely positive finite models, Corollary
2.4; it is unital because \(1\in D\). See also [Arveson
1969] and [Tomiyama 1957].

**(B2) Conditional expectations.** *Takesaki's theorem:* if \(\varphi\) is a faithful normal state on \(M\) and
\(N\subset M\) is a von Neumann subalgebra with \(\sigma^\varphi_t(N)=N\) for all \(t\), there is a unique
\(\varphi\)-preserving normal conditional expectation of \(M\) onto \(N\). In particular, if \(\tau\) is a faithful
normal tracial state on \(M\), every von Neumann subalgebra has a \(\tau\)-preserving normal conditional expectation.
Proved in Conditional expectations from modular invariance, §§ME-01, ME-04 and ME-08
(existence, normality, uniqueness); the tracial case is also Integration for a trace, Theorem 9.1.

**(B3) Topologies.** On bounded sets of a von Neumann algebra, the strong operator topology of any faithful normal
representation coincides with the \(\sigma\)-strong topology, which is intrinsic. If \(\varphi\) is a faithful normal
state, a bounded net \(x_i\) tends to \(x\) \(\sigma\)-strongly if and only if \(\|x_i-x\|_\varphi\to0\). In
particular, for a finite algebra with faithful normal tracial state \(\tau\), strong convergence of bounded nets is
\(\|\cdot\|_2\)-convergence. *Kaplansky's density theorem:* if \(A_0\) is a \(*\)-algebra that is \(\sigma\)-weakly
dense in \(M\), every \(x\in M\) is a \(\sigma\)-strong\* limit of a net in \(A_0\) bounded by \(\|x\|\). The unit ball
of a finite von Neumann algebra is complete for \(\|\cdot\|_2\). Strong and σ-strong topologies agree on bounded sets
(Compact and trace-class operators, Lemma 8.5), and the σ-strong topology is intrinsic because
isomorphisms of von Neumann algebras are σ-weakly bicontinuous (The universal enveloping von Neumann algebra, Corollary
11.4). For a faithful normal state \(\varphi\) with GNS vector \(\xi_\varphi\), convergence in
\(\|\cdot\|_\varphi\) is convergence on \(\xi_\varphi\); since \(\xi_\varphi\) is separating for \(M\), it is cyclic for \(M'\) (The
double commutant theorem, Proposition 9.2), and a bounded net that converges on \(\xi_\varphi\) converges on
the dense set \(M'\xi_\varphi\), hence strongly. Kaplansky's theorem: Kaplansky's density theorem and its consequences, Theorem
7.1. Completeness of the ball: Approximately inner and centrally trivial automorphisms,
(B1).

**(B4) Types and projections.** A von Neumann algebra is the direct sum of its parts of types I\(_n\) (\(1\le
n\le\infty\)), II₁, II∞ and III. The part of type I\(_n\) is isomorphic to \(Z_n\mathbin{\bar\otimes}M_n\) with
\(Z_n\) abelian. A finite von Neumann algebra with separable predual has a faithful normal tracial state. A semifinite
algebra has a finite projection with central support \(1\). Two properly infinite countably decomposable projections
with the same central support are equivalent. The centre of \(eAe\) is \(Z(A)e\), and \(z\mapsto ze\) is an
isomorphism of \(Z(A)\) onto it when \(e\) has central support \(1\). If \(e\) is a nonzero finite projection of a II∞ factor \(M\)
with separable predual, then \(M\cong eMe\mathbin{\bar\otimes}B(\ell^2)\). A factor with separable predual is of
exactly one of the types I\(_n\) (\(n\le\infty\)), II₁, II∞, III\(_\lambda\) (\(0\le\lambda\le1\)); a finite factor
is of type I\(_n\) with \(n<\infty\) or of type II₁. The type decomposition and type I structure: Projections and
types of von Neumann algebras, Theorems 7.2 and 10.3. A finite algebra with separable predual has a
faithful normal state (a convex combination \(\sum_n2^{-n}\varphi_n\) of a dense sequence of normal states), hence is
σ-finite, and so it has a faithful normal tracial state (Traces on von Neumann algebras, Lemma 5.11, Corollary 5.12 and
Theorem 5.2). Finite projections with central support \(1\): Projections and types, Lemma
7.4(2). Properly infinite σ-finite projections with the same central support majorize each other
(Proposition 15.2(2)), hence are equivalent (Proposition 5.1). Centres of corners:
Traces on von Neumann algebras, Lemma 1.5. The tensor splitting of a II∞ factor: Projections and types,
Proposition 15.3(2). For the types III\(_\lambda\) see [Connes 1973].

**(B5) Central decomposition.** Let \(Q\) be a von Neumann algebra on a separable Hilbert space \(H\). There are a
standard probability space \((X,\mu)\), a measurable field \(x\mapsto H(x)\) of Hilbert spaces with
\(H=\int^\oplus_XH(x)\,d\mu(x)\), with \(H(x)\ne0\) for almost every \(x\), and a measurable field \(x\mapsto Q(x)\) of factors
on \(H(x)\), such that:
(i) \(Z(Q)\) is the algebra of diagonal operators \(L^\infty(X,\mu)\); (ii) \(Q\) (respectively \(Q'\)) is the set of
decomposable operators \(T\) with \(T(x)\in Q(x)\) (respectively \(T(x)\in Q(x)'\)) for almost every \(x\); (iii) if
countably many decomposable operators \(a_n\) generate \(Q\) (respectively \(Q'\)), then the \(a_n(x)\) generate
\(Q(x)\) (respectively \(Q(x)'\)) for almost every \(x\); (iv) if \(Q\) is of type II₁, almost every \(Q(x)\) is of
type II₁; (v) if \(\xi=\int^\oplus\xi(x)\,d\mu(x)\) is cyclic for \(Q\), then \(\xi(x)\) is cyclic for \(Q(x)\) for
almost every \(x\), and if the vector state of \(\xi\) is a trace on \(Q\), the vector state of \(\xi(x)\) is a trace on
\(Q(x)\) for almost every \(x\). A measurable field of Hilbert spaces of constant dimension \(\aleph_0\) is isomorphic to
the constant field, so that \(\int^\oplus H(x)\,d\mu=L^2(X,\mu;H_0)\); and for a fixed von Neumann algebra
\(Q_0\subset B(H_0)\), the decomposable operators with values in \(Q_0\) form \(L^\infty(X,\mu)\mathbin{\bar\otimes}
Q_0\). The central decomposition is proved in The central decomposition and the types of the fibres, with \(X=\mathbb R\) and a Borel probability measure \(\mu\): (i), (ii) and \(H(x)\ne0\) are Theorems 2.1 and 4.1(1) there, (iii) is Theorem 4.1(2), (iv) is Theorem 5.3, and (v) is Theorem 4.2; by Theorem 4.4 there, the decomposition is unique up to a Borel identification of the bases and a measurable field of unitaries. Constant dimension gives the constant field by Measurable fields of Hilbert spaces and their direct integrals,
Theorem 5.1, and the decomposable operators with values in \(Q_0\) are \(L^\infty\bar\otimes Q_0\) by
Spatial tensor products of von Neumann algebras, Example 7.2 and Corollary 11.5(2).

**(B6) Uniformization.** *Jankov–von Neumann uniformization theorem:* if \(X,Y\) are standard Borel spaces, \(\mu\) a
probability measure on \(X\), and \(S\subset X\times Y\) a Borel set whose projection to \(X\) is \(\mu\)-conull, there
is a Borel map \(s:X_0\to Y\) on a \(\mu\)-conull Borel set \(X_0\) with \((x,s(x))\in S\). The unitary group of a
separable Hilbert space with the strong topology is a Polish group. The first statement is proved as in Injective von
Neumann algebras, (B11), from Polish spaces and standard Borel spaces, Theorem
7.7. For the second, the unit ball with the strong\* topology is Polish (Injective von Neumann algebras,
(B9)); the unitaries form a closed subset of it, because multiplication is jointly
strong\* continuous on the ball and the adjoint is strong\* continuous; on unitaries the strong and strong\* topologies
agree, since \(\|(u_i-u)^*\xi\|=\|(u_i^*u-1)u^*\xi\|\) and \(\|(u^*u_i-1)\eta\|=\|(u_i-u)\eta\|\) give each other.

**(B7) Infinite tensor products.** Let \(\omega_\lambda\) (\(0<\lambda\le1\)) be the state on \(M_2\) with density
\(\operatorname{diag}(1/(1+\lambda),\lambda/(1+\lambda))\). For states \(\omega_n\) on \(M_2\) with faithful densities,
the infinite tensor product \((P,\varphi)=\bigotimes_{n\ge1}(M_2,\omega_n)\) is a factor with separable predual, the
product state \(\varphi\) is faithful and normal, and \(\sigma^\varphi_t=\bigotimes_n\sigma^{\omega_n}_t\); in
particular \(\sigma^\varphi_t\) maps \(M_2^{\otimes k}\otimes1\) onto itself. The modular group of a tensor product of
faithful normal states is the tensor product of the modular groups. With \(\omega_n=\omega_1\) for all \(n\), \(P\) is
the hyperfinite II₁ factor \(R\). With \(\omega_n=\omega_\lambda\), \(0<\lambda<1\), \(P\) is the *Powers factor*
\(R_\lambda\), of type III\(_\lambda\). With \(\omega_n\) alternately \(\omega_\lambda\) and \(\omega_\mu\), where \(\log
\lambda/\log\mu\) is irrational, \(P\) is the Araki–Woods factor \(R_\infty\), of type III₁. The infinite tensor product, its factoriality, the faithful normal product state and the product
modular group are proved in Infinite tensor products, Theorem 5.1, Proposition 5.2, Corollary 5.3 and Theorem
6.1. The types of \(R_\lambda\) and \(R_\infty\) are
due to Powers and to Araki and Woods [Araki–Woods 1968]; the point spectrum of the product state is computed in Almost periodic weights and
the invariant Sd, Example 3.9.

**(B8) Crossed products by discrete groups.** For an action \(\alpha\) of a countable group \(\Gamma\) on \(N\subset
B(H)\), the crossed product \(N\rtimes_\alpha\Gamma\) is the von Neumann algebra on \(\ell^2(\Gamma,H)\) generated by
\((\pi(a)\xi)(s)=\alpha_{s^{-1}}(a)\xi(s)\) and \((\lambda_g\xi)(s)=\xi(g^{-1}s)\). Then
\(\lambda_g\pi(a)\lambda_g^*=\pi(\alpha_g(a))\); up to isomorphism the crossed product does not depend on the
faithful normal representation of \(N\); there is a faithful normal conditional expectation \(F\) onto \(\pi(N)\) with
\(F(\pi(a)\lambda_g)=0\) for \(g\ne e\), and \(x=0\) whenever \(F(x\lambda_g^*)=0\) for all \(g\); and the linear span of the \(\pi(a)\lambda_g\) is a \(\sigma\)-weakly dense
\(*\)-subalgebra. The construction, covariance and independence of the representation are proved in Changing
the Hilbert space of a regular crossed product, OA-FLOW.REG.CONSTRUCTION and OA-FLOW.REG.INDEPENDENCE.
The expectation \(F\) is constructed in The coefficient algebra as the value space of a weight,
OA-FLOW.OVW.DISCRETE, where also \(F(y)=\pi(V_e^*yV_e)\) with
\(V_e\eta=\delta_e\otimes\eta\). Since \(F(\lambda_h^*y\lambda_h)=\lambda_h^*F(y)\lambda_h\) (check it on the elements
\(\pi(a)\lambda_g\) and use normality), the entry \(V_e^*\lambda_h^*x\lambda_kV_e\) of \(x\) is
\(\alpha_{h^{-1}}(\pi^{-1}(F(x\lambda_{hk^{-1}}^*)))\), which gives the statement about \(F(x\lambda_g^*)\).

**(B9) Discrete decompositions.** Let \(M\) be a factor with separable predual.
- (a) If \(M\) is of type III\(_\lambda\), \(0<\lambda<1\), there are a factor \(N\) of type II∞ with separable predual,
  a faithful normal semifinite trace \(\tau\) on \(N\) and \(\theta\in\operatorname{Aut}N\) with
  \(\tau\circ\theta=\lambda\tau\), such that \(M\cong N\rtimes_\theta\mathbb Z\). [Connes 1973, Théorème 4.4.1]
- (b) If \(M\) is of type III₀, there are a von Neumann algebra \(N\) of type II∞ with separable predual and diffuse
  centre and \(\theta\in\operatorname{Aut}N\) such that \(M\cong N\rtimes_\theta\mathbb Z\) (a *discrete
  decomposition* of \(M\)). [Connes 1973, Théorème 5.3.1]
- (c) If \(M\) is of type III₁, \(\varphi\) is a faithful normal state on \(M\) and \(T>0\), then
  \(P=M\rtimes_{\sigma^\varphi_T}\mathbb Z\) is a factor, and its invariant \(T(P)\), the set of \(t\in\mathbb R\) for
  which the modular automorphism \(\sigma^\psi_t\) of a faithful normal state \(\psi\) on \(P\) is inner, equals
  \(T\mathbb Z\). Consequently \(P\) is of type III\(_\lambda\) with \(\lambda=e^{-2\pi/T}\), or of type III₀.
  [Connes 1973, proof of Corollaire 1.5.8, and Théorème 3.4.1]

**(B10) Automorphisms of \(R_{0,1}\).** For \(\theta\in\operatorname{Aut}R_{0,1}\) the trace-scaling number
\(\operatorname{mod}\theta\) is defined in Section 8. If two automorphisms of \(R_{0,1}\) have the same module
\(\lambda\in\,]0,1[\), they are outer conjugate. [Connes 1975b, Corollary 6]

**(B11) Krieger factors and the flow of weights.** A *Krieger factor* is a crossed product \(L^\infty(X,\mu)\rtimes_T
\mathbb Z\), where \(T\) is an ergodic nonsingular automorphism of a nonatomic standard probability space.
- (a) Krieger factors are approximately finite dimensional. (A crossed product of an injective von Neumann algebra
  by an action of an amenable group, here \(\mathbb Z\), is injective, and an injective von Neumann algebra with
  separable predual is approximately finite dimensional.) The first statement is Injective von Neumann algebras,
Section 5; the second is (B13).
- (b) Let \(M\) be a factor of type III₀ with separable predual and \(M\cong N\rtimes_\theta\mathbb Z\) a discrete
  decomposition as in (B9)(b). If \(N\cong Z(N)\mathbin{\bar\otimes}R_{0,1}\), then \(M\) is a Krieger factor.
  [Connes 1975a]
- (c) Every factor \(M\) of type III with separable predual has a *flow of weights*: an ergodic flow on a standard
  measure space, built from the centre of the crossed product of \(M\) by a modular automorphism group. Its isomorphism
  class is an isomorphism invariant of \(M\). The flow of weights is not transitive exactly when \(M\) is of type
  III₀. The flow of weights and its invariance are constructed in Building an intrinsic flow from modular
coordinates; for the characterization of type III₀ see [Connes–Takesaki 1977].
- (d) Krieger factors with isomorphic flows of weights are isomorphic, and conversely. Every ergodic flow that is not
  transitive is the flow of weights of a Krieger factor of type III₀. This theorem is due to Krieger; it is stated in
[Connes 1976, Theorem 4.5.1], and the flow of weights is constructed in [Connes–Takesaki 1977].

**(B12) Injective factors of type III₁.** Every injective factor of type III₁ with separable predual is isomorphic
to \(R_\infty\). The proof combines a reduction to the triviality of the bicentralizer of a faithful normal state
[Connes 1985] with a proof that this bicentralizer is trivial for injective factors of type III₁ [Haagerup 1987].

**(B13) Approximate finite dimensionality is local.** If \(Q\) is a von Neumann algebra on a separable Hilbert space
and almost every factor in its central decomposition is approximately finite dimensional, then \(Q\) is approximately
finite dimensional. (Those factors are injective, by Theorem 11.1. So each central summand of \(Q\) over which the
fibres have constant dimension is injective, by Theorem 1.1(d), as in the proof of Corollary 11.2, and \(Q\) is
injective by Lemma 2.2(d). Finally, an injective von Neumann algebra with separable predual is approximately finite
dimensional.) The last step, injective implies approximately finite dimensional for separable predual, is proved
for every von Neumann algebra in the course *Positive maps and finite-dimensional approximation*:
Injective algebras and separable tracial envelopes, Theorem 3.1.

**(B14) Groups.** A countable group \(\Gamma\) is *amenable* if there is a left-invariant mean on
\(\ell^\infty(\Gamma)\); equivalently, it has a *Følner sequence*: finite sets \(F_n\) with \(|gF_n\,\triangle\,F_n|/
|F_n|\to0\) for every \(g\). Abelian groups, and more generally solvable locally compact groups, are amenable. For
the left and right regular representations \(\lambda,\rho\) of a locally compact group, \(\lambda(G)'=\rho(G)''\) and
\(\rho\) is unitarily equivalent to \(\lambda\). For a countable group \(\Gamma\), \(\tau(x)=\langle x\delta_e,\delta_e
\rangle\) is a faithful normal tracial state on \(L(\Gamma)=\lambda(\Gamma)''\), and \(\delta_e\) is cyclic and
separating. Abelian groups are amenable, and extensions of amenable groups by amenable closed normal subgroups are
amenable, by Amenability and the equality of full and reduced crossed products;
induction along a derived series gives solvable groups. For the Følner condition see [Namioka 1964] and [Connes 1976, §2.1]; for group von Neumann algebras of
discrete groups see [Anantharaman–Popa, §1.3].

**(B15) Regular representations of connected groups.** For a second countable connected locally compact group
\(G\), the von
Neumann algebra \(\lambda(G)''\) is semifinite, and almost every factor in its central decomposition is of type I or
of type II∞. [Dixmier 1969], [Connes 1976, Corollary 4.3.2]

## 1. What we use from the other lessons

**Injective von Neumann algebras.** From the lesson "Injective von Neumann algebras" of this course we use the
following facts. A von Neumann algebra is injective when it is injective in the category of unital C\*-algebras with
ucp maps.

**Theorem 1.1.** Let \(M\subset B(H)\) be a von Neumann algebra.
- (a) \(M\) is injective if and only if there is a projection of norm one from \(B(H)\) onto \(M\). In particular
  injectivity does not depend on the faithful representation. (Theorem 2.1 and Corollary 2.2(a) there.)
- (b) \(M\) is injective if and only if \(M'\) is injective. (Theorem 4.2 there.)
- (c) If every algebra in an increasing family of von Neumann algebras is injective, then the \(\sigma\)-weak closure
  of their union is injective. (Theorem 4.3(b) there.)
- (d) If \(M=\int^\oplus_XM(x)\,d\mu(x)\) is a direct integral over a standard probability space, with \(x\mapsto
  M(x)\) a measurable field of von Neumann algebras on a fixed separable Hilbert space, then \(M\) is injective if and
  only if \(M(x)\) is injective for almost every \(x\). (Theorem 6.4 there.)
- (e) If \(M\) is generated by an injective von Neumann subalgebra \(N\) and a group \(\mathcal G\) of unitaries that
  normalize \(N\), and \(\mathcal G\) is amenable as a discrete group, then \(M\) is injective. (Theorem 5.1 there.)
- (f) If \(\pi\) is a strongly continuous unitary representation of an amenable locally compact group \(G\), then
  \(\pi(G)''\) and \(\pi(G)'\) are injective. (Corollary 5.3 there.)
- (g) If \(\pi\) is a strongly continuous unitary representation, on a separable Hilbert space, of a locally compact
  group \(G\) whose quotient \(G/G_0\) by the identity component is amenable, for instance a connected group, then
  \(\pi(G)''\) and \(\pi(G)'\) are injective. (Theorem 7.1 and Corollary 7.5 there; the proof there quotes the
  Gleason–Yamabe theorem and two results of Dixmier on Lie groups.)

**The injective II₁ factor.** From the lesson "Uniqueness of the injective II₁ factor" we use one implication of its
main theorem, (d)⇒(a) of Theorem 1.5 there, where a state as below is called a hypertrace (Definition 1.1 there).

**Theorem 1.2.** Let \(N\) be a II₁ factor with separable predual, in standard form on \(H=L^2(N,\tau)\). If
there is a state \(\varphi\) on \(B(H)\) such that \(\varphi(uxu^*)=\varphi(x)\) for all \(x\in B(H)\) and
\(u\in\mathcal U(N)\), then \(N\) is isomorphic to \(R\).

**Recognizing a crossed product.** From Course 1 we use Lemma 8.1 of the lesson "Full factors without almost periodic
weights".

**Lemma 1.3.** Let \(B\) be a von Neumann algebra, \(Q\subset B\) a von Neumann subalgebra with a faithful normal
state, and \(g\mapsto v_g\) a unitary representation of a countable group \(\Gamma\) in \(B\) with
\(v_gQv_g^*=Q\); put \(\alpha_g=\operatorname{Ad}v_g|_Q\). Suppose \(B\) is generated by \(Q\) and the \(v_g\), and there
is a faithful normal conditional expectation \(F:B\to Q\) with \(F(v_g)=0\) for \(g\ne e\). Then there is an
isomorphism \(B\cong Q\rtimes_\alpha\Gamma\) sending \(q\) to \(\pi(q)\) and \(v_g\) to \(\lambda_g\).

## 2. Approximation properties and the model factors

References for this section are [Connes 1976, §4] and [Anantharaman–Popa, Chapters 10–11].

**Definition 2.1.** Let \(M\subset B(H)\) be a von Neumann algebra with separable predual.
- (a) \(M\) is *approximately finite dimensional* (AFD) if \(M\) contains finite-dimensional \(*\)-subalgebras
  \(G_1\subset G_2\subset\cdots\), each containing \(1\), whose union is \(\sigma\)-weakly dense.
- (b) \(M\) is *semidiscrete* if there are a net of finite-dimensional C\*-algebras \(D_i\) and normal ucp maps
  \(\alpha_i:M\to D_i\), \(\beta_i:D_i\to M\) with \(\beta_i(\alpha_i(x))\to x\) \(\sigma\)-weakly for every \(x\in M\).
- (c) For \(T\in B(H)\) let \(K_T\) be the weakly closed convex hull of \(\{uTu^*:u\in\mathcal U(M)\}\). \(M\) has
  *property P* (on \(H\)) if \(K_T\cap M'\ne\emptyset\) for every \(T\in B(H)\).

For a II₁ factor, "AFD" is the classical notion of hyperfiniteness. For infinite algebras the word "hyperfinite" is
sometimes used for other things, so we keep "approximately finite dimensional". Properties (a), (b) and injectivity are
properties of the abstract algebra; property P refers to the representation, and Section 3 shows it is independent of
it for AFD algebras.

**Lemma 2.2 (building injective algebras).**
- (a) Every finite-dimensional von Neumann algebra is injective.
- (b) Abelian von Neumann algebras are injective.
- (c) If \(Z\) is abelian and \(Q\) injective, then \(Z\mathbin{\bar\otimes}Q\) is injective.
- (d) If every summand of a direct sum of von Neumann algebras is injective, so is the sum.
- (e) If \(M\) is injective and \(e\in M\) is a projection, then \(eMe\) is injective.
- (f) If \(M\) is injective and \(E:M\to N\) is a conditional expectation (a projection of norm one) onto a von Neumann
  subalgebra, then \(N\) is injective.

**Proof.** (a) Let \(F\subset B(H)\) be finite dimensional. Its unitary group \(\mathcal U(F)\) is compact; let \(du\)
be its normalized Haar measure. For \(T\in B(H)\) put \(P(T)=\int_{\mathcal U(F)}uTu^*\,du\) (a weak integral). By
invariance of Haar measure \(vP(T)v^*=P(T)\) for \(v\in\mathcal U(F)\), and the unitaries span \(F\), so
\(P(T)\in F'\). Clearly \(\|P(T)\|\le\|T\|\) and \(P(T)=T\) for \(T\in F'\). So \(F'\) is injective by Theorem
1.1(a), and \(F\) is injective by Theorem 1.1(b).

(b) An abelian \(A\) is generated by the injective algebra \(\mathbb C1\) and the group \(\mathcal U(A)\), which is
abelian, hence amenable as a discrete group (B14), and normalizes \(\mathbb C1\). Apply Theorem 1.1(e).

(c) \(Z\mathbin{\bar\otimes}Q\) is generated by \(1\otimes Q\cong Q\), which is injective, and the abelian group
\(\mathcal U(Z)\otimes1\), which commutes with \(1\otimes Q\). Apply Theorem 1.1(e).

(d) Let \(M_i\subset B(H_i)\) be injective with projections of norm one \(E_i\), and \(p_i\) the projection of
\(H=\bigoplus H_i\) onto \(H_i\). Then \(E(T)=\bigoplus_iE_i(p_iTp_i)\) is a projection of norm one from \(B(H)\) onto
\(\bigoplus M_i\).

(e) Let \(E:B(H)\to M\) have norm one. By Tomiyama's theorem (B1), \(E(eTe)=eE(T)e\). So the restriction of \(E\) to
\(B(eH)=eB(H)e\) is a projection of norm one onto \(eMe\).

(f) If \(E_M:B(H)\to M\) has norm one, then \(E\circ E_M\) is a projection of norm one onto \(N\). \(\square\)

**Proposition 2.3 (invariant filtrations).** Let \(M\) be a von Neumann algebra with a faithful normal state
\(\varphi\), and \(G_1\subset G_2\subset\cdots\) finite-dimensional \(*\)-subalgebras containing \(1\), with
\(\sigma\)-weakly dense union and \(\sigma^\varphi_t(G_n)=G_n\) for all \(n,t\). Let \(E_n\) be the
\(\varphi\)-preserving conditional expectation onto \(G_n\) (B2). Then \(E_n(x)\to x\) \(\sigma\)-strongly for every
\(x\in M\). Hence \(M\) is AFD, semidiscrete and injective.

**Proof.** Work in the standard representation on \(L^2(M,\varphi)\), with cyclic and separating vector \(\xi\). For
\(y\in G_n\), \(\langle E_n(x)\xi,y\xi\rangle=\varphi(y^*E_n(x))=\varphi(E_n(y^*x))=\varphi(y^*x)=\langle x\xi,y\xi
\rangle\). So \(E_n(x)\xi=P_nx\xi\), where \(P_n\) is the orthogonal projection onto the finite-dimensional space
\(G_n\xi\). The \(P_n\) increase, and their supremum is the projection onto the closure of \(\bigcup_nG_n\xi\), which is
all of \(L^2(M,\varphi)\) because \(\bigcup_nG_n\) is strongly dense in \(M\) (Kaplansky) and \(M\xi\) is dense. So
\(\|E_n(x)-x\|_\varphi=\|(P_n-1)x\xi\|\to0\), and by (B3) \(E_n(x)\to x\) \(\sigma\)-strongly, since
\(\|E_n(x)\|\le\|x\|\).

\(M\) is AFD by definition. With \(D_n=G_n\), \(\alpha_n=E_n\) and \(\beta_n\) the inclusion, \(M\) is semidiscrete.
Each \(G_n\) is injective (Lemma 2.2(a)), so \(M\) is injective by Theorem 1.1(c). \(\square\)

**Example 2.4 (the model factors).** Proposition 2.3 applies to the following factors, which are therefore AFD,
semidiscrete and injective.
- \(B(K)\), \(K\) separable infinite dimensional, with orthonormal basis \((e_k)\): let \(\omega\) be the state with
  density \(\operatorname{diag}(2^{-k})\), \(p_n\) the projection onto the span of \(e_1,\dots,e_n\), and \(G_n=
  p_nB(K)p_n+\mathbb C(1-p_n)\). The modular group \(\operatorname{Ad}\operatorname{diag}(2^{-ikt})\) preserves
  \(G_n\), and \(G_n\subset G_{n+1}\) because \(1-p_n=(p_{n+1}-p_n)+(1-p_{n+1})\).
- \(R=\bigotimes_n(M_2,\omega_1)\) with \(G_n=M_2^{\otimes n}\otimes1\) and the trace (B7).
- \(R_{0,1}=R\mathbin{\bar\otimes}B(\ell^2)\) with the state \(\tau\otimes\omega\) and \(G_n=(M_2^{\otimes n}\otimes1)
  \otimes(p_nB(\ell^2)p_n+\mathbb C(1-p_n))\). It is a factor of type II∞.
- \(R_\lambda\) and \(R_\infty\) with the product states and \(G_n=M_2^{\otimes n}\otimes1\) (B7).

**Lemma 2.5 (composing approximations).** Let \(M\) be a von Neumann algebra, and suppose there are a net of
semidiscrete von Neumann algebras \(B_j\) and normal ucp maps \(\Phi_j:M\to B_j\), \(\Psi_j:B_j\to M\) with
\(\Psi_j\Phi_j(x)\to x\) \(\sigma\)-weakly for all \(x\in M\). Then \(M\) is semidiscrete.

**Proof.** Index a net by triples \(\iota=(S,W,\varepsilon)\), with \(S\subset M\) and \(W\subset M_*\) finite and
\(\varepsilon>0\), ordered in the obvious way. Given \(\iota\), choose \(j\) with
\(|\omega(\Psi_j\Phi_j(x)-x)|<\varepsilon/2\) for \(x\in S\), \(\omega\in W\). The functionals \(\omega\circ\Psi_j\) are
normal on \(B_j\). By semidiscreteness of \(B_j\) choose \(\alpha:B_j\to D\), \(\beta:D\to B_j\) with
\(|\omega\Psi_j(\beta\alpha(y)-y)|<\varepsilon/2\) for \(y\in\Phi_j(S)\), \(\omega\in W\). Then
\(\alpha_\iota=\alpha\Phi_j\) and \(\beta_\iota=\Psi_j\beta\) are normal ucp, factor through \(D\), and satisfy
\(|\omega(\beta_\iota\alpha_\iota(x)-x)|<\varepsilon\) for \(x\in S\), \(\omega\in W\). \(\square\)

**Proposition 2.6 (crossed products by amenable groups).** Let \(A\) be an abelian von Neumann algebra with separable
predual, and \(\alpha\) an action of a countable amenable group \(\Gamma\) on \(A\). Then \(M=A\rtimes_\alpha\Gamma\)
is semidiscrete.

**Proof.** Represent \(A\) on \(H\) and \(M\) on \(\ell^2(\Gamma,H)\) as in (B8). For a finite set \(F\subset\Gamma\)
let \(V_t:H\to\ell^2(\Gamma,H)\) (\(t\in F\)) put a vector at the point \(t\), and let \(\Phi_F(x)=(V_s^*xV_t)_{s,t\in
F}\in M_F(B(H))\). From (B8),
\[
V_s^*\pi(a)\lambda_gV_t=\delta_{s,gt}\,\alpha_{s^{-1}}(a),\tag{2.1}
\]
so \(\Phi_F\) maps the dense \(*\)-algebra spanned by the \(\pi(a)\lambda_g\) into \(M_F(A)=M_F\otimes A\). As
\(\Phi_F\) is a compression, it is normal and ucp, and by continuity \(\Phi_F(M)\subset M_F(A)\). Define
\(\Psi_F:M_F(A)\to M\) by
\[
\Psi_F\big((b_{st})\big)=\frac1{|F|}\sum_{s,t\in F}\lambda_s\pi(b_{st})\lambda_t^*.
\]
It is \(|F|^{-1}\) times the compression of the normal \(*\)-homomorphism \((b_{st})\mapsto(\pi(b_{st}))\) by the row
operator \((\lambda_s)_{s\in F}\), so it is normal and completely positive, and \(\Psi_F(1)=|F|^{-1}\sum_s\lambda_s
\lambda_s^*=1\). By (2.1),
\[
\Psi_F\Phi_F(\pi(a)\lambda_g)=\frac1{|F|}\sum_{t\in F\cap g^{-1}F}\lambda_{gt}\pi(\alpha_{(gt)^{-1}}(a))\lambda_t^*
=\frac{|F\cap g^{-1}F|}{|F|}\,\pi(a)\lambda_g,\tag{2.2}
\]
using \(\lambda_s\pi(b)\lambda_s^*=\pi(\alpha_s(b))\).

Let \(\psi\) be a faithful normal state on \(A\) and \(\varphi=\psi\circ\pi^{-1}\circ F\), with \(F\) the canonical
expectation; \(\varphi\) is a faithful normal state on \(M\). By (2.2), \(\varphi\circ\Psi_F\Phi_F=\varphi\) on the
dense span, hence everywhere. By Kadison–Schwarz, \(\|\Psi_F\Phi_F(x)\|_\varphi^2\le\varphi(\Psi_F\Phi_F(x^*x))=
\|x\|_\varphi^2\). Now let \((F_n)\) be a Følner sequence and \(x\in M\). Given \(\varepsilon>0\), Kaplansky's theorem
gives \(y\) in the span of the \(\pi(a)\lambda_g\) with \(\|x-y\|_\varphi<\varepsilon\). By (2.2) and the Følner
property, \(\|\Psi_{F_n}\Phi_{F_n}(y)-y\|_\varphi\to0\). Hence
\[
\limsup_n\|\Psi_{F_n}\Phi_{F_n}(x)-x\|_\varphi\le\limsup_n\big(\|\Psi_{F_n}\Phi_{F_n}(x-y)\|_\varphi+
\|\Psi_{F_n}\Phi_{F_n}(y)-y\|_\varphi+\|y-x\|_\varphi\big)\le2\varepsilon.
\]
So \(\Psi_{F_n}\Phi_{F_n}(x)\to x\) \(\sigma\)-strongly (B3).

Finally \(M_F(A)\) is semidiscrete. Indeed \(A\) is generated by countably many projections (its predual is
separable), and the finite-dimensional algebras \(A_k\) generated by the first \(k\) of them increase and have dense
union. The algebras \(M_F\otimes A_k\) are invariant under the modular group of the tracial state
\(\operatorname{tr}\otimes\psi\), which is trivial, so Proposition 2.3 applies. Lemma 2.5 finishes the proof. \(\square\)

**Definition 2.7.** Let \(T\) be a nonsingular automorphism of a standard probability space \((X,\mu)\), acting on
\(A=L^\infty(X,\mu)\) by \(\alpha(f)=f\circ T^{-1}\). \(T\) is *ergodic* if the only \(T\)-invariant functions are the
constants, and *aperiodic* if for each \(n\ne0\) the set of fixed points of \(T^n\) is null.

**Proposition 2.8.** Let \(T\) be ergodic and \(\mu\) nonatomic. Then \(T\) is aperiodic, and the Krieger factor
\(M=A\rtimes_\alpha\mathbb Z\) is a factor. It is semidiscrete and injective.

**Proof.** *Aperiodicity.* Suppose that for some \(n\ge1\) the set of fixed points of \(T^n\) is not null. It is
\(T\)-invariant, so by ergodicity it is conull, and \(T^n=\operatorname{id}\) almost everywhere. Then
\(\nu=\frac1n\sum_{k=0}^{n-1}\mu\circ T^{-k}\) is a \(T\)-invariant probability measure equivalent to \(\mu\), and it is
nonatomic. Choose a Borel set \(B\) with \(0<\nu(B)<1/n\). The set \(C=\bigcup_{k=0}^{n-1}T^kB\) is \(T\)-invariant up to
a null set (as \(T^nB=B\) almost everywhere), and \(0<\nu(B)\le\nu(C)\le n\nu(B)<1\). This contradicts ergodicity.

*Factoriality.* Let \(F\) be the canonical expectation of \(M\) onto \(\pi(A)\) and \(z\in Z(M)\). Put
\(\pi(a_n)=F(z\lambda_n^*)\). For \(f\in A\), using \(\pi(f)\lambda_n^*=\lambda_n^*\pi(\alpha^n(f))\) and the
bimodule property,
\[
\pi(fa_n)=F(\pi(f)z\lambda_n^*)=F(z\pi(f)\lambda_n^*)=F(z\lambda_n^*\pi(\alpha^n(f)))=\pi(a_n\alpha^n(f)),
\]
where \(\alpha^n(f)=f\circ T^{-n}\). Fix \(n\ne0\) and let \(S=T^n\). Choose a Polish topology compatible with the Borel
structure and a countable base \((W_j)\). For each point \(x\) with \(Sx\ne x\) there are disjoint basic sets
\(W_j\ni x\), \(W_l\ni Sx\); the sets \(B_{jl}=W_j\cap S^{-1}W_l\) with \(W_j\cap W_l=\emptyset\) are countably many,
cover the non-fixed points of \(S\) (a conull set, by aperiodicity), and satisfy \(SB_{jl}\cap B_{jl}=\emptyset\). With
\(f=1_{B_{jl}}\) we have \(\alpha^n(f)=1_{SB_{jl}}\), and multiplying \(fa_n=a_n\alpha^n(f)\) by \(1_{B_{jl}}\) gives
\(a_n1_{B_{jl}}=0\). Hence \(a_n=0\) for \(n\ne0\). So \(F((z-\pi(a_0))\lambda_n^*)=0\) for all \(n\), and \(z=\pi(a_0)\)
by (B8). Commuting with \(\lambda_1\) gives \(\alpha(a_0)=a_0\), so \(a_0\) is constant by ergodicity.

Semidiscreteness is Proposition 2.6 with \(\Gamma=\mathbb Z\); injectivity follows from Theorem 1.1(e), or from
Proposition 3.3 below. \(\square\)

## 3. From approximation to injectivity

**Proposition 3.1.** An AFD von Neumann algebra \(M\subset B(H)\) has property P on every Hilbert space on which it
acts.

**Proof.** Let \(G_n\) be as in Definition 2.1(a) and \(T\in B(H)\). Put \(S_n=\int_{\mathcal U(G_n)}uTu^*\,du\)
(normalized Haar measure). As in Lemma 2.2(a), \(S_n\in G_n'\). Also \(S_n\in K_T\): otherwise the Hahn–Banach theorem
gives a weakly continuous functional \(\omega\) and \(c\in\mathbb R\) with \(\operatorname{Re}\omega(S_n)>c\ge
\operatorname{Re}\omega(S)\) for \(S\in K_T\), while \(\operatorname{Re}\omega(S_n)=\int\operatorname{Re}\omega(uTu^*)
\,du\le c\). The set \(K_T\) is bounded and weakly closed, hence weakly compact; let \(S\) be a weak cluster point of
\((S_n)\). For \(m\ge n\), \(S_m\in G_m'\subset G_n'\), and \(G_n'\) is weakly closed, so \(S\in G_n'\) for all \(n\).
Hence \(S\in(\bigcup_nG_n)'=M'\), and \(S\in K_T\cap M'\). \(\square\)

**Proposition 3.2.** If \(M\subset B(H)\) has property P, there is a projection of norm one from \(B(H)\) onto \(M'\).
Consequently \(M'\) and \(M\) are injective.

**Proof.** Let \(\mathcal C_0\) be the convex hull of the maps \(\operatorname{Ad}u\), \(u\in\mathcal U(M)\), acting
on \(B(H)\). Each \(\Phi\in\mathcal C_0\) sends \(T\) into \(K_T\). Consider \(\prod_{T\in B(H)}K_T\) with the product of
the weak topologies; it is compact. Let \(\mathcal C\) be the closure of \(\mathcal C_0\) in it. Its elements are maps
\(\Phi\) with \(\Phi(T)\in K_T\); they are linear, satisfy \(\|\Phi(T)\|\le\|T\|\), and fix every element of \(M'\)
(because \(K_S=\{S\}\) for \(S\in M'\)).

*Step 1: if \(\Phi\in\mathcal C\) and \(\Psi\in\mathcal C_0\), then \(\Psi\circ\Phi\in\mathcal C\).* Write \(\Phi\) as
a pointwise weak limit of \(\Phi_\beta\in\mathcal C_0\). Each \(\operatorname{Ad}u\) is weakly continuous, hence so is
\(\Psi\), and \(\Psi\circ\Phi_\beta\to\Psi\circ\Phi\) pointwise weakly. Since \(\Psi\circ\Phi_\beta\in\mathcal C_0\)
(because \(\operatorname{Ad}u\circ\operatorname{Ad}v=\operatorname{Ad}uv\)), the claim follows.

*Step 2: for every finite set \(T_1,\dots,T_k\in B(H)\), some \(\Phi\in\mathcal C\) has \(\Phi(T_j)\in M'\) for all
\(j\).* Induction on \(k\), starting with \(\Phi_0=\operatorname{id}\). Suppose \(\Phi_{k-1}\in\mathcal C\) maps
\(T_1,\dots,T_{k-1}\) into \(M'\). By property P applied to \(\Phi_{k-1}(T_k)\), there is a net \(\Psi_\gamma\in
\mathcal C_0\) with \(\Psi_\gamma(\Phi_{k-1}(T_k))\to S\in M'\) weakly. By Step 1, \(\Psi_\gamma\circ\Phi_{k-1}\in
\mathcal C\); let \(\Phi_k\) be a cluster point in \(\mathcal C\). Then \(\Phi_k(T_k)=S\in M'\), and
\(\Phi_k(T_j)=\Phi_{k-1}(T_j)\) for \(j<k\), since \(\Psi_\gamma\) fixes elements of \(M'\).

*Step 3.* The sets \(\mathcal C_T=\{\Phi\in\mathcal C:\Phi(T)\in M'\}\) are closed (because \(M'\) is weakly closed),
and by Step 2 they have the finite intersection property. By compactness some \(\Phi\) lies in all of them. Then
\(\Phi\) is a linear map from \(B(H)\) into \(M'\), of norm at most one, equal to the identity on \(M'\): a projection
of norm one. So \(M'\) is injective, and so is \(M\) by Theorem 1.1(b). \(\square\)

**Proposition 3.3.** A semidiscrete von Neumann algebra is injective.

**Proof.** Let \(M\subset B(H)\), and \(\alpha_i,\beta_i,D_i\) as in Definition 2.1(b). Embed \(D_i\) unitally in some
\(M_{n_i}\), with a ucp projection \(P_i:M_{n_i}\to D_i\) (B1). By Arveson's extension theorem, \(\alpha_i\) extends to
a completely positive map \(\tilde\alpha_i:B(H)\to M_{n_i}\) with \(\tilde\alpha_i(1)=1\). Then
\(\Theta_i=\beta_iP_i\tilde\alpha_i:B(H)\to M\) is ucp, and \(\Theta_i(x)=\beta_i\alpha_i(x)\) for \(x\in M\). The product
\(\prod_{T\in B(H)}\{y\in M:\|y\|\le\|T\|\}\), each factor with the \(\sigma\)-weak topology, is compact, and contains
every \(\Theta_i\); let \(\Theta\) be a cluster point of \((\Theta_i)\) in it. It is a linear map
\(B(H)\to M\) of norm at most one, and \(\Theta(x)=\lim\beta_i\alpha_i(x)=x\) for \(x\in M\). \(\square\)

**Proposition 3.4.** Let \(P\) be semidiscrete and \(M\subset P\) a von Neumann subalgebra with a normal conditional
expectation \(E:P\to M\). Then \(M\) is semidiscrete.

**Proof.** If \(\beta_i\alpha_i\to\operatorname{id}_P\) pointwise \(\sigma\)-weakly, then the maps
\(\alpha_i|_M\) and \(E\circ\beta_i\) are normal ucp, and \(E\beta_i\alpha_i(x)\to E(x)=x\) for \(x\in M\), since \(E\)
is normal. \(\square\)

## 4. Injective factors of type II

A reference for this section is [Connes 1976, §4.2–§4.3].

**Theorem 4.1.** A II₁ factor \(N\) with separable predual is injective exactly when it is isomorphic to the
hyperfinite factor \(R\).

**Proof.** \(R\) is injective by Example 2.4. Conversely, let \(N\) be injective. Represent \(N\) standardly on
\(H=L^2(N,\tau)\); it is still injective (Theorem 1.1(a)), so there is a projection of norm one \(E:B(H)\to N\). By
Tomiyama's theorem, \(E\) is positive and \(N\)-bimodular. Put \(\varphi=\tau\circ E\). It is a state, and for
\(u\in\mathcal U(N)\), \(x\in B(H)\),
\[
\varphi(uxu^*)=\tau(uE(x)u^*)=\tau(E(x))=\varphi(x).
\]
Theorem 1.2 gives \(N\cong R\). \(\square\)

The state \(\varphi\) is a *hypertrace*: it extends the trace of \(N\) to all of \(B(H)\), keeping invariance under
the unitaries of \(N\). So an infinite-dimensional factor is \(R\) exactly when it acts standardly with a hypertrace.

**Corollary 4.2 (subfactors of \(R\)).** Let \(Q\subset R\) be a von Neumann subalgebra that is a factor, possibly with
a unit \(p\ne1\). Then \(Q\) is isomorphic to some \(M_n\), \(n<\infty\), or to \(R\). In particular every nonzero
corner \(pRp\) is isomorphic to \(R\).

**Proof.** First let \(p=1\). Let \(\tau\) be the trace of \(R\). By (B2) there is a \(\tau\)-preserving conditional
expectation \(R\to Q\), so \(Q\) is injective (Lemma 2.2(f)). The restriction of \(\tau\) is a faithful normal tracial
state on \(Q\), so \(Q\) is finite; its predual is a quotient of that of \(R\), hence separable. By (B4), \(Q\) is of
type I\(_n\) with \(n<\infty\), so \(Q\cong M_n\), or of type II₁, so \(Q\cong R\) by Theorem 4.1. For general \(p\),
\(pRp\) is a II₁ factor, injective by Lemma 2.2(e), hence isomorphic to \(R\); apply the first case inside \(pRp\).
\(\square\)

**Theorem 4.3.** A II∞ factor \(M\) with separable predual is injective exactly when \(M\cong R_{0,1}\). In
particular every AFD factor of type II∞ is isomorphic to \(R_{0,1}\).

**Proof.** \(R_{0,1}\) is injective and AFD by Example 2.4. Conversely let \(M\) be injective, and \(e\ne0\) a finite
projection of \(M\). Then \(eMe\) is a II₁ factor with separable predual, injective by Lemma 2.2(e), so
\(eMe\cong R\) by Theorem 4.1. By (B4), \(M\cong eMe\mathbin{\bar\otimes}B(\ell^2)\cong R_{0,1}\). An AFD factor is
injective (Proposition 2.3's last step: Lemma 2.2(a) and Theorem 1.1(c)), so the last claim follows. \(\square\)

**Example 4.4.** \(R\mathbin{\bar\otimes}R\cong R\): it is a II₁ factor with separable predual, and it is AFD (use
\(G_n\otimes G_n\)), hence injective. Likewise \(R_{0,1}\mathbin{\bar\otimes}R\cong R_{0,1}\) and
\(R\mathbin{\bar\otimes}M_n\cong R\). None of these isomorphisms needs to be written down by hand.

## 5. Group von Neumann algebras

For a countable group \(\Gamma\), \(L(\Gamma)=\lambda(\Gamma)''\subset B(\ell^2(\Gamma))\), with trace \(\tau\) as in
(B14). A group is *ICC* if it is nontrivial and every conjugacy class other than \(\{e\}\) is infinite.

**Proposition 5.1.** \(L(\Gamma)\) is injective if and only if \(\Gamma\) is amenable.

**Proof.** If \(\Gamma\) is amenable, \(L(\Gamma)\) is generated by \(\mathbb C1\) and the amenable group
\(\lambda(\Gamma)\), so it is injective by Theorem 1.1(e).

Conversely, let \(E:B(\ell^2(\Gamma))\to L(\Gamma)\) be a projection of norm one; it is positive and
\(L(\Gamma)\)-bimodular by Tomiyama's theorem. For \(f\in\ell^\infty(\Gamma)\) let \(m_f\) be the multiplication
operator, and put \(m(f)=\tau(E(m_f))\). Then \(m\) is a positive linear functional with \(m(1)=1\), a mean. A direct
computation gives \(\lambda_gm_f\lambda_g^*=m_{g\cdot f}\) with \((g\cdot f)(s)=f(g^{-1}s)\). Hence
\[
m(g\cdot f)=\tau(E(\lambda_gm_f\lambda_g^*))=\tau(\lambda_gE(m_f)\lambda_g^*)=\tau(E(m_f))=m(f),
\]
and \(m\) is left invariant. \(\square\)

**Theorem 5.2.** Let \(\Gamma\) be an ICC group. Then \(L(\Gamma)\) is a II₁ factor, and \(L(\Gamma)\cong R\) exactly
when \(\Gamma\) is amenable.

**Proof.** Let \(z\in Z(L(\Gamma))\) and write \(z\delta_e=\sum_gc_g\delta_g\in\ell^2(\Gamma)\). Since
\(L(\Gamma)\subset\rho(\Gamma)'\), \(z\) commutes with \(\lambda_h\) and \(\rho_h\), where \((\rho_h\xi)(s)=\xi(sh)\).
As \(\lambda_h\rho_h\delta_g=\delta_{hgh^{-1}}\), we get \(z\delta_e=z\lambda_h\rho_h\delta_e=\lambda_h\rho_hz\delta_e\),
so \(c_{hgh^{-1}}=c_g\): the coefficients are constant on conjugacy classes. Being square summable, they vanish on
infinite classes, so \(z\delta_e=c_e\delta_e\), and since \(\delta_e\) is separating, \(z=c_e1\). So \(L(\Gamma)\) is
a factor. It has a faithful normal tracial state and is infinite dimensional (the \(\lambda_g\) are linearly
independent and \(\Gamma\) is infinite), so it is of type II₁, with separable predual. By Theorem 4.1 and
Proposition 5.1, \(L(\Gamma)\cong R\) if and only if \(\Gamma\) is amenable. \(\square\)

**Example 5.3.** (a) The group \(S_\infty\) of permutations of \(\mathbb N\) moving finitely many points is ICC and
locally finite, hence amenable: \(L(S_\infty)\cong R\). (b) The free group \(\mathbb F_2\) is ICC and not amenable:
\(L(\mathbb F_2)\) is a II₁ factor that is not injective, hence not isomorphic to \(R\), and has no hypertrace in its
standard representation. (c) The trivial group has only finite conjugacy classes; it is amenable but \(L(\{e\})=
\mathbb C\). This is why "nontrivial" is part of the ICC condition. (d) For \(\Gamma=\mathbb Z\),
\(L(\mathbb Z)\cong L^\infty(\mathbb T)\) is abelian; the next section explains how non-ICC amenable groups fit in.

## 6. Injective semifinite von Neumann algebras

The central decomposition lets us pass from factors to general algebras. The key point is to choose isomorphisms of
the fibres with \(R\) in a measurable way.

**Lemma 6.1.** Let \(Q\) be an injective von Neumann algebra of type II₁ with separable predual. Then
\(Q\cong Z(Q)\mathbin{\bar\otimes}R\), by an isomorphism that restricts to \(z\mapsto z\otimes1\) on \(Z(Q)\).

**Proof.** Let \(\tau\) be a faithful normal tracial state on \(Q\) (B4), and represent \(Q\) standardly on
\(H=L^2(Q,\tau)\), with trace vector \(\xi\). Take the central decomposition (B5): \(H=\int^\oplus H(x)\,d\mu\),
\(Q=\int^\oplus Q(x)\,d\mu\), \(Z(Q)=L^\infty(X,\mu)\). By (B5)(iv),(v), for almost every \(x\): \(Q(x)\) is a II₁
factor, \(\xi(x)\) is cyclic for \(Q(x)\), and its vector state is a trace. A cyclic trace vector is separating (if
\(a\xi(x)=0\) then \(\|ab\xi(x)\|^2=\langle b^*a^*ab\,\xi(x),\xi(x)\rangle=\langle abb^*a^*\xi(x),\xi(x)\rangle\le
\|b\|^2\|a^*\xi(x)\|^2=\|b\|^2\|a\xi(x)\|^2=0\) for all \(b\)). So \(\xi(x)\ne0\), and
\(\xi'(x)=\xi(x)/\|\xi(x)\|\) is a cyclic separating unit trace vector: \(Q(x)\) is in standard form on \(H(x)\). In
particular \(H(x)\) is infinite dimensional and separable, and by (B5) we may take \(H(x)=H_0\) for all \(x\).

By Theorem 1.1(d), almost every \(Q(x)\) is injective, hence isomorphic to \(R\) by Theorem 4.1. Fix a copy
\(R_0\subset B(H_0)\) of \(R\) in standard form with unit trace vector \(\xi_0\). If \(\beta:Q(x)\to R_0\) is an
isomorphism, it preserves the unique normalized traces, so \(a\xi'(x)\mapsto\beta(a)\xi_0\) extends to a unitary
\(U\) of \(H_0\) with \(UaU^*=\beta(a)\) and \(U\xi'(x)=\xi_0\). Thus for almost every \(x\) the set
\[
S_x=\{U\in\mathcal U(H_0):UQ(x)U^*=R_0,\ U\xi'(x)=\xi_0\}
\]
is nonempty.

Choose countable self-adjoint sets \(\{a_n\}\subset Q\) and \(\{b_n\}\subset Q'\) generating \(Q\) and \(Q'\), and
countable self-adjoint sets \(\{r_n\}\subset R_0\), \(\{r_n'\}\subset R_0'\) generating \(R_0\) and \(R_0'\) (possible
because the preduals are separable). Discarding a null set, (B5)(iii) says \(Q(x)=\{a_n(x)\}''\)
and \(Q(x)'=\{b_n(x)\}''\). Then \(U\in S_x\) if and only if
\[
[Ua_n(x)U^*,r_m']=0,\qquad[U^*r_mU,b_n(x)]=0\ \ (n,m\in\mathbb N),\qquad U\xi'(x)=\xi_0 .
\]
The first family says \(UQ(x)U^*\subset R_0''=R_0\), the second says \(U^*R_0U\subset Q(x)''=Q(x)\). Fix a countable
dense set \((\eta_k)\) in \(H_0\). Each condition is equivalent to the vanishing of countably many functions such as
\((x,U)\mapsto\langle a_n(x)U^*r_m'\eta_k,U^*\eta_l\rangle-\langle a_n(x)U^*\eta_k,U^*r_m'^*\eta_l\rangle\). These are
Borel on \(X\times\mathcal U(H_0)\): for fixed \(x\) they are continuous in \(U\) (strong topology, bounded
operators), and for fixed \(U\) measurable in \(x\). So \(S=\{(x,U):U\in S_x\}\) is Borel, with conull projection.
By (B6) there is a Borel map \(x\mapsto U_x\in S_x\) on a conull Borel set; set \(U_x=1\) elsewhere.

Then \(U=\int^\oplus U_x\,d\mu\) is a unitary of \(L^2(X,\mu;H_0)\). For \(T\in Q\), \(UTU^*\) is decomposable with
fibres \(U_xT(x)U_x^*\in R_0\) almost everywhere; conversely every decomposable operator with fibres in \(R_0\) is of
this form. By (B5), \(UQU^*=L^\infty(X,\mu)\mathbin{\bar\otimes}R_0\), and \(U\) commutes with the diagonal algebra
\(Z(Q)\). \(\square\)

**Theorem 6.2 (injective semifinite algebras).** Let \(N\) be an injective von Neumann algebra with separable
predual. Then
\[
N\cong\Big(\bigoplus_{1\le n\le\infty}Z_n\mathbin{\bar\otimes}M_n\Big)\oplus\big(Z_{\rm II_1}\mathbin{\bar\otimes}R\big)
\oplus\big(Z_{\rm II_\infty}\mathbin{\bar\otimes}R_{0,1}\big)\oplus N_{\rm III},
\]
where the \(Z\)'s are abelian von Neumann algebras with separable predual (possibly zero) and \(N_{\rm III}\) is of type
III. Conversely every algebra of this form with \(N_{\rm III}\) injective is injective.

**Proof.** Split \(N\) by type (B4). The type I parts have the stated form without any hypothesis. Each summand
\(zN\), \(z\) a central projection, is injective by Lemma 2.2(e). The II₁ part is \(Z_{\rm II_1}\mathbin{\bar\otimes}R\)
by Lemma 6.1.

Let \(N_2=zN\) be the II∞ part. By (B4) choose a finite projection \(e\in N_2\) with central support \(z\). Then
\(eN_2e\) is of type II₁, injective by Lemma 2.2(e), with centre \(Z(N_2)e\cong Z(N_2)\). By Lemma 6.1,
\(eN_2e\cong Z(N_2)\mathbin{\bar\otimes}R\). In \(P=N_2\mathbin{\bar\otimes}B(\ell^2)\) consider \(p=e\otimes1\) and
\(q=z\otimes e_{11}\). Both have central support \(z\otimes1\) and are countably decomposable. The projection \(q\) is
properly infinite because \(N_2\) is. The projection \(p\) is the sum of the infinitely many equivalent projections
\(e\otimes e_{kk}\), each with central support \(z\otimes1\); so for every central projection \(c\) with \(cp\ne0\),
\(cp\) is equivalent to its proper subprojection \(\sum_{k\ge2}c(e\otimes e_{kk})\), and \(p\) is properly infinite. By
(B4), \(p\sim q\), hence
\[
N_2\cong qPq\cong pPp=eN_2e\mathbin{\bar\otimes}B(\ell^2)\cong Z(N_2)\mathbin{\bar\otimes}R\mathbin{\bar\otimes}B(\ell^2)
=Z(N_2)\mathbin{\bar\otimes}R_{0,1}.
\]
The converse follows from Lemma 2.2(b),(c),(d) and Example 2.4. \(\square\)

**Corollary 6.3 (von Neumann subalgebras of \(R\)).** Every von Neumann subalgebra \(Q\) of \(R\) is isomorphic to
\((Z\mathbin{\bar\otimes}R)\oplus\bigoplus_{n<\infty}Z_n\mathbin{\bar\otimes}M_n\) with \(Z,Z_n\) abelian, and \(Q\) is
AFD.

**Proof.** As in Corollary 4.2, \(Q\) is finite, injective and has separable predual; Theorem 6.2 gives the form, with
no infinite summands. Each summand is AFD: if \(A_k\) are increasing finite-dimensional algebras with dense union in an
abelian \(Z\) (as in the proof of Proposition 2.6), use \(A_k\otimes M_2^{\otimes k}\) in \(Z\mathbin{\bar\otimes}R\)
and \(A_k\otimes M_n\) in \(Z_n\mathbin{\bar\otimes}M_n\). For a countable direct sum \(\bigoplus_jQ_j\) with unit
projections \(p_j\) and filtrations \(G_k^{(j)}\), the algebras \(G_k=G_k^{(1)}\oplus\cdots\oplus G_k^{(k)}\oplus
\mathbb C(1-p_1-\cdots-p_k)\) increase (because \(1-p_1-\cdots-p_k=p_{k+1}+(1-p_1-\cdots-p_{k+1})\) and \(p_{k+1}\in
G_{k+1}^{(k+1)}\)) and have dense union. \(\square\)

**Corollary 6.4 (amenable discrete groups).** Let \(\Gamma\) be a countable group. Then \(\Gamma\) is amenable if and
only if
\[
\lambda(\Gamma)'\cong(Z\mathbin{\bar\otimes}R)\oplus\bigoplus_{n<\infty}Z_n\mathbin{\bar\otimes}M_n
\]
for some abelian \(Z,Z_n\). If \(\Gamma\) is ICC, this says \(\lambda(\Gamma)'\cong R\).

**Proof.** By (B14), \(\lambda(\Gamma)'=\rho(\Gamma)''\cong L(\Gamma)\). If \(\Gamma\) is amenable, \(L(\Gamma)\) is
injective (Proposition 5.1), finite (it has the faithful trace \(\tau\)) and has separable predual, so Theorem 6.2
gives the form. Conversely an algebra of that form is injective (Theorem 6.2), so \(\Gamma\) is amenable by
Proposition 5.1. The ICC case is Theorem 5.2. \(\square\)

**Corollary 6.5 (connected groups).** Let \(G\) be a second countable connected locally compact group. Then
\[
\lambda(G)'\cong(Z\mathbin{\bar\otimes}R_{0,1})\oplus\bigoplus_{1\le n\le\infty}Z_n\mathbin{\bar\otimes}M_n
\]
with \(Z,Z_n\) abelian. In other words, the only factors appearing in the central decomposition of the regular
representation are the type I factors and \(R_{0,1}\).

**Proof.** By Theorem 1.1(g), \(\lambda(G)'\) is injective; it has separable predual since \(L^2(G)\) is
separable, \(G\) being second countable, and it is isomorphic to \(\lambda(G)''\) by (B14). By (B15) it has no part
of type II₁ or III. Apply Theorem 6.2. \(\square\)

Second countability is used for the separability of \(L^2(G)\), and a separable locally compact group need not
have a separable \(L^2\)-space. Let \(I\subset\mathbb R\) be an uncountable set that is linearly independent
over \(\mathbb Q\), and \(K=\mathbb T^I\), a compact connected group. The homomorphism
\(f\colon\mathbb R\to K\), \(f(t)_\alpha=e^{2\pi it\alpha}\), has dense image. Indeed, let
\(\alpha_1,\dots,\alpha_n\in I\) be distinct. For a nonzero integer vector \((m_j)\), the number
\(\beta=\sum_jm_j\alpha_j\) is nonzero, so \(\frac1{2T}\int_{-T}^Te^{2\pi it\beta}\,dt\to0\), which is the
Haar integral of the character \(z\mapsto\prod_jz_j^{m_j}\) of \(\mathbb T^n\). By the Stone–Weierstrass
theorem, for every continuous function on \(\mathbb T^n\) the averages over \([-T,T]\) along
\(t\mapsto(e^{2\pi it\alpha_j})_j\) tend to its Haar integral; a nonnegative continuous function with nonzero
integral supported in an open set missed by this curve would contradict this. So the curve is dense in
\(\mathbb T^n\), and since the basic open sets of \(K\) depend on finitely many coordinates, \(f(\mathbb R)\)
is dense in \(K\). As \(f(\mathbb R)\) lies in the closure of \(f(\mathbb Q)\), the countable set
\(f(\mathbb Q)\) is dense, and \(K\) is separable. But the coordinate characters \(z\mapsto z_\alpha\),
\(\alpha\in I\), form an uncountable orthonormal family in \(L^2(K)\): distinct characters are orthogonal,
because the integral of a nontrivial character \(\chi\) is zero (choosing \(z_0\) with \(\chi(z_0)\ne1\),
invariance of Haar measure gives \(\int\chi=\chi(z_0)\int\chi\)). So \(L^2(K)\) is not separable.

**Example 6.6.** Let \(\Gamma=\mathbb Z\times S_\infty\). Then \(L(\Gamma)=L(\mathbb Z)\mathbin{\bar\otimes}L(S_\infty)
\cong L^\infty(\mathbb T)\mathbin{\bar\otimes}R\): a single summand \(Z\otimes R\) with diffuse \(Z\). For a finite
group \(\Gamma\), \(L(\Gamma)\cong\bigoplus_\pi M_{d_\pi}\), a sum over the irreducible representations, and only the
type I summands occur.

## 7. A bicommutant theorem inside \(R\)

In a type I factor, a von Neumann algebra is its own bicommutant. Inside \(R\), relative commutants of a subalgebra
can be trivial, so the commutant of a single subalgebra carries too little information. The right replacement uses
sequences that asymptotically commute. In this section \(\tau\) is the trace of \(R\), and by (B3) strong convergence of
bounded sequences in \(R\) is \(\|\cdot\|_2\)-convergence. Recall \(\|xy\|_2\le\|x\|\,\|y\|_2\) and
\(\|xy\|_2\le\|x\|_2\|y\|\) for \(x,y\in R\), and \(\|uxu^*\|_2=\|x\|_2\) for unitaries \(u\).

**Lemma 7.1.** Let \(G\subset R\) be a finite-dimensional \(*\)-subalgebra containing \(1\), and \(C=G'\cap R\). Then
\(C'\cap R=G\).

**Proof.** Clearly \(G\subset C'\cap R\). Let \((e^j_{ab})\) be a system of matrix units for \(G\), with blocks \(j\) of
size \(k_j\), and \(\sum_{j,a}e^j_{aa}=1\). Put \(p_j=e^j_{11}\). For \(c\in p_jRp_j\) the element
\(\gamma_j(c)=\sum_ae^j_{a1}ce^j_{1a}\) commutes with all \(e^i_{ab}\), so it lies in \(C\). Let \(x\in C'\cap R\) and
put \(x^{ij}_{ab}=e^i_{1a}xe^j_{b1}\in p_iRp_j\). From \(x\gamma_j(c)=\gamma_j(c)x\), multiplying by \(e^i_{1a}\) on the
left and \(e^j_{b1}\) on the right, we get \(x^{ij}_{ab}c=\delta_{ij}\,c\,x^{ij}_{ab}\). For \(i\ne j\), taking
\(c=p_j\) gives \(x^{ij}_{ab}=0\). For \(i=j\), \(x^{jj}_{ab}\) commutes with \(p_jRp_j\), a factor, so
\(x^{jj}_{ab}=\lambda^j_{ab}p_j\). Hence \(x=\sum e^i_{a1}x^{ij}_{ab}e^j_{1b}=\sum_{j,a,b}\lambda^j_{ab}e^j_{ab}\in G\).
\(\square\)

**Theorem 7.2.** Let \(\mathcal S\subset R\) be a self-adjoint set, and \(N\) the von Neumann subalgebra of \(R\) it
generates. Then \(N\) is the set of \(x\in R\) such that \([x,y_n]\to0\) strongly for every bounded sequence
\((y_n)\) in \(R\) with \([y_n,s]\to0\) strongly for all \(s\in\mathcal S\).

**Proof.** Call \(M\) the set described.

*\(N\subset M\).* Fix a bounded sequence \((y_n)\) with \(\|[y_n,s]\|_2\to0\) for \(s\in\mathcal S\), and let \(L\) be
the set of \(a\in R\) with \(\|[y_n,a]\|_2\to0\). It is a linear space containing \(1\) and \(\mathcal S\). It is closed
under products, since \([y_n,ab]=[y_n,a]b+a[y_n,b]\) and \(\|[y_n,a]b\|_2\le\|[y_n,a]\|_2\|b\|\). Its intersection with
each ball of \(R\) is \(\|\cdot\|_2\)-closed, because \(\|[y_n,a]\|_2\le\|[y_n,a']\|_2+2\sup_k\|y_k\|\,\|a-a'\|_2\). Since
\(\mathcal S\) is self-adjoint, \(L\) contains the \(*\)-algebra generated by \(\mathcal S\) and \(1\), and by Kaplansky's
theorem and (B3), its strong closure \(N\).

*\(M\subset N\).* By Corollary 6.3, \(N\) is AFD: choose finite-dimensional \(N_1\subset N_2\subset\cdots\) containing
\(1\) with dense union in \(N\). Let \(y\in R\setminus N\), let \(E_N\) be the \(\tau\)-preserving expectation onto \(N\)
(B2), and \(\varepsilon=\|y-E_N(y)\|_2>0\). As \(E_N\) is the orthogonal projection of \(L^2(R)\) onto the closure of
\(N\), \(\|y-x\|_2\ge\varepsilon\) for every \(x\in N\).

Fix \(k\) and put \(C_k=N_k'\cap R\). Let \(K\) be the \(\|\cdot\|_2\)-closure of the convex hull of \(\{uyu^*:u\in
\mathcal U(C_k)\}\). It lies in the ball of radius \(\|y\|\) of \(R\), which is \(\|\cdot\|_2\)-complete (B3), so \(K\) is a
closed convex subset of \(L^2(R)\) contained in \(R\). Let \(z\) be its unique element of minimal \(\|\cdot\|_2\). For
\(u\in\mathcal U(C_k)\), \(uKu^*=K\) and \(\|uzu^*\|_2=\|z\|_2\), so \(uzu^*=z\) by uniqueness. Hence \(z\in C_k'\cap R=
N_k\subset N\) (Lemma 7.1), and \(\|z-y\|_2\ge\varepsilon\). If \(\|uyu^*-y\|_2<\varepsilon/2\) held for every
\(u\in\mathcal U(C_k)\), every element of \(K\) would be within \(\varepsilon/2\) of \(y\), a contradiction. So there
is \(u_k\in\mathcal U(C_k)\) with
\[
\|[u_k,y]\|_2=\|u_kyu_k^*-y\|_2\ge\varepsilon/2.
\]
Now let \(s\in\mathcal S\) and \(\delta>0\). By Kaplansky's theorem there are \(m\) and \(s'\in N_m\) with
\(\|s-s'\|_2<\delta\). For \(k\ge m\), \(u_k\) commutes with \(N_m\subset N_k\), so \(\|[u_k,s]\|_2=\|[u_k,s-s']\|_2
\le2\delta\). Thus \([u_k,s]\to0\) strongly for every \(s\in\mathcal S\) while \([u_k,y]\not\to0\): \(y\notin M\).
\(\square\)

The same proof works with \(\mathcal S\) replaced by any self-adjoint subset of an AFD subalgebra; what is special about
\(R\) is that every subalgebra is AFD (Corollary 6.3). Self-adjointness is needed: for an arbitrary subset, test
commutation with \(\mathcal S\cup\mathcal S^*\). For example, take \(\mathcal S=\{e_{12}\}\) in a unital copy of \(M_2\)
in \(R\) and the constant sequence \(y_n=e_{12}\). Then \([y_n,s]=0\) for every \(s\in\mathcal S\), but \(e_{21}\) lies in
the von Neumann algebra generated by \(\mathcal S\) and \([e_{21},y_n]=e_{22}-e_{11}\) does not tend to \(0\).

## 8. Injective factors of type III\(_\lambda\), \(0<\lambda<1\)

A reference for this section is [Connes 1973].

**The module.** Let \(N\) be a II∞ factor with a faithful normal semifinite trace \(\tau\). Such traces are unique
up to a positive scalar, so for \(\theta\in\operatorname{Aut}N\) there is a number \(\operatorname{mod}\theta>0\) with
\(\tau\circ\theta=\operatorname{mod}(\theta)\tau\), independent of \(\tau\). If \(\beta:N\to N_1\) is an isomorphism,
then \(\tau\circ\beta^{-1}\) is a trace on \(N_1\) and
\[
(\tau\circ\beta^{-1})\circ(\beta\theta\beta^{-1})=\tau\circ\theta\circ\beta^{-1}=\operatorname{mod}(\theta)\,
\tau\circ\beta^{-1},
\]
so \(\operatorname{mod}(\beta\theta\beta^{-1})=\operatorname{mod}\theta\). Also
\(\operatorname{mod}(\operatorname{Ad}u\circ\theta)=\operatorname{mod}\theta\). Two automorphisms \(\theta_1,\theta_2\)
are *outer conjugate* if \(\theta_2=\operatorname{Ad}u\circ\alpha\theta_1\alpha^{-1}\) for some \(\alpha\in
\operatorname{Aut}N\) and unitary \(u\in N\).

**Lemma 8.1.** Let \(N\) be a von Neumann algebra with separable predual, and \(\theta_1,\theta_2\in\operatorname{Aut}N\).
- (a) If \(\beta:N\to N_1\) is an isomorphism, \(N\rtimes_{\theta_1}\mathbb Z\cong N_1\rtimes_{\beta\theta_1\beta^{-1}}
  \mathbb Z\).
- (b) If \(\theta_1\) and \(\theta_2\) are outer conjugate, \(N\rtimes_{\theta_1}\mathbb Z\cong N\rtimes_{\theta_2}
  \mathbb Z\).

**Proof.** Let \(B=N\rtimes_{\theta_1}\mathbb Z\), with \(\pi\), \(U=\lambda_1\) and canonical expectation \(F\) onto
\(Q=\pi(N)\) (B8). \(Q\) has a faithful normal state since \(N_*\) is separable.

(a) By Lemma 1.3 with \(v_n=U^n\), \(B\cong Q\rtimes_{\operatorname{Ad}U}\mathbb Z\). Now \(\iota=\pi\circ\beta^{-1}\) is
a faithful normal representation of \(N_1\) with image \(Q\), and \(U\iota(y)U^*=\pi(\theta_1\beta^{-1}(y))=
\iota(\beta\theta_1\beta^{-1}(y))\). Computing \(N_1\rtimes_{\beta\theta_1\beta^{-1}}\mathbb Z\) in the representation
\(\iota\) gives exactly \(Q\rtimes_{\operatorname{Ad}U}\mathbb Z\), so by (B8) the two crossed products are isomorphic.

(b) By (a) with \(N_1=N\) we may assume \(\theta_2=\operatorname{Ad}u\circ\theta_1\). Put \(V=\pi(u)U\). Then
\(V\pi(a)V^*=\pi(u\theta_1(a)u^*)=\pi(\theta_2(a))\), and \(Q\) and \(V\) generate \(B\) since \(U=\pi(u)^*V\). By
induction, for \(n\ge1\), \(V^n=\pi(u_n)U^n\) with \(u_n=u\theta_1(u)\cdots\theta_1^{n-1}(u)\), and
\(V^{-n}=U^{-n}\pi(u_n^*)=\pi(\theta_1^{-n}(u_n^*))U^{-n}\). So \(F(V^m)=\pi(w)F(U^m)=0\) for \(m\ne0\), with \(w\) the
appropriate unitary. Lemma 1.3 with \(v_n=V^n\) gives \(B\cong Q\rtimes_{\operatorname{Ad}V}\mathbb Z\), and
\(\operatorname{Ad}V|_Q=\pi\theta_2\pi^{-1}\), so as in (a), \(B\cong N\rtimes_{\theta_2}\mathbb Z\). \(\square\)

**Lemma 8.2.** Let \(M=N\rtimes_\theta\Gamma\) with \(\Gamma\) countable. If \(M\) is injective, so is \(N\).

**Proof.** The canonical expectation \(F\) is a projection of norm one of \(M\) onto \(\pi(N)\cong N\); apply Lemma
2.2(f). \(\square\)

**Theorem 8.3.** Let \(0<\lambda<1\). Every injective factor of type III\(_\lambda\) with separable predual is
isomorphic to the Powers factor \(R_\lambda\). In particular \(R_\lambda\) is the only AFD factor of type
III\(_\lambda\).

**Proof.** Let \(M\) be such a factor. By (B9)(a), \(M\cong N\rtimes_\theta\mathbb Z\) with \(N\) a II∞ factor with
separable predual and \(\operatorname{mod}\theta=\lambda\). By Lemma 8.2, \(N\) is injective, so there is an isomorphism
\(\beta:N\to R_{0,1}\) (Theorem 4.3). By Lemma 8.1(a), \(M\cong R_{0,1}\rtimes_{\theta_1}\mathbb Z\) with
\(\theta_1=\beta\theta\beta^{-1}\) and \(\operatorname{mod}\theta_1=\lambda\).

\(R_\lambda\) is injective, of type III\(_\lambda\) and with separable predual (Example 2.4 and (B7)), so the same
argument gives \(R_\lambda\cong R_{0,1}\rtimes_{\theta_2}\mathbb Z\) with \(\operatorname{mod}\theta_2=\lambda\). By
(B10), \(\theta_1\) and \(\theta_2\) are outer conjugate, and Lemma 8.1(b) gives \(M\cong R_\lambda\). The last claim
holds because AFD factors are injective. \(\square\)

**Example 8.4.** \(R_\lambda\mathbin{\bar\otimes}B(\ell^2)\) is AFD (tensor the filtrations of Example 2.4) and is a
factor of type III\(_\lambda\) (amplification does not change the type). So it is isomorphic to \(R_\lambda\). The
parameter matters: for \(\lambda\ne\mu\) in \(]0,1[\), \(R_\lambda\) and \(R_\mu\) have different types and are not
isomorphic. The case \(\lambda=1\) is different in nature: there the crossed product structure of (B9)(a) is not
available, and Section 10 obtains less.

## 9. Injective factors of type III₀

A reference for this section is [Connes 1975a].

**Theorem 9.1.** Every injective factor \(M\) of type III₀ with separable predual is a Krieger factor.

**Proof.** Take a discrete decomposition \(M\cong N\rtimes_\theta\mathbb Z\) as in (B9)(b), with \(N\) of type II∞ and
separable predual. By Lemma 8.2, \(N\) is injective. By Theorem 6.2, applied to \(N\), which has only a II∞ part,
\(N\cong Z(N)\mathbin{\bar\otimes}R_{0,1}\). By (B11)(b), \(M\) is a Krieger factor. \(\square\)

In the language of the central decomposition: almost every factor in the central decomposition of \(N\) is an
injective II∞ factor, hence \(R_{0,1}\) (Theorem 1.1(d) and Theorem 4.3), and Lemma 6.1, through the proof of
Theorem 6.2, glues these fibres together.

**Corollary 9.2.** Let \(M_1\) and \(M_2\) be injective factors of type III₀ with separable predual. Then
\(M_1\cong M_2\) exactly when the two flows of weights are isomorphic.

**Proof.** Isomorphic factors have isomorphic flows of weights by (B11)(c). Conversely, by Theorem 9.1 both factors
are Krieger factors, and (B11)(d) applies. \(\square\)

**Remark 9.3.** Conversely every Krieger factor is injective (Proposition 2.8). So, up to isomorphism, the Krieger
factors of type III₀ are exactly the injective type III₀ factors, and by (B11)(c),(d) they are in bijection with the
isomorphism classes of ergodic flows that are not transitive.

## 10. Injective factors of type III₁

**Theorem 10.1.** Every injective factor \(M\) of type III₁ with separable predual is semidiscrete. It is also AFD.

**Proof.** Let \(\varphi\) be a faithful normal state on \(M\) and \(T>0\). Put \(P=M\rtimes_{\sigma^\varphi_T}\mathbb
Z\). It has separable predual, and it is generated by the injective algebra \(\pi(M)\) and the group
\(\{\lambda_n\}\cong\mathbb Z\), which normalizes \(\pi(M)\); so \(P\) is injective by Theorem 1.1(e). By (B9)(c),
\(P\) is a factor of type III\(_\lambda\) with \(\lambda=e^{-2\pi/T}\), or of type III₀. In the first case
\(P\cong R_\lambda\) by Theorem 8.3, and \(R_\lambda\) is semidiscrete (Example 2.4). In the second case \(P\) is a
Krieger factor by Theorem 9.1, and Krieger factors are semidiscrete (Proposition 2.8). So \(P\) is semidiscrete. The
canonical expectation of \(P\) onto \(\pi(M)\cong M\) is normal, so \(M\) is semidiscrete by Proposition 3.4.

For the second claim: \(M\) is injective with separable predual, so it is generated by an increasing sequence of
finite-dimensional unital subalgebras, by Injective algebras and separable tracial envelopes, Theorem 3.1. This is Definition 2.1(a). \(\square\)

By the uniqueness theorem (B12), \(M\) is even isomorphic to \(R_\infty\).

Part of (B9)(c) is visible in the proof: the dual weight \(\tilde\varphi=\varphi\circ F\) on \(P\) has a modular group
that fixes \(\lambda_1\) and acts as \(\sigma^\varphi\) on \(\pi(M)\), so \(\sigma^{\tilde\varphi}_T=\operatorname{Ad}
\lambda_1\) is inner. So \(T\) lies in the invariant \(T(P)\), and this forces the invariant \(S(P)\) into
\(\{e^{2\pi n/T}:n\in\mathbb Z\}\cup\{0\}\). The first part of Theorem 10.1 uses only the classifications of Sections
8 and 9. The second part uses the general theorem that injectivity implies approximate finite dimensionality, which is
proved by a direct construction of finite-dimensional subalgebras; the argument through \(P\) alone shows only that
\(M\) is the range of a normal conditional expectation on the semidiscrete factor \(P\).

## 11. The four approximation properties coincide

**Theorem 11.1.** For a factor \(M\) with separable predual on a separable Hilbert space \(H\), these conditions are
equivalent:
- (a) \(M\) is AFD;
- (b) \(M\) is injective;
- (c) \(M\) has property P on \(H\);
- (d) \(M\) is semidiscrete.

**Proof.** (a)⇒(c) is Proposition 3.1, (c)⇒(b) is Proposition 3.2, and (d)⇒(b) is Proposition 3.3.

(b)⇒(a) and (b)⇒(d). Let \(M\) be injective, and go through the types (B4).
- Type I\(_n\), \(n<\infty\): \(M\cong M_n\), trivially AFD and semidiscrete. Type I∞: \(M\cong B(\ell^2)\), Example
  2.4.
- Type II₁: \(M\cong R\) (Theorem 4.1). Type II∞: \(M\cong R_{0,1}\) (Theorem 4.3). Both are covered by Example 2.4.
- Type III\(_\lambda\), \(0<\lambda<1\): \(M\cong R_\lambda\) (Theorem 8.3), Example 2.4.
- Type III₀: \(M\) is a Krieger factor (Theorem 9.1), which is semidiscrete (Proposition 2.8) and AFD (B11)(a).
- Type III₁: Theorem 10.1.

Finally (b)⇒(c) follows from (b)⇒(a)⇒(c). \(\square\)

For factors that are not of type III₁, the proof uses only the background on discrete decompositions and Krieger
factors; for type III₁ the implications from (b) to (a) and (c) use Theorem 10.1, whose second part rests on
Injective algebras and separable tracial envelopes, Theorem 3.1.

**Corollary 11.2.** Let \(G\) be a locally compact group that is amenable, for instance solvable, or whose
quotient \(G/G_0\) by the identity component is amenable, for instance connected, and \(\pi\) a continuous unitary
representation of \(G\) on a separable Hilbert space. Then \(\pi(G)''\) is AFD.

**Proof.** If \(G\) is amenable, the algebra \(Q=\pi(G)''\) is injective by Theorem 1.1(f); solvable locally
compact groups are amenable (B14). If \(G/G_0\) is amenable, \(Q\) is injective by Theorem 1.1(g). Take its central decomposition (B5). The
sets \(X_d=\{x:\dim H(x)=d\}\), \(1\le d\le\aleph_0\), are measurable and correspond to central projections \(z_d\) of
\(Q\); each \(z_dQ\) is injective (Lemma 2.2(e)), and over \(X_d\) the field of Hilbert spaces is constant. By Theorem
1.1(d), applied to each \(z_dQ\), almost every factor \(Q(x)\) is injective. It has separable predual, so it is AFD by
Theorem 11.1. By (B13), \(Q\) is AFD. \(\square\)

For a representation whose von Neumann algebra is semifinite, Theorem 6.2 gives more than (B13): an explicit AFD
model, since every summand in Theorem 6.2 is AFD (as in the proof of Corollary 6.3, with Example 2.4 for \(R_{0,1}\)).

## 12. Exercises

**Exercise 12.1.** Let \(N\subset R\) be a von Neumann subalgebra with \(N'\cap R=\mathbb C\). Show that \(N\cong R\).

*Solution.* \(Z(N)\subset N'\cap R=\mathbb C\), so \(N\) is a factor, and by Corollary 4.2 it is \(M_n\) or \(R\).
Suppose \(N\cong M_n\), with matrix units \(e_{ab}\). As in the proof of Lemma 7.1, \(c\mapsto\sum_ae_{a1}ce_{1a}\)
maps \(e_{11}Re_{11}\) injectively into \(N'\cap R\). But \(e_{11}Re_{11}\cong R\) is infinite dimensional
(Corollary 4.2), so \(N'\cap R\ne\mathbb C\), a contradiction. So \(N\cong R\).

**Exercise 12.2.** Show that \(L(S_3\times S_\infty)\cong R\oplus R\oplus R\) and that \(L(\mathbb Z\times
S_\infty)\not\cong R\oplus R\).

*Solution.* \(L(S_3\times S_\infty)=L(S_3)\mathbin{\bar\otimes}L(S_\infty)\cong(\mathbb C\oplus\mathbb C\oplus M_2)
\mathbin{\bar\otimes}R=R\oplus R\oplus(M_2\mathbin{\bar\otimes}R)\), and \(M_2\mathbin{\bar\otimes}R\cong R\)
(Example 4.4). For the second group, \(L(\mathbb Z\times S_\infty)\cong L^\infty(\mathbb T)\mathbin{\bar\otimes}R\)
(Example 6.6) has diffuse centre \(L^\infty(\mathbb T)\otimes1\), while the centre of \(R\oplus R\) is
\(\mathbb C^2\). Isomorphisms carry centres onto centres, so the algebras are not isomorphic.

**Exercise 12.3.** Let \(T\) be an ergodic automorphism of a nonatomic standard probability space \((X,\mu)\) that
preserves \(\mu\). Show that the Krieger factor \(L^\infty(X,\mu)\rtimes_T\mathbb Z\) is isomorphic to \(R\).

*Solution.* By Proposition 2.8 it is an injective factor. With \(\varphi=\mu\circ\pi^{-1}\circ F\) as in
Proposition 2.6, \(\varphi(\pi(a)\lambda_n\,\pi(b)\lambda_m)=\delta_{n,-m}\int a\,(b\circ T^{-n})\,d\mu\), and by
invariance of \(\mu\) this equals \(\varphi(\pi(b)\lambda_m\,\pi(a)\lambda_n)=\delta_{n,-m}\int b\,(a\circ T^{-m})\,
d\mu\) (substitute \(x\mapsto T^nx\)). By normality \(\varphi\) is a faithful normal tracial state. The factor is
infinite dimensional, so it is of type II₁, with separable predual. By Theorem 4.1 it is isomorphic to \(R\).

**Exercise 12.4.** Let \(\Gamma=S_\infty\), acting on \(\{0,1,2,\dots\}\), and \(H\subset\Gamma\) the subgroup of
permutations fixing \(0\). Put \(N=L(H)\subset L(\Gamma)\cong R\), the von Neumann algebra generated by the
\(\lambda_h\), \(h\in H\). Show that \(N\cong R\), that \(N'\cap L(\Gamma)=\mathbb C\), and that \(N\ne L(\Gamma)\).
Conclude that in Theorem 7.2 the sequences cannot be replaced by single elements: the relative bicommutant
\((N'\cap R)'\cap R\) of \(N\) is \(R\), not \(N\).

*Solution.* The space \(\ell^2(\Gamma)\) is the direct sum of the \(\lambda(H)\)-invariant subspaces
\(\ell^2(Hc)\), \(c\) running over right coset representatives, and on each of them \(\lambda|_H\) is equivalent to
the left regular representation of \(H\). So \(N\) is isomorphic to \(L(H)\) computed on \(\ell^2(H)\), and \(H\cong
S_\infty\) gives \(N\cong R\) (Example 5.3(a)). Let \(g\ne e\) in \(\Gamma\). Its support \(S\) is finite with at least
two points, so it contains some \(k\ne0\). For every \(m\notin S\cup\{0\}\) the transposition \(h=(k\ m)\) lies in
\(H\), and the support of \(hgh^{-1}\) is \(h(S)\ni m\). So \(\{hgh^{-1}:h\in H\}\) is infinite. Now let \(x\in N'\cap
L(\Gamma)\) and \(x\delta_e=\sum_gc_g\delta_g\). As in the proof of Theorem 5.2, \(x\) commutes with \(\lambda_h\rho_h\)
for \(h\in H\), so \(c\) is constant on \(H\)-conjugacy classes, which are infinite except \(\{e\}\); hence \(x=c_e1\).
Finally \(N\delta_e\) lies in the closed subspace \(\ell^2(H)\), while \(\lambda_{(0\,1)}\delta_e=\delta_{(0\,1)}\) is
orthogonal to it, so \(\lambda_{(0\,1)}\notin N\). The relative bicommutant is \(\mathbb C'\cap R=R\ne N\).

**Exercise 12.5.** Show that property P passes to direct sums: if \(M_i\subset B(H_i)\) have property P, so does
\(\bigoplus M_i\subset B(\bigoplus H_i)\), provided the sum is finite.

*Solution.* Let \(M=M_1\oplus M_2\), \(T\in B(H_1\oplus H_2)\) with
blocks \(T_{ij}\). The unitaries \(u_1\oplus1\) average the \((1,1)\) block within \(K_{T_{11}}\) and multiply the
off-diagonal blocks by \(u_1\) on one side. First choose a net of convex combinations of \(\operatorname{Ad}(u\oplus1)\)
moving \(T_{11}\) into \(M_1'\); take a weak cluster point \(T'\) of the images of \(T\). Then do the same with
\(1\oplus v\) on \(T'_{22}\), producing \(T''\) whose diagonal blocks lie in \(M_1'\) and \(M_2'\) (the first block is
unchanged, because \(\operatorname{Ad}(1\oplus v)\) does not act on it). Finally average with \(\operatorname{Ad}
(1\oplus(-1))\), which kills the off-diagonal blocks: \(\frac12(T''+(1\oplus-1)T''(1\oplus-1))\) is block diagonal with
blocks in \(M_1'\) and \(M_2'\), so it lies in \(M'=M_1'\oplus M_2'\). Every step stays in \(K_T\) (weak closures of
convex combinations of the \(\operatorname{Ad}u\), \(u\in\mathcal U(M)\)).

## References



- [Connes 1976] A. Connes, *On the classification of von Neumann algebras and their automorphisms*, IHÉS preprint
  IHES/P/76/132, February 1976. Free at
  https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1976-1984/P_76_132/P_76_132_web.pdf
- [Connes 1994] A. Connes, *Noncommutative geometry*, Academic Press, San Diego, CA, 1994. Free at
  https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf
- [Connes 1973] A. Connes, Une classification des facteurs de type III, Ann. Sci. École Norm. Sup. (4) 6 (1973),
  no. 2, 133–252. https://doi.org/10.24033/asens.1247. Free at https://alainconnes.org/wp-content/uploads/classificationfacteurs.pdf
- [Connes 1975a] A. Connes, On hyperfinite factors of type III₀ and Krieger's factors, J. Functional Analysis 18
  (1975), 318–327. https://doi.org/10.1016/0022-1236(75)90019-1. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123675900191
- [Connes 1975b] A. Connes, Outer conjugacy classes of automorphisms of factors, Ann. Sci. École Norm. Sup. (4) 8
  (1975), no. 3, 383–419. https://doi.org/10.24033/asens.1295. Free at https://alainconnes.org/wp-content/uploads/automorphismes.pdf
- [Connes 1985] A. Connes, Factors of type III₁, property L′λ and closure of inner automorphisms, J. Operator Theory 14
  (1985), 189–211. https://www.theta.ro/jot/archive/1985-014-001/1985-014-001-011.html
- [Connes–Takesaki 1977] A. Connes and M. Takesaki, The flow of weights on factors of type III, Tôhoku Math. J. (2)
  29 (1977), 473–575. https://doi.org/10.2748/tmj/1178240493
- [Haagerup 1987] U. Haagerup, Connes' bicentralizer problem and uniqueness of the injective factor of type III₁, Acta
  Math. 158 (1987), 95–148. https://doi.org/10.1007/BF02392257. Free at https://doi.org/10.1007/BF02392257
- [Araki–Woods 1968] H. Araki and E. J. Woods, A classification of factors, Publ. Res. Inst. Math. Sci. Ser. A 4
  (1968), 51–130. https://doi.org/10.2977/prims/1195195263
- [Tomiyama 1957] J. Tomiyama, On the projection of norm one in W\*-algebras, Proc. Japan Acad. 33 (1957), 608–612.
  https://doi.org/10.3792/pja/1195524885
- [Arveson 1969] W. Arveson, Subalgebras of C\*-algebras, Acta Math. 123 (1969), 141–224.
  https://doi.org/10.1007/BF02392388. Free at https://doi.org/10.1007/BF02392388
- [Dixmier 1969] J. Dixmier, Sur la représentation régulière d'un groupe localement compact connexe, Ann. Sci. École
  Norm. Sup. (4) 2 (1969), 423–436. https://doi.org/10.24033/asens.1180
- [Anantharaman–Popa] C. Anantharaman and S. Popa, *An introduction to II₁ factors*, book draft. Free at
  https://www.math.ucla.edu/~popa/Books/IIun.pdf
- [Namioka 1964] I. Namioka, Følner's conditions for amenable semi-groups, Math. Scand. 15 (1964), 18–28.
  https://doi.org/10.7146/math.scand.a-10723
