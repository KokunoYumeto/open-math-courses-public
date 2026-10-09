# Transverse pullback of normalized conormal cycles

Transversality identifies the pulled-back conormal carrier with the conormal of the inverse-image submanifold. Equality of the normalized cycles also requires their coefficients. For the graph convention used here, its actual coefficient map is the relative fibre trace multiplied by the parity of the relative dimension. The same parity enters the defined zero-section normalization. We compute both signs and show that they cancel in the transverse conormal formula, including where the tangential derivative changes rank.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

[Pulling back Lagrangian cycles through a graph](pulling-back-lagrangian-cycles-through-a-graph.md#the-actual-adjoint-is-an-isomorphism) constructs the actual coefficient adjoint, and its [supported normalization](pulling-back-lagrangian-cycles-through-a-graph.md#supported-inverse-images-and-fundamental-cycles) defines the zero and conormal cycles. The [direct cotangent image](lagrangian-cycles-and-proper-cotangent-images.md#a-direct-image-has-a-cotangent-incidence-domain) specifies the closed-embedding trace used for the conormal. The proof below compares these maps using the [commuting direct microlocal square](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit), its [trace and mate calculation](../../sheaf-proof-readings/src/SH02/microlocal-endpoint-propagation.md#sh02-mep-support-the-support-square-with-its-complete-endpoint), and the ordered relative-dualizing and trace identities. The [normalized point intersection](continuous-sections-and-supported-cycle-intersections.md#every-section-meets-a-full-point-conormal-with-number-one) is used in Exercise 2.

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, gives coefficient-valued chains and an explicit twisted conormal orientation. Here the conormal is normalized by the preceding graph operation, and its transverse pullback is proved from the actual supported coefficient maps. Coefficients remain a commutative ring \(A\) of finite global dimension. Manifolds are real analytic, Hausdorff and countable at infinity, of uniformly bounded finite dimensions. All tensor products and sheaf operations below are derived unless the factors are flat sheaves. Dimensions may be treated component by component.

## The theorem includes a coefficient equality

Let \(i:Z\hookrightarrow X\) be a closed analytic submanifold of codimension \(c\), and let \(f:Y\to X\) be analytic. Assume

\[
 df_y(T_yY)+T_{f(y)}Z=T_{f(y)}X
 \quad\text{for every }y\in W=f^{-1}Z.
 \qquad\text{(1)}
\]

The inverse-image theorem makes \(W\) a closed analytic submanifold of codimension \(c\); denote its embedding by \(j:W\hookrightarrow Y\). If \(W\) is empty, both the pulled-back carrier and the output cycle are empty, and the equality below is immediate. Otherwise write \(n=\dim X\), \(m=\dim Y\), \(a=n-c\) and \(b=m-c\). With the normalizations already defined,

\[
 [T_Z^*X]=i_*[T_Z^*Z],\qquad
 [T_W^*Y]=j_*[T_W^*W],\qquad
 [T_Q^*Q]=a_Q^*[\mathrm{pt}].
 \qquad\text{(2)}
\]

We will prove that the cotangent inverse-image operation is defined on the first cycle and that

\[
 f^*[T_Z^*X]=[T_W^*Y].
 \qquad\text{(3)}
\]

No properness of \(f\), submersion condition on \(f\), constant rank of its tangential derivative, or global orientation of any manifold is assumed.

## The graph coefficient and the relative fibre trace

Retain the cotangent correspondence and coefficient notation

\[
 \begin{gathered}
 C_f=Y\times_XT^*X,
 \quad p:C_f\to Y,\quad r=f_d:C_f\to T^*Y,\quad s=f_\pi:C_f\to T^*X,\\
 E_X=\pi_X^{-1}\omega_X,\quad E_Y=\pi_Y^{-1}\omega_Y,
 \quad Q=s^{-1}E_X=p^{-1}f^{-1}\omega_X.
 \end{gathered}
 \qquad\text{(4)}
\]

The projections \(p,\pi_X,\pi_Y\) are vector-bundle submersions. For a real vector space, an ordered frame and its dual define the same positive orientation: the two transition determinants have the same sign. This specifies an integral isomorphism of the base orientation line with the dual-fibre orientation line. It also fixes the map on dualizing complexes. In a fibre chart the submersion comparison and its compact generator identify its relative dualizing object with that orientation line shifted by the fibre rank; the corresponding compact trace sends the ordered generator paired with its dual to \(1\). Pulling a frame back along \(f\) makes the same construction for \(p\), with no derivative determinant. Thus the frame identifications, with these actual traces retained, give

\[
 E_X\simeq\omega_{\pi_X},\qquad
 E_Y\simeq\omega_{\pi_Y},\qquad Q\simeq\omega_p.
 \qquad\text{(5)}
\]

These are identifications of relative dualizing coefficients along cotangent fibres, not choices of total-space orientation. On an overlap, reversing a frame reverses both its compact-support generator and its dual orientation coefficient, so their pairing remains \(1\). The square pairing of unshifted sign lines is used only for those lines; shifted inverse lines are evaluated with the order fixed by exceptional transitivity. In particular their symmetry still carries its Koszul sign.

Since \(\pi_Yr=p\), exceptional composition gives

\[
 r^!\omega_{\pi_Y}\simeq\omega_p.
 \qquad\text{(6)}
\]

Let \(\gamma_f:Q\to r^!E_Y\) be the isomorphism obtained from (5) and the inverse of (6). We compare it with the actual adjoint \(\beta_f\) constructed through the graph in the preceding lesson. Their ratio need not be \(1\): the relative parity calculated below is necessary for the normalized statement (3).

Use the graph lesson's \(F_1=\operatorname{id}_Y\times f\), diagonal \(N\), graph \(M\), \(K=f^{-1}\omega_X\) and \(\mathscr G=\delta_{Y*}K\). Its [center-supported calculation](../../sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-zero--what-survives-when-the-direction-is-forgotten) gives specialization equal to the coefficient \(K\) on the zero normal section, with its boundary counit fixed. Fourier's closed pairing kernel restricts there to the whole dual bundle, and its projection is the identity on that support. Thus the microlocalizations are naturally \(H=\pi_Y^{-1}K\) and \(Q\), with no Fourier shift. The center map is the identity of \(Y\). The ordinary and proper direct images of \(\mathscr G\) agree because \(F_1\delta_Y=\delta_f\) is a closed embedding. Its normal cone is the zero section, and the normal derivative restricted to that cone is again the identity on \(Y\), hence proper; also \(\operatorname{supp}\mathscr G\cap F_1^{-1}M\subset N\). These verify each supported hypothesis of [MIC12](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit). That square now reads

\[
 \begin{array}{ccc}
 r^{-1}H&\xrightarrow{a_{\mathscr G}}&Q\\
 \downarrow t_r&&\downarrow\mathrm{id}\\
 r^!H\otimes L&\xleftarrow{d_{\mathscr G}}&Q,
 \end{array}
 \quad
 L=p^{-1}\bigl(\omega_Y\otimes K^{-1}\bigr),
 \quad\omega_r=L^{-1}.
 \qquad\text{(7)}
\]

Here \(t_r\) is the specified relative-trace comparison

\[
 r^{-1}H\simeq r^{-1}H\otimes\omega_r\otimes L
 \longrightarrow r^!H\otimes L.
 \qquad\text{(8)}
\]

The upper arrow in (7) is the identity under \(r^{-1}H=Q\). This can be checked through its actual construction. On the positive deformation axis the direct map is the identity on \(K\); the time costalk \(A[-1]\) cancels the positive time-orientation shift \([1]\) by the endpoint restriction counit. At the central zero normal vector the two Fourier kernels both have pairing zero, so proper-support base change and projection formula restrict to identity maps on \(K\). There is no integration over a positive-dimensional normal fibre on this support. The right vertical is the proper-to-ordinary comparison on the closed diagonal support and is also the identity under the center identification. The [support comparison MEP11 with its mate endpoint MEP20](../../sheaf-proof-readings/src/SH02/microlocal-endpoint-propagation.md#sh02-mep-support-the-support-square-with-its-complete-endpoint) identifies the remaining vertical with exactly the trace arrow (8), including its ordered line pairing. Commutativity therefore gives \(d_{\mathscr G}=t_r\) as maps.

Under the graph lesson's actual right-tensor extraction, the target of (8) is transported by

\[
 r^!H\otimes L
 \simeq r^!\bigl(\pi_Y^{-1}(K\otimes(\omega_Y\otimes K^{-1}))\bigr)
 \simeq r^!E_Y.
 \qquad\text{(9)}
\]

The first map in (9) is the [exceptional tensor comparison EX.23](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-tensor--the-normalized-tensor-comparison) for the final invertible base factor \(\omega_Y\otimes K^{-1}\). Its defining transpose is proper-image projection formula followed by the counit, so it respects the adjunction used here. The last map applies the graded symmetry from \(K\otimes(\omega_Y\otimes K^{-1})\) to \((\omega_Y\otimes K^{-1})\otimes K\), then evaluates the adjacent inverse pair. The [graph proof of MIC16](pulling-back-lagrangian-cycles-through-a-graph.md#the-actual-adjoint-is-an-isomorphism) shows that (9) sends \(d_{\mathscr G}\) to \(\beta_f\): after transposition, its tensor unit and counit cancel, leaving exactly the upper inverse microlocal comparison followed by diagonal restriction. That restriction equals the ambient ordinary counit because both restrict to \(\operatorname{id}_K\) on the diagonal. Thus it is the actual coefficient map, with no freedom to multiply its adjoint by a unit of \(A\).

The distinction between \(\beta_f\) and \(\gamma_f\) is a scalar which the actual maps must determine. Both are isomorphisms between invertible complexes, so write \(\beta_f=\gamma_f u_f\), with \(u_f\) an automorphism of \(Q\). First record the geometrically normalized relative line:

\[
 \omega_r\simeq\omega_p\otimes r^{-1}\omega_{\pi_Y}^{-1}
 \simeq Q\otimes r^{-1}E_Y^{-1}.
 \qquad\text{(10)}
\]

The map in (10) is fixed by [right-tensor extraction FF3a](../../sheaf-proof-readings/src/SH02/fourier-functoriality.md#sh02-ff-conventions-the-inverse-transform-and-orientation-lines): tensor on the right with \(r^{-1}\omega_{\pi_Y}\) and recover exceptional composition by the adjacent inverse evaluation. This specifies \(\gamma_f\). It does not identify the graph coefficient merely by matching the two line objects. In particular, the coherent inverse pairing and the forward-ordered tensor–Hom counit differ in odd degree. The [right-line calculation LFT-L1–LFT-L3](../../sheaf-proof-readings/src/SH02/linear-fourier-trace.md#sh02-lft-line-order-a-coefficient-calculation-that-retains-both-orders) exhibits that difference. The two crossings of \(K\) of shift \(n\) with \(\omega_r\) and \(L\) have product \((-1)^{n(n-m)+n(m-n)}=1\), but that fact alone does not compare the contractions. We compute the remaining scalar from the original kernel maps.

Use the negative Fourier cut \(P=\{(v,\eta):v\eta\leq0\}\) on two positively oriented real lines, and put \(q:\omega_{\mathbb R_v}\to A_{\{v=0\}}\otimes\omega_{\mathbb R_v}|_0\) for ordinary zero restriction. The Fourier transform of \(\omega_{\mathbb R_v}\) is the dual zero sheaf, identified by positive compact trace. Under these identifications \(T(q)\) is **minus** the positive point Thom map into \(\omega_{\mathbb R_\eta}\). Here is a direct map calculation. The link of \(P\) has two closed connected arcs, one joining the negative \(v\)-axis to the positive \(\eta\)-axis, the other joining the positive \(v\)-axis to the negative \(\eta\)-axis. The cone localization sequence identifies \(H_c^1(P;A)\) with \(A^2/A(1,1)\). If the two arc values are \(A,B\), restriction to the \(v\)-axis gives its positive endpoint difference \(B-A\), whereas restriction to the \(\eta\)-axis gives \(A-B\). The first restriction identifies the Fourier source by compact trace; the second is compact integration of \(T(q)\). Thus their ratio is \(-1\). The two independent arc components give the same calculation over any coefficient ring. Since a supported map from the dual zero point to its dualizing line is determined by its compact trace, this computes the morphism, not merely its source and target.

For \(f:\mathbb R\to\mathrm{pt}\), the graph pair has normal map \(h:\mathbb R\to0\), and its transpose is the proper zero embedding. Write \(D_h\) for original Fourier R4 and \(E_h\) for original R2. The [actual trace equation FTE34](../../sheaf-proof-readings/src/SH02/fourier-transpose-endpoint.md#sh02-fte-trace-restore-the-original-units-and-conclude-the-trace-equation) is \(\nu_r D_h=E_h T(\theta_h)\). On the point coefficient, \(\theta_h\) is the identity of \(\omega_{\mathbb R}\), and \(\nu_r\) is the identity. The map \(E_h:T(\omega_{\mathbb R})\to A_0\) is the positive compact trace. To check its normalization, test its mate equation on \(A_0\): if \(t:A_0\to\omega_{\mathbb R}\) is the positive point trace, then \(E_hT(t)\) is ordinary restriction \(A_{\mathbb R^*}\to A_0\). Compact trace composition makes \(T(t)\) positive, so \(E_h\), and hence \(D_h\), is positive. The inverse graph coefficient is \(D_h^{-1}\) followed by \(T(q)\). The preceding negative-cut calculation therefore gives \(u_f=-1\).

The other elementary direction must also be checked. For \(f:\mathrm{pt}\to\mathbb R\), use \(h:0\to\mathbb R\). First \(D_h(\omega_{\mathbb R})\) is positive: the exceptional comparison \(\theta_h(\omega_{\mathbb R})\) is the point-composition isomorphism, the original R2 mate is positive by the same point-trace adjunction, and \(T(\omega_{\mathbb R})\) has proper point support, where \(\nu_r\) is identity. Now apply naturality to \(q\). Its ordinary pullback to zero is the identity on the coefficient. Thus
\[
D_h(A_0\otimes\omega_{\mathbb R}|_0)
   =Rr_!T(q)\,D_h(\omega_{\mathbb R}).
\]
The right side has scalar \(-1\), by the link calculation. The graph construction uses its inverse and the adjacent relative-line evaluation. Therefore this elementary direction also has \(u_f=-1\), relative to the positive fibre-collapse trace. These are two independently typed calculations, not an inference from one direction by an unsigned duality.

To pass from these tests to every derivative, retain the parameter dependence. The center-supported specialization calculation used in (7) reduces the coefficient comparison to the linear normal-bundle map \(h=df\), the original Fourier exchanges and the base-pulled orientation lines of ranks \(m,n\). All its maps commute with a change of that base: proper-support base change preserves the pairing cut and zero section, and the exceptional maps are their mates with the same counits. Right extraction commutes as well because it is characterized after faithful tensoring by a pulled-back invertible line. Thus in local frames the construction is the pullback of the universal matrix map over \(S=\operatorname{Hom}(\mathbb R^m,\mathbb R^n)\). Its cotangent incidence is \(S\times\mathbb R^{n*}\). The ratio of its two invertible coefficient maps is an endomorphism of an invertible constant complex, hence a section of the constant sheaf \(A\) on this connected space; as an automorphism it is a locally constant unit. It is therefore constant and can be computed at the zero matrix. This parameter argument is what permits rank jumps; no constant-rank deformation is assumed.

At the zero matrix, split the map as the ordered direct sum of \(m\) copies of \(\mathbb R\to0\) and \(n\) copies of \(0\to\mathbb R\). The coefficient comparisons commute with this ordered product. Before Fourier transform the maps are the tensor products of the closed units, restrictions and evaluations; at the transform stage the independently conic product comparison uses the product halfspace kernels. On the center and constant coefficients in these tests it is the ordered compact-support product map. The relative fibre trace is the product of the same ordered compact traces, by projection formula and composed counits. Reordering the input and output orientation factors to the chosen block order uses the identical graded permutations on these two routes. Consequently those permutations cancel in their ratio, and the ratios of the elementary maps multiply without an extra sign. This proves \(u_f=(-1)^{m+n}=(-1)^{m-n}\). Naturality in frames glues the calculation globally; the scalar is independent of every orientation choice. We have proved

\[
 \beta_f=(-1)^{m-n}\gamma_f,\qquad
 \rho_f=(-1)^{m-n}\operatorname{Tr}_r:
 Rr_!Q\longrightarrow E_Y.
 \qquad\text{(11)}
\]

Here \(\operatorname{Tr}_r\) denotes the geometrically normalized relative fibre trace, whose adjoint is \(\gamma_f\). It and \(\rho_f\) use \(Rr_!\), even if \(r\) is nonproper. Their bounded inputs satisfy the relative-dualizing hypotheses: a fibre of \(r\) is a closed subset of the \(n\)-dimensional fibre of \(p\) over the same point, so its compact-support cohomological dimension is at most \(n\). The coefficient complexes in (5) are bounded invertible lines. Properness is required below only on the cycle support. Neither (6) nor (11) says that either direct trace is an isomorphism.

## A supported point unit survives every tangential rank

For a manifold \(R\) of dimension \(d\), let \(z_R:R\hookrightarrow T^*R\) be its zero embedding. For \(a_R:R\to\mathrm{pt}\), the cotangent map is \(z_R\). Exceptional composition identifies \(z_R^!\omega_{\pi_R}=A_R\). Formula (11) identifies the actual graph coefficient adjoint with

\[
 A_R\xrightarrow{\;(-1)^d\;}z_R^!\omega_{\pi_R}=A_R.
 \qquad\text{(12)}
\]

Write \(p_R:z_{R*}A_R\to\omega_{\pi_R}\) for the positive fibre point trace, whose adjoint under exceptional composition is \(\operatorname{id}_{A_R}\). The normalized zero cycle defined in (2) is \([T_R^*R]=(-1)^d p_R\). This is the sign forced by that graph definition; choosing the positive point trace instead would be a different zero normalization in odd dimension. In rank zero the two agree.

This statement also proves, for every analytic \(g:V\to U\),

\[
 g^*[T_U^*U]=[T_V^*V].
 \qquad\text{(13)}
\]

First perform the calculation for the positive point traces \(p_U,p_V\). The pullback of the zero section to \(C_g\) is its zero section \(e:V\hookrightarrow C_g\). Pullback of \(p_U\) is the positive point unit \(e_*A_V\to\omega_{p_g}\). In a bundle trivialization the zero equations in the covector coordinates are unchanged. Both normal costalks and their trace evaluations use the same ordered generator, so the exceptional mate of proper-support base change identifies these particular maps. This is the product-chart submersion trace base change M28; it requires no ordinary nonproper fibre-base-change assertion and no rank condition on \(dg\).

The cotangent map satisfies \(g_de=z_V\), and it is proper on \(e(V)\), because that restriction is a homeomorphism onto the closed zero section. Apply the geometric relative trace \(\operatorname{Tr}_{g_d}\), leaving its graph parity aside for this calculation. The resulting positive supported morphism is

\[
 z_{V*}A_V=Rg_{d!}e_*A_V
 \longrightarrow Rg_{d!}\omega_{p_g}
 \longrightarrow\omega_{\pi_V}.
 \qquad\text{(14)}
\]

Exceptional composition and the composed-counit identity identify (14) with the point unit \(z_{V*}A_V\to\omega_{\pi_V}\). Namely \(e^!g_d^!\omega_{\pi_V}=z_V^!\omega_{\pi_V}=A_V\), and both adjoint maps are the identity of \(A_V\). This proves equality before forgetting the zero support.

This proves (13) with the normalized cycles: if \(\dim U=a\), \(\dim V=b\), then (11) and (12) give \(g^*((-1)^a p_U)=(-1)^{b-a}(-1)^a p_V=(-1)^b p_V\). The two parities are essential in odd relative dimension.

The positive point-unit calculation also holds for a whole parameter family. Let \(S\) be a manifold and \(\ell:S\times\mathbb R^{a*}\to S\times\mathbb R^{b*}\) a linear family over \(S\), with bundle projections \(q_a,q_b\) and zero embeddings \(e_a,e_b\). Since \(q_b\ell=q_a\) and \(\ell e_a=e_b\), the composite \(e_{b*}A_S=R\ell_!e_{a*}A_S\to R\ell_!\omega_{q_a}\xrightarrow{\operatorname{Tr}_\ell}\omega_{q_b}\) has adjoint \(\operatorname{id}_{A_S}\). This is composed counits M27, an equality over \(S\), not an inference from its individual fibres. The zero support maps properly, even when the family has noncompact kernels or changing rank.

It is natural for a bounded base coefficient morphism \(D\to D'\). Proper-image projection formula and the normalized exceptional tensor comparison transpose both routes to the same counit tensored with that morphism. This gives the normal-support trace compatibility needed below, without an exceptional base-change assertion for a nontransverse square.

## Transverse normal coordinates and the proper carrier map

Near a point of \(W\), choose analytic coordinates \(X=(t,z)\) with \(Z=\{z=0\}\), where \(t\in\mathbb R^a\), \(z\in\mathbb R^c\). Condition (1) says precisely that \(d(z\circ f)\) is surjective there. Choose \(b\) local coordinate functions whose differentials complement its \(c\) independent rows. The analytic inverse-function theorem makes these functions together with \(v=z\circ f\) an analytic coordinate system \(Y=(u,v)\) after shrinking. In these coordinates

\[
 f(u,v)=(g(u,v),v),\qquad W=\{v=0\}.
 \qquad\text{(15)}
\]

Take covectors \((\tau,\zeta)\) dual to \((t,z)\), and \((\eta_u,\eta_v)\) dual to \((u,v)\). The correspondence maps are

\[
 \begin{aligned}
 s(u,v;\tau,\zeta)&=(g(u,v),v;\tau,\zeta),\\
 r(u,v;\tau,\zeta)&=(u,v;g_u^t\tau,g_v^t\tau+\zeta).
 \end{aligned}
 \qquad\text{(16)}
\]

The pulled-back conormal carrier and its image are

\[
 \begin{gathered}
 B=s^{-1}(T_Z^*X)=\{v=0,\ \tau=0,\ \zeta\in\mathbb R^{c*}\},\\
 r(B)=\{v=0,\ \eta_u=0,\ \eta_v\in\mathbb R^{c*}\}=T_W^*Y,\\
 r(u,0;0,\zeta)=(u,0;0,\zeta).
 \end{gathered}
 \qquad\text{(17)}
\]

Globally \(df_y^t\) restricts to an isomorphism from \(N^*_{f(y)}Z\) to \(N_y^*W\). Its inverse depends analytically on local normal charts. These inverses agree as bundle inverses, so \(r|_B\) is a homeomorphism onto the closed conormal \(T_W^*Y\). Its composition with that closed inclusion is proper. This establishes the properness needed for \(f^*\), including over a noncompact \(W\).

## The coefficient and normalization in the normal chart

In the product chart \(X=(t,z)\), the normalized tangent zero section is \((-1)^a\) times the positive point unit \(\mathfrak t_\tau\) in the \(\tau\) variables. The closed embedding \(z=0\) contributes its geometric normal trace \(\nu_z\), paired by the dual frame with the normal coefficient in the \(\zeta\) variables. Keeping tangent first and normal second, the definition \(i_*[T_Z^*Z]\) is

\[
 A_{\{z=0,\tau=0\}}
 \xrightarrow{\;(-1)^a(\mathfrak t_\tau\otimes\nu_z)\;}
 \omega_{\mathbb R^{a*}}\otimes
 \omega_{\mathbb R^{c*}}=E_X
 \quad\text{in this chart}.
 \qquad\text{(18)}
\]

The two \(\omega\) factors here mean their orientation complexes pulled back to the chart. The normal \(\zeta\) variables are free; the second coefficient is not supported at \(\zeta=0\). The positive tangent point trace has free base \(t\). The normal trace is \(A_{\{z=0\}}\to\operatorname{or}_z[c]\), identified by the dual frame with \(\operatorname{or}_{\zeta}[c]\). Their tensor, multiplied by \((-1)^a\), is (18).

This is the actual direct-image definition in (2). Its coefficient map is proper-support base change followed by \(\pi_X^{-1}(Ri_!\omega_Z\to\omega_X)\). In the product chart the base-change mate computes the same normal \(z\)-costalk on both sides, with all cotangent variables unchanged. The trace pairs \(\operatorname{or}_z[-c]\) with the final normal factor of \(\omega_X=\omega_t\otimes\operatorname{or}_z[c]\); its adjoint is the identity. Thus it preserves the already defined tangent scalar \((-1)^a\) and supplies precisely the ordered normal trace. This recovers the [product-chart conormal normalization](pulling-back-lagrangian-cycles-through-a-graph.md#supported-inverse-images-and-fundamental-cycles), not an independently chosen generator.

Pull (18) back by \(s\). Its support equations \((z,\tau)\) pull back to \((v,\tau)\) identically. The positive normal Thom maps and their trace pairings are unchanged, and the scalar \((-1)^a\) is retained. Tangential dependence of \(g\) changes none of these normal variables.

Now use the source fibre shear

\[
 (\tau,\zeta)\longmapsto(\tau,\zeta'),
 \qquad \zeta'=\zeta+g_v^t\tau.
 \qquad\text{(19)}
\]

It is an analytic fibre diffeomorphism with block triangular determinant \(+1\). It fixes \(\tau=0\), preserves the normal \(v\) variable, and changes \(r\) into

\[
 (u,v;\tau,\zeta')\longmapsto
 (u,v;g_u^t\tau,\zeta').
 \qquad\text{(20)}
\]

The shear preserves the ordered fibre orientation: its derivative in \((\tau,\zeta)\) has identity diagonal blocks, and its normal action on the support equations \((v,\tau)\) is identity. The coordinate-orientation calculation and diffeomorphism counit transport both the coefficient and the supported unit without an additional sign.

Set \(S=\{(u,v;\zeta')\}\). Over \(S\), (20) is the linear family \(g_u^t:\mathbb R^{a*}\to\mathbb R^{b*}\). Put \(N_S=\operatorname{or}_{\zeta'}[c]\) and \(D=A_{\{v=0\}}\) on \(S\). The normal trace is the actual morphism \(D\to N_S\). The source and target coefficients are \(\omega_{q_a}\otimes N_S\) and \(\omega_{q_b}\otimes N_S\), with the common normal factor last. Projection formula and exceptional module compatibility identify the geometric trace with \(\operatorname{Tr}_\ell\) tensored on the right by \(N_S\): transposing either route gives the same counit. Formula (11) says that the graph coefficient is \((-1)^{m-n}\) times this map. The common normal block introduces no further permutation or scalar.

Apply the positive parameter point-unit calculation following (14), then its naturality for \(D\to N_S\). The geometric tangent trace preserves the positive point unit and moves the same \(v=0\) trace through it. The input scalar and the graph scalar multiply to \((-1)^a(-1)^{m-n}=(-1)^b\). This holds over the whole chart even at changing rank. All proper-to-ordinary inversions for the cycle occur only on \(v=0,\tau=0\), where (17) is a proper homeomorphism; the unrestricted coefficient trace remains a proper-support image. Denoting the positive output point trace by \(\mathfrak t_{\eta_u}\), we obtain

\[
 A_{\{v=0,\eta_u=0\}}
 \xrightarrow{\;(-1)^b(\mathfrak t_{\eta_u}\otimes\nu_v)\;}
 \omega_{\mathbb R^{b*}}\otimes
 \omega_{\mathbb R^{c*}}=E_Y.
 \qquad\text{(21)}
\]

The map (21) is \((-1)^b\) times the positive tangent point trace followed by the actual normal trace. Formula (12) makes this precisely the normalized tangent zero cycle for \(W\), and the description (18) for \(j\) therefore identifies it with \(j_*[T_W^*W]\). Its source is identified by the proper homeomorphism (17), so the equality retains the full conormal support.

The common normal block has dimension \(c\), and the relative fibre shift is

\[
 n-m=(a+c)-(b+c)=a-b.
 \qquad\text{(22)}
\]

The common normal factors cancel in their original order. The graph parity \((-1)^{m-n}\) is essential; multiplying it by the input zero normalization \((-1)^a\) gives exactly the output zero normalization \((-1)^b\). No additional codimension or parity factor occurs. The maps are the specified inverse-image, tensor, trace and dual-frame maps. A normal-frame reversal changes both its Thom orientation and its dual coefficient, preserving their pairing.

Equality in these charts gives global equality of the supported cycles for a precise degree reason. The common smooth carrier \(D=T_W^*Y\) has dimension \(m\) in \(T^*Y\). Closed-support costalks applied to the coefficient line \(E_Y\) shifted by \(m\) put \(R\Gamma_D E_Y\) in degree zero, with its rank-one twisted cycle coefficient. Hence \(H^0_D(T^*Y;E_Y)=\Gamma(T^*Y;H^0_D E_Y)\). The compared classes are sections of this sheaf, so their local equalities imply global equality. This is not an unrestricted local-to-global assertion about derived morphisms. It proves (3) on nonorientable and noncompact \(W\) as well. \(\square\)

## Exercises with complete solutions

### A transverse map with changing tangential rank

*Difficulty: Advanced.*

Let \(f:\mathbb R^3_{u_1,u_2,v}\to\mathbb R^2_{t,z}\) be \(f(u_1,u_2,v)=(u_1^2+u_2^3,v)\), and let \(Z=\{z=0\}\). Check transversality, compute the cotangent carrier and its normalized cycle, and check the relative shifts at the origin.

**Solution.** The normal coordinate is \(z\circ f=v\), whose derivative is surjective at every point. Thus \(W=\{v=0\}\) is transverse of codimension one. The tangent derivative of \(g=u_1^2+u_2^3\) is \((2u_1,3u_2^2)\), which has rank zero at \(u_1=u_2=0\) and rank one elsewhere. The ambient derivative correspondingly has rank one or two, so a submersion assumption would exclude the origin.

For an input covector \(\tau\,dt+\zeta\,dz\),
\[
 f_d(u_1,u_2,v;\tau,\zeta)
 =(u_1,u_2,v;2u_1\tau,3u_2^2\tau,\zeta).
 \qquad\text{(23)}
\]
On the pulled conormal, \(v=0,\tau=0\), and \(\zeta\) is arbitrary. Its image is exactly \(T_W^*\mathbb R^3\), with a proper homeomorphism on the carrier. Here \(a=1\), \(b=2\): the normalized input tangent unit has scalar \(-1\), and the graph coefficient has scalar \((-1)^{m-n}=-1\) relative to the geometric trace. Their product is \(+1=(-1)^b\), the normalized output. The parameter point-unit argument applies to \(\mathbb R^*\to\mathbb R^{2*}\) at every rank, including zero. The output therefore has coefficient \(1\) relative to the defined normalized conormal. The graph line has shift \([1]\), and the fibre relative line has shift \([-1]\); the exceptional trace supplies this dimension change, while ordinary coefficient restriction would not.

### Three transverse roots have three positive point units

*Difficulty: Intermediate.*

Over \(A=\mathbb Z\), compare pullback of the normalized point conormal at zero by \(q(t)=t^2\) and by \(h(t)=t^3-t\). For \(h\), intersect the result with any continuous section of \(T^*\mathbb R\), and explain why the derivative signs do not give a signed degree.

**Solution.** For \(q\), the only inverse point is zero and \(q'(0)=0\). Transversality fails. Its incidence over that point has arbitrary \(\xi\), all sent to the single zero covector by \(q_d(0;\xi)=(0;0)\). This noncompact fibre violates properness, so this inverse cycle operation is undefined.

For \(h\), the roots are \(-1,0,1\), with derivatives \(2,-1,2\). Each is nonzero, so the map is transverse to the point. On each incidence fibre, \(\xi\mapsto h'(t)\xi\) is a homeomorphism onto that root's full cotangent fibre. Their finite union is proper. The theorem gives
\[
 h^*[T_{\{0\}}^*\mathbb R]
 =\sum_{t\in\{-1,0,1\}}[T_{\{t\}}^*\mathbb R].
 \qquad\text{(24)}
\]
Every coefficient is the normalized unit \(+1\). At the negative branch the normal Thom orientation and the dual cotangent coefficient both reverse; the actual trace normalization retains their pairing. There is no leftover derivative sign. A continuous section meets each full fibre once. The normalized point calculation in the preceding lesson gives local intersection number \(1\) at each point, so the compact total is \(3\in\mathbb Z\). A signed degree calculation would give \(1\); it is a different operation from this twisted conormal pullback and intersection.

### A reversed normal coordinate and a nontransverse line

*Difficulty: Intermediate.*

Let \(f:\mathbb R_u\to\mathbb R^2_{x,z}\) be \(f(u)=(-u,0)\). Compare the normalized inverse image of the vertical line \(Z=\{x=0\}\) with the properness test for the horizontal line \(Z'=\{z=0\}\).

**Solution.** For \(Z\), the normal coordinate pulls back to \(-u\), with derivative \(-1\), so \(W=\{0\}\) is transverse. The input conormal has \(x=0,\zeta=0\), with arbitrary \(\xi\,dx\). Its pulled carrier has \(u=0,\zeta=0\), and \(f_d(0;\xi,0)=(0;-\xi)\). This is a proper homeomorphism onto the full cotangent fibre at zero. The theorem gives the normalized point conormal with coefficient \(1\). Choosing \(v=-u\) puts the proof in its normal-identity chart. Returning to \(u\) reverses both the normal Thom orientation and the dual-frame coefficient; their trace pairing stays \(1\). Keeping just the coordinate determinant would give a wrong negative weight. Here the input line has tangent dimension \(a=1\), so its zero normalization contributes \(-1\); the relative graph parity is also \((-1)^{1-2}=-1\). Their product gives the point normalization \(+1\), consistently with the normal-frame cancellation.

For \(Z'\), the conormal consists of arbitrary \(x\) and \(\zeta\,dz\). Its pulled carrier has arbitrary \(u,\zeta\), while \(f_d(u;0,\zeta)=(u;0)\). Each fixed \(u\) has a noncompact covector fibre. Thus inverse-image properness fails, just as transversality fails: the normal \(dz\) is killed by \(df^t\). The set image is a zero section, but that set calculation defines no inverse cycle.

### A codimension-two inverse image changes cycle dimension

*Difficulty: Advanced.*

Take \(f:\mathbb R^3_{u,v,w}\to\mathbb R^2_{z_1,z_2}\), \(f(u,v,w)=(v,w)\), and \(Z=\{0\}\). Compute the normalized output and check the coefficient degrees along the full incidence map.

**Solution.** The normal derivative onto \((z_1,z_2)\) is surjective, so \(W=\{v=w=0\}\) is the \(u\)-line, of codimension two. The pulled carrier has \(v=w=0\), arbitrary \(u\) and arbitrary \((\xi_1,\xi_2)\). Its image is
\[
 (u,0,0;0,\xi_1,\xi_2)\in T_W^*\mathbb R^3,
 \qquad\text{(25)}
\]
and the map is a proper homeomorphism. The output is the normalized conormal of that line. Its carrier has dimension three, while the input full point conormal has dimension two. Cotangent inverse image changes the Lagrangian cycle dimension to the dimension of the new base. The input has tangent dimension zero and positive point normalization. The graph parity \((-1)^{3-2}=-1\) gives the output scalar \(-1=(-1)^{\dim W}\) relative to its positive geometric tangent unit. This is coefficient \(1\) relative to the defined normalized conormal.

The full \(f_d:C_f\to T^*\mathbb R^3\) is the codimension-one embedding \((u,v,w;\xi_1,\xi_2)\mapsto(u,v,w;0,\xi_1,\xi_2)\). The target coefficient \(E_Y\) is in degree \(-3\). Its exceptional inverse image has the normal costalk shift \([-1]\), hence degree \(-2\), agreeing with \(Q=f_\pi^{-1}E_X\). The graph line has shift \(m-n=1\) and its inverse fibre line shift \(-1\). Ordinary restriction would keep degree \(-3\) and would not give the required coefficient map.

### Codimension zero permits every analytic map

*Difficulty: Intermediate.*

Set \(Z=X\). Apply the theorem to a constant map from a positive-dimensional \(Y\), and compare it with inverse image of a point conormal in a positive-dimensional \(X\).

**Solution.** The transversality condition is automatic because \(T_xZ=T_xX\). The inverse submanifold is \(W=Y\). The pulled zero carrier in \(C_f\) is precisely \(\xi=0\), and \(f_d\) identifies it with the target zero section, even for a constant map. This restriction is proper, and the positive point-unit counit calculation (14), multiplied by the input scalar \((-1)^n\) and graph scalar \((-1)^{m-n}\), gives the output scalar \((-1)^m\). Hence \(f^*[T_X^*X]=[T_Y^*Y]\). The full cotangent map for the constant map can have noncompact fibres; only the zero carrier is used here. Neither properness of the base map nor any positive derivative rank is needed.

If instead \(Z=\{x\}\) and the constant value is \(x\) in an \(n>0\) dimensional \(X\), the pulled point conormal contains all \(\xi\in T_x^*X\). Every one is killed by \(df^t=0\), so a whole noncompact \(n\)-space lies over each target zero covector. Properness fails. If the constant value lies outside the point, the pulled carrier is empty and the output is zero. The permitted zero-section pullback therefore supplies no permission to pull back an arbitrary conormal through the same constant map.

### A large noncompact kernel disappears on the actual support

*Difficulty: Advanced.*

Let \(f:\mathbb R_u\to\mathbb R^3_{x,y,z}\), \(f(u)=(u,0,0)\), and let \(Z=\{x=0\}\). Verify (3) and explain the tangent point-unit trace when the target conormal's base has dimension two.

**Solution.** The normal coordinate \(x\circ f=u\) has derivative \(1\), so \(W=\{0\}\) is transverse. The conormal of the \(yz\)-plane has \(x=0\), tangent covectors \(\eta=\zeta=0\), and arbitrary normal \(\xi\,dx\). Thus the pulled carrier is \(u=0,\eta=\zeta=0\). The map
\[
 f_d(u;\xi,\eta,\zeta)=(u;\xi)
 \qquad\text{(26)}
\]
is a proper homeomorphism on that carrier onto the point conormal in \(T^*\mathbb R\). The theorem identifies its coefficient with the normalized point unit \(1\).

The full map (26) forgets \((\eta,\zeta)\in\mathbb R^{2*}\), so it is nonproper. In the proof, the tangent map from \(W\) to the plane \(Z\) sends its two tangent covectors to the rank-zero cotangent space of a point. We apply its trace to the unit supported at \((\eta,\zeta)=0\). That support maps properly to the point, and the point-embedding counit followed by the collapse counit is the identity point counit. We have not integrated a cycle carried by the whole noncompact two-dimensional tangent-covector space. Here \(m-n=-2\), the graph line has shift \([-2]\), and the fibre relative line has shift \([2]\). Those shifts are part of the actual relative trace, which the point-supported composition handles without an additional scalar or sign.

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, explains chains with coefficients and gives the explicit conormal orientation pairing. Its §3 fixes a field for characteristic cycles. The ring of finite global dimension in the present transverse-cycle theorem is retained through the programme's chain and dualizing constructions; it is not inferred from that later field-coefficient discussion. Nor does an abstract identification of a conormal carrier determine its coefficient.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4–4.6.8, §4.7, Proposition 5.1.5(a)–(c) and Proposition 5.1.9, pp. 95–97 and 107–108, provides the exceptional, support, tensor and orientation framework. The linked programme proofs specify the actual microlocal maps and their ordered line comparisons. The argument above separately tests the coefficient normalization, the proper carrier, and the changing-rank tangential family, then glues the supported cycle sections. Human sources retain their authorship and their own terms.
