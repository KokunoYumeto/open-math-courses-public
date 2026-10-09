# Graph operators, continuity and Egorov

An FIO associated with a canonical graph moves one cotangent direction to one other direction. After dividing its symbol by the graph's symplectic half volume, an order-zero graph operator behaves on \(L^2\) like an order-zero pseudodifferential operator. The same graph calculus constructs inverses and transports pseudodifferential symbols by canonical changes of variables. After a characteristic direction has been straightened, an ordered transport construction removes every lower-order term, including finite matrix terms under a scalar principal direction.

The local phase and symbol inputs are [Phase space and generating families](../20261005-restored-phase-space/phase-space-and-generating-families.md), [Recognizing a Lagrangian distribution intrinsically](../20261005-restored-intrinsic-regularity/intrinsic-lagrangian-regularity.md), [Gaussian lines, densities and invariant symbols](../20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.md), and Kernels, adjoints and clean composition. The coordinate second-jet construction is in [Hamilton fields and subprincipal transport](../20261005-restored-subprincipal-transport/hamilton-fields-and-subprincipal-transport.md).

The exact quantitative inputs are [dyadic endpoint B3–B6](../20261004-free-intrinsic-graph/prerequisites/dyadic-endpoint.md), which proves the finite-seminorm ordinary PDO bound on every real Sobolev scale, and [ordinary operator calculus O3–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), which proves amplitude reduction, full composition remainders, proper representation and the smoothing ideal. [Conic parametrices K1–K4](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) supply supported sums and exact two-sided matrix inverses on a fixed cone. The included [global-inverse and circle-multiplier companion](global-inverses-and-periodic-multipliers.md) proves the global patching and periodic multiplier assertions used below. [Compactness T1–T2](../20261004-free-canonical-composition/compactness-and-essential-norms.md) proves the Hilbert adjoint, product-kernel approximation and compact norm-limit arguments. [FIO mapping W1, W2 and W6](../20261004-free-canonical-composition/fio-sobolev-mapping.md) supplies the existing smooth-kernel estimates, finite-seminorm graph proof and support-controlled Sobolev approximation. Their conventions are \(D=-i\partial\), Fourier phase \(-y\cdot\eta\), and inverse factor \((2\pi)^{-n}\). The [proof map](proof-map.json) identifies every exact prerequisite, including the graph density contraction in the restored [linear-reduction lesson, Section 8](../20261005-restored-linear-reduction/reduction-and-linear-symbol-composition.md).

The primary source is the reprint of Hörmander IV, corrected second printing (1994), [§25.3], through Theorem 25.3.5. The lower-term conjugation construction also uses Volume IV, Proposition 26.1.3, with its exact matrix-ODE and symbol proof providers identified at the point of use. Symbols are ordinary \(S_{1,0}\) symbols. Every noncompact-manifold estimate is local over compact base sets. The canonical relations have the full punctured-cotangent closure and both nonzero covectors specified in the composition lesson. Later corank and fold estimates require additional geometry; their different losses are not consequences of the graph theorem alone.

## 1. Divide out the symplectic half volume

Suppose \(C\) is the graph of a homogeneous canonical diffeomorphism \(\chi:U_Y\to U_X\) between open punctured cotangent cones. Then \(\dim X=\dim Y=n\). Either projection identifies the graph with a symplectic manifold, with common form
\[
\omega_C=\pi_X^*\omega_X=\pi_Y^*\omega_Y.
\tag{1.1}
\]
Its positive symplectic volume and half volume are
\[
v_C=\left|\frac{\omega_C^n}{n!}\right|,
\qquad v_C^{1/2}.
\tag{1.2}
\]
Cotangent dilation pulls \(\omega_C\) back to \(t\omega_C\), so the half volume has degree \(n/2\). The intrinsic symbol of an order-\(m\) kernel on \(X\times Y\) has order \(m+n/2\). Consequently its **reduced graph symbol**
\[
\alpha=\sigma(A)/v_C^{1/2}
\tag{1.3}
\]
has order \(m\), in the Maslov line and the lifted bundle \(\operatorname{Hom}(F,E)\), modulo one lower order. A local Maslov frame turns it into an ordinary matrix symbol. The half volume is canonical; choosing coordinate Lebesgue measures is unnecessary for (1.3).

When one factor of a clean composition is a graph, the matching fiber is a point and the excess is zero. The graph-factor density contraction proved in the linear-symbol lesson removes this half volume exactly. Thus reduced graph symbols compose by their ordered bundle maps and the canonical Maslov identification. The identity graph has unit reduced symbol. The inverse graph and the adjoint use the inverse and conjugated Maslov lines already identified in the adjoint theorem.

For scalar half densities, \(\|u\|_2^2=\int|u|^2\) is intrinsic. For finite-rank bundles choose smooth Hermitian metrics. On each compact chart their norms are uniformly equivalent to component norms, so the local boundedness and compactness assertions below do not depend on that choice. Formal adjoints in these Hilbert spaces agree with the previously proved anti-dual adjoints after the metric identifications.

## 2. A mixed generating function gives a left operator form

**Proposition 2.1.** Near any point of a homogeneous canonical graph, input base coordinates can be chosen, while keeping the output base coordinates fixed, so that
\[
C=\{(x,\phi_x(x,\eta);y=\phi_\eta(x,\eta),\eta)\},
\qquad\det\phi_{x\eta}\neq0,
\tag{2.1}
\]
where \(\phi\) is homogeneous of degree one in \(\eta\).

**Proof.** At the point, take the inverse image under \(\chi\) of the output vertical cotangent fiber. It is a conic Lagrangian in \(T^*Y\). The input covector is nonzero. The diagonal-complement lemma and the input-coordinate second-jet construction of the transport lesson therefore make its tangent plane transverse to the horizontal plane in the new input coordinates.

A tangent vector to \(C\) with \(\delta x=0\) lies in this inverse image of the output vertical plane. If also \(\delta\eta=0\), the new transversality forces its input tangent vector to be zero, and the diffeomorphism forces its output vector to be zero. Thus projection from \(C\) to \((x,\eta)\) has injective differential. Both spaces have dimension \(2n\), so these are local coordinates on the graph.

Write \(y=y(x,\eta)\), \(\xi=\xi(x,\eta)\). Homogeneity makes \(y\) degree zero and \(\xi\) degree one. The conic Lagrangian identity in the signed product is
\[
\xi\cdot dx-\eta\cdot dy=0\quad\text{on }C.
\]
Therefore \(\phi=\eta\cdot y(x,\eta)\) satisfies
\[
d\phi=\xi\cdot dx+y\cdot d\eta.
\]
It gives (2.1). Projection to \((x,\xi)\) is a diffeomorphism because \(C\) is a graph with a diffeomorphic inverse. Its expression in the new parameters is \((x,\eta)\mapsto(x,\phi_x)\), whose determinant is \(\det\phi_{x\eta}\). That determinant is nonzero. ∎

The phase \(\Phi(x,y,\eta)=\phi(x,\eta)-y\cdot\eta\) is nondegenerate: its critical equations are \(\phi_\eta-y=0\), with derivative \(-I\) in \(y\). The kernel normalization and amplitude order are
\[
K_A(x,y)=(2\pi)^{-n}\int e^{i\Phi}a(x,y,\eta)\,d\eta,
\qquad a\in S^m.
\tag{2.2}
\]
The local phase converse supplies this form modulo a smooth kernel. In parameters \((x,\eta)\), its critical density is \(|dx\,d\eta|\), so its intrinsic symbol is the critical restriction
\[
a(x,\phi_\eta,\eta)|dx\,d\eta|^{1/2}
\tag{2.3}
\]
in the Maslov frame associated with \(\Phi\). On the other hand,
\[
v_C^{1/2}=|\det\phi_{x\eta}|^{1/2}|dx\,d\eta|^{1/2}.
\]
Hence the reduced graph symbol in this frame is
\[
\alpha=a(x,\phi_\eta,\eta)|\det\phi_{x\eta}|^{-1/2}.
\tag{2.4}
\]

The amplitude can be made independent of \(y\). Put \(a_0(x,\eta)=a(x,\phi_\eta,\eta)\). Taylor's integral formula expresses \(a-a_0\) as \(\sum_j(y_j-\phi_{\eta_j})a_j\), with \(a_j\in S^m\). In the oscillatory integral,
\[
(y_j-\phi_{\eta_j})e^{i\Phi}
=-\frac1i\partial_{\eta_j}e^{i\Phi},
\]
so integration by parts replaces this term by \(D_{\eta_j}a_j\), of order \(m-1\). Derivatives of \(\phi_\eta\) cost one frequency order. Repeating and using the support-preserving asymptotic sum K1 gives \(b(x,\eta)\in S^m\) with
\[
(Au)(x)=(2\pi)^{-n}\int e^{i\phi(x,\eta)}b(x,\eta)\widehat u(\eta)\,d\eta
\tag{2.5}
\]
microlocally modulo a smooth kernel. All finite remainders have the stated lower orders. Base and angular supports remain in slightly enlarged compact interior sets. Remove a bounded-frequency piece into the smooth remainder, so the working amplitude vanishes near zero. This is a local normal form; base cutoffs equal to one on the working graph patch are retained when estimating operators.

## 3. Order zero gives local L2 continuity

**Theorem 3.1 (graph continuity).** If \(C\) is locally the graph of a homogeneous canonical transformation and \(A\in I^0(X\times Y,C';\Omega^{1/2}\otimes\operatorname{Hom}(F,E))\), then
\[
A:L^2_{\mathrm{comp}}(Y;\Omega^{1/2}\otimes F)
\longrightarrow L^2_{\mathrm{loc}}(X;\Omega^{1/2}\otimes E)
\tag{3.1}
\]
is continuous. For a fixed phase patch and fixed compact support data, its localized operator norm is bounded by finitely many order-zero amplitude seminorms.

Here continuity means that for each compact input support and each compact output cutoff, the output \(L^2\) norm has a bound by the input \(L^2\) norm. It does not assert a uniform estimate across a noncompact manifold.

**Proof on one graph patch.** Localize the kernel to a compact coordinate product and to a sufficiently small graph cone. Call the resulting operator \(T\). Both base support projections are now proper. Shrink the cone so that \(C^{-1}\circ C\) in this patch is the identity graph. Its matching fibers are points. The adjoint and composition theorems give
\[
T^*T\in\Psi^0(Y),
\qquad\sigma(T^*T)=\alpha^*\alpha.
\tag{3.2}
\]
The identity-relation kernel class is exactly the pseudodifferential class: choose the phase \((y-z)\cdot\eta\) and apply the local converse, followed by the exact amplitude reduction O4. The compactly localized smooth remainder stays smooth.

The exact B4 estimate at order and Sobolev exponent zero now gives \(\|T^*T\|_{2\to2}\leq C\). For compact smooth \(u\),
\[
\|Tu\|_2^2=(T^*Tu,u)\leq C\|u\|_2^2.
\tag{3.3}
\]
The pairing identity follows on these smooth inputs from the kernel adjoint; its outputs are compact smooth by the nonzero-covector mapping theorem. Thus no bounded extension of \(T\) has been assumed in using (3.3). Density gives its unique bounded \(L^2\) extension.

The constants depend on finitely many amplitude seminorms. Indeed the composition construction is bilinear and has finite-seminorm estimates on fixed phase/support data. To recover the finitely many ordinary pseudodifferential symbol derivatives required by B4, perform its Fourier reduction to a finite order, and leave a sufficiently negative remainder. The finite coefficients and the absolutely integrable remainder use finitely many input derivatives. The latter remainder and the smooth kernel are controlled in the kernel norms used by the elementary integral estimate. This yields
\[
\|T\|_{2\to2}\leq C p_{0,L}(a)
\tag{3.4}
\]
for a finite \(L\) and the fixed working data. An infinite asymptotic-sum choice is unnecessary for this estimate.

**Assembly.** For fixed compact input and output base supports, the closed normalized kernel relation is compact and contains no covector on either axis. Cover it by finitely many small graph cones and use a smooth phase partition. Each piece has the bound just proved. The residual kernel is smooth on the compact base product and has a bounded integral-operator norm by Cauchy–Schwarz. Sum these finitely many bounds. They prove (3.1), including finite-rank bundle coefficients by B4 applied to the finitely many matrix components and equivalence of local Hermitian norms.

Several different graph branches may occur in the full relation. We have only applied (3.2) to each single graph patch. Cross-products between different patches need not have the identity relation, and no claim that the full \(A^*A\) is pseudodifferential is needed. ∎

For the left form (2.5), a direct calculation makes its finite-seminorm estimate particularly explicit. Cut the amplitude to a small compact output patch and an interior angular cone. First truncate frequency smoothly, writing \(b_R=h(\eta/R)b\), with real \(h\). These operators \(T_R\) have bounded-frequency \(L^2\) kernels, so their Hilbert adjoints and products already exist. Plancherel in the input variable gives their product kernel
\[
(T_RT_R^*)(x,x')=(2\pi)^{-n}\int
e^{i(\phi(x,\eta)-\phi(x',\eta))}
b_R(x,\eta)b_R(x',\eta)^*\,d\eta.
\tag{3.5}
\]
Use a small convex output chart and put
\[
F(x,x',\eta)=\int_0^1\phi_x(x'+t(x-x'),\eta)\,dt.
\]
Then the phase difference is \((x-x')\cdot F\). Take the angular cone to be convex and small around a fixed ray. Homogeneity and continuity allow the output chart and this cone to be chosen so that \(\|F_\eta-A\|<\varepsilon<\|A^{-1}\|^{-1}\) for one fixed invertible matrix \(A\), uniformly in \(x,x'\). Integrating the derivative along the segment between two frequencies in this convex cone gives \(|F(\eta)-F(\eta')|\ge(\|A^{-1}\|^{-1}-\varepsilon)|\eta-\eta'|\). Thus the frequency map is injective on the whole selected cone. The inverse theorem supplies its smooth inverse; homogeneity also gives uniform frequency comparability and all inverse derivative bounds on smaller closed angular sets. Hence \(\zeta=F(x,x',\eta)\) is a homogeneous frequency diffeomorphism onto its image. The amplitude has interior angular support, so its transformed zero extension across the edge of that image is smooth. Changing variables turns (3.5) into an ordinary order-zero PDO amplitude with phase \((x-x')\cdot\zeta\). Its coefficient is
\[
b_R(x,\eta)b_R(x',\eta)^*|\det F_\eta|^{-1},
\tag{3.6}
\]
evaluated at the inverse frequency map. Homogeneity and the chain rule give order-zero bounds uniformly in \(R\). A base derivative of the inverse frequency costs one frequency power, canceled by the frequency derivative of its symbol factor. Derivatives of the cutoff obey the same bounds on its transition annulus.

The quantitative amplitude reduction O4 and the estimate B4 therefore bound \(\|T_RT_R^*\|\) by \(C p_{0,L}(b)^2\), for a finite \(L\) independent of \(R\). The Hilbert adjoint pairing gives \(\|T_R\|\leq C p_{0,L}(b)\). On Schwartz inputs the truncated integrals converge to (2.5), since the input Fourier transform decreases rapidly; their compact-output pointwise limit and the uniform bound give the same norm inequality for the limiting operator, followed by density. Thus
\[
\|T(b)\|_{2\to2}\leq C p_{0,L}(b)
\tag{3.7}
\]
on these fixed supports. Bounded input cutoffs preserve the estimate. This proof uses an actual frequency change and finitely many ordinary amplitude derivatives; it will control the norm of high-frequency tails in the compactness proof.

## 4. A symbol tending to zero gives localized compactness

The symbol limit in this section is uniform over compact base products and over their normalized graph directions. It is a statement about the reduced order-zero symbol; adding a representative of order \(-1\) preserves it.

**Lemma 4.1 (small symbols have small fixed jets).** Let \(b\in S^0\) on a fixed compact-base, compact-angular patch, and suppose \(b(x,\eta)\to0\) uniformly as \(|\eta|\to\infty\). If \(h\in C_c^\infty\) equals one near zero, then
\[
b_R=(1-h(\eta/R))b
\longrightarrow0
\quad\text{in every fixed }S^0\text{ seminorm}.
\tag{4.1}
\]

**Proof.** On a slightly enlarged compact frequency annulus put \(F_r(x,\omega)=b(x,r\omega)\), \(r\geq1\). All derivatives in \((x,\omega)\) are bounded uniformly in \(r\), by the order-zero symbol estimates, while \(\|F_r\|_\infty\to0\). Finite Taylor estimates imply that each fixed derivative also tends uniformly to zero on a smaller annulus and base set. For the first derivative in one direction, Taylor's formula gives, whenever the segment remains in the larger set,
\[
|\partial_jF_r|\leq\frac{2\|F_r\|_\infty}{\delta}
+\frac\delta2\|\partial_j^2F_r\|_\infty.
\tag{4.2}
\]
First choose small \(\delta>0\), then large \(r\). Repeating the argument on successive derivatives, with finitely many nested interior sets, proves the assertion for any prescribed finite jet. A finite cover makes it uniform. Returning to physical frequencies turns each \(\omega\)-derivative into the corresponding weighted frequency derivative. The same bounds hold uniformly for all \(r\) above a large threshold.

In (4.1), derivatives hitting \(h(\eta/R)\) are supported where \(|\eta|\asymp R\); the seminorm weight cancels their \(R^{-1}\) factors. Derivatives not hitting it are supported above a fixed multiple of \(R\), where the preceding uniform jet bounds tend to zero. Leibniz's rule proves (4.1). Zero extension from the interior supporting patch permits the enlarged sets used in the Taylor estimates. ∎

This lemma uses the extra uniform zero limit. For a general order-zero symbol, frequency truncations need not converge in the same-order symbol topology.

**Theorem 4.2 (graph compactness).** Under Theorem 3.1, if the reduced principal symbol tends uniformly to zero at infinity over every compact subset of \(X\times Y\), then every localized operator \(\chi_X A\chi_Y:L^2(Y)\to L^2(X)\), with compact smooth base cutoffs, is compact.

**Proof.** Reduce to finitely many graph patches and a smooth compact kernel, as in Theorem 3.1. On one patch use (2.5). Its symbol is \(b|\det\phi_{x\eta}|^{-1/2}\) modulo order \(-1\). The determinant and its inverse are bounded on the compact normalized patch. Thus the hypothesis implies the zero limit for \(b\) itself. Lemma 4.1 and the finite-seminorm graph estimate give
\[
\|T(b)-T(h(\eta/R)b)\|_{2\to2}\longrightarrow0.
\tag{4.3}
\]
The bounded-frequency operator has an \(L^2\) kernel. For example, Fourier inversion in the input variable and Plancherel give
\[
\|K_R\|_{L^2(dx\,dy)}^2
=(2\pi)^{-n}\iint|h(\eta/R)b(x,\eta)|^2\,dx\,d\eta<\infty
\tag{4.4}
\]
before an additional bounded input cutoff. The output base support is compact and the frequency support is bounded. The phase factor has absolute value one.

An \(L^2\) kernel is compact: approximate it in \(L^2\) by finite sums of product functions of the two variables. Their operators have finite rank, and Cauchy–Schwarz bounds the operator-norm difference by the kernel's \(L^2\) difference. The complete product-kernel approximation is proved in T2, using compact smooth density M7 and rectangular step approximations. T1 proves that norm limits of compact operators are compact. The same proof handles matrix components. Hence (4.3) is a norm limit of compact operators, and is compact. Smooth kernels localized to compact base products are compact by this same argument. Finitely many pieces prove the theorem. ∎

This proves the stated compactness directly from the graph estimates and the symbol limit. It makes no assertion about global compactness without the relevant support or geometry bounds.

## 5. Every real Sobolev order shifts by the operator order

**Theorem 5.1.** For \(A\in I^m\) with locally graph relation as above, and every real \(s\),
\[
A:H^s_{\mathrm{comp}}(Y)\longrightarrow H^{s-m}_{\mathrm{loc}}(X)
\tag{5.1}
\]
continuously, with the same half-density and finite-rank bundle coefficients.

**Proof.** Fix input and output compact localizations. Choose proper elliptic order reducers \(B_Y\in\Psi^s(Y)\), \(B_X\in\Psi^{s-m}(X)\), and a proper parametrix \(C_Y\in\Psi^{-s}(Y)\) of \(B_Y\). These real-order constructions and their localized elliptic norm test are proved in W6 using B4 and K3–K4; the global inverse construction is also proved in companion G0. Arrange an output localization of \(B_X\) to the larger compact set needed for the chosen output cutoff. The graph calculus gives
\[
B_XAC_Y\in I^0.
\]
On compact smooth inputs the exact identity is
\[
B_XA=(B_XAC_Y)B_Y+B_XA(I-C_YB_Y).
\tag{5.2}
\]
The first term maps \(H^s\) to \(L^2\): B4 gives \(B_Y:H^s\to L^2\), with proper support keeping a common compact input set for the graph operator, and Theorem 3.1 treats the order-zero middle factor.

The second term has a smooth kernel on the localized base product. The proper smoothing error \(I-C_YB_Y\) has compact output support relevant to the input support. The FIO smooth-input theorem and its adjoint version show that composing such a smooth kernel with \(A\) is smooth; differentiating compact smooth test families proves every derivative. It therefore maps the fixed compact \(H^s\) input space to every local smooth and Sobolev space. Thus (5.2) bounds \(B_XAu\) in \(L^2\).

Use a proper local parametrix \(C_X\) of \(B_X\). On the smaller output set,
\[
Au=C_XB_XAu+R_XAu,
\]
where \(R_X\) is the localized smoothing error. The first term belongs to \(H^{s-m}\) by B4. The second has a smooth localized kernel when composed with \(A\), by the same adjoint smooth-input argument. These bounds prove (5.1) for smooth inputs. The compact smooth approximation proved in W6, using Fourier truncation and a fixed outer cutoff, converges in \(H^s\) with one common slightly larger compact support and gives the unique extension. Its distributional limit agrees with the original kernel action by the compact-distribution continuity of the mapping theorem. Local partitions prove the bundle and manifold assertions. ∎

## 6. Elliptic graph operators have two-sided parametrices

Assume now that \(C\) is the graph of a homogeneous canonical bijection
\[
\chi:T^*Y\setminus0\longrightarrow T^*X\setminus0.
\tag{6.1}
\]
An order-\(m\) graph FIO is **noncharacteristic** at a point if its reduced symbol has an inverse of order \(-m\) in a conic neighborhood, in the inverse Maslov line and reversed Hom bundle. The two ordered products equal identity modulo order \(-1\). It is **elliptic** if this holds everywhere. This includes the symbol bounds on the inverse; pointwise invertibility alone is insufficient for an arbitrary nonhomogeneous symbol. In the classical case it is the usual nonvanishing or matrix-isomorphism condition on normalized compact cone slices.

**Support lemma.** The base projection of a global graph (6.1) is a closed relation with both base projections proper. Any distribution with wavefront contained in its twisted graph can consequently be replaced, modulo a smooth kernel, by one with proper base support.

**Proof.** For input base points in a compact set, normalize input covectors to length one in finitely many charts. Their set is compact. Homogeneity makes the output base independent of the covector radius; continuity of \(\chi\) therefore confines it to a compact set. Apply \(\chi^{-1}\) for the other projection. For a convergent sequence of base pairs in this relation, normalize the input covectors and take a subsequence. Their output covectors are bounded and bounded away from zero on that compact set, since \(\chi\) is a homogeneous diffeomorphism. The limit yields a graph point over the limiting base pair. Thus the base relation is closed.

We justify the proper cutoff as well. Choose compact exhaustions \(K_j\) of \(X\) and \(L_j\) of \(Y\), each lying inside the next interior. Properness lets us choose integers \(N(j)>j\), \(M(j)>j\) so that the relation avoids
\[
K_j\times(Y\setminus\operatorname{int}L_{N(j)}),
\qquad
(X\setminus\operatorname{int}K_{M(j)})\times L_j.
\]
The union of these closed forbidden sets is locally finite: on a fixed compact product the forbidden outside factor is absent for every sufficiently large \(j\). Its complement is an open neighborhood of the relation. The closure of this neighborhood has both projections proper; over \(K_j\), use the bound from \(K_{j+1}\) to include boundary points, and do the reverse for \(L_j\).

A smooth partition subordinate to this neighborhood and the complement of the closed relation supplies a cutoff equal to one near the relation and supported in that proper neighborhood. Multiplying the kernel by it gives proper support. The difference is smooth, since its multiplier vanishes near the base projection of every permitted wavefront point. ∎

**Theorem 6.1 (elliptic graph parametrix).** A proper elliptic \(A\in I^m(X\times Y,C';\Omega^{1/2}\otimes\operatorname{Hom}(F,E))\) has a proper
\[
B\in I^{-m}(Y\times X,(C^{-1})';\Omega^{1/2}\otimes\operatorname{Hom}(E,F))
\tag{6.2}
\]
such that \(AB-I\) and \(BA-I\) have smooth kernels. At a single noncharacteristic point the corresponding two identities hold microlocally on smaller input and output cones.

**Proof.** The inverse reduced symbol is a section of the inverse-relation symbol bundle: the graph-factor Maslov product identifies its product with the original symbol as the identity unit, and the bundle map is the ordinary inverse map. The invariant-symbol surjectivity theorem realizes it by an FIO \(B_0\) of order \(-m\). The support lemma permits a proper representative without changing its symbol.

The graph composition theorem gives proper order-zero pseudodifferential operators
\[
P_X=AB_0,\qquad P_Y=B_0A,
\tag{6.3}
\]
with identity principal symbols. The global proper matrix parametrix proved in companion G0 supplies proper order-zero \(R_X,S_Y\) with \(P_XR_X-I\) and \(S_YP_Y-I\) smooth. Set
\[
B_R=B_0R_X,\qquad B_L=S_YB_0.
\tag{6.4}
\]
They have the order and relation in (6.2), with proper support. Their right and left inverse identities follow from (6.3). Moreover
\[
B_L-B_R
=B_L(I-AB_R)+(B_LA-I)B_R.
\tag{6.5}
\]
Both terms have smooth kernels: smooth proper kernels form a two-sided ideal with proper FIOs, by the proved smooth-input and adjoint mappings. Thus either representative is a two-sided inverse modulo smooth kernels. This uses the exact conic construction K3 and the locally finite global patching in G0; it does not assume convergence of a bounded-operator Neumann series.

For the local statement, extend the inverse symbol with interior cone cutoffs and use the conic PDO parametrix construction. The same identities hold on smaller cones because changes of extension and separated supports are microlocally smoothing. The graph carries these input cones diffeomorphically to output cones, so the left/right comparison applies there. ∎

## 7. Egorov transports symbols by the canonical map

Let \(C\) be the graph in (6.1), \(A\in I^m(C')\), \(B\in I^{-m}((C^{-1})')\), and let \(P\in\Psi^\mu(X)\). Suppose all three operators are proper. They need not satisfy any inverse identity. Use reduced symbols \(\alpha,\beta\) for \(A,B\), and principal symbol \(p\) for \(P\). In the formulas below regard \(\beta\) as pulled back to \(C\) by the interchange of its two graph members; its bundle map still goes from \(E_x\) to \(F_y\).

**Theorem 7.1 (ordered Egorov formula).** The operator \(Q=BPA\) is a proper pseudodifferential operator of order \(\mu\) on \(Y\). Its principal symbol is
\[
q(\gamma)=\beta(\chi\gamma,\gamma)\,
p(\chi\gamma)\,
\alpha(\chi\gamma,\gamma),
\tag{7.1}
\]
where the inverse Maslov factors are contracted canonically and the bundle maps remain in the displayed order. For scalar \(P\), if \(c\) is the principal symbol of \(BA\), this becomes
\[
q=c\,(p\circ\chi).
\tag{7.2}
\]
In particular a microlocal inverse \(B\) gives \(c=1\) there. For matrix-valued \(p\), the inverse case gives \(q=\alpha^{-1}(p\circ\chi)\alpha\).

**Proof.** The identity graph of \(P\) composed with \(C\) gives \(C\), with excess zero and symbol \(p\alpha\). Composing with the inverse graph gives the identity relation on \(Y\), again with excess zero. Its kernel class is \(\Psi^\mu\), and its symbol is exactly the ordered product (7.1). Proper kernel support is preserved by the already proved support theorem. Scalar \(p\) commutes with the Hom maps, leaving \(c=\beta\alpha\) and (7.2). The inverse identity and the matrix formula follow by substituting \(\beta=\alpha^{-1}\) in this same ordered product. ∎

The theorem has a local conic version. Choose the inverse only near the desired covector, use proper interior cutoffs, and apply the same two compositions on smaller cones. It is principal-symbol transport; subsequent removal of lower terms requires additional arguments.

It also justifies changes of canonical coordinates for a general FIO relation. Choose local elliptic graph FIOs quantizing the desired homogeneous canonical changes on the two sides, using symbol surjectivity and nonzero local Maslov units. Composition replaces \(C\) by \(C_1\circ C\circ C_2\), with zero excess from the graph factors and unchanged order. Their microlocal parametrices undo the change. Order-zero graph quantizations and their inverses preserve the local \(L^2\) estimates. These facts supply a tool for the later corank and fold arguments, without assuming their normal-form theorems here.

### Removing lower terms in a straightened characteristic direction

Principal-symbol transport does not remove a lower-order operator. Suppose the canonical change has already put the principal part into the form \(\xi_1 I_r\), where \(I_r\) is the identity on a finite-dimensional complex fiber. Write \(x=(t,z)\), with \(t=x_1\). The resulting operator is
\[
 P_0=D_t I_r+Q,\qquad D_t=-i\partial_t,\qquad Q\in\Psi^0_{1,0}.
 \tag{GT1}
\]
Its full left symbol \(q(t,z,\xi)\) is a smooth matrix symbol of order zero. No commutation, reality, diagonalizability or Hermitian assumption on \(q\) is made. Work on one fixed finite coordinate cylinder and a smaller closed angular cone in the punctured cotangent bundle. All estimates are uniform on compact base subsets and that angular cone. The initial slice \(t=0\) lies in the cylinder; translate the coordinate if needed.

**Theorem (all-order removal of lower terms).** On a smaller cylinder and cone there are properly supported elliptic \(A_2,B_2\in\Psi^0_{1,0}\) such that, microlocally there,
\[
 B_2A_2-I_r,\quad A_2B_2-I_r,\quad
 B_2P_0A_2-D_tI_r\quad\text{are smoothing}.
 \tag{GT2}
\]
This holds for ordinary symbols without a classical expansion. A scalar principal direction is essential to this statement about systems: a matrix-valued principal symbol with different eigenvalues has not been reduced to (GT1).

The exact finite-matrix existence, inverse and variation-of-constants proofs are retained in [Finite coordinate flows, Sections 17.2–17.3](../20261005-restored-phase-space/finite-coordinate-flows.md), equations NF6–NF11. The inverse solves a right-multiplication equation, and the factorially convergent integrals retain every matrix factor's order. The exact all-parameter inverse and derivative proofs are included there. K1 supplies support-preserving sums, O3 supplies ordinary composition with its full differentiated remainder, and K2–K3 supply the two-sided matrix parametrix. Here we retain the complete symbol bounds and conjugation calculation. Hörmander IV, Proposition 26.1.3, is the mathematical antecedent for the scalar construction.

**One fixed neighborhood.** Take a cylinder whose closure lies inside the coefficient domain, and a closed angular patch whose closure lies inside a larger available patch. Fixed spatial and angular cutoffs, together with a cutoff near zero frequency, extend the symbol smoothly to an ordinary order-zero symbol on a larger coordinate space, agreeing on the cylinder and cone to be used. The spatial cutoff may also be compact in \(t\). Its frequency cutoff is constant near infinity along the retained cone; its differentiated angular factors cost the required inverse frequency powers. Thus the extension has every ordinary symbol bound. Bounded frequencies cause only smoothing changes on localized base products.

Carry out the symbol construction on this fixed extension and then restrict to the retained cylinder and cone. Quantization with a kernel cutoff equal to one near the diagonal gives proper support. Different choices of extensions and such kernel cutoffs have the same microlocal germs on the retained interior patch. Indeed every finite composition coefficient is a local product of symbol derivatives, and the full remainder loses an arbitrary prescribed number of orders; separated spatial or angular cutoffs are smoothing there by integration by parts. No successive shrinking to an empty neighborhood is involved. We write \(q\#a\) for a full left composition representative; its smoothing ambiguity will not affect the construction.

**The leading matrix and every symbol derivative.** Let \(M\) solve
\[
 \partial_tM=-i qM,\qquad M(0,z,\xi)=I_r,
 \qquad H=M^{-1},\qquad \partial_tH=iHq.
 \tag{GT3}
\]
The ordered linear theorem gives these solutions on each finite interval, including negative \(t\), and gives both inverse products \(HM=MH=I_r\). If \(\|q\|\le C\) on an interval of length at most \(T\) from the initial slice, its ordered-series bound gives
\[
 \|M\|\le e^{CT},\qquad \|H\|\le e^{CT},\qquad
 \|Mv\|\ge e^{-CT}\|v\|.
 \tag{GT4}
\]
The uniform coefficient bound is available for all frequencies on the extended patch. Thus the matrix is uniformly invertible, rather than merely pointwise invertible.

We verify that \(M,H\) belong to \(S^0\). Write \(\theta=(z,\xi)\); for a multi-index \(\gamma\) in these variables, let \(w(\gamma)\) be its number of frequency derivatives. The smooth parameter theorem gives the actual derivatives of \(M\). Differentiating (GT3), for \(|\gamma|>0\), gives the ordered equation
\[
 \begin{split}
 \partial_t\partial_\theta^\gamma M
 &=-iq\,\partial_\theta^\gamma M+F_\gamma,\\
 F_\gamma&=-i\sum_{0<\nu\le\gamma}\binom\gamma\nu
       (\partial_\theta^\nu q)
       (\partial_\theta^{\gamma-\nu}M),\qquad
 \partial_\theta^\gamma M(0)=0.
 \end{split}
 \tag{GT5}
\]
Suppose the required bounds have been proved for every smaller derivative order. Each term of \(F_\gamma\) is bounded by
\(C_\gamma\langle\xi\rangle^{-w(\nu)-w(\gamma-\nu)}
=C_\gamma\langle\xi\rangle^{-w(\gamma)}\).
The constants are uniform on the fixed finite cylinder. Ordered variation of constants yields
\[
 \partial_\theta^\gamma M(t)
   =M(t)\int_0^tH(s)F_\gamma(s)\,ds,
 \qquad
 \|\partial_\theta^\gamma M\|
       \le C'_\gamma\langle\xi\rangle^{-w(\gamma)}.
 \tag{GT6}
\]
The integral is oriented when \(t<0\); its absolute estimate uses \(|t|\le T\). This proves induction starting from (GT4). Differentiating \(MH=I_r\) gives
\[
 \partial_\theta^\gamma H
 =-H\sum_{0<\nu\le\gamma}\binom\gamma\nu
       (\partial_\theta^\nu M)
       (\partial_\theta^{\gamma-\nu}H).
 \tag{GT7}
\]
The same induction proves all inverse bounds, with the order of the factors as displayed. Time derivatives and mixed time derivatives follow by differentiating the two equations in (GT3): their finite product sums have the same frequency weights, since a time derivative does not change symbol order. Consequently
\[
 \|\partial_t^l\partial_z^\beta\partial_\xi^\alpha M\|
 +\|\partial_t^l\partial_z^\beta\partial_\xi^\alpha H\|
 \le C_{l\beta\alpha}\langle\xi\rangle^{-|\alpha|}.
 \tag{GT8}
\]
This is the needed ordinary-symbol assertion. An unqualified statement that a pointwise matrix exponential is smooth would not prove it, and would in general give the wrong matrix solution.

The compact-time extension also permits the global symbol operations just specified. Outside its fixed time interval \(q=0\), so \(M\) is constant in time, with the parameter derivatives bounded by their endpoint values; (GT8) then holds on the extended coordinate space. A full left symbol of the product with the compact-base left factor \(Q\) is supported in that factor's output base support: its kernel vanishes for output points outside that compact set, and taking the input Fourier transform retains this property. The residuals below can consequently be represented with compact base support. Their time integrals are constant beyond that one compact time interval. This proves the same global uniform bounds for each correction and justifies applying the full ordinary symbol summation theorem before returning to the smaller patch.

**Correct the entire lower-order remainder.** The exact differential commutator in left quantization is
\[
 [D_tI_r,\operatorname{Op}(a)]=-i\operatorname{Op}(\partial_ta).
 \tag{GT9}
\]
A proper kernel cutoff adds only a smoothing term on the retained patch. Hence the full symbol of \(P_0\operatorname{Op}(a)-\operatorname{Op}(a)D_t\), modulo smoothing, is
\[
 \mathcal L(a)=-i\partial_ta+q\#a.
 \tag{GT10}
\]
Ordinary composition gives \(q\#a-qa\in S^{d-1}\) when \(a\in S^d\); the differentiated finite-seminorm remainder is part of this assertion. It also makes \(\mathcal L:S^d\to S^d\) continuous locally in every controlled seminorm. The cancellation of the two order-one differential terms is why this map preserves order.

Set \(a_0=M\). Equation (GT3) cancels \(-i\partial_ta_0+qa_0\), so
\(r_0=\mathcal L(a_0)\in S^{-1}\).
Suppose \(b_{j-1}=a_0+\cdots+a_{j-1}\) has been constructed, with
\(r_{j-1}=\mathcal L(b_{j-1})\in S^{-j}\), for \(j\ge1\). Use the full residual symbol, rather than only a homogeneous component, and put
\[
 a_j(t,z,\xi)=-iM(t,z,\xi)
       \int_0^t H(s,z,\xi)r_{j-1}(s,z,\xi)\,ds.
 \tag{GT11}
\]
Every differentiated integrand is a finite ordered product. The bounds for \(M,H\) and \(r_{j-1}\), followed by the finite interval bound, give
\(a_j\in S^{-j}\). Time derivatives follow either from (GT11) or from its differential equation. Direct differentiation, without commuting any factors, proves
\[
 -i\partial_ta_j+qa_j=-r_{j-1},\qquad a_j(0)=0,
 \qquad
 \mathcal L(b_{j-1}+a_j)=q\#a_j-qa_j\in S^{-j-1}.
 \tag{GT12}
\]
The negative sign and the outside factor \(-i\) in (GT11) are both forced by \(D_t=-i\partial_t\). This completes the induction at every order, with one fixed neighborhood and the same full lower-order symbol \(q\).

Apply support-preserving symbol summation to \(a_j\), \(j\ge1\), leaving \(a_0\) unchanged. It gives a symbol \(a\in S^0\) satisfying
\[
 a-a_0\in S^{-1},\qquad
 a-b_N\in S^{-N-1}\quad(N\ge0).
 \tag{GT13}
\]
For a concrete realization take \(a=a_0+\sum_{j\ge1}(1-\chi(\xi/R_j))a_j\), where the radii are chosen to bound the first \(j\) derivatives of the \(j\)-th summand in order \(-j+1\) by \(2^{-j}\). The fixed-base seminorms include all required time derivatives. Its finite low-frequency differences are smoothing; the remaining tails have each stated differentiated order. Continuity of \(\mathcal L\) at order \(-N-1\), together with (GT12), gives
\[
 \mathcal L(a)\in S^{-N-1}\quad\text{for every }N,
 \qquad P_0A_2-A_2D_tI_r\in\Psi^{-\infty},
 \quad A_2=\operatorname{Op}(a).
 \tag{GT14}
\]
The proper representative is understood microlocally on the smaller patch. This is an asymptotic construction in decreasing symbol orders; it does not assert convergence of an operator Neumann series.

Since \(a=M+S^{-1}\), (GT4) shows that \(a\) is uniformly invertible at sufficiently large frequencies on each retained compact base and angular set. For example \(\|H(a-M)\|<1/2\) there, and the finite-matrix inverse bound gives \(\|a^{-1}\|\le2\|H\|\). The exact matrix parametrix theorem provides a proper \(B_2\in\Psi^0\) with both inverse defects smoothing. Finally
\[
 B_2P_0A_2-D_tI_r
 =B_2(P_0A_2-A_2D_tI_r)+(B_2A_2-I_r)D_tI_r
 \in\Psi^{-\infty}.
 \tag{GT15}
\]
Smoothing operators remain smoothing after multiplication by a finite-order proper operator; this follows from the full composition estimates at arbitrarily negative orders. Equations (GT14)–(GT15) prove (GT2).

**Return to the canonical graph.** Let \(P\in\Psi^1(X)\) have homogeneous scalar principal symbol \(p\), or principal symbol \(pI_r\) in a local finite-rank frame. Suppose a homogeneous canonical transformation \(\kappa\) has already been constructed on the selected cone with \(p\circ\kappa=\xi_1\). Choose a local elliptic graph FIO \(A_1\) of any real order \(\mu\), with inverse \(B_1\) of order \(-\mu\), as in Section 6. The ordered Egorov theorem puts
\(B_1PA_1=D_tI_r+Q\) modulo a smoothing term on a smaller cone, for \(Q\in\Psi^0\). Its full order-zero term need not be scalar even when its principal direction is scalar.

Use the construction just proved and define
\[
 A=A_1A_2,\qquad B=B_2B_1.
 \tag{GT16}
\]
Proper composition gives the same canonical graphs and orders \(\mu,-\mu\), and the inverse defects are smoothing on the matched cones. Retaining the order of all operators gives
\[
 BPA-D_tI_r\text{ is smoothing},\qquad
 AD_tI_rB-P\text{ is smoothing}.
 \tag{GT17}
\]
For the second assertion multiply the first by \(A\) and \(B\): \((AB)P(AB)-AD_tI_rB\) is smoothing, and \(AB-I_r\) is smoothing. Cone cutoffs are chosen first so their separated pieces have no relevant graph wavefront; the proper smoothing-ideal argument of Section 6 applies to each discarded term. This proves the complete lower-term part of the canonical conjugation, rather than only its principal-symbol formula.

The homogeneous coordinate construction and the propagation theorem have their own hypotheses and proofs. Here the exact input is the already constructed \(\kappa\); no existence of such a change at a radial characteristic is asserted. Locally the result works for arbitrary finite lower-order matrix terms under a scalar principal direction. It does not supply a general system normal form with distinct characteristic roots, nor the entire principal-type existence and propagation theory.

## 8. A half-density change of variables is an exact model

Let \(f:X\to Y\) be a diffeomorphism of one-dimensional manifolds. In positive coordinate charts define
\[
(Au)(x)=|f'(x)|^{1/2}u(f(x)).
\tag{8.1}
\]
This is pullback of half densities. Its kernel is \(|f'(x)|^{1/2}\delta(y-f(x))\), with phase \(f(x)\eta-y\eta\) and amplitude \(|f'|^{1/2}\). Formula (2.4) makes its reduced symbol the unit, since \(|\phi_{x\eta}|=|f'|\). It is a proper order-zero FIO with graph
\[
\chi(y,\eta)=(f^{-1}(y),f'(f^{-1}(y))\eta).
\tag{8.2}
\]
Change of variables gives \(\|Au\|_2=\|u\|_2\), exactly, and its half-density inverse is its Hilbert adjoint.

Take \(X=\mathbb R\), \(Y=(0,\infty)\), and \(f(x)=e^x\). Then
\[
Au(x)=e^{x/2}u(e^x),\qquad
Bv(y)=y^{-1/2}v(\log y),\qquad BA=AB=I.
\tag{8.3}
\]
For \(P=D_x\), direct differentiation gives
\[
B D_x A=yD_y-\frac i2.
\tag{8.4}
\]
The transported principal symbol is \(y\eta\), in agreement with (7.2). Its left order-zero coefficient is \(-i/2\), and the subprincipal correction \((i/2)\partial_y\partial_\eta(y\eta)=i/2\) leaves zero subprincipal symbol. Thus this exact coordinate model also checks the half-density convention used in the transport lesson.

The Fourier-basis completeness, exact diagonal multiplier norm and circle pseudodifferential regularizer used in the next exercises are proved in companion G1–G2.

## 9. Exercises with complete solutions

**Exercise 9.1 (the graph volume; introductory).** On \(T^*\mathbb R^n\), compute the degree of \(|dx\,d\xi|^{1/2}\) under cotangent dilation. Explain why an order-\(m\) graph FIO has a reduced symbol of order \(m\), although its intrinsic symbol has order \(m+n/2\).

**Solution.** Dilation fixes \(dx\) and multiplies each frequency differential by \(t\). Thus the density scales by \(t^n\) and its square root by \(t^{n/2}\). The kernel ambient dimension is \(2n\), giving intrinsic order \(m+2n/4=m+n/2\). Dividing by the graph symplectic half volume subtracts \(n/2\), leaving \(m\). No amplitude-frequency count is substituted for this density calculation.

**Exercise 9.2 (a nonunit coordinate amplitude; intermediate).** For a linear diffeomorphism \(f(x)=Mx\) on \(\mathbb R^n\), write the normalized kernel of half-density pullback, its canonical graph and its reduced symbol. Compare with pullback acting on function coefficients without the half-density factor.

**Solution.** The half-density operator is \(Au(x)=|\det M|^{1/2}u(Mx)\), with kernel
\[
(2\pi)^{-n}\int e^{i(Mx-y)\cdot\eta}|\det M|^{1/2}\,d\eta.
\]
The graph is \((x,M^T\eta;y=Mx,\eta)\), and the mixed determinant has absolute value \(|\det M|\). Therefore (2.4) gives reduced symbol one. Its \(L^2\) norm is one by change of variables. Without the half-density factor the amplitude is one, the reduced symbol is \(|\det M|^{-1/2}\), and its \(L^2\) norm is that same constant. This is a local coefficient comparison; the intrinsic half-density pullback includes its Jacobian.

**Exercise 9.3 (unitary need not be compact; intermediate).** On the circle of length \(2\pi\), let \(T_a u(x)=u(x+a)\). Show that it is an order-zero graph FIO and a unitary \(L^2\) operator, but is not compact.

**Solution.** Its delta kernel has the translation graph and order zero, with unit reduced symbol. The circle is compact, so the kernel support is proper. Rotation preserves the density, hence \(T_a\) is unitary. On the orthonormal modes \(e_k=(2\pi)^{-1/2}e^{ikx}\), it acts by \(T_a e_k=e^{ika}e_k\). Images of distinct modes remain orthonormal and have distance \(\sqrt2\), so the image of the unit ball has no convergent subsequence containing these images. Its unit symbol does not satisfy the zero-limit compactness hypothesis.

**Exercise 9.4 (a compact regularized graph; intermediate).** On the same circle let \(R e_k=\langle k\rangle^{-1}e_k\), where \(\langle k\rangle=(1+k^2)^{1/2}\). Use the ordinary Fourier multiplier calculus to identify the order and symbol of \(T_aR\), and prove compactness directly.

**Solution.** The multiplier \(R\) is a proper ordinary PDO of order \(-1\), with leading symbol \(|\eta|^{-1}\) off zero. Composition with the translation graph leaves order \(-1\), with reduced symbol transported from that multiplier. In particular it lies in the declared order-zero class with a symbol tending to zero. Directly, truncate its Fourier action to \(|k|\leq N\). This is finite rank, and the norm of the omitted diagonal multiplier is
\[
\sup_{|k|>N}\langle k\rangle^{-1}=(1+(N+1)^2)^{-1/2}\longrightarrow0.
\]
Translation is unitary, so it preserves this error norm. The operator is a norm limit of finite-rank maps and is compact, independently confirming Theorem 4.2 in this model.

**Exercise 9.5 (local graph branches; advanced).** On the circle set \(A=I+T_\pi\). Describe its canonical relation, compute \(A^*A\), and explain why Theorem 3.1 still applies although this full product is not pseudodifferential.

**Solution.** Its relation is the disjoint union of the identity and the half-turn graph. Each is locally a canonical graph, and their kernel supports are disjoint base diagonals. Since \(T_\pi^*=T_\pi\) and \(T_\pi^2=I\),
\[
A^*A=(I+T_\pi)^2=2I+2T_\pi.
\]
The half-turn kernel is singular away from the ordinary diagonal, so this full product is not a PDO. The graph-continuity proof estimates the two graph pieces separately and sums the bounds. On Fourier modes, \(A e_k=(1+(-1)^k)e_k\), giving norm two. The zero action on odd modes is consistent with its two different graph pieces; it does not turn their full relation into the identity graph.

**Exercise 9.6 (exact Egorov and the density correction; advanced).** For (8.3), compute \(B D_x A\) directly, its principal and subprincipal symbols, and its formal symmetry on compact smooth half densities on \((0,\infty)\).

**Solution.** Differentiate \(e^{x/2}u(e^x)\): its \(D_x\) derivative is
\(-i e^{x/2}(u(e^x)/2+e^xu'(e^x))\). Multiplying by \(y^{-1/2}\) and substituting \(x=\log y\) gives \(yD_yu-iu/2\). The principal symbol is \(y\eta\), the left next coefficient is \(-i/2\), and the mixed derivative correction is \(+i/2\), so the subprincipal symbol is zero. Moreover
\(yD_y-i/2=\frac12(yD_y+D_yy)\). Integration by parts on compact supports shows that this expression is formally symmetric, as also follows from unitary conjugation of the formally symmetric \(D_x\).

**Exercise 9.7 (retain the noninverse coefficient; intermediate).** In the exact model replace \(B\) by \(2B\). For \(P=D_x\), give the symbol of \((2B)PA\). Explain which hypothesis would have been needed to omit the factor two.

**Solution.** Now \((2B)A=2I\), so \(c=2\). The principal symbol of \((2B)D_xA\) is \(2y\eta\); the full operator is \(2yD_y-i\). Formula (7.2) gives exactly \(c(p\circ\chi)=2y\eta\). To omit the coefficient in the principal-symbol formula, require \(c=\sigma_0(BA)=1\) in the region, equivalently \(BA-I\in\Psi^{-1}\) there. A microlocally smoothing error is sufficient for this normalization, but is stronger than necessary. Proper support and the inverse canonical relation alone do not impose that symbol identity.

**Exercise 9.8 (ordered matrix transport; advanced).** On two-component half densities on the circle, take \(A=S\), \(B=S^{-1}\), and \(P=\operatorname{diag}(1,2)D_x\), where
\[
S=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Compute \(BPA\) and its principal symbol. Explain why the scalar simplification (7.2) cannot be used for this matrix \(P\).

**Solution.** The graph is identity and the constant matrix commutes with \(D_x\), so the full operator is
\[
S^{-1}\operatorname{diag}(1,2)S D_x
=\begin{pmatrix}1&-1\\0&2\end{pmatrix}D_x.
\]
Its symbol is the displayed matrix times \(\eta\). Although \(BA=I\), conjugation by \(S\) changes the matrix principal symbol. The ordered product \(\beta p\alpha\) is therefore required. Scalar \(p\) commutes with the bundle maps, which is the step used in (7.2) and fails here.

**Exercise 9.9 (the gauge sign and finite-interval ellipticity; introductory).** On a finite real interval take \(P_0=D_t+c+i\gamma\), where \(c,\gamma\) are real constants. Find an exact multiplication gauge \(M(0)=1\), its inverse, and the conjugated operator. Determine whether the gauge is unitary.

**Solution.** Equation (GT3) is \(M'=(-ic+\gamma)M\), so
\[
 M(t)=e^{-ict+\gamma t},\qquad H(t)=e^{ict-\gamma t}.
\]
The product rule gives \(P_0(Mv)=(-iM'+(c+i\gamma)M)v+MD_tv=MD_tv\), hence \(HP_0M=D_t\). Both multipliers and their inverses are bounded with every derivative on the finite interval; their moduli are \(e^{\gamma t}\) and \(e^{-\gamma t}\). They are elliptic order-zero multipliers there. Multiplication by \(M\) preserves the local \(L^2\) norm exactly when \(\gamma=0\). Ellipticity on a finite interval does not imply unitarity or uniform bounds on the whole real time axis. Replacing \(-i\) by \(+i\) in the defining exponential would fail the displayed product-rule cancellation.

**Exercise 9.10 (two ordered matrix pulses; advanced).** Let
\[
 N_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 N_2=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
 q(t)=\rho_1(t)N_1+\rho_2(t)N_2.
\]
The real smooth pulses have compact disjoint supports in \(t>0\), the support of \(\rho_1\) precedes that of \(\rho_2\), and their integrals are \(\alpha,\beta\). Compute the final value of the normalized gauge, its inverse and the result of reversing the two pulses. Explain why this gives an exact operator example.

**Solution.** On the first support the equation is \(M'=-i\rho_1N_1M\), so \(M=\exp(-iN_1\int\rho_1)\). Between supports it is constant. On the second support the new evolution multiplies on the left. Since \(N_1^2=N_2^2=0\), after both pulses
\[
 \begin{split}
 M&=(I_2-i\beta N_2)(I_2-i\alpha N_1)
   =\begin{pmatrix}1&-i\alpha\\-i\beta&1-\alpha\beta\end{pmatrix},\\
 H&=(I_2+i\alpha N_1)(I_2+i\beta N_2)
   =\begin{pmatrix}1-\alpha\beta&i\alpha\\i\beta&1\end{pmatrix}.
 \end{split}
\]
Their products are both identity and \(\det M=1\), for arbitrary real \(\alpha,\beta\). Reversing the pulses gives
\[
 \widetilde M=(I_2-i\alpha N_1)(I_2-i\beta N_2)
   =\begin{pmatrix}1-\alpha\beta&-i\alpha\\-i\beta&1\end{pmatrix}.
\]
Thus \(M-\widetilde M=\alpha\beta\operatorname{diag}(1,-1)\); the same integrated matrix does not determine the evolution when \(\alpha\beta\ne0\). Equivalently \(N_2N_1\ne N_1N_2\), and their ordered quadratic terms differ. The symbol has no frequency dependence, so \(Q\) is multiplication by \(q(t)\) and \(q\#M=qM\) exactly. The product rule gives \(H(D_tI_2+q)M=D_tI_2\) without any lower-order correction. Smooth compact pulses keep all coefficient hypotheses; discontinuous jumps are unnecessary. This is a finite system with scalar principal part and arbitrary noncommuting lower terms, precisely within (GT1).

**Exercise 9.11 (why the leading ODE does not finish the symbolic proof; advanced).** In dimension \(n\ge2\), on a finite time cylinder, put
\[
 q(t,\xi)=t\chi(\xi),\qquad
 \chi(\xi)=\frac{\xi_1}{\langle\xi\rangle},\qquad
 M(t,\xi)=e^{-it^2\chi(\xi)/2}.
\]
Compute the first nonzero order of \(\mathcal L(M)\) in left quantization and a correcting symbol modulo order \(-2\). Show that the original residual is not generally of order \(-2\) on a cone where \(0<|\xi_1|/|\xi|<1\).

**Solution.** The pointwise differential equation cancels \(-i\partial_tM+qM\). Since the base dependence is only in \(t\), the ordinary composition expansion gives
\[
 \mathcal L(M)=(\partial_{\xi_1}q)D_tM+S^{-2}
      =-t^2\chi\,\partial_{\xi_1}\chi\,M+S^{-2}.
 \tag{GT18}
\]
All remainders here include every fixed base and frequency derivative uniformly on the finite cylinder. The derivative is
\(\partial_{\xi_1}\chi=(1+|\xi'|^2)\langle\xi\rangle^{-3}\).
For \(\xi=R\omega\), \(|\omega|=1\), with \(0<|\omega_1|<1\), fixed \(t\ne0\) and \(R\to\infty\), the product \(R\chi\partial_{\xi_1}\chi\) tends to \(\omega_1(1-\omega_1^2)\ne0\), and \(|M|=1\). The order \(-2\) error cannot cancel this nonzero order \(-1\) term. Thus the leading ODE alone has not produced a smoothing residual.

A first correction, modulo order \(-2\), is
\[
 a_1(t,\xi)=\frac{i t^3}{3}
                 \chi(\xi)\partial_{\xi_1}\chi(\xi)M(t,\xi).
 \tag{GT19}
\]
Indeed differentiate the displayed expression: the derivative of its \(t^3\) factor contributes \(t^2\chi\partial_{\xi_1}\chi M\) after multiplication by \(-i\), while its remaining differentiated term cancels \(qa_1\). Therefore
\((-i\partial_t+q)a_1=t^2\chi\partial_{\xi_1}\chi M\).
Because \(a_1\in S^{-1}\), the difference \(q\#a_1-qa_1\) is in \(S^{-2}\). Combining this with (GT18) proves \(\mathcal L(M+a_1)\in S^{-2}\). The full recursive integral (GT11), using the actual residual, supplies the correction at every subsequent order. A base cutoff equal to one on the cylinder embeds the local coefficient into the required symbol domain without changing these local principal residuals.

## References

- [Hörmander IV, §25.3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, reprint of the corrected second printing (1994), Theorem 25.3.1, Corollary 25.3.2, Proposition 25.3.3, Definition 25.3.4 and Theorem 25.3.5.

- [Hörmander IV, §26.1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, reprint of the corrected second printing (1994), Proposition 26.1.3. The scalar gauge and successive correction argument are the credited antecedents; the ordinary-symbol derivative bounds, ordered finite-matrix receiving calculation and worked exercises here are independently written.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Restoration and exact programme prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original text: public domain (CC0).*
