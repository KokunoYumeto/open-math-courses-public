# First-order Cauchy problems: energy and wavefront transport

An energy inequality controls the size of a solution and its dependence on the forcing. A transported pseudodifferential test controls which spatial singularities survive. We prove both mechanisms, including existence for integrable forcing and the exact cotangent motion when the principal symbol is purely imaginary.

The Hamilton convention agrees with [Phase space and generating families](../20261005-restored-phase-space/phase-space-and-generating-families.md) and [Hamilton fields and subprincipal transport](../20261005-restored-subprincipal-transport/hamilton-fields-and-subprincipal-transport.md). The symbol, Sobolev, positivity and wavefront inputs are stated below. All solution assertions concern the displayed global scalar problem on a finite time interval.

## 1. The equation and strong time continuity

Use the established Fourier convention, \(D=-i\partial\), left quantization and the pairing linear in its first entry. Set \(E_s=\langle D\rangle^s\), \(\|v\|_s=\|E_sv\|_2\). The dual pairing of \(H^s\) with \(H^{-s}\) extends the \(L^2\) pairing. The equation is
\[
 P u=\partial_tu+A(t)u=f,\qquad A(t)=a(t,x,D),\qquad u(0)=\phi,
 \qquad 0\leq t\leq T<\infty.
\]
Assume the following scalar hypotheses:

1. \(a(t)\) is bounded in the global ordinary class \(S^1_{1,0}(\mathbb R^n_x\times\mathbb R^n_\xi)\), uniformly in \(t\).
2. \(t\mapsto a(t)\) is continuous in distributions, equivalently locally with all spatial/frequency derivatives under the preceding boundedness.
3. \(\operatorname{Re}a(t,x,\xi)\geq-C\), uniformly in all variables.

Do not replace 2 by continuity in the global symbol seminorms or by operator-norm continuity. Distributional continuity plus uniform derivative bounds gives local smooth continuity: on each compact, Arzelà–Ascoli applied successively to all derivatives gives subsequential local smooth limits; their distributional limit is the prescribed symbol, so a contradiction/subsequence argument gives convergence of the entire sequence. The parameter interval is metrizable, so this suffices for continuity. Compact local equicontinuity follows from one extra bounded derivative in each variable.

The following complete earlier programme proofs supply the inputs:

- [Sharp lower bounds and strong time continuity, G1–G7](../20261005-cauchy-foundations/sharp-lower-bound.md) prove global Sobolev action, the full sharp Gårding inequality, and the compactness/density argument just used. G6 includes the required H1 extension and all-real Sobolev conjugation.
- [Ordinary operator calculus, O1–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) gives every full composition/adjoint remainder and its finite-seminorm continuity. The support-preserving asymptotic construction is [Hamilton transport, Section H6](../20261004-free-canonical-composition/homogeneous-symbol-transport.md); its first-time-derivative adaptation is proved in Section5 below.
- [Integration and duality](../20261005-cauchy-foundations/integration-and-duality.md) supplies complex Hahn–Banach, all-exponent integral inequalities, complete Bochner spaces and integrals, smooth tensor density, the actual absolutely continuous primitive and trace, and Hilbert L1/Sobolev duality. Its Hilbert representation input is the complete geometric proof in [T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md).
- [Wavefront localization W1–W4](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) and [conic parametrices K2–K4](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) prove the spatial microlocal tests. [Spacetime composition, M5](spacetime-symbol-composition.md) gives the full global tempered extension of the proper wavefront argument.
- The same [spacetime companion, M1–M4](spacetime-symbol-composition.md), and the complete [smooth pullback and trace companion](smooth-pullback-and-time-slices.md), supply both terminal spacetime proofs used in Section6. Their exact hypotheses are restated at the point of use.

The [proof map](proof-map.json) records exact source hashes, unique locators and all transitive prerequisites. The two earlier foundation companions and the pullback companion retain their stated AN-03 GFDL notices. The present receiving lesson and its original exercises retain their independent exposition. A source citation supplies credit, never a missing proof.

For \(w\in\mathcal S\), the quantization integral and dominated convergence give local smooth convergence of \(A(t_j)w\) when \(t_j\to t\). The uniform ordinary symbol bounds give uniform bounds in every output Schwartz seminorm. One extra position weight controls the complement of a large position ball; local convergence controls its interior. Hence convergence is in \(\mathcal S\). By the uniform bound \(\|A(t)\|_{H^s\to H^{s-1}}\leq M_s\) and Schwartz density, for arbitrary fixed \(w\in H^s\), first approximate \(w\) by a Schwartz vector, then use the uniform \(2M_s\) bound on the approximation error. Thus \(A(t)\) is strongly continuous \(H^s\to H^{s-1}\) for every real \(s\). Consequently \(A(t)u(t)\) is continuous in \(H^{s-1}\) whenever \(u\in C_tH^s\), by adding the fixed-vector and varying-vector errors.

These are scalar hypotheses. The preserved next lesson on first-order systems and ordered evolution requires its own current proof review of the uniform Hermitian lower-bound condition and ordered evolution. Entrywise inequalities and eigenvalue-only tests do not supply that condition; Exercise 16 gives an explicit failure. The scalar Hamiltonian wavefront assertions below retain their stated scalar hypotheses.

## 2. The weighted energy estimate, every real order and every p

Begin with \(u\in C^1([0,T];H^s)\cap C([0,T];H^{s+1})\), \(f=Pu\). For \(s=0\), sharp Gårding gives
\[
 \frac{d}{dt}\|u(t)\|_2^2
 =2\operatorname{Re}(f,u)-2\operatorname{Re}(Au,u)
 \leq2\|f\|_2\|u\|_2+2c\|u\|_2^2.
\]
Let \(w=e^{-ct}u\). Integration gives, for
\(M(t)=\max_{0\leq r\leq t}\|w(r)\|_2\),
\[
 M(t)^2\leq\|u(0)\|_2^2+
       2M(t)\int_0^t e^{-cr}\|f(r)\|_2\,dr.
\]
The positive root is at most \(\|u(0)\|_2+2\int_0^t e^{-cr}\|f(r)\|_2dr\). This includes \(M=0\), so no division by a possibly vanishing norm is needed. For \(\lambda>\max(0,2c)\),
\[
 e^{-\lambda t}\|u(t)\|_2
 \leq e^{-\lambda t/2}\|u(0)\|_2+
 2\int_0^t e^{-\lambda(t-r)/2}e^{-\lambda r}\|f(r)\|_2\,dr.
\]
Extend the weighted forcing by zero to the half-line. For \(1\leq p<\infty\), the \(L^p(0,\infty)\) norm of \(e^{-\lambda t/2}\) is \((2/(p\lambda))^{1/p}\leq(2/\lambda)^{1/p}\); its \(L^\infty\) norm is one. Minkowski's integral inequality for the convolution therefore proves
\[
 \left(\frac\lambda2\int_0^T
       \|e^{-\lambda t}u(t)\|_s^p\,dt\right)^{1/p}
 \leq\|u(0)\|_s+
       2\int_0^T e^{-\lambda t}\|Pu(t)\|_s\,dt. \tag{EC}
\]
For \(p=\infty\), interpret the left side as \(\max_{[0,T]}e^{-\lambda t}\|u(t)\|_s\), with no prefactor. The estimate retains factor 2 and the precise \(\lambda/2\) normalization; the stronger kernel constant \(p^{-1/p}\) need not be claimed as a sharp constant for the whole theorem.

For general \(s\), put \(B(t)=E_sA(t)E_{-s}\). Ordinary composition gives a symbol in \(S^1\), with \(B-A\in\operatorname{Op}(S^0)\), uniformly in \(t\). Indeed the leading product is \(\langle\xi\rangle^s a\langle\xi\rangle^{-s}=a\); every differentiated product loses at least one order. The full finite-seminorm remainder supplies the asserted uniform order-zero bounds. Applying the same composition/adjoint continuity contract gives local smooth parameter continuity. Its real-part lower bound follows directly from \(\operatorname{Re}(Av,v)\geq-c\|v\|_2^2\) plus the uniformly bounded order-zero difference. Apply the already proved order-zero estimate to \(E_su\), with forcing \(E_sf\). The threshold \(c_s\) depends on \(s\) and finitely many uniform seminorms; it is independent of \(p\) and \(u\). Positivity of the pointwise symbol of \(B\) is not needed.

The forward uniform consequence, used repeatedly below, is
\[
 \max_{[0,T]}\|u(t)\|_s
 \leq e^{\lambda T}\left(\|u(0)\|_s+2\|Pu\|_{L^1_tH^s}\right).
\]
All later uses at lower Sobolev orders must check the lemma's \(C^1H^r\cap CH^{r+1}\) domain first.

## 3. Existence, uniqueness and the measurable weak solution

**Theorem (scalar Cauchy problem).** For every real \(s\), \(\phi\in H^s\) and \(f\in L^1((0,T);H^s)\), there is a unique \(u\in C([0,T];H^s)\) solving the distributional equation and its trace condition, and (EC) holds. Its derivative belongs to \(L^1_tH^{s-1}\); it is an absolutely continuous \(H^{s-1}\)-valued function. It need not be \(C^1_tH^{s-1}\) when \(f\) is only integrable.

**Uniqueness in the claimed class.** If \(Pu=0\), \(u(0)=0\), strong continuity gives \(A(t)u(t)\in C_tH^{s-1}\). The distributional equation then gives \(u\in C^1_tH^{s-1}\cap C_tH^s\). Apply (EC) at order \(s-1\), obtaining \(u=0\). For the scalar implication from a distributional derivative to the classical derivative, test against a Sobolev dual vector and use the scalar fundamental theorem. The integration companion H5 proves this vector primitive and constant argument completely, including its norm derivative and unique continuous representative. The separating dual family identifies the vector derivative and trace.

**The reversed adjoint estimate.** Let \(v\in C_c^\infty(( -\infty,T)\times\mathbb R^n)\), restricted to \([0,T]\); it can be nonzero at \(t=0\), and is zero near \(T\). Put
\[
 g=-\partial_tv+A(t)^*v.
\]
After \(t=T-r\), this is the forward equation with operator \(A(T-r)^*\) and zero initial value. The adjoint has ordinary order one and the necessary strong continuity. The adjoint form has the same real part as \(A\)'s form. Equivalently, its left symbol is \(\overline a+S^0\), so the source hypotheses survive with a changed lower constant. Applying the weighted maximum estimate at order \(-s\), absorbing its finite exponential weights into a constant, gives
\[
 \max_{[0,T]}\|v(t)\|_{-s}
 \leq C_{s,T}\int_0^T\|g(t)\|_{-s}\,dt. \tag{AD}
\]

Define on the range of this test map the conjugate-linear functional
\[
 \mathcal F(g)=\int_0^T\langle f(t),v(t)\rangle\,dt+
              \langle\phi,v(0)\rangle.
\]
If two tests have the same \(g\), (AD) applied to their difference makes them identical, so the functional is well defined. Its bound is
\[
 |\mathcal F(g)|\leq C_{s,T}
 (\|f\|_{L^1H^s}+\|\phi\|_s)\|g\|_{L^1H^{-s}}.
\]
Complex Hahn–Banach applied after conjugation extends it to all of \(L^1((0,T);H^{-s})\), with the same bound \(K\).

**The Hilbert representation and its precise scope.** The full finite-interval Hilbert L1 duality proof is SectionH6 of the integration companion. In detail, complete Bochner L2 is a Hilbert space by its retained Section17.3. Restrict the functional to it, with norm at most \(K\sqrt T\), and apply the proved Hilbert representation T1. That proof uses the closest-vector construction and parallelogram identity, so no unproved choice of an orthonormal basis is needed here. Applying the Sobolev multiplier isometry of SectionH6 gives \(u\in L^2_tH^s\) with \(\mathcal F(g)=\int\langle u,g\rangle\). The following normalized test completes the L1 representation in this receiver.
The original \(L^1\) bound forces \(\|u(t)\|_s\leq K\) almost everywhere. Otherwise, on a positive-measure set \(B\) where \(\|u\|_s>K+\epsilon\), choose
\(g(t)=1_B(t)E_{2s}u(t)/\|u(t)\|_s\). This is strongly measurable, has \(H^{-s}\) norm \(1_B\), belongs to \(L^2_tH^{-s}\), and gives \(\int_B\|u(t)\|_sdt>K|B|\), contradicting the bound. The Sobolev multiplier \(E_{2s}:H^s\to H^{-s}\) is an isometry, and the pairing of \(u\) with this normalized vector is its norm. Hence \(u\in L^\infty_tH^s\). Bounded simple Hilbert-valued functions are dense in \(L^1\), by truncation and strongly measurable simple approximation. Equality on \(L^2\) therefore extends to all \(L^1\). This proof uses finite time measure and Hilbert structure, and does not assert the dual formula for an arbitrary Banach space.

The test identity is now
\[
 \int_0^T\langle u,-v_t+A^*v\rangle\,dt
 =\int_0^T\langle f,v\rangle\,dt+\langle\phi,v(0)\rangle. \tag{WK}
\]
Tests supported in \((0,T)\) give \(u_t=f-Au\) in distributions. Strong continuity of \(A\) and approximation of \(u\) by simple measurable vectors show \(Au\) strongly measurable in \(H^{s-1}\); the uniform operator bound gives \(Au\in L^\infty H^{s-1}\). Thus \(u_t\in L^1H^{s-1}\). The Bochner primitive \(w(t)=\int_0^t(f-Au)dr\) is absolutely continuous in \(H^{s-1}\). Every scalarized derivative of \(u-w\) is zero, hence it is constant. More explicitly, scalar distributional constants for a countable separating orthonormal family give a single constant vector: the almost-everywhere Hilbert-valued representative of \(u-w\) agrees with all its constant coordinates on a common full-measure set. It follows that \(u\) has a continuous \(H^{s-1}\) representative. Integrating this representative by parts in (WK) and varying \(v(0)\) gives \(u(0)=\phi\) in \(H^{s-1}\).

**Gain the regularity needed for the energy lemma on smooth data.** First take \(f\) smooth in time with values in \(\mathcal S\), and \(\phi\in\mathcal S\). Perform the preceding weak construction at order \(s+2\). It gives \(u\in L^\infty H^{s+2}\), hence \(u\in C H^{s+1}\). The equation and strong continuity at this lower order imply \(u_t=f-Au\in C H^s\), so \(u\in C^1H^s\cap CH^{s+1}\). Its initial trace is the desired one and (EC) applies at order \(s\). No appeal to uniqueness for an as-yet unproved continuous high-order representative is used in this step.

For arbitrary data, approximate \(\phi\) in \(H^s\) by Schwartz vectors and \(f\) in Bochner \(L^1H^s\) by finite sums of smooth time functions times Schwartz vectors. Such density follows by strongly measurable simple approximation, scalar \(L^1\) smooth approximation and spatial Schwartz density. The uniform maximum estimate applied to differences of the smooth-data solutions makes them Cauchy in \(C H^s\). Completeness here is immediate from the proved Hilbert completeness: at each time the Cauchy sequence has a limit, the uniform Cauchy bound gives uniform convergence to it, and its continuity follows by first choosing one continuous approximant and then using the two uniform errors in the triangle inequality. Their limit has the trace, and \(Au_j\to Au\) uniformly in \(H^{s-1}\), while \(f_j\to f\) in \(L^1H^s\). Passing in the integrated equation gives the solution, its absolute continuity one order lower and its distributional equation. Passing in (EC) gives the stated estimate for each finite \(p\) by uniform convergence and in the forcing term by its \(L^1\) convergence; the maximum case follows directly. The uniqueness already proved identifies all constructions.

For homogeneous forcing and \(\phi\in\bigcap_sH^s\), repeat the theorem at every real order, use uniqueness at a common lower order, and conclude \(u\in C^1_tH^s\) for every \(s\) by first obtaining \(C_tH^{s+1}\). The explicit Fourier Sobolev embedding proof in companion M5 gives spatial smoothness at fixed time. With merely continuous coefficients this gives only one continuous time derivative on every spatial Sobolev scale. If the symbol is smooth in time, with all time derivatives uniformly ordinary of order one on compact time intervals, differentiating the equation inductively gives all time derivatives and spacetime smoothness.

## 4. A real homogeneous principal Hamiltonian and its complete finite-time flow

For exact fixed-time wavefront transport strengthen the assumptions to a bounded classical family
\[
 a(t,x,\xi)/i\sim\sum_{j\geq0}b_j(t,x,\xi),\qquad
 \deg_\xi b_j=1-j,\qquad b_0\text{ real}.
\]
Retain uniform ordinary remainders and uniform coefficient bounds, local smooth continuity in \((x,\xi)\) with respect to \(t\), and uniform bounds in the normalized nonzero-frequency regions. The expression “each individual symbol is classical” alone would not give uniform family remainder estimates; state the family hypothesis explicitly. The principal symbol of \(a\) is \(i b_0\), so both \(a\) and \(-a\) have real part bounded below after removing this purely imaginary order-one term: their real parts are uniformly order zero. Both time directions therefore satisfy the existence/energy theorem. A positive real order-one principal symbol allows the forward theorem but generally destroys backward evolution and equality of wavefronts.

For \(\eta\ne0\), solve
\[
 \dot x=\partial_\xi b_0(t,x,\xi),\qquad
 \dot\xi=-\partial_xb_0(t,x,\xi),\qquad
 (x(0),\xi(0))=(y,\eta),
\]
and write the map as \(\chi_t(y,\eta)\). Uniformity gives constants with \(|\dot x|\leq C\), \(|\dot\xi|\leq C|\xi|\). Integration, or Grönwall for the second inequality in each time direction, gives
\[
 |x(t)-y|\leq CT,\qquad
 e^{-CT}|\eta|\leq|\xi(t)|\leq e^{CT}|\eta|. \tag{FL}
\]
The frequency never reaches zero. On the unit initial-frequency set, these bounds keep the trajectory in a fixed normalized annular region and a bounded displacement from its starting base. The uniform derivative bounds there give a uniform local existence interval, and finitely many such intervals cover \([0,T]\). This excludes both finite base escape and frequency escape, and proves the flow exists for all initial nonzero covectors over the whole finite time interval. Here is the needed time-continuous version of the [finite-flow proof NF1–NF7](../20261005-restored-phase-space/finite-coordinate-flows.md). On a closed small state ball choose a uniform bound \(M\) for the field and \(L\) for its state derivative. On a time interval of length \(h\) with \(hM\) smaller than the ball margin and \(hL<1/2\), the integral map is a contraction of continuous paths in the sup norm. Its iterates have geometrically bounded differences and converge uniformly in the complete continuous-path space; the integral of the continuous field identifies the limit and gives one time derivative. Uniqueness follows from the same difference estimate. For initial-state derivatives, the first variation is the integral equation \(V=I+\int D H_{b_0}\,V\). Its ordered series converges with kth term bounded by \((Lh)^k/k!\). Taylor's formula in the state variable shows that the actual difference quotient minus this solution has a uniformly vanishing forcing; iteration of the integral inequality bounds its norm by that forcing times \(e^{Lh}\). Thus it is the derivative. At derivative order \(k\), differentiate the integral identity: the unknown derivative has the same linear coefficient, and the remaining finite chain-rule sum uses only derivatives of orders less than \(k\) and state derivatives of the field through \(k\). The same ordered-series estimate and Taylor remainder prove existence and continuity of that derivative. This induction proves every initial-state derivative without taking a time derivative of the field. The elementary integral inequality used here follows by iterating \(d(t)\leq a+L\int d\), obtaining \(a\sum_{j<k}(Lt)^j/j!+\|d\|_\infty(Lt)^k/k!\), and taking \(k\to\infty\). Applying it to \(|\xi|\) in both directions proves (FL); integrating \(|\dot x|\leq C\) proves its base bound.

Homogeneity and uniqueness give
\(\chi_t(y,r\eta)=(x(t;y,\eta),r\xi(t;y,\eta))\) for \(r>0\). Differentiating the variational equations on the normalized region and using (FL) gives uniform bounds for every initial derivative, by induction on derivative order and Grönwall; restoring homogeneity gives the symbol-scale bounds. The reverse nonautonomous flow \(\chi_{0,t}\) is the inverse of \(\chi_{t,0}\), by uniqueness. A time-dependent evolution is a two-time family: do not assert \(\chi_{t+s}=\chi_t\chi_s\) without autonomy.

For the established symplectic convention, \(H_b=(b_\xi,-b_x)\). If \(M(t)=D\chi_t\), its variational matrix \(K(t)=DH_{b_0}\) satisfies \(K^T\Omega+\Omega K=0\), because the Hessian of the real \(b_0\) is symmetric. Hence
\(\partial_t(M^T\Omega M)=M^T(K^T\Omega+\Omega K)M=0\).
Since \(M(0)=I\), the map is symplectic. Its homogeneity and symplecticity make it a homogeneous canonical transformation. These are properties of the real flow; no complex flow or imaginary-frequency continuation is used.

## 5. Construct a full commuting symbol, retaining its smoothing errors

Choose a compactly based conic neighborhood of \((y_0,\eta_0)\notin\operatorname{WF}(\phi)\), with \(\phi\in H^r\) for some real \(r\). By the exact Fourier/conic test contract choose a classical order-zero symbol \(q\sim\sum q_j\), \(q_0(y_0,\eta_0)\ne0\), whose microsupport is in that regular neighborhood, so \(q(x,D)\phi\in H^\infty:=\bigcap_sH^s\). One concrete choice is a compact output cutoff times a smooth angular Fourier cutoff times a compact input cutoff; its localized smooth output is compactly supported, hence lies in every Sobolev space. Choose the cutoffs nested so the initial symbol remains elliptic at the selected direction. Its operator can be taken proper. An arbitrary unlocalized smooth function need not lie in \(H^\infty\); use the compact localization.

Seek \(Q(t)\sim\sum_{j\geq0}Q_j(t)\), with each \(Q_j\) homogeneous of degree \(-j\). Since \(a\sim i\sum b_j\), the ordinary commutator expansion is
\[
 \sigma([P,Q])\sim\partial_tQ+
 i\sum_{|\alpha|\geq1}\frac{1}{\alpha!}
   \big[(\partial_\xi^\alpha b)D_x^\alpha Q
       -(\partial_\xi^\alpha Q)D_x^\alpha b\big].
\]
Here \(b=a/i\) is the full symbol, and \(\sigma\) denotes the full left symbol in this display. For each finite \(N\geq1\), subtracting \(\partial_tQ\) and the displayed sum with \(1\leq|\alpha|<N\) from the actual left symbol leaves a remainder uniformly in \(S^{1-N}\), by the two finite composition remainders. The display denotes this asymptotic expansion; it does not assert convergence of an infinite operator series.
The \(\alpha=0\) terms cancel because the symbols are scalar. The \(|\alpha|=1\) leading term is \(H_{b_0}Q_0\), since \(iD_x=\partial_x\); there is no remaining factor \(i\). Thus
\[
 (\partial_t+H_{b_0})Q_0=0,\qquad
 (\partial_t+H_{b_0})Q_j=-R_j\quad(j\geq1),
\]
where \(R_j\) consists of terms with
\(k+\ell+|\alpha|=j+1\), \(|\alpha|\geq1\), from \(b_k,Q_\ell\), omitting only \(k=0,\ell=j,|\alpha|=1\). Hence every \(Q_\ell\) entering \(R_j\) has \(\ell<j\), and the degree is exactly \(-j\). Explicitly the coefficient of a retained pair is
\(i[(\partial_\xi^\alpha b_k)D_x^\alpha Q_\ell-(\partial_\xi^\alpha Q_\ell)D_x^\alpha b_k]/\alpha!\).

The complete solution is
\[
 Q_0(t,\chi_t(y,\eta))=q_0(y,\eta),\qquad
 Q_j(t,\chi_t(y,\eta))=
 q_j(y,\eta)-\int_0^tR_j(r,\chi_r(y,\eta))\,dr. \tag{TR}
\]
The flow bounds prove uniform symbol estimates and continuous time derivatives. Support control follows inductively: the derivatives in \(R_j\) do not enlarge the supports of the previously constructed coefficients, and the characteristic integral carries the initial compactly based conic support along \(\chi_t\). Its base support remains in a fixed compact set by (FL). The normalized angular supports are transported on the cosphere with bounded derivatives. Low-frequency extensions are cutoff choices; they contribute uniformly smoothing errors.

For a parameter-dependent asymptotic sum, apply the actual frequency cutoff construction H6 in the exact Hamilton-transport provider to the supremum in \(t\) of each coefficient seminorm and of its first time derivative. These suprema are finite by (TR). Select cutoff radii \(\Lambda_j\) large enough to make both sets of seminorms through derivative order \(j\) at most \(2^{-j}\) at the next higher order. The cutoff depends only on \(\xi\), not on \(t\). The resulting sum is locally finite in frequency; tails converge uniformly in the stipulated spatial/frequency seminorms, both before and after one time derivative. Thus \(Q\) is \(C^1\) in time with the required locally smooth topology, has all uniform ordinary expansion estimates, and preserves the transported support. Applying the full finite composition remainders at each order, together with (TR), proves
\[
 \begin{gathered}
 Q(0)-q\in S^{-\infty},\\
 [P,Q]=R(t).
 \end{gathered} \tag{SM}
\]
The family \(R(t)\) is bounded in \(S^{-\infty}\) and locally smoothly continuous in \(t\).
Do not claim exact \(Q(0)=q\) or exact vanishing of the commutator. Those errors are sufficient, because every uniformly smoothing ordinary symbol maps a fixed \(H^r\) to every \(H^s\), with uniform finite-seminorm bounds. Strong continuity follows from the same Schwartz-density argument as in §1.

For \(u\in C_tH^r\) solving \(Pu=0\), the product rule in the distributional equation gives
\(P(Qu)=Ru\), \((Qu)(0)=q\phi+(Q(0)-q)\phi\).
The time derivative of \(Q\) has order zero, so this product rule is legitimate in \(H^{r-1}\), first by scalar test integration and then by the uniform operator estimates. Its forcing is \(C_tH^s\) and its initial value is in \(H^s\) for every \(s\). The existence theorem constructs a \(C_tH^s\) solution at each order. Uniqueness at a common lower order identifies each with \(Qu\). Consequently \(Qu\in C_tH^\infty\), and ellipticity of \(Q_0(t)\) at \(\chi_t(y_0,\eta_0)\) removes this covector from \(\operatorname{WF}(u(t))\).

## 6. Exact fixed-time propagation and the separate spacetime statement

Since the preceding construction works at every covector outside \(\operatorname{WF}(\phi)\), and \(\chi_t\) is bijective,
\[
 \operatorname{WF}(u(t,\cdot))\subset\chi_t\operatorname{WF}(\phi).
\]
Restart the solution at time \(t\), reverse time on \([0,t]\), and use the purely imaginary principal-symbol hypothesis to apply the same theorem. The resulting inclusion is
\(\operatorname{WF}(\phi)\subset\chi_{0,t}\operatorname{WF}(u(t))\).
Applying \(\chi_t\) proves the reverse inclusion. Therefore the full statement, for every \(t\in[0,T]\), is
\[
 \boxed{\operatorname{WF}(u(t,\cdot))=\chi_t\operatorname{WF}(\phi)}. \tag{WF}
\]
This is the homogeneous equation \(f=0\), for initial data in the union \(H^{-\infty}:=\bigcup_rH^r\). It neither asserts wavefront equality for an inhomogeneous forcing nor for arbitrary \(\mathcal S'\) outside that union. The evolution map \(F_{t,0}:H^s\to H^s\) is bounded and has the bounded reverse map \(F_{0,t}\); uniqueness supplies the two-time cocycle. Fixed-time wavefront equality alone does not prove that its kernel is an elliptic FIO. That later construction remains a separate assigned goal.

The terminal paragraph of §23.1 requires greater time smoothness, namely an ordinary symbol \(a(t,x,\xi)\) in the joint base \((t,x)\), with uniform time derivatives on the interval under discussion. The expression
\(D_t+a(t,x,D_x)/i\) is not generally an ordinary pseudodifferential operator in all \((\tau,\xi)\): frequency derivatives near large \(|\tau|\) and small \(|\xi|\) have the wrong isotropic loss. Away from the cone \(\xi=0\), a spacetime conic cutoff turns it into an ordinary PDO; its principal symbol is \(\tau+b_0\).

The two complete spacetime companions prove the exact contracts used here:

1. [M1–M4](spacetime-symbol-composition.md) prove that a full ordinary \(c\in S^m\), zero when \(\epsilon|\tau|>1\) and \(|\xi|\leq\epsilon|\tau|\), can be composed in either order with a spatial-only \(b\in S^{m'}\), smooth with uniform bounds in the joint base. Both products have ordinary order \(m+m'\) and the usual full expansions, including every derivative of the finite remainder. M5 proves their actual global-tempered application to the equation and the transported test. The cutoff condition retains the low-frequency exception.
2. [WF11–WF17 and S1–S2](smooth-pullback-and-time-slices.md) construct smooth-map pullback when \(N_F\cap\operatorname{WF}(u)=\varnothing\), prove its exact covector containment and fixed-wavefront sequential continuity, and identify the time-slice pullback with the continuous Sobolev trace. For \(F(x)=(t_0,x)\), the forbidden normals are \((t_0,x;\tau,0)\), \(\tau\ne0\). This theorem supplies containment; the equality below also uses the transported elliptic test.

With these proved contracts and time smoothness, conic elliptic regularity applied to the equation proves
\[
 \operatorname{WF}(u)\subset
 \{(t,x;-b_0(t,x,\xi),\xi):\xi\ne0\}
 \cup\{(t,x;\tau,0):\tau\ne0\},\quad 0<t<T.
\]
Keep the possible pure temporal directions. If independently it is known that no \(\xi=0\) direction lies in \(\operatorname{WF}(u)\), restrictions are valid. Their distributional pullback agrees with the continuous \(H^r\)-valued trace by companion S2: both are continuous distribution-valued families reconstructing the same joint distribution; testing their continuous scalar difference against all time bumps makes it zero at every time. The restriction theorem then gives one inclusion of
\[
 \operatorname{WF}(u(t_0,\cdot))=
 \{(x,\xi):(t_0,x;-b_0(t_0,x,\xi),\xi)\in\operatorname{WF}(u)\}.
\]
For the other inclusion, if the spatial direction at \(t_0\) is regular, construct the same transported \(Q\) with that time as initial slice. With smooth time coefficients, include all time derivatives through order \(j\) in the cutoff choice for the \(j\)-th symbol coefficient; the construction then has all time derivatives. The equation for \(u\) inductively gives \(\partial_t^ku\in C_tH^{r-k}\). Each time derivative of \(Ru\) is a finite sum of smoothing operators applied to such derivatives, hence belongs to \(C_tH^s\) for every \(s\). The forced Cauchy theorem first gives \(Qu\in C_tH^s\) for every \(s\); differentiating its equation with this smooth forcing gives all time derivatives in every Sobolev order. Thus \(Qu\) is smooth in spacetime. Away from \(\xi=0\), M1–M5 of the spacetime companion make the localized \(Q\) an ordinary spacetime elliptic test at the candidate covector, eliminating it from the spacetime wavefront. This proves equality conditionally, rather than misquoting restriction containment as equality.

Finally \(H_{\tau+b_0}\) has \(\dot t=1\), \(\dot x=b_{0,\xi}\), \(\dot\xi=-b_{0,x}\), \(\dot\tau=-\partial_tb_0\). Along \(\tau=-b_0\), differentiation gives \(\dot\tau=-\partial_tb_0\), since \(H_{b_0}b_0=0\). The fixed-time transported wavefront equality identifies the conditional spacetime wavefront with a union of these full bicharacteristics. The separately restored [smooth real-principal-type propagation lesson U034](../20261005-restored-real-principal/real-principal-type-kernels-and-propagation.md) proves its broader statement by canonical conjugation. Its hypotheses and proof are separate from this Cauchy argument.

## 7. Exact models with different conclusions

The following models distinguish the hypotheses and the conclusions.

- Spatial translation with damping: \(a=i c(t)\cdot\xi+\gamma(t)\), real continuous \(c\), complex continuous \(\gamma\) with bounded real part. For \(C(t)=\int_0^tc(r)dr\), \(G(t)=\int_0^t\gamma(r)dr\), derive
  \(u(t,x)=e^{-G(t)}\phi(x-C(t))+\int_0^t e^{-(G(t)-G(r))}f(r,x-C(t)+C(r))dr\).
  Translation is isometric on every \(H^s\), so this tests signs, nonautonomous flow and the regularity of merely \(L^1\) forcing. Do not claim its special exact norm identity for all symbols.
- Strong continuity without operator-norm continuity: \(a(t,x,\xi)=\chi(x-1/t)\langle\xi\rangle\) for \(t>0\), zero at zero, with compact nonzero smooth nonnegative \(\chi\) in one dimension. It is uniformly \(S^1\) and locally smoothly tends to zero. On \(H^1\to L^2\), \(A_t=\chi(x-1/t)E_1\) has norm exactly \(\|\chi\|_\infty\) for every positive \(t\), because \(E_1\) is an isometry onto \(L^2\). For each fixed vector its output tends to zero by the translated-window \(L^2\) tail. This model also satisfies the scalar nonnegative real-part hypothesis.
- Negative real first-order growth: \(a=-\langle\xi\rangle\) gives \(\widehat u(t,\xi)=e^{t\langle\xi\rangle}\widehat\phi(\xi)\). Take the positive smooth \(\widehat\phi=e^{-\langle\xi\rangle^{1/2}}\). It is Schwartz and belongs to every weighted \(L^2\) space, while the putative positive-time Fourier distribution is positive with exponential growth and is not tempered. Show the last claim by translating a fixed nonnegative compact frequency test to large frequencies; its Schwartz seminorms grow only polynomially, whereas the pairing grows exponentially. This diagnoses failure of the lower real-part hypothesis, not failure under that hypothesis.
- Forward damping without reversible propagation: \(a=\langle\xi\rangle\), \(\phi=\delta_0\in H^r\) for \(r<-n/2\). At positive time \(e^{-t\langle\xi\rangle}\) is rapidly decreasing, so the solution is smooth; exact wavefront equality fails because the principal symbol is real positive rather than purely imaginary. Forward existence remains within the theorem.
- A globally bounded variable speed: \(b_0(x,\xi)=\tanh(x)\xi\). Derive
  \(x=\operatorname{arsinh}(e^t\sinh y)\),
  and, since \(dx/dy=e^t\cosh y/\cosh x\), the covector formula is
  \(\boxed{\xi=e^{-t}\eta\cosh x/\cosh y}\).
  Directly differentiating \(\xi\) gives \(-\operatorname{sech}^2(x)\xi\), and the full symplectic Jacobian is one. At \(y=0\), \(x=0\) and \(\xi=e^{-t}\eta\), a diagnostic exact check. The model operator is \(A=\tanh(x)\partial_x\); \(\operatorname{Re}(Au,u)=-\frac12\int\operatorname{sech}^2(x)|u|^2dx\), so the order-one symbol's zero pointwise real part does not imply a skew-adjoint operator.
- For the same variable speed, \(u(t,x)=\phi(\operatorname{arsinh}(e^{-t}\sinh x))\) for smooth data. Substitution verifies the PDE. Change variables gives the exact \(L^2\) Jacobian \(dx/dy=e^t\cosh y/\cosh x\), between \(1\) and \(e^t\) for \(t\geq0\), so the norm lies between the input norm and \(e^{t/2}\) times it. There is no automatic unitarity of the scalar pullback. For half-densities multiply by \((dy/dx)^{1/2}\) and include the half-divergence term in the generator; that is a different explicitly stated operator.
- Nonautonomous translation, \(c(t)=1+t\): \(C(t)=t+t^2/2\) and \(\chi_{t,r}(y,\eta)=(y+C(t)-C(r),\eta)\). The two-time cocycle holds, while \(C(t+r)\ne C(t)+C(r)\) in general.

## 8. Graded original exercises with complete solutions

**Exercise 1 (foundation: the weighted endpoint).** Compute the exact half-line \(L^p\) norm of \(e^{-\lambda t/2}\) for \(1\leq p<\infty\). Explain why the weighted maximum estimate has no \(\lambda/2\) prefactor and why the threshold in Section 2 can be independent of \(p\).

**Solution.** Integration gives \(\int_0^\infty e^{-p\lambda t/2}dt=2/(p\lambda)\), hence the norm is \((2/(p\lambda))^{1/p}\). Multiplication by \((\lambda/2)^{1/p}\) leaves \(p^{-1/p}\leq1\). At infinity the kernel's supremum is one, and \((\lambda/2)^{1/p}\to1\); the expression is simply \(\max e^{-\lambda t}\|u(t)\|_s\). The pointwise kernel comparison uses \(c_s-\lambda<-\lambda/2\) when \(\lambda>2c_s\), independently of \(p\). Choosing also \(\lambda>0\) gives all the stated cases.

**Exercise 2 (foundation: integrable forcing).** Set \(A=0\), take nonzero \(\psi\in\mathcal S\), \(0<t_0<T\), and \(f(t)=1_{(0,t_0)}(t)\psi\), with zero initial data. Determine the solution and all the time regularity claimed by the theorem. Does it have a continuous time derivative?

**Solution.** The integrated equation gives \(u(t)=\min(t,t_0)\psi\). It belongs to \(C_tH^s\) and is absolutely continuous in every \(H^s\), for every real \(s\). Its almost-everywhere derivative is \(f\). Its one-sided derivatives at \(t_0\) are \(\psi\) and zero, so it is not differentiable there and is not \(C^1\) in time. This example satisfies all symbol hypotheses. It shows why the general theorem asserts absolute continuity one order lower, while \(C^1\) conclusions need stronger forcing regularity.

**Exercise 3 (foundation: strong continuity and the escaped window).** Let \(\chi\geq0\) be a nonzero compact smooth function on the line. For \(t>0\), define \(A_t=\chi(x-1/t)E_1\), and set \(A_0=0\). Prove strong continuity \(H^1\to L^2\) at zero and compute the operator norm for \(t>0\).

**Solution.** For fixed \(w\in H^1\), \(E_1w\in L^2\). If \(\operatorname{supp}\chi\subset[-R,R]\),
\[
 \|A_tw\|_2^2\leq\|\chi\|_\infty^2
 \int_{[1/t-R,1/t+R]}|E_1w(x)|^2dx\longrightarrow0
\]
by the integrable tail of \(|E_1w|^2\). The multiplier \(E_1:H^1\to L^2\) is an isometry onto \(L^2\). Multiplication by the translated \(\chi\) has norm \(\|\chi\|_\infty\): the upper bound is immediate; for each \(\epsilon>0\), an \(L^2\)-normalized function supported where the multiplier exceeds \(\|\chi\|_\infty-\epsilon\) gives the lower bound. Pull that test back by \(E_{-1}\). Thus \(\|A_t\|=\|\chi\|_\infty\) for every positive \(t\), while \(A_0=0\). The left symbols form a bounded \(S^1\) family, tend locally smoothly to zero and are nonnegative real, so the actual hypotheses do not require operator-norm continuity.

**Exercise 4 (foundation: use the correct uniqueness domain).** A homogeneous zero-data solution is assumed only in \(C_tH^s\). At which Sobolev order may the original smooth energy lemma be applied directly, and why?

**Solution.** Strong operator continuity gives \(A(t)u(t)\in C_tH^{s-1}\), so the distributional equation gives \(u\in C^1_tH^{s-1}\). The energy lemma at order \(r\) requires \(C^1H^r\cap CH^{r+1}\). Taking \(r=s-1\) satisfies both requirements. Its right side is zero, so its weighted maximum is zero and \(u=0\). Applying the original lemma at order \(s\) before extending it to the constructed continuous solution would lack its \(C^1H^s\) and \(CH^{s+1}\) assumptions.

**Exercise 5 (intermediate: the measurable norm test).** Suppose \(u\in L^2_tH^s\) represents a functional with \(|\int\langle u,g\rangle dt|\leq K\|g\|_{L^1H^{-s}}\). Prove that \(u\in L^\infty_tH^s\) without invoking a general Banach-valued Radon–Nikodym theorem.

**Solution.** If \(B=\{t:\|u(t)\|_s>K+\epsilon\}\) has positive measure, put \(g=1_BE_{2s}u/\|u\|_s\), setting it to zero outside \(B\). Strong measurability follows from that of \(u\), the continuous multiplier and the measurable scalar normalization. Its \(H^{-s}\) norm is \(1_B\), so it is in \(L^2\) as the time interval is finite, and its \(L^1\) norm is \(|B|\). The dual pairing is \(\langle u,g\rangle=1_B\|u\|_s\). The inequality would give \((K+\epsilon)|B|<\int_B\|u\|_sdt\leq K|B|\), a contradiction. Thus the norm is at most \(K\) almost everywhere. This uses the Hilbert Sobolev dual isometry, not an assertion about all Banach duals.

**Exercise 6 (intermediate: the Sobolev correction).** In one dimension let \(a(x,\xi)=i c(x)\xi\), where all derivatives of the real smooth function \(c\) are bounded. Compute the symbol of \(E_sAE_{-s}-A\) modulo \(S^{-1}\), for arbitrary real \(s\).

**Solution.** In \(E_s\circ a\), the first correction is
\(\partial_\xi\langle\xi\rangle^s D_x(i c\xi)
=s\xi\langle\xi\rangle^{s-2}c'(x)\xi\).
The right factor \(E_{-s}\) depends only on frequency, so its composition on the right is exact pointwise multiplication. Hence the correction is
\[
 s c'(x)\frac{\xi^2}{1+\xi^2}\pmod{S^{-1}}.
\]
Terms with two or more paired derivatives have order at most \(-1\) after conjugation, by the full finite composition remainder. The leading correction is bounded order zero, with no condition that \(s\) be an integer. Its real part need not vanish; this is why the conjugated lower-bound constant may depend on \(s\).

**Exercise 7 (intermediate: the adjoint reversal).** A test \(v\) vanishes near \(T\), and \(g=-v_t+A(t)^*v\). Write the forward equation satisfied by \(w(r)=v(T-r)\), including its initial value and the operator sign.

**Solution.** Differentiation gives \(w_r=-v_t(T-r)\), so
\(w_r+A(T-r)^*w=g(T-r)\), with \(w(0)=v(T)=0\). The operator has the plus adjoint sign. Its form real part equals that of \(A\), and its scalar adjoint symbol is \(\bar a+S^0\), so the sharp lower-bound argument remains applicable. Replacing it by \(-A^*\) would not be this test equation and is generally not justified under the forward lower-bound hypothesis alone.

**Exercise 8 (intermediate: two-time translation).** For speed \(c(t)=1+t\), determine the Hamilton flow \(\chi_{t,r}\). Check the two-time cocycle and test whether \(\chi_{t,0}\chi_{r,0}=\chi_{t+r,0}\).

**Solution.** The principal Hamiltonian is \((1+t)\xi\), so \(\xi\) is constant and \(x(t)-x(r)=C(t)-C(r)\), where \(C(t)=t+t^2/2\). Thus \(\chi_{t,r}(y,\eta)=(y+C(t)-C(r),\eta)\). Adding the two displacements proves \(\chi_{t,r}\chi_{r,q}=\chi_{t,q}\). The one-time composition has displacement \(C(t)+C(r)\), whereas \(C(t+r)=C(t)+C(r)+tr\). They differ when \(tr\ne0\). The flow is nonautonomous; its two-time law is the correct evolution law.

**Exercise 9 (intermediate: the complete tanh cotangent map).** Solve the Hamilton equations for \(b_0(x,\xi)=\tanh(x)\xi\). Compute the full symplectic Jacobian and the covector over the initial point \(y=0\).

**Solution.** Since \(d(\sinh x)/dt=\cosh x\tanh x=\sinh x\),
\(x=\operatorname{arsinh}(e^t\sinh y)\). Its derivative is \(J=\partial_yx=e^t\cosh y/\cosh x>0\). The covector equation is \(\dot\xi=-\operatorname{sech}^2(x)\xi\), and its solution is \(\xi=\eta/J=e^{-t}\eta\cosh x/\cosh y\). Differentiating its logarithmic factor gives \(-1+\tanh^2x=-\operatorname{sech}^2x\), verifying the equation. The full derivative matrix is
\[
 \begin{pmatrix}J&0\\-\eta J_y/J^2&1/J\end{pmatrix},
\]
whose determinant is one and whose pullback of \(dx\wedge d\xi\) is \(dy\wedge d\eta\). At \(y=0\), the trajectory has \(x=0\), and \(\xi=e^{-t}\eta\). Using the base derivative rather than its inverse would produce the opposite covector growth.

**Exercise 10 (advanced: scalar transport and half-densities).** For \(A=\tanh(x)\partial_x\), derive the scalar \(L^2\) norm bounds and the generator of the corresponding unitary half-density transport.

**Solution.** With \(Y(t,x)=\operatorname{arsinh}(e^{-t}\sinh x)\), the scalar solution is \(u(t,x)=\phi(Y(t,x))\). The change of variables \(x=X(t,y)\) gives \(\|u(t)\|_2^2=\int|\phi(y)|^2J(t,y)dy\). Writing \(h=\sinh y\),
\[
 J^2=\frac{e^{2t}(1+h^2)}{1+e^{2t}h^2},\qquad
 J^2-1=\frac{e^{2t}-1}{1+e^{2t}h^2},\qquad
 e^{2t}-J^2=\frac{e^{2t}(e^{2t}-1)h^2}{1+e^{2t}h^2}.
\]
For \(t\geq0\), \(1\leq J\leq e^t\), hence \(\|\phi\|_2\leq\|u(t)\|_2\leq e^{t/2}\|\phi\|_2\). Integration by parts also gives \(\operatorname{Re}(Au,u)=-\frac12\int\operatorname{sech}^2x|u|^2dx\), consistent with possible norm growth. Half-density transport has coefficient \(u_{1/2}(t,x)=\sqrt{Y_x(t,x)}\phi(Y(t,x))\), whose squared norm is exactly \(\|\phi\|_2^2\). If \(L=\partial_t+\tanh x\partial_x\), then \(LY=0\) and \(L Y_x=-\operatorname{sech}^2x\,Y_x\). Therefore its equation is
\((\partial_t+\tanh x\partial_x+\frac12\operatorname{sech}^2x)u_{1/2}=0\).
The added half-divergence makes the spatial generator skew-symmetric on compact smooth tests. This is a different explicitly stated generator from scalar pullback.

**Exercise 11 (advanced: forward damping and lost singularities).** Take \(a(\xi)=\langle\xi\rangle\), zero forcing and \(\phi=\delta_0\). Show that this satisfies the forward theorem but does not satisfy its reversible wavefront theorem.

**Solution.** The initial datum lies in \(H^r\) for every \(r<-n/2\), since its Fourier transform is one and \(\int\langle\xi\rangle^{2r}d\xi\) converges exactly in that range. The symbol is ordinary order one, independent of time and nonnegative real. The solution has Fourier transform \(e^{-t\langle\xi\rangle}\), which is Schwartz for each \(t>0\). It is therefore smooth and has empty fixed-time wavefront, while \(\delta_0\) has all nonzero directions over zero in its wavefront. The principal symbol is real positive, not purely imaginary. Reversing its operator would give the forbidden negative real growth, so the second inclusion proof is unavailable. The forward existence theorem is fully consistent with this smoothing.

**Exercise 12 (advanced: a precise ill-posed sign).** Let \(a=-\langle\xi\rangle\) and \(\widehat\phi=e^{-\langle\xi\rangle^{1/2}}\). Prove that the datum is Schwartz but the proposed positive-time solution is not tempered.

**Solution.** Every derivative of the Fourier datum is a finite sum of polynomially bounded factors times its exponential decay; every polynomial weight is absorbed by that decay. Thus \(\widehat\phi\in\mathcal S\), and Fourier inversion gives \(\phi\in\mathcal S\). The Fourier equation, localized to any bounded frequency open set, is the scalar distributional ODE \(\partial_t\widehat u-\langle\xi\rangle\widehat u=0\), whose integrating factor determines \(\widehat u=e^{t\langle\xi\rangle-\langle\xi\rangle^{1/2}}\). For fixed \(t>0\), pair this positive function with a fixed nonnegative compact test translated to \(R e_1\). On a smaller ball where that test is positive the pairing is bounded below by a positive constant times \(e^{t(R-O(1))-O(\sqrt R)}\). Every fixed Schwartz seminorm of the translated test grows at most polynomially in \(R\). This contradicts the finite-seminorm bound required of a tempered distribution. The scalar symbol has unbounded negative real part, so hypothesis 3 excludes exactly this mechanism.

**Exercise 13 (advanced: all degree-three recursion terms).** In the commuting-symbol expansion, list all \((k,\ell,|\alpha|)\) contributing at degree \(-3\) after the leading term for \(Q_3\) is removed. Verify that every remaining \(Q\)-index is smaller than three.

**Solution.** The degree is \(1-k-\ell-|\alpha|\), so the equation is \(k+\ell+|\alpha|=4\), with \(|\alpha|\geq1\). Removing \((0,3,1)\), the triples are
\[
 \{(1,2,1),(2,1,1),(3,0,1),
 (0,2,2),(1,1,2),(2,0,2),
 (0,1,3),(1,0,3),(0,0,4)\}.
\]
All have \(\ell\leq2\). Their coefficients are the sums over the actual multi-indices of the stipulated length, with factor \(i/\alpha!\) and the ordered derivative difference from Section 5. Thus the source term is already known before solving the linear transport equation for \(Q_3\). For general \(j\), if \(\ell=j\), the nonnegative-index equation forces \(k=0,|\alpha|=1\); removing that leading pair proves the same triangular property.

**Exercise 14 (advanced: two smoothing errors are enough).** Suppose \(Q(0)-q\) and \([P,Q]\) are uniformly smoothing, rather than zero. Explain why the wavefront removal argument still works, and identify the regularity used for its forcing.

**Solution.** If \(u\in C_tH^r\), uniform smoothing symbol bounds and strong continuity give \([P,Q]u\in C_tH^s\) for every \(s\). At zero, \((Q(0)-q)\phi\in H^s\) for all \(s\); the chosen conic test also gives \(q\phi\in H^\infty\). The exact equation is \(P(Qu)=[P,Q]u\) with that smooth initial datum. The Cauchy theorem constructs a solution in \(C_tH^s\) at each order. It agrees with \(Qu\) by uniqueness at any common lower order. Thus \(Qu\) is spatially smooth, and a nonzero leading symbol \(Q_0\) is an elliptic test removing the covector. Nothing in this argument requires division by a smoothing error or exact commutation.

**Exercise 15 (advanced: restriction containment and propagation equality).** Compute the normals to the inclusion \(j_{t_0}(x)=(t_0,x)\). Explain which inclusion of the conditional spacetime/slice equality follows from the pullback theorem, and where the other inclusion comes from.

**Solution.** The transpose derivative sends \((\tau,\xi)\) to \(\xi\), so the nonzero normals are \((t_0,x;\tau,0)\), \(\tau\ne0\). If the wavefront avoids them, the pullback theorem gives
\(\operatorname{WF}(u(t_0))\subset\{(x,\xi):(t_0,x;\tau,\xi)\in\operatorname{WF}(u)\text{ for some }\tau\}\).
Away from \(\xi=0\), the equation forces \(\tau=-b_0\), giving the stated left-to-right containment. Conversely, a spatially regular direction at \(t_0\) admits a transported elliptic test \(Q\) whose output is smooth in spacetime under the extra time-smooth hypotheses. Its spacetime localization is ordinary and elliptic at the corresponding nonzero-\(\xi\) covector, so that covector is absent from the spacetime wavefront. This contrapositive gives the reverse inclusion. The restriction theorem alone never states this equality.

**Exercise 16 (advanced: a scalar hypothesis is not a system condition).** Consider the matrix symbol \(a(\xi)=\langle\xi\rangle\begin{pmatrix}0&1\\0&0\end{pmatrix}\). Its entries have nonnegative real parts and both eigenvalues are zero. Compute its Hermitian real part and show a loss of Sobolev regularity in its Cauchy evolution.

**Solution.** The Hermitian real part is \(\frac12\langle\xi\rangle\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with eigenvalues \(\pm\langle\xi\rangle/2\). It has no uniform lower bound by \(-C I\). The system is \(\partial_tu_2=0\), \(\partial_tu_1+E_1u_2=0\); hence \(u_2(t)=\phi_2\), \(u_1(t)=\phi_1-tE_1\phi_2\). Choose \(\phi_1=0\) and \(\phi_2\in H^s\setminus H^{s+1}\). Then for every positive \(t\), \(u_1(t)\notin H^s\), although both initial components lie in \(H^s\). Such data exist, for example by a sum of disjoint normalized Fourier annuli with weighted \(H^s\) norms \(2^{-j/2}\); the corresponding \(H^{s+1}\) squares grow like \(2^j\). Thus neither entrywise inequalities nor real eigenvalue tests replace the Hermitian-form condition needed for a system energy theorem.

## 9. Sources and scope

The mathematical antecedents are Hörmander, *The Analysis of Linear Partial Differential Operators III*, approved 2007 eBook ISBN 978-3-540-49938-1, reprint of the corrected second printing, §23.1 including Lemma 23.1.1, Theorem 23.1.2, Corollary 23.1.3, the complete commuting-symbol argument and Theorem 23.1.4. The section ends before §23.2 on the shared. The mathematical antecedents for the two complete spacetime companions are Volume III, Theorem 18.1.35 and Volume I, Theorem 8.2.4. The exact included programme positivity, symbol, integral and microlocal proofs are identified in Section1. These references give credit for the mathematics; the explanations, proof organization, models and graded exercises here are original teaching text.

The propagation proof uses a uniformly bounded classical symbol family with its coefficient and remainder bounds, homogeneous forcing, and initial data in a Sobolev space. The spacetime statement additionally uses smooth time coefficients and retains the possible pure temporal directions; its slice equality is conditional on excluding those directions. The system extension, elliptic FIO construction of the evolution kernel and higher-order Cauchy theory require their separate receiving reviews. U034 supplies the already restored smooth real-principal-type propagation proof.

Restoration review by GPT-6 Astra (OpenAI), Ultra, 5 October2026; the full receiving proof and all sixteen original solutions were checked against the approved editions and complete included programme proofs. Ten finite model groups verify the listed characteristic, Jacobian, convolution, sign, degree, half-density and system computations. Two additional finite groups check the mixed composition correction and slice conormal. Those finite checks do not certify the general functional-analytic or microlocal theorems. Human review and full-course coverage remain pending. The receiving exposition is CC0; the separately identified retained AN-03 companions carry their complete GFDL1.2 notices.
