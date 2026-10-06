# Integer coefficients and additive characteristic cycles

A characteristic cycle is defined by a microlocal identity and a trace. Its generic coefficients have a simpler description: each is the Euler characteristic of a finite coefficient complex. We prove why that complex is finite, how its integer coefficient extends through singularities, and why one distinguished triangle gives an additive identity of cycles.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Author self-check recorded relative to the prerequisites below; not independently reviewed. New original text is public domain (CC0).*

Use Characteristic cycles from supported microlocal identities for the actual definition, invariance and constructible localized roofs, and Transporting characteristic cycles through a graph for normalized finite constant conormals. Perfect operations and finite microlocal coefficients proves perfection of microlocal Hom. Subanalytic chains and closed cycle supports supplies the dense-piece comparison maps and frontier boundary, while Lagrangian cycles and proper cotangent images supplies the cotangent orientation coefficient. The geometric inputs are compatible analytic stratification and the owned pure-Lagrangian consequence of Involutive subsets of subanalytic isotropic sets.

The prerequisites are the supported coefficient-model theorem in Local models and change of ambient manifold, the submanifold comparison and composition units in Local morphisms in cotangent directions, and the graded point-localized morphism theorem in Categories and operations in one cotangent direction. For the smooth nonzero-covector geometry, the lesson Prescribed canonical coordinates and isotropic fibers, Theorem 5.1 proves that a conic Lagrangian with locally constant base-projection rank is a local open conormal germ. It does not supply compatible subanalytic stratifications; that separate prerequisite is stated in the preceding paragraph. The rank calculation and the Lagrangian-chain definition follow M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1–3.

## Local ranks use an actual derived constant model

Let \(k\) be a field of characteristic zero. Manifolds are real analytic, Hausdorff and countable at infinity, with uniformly bounded finite dimension. Work on a component \(X\) of dimension \(n\). All constructible complexes are bounded with finite-dimensional cohomology stalks. A closed analytic embedding \(i:Z\hookrightarrow X\) is understood locally when \(Z\) is only locally closed. Write \(V_Z=i_*a_Z^{-1}V\) for a constant coefficient complex extended by zero.

Suppose \(A\in D^b(k_Z)\) has locally constant cohomology sheaves of finite ranks \(m_j\). On each connected component of \(Z\), the ranks are constant. Then

\[
 CC(i_*A)=\left(\sum_j(-1)^jm_j\right)[T_Z^*X].
 \qquad\text{(1)}
\]

**Proof.** Around a point of \(Z\), choose a contractible analytic coordinate ball \(U\) on which all the finitely many nonzero cohomology sheaves of \(A\) are constant. Let \(a_U:U\to\{\mathrm{pt}\}\) and put

\[
 V=R\Gamma(U;A),\qquad
 a_U^{-1}V\xrightarrow{\ \epsilon\ }A|_U.
 \qquad\text{(2)}
\]

The arrow is the ordinary constant-section counit. The hypercohomology spectral sequence has terms \(H^q(U;H^jA)\), which vanish for \(q>0\). Its edge maps give \(H^jV=\Gamma(U;H^jA)\). Evaluation at every point of \(U\) is an isomorphism because those cohomology sheaves are constant. Thus (2) is an isomorphism on all cohomology stalks and hence in the derived category. The complex \(V\) is bounded and finite.

Shrink an ambient neighborhood \(W\) so that \(Z\cap W=U\) is closed in \(W\). Normalized constant conormals give

\[
 CC(V_U)=\chi(V)[T_U^*W],\qquad
 \chi(V)=\sum_j(-1)^j\dim_k H^jV.
 \qquad\text{(3)}
\]

Characteristic cycles and their defining kernel maps commute with restriction to \(W\). The local formulas (3) therefore agree on overlaps and glue to (1). The counit proof uses local contractible balls; it permits arbitrary monodromy of \(A\) on \(Z\). \(\square\)

For example, a rank-\(d\) local system on a circle has local zero-section coefficient \(d\). Its global cohomology Euler characteristic is zero. Local conormal rank in (1) is calculated before any proper image to a point.

## Lagrangian chains retain their frontier boundary

Write

\[
 \pi:T^*X\to X,\qquad B=\operatorname{or}_{T^*X/X},\qquad
 E=\pi^{-1}\omega_X
       \simeq\omega_{T^*X}\otimes B[-n].
 \qquad\text{(4)}
\]

The coefficient \(B\) is the orientation sign line of the cotangent fibre. Its integral version will be denoted \(B_{\mathbb Z}\); \(B=B_{\mathbb Z}\otimes k\). The comparison in (4) is the actual relative dualizing identification with its fixed graded order.

For a locally closed subanalytic conic isotropic \(\Lambda\subset T^*X\), its dimension is at most \(n\). The lowest-dualizing comparison gives

\[
 H^0_\Lambda(E)
   \simeq j_{\Lambda*}H^{-n}
                 (\omega_\Lambda\otimes B|_\Lambda).
 \qquad\text{(5)}
\]

Here \(H^0_\Lambda\) is degree zero of sheaf \(R\mathcal Hom(k_\Lambda,-)\). Ordinary \(j_{\Lambda*}\) retains approach germs at the frontier. On a smooth \(n\)-dimensional piece, (5) is its orientation line tensored with \(B\). A piece of dimension strictly less than \(n\) contributes zero.

We define the sheaf of Lagrangian chains by the dense-piece colimit of (5):

\[
 \mathcal{CL}_X
    =\underset{\Lambda}{\operatorname{colim}}H^0_\Lambda(E),
 \qquad
 \mathcal L_X\subset\mathcal{CL}_X\subset\mathcal C_n^{T^*X}(B),
 \qquad
 \mathcal L_X=\mathcal{CL}_X\cap\ker\partial_n.
 \qquad\text{(6)}
\]

The transition maps in this colimit need to be specified. Use the chain comparison preorder: \(\Lambda_1\preceq\Lambda_2\) when a conic subanalytic \(V\subset\Lambda_1\cap\Lambda_2\) is open in \(\Lambda_1\), closed in \(\Lambda_2\), and \(\dim(\Lambda_1\setminus V)<n\). Restriction to \(V\), followed by its closed-support trace into \(\Lambda_2\), defines the map in (5). The lowest-dualizing bound and the dense-piece comparison prove independence of the witness and compatibility with composition. Tensoring with the locally free sign line \(B\) preserves these maps.

**Proof of (6).** The comparison system stays within conic isotropic sets. Indeed their closures remain conic subanalytic isotropic, and the common successor

\[
 R=(\Lambda_1\setminus\partial\Lambda_2)
        \cup(\Lambda_2\setminus\partial\Lambda_1),
 \qquad\partial\Lambda=\overline\Lambda\setminus\Lambda,
 \qquad\text{(7)}
\]

is locally closed, conic and isotropic. The witnesses \(\Lambda_i\setminus\partial\Lambda_j\) are open in \(\Lambda_i\), closed in \(R\), and discard only dimension \(<n\). These are precisely the comparisons already proved for subanalytic top chains.

In a relatively compact subanalytic chart, take a finite compatible subdivision of a representative and its frontier. Its smooth open \(n\)-cells carry the orientation coefficients in (5). The map into \(\mathcal C_n(B)\) sends them to those same oriented cell coefficients. On a common finite subdivision, a difference vanishes in chains exactly when every top-cell coefficient vanishes. The dense-piece comparison then makes the difference zero in the colimit as well. This proves the embedding.

The closed isotropic representatives defining \(\mathcal L_X\) map to chains with zero frontier boundary. Conversely, represent a germ of \(\mathcal{CL}_X\) on \(\Lambda\). Its boundary is the connecting map in the frontier triangle. The exact lowest-degree sequence is

\[
 0\longrightarrow
 j_{\overline\Lambda*}H^{-n}(\omega_{\overline\Lambda}\otimes B)
 \longrightarrow j_{\Lambda*}H^{-n}(\omega_\Lambda\otimes B)
 \xrightarrow{\ \partial\ }
 j_{\partial\Lambda*}H^{1-n}(\omega_{\partial\Lambda}\otimes B).
 \qquad\text{(8)}
\]

A boundary zero in chains is zero in the closed frontier cycle sheaf, by its proved injection into chains. Exactness therefore lifts the germ to the closed carrier \(\overline\Lambda\). That carrier is allowed in \(\mathcal L_X\). This proves the last identity of (6). \(\square\)

An oriented open segment can represent a chain germ at its endpoints and have nonzero boundary there. Its closure being an allowed carrier does not by itself turn that chain into a cycle; the lift in (8) requires vanishing of the boundary.

## A dense regular piece is locally conormal

Let \(F\in D^b_{\mathbb R\text{-}c}(k_X)\) and \(\Lambda=SS(F)\). Its closed conic subanalytic carrier is isotropic and involutive. The geometric theorem on involutive subsets makes it the closure of its regular Lagrangian part. In particular its nonempty support is pure of dimension \(n\).

There is a dense relatively open regular subset \(\Lambda_0\subset\Lambda\) on which the carrier has local conormal charts. After the compatible refinements, write its pieces as \(\Lambda_\alpha\). Around any \(p\in\Lambda_\alpha\), there are an embedded analytic submanifold \(Z\subset X\) and an ambient cotangent neighborhood \(\Omega\) such that

\[
 \Lambda\cap\Omega=T_Z^*X\cap\Omega.
 \qquad\text{(9)}
\]

**Proof.** On the regular \(n\)-dimensional part, use a compatible analytic stratification of the projection and its image, and retain the open constant-rank pieces. The removed pieces have dimension \(<n\). The required local image/refinement statement is the existing subanalytic stratification input. For nonzero conic pieces it can be applied on an angular cotangent link; the radial coordinate is then restored. The zero-section part is handled in ordinary base charts.

Locally the image is an embedded \(Z\), and \(\pi|_{\Lambda_\alpha}\) is a submersion onto \(Z\). The canonical one-form vanishes on \(\Lambda_\alpha\). Thus for \((x;\xi)\in\Lambda_\alpha\) and every \(v\in T_xZ\), choose a tangent vector above \(v\); its canonical-form value is \(\xi(v)=0\). Hence \(\Lambda_\alpha\subset T_Z^*X\).

Both smooth manifolds have dimension \(n\). Their inclusion is locally an open embedding. As \(p\) lies in the relatively open regular part of the entire closed carrier, shrink \(\Omega\) to exclude other pieces and obtain (9). This is a local chart assertion. When larger projected pieces are used, refine their images to embedded submanifolds before naming \(Z\). Constant rank alone does not assert that an arbitrary global image is embedded. \(\square\)

The chain \([\Lambda_\alpha]\) on such a piece is the restriction of the normalized \([T_Z^*X]\). This is a chain normalization with the coefficient \(B\). Equality of its ambient dimension with \(n\) does not supply an untwisted orientation on a nonorientable base.

## Perfection makes the local coefficient finite

The supported local-form theorem applies to (9). It supplies a bounded complex \(V\) of \(k\)-vector spaces and an isomorphism

\[
 F\simeq V_Z\quad\text{in }D^b(k_X;p).
 \qquad\text{(10)}
\]

That theorem allows arbitrary bounded coefficients. We now prove that \(V\) has finite-dimensional cohomology in this constructible situation.

Microlocal Hom descends in both variables to the point-localized category. The actual submanifold comparison and the center-supported microlocalization formula give

\[
 \mu\operatorname{hom}(k_Z,F)_p
 \simeq\mu\operatorname{hom}(k_Z,V_Z)_p
 \simeq(\mu_ZV_Z)_p
 \simeq V.
 \qquad\text{(11)}
\]

The first input \(k_Z\) and \(F\) are finite constructible on the chart. Their microlocal Hom is bounded constructible with perfect stalks, so the left side of (11) is perfect over \(k\). The remaining two maps are valid for arbitrary bounded \(V\). The submanifold comparison cancels the projection and inverse projection orientation lines; the center-supported Fourier formula then gives the constant normal-covector coefficient \(V\). No further shift is present. Consequently \(V\) is perfect and its Euler characteristic is an integer.

After this step, \(V_Z\) is itself constructible. The constructible-roof theorem for localized isomorphisms represents (10) using constructible denominators whose cone microsupports avoid \(p\). Those microsupports are closed, so a smaller neighborhood avoids them all. Actual invariance and finite conormal normalization give

\[
 CC(F)|_\Omega=\chi(V)[T_Z^*X]|_\Omega.
 \qquad\text{(12)}
\]

Thus on a connected normalized regular piece its coefficient is one locally constant integer \(m_\alpha\). If \(\Omega_0\) is an open set whose intersection with the carrier is its chosen regular dense part, the generic chain formula is

\[
 CC(F)=\sum_\alpha m_\alpha[\Lambda_\alpha]
       \quad\text{in }\mathcal{CL}_X.
 \qquad\text{(13)}
\]

This notation is local and sheafified: locally finitely many compatible pieces suffice. At a singular frontier it means their top-chain extension, whose boundary cancels because the left side is already a cycle. Individual trimmed pieces in the sum can have a frontier boundary.

## Integer top chains extend uniquely to integer cycles

Let \(\mathcal C_n(B_{\mathbb Z})\) and \(\mathcal Z_n(B_{\mathbb Z})\) be the integral chain and cycle sheaves on \(T^*X\). The coefficient maps to the \(k\)-valued versions are injective:

\[
 \mathcal C_n(B_{\mathbb Z})\hookrightarrow\mathcal C_n(B),
 \qquad
 \mathcal Z_n(B_{\mathbb Z})\hookrightarrow\mathcal Z_n(B).
 \qquad\text{(14)}
\]

**Proof.** Check chain germs on a common finite oriented subdivision. An integral coefficient maps by \(\mathbb Z\to k\), which is injective in characteristic zero. Vanishing of every image coefficient therefore implies vanishing of every integral coefficient. The same argument applies in every degree and respects the orientation transition signs. Restricting to the kernel of the boundary proves the cycle assertion. \(\square\)

Formula (13) constructs a unique integral top chain \(c\) whose image is \(CC(F)\). To see its existence at every frontier, take a finite compatible triangulation of the carrier near that point and subdivide its top cells by the regular conormal pieces. Any remaining strata have dimension \(<n\). The constant integers \(m_\alpha\), in the normalized conormal orientation with \(B_{\mathbb Z}\), give integral coefficients on all top cells. They represent the same \(k\)-valued top chain as \(CC(F)\). Different subdivisions and orientation trivializations give the same integral germ by (14).

Cellular boundary incidence numbers are integers, and the integral orientation coefficient has transition signs \(\pm1\). The coefficient comparison commutes with boundary. Hence

\[
 \partial c\longmapsto\partial CC(F)=0
       \quad\Longrightarrow\quad\partial c=0.
 \qquad\text{(15)}
\]

The last implication uses the degree-\((n-1)\) chain injection proved as in (14). For \(n=0\), the boundary is zero directly. The integral chain is thus an integral cycle, with closed conic subanalytic isotropic support contained in the original allowed carrier. By (6), it belongs to the integral Lagrangian cycle sheaf.

We have proved the canonical lift

\[
 CC_{\mathbb Z}(F)\in\Gamma(T^*X;\mathcal L_{X,\mathbb Z}),
 \qquad CC_{\mathbb Z}(F)\longmapsto CC(F).
 \qquad\text{(16)}
\]

Existence follows from the generic Euler coefficients and boundary comparison; uniqueness follows from (14). Equivalently, a top chain is determined by its dense regular coefficients. A difference supported on dimension \(<n\) represents zero in the top-chain sheaf. This argument concerns chains and their incidence maps and makes no torsion-freeness assertion about homology groups.

## One coefficient functor represents the whole triangle

Fix a regular conormal point \(p\) as in (9). The exact coefficient functor

\[
 J_Z:\operatorname{Perf}(k)\longrightarrow D^b(k_X;p),
       \qquad V\longmapsto V_Z
 \qquad\text{(17)}
\]

is fully faithful. More precisely its actual coefficient-action map gives

\[
 \begin{aligned}
 R\operatorname{Hom}_k(V',V)
   &\xrightarrow{\sim}
       \mu\operatorname{hom}(V'_Z,V_Z)_p,\\
 \operatorname{Hom}_{D^b(k_X;p)}(V'_Z,V_Z[r])
   &\simeq H^rR\operatorname{Hom}_k(V',V).
 \end{aligned}
 \qquad\text{(18)}
\]

**Proof.** A coefficient morphism tensored with \(k_Z\) gives the ordinary sheaf morphism, and the actual microlocal unit gives its image in microlocal Hom. The finite tensor–Hom adjunction extends this construction to the derived coefficient complex; its arrow is the adjoint of the ordinary coefficient evaluation tensored with the unit of \(k_Z\).

For \(V'=V=k\), the submanifold and center-supported comparisons identify the right side with \(k\). They send that coefficient action to its unit: the actual closed-submanifold comparison transports the identity evaluation, and center-supported microlocalization sends the constant identity to the constant identity. Thus the map is the identity \(k\to k\), with its fixed orientation cancellations.

Microlocal Hom is contravariantly exact in the first variable, covariantly exact in the second, and compatible with shifts and finite direct sums. The coefficient map has the same properties. A bounded finite-dimensional coefficient complex is built from shifts of finite sums of \(k\) by a finite sequence of cones; retracts, if finite projective models are used, are also preserved. The comparison is therefore an isomorphism for all perfect \(V',V\). Finally the point-localized morphism theorem identifies every graded morphism group with the corresponding stalk cohomology, proving the second line of (18).

The comparison is induced by the exact functor \(J_Z\). It preserves actual degree-zero compositions and identities. In the written tensor order of two graded microlocal Hom inputs, the derived symmetry retains the factor \((-1)^{ab}\) for degrees \(a,b\), as in the microlocal composition convention. No unrelated choice of vector-space isomorphism enters full faithfulness. \(\square\)

Take a distinguished triangle of constructible sheaves:

\[
 F'\xrightarrow{u}F\longrightarrow F''\xrightarrow{+1}.
 \qquad\text{(19)}
\]

The triangle microsupport estimate puts all three microsupports in the common closed conic isotropic carrier \(\Lambda=SS(F')\cup SS(F'')\). The union is involutive as well: functions vanishing on the union have Poisson brackets vanishing on both members. The preceding regular-conormal construction therefore applies to the common carrier. On each such chart, choose perfect models \(V'_Z\simeq F'\) and \(V_Z\simeq F\) by (10)–(11). Objects invisible at \(p\) have coefficient zero.

Conjugate the actual arrow \(u\) by those two model isomorphisms. Full faithfulness in (18) represents the resulting arrow by one \(\ell:V'\to V\) in \(\operatorname{Perf}(k)\). Set \(V''=\operatorname{Cone}(\ell)\). Exactness of \(J_Z\) gives an isomorphism of distinguished triangles in the point-localized category:

\[
 \begin{matrix}
 V'_Z&\xrightarrow{\ell_Z}&V_Z&\longrightarrow&V''_Z&\xrightarrow{+1}\\
 \downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim&&
            \downarrow\scriptstyle\sim&\\
 F'&\xrightarrow{u}&F&\longrightarrow&F''&\xrightarrow{+1}.
 \end{matrix}
 \qquad\text{(20)}
\]

For the third isomorphism, the triangle axiom completes the commuting square in the first two columns to a morphism of triangles. Applying each representable Hom functor gives a morphism of long exact sequences; the first two isomorphisms force the third to be an isomorphism. This represents the entire given triangle, including its connecting morphism, up to isomorphism of triangles. Its cone is again perfect.

In a bounded finite cochain representative the cone has graded terms \(V^j\oplus V'^{j+1}\). The alternating dimension sum therefore gives

\[
 \chi(V'')=\chi(V)-\chi(V'),\qquad
             \chi(V)=\chi(V')+\chi(V'').
 \qquad\text{(21)}
\]

The same identity holds using cohomology, since the boundary subspaces cancel in consecutive degrees. Equations (12) and (20) identify these three Euler characteristics with the three generic characteristic-cycle coefficients. Their equality holds on every regular piece of the common carrier. Dense top-chain determination extends it through every singular frontier, giving

\[
 CC(F)=CC(F')+CC(F''),\qquad
 CC_{\mathbb Z}(F)=CC_{\mathbb Z}(F')+CC_{\mathbb Z}(F'').
 \qquad\text{(22)}
\]

The integral equality follows either from the same generic integer coefficients or from uniqueness in (16). For every integer \(s\), the convention \(H^j(V[s])=H^{j+s}(V)\) gives

\[
 CC(F[s])=(-1)^sCC(F),\qquad
 CC_{\mathbb Z}(F[s])=(-1)^sCC_{\mathbb Z}(F).
 \qquad\text{(23)}
\]

These formulas permit cancellation in a nonzero object. They do not assert that the support of a characteristic cycle recovers the microsupport.

## Examples and exercises with solutions

### Local monodromy and the global coefficient have different inputs

*Difficulty: Intermediate.*

Let \(Z=S^1\) be a closed analytic submanifold of an analytic manifold \(X\). Let \(L\) be a rank-\(d\) local system with monodromy \(T\in GL_d(k)\). Compute \(CC(i_*L)\), the complex of its proper image to a point, and the characteristic cycle of that image. Explain the case in which \(T-1\) is invertible.

**Solution.** On a contractible arc, (2) identifies \(L\) with \(k^d\) in degree zero. These actual local coefficient models give
\(CC(i_*L)=d[T_Z^*X]\) by (1); monodromy does not change the local rank. A one-vertex, one-edge cellular model of the circle with its monodromy gives
\(R\Gamma(S^1;L)=[k^d\xrightarrow{T-1}k^d]\) in degrees zero and one. Reversing the chosen edge can replace the differential by a conjugate or its negative without changing this derived object. Its cohomology is \(\ker(T-1)\) and \(\operatorname{coker}(T-1)\) in those degrees. Rank-nullity gives their equal dimensions, so its Euler characteristic is zero and its point characteristic cycle is zero. If \(T-1\) is invertible, the global complex is acyclic and the proper image object is zero. The input cycle still has coefficient \(d\), and for \(d>0\) is nonzero. Proper image to a point permits that cancellation; a global constant-complex model of \(L\) was never used.

### A finite microlocal Hom excludes infinite coefficients

*Difficulty: Intermediate.*

Suppose \(F\) is finite constructible, \(p\) is a regular conormal point, and a supported local form gives \(F\simeq V_Z\) at \(p\). Could \(H^0V\) have a countably infinite basis? Analyze also the model \(V=k^{(\mathbb N)}\) when finite constructibility of \(F\) is dropped.

**Solution.** Equation (11) identifies \(V\) with the stalk of \(\mu\operatorname{hom}(k_Z,F)\). Both inputs are finite constructible, so that stalk is a bounded finite-dimensional complex up to quasi-isomorphism. In particular \(H^0V\) is finite-dimensional; an infinite basis is impossible. This inference uses the finite microlocal-operation theorem in addition to the supported local form.

If \(F=V_Z\) for \(V=k^{(\mathbb N)}\) in degree zero, it is a bounded sheaf and the arbitrary-coefficient submanifold formula still gives \(\mu\operatorname{hom}(k_Z,F)_p=k^{(\mathbb N)}\). Thus the local-form and point-localized Hom statements remain consistent. The perfection inference fails because \(F\) lacks finite constructible stalks. There is no finite integer Euler sum for this model and no characteristic-cycle claim under the present constructible definition. The distinction is finite cohomology, not merely bounded cohomological degree.

### The cone of a rank-one arrow represents the third object

*Difficulty: Intermediate.*

At a fixed regular conormal point, take coefficient models \(V'=k^2\) and \(V=k^3\) in degree zero. Let the actual localized arrow correspond under (18) to a rank-one linear map \(\ell:k^2\to k^3\). Compute a model of the third object and all three characteristic-cycle coefficients. Do the coefficients determine the rank of \(\ell\)?

**Solution.** The cone is \([k^2\xrightarrow{\ell}k^3]\) in degrees minus one and zero. Its cohomology is a one-dimensional kernel in degree minus one and a two-dimensional cokernel in degree zero. Over a field it is isomorphic to \(k[1]\oplus k^2\), so the third sheaf model is \((k[1]\oplus k^2)_Z\). The three coefficients are respectively \(2,3,-1+2=1\). Equation (21) reads \(3=2+1\).

The cone is selected by the actual arrow, and (20) supplies the isomorphism of the whole localized triangles. For any rank \(r\in\{0,1,2\}\), the kernel and cokernel dimensions would be \(2-r\) and \(3-r\), so the cone Euler coefficient remains \(-(2-r)+(3-r)=1\). The three cycle coefficients therefore do not determine the map's rank. Their additivity records an Euler invariant of the whole triangle.

### A nonzero sheaf complex can have zero integral cycle

*Difficulty: Introductory.*

Let \(Z\) be a nonempty closed analytic submanifold and \(F=k_Z\oplus k_Z[1]\). Compute its characteristic cycle and microsupport. Verify the coefficient triangle that explains the cancellation.

**Solution.** The first summand has coefficient \(+1\) and the second \(-1\), by (3) and (23). Thus both \(CC(F)\) and \(CC_{\mathbb Z}(F)\) vanish. The object is nonzero, since on \(Z\) its cohomology is \(k\) in degrees zero and minus one. Its microsupport is the full conormal \(T_Z^*X\), because each nonzero constant submanifold summand has that microsupport and their direct-sum support tests preserve it. The split triangle \(k_Z\to F\to k_Z[1]\xrightarrow{0}k_Z[1]\) comes from inclusion and projection of the summands. Its coefficient triangle is \(k\to k\oplus k[1]\to k[1]\), giving \(0=1+(-1)\). The normalized generic coefficient vanishes even where the microlocal identity of \(F\) is nonzero.

### Boundary incidence detects the integral lift

*Difficulty: Advanced.*

In an oriented top-cell calculation with the sign line locally trivialized, suppose the boundary row is \((1,-1)\). Analyze the chain with generic coefficients \((2,2)\) over characteristic zero. Then work over \(\mathbb F_p\) and compare the integral coefficient vectors \((2,2)\), \((2+p,2+p)\) and \((p,0)\). Which part of the integral-lift proof uses characteristic zero?

**Solution.** The boundary of \((a,b)\) is \(a-b\). Thus \((2,2)\) is an integral cycle and maps to its characteristic-zero cycle with the same coefficients. Since the coefficient embedding is injective, those coefficients determine its unique integral top-chain lift.

Over \(\mathbb F_p\), the first two displayed vectors give the same field chain, while both are distinct integral cycles with boundary zero. Uniqueness from field coefficients therefore fails. Moreover \((p,0)\) maps to the zero field chain, which has zero boundary, whereas its integral boundary is \(p\ne0\). Thus field boundary vanishing alone no longer proves integral boundary vanishing. In (14)–(15), characteristic zero is used exactly through injectivity of \(\mathbb Z\to k\) in the top and boundary degrees. The incidence numbers and orientation transition signs are already integral. This example concerns what one can recover from a field chain; it does not assert that no separate integral invariant can be defined in positive characteristic.

### Two transverse submanifolds give a singular carrier with fixed weights

*Difficulty: Advanced.*

Take the coordinate axes \(Z_1=\{y=0\}\) and \(Z_2=\{x=0\}\) in \(X=\mathbb R^2\), and \(F=k_{Z_1}\oplus k_{Z_2}[1]\). Describe the common conormal carrier, the normalized generic integer coefficients and their extension at its singular intersection. Can one add an extra nonzero two-dimensional chain supported only on the intersection?

**Solution.** In coordinates \((x,y;\xi,\eta)\), the conormals are
\(T_{Z_1}^*X=\{y=0,\xi=0\}\) and
\(T_{Z_2}^*X=\{x=0,\eta=0\}\).
They are closed conic smooth two-dimensional carriers. Their intersection is the single point \((0,0;0,0)\): both base coordinates and both covector coordinates must vanish. Their union is the singular common carrier of \(F\).

The normalized generic coefficients are \(+1\) on the first conormal and \(-1\) on the second. With the same relative sign line \(B=\operatorname{or}_{T^*X/X}\), both normalized full conormals are cycles. The split triangle and (22) give
\(CC_{\mathbb Z}(F)=[T_{Z_1}^*X]-[T_{Z_2}^*X]\).
This is the extension of those generic weights through the intersection, and its boundary vanishes by linearity of the integral boundary. A further two-dimensional chain confined to the zero-dimensional intersection is zero in \(\mathcal C_2(B_{\mathbb Z})\), by its top-cell description. Hence it cannot supply an additional coefficient or a different lift. Removing the intersection to describe the regular pieces does not create a two-dimensional residue there. The signs \(+1,-1\) come from the coefficient shift, with the conormal generators held in their fixed normalization.

## Scope retained for the following calculations

We have proved general local-system conormal rank, Lagrangian-chain comparison, finite generic coefficient models, integer lifts, additivity and shift signs. Antipodal duality requires its actual swapped-kernel orientation comparison. Half-line and Lorentz-cone examples require their complete boundary and vertex coefficient models. Those arguments, the subsequent microlocal index and the remaining perverse and holomorphic solution material remain separate course work.
