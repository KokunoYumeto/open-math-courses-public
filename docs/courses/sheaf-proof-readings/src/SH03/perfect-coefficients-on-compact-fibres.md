# Perfect coefficients on compact fibres

Proper pushforward of a constructible complex preserves its geometric constructibility. To prove that it also preserves perfect stalks, we must calculate cohomology on compact fibres. Finitely many stalk values are not enough by themselves: the maps between them contribute degrees, kernels and cokernels. We will assemble those values through finite localization and descent, preserving the whole complexes and their gluing.

Use the [weak inverse-image theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#characteristic-inverse-images-stay-weakly-constructible) and [proper-on-support weak direct image](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#properness-on-support-supplies-the-cotangent-compactness) for geometric constructibility. [Constructible gluing on an interval](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-gluing-on-an-interval.md#stalks-and-costalks) gives the local support fibres, while [the open-star cohomology theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#an-acyclic-resolution-built-from-closed-simplices) gives the section calculation used in finite descent. Compatible subanalytic triangulation is the geometric input in the common triangulation lemma.

The sheaf-operation inputs are the actual [derived proper-support fibre comparison](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-derived-fibre-formula-and-c-soft-acyclicity-derived-proper-image-fibre), [proper-support base change](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#pulling-back-a-proper-support-proper-support-base-change) and [derived composition maps](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#composing-proper-images-and-preserving-c-softness-proper-image-composition). Their section and c-soft-resolution proofs precede the constructible applications. The oriented interval calculation fixes the compact-support shift in (4).

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Perfection and ordinary inverse image

Let \(k\) be commutative of finite global dimension. Manifolds and maps are real analytic, finite dimensional with uniform dimension bounds, Hausdorff and countable at infinity. All complexes are globally bounded. A coefficient complex is **perfect** when it is quasi-isomorphic to a bounded complex of finitely generated projective \(k\)-modules.

Perfect complexes are closed under finite sums, shifts and cones. For the cone assertion, choose bounded finite-projective representatives for the two inputs. Such a representative computes its derived maps by actual chain maps: it is a bounded projective complex. The mapping cone again has bounded finite-projective terms. This proves the closure without Noetherianity.

If \(f:Y\to X\) is analytic and \(F\) is \(\mathbb R\)-constructible, the weak inverse-image theorem gives weak constructibility of \(f^{-1}F\), and

\[
(f^{-1}F)_y\simeq F_{f(y)}.
\tag{1}
\]

Every stalk on the right is perfect. Thus ordinary inverse image preserves \(\mathbb R\)-constructibility. The same stalk identity applies to restriction to any topological subset; when we use a subanalytic subset below, compatible triangulation supplies its local constancy statements. No exceptional-inverse-image identification is used in (1).

## Compact support on the line

**Line lemma.** If \(G\in D^b_{\mathbb R\text{-}c}(k_{\mathbb R})\) has compact support, then \(R\Gamma(\mathbb R;G)\) is perfect.

**Proof.** Choose a locally finite subanalytic stratification for all its cohomology sheaves, compatible with its compact support. Near that support only finitely many strata occur. On a real analytic line, every stratum is a union of open intervals or isolated points; the zero-dimensional strata are locally finite. Choose finitely many cuts
\(t_0<\cdots<t_N\) containing all changes near the support and enclosing it. Include any additional endpoints needed so that the restrictions outside \([t_0,t_N]\) are zero. On each \(I_j=(t_{j-1},t_j)\), every cohomology sheaf is locally constant, hence constant. Interval acyclicity and the bounded hypercohomology counit give

\[
G|_{I_j}\simeq (B_j)_{I_j},\qquad
B_j\simeq G_x\quad(x\in I_j).
\tag{2}
\]

Each \(B_j\) is perfect. Put \(A_j=G_{t_j}\), also perfect.

Let \(i:P\hookrightarrow\mathbb R\) be the finite closed set of cuts, and \(j:\mathbb R\setminus P\hookrightarrow\mathbb R\) its open complement. The actual localization triangle is

\[
j_!j^{-1}G\longrightarrow G\longrightarrow i_*i^{-1}G\xrightarrow{+1}.
\tag{3}
\]

Its first term is the finite sum of extensions from the bounded intervals with nonzero coefficient. Its last is the finite sum of point coefficients. Since the interval closures are compact, ordinary ambient sections of each open extension equal compactly supported interval sections. In the increasing orientation of \(\mathbb R\),

\[
R\Gamma(\mathbb R;j_!(B_j)_{I_j})\simeq B_j[-1].
\tag{4}
\]

The shift is the one-dimensional compact integration degree. Apply derived global sections to (3). It gives a triangle

\[
\bigoplus_{j=1}^N B_j[-1]\longrightarrow R\Gamma(\mathbb R;G)
\longrightarrow\bigoplus_{j=0}^N A_j\xrightarrow{+1},
\tag{5}
\]

with zero coefficients allowed. Both finite outer sums are perfect. Closure under cones proves the lemma. The connecting map in (5) retains the attachment of interval coefficients to their endpoint values. \(\square\)

The local support version of this argument is useful as well. For a cut \(t_j\), a small interval meeting its two neighbors gives

\[
R\Gamma_{\{t_j\}}(\mathbb R;G)
\simeq\operatorname{Fib}\bigl(A_j\longrightarrow B_j\oplus B_{j+1}\bigr),
\tag{6}
\]

where an absent neighboring coefficient is zero. This is the interval localization triangle with its actual two restriction maps. All three inputs are perfect, so its fibre is perfect. At a point inside a constant interval the two maps are the diagonal and the fibre is \(B_j[-1]\). These are the local costalk triangles underlying the compact-line reduction.

## Coordinate induction has no perfect-push assumption

We next prove

\[
G\in D^b_{\mathbb R\text{-}c}(k_{\mathbb R^N}),\quad
\operatorname{supp}(G)\text{ compact}
\quad\Longrightarrow\quad R\Gamma(\mathbb R^N;G)\text{ perfect}.
\tag{7}
\]

The case \(N=0\) is a point and the case \(N=1\) is the line lemma. For \(N\geq2\), use the coordinate projection
\(p:\mathbb R^N\to\mathbb R^{N-1}\).
It is proper on the compact support. The weak operation theorem makes \(Rp_*G\) bounded and weakly constructible. For any \(x\in\mathbb R^{N-1}\), proper-support base change gives

\[
(Rp_*G)_x\simeq
R\Gamma(\{x\}\times\mathbb R;G|_{\{x\}\times\mathbb R}).
\tag{8}
\]

The restriction is \(\mathbb R\)-constructible by (1), and its support is compact. The line lemma therefore makes this stalk perfect. We have proved that \(Rp_*G\) is \(\mathbb R\)-constructible at this step. Its support lies in the compact projection of \(\operatorname{supp}(G)\). Apply the induction hypothesis in dimension \(N-1\) and derived composition:

\[
R\Gamma(\mathbb R^N;G)
\simeq R\Gamma(\mathbb R^{N-1};Rp_*G).
\tag{9}
\]

This proves (7). Perfection of each intermediate direct image was obtained from its one-dimensional fibres; the general perfect-push theorem has not been assumed.

## Finite descent on a compact triangulation

Here is a second compact-cohomology proof which also treats compact singular subanalytic subsets directly.

**Compact-set lemma.** Let \(F\in D^b_{\mathbb R\text{-}c}(k_X)\) and let \(K\subset X\) be compact and subanalytic. Then \(R\Gamma(K;F|_K)\) is perfect.

**Proof.** Refine a common locally finite subanalytic cover for the finitely many cohomology sheaves, with membership in \(K\) and its complement. Choose a compatible locally finite triangulation
\(i:|S|\simeq X\). The set \(K\) is a union of open simplex images. It is closed, so it contains the faces of every simplex it contains; its inverse image is the realization of a subcomplex \(S_K\).

This subcomplex is finite. The open simplices form a locally finite family: near a point in a simplex, only its finitely many cofaces can occur. A finite neighborhood cover of the compact inverse image of \(K\) then meets only finitely many simplices. The restricted complex \(F|_K\) has simplex-constructible cohomology and perfect stalks on this finite complex.

Cover \(|S_K|\) by the finitely many open vertex stars \(U_v\). An intersection of stars for distinct vertices is empty or is the open star of their face. By [star acyclicity](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#an-acyclic-resolution-built-from-closed-simplices) and its [bounded hypercohomology comparison with the actual stalk map](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#approximating-an-arbitrary-sheaf-by-face-data),

\[
R\Gamma(U_{v_0}\cap\cdots\cap U_{v_p};F|_K)
\simeq F_x
\tag{10}
\]

for a point \(x\) on that face, when the intersection is nonempty. Every such section complex is perfect.

For completeness, finite derived Čech descent does retain the whole object here. Take a bounded-below injective resolution \(I^\bullet\) of the restricted complex. Its terms are flabby, including on open restrictions. The augmented finite Čech complex of their sections is exact: for two opens the difference map onto sections on the intersection is surjective by flabbiness, giving the Mayer–Vietoris exact sequence; induction on a finite cover gives the augmented Čech exactness. Thus the total complex of

\[
\check C^p(I^\bullet)=
\bigoplus_{v_0<\cdots<v_p}
\Gamma(U_{v_0}\cap\cdots\cap U_{v_p};I^\bullet)
\tag{11}
\]

computes \(R\Gamma(K;F|_K)\). Empty intersections contribute zero. The Čech degree is finite, and the resolution is bounded below, so this totalization and its augmentation converge without an infinite-degree interchange.

Filter the total complex by its finitely many Čech columns. Its successive quotients are the column complexes shifted by \([-p]\). Each column is, in the derived category, a finite sum of the perfect complexes (10). Finite cone closure makes the total perfect. Its differentials are the actual alternating restriction maps; they have not been discarded. \(\square\)

This proof uses perfect complexes at the faces. It needs no description by finitely generated cohomology modules, and therefore no Noetherian hypothesis.

## Proper direct image with perfect stalks

**Theorem.** Let \(f:Y\to X\) be analytic and let \(G\in D^b_{\mathbb R\text{-}c}(k_Y)\). If \(f\) is proper on \(\operatorname{supp}(G)\), then

\[
Rf_*G\in D^b_{\mathbb R\text{-}c}(k_X).
\tag{12}
\]

The same conclusion holds for \(Rf_!G\), which agrees with \(Rf_*G\) under this support properness.

**Proof.** Weak constructibility and boundedness are already proved by the weak operation theorem. At \(x\in X\), put \(Z=f^{-1}(x)\). Proper-support base change gives

\[
(Rf_*G)_x\simeq R\Gamma(Z;G|_Z).
\tag{13}
\]

The closed support \(\operatorname{supp}(G)\) is subanalytic: it is the zero-section base of its closed conic subanalytic microsupport. Hence

\[
K=Z\cap\operatorname{supp}(G)
\tag{14}
\]

is subanalytic and compact by the stated properness. The restricted complex on \(Z\) vanishes outside \(K\). Closed-support localization consequently identifies it with the direct image from its ordinary restriction to \(K\), so

\[
R\Gamma(Z;G|_Z)\simeq R\Gamma(K;G|_K).
\tag{15}
\]

The compact-set lemma makes this perfect. Thus every stalk in (13) is perfect, proving (12). The fibre \(Z\) can be singular, disconnected or noncompact away from the coefficient support; none of those possibilities changes (14)–(15). \(\square\)

If \(G\) has compact support and \(f\) is the map to a point, the theorem says that its ordinary and compactly supported global cohomology are the same perfect complex. It asserts perfection as a complex. Over Noetherian \(k\), one can further express this as bounded finitely generated cohomology; that equivalence uses the extra ring hypothesis.

## The graph and manifold-fibre reduction

The graph route gives the coordinate proof of the same general theorem, using the explicit graph factorization below. Factor

\[
Y\xrightarrow{\gamma_f}X\times Y\xrightarrow{p}X,
\qquad \gamma_f(y)=(f(y),y).
\tag{16}
\]

The graph is closed analytic. Its direct image is exact, is weakly constructible by the closed-embedding operation, and has stalks either \(G_y\) on the graph or zero off it. Thus \(\gamma_{f*}G\) is \(\mathbb R\)-constructible. The projection is proper on that object's support precisely by the original support properness. Its fibre over \(x\) is the smooth manifold \(\{x\}\times Y\), and ordinary restriction to that fibre preserves constructibility and perfection by (1). Its coefficient support is compact.

To finish this coordinate route, use the additional geometric prerequisite that a finite-dimensional countable-at-infinity real analytic manifold has a closed analytic embedding into some \(\mathbb R^N\). Closed direct image again preserves weak constructibility and perfect stalks by its exact stalk description, and carries this compact support to a compact support. Equation (7) then proves perfect fibre cohomology. Proper base change and composition in (16) give the stalk in (13). This supplies the full graph, manifold-fibre, Euclidean-coordinate and compact-line chain. The separate proof (14)–(15) uses compatible triangulation to calculate a compact singular fibre directly. The deep triangulation and embedding statements remain geometric prerequisites in their respective routes.

## Examples and exercises with solutions

### An interval needs its attachment map

*Difficulty: Introductory.*

For \(G=k_{[0,1]}\) on \(\mathbb R\), compute the triangle (5), including its connecting map, and find \(R\Gamma(\mathbb R;G)\).

**Solution.** The single interval coefficient is \(B=k\), and both endpoint coefficients are \(k\). In the increasing interval orientation the connecting map \(k^2\to k\) is \((a,b)\mapsto b-a\). Equivalently the section calculation is \([k^2\to k]\) in degrees zero and one. The map is onto and its kernel is the diagonal \(k\), so global cohomology is \(k\) in degree zero. The individual strata contribute two point terms and one interval term shifted by \([-1]\); adding their dimensions without the attachment map would not give the section complex.

### Finite free stalks can yield torsion cohomology

*Difficulty: Intermediate.*

Over \(\mathbb Z\), construct a sheaf supported on \([0,1]\) with stalk \(\mathbb Z\) at both endpoints and on the open interval, and endpoint-to-interior maps multiplication by \(2\) and \(6\), respectively. Compute its global section complex and its endpoint costalks.

**Solution.** This is the face-diagram sheaf for the closed interval, extended by its closed embedding into the line. Its derived section complex is
\[
[\mathbb Z\oplus\mathbb Z\xrightarrow{(a,b)\mapsto6b-2a}\mathbb Z]
\]
in degrees zero and one. The kernel has generator \((3,1)\) and is \(\mathbb Z\); the image is \(2\mathbb Z\), so the cokernel is \(\mathbb Z/2\). Thus \(H^0=\mathbb Z\), \(H^1=\mathbb Z/2\), and the complex is perfect because its displayed terms are finite free. At the left endpoint, (6) is the fibre of \(\mathbb Z\xrightarrow{2}\mathbb Z\), namely \((\mathbb Z/2)[-1]\). At the right it is the fibre of multiplication by \(6\), namely \((\mathbb Z/6)[-1]\). Outside coefficients are zero. Perfection permits this torsion and preserves the local degree.

### A circle projection has merging fibre values

*Difficulty: Intermediate.*

Let \(Y=S^1\subset\mathbb R^2\), \(f(x,y)=x\), and \(G=k_Y\). Compute the stalks of \(Rf_*G\), and describe its restriction maps from an endpoint of \([-1,1]\) into its interior.

**Solution.** The source is compact, so support properness holds. For \(|t|<1\) the fibre has two points, giving \(k^2\) in degree zero. At \(t=\pm1\) there is one point, giving \(k\), and for \(|t|>1\) the fibre is empty. All fibre higher cohomology vanishes. Near either endpoint the two interior points belong to the two sides of one connected small arc of the circle. A section on that arc has the same value on both sides; the endpoint-to-interior restriction is the diagonal \(k\to k^2\). These stalk complexes are perfect, and the direct image is constructible for the two endpoints and complementary intervals. Derived composition gives its global cohomology as that of the circle, with one \(k\) in degrees zero and one; the attachment maps retain the circle class.

### A compact singular fibre is allowed

*Difficulty: Advanced.*

Take \(f:\mathbb R^2\to\mathbb R\), \(f(x,y)=xy\), and \(G=k_K\), where \(K\) is the closed unit disk. Describe the coefficient fibre over zero and compute \((Rf_*G)_0\). What are the fibres for \(0<|t|<1/2\)?

**Solution.** The coefficient support is compact, so \(f\) is proper on it. At zero the compact coefficient fibre is the union of the horizontal and vertical diameter segments, a tree with four arms. A finite graph model has five vertices and four edges. Its constant-coefficient section complex has difference map \(k^5\to k^4\), sending each arm endpoint value minus the central value to its edge. This map is onto with diagonal kernel \(k\). Hence \((Rf_*G)_0=k\) in degree zero. For \(0<|t|<1/2\), the hyperbola inside the disk has two compact interval components, so its coefficient cohomology is \(k^2\) in degree zero. At \(|t|=1/2\) there are two tangency points, and beyond that the fibre is empty. The central fibre is singular, but its finite compact calculation and every displayed stalk are perfect. Smoothness of the original map or of every fibre was unnecessary.

### Finite star descent on a triangle-shaped circle

*Difficulty: Intermediate.*

Take the simplicial circle with vertices \(1,2,3\), edges \(12,13,23\), and no two-dimensional face. Cover it by the three vertex stars and calculate the constant-coefficient Čech complex.

**Solution.** Each star and each nonempty pair intersection has coefficient \(k\) in degree zero by star acyclicity. The triple intersection is empty, since there is no face \(123\). The complex is
\[
[k^3\longrightarrow k^3],\qquad
(a_1,a_2,a_3)\longmapsto(a_2-a_1,a_3-a_1,a_3-a_2),
\]
with pairs ordered \(12,13,23\). Its kernel is the diagonal \(k\), and its cokernel is \(k\), detected by \((c_{12},c_{13},c_{23})\mapsto c_{12}+c_{23}-c_{13}\). The latter map is onto and its kernel is the image: for a triple in its kernel choose \(a_1=0,a_2=c_{12},a_3=c_{13}\). Thus the derived cohomology is perfect with \(H^0=H^1=k\). Acyclic stars compute the global complex; they do not force its positive cohomology to vanish.

### Perfect complexes on a compact circle need no Noetherian reduction

*Difficulty: Advanced.*

Let \(P\) be any perfect coefficient complex and let \(P_{S^1}\) be its constant sheaf complex. Compute its derived global cohomology, and explain which property makes it perfect.

**Solution.** The finite star Čech model in the preceding exercise tensors with a bounded finite-projective representative of \(P\). Its matrix consists only of signed identity maps. The constant-coefficient complex can be split, by elementary changes of basis, into the kernel \(k\) in degree zero, the cokernel \(k\) in degree one, and two contractible identity complexes. Tensoring this decomposition gives
\(R\Gamma(S^1;P_{S^1})\simeq P\oplus P[-1]\).
It is perfect by finite direct-sum and shift closure. This uses finite-projective representatives and actual finite descent. No equivalence between perfection and finitely generated cohomology over an arbitrary ring was invoked; such an equivalence would require the additional Noetherian hypothesis used elsewhere in the course.

## References

Kashiwara and Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), [Remark 8.2.8, printed p. 148](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=151), states perfection of cohomology on a compact subanalytic set. [Proposition 8.3.1, printed pp. 148–149](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=151), proves proper constructible direct image using that remark. Ordinary inverse image is included in [Proposition 8.3.3, printed p. 149](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=152). The compact calculation here is separately proved by localization on a line, coordinate induction and finite star descent; its compatible triangulation and closed analytic embedding inputs remain explicit geometric prerequisites.

## Readable source and dependency account

A finite list of perfect stalks is not by itself a perfect global section object. The proof retains the restriction maps in finite localization triangles and in star descent; finite sums and cones of perfect complexes then give the required fibre object. Proper-support base change identifies that complex with the image stalk. The graph route retains its geometric embedding hypothesis instead of treating it as formal. The no-Noetherian claim is established by perfect-complex operations, not by replacing perfectness with finite cohomology modules.

For the classical operation statements, see Pierre Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, Theorem 6.2.7, p. 128](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=128). That section states the results without proof and uses the Noetherian coefficient convention on p. 127. The argument above establishes its perfect-complex conclusion without that convention. Schapira’s [*A short review on microlocal sheaf theory*, 19 January 2016, p. 7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=7), identifies the closed support through the zero covectors of microsupport; [Theorem 2.9, pp. 10–11](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=10), gives the proper-image microsupport estimate and its closed-embedding equality. These supply the stated classical context for the geometric part. Original programme exposition remains CC0; the human works retain their own rights.
