# Reading the geometry and cycle literature

Two formulas can look identical and describe different sheaf-theoretic objects. A punctured disc and its universal cover have different cohomology; a constant sheaf can have perfect or infinite-dimensional coefficients; a closed union of conormals need not satisfy a quantitative regularity condition. These are useful starting points for choosing a paper and comparing its theorems with this course.

*Written by GPT-6.1 Sol (OpenAI), Ultra; revised by GPT-6 Astra (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Original programme text is public domain (CC0).*

Begin a comparison by recording the data in the following table. The last column identifies the kind of argument needed to pass from one formulation to another.

| Question | Data to retain | Comparison to establish |
|---|---|---|
| Which cycle object is meant? | Zero-fibre inclusion, punctured covering, shift, monodromy action | An identified triangle and its actual maps |
| What is finite? | Coefficient ring, whole stalk complex, boundedness, stratification | Perfectness and the evaluation morphism |
| Which image is controlled? | Analytic map, support or cutoff, relative compactness | The properness condition used by the image theorem |
| Which limiting geometry is measured? | Ordered strata, two moving points, possibly unbounded covectors | A uniform tangent-gap estimate |
| How many holomorphic tests are required? | A cotangent neighborhood and every test function in it | Uniform vanishing, including the zero covectors |

## Calibrate coefficients and cycle conventions first

For the course's constructibility, direct-image and holomorphic-test comparisons, take a commutative coefficient ring of finite global dimension and retain the boundedness and dimension assumptions in the linked statements. The finite abelian-heart comparison also assumes Noetherianity. The basic cycle cone and its shift calculation need no perfectness assumption.

Let $f:X\to\mathbb C$ be holomorphic and let $i:X_0=f^{-1}(0)\hookrightarrow X$. The convention in Nearby cycles and the two monodromy triangles is

\[
 \phi_f(F)\simeq
 \operatorname{Cone}\bigl(i^{-1}F\to\psi_f(F)\bigr)[-1].
 \qquad\text{(NC)}
\]

Nearby cycles use the lifted punctured parameter space before taking sections at the zero fibre. If $F$ is supported on $X_0$, its restriction to that punctured space is zero, hence $\psi_f(F)=0$ and (NC) gives $\phi_f(F)\simeq i^{-1}F$ with its original grading. This supplies a quick check on a proposed shift convention. An unshifted cone would give $i^{-1}F[1]$ instead.

The canonical and variation morphisms in the linked construction compose to $1-M$ for its specified deck and precomposition actions. A convention with $M-1$ requires the corresponding change in the maps; agreement of their source and target objects alone does not identify those morphisms. Similarly, the circle mapping fibre $\operatorname{Cone}(T-1)[-1]$ in Local systems across an analytic boundary computes ordinary puncture cohomology. It retains the loop that the covering construction of nearby cycles removes.

Coefficient conditions provide a second calibration. Weak constructibility asks for locally constant cohomology on an appropriate common locally finite stratification. Perfect constructibility also requires the entire stalk complex to be perfect over the coefficient ring. The latter means a bounded complex of finitely generated projective modules up to quasi-isomorphism, not merely geometric local constancy. The constant sheaf with stalk $\mathbb Q^{(\mathbb N)}$ separates these conditions; its failed biduality is computed in the exercises.

For bounded perfect real-constructible inputs on real analytic manifolds with one finite dimension bound, and an analytic embedded submanifold closed in the chosen ambient neighborhood, Natural duality for specialization and microlocal Hom uses evaluation maps, normal-deformation maps, Fourier duality, antipodal transport and relative orientations. Its relative factor is $\operatorname{or}_{M/X}[-\operatorname{codim}(M,X)]$, and the dual Hom inputs are reversed. Neither a global orientation nor a field hypothesis may be inserted merely to simplify that comparison. Track the actual evaluation $F\to D_XD_XF$, including the coefficient and orientation identifications that make it an isomorphism. A microsupport bound cannot replace that coefficient argument.

For the coefficient distinction, read Kashiwara–Schapira, [*Microlocal study of sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Definition 8.2.5, p.145, and Theorem 8.2.6, pp.146–148. The definition separates weak real constructibility from the perfect-stalk requirement. The theorem relates weak constructibility to subanalytic isotropic and Lagrangian microsupport bounds. Its forward proof explicitly uses Thom's local product theorem; the course's boundary-estimate proof has to be assessed through its own lemmas. Section 5.6, especially Definition 5.6.1 and Proposition 5.6.2, p.98, treats cohomological constructibility using ordinary and compact-support section systems on shrinking neighborhoods. That condition carries more data than an isolated stalk statement.

For a second cycle formalism, Deligne's [SGA 7 II, Exposé XIII, introduction, pp.83–85](https://publications.ias.edu/sites/default/files/Number12.pdf), keeps the specialization data, monodromy and variation within a derived object. Its analytic picture begins with additional topological trivialization and retraction data; the subsequent algebraic construction uses a henselian trait and étale sheaves. Compare the objects and maps before identifying its degree convention with (NC). The course's covering construction supplies the analytic triangles used here.

## Decide which map and which neighborhood a theorem controls

An analytic image need not inherit all the geometric properties of its source. In the subanalytic setting, local projection descriptions retain a relative-compactness condition. Proper-image results likewise require properness on the closure of the selected set; properness only on that set is a different hypothesis. These conditions are relevant to the tangent graphs, normal cones and bad loci used by Subanalytic sets and limiting tangent directions and Conic subanalytic images and isotropic dimension.

Choose the geometric result by its conclusion. Curve selection supplies an analytic arc. Local finiteness controls connected components. Triangulation supplies a homeomorphism with simplices adapted to specified sets. Uniformization presents a closed subanalytic set as a proper analytic image of a manifold. None of these conclusions alone specifies a derived restriction morphism or proves that its cone vanishes.

Bierstone–Milman, [*Semianalytic and subanalytic sets*, §3](https://www.numdam.org/articles/10.1007/BF02699126/), offers a route through these compactness questions: Definition 3.1 and the closure and component properties on p.16, fibre cutting on pp.17–18, the complement theorem on p.19, and Proposition 3.12 on pp.19–20. The last result gives a closed subanalytic set a local representation as a proper projection of a closed analytic set of the same dimension. A closed subset of a compact cutoff has proper projection; relative compactness of an unclosed presenting set alone does not give that conclusion.

The same paper's Theorem 0.1, p.5, is the proper uniformization statement, completed on p.32 from Theorem 5.1 and Proposition 3.12. Theorem 0.2, p.6, and its proof on pp.32–33 instead give rectilinearization near a prescribed compact set: finitely many analytic maps, quadrant-shaped inverse images, and compact pieces whose images cover a neighborhood. Lemma 6.3, p.33, supplies a one-dimensional semianalytic parametrization under its local-connectedness hypothesis. Each is a distinct ingredient to compare with the course's arc-extraction and compatible-triangulation arguments.

For a map between stratified spaces, also distinguish full tangent spaces from tangents to fibres. Let $f$ have constant rank on the strata $M$ and $N$, and let $x_j\in M$ approach $y\in N$. Thom's $A_f$ condition requires

\[
 \ker d(f|_N)_y\subset L
 \quad\text{whenever}\quad
 \ker d(f|_M)_{x_j}\longrightarrow L.
 \qquad\text{(AF)}
\]

The differential of $f$ is part of this condition. Replacing its kernels by the full stratum tangents changes the question. The example $f(z,w)=zw$ in the exercises computes (AF) directly and separates it from a sheaf finiteness assertion.

Henry–Merle–Sabbah, [*Sur la condition de Thom stricte pour un morphisme analytique complexe*, §1, pp.228–230](https://www.numdam.org/articles/10.24033/asens.1471/), compares (AF) with a quantitative fibre-tangent estimate. Its setting is a morphism of reduced complex analytic spaces, a dense Zariski open smooth locus of fixed corank, and an analytic submanifold on which the restriction has constant corank. Definition 1.1 gives the strict condition $W_f$: the directed gap from the lower fibre tangent to the upper fibre tangent is bounded by a constant times the distance between their base points. Remarks 1.2 recall the qualitative $A_f$ comparison. The target-dimension issue in the introduction matters when considering existence of such stratifications; the sheaf theorem below specifically has a complex curve as target.

The complex-curve pushforward theorem makes its neighborhood choice explicit. Near a compact part $K$ of a fibre of a holomorphic map to a complex curve, it supplies suitable open sets $V\supset K$ and $U$ for the restricted map $f_V:V\to U$, together with the stated constructible-image conclusions and cotangent bound. In its Euclidean, single-point case $K=\{0\}$, the neighborhood can be chosen as

\[
 V=B_r(0)\cap f^{-1}(U).
 \qquad\text{(V)}
\]

The inverse-image factor can be necessary even to type the map with target $U$. For $f(z)=z$ and discs $U=B_\epsilon(0)$, $B_r(0)$ with $r>\epsilon$, the whole source ball does not map into $U$. Intersecting it with $f^{-1}(U)$ corrects that problem. The general compact-set statement does not assert this single-ball form.

There is also a stronger constructibility obstruction, even when the whole ball maps into the chosen target. Take $f:\mathbb C^2\to\mathbb C$, $f(z_1,z_2)=z_1$, and the perfect sheaf $G=k_L$ on $L=\{z_2=z_1\}$, with $k\ne0$. For $V=B_r(0)$, the target must contain the disc $D_r$. But $L\cap V$ maps isomorphically to $D_a$, where $a=r/\sqrt2$. With $j:D_a\hookrightarrow U$, the images are

\[
 R(f_V)_*(G|_V)=k_{\overline D_a},
 \qquad R(f_V)_!(G|_V)=j_!k_{D_a}.
\]

Their real-circle boundary lies inside $U$, so neither is weakly complex constructible there. Taking $U=D_\delta$ with $0<\delta<a$ and $V=B_r\cap f^{-1}(U)$ instead gives both images $k_U$. The whole-ball counterexample computes the boundary conormals. The general sheaf proof also controls unbounded horizontal covectors, an exhaustion band, closed cutoff levels and coefficient finiteness; checking (AF) alone does not supply those steps.

## Convert moving tangent estimates into conormal tests

Work in a local Euclidean chart, using its metric to identify vectors and covectors. Let $M$ and $N$ be disjoint smooth strata, with $N$ in the frontier of $M$, and let $P_y$ be orthogonal projection to $T_yN$. The relevant uniform estimate is

\[
 |P_y\xi|\le C|x-y|\,|\xi|,
 \qquad x\in M,\ y\in N,\ \xi\perp T_xM,
 \qquad\text{(W)}
\]

for all such points in one neighborhood of the lower-stratum point. It is the conormal form of Verdier's $(w)$ condition. The corresponding ordered $\mu$ condition requires $\sigma\perp T_pN$ whenever $x_j,y_j\to p\in N$, $\xi_j\perp T_{x_j}M$, $\eta_j\perp T_{y_j}N$, $\xi_j+\eta_j\to\sigma$ and $|x_j-y_j|\,|\xi_j|\to0$. The separate covectors may diverge. Their cancellation is essential to the condition.

The Whitney secant lesson proves the equivalence between (W) and that full limiting-sum condition. Its further implication to Whitney (b), and hence (a), uses subanalytic curve selection. The equivalence itself does not require subanalyticity. Closed conormal unions at singular points supplies the useful contrasting phenomenon: a closed involutive conormal union can still fail the ordered $\mu$ condition.

Read Trotman, [*Une version microlocale de la condition (w) de Verdier*, §§1–2, pp.826–828](https://www.numdam.org/articles/10.5802/aif.1190/), for this exact comparison. The article assumes a $C^2$ ambient manifold and an ordered pair of $C^2$ submanifolds with the lower one in the frontier of the upper one. Section 1 gives the moving-point estimate; the theorem and proof in §2 identify it with the full limiting cotangent sum. A useful way to check both directions is to follow the size of the projected conormal: (W) forces it to vanish in a limiting witness, whereas an unbounded ratio produces the cancelling witness computed below. Subanalytic curve extraction enters the later Whitney implication, rather than this equivalence.

A stratum contributes its conormal bundle $T_M^*X$, whose covectors annihilate $T_xM$. Moving to $T^*X$ lets the same geometry enter sheaf operations, including at singular limit points of a union. The course's route is to control full limiting sums, identify bad pair loci, form compatible refinements and obtain a closed isotropic conormal bound. The refinement retains memberships and upper closures, which gives its frontier property; local finiteness does not assert global finiteness. The resulting conormal cover may be larger than the isotropic set it was built to contain. Microlocal stratifications by removing bad loci develops that route. The constructibility criterion then uses the boundary estimate and local sheaf descent to pass from the cotangent bound to locally constant cohomology on the fixed strata.

## Match the quantifiers before using a sheaf comparison

The holomorphic microsupport test concerns a globally bounded weakly complex constructible object $F$. A covector $p$ is absent from its microsupport exactly when there is an open cotangent neighborhood $W\ni p$ such that

\[
 \phi_h(F)_x=0
 \quad\text{for every local holomorphic }h
 \text{ with }h(x)=0\text{ and }(x;dh_x)\in W.
 \qquad\text{(H)}
\]

The quantifier is over a neighborhood and a family of tests. A single vanishing test at $p$ does not establish (H). Constant functions test zero covectors. Adapted quadratic functions detect the generic nonzero conormal part, and closedness retains its singular limits. The point-sheaf exercise below checks both kinds of covector with the normalization (NC).

Other comparison theorems require their own maps. Derived constructibility through common triangulations compares bounded complexes with constructible terms and bounded ambient objects with constructible cohomology, using common triangulations, actual Hom comparisons and finite roofs. Its weak-coefficient comparison assumes finite global dimension but does not require a Noetherian ring; its finite abelian-heart comparison assumes a Noetherian ring of finite global dimension. A realization theorem for one fixed stratification is a separate assertion and can require extra link conditions. The fixed-stratification criterion uses a boundary estimate, localization and finite local removal of strata. The duality lesson uses evaluation and orientation data. These are different arguments even when all three conclusions concern constructible objects.

Schapira's [*A short review on microlocal sheaf theory* (19 January 2016), Definition 2.3, p.7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), is a compact place to examine the neighborhood quantifier in the real differentiable definition of microsupport. For the complex-geometric background, Astérisque 128, Theorem 8.5.2, pp.151–152, relates weak complex constructibility to microsupport and complex scaling. The holomorphic-cycle criterion (H) is supplied by the linked course proof, with its own coefficient hypotheses and uniform tests.

Astérisque 128, §9.1.5, pp.162–163, records the real-constructible derived-category equivalence with complex coefficients and refers elsewhere for its proof. The common-triangulation lesson supplies the actual object, Hom and roof comparisons used in this course. For duality notation, the review's §§4.1–4.4, pp.19–24, proceeds through Fourier–Sato transform, specialization, microlocalization and microlocal Hom. The “Microlocal Serre functor” formula on p.24 exchanges the inputs and retains a pulled-back dualizing complex. Compare this natural isomorphism, rather than just a support containment, with the maps and relative orientation factor in the course's duality proof.

## Extend the reading route without changing categories silently

An étale sheaf on a scheme, an analytic constructible complex, a perverse sheaf and a differential module do not denote interchangeable input objects. When following a connection between them, write down the category, coefficient field or ring, functor and degree convention before importing a finiteness statement. In particular, ordinary perfect constructibility does not impose the support and costalk degree bounds that define perversity. Those bounds, and the associated truncation structure, are additional mathematics.

Artin's [SGA 4, Exposé IX, §2, especially Definition 2.3](https://www.normalesup.org/~forgogozo/SGA4/09/09.pdf), makes the coefficient issue concrete in the étale setting. The definition uses finite locally closed decompositions on affine opens and locally constant values that are finite, or finitely presented for modules. Its footnote discusses the stronger resolution condition appropriate to non-Noetherian coefficients. This is a useful comparison with perfect stalk complexes, while the topology and category remain different.

For perversity, read Beilinson–Bernstein–Deligne, [*Faisceaux pervers*, Astérisque 100 (1982)](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Definition 1.3.1, p.29, and Theorem 1.3.6, pp.31–32, for t-structures and their abelian hearts. Then §2.1, pp.56–59, imposes the distinct restriction and exceptional-restriction degree bounds on a finite stratification and constructs the resulting perverse heart. Section 4.4, pp.114–117, concerns nearby cycles over a henselian trait. Proposition 4.4.2 proves an upper perversity estimate; the introduction explicitly separates that argument from commutation with duality, which is not proved there. This passage alone therefore does not establish both degree bounds or the analytic canonical/variation signs.

For differential equations, the review's §6.2, pp.37–40, introduces characteristic varieties and holomorphic solution complexes. Theorem 6.4 states the equality of solution microsupport and characteristic variety; its sketch proves the inclusion from the former into the latter. For the correspondence with constructible complexes, Kashiwara's [*The Riemann–Hilbert Problem for Holonomic Systems*, introduction, pp.319–321](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/RiemannHilbert.pdf), distinguishes regular holonomic modules over the ordinary differential operators from the infinite-order formulation and introduces a tempered construction of the inverse. Keep regularity, the operator sheaf and complex coefficients in the comparison. Astérisque 128, §9.2, especially Theorem 9.2.3, pp.164–165, gives a further overview. These entry passages identify the statements and functors; the full correspondence requires the later arguments in those works.

For a comparison in this course, keep a short record of the exact assertion: hypotheses, map, conclusion and the internal argument that uses it. A bibliography identifies a reading route; the transfer between formulations is supplied by a mathematical comparison. The exercises make several of those comparisons explicit.

## Solved exercises

### A point sheaf fixes the cycle shift

*Difficulty: Intermediate.*

On a disc let $F=i_{0*}P$, with $P$ a nonzero perfect coefficient complex. For $h(z)=az$, compute nearby and course-normalized vanishing cycles for $a\ne0$ and for $a=0$. Compare the result with the unshifted-cone convention and with the microsupport criterion (H).

**Solution.** For $a\ne0$, the punctured inverse image misses the support of $F$, so the lifted punctured coefficient object is zero and $\psi_h(F)=0$. Formula (NC) gives $\phi_h(F)=P$ at zero, with its original grading. For $a=0$, the entire disc is the zero fibre and the lifted punctured space is empty. Thus $\psi_0(F)=0$ and $\phi_0(F)=F$, again without changing its degree. The unshifted cone of $i^{-1}F\to0$ would instead be $i^{-1}F[1]$; shifting it by $[-1]$ recovers the convention here.

Each nonzero complex covector at zero is $dh_0$ for some $a\ne0$, and its test is nonzero. The zero covector is tested by $h=0$. Hence the fibre over zero is retained by (H). Away from zero the sheaf is zero on a neighborhood and all local tests vanish, so no covectors there occur. This agrees with the exact closed-embedding formula: the microsupport of a nonzero point sheaf is the whole cotangent fibre over its support. A shift difference in the definition would change the degrees of the tests, though not this nonvanishing conclusion.

### Geometry does not supply coefficient biduality

*Difficulty: Advanced.*

Let $k=\mathbb Q$ and $M=\mathbb Q^{(\mathbb N)}$. The constant sheaf $M_X$ on a complex manifold has zero-section microsupport. Show that it is weakly complex constructible but not perfect constructible. Prove that algebraic evaluation $M\to M^{\vee\vee}$ is not surjective, and identify the missing input in the analytic-extension duality proof.

**Solution.** The one-member analytic cover $X$ gives locally constant cohomology. A finite complex of finite-dimensional vector spaces has finite-dimensional cohomology, whereas $M$ is infinite dimensional in degree zero; the stalk is not perfect. Its algebraic dual is $M^\vee=\mathbb Q^{\mathbb N}$, since a functional on a finite-support vector may have an arbitrary sequence of values on the coordinate basis.

The subspace of finite-support sequences inside $\mathbb Q^{\mathbb N}$ does not contain the constant sequence $(1,1,\ldots)$. Extend its nonzero quotient class to a basis of the quotient, and choose a linear functional on that quotient taking value $1$ on this class. Pull it back to a functional $\ell$ on $M^\vee$. It vanishes on every finite-support sequence but is nonzero. If $\ell$ were evaluation at $m\in M$, evaluating it on each single-coordinate sequence would force every coordinate of $m$ to be zero. Then its evaluation would be zero, a contradiction. Thus $M\to M^{\vee\vee}$ is not surjective.

In the analytic-extension proof the actual input evaluation $F\to D_UD_UF$ is used to identify the ordinary image with the dual of the zero extension of $D_UF$. Locally the orientation shifts cancel under double duality, leaving this coefficient evaluation. The present infinite coefficient object lacks its isomorphism. It also fails the analytic-extension theorem's perfect-input hypothesis. A geometric microsupport argument cannot repair that failure; particular weak extensions may still be geometrically constructible for a separate reason.

### Turn an unbounded ratio into a μ-obstruction

*Difficulty: Advanced.*

Let $x_j\in M$ and $y_j\in N$ approach $p\in N$. Suppose unit conormals $\zeta_j\perp T_{x_j}M$ satisfy $a_j=|P_{y_j}\zeta_j|>0$ and $a_j/|x_j-y_j|\to\infty$. Produce a full limiting-sum witness which violates the ordered μ-condition, after taking a subsequence. State where smoothness of $N$ is used.

**Solution.** Define

\[
 \xi_j=\zeta_j/a_j,\qquad
 \eta_j=-(1-P_{y_j})\zeta_j/a_j.
\]

The first remains conormal to $M$ at $x_j$. The second is conormal to $N$ at $y_j$. Their sum is $P_{y_j}\zeta_j/a_j$, a unit tangent vector to $N$ at $y_j$. The unit sphere is compact, so take a subsequence with sum converging to a unit vector $v$. Smoothness gives $P_{y_j}\to P_p$, hence $v\in T_pN$. Meanwhile $|x_j-y_j|\,|\xi_j|=|x_j-y_j|/a_j\to0$. These are all the full limiting-sum conditions. Its output is the nonzero tangent vector $v$, which is not conormal to $N$ at $p$, so μ fails. The possible divergence of the two separate covectors is the essential feature; a test limited to bounded individual covectors would miss this obstruction.

### Fibre tangents at a normal crossing

*Difficulty: Intermediate.*

For $f(z,w)=zw$ on $\mathbb C^2$, use the strata $M=\{zw\ne0\}$, the two punctured coordinate axes, and the origin. Verify the relative condition (AF) at every frontier incidence. Does the verification alone prove bounded perfect direct images for every nonproper restriction of $f$?

**Solution.** On $M$, the differential is $df(v_z,v_w)=wv_z+zv_w$ and has rank one. Its kernel is the complex line spanned by $(z,-w)$. If $(z,w)$ approaches $(a,0)$ with $a\ne0$, that line tends to the horizontal line. On the punctured horizontal axis $f$ is constant, so the tangent to its fibre is exactly that horizontal line. Inclusion (AF) is equality. At a point $(0,b)$ of the other axis the limit is vertical and again equals the lower fibre tangent.

At the origin the lower tangent is zero. Its fibre tangent is therefore zero, contained in every possible limiting plane from the upper stratum or either punctured axis. These are all distinct frontier incidences. Rank is constant on each stratum, and the same computation works for the underlying real fibre tangents. Thus (AF) holds throughout this stratification.

The calculation proves a relative tangent condition. It does not verify compactness of a support or of a cotangent incidence, a chosen cutoff band, the maps in a derived-image comparison, or finiteness of coefficient complexes. The controlled neighborhood theorem uses those additional sheaf and cutoff arguments. Its conclusion cannot be extended to an arbitrary nonproper restriction solely from the displayed kernel lines.

### What a citation record proves

*Difficulty: Introductory.*

A student finds a journal record for Trotman's 1989 paper giving its author, title, pages and a statement of $(w)$–μ equivalence. Which of the following have thereby been checked: identification of the work, that the work states the equivalence, the complete proof of the equivalence, and historical priority over every other work? Give a proof-reading task that would close the third question for the formulation (W).

**Solution.** The record checks identification and its stated result. It does not show the entire proof, nor does its date compare every possible earlier occurrence. For the proof task, retain the ordered pair, both moving points, the orthogonal projection and the norm–distance product. One must prove both that failure of (W) yields an unbounded cancelling conormal witness and that (W) kills the tangent component of every limiting witness. The ratio exercise supplies the first direction; the converse follows by applying (W) to the first covector and noting that the second is conormal to the lower tangent. This checks the precise equivalence used here without converting a citation date into a priority theorem.

### Distinguish a new proof from a new theorem

*Difficulty: Introductory.*

A reader encounters the projection proof of $(w)$–$\mu$ equivalence and calls the equivalence a new theorem of this course. Another reader insists that the fixed-stratification constructibility argument must use Thom–Mather isotopy because isotopy is common in the literature. Assess these claims using Trotman's 1989 theorem and the actual proof steps: the $\mu$ boundary estimate, zero-section local descent, a localization triangle and finite local removal of strata. What remains to check if any of these steps is supplied by an earlier lemma?

**Solution.** Trotman's theorem in §2 already states the equivalence for the indicated ordered pair of $C^2$ submanifolds. A later presentation of its projection argument therefore does not establish novelty of that equivalence. A publication date alone would not prove a claim of earliest priority either: that would require a comparison with other relevant work.

The proposed necessity of isotopy must be tested against the actual argument. The listed proof uses the boundary estimate to obtain the required support control, local descent on a stratum, and localization to remove strata successively. Merely knowing a different proof by isotopy does not insert an isotopy step into this one. Each earlier lemma still needs its own hypotheses and proof; for example, local finiteness is needed to reduce a neighborhood to finitely many strata. One may establish a direct proof while still relying on substantial geometric or sheaf-theoretic lemmas. The legitimate comparison names those lemmas and the maps they provide, rather than inferring dependence or independence from a subject label.
