# Lagrangian cycles and proper cotangent images

A Lagrangian cycle combines an \(n\)-dimensional cycle in a \(2n\)-dimensional cotangent bundle with the orientation of the cotangent fibres. The coefficient is essential on a nonorientable base. Singular carriers are allowed, but their regular pieces must satisfy the cycle conservation law. A cotangent direct image then uses properness on an incidence set, which can hold even when the base map is nonproper.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

Subanalytic chains and closed cycle supports constructs the cycle complex and its supported dualizing description. Supports, products and proper images of chains proves its finite locally free coefficient and pure-support comparisons, and The dualizing resolution by subanalytic chains identifies the complex with the dualizing object. The geometric input is the singular one-form calculus and proper cotangent transport. We give the dimension, support, product and direct-image application arguments below, using the actual relative-dualizing, base-change and trace maps at their indicated proof locations.

The twisted conormal coefficient and Lagrangian-chain framework are due to M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197. The construction here proves the carrier, product and proper direct-image operations through their supported sheaf maps. The pullback coefficient map and the section-intersection comparison are treated in Pulling back Lagrangian cycles through a graph and Continuous sections and supported cycle intersections.

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

The first isomorphism is the submersion tensor comparison (M11) for \(\pi_X\), followed by exceptional composition. Put \(L=B_X[n]\); its tensor inverse is \(L^{-1}=B_X[-n]\), using the integral orientation square \(B_X\otimes B_X\simeq A\). To specify the second isomorphism, start from \((L\otimes E_X)\otimes L^{-1}\), move \(L^{-1}\) past \(E_X\) with the graded symmetry, and evaluate the adjacent inverse pair. This is the ordered cancellation convention (M16)–(M19). All shift signs are part of that symmetry and evaluation. In a local integral orientation frame the square pairing sends \(e\otimes e\) to \(1\); replacing \(e\) by \(-e\) leaves it unchanged. Thus the map glues on a nonorientable base, without choosing unrelated orientation trivializations of its factors.

For a closed subanalytic \(\Lambda\subset T^*X\) of dimension at most \(n\), exceptional composition and finite local freeness give

\[
 H^0_\Lambda(E_X)
 \simeq j_{\Lambda*}H^{-n}(\omega_\Lambda\otimes B_X|_\Lambda)
 \simeq H^0_\Lambda\mathcal Z_n(B_X).
 \qquad\text{(3)}
\]

These are sheaves on \(T^*X\). Indeed, for the closed inclusion \(j_\Lambda\), the closed-support adjunction and exceptional composition give \(R\Gamma_\Lambda\omega_{T^*X}=j_{\Lambda*}\omega_\Lambda\). Tensoring with the locally free line \(B_X\) commutes with this supported internal-Hom operation: locally it is tensor with \(A\), and evaluation makes these local identifications compatible with orientation changes. Apply (2) to obtain \(R\Gamma_\Lambda E_X\simeq j_{\Lambda*}(\omega_\Lambda\otimes B_X|_\Lambda)[-n]\). The singular dualizing bound \(\omega_\Lambda\in D^{\geq-n}\) makes this object lie in \(D^{\geq0}\). Its degree-zero sheaf is exactly the middle term of (3), and the closed-cycle support identity gives the last term. These are the natural support and coefficient maps; the shift changes supported degree \(-n\) to zero while leaving the geometric cycle dimension \(n\).

## Closed isotropic carriers form a directed system

All conicity means invariance under every strictly positive cotangent scaling. We use symplectic isotropy on the regular locus of a subanalytic set. For a conic set this is equivalent to vanishing there of the canonical one-form \(\alpha_X\). To check the equivalence, scaling preserves the regular locus, so the radial vector field \(R=\sum\xi_i\partial_{\xi_i}\) is tangent to it. With \(\alpha_X=\sum\xi_i dx_i\), we have \(\iota_Rd\alpha_X=\alpha_X\). Thus symplectic isotropy implies one-form vanishing on a conic regular piece. Conversely, differentiating the pulled-back one-form proves vanishing of the two-form. At a zero covector the one-form itself is zero. This is the conic convention in the singular-form theorem; without conicity, a nonzero pulled-back one-form does not disprove symplectic isotropy.

Let \(\mathscr I_X\) be the family of closed, conic, subanalytic isotropic subsets. Each regular tangent space \(V\) is symplectically isotropic in dimension \(2n\), so \(V\subset V^\perp\) and \(\dim V^\perp=2n-\dim V\) give \(\dim V\leq n\). Taking the maximum of the regular dimensions yields \(\dim\Lambda\leq n\) for every \(\Lambda\in\mathscr I_X\).

Finite unions remain closed, conic and subanalytic. They also remain isotropic at their singular intersections. In a chart, the singular-form test says that vanishing of an analytic one-form on a subanalytic set is equivalent to its annihilating every point normal cone. A sequence approaching a point through a finite union has a subsequence in one member, so its point-cone vector belongs to one member's cone. The canonical form therefore kills every cone of the union. The same test gives vanishing on its regular locus, hence isotropy. Thus \(\mathscr I_X\) is directed by inclusion.

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

**Proof.** Closure preserves subanalyticity and dimension. Every positive dilation is a homeomorphism, so it preserves \(\overline\Lambda\) as well. The point-cone form test also proves the required one-form statement at new boundary points. Fix an ambient point \(z\). Given \(z_j\in\overline\Lambda\) tending to \(z\), and \(c_j\to\infty\) with \(c_j(z_j-z)\) convergent, choose \(w_j\in\Lambda\) within \(1/(jc_j)\) of \(z_j\) in the same chart. Then \(w_j\to z\) and the scaled differences have the same limit. This proves equality of the point cones of \(\Lambda\) and \(\overline\Lambda\); the reverse containment is immediate. The canonical one-form annihilates these cones, including those based outside the original set, so it vanishes on the closure. Its dimension is still at most \(n\). \(\square\)

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

**Proof.** For a closed \(\Lambda\), (3) identifies all cycles supported there with one of the allowed terms in (4). The colimit maps are inclusions, so taking the supported subsheaf of \(\mathcal L_X\) gives precisely that term. This proves both cycle-sheaf support identifications. The supported complex calculated after (3) gives the middle description and fixes its maps.

For locally closed \(\Lambda\), choose an open inclusion \(j:O\hookrightarrow T^*X\) with \(\Lambda\) closed in \(O\); then \(\overline\Lambda\cap O=\Lambda\). The closure is an allowed global carrier, so its term in (4), restricted to \(O\), contains all the cycle germs supported on \(\Lambda\). Conversely the inclusion \(\mathcal L_X\subset\mathcal Z_n(B_X)\) bounds its supported germs by precisely those cycles. Thus the closed-case equality holds on \(O\), even if \(O\) is not conic. For any coefficient object \(F\), the locally closed support formula is \(R\Gamma_\Lambda F=Rj_*R\Gamma_\Lambda^O(F|_O)\). The internal-Hom description in (5) makes this independent of \(O\). Apply ordinary direct image to the supported lowest sheaf just identified on \(O\). The complexes on that support start in degree zero, so their degree-zero derived ordinary image is the ordinary image of their degree-zero sheaf. This proves (5) on the full cotangent space, including its approach germs at the frontier. It does not embed that ordinary image back into \(\mathcal L_X\). \(\square\)

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

For the dilation assertion, work near a point where the section is represented on one closed conic carrier \(\Lambda\). Choose a smaller neighborhood whose closure lies in that representative neighborhood. For all dilations sufficiently close to the identity, the whole short scaling path of this smaller neighborhood stays in the representative neighborhood. Scaling preserves \(\Lambda\) and its regular locus. On each regular \(n\)-piece, it transports the orientation continuously from the identity, and its action on the fibre sign line is positive. The coefficient of a cycle in this local orientation line is locally constant. It therefore agrees with its transported coefficient along the short scaling path.

This agreement on regular \(n\)-pieces is agreement of the full cycle germs: their difference is a cycle with locally free coefficient \(B_X\) supported in the complement of the top regular pieces, a subanalytic set of dimension less than \(n\). The pure-support theorem forces that difference to vanish. The argument thus applies at singular points as well. Chaining the short intervals shows that the vanishing or nonvanishing of the section propagates along each connected portion of a dilation orbit contained in \(U\). Zero-section points are fixed by scaling. If \(U\) is conic, every positive orbit lies entirely in \(U\) and is connected, so the actual support is fully conic. \(\square\)

On a general open \(U\), disjoint portions of the same dilation orbit can have independent coefficients. This is the local interpretation of conicity for such a restricted sheaf; Exercise 4 makes the distinction explicit.

These conclusions give pure isotropic support and local dilation invariance. For a section on the full cotangent bundle its actual support is therefore itself a closed conic subanalytic isotropic carrier. Applying (5) to that carrier represents the section by its own supported dualizing class, without commuting global sections with the sheaf colimit (4).

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

Here is the supported map and its degree-zero passage. Put \(K_X=R\Gamma_{\Lambda_X}E_X\) and \(K_Y=R\Gamma_{\Lambda_Y}E_Y\). The closed constant sheaves \(A_{\Lambda_X},A_{\Lambda_Y}\) are flat, with stalks \(A\) or zero, and their external tensor is \(A_{\Lambda_X\times\Lambda_Y}\). Tensor the evaluations defining \(K_X,K_Y\), place each constant argument next to its factor using the graded symmetry, and curry. This gives \(K_X\boxtimes^L K_Y\to R\Gamma_{\Lambda_X\times\Lambda_Y}(E_X\boxtimes^LE_Y)\), the external version of the supported evaluation product.

The supported complexes \(K_X,K_Y\) lie in \(D^{\geq0}\), by (3). Their canonical truncation maps \(H^0K_X\to K_X\), \(H^0K_Y\to K_Y\) give, after derived external tensor and degree-zero cohomology, the first arrow of (7): its source is \(H^0(H^0K_X\boxtimes^L H^0K_Y)=H^0K_X\boxtimes H^0K_Y\). This uses no flatness of the lowest support modules; lower Tor groups may exist and are not being declared zero. Naturality of evaluation makes this product commute with enlargement of each carrier and with restriction to an open set. It therefore passes to common upper carriers in (4), giving

\[
 \mathcal L_X\boxtimes_A\mathcal L_Y
                \longrightarrow\mathcal L_{X\times Y}.
 \qquad\text{(8)}
\]

For three factors, both parenthesizations tensor the same three evaluations in the same order and transpose the same ordered three compact traces. Associativity of proper-support projection and exceptional composition identifies these maps. Thus (8) is associative as a specified operation, including its shifted orientation comparisons. A zero-dimensional factor uses the identity point trace and multiplies coefficients. Product support is only required to lie in the product carrier: it can shrink when coefficients multiply to zero, as Exercise 6 shows.

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

The incidence \(A_f\) is closed and subanalytic because \(f_d\) is analytic and \(\Lambda_Y\) is closed subanalytic; it is conic because \(f_d\) commutes with scaling. Properness of \(f_\pi|_{A_f}\) makes its image closed, and proper subanalytic image calculus makes it subanalytic. In local coordinates, evaluating either pulled-back canonical form on a tangent vector gives \(\sum_i\xi_i\,df_i\), so \(f_d^*\alpha_Y=f_\pi^*\alpha_X\), with no antipode or minus sign. The singular-form pullback and surjective-detection arguments imply first that this form vanishes on \(A_f\), and then that \(\alpha_X\) vanishes on its now-known subanalytic image. The image is conic as well, hence is an allowed carrier \(\Lambda_X'=f_\pi(A_f)\). This is the proper direct-transport theorem applied to the actual incidence, including zero covectors. No rank or noncharacteristic assumption on \(df\) is used.

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

Represent an input class by a derived morphism \(u:A_{\Lambda_Y}\to E_Y\) on \(T^*Y\), where the constant sheaf is extended by the closed inclusion. This represents precisely \(H^0_{\Lambda_Y}(T^*Y;E_Y)\) by supported internal-Hom adjunction. Ordinary inverse image is exact and identifies \(f_d^{-1}A_{\Lambda_Y}=A_{A_f}\) and \(f_d^{-1}E_Y=\pi^{-1}\omega_Y\). Hence \(v=f_d^{-1}u:A_{A_f}\to\pi^{-1}\omega_Y\) is the first supported class in (11). This is ordinary supported inverse image, not an exceptional inverse image requiring an extra dimension shift.

Write \(q=f_\pi\) and \(D=\Lambda_X'\). Closed-constant restriction gives \(q^{-1}A_D\to A_{A_f}\). Its ordinary adjoint is \(A_D\to Rq_*A_{A_f}\). Because \(q\) is proper on the closed \(A_f\), the natural comparison \(Rq_!A_{A_f}\to Rq_*A_{A_f}\) is an isomorphism: factor the coefficient object through its closed inclusion and use the proper restricted map. Invert this comparison and apply \(Rq_!v\). The composite \(A_D\to Rq_*A_{A_f}\simeq Rq_!A_{A_f}\to Rq_!\pi^{-1}\omega_Y\) is exactly the second supported class in (11). This constructs that arrow in the derived category, retains its closed output support, and does not treat the ambient map \(q\) as proper.

The square with horizontal maps \(f_\pi,f\) and vertical maps
\(\pi,\pi_X\) is Cartesian. Proper-support base change and the actual trace for \(f\) give the coefficient map

\[
 Rf_{\pi!}\pi^{-1}\omega_Y
      \simeq \pi_X^{-1}Rf_!\omega_Y
      \xrightarrow{\pi_X^{-1}\operatorname{tr}_f}
             \pi_X^{-1}\omega_X.
 \qquad\text{(12)}
\]

Exceptional composition identifies \(f^!\omega_X\) with \(\omega_Y\), so the last arrow of (12) is the actual counit \(Rf_!f^!\omega_X\to\omega_X\), pulled back by \(\pi_X\). The first arrow is the inverse of the proper-support base-change isomorphism for the displayed Cartesian square. Its proof pulls properly supported sections back to the same fibres and uses a fibrewise acyclic resolution; it does not require \(f\) to be globally proper. Here the fibres of \(f\) are closed subsets of the finite-dimensional manifold \(Y\), so the required integral cohomological dimension bound holds, and \(\omega_Y\) is bounded. Base change preserves the normalized trace by its defining transpose. Thus (12) introduces precisely the coefficient and shift maps already fixed by exceptional composition, with no new orientation choice.

Composing the supported morphism just constructed with (12) gives \(A_D\to E_X\), hence a class in \(H^0_D(T^*X;E_X)\). Since \(D\) is an allowed carrier, (3)–(4) identify it with a global section of \(\mathcal L_X\). For a global input cycle one may use its actual support as \(\Lambda_Y\), by the preceding pure-support and dilation argument; whenever (10) holds on that incidence, (11) defines \(f_*\) of the cycle.

The construction commutes with enlargement of an allowed carrier: closed-constant restriction, ordinary unit, proper comparison and trace are all natural for its inclusion. If two allowed carriers give the same cycle and both satisfy (10), their union also does: its incidence is the union of the two closed incidences, and the inverse image of a compact target set is a union of two compact sets. Comparing both maps through that common upper carrier proves independence. For \(f=\mathrm{id}\), all these cotangent maps, units, proper comparisons and traces are identities, so the resulting operation is exactly the identity.

The inverse cycle operation instead assumes properness of \(f_d\) on \(f_\pi^{-1}(\Lambda_X)\) and uses a different coefficient map. Pulling back Lagrangian cycles through a graph constructs that map with its graph and relative-dualizing normalization; reversing the arrows in (11) would not produce it.

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

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–1.6 and 2.1–2.3, pp. 196–197, describes coefficient-valued chains, the canonical cotangent orientation, and the orientation pairing that gives a conormal its twisted fundamental chain. Its characteristic-cycle discussion in §3 then fixes a field. The finite-global-dimension coefficient ring here is retained through the programme's proved chain and dualizing constructions.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4, 4.6.6–4.6.7, §4.7 and Proposition 5.1.9, pp. 95–98 and 107–108, treats the exceptional composition, support, tensor and submersion identities. The linked programme proofs fix the actual counits and orientation comparisons. The present argument constructs the sheaf of allowed cycles, proves its local dilation and support properties, and defines direct transport by a supported ordinary unit followed by proper comparison and trace. Its examples test singular conservation, nonorientable coefficients, open-frontier germs, nonproper base maps and zero divisors. The human sources retain their authorship and their own terms.
