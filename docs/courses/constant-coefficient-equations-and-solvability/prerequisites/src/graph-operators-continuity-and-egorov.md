# Graph operators, continuity and Egorov

An FIO associated with a canonical graph moves one cotangent direction to one other direction. After dividing its symbol by the graph's symplectic half volume, an order-zero graph operator behaves on \(L^2\) like an order-zero pseudodifferential operator. The same graph calculus constructs inverses and transports pseudodifferential symbols by canonical changes of variables.

The local phase and symbol inputs are [Phase space and generating families](phase-space-and-generating-families.md), [Recognizing a Lagrangian distribution intrinsically](intrinsic-lagrangian-regularity.md), [Gaussian lines, densities and invariant symbols](gaussian-lines-and-invariant-symbols.md), and [Kernels, adjoints and clean composition](clean-composition-of-fourier-integral-operators.md). The coordinate second-jet construction is in [Hamilton fields and subprincipal transport](hamilton-fields-and-subprincipal-transport.md).

We import the finite-seminorm \(L^2\) estimates E23 and E28 from §6–7 of Symbols, operators and Sobolev scales. The quantitative PDO amplitude reduction G3–G4, proper pseudodifferential parametrices, real Sobolev mapping and elliptic tests come from §1, §6 and §11 of Detecting regularity without choosing coordinates. Their exact ordinary-symbol conventions agree with ours: \(D=-i\partial\), Fourier phase \(-y\cdot\eta\), and inverse Fourier factor \((2\pi)^{-n}\). We use those results rather than redoing their symbol calculus.

The authority is [Hörmander IV, §25.3], through Theorem 25.3.5. Symbols are ordinary \(S_{1,0}\) symbols. Every noncompact-manifold estimate is local over compact base sets. The canonical relations have the full punctured-cotangent closure and both nonzero covectors specified in the composition lesson. Later corank and fold estimates require additional geometry; their different losses are not consequences of the graph theorem alone.

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
so integration by parts replaces this term by \(D_{\eta_j}a_j\), of order \(m-1\). Derivatives of \(\phi_\eta\) cost one frequency order. Repeating and using the imported support-preserving asymptotic sum gives \(b(x,\eta)\in S^m\) with
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
The identity-relation kernel class is exactly the pseudodifferential class: choose the phase \((y-z)\cdot\eta\) and apply the local converse, followed by the imported amplitude reduction. The compactly localized smooth remainder stays smooth.

The exact AN-03 estimate now gives \(\|T^*T\|_{2\to2}\leq C\). For compact smooth \(u\),
\[
\|Tu\|_2^2=(T^*Tu,u)\leq C\|u\|_2^2.
\tag{3.3}
\]
The pairing identity follows on these smooth inputs from the kernel adjoint; its outputs are compact smooth by the nonzero-covector mapping theorem. Thus no bounded extension of \(T\) has been assumed in using (3.3). Density gives its unique bounded \(L^2\) extension.

The constants depend on finitely many amplitude seminorms. Indeed the composition construction is bilinear and has finite-seminorm estimates on fixed phase/support data. To recover the finitely many ordinary pseudodifferential symbol derivatives required by E23, perform its Fourier reduction to a finite order, and leave a sufficiently negative remainder. The finite coefficients and the absolutely integrable remainder use finitely many input derivatives. The latter remainder and the smooth kernel are controlled in the kernel norms used by the elementary integral estimate. This yields
\[
\|T\|_{2\to2}\leq C p_{0,L}(a)
\tag{3.4}
\]
for a finite \(L\) and the fixed working data. An infinite asymptotic-sum choice is unnecessary for this estimate.

**Assembly.** For fixed compact input and output base supports, the closed normalized kernel relation is compact and contains no covector on either axis. Cover it by finitely many small graph cones and use a smooth phase partition. Each piece has the bound just proved. The residual kernel is smooth on the compact base product and has a bounded integral-operator norm by Cauchy–Schwarz. Sum these finitely many bounds. They prove (3.1), including finite-rank bundle coefficients by the matrix version of the imported bound and equivalence of local Hermitian norms.

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
Then the phase difference is \((x-x')\cdot F\). The derivative \(F_\eta\) is invertible on the selected patch by (2.1), after shrinking it, so \(\zeta=F(x,x',\eta)\) is a homogeneous local frequency diffeomorphism. Changing variables turns (3.5) into an ordinary order-zero PDO amplitude with phase \((x-x')\cdot\zeta\). Its coefficient is
\[
b_R(x,\eta)b_R(x',\eta)^*|\det F_\eta|^{-1},
\tag{3.6}
\]
evaluated at the inverse frequency map. Homogeneity and the chain rule give order-zero bounds uniformly in \(R\). A base derivative of the inverse frequency costs one frequency power, canceled by the frequency derivative of its symbol factor. Derivatives of the cutoff obey the same bounds on its transition annulus.

The imported quantitative PDO amplitude reduction and E23 therefore bound \(\|T_RT_R^*\|\) by \(C p_{0,L}(b)^2\), for a finite \(L\) independent of \(R\). The Hilbert adjoint pairing gives \(\|T_R\|\leq C p_{0,L}(b)\). On Schwartz inputs the truncated integrals converge to (2.5), since the input Fourier transform decreases rapidly; their compact-output pointwise limit and the uniform bound give the same norm inequality for the limiting operator, followed by density. Thus
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

An \(L^2\) kernel is compact: approximate it in \(L^2\) by finite sums of product functions of the two variables. Their operators have finite rank, and Cauchy–Schwarz bounds the operator-norm difference by the kernel's \(L^2\) difference. Product simple functions are dense by the usual Lebesgue approximation on product charts. The same proof handles matrix components. Hence (4.3) is a norm limit of compact operators, and is compact. Smooth kernels localized to compact base products are compact by this same argument. Finitely many pieces prove the theorem. ∎

This proves the stated compactness directly from the graph estimates and the symbol limit. It makes no assertion about global compactness without the relevant support or geometry bounds.

## 5. Every real Sobolev order shifts by the operator order

**Theorem 5.1.** For \(A\in I^m\) with locally graph relation as above, and every real \(s\),
\[
A:H^s_{\mathrm{comp}}(Y)\longrightarrow H^{s-m}_{\mathrm{loc}}(X)
\tag{5.1}
\]
continuously, with the same half-density and finite-rank bundle coefficients.

**Proof.** Fix input and output compact localizations. Choose proper elliptic order reducers \(B_Y\in\Psi^s(Y)\), \(B_X\in\Psi^{s-m}(X)\), and a proper parametrix \(C_Y\in\Psi^{-s}(Y)\) of \(B_Y\). These are the imported real-order pseudodifferential constructions. Arrange an output localization of \(B_X\) to the larger compact set needed for the chosen output cutoff. The graph calculus gives
\[
B_XAC_Y\in I^0.
\]
On compact smooth inputs the exact identity is
\[
B_XA=(B_XAC_Y)B_Y+B_XA(I-C_YB_Y).
\tag{5.2}
\]
The first term maps \(H^s\) to \(L^2\): the imported mapping gives \(B_Y:H^s\to L^2\), with proper support keeping a common compact input set for the graph operator, and Theorem 3.1 treats the order-zero middle factor.

The second term has a smooth kernel on the localized base product. The proper smoothing error \(I-C_YB_Y\) has compact output support relevant to the input support. The FIO smooth-input theorem and its adjoint version show that composing such a smooth kernel with \(A\) is smooth; differentiating compact smooth test families proves every derivative. It therefore maps the fixed compact \(H^s\) input space to every local smooth and Sobolev space. Thus (5.2) bounds \(B_XAu\) in \(L^2\).

Use a proper local parametrix \(C_X\) of \(B_X\). On the smaller output set,
\[
Au=C_XB_XAu+R_XAu,
\]
where \(R_X\) is the localized smoothing error. The first term belongs to \(H^{s-m}\) by the imported PDO mapping. The second has a smooth localized kernel when composed with \(A\), by the same adjoint smooth-input argument. These bounds prove (5.1) for smooth inputs. Compact smooth approximation of an \(H^s\) distribution, in a common slightly larger compact support, gives the unique extension. Its distributional limit agrees with the original kernel action by the compact-distribution continuity of the mapping theorem. Local partitions prove the bundle and manifold assertions. ∎

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
with identity principal symbols. The exact AN-03 elliptic parametrix result supplies proper order-zero \(R_X,S_Y\) with \(P_XR_X-I\) and \(S_YP_Y-I\) smooth. Set
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
Both terms have smooth kernels: smooth proper kernels form a two-sided ideal with proper FIOs, by the proved smooth-input and adjoint mappings. Thus either representative is a two-sided inverse modulo smooth kernels. This uses the imported finite-order PDO parametrix construction; it does not assume convergence of a bounded-operator Neumann series.

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

## References

- [Hörmander IV, §25.3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, 1985, Theorem 25.3.1, Corollary 25.3.2, Proposition 25.3.3, Definition 25.3.4 and Theorem 25.3.5.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
