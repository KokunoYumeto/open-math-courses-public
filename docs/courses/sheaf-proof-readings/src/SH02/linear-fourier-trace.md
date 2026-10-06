# SH02-LFT. A linear map inside the Fourier comparison

Original programme text: CC0 1.0 Universal. The foundational comparison is with Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §§4.5–4.6 and §4.9](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=92): proper-support base change, exceptional adjunction and the right adjoint of a kernel transform. The proof here retains a potentially noninvertible support map and compares explicitly specified Fourier adjunctions. The final source account distinguishes these additional arguments from the cited foundation.

The first proof retains the middle support-forgetting arrow in the halfspace argument when the pairing is degenerate. That arrow need not be invertible. Its two descriptions give a linear support square with the direct kernel comparison defined below. The original FF L3 map differs from this direct map by a relative-rank sign, as proved for every bundle map in [The graded support comparison](fourier-graded-comparison.md). That supplement completes FTC13 by separately specifying the initial line extraction and final braided contraction. For the trace equation FTC14, the enhanced-center calculation here reduces the paired-adjunction defect to a base scalar, and the actual antipode transport determines its parity. [The complete transpose endpoint](fourier-transpose-endpoint.md) compares that direct endpoint with the full R3 rewrite and proves FTC14. Its proof retains the paired defect, exceptional antipode exchange and both line crossings; the scalar alone does not prove the equation.

## SH02-LFT-DOMAINS. The fixed maps and bounds

Let \(B\) be locally compact Hausdorff. Let \(E_i\to B\) be real vector bundles of fixed finite ranks \(n_i\), and let \(h:E_1\to E_2\) be a continuous bundle morphism over the identity. Its transpose is \(r:E_2^*\to E_1^*\). The rank of \(h_b\) may vary with \(b\). No local kernel bundle, constant-rank stratification, or manifold structure on \(B\) is assumed.

The coefficient ring \(k\) is commutative, unital, and of finite global dimension. All coefficient complexes belong to conic \(D^+\), with a global lower cohomological bound. They need not be constructible or have finite stalks. The bundle ranks give finite bounds for the proper-support cohomological dimensions of the bundle maps that occur. Consequently their exceptional inverse images exist on the stated category. A locally constant rank can be handled componentwise only when these bounds remain global.

We use the orientation lines, Koszul symmetries, and Fourier adjunctions fixed in [Fourier functoriality](fourier-functoriality.md). Put \(W_i=O_{E_i}[n_i]\), with positive dual orientation. On the source of \(r\),
\[
\omega_r=r^!k_{E_1^*}
 \simeq W_{2^*}\otimes W_{1^*}^{-1}.
\tag{LFT1}
\]
This is the transitivity identification of FF3a. Every suppressed orientation factor is pulled back from the indicated base. Adjacent inverse factors are evaluated by tensor duality; moving a factor uses the Koszul symmetry.

Write \(\nu_f:Rf_!\to Rf_*\) for the derived inclusion of sections with proper support into all sections. Write
\[
\bar\theta_f(K):f^{-1}K\longrightarrow
 f^!K\otimes\omega_f^{-1}
\tag{LFT2}
\]
when \(\omega_f\) is an invertible shifted line. This is FTC2 after inserting and evaluating the inverse line. Equivalently, before canceling that line, its exceptional adjunct is the projection formula followed by \(\operatorname{tr}_f\otimes1_K\). It is not assumed to be invertible for arbitrary \(K\).

The foundational dependencies are proper-support base change and composition on locally compact Hausdorff spaces, their mate and pasting identities, exceptional adjunction under the finite dimension bound, the bounded-factor projection formula and its \(D^+\) extension, vector-bundle orientation with its trace, and conic contraction at the zero section. The operation scope is SH02-FF-DOMAINS.

### SH02-LFT-IMP-BC-NU. Base change with its support map

On arbitrary locally compact Hausdorff spaces we use proper-support base
change and composition on \(D^+(k)\), ordinary inverse-image/direct-image
adjunction, and their unit, counit, and cartesian-pasting identities. In a
cartesian square the ordinary base-change morphism is the adjunct of the
pulled-back ordinary counit. The proper-support base-change isomorphism
intertwines the inclusion of proper-support sections with that ordinary
base-change morphism. This last assertion is the square LFT8 proved below,
with the actual derived support maps. For a product with a finite open
interval, the projection satisfies the cylinder comparison for arbitrary
pulled-back coefficients; successive such products give the restricted
ordinary base change in LFT15. This is the product-interval contract of
SH02-CON-CYLINDER, not an assertion of arbitrary nonproper base change.

### SH02-LFT-IMP-PF-ADJUNCTION. Exceptional adjunction and tensor factors

Whenever the proper-support functor on abelian sheaves has finite
cohomological dimension, we use its exceptional right adjoint on \(D^+\),
its transitivity, and the projection-formula and tensor–Hom adjunction
maps. The bounded-factor projection formula and the finite-global-
dimension truncation argument SH02-FF-BOUNDS supply the stated
\(D^+\) scope. These maps respect cartesian pasting and the units and
counits used in taking mates. A flat degree-zero closed-cut sheaf and
every bounded invertible orientation line satisfy these tensor bounds.

### SH02-LFT-IMP-ORIENTATION. Orientation traces and contraction

For a finite-rank vector-bundle projection the exceptional inverse image
is ordinary inverse image tensored with its shifted orientation line.
Its trace is fixed by the orientation evaluation
\(R\Gamma_c(\mathbb R^n;k)\otimes O[n]\to k\). The evaluation respects
base change and changes of fiber coordinates. In particular the lifted
trace in a bundle pullback square is the actual exceptional mate of
proper-support base change, as checked in SH02-FTC-BASE-TRACE. We also
use the natural conic contractions \(Rq_*K\simeq i^{-1}K\) and
\(Rq_!K\simeq i^!K\) for its zero section \(i\), and the specified
Fourier equivalence and first halfspace comparison SH02-FS-COMPARE.
No compatibility with an independently normalized second adjunction is
included in this contract.

## SH02-LFT-SQUARE. The ordinary base-change arrow in a trace calculation

Consider a cartesian square obtained by pulling a finite-rank vector bundle across a map \(b\):
\[
\begin{array}{ccc}
X'&\xrightarrow{u}&X\\
q\downarrow&&\downarrow q_0\\
Y'&\xrightarrow{b}&Y.
\end{array}
\tag{LFT3}
\]
Assume \(b_!\) has finite cohomological dimension and \(\omega_b\) is an invertible bounded line. Give \(\omega_u\simeq q^{-1}\omega_b\) its actual orientation-transitivity identification. Its counit square is FTC9b. There is always an ordinary base-change morphism
\[
\beta:b^{-1}Rq_{0*}K\longrightarrow Rq_*u^{-1}K.
\tag{LFT4}
\]
No assertion that \(\beta\) is an isomorphism is made. There is, however, an isomorphism
\[
\chi:b^!Rq_{0*}K\xrightarrow{\sim}Rq_*u^!K.
\tag{LFT5}
\]
It is the right adjoint mate of proper-support base change
\(q_0^{-1}Rb_!\simeq Ru_!q^{-1}\), with both sides viewed as functors from \(Y'\) to \(X\).

**Trace square.** The following two composites agree:
\[
\begin{aligned}
b^{-1}Rq_{0*}K
&\xrightarrow{\bar\theta_b}b^!Rq_{0*}K\otimes\omega_b^{-1}
 \xrightarrow{\chi}Rq_*(u^!K\otimes q^{-1}\omega_b^{-1}),\\
b^{-1}Rq_{0*}K
&\xrightarrow{\beta}Rq_*u^{-1}K
 \xrightarrow{Rq_*\bar\theta_u}
 Rq_*(u^!K\otimes q^{-1}\omega_b^{-1}).
\end{aligned}
\tag{LFT6}
\]

**Proof.** Keep the factor \(\omega_b\) on the left before taking the mate, and postpone all displayed inverse-line cancellations. Under \(Rb_!\dashv b^!\), the adjunct of the first route is
\[
Rb_!(\omega_b\otimes b^{-1}Rq_{0*}K)
 \xrightarrow{\mathrm{PF}}
 Rb_!\omega_b\otimes Rq_{0*}K
 \xrightarrow{\operatorname{tr}_b\otimes1}
 Rq_{0*}K.
\tag{LFT7}
\]
For the second route, expand \(\beta\) as the ordinary adjoint of pullback of the ordinary counit, and expand \(\chi^{-1}\) as the right mate of the displayed proper-support base-change isomorphism. Substituting the right-mate formula FF10 inserts one ordinary unit and its matching counit. Their triangle identity cancels them. What remains is the proper-support base-change comparison applied to \(\omega_b\), followed by the lifted trace
\(Ru_!\omega_u\to k_X\), tensored with \(K\). The counit square FTC9b identifies this with pullback of \(\operatorname{tr}_b\), tensored with the same coefficient. Projection-formula naturality then gives exactly LFT7. This calculation is a pasting of the ordinary counit square and the exceptional counit square; it does not invert \(\beta\). The adjunction bijection proves the equality before canceling the line, and evaluation gives LFT6. Since all orientation factors are bounded invertible lines, extracting them through \(Rq_*\) is valid on arbitrary \(D^+\). \(\square\)

We will also use a related support identity, valid for any cartesian square for which the proper-support base change is available. Under that base-change isomorphism, the composite
\[
b^{-1}Rq_{0!}K\xrightarrow{b^{-1}\nu_{q_0}}
b^{-1}Rq_{0*}K\xrightarrow{\beta}Rq_*u^{-1}K
\tag{LFT8}
\]
is \(\nu_q:Rq_!u^{-1}K\to Rq_*u^{-1}K\). Before derivation both maps pull back a section with proper support and then regard it as an unrestricted section. The derived base-change maps use that same inclusion. Equivalently the ordinary counit definition of \(\beta\) and proper-support base change give this identity by taking the ordinary adjoint. Thus LFT8 specifies equality of the arrows even when ordinary base change fails to be invertible.

## SH02-LFT-DEGENERATE. Keep the middle arrow of the halfspace chain

Set
\[
Y=E_1\times_BE_2^*,\qquad
q:Y\to E_2^*,\qquad s:Y\to E_1,
\]
and define the closed sets
\[
N=\{(x,\eta):\langle h(x),\eta\rangle\leq0\},
\qquad C=\{(x,\eta):\langle h(x),\eta\rangle\geq0\}.
\tag{LFT9}
\]
For a conic \(A\in D^+(E_1;k)\), put \(L=s^{-1}A\), \(H=R\Gamma_C L\), and \(D=H_N\). Here the subscript is tensor restriction with extension by zero, whereas \(R\Gamma\) is local cohomology.

**Lemma.** There is a canonical composite
\[
\Psi_h(A):Rq_!L_N
 \xleftarrow{\sim}Rq_!R\Gamma_C(L_N)
 \xrightarrow{\sim}Rq_!D
 \xrightarrow{\nu_q}Rq_*D
 \xleftarrow{\sim}Rq_*H.
\tag{LFT10}
\]
The backward arrows mean that their proved inverses are used in the resulting map from the first object to the last. Only the middle support arrow may fail to be invertible.

**Proof.** The halfspace localization argument FS5 applies to the two inequalities in LFT9 even when the bilinear form is degenerate. Indeed the open complement of \(N\) lies in the interior of \(C\), and its closure lies in \(C\). Applying \(R\Gamma_C\) to the tensor-cut triangle gives the natural isomorphism
\(R\Gamma_C(L_N)\simeq(R\Gamma_C L)_N\).

All these objects are conic for scaling \(x\). Let \(i:E_2^*\to Y\) be the zero section in that variable. Since \(i(E_2^*)\subset C\), the local-support map induces
\(i^!R\Gamma_C(L_N)\simeq i^!L_N\). The natural conic contraction \(Rq_!\simeq i^!\) therefore makes the first backward arrow invertible. Similarly \(i(E_2^*)\subset N\), so \(i^{-1}H\to i^{-1}H_N\) is invertible; conic contraction \(Rq_*\simeq i^{-1}\) gives the last backward arrow. None of these steps asserts that \(D\) is proper over \(E_2^*\).

For clarity, the vanishing argument away from the kernel proves only
\[
\operatorname{supp}(D)\subset
 \{(x,\eta):h(x)=0\}.
\tag{LFT11}
\]
If \(h(x)\ne0\), use \(\langle h(x),\eta\rangle\) as one local \(\eta\)-coordinate. The coefficient \(L\) is pulled back from the other variables, and the interval local-support calculation makes \((R\Gamma_C L)_N\) vanish there. If \(h(x)=0\), this coordinate argument is unavailable. A nonzero kernel can extend to infinity, and rank jumps can change it with the base. We retain \(\nu_q\) instead of declaring it invertible. This proves the lemma. \(\square\)

## SH02-LFT-DIRECT. Its first description is support forgetting through \(h\)

On \(X_i=E_i\times_BE_i^*\), use the projections \(p_i,q_i\), the pairing cuts \(N_i,C_i\), and the two Fourier presentations
\[
T_iA=Rq_{i!}(p_i^{-1}A)_{N_i},\qquad
U_iA=Rq_{i*}R\Gamma_{C_i}(p_i^{-1}A).
\tag{LFT12}
\]
Let \(c_i:T_i\to U_i\) be the actual first halfspace comparison FS6.

Define
\[
u(x,\eta)=(x,r\eta)\in X_1,
\qquad v(x,\eta)=(h(x),\eta)\in X_2.
\tag{LFT13}
\]
The two pairing pullbacks are literally \(N=u^{-1}N_1=v^{-1}N_2\) and similarly for \(C\).

The proper-support kernel map FF6 identifies
\[
r^{-1}T_1A\simeq Rq_!L_N\simeq T_2Rh_!A.
\tag{LFT14}
\]
There is an ordinary direct-image identification
\[
U_2Rh_*A\simeq Rq_*R\Gamma_C L.
\tag{LFT15}
\]
To justify its coefficient step, the square with \(p_2,s,h,v\) is a pullback by a vector-bundle projection. The product-interval ordinary base-change identity gives
\(p_2^{-1}Rh_*A\simeq Rv_*s^{-1}A\), including the canonical ordinary counit map. One can obtain this identity from the conic product-interval contract by successive finite-dimensional product factors, then glue bundle trivializations. This is the same restricted product base change used in conic preservation; it is not arbitrary nonproper ordinary base change. Local cohomology commutes with this ordinary image by tensor–Hom adjunction:
\(R\Gamma_{C_2}Rv_*L\simeq Rv_*R\Gamma_C L\). Ordinary composition now gives LFT15.

**Proposition.** Under LFT14 and LFT15,
\[
c_2(Rh_*A)\circ T_2(\nu_h(A))
 =\Psi_h(A).
\tag{LFT16}
\]

**Proof.** Apply the halfspace construction first to
\(p_2^{-1}Rh_*A\), retaining the map from
\(p_2^{-1}Rh_!A\). Expand the proper coefficient by proper-support
base change in the \(p_2\)-square and the ordinary coefficient by
LFT15. Naturality of local cohomology and the proper cut comparison
gives the first endpoint of LFT10. The ordinary closed-cut step merits
an explicit check.

Put \(H_2=Rv_*H\), \(D_2=(H_2)_{N_2}\), and retain
\(D=H_N\). Ordinary base change for the closed inclusion of
\(N_2\), followed by closed extension, gives a morphism
\[
\gamma:(Rv_*H)_{N_2}\longrightarrow Rv_*(H_N).
\tag{LFT16a}
\]
This morphism is not assumed invertible. If
\(b:H_2\to D_2\) and \(d:H\to D\) are restriction, its
ordinary-counit definition gives \(\gamma b=Rv_*d\).
After \(Rq_{2*}\), both \(b\) and \(Rv_*d\) become
isomorphisms: the first by conic contraction in \(E_2\), the second
by composition and conic contraction in \(E_1\). Hence
\(Rq_{2*}\gamma\) is invertible, with its inverse fixed by that
same equation.

Under proper closed-cut transport, LFT8 for the square formed by
\(v\) and the closed inclusion of \(N_2\) gives
\[
\gamma\circ(\nu_v(H))_{N_2}=\nu_v(H_N).
\tag{LFT16b}
\]
The source of this equation is identified with \(Rv_!H_N\) by
the proper cut comparison. Apply the outer proper-support image and
then the outer support-forgetting map. Naturality of \(\nu_{q_2}\)
and its composition law FTC8 identify the result, after
\(Rq_{2*}\gamma\), with precisely
\(\nu_q(D):Rq_!D\to Rq_*D\), since \(q=q_2v\).

At the final endpoint the equation \(\gamma b=Rv_*d\) identifies
the inverse restriction with the last inverse of LFT10. At the
initial endpoint proper cut transport and naturality of local-support
forgetting identify the first inverse with that of LFT10. The local
cut interchange is induced by the same functorial localization
triangles. Thus the expanded chain has exactly the first and last
arrows of LFT10 and exactly its middle support arrow. Inverting only
the already proved invertible endpoint maps proves LFT16. In
particular this proof never commutes a closed tensor restriction
freely through an ordinary direct image. \(\square\)

## SH02-LFT-MATE. The direct ordinary-image kernel comparison

Define the following direct kernel comparison, denoted \(G_h(A)\):
\[
\begin{aligned}
r^!T_1A
&\xrightarrow{r^!c_1}r^!U_1A\\
&\xrightarrow{\sim}Rq_*R\Gamma_C L\otimes\omega_r\\
&\xrightarrow{\sim}U_2Rh_*A\otimes\omega_r
 \xrightarrow{c_2^{-1}}T_2Rh_*A\otimes\omega_r.
\end{aligned}
\tag{LFT17}
\]

**Lemma.** The displayed chain defines a natural isomorphism \(G_h(A)\) in the full domain of this lesson. Its identification with the original FF L3 map is a separate equality of maps and is false in the rank-one test below.

**Proof.** The square \((u,q,q_1,r)\) is cartesian. LFT5 gives
\(r^!Rq_{1*}\simeq Rq_*u^!\). The local tensor–Hom projection formula gives
\[
u^!R\Gamma_{C_1}(p_1^{-1}A)
 \simeq R\Gamma_C(u^!p_1^{-1}A).
\tag{LFT18}
\]
This is obtained by taking the exceptional mate of projection formula with the pulled-back flat cut. The coefficient identification, including its map, is
\[
u^!p_1^{-1}A\simeq s^{-1}A\otimes\omega_r.
\tag{LFT19}
\]
To check it on arbitrary coefficients, regard \(u\) as the map of bundles over \(E_1\) induced by \(r\). Exceptional transitivity gives \(u^!p_1^!A\simeq s^!A\). The two projections contribute \(W_{1^*}\) and \(W_{2^*}\); cancel \(W_{1^*}\) on the right. This is FF3a over the base \(E_1\). In particular the map \(\theta_u(p_1^{-1}A)\) is this isomorphism: its adjunct is the same coefficient tensored with the relative orientation trace, as is checked in bundle coordinates and then by trace compatibility under changes of coordinates. The argument works through rank jumps because it uses the two bundle projections, not a bundle structure on \(\ker r\).

For reference, the raw right adjoint of the negative-cut transform on \(E_i^*\) has the presentation
\[
Rq_{i*}R\Gamma_{N_i}p_i^!
 \simeq a_{E_i^*}^{-1}U_i\otimes W_{i^*}.
\tag{LFT20}
\]
This follows by the ordinary change of pairing cut and the bundle orientation formula. The specified identification with
\(V_i=a_{E_i^*}^{-1}T_i\otimes W_i\)
uses the first halfspace comparison and positive dual orientation. The presentation alone does not identify the mate of a mixed kernel map after the exceptional antipode has been canceled. Such a cancellation uses its exceptional exchange on the coefficient, including its action on the relative orientation line.

The maps LFT18 and LFT19, exceptional/ordinary base change LFT5, the ordinary-image identification LFT15, and the endpoint comparisons \(c_i\) construct every arrow of LFT17. Each is an isomorphism under the stated hypotheses. This proves the lemma for the explicitly defined direct comparison \(G_h\), without replacing that chain by a different adjoint mate. \(\square\)

### SH02-LFT-MATE-COUNTERTEST. Two maps of the same orientation complex

Take \(k=\mathbb Z\), base a point, \(h:\mathbb R\to0\), and its transpose \(r:0\to\mathbb R^*\). Put \(W=\operatorname{or}(\mathbb R)[1]\), write \(\delta=k_{\{0\}\subset\mathbb R^*}\), and let \(P=T_{\mathbb R^*}\). Use the compact-support orientation trace to identify
\(T_{\mathbb R}h^!k=\delta\).
We compare LFT17 for the map \(r\) with the original L3 for \(r\), both on the coefficient \(k\) of its rank-zero source.

The right adjoint \(Q=V_{\mathbb R^*}\) sends \(\delta\) to \(k_{\mathbb R}\otimes W\). Its specified map to the raw right adjoint
\(S\delta=Rp_*R\Gamma_Nq^!\delta\)
is the identity on this object. Indeed \(q^!\delta\) is supported on the axis where the integration covector is zero. That support lies in both pairing cuts and projects isomorphically under \(p\). Thus local support, cut restriction, and proper-to-ordinary comparison in the reverse halfspace chain are all identities on this coefficient.

Consequently the actual Fourier counit
\(TQ\delta\to\delta\)
is the positive compact-support trace. To see its map, expand the raw tensor--Hom adjunction: the ordinary \(p\)-counit and cut evaluation are identities on the supported coefficient, and the remaining \(q\)-counit is precisely
\(R\Gamma_c(\mathbb R;k\otimes W)\to k\).
The original R2 map \(E_h:T h^!k\to Rr_*k\) is positive as well. Its ordinary adjunct is the primitive exchange at the zero covector followed by \(\operatorname{tr}_h\), which is that same trace. By LFT36 and faithfulness of \(T\), the actual mate
\[
b_h(k):h^!Q_0k\longrightarrow Q Rr_*k
\tag{LFT20a}
\]
is therefore \(+1_W\).

Now form the original L3 for \(r\) from this L2 mate. The exceptional exchange for the square \(ha=h\) has value \(-1\) on \(h^!k=W\): its proper-support mate integrates the orientation-reversing map \(x\mapsto-x\). Canceling the output antipode of L2 inserts this exceptional exchange at the source. Thus
\[
\operatorname{L3}_r(k)=-1_W:
h^!P_0k\longrightarrow P\delta\otimes W.
\tag{LFT20b}
\]
There is no nontrivial inverse-line cancellation in this instance of L3: the source bundle of \(r\) has rank zero.

In contrast, LFT17 for \(r\) has mixed space \(0\times\mathbb R=\mathbb R\), identically zero pairing, both cuts equal to that whole space, and identity projection to its output. Its first endpoint is the rank-zero identity comparison. Its coefficient identification LFT19 is the positive trace identification \(h^!k=k\otimes W\). Its last endpoint is the identity first halfspace comparison on a zero-supported coefficient. Therefore
\[
G_r(k)=+1_W.
\tag{LFT20c}
\]
The maps LFT20b and LFT20c differ over \(\mathbb Z\). This separates the two normalization choices before any further relative inverse factor is canceled. It refutes the previous universal identification of LFT17 with original L3; it is not a counterexample to original FTC14 or an erratum attributed to the source book. SH02-FGC-SUPPORT and SH02-FTE-TRACE compare the complete larger squares with their later line contractions retained.

## SH02-LFT-SUPPORT. The linear support equation

We specify the cancellation for the direct comparison. For an invertible line \(K\), let \(\operatorname{coev}_K:k\to K\otimes K^{-1}\) be its tensor--Hom unit. Define
\[
\overline G_h(A)=
\bigl(1_{T_2Rh_*A}\otimes\operatorname{coev}_{\omega_r}^{-1}\bigr)
\bigl(G_h(A)\otimes1_{\omega_r^{-1}}\bigr).
\tag{LFT20d}
\]
The forward-ordered pair is canceled by the inverse coevaluation. This is the cancellation paired with the right-ordered \(\bar\theta_r\) of LFT2 and LFT-L2. It specifies the direct endpoint; it does not replace the separately specified original FF endpoint by a new convention.

**Theorem.** For every \(h\) and \(A\) in SH02-LFT-DOMAINS, the following square commutes. Its left vertical map is the primitive proper-support comparison. Its right vertical map is the explicitly defined \(\overline G_h(A)\):
\[
\begin{array}{ccc}
r^{-1}T_1A&\xrightarrow{\bar\theta_r(T_1A)}&
r^!T_1A\otimes\omega_r^{-1}\\
\downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim\\
T_2Rh_!A&\xrightarrow{T_2\nu_h(A)}&T_2Rh_*A.
\end{array}
\tag{LFT21}
\]
This proves the direct kernel support square relative to the declared operation imports. SH02-FGC-EXTRACTION subsequently computes the full original L3 as \((-1)^{n_2-n_1}G_h\), using the coherent initial FF11 extraction. The final braided contraction in FGC3 contributes the same sign, so SH02-FGC-SUPPORT obtains FTC13b with that explicitly completed endpoint. The uncontracted maps remain distinct in odd relative rank, as the rank-one test requires.

**Proof.** Put \(H_1=R\Gamma_{C_1}p_1^{-1}A\). Apply the trace square LFT6 to the cartesian square \((u,q,q_1,r)\). Naturality of \(\theta_r\) for \(c_1\) shows that, after LFT17 and before the last \(c_2^{-1}\), the upper map of LFT21 becomes
\[
r^{-1}T_1A\xrightarrow{r^{-1}c_1}
r^{-1}Rq_{1*}H_1\xrightarrow{\beta}
Rq_*u^{-1}H_1\longrightarrow Rq_*R\Gamma_C L.
\tag{LFT22}
\]
The last arrow is the local-cohomology inverse-image comparison. To see that it is the arrow supplied by LFT6, combine LFT18 and LFT19. Naturality of \(\theta_u\) with respect to the local tensor–Hom construction identifies its value on \(H_1\), after canceling \(\omega_r\), with
\(u^{-1}R\Gamma_{C_1}p_1^{-1}A\to R\Gamma_C L\). This follows as well by taking the exceptional adjunct: both maps become restriction of the same coefficient trace to the pulled-back support. The invertibility of \(\theta_u\) on the coefficient \(p_1^{-1}A\) is used here; invertibility on \(H_1\) is neither needed nor asserted.

It remains to expand \(r^{-1}c_1\). Let
\(D_1=(H_1)_{N_1}\), and put \(\widetilde D=u^{-1}D_1=(u^{-1}H_1)_N\).
Pull back the FS6 chain for \(c_1\). Proper-support base change identifies its proper-image terms with the corresponding \(Rq_!\) terms. There is a natural map
\[
\widetilde D\longrightarrow D=(R\Gamma_C L)_N.
\tag{LFT23}
\]
Its composite to \(L_N\) agrees with pullback of the local-support-forgetting map. Consequently the square
\[
\begin{array}{ccc}
Rq_!\widetilde D&\longrightarrow&Rq_!D\\
\downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim\\
Rq_!L_N&=&Rq_!L_N
\end{array}
\tag{LFT24}
\]
commutes. The left vertical arrow is invertible because it is proper base change of the first inverse in the original FS6 chain. The right vertical arrow is invertible by SH02-LFT-DEGENERATE. Thus the top arrow is invertible too, although LFT23 itself need not be.

For the middle arrow, LFT8 identifies pullback of \(\nu_{q_1}(D_1)\), followed by ordinary base change, with \(\nu_q(\widetilde D)\). Naturality of \(\nu_q\) for LFT23 then identifies it with the middle arrow of LFT10, after LFT24. The last arrow is compatible with tensor restriction to \(N\) by naturality of the local-cohomology inverse-image comparison. Conic contraction makes the two last restriction arrows invertible. Therefore LFT22 is exactly \(\Psi_h(A)\).

By LFT16, that is \(c_2\circ T_2\nu_h(A)\). Cancel the invertible \(c_2\). The right vertical arrow is the direct chain defining \(G_h\), with its declared right-line cancellation. This proves LFT21 for that explicit comparison as an equality of natural transformations. In particular no assertion that maps are determined by cohomology dimensions, no improper ordinary base-change isomorphism, and no kernel-rank decomposition occurs in the proof. \(\square\)

## SH02-LFT-TESTS. Degenerate examples and solved problems

**Problem 1.** Suppose \(h\) is the zero map \(E_1\to E_2\). Identify the intermediate arrow in LFT10.

**Solution.** Both cuts are all of \(Y\), so \(H=D=L\). Every endpoint comparison in LFT10 is an identity, and \(\Psi_h\) is exactly
\(Rq_!s^{-1}A\to Rq_*s^{-1}A\). This can fail to be invertible. For \(B\) a point, \(E_1=\mathbb R\), and \(A=k_{\mathbb R}\) with nonzero \(k\), the two objects are \(k_{E_2^*}[-1]\) and \(k_{E_2^*}\). The orientation twist on the other side of LFT21 is therefore essential even though the pairing itself is identically zero.

**Problem 2.** Give a family to which LFT21 applies but a proof using a kernel bundle does not apply.

**Solution.** Take \(B=\mathbb R\), both bundles trivial of rank one, and \(h_b(x)=bx\). Its kernel is zero for \(b\ne0\) and the whole line for \(b=0\), so these kernels are not a vector bundle of constant rank. On the correspondence, the cuts are \(bx\eta\leq0\) and \(bx\eta\geq0\). They are closed conic sets, and the zero section in \(x\) lies in both. Every contraction and pullback square in the proof remains defined. The set in LFT11 can acquire a noncompact line at \(b=0\); this is exactly why its support arrow was retained.

**Problem 3.** Why is it permissible to invert the top arrow in LFT24 but not the ordinary base-change arrow LFT4?

**Solution.** The top arrow in LFT24 sits in a commutative square whose two vertical arrows have already been proved invertible: one by proper-support base change of the original Fourier comparison, the other by conic contraction. The two-out-of-three property therefore proves its invertibility. No such argument was given for LFT4. That arrow is used only in the direction provided by the ordinary adjunction, and its mate compatibility suffices.

**Problem 4.** Factor a rank-jumping bundle map into maps with fixed geometric types.

**Solution.** In \(E_1\oplus_BE_2\), let \(j(x)=(x,0)\), let \(p_2\) be the second projection, and set
\[
\sigma_h(x,y)=(x,y+h(x)).
\tag{LFT25}
\]
Its inverse is \((x,y)\mapsto(x,y-h(x))\), so it is a bundle automorphism regardless of the rank of \(h\). Then \(h=p_2\sigma_hj\). Equivalently its graph is a closed subbundle isomorphic to \(E_1\), followed by projection to \(E_2\). This is a useful geometric reduction, but each comparison map must still be checked with its orientation and composition maps. The direct proof above avoids introducing those extra checks.

## SH02-LFT-PAIRED. The two positive adjunctions and their defect

The second linear equation requires comparing specified morphisms, even after
the first has been proved. We give the precise reduction. Put
\(\mathcal C_i=\mathcal D_{E_i}\), \(\mathcal D_i=\mathcal D_{E_i^*}\), and write
\[
\begin{array}{lll}
T_i:\mathcal C_i\to\mathcal D_i,&
P_i=T_{E_i^*}:\mathcal D_i\to\mathcal C_i,\\
V_i=a^{-1}T_i(-)\otimes W_i:\mathcal C_i\to\mathcal D_i,&
Q_i=V_{E_i^*}:\mathcal D_i\to\mathcal C_i.
\end{array}
\tag{LFT26}
\]
The adjunctions fixed in FF are \(T_i\dashv Q_i\) and
\(P_i\dashv V_i\). Let \(u_i:1\to V_iP_i\) and
\(v_i:P_iV_i\to1\) be the unit and counit of the latter.

There is also an adjunction \(V_i\dashv P_i\) obtained from
\(T_i\dashv Q_i\). More explicitly, set
\(M_i=a^{-1}(-)\otimes W_i\), so \(V_i=M_iT_i\).
Its right adjoint is \(Q_iM_i^{-1}\). The antipode identifications,
positive dual orientation, and adjacent evaluation in FF identify this
right adjoint with \(P_i\). Transport the adjunction along that
identification, and call its unit and counit
\[
\alpha_i:1\longrightarrow P_iV_i,
\qquad \beta_i:V_iP_i\longrightarrow1.
\tag{LFT27}
\]
These are definitions using the existing maps, not new normalizations of
the halfspace comparison.

Define the natural automorphism
\[
\delta_i=v_i\alpha_i:1_{\mathcal C_i}\longrightarrow1_{\mathcal C_i}.
\tag{LFT28}
\]
All these maps are invertible because the functors are equivalences.
This does not imply \(\delta_i=1\). In fact the triangle identities give
\[
v_i^{-1}=\alpha_i\delta_i^{-1},
\qquad
u_i^{-1}=\beta_i\circ V_i\delta_iP_i.
\tag{LFT29}
\]
For the second formula, the counit \(v_i=\delta_i\alpha_i^{-1}\)
and its unit \(u_i\) describe the adjunction inverse to
\(V_i\dashv P_i\), with its counit changed by \(\delta_i\).
Substitution in either triangle identity gives
\(u_i=V_i\delta_i^{-1}P_i\circ\beta_i^{-1}\), which is the displayed
formula. In particular \(v_i=\alpha_i^{-1}\) is equivalent to
\(u_i=\beta_i^{-1}\). Either is a normalization statement requiring
proof.

Let \(A_r:h^{-1}P_2\xrightarrow{\sim}P_1Rr_!\) be the primitive
kernel map FF6 for the transposed bundle map. Write the R1 comparison
with every Fourier unit and counit shown:
\[
\begin{aligned}
C_h:V_1h^{-1}
&\xrightarrow{V_1h^{-1}v_2^{-1}}V_1h^{-1}P_2V_2\\
&\xrightarrow{V_1A_rV_2}V_1P_1Rr_!V_2
 \xrightarrow{u_1^{-1}}Rr_!V_2.
\end{aligned}
\tag{LFT30}
\]
For comparison, define
\[
\begin{aligned}
C_h^0:V_1h^{-1}
&\xrightarrow{V_1h^{-1}\alpha_2}V_1h^{-1}P_2V_2\\
&\xrightarrow{V_1A_rV_2}V_1P_1Rr_!V_2
 \xrightarrow{\beta_1}Rr_!V_2.
\end{aligned}
\tag{LFT31}
\]
The difference between these two constructions is exactly
\[
C_h=C_h^0\circ V_1\kappa_h,
\qquad
\kappa_h=\delta_1h^{-1}\circ h^{-1}\delta_2^{-1}.
\tag{LFT32}
\]
Here, for example, \((\delta_1h^{-1})_H=\delta_{1,h^{-1}H}\).

**Proof of LFT32.** Substitute LFT29 in LFT30. Naturality of
\(\delta_1\) for \(A_r\) moves its occurrence at \(P_1Rr_!V_2\)
to the occurrence at \(h^{-1}P_2V_2\). Naturality for
\(h^{-1}\alpha_2\) then moves it to \(h^{-1}\). The remaining
\(\delta_2^{-1}\) was inserted at that same input by the first
formula of LFT29. What remains between these input automorphisms and
the output is exactly LFT31. This proves the formula in its original
ordered tensor convention, before any orientation factor has moved.
\(\square\)

## SH02-LFT-CONIC-TOPOLOGY. An abelian category for the conic objects

Let \(E_{\mathrm{con}}\) have the same underlying set as \(E\), with
the topology consisting of the open sets invariant under positive
fiber dilations. This space need not be Hausdorff. Sheaves and their
bounded-below derived category make sense on this topology; no
proper-support operation on this new space will be used. The identity
map of underlying sets is continuous as a map
\(\gamma:E\to E_{\mathrm{con}}\).

**Lemma.** The ordinary derived adjunction restricts to inverse
equivalences
\[
\gamma^{-1}:D^+(E_{\mathrm{con}};k)
 \ \rightleftarrows\
\mathcal D_E:R\gamma_*.
\tag{LFT-C1}
\]
These are also equivalences of the usual derived enhancements.

**Proof.** Inverse image is exact and preserves stalks, because
\(\gamma\) has the same point set. It is therefore conservative.
A sheaf pulled back from \(E_{\mathrm{con}}\) is conic: the two
maps from \(E\times\mathbb R_{>0}\) given by the action and by
projection have the same inverse images of conic open sets. Their
pullback functors on sheaves are canonically identified. This gives
the parameter transport, including its identity along scalar one.
The same assertion for a derived object follows by exactness.

We check the counit on a conic \(F\). In a local bundle
trivialization choose an open product \(U=W\times D\), where
\(D\) is a Euclidean open ball around the chosen fiber point.
Such products form an ordinary neighborhood basis. Write
\(U^+=\mathbb R_{>0}U\). This is open and conic, and the sets
\(U^+\) form a cofinal family among the conic neighborhoods of
that point. For every point of \(U^+\), the set of positive
parameters taking it into \(U\) is a nonempty interval. Indeed a
ray meets a convex ball in an interval; at a zero vector the
parameter set is either empty or the whole group, and it is the
whole group when that vector belongs to \(U^+\). Inverting the
parameter preserves the interval property. Applying
SH02-CON-RESTRICTION on \(U^+\) gives
\[
R\Gamma(U^+;F)\xrightarrow{\sim}R\Gamma(U;F).
\tag{LFT-C2}
\]
All these arrows are restrictions. Taking the exact filtered colimit
over the indicated neighborhood basis therefore identifies every
cohomology stalk of the counit
\(\gamma^{-1}R\gamma_*F\to F\) with the identity on the
corresponding stalk of \(F\). The counit is an isomorphism.

For any \(A\in D^+(E_{\mathrm{con}};k)\), apply the triangle
identity to \(\gamma^{-1}A\). The counit just proved invertible
makes \(\gamma^{-1}\) of the unit invertible. Conservativity
then makes the unit invertible. The inverse-image and derived-image
adjunction is available in the derived enhancement itself; the same
unit and counit become equivalences there when their cohomology
cones vanish. This proves the enhanced statement as well. It does
not rely on a chosen enhancement of orbitwise equivariant data.
\(\square\)

## SH02-LFT-CENTER. Why an enhanced identity endomorphism is a base scalar

The adjective “enhanced” matters in the following argument. We use
natural transformations of the exact functors in the derived
enhancement, with their coherent naturality, rather than a collection
of maps commuting only in its homotopy category. The transformations
made from the sheaf-operation units, counits, and functorial
localization maps in this supplement have this enhancement.

**Lemma.** If \(\mathcal A\) is a Grothendieck abelian category,
restriction to the heart identifies the degree-zero enhanced center
of \(D^+(\mathcal A)\) with the center of \(\mathcal A\).
Here a center is the ring of natural endomorphisms of the identity;
in the enhanced case we take morphisms up to coherent homotopy.

**Proof.** Use the enhancement by bounded-below complexes of
injectives. First restrict to injective objects placed in degree
zero. Their mapping complexes have cohomology only in degree zero:
positive Ext groups vanish by injectivity of the target, and
negative Ext groups vanish for heart objects. They are therefore
the ordinary category of injectives, regarded as a differential
graded category in degree zero. A degree-zero enhanced natural
endomorphism on this category is exactly an ordinary natural
endomorphism on the injectives.

This ordinary endomorphism extends uniquely to \(\mathcal A\).
To see this explicitly, represent \(A\) as the kernel of a map
\(I\to J\) between injectives, by embedding \(A\) in \(I\)
and embedding its quotient in \(J\). Naturality on the map
\(I\to J\) makes the endomorphism of \(I\) preserve that
kernel. The induced map on \(A\) is independent of the chosen
embeddings: a map between the two embeddings of \(A\) extends to
their injective ambient objects, and naturality on that extension
identifies the two induced kernel maps. For a map \(A\to A'\),
extend its composite with the embedding of \(A'\) to the
injective ambient object of \(A\). The same argument proves
naturality. Conversely restriction of a center element of
\(\mathcal A\) clearly recovers its action on injectives.

We must also show that the enhanced transformation is determined
away from the heart. Bounded complexes of injectives are the finite
stable envelope of the category of injectives: concretely they are
finite twisted complexes, with the usual differential matrices, and
their morphism complexes are the corresponding total Hom complexes.
The universal property of this construction says that restriction
of exact enhanced functors, including their natural transformations,
to the injectives is fully faithful. One can verify it from the
construction: the extension takes the finite differential matrix to
its iterated cofiber, and a coherent natural transformation extends
to that cofiber diagram uniquely. The finite-cofiber universal
properties also identify all higher compatibilities. Thus the
endomorphism is determined, as an enhanced transformation, on every
bounded complex of injectives. This uses the finite stable envelope,
not just objectwise vanishing of cohomology maps.

Finally let \(I^\bullet\) be a bounded-below injective complex.
Let \(I^{\leq n}\) be its brutal upper truncation: it agrees with
\(I^\bullet\) in degrees at most \(n\) and is zero above
\(n\). The projection maps are chain maps and give a tower of
bounded complexes with a common lower bound. In the enhanced
derived category,
\[
I^\bullet\xrightarrow{\sim}
\mathop{\mathrm{holim}}_n I^{\leq n}.
\tag{LFT-C3}
\]
For completeness, products of injectives are injective, since Hom
into a product is the product of the exact Hom functors. Hence the
product of this uniformly bounded-below family of injective
complexes computes its derived product term by term. In each degree
the tower is eventually constant, and the difference map on the
product is surjective with kernel that constant term. The usual
fiber of the difference map therefore computes the displayed
homotopy limit and is quasi-isomorphic to \(I^\bullet\).

Coherent naturality identifies the endomorphism on this limit with
the limit of its endomorphisms on the truncation tower. The equality
already obtained on the finite stable envelope is coherent on that
whole tower, so it gives the equality on \(I^\bullet\).
Conversely a natural endomorphism of the abelian identity acts
termwise on complexes, yielding an exact enhanced natural
endomorphism and the stated restriction. These constructions are
inverse. \(\square\)

**Corollary.** Every degree-zero enhanced natural endomorphism of
\(1_{\mathcal D_E}\) is multiplication by a unique section of the
constant sheaf \(k_B\) on \(B\).

**Proof.** Apply LFT-C1 and the lemma to sheaves of \(k\)-modules
on \(E_{\mathrm{con}}\). For any topological space \(X\), the
center of its sheaf category is \(\Gamma(X;k_X)\). Indeed its
value on \(k_X\) is multiplication by such a section. For every
open \(U\), the natural monomorphism \(k_U\to k_X\), with
extension by zero, forces that same value on \(k_U\). Every
sheaf is a quotient of a sum of these sheaves: its local sections
give the maps \(k_U\to F\), and they generate every stalk.
Naturality for the sum inclusions and for this epimorphism forces
the same multiplication on \(F\). This argument also proves
uniqueness; commutativity of \(k\) ensures that every such scalar
is central.

A locally constant function on \(E_{\mathrm{con}}\) is constant
on each entire vector fiber. A conic neighborhood of a zero vector
contains the whole fiber over that base point, since it contains a
small ball around zero and is dilation invariant. A neighborhood
on which the function is constant therefore forces the same value
on the entire fiber. The zero section and the bundle projection are
continuous for the conic topology, so these fiber-constant locally
constant functions are exactly the locally constant functions on
\(B\). This proves the corollary, with no manifold, compactness,
or countability condition on \(B\). \(\square\)

## SH02-LFT-ANTIPODE-CHECK. The scalar supplied by the actual antipode

The center theorem proves that the paired defect is a base scalar. The
following calculation determines it, retaining the antipode exchange
used in identifying the two adjunctions.

**Theorem.** For the adjunctions specified in LFT26–LFT28,
\[
\delta_E=(-1)^{n_E}\,1_{1_{\mathcal D_E}}.
\tag{LFT-P0}
\]
This assertion covers every conic bounded-below object under the
standing hypotheses.

Write \(P=T_{E^*}\), \(M=a_{E^*}^{-1}(-)\otimes W_E\), and
\(Q=V_{E^*}\). The kernel exchange gives an isomorphism
\[
b:PM\xrightarrow{\sim}Q.
\tag{LFT-P1}
\]
Its input-antipode part moves a negation across the integration
variable. On the constant sheaf over an \(n\)-space, the induced
endomorphism on compactly supported degree-\(n\) orientation
cohomology is multiplication by \((-1)^n\), the orientation degree
of negation. In contrast, an output antipode acts trivially on a
line explicitly pulled back from the base at the zero section.
These are different actions and cannot be interchanged without
checking the orientation identification.

Let \(e:QU\to1\) be the counit obtained by transporting the raw
adjunction \(P\dashv MU\) through \(M\) and \(b\). Let
\(c:T\to U\) be the first halfspace comparison and
\(\eta:1\to QT\) the specified first unit. Adjunction transport
and its triangle identities give
\[
b_T\alpha=\eta,\qquad
v=e\circ Q(c)\circ b_T,\qquad
\delta=e\circ Q(c)\circ\eta.
\tag{LFT-P2}
\]
**Proof.** We first justify LFT-P2 with its counit. The raw right
adjoint of \(P\) is \(MU\), by the first halfspace comparison for
the dual bundle and positive dual orientation. The fixed
adjunction \(P\dashv V\) is transported along
\(Mc:V=MT\to MU\). Let
\(e_{\mathrm{raw}}:PMU\to1\) be its raw counit.
Transporting the adjunction through \(M\), then through \(b\),
gives
\[
e=e_{\mathrm{raw}}\circ b_U^{-1}.
\tag{LFT-P3}
\]
In this equation the equivalence unit and counit of \(M\) have
canceled by their triangle identity. Transporting \(T\dashv Q\)
through \(M\) similarly gives \(b_T\alpha=\eta\).
Naturality of \(b\) gives
\(v=e_{\mathrm{raw}}P(Mc)=e Q(c)b_T\). These prove LFT-P2.
They do not identify \(e\) with a positive trace after suppressing
\(b_U^{-1}\).

By the center theorem it is enough to calculate the resulting
endomorphism on \(i_*k_B\), where \(i\) is the zero section.
The sheaf-operation constructions in a local bundle
trivialization are their fiber constructions with the base
coefficient pulled back; proper base change, functorial
localization, and the vector-bundle trace give these actual
identifications. The test object is in the heart, so its
endomorphism is detected by its stalk maps. This use of stalks
comes after the enhanced-center argument.

Over a point use positive dual coordinates \(x,y\), and put
\(N=\{x\cdot y\leq0\}\) and \(C=\{x\cdot y\geq0\}\).
For \(F=k_{\{0\}}\) both cuts contain the whole coefficient
support \(x=0\), and projection of this support to the output is
an isomorphism. Hence
\[
TF=UF=k_{E^*},\qquad c_F=1.
\tag{LFT-P4}
\]
The raw counit \(e_{\mathrm{raw}}\) at \(F\) is the positive
\(y\)-integration trace. It comes from the raw negative-kernel
adjunction for \(P\); its coefficient restriction to \(x=0\)
is the identity. In contrast \(b_{UF}\) integrates the change of
variable \(y\mapsto-y\). On
\(R\Gamma_c(E^*;k)\) its orientation degree is \((-1)^n\).
The right-hand line \(W_E\) is pulled back from the base and
has not moved. Thus LFT-P3 contributes exactly this factor to
the counit on the test object.

For precision, the unit \(\eta\) contributes the positive
relative class, with no additional parity factor. This can be
checked through its actual construction. Write \(S\) for the raw
right adjoint of \(T\), with unit
\(\eta_{\mathrm{raw}}:1\to ST\). Its specified identification
\(d:Q\to S\) is the dual first halfspace chain, pulled through
the output antipode and tensored on the right with \(W_E\).
It exchanges the two cuts in that chain. Therefore
\(\eta=d_T^{-1}\eta_{\mathrm{raw}}\), and the local-support
part of the raw unit is the Thom map
\[
R\Gamma_{\{x=0\}}W_x\longrightarrow R\Gamma_NW_x.
\tag{LFT-P5}
\]
Normalize a positive relative \(x\)-generator by its actual trace
coefficient \(t_x\); the unit uses its multiple \(t_x^{-1}\).
Positive dual coordinates give the same coefficient
\(t_y=t_x\) for the \(y\)-trace.

Here is the orientation check through \(d_T^{-1}\). Set
\[
u=(x+y)/2,\qquad v=(x-y)/2,
\qquad x\cdot y=|u|^2-|v|^2.
\tag{LFT-P6}
\]
The strict positive-pairing set and
\(C\setminus\{0\}\) both retract, by shrinking \(v\), onto
the punctured positive graph \(x=y\). Projection of that graph
to either coordinate space is orientation preserving. The
projection of the strict positive-pairing set to \(x\ne0\)
also has contractible open-halfspace fibers, and preserves the
same class. Thus the complementary-pair map defining LFT-P5
carries the positive \(x\)-class to the positive graph class.
Restriction of the ambient pair to \(C\) preserves it as well:
the complement is the same strict positive-pairing set and the
ambient restriction preserves the constant section. The map
\(R\Gamma_{\{0\}}k_C\to R\Gamma_Nk_C\) preserves this class,
because its complementary inclusion is identified by the two
retractions with the identity of the oriented sphere. Finally
inclusion of the vertical axis carries this class to the positive
\(y\)-class; on that axis \(u=y/2\), so it has positive
orientation. The middle support comparison for this coefficient
is supported at the origin. Its final proper integration is the
\(y\)-Thom trace.

These assertions describe the maps of relative-cochain models of
the indicated local-support triangles. In rank one the model is
the two-component relative complex \(k\to k\oplus k\);
in higher positive rank it is the degree-\(n\) relative class
of the punctured graph. All generators and maps are integral
before extending to \(k\). Keep \(W_x\) on the right, so no
shifted line is permuted past this relative class. The composite
with a separately positive \(y\)-trace would have coefficient
\(t_x^{-1}t_y=1\).

The actual counit, however, is LFT-P3 and includes the
input-antipode degree. Its value is consequently
\[
\delta_{k_{\{0\}}}=(-1)^n t_x^{-1}t_y\,1=(-1)^n\,1.
\tag{LFT-P7}
\]
Rank zero consists of identity maps and gives the same formula.
Changes of local orientation generators affect both trace
coefficients together, so this calculation glues on a
nonorientable bundle. The center theorem now gives LFT-P0 on
every conic object. No field, constructibility, finite-stalk, or
constant-rank-map assumption occurs. \(\square\)

The adjunctions and input-antipode exchange in this theorem retain their stated maps. The separately specified literal comparison and negative-definite second adjunction are analyzed in [The geometric normalization of Fourier adjunctions](fourier-literal-normalization.md). NDF4–NDF10 compute that literal defect and construct the unique comparison with paired inverse maps. This is a downstream comparison of conventions; the proof of LFT-P0 above does not use it.

## SH02-LFT-EXCEPTIONAL-ANTIPODE. The relative orientation action

Write \(a_i:E_i\to E_i\) for negation. The square
\(h a_1=a_2h\) is cartesian, since the horizontal maps are
isomorphisms. Its exceptional mate gives
\[
\chi_h:a_1^{-1}h^!\xrightarrow{\sim}h^!a_2^{-1}.
\tag{LFT-A1}
\]
At the tensor unit, identify \(a_2^{-1}k=k\) and put
\(\rho_h=\chi_h(k):a_1^{-1}\omega_h\to\omega_h\).
The underlying line \(\omega_h\) is the explicitly base-pulled
line of FF3a, but this particular automorphism of it is
\[
\rho_h=(-1)^{n_1-n_2}\,1.
\tag{LFT-A2}
\]

**Proof.** For the bundle projection \(\tau_i\), its analogous
exceptional antipode action on
\(\tau_i^!k_B=\tau_i^{-1}W_i\) is
\((-1)^{n_i}\). This is the actual trace action of negation
on the oriented integration fiber, whose determinant has
that sign. Equivariance of exceptional transitivity gives a
commuting square for
\(\omega_h\otimes h^{-1}\omega_{\tau_2}\to
\omega_{\tau_1}\). Its three exceptional antipode actions
therefore satisfy
\[
\rho_h\otimes h^{-1}\rho_{\tau_2}=\rho_{\tau_1}
\tag{LFT-A3}
\]
under FF3a. Cancel the second factor on the right in that
same order. The result is the ratio of the two fiber
orientation degrees, namely LFT-A2. This uses the two actual
bundle projections and works even when the rank of \(h\)
changes with the base. \(\square\)

This action fixes the precise naturality square for the trace
comparison. If \(\zeta_h\) is the ordinary inverse-image
exchange \(a_1^{-1}h^{-1}\simeq h^{-1}a_2^{-1}\), then
\[
\begin{aligned}
\chi_h(K)\circ a_1^{-1}\theta_h(K)
={}&\theta_h(a_2^{-1}K)\circ
  \bigl(\rho_h\otimes\zeta_h(K)\bigr).
\end{aligned}
\tag{LFT-A4}
\]
To verify this equation before suppressing its orientation
factor, take its exceptional adjunct. On both sides it is
proper-support projection formula followed by the pulled-back
trace of \(h\). The counit identity for the mate LFT-A1
identifies these trace maps. Adjunction proves LFT-A4.
Thus the identity action on the underlying base-pulled line
cannot replace \(\rho_h\) in this comparison.

## SH02-LFT-LINE-ORDER. A coefficient calculation that retains both orders

Let \(L\) be an invertible shifted line of parity \(d\), let
\(L^\vee=L^{-1}\), and fix
\[
\operatorname{ev}:L^\vee\otimes L\longrightarrow k,\qquad
\operatorname{coev}:k\longrightarrow L\otimes L^\vee.
\tag{LFT-L1}
\]
For a map \(\theta:L\otimes K\to J\), its right-ordered
version is
\[
\bar\theta=
(\theta\otimes1)(\sigma_{K,L}\otimes1)
(1_K\otimes\operatorname{coev}):
K\longrightarrow J\otimes L^\vee.
\tag{LFT-L2}
\]
Then
\[
\sigma_{J,L^\vee}\bar\theta
 =(-1)^d(1_{L^\vee}\otimes\theta)
   (\operatorname{ev}^{-1}\otimes1_K).
\tag{LFT-L3}
\]

**Proof.** Naturality of the symmetry and its hexagon identity
move \(\theta\) past the last symmetry in LFT-L2. The
remaining unit is
\(\sigma_{L,L^\vee}\operatorname{coev}\).
For a pure line of parity \(d\) this equals
\((-1)^d\operatorname{ev}^{-1}\): in a local generator the
two inverse-degree factors cross once. This proves LFT-L3.
Equivalently, on a homogeneous coefficient of degree \(j\),
the first symmetry contributes \((-1)^{jd}\) and the last
contributes \((-1)^{(d+j)d}\). Their product is
\((-1)^d\), independent of \(j\). This local calculation
glues because it uses the line's evaluation maps. It imposes
no purity or finite-rank condition on \(K,J\). \(\square\)

This identity does not supply a sign for a larger comparison
until the extraction at its other endpoint has been included.
In particular FF's R3 rewrite also reorders the inverse
relative line. Applying LFT-L3 and then forgetting that second
specified braid would count only part of the comparison.

## SH02-LFT-TRACE-BOUNDARY. An exact transpose equation with its endpoint written out

Put \(L=\omega_h\). Apply the R1-to-R4 rewrite of FF8 to
LFT30 and LFT31, using the same antipode cancellation,
projection formula, tensor symmetry, and orientation
evaluations. Write the resulting isomorphisms as
\[
D_h,D_h^0:T_1(L\otimes h^{-1}H)
 \xrightarrow{\sim}Rr_!T_2H.
\tag{LFT33}
\]
Thus \(D_h\) is the original R4 map. The already proved
scalar theorem and LFT32 give
\[
C_h=(-1)^{n_1-n_2}C_h^0,\qquad
D_h=(-1)^{n_1-n_2}D_h^0.
\tag{LFT38}
\]
This compares two endpoint constructions; it does not assert
that either one represents the transformed trace.

Let \(\ell_r:h^!P_2\to P_1Rr_*\otimes L\) be the
specified original L3 map for \(r\), and let
\[
\bar\ell_r^{\,c}
=(1\otimes\operatorname{coev}_L^{-1})(\ell_r\otimes1_{L^{-1}}):
h^!P_2(-)\otimes L^{-1}\xrightarrow{\sim}P_1Rr_*(-)
\]
be its coherent final right-line cancellation. The initial extraction defining \(\ell_r\) is FF11b/FGC22; it is a separate operation. Define the coherent transposed endpoint, retaining \(J_h^t=J_h^{t,c}\) for this explicit completion of the earlier notation,
\[
\begin{aligned}
J_h^{\,t,c}=J_h^t:V_1(h^!H\otimes L^{-1})
&\xrightarrow{V_1(h^!v_2^{-1}\otimes1)}
 V_1(h^!P_2V_2H\otimes L^{-1})\\
&\xrightarrow{V_1\bar\ell_r^{\,c}}
 V_1P_1Rr_*V_2H
 \xrightarrow{u_1^{-1}}Rr_*V_2H.
\end{aligned}
\tag{LFT34}
\]
The unit and counit in this formula are the original
\(u_i,v_i\) of \(P_i\dashv V_i\). The separately braided final contraction is
\[
\bar\ell_r^{\,b}
=(1\otimes\operatorname{ev}_L\sigma_{L,L^{-1}})
(\ell_r\otimes1_{L^{-1}})
=(-1)^{n_1-n_2}\bar\ell_r^{\,c}.
\tag{LFT34b}
\]
Define \(J_h^{t,b}\) by the same three arrows in LFT34 with \(\bar\ell_r^{\,b}\) in the middle. Thus \(J_h^{t,b}=(-1)^{n_1-n_2}J_h^{t,c}\). These two names keep the previously compressed final contraction explicit.

The direct proof supplies the following endpoint. Let
\(\overline G_r:h^!P_2(-)\otimes L^{-1}\to P_1Rr_*(-)\)
be the direct comparison LFT17 for \(r\), with exactly the right-line cancellation in LFT21. Define
\[
\begin{aligned}
J_h^{\,\mathrm{dir}}:V_1(h^!H\otimes L^{-1})
&\xrightarrow{V_1(h^!v_2^{-1}\otimes1)}
V_1(h^!P_2V_2H\otimes L^{-1})\\
&\xrightarrow{V_1\overline G_r}V_1P_1Rr_*V_2H
\xrightarrow{u_1^{-1}}Rr_*V_2H.
\end{aligned}
\tag{LFT34a}
\]
All three endpoints use the same Fourier units and counits. FGC24 gives \(J_h^{t,b}=J_h^{\mathrm{dir}}\). The full endpoint theorem FTE6 further proves
\[
J_h^{t,c}=(-1)^{n_1-n_2}F_h,\qquad
J_h^{t,b}=J_h^{\mathrm{dir}}=F_h,
\tag{LFT34c}
\]
where \(F_h\) is the original R3 map precomposed with the specified symmetry \(V_1\sigma_{h^!H,L^{-1}}\). The proof in [The complete transpose endpoint](fourier-transpose-endpoint.md) retains the actual right-line module maps, exceptional antipode exchange and both paired adjunctions.

**Proposition.** The direct support equation for \(r\) gives
the exact equality
\[
\nu_rV_2\circ C_h
 =J_h^{\,\mathrm{dir}}\circ V_1\bar\theta_h.
\tag{LFT35}
\]

**Proof.** Apply LFT21 to \(r\), whose transpose is \(h\),
and substitute \(V_2H\) for its coefficient object. Its
proper endpoint is \(A_r\), and its ordinary endpoint is
\(\overline G_r\), with the right-line cancellation in that square. Apply \(V_1\), insert
\(v_2^{-1}:H\to P_2V_2H\), and use
\(u_1^{-1}:V_1P_1\to1\) at the output. At the proper
endpoint this is exactly LFT30. At the ordinary endpoint it
is exactly LFT34a. Naturality of \(\bar\theta_h\) moves
\(h^{-1}v_2^{-1}\) through that trace comparison to
\(h^!v_2^{-1}\otimes1\). Naturality of \(u_1^{-1}\)
with respect to \(Rr_!\to Rr_*\) identifies the lower
map with \(\nu_rV_2\). This proves LFT35 without
replacing either adjunction structure or reordering
\(h^!H\otimes L^{-1}\). \(\square\)

## SH02-LFT-TRANSPOSE-AUDIT. The complete comparison and its proof

We describe the other map with the same domain and target.
Let \(E_h:T_1h^!\to Rr_*T_2\) be the original R2
map. It can be written without an unnamed inverse-equivalence
comparison. If \(B_h:Q_1Rr_*\to h^!Q_2\) is the
right mate of
\(A_h^{-1}:T_2Rh_!\to r^{-1}T_1\), then
\[
\begin{aligned}
E_h:T_1h^!
&\xrightarrow{T_1h^!\eta_2^T}T_1h^!Q_2T_2\\
&\xrightarrow{T_1B_h^{-1}T_2}T_1Q_1Rr_*T_2
 \xrightarrow{\varepsilon_1^T}Rr_*T_2.
\end{aligned}
\tag{LFT36}
\]
Here \(\eta_i^T,\varepsilon_i^T\) are the unit and
counit of \(T_i\dashv Q_i\). In particular
\(B_h^{-1}\) is the L2 map for \(r\) before its L3
orientation rewrite.

Let \(\mathcal R_{12}\) be the equivalence on sheaves
over \(E_1^*\) given by output antipode followed by right
tensoring with \(W_2\). The R4 source rewrite in FF
is the specified isomorphism
\[
\lambda_h:V_1h^{-1}H
 \xrightarrow{\sim}
 \mathcal R_{12}T_1(L\otimes h^{-1}H).
\tag{LFT39}
\]
Define
\[
\Theta_h^{\mathrm{FF}}=
\mathcal R_{12}(E_hT_1\theta_h)\circ\lambda_h:
V_1h^{-1}H\longrightarrow Rr_*V_2H,
\tag{LFT40}
\]
where the last target uses the canonical ordinary-image
exchange with the output antipode and the base-pulled line.
Thus every map in LFT40 is an existing FF map or its
explicitly stated tensor rewrite.

**Theorem.** FTC14 with the original FF endpoints is equivalent to the following equality, proved by FTE32–FTE33:
\[
J_h^{\,\mathrm{dir}}\circ V_1\bar\theta_h
 =\Theta_h^{\mathrm{FF}}.
\tag{LFT41}
\]
Indeed the inverse R4 rewrite carries \(D_h\) to \(C_h\).
The equivalence \(\mathcal R_{12}\) respects the proper-
support inclusion under its canonical output-antipode and
bounded-line comparisons. It therefore carries
\(\nu_rT_2D_h=E_hT_1\theta_h\) to
\(\nu_rV_2C_h=\Theta_h^{\mathrm{FF}}\).
Substitute LFT35 to obtain LFT41. Faithfulness of the
equivalence proves both directions. FTE32 identifies \(J_h^{\mathrm{dir}}\) with the full R3 rewrite \(F_h\), and FTE33 evaluates its composite with \(V_1\bar\theta_h\) as \(\Theta_h^{\mathrm{FF}}\). This proves LFT41 and therefore FTC14. The coherent endpoint \(J_h^{t,c}\) carries the relative-rank sign in LFT34c, so it cannot replace the braided or direct endpoint without that factor.

The center and scalar results do not prove LFT41 by
themselves. Its comparison includes both the exceptional
antipode action LFT-A4 and the actual R3/R4 line
extractions. The tensor identity LFT-L3 must be applied
with those extraction maps still present. A sign from it
cannot be added again if it is already represented by the
exceptional orientation action.

The line projection gives a useful concrete check. Let
\(h:\mathbb R\to0\), \(k=\mathbb Z\), and
\(H=\mathbb Z\). Then \(r:0\hookrightarrow\mathbb R^*\)
is proper and \(\nu_r=1\), while
\(\theta_h(H)\) is the positive orientation
identification. R2 is the positive integration trace:
its ordinary adjunct is \(A_h\) followed by
\(\operatorname{tr}_h\). R1 for this map is the
inverse dual Fourier unit on the zero-section object,
which has the positive literal reverse-chain normalization
computed above. Its R4 rewrite is the right projection
formula, with the constant input in degree zero.
Consequently the two original maps are both
\(+\mathrm{id}\) on \(\mathbb Z_{\{0\}}\).
The different endpoint \(D_h^0=-D_h\) does not refute
the original square. This test shows why a proposed
transpose reduction that uses only LFT38 is insufficient.

The proof of LFT41 preserves the FF R1/R4 maps. It completes the earlier endpoint obligation by comparing all of its specified line maps. The downstream microlocal endpoint propagation is proved in SH02-MEP-SUPPORT and SH02-MEP-TRACE, including the precise adjoint-mate comparison SH02-MEP-MATE-UNTWIST.

## SH02-LFT-RESEARCH. A finite geometric reduction and further tests

The factorization in Problem 4 reduces the second equation to three
geometric types: a zero inclusion into a direct-sum bundle, a bundle
automorphism, and a projection from a direct-sum bundle. It applies to
every continuous rank-changing bundle map in this lesson.

Here is why proving FTC14 for those three types would suffice. For
composable \(E_1\xrightarrow{h}E_2\xrightarrow{g}E_3\), the trace
comparison is the ordered composite
\[
\begin{aligned}
\omega_h\otimes h^{-1}\omega_g\otimes h^{-1}g^{-1}H
&\xrightarrow{1\otimes h^{-1}\theta_g}
\omega_h\otimes h^{-1}g^!H\\
&\xrightarrow{\theta_h}h^!g^!H\simeq(gh)^!H.
\end{aligned}
\tag{LFT37}
\]
Its exceptional adjunct is the trace of \(h\) followed by that of
\(g\); exceptional transitivity identifies this with the trace of
\(gh\). The projection-formula associators identify its source with
the source of \(\theta_{gh}\). This proves LFT37 with its map.
For the reversed transpose composite, the two support inclusions
compose by FTC8. The maps \(A_h\) respect composition by the
cartesian pasting in FF6. Their mates do so by FF10 and the triangle
identities. Finally FF12 evaluates the intermediate inverse
orientation pair in the same order. Pasting the two FTC14 squares
therefore proves the square for \(gh\).

The generator reduction is an alternative route to the transpose comparison proved in SH02-FTE-TRACE. A separate proof by factorization would have to retain
all three types. In particular, projections and automorphisms alone do not generate all
bundle maps: they are fiberwise surjective, whereas the zero inclusion
usually is not. A proof by this route must keep its zero-inclusion
case and must verify the same R2 and R4 maps, including their trace
normalizations.

**Problem 5.** Suppose a proposed proof knows only that
\(C_h\) and \(C_h^0\) are isomorphisms. Identify the missing assertion,
and explain why a failure of its strongest version need not refute
FTC14.

**Solution.** LFT32 and LFT38 compare the two endpoint constructions, but the trace equation requires LFT41. That equality also involves the exceptional antipode action and the full line extraction of R3/R4. Thus neither invertibility nor a nontrivial scalar by itself settles the comparison. The integral line-projection test above has a nontrivial paired scalar but agrees at the original two trace endpoints.

**Problem 6.** What happens to this reduction when both bundles have
rank zero?

**Solution.** Each total space and dual total space is \(B\), and
the only bundle map over its identity is that identity. Both pairing
cuts are \(B\); all projections and both Fourier transforms are
identities, and \(W_i=k_B\). The kernel adjunction units and counits,
their transported versions, the traces, and the support comparisons
are identity maps. Thus \(\delta_i=1\), and LFT41 holds on every
\(D^+(B;k)\), including arbitrary base topology and arbitrary
bounded-below coefficients. This checks the degenerate rank case
and explains why rank zero cannot detect the odd-rank parity defect.

**Problem 7.** In the trivial bundles of ranks two and one over
\(\mathbb R\), let \(h_b(x,y)=bx\). Does the correction in
LFT38 jump at \(b=0\)?

**Solution.** The rank of the linear map drops from one to zero
there, but the two bundle ranks remain two and one. Hence
\(\epsilon_h=(-1)^{2-1}=-1\) on the entire base. The two comparison constructions in LFT38 differ uniformly by
that scalar. The full transpose proof also retains the additional line maps, as shown in SH02-FTE-INPUT and SH02-FTE-ADJOINT.
No discontinuous sign choice or kernel bundle is involved.
Over a coefficient ring with \(2=0\) that scalar is the
identity, but such a restriction is not needed for the
comparison calculation.

## SH02-LFT-SOURCES. Support maps, kernel adjunctions and the additional scalar argument

Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.5, pp. 92–94](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=92), distinguishes the ordinary base-change morphism from the proper-support base-change isomorphism. Proposition 4.5.1 adds properness on the support for the ordinary comparison; Theorem 4.5.3 proves the proper-support statement on bounded-below complexes. LFT4, LFT8 and LFT16a–LFT16b retain that distinction at the level of arrows. In particular the proof never inverts ordinary base change merely because a fiber has a simple topology, nor moves a closed tensor cutoff freely through an ordinary image.

The adjunction mechanisms are compared with [§4.6, pp. 94–97, and §4.9, pp. 100–101](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=94). The exceptional right adjoint requires a finite cohomological-dimension hypothesis. Propositions 4.6.4–4.6.6 construct tensor and internal-Hom comparisons from projection formula and the counit; formulas (4.9.6)–(4.9.7) identify the raw right adjoint of a kernel transform. Section 4.9 imposes bounded kernels and finite soft dimension of the spaces. LFT6 and LFT17 use the same adjunction method but keep every mate, trace and relative-line map explicit under this reading's separate operation contracts. The full bounded-below range uses the course truncation proof, not an unstated extension of the bounded source formulas.

For the halfspace geometry, [Lemma 5.4.2 and its proof, pp. 112–113](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=112), reduce the local comparison to a product coordinate and compact-support vanishing on a closed halfline. This is the relevant local mechanism away from the kernel in LFT11. When the pairing is degenerate, that coordinate is unavailable on the kernel. LFT10 therefore retains support forgetting as a possibly noninvertible middle arrow. LFT16 proves its compatibility by the actual ordinary closed-cut comparison; LFT21 compares the two complete routes using only endpoint isomorphisms already proved. The zero-map and rank-jumping problems explain why this extra step is necessary. Schapira's subsequent sphere-bundle inversion proof does not supply this degenerate full-bundle support square.

The later paired-adjunction calculation is a further programme argument. LFT-C1 first passes to sheaves on the conic topology using restrictions along interval-shaped orbit intersections. SH02-LFT-CENTER then argues in the derived enhancement, through injectives, the finite stable envelope and a uniformly bounded-below truncation tower. Only after that argument makes the paired defect a base scalar does the zero-section test determine it. The source passages just named do not prove this enhanced-center lemma or identify the paired scalar. The underlying enhanced-category, finite-cofiber and homotopy-limit facts remain part of the stated derived foundations; checking a single sheaf does not replace them.

The trace calculation also keeps the exceptional antipode action on arbitrary coefficients and the two orders of the relative line. LFT34–LFT41 reduce the complete endpoint to the separately written proof in SH02-FTE-TRACE. A relative-rank scalar by itself does not prove that endpoint equality. The integral rank-one test separates two local course constructions; it is not a source-book erratum. The graph-factorization argument is retained as a useful alternative route with its required zero-inclusion case, and all seven complete solutions remain part of the reading.

The organization around a noninvertible support arrow, its countertest, an enhanced-center argument and a fully transposed endpoint is compared here with the source's bounded operation and sphere-kernel discussions. Shared adjunction identities and halfline calculations are standard mathematical ingredients; no source chapter, diagram or exercise sequence is incorporated. This comparison establishes the scope of the passages actually read, not independence from an unread book. Independently expressed text is CC0; actual human component terms and the separate transitive-proof obligations remain in force.

## SH02-LFT-STATUS. What this supplement proves

The direct halfspace proof establishes LFT21 with its explicitly defined direct kernel comparison, for arbitrary continuous bundle maps over a locally compact Hausdorff base, including rank jumps. It remains relative to the declared operation and conic-contraction imports. The rank-one test correctly separates LFT17 from the uncontracted FF L3 map. SH02-FGC-EXTRACTION supplies their full-map sign comparison, and SH02-FGC-SUPPORT proves the support equation FTC13b with its initial extraction and final braided contraction separately named. SH02-MEP-SUPPORT propagates that endpoint through the microlocal square, and SH02-MEP-MATE-UNTWIST verifies its equality with the actual ordinary adjoint mate. These conclusions concern the displayed course maps; the source account does not add an identification with an unspecified external normalization.

The enhanced-center theorem and the actual input-antipode calculation
still establish the paired scalar LFT-P0 and the difference LFT38.
The unconditional transpose equation LFT35 uses the direct endpoint LFT34a. SH02-FTE-TRACE proves LFT41 and FTC14 after the complete comparison of the coherent and braided endpoints in LFT34–LFT34c. The precise mate is proved in [Following the microlocal comparison maps](microlocal-endpoint-propagation.md): MEP16 corrects the old unsigned target PA32 to the relative-rank signed uncontracted equation, and MEP20 identifies its contracted form with the required braided endpoint. MEP11 and MEP14 prove downstream propagation into both microlocal squares. The source account distinguishes the declared course maps in FTC13b and FTC14 from the classical kernel framework. The distinct negative-normalization assertion is proved in SH02-NDF-SOURCE-MAPS by the full defect calculation and unique paired-inverse comparison; the precise mate calculation is the separate full Hom-bijection and graded-line proof in SH02-MEP-PRECISE-MATE, not a consequence of that normalization assertion or of endpoint types.
