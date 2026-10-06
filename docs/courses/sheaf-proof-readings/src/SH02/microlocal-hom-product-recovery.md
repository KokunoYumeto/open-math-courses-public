# SH02-MHPR — Product recovery for microlocal composition

Course SH-02, unit SH02-MHPR. Original AI-authored programme expression is dedicated under CC0 1.0 Universal. This lesson compares the specified Fourier, microlocal product and graph-composition maps with the selected recovery maps. The published mathematical antecedents and the scope of their comparison are stated at the end; human-authored source expression retains its own terms.

The selected zero-direction recoveries in microlocalization are normalized by the actual ordinary no-cut map and the compact codimension-parity map. This lesson proves that the product map MIC19 and graph composition MH30/MH31 commute with those particular recoveries. It proves equality of natural transformations, including the coefficient braids, exceptional counits, support maps and relative traces. The argument uses arbitrary bounded sheaves over a commutative unital finite-global-dimension coefficient ring under the stated bounded six-operation and Fourier contracts. No constructibility, finite stalk generation, orientability, proper bundle projection, or noncharacteristic condition is added.

The proof has three parts. C1–C15 state and establish the selected product identities and their MH30 application. P1–P20 supply the full Fourier product normalization used in C5. S1–S14 give the typed ordinary and compact composition pastes, with raw graph-kernel endpoints. Their separate labels keep each map and its source order visible.

## SH02-MHPR-NORMALIZATION — Selected product identities

### 1. Scope and statement

Let \(k\) be a commutative unital ring of finite global dimension. Work with arbitrary bounded sheaf complexes on finite-dimensional Hausdorff manifolds countable at infinity, within the existing bounded Fourier, specialization, and graph-Hom contracts. No constructibility, field, finite stalk-generation, orientability, or properness of a bundle projection is assumed. Locally closed embeddings are handled in ambient open neighborhoods and then glued.

Let \(i_a:M_a\hookrightarrow X_a\), \(a=1,2\), be closed smooth embeddings of codimensions \(c_a\), let \(F_a\in D^b(k_{X_a})\), and put
\[
H_a=\mu_{M_a}F_a,\quad U_a=i_a^{-1}F_a,\quad \Omega_a=\omega_{i_a}.
\tag{C1}
\]
Write \(i=i_1\times i_2\), \(F=F_1\boxtimes F_2\), \(H=\mu_{M_1\times M_2}F\), and \(\Omega=\omega_i\). Use the canonical product identification of the dual normal bundles. The maps \(r^*,r^!\) are precisely REC6 and REC16, including the codimension parity in REC16. In particular they are not arbitrary choices of the recovery isomorphisms.

Let \(P:H_1\boxtimes H_2\to H\) be MIC19, meaning the inverse of the actual FF20 product map followed by Fourier transform of SP-EXTERNAL. Let \(K_!\) be proper external Künneth and let \(K_*\) be the ordinary lax external comparison. Define
\[
C_!=R\pi_!(P)K_!,\qquad C_*=R\pi_*(P)K_*.
\tag{C2}
\]
The exceptional external-product map \(\operatorname{Ex}_i\) is the adjunct of proper Künneth inverse followed by the two exceptional counits. Its orientation instance is
\[
\kappa_i:\Omega_1\boxtimes\Omega_2\longrightarrow\Omega.
\tag{C3}
\]
This orientation instance is invertible. No exceptional external-product isomorphism for arbitrary sheaves is required.

Define the fully ordered lower compact arrow
\[
b_R=(1_{U_1\boxtimes U_2}\otimes\kappa_i)
 (1_{U_1}\otimes\sigma_{\Omega_1,U_2}\otimes1_{\Omega_2}).
\tag{C4}
\]
Its source is \((U_1\otimes\Omega_1)\boxtimes(U_2\otimes\Omega_2)\), and its target is \(i^{-1}F\otimes\Omega\). The two product-normalization identities are
\[
r_F^!C_!=b_R(r_{F_1}^!\boxtimes r_{F_2}^!),
\qquad
r_F^*C_*=\operatorname{Ex}_i(r_{F_1}^*\boxtimes r_{F_2}^*).
\tag{C5}
\]
The first identity is an equality with proper external Künneth. The second uses the ordinary lax external map, without asserting its invertibility.

### 2. Compact square and all normalization signs

The full proof of the first identity is P1–P20 in SH02-MHPR-FOURIER below. Here are its essential map checks, to make clear which extra result supplements REC.

For a normal bundle \(E_a\to M_a\), original R4 is
\(D_a:\omega_{e_a}\otimes e_a^{-1}A_a\to R\pi_{a!}T_aA_a\).
The natural counit \(\tau_a^{-1}R\tau_{a*}A_a\to A_a\) becomes an isomorphism after zero restriction by conic contraction. Naturality and invertibility of original R4 show that the compact Fourier functors on both sides of the product square invert this particular comparison. This reduces the map equality to arbitrary pulled-back base complexes, not to constant generators or perfect coefficients.

For those pulled-back complexes, Fourier transform is supported on the dual zero section. Full FTE34 identifies original R4 after support forgetting with original R2 composed with the exceptional trace; REC5 identifies that R2 map with the actual no-cut map. At the dual zero section both cuts defining FF20 are the whole normal fibre. The kernel restriction is therefore the identity and the remaining map is exactly proper Künneth. Expanding the exceptional trace and product maps gives the same tensor product of counits. This proves the original R4 product equation. It uses neither an unproved monoidal comparison of inverse Fourier presentations nor conservativity of ordinary recovery on arbitrary conic objects.

For \(W_a=\operatorname{or}_{E_a}[c_a]\), the actual orientation maps obey
\[
d(\kappa\otimes m_W)
=(d_1\boxtimes d_2)
 (1_{\Omega_1}\otimes\sigma_{\Omega_2,W_1}\otimes1_{W_2}).
\tag{C6}
\]
This follows from the four exceptional counits of \(\tau_ae_a=1\), their composition, and faithful right tensoring by the invertible projection line. It is a property of the existing exceptional product maps, not a definition of replacement signs. The displayed line-line braid is \((-1)^{c_1c_2}\). C4 contributes \((-1)^{c_1|u_2|}\) on a homogeneous coefficient \(u_2\). The left-ordered R4 version instead crosses the second relative line past the first coefficient and contributes \((-1)^{c_2|u_1|}\). These are equivalent presentations by tensor symmetry.

REC8 and REC16 give the linear right-ordered recovery
\[
\ell_a=\sigma_{\Omega_a,e_a^{-1}A_a}D_a^{-1}=(-1)^{c_a}Z_a,
\qquad
(-1)^{c_1+c_2}=(-1)^{c_1}(-1)^{c_2}.
\tag{C7}
\]
Consequently the selected parity normalizations preserve the product square. They contribute no additional independent cross-rank scalar. C6 and C4 must nevertheless retain their displayed braids.

The SP external comparison intertwines the ordinary restriction units:
\[
e^{-1}\chi\,(u_{F_1}\boxtimes u_{F_2})=u_F.
\tag{C8}
\]
Indeed the external \(Rj_*\) map is adjunct to the identity on the two positive chambers; pulling it to equal time and precomposing the units leaves the unit for the equal-time chamber. Central zero restriction gives C8. This uses the actual base-exchange map, without assuming that map invertible off the selected restriction.

Finally the normal-to-ambient orientation comparisons in MEP5/O13 commute with the actual exceptional product maps. The expanded argument in the Fourier lemma uses adapted coordinates to identify both the embedding and its normal zero section with the same map \(M\times\{0\}\to M\times\mathbb R^c\). MEP's positive-time counit normalization makes that identification the actual one. Regrouping the product coordinate blocks moves the first normal block past the second tangent block and has determinant \((-1)^{c_1\dim M_2}\); the identical coordinate permutation and derived line symmetries occur on both sides of the comparison square. Naturality of exceptional counits under that diffeomorphism proves the local equality. Chart changes give the same orientation transition functions, so the equality glues without orientability. No determinant or shift sign is silently declared to be positive. C8 and this orientation compatibility finish the first identity in C5.

### 3. Ordinary square, with its actual specialization counit

Write \(A_a=\nu_{M_a}F_a\), \(A=\nu_{M_1\times M_2}F\), and \(\chi:A_1\boxtimes A_2\to A\) for SP-EXTERNAL. For any conic inputs, original R2 satisfies
\[
R\pi_*(\mu^{-1})K_*(E_1\boxtimes E_2)
=E\operatorname{Ex}_e,
\tag{C9}
\]
where \(\mu=T(A_1\boxtimes A_2)\to TA_1\boxtimes TA_2\) is FF20, and the exceptional product on the right has target \(e^!(A_1\boxtimes A_2)\).

To prove C9, apply the specified conic contraction to the dual zero section and then the no-cut proper base-change map. Ordinary lax external pushforward becomes the ordinary external zero-restriction identification: this is the adjunction-unit definition of the lax map, followed by the same contraction units. FF20 becomes proper Künneth because its two cuts are the whole fibre at zero. REC5 identifies each \(E_a\) with
\(k_{\tau_a}^!:e_a^!A_a\to R\tau_{a!}A_a\).
The resulting equation is
\[
K_{\tau!}(k_{\tau_1}^!\boxtimes k_{\tau_2}^!)
=k_\tau^!\operatorname{Ex}_e.
\tag{C10}
\]
The contraction on the right is proper image of the zero-section support counit. The adjunct of \(\operatorname{Ex}_e\) is precisely the product of those two counits after Künneth. Thus the two sides of C10 are the same map by adjunction and proper-image composition. The final conic contraction and no-cut postcomposition used to test C9 are invertible, so C9 follows. This cancellation does not assert invertibility of \(K_*\) or of the exceptional product map.

The remaining specialization equation is
\[
c_F\,e^!\chi\,\operatorname{Ex}_e
=\operatorname{Ex}_i(c_{F_1}\boxtimes c_{F_2}).
\tag{C11}
\]
Here \(c_F:e^!\nu F\to i^!F\) is exactly the support/boundary counit in SP-ZERO and REC3. A useful full-coefficient check avoids treating this counit as an arbitrary inverse isomorphism. Put \(F'_a=i_{a*}i_a^!F_a\), with the actual support counit \(F'_a\to F_a\). SP-ZERO and its naturality show that
\(e_a^!\nu F'_a\to e_a^!\nu F_a\) is invertible. Consequently one can prove C11 after precomposing by their external product. Naturality reduces the resulting equality to the case \(F'_a=i_{a*}L_a\), with completely arbitrary \(L_a=i_a^!F_a\). No isomorphism for the product target is needed in this reduction.

On those supported objects SP-ZERO identifies \(\nu i_{a*}L_a=e_{a*}L_a\). The external comparison, restricted to the zero axis, is the identity on \(L_1\boxtimes L_2\): its positive-chamber adjunct is that identity and its equal-time pullback is the identity. The support counit is also the identity under these particular identifications. This last assertion is the positive-endpoint boundary and projection-orientation cancellation proved in SP-ZERO; its coefficient is \(+1\). Finally each exceptional external comparison restricted to the supported zero axes is the identity, by its two counits. Thus C11 holds on supported objects and naturality proves it for all \(F_a\).

Now REC6 is \(r_F^*=c_FE^{-1}\). Compose C9 with \(e^!\chi\), use naturality of original R2, and then use C11. This proves the second identity in C5 with the specified ordinary recovery maps.

### 4. The mixed support/trace square

The two identities C5 respect the selected recovery trace. For each embedding REC19 says
\[
r_F^*\nu_\pi(r_F^!)^{-1}=\theta_i\sigma_{U,\Omega}.
\tag{C12}
\]
Proper and ordinary external pushforward satisfy
\(\nu_\pi K_!=K_*(\nu_{\pi_1}\boxtimes\nu_{\pi_2})\), as maps into the product pushforward. Expand the actual inclusion of properly supported sections and the composition/base-exchange maps to obtain that identity; no properness assumption is introduced. The product of the two trace comparisons, after C4 and the symmetry placing the relative line on the left, equals the trace comparison for the product followed by \(\operatorname{Ex}_i\). Its exceptional adjunct is the same tensor product of counits with coefficients retained, exactly as in C6. These facts and REC19 prove the whole product recovery/trace diagram. In particular neither an uncontracted unsigned MEP endpoint nor an inverse coevaluation substituted for the prescribed right-Hom contraction is used.

![The selected compact and ordinary product-recovery squares, with each actual comparison map labeled](../assets/product-recovery-squares.png)

The left panel draws the first equality of C5, restated as S2: the top map
\(C_!=R\pi_!(P)K_!\) goes from \(R\pi_{1!}H_1\boxtimes R\pi_{2!}H_2\)
to \(R\pi_!H\), while the REC16 vertical maps land in
\((U_1\otimes\Omega_1)\boxtimes(U_2\otimes\Omega_2)\) and
\((U_1\boxtimes U_2)\otimes\Omega\). The lower arrow is exactly C4:
its first step braids \(\Omega_1\) past \(U_2\), then \(\kappa_i\)
combines the relative lines. The right panel draws the second equality
of C5, restated as S1: \(C_*=R\pi_*(P)K_*\) lands in \(R\pi_*H\),
the REC6 vertical maps land in \(i_1^!F_1\boxtimes i_2^!F_2\)
and \(i^!F\), and the lower arrow is the exceptional external map
\(\operatorname{Ex}_i\). Here \(K_*\) is the specified lax map;
the diagram makes no invertibility claim about it. C12 proves that the
proper-to-ordinary trace intertwines these two squares. The corners and
arrows are a schematic of the typed identities proved at C5, C12, S1,
and S2, not replacement definitions of the maps. The standard Fourier,
microlocalization and recovery constructions are compared with the published
sources at the end of the lesson; the specific product squares and their
normalizations are proved at C5–C12 and P1–P20. This diagram and its labeling
are original course material. Its PNG and SVG share this lesson's
CC0 1.0 dedication.
A vector copy of both product squares
preserves the map labels.

### 5. Application to MH30/MH31

The fully typed composition pasting and its orientation cancellation are S5–S14 in SH02-MHPR-PASTE below. In that note \(a:M\hookrightarrow Q\), \(b:L\hookrightarrow W\), \(c:T\hookrightarrow X\times Z\) are the product-graph, pulled-back graph, and composite-graph inclusions; \(j:W\to Q\) repeats the middle coordinate; \(q:W\to X\times Z\) forgets it; and \(\ell=q|_L:L\to T\) is an isomorphism.

C5 supplies the extra external-product square before the transverse \(j\)-pullback in MH30. Its ordinary endpoint is the actual support/base-change map \(t^{-1}a^!P\to b^!j^{-1}P\). Its compact endpoint is ordinary coefficient pullback with the normal-isomorphism orientation map. The defining specialization inverse comparison carries the ordinary restriction unit to the pulled-back unit, by its positive-chamber base-exchange adjunct and the adjunction triangles; original Fourier exchange for the normal isomorphism preserves that no-cut map. Thus the selected REC recoveries give exactly those endpoint maps. No invertibility of the merely transverse MIC14 map is asserted.

After MH30 the kernel is specifically \(q^!K_h\). Since both \(q\) and \(\ell\) are submersions, MIC-SMOOTH gives the actual inverse-comparison isomorphism
\[
b_q:\mu_Lq^!K_h\xrightarrow{\sim}r_*\mu_TK_h,
\tag{C13}
\]
where \(r\) is the closed inclusion of the zero-middle-covector locus. MIC15/MIC17 identify the restriction/direct-image/counit map \(u_q\) with the mate of \(b_q\). Therefore
\[
r_*u_q\,\eta_r=b_q
\tag{C14}
\]
by the adjunction triangle, as expanded in S12. This is why compact restriction is legitimate on this target. It would not be legitimate to assert the same support statement on an arbitrary earlier kernel.

Set \(S=b^{-1}q^{-1}K_h\), \(Q_q=b^{-1}\omega_q\), and \(\Omega_b=\omega_b\). The compact endpoint of C13 is, in full order,
\[
b^{-1}q^!K_h\otimes\Omega_b
\longrightarrow Q_q\otimes S\otimes\Omega_b
\xrightarrow{\sigma_{Q_q,S}\otimes1}S\otimes Q_q\otimes\Omega_b
\xrightarrow{1\otimes\sigma_{Q_q,\Omega_b}}S\otimes\Omega_b\otimes Q_q
\xrightarrow{1\otimes t_{b,q}}S\otimes\ell^{-1}\omega_c.
\tag{C15}
\]
The first arrow is inverse left-ordered smooth trace and \(t_{b,q}\) is the actual exceptional-transitivity map for \(qb=c\ell\). If \(n=\dim Y\) and \(d=\operatorname{codim}(L,W)\), the two displayed braids contribute \((-1)^{n|s|}\) and \((-1)^{nd}\). Right-ordered smooth purity already contains the first braid and must not acquire it twice. S13 proves C15 by straightening \(q\) locally, applying C5 with the middle dualizing coefficient, and then using its counit-normalized coefficient-one trace. Product orientation coherence makes the result independent of coordinates and valid without orientability.

The full compact composition square is S14. Its top edge uses proper Künneth over the base and the unit restricting to the closed fibre diagonal, followed by the actual MH31 composition. Its lower edge on raw endpoints \(C_{ij}=\Delta^{-1}K_{ij}\otimes\omega_\Delta\) consists, in order, of the initial factor symmetry, C4, the transverse normal orientation map, restriction of MH30, and C15. Pasting the squares proves equality of these maps. The ordinary paste is S5–S8: the last proper-support comparison followed by the \(q\)-counit is the \(\ell\)-counit by exceptional transitivity. This recovers the already specified ordinary composition.

MH30's kernel evaluation has its own explicit braid. Evaluation initially gives \(F_x\otimes\omega_Y\otimes\omega_Z\). The right-ordered smooth-purity presentation of its target uses \(F_x\otimes\omega_Z\otimes\omega_Y\), so it includes \(1_{F_x}\otimes\sigma_{\omega_Y,\omega_Z}\), of parity \((-1)^{\dim Y\dim Z}\). Transposing that evaluated map defines the actual Hom-kernel arrow. Passing to the left-ordered presentation in C15 includes the coefficient-line symmetry already displayed there. These symmetries and the initial factor symmetry are retained as maps, rather than absorbed into an unrecorded scalar.

The precise compact endpoint throughout remains the raw graph restriction \(i^{-1}K\otimes\omega_i\). No replacement by an unrestricted dual-Hom tensor formula is made.

The homogeneous convention in MH31 uses the derived symmetry in the written source order. With the usual closed-monoidal convention, composition has source
\(R\mathcal Hom(F_2,F_3)\otimes R\mathcal Hom(F_1,F_2)\).
For the source order actually displayed in MH31 the map is \(\mathrm{comp}\circ\sigma\), and homogeneous \(a\otimes b\) maps to \((-1)^{|a||b|}b\circ a\), when the latter \(b\circ a\) means usual chain-level composition. The categorical construction retains that symmetry; degree-zero arrows are unaffected.

## SH02-MHPR-FOURIER — Fourier product normalization

### 1. Domain and specified maps

Let \(k\) be commutative, unital and of finite global dimension. Initially let \(E_i\to B_i\) be finite-rank real vector bundles over locally compact Hausdorff bases, with ranks \(c_i\), and let \(A_i\in D^+_{\mathbb R_{>0}}(E_i;k)\) have global lower bounds. Put
\[
E=E_1\times E_2\to B=B_1\times B_2,\qquad c=c_1+c_2.
\]
The same argument works over a common base with all products replaced by fibre products and pullback tensors. Exceptional maps used below have the bundle-rank cohomological bounds. There is no assumption of a field, constructibility, finite stalk generation, orientability or proper bundle projections. Locally constant ranks require the existing global amplitude bounds.

Write \(e_i,e\) for the zero sections, \(\tau_i,\tau\) for the normal projections, and \(\pi_i,\pi\) for the dual projections. Let
\[
U_i=e_i^{-1}A_i,\quad W_i=\operatorname{or}_{E_i}[c_i],\quad
\Omega_i=\omega_{e_i},\quad d_i:\Omega_i\otimes W_i\longrightarrow k_{B_i}.
\tag{P1}
\]
Use the analogous notation without a subscript on the product bundle. Each \(d_i\) and \(d\) is exactly FF3a for \(\tau_i e_i=1\), respectively \(\tau e=1\). In particular these are counit-normalized maps of shifted lines.

Let
\[
D_i(A_i):\Omega_i\otimes U_i\xrightarrow{\sim}R\pi_{i!}T_iA_i
\]
be original R4, and let \(D(A_1\boxtimes A_2)\) be original R4 for \(e\). Let
\[
\mu:T_E(A_1\boxtimes A_2)\xrightarrow{\sim}T_1A_1\boxtimes T_2A_2
\tag{P2}
\]
be exactly FF20, whose direction is restriction from the sum halfspace to the two separate halfspaces followed by the inverse proper Künneth identification. All occurrences of proper Künneth use the base-change, projection-formula and composition map specified in FF20. Denote the resulting isomorphism
\[
K:R\pi_{1!}T_1A_1\boxtimes R\pi_{2!}T_2A_2
\longrightarrow R\pi_!(T_1A_1\boxtimes T_2A_2).
\tag{P3}
\]

### 2. The actual product orientation and its sign

For maps \(f_i\), denote their exceptional external-product comparison by \(\operatorname{Ex}_{f_1,f_2}\). This is a map, specified by adjunction: its proper-image adjunct is proper Künneth inverse followed by the tensor product of the two exceptional counits. Only its value on the indicated orientation objects is asserted invertible here.

Define
\[
\kappa:\Omega_1\boxtimes\Omega_2\xrightarrow{\sim}\Omega
\tag{P4}
\]
to be \(\operatorname{Ex}_{e_1,e_2}\) at the constant ambient coefficient. Define
\[
m_W:W_1\boxtimes W_2\xrightarrow{\sim}W
\tag{P5}
\]
by restricting \(\operatorname{Ex}_{\tau_1,\tau_2}\) at the constant base coefficient to the product zero section. Thus both maps come from the existing exceptional counits. Neither is stipulated to be an unsigned identification of orientation generators.

These particular maps satisfy, with canonical associators and base pullbacks understood,
\[
d\,(\kappa\otimes m_W)
=(d_1\boxtimes d_2)
 (1_{\Omega_1}\otimes\sigma_{\Omega_2,W_1}\otimes1_{W_2}).
\tag{P6}
\]
Both sides have source \(\Omega_1\otimes\Omega_2\otimes W_1\otimes W_2\) and target \(k_B\). The displayed interchange contributes exactly \((-1)^{c_1c_2}\).

Here is why P6 holds for the already specified maps, rather than defining replacements for them. Expand the exceptional-product maps by their adjuncts. For the two composites \(\tau_i e_i=1\), the product of the composite counits first applies the two zero-section counits and then the two projection counits. The composite of the exceptional-product maps has that same adjunct: proper base-change and Künneth pasting arrange the same four counits in the same order. Moving the second relative zero-section line next to its projection line is exactly the symmetry in P6. The unit/counit triangles remove the inserted adjunction pairs. Exceptional adjunction uniqueness proves the equality. FF3a is precisely the right-tensor extraction of these composite counits. Faithful right tensoring by \(W\) therefore identifies the resulting line map with the original \(\kappa\). This derivation uses coherence of the six-operation maps, not a new choice of scalar.

The ungraded orientation comparison between a product normal bundle and the normal bundle of a product embedding also uses the ordered tangent exact sequences and their symmetries, as in MEP5/O13. Any determinant sign from regrouping ambient tangent and normal blocks is already in that counit-normalized comparison. It must not be inserted a second time into P6.

#### 2a. Normal-to-ambient orientations commute with the actual product maps

For embeddings \(i_j:M_j\hookrightarrow X_j\), let
\(\phi_j:\omega_{e_j}\xrightarrow{\sim}\omega_{i_j}\) and
\(\phi:\omega_e\xrightarrow{\sim}\omega_i\) be the inverses, at the zero-normal map of pairs, of the normal orientation maps fixed by MEP5/O13. Write \(\kappa_e\) for P4 and \(\kappa_i\) for the analogous exceptional-product map of the ambient embeddings. The precise compatibility required later is
\[
\phi\,\kappa_e=\kappa_i(\phi_1\boxtimes\phi_2).
\tag{P6a}
\]

We prove this for the actual O13 maps. For any map \(f:Y\to X\) over a parameter space \(S\), where both parameter projections are submersions, and any base change \(S'\to S\) within the existing M28 operation domain, let \(\gamma_f\) denote the exceptional comparison for the induced cartesian square. Its definition is the O13 adjunct: proper base change followed by the counit of \(f\). Expanding this adjunct proves two compatibilities. First, successive parameter base changes give the same map as the composite base change, since their proper base-change maps paste. Second, a product of two such comparisons commutes with the actual exceptional-product maps: after proper image and Künneth, both adjuncts are the product of the two original counits. These are identities of counit maps, including their coefficient extraction and symmetries.

The O13 proof applies to this general parameter base change, not only the inclusion of zero in a real line. M28 gives the submersion orientation isomorphisms for both parameter projections. Exceptional mate pasting identifies the comparison at the invertible target submersion orientation with their composite. Extracting that orientation on the right is faithful and determines \(\gamma_f(k)\) uniquely. Thus the two compatibilities just proved for the adjuncts also hold for these specified relative-orientation maps. No exceptional base-change isomorphism for arbitrary coefficients of \(f\) is asserted.

Apply this to the product of the two zero-normal deformation maps
\[
\widetilde i_1\times\widetilde i_2:
(M_1\times\mathbb R)\times(M_2\times\mathbb R)
\longrightarrow D_{M_1}X_1\times D_{M_2}X_2
\]
over the two-parameter space \(\mathbb R^2\). Both parameter projections are submersions. Pullback by \(\delta:\mathbb R\to\mathbb R^2\), \(t\mapsto(t,t)\), is exactly the deformation map for the product embedding, using the equal-time identification from SP-EXTERNAL. The central pullback factors either through \(\delta\) and \(0\in\mathbb R\), or directly through \((0,0)\in\mathbb R^2\); its exceptional comparisons agree by the first compatibility. The second compatibility identifies the direct two-parameter central comparison with the product of the individual central comparisons. The same argument on the positive chambers identifies the ambient comparisons. Taking the central-to-positive relative-orientation identification yields P6a.

All extractions here are the right-tensor extractions in the O13 proof. In a presentation using absolute dualizing objects, the positive time orientation is put last, and the same time factor is canceled on the source and target. In the two-parameter presentation one retains the ordered pair of time factors and its actual product map before cancellation. Pullback to the diagonal is a parameter base change of relative orientations; it does not insert an arbitrarily oriented exceptional diagonal line. The counit-pasting calculation already includes every symmetry needed to regroup those factors. Finally, the positive deformation chart has determinant \(t^{c_j}>0\) in each normal block, so these counit-normalized identifications coincide with MEP5's ordered tangent/normal representative. Positivity fixes this chart comparison; it does not replace \(\kappa_e\), \(\kappa_i\), or P6 by an unsigned determinant map. This proves P6a without suppressing a time or cross-rank sign.

One can also check P6a directly on adapted charts, which records the potentially hidden ambient-block sign. An adapted chart identifies both \(i_j\) and its normal zero section with the same map \(U_j\times\{0\}\hookrightarrow U_j\times\mathbb R^{c_j}\). O13's positive-time counit normalization identifies their relative lines by the actual chart identification: after retaining and canceling the common right-hand time factor, its local comparison is the identity for this same zero-section map. On products, regrouping the adapted coordinates
\((x_1,v_1,x_2,v_2)\mapsto(x_1,x_2,v_1,v_2)\)
moves the first normal block past the second tangent block. Its determinant sign is \((-1)^{c_1\dim M_2}\). The identical diffeomorphism acts on both the ambient-embedding and normal-zero-section product diagrams. Naturality of exceptional-product adjuncts under this diffeomorphism makes the two local diagrams identical diagrams of the same counits. On shifted determinant lines the corresponding derived braids are retained on both sides; the determinant sign is not discarded because it occurs twice. Arbitrary changes of adapted chart preserve these counit diagrams, so the local equality glues, without chosen global orientations. This gives the same P6a as the parameter-pasting proof.

### 3. The R4 external-product square

Define the left-ordered shuffle
\[
\begin{aligned}
b_L:(\Omega_1\otimes U_1)\boxtimes(\Omega_2\otimes U_2)
&\xrightarrow{\ 1\otimes\sigma_{U_1,\Omega_2}\otimes1\ }
(\Omega_1\boxtimes\Omega_2)\otimes(U_1\boxtimes U_2)\\
&\xrightarrow{\ \kappa\otimes1\ }
\Omega\otimes(U_1\boxtimes U_2).
\end{aligned}
\tag{P7}
\]
The assertion about the original maps is
\[
K\,(D_1(A_1)\boxtimes D_2(A_2))
=R\pi_!(\mu)\,D(A_1\boxtimes A_2)\,b_L.
\tag{P8}
\]
In a homogeneous coefficient notation the explicit coefficient-line shuffle in P7 is \((-1)^{c_2|U_1|}\). This notation records a chain-level symmetry; the proof applies to arbitrary complexes, not only homogeneous modules.

#### 3a. A natural reduction covering every input

Put \(V_i=R\tau_{i*}A_i\). The ordinary adjunction counit gives
\[
q_i:\tau_i^{-1}V_i\longrightarrow A_i.
\tag{P9}
\]
SH02-CON-RADIAL-STAR proves that \(e_i^{-1}q_i\) is an isomorphism: its definition is the contraction map in that theorem. Original R4 is natural and invertible, so its naturality square implies
\[
R\pi_{i!}T_i(q_i)\text{ is an isomorphism}.
\tag{P10}
\]
The product \(q_1\boxtimes q_2\) is a map of conic objects whose zero restriction is the tensor of two isomorphisms. Applying original R4 on \(E\) gives the same conclusion for its compact Fourier image. Naturality of FF20, Künneth and the line shuffles makes P8 natural in both inputs. Consequently P8 for \(\tau_i^{-1}V_i\) implies P8 for \(A_i\), by cancellation of the displayed isomorphisms.

This is not a constant-generator argument. It constructs an actual comparison from arbitrary base complexes \(V_i\) to each particular input and proves that the functors in the square invert that comparison. No claim that \(R\tau_*\), zero restriction, or ordinary recovery is conservative on all conic sheaves is made.

#### 3b. The comparison for arbitrary base coefficients

Now let \(A_i=\tau_i^{-1}V_i\), for arbitrary \(V_i\) in the stated domain. The actual Fourier kernel and proper projection formula identify \(T_iA_i\) with an object supported on the dual zero section. Indeed, over a nonzero covector the normal integration fibre is a closed halfspace and has zero compact cohomology (FS3); over the zero covector there is no cut. Proper base change provides the restriction map, and the localization triangle identifies its closed zero-section extension. The coefficient \(V_i\) is carried through by the proper projection formula; no dualizability of \(V_i\) is needed. This also applies to the product input.

The support-forgetting map \(\nu_{\pi_i}\) is therefore an isomorphism on \(T_iA_i\). The existing full trace equation FTE34, specialized to \(e_i\), reads
\[
\nu_{\pi_i}\,D_i(A_i)=E_i(A_i)\,\theta_{e_i}(A_i),
\tag{P11}
\]
where \(E_i\) is original R2. Thus it suffices to compare the right sides of P11. This uses the original R4 and its already proved trace equation; it does not define R4 by a new trace convention.

Let \(z_i:s_i^{-1}T_iA_i\to R\tau_{i!}A_i\) be the no-cut proper base-change map, and let \(k_{\pi_i}^*\) and \(k_{\tau_i}^!\) be the actual conic contraction maps. REC5 proves
\[
z_i k_{\pi_i}^* E_i(A_i)=k_{\tau_i}^!.
\tag{P12}
\]
Under these specified maps, the right side of P11 becomes
\[
\Omega_i\otimes V_i
\xrightarrow{\theta_{e_i}(\tau_i^{-1}V_i)}e_i^!\tau_i^{-1}V_i
\xrightarrow{k_{\tau_i}^!}R\tau_{i!}\tau_i^{-1}V_i.
\tag{P13}
\]
Its product compatibility follows by expanding these two maps. The first map is the trace comparison whose adjunct is projection formula followed by the zero-section counit. The second map is proper image of that same support counit. On taking the product, proper Künneth and projection-formula pasting leave the tensor product of the two zero-section counits. On taking the product embedding first, the adjunct of \(\operatorname{Ex}_{e_1,e_2}\) is, by P4, that identical tensor product of counits. The relative-line extraction for the two projections is precisely P6. Thus the two composites are equal, including the shuffle in P7. This reasoning is an equality of module/counit maps with the coefficients \(V_1,V_2\) retained throughout; it does not use a general exceptional Künneth isomorphism for arbitrary sheaves.

Finally restrict the actual FF20 map to the dual zero section. Both \(\langle x_1,\xi_1\rangle+\langle x_2,\xi_2\rangle\leq0\) and the pair of separate inequalities become the whole product normal fibre. Their kernel restriction map is therefore the identity, and the remaining comparison is exactly proper Künneth. It consequently intertwines the two no-cut maps \(z_i\) with the product no-cut map. All the Fourier objects currently being compared are supported on the dual zero section, so its restriction and the support-forgetting identifications detect the equality. Combining this observation with P11–P13 proves P8 on the pullback inputs. Part 3a proves P8 on all inputs in the stated domain.

### 4. The selected compact recoveries

Define the linear right-ordered recovery
\[
\ell_i=\sigma_{\Omega_i,U_i}D_i(A_i)^{-1}:
R\pi_{i!}T_iA_i\longrightarrow U_i\otimes\Omega_i.
\tag{P14}
\]
Here the symmetry has source \(\Omega_i\otimes U_i\), as displayed; its subscript order is not interchangeable with its target order. Define \(\ell\) similarly. REC8 states \(Z_iD_i=(-1)^{c_i}\sigma_{\Omega_i,U_i}\), so
\[
\ell_i=(-1)^{c_i}Z_i,\qquad \ell=(-1)^{c_1+c_2}Z.
\tag{P15}
\]
Define the right-ordered shuffle
\[
b_R=(1\otimes\kappa)
 (1_{U_1}\otimes\sigma_{\Omega_1,U_2}\otimes1_{\Omega_2}).
\tag{P16}
\]
Its source is \((U_1\otimes\Omega_1)\boxtimes(U_2\otimes\Omega_2)\), and its target is \((U_1\boxtimes U_2)\otimes\Omega\). The coefficient-line braid contributes \((-1)^{c_1|U_2|}\). Symmetric-monoidal coherence, or expanding the three indicated interchanges, gives P8 in the equivalent form
\[
\ell\,R\pi_!(\mu^{-1})K=b_R(\ell_1\boxtimes\ell_2).
\tag{P17}
\]
The parity normalizations are multiplicative: \((-1)^{c_1+c_2}=(-1)^{c_1}(-1)^{c_2}\). Thus P17 is also the product equation for the literal \(Z\) maps with this same \(b_R\). In particular there is no additional free cross-rank scalar attached to the Fourier product comparison. The cross-rank sign in P6 and coefficient-line sign in P16 must still be retained inside their specified orientation and symmetry maps.

### 5. The microlocalization external-product square

Let \(i_j:M_j\hookrightarrow X_j\) be closed smooth embeddings of codimensions \(c_j\), and let \(F_j\in D^b(k_{X_j})\) be arbitrary. Work in the manifold scope of SH02-MIC-ZERO and impose its existing bounded microlocalization contracts. Put \(A_j=\nu_{M_j}F_j\), \(H_j=\mu_{M_j}F_j\), \(F=F_1\boxtimes F_2\), and \(i=i_1\times i_2\). Let
\[
\chi:A_1\boxtimes A_2\longrightarrow\nu_{M_1\times M_2}F
\tag{P18}
\]
be exactly SH02-SP-EXTERNAL. Let \(u_j:i_j^{-1}F_j\to e_j^{-1}A_j\) and \(u:i^{-1}F\to e^{-1}\nu F\) be the units of SH02-SP-ZERO. Then
\[
e^{-1}\chi\,(u_1\boxtimes u_2)=u.
\tag{P19}
\]
To check the map, expand SP-EXTERNAL: the external \(Rj_*\) comparison is adjoint to the identity of the two positive-chamber coefficients, and ordinary base exchange restricts to the equal-time locus. Precomposing by the two ordinary units leaves the ordinary unit for that equal-time positive chamber, by unit naturality and the two counit triangles. Restricting to the central zero section gives exactly P19. This proof uses the actual ordinary base-exchange morphism, without asserting it invertible elsewhere. The normal product and ambient coefficient identifications here are ordinary inverse-image identifications, so this step adds no orientation shift or sign.

MIC19 is \(T_E(\chi)\mu^{-1}\). Apply naturality of P14 and then P17 and P19. With the normal-to-ambient line comparisons MEP5/O13, the selected recovery REC16 satisfies the following exact square:
\[
\begin{array}{ccc}
R\pi_{1!}H_1\boxtimes R\pi_{2!}H_2
&\xrightarrow{\ R\pi_!(\mathrm{MIC19})K\ }&
R\pi_!\mu_{M_1\times M_2}(F_1\boxtimes F_2)\\
{r_{F_1}^!\boxtimes r_{F_2}^!}\downarrow&&\downarrow {r_F^!}\\
(i_1^{-1}F_1\otimes\omega_{i_1})\boxtimes(i_2^{-1}F_2\otimes\omega_{i_2})
&\xrightarrow{\ b_R\ }&i^{-1}(F_1\boxtimes F_2)\otimes\omega_i.
\end{array}
\tag{P20}
\]
In the bottom arrow \(\kappa\) is the actual exceptional product for the embeddings, identified with the normal-bundle map above by counit pasting and MEP5/O13. Naturality of those counit-normalized comparisons makes the substitution legitimate. Locally closed embeddings are treated by restriction to suitable ambient open sets; all constructions commute with those restrictions.

### 6. Boundary of this lemma

P20 proves external-product compatibility of the selected compact microlocal recoveries, with the actual MIC19, original R4, coefficient braids and product orientation map. It does not by itself prove the subsequent inverse/direct microlocal comparison compatibilities for a multi-kernel composition, internal-Hom compact recovery, its constructibility-dependent formula, or all of MH30/MH31. Those are separate map calculations. Nor does this lemma prove that the raw inverse presentation \(Q\to S\) is monoidal for an independently selected product map. That stronger assertion is unnecessary for the counit reduction above and has not been silently imported.

## SH02-MHPR-PASTE — Typed MH30/MH31 composition pastes

### 1. Product squares and their endpoint maps

Let \(i:M\hookrightarrow X\), \(j:N\hookrightarrow Y\) be the embeddings of REC1, of codimensions \(c,d\). Write
\[
 H=\mu_MK,\quad J=\mu_NL,\quad P=K\boxtimes L,\quad
 I=i\times j,\quad H_P=\mu_{M\times N}P,
\]
and let \(\pi_i,\pi_j,\pi_I=\pi_i\times\pi_j\) denote conormal projections. All objects lie in the stated bounded ranges. Let
\[
 m_{K,L}:H\boxtimes J\longrightarrow H_P
\]
be exactly MIC19, built from the specialization external comparison and the specified Fourier product map. It is not replaced by an arbitrary map or asserted to be invertible.

For \(\epsilon=*,!\), let \(\kappa_\epsilon\) denote the actual external direct-image comparison
\[
 R\pi_{i\epsilon}H\boxtimes R\pi_{j\epsilon}J
 \longrightarrow R\pi_{I\epsilon}(H\boxtimes J).
\]
The \(*\) map is the mate of the tensor product of the ordinary evaluation counits. The \(!\) map uses the external projection formula and proper-support base change. No invertibility of the \(*\) map is needed.

The ordinary square to prove is
\[
\begin{array}{ccc}
R\pi_{i*}H\boxtimes R\pi_{j*}J
 &\xrightarrow{R\pi_{I*}(m)\,\kappa_*}&R\pi_{I*}H_P\\
r_K^*\boxtimes r_L^*\downarrow&&\downarrow r_P^*\\
i^!K\boxtimes j^!L&\xrightarrow{\chi_!}&I^!(K\boxtimes L).
\end{array}
\tag{S1}
\]
Here every \(r^*\) is REC6. The bottom map \(\chi_!\) is the exceptional external-product comparison: its adjunct is the product of the support counits \(i_*i^!K\to K\) and \(j_*j^!L\to L\), using \(I_*(A\boxtimes B)\simeq i_*A\boxtimes j_*B\). This definition fixes the map without imposing dualizability or constructibility.

Set \(U=i^{-1}K\), \(V=j^{-1}L\), \(\Omega_i=\omega_i\), \(\Omega_j=\omega_j\). Let
\[
 \lambda_{i,j}:\Omega_i\boxtimes\Omega_j\longrightarrow\Omega_I
\]
be the ordered, counit-normalized orientation isomorphism for the product embedding. It includes the specified tangent/normal and shifted-line permutations. The compact square to prove is
\[
\begin{array}{ccc}
R\pi_{i!}H\boxtimes R\pi_{j!}J
 &\xrightarrow{R\pi_{I!}(m)\,\kappa_!}&R\pi_{I!}H_P\\
r_K^!\boxtimes r_L^!\downarrow&&\downarrow r_P^!\\
(U\otimes\Omega_i)\boxtimes(V\otimes\Omega_j)
 &\xrightarrow{\chi_{\rm or}}&(U\boxtimes V)\otimes\Omega_I.
\end{array}
\tag{S2}
\]
Every \(r^!\) is precisely REC16. The bottom edge is
\[
 U\otimes\Omega_i\otimes V\otimes\Omega_j
 \xrightarrow{1\otimes\sigma_{\Omega_i,V}\otimes1}
 U\otimes V\otimes\Omega_i\otimes\Omega_j
 \xrightarrow{1\otimes\lambda_{i,j}}
 U\otimes V\otimes\Omega_I,
\tag{S3}
\]
with the omitted projection pullbacks understood. This is a typed map on \(M\times N\), not an unqualified equality of four tensors.

The statements use arbitrary bounded inputs and the finite global-dimension coefficient contract of REC1. They add no properness, noncharacteristic, perfect-stalk, orientability, or constructibility hypothesis. The proofs of S1 and S2 are C5 and P20 above. Their equality is an equality of the specified maps, not an inference from the existence of the four corner objects.

### 2. Signs that may not be suppressed

The line \(\Omega_i=\operatorname{or}_i[-c]\) has parity \(c\). On a homogeneous coefficient \(v\), the crossing in S3 contributes \((-1)^{c|v|}\). The map \(\lambda_{i,j}\) is still required after that crossing; an unsigned identification of the two inverse orientation lines is not a substitute for it.

The REC16 scalar is multiplicative in rank:
\[
 (-1)^{c+d}=(-1)^c(-1)^d.
\tag{S4}
\]
Thus passing from the unmodified FS14 recoveries to REC16 creates no additional product scalar. This elementary observation does not prove that the raw FS14 recovery commutes with the chosen Fourier product: that particular natural-transformation identity must be established in the external-normalization proof. Nor does S4 remove any Koszul crossing of coefficients or orientation lines.

Forgetting proper support gives a comparison from the top row of S2 to the top row of S1. Under REC19 its lower comparison is the product of the relative traces
\(U\otimes\Omega_i\to i^!K\) and \(V\otimes\Omega_j\to j^!L\), versus the relative trace for \(I\). Its commutativity is the product counit identity with S3's braid. This is a useful consistency check. The trace need not be invertible, so it cannot be used to infer S1 from S2 or conversely by cancellation.

### 3. What this supplies for MH21 and MH30

For MH21, substitute the two Hom kernels into S1/S2 and then use naturality of recovery with respect to the kernel evaluation map defining MH21. This proves compatibility at the recovered kernel level. The ordinary endpoint is subsequently identified using exceptional internal-Hom adjunction. Compact endpoints remain
\(\Delta^{-1}K\otimes\omega_\Delta\) unless the separately stated constructible external-Hom exchange is invoked with its actual hypotheses. S2 alone never supplies that exchange.

For the graph-composition construction, retain MH's notation
\[
 Q=X\times Y\times Y\times Z,\quad
 W=X\times Y\times Z,\quad
 M=\Gamma_f\times\Gamma_g,\quad L=j^{-1}M,
\]
where \(j\) repeats the middle coordinate and \(q:W\to X\times Z\) forgets it. Put \(T=\Gamma_h\), \(a:M\hookrightarrow Q\), \(b:L\hookrightarrow W\), \(c:T\hookrightarrow X\times Z\), and \(\ell=q|_L:L\to T\). The map \(\ell\) is the specified isomorphism, even if \(q\) is not proper. Let \(t=j|_L\).

The normal map for \(j\) is an isomorphism. Its ordinary-recovery comparison is the actual support/base-change morphism
\[
 t^{-1}a^!P\longrightarrow b^!j^{-1}P.
\tag{S5}
\]
This does not assert that S5 is invertible. The corresponding compact endpoint uses ordinary pullback and the orientation identification furnished by that same normal isomorphism. A proof may use these endpoints by pasting the defining specialization base-change maps and the no-cut REC5 Fourier map. Mere transversality does not permit replacing MIC14 by an isomorphism.

The final direct-image comparison is followed by the actual counit \(Rq_!q^!K_h\to K_h\), where \(K_h=R\mathcal Hom(H_z,F_x\otimes\omega_Z)\). At the ordinary endpoint its precise support morphism is
\[
 R\ell_!b^!D\longrightarrow c^!Rq_!D.
\tag{S6}
\]
Define S6 by applying \(Rq_!\) to \(b_*b^!D\to D\), identifying \(Rq_!b_*\simeq c_*R\ell_!\), and taking the \(c_*\dashv c^!\) adjunct. Taking \(D=q^!K_h\) and following S6 by \(c^!\) of the \(q\)-counit gives
\[
 R\ell_!b^!q^!K_h\simeq R\ell_!\ell^!c^!K_h
 \longrightarrow c^!K_h,
\tag{S7}
\]
the counit for the isomorphism \(\ell\). The equality is the transitivity identity of exceptional counits, not a properness assertion for \(q\). The conormal restriction in MH29 preserves zero sections, so ordinary conic contraction is compatible with it. It introduces no independent middle covector or integration at this ordinary endpoint.

Consequently S1/S2 for the selected MIC19 map, the existing actual transverse comparison, naturality at MH30, and the proper-direct comparison/counit paste establish compatibility of the construction with normalized product recovery and its ordinary recovered composition. The explicit endpoint maps S5--S7 are the short mate check that must appear or be cited precisely in that paste. These are consequences of the stipulated coherent base-change and counit definitions; no new support hypothesis is required.

This conclusion concerns that specified paste. It does not assert a separate universal formula expressing a compact endpoint as a tensor of a dual and an arbitrary sheaf. The raw compact endpoint does permit the typed comparison below. Integration after restricting a conormal bundle to the zero-middle-covector locus must not be replaced without proof by compact integration over the whole conormal bundle; the reason that replacement is legitimate on the final MH30 target is explicit below.

#### 3a. The compact q-stage: the actual mate and its line order

Let \(r:C\hookrightarrow N_L^*W\) be the closed vector-bundle inclusion of the zero-middle-covector locus, and identify \(C\) with \(N_T^*(X\times Z)\) using \(\ell\). The ambient projection \(q\) is a submersion and \(\ell\) is an isomorphism. Thus the lower inverse comparison of MIC13 is the actual isomorphism
\[
 b_q:\mu_Lq^!K_h\xrightarrow{\sim}r_*\mu_TK_h.
\tag{S10}
\]
This is precisely the MIC-SMOOTH case: the ambient map and its submanifold map are submersions. It is not an assertion of invertibility for the earlier merely transverse map \(j\).

Set \(D=\mu_Lq^!K_h\), \(V=\mu_TK_h\). The direct-image comparison followed by the ambient counit, denoted \(u_q:r^{-1}D\to V\), is the mate of S10, by MIC15/MIC17:
\[
 u_q=\epsilon_{r^{-1},r_*}\,r^{-1}(b_q).
\tag{S11}
\]
Here the conormal base map is the isomorphism \(\ell\), so it contributes only that identified transport, and \(r^{-1}\dashv r_*\) is the remaining adjunction. Let \(\eta_r:D\to r_*r^{-1}D\) be its unit. Naturality of this unit followed by the triangle identity gives the equality of maps on the entire normal bundle
\[
 r_*u_q\,\eta_r
 =r_*\epsilon_{r^{-1},r_*}\,r_*r^{-1}(b_q)\,\eta_r
 =r_*\epsilon_{r^{-1},r_*}\,\eta_{r_*V}\,b_q
 =b_q.
\tag{S12}
\]
The proper projection of the left side is exactly compact restriction to the zero-middle-covector locus, the direct comparison, and the \(q\)-counit. Therefore its compact pushforward equals that of the actual smooth inverse comparison S10. In particular \(D\) is supported on the image of \(r\); this support assertion is justified on \(q^!K_h\), not on an arbitrary preceding kernel.

Here is the full ordered endpoint of that map. Use the specified left-ordered smooth trace isomorphism
\[
 \theta_q^L(K_h):\omega_q\otimes q^{-1}K_h\xrightarrow{\sim}q^!K_h.
\]
On \(L\), write \(S=b^{-1}q^{-1}K_h=\ell^{-1}c^{-1}K_h\), \(Q_q=b^{-1}\omega_q\), and let
\[
 t_{b,q}:\Omega_b\otimes Q_q\xrightarrow{\sim}\ell^{-1}\Omega_c
\]
be exceptional transitivity for \(qb=c\ell\), including the counit-normalized trivialization of \(\omega_\ell\) for the isomorphism \(\ell\). Then the compact endpoint is
\[
\begin{aligned}
\beta_q:
b^{-1}q^!K_h\otimes\Omega_b
&\xrightarrow{\ b^{-1}(\theta_q^L)^{-1}\otimes1\ }
Q_q\otimes S\otimes\Omega_b\\
&\xrightarrow{\ \sigma_{Q_q,S}\otimes1\ }
S\otimes Q_q\otimes\Omega_b\\
&\xrightarrow{\ 1\otimes\sigma_{Q_q,\Omega_b}\ }
S\otimes\Omega_b\otimes Q_q\\
&\xrightarrow{\ 1\otimes t_{b,q}\ }
S\otimes\ell^{-1}\Omega_c.
\end{aligned}
\tag{S13}
\]
This records separately the crossing that puts the sheaf coefficient first and the crossing that puts the two relative lines into exceptional-transitivity order. If right-ordered smooth purity is used initially, its inverse already includes the first crossing; it must not be counted again. Neither crossing is optional.

To identify the selected REC16 recoveries with S13, straighten the submersion locally by the coordinates \((x,z,y-g(z))\). The pair is then the product of \((X\times Z,T)\) with \((\mathbb R^{\dim Y},0)\), and \(q\) is the first projection. The smooth input is the first kernel tensored with the second factor's dualizing line, in exactly the order specified by \(\theta_q^L\). Apply the proved compact external square S2 (P20 above) to this product. The second microlocal factor is supported on its zero section. Its compact recovery and projection counit have coefficient one under REC16: REC19 on this supported factor identifies that counit with the specified smooth/zero-section composite trace. Exceptional counit transitivity is exactly \(t_{b,q}\), and the reordering into right-ordered compact endpoints is the two braids displayed in S13. This identifies the compact pushforward of S10 with S13. Changes between these product coordinates preserve the defining counits; the normal orientation comparisons MEP5/O13 retain their determinant signs, so these local equalities glue. This is a reduction to the proved product square and the existing trace maps, not an assertion that arbitrary exceptional Künneth maps are isomorphisms.

For the transverse \(j\)-stage, the normal fibre isomorphism and its counit-normalized orientation map identify the compact endpoints with ordinary pullback. The defining specialization ordinary inverse comparison carries the restriction unit on the source to the pulled-back restriction unit. Restricting its positive-chamber base-change definition to the zero normal section, then using the unit/counit triangles, proves this statement with the same units as REC3/REC4. The Fourier normal isomorphism is a coordinate-change map, so its no-cut comparison commutes with the chosen proper contraction. Thus this step adds the specified normal orientation identification and no new scalar. In particular no noncharacteristic assumption or unjustified invertibility of MIC14 enters the paste.

#### 3b. A typed compact composition statement, with raw endpoints

For MH31 put
\[
 K_{ij}=R\mathcal Hom(q_2^{-1}F_i,q_1^!F_j),\qquad
 C_{ij}=\Delta^{-1}K_{ij}\otimes\omega_\Delta.
\]
Let \(\rho^!_{ij}:R\pi_!A_{ij}\to C_{ij}\) be REC16. The bottom composition map \(c_C:C_{12}\otimes C_{23}\to C_{13}\) is defined without a duality formula:

1. Apply \(\sigma_{C_{12},C_{23}}\), since MH30 takes \(K_{23}\) before \(K_{12}\).
2. Apply the product braid S3, pull to the diagonal base, and use the transverse normal orientation identification \(t^{-1}\Omega_a\simeq\Omega_b\). The resulting kernel coefficient is \(b^{-1}j^{-1}(K_{23}\boxtimes K_{12})\), with \(\Omega_b\) on its right.
3. Apply \(b^{-1}(\mathrm{MH30})\otimes1_{\Omega_b}\).
4. Apply S13, obtaining \(\Delta^{-1}K_{13}\otimes\omega_\Delta=C_{13}\).

The compact lax tensor map \(\kappa_!^{\Delta}\) used here is concrete: proper Künneth over the base first maps into proper pushforward from \(T^*X\times_XT^*X\), then the unit for its closed diagonal restricts to \(A_{12}\otimes A_{23}\), and transitivity gives \(R\pi_!(A_{12}\otimes A_{23})\). This yields the fully typed square
\[
\begin{array}{ccc}
R\pi_!A_{12}\otimes R\pi_!A_{23}
 &\xrightarrow{R\pi_!(m)\,\kappa_!^{\Delta}}&R\pi_!A_{13}\\
\rho^!_{12}\otimes\rho^!_{23}\downarrow&&\downarrow\rho^!_{13}\\
C_{12}\otimes C_{23}&\xrightarrow{c_C}&C_{13}.
\end{array}
\tag{S14}
\]
The required proof is the pasted S2, the just-described transverse unit comparison, naturality at MH30, and S12/S13. This constructs a map between raw compact kernel endpoints. It is not a claim that those endpoints equal \(D'F_i\otimes F_j\) or \(R\mathcal Hom(F_i,F_j)\) for unrestricted inputs.

![Compact graph-composition recovery through raw diagonal restrictions, with the ordinary derived source order below](../assets/composition-recovery-square.png)

The square is S14. Its upper arrow is \(R\pi_!(m)\kappa_!^\Delta\)
from \(R\pi_!A_{12}\otimes R\pi_!A_{23}\) to \(R\pi_!A_{13}\);
the vertical arrows are the selected REC16 maps \(\rho^!_{ij}\).
The lower arrow \(c_C:C_{12}\otimes C_{23}\to C_{13}\) retains the
raw endpoints \(C_{ij}=\Delta^{-1}K_{ij}\otimes\omega_\Delta\).
Its construction first exchanges graph-factor order, then applies the
S3 relative-line braid and transverse normal-line identification,
then the actual MH30 kernel map, and finally the S13 exceptional trace
and braids. No unrestricted compact-Hom identification is inserted.
The lower annotation points forward to S8--S9 in the next subsection:
the ordinary composition source
order \(A_{12}\otimes A_{23}\) requires the derived symmetry and sends
homogeneous \(a\otimes b\) to \((-1)^{|a||b|}b\circ a\).
The diagram is a schematic of the typed paste at S14 and the separate
ordinary square at S8--S9, under the lesson's stated ring, boundedness,
and manifold hypotheses. The underlying graph Hom and diagonal recovery
constructions are compared with published sources at the end of the lesson;
the ordered composition, raw compact endpoints and selected normalization
are established by the S1–S14 calculations here. The figure and explanatory
routing are original course material; its PNG and SVG share this lesson's CC0 1.0 dedication. A
vector copy of the composition square
preserves the labels.

Finally, the MH30 kernel evaluation must itself retain its orientation ordering. Evaluation of \(K_f\otimes K_g\otimes H_z\) first gives \(F_x\otimes\omega_Y\otimes\omega_Z\). In the right-ordered smooth purity presentation of \(q^!K_h\), the corresponding target for its Hom adjunct is \(F_x\otimes\omega_Z\otimes\omega_Y\). The required map between these is \(1_{F_x}\otimes\sigma_{\omega_Y,\omega_Z}\). Transpose this evaluated map using internal Hom and exceptional adjunction; if the left-ordered presentation \(\theta_q^L\) is then used, include its coefficient-line symmetry as in S13. This avoids expressing a single scalar in terms of unspecified homogeneous evaluation inputs. Together with step 1 above, it retains both the initial graph-factor symmetry and the \(\omega_Y/\omega_Z\) braid.

### 4. The final ordinary-composition square and source order

Let \(A_{12}=\mathsf M_X(F_1,F_2)\), \(A_{23}=\mathsf M_X(F_2,F_3)\), \(A_{13}=\mathsf M_X(F_1,F_3)\), and let \(\rho_{ij}:R\pi_*A_{ij}\to R\mathcal Hom(F_i,F_j)\) be REC6 followed by the specific graph internal-Hom adjunction. With \(m\) the actual MH31 map, the typed ordinary square is
\[
\begin{array}{ccc}
R\pi_*A_{12}\otimes R\pi_*A_{23}
 &\xrightarrow{R\pi_*(m)\,\kappa_*}&R\pi_*A_{13}\\
\rho_{12}\otimes\rho_{23}\downarrow&&\downarrow\rho_{13}\\
R\mathcal Hom(F_1,F_2)\otimes R\mathcal Hom(F_2,F_3)
 &\xrightarrow{\operatorname{comp}\circ\sigma}&R\mathcal Hom(F_1,F_3).
\end{array}
\tag{S8}
\]
The source order matters. Standard closed-monoidal composition has the reversed source order: the map from \(R\mathcal Hom(F_2,F_3)\otimes R\mathcal Hom(F_1,F_2)\) evaluates the first input after the second. Accordingly the bottom map in S8 sends homogeneous \(a\otimes b\) to
\[
 (-1)^{|a||b|}\,b\circ a
\tag{S9}
\]
in the usual cochain Hom model. This follows already at a point, where all orientation factors have rank zero. The MH27 construction explicitly applies this initial derived symmetry to reach the MH30 source order.

MH31 states that its written-order map is \(\operatorname{comp}\circ\sigma\), giving S9, while degree-zero arrows compose in the familiar order. This keeps the derived source-order symmetry explicit and does not change any REC normalization.

An unsigned reversed composition is not a chain map in general: \(d(ba)=(db)a+(-1)^{|b|}b(da)\), while the tensor differential on \(a\otimes b\) places its sign after \(a\). The Koszul factor in S9 reconciles these different orders. Any final statement that advertises compatibility of the actual derived composition maps must preserve it.

## SH02-MHPR-BOUNDARY — Exact scope and dependencies

The result concerns the selected REC recoveries and the specified MIC19/MH30/MH31 composition. It establishes equality of the named maps by kernel restriction, units, counits, and their mates. It does not establish invertibility of an arbitrary SP external comparison, arbitrary transverse MIC comparison, or arbitrary exceptional external-product map. It does not replace a graph-Hom boundedness contract by a theorem for an unbounded internal Hom, does not add constructibility, and does not reprove the REC or MEP results. The individually stated operation, specialization, Fourier and graph-Hom prerequisites remain separate dependencies.

The specific prerequisite maps used here are REC1–REC20 in SH02-MIC-ZERO, MIC12–MIC19 in microlocalization, MH21 and MH26–MH32 in [microlocal Hom](microlocal-hom.md), and the stated original R2/R4, FF20, FTE34, MEP5/O13 and specialization maps in their owning units. Each prerequisite retains its own hypotheses and proof obligations.

For direct navigation to the named inputs, see
Fourier product,
[specialization zero](specialization.md#SH02-SP-ZERO) and
[external product](specialization.md#SH02-SP-EXTERNAL),
microlocal recovery and
external product,
the Fourier trace endpoint,
[normal counits](microlocal-endpoint-propagation.md#SH02-MEP-NORMAL-COUNITS),
and [graph composition](microlocal-hom.md#SH02-MH-GRAPH-COMPOSITION).
These dependencies retain their own scope and proof obligations; this
compatibility lesson does not prove them merely by invoking their labels.

**Published sources and proof mechanisms.** Schapira's [*A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §§4.1–4.4, pp. 19–23, gives the negative proper Fourier cut, the positive ordinary-support presentation, specialization through the positive deformation chamber, the microlocal recovery triangle, and the diagonal definition of microlocal Hom. Kashiwara and Schapira's [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Definition 2.3.1, Proposition 2.3.2 and Corollary 2.3.3, pp. 46–47 (PDF pp. 49–50), and Definition 5.5.1 and Proposition 5.5.2, pp. 91–92 (PDF pp. 94–95), supply earlier microlocal and graph-Hom recovery constructions. These passages explain the objects and recovery mechanisms used here. They do not fix this lesson's selected REC16 parity, the line order in C4/P15, or the actual product and composition squares C5 and S14.

The sheaf-operation part of the proof can be compared directly with Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Proposition 4.5.6, p. 94, and Propositions 4.6.4–4.6.8, pp. 95–97. The compact Künneth proof uses proper base change and the projection formula. The exceptional tensor comparison is defined by adjunction, and the Hom and diagonal identifications are derived through the same adjunction and projection formula. C6 and P6 retain those actual counits when multiplying relative orientations; C5 retains the ordinary external pushforward as a lax map. Thus the comparison does not silently assume either ordinary Künneth invertibility or exceptional external-product invertibility. The cited Künneth statement has bounded inputs; the bounded-below, finite-rank-bundle argument in P1–P20 still requires the course's wider finite-dimensional operation contracts.

The additional work is a compatibility proof for specified maps. P8 first reduces arbitrary conic inputs using the actual zero-section adjunction maps whose indicated recoveries are invertible; it does not assume that pulled-back constant sheaves generate the category or that ordinary bundle pushforward is conservative. The supported Fourier calculation then fixes the proper contraction and its coefficient. P6a has two complete comparisons of the normal and ambient relative orientation products: parameter base change and pasting of counits, and the adapted-chart calculation with the same ordered normal and tangent blocks on both sides. Positive deformation time fixes the local comparison, while the counits and tensor symmetries retain the cross-rank sign. Both arguments are part of the present proof, not consequences of the existence of a Sato triangle alone.

For graph composition, the support restriction is made at the final submersion stage only, after applying the smooth microlocal inverse isomorphism to its actual exceptional target. This is why C13–C15 and S10–S13 may use the zero-middle-covector locus without assuming that the earlier arbitrary kernel already has that support. S14 keeps raw diagonal restrictions as compact endpoints, and S8–S9 keeps the derived symmetry in the written Hom order. The compact-Hom triangle on p. 23 of the review assumes cohomological constructibility of its first input and cannot replace those raw endpoints for the arbitrary bounded complexes here. The two illustrations record the stated product and composition pastes; their arrows, orientation braids and homogeneous composition sign are fixed by these proofs.

This comparison identifies shared Fourier, deformation, support and adjunction mechanisms and the extra normalization work required here. It establishes no full-scope theorem merely from a source's availability and makes no assertion that the selected product and composition proof structures are historically independent of all other treatments. Every Fourier, specialization, operation and graph-Hom input listed above remains a separate obligation in its own coefficient and boundedness range.
