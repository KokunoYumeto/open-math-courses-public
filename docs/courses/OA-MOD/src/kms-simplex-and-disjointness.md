# Central decompositions and disjoint equilibrium representations

**Self-checked by the writing AI.** The proofs are complete relative to their declared inputs.

Two mechanisms control the geometry of equilibrium states. Central densities refine their convex decompositions; modular time detects when two states can share a von Neumann algebra summand. We develop those mechanisms separately and then apply them to a common dynamics.

The comparison target is Takesaki, *Theory of Operator Algebras II*, Exercise VIII.2(3), printed page 106. All three mathematical clauses are treated below. The nonmetrizable meaning of the measure clause is stated precisely using the complete preceding compact-convex measure proof. No separability assumption is added to the algebra.

The local prerequisite bundle also contains the full countable-amplification proof used by the earlier normal-representation results.

## Equilibrium states at every real inverse temperature

Let \(A\) be a nonzero unital C*-algebra, and let \(\alpha_t\) be a pointwise norm-continuous one-parameter group of automorphisms. For each real \(\beta\), set

\[
 \begin{gathered}
 \gamma_t^\beta=\alpha_{\beta t},\\
 K_\beta=K_{\gamma^\beta}.
 \end{gathered}
 \tag{KS.1}
\]

The set on the right uses the modular upper-strip convention of Fix the strip and build its analytic tests and Replace the strip by exact linear equations. Invariance under \(\gamma^\beta\) is included. If \(\beta\ne0\), it is equivalent to invariance under \(\alpha\). If \(\beta=0\), invariance under the identity group imposes no extra invariance under \(\alpha\); the boundary condition is precisely the trace identity. This exceptional value is zero **inverse** temperature.

By The KMS set is weak-star compact and convex, \(K_\beta\) is weak-star compact and convex and can be empty. Statements concerning a point of it are then vacuous. When it is nonempty, the conclusions are:

- It is a Choquet simplex: each point has a unique maximal regular Borel representing probability in the Choquet order. That measure has the Baire boundary concentration proved in CB-05.
- Distinct extreme points give disjoint primary GNS representations.
- If \(\varphi\in K_{\beta_1}\) has a type III GNS algebra, its representation is disjoint from that of every \(\psi\in K_{\beta_2}\) with \(\beta_2\ne\beta_1\).

For metrizable \(K_\beta\), the first statement says that each point has a unique regular Borel representing measure concentrated on the extreme boundary. In particular this applies when \(A\) is separable. We justify that last metrizability assertion in KS-04.

## A common ambient algebra and the meaning of disjointness

Put \(N=A^{**}\), with the von Neumann algebra and normal-extension structure proved in Transfer of the algebra structure to the Banach bidual through Surjectivity uses a compact ball and the exact density theorem. For a state \(\omega\), write
\((H_\omega,\pi_\omega,\Omega_\omega)\) for its GNS triple and \(M_\omega=\pi_\omega(A)''\). The representation is nondegenerate since \(A\) is unital. Its normal extension \(T_\omega:N\to M_\omega\) has a central kernel. Thus there is a central projection \(e_\omega\) with

\[
 \begin{gathered}
 \ker T_\omega=N(1-e_\omega),\\
 Ne_\omega\cong M_\omega.
 \end{gathered}
 \tag{KS.2}
\]

The isomorphism and its inverse are normal, by UB-08.

For \(\omega\in K_\beta\), Domination transfers the boundary to the GNS algebra proves that the vector state on \(M_\omega\) is faithful and normal, even when \(\omega\) is not faithful on \(A\). Its pullback is the canonical normal extension \(\widehat\omega\) to \(N\): the two extensions agree on \(A\), so normality and density identify them. Therefore \(\widehat\omega\) vanishes on \(N(1-e_\omega)\) and is faithful on \(Ne_\omega\).

In particular \(e_\omega\) is the ordinary support projection of \(\widehat\omega\). To see this without confusing support with central support, let \(q\) be a projection of zero \(\widehat\omega\)-mass. The centrality of \(e_\omega\) makes \(qe_\omega\) a projection; faithfulness on the corner gives \(qe_\omega=0\). Conversely every projection below \(1-e_\omega\) has zero mass. Thus \(1-e_\omega\) is exactly the largest null projection. Its complement is central because of the equilibrium condition and KG-04; that conclusion is not asserted for arbitrary states.

Two representations are **disjoint** if they have no unitarily equivalent nonzero reducing subrepresentations. Equivalently, there is no nonzero bounded intertwiner \(V:H_1\to H_2\) satisfying \(V\pi_1(a)=\pi_2(a)V\) for every \(a\in A\). Here is the equivalence. An equivalence of reducing subrepresentations, extended by zero, is an intertwiner. Conversely an intertwiner has \(V^*V\) in \(\pi_1(A)'\) and \(VV^*\) in \(\pi_2(A)'\), by taking adjoints and multiplying the intertwining identities. Their support projections are reducing. The polar partial isometry of \(V\) intertwines on those supports: approximate it strongly by \(V(V^*V+\varepsilon)^{-1/2}\), using the polar and spectral construction in Polar decomposition and its regularized limit. It is a unitary between the two supported subrepresentations, both nonzero when \(V\ne0\).

Orthogonal central projections in (KS.2) imply disjointness. Indeed an intertwiner for \(A\) intertwines the normal extensions for every \(X\in N\). Approximate \(X\) ultraweakly by elements of \(A\), and pass to each vector coefficient of the two sides; multiplication by the fixed bounded intertwiner is ultraweakly continuous by The ultraweak convergence needed by finite cutoffs. If \(e_1e_2=0\), substitute \(X=e_1\). The first extension takes \(e_1\) to the identity, while the second takes it to zero. Thus the intertwiner is zero.

## Distinct extreme states occupy orthogonal central summands

Extreme equilibrium states are exactly primary states proves that an equilibrium state is extreme in \(K_\beta\) exactly when its GNS algebra is a factor. By (KS.2), an extreme state's \(e_\omega\) is therefore a minimal nonzero central projection of \(N\). Indeed a nontrivial central subprojection would give one in the factor \(Ne_\omega\). Conversely a nonscalar self-adjoint element in the center has a proper nonzero spectral projection, so having no such projections forces a scalar center.

Let \(\varphi,\psi\) be extreme in the same \(K_\beta\). Two minimal central projections are either equal or orthogonal: their product is a central subprojection of each. Suppose they are equal to \(e\). The state
\(\omega=(\varphi+\psi)/2\) belongs to \(K_\beta\). Its normal extension is faithful on \(Ne\), as each summand is, and is zero on \(N(1-e)\). KS-02 shows that \(e_\omega=e\). Hence \(M_\omega\cong Ne\) is a factor, so KG-06 makes \(\omega\) extreme. Its displayed decomposition then forces \(\varphi=\psi=\omega\).

Thus distinct extreme states have \(e_\varphi e_\psi=0\). KS-02 gives disjointness, and KG-06 already gives primarity. This proof concerns extremality among equilibrium states, not purity in the whole state space.

## Central densities refine decompositions and prove the simplex assertion

Fix \(\omega\in K_\beta\), and realize it as a faithful normal state \(\rho\) on \(M=M_\omega\) by KG-04. Consider two finite convex decompositions

\[
 \begin{aligned}
 \omega&=\sum_i t_i\varphi_i\\
       &=\sum_j s_j\psi_j
 \end{aligned}
 \tag{KS.3}
\]

inside \(K_\beta\), omitting zero coefficients.

Each \(t_i\varphi_i\) is dominated by \(\omega\) and satisfies the same KMS boundary, as a positive functional. Domination transfers the boundary to the GNS algebra and A dominated normal KMS functional has a central density give unique central positive contractions \(h_i,k_j\in Z(M)\) with

\[
 \begin{aligned}
 t_i\varphi_i(a)&=\rho(h_i x),\\
 s_j\psi_j(a)&=\rho(k_j x),\\
 x&=\pi_\omega(a).
 \end{aligned}
 \tag{KS.4}
\]

Their sums equal one. In fact the normal functionals with densities \(\sum_i h_i\) and \(1\) agree on \(\pi_\omega(A)\), hence on \(M\); uniqueness of the central density gives \(\sum_i h_i=1\). The other sum is identical.

Since these densities commute, each \(h_i k_j\) is positive and central. Define

\[
 \begin{gathered}
 \nu_{ij}(a)=\rho(h_i k_jx),\\
 x=\pi_\omega(a),\\
 r_{ij}=\nu_{ij}(1).
 \end{gathered}
 \tag{KS.5}
\]

The converse in KG-05 proves its KMS boundary. If \(r_{ij}=0\), positivity and the norm formula for a positive functional make \(\nu_{ij}=0\); if \(r_{ij}>0\), put \(\eta_{ij}=\nu_{ij}/r_{ij}\in K_\beta\). Summing (KS.5) over a row or column gives precisely \(t_i\varphi_i\) or \(s_j\psi_j\). The row masses are \(t_i\) and column masses \(s_j\). These \(\eta_{ij}\) are a common refinement of (KS.3) in the exact sense of CB-06.

Apply Common refinements give a unique maximal representing measure to \(K_\beta\), viewed as a compact convex set in the real dual of \(A_{\mathrm{sa}}\). For every \(\omega\) there is a unique maximal regular Borel representing probability \(\mu_\omega\), in fact a greatest one for the Choquet order. The proof there constructs it by maximizing continuous convex functions over finite decompositions; common refinement proves additivity, and the compact Hausdorff representation theorem constructs the measure. Thus this conclusion is not an invocation of an unwritten Choquet theorem.

Boundary concentration without metrizability proves that \(\mu_\omega(B)=0\) for every Baire set \(B\) disjoint from the extreme boundary. It also constructs the induced probability on traces of Baire sets of that boundary. This is the general boundary interpretation. We do not declare a possibly non-Borel boundary Borel or assert uniqueness for arbitrary measures on an unspecified sigma-algebra.

If \(K_\beta\) is metrizable, CB-04 proves that its boundary is a \(G_\delta\) and that a regular Borel probability is maximal exactly when it is concentrated there. Hence in this case there is a unique representing boundary probability in that ordinary Borel sense.

When \(A\) is separable, choose a sequence \(a_n\) dense in its unit ball. Evaluation on this sequence separates states: equality on the dense sequence extends to all of \(A\) by their common norm bound one. On the state space define

\[
 \begin{aligned}
 d(\varphi,\psi)
 &=\sum_{n\geq1}2^{-n}d_n,\\
 d_n&=\bigl|\varphi(a_n)\\
    &\quad-\psi(a_n)\bigr|.
 \end{aligned}
 \tag{KS.6}
\]

The series is uniformly convergent since each difference is at most two. It defines a metric. Its topology is exactly pointwise convergence on the \(a_n\)'s: finitely many summands control a given finite set of coordinates, and their bounded tail controls the converse. The common norm bound and density then turn convergence on these coordinates into convergence on every \(a\in A\). That is the weak-star topology on states. Restriction gives the asserted metrizability of \(K_\beta\).

## A trivial modular group forces a finite projection

We isolate the part of type theory needed for comparing temperatures. A projection \(p\) in a von Neumann algebra is **finite** if a partial isometry with initial projection \(p\) and final projection at most \(p\) must have final projection \(p\). An algebra is **type III** here if it has no nonzero finite projections.

**Lemma.** A nonzero von Neumann algebra admitting a faithful normal semifinite weight with trivial modular group cannot be type III.

Let the weight be \(\theta\). Semifiniteness supplies a nonzero positive bounded \(a\) of finite weight: otherwise its finite positive cone, and hence its finite linear domain, would be zero and could not be ultraweakly dense. Choose \(\varepsilon>0\) such that

\[
 p=1_{[\varepsilon,\infty)}(a)\ne0.
 \tag{KS.7}
\]

Bounded spectral calculus gives \(p\leq\varepsilon^{-1}a\), so \(0<\theta(p)<\infty\). Triviality of the modular flow puts \(p\) in the centralizer.

The proved corner restriction in Justify spectral restriction before using it identifies the modular group of the faithful restricted weight on \(pMp\) with that same identity group. The restriction is finite because every positive \(x\in pMp\) satisfies \(x\leq\|x\|p\). Normalize it to a faithful state \(\tau\). Positive scalar normalization does not change the modular group: the same invariance and KMS equations hold after scaling, and the uniqueness theorem Uniqueness by an imaginary shift and periodicity applies.

For \(x,y\in pMp\), the constant function with value \(\tau(xy)\) has the real edge of its KMS strip. Boundary uniqueness in Two facts about closed strips makes it that strip function, whose upper edge is \(\tau(yx)\). Thus \(\tau(xy)=\tau(yx)\). If \(v^*v=p\) and \(vv^*\leq p\), then \(v=pvp\), so

\[
 \begin{aligned}
 \tau(vv^*)&=\tau(v^*v)\\
          &=\tau(p).
 \end{aligned}
 \tag{KS.8}
\]

Faithfulness gives \(vv^*=p\). Thus \(p\) is finite and nonzero, proving the lemma.

The same argument shows directly that a nonzero corner carrying a faithful normal tracial state has finite identity. A projection finite in a corner is finite in the ambient algebra: any partial isometry witnessing infiniteness of that projection has both supports below it and hence lies in that corner. In particular a nonzero central corner of a type III algebra remains type III.

## Unequal modular speeds cannot share a type III summand

Let \(\varphi\in K_{\beta_1}\) with \(M_\varphi\) type III, and let \(\psi\in K_{\beta_2}\), where \(\beta_2\ne\beta_1\). Use the central projections \(e_\varphi,e_\psi\in N=A^{**}\) from KS-02 and set \(e=e_\varphi e_\psi\). It suffices to prove \(e=0\), because orthogonality implies disjointness.

First, \(\beta_1\ne0\). If it were zero, KG-04 would identify the modular group of the faithful normal state on \(M_\varphi\) with the identity, contradicting KS-05.

If \(\beta_2=0\), \(\psi\) is tracial on \(A\), by KG-02 with the identity group. Its normal extension is tracial on \(N\): extend the equality \(\widehat\psi(XY)=\widehat\psi(YX)\) first in one variable and then in the other from \(A\), using separate ultraweak continuity of multiplication and normality. If \(e\ne0\), its normalized restriction to \(Ne\) is a faithful normal tracial state, since \(\widehat\psi\) is faithful on \(Ne_\psi\). But \(Ne\) is a nonzero central corner of \(Ne_\varphi\cong M_\varphi\). KS-05 contradicts type III. Thus \(e=0\) in this case.

It remains to treat two nonzero inverse temperatures. Each individual \(\alpha_t\) has a unique normal extension to \(N\) by Second adjoints preserve homomorphisms and composition; uniqueness proves their group law. We do not assume that this extended group is ultraweakly continuous on all of \(N\). Each of the two states is \(\alpha\)-invariant, so its normal extension is invariant. The unique support characterization in KS-02 then makes \(e_\varphi,e_\psi\), and \(e\), invariant under every extended automorphism.

Assume \(e\ne0\), and work in \(R=Ne\). The normalized restrictions

\[
 \begin{gathered}
 \rho=\widehat\varphi|_R/\widehat\varphi(e),\\
 \eta=\widehat\psi|_R/\widehat\psi(e)
 \end{gathered}
 \tag{KS.9}
\]

are faithful normal states. The denominators are strictly positive by faithfulness on the respective larger summands. KG-04 identifies the scaled dynamics with the modular group on each GNS algebra. Normal extension carries the identification to \(Ne_\varphi\) and \(Ne_\psi\); central-corner restriction and the scalar-normalization argument from KS-05 carry it to \(R\). Hence, writing the restricted extended action again as \(\alpha\),

\[
 \begin{gathered}
 \sigma_t^\rho=\alpha_{\beta_1t}|_R,\\
 \sigma_t^\eta=\alpha_{\beta_2t}|_R.
 \end{gathered}
 \tag{KS.10}
\]

These restricted groups have the required continuity because they are modular groups. In particular \(\eta\) is invariant under \(\sigma^\rho\).

The full invariant-density theorem The faithful invariant-weight equivalence now gives a positive injective self-adjoint \(h\), affiliated with \(R_\rho\), such that \(\eta=\rho_h\). The supported perturbation formula Recover modular time on the support and (KS.10) give

\[
 \begin{gathered}
 \sigma_{ct}^\rho
 =\operatorname{Ad}(h^{it})\sigma_t^\rho,\\
 c=\beta_2/\beta_1.
 \end{gathered}
 \tag{KS.11}
\]

Compose on the right with \(\sigma_{-t}^\rho\). For \(\delta=c-1\ne0\), this yields

\[
 \begin{gathered}
 \sigma_s^\rho=\operatorname{Ad}(h^{is/\delta})\\
 (s\in\mathbb R).
 \end{gathered}
 \tag{KS.12}
\]

Set \(k=h^{-1/\delta}\) by spectral calculus. It is positive, injective and self-adjoint, affiliated with \(R_\rho\). Its domain is dense: spectral bands of \(h\) between \(1/n\) and \(n\) increase to one and lie in that domain. No bounded inverse or trace-measurability condition is needed. The construction in Construct affiliated density weights and determine their support makes \(\theta=\rho_k\) a faithful normal semifinite weight. Applying CZ-11 once more gives

\[
 \begin{aligned}
 \sigma_s^\theta
 &=\operatorname{Ad}(h^{-is/\delta})\sigma_s^\rho\\
 &=\mathrm{id}.
 \end{aligned}
 \tag{KS.13}
\]

KS-05 now supplies a nonzero finite projection in \(R\), contradicting that \(R\) is a nonzero central corner of the type III algebra \(M_\varphi\). Therefore \(e=0\). KS-02 proves that the original GNS representations are disjoint.

The argument includes negative inverse temperatures and either sign of \(\delta\). It uses powers of an affiliated operator with their full spectral domains. It does not identify two weights merely because their modular groups are related, nor infer semifiniteness of the new weight without the construction theorem.

## Why the type III and measure qualifications matter

Let \(A=M_2(\mathbb C)\), \(D=\operatorname{diag}(1,2)\), and \(\alpha_t(a)=D^{it}aD^{-it}\). For every real \(\beta\), set

\[
 \begin{gathered}
 \omega_\beta(a)\\
 =\frac{\operatorname{Tr}(D^\beta a)}
        {\operatorname{Tr}(D^\beta)}.
 \end{gathered}
 \tag{KS.14}
\]

The faithful finite-dimensional modular computation in A block model with infinite mass and arbitrarily fast modular motion makes its modular group exactly \(\alpha_{\beta t}\), so \(\omega_\beta\in K_\beta\). Distinct \(\beta\)'s give distinct ratios of the two diagonal masses. Nevertheless all their GNS representations identify with left multiplication by \(M_2\) on the Hilbert–Schmidt matrices: the map sends the GNS vector of \(x\) to \(x(D^\beta/\operatorname{Tr}D^\beta)^{1/2}\), an onto isometry in finite dimension. Thus those representations are unitarily equivalent, not disjoint. The type III assumption in KS-06 cannot be omitted.

The measure qualification has a different source. Neither the definition of a unital C*-algebra nor pointwise norm continuity of \(\alpha\) supplies a countable dense subset of \(A\). KS-04 therefore uses CB-02 on compact Hausdorff spaces and CB-05's Baire formulation. Where a countable dense subset is available, (KS.6) recovers the familiar unique Borel probability on the extreme boundary. Both conclusions are consequences of the full proof, with their actual hypotheses exposed.
