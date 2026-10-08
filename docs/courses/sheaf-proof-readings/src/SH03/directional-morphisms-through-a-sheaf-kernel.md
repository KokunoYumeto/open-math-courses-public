# Directional morphisms through a sheaf kernel

A kernel transform has an ordinary adjunction. It also has a comparison at each cotangent direction. The latter is an isomorphism of sheaves on a cotangent region, so it contains more information than an adjunction between global morphism groups. We will construct this comparison in both directions and prove its invertibility by cutting off the input over a compact part of the chosen cotangent region.

Use [Kernels that preserve chosen cotangent directions](kernels-that-preserve-chosen-cotangent-directions.md) and [Adjoints of localized sheaf kernels](adjoints-of-localized-sheaf-kernels.md). The definition, support bound and natural transformations for microlocal Hom come from [Local morphisms in cotangent directions](../SH02/microlocal-hom.md#sh02-mh-hom--the-sheaf-of-directional-morphisms). We use the [microlocal direct-image comparison](../SH02/microlocalization.md#sh02-mic-direct--pushing-forward-a-normal-limit) and the [inverse-image comparison for a map whose restriction to the centers is a submersion](../SH02/local-forms-and-inverse-image.md#sh02-lfi-submersive-centers--a-simpler-test-on-the-centers). Their precise hypotheses are recalled below. The proofs remain relative to those operation and microlocalization prerequisites.

Kashiwara and Schapira's *Microlocal Study of Sheaves*, Theorem 6.3.9 and its proof, pp. 115–117, is the human antecedent for the common diagonal-Hom construction: both sides are obtained from one fourfold kernel using direct and inverse microlocalization comparisons. That theorem is stated for a contact correspondence satisfying the constructibility and microlocal endomorphism assumptions of Theorem 6.3.4. The one-sided admissibility theorem proved here has different scope. Its extra work is the two separate no-escape checks, the orientation calculation for each repeated coordinate, and compact replacement over each output neighborhood. The source theorem alone would not justify discarding its additional assumptions.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## A sheaf of directional morphisms

Let \(k\) be a commutative unital ring of finite global dimension. Manifolds are smooth, Hausdorff, finite dimensional and countable at infinity. All input complexes are globally bounded complexes of arbitrary sheaves of \(k\)-modules. We impose no constructibility, perfectness or Noetherian condition.

For the projections \(r_1,r_2:M\times M\to M\), set

\[
\mu\operatorname{hom}_M(A,B)
=\mu_{\Delta_M}R\mathcal Hom(r_2^{-1}A,r_1^!B).
\tag{1}
\]

Here \(\mu_{\Delta_M}\) means normal specialization followed by Fourier–Sato transformation with kernel \(\langle v,\xi\rangle\leq0\). Identify the diagonal conormal with \(T^*M\) by
\((m,m;\xi,-\xi)\mapsto(m;\xi)\). Thus the retained covector belongs to the **target** coordinate in (1).

The prerequisite gives boundedness, functoriality in both arguments, the support inclusion and ordinary recovery

\[
\begin{split}
\operatorname{supp}\mu\operatorname{hom}_M(A,B)
&\subset\operatorname{SS}(A)\cap\operatorname{SS}(B),\\
R\pi_*\mu\operatorname{hom}_M(A,B)
&\simeq R\mathcal Hom(A,B),
\end{split}
\tag{2}
\]

where support is closed support and \(\pi:T^*M\to M\). Restricting to an arbitrary open cotangent region is permitted; the region need not be conic. Formula (2) over the whole bundle does not identify morphisms in every localized category with sections over every open region.

Let \(P=X\times Y\), with projections \(q_1,q_2\). For a bounded kernel \(K\) on \(P\), write

\[
\begin{split}
\Phi_KG&=Rq_{1!}(K\otimes^Lq_2^{-1}G),\\
\Psi_KF&=Rq_{2*}R\mathcal Hom(K,q_1^!F),\\
Q(F,G)&=R\mathcal Hom(q_2^{-1}G,q_1^!F).
\end{split}
\tag{3}
\]

Boundedness of these complexes is supplied by the manifold bounds used in the adjoint lesson. On \(T^*P\), use

\[
p_1(x,y;\xi,\eta)=(x;\xi),\qquad
p_2^a(x,y;\xi,\eta)=(y;-\eta).
\tag{4}
\]

The twisted kernel relation is

\[
C_K=\{((x;\xi),(y;\alpha)):
(x,y;\xi,-\alpha)\in\operatorname{SS}(K)\}.
\tag{5}
\]

Recall the two separate conditions. **Forward admissibility** over \(\Omega_X\) says that the part of \(C_K\) with first coordinate in \(\Omega_X\) is contained in \(\Omega_X\times\Omega_Y\), and its projection to \(\Omega_X\) is proper. **Reverse admissibility** over \(\Omega_Y\) says that the part with second coordinate in \(\Omega_Y\) is contained in \(\Omega_X\times\Omega_Y\), and its projection to \(\Omega_Y\) is proper. Both properness statements control the entire forgotten cotangent coordinate, including its base point.

**Theorem 1.** There are natural comparisons, invertible under the indicated one-sided conditions:

\[
\begin{split}
\mu\operatorname{hom}_X(\Phi_KG,F)|_{\Omega_X}
&\xrightarrow{\sim}
(Rp_{1*}\mu\operatorname{hom}_P(K,Q(F,G)))|_{\Omega_X}
&&\text{if }K\text{ is forward admissible},\\
\mu\operatorname{hom}_Y(G,\Psi_KF)|_{\Omega_Y}
&\xrightarrow{\sim}
(R(p_2^a)_*\mu\operatorname{hom}_P(K,Q(F,G)))|_{\Omega_Y}
&&\text{if }K\text{ is reverse admissible}.
\end{split}
\tag{6}
\]

In the first line, \(G\) may be taken in the localized category over \(\Omega_Y\); \(F\) may be taken over \(\Omega_X\). The same is true in the second line. The theorem asserts a comparison of cotangent sheaves, with the actual ordinary direct images and antipode displayed. Its proof uses neither duality of arbitrary sheaves nor a compact-support tensor description of their internal Hom.

## The two microlocal comparison inputs

We use the following exact parts of the microlocalization calculus.

For inverse image, the comparison is traced to *Microlocal Study of Sheaves*, Theorem 5.4.1, pp. 85–89. Remark 5.4.3, p. 90, removes its first and third conditions when the map of centers is a submersion, leaving the local noncharacteristic condition. The sequence criterion for that condition is Proposition 1.2.6(ii), p. 19, together with Definition 5.3.1, p. 83. These locators explain why boundedness of the entire ambient covector is the decisive check below. The direct-image antecedent is Proposition 2.3.4, p. 48; its stated isomorphism case is transverse and proper on support. The ordinary direct comparison and the clean-map normal-support formulation used here are supplied by the linked microlocalization prerequisite. In the actual applications below the maps are product projections with transverse inverse centers, so the proof verifies this more concrete geometry as well.

First, suppose \(h:(A,N)\to(B,M)\) is a map of manifolds with centers, \(N=h^{-1}M\), and \(h|_N\) is a submersion. On an open part of the conormal of \(N\), assume the **local noncharacteristic condition at infinity** for a complex \(E\) on \(B\): there is no sequence

\[
a_n\to a_0,\quad (b_n;\beta_n)\in\operatorname{SS}(E),
\quad b_n\to h(a_0),\quad
dh_{a_n}^{,t}\beta_n\to\gamma_0,
\quad |b_n-h(a_n)|\,|\beta_n|\to0,
\quad |\beta_n|\to\infty,
\tag{7}
\]

with \((a_0;\gamma_0)\) in that open conormal part. The exceptional inverse microlocal comparison is then invertible there. In our applications the map of centers is the identity. Its cotangent base change is therefore the identity as well, so no exceptional orientation factor remains on that side of the comparison. This is the submersive-centers case of the inverse theorem; a check of the ordinary kernel of \(dh^t\) alone would not suffice.

Second, for a clean map of pairs \(h:(A,N)\to(B,M)\) with \(N=h^{-1}M\), the ordinary direct microlocal comparison is invertible if \(h\) is proper on the closed support of \(E\). Clean means that the normal derivative embeds the normal bundle of \(N\) into the pulled-back normal bundle of \(M\). The prerequisite's normal-cone properness lemma then supplies the additional properness on the normal support. The support and inverse-center conditions are also needed; this statement does not discard them for an arbitrary proper map.

All the comparisons are the ones formed from specialization, Fourier transformation, adjunction units and counits, and relative trace. We use their specified maps, not merely isomorphisms between their endpoint objects.

## One fourfold kernel, with every orientation retained

Put

\[
B=X_1\times Y_2\times X_3\times Y_4,
\qquad N=\Delta_P\subset B.
\]

Subscripts indicate coordinates rather than copies of the coefficient ring. Let

\[
H=R\mathcal Hom\left(K_{34}\otimes^LG_2,
F_1\otimes\omega_{Y_2}\otimes\omega_{X_3}\otimes\omega_{Y_4}\right).
\tag{8}
\]

Inverse images along the displayed projections are implicit. Each \(\omega_M=\operatorname{or}_M[\dim M]\) is retained in its displayed order; every permutation uses the Koszul tensor symmetry.

By tensor–Hom adjunction, (8) is the defining kernel of
\(\mu\operatorname{hom}_P(K,Q(F,G))\): applying the target projection's exceptional inverse image on \(P\times P\) adds \(\omega_{X_3}\otimes\omega_{Y_4}\), while \(q_1^!F\) inside \(Q\) already adds \(\omega_{Y_2}\). Hence

\[
\mu_NH=\mu\operatorname{hom}_P(K,Q(F,G)).
\tag{9}
\]

This is the external estimate of Kashiwara–Schapira, Proposition 4.2.2, pp. 64–65, also stated by Schapira as Theorem 2.8. Its proof treats each independent coordinate by a local support test and an ordinary/compact-support Hom adjunction. It does not replace an arbitrary sheaf by the dual of a dual. Applied in the independent coordinates of the present fourfold product, it yields the following bound.

The external Hom estimate, applied twice, gives

\[
\operatorname{SS}(H)\subset
\operatorname{SS}(F)_1\times\operatorname{SS}(G)^a_2
\times\operatorname{SS}(K)^a_{34}.
\tag{10}
\]

To apply it to an ordinary inverse-image factor, insert and cancel its invertible projection orientation. Such factors do not change microsupport. The coordinates in (10) are independent, so this is the external Hom bound, without a constructibility-dependent dual–tensor substitution.

## The forward comparison

Define

\[
A_X=X_1\times X_3\times Y,
\quad j_X(x_1,x_3,y)=(x_1,y,x_3,y),
\quad u_X(x_1,x_3,y)=(x_1,x_3).
\tag{11}
\]

The inverse image of \(N\) under \(j_X\) is
\(M_X=\Delta_X\times Y\). The map of centers is the identity of \(X\times Y\). Under the first-covector identification, its conormal correspondence projects
\((x,y;\xi,\eta)\mapsto(x,y;\xi)\), forgetting \(\eta\).

**No escape for \(j_X\).** Consider a sequence as in (7), whose pulled-back limit is
\((x_0,x_0,y_0;\xi_0,-\xi_0,0)\), with \((x_0;\xi_0)\in\Omega_X\). Write a covector of (10) as
\((\xi_1,\eta_2,\xi_3,\eta_4)\). Its pullback is
\((\xi_1,\xi_3,\eta_2+\eta_4)\). Therefore
\((x_3;-\xi_3)\to(x_0;\xi_0)\), and
\((x_3,y_4;-\xi_3,-\eta_4)\in\operatorname{SS}(K)\).

Choose a compact neighborhood of \((x_0;\xi_0)\) inside \(\Omega_X\). Forward properness bounds \(\eta_4\) for all sufficiently late terms. The convergence of \(\eta_2+\eta_4\) then bounds \(\eta_2\); the other two components already converge. Thus the whole ambient covector is bounded, contradicting (7). This works for every \(y_0\) and for every relevant conormal covector. It uses actual nearby points, so the weighted base error in (7) causes no omitted escape.

The submersive-centers inverse comparison consequently gives

\[
\mu_{M_X}j_X^!H\simeq Rr_{X*}\mu_NH
\quad\text{over the part projecting to }\Omega_X.
\tag{12}
\]

Here \(r_X\) is the conormal projection just described. To compute the left side, use the exact internal Hom identity
\(j^!R\mathcal Hom(A,E)=R\mathcal Hom(j^{-1}A,j^!E)\).
The target of (8) is locally constant in the repeated \(Y\)-normal coordinate except for its invertible orientation factors. Exceptional restriction cancels \(\omega_{Y_4}\), leaving

\[
j_X^!H\simeq
R\mathcal Hom(K_{3Y}\otimes^LG_Y,
F_1\otimes\omega_{X_3}\otimes\omega_Y).
\tag{13}
\]

There is no leftover \([\dim Y]\) shift: it has been cancelled by the embedding's relative dualizing complex. Internal Hom adjunction for proper-support image now gives

\[
Ru_{X*}j_X^!H\simeq
R\mathcal Hom(r_2^{-1}\Phi_KG,r_1^!F)
\quad\text{on }X\times X.
\tag{14}
\]

Indeed the complex before integration is
\(K_{3Y}\otimes G_Y\); its proper-support image along \(u_X\) is
\(r_2^{-1}\Phi_KG\) by proper-support product base change. The target in (13) equals \(u_X^!r_1^!F\). Applying
\(Ru_*R\mathcal Hom(A,u^!E)=R\mathcal Hom(Ru_!A,E)\)
proves (14).

Apply the ordinary direct microlocal comparison to \(u_X\), then (12). This constructs the first map of (6). If \(G\) has compact closed support, it is an isomorphism: the support of (13) is contained in \(X^2\times\operatorname{supp}G\), so \(u_X\) is proper there. It is a product projection, transverse to \(\Delta_X\), with inverse center \(M_X\). Its normal derivative is the identity in the \(X\)-difference coordinate. Thus the exact clean normal-support criterion applies. Finally \(u_X\) after \(r_X\) is \(p_1\); composition of ordinary direct images gives the displayed target of (6).

## The reverse comparison

For the second map, retain the same \(B,N,H\), and instead put

\[
A_Y=Y_2\times Y_4\times X,
\quad j_Y(y_2,y_4,x)=(x,y_2,x,y_4),
\quad u_Y(y_2,y_4,x)=(y_2,y_4).
\tag{15}
\]

Now the inverse center is \(M_Y=\Delta_Y\times X\), again mapping identically onto \(N\). Its conormal projection \(r_Y\) retains the \(Y_2\)-covector \(\eta\) and forgets the \(X\)-covector.

**No escape for \(j_Y\).** A pulled-back covector of (10) is
\((\eta_2,\eta_4,\xi_1+\xi_3)\). Suppose it converges to
\((\eta_0,-\eta_0,0)\), with \((y_0;-\eta_0)\in\Omega_Y\). The kernel's twisted input coordinate is \((y_4;\eta_4)\), which tends to \((y_0;-\eta_0)\). Reverse properness therefore bounds its other coordinate \((x_3;-\xi_3)\). The convergence of \(\xi_1+\xi_3\) bounds \(\xi_1\). Both \(Y\)-components already converge. Once again every ambient component is bounded, excluding (7). Consequently

\[
\mu_{M_Y}j_Y^!H\simeq Rr_{Y*}\mu_NH
\quad\text{over the part with }(y;-\eta)\in\Omega_Y.
\tag{16}
\]

Exceptional restriction now cancels \(\omega_{X_3}\). Its precise result is

\[
j_Y^!H\simeq
R\mathcal Hom(K_{XY_4}\otimes^LG_{Y_2},
F_X\otimes\omega_{Y_2}\otimes\omega_{Y_4}).
\tag{17}
\]

Use tensor–Hom adjunction to put \(G_{Y_2}\) in the outer Hom. Ordinary direct image commutes with this outer Hom by internal Hom adjunction, since that input is pulled back from \(Y^2\). Smooth product base change for the independent \(Y_2\)-coordinate, followed by the projection formula for its invertible orientation complex, gives

\[
Ru_{Y*}j_Y^!H\simeq
R\mathcal Hom(s_1^{-1}G,s_2^!\Psi_KF)
\quad\text{on }Y_2\times Y_4.
\tag{18}
\]

In detail, integrating the inner Hom in (17) over \(X\) is the pullback from \(Y_4\) of
\(Rq_{2*}R\mathcal Hom(K,F_X\otimes\omega_{Y_4})=\Psi_KF\).
The remaining \(\omega_{Y_2}\) is exactly the orientation of the fiber of \(s_2\). This argument uses ordinary product base change for a submersion with an independent coordinate, not unrestricted nonproper base change.

The kernel in (18) has its **source** in the first \(Y\)-coordinate. Exchanging the two factors turns it into the kernel in (1); the exchange sends the diagonal conormal \((\eta,-\eta)\) to \((-\eta,\eta)\). Its microlocalization is therefore
\(a_Y^{-1}\mu\operatorname{hom}_Y(G,\Psi_KF)\).

The ordinary direct comparison for \(u_Y\), followed by (16) and this factor exchange, constructs the second map of (6). If \(F\) has compact closed support, (17) is supported in \(Y^2\times\operatorname{supp}F\). The same clean product-projection argument as before makes the direct comparison invertible. The final projection is \(a_Y\circ p_2=p_2^a\), proving the second formula with its sign. No constructibility-dependent bidual identification was used in this argument.

## Compact replacement proves the general case

This is the point where the present argument goes beyond the contact-graph proof in Theorem 6.3.9. We first isolate a compact set of forgotten base points from cotangent properness. A compactly supported replacement agrees with the input near that set, and both sides of the actual natural comparison kill its cone over the chosen output neighborhood. The compact-support isomorphism therefore transfers through a naturality square. This step needs the forward or reverse transform estimate from the corresponding prerequisite; ordinary recovery of microlocal Hom by itself would not supply it.

We remove the temporary support assumptions and make the locality argument explicit. The external Hom estimate gives

\[
\operatorname{SS}(Q(F,G))
\subset\operatorname{SS}(F)\times\operatorname{SS}(G)^a.
\tag{19}
\]

By (2), the support of the cotangent sheaf on the right side of (6) is contained in
\(\operatorname{SS}(K)\cap\operatorname{SS}(Q(F,G))\).

For the forward formula, choose a compact neighborhood \(A\) inside \(\Omega_X\). The part of \(C_K\) over \(A\) is compact. Its projection to the base \(Y\) is a compact set \(D\). If the closed support of an input \(G_0\) misses \(D\), (19) and (2) make
\(Rp_{1*}\mu\operatorname{hom}_P(K,Q(F,G_0))\)
zero on the interior of \(A\). Ordinary direct image is local on its target, so this follows by restricting to \(p_1^{-1}(\operatorname{Int}A)\) before pushing.

The other side also vanishes there. The kernel microsupport bound from the forward lesson gives
\(\operatorname{SS}(\Phi_KG_0)\cap A=\varnothing\), since a possible input covector would have its base in \(D\). Then (2) gives the required vanishing of microlocal Hom.

Choose a relatively compact open \(V\subset Y\) containing \(D\), and write
\(G'=j_!j^{-1}G\), where \(j:V\hookrightarrow Y\). Its closed support lies in the compact set \(\overline V\). The canonical map \(G'\to G\) is an isomorphism near \(D\); its cone \(G_0\) has closed support disjoint from \(D\). Apply both functors in the first line of (6) to this triangle. They are contravariant in \(G\), so both arrows from the value at \(G\) to the value at \(G'\) are isomorphisms on \(\operatorname{Int}A\). Naturality gives a square whose bottom comparison is already an isomorphism by the compact-support proof. Its top comparison is therefore an isomorphism too.

For the reverse formula, choose a compact neighborhood \(A\subset\Omega_Y\), project the compact part of \(C_K\) over it to a compact \(D\subset X\), and use \(F'=j_!j^{-1}F\) for a relatively compact open neighborhood of \(D\). Formula (19) makes the right side zero for the cone of \(F'\to F\). The reverse microsupport bound makes \(\Psi_K\) of that cone invisible over \(A\), so (2) makes the left side zero as well. Both functors are covariant in \(F\); the same naturality square now has vertical arrows in the opposite direction and proves the claim. Compact neighborhoods of this kind cover both open cotangent regions. This completes the proof of Theorem 1. \(\square\)

The same support argument proves the stated use of localized inputs. A denominator has a cone whose microsupport misses the appropriate input region. Admissibility and (19) make its contribution to the right side invisible, while the localized transform and (2) do the same on the left. The comparison consequently descends in both input variables. This is a cone argument for the actual morphism of cotangent sheaves; no identification of localized Hom groups with global cotangent sections has been inserted.

## Exercises with complete solutions

### A shifted dilation

*Difficulty: Introductory.*

Let \(X=Y=\mathbb R\), \(f(y)=3y\), and \(K=k_{\Gamma_f}[s]\). Write both transform formulas and the covector relation. Check that shifting the target by \([t]\) produces the same net shift in both comparisons in (6).

**Solution.** The graph projection to \(X\) is the diffeomorphism \(f\), so
\(\Phi_KG=Rf_*G[s]\) and \(\Psi_KF=f^{-1}F[-s]\).
For \(k\neq0\), the twisted relation is \((y;\alpha)\mapsto(3y;\alpha/3)\); both projections are proper isomorphisms. For \(k=0\), all unital coefficient modules and \(K\) are zero, so the relation is empty and its projections are proper. The transform formulas hold in both cases. Shifts leave each relation unchanged. Microlocal Hom satisfies
\(\mu\operatorname{hom}(A[u],B[v])=\mu\operatorname{hom}(A,B)[v-u]\), directly from (1). The first formula for \(F[t]\) thus has shift \([t-s]\), and the second has the same shift because \(\Psi_K(F[t])=f^{-1}F[t-s]\). On the kernel side the first Hom input is shifted by \([s]\), while \(Q(F[t],G)=Q(F,G)[t]\), again giving \([t-s]\). The input covector in the second comparison is \(\alpha\), obtained by negating the physical kernel covector \(-\alpha\).

### Integration around a circle

*Difficulty: Intermediate.*

Take \(X=\{*\}\), \(Y=S^1\), and field coefficients. Let \(K=k_{S^1}\), \(G=k_{S^1}\), and \(F=k\). Use the full cotangent regions. Compute the complexes on both sides of each comparison, including their degrees.

**Solution.** Choose an orientation of the circle for this calculation. Then
\(\omega_{S^1}=k_{S^1}[1]\), \(\Phi_KG=R\Gamma(S^1;k)=k\oplus k[-1]\), and \(\Psi_KF=k_{S^1}[1]\).
The kernel microsupport is the zero section. Its projection to the point is proper because the circle is compact, and its projection to \(T^*S^1\) is a proper closed embedding. Thus both conditions hold.

For locally constant perfect complexes, (1) gives microlocal Hom supported on the zero section with value ordinary internal Hom. Therefore
\(\mu\operatorname{hom}_{S^1}(k_{S^1},\omega_{S^1})\)
is \(k_{S^1}[1]\) on that zero section. Its direct image to the point is
\(R\Gamma(S^1;k)[1]=k[1]\oplus k\).
On the other side,
\(R\operatorname{Hom}_k(k\oplus k[-1],k)=k\oplus k[1]\).
These agree, with cohomology in degrees \(-1\) and \(0\). For the reverse formula, both sides are \(k_{S^1}[1]\) on the zero section and zero away from it. The antipode fixes the zero section but is still part of the formula.

### Cutting off a noncompact input

*Difficulty: Intermediate.*

Let \(X=Y=\mathbb R\), \(K=k_\Delta\oplus k_{\mathbb R^2}\), and
\(\Omega_X=\Omega_Y=T^*\mathbb R\setminus T^*_{\mathbb R}\mathbb R\).
For the compact set \(A=\{(x;\xi):|x|\leq1,\ 1\leq|\xi|\leq2\}\), find a compact base set that supports the replacement argument. Explain why the constant-plane summand creates no additional directional morphisms over \(A\), even for noncompact \(G\).

**Solution.** If \(k\neq0\), the diagonal relation is the identity. The constant-plane summand has only zero covectors and contributes no relation above \(A\), so the actual projected relation base is \([-1,1]\). If \(k=0\), both summands vanish and the relation and its base projection are empty. In either case the compact set \(D=[-1,1]\) contains that projection. Take \(V=(-2,2)\) and \(G'=j_!j^{-1}G\). Its closed support is compact, and the cone of \(G'\to G\) is zero on a neighborhood of \(D\).

Microlocal Hom is additive in a finite direct sum in its first argument. The summand with first input \(k_{\mathbb R^2}\) has support contained in its zero-section microsupport by (2); hence it is zero above \(A\). On the transform side, the constant-plane contribution is locally constant in \(x\), with value \(R\Gamma_c(\mathbb R;G)\); it likewise has no nonzero output covectors. Thus the compact replacement works over the interior of \(A\), despite the nonproper support of the original kernel and the possible noncompactness of \(G\). This conclusion uses cotangent properness on the selected region.

### The orientation hidden in an omitted factor

*Difficulty: Advanced.*

In (8), suppose one drops \(\omega_{X_3}\otimes\omega_{Y_4}\), retaining only \(\omega_{Y_2}\). Determine the error in the forward and reverse restrictions. Explain why an arbitrary-sheaf biduality claim would not repair it.

**Solution.** Forward restriction along \(j_X\) contributes the inverse normal orientation \(\omega_Y^{-1}\). Without \(\omega_{Y_4}\), it cancels the remaining \(\omega_{Y_2}\), leaving a target \(F_1\) rather than
\(F_1\otimes\omega_{X_3}\otimes\omega_Y\) in (13). Both the exceptional factor for integration over \(Y\) and the exceptional factor for the second coordinate of \(X^2\) have been lost. The resulting direct-image kernel need not be (14).

Reverse restriction along \(j_Y\) contributes \(\omega_X^{-1}\). Without \(\omega_{X_3}\), this factor remains, and without \(\omega_{Y_4}\) the inner Hom no longer computes \(\Psi_KF\). The target is
\(F_X\otimes\omega_{Y_2}\otimes\omega_X^{-1}\), instead of the target in (17). These are degree and orientation errors before microlocalization; on nonorientable manifolds the line error is also nontrivial. Formula (8) is forced by the exceptional target projection in the definition (1). Biduality is neither used nor available for general bounded sheaves, and it cannot change the definition's missing projection orientation.

## References

- Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985): Proposition 1.2.6, p. 19; Propositions 2.3.4–2.3.5, p. 48; Proposition 4.2.2 and proof, pp. 64–65; Definition 5.3.1, p. 83; Theorem 5.4.1 and Remark 5.4.3, pp. 85–90; Definition 5.5.1 and Proposition 5.5.2, pp. 91–92; Theorem 6.3.9 and proof, pp. 115–117. The last theorem uses the contact and constructibility hypotheses displayed in Theorem 6.3.4, pp. 111–112.
- Pierre Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016: coefficient and orientation conventions, pp. 6–7; external Hom, Theorem 2.8, p. 10; diagonal definition, ordinary recovery and support bound for microlocal Hom, Definition 4.5 and equation (4.6), p. 23.

**Conventions and mathematical credit.** Definition 5.5.1 in the monograph and Definition 4.5 in the review use ordinary pullback in the source Hom argument and exceptional pullback in the target argument, with the first diagonal conormal covector retained. Those conventions produce the three orientation factors in (8). The factor exchange in the reverse calculation then accounts for the input antipode; it is not an orientation correction. The common-kernel proof organization has a concrete precedent in the proof of Theorem 6.3.9, and that dependence is acknowledged even though the present coordinates, exposition and exercises are independently written.

**Extent of this proof.** The two one-sided conclusions here retain arbitrary bounded sheaves, general open cotangent regions and separate properness assumptions. The no-escape, orientation and compact-replacement arguments establish the stated comparisons relative to the specified microlocal operation maps, the external Hom estimate, the forward and reverse transform estimates, and the manifold boundedness results. The selected source passages do not by themselves supply this whole formulation, and their comparison is not a claim that every prerequisite proof is closed. In particular, neither a dual–tensor substitution for arbitrary sheaves nor an identification of localized morphism groups with sections over every open region has been added. All four complete solutions remain part of the argument's checks.
