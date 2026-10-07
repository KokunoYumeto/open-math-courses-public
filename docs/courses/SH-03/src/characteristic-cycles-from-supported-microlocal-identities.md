# Characteristic cycles from supported microlocal identities

A characteristic cycle is a trace of the identity after its directional information has been retained. The trace takes values in a dualizing coefficient and carries a support condition. Forgetting that condition too early can erase a nonzero cycle. We construct the actual supported map, prove its product formula and microlocal invariance, and calculate its normalization for finite complexes at a point.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

Use Constructible traces and local Euler indices for the diagonal external-Hom map, its ordinary restriction and the graded contraction. Perfect operations and finite microlocal coefficients supplies bounded constructible microlocal Hom. Lagrangian cycles and proper cotangent images supplies its cycle coefficient and the lowest supported dualizing sheaf. The operation proofs used below are ordinary microlocal-Hom recovery, its actual kernel unit and composition, external microlocalization, point-localized morphisms, and the cone-topology kernel. The cutoff kernel initially uses ordinary direct image; its properness for the compactly supported input in this lesson is proved below.

The characteristic cycle of a constructible sheaf goes back to M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§3.1–3.4, pp. 197–199. That paper defines its local multiplicities through Euler characteristics. This lesson constructs a supported microlocal identity and its evaluated trace, then proves the product formula, microlocal invariance and the closed-point coefficient. The closed-point calculation below is an application of the normalized closed trace. Cotangent transport, the general conormal normalization, antipodal duality, integrality, additivity and the half-line and Lorentz-cone examples are treated in later lessons.

## The coefficient and the supported identity

Fix a field \(k\) of characteristic zero. The chain and Lagrangian-cycle constructions in the preceding lessons allow a commutative ring of finite global dimension; the characteristic-cycle results here use the stated field hypothesis. Let \(X\) be real analytic, Hausdorff and countable at infinity, with the standing finite uniform dimension bound, and let

\[
 F\in D^b_{\mathbb R\text{-c}}(k_X),\qquad
 \Lambda=\operatorname{SS}(F),\qquad
 E_X=\pi_X^{-1}\omega_X.
 \qquad\text{(1)}
\]

Constructibility includes finite perfect stalks and a uniform bounded cohomological range. Over the field fixed here, stalk perfection follows from finite-dimensional stalk cohomology; the uniform range is a separate part of the bounded hypothesis. The constructible geometric criterion makes \(\Lambda\) a closed conic subanalytic isotropic carrier. Thus supported degree-zero classes with coefficient \(E_X\) give sections of \(\mathcal L_X\). We do not infer the support of the final cycle is all of \(\Lambda\).

Let \(\delta:X\hookrightarrow X^2\) be the closed diagonal. With projections \(q_1,q_2\), put

\[
 K_F=F\boxtimes D_XF,\qquad
 \mathsf M(F,F)=\mu_{\Delta_X}
      R\mathcal Hom(q_2^{-1}F,q_1^!F).
 \qquad\text{(2)}
\]

The diagonal conormal is identified by
\((x,x;\xi,-\xi)\mapsto(x;\xi)\).
The actual constructible external-Hom comparison identifies
\(K_F\) with the Hom kernel in (2). Its exceptional diagonal restriction identifies
\(\delta^!K_F\) with \(R\mathcal Hom(F,F)\). Indeed, the exceptional internal-Hom isomorphism changes the first Hom input by \(\delta^{-1}\) and the second by \(\delta^!\); it applies because \(q_2^{-1}F\) is bounded and \(q_1^!F\) is bounded below. The identities \(q_2\delta=q_1\delta=\mathrm{id}_X\), with the actual exceptional-composition isomorphism for the second, give precisely the two arguments \(F,F\). The relative orientation and shift of \(q_1^!\) are already included in this composition. They cannot be removed by replacing \(\delta^!\) with ordinary restriction.

The identity of \(F\), under these actual adjunctions, gives a kernel morphism

\[
 u_F:k_{\Delta_X}\longrightarrow K_F.
 \qquad\text{(3)}
\]

Indeed
\(\operatorname{Hom}(k_{\Delta_X},K_F)
=\operatorname{Hom}(k_X,\delta^!K_F)
=\operatorname{Hom}(F,F)\).
Apply diagonal microlocalization. The center-supported formula sends \(k_{\Delta_X}\) to \(k_{T^*X}\), without a shift, so (3) becomes the canonical unit

\[
 e_F:k_{T^*X}\longrightarrow\mathsf M(F,F).
 \qquad\text{(4)}
\]

Ordinary recovery \(R\pi_{X*}\mathsf M(F,F)\simeq R\mathcal Hom(F,F)\) carries (4) back to \(\mathrm{id}_F\). This follows from the zero-direction recovery and the same kernel adjunction defining (3); it is a statement about the particular identity, rather than just an equality of objects. Here \(R\mathcal Hom\) is a sheaf on \(X\); taking derived global sections gives the global endomorphism group.

The support estimate gives
\(\operatorname{supp}\mathsf M(F,F)\subset\Lambda\).
In fact the canonical unit detects the whole microsupport: if its germ at \(p\) is zero, the point-localized morphism theorem says the identity of \(F\) is zero in \(D^b(k_X;p)\). The object is then zero in that category, equivalently \(p\notin\operatorname{SS}(F)\). Only after the trace below can cancellation reduce the support. In detail, an object whose identity is zero in an additive category is isomorphic to the zero object: its unique maps to and from zero compose to its identity and to the identity of zero. The thick quotient and saturation statement identifies the objects killed by the point localization with those whose microsupport avoids \(p\). This argument uses the point-localized identity, rather than treating \(R\pi_{X*}\) as a conservative functor.

## Ordinary restriction and the unique supported trace

Use the order

\[
 t_F:F\otimes D_XF
 \xrightarrow{\text{graded symmetry}}D_XF\otimes F
 \xrightarrow{\mathrm{evaluation}}\omega_X.
 \qquad\text{(5)}
\]

The symmetry includes the Koszul sign. The kernel map to be microlocalized is

\[
 v_F:K_F\longrightarrow
 \delta_*\delta^{-1}K_F
 =\delta_*(F\otimes D_XF)
 \xrightarrow{\delta_*t_F}\delta_*\omega_X.
 \qquad\text{(6)}
\]

Its first arrow is the ordinary closed-embedding unit. It is not an exceptional restriction. The center-supported microlocalization formula identifies
\(\mu_{\Delta_X}(\delta_*\omega_X)=E_X\):
specialization has coefficient \(\omega_X\) on the zero normal section; that section has zero pairing with every covector, and its Fourier-kernel projection is the identity. The orientation and shift already lie in \(\omega_X\).

Consequently (6) gives \(T_F:\mathsf M(F,F)\to E_X\). The source is supported on the closed \(\Lambda\), so its support-localization map is invertible. Apply support localization to \(T_F\) and invert that source map:

\[
 \kappa_F:\mathsf M(F,F)
 \xrightarrow{\sim}R\Gamma_\Lambda\mathsf M(F,F)
 \xrightarrow{R\Gamma_\Lambda T_F}R\Gamma_\Lambda E_X.
 \qquad\text{(7)}
\]

This is the unique lift of \(T_F\) from a source supported on \(\Lambda\). To see the adjunction explicitly, let \(A\) be any complex supported on \(\Lambda\). The support triangle for \(E_X\) has third term \(Rj_*j^{-1}E_X\), where \(j\) is the complementary open inclusion. For every integer \(r\),
\(\operatorname{Hom}(A,Rj_*j^{-1}E_X[r])
=\operatorname{Hom}(j^{-1}A,j^{-1}E_X[r])=0\).
Applying \(\operatorname{Hom}(A,-)\) to that triangle therefore gives the bijection
\(\operatorname{Hom}(A,R\Gamma_\Lambda E_X)\simeq
\operatorname{Hom}(A,E_X)\), induced by the support counit. Taking \(A=\mathsf M(F,F)\) proves existence and uniqueness of the lift in (7). Vanishing of a map outside \(\Lambda\), without such a source, would not by itself provide a unique lift.

Define

\[
 \operatorname{CC}(F)
 =[\kappa_Fe_F]\in H^0_\Lambda(T^*X;E_X)
 \subset\Gamma(T^*X;\mathcal L_X).
 \qquad\text{(8)}
\]

This constructs the supported characteristic class from ordinary Hom recovery, support on microsupport, the actual external-Hom kernel, ordinary diagonal restriction, graded evaluation, and the center-supported coefficient. All maps restrict to their counterparts on an open subset. Enlarging \(\Lambda\) to another allowed closed carrier composes (7) with its support-enlargement map.

On an \(n\)-dimensional component, the earlier cycle comparison identifies
\(R\Gamma_\Lambda E_X\) with
\(j_{\Lambda*}(\omega_\Lambda\otimes B_X|_\Lambda)[-n]\).
Since \(\dim\Lambda\leq n\), this complex has no negative cohomology. Thus

\[
 H^0_\Lambda(T^*X;E_X)
 =\Gamma\bigl(T^*X;H^0R\Gamma_\Lambda E_X\bigr).
 \qquad\text{(9)}
\]

This explains why equality of cycle germs proves equality of the corresponding global degree-zero sections. It also explains why forgetting the support in (8) can lose information: the map to ordinary \(H^0(T^*X;E_X)\) need not be injective.

## Products retain the actual graded kernel maps

For bounded constructible \(F,G\) on \(X,Y\), respectively,

\[
 \operatorname{CC}(F\boxtimes G)
 =\operatorname{CC}(F)\boxtimes\operatorname{CC}(G).
 \qquad\text{(10)}
\]

The right side uses the supported cycle product and its ordered dualizing coefficient. Its carrier is
\(\operatorname{SS}(F)\times\operatorname{SS}(G)\).
This is closed, conic, subanalytic and isotropic; the external microsupport estimate puts the left side inside that carrier.

**Proof.** Reorder \((X\times Y)^2\) as \(X^2\times Y^2\); the diagonal becomes \(\Delta_X\times\Delta_Y\). Constructible product duality and the graded permutation give the actual comparison from \(K_F\boxtimes K_G\) to \(K_{F\boxtimes G}\). Under exceptional diagonal restriction and internal Hom adjunction, the tensor of the kernel units (3) represents
\(\mathrm{id}_F\otimes\mathrm{id}_G=\mathrm{id}_{F\boxtimes G}\).
Hence it is the kernel unit of the product with these identifications.

The external microlocal comparison

\[
 \mu_{\Delta_X}K_F\boxtimes
 \mu_{\Delta_Y}K_G
 \longrightarrow
 \mu_{\Delta_X\times\Delta_Y}(K_F\boxtimes K_G)
 \qquad\text{(11)}
\]

comes from the product normal deformation, its two independent positive scalings and the Fourier product kernel. On the center-supported unit kernels, its map sends \(1\otimes1\) to \(1\): both zero-normal kernel projections are identities. Thus (11), followed by the actual external-Hom comparison, carries \(e_F\boxtimes e_G\) to \(e_{F\boxtimes G}\). One can verify the selected comparison before applying Fourier: the specialization external map is adjoint to the identity on the two positive chambers, and its restriction to equal deformation parameters is ordinary base exchange. Precomposing with the two ordinary units leaves the single product unit by naturality and the counit triangles. This is the zero-section identity P19 in the product-normalization proof. On zero-normal supported inputs the remaining Fourier correspondence has no fibre to integrate, so its product map is the ordered tensor identity. This checks the unit map itself without inferring equality from its ordinary direct image.

Ordinary diagonal restriction is compatible with products. Tensor the evaluations in (5), permute the factors to the displayed product order and use
\(\omega_X\boxtimes\omega_Y\simeq\omega_{X\times Y}\).
Tensor–Hom adjunction says this is exactly the evaluation of the product dual. This verifies the evaluated kernel square, including its graded permutations. Naturality of (11) then makes the same square commute after microlocalization. On the final center-supported objects its comparison is the ordered map
\(E_X\boxtimes E_Y\to E_{X\times Y}\).

All these maps have sources supported on the product carrier. Their unique supported lifts therefore agree by the adjunction used in (7). Applying them to the product units proves (10) with its support condition. We have used the external comparison as a map; no general invertibility of (11) is needed. \(\square\)

## Naturality of evaluation proves microlocal invariance

First take an ordinary degree-zero morphism \(h:F\to G\) between bounded constructible complexes. On \(T^*X\), let

\[
 A=\mathsf M(G,F),\quad B=\mathsf M(F,F),\quad
 C=\mathsf M(G,G),\quad D=\mathsf M(F,G).
 \qquad\text{(12)}
\]

Precomposition acts on the first argument; postcomposition acts on the second. Their square commutes:

\[
 \begin{array}{ccc}
 A&\xrightarrow{\mathrm{pre}\,h}&B\\
 \downarrow{\mathrm{post}\,h}&&\downarrow{\mathrm{post}\,h}\\
 C&\xrightarrow{\mathrm{pre}\,h}&D.
 \end{array}
 \qquad
 (\mathrm{post}\,h)e_F=(\mathrm{pre}\,h)e_G.
 \qquad\text{(13)}
\]

Both statements follow before microlocalization from pre- and postcomposition of the actual Hom kernels. For the upper-right and lower-left routes, applying a map to the second Hom argument commutes with applying a map contravariantly to the first; these are degree-zero maps, so their interchange introduces no graded sign. The two maps from \(k_{\Delta_X}\) in the unit equality are adjoint to \(h\circ\mathrm{id}_F\) and \(\mathrm{id}_G\circ h\), respectively. They are equal under the same kernel adjunction used in (3); applying microlocalization proves the asserted equality of units.

There is also an equality of trace maps from \(A\). Its constructible kernel is \(F\boxtimes D_XG\). The two routes apply \(h\) to the first factor or \(D_Xh\) to the second. On the diagonal, naturality of Verdier evaluation gives

\[
 t_G(h\otimes1_{D_XG})
 =t_F(1_F\otimes D_Xh).
 \qquad\text{(14)}
\]

The same ordinary diagonal restriction precedes both maps. Apply microlocalization and lift to a common allowed carrier
\(\Lambda_0=\operatorname{SS}(F)\cup\operatorname{SS}(G)\).
The carrier \(\Lambda_0\) is allowed: the finite union is closed, conic and subanalytic, and a common stratification refines its two isotropic carriers into isotropic strata. The cross source \(A\) has support inside \(\operatorname{SS}(F)\cap\operatorname{SS}(G)\), hence inside \(\Lambda_0\). The adjunction just proved for (7), applied to this cross source, therefore lifts the equality of the evaluated kernel maps uniquely and gives

\[
 \kappa_G^{\Lambda_0}(\mathrm{post}\,h)
 =\kappa_F^{\Lambda_0}(\mathrm{pre}\,h):
 A\longrightarrow R\Gamma_{\Lambda_0}E_X.
 \qquad\text{(15)}
\]

This is equality of the particular evaluated trace maps, not just an isomorphism between endomorphism objects.

Suppose \(\operatorname{SS}(\operatorname{Cone}h)\) avoids an open \(\Omega\subset T^*X\). Exactness and the microlocal-Hom support estimate make all four arrows in (13) isomorphisms on \(\Omega\). Put
\(w=(\mathrm{pre}\,h)^{-1}e_F:k_\Omega\to A|_\Omega\).
The square and the unit equality in (13) imply
\((\mathrm{post}\,h)w=e_G\): apply the invertible bottom precomposition to both sides and use the square. Equation (15), applied to \(w\), now proves

\[
 \operatorname{CC}(F)|_\Omega
 =\operatorname{CC}(G)|_\Omega
 \quad\text{for an ordinary constructible denominator }h.
 \qquad\text{(16)}
\]

We extend this to an isomorphism in the full localized category \(D^b(k_X;\Omega)\). Its intermediate objects need not initially be constructible, so this extension requires a representative argument.

Fix \(p\in\Omega\) with nonzero covector, and work in a vector-space chart. The point-localized morphism theorem represents a chosen isomorphism from \(F\) to \(G\) by

\[
 F\ \xleftarrow{\,a\,}\ Q_{U,\gamma}F\
 \xrightarrow{\,b\,}\ G,\qquad
 Q_{U,\gamma}F=(P_\gamma(F_U))_U,
 \qquad\text{(17)}
\]

where \(a\) is a \(p\)-denominator and
\(P_\gamma=\phi_\gamma^{-1}R\phi_{\gamma*}\).
Choose relatively compact subanalytic \(U\) and a closed proper polyhedral cone \(\gamma\), with the chosen covector strictly negative on its nonzero vectors. These choices are cofinal in the cone-stalk system. If the admissible cone is \(\gamma_0=\{0\}\), retain it: it is already closed, proper and polyhedral. For any other admissible closed cone \(\gamma_0\), take the nonempty compact convex section
\(B=\{v\in\gamma_0:-\xi(v)=1\}\). A sufficiently close outer polytope in the affine hyperplane \(-\xi=1\) contains \(B\): choose a finite sufficiently fine grid covering a small convex thickening of \(B\), and take the convex hull of the grid cubes meeting \(B\). Its distance from \(B\) can be made arbitrarily small. The positive cone over this polytope is closed, proper and polyhedral, contains \(\gamma_0\), and stays in any prescribed angular enlargement of it. The functional \(\xi\) remains strictly negative on every nonzero vector, because its value is \(-1\) on the section. Polarity gives the required angular refinement in the cone-stalk system. Relatively compact subanalytic balls are cofinal ordinary neighborhoods, so shrinking \(U\) gives simultaneous refinements. Thus the representation in (17) can be chosen with both of these properties; no cycle is assigned to a nonconstructible intermediate object.

The object in the middle of (17) is constructible. To check the nonproper operation, use G10, the cone-topology projector. In its incidence coordinates \(z-x\in\gamma\), put \(v=z-x\); projection to \(x\) becomes \(d(v,z)=z-v\). This invertible coordinate change gives its actual difference kernel

\[
 P_\gamma(F_U)=Rd_*(k_\gamma\boxtimes F_U),
 \qquad d(v,z)=z-v.
 \qquad\text{(18)}
\]

The closed support of \(F_U\) lies in compact \(\overline U\). Over a compact target set \(K\), an incidence satisfies
\(z\in\operatorname{supp}(F_U)\) and \(v=z-x\), \(x\in K\).
Both variables are bounded, and the inverse image in the closed kernel support is closed in that compact product. Thus \(d\) is proper on this support. The kernel is bounded constructible with perfect coefficients, so the proper constructible-image theorem applies; it also identifies \(Rd_*\) with \(Rd_!\) on this kernel. The outer subanalytic open extension preserves bounded constructibility. Extending from the chart to \(X\) retains it.

The fraction represents an isomorphism at \(p\); since \(a\) is invertible there, \(b\) is invertible there too. Saturation of the denominator system implies that both cones have microsupport avoiding \(p\). Closedness gives a smaller cotangent neighborhood on which both avoid it. Apply (16) to each arrow of (17), obtaining equality of the two cycle germs at \(p\).

At a zero covector, the localized category is the ordinary germ category: an invisible cone vanishes on an ordinary neighborhood of the base point. A representative of the isomorphism therefore gives an ordinary local derived isomorphism after shrinking, with constructible inputs. The ordinary isomorphism naturality of (3)–(7) proves the same equality there. Finally (9) turns equality of all the germs into

\[
 F\simeq G\text{ in }D^b(k_X;\Omega)
 \quad\Longrightarrow\quad
 \operatorname{CC}(F)|_\Omega=\operatorname{CC}(G)|_\Omega.
 \qquad\text{(19)}
\]

This proof retains the identities and their evaluated supported maps. It also checks constructibility of the pointwise roofs instead of assigning a characteristic cycle to an arbitrary bounded intermediate object. \(\square\)

## A finite point coefficient fixes the normalization

For \(X=\mathrm{pt}\), all diagonal and microlocal operations in (3)–(8) are identities and \(E_X=k\). Represent \(V\) by a bounded finite-dimensional complex \(P\). With its ordinary complex dual, the actual tensor–Hom map is

\[
 P\otimes P^\vee\longrightarrow\operatorname{Hom}^{\bullet}(P,P),
 \qquad p\otimes\varphi\longmapsto(q\mapsto p\,\varphi(q)).
 \qquad\text{(20)}
\]

For a homogeneous functional \(\varphi\) of degree \(b\), the dual differential is
\(d^\vee\varphi=-(-1)^b\varphi d_P\).
If \(p\) has degree \(a\), the tensor differential sends \(p\otimes\varphi\) to
\(d_Pp\otimes\varphi+(-1)^a p\otimes d^\vee\varphi\).
Applying (20) gives the two terms \(d_PT-(-1)^{a+b}Td_P\), which are exactly the Hom differential of the degree-\(a+b\) map \(T\). Thus (20) is a chain map. In each degree its basis tensors are the corresponding matrix units; bounded finite dimensionality makes their total sum finite, so it is an isomorphism of complexes. For homogeneous bases \(e_{r,s}\) of \(P^r\), its inverse carries the identity to
\(\sum_{r,s}e_{r,s}\otimes e_{r,s}^*\).
The symmetry in (5) contributes
\((-1)^{r(-r)}=(-1)^r\).
Evaluation therefore gives
\(\sum_r(-1)^r\dim P^r\).
Write \(Z^r=\ker(d:P^r\to P^{r+1})\) and
\(B^r=\operatorname{im}(d:P^{r-1}\to P^r)\).
The exact sequences
\(0\to Z^r\to P^r\to B^{r+1}\to0\) and
\(0\to B^r\to Z^r\to H^r(P)\to0\)
give
\(\dim P^r=\dim H^r(P)+\dim B^r+\dim B^{r+1}\).
In the finite alternating sum the two boundary sums cancel after shifting the index by one. Consequently the evaluated identity depends only on cohomology and gives

\[
 \operatorname{CC}(V)=\chi(V)[\mathrm{pt}],
 \qquad \chi(V)=\sum_r(-1)^r\dim_k H^r(V)\in\mathbb Z.
 \qquad\text{(21)}
\]

The integer is viewed in \(k\). Characteristic zero makes that coefficient map injective.

There is also a direct calculation for a closed point \(i:\{x\}\hookrightarrow X\):

\[
 \operatorname{CC}(i_*V)
 =\chi(V)[T_{\{x\}}^*X].
 \qquad\text{(22)}
\]

Here \(D_X(i_*V)=i_*V^\vee\), by the actual closed duality and
\(i^!\omega_X=k\).
The external kernel is supported at \((x,x)\). Its diagonal specialization is on the zero normal vector over \(x\); its Fourier transform is constant on the full cotangent fibre with coefficient \(V\otimes V^\vee\), without an integration shift. The kernel unit (3) becomes the identity tensor there. Since the kernel is already supported on the diagonal, its ordinary diagonal restriction in (6) is the identity on that supported object. The remaining evaluation is the point contraction followed by the actual closed trace
\(i_*k\to\omega_X\).
Thus its center-supported microlocalization is the pullback of this closed trace to the full fibre, multiplied by the supertrace (21).

The normalized point conormal in the preceding cotangent lessons is exactly that pullback: the direct-image coefficient is Cartesian proper-support base change followed by the same closed point trace. This proves (22) with coefficient \(+1\) when \(V=k\). No assertion about general conormal normalization or general cycle transport has been used.

## Exercises with complete solutions

### An acyclic pair contributes no point trace

*Difficulty: Introductory.*

At a point, take a complex which is the direct sum of \(k^3\) in degree \(0\), \(k^2\) in degree \(1\), and the two-term complex \(k\xrightarrow{\mathrm{id}}k\) in degrees \(2,3\). Compute its characteristic cycle from both the chain terms and the cohomology.

**Solution.** The term dimensions are \(3,2,1,1\), so the graded identity contraction is \(3-2+1-1=1\). The identity differential in the last two degrees gives zero cohomology there. The other cohomology groups are \(k^3\) and \(k^2\) in degrees zero and one, giving \(3-2=1\). Thus the cycle is \([\mathrm{pt}]\). The odd-degree minus signs come from the symmetry between a basis vector of degree \(r\) and its dual of degree \(-r\), not from an ungraded trace of the total underlying vector space, which would count \(7\).

### A nonzero complex can have zero characteristic cycle

*Difficulty: Intermediate.*

Let \(i:\{x\}\hookrightarrow X\) be a closed point in a positive-dimensional manifold, and take \(F=i_*(k\oplus k[1])\). Compute its characteristic cycle and its microsupport.

**Solution.** The point coefficient has cohomology \(k\) in degrees zero and minus one. Its Euler coefficient is \(1-1=0\), so (22) gives \(\operatorname{CC}(F)=0\). The object is nonzero. The closed-embedding microsupport formula gives its microsupport as the full cotangent fibre \(T_x^*X\), since the point coefficient has nonzero cohomology. The identity unit detects that whole fibre, but the evaluated trace cancels its two shifted coefficients. Therefore the support of the characteristic cycle can be strictly smaller than microsupport, even empty.

### Evaluation naturality does not identify two arbitrary identities

*Difficulty: Intermediate.*

At a point, let \(F=k^2\), \(G=k\), \(h(a,b)=a\), and \(w(c)=(c,0)\). Check (14) on \(w\), and explain why it does not assert \(\operatorname{CC}(F)=\operatorname{CC}(G)\).

**Solution.** Precomposition sends \(w:G\to F\) to \(wh:F\to F\), the matrix \(\mathrm{diag}(1,0)\). Postcomposition sends it to \(hw:G\to G\), the identity. Their ordinary traces are both \(1\), which is (14) in degree zero. The identity of \(F\) has trace \(2\), while the identity of \(G\) has trace \(1\). The map \(h\) is not invertible: its kernel is a one-dimensional point coefficient. Its cone is nonzero at the only cotangent point, so \(h\) is not a denominator. In (16) invertibility is what constructs an inverse image of the identity under precomposition; the present \(w\) only gives a projection on \(F\).

### A constant summand is invisible at a nonzero point covector

*Difficulty: Advanced.*

On \(X=\mathbb R\), let \(F=k_{\{0\}}\), \(G=F\oplus k_X\), and let \(h:F\to G\) be the summand inclusion. Work at \(p=(0;dt)\). Identify the denominator and determine the characteristic-cycle germ of \(G\).

**Solution.** The cone of the inclusion is \(k_X\), whose microsupport is the zero section. It avoids a small cotangent neighborhood of the nonzero covector \(p\). Thus \(h\) is an ordinary constructible denominator there. The trace-map proof (13)–(16) gives equal characteristic-cycle germs for \(F\) and \(G\). Formula (22) gives the germ of the normalized point conormal with coefficient \(1\). The extra constant summand has changed the ordinary sheaf near zero, but it contributes no directional information at \(p\). At the zero covector \((0;0)\) the cone is visible, so this denominator argument supplies no equality there. We have not used a general additivity or constant-zero-section formula.

### The compact cutoff kernel is proper on its support

*Difficulty: Advanced.*

In \(\mathbb R\), take \(F=k_{[0,\infty)}\), \(U=(-a,a)\) with \(a>0\), and \(\gamma=(-\infty,0]\). Verify the support-properness of the kernel in (18), and calculate its coefficient near the origin. Use the covector \(dt\).

**Solution.** The restricted and extended coefficient is \(F_U=k_{[0,a)}\); its closed support is \([0,a]\), including the endpoint with zero stalk. A kernel incidence over \(x\) has \(z\in[0,a]\), \(v\leq0\), and \(x=z-v\). For \(x\) in a compact set \(K\), \(v=z-x\) lies in a bounded interval. The incidence in the closed support is closed in the product of these compact intervals and is compact. Thus the difference map is proper on the closed kernel support, despite its noncompact unrestricted fibres.

For \(x<0\) close to zero, the condition \(z\leq x\) gives no coefficient. For \(0\leq x<a\), the coefficient fibre is the compact interval \(0\leq z\leq x\), with constant coefficient \(k\). Its cohomology is \(k\) in degree zero, including the single point at \(x=0\). Restriction between these compact intervals preserves \(1\), so proper base change and these maps give the closed positive-ray coefficient near zero. The outer restriction to \(U\) leaves that germ unchanged. The covector \(dt\) is strictly negative on the nonzero vectors of \(\gamma\), so it lies in the interior of the required negative polar. The cutoff counit consequently is a denominator at \((0;dt)\). This example checks a constructible compact cutoff without replacing a nonproper ordinary direct image by a proper one on its whole domain.

### A graded product has the product of the two supertraces

*Difficulty: Intermediate.*

At points take \(P=k^2\oplus k[-1]\) and \(Q=k^2[1]\oplus k[-2]\), with zero differentials. Calculate their two characteristic cycles and that of \(P\otimes Q\), and reconcile the tensor degree count with (10).

**Solution.** The nonzero degrees of \(P\) are \(0,1\), with dimensions \(2,1\), so \(\chi(P)=1\). Those of \(Q\) are \(-1,2\), with dimensions \(2,1\), so \(\chi(Q)=-2+1=-1\). Their tensor has dimensions \(4,2,2,1\) in degrees \(-1,0,2,3\), respectively. Its supertrace is
\[
 -4+2+2-1=-1=1\cdot(-1).
 \qquad\text{(23)}
\]
Thus the product cycle is \(-[\mathrm{pt}]\), as (10) predicts. In the kernel product proof, the permutation grouping the two identity tensors and the permutation in their graded evaluation retain the same tensor degree signs. An ungraded contraction would instead count all \(9\) tensor basis vectors and fail this calculation.

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§3.1–3.4, pp. 197–199, works with bounded constructible complexes over a field, uses their microlocal local models, and defines conormal multiplicities by Euler characteristics. This is credit for the characteristic-cycle framework. The supported identity construction (3)–(8), its evaluated product square, the constructible-roof argument, and the explicit point supertrace are proved above from the indicated programme operations. The paper's conormal orientation and index-intersection convention must be compared before identifying its generators with a differently normalized graph construction.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4–4.6.8 and §4.7, pp. 95–97, supplies the exceptional composition, tensor, internal-Hom, closed-support and diagonal identities. In particular Proposition 4.6.8 explains the exceptional diagonal recovery; ordinary restriction is the separate evaluation step in (6). The present teaching order follows the maps needed to keep support, then tests loss of support, naturality without invertibility, compact cutoff representatives and graded cancellation in six solved examples. The human texts retain their authorship and their own terms.
