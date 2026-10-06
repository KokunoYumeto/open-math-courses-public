# Specializing Lefschetz contributions to the tangent space

At a transverse fixed point, a nonlinear map and a constructible coefficient can be replaced by their normal models. The replacement of the map is its derivative. The replacement of the sheaf is specialization, which retains how its support approaches the point. We prove that this replacement preserves the evaluated local class, including its orientation and grading.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Lefschetz traces of constructible correspondences, Natural duality for specialization and microlocal Hom, and Homotopies and local cutoffs for Lefschetz contributions. We use the earlier specialization construction with its actual inverse-image comparison, adjunction mates, equal-time external/tensor comparisons, zero-section support maps and conic calibration. Those are exact written programme prerequisites, together with the constructibility theorem; their transitive foundations and independent review remain open.

## The coefficient morphism uses a comparison in one direction

Let \(X\) be a real analytic manifold with the standing Hausdorff, countability and uniform finite dimension assumptions. Let \(k\) be a characteristic-zero field, \(F\in D^b_{\mathbb R\text{-c}}(k_X)\) have perfect stalks, and take
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

**Map check.** Transpose the first line under \(s_*\dashv s^!\). The exceptional tensor comparison and the central restriction counit give the restriction of
\[
 A\otimes D_DA\longrightarrow\omega_D.
 \qquad\text{(10)}
\]
Transpose (10) under \(j_!\dashv j^{-1}\). Since
\(D_D(j_!r^!F)=Rj_*r^{-1}D_XF\), open projection and restriction reduce it to
\[
 r^!F\otimes r^{-1}D_XF
 \longrightarrow r^!\omega_X.
 \qquad\text{(11)}
\]
This is the exceptional tensor comparison followed by \(r^!\mathrm{ev}_X\). The equal-time tensor comparison \(\mu\) is made from these same restriction counits on the positive chamber, followed by central restriction. Its boundary form transposes to exactly (11): the connecting map contributes the endpoint \([-1]\), while the positive exceptional pullback contributes \([1]\). The comparison for \(\omega_X\) is (6), with the same orientation.

Consequently both lines of (9) have the same adjoint (11). The open and closed adjunction bijections, and their triangular identities, prove equality before restriction and at the boundary. Agreement only on the positive chamber would not suffice; this check uses the prescribed boundary connecting map. It also explains why no extra sign or parameter degree remains in (9).

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
This arrow also need not be invertible.

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

**Proof.** It is useful to check the mate rather than invert (13). Write \(\eta,\epsilon\) for the diagonal unit and counit. By its definition, (14) is the composite
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
The middle map is the closed direct-image comparison just checked. This formula follows from the actual specialization-adjunction mate identity.

Apply it to the first line of (15), and transpose under \(\delta_{V*}\dashv\delta_V^!\). On the positive chamber, the result is the diagonal identity kernel of \(r^{-1}F\), transported through the common parameter. Currying its coefficient evaluation gives
\[
 r^{-1}F\xrightarrow{\mathrm{id}}r^{-1}F.
 \qquad\text{(17)}
\]
Indeed the diagonal unit followed by its counit in (16) is the diagonal triangular identity; the ordinary inverse comparison is defined by the restriction counits. Under open and central adjunction, the boundary transpose of (17) is \(\mathrm{id}_{s^!A}\): the central unit followed by its counit cancels, and the connecting map in (8) occurs once in each direction.

Perform the same transposition for the second line of (15). The external comparison (13) synchronizes the two parameters. Currying the dual factor uses precisely \(\sigma_F\), so (9) reduces this path to (11) and then to (17). The diagonal unit and counit again cancel. These computations take place under adjunction bijections: they identify the boundary maps, including their support counits, rather than identifying objects or only positive-chamber restrictions.

For completeness, the resulting internal-Hom comparison has adjoint
\[
 \nu_xR\mathcal Hom(F,F)\otimes\nu_xF
 \xrightarrow{\mu}
 \nu_x(R\mathcal Hom(F,F)\otimes F)
 \xrightarrow{\nu_x\mathrm{ev}}\nu_xF.
 \qquad\text{(18)}
\]
On \(\nu_x(\mathrm{id}_F)\), its adjoint is the identity by the tensor-unit and restriction-counit identities. Formula (16), (9) and the external restriction maps are exactly its diagonal mate. This gives the same computation of (15). The graded tensor order has remained fixed throughout. \(\square\)

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

**Proof.** Shrink the neighbourhood to retain only \(x\) in its fixed locus. Put \(h=(f,\mathrm{id})\) and \(h_0=(u,\mathrm{id})\). The lifted graph map and the equal-time product comparisons give
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

Pull (15) to the two graphs by the supported comparison. This operation is the closed-diagonal adjunction chain proved in the correspondence lesson, followed by the ordinary unit. That chain commutes with the lifted graph and with the closed-diagonal mate (16): transpose each side under the closed diagonal adjunction; both become the ordinary graph unit and the same restriction counits. Thus it identifies the pulled identity classes through (21), retaining support at the original fixed point and at its normal zero cone.

Take point-supported global sections of (22). Use (4) on its right column, and evaluate its bottom row using (9). For a readable supported diagram, abbreviate the original coefficients by
\(E_1=f^{-1}F\otimes D_XF\), \(E_2=F\otimes D_XF\), and the normal coefficients by
\(N_1=u^{-1}\nu_xF\otimes D_V\nu_xF\), \(N_2=\nu_xF\otimes D_V\nu_xF\).
The left horizontal arrows below are isomorphisms from (4); the right horizontal arrows are the actual lax comparisons:
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

The specialization of Lefschetz contributions to the tangent space belongs to Kashiwara's microlocal Lefschetz fixed-point formula for constructible sheaves. The proof above spells out the inverse comparison, diagonal mate, boundary duality, supported coefficient square and point-trace normalization behind the specialization diagram.

Y. Matsui and K. Takeuchi, [*Microlocal study of Lefschetz fixed point formulas for higher-dimensional fixed point sets*, arXiv 0812.4480v1](https://arxiv.org/abs/0812.4480v1), Proposition 3.3, gives the corresponding identity/evaluation comparison along a smooth fixed component. Its positive-dimensional setting requires a separate normal-eigenvalue condition and compactness for an integrated contribution. The point theorem here neither proves that generalization nor substitutes its integrated invariant for the normalized isolated class.

Y. Ike, Y. Matsui and K. Takeuchi, [*Hyperbolic localization and Lefschetz fixed point formulas for higher-dimensional fixed point sets*, arXiv 1504.04185v2, 25 May 2015](https://arxiv.org/abs/1504.04185v2), §2, Proposition 2.13, retains compact support on the smooth fixed component and exclusion of normal eigenvalue one. That statement refers to their earlier component proof. Later hyperbolic localization is further reading; the point proof and all its map checks above are supplied here.
