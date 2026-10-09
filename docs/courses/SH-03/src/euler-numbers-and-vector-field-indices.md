# Euler numbers and vector-field indices

The Euler characteristic of a compact manifold can be computed from finite cells, from duality, or from intersections of a section with the zero section. These calculations explain both the vanishing in odd dimension and the Hopf index formula. Orientation lines let the same argument work on nonorientable manifolds.

*Original programme exposition, examples and solutions are dedicated to the public domain under CC0.*

The [finite compact-cohomology proof](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#finite-descent-on-a-compact-triangulation) supplies the perfect section complexes, and the [trace-normalized dual-sections pairing](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#duality-exchanges-the-measurements-before-biduality) supplies their actual duality map. The [Euclidean compact-support generator](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-euclidean--the-compact-support-generator), [orientation line](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-orientation-line--orientation-as-a-local-system) and [submersion dualizing comparison](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-submersion--recovering-the-exceptional-inverse-image-locally) fix the integral Thom class and \(\omega_X=\operatorname{or}_X[n]\). We use a finite compatible subanalytic triangulation for the compact manifold. The proof below keeps the skeleton localization maps, so their Euler sum is an integer over every field.

For the index, the [continuous-section supported unit](continuous-sections-and-supported-cycle-intersections.md#a-continuous-section-supplies-a-supported-unit) and [complete supported comparison](continuous-sections-and-supported-cycle-intersections.md#the-complete-supported-section-intersection-comparison) identify the ordered cup with ordinary pullback of the cycle class and proper trace on its actual intersection. The [compact characteristic-cycle index](differential-sections-and-proper-below-euler-indices.md#recovering-the-base-class-from-the-microlocal-trace) evaluates that class for every continuous section. The [tangent sign of the graph-normalized conormal](orientations-of-conormal-cycles-and-transverse-intersections.md#the-normalized-conormal-retains-the-tangent-zero-section-sign) must be combined with the [signed constant-sheaf coefficient](integer-coefficients-and-additive-characteristic-cycles.md#local-ranks-use-an-actual-derived-constant-model); their two factors cancel for the positive zero-section Thom class used here. The [ordered transverse formula](orientations-of-conormal-cycles-and-transverse-intersections.md#ordered-transverse-forms-give-the-local-number) and [local map-of-pairs sign calculation](../../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-smooth-sign--submersion-signs) then fix the determinant without a global orientation choice.

Throughout, manifolds have no boundary. They are real analytic, Hausdorff and countable at infinity, with the standing finite dimension bounds. The compact manifold in the global theorems has dimension \(n\). The supported index is defined for continuous vector fields with isolated zeros. Its determinant formula applies when the field is continuously differentiable near the zero, in particular for smooth or analytic fields. Local indices require only an isolating neighborhood; compactness of \(X\) is used for the global Euler number and finite total trace.

## Finite cells give an integer independent of the field

Let \(k\) be any field and \(X\) compact. Compact constructible finiteness makes the following sum finite:

\[
 \chi_k(X)=\sum_j(-1)^j\dim_k H^j(X;k_X).
 \qquad\text{(1)}
\]

For a finite-dimensional local system \(L\) of constant rank \(r\) on a connected \(X\), we claim

\[
 \chi(X;L)=r\sum_{\sigma}(-1)^{\dim\sigma}
           =r\,\chi_k(X).
 \qquad\text{(2)}
\]

**Proof.** Fix a finite compatible triangulation, independent of the coefficient field, and let \(X_q\) be its closed \(q\)-skeleton, with \(X_{-1}=\varnothing\). Put \(L_q=L|_{X_q}\), let \(a_q:X_{q-1}\hookrightarrow X_q\) be the closed inclusion and \(b_q:X_q\setminus X_{q-1}\hookrightarrow X_q\) the open inclusion. The actual localization triangle is \(b_{q!}b_q^{-1}L_q\to L_q\to a_{q*}L_{q-1}\xrightarrow{+1}\). Applying \(R\Gamma_c(X_q;-)\), proper-support composition identifies its first term with the finite sum of compact section complexes on the open \(q\)-simplices, and its last term with \(R\Gamma_c(X_{q-1};L_{q-1})\).

Every such simplex is contractible, so the restricted local system is constant with fibre \(k^r\). The ordered compact-support calculation on \(\mathbb R^q\) gives \(R\Gamma_c(\sigma^\circ;L)=k^r[-q]\). These terms are perfect. Starting with the empty skeleton, the finite triangles also prove perfection of the whole section complex while retaining all attaching maps. Each finite long exact cohomology sequence has alternating dimension sum zero. Hence the difference between the Euler numbers of two successive skeleta is \(r(-1)^q\) times the number of their new \(q\)-simplices. At the final compact skeleton ordinary and compact sections coincide.

Adding the open-simplex contributions gives the first equality in (2). Applying the same argument to \(k_X\) gives the second. Euler additivity is an integer identity: for a finite cochain complex, the dimensions of the image of each differential occur once in each adjacent degree and cancel. No reduction of integers into \(k\) is involved.

In particular \(\chi_k(X)\) is the same integer for every field \(k\). For a disconnected compact manifold, apply the formula on each component. There are finitely many components: components are open, and compactness gives a finite subcover of their cover of \(X\). \(\square\)

Rank controls the Euler characteristic of a local system; its monodromy can still change the individual cohomology groups.

## Duality forces vanishing in odd dimension

Write \(\operatorname{or}_{X,k}\) for the orientation local system. It has rank one, whether or not it is globally trivial. The manifold dualizing complex and compact dual-sections comparison give

\[
 D_Xk_X=\operatorname{or}_{X,k}[n],\qquad
 R\Gamma(X;D_Xk_X)
    \simeq R\operatorname{Hom}_k(R\Gamma(X;k_X),k).
 \qquad\text{(3)}
\]

The second map is the transpose of the evaluation pairing followed by the point trace: \(R\Gamma(X;D_Xk_X)\otimes_k^L R\Gamma_c(X;k_X)\to R\Gamma_c(X;\omega_{X,k})\to k\). Dual-sections adjunction identifies its transpose with the displayed isomorphism. Compactness makes \(R\Gamma_c(X;k_X)=R\Gamma(X;k_X)\). The compact finiteness theorem applies both to the constant sheaf and to the rank-one orientation local system, so all these section complexes are perfect. The orientation line in (3) is retained even when it has nontrivial sign monodromy; its reduction in characteristic two still has rank one.

Coefficient duality reverses the finite cohomology degrees without changing the Euler characteristic. A shift by \(n\) multiplies it by \((-1)^n\). Formula (2) gives the remaining equality:

\[
 \chi_k(X)
   =(-1)^n\chi(X;\operatorname{or}_{X,k})
   =(-1)^n\chi_k(X).
 \qquad\text{(4)}
\]

**Theorem.** A compact odd-dimensional manifold without boundary satisfies

\[
 \chi_k(X)=0\qquad\text{for every field }k.
 \qquad\text{(5)}
\]

**Proof.** For odd \(n\), equation (4) says \(2\chi_k(X)=0\) in \(\mathbb Z\), so \(\chi_k(X)=0\). The orientation local system was retained throughout. The calculation is valid also in characteristic two because the dimensions and their alternating sum are integers. \(\square\)

Equivalently, the compact constructible-function duality theorem gives
\(\int_XD_X1_X\,d\chi=\int_X1_X\,d\chi\), while
\(D_X1_X=(-1)^n1_X\). The finite-dimensional argument above explains why this is an integer equality over every field.

## Turn a vector field into an admissible section

Let \(v\) be a continuous vector field on the compact manifold \(X\), and choose a smooth positive definite metric \(g\). Lower its tangent index:

\[
 \sigma=g^\flat(v):X\longrightarrow T^*X,\qquad
 \sigma(x)(w)=g_x(v(x),w).
 \qquad\text{(6)}
\]

Here is an explicit existence argument for \(g\). Choose finitely many coordinate neighborhoods and smaller neighborhoods covering \(X\), with closures inside the larger charts. In each chart choose a nonnegative smooth bump supported in the larger neighborhood and positive on the smaller one. Divide these bumps by their everywhere-positive sum to obtain a finite smooth partition of unity. The weighted sum of the pulled-back Euclidean metrics is smooth and positive definite. Each weighted term extends by zero outside its chart. Thus no global analytic metric is needed.

Positive definiteness gives \(\sigma(x)=0\) exactly when \(v(x)=0\). The section is continuous, so its graph is closed in the Hausdorff cotangent bundle, and \(\sigma\) is a proper closed embedding onto that graph. These facts suffice to define its exceptional counit and supported unit. For a smooth field one may compute that unit in smooth normal coordinates; no analyticity or isotropy of the graph is required.

Let \(0_X\subset T^*X\) denote the zero section. Write \(\lambda_0\) for its positive integral fibre Thom class, viewed as a cycle with the relative cotangent orientation coefficient. In base coordinates \(x\) and cotangent coordinates \(\xi\), its coefficient is

\[
 (-1)^n\operatorname{sgn}(dx_1\wedge\cdots\wedge dx_n)
   \otimes
 \operatorname{sgn}(d\xi_1\wedge\cdots\wedge d\xi_n).
 \qquad\text{(7)}
\]

The normal-first ambient orientation is \(\Omega=d\xi_1\wedge\cdots\wedge d\xi_n\wedge dx_1\wedge\cdots\wedge dx_n\). A positive normal Thom generator in the fibre variables \(\xi\), with base orientation coefficient \(\operatorname{sgn}(dx)\), corresponds to (7). The ordered comparison with cycle coefficients moves the shifted inverse fibre line past the base dualizing line. The inverse fibre generator has degree \(n\), while the base dualizing generator has degree \(-n\); their graded exchange contributes \((-1)^{n^2}=(-1)^n\); this factor must remain in (7). Under a base-coordinate change with Jacobian \(J\), the fibre frame changes by \(J^{-t}\). Their orientation signs therefore change together, and (7) glues without orienting \(X\).

The graph-normalized conormal has a different convention: \([T_X^*X]=(-1)^n\lambda_0\). Its tangent zero-section factor comes from the graph inverse coefficient and is \((-1)^n\) times the positive fibre Thom unit. The constant-sheaf coefficient theorem contributes the same factor, so \(\operatorname{CC}(\mathbb Q_X)=(-1)^n[T_X^*X]_{\mathbb Q}=(\lambda_0)_{\mathbb Q}\). Thus \(\lambda_0=(-1)^n[T_X^*X]\) is the integral class used below. In odd dimension it must not be identified with the graph-normalized conormal itself.

For integral coefficients put \(M=T^*X\) and \(\pi:M\to X\). The actual section unit and the ordered cup have types

\[
 \begin{aligned}
 {[\sigma]}&\in H^0_{\sigma(X)}(M;\pi^!\mathbb Z_X),\\
 \lambda_0&\in H^0_{0_X}(M;\pi^{-1}\omega_{X,\mathbb Z}),\\
 [\sigma]\cap\lambda_0
   &\in H^0_{\sigma(X)\cap0_X}(M;\omega_{M,\mathbb Z}).
 \end{aligned}
 \qquad\text{(8)}
\]

Put \(G=\sigma(X)\), \(P=\pi^!\mathbb Z_X\) and \(E=\pi^{-1}\omega_{X,\mathbb Z}\). The section unit is the morphism \(\mathbb Z_G=\sigma_*\mathbb Z_X\to\sigma_*\sigma^!P\to P\), using the inverse of exceptional composition \(\sigma^!P\simeq\mathbb Z_X\), then the closed-embedding counit. The second input is the Thom morphism \(\lambda_0:\mathbb Z_{0_X}\to E\). Since the two closed constant sheaves tensor to \(\mathbb Z_{G\cap0_X}\), their supported cup is their ordered tensor followed by \(P\otimes^LE\to\pi^!\omega_{X,\mathbb Z}\simeq\omega_{M,\mathbb Z}\). This gives exactly the supports and types in (8).

The coefficient order is the section first and the zero-section cycle second. The complete supported comparison says more than equality after forgetting support: its proper trace along \(\pi:G\cap0_X\to Z(v)\) is the morphism obtained by ordinary pullback \(\sigma^{-1}\lambda_0:\mathbb Z_{Z(v)}\to\omega_{X,\mathbb Z}\). Indeed transposing the cup along \(\sigma\) cancels its exceptional unit and counit; subsequent \(\pi\)-trace is the composite counit for \(\pi\sigma=1_X\). No factor is interchanged. Projection is a homeomorphism on this intersection, so the trace is proper there even in a noncompact local calculation. This is the map underlying the Thom pullback in (16).

## Isolated zeros carry integer local numbers

Assume first that the zero set \(Z(v)\) is finite. For each zero \(a\), choose a neighborhood in \(T^*X\) meeting \(G\cap0_X\) only at \((a,0)\). The restricted class of (8) then has compact point support. Its point trace, with \(i_{(a,0)}^!\omega_{M,\mathbb Z}=\mathbb Z\), defines

\[
 \operatorname{ind}_a(v)
   =\#([\sigma]\cap\lambda_0)_{(a,0)}
   \in\mathbb Z.
 \qquad\text{(9)}
\]

For a smaller such neighborhood, the restricted point-supported class is the same under support excision, and open extension followed by trace is the trace on the smaller neighborhood. This is exceptional composition for the open inclusion and the map to a point. Two choices have a common smaller neighborhood, so the number is independent of that choice. The same definition makes sense at any isolated zero on a noncompact manifold. Its independence of the positive metric is proved below by the actual relative-pair homotopy. On compact \(X\), if every zero is isolated, the zero set is closed and compact and therefore finite.

**Theorem.** For every continuous vector field on a compact \(X\) with finitely many isolated zeros,

\[
 \chi_k(X)=\sum_{a\in Z(v)}\operatorname{ind}_a(v)
             \qquad\text{for every field }k.
 \qquad\text{(10)}
\]

**Proof.** Put \(K=G\cap0_X=\{(a,0):a\in Z(v)\}\). Closed support at this finite set decomposes into the direct sum of its point supports. Restrict to disjoint small neighborhoods and use support excision. The supported-to-compact map and composition of open-extension traces then identify the trace of the class in (8) with the sum of its integral local numbers.

Extend these local Thom and orientation generators from \(\mathbb Z\) to \(\mathbb Q\). The relative orientation line is locally free over \(\mathbb Z\); the coefficient map preserves its square pairing, the ordered cup, and the point generator sent to \(1\) by trace. Thus the rational number of each point-supported class is exactly the image of its integer number. Only these finite supports and the normalized Thom maps are being compared, so no commutation of scalar extension with an unrestricted nonproper ordinary pushforward is needed.

The rational cycle \((\lambda_0)_{\mathbb Q}\) is \(\operatorname{CC}(\mathbb Q_X)\), as proved after (7). For this constructible sheaf the microsupport is \(0_X\), its closed support is the compact manifold \(X\), and the section \(\sigma\) is continuous. The compact continuous-section theorem therefore applies to the same ordered cup. In terms of its actual maps, proper trace from \(K\), followed by enlargement from \(Z(v)\) to \(X\), is the base characteristic class \(C(\mathbb Q_X)\); the point trace of that class is \(\chi_{\mathbb Q}(X)\). Composition of those traces identifies the rational total with the image of the finite sum above.

Both the sum and \(\chi_{\mathbb Q}(X)\) are integers. Injectivity of \(\mathbb Z\to\mathbb Q\) proves their equality in \(\mathbb Z\). The finite-cell argument (2), applied to the constant rank-one sheaf, gives \(\chi_k(X)=\chi_{\mathbb Q}(X)\) for every field \(k\). This proves (10), including characteristic two and nonorientable \(X\). \(\square\)

An empty zero set is permitted. Its supported class and its finite sum are zero, so a nowhere-zero field forces \(\chi_k(X)=0\).

## The local determinant has no extra orientation sign

Suppose that \(v\) is continuously differentiable near a zero \(a\) and \(A=Dv(a)\) is invertible. Choose a coordinate chart centered at \(a\). Then \(v(x)=Ax+o(|x|)\); for an analytic field the stronger remainder \(O(|x|^2)\) is available. A smooth positive metric makes \(\sigma\) continuously differentiable there.

The graph unit can be computed directly as a supported Thom class. The coordinate change \((x,\xi)\mapsto(x,\eta)\), where \(\eta=\xi-\sigma(x)\), is a fibre translation with inverse \((x,\eta)\mapsto(x,\eta+\sigma(x))\). It preserves the relative fibre orientation and sends the graph to \(\eta=0\). In the continuously differentiable case its normal-first orientation satisfies

\[
 d\eta_1\wedge\cdots\wedge d\eta_n\wedge dx
     =d\xi_1\wedge\cdots\wedge d\xi_n\wedge dx
     =\Omega.
 \qquad\text{(11)}
\]

Every other wedge term has an additional base differential and vanishes. Use the positive dual-frame identification of the relative and base orientation lines to put both inputs in the same cycle coordinates. The ordered coefficient comparison then gives the supported graph Thom unit its base tangent orientation tensored with the fibre orientation, multiplied by \((-1)^n\). The positive Thom class \(\lambda_0\) has the same scalar in (7). This is a normal-coordinate computation of the classes in (8); it does not require placing a nonanalytic graph in the subanalytic cycle sheaf. Neither symmetry of \(D\sigma\) nor a Lagrangian graph is used.

Let \(G=g(a)\) be the positive definite metric matrix and \(B=D\sigma(a)\). Differentiating \(g(x)v(x)\) gives \(B=GA\), since the term involving \(Dg\) is multiplied by \(v(a)=0\). In row order \((\xi,x)\), the tangent columns for the graph followed by the zero section give

\[
 B=GA,\qquad
 [\,V_{\mathrm{graph}}\ V_{\mathrm{zero}}\,]
      =\begin{pmatrix}B&0\\ I&I\end{pmatrix},
 \qquad
 \det\begin{pmatrix}B&0\\ I&I\end{pmatrix}=\det B.
 \qquad\text{(12)}
\]

The two submanifolds are transverse exactly when \(B\) is invertible. Their cycle weights are both \((-1)^n\), so the weights multiply to one; the integral fibre sign generators also have square one. The ordered transverse formula with
\(\Omega=d\xi\wedge dx\) consequently gives

\[
 \operatorname{ind}_a(v)
    =\operatorname{sgn}\det B
    =\operatorname{sgn}\det A,
 \qquad\text{(13)}
\]

because a positive definite \(G\) has positive determinant. The first input is the graph and the second is the positive Thom class \(\lambda_0\), not the differently signed graph-normalized conormal. Exchanging the two inputs would contribute \((-1)^n\); replacing \(\Omega\) by the symplectic orientation requires the corresponding ambient orientation comparison.

There is also a direct local-cohomology check that includes the continuously differentiable case. Write the fibre-coordinate map of \(\sigma\) as \(h(x)=Bx+r(x)\), with \(r(x)=o(|x|)\). Choose a sufficiently small ball so that \(|r(x)|\leq\tfrac12\|B^{-1}\|^{-1}|x|\). Each map \(h_t(x)=Bx+t r(x)\), for \(0\leq t\leq1\), is then nonzero away from zero, by the reverse triangle inequality. These are maps of the same relative pair into \((\mathbb R^n,\mathbb R^n\setminus\{0\})\), so they induce the same pullback of the positive fibre Thom generator. The linear map \(B\) acts on that generator by \(\operatorname{sgn}\det B\): positive-determinant linear maps deform through invertible maps to the identity, and a coordinate reflection sends the ordered one-dimensional difference generator to its negative. The paired base orientation and point trace therefore give exactly (13).

The formula also verifies coordinate independence directly. For a coordinate change with Jacobian \(J\) at the zero,

\[
 A'=JAJ^{-1},\qquad
 B'=J^{-t}BJ^{-1}.
 \qquad\text{(14)}
\]

The derivative of \(J\) contributes nothing because \(v(a)=0\), and the base derivative of the cotangent transition contributes nothing because \(\sigma(a)=0\). Thus \(\det A'=\det A\), and \(\det B'=(\det J)^{-2}\det B\). Both signs are unchanged, including for a reversed chart. This agrees with the two simultaneous orientation changes in (7).

**Hopf index theorem.** If every zero of \(v\) is nondegenerate, then

\[
 \chi_k(X)=\sum_{a\in Z(v)}\operatorname{sgn}\det Dv(a).
 \qquad\text{(15)}
\]

Every nondegenerate zero is isolated by the inverse function theorem. The closed zero set on compact \(X\) is therefore finite, so (10) and (13) give (15). This includes smooth and analytic fields and is an equality of integers over every coefficient field. For a zero-dimensional compact manifold, the empty determinant is one; every point is a zero and contributes one.

## A degenerate zero is read by its Thom pullback

The definition (9) remains valid when the derivative is singular or the field is only continuous. Its computation uses the positive fibre Thom class \(\lambda_0\) fixed in (7). On a coordinate neighborhood \(U\) containing exactly one zero \(a\), ordinary pullback of its coefficient \(E=\pi^{-1}\omega_{U,\mathbb Z}\) along the section is \(\omega_{U,\mathbb Z}\), and the inverse image of its support \(0_U\) is \(\{a\}\). The supported comparison proved after (8) identifies the local cup number with

\[
 \sigma^*:H^n_{0_U}(T^*U;\pi^{-1}\operatorname{or}_{U,\mathbb Z})
       \longrightarrow H^n_{\{a\}}(U;\operatorname{or}_{U,\mathbb Z})
       \simeq\mathbb Z.
 \qquad\text{(16)}
\]

The class in the first group is the positive fibre Thom unit, not the graph-normalized conormal with its additional \((-1)^n\). Trivialize \(T^*U\) by the coordinate covectors. The class is the pullback of the positive generator of \(H^n_{\{0\}}(\mathbb R^n_\xi;\mathbb Z)\), tensored with the local base orientation. If \(h:U\to\mathbb R^n_\xi\) is the fibre-coordinate function of the section, (16) is precisely its map of pairs \((U,U\setminus\{a\})\to(\mathbb R^n,\mathbb R^n\setminus\{0\})\) on this generator. The last isomorphism in (16) pairs the local support orientation with \(\operatorname{or}_{U,\mathbb Z}\); it is the canonical point trace of \(\omega_{U,\mathbb Z}=\operatorname{or}_{U,\mathbb Z}[n]\). Thus it reads the integer local degree with both orientation factors retained.

In dimension one, the local relative group is explicitly

\[
 H^1(I,I\setminus\{0\};\mathbb Z)
       =\mathbb Z^2/\mathbb Z(1,1).
 \qquad\text{(17)}
\]

The two coordinates refer to the left and right punctured intervals. The quotient is identified with \(\mathbb Z\) by \([(c_-,c_+)]\mapsto c_+-c_-\), using the increasing-coordinate Thom convention. Take a small target fibre interval containing the image of a sufficiently small base interval. If the fibre-coordinate function \(h\) is positive on both punctured base intervals, pullback of a locally constant pair on the punctured target sends \((c_-,c_+)\) to \((c_+,c_+)\). The localization long exact sequences are natural for this map of pairs, so its induced map on (17) is zero. Consequently such an isolated zero has index zero, regardless of its derivative.

Finally let \(g_0,g_1\) be two positive metrics. Their convex interpolation \(g_t=(1-t)g_0+t g_1\) is positive definite, and \(\sigma_t=g_t^\flat(v)\) has exactly the same zero set for every \(t\). In an isolating chart, the homotopy \((t,x)\mapsto\sigma_t(x)\) is therefore a homotopy of the relative pair maps in (16). Its projection to \(U\) is always \(x\), so the pulled-back orientation coefficient is the same base orientation line throughout. After trivializing that line in the chart, the relative singular-cochain prism homotopy shows equality of the two induced pullbacks; it preserves the punctured subspace because no new zero is introduced. Equivalently one may use the proper-interval homotopy comparison on the corresponding support-localization triangles. Thus the point trace, and hence the local integer, is independent of the metric. The same argument applies to continuous \(v\); differentiability was used only for the determinant formula.

## Exercises with complete solutions

### Monodromy changes cohomology without changing Euler characteristic
*Difficulty: Introductory.*

Let \(L\) be a rank-\(r\) local system on \(S^1\), with invertible monodromy matrix \(T\) over any field. Compute its Euler characteristic without assuming that \(T=I\).

**Solution.** Cutting at one vertex gives the two-term cochain complex
\(k^r\xrightarrow{T-I}k^r\), in degrees zero and one. Thus
\(H^0=\ker(T-I)\) and \(H^1=\operatorname{coker}(T-I)\). Rank-nullity gives equal dimensions for these two spaces, and their alternating sum is zero. If \(T-I\) is invertible, both vanish; if \(T=I\), both have dimension \(r\). Both cases have the same Euler characteristic, agreeing with \(r\chi(S^1)=0\).

### Characteristic two on a nonorientable three-manifold
*Difficulty: Intermediate.*

Let \(X=S^1\times\mathbb{RP}^2\). Over a field of characteristic two, use the usual one-cell-per-dimension cell structure on \(\mathbb{RP}^2\) to compute the cohomology dimensions of \(X\). Explain why the odd-dimensional vanishing is still an integer assertion.

**Solution.** The cellular differential on \(\mathbb{RP}^2\) has the integer boundary multiplication by two in the top cell and zero in the other positive degree. Over a characteristic-two field both differentials vanish, so the dimensions in degrees zero, one and two are \(1,1,1\). The circle has one-dimensional cohomology in degrees zero and one. Finite Künneth gives dimensions
\(1,2,2,1\) on \(X\), and Euler characteristic
\(1-2+2-1=0\) in \(\mathbb Z\).
The product is nonorientable: the circle's orientation line is trivial, while that of \(\mathbb{RP}^2\) is nontrivial integrally. Its sign representation becomes trivial in characteristic two. Neither change affects its rank-one Euler formula. A scalar equation \(2z=0\) in this field alone would give no vanishing conclusion; (4) is instead an equality of integer alternating dimensions.

### A rotating field has a positive index
*Difficulty: Intermediate.*

Near the origin of \(\mathbb R^2\), take
\(v(x,y)=(-y,x)\) and the Euclidean metric. Compute its local index and check whether the associated one-form is a differential.

**Solution.** The linearization is
\(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), with determinant one, so (13) gives index \(+1\). The lowered one-form is
\(-y\,dx+x\,dy\), whose exterior derivative is
\(2\,dx\wedge dy\), not zero. It is therefore not locally a differential. The graph need not be Lagrangian, yet its supported section unit and ordered intersection are valid. Restricting the Hopf proof to gradient fields would miss this example.

### A chart reversal and a positive metric
*Difficulty: Intermediate.*

At a planar saddle take
\(A=\operatorname{diag}(-1,1)\), metric matrix
\(G=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), and coordinate reversal
\(J=\operatorname{diag}(-1,1)\). Compute the signs before and after the reversal.

**Solution.** The metric is positive definite: its eigenvalues are one and three. Its determinant is three. Hence
\(B=GA=\begin{pmatrix}-2&1\\-1&2\end{pmatrix}\) has determinant \(-3\), and the index is \(-1\).
The new tangent matrix is \(A'=JAJ^{-1}=A\). The new cotangent derivative is
\(B'=J^{-t}BJ^{-1}=\begin{pmatrix}-2&-1\\1&2\end{pmatrix}\), again with determinant \(-3\). The base and fibre orientation generators both reverse; their tensor coefficient is unchanged. A local maximum with \(A=-I\) in this same two-dimensional setting would instead have determinant \(+1\) and index \(+1\).

### The two zeros of a height gradient
*Difficulty: Intermediate.*

On the unit sphere \(S^2\subset\mathbb R^3\), take the round-metric gradient of the height function \(h(p)=p_3\). Find its zeros and local indices.

**Solution.** The tangent gradient is
\(v(p)=e_3-p_3p\). Its only zeros are the north and south poles. For a tangent displacement \(w\) at either pole, \(dp_3(w)=0\), so
\(Dv(w)=-p_3w\). At the north pole the matrix on the two-dimensional tangent plane is \(-I\); at the south pole it is \(I\). Both determinants are positive, so the sum of local indices is two. The sphere's zero- and two-dimensional cell structure gives \(\chi(S^2)=2\), as required. Reversing the vector field exchanges its maximum and minimum behavior but leaves both two-dimensional determinant signs positive.

### Three projective critical points on a nonorientable surface
*Difficulty: Advanced.*

For real numbers \(a_1<a_2<a_3\), let
\(h([x])=(a_1x_1^2+a_2x_2^2+a_3x_3^2)/(x_1^2+x_2^2+x_3^2)\)
on \(\mathbb{RP}^2\). Using its descended round metric, compute the indices of its gradient.

**Solution.** On the unit sphere the gradient is
\(2(\operatorname{diag}(a_1,a_2,a_3)x-h(x)x)\). It is antipodally equivariant and descends to the projective surface. Since the eigenvalues are distinct, its zeros are exactly the three coordinate axes. In an affine projective chart near the \(i\)-th axis, the Hessian at that critical point has diagonal entries
\(2(a_j-a_i)\) for \(j\ne i\). Lowering or raising indices by the positive metric preserves the determinant sign. The three signs are respectively \(+1,-1,+1\). Their sum is one, equal to the cell Euler characteristic \(1-1+1\) of \(\mathbb{RP}^2\). No orientation of this nonorientable surface was used to assign the local integers.

### A nowhere-zero field and a boundary counterexample
*Difficulty: Intermediate.*

Compare the constant nonzero field on the flat two-torus with the field \(\partial_t\) on the closed interval \([0,1]\). Explain which Euler conclusion the theorem permits.

**Solution.** The torus has no vector-field zeros, so (10) gives Euler characteristic zero. Its cell counts \(1,2,1\) confirm this. On the interval the constant field also has no zeros, but the interval is contractible and has Euler characteristic one. It has boundary and is outside the theorem's hypotheses. Thus the interval is not a counterexample to (10); it shows why a theorem allowing boundary would need boundary data and contributions. No such extension is being assumed here.

### A degenerate circle zero has index zero
*Difficulty: Advanced.*

On \(S^1\), in the standard periodic coordinate, take
\(v(t)=(1-\cos t)\partial_t\). Compute the local index of its unique zero and compare with the Euler characteristic.

**Solution.** The only zero is \(t=0\) modulo \(2\pi\). Its derivative vanishes, so the determinant formula for nondegenerate zeros does not apply. In a small punctured interval on both sides of zero the coefficient \(1-\cos t\) is positive. For the flat metric the lowered section has the same positive coefficient. Its Thom pullback in (17) sends every pair to a diagonal pair, so the local index is zero. The general isolated-zero formula (10) therefore gives \(\chi(S^1)=0\). This agrees with its two-term cellular calculation. A zero derivative alone would not determine this local index; the signs on the two punctured sides do.

## References

M. Kashiwara, [Index theorem for constructible sheaves](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), Theorem 4.2, p. 199, gives the sheaf Euler index as an intersection with a differential graph, assuming compact closed sublevels on the coefficient support and compact intersection with the microsupport. The local quadratic calculation is Proposition 5.1 and Lemma 5.2, pp. 200–201; the general argument proceeds through generic perturbation and homotopy in §7. For compact constant coefficients the theorem gives the zero-section index. The linked programme lessons supply the continuous-section comparison, the integral local traces and the determinant calculation used here to obtain the vector-field formula, including on nonorientable manifolds.
