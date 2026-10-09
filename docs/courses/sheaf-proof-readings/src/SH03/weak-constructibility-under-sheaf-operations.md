# Weak constructibility under sheaf operations

Weak constructibility asks for a geometric condition on microsupport and permits infinite coefficient modules. We can therefore prove stability under sheaf operations by transporting isotropic cotangent sets. Characteristic inverse image needs its limiting covectors, proper direct image needs compact control on the actual support, and Fourier transport needs both radial actions. These distinctions explain the hypotheses of the resulting theorem.

Use [Constructibility from microsupport and perfect stalks](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructibility-from-microsupport-and-perfect-stalks.md#three-equivalent-geometric-descriptions) for the geometric criterion, [Limiting cotangent sums and characteristic inverse images](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#isotropy-of-the-full-limiting-sum) for full limiting isotropy, and [Isotropic cotangent transport and discrete critical values](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#proper-direct-transport) for proper direct transport. The proof separates cotangent geometry from the sheaf estimates that transport microsupport. The exact suppliers are linked below; this lesson derives the constructibility applications from their stated contracts.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

## Coefficients, bounds and the geometric criterion

Manifolds and maps are real analytic, Hausdorff and countable at infinity, with uniform finite dimension bounds. Vector bundles have fixed finite rank. Let \(k\) be a commutative ring of finite global dimension \(g\). Every input below is an actual bounded derived object. No Noetherian, finite-generation or perfect-stalk assumption is made.

The criterion we will apply repeatedly is

\[
H\text{ is weakly }\mathbb R\text{-constructible}
\quad\Longleftrightarrow\quad
\operatorname{SS}(H)\text{ is contained in a closed conic
subanalytic isotropic set}.
\tag{1}
\]

For such an \(H\), its actual \(\operatorname{SS}(H)\) is itself closed, conic, subanalytic and Lagrangian, hence isotropic. The empty set is allowed for the zero object.

The boundedness inputs must accompany the geometric estimates. Exact inverse image, derived tensor over this ring and the finite-dimensional direct/exceptional image operations preserve boundedness in the cases used here. Internal Hom has the explicit sufficient bound

\[
A\in D^{[a,b]}(k_X),\quad B\in D^{[c,d]}(k_X)
\ \Longrightarrow\
R\mathcal Hom(A,B)\in
D^{[c-b,\ d-a+3\dim X+g+1]}(k_X).
\tag{2}
\]

This is the existing bounded-Hom prerequisite, for arbitrary bounded coefficients. Normal specialization and Fourier transformation in fixed rank have finite amplitude as well. We retain these inputs rather than infer boundedness just from a symbol \(R\mathcal Hom\) or from fibrewise bounded stalks.

The [ordinary and exceptional characteristic estimates](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/characteristic-estimates.md#sh02-che-005--ordinary-and-exceptional-inverse-image) and [full limiting tensor/Hom estimates](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/characteristic-estimates.md#sh02-che-006--tensor-and-internal-hom-without-a-transversality-assumption) apply to bounded inputs with arbitrary stalk modules. Their graph, normal-deformation and recovery contracts remain dependencies. The [proper-image estimate](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#the-proper-image-microsupport-estimate-proper-image-microsupport-proof) requires properness on the actual closed support; the separate [characteristic-inverse isotropy proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#the-graph-conormal-and-characteristic-inverse-image) supplies the geometric bound for inverse images.

For Fourier transport use the [Euler criterion and both radial actions](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-conic-test--the-euler-equation-detects-conic-sheaves) and [full Fourier microsupport equality](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-fs-ss--fourier-transformation-of-microsupport), including its zero-direction argument and its use of Fourier inversion for the reverse inclusion. The [positive normal deformation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/normal-scaling-and-microlocal-hom.md#normal-scaling-and-the-positive-deformation-normal-deformation-charts), [normalized conic specialization](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/normal-scaling-and-microlocal-hom.md#normal-scaling-and-strong-conicity-specialization-strong-conicity) and [diagonal microlocal-Hom definition](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/normal-scaling-and-microlocal-hom.md#a-sheaf-of-directional-morphisms-microlocal-hom-estimate) specify the constructions used here. The forward Fourier estimate in that last lesson alone is not the full equality.

The later coefficient comparisons use [projection with arbitrary coefficients](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-projection--projection-with-arbitrary-coefficients) and [bounded exceptional internal-Hom adjunction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom). The small-ball provider retains the natural restriction and support maps, with its [compact chart cutoff](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#applying-the-theorem-in-an-open-coordinate-chart-local-chart-cutoff). These are exact immediate inputs; their further topological and subanalytic foundations remain separate proof obligations.

## Characteristic inverse images stay weakly constructible

Let \(f:Y\to X\) be analytic and let \(F\) be weakly constructible. The full characteristic estimates are

\[
\operatorname{SS}(f^{-1}F)\subset f^\sharp\operatorname{SS}(F),
\qquad
\operatorname{SS}(f^!F)\subset f^\sharp\operatorname{SS}(F).
\tag{3}
\]

The characteristic inverse \(f^\sharp\) includes the limits of moving transpose differentials applied to possibly unbounded covectors. The preceding geometric theorem proves that \(f^\sharp\Lambda\) is closed, conic, subanalytic and isotropic whenever \(\Lambda\) is conic, subanalytic and isotropic. Apply this to the actual \(\Lambda=\operatorname{SS}(F)\); (1) and (3) prove that both \(f^{-1}F\) and \(f^!F\) are weakly constructible.

No noncharacteristic hypothesis or submersion assumption on \(f\) is required. In particular, we have not identified \(f^!F\) with \(f^{-1}F\) times an orientation complex for an arbitrary map. The latter formula requires its own hypotheses.

## Properness on support supplies the cotangent compactness

Let \(G\) be weakly constructible on \(Y\), and suppose \(f\) is proper on its closed support. In the cotangent correspondence put

\[
C_f=Y\times_XT^*X,\qquad
f_d(y;\xi)=(y;df_y^t\xi),\qquad
f_\pi(y;\xi)=(f(y);\xi).
\tag{4}
\]

The proper-support microsupport estimate is

\[
\operatorname{SS}(Rf_*G)\subset
f_\pi f_d^{-1}\operatorname{SS}(G).
\tag{5}
\]

We must verify that the right side is the closed subanalytic isotropic set required in (1). Put \(\Lambda=\operatorname{SS}(G)\) and \(A=f_d^{-1}\Lambda\). The domain \(A\) is closed and subanalytic. Every point \((y;\xi)\in A\) has \(y\in\pi_Y(\Lambda)=\operatorname{supp}(G)\), including points where \(df_y^t\xi=0\).

For a compact \(K\subset T^*X\), let \(Q\subset X\) be its compact base projection and put

\[
Y_Q=\operatorname{supp}(G)\cap f^{-1}(Q).
\tag{6}
\]

This is compact by the stated properness. The inverse image of \(K\) in \(A\) lies in the fibre product of the compact sets \(Y_Q\) and \(K\). That fibre product is closed in \(Y_Q\times K\), and the additional condition \(f_d(y;\xi)\in\Lambda\) is closed. The inverse image is consequently compact. Thus \(f_\pi|_A\) is proper.

The proper direct-transport theorem now proves that
\(f_\pi(A)\) is closed, conic, subanalytic and isotropic. Equations (1) and (5) prove weak constructibility of \(Rf_*G\). Under the same support properness \(Rf_!G\simeq Rf_*G\), so that object has the same conclusion.

We used the actual \(\operatorname{SS}(G)\). An arbitrarily enlarged containing isotropic set can have extra base points on which \(f\) is not proper, and cannot be substituted in this compactness proof.

## Tensor and internal Hom retain the full limiting sum

For weakly constructible \(F,G\) on \(X\), the bounded estimates give

\[
\begin{aligned}
\operatorname{SS}(F\otimes^LG)&\subset
\operatorname{SS}(F)\widehat+\operatorname{SS}(G),\\
\operatorname{SS}(R\mathcal Hom(G,F))&\subset
\operatorname{SS}(F)\widehat+\operatorname{SS}(G)^a.
\end{aligned}
\tag{7}
\]

Here \(a(x;\xi)=(x;-\xi)\) is the cotangent antipode. It carries a conic subanalytic isotropic set to another such set: its pullback changes the canonical one-form by a minus sign, which still vanishes. The full limiting-sum theorem then makes both right sides of (7) closed, conic, subanalytic and isotropic. Criterion (1) proves weak constructibility of both objects.

The first Hom argument carries the antipode. No transversality assumption is used, and the limiting sum cannot generally be replaced by an ordinary same-base sum. The Hom argument also uses its actual internal-Hom estimate, not a replacement by a tensor with a dual of an infinite coefficient complex.

## Fourier transport and the Euler pairing

Let \(E\to Z\) be an analytic vector bundle and let \(F\) be a bounded conic weakly constructible complex on \(E\). Conic for a sheaf means local constancy along positive fibre-scaling orbits, including the fixed zero-section orbits.

In local bundle coordinates write a point of \(T^*E\) as
\((z,v;\zeta,\eta)\). The Fourier cotangent map is the global analytic diffeomorphism whose coordinate formula is

\[
\Phi_E(z,v;\zeta,\eta)=(z,\eta;\zeta,-v).
\tag{8}
\]

Let \(\theta_E=\langle v,\eta\rangle\), the pairing of a covector with the fibre Euler vector field. With \(\alpha_E,\alpha_{E^*}\) the canonical one-forms,

\[
\Phi_E^*\alpha_{E^*}=\alpha_E-d\theta_E.
\tag{9}
\]

For conic \(F\), its actual microsupport \(\Lambda\) lies in \(\theta_E^{-1}(0)\), and is invariant under both actions

\[
r_\lambda(z,v;\zeta,\eta)=(z,v;\lambda\zeta,\lambda\eta),
\qquad
s_\mu(z,v;\zeta,\eta)=(z,\mu v;\zeta,\mu^{-1}\eta).
\tag{10}
\]

The first is cotangent dilation, the second the cotangent lift of bundle dilation. This biconicity is the existing conic microsupport criterion.

Because \(\theta_E\) is zero on \(\Lambda\), its differential restricts to zero on the regular locus of \(\Lambda\). Isotropy of \(\Lambda\) and (9) therefore prove isotropy of \(\Phi_E\Lambda\). The analytic diffeomorphism preserves closedness and subanalyticity. It also carries biconic sets to biconic sets: direct substitution gives

\[
\Phi_Er_\lambda=r_\lambda s_\lambda\Phi_E,
\qquad
\Phi_Es_\mu=s_{\mu^{-1}}\Phi_E.
\tag{11}
\]

In particular its image is conic in the target cotangent fibres. For example,
\(r_\lambda\Phi_E=\Phi_Er_\lambda s_\lambda\),
which expresses target cotangent dilation using the two source actions.

The full bounded conic Fourier microsupport theorem, including both zero loci, is

\[
\operatorname{SS}(F^\wedge)=\Phi_E\operatorname{SS}(F).
\tag{12}
\]

Equations (8)–(12) and (1) prove that \(F^\wedge\) is weakly constructible. We use the negative-pairing proper-support convention

\[
F^\wedge=Rq_!\bigl(p^{-1}F\otimes k_{\{\langle v,\eta\rangle\leq0\}}\bigr),
\tag{13}
\]

with \(p:E\times_ZE^*\to E\), \(q:E\times_ZE^*\to E^*\). The projection in (13) is generally nonproper; the proof used the Fourier theorem and conicity, not the proper-push theorem (5). For rank zero \(\Phi_E\) and the Fourier functor are the identity, and the argument still applies.

## The open extension used in specialization

For an open subanalytic inclusion \(j:\Omega\hookrightarrow W\) and a bounded weakly constructible \(H\) on \(W\), there is the natural identity

\[
Rj_*j^{-1}H\simeq R\mathcal Hom(k_\Omega,H).
\tag{14}
\]

Here \(k_\Omega=j_!k\). Internal-Hom adjunction identifies the right side with
\(Rj_*R\mathcal Hom(k,j^{-1}H)\); the inner Hom is \(j^{-1}H\). Thus (14) is the actual open-extension identity for arbitrary coefficients. The sheaf \(k_\Omega\) is constructible by the locally closed subanalytic example. The Hom result (7) proves that (14) is weakly constructible without properness of \(j\) on the support.

Now let \(M\) be an analytic embedded submanifold of \(X\), closed in the ambient neighborhood under consideration. In its analytic normal deformation use

\[
p:\widetilde X_M\to X,\quad
\Omega=\{t>0\},\quad j:\Omega\hookrightarrow\widetilde X_M,
\quad s:T_MX\hookrightarrow\widetilde X_M.
\]

In adapted coordinates \(p(v,z,t)=(tv,z)\), so \(p\) is defined and analytic also at \(t=0\). Normal specialization is

\[
\nu_MF=s^{-1}Rj_*j^{-1}p^{-1}F.
\tag{15}
\]

By (3), \(p^{-1}F\) is weakly constructible on the whole deformation. Apply (14), then (3) for \(s\). This proves weak constructibility of \(\nu_MF\). Its boundedness and conicity are the specialization contracts: the scaling
\((v,z,t)\mapsto(\lambda v,z,t/\lambda)\)
fixes \(p\) and preserves the positive chamber, and restricts to ordinary dilation on the central normal bundle. Equivariant inverse and direct image give its conic structure, with the previously stated finite amplitude.

Consequently

\[
\mu_MF=(\nu_MF)^\wedge
\tag{16}
\]

is weakly constructible on \(T_M^*X\), by the Fourier argument. For a locally closed \(M\), restrict to neighborhoods where it is closed; the deformation constructions are compatible with these restrictions, so the assertion is local and gives the same global object.

## Microlocal Hom follows from its diagonal kernel

Let \(q_1,q_2:X\times X\to X\) be the projections, and let \(F,G\) be weakly constructible. Both \(q_2^{-1}G\) and \(q_1^!F\) are weakly constructible by (3). Their internal Hom is weakly constructible by (7), and is bounded by (2). The defining formula is

\[
\mu\operatorname{hom}(G,F)=
\mu_{\Delta_X}R\mathcal Hom(q_2^{-1}G,q_1^!F),
\tag{17}
\]

under the identification
\(T^*_{\Delta_X}(X\times X)\simeq T^*X\),
\((x,x;\xi,-\xi)\mapsto(x;\xi)\).
Apply (15)–(16) to the bounded diagonal kernel. It proves that (17) is weakly constructible on \(T^*X\).

The exceptional projection in this formula matters. It is
\(q_1^!F=q_1^{-1}F\otimes q_2^{-1}\omega_X\),
where \(\omega_X=\operatorname{or}_X[\dim X]\). Both its orientation line and its shift are retained in the kernel. The argument needs no constructible biduality and places no perfection hypothesis on either Hom input.

We have proved the full weak stability theorem: analytic ordinary and exceptional inverse images; proper-on-support direct image; tensor and internal Hom; conic Fourier transform; and microlocal Hom. Specialization and the microlocalization of a weakly constructible object were proved along the way. Assertions that these operations preserve perfect stalks require the separate finiteness arguments that follow this lesson.

## Examples and exercises with solutions

### The cubic inverse needs covectors growing to infinity

*Difficulty: Intermediate.*

Let \(f(y)=y^3\) and \(F=k_{\{0\}}\) on \(\mathbb R_x\), with \(k\neq0\). Compute the ordinary transpose-differential image of \(\operatorname{SS}(F)\). Exhibit every covector over zero in its characteristic inverse, and compare with \(f^{-1}F\).

**Solution.** The source microsupport is the full fibre at zero. Its ordinary inverse requires \(y=0\) and sends each \(\xi\) to \(3y^2\xi=0\); thus it is only \((0;0)\). For any \(\eta\neq0\), choose \(y_j\neq0\) tending to zero, \(x_j=0\) and \(\xi_j=\eta/(3y_j^2)\). Then
\(3y_j^2\xi_j=\eta\) and
\(|x_j-y_j^3||\xi_j|=|\eta||y_j|/3\to0\).
These are full characteristic-inverse witnesses. The zero covector has a constant zero witness. The inverse sheaf is \(k_{\{0\}}\) on the \(y\)-line, whose microsupport is the full fibre. This fits (3), whereas the ordinary inverse set cannot bound it. All outputs remain weakly constructible.

### A tangency enlarges the tensor microsupport

*Difficulty: Advanced.*

In \(\mathbb R^2_{u,v}\), take \(Y=\{v=0\}\), \(Z=\{v=u^2\}\), \(F=k_Y\), \(G=k_Z\), with \(k\neq0\). Compare the ordinary conormal sum over the origin with \(\operatorname{SS}(F\otimes^LG)\). Construct a full limiting-sum witness for an arbitrary \(a\,du+b\,dv\) at the origin.

**Solution.** Both stalk sheaves are flat over \(k\), having stalks \(k\) or zero. Their tensor is \(k_{Y\cap Z}=k_{\{0\}}\), so its microsupport is the whole origin fibre. At the origin both conormals are the line spanned by \(dv\), and their ordinary sum is that line. For \(t\neq0\) tending to zero, choose the first base \((t,0)\), the second \((t,t^2)\), second coefficient \(\mu=-a/(2t)\), and first coefficient \(\lambda=b-\mu\). The conormals are
\(\lambda\,dv\) and \(\mu(-2t\,du+dv)\); their sum is precisely \(a\,du+b\,dv\). The base gap is \(t^2\), and \(t^2|\lambda|\to0\). This is a full limiting witness, including the case of zero coefficients. The right side of (7) contains the actual tensor microsupport.

### Singular values escaping from a nonproper support

*Difficulty: Advanced.*

Let \(f(y)=1/(1+y^2)\) and \(G=\bigoplus_{m\geq1}k_{\{m\}}\) on \(\mathbb R\), over a nonzero field. Show that \(G\) is constructible with perfect stalks. Explain why \(f_*G\) is not weakly constructible near zero and why (5) does not apply.

**Solution.** The positive integers are closed and locally finite, and the sheaf is locally a single point sheaf or zero. Its stalks are \(k\) or zero. Its locally finite analytic partition therefore proves constructibility and perfection. At each \(x_m=1/(1+m^2)\), the direct image has a stalk \(k\): choose a sufficiently small neighborhood isolating that value among the \(x_j\). On the intervening open gaps the direct image is zero. These infinitely many point jumps accumulate at the ambient point zero. A weakly constructible sheaf on a real analytic line has, near any point, only finitely many point strata in a compatible locally finite subanalytic stratification. All other strata there are open intervals with locally constant cohomology. The infinitely many isolated nonzero jumps violate that condition. Thus \(f_*G\) is not weakly constructible near zero. Properness on support fails, because the inverse image of the compact interval \([0,1]\) in the support is the unbounded set of all positive integers. Indeed \(G\) is flabby, its sections being products of the stalks on the discrete support with surjective restriction maps; it is acyclic on every inverse-image open set. Hence here \(Rf_*G=f_*G\), and the failure also concerns the bounded derived direct image.

### The first Hom argument reverses a boundary direction

*Difficulty: Intermediate.*

On \(\mathbb R\), let \(G=k_{[0,\infty)}\) and \(F=k_{\mathbb R}\). Compute \(R\mathcal Hom(G,F)\), and compare its boundary microsupport with that of \(G\).

**Solution.** Internal Hom from the closed-support constant sheaf is local cohomology with support in that closed set. At an interior positive point it is \(k\), and on the negative open half-line it is zero. At zero, the local support triangle compares the constant coefficient on a small interval to its restriction to the negative half-interval; that map is the identity of \(k\), so the supported stalk is zero in every degree. Thus the Hom is \(k_{(0,\infty)}\), with no shift. The closed positive half-line has boundary covectors \(\xi\geq0\); the open positive half-line has boundary covectors \(\xi\leq0\). The antipode on \(\operatorname{SS}(G)\) in (7) accounts for this reversal.

### Infinite coefficients invalidate a dual-tensor shortcut

*Difficulty: Intermediate.*

At one point over a field, take \(V=\bigoplus_{m\geq1}k\). Compare the evaluation map \(V^*\otimes V\to\operatorname{Hom}(V,V)\). Is the identity in its image? How does this bear on the Hom proof?

**Solution.** A finite sum \(\sum_{j=1}^r\ell_j\otimes v_j\) acts by \(w\mapsto\sum_j\ell_j(w)v_j\). Its image is contained in the finite-dimensional span of the \(v_j\), so every operator in the image has finite rank. The identity of \(V\) has infinite rank and is absent. All vector spaces here are projective, so the same failure holds for the derived comparison in degree zero. They are weakly constructible on a point, and \(\operatorname{Hom}(V,V)\) is another allowed weak coefficient module. Thus weak constructibility alone cannot justify the dual-tensor identification. Formula (7) uses actual internal Hom and still applies.

### Fourier transforms a line into its annihilator

*Difficulty: Intermediate.*

On \(E=\mathbb R^2\), let \(L\) be the first coordinate axis with its standard orientation. Compute \((k_L)^\wedge\) under (13), and check (12) at its zero loci.

**Solution.** At \(\eta\notin L^\perp\), the allowed part of \(L\) is a closed half-line, whose compactly supported cohomology is zero. At \(\eta\in L^\perp\), it is all of the oriented line, whose compactly supported cohomology is \(k[-1]\). The proper-support kernel calculation and its closed-support localization therefore give \((k_L)^\wedge=k_{L^\perp}[-1]\). Its shift comes from the one-dimensional integration. The source conormal has \(v=(u,0)\), \(\eta=(0,b)\); (8) sends it to base \((0,b)\) with covector \((-u,0)\), precisely the conormal of \(L^\perp\). This computation includes \(u=0\), \(b=0\) and the total zero point, not just nonzero incidence directions.

### The exceptional projection cancels the normal Fourier shift

*Difficulty: Advanced.*

On the oriented line \(X=\mathbb R\), compute \(\mu\operatorname{hom}(k_X,k_X)\) from (17). Track the exceptional projection and the normal Fourier shift.

**Solution.** The projection \(q_1:X^2\to X\) has oriented one-dimensional fibres, so \(q_1^!k_X=k_{X^2}[1]\). Internal Hom from \(q_2^{-1}k_X=k_{X^2}\) leaves that kernel unchanged. Specialization of a constant sheaf along the diagonal is the constant sheaf on its normal line bundle, with the same shift \([1]\): in deformation charts the positive half-interval has ordinary cohomology \(k\) in degree zero, so (15) adds no shift. Fourier transform of the constant sheaf on each oriented normal line is the sheaf on its zero covector shifted by \([-1]\). The two shifts cancel. Hence \(\mu\operatorname{hom}(k_X,k_X)\) is \(k_X\) extended from the zero section of \(T^*X\), in degree zero. Removing the exceptional projection's shift from the defining kernel would have produced the wrong degree.

## References

The classical geometric source is Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). Theorem 8.2.6, printed pp. 146–147, characterizes weak constructibility by isotropic containment and by the actual Lagrangian microsupport. Its proof uses a compatible stratification, local constancy on flat strata and involutivity. Proposition 8.3.1, pp. 148–149, first proves weak constructibility of proper image by transporting the canonical one-form, then obtains finite coefficients separately. Propositions 8.3.3–8.3.6, pp. 149–150, treat inverse images, specialization, microlocalization, conic Fourier transformation and tensor/Hom for the perfect-stalk category. Their statements and proofs are not a blanket arbitrary-module stability theorem.

The first part of this lesson proves the weak-coefficient applications through the separately supplied geometric and sheaf-operation estimates. The distinction is visible in the arguments: support properness supplies cotangent compactness; limiting isotropy handles characteristic inverse image and tensor/Hom; the Euler pairing and both radial actions handle Fourier transport; and open-extension Hom identifies the specialization input. No perfect dual is used for the weak Hom operation. The bounded-Hom estimate has the exact supplier Local orientations, dimension, and integration. The characteristic estimates, full limiting isotropy, proper direct transport, conic Fourier comparison, normal deformation and diagonal Hom identity retain their own prerequisite obligations. The monograph refers onward for normal-cone isotropy and stratified topology; comparing its proof does not close those dependencies.

Andreas Hohl and Pierre Schapira, [*Unusual functorialities for weakly constructible sheaves*, arXiv:2303.11189v2](https://arxiv.org/html/2303.11189v2), 7 January 2025, supplies the infinite locally constant coefficient comparisons developed next. The comparison was made with the versioned author source. Its §3 develops weak cohomological constructibility and its point comparisons; §4 proves inverse-image, tensor/Hom and direct-image compatibilities. The opening stability facts and the passage from weak real constructibility to weak cohomological constructibility are recalled from earlier work. They are inputs to that paper, rather than new proofs contained there.

These references identify both the older geometric mechanism and the later coefficient theorems. The programme supplies its own teaching expression, expanded map checks and complete solved examples. Its CC0 dedication does not apply to human source text or diagrams, none of which are imported here. The specific earlier foundation references are not replaced by a claim of complete source or prerequisite closure.

## Natural comparisons with infinite locally constant coefficients

The statements in (18), (21), (24), (29), (31), (36) and (37) follow the coefficient comparisons of Hohl–Schapira, §§3–4, with the same arbitrary bounded locally constant coefficients and the stated perfect-factor, boundary-control and field hypotheses. Their §3 point-comparison proof uses representable ind- and pro-systems. The argument below instead applies ordinary Hom and compact-support projection to values already stabilized on actual small balls, using [Small balls, central fibres, and supported cohomology](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#applying-the-theorem-in-an-open-coordinate-chart-local-chart-cutoff). This is a different presentation of the local input, with an explicit obligation to prove stabilization for the Hom and tensor outputs as well. It does not move an infinite Hom through an arbitrary filtered colimit.

The later steps retain the paper's mathematical mechanisms and are credited accordingly. Its §4 inverse-image theorem is tested on stalks and costalks; its tensor/Hom theorem puts the perfect factor in two different positions and uses the diagonal for the second; its direct-image theorem places the graph in the ambient compactification and controls the graph-coefficient supports. The present proof expands the external evaluation map on rectangles, supplies both direct-image comparisons and checks their canonical maps. The costalk argument uses the actual ball/sphere restriction map, including its diagonal in dimension one, so no conclusion is drawn merely from an abstract module being isomorphic to its double. In the direct-image theorem the images lie on the target ambient pair, as the graph projections show.

The final field result uses the same finite direct-summand mechanism as the paper's closing proposition: one nonzero cohomology module contains a copy of the coefficient field, which makes a shift of the original sheaf a retract of each output. It applies to arbitrary bounded target sheaves and does not need weak constructibility of that target. The worked finite-rank, boundary-accumulation, disconnected-space and integral-torsion examples then show separately why the hypotheses of the coefficient comparisons matter. The earlier perfect-operation lesson retains responsibility for the finite-coefficient stability inputs; neither source is treated as a proof of the entire prerequisite chain.

We keep the coefficient and manifold conventions of this lesson. A locally constant complex means a bounded derived object locally isomorphic to \(L_U\), for \(L\in D^b(k)\). In particular, the individual modules of \(L\) can be infinite. All tensors in this extension are derived, and every comparison is the usual map obtained from evaluation, adjunction or projection, rather than an unspecified isomorphism between its two objects.

### Small balls give the actual point comparisons

For weakly constructible \(G\), a point \(x\), and arbitrary \(L\in D^b(k)\), the natural maps are isomorphisms:

\[
\begin{aligned}
\bigl(R\mathcal Hom(L_X,G)\bigr)_x
&\longrightarrow R\operatorname{Hom}_k(L,G_x),\\
(i_x^!G)\otimes L
&\longrightarrow i_x^!(G\otimes L_X).
\end{aligned}
\tag{18}
\]

**Proof.** Use the small-ball theorem in a coordinate chart, with its compact support cutoff. It gives a cofinal basis of balls \(U\) on which the natural ordinary and compact comparisons for \(G\) are respectively \(R\Gamma(U;G)\simeq G_x\) and \(i_x^!G\simeq R\Gamma_c(U;G)\). The preceding stability proof also applies to \(R\mathcal Hom(L_X,G)\) and \(G\otimes L_X\). Shrink the balls so that their comparisons stabilize as well.

For every such ball, constant-sheaf adjunction and proper-support projection give

\[
\begin{aligned}
R\Gamma(U;R\mathcal Hom(L_U,G|_U))
&\simeq R\operatorname{Hom}_k(L,R\Gamma(U;G)),\\
R\Gamma_c(U;G|_U)\otimes L
&\simeq R\Gamma_c(U;G|_U\otimes L_U).
\end{aligned}
\tag{19}
\]

For the first identity, tensor–Hom adjunction followed by the adjunction between the constant-sheaf functor and sections gives the indicated derived coefficient Hom. For the second use projection for \(a_U:U\to\{\mathrm{pt}\}\), whose proper-support functor is compact cohomology. Neither identity needs a finite first Hom argument or a perfect tensor factor.

Insert the stabilized values into (19). Naturality in restriction and inclusion of supports identifies the resulting maps with (18): the stalk map is restriction followed by evaluation, and the costalk map is the tensor–exceptional comparison followed by the compact comparison. Thus these particular maps are invertible. We have applied Hom to an already stabilized value, never interchanged infinite Hom with an arbitrary filtered colimit. \(\square\)

### Costalks detect a weakly constructible object

**Lemma.** If \(H\) is bounded and weakly constructible and every \(i_x^!H\) vanishes, then \(H=0\). Consequently a morphism between bounded weakly constructible objects is an isomorphism if all its costalk maps are isomorphisms.

**Proof.** A constant complex \(A_B\) on a \(d\)-dimensional coordinate ball has

\[
i_x^!A_B\simeq A\otimes \mathrm{or}_{B,x}^{\vee}[-d].
\tag{20}
\]

This is the relative ball/sphere calculation, retaining the orientation line. For \(d=1\), ordinary restriction to the two punctured components is the diagonal \(A\to A\oplus A\); its difference quotient is \(A\), and its fibre is \(A[-1]\). For larger \(d\), a finite cellular cochain complex for the ball/sphere pair has one relative top generator; tensoring it with \(A\) gives (20). This finite free calculation is valid for arbitrary coefficient modules. The zero-dimensional case is ordinary evaluation. A line and a shift are invertible, so (20) vanishes exactly when \(A\) does.

Choose a locally finite subanalytic stratification on which the finitely many cohomology sheaves of \(H\) are locally constant, refining it to connected strata with the frontier condition. If \(H\neq0\), choose a stratum \(S\) of maximal dimension among those with nonzero cohomology. Near a point \(x\in S\), all other nonzero strata can be excluded: there are locally only finitely many of them, and if the closure of one met \(S\), the frontier condition would make its dimension strictly greater than \(\dim S\), contrary to maximality. Shrink also so that \(S\) is closed in the chosen ambient neighborhood.

On a smaller ball in \(S\), the whole derived restriction of \(H\) is constant. Here is why cohomological local constancy suffices. Trivialize all its finitely many cohomology sheaves on that ball. Constant sheaves with arbitrary coefficients are acyclic on smaller convex balls. The bounded hypercohomology sequence therefore identifies every cohomology group of its section complex with the corresponding stalk module. The counit from the constant section complex to the restriction is an isomorphism on every stalk, and hence is an isomorphism of derived sheaves.

In this neighborhood \(H\) has no stalks outside the closed \(S\). Closed-complement localization identifies it with the closed direct image of its restriction to \(S\). Exceptional composition then identifies its costalk at \(x\) with the intrinsic costalk on \(S\). Equation (20) makes that costalk a nonzero shifted, orientation-twisted coefficient, a contradiction. The morphism assertion follows by applying this argument to its cone, which remains bounded and weakly constructible. \(\square\)

The diagonal in dimension one is essential: an infinite module can be abstractly isomorphic to its double. Its natural restriction map can still have a nonzero cokernel.

### Analytic inverse images commute with these coefficients

Let \(f:X\to Y\) be analytic, let \(G\) be bounded weakly constructible, and let \(M\) be bounded locally constant on \(Y\). Then

\[
\begin{aligned}
f^{-1}R\mathcal Hom(M,G)
&\xrightarrow{\sim}R\mathcal Hom(f^{-1}M,f^{-1}G),\\
f^!G\otimes f^{-1}M
&\xrightarrow{\sim}f^!(G\otimes M).
\end{aligned}
\tag{21}
\]

**Proof.** Work near \(y=f(x)\), where \(M=L_Y\). At \(x\), the first comparison is the identity of \(R\operatorname{Hom}_k(L,G_y)\), by (18) and ordinary stalk composition. Stalks detect isomorphisms of sheaves, proving the first line.

For the second line take a costalk at \(x\). Equation (18), first for \(f^!G\) and then for \(G\), and exceptional composition identify the comparison with

\[
(i_x^!f^!G)\otimes L
\simeq(i_y^!G)\otimes L
\xrightarrow{\sim}i_y^!(G\otimes L_Y)
\simeq i_x^!f^!(G\otimes L_Y).
\tag{22}
\]

The two objects in the second line of (21) are bounded weakly constructible by the preceding stability sections. The costalk lemma proves that their canonical comparison is invertible. Local computations glue because all maps are the canonical ones. No noncharacteristic or perfection assumption on \(M\) is needed. \(\square\)

### Two different positions for the perfect factor

The elementary algebraic input is

\[
R\operatorname{Hom}_k(L,A)\otimes P
\xrightarrow{\sim}R\operatorname{Hom}_k(L,A\otimes P),
\qquad P\ \text{perfect},\quad L,A\in D^b(k).
\tag{23}
\]

For \(P=k\) this is the identity. Finite sums, shifts and direct summands give the result for a finite projective module in any degree. Represent a perfect \(P\) by a bounded finite-projective complex and filter it by its finitely many terms. Both sides and the comparison respect the resulting triangles. Induction and the five lemma give (23). This proves invertibility of the natural map, with no finiteness imposed on \(L\) or \(A\).

If \(K\) is bounded locally constant, \(G\) is bounded weakly constructible, and \(P\) is \(\mathbb R\)-constructible with perfect stalks, then

\[
\begin{aligned}
R\mathcal Hom(K,G)\otimes P
&\xrightarrow{\sim}R\mathcal Hom(K,G\otimes P),\\
R\mathcal Hom(P,G)\otimes K
&\xrightarrow{\sim}R\mathcal Hom(P,G\otimes K).
\end{aligned}
\tag{24}
\]

**Proof of the first line.** Locally put \(K=L_X\). At \(x\), (18) identifies the comparison with (23) for \(A=G_x\) and perfect \(P_x\). Stalks detect its invertibility.

For the second line we need the external comparison, and give its proof rather than infer it from Hom of ordinary stalks. For projections \(q_1,q_2:X\times X\to X\) there is the evaluation map

\[
D_XP\boxtimes G
\longrightarrow R\mathcal Hom(q_1^{-1}P,q_2^!G).
\tag{25}
\]

On a rectangle \(U\times V\), exceptional adjunction for its second projection and proper-support base change identify sections of the right side with

\[
R\operatorname{Hom}_k(R\Gamma_c(U;P),R\Gamma(V;G)).
\tag{26}
\]

Indeed the proper-support image of the first projection's inverse image of \(P|_U\) is the constant complex on \(V\) with value \(R\Gamma_c(U;P)\); adjunction with sections gives (26). These identities commute with shrinking both factors.

Choose cofinally small \(U\) at \(x\). The actual small-ball comparison identifies \(R\Gamma_c(U;P)\) with the perfect \(C_x=i_x^!P\). Its perfection is supplied by [the perfect-costalk proposition](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#perfect-stalks-give-perfect-costalks), using [finite descent on a compact triangulation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#finite-descent-on-a-compact-triangulation) for the small sphere. Those arguments use the weak-operation theorem already proved above and the small-ball theorem; they do not use the infinite-coefficient comparisons being proved in this section. In the second variable stalk passage in (26) is valid because \(R\operatorname{Hom}_k(C_x,-)\) is represented by a bounded finite-projective dual tensor, which commutes with filtered stalk passage. Thus the right side's stalk at \((x,y)\) is \(R\operatorname{Hom}_k(C_x,G_y)\). The left side's stalk is \(C_x^\vee\otimes G_y\), by the stalk–costalk formula for \(D_XP\). Finite-projective evaluation identifies these stalks and is precisely (25) on them. This proves (25). This argument would also allow an arbitrary bounded \(G\).

Put \(H=D_XP\boxtimes G\) and let \(\delta:X\to X^2\) be the diagonal. The bounded exceptional internal-Hom identity and \(q_i\delta=\operatorname{id}\) give

\[
\delta^!H\simeq R\mathcal Hom(P,G).
\tag{27}
\]

The object \(D_XP\) is constructible by [constructible duality](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#duality-exchanges-the-measurements-before-biduality), so \(H\) is weakly constructible. Apply the second line of (21) to \(\delta\), \(H\), and the locally constant \(q_2^{-1}K\). Using (25)–(27) before and after tensoring gives

\[
\delta^!H\otimes K
\xrightarrow{\sim}\delta^!(H\otimes q_2^{-1}K)
\simeq R\mathcal Hom(P,G\otimes K).
\tag{28}
\]

All external comparisons are evaluation maps; exceptional comparison is constructed by currying evaluation and trace. Their associativity identifies (28) with the second natural map in (24), including Koszul symmetry. This proves that map invertible. \(\square\)

In the first line of (24) perfection is in the tensor factor \(P\); in the second it is in the first Hom argument. Neither line asserts that a tensor with an arbitrary weak coefficient can be moved out of any Hom.

### An ambient extension controls an open boundary

Let \(j:U\hookrightarrow X\) be open and subanalytic, and suppose \(F\) on \(U\) is the restriction of a bounded weakly constructible \(G\) on \(X\). Let \(K\) be bounded locally constant on \(X\). Then

\[
\begin{aligned}
j_!R\mathcal Hom(j^{-1}K,F)
&\xrightarrow{\sim}R\mathcal Hom(K,j_!F),\\
(Rj_*F)\otimes K
&\xrightarrow{\sim}Rj_*(F\otimes j^{-1}K).
\end{aligned}
\tag{29}
\]

**Proof.** The two ambient descriptions are

\[
j_!F=k_U\otimes G,\qquad
Rj_*F=R\mathcal Hom(k_U,G),
\tag{30}
\]

where \(k_U=j_!k\) has perfect stalks. Apply the first line of (24) with \(P=k_U\). Its left side is \(j_!j^{-1}R\mathcal Hom(K,G)=j_!R\mathcal Hom(j^{-1}K,F)\), by open restriction. Its right side is \(R\mathcal Hom(K,j_!F)\). This gives the first natural map in (29).

The second line of (24), again with \(P=k_U\), gives
\(R\mathcal Hom(k_U,G)\otimes K\simeq R\mathcal Hom(k_U,G\otimes K)\). Equation (30) identifies these with the second map's two objects. All identities use the actual open adjunctions. Relative compactness is sufficient when needed below, but this proof only needs a subanalytic open set and the specified ambient extension. It does not assert this extension exists for an arbitrary weakly constructible object on \(U\). \(\square\)

### Nonproper maps with controlled behavior at infinity

A **b-analytic manifold** here is a pair \(X_\infty=(X,\widehat X)\), with \(X\) an open relatively compact subanalytic subset of a real analytic manifold \(\widehat X\). Write \(j_X:X\hookrightarrow\widehat X\). A morphism \(f:X_\infty\to Y_\infty\) is an analytic map \(f:X\to Y\) whose graph is subanalytic in \(\widehat X\times\widehat Y\). A bounded \(F\) is weakly constructible up to infinity if \(j_{X!}F\) is weakly constructible on \(\widehat X\).

Equivalently \(Rj_{X*}F\) is weakly constructible there. In one direction apply (30) with \(G=j_{X!}F\); in the other use \(j_{X!}F=k_X\otimes Rj_{X*}F\). Both implications are instances of the preceding tensor/Hom stability. The same equivalence with perfect stalks follows from [perfect operations](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom).

**Theorem.** Let \(f:X_\infty\to Y_\infty\) be such a morphism and \(F\) bounded weakly constructible up to infinity. Then \(Rf_!F\) and \(Rf_*F\) are bounded weakly constructible up to infinity on **\(Y_\infty\)**. For bounded locally constant \(M\) on \(Y\), the natural comparisons on \(Y\) are

\[
\begin{aligned}
Rf_!R\mathcal Hom(f^{-1}M,F)
&\xrightarrow{\sim}R\mathcal Hom(M,Rf_!F),\\
(Rf_*F)\otimes M
&\xrightarrow{\sim}Rf_*(F\otimes f^{-1}M).
\end{aligned}
\tag{31}
\]

**Proof of the image assertion.** Put \(Z=\widehat X\times\widehat Y\), with projections \(q_1,q_2\), and \(\Gamma=\Gamma_f\). The graph is closed in the open \(X\times Y\), so it is locally closed in \(Z\); its subanalytic cutoff \(k_\Gamma\) is constructible with perfect stalks. Define

\[
\begin{aligned}
A(F)&=q_1^{-1}j_{X!}F\otimes k_\Gamma,\\
B(F)&=R\mathcal Hom(k_\Gamma,q_1^!Rj_{X*}F).
\end{aligned}
\tag{32}
\]

These two objects are bounded weakly constructible by the preceding stability theorem. Their closed supports lie in \(\overline\Gamma\), a compact subset of \(Z\), because \(\Gamma\subset X\times Y\) and both factors are relatively compact. Consequently \(q_2\) is proper on these actual supports.

The graph formulas, with their natural maps, are

\[
Rf_!F\simeq j_Y^{-1}Rq_{2!}A(F),\qquad
Rf_*F\simeq j_Y^{-1}Rq_{2*}B(F).
\tag{33}
\]

For the first factor the graph embedding followed by \(q_2\), using ordinary restriction and zero extension. For the second use
\(R\mathcal Hom(k_\Gamma,H)=Ri_{\Gamma*}i_\Gamma^!H\). Exceptional composition identifies \(i_\Gamma^!q_1^!Rj_{X*}F=j_X^!Rj_{X*}F=F\). Restricting to the open \(Y\) then gives ordinary graph-image composition. Open \(j_Y^!\) and \(j_Y^{-1}\) coincide; this does not replace an exceptional inverse image for a general map.

Proper-support image stability makes both ambient images in (33) weakly constructible. Their restriction followed by \(j_{Y!}\) is their tensor with \(k_Y\), hence still weakly constructible. This proves the claim on the target pair. If \(F\) is constructible up to infinity with perfect stalks, every operation in (32), the proper images and the final cutoff preserves perfection by the existing perfect-operation and compact-fibre proofs. Thus both images are constructible up to infinity in this stronger sense as well.

**Proof of the comparisons.** The question is local on the output \(Y\). On a chart where \(M=L_Y\), we can test the canonical maps using the globally constant \(L_Y\): open base change restricts both images to that chart and their inputs to its inverse image. This does not assume a global constant trivialization, or an extension of \(M\) to \(\widehat Y\). Set \(L_Z\) and \(L_{\widehat X},L_{\widehat Y}\) to be the associated constant complexes.

For the first line of (31), (29), the first line of (21), and the first line of (24) with \(P=k_\Gamma\) give

\[
A(R\mathcal Hom(L_X,F))
\simeq R\mathcal Hom(L_Z,A(F)).
\tag{34}
\]

To spell out the order: commute \(j_{X!}\) with Hom from the constant coefficient using (29); commute \(q_1^{-1}\) with that Hom using (21); then move the perfect cutoff \(k_\Gamma\) into its target using (24). Every sheaf here has support in the compact \(\overline\Gamma\).

Internal-Hom direct-image adjunction always identifies
\(Rq_{2*}R\mathcal Hom(q_2^{-1}L_{\widehat Y},A(F))\)
with \(R\mathcal Hom(L_{\widehat Y},Rq_{2*}A(F))\). It follows by tensor–Hom adjunction and ordinary inverse/direct adjunction on each output open set; all operations are bounded. Support properness changes both images of the graph coefficients from \(*\) to \(!\). Equation (33) and open restriction now identify this adjunction map with the first comparison of (31).

For the second comparison, use (29) for \(j_X\), the exceptional line of (21) for \(q_1\), and the second line of (24) with first Hom argument \(k_\Gamma\). They give, in that order,

\[
B(F\otimes L_X)\simeq B(F)\otimes L_Z.
\tag{35}
\]

Projection for \(Rq_{2!}\) with arbitrary \(L\) is invertible; properness on the graph coefficient support identifies it with the ordinary-image projection for \(B(F)\). After (33) and open restriction this is the second comparison of (31). Evaluation and projection in (34)–(35) show that the resulting isomorphisms are the stated canonical maps. Their local forms therefore glue for arbitrary locally constant \(M\). \(\square\)

There is no properness assumption on \(f\) itself. Compact control entered through the graph coefficients in the ambient pair, and is additional information beyond weak constructibility on \(X\).

### Two cohomology comparisons on a relatively compact open set

If \(U\subset X\) is relatively compact, open and subanalytic, \(G\) is bounded weakly constructible on \(X\), and \(L\in D^b(k)\) is arbitrary, then

\[
\begin{aligned}
R\Gamma_c(U;R\mathcal Hom(L_U,G|_U))
&\xrightarrow{\sim}R\operatorname{Hom}_k(L,R\Gamma_c(U;G)),\\
R\Gamma(U;G)\otimes L
&\xrightarrow{\sim}R\Gamma(U;G|_U\otimes L_U).
\end{aligned}
\tag{36}
\]

Apply (31) to \((U,X)\to(\{\mathrm{pt}\},\{\mathrm{pt}\})\). The required ambient extension is \(G\): its zero cutoff on \(U\) is weakly constructible by tensor stability. The graph condition follows from subanalyticity of \(U\). Formula (36) supplies the compact-Hom and ordinary-tensor comparisons. The compact-tensor and ordinary-Hom comparisons (19) already hold without these constructibility or relative-compactness assumptions; the opposite two require the extra control just proved.

### Nonzero locally constant coefficients preserve microsupport over a field

**Theorem.** Suppose \(k\) is a field, \(X\) is connected, \(K\neq0\) is bounded locally constant, and \(F\in D^b(k_X)\) is arbitrary. Then

\[
\operatorname{SS}(K\otimes F)=\operatorname{SS}(F)
=\operatorname{SS}(R\mathcal Hom(K,F)).
\tag{37}
\]

Weak constructibility of \(F\), finite rank of \(K\), and finite dimension of its stalk modules are not needed.

**Proof.** A locally constant complex has microsupport in the zero section. The noncharacteristic tensor and Hom estimates therefore give both upper inclusions in (37), because adding the zero covector or its antipode changes no cotangent direction.

Work on a connected trivializing chart, with \(K=L_U\). Connectedness and \(K\neq0\) imply \(L\neq0\) on every such chart: the set of points with nonzero stalk is both open and closed. Over a field, split the cycles, boundaries and their complements in a complex representing \(L\). This decomposes it in the derived category as its finitely many nonzero cohomology degrees plus a contractible complex. Choose a nonzero vector in one \(H^j(L)\) and split its one-dimensional span. Thus

\[
L\simeq k[-j]\oplus L',\qquad
K\otimes F|_U\simeq F|_U[-j]\oplus(L'_U\otimes F|_U),
\tag{38}
\]

and

\[
R\mathcal Hom(K,F)|_U
\simeq F|_U[j]\oplus R\mathcal Hom(L'_U,F|_U).
\tag{39}
\]

Only a decomposition into two summands was used, even when \(L'\) is infinite dimensional. Microsupport is invariant under shifts and is the union for a finite direct sum: the defining support tests preserve that sum and a retract of a zero test is zero. Hence both right sides have microsupport containing \(\operatorname{SS}(F|_U)\). These lower inclusions are local and glue, proving (37). A global splitting compatible with monodromy is unnecessary. \(\square\)

In particular, extension and coextension by any field extension \(\ell/k\), including one of infinite degree, preserve the microsupport of \(F\). The preceding argument applies to the nonzero locally constant \(k\)-complex \(\ell_X\). Comparing the answer as a sheaf of \(\ell\)-modules or of \(k\)-modules gives the same microsupport: restriction of coefficients is exact and conservative and commutes with the local support tests. For a direct verification it preserves injectives, because its left adjoint \(\ell\otimes_k-\) is exact; the ordinary support subfunctor has the same underlying sections in both coefficient categories. Thus its derived support tests have exactly the same vanishing.

## Further exercises on the comparison hypotheses

### A finite tensor factor and an infinite one behave differently

*Difficulty: Intermediate.*

At a point over a field let \(V=\bigoplus_{n\geq0}k\). Compare the natural maps
\(\operatorname{Hom}_k(V,k)\otimes k^r\to\operatorname{Hom}_k(V,k^r)\) and
\(\operatorname{Hom}_k(V,k)\otimes V\to\operatorname{Hom}_k(V,V)\).
Explain their relevance to (24).

**Solution.** For finite \(r\), a map to \(k^r\) is exactly its \(r\) coordinate functionals, and a finite tensor with \(k^r\) is the same list. The first comparison is therefore invertible, including \(r=0\). A tensor in the second source is a finite sum of vector/functionals and has finite-dimensional image. The identity of \(V\) has infinite-dimensional image and is absent. Since vector spaces are projective, these degree-zero calculations are also the derived comparisons. The first line of (24) allows the perfect finite tensor factor; weak constructibility alone does not permit replacing it by \(V\).

### An infinite boundary accumulation breaks the ordinary tensor comparison

*Difficulty: Advanced.*

Let \(U=(0,1)\subset\mathbb R\), \(S=\{1/n:n\geq2\}\), \(i:S\hookrightarrow U\), and \(F=i_*k_S\) over a field. Let \(V=\bigoplus_{m\geq0}k\). Compute ordinary sections of \(F\) and \(F\otimes V_U\). Show that the second map in (36) fails, and identify its missing hypothesis.

**Solution.** The support \(S\) is closed and locally finite in \(U\), so \(F\) is weakly constructible there with perfect nonzero stalks. Sections on any subset of this discrete support form a product, and restriction just drops coordinates. These sheaves are flabby and have no higher cohomology. Consequently the comparison is

\[
\left(\prod_{n\geq2}k\right)\otimes V
\longrightarrow\prod_{n\geq2}V.
\tag{40}
\]

Every element in its image has all coordinate values contained in one finite-dimensional subspace of \(V\): express its source as a finite sum of tensors. The family whose \(n\)-th coordinate is the basis vector \(e_n\) has no such common finite-dimensional span, so (40) is not surjective. Although \(U\) is relatively compact and subanalytic, \(F\) has no weakly constructible extension to \(\mathbb R\). Such an extension would require a locally finite subanalytic stratification near zero, whereas the nonzero isolated jumps \(1/n\) accumulate there. Thus \(F\) is not weakly constructible up to this boundary. Formula (36) requires an ambient weakly constructible coefficient, not just weak constructibility on \(U\). The support-compact graph proof cannot be applied.

### Connectedness ensures that a nonzero coefficient is present everywhere

*Difficulty: Introductory.*

Let \(X=X_1\sqcup X_2\), with both components nonempty. Put \(K=k_{X_1}\), extended by zero, and let \(F=k_{\{p\}}\) for \(p\in X_2\). Compute both outputs in (37).

**Solution.** This \(K\) is a nonzero locally constant sheaf on the disconnected \(X\). Near \(X_2\) it is zero, so both its tensor with \(F\) and its internal Hom into \(F\) are zero there; near \(X_1\), the target \(F\) is zero. Hence both outputs are zero everywhere, with empty microsupport. The microsupport of \(F\) is the full cotangent fibre at \(p\), including its zero covector. Thus global nonvanishing of \(K\) is insufficient on a disconnected space. The sufficient replacement for connectedness is that \(K\) have a nonzero stalk on every component.

### A nonzero integral coefficient can erase a microsupport

*Difficulty: Intermediate.*

On \(X=\mathbb R\), take \(k=\mathbb Z\), \(K=(\mathbb Z/p)_X\) for a prime \(p\), and \(F=i_*\mathbb Q\) for the point \(i:\{0\}\hookrightarrow X\). Compute \(K\otimes^LF\) and \(R\mathcal Hom(K,F)\). Does perfection of \(K\) replace the field hypothesis in (37)?

**Solution.** The finite free resolution
\([\mathbb Z\xrightarrow{p}\mathbb Z]\) of \(\mathbb Z/p\), in degrees minus one and zero, makes \(K\) perfect. After tensoring with \(F\), multiplication by \(p\) on \(\mathbb Q\) is invertible, so the resulting two-term complex is acyclic. The same finite resolution calculates internal Hom into \(F\), with multiplication by \(p\) in the opposite cohomological degrees; it is also acyclic. Both outputs are zero. The nonzero point coefficient \(F\) has the entire cotangent fibre at zero as its microsupport, so equality fails. The field proof needed a copy of the coefficient unit as a direct summand of a nonzero coefficient complex. A nonzero perfect torsion complex over \(\mathbb Z\) need not contain that unit. Perfection of \(K\) therefore does not substitute for the field hypothesis.
