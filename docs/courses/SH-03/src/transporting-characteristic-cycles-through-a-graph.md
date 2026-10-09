# Transporting characteristic cycles through a graph

Transport of a characteristic cycle must carry its identity and its evaluated trace. A graph separates a map into two changes of one product variable. This makes ordinary restriction, proper duality and the relative orientation visible. We prove proper direct image and noncharacteristic inverse image with their actual microlocal comparisons, then obtain normalized conormal cycles for globally constant finite coefficients.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The proof follows the identity, its evaluated kernel and its supported coefficient through two changes of a product variable. [The supported microlocal identity construction](characteristic-cycles-from-supported-microlocal-identities.md#ordinary-restriction-and-the-unique-supported-trace) specifies the input cycle. The [evaluated proper-duality calculation](proper-characteristic-classes-and-the-compact-index.md#evaluation-completes-the-trace-diagram) controls direct image; the [actual graph adjoint](pulling-back-lagrangian-cycles-through-a-graph.md#the-actual-adjoint-is-an-isomorphism) and [graph/fibre-trace comparison](transverse-pullback-of-normalized-conormal-cycles.md#the-graph-coefficient-and-the-relative-fibre-trace) specify the inverse-cycle map.

The applications below use the [two microlocal functorial squares](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit), their [unit-and-counit identities](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-adjunctions--checking-the-actual-comparison-maps), the [microlocal support bound](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-microlocal-support--where-directional-sheaves-can-live), and the [inverse comparison for a submersive center](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-submersive-centers--a-simpler-test-on-the-centers). The positive-first conormal parameter used for microlocal Hom differs from the inverse-cycle lesson's parameter by a fibre antipode. We keep that comparison visible: it supplies a dimension sign in inverse transport with the normalized cycles used here.

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§2–3, pp. 196–199, supplies the twisted conormal and characteristic-cycle framework. The graph argument here proves transport by following the specified kernel units and evaluations; it retains the distinction between the conormal parameters in the cycle operation and in microlocal Hom. We retain a field \(k\) of characteristic zero and bounded R-constructible complexes with perfect stalks. Manifolds are real analytic, Hausdorff and countable at infinity, with the standing uniform finite dimension bounds. No global orientation is chosen.

## The two carriers and coefficient maps

Let \(f:Y\to X\) be analytic, with \(\dim Y=m\) and \(\dim X=n\). Dimension-dependent signs are interpreted component by component. Set

\[
 \begin{gathered}
 C=Y\times_XT^*X,\quad p:C\to Y,\\
 r(y;\xi)=(y;df_y^t\xi),\qquad
 s(y;\xi)=(f(y);\xi),\\
 E_Y=\pi_Y^{-1}\omega_Y,\quad E_X=\pi_X^{-1}\omega_X,
 \quad Q=s^{-1}E_X=p^{-1}f^{-1}\omega_X.
 \end{gathered}
 \qquad\text{(1)}
\]

The transpose in \(r\) is positive. Direct image uses a carrier
\(S=\operatorname{SS}(G)\subset T^*Y\),
\(S'=r^{-1}S\subset C\), and \(S''=s(S')\).
Its hypothesis is properness of \(s\) on \(S'\).
Inverse image uses \(S=\operatorname{SS}(F)\subset T^*X\),
\(B=s^{-1}S\), and \(T=r(B)\).
Its hypothesis is properness of \(r\) on \(B\).
The geometric cotangent transport theorem makes the resulting \(S''\) or \(T\) closed, conic, subanalytic and isotropic under the respective properness test. These are allowed cycle carriers.

The cycle operations use the coefficient maps

\[
 \begin{aligned}
 R s_!r^{-1}E_Y
 &=R s_!p^{-1}\omega_Y
   \longrightarrow E_X,\\
 R r_!Q&\xrightarrow{\rho_f}E_Y.
 \end{aligned}
 \qquad\text{(2)}
\]

The first is Cartesian proper-support base change followed by
\(\pi_X^{-1}\operatorname{tr}_f\).
The second is the actual graph comparison of the [inverse-cycle construction](pulling-back-lagrangian-cycles-through-a-graph.md#construct-the-coefficient-arrow-before-using-a-carrier). That construction uses \((-df^t\xi,\xi)\) on the graph and \((-\eta,\eta)\) on the diagonal. Its exceptional adjoint \(\beta_f:Q\to r^!E_Y\) is the particular isomorphism proved there. Exceptional composition also gives an auxiliary isomorphism from the [cotangent-fibre dualizing lines](transverse-pullback-of-normalized-conormal-cycles.md#the-graph-coefficient-and-the-relative-fibre-trace). Identifying these two maps requires their orientation normalization; an isomorphism of their endpoint objects alone would not suffice. For the comparison below we use the actual \(\beta_f\) and explicitly track the change to the positive-first parameters of the Hom kernel. Properness is required on the supported objects to which these arrows are applied, rather than on every point of their ambient domains.

For \(G\) with closed support \(Z\) and \(f|_Z\) proper, \(s\) is proper on \(S'\). Indeed its inverse image of a compact cotangent set has base points in the compact set \(Z\cap f^{-1}(\pi_X K)\) and bounded \(\xi\). The incidence and \(S'\) are closed, so this inverse image is compact. The same proof makes \(s\) proper on every closed subset of \(p^{-1}Z\). No norm bound for \(df^t\) is needed here.

For inverse image, properness of \(r|_B\) is equivalent to

\[
 B\cap\ker r\subset\{\xi=0\}.
 \qquad\text{(3)}
\]

The proof is the [compact uniform lower-norm argument](pulling-back-lagrangian-cycles-through-a-graph.md#the-two-cotangent-properness-conditions-are-different): a killed nonzero covector gives an unbounded ray over one target point; conversely, failure of a compact lower bound gives a normalized nonzero killed limit. Condition (3) is noncharacteristicity for \(F\). Neither condition implies the other.

We will also use \(\operatorname{SS}(D_WB)=\operatorname{SS}(B)^a\) for bounded constructible \(B\) on a manifold \(W\). The [Hom microsupport estimate with constant target](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-external-hom--reversing-the-second-direction) gives the inclusion for coefficient duality; tensoring by the invertible \(\omega_W\) changes no support test. Applying that inclusion to \(D_WB\) and using the [actual constructible biduality map](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality) gives the reverse inclusion. The antipode in this equality is essential in both graph support calculations.

## The direct-image graph keeps the ordinary counit

Put

\[
 P=Rf_!G\simeq Rf_*G,\qquad
 D=D_YG,\qquad Q_P=D_XP\simeq Rf_!D,
 \qquad\text{(4)}
\]

where the last is the inverse of the actual evaluated map \(Rf_!D\to D_XP\) in [proper duality](proper-characteristic-classes-and-the-compact-index.md#properness-is-imposed-on-a-closed-support). Its curry is projection, the ordinary counit on a pulled-back coefficient, graded evaluation and the trace \(Rf_!\omega_Y\to\omega_X\). The [proper perfect-image proof](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) and constructible duality make every object in (4) bounded constructible with perfect stalks. The supports of \(D\) and \(R\mathcal Hom(G,G)\) lie in \(Z\), so proper and ordinary images agree on those objects as well. Define

\[
 \begin{gathered}
 f_1=f\times\mathrm{id}_Y:Y^2\to X\times Y,
 \qquad f_2=\mathrm{id}_X\times f:X\times Y\to X^2,\\
 \gamma(y)=(f(y),y),\quad
 H=G\boxtimes D,\quad K=P\boxtimes D,
 \quad J=P\boxtimes Q_P.
 \end{gathered}
 \qquad\text{(5)}
\]

The diagonal \(\delta_Y\), graph \(\gamma\) and diagonal \(\delta_X\) are closed. The first change has center map the identity and normal derivative \(df\); its conormal correspondence is \(r\) followed by the identity of \(C\). The second change has center map \(f\) and identity normal derivative; its correspondence is the identity of \(C\) followed by \(s\). On the graph we use
\((f(y),y;\xi,-df_y^t\xi)\).
For these positive-first-covector identifications, the normal differences are \(v_1-v_2\) on either diagonal and \(v_X-df(v_Y)\) on the graph. They give \(df\) for \(f_1\) and the identity for \(f_2\), including their signs.

Properness on \(Z\) gives product isomorphisms
\(Rf_{1!}H\simeq K\) and \(Rf_{2!}K\simeq J\), with ordinary and proper images agreeing on these kernels. For the first map this follows on the containing support \(Z\times Z\); for the second it follows on \(\operatorname{supp}(P)\times Z\). The two upper direct microlocal comparisons therefore give

\[
 r^{-1}\mathsf M_Y(G,G)
 \xrightarrow{a_1}\mu_\gamma K,
 \qquad
 Rs_!\mu_\gamma K
 \xrightarrow{a_2}\mathsf M_X(P,P).
 \qquad\text{(6)}
\]

These are the specified comparisons, including the product isomorphisms in (4)–(5). The first need not be an isomorphism. The second has an inverse ordinary comparison

\[
 d_2:\mathsf M_X(P,P)\longrightarrow Rs_*\mu_\gamma K.
 \qquad\text{(7)}
\]

To verify invertibility, apply the three closed-support conditions of [MIC12](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit) to \(f_2\). It is proper on \(\operatorname{supp}K\), its preimage of \(\Delta_X\) is exactly \(\Gamma_f\), and its normal derivative is the identity. The normal map on the closed normal cone of \(\operatorname{supp}K\) is proper: compact target base bounds \(y\) in \(Z\) by properness of \(f|_Z\), and bounded target normal coordinates bound the source normal coordinates, which are unchanged. The cone is closed, so these bounds give compact inverse images. All three tests hold. The relative line for this second pair is the unit, and its left vertical is \(Rs_!\to Rs_*\). The support of \(\mu_\gamma K\) lies over \(Z\), so that vertical is invertible by the compactness observation following (2). Consequently (7) is inverse to (6)'s second map under this support comparison.

Write \(\lambda_N(A):A\to i_{N*}i_N^{-1}A\) for the **ordinary** closed unit. The first restriction comparison is

\[
 \gamma_*\bigl(b_G\otimes1_D\bigr)
 \lambda_\gamma(K)
 =Rf_{1!}\lambda_{\Delta_Y}(H),
 \qquad b_G:f^{-1}Rf_*G\to G,
 \qquad\text{(8)}
\]

under the product and closed-composition identifications. Both sides map \(Rf_{1!}H\) to \(\gamma_*(G\otimes D)\). In particular, \(b_G\) is a counit pointing from the pulled-back image to \(G\). It has not been inverted.

Here is an explicit verification of (8). For ordinary direct image, let \(i=\delta_Y\), \(h=f_1i=\gamma\), and denote ordinary units and counits by \(a,b\). The unit of the composite adjunction and its triangular identity give

\[
 h_*\bigl(i^{-1}b_{f_1,H}\bigr)
       a_{h,Rf_{1*}H}
 =Rf_{1*}a_{i,H}.
 \qquad\text{(9)}
\]

Expand the composite unit as the unit for \(f_1\) followed by that for \(i\), move the counit past the latter by naturality, and cancel \(Rf_{1*}b_{f_1,H}\,a_{f_1,Rf_{1*}H}\). This proves (9). On the diagonal its counit is \(b_G\otimes1_D\). Both \(H\) and \(i_*i^{-1}H\) have closed supports on which \(f_1\) is proper; the support-forgetting comparisons respect the units. Thus (9) is (8).

For \(f_2\), the graph square over \(\Delta_X\) is Cartesian. Proper-support base change and compatibility with the closed unit give the second restriction cell

\[
 \lambda_{\Delta_X}(J)
 =\delta_{X*}B\;Rf_{2!}\lambda_\gamma(K),
 \quad
 B:Rf_!\gamma^{-1}K\xrightarrow{\sim}\delta_X^{-1}J.
 \qquad\text{(10)}
\]

This is the [Cartesian closed-restriction identity](closed-supports-and-evaluated-proper-transport.md#a-cartesian-closed-restriction-compares-before-support-is-forgotten). Transposing both sides along \(\delta_X^{-1}\dashv\delta_{X*}\) leaves the same proper-base-change map \(B\); the closed ordinary counit cancels its unit. Thus it holds before any vertical proper support is forgotten.

On the graph, set
\(t_\gamma=t_G(b_G\otimes1_D):f^{-1}P\otimes D\to\omega_Y\).
The evaluated proper-duality comparison in (4) says

\[
 t_P\;B
 =\operatorname{tr}_f\;Rf_!t_\gamma.
 \qquad\text{(11)}
\]

Its proof curries the two pairings against \(P\). Projection formula, the ordinary counit and \(Rf_!\omega_Y\to\omega_X\) give the defining internal-adjunction pairing on both paths. The support-forgetting evaluation identity compares the counit on \(G\) with the counit on \(D\). Their flat/soft resolution evaluations coincide on properly supported sections. The same graded permutations occur in both evaluations. This is the [evaluated identity (19)](proper-characteristic-classes-and-the-compact-index.md#evaluation-completes-the-trace-diagram), obtained from the [support-forgetting evaluation equality EX.40–EX.41](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom-support-compatibility--evaluation-when-either-support-is-forgotten). It compares the two actual pairings while retaining their graded tensor order.

## Naturality supplies every microlocal trace cell

Put \(v_G=\delta_{Y*}t_G\lambda_{\Delta_Y}\),
\(v_\gamma=\gamma_*t_\gamma\lambda_\gamma\), and
\(v_P=\delta_{X*}t_P\lambda_{\Delta_X}\).
Equations (8),(10),(11) give actual kernel identities

\[
 Rf_{1!}v_G=v_\gamma,
 \qquad
 v_P=\delta_{X*}\operatorname{tr}_f\;Rf_{2!}v_\gamma.
 \qquad\text{(12)}
\]

The intermediate ordinary restriction objects and the counit in (8) remain part of this factorization. Apply naturality of the upper direct microlocal comparison separately to these maps. For a center-supported coefficient its specialization is on the zero normal section, and Fourier projects that zero-normal kernel by the identity. Hence the first center-supported comparison is the identity on \(p^{-1}\omega_Y\). The second is Cartesian proper-support base change
\(Rs_!p^{-1}\omega_Y\simeq\pi_X^{-1}Rf_!\omega_Y\).
Its final map is \(\pi_X^{-1}\operatorname{tr}_f\).

Thus, if \(\kappa\) denotes the trace after microlocalization, every restriction and evaluation cell of (12) has the same actual arrow after microlocalization, and

\[
 \begin{aligned}
 \kappa_\gamma a_1&=r^{-1}\kappa_G,\\
 \kappa_P a_2
 &=\bigl(Rs_!p^{-1}\omega_Y\to E_X\bigr)
                   Rs_!\kappa_\gamma.
 \end{aligned}
 \qquad\text{(13)}
\]

This proves the coefficient row of the full direct-image diagram. It also proves its middle rows: (8) is the ordinary restriction/counit cell, (10) is the Cartesian restriction cell, and (11) is the evaluated-duality cell; naturality uses these particular morphisms, rather than an isomorphism of their endpoint objects.

The support needed here is the full cotangent carrier, not merely its base projection. By the [external product estimate](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-external-tensor--product-tests) and [microlocalization support bound](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-microlocal-support--where-directional-sheaves-can-live), a point of \(\operatorname{supp}\mu_\gamma K\) has graph covector \((\xi,-df_y^t\xi)\) whose second component lies in \(\operatorname{SS}(D)\). The duality identity above makes \(df_y^t\xi\in\operatorname{SS}(G)\). Therefore \(\operatorname{supp}\mu_\gamma K\subset S'\). Both sources in the first row of (13) are now supported on the same closed carrier.

The map \(s\) is proper there, so \(Rs_!\mu_\gamma K\to Rs_*\mu_\gamma K\) is an isomorphism and its target support is contained in \(S''\). Any map from an object supported on a closed set \(A\) to \(E\) has a unique factorization through \(R\Gamma_AE\): apply Hom from that object to the localization triangle for the complement, whose last term has zero Hom in every degree by open adjunction. Applying this fact to (13) supplies its actual supported coefficient maps. Ordinary global sections are transferred from \(Rs_*\) to \(Rs_!\) only on this supported kernel. The [proper-image microsupport estimate](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-proper-push--collecting-tests-along-a-fibre) places \(\operatorname{SS}(P)\) in \(S''\), so both final traces are compared in \(H^0_{S''}(T^*X;E_X)\), even when the actual output support is smaller.

## The transported microlocal identity is the identity of the image

The unit \(u_G:k_{\Delta_Y}\to H\) represents \(\mathrm{id}_G\). Its first proper image is a graph map
\(v:k_{\Gamma_f}\to K\).
Exceptional graph restriction identifies this map with
\(G\to f^!P\), the exceptional unit. To check its normalization, curry the first-factor product map in (5) against \(G\): its adjoint is \(Rf_!G\to P\), the identity. This is precisely the defining adjunction of that unit. The center-supported upper comparison sends \(1\) to \(1\), so
\(e_\gamma=\mu_\gamma v=a_1r^{-1}e_G\).

Before microlocalization, ordinary image of \(v\) and the ordinary unit \(k_X\to Rf_*k_Y\) give \(u_P\). To verify the particular map, the [constructible external-Hom evaluation](../../sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-external-hom--a-constructible-factor-in-a-product) identifies \(\gamma^!K\) with \(R\mathcal Hom(G,f^!P)\). The resulting graph adjunction is the chain
\(\operatorname{Hom}(k_{\Gamma_f},K)\simeq\operatorname{Hom}(G,f^!P)\simeq\operatorname{Hom}(Rf_!G,P)\).
The first graph unit represents \(\eta_G\), and its last adjoint is \(\varepsilon_P Rf_!\eta_G=\mathrm{id}_P\). The [evaluated graph-Hom proof](proper-characteristic-classes-and-the-compact-index.md#the-hom-comparison-transports-the-endomorphism-itself) identifies this chain with the product isomorphisms in (4)–(5), including the actual proper-duality curry. Thus the ordinary image and unit produce the identity under the target's diagonal Hom adjunction. Since the closed diagonal adjunction is a bijection on morphisms, the kernel map itself is \(u_P\). No inference from ordinary microlocal recovery alone is needed.

The specified ordinary microlocal identity [MIC16](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-adjunctions--checking-the-actual-comparison-maps), applied to this kernel map and its ordinary adjoint \(v\), yields

\[
 d_2e_P=Rs_*e_\gamma\;\eta_s,
 \qquad \eta_s:k_{T^*X}\to Rs_*k_C.
 \qquad\text{(14)}
\]

To see why (14) is a statement about this unit, the ordinary microlocal identity inserts the \(s^{-1}\dashv Rs_*\) unit, applies the orientation-canceled upper inverse comparison, and then the ordinary counit. On \(k_{\Delta_X}\) the inverse comparison is the zero-normal identity onto \(k_{\Gamma_f}\). Its last counit is the ordinary adjoint \(v\) just identified. This gives exactly (14), with the maps fixed before and after microlocalization. Checking only after \(R\pi_*\) would not prove it.

Since (7) is invertible, (14) says that (6), with ordinary support replaced by proper support on \(\mu_\gamma K\), carries the unit in the direct-image diagram to \(e_P\). Applying the supported trace equalities (13) to it proves

\[
 \boxed{CC(Rf_*G)=f_!CC(G)\quad
               \text{if }f\text{ is proper on }\operatorname{supp}(G).}
 \qquad\text{(15)}
\]

The top constant term remains \(Rs_*k_C\) in (14). We have imposed no properness on \(k_C\). Only its image in the supported microlocal kernel is passed through \(Rs_!\).

## Inverse image retains its relative dualizing factor

Let \(F\) be bounded constructible and satisfy (3). The [perfect inverse-image theorem](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom) makes \(P=f^{-1}F\) bounded constructible with perfect stalks. Factor in the other product order:

\[
 \begin{gathered}
 h_1=f\times\mathrm{id}_X:Y\times X\to X^2,
 \qquad h_2=\mathrm{id}_Y\times f:Y^2\to Y\times X,\\
 \gamma(y)=(y,f(y)),\quad
 A=P\boxtimes D_XF,\quad
 J_0=P\boxtimes(\omega_f\otimes f^{-1}D_XF).
 \end{gathered}
 \qquad\text{(16)}
\]

Use the graph parameter \((y,f(y);df_y^t\xi,-\xi)\) and diagonal parameter \((\eta,-\eta)\), agreeing with the positive-first convention of the Hom kernel. The corresponding normal differences are \(df(v_Y)-v_X\) on the graph and \(v_1-v_2\) on a diagonal. For \(h_1\), the second product variable is free, so the derivative onto the diagonal normal quotient is surjective; its normal map is the identity and its center map is \(f\). The [transverse ordinary microlocal comparison MIC14](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-transverse--the-transverse-ordinary-inverse-map) cancels the common relative center line with its prescribed graded extraction and gives

\[
 c_1:s^{-1}\mathsf M_X(F,F)\longrightarrow\mu_\gamma A.
 \qquad\text{(17)}
\]

The second change has center map the identity, normal derivative \(df\), and correspondence \(r\) followed by the identity. Its upper inverse comparison is

\[
 c_2:Rr_!\mu_\gamma A\longrightarrow\mu_{\Delta_Y}J_0.
 \qquad\text{(18)}
\]

The right coefficient in \(J_0\) is essential. Originally the ambient relative line is placed before \(h_2^{-1}A\); the canonical graded shuffle places it in the second external factor as in (16). For dimensions \(m,n\), it has shift \(m-n\). It is not removed from that factor.

Constructible biduality and the Hom estimate with constant target give
\(\operatorname{SS}(D_XF)=\operatorname{SS}(F)^a\).
Indeed ordinary coefficient dual has the indicated inclusion, and applying it again with actual biduality gives the reverse inclusion; tensoring with \(\omega_X\) changes no microsupport. Thus (3) also holds for \(D_XF\). The canonical noncharacteristic trace and exceptional internal-Hom comparison give the actual isomorphism

\[
 \theta_D:\omega_f\otimes f^{-1}D_XF
 \xrightarrow{\sim}f^!D_XF
 \xrightarrow{\sim}D_YP.
 \qquad\text{(19)}
\]

The first map is the [noncharacteristic trace comparison MO20](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-pullback--the-general-noncharacteristic-inverse-image), with the displayed graded order. The second is [EX.26](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom) applied to \(R\mathcal Hom(F,\omega_X)\): its evaluation and \(f^!\omega_X=\omega_Y\) give \(R\mathcal Hom(f^{-1}F,\omega_Y)=D_YP\). Both maps are therefore fixed by their actual contractions. They identify \(\mu_{\Delta_Y}J_0\) with \(\mathsf M_Y(P,P)\); write \(q=\mu(1\boxtimes\theta_D)c_2\).

For later use, the lower inverse comparison is an isomorphism

\[
 b_2:\mathsf M_Y(P,P)\xrightarrow{\sim}Rr_*\mu_\gamma A.
 \qquad\text{(20)}
\]

We check all three hypotheses of [LFI26–LFI27](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-inverse--microlocalization-commutes-with-inverse-image-under-three-tests). An ambient covector of \(A\) has components \((\alpha,\beta)\), with \(\beta\in\operatorname{SS}(D_XF)\) by the product estimate. Its transpose under \(h_2\) is \((\alpha,df^t\beta)\). If that transpose is zero, \(\alpha=0\) and (3), applied to the antipodal dual microsupport, forces \(\beta=0\).

The theorem's first condition also excludes unbounded covector sequences, including those whose ambient base points only approach the image of \(h_2\). If such a sequence had bounded transposes and covector norm tending to infinity, normalize by its total norm and pass to a unit-sphere subsequence in a relatively compact chart. The first normalized component tends to zero. Closedness of the product microsupport bound retains a nonzero limit \(\beta\in\operatorname{SS}(D_XF)\) at the limiting image point, and continuity gives \(df^t\beta=0\), a contradiction. Thus no escaping sequence of LFI14 exists; its additional weighted-mismatch condition is not even needed for this contradiction.

For the remaining two conditions, the center map is the identity of \(Y\). The conormal base map is consequently the identity, hence noncharacteristic for the entire normal-cone bound. Finally, if \((\alpha,df^t\beta)\) annihilates the diagonal tangent, then \(\alpha+df^t\beta=0\). This is exactly the condition that \((\alpha,\beta)\) annihilate the graph tangent. Thus the ambient-lift condition LFI15 holds for every covector. The [submersive-center proof](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-submersive-centers--a-simpler-test-on-the-centers) applies on the whole conormal bundle, including its zero section, and makes the actual upper and lower inverse comparisons isomorphisms. No constant derivative rank or properness of the base map has entered.

The support estimate \(\operatorname{supp}\mu_\gamma A\subset\operatorname{SS}(A)\cap T^*_{\Gamma_f}(Y\times X)\) and the product estimate also give

\[
 \operatorname{supp}\mu_\gamma A\subset B=s^{-1}\operatorname{SS}(F).
 \qquad\text{(21)}
\]

In fact the graph covector is \((df_y^t\xi,-\xi)\); its second component must lie in \(\operatorname{SS}(D_XF)\), so \(\xi\in\operatorname{SS}(F)\). Properness of \(r|_B\) therefore makes \(Rr_!\to Rr_*\) an isomorphism on this kernel. [The actual inverse trace square MIC13](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-inverse--pullback-has-two-comparison-directions) gives
\(b_2q=(Rr_!\to Rr_*)\), with the indicated maps. This is the inverse-diagram relative-duality cell.

## Ordinary restriction, evaluation and the inverse coefficient

The Cartesian identity \(h_1^{-1}k_{\Delta_X}=k_{\Gamma_f}\) gives the first restriction cell of (17). Ordinary pullback of the diagonal evaluation gives
\(t'_A:P\otimes f^{-1}D_XF\to f^{-1}\omega_X\).
Consequently, by naturality and the zero-normal center comparison,

\[
 \kappa_Ac_1=s^{-1}\kappa_F,
 \qquad \kappa_A:\mu_\gamma A\to Q.
 \qquad\text{(22)}
\]

The graph preimage under \(h_2\) can have additional branches. The next restriction is therefore the ordinary diagonal unit \(h_2^{-1}\gamma_*L\to\delta_{Y*}L\), with \(L=f^{-1}\omega_X\), rather than an equality of those two supported sheaves. The upper comparison on this center-supported object, followed by that restriction and \(\omega_f\otimes f^{-1}\omega_X\simeq\omega_Y\), defines a coefficient map \(\rho_f^+:Rr_!Q\to E_Y\) in the positive-first parameters used here.

To compare it with (2), let \(a_C(y;\xi)=(y;-\xi)\) and \(a_Y(y;\eta)=(y;-\eta)\). The inverse-cycle construction's graph and diagonal parameters become ours after these two antipodes, and \(ra_C=a_Yr\). Center-supported microlocalization identifies its coefficients with pullbacks from the center, so the parameter change acts identically on \(Q\) and \(E_Y\). Cartesian base change therefore identifies \(\rho_f^+\) with the conjugate \(a_Y^{-1}\rho_f\), using \(a_C^{-1}Q=Q\) on its source.

The difference between this identity action and the dualizing action determines the sign. Let \(\gamma_f:Q\to r^!E_Y\) be the inverse exceptional-composition map under \(Q\simeq\omega_p\) and \(E_Y\simeq\omega_{\pi_Y}\), and let \(\tau_f\) be its adjoint trace. The canonical fibre-antipode actions on these relative dualizing lines are \((-1)^n\) and \((-1)^m\): the [orientation action](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-smooth-sign--submersion-signs) is the sign of \(\det(-I)\) in the corresponding fibre dimension. Naturality of the trace therefore gives \((-1)^n\tau_f=(-1)^m\tau_f^+\).

This also determines the transformation of \(\rho_f\) without presupposing \(\beta_f=\gamma_f\). Both adjoints are isomorphisms from the same invertible complex \(Q\), so \(\gamma_f^{-1}\beta_f\) is multiplication by a locally constant unit on \(C\). Every vector fibre is connected and meets the zero section, so this unit is invariant under \(a_C\). Conjugating \(\rho_f\) thus has exactly the same sign as conjugating \(\tau_f\). Hence
\[
 \rho_f^+=(-1)^{m-n}\rho_f.
\]
This calculation uses only the two bundle ranks and remains valid when \(df\) changes rank. Already for \(\mathbb R\to\mathrm{pt}\), the target fibre antipode reverses the one-dimensional normal costalk of the zero embedding, so the two zero-supported traces have opposite signs. A positive transpose for \(r\) alone would not detect this coefficient difference.

It remains to check that evaluation after (19) is the same evaluation in this construction. Tensor (19) with \(P\). By its defining curry, contraction against \(P\) is the exceptional tensor comparison followed by \(f^!\) of the original dual-first evaluation. Precompose with the relative trace \(\omega_f\otimes f^{-1}D_XF\to f^!D_XF\). Naturality of that trace and projection identify this pairing with
\(\omega_f\otimes f^{-1}t_F\), followed by \(\omega_f\otimes f^{-1}\omega_X\to\omega_Y\), after the graded shuffle placing \(\omega_f\) before \(P\). The symmetry changing dual-first evaluation to \(t_P\) is the same symmetry as on this path. Tensor–Hom adjunction thus gives equality of these particular contractions, including the shift signs.

Apply the second upper inverse comparison to (22), its ordinary restriction arrow, and this evaluated identity. Naturality gives

\[
 \kappa_P q=(-1)^{m-n}\rho_f Rr_!\kappa_A.
 \qquad\text{(23)}
\]

Equations (17)–(23) retain every inverse-diagram row: transverse ordinary inverse comparison, its relative line, the exceptional-duality comparison, ordinary graph-to-diagonal restriction, evaluated contraction and the final coefficient map. The supported versions are unique on \(B\) and \(T=r(B)\); properness in (3) retains those supports during the use of \(Rr_!\).

## The inverse identity is checked by its exceptional adjoint

Pulling the kernel unit \(u_F\) through \(h_1\) gives
\(v:k_{\Gamma_f}\to A\).
The exceptional graph-Hom comparison identifies
\(\gamma^!A\simeq R\mathcal Hom(P,P)\).
The map \(v\) corresponds to \(\mathrm{id}_P\): pull the first-factor external-Hom kernel of \(u_F\) through \(h_1\), retain the second-factor exceptional projection, and use \(p_Y\gamma=\mathrm{id}_Y\). Its evaluation is ordinary inverse image of the identity of \(F\), hence the identity of \(P\). This checks the actual graph unit. The center-supported comparison in (17) sends \(1\) to \(1\), so \(e_A=\mu_\gamma v=c_1s^{-1}e_F\).

For an explicit exceptional-Hom identification, on \(Y\times X\) write \(q_X,q_Y\) for the two projections. The [external evaluation isomorphism](../../sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-external-hom--a-constructible-factor-in-a-product) gives \(A=R\mathcal Hom(q_X^{-1}F,q_Y^!P)\). Apply [exceptional inverse image of Hom](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom) and the identities \(q_Xh_2=fq_2\), \(q_Yh_2=q_1\). This gives \(h_2^!A=R\mathcal Hom(q_2^{-1}P,q_1^!P)\), which is the actual kernel \(P\boxtimes D_YP\). In external factors this is exactly \(P\boxtimes f^!D_XF\simeq P\boxtimes D_YP\), with the evaluation used in (19).

The diagonal unit \(u_P:k_{\Delta_Y}\to h_2^!A\) is the exceptional adjoint of \(v\). Indeed \(h_2\delta_Y=\gamma\), and the counit-normalized exceptional composition identifies both closed-adjunction morphism sets with \(\operatorname{Hom}(P,P)\). In both cases the element is \(\mathrm{id}_P\), so bijectivity of adjunction proves equality of the kernel maps.

Apply the specified exceptional identity [MIC15–MIC17](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-adjunctions--checking-the-actual-comparison-maps) to this pair of adjoint maps. The upper direct comparison on \(k_{\Delta_Y}\) is the zero-normal identity onto \(k_{\Gamma_f}\). The resulting equality is the adjunction transpose of

\[
 b_2e_P=Rr_*e_A\;\eta_r,
 \qquad \eta_r:k_{T^*Y}\to Rr_*k_C.
 \qquad\text{(24)}
\]

Explicitly, that identity inserts the \(r^{-1}\dashv Rr_*\) unit, the upper direct comparison and the exceptional counit. Moving the counit through the inserted unit cancels them by the triangular identity; the remaining map is \(\mu_\gamma v\). Taking its ordinary adjunction transpose gives (24). Thus the unit is established through actual kernel adjoints, rather than inferred from ordinary recovery.

Write \(\pi_A:Rr_!\mu_\gamma A\to Rr_*\mu_\gamma A\). It is invertible because this kernel is supported on \(B\), where \(r\) is proper. Since \(b_2\) is invertible and \(b_2q=\pi_A\), (24) gives the actual identity
\(e_P=q\,\pi_A^{-1}\,Rr_*e_A\,\eta_r\).
The constant term in \(\eta_r\) remains \(Rr_*k_C\); no properness of its full support and no inverse of its support-forgetting map is assumed.

Now \(e_A=c_1s^{-1}e_F\), and (22) identifies its evaluated graph class with the supported pullback of \(CC(F)\) to \(B\). Apply (23) to the displayed unit identity. Its middle inverse \(\pi_A^{-1}\) transfers ordinary sections to proper image only on that supported kernel; closed-support adjunction then maps the trace into \(R\Gamma_T E_Y\). This is exactly the supported inverse-cycle construction with coefficient \(\rho_f\), multiplied by the scalar in (23). Thus, with all supports retained, we obtain

\[
 \boxed{CC(f^{-1}F)=(-1)^{m-n}f^*CC(F)\quad
                    \text{if }f\text{ is noncharacteristic for }F.}
 \qquad\text{(25)}
\]

The inverse image \(P\) exists without this hypothesis. Formula (25) requires it because the cycle operation and the microlocal support-forgetting step require properness of \(r\) on \(B\).

## Globally constant finite coefficients fix conormal normalization

Let \(d=\dim Z\). For \(a_Z:Z\to\mathrm{pt}\), a finite complex \(V\) has point cycle \(\chi(V)\), with the graded supertrace normalization of the preceding lesson. Its pullback is noncharacteristic: the point has only its zero covector, and the incidence map is the closed zero embedding of \(Z\). The relative dimension in (25) is \(d\). Since the normalized zero cycle was defined using the inverse-cycle map \(a_Z^*\), we obtain

\[
 CC(a_Z^{-1}V)=(-1)^d\chi(V)[T_Z^*Z].
 \qquad\text{(26)}
\]

For a closed analytic submanifold \(i:Z\hookrightarrow X\), the map is proper. Formula (15) and the definition \([T_Z^*X]=i_![T_Z^*Z]\) yield

\[
 CC(i_*a_Z^{-1}V)=(-1)^d\chi(V)[T_Z^*X],
 \qquad CC(k_Z)=(-1)^d[T_Z^*X].
 \qquad\text{(27)}
\]

The brackets in (26)–(27) are the conormal cycles normalized by the preceding graph and closed-trace constructions. Their dimension factor records that normalization together with the positive-first Hom parameter; it is not a Jacobian sign or a failure of transversality. These are globally constant coefficient models. A local system with monodromy need not be a global pullback from a point. Its rank formula, and the coefficient calculation for a general localized constructible model, require local trivialization and microlocal invariance; the subsequent integrality and additivity argument will supply them. Equations (26)–(27) do not assume away monodromy or assert that every complex with locally constant cohomology globally splits.

## Exercises with complete solutions

### Nonproper ambient transport can cancel two finite point weights

*Difficulty: Intermediate.*

Let \(f(t)=\sin(\pi t)\) and \(G=i_{0*}k[2]\oplus i_{1*}k[1]\) on \(\mathbb R\). Verify the direct-image hypotheses, compute its image and cycle, and determine whether the opposite derivative signs give additional weights.

**Solution.** The ambient map is nonproper, with infinitely many points over zero, but its restriction to the closed support \(\{0,1\}\) is proper. The microsupport of each point summand is its full cotangent fibre. Since \(f'(0)=\pi\) and \(f'(1)=-\pi\), \(S'\) consists of two unrestricted \(\xi\)-lines and \(s\) maps each identically onto the target fibre at zero. The inverse image of a compact subset is a finite union of compact subsets, so the direct cycle map is defined.

Finite point image gives \(Rf_*G=Rf_!G=i_{0*}(k[2]\oplus k[1])\). The point supertrace is \(1-1=0\), so this is a nonzero complex with zero characteristic cycle. The normalized point trace on each source summand composes to the normalized target point trace. Each unshifted point coefficient therefore has weight \(+1\); the two cohomological shifts provide the displayed \(+1,-1\). The derivative signs do not supply another signed degree. Formula (15) carries their sum to zero with the full target fibre retained as a containing support.

### A ramified pullback exists where its cycle operation fails

*Difficulty: Intermediate.*

For \(f(t)=t^2\), compare \(F=k_{\{1\}}\) and \(F=k_{\{0\}}\). Compute the ordinary inverse objects, check (3), and state precisely where (25) applies.

**Solution.** Over one, the incidence has \(t=\pm1\) and arbitrary \(\xi\); \(r\) multiplies covectors by \(2\) and \(-2\) on the two components. Both restrictions are proper homeomorphisms onto the two target fibres. Ordinary inverse image is \(k_{\{-1\}}\oplus k_{\{1\}}\), whose cycle has coefficient \(+1\) on both fibres by point normalization. Transverse normalized conormal pullback gives the same cycle, so (25) applies.

Over zero, all \((0;\xi)\) are sent to \((0;0)\). A noncompact line lies over one target point; (3) fails. The ordinary inverse object still exists and is \(k_{\{0\}}\), with normalized full point-fibre cycle. The proposed set image of the source carrier is only its zero covector and cannot replace this cycle. The operation \(f^*CC(F)\) under (2) is undefined on that carrier, so (25) makes no assertion there. For \(t\mapsto t^3\), even a homeomorphism of the base fails the same derivative test at zero.

### A nonproper projection retains the dualizing shift

*Difficulty: Advanced.*

Let \(f:\mathbb R^2_{u,v}\to\mathbb R_x\) be \(f(u,v)=u\), and \(F=k_{\{0\}}[r]\). Compute the inverse cycle, the inverse object's Verdier dual and both cotangent properness tests.

**Solution.** The inverse object is \(P=k_{\{u=0\}}[r]\). The carrier \(B\) has \(u=0\), arbitrary \(v,\xi\), and \(r(0,v;\xi)=(0,v;\xi,0)\). This is a homeomorphism onto a closed conormal, so it is proper. It follows from (25), point normalization and transverse conormal normalization that \(CC(P)=(-1)^{r+1}[T^*_{\{u=0\}}\mathbb R^2]\): the point shift gives \((-1)^r\), and (25) contributes \((-1)^{2-1}\).

With coordinate orientations, \(\omega_f=k[1]\) and \(D_XF=k_{\{0\}}[-r]\). The right coefficient in (16) is therefore \(k_{\{u=0\}}[1-r]\), equal to \(D_YP\). Closed-submanifold duality gives this same result as the zero extension of the line's dualizing complex shifted by \([-r]\). Deleting \(\omega_f\) would lose one degree. The final dimension sign is the separate comparison of the two conormal parameters proved before (23); after applying (25), it must not be counted a second time. The dual coefficient and its graded evaluation still use the full map (19).

The other map is \(s(0,v;\xi)=(0;\xi)\), with an unbounded \(v\)-line over each point. It is not proper on this incidence. Thus this example verifies inverse transport for a nonproper base projection and separates it from the direct-image properness test.

### Changing tangential rank leaves a transverse conormal normalized

*Difficulty: Advanced.*

Take \(f(u,v)=(u^2,v)\), \(Z=\{z=0\}\subset\mathbb R^2_{x,z}\), and \(F=k_Z\). Calculate both sides of (25), including at \(u=0\). Identify the proper carrier map and the role of the vanishing tangential derivative.

**Solution.** Since \(\dim Z=1\), formula (27) gives \(CC(F)=-[T_Z^*\mathbb R^2]\). This conormal has \(z=0,\xi_x=0\), with arbitrary \(\zeta\). Pulling it back gives \(v=0,\xi_x=0\), and
\(r(u,0;0,\zeta)=(u,0;0,\zeta)\).
Its restriction is a homeomorphism onto \(T^*_{\{v=0\}}\mathbb R^2\), hence proper, even at \(u=0\). Ordinary inverse image is \(k_{\{v=0\}}\), so (27) gives its same normalized conormal cycle.

The tangential derivative \(2u\) changes rank and vanishes at zero, but no nonzero covector of the input conormal has a tangential component to be killed. The normal derivative is the identity. The normalized transverse-conormal theorem retains the zero-point unit in the tangent cotangent directions under this changing-rank linear map and the closed trace in the normal direction. The normalized conormal itself is transported with coefficient \(+1\). The characteristic cycle has coefficient \(-1\) on both sides, because both supporting submanifolds have dimension one; the source and target ambient dimensions are both two, so (25) contributes no further sign. A Jacobian sign or a constant-rank assumption would give an erroneous restriction on the theorem.

### A circle local system can have a nonzero cycle and a zero proper image

*Difficulty: Advanced.*

Let \(L\) be a rank-\(d>0\) local system on \(S^1\), with monodromy \(T\). Determine its cycle locally and globally, and its proper image's cycle under \(a:S^1\to\mathrm{pt}\). Treat the case where \(T-1\) is invertible without replacing \(L\) by a global constant system.

**Solution.** On each small contractible arc, \(L\) is actually isomorphic to \(k^d\). Formula (26) on that one-dimensional arc gives cycle \(-d\) times its normalized zero section. The construction restricts to open charts, and the degree-zero cycle coefficient is a sheaf; these local statements therefore give \(CC(L)=-d[T^*_{S^1}S^1]\). Since \(k\) has characteristic zero, \(-d\) is nonzero. No assertion of a global constant trivialization was needed.

Cut the circle at one point. The resulting two-arc gluing calculation computes ordinary global sections by \([k^d\xrightarrow{T-1}k^d]\) in degrees zero and one. Compact and ordinary sections agree because the circle is compact. Its Euler characteristic is zero, independently of the kernel and cokernel of \(T-1\), so the image has point cycle zero. Formula (15) gives \(a_!CC(L)=0\). If \(T-1\) is invertible, the image complex is zero as well, while the input cycle is nonzero. The closed containing image support can still be the point. This distinguishes local rank, global Euler index and actual support of the image.

### Finite output coefficients do not replace support properness

*Difficulty: Intermediate.*

Let \(a:(0,1)\to\mathrm{pt}\) and \(G=k_{(0,1)}\) on the source manifold. Compute its cycle, both direct-image cycles and the cotangent properness test. Then extend by zero into the ambient line.

**Solution.** The source has dimension one, so formula (26) gives \(CC(G)=-[T^*_{(0,1)}(0,1)]\). The incidence is \((0,1)\), \(r\) is its zero embedding, and \(s\) collapses it to the point. Thus \(s\) is nonproper on the entire pulled-back carrier. The closed support of \(G\) in its source manifold is the same noncompact interval.

Ordinary sections give \(Ra_*G=k\), with point cycle \(+1\). Compact sections give \(Ra_!G=k[-1]\), with point cycle \(-1\). Both outputs are bounded finite, but no direct cycle operation in (2) is defined on the input carrier. Formula (15) cannot identify either of them with such an undefined image. In particular, finite output coefficients do not justify inverting support forgetting.

For \(j:(0,1)\hookrightarrow\mathbb R\), the extension \(j_!G\) has compact closed support \([0,1]\), including its zero-stalk endpoints. Proper transport to a point now applies, and its resulting point cycle is \(-1\). The endpoint contributions to its ambient characteristic cycle are additional data; the later half-line calculation describes them. The source interval's zero-section cycle and the ambient extension's cycle belong to different cotangent spaces and have different support conditions.

## What remains after transport

Properness on closed support proves (15), and noncharacteristicity proves (25), with the actual unit, restriction, evaluation and coefficient maps of both graph diagrams. Equations (26)–(27) normalize globally constant finite models. The general local-system and generic conormal coefficient formulas, integral multiplicities, triangle additivity, antipodal duality and all half-line and Lorentz-cone formulas remain further teaching targets.

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§2.1–3.4, pp. 196–199, gives the twisted conormal orientation and local Euler-multiplicity description of characteristic cycles. These are the historical and mathematical framework, rather than a replacement for the graph comparison proof. The coefficient maps, supported units, and conversion between conormal parameters used here are specified in the programme proofs linked at their use.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4–4.6.8, §4.7 and Proposition 5.1.9, pp. 95–97 and 107–108, gives the exceptional and relative-dualizing framework. The proper-image argument above checks both the image identity and its contraction, imposing properness only on the actual support. The inverse argument keeps its relative line and follows the ordinary graph restriction and unit through the microlocal adjunction. Its examples test the coefficient and properness requirements separately. The human texts retain their authorship and their own terms.
