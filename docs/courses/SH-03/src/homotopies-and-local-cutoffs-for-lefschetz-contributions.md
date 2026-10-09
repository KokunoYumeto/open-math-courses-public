# Homotopies and local cutoffs for Lefschetz contributions

There are two ways to make a local fixed-point calculation manageable. A deformation transports its supported class through one compact region; a cutoff replaces its coefficient complex while preserving the map near the fixed point. In either case, the maps matter as much as the objects. We will keep the class on its support during the deformation, construct the two cutoff morphisms from their boundary adjunctions, and then compute their traces on intervals and a rectangle.

*Original lesson text and complete solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The [supported diagonal construction and germ theorem](lefschetz-traces-of-constructible-correspondences.md#pull-the-diagonal-identity-to-the-coincidence-set) define the local contribution; that lesson's [compact correspondence trace](lefschetz-traces-of-constructible-correspondences.md#the-compact-support-trace-square) identifies the global operator for the cutoff. Its evaluation order is fixed by [closed supports and evaluated proper transport](closed-supports-and-evaluated-proper-transport.md#the-evaluated-proper-hom-map-has-a-prescribed-tensor-order). We use [perfect tensor and internal Hom](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom), together with that proof's compact-cohomology calculation, to justify the finite trace.

For the parameter comparison, the needed inputs are the [proper-fibre restriction map](../../sheaf-proof-readings/src/SH02/open-prerequisite-proofs.md#proper-fibres-and-section-restriction) and [interval evaluation](../../sheaf-proof-readings/src/SH02/convex-acyclicity.md#sh02-ca-local-system--locally-constant-coefficients-and-evaluation), including interval endpoints. The [locally closed embedding formulas](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions) fix the distinction between extension by zero and locally closed supported Hom. Below we identify the actual supported pullbacks, the common parameter support and each boundary arrow before taking a trace.

## A family class has no parameter integration shift

Let \(k\) be a characteristic-zero field and \(F\in D^b_{\mathbb R\text{-c}}(k_X)\), with perfect stalks. The real analytic manifold \(X\) has the standing Hausdorff, countability and uniform finite dimension hypotheses. Write \(S=\operatorname{supp}(F)\), using closed support.

All morphisms below have degree zero in the derived category. Take \(I=[0,1]\), with its subspace topology, the projection \(p:X\times I\to X\), a continuous family \(f:X\times I\to X\), and a morphism

\[
 \phi:f^{-1}F\longrightarrow p^{-1}F.
 \qquad\text{(1)}
\]

For the analytic version, \(f\) is the restriction of an analytic map on \(X\times\mathbb R\). Define \(f_t(x)=f(x,t)\), \(\phi_t=i_t^{-1}\phi\), and

\[
 \widetilde Z=\{(x,t):x\in S,\ f(x,t)=x\},
 \qquad Q=p(\widetilde Z).
 \qquad\text{(2)}
\]

The diagonal is closed, and \(S\) is closed, so \(\widetilde Z\) is closed even for a merely continuous family. Assume it is compact. Then \(Q\) is compact and closed. Each slice support \(\widetilde Z_t=S\cap\{f_t=\mathrm{id}\}\) lies in this same \(Q\).

For a continuous slice, define \(C(\phi_t)\) by the ordinary diagonal pullback and evaluation in the proof below. For analytic slices this is exactly the self-map class of the preceding lesson. This definition needs constructible duality only for \(F\) on \(X\); it makes no constructibility assertion about a continuous inverse image.

**Theorem.** The image of \(C(\phi_t)\) in \(H_Q^0(X;\omega_X)\), and hence in \(H_c^0(X;\omega_X)\), is independent of \(t\).

**Proof.** Put \(K=F\boxtimes D_XF\), \(h=(f,p):X\times I\to X^2\), and \(W=h^{-1}\Delta_X\). The identity \(\mathrm{id}_F\), transported by the normalized exceptional diagonal comparison, gives \(e_\Delta(F)\in H^0_\Delta(X^2;K)\). Apply the ordinary unit \(K\to Rh_*h^{-1}K\) with its closed-support comparison to obtain a class in \(H_W^0(X\times I;h^{-1}K)\). This is the supported pullback of the preceding lesson: closed-diagonal base change and ordinary adjunction construct it for continuous \(h\) as well. Its coefficient map is
\[
 f^{-1}F\otimes p^{-1}D_XF
 \xrightarrow{\phi\otimes1}
 p^{-1}(F\otimes D_XF)
 \longrightarrow p^{-1}\omega_X.
 \qquad\text{(3)}
\]
Set \(T=f^{-1}S\cap p^{-1}S\), a closed subset of the parameter product. The coefficient \(h^{-1}K\) is zero off \(T\), since both \(F\) and its dual vanish off \(S\). Thus \(R\Gamma_T(h^{-1}K)\to h^{-1}K\) is an isomorphism. The composition law for closed support gives \(R\Gamma_W(h^{-1}K)\simeq R\Gamma_{W\cap T}(h^{-1}K)\). Here \(W\cap T=\widetilde Z\). Applying (3) with this support retained produces
\[
 c\in H_{\widetilde Z}^0(X\times I;p^{-1}\omega_X).
 \qquad\text{(4)}
\]
To restrict the class, use the ordinary supported inverse comparison for \(i_t:X\to X\times I\); it gives support \(i_t^{-1}\widetilde Z=\widetilde Z_t\) and coefficient \(i_t^{-1}p^{-1}\omega_X=\omega_X\). The identities \(hi_t=(f_t,\mathrm{id}_X)\) and \(i_t^{-1}\phi=\phi_t\) identify the resulting path with the definition of \(C(\phi_t)\). Ordinary units and the closed-support comparisons compose under inverse image; the tensor comparison and evaluation do too. Consequently this is equality of the supported classes, not only equality after integration.

This construction uses the duality and diagonal comparison of \(F\) on \(X\), not duality of \(f^{-1}F\) on the family. It therefore works for a continuous \(f\), without asserting constructibility of its whole pullback. If the family morphism also extends to an ambient open parameter interval in the analytic version, one may construct the class there and restrict to \(I\). There is no integration over time in (3); its target is \(p^{-1}\omega_X\), not the dualizing complex of the parameter product.

Enlarge the support in (4) to \(Q\times I\). For any bounded complex \(H\) on \(X\), ordinary interval descent and the closed support adjunction give
\[
 \begin{aligned}
 Rp_*p^{-1}H&\simeq H,\\
 Rp_*R\Gamma_{Q\times I}p^{-1}H
 &\simeq R\Gamma_Q(Rp_*p^{-1}H)
 \simeq R\Gamma_QH.
 \end{aligned}
 \qquad\text{(5)}
\]
Here are the maps and the reason they are invertible. The projection \(p\) is proper: the inverse image of a compact set is its product with compact \(I\). Proper-fibre restriction identifies the stalk of \(Rp_*p^{-1}H\) at \(x\) with \(R\Gamma(I;(H_x)_I)\). Under this identification the ordinary unit \(H\to Rp_*p^{-1}H\) is the constant-section map. The interval evaluation theorem makes this map an isomorphism: evaluation at any \(t\in I\), including an endpoint, is its inverse. For a bounded coefficient complex the same assertion follows through its finite truncation filtration. Thus the first arrow of (5) is the inverse of this particular unit.

For the support comparison, use \(R\Gamma_Q(-)=R\mathcal Hom(k_Q,-)\). Ordinary internal adjunction gives, for \(L=p^{-1}H\),

\[
R\mathcal Hom(k_Q,Rp_*L)
\simeq Rp_*R\mathcal Hom(p^{-1}k_Q,L)
=Rp_*R\Gamma_{Q\times I}L.
\]

The last equality uses the canonical inverse-image identification \(p^{-1}k_Q=k_{Q\times I}\) for the closed subset \(Q\). To check the first map, test on every open set against a complex \(B\): tensor–Hom adjunction, ordinary \((p^{-1},Rp_*)\) adjunction and the tensor comparison identify both sides with maps from \(p^{-1}(B\otimes k_Q)\) to \(L\). The resulting comparison commutes with the support-forgetting maps because both are induced by \(k_X\to k_Q\). Combining it with the actual unit proves the second line of (5). This argument concerns ordinary sections on a compact interval, with no exceptional parameter trace.

Under (5), the pullback
\[
 H_Q^0(X;\omega_X)
 \xrightarrow{\ p^*\ }
 H_{Q\times I}^0(X\times I;p^{-1}\omega_X)
 \qquad\text{(6)}
\]
is an isomorphism induced by the unit just checked, with support \(Q\). Let \(r_t\) be the supported slice restriction with support enlarged to \(Q\). Functoriality of supported inverse image and \(pi_t=\mathrm{id}_X\) give \(r_t p^*=\mathrm{id}\), by the ordinary unit–counit identity. Since \(p^*\) is invertible, every \(r_t\) is the same inverse. The support enlargement from \(\widetilde Z\) to \(Q\times I\) commutes with slice restriction, so \(r_t(c)\) is exactly the image of \(C(\phi_t)\) in \(H_Q^0(X;\omega_X)\). Those images are independent of \(t\). Compactness of \(Q\) then permits forgetting to compact support and applying \(R\Gamma_c(X;\omega_X)\to k\). The retained dualizing coefficient fixes this scalar without a choice of orientation or a parameter shift. \(\square\)

The assertion concerns the class after its support is enlarged to the single compact set \(Q\). It does not identify the varying groups \(H_{\widetilde Z_t}^0(X;\omega_X)\) by arbitrary choices.

**Linear-family consequence.** Let \(V\) be a finite-dimensional real vector space, \(F\) a bounded conic constructible complex with perfect stalks, \(u_t:V\to V\) a continuous linear family, and \(\phi:u^{-1}F\to p^{-1}F\) a given family morphism. If \(1\) is never an eigenvalue, then \(\ker(u_t-\mathrm{id})=\{0\}\) for every \(t\). On each compact parameter subinterval the supported fixed locus is a closed subset of \(\{0\}\times I\), hence compact. If zero is outside the closed support, all classes are zero. Otherwise enlarge every slice support to \(\{0\}\), and the theorem says their common point-supported class is constant. The normalization \(i_0^!\omega_V=k\) identifies its point trace with a scalar \(C_0(\phi_t)\). Any two parameters in a connected interval lie in one compact subinterval, so the scalar is constant on the whole interval. This uses the single family morphism; independent slice morphisms do not supply the class (4).

## Compact closure controls the boundary

A proper first map alone does not give a global compact-cohomology trace formula. Translation \(t\mapsto t+1\) on \(\mathbb R\), with constant coefficient, has no fixed point, while its compact cohomology is \(k[-1]\) with trace \(-1\). Properness of translation does not remove that contribution at infinity.

For a self-map and a coefficient morphism \(\psi:f^{-1}G\to G\), the ordinary global endomorphism meant below is the composite

\[
R\Gamma(X;G)\longrightarrow R\Gamma(X;f^{-1}G)
\xrightarrow{R\Gamma(\psi)}R\Gamma(X;G).
\]

The first arrow comes from the ordinary unit \(G\to Rf_*f^{-1}G\). It does not require \(f\) to be proper. The preceding correspondence trace theorem with second map identity gives this very composite: its supported lift followed by support forgetting is \(\psi\), and the identity map's exceptional counit is the identity.

For a relatively compact cutoff, use its compact **closed support** in the ambient manifold. The trace theorem then applies to that compact coefficient. To have only the original contribution at \(x\), we must require
\(Z\cap\overline V=\{x\}\).
Deleting a boundary point from \(V\) does not by itself remove it from the closed support of an extension. This closure in the hypothesis is essential.

## The ordinary cutoff has a closed entrance and an open exit

Return to an analytic \(f:X\to X\), a morphism \(\phi:f^{-1}F\to F\), and an isolated \(x\) of
\[
 Z=S\cap\{f=\mathrm{id}\}.
 \qquad\text{(7)}
\]
Let \(V\) be a locally closed subanalytic neighbourhood of \(x\). A neighbourhood contains an ambient open neighbourhood of \(x\). Put
\[
 A=f^{-1}V,\qquad W=A\cap V,
 \qquad H=i^{-1}F,\quad i:V\hookrightarrow X.
 \qquad\text{(8)}
\]
Suppose
\[
 W\text{ is open in }V
 \quad\text{and closed in }A.
 \qquad\text{(9)}
\]
For a locally closed set \(L\), write \(F_L=k_L\otimes F\), using extension by zero. The map is
\[
 \phi_V:f^{-1}F_V=(f^{-1}F)_A
 \xrightarrow{\phi_A}F_A
 \longrightarrow F_W
 \longrightarrow F_V.
 \qquad\text{(10)}
\]
The canonical isomorphism \(f^{-1}k_V=k_A\) follows by factoring a locally closed inclusion into an open and a closed inclusion: inverse image preserves the open zero extension and the closed extension, with identity on the surviving stalks. Tensoring gives the first identification in (10).

The two remaining arrows can be constructed before adding \(F\). Closed restriction for \(W\hookrightarrow A\) gives \(k_A\to k_W\), and the open-extension counit for \(W\hookrightarrow V\) gives \(k_W\to k_V\). Extend these relative maps to \(X\) through the locally closed factorizations and tensor with \(F\). This gives exactly the middle and last arrows of (10); their compatibility with \(\phi\) follows from tensor naturality. Thus both clauses of (9) are map-existence conditions. Neither an arbitrary restriction from an open set nor an arbitrary extension from a closed subset can replace them.

**Ordinary cutoff theorem.** The new map agrees with \(\phi\) near \(x\), so
\(C_x(\phi_V)=C_x(\phi)\).
If, in addition, \(V\) is relatively compact and \(Z\cap\overline V=\{x\}\), then
\[
 C_x(\phi)=\operatorname{str}R\Gamma(X;\phi_V).
 \qquad\text{(11)}
\]
The endomorphism on the right includes ordinary \(f\)-pullback.

**Proof.** Choose an ambient open \(O\) containing \(x\) and contained in \(V\). Since \(f(x)=x\), continuity gives an open \(N\) containing \(x\) with \(N\subset O\cap f^{-1}O\). Shrink it further so that \(Z\cap N=\{x\}\). On \(O\), the coefficient \(F_V\) is canonically \(F\); on \(N\), both sides of (10), and all its cutoff arrows, identify with those of \(\phi\). Equivalently, \((f,\mathrm{id})(N)\subset O\times O\), where the two diagonal identities and their evaluations coincide. Supported restriction, point-support excision and the normalized point trace therefore give the local equality. We do not need the stronger condition \(f(N)\subset N\), which need not hold at a repelling fixed point.

For the global trace put \(G=F_V\). Tensor closure makes \(G\) bounded constructible with perfect stalks, and

\[
 \operatorname{supp}G\subset S\cap\overline V.
 \qquad\text{(12)}
\]

The right side is compact. The common support
\(f^{-1}\operatorname{supp}G\cap\operatorname{supp}G\)
is therefore compact as a closed subset of \(\operatorname{supp}G\). Its coincidence support lies in
\(Z\cap\overline V=\{x\}\).
The compact-coefficient case of the correspondence trace theorem, with second map identity and coefficient \(G\), applies to this compact common support. Its global operator is the ordinary pullback followed by (10), as described above. Its sole supported contribution agrees with that of \(\phi\) by the germ comparison. This proves (11).

For computations, properness on the closed support also fixes the comparison of section complexes:

\[
R\Gamma(X;F_V)\simeq R\Gamma_c(X;F_V)
\simeq R\Gamma_c(V;i^{-1}F).
\]

The first arrow is the inverse of forgetting compact support on a compactly supported complex; the second is composition for the locally closed extension by zero. Both identify the actual induced map, whenever that map is further computed by restriction and extension. Perfect cutoff coefficients and compact constructible cohomology make this complex perfect. In particular, open \(V\) generally contributes compact cohomology on \(V\), not ordinary cohomology on \(V\). The trace is an element of \(k\), with the full coefficient endomorphism retained; it need not be an integer.

The deleted boundary stays in the possible closed support in (12); the closure hypothesis is the step that excludes other fixed-point contributions there. No compact-cohomology trace theorem for an arbitrary noncompact correspondence is needed. \(\square\)

## The supported cutoff reverses the two conditions

Instead suppose
\[
 W\text{ is closed in }V
 \quad\text{and open in }A.
 \qquad\text{(13)}
\]
Write \(R\Gamma_LF=Ri_{L*}i_L^!F\) for a locally closed support functor. Its natural inverse comparison and cutoff maps give
\[
 \begin{aligned}
 I_V(\phi):f^{-1}R\Gamma_VF
 &\longrightarrow R\Gamma_A(f^{-1}F)
 \xrightarrow{\phi}R\Gamma_AF\\
 &\longrightarrow R\Gamma_WF
 \longrightarrow R\Gamma_VF.
 \end{aligned}
 \qquad\text{(14)}
\]
The first arrow is a natural comparison, not an asserted isomorphism. Using \(R\Gamma_VF=R\mathcal Hom(k_V,F)\), pull back evaluation and curry the resulting map

\[
f^{-1}R\mathcal Hom(k_V,F)\otimes k_A
\simeq f^{-1}\bigl(R\mathcal Hom(k_V,F)\otimes k_V\bigr)
\longrightarrow f^{-1}F.
\]

This defines \(f^{-1}R\Gamma_VF\to R\mathcal Hom(k_A,f^{-1}F)\), the first arrow of (14), with its normalization. The next arrow is internal Hom applied covariantly to \(\phi\).

For the last two arrows, use the contravariant first input of internal Hom. Since \(W\) is open in \(A\), its open-extension counit gives \(k_W\to k_A\), hence \(R\Gamma_AF\to R\Gamma_WF\). Since \(W\) is closed in \(V\), closed restriction gives \(k_V\to k_W\), hence \(R\Gamma_WF\to R\Gamma_VF\). These are respectively open support restriction and closed support enlargement. This constructs every arrow and explains exactly why (13) reverses the boundary order in (9). The locally closed identity \(R\Gamma_LF=Ri_{L*}i_L^!F\) uses ordinary direct image; replacing it by extension by zero would change this construction.

**Supported cutoff theorem.** We have
\(C_x(I_V(\phi))=C_x(\phi)\).
For relatively compact \(V\) with \(Z\cap\overline V=\{x\}\),
\[
 C_x(\phi)=\operatorname{str}I_V(\phi)
 \quad\text{on }R\Gamma_V(X;F).
 \qquad\text{(15)}
\]

**Proof.** Use the same \(O\) and \(N\subset O\cap f^{-1}O\) as in the ordinary proof, with \(Z\cap N=\{x\}\). On \(O\), internal Hom from \(k_V\) identifies \(R\Gamma_VF\) with \(F\). On \(N\), the pulled-back evaluation used to define the first arrow of (14) is evaluation from the tensor unit, so its curry is the identity of \(f^{-1}F\). Both coefficient arrows \(k_W\to k_A\) and \(k_V\to k_W\) are identities there as well. Thus the entire morphism (14) identifies with \(\phi\) on \(N\), including its initial inverse comparison. The same supported diagonal restriction and point trace prove the germ equality.

Put \(G=R\Gamma_VF=R\mathcal Hom(k_V,F)\). Internal-Hom constructibility and perfection apply to the locally closed subanalytic cutoff. Its closed support satisfies
\[
 \operatorname{supp}G\subset S\cap\overline V.
 \qquad\text{(16)}
\]
Indeed it vanishes on every open set disjoint from \(S\) or from \(\overline V\). The right side is compact, so both its global complex \(R\Gamma(X;G)=R\Gamma_V(X;F)\) and its correspondence trace factor are perfect. As in the ordinary proof, its coincidence support is contained in \(Z\cap\overline V=\{x\}\).

Apply the compact-coefficient correspondence theorem to \(G\), \(f\), and the complete morphism (14). The operator on \(R\Gamma(X;G)=R\Gamma_V(X;F)\) first uses the ordinary unit for \(f\), then the evaluation-defined supported inverse comparison, \(\phi\), open support restriction, and closed support enlargement. This is the precise meaning of \(\operatorname{str}I_V(\phi)\) in (15); it is not a trace of a stalk map or of the coefficient arrow without its ordinary pullback. Compactness of the common support follows from compactness of \(\operatorname{supp}G\) and closedness of \(f^{-1}\operatorname{supp}G\), as before. The only possible fixed contribution is \(x\), and its germ is the original one. The theorem therefore gives (15). The ambient boundary in (16) is retained throughout and excluded from additional fixed contributions by the closure condition. \(\square\)

The complexes in (11) and (15) need not be isomorphic. The theorem compares their correctly induced traces with a local class under their respective boundary conditions.

## An interval endpoint distinguishes attraction from repulsion

Use the canonical coefficient map for an orientation-preserving analytic local diffeomorphism preserving a closed interval, and let \(x\) be a fixed endpoint with \(f'(x)\ne1\). Only its germ at that endpoint is used. Translate and, if necessary, reflect the inward coordinate so that \(x=0\), \(f(0)=0\), and the coefficient germ is \(k_{[0,\infty)}\). On a sufficiently small interval \(f'>0\); there the inverse image of this coefficient support is the same half-line germ, and the canonical coefficient morphism is the identity under that identification. Since \(f'(0)-1\ne0\), the function \(f(t)-t\) is strictly monotone on a smaller interval. Zero is its only zero there. Choose every cutoff below with closure inside this interval, so the fixed-locus isolation condition holds on the closure as well.

If \(0<f'(0)<1\), choose \(0<a<1\) and a neighborhood on which \(0<f'(t)\leq a\). The mean-value theorem and \(f(0)=0\) give \(|f(t)|\leq a|t|\). Hence for every sufficiently small \(\epsilon>0\),
\(f([-\epsilon,\epsilon])\subset(-\epsilon,\epsilon)\).
Take \(V=[-\epsilon,\epsilon]\). Then \(W=V\) is open in \(V\) and closed in \(f^{-1}V\), so the ordinary cutoff theorem applies. Its coefficient is \(k_{[0,\epsilon]}\), with global section complex \(k\) and identity action on the constant section. Hence
\[
 C_0(\phi)=1.
 \qquad\text{(17)}
\]

If \(f'(0)>1\), choose \(a>1\) and a neighborhood on which \(f'(t)\geq a\). Thus \(|f(t)|\geq a|t|\), with the same sign as \(t\). Take \(V=(-\epsilon,\epsilon)\) with closure in that neighborhood, and put \(A=f^{-1}V\). The local inverse branch has preimage \(W=A\cap V=(\alpha,\beta)\), where \(-\epsilon<\alpha<0<\beta<\epsilon\), \(f(\alpha)=-\epsilon\), and \(f(\beta)=\epsilon\). In particular \(W\) is open in \(V\). It is also closed in \(A\): its only boundary points \(\alpha,\beta\) are not in \(A\). Equivalently, the strict inequalities \(f(-\epsilon)<-\epsilon\) and \(f(\epsilon)>\epsilon\) give a collar of \(\partial V\) disjoint from \(A\). Remote components of \(A\) may exist, but they do not meet this local component or its closure inside \(A\). This proves exactly (9), without a global injectivity assumption.

The cutoff coefficient is \(k_{[0,\epsilon)}\). Its ambient ordinary cohomology equals its compact cohomology by its compact closed support. In the closed interval \([0,\epsilon]\), the open-complement localization triangle has middle complex \(k\) and endpoint complex \(k_\epsilon\); restriction is the identity. Its fibre, which is the compact cohomology of \([0,\epsilon)\), is therefore zero. Every endomorphism of that zero complex has trace zero. Thus
\[
 C_0(\phi)=0.
 \qquad\text{(18)}
\]

The same argument applies at the other endpoint after reflecting its inward coordinate. It proves the endpoint formula from the actual cutoff complexes. Shifts multiply the result by \((-1)^r\), and a rank-\(m\) identity coefficient multiplies it by \(m\).

## Exercises with complete solutions

### A contraction and an expansion use opposite cutoffs

*Difficulty: Intermediate.*

On \(\mathbb R\), take \(F=k_{\mathbb R}[r]\), \(f(t)=at\), \(a>0\), \(a\ne1\), and the canonical coefficient map. Verify a cutoff pattern and compute \(C_0(\phi)\) for \(a<1\) and \(a>1\).

**Solution.** For \(a<1\), take closed \(V=[-1,1]\). Its inverse image is \([-1/a,1/a]\), so \(W=V\) is open in \(V\) and closed in \(f^{-1}V\). Ordinary cutoff gives the closed-interval coefficient \(k_{[-1,1]}[r]\); its global section complex is \(k[r]\), and its induced constant-section action is one. The trace is \((-1)^r\).

For \(a>1\), take open \(V=(-1,1)\). Then \(W=f^{-1}V=(-1/a,1/a)\) is open in \(V\) and closed in \(f^{-1}V\). The cutoff's ambient section complex is its compact section complex \(k[r-1]\). The restriction \(f:W\to V\) is a positive homeomorphism and is proper as a map between those two open intervals, so its pullback preserves compact supports.

To compute the maps, place the open intervals inside a larger compact interval \(D\). For either interval \(J\), the localization triangle for \(k_J\to k_D\to k_{D\setminus J}\) computes its compact cohomology as the fibre of the diagonal \(k\to k\oplus k\). The two complementary components are ordered left, right; their quotient by the diagonal is the degree-one generator, represented by the difference of their values. For nested intervals, the open-extension map gives a map between these triangles: it is the identity on \(k\), and the restriction on the two complementary components is the identity on each ordered constant coefficient. It therefore induces identity on the quotient. Positive dilation likewise matches the two ordered components, so its compact pullback induces identity on this generator. The closed restriction in (10) is identity here because \(A=W\). The full return operator is consequently identity on \(k[r-1]\), giving \((-1)^{r-1}\). For \(r=0\), the local contributions are \(+1,-1\). This computes the ordinary pullback and cutoff maps in their actual compact degree, rather than substituting the stalk identity.

### A rectangular saddle has one compact orientation degree

*Difficulty: Advanced.*

Let \(f(x,y)=(2x,y/2)\), \(F=k_{\mathbb R^2}\), and \(V=(-1,1)\times[-1,1]\). Check (9), compute the cutoff trace, and identify its local contribution.

**Solution.** Here \(f^{-1}V=(-1/2,1/2)\times[-2,2]\), and
\(W=(-1/2,1/2)\times[-1,1]\).
It is open in \(V\): the first interval is open and the second is the whole relative closed factor. It is closed in \(f^{-1}V\): the first factor is the whole relative open factor and the second is closed.

Compact cohomology, with the factors kept in the order \(x,y\), is
\(R\Gamma_c((-1,1);k)\otimes R\Gamma([-1,1];k)=k[-1]\otimes k=k[-1]\).
The first factor is the quotient of the ordered two-component constants by the diagonal, as in Exercise 1; the second is the constant section of a closed interval.

The ordinary pullback is along the positive product homeomorphism \(f:A\to V\); it preserves these two generators. The closed entrance \(A\to W\) on coefficients restricts the closed \(y\)-interval from \([-2,2]\) to \([-1,1]\), sending its constant section to itself, and leaves the open \(x\)-factor unchanged. The open exit from \(W\) to \(V\) enlarges the open \(x\)-interval; its localization-triangle map is identity on the ordered quotient generator proved in Exercise 1, and it leaves the closed \(y\)-factor unchanged. The product section comparison is natural for all three maps, and no factors are exchanged. Thus the full operator is identity on \(k[-1]\) and its supertrace is \(-1\). The only fixed point in \(\overline V\) is \((0,0)\), so (11) gives \(C_{(0,0)}(\phi)=-1\). This verifies the mixed boundary conditions and their maps without replacing the rectangle by an open ball.

### The supported calculation keeps the orientation action

*Difficulty: Intermediate.*

For \(f(t)=2t\), \(F=k_{\mathbb R}\) and \(V=[-1,1]\), verify (13) and compute (15) from the localization triangle.

**Solution.** Now \(W=[-1/2,1/2]\), closed in \(V\) and open in \(A=W\). Localization for the complement of \(V\) gives the restriction map
\(k\to k\oplus k\), the diagonal, since the two exterior components are contractible. Its fibre has cohomology \(k\) in degree one, hence \(R\Gamma_V(\mathbb R;k)=k[-1]\).

The supported inverse comparison is compatible with the localization triangles for \(V\) and \(A=[-1/2,1/2]\): positive dilation sends each component of \(\mathbb R\setminus A\) to the corresponding component of \(\mathbb R\setminus V\). Pullback is the identity on the ambient constant section and on both ordered exterior constants. It therefore gives identity on the cokernel \((k\oplus k)/\operatorname{diag}k\). The open restriction in (14) is identity because \(W=A\). The final enlargement \(A\subset V\) is induced by restricting the exterior constants from \(\mathbb R\setminus A\) to \(\mathbb R\setminus V\), again identity on each component. Hence the full supported operator is identity on the degree-one class. Its trace is \(-1\), so \(C_0(\phi)=-1\). The ordinary cutoff with this same closed \(V\) is not supplied by (9): \(W\) is not open in \(V\). A numerical agreement found by ignoring that failed hypothesis would not define the required cutoff morphism.

### Complete the two-endpoint calculation

*Difficulty: Advanced.*

For \(f(t)=t+\frac1{10}t(1-t)e^{-t^2}\) and \(F=k_{[0,1]}[r]\), compute the two local contributions individually. Use the global calculation in the preceding lesson as a check.

**Solution.** The derivative at zero is \(11/10>1\), so zero is repelling in the inward coordinate. Formula (18) gives \(C_0=0\). At one, the derivative is \(1-\frac1{10e}\), lying strictly between zero and one. Reflection of the inward coordinate preserves that derivative, so (17) gives \(C_1=(-1)^r\).

Their sum is \((-1)^r\), equal to the global trace on the constant interval section \(k[r]\). Each endpoint stalk still has trace \((-1)^r\), and each endpoint point-support complex is still zero. Thus the discrepancy is now resolved locally: attraction contributes the constant section; repulsion uses the vanishing half-open cutoff complex.

### A fixed point escaping to infinity defeats compact family support

*Difficulty: Advanced.*

Take \(F=k_{\mathbb R}\), \(f(x,t)=(1+t)x-1\), \(0\le t\le1\), and the canonical family coefficient map. Find the fixed locus and its local traces. Explain precisely why the family theorem does not assert constancy.

**Solution.** At \(t=0\), \(f(x,0)=x-1\) has no fixed point. For \(t>0\), its unique fixed point is \(x=1/t\). Its derivative is \(1+t>1\). Translate that fixed point to zero and use the expansion calculation of Exercise 1: its local contribution is \(-1\).

The family fixed locus is \(\{(1/t,t):0<t\le1\}\), an unbounded closed subset of \(\mathbb R\times[0,1]\). It is not compact, and its projection cannot be placed in one compact \(Q\). The passage from (4) to a common compact support and its point trace therefore fails. The family coefficient morphism is valid; the lost hypothesis is compactness of the whole supported fixed locus, not continuity or existence of a map on each slice.

### Continuous linear deformations require a single family morphism

*Difficulty: Intermediate.*

Let \(F=k_{\{0\}}[r]\) on \(\mathbb R\), \(u_t(x)=(2+t)x\), \(-1/2\le t\le1/2\), and let the family coefficient map be multiplication by a scalar \(b\in k\). Compute all local contributions. Could one instead choose \(b_t\) independently on each slice?

**Solution.** Inverse image of the point coefficient under this family is the coefficient on \(\{0\}\times I\), equal to \(p^{-1}F\). Multiplication by the one scalar \(b\) is a sheaf morphism of that constant family. Every slice has compact common support \(\{0\}\), global coefficient \(k[r]\), and trace \((-1)^r b\). Its unique local contribution is that number.

The supported fixed locus is \(\{0\}\times I\); absence of eigenvalue one and the linear-family consequence give the same constant result. An arbitrary choice of slice scalars need not assemble to a sheaf morphism. For a constant coefficient along a connected interval, a morphism acts locally constantly and hence by one fixed scalar. Separate slice maps do not meet the hypothesis (1).

## References and further reading

Y. Matsui and K. Takeuchi, [*Microlocal study of Lefschetz fixed point formulas for higher-dimensional fixed point sets*](https://arxiv.org/abs/0812.4480v1), arXiv 0812.4480v1, 24 December 2008, §3, pp. 7–11, study deformation and localization of Kashiwara's local contributions near a smooth fixed component. Proposition 3.3 compares the contribution with its normal specialization when the supported fixed component is compact and the induced normal map has no eigenvalue \(1\). Theorem 3.4 gives a localization formula under the stronger exclusion of real normal eigenvalues in \([1,\infty)\). These results have additional smooth-component and spectral hypotheses.

The continuous-family theorem above instead transports an ordinary diagonal-pullback class in \(p^{-1}\omega_X\), with no integration over the parameter. The two cutoff theorems use the supported diagonal construction and compact correspondence trace in the preceding lesson. Their boundary arrows are fixed by closed restriction and open extension, or by the opposite arrows under internal Hom. The common compact support and the condition \(Z\cap\overline V=\{x\}\) are what make those local calculations into finite traces.
