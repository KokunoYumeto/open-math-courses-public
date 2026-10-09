# Complex middle perversity and exterior products

On a complex stratum, the middle perversity puts a locally constant coefficient in ordinary degree minus its complex dimension. Its point costalk lies in the opposite positive degree: the point orientation shift uses twice that dimension. These measurements determine the cuts. We construct their truncations inside the complex constructible category, then prove functor, tensor and Hom bounds with their coefficient hypotheses.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

Use [Perverse support, costalks and truncation triangles](perverse-support-costalks-and-truncation-triangles.md) for the complete real criteria, fixed-stratum exceptional local constancy and actual closed/open construction. Perverse descent and fibre dimension bounds proves descent, real functor bounds and field duality. [Complex microlocal stratifications and constructibility](complex-microlocal-stratifications-and-constructibility.md) supplies compatible complex μ-strata and their closed total conormal. [Holomorphic operations and complex Fourier symmetries](holomorphic-operations-and-complex-fourier-symmetries.md) supplies globally bounded complex membership for the operations used below.

Let \(k\) be commutative of finite global dimension. Manifolds and maps are complex analytic, Hausdorff and countable at infinity, with uniform finite dimension bounds. Every \(D^b\) object has one global cohomology interval. Weak complex constructibility permits arbitrary modules; strong constructibility requires perfect stalks. The strong perverse t-structure retains Noetherianity. Field hypotheses below are separate.

Write \(\dim_{\mathbb C}\) for complex dimension; on analytic sets real dimension is twice it. Supports mean nonzero-stalk loci, with dimension unchanged by closure. Empty loci have dimension \(-\infty\). Locally closed analytic pieces and complex μ-strata have the precise closure, frontier and local finiteness conditions of the stratification lesson.

## The even values determine the complex cuts

Choose a real perversity \(p\) with

\[
 p(2a)=-a\qquad(a\in\mathbb Z).
 \tag{1}
\]

Both \(-\lfloor r/2\rfloor\) and \(-\lceil r/2\rceil\) satisfy this. Define the middle cuts by intersecting the real \(p\)-cuts with \(D^b_{\mathrm w\mathbb C\mathrm c}(X;k)\), and define their degree translates by the usual shifts. We write \({}^{\mathrm{mid}}D^{\le r}\) and \({}^{\mathrm{mid}}D^{\ge r}\).

For an adapted complex μ-stratification \(X=\bigsqcup_\alpha S_\alpha\), put \(a_\alpha=\dim_{\mathbb C}S_\alpha\). The full real stratum criterion gives

\[
\begin{aligned}
 F\in{}^{\mathrm{mid}}D^{\le0}
 &\Longleftrightarrow i_\alpha^{-1}F\in D^{\le-a_\alpha},\\
 F\in{}^{\mathrm{mid}}D^{\ge0}
 &\Longleftrightarrow i_\alpha^!F\in D^{\ge-a_\alpha},
\end{aligned}
\quad\text{for every }\alpha .
\tag{2}
\]

The chosen exceptional restrictions have locally constant cohomology by the earlier full limiting-conormal proof. All strata have real dimension \(2a_\alpha\), so (2) uses only (1). It proves independence from every odd value of \(p\). No complex dimension is being assigned to arbitrary real subsets.

Complex coordinate changes give a canonical real orientation, since their real determinant is \(|\det_{\mathbb C}|^2>0\). Thus \(\omega_S=k_S[2a]\) on a complex \(a\)-manifold. Point exceptional composition gives

\[
 i_x^!F\simeq(i_\alpha^!F)_x[-2a_\alpha]\qquad(x\in S_\alpha).
 \tag{3}
\]

The orientation line is canonical, but the degree shift is still present.

## Support, cosupport and analytic-subset tests

The intrinsic criteria are

\[
\begin{aligned}
 F\in{}^{\mathrm{mid}}D^{\le0}
 &\Longleftrightarrow
 \dim_{\mathbb C}\operatorname{supp}H^jF\le-j,\\
 F\in{}^{\mathrm{mid}}D^{\ge0}
 &\Longleftrightarrow
 \dim_{\mathbb C}\operatorname{cosupp}^jF\le j,
\end{aligned}
\quad\text{for every }j ,
\tag{4}
\]

where \(\operatorname{cosupp}^jF=\{x:H^j(i_x^!F)\ne0\}\).

For the first line, a nonzero ordinary restriction in degree \(j\) on an \(a\)-stratum contributes dimension \(a\). The support inequalities therefore say \(j\le-a\) whenever that restriction is nonzero, exactly the upper condition (2). Locally finite unions preserve the supremum of these dimensions, including infinitely many components.

For the second, (3) identifies point costalk degree \(j\) with exceptional stratum degree \(j-2a\). The lower stratum condition says \(j-2a\ge-a\), equivalently \(a\le j\). This proves both directions of the cosupport criterion. Negative point-costalk degrees consequently vanish in the lower cut; this is not an ordinary-stalk assertion.

Another equivalent formulation is

\[
 F\in{}^{\mathrm{mid}}D^{\ge0}
 \Longleftrightarrow
 i_T^!F\in D^{\ge-\dim_{\mathbb C}T}(T)
 \quad\text{for every locally closed complex analytic }T\subset X.
 \tag{5}
\]

Allow singular and nonpure \(T\), using maximal dimension. For the forward implication intersect adapted complex strata with \(T\), refine analytically, and use the actual finite closed support filtration. On an \(a\)-stratum the exceptional coefficient starts in degree \(-a\). For an intersection piece of complex dimension \(t\le a\), the full arbitrary-coefficient singular-subset estimate gives
\[
 -a+2a-2t=a-2t\ge-t\ge-\dim_{\mathbb C}T.
\]
That estimate uses the actual flat cellular dualizing model. The finite closed-layer reconstruction and ordinary left t-exactness of closed direct image give the bound on all of \(T\). Conversely, take \(T\) to be each analytic stratum in (5); the result is (2). This does not presuppose a perverse t-structure on singular \(T\).

## Truncation triangles remain complex constructible

Massey's *Notes on Perverse Sheaves and Vanishing Cycles*, §2, pp. 19–20, and §5, pp. 44–45, provides the complex support and cosupport normalization for comparison. Beilinson–Bernstein–Deligne's *Faisceaux pervers*, Theorem 1.4.10, provides the formal open/closed gluing mechanism. To apply it here, the closed-layer correction must remain complex constructible; the real t-structure by itself does not establish that fact. The construction below checks this membership before invoking the gluing triangle, retaining the actual exceptional restriction and its adjunction arrow.

**Theorem.** The middle cuts form a bounded t-structure on \(D^b_{\mathrm w\mathbb C\mathrm c}(X;k)\). Over a Noetherian \(k\), they form a bounded t-structure on \(D^b_{\mathbb C\mathrm c}(X;k)\).

**Proof.** Shift stability and orthogonality follow from the real theorem because the complex category is full. We must construct triangles in that smaller category.

Choose adapted complex μ-strata and their closed dimension filtration
\(\varnothing=Z_{-1}\subset Z_0\subset\cdots\subset Z_n=X\).
The layer \(M_a=Z_a\setminus Z_{a-1}\) is a smooth complex \(a\)-manifold, possibly disconnected. The frontier rule makes each union of strata of dimension at most \(a\) closed. Their analytic closures are locally finite, so those unions are closed analytic. The dimension-filtration theorem retains the full approaching-layer μ-condition. The corresponding real filtration has empty odd layers.

Suppose an adapted triangle \(A_U\to F|_U\to B_U\to\) is constructed on \(U=X\setminus Z_a\). Put \(E=X\setminus Z_{a-1}\), with closed \(i:M_a\hookrightarrow E\) and complementary open \(j:U\hookrightarrow E\). Form

\[
 j_!A_U\longrightarrow F|_E\longrightarrow G\longrightarrow,
 \qquad C=\tau^{\le-a}i^!G .
 \tag{6}
\]

Its first arrow is the actual open counit. The ordinary cut arrow and closed exceptional counit give \(i_*C\to i_*i^!G\to G\). Let \(B\) be its cone and \(A\) the fibre of \(F|_E\to G\to B\). The octahedron gives \(j_!A_U\to A\to i_*C\to\), and

\[
\begin{aligned}
 j^{-1}A&\simeq A_U,&j^{-1}B&\simeq B_U,\\
 i^{-1}A&\simeq C,&i^!B&\simeq\tau^{\ge-a+1}i^!G .
\end{aligned}
\tag{7}
\]

The first row uses \(j^{-1}i_*=0\). The ordinary closed identity follows from the octahedron and \(i^{-1}j_!=0\). The exceptional identity applies \(i^!\) to the cone of the actual smart-cut arrow. Thus (2) gives upper zero for \(A\) and lower one for \(B\).

Check complex membership at each stage. The adapted boundary extension argument puts \(j_!A_U\) in the same total conormal bound, and the first cone does so for \(G\). This total bound is closed complex analytic and complex-conic. Exceptional stratum local constancy gives that property for \(i^!G\) on \(M_a\), and its smart cut remains locally constant. Closed extension and the two remaining cones retain the bound. The four-test complex theorem therefore makes all constructed objects weakly complex constructible. This verifies membership; it does not assume that arbitrary real perverse truncations preserve the subcategory.

There are \(n+1\) stages. Uniform exceptional amplitudes and finitely many cuts and cones retain one global cohomology interval. For strong inputs, exceptional restriction preserves perfectness. Noetherianity gives finitely generated bounded cohomology of the ordinary cuts; finite global dimension makes those cuts perfect. Extension and cones preserve perfect stalks.

Finally the ordinary-to-perverse bounds of the real theorem prove boundedness, since \(-a\) has a finite range for \(0\le a\le n\). All axioms are proved. \(\square\)

Abstract uniqueness supplies natural middle truncations and cohomology with their actual arrows. The abelian heart is a stack by the earlier descent proof, now using local complex membership. Its objects are called **perverse sheaves**; they need not be ordinary sheaves.

For a closed complex \(a\)-submanifold \(i:Y\hookrightarrow X\),

\[
 i_*k_Y[a]\in{}^{\mathrm{mid}}D^0_{\mathbb C\mathrm c}(X).
 \tag{8}
\]

Its support has complex dimension \(a\) in ordinary degree \(-a\). At a point of \(Y\) its costalk is \(k[-a]\), in degree \(a\); off \(Y\) it is zero. Both tests (4) apply. Arbitrary coefficient modules in the same shift give weak heart objects, with perfectness decided separately.

## Four bounds for holomorphic maps

Suppose \(f:Y\to X\) is holomorphic with \(\dim_{\mathbb C}f^{-1}(x)\le d\), \(d\ge0\). Then

\[
\begin{aligned}
 f^{-1}:{}^{\mathrm{mid}}D^{\le0}(X)
 &\longrightarrow{}^{\mathrm{mid}}D^{\le d}(Y),\\
 f^!:{}^{\mathrm{mid}}D^{\ge0}(X)
 &\longrightarrow{}^{\mathrm{mid}}D^{\ge-d}(Y).
\end{aligned}
\tag{9}
\]

For globally bounded weakly complex constructible \(G\) on \(Y\),

\[
\begin{aligned}
 G\in{}^{\mathrm{mid}}D^{\le0},\
 Rf_!G\in D^b_{\mathrm w\mathbb C\mathrm c}(X)
 &\Longrightarrow Rf_!G\in{}^{\mathrm{mid}}D^{\le d}(X),\\
 G\in{}^{\mathrm{mid}}D^{\ge0},\
 Rf_*G\in D^b_{\mathrm w\mathbb C\mathrm c}(X)
 &\Longrightarrow Rf_*G\in{}^{\mathrm{mid}}D^{\ge-d}(X).
\end{aligned}
\tag{10}
\]

The real fibre bound is \(2d\), and
\(p[-2d](2a)=d-a\), \(p[2d](2a)=-d-a\).
On even dimensions these are constant perversity changes \(+d,-d\). The real inverse upper target becomes upper \(d\). The exceptional lower target has the additional degree \(-2d\), hence becomes lower \(d-2d=-d\). The compact direct upper target has degree \(2d\) and constant \(-d\), hence upper \(d\). The ordinary direct lower target has constant \(-d\), hence lower \(-d\). These are (9)–(10).

The holomorphic operation theorem supplies complex membership for the inverse operations. Direct membership in (10) remains a separate hypothesis; properness on the actual closed support supplies it. A zero-dimensional analytic map with accumulating images still disproves automatic nonproper constructibility, as in the preceding lesson.

## Field duality exchanges the middle cuts

On even dimensions \(p^*(2a)=-p(2a)-2a=-a\). Strong field duality therefore gives

\[
 D_X:{}^{\mathrm{mid}}D^{\le0}_{\mathbb C\mathrm c}(X)
       \longleftrightarrow{}^{\mathrm{mid}}D^{\ge0}_{\mathbb C\mathrm c}(X).
 \tag{11}
\]

Use the actual local pairings
\((D_XF)_x=R\operatorname{Hom}_k(i_x^!F,k)\) and
\(i_x^!D_XF=R\operatorname{Hom}_k(F_x,k)\), exact field degree reversal, and perfect bidual evaluation. The complex Hom theorem retains bounded complex membership. On the strong heart this is an exact contravariant equivalence, reversing short exact sequences. Complex orientation does not make integral coefficient dualization exact.

## Exterior tensor and its evaluated dual pairing

The product calculation has two different inputs. Massey's notes, §1, p. 14, records the proper-support Künneth comparison and the adjoint product-Hom identity in its finite constructible setting. The upper tensor bound below comes instead from the direction of derived tensor degrees and permits weak coefficients. To obtain the lower bound we use the explicitly constructed evaluation pairing, finite local cochains and field duality. The order of the factors and the complex orientation identify the actual morphism; an abstract object isomorphism would not check that pairing. The integral Tor example shows why this second argument cannot simply inherit the first argument's coefficient range.

Put \(F\boxtimes^LG=q_1^{-1}F\otimes_k^Lq_2^{-1}G\). The weak operation theorem gives its globally bounded complex membership. For the full coefficient ring,

\[
 F\in{}^{\mathrm{mid}}D^{\le0}(X),\
 G\in{}^{\mathrm{mid}}D^{\le0}(Y)
 \Longrightarrow F\boxtimes^LG\in{}^{\mathrm{mid}}D^{\le0}(X\times Y).
 \tag{12}
\]

On a product of strata of complex dimensions \(a,b\), ordinary restriction is the tensor of the restrictions, upper bounded by \(-a,-b\). Locally take bounded-above flat coefficient resolutions with those upper term bounds. Their total tensor has no terms above \(-a-b\), the required upper stratum bound. Negative Tor can lower the degree but cannot raise it.

For strong inputs there is an actual comparison

\[
 D_XF\boxtimes^LD_YG
 \xrightarrow{\sim}D_{X\times Y}(F\boxtimes^LG).
 \tag{13}
\]

Define it by the tensor of the evaluation pairings, Koszul interchange and the ordered orientation identification
\(\omega_X\boxtimes^L\omega_Y=\omega_{X\times Y}\), then curry. Here is a local verification of that arrow.

The [actual small-ball compact-section comparisons](constructible-costalks-and-verdier-duality.md#the-two-local-measurements) represent \(i_x^!F\) and \(i_y^!G\). Compact-support cross product gives
\[
 i_x^!F\otimes_k^Li_y^!G\longrightarrow i_{(x,y)}^!(F\boxtimes^LG).
\]
It is an isomorphism: choose compatible real triangulations, finite on compact ball closures, including the boundaries and coefficient strata. Delete the boundaries to obtain the open balls. The finite closed simplex filtrations build coefficients by localization triangles from open simplex coefficients, which are [locally derived constant on each contractible simplex](constructible-sheaves-on-a-triangulation.md#approximating-an-arbitrary-sheaf-by-face-data). For real open simplices of dimensions \(r,s\), compact sections are \(P\otimes\mathrm{or}_r[-r]\) and \(Q\otimes\mathrm{or}_s[-s]\). On their product they are
\((P\otimes^LQ)\otimes(\mathrm{or}_r\otimes\mathrm{or}_s)[-r-s]\).
The cross product is this identification with the ordered product orientation and cohomological tensor sign. It is an isomorphism on the coefficient cells. Naturality for localization triangles and induction through both finite filtrations prove it on the original coefficients. The small-ball transition maps identify this arrow with the displayed point costalk map. Finite triangulation and local derived-constant prerequisites remain explicit; no unrestricted inverse-limit claim is used.

[The costalks are perfect](constructible-costalks-and-verdier-duality.md#perfect-stalks-give-perfect-costalks). For perfect coefficients the evaluation map
\(P^\vee\otimes^LQ^\vee\to(P\otimes^LQ)^\vee\)
is an isomorphism: check finite projectives, then bounded total complexes with their Koszul signs. The local dual pairings identify the stalk of (13) with this map and the dual of the verified costalk cross product. Thus (13) is an isomorphism on every stalk, with its actual evaluation normalization.

Over a field, strong lower-cut objects have upper-cut duals by (11). Apply (12), (13), and evaluated biduality:

\[
 F\in{}^{\mathrm{mid}}D^{\ge0}_{\mathbb C\mathrm c}(X),\
 G\in{}^{\mathrm{mid}}D^{\ge0}_{\mathbb C\mathrm c}(Y)
 \Longrightarrow F\boxtimes^LG
       \in{}^{\mathrm{mid}}D^{\ge0}_{\mathbb C\mathrm c}(X\times Y).
 \tag{14}
\]

Tensor of perfect stalks remains perfect. Thus the exterior product of strong perverse sheaves over a field is perverse. The field condition enters the cut exchange, separately from the product pairing.

## Exceptional exterior Hom has the lower bound

For weak complex constructible inputs,

\[
 F\in{}^{\mathrm{mid}}D^{\le0}(X),\
 G\in{}^{\mathrm{mid}}D^{\ge0}(Y)
 \Longrightarrow R\mathcal Hom(q_1^{-1}F,q_2^!G)
       \in{}^{\mathrm{mid}}D^{\ge0}(X\times Y).
 \tag{15}
\]

Use the bounded-first-argument exceptional Hom isomorphism in the [exceptional-Hom proof in *Exceptional operations*, SH02-EX-HOM](../SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom), and the actual submersion comparison in *Manifold duality*, SH02-MD-SUBMERSION. Their exact coefficient, amplitude and evaluation contracts remain prerequisites.

On \(i:S_\alpha\times T_\beta\hookrightarrow X\times Y\), write \(r_1,r_2\) for its projections, with complex dimensions \(a,b\). Exceptional Hom and exceptional composition give

\[
\begin{aligned}
 i^!R\mathcal Hom(q_1^{-1}F,q_2^!G)
 &\simeq R\mathcal Hom
       (r_1^{-1}i_\alpha^{-1}F,r_2^!i_\beta^!G),\\
 r_2^!i_\beta^!G
 &\simeq\omega_{S_\alpha}\boxtimes^Li_\beta^!G
       =k_{S_\alpha}[2a]\boxtimes^Li_\beta^!G .
\end{aligned}
\tag{16}
\]

The second line is the trace-normalized comparison for the real oriented \(2a\)-dimensional projection, valid for arbitrary bounded-below coefficients. Its lower ordinary bound is \(-2a-b\); the first Hom argument has upper bound \(-a\). Internal Hom from \(D^{\le u}\) into \(D^{\ge v}\) lies in \(D^{\ge v-u}\): use a representative zero above \(u\), an injective resolution zero below \(v\), and inspect Hom total degrees. Here the result is \(-a-b\), the lower stratum test (2). The complex operation theorem supplies global bounded membership. This proves (15) without field or perfectness assumptions, or a tensor-with-infinite-dual substitution.

## Exercises with complete solutions

### Odd values disappear only on complex strata

*Difficulty: Introductory.*

Compare \(p_-(r)=-\lfloor r/2\rfloor\), \(p_+(r)=-\lceil r/2\rceil\). Prove equality of their complex cuts and inequality of their real line hearts.

**Solution.** Their consecutive steps are zero or minus one, so both are real perversities. Both have value \(-a\) at \(2a\), hence (2) identifies all complex cuts. On the real line their values at its stratum dimension one are zero and minus one. The real smooth-stratum criterion puts a nonzero locally constant coefficient in their hearts only in ordinary degrees zero and minus one respectively. Thus \(k_{\mathbb R}\) belongs to the first heart and not the second; \(k_{\mathbb R}[1]\) belongs to the second. Even-dimensional stratification was essential.

### A closed curve and its two restrictions

*Difficulty: Intermediate.*

For a closed coordinate line \(i:\mathbb C\hookrightarrow\mathbb C^2\), show \(i_*k[1]\) is perverse and compare \(i^{-1}k_{\mathbb C^2}[2]\), \(i^!k_{\mathbb C^2}[2]\) with the curve heart.

**Solution.** The supported object's ordinary degree is minus one with dimension-one support; its curve-point costalk is \(k[-2][1]=k[-1]\), in degree one, and zero off the curve. Both tests (4) hold. Ordinary restriction of the ambient heart object is \(k_{\mathbb C}[2]\), degree minus two: it meets the upper curve bound minus one but fails the lower. Exceptional restriction includes the real normal shift minus two, giving \(k_{\mathbb C}\), which meets the lower bound but fails the upper. Shifting the former by minus one or the latter by plus one gives \(k_{\mathbb C}[1]\). Complex codimension and real normal degree are different.

### Four sharp complex fibre shifts

*Difficulty: Intermediate.*

For \(f:\mathbb C^d\to\{\mathrm{pt}\}\), \(d>0\), compute the inverse images of \(k\) and direct images of \(k_{\mathbb C^d}[d]\).

**Solution.** The smooth heart normalization is \(k[d]\). Ordinary inverse \(k\) is this object shifted by \(-d\), hence has perverse degree \(d\); exceptional inverse \(k[2d]\) is shifted by \(d\), hence has perverse degree \(-d\). Its point costalk is still \(k\), by the cancelling real point shift. Ordinary cohomology of \(\mathbb C^d\) is \(k\), while compact cohomology is the oriented real top class \(k[-2d]\). Thus \(Rf_*k[d]=k[d]\), target degree \(-d\), and \(Rf_!k[d]=k[-d]\), target degree \(d\). All four endpoints are attained. Their target membership is checked directly.

### A finite branched map retains monodromy

*Difficulty: Intermediate.*

Over a field let \(f:\mathbb C\to\mathbb C\), \(z\mapsto z^2\). Prove \(Rf_*k[1]\) is perverse and compute its stalks, point costalks and punctured monodromy.

**Solution.** The map is proper with zero-dimensional fibres, so the output is strong bounded complex constructible, \(Rf_*=Rf_!\), and both bounds (10) put it in the heart. Its stalks are \(k^2[1]\) at nonzero points and \(k[1]\) at zero by the proper fibre calculation. A punctured loop exchanges the two sheets, giving the transposition matrix.

At a nonzero point the costalk is \(k^2[-1]\). At zero, preimages of a sufficiently small disk and its puncture are a disk and its puncture. The unshifted fibre of their section restriction is \(k[-2]\), so the shifted point costalk is \(k[-1]\). These have degree one and satisfy (4). In characteristic two the transposition minus the identity is nonzero nilpotent, so the monodromy is not diagonalizable. Perverse membership does not imply semisimplicity.

### Integral Tor destroys a lower product bound

*Difficulty: Advanced.*

Use \(k=\mathbb Z\), \(M=\mathbb Z/2\), and \(F=M_{\mathbb C}[1]\). Show \(F\) is strong perverse but its exterior square fails the lower middle cut.

**Solution.** The resolution \([\mathbb Z\xrightarrow{2}\mathbb Z]\) in degrees minus one and zero makes \(M\) perfect. The smooth curve shift makes \(F\) a heart object. Tensoring the resolution with \(M\) gives \([M\xrightarrow0M]\), with cohomology in degrees minus one and zero. The exterior shift by two puts the product cohomology in degrees minus three and minus two. On its smooth dimension-two stratum the lower bound is minus two, violated by the negative Tor term. Both degrees meet the upper bound. The output remains strong and bounded; the absent field condition in (14) is substantive despite Noetherianity and perfect inputs.

### Exceptional Hom fixes smooth normalization

*Difficulty: Intermediate.*

Take \(X=\mathbb C^a,Y=\mathbb C^b,F=k_X[a],G=k_Y[b]\). Compute (15) and compare replacing \(q_2^!\) by \(q_2^{-1}\).

**Solution.** The real oriented fibre dimension of \(q_2\) is \(2a\), hence \(q_2^!G=k[2a+b]\). Hom from \(k[a]\) gives \(k[a+b]\), exactly the product heart object attaining the lower degree \(-a-b\). Ordinary inverse instead gives Hom \(k[b-a]\), equal to the product heart shifted by \(-2a\), with perverse degree \(2a\). For \(a>0\) it is outside the upper zero cut, though it still meets a lower bound. This is not a lower-bound counterexample; it verifies the exceptional operation's sharp normalization and real orientation shift.

### A node gives a nonsplit perverse sequence

*Difficulty: Advanced.*

Let \(Z=\{xy=0\}\subset\mathbb C^2\), \(i:Z\hookrightarrow\mathbb C^2\), and \(\nu:\mathbb C\sqcup\mathbb C\to Z\) its normalization. Over a field set \(F=i_*k_Z[1]\), \(G=i_*\nu_*k[1]\). Prove perversity and find their exact sequence.

**Solution.** On the smooth branches both are shifted rank-one curve coefficients. A small nodal neighborhood is contractible; its puncture is two disjoint punctured disks, with \(k^2\) in degrees zero and one. Restriction in degree zero is the diagonal \(k\to k^2\). Its unshifted supported fibre has \(k\) in degree one and \(k^2\) in degree two. Thus the point costalk of \(F\) has \(k\) in degree zero and \(k^2\) in degree one. For \(G\), its two normalized disks give \(k^2[-1]\), in degree one. Both meet the node's lower bound zero; their only ordinary degree minus one has dimension-one support, giving upper membership. They are strong perverse.

The ordinary sheaf sequence \(0\to k_Z\to\nu_*k\to k_{\{0\}}\to0\) is stalkwise exact, with diagonal first map at the node. Shift and rotate its triangle to obtain \(k_{\{0\}}\to F\to G\to k_{\{0\}}[1]\). All first three objects lie in the heart, giving \(0\to k_{\{0\}}\to F\to G\to0\) there. It is nonsplit: a splitting would give \(F=k_{\{0\}}\oplus G\), with nonzero ordinary \(H^0\), while \(H^0F=0\). The perverse kernel appears in point costalk degree zero despite ordinary sheaf injectivity.

### Complex orientation does not remove integral Ext

*Difficulty: Intermediate.*

For \(k=\mathbb Z,F=(\mathbb Z/2)_{\mathbb C}[1]\), compute \(D_{\mathbb C}F\) and its middle cuts.

**Solution.** Complex orientation gives \(\omega_{\mathbb C}=\mathbb Z[2]\). Dualizing the finite free resolution of \(\mathbb Z/2\) leaves \(\mathbb Z/2\) in degree one, so its coefficient dual is \((\mathbb Z/2)[-1]\). Therefore
\(D_{\mathbb C}F=(\mathbb Z/2)[-1][2-1]=(\mathbb Z/2)_{\mathbb C}\).
Its ordinary degree zero on a dimension-one stratum satisfies the lower bound minus one and violates the upper. The original was a strong heart object. Perfectness and canonical orientation hold; field-exact coefficient dualization is what fails.

## References and the subsequent programme

David Massey's [*Notes on Perverse Sheaves and Vanishing Cycles*, arXiv:math/9908107v13](https://arxiv.org/abs/math/9908107v13), §2, pp. 19–20, gives the support/cosupport and ordinary/exceptional stratum conventions, including the field duality comparison on p. 20. Section 5, pp. 44–45, gives the four holomorphic dimension bounds with constructible-output conditions. Section 1, p. 14, records the proper-support Künneth and product-Hom formulas used for comparison. Its standing constructibility assumption (p. 3) is finite generation over a regular Noetherian coefficient ring of finite Krull dimension, and the notes give these comparison results without full proofs. The weak arbitrary-coefficient results here therefore rest on the supplied degree and exceptional-Hom arguments, while the lower ordinary exterior product retains the field and strong hypotheses. Beilinson, Bernstein and Deligne's [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), §1.4.9–1.4.10, printed pp. 48–49, supplies the gluing proof mechanism. The present application separately checks complex membership, global boundedness and the evaluated product morphism. These distinctions are part of the statement's scope, not optional conventions.

The earlier lessons contain the real criteria, singular-subset bound, finite closed reconstruction and truncation arrows. Finite triangulation and lower analytic foundations retain their recorded status. The captured SH-02 [exceptional operations](../SH02/exceptional-operations.md) and manifold duality providers supply exceptional composition, bounded-first exceptional Hom and the actual submersion tensor comparison. Their own prerequisites remain dependencies. Human source expression and diagrams retain their own terms; the programme CC0 dedication covers the independently expressed exposition and worked examples.

Microlocal perversity, regular-type equivalences, full Stein vanishing, transverse microlocal restriction, specialization and final microlocal characterization remain later teaching.
