# Transverse restrictions of microlocal coefficients

Let a complex submanifold meet every stratum transversely. Restricting a sheaf to it lowers both perverse degree thresholds by the complex codimension. Exceptional restriction raises them by that codimension. We first calculate these two bounds from stratum restrictions and orientations. We then recover the same shifts from microlocal coefficient complexes, proving why a model at one cotangent direction describes the actual restriction.

*Written by GPT-6.1 Sol (OpenAI), Ultra; revised by GPT-6 Astra (OpenAI), Ultra, 6 October 2026. Self-checked by the writing AI. Original programme text is public domain (CC0).*

Learn first [Unshared conormal directions and dimension filtrations](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/unshared-conormal-directions-and-dimension-filtrations.md#a-covector-that-belongs-only-to-one-stratum), [Complex microlocal stratifications and constructibility](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#the-closed-analytic-total-conormal), Microlocal types and Stein cohomology, and [Complex middle perversity and exterior products](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-middle-perversity-and-exterior-products.md#the-even-values-determine-the-complex-cuts). Two further arguments identify the functors used below: the full-fibre comparison for localized inverse images and [the canonical noncharacteristic inverse-image theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-pullback--the-general-noncharacteristic-inverse-image). The first requires control of the entire incidence fibre when it compares a localized object with the ordinary restriction. The second identifies an actual natural morphism and its relative orientation factor. The examples below show why both distinctions matter.

Let \(k\) be commutative of finite global dimension. Let \(X\) be a complex \(n\)-manifold and \(i:Y\hookrightarrow X\) a locally closed complex submanifold of codimension \(c\), so \(m=\dim_{\mathbb C}Y=n-c\). Manifolds are Hausdorff and countable at infinity. Let \(F\in D^b_{\mathrm w\mathbb C\mathrm c}(X;k)\). Coefficients may be arbitrary modules. Fix a locally finite complex μ-stratification \(\mathcal S=(S_\alpha)\) with

\[
\Lambda=\operatorname{SS}(F)\subset
\Gamma=\bigcup_\alpha T^*_{S_\alpha}X,
\qquad
T_yY+T_yS_\alpha=T_yX
\quad(y\in Y\cap S_\alpha).
\tag{1}
\]

The μ-condition includes its approaching-stratum direction. Analytic regularity, subanalytic set calculus and the constant-rank theorem enter through the linked geometry lessons. The dimension and lifting arguments needed for this transverse section are proved below. This theorem retains its μ-stratification hypothesis; a result formulated for an arbitrary adapted analytic partition would require an additional argument.

## The conormal map is a fibrewise isomorphism

Put \(T_\alpha=Y\cap S_\alpha\), omitting empty intersections, and \(d_\alpha=\dim_{\mathbb C}S_\alpha\). Transversality gives a smooth complex intersection of dimension \(d_\alpha-c\). At \(y\in T_\alpha\), restriction of covectors is an isomorphism

\[
A_y:T^*_{y,S_\alpha}X
\longrightarrow T^*_{y,T_\alpha}Y,
\qquad \xi\longmapsto \xi|_{T_yY}.
\tag{2}
\]

Indeed a covector in its kernel annihilates both \(T_yS_\alpha\) and \(T_yY\), hence all \(T_yX\). The two spaces have the same complex dimension \(n-d_\alpha\), so injection implies surjection. The tangent equality used for the target is \(T_yT_\alpha=T_yY\cap T_yS_\alpha\), supplied by the transverse inverse-image theorem. These isomorphisms vary analytically on each \(T_\alpha\).

In particular \(i\) is noncharacteristic for the whole closed conic set \(\Gamma\), not merely for \(\Lambda\). A nonzero conormal to \(Y\) cannot belong to \(T^*_{S_\alpha}X\) at a point of \(T_\alpha\). The earlier μ-stratification proof establishes that \(\Gamma\) is closed and that every conormal limit above a point of \(S_\alpha\) remains in \(T^*_{S_\alpha}X\). Thus, for every \(y\in T_\alpha\),

\[
\Gamma_y=T^*_{y,S_\alpha}X.
\tag{3}
\]

This equality includes zero covectors and approaching conormal pieces.

## Bounded outputs have bounded lifts

Write \(E=Y\times_XT^*X\), with \(i_\pi:E\to T^*X\) and \(i_d:E\to T^*Y\). Locally over a relatively compact base neighborhood in \(Y\), there is a constant \(C\) such that

\[
|\xi|\le C|A_y\xi|
\quad\text{for }(y;\xi)\in i_\pi^{-1}\Gamma.
\tag{4}
\]

**Proof.** Otherwise choose lifts with \(|\xi_j|>j|A_{y_j}\xi_j|\) and basepoints in a fixed compact neighborhood. Normalize \(\xi_j\) to length one; conicity retains membership. A subsequence has a base and covector limit \((y;\xi)\) in the closed set \(i_\pi^{-1}\Gamma\), with \(|\xi|=1\) and \(A_y\xi=0\). This contradicts noncharacteristicity. Coordinate norms are sufficient; shrinking to a compact base chart gives the assertion. \(\square\)

Consequently \(i_d\) on this closed conic incidence is proper over a small target cotangent neighborhood: the inverse image of a compact set has compact base and bounded covectors, and is closed. Define

\[
\Gamma_Y=i_d(i_\pi^{-1}\Gamma)
=\bigcup_\alpha T^*_{T_\alpha}Y,
\qquad
\Sigma=\operatorname{SS}(i^{-1}F)
\subset i_d(i_\pi^{-1}\Lambda)\subset\Gamma_Y.
\tag{5}
\]

The equality follows fibre by fibre from (2)–(3). Properness proves closedness of the image. The noncharacteristic microsupport estimate gives the inclusion for the actual ordinary inverse image. The [holomorphic-operation theorem](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#full-characteristic-inverse-image-for-a-holomorphic-map) proves its bounded weak complex constructibility and makes \(\Sigma\) closed complex analytic and Lagrangian, with every regular piece of complex dimension \(m\).

The canonical comparison and the relative dualizing calculation give

\[
i^!F\simeq i^{-1}F\otimes\omega_{Y/X}
\simeq i^{-1}F[-2c].
\tag{6}
\]

Complex orientation supplies the indicated trivialization of the relative sign line. A complex change of normal coordinates has positive real determinant \(|\det_{\mathbb C}|^2\); it preserves the normal orientation generator. The relative dimension is \(-2c\) as a real dimension, so its shift is \([-2c]\). The comparison in (6) is the canonical noncharacteristic map; an arbitrary chosen isomorphism would not establish it.

## Calculate the ordinary perverse bounds on each stratum

For the ordinary middle cuts, the condition on a stratum of complex dimension $d$ is an upper bound $a-d$ on ordinary restriction, or a lower bound $a-d$ on exceptional restriction, respectively. We prove their shifts directly, without using an equality with the microlocal cuts. On each \(S_\alpha\), put \(u_\alpha:S_\alpha\hookrightarrow X\); on each \(T_\alpha\), put \(v_\alpha:T_\alpha\hookrightarrow Y\) and \(j_\alpha:T_\alpha\hookrightarrow S_\alpha\). The preceding fixed-stratum proof makes both \(u_\alpha^{-1}F\) and \(u_\alpha^!F\) locally constant derived objects.

Composition of exceptional inverse images, followed by (6), gives

\[
v_\alpha^!i^{-1}F[-2c]
\simeq j_\alpha^!u_\alpha^!F
\simeq j_\alpha^{-1}u_\alpha^!F[-2c],
\qquad
v_\alpha^!i^{-1}F\simeq j_\alpha^{-1}u_\alpha^!F.
\tag{7}
\]

The second comparison uses locally constant \(u_\alpha^!F\) on the complex manifold \(S_\alpha\), so \(j_\alpha\), of complex codimension \(c\), is noncharacteristic for it. Cancelling the common shift produces the last comparison. We have proved this exceptional restriction identity using actual functor composition and canonical maps, without asserting an unconditional exceptional base-change theorem.

Ordinary restrictions satisfy \(v_\alpha^{-1}i^{-1}F=j_\alpha^{-1}u_\alpha^{-1}F\). Thus the source bounds \(u_\alpha^{-1}F\in D^{\le a-d_\alpha}\) and \(u_\alpha^!F\in D^{\ge a-d_\alpha}\) become the same bounds on the target pieces. Both target degree thresholds equal \((a-c)-(d_\alpha-c)=a-d_\alpha\).

The target intersections form a locally finite analytic-piece cover. Locally \(T_\alpha\) is the difference of \(Y\cap\overline{S_\alpha}\) and \(Y\cap(\overline{S_\alpha}\setminus S_\alpha)\), both closed analytic sets. Its closure retains precisely the locally finite analytic components of the first set not contained in the second; its frontier is their intersection with the second. These are the same analytic component and dimension facts used by the preceding complex refinement proof.

To apply the middle criteria, refine this cover by a complex μ-stratification. The ordinary restrictions remain locally constant. Exceptional restriction to a refining smooth piece \(R\subset T_\alpha\) of dimension \(e\) adds shift \([-2((d_\alpha-c)-e)]\) to the locally constant object in (7). Its lower bound consequently increases by \(2((d_\alpha-c)-e)\), which is at least the increase \((d_\alpha-c)-e\) required by the finer stratum criterion. Its ordinary upper bound already implies the weaker upper bound on \(R\). Hence the complete middle criteria apply on that refinement. Finally (6) supplies the exceptional shifts. We have proved

\[
i^{-1}:{}^{\mathrm{mid}}D^{\le a,\ge a}(X)
\longrightarrow{}^{\mathrm{mid}}D^{\le a-c,\ge a-c}(Y),
\qquad
i^!:{}^{\mathrm{mid}}D^{\le a,\ge a}(X)
\longrightarrow{}^{\mathrm{mid}}D^{\le a+c,\ge a+c}(Y),
\tag{8}
\]

where the two cuts are asserted separately. No field duality or perfect-stalk assumption was used.

## A dimension estimate for exceptional directions

We need an elementary consequence of the existing subanalytic regularity and ordinary stratification proofs. Let \(V\to M\) be a real analytic vector bundle of rank \(r\), and let \(B\subset V\) be subanalytic. Suppose every \(B_x\) is closed and nowhere dense in \(V_x\). Then

\[
\dim_{\mathbb R}B\le \dim_{\mathbb R}M+r-1.
\tag{9}
\]

For \(r=0\), all fibres are empty, and \(B=\varnothing\).

**Proof.** A subanalytic subset of an \(r\)-manifold with dimension \(r\) has an \(r\)-dimensional regular piece. The inverse function theorem makes such a piece open in that manifold. Thus each nowhere-dense \(B_x\) has dimension at most \(r-1\).

Decompose \(B\) into locally finite analytic submanifolds using the preceding ordinary refinement theorem. On each such piece \(P\), the bundle projection is analytic. It can be further decomposed into analytic pieces on which its restricted differential has constant rank. Here is the construction rather than an appeal to a fibre-dimension formula. On a connected analytic manifold take the maximal rank \(s\). The locus where an \(s\)-minor is nonzero is open and has constant rank \(s\). Its complement is analytic and has smaller dimension, because some such minor is not identically zero. Stratify that complement and repeat with the restricted projection on each resulting smooth piece. Dimension decreases at each exceptional stage, so local induction terminates. Countable charts and local finiteness make these decompositions sufficient for the dimension calculation.

On a constant-rank piece of dimension \(e\) and projection rank \(s\), the constant-rank theorem supplies a local fibre submanifold of dimension \(e-s\). It lies in one \(B_x\). Therefore \(e-s\le r-1\), while \(s\le\dim M\). Every such piece has \(e\le\dim M+r-1\). Taking the largest local stratum dimension proves (9). \(\square\)

This proof uses regularity and dimension drop for analytic zero sets. It does not assume that arbitrary smooth nowhere-dense sets have smaller dimension.

## Unshared lifts are enough at every regular target chart

Over \(T_\alpha\), let the bad source directions be

\[
B_\alpha=
\left(T^*_{S_\alpha}X|_{T_\alpha}\right)
\cap\bigcup_{\beta\ne\alpha}\overline{T^*_{S_\beta}X}.
\tag{10}
\]

Every fibre of \(B_\alpha\) is closed and nowhere dense by the full unshared-direction theorem. Its ambient bundle has real base dimension \(2(d_\alpha-c)\) and rank \(2(n-d_\alpha)\). Formula (9) gives \(\dim_{\mathbb R}B_\alpha\le2m-1\); for rank zero the set is empty. The isomorphism (2) preserves dimension on each bundle, and the locally finite union

\[
B_Y=\bigcup_\alpha i_d(B_\alpha)
\quad\text{satisfies}\quad
\dim_{\mathbb R}B_Y\le2m-1.
\tag{11}
\]

Subanalyticity and the dimension assertion are local in the ambient cotangent bundle. The source bad sets are subanalytic there by the earlier set calculus. Their ambient closures lie in the closed incidence $i_\pi^{-1}\Gamma$, so (4) also bounds the lifts on those closures. On a relatively compact base chart this gives properness on the closure, as required by the subanalytic image theorem. It does not assert that restriction to a nonclosed stratum is proper. Local finiteness of the original strata allows the finite-union dimension calculation near each basepoint.

Every nonempty open subset of a regular chart of \(\Sigma\) has real dimension \(2m\). It cannot be contained in \(B_Y\). Hence \(\Sigma_{\mathrm{reg}}\setminus B_Y\) is dense in \(\Sigma_{\mathrm{reg}}\).

Choose \(q\) in that dense set, with base \(y\in T_\alpha\). By (3) and (2), it has exactly one lift \(p\) in \(i_\pi^{-1}\Gamma\). That lift is unshared. Near \(p\), \(\Gamma\) is precisely the smooth conormal \(T^*_{S_\alpha}X\): the other locally finite closed conormal pieces miss \(p\), and \(S_\alpha\) is locally closed.

The stronger inclusion in (5) makes \(p\in\Lambda\): any lift in \(\Lambda\) is also a lift in \(\Gamma\), whose uniqueness was proved. The full localized comparison applies to \(F\), since \(i\) is noncharacteristic and the entire incidence fibre of \(\Lambda\) has exactly this lift.

The [earlier Hamiltonian-flow proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/involutive-subsets-of-subanalytic-isotropic-sets.md#a-closed-involutive-subset-of-a-smooth-isotropic-manifold) shows that a relatively closed involutive subset of a smooth Lagrangian is open there. Applied to \(\Lambda\subset\Gamma\) near \(p\), it gives \(\Lambda=\Gamma\) after a further shrink. Thus \(p\) is a regular constant-projection-rank point of the actual microsupport, not just of its containing set.

The confinement assertion in the localized comparison, or equivalently (4) and properness, excludes other source neighborhoods from contributing near \(q\). Thus \(\Sigma\) near \(q\) is contained in \(T^*_{T_\alpha}Y\). Since it contains \(q\), the same involutive-openness argument makes it equal to that conormal locally. Both regular conormal models needed for the type calculation have now been justified.

## Ordinary restriction retains the normalized type

At this \(p\), write the bounded conormal model as \(F\simeq Q_{S_\alpha}\) in \(D^b(X;p)\). It is an isomorphism in the localized category. It is not a statement that the original sheaf is constant on an ordinary neighborhood. On small base charts the model \(Q_{S_\alpha}\) is itself noncharacteristic for \(i\), and its entire incidence fibre at \(q\) has only \(p\). Apply the actual localized inverse functor to both objects and use its comparison with their ordinary restrictions. This gives

\[
i^{-1}F\simeq Q_{T_\alpha}\quad\text{in }D^b(Y;q).
\tag{12}
\]

For extension by zero along a locally closed submanifold, the identity \(i^{-1}Q_{S_\alpha}=Q_{T_\alpha}\) is also visible on stalks, and the natural pullback map has those identities at every stalk. The localized argument explains why the original \(F\) has that same model at \(q\).

Using numerical shift zero for type, the normalization in the preceding lesson gives

\[
\begin{aligned}
T_p(F)&=Q[n-d_\alpha],\\
T_q(i^{-1}F)&=Q[m-(d_\alpha-c)]=Q[n-d_\alpha],\\
T_q(i^!F)&=Q[n-d_\alpha][-2c].
\end{aligned}
\tag{13}
\]

Equivalently, if \(L=Q[-d_\alpha]\), then the normalized stratum coefficients of the two target models are \(L[c]\) and \(L[-c]\). This is where the two thresholds separate even though ordinary restriction retained the type.

## Both microlocal cuts and every threshold

For every integer \(a\), the formulas are

\[
\begin{array}{lll}
F\in{}^\mu D^{\le a}(X)&\Longrightarrow&
i^{-1}F\in{}^\mu D^{\le a-c}(Y),\qquad
i^!F\in{}^\mu D^{\le a+c}(Y),\\
F\in{}^\mu D^{\ge a}(X)&\Longrightarrow&
i^{-1}F\in{}^\mu D^{\ge a-c}(Y),\qquad
i^!F\in{}^\mu D^{\ge a+c}(Y).
\end{array}
\tag{14}
\]

**Proof.** The source upper condition is \(T_p(F)\in D^{\le a-n}(k)\). The target upper threshold for ordinary restriction is \((a-c)-m=a-n\), exactly the degree of the unchanged type in (13). For exceptional restriction the type is shifted by \([-2c]\); its upper bound is \(a-n+2c=(a+c)-m\). The lower calculation uses the same equalities with \(D^{\ge}\).

These comparisons initially hold at the dense good points constructed above. On every connected regular complex microsupport chart, the numerical-shift-zero type is locally constant as a bounded coefficient complex, by the preceding arbitrary-complex continuity theorem and the zero real inertia of complex Lagrangian planes. Shrink around any remaining regular point until the type is constant. A good point in that chart supplies its cut. Hence all regular points satisfy it. The microsupport of \(i^!F\) is the same as that of \(i^{-1}F\) by (6), so the exceptional conclusion propagates on the same charts. Empty microsupport makes every cut vacuous. \(\square\)

In particular \(i^{-1}F[-c]\) and \(i^!F[c]\) preserve the intersection of the two microlocal zero cuts. The signs in this assertion also follow by substituting \(H^j(C[s])=H^{j+s}(C)\).

## Exercises with complete solutions

### A constant complex fixes both signs

*Difficulty: Introductory.*

Take \(F=M_X[n]\), for any nonzero \(k\)-module \(M\), and a complex codimension-\(c\) section \(Y\). Compute ordinary and exceptional restriction, their middle degrees and their numerical-shift-zero types.

**Solution.** The source lies in the middle heart and has type \(M[n]\). Ordinary restriction is \(M_Y[n]=M_Y[m][c]\), whose middle degree is \(-c\). Exceptional restriction is \(M_Y[n-2c]=M_Y[m][-c]\), whose middle degree is \(c\). Their types are \(M[n]\) and \(M[n-2c]\), respectively. The target type thresholds at those degrees are \(-c-m=-n\) and \(c-m=-n+2c\), matching their actual cohomological degrees. The shifted functors preserving the heart are ordinary restriction followed by \([-c]\), and exceptional restriction followed by \([c]\).

### A transverse section of a supported complex

*Difficulty: Intermediate.*

Let \(X=\mathbb C^3\), \(S=\{z_3=0\}\), \(Y=\{z_2=0\}\), and \(F=(\mathbb Z/2)_S[2]\). Compute the section \(T\), the two restrictions and their normalized stratum coefficients. Explain why the example needs no field.

**Solution.** The planes have tangent sum \(T_xX\) at every intersection point. Their intersection is the line \(T=\{z_2=z_3=0\}\). Here \(d=2\), \(c=1\), \(m=2\), and ordinary restriction is \((\mathbb Z/2)_T[2]\). With the target normalization \([1]\), its stratum coefficient is \((\mathbb Z/2)[1]\). Exceptional restriction is \((\mathbb Z/2)_T[0]\), with stratum coefficient \((\mathbb Z/2)[-1]\). The type formula gives source and ordinary types \((\mathbb Z/2)[3]\), and exceptional type \((\mathbb Z/2)[1]\). The ring is \(\mathbb Z\), of finite global dimension; the support and orientation computations tensor finite free normal cochains with the module. No vector-space dimension or duality calculation occurs.

### A characteristic section gives a different answer

*Difficulty: Intermediate.*

Let \(X=\mathbb C\), \(Y=\{0\}\), and \(F=k_{\{0\}}\) with \(k\ne0\). Show that the section is characteristic and compute both actual restrictions. Compare with the ordinary upper bound proposed by (14).

**Solution.** The microsupport is the whole cotangent fibre above zero. Every such covector restricts to zero on the zero-dimensional tangent space of \(Y\), so the noncharacteristic condition fails for every nonzero covector. Both \(i^{-1}F\) and \(i^!F\) are \(k\) in degree zero: for the latter use \(i^!i_*=\mathrm{id}\) for the closed embedding. The point-supported source is in the microlocal zero cuts: its normalized type is \(k[1]\), concentrated in degree \(-1=-n\). With \(c=1\), the claimed ordinary upper target cut would be \(-1\), which excludes the nonzero \(k\). The failed hypothesis produces an actual failed bound.

### Nowhere-dense fibres give the needed strict inequality

*Difficulty: Intermediate.*

In the trivial real rank-two bundle \(V=\mathbb R_x\times\mathbb R^2_{a,b}\), take \(B=\{ab=0\}\). Give a constant-rank decomposition for the bundle projection and check (9). Contrast it with the rank-zero case.

**Solution.** The pieces \(a=0,b\ne0\) and \(b=0,a\ne0\) have dimension two and projection rank one. Their local fibres have dimension one. The piece \(a=b=0\) has dimension one and projection rank one, with zero-dimensional fibres. All fibres of \(B\) are the union of two lines, closed with empty interior in the rank-two vector space. Thus \(\dim B=2=\dim\mathbb R+2-1\). In a rank-zero bundle a fibre is a singleton; the only closed nowhere-dense subset of that singleton is empty. The conclusion is an empty total set, rather than a negative-dimension nonempty piece.

### Local isolation does not identify the global restriction

*Difficulty: Advanced.*

In \(X=\mathbb C^2\), let \(S_1=\{z_2=z_1\}\), \(S_2=\{z_2=-z_1\}\), \(Y=\{z_2=0\}\), and \(F=k_{S_1}\oplus k_{S_2}\). Above the origin choose the target covector \(q=dz_1\). Find both conormal lifts and explain the difference between a represented microlocal inverse image at one lift and the ordinary restriction.

**Solution.** A covector conormal to \(S_1\) is \(a(dz_2-dz_1)\); its restriction is \(-a\,dz_1\). The lift of \(q\) is therefore \(p_1=dz_1-dz_2\). On \(S_2\) the conormal is \(b(dz_2+dz_1)\), giving lift \(p_2=dz_1+dz_2\). Both source lines are transverse to \(Y\), and \(i\) is noncharacteristic for their union, but the entire incidence fibre at \(q\) contains these two distinct points.

Near \(p_1\) the second summand is invisible, so its represented microlocal inverse image is \(k_{\{0\}}\) at \(q\). The actual ordinary restriction is \(k_{\{0\}}\oplus k_{\{0\}}\), because both supported lines meet \(Y\) at zero. Local isolation near \(p_1\) supplies representability, but does not supply the full-fibre comparison. This example does not satisfy (1) at the origin: a transverse section of the zero-dimensional crossing stratum would have to be the whole two-dimensional ambient space.

### Two sections add their shifts

*Difficulty: Intermediate.*

Suppose \(Z\xrightarrow{j}Y\xrightarrow{i}X\) are successive transverse complex sections of codimensions \(c_2,c_1\), with the adapted stratification hypotheses at both stages. Compute the ordinary and exceptional cuts after both restrictions, and check the relative orientation shift under composition.

**Solution.** Ordinary inverse images compose as \(j^{-1}i^{-1}=(ij)^{-1}\). Applying (14) twice gives cut \(a-c_1-c_2\), for either upper or lower bounds. Exceptional inverse images compose as \(j^!i^!=(ij)^!\) and give cut \(a+c_1+c_2\). The relative dualizing comparisons compose in their fixed order, with shifts \([-2c_1]\) and \([-2c_2]\), hence total shift \([-2(c_1+c_2)]\). The complex normal orientations multiply to the complex orientation of the composite normal bundle. Both shifts are even, so exchanging their shifted lines contributes the Koszul sign \((-1)^{4c_1c_2}=1\). The heart-preserving ordinary shifts add to \([-(c_1+c_2)]\), and the exceptional shifts add to \([c_1+c_2]\).

## Further reading

Beilinson–Bernstein–Deligne, [*Faisceaux pervers*, Astérisque 100 (1982), §2.1, pp.56–59](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), introduces the stratum restriction and exceptional-restriction bounds and constructs the associated perverse heart. Those two different bounds explain why the ordinary calculation above must retain both functors. Its categories and coefficient conventions should be compared with the commutative-ring hypotheses stated here.

The microlocal proof additionally uses the linked unshared-direction theorem, conormal coefficient model, full-fibre localized inverse comparison and complex type-continuity argument. Each has a different role: isolating a lift, representing the coefficient object, identifying the actual restricted sheaf, and extending degree bounds across its regular microsupport. The ordinary argument does not require an identification of the two definitions of a perverse cut.
