# Trace scaling on the hyperfinite semifinite factor

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Source, construction and direct proof review by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently written programme text: CC0 1.0. Full transitive prerequisite review remains unfinished.*

## Introduction

A finite trace forces every automorphism to preserve the size of the identity. An infinite semifinite factor has more room: an automorphism can multiply the trace of every finite projection by the same positive number. On the hyperfinite semifinite factor, a multiplier different from one determines the automorphism up to conjugacy.

The proof brings together three mechanisms. Central triviality makes commutators with approximately inner automorphisms inner. Type-I amplification preserves central sequences and absorbs an automorphism up to an explicit inner perturbation. A trace-preserving automorphism can then be reduced to a finite corner, where the hyperfinite finite-factor classification applies.

The actual classical construction sources are [Connes] and [Takesaki III]; [Takesaki II] supplies the related real-action stability theorem. [Ando–Haagerup] provides ultraproduct context. The programme prerequisites are [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md), Proposition 6.3 for absorption of the original action, and [Comparing asymptotically aperiodic automorphisms](comparing-asymptotically-aperiodic-automorphisms.md), with their full stated hypotheses.

Proposition 3.1 below supplies a direct proof of the full type-I centralizer interface. Approximate innerness of every automorphism of the finite hyperfinite factor is Local approximation and the hyperfinite finite factor, Theorem 6.3; Corollary 5.2 supplies the amplified finite-corner identification. The [normal tensor and tracial product companion](../foundations/normal-tensor-and-tracial-product-foundations.md), TF1–TF4, supplies normal slices, product-functional norm density and the specified tracial product identifications used here. Section 6 links the full discrete stability argument and states its remaining general trace and modular inputs. The factor trace, comparison, hyperfinite-corner and general tensor foundations retain their own proof obligations.

Write \(R\) for the hyperfinite factor of type \({\rm II}_1\), with normalized trace \(\tau_R\), and put
\[
R_\infty=R\overline\otimes B(\ell^2(\mathbb N)),
\qquad \tau=\tau_R\otimes\operatorname{Tr}.
\tag{0.1}
\]
An automorphism is approximately inner if it lies in the closure of the inner automorphisms for pointwise norm convergence on the predual. We denote that closure by \(\overline{\operatorname{Inn}}(M)\). A bounded sequence \((x_n)\) is strongly central if
\(\|[x_n,\psi]\|\to0\) for every \(\psi\in M_*\). An automorphism \(\theta\) is centrally trivial if \(\theta(x_n)-x_n\to0\) strongly-star for every such sequence. Denote these automorphisms by \(\operatorname{Ct}(M)\).

For a faithful normal state \(\varphi\), use
\[
\begin{aligned}
\|x\|_\varphi^2&=\varphi(x^*x),\\
\|x\|_\varphi^{\sharp\,2}
&=\varphi(x^*x)+\varphi(xx^*).
\end{aligned}
\tag{0.2}
\]
On bounded sets the sharp seminorm tests the strong-star topology. The asymptotic period \(p_a(\theta)\) is the order of \(\theta\) modulo \(\operatorname{Ct}(M)\); infinite order is denoted by \(0\).

## 1. A commutator with an approximately inner automorphism

**Lemma 1.1.** Let \(M\) have separable predual. If \(\theta\in\operatorname{Ct}(M)\) and \(\alpha\in\overline{\operatorname{Inn}}(M)\), then
\[
\alpha^{-1}\theta\alpha\theta^{-1}\in\operatorname{Inn}(M).
\tag{1.1}
\]
No trace or strong-stability assumption is required.

*Proof.* We first convert central triviality into a finite-neighborhood statement. Given finitely many normal positive functionals \(\rho_j\) and \(a>0\), there is a neighborhood \(V\) of the identity in \(\operatorname{Aut}(M)\) such that
\[
\begin{gathered}
\operatorname{Ad}v\in V,\quad v\in\mathcal U(M)\\
\Longrightarrow\quad
\|\theta(v)-v\|_{\rho_j}<a
\quad\text{for every }j.
\end{gathered}
\tag{1.2}
\]
Otherwise a countable neighborhood basis supplies unitaries \(v_n\) with \(\operatorname{Ad}v_n\to\mathrm{id}\) and with at least one of these errors at least \(a\). The identity
\(\|[v_n,\psi]\|=\|\psi\circ\operatorname{Ad}v_n-\psi\|\)
shows that \((v_n)\) is strongly central. Central triviality makes every error tend to zero, a contradiction.

Fix a faithful normal state \(\varphi\), and define two fixed states
\[
\rho_1=\varphi\circ\alpha^{-1},
\qquad
\rho_2=\varphi\circ\theta\circ\alpha^{-1}\circ\theta^{-1}.
\tag{1.3}
\]
Set \(a_n=2^{-n}\). Choose \(V_n\) so that (1.2) holds for these two states with error \(a_n\). Continuity of multiplication and inversion in \(\operatorname{Aut}(M)\) permits a decreasing neighborhood basis \(U_n\) at \(\alpha\) with
\[
U_nU_n^{-1}\subset V_n,
\tag{1.4}
\]
and, for every \(\beta\in U_n\),
\[
\begin{aligned}
\|\varphi\circ\beta^{-1}-\rho_1\|&<a_n^2,\\
\|\varphi\circ\theta\circ\beta^{-1}\circ\theta^{-1}-\rho_2\|&<a_n^2.
\end{aligned}
\tag{1.5}
\]
Choose unitaries \(u_n\) with \(\beta_n=\operatorname{Ad}u_n\in U_n\). Put
\[
v_n=u_{n+1}u_n^*,
\qquad
w_n=u_n^*\theta(u_n).
\tag{1.6}
\]
Then \(\operatorname{Ad}v_n=\beta_{n+1}\beta_n^{-1}\in V_n\). Write
\[
B_n=\theta(v_n)-v_n,\qquad
A_n=v_n^*\theta(v_n)-1.
\tag{1.7}
\]
The element \(A_n\) is a unitary minus the identity, so it is normal. Moreover
\[
A_n^*A_n=A_nA_n^*=B_n^*B_n.
\tag{1.8}
\]
Thus, for \(d_n=w_{n+1}-w_n=u_n^*A_n\theta(u_n)\),
\[
\begin{aligned}
\varphi(d_nd_n^*)&=(\varphi\circ\beta_n^{-1})(B_n^*B_n),\\
\varphi(d_n^*d_n)&=
(\varphi\circ\theta\circ\beta_n^{-1}\circ\theta^{-1})(B_n^*B_n).
\end{aligned}
\tag{1.9}
\]
Equation (1.2) bounds each fixed-state value by \(a_n^2\). Since \(\|B_n\|\le2\), (1.5) adds at most \(4a_n^2\) to either value. Hence
\[
\|w_{n+1}-w_n\|_\varphi^\sharp
\le\sqrt{10}\,2^{-n}.
\tag{1.10}
\]
Both \(w_n\) and \(w_n^*\) are strong Cauchy. Their limits are adjoints, and the equalities \(w_n^*w_n=w_nw_n^*=1\) pass to the limit. The limit \(w\) is unitary.

Finally,
\[
\operatorname{Ad}w_n
=\beta_n^{-1}\theta\beta_n\theta^{-1}
\longrightarrow\alpha^{-1}\theta\alpha\theta^{-1}.
\tag{1.11}
\]
Strong-star convergence of the unitaries to \(w\) also gives predual convergence of their inner automorphisms to \(\operatorname{Ad}w\). These two limits agree, proving (1.1). \(\square\)

*Reference:* [Connes, Lemma 2.2.2].

The two transported states in (1.3) are essential in a nontracial algebra. Left and right multiplication by the varying implementers do not preserve a fixed state seminorm.

## 2. Central triviality can be detected in the outer group

Let \(q:\operatorname{Aut}(M)\to\operatorname{Out}(M)\) be the quotient map. For a strongly stable factor with separable predual, tensor absorption identifies the centralizer of the approximately inner outer classes.

**Theorem 2.1.** Under these hypotheses and the tensor-absorption prerequisite,
\[
q(\operatorname{Ct}(M))
=C_{\operatorname{Out}(M)}
   \bigl(q(\overline{\operatorname{Inn}}(M))\bigr).
\tag{2.1}
\]

*Proof.* Lemma 1.1 gives one inclusion.

For the reverse inclusion, suppose \(\theta\) is not centrally trivial and put \(p=p_a(\theta)\ne1\). Proposition 6.3 of the matrix-absorption lesson, concerning the original action, allows us to replace \(\theta\), up to outer conjugacy, by \(\theta\otimes\sigma_p\) on \(M\overline\otimes R\). Approximately inner automorphisms form a normal subgroup of the automorphism group: conjugate any net of inner approximants. Their outer image is therefore invariant under this replacement. Inner perturbations also do not change the outer commutation question.

We construct \(a\in\operatorname{Aut}(R)\) for which
\[
\sigma_pa\sigma_p^{-1}a^{-1}
\quad\text{is outer}.
\tag{2.2}
\]
For \(p\ge2\), use the product model with a \(p\)-dimensional clock in each coordinate. Multiply a clock by a scalar so its first two eigenvalues are \(1,\zeta_p\). Let \(T\) be a rotation by \(\pi/8\) on their two-dimensional span, acting as the identity on its orthogonal complement, and let \(V=T c_pT^*\). Take \(a=\bigotimes\operatorname{Ad}V\).

The coordinate commutator
\[
W=c_pV c_p^*V^*
\tag{2.3}
\]
acts as the identity off this span. On the span its determinant is one and its half-trace is
\[
\frac12\operatorname{Tr}(W|_{\mathbb C^2})
=1-\sin^4(\pi/p)\in[0,1).
\tag{2.4}
\]
The calculation is the rotation formula of Section 2 in [The simple outer group of the hyperfinite factor](the-simple-outer-group-of-the-hyperfinite-factor.md). Thus \(W\) has two distinct eigenvalues. A matrix entry between their eigenvectors is moved by \(\operatorname{Ad}W\) by a nonzero scalar difference. Place this same entry in successively later coordinates. The resulting sequence is strongly central, but its tracial \(2\)-norm displacement under the product commutator is a fixed positive number. The commutator is not centrally trivial and hence is outer.

For \(p=0\), the model \(\sigma_0\) has infinitely many two-dimensional coordinates. Make the same choice of \(V\) on those coordinates and take the identity on all other coordinates. The same tail entries prove (2.2).

Every automorphism of \(R\), including \(a\), is approximately inner. TF1 product normal-functionals and their norm density show that \(\mathrm{id}_M\otimes a\) is approximately inner on \(M\overline\otimes R\). Its commutator with \(\theta\otimes\sigma_p\) is
\[
\mathrm{id}_M\otimes
(\sigma_pa\sigma_p^{-1}a^{-1}).
\tag{2.5}
\]
This is outer. Indeed an inner tensor-product automorphism has inner restrictions to both factors, as proved in Lemma 4.1 below. Consequently the outer class of \(\theta\) fails to centralize the approximately inner classes. \(\square\)

Only a nontrivial commutator is needed here. Its nonzero powers need not all be outer.

## 3. What type-I amplification preserves

Let \(B=B(\ell^2(\mathbb N))\).

**The quotient at nonfactor scope.** The linked central-sequence lesson assumes a factor. Here is the finite-quotient construction at the full scope needed for both \(N\) and \(N\overline\otimes B\). The latter also has separable predual: TF1 gives norm-dense finite sums of product functionals, and countable norm-dense sets in \(N_*\) and in the trace-class predual of \(B(\ell^2(\mathbb N))\), with rational complex coefficients, give a countable dense set of such sums. Let \(M\ne0\) be any von Neumann algebra with separable predual, let \(\varphi\) be a faithful normal state, and let \(\omega\) be any free ultrafilter on \(\mathbb N\). Put
\[
\begin{aligned}
&C_\omega(M)\\
&=\{(x_n)\in\ell^\infty(\mathbb N,M):\\
&\|[x_n,\rho]\|\longrightarrow_\omega0\\
&\text{for every }\rho\in M_*\}.
\end{aligned}
\]
The functional actions are \((x\rho)(a)=\rho(ax)\) and \((\rho x)(a)=\rho(xa)\). Their product and adjoint identities give
\[
\begin{aligned}
{}[xy,\rho]&=x[y,\rho]+[x,\rho]y,\\
[x^*,\rho]^*&=-[x,\rho^*].
\end{aligned}
\]
Together with \(\|[x,\rho]\|\le2\|x\|\|\rho\|\), these identities prove that \(C_\omega(M)\) is a unital \(C^*\)-algebra, including norm closure.

Define a bounded positive unital functional on this algebra by
\[
t_\varphi((x_n))=\lim_{n\to\omega}\varphi(x_n).
\]
Scalar ultralimits are linear and positive. For \(x,y\in C_\omega(M)\),
\[
|\varphi(x_ny_n-y_nx_n)|
\le\|y_n\|\,\|[x_n,\varphi]\|\longrightarrow_\omega0,
\]
so \(t_\varphi\) is tracial. This argument uses no scalar ultraweak limit of \(x_n\); in a nonfactor such a limit can be nonscalar.

For this paragraph use the normalized sharp seminorm
\[
\|x\|_{\varphi,\#}^2
=\tfrac12\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr).
\]
The tracial identity just proved gives
\[
\lim_{n\to\omega}\|x_n\|_{\varphi,\#}^2
=t_\varphi(x^*x)=t_\varphi(xx^*).
\]
The faithful-state bounded-topology criterion therefore identifies
\[
\begin{aligned}
&J_\omega(M)\\
&=\{x\in C_\omega(M):\\
&\qquad x_n\longrightarrow_\omega0
       \text{ strongly-star}\}\\
&=\{x\in C_\omega(M):t_\varphi(x^*x)=0\}.
\end{aligned}
\]
This is a closed two-sided *-ideal. Indeed Cauchy–Schwarz makes the null space linear, traciality makes it *-closed, and for \(a\in C_\omega(M)\),
\[
\begin{aligned}
&t_\varphi((ax)^*(ax))\\
&\le\|a\|^2t_\varphi(x^*x),\\
&t_\varphi((xa)^*(xa))\\
&=t_\varphi(x^*x\,aa^*)\\
&\le\|a\|^2t_\varphi(x^*x).
\end{aligned}
\]
In the last inequality one may write the trace as
\(t_\varphi((x^*x)^{1/2}aa^*(x^*x)^{1/2})\), so it is an inequality between positive elements. Continuity gives closedness. Cauchy–Schwarz also shows that \(t_\varphi\) vanishes on this ideal, and hence descends to a faithful tracial state \(\tau_\varphi\) on
\[
A=C_\omega(M)/J_\omega(M).
\]
Faithfulness follows from the displayed description of the square-null ideal: if \(a=\pi(x)\) and \(\tau_\varphi(a^*a)=0\), then \(x\in J_\omega(M)\) and \(a=0\).

We now prove that this quotient is a von Neumann algebra; no von Neumann closure is being silently appended. Every contraction of \(A\) has a contraction representative: for an arbitrary representative \(a\), use \(a f(a^*a)\), where the continuous function \(f\) is \(1\) on \([0,1]\) and \(s^{-1/2}\) on \([1,\infty)\). Functional calculus in the quotient shows that its class is unchanged.

The unit ball of \(A\) is complete for \(\|X\|_{2,\tau_\varphi}=\tau_\varphi(X^*X)^{1/2}\). To prove this, pass from any Cauchy sequence to a subsequence \(X_r\) with
\[
\|X_r-X_p\|_{2,\tau_\varphi}<2^{-p}\qquad(r>p),
\]
and choose contraction representatives \(x_r(n)\). Choose a norm-dense sequence \((\rho_j)\) in the unit ball of \(M_*\). There are nested sets \(A_r\in\omega\), with \(A_r\subseteq\{n\ge r\}\), on which
\[
\begin{aligned}
&\|[x_r(n),\rho_j]\|\le1/r \quad(j\le r),\\
&\|x_r(n)-x_p(n)\|_{\varphi,\#}\\
&\le2^{-p}+2^{-r} \quad(p<r).
\end{aligned}
\]
For each \(r\) these are finitely many ultrafilter-large conditions; the second line follows from the preceding sharp-norm identity applied to \(x_r-x_p\). Intersect them with \(A_{r-1}\) and \(\{n\ge r\}\). Freeness makes the latter set available.

For each \(n\), let \(r(n)\) be the largest \(r\le n\) with \(n\in A_r\), or zero if there is none; set \(x_0(n)=0\) and \(x(n)=x_{r(n)}(n)\). For every fixed \(r\), \(r(n)\ge r\) on \(A_r\), so \(r(n)\to_\omega\infty\). The first line of the conditions gives predual centrality on each \(\rho_j\); the uniform commutator bound and norm density give it on every \(\rho\in M_*\). Thus \(x\in C_\omega(M)\). For fixed \(p\), on the set where \(r(n)>p\), the second line gives
\[
\|x(n)-x_p(n)\|_{\varphi,\#}
\le2^{-p}+2^{-r(n)}.
\]
Taking ultralimits yields
\(\|\pi(x)-X_p\|_{2,\tau_\varphi}\le2^{-p}\).
The selected subsequence, and hence the original Cauchy sequence, converges in the quotient unit ball.

Represent \(A\) by left multiplication on the completion of its trace inner-product space, with reference vector \(\Omega=1\). The representation is faithful because \(\tau_\varphi\) is faithful. Right multiplication is bounded, commutes with the left action, and has cyclic vector \(\Omega\); therefore \(\Omega\) separates the left algebra. On a uniformly bounded subset of \(A\), convergence in \(2\)-norm is equivalent to strong operator convergence in this representation. One direction tests on \(\Omega\); for the other use
\[
\begin{aligned}
&\|(X_i-X)Y\|_{2,\tau_\varphi}\\
&\le\|Y\|\,\|X_i-X\|_{2,\tau_\varphi}
\quad(Y\in A)
\end{aligned}
\]
and density of the vectors \(Y\Omega\).

Kaplansky density makes the represented unit ball strongly dense in the unit ball of its bicommutant. A bounded net converging strongly to a bicommutant element is \(2\)-norm Cauchy, by testing on \(\Omega\). The metric completeness just proved also gives convergence of Cauchy nets: choose successively indices beyond which the pairwise distances are \(<2^{-k}\), use the resulting Cauchy sequence, and then its metric limit. Its limit \(X\) lies in the quotient unit ball. The preceding bounded-topology equivalence identifies the original strong limit with the represented \(X\). Thus the quotient already equals its bicommutant. Its trace is the vector functional of \(\Omega\), hence is normal; it is faithful and tracial as proved above. This constructs the finite von Neumann algebra \(M_\omega=A\) at nonfactor scope.

The quotient \(C_\omega(M)/J_\omega(M)\) is independent of the auxiliary faithful state because both its algebra and its strong-star null ideal were defined intrinsically. Normality assertions also hold at the required scope. For \(\theta\in\operatorname{Aut}(M)\),
\[
[\theta(x),\rho]=[x,\rho\circ\theta]\circ\theta^{-1}
\]
preserves \(C_\omega(M)\). The faithful-state tests, or their full family of positive normal functionals, show that a normal automorphism preserves bounded strong-star convergence, so it preserves \(J_\omega(M)\). It induces a *-automorphism \(\theta_\omega\) of the quotient. This map and its inverse preserve positive order and therefore every bounded increasing positive supremum. Composing with a positive predual functional gives an order-normal positive functional. TP1 of the tracial-normality companion makes it ultraweakly continuous; positive spanning of the predual gives the same for all normal tests. Thus \(\theta_\omega\) is normal. The same argument shows that different faithful-state GNS realizations of this same quotient are normally isomorphic by their specified identity map.

For a nonfactor, \(\theta_\omega\) need not preserve the particular auxiliary trace \(\tau_\varphi\), and no such assertion is needed. For example, on \(M=\mathbb C\oplus\mathbb C\) the coordinate swap does not preserve the state \(\varphi(a,b)=a/3+2b/3\). The algebra, null ideal, normal quotient automorphism, and the amplification map below remain well-defined.

**Proposition 3.1.** For a von Neumann algebra \(N\) with separable predual, the canonical map
\[
\begin{gathered}
j_\omega:N_\omega\longrightarrow
(N\overline\otimes B)_\omega,\\
[(x_n)]\longmapsto[(x_n\otimes1)].
\end{gathered}
\tag{3.1}
\]
is an isomorphism for every free ultrafilter. It intertwines \(\theta_\omega\) with \((\theta\otimes\mathrm{id}_B)_\omega\). In particular,
\[
\begin{gathered}
\theta\in\operatorname{Ct}(N)
\ \Longleftrightarrow\
\theta\otimes\mathrm{id}_B\in\operatorname{Ct}(N\overline\otimes B),\\
p_a(\theta\otimes\mathrm{id}_B)=p_a(\theta).
\end{gathered}
\tag{3.2}
\]

*Proof.* We give a matrix proof of the exact type-I statement. The general spectral-gap route in the earlier programme provider, Theorem 9.2 and Example 9.4, is an alternative construction source; the argument here only needs the type-I matrix units. The [tensor-foundation companion](../foundations/normal-tensor-and-tracial-product-foundations.md), TF1, supplies product normal functionals and their norm density. The quotient construction above supplies the full nonfactor interface. Its diagonal completeness method is the one in Central sequence algebras and exact lifts, Sections 1–3, with the general state-defined trace proved here in place of that provider’s factor-specific scalar limit.

First recall why predual centrality implies the operator commutators needed below. For a bounded element \(x\), a fixed \(a\) and a positive normal functional \(\psi\), put \(d=ax-xa\). With the bimodule convention \((x\psi)(b)=\psi(bx)\), expanding \(\psi(d^*d)\) gives
\[
\begin{aligned}
\psi(d^*d)
&=(x\psi)(d^*a)-(x(a\psi))(d^*).
\end{aligned}
\]
Move \(x\) through each fixed functional. The resulting terms \(\psi(xd^*a)\) cancel, so
\[
\begin{aligned}
&\psi([a,x]^*[a,x])\\
&\leq2\|a\|\|x\|\bigl(\|a\|\|[x,\psi]\|\\
&\hspace{20mm}+\|[x,a\psi]\|\bigr).
\end{aligned}
\]
Applying the same inequality to \(a^*,x^*\), and using \([x^*,\eta]^*=-[x,\eta^*]\), bounds the other squared seminorm by
\(2\|a\|\|x\|(\|a\|\|[x,\psi]\|+\|[x,\psi a]\|)\).
Thus a bounded predual-central family commutes strongly-star with every fixed operator, along the same filter. This is the cancellation proof in the earlier programme Theorem 7.1; it requires no factor or trace assumption. [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md), Section 3A, identifies these bounded tests with strong-star convergence.

The zero algebra is immediate; suppose \(N\ne0\). Represent \(N\) faithfully and normally on a Hilbert space \(H\), and write \(P=N\overline\otimes B\) on \(H\otimes\ell^2(\mathbb N)\). TF1 product-functional density and the countable matrix normal-functional tests on \(B\) show that \(P\) also has separable predual. Thus the general quotient construction above applies to both algebras. Choose a faithful normal state \(\varphi\) of \(N\) and positive numbers \(t_j\) with \(\sum_jt_j=1\). The normal product state
\(\Phi=\varphi\otimes\sum_jt_j\omega_{e_j,e_j}\) is faithful: for \(X\geq0\), \(\Phi(X)=0\) forces every positive diagonal entry \(X_{jj}\) to vanish by faithfulness of \(\varphi\); then \(X^{1/2}(h\otimes e_j)=0\) for every \(h,j\), so \(X=0\).

For any centralizing bounded sequence \((y_n)\) in \(N\),
\[
[y_n\otimes1,\rho\otimes\eta]
=[y_n,\rho]\otimes\eta.
\]
TF1 and the uniform commutator bound extend this convergence from product tests to all of \(P_*\). Also
\(\|y_n\otimes1\|_\Phi^\sharp=\|y_n\|_\varphi^\sharp\).
Consequently the prescribed map \(j_\omega\) is a well-defined injective unital *-homomorphism of the centralizer quotients.

For surjectivity, let \((X_n)\) be a bounded predual-central sequence in \(P\), with all limits now taken along \(\omega\). Write \(E_{ij}=1\otimes e_{ij}\), and let
\(y_n=(\operatorname{id}\otimes\omega_{e_1,e_1})(X_n)\in N\).
This slice exists and has norm at most \(\|X_n\|\), by TF1's slice construction. Write \(X_{n,ij}\) for all the matrix entries. The operator commutator conclusion above gives
\[
\begin{aligned}
&[X_n,E_{jj}]E_{jj}\\
&=X_nE_{jj}-E_{jj}X_nE_{jj}\longrightarrow0,\\
&E_{jj}[X_n,E_{j1}]E_{11}\\
&=(X_{n,jj}-y_n)\otimes e_{j1}\longrightarrow0.
\end{aligned}
\]
strongly-star, for each fixed \(j\). Hence
\((X_n-y_n\otimes1)(h\otimes e_j)\to0\) for every \(h,j\). Apply the same argument to \(X_n^*\) for the adjoint limit. Finite-support vectors are dense, and \(\|X_n-y_n\otimes1\|\leq2\sup_n\|X_n\|\), so these two limits hold on every vector. This proves
\[
\begin{gathered}
X_n-y_n\otimes1\longrightarrow0\\
\text{strongly-star along }\omega.
\end{gathered}
\]
This density argument uses only finitely many filter conditions for each prescribed error; it does not require a countable basis of \(H\).

For \(a\in N\), evaluating \([X_n,\rho\otimes\omega_{e_1,e_1}]\) at \(a\otimes e_{11}\) gives \(y_n,\rho\). Therefore
\[
\|[y_n,\rho]\|
\leq\|[X_n,\rho\otimes\omega_{e_1,e_1}]\|
\longrightarrow0.
\]
Thus \((y_n)\) is centralizing in \(N\), and its image represents the class of \((X_n)\). This proves surjectivity. The inverse as well as \(j_\omega\) is normal: a bijective *-homomorphism preserves positive order and hence every bounded increasing positive supremum in both directions. Apply TP1 of the tracial-normality companion to positive predual tests, and then their linear span, to obtain global ultraweak continuity. Equivariance follows immediately from the specified representatives \(y_n\otimes1\).

Finally, an automorphism of a separable-predual algebra is centrally trivial exactly when its induced automorphism on the asymptotic centralizer is the identity for every free ultrafilter. If an ultrafilter-central sequence is displaced, select increasing coordinates meeting successively the first \(k\) tests from a norm-dense predual sequence and the faithful-state displacement bound. The resulting ordinary central sequence is still displaced. Conversely, from a displaced ordinary central sequence select a subsequence with displacement bounded below and take a free ultrafilter on that subsequence. The faithful-state criterion of Section 3A justifies both tests. Equivariance and surjectivity of \(j_\omega\) therefore give the first line of (3.2); applying it to every power gives the second. \(\square\)

There is also an explicit absorption formula which does not use central sequences.

**Lemma 3.2.** Let \(N\) be a properly infinite factor with separable predual, and let \(\beta\in\operatorname{Aut}(N)\). Then \(\beta\otimes\mathrm{id}_B\) is outer conjugate to \(\beta\).

*Proof.* Choose isometries \(s_i\in N\) with
\[
s_i^*s_j=\delta_{ij}1,\qquad
\sum_i s_is_i^*=1
\tag{3.3}
\]
strongly. Proper infiniteness and countable decomposability supply this decomposition. Define
\[
\begin{gathered}
\Pi:N\overline\otimes B\longrightarrow N,\\
\Pi(x\otimes e_{ij})=s_ixs_j^*,\\
V=\sum_i s_i\beta(s_i^*).
\end{gathered}
\tag{3.4}
\]
The inverse of \(\Pi\) has matrix entries \(s_i^*ys_j\). Thus \(\Pi\) is a normal isomorphism. The summands defining \(V\) have mutually orthogonal initial projections \(\beta(s_is_i^*)\) and mutually orthogonal final projections \(s_is_i^*\), both summing to one. Their strong sum is unitary, and \(V\beta(s_i)=s_i\). Hence
\[
\Pi(\beta\otimes\mathrm{id}_B)\Pi^{-1}
=\operatorname{Ad}V\circ\beta.
\tag{3.5}
\]
The formula is first checked on \(x\otimes e_{ij}\) and then extended by normality. \(\square\)

## 4. Centrally trivial automorphisms of the semifinite factor

**Lemma 4.1.** Suppose \(N_1,N_2\) are factors and \(\alpha_1\otimes\alpha_2\) is inner on \(N_1\overline\otimes N_2\). Then each \(\alpha_i\) is inner.

*Proof.* Let the unitary \(W\) implement the tensor automorphism. Then
\[
W(x\otimes1)=(\alpha_1(x)\otimes1)W.
\tag{4.1}
\]
Choose a normal functional \(f\) on \(N_2\) such that \(b=(\mathrm{id}\otimes f)(W)\ne0\); normal slices separate points by TF1. Equation (4.1) gives \(bx=\alpha_1(x)b\). It follows that \(b^*b\in Z(N_1)\) and \(bb^*\in Z(N_1)\). Both are nonzero scalar multiples of the identity. Polar decomposition therefore makes \(b\) a nonzero scalar multiple of a unitary implementing \(\alpha_1\). Slice in the other direction to handle \(\alpha_2\). \(\square\)

**Theorem 4.2.** Under the tensor-absorption prerequisite,
\[
\operatorname{Ct}(R_\infty)=\operatorname{Inn}(R_\infty).
\tag{4.2}
\]

*Proof.* Inner automorphisms are centrally trivial. Conversely let \(\theta\in\operatorname{Ct}(R_\infty)\). The algebra \(R_\infty\) is strongly stable, since \(R\overline\otimes R\cong R\). Interleaving the finite matrix coordinates of the tracial product gives this specified normal isomorphism by TF2–TF3. Tensor absorption for the identity model gives an outer conjugacy between \(\theta\) and \(\theta\otimes\mathrm{id}_R\). Central triviality is invariant under isomorphism and inner perturbation, so
\[
\theta\otimes\mathrm{id}_R\in
\operatorname{Ct}(R_\infty\overline\otimes R).
\tag{4.3}
\]
Proposition 3.1, applied to this algebra, permits a further identity \(B\) leg. Regrouping \(R\overline\otimes B=R_\infty\) gives
\[
\Theta=\theta\otimes\mathrm{id}_{R_\infty}
\in\operatorname{Ct}(R_\infty\overline\otimes R_\infty).
\tag{4.4}
\]

The flip \(S(x\otimes y)=y\otimes x\) on this tensor square is approximately inner. To check this in the semifinite setting, regroup the algebra as
\[
(R\overline\otimes R)
\overline\otimes B(\ell^2\otimes\ell^2).
\tag{4.5}
\]
The flip on \(R\overline\otimes R\) is approximately inner: transport it through the specified TF3 interleaving isomorphism to an automorphism of \(R\), apply the finite-factor Theorem 6.3, and transport its inner approximants back. The Hilbert-space swap implements the flip on the two type-I legs exactly. Tensor the finite-factor inner approximants with this swap unitary. Convergence on product normal functionals extends by their norm density to convergence on the entire predual, proving the assertion.

Lemma 1.1 says that \(S\) and \(\Theta\) commute modulo inner automorphisms. Their commutator is
\[
S\Theta S^{-1}\Theta^{-1}
=\theta^{-1}\otimes\theta.
\tag{4.6}
\]
It is inner, so Lemma 4.1 makes \(\theta\) inner. \(\square\)

This argument uses both identity amplifications in (4.3)–(4.4). Approximate innerness of the flip alone does not replace the assertion that \(\Theta\) is centrally trivial.

## 5. Straightening a trace-preserving automorphism

Every automorphism \(\beta\) of \(R_\infty\) multiplies its n.s.f. trace by a unique scalar:
\[
\tau\circ\beta=\operatorname{mod}(\beta)\tau,
\qquad \operatorname{mod}(\beta)>0.
\tag{5.1}
\]
This follows from uniqueness, up to a positive scalar, of an n.s.f. trace on a semifinite factor. Composition multiplies these scalars. Inner automorphisms have multiplier one.

**Proposition 5.1.** If \(\eta\in\operatorname{Aut}(R_\infty)\) preserves \(\tau\), then \(\eta\) is approximately inner. More precisely, an inner perturbation is of the form
\(\delta\otimes\mathrm{id}_B\), where \(\delta\in\operatorname{Aut}(R)\). If \(p_a(\eta)=0\), then \(\eta\) is outer conjugate to
\[
A=\sigma_0\otimes\mathrm{id}_B
\quad\text{on }R\overline\otimes B.
\tag{5.2}
\]

*Proof.* Choose a projection \(p\) with \(\tau(p)=1\) and a complete system of matrix units \(e_{ij}\) with \(e_{11}=p\). Since \(\eta\) preserves trace, \(p\sim\eta(p)\). Their complements have infinite trace and are equivalent as well. Adding the two matching partial isometries gives a unitary \(u\) such that
\[
\eta'=\operatorname{Ad}u\circ\eta,
\qquad \eta'(p)=p.
\tag{5.3}
\]
The finite corner \(pR_\infty p\) is isomorphic to \(R\).

Define a second unitary by
\[
w=\sum_{i\ge1}e_{i1}\eta'(e_{1i}).
\tag{5.4}
\]
The \(i\)-th summand has initial projection \(\eta'(e_{ii})\) and final projection \(e_{ii}\). Orthogonality and the sums of these projections show that (5.4) converges strongly, with strongly convergent adjoints, to a unitary. Direct multiplication gives
\[
w\eta'(e_{ij})=e_{ij}w.
\tag{5.5}
\]
Therefore \(\eta''=\operatorname{Ad}w\circ\eta'\) fixes every matrix unit. In the identification
\[
R_\infty\cong(pR_\infty p)\overline\otimes B,
\tag{5.6}
\]
an automorphism fixing the matrix units acts on their coefficient algebra alone. Thus \(\eta''=\delta\otimes\mathrm{id}_B\), with \(\delta=\eta''|_{pR_\infty p}\).

Every automorphism of \(R\) is approximately inner. Tensoring its inner approximants with \(1_B\) and using density of product normal functionals makes \(\delta\otimes\mathrm{id}_B\) approximately inner. Undoing the inner perturbations gives the same conclusion for \(\eta\).

If \(p_a(\eta)=0\), inner invariance and Proposition 3.1 give \(p_a(\delta)=0\). The finite-factor aperiodic comparison theorem makes \(\delta\) outer conjugate to \(\sigma_0\). Tensor this outer conjugacy with the identity on \(B\), and undo (5.3)–(5.4), to obtain (5.2). \(\square\)

The proposition proves approximate innerness, not innerness. For example, \(A\) itself preserves trace and has outer period zero.

## 6. A multiplier different from one determines conjugacy

The [discrete trace-stability companion](../foundations/discrete-trace-stability-foundations.md), Theorem DS and Sections 2–8, supplies the complete discrete argument for the following statement. Its general extended-positive/spectral, tracial-density, modular-transfer and trace-existence imports W1–W3 and T1 are explicitly retained; the whole transitive graph is not certified closed. In particular this integer-action theorem is not obtained merely by renaming the real-action theorem in [Takesaki II, XII.1.11].

**Trace-scaling stability theorem.** Let \(Q\) be a semifinite von Neumann algebra with separable predual and faithful normal semifinite trace \(T\). If
\[
T\circ\alpha=\lambda T,\qquad
0<\lambda\ne1,
\tag{6.1}
\]
then for every \(c\in\mathcal U(Q)\) there is \(z\in\mathcal U(Q)\) with
\[
c=z^*\alpha(z).
\tag{6.2}
\]
Equivalently, every unitary cocycle for the integer action generated by \(\alpha\) is a coboundary. Consequently
\[
\operatorname{Ad}z\circ(\operatorname{Ad}c\circ\alpha)
\circ\operatorname{Ad}z^*
=\alpha.
\tag{6.3}
\]
This is trace-scaling cohomology, rather than central-sequence cohomology. The cocycle \(c\) need not be central. The integer-action theorem for \(0<\lambda<1\) also yields the case \(\lambda>1\): apply it to \(\alpha^{-1}\) and \(d=\alpha^{-1}(c^*)\). The equation \(d=z^*\alpha^{-1}(z)\), after applying \(\alpha\) and taking adjoints, gives (6.2).

**Theorem 6.1.** Assume the tensor-absorption and trace-scaling stability prerequisites. If \(\beta_1,\beta_2\in\operatorname{Aut}(R_\infty)\) and
\[
\operatorname{mod}(\beta_1)
=\operatorname{mod}(\beta_2)=\lambda\ne1,
\tag{6.4}
\]
then \(\beta_1\) and \(\beta_2\) are conjugate. Conversely, conjugate automorphisms have the same multiplier.

*Proof.* Every nonzero power of \(\beta_j\) has trace multiplier \(\lambda^k\ne1\), so it is outer. By Theorem 4.2 it is not centrally trivial either. Thus both outer and asymptotic periods are zero.

For \(i,j\in\{1,2\}\), consider
\[
T_{ij}=\beta_i\otimes\beta_j^{-1}
\quad\text{on }R_\infty\overline\otimes R_\infty.
\tag{6.5}
\]
This tensor square is isomorphic to \(R_\infty\): combine \(R\overline\otimes R\cong R\) with the type-I tensor identification. The product trace is scaled by \(\lambda\lambda^{-1}=1\). No nonzero power of \(T_{ij}\) is inner, by Lemma 4.1 and the outer powers of \(\beta_i\). Theorem 4.2 therefore gives \(p_a(T_{ij})=0\). Proposition 5.1 shows that every \(T_{ij}\) is outer conjugate to \(A\) from (5.2).

Write \(\sim_o\) for outer conjugacy. Tensor absorption and Lemma 3.2 show, for \(j=1,2\), that
\[
\begin{aligned}
\beta_j&\sim_o\beta_j\otimes\sigma_0\\
&\sim_o(\beta_j\otimes\sigma_0)\otimes\mathrm{id}_B\\
&=\beta_j\otimes A.
\end{aligned}
\tag{6.6}
\]
Outer conjugacy is preserved by tensoring with another automorphism, by permutations of tensor legs, and by association of tensor products. Therefore
\[
\begin{aligned}
\beta_2&\sim_o\beta_2\otimes A\\
&\sim_o\beta_2\otimes T_{12}\\
&\cong T_{22}\otimes\beta_1\\
&\sim_o A\otimes\beta_1\\
&\sim_o\beta_1.
\end{aligned}
\tag{6.7}
\]
The middle isomorphism only reorders the three legs
\(\beta_2,\beta_1,\beta_2^{-1}\).
This proves outer conjugacy without cancelling an automorphism from a tensor product.

Thus there are an isomorphism \(\Phi:R_\infty\to R_\infty\) and a unitary \(c\) such that
\[
\beta_2=\operatorname{Ad}c\circ\alpha,
\qquad \alpha=\Phi\beta_1\Phi^{-1}.
\tag{6.8}
\]
The multiplier of \(\alpha\) is still \(\lambda\): if \(\tau\circ\Phi=b\tau\), the scalars \(b\) and \(b^{-1}\) cancel in this conjugation. The stability theorem gives \(c=z^*\alpha(z)\). Equation (6.3) makes
\[
\beta_2=
(\operatorname{Ad}z^*\circ\Phi)\,
\beta_1\,
(\operatorname{Ad}z^*\circ\Phi)^{-1}.
\tag{6.9}
\]
This is conjugacy.

The same trace calculation shows directly that conjugacy preserves the multiplier, proving the converse. \(\square\)

The restriction \(\lambda\ne1\) has mathematical content. The identity and \(A=\sigma_0\otimes\mathrm{id}_B\) both have multiplier one. Their outer periods are \(1\) and \(0\), so they are not even outer conjugate.

## 7. A discrete trace-scaling model

Fix \(0<\lambda<1\), and consider
\[
\begin{aligned}
Q&=\ell^\infty(\mathbb Z)\overline\otimes M_d(\mathbb C),\\
T(x)&=\sum_{n\in\mathbb Z}\lambda^n\operatorname{Tr}(x(n)),\\
\alpha(x)(n)&=x(n-1).
\end{aligned}
\tag{7.1}
\]
Finite coordinate cutoffs show that \(T\) is semifinite, and scalar monotone convergence gives normality. Its positive coefficients give faithfulness. Reindexing the sum gives \(T\circ\alpha=\lambda T\).

For any unitary field \(c(n)\), set \(z(0)=1\) and solve recursively
\[
z(n-1)=z(n)c(n).
\tag{7.2}
\]
For positive \(n\), use \(z(n)=z(n-1)c(n)^*\); for negative \(n\), proceed downward from zero. Every value is unitary, so the field belongs to \(Q\). Equation (7.2) gives
\[
c(n)=z(n)^*z(n-1)
=(z^*\alpha(z))(n).
\tag{7.3}
\]
No values of the field need commute. This model makes the direction of the coboundary equation visible. The general trace-scaling stability theorem asserts such a solution even when there is no central coordinate decomposition of this form.

## 8. Exercises with complete solutions

**Exercise 8.1 (basic: trace transport).** Let \(\tau\circ\beta=\lambda\tau\) on a semifinite factor, and let \(\tau\circ\Phi=b\tau\). Compute the multiplier of \(\Phi\beta\Phi^{-1}\). If \(\lambda=1/3\) and \(\tau(p)=2\), compute \(\tau(\beta^{-2}(p))\).

*Solution.* We have
\[
\tau\circ\Phi\beta\Phi^{-1}
=b\lambda\,\tau\circ\Phi^{-1}
=\lambda\tau.
\]
Also \(\tau\circ\beta^{-2}=\lambda^{-2}\tau=9\tau\), so the requested value is \(18\). No finiteness of the identity is used.

**Exercise 8.2 (intermediate: why the increment is normal).** For unitaries \(v,t\), set \(B=t-v\) and \(A=v^*t-1\). Prove \(A^*A=AA^*=B^*B\). Then derive both equalities (1.9).

*Solution.* Put \(U=v^*t\). Since \(U\) is unitary,
\[
\begin{aligned}
A^*A=AA^*&=2-U-U^*\\
&=2-v^*t-t^*v=B^*B.
\end{aligned}
\]
For \(d=u^*A\theta(u)\), this gives
\[
dd^*=u^*B^*Bu,\qquad
d^*d=\theta(u)^*B^*B\theta(u).
\]
Applying \(\varphi\) gives \(\varphi\circ\operatorname{Ad}u^*\) on the first term. On the second it gives
\(\varphi\circ\theta\circ\operatorname{Ad}u^*\circ\theta^{-1}\).
These are the two moving states in (1.9). In particular, the calculation cannot replace both by \(\varphi\) unless additional invariance holds.

**Exercise 8.3 (intermediate: matrix straightening).** Suppose \(\eta'(e_{11})=e_{11}\). Verify the initial and final projections of \(a_i=e_{i1}\eta'(e_{1i})\), and prove (5.5).

*Solution.* The matrix-unit relations give
\[
\begin{aligned}
a_i^*a_i
&=\eta'(e_{i1})e_{11}\eta'(e_{1i})\\
&=\eta'(e_{ii}),\\
a_ia_i^*&=e_{ii}.
\end{aligned}
\]
The supports are orthogonal, so \(w=\sum_i a_i\) is unitary. Multiplication gives
\[
w\eta'(e_{ij})=e_{i1}\eta'(e_{1j})
=e_{ij}w.
\]
Thus conjugation by \(w\) makes every matrix unit fixed. The finite corner is preserved and supplies the coefficient automorphism \(\delta\); the type-I leg then carries the identity.

**Exercise 8.4 (advanced: a tensor commutator detects central triviality).** Explain why the witness in (2.4) can be used inside \(M\overline\otimes R\) even when \(M\) has no trace. Show that an inner automorphism of this tensor product cannot restrict to the identity on \(M\) and an outer automorphism on \(R\).

*Solution.* If \(x_n\) is a bounded strongly central sequence in \(R\), then \(1\otimes x_n\) commutes asymptotically in predual norm with every product normal functional. Such functionals have norm-dense linear span, and the commutator norm is uniformly bounded by \(2\sup_n\|x_n\|\) times the functional norm. The sequence is therefore strongly central in the tensor product.

For any faithful normal state \(\varphi\) on \(M\), its displacement in the seminorm from \(\varphi\otimes\tau_R\) equals the tracial displacement in \(R\). The tail entries from Section 2 retain a positive value there. Finally, Lemma 4.1, applied to the identity on \(M\) and the given outer automorphism on \(R\), excludes innerness of their tensor product. The argument uses factor slices, not a trace on \(M\).

**Exercise 8.5 (advanced: cocycle orientation and the unimodular boundary).** If \(c=z^*\alpha(z)\), verify (6.3) and give the conjugator in (6.9). Explain why the same coboundary theorem cannot hold for all trace-preserving automorphisms.

*Solution.* For \(x\in Q\), substitution gives
\[
\begin{aligned}
z c\,\alpha(z^*xz)c^*z^*
&=\alpha(z)\alpha(z^*)\alpha(x)\\
&\qquad{}\cdot\alpha(z)\alpha(z^*)\\
&=\alpha(x).
\end{aligned}
\]
Thus \(\operatorname{Ad}z\) conjugates \(\operatorname{Ad}c\circ\alpha\) to \(\alpha\). If \(\alpha=\Phi\beta_1\Phi^{-1}\), rearranging gives conjugator \(\operatorname{Ad}z^*\circ\Phi\) from \(\beta_1\) to \(\beta_2\).

For the identity automorphism of a finite factor, every expression \(z^*\alpha(z)\) equals \(1\). A scalar unitary \(c\ne1\) cannot be such a coboundary, though the trace is preserved. Even the classification conclusion fails at multiplier one: the identity and \(\sigma_0\otimes\mathrm{id}_B\) have different outer periods, as explained after Theorem 6.1.

## Construction and teaching organization

The commutator calculation uses the mechanism of [Connes, Lemma 2.2.2]; the two transported states are displayed separately to make its nontracial estimates checkable. The outer-centralizer argument uses [Takesaki III, XVII.2.11]. The semifinite innerness and multiplier classification use the actual proofs of XVII.3.11–3.12. Their matrix straightening and balanced tensor comparison are retained as credited mathematics. They are not newly independent discoveries.

The lesson organizes that material around specific interfaces: the transported-state estimate, a nontracial tensor witness, a full nonfactor quotient construction and type-I matrix proof, two identity amplifications, separate corner straightening, the discrete coboundary with its exact orientation, and a coordinate model. The five solved exercises check those interfaces and the multiplier-one failure; they do not reproduce the Borel-section, characteristic-invariant and crossed-product exercise sequence of [Takesaki III, Exercise XVII.3]. The earlier programme *Ultraproducts and the asymptotic centralizer*, written by Claude Opus 5.5 (Anthropic), Theorem 7.1, supplies the predual cancellation argument used in the new matrix proof. Its former spectral-gap route, Theorem 9.2 and Example 9.4, remains part of the construction history and is an alternative proof route.

This records the actual mathematical ancestry and the bounded comparison of exposition and teaching organization.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, series 4, 8 (1975), 383–419. [Open article](https://numdam.org/item/ASENS_1975_4_8_3_383_0/).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. [Open author version](https://arxiv.org/abs/1212.5457).

[Takesaki II] Masamichi Takesaki, *Theory of Operator Algebras II*, Encyclopaedia of Mathematical Sciences 125, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10451-4).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. XVII.2.11, printed pp. 268–269, and XVII.3.11–3.12, printed pp. 282–283. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The exact registered receipt-backed edition was used for the source and proof comparison; no book text is reproduced.
