# Complex nearby cycles as normal and conormal sections

A complex normal line has two useful sections. A normal vector on which the defining function has derivative one computes nearby cycles. The conormal covector given by that derivative computes vanishing cycles. The second assertion depends on the Fourier convention and on including the endpoint of a closed ray. We prove both comparisons, then deduce constructibility and the support bound for an arbitrary holomorphic function.

Let \(k\) be a commutative ring of finite global dimension. Manifolds are complex analytic, Hausdorff and countable at infinity, with uniform finite dimension bounds. An object of \(D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) has locally constant cohomology on a locally finite complex analytic stratification. Its coefficient modules may be infinite. The perfect constructible subcategory additionally requires perfect stalk complexes. No Noetherian hypothesis is imposed on \(k\).

We retain the cycle normalization from [Nearby cycles and the two monodromy triangles](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#one-two-term-complex-gives-two-triangles):

\[
\phi_f(F)=\operatorname{Cone}\bigl(i^{-1}F\longrightarrow\psi_f(F)\bigr)[-1].
\tag{1}
\]

Thus the vanishing object here already contains the source's shift by \(-1\). The real covector associated to a complex covector is its real part. On a normal complex line the pairing is \(\operatorname{Re}(v\xi)\), without a conjugate. The Fourier transform uses the closed kernel \(\operatorname{Re}(v\xi)\leq0\).

The normal-deformation comparison for weak real constructibility is proved in [Nearby cycles through the normal deformation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-through-the-normal-deformation.md#recovering-nearby-cycles-from-the-punctured-normal-bundle). Here the additional complex geometry is essential. The proof uses the bounded specialization estimate, Fourier test and whole-complex descent theorems in the precise forms stated below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Complex constructibility survives specialization

Let \(Y\subset X\) be a closed complex submanifold. Put \(E=T_YX\), \(L=T_Y^*X\subset T^*X\), and \(\Lambda=\operatorname{SS}(F)\). The complex constructibility criterion proved in [Complex microlocal stratifications and constructibility](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests) makes \(\Lambda\) closed complex analytic, complex-conic and real-isotropic.

The [bounded specialization estimate SH02-CHE-001](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/characteristic-estimates.md#sh02-che-001--what-specialization-can-contribute) gives

\[
\operatorname{SS}(\nu_YF)\subset C_L(\Lambda),
\tag{2}
\]

under the canonical normal/cotangent identification. In adapted holomorphic coordinates \((u,y)\), with \(Y=\{u=0\}\), write \((\alpha,\beta)\) for their complex covectors. The coordinates and signs of that identification are

\[
(v,y;\alpha,\beta)\in T^*E
\longleftrightarrow(\alpha,y;-v,\beta)\in T^*L
\longleftrightarrow
\bigl((0,y;\alpha,0);v,\beta\bigr)\in N_L(T^*X).
\tag{3}
\]

Each map is holomorphic. The second map uses the [symplectic normal identification](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/boundary-forms-and-lagrangian-normal-cones.md#the-cotangent-identification-and-its-sign) \(K([w])(a)=\operatorname{Re}\Omega(w,a)\); its inverse is induced by \(-H\) with the Hamiltonian convention used earlier. The first is the Fourier cotangent map. These signs agree with the selected specialization contract.

The [analytic normal-cone argument](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/analytic-normal-cones-through-complex-deformation.md#reparameterizing-an-arc-to-make-the-scale-positive-real), in its [adapted-submanifold form](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#why-the-full-limiting-conormal-sum-is-analytic), applies to the analytic set \(\Lambda\) and the analytic submanifold \(L\). Its accessible central fibre is analytic and invariant under complex normal scaling. The [Lagrangian normal-cone theorem proved in Boundary forms and Lagrangian normal cones](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/boundary-forms-and-lagrangian-normal-cones.md#the-full-lagrangian-normal-cone-theorem) makes its image in \(T^*L\) real-isotropic. The holomorphic symplectic Fourier identification in (3) preserves this property on \(T^*E\).

We must also check cotangent conicity in \(T^*E\), since normal scaling alone is a different action. A normal-cone sequence in these coordinates has

\[
(t_jv_j,y_j;\alpha_j,t_j\beta_j)\in\Lambda,
\qquad t_j>0,\quad t_j\to0,
\tag{4}
\]

with all four displayed limiting coordinates finite. Multiplying the input covector by any fixed \(\lambda\in\mathbb C^*\) gives the same witnesses with \(\alpha_j,\beta_j\) replaced by \(\lambda\alpha_j,\lambda\beta_j\). Under (3) this is exactly complex dilation of the output cotangent covector at the unchanged base \((v,y)\). Therefore the bound in (2) is closed complex analytic, complex-conic and real-isotropic. The same constructibility criterion, applied to this bound, proves

\[
\nu_YF\in D^b_{w\text{-}\mathbb C\text{-}c}(k_E),
\qquad
\mu_YF=(\nu_YF)^\wedge\in
D^b_{w\text{-}\mathbb C\text{-}c}(k_{E^\vee}).
\tag{5}
\]

For the second assertion use the [complex Fourier theorem proved in Holomorphic operations and complex Fourier symmetries](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#holomorphic-fourier-exchange-and-its-cotangent-conicity). Both objects are bounded and positively conic along their bundle fibres. The [uniform boundedness](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#the-geometric-and-boundedness-contracts) and [positive conicity](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-conic--directions-and-support) are part of the specialization/Fourier contracts, rather than consequences of finite-dimensional coefficient modules.

For perfect constructible \(F\), [Perfect operations and finite microlocal coefficients](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#specialization-and-microlocal-hom) proves perfect stalks for both \(\nu_YF\) and \(\mu_YF\). That proof keeps the real deformation chamber and treats it using weak real constructibility and perfect internal Hom. We have not treated a positive real chamber as a holomorphic open subset. Combining the real perfection theorem with (5) proves both perfect complex constructibility statements.

## Fibre constancy after lifting the punctured normal line

For now suppose \(Y=f^{-1}(0)\) is a regular analytic fibre: \(df_y\ne0\) for every \(y\in Y\). Its normal line is canonically identified with \(\mathbb C_v\times Y\) by

\[
\ell_y([a])=df_y(a),\qquad
s(y)=\ell_y^{-1}(1),\qquad
s'(y)=df_y\in T_Y^*X.
\tag{6}
\]

In the dual coordinate \(\xi\), \(s'\) is the section \(\xi=1\). Let \(G=\nu_YF\), and let \(e:Y\hookrightarrow E\) be the zero section. A reduced smooth zero set for a ramified defining function does not suffice for (6); \(z^m\), \(m>1\), has zero derivative at its reduced zero set.

On \(E\setminus e(Y)\), the cohomology of \(G\) is locally constant on every \(\mathbb C^*\) fibre. Here is the relevant microsupport check. Positive conicity annihilates the real radial vector field. The [full complex Euler calculation in the preceding Fourier lesson](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#the-two-complex-fourier-actions), using the complex-conic actual microsupport, annihilates the imaginary radial vector field as well. In local coordinates a vertical covector \(\alpha\) consequently satisfies

\[
\operatorname{Re}(v\alpha)=0,
\qquad \operatorname{Im}(v\alpha)=0.
\tag{7}
\]

When \(v\ne0\), it has \(\alpha=0\). The [submersion descent criterion for microsupport](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-submersion--exact-pullback-and-local-descent) therefore makes \(G\) locally a whole derived pullback in these fibre coordinates, and in particular makes its cohomology locally constant on each punctured fibre. The same reasoning applies to \(\mu_YF\) away from its dual zero section, by (5).

Use the cover

\[
p:\mathbb C_w\times Y\longrightarrow\mathbb C_v^*\times Y,
\qquad p(w,y)=(e^{2\pi iw},y),
\qquad q(w,y)=y.
\tag{8}
\]

The pullback \(p^{-1}(G|_{v\ne0})\) has locally constant cohomology on the contractible \(\mathbb C_w\) fibres. The [whole-complex cylinder descent theorem (SH02-CON-CYLINDER)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) identifies its derived direct image with evaluation at \(w=0\), through the actual evaluation morphism. It applies twice, to the two real coordinates of \(w\), and retains the full extension data and arbitrary coefficient modules. Thus

\[
Rq_*p^{-1}(G|_{v\ne0})\simeq s^{-1}G.
\tag{9}
\]

This contract proves descent on a product with \(\mathbb R\) using closed-strip exhaustions and their evaluation maps. Iteration on \(\mathbb R^2\) is legitimate. It does not assert unrestricted nonproper base change or descent from a punctured fibre with nontrivial fundamental group.

[Ordinary positive-conic contraction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-radial-star--ordinary-contraction-to-the-zero-section) identifies the left side of (9) with \(\psi_\ell(G)\). Explicitly, the cover direct image in the nearby definition has a lifted positive action: multiplying \(v\) by \(r>0\) translates \(w\) by \(\log r/(2\pi i)\). Contracting its ordinary direct image to the zero section and composing the two direct images gives \(Rq_*\) in (9). The normal comparison already proved therefore yields

\[
\psi_f(F)\simeq\psi_\ell(G)\simeq s^{-1}\nu_YF.
\tag{10}
\]

Fixing \(w=0\) fixes the lift of the normal section. Deck translation \(w\mapsto w+1\) remains visible through the [coefficient action and its induced nearby monodromy](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#deck-action-and-its-exact-sequence). Fibrewise local constancy on \(\mathbb C^*\) does not force this automorphism to be the identity.

## A dual halfspace has a closed-ray polar

Let \(\tau:E\to Y\) and \(\tau^\vee:E^\vee\to Y\) be the bundle projections. Set

\[
U=\{\xi\in\mathbb C:\operatorname{Re}\xi>0\},
\qquad R=\{v\in\mathbb C:\operatorname{Im}v=0,
\ \operatorname{Re}v\geq0\}.
\tag{11}
\]

The cohomology of \(\mu_YF\) is locally constant along the \(U\) fibres. A smooth product identification \(U\simeq\mathbb R^2\), chosen to take \(1\) to the origin, and the whole-complex cylinder descent give

\[
s'^{-1}\mu_YF\simeq
R\tau^\vee_*R\mathcal Hom(k_{U\times Y},\mu_YF).
\tag{12}
\]

The internal Hom for this open coefficient means ordinary sections over the open halfspace, pushed into the ambient bundle. It does not mean compactly supported cohomology.

In the real pairing \(\operatorname{Re}(v\xi)\), the positive polar of \(U\) is \(R\). Indeed, write \(v=u+iw\) and \(\xi=a+ib\). Then

\[
\operatorname{Re}(v\xi)=ua-wb,
\qquad a>0,\quad b\in\mathbb R.
\tag{13}
\]

Nonnegativity for every such \(a,b\) forces \(w=0\) and \(u\geq0\), and these conditions suffice. The zero vector passes every inequality and must be included.

The [open-convex-cone test SH02-FS-SECTIONS, formula FS13](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/fourier-sato.md#sh02-fs-sections--testing-a-transform-on-regions), now gives

\[
R\tau^\vee_*R\mathcal Hom(k_{U\times Y},G^\wedge)
\simeq R\tau_*R\mathcal Hom(k_{R\times Y},G).
\tag{14}
\]

To obtain an isomorphism of sheaves on \(Y\), apply the natural Fourier test to the restriction over every open base subset and its restriction maps. Its proof applies the inverse Fourier equivalence to both Hom arguments; the inverse image of the open-cone coefficient is its closed-polar coefficient. The inverse Fourier shifts and dual orientation lines cancel in this test. The real rank of the complex line remains two; (14) introduces no further shift or orientation factor.

## The slit and the cover have the same section complex

Let \(O=\mathbb C\setminus R\). This slit plane is contained in \(\mathbb C^*\), and its inverse image has the distinguished open strip

\[
S=\{w\in\mathbb C:0<\operatorname{Re}w<1\}.
\tag{15}
\]

The restriction \(p|_S:S\to O\) is a homeomorphism. Write \(E^*=\mathbb C^*\times Y\) and \(j:E^*\hookrightarrow E\); the cover \(p\) has target \(E^*\). Extension by zero from \(S\) to the cover, proper-support direct image along \(p\), and then \(j_!\) give a coefficient morphism on \(E\)

\[
\alpha:k_{O\times Y}\longrightarrow
L=j_!p_!k_{\mathbb C_w\times Y},
\qquad
\operatorname{tr}\circ\alpha:
k_{O\times Y}\longrightarrow k_E.
\tag{16}
\]

The [trace](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#the-coefficient-sheaf-uses-a-sum) is the composite of the punctured-target counit, extended by \(j_!\), with the open-inclusion counit \(j_!k_{E^*}\to k_E\). On \(E^*\) it sums finitely supported sheet coefficients. Consequently \(\operatorname{tr}\circ\alpha\) is the ordinary open-extension inclusion. Both two-term complexes below are objects on \(E\), with terms in degrees \(-1,0\):

\[
B=[k_{O\times Y}\longrightarrow k_E],
\qquad K=[L\xrightarrow{\operatorname{tr}}k_E],
\qquad B\longrightarrow K=(\alpha,\mathrm{id}).
\tag{17}
\]

Open–closed localization identifies \(B\simeq k_{R\times Y}\), in degree zero. Applying contravariant internal Hom to (17) gives

\[
R\tau_*R\mathcal Hom(K,G)
\longrightarrow R\tau_*R\mathcal Hom(k_{R\times Y},G).
\tag{18}
\]

The left side equals \(\phi_\ell(G)\). This follows from the [two-term coefficient definition in the monodromy lesson](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#one-two-term-complex-gives-two-triangles) and ordinary positive-conic contraction to \(e\). The coefficient \(K\), the target \(G\), and their internal Hom have the needed [positive conicity](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-functors--transport-through-sheaf-operations); the lifted positive action preserves \(S\), so it also preserves the coefficient map in (17).

We show that (18) is an isomorphism by comparing the Hom triangles of the two complexes in (17). Their \(k_E\) terms have the identity map. On the other terms, ordinary composition and the cover adjunction identify the map with restriction

\[
Rq_*p^{-1}(G|_{v\ne0})
\longrightarrow
R(\tau|_{O\times Y})_*(G|_{O\times Y}).
\tag{19}
\]

It is restriction from the entire cover to \(S\). The whole cover and the open strip are each a product with a contractible real two-dimensional fibre. Their cohomology is vertically locally constant. Apply the cylinder descent contract, identifying \(S\) with \(\mathbb R^2\), and evaluate both sides at \(w=1/2\). The two evaluation maps commute with restriction. Both are isomorphisms, so (19) is an isomorphism.

The evaluation point lies above \(v=-1\), which belongs to \(O\). In contrast, \(v=1\) lies on the removed ray. Evaluation at \(w=0\) from (9) is related to evaluation at \(w=1/2\) by transport in the contractible cover, rather than by pretending that the normal section \(1\) lies in the slit. This distinction allows arbitrary monodromy on the punctured normal line.

The map between the two Hom triangles is now an isomorphism on both their other terms. Their fibre term (18) is an isomorphism too. Combining (12), (14), (18), and the [normal vanishing comparison](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-through-the-normal-deformation.md#the-ordinary-unit-and-the-vanishing-comparison) gives

\[
\phi_f(F)\simeq\phi_\ell(\nu_YF)
\simeq R\tau_*R\mathcal Hom(k_{R\times Y},\nu_YF)
\simeq s'^{-1}\mu_YF.
\tag{20}
\]

The coefficient map (17) fixes the slit branch used in this comparison. Formula (20) retains exactly the normalization (1). It does not append a further Fourier, real-rank or complex-orientation shift. Changing the lift is governed by deck transport; no trivialization of monodromy on the entire punctured line has been assumed.

## Constructibility and support for a critical function

For a regular fibre, (5), (10), and (20), followed by [holomorphic ordinary inverse image](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#full-characteristic-inverse-image-for-a-holomorphic-map) along \(s,s'\), prove weak complex constructibility of both cycles. If \(F\) has perfect stalks, both bundle objects have perfect stalks and ordinary inverse image retains them. This proves perfect complex constructibility as well.

Now allow any holomorphic \(f:X\to\mathbb C\). Its zero set \(Y\) can be singular. Use the closed graph and the coordinate projection

\[
g:X\hookrightarrow\mathbb C_t\times X,
\quad g(x)=(f(x),x),\qquad H=g_*F,
\quad Z=\{t=0\}\simeq X.
\tag{21}
\]

The graph is proper and holomorphic. The [proper holomorphic operation theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#proper-direct-image-uses-the-actual-support) makes \(H\) weakly, or perfectly, complex constructible as appropriate. The target coordinate \(t\) has a regular fibre \(Z\), so the results just proved apply to \(\psi_t(H)\) and \(\phi_t(H)\). With \(a:Y\hookrightarrow Z\) the closed inclusion, the actual proper-on-support comparisons from [Proper pushforwards of nearby and vanishing cycles](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/proper-pushforwards-of-nearby-and-vanishing-cycles.md#the-graph-construction-has-a-zero-extension-term) give

\[
\psi_t(H)\simeq a_*\psi_f(F),
\qquad \phi_t(H)\simeq a_*\phi_f(F).
\tag{22}
\]

These are objects supported on \(a(Y)\). Refine their analytic stratifications in \(Z\) compatibly with the analytic subset \(Y\). Their restrictions are locally constant on the resulting strata of \(Y\); ordinary stalk restriction retains the perfect condition. Thus both cycles are weakly complex constructible on \(Y\), and are perfect constructible when \(F\) is. This argument does not assign a smooth normal line to a singular fibre.

The [microlocal support theorem SH02-MO-MICROLOCAL-SUPPORT](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-microlocal-support--where-directional-sheaves-can-live) gives

\[
\operatorname{supp}(\mu_YF)
\subset T_Y^*X\cap\operatorname{SS}(F)
\tag{23}
\]

for a smooth \(Y\). Here and below support is the closed support of the cohomology sheaves. For a regular fibre, pulling (23) back along \(s'\) and using (20) gives the closed bound

\[
\operatorname{supp}(\phi_f(F))
\subset\{y\in f^{-1}(0):(y;df_y)\in\operatorname{SS}(F)\}.
\tag{24}
\]

For a critical function use (21)–(22). At \((0,x)\), the covector \(dt\) restricts to the graph as \(df_x\). More explicitly, graph transpose pullback sends \((c,\xi)\) to \(c\,df_x+\xi\). The [proper direct-image estimate SH02-MO-PROPER-PUSH, formula MO8](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-proper-push--collecting-tests-along-a-fibre), implies

\[
((0,x);dt)\in\operatorname{SS}(g_*F)
\ \Longrightarrow\ (x;df_x)\in\operatorname{SS}(F).
\tag{25}
\]

Apply the regular support bound to \(t,H\) and use (22). It gives (24) for arbitrary \(f\), including \(df_x=0\). Closedness matters: the preimage of the closed set \(\operatorname{SS}(F)\) under \(y\mapsto(y;df_y)\) is closed, so the assertion bounds closed support and not merely individual nonzero stalks.

Finally, if \(p\notin\operatorname{SS}(F)\), choose an open cotangent neighborhood \(V\) disjoint from microsupport. For every point \(x\) and every local holomorphic function \(h\) with \(h(x)=0\) and \((x;dh_x)\in V\), restriction of microsupport to the domain of \(h\) and (24) give

\[
\phi_h(F)_x=0.
\tag{26}
\]

This proves the uniform forward holomorphic test. [Quadratic cycles and the holomorphic microsupport test](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/quadratic-cycles-and-the-holomorphic-microsupport-test.md#the-uniform-holomorphic-criterion) proves the reverse implication using generic microlocal models, transfer of the test to those models, and the quadratic calculation.

## Exercises with complete solutions

### The endpoint and two Fourier calibrations

*Difficulty: Introductory.*

Compute the polar of \(U=\{\operatorname{Re}\xi>0\}\) using the pairing in (13). Over a field, check (20) for \(G=k_{\mathbb C}\) and \(G=k_{\{0\}}\), with \(f(v)=v\). Explain why the ray's endpoint changes the answer.

**Solution.** Allowing every real \(b\) forces \(w=0\), and then every \(a>0\) forces \(u\geq0\). Thus the polar is the closed ray \(R\), including zero. For \(k_{\mathbb C}\), nearby cycles are \(k\) and the central-to-nearby map is the identity, so \(\phi=0\). The Fourier transform is \(k_{\{0\}}[-2]\), with the canonical real rank-two orientation, and restriction at \(\xi=1\) is zero. For \(k_{\{0\}}\), the nearby object is zero and (1) gives \(\phi=k\); its Fourier transform is the constant \(k\) in degree zero, agreeing at \(1\). Equivalently, \(R\operatorname{Hom}(k_R,k_{\{0\}})=k\), since closed support at zero belongs to \(R\). Removing the endpoint makes that Hom zero: the coefficient then has zero stalk at zero and closed-embedding adjunction computes it there. The second calibration would fail.

### A slit cannot be evaluated at the removed normal section

*Difficulty: Intermediate.*

For (15), locate lifts of \(v=1\) and \(v=-1\). Prove directly that restriction from the cover to \(S\) induces an isomorphism of ordinary derived section complexes for a cohomologically locally constant complex on the cover. Describe the effect of choosing the strip \(m<\operatorname{Re}w<m+1\) instead.

**Solution.** The lifts of \(1\) are the integers, all on strip boundaries. The lift \(1/2\) of \(-1\) lies inside \(S\). The two cylinder descent evaluations at \(1/2\) are isomorphisms and commute with the restriction morphism, so that morphism is an isomorphism in the derived category, including higher extension data. For the other strip use \(m+1/2\). Let \(\rho_m\) be restriction to that strip, transported to the original strip by translation by \(-m\), and let \(M\) denote the nearby deck action. With the coefficient convention \(T(e_n)=e_{n-1}\), and nearby monodromy induced by precomposition with this action, these maps satisfy \(\rho_m M^m=\rho_0\), or \(\rho_m=\rho_0M^{-m}\). The result is independent up to this specified transport, without assuming trivial monodromy.

### Nontrivial puncture monodromy survives the section formula

*Difficulty: Intermediate.*

Let \(k=\mathbb Q\), let \(j:\mathbb C^*\hookrightarrow\mathbb C\), and let \(\mathcal L\) be the rank-one local system with counterclockwise holonomy \(H\) equal to multiplication by \(2\). For \(F=j_!\mathcal L\) and \(f(z)=z\), compute the nearby and vanishing objects at zero and the conormal section of \(\mu_{\{0\}}F\). Explain why (9) does not trivialize the original local system.

**Solution.** The central stalk is zero. The cover pullback of \(\mathcal L\) is constant \(\mathbb Q\); its contractible fibre has ordinary derived sections \(\mathbb Q\), with no higher cohomology. Thus \(\psi=\mathbb Q\), with nearby deck automorphism \(M=H^{-1}=1/2\) under the [coefficient and precomposition convention](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#a-disc-calculation-including-the-action-direction) \(T(e_n)=e_{n-1}\), and (1) gives \(\phi=\mathbb Q[-1]\). The conormal section \(\xi=1\) is therefore \(\mathbb Q[-1]\) by (20). Positive radial transport makes the original sheaf positively conic; its specialization at zero is the same conic sheaf by the [homogeneous specialization calibration](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-homogeneous--a-calibration-on-a-vector-space). The descent takes place on the simply connected cover. Descent to a counterclockwise loop recovers \(H=M^{-1}=2\), so \(\mathcal L\) on \(\mathbb C^*\) remains nontrivial. Both coefficients are perfect, and the two-stratum complex analytic stratification is valid.

### Arbitrary weak coefficients and central support

*Difficulty: Intermediate.*

Let \(M=\bigoplus_{r\geq1}\mathbb Q\), in degree zero, and use \(E=\mathbb C\times Y\), \(f(v,y)=v\). Compute both cycles for \(F=\tau^{-1}M_Y\) and for \(F=e_*M_Y\). Check their normal and conormal sections. Which perfect condition fails?

**Solution.** For the normal-constant family, cover descent gives \(\psi=M_Y\), and the central-to-nearby map is the identity, so \(\phi=0\). Its specialization is the same family; the normal section is \(M_Y\), while its Fourier transform is \(e_*M_Y[-2]\), whose nonzero conormal section is zero. For central support the specialization is \(e_*M_Y\), the punctured restriction is zero, and \(\psi=0\), \(\phi=M_Y\). Its Fourier transform is the normal-constant \(M_Y\), so its conormal section is \(M_Y\). All descent and coefficient maps retain the infinite module \(M\); finite-dimensionality was not used. These objects are weakly complex constructible but not perfect constructible on their nonzero strata, since a perfect complex over \(\mathbb Q\) has finite-dimensional cohomology.

### A ramified function needs the graph construction

*Difficulty: Intermediate.*

For \(F=\mathbb Q_{\mathbb C}\), \(f(z)=z^m\), \(m\geq2\), compute the cycles at zero and their deck monodromy. Compare the answer with a putative normal section defined by \(df_0\).

**Solution.** The pulled-back cover is described by \(z^m=e^{2\pi iw}\). It has \(m\) components, each parametrized by \(z=\exp(2\pi i(w+r)/m)\), \(r=0,\ldots,m-1\). Small covered punctured neighborhoods have contractible component fibres, giving \(\psi=\mathbb Q^m\) with cyclic permutation of components. The central unit is the diagonal \(\mathbb Q\to\mathbb Q^m\). It is injective, so (1) gives \(\phi=(\mathbb Q^m/\mathbb Q\mathbf1)[-1]\) with the induced cyclic monodromy. This is nonzero. The reduced zero set is a point, but \(df_0=0\) cannot identify its normal line with the target line or produce \(\ell^{-1}(1)\). The graph in (21) instead has the regular ambient coordinate \(t\), and its cycle comparison gives exactly these objects. The support bound uses the zero covector \(df_0\), which belongs to the microsupport of the nonzero constant sheaf.

### The graph transpose keeps the critical zero covector

*Difficulty: Intermediate.*

For a holomorphic \(f\) on \(X\), calculate the transpose differential of \(g(x)=(f(x),x)\). Derive (25) from the proper direct-image estimate and explain why the conclusion is still valid at a critical point.

**Solution.** A tangent vector \(a\) maps to \((df_x(a),a)\). A target covector \(c\,dt+\xi\) therefore evaluates to \(c\,df_x(a)+\xi(a)\), and its transpose image is \(c\,df_x+\xi\). At a graph point \((0,x)\), the covector \(dt\) corresponds to \((c,\xi)=(1,0)\), hence to \(df_x\). Properness holds because \(g\) is a closed embedding; its support restriction is proper too. The estimate forces \(df_x\in\operatorname{SS}(F)\) whenever \(dt\in\operatorname{SS}(g_*F)\). At a critical point this is a zero covector, not an undefined pullback. Zero covectors are retained in the estimate and in the closed support bound. For instance, in the preceding ramification example the graph covector \(dt\) can be characteristic even though its transpose is zero.

### The cotangent sign and the two scaling actions

*Difficulty: Advanced.*

In the coordinates of (3), evaluate the symplectic normal map on tangent vectors to \(L\). Verify its \(-v\) term. Distinguish complex normal scaling of the cone from the complex cotangent dilation needed for the bound (2).

**Solution.** The complex symplectic form is \(d\alpha\wedge du+d\beta\wedge dy\). A normal representative has components \((\delta u,\delta\beta)=(v,\beta)\); a tangent vector to \(L\) has components \((\delta\alpha,\delta y)=(a,b)\). Pairing the normal representative first gives \(-av+\beta b\). Taking real parts is exactly the real symplectic normal map, so its complex covector on \(L\) is \(-v\,d\alpha+\beta\,dy\). Normal scaling multiplies \(v,\beta\) at fixed \((\alpha,y)\); transported to \(T^*E\), it changes the base \(v\), so it is not cotangent dilation there. Multiplying ambient input covectors in (4) by \(\lambda\), however, changes \((\alpha,\beta)\) to \((\lambda\alpha,\lambda\beta)\) at fixed \((v,y)\). This proves the actual output cotangent dilation property. The analytic normal cone and the isotropy theorem supply the other hypotheses of the complex constructibility criterion.

### A uniform test near the zero section

*Difficulty: Advanced.*

For \(F=k_X\) with nonzero \(k\), prove the forward test near any nonzero cotangent covector. Show that no neighborhood of a zero covector can have every holomorphic test vanish, by choosing a constant function. Keep the normalization (1).

**Solution.** The microsupport of \(k_X\) is the zero section. A small cotangent neighborhood of a nonzero covector can be chosen disjoint from that section. Formula (24), applied on the domain of each holomorphic test, makes its vanishing stalk zero whenever its derivative belongs to that neighborhood. At a zero covector \((x;0)\), take \(h=0\) on a neighborhood of \(x\). Its punctured inverse image is empty, so \(\psi_h(F)=0\), and (1) gives \(\phi_h(F)=F\), with nonzero stalk \(k\) in degree zero. Thus that test belongs to every neighborhood of \((x;0)\) and prevents uniform vanishing. This verifies the zero-function phenomenon directly without asserting the reverse criterion for general weakly complex constructible objects.

## What has been established

The normal and conormal comparisons give weak and perfect complex cycle constructibility for every holomorphic function, the closed vanishing support bound, and the uniform forward test, using the stated prerequisite theorems. [Quadratic cycles and the holomorphic microsupport test](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/quadratic-cycles-and-the-holomorphic-microsupport-test.md#the-uniform-holomorphic-criterion) proves the reverse criterion and its coefficient model. [Vanishing cycles as positive real support](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/vanishing-cycles-as-positive-real-support.md#the-actual-cover-to-sector-restriction-is-an-isomorphism) gives the local-support comparison, including critical functions and singular zero fibres.

## References

David B. Massey, *Notes on Perverse Sheaves and Vanishing Cycles*, [arXiv:math/9908107v13, §3, pp. 26 and 28](https://arxiv.org/pdf/math/9908107v13#page=28), supplies the cycle conventions and explains the coefficient-complex construction credited to Kashiwara and Schapira. Ren Fernandes, Kazuki Kudomi and Kiyoshi Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, [arXiv:2603.14821v2, §2.4](https://arxiv.org/html/2603.14821v2#S2.SS4) and [§5, (5.42)–(5.43)](https://arxiv.org/html/2603.14821v2#S5.E42), defines specialization and states the regular-fibre conormal comparison. Its vanishing object is this lesson's object shifted by one. The paper refers elsewhere for that comparison; it does not supply an independent proof of it in those passages. Its characteristic-zero field-valued constructible setting also does not establish our weak-coefficient extension.

The argument here must therefore stand on its displayed normal-cone estimate, complex Euler annihilation, full-complex cylinder descent, Fourier section formula and slit coefficient map. The graph factorisation then handles critical functions. The linked programme proofs supply these geometric and sheaf-theoretic inputs. The human sources retain their mathematical credit; this lesson’s independently written exposition and eight solutions are CC0.
