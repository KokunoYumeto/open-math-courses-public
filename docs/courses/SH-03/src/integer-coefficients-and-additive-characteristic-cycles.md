# Integer coefficients and additive characteristic cycles

A characteristic cycle is defined by a microlocal identity and a trace. Its generic coefficient on a normalized conormal is \((-1)^{\dim Z}\) times the Euler characteristic of a finite coefficient complex, where \(Z\) is its local supporting base. We prove why that complex is finite, how its integer coefficient extends through singularities, and why one distinguished triangle gives an additive identity of cycles.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The [supported identity and trace construction](characteristic-cycles-from-supported-microlocal-identities.md#ordinary-restriction-and-the-unique-supported-trace) defines \(CC\), and its [constructible-roof proof of microlocal invariance](characteristic-cycles-from-supported-microlocal-identities.md#naturality-of-evaluation-proves-microlocal-invariance) permits the local replacements used below. The [finite constant-conormal formula](transporting-characteristic-cycles-through-a-graph.md#globally-constant-finite-coefficients-fix-conormal-normalization) fixes the sign: for a smooth \(d\)-dimensional base, its coefficient is \((-1)^d\chi(V)\). The brackets retain the graph and closed-trace normalization; the [relative fibre-trace calculation](transverse-pullback-of-normalized-conormal-cycles.md#the-graph-coefficient-and-the-relative-fibre-trace) fixes that normalization over the integers.

The coefficient argument uses the [supported local-form theorem LFI8–LFI10](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-supported--replacing-a-complex-by-one-on-a-submanifold), the [actual submanifold comparison](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-submanifold--recovering-microlocalization-from-hom), [center-supported microlocalization](../../sheaf-proof-readings/src/SH02/microlocalization.md#sh02-mic-examples--three-checks-with-arbitrary-coefficient-modules), and the graded point-localized morphism theorem MC.4. The [perfect microlocal-Hom calculation](../../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#specialization-and-microlocal-hom) supplies finite coefficients; its finiteness hypothesis is not part of the arbitrary-coefficient local-form theorem.

The geometric inputs are the [regular-locus and dimension rules](../../sheaf-proof-readings/src/SH03/finite-conormal-closures-and-generic-base-directions.md#the-precise-dimension-prerequisite), the [subanalytic rank-locus calculation](../../sheaf-proof-readings/src/SH03/finite-conormal-closures-and-generic-base-directions.md#subanalytic-rank-loci-with-bounded-auxiliary-vectors), and the [pure-Lagrangian consequence of involutivity](../../sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#subanalyticity-forced-by-an-isotropic-containing-set). The local tangent-lifting proof below gives conormal charts, with the nonzero-covector statement also proved as [Theorem 5.1 of Prescribed canonical coordinates and isotropic fibers](../../AN-04/reconstructions/20261005-restored-prescribed-coordinates/prescribed-canonical-coordinates-and-isotropic-fibers.md#5-recognize-conormal-germs-where-the-base-projection-has-constant-rank). It does not require a global embedded image of the projection. Compatible subanalytic triangulation is used through the [dense-piece chain comparison](subanalytic-chains-and-closed-cycle-supports.md#directed-comparison-of-locally-closed-representatives) and its [frontier boundary](subanalytic-chains-and-closed-cycle-supports.md#the-boundary-comes-from-the-frontier-triangle); the [cotangent orientation comparison](lagrangian-cycles-and-proper-cotangent-images.md#the-orientation-coefficient-fixes-the-dimension) fixes the coefficient line.

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, develops coefficient-valued subanalytic chains and the twisted orientation of conormals. Proposition 3.3 and §3.4, pp. 198–199, describe the finite localized coefficient model and generic Euler multiplicities. The conormal brackets in this lesson use the graph normalization fixed above, so the comparison with an Euler multiplicity includes \((-1)^{\dim Z}\). The proofs below construct that local coefficient with its actual maps, extend the integral chain through the frontier, and represent a whole distinguished triangle by one coefficient cone.
## Local ranks use an actual derived constant model

Let \(k\) be a field of characteristic zero. Manifolds are real analytic, Hausdorff and countable at infinity, with uniformly bounded finite dimension. Work on a component \(X\) of dimension \(n\). All constructible complexes are bounded with finite-dimensional cohomology stalks. A closed analytic embedding \(i:Z\hookrightarrow X\) is understood locally when \(Z\) is only locally closed. Write \(V_Z=i_*a_Z^{-1}V\) for a constant coefficient complex extended by zero.

Suppose \(A\in D^b(k_Z)\) has locally constant cohomology sheaves of finite ranks \(m_j\). On each connected component of \(Z\), the ranks are constant. Then

\[
 CC(i_*A)=(-1)^{\dim Z}\left(\sum_j(-1)^jm_j\right)[T_Z^*X].
 \qquad\text{(1)}
\]

**Proof.** Around a point of \(Z\), choose a contractible analytic coordinate ball \(U\) on which all the finitely many nonzero cohomology sheaves of \(A\) are constant. Let \(a_U:U\to\{\mathrm{pt}\}\) and put

\[
 V=R\Gamma(U;A),\qquad
 a_U^{-1}V\xrightarrow{\ \epsilon\ }A|_U.
 \qquad\text{(2)}
\]

The arrow is the counit of \(a_U^{-1}\dashv R\Gamma(U;-)\). Its cohomology maps are the evaluation maps. To compute their source, use the bounded hypercohomology spectral sequence \(H^q(U;H^jA)\Rightarrow H^{q+j}V\). Every \(H^jA\) is a finite constant sheaf on the contractible ball, so the rows with \(q>0\) vanish. Hence \(H^jV=\Gamma(U;H^jA)\), and the stalk at any \(z\in U\) of the counit is the isomorphism from those constant sections to \(H^j(A)_z\). This proves the derived isomorphism (2) itself, including its actual morphism. There are finitely many nonzero finite groups, so \(V\) is perfect over \(k\).

Shrink an ambient neighborhood \(W\) so that \(Z\cap W=U\) is closed in \(W\). Apply the constant-conormal formula to this actual model. The point coefficient has trace \(\chi(V)\); pulling it to the \(d=\dim U\) dimensional base contributes \((-1)^d\), and the closed embedding into \(W\) has the unsigned proper direct formula. Thus

\[
 CC(V_U)=(-1)^{\dim U}\chi(V)[T_U^*W],\qquad
 \chi(V)=\sum_j(-1)^j\dim_k H^jV.
 \qquad\text{(3)}
\]

Characteristic cycles and their defining kernel maps commute with restriction to \(W\). The local formulas (3) therefore agree on overlaps and glue to (1). The counit proof uses local contractible balls; it permits arbitrary monodromy of \(A\) on \(Z\). \(\square\)

For example, a rank-\(d\) local system on a circle has local zero-section coefficient \(-d\). Its global cohomology Euler characteristic is zero. Local conormal rank in (1) is calculated before any proper image to a point.

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

Here \(H^0_\Lambda\) is degree zero of sheaf \(R\mathcal Hom(k_\Lambda,-)\). For a closed carrier, support adjunction and (4) identify the supported complex with \(j_{\Lambda*}(\omega_\Lambda\otimes B|_\Lambda)[-n]\). Its lowest possible degree is zero, since \(\dim\Lambda\le n\). For a locally closed carrier, make it closed in an open neighborhood and then apply derived ordinary image to the same calculation. The lower bound makes degree zero of that image ordinary \(j_{\Lambda*}\) of the lowest sheaf, proving (5). Thus approach germs at the frontier remain. On a smooth \(n\)-dimensional piece the coefficient is \(\operatorname{or}_\Lambda\otimes B\); a piece of dimension strictly less than \(n\) contributes zero.

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

**Proof.** Let \(R\) be the relatively open regular Lagrangian part of \(\Lambda\). On \(R\), the finitely many exact-rank loci of \(d\pi\) are subanalytic: the bounded tangent-witness calculation in the geometric prerequisite proves this for an analytic map restricted to a subanalytic analytic submanifold. Let \(\Lambda_0\) be the union of their relative interiors. It is open and dense in \(R\). Indeed, in any nonempty open patch choose the largest rank attained there; a minor nonzero at a point of that rank stays nonzero on a smaller patch, and maximality makes the rank constant on that smaller patch. The complement is subanalytic with empty interior in the \(n\)-manifold \(R\), so it has dimension \(<n\). Together with \(\Lambda\setminus R\), it remains lower-dimensional. Rank and the relative-interior construction are invariant under positive fibre dilation, so these choices preserve conicity.

Near \(p\in\Lambda_0\), write the constant rank as \(d\). The local constant-rank theorem gives an embedded image germ \(Z\) of dimension \(d\), and makes the restricted projection a submersion onto it. This is a local statement about a sufficiently small source patch. For \((x;\xi)\) in that patch and \(v\in T_xZ\), lift \(v\) to a tangent vector \(w\) of the patch. Isotropy gives \(0=\alpha_X(w)=\xi(v)\), hence the patch lies in \(T_Z^*X\).

The patch and the conormal are both smooth of dimension \(n\). The inclusion therefore has invertible differential and is an open embedding locally. Since \(R\) is relatively open in the full carrier, a smaller ambient cotangent neighborhood meets no other local carrier piece; shrinking once more gives (9). This argument also covers a zero covector: it uses one-form vanishing on the whole smooth patch, without division by \(\xi\). A local base chart makes \(Z\) closed in a smaller neighborhood. The global image of a projection may self-intersect or have a caustic, and is not being declared embedded. \(\square\)

The chain \([\Lambda_\alpha]\) on such a piece is the restriction of the normalized \([T_Z^*X]\). This is a chain normalization with the coefficient \(B\). Its integrality can be checked in adapted tangent and normal frames: the tangent zero-section class is \((-1)^{\dim Z}\) times the positive integral fibre-point unit, and the normal factor is the integral closed-submanifold trace. Their product is therefore a primitive integral generator, with coefficient \(+1\) or \(-1\) in any integral orientation frame. Reversing a base frame reverses the corresponding dual fibre frame too; their paired signs cancel. These local generators thus glue with the fixed relative sign line, including on a nonorientable base. This proves primitivity, rather than assuming that an arbitrary rank-one \(k\)-coefficient is integral. The constant sheaf coefficient is \((-1)^{\dim Z}\) in this fixed normalized generator.

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

The first input \(k_Z\) and \(F\) are finite constructible on the chart. The perfect-operation theorem applies to the actual diagonal kernel \(R\mathcal Hom(q_2^{-1}k_Z,q_1^!F)\), then to its specialization and Fourier transform; it therefore makes the left side of (11) a perfect stalk. The last two arrows do not require this finiteness. The submanifold comparison cancels its projection orientation with the inverse projection orientation, giving \(\mu_ZV_Z\) with no remaining shift. Specialization of \(V_Z\) is supported on the zero normal vector with coefficient \(V\); in the Fourier kernel that vector pairs to zero with every covector, and projection is the identity on its support. The output stalk is exactly \(V\). Thus (11) proves perfection of the initially arbitrary model, and its Euler characteristic is a finite integer sum.

After this step, \(V_Z\) is itself constructible. For a nonzero \(p\), the constructible-roof theorem realizes (10) by two ordinary arrows through a constructible cutoff object, both with cone microsupport avoiding \(p\). Closedness lets us choose one neighborhood avoiding both cones; the actual identity-and-trace invariance applies to each arrow there. At a zero covector, the localized isomorphism is an ordinary derived isomorphism on a smaller base neighborhood, where the same trace naturality applies. Using the constant-conormal formula (3) in either case gives

\[
 CC(F)|_\Omega=(-1)^{\dim Z}\chi(V)[T_Z^*X]|_\Omega.
 \qquad\text{(12)}
\]

Thus on a connected normalized regular piece its coefficient is the locally constant integer \(m_\alpha=(-1)^{\dim Z}\chi(V)\). The base dimension is the locally constant rank of the conormal projection on this piece. The parity factor is a unit in \(\mathbb Z\), so the integrality and frontier arguments below are unchanged. If \(\Omega_0\) is an open set whose intersection with the carrier is its chosen regular dense part, the generic chain formula is

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

The comparison is induced by the exact functor \(J_Z\). The [kernel unit and composition calculation](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-composition--directional-composition-identities-and-associativity) shows that it preserves actual degree-zero compositions and identities: composing with the diagonal identity cancels the adjacent evaluation and trace counit. In the written tensor order of two graded microlocal Hom inputs, the derived symmetry retains the factor \((-1)^{ab}\) for degrees \(a,b\). For (20) we use the degree-zero functorial map, so no further sign changes the actual arrow \(u\). Thus full faithfulness identifies morphisms compatibly with the exact functor, rather than choosing abstract vector-space isomorphisms. \(\square\)

Take a distinguished triangle of constructible sheaves:

\[
 F'\xrightarrow{u}F\longrightarrow F''\xrightarrow{+1}.
 \qquad\text{(19)}
\]

The triangle microsupport estimate puts all three microsupports in the common closed conic isotropic carrier \(\Lambda=SS(F')\cup SS(F'')\). This is also \(SS(F'\oplus F'')\): the finite direct-sum support tests vanish exactly when both summand tests vanish. Thus it is involutive by the microsupport theorem itself. The preceding regular-conormal construction therefore applies to the common carrier. On each such chart, choose perfect models \(V'_Z\simeq F'\) and \(V_Z\simeq F\) by (10)–(11). Objects invisible at \(p\) have coefficient zero.

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

The same identity holds using cohomology, since the boundary subspaces cancel in consecutive degrees. Equations (12) and (20) multiply these three Euler characteristics by the same factor \((-1)^{\dim Z}\) to obtain the three generic characteristic-cycle coefficients. Their additive identity therefore survives unchanged. Their equality holds on every regular piece of the common carrier. Dense top-chain determination extends it through every singular frontier, giving

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
\(CC(i_*L)=-d[T_Z^*X]\) by (1); monodromy does not change the local rank. A one-vertex, one-edge cellular model of the circle with its monodromy gives
\(R\Gamma(S^1;L)=[k^d\xrightarrow{T-1}k^d]\) in degrees zero and one. Changing the orientation, lifts, or trivializations gives a chain-isomorphic cellular complex. For example, reversing the monodromy generator replaces \(T-1\) by \(T^{-1}-1=-T^{-1}(T-1)\), an invertible change on the target term. Its cohomology is \(\ker(T-1)\) and \(\operatorname{coker}(T-1)\) in those degrees. Rank-nullity gives their equal dimensions, so its Euler characteristic is zero and its point characteristic cycle is zero. If \(T-1\) is invertible, the global complex is acyclic and the proper image object is zero. The input cycle still has coefficient \(-d\), and for \(d>0\) is nonzero. Proper image to a point permits that cancellation; a global constant-complex model of \(L\) was never used.

### A finite microlocal Hom excludes infinite coefficients

*Difficulty: Intermediate.*

Suppose \(F\) is finite constructible, \(p\) is a regular conormal point, and a supported local form gives \(F\simeq V_Z\) at \(p\). Could \(H^0V\) have a countably infinite basis? Analyze also the model \(V=k^{(\mathbb N)}\) when finite constructibility of \(F\) is dropped.

**Solution.** Equation (11) identifies \(V\) with the stalk of \(\mu\operatorname{hom}(k_Z,F)\). Both inputs are finite constructible, so that stalk is a bounded finite-dimensional complex up to quasi-isomorphism. In particular \(H^0V\) is finite-dimensional; an infinite basis is impossible. This inference uses the finite microlocal-operation theorem in addition to the supported local form.

If \(F=V_Z\) for \(V=k^{(\mathbb N)}\) in degree zero, it is a bounded sheaf and the arbitrary-coefficient submanifold formula still gives \(\mu\operatorname{hom}(k_Z,F)_p=k^{(\mathbb N)}\). Thus the local-form and point-localized Hom statements remain consistent. The perfection inference fails because \(F\) lacks finite constructible stalks. There is no finite integer Euler sum for this model and no characteristic-cycle claim under the present constructible definition. The distinction is finite cohomology, not merely bounded cohomological degree.

### The cone of a rank-one arrow represents the third object

*Difficulty: Intermediate.*

At a fixed regular conormal point, take coefficient models \(V'=k^2\) and \(V=k^3\) in degree zero. Let the actual localized arrow correspond under (18) to a rank-one linear map \(\ell:k^2\to k^3\). Compute a model of the third object and all three characteristic-cycle coefficients. Do the coefficients determine the rank of \(\ell\)?

**Solution.** The cone is \([k^2\xrightarrow{\ell}k^3]\) in degrees minus one and zero. Its cohomology is a one-dimensional kernel in degree minus one and a two-dimensional cokernel in degree zero. Over a field it is isomorphic to \(k[1]\oplus k^2\), so the third sheaf model is \((k[1]\oplus k^2)_Z\). Put \(\epsilon_Z=(-1)^{\dim Z}\). The three characteristic-cycle coefficients are respectively \(2\epsilon_Z,3\epsilon_Z,\epsilon_Z(-1+2)=\epsilon_Z\). The raw Euler identity (21) is \(3=2+1\); multiplying it by the common \(\epsilon_Z\) gives the cycle identity.

The cone is selected by the actual arrow, and (20) supplies the isomorphism of the whole localized triangles. For any rank \(r\in\{0,1,2\}\), the kernel and cokernel dimensions would be \(2-r\) and \(3-r\), so the cone Euler characteristic remains \(-(2-r)+(3-r)=1\), and its cycle coefficient remains \(\epsilon_Z\). The three cycle coefficients therefore do not determine the map's rank. Their additivity records an Euler invariant of the whole triangle.

### A nonzero sheaf complex can have zero integral cycle

*Difficulty: Introductory.*

Let \(Z\) be a nonempty closed analytic submanifold and \(F=k_Z\oplus k_Z[1]\). Compute its characteristic cycle and microsupport. Verify the coefficient triangle that explains the cancellation.

**Solution.** The first summand has coefficient \(\epsilon_Z=(-1)^{\dim Z}\) and the second \(-\epsilon_Z\), by (3) and (23). Thus both \(CC(F)\) and \(CC_{\mathbb Z}(F)\) vanish. The object is nonzero, since on \(Z\) its cohomology is \(k\) in degrees zero and minus one. Its microsupport is the full conormal \(T_Z^*X\), because each nonzero constant submanifold summand has that microsupport and their direct-sum support tests preserve it. The split triangle \(k_Z\to F\to k_Z[1]\xrightarrow{0}k_Z[1]\) comes from inclusion and projection of the summands. Its coefficient triangle is \(k\to k\oplus k[1]\to k[1]\), giving \(0=1+(-1)\). The normalized generic coefficient vanishes even where the microlocal identity of \(F\) is nonzero.

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

The normalized generic coefficients are \(-1\) on the first conormal and \(+1\) on the second, since both axes have dimension one and the second coefficient is shifted. With the same relative sign line \(B=\operatorname{or}_{T^*X/X}\), both normalized full conormals are cycles. The split triangle and (22) give
\(CC_{\mathbb Z}(F)=-[T_{Z_1}^*X]+[T_{Z_2}^*X]\).
This is the extension of those generic weights through the intersection, and its boundary vanishes by linearity of the integral boundary. A further two-dimensional chain confined to the zero-dimensional intersection is zero in \(\mathcal C_2(B_{\mathbb Z})\), by its top-cell description. Hence it cannot supply an additional coefficient or a different lift. Removing the intersection to describe the regular pieces does not create a two-dimensional residue there. The signs \(-1,+1\) combine the one-dimensional base parity with the coefficient shift, with both conormal generators held in their fixed normalization.

## From local coefficients to duality

The integer lift retains local Euler coefficients through singular frontiers, and additivity allows them to cancel in a nonzero complex. Verdier duality adds a geometric operation: it reverses the cotangent covector together with its orientation coefficient. The next lesson proves that compatibility at the kernel unit and trace, then uses it to distinguish open and closed half-lines.
