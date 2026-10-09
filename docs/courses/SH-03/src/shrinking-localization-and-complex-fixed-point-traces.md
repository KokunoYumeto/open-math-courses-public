# Shrinking localization and complex fixed-point traces

The compact cohomology of an expanding space and the supported cohomology of a shrinking space can have different degrees while computing the same local contribution. The shrinking construction uses ordinary supported pullback, so it still makes sense when the map collapses a direction. We will stabilize an explicit support map, compare its operator with the cutoff operator, and then remove the choice of shrinking space. A local complex-scalar family will turn these real results into holomorphic stalk and costalk formulas.

*Original lesson text and complete solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The preceding lesson proves the [spectral subspace conditions](expanding-subspaces-and-hyperbolic-lefschetz-cutoffs.md#spectral-intervals-define-the-two-kinds-of-subspace), [conic projection and contraction maps](expanding-subspaces-and-hyperbolic-lefschetz-cutoffs.md#conic-projections-and-the-actual-contraction-maps), [forward cutoff stabilization](expanding-subspaces-and-hyperbolic-lefschetz-cutoffs.md#a-large-cutoff-stabilizes-by-extension-by-zero), and the [zero trace on positive rays](expanding-subspaces-and-hyperbolic-lefschetz-cutoffs.md#a-quotient-with-no-positive-eigenvalue-has-zero-ray-trace). We use the [supported cutoff morphism](homotopies-and-local-cutoffs-for-lefschetz-contributions.md#the-supported-cutoff-reverses-the-two-conditions) and that lesson's parameter-unit proof, with the [evaluated constructible biduality](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality) and [ordinary/compact dual-section comparison](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-dual-sections--duality-of-ordinary-and-supported-sections).

For the complex application we use the actual maps in [tangent specialization](specializing-lefschetz-contributions-to-the-tangent-space.md#the-point-comparison-fixes-the-normalization), [complex constructibility of specialization](../../nearby-cycles-monodromy-and-specialization/src/complex-nearby-cycles-as-normal-and-conormal-sections.md#complex-constructibility-survives-specialization), and the [complex Euler equation](../../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#the-two-complex-fourier-actions). The [submersion microsupport criterion](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-submersion--exact-pullback-and-local-descent) and [whole-complex parameter descent](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) supply transport on a small scalar disk. Each application below checks its support and map; a global trivialization around a punctured complex orbit is not assumed.

Throughout the linear proof, \(V\) is a finite-dimensional real vector space, \(k\) a characteristic-zero field, and \(F\in D^b_{\mathbb R\text{-c}}(k_V)\) is positively conic with perfect stalks. Fix
\[
 u:V\longrightarrow V,\qquad \phi:u^{-1}F\longrightarrow F,
 \qquad 1\notin\operatorname{Ev}(u).
 \qquad\text{(1)}
\]
All supports are supports in the ambient space, with the locally closed convention \(R\Gamma_LF=R\mathcal Hom(k_L,F)\). A trace is the alternating trace of the actual induced endomorphism, denoted \(\operatorname{str}\).

## The supported action needs an inverse image of the support

Let \(S\subset V\) be a shrinking space: it is invariant, \(u|_S\) has no real eigenvalue greater than one, and \(u\) on \(V/S\) has no real eigenvalue in \([0,1)\). The spectral proof in the preceding lesson gives
\[
 u^{-1}S=S.
 \qquad\text{(2)}
\]
Indeed the quotient endomorphism on \(V/S\) has no zero eigenvalue and is therefore invertible. If \(uv\in S\), its quotient class vanishes, so the class of \(v\) vanishes as well; the reverse inclusion follows from invariance. This proves (2) without requiring \(u|_S\) to be invertible. Put \(C_S=R\Gamma_S(V;F)\). Its action \(U_S\) is
\[
 \begin{aligned}
 C_S&\xrightarrow{u^*}
 R\Gamma_{u^{-1}S}(V;u^{-1}F)
 \xrightarrow{\phi}R\Gamma_{u^{-1}S}(V;F)
 =C_S.
 \end{aligned}
 \qquad\text{(3)}
\]
The first arrow combines the ordinary unit for \(u\) with the natural comparison
\(u^{-1}R\mathcal Hom(k_S,F)\to R\mathcal Hom(k_{u^{-1}S},u^{-1}F)\).
To define this comparison, pull back evaluation, identify \(u^{-1}k_S=k_{u^{-1}S}\), and curry. It is a natural morphism and need not be an isomorphism. Applying ordinary global sections and then \(\phi\) gives exactly (3). This construction is available for a singular \(u\); it uses no compact-support pullback by that map.

For the closed inclusion \(i:S\hookrightarrow V\), put \(H=i^!F\). Perfect exceptional inverse image makes \(H\) bounded constructible. The inclusion is equivariant for positive dilation. The normalized [transport through exceptional inverse image](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-functors--transport-through-sheaf-operations) therefore makes \(H\) conic: the two parameter submersions have the same positive relative orientation and shift. Closed adjunction identifies \(C_S=R\Gamma(S;H)\). The actual ordinary contraction map, restriction to the zero stalk, identifies this complex with \(H_0\), so it is perfect. Its endomorphism will be the one induced by (3), not an arbitrarily chosen action on an abstractly isomorphic stalk.

The theorem to prove is
\[
 \boxed{C_0(\phi)=\operatorname{str}(U_S)
 \quad\text{for every shrinking space }S.}
 \qquad\text{(4)}
\]

## The supported hyperbolic box reverses both boundaries

First assume that no eigenvalue of \(u\) has modulus one. Retain the invariant splitting \(V=V_+\oplus V_-\) and adapted metric from the preceding lesson:
\[
 |u_+a|\ge c_2|a|,\qquad |u_-b|\le c_1|b|,
 \qquad 0<c_1<1<c_2.
 \qquad\text{(5)}
\]
The supported cutoff is now
\[
 Q_{a,b}=\overline B_a^+\times B_b^-.
 \qquad\text{(6)}
\]
The plus ball is closed, and the minus ball open. Its intersection with its inverse image is
\[
 u^{-1}Q_{a,b}\cap Q_{a,b}
 =u_+^{-1}\overline B_a^+\times B_b^-.
 \qquad\text{(7)}
\]
The inequalities give \(u_+^{-1}\overline B_a^+\subset B_a^+\) and \(B_b^-\subset u_-^{-1}B_b^-\), even when \(u_-\) is singular. Thus (7) is closed in \(Q_{a,b}\), by its closed plus factor, and open in \(u^{-1}Q_{a,b}\), by its open minus factor. These are relative statements, exactly in the order required for the supported cutoff. A zero-dimensional factor has both its open and closed ball equal to the point; all containments and maps then retain their stated meanings.

Its compact closure has no fixed point other than zero. The supported cutoff theorem gives
\[
 C_0(\phi)=\operatorname{str}(U_{Q_{a,b}})
 \quad\text{on }C_{Q_{a,b}}=R\Gamma_{Q_{a,b}}(V;F).
 \qquad\text{(8)}
\]
The coefficient for this application is \(R\Gamma_{Q_{a,b}}F\). It is perfect constructible, and its ambient closed support lies in the compact closure of the box. Its common correspondence support is consequently compact. Since \(u-1\) is invertible, there is no additional fixed point on that closure. The operator in (8) is ordinary supported pullback to \(u^{-1}Q_{a,b}\), the coefficient map, open restriction to (7), and enlargement of its closed plus support to \(\overline B_a^+\). These are the evaluation-defined inverse comparison and the two contravariant cutoff arrows of the supported cutoff theorem.

We compare this complex with \(C_{V_-}\). Restrict to the open minus ball, then enlarge the zero plus support to the closed plus ball. These specified maps give
\[
 \beta_{a,b}:C_{V_-}\longrightarrow C_{Q_{a,b}}.
 \qquad\text{(9)}
\]
Write \(O_b=V_+\times B_b^-\) and \(N_b=\{0\}\times B_b^-\). The first step of \(\beta_{a,b}\) is ordinary open restriction
\(R\Gamma_{V_-}(V;F)\to R\Gamma_{N_b}(O_b;F|_{O_b})\).
The second is the inclusion of closed support \(N_b\subset Q_{a,b}\) inside \(O_b\). It is induced contravariantly by \(k_{Q_{a,b}}\to k_{N_b}\). Locally closed support adjunction identifies the target with
\(R\Gamma(O_b;R\Gamma_{Q_{a,b}}^{O_b}(F|_{O_b}))=C_{Q_{a,b}}\).
Thus (9) uses ordinary sections on the open ambient set; the minus direction has acquired no compact-support degree.

## Duality proves stabilization of that support map

For each fixed \(a>0\), (9) is an isomorphism when \(b\) is sufficiently large. We prove this for the actual map.

For a locally closed inclusion \(\ell:L\hookrightarrow V\), duality and its adjunction maps give
\[
 D_V(R\ell_*\ell^!F)=\ell_!\ell^{-1}D_VF.
 \qquad\text{(10)}
\]
One can verify this particular map directly. The bidual evaluation of \(F\) and tensor–Hom adjunction identify
\[
R\Gamma_LF=R\mathcal Hom(k_L,F)
\simeq D_V(k_L\otimes D_VF).
\]
The first Hom input is bounded, and both \(k_L\) and \(F\) are perfect constructible, so the tensor is constructible and biduality applies. Dualizing the displayed evaluation comparison gives (10), since \(k_L\otimes D_VF=\ell_!\ell^{-1}D_VF\). This also fixes its naturality for the coefficient arrows of open extension and closed restriction. The dualizing complex already contains the ambient orientation and degree; no new dimension shift is inserted.

Both the supported and compact complexes below are perfect. For a relatively compact locally closed set this follows from constructible operations with compact ambient closed support. For \(V_-\), ordinary contraction proves perfection of \(C_{V_-}\), and proper-support contraction proves perfection of \(R\Gamma_c(V_-;D_VF|_{V_-})\). Thus the general ordinary/proper duality identity and constructible biduality may be reversed to give
\[
 \begin{aligned}
 C_{Q_{a,b}}^\vee&\simeq R\Gamma_c(Q_{a,b};D_VF),\\
 C_{V_-}^\vee&\simeq R\Gamma_c(V_-;D_VF|_{V_-}).
 \end{aligned}
 \qquad\text{(11)}
\]
More explicitly, put \(M_L=k_L\otimes D_VF\). The evaluated global dual-section comparison gives
\(C_L\simeq R\Gamma(V;D_VM_L)\simeq R\Gamma_c(V;M_L)^\vee\).
For either \(L=Q_{a,b}\) or \(L=V_-\), the compact complex on the right is perfect by the preceding finiteness checks. Dualizing and using its actual coefficient bidual evaluation therefore gives (11), with the maps induced by the same pairing. For \(V_-\), this uses the conicity of the ordinary restriction of \(D_VF\) and its proper-support contraction; it does not require the inclusion or projection to be proper. Finiteness is established before reversing the duality comparison.

Apply the forward stabilization theorem of the preceding lesson to \(D_VF\), using \(V_-\) as its open expanding coordinate and \(V_+\) as its closed coordinate. That theorem concerns a conic coefficient and a box; its proof requires no linear dynamics in those coordinates. For fixed \(a\), it gives
\[
 R\Gamma_c(Q_{a,b};D_VF)
 \xrightarrow{\mathrm{open\ extension}}
 R\Gamma_c(\overline B_a^+\times V_-;D_VF)
 \quad(b\gg1).
 \qquad\text{(12)}
\]
Let \(q:V\to V_+\) project along \(V_-\), and put \(G=Rq_!D_VF\). The conic projection theorem makes \(G\) perfect constructible. Fibre base change and closed-ball contraction give
\[
 \begin{aligned}
 R\Gamma_c(\overline B_a^+\times V_-;D_VF)
 &\simeq R\Gamma(\overline B_a^+;G)\\
 &\xrightarrow{\mathrm{restriction}}G_0
 \simeq R\Gamma_c(V_-;D_VF|_{V_-}).
 \end{aligned}
 \qquad\text{(13)}
\]
Let \(K=D_VF\). Under the pairings (11), the dual of the closed support enlargement is closed restriction from \(Q_{a,b}\) to \(N_b\), and the dual of the ordinary open restriction is open extension from \(N_b\) to \(V_-\). The two possible orders form the square
\[
\begin{array}{ccc}
R\Gamma_c(Q_{a,b};K)&\longrightarrow&R\Gamma_c(\overline B_a^+\times V_-;K)\\
\downarrow&&\downarrow\\
R\Gamma_c(N_b;K)&\longrightarrow&R\Gamma_c(V_-;K).
\end{array}
\]
The horizontal maps are open extension in the minus coordinate; the vertical maps are closed restriction to the zero plus fibre. This is a Cartesian open/closed inclusion square. On its coefficient sheaves both paths are the same closed restriction followed by the open-extension counit. Tensoring with \(K\), then composing proper-support direct images, proves commutation with those actual maps.

The lower path is \(\beta_{a,b}^\vee\) by evaluation naturality. The upper horizontal path is (12). Integrating along \(q\) identifies the upper right term with sections of \(G=Rq_!K\) on the compact closed ball. Proper-support base change identifies the vertical restriction with the ordinary restriction \(R\Gamma(\overline B_a^+;G)\to G_0\), followed by the fibre identification in (13). Thus the upper path is precisely (12)–(13), and proves the claimed identification of the dual map. No inverse to \(u_-\), nor a dual dynamics map, is used in this argument.

Fix \(a>0\) first. The forward stabilization theorem then supplies one bound \(b_0(a)\) such that (12) is invertible for every \(b>b_0(a)\); it is a statement about conic coefficients and open/closed boxes, independent of dynamics. The conic projection theorem applies to simultaneous conicity of \(K\), as its hemisphere compactification proof shows; conicity along the individual fibres of \(q\) is not required. Equation (13) is invertible for every positive \(a\), by its actual conic closed-ball restriction. Hence the dual map is invertible for all these \(b\), and perfect biduality makes \(\beta_{a,b}\) invertible. If the minus factor is zero, the forward extension is already identity; if the plus factor is zero, the closed restriction is identity. This includes both degenerate splittings.

## The original shrinking operator commutes with stabilization

Since \(u^{-1}V_-=V_-\), (3) gives \(U_{V_-}\). We have an equality of actual maps
\[
 \beta_{a,b}U_{V_-}=U_{Q_{a,b}}\beta_{a,b}.
 \qquad\text{(14)}
\]
To verify the square, retain all three plus supports
\(\{0\}\subset u_+^{-1}\overline B_a^+\subset\overline B_a^+\)
and both minus opens \(B_b^-\subset u_-^{-1}B_b^-\). Pulling back \(\beta_{a,b}\) pulls the zero plus support to itself, because \(u_+\) is invertible, and pulls its open ambient set to \(V_+\times u_-^{-1}B_b^-\). The cutoff then restricts this minus open to \(B_b^-\). This is the same composite ordinary restriction as first applying \(U_{V_-}\) on the whole minus space and then restricting to \(B_b^-\).

In the plus coordinate, the first path enlarges zero support directly to \(\overline B_a^+\); the second enlarges it through \(u_+^{-1}\overline B_a^+\). Transitivity of closed support inclusion identifies these maps. The evaluation-defined supported inverse comparison is natural in the support coefficient, and \(\phi\) is natural under both restrictions and support inclusions. Moving it through these squares therefore preserves the composite. The open/closed square used above commutes as well. These identities prove (14) as an equality of derived morphisms for every \(a,b>0\), before stabilization. Singular \(u_-\) changes none of the containments or the ordinary restriction maps.

For sufficiently large \(b\), (9) is invertible. Equations (8) and (14) prove (4) for \(S=V_-\) in the hyperbolic case. Singular \(u_-\) causes no difficulty: the proof uses ordinary supported pullback, and duality was used to check \(\beta\), not to replace \(u_-\) by an inverse.

## A minimal shrinking space compares all choices

Let
\[
 P=\left(\bigoplus_{\lambda\in[0,1)}V^\mathbb C_\lambda\right)\cap V.
 \qquad\text{(15)}
\]
The spectral inclusions force every shrinking space to contain each whole generalized block with eigenvalue in \([0,1)\), including the zero block. Thus every such space contains \(P\). Its restriction has only these eigenvalues and its quotient has none of them, so \(P\) is itself shrinking and \(u^{-1}P=P\). These assertions include nilpotent blocks, not just eigenspaces. For a shrinking \(S\), retain \(H=i^!F\) on \(S\). The inverse support comparison for \(u^{-1}S=S\), followed by \(\phi\), defines
\[
 \chi:u_S^{-1}H\longrightarrow H.
 \qquad\text{(16)}
\]
Since \(R\Gamma_SF=i_*H\) and \(u^{-1}S=S\), the square of \(u\) with the closed inclusion \(i\) is Cartesian. Closed proper base change identifies \(u^{-1}i_*H\) with \(i_*u_S^{-1}H\). Now restrict
\(u^{-1}R\Gamma_SF\to R\Gamma_S(u^{-1}F)\to R\Gamma_SF\)
to \(S\), using the evaluation-defined first comparison and then \(\phi\). This constructs (16). Ordinary unit naturality and closed direct-image composition show that the ordinary pullback operator on \(R\Gamma(S;H)\) is exactly (3). No inverse of \(u_S\) enters.

Put \(L=S/P\), \(A=u_{S/P}\), \(p:S\to L\), and \(G=Rp_*H\). The induced \(A\) has no real eigenvalue in \([0,\infty)\): the full primary blocks in \([0,1)\) have been removed, blocks greater than one were excluded from \(S\), and one is absent. In particular \(A\) is invertible. The conic projection theorem makes \(G\) perfect constructible.

The coefficient map on \(G\) is the ordinary comparison followed by \(Rp_*\chi\):
\[
 \psi:A^{-1}Rp_*H
 \longrightarrow Rp_*u_S^{-1}H
 \xrightarrow{Rp_*\chi}Rp_*H.
 \qquad\text{(17)}
\]
The first arrow is defined by adjunction from the ordinary counit
\[
 p^{-1}A^{-1}Rp_*H
 =u_S^{-1}p^{-1}Rp_*H
 \longrightarrow u_S^{-1}H.
 \qquad\text{(18)}
\]
Write \(c:A^{-1}Rp_*H\to Rp_*u_S^{-1}H\) for that comparison and \(\epsilon_H:p^{-1}Rp_*H\to H\) for the ordinary counit. Its defining mate identity is
\[
\epsilon_{u_S^{-1}H}\,p^{-1}c=u_S^{-1}\epsilon_H,
\]
after the canonical identification \(p^{-1}A^{-1}=u_S^{-1}p^{-1}\). This fixes the comparison and the dynamics map, rather than only their objects. The square need not be Cartesian when \(u|_P\) is singular, so \(c\) is not declared invertible. All global and supported comparisons below use this mate in its given direction.

Ordinary composition gives \(R\Gamma(L;G)=R\Gamma(S;H)=C_S\), with its operator (3). At zero, the closed-support adjunction gives
\[
 R\Gamma_{\{0\}}(L;Rp_*H)
 \simeq R\Gamma_P(S;H)
 \simeq R\Gamma_P(V;F)=C_P.
 \qquad\text{(19)}
\]
Here is the nonproper adjunction check. For the point inclusion \(e:0\hookrightarrow L\), the inclusion \(j:P\hookrightarrow S\), and \(p_0:P\to0\), closed proper base change gives \(p^{-1}e_*Q=j_*p_0^{-1}Q\). Thus
\[
 \begin{aligned}
 \operatorname{Hom}(Q,e^!Rp_*H)
 &\simeq\operatorname{Hom}(p^{-1}e_*Q,H)\\
 &\simeq\operatorname{Hom}(p_0^{-1}Q,j^!H)
 \simeq\operatorname{Hom}(Q,Rp_{0*}j^!H).
 \end{aligned}
 \qquad\text{(20)}
\]
This proves the first map of (19) by Yoneda, through ordinary adjunction and the closed point counit; properness of \(p\) has not been asserted. Exceptional composition for \(P\hookrightarrow S\hookrightarrow V\) gives the second map, with the composite closed-support counit.

These comparisons also fix the actions. For ordinary sections, transpose (17) under \(p^{-1}\dashv Rp_*\). Its transpose is (18) followed by \(\chi\); the mate identity above and the ordinary triangular identity turn the resulting global operator into ordinary \(u_S\)-pullback followed by \(\chi\), namely \(U_S\). For point-supported sections perform the same transposition in (20). The inverse image of the point is \(P\), and \(u_S^{-1}P=P\) because \(A\) is invertible. The supported inverse comparison then becomes supported pullback along \(u_S\) on \(P\). The composite closed counit identifies the action of \(\chi\) with the action induced by \(\phi\) on \(R\Gamma_P(V;F)\). Naturality of evaluation, from which both support comparisons are curried, makes these identifications commute with the coefficient map. Thus the two identified operators are precisely \(U_S\) and \(U_P\), including the ordinary pullbacks.

The positive-ray proof applies to this particular \(\psi\). Its quotient map \([v]\mapsto[Av]\) on the compact sphere of positive rays has no fixed point, because a fixed ray would give a positive real eigenvalue. Whole-complex radial descent identifies the ordinary punctured operator with the descended coefficient operator on that sphere. The compact correspondence trace there is zero, even when \(\psi\) is not invertible.

All terms of the localization triangle at zero are perfect: the ordinary term is \(G_0\) by conic contraction, the point-supported term is a constructible costalk, and the punctured term is the finite sphere complex. The triangle is a triangle of endomorphisms, since \(A^{-1}(0)=0\) and (17) is the given coefficient map. With (19) it reads \(C_P\to C_S\to R\Gamma(L\setminus0;G)\xrightarrow{+1}\), carrying the two operators just identified. Trace additivity follows from the finite invariant long exact cohomology sequence: traces on consecutive image subspaces cancel. The zero punctured trace therefore gives
\[
 \operatorname{str}(U_S)=\operatorname{str}(U_P).
 \qquad\text{(21)}
\]
For \(L=0\) this is the identity. In the hyperbolic case \(V_-\) is shrinking, so (21) compares any \(S\) with \(V_-\) through \(P\). The already proved case \(S=V_-\) proves (4) for every shrinking space in that case.

## Scalar deformation also preserves the supported operator

Choose a small closed interval \(I\subset(0,\infty)\) about one such that \(tu\) never has eigenvalue one. The same \(S\) is shrinking for every parameter after making \(I\) smaller: its finitely many positive real eigenvalues and those of the quotient stay on their original side of one; zero stays zero, and negative or nonreal eigenvalues stay outside the positive real intervals. In particular \((tu)^{-1}S=S\) throughout \(I\).

The normalized positive transport of \(F\) is an isomorphism between inverse image by scalar multiplication and inverse image by projection, restricting to identity at one. Pull it back by \((v,t)\mapsto(uv,t)\), then compose with the pullback of \(\phi\). This gives a single family coefficient morphism for \(tu\), whose slice at one is the original \(\phi\).

The linear-family class theorem gives constant \(C_0(\phi_t)\). The operators \(U_{S,t}\) have constant trace too. Put \(P=\mathrm{pr}_V^{-1}F\), and let \(h(v,t)=(tuv,t)\). The equality \(h^{-1}(S\times I)=S\times I\) holds for every parameter, even if \(u_S\) is singular. The ordinary unit for \(h\), the comparison obtained by pulling back evaluation, and the one family coefficient morphism define an endomorphism of \(R\Gamma_{S\times I}(V\times I;P)\).

For the projection to \(V\), the supported parameter-unit comparison of the homotopy lesson applies to any closed support \(S\). Compactness of \(I\), ordinary fibre evaluation and the closed-support adjunction give
\(C_S\xrightarrow{\sim}R\Gamma_{S\times I}(V\times I;P)\).
Compactness of \(S\) is not used for this unit statement; it was needed there only for integrating a class. The same result on an open interval follows from whole-complex interval descent. In particular, on every open parameter interval \(J\), closed-support adjunction and ordinary interval descent identify
\[
 R\Gamma_{S\times J}(V\times J;\mathrm{pr}_V^{-1}F)
 \simeq C_S.
 \qquad\text{(22)}
\]
These are the maps induced by the same ordinary unit, and their inverses are the supported slice restrictions. Restriction in the parameter commutes with the unit, so all transition maps are identity under (22). More directly on the closed interval \(I\), every slice restriction inverts the one displayed unit. Supported pullback commutes with further slice pullback, since \(h i_t=i_t(tu)\), and the family coefficient map restricts to \(\phi_t\). Therefore each slice intertwines the family endomorphism with exactly \(U_{S,t}\). All these endomorphisms of the fixed perfect complex \(C_S\) are the same, proving trace constancy. No proper-support pullback by \(h\), and no inverse to \(u_S\), is needed.

Choose \(t\) avoiding the finitely many values \(1/|\lambda|\) for nonzero eigenvalues. The hyperbolic theorem applies to \(tu\). Constancy of both sides now proves (4) for the original \(u\). The shrinking-space theorem is complete.

## Complex constructibility supplies local scalar transport

Let \(X\) now be a complex analytic manifold, \(F\in D^b_{\mathbb C\text{-c}}(k_X)\) have perfect stalks, and let
\[
 f:X\longrightarrow X\text{ be holomorphic},\qquad
 f(x)=x,\qquad \phi:f^{-1}F\longrightarrow F,
 \qquad \det_{\mathbb C}(1-df_x)\ne0.
 \qquad\text{(23)}
\]
The determinant condition makes \(x\) an isolated fixed point by the analytic inverse function theorem applied to \(f-\mathrm{id}\). Tangent specialization replaces its local number by that for \(V=T_xX\), \(u=df_x\), and
\(\nu\phi:u^{-1}K\xrightarrow{\alpha_f}\nu_x(f^{-1}F)\xrightarrow{\nu_x\phi}K\), where \(K=\nu_xF\).
The ordinary inverse comparison \(\alpha_f\) is kept in its given direction, even for singular \(df_x\). The natural zero-stalk restriction compares it with ordinary pullback at \(x\); hence the induced map on \(K_0\simeq F_x\) is \(\phi_x\). The point-costalk object comparison is also available, but its compatibility with a dynamical supported pullback will be used only in the local-isomorphism case below. Complex constructibility of specialization makes \(K\) complex constructible with perfect stalks, and real specialization makes it positively conic. These are separate inputs: the positive deformation chamber is not treated as a holomorphic open set.

We need transport by a small complex scalar, not a globally trivial action of \(\mathbb C^*\). Write a cotangent covector as the real part of a complex covector \(\xi\). The conic Euler criterion gives \(\operatorname{Re}\langle v,\xi\rangle=0\) on \(\operatorname{SS}(K)\). Complex cotangent conicity also puts \(i\xi\) in that set; its Euler equation gives the imaginary part zero. Thus
\[
 \langle v,\xi\rangle=0
 \quad\text{on }\operatorname{SS}(K).
 \qquad\text{(24)}
\]
The factor two in the alternative real-covector convention does not change this annihilator.

Take a small rectangular coordinate neighborhood \(D_0\subset\mathbb C^*\) of one, and let \(a(v,\lambda)=\lambda v\), \(p(v,\lambda)=v\). The differential of the submersion \(a\) is
\(da(\dot v,\dot\lambda)=\lambda\dot v+\dot\lambda v\).
For \((\lambda v;\xi)\in\operatorname{SS}(K)\), its cotangent pullback has components \((\lambda\xi,\langle v,\xi\rangle)\), interpreted by real parts. Equation (24) at \(\lambda v\) says \(\lambda\langle v,\xi\rangle=0\); since \(\lambda\ne0\), the scalar component vanishes. Exact submersion pullback therefore puts all of \(\operatorname{SS}(a^{-1}K)\) in the horizontal cotangent bundle for \(p\). The submersion descent criterion now makes the whole bounded complex locally a pullback from \(V\), and its cohomology locally constant on every parameter fibre. This argument also includes \(v=0\).

Apply whole-complex interval descent successively to the two real coordinates of \(D_0\), and then restrict to a smaller disk \(D\) about one. It gives the following isomorphism
\[
 a^{-1}K\simeq p^{-1}K
 \quad\text{normalized to the identity at }\lambda=1.
 \qquad\text{(25)}
\]
Its actual construction is useful. Put \(B=a^{-1}K\). Parameter descent says that the ordinary counit \(p^{-1}Rp_*B\to B\) and evaluation at one \(Rp_*B\to K\) are isomorphisms. The map in (25) is the inverse of that counit followed by the pullback of evaluation. It restricts to identity at one by the ordinary triangular identity. Full faithfulness of parameter pullback, proved by the same descent, makes this normalized comparison unique. Thus it preserves the extension data of the whole bounded complex. On the zero orbit both restrictions are the constant complex \(K_0\); uniqueness makes (25) the identity there for every parameter. None of this asserts trivial monodromy around all of \(\mathbb C^*\).

There are only finitely many nonzero eigenvalues \(\mu\) of \(u\), and \(1/\mu\ne1\). Shrink \(D\) to avoid all these finitely many points; then \(\lambda u\) has no eigenvalue one throughout \(D\). Pull (25) back by \((v,\lambda)\mapsto(uv,\lambda)\), and follow it by the pullback of \(\nu\phi\). This constructs a single family coefficient morphism for \(\lambda u\), with the original morphism at \(\lambda=1\).

For every nonzero \(\mu\), the condition \(\lambda\mu\in\mathbb R\) defines one real line in the scalar plane. Their finite union has empty interior. Choose \(\lambda\in D\) outside it, so every nonzero complex eigenvalue of \(\lambda u\) is nonreal. Zero eigenvalues are allowed and stay zero. Along a path in \(D\) from one to this value, the supported fixed locus is contained in the compact set \(\{0\}\times[0,1]\). The linear-family theorem applied to the one coefficient morphism consequently preserves the local contribution.

## Stalk trace, and costalk trace for a local isomorphism

For the rotated \(\lambda u\), the zero subspace is expanding: its restriction has no eigenvalues, and the quotient has no positive real eigenvalue greater than one. Its compact complex is \(K_0\). The expanding theorem yields
\[
 \boxed{C_x(\phi)=\operatorname{str}(\phi_x).}
 \qquad\text{(26)}
\]
The point coefficient map in that family is the original one: (25) is identity on the zero orbit, and the pulled-back morphism there is the fixed endomorphism \((\nu\phi)_0\). The zero-stalk comparison for the actual \(\alpha_f\) identifies it with \(\phi_x\). This remains true when \(u\) has zero eigenvalues: the stalk of \(u^{-1}K\) at zero is \(K_0\), even though the full inverse image of the point may be larger than the point. No point-support pullback for a singular normal map was used to prove (26).

If \(0\notin\operatorname{Ev}(df_x)\), the inverse function theorem supplies neighborhoods \(O,O'\) of \(x\) for which \(f:O\to O'\) is an analytic isomorphism. Its inverse image of \(x\) in \(O\) is just \(x\). Thus ordinary supported pullback, followed by \(\phi\), defines the local point-support operator \(U_{\{x\}}\). Excision identifies it with the point-supported complex on \(X\). Other preimages of \(x\) outside \(O\) do not affect this local component; no global injectivity is assumed. The normal map \(u\) is invertible. After the same scalar rotation, the zero subspace is also shrinking, because every quotient eigenvalue is nonreal and zero is absent. The shrinking theorem gives
\[
 \boxed{C_x(\phi)
 =\operatorname{str}\bigl(U_{\{x\}}:
 R\Gamma_{\{x\}}(X;F)\longrightarrow R\Gamma_{\{x\}}(X;F)\bigr).}
 \qquad\text{(27)}
\]
For the scalar path, invertibility of \(\lambda u\) makes the inverse image of zero equal zero at every parameter. The supported parameter argument (22), applied to this path with \(S=0\) and the one morphism from (25), identifies all of its point-support operators with the original normal one.

It remains to compare the nonlinear action with that normal action. In the local-isomorphism neighborhoods just chosen, the lifted map of normal deformations is an isomorphism and preserves the zero-normal parameter axis. Pullback of the closed point counit and of its localization triangle therefore commutes with the boundary connecting map that defines the point-costalk comparison. Exceptional composition identifies the original and normal support counits. This is the dynamical naturality square in the tangent-specialization proof for a local isomorphism; it intertwines \(U_{\{x\}}\) with the action of \(\nu\phi\) on \(R\Gamma_{\{0\}}(V;K)\). The positive parameter and exceptional boundary degrees already cancel in that comparison. Thus (27) concerns the original operator, without an additional orientation sign. An isomorphism of costalk objects alone would not identify these actions; the local-isomorphism hypothesis is used in this square.

The additional invertibility condition has content. A branched holomorphic map can have a defined point-support action whose trace differs from the local contribution, as the fourth exercise shows.

## Constant real coefficients give the determinant sign

Return to a real analytic manifold, constant \(F=k_X\), canonical coefficient map, and a transverse fixed point \(x\). Transversality is \(\det_{\mathbb R}(1-u)\ne0\), where \(u=df_x\). Tangent specialization gives \(k_V\) with its canonical map. Choose the minimal expanding space \(W\), the sum of the real generalized eigenspaces with eigenvalue greater than one, and set \(d=\dim_{\mathbb R}W\).

Compact cohomology of \(W\) is its orientation line in degree \(d\), written \(k[-d]\) after an orientation is chosen. The restriction \(u|_W\) is invertible and has determinant equal to the product of its positive eigenvalues with their algebraic multiplicities. Hence it has positive determinant. Its proper pullback acts by \(+1\) on the compact orientation line. Concretely, in a real Jordan basis one can first scale the nilpotent parts to zero and then move the positive diagonal entries to one. This is a path of invertible maps; the associated proper linear family preserves the normalized orientation class. Thus the actual coefficient operator is identity on that line in degree \(d\), and the expanding theorem gives \(C_x(\phi)=(-1)^d\). No invertibility of \(u\) on the complementary directions is required.

This equals the determinant sign. A real eigenvalue greater than one contributes a negative factor to \(\det(1-u)\), with its algebraic multiplicity. Every other real eigenvalue contributes a positive factor, since one is excluded. Each nonreal conjugate pair contributes
\[
 (1-\lambda)(1-\overline\lambda)=|1-\lambda|^2>0.
 \qquad\text{(28)}
\]
The Jordan off-diagonal entries do not change a determinant. Consequently
\[
 \boxed{C_x(\phi)=\operatorname{sgn}\det_{\mathbb R}(1-df_x).}
 \qquad\text{(29)}
\]
More generally a locally constant perfect coefficient complex \(P\), with constant coefficient endomorphism \(b\), gives
\[
 C_x(\phi)=\operatorname{sgn}\det_{\mathbb R}(1-df_x)\,
 \operatorname{str}(b).
 \qquad\text{(30)}
\]
Indeed its compact expanding complex is \(P[-d]\), with identity on the orientation factor and \(b\) on \(P\). Rank \(m\) in shift \([r]\) gives \(m(-1)^r\) times (29).

For a complex-linear derivative,
\[
 \det_{\mathbb R}(1-u)=|\det_{\mathbb C}(1-u)|^2>0.
 \qquad\text{(31)}
\]
This explains the positive constant-coefficient holomorphic contribution. The real orientation computation uses the real dimension; a complex expanding line has dimension two.

## Exercises with complete solutions

### Equal traces can come from different degrees

*Difficulty: Introductory.*

Let \(u=-\mathrm{id}\) on \(\mathbb R\), with constant coefficient and its canonical map. Compare the expanding space zero and the shrinking space zero.

**Solution.** Both spaces satisfy their spectral conditions because the quotient eigenvalue is \(-1\). The expanding complex is the stalk \(k\), with identity and trace one. The shrinking complex is the zero costalk \(k[-1]\). To see the actual action, localization at zero has the diagonal map \(k\to k\oplus k\), with the two punctured rays ordered left and right. Its fibre has degree-one cohomology \((k\oplus k)/\operatorname{diag}k\). Reflection exchanges the two rays and therefore acts by \(-1\) on this quotient. Its alternating trace is \((-1)^1(-1)=1\), also one. The complexes have nonzero cohomology in different degrees. Both compute \(C_0=1\).

### A shrinking map can collapse a direction

*Difficulty: Intermediate.*

Take \(u=\operatorname{diag}(2,0,\tfrac12)\) on \(\mathbb R^3\), \(F=k_{\mathbb R^3}\), and \(S=\{x_1=0\}\). Calculate (3), including its degree.

**Solution.** The restriction to \(S\) has eigenvalues zero and \(1/2\), and its quotient has eigenvalue two, so \(S\) is shrinking and \(u^{-1}S=S\). Exceptional restriction to the codimension-one plane is the normal orientation line shifted by \(-1\); its ordinary sections on \(S\) are \(k[-1]\). This action can be computed without inverting the collapsing map. The complement of \(S\) consists of the two contractible half-spaces \(x_1<0\) and \(x_1>0\). Ordinary localization has the diagonal restriction \(k\to k\oplus k\), whose fibre is \(k[-1]\). Since \(u^{-1}S=S\), supported pullback gives a map of these localization triangles. It is identity on the ambient constant section and on the constants of each of the two half-spaces, because \(x_1\mapsto2x_1\) preserves their order. Collapsing the second coordinate changes neither section map. Thus \(U_S\) is identity on the quotient in degree one and has trace \(-1\), agreeing with the normal-orientation description. The shrinking theorem gives \(C_0=-1\), agreeing with \(\det(1-u)=(-1)(1)(1/2)<0\).

### The closed-plus open-minus box has one supported degree

*Difficulty: Intermediate.*

For \(u(x,y)=(2x,y/2)\) and constant coefficients, compute \(R\Gamma_{[-a,a]\times(-b,b)}(\mathbb R^2;k)\) and its cutoff trace.

**Solution.** Localize the constant sheaf on the plus line into the closed interval and its two complementary rays. Ordinary sections give the diagonal map \(k\to k^2\). Its fibre has one copy of \(k\) in degree one, so the plus support complex is \(k[-1]\). The open minus factor contributes ordinary sections \(R\Gamma((-b,b);k)=k\); it contributes no compact-support degree. The product gives \(k[-1]\). The operator first pulls the plus closed support back to \([-a/2,a/2]\). On the two complementary rays, positive dilation preserves the ordered constants; closed support enlargement back to \([-a,a]\) also restricts each ordered complementary constant identically. Their quotient generator therefore has action \(+1\). In the minus direction, inverse image enlarges the open interval to \((-2b,2b)\), and the cutoff restricts back to \((-b,b)\); pullback and restriction both preserve its ordinary constant section. The tensor factors stay in plus-then-minus order. Hence the full cutoff operator is identity on \(k[-1]\), with trace \(-1\), equal to the shrinking-plane trace and \(C_0\).

### Branching separates local and point-support traces

*Difficulty: Advanced.*

For \(f(z)=z^2\) near zero in \(\mathbb C\), with constant coefficient and canonical map, calculate the stalk, local and point-support traces. Explain the extra hypothesis in (27).

**Solution.** The derivative at zero is zero, so one is absent. The stalk map is the identity on \(k\), and (26) gives local contribution one. The point preimage is \(\{0\}\), so a point-support operator is defined, although \(f\) is branched. Localization identifies \(H^2_{\{0\}}(\mathbb C;k)\) with \(H^1(\mathbb C^*;k)\) near zero. Choose small source and target disks for which \(z^2\) maps the punctured source disk to the punctured target disk. Supported pullback is the morphism of their localization triangles induced by the ordinary unit and the canonical coefficient map. The connecting isomorphism from punctured degree-one cohomology to point-supported degree two therefore intertwines these maps. On an oriented circle the map has degree two: a positively oriented source loop traverses the target twice. Its pullback multiplies the degree-one circle class, and hence the degree-two support generator, by two. The costalk is \(k[-2]\) and its trace is two. Thus the costalk trace need not equal the local contribution when \(df_x\) has a zero eigenvalue. The local-isomorphism condition in (27) excludes this branching.

### Puncture monodromy survives scalar transport

*Difficulty: Advanced.*

Let \(j:\mathbb C^*\hookrightarrow\mathbb C\), let \(L\) have finite-dimensional fibre \(M\) and monodromy \(T\), and put \(F=j_!L\). For \(f(z)=az\), \(a\ne0,1\), choose a scalar-path lift and a coefficient morphism inducing an endomorphism \(B\) commuting with \(T\). Determine the local trace and check it using compact cohomology.

**Solution.** The zero stalk of \(j_!L\) is zero, so (26) gives contribution zero. A path lift identifies the scalar rotation with its continued coefficient action; different lifts can change that action by powers of \(T\), but do not remove the monodromy. Polar coordinates give
\[
 R\Gamma_c(\mathbb C^*;L)
 \simeq R\Gamma(S^1;L)[-1].
 \qquad\text{(32)}
\]
The circle complex is \([M\xrightarrow{T-1}M]\) in degrees zero and one. Under the chosen continuation its action is represented, up to the corresponding homotopy, by \(B\) on both terms. The shifted compact complex has degrees one and two; its trace is \(-\operatorname{tr}B+\operatorname{tr}B=0\). Equivalently, the traces on \(\ker(T-1)\) and \(\operatorname{coker}(T-1)\) agree by the invariant kernel/image exact sequences. The same cancellation holds after replacing \(B\) by \(BT^q\). Here the compact calculation is a valid check of the local number for every allowed \(a\). The map \(z\mapsto az\) is a local isomorphism, so (27) gives the point-support trace. The conic support-inclusion isomorphism identifies that point-support complex with \(R\Gamma_c(\mathbb C;F)=R\Gamma_c(\mathbb C^*;L)\), and commutes with proper pullback by this scalar homeomorphism and the coefficient map. Thus the operator just computed is the same supported operator; no general compact-cohomology trace formula for arbitrary noncompact coefficient support is being assumed. Nontrivial \(T\) is retained throughout, and no global trivialization of complex scaling was used.

### Graded point coefficients need their alternating trace

*Difficulty: Intermediate.*

On \(\mathbb C\), take a coefficient supported at zero with two copies of \(k\) in degree zero and three in degree one. Let the coefficient map act by two and three on these respective summands. For \(f(z)=2z\), calculate the local trace and the point-support trace.

**Solution.** The stalk trace is \(2\cdot2-3\cdot3=-5\). Formula (26) gives local contribution \(-5\). Since \(df_0=2\) is invertible, (27) gives the same point-support trace. A sheaf complex already supported at a point has the same point costalk and stalk; no ambient real-dimensional shift is added to those coefficients. Thus the supported operator also has alternating trace \(-5\).

### Jordan blocks count with their multiplicity

*Difficulty: Advanced.*

Let \(u=\operatorname{diag}(3,J_2(2),-3,R_{\pi/2},0)\) on \(\mathbb R^7\), where \(J_2(2)\) is one two-dimensional Jordan block and \(R_{\pi/2}\) is plane rotation. For rank \(m\) constant coefficients in shift \([r]\), compute the determinant and local contribution.

**Solution.** The positive real eigenvalues greater than one occupy three real dimensions: the eigenvalue three and the full two-dimensional block at two. Thus \(d=3\). Direct multiplication gives \(\det(1-u)=(-2)\cdot1\cdot4\cdot2\cdot1=-16\). The expanding orientation map has determinant \(3\cdot4=12>0\), so it acts by \(+1\). The compact complex is \(k^m[r-3]\), with alternating trace \(-m(-1)^r\). This is (30). The Jordan off-diagonal entry affects neither determinant.

### A complex line has an even real orientation degree

*Difficulty: Introductory.*

For \(f(z)=2z\) on \(\mathbb C\), compute the local contribution of \(k_{\mathbb C}[r]\) using the real expanding space \(\mathbb C\) and using the stalk formula.

**Solution.** The real expanding space has dimension two. Its compact complex is \(k[r-2]\), and the positive complex dilation acts by \(+1\) on the real orientation generator. Its trace is \((-1)^{r-2}=(-1)^r\). The stalk formula gives the identity on \(k[r]\), with the same trace. Using complex dimension one as a compact cohomological degree would insert an erroneous minus sign.

### The endpoint coefficient changes the shrinking answer

*Difficulty: Intermediate.*

Let \(F=k_{[0,\infty)}\) on \(\mathbb R\) with its canonical positive-dilation map. Compute the local contribution for \(u(t)=2t\) and \(u(t)=t/2\) using shrinking spaces.

**Solution.** For expansion, zero is shrinking. Its supported complex vanishes: localization maps \(R\Gamma(\mathbb R;F)=k\) isomorphically to \(R\Gamma(\mathbb R\setminus0;F)=k\), so its fibre is zero. The local contribution is zero. For contraction, the entire line is shrinking, and its ordinary supported complex is \(R\Gamma(\mathbb R;F)=k\) with identity action; the contribution is one. Both match the preceding endpoint theorem. The coefficient support, rather than only the derivative, changes the answer from the constant-sheaf determinant sign.

## Source context and the next chapter

Y. Ike, [*Hyperbolic localization via shrinking subbundles*](https://arxiv.org/abs/1602.04651v3), arXiv 1602.04651v3, 5 May 2017, §4, Definitions 4.3–4.4, specifies shrinking subbundles and their supported operator. Proposition 4.5 states a local component trace formula and omits its proof. Proposition 4.6 compares the expanding and shrinking trace functions. These results concern normal bundles over smooth fixed components. The present point proof supplies the reversed-box stabilization and its dynamical compatibility, including a singular map on the minimal shrinking block.

The complex application uses specialization and a normalized scalar family on a small disk. Its point-costalk formula requires a local isomorphism; the branched example explains that hypothesis. The next chapter relates constructible functions to Lagrangian cycles.
