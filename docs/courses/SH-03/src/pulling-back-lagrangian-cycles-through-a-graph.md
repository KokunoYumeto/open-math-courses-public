# Pulling back Lagrangian cycles through a graph

A cotangent inverse image needs a map between dualizing coefficients, as well as an image of its carrier. The map comes from comparing a graph with a diagonal. Its adjoint is an isomorphism even when the derivative changes rank. Properness is a separate condition on the carrier to which the operation is applied.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The construction has three distinct steps. A graph identifies the positive cotangent transpose. A restriction to the diagonal constructs its coefficient arrow, and an adjunction proves that arrow's exceptional mate invertible. Only then do we impose properness on a cycle carrier and transport its supported class. This order separates the geometry of the allowed support from the normalization of its coefficient.

Use [Lagrangian cycles and proper cotangent images](lagrangian-cycles-and-proper-cotangent-images.md#the-orientation-coefficient-fixes-the-dimension) for \(\mathcal L_X\) and \(E_X=\pi_X^{-1}\omega_X\). The geometric input is [isotropic inverse transport](../../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#isotropic-inverse-transport). The coefficient proof uses the [center-supported specialization calculation](../../sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-zero--what-survives-when-the-direction-is-forgotten), the [direct microlocal comparison](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit), the [inverse comparison](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-inverse--pullback-has-two-comparison-directions), and their [actual unit-and-counit identities](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-adjunctions--checking-the-actual-comparison-maps). The applications below specify both the maps and every support hypothesis.

M. Kashiwara's [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§2.1–2.3, pp. 196–197, supplies the twisted conormal and Lagrangian-chain framework. The graph coefficient arrow below is derived from the linked microlocal comparison maps, with its adjunction and orientation normalization proved explicitly. We retain a general commutative coefficient ring \(A\) of finite global dimension. Manifolds are real analytic, Hausdorff and countable at infinity, with uniformly bounded finite dimensions.

## The two cotangent properness conditions are different

Let \(f:Y\to X\), with \(\dim Y=m\), \(\dim X=n\). Its cotangent correspondence is

\[
 \begin{gathered}
 C_f=Y\times_XT^*X,\qquad \pi:C_f\to Y,\\
 f_\pi(y;\xi)=(f(y);\xi),\qquad
 f_d(y;\xi)=(y;df_y^t\xi).
 \end{gathered}
 \qquad\text{(1)}
\]

For a closed conic subanalytic isotropic \(\Lambda_X\subset T^*X\), inverse image assumes

\[
 f_d\text{ proper on }B_f=f_\pi^{-1}\Lambda_X.
 \qquad\text{(2)}
\]

Its carrier is \(\Lambda_Y'=f_d(B_f)\). Here is how each property enters. The correspondence maps commute with positive dilation, so the image is conic. Properness on the closed subanalytic \(B_f\) gives a closed subanalytic image. For isotropy, the canonical one-forms satisfy \(f_d^*\alpha_Y=f_\pi^*\alpha_X\): on a tangent vector based at \(y\), both evaluate as \(\xi(df_yv)\). The pullback to a smooth test of \(B_f\) therefore vanishes. The [surjective form-detection proof](../../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#surjective-form-detection) descends this vanishing to the subanalytic image; the [inverse-transport proof](../../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#isotropic-inverse-transport) supplies the subanalytic image construction without a constant-rank assumption. Thus \(\Lambda_Y'\) is an allowed isotropic carrier, including any zero covectors. Direct image instead assumes \(f_\pi\) proper on \(f_d^{-1}\Lambda_Y\). The domains and maps in those two tests cannot be exchanged.

Here is a useful complete test for (2). For a closed positive-conic \(\Lambda_X\),

\[
 f_d|_{B_f}\text{ is proper}
 \quad\Longleftrightarrow\quad
 \bigl((f(y);\xi)\in\Lambda_X, df_y^t\xi=0\bigr)
                   \Longrightarrow\xi=0.
 \qquad\text{(3)}
\]

This is the noncharacteristic condition for this closed carrier, with zero covectors retained.

**Proof.** A nonzero killed covector gives the unbounded ray
\((y;t\xi)\), \(t>0\), in the inverse image of the single target point \((y;0)\). That fibre is not compact, so properness fails.

Conversely fix a compact set of base points \(K\subset Y\), and choose continuous bundle norms near \(K\) and \(f(K)\). There is a constant \(c_K>0\) such that

\[
 \|df_y^t\xi\|\geq c_K\|\xi\|
 \quad(y\in K,\ (f(y);\xi)\in\Lambda_X).
 \qquad\text{(4)}
\]

If not, normalize offending covectors to length one. The unit sphere bundle over the compact \(f(K)\), together with \(y\in K\), is compact. A subsequence converges to \((y;\xi)\) with \(\|\xi\|=1\), still in the closed pulled-back carrier, and with \(df_y^t\xi=0\). This contradicts the right side of (3). If there are no nonzero covectors over these points, (4) holds vacuously.

For a compact \(Q\subset T^*Y\), its base projection is such a \(K\), and its covector norms are bounded. Inequality (4) bounds every \(\xi\) in \((f_d|_{B_f})^{-1}Q\). A bounded disk bundle over compact \(K\) is compact. The inverse image is closed in it, by closedness of \(\Lambda_X,Q\) and continuity of the maps. It is therefore compact. \(\square\)

Neither constant rank of \(df\) nor properness of the base map \(f\) was used. The quantitative bound is uniform on compact base sets; it is not a global positive lower bound over a noncompact \(Y\).

## A graph turns the transpose derivative into a conormal map

Set

\[
 \begin{gathered}
 Z=Y\times Y,\qquad W=Y\times X,\qquad
 F_1=\operatorname{id}_Y\times f:Z\to W,\\
 \delta_Y(y)=(y,y),\qquad \delta_f(y)=(y,f(y)),\\
 N=\Delta_Y\subset Z,\qquad M=\Gamma_f\subset W.
 \end{gathered}
 \qquad\text{(5)}
\]

Both embeddings are closed. The restriction \(N\to M\) is the identity on their shared parameter \(Y\). Thus the center map is a diffeomorphism, even if the ambient map \(F_1\) is singular.

Identify the graph and diagonal conormals by

\[
 \begin{aligned}
 C_f&\simeq T^*_MW,
 &(y;\xi)&\longmapsto(y,f(y);-df_y^t\xi,\xi),\\
 T^*Y&\simeq T^*_NZ,
 &(y;\eta)&\longmapsto(y,y;-\eta,\eta).
 \end{aligned}
 \qquad\text{(6)}
\]

The transpose of \(dF_1\) takes the first covector to
\((-df_y^t\xi,df_y^t\xi)\). Hence the conormal transpose map is precisely \(r=f_d\), while the conormal base-change map \(s\) is the identity on \(C_f\). The minus signs in (6) express annihilation of graph tangents; they do not insert an antipode into \(f_d\).

On normal vectors use the differences \(v_2-v_1\) for the diagonal and \(v_X-df(v_Y)\) for the graph. The induced normal map is \(v\mapsto df(v)\). Its relative invertible line is

\[
 P=\omega_{Y/X}=\omega_Y\otimes(f^{-1}\omega_X)^{-1},
 \qquad L=\pi^{-1}P,
 \qquad\omega_r=L^{-1}.
 \qquad\text{(7)}
\]

The shift of \(P\) is \(m-n\). To determine its map, use exceptional transitivity \(f^!\omega_X\simeq\omega_Y\) and the invertible-line comparison \(\omega_f\otimes f^{-1}\omega_X\simeq f^!\omega_X\). There is a unique identification \(\omega_f\simeq P\) whose tensor product on the right with \(f^{-1}\omega_X\), followed by evaluation of the adjacent inverse pair, is this transitivity map. This is the [ordered relative-dualizing construction](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-relative--relative-dimensions-graph-supports-and-coordinate-changes), not a choice of a local orientation generator.

For the normal map, the bundles are \(TY\) and \(f^{-1}TX\) over the same \(Y\), so the base orientation factors cancel. Their normal dualizing ratio is \(P\). The transpose goes from the dual of the second bundle to the dual of the first; the ratio and the rank difference are both reversed. Positive dual orientation and the [right-tensor extraction in FF3a](../../sheaf-proof-readings/src/SH02/fourier-functoriality.md#sh02-ff-conventions-the-inverse-transform-and-orientation-lines) therefore give \(\omega_r=L^{-1}\), as a specified map of shifted lines. All later permutations use the graded symmetry. In particular exchanging shifts \([a]\) and \([b]\) contributes \((-1)^{ab}\); replacing an inverse shifted line by its unshifted sign local system would change the construction. This calculation uses the ranks of the two bundles, never the rank of \(df\).

## Construct the coefficient arrow before using a carrier

Put \(K=f^{-1}\omega_X\) on \(Y\), and \(\mathscr F=\delta_{f*}K\) on \(W\). Microlocalization of a coefficient supported on its smooth center has the actual natural identification

\[
 \mu_M\mathscr F\simeq\pi^{-1}K.
 \qquad\text{(8)}
\]

Here is a map-level calculation of (8). For any closed smooth center \(i:M\hookrightarrow W\) and \(K\in D^b(A_M)\), let \(e\) be the zero section of its normal bundle. The [center-supported calculation](../../sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-zero--what-survives-when-the-direction-is-forgotten) identifies the positive-time deformation term with the closed-axis image of \(K\boxtimes A_{(0,\infty)}[1]\). At time zero the open half-line has costalk \(A[-1]\). Its connecting morphism, fixed by restriction from the closed half-line to its endpoint, cancels the time-orientation \([1]\) and gives the identity on \(K\). Thus the actual specialization is \(e_*K\), with its prescribed counit. Fourier transformation now restricts its pairing kernel to zero normal vector, where the closed halfspace condition is automatic. Projection of this support to the dual bundle is the identity, so its proper direct image is the pulled-back \(K\), with no integration shift. This proves (8) naturally for bounded coefficients; it applies again to the diagonal.

Apply the upper ordinary-inverse comparison [MIC13](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-inverse--pullback-has-two-comparison-directions) to the pair map \(F_1:(Z,N)\to(W,M)\). In its correspondence, \(r=f_d\), \(s=\operatorname{id}_{C_f}\), and the center map is the identity, whose relative line is the unit. Hence MIC13, with the identification (8), gives

\[
 Rf_{d!}\pi^{-1}K
    \longrightarrow
 \mu_N(\omega_{F_1}\otimes F_1^{-1}\mathscr F).
 \qquad\text{(9)}
\]

The second arrow is restriction to the diagonal. More precisely the unit of \(\delta_Y^{-1}\dashv\delta_{Y*}\) gives
\(F_1^{-1}\mathscr F\to\delta_{Y*}\delta_Y^{-1}F_1^{-1}\mathscr F
=\delta_{Y*}K\).
Indeed \(F_1\delta_Y=\delta_f\) and \(\delta_f^{-1}\delta_{f*}K=K\), so this target identification does not require \(F_1^{-1}M=N\). Restricting the ambient relative-dualizing comparison to \(N\) cancels its common \(Y\) factor and gives \(\delta_Y^{-1}\omega_{F_1}=P\). The closed-embedding projection formula, followed by the actual evaluation \((\omega_Y\otimes K^{-1})\otimes K\to\omega_Y\) fixed in (7), now gives

\[
 \omega_{F_1}\otimes F_1^{-1}\mathscr F
       \longrightarrow\delta_{Y*}(P\otimes K)
       \simeq\delta_{Y*}\omega_Y.
 \qquad\text{(10)}
\]

Apply \(\mu_N\) and the center-supported formula (8) for the diagonal. The composite is the coefficient map

\[
 \rho_f:Rf_{d!}\pi^{-1}f^{-1}\omega_X
                   \longrightarrow\pi_Y^{-1}\omega_Y=E_Y.
 \qquad\text{(11)}
\]

The restriction in (10) is an arrow. The preimage of the graph under \(F_1\) can be larger than the diagonal, so there is no general ordinary inverse-image equality of their supported sheaves. Exercise 1 exhibits this issue at a critical point.

Formula (11) is constructed for every analytic \(f\), before any properness assumption on a cycle carrier. The analytic hypotheses provide finite-dimensional bounded operations; \(P,K\) are bounded invertible orientation complexes. The map is the specified microlocal comparison followed by the specified restriction and relative dualizing pairing.

## The actual adjoint is an isomorphism

Let

\[
 \beta_f:\pi^{-1}f^{-1}\omega_X
                       \longrightarrow f_d^!E_Y
 \qquad\text{(12)}
\]

be the \(Rf_{d!}\dashv f_d^!\) adjoint of (11). We prove that this particular arrow is an isomorphism.

Take \(\mathscr G=\delta_{Y*}K\) on \(Z\). Its support lies on \(N\), and
\(RF_{1*}\mathscr G=\delta_{f*}K=\mathscr F\).
The ordinary direct microlocal comparison is

\[
 d_{\mathscr G}:\mu_M(RF_{1*}\mathscr G)
       \longrightarrow r^!(\mu_N\mathscr G)\otimes L.
 \qquad\text{(13)}
\]

This is the lower ordinary-direct arrow of [MIC12](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit). Its isomorphism assertion follows from all three supported hypotheses, which can be checked here without a clean-preimage assumption. First, \(F_1\) restricted to the closed support of \(\mathscr G\) factors through the closed graph embedding of \(Y\) in \(W\), so it is proper there. Second, a normal-coordinate sequence in a subset of \(N\) has identically zero normal component; its normal cone is consequently contained in the zero section over that closed support. The induced normal map takes this section to the graph's zero section by the identity on \(Y\), so its restriction is a closed embedding and is proper. Third, \(\operatorname{supp}\mathscr G\cap F_1^{-1}M\subset N\) because the whole support already lies in \(N\). These are exactly the three conditions of MIC12, and hence its specialization square and its Fourier transform are isomorphisms. None of these arguments assumes that \(df\) is injective, surjective, or of locally constant rank.

To identify (13) with (12), retain the adjunction maps. In the conormal correspondence put

\[
 \mathcal D(H)=Rr_!(L^{-1}\otimes H),\qquad
 \mathcal C(J)=r^!J\otimes L.
 \qquad\text{(14)}
\]

They are adjoint: first transpose across \(Rr_!\dashv r^!\), then across tensoring by the invertible \(L^{-1}\). This second transposition uses its tensor–Hom unit and counit and the indicated order of the factors. The exact identity [MIC16](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-adjunctions--checking-the-actual-comparison-maps) says that (13) is

\[
 \mu_M\mathscr F
 \xrightarrow{\eta_{\mathcal D}}
 \mathcal C\mathcal D\mu_M\mathscr F
 \xrightarrow{\mathcal C\widetilde c_{\mathscr F}}
 \mathcal C\mu_NF_1^{-1}\mathscr F
 \xrightarrow{\mathcal C\mu_N\varepsilon'}
 \mathcal C\mu_N\mathscr G.
 \qquad\text{(15)}
\]

Here \(\widetilde c\) is the upper inverse comparison after the right-ordered orientation cancellation, and \(\varepsilon':F_1^{-1}RF_{1*}\mathscr G\to\mathscr G\) is the counit of \(F_1^{-1}\dashv RF_{1*}\). This counit agrees with the embedding unit used in (10), although the two adjunctions are different. To check equality, a map into \(\delta_{Y*}K\) is determined by its adjoint after \(\delta_Y^{-1}\). The restriction of the embedding unit is the identity of \(K\). The restriction of \(\varepsilon'\) is also the identity: identify \(RF_{1*}\delta_{Y*}K=\delta_{f*}K\) by composition, and use \(F_1\delta_Y=\delta_f\) and the two fully faithful closed-embedding adjunctions. Their triangular identities make the resulting \(K\to K\) the identity. Thus the two maps, not merely their target sheaves, coincide.

Now \(\mu_N\mathscr G=\pi_Y^{-1}K\). The right-tensor extraction of the relative line identifies

\[
 r^!(\pi_Y^{-1}K)\otimes L
     \simeq r^!(\pi_Y^{-1}(K\otimes P))
     \simeq r^!E_Y.
 \qquad\text{(16)}
\]

The first arrow is the [exceptional tensor comparison](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-tensor--the-normalized-tensor-comparison), which is invertible for the bounded invertible base line \(P\); indeed \(r^{-1}\pi_Y^{-1}P=L\). The second uses the graded symmetry from \(K\otimes P\) to \(P\otimes K\), followed by the pairing in (10). Denote this composite by \(q_K:\mathcal C(\pi_Y^{-1}K)\to r^!E_Y\).

To check the map, put \(H=\mu_M\mathscr F\) and \(\kappa=\mu_N\varepsilon'\circ\widetilde c_{\mathscr F}\). Formula (15) is exactly \(\mathcal C(\kappa)\circ\eta_{\mathcal D,H}\). Its \(\mathcal D\dashv\mathcal C\) transpose is \(\kappa\): the counit followed by the inserted unit cancels by the triangular identity. Now transpose \(q_K\circ d_{\mathscr G}\) across \(Rr_!\dashv r^!\). The exceptional tensor comparison is defined as the mate of the proper-image projection formula and the counit; it therefore moves the final \(L\) through this transposition by that projection formula. Evaluation of its adjacent inverse factor converts \(\widetilde c_{\mathscr F}\) back to the upper comparison (9). Its remaining factor is precisely the graded permutation \(K\otimes P\to P\otimes K\) in \(q_K\), followed by the pairing (10). Finally \(\varepsilon'\) is the restriction arrow just checked. The resulting transpose is consequently \(\rho_f\), not an unspecified scalar multiple of it.

This computation uses the [specified third and fourth Fourier exchanges](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-exchange--four-fourier-identities-for-the-correspondence): the third is obtained by right-ordered tensor–Hom transposition, and the fourth is its actual right mate. Their units, counits and graded permutations are the ones in MIC16. An unsigned interchange of shifted lines would not satisfy this calculation in general. We have proved \(q_K\circ d_{\mathscr G}=\beta_f\) by equality of their adjoints.

Thus \(\beta_f\) is (13) under the actual identifications (8),(16). Since (13) is an isomorphism, so is (12). This proof allows changing rank and nonproper \(f\). It does not assert that \(\rho_f\) itself is an isomorphism: an adjunction counit can fail to be one when its adjoint is invertible.

## Supported inverse images and fundamental cycles

Under (2), the operation on a cycle is the composite

\[
 \begin{aligned}
 H^0_{\Lambda_X}(T^*X;E_X)
 &\longrightarrow H^0_{B_f}(C_f;\pi^{-1}f^{-1}\omega_X)\\
 &\longrightarrow
 H^0_{\Lambda_Y'}(T^*Y;Rf_{d!}\pi^{-1}f^{-1}\omega_X)\\
 &\xrightarrow{\rho_f}
 H^0_{\Lambda_Y'}(T^*Y;E_Y).
 \end{aligned}
 \qquad\text{(17)}
\]

Here are the support maps in (17). Write \(r=f_d\), \(H=\pi^{-1}f^{-1}\omega_X=f_\pi^{-1}E_X\), and \(S=\Lambda_Y'\). Pullback of the support-forgetting map gives
\(f_\pi^{-1}R\Gamma_{\Lambda_X}E_X\to H\). Its source is supported on \(B_f\), so closed-support adjunction factors it canonically through \(J=R\Gamma_{B_f}H\). The ordinary inverse-image unit on global sections and this factorization give the first arrow. No properness of \(f_\pi\) is involved.

The natural comparison \(Rr_!J\to Rr_*J\) is an isomorphism because \(r\) is proper on the closed support \(B_f\). Its inverse gives an actual route
\(R\Gamma(C_f;J)=R\Gamma(T^*Y;Rr_*J)\to R\Gamma(T^*Y;Rr_!J)\).
The object \(Rr_!J\) is supported on \(S\), and the image of \(J\to H\) factors canonically as \(Rr_!J\to R\Gamma_S(Rr_!H)\). Taking degree zero gives the second arrow in (17). Thus we invert the proper/ordinary comparison only on \(J\), never on the unrestricted coefficient \(H\). The last arrow is \(R\Gamma_S\) applied to the actual \(\rho_f\). These are the closed-support adjunction and counit maps of the [exceptional-operations construction](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions), with proper-support functoriality as in the [direct cycle construction](lagrangian-cycles-and-proper-cotangent-images.md#a-direct-image-has-a-cotangent-incidence-domain).

The output carrier is allowed in \(\mathcal L_Y\), so (17) defines \(f^*\). For the identity map, \(F_1\), its normal map, the graph restriction and the relative pairing are all identities; hence so is \(\rho_f\), and (17) is the identity on supported classes. If a carrier is enlarged while (2) remains valid, the natural maps between its closed-support functors commute with pullback, the proper/ordinary comparison and \(\rho_f\). The resulting cycles therefore agree under the support-enlargement map. These facts ensure that (17) is an operation on the cycle sheaf, rather than on a particular presentation of a cycle.

For a point, \(\mathcal L_{\mathrm{pt}}=A\) and its fundamental cycle \([\mathrm{pt}]\) is \(1\). For \(a_X:X\to\mathrm{pt}\), the incidence is \(X\) and its map to \(T^*X\) is the closed zero embedding \(z_X\). It is proper even when \(X\) is noncompact. Define

\[
 [T_X^*X]=a_X^*[\mathrm{pt}].
 \qquad\text{(18)}
\]

It is a generator of the twisted zero-section cycle coefficient. In this case the first map of (17) pulls \(1\) back to \(1\in H^0(X;A_X)\). Closed-support adjunction for \(z_X\) then identifies its last two maps with the actual isomorphism \(A_X\xrightarrow{\beta_{a_X}}z_X^!E_X\). Thus (18) is the image of \(1\) under this specified isomorphism, not an independently chosen Thom class.

To identify its coefficient, the [relative cotangent orientation](lagrangian-cycles-and-proper-cotangent-images.md#the-orientation-coefficient-fixes-the-dimension) restricts to \(B_X|_X=\operatorname{or}_{T^*X/X}|_X\simeq\operatorname{or}_X\), with positive dual orientation. The smooth-cycle coefficient is \(\operatorname{or}_X\otimes B_X|_X\). The integral orientation square pairs this with the constant rank-one line: each reversal changes both factors by \(-1\). Hence the image of \(1\) is a local generator and agrees on overlaps without a global base orientation. The coefficient isomorphism, including its sign relative to an ordered chart, is the one fixed by \(\beta_{a_X}\); the square-line description does not introduce an additional normalization.

If \(i:Y\hookrightarrow X\) is a closed analytic submanifold, \(i_\pi\) is a closed embedding, and
\(i_d^{-1}(T_Y^*Y)=T_Y^*X\) in its incidence. The direct operation is therefore defined. Set

\[
 [T_Y^*X]=i_*[T_Y^*Y].
 \qquad\text{(19)}
\]

This defines the normalized conormal cycle with its relative cotangent orientation coefficient. To prove that it is a generator with the stated normalization, retain the direct-image coefficient map. In the Cartesian square with horizontal maps \(i_\pi:C_i\to T^*X\) and \(i:Y\to X\), and vertical maps \(\pi\) and \(\pi_X\), it is
\(Ri_{\pi!}\pi^{-1}\omega_Y\simeq\pi_X^{-1}Ri_!\omega_Y\to\pi_X^{-1}\omega_X\).
The first arrow is proper-support base change; the second is the pulled-back trace of \(i\). Its \(Ri_{\pi!}\dashv i_\pi^!\) mate is the exceptional base-change map
\(\pi^{-1}\omega_Y=\pi^{-1}i^!\omega_X\to i_\pi^!\pi_X^{-1}\omega_X\).
This map is an isomorphism, as can be checked with its defining trace in a product chart. There \(\pi_X\) is projection of a free cotangent coordinate factor, while \(i_\pi\) and \(i\) both impose the same equation \(z=0\) in the base coordinates. The [closed-embedding costalk calculation](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-closed--the-closed-embedding-comparison) computes both exceptional restrictions by the same normal \(z\)-orientation line shifted by minus its codimension. In [EX.18](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-basechange--two-exceptional-base-change-comparisons), proper-support base change pulls back the same sections, and the subsequent trace evaluates the same normal generator; the additional cotangent coordinate factor is unchanged. Thus this particular base-change map is the identity on that normal costalk calculation. Cancellation against the normal factor of \(\omega_X\) makes it an isomorphism. This local trace calculation also proves the smooth base-change instance used here without substituting an arbitrary isomorphism between its two objects.

More explicitly, choose coordinates \((u,z)\) with \(Y=\{z=0\}\), and dual coordinates \((\xi_u,\zeta)\). The conormal carrier is \(z=0,\xi_u=0\), with free coordinates \((u;\zeta)\). Pullback under \(i_d(u;\xi_u,\zeta)=(u;\xi_u)\) leaves the zero-section Thom class in the \(\xi_u\) directions and adds the free \(\zeta\) coordinates. The subsequent supported trace for \(i_\pi\) is adjoint to the isomorphism above; in the \(z\) directions it pairs the normal costalk generator with its dualizing factor. A generator therefore maps to a generator, with the ordered evaluation sign fixed by that counit. This assertion can also be read directly as an isomorphism of the rank-one supported coefficient sheaves before taking sections. Since both base change and trace are natural under restriction of charts, these generators agree with the definition (19) on all overlaps, including orientation-reversing ones. No separate choice of a sign for the conormal cycle remains.

The formula for transverse inverse images of these normalized conormal cycles needs its own comparison of the two constructions. We have not inferred that formula merely from equality of their carrier sets.

## Exercises with complete solutions

### A graph preimage can contain an extra branch

*Difficulty: Advanced.*

Take \(f:\mathbb R_t\to\mathbb R_x\), \(f(t)=t^2\). Compute (6) and the preimage of \(\Gamma_f\) under \(F_1(s,t)=(s,t^2)\). Explain why (10) must be a restriction arrow.

**Solution.** A graph covector at \((s,s^2)\) is
\((-2s\xi,\xi)\). At a point of the diagonal, the transpose of \(dF_1\) gives \((-2s\xi,2s\xi)\), so the diagonal coordinate is \(\eta=2s\xi\). This is the positive transpose \(f_d\), with no additional sign.

The preimage condition is \(t^2=s^2\). It contains both \(t=s\) and \(t=-s\), crossing at the origin. Near a point of the antidiagonal away from zero, the ordinary inverse image of a nonzero coefficient supported on \(\Gamma_f\) is nonzero while a coefficient supported on \(\Delta_Y\) has zero stalk. Thus these two sheaves are not equal. The ordinary embedding unit restricts the preimage sheaf to the diagonal and discards that other branch. At the origin the branches meet, but the same natural restriction still exists. The microlocal construction uses that arrow and does not require the ambient map to be noncharacteristic for the graph sheaf.

### Properness is a compact uniform estimate

*Difficulty: Intermediate.*

Explain every compactness step in (3)–(4). Then give a map for which a uniform positive bound exists on every compact base set but no global positive bound exists, while cotangent inverse image is still proper.

**Solution.** Closedness of \(\Lambda_X\) retains the limit of normalized covectors. Positive conicity permits normalization. The base coordinates lie in compact \(K\); the covectors lie in the unit sphere over compact \(f(K)\). Hence a subsequence converges jointly. The assumed failure of (4) would kill a nonzero limit covector. For a compact target \(Q\), its base projection is compact and its fibre norms are bounded; (4) then puts the preimage in a compact disk bundle. Its closedness makes it compact, which is exactly properness.

Take \(f(t)=\arctan t\) and \(\Lambda_X=T^*\mathbb R\). The derivative is \(1/(1+t^2)>0\), so
\(f_d(t;\xi)=(t;\xi/(1+t^2))\) is a homeomorphism from the incidence to \(T^*\mathbb R_t\), with inverse \((t;\eta)\mapsto(t;(1+t^2)\eta)\). It is proper. On \([-R,R]\), (4) holds with \(c_K=1/(1+R^2)\), whereas these constants approach zero as \(R\to\infty\). The full cotangent carrier here is used only to test properness; it is not isotropic and is not declared an allowed Lagrangian carrier.

### The critical fibre of a ramified map fails the test

*Difficulty: Intermediate.*

For \(f(t)=t^2\), compare inverse image of the full cotangent fibre over \(x=0\) with that over \(x=1\). Compute the image carriers and verify or disprove properness directly.

**Solution.** Over zero, \(B_f=\{t=0,\xi\in\mathbb R\}\), and
\(f_d(0;\xi)=(0;0)\). A whole noncompact line maps to one point. The inverse cycle operation on this carrier is undefined by (2), although its set image is a single zero covector.

Over one, \(B_f\) has two components \(t=1\) and \(t=-1\), with unrestricted \(\xi\). On them the covector maps are \(\xi\mapsto2\xi\) and \(\xi\mapsto-2\xi\). Each is a homeomorphism onto the cotangent fibre at its base point. A compact target has compact inverse image in each of these two components, and a finite union of compact sets is compact. The map is proper, with image the two full cotangent fibres. They are closed conic isotropic carriers of dimension one. This calculation verifies the operation's domain and carrier; it does not substitute a set calculation for its coefficient map.

### A nonproper base projection has a proper cotangent inverse image

*Difficulty: Advanced.*

Let \(f:\mathbb R^2_{u,v}\to\mathbb R_x\), \(f(u,v)=u\), and let \(\Lambda_X=T^*_{\{0\}}\mathbb R\). Compute (2) and its dimension shifts. Compare the map \(f_\pi\) on this same incidence subset.

**Solution.** The pulled-back carrier is
\(B_f=\{u=0,v\in\mathbb R,\xi\in\mathbb R\}\), and
\(f_d(0,v;\xi)=(0,v;\xi,0)\). It is a homeomorphism onto the closed conormal of \(\{u=0\}\subset\mathbb R^2\), hence proper as a map to \(T^*\mathbb R^2\). Compact inverse images are compact even though the \(v\) coordinate is globally unbounded. The base map is nonproper, but the inverse cycle operation is defined.

Here \(m=2,n=1\), so \(P\) has shift \([1]\), \(L^{-1}\) has shift \([-1]\), and \(f_d\) is the codimension-one horizontal embedding of the full incidence. \(E_Y\) is locally in degree \(-2\); its exceptional inverse image along that embedding is locally in degree \(-1\), agreeing with \(\pi^{-1}f^{-1}\omega_X\). Ordinary restriction would keep degree \(-2\) and miss (12).

The other map is \(f_\pi(0,v;\xi)=(0;\xi)\). It forgets \(v\) and has a whole noncompact line over each target covector. It is not proper on this subset. This demonstrates the difference between the two cotangent properness tests using the actual maps.

### Tangential and normal covectors give different embedding tests

*Difficulty: Intermediate.*

Let \(i:\mathbb R_u\hookrightarrow\mathbb R^2_{x,z}\), \(i(u)=(u,0)\). Test inverse-image properness for the zero section, the conormal of the vertical line \(\{x=0\}\), and the conormal of the horizontal line \(\{z=0\}\).

**Solution.** A correspondence covector is \((u;\xi\,dx+\zeta\,dz)\), and
\(i_d(u;\xi,\zeta)=(u;\xi)\).
For the zero section, \(\xi=\zeta=0\); the restriction identifies its pulled-back carrier with the zero section of \(T^*\mathbb R\) and is proper.

The vertical line's conormal has \(x=0\), \(\zeta=0\), and arbitrary \(\xi\). Its pulled-back carrier has \(u=0,\zeta=0\); the remaining \(\xi\) maps identically to the cotangent fibre at zero. Properness holds. The embedding is transverse to that vertical line.

The horizontal line's conormal has arbitrary \(x\), \(\xi=0\), and arbitrary \(\zeta\). Its pulled-back carrier has arbitrary \(u,\zeta\) and maps to \((u;0)\). Each fixed \(u\) has a noncompact \(\zeta\)-fibre, so properness fails. This is exactly a nonzero normal covector killed by restriction to the tangent line. These conclusions distinguish properness and carriers; the normalized transverse conormal equality is a further comparison theorem.

### Point weights and the normalized zero section

*Difficulty: Intermediate.*

Take a map from a two-point zero-dimensional manifold to a point. Compute pullback and direct image of point weights over \(A=\mathbb Z\). Then explain why (18) remains a generator for a nonorientable positive-dimensional \(X\), and why (19) is defined for a closed point embedding.

**Solution.** In dimension zero, all cotangent fibres have rank zero and every dualizing coefficient is \(A\) in degree zero. The graph and diagonal conormal maps are identity maps on their point components, and the point counit is the identity. Pullback sends \(a\) to \((a,a)\); proper direct image sums weights. Thus pulling back \(1\) and then pushing it forward gives \(2\in\mathbb Z\). This records the two sheets. No orientation permutation or nonzero cohomological degree occurs, and the ring has finite global dimension one.

For general \(X\), the zero embedding is proper and the actual map
\(A_X\xrightarrow{\beta_{a_X}}z_X^!E_X\) is an isomorphism. The image of \(1\) gives (18), a generator on every connected local zero-section piece. Its coefficient is \(\operatorname{or}_X\otimes B_X|_X\), so the two orientation signs cancel on an orientation-reversing chart overlap. No global choice of base orientation is needed.

For a closed point \(p\hookrightarrow X\), the direct-image incidence is the full fibre \(T_p^*X\), and its map \(i_\pi\) is a closed embedding into \(T^*X\), hence proper. Its \(i_d\) maps to the point zero section. Thus (19) is the actual supported trace image of \(1\), a conormal generator with the cotangent-fibre coefficient included. The inverse operation would instead require the fibre collapse to be proper; in positive dimension it is not. The existence of this direct conormal cycle does not authorize that distinct inverse operation.

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§2.1–2.3, pp. 196–197, gives the cotangent orientation and twisted conormal-chain convention. It supplies that framework, rather than the graph/diagonal adjunction proof developed here. The exact specialization and microlocalization comparison maps used in (8)–(16), with their transformation identities, are proved in the programme lessons linked at each step.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4, 4.6.6–4.6.7, §4.7 and Proposition 5.1.9, pp. 95–98 and 107–108, explains the exceptional composition, tensor, support and relative-dualizing operations. Here the graph calculation retains changing derivative rank, distinguishes the diagonal restriction unit from the ambient counit, and proves equality of the two actual adjoints with the ordered orientation factors. Properness is imposed only for transport of the chosen carrier. The six worked examples separately check that domain, its shifts, and the normalized point, zero-section and conormal classes. The human sources retain their authorship and their own terms.
