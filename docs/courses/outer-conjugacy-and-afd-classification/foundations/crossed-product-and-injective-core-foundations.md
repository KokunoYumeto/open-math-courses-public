# Crossed-product recognition and injective cores

This companion supplies the bounded programme arguments used by [Permutation symmetry and Powers factors](../src/permutation-symmetry-and-powers-factors.md), Theorems 4.1 and 5.2 and Corollary 6.1. The proofs are adapted and expanded from two earlier CC0 programme lessons: *Full factors without almost periodic weights*, Lemma 8.1, and *Classification of injective factors*, Lemma 2.2(e,f), Propositions 3.1–3.2, Theorems 4.1 and 4.3, Corollary 4.2, Example 4.4, and Lemmas 8.1–8.2 and Theorem 8.3. Those lessons were written by Claude Opus 5.5 in September 2026. This independently written programme text is dedicated to CC0 1.0; external source texts retain their own terms.

We write \(R_\infty=R\overline\otimes B(\ell^2)\), where \(R\) is the tracial hyperfinite factor. This notation denotes the semifinite factor here. For an action \(\alpha\), our convention is \(U_gxU_g^*=\alpha_g(x)\). Every algebra and action in a displayed crossed product is normal in its von Neumann algebra variables.

<a id="pc0"></a>

## PC0. Exact imports and the boundary of this companion

The elementary arguments below still use the following named foundations.

1. **Bounded topology and faithful GNS representations.** Bounded density, weak compactness of operator balls, normality of faithful-state GNS representations, and the fact that a faithful normal representation has a von Neumann algebra as its image are supplied by [Bounded topology and tracial representations](../src/bounded-topology-and-tracial-representations.md), Section 3A and Theorem 3.1, and the [bounded-topology companion](bounded-topology-foundations.md). In particular, the GNS arguments below do not require a trace.
2. **Injectivity and commutants.** An algebra is injective exactly when, in a faithful normal representation, it is the image of a norm-one projection from the ambient \(B(H)\); this condition is independent of the representation. An algebra is injective if and only if its commutant is injective. A norm-one projection onto a unital C*-subalgebra is positive, unital, completely positive and bimodular. These are the representation-independent injectivity, commutant-duality and Tomiyama inputs. Takesaki III, XV.3.2(iii), supplies the commutant argument through standard form and amplification. Theorems PC9.1–PC9.2 below prove the full unital C*-algebra norm-one retraction statement and the representation-independent injectivity criterion. Amplifications and commutants, Proposition 1.1, Lemma 1.2 and Theorem 1.3, prove commutant duality in arbitrary faithful normal representations. Their standard-pair construction and bounded modular foundation BG-1–BG-6 remain explicit transitive inputs; PC3 alone does not supply that modular theorem.
3. **The finite classification input.** If a type \({\rm II}_1\) factor \(N\) with separable predual, acting on \(L^2(N,\tau)\), admits a state \(\chi\) on \(B(L^2(N,\tau))\) invariant under every \(\operatorname{Ad}u\), \(u\in\mathcal U(N)\), then \(N\cong R\). The state is not assumed normal. Theorem PC10.1 proves this invariant-state formulation: norm averaging identifies the restricted trace, finite densities and product-vector states produce matrix maps, and balanced reconstruction and unitary coupling produce actual finite-dimensional subalgebras. PC4 supplies the invariant state from injectivity. For an injective factor directly, [Unitary couplings and finite injective factors, Theorem 5.1](../../OA-APPROX/src/unitary-couplings-and-finite-injective-factors.md), gives the finite classification conclusion through matrix models, balanced couplings and finite-factor uniqueness. PC10 identifies the complete direct finite-model and uniqueness proofs used by this route, with their transitive scalar, trace, projection, ultrapower and tensor foundations stated explicitly.
4. **Finite corners and countable amplification.** A nonzero finite corner of a type \({\rm II}_\infty\) factor is of type \({\rm II}_1\). In separable-predual scope the unit is a countable sum of mutually orthogonal projections equivalent to a fixed nonzero finite projection. In a type \({\rm II}_1\) factor every nonzero corner is again of type \({\rm II}_1\). A subalgebra of a finite tracial algebra has a trace-preserving normal conditional expectation. These type, projection-comparison and tracial-expectation inputs are needed in PC4. The countable matrix isomorphism is written out there. [Unitary couplings and finite injective factors, Corollary 5.2](../../OA-APPROX/src/unitary-couplings-and-finite-injective-factors.md), gives the countable filling construction, including absorption of a residual subprojection.
5. **Discrete decomposition and trace scaling.** For a type \({\rm III}_\lambda\) factor \(M\) with separable predual and \(0<\lambda<1\), there are a type \({\rm II}_\infty\) factor \(N\), a faithful normal semifinite trace \(\tau\), and an automorphism \(\theta\), all with the same separable-predual scope, such that
   \[
   \begin{gathered}
   M\cong N\rtimes_\theta\mathbb Z,\\
   \tau\circ\theta=\lambda\tau.
   \end{gathered}
   \]
   [Discrete decomposition, DD-0–DD-5](../../OA-FLOW/OA-FLOW-DD.html#oa-flow.dd.0), proves existence with these hypotheses and conventions. It supplies the faithful normal period expectation, separable core, exact multiplier on the entire positive cone and onto regular representation. Its explicitly linked IP, PW, CA, PF and GT constructions and their modular and spectral foundations remain part of the transitive proof chain. DD is an existence theorem; PC6 supplies the additional classification reduction. The same-multiplier automorphism input is [Trace scaling on the hyperfinite semifinite factor](../src/trace-scaling-on-the-hyperfinite-semifinite-factor.md), Theorem 6.1, with that theorem's stated prerequisites. PC6 uses only its weaker outer-conjugacy consequence.

The Powers model's type calculation additionally uses the **factorial-centralizer spectral theorem**: for a factor \(M\) with a faithful normal state \(\varphi\) whose centralizer \(M_\varphi\) is a factor,
\[
S(M)=\operatorname{Sp}\Delta_\varphi.
\]
Here \(S(M)\) is the intersection of the modular spectra over all faithful normal semifinite weights on \(M\). Theorem PC8.1 below proves the full faithful normal semifinite weight formulation, including zero, using the fixed-algebra argument of PC7 and the exact earlier modular and action-spectrum results MG-0–MG-3 and CS-3. Their GNS, balanced-weight, normal-filter and spectral-calculus predecessors remain part of the transitive prerequisite chain. Connes's 1973 Corollary 3.2.7(a) is the classical human-source reference.

<a id="pc1"></a>

## PC1. The canonical coefficient expectation

Let \(Q\subset B(H)\) be a faithful normal representation and let a countable group \(G\) act on \(Q\) by normal automorphisms \(\alpha_g\). On \(\ell^2(G,H)\), set
\[
\begin{aligned}
(\pi(q)\xi)(s)&=\alpha_{s^{-1}}(q)\xi(s),\\
(U_g\xi)(s)&=\xi(g^{-1}s).
\end{aligned}
\]
Let \(A=Q\rtimes_\alpha G\) be generated by \(\pi(Q)\) and the \(U_g\). These formulas give the covariance relation and show that finite sums \(\sum_g\pi(q_g)U_g\) form a weakly dense unital *-algebra.

For \(s\in G\), write \(J_s:H\to\ell^2(G,H)\) for insertion in coordinate \(s\). Compression \(x\mapsto J_e^*xJ_e\) sends a finite Fourier sum to \(q_e\). Since \(Q\) is weakly closed, it sends every \(x\in A\) into \(Q\). Thus
\[
E(x)=\pi(J_e^*xJ_e),\qquad x\in A,
\]
is a normal unital completely positive map onto \(\pi(Q)\), fixes \(\pi(Q)\), and is bimodular. The last assertions also follow directly from the fact that \(\pi(q)\) is diagonal in these coordinates. In particular,
\[
E(\pi(q)U_g)=
\begin{cases}
\pi(q),&g=e,\\
0,&g\ne e.
\end{cases}
\]

The expectation is faithful. On Fourier sums, and then on \(A\) by normality, one has
\[
J_s^*xJ_s=\alpha_{s^{-1}}(J_e^*xJ_e).
\]
If \(x\ge0\) and \(E(x)=0\), every diagonal compression vanishes. Hence \(x^{1/2}J_s=0\) for every \(s\). The coordinate subspaces span a dense subspace, so \(x=0\).

For completeness, the whole coefficient family determines \(x\). On Fourier sums,
\[
J_s^*xJ_t
=\alpha_{s^{-1}}\!\left(
 J_e^*xU_{st^{-1}}^*J_e
\right).
\]
Both sides are normal linear functions of \(x\), so the formula holds for \(x\in A\). If all \(E(xU_g^*)\) vanish, all matrix entries vanish, and \(x=0\). No scalar-valued mean is used in place of this algebra-valued expectation.

<a id="pc2"></a>

## PC2. Recognition with prescribed generators

**Theorem PC2.1.** Let \(Q\subset B\) be a unital von Neumann subalgebra with a faithful normal state \(\chi\). Let \(g\mapsto v_g\) be a unitary representation of a countable group \(G\) in \(B\), normalizing \(Q\), and put \(\alpha_g=\operatorname{Ad}v_g|_Q\). Suppose that \(Q\) and the \(v_g\) generate \(B\), and that a faithful normal conditional expectation \(F:B\to Q\) satisfies \(F(v_g)=0\) for \(g\ne e\). There is a normal isomorphism
\[
B\longrightarrow Q\rtimes_\alpha G
\]
sending \(q\) to \(\pi(q)\) and \(v_g\) to \(U_g\).

*Proof.* Let \(B_0\) be the finite linear span of the \(qv_g\). The multiplication and adjoint rules are
\[
\begin{aligned}
(qv_g)(rv_h)&=q\alpha_g(r)v_{gh},\\
(qv_g)^*&=\alpha_{g^{-1}}(q^*)v_{g^{-1}}.
\end{aligned}
\]
Bimodularity gives
\[
F\!\left(\left(\sum_gq_gv_g\right)v_h^*\right)=q_h.
\]
Thus the coefficients of a finite sum are unique. The same holds in the regular crossed product by PC1. The prescribed generator map therefore gives a bijective *-homomorphism \(\Phi_0:B_0\to A_0\), where \(A_0\) is the finite Fourier algebra in the regular crossed product.

Put \(\psi=\chi\circ F\) and
\(\psi'=\chi\circ\pi^{-1}\circ E\). Both states are faithful and normal: for example, \(\chi(F(x))=0\) with \(x\ge0\) forces \(F(x)=0\), and then \(x=0\). For \(x=\sum_gq_gv_g\) and \(y=\sum_gr_gv_g\),
\[
\begin{aligned}
\psi(y^*x)
 &=\sum_g\chi\!\left(\alpha_{g^{-1}}(r_g^*q_g)\right)\\
 &=\psi'\!\left(\Phi_0(y)^*\Phi_0(x)\right).
\end{aligned}
\]
The map \(x\xi_\psi\mapsto\Phi_0(x)\xi_{\psi'}\) is consequently an isometry. Bounded density makes its domain and range dense in the respective GNS Hilbert spaces, so it extends to an onto unitary \(W\). On the dense set \(B_0\xi_\psi\),
\[
Wxy\xi_\psi
=\Phi_0(xy)\xi_{\psi'}
=\Phi_0(x)Wy\xi_\psi.
\]
Hence \(W\pi_\psi(x)W^*=\pi_{\psi'}(\Phi_0(x))\) for \(x\in B_0\). The faithful normal GNS representations and the von Neumann-image result in PC0 identify their weak closures with \(B\) and \(A\). Conjugation by \(W\) is normal and carries one closure onto the other. It gives the asserted normal isomorphism. \(\square\)

Applied to the Powers lesson, the exact data are \(B=R_\lambda\), \(Q=D\), \(\chi=\omega|_D\), \(F=E_D\), and \(v_g=u_g\) for the finite coordinate flips. The group is countable; the diagonal state is faithful and normal; and the lesson proves every other hypothesis, including \(E_D(u_g)=0\). The ambient state need not be tracial.

<a id="pc3"></a>

## PC3. From finite-dimensional approximation to injectivity

An algebra \(M\subset B(H)\) is AFD here if it has an increasing sequence \(G_n\) of unital finite-dimensional *-subalgebras with weakly dense union. For \(T\in B(H)\), let \(K_T\) be the ultraweakly closed convex hull of
\(\{uTu^*:u\in\mathcal U(M)\}\). It is an ultraweakly compact subset of the operator ball of radius \(\|T\|\). On bounded sets this is also the weak operator closure.

**Proposition PC3.1.** If \(M\) is AFD, then \(K_T\cap M'\ne\varnothing\) for every \(T\in B(H)\).

*Proof.* Haar averaging over the compact group \(\mathcal U(G_n)\) gives
\[
S_n=\int_{\mathcal U(G_n)}uTu^*\,du\in G_n'.
\]
This is a weak integral, has norm at most \(\|T\|\), and belongs to \(K_T\). To see the last assertion, a separating ultraweakly continuous real functional, if one existed, would take at the integral the average of its values on the orbit, contradicting separation from the closed convex hull. A subnet converges ultraweakly to some \(S\in K_T\). For each fixed \(n\), its tail commutes with \(G_n\); therefore \(S\) commutes with every \(G_n\), and hence with \(M\). \(\square\)

**Proposition PC3.2.** If \(K_T\cap M'\ne\varnothing\) for every \(T\), there is a linear norm-one projection \(P:B(H)\to M'\). Consequently \(M'\) and \(M\) are injective under the injectivity and commutant inputs of PC0.

*Proof.* Let \(\mathcal C_0\) be the finite convex combinations of the maps \(\operatorname{Ad}u\), \(u\in\mathcal U(M)\), and let \(\mathcal C\) be their closure in the compact product \(\prod_{T\in B(H)}K_T\). A point of this product is a map on \(B(H)\); the topology is pointwise ultraweak convergence. The linear identities and norm bounds survive this convergence. Every \(\Phi\in\mathcal C\) is therefore linear and contractive, and fixes \(M'\).

If \(\Psi\in\mathcal C_0\) and \(\Phi\in\mathcal C\), then \(\Psi\circ\Phi\in\mathcal C\). Indeed, approximate \(\Phi\) by a net from \(\mathcal C_0\), use the normality of \(\Psi\), and note that compositions of finite convex combinations of inner conjugations are again such combinations.

For a finite list \(T_1,\ldots,T_k\), we construct a map in \(\mathcal C\) sending each \(T_j\) into \(M'\). Begin with the identity map. If \(\Phi\) already does so for the first \(k-1\) elements, the assumed intersection property applied to \(\Phi(T_k)\) gives a net \(\Psi_i\in\mathcal C_0\) for which \(\Psi_i(\Phi(T_k))\) converges ultraweakly to a member of \(M'\). A cluster point of \(\Psi_i\circ\Phi\) in \(\mathcal C\) has the desired property for all \(k\) elements; the first \(k-1\) images remain fixed throughout.

The closed subsets
\[
\{\Phi\in\mathcal C:\Phi(T)\in M'\},\qquad T\in B(H),
\]
thus have the finite intersection property. Compactness gives \(P\) in their common intersection. It is contractive, maps into \(M'\), and fixes \(M'\), so \(P^2=P\) and \(\|P\|=1\). Apply Corollary PC9.2 and the exact commutant theorem identified in PC0. The projection need not be normal; no such assertion is needed. \(\square\)

<a id="pc4"></a>

## PC4. Corners and the semifinite core

**Lemma PC4.1.** If \(M\) is injective, then every nonzero corner \(eMe\) is injective. If \(F:M\to N\) is a conditional expectation onto a unital von Neumann subalgebra, then \(N\) is injective.

*Proof.* Represent \(M\) faithfully and normally on \(H\), and choose a norm-one projection \(P:B(H)\to M\). By Theorem PC9.1,
\[
P(eTe)=eP(T)e.
\]
Thus restriction to \(B(eH)=eB(H)e\) is a norm-one projection onto \(eMe\). For the second assertion, \(F\circ P:B(H)\to N\) is contractive and fixes \(N\), hence is a norm-one projection. Use the representation-independent injectivity criterion. \(\square\)

**Theorem PC4.2.** An injective type \({\rm II}_1\) factor with separable predual is isomorphic to \(R\). Conversely, \(R\) is injective.

*Proof.* The converse follows from the matrix filtration of \(R\) and PC3. For the forward implication, represent \(N\) on \(L^2(N,\tau)\) and let \(P:B(L^2(N,\tau))\to N\) be a norm-one projection. The state \(\chi=\tau\circ P\) obeys
\[
\begin{aligned}
\chi(uTu^*)
 &=\tau(uP(T)u^*)\\
 &=\tau(P(T))=\chi(T)
\end{aligned}
\]
for \(u\in\mathcal U(N)\). Theorem PC10.1 applies. No normality of \(\chi\) is asserted. \(\square\)

**Theorem PC4.3.** Under PC0's projection and finite classification inputs, an injective type \({\rm II}_\infty\) factor \(N\) with separable predual is isomorphic to \(R_\infty\). Conversely, \(R_\infty\) is AFD and injective.

*Proof.* Choose a nonzero finite projection \(e\in N\). Its corner is an injective type \({\rm II}_1\) factor by PC4.1 and the type input, and has separable predual. Hence \(eNe\cong R\) by PC4.2.

Here is the exact use of countable projection comparison. Choose mutually orthogonal \(e_i\) summing strongly to \(1\) and partial isometries \(w_i\in N\) with
\[
w_i^*w_i=e,\qquad w_iw_i^*=e_i.
\]
The map
\[
\begin{gathered}
V:\ell^2(\mathbb N)\otimes eH\longrightarrow H,\\
V(\delta_i\otimes\xi)=w_i\xi
\end{gathered}
\]
is an onto unitary. The \(i,j\) matrix entry of \(V^*xV\) is \(w_i^*xw_j\in eNe\). Conversely \(V(E_{ij}\otimes a)V^*=w_i a w_j^*\in N\) for \(a\in eNe\). Finite matrix compressions converge strongly on both sides, so these inclusions extend to
\[
V^*NV=B(\ell^2)\overline\otimes eNe.
\]
This is a normal isomorphism, and the tensor flip followed by \(eNe\cong R\) identifies \(N\) with \(R_\infty\).

For the converse, let \(A_n\subset R\) be its unital matrix filtration and \(p_n\) the projection onto the first \(n\) basis vectors of \(\ell^2\). The increasing unital finite-dimensional algebras
\[
A_n\otimes
\bigl(p_nB(\ell^2)p_n+\mathbb C(1-p_n)\bigr)
\]
have weakly dense union in \(R_\infty\): they contain every fixed matrix entry tensored with the eventually dense union of the \(A_n\). Thus \(R_\infty\) is AFD, and PC3 makes it injective. \(\square\)

Further finite consequences follow from the same inputs. If \(Q\subset R\) is a factor with unit \(1\), the trace-preserving expectation makes \(Q\) injective by PC4.1. Its restricted trace is faithful and normal, and its predual is a quotient of \(R_*\), hence separable. The finite type dichotomy and PC4.2 give \(Q\cong M_n\) or \(Q\cong R\). For unit \(p\ne1\), first apply PC4.1 and PC4.2 to the type \({\rm II}_1\) corner \(pRp\), and then argue inside that corner. In particular every nonzero \(pRp\) is isomorphic to \(R\).

Likewise \(R\overline\otimes R\) and \(R\overline\otimes M_n\) are AFD type \({\rm II}_1\) factors and hence isomorphic to \(R\). Use the product filtrations and faithful product traces. To check factoriality of a tensor product \(A\overline\otimes B\) of factors, let \(z\) be central. For every normal functional \(\eta\) on \(B\), the slice \((\operatorname{id}\otimes\eta)(z)\) is central in \(A\), hence scalar. Fixing a normal state \(\rho\) on \(A\) and putting \(b=(\rho\otimes\operatorname{id})(z)\), every such slice of \(z-1\otimes b\) vanishes. Product normal functionals separate the tensor product, so \(z=1\otimes b\). Centrality now gives \(b\in Z(B)=\mathbb C1\). Both tensor products under consideration are infinite dimensional and have faithful tracial states, so the finite-factor type dichotomy gives type \({\rm II}_1\).

Tensoring the first isomorphism with \(B(\ell^2)\), and using the normal tensor flip, gives \(R_\infty\overline\otimes R\cong R_\infty\). The normal product, slice, density and flip constructions are supplied by TF1 and TF3 of the [tensor companion](normal-tensor-and-tracial-product-foundations.md). These are existence statements; no canonical choice of isomorphism is asserted.

<a id="pc5"></a>

## PC5. Changing a crossed-product presentation

**Lemma PC5.1.** Let \(N\) have separable predual and let \(\theta_1\in\operatorname{Aut}(N)\).

(a) If \(\beta:N\to N_1\) is a normal isomorphism, there is a normal isomorphism
\[
N\rtimes_{\theta_1}\mathbb Z
\longrightarrow
N_1\rtimes_{\beta\theta_1\beta^{-1}}\mathbb Z
\]
sending \(x\) to \(\beta(x)\) and the generating unitary to the generating unitary.

(b) If \(\theta_2=\operatorname{Ad}u\circ\theta_1\), with \(u\in\mathcal U(N)\), then the crossed products by \(\theta_1\) and \(\theta_2\) are normally isomorphic. Consequently outer conjugate automorphisms give isomorphic crossed products.

*Proof.* For (a), view the second algebra as generated by the copy \(\beta(N)\) and its implementing unitary. Pull its coefficient algebra and faithful normal state back by \(\beta\). PC1 gives the faithful normal expectation and vanishing nonzero coefficients, so PC2 identifies this presentation with the first algebra, with the stated generator images.

For (b), work in \(B=N\rtimes_{\theta_1}\mathbb Z\), and write \(U\) for its unitary and \(F\) for its canonical expectation. Set \(V=uU\). Then
\[
VxV^*=u\theta_1(x)u^*=\theta_2(x).
\]
Also \(N\) and \(V\) generate \(B\), because \(U=u^*V\). For \(n\ge1\), induction gives
\[
\begin{aligned}
c_n&=u\theta_1(u)\cdots\theta_1^{n-1}(u),\\
V^n&=c_nU^n,\\
V^{-n}&=\theta_1^{-n}(c_n^*)U^{-n}.
\end{aligned}
\]
Thus \(F(V^m)=0\) for every nonzero integer \(m\). The assignment \(m\mapsto V^m\) is an exact unitary representation of \(\mathbb Z\), and \(N\) has a faithful normal state because its predual is separable. PC2 therefore gives a normal isomorphism from \(B\) to \(N\rtimes_{\theta_2}\mathbb Z\), sending \(x\) to \(x\) and \(V\) to the new unitary \(U_2\). Equivalently it sends \(U\) to \(u^*U_2\). Combine this with (a) for outer conjugacy. \(\square\)

**Lemma PC5.2.** If \(N\rtimes_\alpha G\) is injective, where \(G\) is countable and acts normally on \(N\), then \(N\) is injective.

*Proof.* Its canonical faithful normal expectation is supplied by PC1. Apply PC4.1 to that expectation and then identify \(\pi(N)\) with \(N\). \(\square\)

<a id="pc6"></a>

## PC6. The uniqueness reduction with the same parameter

**Lemma PC6.0 (trace normalization).** On any semifinite factor \(N\), two faithful normal semifinite traces differ by one strictly positive finite scalar.

*Proof.* Let the traces be \(\tau_1,\tau_2\). Semifiniteness and faithfulness of \(\tau_1\) give a nonzero positive element of finite trace. A nonzero spectral cut at a positive threshold is a projection \(e\) with \(0<\tau_1(e)<\infty\). Semifiniteness of \(\tau_2\) gives \(0\ne y\le e\) with \(\tau_2(y)<\infty\). Choose a positive threshold \(\varepsilon\) for which \(f=1_{[\varepsilon,\infty)}(y)\ne0\). Then
\[
\begin{aligned}
0<\tau_1(f)&\le\tau_1(e)<\infty,\\
0<\tau_2(f)&\le\varepsilon^{-1}\tau_2(y)<\infty.
\end{aligned}
\]
The spectral cuts and their order bounds are supplied by [S1 of the trace companion](trace-existence-foundations.md#s1-all-bounded-spectral-cuts-used-here). The corner \(fNf\) is finite: an isometry onto a proper subprojection of \(f\) would contradict finiteness and faithfulness of \(\tau_1(f)\). Its center is scalar by the corner-center theorem PC-4 in that companion. The restrictions
\[
\tau_1|_{fNf}/\tau_1(f),\qquad
\tau_2|_{fNf}/\tau_2(f)
\]
are therefore normalized normal traces on a finite factor, and [FCT7](trace-existence-foundations.md#fct-7) makes them equal. Put \(c=\tau_1(f)/\tau_2(f)\). The normal traces \(\tau_1\) and \(c\tau_2\) agree on the entire positive cone of \(fNf\), including its bounded positive elements. The central support of the nonzero projection \(f\) is \(1\), since \(N\) is a factor. Uniqueness in the full [corner-extension theorem GS1](trace-existence-foundations.md#gs1) consequently gives \(\tau_1=c\tau_2\) on all of \(N_+\), including infinite values. \(\square\)

In particular, the lemma applies to a type \({\rm II}_\infty\) factor. Thus \(\tau\circ\theta=c\tau\) defines a number \(c>0\) independent of the trace normalization. Under a normal isomorphism \(\beta:N\to N_1\), the transported trace \(\tau_1=\tau\circ\beta^{-1}\) satisfies
\[
\tau_1\circ(\beta\theta\beta^{-1})=c\tau_1.
\]
Since inner automorphisms preserve a trace, they preserve \(c\). This is why both changes of presentation in PC5 preserve the relevant multiplier.

**Theorem PC6.1.** Fix \(0<\lambda<1\). Under the exact imports in PC0 and the modular foundations of PC8, every injective factor of type \({\rm III}_\lambda\) with separable predual is isomorphic to the Powers factor \(R_\lambda\). In particular this holds for every AFD factor of that type with separable predual.

*Proof.* Let \(M\) be an injective factor with these hypotheses. Apply discrete decomposition with the convention
\[
\begin{gathered}
M\cong N\rtimes_\theta\mathbb Z,\\
\tau\circ\theta=\lambda\tau.
\end{gathered}
\]
The expected core \(N\) is injective by PC5.2. PC4.3 gives a normal isomorphism \(\beta:N\to R_\infty\). PC5.1(a) then gives
\[
M\cong R_\infty\rtimes_{\theta_1}\mathbb Z,
\qquad
\theta_1=\beta\theta\beta^{-1}.
\]
The trace multiplier of \(\theta_1\) is exactly \(\lambda\), by the transport computation above.

The Powers lesson proves that its model \(R_\lambda\), with density
\[
\operatorname{diag}\!\left(
\frac1{1+\lambda},\frac{\lambda}{1+\lambda}
\right),
\]
has separable predual and an increasing dense matrix filtration. PC3 makes it injective. Its Theorem 4.1 gives type \({\rm III}_\lambda\) using the factorial-centralizer spectral theorem proved in PC8. Applying the same decomposition and core argument to this model gives
\[
R_\lambda\cong R_\infty\rtimes_{\theta_2}\mathbb Z
\]
with multiplier \(\lambda\) again. The same-multiplier theorem in the trace-scaling lesson makes \(\theta_1\) and \(\theta_2\) outer conjugate. PC5.1(b) now supplies a normal isomorphism \(M\cong R_\lambda\). Finally PC3 makes every AFD \(M\) injective, so the final assertion follows. \(\square\)

The conclusion applies to injective factors as well as AFD factors. It does not extend the discrete-decomposition assertion to \(\lambda=1\). The separate equal-probability endpoint \(\lambda=1\) remains the type \({\rm II}_1\) conclusion and full solution in Exercise 7.6 of the Powers lesson.

<a id="pc7"></a>

## PC7. A factorial fixed algebra retains every action frequency

Let \(M\ne0\) be a von Neumann algebra and let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be a group of normal automorphisms continuous on every normal scalar coefficient. Write \(F=M^\alpha\). For \(f\in L^1(\mathbb R)\), use the normal weak-star filter and the Fourier convention
\[
\begin{aligned}
T_f(x)&=\int_{\mathbb R}f(t)\alpha_t(x)\,dt,\\
\widehat f(r)&=\int_{\mathbb R}f(t)e^{itr}\,dt.
\end{aligned}
\]
[CS-0](../../OA-FLOW/OA-FLOW-CS.html#oa-flow.cs.0), with its AL-1 integral construction, defines the action spectrum as
\[
\operatorname{Sp}(\alpha)
=\bigcap_{T_f=0\text{ on }M}\{r:\widehat f(r)=0\}.
\]
For a nonzero fixed projection \(e\), the restricted action \(\alpha^e\) acts on \(eMe\) with unit \(e\). Its filters are the restrictions of \(T_f\): testing every normal coefficient verifies the integral identity. Normal left and right multiplication by elements \(a,b\in F\) also pass through that integral, so
\[
T_f(axb)=aT_f(x)b.
\tag{PC7.1}
\]
The Connes spectrum is the fixed-corner intersection
\[
\Gamma(\alpha)
=\bigcap_{0\ne e\in\operatorname{Proj}(F)}
       \operatorname{Sp}(\alpha^e).
\]

**Lemma PC7.1.** If \(F\) is a factor, then for every nonzero projection \(e\in F\),
\[
\operatorname{Sp}(\alpha^e)
=\operatorname{Sp}(\alpha)=\Gamma(\alpha).
\tag{PC7.2}
\]
Neither \(M\) nor its representation is assumed countably decomposable. No trace, state, period or eigenvector decomposition is required.

*Proof.* Work first inside the factor \(F\), in any faithful normal concrete representation. Choose a maximal family \((w_i)_{i\in I}\) of nonzero partial isometries in \(F\) whose initial projections satisfy \(w_i^*w_i\le e\) and whose final projections \(q_i=w_iw_i^*\) are mutually orthogonal. Zorn's lemma applies because a union of a chain of such families still has the stated properties. The initial projections need not be mutually orthogonal, and the index set need not be countable.

The arbitrary projection join \(q=\sum_i q_i\) belongs to \(F\). If \(r=1-q\ne0\), the two nonzero projections \(r,e\) have central support one in \(F\). [The central-support criterion PC-2](trace-existence-foundations.md#pc-2) therefore gives \(rFe\ne\{0\}\). The polar partial isometry of a nonzero element of \(rFe\), supplied by PC-1 there, has initial projection below \(e\) and nonzero final projection below \(r\). It could be added to the family, contradicting maximality. Hence
\[
\begin{gathered}
\sum_{i\in I}q_i=1\quad\text{strongly},\\
\text{over finite subsets of }I.
\end{gathered}
\tag{PC7.3}
\]

Suppose \(T_f\) vanishes on \(eMe\), and let \(x\in M\). For every \(i,j\), one has \(w_i^*xw_j\in eMe\). Equation (PC7.1) gives
\[
w_i^*T_f(x)w_j
=T_f(w_i^*xw_j)=0.
\]
Multiplication by \(w_i\) and \(w_j^*\) yields \(q_iT_f(x)q_j=0\). Thus for every finite \(J\subset I\), with \(P_J=\sum_{i\in J}q_i\),
\[
P_JT_f(x)P_J=0.
\]
The projections \(P_J\) converge strongly to one. For any bounded operator \(y\) and any vector \(\xi\),
\[
\begin{aligned}
\|(P_JyP_J-y)\xi\|
&\le\|y\|\|(P_J-1)\xi\|\\
&\quad+\|(P_J-1)y\xi\|\longrightarrow0.
\end{aligned}
\]
Apply this to \(y=T_f(x)\) to conclude \(T_f(x)=0\). The converse implication, from vanishing on \(M\) to vanishing on its corner, is immediate. The entire action and every such corner therefore have exactly the same annihilating filters. Their defining hulls coincide, proving the first equality in (PC7.2). Intersecting those equal spectra over all nonzero fixed projections proves the second. \(\square\)

Factoriality of the fixed algebra is substantive. For example, on \(M_2(\mathbb C)\) the action generated by \(h=\operatorname{diag}(0,a)\), \(a>0\), fixes the diagonal algebra, which is not a factor. Its full spectrum is \(\{0,-a,a\}\), whereas either rank-one diagonal corner has spectrum \(\{0\}\). The scalar filter acts on each matrix unit by its Fourier transform at that unit's frequency, proving both statements directly.

<a id="pc8"></a>

## PC8. The full factorial-centralizer spectral theorem

The following exact earlier programme results connect the action calculation to modular operators.

- [MG-0–MG-1](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.0) prove, for every faithful normal semifinite weight \(\psi\) on a nonzero von Neumann algebra, the full finite-ideal filter identity and
  \[
  \begin{aligned}
  \operatorname{Sp}(\sigma^\psi)
  &=\operatorname{Sp}(\log\Delta_\psi),\\
  \exp\operatorname{Sp}(\sigma^\psi)
  &=\operatorname{Sp}(\Delta_\psi)\cap(0,\infty).
  \end{aligned}
  \tag{PC8.1}
  \]
  These are identities for the complete closed operators. Their proof uses bounded operator approximants together with convergence of their GNS vectors and the closed GNS graph; it does not assume the GNS map is bounded on an operator ball.
- [MG-3](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.3) proves that for a factor \(M\), the group \(\Gamma(\sigma^\psi)\) is the same for every faithful normal semifinite weight \(\psi\). It constructs a balanced weight on \(M_2(M)\), identifies its two diagonal modular actions and applies [CS-3](../../OA-FLOW/OA-FLOW-CS.html#oa-flow.cs.3) to both corners. The underlying full weight, normal-filter, balanced-graph and spectral-calculus proofs are the named predecessors of MG and CS.

These results hold for arbitrary Hilbert-space cardinality and do not assume that \(M\) is already type III. In particular we use MG-0–MG-3; the type III corner-transport hypothesis of MG-4 is unnecessary here.

**Theorem PC8.1.** Let \(M\ne0\) be a factor, and let \(\varphi\) be a faithful normal semifinite weight such that its centralizer \(M_\varphi\) is a factor. With the intersection taken over all faithful normal semifinite weights,
\[
S(M)=\bigcap_\psi\operatorname{Sp}(\Delta_\psi)
    =\operatorname{Sp}(\Delta_\varphi).
\tag{PC8.2}
\]
The equality includes zero when zero belongs to the spectrum. There is no state, separability, periodicity or finite-total-weight restriction.

*Proof.* The modular action has fixed algebra \(M_\varphi\). Lemma PC7.1 therefore gives
\[
\Gamma(\sigma^\varphi)
=\operatorname{Sp}(\sigma^\varphi).
\]
For any faithful normal semifinite weight \(\psi\), MG-3 and the definition of the corner intersection give
\[
\begin{aligned}
\operatorname{Sp}(\sigma^\varphi)
&=\Gamma(\sigma^\varphi)\\
&=\Gamma(\sigma^\psi)
 \subseteq\operatorname{Sp}(\sigma^\psi).
\end{aligned}
\]
Taking exponentials and using (PC8.1) shows that every positive spectral value of \(\Delta_\varphi\) belongs to every \(\operatorname{Sp}(\Delta_\psi)\). Since \(\varphi\) is itself one of the weights in the intersection, this proves
\[
S(M)\cap(0,\infty)
=\operatorname{Sp}(\Delta_\varphi)\cap(0,\infty).
\tag{PC8.3}
\]

It remains to handle zero. The modular operator \(\Delta_\varphi\) is positive and injective, so its spectral projection at zero vanishes. If zero is not in its spectrum, then it is not in \(S(M)\), by the defining inclusion.

If instead \(0\in\operatorname{Sp}(\Delta_\varphi)\), then every interval \((0,\varepsilon)\) has nonzero spectral projection. Otherwise the spectrum is supported in \([\varepsilon,\infty)\), because the projection at zero is zero. The Borel reciprocal \(r\mapsto r^{-1}\) on that support would then be bounded and, since its product with \(r\) equals one, would map the whole Hilbert space into the full domain of \(\Delta_\varphi\) and provide a bounded two-sided inverse. This contradicts zero being spectral. These full-domain inverse rules and the support-on-spectrum assertion are established in the spectral-measure argument of MG-1.

Consequently, for every positive integer \(n\), choose
\[
r_n\in\operatorname{Sp}(\Delta_\varphi)\cap(0,1/n).
\]
Equation (PC8.3) puts each \(r_n\) in every \(\operatorname{Sp}(\Delta_\psi)\). Each such operator spectrum is closed, so \(r_n\to0\) puts zero in every one of them, hence in \(S(M)\). All modular spectra are subsets of \([0,\infty)\); the positive comparison and the zero argument therefore prove (PC8.2) in full. \(\square\)

For the Powers state, Theorem 3.2 of the lesson proves the factorial-centralizer hypothesis, and Proposition 2.1 computes the entire modular spectrum as \(\{0\}\cup\lambda^{\mathbb Z}\). Theorem PC8.1 therefore gives its \(S\)-invariant directly, without assuming its factor type in advance. At the tracial endpoint the computed spectrum is \(\{1\}\), so the same theorem introduces no zero spectral point.

<a id="pc9"></a>

## PC9. Contractive retractions and the injectivity criterion

The word *projection* in this section means a bounded linear idempotent map. It need not be an orthogonal projection on a Hilbert space, and it need not be normal. Inner products in this section are linear in the second variable. We retain the full unital C*-algebra assertion as well as its von Neumann algebra application.

The earlier programme inputs are [completely positive extension, Lemmas 2.1–2.2 and Theorem 2.3](../../OA-APPROX/completely-positive-finite-models.html#2-order-allows-extensions), and the [universal bidual construction](../../OA-APPROX/abstract-tensor-and-universal-bidual-foundations.html#abf-bidual-product). The former proves extension from an arbitrary operator system into any Hilbert-space operator algebra, including preservation of the unit value. The latter equips the Banach bidual of every C*-algebra with its von Neumann product and original weak-star topology; its product is separately weak-star continuous and the original algebra is weak-star dense. Their scalar extension, compactness, GNS, concrete-predual and operator-density foundations remain the stated predecessors of those results.

**Theorem PC9.1.** Let \(B\subseteq A\) be nonzero unital C*-algebras with the same unit. If \(E:A\to B\) is a linear retraction of norm one, then it is unital, completely positive and \(B\)-bimodular:
\[
E(bxc)=bE(x)c
\quad(b,c\in B,\ x\in A).
\tag{PC9.1}
\]
In particular,
\[
E(x)^*E(x)\le E(x^*x).
\tag{PC9.2}
\]
The result has no separability, finite-state or normality hypothesis.

*Proof.* We first establish the assertion for a von Neumann subalgebra \(N\) of a concrete von Neumann algebra \(D\), and a norm-one retraction \(F:D\to N\). The range contains the shared unit, so \(F(1)=1\).

For every unit vector \(\xi\), the functional \(g(x)=\langle\xi,F(x)\xi\rangle\) has norm one and value one at the unit. The [scalar positivity criterion](../../OA-APPROX/abstract-tensor-and-universal-bidual-foundations.html#abf-positive-norm-criterion) proves it positive: for self-adjoint \(h\), the norm estimate on \(1+ith\) for both signs of \(t\) makes \(g(h)\) real, and \(\|1-a\|\le1\) for \(0\le a\le1\) makes \(g(a)\ge0\). All vector tests therefore make \(F\) positive. Decomposing self-adjoint elements into positive parts shows that it preserves adjoints.

Fix a projection \(p\in N\) and put \(q=1-p\). Positivity and \(F(p)=p\) show that \(F\) sends \(pDp\) into \(pNp\): for \(0\le x\le p\), its image lies between zero and \(p\), and linear combinations of positive elements fill the corner.

Now take \(x=pxq\) with \(\|x\|\le1\), and set \(y=F(x)\). The row and column norms give, for every positive integer \(n\) and real \(t\),
\[
\begin{aligned}
\|np+e^{it}x\|&\le\sqrt{n^2+1},\\
\|nq+e^{it}x\|&\le\sqrt{n^2+1}.
\end{aligned}
\]
The same bounds hold with \(x\) replaced by \(y\), by contractivity. Testing the first on a unit vector in \(pH\) gives
\[
|n+e^{it}\langle\xi,y\xi\rangle|
\le\sqrt{n^2+1}.
\]
Choose the phase to make the coefficient nonnegative and let \(n\) increase. The coefficient must vanish. Polarization gives \(pyp=0\); the second bound similarly gives \(qyq=0\).

There can be no output in the opposite off-diagonal corner either. If \(v=qyp\ne0\), then \(v\in N\) and \(F(v)=v\). Operators in the two off-diagonal corners have orthogonal domains and ranges, so
\[
\begin{gathered}
\max\{\|pyq\|,(n+1)\|v\|\}\\
\begin{aligned}
&=\|F(x+nv)\|\\
&\le\|x+nv\|\\
&=\max\{\|x\|,n\|v\|\}.
\end{aligned}
\end{gathered}
\]
For sufficiently large \(n\), the right side is \(n\|v\|\), contradicting the left side. Thus \(F(pxq)=pF(pxq)q\). Scaling, adjoints and the four-corner decomposition give
\[
F(px)=pF(x),\qquad F(xp)=F(x)p.
\tag{PC9.3}
\]
This is Tomiyama's range-block norm method, with the phase and opposite-corner steps explicit. All operators in the argument belong to \(D\); the domain need not be the whole \(B(H)\).

Every self-adjoint \(b\in N\) is a norm limit of finite real linear combinations of projections in \(N\). The complete construction in [Q3](../../OA-APPROX/semidiscrete-finite-models.html#projection-bimodularity) takes the support projections of \((b-t)_+\), forms their differences along a finite mesh, and obtains \(b_\delta\) with \(\|b-b_\delta\|\le\delta\). These support projections belong to \(N\) by its strong closedness; no continuity of \(F\) in the strong topology is used. Apply (PC9.3) to the finite combinations and pass to the norm limit. Splitting general multipliers into real and imaginary parts proves \(N\)-bimodularity.

We spell out why this also gives complete positivity. If \(X=[x_{ij}]\ge0\) in \(M_k(D)\), let \(Y=[F(x_{ij})]\in M_k(N)\). It is self-adjoint, and every column \(b\) over \(N\) satisfies
\[
b^*Yb=F(b^*Xb)\ge0.
\]
Let \(R=Y_-\) be the negative part, and test the columns \(c_j\) of \(R^{1/2}\). Continuous matrix calculus gives
\[
0\le c_j^*Yc_j=-(R^2)_{jj}\le0.
\]
Since \((R^2)_{jj}=\sum_iR_{ij}^*R_{ij}\), every entry of \(R\) is zero. Hence \(Y\ge0\). This proves complete positivity at every matrix size, as in the full matrix argument of Corollary 4.3 in the same programme lesson.

We now pass to the stated C*-algebra scope. Write \(j:B\to A\) for inclusion. Its Banach adjoint \(j^*:A^*\to B^*\) is restriction. Hahn–Banach extends every bounded functional on \(B\) to \(A\) with unchanged norm. Consequently
\[
j^{**}:B^{**}\longrightarrow A^{**}
\]
is an isometry. Its image is exactly \((\ker j^*)^\perp\). Indeed an element \(Y\) of that annihilator defines a bounded functional on \(B^*\) by sending \(f\) to \(Y(g)\), where \(g|_B=f\). The value is independent of the extension, and a norm-preserving extension bounds it by \(\|Y\|\|f\|\). This proves the image assertion and its weak-star closedness.

The bidual products identify \(j^{**}\) as a unital *-homomorphism. To check this rather than assume it, approximate one variable in \(B^{**}\) weak-star by elements of \(B\), keeping the other in \(B\); separate continuity and the original multiplicativity of \(j\) give the identity. Approximate the second variable to obtain the identity for both arbitrary variables. The weak-star continuous involutions give preservation of adjoints by one such limit. Thus
\[
N=j^{**}(B^{**})\subseteq D=A^{**}
\]
is a unital von Neumann subalgebra.

The identity \(Ej=\operatorname{id}_B\) passes to second adjoints. Therefore
\[
F=j^{**}E^{**}:D\longrightarrow N
\]
is a retraction, is contractive, and fixes the unit, so has norm one. The von Neumann argument just proved makes \(F\) unital, completely positive and \(N\)-bimodular. On the canonical copies of \(A\) and \(B\), it is exactly \(E\). Faithful *-embeddings preserve and reflect all matrix positive cones, by continuous matrix calculus. Restriction therefore gives complete positivity and (PC9.1) for \(E\).

Finally apply positivity to \((x-E(x))^*(x-E(x))\) and expand using bimodularity and \(E^2=E\). Its image is \(E(x^*x)-E(x)^*E(x)\), proving (PC9.2). \(\square\)

**Corollary PC9.2.** For a nonzero von Neumann algebra in any faithful normal unital representation \(M\subseteq B(H)\), the following are equivalent:

1. Every completely positive map from an operator system into \(M\) has a completely positive extension to its containing unital C*-algebra, preserving the unit value.
2. There is a ucp retraction \(P:B(H)\to M\).
3. There is a bounded linear projection of norm one from \(B(H)\) onto \(M\).

*Proof.* Apply the first property to the identity of the operator system \(M\subseteq B(H)\). This gives the second, which implies the third. Theorem PC9.1 makes the projection in the third property ucp. Given a completely positive map \(\phi:S\to M\), the earlier extension theorem gives \(\widetilde\phi:A\to B(H)\) with the same restriction and unit value. Then \(P\widetilde\phi:A\to M\) is the required extension; its unit value is unchanged because \(P\) fixes \(M\). The norm of a completely positive map on an operator system is the norm of its unit value, as proved in that extension theorem. This proves the equivalence. The first property is intrinsic to \(M\), so the criterion holds in every faithful normal representation. None of these extensions or retractions is asserted normal. \(\square\)

For the commutant implication used in PC3, Amplifications and commutants, Proposition 1.1, Lemma 1.2 and Theorem 1.3 supply the exact earlier proof. Its arbitrary-basis matrix construction amplifies a possibly singular ucp retraction; compression gives corner retractions. Transposition identifies the positive matrix cones of opposite operator systems, so the extension property passes to the opposite algebra. In a standard pair the linear anti-isomorphism \(x\mapsto Jx^*J\) identifies that opposite algebra with the commutant. The normal representation comparison realizes any other faithful normal representation in a commutant corner of an amplification. These steps prove commutant duality at arbitrary cardinality. The standard-pair construction verifies the Hilbert-algebra hypotheses and uses its explicitly linked bounded modular theorem BG-1–BG-6; that theorem and the concrete-predual and faithful-image predecessors remain part of the transitive foundations.

Thus the norm-one maps constructed in PC3 and PC4 are legitimate completely positive retractions, and the state used in PC4.2 is a hypertrace. The classification consequence follows from Theorem PC10.1 and its stated earlier foundations.

<a id="pc10"></a>

## PC10. From an invariant state to finite classification

An invariant state on the ambient bounded operators need not be normal. The argument below retains that scope. It first identifies the trace remembered by that state, then obtains completely positive matrix approximations, and finally converts those maps into actual matrix subalgebras. These are distinct steps.

**Theorem PC10.1.** Let \(N\) be a type \({\rm II}_1\) factor with normalized faithful normal trace \(\tau\), represented by left multiplication on \(H=L^2(N,\tau)\). Suppose a state \(\chi\) on \(B(H)\) satisfies
\[
\begin{gathered}
\chi(uTu^*)=\chi(T)\\
(u\in\mathcal U(N),\ T\in B(H)).
\end{gathered}
\tag{PC10.1}
\]
Then \(N\) is injective and locally approximately finite dimensional. If \(N\) has separable predual, it is normally isomorphic to \(R\), and has a generating increasing sequence of unital dyadic matrix algebras. No normality of \(\chi\) is required; the local approximation and injectivity assertions have no separability hypothesis.

*Proof.* We use the complete earlier finite-model proofs at the specific places indicated below. The finite trace and projection premises are the PC/FCT construction in the [trace companion](trace-existence-foundations.md#fct-7). The trace representation, scalar separation and finite-matrix extension are also written out in Sections 1–2 of [Hypertraces and finite injective algebras](../../OA-APPROX/hypertraces-finite-injectivity.html#trace-realization).

**The state restricts to the specified trace.** Equation (PC10.1), applied to \(Tu\), gives \(\chi(uT)=\chi(Tu)\). A self-adjoint contraction \(a\) is the real part of the unitary \(a+i(1-a^2)^{1/2}\). Splitting real and imaginary parts therefore writes every element of \(N\) as a linear combination of at most four unitaries. Thus \(\chi\) is an \(N\)-central state on \(B(H)\), a hypertrace.

The norm-averaging proof in [Balancing Kraus families, Lemma 2.1](../../OA-APPROX/balancing-kraus-families-and-unitary-couplings.html#2-simultaneous-averaging-in-operator-norm) applies to every type \({\rm II}_1\) factor. For each \(x\in N\) it gives finite convex averages \(A_j\) of inner conjugations such that
\[
\|A_j(x)-\tau(x)1\|\longrightarrow0.
\]
It uses trace cuts, finite matrix permutations and a norm estimate on the rounded residual; its alternative spectral-contraction proof gives the same conclusion. Since \(\chi A_j(x)=\chi(x)\) and \(\|\chi\|=1\), the displayed limit proves
\[
\chi|_N=\tau.
\tag{PC10.2}
\]
Norm convergence is essential here: no continuity of this state for a weaker operator topology is being assumed.

**A hypertrace supplies matrix maps.** Apply the trace-controlled density approximation DEN in Section 3 of [Hypertraces and finite injective algebras](../../OA-APPROX/hypertraces-finite-injectivity.html#3-finite-densities-retain-both-invariance-and-the-chosen-trace) to \(\chi\) and (PC10.2). Its proof uses convex separation of finite-rank normal states while retaining their restriction to \(N\), followed by its proved finite-matrix Powers–Størmer inequality. Thus, for any finite lists and positive tolerances, there is a positive finite-rank operator \(h\) with
\[
\begin{gathered}
\operatorname{Tr}(h^2)=1,\qquad
\|\rho_{h^2}|_N-\tau\|<\alpha,\\
\|[h,b_i^*]\|_{\rm HS}<\beta,
\qquad \rho_d(T)=\operatorname{Tr}(dT).
\end{gathered}
\tag{PC10.3}
\]
The trace on \(B(H)\) and its Hilbert–Schmidt norm are distinguished from \(\tau\) and its \(2\)-norm on \(N\).

For \(a_i,b_i\in N\), put \(c=\sum_i a_i b_i^*\). On the fixed spatial tensor representation of \(N\) and its opposite algebra, the Hilbert–Schmidt vector \(h\) defines the state
\[
\theta_h\!\left(\sum_i a_i\otimes\bar b_i\right)
=\sum_i\operatorname{Tr}(h a_i h b_i^*).
\]
Here \(\bar b\) acts on the conjugate Hilbert space; the tensor acts on a Hilbert–Schmidt operator \(d\) by \(d\mapsto adb^*\). The finite trace estimates FP and spatial construction SP in that same lesson prove both this identification and the state norm bound. Cyclicity and Cauchy–Schwarz, together with (PC10.3), give
\[
\begin{aligned}
|\tau(c)|
&\le\left\|\sum_i a_i\otimes\bar b_i\right\|\\
&\quad+\alpha\|c\|+\beta\sum_i\|a_i\|.
\end{aligned}
\]
Letting \(\alpha,\beta\) decrease to zero proves the scalar spatial bound SC for the specified trace. This derivation uses the given hypertrace; it does not first produce one from an assumed retraction.

The functional
\[
\Omega\!\left(\sum_i a_i\otimes\bar b_i\right)
=\tau\!\left(\sum_i a_i b_i^*\right)
\tag{PC10.4}
\]
is positive on algebraic squares: it is the vector functional of \(1\in L^2(N,\tau)\) for the commuting left and right actions. The scalar bound extends it to a state on the fixed spatial completion; positivity there follows by approximating positive square roots with algebraic tensors.

We can now apply exactly the matrix-map construction (M1)–(M6) in [Section 5](../../OA-APPROX/hypertraces-finite-injectivity.html#5-explicit-completely-positive-matrix-models). Its argument after the construction of \(\Omega\) uses only this spatial state, the faithful normal trace and its concrete predual. It approximates \(\Omega\) by finite mixtures of product-vector states, while keeping the right marginal close to \(\tau\) in functional norm. If \(\zeta_{li}\in N\) are their right coefficients, its maps have the form
\[
\begin{aligned}
S(a)&=\operatorname{diag}_l
 [\langle\xi_{li},a\xi_{lj}\rangle]_{i,j},\\
R_0(X)&=\sum_{l,i,j}X_{li,lj}\zeta_{li}\zeta_{lj}^*,\\
w&=R_0(1),\qquad r=\max(w,1)^{-1/2},\\
R(X)&=rR_0(X)r.
\end{aligned}
\tag{PC10.5}
\]
The vectors \(\xi_{li}\) are orthonormal within each block. Consequently \(S\) is normal ucp; \(R\) is cpc because \(R(1)\le1\). The marginal estimate is \(\tau(|w-1|)<\delta\). The square-root correction changes the spatial functional by at most \(2\sqrt\delta\), and the proof gives
\[
|\tau((RS(a)-a)b^*)|
<\delta+2\sqrt\delta\,\|a\|\|b\|
\tag{PC10.6}
\]
on the prescribed finite tests. The functionals \(x\mapsto\tau(xb^*)\) span a norm-dense subspace of \(N_*\): a nonzero annihilator would contradict faithfulness by taking \(b=x\). Contractivity therefore extends (PC10.6) to every finite list of normal tests. Directing over the lists and tolerances produces normal cpc maps \(S_i:N\to M_{m_i}\) and cpc maps \(R_i:M_{m_i}\to N\) with \(R_iS_i\to\operatorname{id}_N\) pointwise ultraweakly. This is semidiscreteness, obtained from (PC10.1).

For completeness it also gives the required retraction. Extend \(S_i\) to a cpc map \(\widetilde S_i:B(H)\to M_{m_i}\) by the finite-matrix extension proof FEXT. The maps \(R_i\widetilde S_i\) have a subnet converging in the compact product of the ultraweak balls \(\{x\in N:\|x\|\le\|T\|\}\), indexed by \(T\in B(H)\). Their limit \(P:B(H)\to N\) is linear and completely positive: linear identities and positive matrix cones are closed for these scalar coefficient limits. It fixes every \(x\in N\) because \(R_iS_i(x)\to x\), and hence fixes the unit and is a retraction. Corollary PC9.2 proves injectivity. The product compactness and finite-matrix extension used here are proved in Section 1 of the hypertrace lesson. Neither the subnet nor its limit is asserted normal.

**Matrix maps give actual finite-dimensional subalgebras.** We now use the following complete direct proofs, with their different tasks kept explicit.

1. [Tracial adjoints and rational matrix models, Lemma 1.1 and Theorems 2.1–3.1](../../OA-APPROX/tracial-adjoints-and-rational-matrix-models.html#weighted-adjoint-mechanism), prove the normal cp trace adjoint, the improved weighted Hilbert bound, and the rational integer-slot channels. Trace-preserving finite models, (N1)–(N3), Theorem 2.1 and Corollary 4.2, then turn semidiscrete maps into trace-preserving ucp reconstructions with unitary input models. The unit corrections are actual positive maps, and their trace-norm errors tend to zero.
2. [Balancing Kraus families, Theorem 3.1 and Corollary 4.2](../../OA-APPROX/balancing-kraus-families-and-unitary-couplings.html#3-balanced-reconstruction-on-a-matrix-subfactor), embed that full matrix algebra as a unital subfactor, average the second Kraus sum in its relative commutant, and fill both positive defects by countable trace exhaustion. The [internal Kraus formula, Lemma 4.1](../../OA-APPROX/properly-infinite-injective-algebras-and-dyadic-approximation.html#lemma-4-1), applies here in its finite-family form; its properly infinite one-isometry conclusion is not used. The two strong sums are both exactly one, and the coupling-energy identity turns the reconstruction error into a small intertwining energy.
3. [Unitary couplings and finite injective factors, Lemmas 1.1, 2.1–2.2 and 3.1, and Theorem 4.1](../../OA-APPROX/unitary-couplings-and-finite-injective-factors.html#4-small-coupling-energy-gives-unitary-conjugation), sample the coupling, clip it without increasing that energy, and compare the two coordinate projections in a finite tracial ultrapower commutant. Equality is tested against every central projection; scalar trace equality alone would not suffice in that commutant. Finite projection comparison and the polar unitary lift give one implementing unitary in the original factor.

Here is the quantitative assembly. Given unitaries \(u_1,\ldots,u_n\) and \(\varepsilon>0\), first choose the coupling threshold \(\delta>0\) in Theorem 4.1 of the last provider. The second provider, with the first as its input, supplies a matrix subfactor \(D\subset N\) and unitaries \(v_k\in D\) that are \(\delta\)-related to the \(u_k\). The last theorem gives a unitary \(z\in N\) such that
\[
\|u_k-zv_kz^*\|_{2,\tau}<\varepsilon
\qquad(1\le k\le n).
\tag{PC10.7}
\]
The approximants lie in the actual finite-dimensional algebra \(zDz^*\). Express any finite set of general operators as finite linear combinations of unitaries and divide the error budget by the largest coefficient sum. This gives finite-set \(2\)-norm approximation with operator norms bounded independently of the shrinking error. The bounded trace-topology proof PB1–PB2 in [Local approximation and the hyperfinite finite factor](../../OA-APPROX/hyperfinite-finite-factors.html#bounded-trace-topology) converts it to local sigma-strong* approximation. Thus \(N\) is locally AFD without any countability assumption.

**Separable predual gives the specified factor.** In separable-predual scope, [the same lesson, Lemmas 1.1, 3.1, 4.1 and Theorem 5.1](../../OA-APPROX/hyperfinite-finite-factors.html#5-uniqueness-and-all-finite-corners), turn these local approximants into nested dyadic factors. Its proof cuts rational dyadic traces, aligns the first corner by a controlled projection rotation, reconstructs the old matrix system exactly, and iterates on a countable dense set. Inserting the intermediate matrix levels gives \(A_m\cong M_{2^m}\), \(A_m\subset A_{m+1}\), with weakly dense union. The compatible trace-preserving isomorphism of their algebraic union with the dyadic tensor union extends to an onto unitary of trace GNS spaces. Intertwining the left actions gives the normal isomorphism \(N\cong R\). This completes the invariant-state formulation used in PC4.2. \(\square\)

The finite classification chain uses the tracial quotient, normal embedding, unitary representatives and bounded expectations in PC11. The concrete predual, bounded calculus, density and faithful-image proofs are identified there, and finite projection comparison is supplied by the trace companion. [TL1–TL6](../../OA-APPROX/invariant-state-trace-hilbert-inputs.html#finite-trace-expectation) retain their general trace Hilbert scope and measurable-operator realization of the \(L^1\)-predual. For the expectations actually used here, the complete bounded proof HF0 is applied in PC11. [TF2–TF3 of the tensor companion](normal-tensor-and-tracial-product-foundations.md#tf3-compatible-finite-identifications-extend-normally) supply the dyadic trace-GNS realization and normal identification; its TF5–TF6 give normal tensor maps in arbitrary faithful normal representations. The modular foundations elsewhere retain their stated scope.

The finite-factor matrix reconstruction and balanced-coupling method is due to Haagerup, as credited in the linked programme proofs. The hypertrace-to-spatial-state route is the one developed in their finite-density and product-vector arguments.

<a id="pc11"></a>

## PC11. Tracial quotients, normal embeddings and expectations

The finite-classification argument uses a finite ultrapower and a relative commutant inside it. Their centers can be nontrivial. The following statement supplies the quotient, expectation and lifting operations at that generality.

**Theorem PC11.1.** Let \(A\) be a nonzero von Neumann algebra with a faithful normal tracial state \(\tau\), and let \(\omega\) be a free ultrafilter on the positive integers. Set
\[
\begin{aligned}
I_\omega&=\{(a_n)\in\ell^\infty(\mathbb N,A):\\
&\hspace{2em}\lim_\omega\|a_n\|_{2,\tau}=0\},\\
A^\omega&=\ell^\infty(\mathbb N,A)/I_\omega,\\
\tau^\omega([a_n])&=\lim_\omega\tau(a_n).
\end{aligned}
\tag{PC11.1}
\]
Then:

1. This quotient is a finite von Neumann algebra in its faithful trace GNS representation, with faithful normal tracial state \(\tau^\omega\). The constant embedding \(\iota:A\to A^\omega\) is faithful, unital, trace preserving and ultraweakly continuous, with von Neumann range and a normal inverse onto that range.
2. Every unitary in \(A^\omega\) has a representative consisting of unitaries in \(A\).
3. For every unital von Neumann subalgebra \(B\) of any faithfully tracial finite algebra \((D,\rho)\), there is a unique trace-preserving \(B\)-bimodule projection \(E_B:D\to B\). It is faithful, normal and ucp. On trace Hilbert spaces it is the orthogonal projection onto \(L^2(B,\rho|_B)\), and hence gives the nearest \(2\)-norm approximant in \(B\).

No factoriality, separable predual or separable representation is assumed. In the third assertion the trace is normalized; dividing any nonzero faithful normal finite trace by its value at the unit gives the same expectation.

*Proof.* The bounded calculus and Hilbert tools are proved in CF1–10. CP1–6 constructs the concrete predual, its norm-closed inclusion in the dual and its square-summable vector coefficients. BD1–5 proves bounded density, using a direct resolvent identity and continuous calculus; ST1–2 and ST-C proves faithful normal ranges, inverses and normal trace representations. These are the bounded foundations used below. The positive-functional Schwarz estimate and the bounded trace topology are proved in [NT1–2](../../OA-APPROX/central-sequence-foundations.html#nt1-normal-functional-decomposition).

**The quotient and its trace.** For \(a,b,x\in A\), positivity and traciality give
\[
\|axb\|_{2,\tau}\leq
\|a\|\,\|b\|\,\|x\|_{2,\tau}.
\tag{PC11.2}
\]
Thus every bounded sequence multiplies \(I_\omega\) into itself on both sides. This ideal is star closed since the two trace seminorms agree, and norm closed since \(\|x\|_2\leq\|x\|\). The complete quotient-norm and positivity proof [CQ1](../../OA-APPROX/central-sequence-quotient-and-lifting-inputs.html#cq1-complete-cstar-quotient) applies.

Apply [Multiplier ultraproducts, Lemma 2.1, Lemma 3.1 and Theorem 3.2](../../OA-APPROX/multiplier-ultraproducts-and-normal-embeddings.html#3-completeness-on-two-cyclic-vectors) with state \(\tau\). Its normalizer is the whole bounded sequence algebra by (PC11.2), so its quotient is exactly (PC11.1). The proof first establishes a faithful quotient state, then constructs its isometric GNS representation, then proves strong closure. In that last step finite simultaneous tests select one coordinate row from a fast Cauchy sequence; the two cyclic-vector metrics handle arbitrary strong Cauchy nets without assuming a countable cofinal set. Normality follows only after strong closure, because the state is then a vector state on a von Neumann algebra. This argument requires a faithful normal state, not separable predual. The earlier tracial Hilbert and complete-ball arguments are also given in [CQ2–3](../../OA-APPROX/central-sequence-quotient-and-lifting-inputs.html#cq2-faithful-trace-hilbert-representation).

Coordinate traces give
\[
\tau^\omega([a_n][b_n])=
\tau^\omega([b_n][a_n]).
\tag{PC11.3}
\]
Consequently the faithful normal quotient state is tracial. It makes the quotient finite: for an isometry \(v\), the positive projection \(1-vv^*\) has trace zero and hence is zero.

**Normality of the constant embedding.** Constants give an injective unital star homomorphism, since a constant has zero \(2\)-norm only when it is zero, and
\[
\tau^\omega\circ\iota=\tau.
\tag{PC11.4}
\]
Here is a direct proof of ultraweak continuity on the whole domain. In any faithfully tracial von Neumann algebra \((Q,\sigma)\), the functionals \(x\mapsto\sigma(bx)\), \(b\in Q\), are norm dense in \(Q_*\). They are normal by the coefficient module operations. If their norm-closed linear span were proper, Hahn–Banach and the duality \(Q=(Q_*)^*\) would give a nonzero \(x\in Q\) annihilating all of them. Taking \(b=x^*\) contradicts faithfulness. This proof uses only CP and the trace; no measurable density is required.

For fixed \(b\in A^\omega\), let
\[
f_b(x)=\tau^\omega(b\iota(x)),\qquad x\in A.
\]
Cauchy–Schwarz and (PC11.4) give
\[
|f_b(x)|\leq\|b\|_{2,\tau^\omega}\|x\|_{2,\tau}.
\tag{PC11.5}
\]
Thus \(f_b\) extends to a bounded linear functional on \(L^2(A,\tau)\). With the inner product linear in its first variable, Hilbert representation supplies a vector \(\eta\) with \(f_b(x)=\langle x,\eta\rangle\). Choose \(c_j\in A\) converging to \(\eta\) in that Hilbert space. On the operator-norm unit ball,
\[
\begin{aligned}
|f_b(x)-\tau(c_j^*x)|
&\leq\|\eta-c_j\|_2\|x\|_2\\
&\leq\|\eta-c_j\|_2.
\end{aligned}
\tag{PC11.6}
\]
The functionals on the right are normal, and CP makes \(A_*\) norm closed. Hence \(f_b\in A_*\). Apply the preceding density statement to \(Q=A^\omega\): every normal functional there is a norm limit of trace pairings. Composition with the contractive \(\iota\) preserves those norm limits. Every such pullback therefore belongs to \(A_*\), which is precisely whole-domain ultraweak continuity. ST2 now gives the von Neumann range and its normal inverse. The proof does not infer continuity on arbitrary ultraweak nets from continuity on bounded nets.

**The unitary representative.** Let \(u\in A^\omega\) be unitary and choose a bounded representative \((x_n)\). Its relation \(u^*u=1\) says
\[
\lim_\omega\|x_n^*x_n-1\|_2=0.
\tag{PC11.7}
\]
For each polar decomposition \(x_n=v_n|x_n|\), the support projections \(v_n^*v_n\) and \(v_nv_n^*\) are equivalent in the finite algebra \(A\). Their center-valued traces agree. Therefore their complements are equivalent by the complete finite comparison theorem [FCT](trace-existence-foundations.md#fct-7). Adding a partial isometry between the complements extends \(v_n\) to a unitary \(w_n\), with \(x_n=w_n|x_n|\). Continuous positive calculus and \(|t-1|\leq|t^2-1|\) for \(t\geq0\) imply
\[
\|x_n-w_n\|_2
=\||x_n|-1\|_2
\leq\|x_n^*x_n-1\|_2.
\tag{PC11.8}
\]
The difference belongs to \(I_\omega\); hence \([w_n]=u\). This is the full finite-algebra polar lift of [Unitary couplings, Lemma 3.1](../../OA-APPROX/unitary-couplings-and-finite-injective-factors.html#3-unitary-representatives-in-a-finite-ultrapower). Equality of scalar traces of unrelated projections is not used.

**The bounded expectation.** The complete earlier proof is [HF0, the tracial commutant and subalgebra expectation](../../OA-APPROX/hyperfinite-finite-algebra-and-vacuum-inputs.html#hf0). Its hypotheses are exactly those in the third assertion. Its bounded-vector argument is as follows. If \(T\) commutes with right multiplication on \(L^2(B)\), put \(C=\|T\|\) and \(\xi=T1\). The set
\[
\mathcal K_C=\{a1:a\in B,\ \|a\|\leq C\}
\]
is weakly compact: the operator ball is ultraweakly compact by ST1, and its map to the Hilbert space is weakly continuous by the normal trace pairings and uniform approximation of Hilbert test vectors. For \(b=v|b|\), right multiplication by \(|b|^{1/2}\) gives
\[
|\langle\xi,b1\rangle|\leq C\rho(|b|)
=\sup_{\|a\|\leq C}\operatorname{Re}\rho(b^*a).
\tag{PC11.9}
\]
The supremum is attained at \(a=Cv\). Dense Hilbert tests and continuity extend this support inequality to every Hilbert vector. Separation of a point from a closed convex set, by its nearest point and the parallelogram argument given in NT2, puts \(\xi\) in \(\mathcal K_C\). Commutation then gives \(T(b1)=ab1\). This proves that the whole right commutant is the left algebra; it applies with arbitrary center and Hilbert dimension.

Let \(e_B:L^2(D)\to L^2(B)\) be the orthogonal projection. Its range reduces both actions of \(B\). Thus \(e_BL_xe_B|_{L^2(B)}\) commutes with right \(B\), and the result just proved defines the unique element \(E_B(x)\in B\) such that
\[
\begin{gathered}
L_{E_B(x)}=e_BL_xe_B|_{L^2(B)},\\
E_B(x)1=e_Bx1,\qquad
\|E_B(x)\|\leq\|x\|.
\end{gathered}
\tag{PC11.10}
\]
Faithfulness of left multiplication gives linearity, the bimodule identities and the projection property. Matrix compression gives complete positivity at every size, and the unit is fixed. Since \(e_B1=1\), the trace is preserved. If \(x\geq0\) and \(E_B(x)=0\), trace faithfulness gives \(x=0\). Orthogonal projection gives the nearest \(2\)-norm assertion, even though the full Hilbert space contains unbounded vectors.

For normality, pull back a square-summable coefficient series through the compression in (PC11.10). It becomes the corresponding coefficient series in the normal trace representation of \(D\). Its pullback is in \(D_*\), by CP and ST-C. Composing with the normal inverse of the faithful trace representation of \(B\), supplied by ST2, proves ultraweak continuity of \(E_B\) on all of \(D\). Finally any trace-preserving \(B\)-bimodule projection has, for every \(b\in B\), the pairing
\[
\rho(b^*E_B(x))=\rho(b^*x).
\tag{PC11.11}
\]
Those pairings determine the vector \(e_Bx1\), and faithfulness determines its element of \(B\). This proves uniqueness and all three assertions. \(\square\)

**Corollary PC11.2.** The central corner comparison in PC10 may be carried out in the relative commutant \(C\subseteq M_2\overline\otimes A^\omega\) of any unital star subalgebra, with the restricted faithful normal normalized trace. If projections \(p,q\in C\) satisfy \(\rho(zp)=\rho(zq)\) for every central projection \(z\in C\), then \(p\sim q\) in \(C\).

*Proof.* Commutation with a fixed operator is weak-operator closed, so the relative commutant is a von Neumann algebra. Its restricted trace is faithful and normal, and its trace law makes it finite. Let \(\mathcal T_C\) be its faithful normal center-valued trace, constructed in FCT, and put \(h=\mathcal T_C(p)-\mathcal T_C(q)\). The identity \(\rho=\rho\circ\mathcal T_C\) gives \(\rho(zh)=0\) for every central projection \(z\). If the positive part of \(h\) were nonzero, one of its central spectral projections above a positive threshold would contradict that equality and faithfulness; apply the same argument to \(-h\). Thus \(h=0\), and FCT projection comparison gives the equivalence. Theorem PC11.1 supplies the expectation onto \(C\), and its polar-lifting assertion applies to the resulting unitary in \(A^\omega\). No assertion that \(C\) is a factor is required. \(\square\)

These results supply the tracial quotient, bounded expectations and unitary representatives used by PC10. The more general measurable-operator realization of the trace predual remains a separate theorem. The tensor companion supplies the tracial product and general normal tensor maps. The modular-weight, bidual and standard-pair foundations elsewhere in this companion retain their stated scope.

## Sources and authorship

The coefficient and faithful-GNS proof identifies a crossed product with prescribed generators. Finite-dimensional averaging yields injectivity, and the corner and matrix arguments identify the semifinite core using the invariant-state classification theorem. Coordinate changes and inner perturbations preserve the regular presentation. The trace-normalization proof explains why the classification uses the same parameter. Full central support in a factorial fixed algebra preserves every action frequency in each nonzero fixed corner. The modular-weight comparison then identifies the entire factorial-centralizer spectrum, including zero. Contractive retractions onto unital C*-subalgebras are shown to be completely positive and bimodular; the operator-system extension property gives the injectivity criterion in every faithful normal representation. Invariant states yield finite matrix maps, balanced couplings and actual matrix subalgebras; separable predual yields the dyadic factor. Tracial quotients have normal constant embeddings and unitary representatives; bounded trace expectations apply to every von Neumann subalgebra.

The programme exposition uses *Full factors without almost periodic weights*, Lemma 8.1, and *Classification of injective factors*, Lemma 2.2(e,f), Propositions 3.1–3.2, Theorems 4.1 and 4.3, Corollary 4.2, Example 4.4, and Lemmas 8.1–8.2 and Theorem 8.3, by Claude Opus 5.5 (Anthropic). The companion exposition, trace-normalization proof and PC7–PC11 arguments are by GPT-6 Astra (OpenAI). The exact earlier programme proofs [MG-0–MG-3](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.0) and [CS-3](../../OA-FLOW/OA-FLOW-CS.html#oa-flow.cs.3) supply the modular filter identity and weight-independent Connes spectrum, with their stated foundations. The [source record](crossed-product-and-injective-core-foundations.provenance.json) identifies the mathematical contributions and prerequisite scope.

- Masamichi Takesaki, [*Theory of Operator Algebras III*](https://doi.org/10.1007/978-3-662-10453-8), Springer, 2003, XV.3.2 and XVIII.1.1–XVIII.1.4(i): injectivity, commutants and Powers-factor classification. [*Theory of Operator Algebras II*](https://doi.org/10.1007/978-3-662-10451-4) supplies crossed-product and modular background.
- Alain Connes, [*Une classification des facteurs de type III*](https://www.numdam.org/item/ASENS_1973_4_6_2_133_0/), Annales scientifiques de l'École Normale Supérieure 6 (1973), 133–252: Corollary 3.2.7(a), printed pp. 192–193, for the full factorial-centralizer spectral theorem and Theorem 4.3.2(a), Corollary 4.3.3 for discrete decomposition.

- Jun Tomiyama, [*On the projection of norm one in W*-algebras*](https://www.jstage.jst.go.jp/article/pjab1945/33/10/33_10_608/_pdf/-char/en), Proceedings of the Japan Academy 33 (1957), 608–612, Theorem 1, pp. 608–609: the range-block norm argument and passage through biduals. The programme exposition supplies the scalar positivity, projection approximation, full matrix-positivity and bidual-inclusion details.

Original programme exposition is dedicated to CC0-1.0 to the extent of rights held. The human sources retain their own rights. The modular and normal-filter foundations of PC8, the bidual and standard-pair foundations of PC9, the finite-model and tracial foundations of PC10–PC11, and the trace-scaling theorem's prerequisite chain have the exact scopes stated in PC0 and PC8–PC11.
