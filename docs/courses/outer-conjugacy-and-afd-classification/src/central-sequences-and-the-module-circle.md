# Central sequences and the module circle

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Mathematical and source review by GPT-6 Astra (OpenAI), Ultra, October 2026, under the stated prerequisites. New original text is public domain (CC0).*

## Introduction

A discrete decomposition writes a type III factor as a semifinite algebra together with one crossing unitary. Two questions then become concrete. Which central sequences come from the semifinite algebra? When does an inner approximation on that algebra extend to the whole factor?

Both answers involve invariance under the crossing automorphism. A modular spectral gap pushes central sequences into the coefficient algebra. Fourier coefficients prove the converse and also transfer approximately inner automorphisms. For the hyperfinite type \(III_\lambda\) factor, this transfer identifies the kernel of the module. A scalar modular derivative gives a continuous coordinate on its quotient circle.

Read [Central towers and unitary cocycles](central-towers-and-unitary-cocycles.md), [Almost invariant inner implementers](almost-invariant-inner-implementers.md), [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md) and Permutation symmetry and Powers factors. We also use *Ultraproducts and the asymptotic centralizer* (Claude Opus 5.5, September 2026; exact historical programme proof retained in the source review, not yet bundled in this selection): Theorems 6.2–6.6 give the relative-state and modular almost-invariance estimates; Theorem 7.1 compares predual and operator centrality, and Theorem 8.2 constructs the asymptotic centralizer for a general countably decomposable algebra. These are the exact earlier proofs used here. The general continuous and discrete decomposition theorems, generalized-trace comparison and Connes cocycle identities are prerequisites. Their roles are stated where used. The source targets are [Takesaki], Lemma XVIII.1.10 and Theorem XVIII.1.11(i). Sections 1–3 isolate the coefficient and approximation arguments; Sections 4–6 use them to identify and split the module quotient. [Connes 1975], Theorem 2.1.3, supplies the central cohomology input through the central-tower lesson. [Connes 1974] records the historical modular and central-sequence background.

The bounded strong-star tests, finite predual approximation and ordinary subsequence extraction are proved in [Bounded topology and tracial representations, Section 3A](bounded-topology-and-tracial-representations.md#3a-faithful-state-tests-and-ordinary-extraction), with the accompanying [bounded-topology proofs](../foundations/bounded-topology-foundations.md) and [normality and trace proofs](../foundations/tracial-normality-foundations.md). The further modular inputs have different roles: the standard-form cone estimate and relative modular operator give (1.5) and (4.5); the lacunary gap theorem gives (1.3); generalized-trace comparison and discrete trace-scaling cohomology give the normalization in Section 6; the continuous-core subtype theorem and factorial-centralizer spectral theorem give Lemma 5.1. These general modular and decomposition results remain explicit prerequisites. None is inferred from the bounded-topology companions.

A bounded sequence \((x_n)\) in a von Neumann algebra \(M\) is **strongly central** when
\[
\|[x_n,\eta]\|\longrightarrow0\quad(\eta\in M_*).
\tag{1.1}
\]
Here \((x\eta)(a)=\eta(ax)\) and \((\eta x)(a)=\eta(xa)\). On a countably decomposable algebra this implies \([x_n,a]\to0\) strongly-star for every fixed \(a\in M\), by the linked centrality theorem. Two bounded sequences are equivalent when their difference tends strongly-star to zero. A strongly-star null bounded perturbation preserves (1.1).

## 1. A modular gap removes the nonzero coefficients

Let \(M\) be countably decomposable and let \(\phi\) be an n.s.f. weight whose modular action has a gap about zero. Write
\[
N=M_\phi.
\tag{1.2}
\]
The gap projection theorem for modular actions supplies a normal faithful conditional expectation and a function \(f\in L^1(\mathbb R)\) such that
\[
E(x)=\int_{\mathbb R}f(t)\sigma_t^\phi(x)\,dt,
\qquad E:M\to N.
\tag{1.3}
\]
One may choose a smooth Fourier multiplier equal to one at zero and supported in the gap. Thus \(\int f=1\). The integral is a normal weak-star integral; the conditional expectation is the zero-frequency projection, even though \(f\) need not be positive.

**Lemma 1.1.** If \((x_n)\) is strongly central in \(M\), then
\[
x_n-E(x_n)\longrightarrow0
\quad\text{strongly-star}.
\tag{1.4}
\]

*Proof.* Choose a faithful normal state \(\psi\). The modular almost-invariance theorem gives
\[
\sigma_t^\psi(x_n)-x_n\longrightarrow0
\quad\text{strongly-star}
\tag{1.5}
\]
for each fixed \(t\). Connes's cocycle relation writes
\[
\sigma_t^\phi=\operatorname{Ad}(u_t)\sigma_t^\psi,
\qquad u_t=(D\phi:D\psi)_t.
\tag{1.6}
\]
The unitary \(u_t\) is fixed while \(n\) tends to infinity. Operator centrality gives \([u_t,x_n]\to0\) strongly-star. Combining this with (1.5) proves the same almost-invariance for \(\sigma_t^\phi\).

For every positive normal functional \(\eta\), Minkowski's inequality in the two GNS spaces gives
\[
\begin{aligned}
\|E(x_n)-x_n\|_\eta^\sharp\\
\le\int |f(t)|\,
\|\sigma_t^\phi(x_n)-x_n\|_\eta^\sharp\,dt.
\end{aligned}
\tag{1.7}
\]
The integrand tends to zero pointwise. If \(\|x_n\|\le C\), its seminorm is at most \(2\sqrt2 C\eta(1)^{1/2}\), uniformly in \(t,n\). Dominated convergence proves (1.4). \(\square\)

For \(0<\lambda<1\), the dual weight of a discrete decomposition has modular frequencies in \((\log\lambda)\mathbb Z\), so it has this gap. In the type \(III_0\) decomposition, choose the trace-contracting representative whose central trace density is bounded above by a fixed number less than one. The lacunary decomposition theorem then supplies the same gap and (1.3). No periodic modular action is required for this second case.

## 2. Fourier coefficients characterize the central sequences

Consider a normal crossed product
\[
\begin{gathered}
M=N\rtimes_\theta\mathbb Z,\\
\qquad UxU^*=\theta(x)\quad(x\in N).
\end{gathered}
\tag{2.1}
\]
Let \(E:M\to N\) be its faithful normal coefficient expectation. Put
\[
C_k(x)=E(xU^{-k})\quad(k\in\mathbb Z).
\tag{2.2}
\]
Each \(C_k\) is normal and contractive. For completeness, Fourier uniqueness follows from the dual circle action \(\widehat\theta_z(x)=x\) on \(N\) and \(\widehat\theta_z(U)=zU\). Its \(k\)-th coefficient is \(C_k(x)U^k\). Fejér averaging gives finite sums of these coefficients that converge ultraweakly to \(x\): test against a normal functional and apply the circle approximate identity to its continuous orbit coefficient. Thus all \(C_k(x)=0\) imply \(x=0\). Therefore the functionals
\[
f_{k,\eta}=\eta\circ C_k,
\qquad\eta\in N_*,
\tag{2.3}
\]
have norm-dense linear span in \(M_*\): their annihilator in \(M\) is zero, and Hahn–Banach gives the density. This is a predual density statement, so it will control errors uniformly over the unit ball of \(M\).

**Theorem 2.1.** A bounded sequence \((y_n)\) in \(N\) is strongly central in \(M\) precisely when it is strongly central in \(N\) and
\[
\theta(y_n)-y_n\longrightarrow0
\quad\text{strongly-star}.
\tag{2.4}
\]

*Proof.* Suppose first that it is strongly central in \(M\). For \(\eta\in N_*\), extend it by \(\eta\circ E\). Bimodularity of \(E\) gives
\[
[y_n,\eta\circ E]=[y_n,\eta]\circ E.
\tag{2.5}
\]
Restriction to \(N\), where \(E\) is the identity, shows that the two norms in (2.5) are equal. Thus the sequence is strongly central in \(N\). Its commutator with the fixed unitary \(U\) tends strongly-star to zero, and
\[
\theta(y_n)-y_n=[U,y_n]U^*.
\tag{2.6}
\]
This proves (2.4).

Conversely, (2.4) implies \(d_{n,k}=\theta^k(y_n)-y_n\to0\) strongly-star for each fixed integer \(k\). For positive \(k\), telescope the finitely many translates of (2.4); negative \(k\) follow by applying the fixed inverse automorphism.

If \(z=C_k(x)\), bimodularity and covariance give
\[
C_k(xy_n-y_nx)
=z\theta^k(y_n)-y_nz.
\tag{2.7}
\]
Hence, uniformly for \(\|x\|\le1\),
\[
|f_{k,\eta}(xy_n-y_nx)|
\le\|d_{n,k}\eta\|+\|[y_n,\eta]\|.
\tag{2.8}
\]
Both terms tend to zero. For a positive \(\eta\), the first is at most \(\eta(1)^{1/2}\|d_{n,k}\|_\eta\); arbitrary normal functionals are linear combinations of positive ones. The dense span from (2.3) now gives (1.1) for all \(M_*\). Indeed the commutator maps have common bound \(2\sup_n\|y_n\|\), so convergence on a dense set extends to every functional. \(\square\)

**Corollary 2.2.** In a countably decomposable discrete decomposition of a factor of type \(III_\lambda\), \(0\le\lambda<1\), with its lacunary dual weight, every strongly central sequence is equivalent to one in \(N\) satisfying (2.4). Conversely, every strongly central sequence in \(N\) satisfying (2.4) is strongly central in \(M\).

*Proof.* For the forward direction, choose the lacunary dual weight described in Section 1 and take \(y_n=E(x_n)\). Lemma 1.1 makes the difference null; Theorem 2.1 gives the remaining assertions. The reverse direction is Theorem 2.1. \(\square\)

There is also an ultrafilter consequence that needs no interchange of an ultralimit and an integral. If \(\omega\) is free, the coefficient inclusion induces an injective homomorphism
\[
(N_\omega)^{\theta_\omega}\longrightarrow M_\omega.
\tag{2.9}
\]
Represent a fixed class by \((y_n)\). Centrality in \(N\) and (2.4) hold along \(\omega\), and the estimate (2.8) proves centrality in \(M\) along that same filter. A faithful state \(\eta_0\) on \(N\) extends to the faithful state \(\eta_0E\) on \(M\); their sharp seminorms agree on \(N\). Thus the null ideals agree there, proving injectivity. This assertion does not use dominated convergence for ultrafilters.

## 3. Extending an inner approximation

Let \(\beta\in\operatorname{Aut}N\) commute with \(\theta\). Its normal extension \(\widehat\beta\) to (2.1) acts by
\[
\widehat\beta(x)=\beta(x),\qquad
\widehat\beta(U)=U.
\tag{3.1}
\]
The extension follows in the regular representation by representing \(N\) in standard form and applying its spatial implementation of \(\beta\) in every coefficient fiber; commutation with \(\theta\) preserves covariance. The inverse is the extension of \(\beta^{-1}\).

**Lemma 3.1.** Suppose \(w_n\in\mathcal U(N)\), \(\operatorname{Ad}w_n\to\beta\) in the \(u\)-topology on \(N\), and \(\theta(w_n)-w_n\to0\) strongly-star. Then
\[
\operatorname{Ad}w_n\longrightarrow\widehat\beta
\quad\text{in the }u\text{-topology on }M.
\tag{3.2}
\]

*Proof.* For fixed \(k\), the same telescoping argument gives \(\theta^k(w_n)-w_n\to0\) strongly-star. The exact coefficient formula is
\[
C_k(w_nxw_n^*)
=w_nC_k(x)\theta^k(w_n^*).
\tag{3.3}
\]
Put \(b_{n,k}=w_n\theta^k(w_n^*)-1\). It tends strongly to zero, since
\[
\begin{aligned}
\delta_{n,k}&=\theta^k(w_n^*)-w_n^*,\\
b_{n,k}^*b_{n,k}&=\delta_{n,k}^*\delta_{n,k}.
\end{aligned}
\tag{3.4}
\]
Writing the right side of (3.3) as \((w_nC_k(x)w_n^*)(1+b_{n,k})\), we get
\[
\begin{aligned}
\|f_{k,\eta}\operatorname{Ad}w_n
 -f_{k,\eta}\widehat\beta\|
\le{}&\|\eta\operatorname{Ad}w_n-\eta\beta\|\\
&+\|b_{n,k}\eta\|.
\end{aligned}
\tag{3.5}
\]
The right side tends to zero. The coefficient functionals are norm dense and all the automorphisms are isometries on the predual, so (3.2) follows. Inversion also converges: composing the difference with \(\operatorname{Ad}w_n\) rewrites the inverse test using the fixed functional \(\eta\widehat\beta^{-1}\). \(\square\)

**Lemma 3.2 (an equivariant correction).** Let \(N\) be a strongly stable factor with separable predual. Suppose \(p_a(\theta)=0\) and \(\beta\) is approximately inner and commutes with \(\theta\). There are implementers \(w_n\) for \(\beta\) satisfying the hypotheses of Lemma 3.1.

*Proof.* Choose \(u_n\) with \(\operatorname{Ad}u_n\to\beta\). Commutation gives
\[
\operatorname{Ad}\theta(u_n)
=\theta\operatorname{Ad}(u_n)\theta^{-1}\longrightarrow\beta.
\tag{3.6}
\]
Thus \(c_n=u_n^*\theta(u_n)\) is strongly central. Put \(C=[(c_n)]\in\mathcal U(N_\omega)\). The central-tower lesson, Theorem 5.1, applied to \(C^*\), gives a unitary \(X\) satisfying \(\theta_\omega(X)=C^*X\). Put \(V=X^*\). Then \(\theta_\omega(V)=VC\), so
\[
C=V^*\theta_\omega(V),
\qquad C=[(c_n)].
\tag{3.7}
\]
Lift \(V\) to exactly unitary \(\omega\)-central \(v_n\), and set \(w'_n=u_nv_n^*\) at the same coordinate. Then
\[
\begin{gathered}
(w'_n)^*\theta(w'_n)=v_nc_n\theta(v_n^*)\\
\longrightarrow1
\quad\text{strongly-star along }\omega.
\end{gathered}
\tag{3.8}
\]
Also \(\operatorname{Ad}w'_n\to\beta\) along \(\omega\). Choose a norm-dense sequence \((\eta_j)\) in the unit ball of \(N_*\) and a faithful normal state \(\eta_0\). At stage \(r\), intersect the finitely many ultrafilter sets on which the first \(r\) predual errors \(\|\eta_j\operatorname{Ad}w'_n-\eta_j\beta\|\) and the sharp error in (3.8) for \(\eta_0\) are below \(1/r\). A free ultrafilter contains every cofinite set, so this intersection contains a coordinate larger than the preceding choice. The faithful-state and uniform finite-test results of the bounded-topology prerequisite turn these tests into ordinary convergence for both conclusions. Relabel the same chosen coordinates as \(w_r\); the correction and original implementer have remained paired.

Finally, \(\theta(w_n)-w_n=w_n((w_n)^*\theta(w_n)-1)\). The moving-functional lemma in the implementer prerequisite applies because \(\operatorname{Ad}w_n\to\beta\). It gives strong-star convergence, including the adjoint seminorm. Thus varying multipliers have not been discarded without control. \(\square\)

## 4. A scalar at one modular period

Now let \(M\) be the hyperfinite factor of type \(III_\lambda\), \(0<\lambda<1\), with separable predual. Put
\[
L=-\log\lambda,\qquad P=\frac{2\pi}{L}.
\tag{4.1}
\]
The flow of weights has time period \(L\). The modular action of a generalized trace has time period \(P\). These are different clocks.

The Powers construction supplies a faithful normal state \(\psi\) with \(\sigma_P^\psi=\operatorname{id}\). For \(\alpha\in\operatorname{Aut}M\), define
\[
\zeta(\alpha)=(D(\psi\circ\alpha):D\psi)_P.
\tag{4.2}
\]
The two modular actions have period \(P\), so the inner action of (4.2) is the identity. Factoriality therefore makes \(\zeta(\alpha)\) a scalar in \(\mathbb T\).

**Proposition 4.1.** The map \(\zeta:\operatorname{Aut}M\to\mathbb T\) is a continuous homomorphism, is trivial on inner automorphisms, and is independent of the chosen faithful normal state whose modular action is the identity at this same time \(P\).

*Proof.* The chain and naturality rules give
\[
\begin{aligned}
(D(\psi\alpha\beta):D\psi)_P
&=\beta^{-1}\bigl((D(\psi\alpha):D\psi)_P\bigr)\\
&\qquad\cdot(D(\psi\beta):D\psi)_P.
\end{aligned}
\tag{4.3}
\]
The factors are scalars, so this is \(\zeta(\alpha)\zeta(\beta)\). For an inner automorphism,
\[
(D(\psi\operatorname{Ad}u):D\psi)_P
=u^*\sigma_P^\psi(u)=1.
\tag{4.4}
\]

If \(\chi\) is another faithful normal state with \(\sigma_P^\chi=\operatorname{id}\), \(d=(D\chi:D\psi)_P\) is scalar. In the chain rule for \((D(\chi\alpha):D\chi)_P\), naturality supplies \(\alpha^{-1}(d)=d\), and the inverse comparison supplies \(d^{-1}\). They cancel, leaving (4.2). The same cancellation allows any n.s.f. weight \(\chi\) with \(\sigma_P^\chi=\operatorname{id}\) in place of the state.

For continuity, put \(\psi_j=\psi\alpha_j\) and \(\psi_0=\psi\alpha\). If \(\alpha_j\to\alpha\) in the \(u\)-topology, \(\|\psi_j-\psi_0\|\to0\). The relative modular estimate in the linked prerequisite, applied to these two states at time \(P\), yields
\[
\begin{aligned}
\left|1-\zeta(\alpha_j)\zeta(\alpha)^{-1}\right|\\
\le(8P^2+5P+8)\|\psi_j-\psi_0\|.
\end{aligned}
\tag{4.5}
\]
Indeed their derivative at \(P\) is exactly the scalar on the left, so evaluation by \(\psi_0\) does not change it. This proves continuity, for nets as well as sequences. \(\square\)

The common time \(P\) is necessary. On \(R_\lambda\overline\otimes M_2\), let \(\omega\) be the Powers state and let \(\operatorname{tr}_2\) be normalized matrix trace. The states
\[
\begin{gathered}
\psi=\omega\otimes\operatorname{tr}_2,\qquad
\chi=\omega\otimes\operatorname{Tr}(d\,\cdot),\\
d=\frac{\operatorname{diag}(1,\sqrt\lambda)}
        {1+\sqrt\lambda}
\end{gathered}
\]
are faithful and periodic, but \(\chi\) has period \(2P\). At time \(P\), the two diagonal entries of \(d^{iP}\) have ratio \(-1\), so
\[
(D\chi:D\psi)_P=1\otimes(2d)^{iP}
\]
is not scalar. If \(v=1\otimes\begin{pmatrix}0&1\\1&0\end{pmatrix}\), then \(\sigma_P^\chi(v)=-v\), and
\[
(D(\chi\operatorname{Ad}v):D\chi)_P
=v^*\sigma_P^\chi(v)=-1.
\]
Using an arbitrary periodic state would therefore fail even on this inner automorphism. The generalized traces used below satisfy the required identity at \(P\).

Take a generalized trace \(\phi\) and use generalized-trace comparison to replace \(\alpha\) by an inner perturbation with
\[
\phi\circ\alpha=\mu\phi,\qquad\mu>0.
\tag{4.6}
\]
Equations (4.2) and (4.6) give
\[
\zeta(\alpha)=\mu^{iP}.
\tag{4.7}
\]
Another such normalization changes \(\mu\) by a power of \(\lambda\). Thus \(\zeta\) is the phase coordinate of the module, with the time convention
\[
\begin{aligned}
\operatorname{mod}(\alpha)&=[-\log\mu]\in\mathbb R/L\mathbb Z,\\
\zeta(\alpha)&=e^{-iP\operatorname{mod}(\alpha)}.
\end{aligned}
\tag{4.8}
\]
The exponential in (4.8) is well-defined on the quotient. This is the translation coordinate for the flow of weights: a scaling \(\phi\alpha=e^{-s}\phi\) has flow translation time \(s\).

## 5. One coherent trace-scaling flow

The next construction uses a continuous trace-scaling action on the hyperfinite semifinite factor \(R_\infty\). Its existence follows from the continuous-core theorem and the already known Powers models; it does not require uniqueness of a type \(III_1\) factor.

**Lemma 5.1.** There are an n.s.f. trace \(\tau\) on \(R_\infty\) and a continuous action \(s\mapsto b_s\) such that
\[
\tau b_s=e^{-s}\tau\quad(s\in\mathbb R).
\tag{5.1}
\]

*Proof.* Choose two Powers parameters \(q,r\in(0,1)\) with \(\log q/\log r\) irrational, and form their tensor product with its product state. The modular eigenvectors in the Powers lesson give a dense joint eigenvector family, of eigenvalues \(q^k r^l\). The zero-frequency space has \(k=l=0\), so the product centralizer is exactly the tensor product of the two factorial centralizers. One can see the equality on GNS vectors: the product of their state-preserving expectations projects onto the zero-frequency space, and the separating state vector makes equality of those vectors equality of the bounded operators.

The additive subgroup \((\log q)\mathbb Z+(\log r)\mathbb Z\) is dense in \(\mathbb R\). For example, pigeonhole approximation supplies nonzero elements arbitrarily near zero, and a closed nondiscrete subgroup of \(\mathbb R\) is all of \(\mathbb R\). Hence the ordinary modular spectrum of this product is all of \([0,\infty)\). The factorial-centralizer spectral theorem identifies it with the Connes invariant. Thus the product is an AFD factor of type \(III_1\).

Its continuous core is a semifinite factor, since the center flow of a type \(III_1\) factor is trivial. The dual action scales its n.s.f. trace by \(e^{-s}\), by the general continuous-core theorem. The core is injective: in its regular representation the original AFD algebra is injective, and the strongly continuous implementing representation of the amenable group \(\mathbb R\) normalizes it. Apply Averaging, crossed products and injectivity, Theorem 2.3. Its locally compact hypothesis includes this strongly continuous real action.

The core cannot be a finite factor or a type I factor: automorphisms of either preserve its scalar trace, contradicting nontrivial trace scaling. It is therefore an injective type \(II_\infty\) factor with separable predual. Choose a nonzero finite-trace projection \(e\) in this core \(Q\). Its corner \(eQe\) is an injective \(II_1\) factor: compress an injectivity retraction to \(eB(H)e\). By Small corners and the second injective proof, Theorem 4.1, \(eQe\cong R\). Semifinite-factor projection comparison gives countably many orthogonal projections equivalent to \(e\) with sum \(1\); separable predual makes the finite-trace exhaustion countable. The resulting matrix units identify \(Q\) normally with \(eQe\overline\otimes B(\ell^2)\): finite matrix compressions give the coefficient map and its inverse, and their strong limits exhaust the identity. Hence \(Q\cong R_\infty\). Transport its trace and dual action. \(\square\)

The generalized continuous decomposition and [Connes 1973], Corollary 3.2.7(a), the factorial-centralizer spectral theorem, are used here at their stated strengths. The argument specializes their conclusions; it does not construct a new general flow of weights.

## 6. The split module quotient

**Theorem 6.1.** For the hyperfinite type \(III_\lambda\) factor with separable predual,
\[
\ker\zeta=\overline{\operatorname{Inn}M}.
\tag{6.1}
\]
Consequently its module quotient is \(\mathbb R/L\mathbb Z\), and the exact sequence
\[
\begin{gathered}
1\longrightarrow\overline{\operatorname{Inn}M}
\longrightarrow\operatorname{Aut}M\\
\xrightarrow{\ \operatorname{mod}\ }\mathbb R/L\mathbb Z
\longrightarrow1.
\end{gathered}
\tag{6.2}
\]
has a continuous group section.

*Proof of the kernel statement.* Proposition 4.1 gives the inclusion of the closure of the inner group in the kernel. For the converse, choose a discrete decomposition
\[
\begin{gathered}
M=N\rtimes_\theta\mathbb Z,\qquad N\cong R_\infty,\\
\tau\theta=\lambda\tau,\qquad\phi=\tau E.
\end{gathered}
\tag{6.3}
\]
The generalized-trace comparison theorem first gives (4.6). Since \(\zeta(\alpha)=1\), (4.7) implies \(\mu\in\lambda^{\mathbb Z}\). Composing with a suitable inner power of \(U\) makes \(\mu=1\). Hence we may assume \(\phi\alpha=\phi\).

This automorphism commutes with \(\sigma^\phi\), preserves \(N\), and has \(\alpha(U)=vU\) for a unitary \(v\in N\). The discrete suspension in [Central triviality and modular powers, Lemma 1.2](central-triviality-and-modular-powers.md#1a-from-real-trace-scaling-to-the-needed-discrete-coboundary) proves the required reduction to real trace-scaling stability; that proof does not use this module theorem. Exact discrete trace-scaling stability gives \(v=w^*\theta(w)\), with \(w\in\mathcal U(N)\). Replacing \(\alpha\) by \(\operatorname{Ad}w\circ\alpha\) makes \(\alpha(U)=U\). This perturbation still preserves \(\phi\), because \(w\) belongs to its centralizer.

Thus \(\alpha=\widehat\beta\), where \(\beta\in\operatorname{Aut}N\) preserves \(\tau\) and commutes with \(\theta\). Every trace-preserving automorphism of \(R_\infty\) is approximately inner, by the semifinite prerequisite. The same prerequisite proves \(p_a(\theta)=0\), since its trace multiplier is different from one. Also \(R_\infty\) is strongly stable. Lemmas 3.2 and 3.1 therefore prove that \(\widehat\beta\) is approximately inner on \(M\). Removing the two inner perturbations gives (6.1).

*Construction of the section.* Use Lemma 5.1 and choose \(\theta=b_L\). The discrete crossed product is the same hyperfinite type \(III_\lambda\) factor, by the Powers classification. Extend the flow by
\[
B_s|_N=b_s,\qquad B_s(U)=U.
\tag{6.4}
\]
The normal extensions form a group because they agree on the generating coefficients and \(U\). Their continuity follows directly on the predual tests of Section 2:
\[
f_{k,\eta}\circ B_s=f_{k,\eta\circ b_s}.
\]
Thus the difference at \(s,t\) has norm at most \(\|\eta\circ b_s-\eta\circ b_t\|\), which tends to zero as \(s\to t\). Density of the coefficient tests and the common isometric bound extend convergence to every normal functional. This proves continuity in the \(u\)-topology. We have \(B_L=\operatorname{Ad}U\) and \(\phi B_s=e^{-s}\phi\). Choose a bounded self-adjoint Borel logarithm \(h\in W^*(U)\) with \(U=e^{iLh}\), and set
\[
\kappa_s=\operatorname{Ad}(e^{-ish})B_s.
\tag{6.5}
\]
Every \(B_s\) fixes \(h\), so \(\kappa_{s+t}=\kappa_s\kappa_t\). Moreover \(\kappa_L=\operatorname{id}\), and inner invariance gives \(\zeta(\kappa_s)=e^{-iPs}\). Thus (6.5) descends to a continuous section from \(\mathbb R/L\mathbb Z\). It is a right inverse to (4.8), proving surjectivity and (6.2). \(\square\)

There is a second circle in the same automorphism group. The modular automorphisms are centrally trivial by the modular almost-invariance theorem. They preserve \(\phi\), so Theorem 6.1 makes them approximately inner. Since their inner-period group is \(P\mathbb Z\), they give an injective homomorphism
\[
\begin{gathered}
\mathbb R/P\mathbb Z\longrightarrow
\overline{\operatorname{Inn}M}/\operatorname{Inn}M,\\
\qquad[t]\longmapsto[\sigma_t^\phi].
\end{gathered}
\tag{6.6}
\]
Its image is central: for any \(\alpha\), naturality and Connes's cocycle relation make \(\alpha\sigma_t^\phi\alpha^{-1}\) an inner perturbation of \(\sigma_t^\phi\). The circle in (6.2) detects trace scaling; the one in (6.6) consists of modular outer classes with trivial module. Identifying every centrally trivial automorphism requires the relative-character argument in addition to these facts.

## 7. Exercises with solutions

Level 1 is a computation. Level 2 checks a construction or estimate. Level 3 tests a topology or proves a compatibility assertion.

**Exercise 7.1 (why the coefficient tests are norm dense).** *Level 2.* Suppose a functional family (2.3) has zero annihilator in \(M\). Prove norm density of its linear span in \(M_*\), and explain why a uniformly bounded family of maps converging on that span converges on all of \(M_*\).

*Solution.* If its norm-closed span were proper, Hahn–Banach would give a nonzero continuous functional on \(M_*\) vanishing there. Since \((M_*)^*=M\), it would be a nonzero annihilator, a contradiction. For maps \(T_n\) with \(\|T_n\|\le C\), choose a span element \(\eta'\) with \(\|\eta-\eta'\|<\varepsilon\). Then \(\limsup_n\|T_n\eta\|\le C\varepsilon\). Let \(\varepsilon\) tend to zero. Strong centrality uses the bound \(2\sup_n\|y_n\|\); automorphism differences use the bound two.

**Exercise 7.2 (weak invariance is insufficient).** *Level 3.* Let \(N=L^\infty(\mathbb T)\) with Haar measure, let \(\theta(f)(z)=f(-z)\), and put \(y_n(z)=z^{2n+1}\). These sequences are strongly central in \(N\). Show that \(\theta(y_n)-y_n\to0\) weak-star, but that \((y_n)\) is not strongly central in \(N\rtimes_\theta\mathbb Z\).

*Solution.* Abelianity makes every predual commutator zero. Also \(\theta(y_n)-y_n=-2y_n\), whose integrals against every \(L^1\) function tend to zero by Fourier approximation and the Riemann–Lebesgue argument. Its \(L^2\) norm is exactly two. The crossed product has the faithful trace \(\nu E\), and \([U,y_n]=-2y_nU\), also of \(L^2\) norm two. Thus operator centrality fails. The estimate (2.8) needs strong convergence, rather than weak convergence, of the invariance defect.

**Exercise 7.3 (the side of the coefficient defect).** *Level 2.* For \(w\in\mathcal U(N)\), compute \(C_k(wxw^*)\). If \(b=w\theta^k(w^*)-1\), explain why the error pairs with \(b\eta\), rather than \(\eta b\).

*Solution.* Covariance gives \(w^*U^{-k}=U^{-k}\theta^k(w^*)\). Applying bimodularity to \(wxw^*U^{-k}\) gives (3.3). Its difference from \(wC_k(x)w^*\) is \(wC_k(x)w^*b\). Since \((b\eta)(a)=\eta(ab)\), its supremum over \(\|x\|\le1\) is bounded by \(\|b\eta\|\). For positive \(\eta\), this is bounded by \(\eta(1)^{1/2}\eta(b^*b)^{1/2}\). Equation (3.4) makes this tend to zero without asserting that multiplication by every moving unitary preserves both strong seminorms.

**Exercise 7.4 (two order-three symmetries).** *Level 1.* Let \(\lambda=e^{-3}\). Compute \(L,P\), the module of \(\kappa_1\), and the module and outer order of \(\sigma_{P/3}^\phi\). Are the two order-three classes the same?

*Solution.* Here \(L=3\) and \(P=2\pi/3\). The section has additive module \(\operatorname{mod}(\kappa_1)=[1]\in\mathbb R/3\mathbb Z\) and period scalar \(\zeta(\kappa_1)=e^{-2\pi i/3}\), a phase of order three, and \(\kappa_1^3=\operatorname{id}\). The modular automorphism has additive module \([0]\), equivalently period scalar \(1\), while its outer class has order three because \(T(M)=P\mathbb Z\). Indeed \(\sigma_{P/3}^\phi(U)=e^{-2\pi i/3}U\). This phase on \(U\) does not determine its module: \(\kappa_1\) itself fixes \(U\), since both factors in (6.5) do. The first class has nontrivial module; the second has trivial module, so they differ.

**Exercise 7.5 (continuity from the period scalar).** *Level 2.* Let \(\alpha_n\to\alpha\) in the \(u\)-topology. Derive (4.5), then prove that an approximately inner automorphism has trivial period scalar without assuming continuity of a general flow-of-weights construction.

*Solution.* Set \(\omega_n=\psi\alpha_n\), \(\omega=\psi\alpha\). The chain rule gives \((D\omega_n:D\omega)_P=\zeta(\alpha_n)\zeta(\alpha)^{-1}\). These derivatives are scalar because both modular actions have period \(P\). The relative-state estimate
\[
\begin{aligned}
|1-\omega((D\omega_n:D\omega)_P)|\\
\le(8P^2+5P+8)\|\omega_n-\omega\|
\end{aligned}
\]
is exactly (4.5). For inner approximants the scalar is one by (4.4); taking the limit proves the claim. This supplies the forward inclusion in (6.1).

**Exercise 7.6 (changing the logarithm changes only an inner factor).** *Level 3.* Use a second bounded self-adjoint logarithm \(h'\in W^*(U)\), with \(e^{iLh'}=U\), in (6.5). Prove that it also gives a circle section, and compare the two sections at each \(s\).

*Solution.* Both logarithms are Borel functions of \(U\), commute, and are fixed by \(B_s\). Thus both formulas give homomorphisms and both become the identity at \(s=L\). Their quotient at a fixed parameter is
\[
\kappa'_s\kappa_s^{-1}
=\operatorname{Ad}\bigl(e^{-is(h'-h)}\bigr).
\]
It is inner, so the two maps give the same module and the same outer class at every parameter. The logarithm choice affects the representatives in \(\operatorname{Aut}M\), while the quotient coordinate in (6.2) stays fixed.

## References

- [Connes 1974] Alain Connes, “Almost periodic states and factors of type \(III_1\),” *Journal of Functional Analysis* **16** (1974), 415–445. [Publisher open-archive article](https://www.sciencedirect.com/science/article/pii/0022123674900597). This is a historical bibliographic reference, checked here at metadata level; no direct reading of its mathematical body is claimed. The modular almost-invariance and asymptotic-centralizer proofs used here are the exact named programme prerequisite.
- [Connes 1975] Alain Connes, “Outer conjugacy classes of automorphisms of factors,” *Annales scientifiques de l’École Normale Supérieure* (4) **8** (1975), 383–419. [Open article](https://www.numdam.org/article/ASENS_1975_4_8_3_383_0.pdf).
- [Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. Lemma XVIII.1.10 and Theorem XVIII.1.11(i), printed pages 307–310: discrete-core central sequences and the split module sequence. The closure over the inner group in (6.1) is essential. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).
- [Connes 1973] Alain Connes, “Une classification des facteurs de type III,” *Annales scientifiques de l’École Normale Supérieure* (4) **6** (1973), 133–252. Corollary 3.2.7(a) supplies the exact factorial-centralizer spectral input to Lemma 5.1. [Open article](https://www.numdam.org/item/ASENS_1973_4_6_2_133_0/).
