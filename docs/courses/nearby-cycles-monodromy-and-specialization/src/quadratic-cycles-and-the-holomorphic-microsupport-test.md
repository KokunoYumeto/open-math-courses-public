# Quadratic cycles and the holomorphic microsupport test

Holomorphic tests detect every direction in the microsupport of a weakly complex constructible sheaf. The forward direction follows from the vanishing support bound. To prove the reverse direction, we compute a quadratic test on a generic conormal model and show that the test depends only on its microlocal class. Both the dimension of the model and the source's vanishing-cycle shift matter.

Throughout, \(k\) is commutative of finite global dimension, and complex manifolds are Hausdorff and countable at infinity. Coefficient complexes belong to \(D^b(k)\); they need not be perfect or have finite cohomology modules. We use the cycle convention

\[
\phi_f(F)=\operatorname{Cone}\bigl(i^{-1}F\longrightarrow\psi_f(F)\bigr)[-1],
\tag{1}
\]

where \(i:f^{-1}(0)\hookrightarrow X\). The comparison with a conormal section, and its exact Fourier and closed-ray normalization, were proved in Complex nearby cycles as normal and conormal sections.

We prove the quadratic calculation directly, including its unit map and deck action. The generic coefficient object model is the theorem `SH02-LFI-SUPPORTED`. The quotient/null criterion and arbitrary bounded microlocal support estimate are `SH02-MC-LOCAL` and `SH02-MO-MICROLOCAL-SUPPORT`. Their precise hypotheses are retained in the applications below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The covered quadratic ball retracts to a sphere

Put \(Q(z)=\sum_{j=1}^d z_j^2\) on \(\mathbb C^d\), with \(d\geq1\), and let \(M_{\mathbb C^d}\) be the constant complex with value \(M\). Only zero can support its vanishing cycles: outside zero the differential \(dQ\) is nonzero, while the constant complex has microsupport contained in the zero section. The support bound of the preceding lesson applies.

We compute the central stalk using the ordinary cover in the nearby definition. Above \(Q(z)\ne0\), write the target parameter as \(\lambda=e^{2\pi iw}\). The covered open ball of radius \(\epsilon\) is

\[
\mathcal B_\epsilon=
\{(z,w):Q(z)=e^{2\pi iw},\ |z|<\epsilon\}.
\tag{2}
\]

For \(w\) fixed, write \(\lambda=r e^{i\theta}\) using the lifted argument \(\theta=2\pi\operatorname{Re}w\), and rotate

\[
e^{-i\theta/2}z=x+iy,\qquad x,y\in\mathbb R^d.
\tag{3}
\]

The equations in (2) become

\[
|x|^2-|y|^2=r,\qquad x\cdot y=0,
\qquad r+2|y|^2<\epsilon^2.
\tag{4}
\]

Thus \(0<r<\epsilon^2\), and

\[
u=\frac{x}{\sqrt{r+|y|^2}}\in S^{d-1},\qquad
y\in u^\perp,\qquad
|y|<\sqrt{(\epsilon^2-r)/2}.
\tag{5}
\]

These formulas give a homeomorphism of \(\mathcal B_\epsilon\) with an open tangent-disc bundle over

\[
A_\epsilon\times S^{d-1},\qquad
A_\epsilon=\{w\in\mathbb C:|e^{2\pi iw}|<\epsilon^2\}.
\tag{6}
\]

The base \(A_\epsilon\) is an open halfplane. The disc radius in (5) is strictly positive on it. Sending \(y\) to \(t y\), \(0\leq t\leq1\), and replacing \(x\) by \(\sqrt{r+t^2|y|^2}\,u\), is a deformation retraction to the zero-disc section. It preserves (4), stays in the ball, and fixes \(w,u\). Consequently \(\mathcal B_\epsilon\) retracts to \(A_\epsilon\times S^{d-1}\).

The pullback coefficient in the nearby definition is the constant complex \(M\). Its ordinary sheaf cohomology on these locally contractible spaces is computed by constant-coefficient cochains. We use the usual sheaf/singular comparison and homotopy invariance for constant coefficients, with the bounded-complex extension supplied by its cohomology spectral sequence. These are explicit topological prerequisites. Only the finite free cochain complex of the sphere is required in the resulting coefficient calculation, so no finite-module or infinite-product Künneth assumption appears.

For \(0<\delta<\epsilon\), the inclusion \(\mathcal B_\delta\hookrightarrow\mathcal B_\epsilon\) is, in (5), the identity on \(u\), an inclusion of halfplanes, and an inclusion of the smaller tangent discs. Both retractions commute with this inclusion at the zero-disc section. Restriction therefore induces the identity on the sphere cochain model after the contractible halfplanes are removed. These are the actual maps entering the stalk colimit. It follows that

\[
\psi_Q(M_{\mathbb C^d})_0
\simeq R\Gamma(S^{d-1};M),
\tag{7}
\]

and the central unit \(M\to\psi_Q(M)_0\) is the constant-cochain map. This identifies the map as well as the object. The stalk of an ordinary derived direct image is computed by this filtered system of open balls; exact filtered colimits of coefficient modules preserve the cohomology isomorphisms just exhibited.

## The reduced cochains fix the degree and monodromy

For \(d\geq2\), orient \(\mathbb R^d\) in the displayed coordinate order and give its unit sphere the boundary orientation. Its reduced cochain complex is \(k[1-d]\), using the finite cellular computation of a sphere. For \(d=1\), the sphere has two points; the constant-cochain map is the diagonal \(k\to k^2\), and its quotient is \(k=k[1-d]\). In both cases, with arbitrary bounded \(M\), the augmented finite free cochain model gives

\[
\operatorname{Cone}\bigl(M\longrightarrow R\Gamma(S^{d-1};M)\bigr)
\simeq M[1-d].
\tag{8}
\]

Tensoring a finite free model with \(M\) is a derived tensor calculation with no perfection requirement on \(M\). Formula (1) supplies the remaining shift. With \(b:\{0\}\hookrightarrow Q^{-1}(0)\), localization for the support already determined therefore proves

\[
\phi_Q(M_{\mathbb C^d})\simeq b_*M[-d].
\tag{9}
\]

For \(d=0\), the domain is a point and \(Q=0\). The punctured inverse image is empty, so \(\psi_Q=0\) and \(\phi_Q=M\). This agrees with (9) at \(d=0\), without inventing a negative-dimensional sphere.

The cover deck translation \(w\mapsto w+1\) changes the lifted half-angle in (3) by \(\pi\). It acts on the retracted real sphere by \(u\mapsto-u\). The antipodal map has degree \((-1)^d\) on \(S^{d-1}\); this follows by extending it to the linear map \(-\mathrm{id}\) of \(\mathbb R^d\), whose determinant is \((-1)^d\), and using boundary orientation. On the reduced complex in (8), and hence on \(M[-d]\), deck monodromy is

\[
M_Q=(-1)^d\,\mathrm{id}.
\tag{10}
\]

For \(d=1\), swapping the two points negates their diagonal quotient, giving the same sign directly. For \(d=0\) the empty-nearby coefficient construction gives identity on the central vanishing complex, consistent with (10). The degree convention in (9) is the source convention, rather than the unshifted reduced cohomology degree in (8).

## A conormal test descends through arbitrary denominator cones

Let \(h\) be holomorphic near \(x\), with \(h(x)=0\) and \(dh_x\ne0\). After shrinking, \(T=h^{-1}(0)\) is a smooth hypersurface. Put \(p=(x;dh_x)\). The exact functor

\[
\mathcal T_h:D^b(k_X)\longrightarrow D^b(k),
\qquad A\longmapsto(\mu_TA)_p
\tag{11}
\]

is defined on all bounded sheaf complexes on this neighborhood. If \(p\notin\operatorname{SS}(A)\), the arbitrary bounded support contract MO15 makes \(\mathcal T_h(A)=0\). Hence, for any morphism whose cone has microsupport avoiding \(p\), exactness makes its image under \(\mathcal T_h\) an isomorphism.

The quotient contract `SH02-MC-LOCAL` identifies precisely these cones as the null subcategory in \(D^b(k_X;p)\). Its quotient property therefore makes (11) descend to that category. In particular,

\[
A\simeq B\text{ in }D^b(k_X;p)
\quad\Longrightarrow\quad
\mathcal T_h(A)\simeq\mathcal T_h(B).
\tag{12}
\]

This implication can also be read directly through denominator fractions: every denominator is sent to an isomorphism, so a representative fraction induces an isomorphism of the test objects. Its cone need not be weakly complex constructible.

For weakly complex constructible \(A\), the conormal section comparison from the preceding lesson identifies

\[
\mathcal T_h(A)\simeq\phi_h(A)_x.
\tag{13}
\]

We use (13) only on the two weakly complex constructible endpoints of (12). We do not claim that holomorphic vanishing cycles of an arbitrary intermediate roof object satisfy that comparison. The proof requires the generic coefficient *object* model, not full faithfulness of all coefficient morphisms.

## Generic analytic conormals give nonzero quadratic tests

For weakly complex constructible \(F\) on a complex \(n\)-manifold, its actual microsupport \(\Lambda\) is a closed complex analytic Lagrangian cone by the complex criterion and singular involutivity developed earlier. Its nonempty components have complex dimension \(n\). On a dense open subset, each point is regular, lies on only one local component, and the projection \(\pi:\Lambda\to X\) has locally constant rank. This follows from analytic regular density, local finiteness of components, and the holomorphic minor description of the lower-rank locus.

At such a point \(p\), the constant-rank theorem supplies a local complex image submanifold \(Y\subset X\). Canonical-form vanishing gives \(\xi|_{T_yY}=0\) at points \((y;\xi)\) of the selected component: every vector of \(T_yY\) lifts to a tangent vector of that component. Thus its germ lies in \(T_Y^*X\). Both smooth manifolds have complex dimension \(n\), so the inclusion is open near \(p\) and their germs agree. Removing other components ensures

\[
\operatorname{SS}(F)\subset T_Y^*X\quad\text{near }p.
\tag{14}
\]

The current bounded object-model contract LFI9–LFI10 now gives

\[
F\simeq M_Y\quad\text{in }D^b(k_X;p)
\tag{15}
\]

for some bounded \(k\)-complex \(M\), where \(M_Y\) means the local constant complex on \(Y\), extended by zero. This is a local statement; it does not make \(F\) globally constant on \(Y\).

Suppose \(p\ne0\), translate its base to zero, and choose adapted holomorphic coordinates with

\[
Y=\{z_1=\cdots=z_c=0\},\qquad
p=(0;dz_1),\qquad c\geq1.
\tag{16}
\]

The nonzero normal covector can be made the first coordinate differential by an invertible complex change of normal coordinates. Use

\[
h(z)=z_1+\sum_{j=c+1}^{n}z_j^2,
\qquad dh_0=dz_1.
\tag{17}
\]

This is regular on \(X\), whereas its restriction to \(Y\) is the standard quadratic on \(d=n-c\) variables. The proper closed-embedding cycle comparison, applied to \(Y\hookrightarrow X\), and (9) give

\[
\phi_h(M_Y)_0\simeq M[-(n-c)]=M[c-n].
\tag{18}
\]

When \(c=n\), the restriction is zero on the point \(Y\); the separate dimension-zero calculation gives \(M\), in degree zero, exactly as (18) says. By (12)–(13),

\[
\phi_h(F)_0\simeq M[c-n].
\tag{19}
\]

No finite-rank or perfectness assumption enters this detection. If the test is zero, the invertibility of a cohomological shift gives \(M=0\). Formula (15) then makes \(F\) zero in \(D^b(k_X;p)\). The quotient/null criterion MC.2 implies \(p\notin\operatorname{SS}(F)\).

The model degree depends on the complex dimension \(n-c\) of \(Y\). The quadratic calculation and proper cycle comparison give \(M[c-n]\), including the dimension-zero calibration above. The criterion needs detection of a nonzero coefficient complex, and (18) supplies it in every codimension.

## The uniform holomorphic criterion

**Theorem.** For \(F\in D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) and \(p\in T^*X\), the following are equivalent:

1. \(p\notin\operatorname{SS}(F)\).
2. There is an open cotangent neighborhood \(V\) of \(p\) such that every local holomorphic \(h\), defined near any \(x\), with \(h(x)=0\) and \((x;dh_x)\in V\), satisfies \(\phi_h(F)_x=0\).

The forward implication was proved using the closed support bound in the preceding lesson. For the reverse implication, retain the neighborhood \(V\) in condition 2. First let

\[
B=\{x\in X:(x;0)\in V\}.
\tag{20}
\]

This is open. The test \(h=0\) at each \(x\in B\) has empty nearby inverse image and \(\phi_0(F)_x=F_x\). Condition 2 gives \(F|_B=0\), so no microsupport lies over \(B\). In particular there are no zero covectors in \(\Lambda\cap V\).

If \(\Lambda\cap V\) were nonempty, it would be a relatively open subset of the analytic Lagrangian set \(\Lambda\), and would meet the dense generic set used for (14). Choose such a point \(p'\in\Lambda\cap V\). It is nonzero by the preceding paragraph. The test (17), with \(dh_0=p'\), belongs to the required family. Its vanishing stalk is zero by condition 2. Formula (19) gives \(M=0\), and the null criterion gives \(p'\notin\Lambda\), a contradiction. Hence \(\Lambda\cap V=\varnothing\), and in particular \(p\notin\Lambda\).

The use of a dense generic set requires the whole open cotangent neighborhood in the theorem. Vanishing of one test at one covector would not supply the contradiction at a nearby generic point. Closed microsupport and analytic generic density ensure that every nonempty relatively open part is tested, including neighborhoods of singular points of \(\Lambda\).

## Exercises with complete solutions

### Real coordinates of a complex quadratic fibre

*Difficulty: Introductory.*

For \(Q\) in dimension \(d\geq1\) and a positive real value \(r\), derive (4)–(5). Construct the deformation retraction explicitly, and explain the dimension-one case.

**Solution.** Expanding \(Q(x+iy)\) gives \(|x|^2-|y|^2+2i x\cdot y\). Setting it equal to \(r\) gives \(|x|^2=r+|y|^2\) and \(x\cdot y=0\), so \(u=x/\sqrt{r+|y|^2}\) is a unit vector and \(y\in u^\perp\). The ball condition is \(r+2|y|^2<\epsilon^2\). The path \(y_t=t y\), \(x_t=\sqrt{r+t^2|y|^2}\,u\), preserves these equations and reduces the norm. At \(t=0\) it gives \(\sqrt r\,u\) and fixes the zero-disc section. In dimension one, \(u\) has the two values \(\pm1\), and its orthogonal complement is zero; the fibre is precisely two points. No positive-dimensional tangent disc is present.

### Coefficient degrees in dimensions zero through three

*Difficulty: Intermediate.*

For any bounded \(M\), list the central nearby unit and vanishing complex for \(d=0,1,2,3\). Locate the two shifts that produce the degree in (9).

**Solution.** At \(d=0\), the nearby complex is zero and \(\phi=M\). At \(d=1\), it is \(M^2\) with diagonal unit, and \(\phi=M[-1]\). At \(d=2\), sphere cochains have \(M\) in degree zero and \(M[-1]\) in the reduced summand; the unit is the constant summand, and \(\phi=M[-2]\). At \(d=3\), the reduced summand is \(M[-2]\), giving \(\phi=M[-3]\). The sphere's reduced cochain complex contributes \([1-d]\); the definition of \(\phi\) contributes \([-1]\). The first step is finite free and works for arbitrary modules in \(M\). Choosing a sphere basepoint splits the constant summand when needed; the calculation of its cone does not require a canonical global splitting.

### Odd-dimensional sign in characteristic two

*Difficulty: Intermediate.*

Compute the vanishing monodromy for \(d=1,2,3\) over \(\mathbb Z\), and then over \(\mathbb F_2\). Does trivial monodromy imply a zero vanishing object?

**Solution.** Over \(\mathbb Z\), the signs are respectively \(-1,+1,-1\), by the antipodal degrees in (10). Over \(\mathbb F_2\) all three signs become \(+1\). The vanishing objects are still \(M[-1],M[-2],M[-3]\). With \(M=\mathbb F_2\) each is nonzero. Even over \(\mathbb Z\), dimension two gives nonzero vanishing with identity monodromy. Thus identity monodromy does not detect the zero object. The source-normalized shift remains the same in either characteristic.

### Infinite coefficients pass the same quadratic test

*Difficulty: Intermediate.*

Use \(k=\mathbb Q\), \(M=\bigoplus_{r\geq1}\mathbb Q\), and \(d=2\). Compute the vanishing object and explain precisely why the argument did not require a finite-dimensional Künneth theorem.

**Solution.** The result is \(M[-2]\) at zero and zero elsewhere on \(Q^{-1}(0)\). The covered ball retracts to a contractible halfplane times \(S^1\). Constant-coefficient sphere cochains are represented by a finite free cellular complex, and its augmented reduced part is \(k[-1]\). Tensoring that finite free model with the arbitrary module \(M\), then applying the defining \([-1]\), gives \(M[-2]\). No infinite tensor/product interchange occurs. Its nonzero stalk is not perfect over \(\mathbb Q\), but it is weakly complex constructible, which is the theorem's coefficient scope.

### Denominator cones need not be complex constructible

*Difficulty: Advanced.*

Suppose \(A\simeq B\) in \(D^b(k_X;p)\), with \(A,B\) weakly complex constructible, and \(p=(x;dh_x)\ne0\) for a regular holomorphic \(h\). Prove that their \(\phi_h\) stalks agree without imposing constructibility on any cone in a fraction representing the isomorphism.

**Solution.** Every denominator has a cone \(C\) with \(p\notin\operatorname{SS}(C)\). The arbitrary bounded support estimate for \(\mu_T C\), \(T=h^{-1}(0)\), makes its stalk at \(p\) zero. The exact functor \(A\mapsto(\mu_TA)_p\) therefore sends every denominator to an isomorphism. It induces a functor on the quotient, so the localized isomorphism gives equal test objects. The conormal section comparison identifies those two endpoint test objects with \(\phi_h(A)_x\) and \(\phi_h(B)_x\). That identification is used on the two constructible endpoints only. No hypothesis or cycle comparison for the intermediate cones was needed.

### Codimension changes the model's cycle degree

*Difficulty: Advanced.*

In \(X=\mathbb C^4\), take \(Y=\{z_1=z_2=0\}\), \(F=M_Y\), and \(h=z_1+z_3^2+z_4^2\). Compute \(\phi_h(F)_0\). Repeat for \(Y=\{0\}\subset\mathbb C^2\) and \(h=z_1\). Compare with a degree depending only on the ambient dimension.

**Solution.** The closed embedding is proper, and \(h|_Y\) is a quadratic on two complex variables. Its cycles therefore give \(M[-2]\), with identity monodromy, at the origin. The formula \(M[c-n]\) has \(c=2,n=4\), agreeing. In the second example, the restriction to the point is zero; its nearby object is zero and its vanishing object is \(M\) in its original degrees. Here \(c=n=2\). A proposed \(M[1-n]=M[-1]\) would put a degree-zero nonzero coefficient in degree one, contradicting the defining triangle. This hypothetical dimension-only formula fails that calibration; the detection required by the criterion uses the proved codimension-dependent degree.

### Why an open family is stronger than one test

*Difficulty: Advanced.*

Assume \(1_k\ne0\). For \(F=k_X\), compare a regular holomorphic test at a point with the zero-function test. Then explain where the full open cotangent family enters the reverse proof for arbitrary weakly complex constructible \(F\).

**Solution.** A regular test has nonzero derivative outside the constant sheaf's zero-section microsupport, so its vanishing stalk is zero. This single vanishing test does not imply that \(F\) is zero nearby or that its zero covectors are absent. The test \(h=0\) has \(\phi_0(F)=F\), so every neighborhood of a zero covector contains a nonzero vanishing test. In the reverse proof, the constant test first excludes all zero covectors in the chosen neighborhood. If microsupport still meets that neighborhood, relative openness and generic density produce a nonzero generic conormal point inside it. The adapted quadratic test has exactly that point as its derivative and must vanish by the whole-family hypothesis. Its coefficient detection contradicts membership in microsupport. The proof cannot replace this open-family condition by a single prescribed test at an arbitrary singular covector.

## Scope of the proof

The quadratic calculation fixes the coefficient degree and deck action. The generic conormal model, arbitrary-cone microlocal transfer and zero-function test then prove both directions of the uniform holomorphic criterion under the named prerequisite theorems. Vanishing cycles as positive real support supplies a complementary support calculation and explains why weak real constructibility alone does not suffice.

## References

Masaki Kashiwara, *Index theorem for constructible sheaves*, [Astérisque 130 (1985), pp. 193–209, Lemma 5.2 on p. 201](https://www.numdam.org/item/AST_1985__130__193_0/), states the local closed-support degree for a nondegenerate real quadratic with vector-space coefficients. Fernandes, Kudomi and Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, [arXiv:2603.14821v2, proof of Theorem 5.5, (5.13)–(5.17)](https://arxiv.org/abs/2603.14821v2), uses the complex dimension of the stratum in the quadratic degree. That proof imports its generic microlocal coefficient model; it does not prove the broader object-model prerequisite used here.

Our calculation (2)–(10) uses an explicit covered ball, compatible retractions, finite free reduced sphere cochains and the deck action. It establishes the arbitrary-module degree and monodromy relative to the stated sheaf/cochain comparison. The subsequent criterion additionally requires the arbitrary-cone support estimate, microlocal quotient property, analytic generic conormal geometry and coefficient model specified in (11)–(19). Those prerequisites cannot be inferred from either reference. See the source and proof guide for their separation from the quadratic calculation.
