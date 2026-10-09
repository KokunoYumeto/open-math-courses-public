# Holomorphic operations and complex Fourier symmetries

Holomorphic maps preserve the complex symmetries of the cotangent estimates for sheaf operations. This proves weak complex constructibility even when coefficient modules are infinite. Perfect stalks require the separate real finiteness arguments already developed. Fourier–Sato has one additional issue: its cotangent map moves a covector into a new base vector, so complex cotangent dilation must be transported using both source actions. Microlocal Hom instead uses an analytic normal cone with its own complex normal-fibre scaling.

Let \(k\) be a commutative ring of finite global dimension \(g\). All complex manifolds are Hausdorff, countable at infinity, and of uniformly bounded finite dimension. Maps are holomorphic and vector bundles have fixed finite complex rank. Every sheaf complex is globally bounded. Weak complex constructibility imposes the geometric conditions of [Complex microlocal stratifications and constructibility](complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests); complex constructibility additionally imposes perfect stalks. We assume no Noetherianity, field, noncharacteristic map, or arbitrary support properness.

Use the real covector identification \(\rho(\xi)(v)=\operatorname{Re}\xi(v)\), with \(\alpha=\sum\xi_jdz_j\), \(\Omega=d\alpha\), and real symplectic form \(\operatorname{Re}\Omega\). For a holomorphic differential, real transpose pullback under \(\rho\) agrees with complex-linear transpose pullback. Indeed both real covectors evaluate to \(\operatorname{Re}\xi(df(v))\). We can therefore use the existing real estimates in these complex cotangent coordinates without conjugating the transpose differential.

Kashiwara and Schapira’s *Microlocal Study of Sheaves* gives the real operation results in [Propositions 8.3.3–8.3.6, printed pp. 149–150](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=152), and the complex microsupport criterion in [Theorem 8.5.2, pp. 151–152](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=154). Its analytic closure input, Proposition 8.5.3, continues through p. 154. These are the classical comparisons for the real operation framework and complex conicity. The independent argument below supplies the holomorphic invariance and the uniform boundedness needed for their combination. The exact bounded sheaf estimates, full Fourier microsupport equality, conic Euler criterion and ordered microlocal Hom normal-cone estimate are current prerequisites from the microlocal foundations. This lesson proves the complex constructibility applications.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## The geometric and boundedness contracts

For a bounded object \(H\) on a complex manifold, we will use

\[
H\text{ weakly complex constructible}
\quad\Longleftrightarrow\quad
\operatorname{SS}(H)\subset A
\text{ for a closed complex-conic subanalytic real-isotropic }A.
\tag{1}
\]

Such an \(H\) has actual microsupport closed complex analytic, complex-conic and Lagrangian. “Complex-conic” here refers to cotangent-fibre dilation, not to a vector-bundle dilation on the base of a sheaf.

The real operation theorem in [Weak constructibility under sheaf operations](weak-constructibility-under-sheaf-operations.md#coefficients-bounds-and-the-geometric-criterion) supplies boundedness and weak real constructibility for the operations considered below. It also supplies the finite-dimensional exceptional/direct-image and specialization/Fourier amplitude contracts. For arbitrary bounded Hom inputs on a real manifold \(M\), the bounded-Hom proof gives the explicit sufficient range

\[
A\in D^{[a,b]},\ B\in D^{[c,d]}
\quad\Longrightarrow\quad
R\mathcal Hom(A,B)\in D^{[c-b,\ d-a+3\dim_{\mathbb R}M+g+1]}.
\tag{2}
\]

For a complex \(n\)-manifold this uses \(\dim_{\mathbb R}M=2n\). We use this global bound, not a separate bound chosen independently at every stalk. The perfect real operation theorems in [Perfect operations and finite microlocal coefficients](perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom) and [Perfect coefficients on compact fibres](perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) will supply the perfect-stalk condition.

## Full characteristic inverse image for a holomorphic map

Let \(f:Y\to X\) be holomorphic and \(\Lambda\subset T^*X\) closed complex analytic, complex-conic and isotropic. The full characteristic inverse has the local sequence criterion

\[
\begin{gathered}
y_j\to y,\quad x_j\to f(y),\quad (x_j,\xi_j)\in\Lambda,\\
(df_{y_j})^t\xi_j\to\eta,\qquad
|x_j-f(y_j)|\,|\xi_j|\to0.
\end{gathered}
\tag{3}
\]

The input covectors may be unbounded. Multiplying every \(\xi_j\) by a fixed \(\lambda\in\mathbb C^*\) preserves membership in \(\Lambda\), multiplies the final product by \(|\lambda|\), and changes the output to \(\lambda\eta\), because the transpose differential is complex-linear. Thus \(f^\sharp\Lambda\) is complex-conic.

It is also closed analytic. For completeness, the exact graph-conormal model from [Limiting cotangent sums and characteristic inverse images](limiting-cotangent-sums-and-characteristic-inverse-images.md#the-graph-conormal-and-characteristic-inverse-image) is

\[
P=T^*(Y\times X),\quad L=T^*_{\Gamma_f}(Y\times X),\quad
S=T_Y^*Y\times\Lambda,
\qquad f^\sharp\Lambda=e^{-1}\bigl(KC_L(S)\bigr).
\tag{4}
\]

The first factor is the zero section. The graph is a smooth closed complex submanifold even at critical points of \(f\). The normal identification \(K\), whose inverse is induced by \(-H\), and the zero-conormal-section embedding \(e\) are holomorphic. The [analytic normal-cone argument](analytic-normal-cones-through-complex-deformation.md#reparameterizing-an-arc-to-make-the-scale-positive-real) makes \(C_L(S)\) analytic in its normal bundle. Formula (4) is consequently a closed analytic inverse image. The full real graph-slice theorem proves its real isotropy. This proves every premise of (1); no rank or properness condition on \(f\) was imposed.

For weakly complex constructible \(F\), use the actual \(\Lambda=\operatorname{SS}(F)\) and the [bounded characteristic estimates](../SH02/characteristic-estimates.md#sh02-che-005--ordinary-and-exceptional-inverse-image)

\[
\operatorname{SS}(f^{-1}F)\subset f^\sharp\Lambda,
\qquad \operatorname{SS}(f^!F)\subset f^\sharp\Lambda.
\tag{5}
\]

Boundedness and (1) prove that both inverse images are weakly complex constructible. The ordinary same-base transpose image alone would omit critical escaping directions in (3).

## Proper direct image uses the actual support

Let \(G\) be weakly complex constructible on \(Y\), and assume \(f\) is proper on its closed support. In the holomorphic cotangent correspondence set

\[
C_f=Y\times_XT^*X,
\quad f_d(y,\xi)=(y,(df_y)^t\xi),
\quad f_\pi(y,\xi)=(f(y),\xi).
\tag{6}
\]

For \(\Lambda=\operatorname{SS}(G)\), put \(A=f_d^{-1}\Lambda\). It is closed complex analytic. Over a compact cotangent set \(K\subset T^*X\), every point of \(A\) has \(y\) in the compact set \(\operatorname{supp}(G)\cap f^{-1}(\pi K)\); even a zero transpose covector has this support condition. The preimage of \(K\) is a closed subset of the corresponding compact product with \(K\). Thus \(f_\pi|_A\) is proper. This is the full cotangent compactness check, including points at which \(df\) has a kernel.

[Remmert’s proper mapping theorem](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=118) makes

\[
B=f_\pi f_d^{-1}\Lambda
\tag{7}
\]

closed complex analytic. Both maps commute with complex cotangent dilation. The [real proper cotangent-transport theorem](isotropic-cotangent-transport-and-discrete-critical-values.md#proper-direct-transport) gives real isotropy. The [proper-support sheaf estimate](small-balls-central-fibres-and-supported-cohomology.md#the-proper-image-microsupport-estimate) and (1) now give

\[
\operatorname{SS}(Rf_*G)\subset B,
\qquad Rf_*G\text{ weakly complex constructible}.
\tag{8}
\]

Under the same support properness \(Rf_!G\simeq Rf_*G\), so the same conclusion holds for that functor. A larger cotangent bound with extra base points could violate the properness check and must not be substituted for the actual microsupport in this proof. Holomorphicity by itself does not permit unrestricted nonproper direct image.

## Tensor and Hom use full complex limiting sums

For weakly complex constructible \(F,G\), the [bounded tensor and internal-Hom estimates](../SH02/characteristic-estimates.md#sh02-che-006--tensor-and-internal-hom-without-a-transversality-assumption) are

\[
\begin{aligned}
\operatorname{SS}(F\otimes^LG)&\subset
\operatorname{SS}(F)\widehat+\operatorname{SS}(G),\\
\operatorname{SS}(R\mathcal Hom(G,F))&\subset
\operatorname{SS}(F)\widehat+\operatorname{SS}(G)^a,
\qquad a(x,\xi)=(x,-\xi).
\end{aligned}
\tag{9}
\]

The [analytic limiting-sum proof](complex-microlocal-stratifications-and-constructibility.md#why-the-full-limiting-conormal-sum-is-analytic) from the complex stratification lesson applies to any closed analytic isotropic inputs: its product is analytic and its diagonal normal-cone slice is holomorphic. It is not restricted to ordinary smooth conormals. Multiplying both input covectors by the same complex scalar proves target complex conicity in the full sequence criterion. The antipode is holomorphic and preserves isotropy, changing \(\alpha\) by a minus sign. Hence both right sides of (9) are closed analytic, complex-conic and real-isotropic. With the actual boundedness contracts, (1) proves weak complex constructibility of tensor and internal Hom.

No transversality is needed. The first Hom input carries the antipode. For infinite weak coefficients we used the actual internal-Hom estimate; we have not substituted tensor with a dual, or replaced a Hom stalk by Hom of two ordinary stalks.

## Perfect coefficients after the weak geometric proof

If all relevant inputs are complex constructible, every output just considered also has perfect stalks. Here are the separate finiteness mechanisms.

Ordinary inverse image has stalk \((f^{-1}F)_y=F_{f(y)}\). Proper-on-support direct image has perfect stalks by the finite compact-fibre theorem applied in the underlying real analytic manifolds. Fibres may be singular; that theorem uses the compact supported constructible coefficient complex and finite subanalytic descent, not smoothness of the fibre.

Tensor stalks are tensors of perfect \(k\)-complexes, with a bounded finite-projective total tensor representative. For exceptional inverse and Hom use the actual constructible Verdier evaluation and normalized identities

\[
f^!F\simeq D_Y(f^{-1}D_XF),\qquad
R\mathcal Hom(G,F)\simeq D_X(D_XF\otimes^LG).
\tag{10}
\]

The real constructible duality theorem preserves perfection. These comparisons carry their evaluation maps and the usual Koszul symmetry. They are invoked for perfect constructible inputs; the weak proof above does not need biduality of an infinite coefficient module. A complex \(n\)-manifold has its canonical real orientation, so \(\omega_X\simeq k_X[2n]\); a general holomorphic map still does not have \(f^!\) equal to a universally shifted \(f^{-1}\).

Together with the already proved complex geometry, these finiteness facts give complex constructibility of ordinary and exceptional inverse images, proper-on-support direct image, tensor and internal Hom.

## The two complex Fourier actions

Let \(E\to Z\) be a holomorphic vector bundle of complex rank \(r\), with complex dual \(E^*\). The real dual is identified with this complex dual by the real part of the pairing. Let \(F\) be bounded, weakly complex constructible on \(E\), and conic as a sheaf under **positive real bundle dilation**. This last hypothesis is a sheaf condition on its cohomology along positive radial orbits, including the fixed zero-section orbits. No complex equivariant structure on the sheaf is assumed.

Its actual microsupport \(\Lambda\) is closed analytic and complex-conic. In a holomorphic frame, write \((z,v;\zeta,\eta)\) for a cotangent point and put

\[
\theta(z,v;\zeta,\eta)=\langle v,\eta\rangle\in\mathbb C.
\tag{11}
\]

The [real conic Euler theorem](../SH02/microsupport-operations.md#sh02-mo-conic-test--the-euler-equation-detects-conic-sheaves) says \(\operatorname{Re}\theta=0\) on \(\Lambda\), and that \(\Lambda\) is invariant under positive bundle lifts as well as positive cotangent dilation. Complex cotangent invariance additionally puts \(i\) times every covector in \(\Lambda\). Testing its Euler equation gives \(\operatorname{Re}(i\theta)=-\operatorname{Im}\theta=0\). Hence

\[
\theta|_\Lambda=0\quad\text{as a complex-valued function}.
\tag{12}
\]

The two actions, now with complex parameters, are

\[
\begin{aligned}
r_\lambda(z,v;\zeta,\eta)&=(z,v;\lambda\zeta,\lambda\eta),\\
s_\mu(z,v;\zeta,\eta)&=(z,\mu v;\zeta,\mu^{-1}\eta),
\qquad \lambda,\mu\in\mathbb C^*.
\end{aligned}
\tag{13}
\]

The first preserves \(\Lambda\) by complex constructibility. The second preserves it for positive real \(\mu\) by the conic sheaf criterion. It preserves it for every complex \(\mu\) as well: for a fixed point of \(\Lambda\), the holomorphic orbit map \(\mu\mapsto s_\mu p\) has analytic inverse image of \(\Lambda\) in \(\mathbb C^*\). That inverse image contains the positive real axis. The identity theorem on the connected complex curve makes it the whole curve. Applying the same reasoning to \(\mu^{-1}\) gives set invariance. This extends the microsupport symmetry; it does not assert trivial monodromy of the sheaf along a complex orbit.

## Holomorphic Fourier exchange and its cotangent conicity

The Fourier cotangent map is

\[
\Phi_E(z,v;\zeta,\eta)=(z,\eta;\zeta,-v),
\qquad \Phi_E^*\alpha_{E^*}=\alpha_E-d\theta.
\tag{14}
\]

The formula is holomorphic. Its intrinsic base map is restriction to the vertical cotangent followed by projection to \(E^*\). The canonical-form identity determines the remaining covector coordinates uniquely in every holomorphic frame, so the formulas agree when the frame changes; no horizontal splitting was chosen. Taking real parts identifies this map with the real Fourier cotangent map. Taking exterior derivatives makes it symplectic.

Direct substitution gives the identities for complex parameters

\[
\Phi_Er_\lambda=r_\lambda s_\lambda\Phi_E,
\qquad \Phi_Es_\mu=s_{\mu^{-1}}\Phi_E,
\qquad r_\lambda\Phi_E=\Phi_Er_\lambda s_\lambda.
\tag{15}
\]

Therefore \(\Phi_E\Lambda\) is complex-conic in the **target cotangent fibre**, using both source actions. The map does not commute with cotangent dilation alone: that action changes the target base coordinate \(\eta\).

The image is closed complex analytic because \(\Phi_E\) is a biholomorphism. Equation (12) makes \(d\theta\) vanish on regular tangent vectors of \(\Lambda\); (14) and source isotropy thus give target isotropy. In rank zero, \(\theta=0\) and \(\Phi_E\) is the identity, so the same assertions have no exception.

We use the real Fourier–Sato convention

\[
F^\wedge=Rq_!\bigl(p^{-1}F\otimes
k_{\{\operatorname{Re}\langle v,\eta\rangle\le0\}}\bigr),
\qquad
\operatorname{SS}(F^\wedge)=\Phi_E\operatorname{SS}(F).
\tag{16}
\]

Here \(p,q\) are the two projections of \(E\times_ZE^*\). The [full bounded conic Fourier theorem](../SH02/microsupport-operations.md#sh02-mo-fs-ss--fourier-transformation-of-microsupport) includes both zero loci and gives the equality. The analytic image and (15), or (1), prove weak complex constructibility of \(F^\wedge\). The [real Fourier perfection theorem](perfect-operations-and-finite-microlocal-coefficients.md#fourier-perfection-by-the-zero-section) gives perfect stalks when \(F\) is complex constructible, proving the perfect assertion as well. Its proof uses the actual zero-section contraction maps on the negative cutoff or positive supported kernel; it does not assume \(q\) is proper on the generally unbounded support in (16).

The fibre has real rank \(2r\). Thus, for example, the constant sheaf on an entire complex fibre transforms to the origin sheaf shifted by \(-2r\), with the canonical complex orientation. Neither the rank nor the kernel sign is to be read as the complex dimension \(r\) in a real Fourier integral.

## Ordered microlocal Hom through an analytic normal-cone bound

Let \(F,G\) be weakly complex constructible on \(X\), and let \(P=T^*X\). The [exact ordered microlocal-Hom estimate](normal-scaling-and-microlocal-hom.md#a-sheaf-of-directional-morphisms-microlocal-hom-estimate) is

\[
\operatorname{SS}(\mu\operatorname{hom}(G,F))
\subset\kappa C\bigl(\operatorname{SS}(F),\operatorname{SS}(G)\bigr)
\subset T^*P,
\qquad \kappa(w)=\iota_w\Omega_P.
\tag{17}
\]

The pair cone is first minus second with positive real scales, based at a common point of \(P\). For a tangent vector \(w=(u,v)\) in coordinates \((z,\xi)\), the convention is \(\kappa(w)=v\,dz-u\,d\xi\). Its inverse is the earlier \(-H\) identification. Thus the order in (17) is the target \(F\) first and the source \(G\) second.

Both input microsupports are analytic. The analytic pair-cone theorem makes the cone in (17) closed complex analytic and complex-conic in its tangent-vector fibres. The holomorphic fibre-linear isomorphism \(\kappa\) makes its image complex-conic in the cotangent fibres of \(P\).

We also need isotropy of that bound. Its exact model uses \(P_1=T^*(X\times X)\), \(L=T^*_{\Delta}(X\times X)\), and the isotropic product \(\operatorname{SS}(F)\times\operatorname{SS}(G)^a\). The [Lagrangian normal-cone theorem](boundary-forms-and-lagrangian-normal-cones.md#the-full-lagrangian-normal-cone-theorem) makes \(KC_L\) of this product real-isotropic. Under \(L\simeq P\), \((x,x;\xi,-\xi)\mapsto(x;\xi)\), it is exactly the image in (17). To check the sign, use \(\delta=y-x\), \(\nu=\eta\), \(s=\xi+\eta\). With the second input antipodal, the position difference is \(-\delta\), the covector difference is \(s\), and \(K\) gives \(s\,dz-(-\delta)\,d\xi\) after the positive scaling. This is \(\kappa\) of the ordered pair difference. The antipode in the product is part of this identification, not an additional antipode to insert into (17).

Boundedness and weak real constructibility of microlocal Hom are supplied by the existing full diagonal-kernel theorem, with its global Hom and finite specialization/Fourier amplitude. Its definition is

\[
\mu\operatorname{hom}(G,F)=
\mu_{\Delta_X}R\mathcal Hom(q_2^{-1}G,q_1^!F).
\tag{18}
\]

Now (1) on the complex manifold \(P\), together with the analytic complex-conic isotropic bound (17), proves weak complex constructibility there. For perfect constructible \(F,G\), the [real microlocal Hom perfection theorem](perfect-operations-and-finite-microlocal-coefficients.md#specialization-and-microlocal-hom) gives perfect output stalks, so the output is complex constructible.

The proof uses the bounded normal-cone estimate directly. The positive real deformation chamber used inside specialization is subanalytic but is not a complex analytic piece; we have not applied holomorphic-operation stability to that chamber. Likewise the exceptional projection in (18) remains present: \(q_1^!F\simeq q_1^{-1}F\otimes q_2^{-1}\omega_X\), with \(\omega_X=k_X[2n]\). This factor controls the normal Fourier degree even though all complex orientations are canonical.

We have proved every weak and perfect assertion of the complex operation theorem: holomorphic ordinary and exceptional inverse image, proper-on-support direct image, tensor, internal Hom, microlocal Hom, and positive-conic Fourier–Sato on a holomorphic vector bundle. General nonproper holomorphic direct images require the further cutoff and curve-base arguments.

## Exercises with complete solutions

In examples asserting a nonempty microsupport, take the coefficient ring to be nonzero.

### A holomorphic ramification keeps escaping inverse directions

*Difficulty: Intermediate.*

Let \(f:\mathbb C_w\to\mathbb C_z\), \(f(w)=w^m\), with \(m\ge2\), and let \(F=k_{\{0\}}\). Compare the ordinary cotangent inverse with the full characteristic inverse, and check complex transpose and the product condition.

**Solution.** Microsupport of the point sheaf is \(T_0^*\mathbb C_z\). The ordinary correspondence requires \(w=0\), and its transpose differential is zero there, so gives only the zero covector. For any complex output coefficient \(\eta\), take positive real \(w_j\to0\), \(z_j=0\), and

\[
\xi_j=\frac{\eta}{m w_j^{m-1}},\qquad
m w_j^{m-1}\xi_j=\eta,\qquad
|z_j-w_j^m|\,|\xi_j|=\frac{|\eta|}{m}|w_j|\to0.
\tag{19}
\]

For \(\eta=0\) the witnesses are zero and still valid. No other base can occur, because input base zero must approach \(f(w)\). Thus \(f^\sharp T_0^*\mathbb C_z=T_0^*\mathbb C_w\). The holomorphic transpose uses \(m w^{m-1}\), without complex conjugation. Ordinary inverse image is the point sheaf, whose full origin microsupport is bounded by this characteristic inverse. Its stalks \(k\) and zero are perfect.

### Tangent complex curves need the full sum

*Difficulty: Advanced.*

In \(\mathbb C^2_{z,w}\), put \(Y=\{w=0\}\), \(Z=\{w=z^2\}\). Compute the tensor of their constant sheaves and produce the limiting-sum covector \(a\,dz+b\,dw\) at their intersection for arbitrary complex \(a,b\).

**Solution.** Stalks of the two coefficient sheaves are \(k\) or zero and are flat, so their derived tensor is \(k_{Y\cap Z}=k_{\{0\}}\). It has the full complex cotangent fibre at zero as microsupport. The ordinary same-base conormal sum there is only the \(dw\) line. For positive real \(t\to0\), take bases \((t,0)\), \((t,t^2)\), parabola coefficient \(\mu=-a/(2t)\), and axis coefficient \(\lambda=b-\mu\). Their conormals are \(\lambda\,dw\) and \(\mu(-2t\,dz+dw)\); their sum is exactly \(a\,dz+b\,dw\). The base gap is \(t^2\), and \(t^2|\lambda|\le |b|t^2+|a|t/2\to0\). This witnesses every complex output covector, including \(a=0\). The full limiting sum supplies the missing directions with no transversality assumption.

### Proper branched pushforward and its cotangent bound

*Difficulty: Intermediate.*

For \(f(w)=w^m\) with \(m\ge2\), take \(G=k_{\mathbb C}\). Determine its direct-image stalks, its local monodromy off zero, and the set (7). Verify perfection and properness.

**Solution.** The polynomial map is proper: a compact target set bounds \(|w|^m\), and its preimage is closed and bounded. Fibres are finite, so proper base change gives cohomology only in degree zero, with stalk \(k^m\) away from zero and \(k\) at zero. A loop around zero cyclically permutes the \(m\) roots, giving that permutation monodromy on \(k^m\). Restrictions from the central constant section give the diagonal map \(k\to k^m\). All these finite free stalks are perfect.

Input microsupport is the zero section. Its correspondence inverse is the condition \(m w^{m-1}\xi=0\), so over \(w\ne0\) it has only zero covectors, and over \(w=0\) it has every complex covector. Projection gives the zero section of the target together with its full origin fibre. This is the closed analytic complex-conic bound (7). The common analytic cover \(\mathbb C^*,\{0\}\) also exhibits weak complex constructibility; perfection gives the strong assertion. Finite-fibre integration inserts no real two-dimensional shift.

### Holomorphic nonproper support can accumulate singular values

*Difficulty: Advanced.*

Let \(f:\mathbb C\to\mathbb C\), \(f(z)=e^z\), and let \(G=\bigoplus_{m\ge1}k_{\{-m\}}\), for a nonzero field \(k\). Show that \(G\) is complex constructible, while \(Rf_*G\) is not weakly complex constructible near zero. Identify the failed hypothesis.

**Solution.** The support is a closed discrete analytic subset of \(\mathbb C\), with no finite accumulation. The locally finite point/open analytic decomposition has stalks \(k\) or zero, hence perfect; thus \(G\) is complex constructible. Sections over any open set are the product of the point coefficients occurring there, and restrictions are surjective. This sheaf is flabby, so is acyclic on every inverse-image open set. Consequently \(Rf_*G=f_*G\).

At each isolated target value \(e^{-m}\), a small target neighborhood isolates that value from all other support images, giving stalk \(k\); on intervening open regions the sheaf is zero. Infinitely many such point jumps approach zero. An analytic μ-stratification of a complex curve is locally a finite set of point strata and open complex strata. Locally constant restriction on the open strata cannot have these accumulating isolated jumps. Therefore condition 1 fails near zero. No assertion that the stalk at zero vanishes is needed; nonproper stalk base change would not be justified there.

Properness on support fails: the inverse image of the compact closed unit disc contains all the support points \(-m\), an unbounded set. Thus (8) is inapplicable. Holomorphicity of \(f\) does not replace its support-properness hypothesis.

### Fourier of a complex linear subspace

*Difficulty: Intermediate.*

In \(E=\mathbb C^r\), let \(L\) be a complex linear subspace of dimension \(d\). Compute \((k_L)^\wedge\) with convention (16), including the real degree, orientation and cotangent sign. Check the case \(d=0\).

**Solution.** For \(\eta\notin L^\perp\), the real linear form \(\operatorname{Re}\eta|_L\) is nonzero: if it were zero on every real vector of the complex space \(L\), testing imaginary multiples would make \(\eta|_L=0\). The allowed part of \(L\) is then a closed real halfspace, whose compactly supported cohomology is zero. For \(\eta\in L^\perp\), it is all of \(L\), of real dimension \(2d\), with compact cohomology \(k[-2d]\). The closed-support Fourier comparison therefore gives

\[
(k_L)^\wedge=k_{L^\perp}[-2d].
\tag{20}
\]

Complex linear transition determinants have positive real determinant \(|\det_{\mathbb C}|^2\), so the orientation factor is canonically trivial. Source conormals have \(v\in L\), \(\eta\in L^\perp\); \(\Phi_E\) sends them to base \(\eta\) with covector \(-v\), the target conormal, including both zero loci. For \(d=0\), the point coefficient transforms to the constant sheaf on all \(E^*\), with shift zero. For \(d=r\), the whole fibre transforms to its origin sheaf shifted by \(-2r\).

### A real ray fails the complex Fourier input condition

*Difficulty: Intermediate.*

Regard the closed positive real ray \(R=\{t\in\mathbb C:t\ge0\text{ real}\}\) as a subset of \(E=\mathbb C\). Compute \((k_R)^\wedge\) and explain why it does not contradict the complex Fourier theorem.

**Solution.** Write \(\eta=a+ib\). On the ray the cutoff is \(at\le0\). If \(a>0\), only \(t=0\) is allowed, with compact cohomology \(k\). If \(a\le0\), the whole closed half-line is allowed and its compact cohomology vanishes. The resulting negative-cutoff comparison is the constant sheaf on the open half-plane \(\{a>0\}\) extended by zero, in degree zero. Its real boundary is not a complex analytic boundary, and its microsupport at that boundary is not complex-conic.

Although \(k_R\) is positive-conic and real constructible, it is not weakly complex constructible: on the nonzero ray its real conormal is not invariant under complex cotangent dilation. Thus it fails the input complex condition. The kernel in (16) is real; analyticity of the output follows from both symmetries of a valid input microsupport, not from analyticity of this inequality.

### The exceptional diagonal degree cancels a real normal Fourier degree

*Difficulty: Advanced.*

For constant inputs \(F=G=k_X\) on a complex \(n\)-manifold, compute \(\mu\operatorname{hom}(k_X,k_X)\) from (18). Retain the exceptional projection and the real normal rank, and identify its support.

**Solution.** Canonical complex orientation gives \(q_1^!k_X=k_{X\times X}[2n]\). The internal Hom from \(q_2^{-1}k_X\) is therefore this same constant kernel shifted by \(2n\). Specialization along the diagonal keeps the constant sheaf on the real normal bundle with that shift. Its real normal rank is \(2n\), and Fourier of the entire normal fibre is its zero-section coefficient shifted by \(-2n\), with canonical complex orientation. The shifts cancel. Hence the result is \(k_{T_X^*X}\), the zero-section constant sheaf extended to \(T^*X\), in degree zero. Off that zero section it vanishes. Dropping \(q_1^!\)'s degree would instead give an incorrect \(-2n\) shift; using complex rank \(n\) for the real Fourier degree would also fail.

### Perfect torsion coefficients keep opposite derived degrees

*Difficulty: Intermediate.*

At a closed point of a complex manifold, take coefficients \(A=\mathbb Z/m\), \(B=\mathbb Z/n\), with \(m,n>1\), and \(d=\gcd(m,n)\). Compute their derived tensor and internal Hom cohomology. Explain why degree-zero coefficients alone do not verify the operation theorem.

**Solution.** The finite free resolution \([\mathbb Z\xrightarrow{m}\mathbb Z]\) of \(A\), in degrees \(-1,0\), gives tensor complex \([B\xrightarrow{m}B]\) in those same degrees. Its kernel and cokernel are \(\mathbb Z/d\), so tensor has this group in degrees \(-1\) and zero. Applying Hom gives the two-term complex in degrees zero and one, with differential \(\pm m\); both cohomology groups are again \(\mathbb Z/d\). For point-supported sheaves these are the corresponding supported coefficient complexes: closed-embedding adjunction identifies Hom on that support with coefficient Hom, and tensor is stalkwise.

Both outputs are perfect, using finite-projective representatives of the two inputs. The derived terms in opposite degrees are part of the theorem and cannot be omitted by replacing tensor or Hom with only its ordinary degree-zero functor. No complex manifold dimension shift is added to these point-supported coefficient operations.

## Remaining scope

The complex operation applications and their independent weak/perfect hypotheses are proved relative to the stated current microlocal and real finiteness contracts. The general complex derived-realization phenomenon and nonproper cutoff and complex-curve direct-image theorem require further arguments; they are not consequences of unrestricted holomorphic pushforward stability.

## Readable source and dependency account

A holomorphic differential commutes with complex cotangent dilation, but the Fourier cotangent map exchanges a fibre covector with a base vector. The proof therefore uses both complex scaling actions, not just conicity in the original cotangent fibre. Microlocal Hom is handled through the complex normal cone while retaining the exceptional projection’s orientation shift. The positive real deformation chamber is not incorrectly declared a complex analytic stratum. Perfect coefficients are obtained only after the weak geometric theorem by the separate real finiteness and duality providers.

**Real and complex constructibility.** Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=152), Propositions 8.3.3–8.3.6, printed pp. 149–150, treat inverse operations, specialization, Fourier transformation, tensor and internal Hom. [Theorem 8.5.2 and Proposition 8.5.3](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=154), pp. 151–154, supply the complex microsupport criterion and its analytic closure argument. The linked programme proofs keep the characteristic limits, coefficient bounds and perfect-stalk hypotheses explicit.

**Fourier normalization.** Pierre Schapira’s [*An Introduction to Sheaves on Grothendieck Topologies*, edition dated 01/08/2026, Definitions 5.4.4–5.4.5 and Example 5.4.7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=114), pp. 114–115, give positive-orbit conicity, the negative-cut/positive-support presentations and the real-dimensional orientation shifts. His [*A short review on microlocal sheaf theory*, 19 January 2016, Definition 4.1 and Example 4.3](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=19), pp. 19–20, use these same conventions. Their stated Fourier equivalences refer to the book treatment; the actual programme proof used in (16) includes the zero-direction stabilization and inversion step.

**Microlocal Hom and signs.** The same [2016 review, Definition 4.5 and Theorem 4.7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=23), pp. 23–24, gives the exceptional diagonal kernel and normal-cone estimate; equation (4.9), p. 25, gives the Fourier cotangent exchange. Its [ordered cone and Hamiltonian conventions](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=5), pp. 5–6, put the source set first before applying the Hamiltonian inverse. Reversing the pair and using the negative Hamiltonian inverse gives exactly (17). The lesson’s target-first order and its displayed normal identification therefore agree with that source.

**Proper analytic image.** Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, 21 June 2012, Chapter II, Theorem 8.8](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=118), pp. 118–121, proves the proper mapping theorem by simultaneous induction with the extension theorem. This is the analytic-image prerequisite in (7), applied only after the support compactness check. The theorem’s analytic local algebra and extension foundations remain separate inputs.

These citations identify the human antecedents and their exact roles. Original programme exposition remains CC0; the human works retain their own rights.
