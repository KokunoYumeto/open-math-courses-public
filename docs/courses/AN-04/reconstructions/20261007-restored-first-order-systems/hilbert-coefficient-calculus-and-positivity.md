# Hilbert coefficients, ordered calculus and the sharp lower bound

The systems theorem needs estimates in operator norm. A bound obtained by summing matrix entries can grow with the matrix size and does not prove that theorem for an infinite-dimensional coefficient space. Here we prove the ordinary Hilbert-coefficient statements with constants depending on symbol seminorms and the spatial dimension alone.

The scalar inputs are the complete [ordinary multiplier, composition and adjoint proofs O1–O3](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), the [packet estimate E23–E27](../20261005-restored-airy-models/bounded-derivative-operators.md), and the [moving-probe construction and every differentiated cancellation, G4–G5](../20261005-cauchy-foundations/sharp-lower-bound.md). The complete [Hahn–Banach, Banach integration, Bochner-space, primitive and duality proofs](../20261005-cauchy-foundations/integration-and-duality.md) supply the norm and integral operations. The [Fourier proofs L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), [measure proofs M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), and [Hilbert representation proof T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md) are also included earlier. Their component notices remain in place. This connecting exposition is independently written and dedicated to CC0 1.0.

## H1. The Hilbert Fourier scale and its dense test space

Let \(K\) be a separable complex Hilbert space, with inner product linear in the first entry. The zero space is harmless. Applying Gram–Schmidt to a countable dense set, omitting zero residuals, gives a finite or countable orthonormal basis \((e_j)\). If a vector is orthogonal to every \(e_j\), it is orthogonal to the original dense set and hence is zero. For the finite orthogonal projections \(\Pi_M\), Pythagoras and density therefore give \(\Pi_Mv\to v\) and \(\|v\|^2=\sum_j|(v,e_j)|^2\). The projection norms are at most one.

A \(K\)-valued Schwartz function is norm-smooth with all weighted derivative suprema finite. Its Fourier integral converges in \(K\); frequency derivatives and integration by parts are justified by the integrable norm bounds. Applying each coordinate functional gives scalar Fourier inversion. The scalar inversion estimate also bounds the norm of the vector inverse integral, and coordinates identify the two vectors. Thus inversion holds with the original coefficient \((2\pi)^{-n}\).

For finite-coordinate Schwartz functions, scalar Plancherel and a finite sum give
\[
 \|u\|_{L^2(K)}^2
  =(2\pi)^{-n}\int\|\widehat u(\xi)\|_K^2\,d\xi .
 \tag{HS1}
\]
Bochner simple-function approximation, followed by approximation of each of its finitely many vectors by basis spans and scalar \(L^2\) approximation by compact smooth functions, proves density of this test space in \(L^2(K)\). Completeness, proved in the earlier Bochner-space chapter, extends the Fourier isometry. The inverse extends in the same way, and both compositions are identity on a dense subspace and hence everywhere.

Define \(H^s(K)\) by \(\langle\xi\rangle^s\widehat u\in L^2(K)\). Multiplication by this positive weight and the extended inverse Fourier transform give onto isometries \(E_s:H^s(K)\to L^2(K)\), with inverse \(E_{-s}\). This proves completeness. Truncate frequency to a compact ball, approximate there by finite-coordinate compact smooth functions, and invert. On that ball any finite list of real weights is bounded above and below. This proves simultaneous Schwartz density in any finite list of \(H^s\) norms. The same procedure, using rational boxes and a countable dense set of coefficients, proves separability.

The frequency Cauchy–Schwarz inequality bounds the pairing of \(H^s(K)\) with \(H^{-s}(K)\). It also bounds pairing against each Schwartz test, so these weighted functions define compatible \(K\)-valued tempered distributions. Hilbert representation after applying \(E_s\) proves that every continuous conjugate-linear functional on \(H^s(K)\) is pairing with a unique element of \(H^{-s}(K)\). In particular \(E_{2s}\) is an onto isometry from \(H^s(K)\) to \(H^{-s}(K)\) and \(\langle u,E_{2s}u\rangle=\|u\|_s^2\).

We will also use finite-coordinate approximation in the full Schwartz topology. For any fixed weight and derivative, the function \(x\mapsto\langle x\rangle^N\partial^\alpha u(x)\) has compact closure of its range: it is continuous on compact balls and tends to zero at infinity by one stronger Schwartz weight. Strong convergence of the contractions \(\Pi_M\) is uniform on a compact set, as follows from a finite epsilon net and the common norm bound. Hence \(\Pi_Mu\to u\) in every Schwartz seminorm. Multiplying afterwards by an expanding compact smooth spatial cutoff proves density of finite-coordinate compact smooth tests as well.

## H2. Banach norm limits and the ordered ordinary calculus

The space \(\mathcal L(K)\) is Banach. Indeed an operator-norm Cauchy sequence has a limit on every vector by completeness of \(K\); that pointwise limit is linear and bounded, and the uniform Cauchy inequality passes to the limit to give operator-norm convergence. The same proof applies between two Hilbert spaces.

Let \(a\in S^r_{1,0}(\mathcal L(K))\), with seminorms
\[
 p_{r,L}(a)=\max_{|\alpha|+|\beta|\le L}
 \sup_{x,\xi}\langle\xi\rangle^{-r+|\alpha|}
       \|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)\|.
 \tag{HS2}
\]
Left quantization on \(\mathcal S(K)\) is the norm-convergent integral
\[
 A u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}
                 a(x,\xi)\widehat u(\xi)\,d\xi .
 \tag{HS3}
\]
Its differentiated integrands have integrable norms. Moving frequency derivatives off the exponential controls each \(x^\gamma\partial_x^\beta Au\) by finitely many symbol seminorms and a sufficiently strong input Schwartz seminorm. This is the full Schwartz action, with constants uniform on bounded symbol sets.

Here is the norm-valued extension of the multiplier step in O1–O3. For a Banach space \(E\), first define each compactly truncated scalar-kernel integral with an \(E\)-valued smooth amplitude by its Bochner integral. The amplitude has separable range on its sigma-compact parameter domain: each compact image has finite epsilon nets, and their countable union is separable. The preceding integration chapter therefore applies even when \(E\) itself is not separable. Continuous linear functionals commute with these integrals.

The complete scalar quadratic-multiplier proof bounds each localized term and every derivative of its cutoff remainder by weighted suprema of finitely many amplitude derivatives, using summable bounds for the discarded localization terms. Apply an arbitrary \(\ell\in E'\), \(\|\ell\|\le1\), to the finite integral. Each scalar input seminorm is at most the corresponding norm-valued seminorm. The Hahn–Banach norm identity therefore gives the same bound for the norm of that term and of each difference of cutoffs, with one constant for all \(\ell\). The summable discarded terms make those differences Cauchy in every required compact derivative norm. Banach completeness supplies the limit. The fundamental theorem on a compact segment passes derivatives to the limit, so the limiting function is norm-smooth and has all the claimed differentiated bounds. This proves norm convergence, rather than merely weak convergence.

Take \(E=\mathcal L(K)\) and use the amplitude \(a(x,\eta)b(y,\xi)\) in that fixed order. Every derivative is a finite sum of ordered products and is bounded by the product of the appropriate operator norms. The original ordinary metric and pre-diagonal estimates O8–O9 consequently give, for every integer \(N\ge0\),
\[
 \begin{split}
 a\circ b&\in S^{r+t},\\
 a\circ b-\sum_{|\alpha|<N}
       \frac{(\partial_\xi^\alpha a)(D_x^\alpha b)}{\alpha!}
       &\in S^{r+t-N},\\
 a^\dagger-\sum_{|\alpha|<N}
       \frac{\partial_\xi^\alpha D_x^\alpha(a^*)}{\alpha!}
       &\in S^{r-N}.
 \end{split}
 \tag{HS4}
\]
All remainders have finite-seminorm operator-norm bounds. The adjoint uses norm-continuity of \(a\mapsto a^*\); its kernel has coefficient \(a(y,\xi)^*\), so the same conversion supplies the displayed sign and order.

For compact smooth symbols, norm Fubini identifies \(a\circ b\) with actual composition on Schwartz vectors and identifies \(a^\dagger\) by the Hilbert pairing. For general symbols insert the scalar cutoffs \(\chi(\epsilon x)\chi(\epsilon\xi)\) from O3. Their symbol seminorms are uniformly bounded and they converge locally in norm with every derivative. The proved multiplier estimates give bounded locally convergent product and adjoint symbols. For a fixed Schwartz vector, local convergence and dominated frequency integration give local convergence of every output derivative. One additional uniform output position weight bounds the tails outside a large ball, proving convergence in the full Schwartz topology. Uniform Schwartz operator bounds allow a varying intermediate input in the double product. Passing to the limit proves \( \operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(a\circ b)\) and the actual adjoint identity. The same tail argument proves continuity of these constructions for bounded symbol families converging locally smoothly in norm.

## H3. A dimension-independent packet bound

Choose the fixed scalar normalized Schwartz packet \(\phi\) in E25 and phase-space measure \(d\mu(q,p)=(2\pi)^{-n}dq\,dp\). Define
\(Vu(q,p)=\int u(x)\overline{e^{ip\cdot x}\phi(x-q)}\,dx\), a vector in \(K\). Hilbert Plancherel from H1 and Tonelli give exactly
\(\int\|Vu(Q)\|_K^2d\mu(Q)=\|u\|_{L^2(K)}^2\).
The vector synthesis integral is first defined on bounded compactly supported coefficients. Pairing it with a unit vector in \(L^2(K)\) and applying Cauchy–Schwarz gives norm at most one. Completeness extends synthesis, and polarization gives \(V^*V=I\). For a Schwartz input, integration by parts and the two Schwartz factors give rapid norm decay of \(Vu\) and reconstruction in every Schwartz seminorm.

The packet matrix \(M(Q,Q')\) is now an operator on \(K\). Its norm-convergent integral is E26 with the operator coefficient \(a(q+s,p'+t)\). The two integrations by parts with \((1-\Delta_s)^N(1-\Delta_t)^N\) differentiate at most \(4N\) times; every derivative of the scalar oscillation produces a polynomial absorbed by the fixed Schwartz factors. Taking operator norms inside the resulting absolute integrals yields
\[
 \|M(Q,Q')\|\le C_{n,N,\phi}p_{0,4N}(a)
       \langle q-q'\rangle^{-2N}
       \langle p-p'\rangle^{-2N},\qquad 2N>n .
 \tag{HS5}
\]
The same assertion holds with the maximum of bounded derivatives for a symbol not assigned an order. Both marginals of this scalar majorant are integrable. For a compact vector coefficient \(F\), the norm of \(\int M(Q,Q')F(Q')d\mu(Q')\) is bounded by the scalar integral of the majorant times \(\|F(Q')\|\). The complete scalar Schur proof E24 thus bounds the vector operator by \(C p_{0,4N}(a)\). Exhaustion and completeness give its extension to \(L^2(d\mu;K)\).

For Schwartz \(u,v\), norm-rapid packet reconstruction and HS5 justify both integrations and give \((Au,v)=(MVu,Vv)\). Thus \(A=V^*MV\) as distributions on this dense test space; no boundedness of \(A\) was assumed. We obtain the actual global \(L^2(K)\) bound with no factor depending on \(\dim K\).

For arbitrary real \(s,r\), H2 applied to the scalar weight multipliers gives an order-zero symbol for \(E_{s-r}AE_{-s}\). Its finitely many required seminorms are bounded by finitely many original seminorms of \(a\). Hence
\[
 \|Au\|_{s-r}\le C_{n,r,s}p_{r,J}(a)\|u\|_s .
 \tag{HS6}
\]
Density extends the operator to every \(H^s(K)\); simultaneous density from H1 makes these extensions distributionally compatible. In particular an order-\(2m\) symbol has quadratic form bounded by \(C p_{2m,J}(a)\|u\|_m^2\).

## H4. The moving probe with an operator coefficient

Retain the scalar \(B,\psi,U_{y,\eta,q}\) constructed and normalized in G4, with \(\int\psi=1\), even \(\psi\), and \(q(\eta)=\langle\eta\rangle^{1/2}\). For an operator-valued symbol \(b\), define \(\mathcal I_vb\) by the same scalar-kernel integral P29. P30 with \(\|b(y,\eta)\|\le p_{r,0}(b)\langle\eta\rangle^r\) proves absolute norm convergence, locally uniformly with every derivative. There is consequently an actual smooth operator-valued function, regardless of whether \(\mathcal L(K)\) is separable.

For completeness, the full cancellation estimate transfers in operator norm as follows. \(T_v=\mathcal I_v-(\int v)I\) is linear with scalar kernel. For each unit \(\ell\in\mathcal L(K)'\), norm convergence gives \(\ell(T_vb)=T_v(\ell b)\). The scalar G5 proof, including its finite-seminorm differentiated remainders, bounds the latter uniformly in \(\ell\). The norm identity then gives
\[
 \|\partial_\xi^\alpha\partial_x^\beta T_vb(x,\xi)\|
   \le C p_{r,J}(b)\langle\xi\rangle^{r-1-|\alpha|}.
 \tag{HS7}
\]
This applies to every even Schwartz \(v\). In particular the exact derivative identities P42 remain identities of norm-valued integrals. Each frequency derivative either differentiates \(b\) or inserts \(F_j=q^{-1}\partial_jq\in S^{-1}\); the resulting kernels \(\mathcal L^kv\) are even. Thus every derivative in HS7 has the stated full one-order improvement, including the moving-scale mass correction. This argument uses the complete linear scalar estimate, not an entrywise estimate with a dimension-dependent constant.

If \(b=b^*\ge0\), put \(b_+=\mathcal I_\psi b\). Scalar probe operators commute with a fixed bounded coefficient. For \(u\in\mathcal S(K)\), the norm-valued version of P32 is justified by Fourier inversion and has arbitrary product decay in \(\langle y\rangle,\langle\eta\rangle\) in \(L^2_t(K)\): on the fixed \((t,\theta)\) support of the bump, \(|\eta+q\theta|\ge|\eta|/2\) at large \(\eta\); integration by parts in \(\theta\) gives arbitrary powers of \(\langle t+qy\rangle^{-1}\). Its \(q\) factors grow polynomially and are absorbed by stronger Schwartz decay of \(\widehat u\). As \(q\ge1\), this gives the stated product decay also in \(y\); bounded \(\eta\) is handled by the same integrations. Therefore the following integral converges absolutely:
\[
 (\operatorname{Op}(b_+)u,u)
   =\iint (b(y,\eta)BU_{y,\eta,q}^*u,
                         BU_{y,\eta,q}^*u)_{L^2(K)}\,dy\,d\eta
   \ge0 .
 \tag{HS8}
\]
To prove the equality, first use \(u=\Pi_Mu\) and a compact parameter cutoff. Expand the finite Hilbert pairing; the scalar kernel identity P26 and norm Fubini give the equality for each pair of scalar components. This is an identity, without a finite-matrix norm bound. Remove the parameter cutoff using P30 on the symbol side and the product decay just proved on the quadratic-form side. Finally \(\Pi_Mu\to u\) in the Schwartz topology by H1. Its seminorms are uniformly bounded, so the same decay gives an integrable majorant; the scalar-kernel integrals and HS3 converge as well. Dominated convergence proves HS8 for the original \(u\). There is no operator-norm approximation of \(b\) by finite-rank symbols.

## H5. The full lower bound and time-dependent families

Let \(a\in S^{2m+1}(\mathcal L(K))\) have nonnegative Hermitian part. Write \(a=b+ic\), where \(b=(a+a^*)/2\ge0\) and \(c=(a-a^*)/(2i)=c^*\). HS7 gives \(b-b_+\in S^{2m}\), and HS8 gives the positive part of its quadratic form. H2 also gives \(\operatorname{Op}(c)-\operatorname{Op}(c)^*\in\operatorname{Op}(S^{2m})\). Since the pairing is linear in the first entry,
\[
 \operatorname{Re}(i\operatorname{Op}(c)u,u)
  =\frac i2\big((\operatorname{Op}(c)-\operatorname{Op}(c)^*)u,u\big).
 \tag{HS9}
\]
The order-\(2m\) quadratic bound from H3 controls both errors. We have proved
\[
 \operatorname{Re}(\operatorname{Op}(a)u,u)
       \ge-C_{m,n}p_{2m+1,J}(a)\|u\|_m^2 .
 \tag{HS10}
\]
The constant uses finitely many operator-norm seminorms and has no dimension factor. For an order-one symbol with Hermitian part bounded below by \(-CI_K\), apply HS10 at \(m=0\) to \(a+CI_K\). Schwartz density in \(H^1(K)\) and HS6 extend the inequality to that exact energy domain.

Suppose \(a(t)\) is bounded in the global ordinary symbol class and converges locally smoothly in norm as \(t\to t_0\). For a Schwartz vector, dominated frequency integration gives local convergence of each output derivative; the uniform stronger Schwartz estimate from H2 bounds every weighted tail. This proves Schwartz convergence. HS6 and Schwartz approximation then prove strong continuity \(A(t):H^s(K)\to H^{s-r}(K)\) on each fixed input. The same holds for adjoints and ordered remainders by H2's bounded local convergence. For a varying continuous vector, split its difference into the fixed-input difference and the uniformly bounded image of its vector difference. These statements establish exactly the strong time continuity used by the evolution theorem.

## H6. The finite-dimensional algebra used in the examples

A Hermitian matrix has a unitary diagonalization by the following compact argument. Its real Rayleigh quotient attains a maximum on the unit sphere. Differentiating along every orthogonal direction, and then along that direction multiplied by \(i\), shows that a maximizing unit vector is an eigenvector. Its orthogonal complement is invariant by Hermitian symmetry. Induction supplies an orthonormal eigenbasis, with real eigenvalues. For a positive definite matrix all eigenvalues are positive; taking their positive square roots gives its Hermitian positive square root, inverse, and the exact smallest and largest eigenvalue norm bounds. This also applies to \(M^*M\), proving the singular-value assertions used for a finite matrix \(M\).

The exponential of a fixed matrix \(a\) is defined by its power series. The bound \(\|a^j\|/j!\le\|a\|^j/j!\) gives absolute uniform convergence, with every derivative on compact time intervals. Thus \(M(t)=e^{ta}\) solves \(M'=aM\), \(M(0)=I\), and differentiating \(e^{ta}e^{-ta}\) proves invertibility. Multilinearity of the determinant in rows shows \( (\det M)'=(\operatorname{tr}a)\det M\): in the derivative of row \(j\), only its coefficient \(a_{jj}\) contributes, since every other summand repeats another row. The scalar exponential equation therefore gives \(\det e^{ta}=e^{t\operatorname{tr}a}\), without assuming triangularization of a general complex matrix. For \(2\times2\) matrices, Cauchy–Schwarz applied to the two columns gives \(|\det M|\le\|M\|^2\); equivalently the product of the two singular values is \(|\det M|\).

These proofs receive precisely the classical \((\rho,\delta)=(1,0)\) Hilbert-coefficient scope of AN-03's *Positivity through a moving family of scalar probes*, Sections 1–6. They use the already included complete scalar proofs and add the norm-valued limits, packet action, positivity identity and dense vector tests explicitly. Hörmander III, §23.1, supplies the scalar energy and existence antecedent for the receiving lesson; it is not used as a substitute for any proof here.

*Written by GPT-6 Astra (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Original connecting text: CC0 1.0; linked components retain their stated licences.*
