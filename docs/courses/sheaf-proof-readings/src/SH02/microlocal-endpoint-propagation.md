# SH02-MEP-UNIT. Following the comparison maps into the normal bundle

Independently expressed programme text is dedicated under CC0 1.0 Universal. This lesson follows the Fourier operation comparisons through normal deformation and identifies their support and trace endpoints. The source account compares the classical microlocalization squares with the additional orientation, module and adjunction calculations required for the specified course maps.

## SH02-MEP-SOURCES. Classical squares and their specified endpoints

Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Propositions 2.2.2–2.2.3, printed pp. 44–46, construct direct and inverse specialization comparisons on the normal deformation and prove the inverse square by base-change maps. Propositions 2.3.4–2.3.5, p. 48, transport them to microlocalization using the linear and base Fourier exchanges of Propositions 2.1.5–2.1.6, p. 41. This is the geometric and functorial framework shared by the present proof. Section 2.1 explicitly supplies statements without proofs; these citations do not prove the raw Fourier adjunction or determine every tensor-order convention used below.

For the underlying sheaf operations, the compared edition of Pierre Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), dated 01/08/2026, §§4.5–4.7, pp. 92–97, treats proper base change, exceptional adjunction, composition, invertible-coefficient comparison and relative trace. Its §5.1, pp. 107–108, give orientation complexes and the submersion orientation formula by local product reduction. These are relevant mechanisms for the coefficient and trace maps here. The passage invoking a separate representability proof is a dependency, not a proof supplied by this comparison, and references from these notes to other books have not been followed.

SH02-MEP-ORIENTATION specifies the normal orientation through ordered tangent exact sequences and the positive deformation parameter. O13 is identified by its actual adjunct: proper base change followed by the counit for the two time submersions. The proof pastes the positive and central squares and extracts only an invertible coefficient. It never asserts a purity isomorphism for every sheaf under an arbitrary map, and does not require the normal derivative to be invertible. O14 then compares the trace with that specified central orientation. This explains which orientation map the classical deformation comparison uses in the course normalization.

The four Fourier endpoints are subsequently written in their original tensor order. PM1–PM17 use the actual equivalence unit, counit, right-Hom transpose and module-mate square to obtain the signed uncontracted identity MEP16. MEP17–MEP20 contract that identity with the coherent orientation pairing and recover the braided endpoint. The rank-one computation tests the sign; the full adjunction calculation proves it for every object in the declared category. The corrected unsigned target was an earlier course claim. No erratum in a human source is asserted, and the exact course parity formula is not presented as a quotation or an unprinted recipe from Astérisque 128.

MEP11 identifies the support half by composing specialization, linear exchange and base exchange. MEP14 identifies the trace half using the original ordinary and exceptional inverse Fourier comparisons, with the relative trace on the actual invertible source coefficient. Thus the proof concerns specified natural transformations, rather than only isomorphic endpoints. Its linear input retains conic bounded-below complexes with a global lower bound over locally compact Hausdorff bases, including rank-jumping bundle maps; the subsequent microlocal application uses bounded arbitrary sheaves on manifolds. The source account does not silently narrow either scope to constructible objects or constant-rank kernels.

The organization is normal orientation, four endpoints, the module-mate calculation, and the two assembled squares, followed by three solved checks. The cited sources supply the classical framework and operation mechanisms; the detailed endpoint word and sign calculation are expressed through the separately named programme proofs. Those suppliers retain their own foundation obligations. Human source expression and diagrams are not imported or relicensed, and no claim is made that every transitive prerequisite is proved.

## SH02-MEP-SCOPE. Domains and the finite proof inputs

For microlocalization let \(k\) be a commutative unital ring of finite global dimension. Manifolds are finite dimensional, Hausdorff and countable at infinity, and complexes are in \(D^b\) of arbitrary sheaves of \(k\)-modules. A map of manifolds need not be a submersion. Let \(f:(Y,N)\to(X,M)\) be a map of pairs of smooth manifolds, with closed embedded submanifolds and \(f(N)\subset M\). The locally closed case is obtained by the restriction identifications already used in specialization. There is no assumption that \(N=f^{-1}M\).

Write \(g=f|_N\), \(E_1=N_NY\), \(E_2=g^{-1}N_MX\), and factor the normal derivative as
\[
E_1\xrightarrow h E_2\xrightarrow b N_MX.
\tag{MEP1}
\]
The dual correspondence is
\[
E_1^*\xleftarrow r E_2^*\xrightarrow s N_M^*X,
\qquad r={}^th.
\tag{MEP2}
\]
These are the positive transpose maps: \(\langle h(v),\xi\rangle=\langle v,r(\xi)\rangle\). The letter \(q\) will mean \(bh\), and \(u:E_2^*\to N\) is the bundle projection.

The linear inputs used here are the full theorems for a continuous bundle map over an arbitrary locally compact Hausdorff base, on conic \(D^+\) with a single global lower bound. They include nonorientable bundles, arbitrary coefficient modules and rank-jumping maps. No constant-rank kernel bundle is introduced. Bundle ranks are finite; locally constant ranks are allowed componentwise only when all required cohomological bounds remain global. Those input theorems are not narrowed to the manifold case in which we subsequently apply them.

Here is the sufficient proof cut. Each entry supplies the indicated map, not merely its isomorphism class.

| Input | Exact use |
|---|---|
| SH02-FF-LINEAR-KERNEL and SH02-FF-BASE | The negative-cut primitive exchange \(A_h\), and the base exchanges with their ordinary and exceptional mates |
| SH02-FF-CONVENTIONS and SH02-FF-MATES | The raw Fourier units and counits, FF3a, the original R2 and R4 maps, and the coherent initial L3 extraction FF11b |
| SH02-FGC-SUPPORT | FTC13b with the final braided evaluation specified in FTC13a |
| SH02-FTE-TRACE | FTE34, the original R2/R4 trace equation on every conic bounded-below object |
| SH02-FTC-BASE-SUPPORT and SH02-FTC-BASE-TRACE | FTC6 and the base relative-trace square, including its counit characterization FTC9a–FTC9b |
| SH02-SP-DIRECT, SH02-SP-INVERSE and SH02-SP-ADJUNCTION | The deformation comparison maps, their two commuting squares and their adjunction identities |
| SH02-SP-TWISTS and SH02-SP-ORIENTATIONS | Transport of the invertible coefficient and the orientation identification fixed by normal tangent sequences and the positive parameter |
| SH02-MD-TRACE, M28 | Counit-normalized exceptional base change for the two time submersions, used only to identify the normal orientation map |
| The declared six-operation contracts | Proper-support composition and base change, projection formula, bounded exceptional adjunction, module compatibility, and the corresponding unit/counit pasting identities |

No result about field coefficients, finite stalks, constructibility, Verdier biduality or compact support of an input object is used. A proof of the map calculation does not by itself prove the results listed in the table above.

## SH02-MEP-ORIENTATION. The normal orientation is a specified trace map

Put \(W_1=O_{E_1}[c_Y]\), \(W_2=O_{E_2}[c_X]\), where \(c_Y,c_X\) are the normal bundle ranks. Let \(\Omega=\omega_h\) and \(K=\omega_r\), with base pullbacks understood. The relative-line identifications are characterized by
\[
d_h:\Omega\otimes W_2\longrightarrow W_1,
\qquad d_r:K\otimes W_1\longrightarrow W_2.
\tag{MEP3}
\]
They are the exceptional-transitivity maps FF3a, with positive dual orientations. Both are maps of graded lines. They are not choices of a scalar after choosing bases.

In particular the coherent inverse pairing between \(\Omega\) and \(K\) is fixed by the requirement that, after right tensoring by \(W_1\), it be
\[
\Omega\otimes K\otimes W_1
\xrightarrow{1\otimes d_r}\Omega\otimes W_2
\xrightarrow{d_h}W_1.
\tag{MEP4}
\]
Right tensoring by \(W_1\) is faithful and an equivalence. Hence MEP4 uniquely fixes the pairing and the corresponding identification \(\Omega\simeq K^\vee\), including its scalar and shift. Every conversion below between those two lines uses this identification. If \(\Omega^\vee\) is identified with \(K\) by PM3 below, MEP4 on \(\Omega\otimes\Omega^\vee\) is inverse coevaluation. It must not be substituted for the left-tensor internal-Hom counit, whose forward-ordered contraction is braided evaluation and differs by the parity of \(\Omega\).

The relative orientations of the composite maps use the unique right-tensor extraction of exceptional transitivity, with its counit normalization, as in FF3a. In particular the composite \(h^!b^!k\simeq q^!k\), preceded by the trace-compatible extraction \(\theta_h(\omega_b)\), fixes the ordered line map for \(q\). The normal tangent exact sequences are ordered with tangent directions to the submanifold before normal directions. The determinant representatives of these fixed maps give
\[
\omega_q\simeq \tau_1^{-1}j^{-1}\omega_f,
\qquad
\omega_b\simeq\tau_2^{-1}\omega_g,
\qquad
\omega_s\simeq u^{-1}\omega_g.
\tag{MEP5}
\]
Here \(j:N\hookrightarrow Y\). To check the first map, choose a local splitting of each normal exact sequence. The orientation of the total normal bundle is the ordered product of the tangent orientation of its base and its normal orientation, exactly as for the ambient tangent bundle restricted to the submanifold. The shifts agree because \(\dim E_1=\dim Y\) and \(\dim N_MX=\dim X\). Changing the splitting acts by an upper triangular matrix with identity diagonal on the associated graded spaces, hence has determinant one. Changing frames multiplies both descriptions by the same orientation transition functions. Thus the map is independent of these choices and glues without an orientability hypothesis.

The identification with the deformation trace is proved in SH02-MEP-NORMAL-COUNITS below. That proof uses the time submersions and their counit-normalized base-change maps; it does not assume that the normal derivative has an invertible tangent matrix.

There is a useful counit check for the second and third maps of MEP5. For the bundle base-change square, let
\(\chi:Rb_!\tau_2^{-1}\to\tau_X^{-1}Rg_!\) be proper-support base change. The lift of the base orientation is the exceptional adjunct of
\[
Rb_!\tau_2^{-1}\omega_g
\xrightarrow\chi \tau_X^{-1}Rg_!\omega_g
\xrightarrow{\tau_X^{-1}\operatorname{tr}_g}k.
\tag{MEP6}
\]
On a bundle trivialization, exceptional transitivity cancels the same fibre orientation evaluation on the right. The coefficient map left over is exactly \(\operatorname{tr}_g\), so this adjunct is the line map in MEP5. Frame changes affect the two cancelled copies equally; this identifies the actual maps globally. The same proof applies to the dual bundle and \(s\). This is the content of the explicit counit square FTC9b and also explains why an unspecified orientation isomorphism would not suffice here.

## SH02-MEP-NORMAL-COUNITS. The central orientation and the actual counit

This compatibility is stronger than the equality of orientation line types. Write \(E_Y=E_1\), \(E_X=N_MX\), \(\Omega_P=p_P^!k\), and let \(\kappa_q:\tau_1^{-1}j^{-1}\omega_f\to\omega_q\) denote the normal map MEP5. A base-changing exceptional comparison is denoted by \(\gamma\); every such map below is the mate of proper-support base change. Let
\(\widetilde f:D_NY\to D_MX\) be the deformation map over the same real time coordinate \(t\), let \(\sigma_Y,\sigma_X\) denote the central inclusions, and let \(\jmath_Y,\jmath_X\) denote the positive open inclusions. Its positive restriction is \(f\times1_{\mathbb R_{>0}}\), and its central restriction is \(q\).

Put the positive time direction last in both deformation orientation frames. In a normal chart, passage from central coordinates to the positive ambient chart is
\((n,v,t)\mapsto(n,tv,t)\). On \(t>0\) its determinant in the normal directions is \(t^{c_Y}>0\), and similarly \(t^{c_X}>0\) on the target. Thus its orientation comparison restricts at the centre to the ordered exact-sequence map MEP5 and in the positive chamber to the ambient orientation map. Both comparisons cancel the same positive time factor. Every interchange of shifted factors is the symmetry already used in MEP3–MEP6; the positivity of \(t^c\) is not a license to omit such a symmetry.

The central square is Cartesian because the deformation map preserves \(t\). Its exceptional comparison
\[
\gamma:\sigma_Y^{-1}\widetilde f^!K
 \longrightarrow q^!\sigma_X^{-1}K
\]
is defined as the adjunct of
\[
Rq_!\sigma_Y^{-1}\widetilde f^!K
 \xrightarrow{\rm BC}\sigma_X^{-1}R\widetilde f_!\widetilde f^!K
 \xrightarrow{\sigma_X^{-1}\epsilon_{\widetilde f}(K)}
 \sigma_X^{-1}K.                                                  \tag{O13}
\]
Here is a proof that O13 at \(K=k\) is the specified orientation isomorphism, using only base change for submersions. Let \(t_Y:D_NY\to\mathbb R\) and \(t_X:D_MX\to\mathbb R\) be the two time submersions. They satisfy \(t_X\widetilde f=t_Y\). Pulling each of them back to \(0\in\mathbb R\) gives the central fibre projection to a point. The trace-normalized submersion theorem (SH02-MD-TRACE, equation M28) therefore supplies isomorphisms
\[
\gamma_{t_Y}:\sigma_Y^{-1}\omega_{t_Y}\xrightarrow{\sim}\Omega_{E_Y},
\qquad
\gamma_{t_X}:\sigma_X^{-1}\omega_{t_X}\xrightarrow{\sim}\Omega_{E_X}.
\]
Exceptional mate pasting, which follows by transposing the proper-support base-change pasting identity, gives
\[
\gamma_{t_Y}
 =
q^!(\gamma_{t_X})\,
\gamma_{\widetilde f}(\omega_{t_X})
\]
after the exceptional transitivity identifications
\(\widetilde f^!\omega_{t_X}=\omega_{t_Y}\) and
\(q^!\Omega_{E_X}=\Omega_{E_Y}\).
In particular \(\gamma_{\widetilde f}(\omega_{t_X})\) is invertible.

The exceptional comparison is compatible with invertible coefficient extraction: this follows by transposing its two module routes, when both are proper-support base change, projection formula and the same counit. Thus, after extracting the invertible factor \(\sigma_X^{-1}\omega_{t_X}\), the last equality says that \(\gamma_{\widetilde f}(k)\) is the unique relative-orientation map whose tensor on the right makes the orientation transitivity square commute. This is exactly the prescription MEP3–MEP6. Tensoring by that invertible factor is an equivalence, so it also proves that \(\gamma_{\widetilde f}(k)\) is invertible.

The submersion orientation maps used here come from the same ordered fibre compact-support generators. In the positive chamber their frames are the ambient frames and in the central fibre they are the normal frames; the positive chart determinant \(t^c\) identifies them by MEP5. Hence their right-tensor extraction is precisely MEP5. Only the time projections were required to be submersions. This argument neither assumes that \(q\) or \(\widetilde f\) is a submersion nor asserts purity for a general nontransverse square.

The definition O13 proves its trace equation, including coefficients, by the adjunction bijection. For an invertible orientation factor the coefficient extraction is the invertible-line extraction; thus it uses the orientation comparison already fixed, not a second isomorphism chosen after base change. The positive open square has the same property: exceptional exchange is the mate of its proper-support base-change map, so its counit equation is built into that mate.

Now construct the specialization inverse comparisons \(\alpha\) and \(\beta\) by these positive and central squares, as in SH02-SP-INVERSE. Tensor the positive ordinary base-change map by the deformation relative orientation. Take the adjunct first through \(R\widetilde f_!\dashv\widetilde f^!\), then through \(\jmath_X^{-1}\dashv R\jmath_{X*}\). The two proposed trace routes both become projection formula followed by the trace of \(f\times1_{\mathbb R_{>0}}\); their inserted open unit/counit pairs cancel. Restrict this equality to the centre and apply O13. The remaining trace is the counit of \(q\), with MEP5, by the defining adjunct equation O13. This gives
\[
\theta_q\circ(\kappa_q\otimes1)
 =
\beta\circ\nu_N(\theta_f)\circ
  \bigl(\text{twist comparison followed by }\alpha\bigr),           \tag{O14}
\]
as an equality with source
\(\tau_Y^{-1}j^{-1}\omega_f\otimes q^{-1}\nu_MF\).
Writing the upper arrow in the opposite direction of the twist identification gives exactly SH02-SP-INVERSE-SQUARE.

This does not say that \(\operatorname{tr}_q\) is an ordinary pullback of \(\operatorname{tr}_f\) along the non-Cartesian normal-bundle square. The equality uses the deformation, its genuinely Cartesian time and open squares, and their actual counits.

## SH02-MEP-ENDPOINTS. Record the four exchange maps before pasting

Use \(T_1,T_2,T_X\) on \(E_1,E_2,N_MX\), respectively. Denote the linear maps by
\[
A_h:r^{-1}T_1\longrightarrow T_2Rh_!,
\qquad E_h:T_1h^!\longrightarrow Rr_*T_2,
\qquad D_h:T_1(\Omega\otimes h^{-1}(-))\longrightarrow Rr_!T_2.
\tag{MEP7}
\]
The first is the negative-cut primitive FF4. The second is original R2. The third is original R4, with its prescribed input orientation rewrite; it is not replaced by a normalization defined to force a square to commute.

Let \(\ell_h:r^!T_1\to T_2Rh_*\otimes K\) be FF L3 with its coherent initial FF11b extraction. Put \(D=K^\vee\). The complete support endpoint is
\[
B_h=(1\otimes\operatorname{ev}_K\sigma_{K,D})
(\ell_h\otimes1_D):r^!T_1(-)\otimes D\longrightarrow T_2Rh_*.
\tag{MEP8}
\]
The final contraction is braided evaluation. The initial insertion in \(\ell_h\) remains coevaluation. Replacing only the final contraction by inverse coevaluation gives a different endpoint when \(c_X-c_Y\) is odd. This distinction persists after a base change; a base exchange cannot erase it.

Write \(P_b:T_XRb_!\to Rs_!T_2\) and \(S_b:T_XRb_*\to Rs_*T_2\) for the proper and ordinary base exchanges. The first and fourth normal exchanges, with their directions fixed, are
\[
\begin{aligned}
I_q^!&=(Rs_!A_h^{-1})P_b:
T_XRq_!\longrightarrow Rs_!r^{-1}T_1,\\
I_q^*&=(Rs_*B_h^{-1})S_b:
T_XRq_*\longrightarrow Rs_*(r^!T_1\otimes D).
\end{aligned}
\tag{MEP9}
\]
The inverse exceptional normal exchange uses original \(E_h\) after the exceptional base exchange. The oriented ordinary inverse exchange uses original \(D_h\) after ordinary base pullback. To give these endpoints without shorthand, put \(Q_H=\omega_b\otimes b^{-1}H\), \(J_H=b^!H\), and let \(d_{h,b}:\Omega\otimes h^{-1}\omega_b\to\omega_q\) be the trace-compatible transitivity map. Let
\[
a_H:T_2Q_H\longrightarrow\omega_s\otimes s^{-1}T_XH,
\qquad e_H:T_2J_H\longrightarrow s^!T_XH
\tag{MEP10a}
\]
be the base exchanges, with the MEP6 orientation map and the fixed left-line module symmetry. The full endpoints are
\[
\begin{aligned}
\Phi_H^{\mathrm{in}}&=Rr_!(a_H)D_h(Q_H)T_1(d_{h,b}^{-1}\otimes1),\\
\Phi_H^{\mathrm{out}}&=Rr_*(e_H)E_h(J_H)T_1(q^!H\simeq h^!b^!H).
\end{aligned}
\tag{MEP10b}
\]
In particular the first has domain identification
\[
T_1(\omega_q\otimes q^{-1}H)
\simeq Rr_!(\omega_s\otimes s^{-1}T_XH).
\tag{MEP10}
\]
All these identifications include associativity and symmetry of the base module structure. The line \(\omega_s\) remains a local system on the correspondence, rather than a chosen global module.

MEP9 specifies a completed fourth row. SH02-MEP-MATE-UNTWIST below proves that this is exactly the right mate of the original third row after the stated untwisting. The proof checks its tensor–Hom counit; it does not infer the conclusion from common endpoint objects.

## SH02-MEP-PRECISE-MATE. The right mate has a relative-rank sign

Keep the original FF R4 map

\[
D_h:T_1(\Omega\otimes h^{-1}H)\longrightarrow Rr_!T_2H,
\qquad \Omega=\omega_h,
\tag{PM1}
\]

and the original FF L3 map \(\ell_h:r^!T_1F\to T_2Rh_*F\otimes K\), where \(K=\omega_r\), with the coherent initial FF11b extraction. The transpose of \(h:E_1\to E_2\) is \(r:E_2^*\to E_1^*\). Set \(A=W_1\), \(B=W_2\), \(D=\Omega^\vee\), and \(\varepsilon=(-1)^{n_1-n_2}\).

Take the actual right mate of PM1, conjugate it by the original \(T_i\dashv Q_i\) unit/counit as in PA31, and identify
\(R\mathcal Hom(\Omega,F)\) with \(F\otimes D\) by its **right-ordered tensor–Hom map** specified in PM4 below. Move this right line through \(Rh_*\) and \(T_2\), and identify \(D\) with \(K\) by PM3. Call the resulting map \(\mu_h\). Then

\[
\boxed{\mu_h=\varepsilon\ell_h.}
\tag{PM2}
\]

The course's previously unproved shorthand PA32 asked for the unsigned equality. With this actual right-ordered extraction it is false as an assertion \(\mu_h=\ell_h\) in general. The discrepancy is a natural scalar on the full category, not a restriction to a test object. Combined with the independently proved FGC2, this says \(\mu_h=G_h\), the direct support comparison. The coherent final contraction of \(\mu_h\) is the **braided** final contraction of \(\ell_h\).

The base is any locally compact Hausdorff space. Bundles have fixed finite ranks, or locally constant ranks on components with the required global bounds. The map is continuous and fiberwise linear, including rank jumps. Coefficients are all modules over a commutative unital ring of finite global dimension. Inputs are the full conic globally bounded-below derived categories with parameter-space scalar transport. No upper bound, constructibility, finite stalk generation, field, orientability, manifold-base, or properness hypothesis is added. Exceptional adjoints exist because the bundle ranks bound proper-support cohomological dimension on abelian sheaves. All new tensor factors are bounded invertible lines. Empty bases and rank zero cause no exception. Over the zero ring every displayed map is the unique map; nontriviality of the discrepancy is witnessed over \(\mathbb Z\).

## SH02-MEP-MATE-LINES. Specify the right internal-Hom map

Let \(d:\Omega\otimes B\to A\) be exactly FF3a and put

\[
c:D\otimes A\xrightarrow{1\otimes d^{-1}}D\otimes\Omega\otimes B
 \xrightarrow{\operatorname{ev}_{\Omega}\otimes1}B.
\tag{PM3}
\]

Let \(d_r:K\otimes A\to B\) be FF3a for the transpose. The identification \(D\to K\) used here is the unique map \(\iota\) for which \(d_r(\iota\otimes1_A)=c\). Tensoring by \(A\) is faithful and an equivalence, so this is an exact specification, without a choice of an orientation generator. Subsequently write \(D=K\) using this map. In particular \(|D|=|A|+|B|\) modulo two.

For \(g:\Omega\otimes X\to F\), the right-ordered transpose is

\[
\bar g=(g\otimes1_D)(\sigma_{X,\Omega}\otimes1_D)
 (1_X\otimes u_{\Omega}):X\longrightarrow F\otimes D,
\qquad u_{\Omega}:k\longrightarrow\Omega\otimes D.
\tag{PM4}
\]

This is the right-line transpose used in SH02-LFT-LINE-ORDER. Indeed first change the source to \(X\otimes\Omega\) by symmetry and then apply the usual right-tensor adjunction. It defines the isomorphism \(R\mathcal Hom(\Omega,F)\to F\otimes D\) on every Hom set. Its counit on \(\Omega\otimes F\otimes D\) braids \(\Omega\) past \(F\), then contracts \(\Omega\otimes D\) by \(\operatorname{ev}_{\Omega}\sigma_{\Omega,D}\). Replacing that last contraction by \(u_{\Omega}^{-1}\) changes the map by \(\varepsilon\).

The duality triangle gives

\[
(1_{\Omega}\otimes c)(u_{\Omega}\otimes1_A)=d^{-1}.
\tag{PM5}
\]

Consequently, if
\(\lambda_X=(\sigma_{X,\Omega}\otimes1_B)(1_X\otimes d^{-1})\), then

\[
(1_F\otimes c)(\bar g\otimes1_A)=(g\otimes1_B)\lambda_X:
X\otimes A\longrightarrow F\otimes B.
\tag{PM6}
\]

To verify PM6, insert PM4 on its left. Naturality moves \(c\) past \(g\); the adjacent \(u_{\Omega}\) and \(c\) then give PM5. The remaining symmetry is exactly \(\sigma_{X,\Omega}\). This proves the identity without any assertion about the degrees of \(X\) or \(F\).

## SH02-MEP-MATE-HOM. The actual adjunction bijections

Write \(U=h^{-1}\), \(R=Rr_!\), \(U^R=Rh_*\), and \(R^R=r^!\). Let \(P_i=T_{E_i^*}\) and \(V_i=a^{-1}T_i(-)\otimes W_i\). Retain the original adjunction \(P_i\dashv V_i\) with unit \(u_i\) and counit \(v_i\). The primitive transpose kernel map is

\[
a:UP_2\longrightarrow P_1R.
\tag{PM7}
\]

The original R1 is

\[
C_H=u_1^{-1}\,V_1(a_{V_2H})\,V_1U(v_{2,H}^{-1}):
V_1UH\longrightarrow RV_2H.
\tag{PM8}
\]

The original L2 is the right mate \(b:R^RV_1\to V_2U^R\) of PM7. For arbitrary \(H,F\), it has the following exact characterization: the map

\[
\operatorname{Hom}(RV_2H,V_1F)\longrightarrow
\operatorname{Hom}(H,U^RF)
\tag{PM9}
\]

induced by \(b\), the \(R\)-adjunction and the fully faithful functor \(V_2\), is precomposition with \(C_H\), followed by the fully faithful \(V_1\) identification and the \(U\)-adjunction.

Here is the verification with the actual Fourier maps. For \(f:RV_2H\to V_1F\), the \(P_1\)-adjunct is \(v_{1,F}P_1f\). Precompose it with \(a_{V_2H}\) and then with \(U(v_{2,H}^{-1})\). This gives
\(v_{1,F}P_1f\,a_{V_2H}\,U(v_{2,H}^{-1}):UH\to F\).
On the other route, apply \(P_1\) to \(fC_H\), conjugate by \(v_1\), and substitute PM8. The identity
\(P_1u_1^{-1}=v_1P_1\), followed by naturality of \(v_1\) for \(a\) and \(U(v_2^{-1})\), cancels the intervening factors and gives exactly that same expression. This is the triangle identity, not an identification of two inverse functors by their objects. Ordinary \(U\)-adjunction finishes PM9. Because \(V_2\) is an equivalence, these Hom sets determine \(b\) on all coefficients.

Canceling the output antipodes in PM8 gives a map

\[
\widetilde C_H:T_1UH\otimes A\longrightarrow R(T_2H\otimes B).
\tag{PM10}
\]

Canceling them in \(b\) gives FF11,

\[
\widetilde\ell_F:r^!T_1F\otimes A\longrightarrow T_2Rh_*F\otimes B.
\tag{PM11}
\]

These cancellations mean the actual ordinary antipode exchange in PM10 and its exceptional mate in PM11. The exceptional exchange is retained on its arbitrary coefficient; it is not replaced by its action on \(k\). Taking the proper-support adjunct of the coordinate-change square verifies that these exchanges are mates. The two adjunct routes are the same coordinate pullback followed by its counit; the inserted unit and counit cancel by the triangle identity. Hence PM9 remains valid after these cancellations and right-line projection formulas. FTE-A2 and FTE-A7 use this same compatibility; their mention compares the calculations rather than adding premises to this derivation.

In this notation the two defining orientation rewrites are exactly

\[
\widetilde C_H=(D_h(H)\otimes1_B)\lambda_{UH},
\qquad
\widetilde\ell_F=(1\otimes c)(\ell_h(F)\otimes1_A).
\tag{PM12}
\]

The usual right-line projection formulas of \(T_1\) and \(R\) are understood on the first equality. Its source symmetry and \(d^{-1}\) are precisely the R1-to-R4 rewrite in SH02-FF-MATES, with its input identification checked in FTE33. The second equality is equivalent to coherent FF11b extraction: tensor it by the inverse of \(A\) and use the unit/counit triangles. In particular no braided final contraction has been inserted into FF11b.

## SH02-MEP-MATE-CONJUGATION. Keep both Fourier conjugating arrows

Let \(m:Q_2r^!\to Rh_*R\mathcal Hom(\Omega,Q_1(-))\) be the right mate of PM1. If \(\eta_i:1\to Q_iT_i\) and \(\epsilon_i:T_iQ_i\to1\) are the original Fourier unit and counit, the unconsolidated PA31 conjugation is

\[
\gamma_F=
T_2Rh_*R\mathcal Hom(\Omega,\eta_{1,F}^{-1})
\;T_2m_{T_1F}\;\epsilon_{2,r^!T_1F}^{-1}:
r^!T_1F\longrightarrow T_2Rh_*R\mathcal Hom(\Omega,F).
\tag{PM13}
\]

Thus the specified inverse counit is first and the specified inverse unit is last, with the order prescribed in the preceding definition. Follow PM13 by PM4 and right-line extraction to obtain \(\mu_F:r^!T_1F\to T_2Rh_*F\otimes D\).

Equivalently, for any \(f:RT_2H\to T_1F\), its \(R\)-adjunct followed by \(\mu_F\) corresponds to the following map. Precompose \(f\) with \(D_h(H)\), use full faithfulness of \(T_1\) to obtain \(g:\Omega\otimes UH\to F\), apply PM4 to obtain \(\bar g:UH\to F\otimes D\), and take the ordinary \(U\)-adjunct. Applying \(T_2\) and extracting \(D\) gives the claimed target. This is exactly the defining Hom bijection for the composite right mate PM13; expanding that bijection gives its three displayed factors. It is not an extra convention for a mate.

Put \(Y_F=r^!T_1F\), \(Z_F=T_2Rh_*F\). Apply PM9 after canceling antipodes, with the coefficient \(F\otimes D\) in place of \(F\). PM6 says that the route obtained from precomposition with \(D_h\) and right-Hom transposition is exactly precomposition with \(\widetilde C\), after the target change
\((F\otimes D)\otimes A\xrightarrow{1_F\otimes c}F\otimes B\).
Yoneda and PM13 therefore give

\[
\mu_F\otimes1_B=
\widetilde\ell_{F\otimes D}\,(1_{Y_F}\otimes c^{-1}):
Y_F\otimes B\longrightarrow Z_F\otimes D\otimes B.
\tag{PM14}
\]

On the right, the source \(Y_F\otimes D\otimes A\) is identified with \(r^!T_1(F\otimes D)\otimes A\), and the target uses \(T_2Rh_*(F\otimes D)=Z_F\otimes D\), by their actual right module maps. Every conversion has now been specified.

## SH02-MEP-MATE-MODULE. Follow the two copies of the relative line

The primitive PM7 commutes with a right base-line factor by its pullback, proper-image base-change and projection-formula definition. Its right mate commutes with the induced module maps. A right module map for \(V_i=a^{-1}T_i(-)\otimes W_i\) first extracts the coefficient line from \(T_i\), then moves it past the rightmost \(W_i\). Both movements are prescribed; the second is a Koszul symmetry. The exceptional antipode exchange commutes with a base-line coefficient by taking its proper-support adjunct. Therefore, for any bounded invertible base line \(C\),

\[
\widetilde\ell_{F\otimes C}=
(1_{Z_F}\otimes\sigma_{B,C})
(\widetilde\ell_F\otimes1_C)
(1_{Y_F}\otimes\sigma_{C,A}),
\tag{PM15}
\]

under the right projection formulas. Its source is \(Y_F\otimes C\otimes A\); its target is \(Z_F\otimes C\otimes B\). This is the module-mate square itself, not an assumption that the line on the right of a Fourier functor can cross its fixed orientation for free. The raw right kernel retains its rightmost orientation, and every reverse-FS6 arrow is a module map for that structure: localization and support inclusion are natural in the coefficient, while each image arrow is its specified projection formula. FTE10 is the same verification with the dual-bundle indices; its mention compares the calculations rather than adding a proof input.

Apply PM15 with \(C=D\) to PM14 and insert the second equality in PM12. Naturality moves \(\ell_h(F)\) ahead of the pure line word. There remain two routes from \(D_0\otimes D_1\otimes A\) to \(D\otimes B\):

\[
\begin{aligned}
p&=\sigma_{B,D}\,(c\otimes1_D)(1_D\otimes\sigma_{D,A}),\\
q&=1_D\otimes c.
\end{aligned}
\tag{PM16}
\]

The subscripts 0 and 1 distinguish the equal line \(D\) that comes from \(\ell_h(F)\) and the equal line inserted by \(c^{-1}\). Route \(p\) crosses \(D_1\) past \(A\), contracts \(D_0\otimes A\), then crosses \(B\) past the remaining \(D_1\). Route \(q\) leaves \(D_0\) in place and contracts \(D_1\otimes A\).

For a homogeneous local generator, the same coefficient of \(c\) appears once on each route. The symmetry coefficients of \(p\) multiply to

\[
(-1)^{|D||A|+|B||D|}=(-1)^{|D|^2}=\varepsilon.
\tag{PM17}
\]

Thus \(p=\varepsilon q\) as line morphisms. Changing any orientation generator changes both occurrences of the evaluation coefficient by the same invertible transition factor. Hence the equality glues on nonorientable bundles. This is a calculation of bounded invertible tensor morphisms before applying arbitrary sheaf operations; it imposes no restriction on a coefficient object or on the rank of the map \(h\).

The \(c\) and \(c^{-1}\) in the \(q\) route cancel. PM14 now gives
\(\mu_F\otimes1_B=\varepsilon\ell_h(F)\otimes1_B\).
Tensoring by \(B\) is faithful on every Hom set, so PM2 follows for every \(F\). No constant-sheaf detection argument has been used.

## SH02-MEP-MATE-UNTWIST. The contracted mate is the required fourth row

The conclusion of the precise-mate proof is
\[
\mu_h=\varepsilon\ell_h,
\qquad \varepsilon=(-1)^{c_Y-c_X}.
\tag{MEP16}
\]
Writing \(D=K^\vee\) again for the dual of the output line, coherent contraction of this map is
\[
\overline\mu_h^{\,c}
=(1\otimes u_K^{-1})(\mu_h\otimes1_D)
=\varepsilon\bar\ell_h^{\,c}
=\bar\ell_h^{\,b}=B_h.
\tag{MEP17}
\]
The last equality uses \(\operatorname{ev}_K\sigma_{K,D}=\varepsilon u_K^{-1}\). This is not an unsigned assertion about bare L3.

We verify that the ordinary-inverse row in MIC11 has exactly the mate \(B_h^{-1}\). For this purpose suppress the functor projection formulas and put \(U=T_1h^{-1}\), \(R=Rr_!T_2\). Original R4 has form \(D_h:\Omega\otimes U\to R\). Untwist it by taking its right-ordered transpose PM4, obtaining \(U\to R\otimes K\), and then apply \(\sigma_{R,K}\) to put the line on the left. This defines
\[
I_h:U\longrightarrow K\otimes R
\simeq Rr_!(K\otimes T_2(-)).
\tag{MEP18}
\]
This is the original R4 rewritten by the actual tensor adjunction and the specified left-line projection formula. In particular the coherent inverse pairing MEP4 is not substituted for that tensor adjunction's counit.

Let \(J=r^!T_1F\), \(Z=T_2Rh_*F\). By the Hom characterization of the right mate of \(D_h\), the right mate of \(I_h\), in the inverse comparison direction, is the left-\(K\) adjunct of
\[
K\otimes Z\xrightarrow{\sigma_{K,Z}}Z\otimes K
\xrightarrow{\mu_h^{-1}}J.
\tag{MEP19}
\]
This assertion can be verified on each Hom set: precomposition with MEP18 first uses the right-tensor adjunction for \(\Omega\) and then the output symmetry; moving these across Hom gives exactly the inverse map \(\mu_h^{-1}\) and the displayed input symmetry. The original Fourier conjugating unit and counit are already those in PM13, so none are replaced in this step.

To express the adjunct as \(Z\to J\otimes D\), apply PM4 with line \(K\). It inserts \(1_Z\otimes u_K\), then \(\sigma_{Z,K}\otimes1_D\), then MEP19 tensored with \(D\). The two consecutive symmetries \(\sigma_{Z,K}\) and \(\sigma_{K,Z}\) cancel by the symmetry identity, on an arbitrary derived object \(Z\). The result is
\[
(\mu_h^{-1}\otimes1_D)(1_Z\otimes u_K)
=(\overline\mu_h^{\,c})^{-1}=B_h^{-1}.
\tag{MEP20}
\]
This proves the actual linear mate identification. The pairing MEP4 identifies \(D\) with the MIC orientation ratio, and the right-line projection formula moves that base line through \(Rs_*\). Base proper/inverse exchanges and their ordinary/exceptional mates preserve pasting. Thus the fourth normal exchange in MEP9 is the right mate of the third exchange MEP18 followed by base inverse exchange. All four rows of MIC11 now have their precise constructions simultaneously fixed.

The former PA32 target is therefore corrected, not left as an unproved unsigned equality. With the canonical right-Hom extraction its uncontracted form is MEP16; its contracted form is MEP20. For example, over \(\mathbb Z\), the map \(h:0\to\mathbb R\) has \(\ell_h(k)=-1\) and the direct comparison \(G_h(k)=+1\), as calculated in LFT20b–LFT20c. MEP16 gives \(\mu_h(k)=+1\). This is a counterexample to the bare unsigned course target, and confirms the general calculation. It is not a source-book erratum claim.

## SH02-MEP-SUPPORT. The support square with its complete endpoint

Let \(\bar\theta_r:r^{-1}T_1A\to r^!T_1A\otimes D\) be the right-ordered trace comparison used in FTC13b. For every conic bounded complex \(A\) on \(E_1\),
\[
I_q^*\,T_X(\nu_q)
=\nu_s\,Rs_!(\bar\theta_r)\,I_q^!.
\tag{MEP11}
\]
The natural transformation \(\nu_s\) on the right is evaluated at \(r^!T_1A\otimes D\). Thus the order is first the trace for \(r\), then forgetting proper support along \(s\).

**Proof.** Under the composition maps, \(\nu_q\) is
\[
Rb_!Rh_!\xrightarrow{Rb_!\nu_h}Rb_!Rh_*
\xrightarrow{\nu_b\,Rh_*}Rb_*Rh_*.
\tag{MEP12}
\]
This follows from the actual inclusion of proper-support sections; the derived composition and inclusion maps preserve that equality. The FGC theorem is precisely
\(B_h\bar\theta_r=T_2(\nu_h)A_h\).
Conjugating this equality by the two invertible endpoints gives
\[
B_h^{-1}T_2(\nu_h)=\bar\theta_r A_h^{-1}.
\tag{MEP13}
\]
Apply the proper base exchange to the first arrow of MEP12 and use MEP13. FTC6 sends the second arrow to \(\nu_s\). Move \(B_h^{-1}\) through that arrow by naturality of \(\nu_s\). The resulting composite is the right side of MEP11. The base and fibre kernel squares paste by FF4/FF13, so the endpoints are exactly MEP9. No new isomorphism is chosen in this proof. \(\square\)

Consequently applying Fourier to the specialization direct square gives MIC12 with its stated relative-trace vertical, using the fourth-row completion MEP9. MEP20 proves that this completion is its prescribed ordinary adjoint-mate row. All three properness hypotheses for invertibility remain those of SH02-SP-PROPER: properness of \(f\) on the support, properness of the normal derivative on its normal cone, and \(\operatorname{supp}(G)\cap f^{-1}M\subset N\). The identity MEP11 itself uses none of those properness assumptions.

## SH02-MEP-TRACE. The trace square with the original R2 and R4 maps

For a conic bounded complex \(H\) on \(N_MX\), the Fourier transform of \(\theta_q(H)\), under MEP10 and the original exceptional exchange, is
\[
Rr_!(\omega_s\otimes s^{-1}T_XH)
\xrightarrow{Rr_!\theta_s}Rr_!s^!T_XH
\xrightarrow{\nu_r}Rr_*s^!T_XH.
\tag{MEP14}
\]

**Proof.** First fix the orientation comparison for the composite \(q=bh\). Exceptional transitivity identifies \(\omega_q=h^!\omega_b\). Since \(\omega_b\) is a base-pulled invertible graded line in this normal-bundle situation, its canonical trace comparison
\(\theta_h(\omega_b):\Omega\otimes h^{-1}\omega_b\to h^!\omega_b\)
is an isomorphism. This is the same map as invertible-line extraction: their adjuncts under \(Rh_!\dashv h^!\) are both \(\operatorname{tr}_h\otimes1\) after the proper-support projection formula. The exceptional adjunction bijection proves equality of those maps, rather than just their invertibility.

With this identification the trace for \(q\) is
\[
\begin{aligned}
\Omega\otimes h^{-1}\omega_b\otimes h^{-1}b^{-1}H
&\xrightarrow{1\otimes h^{-1}\theta_b}
\Omega\otimes h^{-1}b^!H\\
&\xrightarrow{\theta_h(b^!H)}h^!b^!H
\simeq q^!H.
\end{aligned}
\tag{MEP15}
\]
Indeed its adjunct under the composite exceptional adjunction is first the counit for \(h\), then the counit for \(b\), with the indicated coefficient projection formula. The counit of a composite adjunction is exactly that composite, so its adjunct is \(\operatorname{tr}_q\otimes1_H\). By the defining adjunction for \(\theta_q\), this proves MEP15 with its actual arrows.

Apply \(T_1\) to MEP15. Naturality of original R4 identifies its first arrow with \(Rr_!\) of the transformed \(\theta_b\). The base trace theorem, with the counit normalization MEP6, identifies this with \(Rr_!\theta_s\). Apply FTE34 to the arbitrary conic coefficient \(b^!H\) in the second arrow. It states
\(E_hT_1\theta_h=\nu_rT_2D_h\), with unchanged original R2 and R4. Under the exceptional base exchange \(T_2b^!H=s^!T_XH\), its result is the second arrow in MEP14. Both calculations use the same R4 endpoint at their joint vertex, so those inverse endpoint maps cancel. Proper-support projection-formula pasting moves only the base-pulled \(\omega_b\), with the module symmetries already specified in R4. MEP6 identifies it with \(\omega_s\). This proves MEP14, retaining the order of its arrows. \(\square\)

Taking \(H=\nu_MF\) and applying this theorem to the specialization inverse square proves MIC13 with its explicit trace vertical. The specialization orientation map is MEP5, as checked above; the locally constant twist uses SH02-SP-TWISTS. This trace-half conclusion uses the original second and third Fourier exchange maps. It does not need an assertion about the fourth row's separate adjoint-mate comparison.

## SH02-MEP-PROBLEMS. Checks that keep the scope visible

**Problem 1.** Let \(g\) be the identity and let the normal derivative have varying rank. Which parts of the support and trace proofs need a splitting of its kernel?

**Solution.** None. The primitive exchange uses the equality of the two pairing functions; the finite dimension bound for an exceptional inverse image comes from affine fibres of dimension at most the source rank. MEP3 uses exceptional transitivity of the two bundle projections. The subsequent proof pastes those existing maps. Local splittings were used only for the normal tangent exact sequences of the embeddings, whose quotient bundles have fixed ranks; they were not splittings of \(h\). Thus a family \(h_x(v)=xv\) over \(\mathbb R\) is included, including its zero-rank fibre at \(x=0\).

**Problem 2.** Suppose \(c_X-c_Y\) is odd. Change only the last contraction in MEP8 to inverse coevaluation. What becomes of MEP11?

**Solution.** The new \(B_h\) is \(-B_h\), since braided evaluation and inverse coevaluation on the forward ordered pair \(K\otimes K^\vee\) differ by the parity of \(K\). Its inverse is also \(-B_h^{-1}\). Thus the new \(I_q^*\) changes sign while \(I_q^!\), \(\theta_r\) and \(\nu_s\) are unchanged. The support identity acquires that minus sign. It is therefore incorrect to propagate only the objects in MIC11 while discarding the final contraction convention. In characteristic two this scalar happens to be one; that special coefficient case does not justify omitting the convention for a general ring.

**Problem 3.** If \(f\) and \(g\) are submersions, explain why both constituents of MEP14 are invertible.

**Solution.** Surjectivity of \(df\) implies surjectivity of the map of normal quotients, hence \(h\) is fibrewise surjective. Its transpose \(r\) is a closed embedding of vector bundles, so \(Rr_!=Rr_*\) and \(\nu_r\) is invertible. The map \(s\) is a bundle base change of the submersion \(g\), so its relative-trace comparison \(\theta_s\) is invertible. These are different reasons for the two arrows. Neither would follow merely from contractibility of fibres or from orientability.

## SH02-MEP-STATUS. What has and has not been identified

The trace-half endpoint calculation MEP14 is a full proof relative to the finite named cut, with original R2/R4, full coefficients and normal-derivative hypotheses. MEP11 proves the support-half calculation, and MEP20 identifies its braided endpoint with the actual mate of the ordinary-inverse row. The uncontracted course target PA32 is corrected to the signed equation MEP16; it is not retained as an unresolved unsigned target. These results supply both exact identifications in SH02-MIC-TRACE-EXCHANGE.
