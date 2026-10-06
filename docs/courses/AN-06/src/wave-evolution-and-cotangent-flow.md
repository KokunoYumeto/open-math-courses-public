# Wave evolution and cotangent flow

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Original exposition: CC0.*

**Working question: Which return is visible in an evolution kernel?** A classical particle may revisit its position with a different covector. A diagonal wave kernel tests position return, while taking the spatial trace imposes the full covector return needed for its singularities. Separating these observations first explains why counting estimates later use a phase-space condition rather than a picture of a closed path alone.

An eigenvalue is a frequency of an evolution. Taking the Fourier transform of the spectral measure produces a wave kernel, and its singularities reveal where the classical Hamiltonian flow travels. This lesson constructs that connection for a scalar first-order elliptic operator on a closed manifold. The construction also explains why a smooth error in an approximate evolution does not alter its singularities.

The freely accessible construction in Hörmander's 1968 spectral-function article [HS, Sections 2–3] supplies the local phase and successive amplitude equations. The original articles *Fourier integral operators I* [FI] and *II* [FII] supply their classical invariant symbols, composition and transport. The phase and principal-symbol proofs are now supplied by the programme reading below. The graph-composition and adjoint proofs are now supplied by the subsequent programme reading. The scalar-transport and qualified-pullback proofs are supplied by the two subsequent programme readings. Guillemin and Sternberg [GS, Section 8.7.5] explain the corresponding semiclassical transport; Wunsch [W, Sections 4.1 and 6] treats the metric half-wave construction. The operator prerequisites are the real Sobolev calculus in [Classical scalar symbols, summation and regularity](../providers/analysis/classical-scalar-calculus.md#finite-symbol-calculus), compact Sobolev inclusions in [Compact Sobolev inclusion and elliptic Fredholm maps](../providers/analysis/classical-scalar-calculus.md#compact-sobolev-inclusion), and the complete bundled [Compact positive inverses and diagonal domains](../providers/analysis/compact-spectrum-domains.md#compact-inverse-domains). The latter supplies the generic compact positive eigenbasis, the exact second-moment inverse domain and every diagonal multiplier domain; its full Hilbert-space input is Lemma 6.1 and Theorem 6.2 of the linked current programme proof. The PDE inverse and compact Sobolev inclusion are proved separately below.


Read the finite scalar calculus and its summation proof first, then [Phase geometry, stationary phase and the Maslov symbol](../providers/analysis/phase-geometry-and-stationary-phase.md#phase-foundations). Sections 1–9 of that reading prove the parameter-dependent quadratic reduction and Gaussian remainder, construction and equivalence of nondegenerate homogeneous phases including caustics, the normalized Maslov symbol and its realization/recovery, and the wavefront implication of a nonzero symbol. Next read [Transverse composition and graph operators](../providers/analysis/transverse-composition-and-graph-operators.md#transverse-composition), whose Sections 1–9 prove transverse composition, normalized symbol contraction, adjoints, graph Sobolev mapping and ordered Egorov. Then read [Wavefront-qualified pullback and restriction of phases](../providers/analysis/wavefront-qualified-pullback.md#qualified-pullback), which proves arbitrary smooth-map pullback, its convergence and the precise transverse restriction rule, and [Scalar transport and finite action on a phase](../providers/analysis/scalar-transport-and-phase-action.md#scalar-transport), which proves every finite phase-action remainder and the invariant half-density transport formula at caustics. Free references are comparisons, not substitutes for proofs. In a clean composition with excess zero, the required rank condition is transversality, and a connected zero-dimensional matching fiber is one point. The subsequent [Clean composition with positive excess](../providers/analysis/clean-composition-with-excess.md#clean-composition) proves the general proper clean theorem, including the order increase by half the excess and the normalized principal-symbol fiber integral. Its homogeneous reduction, density quotient and Maslov calculation are explicit programme proofs; the graph applications below still have excess zero.

The smooth-flow argument required here is written in Section 3, before its use. The later [Hamilton trajectories under a long-range force](hamilton-trajectories-under-a-long-range-force.md) gives a separate long-range application. Smooth coordinate inverses and finite smooth partitions are provided by [Coordinate inverses, integration and surface measure](../providers/analysis/coordinate-inverses-and-integration.md). The [graph Sobolev and ordered Egorov section](../providers/analysis/classical-scalar-calculus.md#graph-sobolev-mapping-and-ordered-egorov) links the actual graph-composition and mapping proofs. Fourier inversion and Plancherel are proved in [Fourier facts](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The compact fiber-integration argument at the trace calculation below is proved there after verifying the general pullback hypotheses.

Throughout, \(X\) is a compact connected smooth manifold without boundary, of dimension \(n\geq2\). We act on scalar half densities, use \(D=-i\partial\), and take the Hilbert pairing linear in its first argument. Symbols are classical \(S_{1,0}\) symbols with a step-one homogeneous expansion.

## 1. The closed operator and its frequencies

A half density has a local expression \(u(x)|dx|^{1/2}\). Its squared absolute value is a density, so
\[
\|u\|_2^2=\int_X |u|^2
\]
requires no choice of volume form or orientation. If a scalar operator \(Q\) is symmetric in \(L^2(X,\rho)\) for a smooth positive density \(\rho\), the unitary map \(f\mapsto f\rho^{1/2}\) changes it to an operator on half densities with the same eigenvalues.

Let
\[
P\in\Psi^1_{\mathrm{cl}}(X;\Omega^{1/2})
\]
be elliptic and symmetric on smooth half densities. Its principal symbol \(p\) is real and homogeneous of degree one. The cosphere bundle is connected: its base is connected and each fiber \(S^{n-1}\) is connected. Thus the nowhere-zero \(p\) has one sign. We choose the sign of \(P\) so that
\[
p(x,\xi)>0,\qquad \xi\neq0.
\tag{1}
\]
This choice concerns the principal symbol; finitely many eigenvalues of \(P\) may still be negative.

**Proposition 1.1.** The maximal realization
\[
\mathcal D(P)=\{u\in L^2:Pu\in L^2\text{ distributionally}\}
\]
is self-adjoint, has domain \(H^1(X;\Omega^{1/2})\), and is the closure of its smooth restriction. It is bounded below and has a complete orthonormal basis of smooth eigenvectors. Each eigenspace is finite dimensional, and its eigenvalues tend to \(+\infty\).

**Proof.** The elliptic inverse and Sobolev mapping give
\[
\|u\|_{H^1}\leq C(\|Pu\|_2+\|u\|_2).
\tag{2}
\]
They also give \(Pu\in L^2\Rightarrow u\in H^1\) for an initially distributional \(u\). The reverse inclusion follows from \(P:H^1\to L^2\). Smooth density in \(H^1\) and (2) identify the graph closure. In particular the maximal realization is closed and symmetric.

If \(v\) lies in its Hilbert adjoint domain, the smooth-test adjoint identity says that \(Pv\in L^2\) distributionally. Hence \(v\in H^1\), and the two domains coincide. This proves self-adjointness without adding an independent domain condition.

Quantize \(p^{1/2}\) as a scalar classical elliptic \(Q\) of order \(1/2\). The principal-symbol and adjoint rules give \(Q^*Q-P\in\Psi^0\). The elliptic estimate for \(Q\) therefore gives, first on smooth inputs,
\[
\|u\|_{H^{1/2}}^2
\leq C\{\|Qu\|_2^2+\|u\|_2^2\}
\leq C\{(Pu,u)+C'\|u\|_2^2\}.
\tag{3}
\]
All terms extend to \(H^1\). In particular \(P\) has a finite lower bound.

Choose \(c\) so that \(A=P+c\geq I\). Its range is closed because \(\|Au\|_2\geq\|u\|_2\). It is dense because its orthogonal complement is \(\ker A^*=0\), so \(A\) is onto. Estimate (2) makes \(A^{-1}:L^2\to H^1\) bounded. The compact inclusion \(H^1\to L^2\) makes this inverse a compact positive self-adjoint injective operator.

Apply the exact compact positive spectral argument from the stated prerequisite to \(A^{-1}\). Its kernel is zero, so its positive eigenvectors form a complete orthonormal basis \(\phi_j\), with eigenvalues \(\beta_j\downarrow0\) and finite multiplicities. The argument concerns any compact positive Hilbert-space operator; the differential expression of its earlier application is unnecessary. Consequently
\[
P\phi_j=\lambda_j\phi_j,\qquad
\lambda_j=\beta_j^{-1}-c\longrightarrow+\infty.
\tag{4}
\]
The eigenvalue equation and elliptic regularity raise the regularity by one order repeatedly, so every \(\phi_j\) is smooth. The same prerequisite's closed graph argument gives the exact second-moment domain in this basis, and identifies every recursive integer power with its corresponding moment domain. ∎

The eigensystem defines
\[
E(t)u=\sum_j e^{-it\lambda_j}(u,\phi_j)\phi_j.
\tag{5}
\]
It is a strongly continuous unitary group on \(L^2\), and
\[
(D_t+P)E(t)=0,\qquad E(0)=I.
\tag{6}
\]
For completeness, its Sobolev assertions require no pseudodifferential fractional-power theorem. The operator \(A^k\) is elliptic of order \(k\), and its recursive domain is \(H^k\). Induction proves this: \(Au\in H^{k-1}\) gives \(u\in H^k\) by the elliptic inverse, and the mapping theorem gives the converse. Its graph norm is equivalent to \(H^k\). Formula (5) preserves the \(A^k\) moment norm, so \(E(t)\) is uniformly bounded on each nonnegative integer Sobolev space. Duality gives negative integers. The [two-endpoint Sobolev proof, (FC18)–(FC19)](../providers/analysis/classical-scalar-calculus.md#two-endpoint-sobolev), now gives every real order, with bounds uniform in time: its annular Fourier blocks have a summable geometric bound, and its finite-atlas reassembly applies to these actual manifold norms.

These extensions agree on distributions. Smooth density and uniform bounds give strong continuity on each \(H^s\). Differentiation of the series on smooth inputs, followed by its moment bounds, gives
\[
\partial_t^rE(t)=(-iP)^rE(t):
H^s\longrightarrow H^{s-r}.
\tag{7}
\]
Thus \(E\) also acts continuously on smooth half densities and distributions.

## 2. Spectral kernels with polynomial growth

Let \(\Pi_\lambda\) be the projection onto the span of the \(\phi_j\) with \(\lambda_j\leq\lambda\). It has finite rank and smooth kernel
\[
e(x,y,\lambda)=\sum_{\lambda_j\leq\lambda}
\phi_j(x)\otimes\overline{\phi_j(y)}.
\tag{8}
\]
On the diagonal this is a density. Its integral is the counting function \(N(\lambda)\).

**Proposition 2.1.** For a differential operator \(B\) of order \(\mu\) on \(X\times X\), acting on these kernel coefficients,
\[
|Be(x,y,\lambda)|\leq C_B(1+\lambda)^{n+\mu},
\qquad \lambda\geq1.
\tag{9}
\]
In particular \(N(\lambda)=O(\lambda^n)\).

**Proof.** In a fixed compact coordinate chart, Fourier Cauchy–Schwarz gives the scaled point estimate
\[
|\partial^\alpha v(x)|^2
\leq C r^{-n-2|\alpha|}
\sum_{\ell=0}^k r^{2\ell}\|v\|_{H^\ell}^2,
\quad 0<r\leq1,\quad k>|\alpha|+n/2.
\tag{10}
\]
Here \(v\) has a fixed compact chart support. Indeed insert the weight \((1+r^2|\xi|^2)^k\) in its differentiated inverse Fourier integral. The reciprocal integral with numerator \(|\xi|^{2|\alpha|}\) equals a finite constant times \(r^{-n-2|\alpha|}\); expanding the positive weight controls its other factor by the displayed derivative norms. Smooth chart cutoffs and finitely many charts give the corresponding local estimate for a half density.

For \(u=\Pi_\lambda u\), the integer-power bounds above imply
\(\|u\|_{H^\ell}\leq C_\ell(1+\lambda)^\ell\|u\|_2\).
Take \(r=(1+\lambda)^{-1}\) in (10). Derivative evaluation on this finite-dimensional spectral space has norm at most
\(C(1+\lambda)^{n/2+|\alpha|}\). By finite-dimensional Hilbert representation, its squared norm is
\[
\sum_{\lambda_j\leq\lambda}
|\partial^\alpha\phi_j(x)|^2
\leq C(1+\lambda)^{n+2|\alpha|}.
\tag{11}
\]
Cauchy–Schwarz in \(j\) now bounds each mixed derivative of (8) by
\(C(1+\lambda)^{n+|\alpha|+|\beta|}\).
Every \(B\) is a finite local sum of such derivatives with bounded smooth coefficients. This proves (9). Integrating the diagonal bound over the finite atlas proves the counting bound. ∎

It follows that the kernel of (5) is a distribution in \(t,x,y\):
\[
K_E(t,x,y)=\sum_j e^{-it\lambda_j}
\phi_j(x)\otimes\overline{\phi_j(y)}.
\tag{12}
\]
Pairing in \(t\) with a compact smooth test produces a rapidly decreasing function of \(\lambda_j\). Estimates (9) and the counting bound make the resulting differentiated spatial series absolutely convergent. The same estimates make it continuous, with values in distributions in \(t\), under every spatial derivative. In particular (12) is precisely the Fourier transform, with phase \(e^{-it\lambda}\), of the discrete spectral measure.

## 3. A flow whose time direction never stops

**Local flow and preservation of the canonical forms.** We give the smooth-flow argument used here before applying it. On a compact coordinate ball, a smooth vector field $F$ has bounded size and derivative, say $M,L$. Choose $T>0$ so that $TM$ stays within the chosen ball and $TL<1$. For initial data in a smaller ball the integral map $z(t)=z_0+\int_0^t F(z(s))\,ds$ preserves a closed set of continuous paths. Its successive iterates have geometrically summable differences in the uniform norm. The uniform limit is a continuous path satisfying the integral equation, hence a differentiable solution. The contraction inequality proves uniqueness, for both positive and negative time. The uniform path space is complete because uniform limits of continuous paths are continuous.

Dependence on initial data follows from the same estimate. More generally, iterating the integral inequality $b(t)\le a+L\int_0^t b(s)\,ds$ gives $b(t)\le ae^{L|t|}$: the successive integral terms are $aL^j|t|^j/j!$, and the final remainder tends to zero since $b$ is bounded on the compact interval. The prospective first derivative $J$ solves $J=I+\int_0^t DF(z(s))J(s)\,ds$; its series converges by the same factorial bound. For an initial displacement $h$, the fundamental theorem on the segment between two paths gives
$F(z_h)-F(z)=DF(z)(z_h-z)+R_h(z_h-z)$ with $\sup\|R_h\|\to0$, by uniform continuity of $DF$. Subtract the equation for $Jh$ and divide by $|h|$. The integral inequality just proved forces the remainder to zero uniformly. Thus $J$ is the actual initial-data derivative and is continuous by its integral equation. Apply this argument to the coupled system for $(z,J)$: its vector field is smooth, so its solution is continuously differentiable by the same argument. This gives second derivatives of $z$. Iterating the coupled systems for its finitely many jets proves every derivative, with bounds on compact intervals. Parameters are additional variables with zero time derivative, so the argument also proves smooth parameter dependence. Uniqueness gives the flow law and the inverse at negative time. A trajectory contained in a compact subset extends past every finite endpoint: its bounded derivative gives a limit there, and the local construction restarts from that limit. Finitely many charts make these assertions valid on a manifold.

For a Hamiltonian $p$, conservation follows directly from $dp(H_p)=p_x\cdot p_\xi-p_\xi\cdot p_x=0$. Put $z=(x,\xi)$ and $J_0=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$, so the vector field is $J_0p''$ at the derivative level. If $M(t)$ is its flow derivative and $S=p''$ along a trajectory, then $M'=J_0SM$ and $S^T=S$. Direct differentiation gives $(M^TJ_0M)'=M^T(S-S)M=0$. This proves symplectic preservation in canonical coordinates, and hence globally by coordinate change. For a degree-one $p$, its Hamilton equations and uniqueness show that the flow commutes with $(x,\xi)\mapsto(x,r\xi)$ for $r>0$. The radial field $R=\xi\partial_\xi$ is therefore preserved. With $\omega=\sum dx_j\wedge d\xi_j$ and $\alpha=\sum\xi_jdx_j=-\iota_R\omega$, preservation of $R$ and $\omega$ implies preservation of the Liouville form $\alpha$. These calculations supply the conservation and canonical-form statements used next.

Let \(\chi_t=\exp(tH_p)\), with
\[
H_p=\sum_\ell
(p_{\xi_\ell}\partial_{x_\ell}
-p_{x_\ell}\partial_{\xi_\ell}).
\tag{13}
\]
The level \(p=1\) is compact, since \(p\) is positive elliptic and homogeneous. The flow preserves \(p\), so it exists for every real \(t\) on this level. Homogeneity extends it to the whole punctured cotangent bundle. With any fixed cotangent norm,
\[
|\xi|\asymp|\eta|
\quad\text{if }(x,\xi)=\chi_t(y,\eta),
\tag{14}
\]
with constants independent of \(t\). Both norms are comparable with the same conserved value of \(p\).

In kernel covectors define
\[
\Lambda=\{(t,x,y;\tau,\xi,-\eta):
(x,\xi)=\chi_t(y,\eta),\
\tau=-p(y,\eta)\}.
\tag{15}
\]

**Lemma 3.1.** This is a closed embedded conic Lagrangian in
\(T^*(\mathbb R\times X\times X)\setminus0\).
Neither spatial covector nor its time covector vanishes. Restricting at a fixed time gives the twisted graph of \(\chi_t\).

**Proof.** Parameters \((t,y,\eta)\) give an embedding with inverse the displayed time and input covector. Conservation, positivity and (14) exclude any nonzero limiting covector with a zero spatial component, and prevent escape in its remaining parameters over a compact cotangent set. This proves closure.

Homogeneity of the Hamilton flow makes the relation conic. Each \(\chi_t\) preserves the symplectic form and, by homogeneity, the Liouville form on the punctured cotangent bundle. Euler's identity gives \(\xi\cdot p_\xi=p\). Consequently the pullback to (15) of the full tautological form is
\[
-p\,dt+\xi\cdot dx-\eta\cdot dy=0.
\tag{16}
\]
For fixed \(t\) the last two terms cancel by Liouville invariance; their derivative in the time parameter is \(p\,dt\), which cancels the first term. Thus the pulled-back symplectic form vanishes. The parameter dimension is \(2n+1\), half the cotangent dimension, so the relation is Lagrangian. All its stated nonvanishing properties follow from \(p>0\). ∎

The lifted characteristic field is \(W=\partial_t+H_p\). On \(\Lambda\) it advances \(t\) while keeping the initial \((y,\eta)\) fixed. Every one of its trajectories meets \(t=0\) exactly once. Periodic motion in \(X\) does not make this time coordinate periodic.

## 4. The symbol facts needed for an approximate evolution

The following statements retain the full required scalar FIO scope. The phase, summation, principal-symbol, transverse-composition, scalar-transport and qualified-pullback assertions have the programme proofs linked below. 

- On an ambient manifold of dimension \(d\), an \(I^m\) kernel has principal symbol of order \(m+d/4\) in the Maslov-valued half-density line of its Lagrangian. Every such symbol class is realized, and a zero principal class lowers the kernel order by one.
- Support-preserving asymptotic sums of amplitudes realize successive kernel orders tending to minus infinity. A remainder of every negative order is smooth.
- Proper connected clean composition with excess zero adds the kernel orders and composes the corresponding symbols. An identity-graph kernel of order \(m\) is a pseudodifferential operator of order \(m\).
- For a classical scalar half-density operator \(L\) of order one whose principal symbol \(h\) vanishes on the relation, the product retains order \(m\), with symbol
\[
\sigma(LV)=\frac1i\mathcal L_{H_h}\sigma(V)
+h_{\mathrm{sub}}\sigma(V).
\tag{17}
\]
Here
\(h_{\mathrm{sub}}=h_0+(i/2)\sum h_{z_\ell\zeta_\ell}\)
in left-symbol coordinates.


**Phase and principal-symbol proofs.** Use the unshifted local half-density normalization
\[
 (2\pi)^{-(d+2N)/4}\int e^{i\phi(z,\theta)}a(z,\theta)\,d\theta\,|dz|^{1/2},
 \qquad a\text{ of order }m+\frac{d-2N}{4}.
\]
The full programme [phase-geometry proof, Section 5](../providers/analysis/phase-geometry-and-stationary-phase.md#phase-geometry) shows that the critical manifold \(C_\phi=\{\phi_\theta=0\}\) maps locally diffeomorphically to its conic Lagrangian by \((z,\theta)\mapsto(z,\phi_z)\). It constructs a minimal mixed-coordinate phase at every Lagrangian point without a constant-rank assumption. [Section 6](../providers/analysis/phase-geometry-and-stationary-phase.md#phase-equivalence) proves exact homogeneous fiber equivalence after eliminating nondegenerate quadratic variables, including the parameter dependence.

The quadratic calculation, with its full proof in [Sections 1–3](../providers/analysis/phase-geometry-and-stationary-phase.md#parameter-morse), is
\[
 \int e^{iR v^THv/2}b(v)\,dv
 =(2\pi/R)^{k/2}e^{i\pi\operatorname{sgn}H/4}|\det H|^{-1/2}
 \left\{\sum_{j<L}\frac{(i/2R)^j}{j!}(Q_H^jb)(0)+O(R^{-L})\right\},
\]
where \(Q_H=\sum(H^{-1})_{jl}\partial_{v_j}\partial_{v_l}\). The proof obtains the Gaussian by regularization and an ordinary differential equation, supplies a smooth quadratic reduction and bounds every differentiated finite remainder. For parameter-dependent nonquadratic phases the symbol bounds apply after removing the critical-value exponential.

Let \(d_\phi\) be the critical density obtained by dividing \(|dz\,d\theta|\) by \(|d\phi_\theta|\). In the unshifted normalization above the Maslov coefficient is
\[
 s_\phi=e^{i\pi N/4}a_q\sqrt{d_\phi},
 \qquad q=m+(d-2N)/4.
\]
The extra phase is required for the fourth-root transition convention. [Section 7](../providers/analysis/phase-geometry-and-stationary-phase.md#maslov-line) proves the density transformation and the locally constant integer cocycle
\[
 c_{jk}=\tfrac12\bigl[(\operatorname{sgn}\phi_{k,\theta\theta}-N_k)
                  -(\operatorname{sgn}\phi_{j,\theta\theta}-N_j)\bigr],
 \qquad s_j=i^{c_{jk}}s_k.
\]
Equivalently one may put \(e^{-i\pi N/4}\) into the phase-integral normalization and use a rephased amplitude, as in [FI, (3.2.14)–(3.2.15)]. These conventions must not be mixed. The critical half density has degree \(N/2\), so the symbol has degree \(m+d/4\). The identity-graph frame is fixed by the actual identity kernel: with phase \((x-y)\cdot\eta\), the unshifted integral is precisely ordinary left quantization.

[Section 8](../providers/analysis/phase-geometry-and-stationary-phase.md#principal-symbol-proof) proves realization by a homogeneous retraction and supported partition, lowers a vanishing critical amplitude by integration by parts, and proves the converse by an explicit transverse oscillatory test. It establishes both directions of the principal-symbol correspondence modulo one lower order. [Section 9](../providers/analysis/phase-geometry-and-stationary-phase.md#phase-wavefront) proves Fourier wavefront inclusion and shows that a nonzero principal symbol produces a wavefront point. Thus these phase and symbol assertions use actual earlier programme proofs, and the additional graph-composition proof is given next. The scalar-transport and qualified-pullback proofs are applied below with their exact hypotheses and normalization.

Asymptotic summation can be constructed directly. For amplitudes \(a_j\) of orders \(q-j\), retain \(a_0\) separately and, for \(j\geq1\), choose radii \(R_j\) tending sufficiently rapidly to infinity and a radial cutoff \(\chi\) vanishing near zero and equal to one outside a larger ball. Choose \(R_j\) so that the first \(j\) symbol seminorms, on the first \(j\) compact coordinate sets, of
\(\chi(\theta/R_j)a_j\) in order \(q-j/2\) are at most \(2^{-j}\). Such a choice is possible because the original order is lower by \(j/2\); derivatives of the cutoff satisfy the same estimates on its annulus. The sum is locally finite in bounded frequency sets. Its tail starting at \(j\geq2N\) converges in order \(q-N\), and its finitely many intervening terms already have the required lower orders. Removing the cutoff from any fixed finite prefix changes only a smooth compact-frequency amplitude. This proves the full asymptotic expansion with all derivatives. Fixed conic support and a locally finite phase partition preserve support. An amplitude in every negative order has an absolutely convergent integral after any prescribed number of base derivatives, hence a smooth kernel.

**Transverse composition and adjoints.** The complete programme proof is [Transverse composition and graph operators, Sections 1–7](../providers/analysis/transverse-composition-and-graph-operators.md#transverse-composition). It first proves smooth-input and distributional actions, so the cutoff kernel product converges to the actual operator product. For phases \(\phi_1(x,y,\theta)\) and \(\phi_2(y,z,\sigma)\), transverse matching is precisely the full-rank condition for
\((\phi_{1,\theta},\phi_{2,\sigma},\phi_{1,y}+\phi_{2,y})\).
A proper injective matching projection gives the composed Lagrangian, and its immersion is proved by the symplectic orthogonality argument there. The incomparable-frequency part is smooth by (G6)–(G7), with every differentiated tail estimated. On the comparable-frequency part, the homogeneous variables
\[
\omega=(ry,\theta,\sigma),\qquad r=(|\theta|^2+|\sigma|^2)^{1/2}
\]
give \(N=N_1+N_2+\dim Y\) and amplitude \(r^{-\dim Y}a_1a_2\), hence precisely the order \(m_1+m_2\). Both critical-density Jacobians are retained in (G10)–(G11). In our unshifted convention the combined phase frame has
\[
 s_1\star s_2=e^{i\pi\dim Y/4}\mu_D(s_1\otimes s_2),
\]
where \(\mu_D\) is the explicitly proved half-density contraction over the matching equations. The phase-transition proof makes this intrinsic. The adjoint has phase \(-\phi\) with the base variables swapped and coefficient \(i^N\overline{s_\phi}\) in those paired frames, as proved in (G14). These factors preserve the identity-graph symbol and ordinary pseudodifferential normalization. [Sections 8–9](../providers/analysis/transverse-composition-and-graph-operators.md#graph-sobolev) give every real graph Sobolev shift, elliptic graph inverses modulo smooth kernels and the ordered Egorov rule. Hamiltonian graphs have unique transverse matching; their actual compact-time supports provide the properness used here. No positive-excess composition is inferred.

**Scalar transport with finite remainders.** The complete argument is [Scalar transport and finite action on a phase, Sections 1–5](../providers/analysis/scalar-transport-and-phase-action.md#invariant-transport-formula). Its (T1) makes the exact change from the composed phase to a bilinear phase and applies the proved quadratic remainder estimate, giving a finite expansion with an $S^{r+q-L}$ remainder after $L$ terms, including all parameter derivatives. At an arbitrary Lagrangian point it constructs an actual base coordinate change making frequency a local coordinate, then uses $\phi=z\cdot\zeta-H(\zeta)$ and reduces the amplitude to $a_0(\zeta)$ to every order. No product-compatible normal coordinates through a caustic are assumed.

Writing $h=\sum_j(z_j-H_{\zeta_j})h_j$, integration by parts gives the leading amplitude

\[
 h_0a_0-\frac1i\sum_j\bigl(h_j\partial_{\zeta_j}a_0
                       +(\partial_{\zeta_j}h_j)_{z\ \mathrm{fixed}}a_0\bigr)
 \quad\text{on }z=H_\zeta.
\]

The vector field there is $V=-\sum_jh_j^c\partial_{\zeta_j}$. Formulas (T7)–(T8) distinguish its total derivative along the critical graph from the fixed-base derivative above. Substitution gives $(1/i)(V+\tfrac12\operatorname{div}V)+h_{\mathrm{sub}}$, proving (17). The same reading proves the coordinate rule for the half-density derivative and uses the already proved invariant subprincipal formula (FC9)–(FC15). This establishes the statement intrinsically, with all lower remainders, also at caustics. Its (T12) supplies the inhomogeneous transport solution used below. The free comparison is [FII, Sections 5.2–5.3]; the written programme calculation is the proof used here.

Time restriction needs the exact order shift. The kernel of evaluation at \(t=t_0\) is locally
\(\delta(s-t_0)\delta(z-z')\), with \(z=(x,y)\).
It is conormal of codimension \(2n+1\) in ambient dimension \(4n+1\), so its order is
\[
\frac{2n+1}{2}-\frac{4n+1}{4}=\frac14.
\tag{18}
\]
Time pullback has no forbidden pure-time covector, because \((\xi,\eta)\neq0\). Its critical equations are transverse on this relation: in the coordinates \((t,y,\eta)\), fixing time has independent differential \(dt\). Equivalently, the time-evaluation composition has a single matching point and excess zero. The complete [qualified-pullback proof, (R1)–(R12)](../providers/analysis/wavefront-qualified-pullback.md#qualified-pullback), constructs the distributional restriction and proves equality with the restricted phase integral by smooth cutoff convergence. Its transverse restriction proof lowers the ambient dimension by one while leaving the number of phase variables and amplitude order unchanged; its normalized amplitude is multiplied by $(2\pi)^{-1/4}$. Hence the kernel order increases by \(1/4\), in agreement with (18), and gives
\[
V\in I^{-1/4}(\Lambda)
\quad\Longrightarrow\quad
V(t_0)\in I^0(\operatorname{graph}\chi_{t_0}).
\tag{19}
\]
On compact time intervals all local support and matching conditions are proper. At \(t=0\), the restricted relation is the identity graph, so the restricted symbol supplies the ordinary order-zero principal symbol. For the explicit smooth phase families here, [the joint normalization in (G18)](../providers/analysis/transverse-composition-and-graph-operators.md#joint-parameters) fixes its constant as well: passing from the joint section to the fixed-time section removes \((2\pi)^{1/4}|dt|^{1/2}\). The order calculation alone would not determine that factor.

To use (17), the partial operator \(P_x\) requires care: its symbol is not an ordinary symbol in all joint frequencies near the axis \(\xi=0\). The following elementary localization resolves this.

**Lemma 4.1.** Microlocally on \(\Lambda\), the action of \(D_t+P_x\) on its Lagrangian kernels agrees, up to a smooth remainder, with an ordinary joint scalar pseudodifferential operator having principal symbol \(\tau+p(x,\xi)\) and subprincipal symbol \(p_{\mathrm{sub}}(x,\xi)\).

**Proof.** On a compact normalized portion of $\Lambda$, (14) and positivity give $|\xi|\asymp|\eta|+|\tau|$. Write $z=(t,x,y)$ and $\omega=(\tau,\xi,\eta)$. Choose an ordinary joint order-zero cutoff operator $C=c(z,D_z)$, with full symbol equal to one on a conic neighborhood of that portion of $\Lambda$ and supported where $|\xi|\ge\epsilon|\omega|$ at high frequency. Low frequencies are smoothly cut off. We first show that $u-Cu$ is smooth for a phase kernel $u$ localized to this portion.

Near its phase-critical set, the nonzero joint phase derivative satisfies $|\phi_z|\ge c|\theta|$. Apply (T1) to $(I-C)e^{i\phi}a$. Every coefficient of the finite expansion vanishes near that critical set, because all derivatives of $1-c$ vanish near $(z,\phi_z)\in\Lambda$. Their integrals away from the critical set are smooth by repeated transfer of $\phi_\theta$. The remainder has arbitrarily low order as the finite expansion length increases, and hence gives every prescribed kernel derivative. On the remaining phase region, the same noncritical estimate applies before acting with $C$. Therefore $(I-C)u$ is smooth. The partial operator $P_x$ preserves jointly smooth compactly localized coefficients: its spatial Sobolev estimates apply uniformly after every $t,y$ derivative, and spatial Sobolev embedding supplies all joint derivatives. Thus $P_xu-P_xCu$ is smooth.

It remains to prove that $P_xC$ is an ordinary joint operator. Its left composition amplitude is the oscillatory integral
\[
 b(t,x,y;\tau,\xi,\eta)=(2\pi)^{-n}
   \iint e^{-iw\cdot\rho}P_L(x,\xi+\rho)
             c(t,x+w,y;\tau,\xi,\eta)\,dw\,d\rho.
\]
The finite scalar composition proof (FC1)–(FC4) applies uniformly in the additional frequencies as follows. Put $R=|\omega|$. Wherever $c$ is supported, $|\xi|\ge\epsilon R$. Split $\zeta=\xi+\rho$ into small, comparable and large multiples of $R$. On the noncomparable parts, $|\rho|=|\zeta-\xi|\ge c(R+|\zeta|)$; transfer the $w$ derivative in the exponential repeatedly. The cutoff has bounded base derivatives and order-decreasing joint frequency derivatives, while $P_L(x,\zeta)$ has at most fixed polynomial growth. Integrating in $\zeta$ after sufficiently many transfers gives any inverse power of $R$, also after every fixed joint frequency and base derivative. On the comparable part, $|\zeta|\asymp R$, so every differentiated $P_L$ satisfies ordinary order-one symbol bounds at the joint scale. The finite bilinear-phase remainder proof gives a joint $S^1_{1,0}$ symbol, with expansion
\[
 b\sim\sum_\alpha\frac{1}{i^{|\alpha|}\alpha!}
           (\partial_\xi^\alpha P_L)(x,\xi)
           (\partial_x^\alpha c)(t,x,y;\omega).
\]
The remainder after $L$ terms has order $1-L$ with all joint derivatives. The same cutoff-limit argument as in the scalar calculus identifies its quantization with the actual operator product, modulo the properly localized smooth tails; those tails obey the just-given estimates. Where $c=1$, every positive derivative of it is zero, so the principal and subprincipal terms of $P_xC$ are precisely $p(x,\xi)$ and $p_{\mathrm{sub}}(x,\xi)$. Adding the ordinary joint operator $D_t$ gives principal symbol $\tau+p$ and the claimed subprincipal symbol. Finite partitions cover each compact normalized portion of $\Lambda$. ∎

Use the fixed time half density \(|dt|^{1/2}\) to identify our time-family kernel with a full half-density kernel on \(\mathbb R\times X\times X\). In coordinates \((t,y,\eta)\) on \(\Lambda\), write its symbol as a Maslov-valued coefficient times
\[
|dt\,dy\,d\eta|^{1/2}.
\tag{20}
\]
This density is preserved by \(W\), since its parameters have \(W=\partial_t\). Its degree under cotangent dilation is \(n/2\), precisely the intrinsic symbol order for a kernel of order \(-1/4\). Under the unshifted joint normalization, the coefficient at zero in (20) is \((2\pi)^{1/4}\) times the identity-graph coefficient. Equivalently, rescale the joint coefficient by \((2\pi)^{-1/4}\) to use the identity as its initial value; this constant rescaling preserves the transport equation. Formula (17), with \(h=\tau+p\), becomes the ordinary differential equation
\[
\partial_t a+i\,p_{\mathrm{sub}}(\chi_t(y,\eta))a=0.
\tag{21}
\]
The scaled joint identity section just specified supplies its initial value at \(t=0\). Parallel transport in the flat Maslov line is understood. In a transported frame, the solution is
\[
a(t,y,\eta)=
\exp\left(-i\int_0^t
p_{\mathrm{sub}}(\chi_s(y,\eta))\,ds\right)a(0,y,\eta).
\tag{22}
\]
It is nonzero everywhere when its identity initial value is nonzero. Symmetry makes \(p_{\mathrm{sub}}\) real, so the scalar factor has absolute value one.

**Local construction of the full amplitude.** The symbol transport above determines the leading term. Here is the successive construction, including the lower terms and the smooth error. Use the ordinary fixed-time kernel normalization \((2\pi)^{-n}\int e^{i(\psi-y\cdot\eta)}a\,d\eta\); its amplitude in the normalized joint \(I^{-1/4}\) integral is \((2\pi)^{1/4}a\), as proved in (G18). In a coordinate patch write the left symbol of \(P\) as
\(P_L\sim p+p_0+p_{-1}+\cdots\). For small \(t\), the map taking an initial base point \(y\) to the final base point \(x\), with initial covector \(\eta\) fixed, has invertible derivative at \(t=0\). Inverting it gives \(y=y(t,x,\eta)\). Homogeneity and the Liouville identity give the degree-one function
\[
\psi(t,x,\eta)=\eta\cdot y(t,x,\eta),\qquad
d\psi=\xi\cdot dx+y\cdot d\eta-p\,dt.
\]
Thus \(\psi(0,x,\eta)=x\cdot\eta\) and
\(\psi_t+p(x,\psi_x)=0\). All these assertions are uniform on a compact normalized cotangent patch. The phase
\(\psi(t,x,\eta)-y\cdot\eta\) parametrizes (15).

Apply the left symbol product expansion to
\(e^{i\psi}a\), and use this eikonal equation to cancel its degree-one term. The degree-zero operator on the amplitude is
\[
\mathcal T a=-i\left(\partial_t+
 \sum_jp_{\xi_j}(x,\psi_x)\partial_{x_j}\right)a
 +\left[p_0(x,\psi_x)+\frac{1}{2i}
 \sum_{j,k}p_{\xi_j\xi_k}(x,\psi_x)\psi_{x_jx_k}\right]a.
\]
This is exactly [the finite phase-action calculation (T1)–(T2), specialized in (T11)](../providers/analysis/scalar-transport-and-phase-action.md#finite-phase-action). In its exact bilinear change of variables, $\partial_{w_j}F_k=\psi_{x_jx_k}/2$ at the critical point, giving the displayed last term and its sign. Each further term lowers the symbol degree, and the proved finite remainder is uniform after every base and parameter derivative. The free comparison [HS, Corollary 2.13] uses an adapted phase; the programme proof applies directly to the phase used here.

Solve \(\mathcal T a_0=0\) with \(a_0(0,x,\eta)=1\). Its real characteristic vector field is
\(\partial_t+p_\xi(x,\psi_x)\cdot\partial_x\), so the equation is a scalar ordinary differential equation along its characteristics. Its solution is nonzero. If the residual left by
\(a_0+\cdots+a_{-(j-1)}\) has leading term \(r_{-j}\), solve
\[
\mathcal T a_{-j}=-r_{-j},\qquad
a_{-j}(0,x,\eta)=0,\qquad j\geq1.
\]
In characteristic coordinates this has the explicit integral solution (T12) of the transport reading, after multiplication by the local half-density factor. The vector field and multiplication coefficient have degree zero in \(\eta\). Differentiation under its finite time integral and the product rule prove every symbol estimate; dilation and uniqueness prove degree \(-j\) for each solution. Classical asymptotic summation gives \(a\sim\sum_{j\geq0}a_{-j}\). Its residual has every negative symbol order, hence a smooth kernel; the initial error is smooth as well. This reproduces the successive cancellation in [HS, equations (3.14)–(3.19)] with the sign \(E(t)=e^{-itP}\).

For a localized initial pseudodifferential partition, prescribe its successive symbol terms instead of the displayed identity initial values. Take a finite partition of the compact cosphere bundle, and choose the phase patches large enough to contain the short-time flow of its supports. Cutoffs equal to one on these supports introduce only smooth errors: outside them there is no matching stationary covector. Summing the patch kernels gives the identity at zero modulo a smooth kernel. Subtract that smooth initial error with a smooth time cutoff. The resulting \(V\) has \(V(0)=I\) and a smooth residual. Lemma 5.1 then identifies its singular kernel with that of \(E\).

For any fixed finite time interval, choose an integer \(k\) so that \(|t/k|\) lies in this common short-time interval, and use
\(E(t)=E(t/k)^k\). Every matching intermediate covector is unique, because each relation is a Hamiltonian graph. Composition has excess zero and preserves order zero at fixed time. [The joint-parameter calculation, (G18)](../providers/analysis/transverse-composition-and-graph-operators.md#joint-parameters), shows that including time gives joint order \(-1/4\); its time covector is the sum of the phase time derivatives, giving relation (15) for this Hamiltonian evolution. Smooth remainders remain smooth under these compositions by the Sobolev estimates (7). The chart transitions of the phases carry the Maslov line; no single phase through a caustic is required. Their leading symbols compose to the nonzero symbol (22). This gives the same global construction as the intrinsic induction in the next theorem, from the local recursion and the stated graph-composition calculus.

The source conventions must be kept separate. The semiclassical order in [GS] is a power of \(h\), while our order is classical cotangent degree. In particular [GS, Section 10.2] constructs an unscaled-time pseudodifferential family; its formula alone is not the construction of \(e^{-itP_h/h}\). The classical recursion just given provides the needed bridge. Wunsch's Section 6 supplies the metric model, with density and global patching details left to its calculus. Neither comparison replaces the scalar half-density transport or the chart construction here.

## 5. A smooth residual disappears from the singular kernel

**Lemma 5.1 (evolution with a residual).** Suppose \(V(t)\) is an operator family on smooth half densities with \(V(0)=I\), and
\[
(D_t+P)V(t)=R(t).
\]
If \(R\) has a smooth kernel jointly in \(t,x,y\), then
\[
V(t)-E(t)=i\int_0^t E(t-s)R(s)\,ds
\tag{23}
\]
has a jointly smooth kernel.

**Proof.** For a smooth input differentiate \(E(-t)V(t)\), using (6). Since
\(\partial_tV=-iPV+iR\), its derivative is \(iE(-t)R(t)\).
Integrating and multiplying by \(E(t)\) gives (23), for positive and negative \(t\) with the oriented integral.

Fix a compact time interval. A smooth kernel \(R(s)\), with every time derivative, maps each \(H^{-N}\) boundedly into every \(H^k\), uniformly there. Equations (7) show that the integral in (23) has the same property for every time derivative: choose a still higher output order before differentiating. These estimates give continuity of the differentiated maps.

They imply a smooth joint kernel directly. In a chart, \(y\mapsto\partial_y^\beta\delta_y\) is continuous into \(H^{-N}\), and differentiable to any prescribed finite order when \(N\) is chosen sufficiently large. This follows from its local Fourier expression and the integrability of sufficiently negative Sobolev weights. Apply the integral operator to these families, choose \(k>n/2+|\alpha|\), and evaluate \(\partial_x^\alpha\) by Sobolev embedding. The resulting mixed \(t,x,y\) derivatives are continuous. Since their orders were arbitrary, its kernel is smooth. ∎

**Theorem 5.2 (the wave kernel).** The kernel (12) belongs to
\[
I^{-1/4}(\mathbb R\times X\times X,\Lambda).
\tag{24}
\]
Its principal symbol is the joint initial section specified after (20), transported by (21). Its kernel wavefront set equals \(\Lambda\). At every fixed time its kernel is an elliptic order-zero graph FIO associated with \(\chi_t\).

**Proof.** Realize the symbol (22) as \(V_0\in I^{-1/4}(\Lambda)\). We may choose classical amplitudes. By (17) and Lemma 4.1, its residual has order \(-5/4\); by (19), its initial error \(V_0(0)-I\) has pseudodifferential order \(-1\).

Suppose corrections through order \(-1/4-(j-1)\) have left a residual of order \(-1/4-j\) and an initial error of order \(-j\). Choose \(V_j\in I^{-1/4-j}(\Lambda)\). Its leading coefficient solves the inhomogeneous version of (21), with right side chosen to cancel the current residual and initial value chosen to cancel the current initial error. The symbol restriction in (19) identifies that initial value with exactly the needed pseudodifferential symbol.

Every trajectory of \(W\) meets the initial slice once, so the explicit variation-of-constants formula [(T12)](../providers/analysis/scalar-transport-and-phase-action.md#wave-transport-recursion) solves this equation globally. The initial correction includes the factor $(2\pi)^{1/4}$ inverse to the restriction factor in (R12). On every compact time interval, differentiating the flow and the equation gives all ordinary symbol estimates of order \(-j\). Homogeneity gives the leading degree, and the smooth source coefficients give its classical representative. Principal-symbol realization supplies \(V_j\); (17) and (19) lower both errors by another order.

Asymptotically sum these corrections in a locally finite collection of phase charts. The support-preserving sums have every asserted lower-order tail; the phase converse and symbol estimates make the construction independent of chart representatives modulo smooth kernels. Thus the resulting \(V\) has a smooth residual and a smooth initial error. Subtract a smooth time extension of that initial error. This makes \(V(0)=I\) exactly and keeps its residual smooth.

Each time restriction maps smooth inputs to smooth outputs by the FIO mapping theorem. It depends smoothly on time on those inputs: differentiating a phase integral only adds a finite symbol order, and its nonzero input covector gives the same smooth-input estimates. Consequently Lemma 5.1 applies. It gives \(V-E\) smooth and proves (24), with the same principal symbol.

The symbol (22) never vanishes. In a local Fourier normal form, a smooth direction would force its symbol to decrease faster than every power. Its nonzero homogeneous leading term prevents that. Hence every point of \(\Lambda\) occurs in the wavefront set; the opposite inclusion is the FIO wavefront theorem. Finally (19) gives the fixed-time order and relation, with nonzero restricted principal symbol. ∎

The construction is global in time but its symbol bounds are local on compact time intervals. It does not require a single generating phase through every caustic. Nor does it identify time modulo a classical period; the transported Maslov phase remains part of the symbol.

## 6. What a diagonal and a trace can detect

Apply [the qualified-pullback theorem and its wave applications, (R1)–(R2) and Section 7](../providers/analysis/wavefront-qualified-pullback.md#wave-restrictions). The kernel can be restricted to the time line above any fixed \(x,y\). Its wavefront contains no covector with time component zero, so the conormal obstruction to that restriction is absent. It is smooth near a time \(t_0\) if no trajectory travels from the input fiber above \(y\) to the output fiber above \(x\) at that time.

The same observation permits restriction to the spatial diagonal. Write the resulting density as \(k(t,x)=K_E(t,x,x)\).

Here is the compact integration rule needed for its trace. If \(u(t,x)\) is a distribution with a density in \(x\), and its support in \(x\) is compact locally in \(t\), define \(\pi_*u\) by testing \(u\) against a test function of \(t\) that is constant in \(x\) near that support. Suppose \((t_0,\tau_0)\), with \(\tau_0\ne0\), has no lift \((t_0,x;\tau_0,0)\) in \(\operatorname{WF}(u)\). Cover the compact fiber by finitely many coordinate neighborhoods. The definition of wavefront regularity and cutoff stability give a common time cutoff \(a=1\) near \(t_0\), a spatial partition \(b_j\), and rapid Fourier decrease of each compact coordinate distribution \(v_j=a(t)b_j(x)u\) on a cone about \((\tau_0,0)\). Each local coefficient includes its full density factor. Its spatial integral has Fourier transform

\[
 \widehat{\pi_*v_j}(\tau)=\widehat v_j(\tau,0).
\]

Thus every inverse power of \(|\tau|\) bounds that transform in a smaller cone about \(\tau_0\). The finite sum is the transform of \(a\,\pi_*u\). This proves
\(\operatorname{WF}(\pi_*u)\subset\{(t,\tau): (t,x;\tau,0)\in\operatorname{WF}(u)\text{ for some }x\}\).
Compactness is what permits one common time neighborhood and a finite sum. It also makes the distributional definition independent of the inserted spatial cutoff. Applying the qualified pullback theorem and this rule gives
\[
\operatorname{WF}(k)\subset
\{(t,x;-p(x,\eta),\xi-\eta):
(x,\xi)=\chi_t(x,\eta)\},
\tag{25}
\]
and therefore
\[
\operatorname{WF}\left(\int_X k(t,x)\right)
\subset
\{(t,-p(x,\eta)):
\chi_t(x,\eta)=(x,\eta)\}.
\tag{26}
\]
Both inclusions refer to nonzero covectors. The trace is a distribution, interpreted equivalently by pairing \(t\) against a compact smooth test and taking the convergent spectral sum.

Equation (25) can detect a trajectory returning to the same base point with a different covector. Equation (26) requires the whole covector to return, because integration sets \(\xi-\eta=0\). It gives a restriction on possible trace singularities; it does not preclude cancellations at a permitted time.

There is a uniform small deleted neighborhood of zero on which the diagonal time-line kernel is smooth. Indeed on the compact \(p=1\) level the base velocity \(p_\xi\) is nowhere zero, by Euler's identity. In finitely many coordinate charts,
\[
x(t)-x(0)=t\,p_\xi(x(0),\xi(0))+O(t^2)
\]
uniformly, with its leading vector bounded away from zero. Choose a common small time for the chart containment and this lower bound. No trajectory can return to its initial base point during that deleted interval. Homogeneity extends this conclusion to every nonzero energy.

**Example 6.1 (straight propagation on a flat torus).** On
\(\mathbb R^n/(2\pi\mathbb Z^n)\), the principal symbol \(p(\xi)=|\xi|\) has
\[
\chi_t(y,\eta)=(y+t\eta/|\eta|,\eta).
\tag{27}
\]
In a small coordinate lift its principal phase is
\((x-y)\cdot\eta-t|\eta|\).
The time covector is \(-|\eta|\), in agreement with (15). A full return requires
\[
t\,\eta/|\eta|=2\pi m,\qquad m\in\mathbb Z^n.
\]
Thus the possible nonzero trace-singular times are
\(\pm2\pi|m|\) for nonzero lattice vectors \(m\). This conclusion specifies the possible times; evaluating their coefficients is a further calculation.

### Use the conclusion

Check the time-covector component of the characteristic relation and the role of a smooth residual. The diagonal and the trace impose different restrictions; identify both before applying a return-time bound.

## 7. Exercises and complete solutions

**Exercise 7.1 (the density correction; introductory).** On the circle let \(\rho(x)>0\) be smooth, and use the weighted inner product \(\int f\overline g\,\rho\,dx\). Compute the formal adjoint of \(D_x\). Show that
\[
Q=D_x-\frac i2\frac{\rho'}{\rho}
\]
is symmetric, and conjugate it by \(Uf=\rho^{1/2}f\). Explain why its ellipticity does not imply a positive principal symbol.

**Solution 7.1.** Periodic integration by parts gives
\(D_x^*=D_x-i\rho'/\rho\). The adjoint of multiplication by
\(-i\rho'/(2\rho)\) is multiplication by \(+i\rho'/(2\rho)\), so \(Q^*=Q\).
Differentiation of \(\rho^{-1/2}u\) gives
\[
\rho^{1/2}D_x(\rho^{-1/2}u)
=D_xu+\frac i2\frac{\rho'}{\rho}u.
\]
The correction in \(Q\) cancels this term, hence \(UQU^{-1}=D_x\).
Its principal symbol is \(\xi\), positive on one component of the punctured cotangent fiber and negative on the other. The connected-cosphere argument in Section 1 requires \(n\geq2\), and therefore does not apply to this one-dimensional model.

**Exercise 7.2 (count the ambient dimensions; intermediate).** In a coordinate patch take the high-frequency kernel with phase
\[
(x-y)\cdot\eta-t|\eta|
\]
and an ordinary order-zero amplitude supported away from \(\eta=0\). Determine its Lagrangian order when time is a variable and when time is fixed. Verify its relation and time sign.

**Solution 7.2.** With \(N=n\) phase variables and ambient dimension \(d=2n+1\), an amplitude of order zero gives
\[
m=N/2-d/4=-1/4.
\]
At fixed time the ambient dimension is \(2n\), giving order zero.
The critical equation is \(x-y=t\eta/|\eta|\); the kernel derivatives are
\(\tau=-|\eta|\), \(\xi=\eta\) and input kernel covector \(-\eta\).
This is exactly the twist of (27), with the negative time frequency required by \(E(t)=e^{-itP}\). Time restriction adds \(1/4\), consistently with (18).

**Exercise 7.3 (a constant subprincipal shift; intermediate).** Replace \(P\) by \(P+cI\), for real \(c\). Compute its group, Hamilton flow, principal transport factor and trace. Which part of the kernel geometry changes?

**Solution 7.3.** Formula (5) gives
\[
E_{P+c}(t)=e^{-ict}E_P(t).
\]
Its principal symbol remains \(p\), while the subprincipal symbol becomes \(p_{\mathrm{sub}}+c\). Formula (22) therefore acquires exactly \(e^{-ict}\). The Hamilton flow and the entire wavefront relation remain unchanged. The distributional trace is multiplied by that same smooth nowhere-zero factor. Thus its singular times remain unchanged, though its coefficients may change.

**Exercise 7.4 (derive the trace restriction; advanced).** Starting with the full kernel relation (15), derive (25) and (26). Explain why a return to the same base point alone is insufficient for the trace conclusion. On the flat torus, determine the shortest possible positive return time.

**Solution 7.4.** The differential of \((t,x)\mapsto(t,x,x)\) pulls a kernel covector
\((\tau,\xi,-\eta)\) back to \((\tau,\xi-\eta)\). Its conormal would have \(\tau=0\), which (15) excludes. Substituting the relation gives (25). Integration over the compact spatial variable retains only covectors with spatial component zero, hence imposes \(\xi=\eta\), giving (26). A trajectory with the same initial and final base point but different covectors contributes a potentially nonzero spatial wavefront component; the trace rule discards that component. On the flat torus the covector is constant, and a return has length \(2\pi|m|\). A nonzero integer vector has minimum Euclidean length one, so the shortest possible positive return time is \(2\pi\).

**Exercise 7.5 (smooth perturbations preserve the relation; advanced).** Let \(F\) be a bounded symmetric operator with a smooth kernel on \(X\times X\). Prove that the wave kernels of \(P+F\) and \(P\) differ by a jointly smooth kernel. Give an \(L^2\) norm bound for their difference.

**Solution 7.5.** The bounded symmetric perturbation is self-adjoint on the same \(H^1\) domain. Its principal symbol, ellipticity and every integer Sobolev graph estimate remain those in Section 1, since \(F\) is smoothing. It has the same Sobolev group continuity. Applying the residual identity with the generator \(P+F\) to the family \(E_P(s)\) gives
\[
E_{P+F}(t)-E_P(t)
=-i\int_0^t E_{P+F}(t-s)F E_P(s)\,ds.
\tag{28}
\]
The residual \(F E_P(s)\), with every time derivative, maps each negative Sobolev space to every positive one: \(E_P\) preserves Sobolev order, each derivative inserts a finite power of \(P\), and \(F\) supplies arbitrary smoothing. The proof of Lemma 5.1 therefore makes (28) jointly smooth in all kernel variables. Unitarity of both groups bounds its \(L^2\) norm by
\[
\|E_{P+F}(t)-E_P(t)\|_{2\to2}\leq |t|\,\|F\|_{2\to2}.
\]
Their wavefront relations coincide, as also follows from their identical transported leading symbols. This result concerns a smooth perturbation; boundedness alone would not provide the smoothing conclusion.

## References

- [FI] Lars Hörmander, “Fourier integral operators I,” *Acta Mathematica* 127 (1971), 79–183. Sections 1.2 and 2.5, Chapter III, Proposition 4.1.7, and Theorems 4.2.2–4.2.3. [Original article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392052).
- [FII] Johannes J. Duistermaat and Lars Hörmander, “Fourier integral operators II,” *Acta Mathematica* 128 (1972), 183–269. Sections 5.2–5.3, especially Theorems 5.3.1–5.3.2. [Original article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392165).
- [HS] Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* 121 (1968), 193–218. Sections 2–3, especially Corollary 2.13 and equations (3.14)–(3.19). [Full article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02391913).
- [GS] Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*, author text dated April 25, 2012. Sections 8.7.5 and 8.13. [Author PDF](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf).
- [W] Jared Wunsch, *Microlocal analysis and evolution equations*, lecture notes, arXiv:0812.3181v3 (2023 revision of 2008 notes). Sections 4.1 and 6. [Author preprint](https://arxiv.org/abs/0812.3181v3).
- [DG] Johannes J. Duistermaat and Victor W. Guillemin, “The spectrum of positive elliptic operators and periodic bicharacteristics,” *Inventiones Mathematicae* 29 (1975), 39–79. [Freely readable complete GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0029/LOG_0010.pdf).
