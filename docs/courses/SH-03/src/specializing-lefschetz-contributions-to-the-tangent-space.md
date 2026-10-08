# Specializing Lefschetz contributions to the tangent space

At a transverse fixed point, a nonlinear map and a constructible coefficient can be replaced by their normal models. The replacement of the map is its derivative. The replacement of the sheaf is specialization, which retains how its support approaches the point. We prove that this replacement preserves the evaluated local class, including its orientation and grading.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Learn first Lefschetz traces of constructible correspondences, Natural duality for specialization and microlocal Hom, and Homotopies and local cutoffs for Lefschetz contributions. The specialization construction supplies the inverse-image comparison and its mates, the zero-section comparisons, and the normalized positive-parameter boundary map. The perfect-coefficient specialization theorem gives bounded constructible outputs. We identify below the particular tensor, evaluation and supported diagonal maps needed for the trace.

## The coefficient morphism uses a comparison in one direction

Let \(X\) be a real analytic manifold with the standing Hausdorff, countability and uniform finite dimension assumptions. Let \(k\) be a characteristic-zero field, \(F\in D^b_{\mathbb R\text{-c}}(k_X)\) have perfect stalks, and take a real analytic map \(f\) with coefficient morphism
\[
 f:X\longrightarrow X,\qquad
 \phi:f^{-1}F\longrightarrow F,\qquad f(x)=x.
 \qquad\text{(1)}
\]
Work in a neighbourhood of \(x\), write \(V=T_xX\), and put \(u=d f_x\). Normal deformation gives an analytic map between the deformations at \(x\), whose central map is \(u\). In adapted coordinates its normal component is
\[
 f_t(v)=\frac{f(x+tv)-x}{t}\quad(t>0),
 \qquad f_0(v)=uv.
 \qquad\text{(2)}
\]
Analyticity supplies the extension at \(t=0\). Formula (2) is a chart description of the lifted map, not a globally chosen coordinate on \(X\).

The inverse-image comparison and functoriality of specialization give
\[
 \nu\phi:
 u^{-1}\nu_xF
 \xrightarrow{\alpha_f}\nu_x(f^{-1}F)
 \xrightarrow{\nu_x(\phi)}\nu_xF.
 \qquad\text{(3)}
\]
The first arrow need not be invertible. Its definition is the ordinary positive-chamber base-change map, followed by central restriction. The same definition fixes its composition law and its adjunction mate. No invertibility of \(u\) is required.

The output is bounded conic constructible with perfect stalks. Its local contribution at zero is defined when zero is isolated in its supported fixed set.

## The point comparison fixes the normalization

Write \(i:\{x\}\hookrightarrow X\), \(e:\{0\}\hookrightarrow V\). The earlier zero-section theorem gives actual natural comparisons
\[
 i^{-1}G\simeq e^{-1}\nu_xG,\qquad
 i^!G\simeq e^!\nu_xG.
 \qquad\text{(4)}
\]
Recall the map in the second formula. Sections supported on \(\{x\}\) pull to the positive chamber and then to the central zero cone. The resulting support comparison is adjoint to the original support counit. For a point-supported coefficient \(i_*L\), the deformation is the zero-normal axis times the parameter; its boundary model is
\[
 L\boxtimes k_{\{t>0\}}[1].
 \qquad\text{(5)}
\]
The exceptional endpoint restriction of \(k_{\{t>0\}}\) is \(k[-1]\). The positive-parameter localization connecting map identifies (5) at the boundary with \(L\), by the identity of \(L\). This checks the map and cancels the parameter shift.

For a general \(G\), the comparison with point support reduces to this case by its support counit. In the normal-support description, a closed set with no nonzero limiting normal direction is locally contained in \(\{x\}\): otherwise a sequence approaching \(x\), normalized in a small chart, has a subsequence of unit directions. That gives a nonzero normal direction. Thus the zero-cone support system is cofinal with point support, which is precisely the support comparison in (4).

The first comparison in (4) also identifies the actual dynamical stalk maps. If \(\rho_G:i^{-1}G\to e^{-1}\nu_xG\) denotes its forward direction, the square is
\[
\begin{array}{ccc}
i^{-1}f^{-1}G=i^{-1}G&\xrightarrow{\rho_{f^{-1}G}}&e^{-1}\nu_x(f^{-1}G)\\
\downarrow\rho_G&&\uparrow e^{-1}\alpha_f\\
e^{-1}\nu_xG=e^{-1}u^{-1}\nu_xG&=&e^{-1}u^{-1}\nu_xG.
\end{array}
\qquad\text{(4a)}
\]
Both maps on the zero axis of the deformation are the identity map of the parameter. The ordinary restriction counits defining \(\alpha_f\) therefore restrict there to the same counits defining \(\rho_G\). This proves the square by the ordinary inverse-image composition identity. Composing its top row with \(e^{-1}\nu_x\phi\) proves that the zero-stalk action of (3) is exactly \(\phi_x\), even when \(u\) is singular.

The costalk comparison in (4) is natural in coefficient morphisms on the fixed ambient space. Identifying a supported pullback action under a change of the ambient map needs an additional hypothesis. When \(f\) is a local analytic isomorphism at \(x\), choose its local inverse branch; its only preimage of \(x\) is \(x\). Its deformation lift is an isomorphism near the zero axis, with central map \(u\). The support-pullback comparison is then the isomorphism for these Cartesian point-support squares. Pullback carries the support counit to the support counit, and leaves the increasing parameter unchanged. Thus (4) intertwines the supported actions for this local-isomorphism case. For a singular map, the object isomorphism in (4) alone gives no such assertion: supported pullback can carry a local degree absent from the singular linear map. The proof of (20) below instead compares the complete diagonal/evaluation classes.

In particular,
\[
 \nu_x\omega_X\simeq\omega_V,\qquad
 H_{\{x\}}^0(X;\omega_X)
 \simeq H_{\{0\}}^0(V;\omega_V)\simeq k.
 \qquad\text{(6)}
\]
Locally \(\omega_X=\operatorname{or}_X[n]\); its specialization is the same tangent orientation line in degree \(-n\). The point traces in (6) are exceptional composition with the map to a point. The calculation (5) shows that the support comparison commutes with these traces. No independent scalar identification with \(k\) is chosen.

## Evaluation survives the boundary comparison

We need compatibility of actual evaluation, not just the existence of a duality isomorphism. On the normal deformation write \(j:\Omega\hookrightarrow D\) for the positive chamber, \(r:\Omega\to X\), and \(s:V\hookrightarrow D\) for the central fibre. The positive orientation gives \(r^!F=r^{-1}F[1]\). Put
\[
 A=j_!r^!F.
 \qquad\text{(7)}
\]
The normalized boundary and duality proofs give
\[
 \nu_xF=s^!A,\qquad
 \nu_xD_XF=s^{-1}D_DA
 \xrightarrow{\sigma_F}D_V(\nu_xF).
 \qquad\text{(8)}
\]
The first equality includes the particular localization connecting map. The last arrow is exceptional-duality adjunction followed by the dual of that connecting map.

Let \(\mu\) denote the lax tensor comparison of specialization. With the indicated tensor order, the following equality of maps holds:
\[
 \begin{aligned}
 \nu_xF\otimes\nu_xD_XF
 &\xrightarrow{1\otimes\sigma_F}
 \nu_xF\otimes D_V\nu_xF
 \xrightarrow{\mathrm{ev}_V}\omega_V\\
 &=
 \nu_xF\otimes\nu_xD_XF
 \xrightarrow{\mu}\nu_x(F\otimes D_XF)
 \xrightarrow{\nu_x\mathrm{ev}_X}
 \nu_x\omega_X
 \xrightarrow{(6)}\omega_V.
 \end{aligned}
 \qquad\text{(9)}
\]

**Map check.** Write \(H=r^{-1}F\) and \(L=r^{-1}D_XF\). For any two chamber complexes, multiplication by \(Rj_*L\) makes the localization triangle for \(j_!H\) compatible with the localization triangle for \(j_!(H\otimes L)\). Indeed open projection identifies
\(j_!H\otimes Rj_*L\simeq j_!(H\otimes L)\): restrict to the chamber and use \(j^{-1}Rj_*L=L\); outside the chamber both ordinary stalks are zero. On the ordinary direct-image term use the cup comparison \(Rj_*H\otimes Rj_*L\to Rj_*(H\otimes L)\). These two maps commute with the localization arrow by its restriction counit. Taking its fibre therefore gives a morphism of localization triangles, including their connecting arrows.

After central restriction, this says that the boundary map \(\delta\) satisfies
\[
\delta_{H\otimes L}\,\mu =
\bigl[s^!j_!H[1]\otimes s^{-1}Rj_*L
\longrightarrow s^!(j_!H[1]\otimes Rj_*L)
\longrightarrow s^!j_!(H\otimes L)[1]\bigr]
(\delta_H\otimes1).
\qquad\text{(9a)}
\]
Here \(\delta_H:s^{-1}Rj_*H\to s^!j_!H[1]\) is the localization connecting map. The first arrow in brackets is the exceptional tensor comparison, and the second is open projection. The equality follows from the morphism of triangles just constructed. In a cochain-cone model it is the inclusion into the same shifted cone on both sides. Tensor orders and the connecting-map convention are unchanged, so it introduces no independently chosen sign.

Now transpose the evaluation determined by \(\sigma_F\) under \(s_*\dashv s^!\). It is precisely the composite
\(s_*s^!A\otimes D_DA\to A\otimes D_DA\to\omega_D\), whose first arrow is the central support counit and whose second is
\[
 A\otimes D_DA\longrightarrow\omega_D.
 \qquad\text{(10)}
\]
Since \(A=j_!r^!F\), open projection and \(j_!\dashv j^{-1}\) identify (10) with
\[
 r^!F\otimes r^{-1}D_XF
 \longrightarrow r^!\omega_X.
 \qquad\text{(11)}
\]
This is exceptional tensor comparison followed by \(r^!\mathrm{ev}_X\). The open counit then sends \(j_!r^!\omega_X=j_!\omega_\Omega\) to \(\omega_D\); applying \(s^!\) gives \(\omega_V\). By the positive-interval trace and (5), this last boundary map is exactly the identification (6).

Apply (9a) to \(H,L\) and then apply the evaluation in (11). The result is the first line of (9), expressed using the central support counit. Its other side is the second line of (9), expressed using the lax tensor map and the same boundary map for \(\omega_X\). Thus (9a), followed by these actual counits, proves (9). The equality is established on the localization triangle itself; an equality only after positive-chamber restriction would not determine a boundary morphism.

## The specialized diagonal identity is the diagonal identity

Set
\[
 K=F\boxtimes D_XF,\qquad
 K_0=\nu_xF\boxtimes D_V\nu_xF.
 \qquad\text{(12)}
\]
Let \(\nu^{(2)}\) be specialization at \((x,x)\) in \(X^2\). Using \(\sigma_F^{-1}\) on the second factor, the equal-time external comparison is
\[
 \lambda:K_0\longrightarrow\nu^{(2)}K.
 \qquad\text{(13)}
\]
At our constructible scope the external comparison (13) is invertible, as the following argument proves. The later tensor comparison on one ambient space can still fail to be invertible.

**External products in the point deformation.** At the constructible scope of this lesson, the equal-time external comparison is an isomorphism. This differs from the tensor comparison on one ambient space. Here is a local check of its actual map. Around a pair of normal vectors choose compact closed normal balls \(B,C\), each containing its vector in its interior, and a small parameter interval \(I\) containing zero on which the two deformation charts are defined. Restrict the ambient analytic pullbacks of the two coefficients to these balls, equivalently extending those restrictions by their closed inclusions in the charts. Projection to \(I\) is proper on their closed supports. The resulting parameter complexes are bounded constructible with perfect stalks. Constructibility on an interval containing zero permits shortening its positive part to \((0,\epsilon)\) on which both complexes are constant; no infinite sequence of new parameter strata can accumulate at zero.

The proper direct image from \(B\times C\times I\) of the product coefficient is the tensor of these two parameter complexes, by the following actual Künneth cup. In the Cartesian square formed by \(B\times C\times I\), \(B\times I\), \(C\times I\) and \(I\), proper base change pulls the direct image from \(B\times I\) back to \(C\times I\). Tensor with the coefficient on \(C\times I\), apply the projection formula for the projection to \(C\times I\), and then compose the proper images. This identifies the tensor of the parameter complexes with the product direct image. All the projections here are proper, and the composite is induced by the ordinary product of sections.

Ordinary descent on the positive interval identifies sections of the constant parameter complexes with their fibres, and identifies the equal-time cup with tensor product of those fibres. It is therefore an isomorphism on these neighborhood section complexes. Passing to the filtered systems of balls and positive intervals computes the two specialization stalks and the product specialization stalk. Closed balls can be used because each contains a smaller open neighborhood and is contained in a larger one; the resulting restriction systems interleave. This passage does not require base change for \(Rj_*\) at a fixed lateral ball boundary. A single sufficiently small parameter interval is cofinal among the two choices; its size may depend on the chosen balls. Tensor products over the field commute with these filtered colimits. Consequently the actual external comparison is an isomorphism on every stalk, hence an isomorphism of sheaves. This argument does not identify specialization of \(A\otimes B\) with \(\nu A\otimes\nu B\) on the same space.

The diagonal lifts to a closed embedding \(\delta_D:D\hookrightarrow D^{(2)}\). Its positive and central squares are Cartesian: equality of the two rescaled chart coordinates is the same as equality before rescaling, and the central map is \(\delta_V:V\hookrightarrow V^2\). Closed proper base change therefore identifies specialization of diagonal direct image with normal diagonal direct image. Its exceptional adjunction mate is
\[
 \beta_\delta:\nu_x(\delta_X^!K)
 \longrightarrow\delta_V^!\nu^{(2)}K.
 \qquad\text{(14)}
\]
All direct images in this check are those of a closed embedding; no properness of the deformation projection is assumed.

**Identity compatibility.** Under the normalized comparisons
\(\delta_X^!K=R\mathcal Hom(F,F)\) and
\(\delta_V^!K_0=R\mathcal Hom(\nu_xF,\nu_xF)\), the two paths
\[
 \begin{aligned}
 k_V&\xrightarrow{\nu_x(\mathrm{id}_F)}
 \nu_x(\delta_X^!K)
 \xrightarrow{\beta_\delta}\delta_V^!\nu^{(2)}K,\\
 k_V&\xrightarrow{\mathrm{id}_{\nu_xF}}
 \delta_V^!K_0
 \xrightarrow{\delta_V^!\lambda}\delta_V^!\nu^{(2)}K
 \end{aligned}
 \qquad\text{(15)}
\]
are equal. Here \(\nu_xk_X=k_V\) is the normalized constant-coefficient calibration.

**Proof.** First retain the actual exceptional mate. Its unit, closed direct-image comparison and counit give
\[
 \begin{aligned}
 \nu_x\delta_X^!K
 &\xrightarrow{\eta}
 \delta_V^!\delta_{V*}\nu_x\delta_X^!K\\
 &\xrightarrow{c_!}
 \delta_V^!\nu^{(2)}\delta_{X*}\delta_X^!K
 \xrightarrow{\nu^{(2)}\epsilon}
 \delta_V^!\nu^{(2)}K.
 \end{aligned}
 \qquad\text{(16)}
\]
The second arrow in (16) is the inverse direction of the closed proper comparison \(b\). Its units and counits fix the map \(\beta_\delta\).

We use coevaluation and its Verdier dual. Put \(G=\nu_xF\), and denote the identity kernels by
\[
c_F:\delta_{X*}k_X\longrightarrow F\boxtimes D_XF=K,\qquad
c_G:\delta_{V*}k_V\longrightarrow G\boxtimes D_VG=K_0.
\]
Write \(b_L:\nu^{(2)}\delta_{X*}L\xrightarrow{\sim}\delta_{V*}\nu_xL\) for the closed proper comparison. The desired equality, before exceptional diagonal adjunction, is
\[
\nu^{(2)}c_F\,b_{k_X}^{-1}=\lambda c_G.
\]
This is a statement on the central fibre. We will prove it there by duality, without inferring it from its positive-chamber restriction.

Identify \(D_{X^2}K\) with \(Q=D_XF\boxtimes F\) by actual constructible biduality, and \(D_{V^2}K_0\) with \(Q_0=D_VG\boxtimes G\). With these identifications the dual of \(c_F\) is
\[
e_F:Q\longrightarrow\delta_{X*}\omega_X,
\]
whose ordinary diagonal adjoint is \(D_XF\otimes F\to\omega_X\). This follows by transposing the identity of \(F\) in the external-Hom identification: currying gives the evaluation map, and the evaluation biduality map is the one just used in \(D K=Q\). Define \(e_G\) in the same way. Let
\[
\kappa:Q_0\longrightarrow
\nu_xD_XF\boxtimes\nu_xF\longrightarrow\nu^{(2)}Q
\]
use \(\sigma_F^{-1}\) in its first factor and the actual external comparison. The preceding external-product proof makes \(\lambda\) and \(\kappa\) invertible.

There are two map identities to check. First, if \(\sigma_K:\nu^{(2)}D_{X^2}K\to D_{V^2}\nu^{(2)}K\) is the boundary duality comparison on the product, then
\[
D_{V^2}\lambda\;\sigma_K\;\kappa=\operatorname{id}_{Q_0}.
\]
To verify it, pair its source with \(K_0\). The resulting pairing is the evaluation of \(\nu^{(2)}K\) after \(\lambda\otimes\kappa\). Apply (9) on \(X^2\). The evaluation of \(K\) is the product of \(F\otimes D_XF\to\omega_X\) and \(D_XF\otimes F\to\omega_X\), after the prescribed graded exchange. The lax tensor and external comparisons commute with that exchange and with products: both comparisons are defined by the same chamber restriction counits, so their adjoint composites are the same ordered product of counits. Apply (9) to the two evaluations of \(F\), using their Koszul exchange. The result is exactly the evaluation of \(K_0\). The product of the tangent orientation comparisons (6) is the product-space comparison (6), in the same ordered coordinates. Tensor–Hom adjunction now proves the displayed identity. This argument uses Verdier evaluation and biduality; it does not regard arbitrary constructible sheaves as dualizable for ordinary tensor product.

Second, identifying \(\nu_x\omega_X\) with \(\omega_V\), one has
\[
b_{\omega_X}\,\nu^{(2)}e_F\,\kappa=e_G.
\]
Transpose this equality under \(\delta_V^{-1}\dashv\delta_{V*}\). The left transpose is
\[
D_VG\otimes G
\xrightarrow{\sigma_F^{-1}\otimes1}\nu_xD_XF\otimes\nu_xF
\xrightarrow{\mu}\nu_x(D_XF\otimes F)
\xrightarrow{\nu_x\mathrm{ev}}\nu_x\omega_X\longrightarrow\omega_V.
\]
Indeed, ordinary diagonal restriction of the external cup, followed by the specialization inverse-image comparison for the diagonal, is the lax tensor cup. This follows directly by restricting its two chamber counits to the diagonal. The ordinary restriction counit for \(\delta_X^{-1}\dashv\delta_{X*}\), transported by \(b\), then gives \(\nu_x\mathrm{ev}\); the two closed embedding counits compose by the base-change triangle identity. Thus the transposition retains all the maps. Equation (9), with the displayed graded order, identifies this transpose with the evaluation of \(G\), which is the transpose of \(e_G\). Ordinary diagonal adjunction proves the second identity.

Finally the boundary duality comparison is natural for the coefficient morphism \(c_F\). It is also compatible with \(b_L\) and closed-embedding duality. For this latter assertion, the boundary model of \(\delta_{X*}L\) is the closed direct image of the boundary model of \(L\): the chamber square is Cartesian, its parameter submersion has the same positive orientation, and both central restriction comparisons are closed proper base change. The closed direct-image counit commutes with the localization triangle. Applying the duality construction (8) therefore yields the usual closed duality map, with no additional parameter sign. In particular it identifies the dual of \(b_{k_X}\) with \(b_{\omega_X}^{-1}\) through these duality comparisons.

Use this naturality in the second identity, then use \(D\lambda\,\sigma_K\,\kappa=1\). Since \(\kappa\) is invertible, it gives
\[
D_{V^2}\!\left(\nu^{(2)}c_F\,b_{k_X}^{-1}\right)
=D_{V^2}c_G\,D_{V^2}\lambda.
\]
Constructible biduality is faithful, so dualizing proves the desired coevaluation square. Transposition under \(\delta_{V*}\dashv\delta_V^!\) proves (15). Its first transpose is exactly (16), since the unit and counit there define the mate of \(b^{-1}\); its second is \(\delta_V^!\lambda\) applied to the identity kernel of \(G\). The internal-Hom cup (18) describes the induced action on endomorphisms, but the equality in the common diagonal-kernel target has now been proved separately.

On the positive chamber the corresponding coefficient identity is
\[
 r^{-1}F\xrightarrow{\mathrm{id}}r^{-1}F.
 \qquad\text{(17)}
\]
This is consistent with the coevaluation square just proved, but its restriction alone would not determine that square on the central fibre. The induced internal-Hom comparison is adjoint to
\[
 \nu_xR\mathcal Hom(F,F)\otimes\nu_xF
 \xrightarrow{\mu}
 \nu_x(R\mathcal Hom(F,F)\otimes F)
 \xrightarrow{\nu_x\mathrm{ev}}\nu_xF.
 \qquad\text{(18)}
\]
Its value on \(\nu_x(\mathrm{id}_F)\) is the identity of \(\nu_xF\), by the tensor-unit and restriction-counit identities. The coevaluation argument establishes (15) in its specified diagonal-kernel target in addition to this endomorphism calculation. \(\square\)

## The full supported trace comparison

Assume
\[
 \det(1-u)\ne0.
 \qquad\text{(19)}
\]
The graph of \(f\) is transverse to the diagonal at \(x\). Equivalently, the derivative of \(f-\mathrm{id}\) is invertible. The analytic inverse function theorem makes \(x\) an isolated fixed point in a sufficiently small neighbourhood. The only fixed vector of \(u\) is zero.

**Tangent specialization theorem.**
\[
 C_x(\phi)=C_0(\nu\phi).
 \qquad\text{(20)}
\]

**Proof.** The isolation is uniform in the deformation parameter. Choose chart norms and \(m>0\) with \(\lVert(u-1)v\rVert\ge m\lVert v\rVert\). Write \(f(x+z)-x=uz+R(z)\). Differentiability gives a ball on which \(\lVert R(z)\rVert\le(m/2)\lVert z\rVert\). Whenever \(t>0\) and \(tv\) lies in this ball, (2) gives \(\lVert f_t(v)-v\rVert\ge(m/2)\lVert v\rVert\). At \(t=0\) the stronger bound with \(m\) holds. Thus the inverse image of the diagonal by the lifted graph is exactly the zero-normal parameter axis in this deformation neighborhood. In particular, no nonzero central fixed support appears in the comparison. Put \(h=(f,\mathrm{id})\) and \(h_0=(u,\mathrm{id})\). The lifted graph map and the equal-time product comparisons give
\[
 \begin{aligned}
 h_0^{-1}K_0
 &=u^{-1}\nu_xF\otimes D_V\nu_xF\\
 &\longrightarrow
 \nu_x(f^{-1}F\otimes D_XF).
 \end{aligned}
 \qquad\text{(21)}
\]
This is \(h_0^{-1}\lambda\) followed by the inverse comparison for the lifted graph. Its first-factor component is \(\alpha_f\); its second is \(\sigma_F^{-1}\). Naturality of the positive restriction counits consequently gives the commutative coefficient square
\[
 \begin{array}{ccc}
 u^{-1}\nu_xF\otimes D_V\nu_xF&
 \longrightarrow&\nu_x(f^{-1}F\otimes D_XF)\\
 \downarrow\,\nu\phi\otimes1&&
 \downarrow\,\nu_x(\phi\otimes1)\\
 \nu_xF\otimes D_V\nu_xF&
 \longrightarrow&\nu_x(F\otimes D_XF).
 \end{array}
 \qquad\text{(22)}
\]
The vertical arrow on the left is exactly (3), including \(\alpha_f\).

Here is the supported graph comparison with its unit retained. Each graph map is a closed embedding, because its second component is the identity. Its deformation lift is also a closed graph, and the chamber and central squares are Cartesian. Write
\[
b_h:\nu^{(2)}h_*E\xrightarrow{\sim}h_{0*}\nu_xE
\]
for closed proper comparison. The ordinary inverse comparison \(\alpha_h:h_0^{-1}\nu^{(2)}K\to\nu_xh^{-1}K\) is its mate. If \(\eta_h:K\to h_*h^{-1}K\) is the ordinary graph unit, the defining mate identity is
\[
b_h\,\nu^{(2)}\eta_h
=(h_{0*}\alpha_h)\eta_{h_0}.
\qquad\text{(22a)}
\]
Indeed, substitute the ordinary unit and counit formula for \(\alpha_h\); the inserted unit and counit cancel by their triangle identity, leaving the left side. This is an equality of maps on the central fibre.

Compose (22a) with the specialized diagonal coevaluation. Identity compatibility (15) replaces that coevaluation by the normal one followed by \(\lambda\). Thus the two paths into \(h_{0*}\nu_xE_1\) agree, where \(E_1=h^{-1}K\). Under ordinary graph adjunction their source is \(h^{-1}\delta_{X*}k_X=k_{\operatorname{Fix}(f)}\); closed proper base change for the diagonal gives this identification. Hence their original Hom group is \(H^0_{\{x\}}(X;E_1)\), and the corresponding normal Hom group is \(H^0_{\{0\}}(V;\nu_xE_1)\). The uniform fixed-axis estimate proves that these are exactly the two point supports. On their constant support sheaves the inverse comparison is the identity: both are the sheaf of the point, and the zero-stalk restriction counits are identity as in (4a). Consequently the comparison of these Hom groups is precisely the support-counit comparison (4), applied to \(E_1\). The other normal path is the diagonal identity pulled to \(h_0\) and then mapped by (21). This proves the required equality of supported identity classes without imposing invertibility of \(u\).

Take point-supported global sections of (22). Use (4) on its right column, and evaluate its bottom row using (9). For a readable supported diagram, abbreviate the original coefficients by
\(E_1=f^{-1}F\otimes D_XF\), \(E_2=F\otimes D_XF\), and the normal coefficients by
\(N_1=u^{-1}\nu_xF\otimes D_V\nu_xF\), \(N_2=\nu_xF\otimes D_V\nu_xF\).
The left horizontal arrows below are the coefficient-natural isomorphisms from (4), applied separately to \(E_1\) and \(E_2\); the right horizontal arrows are the actual lax comparisons. The left square uses the coefficient morphism \(\phi\otimes1:E_1\to E_2\) on \(X\), and does not identify a singular ambient pullback action on \(i^!F\):
\[
 \begin{array}{ccccc}
 H_{\{x\}}^0(X;E_1)&
 \xrightarrow{\sim}&
 H_{\{0\}}^0(V;\nu_xE_1)&
 \overset{(21)}{\longleftarrow}&H_{\{0\}}^0(V;N_1)\\
 \downarrow\,\phi\otimes1&&
 \downarrow\,\nu_x(\phi\otimes1)&&
 \downarrow\,\nu\phi\otimes1\\
 H_{\{x\}}^0(X;E_2)&
 \xrightarrow{\sim}&H_{\{0\}}^0(V;\nu_xE_2)&
 \overset{\mu(1\otimes\sigma_F^{-1})}{\longleftarrow}&H_{\{0\}}^0(V;N_2).
 \end{array}
 \qquad\text{(23)}
\]
The diagonal identity starts the two upper paths by (15). Both horizontal directions point into the specialization groups; the proof does not compose an inverse of a lax arrow.

After evaluation, (23) ends in
\[
 \begin{array}{ccc}
 H_{\{x\}}^0(X;\omega_X)&
 \xrightarrow{\sim}&H_{\{0\}}^0(V;\nu_x\omega_X)\\
 \downarrow&&\uparrow\,\sim\\
 k&\overset{\mathrm{trace}}{\longleftarrow}&H_{\{0\}}^0(V;\omega_V).
 \end{array}
 \qquad\text{(24)}
\]
This square commutes by (6). The original path is the defining supported diagonal/evaluation path for \(C_x(\phi)\). The normal path is that for \(C_0(\nu\phi)\). Equations (15), (22), (9) and (24) identify the complete paths, proving (20). \(\square\)

This theorem specializes the coefficient as well as the map. Replacing \(F\) only by its stalk generally discards the local boundary information seen in the endpoint example.

## Exercises with complete solutions

### A nonlinear contraction keeps its half-line coefficient

*Difficulty: Intermediate.*

Near zero take \(f(t)=t/2+t^3\), \(F=k_{[0,\infty)}[r]\), and the canonical coefficient map. Compute the local contribution using (20).

**Solution.** Restrict to a sufficiently small interval. There \(f\) is increasing, preserves the two sides of zero and has no fixed point except zero; the other solutions of \(f(t)=t\) are outside this interval. Its derivative is \(u(t)=t/2\), so \(1-u\) is invertible.

The half-line sheaf is conic. Its normalized specialization is itself by conic calibration, and the inverse comparison sends the canonical coefficient map to the canonical map for \(u\). The attracting endpoint computation in the preceding lesson gives \(C_0(\nu\phi)=(-1)^r\). Equation (20) therefore gives \(C_0(\phi)=(-1)^r\), although the original map contains a cubic term.

### A zero derivative does not allow inversion of the comparison

*Difficulty: Advanced.*

Take \(f(t)=t^2\), \(F=k_{\{0\}}\), and the identity coefficient map \(f^{-1}F=F\). Work near zero. Describe (3) and compute its local contribution.

**Solution.** The derivative \(u\) is the zero map, so \(1-u=1\) is invertible. Point calibration gives \(\nu F=k_{\{0\}}\) and \(\nu(f^{-1}F)=k_{\{0\}}\). But \(u^{-1}\nu F=k_{\mathbb R}\). The inverse comparison is the ordinary closed restriction
\(k_{\mathbb R}\to k_{\{0\}}\): on the positive chamber the map is restriction to \(t v^2=0\), and the central counits retain that restriction. It is identity on the zero stalk and zero on every nonzero stalk, hence is not an isomorphism.

The normal correspondence has maps \(u=0\) and \(\mathrm{id}\), with common coefficient support \(\{0\}\). Its finite trace factor and global point coefficient are both \(k\). The supported restriction map and return map are identity on them, giving trace \(1\). There is only one supported coincidence point, so \(C_0(\nu\phi)=1\), and (20) gives \(C_0(\phi)=1\). This uses (3) in its stated direction and allows a singular derivative.

### A curved support becomes its tangent line

*Difficulty: Advanced.*

Let \(Y=\{(x,y):y=x^2\}\), \(F=k_Y\), and
\[
 f(x,y)=(2x,\tfrac12y+\tfrac72x^2).
 \qquad\text{(25)}
\]
Use the canonical coefficient map. Compute the contribution at the origin.

**Solution.** The analytic diffeomorphism \(q(x,y)=(x,y-x^2)\) carries \(Y\) to the horizontal line and conjugates \(f\) to \((a,b)\mapsto(2a,b/2)\). In particular \(f^{-1}Y=Y\); the coefficient map is the canonical identity under that restriction.

The tangent map is \(\operatorname{diag}(2,1/2)\), with no eigenvalue one. The lifted coordinate change is
\((v_x,v_y,t)\mapsto(v_x,v_y-t v_x^2,t)\), whose central map is identity. By its actual inverse comparison, specialization of \(k_Y\) is the coefficient on the horizontal tangent line, and the specialized morphism is expansion by \(2\) on that line.

For this normal coefficient, closed direct image from the line transports the diagonal identity and evaluation by closed proper adjunction. Its point class is therefore the one-dimensional point class; no ambient dimension shift is added. The positive line expansion has contribution \(-1\), by the open cutoff calculation in the preceding lesson. Equation (20) gives \(C_{(0,0)}(\phi)=-1\). A rank-\(m\) coefficient shifted by \(r\) instead gives \(m(-1)^{r+1}\).

### Tangent supports need not commute with tensor product

*Difficulty: Advanced.*

At zero in \(\mathbb R^2\), let \(L=\{y=0\}\), \(Y=\{y=x^2\}\), \(A=k_L\), \(B=k_Y\). Show why the lax tensor comparison used in (23) cannot generally be inverted.

**Solution.** Both supports are closed, and the sheaves are stalkwise flat. Thus \(A\otimes B=k_{L\cap Y}=k_{\{0\}}\). Point calibration gives \(\nu(A\otimes B)=k_{\{0\}}\).

The line is conic, hence \(\nu A=k_L\). The lifted analytic coordinate change from the preceding solution, with central identity, gives \(\nu B=k_L\) by the actual deformation comparison. Consequently \(\nu A\otimes\nu B=k_L\). The lax comparison has source \(k_L\) and target \(k_{\{0\}}\). At a nonzero point of \(L\), its stalk is \(k\to0\), so it is not an isomorphism. At zero the restriction-counit normalization makes it identity, namely closed restriction to zero.

The two curved and straight supports originally meet only at the point, while their limiting normal directions agree on a whole line. The proof of (20) uses arrows into specialization and commutative evaluation; it never cancels this noninvertible tensor map.

### An isolated nonlinear fixed point need not have an isolated normal one

*Difficulty: Intermediate.*

For \(f(t)=t+t^3\), \(F=k_{\mathbb R}\), explain why (20) does not follow just from isolation of the original fixed point.

**Solution.** The only solution of \(f(t)=t\) is zero. Its original local class is therefore defined. But \(df_0=1\), so the normal self-map is identity, its coefficient is \(k_{\mathbb R}\), and its supported fixed set is the entire line. Zero is not isolated in that set, so the isolated normal contribution in (20) is not defined by the point-summand construction.

The determinant hypothesis fails exactly here. An isolated original fixed point does not imply an isolated normal one. One would need another result or a different supported invariant to make a comparison in this case; the isolated contribution theorem supplies neither an arbitrary point projection from the line nor a stalk-trace formula.

### Parameter and coefficient degrees have different roles

*Difficulty: Intermediate.*

At zero take the point coefficient with graded cohomology \(k^2\) in degree zero and \(k^3\) in degree one, zero differential, and scalar actions \(2\) and \(3\), respectively. Let \(f(t)=t^2\). Compute the local contribution, and explain why deformation adds no degree to it.

**Solution.** The coefficient trace is \(2\cdot2-3\cdot3=-5\). The inverse comparison for the zero derivative restricts the constant normal pullback to the point, as in the second solution, with the same graded scalar actions. Its common support is the point and its finite trace factor is this graded coefficient. Thus the normal local contribution is \(-5\).

The positive parameter introduces \([1]\) only in the boundary representation \(j_!r^!F\). Exceptional central restriction contributes the endpoint \([-1]\); (5), (8) and (9) cancel them through the fixed connecting map. The normalized point trace consequently retains the two original cohomology degrees. Equation (20) gives the original local contribution \(-5\), rather than a sign-reversed trace. Shifting the coefficient by \(r\) would multiply it by \((-1)^r\).

## References and further reading

Y. Matsui and K. Takeuchi, [*Microlocal study of Lefschetz fixed point formulas for higher-dimensional fixed point sets*](https://arxiv.org/abs/0812.4480v1), arXiv 0812.4480v1, 24 December 2008, Proposition 3.3 and its diagram (3.14), compare the local contribution with normal specialization. They require compact supported intersection with the smooth fixed component and exclude eigenvalue \(1\) in its normal map. The present theorem concerns an isolated transverse point and retains a possibly singular derivative.

Y. Ike, Y. Matsui and K. Takeuchi, [*Hyperbolic localization and Lefschetz fixed point formulas for higher-dimensional fixed point sets*](https://arxiv.org/abs/1504.04185v2), arXiv 1504.04185v2, 25 May 2015, Proposition 2.13, states the corresponding component result. The proof of Proposition 5.1 describes the ordinary supported identity/evaluation diagram before passing to Lefschetz cycles. The boundary normalization and supported maps used here are proved through the stated programme adjunctions; a citation to the component result does not replace those checks.
