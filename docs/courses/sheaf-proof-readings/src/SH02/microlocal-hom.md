# Local morphisms in cotangent directions

This lesson constructs microlocal Hom and its functorial and composition maps. The general fibre-product ordinary-Hom target is constructed in the [separate-transport supplement](microlocal-hom-product-comparison.md), with its prerequisites stated there; SH02-MH-HOM-PRODUCT-OPEN explains the limitation of direct exceptional restriction. The graph functorial squares use the exact trace and support identifications proved in SH02-MIC-TRACE-EXCHANGE and its [endpoint supplement](microlocal-endpoint-propagation.md). The zero-section recovery arrow is identified with the relative trace in SH02-MH-RECOVERY using the explicit codimension-parity normalization proved in SH02-MIC-ZERO. The [product-recovery supplement](microlocal-hom-product-recovery.md) proves compatibility of the actual MIC19 and MH30/MH31 maps with those selected recoveries. Each foundational dependency is used in its individually stated scope.

Original AI-authored programme expression is dedicated under CC0 1.0 Universal. The published mathematical sources compared with the arguments are identified at the end of this lesson; their human-authored expression retains its own terms. Proofs below are relative to the individually stated prerequisite contracts. A source citation does not prove an unresolved prerequisite or certify the whole course.

The construction in this lesson takes a morphism problem on a manifold and separates it by covector direction. It has two checks that guide the calculations: forgetting the direction must recover ordinary derived Hom, and composing directional morphisms must agree with composing ordinary morphisms. Neither check permits an arbitrary comparison morphism to be replaced by an isomorphism.

## SH02-MH-CONVENTIONS — Types, orientations, and dependencies

Let \(k\) be a commutative ring of finite global dimension. Manifolds are finite-dimensional real smooth manifolds, Hausdorff and countable at infinity; real analytic manifolds and maps may be used throughout. A closed submanifold means an embedded submanifold closed in the ambient manifold under discussion. All constructions are local in the ambient manifold, so a locally closed embedding is handled by restricting to an open neighborhood in which it is closed. In the sheaf-operation criteria, a smooth map means a submersion; all maps are otherwise merely smooth as maps of manifolds. Neither orientability nor compactness is assumed. The notation \(D^b(k_X)\) means bounded cohomology sheaves of \(k\)-modules; it does not mean constructible cohomology, finite rank, or perfect stalks.

Tensor products are derived unless an invertible orientation complex is one of the factors. We write \(D'_XA=R\mathcal Hom(A,k_X)\), \(D_XA=R\mathcal Hom(A,\omega_X)\), and

\[
\omega_X=\operatorname{or}_X[\dim X],\qquad
\omega_{Y/X}=\omega_Y\otimes f^{-1}\omega_X^{\otimes-1}.
\]

For a codimension \(c\) embedding \(i:M\hookrightarrow X\),
\[
\omega_{M/X}=\operatorname{or}_{M/X}[-c].
\]

Evaluation of an orientation line with its inverse is fixed before any permutation of factors. Permutations of shifted complexes use the Koszul symmetry: interchanging homogeneous factors of degrees \(r,s\) multiplies by \((-1)^{rs}\). In local coordinates, an ambient product is ordered in the displayed order of its factors. These choices make orientation cancellations reproducible.

The following are prerequisite contracts. Their proofs, coefficient ranges and exact remaining imports belong to the indicated course units; the table identifies the required content rather than assigning a publication or approval state.

| Contract | Required content | Provider and scope |
|---|---|---|
| SH02-OPS-SIX | Bounded six operations, proper base change, projection, internal Hom adjunction, smooth product base change, orientation traces and coherent units/counits | [Exceptional operations](exceptional-operations.md) and [Manifold duality](manifold-duality.md); used with their stated finite-dimensional hypotheses |
| SH02-CB-EXTERNAL-HOM, SH02-CB-BIDUALITY, SH02-CB-INTERNAL-HOM | External Hom exchange and Verdier biduality under the precise cohomological constructibility hypotheses | [Cohomological biduality](cohomological-biduality.md); constructibility is required exactly where invoked |
| SH02-GAM-KERNEL | \(\phi_\gamma^{-1}R\phi_{\gamma *}A\simeq Rq_{1*}(q_2^{-1}A)_{Z_\gamma}\), \(Z_\gamma=\{y-x\in\gamma\}\) | [Cone topology](cone-topology.md); the displayed cone-kernel identification is required |
| SH02-FF-LINEAR-KERNEL, SH02-FF-MATES, SH02-FF-BASE, SH02-FF-PRODUCT | The four bundle Fourier exchanges and external product, with orientations and coherent adjunction mates | [Fourier functoriality](fourier-functoriality.md); actual maps and orientation normalizations are required |
| SH02-SP-CONIC, SH02-SP-SECTIONS, SH02-SP-SUPPORTS, SH02-SP-ZERO | Bounded conic specialization, normal-cone neighborhood tests and both zero-section recoveries | [Specialization](specialization.md); section and support systems are used in their stated scope |
| SH02-SP-DIRECT, SH02-SP-PROPER, SH02-SP-INVERSE, SH02-SP-ADJUNCTION, SH02-SP-EXTERNAL, SH02-SP-TENSOR | Specialization comparisons with exact properness, smoothness, tensor and adjunction statements | [Specialization](specialization.md); each comparison retains its own isomorphism hypotheses |
| SH02-MIC-DIRECT, SH02-MIC-INVERSE, SH02-MIC-TRANSVERSE, SH02-MIC-ADJUNCTIONS, SH02-MIC-EXTERNAL | The microlocal comparison transformations used in the graph, product and composition arguments | [Microlocalization](microlocalization.md); the specified transformations and their relative proofs are required |
| SH02-MIC-TRACE-EXCHANGE | Identification of Fourier-transported vertical arrows in the direct and inverse functorial squares with the separately defined relative traces and forget-support maps | Proofs in SH02-MEP-SUPPORT, SH02-MEP-TRACE and SH02-MEP-MATE-UNTWIST, relative to the finite operation and specialization cut |

Comparison constructions are made on injective/flat replacements in the bounded-below derived category when necessary. All statements in this lesson have bounded input complexes. A boundedness assertion also depends on the finite-dimension contracts above; it is not inferred merely from the symbol \(R\mathcal Hom\). No result here asserts an unbounded extension.

## SH02-MH-ADJUNCTION — Specifying a canonical comparison

If \(L\dashv R\) has unit \(u:1\to RL\) and counit \(e:LR\to1\), the mates of \(v:LA\to B\) and \(w:A\to RB\) are
\[
A\xrightarrow u RLA\xrightarrow{Rv}RB,\qquad
LA\xrightarrow{Lw}LRB\xrightarrow e B.
\]
They are inverse assignments. Applying the first and then the second inserts \(L(u_A)\) followed, after naturality, by \(e_{LA}\); their composite is \(1_{LA}\). Applying them in the other order inserts \(u_{RB}\) followed by \(R(e_B)\); their composite is \(1_{RB}\). Naturality shows that taking mates respects a commuting square. Thus a comparison assembled from evaluation, base change, and units and counits is checked by moving the entire diagram across the adjunction; comparing only its objects is insufficient.

The standard map
\[
\vartheta_f:f^{-1}A\otimes\omega_{Y/X}\longrightarrow f^!A
\]
is adjoint to
\[
Rf_!(f^{-1}A\otimes\omega_{Y/X})
\simeq A\otimes Rf_!\omega_{Y/X}\longrightarrow A,
\]
where the last map is the relative trace. Thus its orientation factor has a fixed direction. It is an isomorphism for a smooth map; it is not declared an isomorphism for an arbitrary map.

## SH02-MH-GRAPH — Covector correspondences

For \(f:Y\to X\), put \(E_f=Y\times_XT^*X\). Write
\[
T^*Y\xleftarrow{\rho_f}E_f\xrightarrow{\varpi_f}T^*X,
\quad
\rho_f(y,\xi)=(y,df_y^*\xi),\quad
\varpi_f(y,\xi)=(f(y),\xi).
\]
The graph \(\Gamma_f\subset X\times Y\) has conormal
\[
T^*_{\Gamma_f}(X\times Y)
=\{(f(y),y;\xi,-df_y^*\xi)\}.
\]
Proof: \((\xi,\eta)\) vanishes on every tangent vector \((df_yv,v)\) precisely when \(\eta=-df_y^*\xi\). The identification with \(E_f\) remembers the first covector. The graph conormal has a negative second component, whereas \(\rho_f\) uses the positive transpose derivative.

There is an orientation cancellation
\[
\omega_{E_f/T^*Y}\otimes\omega_{E_f/T^*X}\simeq k_{E_f}.
\]
Indeed, with \(m=\dim Y,n=\dim X\), the dimensions of these three spaces are \(m+n,2m,2n\); the relative shifts are \(n-m,m-n\). A vector-bundle total space has orientation line equal to base orientation times fibre orientation. The relative orientation lines here are \(\operatorname{or}_X\otimes\operatorname{or}_Y^{-1}\) and its inverse, pulled to \(E_f\). Evaluation cancels both lines and shifts. This proof does not require \(f\) to be a submersion.

## SH02-MH-MICRO — From normal limits to conormal sheaves

For \(i:M\hookrightarrow X\), put \(N_MX=TX|_M/TM\) and let \(N_M^*X\) be its dual. Write \(\pi:N_M^*X\to M\), \(s:M\hookrightarrow N_M^*X\), and \(\dot\pi:N_M^*X\setminus M\to M\) for the projection, zero section, and punctured projection. Define
\[
\mu_MF=(\nu_MF)^\wedge.
\]
Here \(\nu_M\) is normal specialization and our Fourier–Sato convention is
\[
A^\wedge=Rp_{2!}(p_1^{-1}A)_{\{\langle v,\xi\rangle\leq0\}}.
\]
The subscript means tensor with the constant sheaf of the indicated locally closed subset, extended by zero; it is not local cohomology with support. For \(F\in D^b(k_X)\), \(\mu_MF\in D^b_{\mathbb R_{>0}}(k_{N_M^*X})\), by the finite-amplitude conicity theorem for specialization and the Fourier equivalence. This inference uses no constructibility assumption.

### SH02-MH-RECOVERY — Zero direction and punctured directions

Use the exact recoveries of [SH02-MIC-ZERO](microlocalization.md#SH02-MIC-ZERO). Thus ordinary recovery is the no-cut Fourier map followed by the specialization support counit. In codimension \(c\), compact recovery is \((-1)^c\) times the specified zero-cone FS14 map, followed by the inverse specialization restriction unit. There are natural identifications
\[
s^{-1}\mu_MF\simeq R\pi_*\mu_MF\simeq i^!F,
\qquad s^!\mu_MF\simeq R\pi_!\mu_MF\simeq i^{-1}F\otimes\omega_{M/X}.
\]
With these maps,
\[
i^{-1}F\otimes\omega_{M/X}\xrightarrow{\vartheta_i}i^!F
\longrightarrow R\dot\pi_*(\mu_MF|_{N_M^*X\setminus M})\xrightarrow{+1}
\]
is the distinguished recovery triangle. Here \(\vartheta_i\) is the relative trace with the input orientation on the right, including the tensor symmetry.

**Proof.** REC4 identifies the specialized inverse maps for \(i:(M,M)\to(X,M)\) with the inverses of the chosen specialization recoveries. REC5 proves that original R2 is the ordinary Fourier recovery inverse. REC8 proves that original R4 and the unmodified FS14 compact recovery differ by \((-1)^c\), with the full graded-line permutation displayed. After the displayed tensor symmetry, the selected compact recovery is the actual upper arrow in the specialized MEP14 square. REC18–REC19 identify the support-forgetting arrow with \(\vartheta_i\) under these particular recoveries. Applying ordinary pushforward to the zero-section localization triangle gives the displayed triangle, transporting its connecting arrow by the same first-term normalization. This is a proof relative to the exact operation, Fourier and specialization suppliers listed in SH02-MIC-ZERO; the suppliers and the separate graph-Hom recovery contracts remain independent proof obligations.

### SH02-MH-TESTS — Directional cohomology formulas

For a fibrewise convex open cone \(V\subset N_M^*X\), use the positive polar
\[
V^\circ=\{v:\langle v,\xi\rangle\geq0
\text{ for every }\xi\in V\text{ over its base point}\}.
\]
Let \(C_M(Z)\subset N_MX\) denote the normal cone. Then
\[
H^r(V;\mu_MF)\simeq\varinjlim_{U,Z}H^r_{Z\cap U}(U;F),
\]
where \(U\subset X\) is open, \(U\cap M=\pi(V)\), and \(Z\subset X\) is closed with \(C_M(Z)\subset V^\circ\), over the base under consideration. Transition maps use neighborhood restriction and enlargement of admissible support on a common refinement. For \(p\in N_M^*X\), \(x=\pi(p)\), this gives
\[
H^r(\mu_MF)_p\simeq\varinjlim_Z H^r(R\Gamma_ZF)_x,\qquad
C_M(Z)_x\subset\{v:\langle v,p\rangle>0\}\cup\{0\}.
\]

If \(Z\subset N_M^*X\) is a closed fibrewise convex proper cone containing the zero section, and \(Z^{\circ a}=-Z^\circ\), then
\[
H_Z^r(N_M^*X;\mu_MF\otimes\operatorname{or}_{M/X})
\simeq\varinjlim_U H^{r-c}(U;F),
\]
where \(U\subset X\) is open and
\[
C_M(X\setminus U)\cap\operatorname{Int}(Z^{\circ a})=\varnothing.
\]
Proper means that each fibre cone contains no line. These formulas hold for all integers \(r\). The orientation local system in the last formula is unshifted; the shift is already present in \(r-c\).

Proof conditional on the Fourier cone formulas and SH02-SP-SECTIONS/SH02-SP-SUPPORTS. The Fourier open-cone formula calculates sections of \((\nu_MF)^\wedge\) using local cohomology of \(\nu_MF\) with polar normal support. The specialization formula replaces this by neighborhoods in \(X\) with the displayed normal-cone condition. The iterated neighborhood/support systems admit common refinements, so their diagonal system is cofinal; filtered colimits of \(k\)-modules are exact and the substitution holds degree by degree. On shrinking \(V\) to \(p\), the polar condition becomes strict positivity for each nonzero normal vector: a compact set of unit directions with positive pairing remains positive on a neighborhood of \(p\), whereas nonnegative pairing against a whole covector neighborhood forces strict positivity on every nonzero vector. This proves the stalk condition. The supported Fourier formula involves the antipodal polar and the compactly supported cohomology of a \(c\)-dimensional fibre, namely its orientation line in degree \(c\); this gives the last shift and orientation. Substitution of the specialization neighborhood formula completes the deduction. The two cone-formula dependencies themselves are not replaced by this deduction.

## SH02-MH-HOM — The sheaf of directional morphisms

For \(f:Y\to X\), write \(p:X\times Y\to X\), \(q:X\times Y\to Y\). For bounded \(F,G\) on \(X,Y\), respectively, define on \(E_f\)
\[
\mathcal H_f^+(G,F)=\mu_{\Gamma_f}R\mathcal Hom(q^{-1}G,p^!F),
\qquad
\mathcal H_f^-(F,G)=a^{-1}\mu_{\Gamma_f}R\mathcal Hom(p^{-1}F,q^!G),
\]
where \(a(y,\xi)=(y,-\xi)\). For \(f=1_X\), write
\[
\mu hom(G,F)=\mu_{\Delta_X}R\mathcal Hom(q_2^{-1}G,q_1^!F).
\]
Factor exchange on \(X\times X\) induces \(a\) on the diagonal conormal. Thus \(\mathcal H^-_{1_X}(F,G)\simeq\mu hom(F,G)\). This does not assert a symmetry between \(F\) and \(G\).

### SH02-MH-BOUNDED — Finite amplitude without constructibility

For bounded inputs the two graph Hom objects, and hence ordinary microlocal Hom, belong to the bounded conic category:
\[
\mathcal H_f^+(G,F),\ \mathcal H_f^-(F,G)\in D^b_{\mathbb R_{>0}}(k_{E_f}),
\qquad
\mathsf M_X(A,B)\in D^b_{\mathbb R_{>0}}(k_{T^*X}).
\tag{MH0}
\]
Here \(\mathsf M_X(A,B)\) denotes \(\mu hom(A,B)\), a notation used below. This assertion has the precise amplitude dependency SH02-MD-BOUNDED-HOM in [Manifold duality](manifold-duality.md), followed by SH02-MIC-DEFINITION in [Microlocalization](microlocalization.md). Both dependencies must hold in the stated coefficient and boundedness ranges.

**Proof relative to those contracts.** Put \(n=\dim X\), \(m=\dim Y\), and \(g=\operatorname{gld}k\). Suppose \(F\in D^{[a,b]}\) and \(G\in D^{[c,d]}\). The smooth projection formula gives \(p^!F=p^{-1}F\otimes\omega_Y\), with bounds \([a-m,b-m]\). On the \((n+m)\)-manifold \(X\times Y\), SH02-MD-BOUNDED-HOM therefore puts
\[
R\mathcal Hom(q^{-1}G,p^!F)
\in D^{[a-m-d,\ b-m-c+3(n+m)+g+1]}.
\]
For the other kernel, \(q^!G=q^{-1}G\otimes\omega_X\), so the corresponding sufficient bounds are
\[
R\mathcal Hom(p^{-1}F,q^!G)
\in D^{[c-n-b,\ d-n-a+3(n+m)+g+1]}.
\]
These estimates are uniform and need not be optimal. Bounded normal specialization followed by the finite-rank Fourier transform sends each such kernel to a bounded conic complex; antipodal pullback is exact. This proves MH0. The argument uses arbitrary bounded sheaves, not finite-rank local systems, perfect stalks, or biduality. \(\square\)

### SH02-MH-HOM-RECOVERY — Ordinary and compact Hom

Let \(\pi_f:E_f\to Y\). With no constructibility assumptions,
\[
R\pi_{f*}\mathcal H_f^+(G,F)\simeq R\mathcal Hom(G,f^!F),\qquad
R\pi_{f*}\mathcal H_f^-(F,G)\simeq R\mathcal Hom(f^{-1}F,G).
\]
In particular \(R\pi_*\mu hom(G,F)\simeq R\mathcal Hom(G,F)\).

If \(G\) is cohomologically constructible,
\[
R\pi_{f!}\mathcal H_f^+(G,F)\simeq D'_YG\otimes f^{-1}F\otimes\omega_{Y/X}.
\]
If \(F\) is cohomologically constructible,
\[
R\pi_{f!}\mathcal H_f^-(F,G)\simeq f^{-1}D'_XF\otimes G.
\]
The two hypotheses are separate. “Cohomologically constructible” has the precise Verdier-duality meaning in the imported duality unit; it is not replaced by “locally constant.” For \(f=1_X\), the first compact formula is \(R\pi_!\mu hom(G,F)\simeq D'_XG\otimes F\).

Proof. Let \(e:Y\hookrightarrow X\times Y\) be the graph. Recovery for \(\mu_e\) gives \(R\pi_{f*}\mu_eK=e^!K\). Internal Hom adjunction yields
\[
e^!R\mathcal Hom(q^{-1}G,p^!F)
\simeq R\mathcal Hom(e^{-1}q^{-1}G,e^!p^!F)
\simeq R\mathcal Hom(G,f^!F),
\]
using \(qe=1_Y,pe=f\). The other kernel gives \(R\mathcal Hom(f^{-1}F,G)\). Antipodal pullback does not change either pushforward because \(\pi_fa=\pi_f\) and \(a\) is a proper isomorphism.

Compact recovery is \(e^{-1}K\otimes\omega_{Y/(X\times Y)}\). The external Hom exchange, under constructibility of \(G\), identifies the restriction of the first kernel with \(D'_YG\otimes f^{-1}F\otimes\omega_Y\). This is an external-product exchange before graph restriction; it does not assert \(R\mathcal Hom(G,A)=D'G\otimes A\) for arbitrary \(A\) on \(Y\). Since \(\omega_{Y/(X\times Y)}=f^{-1}\omega_X^{-1}\), the product gives \(\omega_{Y/X}\). For the second kernel, constructibility of \(F\) gives \(f^{-1}D'_XF\otimes G\otimes f^{-1}\omega_X\); its last factor cancels the graph relative orientation. This proves both formulas with their stated hypotheses.

### SH02-MH-SUBMANIFOLD — Recovering microlocalization from Hom

If \(i:M\hookrightarrow X\) is closed and \(j:N_M^*X\hookrightarrow T^*X\), then
\[
\mu hom(k_M,F)\simeq j_*\mu_MF.
\]
Proof. For \(b=1_X\times i:X\times M\hookrightarrow X\times X\), the first Hom input \(q_2^{-1}k_M\) is \(b_*k_{X\times M}\). Exceptional adjunction changes its Hom kernel to \(Rb_*b^!q_1^!F\). The inverse image of the diagonal is the graph of \(i\), and \(b\) is transverse to the diagonal because the first-coordinate tangent can vary arbitrarily. The microlocal direct-image comparison for this closed embedding is an isomorphism: it is proper and its normal map is a closed fibrewise injection. It identifies the kernel's diagonal microlocalization with graph microlocalization of \(p^!F\). The inverse-image comparison for \(p:X\times M\to X\) identifies this with \(j_*\mu_MF\). On conormals the embedding is \((x,\xi)\mapsto(x,x;\xi,-\xi)\), \(\xi|_{T_xM}=0\); the projection orientation and its inverse cancel. There is therefore no residual antipodal or codimension shift. The comparison isomorphisms used here are constructed below and depend on the stated specialization/Fourier contracts.

### SH02-MH-GAMMA-STALK — Local testing with a cone topology

Let \(X=V\) be a finite-dimensional real vector space. For a closed convex proper cone \(\gamma\subset V\), let \(\phi_\gamma:V\to V_\gamma\) map to the topology whose open sets are ordinary opens invariant under addition by \(\gamma\). Let \(G_U\) denote restriction to \(U\) followed by extension by zero. Then
\[
H^r(\mu hom(G,F))_{(x_0,\xi_0)}
\simeq\varinjlim_{U,\gamma}
H^rR\Gamma\bigl(U;
R\mathcal Hom(\phi_\gamma^{-1}R\phi_{\gamma *}G_U,F)\bigr),
\]
where \(U\) runs through neighborhoods of \(x_0\) and
\[
\gamma\subset\{v:\langle v,\xi_0\rangle<0\}\cup\{0\}.
\]
The zero cone is allowed; it is the only allowable cone when \(\xi_0=0\).

Proof. Use normal coordinate \(x-y\) for the diagonal and the first-covector identification. Directional supports are represented cofinally by \(Z_\gamma=\{(x,y):y-x\in\gamma\}\). Locally, intersect the normal cone with a unit sphere. Its compact set of directions lies in the strict positive half-space; a slightly larger closed convex cone still lies there. The normal-cone definition forces the support into that wedge after shrinking both neighborhoods: otherwise normalized offending secants would have a convergent subsequence giving a forbidden normal direction. Negating \(x-y\) explains the negative inequality for \(\gamma\). The stalk is consequently the colimit over \(U,W,\gamma\) of
\[
H^rR\Gamma_{Z_\gamma}(U\times W;
R\mathcal Hom(q_2^{-1}G,q_1^!F)).
\]
Moving support into the first Hom argument and applying \(Rq_{1!}\dashv q_1^!\) gives
\[
H^rR\Gamma\bigl(U;
R\mathcal Hom(Rq_{1!}(q_2^{-1}G_W)_{Z_\gamma},F)\bigr).
\]
Take relatively compact \(W\), a cofinal restriction. The closed support of the kernel is contained in \(V\times\overline W\), so the first projection is proper on it: over any compact subset of \(V\), the support is a closed subset of a compact product. Hence \(Rq_{1!}=Rq_{1*}\) on this kernel. SH02-GAM-KERNEL now identifies it with \(\phi_\gamma^{-1}R\phi_{\gamma *}G_W\). Finally \(U=W\) is cofinal among pairs of neighborhoods, by passing to their intersection. This gives the formula with \(G_U\). There is no assertion that shriek and ordinary pushforward coincide for unlocalized \(G\).

## SH02-MH-TWISTS — Twisting both arguments and changing an arrow

Write \(\mathsf M_X(A,B)=\mu hom(A,B)\). Let \(L\) be an invertible locally constant complex on \(X\), with \(L\), its tensor inverse, and the displayed twisted inputs in the bounded categories under consideration. There are natural identifications
\[
\mathsf M_X(A\otimes L,B\otimes L)\simeq\mathsf M_X(A,B),
\quad
\mathsf M_X(A,B\otimes L)\simeq\mathsf M_X(A,B)\otimes\pi^{-1}L.
\tag{MH1}
\]
**Proof.** Work on a neighborhood where \(L\) is constant with tensor-invertible value \(P\), and write \(P^\vee\) for its tensor inverse. Tensoring with \(P\) is an equivalence with inverse tensoring with \(P^\vee\). No freeness of a rank-one module, and no expression of \(P\) as a single shifted free module, is needed. Tensor–Hom adjunction and this equivalence give natural identifications
\[
R\mathcal Hom(C\otimes P,D\otimes P)\simeq R\mathcal Hom(C,D),
\qquad
R\mathcal Hom(C,D\otimes P)\simeq R\mathcal Hom(C,D)\otimes P.
\]
For example, apply \(\operatorname{Hom}(T,-)\) to the second formula: moving \(P^\vee\) onto \(T\), and then currying, identifies both sides with \(\operatorname{Hom}(T\otimes C,D\otimes P)\). This proves the actual natural comparison by Yoneda and preserves the ordered evaluation and Koszul symmetry.

The same invertibility proves that a coefficient pulled back from the base commutes with ordinary derived direct image. For \(j:U\to V\), move \(P^\vee\) across the \(j^{-1}\dashv Rj_*\) adjunction: both mapping sets for
\[
Rj_*(H\otimes j^{-1}P)\simeq Rj_*H\otimes P
\]
identify naturally with \(\operatorname{Hom}(j^{-1}(T\otimes P^\vee),H)\). Thus this projection comparison is an isomorphism without commuting arbitrary Hom with a colimit. Localization triangles give the corresponding support comparison. Proper direct image uses the already established shriek projection formula, with the same ordered tensor comparison.

Near the diagonal the two pullbacks of \(L\) have a canonical germ identification given by locally constant transport, agreeing with the identity on the diagonal. Apply the two Hom identifications to the diagonal kernel; the smooth exceptional projection retains the pulled-back coefficient by its projection-adjunction comparison. Specialization commutes with that local coefficient by inverse image and the ordinary direct-image comparison just proved. Fourier commutes with the resulting base coefficient by the shriek projection formula. These are precisely the maps in MH1. On overlaps all comparisons are defined by transport, adjunction and evaluation, so they glue. Their symmetry is the stipulated graded symmetry, including when different coefficient summands carry different shifts. All operations are used in the stated bounded ranges. $\square$

A morphism \(A\to A'\) acts contravariantly on the first argument of \(\mathsf M\), and a morphism \(B\to B'\) acts covariantly on its second argument. These two actions commute. Indeed the two composites become the same map of internal Hom kernels after tensoring with \(A\) and evaluating. The tensor–Hom adjunction is faithful on these mapping sets, and specialization and Fourier are functors. This proves the assertion without a constructibility assumption.

For later use set \(W=\pi_f^{-1}\omega_{Y/X}\) on \(E_f\). Relative orientations of the two covector arrows are
\[
\omega_{\varpi_f}=W,\qquad \omega_{\rho_f}=W^{-1}.
\tag{MH2}
\]
For the first equality, \(\varpi_f\) is the base change of \(f\) by the rank-\(\dim X\) cotangent bundle, so the fibre orientation factors cancel. For the second, the calculation in SH02-MH-GRAPH gives the inverse line and opposite shift. The trace comparisons therefore read
\[
\varpi_f^{-1}A\longrightarrow\varpi_f^!A\otimes W^{-1},
\qquad
\rho_f^{-1}B\longrightarrow\rho_f^!B\otimes W.
\tag{MH3}
\]
These are not declared invertible for arbitrary \(f\).

## SH02-MH-FOUR-SQUARES — How a graph Hom changes under a map

For \(F\in D^b(k_X)\), \(G\in D^b(k_Y)\), abbreviate \(P=\mathcal H_f^+(G,F)\) and \(Q=\mathcal H_f^-(F,G)\). There are the following four squares:
\[
\begin{array}{ccc}
R\rho_{f!}P&\longrightarrow&\mathsf M_Y(G,f^{-1}F\otimes\omega_f)\\
\downarrow&&\downarrow\\
R\rho_{f*}P&\longleftarrow&\mathsf M_Y(G,f^!F),
\end{array}
\tag{MH4}
\]
\[
\begin{array}{ccc}
R\rho_{f!}Q&\longrightarrow&\mathsf M_Y(f^!F,G\otimes\omega_f)\\
\downarrow&&\downarrow\\
R\rho_{f*}Q&\longleftarrow&\mathsf M_Y(f^{-1}F,G),
\end{array}
\tag{MH5}
\]
\[
\begin{array}{ccc}
R\varpi_{f!}P&\longrightarrow&\mathsf M_X(Rf_*G,F)\\
\downarrow&&\downarrow\\
R\varpi_{f*}P&\longleftarrow&\mathsf M_X(Rf_!G,F),
\end{array}
\tag{MH6}
\]
\[
\begin{array}{ccc}
R\varpi_{f!}Q&\longrightarrow&\mathsf M_X(F,Rf_!G)\\
\downarrow&&\downarrow\\
R\varpi_{f*}Q&\longleftarrow&\mathsf M_X(F,Rf_*G).
\end{array}
\tag{MH7}
\]
Here and below \(\omega_f=\omega_{Y/X}\). The left verticals forget proper support. The right vertical of MH4 is induced by \(\vartheta_f\). In MH5 it is induced contravariantly by
\(f^{-1}F\otimes\omega_f\to f^!F\), followed by simultaneous untwisting using MH1. In MH6 it is induced contravariantly by \(Rf_!G\to Rf_*G\); in MH7 that map acts covariantly.

All maps in MH4 and MH5 are isomorphisms if \(f\) is a submersion. All maps in MH6 and MH7 are isomorphisms if \(f\) is proper on the closed support of \(G\). These statements do not assume that the input complexes are constructible.

**Construction of all eight horizontal maps.** This construction also specifies exactly which comparison maps are meant. Put
\[
u:Y\times Y\to X\times Y,\quad u(y_1,y_2)=(f(y_1),y_2),
\qquad
v:X\times Y\to X\times X,\quad v(x,y)=(x,f(y)).
\]
Let \(K^+=R\mathcal Hom(q^{-1}G,p^!F)\) and \(K^-=R\mathcal Hom(p^{-1}F,q^!G)\) on \(X\times Y\). The maps \(u\) and \(v\) carry the relevant diagonal to the graph and the graph to the diagonal, respectively. The following table records a map or identification before microlocalization. In its third column, “direct” and “inverse” mean the actual transformations SH02-MIC-DIRECT and SH02-MIC-INVERSE, including their adjunction mates.

| Arrow | Map of ordinary kernels | Microlocal comparison used |
|---|---|---|
| MH4, upper | \(K^+\to Ru_*R\mathcal Hom(q_{Y,2}^{-1}G,q_{Y,1}^{!}f^{-1}F)\), from the unit on the second Hom argument | ordinary direct comparison, then its \(R\rho_!\dashv\rho^!\) mate |
| MH4, lower | \(u^!K^+\simeq R\mathcal Hom(q_{Y,2}^{-1}G,q_{Y,1}^{!}f^!F)\) | exceptional inverse comparison |
| MH5, upper | \(K^-\to Ru_*R\mathcal Hom(q_{Y,1}^{-1}f^!F,q_{Y,2}^{!}G)\), from the \(Ru_!u^!\to1\) counit in the first Hom argument | ordinary direct comparison and its mate, then antipodal pullback |
| MH5, lower | \(u^!K^-\simeq R\mathcal Hom(q_{Y,1}^{-1}f^{-1}F,q_{Y,2}^{!}G)\) | exceptional inverse comparison, then antipodal pullback |
| MH6, upper | \(K^+\to v^!R\mathcal Hom(q_{X,2}^{-1}Rf_*G,q_{X,1}^{!}F)\), using \(v^{-1}Rv_*q^{-1}G\to q^{-1}G\) contravariantly | exceptional inverse comparison and its \(R\varpi_!\dashv\varpi^!\) mate |
| MH6, lower | \(R\mathcal Hom(q_{X,2}^{-1}Rf_!G,q_{X,1}^{!}F)\simeq Rv_*K^+\) | ordinary direct comparison |
| MH7, upper | \(K^-\to v^!R\mathcal Hom(q_{X,1}^{-1}F,q_{X,2}^{!}Rf_!G)\), using \(q^!G\to v^!Rv_!q^!G\) | exceptional inverse comparison and its mate, then antipodal pullback |
| MH7, lower | \(R\mathcal Hom(q_{X,1}^{-1}F,q_{X,2}^{!}Rf_*G)\simeq Rv_*K^-\) | ordinary direct comparison, then antipodal pullback |

Here \(q_{X,i}\) and \(q_{Y,i}\) denote projections from \(X^2\) and \(Y^2\). We give the details that make the table legitimate. For MH4 upper, the unit \(p^!F\to Ru_*u^{-1}p^!F\), internal Hom adjunction, and smooth projection orientations identify the target kernel under \(Ru_*\) as the indicated one; the missing relative orientation is precisely \(\omega_f\) supplied by the microlocal direct comparison. For MH5 upper, smooth proper-support base change gives
\(Ru_!q_{Y,1}^{-1}f^!F\simeq p^{-1}Rf_!f^!F\to p^{-1}F\).
Move \(Ru_!\) through Hom by its exceptional adjunction, and use \(u^!q^!G=q_{Y,2}^!G\). The resulting arrow points out of \(K^-\) because its first argument is contravariant. Thus this route uses the exceptional counit, not an ordinary inverse-image unit.

For MH6 upper, \(Rv_*q^{-1}G\simeq q_{X,2}^{-1}Rf_*G\) follows from product base change for the smooth first-coordinate projection; this is the locally rectangular product calculation, not arbitrary nonproper base change. Also \(v^!q_{X,1}^!F=p^!F\). MH6 lower is the identity
\(R\mathcal Hom(Rv_!A,B)\simeq Rv_*R\mathcal Hom(A,v^!B)\), applied with \(A=q^{-1}G\), and proper-support base change. For MH7 upper, smooth projection orientation and proper-support base change identify \(Rv_!q^!G=q_{X,2}^!Rf_!G\). For MH7 lower, product base change with the same locally constant projection orientation identifies \(Rv_*q^!G=q_{X,2}^!Rf_*G\). The internal Hom adjunction then gives the stated identification. These are all identities on bounded complexes in the imported finite-dimensional six-operation range.

The graph map induced by \(u\) on its submanifolds is the identity of \(Y\). Its conormal correspondence therefore has \(\rho_f\) as its only nonidentity arrow. The graph map induced by \(v\) has \(\varpi_f\) as its only nonidentity arrow: \(v\) is transverse to \(\Delta_X\), since the first coordinate of \(X\times Y\) is free. Substituting these geometric facts in the microlocal comparisons gives exactly MH4–MH7. The relative factors from \(u\), the covector map, and the smooth product projections cancel by MH2. In MH5 both arguments are first written with the same factor \(\omega_f\), and MH1 removes it from the lower-right object. Antipodal pullback commutes with both covector maps and with all four operations because scalar minus one defines proper isomorphisms of the relevant bundles.

**Commutativity, with its exact dependency.** Before Fourier transformation the four diagrams are built from evaluation and the two adjunction pairs. Move a square to its kernel mapping space using the corresponding adjunction. For MH4 the two paths become the unit \(p^!F\to Ru_*u^{-1}p^!F\), followed by the trace map to \(Ru_*u^!p^!F\), followed by its counit. Naturality moves the trace through the unit, and the triangle identity removes the inserted unit–counit pair. For MH5 the same calculation starts with the exceptional counit on the first argument; applying the contravariant Hom functor reverses that arrow, and MH1 cancels the common orientation. For MH6 and MH7 the calculation instead uses the natural map \(Rv_!\to Rv_*\), in the first and second arguments respectively. Its naturality with evaluation makes the two paths agree. These are the mate identities proved in SH02-MIC-ADJUNCTIONS. Fourier transports these commuting kernel diagrams. SH02-MIC-TRACE-EXCHANGE identifies the displayed independent trace and forget-support verticals by MEP11 and MEP14. Apply these identities to the maps of pairs induced by the displayed maps \(u\) and \(v\), with the kernels in the table. MEP20 identifies the ordinary direct endpoint with its actual adjoint mate, including the orientation contraction used in taking the horizontal mates. The resulting squares are therefore compatible with those verticals, relative to the finite operation and specialization inputs stated in SH02-MEP-SCOPE.

**Isomorphism conditions.** If \(f\) is a submersion, \(u\) is a submersion and its map on diagonals is the identity. The inverse comparison is therefore invertible; \(\rho_f\) is a closed embedding, so its two direct images coincide. The trace for \(f\) is invertible, proving both assertions for MH4 and MH5. If \(f\) is proper on \(\operatorname{supp}G\), then \(v\) is proper on the closed supports of \(K^+\) and \(K^-\), both contained in \(X\times\operatorname{supp}G\). It is transverse to the diagonal and its inverse image is precisely the graph. The clean normal-cone properness criterion of SH02-MIC-DIRECT verifies the extra normal support condition; properness of the ambient support alone would not be a sufficient general argument. Hence the direct comparison is invertible. The support of \(P,Q\) projects into \(\operatorname{supp}G\), so \(\varpi_f\) is proper on those supports too. Finally \(Rf_!G\to Rf_*G\) is invertible. This proves the assertions for MH6 and MH7.

## SH02-MH-TRANSPORT — Removing the graph object

The four squares give the following maps entirely in terms of ordinary microlocal Hom:
\[
R\rho_{f!}\varpi_f^{-1}\mathsf M_X(Rf_!G,F)
\longrightarrow\mathsf M_Y(G,f^{-1}F\otimes\omega_f),
\tag{MH8}
\]
\[
R\rho_{f!}\varpi_f^{-1}\mathsf M_X(F,Rf_*G)
\longrightarrow\mathsf M_Y(f^!F,G\otimes\omega_f),
\tag{MH9}
\]
\[
R\varpi_{f!}\rho_f^{-1}\mathsf M_Y(G,f^!F)
\longrightarrow\mathsf M_X(Rf_*G,F),
\tag{MH10}
\]
\[
R\varpi_{f!}\rho_f^{-1}\mathsf M_Y(f^{-1}F,G)
\longrightarrow\mathsf M_X(F,Rf_!G).
\tag{MH11}
\]
For completeness, the mate before the final proper direct image in MH8 is the composite
\[
\varpi_f^{-1}\mathsf M_X(Rf_!G,F)
\longrightarrow\varpi_f^{-1}R\varpi_{f*}P
\xrightarrow{\varepsilon_{\varpi_f}}P
\longrightarrow\rho_f^!\mathsf M_Y(G,f^{-1}F\otimes\omega_f).
\]
The first map is MH6 lower and the last is the mate of MH4 upper. MH9 replaces \(P\) by \(Q\), MH6 by MH7, and MH4 by MH5. For MH10 begin with MH4 lower, apply \(\rho_f^{-1}\), then use the ordinary adjunction counit \(\rho_f^{-1}R\rho_{f*}P\to P\), followed by the mate of MH6 upper. MH11 uses MH5 and MH7 in the same specified positions. Applying the appropriate proper direct image and its exceptional counit gives the four displayed arrows. This specifies every unit and counit used.

If \(f\) is a submersion and proper on \(\operatorname{supp}G\), MH10 and MH11 are isomorphisms. Indeed \(\rho_f\) is a closed embedding, and for every complex \(A\) on \(E_f\) the counit \(\rho_f^{-1}R\rho_{f*}A\to A\) is invertible. This follows by restriction of extension from a closed subset, or stalkwise from the exact closed direct image. The horizontal comparisons used in the preceding constructions are invertible by the two parts of SH02-MH-FOUR-SQUARES. Their composite is consequently invertible. No analogous assertion for MH8 or MH9 follows merely from these two hypotheses.

## SH02-MH-PAIR-TRANSPORT — Moving both arguments at once

For \(A=\mathsf M_X(F_2,F_1)\) and \(B=\mathsf M_Y(G_2,G_1)\), there are squares
\[
\begin{array}{ccc}
R\rho_{f!}\varpi_f^{-1}A&\longrightarrow&
\mathsf M_Y(f^!F_2,f^{-1}F_1\otimes\omega_f)\\
\downarrow&&\downarrow\\
R\rho_{f*}(\varpi_f^!A\otimes W^{-1})&\longleftarrow&
\mathsf M_Y(f^{-1}F_2\otimes\omega_f,f^!F_1),
\end{array}
\tag{MH12}
\]
\[
\begin{array}{ccc}
R\varpi_{f!}\rho_f^{-1}B&\longrightarrow&
\mathsf M_X(Rf_*G_2,Rf_!G_1)\\
\downarrow&&\downarrow\\
R\varpi_{f*}(\rho_f^!B\otimes W)&\longleftarrow&
\mathsf M_X(Rf_!G_2,Rf_*G_1).
\end{array}
\tag{MH13}
\]
The left verticals are MH3 followed by forgetting proper support. To specify the right vertical of MH12, both routes through the following intermediate objects agree:
\[
\begin{array}{ccccc}
&&\mathsf M_Y(f^!F_2,f^!F_1)&&\\
&\nearrow&&\searrow&\\
\mathsf M_Y(f^!F_2,f^{-1}F_1\otimes\omega_f)
&&&&\mathsf M_Y(f^{-1}F_2\otimes\omega_f,f^!F_1)\\
&\searrow&&\nearrow&\\
&&\mathsf M_Y(f^{-1}F_2,f^{-1}F_1).&&
\end{array}
\tag{MH14}
\]
Every arrow is induced by \(\vartheta_f\) in one argument, and the bottom route also uses MH1. Equality of the routes follows from commuting precomposition and postcomposition. In MH13 the analogous two intermediate objects are \(\mathsf M_X(Rf_!G_2,Rf_!G_1)\) and \(\mathsf M_X(Rf_*G_2,Rf_*G_1)\). The natural map \(Rf_!\to Rf_*\) supplies both routes, which again commute.

**Proof of construction.** Retain the maps \(u,v\) from the preceding section. The inverse comparison for the transverse map \(v\) and the module action of internal Hom on exceptional inverse image give
\[
\varpi_f^{-1}A\longrightarrow\mathcal H_f^+(f^!F_2,F_1).
\tag{MH15}
\]
More explicitly, apply \(\mu_{\Gamma_f}\) to
\[
v^{-1}R\mathcal Hom(q_{X,2}^{-1}F_2,q_{X,1}^!F_1)
\longrightarrow
R\mathcal Hom(v^!q_{X,2}^{-1}F_2,v^!q_{X,1}^!F_1).
\]
The arrow is adjoint to the action
\(v^{-1}R\mathcal Hom(C,D)\otimes v^!C\to v^!D\): first use the module map into \(v^!(R\mathcal Hom(C,D)\otimes C)\), then apply \(v^!\) to evaluation. Smooth product base change identifies the two exceptional inputs with \(q^{-1}f^!F_2\) and \(p^!F_1\). Thus its target is exactly the graph object in MH15.

The exceptional inverse comparison gives a second map
\[
\mathcal H_f^+(f^{-1}F_2\otimes\omega_f,F_1)
\longrightarrow\varpi_f^!A\otimes W^{-1}.
\tag{MH16}
\]
Indeed \(v^!R\mathcal Hom(C,D)=R\mathcal Hom(v^{-1}C,v^!D)\); tensoring its microlocalization by \(W^{-1}\) moves that inverse line into the first Hom input. The comparison for \(v\), whose map on normal fibres is an isomorphism, has precisely the target in MH16. The square formed by MH15, MH16 and the two trace comparisons is the inverse square SH02-MIC-INVERSE followed by the action just described. Apply \(R\rho_{f!}\) to MH15 and MH4 upper; apply \(R\rho_{f*}\) to MH16 and MH4 lower. Pasting these two squares gives MH12, with the right route MH14. Naturality of evaluation proves compatibility of the paste with both argument changes. The trace verticals are the specified maps by SH02-MIC-TRACE-EXCHANGE: MEP14 identifies the inverse square for \(v\), while MEP11 and MEP20 retain the direct comparison and its actual ordinary mate in the graph square being pasted.

For the direct counterpart start from \(B\) in its antipodal kernel presentation. The direct comparison for \(u\) supplies
\[
\rho_f^{-1}B\longrightarrow
\mu_{\Gamma_f}(Ru_!R\mathcal Hom(q_{Y,1}^{-1}G_2,q_{Y,2}^!G_1))^a
\longrightarrow\mathcal H_f^-(Rf_*G_2,G_1).
\tag{MH17}
\]
The second arrow is adjoint to the following evaluation. Pull \(p^{-1}Rf_*G_2\) back by \(u\), apply the ordinary counit to obtain \(q_{Y,1}^{-1}G_2\), evaluate against the displayed Hom, then apply \(Ru_!\) and the exceptional counit for \(u\). The projection formula moves the pulled-back first input across \(Ru_!\). This determines the arrow and explains the ordinary direct image on \(G_2\).

Internal exceptional adjunction also identifies the kernel of \(\mathcal H_f^-(Rf_!G_2,G_1)\) with \(Ru_*R\mathcal Hom(q_{Y,1}^{-1}G_2,q_{Y,2}^!G_1)\). Hence the ordinary direct comparison gives
\[
\mathcal H_f^-(Rf_!G_2,G_1)\longrightarrow\rho_f^!B\otimes W.
\tag{MH18}
\]
Apply \(R\varpi_{f!}\) to MH17 and MH7 upper, and \(R\varpi_{f*}\) to MH18 and MH7 lower. The direct comparison square, its mate identity, and naturality of the evaluated \(Rf_!\to Rf_*\) map give MH13. No properness has been imposed to construct any of these maps.

If \(f\) is a submersion, all arrows in MH12 are isomorphisms. The smooth local product calculation identifies
\[
\mathcal H_f^+(f^!F_2,F_1)\otimes W\simeq\varpi_f^!A.
\]
To check it, use \(f^!F_2=f^{-1}F_2\otimes\omega_f\), move the factor through Hom, and use the smooth inverse comparison for \(v\); both its ambient map and its map of submanifolds are submersions. MH4 is then invertible, and \(\rho_f\) is a closed embedding. Together with the invertible smooth trace this proves the assertion.

If \(f\) is a closed embedding, all arrows in MH13 are isomorphisms. Proper direct image equals ordinary direct image. In graph coordinates, internal Hom adjunction and exact extension from a closed subset identify
\[
\mathcal H_f^+(G_2,Rf_!G_1)\simeq\rho_f^{-1}B.
\]
This is the proper microlocal direct comparison for \(u\); the normal derivative is a closed embedding and the graph support satisfies the normal properness criterion. Applying MH6, which is invertible for a proper support, proves the upper identification in MH13. The lower one follows by the same direct comparison and MH2. Equivalently, its two trace and proper-support verticals are invertible on these objects. This argument uses the closed embedding condition; a general proper map is not asserted to make MH13 invertible.

Two consequences used below are the maps
\[
R\rho_{f!}\varpi_f^{-1}\mathsf M_X(A_2,A_1)
\longrightarrow\mathsf M_Y(f^{-1}A_2,f^{-1}A_1),
\tag{MH19}
\]
\[
R\rho_{f!}\varpi_f^{-1}\mathsf M_X(A_2,A_1)
\longrightarrow\mathsf M_Y(f^!A_2,f^!A_1),
\tag{MH20}
\]
obtained from MH12 upper followed by the lower and upper routes of MH14. Similarly MH13 upper followed by either direct-image argument change gives maps to \(\mathsf M_X(Rf_!B_2,Rf_!B_1)\) and to \(\mathsf M_X(Rf_*B_2,Rf_*B_1)\). The exceptional image map with both arguments \(Rf_!\) is particularly useful for kernel composition.

## SH02-MH-PRODUCT — Independent directional morphisms

First take two unrelated manifolds \(X,Y\). There is a natural morphism
\[
\mathsf M_X(F_2,F_1)\boxtimes^L\mathsf M_Y(G_2,G_1)
\longrightarrow
\mathsf M_{X\times Y}(F_2\boxtimes^LG_2,F_1\boxtimes^LG_1).
\tag{MH21}
\]
Let \(r_i\) be projections from \((X\times Y)^2\), and reorder this space as \(X^2\times Y^2\). The product of diagonals becomes \(\Delta_{X\times Y}\). Apply SH02-MIC-EXTERNAL to the two Hom kernels. The resulting kernel has a map to
\[
R\mathcal Hom(r_2^{-1}(F_2\boxtimes^LG_2),r_1^!(F_1\boxtimes^LG_1)).
\]
To construct that map, tensor the two evaluation maps, apply the Koszul permutation that groups their two first arguments, and use the orientation isomorphism for the two smooth first projections. Tensor–Hom adjunction gives the map uniquely. Applying diagonal microlocalization gives MH21. This proof uses a tensor–Hom comparison, not an assertion that it is an isomorphism for arbitrary inputs.

Now let \(X\to S\) and \(Y\to S\) be maps of manifolds, and assume their fibre product \(Z=X\times_SY\) is an embedded submanifold of \(X\times Y\). Put \(j:Z\hookrightarrow X\times Y\), and let \(q_X,q_Y\) be its two projections. The conormal correspondence of \(j\) is
\[
T^*Z\xleftarrow{\rho_j}C\xrightarrow{\varpi_j}T^*X\times T^*Y,
\quad C=Z\times_{X\times Y}(T^*X\times T^*Y).
\]
For sheaves on the two cotangent bundles, \(A\boxtimes_S^LB\) means their ordinary inverse images to \(C=T^*X\times_ST^*Y\), tensored there. Then
\[
\begin{aligned}
&R\rho_{j!}\bigl(\mathsf M_X(F_2,F_1)\boxtimes_S^L\mathsf M_Y(G_2,G_1)\bigr)\\
&\quad\longrightarrow
\mathsf M_Z(F_2\boxtimes_S^LG_2,F_1\boxtimes_S^LG_1),
\end{aligned}
\tag{MH22}
\]
where \(F\boxtimes_S^LG=q_X^{-1}F\otimes^Lq_Y^{-1}G\). Pull MH21 back by \(\varpi_j\), apply \(R\rho_{j!}\), and use MH19 for \(j\). Ordinary inverse image preserves derived tensor, giving exactly the target in MH22. No transversality of \(X\to S\) and \(Y\to S\), and no submersion condition on either projection, is used.

The matching covector equation is transparent: \(\rho_j\) sends the pair \((\xi,\eta)\) over \((x,y)\in Z\) to its restriction to \(T_{(x,y)}Z\). Thus addition of covectors in an internal tensor product is a special case of restriction from an external tensor product.

## SH02-MH-HOM-PRODUCT — Reversing one directional arrow

There is also, on an ordinary product, a natural map
\[
\begin{aligned}
&\mathsf M_X(F_2,F_1)^a\boxtimes^L\mathsf M_Y(G_2,G_1)\\
&\quad\longrightarrow
\mathsf M_{X\times Y}\bigl(
R\mathcal Hom(q_X^{-1}F_1,q_Y^{-1}G_2),
R\mathcal Hom(q_X^{-1}F_2,q_Y^{-1}G_1)\bigr).
\end{aligned}
\tag{MH23}
\]
Here \(a\) reverses only the covector on \(X\). We prove the morphism at the kernel level. On \((X\times Y)^2\), let subscripts \(s,t\) designate the second (source) and first (target) copy. After exchanging the two \(X\)-factors, the first microlocal Hom kernel represents a morphism \(F_{2,t}\to F_{1,s}\); the \(Y\)-kernel represents a morphism \(G_{2,s}\to G_{1,t}\). The ordinary closed-monoidal composition map is
\[
\begin{aligned}
&R\mathcal Hom(F_{2,t},F_{1,s})\otimes
R\mathcal Hom(G_{2,s},G_{1,t})\\
&\quad\longrightarrow
R\mathcal Hom\bigl(
R\mathcal Hom(F_{1,s},G_{2,s}),
R\mathcal Hom(F_{2,t},G_{1,t})\bigr).
\end{aligned}
\tag{MH24}
\]
It sends a pair of arrows to precomposition followed by postcomposition. Formally, tensor its proposed source with \(R\mathcal Hom(F_{1,s},G_{2,s})\) and with \(F_{2,t}\); evaluate successively into \(F_{1,s}\), then \(G_{2,s}\), then \(G_{1,t}\). The tensor–Hom adjunction, twice, gives MH24. This description determines all signs in the derived setting.

The actual microlocal kernels carry smooth projection dualizing factors. Pull them outside the displayed Hom expressions and order them as the orientation of \(X\times Y\) on the source copy. This is precisely the factor that changes the outer target pullback in MH24 into its exceptional pullback. Thus the product of the two kernels maps to the defining kernel of the right side of MH23. Apply SH02-MIC-EXTERNAL and diagonal microlocalization. Exchanging the two \(X\)-factors acted by \(\xi\mapsto-\xi\) on their diagonal conormal, which proves the stated antipode. No duality or constructibility was used.

There is a general fibre-product version that the same argument establishes without a smoothness condition:
\[
\begin{aligned}
&R\rho_{j!}\bigl(\mathsf M_X(F_2,F_1)^a\boxtimes_S^L\mathsf M_Y(G_2,G_1)\bigr)\\
&\quad\longrightarrow\mathsf M_Z\bigl(
R\mathcal Hom(q_X^{-1}F_1,q_Y^!G_2),
R\mathcal Hom(q_X^{-1}F_2,q_Y^!G_1)\bigr).
\end{aligned}
\tag{MH25}
\]
To prove it, apply MH20, rather than MH19, to MH23. Both arguments become \(j^!R\mathcal Hom(P,Q)\). On \(X\times Y\), the projection \(\widetilde q_Y\) is smooth. Replacing \(\widetilde q_Y^{-1}G_i\) by \(\widetilde q_Y^!G_i\) twists both Hom arguments by the same invertible orientation complex and does not change their microlocal Hom, by MH1. Internal exceptional adjunction then gives
\[
j^!R\mathcal Hom(\widetilde q_X^{-1}F,\widetilde q_Y^!G)
\simeq R\mathcal Hom(q_X^{-1}F,q_Y^!G).
\]
The common invertible factor induced by the preliminary replacement cancels in the two microlocal Hom arguments. This proves MH25 for every embedded fibre product in MH22.

If \(q_Y:Z\to Y\) is a submersion, then \(q_Y^!G=q_Y^{-1}G\otimes\omega_{q_Y}\), and MH1 cancels that common factor. In that case MH25 has the same target with both \(q_Y^!\) replaced by \(q_Y^{-1}\). This includes the ordinary-product case MH23.

### SH02-MH-HOM-PRODUCT-OPEN — The corrected route to the ordinary target

The general embedded fibre product need not have a submersion as its projection \(q_Y\). Direct exceptional restriction and internal exceptional adjunction give the target of MH25. For an arbitrary projection from an embedded fibre product, \(q_Y^!G\) cannot in general be replaced by \(q_Y^{-1}G\) times a fixed invertible line. MH25 and its submersion specialization therefore do not by themselves provide the general ordinary-inverse target. The full comparison is proved in `SH02-MHPC-FIBRE-PRODUCT` of the [separate-transport supplement](microlocal-hom-product-comparison.md): transport the two microlocal Hom inputs separately by MH19, then use the diagonal internal-Hom convolution. Its normalization is checked against the actual ordinary-product evaluation and adjunction maps. This construction retains arbitrary embedded manifold fibre products and uses no universal line replacement for $q_Y^!$. The named six-operation, microlocal Hom and Fourier prerequisites remain separate obligations.

## SH02-MH-GRAPH-COMPOSITION — Joining two maps

Let \(g:Z\to Y\), \(f:Y\to X\), and \(h=fg\). On \(E_h=Z\times_XT^*X\), define
\[
r(z,\xi)=(g(z),\xi)\in E_f,
\qquad
s(z,\xi)=(z,df_{g(z)}^*\xi)\in E_g.
\tag{MH26}
\]
For bounded \(F,G,H\) on \(X,Y,Z\), respectively, there are composition maps
\[
s^{-1}\mathcal H_g^+(H,G)\otimes r^{-1}\mathcal H_f^+(G,F)
\longrightarrow\mathcal H_h^+(H,F),
\tag{MH27}
\]
\[
r^{-1}\mathcal H_f^-(F,G)\otimes s^{-1}\mathcal H_g^-(G,H)
\longrightarrow\mathcal H_h^-(F,H).
\tag{MH28}
\]
Neither \(f\) nor \(g\) is assumed proper or a submersion. There is no constructibility hypothesis.

**The geometry behind the maps.** Work first on \(Q=X\times Y\times Y\times Z\), with submanifold \(M=\Gamma_f\times\Gamma_g\). Let
\(j:W=X\times Y\times Z\hookrightarrow Q\) repeat the middle coordinate, and let \(L=j^{-1}M\). Then
\[
L=\{(f(g(z)),g(z),z):z\in Z\}.
\]
The map \(j\) is transverse to \(M\). Indeed, on \(M\) the difference between its two middle coordinates is \(g(z)-y\) in local coordinates, and its derivative with respect to \(y\) is minus the identity. Thus this difference has surjective derivative, independently of the ranks of \(df,dg\). Equivalently \(TQ=Tj(W)+TM\). The induced normal map is consequently an isomorphism, and the transverse inverse comparison for microlocalization applies.

At a point of \(L\), a covector in \(N_M^*Q\) has coordinates
\[
(\xi,-df^*\xi;\eta,-dg^*\eta).
\]
Restriction by \(j\) sends it to
\[
(\xi,\eta-df^*\xi,-dg^*\eta)\in N_L^*W.
\tag{MH29}
\]
Let \(q:W\to X\times Z\) forget \(Y\). Its restriction \(L\to\Gamma_h\) is an isomorphism, with inverse
\((h(z),z)\mapsto(h(z),g(z),z)\). The transpose normal map of \(q\) selects those covectors in MH29 with zero middle component. They satisfy \(\eta=df^*\xi\), and their last component is \(-dh^*\xi\). This selection is exactly the pair of maps \((r,s)\) in MH26. These equalities prove both conormal identifications used in the composition; there is no lost independent middle covector.

**The kernel map and its trace.** On \(X\times Y\) and \(Y\times Z\), take
\[
K_f=R\mathcal Hom(G_y,F_x\otimes\omega_Y),
\qquad
K_g=R\mathcal Hom(H_z,G_y\otimes\omega_Z),
\]
where the symbols denote the appropriate inverse images and the orientation lines of smooth projections. On \(W\), evaluation gives
\[
q_{12}^{-1}K_f\otimes q_{23}^{-1}K_g
\longrightarrow
q^!R\mathcal Hom(H_z,F_x\otimes\omega_Z).
\tag{MH30}
\]
To specify it, tensor with \(H_z\), evaluate the second Hom into \(G_y\otimes\omega_Z\), then evaluate the first Hom into \(F_x\otimes\omega_Y\), carrying \(\omega_Z\) along. The result is \(F_x\otimes\omega_Y\otimes\omega_Z\), which is the right target after including the \(Y\)-fibre orientation of \(q^!\). The tensor symmetry moves the factors into the displayed order and determines the Koszul sign.

Apply the external microlocalization map to \(K_f\boxtimes K_g\) on \(Q\), the transverse ordinary inverse comparison for \(j\), and the kernel morphism MH30. Pull the resulting object on \(N_L^*W\) back to the zero-middle-covector locus in MH29. The proper-direct microlocal comparison for \(q\) then maps it to
\[
\mu_{\Gamma_h}Rq_!q^!R\mathcal Hom(H_z,F_x\otimes\omega_Z).
\]
Here the map between the submanifolds is an isomorphism, so the proper direct image on their conormal bases contributes no additional integration. Apply \(\mu_{\Gamma_h}\) to the counit \(Rq_!q^!\to1\). This gives MH27, after the initial tensor symmetry arranging the two graph factors in the stated order. Notice that \(q\) itself need not be proper: the counit is for proper-support image, which is defined for this nonproper projection. No support-properness is being assumed to construct it.

For MH28 use instead the kernels \(R\mathcal Hom(F_x,G_y\otimes\omega_X)\) and \(R\mathcal Hom(G_y,H_z\otimes\omega_Y)\). Their evaluations land in \(R\mathcal Hom(F_x,H_z\otimes\omega_X\otimes\omega_Y)\), which is again \(q^!\) of the desired composed kernel. Apply the same external, transverse-inverse, direct, and trace maps, then the antipodal pullback. Since MH29 commutes with simultaneous negation of all covectors, the maps on \(E_h\) are still exactly \(r,s\). This proves MH28 rather than merely asserting a second composition by symmetry of the two Hom arguments.

## SH02-MH-COMPOSITION — Directional composition, identities, and associativity

Taking \(f=g=1_X\) in MH27 gives
\[
\mathsf M_X(F_1,F_2)\otimes\mathsf M_X(F_2,F_3)
\longrightarrow\mathsf M_X(F_1,F_3).
\tag{MH31}
\]
In the written source order the map is \(\operatorname{comp}\circ\sigma\), where \(\operatorname{comp}\) is the usual closed-monoidal composition with the second morphism as its first tensor factor. Thus at a point homogeneous morphisms \(a:F_1\to F_2\) and \(b:F_2\to F_3\) are sent to \((-1)^{|a||b|}b\circ a\), with \(b\circ a\) denoting ordinary cochain composition. In degree zero this is the familiar composition order; all permutations used to fit MH30 retain the derived symmetry.

There is a unit morphism
\[
k_{T^*X}\longrightarrow\mathsf M_X(F,F).
\tag{MH32}
\]
Here is a construction that also proves it is a unit microlocally. If \(e:\Delta_X\hookrightarrow X^2\), then
\[
\operatorname{Hom}(k_{\Delta_X},R\mathcal Hom(q_2^{-1}F,q_1^!F))
\simeq\operatorname{Hom}(F,F).
\]
Use exceptional restriction along \(e\) and internal Hom adjunction to obtain this bijection. The identity of \(F\) therefore determines a map of ordinary kernels from \(k_{\Delta_X}\). Since \(\mu_{\Delta_X}k_{\Delta_X}=k_{T^*X}\), its microlocalization is MH32. Insert this kernel map into either factor of MH30. Its diagonal support identifies the intermediate variable with the adjacent variable; the resulting evaluation and projection trace become the identity counit for that identification. Proper base-change pasting makes this identification before applying microlocalization as well as after it. Therefore composing with MH32 on either side gives the identity of the corresponding microlocal Hom object. It would not have been enough to check this only after \(R\pi_*\), which is not a conservative functor on conic sheaves.

The compositions MH27, MH28 and MH31 are associative. To check the actual maps, take three consecutive graph kernels on a product with three independently repeated intermediate variables. Before taking any normal limit, both parenthesizations are the adjoint of the same evaluation: an input at the last manifold is evaluated successively into the second, then the first, and then the final target. Associativity of the derived tensor product identifies the two source objects, and the tensor–Hom adjunction shows equality of the two evaluation morphisms. Eliminating two intermediate variables uses
\[
R(q_1q_2)_!\simeq Rq_{1!}Rq_{2!},\qquad
\varepsilon_{q_1q_2}=\varepsilon_{q_1}\circ Rq_{1!}(\varepsilon_{q_2}),
\]
with the transitivity identification for exceptional inverse image. This identity of counits follows by taking the mate of the identity of the composite proper direct image, or directly from the two triangular identities. Hence the two traces agree, including their orientation signs.

The deformation external maps used above are the lax tensor maps obtained from evaluation under open inverse/direct adjunction; their two triple composites are mates of the same threefold tensor identity. Proper-support base-change pasting and the Fourier product kernel give the same statement after transformation. Restricting the three conormal correspondences in either order imposes exactly the two transpose-derivative equations, so it selects the same covector locus. These observations prove equality of the two microlocalized maps, relative to the coherent adjunction and base-change contracts already stated. They do not use a claim that equality of the two output objects determines a natural transformation.

Finally SH02-MH-HOM-RECOVERY identifies directional composition after forgetting covectors with ordinary composition of derived Hom. The comparison from
\(R\pi_*A\otimes R\pi_*B\) to \(R\pi_*(A\otimes B)\) is its usual lax tensor map. With it, applying \(R\pi_*\) to MH31 gives
\[
R\mathcal Hom(F_1,F_2)\otimes R\mathcal Hom(F_2,F_3)
\longrightarrow R\mathcal Hom(F_1,F_3).
\]
To verify the arrow, use the zero-section recovery of each Hom kernel. The graph evaluation MH30 becomes ordinary evaluation on the diagonal, and transitivity identifies its remaining exceptional counit with the ordinary composition counit. This is the same kernel calculation used for the unit and associativity. SH02-MH-RECOVERY fixes each individual zero-section recovery and its trace map. The [product-recovery supplement](microlocal-hom-product-recovery.md#SH02-MHPR-NORMALIZATION) proves the additional comparison for the actual MIC19 map and selected REC6/REC16 recoveries. Its C5 and C12 product squares, followed by the typed S8/S14 paste through MH30, identify the ordinary and compact recovered composition maps. The result remains relative to the individually stated prerequisite contracts.

## SH02-MH-KERNEL-COMPOSITION — Integrating an intermediate covector

Let \(K_1,F_1\in D^b(k_{X\times Y})\) and \(K_2,F_2\in D^b(k_{Y\times Z})\). Define convolution as in [Kernel calculus](kernel-calculus.md):
\[
A_1\circ A_2=Rq_{13!}(q_{12}^{-1}A_1\otimes q_{23}^{-1}A_2).
\]
On \(T^*X\times T^*Y\times T^*Z\), specify every signed projection by
\[
\begin{aligned}
p_{12}^a(x,\xi,y,\eta,z,\zeta)&=(x,\xi,y,-\eta),\\
p_{23}^a(x,\xi,y,\eta,z,\zeta)&=(y,\eta,z,-\zeta),\\
p_{13}^a(x,\xi,y,\eta,z,\zeta)&=(x,\xi,z,-\zeta).
\end{aligned}
\tag{MH33}
\]
There is a canonical morphism
\[
\begin{aligned}
&R(p_{13}^a)_!\bigl(
(p_{12}^a)^{-1}\mathsf M_{X\times Y}(K_1,F_1)
\otimes
(p_{23}^a)^{-1}\mathsf M_{Y\times Z}(K_2,F_2)
\bigr)\\
&\quad\longrightarrow
\mathsf M_{X\times Z}(K_1\circ K_2,F_1\circ F_2).
\end{aligned}
\tag{MH34}
\]
The third cotangent factor is \(T^*Z\). This follows from the domains and codomains of \(p_{23}^a\) and \(p_{13}^a\); substituting a repeated \(T^*X\) would not type these maps correctly.

**Proof, including the change of correspondence.** Set \(W=X\times Y\times Z\), let \(j:W\hookrightarrow (X\times Y)\times(Y\times Z)\) repeat the middle coordinate, and let \(q=q_{13}\). Put
\[
A=q_{12}^{-1}K_1\otimes q_{23}^{-1}K_2,
\qquad B=q_{12}^{-1}F_1\otimes q_{23}^{-1}F_2.
\]
Apply MH22 over the intermediate base \(Y\). It gives
\[
R\rho_{j!}\bigl(
\mathsf M_{X\times Y}(K_1,F_1)\boxtimes_Y^L
\mathsf M_{Y\times Z}(K_2,F_2)\bigr)
\longrightarrow\mathsf M_W(A,B),
\]
The fibre product in this expression is already a complex on the restricted cotangent correspondence of \(j\), as defined in SH02-MH-PRODUCT.

Apply \(R\varpi_{q!}\rho_q^{-1}\) to this map. MH13 for \(q\), followed by the argument change induced by \(Rq_!A\to Rq_*A\), gives
\[
R\varpi_{q!}\rho_q^{-1}\mathsf M_W(A,B)
\longrightarrow\mathsf M_{X\times Z}(Rq_!A,Rq_!B).
\tag{MH35}
\]
This is the proper-image map with both arguments proper, so its target is exactly the right side of MH34.

It remains to identify the source. An element of the restricted product cotangent space has coordinates
\((x,y,z;\xi,\eta_1,\eta_2,\chi)\), and
\[
\rho_j(\xi,\eta_1,\eta_2,\chi)=(\xi,\eta_1+\eta_2,\chi).
\]
The image of \(\rho_q\) consists of \((\xi,0,\chi)\), because \(q\) forgets \(Y\). The Cartesian pullback thus imposes \(\eta_1+\eta_2=0\). Parametrize it by \(\eta_1=-\eta\), \(\eta_2=\eta\), \(\chi=-\zeta\). Its two source projections are precisely \(p_{12}^a,p_{23}^a\), and the final target projection is \(p_{13}^a\). Proper-support base change identifies \(\rho_q^{-1}R\rho_{j!}\) with proper direct image from this Cartesian locus. Composition of proper direct images then identifies the source of MH35 with the left side of MH34. This base change is valid without properness of \(\rho_j\); it uses the proper-support base-change theorem, not ordinary direct-image base change. The coordinate parametrization is an actual isomorphism of the correspondences, so no shift or orientation twist arises from it. This proves MH34.

For three consecutive kernels, both iterations of MH34 agree after the usual associativity isomorphism for convolution. In the common cotangent space, each internal manifold contributes one equation that its two incident covectors sum to zero. The equations and the final signed projection do not depend on the order in which the two internal variables are eliminated. The kernel morphism before elimination is the threefold tensor product of the input morphisms, followed by the same evaluation. Proper-support base-change pasting and Fubini identify the two eliminations, and the counit identity used in SH02-MH-COMPOSITION identifies their morphisms. Thus this associativity is a compatibility of the actual comparison maps, not a properness claim or an assertion that MH34 is invertible.

## SH02-MH-EXAMPLES — Models that test the hypotheses

**A point with unrestricted coefficients.** Let \(i:\{x\}\hookrightarrow X\) and let \(A,B\) be any bounded complexes of \(k\)-modules. The closed-embedding case of MH13 gives
\[
\mathsf M_X(i_*A,i_*B)\simeq
j_*\underline{R\operatorname{Hom}_k(A,B)}_{T_x^*X},
\tag{MH36}
\]
where \(j:T_x^*X\hookrightarrow T^*X\). To see every map, \(E_i=T_x^*X\), \(\rho_i\) is its map to the cotangent space of a point, and \(\varpi_i=j\). Thus the left side of MH13 is exactly the displayed constant complex extended from the whole cotangent fibre. The finite global dimension of \(k\) bounds the derived module Hom; no finite generation of \(A\) or \(B\) is required. MH31 becomes ordinary derived module composition in every direction, and its identity is the constant identity of \(A\). A sheaf concentrated at one base point can therefore retain morphisms in all its cotangent directions.

**Why forgetting proper support can lose an isomorphism.** Take \(f:\mathbb R\to\{*\}\), \(G=k_{\mathbb R}\), \(F=k\), with \(k\ne0\). The graph is the whole line, so
\(P=\mathcal H_f^+(G,F)=D_{\mathbb R}k_{\mathbb R}=k_{\mathbb R}[1]\).
The left vertical of MH6 is
\[
R\Gamma_c(\mathbb R;k[1])=k\longrightarrow
R\Gamma(\mathbb R;k[1])=k[1].
\]
It is zero: \(\operatorname{Hom}_{D(k)}(k,k[1])=\operatorname{Ext}_k^1(k,k)=0\). Its right vertical is the same zero map, induced by \(R\Gamma_c(\mathbb R;k)\to R\Gamma(\mathbb R;k)\) in the first Hom argument. The two horizontal maps happen to be isomorphisms in this example, by the ordinary duality calculation. Nevertheless the four-arrow isomorphism assertion fails. This distinguishes the precise sufficient proper-support hypothesis from a claim based solely on smoothness of \(f\).

**Directions normal to a submanifold.** For a closed embedded \(M\subset X\), SH02-MH-SUBMANIFOLD and specialization of a supported sheaf give
\[
\mathsf M_X(k_M,k_M)\simeq j_*k_{N_M^*X}.
\]
There is no codimension shift. In fact \(\nu_Mk_M\) is the constant sheaf on the zero section of \(N_MX\), extended by zero. The negative Fourier kernel sends this sheaf to the constant sheaf on the entire dual bundle. Its directional identity is the section one on each normal covector. Compare this with \(\mu_Mk_X\), which has a relative orientation shift and is supported on the zero covector: changing the second Hom input changes both the support and the degree.

## SH02-MH-PROBLEMS — Worked problems and solutions

**Problem 1: track a two-step derivative.** Let \(g:\mathbb R\to\mathbb R^2\) be \(g(t)=(t,t^2)\), and let \(f:\mathbb R^2\to\mathbb R\) be \(f(u,v)=u+3v\). Calculate the two graph-composition maps in MH26 over a covector \(\xi\) at \(h(t)\), and verify MH29 has zero middle component there.

**Solution.** We have \(h(t)=t+3t^2\), \(df^*\xi=(\xi,3\xi)\), and \(dg_t^*(\eta_1,\eta_2)=\eta_1+2t\eta_2\). Hence
\[
r(t,\xi)=((t,t^2),\xi),\qquad
s(t,\xi)=(t;\xi,3\xi).
\]
Set \(\eta=(\xi,3\xi)\) in MH29. Its middle component is \(\eta-df^*\xi=0\), and its last component is \(-(1+6t)\xi=-dh_t^*\xi\). At \(t=-1/6\) the last component is zero for every \(\xi\). No invertibility of \(dh\) was used or should be inferred from composition.

**Problem 2: duality reverses the direction.** Assume \(A,B\in D^b(k_X)\) are cohomologically constructible in the precise sense of [Cohomological biduality](cohomological-biduality.md). Prove
\[
\mathsf M_X(A,B)\simeq\mathsf M_X(D_XB,D_XA)^a.
\tag{MH37}
\]
Explain where the antipode enters.

**Solution.** External Hom exchange identifies the defining kernel of \(\mathsf M_X(A,B)\) with \(B\boxtimes^LD_XA\), in the order target then source. Cohomological biduality gives \(D_XD_XB\simeq B\). The defining kernel of \(\mathsf M_X(D_XB,D_XA)\) is therefore \(D_XA\boxtimes^LB\). Exchanging the two factors, with the Koszul tensor symmetry, carries one of these kernels to the other. It fixes the diagonal and sends its conormal coordinate \((\xi,-\xi)\) to \((-\xi,\xi)\), hence acts by \(a\) on \(T^*X\). Naturality of specialization under this diffeomorphism and of the Fourier pairing gives MH37. Both uses of external exchange and the biduality of \(B\) require the stated constructibility; they do not follow from mere boundedness. The antipode is caused by the geometric factor exchange, so dropping it would change the assertion at a nonzero direction.

**Problem 3: add a passive real coordinate in two ways.** Let \(i:X\hookrightarrow X\times\mathbb R\), \(i(x)=(x,0)\), and let \(p:X\times\mathbb R\to X\). Write \((t,\tau)\) for the extra cotangent coordinates. Show that restriction of
\(\mathsf M_{X\times\mathbb R}(i_*F_2,i_*F_1)\) to \(t=0\) and any fixed \(\tau\) recovers \(\mathsf M_X(F_2,F_1)\). Show that \(\mathsf M_{X\times\mathbb R}(p^{-1}F_2,p^{-1}F_1)\) is concentrated at \(\tau=0\), and its restriction at any fixed \(t\) recovers the same object.

**Solution.** For \(i\), the correspondence space is \(T^*X\times\mathbb R_\tau\); \(\rho_i\) forgets \(\tau\), and \(\varpi_i\) inserts \(t=0\). The closed-embedding isomorphism in MH13 identifies the first object with extension from \(t=0\) of the inverse image of \(\mathsf M_X(F_2,F_1)\) along \(\rho_i\). Restriction to any \(\tau\) is consequently that object. For \(p\), the correspondence space is \(T^*X\times\mathbb R_t\); \(\rho_p\) embeds it by \(\tau=0\), while \(\varpi_p\) forgets \(t\). The smooth isomorphism in MH12, followed by MH14 and cancellation of the common line \(\omega_p=k[1]\), identifies the second object with extension from \(\tau=0\) of \(\varpi_p^{-1}\mathsf M_X(F_2,F_1)\). This proves both recoveries and explains why neither has an extra degree shift. Choosing a nonzero fixed \(\tau\) in the first case and zero in the second gives the two stabilization phenomena.

**Problem 4: test the cotangent signs without a sheaf computation.** In the composition of two kernels, start with covectors \((\xi,\alpha)\) and \((\beta,\chi)\) over \((x,y)\) and \((y,z)\). Determine the condition for their restriction to \(X\times Y\times Z\) to come from \(X\times Z\). Express the result in the variables of MH33.

**Solution.** Restriction adds the two middle components, giving \((\xi,\alpha+\beta,\chi)\). It comes from \(X\times Z\) exactly when \(\alpha+\beta=0\). Put \(\eta=\beta=-\alpha\) and \(\zeta=-\chi\). The two input covectors then become \((\xi,-\eta)\) and \((\eta,-\zeta)\), and the output is \((\xi,-\zeta)\). These are the three maps in MH33. Replacing the first negative sign by a positive sign would impose equality of the middle covectors instead of their cancellation.

**Problem 5: distinguish exceptional restriction from a stalk.** Let \(q:\{0\}\hookrightarrow\mathbb R\). Compute \(q^!k_{\mathbb R}\) and \(q^{-1}k_{\mathbb R}\). Then compare \(q^!k_{\{0\}}\) and \(q^{-1}k_{\{0\}}\). Deduce why a common shift cannot identify the two functors on all bounded sheaves.

**Solution.** The local orientation calculation gives \(q^!k_{\mathbb R}=k[-1]\), while ordinary restriction gives \(k\). Since extension from a closed point is fully faithful and \(q^!q_*=1\), both \(q^!k_{\{0\}}\) and \(q^{-1}k_{\{0\}}\) are \(k\). A shift that repairs the first pair changes the second pair incorrectly. Thus no single invertible coefficient complex identifies \(q^!\) with \(q^{-1}\) on all these inputs. Such a nonsubmersive projection occurs in a legitimate fibre product: take \(X=\{0\}\to S=\mathbb R\) and \(Y=\mathbb R\to S\) the identity. This proves the specific invalidity of the unrestricted replacement discussed in SH02-MH-HOM-PRODUCT-OPEN, while the separate-transport supplement constructs the general ordinary target by a different comparison.

**Problem 6: what is proved at the zero covector?** Let \(X\) be a vector space. In SH02-MH-GAMMA-STALK take \(\xi_0=0\), and identify the resulting colimit. Explain why this check is insufficient to prove equality of two morphisms on all of \(T^*X\).

**Solution.** The strict inequality permits only the zero cone. Its cone topology is the ordinary topology, so the projector is the identity. On \(U\), the sheaf \(G_U\) restricts to \(G\), and the term is \(H^rR\Gamma(U;R\mathcal Hom(G,F))\). The filtered colimit over \(U\) is \(H^r(R\mathcal Hom(G,F))_{x_0}\), agreeing with zero-direction recovery. A conic sheaf may be nonzero away from the zero section while having zero ordinary restriction to it. For example extension by zero of the constant sheaf on an open positive ray in a one-dimensional fibre has zero zero-stalk and nonzero positive stalks. Consequently zero-direction equality cannot detect every morphism of conic sheaves; the composition and unit arguments above use actual kernels.

## SH02-MH-ROUTES — What remains to audit and what comes next

The lesson now contains the graph and diagonal definitions, recoveries, submanifold and cone-topology tests, all four graph squares, all four graph-elimination comparisons, transport of two arguments, the external tensor map, the established external Hom maps, graph and kernel composition, units, associativity, and solved coefficient, orientation, and stabilization tests. These constructions feed the later study of localized categories and microsupport functorial estimates: the support of \(\mathsf M_X(A,B)\) restricts where a morphism can survive after localization, and MH34 describes how such restrictions behave under convolution.

The exact general fibre-product ordinary-Hom target has the relative proof `SH02-MHPC-FIBRE-PRODUCT`; SH02-MH-HOM-PRODUCT-OPEN explains the limitation of direct exceptional restriction. The trace and support verticals in the functorial graph squares have the exact identifications supplied by SH02-MIC-TRACE-EXCHANGE and the endpoint supplement. The zero-section recovery-map comparison is proved with the explicit compact normalization in SH02-MH-RECOVERY. Compatibility of the multi-kernel composition with the separately normalized product recoveries is proved relative to its stated contracts in the [product-recovery supplement](microlocal-hom-product-recovery.md). All uses of six operations, cohomological constructibility, specialization, cone topology and Fourier exchange retain the individual hypotheses and proof obligations stated by their providers. The arguments here do not close those obligations merely by citing them.

**Published sources and proof mechanisms.** Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §5.5, pp. 90–96 (PDF pp. 93–99), supplies a direct mathematical antecedent. Definition 5.5.1 defines the graph and diagonal Hom kernels by ordinary pullback in the first Hom argument and exceptional pullback in the second; Proposition 5.5.2 recovers ordinary derived Hom by pushing back to the graph. Proposition 5.5.3 treats a closed submanifold, and Propositions 5.5.4–5.5.5 and Corollaries 5.5.6–5.5.7 give graph comparisons with their proper-support, noncharacteristic or submersion hypotheses. These are concrete antecedents for SH02-MH-HOM, SH02-MH-GRAPH and the graph functorial constructions. The source permits one bounded-below input in its definition and ordinary recovery; it does not supply this lesson's explicit SH02-MD-BOUNDED-HOM amplitude estimate or justify omitting an isomorphism hypothesis.

The source's Proposition 5.5.8, pp. 94–96 (PDF pp. 97–99), also supplies the structure of SH02-MH-GAMMA-STALK: use the difference-coordinate cone as a support kernel, move that support into the first Hom argument, apply exceptional adjunction, and identify the localized kernel with the cone-topology projector. Its proof computes on a compact closure and its boundary and then uses localization triangles. The proof here gives the directional cofinality argument explicitly and uses the closed support inside a compact second-coordinate closure to justify replacing proper by ordinary direct image after localization. These are details of the same support-kernel mechanism, not grounds for claiming a new cone-stalk theorem or for dropping relative compactness. The section and support tests themselves have their antecedent in Proposition 2.3.2, pp. 46–47 (PDF pp. 49–50); the present deduction still requires the stated Fourier cone and specialization formulas.

Schapira's [*A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), pp. 19–23, presents the Fourier and positive-deformation constructions, the Sato triangle, and Definition 4.5 of microlocal Hom with the same first-covector diagonal convention. Its coefficient convention on p. 6 is a commutative unital ring of finite global dimension. The compact Hom triangle stated on p. 23 requires cohomological constructibility of the first argument. Accordingly it is not a substitute for this lesson's unrestricted raw compact graph-kernel recovery, nor for the separate constructibility hypotheses in the biduality exercise. The selected relative-trace map and codimension-parity normalization are proved through REC4–REC19 here and in the named recovery provider; neither the displayed triangle nor an object isomorphism alone specifies those maps.

The internal exceptional adjunction used in MH25 is proved by tensor–Hom adjunction and the projection formula in Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Proposition 4.6.5, p. 95; Proposition 4.6.8, pp. 96–97, identifies the corresponding diagonal kernel. Proposition 5.1.9, pp. 107–108, identifies exceptional pullback with the orientation-twisted ordinary pullback for a topological submersion. Its local proof uses compactly supported cohomology of a convex fibre. It does not assert that replacement for an arbitrary embedding. The point-embedding example and MHPC's separate transport retain exactly this distinction, without weakening the general fibre-product statement.

The common-invertible-coefficient argument, the two-argument transports, the evaluation construction of MH23, and the ordered graph compositions are specified above as actual maps. Their checks use adjunction, coherent tensor symmetry and proper-support pasting; they are not inferred from equality of recovered objects. The source passages just cited do not identify the full MHPC separate-transport comparison or the selected MHPR product and composition squares with these precise normalizations. Those conclusions therefore retain their displayed relative proofs, including both covector signs and all orientation braids. This comparison records mathematical overlap and scope, without asserting that the construction history establishes structural independence from every other treatment.
