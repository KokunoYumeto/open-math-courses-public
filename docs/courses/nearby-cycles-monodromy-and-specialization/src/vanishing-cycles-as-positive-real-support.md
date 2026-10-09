# Vanishing cycles as positive real support

For a holomorphic function and a weakly complex constructible sheaf, vanishing cycles can be computed by local cohomology with support in its closed positive real halfspace. The comparison is an actual coefficient-triangle map. Its proof compares the lifted punctured neighborhood with one negative sector, using the local pushforward theorem over a complex curve.

Let \(k\) be a commutative ring of finite global dimension, \(X\) a complex manifold that is Hausdorff and countable at infinity, with a uniform finite dimension bound, and \(f:X\to\mathbb C\) holomorphic. Put

\[
Y=f^{-1}(0),\quad i:Y\hookrightarrow X,\qquad
A=\{x:\operatorname{Re}f(x)<0\},\qquad
H=\{x:\operatorname{Re}f(x)\geq0\}.
\tag{1}
\]

The input \(F\in D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) may have infinite coefficient modules. We will prove a natural isomorphism

\[
i^{-1}R\Gamma_HF\simeq\phi_f(F),
\tag{2}
\]

with the source convention \(\phi_f(F)=\operatorname{Cone}(i^{-1}F\to\psi_f(F))[-1]\). The fibre \(Y\) may be singular and \(df\) may vanish. Properness of \(f\) is not assumed.

The [local complex-curve pushforward theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/local-holomorphic-pushforwards-over-a-complex-curve.md#the-neighborhood-theorem-and-its-cotangent-bound) applies on a ball intersected with a sufficiently small inverse-image target neighborhood. Contractible-fibre descent uses the [whole-complex cylinder theorem SH02-CON-CYLINDER](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter). These inputs retain their analytic, conic, sheaf-operation and boundedness hypotheses.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The normalized negative sector supplies a coefficient map

Use the fixed cover and [coefficient trace from the monodromy lesson](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#the-coefficient-sheaf-uses-a-sum),

\[
p:\mathbb C_w\longrightarrow\mathbb C,
\qquad p(w)=e^{2\pi iw},\qquad
\widetilde U=X\times_{\mathbb C}\mathbb C_w,
\quad q:\widetilde U\longrightarrow X.
\tag{3}
\]

Its image is \(X\setminus Y\). Write \(L_f=q_!k_{\widetilde U}\). The proper-support trace \(\operatorname{tr}:L_f\to k_X\) sums the finitely supported sheet coefficients. It gives the [normalized two-term coefficient complex](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-and-the-two-monodromy-triangles.md#one-two-term-complex-gives-two-triangles)

\[
K_f=[L_f\xrightarrow{\operatorname{tr}}k_X],
\quad\text{in degrees }-1,0,
\qquad
\phi_f(F)=i^{-1}R\mathcal Hom(K_f,F).
\tag{4}
\]

Let \(N=\{\lambda:\operatorname{Re}\lambda<0\}\). It has the normalized argument in \((\pi/2,3\pi/2)\), so the strip

\[
S=\{w:1/4<\operatorname{Re}w<3/4\}
\tag{5}
\]

maps homeomorphically onto \(N\). This fixes the lift of the negative sector, with \(-1\) lifted to \(1/2\), in the cover convention (3). Its pullback to \(X\) is an open subset \(\widetilde A\subset\widetilde U\) mapped homeomorphically by \(q\) onto \(A\).

Extend its constant coefficient by zero into \(\widetilde U\) and apply \(q_!\). The resulting map is

\[
\alpha_f:k_A\longrightarrow L_f,
\qquad \operatorname{tr}\circ\alpha_f:k_A\longrightarrow k_X.
\tag{6}
\]

The composite is the ordinary open-extension inclusion. Let \(C_f=[k_A\to k_X]\), again in degrees \(-1,0\). Open–closed localization gives \(C_f\simeq k_H\), in degree zero. The coefficient morphism

\[
C_f\longrightarrow K_f=(\alpha_f,\mathrm{id})
\tag{7}
\]

induces, by contravariant internal Hom and restriction to \(Y\),

\[
\phi_f(F)\longrightarrow i^{-1}R\Gamma_HF.
\tag{8}
\]

It is a natural map of the two defining fibre triangles. Their middle term is \(i^{-1}F\), with the identity map. On their other terms it is

\[
\beta_F:
\psi_f(F)=i^{-1}Rq_*q^{-1}F
\longrightarrow i^{-1}Rj_*j^{-1}F,
\qquad j:A\hookrightarrow X.
\tag{9}
\]

The cover adjunction and the open-set Hom interpretation identify this map with ordinary restriction from the entire lifted punctured neighborhood to \(\widetilde A\). The trace square in (6) makes it commute with the central unit. Thus proving (9) to be an isomorphism proves (8) to be an isomorphism, whose natural inverse is (2). No additional shift can enter this fibre-triangle comparison.

## Local curve pushforwards give a cofinal family of balls and target discs

Fix \(x\in Y\), choose a relatively compact holomorphic coordinate chart around \(x\), and translate \(x\) to zero. The [centered-ball germ theorem of the complex-curve lesson](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/local-holomorphic-pushforwards-over-a-complex-curve.md#centered-balls-in-the-source-germ) supplies arbitrarily small source radii \(r\) and target neighborhoods \(D\ni0\) for which

\[
V=B_r(x)\cap f^{-1}(D),\qquad
G_V=R(f|_V)_*(F|_V)
\tag{10}
\]

is bounded weakly complex constructible on \(D\). This includes critical functions and arbitrary weak coefficients. The theorem's proof chooses radii below the first positive selected central critical value and a compact cutoff band; it works at arbitrarily small radii. Its [reciprocal exhaustion](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/local-holomorphic-pushforwards-over-a-complex-curve.md#all-closed-levels-after-restricting-the-source) verifies every finite closed-level properness condition. We need the ordinary direct image in (10).

On a complex curve, weak complex constructibility makes the cohomology locally constant away from a locally finite set of points. Shrink \(D\) to a small centered disc so that the only possible exceptional point of \(G_V\) in that disc is zero. Restricting the target disc also restricts \(V\); ordinary open-base restriction commutes with direct image, so (10) and its statement remain valid. We obtain nested cofinal neighborhoods

\[
V_a=B_{r_a}(x)\cap f^{-1}(D_{\delta_a}),
\quad r_a\downarrow0,\quad\delta_a\downarrow0,
\qquad G_a=R(f|_{V_a})_*(F|_{V_a}),
\tag{11}
\]

with \(G_a\) cohomologically locally constant on \(D_{\delta_a}^*\). Choose each next radius and disc inside the previous ones; the curve theorem and open target restriction permit this. The \(V_a\) are open neighborhoods of \(x\), are contained in shrinking coordinate balls, and are therefore cofinal in the ordinary neighborhood system.

It is not required that \(f(B_{r_a})\subset D_{\delta_a}\). The actual domain in (11) is the intersection. The curve theorem applies to this intersection, and these intersections supply the cofinal source neighborhoods used below.

## The actual cover-to-sector restriction is an isomorphism

Let

\[
P_a=\{w:|e^{2\pi iw}|<\delta_a\},
\qquad S_a=P_a\cap S.
\tag{12}
\]

The cover \(P_a\to D_{\delta_a}^*\) is a local homeomorphism, \(P_a\) is an open halfplane, and \(S_a\) is an open half-strip. Each is diffeomorphic to \(\mathbb R^2\). The latter maps homeomorphically onto \(D_{\delta_a}\cap N\).

Ordinary base change along a local homeomorphism is valid for any map in the other direction. To check its actual morphism, restrict to an evenly covered target open set and one sheet, where the base map is a homeomorphism. The two preimages and their restriction maps identify, so open-base restriction of derived direct image gives the isomorphism there. These local identifications prove the global base-change morphism; they use no properness assertion.

Apply this to \(f|_{V_a}\) over the punctured disc. Direct-image composition and open restriction give natural identifications

\[
\begin{aligned}
R\Gamma(q^{-1}V_a;q^{-1}F)
&\simeq R\Gamma(P_a;p^{-1}(G_a|_{D_{\delta_a}^*})),\\
R\Gamma(V_a\cap A;F)
&\simeq R\Gamma(S_a;p^{-1}(G_a|_{D_{\delta_a}^*})|_{S_a}).
\end{aligned}
\tag{13}
\]

The identifications carry the restriction in (9) to restriction from \(P_a\) to \(S_a\), by their open-set and base-change naturality.

The coefficient \(p^{-1}(G_a|_{D_{\delta_a}^*})\) has locally constant cohomology on the simply connected \(P_a\). Choose any \(w_a\in S_a\). The [whole-complex cylinder descent theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter), iterated on two real coordinates after product identifications of \(P_a,S_a\), gives isomorphisms from both section complexes to evaluation at \(w_a\). They commute with the actual restriction map. Consequently

\[
R\Gamma(q^{-1}V_a;q^{-1}F)
\longrightarrow R\Gamma(V_a\cap A;F)
\quad\text{is an isomorphism.}
\tag{14}
\]

This uses the whole bounded complex, not only its separate cohomology modules, and does not impose finite generation. Nontrivial monodromy on the punctured target disc remains allowed; both evaluation arguments take place on the contractible cover and its selected strip.

Take the filtered stalk system over the cofinal \(V_a\). The two systems in (14) compute the stalks of \(Rq_*q^{-1}F\) and \(Rj_*j^{-1}F\) at \(x\). Their maps are the restrictions induced by the globally defined coefficient branch (6), so they commute with all smaller-neighborhood restriction maps. Exact filtered colimits on cohomology show that \((\beta_F)_x\) is an isomorphism. Since this holds at every \(x\in Y\), (9) is an isomorphism on \(Y\). The fibre-triangle map (8) is then an isomorphism, proving (2).

The auxiliary coordinate balls, discs and evaluation points prove that a previously defined natural map is invertible. They are not part of its definition. The branch normalization is part of the fixed covering convention: translating the strip by an integer gives the corresponding deck-translated comparison. With (3)–(5) fixed, (2) is natural in \(F\).

## Endpoints, coefficients and critical functions

The support in (2) is the closed halfspace, with \(\operatorname{Re}f=0\) included. Its complementary sector is the strictly negative halfplane. It is local cohomology \(R\mathcal Hom(k_H,F)\), not ordinary restriction of \(F\) to \(H\) extended by zero, and not compactly supported cohomology of \(H\).

If \(F\) has perfect stalks, its cycles are perfect complex constructible by the [normal/conormal section theorem and its critical-function graph comparison](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/complex-nearby-cycles-as-normal-and-conormal-sections.md#constructibility-and-support-for-a-critical-function). The comparison therefore also proves that the restricted support object in (2) has perfect stalks. The proof of invertibility itself retains arbitrary weak coefficients throughout. For \(f=0\), the two negative-sector and punctured-cover objects are zero, so the comparison is the identity on \(F\). No regular-fibre hypothesis was used.

## Exercises with complete solutions

### The ball must be read over a smaller target germ

*Difficulty: Intermediate.*

For \(f(z_1,z_2)=z_1\) and \(F=k_{\{z_2=z_1\}}\), compute the image of the support inside a ball of radius \(r\). Explain why the proof uses \(B_r\cap f^{-1}(D_\delta)\), and why neighborhoods of this form with \(r\to0\) are cofinal at zero.

**Solution.** On the support, the squared norm is \(2|z_1|^2\), so the support in the open ball maps to \(D_{r/\sqrt2}\). The entire ball maps to \(D_r\). Ordinary pushforward of the support's open disc, viewed on a target containing \(D_r\), acquires a real circle boundary at radius \(r/\sqrt2\); it is not weakly complex constructible across that boundary. On a smaller disc \(D_\delta\) with \(\delta<r/\sqrt2\), the source intersection's support instead projects homeomorphically onto all of that target disc, with constant coefficient. There is no need to include the whole ball in its target inverse image. Each \(B_r\cap f^{-1}(D_\delta)\) contains zero, is open, and is contained in \(B_r\); shrinking radii makes such neighborhoods cofinal regardless of the relative rate of shrinking \(\delta\).

### A nontrivial local system still restricts from cover to sector

*Difficulty: Intermediate.*

Let \(k=\mathbb Q\), \(j_0:\mathbb C^*\hookrightarrow\mathbb C\), and \(F=j_{0!}\mathcal L\), where the rank-one local system has deck monodromy \(2\). For \(f(z)=z\), compute the restricted closed-halfspace support object at zero. Identify it with the vanishing object and explain the role of the negative-sector branch.

**Solution.** The central stalk of \(F\) is zero. Its ordinary cohomology on a small negative half-disc is \(\mathbb Q\) in degree zero, since the sector is contractible and \(\mathcal L\) restricts to a constant local system there. The support triangle gives \((R\Gamma_{\{\operatorname{Re}z\geq0\}}F)_0=\mathbb Q[-1]\). Cover descent gives nearby \(\mathbb Q\) with deck automorphism \(2\), and the source-normalized vanishing object is the same \(\mathbb Q[-1]\). The strip \(1/4<\operatorname{Re}w<3/4\) identifies the actual restriction map with the sector evaluation. Translating it by an integer applies deck transport to that identification; it does not make the local system's monodromy trivial.

### Ramification produces several negative sectors

*Difficulty: Intermediate.*

Take \(f(z)=z^m\), \(m\geq1\), and the constant complex \(M_{\mathbb C}\) for arbitrary bounded \(M\). Compute the negative-sector extension stalk and the positive-real-support object at zero. Check the cycle comparison even when the coefficient ring has characteristic dividing \(m\).

**Solution.** The set \(\operatorname{Re}z^m<0\) has \(m\) open sectors in a small punctured disc. Each is contractible, so the extension stalk is \(M^m\), and the unit \(M\to M^m\) is diagonal. The diagonal has a splitting given by projection to its first component, and its quotient complex is \(M^{m-1}\), for instance through the differences from that component. Thus the support fibre is \(M^{m-1}[-1]\). The nearby cover also has \(m\) components, the same diagonal unit, and cyclic deck permutation; its vanishing object agrees. No division by \(m\) is used. The comparison therefore remains valid in every characteristic and for nonperfect \(M\). For \(m=1\) both vanish.

### The real quadratic support has the complex dimension degree

*Difficulty: Intermediate.*

Let \(M\in D^b(k)\) and \(F=M_{\mathbb C^d}\). For \(Q(z)=\sum_{j=1}^d z_j^2\), write the negative real-part region in real coordinates and compute its augmented cochains near zero. Recover the degree of the quadratic vanishing object, including \(d=0\).

**Solution.** With \(z=x+iy\), the negative region is \(|x|^2<|y|^2\). In a punctured small ball, sending \(x\) to zero preserves the inequality and reduces the norm. The remaining nonzero \(y\) ball retracts onto \(S^{d-1}\); the radial retraction can be chosen on a fixed smaller radius, and its cohomology maps agree as neighborhoods shrink. The [constant-coefficient homotopy comparison](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/quadratic-cycles-and-the-holomorphic-microsupport-test.md#the-covered-quadratic-ball-retracts-to-a-sphere) identifies the central unit with the constant-cochain map \(M\to R\Gamma(S^{d-1};M)\). The [relative-ball and augmented-sphere calculation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/quadratic-cycles-and-the-holomorphic-microsupport-test.md#the-reduced-cochains-fix-the-degree-and-monodromy) gives its cone as \(M[1-d]\), and the support triangle's \([-1]\) gives \(M[-d]\), agreeing with the full covered quadratic calculation. For \(d=0\) the negative set is empty, so the support object is \(M\) directly. The real ambient dimension \(2d\) does not replace the negative-direction count \(d\).

### Central support and infinite normal constants

*Difficulty: Intermediate.*

Check (2) for \(f=0\), for a sheaf complex supported on \(Y\), and for \(f(v,y)=v\) with \(F\) the normal-constant family of \(\bigoplus_{r\geq1}\mathbb Q\) over \(\mathbb Q\). Explain the closed endpoint.

**Solution.** If \(f=0\), then \(H=X\), the punctured and negative sets are empty, and both sides of (2) are \(F\). If \(F\) is supported on \(Y\), its restriction to \(A\) and to the cover is zero, so again the support and vanishing objects are \(i^{-1}F\), in their original degrees. Removing the boundary from \(H\) would give zero for the support Hom to such a central complex, since the open coefficient has zero stalk along \(Y\). For the normal-constant infinite family, both the cover and the negative half-disc have whole derived evaluation equal to the infinite module, and the central unit is the identity. Both fibre terms vanish. The argument retains the infinite coefficient, with no perfectness claim.

### Weak real constructibility does not suffice

*Difficulty: Advanced.*

Over a field, let \(F=k_{[0,\infty)}\) on \(\mathbb C\), the closed positive real ray, and let \(f(z)=z\). Compare its positive-real-support stalk at zero with its source-normalized vanishing object. Locate the hypothesis that fails in the proof.

**Solution.** The support of \(F\) is contained in \(\{\operatorname{Re}z\geq0\}\), so local cohomology with that closed support is \(F\), with stalk \(k\) at zero. Its [lifted punctured-ray calculation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/nearby-cycles-monodromy-and-specialization/src/nearby-cycles-through-the-normal-deformation.md#a-real-angular-sheaf-produces-infinitely-many-nearby-coefficients) has countably many components. A small lifted punctured neighborhood has ordinary section complex \(P=\prod_{n\in\mathbb Z}k\) in degree zero. The central unit is the diagonal \(k\to P\), and the vanishing object is \((P/k\mathbf1)[-1]\), which is nonzero in degree one. It cannot be isomorphic to the support stalk \(k\) in degree zero. The sheaf is weakly real constructible but not weakly complex constructible. Its curve pushforward for the identity function still has a real ray stratum in every punctured disc, so the cohomological local constancy required in (11) fails. Correspondingly, restriction from the cover to the negative sector is \(P\to0\), not an isomorphism.

## Scope of the result

The normalized branch makes the comparison compatible with the central unit; its map of fibre triangles identifies positive real support with the chosen vanishing-cycle normalization. The proof permits all bounded weakly complex constructible coefficients, critical functions and singular zero fibres. The last example shows exactly where complex constructibility is needed.

## References

David B. Massey, *Notes on Perverse Sheaves and Vanishing Cycles*, [arXiv:math/9908107v13, §3, pp. 28–29, the nonnegative-real-part support comparison](https://arxiv.org/pdf/math/9908107v13#page=28), credits the construction to Kashiwara and Schapira and states its agreement with his shifted vanishing object. His shifted object agrees with the convention used here. This is a source for the comparison and its historical attribution; its constructible coefficient scope and brief cone description do not supply the full weak-coefficient argument.

The proof above identifies a particular map by fixing a covering strip, follows the unit into the closed-support triangle, and establishes cofinal shrinking neighborhoods before applying complex-curve and cylinder results. These are the steps needed for the stronger formulation, including arbitrary bounded coefficients and critical functions. The linked programme proofs supply the centered-ball curve theorem, full-complex descent and coefficient-triangle inputs. The source and proof guide records them separately from the checked source passage.
