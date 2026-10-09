# Complex stalk–costalk Euler numbers and function duality

The difference between a point costalk and a stalk is measured by the cohomology of a punctured neighborhood. We replace that neighborhood by the punctured tangent specialization, keeping the maps in the localization triangle. The resulting complex is constant along positive rays and locally constant along complex scalar orbits. Its link projects properly onto projective space with circle fibres. Each circle has Euler number zero, including with nontrivial monodromy, so the costalk and stalk have the same integer Euler number. This proves that duality fixes complex constructible functions over the coefficient domain in which function duality was defined.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

The proof uses four comparisons. [Complex nearby cycles as normal and conormal sections](../../nearby-cycles-monodromy-and-specialization/src/complex-nearby-cycles-as-normal-and-conormal-sections.md#complex-constructibility-survives-specialization) proves complex constructibility of specialization, while [perfect specialization](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#specialization-and-microlocal-hom) proves its coefficient finiteness through the real deformation chamber. [The complex Euler annihilator](../../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#the-two-complex-fourier-actions), [horizontal submersion descent](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-submersion--exact-pullback-and-local-descent) and [whole-complex interval descent](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) control scalar orbits. [Perfect cohomology on compact fibres](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) supplies the finite complexes on the sphere and projective space. Finally, [the stalk–costalk dual pairing](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#duality-exchanges-the-measurements-before-biduality) and [function duality](constructible-functions-and-euler-integration.md#duality-is-an-open-ball-euler-integral) turn the local calculation into a statement about functions. The finite-cell argument below also explains the integer Euler calculation used in [Euler numbers and vector-field indices](euler-numbers-and-vector-field-indices.md#finite-cells-give-an-integer-independent-of-the-field).

The point comparisons come from [Reading a sheaf at the normal scale](../../sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-zero--what-survives-when-the-direction-is-forgotten). We specify its ordinary unit, exceptional counit and their localization compatibility below. Its coefficient domain includes every field. Positive radial contraction uses [restriction to the zero section](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-radial-star--ordinary-contraction-to-the-zero-section); the orbit calculation uses ordinary sections along a contractible interval. The compact sphere projection is the proper map in the proof.

## Integer Euler numbers and the point-specialization maps

Let \(k\) be any field. For a perfect coefficient complex \(P\), set

\[
 \chi(P)=\sum_j(-1)^j\dim_k H^j(P)\in\mathbb Z.
 \qquad\text{(1)}
\]

The sum is finite, and it is additive in distinguished triangles. Dualizing a finite complex over \(k\) reverses cohomology degrees and preserves (1). These are integer calculations in every characteristic.

Let \(X\) be a complex analytic manifold of complex dimension \(d\), Hausdorff and countable at infinity. More generally, component dimensions may vary under one finite bound, and the proof uses the dimension of the component containing the chosen point. Let
\(F\in D^b_{\mathbb C\text{-c}}(k_X)\) be globally bounded with finite-dimensional cohomology stalks, locally constant on a locally finite complex analytic stratification. Over a field this is the perfect-stalk condition. Neither \(X\) nor the closed support of \(F\) is required to be compact; stalk ranks need not have one global bound. Fix \(x\in X\), and write \(i:\{x\}\hookrightarrow X\). Specialize at that point:

\[
 V=T_xX,\qquad K=\nu_xF,\qquad e:\{0\}\hookrightarrow V,
 \qquad
 e^{-1}K\simeq F_x,\quad e^!K\simeq i^!F.
 \qquad\text{(2)}
\]

Here are the actual arrows in (2). In the deformation to \(x\), write \(p:\widetilde X_x\to X\), \(\Omega=\{t>0\}\), \(j_+:\Omega\hookrightarrow\widetilde X_x\), \(r=p|_\Omega\), and \(s:V\hookrightarrow\widetilde X_x\). Then \(K=s^{-1}Rj_{+*}r^{-1}F\). The ordinary unit gives

\[
u_F:F_x=(s e)^{-1}p^{-1}F
 \longrightarrow e^{-1}s^{-1}Rj_{+*}r^{-1}F=e^{-1}K.
\]

The ordinary conic contraction is the restriction map
\(\rho_K:R\Gamma(V;K)\to e^{-1}K\).
Its proof compares sections on the whole vector space with sections on all balls, then takes their stalk colimit; it does not use properness of \(V\to\{*\}\). For \(u_F\), the specialization section formula on the entire normal space has as its admissible original sets precisely the neighborhoods of \(x\). Their ordinary-section colimit is \(F_x\). The map induced by the displayed unit is the same restriction-to-germs map, proving \(u_F\) invertible. Thus the identification of ordinary sections with \(F_x\) is \(u_F^{-1}\rho_K\).

The positive-parameter boundary triangle gives \(K\simeq s^!j_{+!}r^!F\). Its exceptional counit is

\[
c_F:e^!K\simeq e^!s^!j_{+!}r^!F
 \longrightarrow e^!s^!p^!F\simeq i^!F.
\]

To verify this particular arrow, first apply the supported neighborhood formula to the counit \(i_*i^!F\to F\). Closed supports whose normal cone lies in the zero section reduce, near \(x\), to supports contained in \(\{x\}\): otherwise normalize a sequence of nonzero approaching vectors and take a limit on the unit sphere. This produces a nonzero normal direction, a contradiction. The resulting colimit has terms \(R\Gamma_{\{x\}}(U;F)\); the counit induces isomorphisms on these terms by idempotence of sections supported at \(x\). Thus \(e^!\nu_x(i_*i^!F)\to e^!K\) is an isomorphism. It remains to calculate the counit for a point coefficient \(i_*P\). On the zero-normal parameter axis it is the endpoint counit for \(P\boxtimes k_{(0,\infty)}[1]\). The positive parameter contributes \([1]\), the endpoint costalk contributes \([-1]\), and the connecting morphism in the closed/open triangle identifies their composite with \(\operatorname{id}_P\). Naturality for \(i_*i^!F\to F\) now proves that \(c_F\) is an isomorphism. This fixes (2) without inserting a dimension shift or an independent orientation scalar.

There are two distinct constructibility checks. For perfection, \(p\) is real analytic and the positive chamber is subanalytic. The actual open-adjunction identity

\[
Rj_{+*}j_+^{-1}p^{-1}F
 \simeq R\mathcal Hom(k_\Omega,p^{-1}F)
\]

allows perfect internal Hom and ordinary restriction by \(s\) to give a bounded real constructible \(K\) with perfect stalks. For complex constructibility use the bounded specialization estimate in the nearby-cycle provider. It bounds \(\operatorname{SS}(K)\) by the analytic isotropic normal cone of \(\operatorname{SS}(F)\) along \(T_x^*X\), under its holomorphic normal/cotangent identification. In its sequence description, multiplying every original covector by \(\lambda\in\mathbb C^*\) multiplies the limiting output covector by \(\lambda\) and leaves its base vector fixed. The bound is therefore complex-conic in the required cotangent fibres, and the complex constructibility criterion applies. Real scaling in the deformation separately proves positive conicity. The positive real chamber itself has not been declared complex analytic. All these arguments apply over every field.

## Both radial directions are invisible to the microsupport

Write a real cotangent covector as the real part of a complex covector \(\xi\), and put \(\Lambda=\operatorname{SS}(K)\). Positive conicity and the real Euler criterion give
\(\operatorname{Re}\langle v,\xi\rangle=0\) on \(\Lambda\). Complex constructibility also puts \(i\xi\) in \(\Lambda\). Applying the same criterion to \(i\xi\) gives the imaginary part:

\[
 \operatorname{Re}\langle v,\xi\rangle=0,\qquad
 \operatorname{Re}\langle v,i\xi\rangle
       =-\operatorname{Im}\langle v,\xi\rangle=0,
 \qquad
 \langle v,\xi\rangle=0.
 \qquad\text{(3)}
\]

Hence every covector of \(\Lambda\) annihilates both \(v\) and \(iv\). The quotient coordinates can be written explicitly. At \(v_0\ne0\), choose a complex-linear form \(\ell\) with \(\ell(v_0)\ne0\), and put \(H=\{\ell=1\}\). The biholomorphism

\[
H\times\mathbb C^*\longrightarrow\{\ell\ne0\},\qquad
(h,\lambda)\longmapsto\lambda h
\]

has inverse \(v\mapsto(v/\ell(v),\ell(v))\). In a small product chart its vertical real tangent is spanned by \(h,ih\). Equation (3) says precisely that the pulled-back microsupport has zero covector component in that scalar coordinate. Horizontal submersion descent consequently makes the entire bounded complex locally a pullback from \(H\); in particular its cohomology restricts to local systems on every scalar orbit. Covering an orbit with these charts proves local constancy all around it, but does not identify its continuation around a loop with the identity. No generic hyperplane or noncharacteristic inclusion of the entire \(H\) is being assumed: the map just used is a coordinate isomorphism followed by a submersion.

Choose a Hermitian norm and let \(S\) be its unit sphere. The real analytic polar homeomorphism is

\[
 (0,\infty)\times S\xrightarrow{\sim}V\setminus\{0\},
 \qquad(r,s)\longmapsto rs,\qquad L=K|_S.
 \qquad\text{(4)}
\]

Let \(b:(0,\infty)\times S\to V\setminus\{0\}\) be (4), let \(\pi\) be projection to \(S\), and let \(s_1(s)=(1,s)\). Put \(B=b^{-1}(K|_{V\setminus\{0\}})\). The parameter \(\log r\) identifies its positive radial fibres with \(\mathbb R\). Interval descent supplies the actual evaluation and counit isomorphisms

\[
R\pi_*B\longrightarrow s_1^{-1}B=L,\qquad
\pi^{-1}R\pi_*B\longrightarrow B.
\]

The inverse counit followed by pullback of evaluation gives \(B\simeq\pi^{-1}L\), normalized to identity at radius one. Ordinary direct-image composition then gives
\(R\Gamma(V\setminus\{0\};K)\simeq R\Gamma(S;L)\).
This comparison concerns the whole complex and imposes no angular trivialization. It is ordinary radial descent, not compact-support integration along \((0,\infty)\), so it inserts no shift.

The radial boundary is also controlled directly by (3). For \(\rho(v)=\|v\|^2\) and \(v\ne0\), one has \(d\rho_v(v)=2\|v\|^2>0\). Thus no nonzero real multiple of \(d\rho_v\) belongs to \(\Lambda\). Every positive-radius sphere is noncharacteristic for this conic complex. This explains why changing the radius introduces no extra local jump; the specified interval maps above give the stronger comparison of the entire section complexes.

## A circle contributes zero even with monodromy

Let \(A\) be a rank-\(r\) local system on a circle. Cutting at one vertex gives its cellular cochain complex

\[
 k^r\xrightarrow{T-I}k^r,
 \qquad
 H^0(S^1;A)=\ker(T-I),\quad
 H^1(S^1;A)=\operatorname{coker}(T-I),
 \qquad\text{(5)}
\]

Here the two terms are in degrees zero and one, and \(T\) is the invertible transport after one positively oriented turn. One can obtain this complex by cutting the circle at a vertex, trivializing on the remaining interval, and identifying its two endpoint fibres by \(T\). The endpoint difference is \(T-I\); reversing the orientation gives an isomorphic complex. Equivalently, the two-arc Čech complex eliminates one identity restriction and leaves this differential. Intervals and their overlap intervals have no higher cohomology for a local system, so this computation gives the derived section complex and there are no other cohomology groups. Rank-nullity gives
\(\dim\ker(T-I)=r-\operatorname{rank}(T-I)=\dim\operatorname{coker}(T-I)\).
Therefore \(\chi(R\Gamma(S^1;A))=0\) as an integer in every characteristic.

For a bounded complex \(B\) with finite locally constant cohomology on the circle, the finite hypercohomology spectral sequence gives

\[
 \chi(R\Gamma(S^1;B))
   =\sum_j(-1)^j\chi(R\Gamma(S^1;H^j(B)))=0.
 \qquad\text{(6)}
\]

Indeed its cohomology-sheaf rows are confined to finitely many \(j\), and the circle columns are zero and one. Passing from any page to the next preserves the alternating dimension sum: the image of a differential cancels in its two adjacent total degrees. The limit filtration has the same sum. Formula (5) makes each row sum zero. This proves (6) for the entire bounded complex, retaining its extension data.

## Proper circle fibres make the whole link Euler number zero

Assume \(d\ge1\). The Hopf projection is

\[
 q:S\longrightarrow\mathbb P(V)\simeq\mathbb{CP}^{d-1},
 \qquad q(s)=\mathbb C s.
 \qquad\text{(7)}
\]

It is proper because \(S\) is compact. Each fibre is the unit circle in its complex line. In the chart of lines with a specified nonzero coordinate, represent the line by a vector with that coordinate one, normalize its length, and multiply it by a unit complex number. This gives a local product with a circle and proves that \(q\) is a real analytic submersion.

Ordinary inverse image to the real analytic sphere makes \(L\) bounded and real constructible with perfect stalks. The map \(q\) is real analytic and proper on all of \(S\), hence on the closed support of \(L\). The proper constructible direct-image theorem therefore makes \(Q=Rq_*L=Rq_!L\) bounded and perfect constructible on compact projective space. If \(L\) has cohomology in degrees \([a,b]\), restriction to a circle has locally constant finite cohomology in those degrees. Its hypercohomology lies in \([a,b+1]\), giving one uniform bound for the stalks of \(Q\). Proper base change is the restriction of sections to the compact fibre, and gives

\[
 Q_\ell\simeq R\Gamma(q^{-1}(\ell);L),\qquad
 \chi(Q_\ell)=0\quad(\ell\in\mathbb P(V)).
 \qquad\text{(8)}
\]

The second equality is (6), because that fibre is contained in one complex scalar orbit.

Here is the finite filtration that passes from the stalk values to the global value. Write \(P=\mathbb P(V)\), choose a finite compatible triangulation, and let \(P_a\) be its closed \(a\)-skeleton, with \(P_{-1}=\varnothing\). Put \(U_a=P_a\setminus P_{a-1}\), \(j_a:U_a\hookrightarrow P_a\), and \(Q_a=Q|_{P_a}\). The triangle

\[
j_{a!}j_a^{-1}Q_a\longrightarrow Q_a
\longrightarrow (P_{a-1}\hookrightarrow P_a)_*Q_{a-1}\xrightarrow{+1}
\]

gives a triangle of perfect section complexes on the compact skeleton. Its first term has section complex \(R\Gamma_c(U_a;Q|_{U_a})\), because extension by zero followed by the map from the compact \(P_a\) is the proper-support map from \(U_a\). There are finitely many open simplices. On each simplex \(\tau\) of dimension \(a\), the cohomology sheaves of \(Q\) are constant, and compact cohomology of a rank-\(r\) constant coefficient is \(k^r[-a]\). Truncation, or the finite hypercohomology filtration, thus gives
\(\chi R\Gamma_c(\tau;Q)=(-1)^a\chi(Q_{\ell_\tau})\).
Iterating the finitely many skeleton triangles yields

\[
 \chi(R\Gamma(\mathbb P(V);Q))
   =\sum_{\tau}(-1)^{\dim\tau}\chi(Q_{\ell_\tau})=0.
 \qquad\text{(9)}
\]

Here \(\ell_\tau\) is any point of that open simplex. This is a finite integer sum. A derived splitting of \(Q\) was never required.

Composition of ordinary direct images, (4), and (9) now give

\[
 \chi(R\Gamma(V\setminus\{0\};K))
       =\chi(R\Gamma(S;L))=0.
 \qquad\text{(10)}
\]

For \(d=0\), the punctured vector space is empty and (10) holds directly.

## The point-localization triangle proves the Euler equality

Let \(j:V\setminus\{0\}\hookrightarrow V\). Apply ordinary sections to the canonical triangle
\(e_*e^!K\to K\to Rj_*j^{-1}K\xrightarrow{+1}\).
Its first arrow is the closed-embedding counit and its second is the open-adjunction unit. Since the first object is supported at zero, its ordinary sections are \(e^!K\). Ordinary composition identifies the third term with sections on the punctured vector space. We obtain

\[
 R\Gamma_{\{0\}}(V;K)
       \longrightarrow R\Gamma(V;K)
       \longrightarrow R\Gamma(V\setminus\{0\};K)
       \xrightarrow{+1}.
 \qquad\text{(11)}
\]

The first two terms are perfect through (2) and the actual conic restriction map; the third is the perfect cohomology of the compact sphere through (4). These statements supply finiteness on the noncompact vector space without assuming a finite global cohomology theorem for arbitrary noncompact supports.

The identifications also preserve the first arrow. Specialize the support counit \(i_*i^!F\to F\), using \(\nu_x(i_*i^!F)\simeq e_*i^!F\). Its adjoint \(\sigma:i^!F\to e^!K\) satisfies \(c_F\sigma=\operatorname{id}\) by the endpoint normalization above, so \(\sigma=c_F^{-1}\). Naturality of \(u_F\) for that same support counit identifies the supported-to-ordinary map with \(i^!F\to F_x\). Hence the third term of (11) also identifies with the actual punctured-neighborhood germ \(i^{-1}Ra_*a^{-1}F\), where \(a:X\setminus\{x\}\hookrightarrow X\). No unrelated isomorphisms of the two point complexes have been substituted into the triangle. Euler additivity and (10) now prove the theorem:

\[
 \boxed{\chi(i^!F)=\chi(F_x)
       \qquad\text{for every }x\in X\text{ and every field }k.}
 \qquad\text{(12)}
\]

For a point embedding, \(R\Gamma_{\{x\}}(X;F)=R\Gamma(X;i_*i^!F)\) is precisely the coefficient complex \(i^!F\). Thus (12) also computes the integer Euler number of point-supported cohomology. Excision makes this a local assertion at \(x\). It requires neither finite cohomology on all of \(X\) nor any properness of the map \(X\to\{*\}\).

The proof preserves the actual specialization maps and the angular monodromy, and uses integer dimensions throughout. It applies to arbitrary finite perfect coefficients along the strata, without demanding trivial scalar-orbit monodromy.

## Duality fixes the complex constructible function

Take \(D_XF=R\mathcal Hom(F,\omega_X)\). The evaluation pairing on an open neighborhood \(U\) gives
\(R\Gamma(U;D_XF)\simeq R\operatorname{Hom}_k(R\Gamma_c(U;F),k)\).
For small coordinate balls, the actual map \(i^!F\to R\Gamma_c(U;F)\) is an isomorphism; it is inclusion of point support followed by compact extension, and it commutes with shrinking-ball extensions. Dualizing this represented neighborhood system and taking the ordinary stalk gives the actual stalk–costalk pairing

\[
 (D_XF)_x\simeq R\operatorname{Hom}_k(i^!F,k).
 \qquad\text{(13)}
\]

Coefficient duality preserves the Euler number in (1), so (12) gives

\[
 \chi_X(D_XF)(x)=\chi(i^!F)=\chi_X(F)(x).
 \qquad\text{(14)}
\]

Let \(\varphi\) be an integer-valued complex constructible function, constant on the strata of a locally finite complex analytic stratification. Its values may be unbounded on a noncompact \(X\). The characteristic-zero Grothendieck construction in the function lesson defines \(D_X\varphi\) and proves it independent of a representative. Its germ-local formula is
\((D_X\varphi)(x)=\chi(i^!F)\) for any local realization \(\chi_X(F)=\varphi\). We use \(k=\mathbb Q\) for that application. The theorem (12) itself continues to hold over the arbitrary field fixed at the beginning.

Here such a realization can be chosen complex constructible. Near a given point choose a neighborhood meeting only finitely many strata \(S_\alpha\), and let \(n_\alpha=\varphi|_{S_\alpha}\). With extension by zero from each locally closed stratum, take

\[
 F=
 \bigoplus_{n_\alpha>0} k_{S_\alpha}^{\,n_\alpha}
 \ \oplus\
 \bigoplus_{n_\alpha<0} k_{S_\alpha}^{\,-n_\alpha}[1].
 \qquad\text{(15)}
\]

The sum is finite on the chosen neighborhood, has cohomology only in degrees \(-1,0\), and is complex constructible: each locally closed stratum coefficient is \(k\) on that stratum and zero on the other strata. Its Euler function is \(\varphi\), with \([1]\) supplying the negative weights. Its closed sheaf support is exactly the closure of the nonzero-value locus in that neighborhood. If desired, the same construction on all strata is a locally finite sheaf sum and gives one globally bounded realization even when infinitely many strata or weights occur. This is a construction of sheaves, not an infinite sum of Grothendieck classes. Local realizations already suffice because point costalks and function duality commute with open restriction. Formula (14) therefore proves

\[
 \boxed{D_X\varphi=\varphi.}
 \qquad\text{(16)}
\]

For the function operation one may use \(\mathbb Q\) in (15), within its existing Grothendieck/function definition. The stalk–costalk theorem itself was proved over every field. Neither conclusion identifies a sheaf complex with its Verdier dual: the equality records integer Euler data, and examples below retain the different complexes.

## Exercises with complete solutions

### A shifted unipotent circle coefficient
*Difficulty: Introductory.*

Over any field take the rank-two circle local system with monodromy
\(T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\). Compute the cohomology and Euler number of \(R\Gamma(S^1;A[1])\), including in characteristic two.

**Solution.** The matrix \(T-I\) has rank one in every field. Both its kernel and its cokernel have dimension one. Thus \(R\Gamma(S^1;A)\) has one-dimensional cohomology in degrees zero and one. Shifting by \([1]\) moves them to degrees minus one and zero. The integer Euler number is \(-1+1=0\). The nontrivial monodromy and the characteristic-two Jordan matrix do not alter this calculation.

### The two extensions from a punctured disk
*Difficulty: Advanced.*

Let \(j:\Delta^*\hookrightarrow\Delta\) be a punctured complex disk, and let \(A\) have invertible monodromy \(T\) on a finite-dimensional space \(W\). Compare the stalk and costalk Euler numbers at zero of \(j_!A\) and \(Rj_*A\).

**Solution.** Put \(C=[W\xrightarrow{T-I}W]\) in degrees zero and one. Radial interval descent computes punctured-disk sections as \(C\). The stalk of \(j_!A\) at zero is zero. Its point-localization triangle is
\(i^!j_!A\to0\to C\xrightarrow{+1}\), so \(i^!j_!A\simeq C[-1]\).
Its cohomology is \(\ker(T-I)\) in degree one and \(\operatorname{coker}(T-I)\) in degree two. Their dimensions are equal, giving Euler number zero.

The stalk of \(Rj_*A\) is \(C\). Its costalk vanishes: the map from \(Rj_*A\) to \(Rj_*j^{-1}Rj_*A\) is the identity under open adjunction, and the localization triangle gives zero for the supported term. Thus both stalk and costalk Euler numbers are zero for each extension. For \(T=I\) the first extension has nonzero costalk and zero stalk, while the second has nonzero stalk and zero costalk. These different complexes satisfy the same Euler theorem.

For the first triangle, ordinary sections on the full disk really are zero. Identify the disk radially with \(\mathbb C\); the extension \(j_!A\) is positive-conic, so ordinary conic restriction identifies its section complex with its zero stalk. The map from these sections to punctured sections is therefore the zero map \(0\to C\), yielding the stated fibre \(C[-1]\). For the second extension, the localization unit is \(Rj_*\) of the identity under \(j^{-1}Rj_*A\simeq A\). Its supported fibre is zero before taking Euler numbers. These arguments distinguish the actual two localization maps.

### A constant complex with an arbitrary shift
*Difficulty: Introductory.*

On \(\mathbb C^d\) take \(F=k[r]\). Compute its stalk and point costalk at zero, including \(d=0\).

**Solution.** The stalk is \(k[r]\). The real manifold has dimension \(2d\) and its complex orientation trivializes the local orientation line. The point costalk of the constant sheaf is \(k[-2d]\), so \(i^!F=k[r-2d]\). Their Euler numbers are respectively \((-1)^r\) and \((-1)^{r-2d}=(-1)^r\). For \(d=0\) the two actual complexes agree. In higher dimension their nonzero cohomology degrees differ by \(2d\).

### Negative weights and a special point value
*Difficulty: Intermediate.*

On \(\mathbb C\), let \(\varphi=-3\) off zero and \(\varphi(0)=2\). Construct a bounded complex realization and compute \(D\varphi\).

**Solution.** The function is \(-3\,1_{\mathbb C}+5\,1_{\{0\}}\). Thus
\(F=k_{\mathbb C}^{\,3}[1]\oplus k_{\{0\}}^{\,5}\) realizes it. Away from zero its stalk Euler is \(-3\); at zero it is \(-3+5=2\). The constant summand has costalk \(k^3[-1]\) at zero, of Euler \(-3\), and the point summand has costalk \(k^5\), of Euler five. Their total is two. At a nonzero point, the constant costalk has the same Euler \(-3\) and the point summand vanishes. Hence \(D\varphi=\varphi\). Formula (15) also realizes the same function using the two disjoint strata directly.

### The crossing has two costalk degrees
*Difficulty: Advanced.*

Let \(Z=\{z_1z_2=0\}\subset\mathbb C^2\), and take its constant sheaf extended from this closed subset. Compute the stalk and point costalk cohomology at the crossing.

**Solution.** The union of the two complex axes is contractible, and its constant sheaf has stalk \(k\) at zero. Its punctured link is the disjoint union of two circles. Consequently link cohomology is \(k^2\) in degrees zero and one. The restriction \(k\to k^2\) in degree zero is diagonal. The point-localization long exact sequence gives zero supported cohomology in degree zero, its diagonal cokernel \(k\) in degree one, and \(k^2\) in degree two, with no other groups. The costalk Euler number is \(-1+2=1\), equal to the stalk Euler number. As a function,
\(1_Z=1_{\{z_1=0\}}+1_{\{z_2=0\}}-1_{\{0\}}\); all three indicators are fixed by (16), so their same integer combination is fixed too.

### A proper image with zero stalk Euler need not split
*Difficulty: Advanced.*

For the Hopf projection \(q:S^3\to\mathbb{CP}^1\), put \(Q=Rq_*k_{S^3}\). Compute its cohomology sheaves. Show that it is nonzero, has zero Euler number at every stalk, and is not isomorphic to
\(k_{\mathbb{CP}^1}\oplus k_{\mathbb{CP}^1}[-1]\).

**Solution.** Proper base change gives the cohomology of a circle at each stalk. The local product transitions rotate that circle, so they act identically on its degree-zero and degree-one cohomology. Thus \(H^0(Q)=k_{\mathbb{CP}^1}\) and \(H^1(Q)=k_{\mathbb{CP}^1}\), with no other cohomology sheaves. In particular \(Q\ne0\), while its stalk Euler number is \(1-1=0\).

If the proposed splitting existed, ordinary global sections would give
\(R\Gamma(\mathbb{CP}^1;k)\oplus R\Gamma(\mathbb{CP}^1;k)[-1]\), with one copy of \(k\) in each of degrees zero, one, two and three. But direct-image composition gives \(R\Gamma(\mathbb{CP}^1;Q)=R\Gamma(S^3;k)\), which has cohomology only in degrees zero and three. The zero- and top-dimensional cell structures of the sphere and of \(\mathbb{CP}^1\simeq S^2\) give these calculations over every field. The contradiction rules out the splitting. Formula (9) retains precisely the extension data that can cancel the two middle degrees.

The contradiction also works in characteristic two: it compares the dimensions of cohomology groups, not a sign in the coefficient field. The finite filtration in (9) proves an equality of Euler numbers by additivity of triangles; it does not remove the attaching maps responsible for the nonsplitting of \(Q\).

### A real ray fails the complex conclusion
*Difficulty: Intermediate.*

Inside the complex line take the closed real ray \(H=\{t\in\mathbb R:t\ge0\}\), and its constant sheaf extended from that closed subset. Compute stalk and point costalk Euler numbers at zero.

**Solution.** The stalk at zero is \(k\). Closed-embedding adjunction computes the ambient point costalk intrinsically on \(H\). In a small half-interval, ordinary sections and sections on the punctured half-interval are both \(k\), and their restriction map is the identity. The relative localization complex is therefore zero, so the point costalk Euler number is zero. The stalk Euler number is one.

This sheaf is real constructible on the complex line, but the ray is not a stratum of any locally finite complex analytic stratification with the required constant stalks. In particular it does not satisfy the complex hypothesis used in (3). Its Euler function has value one at zero, whereas its dual function has value zero there. Complex constructibility is essential to both conclusions.

### A cusp retains two normal branches and their monodromy
*Difficulty: Advanced.*

Let \(Z=\{y^2=x^3\}\subset\mathbb C^2\), with its constant sheaf \(F=k_Z\). Compute its stalk and costalk at the cusp. Explain why its point specialization has rank two on the nonzero tangent line, although its central stalk has rank one.

**Solution.** The map \(t\mapsto(t^2,t^3)\) is a homeomorphism from \(\mathbb C\) onto \(Z\). It is bijective: off zero its inverse is \(t=y/x\), and zero has only the preimage zero. The inverse is continuous at zero because \(|t|^2=|x|\). This also proves properness over compact subsets. Intrinsic closed-support adjunction therefore gives stalk \(k\) and point costalk \(k[-2]\), with Euler number one for each.

For the real positive normal-deformation parameter \(a>0\), normal coordinates \((u,w)\) satisfy
\(w^2=a u^3\). Near a nonzero tangent point \((u_0,0)\), choose a small complex disk in \(u\) avoiding zero and a branch of \(u^{3/2}\). The positive chamber consists of the two graphs
\(w=\pm\sqrt a\,u^{3/2}\). For sufficiently small \(a\) both lie in the chosen vertical neighborhood. They are disjoint, and each is a product of that disk with a positive interval. The constant coefficient on each has ordinary sections \(k\) and no higher cohomology. The cofinal chamber restrictions preserve both copies. Hence specialization has rank two there. Off the tangent line it vanishes by the normal-cone support bound.

A loop in \(u\) around zero changes the sign of \(u^{3/2}\) and interchanges the two branches. The tangent-line local system consequently has transposition monodromy. Its circle cochains have \(T=\begin{pmatrix}0&1\\1&0\end{pmatrix}\); kernel and cokernel of \(T-I\) each have dimension one, even in characteristic two. The central specialization stalk is \(k\) by (2). The restriction to the invariant circle sections is the diagonal map \(c\mapsto(c,c)\): it is specialization of the constant-section unit \(k_{\mathbb C^2}\to k_Z\). This is an isomorphism onto the invariant line. The localization triangle then gives costalk \(k[-2]\), in agreement with the original cusp. The two approaching branches and their monodromy are therefore retained by specialization while the Euler equality holds.

The chamber calculation can be made uniform on a cofinal basis. Choose \(\delta<|u_0|\), let \(D=\{|u-u_0|<\delta\}\), take a vertical disk \(|w|<\eta\), and put \(M=|u_0|+\delta\). For

\[
0<a<\varepsilon,\qquad \varepsilon M^3<\eta^2,
\]

both graphs lie wholly in the same product box \(D\times\{|w|<\eta\}\times(0,\varepsilon)\), because \(|w|^2=a|u|^3<\varepsilon M^3\). Each graph is a copy of \(D\times(0,\varepsilon)\); its projection to these coordinates is a homeomorphism. Such smaller boxes are cofinal at \((u_0,0,0)\), and compatible choices of the square-root branch make their restriction maps the identity on the two coefficients. This proves the stalk calculation for \(Rj_{+*}\), including absence of higher cohomology. Around a loop, choose an annulus with bounded \(|u|\) and the same inequality with its upper radius in place of \(M\). The two sheets glue by transposition after one turn. The map from the central coefficient is diagonal, not the sum map \(k^2\to k\); it remains an isomorphism to the invariant line when the characteristic is two. In the localization long exact sequence that diagonal map kills the possible degree-one costalk, leaving the one-dimensional cokernel of \(T-I\) in degree two.

## References

P. Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), *Journal of Pure and Applied Algebra* **72** (1991), 83–93, supplies the general Euler-function formalism; Theorem 2.5 concerns duality for real constructible functions. The complex stalk–costalk equality proved here uses the point-specialization maps, complex microsupport annihilator, scalar-orbit descent and compact projective projection developed in the programme lessons linked above. Its circle calculation retains arbitrary finite monodromy and works with integer Euler numbers over every field.