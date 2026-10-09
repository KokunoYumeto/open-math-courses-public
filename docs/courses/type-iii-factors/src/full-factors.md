# Full factors

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. The nonzero amplification condition was checked and corrected by GPT-6 Astra (OpenAI), Ultra, October 2026. Public domain (CC0).*

## Introduction

Every unitary \(u\) of a von Neumann algebra \(M\) defines an automorphism \(\operatorname{Ad}u(x)=uxu^*\). These inner
automorphisms form a normal subgroup \(\operatorname{Int}M\) of the automorphism group \(\operatorname{Aut}M\). When
\(M\) has separable predual, \(\operatorname{Aut}M\) carries a natural topology that makes it a Polish group, and it
is natural to ask whether \(\operatorname{Int}M\) is closed. If it is, the quotient
\(\operatorname{Out}M=\operatorname{Aut}M/\operatorname{Int}M\) is again a Polish group, and topological arguments on
\(\operatorname{Out}M\) become available. We call \(M\) *full* in that case.

This lesson does four things.

1. It sets up the topology of \(\operatorname{Aut}M\) and of the unitary group, and proves the open mapping theorem for
   Polish groups (Sections 2 and 3).
2. It proves that \(M\) is full exactly when every bounded sequence that asymptotically commutes with all normal
   functionals is asymptotically central, and gives three more equivalent forms (Section 4). For a factor this says
   that the asymptotic centralizer \(M_\omega\) is trivial (Section 5).
3. It identifies full factors of type II₁ as those without property \(\Gamma\) (Section 6), and shows that factors
   of type III₀ are never full: their modular automorphisms are limits of inner automorphisms (Section 7).
4. It builds full factors of types I, II₁, II∞ and III\(_\lambda\) for every \(\lambda\in\,]0,1]\), from crossed
   products of infinite tensor products by the free group on two generators. The key input is a spectral gap
   inequality for the free group (Sections 8 to 10).

Fullness is used throughout the next lessons, "Almost periodic weights and the invariant \(Sd\)" and "Full factors
without almost periodic weights", where the Polish group \(\operatorname{Out}M\) of a full factor is the stage on which
the invariants \(Sd\) and \(\tau\) are built.

**What is assumed.** The lesson "Ultraproducts and the asymptotic centralizer" of this course is a prerequisite. From
it we use the definition of centralizing and central sequences, the comparison between them, the construction of the
asymptotic centralizer \(M_\omega\) with its trace, and the fact that \(M_\omega\neq\mathbb C\) for factors of type
III₀ with separable predual. Section 1 restates exactly these statements, so that the present lesson can be read alongside it. We also use
standard operator algebra and descriptive set theory, listed in "Results used from other lessons" with the place where
each fact is proved.

Basic references are [Connes 1974] and [Connes 1973].

**Conventions.** \(M_*\) is the predual of \(M\) and \(M_*^+\) its positive part. \(C\) always denotes the centre of
\(M\), \(\mathcal U(M)\) the unitary group and \(\mathcal U(C)\) the group of central unitaries. For
\(\varphi\in M_*\) we write \(\varphi^*(x)=\overline{\varphi(x^*)}\).

## Results used from other lessons

**(B1) Topologies on bounded sets.** For \(\psi\in M_*^+\) and \(x\in M\) put
\(\|x\|_\psi=\psi(x^*x)^{1/2}\) and \(\|x\|_\psi^\#=\psi(x^*x+xx^*)^{1/2}\). The *strong* (respectively *strong\**)
topology on \(M\) is the one given by the seminorms \(\|\cdot\|_\psi\) (respectively \(\|\cdot\|^\#_\psi\)),
\(\psi\in M_*^+\). On bounded sets it agrees with the strong (respectively strong\*) operator topology in every
faithful normal representation. Suppose \(M\) has separable predual, and fix a faithful normal state \(\varphi\). Then
on bounded sets the strong topology is given by the single norm \(\|\cdot\|_\varphi\) and the strong\* topology by
\(\|\cdot\|^\#_\varphi\); the unit ball of \(M\) is separable for these topologies; and in the GNS representation
\((\pi_\varphi,H_\varphi,\xi_\varphi)\) the space \(H_\varphi\) is separable and \(\xi_\varphi\) is cyclic and
separating for \(\pi_\varphi(M)\), so that \(\pi_\varphi(M)'\xi_\varphi\) is dense. Every \(\varphi\in M_*\) is a
linear combination of four elements of \(M_*^+\). On bounded sets the strong and σ-strong operator topologies
agree and are given by these seminorms (Compact and trace-class operators, Lemma 8.5 and Theorem 9.1),
and every normal functional of \(M\) is the restriction of one of \(B(H)\) (Theorem 9.4(a) there),
which is a combination of four positive normal functionals (Proposition 6.3(c)). For a faithful
normal state \(\varphi\), \(\xi_\varphi\) is separating for \(\pi_\varphi(M)\), hence cyclic for \(\pi_\varphi(M)'\) (The double
commutant theorem, Proposition 9.2); a bounded net that converges on \(\xi_\varphi\), and whose adjoints do
for \(\|\cdot\|^\#_\varphi\), converges on the dense set \(\pi_\varphi(M)'\xi_\varphi\), hence strongly (strongly\*). If \(M_*\) is
separable, the unit ball is σ-weakly compact and metrizable, so it has a countable σ-weakly dense subset; σ-weak
convergence of \(x\) gives weak convergence of \(x\xi_\varphi\), and convex sets in a Hilbert space have the same weak and
norm closures, so rational convex combinations of that subset give a countable set dense in \(\pi_\varphi(M)\xi_\varphi\), and
\(H_\varphi\) and the unit ball (for \(\|\cdot\|_\varphi\), and likewise for \(\|\cdot\|^\#_\varphi\)) are separable.

**(B2) Kaplansky density theorem.** If \(\mathcal A\) is a \(\ast\)-subalgebra of a von Neumann algebra \(M\) whose
\(\sigma\)-weak closure is \(M\), then every element of the unit ball of \(M\) is a strong\* limit of a net in the unit
ball of \(\mathcal A\). Proved in Kaplansky's density theorem and its consequences, Theorem
7.1.

**(B3) Polish spaces.** A Polish space is a Baire space. Closed and open subsets of a Polish space are Polish. A
continuous image of a Polish space in a Polish space (an analytic set) has the Baire property, that is, it differs
from an open set by a meager set. The Baire category theorem: Hahn–Banach, Baire and the basic theorems on Banach
spaces, Theorem 3.1. Closed and open subsets: The Effros Borel structure, Lemma 1.3(3) and Theorem
2.1. The Baire property of analytic sets: Polish spaces and standard Borel spaces, Lemma
8.1.

**(B4) Modular theory.** Fix a faithful semifinite normal (f.s.n.) weight \(\varphi\) on \(M\), with modular group
\(\sigma^\varphi\).

- (a) *Connes cocycle.* For another f.s.n. weight \(\chi\) there is a strongly continuous family of unitaries
  \((D\chi:D\varphi)_t\) with \(\sigma^\chi_t=\operatorname{Ad}(D\chi:D\varphi)_t\circ\sigma^\varphi_t\).
- (b) *Centralizer.* Let \(M_\varphi\) be the fixed point algebra of \(\sigma^\varphi\). A unitary \(u\) satisfies
  \(\varphi\circ\operatorname{Ad}u=\varphi\) if and only if \(u\in M_\varphi\). The restriction of \(\varphi\) to
  \(M_\varphi\) is a trace: \(\varphi(x^*x)=\varphi(xx^*)\) for \(x\in M_\varphi\). If \(\varphi\) is a state,
  \(M_\varphi=\{x:\varphi(xy)=\varphi(yx)\ \forall y\in M\}\).
- (c) *KMS uniqueness.* If a faithful normal state \(\rho\) on \(M\) is invariant under a \(\sigma\)-weakly continuous
  one-parameter automorphism group \(\beta\) and satisfies the KMS condition for \(\beta\), then
  \(\beta=\sigma^\rho\).
- (d) *Conditional expectations.* If \(E\) is a faithful normal conditional expectation of \(M\) onto a von Neumann
  subalgebra \(N\) and \(\rho,\rho_1,\rho_2\) are f.s.n. weights on \(N\), then \(\rho\circ E\) is an f.s.n. weight on
  \(M\), \(\sigma^{\rho\circ E}_t(x)=\sigma^\rho_t(x)\) for \(x\in N\), and
  \((D(\rho_1\circ E):D(\rho_2\circ E))_t=(D\rho_1:D\rho_2)_t\).
- (e) *Semifinite algebras.* If \(N\) is semifinite with f.s.n. trace \(\tau\) and \(\rho\) is a faithful normal
  state of \(N\), then \(\rho=\tau(h\,\cdot)\) for a positive nonsingular operator \(h\) affiliated with \(N\), and
  \(\sigma^\rho_t=\operatorname{Ad}h^{it}\). Conversely, \(M\) is semifinite if \(\sigma^\varphi_t\) is inner for
  every \(t\).
- (f) *Tensor products.* If \(\varphi_1,\varphi_2\) are faithful normal states on \(M_1,M_2\), then
  \(\sigma^{\varphi_1\otimes\varphi_2}_t=\sigma^{\varphi_1}_t\otimes\sigma^{\varphi_2}_t\).

These are proved in the course *Modular theory and weights*: (a) in Comparing supported weights and transporting
their cuts, §WC-02; (b) in Fixed elements and changes of density,
§CZ-05, since \(\varphi\circ\operatorname{Ad}u=\varphi\) means \(\varphi(ux)=\varphi(xu)\) for all
\(x\); (c) in The KMS boundary condition determines the modular group, §KM-05; the
modular group of \(\rho\circ E\) in (d) in Conditional expectations from modular invariance,
§ME-10; (e) in Recognizing a weight by its fixed density,
§PT-08, Fixed elements and changes of density, §CZ-11 and
Inner modular flow and rigidity of finite weight data, §VR-02; (f) in Tensor operators,
their full domains, and tensor weights. The cocycle identity in (d) follows from the
first part of (d). Let \(\theta(\sum x_{ij}\otimes e_{ij})=\rho_2(x_{11})+\rho_1(x_{22})\) be the balanced weight on
\(N\otimes M_2(\mathbb C)\), so that \(\sigma^\theta_t(1\otimes e_{21})=(D\rho_1:D\rho_2)_t\otimes e_{21}\) (Supported GNS
representations and the balanced cocycle, §§GC-03–GC-04). The map \(E\otimes\mathrm{id}\) is a
faithful normal conditional expectation of \(M\otimes M_2(\mathbb C)\) onto \(N\otimes M_2(\mathbb C)\): it is positive because
\(E\) is completely positive (Contractive retractions and the algebraic structure of expectations,
§CE-006), and faithful because the diagonal entries of \((E\otimes\mathrm{id})(X^*X)\) are the
elements \(E(\sum_kx_{ki}^*x_{ki})\). The weight \(\theta\circ(E\otimes\mathrm{id})\) is the balanced weight of
\(\rho_2\circ E\) and \(\rho_1\circ E\), and its modular group agrees with \(\sigma^\theta\) on \(N\otimes M_2(\mathbb C)\);
evaluating at \(1\otimes e_{21}\) gives \((D(\rho_1\circ E):D(\rho_2\circ E))_t=(D\rho_1:D\rho_2)_t\).

**(B5) Traces.** On a von Neumann algebra with f.s.n. trace \(\tau\), every other f.s.n. trace has the form
\(\tau(h\,\cdot)\) with \(h\) positive, nonsingular and affiliated with the centre; hence a finite sum of f.s.n. traces
is an f.s.n. trace. A factor \(M\) of type II₁ has a unique normal tracial state \(\tau\), which is faithful; on
bounded sets the strong\* topology is given by \(\|x\|_2=\tau(x^*x)^{1/2}\); and for every projection \(q\) and every
\(s\in[0,\tau(q)]\) there is a projection \(q'\le q\) with \(\tau(q')=s\). *Dixmier approximation theorem:* in a
factor \(M\), the norm closed convex hull of \(\{uxu^*:u\in\mathcal U(M)\}\) contains a scalar, for every \(x\in M\).
Traces: Integration for a trace, Theorem 7.2 (with Corollary 7.4 for factors) and Traces on von
Neumann algebras, Propositions 3.2 and 3.5; the strong\* topology of a II₁ factor is given by
\(\|\cdot\|_2\) as in (B1) with \(\varphi=\tau\); subprojections of every trace: Measurable operators for a trace, Lemma
4.3. The Dixmier approximation theorem in norm is Traces on von Neumann algebras, Theorem 8.2 and Corollary 8.3; its σ-weak form is Traces on
von Neumann algebras, Lemma 5.1.

**(B6) The invariant \(S\).** For a factor \(M\), \(S(M)\) is the intersection of the spectra of the modular operators
\(\Delta_\varphi\) over all f.s.n. weights \(\varphi\) [Connes 1973, Definition 3.1.1]. If the centralizer \(M_\varphi\) is
a factor, then \(S(M)=\operatorname{Sp}\Delta_\varphi\) [Connes 1973, Corollary 3.2.7]. A factor is semifinite if and only
if \(S(M)=\{1\}\) [Connes 1973, Lemma 3.1.2]. The types are defined through \(S\): a factor is of type
III\(_\lambda\) for \(0<\lambda<1\) if and only if \(S(M)=\{\lambda^n:n\in\mathbb Z\}\cup\{0\}\), of type III₁ if
and only if \(S(M)=[0,\infty[\), and of type III₀ if and only if \(S(M)=\{0,1\}\) [Connes 1973, opening of Chapter IV].

**(B7) Structure of factors of type III₀.** Suppose \(M\) is a type III₀ factor whose predual is separable. There are a
von Neumann subalgebra \(N\subset M\) of type II∞, a faithful normal conditional expectation \(E\) of \(M\) onto \(N\),
and an increasing sequence \(G_1\subset G_2\subset\cdots\) of finite groups of unitaries of \(M\) (one can take
\(G_k\cong(\mathbb Z/2)^k\)) such that every \(u\in\bigcup_kG_k\) satisfies \(uNu^*=N\) and
\(E(uxu^*)=uE(x)u^*\) for \(x\in M\), and \(N\cup\bigcup_kG_k\) generates \(M\).
[Connes 1973, Corollary 5.3.6 and Proposition 1.4.6]

## 1. What is used from the asymptotic centralizer

This section restates, without proofs, the results of the lesson "Ultraproducts and the asymptotic centralizer" that
are used below.

**Commutators with functionals.** For \(x\in M\) and \(\varphi\in M_*\) define \(x\varphi,\varphi x\in M_*\) by
\((x\varphi)(y)=\varphi(yx)\) and \((\varphi x)(y)=\varphi(xy)\), and put \([x,\varphi]=x\varphi-\varphi x\). These
operations are associative: \(x(y\varphi)=(xy)\varphi\), \((\varphi x)y=\varphi(xy)\) (the functional
\(z\mapsto\varphi(xyz)\)), and \(x(\varphi y)=(x\varphi)y\).

**Limits along a filter.** Let \(\mathcal F\) be a filter on a set \(I\). A family \((t_i)_{i\in I}\) of real numbers
*tends to \(0\) along \(\mathcal F\)* if \(\{i:|t_i|<\varepsilon\}\in\mathcal F\) for every \(\varepsilon>0\). Three
cases matter: the filter of tails of a directed set (convergence of nets), the filter of cofinite subsets of
\(\mathbb N\) (ordinary sequences), and a free ultrafilter \(\omega\) on \(\mathbb N\) (limits \(\lim_{n\to\omega}\)).
A family \((x_i)\) in \(M\) tends to \(0\) strongly (strong\*) along \(\mathcal F\) if \(\|x_i\|_\psi\to0\)
(respectively \(\|x_i\|^\#_\psi\to0\)) along \(\mathcal F\) for every \(\psi\in M_*^+\).

**Definition 1.1.** A norm-bounded family \((x_i)_{i\in I}\) in \(M\) is *centralizing along \(\mathcal F\)* if
\(\|[x_i,\psi]\|\to0\) along \(\mathcal F\) for every \(\psi\in M_*\). It is *central along \(\mathcal F\)* if
\([x_i,y]\to0\) strong\* along \(\mathcal F\) for every \(y\in M\). For sequences and the cofinite filter we speak of
*centralizing sequences* and *central sequences*.

**Proposition 1.2.** Let \(M\) be countably decomposable, \((x_i)_{i\in I}\) a bounded family in \(M\) and
\(\mathcal F\) a filter on \(I\).

- (a) If \(\|[x_i,\psi]\|\to0\) along \(\mathcal F\) for every \(\psi\) in a subset of \(M_*\) with norm dense linear
  span, then \((x_i)\) is centralizing along \(\mathcal F\). Every family centralizing along \(\mathcal F\) is central
  along \(\mathcal F\).
- (b) Suppose \(\|[x_i,\varphi]\|\to0\) along \(\mathcal F\) for some faithful \(\varphi\in M_*^+\), and
  \([x_i,y]\to0\) strongly along \(\mathcal F\) for every \(y\) in some \(\sigma\)-weakly dense subset
  \(\mathcal S\subset M\). Then \((x_i)\) is centralizing along \(\mathcal F\).

This is Theorem 7.1 of "Ultraproducts and the asymptotic centralizer", which is proved there along an arbitrary
filter: (a) is its implication (β)⇒(γ), and (b) is (α)⇒(γ).

**Theorem 1.3.** Assume that the von Neumann algebra \(M\) is countably decomposable, and fix a free ultrafilter
\(\omega\) on \(\mathbb N\). Let \(A_\omega\subset\ell^\infty(\mathbb N,M)\) be the set of sequences centralizing along \(\omega\),
and \(I_\omega\) the set of bounded sequences tending to \(0\) strong\* along \(\omega\). Then \(A_\omega\) is a
C\*-algebra, \(A_\omega\cap I_\omega\) is a closed two-sided ideal of it, and the quotient
\(M_\omega=A_\omega/(A_\omega\cap I_\omega)\), the *asymptotic centralizer*, is again a finite von Neumann algebra. For every
faithful normal state \(\varphi\) on \(M\), the formula \(\varphi_\omega(x)=\lim_{n\to\omega}\varphi(x_n)\), where
\((x_n)\) represents \(x\), defines a faithful normal tracial state on \(M_\omega\).

In "Ultraproducts and the asymptotic centralizer" this is Definition 8.1 with Theorems 5.1 and 8.2; the sequences in
\(A_\omega\) are called \(\omega\)-central there. That lesson also shows \(I_\omega\subset A_\omega\), so
\(M_\omega=A_\omega/I_\omega\). Constant sequences with values in the centre \(C\) belong to \(A_\omega\), so \(C\)
sits in \(M_\omega\); for a factor we write \(M_\omega=\mathbb C\) when \(M_\omega\) consists of the classes of
constant scalar sequences.

**Theorem 1.4.** If \(M\) is a factor of type III₀ with separable predual, then \(M_\omega\neq\mathbb C\) for every
free ultrafilter \(\omega\) on \(\mathbb N\).

This is Theorem 11.2 of "Ultraproducts and the asymptotic centralizer".

## 2. The topology of the automorphism group

A reference for this section is [Connes 1974].

**Definition 2.1.** The *\(u\)-topology* on \(\operatorname{Aut}M\) is the topology in which a net \(\alpha_i\)
converges to \(\alpha\) if and only if \(\|\varphi\circ\alpha_i-\varphi\circ\alpha\|\to0\) for every
\(\varphi\in M_*\).

Since \(\|\varphi\circ\alpha_i-\varphi\circ\alpha\|=\sup_{\|x\|\le1}|\varphi(\alpha_i(x))-\varphi(\alpha(x))|\), this
is uniform convergence of \(\varphi(\alpha_i(x))\) on the unit ball of \(M\), for each \(\varphi\). A basis of
neighbourhoods of the identity is formed by the sets
\[
\mathcal W(\varphi_1,\dots,\varphi_n;\varepsilon)=\{\alpha\in\operatorname{Aut}M\ \mid\ \|\varphi_j\circ\alpha-\varphi_j\|<
\varepsilon,\ j=1,\dots,n\}.
\]

We realize \(\operatorname{Aut}M\) inside the isometry group of the Banach space \(M_*\).

**Proposition 2.2.** Let \(X\) be a separable Banach space and \(\operatorname{Isom}X\) the group of surjective
linear isometries of \(X\), topologized by pointwise convergence in norm. Then \(\operatorname{Isom}X\) is a
topological group, and it is Polish. More precisely, let \((\varphi_k)_{k\ge1}\) be a dense sequence in the unit ball
of \(X\); then
\[
d(S,T)=\sum_{k\ge1}2^{-k}\bigl(\|S\varphi_k-T\varphi_k\|+\|S^{-1}\varphi_k-T^{-1}\varphi_k\|\bigr)
\]
is a complete metric inducing the topology, and its uniform structure is the least upper bound of the left and the
right uniform structures of the group.

*Proof.* Group operations. If \(S_i\to S\) and \(T_i\to T\) pointwise, then
\(\|S_iT_i\varphi-ST\varphi\|\le\|T_i\varphi-T\varphi\|+\|(S_i-S)T\varphi\|\to0\), because \(S_i\) is isometric. If
\(T_i\to T\), then with \(\chi=T^{-1}\varphi\),
\[
\|T_i^{-1}\varphi-T^{-1}\varphi\|=\|T_i^{-1}(T\chi-T_i\chi)\|=\|T\chi-T_i\chi\|\to0 .
\]
So \(\operatorname{Isom}X\) is a topological group.

The metric. Since all operators involved are isometries, pointwise convergence on the dense set \(\{\varphi_k\}\) is
the same as pointwise convergence on \(X\). Hence \(d(S_i,S)\to0\) if and only if \(S_i\to S\) and
\(S_i^{-1}\to S^{-1}\) pointwise, and by continuity of inversion this is the same as \(S_i\to S\). The map
\(S\mapsto(S\varphi_k,S^{-1}\varphi_k)_k\) embeds \(\operatorname{Isom}X\) into the separable metrizable space
\((X\times X)^{\mathbb N}\), so \(\operatorname{Isom}X\) is separable. The left uniform structure has the entourages
\(\{(S,T):S^{-1}T\in\mathcal N\}\), \(\mathcal N=\{R:\|R\varphi_k-\varphi_k\|<\varepsilon,\ k\le m\}\), and
\(\|S^{-1}T\varphi_k-\varphi_k\|=\|T\varphi_k-S\varphi_k\|\); the right one has \(\{(S,T):ST^{-1}\in\mathcal N\}\) and
\(\|ST^{-1}\varphi_k-\varphi_k\|=\|S^{-1}\varphi_k-T^{-1}\varphi_k\|\). So the uniform structure of \(d\) is the least
upper bound of the two.

Completeness. Let \((T_n)\) be \(d\)-Cauchy. Then \((T_n\varphi_k)_n\) and \((T_n^{-1}\varphi_k)_n\) converge for
every \(k\), hence, by equicontinuity, \(T_n\varphi\to T\varphi\) and \(T_n^{-1}\varphi\to R\varphi\) for all
\(\varphi\), where \(T,R\) are linear isometries. Now \(\|T_nR\varphi-\varphi\|=\|R\varphi-T_n^{-1}\varphi\|\to0\)
while \(T_nR\varphi\to TR\varphi\), so \(TR=1\); in the same way \(RT=1\). Thus \(T\in\operatorname{Isom}X\),
\(R=T^{-1}\), and \(d(T_n,T)\to0\). \(\square\)

**Proposition 2.3.** Let \(M\) have separable predual. For \(\alpha\in\operatorname{Aut}M\) let
\(T_\alpha\varphi=\varphi\circ\alpha^{-1}\) (\(\varphi\in M_*\)). Then \(\alpha\mapsto T_\alpha\) is an injective
homomorphism of \(\operatorname{Aut}M\) onto a closed subgroup of \(\operatorname{Isom}M_*\), and it is a
homeomorphism onto its image when \(\operatorname{Aut}M\) has the \(u\)-topology. Consequently \(\operatorname{Aut}M\)
with the \(u\)-topology is a Polish group, and for a dense sequence \((\varphi_k)\) in the unit ball of \(M_*\),
\[
d(\alpha,\beta)=\sum_{k\ge1}2^{-k}\bigl(\|\varphi_k\circ\alpha-\varphi_k\circ\beta\|+
\|\varphi_k\circ\alpha^{-1}-\varphi_k\circ\beta^{-1}\|\bigr)
\]
is a complete metric on \(\operatorname{Aut}M\) inducing the \(u\)-topology and the two-sided uniform structure.

*Proof.* Each \(T_\alpha\) is a surjective linear isometry of \(M_*\), and
\(T_\alpha T_\beta\varphi=\varphi\circ\beta^{-1}\circ\alpha^{-1}=T_{\alpha\beta}\varphi\). Injectivity holds because
\(M_*\) separates the points of \(M\). By definition \(\alpha_i\to\alpha\) in the \(u\)-topology if and only if
\(T_{\alpha_i}^{-1}\to T_\alpha^{-1}\) pointwise, and by Proposition 2.2 this is equivalent to
\(T_{\alpha_i}\to T_\alpha\). So \(\alpha\mapsto T_\alpha\) is a homeomorphism onto its image, and the metric \(d\) is
the metric of Proposition 2.2 transported.

It remains to show that the image is closed. Since \(\operatorname{Isom}M_*\) is metrizable, let
\(T_{\alpha_n}\to T\in\operatorname{Isom}M_*\). Then \(T_{\alpha_n}^{-1}\to T^{-1}\) and \(T_{\alpha_n}\to T\)
pointwise, that is,
\[
\varphi\circ\alpha_n\to T^{-1}\varphi,\qquad \varphi\circ\alpha_n^{-1}\to T\varphi\qquad\text{in norm, for every }
\varphi\in M_*. \tag{2.1}
\]
Let \(\beta\) and \(\gamma\) be the transposes of \(T^{-1}\) and \(T\) on \(M=(M_*)^*\), so
\(\varphi(\beta(x))=(T^{-1}\varphi)(x)\) and \(\varphi(\gamma(x))=(T\varphi)(x)\). They are \(\sigma\)-weakly
continuous linear bijections with \(\gamma=\beta^{-1}\), and (2.1) says that \(\alpha_n(x)\to\beta(x)\) and
\(\alpha_n^{-1}(x)\to\gamma(x)\) \(\sigma\)-weakly, for every \(x\).

Fix \(a,b\in M\) and \(\varphi\in M_*\). On the one hand \(\varphi(\alpha_n(b)a)=(a\varphi)(\alpha_n(b))\to
\varphi(\beta(b)a)\). On the other hand \(\varphi(\alpha_n(b)a)=(\varphi\circ\alpha_n)(b\,\alpha_n^{-1}(a))\). Put
\(\varphi'=T^{-1}\varphi\). Since \(\|\varphi\circ\alpha_n-\varphi'\|\to0\) and \(\|b\alpha_n^{-1}(a)\|\le\|a\|\|b\|\),
\[
(\varphi\circ\alpha_n)(b\,\alpha_n^{-1}(a))-\varphi'(b\,\alpha_n^{-1}(a))\to0,\qquad
\varphi'(b\,\alpha_n^{-1}(a))=(\varphi'b)(\alpha_n^{-1}(a))\to\varphi'(b\gamma(a))=\varphi(\beta(b\gamma(a))).
\]
Hence \(\beta(b)a=\beta(b\gamma(a))\) for all \(a,b\); with \(a=\beta(c)\) this reads
\(\beta(b)\beta(c)=\beta(bc)\). Next, \(\varphi^*\circ\alpha_n=(\varphi\circ\alpha_n)^*\) because \(\alpha_n\)
preserves adjoints; letting \(n\to\infty\) gives \(\varphi^*(\beta(x))=\overline{\varphi(\beta(x^*))}\), i.e.
\(\varphi(\beta(x)^*)=\varphi(\beta(x^*))\) for all \(\varphi\), so \(\beta(x)^*=\beta(x^*)\). Thus \(\beta\) is a
normal \(\ast\)-automorphism of \(M\), and \(T_\beta\varphi=\varphi\circ\beta^{-1}=\varphi\circ\gamma=T\varphi\). So
\(T=T_\beta\) lies in the image. A closed subgroup of a Polish group is Polish (B3). \(\square\)

Now the unitary group. We use the elementary identities of the next lemma throughout.

**Lemma 2.4.** Let \(x,y\in M\), \(\varphi\in M_*\), \(\psi\in M_*^+\), and \(u\in\mathcal U(M)\).

- (a) \(\|\varphi\circ\operatorname{Ad}u-\varphi\|=\|[u,\varphi]\|\).
- (b) \(\|[x^*,\varphi]\|=\|[x,\varphi^*]\|\).
- (c) \([xy,\varphi]=x[y,\varphi]+[x,\varphi]y\), hence \(\|[xy,\varphi]\|\le\|x\|\|[y,\varphi]\|+\|y\|\|[x,\varphi]\|\).
- (d) \(\|x\psi\|\le\psi(1)^{1/2}\|x\|_\psi\), \(\|\psi x\|\le\psi(1)^{1/2}\|x^*\|_\psi\), hence
  \(\|[x,\psi]\|\le\sqrt2\,\psi(1)^{1/2}\|x\|^\#_\psi\).
- (e) If \(z\in\mathcal U(C)\), then \(\|zx\|^\#_\psi=\|x\|^\#_\psi\).

*Proof.* (a) \(\varphi(uyu^*)=(u^*\varphi u)(y)\), where \((a\varphi b)(y)=\varphi(bya)\). The map \(\chi\mapsto u\chi\)
is isometric on \(M_*\) and sends \(u^*\varphi u-\varphi\) to \(\varphi u-u\varphi\). (b) For \(y\in M\),
\([x,\varphi^*](y^*)=\overline{\varphi(x^*y)}-\overline{\varphi(yx^*)}=-\overline{[x^*,\varphi](y)}\), and \(y\mapsto
y^*\) preserves the unit ball. (c) By associativity of these operations (Section 1), \((xy)\varphi=x(y\varphi)\),
\(\varphi(xy)=(\varphi x)y\) and \(x(\varphi y)=(x\varphi)y\), so \([xy,\varphi]=x(y\varphi-\varphi y)+(x\varphi-\varphi x)y\); and \(\|x\chi\|,\|\chi x\|\le
\|x\|\|\chi\|\). (d) By the Cauchy–Schwarz inequality \(|\psi(yx)|\le\psi(yy^*)^{1/2}\psi(x^*x)^{1/2}\le\|y\|
\psi(1)^{1/2}\|x\|_\psi\), and \(|\psi(xy)|\le\psi(xx^*)^{1/2}\psi(y^*y)^{1/2}\). (e) \((zx)^*(zx)=x^*x\) and
\((zx)(zx)^*=zxx^*z^*=xx^*\) since \(z\) is central. \(\square\)

**Proposition 2.5.** Suppose \(M\) has separable predual, and fix a faithful normal state \(\varphi\) of \(M\).

- (a) On \(\mathcal U(M)\) the strong and strong\* topologies coincide, and \(\mathcal U(M)\) with this topology is a
  Polish group; \(D(u,v)=\|u-v\|^\#_\varphi\) is a complete metric inducing it.
- (b) The map \(u\mapsto\operatorname{Ad}u\) from \(\mathcal U(M)\) to \(\operatorname{Aut}M\) is a continuous
  homomorphism with kernel \(\mathcal U(C)\) and range \(\operatorname{Int}M\).
- (c) The quotient \(\underline{\mathcal U}(M)=\mathcal U(M)/\mathcal U(C)\), with the quotient topology, is a Polish
  group. The formula \(\rho(u\,\mathcal U(C),v\,\mathcal U(C))=\inf_{z\in\mathcal U(C)}\|u-vz\|^\#_\varphi\) defines a
  complete metric inducing that topology. If \((V_n)\) is a basis of strong\* neighbourhoods of \(0\) in \(M\), the
  images of the sets \(\mathcal U(M)\cap(1+V_n)\) form a basis of neighbourhoods of the identity of
  \(\underline{\mathcal U}(M)\).
- (d) \(u\mapsto\operatorname{Ad}u\) induces a continuous injective homomorphism \(\underline{\operatorname{Ad}}\) of
  \(\underline{\mathcal U}(M)\) onto \(\operatorname{Int}M\).

*Proof.* (a) Let \(u_i\to u\) strongly in \(\mathcal U(M)\) and \(\psi\in M_*^+\). Then
\(\|(u_i-u)^*\|_\psi^2=2\psi(1)-2\operatorname{Re}\psi(u_iu^*)\) and, by the Cauchy–Schwarz inequality,
\[
|\psi(u_iu^*)-\psi(1)|=|\psi((u_i-u)u^*)|\le\psi(1)^{1/2}\,\psi\bigl(u(u_i-u)^*(u_i-u)u^*\bigr)^{1/2}
=\psi(1)^{1/2}\|u_i-u\|_{\psi\circ\operatorname{Ad}u}\to0 .
\]
So the two topologies agree on \(\mathcal U(M)\). Multiplication is jointly strongly continuous on bounded sets and
inversion is the adjoint, which is strong\* continuous; so \(\mathcal U(M)\) is a topological group. By (B1) the metric
\(D\) induces the strong\* topology on \(\mathcal U(M)\) and \(\mathcal U(M)\) is separable. Completeness: let
\((u_n)\) be \(D\)-Cauchy. In the GNS representation of \(\varphi\), \((u_n\xi_\varphi)\) and
\((u_n^*\xi_\varphi)\) are Cauchy, hence so are \((u_na'\xi_\varphi)=(a'u_n\xi_\varphi)\) and
\((u_n^*a'\xi_\varphi)\) for \(a'\in M'\). As \(M'\xi_\varphi\) is dense and \(\|u_n\|=1\), \(u_n\to u\) and
\(u_n^*\to w\) strongly for some \(u,w\in M\), and \(\langle u_n^*\xi,\eta\rangle=\langle\xi,u_n\eta\rangle\) gives
\(w=u^*\). Products of strongly convergent bounded sequences converge strongly, so \(u^*u=\lim u_n^*u_n=1\) and
\(uu^*=1\). Hence \(u\in\mathcal U(M)\) and \(D(u_n,u)\to0\).

(b) \(\operatorname{Ad}\) is a homomorphism, and \(\operatorname{Ad}u=1\) means \(u\in M'\cap M=C\). By Lemma 2.4(a),
\(\|\varphi\circ\operatorname{Ad}u-\varphi\|=\|[u,\varphi]\|=\|[u-1,\varphi]\|\), and by Lemma 2.4(d) (applied to the
four positive parts of \(\varphi\), (B1)) this tends to \(0\) when \(u\to1\) strongly\*. So \(\operatorname{Ad}\) is
continuous at \(1\), hence everywhere, since both groups are topological groups.

(c) \(\mathcal U(C)\) is closed and central. By Lemma 2.4(e), \(\|zy\|^\#_\varphi=\|yz\|^\#_\varphi=
\|y\|^\#_\varphi\) for \(z\in\mathcal U(C)\). Therefore the infimum defining \(\rho\) does not depend on the chosen
representatives, and \(\rho\) is symmetric: \(\|u-vz\|^\#_\varphi=\|(uz^*-v)z\|^\#_\varphi=\|v-uz^*\|^\#_\varphi\).
The triangle inequality follows from \(\|u-wz_1z_2\|^\#_\varphi\le\|u-vz_1\|^\#_\varphi+\|v-wz_2\|^\#_\varphi\). If
\(\rho=0\), there are \(z_n\in\mathcal U(C)\) with \(vz_n\to u\) strongly\*, hence \(z_n\to v^*u\) strongly\* and
\(v^*u\in\mathcal U(C)\), since \(\mathcal U(C)\) is strong\* closed; so the two cosets are equal. The open
\(\rho\)-ball about \(u\,\mathcal U(C)\) of radius \(r\) is the image of the open \(D\)-ball about \(u\) of radius
\(r\); since the quotient map is open and the \(D\)-balls form a basis of \(\mathcal U(M)\), \(\rho\) induces the
quotient topology, and the last assertion of (c) follows. Separability passes to the quotient. Completeness: given a
\(\rho\)-Cauchy sequence, pass to a subsequence with \(\rho(\underline{u_n},\underline{u_{n+1}})<2^{-n}\) and choose
representatives inductively, \(u_{n+1}\) in its coset with \(D(u_n,u_{n+1})<2^{-n}\). Then \((u_n)\) is \(D\)-Cauchy,
converges to some \(u\) by (a), and \(\rho(\underline{u_n},\underline u)\le D(u_n,u)\to0\). A Cauchy sequence with a
convergent subsequence converges. The quotient of a topological group by a closed normal subgroup is a topological
group.

(d) follows from (b) and the universal property of the quotient. \(\square\)

## 3. The open mapping theorem for Polish groups



**Lemma 3.1 (Pettis lemma).** Let \(K\) be a topological group which is a Baire space, and let \(A\subset K\) be a
non-meager set with the Baire property. Then \(AA^{-1}\) is a neighbourhood of the identity.

*Proof.* There is an open set \(U\) with \(U\setminus A\) meager; \(U\neq\emptyset\) because \(A\) is not meager. Fix
\(u_0\in U\) and put \(\mathcal N=Uu_0^{-1}\), an open neighbourhood of \(1\). Let \(k\in\mathcal N\). Then
\(ku_0\in U\cap kU\), so \(O=U\cap kU\) is open and nonempty. Now \(O\setminus A\subset U\setminus A\) is meager and
\(O\setminus kA\subset k(U\setminus A)\) is meager, because left translation is a homeomorphism. So
\(O\setminus(A\cap kA)\) is meager. As \(K\) is a Baire space, \(O\) is not meager, and \(A\cap kA\neq\emptyset\). If
\(a=ka'\) with \(a,a'\in A\), then \(k=a a'^{-1}\in AA^{-1}\). Hence \(\mathcal N\subset AA^{-1}\). \(\square\)

**Theorem 3.2 (open mapping theorem).** Let \(G\) and \(K\) be Polish groups and \(f:G\to K\) a continuous surjective
homomorphism. Then \(f\) is open.

*Proof.* Take a neighbourhood \(V\) of \(1\) in \(G\), and choose an open neighbourhood \(W\) of \(1\) with
\(WW^{-1}\subset V\). Let \((g_n)\) be dense in \(G\). For \(g\in G\) the open set \(gW^{-1}\) contains some \(g_n\),
so \(g\in g_nW\); thus \(G=\bigcup_ng_nW\) and \(K=\bigcup_nf(g_n)f(W)\). By the Baire category theorem (B3) some
\(f(g_n)f(W)\) is not meager, hence neither is \(f(W)\). As \(W\) is Polish (B3), \(f(W)\) is analytic and has the
Baire property. By Lemma 3.1, \(f(V)\supset f(W)f(W)^{-1}\) is a neighbourhood of \(1\) in \(K\). Finally, if
\(O\subset G\) is open and \(g\in O\), then \(f(O)=f(g)f(g^{-1}O)\) contains a neighbourhood of \(f(g)\). \(\square\)

**Corollary 3.3.** A continuous bijective homomorphism between Polish groups is a homeomorphism. \(\square\)

## 4. Full von Neumann algebras

In this section \(M\) has separable predual and \(C\) is its centre. A reference for this section is [Connes 1974].

We first record that centralizing families form an algebra closed under continuous functional calculus.

**Lemma 4.1.** Let \(\mathcal F\) be a filter on a set \(I\).

- (a) The bounded families centralizing along \(\mathcal F\) form a unital \(\ast\)-algebra.
- (b) If \((a_i)\) is centralizing along \(\mathcal F\), each \(a_i\) is self-adjoint with spectrum in \([\alpha,\beta]\),
  and \(f\) is continuous on \([\alpha,\beta]\), then \((f(a_i))\) is centralizing along \(\mathcal F\).
- (c) If \((x_i)\) is centralizing along \(\mathcal F\) and \((y_i)\) is bounded with \(x_i-y_i\to0\) strong\* along
  \(\mathcal F\), then \((y_i)\) is centralizing along \(\mathcal F\).

*Proof.* (a) Sums and scalar multiples are clear; adjoints by Lemma 2.4(b), since \(\varphi^*\) ranges over \(M_*\)
with \(\varphi\); products by Lemma 2.4(c). (b) For a polynomial \(p(t)=\sum c_kt^k\), Lemma 2.4(c) gives
\(\|[a_i^k,\varphi]\|\le k\|a_i\|^{k-1}\|[a_i,\varphi]\|\), so \((p(a_i))\) is centralizing. Given \(\varepsilon>0\)
choose \(p\) with \(|f-p|\le\varepsilon\) on \([\alpha,\beta]\); then
\(\|[f(a_i)-p(a_i),\varphi]\|\le2\varepsilon\|\varphi\|\). (c) By Lemma 2.4(d),
\(\|[x_i-y_i,\psi]\|\le\sqrt2\psi(1)^{1/2}\|x_i-y_i\|^\#_\psi\to0\) for \(\psi\ge0\), and every \(\varphi\in M_*\) is
a combination of four such \(\psi\). \(\square\)

**Theorem 4.2.** Suppose the von Neumann algebra \(M\) has separable predual, and let \(C\) be its centre. The
following are equivalent.

- (a) \(\operatorname{Int}M\) is closed in \(\operatorname{Aut}M\) for the \(u\)-topology.
- (b) The homomorphism \(u\mapsto\operatorname{Ad}u\) from \(\mathcal U(M)\), with the strong topology, onto
  \(\operatorname{Int}M\), with the relative \(u\)-topology, is open. Equivalently,
  \(\underline{\operatorname{Ad}}:\underline{\mathcal U}(M)\to\operatorname{Int}M\) is an isomorphism of topological
  groups.
- (c) For every strong\* neighbourhood \(V\) of \(0\) in \(M\) there are \(\varphi_1,\dots,\varphi_n\in M_*\) and
  \(\varepsilon>0\) such that every \(u\in\mathcal U(M)\) with \(\|[u,\varphi_j]\|<\varepsilon\) for all \(j\) lies in
  \(\mathcal U(C)+V\).
- (d) For every set \(I\), every filter \(\mathcal F\) on \(I\) and every family \((x_i)_{i\in I}\) centralizing along
  \(\mathcal F\), there is a bounded family \((z_i)_{i\in I}\) in \(C\) with \(x_i-z_i\to0\) strong\* along
  \(\mathcal F\).
- (e) For every centralizing sequence \((x_n)\) there is a bounded sequence \((z_n)\) in \(C\) with \(x_n-z_n\to0\)
  strong\*.

*Reference:* [Connes 1974].

By Lemma 2.4(a), \(\|[u,\varphi_j]\|=\|\varphi_j\circ\operatorname{Ad}u-\varphi_j\|\), so (c) says: for every \(V\) there
is a neighbourhood \(\mathcal W\) of the identity in \(\operatorname{Aut}M\) with
\(\{u\in\mathcal U(M):\operatorname{Ad}u\in\mathcal W\}\subset\mathcal U(C)+V\).

*Proof.* We prove (a)⇒(b)⇒(c)⇒(d)⇒(e)⇒(c)⇒(a). Fix a faithful normal state \(\varphi\) on \(M\). By Lemma 2.4(e),
the strong\* neighbourhoods
\[
V(\psi_1,\dots,\psi_m;\delta)=\{x\in M\mid\|x\|^\#_{\psi_k}<\delta,\ k=1,\dots,m\}\qquad(\psi_k\in M_*^+,\ \delta>0),
\]
which form a basis at \(0\), satisfy \(zV=V\) for \(z\in\mathcal U(C)\).

(a)⇒(b). \(\operatorname{Int}M\) is a closed subgroup of the Polish group \(\operatorname{Aut}M\) (Proposition 2.3),
hence a Polish group. The map \(\operatorname{Ad}:\mathcal U(M)\to\operatorname{Int}M\) is a continuous surjective
homomorphism of Polish groups (Proposition 2.5), hence open by Theorem 3.2. Since the quotient map
\(\mathcal U(M)\to\underline{\mathcal U}(M)\) is continuous and surjective, \(\underline{\operatorname{Ad}}\) is then
open as well; being a continuous bijection, it is an isomorphism of topological groups.

(b)⇒(c). Let \(V\) be a strong\* neighbourhood of \(0\); we may take \(V\) basic, so \(zV=V\) for central unitaries
\(z\). The set \(\mathcal O=\{v\in\mathcal U(M):v-1\in V\}\) is a neighbourhood of \(1\) in \(\mathcal U(M)\). By (b),
\(\operatorname{Ad}(\mathcal O)\) contains \(\mathcal W\cap\operatorname{Int}M\) for some basic neighbourhood
\(\mathcal W=\mathcal W(\varphi_1,\dots,\varphi_n;\varepsilon)\) of the identity. If \(\|[u,\varphi_j]\|<\varepsilon\)
for all \(j\), then \(\operatorname{Ad}u\in\mathcal W\), so \(\operatorname{Ad}u=\operatorname{Ad}v\) with
\(v\in\mathcal O\), and \(z=v^*u\) is a central unitary. Then \(u-z=zv-z=z(v-1)\in zV=V\).

(c)⇒(d). Let \((x_i)\) be centralizing along \(\mathcal F\). Writing \(x_i=a_i+ib_i\) with \(a_i,b_i\) self-adjoint,
Lemma 4.1(a) shows that \((a_i)\) and \((b_i)\) are centralizing, so it suffices to treat a self-adjoint family, and
after scaling we may assume \(\|a_i\|\le1\). Put \(c_i=(1+a_i)/4\), with spectrum in \([0,1/2]\), and
\[
w_i=c_i+i(1-c_i^2)^{1/2}.
\]
Each \(w_i\) is unitary, \(c_i=(w_i+w_i^*)/2\), and \((w_i)\) is centralizing along \(\mathcal F\) by Lemma 4.1(a),(b).
Let \(d_i=\inf\{\|w_i-z\|^\#_\varphi:z\in\mathcal U(C)\}\).

We claim \(d_i\to0\) along \(\mathcal F\). Let \(\varepsilon>0\) and \(V=\{x:\|x\|^\#_\varphi<\varepsilon\}\). By (c) there
are \(\varphi_1,\dots,\varphi_n\) and \(\delta>0\) such that \(\|[w_i,\varphi_j]\|<\delta\) for all \(j\) implies
\(w_i\in\mathcal U(C)+V\), that is, \(d_i<\varepsilon\). The set of such \(i\) belongs to \(\mathcal F\).

Choose \(z_i\in\mathcal U(C)\) as follows. If \(d_i>0\), take \(z_i\) with \(\|w_i-z_i\|^\#_\varphi<2d_i\). If
\(d_i=0\), then \(w_i\) is a strong\* limit of central unitaries (B1), hence a central unitary, and we take
\(z_i=w_i\). Then \(\|w_i-z_i\|^\#_\varphi\to0\) along \(\mathcal F\), and since \(\|w_i-z_i\|\le2\), (B1) gives
\(w_i-z_i\to0\) strong\* along \(\mathcal F\); so does \(w_i^*-z_i^*\). Hence
\[
a_i-\bigl(2(z_i+z_i^*)-1\bigr)=4c_i-1-2(z_i+z_i^*)+1=2(w_i-z_i)+2(w_i^*-z_i^*)\to0
\]
strong\* along \(\mathcal F\), and \(2(z_i+z_i^*)-1\) is a central element of norm at most \(5\).

(d)⇒(e) is the special case of the cofinite filter on \(\mathbb N\).

(e)⇒(c). Suppose (c) fails for some strong\* neighbourhood \(V\) of \(0\). The \(u\)-topology is metrizable
(Proposition 2.3), so there is a decreasing basis \((\mathcal W_n)\) of neighbourhoods of the identity, and unitaries
\(u_n\) with \(\operatorname{Ad}u_n\in\mathcal W_n\) and \(u_n\notin\mathcal U(C)+V\). Then
\(\|[u_n,\psi]\|=\|\psi\circ\operatorname{Ad}u_n-\psi\|\to0\) for all \(\psi\in M_*\): the sequence \((u_n)\) is
centralizing. By (e) there are bounded \(z_n\in C\) with \(u_n-z_n\to0\) strong\*. We replace \(z_n\) by central
unitaries. Since \(z_n\) is central,
\[
z_n^*z_n-1=z_n^*(z_n-u_n)+(z_n^*-u_n^*)u_n=z_n^*(z_n-u_n)+u_n(z_n^*-u_n^*)\to0\quad\text{strongly}.
\]
Let \(z_n=v_n|z_n|\) with \(v_n\in\mathcal U(C)\) (polar decomposition in the abelian algebra \(C\)). As
\(1-|z_n|=(1+|z_n|)^{-1}(1-z_n^*z_n)\) and \(0\le(1+|z_n|)^{-1}\le1\) commutes with everything involved,
\(\|(1-|z_n|)\xi\|\le\|(1-z_n^*z_n)\xi\|\) in any representation, so \(|z_n|\to1\) strongly. Therefore
\(v_n-z_n=v_n(1-|z_n|)\) and \((v_n-z_n)^*=v_n^*(1-|z_n|)\) tend to \(0\) strongly, i.e. \(v_n-z_n\to0\) strong\*.
So \(u_n-v_n\to0\) strong\*, and \(u_n-v_n\in V\) for large \(n\), a contradiction.

(c)⇒(a). Let \(\theta\) be in the closure of \(\operatorname{Int}M\). Put \(\psi=\varphi+\varphi\circ\theta\), a
faithful element of \(M_*^+\), and \(V_n=\{x:\|x\|^\#_\psi<2^{-n}\}\). By (c) choose neighbourhoods \(\mathcal W_n\) of
the identity with \(\{u:\operatorname{Ad}u\in\mathcal W_n\}\subset\mathcal U(C)+V_n\). As \(\operatorname{Aut}M\) is
metrizable, there are unitaries \(v_m\) with \(\operatorname{Ad}v_m\to\theta\). By continuity of
\((\alpha,\beta)\mapsto\alpha^{-1}\beta\) at \((\theta,\theta)\), and because \(\|\varphi\circ\operatorname{Ad}v_m-
\varphi\circ\theta\|\to0\), we may pass to a subsequence and assume, for all \(n\),
\[
\operatorname{Ad}(v_{n+1}^*v_n)=(\operatorname{Ad}v_{n+1})^{-1}\operatorname{Ad}v_n\in\mathcal W_n,\qquad
\|\varphi\circ\operatorname{Ad}v_{n+1}-\varphi\circ\theta\|<4^{-n}.
\]
So there are \(c_n\in\mathcal U(C)\) with \(y_n=c_n-v_{n+1}^*v_n\) satisfying \(\|y_n\|^\#_\psi<2^{-n}\); in
particular \(\varphi(y_n^*y_n)<4^{-n}\) and \((\varphi\circ\theta)(y_ny_n^*)<4^{-n}\). Put \(\gamma_1=1\),
\(\gamma_{n+1}=c_n\gamma_n\in\mathcal U(C)\) and \(u_n=v_n\gamma_n\). Then
\[
u_{n+1}-u_n=v_{n+1}c_n\gamma_n-v_n\gamma_n=v_{n+1}y_n\gamma_n .
\]
Since \(\gamma_n\) is a central unitary, \(\varphi((u_{n+1}-u_n)^*(u_{n+1}-u_n))=\varphi(y_n^*y_n)<4^{-n}\), and, using
\(\|y_n\|\le2\),
\[
\varphi\bigl((u_{n+1}-u_n)(u_{n+1}-u_n)^*\bigr)=(\varphi\circ\operatorname{Ad}v_{n+1})(y_ny_n^*)
\le(\varphi\circ\theta)(y_ny_n^*)+4\cdot4^{-n}<5\cdot4^{-n}.
\]
Thus \(\sum_n\|u_{n+1}-u_n\|^\#_\varphi<\infty\), and by Proposition 2.5(a) \(u_n\to u\) strong\* for some
\(u\in\mathcal U(M)\). For \(x\in M\), \(u_nxu_n^*=v_nxv_n^*\to\theta(x)\) \(\sigma\)-weakly (because
\(\chi(\operatorname{Ad}v_n(x))\to\chi(\theta(x))\) for every \(\chi\in M_*\)), while \(u_nxu_n^*\to uxu^*\) strongly
(products of strong\* convergent bounded sequences). Hence \(\theta=\operatorname{Ad}u\in\operatorname{Int}M\).
\(\square\)

**Definition 4.3.** A von Neumann algebra whose predual is separable is *full* if it satisfies the equivalent conditions
of Theorem 4.2. The word "full" alludes to a completeness property: by Proposition 2.3, \(\operatorname{Int}M\) is closed exactly when it
is complete for the two-sided uniform structure of \(\operatorname{Aut}M\).

**Remark 4.4.** In (c) one may use strong neighbourhoods instead of strong\* ones. Indeed, for a unitary \(u\) and a
central unitary \(z\), put \(w=z^*u\). Then \((u-z)^*(u-z)=(w-1)^*(w-1)=2-w-w^*=(w-1)(w-1)^*=(u-z)(u-z)^*\), so
\(\|u-z\|_\psi=\|(u-z)^*\|_\psi\) for every \(\psi\in M_*^+\).

**Example 4.5.**

- (a) An abelian von Neumann algebra is full: \(\operatorname{Int}M=\{1\}\). In (d) one simply takes \(z_i=x_i\).
- (b) \(\mathbb C\) is full, and so is \(B(H)\) for separable \(H\); this follows from Proposition 10.1 below, and also
  from the classical fact that every automorphism of \(B(H)\) is inner.
- (c) A direct sum \(M_1\oplus M_2\) is full if and only if \(M_1\) and \(M_2\) are full (Exercise 2).

## 5. Full factors and the asymptotic centralizer

For a factor, \(C=\mathbb C\) and fullness becomes a statement about centralizing sequences. A bounded sequence
\((x_n)\) is *trivial* if there are scalars \(\lambda_n\) with \(x_n-\lambda_n\to0\) strong\*.

**Lemma 5.1.** Suppose \(M\) is a full factor whose predual is separable, \(\varphi\) is a faithful normal state of
\(M\), and \(\mathcal F\) is a filter on a set \(I\). If \((x_i)\) is centralizing along \(\mathcal F\), then
\(x_i-\varphi(x_i)\to0\) strong\* along \(\mathcal F\).

*Proof.* By Theorem 4.2(d) there are bounded scalars \(\lambda_i\) with \(x_i-\lambda_i\to0\) strong\*. Then
\(|\varphi(x_i)-\lambda_i|\le\|x_i-\lambda_i\|_\varphi\to0\), and
\(x_i-\varphi(x_i)=(x_i-\lambda_i)+(\lambda_i-\varphi(x_i))\). \(\square\)

**Corollary 5.2.** For a factor \(M\) with separable predual the following are equivalent:

- (i) \(M\) is full;
- (ii) every centralizing sequence in \(M\) is trivial;
- (iii) \(M_\omega=\mathbb C\) for every free ultrafilter \(\omega\) on \(\mathbb N\);
- (iv) \(M_\omega=\mathbb C\) for some free ultrafilter \(\omega\) on \(\mathbb N\).

*Proof.* (i)⇔(ii) is Theorem 4.2 (a)⇔(e) with \(C=\mathbb C\) (if \(x_n-\lambda_n\to0\) strong\*, then
\(|\lambda_n|\le\sup_k\|x_k\|+1\) for large \(n\), and changing finitely many \(\lambda_n\) makes them bounded). (i)⇒(iii): if \((x_n)\in A_\omega\), Lemma 5.1 with
\(\mathcal F=\omega\) gives \(x_n-\varphi(x_n)\to0\) strong\* along \(\omega\). With
\(\lambda=\lim_{n\to\omega}\varphi(x_n)\), also \(x_n-\lambda\to0\) strong\* along \(\omega\), so the class of
\((x_n)\) is \(\lambda\). (iii)⇒(iv) is clear. (iv)⇒(ii): suppose \((x_n)\) is a centralizing sequence that is not
trivial, and fix a faithful normal state \(\varphi\). For every \(\lambda\in\mathbb C\),
\(\|x-\lambda\|_\varphi\ge\|x-\varphi(x)\|_\varphi\) and \(\|(x-\lambda)^*\|_\varphi\ge\|x^*-\overline{\varphi(x)}\|
_\varphi\), because \(\varphi(x)\) and \(\overline{\varphi(x)}\) are the coefficients of the orthogonal projections of
\(x\xi_\varphi\) and \(x^*\xi_\varphi\) onto \(\mathbb C\xi_\varphi\). So \(d_n=\|x_n-\varphi(x_n)\|^\#_\varphi\) does
not tend to \(0\) (otherwise \((x_n)\) would be trivial with \(\lambda_n=\varphi(x_n)\), by (B1)), and there are
\(\varepsilon>0\) and a subsequence \(y_k=x_{n_k}\) with \(\|y_k-\lambda\|^\#_\varphi\ge\varepsilon\) for all \(k\) and
all \(\lambda\in\mathbb C\). The sequence \((y_k)\) is centralizing, hence in \(A_\omega\) for every \(\omega\). If its
class were a scalar \(\lambda\), then \(\|y_k-\lambda\|^\#_\varphi\to0\) along \(\omega\), which is impossible. So
\(M_\omega\ne\mathbb C\) for every \(\omega\). \(\square\)

**Corollary 5.3.** Let \(M\) be a factor whose predual is separable. If every central sequence \((x_n)\) in \(M\) is
trivial in the weak sense that \(x_n-\lambda_n\to0\) strongly for some scalars \(\lambda_n\), then \(M\) is full.

*Proof.* We check (ii) of Corollary 5.2. Let \((x_n)\) be centralizing. By Proposition 1.2(a) it is central, and so is
\((x_n^*)\) (Lemma 4.1(a)). So \(x_n-\lambda_n\to0\) and \(x_n^*-\mu_n\to0\) strongly. With a faithful normal state
\(\varphi\), \(|\varphi(x_n)-\lambda_n|\le\|x_n-\lambda_n\|_\varphi\to0\) and likewise
\(\overline{\varphi(x_n)}-\mu_n\to0\). Hence \(x_n-\varphi(x_n)\to0\) and \(x_n^*-\overline{\varphi(x_n)}\to0\)
strongly, that is, \(x_n-\varphi(x_n)\to0\) strong\*. \(\square\)

For factors of type II₁ the converse holds as well, since there central and centralizing sequences coincide
(Lemma 6.2). For general factors the hypothesis of Corollary 5.3 is stronger than fullness a priori, because a central
sequence need not be centralizing.

## 6. Factors of type II₁: fullness and property Γ

In this section \(M\) is a factor of type II₁ with separable predual and trace \(\tau\), and
\(\|x\|_2=\tau(x^*x)^{1/2}\). Recall \(\|xy\|_2\le\|x\|\|y\|_2\), \(\|xy\|_2\le\|x\|_2\|y\|\), \(\|x^*\|_2=\|x\|_2\), and
\(|\tau(x)|\le\|x\|_1\le\|x\|_2\) where \(\|x\|_1=\tau(|x|)\).

**Definition 6.1 (property Γ).** \(M\) has *property Γ* if for every \(\varepsilon>0\) and every finite set
\(y_1,\dots,y_k\in M\) there is a unitary \(u\in M\) with \(\tau(u)=0\) and \(\|uy_j-y_ju\|_2<\varepsilon\) for all
\(j\).

*Reference:* the definition is due to Murray and von Neumann.

**Lemma 6.2.** Let \(\mathcal F\) be a filter on a set \(I\) and \((x_i)\) a bounded family in \(M\). The following are
equivalent: (i) \((x_i)\) is centralizing along \(\mathcal F\); (ii) \((x_i)\) is central along \(\mathcal F\);
(iii) \(\|[x_i,y]\|_2\to0\) along \(\mathcal F\) for every \(y\in M\).

*Proof.* (i)⇒(ii) is Proposition 1.2(a). (ii)⇔(iii) because \(\|\cdot\|_2\) gives the strong\* topology on bounded sets
(B5). (iii)⇒(i): \([x_i,\tau]=0\) since \(\tau\) is a trace, so Proposition 1.2(b) applies with \(\varphi=\tau\) and
\(\mathcal S=M\). \(\square\)

**Lemma 6.3 (asymptotic independence).** Let \((y_i)\) be bounded and central along a filter \(\mathcal F\). Then for
every \(x\in M\), \(\tau(xy_i)-\tau(x)\tau(y_i)\to0\) along \(\mathcal F\).

*Proof.* For a unitary \(u\), \(\tau(uxu^*y_i)=\tau(xu^*y_iu)\), so
\[
|\tau(uxu^*y_i)-\tau(xy_i)|\le\|x\|\,\|u^*y_iu-y_i\|_1\le\|x\|\,\|y_iu-uy_i\|_2 .
\]
Let \(\delta>0\). By the Dixmier approximation theorem (B5) there are unitaries \(u_1,\dots,u_m\) and weights
\(t_k\ge0\), \(\sum t_k=1\), with \(\|x'-\lambda\|<\delta\) for \(x'=\sum_kt_ku_kxu_k^*\) and some scalar \(\lambda\);
since \(\tau(x')=\tau(x)\), \(|\lambda-\tau(x)|<\delta\) and \(\|x'-\tau(x)\|<2\delta\). Then
\[
|\tau(xy_i)-\tau(x)\tau(y_i)|\le|\tau(xy_i)-\tau(x'y_i)|+|\tau((x'-\tau(x))y_i)|\le
\|x\|\sum_kt_k\|[y_i,u_k]\|_2+2\delta\sup_i\|y_i\|,
\]
and the first term tends to \(0\) along \(\mathcal F\). \(\square\)

Let \(\omega\) be a free ultrafilter on \(\mathbb N\). By Lemma 6.2, \(A_\omega\) is the set of bounded sequences
with \(\|[x_n,y]\|_2\to0\) along \(\omega\) for all \(y\); a bounded sequence lies in \(I_\omega\) exactly when
\(\|x_n\|_2\to0\) along \(\omega\); and by Theorem 1.3 the trace \(\tau_\omega(x)=\lim_{n\to\omega}\tau(x_n)\) is a
faithful normal tracial state on the von Neumann algebra \(M_\omega\).

**Lemma 6.4 (lifting projections).** Every projection \(e\in M_\omega\) is the class of a sequence \((e_n)\) of
projections of \(M\), and every such sequence lies in \(A_\omega\).

*Proof.* Let \((x_n)\in A_\omega\) represent \(e\). Then \(a_n=(x_n+x_n^*)/2\) also represents \(e\), and
\(\|a_n^2-a_n\|_2\to0\) along \(\omega\). Denote by \(e_n\) the spectral projection of \(a_n\) for \([1/2,\infty[\). For
real \(t\), \(|\chi_{[1/2,\infty[}(t)-t|\le2|t^2-t|\): for \(t\ge1/2\) because \(2|t|\ge1\), for \(t<1/2\) because
\(2|t-1|\ge1\). By functional calculus, \(\|e_n-a_n\|_2\le2\|a_n^2-a_n\|_2\to0\) along \(\omega\). So \((e_n)\)
represents \(e\), and \(\|[e_n,y]\|_2\le\|[a_n,y]\|_2+2\|y\|\|e_n-a_n\|_2\to0\) along \(\omega\). The same estimate
shows that any bounded sequence differing from an element of \(A_\omega\) by an element of \(I_\omega\) is in
\(A_\omega\). \(\square\)

**Theorem 6.5.** A factor \(M\) of type II₁ with separable predual is full if and only if it does not have property
Γ.

*Proof.* Suppose \(M\) has property Γ. Let \((y_j)\) be a sequence dense in the unit ball of \(M\) for \(\|\cdot\|_2\)
(B1), and choose unitaries \(u_n\) with \(\tau(u_n)=0\) and \(\|[u_n,y_j]\|_2<1/n\) for \(j\le n\). For \(y\) in the
unit ball and any \(j\), \(\|[u_n,y]\|_2\le\|[u_n,y_j]\|_2+2\|y-y_j\|_2\), so \(\|[u_n,y]\|_2\to0\) for every \(y\).
By Lemma 6.2, \((u_n)\) is centralizing. If it were trivial, \(u_n-\lambda_n\to0\) strongly, then
\(\lambda_n=\tau(\lambda_n-u_n)\to0\) and \(\|u_n\|_2\to0\), contradicting \(\|u_n\|_2=1\). By Corollary 5.2, \(M\) is
not full.

Conversely, suppose \(M\) is not full, and fix a free ultrafilter \(\omega\). By Corollary 5.2, \(M_\omega\neq\mathbb C\).

*Step 1: \(M_\omega\) has no minimal projection.* Let \(e\neq0\) be a projection of \(M_\omega\). If \(e=1\), it is not
minimal, because \(M_\omega\neq\mathbb C\) contains a projection different from \(0\) and \(1\). Otherwise
\(\lambda=\tau_\omega(e)\in\,]0,1[\) by faithfulness. By Lemma 6.4, let \((e_n)\) be projections representing \(e\);
then \(\tau(e_n)\to\lambda\) along \(\omega\). Let \((y_j)\) be \(\|\cdot\|_2\)-dense in the unit ball of \(M\). For
each \(n\) the following conditions on \(k\) each hold for all \(k\) in a set belonging to \(\omega\): 

- \(\|[e_n,e_k]\|_2<1/n\) (because \((e_k)\) is central along \(\omega\));
- \(|\tau(e_ne_k)-\lambda\tau(e_n)|<1/n\) (by Lemma 6.3 with \(x=e_n\), and \(\tau(e_k)\to\lambda\) along \(\omega\));
- \(\|[e_k,y_j]\|_2<1/n\) for \(j\le n\).

Choose such a \(k=k_n\) and put \(f_n=e_{k_n}\). The third condition gives \(\|[f_n,y]\|_2\to0\) for every \(y\) as
\(n\to\infty\), since \(\|[f_n,y-y_j]\|_2\le2\|y-y_j\|_2\) for \(y\) in the unit ball. Hence \((f_n)\) is central
along the cofinite filter, and so along \(\omega\). The product \(g_n=e_nf_n\) is then in \(A_\omega\) (Lemma 4.1(a)
and Lemma 6.2). Let \(g\) be its class. From \(\|[e_n,f_n]\|_2<1/n\):
\[
g_n^*-g_n=f_ne_n-e_nf_n\to0,\qquad g_n^2-g_n=e_n(f_ne_n-e_nf_n)f_n\to0\quad\text{in }\|\cdot\|_2,
\]
so \(g\) is a projection. Also \(eg=g\), so \(g\le e\), and \(\tau_\omega(g)=\lim_{n\to\omega}\tau(e_nf_n)=
\lim_{n\to\omega}\lambda\tau(e_n)=\lambda^2\in\,]0,\lambda[\). So \(g\) is a nonzero projection strictly below \(e\).

*Step 2: a projection of trace \(1/2\).* Every nonzero projection \(q\) of \(M_\omega\) has a subprojection \(q'\) with
\(0<\tau_\omega(q')\le\tau_\omega(q)/2\): split \(q=q_1+(q-q_1)\) with \(0\neq q_1\neq q\) (Step 1) and take the
smaller piece. Iterating, \(q\) has nonzero subprojections of arbitrarily small trace. By Zorn's lemma, choose a
projection \(p\) maximal among projections with \(\tau_\omega(p)\le1/2\) (the supremum of a chain is a projection with
trace equal to the supremum of the traces, by normality). If \(\tau_\omega(p)<1/2\), then \(1-p\neq0\) has a nonzero
subprojection \(q\) with \(\tau_\omega(q)\le1/2-\tau_\omega(p)\), and \(p+q\) contradicts maximality. So
\(\tau_\omega(p)=1/2\).

*Step 3: property Γ.* By Lemma 6.4 let \((p_n)\) be projections of \(M\) representing \(p\), so \(t_n=\tau(p_n)\to1/2\)
along \(\omega\). By (B5) choose a projection \(p_n'\) with \(\tau(p_n')=1/2\), with \(p_n'\le p_n\) if \(t_n\ge1/2\)
and \(p_n'\ge p_n\) otherwise; then \(\|p_n-p_n'\|_2=|t_n-1/2|^{1/2}\to0\) along \(\omega\). The unitaries
\(u_n=2p_n'-1\) satisfy \(\tau(u_n)=0\) and
\(\|[u_n,y]\|_2\le2\|[p_n,y]\|_2+4\|y\|\|p_n-p_n'\|_2\to0\) along \(\omega\) for every \(y\). Given
\(y_1,\dots,y_k\) and \(\varepsilon>0\), the set of \(n\) with \(\|[u_n,y_j]\|_2<\varepsilon\) for all \(j\) belongs to
\(\omega\), hence is not empty. So \(M\) has property Γ. \(\square\)

**Example 6.6.** The hyperfinite factor \(R=\bigotimes_{n\ge1}(M_2(\mathbb C),\operatorname{tr})\) of type II₁ has
property Γ and is not full (Exercise 1). The group von Neumann algebra of the free group on two generators is full
(Theorem 9.4 below with \(P=\mathbb C\)).

## 7. Factors of type III₀ are never full

**Theorem 7.1.** Let \(M\) be a type III₀ factor whose predual is separable. Then \(M\) is not full. More precisely,
\(\sigma^\varphi_t\) lies in the closure of \(\operatorname{Int}M\) for every f.s.n. weight \(\varphi\) on \(M\) and
every \(t\in\mathbb R\), while \(\sigma^\varphi_t\notin\operatorname{Int}M\) for some \(t\).

*Reference:* [Connes 1974].

A first proof that \(M\) is not full is immediate from what we have: \(M_\omega\neq\mathbb C\) by Theorem 1.4, and
Corollary 5.2 applies. The stronger statement needs the structure (B7). We first extract from it what is used.

**Lemma 7.2.** Let \(M\) be a type III₀ factor whose predual is separable. There are a faithful normal state
\(\varphi_0\) of \(M\) and an increasing sequence \(N_1\subset N_2\subset\cdots\) of semifinite von Neumann
subalgebras of \(M\), with \(\sigma\)-weakly dense union, such that \(\sigma^{\varphi_0}_t(N_k)=N_k\) for all \(k\)
and \(t\).

*Proof.* Take \(N,E,(G_k)\) as in (B7) and put \(N_k=(N\cup G_k)''\). These increase, and their union contains the
generating set \(N\cup\bigcup G_k\), so it is \(\sigma\)-weakly dense.

*\(N_k\) is semifinite.* Let \(\tau\) be an f.s.n. trace on \(N\). For \(u\in G_k\), \(\operatorname{Ad}u\) restricts
to an automorphism of \(N\), so \(\tau\circ\operatorname{Ad}u\) is an f.s.n. trace on \(N\), and
\(\tau_k=\sum_{u\in G_k}\tau\circ\operatorname{Ad}u\) is an f.s.n. trace on \(N\) (B5) with
\(\tau_k\circ\operatorname{Ad}v=\tau_k\) for \(v\in G_k\). The weight \(\varphi_k=\tau_k\circ E\) is an f.s.n. weight
on \(M\) (B4d), and \(\sigma^{\varphi_k}_t\) acts on \(N\) as \(\sigma^{\tau_k}_t=\mathrm{id}\) (B4d). For \(v\in
G_k\), \(\varphi_k\circ\operatorname{Ad}v=\tau_k\circ E\circ\operatorname{Ad}v=\tau_k\circ\operatorname{Ad}v\circ E=
\varphi_k\), so \(v\in M_{\varphi_k}\) (B4b). Hence \(\sigma^{\varphi_k}\) fixes \(N_k\) pointwise, i.e.
\(N_k\subset M_{\varphi_k}\), and the restriction of \(\varphi_k\) to \(N_k\) is a faithful normal trace (B4b). It is
semifinite: \(\tau_k\) is semifinite on \(N\), so there are projections \(e_j\uparrow1\) in \(N\) with
\(\varphi_k(e_j)<\infty\), and \(\varphi_k(e_jx^*xe_j)\le\|x\|^2\varphi_k(e_j)\) for \(x\in N_k\), while
\(\bigcup_je_jN_ke_j\) is \(\sigma\)-weakly dense in \(N_k\). So \(N_k\) is semifinite.

*The state.* Fix a faithful normal state \(\rho\) of \(N\) and put \(\varphi_0=\rho\circ E\). By (B4a,d),
\(\sigma^{\varphi_0}_t=\operatorname{Ad}w_t\circ\sigma^{\varphi_k}_t\) with
\(w_t=(D\varphi_0:D\varphi_k)_t=(D\rho:D\tau_k)_t\in N\). Since \(\sigma^{\varphi_k}_t\) fixes \(N_k\) and
\(w_t\in N\subset N_k\), we get \(\sigma^{\varphi_0}_t(N_k)\subset N_k\) for all \(t\), hence equality. \(\square\)

*Proof of Theorem 7.1.* Take \(\varphi_0\) and \((N_k)\) as in Lemma 7.2 and fix \(t\). Write \(\rho_k\) for the
restriction of \(\varphi_0\) to \(N_k\), a faithful normal state. The restriction of \(\sigma^{\varphi_0}\) to \(N_k\)
is a \(\sigma\)-weakly continuous one-parameter automorphism group of \(N_k\) leaving \(\rho_k\) invariant, and
\(\rho_k\) satisfies the KMS condition for it (the KMS functions of \(\varphi_0\) for pairs of elements of \(N_k\)
serve). By (B4c), \(\sigma^{\varphi_0}_s|_{N_k}=\sigma^{\rho_k}_s\). As \(N_k\) is semifinite, (B4e) gives a positive
nonsingular \(h_k\) affiliated with \(N_k\) with \(\sigma^{\rho_k}_s=\operatorname{Ad}h_k^{is}\). Put
\(u_k=h_k^{it}\in\mathcal U(N_k)\). Then:

- \(u_kxu_k^*=\sigma^{\varphi_0}_t(x)\) for \(x\in N_k\), hence for \(x\in N_j\), \(j\le k\);
- \(\sigma^{\varphi_0}_s(u_k)=h_k^{is}h_k^{it}h_k^{-is}=u_k\), so \(u_k\in M_{\varphi_0}\) and
  \(\varphi_0\circ\operatorname{Ad}u_k=\varphi_0\) (B4b).

We show \(\operatorname{Ad}u_k\to\sigma^{\varphi_0}_t\) in the \(u\)-topology. Let \(\mathcal L\) be the set of
\(\chi\in M_*\) with \(\|\chi\circ\operatorname{Ad}u_k-\chi\circ\sigma^{\varphi_0}_t\|\to0\); it is a norm closed linear
subspace. For \(a,b\in N_j\) let \(\chi_{a,b}(y)=\varphi_0(bya)\). For \(k\ge j\), using the invariance of
\(\varphi_0\) under \(\operatorname{Ad}u_k^*\) and under \(\sigma^{\varphi_0}_{-t}\),
\[
\chi_{a,b}(u_kyu_k^*)=\varphi_0(u_k^*bu_k\,y\,u_k^*au_k)=\varphi_0\bigl(\sigma^{\varphi_0}_{-t}(b)\,y\,
\sigma^{\varphi_0}_{-t}(a)\bigr)=\chi_{a,b}(\sigma^{\varphi_0}_t(y)).
\]
So \(\chi_{a,b}\in\mathcal L\). The span of these functionals is norm dense in \(M_*\): if \(y\in M\) satisfies
\(\varphi_0(bya)=0\) for all \(a,b\in\bigcup_jN_j\), then by (B2) and continuity also for all \(a,b\in M\), and
\(b=1\), \(a=y^*\) give \(\varphi_0(yy^*)=0\), so \(y=0\); now apply the Hahn–Banach theorem in \(M_*\), whose dual is
\(M\). Hence \(\mathcal L=M_*\), and \(\sigma^{\varphi_0}_t\in\overline{\operatorname{Int}M}\).

For an arbitrary f.s.n. weight \(\varphi\), \(\sigma^\varphi_t=\operatorname{Ad}(D\varphi:D\varphi_0)_t\circ
\sigma^{\varphi_0}_t\) (B4a). The closure of the subgroup \(\operatorname{Int}M\) is a subgroup, so
\(\sigma^\varphi_t\in\overline{\operatorname{Int}M}\). Finally, \(M\) is not semifinite, so by (B4e) some
\(\sigma^\varphi_t\) is not inner. Thus \(\operatorname{Int}M\) is not closed. \(\square\)

## 8. A spectral gap for the free group

Let \(\mathbb F_2\) be the free group on two generators \(a,b\). Every element has a unique reduced word in
\(a^{\pm1},b^{\pm1}\). Let \(W_a\) (respectively \(W_b\)) be the set of nontrivial elements whose reduced word begins,
on the left, with \(a^{\pm1}\) (respectively \(b^{\pm1}\)). For an element whose reduced word begins with \(a^k\)
followed by a letter \(b^{\pm1}\), or equals \(a^k\), we call \(a^k\) its *leading \(a\)-block*.

Let \(\mathbb F_2\) act on a set \(X\), and let \(\pi(g)f(x)=f(g^{-1}\cdot x)\) be the associated unitary
representation on \(\ell^2(X)\).

**Lemma 8.1.** Suppose \(X=X_1\sqcup X_2\) with
\[
b\cdot X_1\subset X_2,\qquad a\cdot X_2\subset X_1,\qquad a^2\cdot X_2\subset X_1,\qquad
(a\cdot X_2)\cap(a^2\cdot X_2)=\emptyset .
\]
Then for every \(f\in\ell^2(X)\),
\[
\|f\|\le14\,\max\bigl(\|\pi(a)f-f\|,\|\pi(b)f-f\|\bigr),\qquad\text{hence}\qquad
\|f\|^2\le196\bigl(\|\pi(a)f-f\|^2+\|\pi(b)f-f\|^2\bigr). \tag{8.1}
\]

*Proof.* Let \(\varepsilon=\max(\|\pi(a)f-f\|,\|\pi(b)f-f\|)\), \(x=\|1_{X_1}f\|\), \(y=\|1_{X_2}f\|\). For
\(g\in\mathbb F_2\) and \(S\subset X\),
\[
\|1_{g\cdot S}f\|^2=\sum_{s\in S}|f(g\cdot s)|^2=\|1_S\,\pi(g^{-1})f\|^2,\qquad
\|1_S\pi(g^{-1})f\|\ge\|1_Sf\|-\|\pi(g^{-1})f-f\|,
\]
and \(\|\pi(g^{-1})f-f\|=\|f-\pi(g)f\|\). Also \(\|\pi(a^2)f-f\|\le\|\pi(a)(\pi(a)f-f)\|+\|\pi(a)f-f\|\le2\varepsilon\).
From \(b\cdot X_1\subset X_2\): \(y\ge x-\varepsilon\). From the disjoint sets \(a\cdot X_2,a^2\cdot X_2\subset X_1\):
\(x^2\ge(y-\varepsilon)_+^2+(y-2\varepsilon)_+^2\ge2(y-2\varepsilon)_+^2\). If \(y\ge2\varepsilon\), then
\(\sqrt2(y-2\varepsilon)\le x\le y+\varepsilon\), so
\[
y\le\frac{2\sqrt2+1}{\sqrt2-1}\,\varepsilon=(5+3\sqrt2)\,\varepsilon,\qquad x\le(6+3\sqrt2)\,\varepsilon,
\]
and \(\|f\|^2=x^2+y^2\le\bigl((5+3\sqrt2)^2+(6+3\sqrt2)^2\bigr)\varepsilon^2=(97+66\sqrt2)\varepsilon^2<191\,
\varepsilon^2\). If \(y<2\varepsilon\), then \(x<3\varepsilon\) and \(\|f\|^2<13\varepsilon^2\). In both cases
\(\|f\|\le14\varepsilon\). \(\square\)

**Lemma 8.2 (conjugation).** Let \(\mathbb F_2\) act on \(\Omega=\mathbb F_2\setminus\{1\}\) by conjugation,
\(g\cdot s=gsg^{-1}\). Then \(X_1=W_a\), \(X_2=W_b\) satisfy the hypotheses of Lemma 8.1.

*Proof.* \(\Omega=W_a\sqcup W_b\). Let \(s\in W_a\). The word \(bs\) is reduced and begins with \(b\). Multiplying by
\(b^{-1}\) on the right cancels at most a final \(b\) of \(s\), and never reaches the initial \(a^{\pm1}\) of \(s\);
so \(bsb^{-1}\) is nontrivial and begins with \(b\). Thus \(b\cdot W_a\subset W_b\). Now let \(s\in W_b\) and
\(k\in\{1,2\}\). Write \(s=s'a^m\) with \(m\in\mathbb Z\) and \(s'\) ending with \(b^{\pm1}\) (possible because
\(s\) begins with \(b^{\pm1}\)). Then \(a^ksa^{-k}=a^ks'a^{m-k}\), and this word is reduced. So \(a^k\cdot s\) lies in
\(W_a\) and its leading \(a\)-block is exactly \(a^k\). Elements of \(a\cdot W_b\) and \(a^2\cdot W_b\) have different
leading \(a\)-blocks, so the two sets are disjoint. \(\square\)

**Lemma 8.3 (free actions).** If \(\mathbb F_2\) acts freely on \(X\), there is a partition of \(X\) satisfying
the hypotheses of Lemma 8.1.

*Proof.* Choose a point \(x_O\) in each orbit \(O\). By freeness, \(g\mapsto g\cdot x_O\) is a bijection of
\(\mathbb F_2\) onto \(O\). Let \(X_1=\{g\cdot x_O:g\in W_a,\ O\text{ an orbit}\}\) and \(X_2=X\setminus X_1\), which
corresponds to \(\{1\}\cup W_b\) in each orbit. Left multiplication by \(b\) maps \(W_a\) into \(W_b\) (no cancellation
occurs), so \(b\cdot X_1\subset X_2\). For \(k\in\{1,2\}\) and \(g\in\{1\}\cup W_b\), the word \(a^kg\) is reduced, lies
in \(W_a\) and has leading \(a\)-block \(a^k\). So \(a\cdot X_2\) and \(a^2\cdot X_2\) are disjoint subsets of \(X_1\).
\(\square\)

**Example 8.4.** The analogue of Lemma 8.1 fails for \(\mathbb Z\) acting on itself by translation: the unit vectors
\(f_n=n^{-1/2}1_{\{1,\dots,n\}}\) satisfy \(\|\pi(1)f_n-f_n\|=(2/n)^{1/2}\to0\). The inequality (8.1) expresses the
non-amenability of \(\mathbb F_2\), and it is the only place where the free group matters below.

## 9. Bernoulli crossed products over the free group

A reference for this section is [Connes 1974].

**Construction 9.1.** Consider a von Neumann algebra \(P\) on a separable Hilbert space \(H\), and a unit vector
\(\xi_0\in H\) that is cyclic and separating for \(P\). Put \(\varphi_P=\omega_{\xi_0}|_P\) and let \(\Delta_P\) be its
modular operator. Write \(G=\mathbb F_2\).

*The infinite tensor product.* Fix an orthonormal basis \(\mathcal B\) of \(H\) containing \(\xi_0\). Let
\(\mathcal X\) be the countable set of maps \(g:G\to\mathcal B\) with \(g(s)=\xi_0\) for all but finitely many \(s\),
and let \(\mathcal K\) be the Hilbert space with orthonormal basis \((\xi_g)_{g\in\mathcal X}\). Put
\(\eta_0=\xi_{g_0}\), where \(g_0\equiv\xi_0\). For a finite set \(F\subset G\), the map
\(\bigotimes_{s\in F}g(s)\mapsto\xi_g\) (for \(g\) equal to \(\xi_0\) off \(F\)) extends to an isometry
\(j_F:\bigotimes_{s\in F}H\to\mathcal K\); these isometries are compatible under the embeddings
\(h\mapsto h\otimes\xi_0\otimes\cdots\otimes\xi_0\) and their ranges have dense union. For \(t\in G\), the map
\(\xi_g\mapsto g(t)\otimes\xi_{g|_{G\setminus\{t\}}}\) identifies \(\mathcal K\) with \(H\otimes\mathcal K^{(t)}\), where
\(\mathcal K^{(t)}\) is built in the same way from \(G\setminus\{t\}\); let \(\pi_t(x)\) be the operator corresponding
to \(x\otimes1\), for \(x\in P\). Operators \(\pi_s(x)\) and \(\pi_t(y)\) commute for \(s\neq t\), and also \(\pi_t(x)\)
commutes with \(\pi_t(x')\) for \(x'\in P'\). Let
\[
N=\{\pi_t(x):t\in G,\ x\in P\}''.
\]
The vector \(\eta_0\) is cyclic for \(N\): the span of \(\pi_{t_1}(x_1)\cdots\pi_{t_m}(x_m)\eta_0=
j_F(x_1\xi_0\otimes\cdots\otimes x_m\xi_0)\), \(F=\{t_1,\dots,t_m\}\) distinct, is dense in the range of \(j_F\),
because \(P\xi_0\) is dense in \(H\). The same argument with \(P'\), whose images \(\pi_t(P')\) lie in \(N'\), shows that
\(\eta_0\) is cyclic for \(N'\), i.e. separating for \(N\). So \(\varphi_N=\omega_{\eta_0}|_N\) is a faithful normal
state.

*The shift.* For \(s\in G\) let \((s\cdot g)(t)=g(s^{-1}t)\) and \(V_s\xi_g=\xi_{s\cdot g}\). Then \(V\) is a unitary
representation of \(G\) on \(\mathcal K\), \(V_s\eta_0=\eta_0\), and \(V_s\pi_t(x)V_s^*=\pi_{st}(x)\) (check on basis
vectors). So \(\theta_s=\operatorname{Ad}V_s|_N\) is an action of \(G\) on \(N\) with \(\varphi_N\circ\theta_s=
\varphi_N\).

*The crossed product.* On \(\mathcal K\otimes\ell^2(G)\) let \(\lambda\) and \(r\) be the left and right regular
representations, \(\lambda_s\delta_t=\delta_{st}\), \(r_s\delta_t=\delta_{ts^{-1}}\). Put
\[
I(x)=x\otimes1\ (x\in N),\qquad U_s=V_s\otimes\lambda_s\ (s\in G),\qquad M=\{I(N),U_s:s\in G\}'' ,
\]
\(\zeta_0=\eta_0\otimes\delta_1\) and \(\psi=\omega_{\zeta_0}|_M\). Then \(U_sI(x)U_s^*=I(\theta_s(x))\); \(M\) is a
model of the crossed product of \(N\) by \(\theta\), but we shall not need this. The span \(\mathcal A\) of
\(\{I(x)U_s\}\) is a \(\ast\)-algebra with \(\sigma\)-weak closure \(M\), and \(I(x)U_s\zeta_0=x\eta_0\otimes\delta_s\).

**Proposition 9.2.** In Construction 9.1:

- (a) \(\zeta_0\) is cyclic and separating for \(M\), so \(\psi\) is a faithful normal state; and
  \(\psi\circ\operatorname{Ad}U_s=\psi\), so \(U_s\in M_\psi\) for all \(s\).
- (b) For every \(T\in M\),
  \[
  \|T-\psi(T)\|_\psi\le20\max\bigl(\|[T,U_a]\|_\psi,\|[T,U_b]\|_\psi\bigr).\tag{9.1}
  \]
- (c) Under \(\mathcal K\otimes\ell^2(G)\), the modular operator of \(\psi\) is \(\Delta_\psi=\Delta_{\varphi_N}\otimes1\).
  Moreover \(\Delta_{\varphi_N}^{it}\) is the infinite tensor product of copies of \(\Delta_P^{it}\): it is the unitary
  \(W_t\) with \(W_tj_F(h_1\otimes\cdots\otimes h_m)=j_F(\Delta_P^{it}h_1\otimes\cdots\otimes\Delta_P^{it}h_m)\).

*Proof.* (a) Cyclicity: \(\mathcal A\zeta_0\) contains all \(x\eta_0\otimes\delta_s\), whose span is dense. For the
commutant: each \(1\otimes r_t\) commutes with \(I(x)\) and with \(U_s\), so lies in \(M'\). For \(y\in N'\) let
\(Y=\sum_{g\in G}V_gyV_g^*\otimes e_{g,g}\), where \(e_{g,g}\) is the projection onto \(\mathbb C\delta_g\). Since
\(V_g\) normalizes \(N\), \(V_gyV_g^*\in N'\), so \(Y\) commutes with \(I(N)\); and
\(U_sYU_s^*=\sum_gV_{sg}yV_{sg}^*\otimes e_{sg,sg}=Y\). So \(Y\in M'\), and \((1\otimes r_t)Y\zeta_0=y\eta_0\otimes
\delta_{t^{-1}}\). These span a dense subspace since \(N'\eta_0\) is dense. So \(\zeta_0\) is cyclic for \(M'\), i.e.
separating for \(M\). Next, \(U_s^*\zeta_0=V_s^*\eta_0\otimes\delta_{s^{-1}}=(1\otimes r_s)\zeta_0\), and
\(1\otimes r_s\) is a unitary in \(M'\), so \(\psi(U_sTU_s^*)=\langle T(1\otimes r_s)\zeta_0,(1\otimes r_s)\zeta_0
\rangle=\psi(T)\). By (B4b), \(U_s\in M_\psi\).

(b) Write \(T\zeta_0=\sum_{s\in G}\zeta_s\otimes\delta_s\) with \(\zeta_s\in\mathcal K\); then
\(\|T\|_\psi^2=\sum_s\|\zeta_s\|^2\) and \(\psi(T)=\langle\zeta_1,\eta_0\rangle\). Let \(c\in\{a,b\}\). Since
\(U_c\zeta_0=\eta_0\otimes\delta_c=(1\otimes r_{c^{-1}})\zeta_0\) and \(1\otimes r_{c^{-1}}\in M'\),
\[
U_c^*TU_c\zeta_0=U_c^*(1\otimes r_{c^{-1}})T\zeta_0=\sum_sV_c^*\zeta_s\otimes\delta_{c^{-1}sc}.
\]
So the \(\delta_t\)-component of \(U_c^*TU_c\zeta_0\) is \(V_c^*\zeta_{ctc^{-1}}\). Moreover
\(\|[T,U_c]\|_\psi=\|U_c(U_c^*TU_c-T)\|_\psi=\|U_c^*TU_c-T\|_\psi\). Hence
\[
\sum_{t\in G}\|V_c^*\zeta_{ctc^{-1}}-\zeta_t\|^2=\|[T,U_c]\|_\psi^2. \tag{9.2}
\]
*The components \(t\neq1\).* Let \(f(t)=\|\zeta_t\|\) for \(t\in\Omega=G\setminus\{1\}\). With the conjugation action of
Lemma 8.2, \((\pi(c^{-1})f)(t)=f(ctc^{-1})\) and \(|f(ctc^{-1})-f(t)|\le\|V_c^*\zeta_{ctc^{-1}}-\zeta_t\|\). By (9.2),
\(\|\pi(c)f-f\|=\|\pi(c^{-1})f-f\|\le\|[T,U_c]\|_\psi\). Lemmas 8.1 and 8.2 give
\[
\sum_{t\neq1}\|\zeta_t\|^2\le196\,\varepsilon^2,\qquad \varepsilon=\max\bigl(\|[T,U_a]\|_\psi,\|[T,U_b]\|_\psi\bigr).
\]
*The component \(t=1\).* By (9.2), \(\|V_c^*\zeta_1-\zeta_1\|\le\|[T,U_c]\|_\psi\). The representation \(V\) permutes
the basis \((\xi_g)\), fixes \(\eta_0\), and acts freely on \(\mathcal X\setminus\{g_0\}\): if \(g\neq g_0\) and
\(s\cdot g=g\), then \(s\) permutes the finite nonempty set \(\{t:g(t)\neq\xi_0\}\), so some power \(s^k\), \(k\ge1\),
fixes a point of \(G\) under left multiplication, whence \(s^k=1\) and \(s=1\), as \(G\) is torsion free. Apply Lemmas
8.1 and 8.3 to \(X=\mathcal X\setminus\{g_0\}\) and \(f'(g)=\langle\zeta_1,\xi_g\rangle\): since
\(\langle V_c\zeta_1,\xi_g\rangle=f'(c^{-1}\cdot g)\), we have \(\|\pi(c)f'-f'\|\le\|V_c\zeta_1-\zeta_1\|\), and so
\[
\|\zeta_1-\psi(T)\eta_0\|^2=\sum_{g\neq g_0}|\langle\zeta_1,\xi_g\rangle|^2\le196\,\varepsilon^2 .
\]
Adding, \(\|T-\psi(T)\|_\psi^2=\|T\zeta_0-\psi(T)\zeta_0\|^2=\sum_{t\ne1}\|\zeta_t\|^2+\|\zeta_1-\psi(T)\eta_0\|^2\le392
\,\varepsilon^2\), and \(\sqrt{392}<20\). Since a maximum is at most the sum, (9.1) also gives
\(\|T-\psi(T)\|_\psi\le20\bigl(\|[T,U_a]\|_\psi+\|[T,U_b]\|_\psi\bigr)\).

(c) Let \(S_\psi\) be the closure of \(T\zeta_0\mapsto T^*\zeta_0\) (\(T\in M\)) and \(S_N\) that of
\(x\eta_0\mapsto x^*\eta_0\) (\(x\in N\)). For \(T=I(x)U_s\),
\(T^*=U_s^*I(x^*)=I(\theta_{s^{-1}}(x^*))U_{s^{-1}}\), so
\[
T^*\zeta_0=V_s^*x^*V_s\eta_0\otimes\delta_{s^{-1}}=V_s^*S_N(x\eta_0)\otimes\delta_{s^{-1}} .
\]
Let \(B\) be the closed conjugate-linear operator on \(\bigoplus_s\mathcal K\otimes\delta_s\) acting on the \(s\)-th
summand as \(V_s^*S_N\), and \(R\) the unitary \(1\otimes(\delta_s\mapsto\delta_{s^{-1}})\). Then \(S_\psi\) and \(RB\)
agree on \(\mathcal A\zeta_0\). This is a core for \(S_\psi\): by (B2), for \(T\in M\) there is a bounded net
\(T_i\in\mathcal A\) with \(T_i\to T\) strong\*, so \((T_i\zeta_0,T_i^*\zeta_0)\to(T\zeta_0,T^*\zeta_0)\). It is also a
core for \(RB\), because \(N\eta_0\) is a core for \(S_N\) and algebraic direct sums of cores are cores for direct
sums. Hence \(S_\psi=RB\), and
\[
\Delta_\psi=S_\psi^*S_\psi=B^*R^*RB=B^*B=\bigoplus_s(V_s^*S_N)^*(V_s^*S_N)=\bigoplus_sS_N^*V_sV_s^*S_N=
\bigoplus_s\Delta_{\varphi_N}.
\]
For the second statement, \(W_t\) is well defined and unitary because \(\Delta_P^{it}\xi_0=\xi_0\), and \(W_t\eta_0=
\eta_0\). For a finite set \(F\), the identification \(\mathcal K\cong\bigl(\bigotimes_{s\in F}H\bigr)\otimes
\mathcal K^{(F)}\) (with \(\mathcal K^{(F)}\) built from \(G\setminus F\)) carries \(N\) onto the tensor product of
\(\bigotimes_{s\in F}P\) and the analogous algebra \(N^{(F)}\), and \(\varphi_N\) onto
\(\bigl(\bigotimes_{s\in F}\varphi_P\bigr)\otimes\varphi_{N^{(F)}}\). By (B4f),
\(\sigma^{\varphi_N}_t(\pi_s(x))=\pi_s(\sigma^{\varphi_P}_t(x))=W_t\pi_s(x)W_t^*\) for \(s\in F\), \(x\in P\). Hence
\(\sigma^{\varphi_N}_t=\operatorname{Ad}W_t\) on \(N\), and
\(\Delta_{\varphi_N}^{it}y\eta_0=\sigma^{\varphi_N}_t(y)\eta_0=W_tyW_t^*\eta_0=W_ty\eta_0\) for \(y\in N\), so
\(\Delta_{\varphi_N}^{it}=W_t\). \(\square\)

**Remark 9.3.** One is tempted to expand \(T\in M\) as a series \(\sum_sI(x_s)U_s\) converging strongly. This is not
possible in general: already for \(P=\mathbb C\) (so \(M\) is the group von Neumann algebra of \(G\)), the subalgebra
generated by \(U_a\) is isomorphic to \(L^\infty\) of the circle, and the partial Fourier sums of a bounded function
need not be uniformly bounded, while a strongly convergent sequence of operators is bounded. The proof of (b) uses
only the expansion of the vector \(T\zeta_0\), which always converges.

**Theorem 9.4.** In Construction 9.1, \(M\) and \(M_\psi\) are factors, and \(M\) is full. If \(\varphi_P\) is a
trace, \(M\) is of type II₁. Otherwise \(M\) is of type III and \(S(M)=\operatorname{Sp}\Delta_{\varphi_N}\).

*Proof.* If \(z\) commutes with \(U_a\) and \(U_b\), then (9.1) gives \(\|z-\psi(z)\|_\psi=0\), so
\(z=\psi(z)1\) since \(\psi\) is faithful. This applies to the centre of \(M\), and to the centre of \(M_\psi\),
because \(M_\psi\) contains \(U_a,U_b\) by Proposition 9.2(a). So both are factors.

Fullness. Let \((x_n)\) be a centralizing sequence in \(M\). By Proposition 1.2(a), \([x_n,U_c]\to0\) strongly, so
\(\|[x_n,U_c]\|_\psi\to0\) for \(c=a,b\), and (9.1) gives \(\|x_n-\psi(x_n)\|_\psi\to0\). The sequence \((x_n^*)\) is
centralizing too, so \(\|x_n^*-\overline{\psi(x_n)}\|_\psi\to0\). Hence \(\|x_n-\psi(x_n)\|^\#_\psi\to0\) and, by
(B1), \(x_n-\psi(x_n)\to0\) strong\*. By Corollary 5.2, \(M\) is full.

Type. If \(\varphi_P\) is a trace, then \(\Delta_P=1\), so \(W_t=1\) and \(\Delta_\psi=1\) by Proposition 9.2(c);
thus \(\psi\) is a faithful normal tracial state, \(M\) is a finite factor, and it is infinite dimensional because the
vectors \(U_s\zeta_0=\eta_0\otimes\delta_s\) are orthonormal. So \(M\) is of type II₁. If \(\varphi_P\) is not a trace,
then \(\Delta_P\neq1\); since \(W_t\) acts on the range of \(j_{\{s\}}\) as \(\Delta_P^{it}\), \(\Delta_{\varphi_N}\neq1\).
By (B6), Proposition 9.2(c) and the factoriality of \(M_\psi\),
\(S(M)=\operatorname{Sp}\Delta_\psi=\operatorname{Sp}\Delta_{\varphi_N}\neq\{1\}\), so \(M\) is not semifinite: it is
of type III. \(\square\)

## 10. Full factors of types I, II₁, II∞ and III\(_\lambda\), \(\lambda\neq0\)

**Proposition 10.1.** Let \(M\) be a full factor whose predual is separable, and \(K\) a nonzero separable Hilbert space. Then
\(Q=M\bar\otimes B(K)\) is a full factor.

*Proof.* \(Q\) is a factor. Let \((e_{ij})\) be matrix units of \(B(K)\) for an orthonormal basis \((\delta_j)\),
\(f_j=1\otimes e_{jj}\) and \(v_j=1\otimes e_{j1}\). Identify \(M\) with \(f_1Qf_1\) by \(m\mapsto m\otimes e_{11}\).
Fix a faithful normal state \(\varphi\) of \(M\) and put \(\psi=\varphi\otimes\operatorname{Tr}(h\,\cdot)\) with
\(h=\sum_j\mu_je_{jj}\), \(\mu_j>0\), \(\sum\mu_j=1\); \(\psi\) is a faithful normal state of \(Q\).

Now let \((x_n)\) be centralizing in \(Q\). By Proposition 1.2(a), \([x_n,y]\to0\) strong\* for every \(y\in Q\). Let
\(y_n=f_1x_nf_1\in M\). For \(\chi\in M_*\) put \(\tilde\chi=\chi\otimes\omega_{\delta_1}\in Q_*\); then
\(\tilde\chi(z)=\tilde\chi(f_1zf_1)\), and for \(m\in M\), \(\chi(my_n)=\tilde\chi(mx_n)\) and
\(\chi(y_nm)=\tilde\chi(x_nm)\). So \(\|[y_n,\chi]\|\le\|[x_n,\tilde\chi]\|\to0\): \((y_n)\) is centralizing in \(M\).
By Lemma 5.1, with \(\lambda_n=\varphi(y_n)\), \(y_n-\lambda_n\to0\) strong\* in \(M\), hence
\(f_1(x_n-\lambda_n)f_1\to0\) strong\* in \(Q\). Also \((1-f_1)x_nf_1=(1-f_1)[x_n,f_1]\to0\) strongly. So
\((x_n-\lambda_n)f_1\to0\) strongly. For each \(j\),
\[
(x_n-\lambda_n)f_j=(x_n-\lambda_n)v_jf_1v_j^*=[x_n,v_j]f_1v_j^*+v_j(x_n-\lambda_n)f_1v_j^*\to0\quad\text{strongly}.
\]
Let \(q_J=\sum_{j\le J}f_j\). Since \(\|zq\|_\psi^2=\psi(qz^*zq)\le\|z\|^2\psi(q)\) for a projection \(q\),
\[
\|x_n-\lambda_n\|_\psi\le\sum_{j\le J}\|(x_n-\lambda_n)f_j\|_\psi+2\sup_n\|x_n\|\,\psi(1-q_J)^{1/2},
\]
and \(\psi(1-q_J)\to0\) as \(J\to\infty\). Hence \(\|x_n-\lambda_n\|_\psi\to0\). The same argument for the centralizing
sequence \((x_n^*)\), whose corner is \(y_n^*\) with \(\varphi(y_n^*)=\overline{\lambda_n}\), gives
\(\|x_n^*-\overline{\lambda_n}\|_\psi\to0\). So \(x_n-\lambda_n\to0\) strong\* (B1), and \(Q\) is full by Corollary 5.2.
\(\square\)

**Theorem 10.2.** There are full factors with separable predual of type I\(_n\) (\(n\le\infty\)), II₁, II∞, and
III\(_\lambda\) for every \(\lambda\in\,]0,1]\).

*Proof.* *Type I.* \(\mathbb C\) is full, so \(B(K)=\mathbb C\bar\otimes B(K)\) is full by Proposition 10.1.

*Type II₁.* Take \(P=\mathbb C\), \(H=\mathbb C\), \(\xi_0=1\) in Construction 9.1. Then \(\mathcal K=\mathbb C\),
\(N=\mathbb C\), and \(M\) is the von Neumann algebra generated by the left regular representation of \(\mathbb F_2\).
By Theorem 9.4 it is a full factor of type II₁.

*Type II∞.* \(M\bar\otimes B(\ell^2)\) with \(M\) as in the previous case, by Proposition 10.1.

*Type III.* Suppose \(\Delta_P\) has an orthonormal basis of eigenvectors, for instance \(P\) finite dimensional. In
Construction 9.1 choose \(\mathcal B\) to consist of eigenvectors and to contain \(\xi_0\) (possible because \(\Delta_P\xi_0=\xi_0\)), and let
\(\Lambda\) be the set of eigenvalues of \(\Delta_P\). By Proposition 9.2(c), \(W_t\xi_g=\prod_s\lambda_{g(s)}^{it}\,
\xi_g\), where \(\lambda_{g(s)}\) is the eigenvalue of \(g(s)\), so by Stone's theorem \(\Delta_{\varphi_N}\) is
diagonal in the basis \((\xi_g)\) with eigenvalues \(\prod_s\lambda_{g(s)}\). These are exactly the finite products of
elements of \(\Lambda\) (use distinct tensor slots for the factors). Since \(J_P\Delta_PJ_P=\Delta_P^{-1}\), \(\Lambda\)
is closed under inversion, and \(1\in\Lambda\); so the finite products form the subgroup \(\langle\Lambda\rangle\) of
\(\mathbb R_+^*\) generated by \(\Lambda\), and
\[
S(M)=\operatorname{Sp}\Delta_{\varphi_N}=\overline{\langle\Lambda\rangle}\quad(\text{closure in }[0,\infty[).
\]
Now take \(P=M_k(\mathbb C)\) acting on \(H=M_k(\mathbb C)\) (Hilbert–Schmidt inner product) by left multiplication,
with \(\xi_0=\rho^{1/2}\) for a diagonal density matrix \(\rho=\operatorname{diag}(\mu_1,\dots,\mu_k)\), all
\(\mu_i>0\). Then \(\xi_0\) is cyclic and separating, \(S_P(x\rho^{1/2})=x^*\rho^{1/2}\), and
\(\Delta_P(h)=\rho h\rho^{-1}\), \(J_P(h)=h^*\): indeed \(h\mapsto\rho^{1/2}h\rho^{-1/2}\) is positive (a product of
commuting positive operators of left and right multiplication), \(h\mapsto h^*\) is an antiunitary involution, and
\((\rho^{1/2}x\rho^{1/2}\rho^{-1/2})^*=x^*\rho^{1/2}\), so uniqueness of the polar decomposition applies. The matrix
units \(e_{ij}\) are eigenvectors with eigenvalues \(\mu_i/\mu_j\), and \(\xi_0\) lies in the eigenspace of \(1\).
So \(\Lambda=\{\mu_i/\mu_j\}\).

- For \(0<\lambda<1\), take \(k=2\), \(\rho=\operatorname{diag}\bigl(\tfrac1{1+\lambda},\tfrac\lambda{1+\lambda}\bigr)\).
  Then \(\Lambda=\{1,\lambda,\lambda^{-1}\}\), \(\langle\Lambda\rangle=\lambda^{\mathbb Z}\), and
  \(S(M)=\lambda^{\mathbb Z}\cup\{0\}\): \(M\) is a full factor of type III\(_\lambda\).
- For \(\lambda=1\), take \(k=3\) and \(\rho\) proportional to \(\operatorname{diag}(1,\lambda_1,\lambda_2)\) with
  \(\lambda_1,\lambda_2\in\,]0,1[\) and \(\log\lambda_1/\log\lambda_2\notin\mathbb Q\). Then
  \(\langle\Lambda\rangle\supset\lambda_1^{\mathbb Z}\lambda_2^{\mathbb Z}\), which is dense in \(\mathbb R_+^*\), so
  \(S(M)=[0,\infty[\): \(M\) is a full factor of type III₁.

In both cases Theorem 9.4 gives factoriality and fullness, and (B6) the type. \(\square\)

Combined with Theorem 7.1, this shows that type III₀ is the only type (among I, II₁, II∞ and III\(_\lambda\),
\(0\le\lambda\le1\)) with no full factor.

## 11. Exercises

**Exercise 1.** Let \(R=\bigotimes_{n\ge1}(M_2(\mathbb C),\operatorname{tr})\), with \(\operatorname{tr}\) the normalized
trace. Let \(u_n=1\otimes\cdots\otimes1\otimes\sigma\otimes1\otimes\cdots\), with \(\sigma=\operatorname{diag}(1,-1)\)
in the \(n\)-th slot. Show that \((u_n)\) is a nontrivial centralizing sequence, so that \(R\) has property Γ and is
not full.

*Solution.* \(u_n\) is a unitary with \(\tau(u_n)=\operatorname{tr}(\sigma)=0\). If \(y\) lies in the algebra
\(R_m\) generated by the first \(m\) slots, then \([u_n,y]=0\) for \(n>m\). For general \(y\) and \(\delta>0\) pick
\(y'\in\bigcup_mR_m\) with \(\|y-y'\|_2<\delta\) (the union is \(\sigma\)-weakly dense, so (B2) applies); then
\(\|[u_n,y]\|_2\le2\|y-y'\|_2<2\delta\) for large \(n\). By Lemma 6.2, \((u_n)\) is centralizing. It is not trivial: if
\(u_n-\lambda_n\to0\) strongly, then \(\lambda_n=\tau(\lambda_n-u_n)\to0\) and \(\|u_n\|_2\to0\), but
\(\|u_n\|_2=1\). By Corollary 5.2, \(R\) is not full, and by Theorem 6.5 it has property Γ (which is also visible
directly from the \(u_n\)).

**Exercise 2.** Let \(M=M_1\oplus M_2\) with separable preduals. Show that \(M\) is full if and only if \(M_1\) and
\(M_2\) are full.

*Solution.* Use Theorem 4.2(e). Let \(p_k\) be the central projections with \(p_kM=M_k\). We have \(M_*=(M_1)_*\oplus
(M_2)_*\), and for \(x=x^{(1)}\oplus x^{(2)}\) and \(\varphi=\varphi_1\oplus\varphi_2\),
\(\|[x,\varphi]\|=\|[x^{(1)},\varphi_1]\|+\|[x^{(2)},\varphi_2]\|\). So a bounded sequence in \(M\) is centralizing if
and only if both components are. The centre is \(C_1\oplus C_2\), and \(x_n-z_n\to0\) strong\* if and only if this
holds in both components (a normal positive functional on \(M\) is a sum of such on \(M_1\) and \(M_2\)). Hence (e)
holds for \(M\) if and only if it holds for \(M_1\) and for \(M_2\).

**Exercise 3.** Let \(M\) be a full factor whose predual is separable, \(\varphi\) a faithful normal state, and \((x_n)\)
a bounded sequence. Show that \((x_n)\) is centralizing if and only if \(\|x_n-\varphi(x_n)\|^\#_\varphi\to0\).

*Solution.* If \((x_n)\) is centralizing, Lemma 5.1 gives \(x_n-\varphi(x_n)\to0\) strong\*, in particular in
\(\|\cdot\|^\#_\varphi\). Conversely, if \(\|x_n-\varphi(x_n)\|^\#_\varphi\to0\), then \(y_n=x_n-\varphi(x_n)\) is
bounded and tends to \(0\) strong\* (B1). For \(\psi\in M_*^+\), Lemma 2.4(d) gives
\(\|[x_n,\psi]\|=\|[y_n,\psi]\|\le\sqrt2\psi(1)^{1/2}\|y_n\|^\#_\psi\to0\), and every element of \(M_*\) is a
combination of four positive ones. The converse does not use fullness.

**Exercise 4.** Show that the tensor product \(M\bar\otimes R\) of any factor \(M\) with separable predual and the
hyperfinite II₁ factor \(R\) is not full.

*Solution.* Let \(u_n\in R\) be as in Exercise 1 and \(x_n=1\otimes u_n\). For \(\varphi\in M_*\), \(\chi\in R_*\),
\([x_n,\varphi\otimes\chi]=\varphi\otimes[u_n,\chi]\) has norm at most \(\|\varphi\|\|[u_n,\chi]\|\to0\). Elementary tensors
\(\varphi\otimes\chi\) have dense span in the predual of \(M\bar\otimes R\), so \((x_n)\) is centralizing by
Proposition 1.2(a). With the faithful normal state \(\varphi_0\otimes\tau\), we have \((\varphi_0\otimes\tau)(x_n)=0\)
while \(\|x_n\|_{\varphi_0\otimes\tau}=1\); by Exercise 3 (or Lemma 5.1), the tensor product is not full.

**Exercise 5.** In Construction 9.1 with \(P=\mathbb C\), show directly from (9.1) that every unitary \(u\) of \(M\)
with \(\tau(u)=0\) satisfies \(\max(\|[u,U_a]\|_2,\|[u,U_b]\|_2)\ge1/20\). Deduce again that the group von Neumann
algebra of \(\mathbb F_2\) does not have property Γ.

*Solution.* Here \(\psi=\tau\) and \(\|\cdot\|_\psi=\|\cdot\|_2\). By (9.1), \(1=\|u\|_2=\|u-\tau(u)\|_2\le20\max_c\|
[u,U_c]\|_2\). Property Γ would require, for \(\varepsilon=1/20\) and \(y_1=U_a\), \(y_2=U_b\), a unitary with trace
\(0\) and both commutators of \(2\)-norm below \(1/20\).

## References



- [Connes 1974] A. Connes, Almost periodic states and factors of type III₁, J. Functional Analysis 16 (1974),
  415–445. Free at https://doi.org/10.1016/0022-1236(74)90059-7
- [Connes 1973] A. Connes, Une classification des facteurs de type III, Ann. Sci. École Norm. Sup. (4) 6 (1973), no. 2,
  133–252. https://doi.org/10.24033/asens.1247 (open access: http://www.numdam.org/item?id=ASENS_1973_4_6_2_133_0). Free at https://alainconnes.org/wp-content/uploads/classificationfacteurs.pdf
