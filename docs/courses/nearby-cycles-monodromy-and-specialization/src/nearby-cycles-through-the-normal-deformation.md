# Nearby cycles through the normal deformation

Normal specialization follows a sheaf toward a submanifold along positive real scales. Nearby cycles follow a complex function after lifting its nonzero values to the universal cover. For a regular zero fibre these two limits agree, including for weak real-constructible sheaves. The key boundary comparison involves a countable covering. We prove its actual map using a common cofinal system of neighborhoods, rather than exchanging an infinite product with a stalk colimit formally.

We retain the regular defining-function hypothesis required by the normal section. The positive-chamber specialization construction is described in the freely accessible [Fernandes–Kudomi–Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, version 2, §2.4](https://arxiv.org/html/2603.14821v2#S2.SS4). Their [equation (4.54)](https://arxiv.org/html/2603.14821v2#S4.E54) also identifies this construction with real nearby cycles of the deformation parameter. These passages specify the positive-chamber construction; they do not prove the weak real-coefficient complex-cover comparison needed here. Our route first isolates the countable-cover boundary map, checks the common shrinking neighborhoods it requires, then uses the logarithmic lift to compare the deformation with the cover. The gluing argument records the dependence on a lift of one. Its small-ball, base-change and conic-recovery inputs are stated at the points of use and remain separate prerequisite theorems. Complex-conic section and microlocalization formulas are subsequent results.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## The normal function and the hypothesis it needs

All manifolds in this lesson are Hausdorff and countable at infinity, with uniform finite dimension bounds.

Let \(X\) be a finite-dimensional complex manifold, \(k\) a commutative ring of finite global dimension, and \(F\in D^b_{w\text{-}\mathbb R\text{-}c}(k_X)\). Let \(f:X\to\mathbb C\) be holomorphic, with

\[
Y=f^{-1}(0),\qquad i:Y\hookrightarrow X,
\qquad df_y\neq0\quad(y\in Y).
\tag{1}
\]

The condition makes the analytic fibre regular. Its complex normal bundle \(E=T_YX\) has a canonical fibrewise linear function

\[
\ell:E\longrightarrow\mathbb C,\qquad
\ell_y([v])=df_y(v).
\tag{2}
\]

Since \(df\) vanishes on \(T_yY\), this is well-defined. Since the normal line is one-dimensional and the derivative is nonzero, it identifies \(E\) with \(\mathbb C\times Y\). Write \(e:Y\hookrightarrow E\) for the zero section, \(\tau:E\to Y\) for the projection, \(E^*=E\setminus e(Y)\), and \(\tau^\circ:E^*\to Y\). The derivative determines the normal section

\[
s(y)=\ell_y^{-1}(1).
\tag{3}
\]

This section does not exist for a ramified defining function whose reduced zero set happens to be smooth. For example \(f(z)=z^2\) has \(df_0=0\). General cycles of a critical function still have the [proper graph construction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/proper-pushforwards-of-nearby-and-vanishing-cycles.md#the-graph-construction-has-a-zero-extension-term) in the preceding lesson.

We will prove, with the [coefficient-complex cycle convention](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#one-two-term-complex-gives-two-triangles) fixed in the first lesson,

\[
\psi_f(F)\simeq\psi_\ell(\nu_YF),
\qquad
\phi_f(F)\simeq\phi_\ell(\nu_YF).
\tag{4}
\]

Both sides live on \(Y\). A lift of \(1\) in the universal cover fixes its coordinate convention. No finite-generation, perfect-stalk or complex-constructibility assumption is made.

## Small neighborhoods control a countable cover

We first prove the boundary lemma needed in the deformation. Let \(M\) be a real analytic manifold, \(b:N\hookrightarrow M\) a closed analytic submanifold, and \(\pi:\widehat M\to M\) a covering whose fibres have a fixed countable index set locally. Let \(\pi_0:\widehat N\to N\) be its base change. For \(G\in D^b_{w\text{-}\mathbb R\text{-}c}(k_M)\), the ordinary base-change morphism

\[
b^{-1}R\pi_*\pi^{-1}G
\longrightarrow R\pi_{0*}\pi_0^{-1}b^{-1}G
\tag{5}
\]

is an isomorphism.

Fix \(x\in N\). Choose an analytic coordinate ball centred at \(x\), with \(N\) a coordinate plane, small enough to trivialize the covering. The [weak inverse-image theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#characteristic-inverse-images-stay-weakly-constructible) makes \(b^{-1}G\) weakly constructible. The [small-ball stabilization proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#an-interval-star-and-its-closed-endpoint), with its [compact chart cutoff](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#applying-the-theorem-in-an-open-coordinate-chart), gives a cofinal family of sufficiently small balls \(B_\epsilon\) for which the actual maps

\[
R\Gamma(B_\epsilon;G)\longrightarrow G_x,
\qquad
R\Gamma(B_\epsilon\cap N;b^{-1}G)\longrightarrow G_x
\tag{6}
\]

are isomorphisms. Both assertions hold for every sufficiently small radius, so one family works for both. The restriction between their left sides becomes the identity under the right-side identifications. These statements concern whole bounded complexes, not just an independently chosen basis in each cohomology module.

If the local sheet set is \(I\), then

\[
R\Gamma(\pi^{-1}B_\epsilon;\pi^{-1}G)
\simeq\prod_{a\in I}R\Gamma(B_\epsilon;G).
\tag{7}
\]

The space on the left is a disjoint union of copies of the ball. Derived sections on a disjoint union are the product of the component derived sections. Products of modules are exact, so this product has no extra product-derived term and preserves the bounded quasi-isomorphisms in (6). The analogous formula on \(N\) uses \(B_\epsilon\cap N\).

On this cofinal system, both sides of (7) map naturally to \(\prod_{a\in I}G_x\), and every restriction map is identified with its identity. Taking the filtered stalk colimit therefore gives

\[
(R\pi_*\pi^{-1}G)_x\simeq\prod_{a\in I}G_x,
\qquad
(R\pi_{0*}\pi_0^{-1}b^{-1}G)_x\simeq\prod_{a\in I}G_x.
\tag{8}
\]

The actual map (5), defined by restriction of sections and ordinary adjunction, is the product of the maps between the two left sides in (6). It becomes the identity in (8). Thus it is a stalk isomorphism at every point, proving the lemma.

We have not asserted that filtered colimits commute with arbitrary infinite products. The cofinal stabilization and the same restriction map on every sheet are what make this particular calculation valid. Neither finite rank nor properness of the covering is required. Exercise 4 gives an explicit failure without constructibility.

## Deformation and its logarithmic lift

First work locally near the zero fibre in a holomorphic submersion chart. Use \(X=\mathbb C\times Y\) only as notation for this local product model, with \(f(z,y)=z\). Shrinking to product neighborhoods is enough; all displayed spaces and maps are restricted to their actual chart domains. The [normal-deformation chart construction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/normal-geometry.md#sh02-ng-construction--the-deformation-manifold-and-its-maps) gives coordinates

\[
D=\mathbb R_t\times\mathbb C_z\times Y,
\quad p_D(t,z,y)=(tz,y),
\quad D_+=\{t>0\}.
\tag{9}
\]

Let \(j:D_+\hookrightarrow D\) and \(b:E\hookrightarrow D\) be the positive chamber and the time-zero fibre. The [normalized normal-specialization construction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-boundary--fixing-the-boundary-shift) gives

\[
\nu_YF=b^{-1}Rj_*p_+^{-1}F,
\qquad p_+=p_D|_{D_+}.
\tag{10}
\]

No extra degree shift occurs in this definition: the oriented positive-parameter contribution and the boundary convention have already been fixed in the existing specialization course.

Remove the normal zero coordinate and set

\[
D^*=\mathbb R\times\mathbb C^*\times Y,
\quad D_+^*=\mathbb R_{>0}\times\mathbb C^*\times Y,
\quad E^*=\mathbb C^*\times Y.
\]

Write \(j^*:D_+^*\hookrightarrow D^*\) and \(b^*:E^*\hookrightarrow D^*\). Let \(q:\widetilde U=\mathbb C_w\times Y\to X\) be
\(q(w,y)=(\exp(2\pi\mathrm i w),y)\). Define the deformation covering

\[
\pi:\widehat D^*=\mathbb R\times\mathbb C_w\times Y\longrightarrow D^*,
\qquad \pi(t,w,y)=(t,\exp(2\pi\mathrm i w),y).
\tag{11}
\]

Its positive and central restrictions are \(\pi_+\) and \(\pi_0\). Put \(\widehat j:\widehat D_+^*\hookrightarrow\widehat D^*\). The lift of \(p_+\) is

\[
\widehat p_+(t,w,y)
=\left(w+\frac{\log t}{2\pi\mathrm i},y\right),
\qquad t>0.
\tag{12}
\]

Indeed exponentiating its first coordinate multiplies \(\exp(2\pi\mathrm i w)\) by \(t\). The square with \(q,p_+,\pi_+,\widehat p_+\) is cartesian. For a pair of lifts in this square their difference is exactly the displayed logarithmic translation. Both \(p_+\) and \(\widehat p_+\) are submersions. The latter is a projection after the diffeomorphism \((t,w,y)\mapsto(t,w+\log t/(2\pi\mathrm i),y)\). The logarithm is the unique real logarithm of the positive parameter; no branch across time zero is being chosen.

## Comparing the lifted boundary objects

Set \(H=Rq_*q^{-1}F\). The [finite-dimensional ordinary direct-image bound](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#from-compact-extension-to-ordinary-cohomology-ordinary-cohomology-bound) makes it bounded. The [ordinary product base-change proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-functors--transport-through-sheaf-operations), applied in submersion coordinates to the cartesian square in (12), gives

\[
p_+^{-1}H|_{D_+^*}
\simeq R\pi_{+*}\widehat p_+^{-1}q^{-1}F
=R\pi_{+*}\pi_+^{-1}p_+^{-1}F|_{D_+^*}.
\tag{13}
\]

In those coordinates, the proof computes the actual ordinary base-change map on a cofinal basis of product neighborhoods. [Cylinder descent](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) removes their interval factor by the ordinary unit, compatibly with restriction. This proves the stated comparison for the submersions in (12), without requiring properness of the covering.

Let

\[
G=Rj^*_*p_+^{-1}F|_{D_+^*}.
\tag{14}
\]

This is weakly real constructible on the whole \(D^*\), including time zero. To justify that assertion, the analytic map \(p_D\) pulls \(F\) back to a weakly constructible object on \(D\). The constant sheaf on \(D_+\), extended by zero, is weakly constructible on \(D\). The identity
\(Rj_*j^{-1}p_D^{-1}F=R\mathcal Hom(k_{D_+},p_D^{-1}F)\), together with the [weak internal-Hom theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#tensor-and-internal-hom-retain-the-full-limiting-sum) and its [open-extension application](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#the-open-extension-used-in-specialization), gives weak constructibility and boundedness. Restriction gives (14). Thus we are not applying a theorem about arbitrary nonproper direct images to an unrestricted sheaf on an open chamber.

Ordinary composition of direct images and local-homeomorphism base change in the open square give

\[
\begin{split}
\nu_YH|_{E^*}
&\simeq (b^*)^{-1}Rj^*_*R\pi_{+*}\pi_+^{-1}p_+^{-1}F\\
&\simeq (b^*)^{-1}R\pi_*R\widehat j_*\pi_+^{-1}p_+^{-1}F\\
&\simeq (b^*)^{-1}R\pi_*\pi^{-1}G\\
&\simeq R\pi_{0*}\pi_0^{-1}(b^*)^{-1}G\\
&=R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\end{split}
\tag{15}
\]

The local-homeomorphism exchange in the third line is checked near one point of the covering, where it is a diffeomorphism; it introduces no infinite product. The fourth line is the proved boundary lemma (5), whose hypothesis is exactly the whole-chamber weak constructibility established for \(G\). This is the countable-cover boundary step, with the common neighborhoods required for it established in (6).

All maps in (15) are the ordinary restriction/base-change and composition maps. They commute with the deck translations and their trace units. Under positive normal dilation, the covering lift is translation by \(\log\lambda/(2\pi\mathrm i)\). These canonical lifted actions also make (15) compatible with positive conicity.

## Recovering nearby cycles from the punctured normal bundle

We use the existing specialization recovery maps with their precise punctured form. If \(a:U=X\setminus Y\hookrightarrow X\), they give

\[
e^{-1}\nu_YB\simeq i^{-1}B,
\qquad
R\tau^\circ_*(\nu_YB|_{E^*})
\simeq i^{-1}Ra_*a^{-1}B.
\tag{16}
\]

These are the current SH02-SP-ZERO and SH02-SP-PUNCTURE comparisons, including their actual unit, support counit and first-arrow compatibility. The [ordinary and punctured recovery proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-zero--what-survives-when-the-direction-is-forgotten) checks both comparisons in one localization diagram. Its lower tautness and topology inputs remain separate prerequisites.

The covering map factors as \(q=a\widetilde q\). Hence \(H=Ra_*R\widetilde q_*\widetilde q^{-1}(F|_U)\), and the natural localization unit

\[
H\longrightarrow Ra_*a^{-1}H
\tag{17}
\]

is an isomorphism. Apply the punctured formula (16) to \(B=H\). It identifies the pushforward of the left side of (15) with \(i^{-1}H=\psi_f(F)\).

On the right side of (15), composition gives

\[
R\tau^\circ_*R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\tag{18}
\]

This is \(\psi_\ell(\nu_YF)\). To see the exact type, let \(c:E^*\hookrightarrow E\). The normal covering map is \(c\pi_0\). Its nearby object is
\(e^{-1}Rc_*R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*})\). The object inside \(e^{-1}\) is positively conic, by the lifted dilation just described. [Conic ordinary contraction](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-radial-star--ordinary-contraction-to-the-zero-section) identifies its zero-section restriction with its \(R\tau_*\), which is precisely (18). Thus (15) proves the first comparison in (4). Restricting to the whole normal bundle without its puncture would not be the same intermediate calculation.

## The ordinary unit and the vanishing comparison

Let \(u_F:F\to H\) be the covering adjunction unit. In the coefficient description of the preceding lessons it is precomposition with the finite-support trace \(L\to k\). The smooth comparison (13) sends its pullback to the covering unit on the positive chamber. The composition and local-cover maps in (15) preserve that unit, and the boundary map (5) is induced by the actual restriction of those same sections. Consequently (15) sends \(\nu_Yu_F|_{E^*}\) to the unit

\[
\nu_YF|_{E^*}\longrightarrow
R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\tag{19}
\]

The natural ordinary restriction recovery in (16), and its punctured-unit compatibility, now give the commutative square

\[
\begin{array}{ccc}
i^{-1}F&\longrightarrow&\psi_f(F)\\
\downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim\\
e^{-1}\nu_YF&\longrightarrow&\psi_\ell(\nu_YF).
\end{array}
\tag{20}
\]

The horizontal arrows use the same trace/shift convention. Vanishing cycles are the signed fibre complexes supplied by the explicit coefficient complex \(K=[L\to k]\), with \(L\) in degree \(-1\). Apply its functorial coefficient-Hom construction to (20). Equivalently, choose compatible complex models for the trace-unit square and take its fixed signed fibre. This produces a map of the actual first monodromy triangles

\[
\psi_f(F)[-1]\longrightarrow\phi_f(F)\longrightarrow i^{-1}F\longrightarrow,
\qquad
\psi_\ell(\nu_YF)[-1]\longrightarrow\phi_\ell(\nu_YF)
\longrightarrow e^{-1}\nu_YF\longrightarrow.
\tag{21}
\]

The nearby and ordinary-restriction maps are isomorphisms, so the induced fibre map is an isomorphism. This is the second comparison in (4). It is a specified natural construction; an arbitrary object-level choice of cone isomorphism would not establish (20) or the canonical-map compatibility. The deck action and its identity on the constant coefficient term commute throughout, so the comparison also intertwines monodromy. The original \([-1]\) remains in (21).

## Why the local calculation glues

For a general regular \(f\), holomorphic submersion charts use \(f\) as their first coordinate. The normal deformation has a more intrinsic way to express the logarithmic construction. On its positive chamber define

\[
f_t=\frac{f\circ p_D}{t}.
\tag{22}
\]

It extends analytically through the central fibre and has central value \(\ell\). In an adapted normal chart \(p_D(v,y,t)=(tv,y)\), the numerator vanishes at \(t=0\); its analytic power series is divisible by \(t\), and its quotient at zero is \(df_y(v)\). This proves the extension and independence of the chart. The global deformation parameter is the same \(t\) in every chart.

Pull the universal cover back by \(f_t\) on its nonzero locus. For \(t>0\), adding \(\log t/(2\pi\mathrm i)\) to the covering coordinate lifts multiplication by \(t\), exactly as in (12). At time zero the covering is that of \(\ell\). Thus all covering, unit and boundary maps used above are restrictions of maps defined by (22), rather than unrelated choices on each chart. They glue. Replacing the chosen lift of \(1\) translates the covering coordinate by an integer; the resulting comparisons are conjugated by the corresponding deck identification. This records the precise dependence of these comparison maps on the chosen lift.

The proof establishes the full weak real comparison. It does not replace nearby cycles by the value of \(\nu_YF\) at \(s(y)\). The latter requires additional complex conicity, as the next example shows.

## A real angular sheaf produces infinitely many nearby coefficients

For this counterexample take a nonzero coefficient ring. On \(X=\mathbb C\), take \(f(z)=z\) and the closed-ray sheaf

\[
F=k_{[0,\infty)}.
\tag{23}
\]

It is perfect real constructible over a field, with a finite real analytic partition, but it is not complex constructible. It is positively conic, so the [homogeneous specialization calibration](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/specialization.md#sh02-sp-homogeneous--a-calibration-on-a-vector-space) gives \(\nu_{\{0\}}F=F\).

A punctured disc \(0<|z|<\epsilon\) lifts to the half-plane
\(\operatorname{Im}w>-(\log\epsilon)/(2\pi)\). The positive real ray lifts to the disjoint vertical lines \(\operatorname{Re}w=n\), \(n\in\mathbb Z\). Their portions in that half-plane are contractible and form a closed locally finite family there. Derived sections are therefore

\[
\psi_f(F)=\prod_{n\in\mathbb Z}k
\quad\text{in degree zero}.
\tag{24}
\]

The same covering computation applies to \(\psi_\ell(\nu F)\), verifying (4) with an actual infinite product. But \(s^{-1}\nu F\), at the normal direction \(1\), is only \(k\). Thus the weak real comparison cannot be strengthened to that section formula without a complex-constructibility hypothesis.

The central restriction is the diagonal \(k\to\prod_n k\). With the fixed deck convention, nearby monodromy is a bilateral shift; canonical is the quotient onto
\((\prod_n k)/\operatorname{diag}k\), in degree one, and variation is induced by \(1-M\). This difference operator is surjective on the product: fix the value at index zero and solve the difference equation successively in both directions, using a finite sum for each individual coordinate. Its kernel is exactly the diagonal. Hence variation is an isomorphism on that quotient and the central costalk is zero, consistently with the closed-ray endpoint calculation.

## Exercises

### 1. A nonconstant unit in the defining function
*Difficulty: Introductory.*

Let \(X=\mathbb C_z\times Y\), let \(a:Y\to\mathbb C^*\) be holomorphic, and take \(f(z,y)=a(y)z\). Calculate \(\ell\), \(s\), and \(f_t\). Explain why no global logarithm of \(a\) is required.

**Solution.** The zero fibre is \(z=0\), with nonzero normal derivative. In the normal coordinate \(v\), formula (2) is \(\ell(v,y)=a(y)v\), so \(s(y)=(a(y)^{-1},y)\). The deformation map is \((t,v,y)\mapsto(tv,y)\), and \(f_t=a(y)v\) for all \(t\), including zero. It is already the intrinsic extended quotient.

The covering is pulled back by this nonzero normal function. Its positive-to-original lifted map uses only multiplication by \(t\), hence the real \(\log t\). It does not trivialize the covering by selecting a logarithm of \(a(y)\). Local logarithms of \(a\), if used to write coordinates, differ on overlaps by integer deck translations. The intrinsic pullback-cover construction respects those transitions and gives the same global comparison.

### 2. Check the logarithmic square and its dimension
*Difficulty: Intermediate.*

Verify that (12) gives a cartesian square and a submersion. Explain why the nearby comparison has no new cohomological shift from the positive deformation parameter.

**Solution.** A point of the fibre product consists of \((t,z,y)\), \(t>0,z\neq0\), and \((w',y)\) with \(\exp(2\pi\mathrm i w')=tz\). Its corresponding coordinate in \(\widehat D_+^*\) is \(w=w'-\log t/(2\pi\mathrm i)\); exponentiating gives \(\exp(2\pi\mathrm i w)=z\). This construction and its inverse are continuous and smooth, proving the cartesian identification.

The change \((t,w,y)\mapsto(t,w+\log t/(2\pi\mathrm i),y)\) is a diffeomorphism, with the inverse subtracting that logarithm. Under it \(\widehat p_+\) is projection, hence a submersion. Formula (13) is ordinary smooth base change and ordinary inverse image. Formula (10) is the already normalized ordinary boundary restriction defining \(\nu\). Neither adds an orientation factor or an exceptional fibre-integration shift. The \([-1]\) in the vanishing triangle is its coefficient-cone normalization, retained identically on both sides.

<a id="locate-the-productlimit-argument"></a>
<a id="3-locate-the-productlimit-argument"></a>

### 3. Locate the product–colimit argument
*Difficulty: Intermediate.*

In the boundary lemma, explain why the balls can be chosen simultaneously for \(G\) and \(b^{-1}G\). Prove that the base-change map is the identity on the product of stalks. Does the proof require finite coefficient modules?

**Solution.** In submanifold coordinates the intersection of an ambient centred ball with the coordinate plane is its centred ball. Apply the local weak small-ball theorem to \(G\), and separately to the weak inverse image \(b^{-1}G\). Each theorem works for all radii below some positive bound. The smaller bound, together with a bound ensuring cover trivialization, works simultaneously. These balls form a cofinal neighborhood system.

The natural restriction \(R\Gamma(B_\epsilon;G)\to R\Gamma(B_\epsilon\cap N;b^{-1}G)\) commutes with restriction to the common stalk \(G_x\). Both stalk maps are isomorphisms, so that restriction is identified with the identity of \(G_x\). A trivialized covering gives the same map on every sheet. Their product is therefore the identity on \(\prod_I G_x\). Exactness of module products preserves the bounded quasi-isomorphisms. The cofinal restriction system has already stabilized before its filtered colimit is taken. No finite-generation hypothesis is used or needed.

### 4. A covering boundary map without constructibility
*Difficulty: Advanced.*

On \(M=\mathbb R\), let \(G=\bigoplus_{n\geq1}k_{\{1/n\}}\), and let \(N=\{0\}\). Use the trivial countable covering \(\pi:\mathbb N\times M\to M\). For a nonzero ring, show that (5) is not an isomorphism in degree zero.

**Solution.** Stalks commute with direct sums, and each point sheaf has zero stalk at zero, so \(G_0=0\). The right side of (5) is thus zero: the covering over a point has exact product direct image of zero modules.

For a small interval \(B_\epsilon\) about zero, sections of \(G\) are finite-support families on the points \(1/n<\epsilon\). Indeed a section of a sheaf direct sum is locally a finite sum; a neighborhood of zero must contain only finitely many nonzero terms of that section. Outside a still smaller neighborhood of zero, only finitely many of the points \(1/n\) remain. Thus its whole family is finite-support.

Sections of \(\pi_*\pi^{-1}G\) on that interval are the product, over the sheet index \(r\), of these finite-support families. Take the \(r\)-th component to be the point section at \(1/r\) when that point is in the interval, and zero otherwise. On every smaller interval infinitely many of those components remain nonzero. Consequently this product section defines a nonzero germ at zero. Since the input is in degree zero, \(H^0(R\pi_*\pi^{-1}G)=\pi_*\pi^{-1}G\); the left side of (5) therefore has nonzero degree-zero stalk. This proves failure.

The sheaf is not weakly real constructible near zero: its exceptional points accumulate there. The example violates precisely the cofinal stabilization hypothesis, not finite rank on an individual point. It gives a sheaf-level instance of the product–colimit obstruction.

### 5. Compute the closed-ray monodromy and variation
*Difficulty: Advanced.*

For (23), prove (24), calculate vanishing cycles, and prove that variation is an isomorphism. Compare the output with the normal section at \(1\).

**Solution.** The lifted supported set in every upper half-plane is a disjoint locally finite union of vertical half-lines indexed by integers. Each component carries the constant sheaf with ordinary cohomology \(k\) in degree zero. Derived sections on their disjoint union are their exact product, so every lifted-neighborhood coefficient is \(P=\prod_{\mathbb Z}k\). Shrinking the original disc raises the lower horizontal bound, and each vertical restriction is the constant-sheaf isomorphism. Hence the filtered colimit remains \(P\).

The central stalk of the closed ray is \(k\); a constant central section restricts to the same value on each lift, giving \(D=\operatorname{diag}k\subset P\). The first cycle triangle gives \(\phi=(P/D)[-1]\), with canonical the quotient. Monodromy is the bilateral shift under the source sheet convention. Variation sends \(\overline v\) to \((1-M)v\). Its kernel is zero because the shift invariants in the product are exactly \(D\). For every \(b\in P\), the equations for \((1-M)v=b\) can be solved by fixing \(v_0=0\) and recursively defining successive coordinates on both sides of zero. Each coordinate involves only finitely many additions, so the solution works over any ring. Variation is therefore surjective and hence an isomorphism.

The second triangle gives zero costalk, consistent with a constant sheaf on a closed half-ray at its endpoint. Positive-conic calibration makes \(\nu F=F\), so the same calculation verifies the normal nearby comparison. But its stalk at \(1\) is \(k\), whereas the nearby object is \(P\). Over a field this is an infinite-dimensional distinction. Real angular constructibility cannot replace the complex conicity needed for the section formula.

### 6. A complex supported on the central fibre
*Difficulty: Introductory.*

Let \(F=i_*A\), for a bounded weakly real-constructible complex \(A\) on \(Y\). Check both comparisons in (4), including the ordinary restriction and monodromy.

**Solution.** The punctured covering pullback is zero, so \(\psi_f(F)=0\) and the first triangle gives \(\phi_f(F)=A\). The deck action on its constant coefficient term is the identity, so monodromy is the identity. The current specialization construction identifies \(\nu_Yi_*A=e_*A\) with its actual ordinary and supported recovery maps. This has zero restriction to \(E^*\), giving \(\psi_\ell(e_*A)=0\) and \(\phi_\ell(e_*A)=A\). The square (20) becomes the identity between the ordinary coefficients \(A\) and zero nearby terms. Its signed fibre comparison is the identity of \(A\). All shifts already present in \(A\) are retained.

### 7. A normal constant family with arbitrary coefficients
*Difficulty: Intermediate.*

On \(X=\mathbb C\times Y\), let \(F\) be the pullback of a bounded weakly real-constructible complex \(A\) on \(Y\). Take \(f(z,y)=z\). Compute \(\nu_YF\), both nearby objects in (4), and both vanishing objects, without assuming \(A\) perfect.

**Solution.** In the positive deformation chamber, \(p_+^{-1}F\) is the pullback of \(A\) under the \(Y\)-projection and is independent of the time and normal coordinates. [Product interval descent](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) at time zero identifies \(\nu_YF\) with the same normal-constant pullback of \(A\) to \(E\). On the universal cover, small lifted punctured normal discs are half-planes. Such a half-plane is a product of two real open intervals; applying [interval-fibre descent](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-interval-fibres--an-open-submersion-calculation) successively to their projections identifies its ordinary derived sections, as a family over \(Y\), with \(A\). Both nearby objects are therefore \(A\).

The ordinary restriction of either original or specialized family is \(A\), and its map to the nearby coefficient is the identity under that descent. Both vanishing objects are zero. Monodromy is the identity because translating the lifted coordinate does not change a normal-constant family. All arguments concern whole bounded complexes and interval descent; they require neither splitting the cohomology sheaves nor finite generation of their modules. This contrasts with the real angular example, where distinct lifted supported components survive.

## What has been established

The regular-fibre weak real comparison is proved with its logarithmic lifted square, actual countable-cover boundary map, punctured normal recovery, ordinary unit, source shifts and monodromy. The global construction uses analytic division by the deformation parameter to glue its local maps. Complex section and microlocal formulas, full cycle constructibility, holomorphic microsupport tests and the quadratic model remain separate targets. The proof requires the small-ball stabilization, weak inverse-image and internal-Hom theorems, smooth base change for submersions, and the ordinary and punctured conic-recovery maps stated in the relevant steps. It does not prove those underlying topology and sheaf-operation results.


## Human sources and proof scope

Ren Fernandes, Kazuki Kudomi and Kiyoshi Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, arXiv:2603.14821v2, §2.4, define specialization on the positive deformation chamber; equation (4.54) identifies it with real nearby cycles for the deformation parameter. Their complex nearby-cycle comparison in §5 uses complex constructibility and cites an additional theorem for its invertibility. These passages provide the stated definitions and classical context, rather than the weak real-coefficient countable-cover proof developed here. The linked programme arguments supply the common small balls, actual product base-change map, punctured recovery and conic contraction used in this lesson. Its logarithmic lift, unit square and signed fibre comparison retain their complete maps and shifts. The exposition and seven solutions are independently written CC0 programme text; mathematical source credit is retained. The further specialization and microlocal results, and a complete audit of every transitive prerequisite, remain separate.
