# Lagrangian cycles and proper cotangent images

A Lagrangian cycle combines an \(n\)-dimensional cycle in a \(2n\)-dimensional cotangent bundle with the orientation of the cotangent fibres. The coefficient is essential on a nonorientable base. Singular carriers are allowed, but their regular pieces must satisfy the cycle conservation law. A cotangent direct image then uses properness on an incidence set, which can hold even when the base map is nonproper.

*Original text by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Source-scope and reader repairs by GPT-6 Astra (OpenAI), Ultra, 6 October 2026. Self-checked by the revising AI. New original text is public domain (CC0).*

Use Subanalytic chains and closed cycle supports, Supports, products and proper images of chains and The dualizing resolution by subanalytic chains for singular dualizing bounds, finite-rank coefficient supports and the cycle complex. Conic subanalytic images and isotropic dimension and Isotropic cotangent transport and discrete critical values supply the geometric bounds and image theorem. The exact current SH-02 imports are the submersion/relative dualizing formula, closed support, proper-support base change and normalized trace.

This lesson defines Lagrangian cycles and their proper cotangent direct images, in the framework of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1–3. The pullback coefficient map and the section-intersection comparison are treated in Pulling back Lagrangian cycles through a graph and Continuous sections and supported cycle intersections.

## The orientation coefficient fixes the dimension

Let \(A\) be a commutative ring of finite global dimension. Throughout this lesson manifolds are real analytic, Hausdorff and countable at infinity, of uniformly bounded finite dimension. Work on a component \(X\) of dimension \(n\), and write

\[
 \pi_X:T^*X\longrightarrow X,\qquad
 B_X=\operatorname{or}_{T^*X/X},\qquad
 E_X=\pi_X^{-1}\omega_X.
 \qquad\text{(1)}
\]

The relative sign line \(B_X\) is the orientation of the \(n\)-dimensional cotangent fibre, with coefficients in \(A\).
The submersion formula and exceptional composition give

\[
 \omega_{T^*X}\simeq B_X[n]\otimes_A E_X,
 \qquad
 E_X\simeq\omega_{T^*X}\otimes_A B_X[-n].
 \qquad\text{(2)}
\]

The second map cancels the shifted invertible first factor of the first map, with the canonical integral square pairing \(B_X\otimes B_X\simeq A\). The displayed ordering and the usual symmetry of shifted complexes specify the cancellation. This is the actual relative dualizing identification; a choice of unrelated orientation trivializations would not specify the same map.

For a closed subanalytic \(\Lambda\subset T^*X\) of dimension at most \(n\), exceptional composition and finite local freeness give

\[
 H^0_\Lambda(E_X)
 \simeq j_{\Lambda*}H^{-n}(\omega_\Lambda\otimes B_X|_\Lambda)
 \simeq H^0_\Lambda\mathcal Z_n(B_X).
 \qquad\text{(3)}
\]

These are sheaves on \(T^*X\). The first term uses the sheaf support operation; the last is its actual closed-support subsheaf of cycles. The shift in (2) turns degree \(-n\) into supported degree zero. It does not turn the geometric dimension into \(2n\).

## Closed isotropic carriers form a directed system

All conicity is with respect to strictly positive cotangent scaling. Let \(\mathscr I_X\) be the family of closed, conic, subanalytic isotropic subsets of \(T^*X\). The canonical-form criterion gives
\(\dim\Lambda\leq n\) for every such subset.

Finite unions remain closed, conic and subanalytic. They remain isotropic because vanishing of the canonical one-form on a finite union follows from the point-normal cone test. Thus \(\mathscr I_X\) is directed by inclusion.

Define

\[
 \mathcal L_X=
       \underset{\Lambda\in\mathscr I_X}{\operatorname{colim}}
                  H^0_\Lambda(E_X)
       \ \subset\ \mathcal Z_n(B_X).
 \qquad\text{(4)}
\]

The colimit is a filtered colimit of sheaves. Its maps are the closed-support maps. Formula (3) identifies each with the inclusion of cycles supported on \(\Lambda\), so they are injective and compatible with common upper carriers. Consequently (4) is an actual subsheaf of cycles. Every germ has a representative on one closed conic isotropic carrier. The assertion does not require a globally finite carrier presentation for every section.

The notation \(\mathcal L_X\) names the sheaf of Lagrangian cycles. Its allowed carriers can have singularities and components of smaller dimension. A nonzero cycle itself will have pure dimension \(n\).

We will also use a closure fact. If a conic subanalytic isotropic \(\Lambda\) is locally closed, then its closure is still conic, subanalytic and isotropic, with the same dimension bound.

**Proof.** Closure preserves subanalyticity and dimension, and commutes with positive scaling. For each ambient point \(z\), the point normal cones of \(\Lambda\) and \(\overline\Lambda\) coincide. Indeed, approximate a sequence \(z_j\in\overline\Lambda\), with scales \(c_j\to\infty\), by points \(w_j\in\Lambda\) within \(1/(jc_j)\) in a fixed chart. The scaled differences have the same limit. The reverse inclusion is immediate. The canonical one-form kills those cones for \(\Lambda\), so the cone criterion makes it vanish on \(\overline\Lambda\). \(\square\)

## Locally closed support retains boundary germs

For a locally closed conic subanalytic isotropic \(\Lambda\), the more general form of (3) is

\[
 \begin{aligned}
 H^0_\Lambda\mathcal L_X
   &\simeq H^0_\Lambda(E_X)\\
   &\simeq j_{\Lambda*}H^{-n}
                  (\omega_\Lambda\otimes B_X|_\Lambda)
    \simeq H^0_\Lambda\mathcal Z_n(B_X).
 \end{aligned}
 \qquad\text{(5)}
\]

Here \(H^0_\Lambda F=H^0R\mathcal Hom(A_\Lambda,F)\), with the locally closed constant coefficient extended by zero. For a closed \(\Lambda\) it means the supported subsheaf. For a locally closed one it involves ordinary direct image from an open neighborhood in which \(\Lambda\) is closed. It need not be a subsheaf embedded into \(F\) on the full ambient space.

**Proof.** For a closed \(\Lambda\), any cycle supported there is already one of the allowed terms in (4), by (3). This proves the two cycle-sheaf support identifications. The exceptional support formula \(R\Gamma_\Lambda\omega_{T^*X}=j_{\Lambda*}\omega_\Lambda\), together with (2), gives the middle description and the actual maps.

For a locally closed \(\Lambda\), choose an open \(O\) in which it is closed. Its closure \(\overline\Lambda\) is an allowed carrier. On \(O\), the supported lowest sheaf on \(\overline\Lambda\) restricts to that on \(\Lambda\), by open restriction of the dualizing object. Thus these same cycle germs occur in \(\mathcal L_X|_O\). Conversely \(\mathcal L_X\subset\mathcal Z_n(B_X)\), whose supported lowest-degree identity is already proved. The closed-case argument on \(O\), followed by ordinary direct image, proves (5) on the original ambient space. All dualizing support objects involved start in degree \(-n\), so taking their lowest degree is exactly taking the degree-zero support of their lowest sheaf. \(\square\)

If \(\Lambda\) is smooth of dimension \(n\), restriction to \(\Lambda\) yields

\[
 (H^0_\Lambda\mathcal L_X)|_\Lambda
       \simeq\operatorname{or}_\Lambda\otimes_A B_X|_\Lambda.
 \qquad\text{(6)}
\]

Indeed \(\omega_\Lambda=\operatorname{or}_\Lambda[n]\).
If its dimension is strictly less than \(n\), the degree \(-n\) sheaf is zero. The same vanishing holds on any smaller-dimensional singular carrier by the lowest-dualizing bound.

Ordinary \(j_{\Lambda*}\) in (5) retains approach germs at the frontier. Exercise 4 explains why these do not automatically give a closed global cycle on \(\overline\Lambda\).

## A cycle has pure support and local dilation invariance

Let \(s\in\Gamma(U;\mathcal L_X)\), for an open \(U\subset T^*X\).
Its actual support is closed in \(U\), subanalytic there and, if nonempty, pure of dimension \(n\). It is isotropic and locally invariant under positive dilation. If \(U\) is conic, its support is conic for the full action.

**Proof.** The coefficient \(B_X\) is locally free of rank one, so the finite-rank chain support theorem applies to the inclusion (4). A local finite compatible cell refinement describes its nonzero coefficients on \(n\)-pieces; their closures give its closed subanalytic pure support. A germ has an allowed carrier \(\Lambda\), so its support near that germ is a subanalytic subset of \(\Lambda\). The one-form subset rule proves isotropy.

For dilation, a carrier and its regular locus are preserved by the positive analytic scaling maps. Away from the zero section, their regular \(n\)-pieces contain the radial direction, and their orientation coefficients are locally constant along it. The fibre sign line transports by positive scaling with sign plus. The cycle is determined by the coefficients on these regular pieces: its difference from another such description cannot be supported solely on a lower-dimensional frontier. Hence the cycle germs, and their vanishing, transport along a sufficiently small radial interval. Chaining those intervals proves support invariance along each connected portion of an orbit contained in \(U\). Zero-section orbits are fixed points. If \(U\) is invariant under the action, each positive orbit in it is connected, giving full conicity. \(\square\)

On a general open \(U\), disjoint portions of the same dilation orbit can have independent coefficients. This is the local interpretation of conicity for such a restricted sheaf; Exercise 4 makes the distinction explicit.

The cycle-support theorem proves pure isotropic support and local dilation invariance. Generalized involutivity requires a separate argument beyond the properties established here.

## External products use the ordered dualizing comparison

Let \(Y\) have dimension \(m\). Under
\(T^*(X\times Y)\simeq T^*X\times T^*Y\), product carriers
\(\Lambda_X\times\Lambda_Y\) are closed, conic, subanalytic and isotropic. The canonical one-form is the sum of the two factor forms, so it vanishes on the product. The dimension bound is \(n+m\).

The supported external evaluation product, followed by the ordered dualizing product, gives

\[
 \begin{aligned}
 H^0_{\Lambda_X}(E_X)\boxtimes_A
                 H^0_{\Lambda_Y}(E_Y)
 &\longrightarrow
 H^0_{\Lambda_X\times\Lambda_Y}(E_X\boxtimes_A^L E_Y)\\
 &\longrightarrow
 H^0_{\Lambda_X\times\Lambda_Y}
                   (\pi_{X\times Y}^{-1}\omega_{X\times Y}).
 \end{aligned}
 \qquad\text{(7)}
\]

The last map is inverse image of the actual ordered manifold product
\(\omega_X\boxtimes^L\omega_Y\simeq\omega_{X\times Y}\).
It is fixed as the mate of the two factor compact traces, integrated in factor order. All shifts and their graded symmetries stay in this comparison. We do not replace it by separately chosen unshifted orientation bases.

Both supported factor objects begin in degree zero, by (3). Their degree-zero classes therefore have the indicated natural product into degree zero of the derived tensor; no flatness of those lowest support modules is required. The supported-evaluation construction keeps the product carrier. Taking common upper carriers in (4) makes (7) well defined and yields

\[
 \mathcal L_X\boxtimes_A\mathcal L_Y
                \longrightarrow\mathcal L_{X\times Y}.
 \qquad\text{(8)}
\]

Its associativity follows from the associativity of evaluation, proper-support projection and the ordered traces that define the dualizing comparison. A zero-dimensional factor multiplies coefficients with its point trace. The product support can be smaller than the product of two nonzero supports when coefficients multiply to zero; Exercise 6 checks this.

## A direct image has a cotangent incidence domain

For an analytic \(f:Y\to X\), write

\[
 \begin{gathered}
 C_f=Y\times_XT^*X,\qquad \pi:C_f\to Y,\\
 f_\pi(y;\xi)=(f(y);\xi)\in T^*X,\qquad
 f_d(y;\xi)=(y;df_y^t\xi)\in T^*Y.
 \end{gathered}
 \qquad\text{(9)}
\]

Choose a closed conic subanalytic isotropic \(\Lambda_Y\subset T^*Y\).
The required direct-image hypothesis is

\[
 f_\pi\text{ proper on }A_f=f_d^{-1}(\Lambda_Y).
 \qquad\text{(10)}
\]

The geometric transport theorem proves that
\(\Lambda_X'=f_\pi(A_f)\) is closed, conic, subanalytic and isotropic.
The canonical-form equality
\(f_d^*\alpha_Y=f_\pi^*\alpha_X\) has no antipode or minus sign.
Properness in (10) controls the actual incidence, including its zero covectors.

We construct the operation by the full typed chain

\[
 \begin{aligned}
 H^0_{\Lambda_Y}(T^*Y;E_Y)
 &\longrightarrow H^0_{A_f}(C_f;\pi^{-1}\omega_Y)\\
 &\longrightarrow H^0_{\Lambda_X'}(T^*X;Rf_{\pi!}\pi^{-1}\omega_Y)\\
 &\longrightarrow H^0_{\Lambda_X'}(T^*X;E_X).
 \end{aligned}
 \qquad\text{(11)}
\]

The first arrow is supported inverse-image evaluation under \(f_d\);
\(f_d^{-1}E_Y=\pi^{-1}\omega_Y\).
For the second, sections supported on the closed \(A_f\) have proper support over \(T^*X\), by (10). On objects supported on \(A_f\), proper and ordinary direct image agree. Thus supported global sections give the displayed map through \(Rf_{\pi!}\), with the closed output support \(\Lambda_X'\) retained. This argument applies to derived supported sections, using the closed inclusion of \(A_f\).

The square with horizontal maps \(f_\pi,f\) and vertical maps
\(\pi,\pi_X\) is Cartesian. Proper-support base change and the actual trace for \(f\) give the coefficient map

\[
 Rf_{\pi!}\pi^{-1}\omega_Y
      \simeq \pi_X^{-1}Rf_!\omega_Y
      \xrightarrow{\pi_X^{-1}\operatorname{tr}_f}
             \pi_X^{-1}\omega_X.
 \qquad\text{(12)}
\]

Here \(f^!\omega_X=\omega_Y\) by exceptional composition. The trace is defined for the map even when it is not globally proper; the support condition governs the sections to which it is applied. The finite-dimensional proper-support base-change prerequisite applies to this actual Cartesian square and this bounded dualizing input.

The output of (11) belongs to \(\mathcal L_X\), by its allowed carrier. This defines the direct image \(f_*\) of a Lagrangian cycle under (10). For \(f=\operatorname{id}\), both cotangent maps, the support comparisons and the trace are identities, so this is the identity operation. Enlarging a carrier compatibly leaves the result unchanged whenever the properness condition remains valid.

The inverse cycle operation instead assumes properness of \(f_d\) on
\(f_\pi^{-1}(\Lambda_X)\) and needs a different coefficient map. Its proof cannot be obtained merely by reversing (11). We retain that task for the next lesson.

## Exercises with complete solutions

### A lower-dimensional carrier contributes no Lagrangian cycle

*Difficulty: Intermediate.*

For \(X=\mathbb R\), compute the supported cycle sheaf on a cotangent fibre and on its single zero covector. On the cross consisting of the zero section and this fibre, calculate the conservation condition at their intersection using outward orientations on its four rays.

**Solution.** Here \(n=1\), the fibre sign line is trivialized by increasing \(\xi\), and a smooth full cotangent fibre is a one-manifold. Formula (6) gives its orientation coefficient \(A\), with this fibre coefficient included. A single covector has dimension zero; its dualizing object begins in degree zero, so its degree-\(-1\) term vanishes. It contributes no one-cycle to (3).

The cross has four outgoing half-rays. Let their weights be
\((a,b,c,d)\). The terminal-minus-initial boundary at their common vertex is
\(-(a+b+c+d)[0]\). Thus the supported cycle germ is
\[
 \{(a,b,c,d)\in A^4:a+b+c+d=0\}.
 \qquad\text{(13)}
\]
It is isomorphic to \(A^3\), by solving for the fourth coefficient; no division or field hypothesis is required. Its nonzero pieces remain one-dimensional. The vertex enforces the conservation law rather than furnishing an independent lower-dimensional cycle coefficient.

### The two orientation changes cancel on the zero section

*Difficulty: Advanced.*

In dimension two, consider a base chart change that reflects one coordinate. Compute its signs on the base orientation, the cotangent-fibre orientation and the total cotangent orientation. Explain why a zero-section cycle with the coefficient \(B_X\) can be canonical even when the base is nonorientable.

**Solution.** A reflection has base determinant sign \(-1\). Its cotangent coordinate change uses the inverse transpose, which also has determinant sign \(-1\). The total cotangent change therefore has sign
\((-1)(-1)=+1\). The fibre sign line \(B_X\) retains the second minus sign even though the total space orientation does not change.

On the zero section \(\Lambda=X\), its tangent orientation line is
\(\operatorname{or}_X\), and the dual-frame identification gives
\(B_X|_\Lambda\simeq\operatorname{or}_X\). Thus (6) has coefficient
\[
 \operatorname{or}_\Lambda\otimes B_X|_\Lambda
        \simeq\operatorname{or}_X\otimes\operatorname{or}_X
        \simeq A_X.
 \qquad\text{(14)}
\]
The two local minus signs cancel, so the section \(1\) of this coefficient glues across an orientation-reversing overlap. This produces a canonical twisted zero-section cycle on a nonorientable base. Dropping \(B_X\) would instead leave the orientation obstruction. Its later identification with the fundamental cycle defined by the inverse operation requires that operation's normalization.

For this same dimension, \(\omega_X=o_X[2]\), while
\(\omega_{T^*X}\) has degree \(-4\). The shift \([-2]\) in (2) produces degree \(-2\), as required for the Lagrangian two-cycle interpretation. Total cotangent orientability does not erase that shift or the relative coefficient.

### A corner can balance two conic rays

*Difficulty: Intermediate.*

In \(T^*\mathbb R\), take the right-hand zero-section ray
\(H=\{x\geq0,\xi=0\}\) and the positive fibre ray
\(V=\{x=0,\xi\geq0\}\). Orient both away from the origin and trivialize \(B_X\) by the positive fibre orientation. Determine the weights that make their union a cycle. Is either ray alone a nonzero global cycle?

**Solution.** Both rays are closed, conic and semianalytic.
The canonical form \(\xi\,dx\) vanishes on each: \(\xi=0\) on \(H\), and \(dx=0\) on \(V\). It also vanishes on their union by the finite-union rule. Their boundary weights are respectively \(-a[0]\) and \(-b[0]\), so the union is a cycle exactly when \(a+b=0\). In particular
\[
 [H]-[V]
 \qquad\text{(15)}
\]
is a cycle, with support both rays when \(1\ne0\) in \(A\).
Each ray alone has a nonzero boundary for a nonzero coefficient, and is not a global cycle. Their two-dimensional ambient location does not change their one-dimensional boundary law.

The corner is singular at its vertex, but its support is pure of dimension one and isotropic. This computation establishes the cycle and its support; it does not add a generalized involutivity assertion.

### Locally closed and locally conic mean different things

*Difficulty: Advanced.*

Let \(\Lambda=\{x=0,\xi>0\}\subset T^*\mathbb R\).
Compare \(H^0_\Lambda\mathcal L_X\) with closed cycles supported on
\(\overline\Lambda\). Then restrict the full fibre's cycle sheaf to
\[
 U=(-\epsilon,\epsilon)\times((1,2)\cup(3,4)).
 \qquad\text{(16)}
\]
Can its coefficients be \(1\) on the first fibre interval and \(0\) on the second?

**Solution.** The locally closed \(\Lambda\) is a positively oriented one-manifold. Formula (5) gives the ordinary image of its rank-one orientation coefficient. That image has a nonzero germ at \((0,0)\), because every small neighborhood meets a connected positive fibre interval. Its section represented by weight \(a\) corresponds to the open ray chain with boundary \(-a[0]\). The locally closed support functor retains this approach germ and permits this frontier.

For the closed half-fibre \(\overline\Lambda\), a global cycle would require that endpoint boundary to vanish. Over \(A\), the map on its endpoint is multiplication by \(-1\), so only the zero constant weight gives a global cycle on this sole carrier. Its lowest dualizing sheaf is the positive-ray orientation extended by zero, whose endpoint stalk is zero. Thus an ordinary-image approach germ is not a closed cycle germ on the full half-fibre.

The two strips in (16) are disjoint. The full fibre's cycle coefficient is constant on each connected interval, and a sheaf section can independently choose \(1\) and \(0\). Its support in \(U\) is the first fibre interval, closed relative to \(U\) and pure of dimension one. Dilation preserves that support along connected orbit portions inside \(U\). A larger dilation can send a point of the first interval to the second while passing through the gap outside \(U\); the section need not have the same weight there. Hence full orbit invariance on an arbitrary disconnected nonconic \(U\) would be too strong. On a conic open domain, (as proved above) the entire positive orbit lies in the domain and invariance is global along it.

### Proper cotangent incidence for a nonproper projection

*Difficulty: Advanced.*

For \(f:\mathbb R^2_{u,v}\to\mathbb R_x\), \(f(u,v)=u\), compare
\(\Lambda_Y=T^*_{\{(0,0)\}}\mathbb R^2\) with the zero section of \(T^*\mathbb R^2\). Compute the incidence and its direct-image carrier. Identify where the proof of (11) applies or fails.

**Solution.** Write a correspondence point as \((u,v;\xi)\).
Then \(f_d(u,v;\xi)=(u,v;\xi,0)\), and
\(f_\pi(u,v;\xi)=(u;\xi)\).
For the point fibre,
\[
 A_f=\{u=v=0,\ \xi\in\mathbb R\},\qquad
 f_\pi(A_f)=T^*_{\{0\}}\mathbb R.
 \qquad\text{(17)}
\]
The restriction is a homeomorphism onto this closed target fibre and is proper. Its target compact inverse images are compact even though \(f\) itself has noncompact \(v\)-fibres. The point conormal is an allowed two-dimensional isotropic carrier, and (11) defines its cycle direct image on the displayed one-dimensional target carrier by supported pullback, proper incidence image and the coefficient trace (12).

For the zero section, \(df^t\xi=(\xi,0)\) must be zero, so
\(A_f=\{\xi=0,\ u,v\text{ arbitrary}\}\).
Its fibre over \((u_0;0)\) under \(f_\pi\) is the whole \(v\)-line, noncompact. The hypothesis (10) fails. Although the set image is the zero section of \(T^*\mathbb R\), the second arrow of (11) cannot push arbitrary sections on this incidence with proper support. A familiar image set does not repair the missing support condition.

These are direct-image incidence calculations. They do not verify the distinct properness condition for the inverse cycle operation.

### Point factors and zero-divisor coefficients

*Difficulty: Intermediate.*

Compute the Lagrangian cycle sheaf for a point and its external product with \(\mathcal L_Y\). Then take \(A=\mathbb Z\times\mathbb Z\) and two point cycles with weights \(a=(1,0)\), \(b=(0,1)\). Explain why their product has empty support despite two nonzero inputs.

**Solution.** For a point, \(n=0\), the cotangent bundle is the point,
\(\omega=A\), and \(B=A\). The single allowed carrier gives
\(\mathcal L_{\mathrm{pt}}=A\) in degree zero. Its trace is the identity. The ordered comparison (7) with this factor is therefore ordinary scalar multiplication:
\[
 a\boxtimes\lambda=a\lambda
       \quad\text{under }\{\mathrm{pt}\}\times Y\simeq Y.
 \qquad\text{(18)}
\]
There is no nonzero degree to permute in the point factor.

The product ring has finite global dimension one: its modules decompose by its two idempotents into pairs of \(\mathbb Z\)-modules, and projective resolutions and their length are computed in those two components. Thus it satisfies the standing coefficient condition. The two displayed weights are nonzero, but \(ab=(0,0)\). The external product of the two point cycles is zero and has empty support. Its support is contained in the product carrier as (7) requires; equality with the product of the input supports is not asserted. The pure-support theorem allows this zero case.
