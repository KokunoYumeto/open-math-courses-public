# SH02-FTC. Comparing traces after Fourier transformation

Original programme text: CC0 1.0 Universal. This unit isolates the maps in the Fourier normalization and microlocalization comparison problems. The base-change results and the categorical normalization construction below are proved relative to their explicit operation imports. The support equation in SH02-FTC-LINEAR is proved in SH02-FGC-SUPPORT, and the trace equation is proved in SH02-FTE-TRACE with its full endpoint comparison.

The published Fourier antecedent used here is Kashiwara–Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §2.1, especially the linear and base-map statements in Propositions 2.1.5–2.1.6. The supplement proves compatibility of specified support-forgetting and trace maps, which those functoriality statements alone do not identify. Read it with [Fourier kernels](fourier-sato.md), [Fourier functoriality](fourier-functoriality.md), and [the duality supplement](fourier-duality-normalization.md).

## SH02-FTC-DOMAINS. Which maps are fixed

Let \(k\) be a commutative unital ring of finite global dimension. Bases are locally compact Hausdorff spaces. All real vector bundles have fixed finite rank, and complexes are in the conic category \(D^+\), with a global lower bound. There is no finite-generation, constructibility, field, or compact-base assumption. Statements involving \(f^!\) require finite cohomological dimension of \(f_!\) on abelian sheaves. On maps of the manifolds used for microlocalization, the relative orientation complexes are invertible and bounded. A variable-rank bundle is treated on rank components only when the resulting global bounds hold.

We retain the actual negative-cut transform
\[
T_EF=Rq_!((p^{-1}F)_{\{\langle x,\xi\rangle\leq0\}}),
\]
its kernel right adjoint \(S_E\), and the specified first comparison \(c_E:T_E\to U_E\) of SH02-FS-COMPARE. The positive orientation identification between a vector space and its dual and all Koszul tensor symmetries are those of SH02-FF-CONVENTIONS. A new adjunction comparison will always receive a new name.

For a continuous map \(f:X\to Y\), write
\[
\nu_f: Rf_!\longrightarrow Rf_*
\tag{FTC1}
\]
for the derived inclusion of proper-support sections into unrestricted sections. When \(f^!\) exists, put \(\omega_f=f^!k_Y\). The map
\[
\theta_f(H):\omega_f\otimes^L f^{-1}H\longrightarrow f^!H
\tag{FTC2}
\]
is the mate, under \(Rf_!\dashv f^!\), of
\[
Rf_!(\omega_f\otimes^L f^{-1}H)
 \simeq Rf_!\omega_f\otimes^L H
 \xrightarrow{\operatorname{tr}_f\otimes1}k_Y\otimes^L H
 \simeq H.
\tag{FTC3}
\]
Here \(\operatorname{tr}_f\) is the counit evaluated at \(k_Y\). If the orientation factor is written on the right instead, the specified tensor symmetry is included. Formula FTC2 is not asserted to be an isomorphism for an arbitrary map or arbitrary \(H\).

The imports in use are proper-support base change and composition, ordinary and exceptional adjunctions, the proper-support projection formula, their mate and pasting compatibilities, and the bundle orientation formula with its trace. Their full locally compact Hausdorff scope is the explicit foundation contract of SH02-FF-DOMAINS. The proof also uses the already constructed conic Fourier equivalence with its fixed adjunction.

## SH02-FTC-OPEN. Forgetting support across an open restriction

We first give the categorical argument that removes any possible scalar ambiguity for an open base inclusion.

Let \(j:B_0\hookrightarrow B\) be open, with induced open bundle inclusions \(j_E,j_{E^*}\). The kernel gives a restriction isomorphism
\[
j_{E^*}^{-1}T_E\simeq T_{E_0}j_E^{-1}.
\tag{FTC4}
\]
The open-extension comparison is its left adjoint mate, after conjugating by the Fourier equivalences. The ordinary direct-image comparison is its right adjoint mate. These are exactly the open cases of the base-change maps in SH02-FF-BASE: extension by zero commutes with the cut kernel and with proper integration, and the right comparison there was defined by the same mate operation.

**Lemma.** Under those two comparisons, \(T_E\nu_{j_E}\) is \(\nu_{j_{E^*}}T_{E_0}\).

**Proof.** For any object \(A\) on an open subset, the adjunctions give a bijection
\[
\operatorname{Hom}(j_!A,Rj_*A)
 \simeq\operatorname{Hom}(A,j^{-1}Rj_*A)
 \simeq\operatorname{Hom}(A,A).
\tag{FTC5}
\]
The support-forgetting map is the preimage of the identity: restriction of a section extended by zero is the same section on the open subset. Fourier conjugation with the two mates of FTC4 carries this bijection to the corresponding bijection for \(j_{E^*}\). It carries the identity to the identity. The bijection therefore proves equality of the two morphisms, not just equality of their restrictions or their cohomology dimensions. This works for arbitrary bounded-below objects because both open adjunctions and the restriction identity hold on that category. \(\square\)

## SH02-FTC-BASE-SUPPORT. General base maps preserve the support comparison

Let \(b:B'\to B\) be continuous and let \(E'=b^{-1}E\), with induced bundle maps \(b_E,b_{E^*}\). Use the proper and ordinary base-image comparisons of SH02-FF-BASE.

**Theorem.** The following square commutes:
\[
\begin{array}{ccc}
T_E R(b_E)_! A&\xrightarrow{T_E\nu_{b_E}}&T_E R(b_E)_* A\\
\downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim\\
R(b_{E^*})_!T_{E'}A&\xrightarrow{\nu_{b_{E^*}}}&R(b_{E^*})_*T_{E'}A.
\end{array}
\tag{FTC6}
\]
No finite cohomological-dimension assumption on \(b_!\) is needed for this statement.

**Proof.** We record first the proper case, including which comparison is used. If \(b\) is proper, so are its bundle pullbacks. Write \(P=b_E\), \(Q=b_{E^*}\), and let \(\alpha:Q^{-1}T_E\to T_{E'}P^{-1}\) be inverse-image base exchange. Let \(\lambda:T_ERP_*\to RQ_*T_{E'}\) be the proper-image kernel interchange. Its required mate equation is
\[
\epsilon_Q\circ Q^{-1}(\lambda_A)
 =T_{E'}(\epsilon_P)\circ\alpha_{RP_*A},
\tag{FTC6a}
\]
where \(\epsilon_P:P^{-1}RP_*A\to A\) and \(\epsilon_Q:Q^{-1}RQ_*T_{E'}A\to T_{E'}A\) are the ordinary counits. Both sides start at \(Q^{-1}T_ERP_*A\).

To verify FTC6a, expand \(T\) as proper integration of the pulled-back coefficient tensored with the flat cut. On the right, proper-support base change first pulls this integration to \(E'^*\); the coefficient morphism inside it is the inverse image of \(P^{-1}RP_*A\to A\). On the left, proper-image interchange moves \(RP_*\) through the two projection squares and the same cut, after which \(Q^{-1}RQ_*\to1\) is applied. The counit identity for proper base change in each Cartesian square identifies this coefficient morphism with that on the right. Concretely the base-change morphism is the adjoint of pullback of sections followed by the ordinary counit; applying the second counit removes its inserted unit by the triangle identity. The cut is the inverse image of the same degree-zero constant-extension sheaf, so projection-formula naturality adds no further coefficient map. Proper-support composition then gives exactly the same integration of that coefficient morphism on both sides. This proves FTC6a with no orientation permutation.

The ordinary adjunction bijection makes FTC6a characterize \(\lambda\) uniquely. That is the right-mate characterization used in SH02-FF-BASE, equivalently obtained there by conjugating with the Fourier equivalences. Thus the proper and ordinary base-image comparisons coincide when \(b\) is proper. Both horizontal arrows of FTC6 are then identities under \(!=*\), and the square commutes.

Here is a compactification that applies to every continuous map in the stated topological category. Give \(B'\) its one-point compactification \(B'^+\); if \(B'\) is already compact, adjoining a disjoint point suffices. The graph of \(b\) is closed in \(B'\times B\), since \(B\) is Hausdorff. Its closure \(\overline{\Gamma_b}\) in \(B'^+\times B\) is a locally compact Hausdorff space. Projection to \(B\) is proper: for every compact \(K\subset B\), its inverse image is a closed subset of the compact space \(B'^+\times K\). The graph is open in its closure and is homeomorphic to \(B'\). Thus
\[
B'\xrightarrow{j}\overline{\Gamma_b}
 \xrightarrow{\bar b}B,
\qquad b=\bar b j,
\tag{FTC7}
\]
is an open inclusion followed by a proper map. Pull back \(E\) to this intermediate base. This is still a finite-rank real vector bundle over a locally compact Hausdorff space. No manifold or finite-dimensional property of the compactification is required.

Under the composition maps, the support comparison for a composite \(vf\) is
\[
R(vf)_!\simeq Rv_!Rf_!
 \xrightarrow{Rv_!\nu_f}Rv_!Rf_*
 \xrightarrow{\nu_v}Rv_*Rf_*
 \simeq R(vf)_*.
\tag{FTC8}
\]
At the underived level this is the inclusion of sections with proper support into all sections; the derived identity follows from that natural inclusion and the derived composition maps. Equivalently one may interchange the middle two steps by naturality of \(\nu_v\).

Apply the open lemma to \(j\), the proper-case verification to \(\bar b\), and FTC8 to their composite. The Fourier base-image comparisons respect composition because their kernel base-change squares paste, and the same holds for their mates. The resulting pasted square is FTC6. The compactification is only a proof device; FTC6 uses the pre-existing maps for \(b\), so it is independent of that choice. \(\square\)

## SH02-FTC-BASE-TRACE. The relative trace in the base direction

Assume now that \(b_!\) has finite cohomological dimension on abelian sheaves. Use exceptional base-change Fourier exchange with the precise mate convention of SH02-FF-BASE. There are specified identifications
\[
\omega_{b_E}\simeq\tau'^{-1}\omega_b,
\qquad
\omega_{b_{E^*}}\simeq\pi'^{-1}\omega_b.
\tag{FTC9}
\]
For example, apply exceptional transitivity to \(\tau b_E=b\tau'\), use the bundle formula \(\tau^!Q=\tau^{-1}Q\otimes W_E\), and cancel the pulled-back invertible orientation complex \(W_E\) on the right. It is not an assumption that \(\omega_b\) itself is invertible. The following counit check fixes the map identification needed below.

Let \(\chi:R(b_E)_!\tau'^{-1}\xrightarrow\sim\tau^{-1}Rb_!\) be proper-support base change. Its exceptional mate, evaluated at the base unit, is
\[
\lambda_b:\tau'^{-1}\omega_b\longrightarrow b_E^!k_E,
\qquad
\lambda_b=\operatorname{adj}\bigl(\tau^{-1}\operatorname{tr}_b\circ\chi_{\omega_b}\bigr).
\tag{FTC9a}
\]
It therefore makes the following square commute by its definition:
\[
\begin{array}{ccc}
R(b_E)_!\tau'^{-1}\omega_b&\xrightarrow{\chi}&\tau^{-1}Rb_!\omega_b\\
\downarrow\scriptstyle R(b_E)_!\lambda_b&&\downarrow\scriptstyle\tau^{-1}\operatorname{tr}_b\\
R(b_E)_!\omega_{b_E}&\xrightarrow{\operatorname{tr}_{b_E}}&k_E.
\end{array}
\tag{FTC9b}
\]
To identify \(\lambda_b\) with the invertible transitivity map in FTC9, one may work over an open base trivialization of \(E\). On a product with \(\mathbb R^n\), the bundle adjunction uses the orientation evaluation
\(R\Gamma_c(\mathbb R^n;k)\otimes O_E[n]\to k\).
Proper-support base change in the base direction is the identity on this factor, and operates on the coefficient object in the base. Hence taking its exceptional mate and taking this orientation evaluation commute: both composites first apply the same base counit and the same displayed evaluation, with the orientation factor on the right. This is precisely the formula obtained by composing \(\tau'^!b^!\simeq b_E^!\tau^!\) and canceling the orientation factor. It proves equality of the two maps, rather than simply equality of the resulting objects. The calculation is natural under an oriented or orientation-reversing change of the fibre trivialization because the same orientation local system and evaluation occur on both sides. Thus it glues over the base. This proves FTC9 with its stated counit compatibility. Apply the same argument to the dual bundle for the second identification.

**Theorem.** Fourier transformation carries the map \(\theta_{b_E}(H)\) to \(\theta_{b_{E^*}}(T_EH)\) under exceptional base exchange, ordinary base pullback exchange, and FTC9.

**Proof.** Fourier has the base-module comparison
\[
T_E(F\otimes^L\tau^{-1}Q)
 \simeq T_EF\otimes^L\pi^{-1}Q,
\tag{FTC10}
\]
given by the proper-support projection formula. This includes its associativity and tensor symmetry. For two bounded-below inputs the finite global dimension bound and the degreewise truncation argument in SH02-FF-BOUNDS apply. The finite-dimensional vector integration is the only image involved in FTC10.

Transpose the proposed equality through
\(R(b_{E^*})_!\dashv b_{E^*}^!\). For the transformed \(\theta_{b_E}\), the resulting morphism is Fourier applied to FTC3 for \(b_E\), preceded by the proper base-image comparison. This assertion is exactly the definition of exceptional Fourier exchange as the right mate of proper-image exchange: its mate equation identifies the two exceptional counits. Thus no independent normalization of an inverse Fourier functor enters this step.

Use FTC9 and the proper-support base-change and projection-formula maps to expand that transformed FTC3. Its coefficient morphism is
\[
Rb_!\omega_b\xrightarrow{\operatorname{tr}_b}k_B;
\tag{FTC11}
\]
all other factors are the pulled-back coefficient \(H\), the flat halfspace cut, and proper vector integration. The corresponding expansion of FTC3 for \(b_{E^*}\) has exactly FTC11 as coefficient morphism and the same other factors. Indeed the trace for either lifted base map is pulled back from the trace for \(b\): this is the counit compatibility of exceptional transitivity used to define FTC9, together with proper-support base change. The module comparison FTC10 is itself the projection-formula comparison, so its associators identify these two expansions without adding an unsigned permutation of graded factors. Hence the transposed maps agree. The exceptional adjunction bijection proves the original equality.

For bounds, \(\omega_b\in D^+\) by the dimension-bounded construction of \(b^!\). Tensor products of two bounded-below inputs remain bounded below because \(k\) has finite global dimension. The lifted base maps have the same fibers as \(b\), so the same finite abelian-sheaf cohomological-dimension bound applies. These facts justify all operations and both adjunction bijections. \(\square\)

## SH02-FTC-LINEAR. The two fibre comparisons with their maps fixed

For a bundle map \(h:E_1\to E_2\) over the identity of \(B\), let \(r={}^th:E_2^*\to E_1^*\), and let \(W_i=O_{E_i}[n_i]\). The orientation comparisons fixed by exceptional transitivity give
\[
\omega_h=W_1\otimes W_2^{-1},
\qquad \omega_r=W_{2^*}\otimes W_{1^*}^{-1}.
\tag{FTC12}
\]
All pullbacks to the indicated source bundle are understood. Use the exact maps of SH02-FF-LINEAR-KERNEL and SH02-FF-MATES, including their chosen Fourier adjunction. The two equations, with their complete proofs referenced below, are the following.

**Linear support equation.** Under those isomorphisms, the map
\[
T_2Rh_!A\xrightarrow{T_2\nu_h}T_2Rh_*A
\]
must be identified with
\[
r^{-1}T_1A
 \xrightarrow{\theta_r\,\otimes\,\omega_r^{-1}}
r^!T_1A\otimes\omega_r^{-1}.
\tag{FTC13}
\]
The complete maps are now specified as follows. The input is the right-ordered \(\bar\theta_r\) of LFT-L2. The FF L3 map \(\ell_h\) uses the coherent initial extraction FF11b. Put \(L=\omega_r\), \(D=R\mathcal Hom(L,k)\), and use at its final endpoint
\[
\bar\ell_h^{\,b}
=(1\otimes\operatorname{ev}_L\sigma_{L,D})
(\ell_h\otimes1_D).
\tag{FTC13a}
\]
With these separately named operations, FTC13 means precisely
\[
\bar\ell_h^{\,b}\bar\theta_r
=T_2(\nu_h)A_h.
\tag{FTC13b}
\]
SH02-FGC-SUPPORT in [The graded support comparison](fourier-graded-comparison.md) proves FTC13b at the full bundle-map range, relative to the declared operation imports. Braided evaluation and inverse coevaluation are distinct contractions on this forward-ordered pair. Replacing only the final contraction by inverse coevaluation leaves the factor \((-1)^{n_2-n_1}\), so it is a different map. FTC13a specifies which contraction is used in the asserted support equation.

**Linear trace equation.** The map
\[
T_1(\omega_h\otimes h^{-1}H)
 \xrightarrow{T_1\theta_h}T_1h^!H
\]
must be identified with
\[
Rr_!T_2H\xrightarrow{\nu_r}Rr_*T_2H.
\tag{FTC14}
\]

These are equalities of maps. FGC23 proves the support equation with exactly FTC13a–FTC13b. FTE6 and FTE32–FTE34 in [The complete transpose endpoint](fourier-transpose-endpoint.md) prove FTC14 with its original R2 and R4 constructions: the coherent endpoint is a relative-rank sign times the right-ordered R3 rewrite, while its separately braided form equals the direct endpoint. The full input-line calculation then gives the trace square. Both proofs include rank-jumping bundle maps and the stated conic bounded-below coefficient range. SH02-MEP-SUPPORT and SH02-MEP-TRACE propagate these exact endpoints to both microlocal squares, and SH02-MEP-MATE-UNTWIST identifies the actual ordinary adjoint mate. The operation imports and fixed orientation-line conventions are retained in each application.

## SH02-FTC-REDUCTION. Pasting the microlocal comparison squares

Consider the normal derivative \(q=bh\) and its covector correspondence
\(E_Y^*\xleftarrow r C\xrightarrow s E_X^*\)
from SH02-MIC-CORRESPONDENCE in [microlocalization](microlocalization.md). The map \(s\) is the base lift of \(b\), while \(r={}^th\). Put \(L=\omega_r^{-1}\), with the transitivity identification used there.

**Reduction theorem.** FTC13 for \(h\), with the same complete orientation endpoint used in the normal-derivative comparison, implies part 1 of SH02-MIC-TRACE-EXCHANGE. FTC14 for \(h\) implies part 2. The additional base-change comparisons required in those implications are FTC6 and SH02-FTC-BASE-TRACE, respectively. SH02-MEP-MATE-UNTWIST proves that the explicit FTC13a endpoint is the actual fourth MIC11 row after the stated tensor–Hom extraction. SH02-MEP-NORMAL-COUNITS and MEP10a–MEP10b fix the normal orientation and both original R2/R4 endpoints. Thus SH02-MEP-SUPPORT and SH02-MEP-TRACE establish both microlocal identities, with the full map prescriptions.

**Proof for proper-support forgetting.** Expand \(\nu_q\) using FTC8. Apply Fourier to the first step \(Rb_!\nu_h\). The proper base-image exchange and FTC13 identify it with \(Rs_!\) applied to
\[
r^{-1}T_{E_Y}A\longrightarrow r^!T_{E_Y}A\otimes L.
\]
The second step is \(\nu_b\) applied to \(Rh_*A\). FTC6 identifies its transform with \(\nu_s\) on the displayed target. The resulting composite is exactly the independently described left vertical map in SH02-MIC-DIRECT. Pasting compatibility of the operation maps ensures that the endpoint identifications are MIC11, rather than new identifications chosen for this proof.

**Proof for the relative trace.** Exceptional transitivity and the projection formula give the composition identity for FTC2. In ordered tensor form, it is the composite
\[
\begin{aligned}
\omega_h\otimes h^{-1}\omega_b\otimes h^{-1}b^{-1}H
&\xrightarrow{1\otimes h^{-1}\theta_b}
\omega_h\otimes h^{-1}b^!H\\
&\xrightarrow{\theta_h}h^!b^!H
 \simeq q^!H.
\end{aligned}
\tag{FTC15}
\]
In the normal-bundle situation the left endpoint is identified with \(\omega_q\otimes q^{-1}H\) by the relative orientation comparison. Here \(\omega_b\) is a base-pulled invertible shifted local system. For such an object \(Q\), the map
\(\theta_h(Q):\omega_h\otimes h^{-1}Q\to h^!Q\)
is the canonical invertible-line extraction comparison: transpose both across \(Rh_!\dashv h^!\), and both become \(\operatorname{tr}_h\otimes1_Q\) after projection formula. Its invertibility follows locally by trivializing \(Q\), when it is the tensor-unit identity with a shift. Consequently the orientation comparison for \(\omega_q=h^!\omega_b\) used here agrees with the actual \(\theta_h(\omega_b)\), not an independently chosen line isomorphism.

To verify FTC15, transpose it across the composite exceptional adjunction. Its image first applies the trace of \(h\), then that of \(b\). This is the trace of \(bh\) by the counit formula for a composite adjunction; projection-formula pasting supplies the same input tensor. That is FTC3 for \(q\), proving the identity.

Apply Fourier to FTC15. SH02-FTC-BASE-TRACE identifies the first factor with the trace comparison for \(s\). FTC14 identifies the linear factor with \(\nu_r\). Extraction and evaluation of the base-pulled orientation factors give \(\omega_s=u^{-1}\omega_g\), exactly as in MIC10. Thus the resulting composite is
\[
Rr_!(u^{-1}\omega_g\otimes s^{-1}T_{E_X}H)
 \longrightarrow Rr_!s^!T_{E_X}H
 \longrightarrow Rr_*s^!T_{E_X}H,
\]
which is part 2 of SH02-MIC-TRACE-EXCHANGE. The order of the two arrows is retained. \(\square\)

The complete endpoint verifications are in [Following the microlocal comparison maps](microlocal-endpoint-propagation.md). They prove both identities with the stated normal orientations and retain the order of the base trace and support-forgetting arrows. The uncontracted right-ordered R4 mate is the relative-rank sign times coherent L3; after its coherent contraction it is exactly the braided endpoint needed here. Thus PA32 requires this relative-rank sign with the original R4 construction.

## SH02-FTC-NORMALIZED-MATE. A valid normalization construction

Here is a separate categorical fact that is useful when choosing conventions. It does not identify an already given geometric comparison with the convention it constructs.

Let \(T,U:\mathcal A\to\mathcal B\) and \(S,V:\mathcal B\to\mathcal A\) be inverse equivalences, with adjunctions
\[
T\dashv S\quad(\eta,\epsilon),
\qquad V\dashv U\quad(\bar\eta,e).
\]
Let \(c:T\xrightarrow\sim U\) be fixed. The inverse adjunction \(U\dashv V\) has unit \(e^{-1}\) and counit \(\bar\eta^{-1}\). Define
\[
d^{\mathrm{adj}}_G
=S(\bar\eta_G^{-1})\circ S(c_{VG})\circ\eta_{VG}:
VG\longrightarrow SG.
\tag{FTC16}
\]

**Proposition.** This is the unique right mate of \(c\) for \(T\dashv S\) and \(U\dashv V\). It is invertible and satisfies
\[
e_F\circ V(c_F)\circ(d^{\mathrm{adj}}_{TF})^{-1}
 =\eta_F^{-1}.
\tag{FTC17}
\]
It also makes the corresponding second paired unit–counit composite the identity.

**Proof.** The right-mate formula is obtained by inserting the unit \(\eta\), applying \(c\), and applying the counit \(\bar\eta^{-1}\); these are exactly the three arrows in FTC16. Applying the same formula to \(c^{-1}\) gives its inverse by the two triangle identities. The mate relation on units is
\[
S(c_F)\circ\eta_F
 =d^{\mathrm{adj}}_{UF}\circ e_F^{-1}.
\tag{FTC18}
\]
Naturality of \(d^{\mathrm{adj}}\) for \(c_F:TF\to UF\) rewrites its right side to give
\[
\eta_F
 =d^{\mathrm{adj}}_{TF}\circ V(c_F)^{-1}\circ e_F^{-1}.
\]
Invert this equality to obtain FTC17. Transporting \(V\dashv U\) along \(c,d^{\mathrm{adj}}\) therefore gives \(S\dashv T\) with counit \(\eta^{-1}\). Its triangle identity and the triangle identity for \(T\dashv S\) show that its unit is \(\epsilon^{-1}\); faithfulness of \(S\) cancels \(S\) from that equality. This proves the second assertion. Uniqueness is the mate bijection, not a choice of scalar. \(\square\)

This construction works over all the bases and coefficient rings above whenever the Fourier equivalences and their chosen adjunctions exist. Its relation to the specified literal reversed-halfspace map is computed in [The geometric normalization of Fourier adjunctions](fourier-literal-normalization.md): NDF4–NDF9 prove \(d^{\mathrm{adj}}=\rho d^{\mathrm{lit}}\) when the second orientation comparison is \(\rho\) times positive dual orientation. This later calculation uses the categorical result proved here; it is not a premise of FTC16–FTC18.

## SH02-FTC-LITERAL-SIGN. A test that distinguishes two normalizations

The phrase “reverse the two halfspaces” does not determine an adjunction normalization compatible with every independent choice of orientation comparison. We give an integral rank-one test that detects this issue at the level of the actual maps.

Take \(E=\mathbb R_x\), \(E^*=\mathbb R_y\), with increasing-coordinate orientations, and let
\[
N=\{xy\leq0\},\qquad C=\{xy\geq0\}.
\]
Write \(W_x=\operatorname{or}(\mathbb R_x)[1]\) and \(W_y=\operatorname{or}(\mathbb R_y)[1]\). Keep the shifted orientation factor on the right throughout. For \(L=q^!G\), define the **literal** inverse comparison by the exact chain
\[
\begin{aligned}
SG=Rp_*R\Gamma_NL
&\longrightarrow Rp_*((R\Gamma_NL)_C)\\
&\longleftarrow Rp_!((R\Gamma_NL)_C)\\
&\xrightarrow{\sim}Rp_!R\Gamma_N(L_C)
 \longrightarrow Rp_!L_C=VG.
\end{aligned}
\tag{FTC19}
\]
These arrows are restriction, the support-forgetting comparison on its proper support, the natural support/cut interchange, and forgetting local support. Multiplication of one arrow by a scalar is excluded from this definition. Denote the inverse of FTC19 by \(d^{\mathrm{lit}}:V\to S\).

Choose \(\phi:W_x\to W_y\) and use it to define the second adjunction \(V\dashv U\) by canceling the two relative orientation factors in its Hom calculation. Let \(e_\phi\) be its counit. Set
\[
\Delta_F=e_{\phi,F}\circ V(c_F)\circ
(d^{\mathrm{lit}}_{TF})^{-1}\circ\eta_F.
\tag{FTC20}
\]

**Proposition.** If \(F=\mathbb Z_{\{0\}}\), then \(\Delta_F\) is the scalar by which \(\phi\) differs from the positive coordinate identification. In particular, the negative-definite rank-one identification gives \(-\operatorname{id}_F\).

**Proof.** A small contractible neighborhood with a support whose complement has two contractible components has the relative-cochain model
\[
D^0=\mathbb Z,
\qquad D^1=\mathbb Z\oplus\mathbb Z,
\qquad d(a)=(a,a).
\tag{FTC21}
\]
Use the same homotopy-fiber convention in every occurrence of this model. Its degree-one class \(b=[(1,0)]\) is read with the positive component first. Let \(t_x\) be the value of the actual point-support-to-compact-support trace on \(b_x\otimes o_x[1]\), and define \(t_y\) similarly. Thom and trace make these units in \(\mathbb Z\). Naturality for the positive coordinate isomorphism gives \(t_x=t_y\). Their common value need not be chosen: it will cancel.

The sheaf \(p^{-1}F\) is supported on \(x=0\), lies in both halfspaces, and projects isomorphically to the \(y\)-axis. Thus \(TF=UF=\mathbb Z_{\mathbb R_y}\) and \(c_F\) is the identity. Under the composite kernel adjunction, the unit \(\eta_F\) is the relative \(x\)-Thom morphism followed by inclusion of support
\[
R\Gamma_{\{x=0\}}W_x\longrightarrow R\Gamma_NW_x.
\]
The complement of \(N\) has the two open quadrants \((++),(--)\). Restriction from the two components of \(x\ne0\) to those quadrants preserves their order, so this map sends the unit to \(t_x^{-1}(b_N\otimes o_x[1])\).

Now follow FTC19. Restriction from a small disk to \(C\) preserves the two complement components and induces the identity on both terms of FTC21. The map \(R\Gamma_{\{0\}}\mathbb Z_C\to R\Gamma_N\mathbb Z_C\) is an isomorphism: \(C\setminus\{0\}\) consists of two punctured closed quadrants, and their open quadrant interiors include by homotopy equivalences preserving the two labels. Inverse-image/local-support comparison to the \(y\)-axis takes its positive and negative components to the positive and negative half-axes. It therefore sends \(b_N\) to \(b_y\). These are morphisms of relative-cochain complexes induced by the inclusions of pairs, not identifications chosen from the ranks of their cohomology groups. The middle complex in FTC19 is supported at the origin for this coefficient object, so its proper-support comparison is the identity. Proper-support base change identifies the last integration at \(x=0\) with compactly supported cohomology of the \(y\)-axis. Hence the composite \((d^{\mathrm{lit}}_{TF})^{-1}\eta_F\) is represented by
\[
t_x^{-1}(b_y\otimes o_x[1]).
\tag{FTC22}
\]
No shifted factor has been commuted past a cochain in this calculation.

Finally expand the second adjunction itself. The identity \(\mathbb Z_y\to UF\) transposes before \(p\)-integration to restriction from \(C\) to \(x=0\), with the map \(\phi\) on the right orientation factor:
\[
(W_x)_C\longrightarrow (W_y)_{\{x=0\}}=p^!F.
\]
Its integration is the \(p\)-trace. If \(\phi(o_x[1])=s\,o_y[1]\), the value on FTC22 is \(t_x^{-1}s\,t_y=s\). This proves the proposition. It also explains why an untracked convention for the Thom generator cannot remove the result: that convention enters twice with inverse coefficients. \(\square\)

The same calculation on the zero-section object of an \(n\)-space gives \((-1)^n\) for a negative-definite identification. For the geometric orientation check use positive dual coordinates, set \(u=(x+y)/2\), \(v=(x-y)/2\), and observe that \(C\setminus\{0\}=\{|u|^2\geq|v|^2\}\setminus\{0\}\) retracts onto the punctured positive graph \(x=y\). The strict positive-pairing set retracts onto the same graph. Its projections to the \(x\)- and \(y\)-spaces preserve orientation, as does the map \(y\mapsto y/2\) from the vertical axis into the \(u\)-space. The relative degree-\(n\) class therefore transfers by the positive orientation comparison, with matching trace coefficients cancelling as above. A negative-definite map has determinant sign \((-1)^n\). This remains a calculation on the zero-section test object; it is not a proof that FTC20 has that value on every conic complex.

A consistent antipode transport of FTC19 does not add a scalar to just one endpoint. Negation in the output exchanges the two halfspaces. Viewed on a base-pulled orientation line it is the identity; viewed through the canonical action on a relative dualizing complex it is \((-1)^n\). In the latter convention that same identification is used on both endpoints of the transported comparison, so its two scalar factors cancel by conjugation. Inserting it on only one endpoint would define a different comparison and must be stated as such.

Consequently the literal chain and the negative-definite second adjunction do not satisfy FTC17 in odd rank over the integers. NDF4 extends the literal defect calculation to the full conic category, and NDF5–NDF10 prove that \(d^{\mathrm{adj}}=(-1)^n d^{\mathrm{lit}}\) is the unique comparison realizing both normalized inverse equations. The counterexample tests the explicitly defined literal chain and second adjunction; the corrected comparison is identified by the computed scalar and the uniqueness proof.

## SH02-FTC-PROBLEMS. Tests of what the proof does and does not say

**Problem 1.** Explain why the compactification FTC7 does not prove arbitrary nonproper base change for \(Rf_*\).

**Solution.** It factors one base map as an open inclusion followed by a proper map. The open lemma uses the restriction adjunction and the particular map \(j_!\to Rj_*\). It makes no assertion that pulling \(Rj_*\) through a closed inclusion is invertible. The proper factor uses proper base change under its actual properness hypothesis. Their combination proves only the comparison square FTC6 for a Fourier functor already known to commute with these base operations.

**Problem 2.** For \(b:(0,1)\hookrightarrow\mathbb R\), take a rank-zero bundle and the constant sheaf \(k\). Is the square FTC6 a square of isomorphisms?

**Solution.** Fourier is the identity in rank zero, so the square is the map \(b_!k\to Rb_*k\) on both rows. At \(0\) the first stalk is zero and the second has \(k\) in degree zero. For nonzero \(k\), the horizontal arrows are not isomorphisms. The vertical operation comparisons and the equality of the horizontal maps remain valid. Commuting with a comparison does not make the comparison invertible.

**Problem 3.** Why does the construction FTC16 not by itself prove equality with a separately specified halfspace comparison?

**Solution.** FTC16 defines a comparison from the fixed adjunctions and \(c\); its triangle identities prove FTC17 for that comparison. A separately specified literal map still requires an actual comparison calculation. NDF4 supplies that calculation on the full conic category and NDF5–NDF9 give \(d^{\mathrm{adj}}=\rho d^{\mathrm{lit}}\), with \(\rho=(-1)^n\) for the negative-definite orientation choice. Thus equality with the literal map holds exactly where that scalar is one. NDF10 uniquely characterizes the comparison satisfying the normalized inverse equations, once the first comparison and both adjunctions have been fixed.

## SH02-FTC-STATUS. Exact continuation boundary

This supplement supplies the base support-comparison theorem, the base relative-trace theorem, the composition reduction of both microlocal trace obligations to their fibre-linear equations, an explicit adjunction-normalized replacement construction, and an integral counterexample to combining the literal reverse chain with the negative-definite second adjunction. The complete support equation FTC13b is proved in SH02-FGC-SUPPORT with its explicit initial and final line conventions. Its propagation to the microlocal support square and the corresponding trace square is proved in SH02-MEP-SUPPORT and SH02-MEP-TRACE, with the exact adjoint endpoint supplied by SH02-MEP-MATE-UNTWIST. The complete trace equation FTC14 is proved in SH02-FTE-TRACE using the unchanged raw Fourier adjunctions and the explicit R3/R4 line maps. NDF10 constructs the unique opposite comparison satisfying the normalized paired inverse equations and identifies it with FTC16; NDF4–NDF9 compute its exact relation to the literal map. These results retain the named operation prerequisites at their stated scope.

**Published source and proof mechanism.** [Kashiwara–Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §2.1.1–2.1.2, printed pp. 39–41 (PDF pp. 42–44), provides bounded-below vector-bundle Fourier presentations, inverse equivalences, linear functoriality and the four base-map exchanges of Proposition 2.1.6. This section recalls results without proofs. Its exchange statements alone do not prove FTC6, FTC10, FTC13b or FTC14: these are equalities involving the actual support-forgetting map, the actual trace counit and specified orientation-line contractions.

The proof of FTC6 starts with the open-inclusion adjunction characterization of support forgetting, handles a proper base map with proper-support base change, and pastes those maps through the graph compactification. Composition of support inclusions specifies the pasted morphism; no nonproper ordinary-image base-change isomorphism is inferred. For FTC10, FTC9a–FTC9b define exceptional exchange by its mate and counit equation. Transposing the two proposed trace maps then gives the same base trace, with the bundle orientation line kept in the stated position. FTC13b and FTC14 require the additional FGC and FTE ordered-line calculations; reducing to them does not discard their relative-rank signs or their rank-jumping cases. Finally FTC16–FTC18 are a categorical construction and proof, while FTC19–FTC22 compute the distinct literal comparison by relative cochains. These are separate mechanisms and both are needed to identify the normalized map.

The sheaf-operation comparison used for this account is [Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026 version](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf): Theorem 4.5.3 and equation (4.5.4), p. 93, for proper-support base change and its fibre formula; Theorem 4.6.1 and Corollary 4.6.2, pp. 94–95, for dimension-bounded exceptional adjunction and transitivity; the relative-dualizing comparison (4.7.4), p. 97, for the map built by projection formula and trace; and Proposition 5.1.9, pp. 107–108, for the local product orientation mechanism. The comparison in (4.7.4) places the orientation object on the right, whereas FTC2 places it on the left and explicitly includes the required symmetry. The printed projection formula, Theorem 4.4.7, p. 91, does not by itself supply the two-bounded-below form: SH02-FF-BOUNDS supplies the degreewise truncation argument, and the finite exceptional-operation bounds remain required. Definition 5.4.5 and Theorem 5.4.6, p. 114, supply a bounded manifold-base Fourier comparison, not a proof of this lesson's ordered natural transformations in the full stated range. The independently written course text is under CC0; these human sources retain their own terms.
