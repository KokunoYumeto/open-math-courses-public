# Constructible functions and Euler integration

The Euler characteristic of each stalk turns a constructible complex into an integer-valued function. We prove that this gives exactly its Grothendieck class, including on a noncompact manifold with infinitely many strata. Compactly supported cohomology then defines integration, and point-supported cohomology defines duality. These two operations retain the difference between an open endpoint and a closed endpoint.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded relative to the prerequisites below; not independently reviewed. New original text is public domain (CC0).*

Use Constructible sheaves on a triangulation for face models and bounded constructible categories, Perfect coefficients on compact fibres for finite proper images, Small balls, central fibres and supported cohomology for the actual local contraction maps, and Constructible costalks and Verdier duality for perfect costalks and evaluation biduality. Perfect operations and finite microlocal coefficients proves exceptional inverse-image and internal-Hom closure; Duality maps for constructible inverse and direct images proves their normalized duality comparisons. The geometric prerequisite is locally finite compatible subanalytic triangulation, subordinate to an open cover when required, with a uniform dimension bound. Its lower Boolean, regularity and triangulation proofs are owned SH-03 foundations still being completed; the present proof is relative to that exact geometric input. Ordinary and proper-support adjunction, localization and composition are the standing sheaf-operation prerequisites.

P. Schapira's [Operations on constructible functions](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), *Journal of Pure and Applied Algebra* **72** (1991), 83–93, gives the calculus of constructible functions and Euler integration in §§2–3. The arguments below use the programme lessons linked here and explicitly treat locally finite strata, support and coefficient finiteness.

## Locally finite values and a sheaf of rings

Let \(X\) be a real analytic manifold, Hausdorff and countable at infinity, of uniformly bounded finite dimension. A function \(\varphi:X\to\mathbb Z\) is **constructible** if every level set is subanalytic and the family of nonempty level sets is locally finite. Write \(CF(X)\) for these functions and

\[
 |\varphi|=\overline{\{x:\varphi(x)\ne0\}}
 \qquad\text{(1)}
\]

for their closed support. A constructible function can be unbounded on a noncompact manifold. Local finiteness means that near every point only finitely many integer values occur.

Compatible stratification makes this equivalent to being constant on the pieces of a locally finite subanalytic stratification. Indeed, refine the locally finite family of level sets by a compatible stratification. Conversely, near a point only finitely many strata occur; their constant values give finitely many local level sets, each a finite union of subanalytic pieces. Subanalyticity is local, so each global level set is subanalytic.

Pointwise addition and multiplication preserve constructibility. Near a point choose finite common refinements of the two level partitions. Each refined piece has one pair of values, so both outputs have finitely many local values and subanalytic level sets. The constant function \(1\) is the unit.

Restriction to an open set preserves these conditions. Functions agreeing on overlaps glue uniquely, and the two constructibility conditions can be checked locally. Thus

\[
 U\longmapsto CF(U)
 \quad\text{is a sheaf of commutative rings, denoted }\mathcal{CF}_X.
 \qquad\text{(2)}
\]

## Closed simplices give compact generators

Take a locally finite subanalytic triangulation compatible with \(\varphi\), and write \(m_\sigma\) for its value on the open simplex \(\sigma^\circ\). Closed simplices are compact, subanalytic and contractible. For every simplex,

\[
 1_{\sigma^\circ}
   =\sum_{\tau\leq\sigma}
      (-1)^{\dim\sigma-\dim\tau}1_{\overline\tau}.
 \qquad\text{(3)}
\]

To check (3), evaluate at a point of \(\rho^\circ\). If \(\rho\not\leq\sigma\), all terms vanish. Otherwise the sum over \(\rho\leq\tau\leq\sigma\) is
\((1-1)^{\dim\sigma-\dim\rho}\), equal to one precisely when \(\rho=\sigma\).

Every simplex has finitely many cofaces in a locally finite triangulation. Regrouping the locally finite function sums therefore gives

\[
 \varphi=\sum_\tau c_\tau1_{\overline\tau},
 \qquad
 c_\tau=\sum_{\sigma\geq\tau}
       (-1)^{\dim\sigma-\dim\tau}m_\sigma.
 \qquad\text{(4)}
\]

Both sums are locally finite. This proves the compact contractible generator description. Conversely, any locally finite sum of integer multiples of indicators of compact subanalytic sets is constructible: near a point it is a finite sum, whose level sets are finite Boolean combinations. Contractibility is needed for the later integral normalization, rather than for this converse.

For compactly supported \(\varphi\), only finitely many nonzero open-simplex values occur: the closed support meets finitely many simplices. Its representation (4) can therefore be chosen finite.

## Extension from an arbitrary closed set

The sheaf \(\mathcal{CF}_X\) is **soft**: every section of its restriction to a closed subset \(K\subset X\) extends to \(X\). The subset \(K\) itself need not be subanalytic.

**Proof.** A section on \(K\) has, near each point of \(K\), a constructible representative on an open neighborhood \(U_\alpha\). Choose a countable locally finite family of compact subanalytic coordinate balls \(C_\alpha\subset U_\alpha\) whose interiors cover \(K\). Such a family is obtained by a locally finite refinement and shrinking of the open cover \(\{U_\alpha,X\setminus K\}\), retaining only balls meeting \(K\). Compact coordinate balls can be chosen inside each refined open set; finite coverings of compact layers of an exhaustion keep the resulting family locally finite.

Let \(\varphi_\alpha\) be the representative on \(U_\alpha\). In the chosen enumeration put

\[
 P_\alpha=C_\alpha\setminus\bigcup_{\beta<\alpha}C_\beta,
 \qquad
 \widetilde\varphi(x)=
 \begin{cases}
   \varphi_\alpha(x),&x\in P_\alpha,\\
   0,&x\notin\bigcup_\alpha C_\alpha.
 \end{cases}
 \qquad\text{(5)}
\]

Near any point, only finitely many balls and representatives are involved. Their Boolean pieces and level sets are subanalytic, so (5) is constructible. At \(x\in K\), shrink to a neighborhood meeting only the finitely many balls relevant there; balls in this list not containing \(x\) can be excluded because they are closed. For every remaining ball, its representative has the prescribed germ at \(x\). The finitely many representatives hence agree with one representative on a smaller neighborhood of \(x\). One of the balls contains \(x\) in its interior, so that neighborhood lies in their union. Formula (5) has the prescribed germ there. It therefore extends the original section on \(K\). \(\square\)

Softness asserts extension of germs on a closed set. Extension by assigning zero directly on its complement can fail constructibility when that closed set is arbitrary.

## Euler functions respect triangles and tensor products

For the rest of the lesson, \(k\) is a field of characteristic zero. Put
\(\mathcal D_X=D^b_{\mathbb R\text{-}c}(k_X)\): complexes are globally bounded and have finite-dimensional cohomology stalks on a locally finite subanalytic stratification. For \(F\in\mathcal D_X\), set

\[
 \chi_X(F)(x)=\sum_q(-1)^q\dim_k H^q(F_x).
 \qquad\text{(6)}
\]

This function is constructible. A common stratification for the finitely many cohomology sheaves makes all ranks locally constant; refinement into connected pieces makes them constant. All pointwise sums below are finite:

\[
 \begin{aligned}
 \chi_X(F\oplus G)&=\chi_X(F)+\chi_X(G),\\
 \chi_X(F\otimes_k^LG)&=\chi_X(F)\chi_X(G),\\
 \chi_X(F[r])&=(-1)^r\chi_X(F).
 \end{aligned}
 \qquad\text{(7)}
\]

The tensor identity follows from the finite Künneth formula over \(k\). For a distinguished triangle \(F'\to F\to F''\xrightarrow{+1}\), its finite stalk cohomology sequence gives

\[
 \chi_X(F)=\chi_X(F')+\chi_X(F'').
 \qquad\text{(8)}
\]

Indeed, break that sequence into kernels and images. Each image contributes in two adjacent terms with opposite signs and cancels.

Let \(K_0(\mathcal D_X)\) be generated by object classes, with the relations supplied by these triangles. Then (6) induces a ring homomorphism

\[
 \chi_X:K_0(\mathcal D_X)\longrightarrow CF(X).
 \qquad\text{(9)}
\]

The analogous Grothendieck group of constructible sheaves in degree zero is the same group. To prove this directly, send a bounded complex to
\(\sum_q(-1)^q[H^qF]\) in the abelian Grothendieck group. Kernels and images in its triangle sequence prove this additive. Successive truncation triangles give the inverse identity in \(K_0(\mathcal D_X)\); a sheaf in degree zero maps back to its own class. This argument uses the bounded constructible \(t\)-structure and does not require choosing a global complex of locally constant sheaves.

## Every function has a bounded realization with its support

**Theorem.** The homomorphism (9) is an isomorphism.

**Surjectivity.** Choose a compatible triangulation and its open simplices. Let \(k_{\sigma^\circ}\) denote constant coefficients extended by zero through their locally closed inclusion. Form the two sheaves

\[
 A=\bigoplus_{m_\sigma>0}k_{\sigma^\circ}^{\,m_\sigma},
 \qquad
 B=\bigoplus_{m_\sigma<0}k_{\sigma^\circ}^{\,-m_\sigma},
 \qquad F_\varphi=A\oplus B[1].
 \qquad\text{(10)}
\]

The families of closed simplices are locally finite. Thus these are locally finite sheaf sums, with finite stalks; locally each is a finite constructible sum. The complex is globally bounded in degrees \(-1,0\), even if the ranks are unbounded globally. Its Euler function is \(\varphi\), and its closed sheaf support is exactly \(|\varphi|\). This last statement follows by taking the closure of its nonzero stalk locus, which is exactly \(\{\varphi\ne0\}\).

The sums in (10) construct actual sheaves. They do not assert the existence of an infinite sum of classes in a Grothendieck group.

**Injectivity.** Every group element is the class of one object: use finite direct sums for positive integer coefficients, and \(G[1]\) for a negative copy of \([G]\). It is enough to prove \([F]=0\) when \(\chi_X(F)=0\).

Choose a compatible locally finite triangulation on which every \(H^qF\) is constant on open simplices. Let \(X_{\leq d}\) be its closed \(d\)-skeleton, \(X_{\leq-1}=\varnothing\), and
\(U_d=X_{\leq d}\setminus X_{\leq d-1}\). Write \(j_d:U_d\hookrightarrow X_{\leq d}\) and \(i_d:X_{\leq d}\hookrightarrow X\). Put \(F_d=i_d^{-1}F\). Localization on \(X_{\leq d}\), followed by closed direct image, gives

\[
 (i_d)_*j_{d!}j_d^{-1}F_d
 \longrightarrow (i_d)_*F_d
 \longrightarrow (i_{d-1})_*F_{d-1}
 \xrightarrow{+1}.
 \qquad\text{(11)}
\]

If \(n\) is the uniform dimension bound, iterate this only \(n+1\) times and then use bounded cohomological truncation on each \(U_d\):

\[
 [F]=\sum_{d=0}^{n}\ \sum_q(-1)^q
       [(i_d)_*j_{d!}(H^qF)|_{U_d}].
 \qquad\text{(12)}
\]

These are finite sums of classes. Each \(U_d\) is a disjoint union of open \(d\)-simplices. On one such simplex, the constant sheaves
\(\bigoplus_{q\text{ even}}H^qF\) and
\(\bigoplus_{q\text{ odd}}H^qF\)
have equal finite rank because \(\chi_X(F)=0\). Choose an isomorphism there. The choices combine into a sheaf isomorphism on their disjoint union \(U_d\). Its extension by \(j_{d!}\) and \((i_d)_*\) cancels the even and odd terms of (12). Every \(d\)-term is zero, proving injectivity. \(\square\)

The same proof works in the full subcategory whose objects have closed support contained in a fixed closed subanalytic set \(C\). Take the triangulation compatible with \(C\); all skeleton triangles and truncations retain that support. Thus it also gives

\[
 K_0(\mathcal D_{X,C})
   \simeq\{\varphi\in CF(X):|\varphi|\subset C\}.
 \qquad\text{(13)}
\]

In particular, there is an identical statement for compact closed support, using finite unions of such compact supports for any finite collection of representatives and relations.

## Products and ordinary inverse image

For real analytic \(f:Y\to X\) and functions on \(X,Y\), define

\[
 f^*\varphi=\varphi\circ f,\qquad
 (\varphi\boxtimes\psi)(x,y)=\varphi(x)\psi(y).
 \qquad\text{(14)}
\]

The subanalytic inverse-image property and locally finite level partitions prove constructibility of \(f^*\varphi\); products use finite local common partitions. The stalk and external tensor formulas give

\[
 f^*\chi_X(F)=\chi_Y(f^{-1}F),\qquad
 \chi_{X\times Y}(F\boxtimes G)=\chi_X(F)\boxtimes\chi_Y(G).
 \qquad\text{(15)}
\]

Ordinary inverse image is a ring homomorphism, with \((f\circ g)^*=g^*f^*\). There is no dimension sign in it.

## Integration with compact closed support

For \(\varphi\in CF(X)\) with compact \(|\varphi|\), choose the realization (10), which has compact closed support. Define

\[
 \int_X\varphi\,d\chi
    =\chi\bigl(R\Gamma_c(X;F_\varphi)\bigr).
 \qquad\text{(16)}
\]

That section complex is perfect by compact constructible finiteness. Compact and ordinary global sections agree for this representative.

The number is independent of the representative **within the compact-support category**. Two compactly supported representatives with the same Euler function have the same class by (13); their finite triangles remain supported in a compact union. The exact functor \(R\Gamma_c\) takes this category to perfect coefficient complexes, whose Euler characteristic is additive. It gives the same integer for both classes. A representative with a noncompact closed support requires its own finiteness check before taking a global Euler characteristic.

For a finite expression by relatively compact locally closed subanalytic sets,

\[
 \varphi=\sum_\alpha a_\alpha1_{S_\alpha},
 \qquad
 \int_X\varphi\,d\chi
    =\sum_\alpha a_\alpha\chi_c(S_\alpha;k).
 \qquad\text{(17)}
\]

This follows by representing each indicator by \(k_{S_\alpha}\), whose closed support is compact, and using proper-support composition for its inclusion. On an open \(d\)-simplex,
\(R\Gamma_c(\sigma^\circ;k)=k[-d]\), so the finite open-cell formula is
\(\sum_\sigma(-1)^{\dim\sigma}m_\sigma\). On a compact contractible closed simplex the cohomology is \(k\) in degree zero, so (4) gives instead \(\sum_\tau c_\tau\). These agree by (3) and (17).

## Direct image integrates the fibres

Let \(f:Y\to X\) be real analytic and assume it is proper on the closed support \(|\psi|\) of \(\psi\in CF(Y)\). Define

\[
 (f_!\psi)(x)
    =\int_{f^{-1}(x)}\psi|_{f^{-1}(x)}\,d\chi.
 \qquad\text{(18)}
\]

A singular fibre is treated as a subanalytic subset: its integral is equivalently the ambient integral on \(Y\) after multiplying by \(1_{f^{-1}(x)}\). Its nonzero closed support is compact by support properness.

Choose (10) on \(Y\). The proper-on-support theorem and proper-support base change give

\[
 Rf_!F_\psi\in\mathcal D_X,\qquad
 (Rf_!F_\psi)_x
   \simeq R\Gamma_c(f^{-1}(x);F_\psi|_{f^{-1}(x)}),
 \quad
 f_!\psi=\chi_X(Rf_!F_\psi).
 \qquad\text{(19)}
\]

In particular (18) is constructible. Equation (13), applied on the support-proper subcategory, makes (19) independent of the chosen representative with that support. The closed support of the output is contained in the closed subanalytic proper image \(f(|\psi|)\). Locally on \(X\), this defines the sheaf morphism \(f_!\mathcal{CF}_Y\to\mathcal{CF}_X\) on sections with support proper over that neighborhood.

Proper-support composition and projection yield, whenever their supports satisfy these conditions,

\[
 \begin{aligned}
 g_!(f_!\psi)&=(g\circ f)_!\psi,\\
 f_!(\psi\,f^*\varphi)&=(f_!\psi)\varphi.
 \end{aligned}
 \qquad\text{(20)}
\]

For the first identity it suffices to require \(f\) proper on \(|\psi|\) and \(g\) proper on \(f(|\psi|)\). One can also assume directly that \(g\circ f\) is proper on \(|\psi|\); then \(f\) is proper there, and \(g\) is proper on its image. For example, the inverse image in \(|\psi|\) of a compact \(K\subset X\) is a closed subset of the compact inverse image of \(g(K)\); the same argument over a compact subset of the final target proves properness on the image. The sheaf projection formula proves the second identity through (7), (15) and (19). Tensoring with \(f^{-1}F_\varphi\) keeps support inside \(|\psi|\).

## Duality is an open-ball Euler integral

Define an additive operation on constructible functions by

\[
 D_X\varphi=\chi_X(D_XF),\qquad \chi_X(F)=\varphi,
 \quad D_XF=R\mathcal Hom(F,\omega_X).
 \qquad\text{(21)}
\]

Duality is a contravariant exact functor preserving constructibility. Reversing a triangle preserves its additive relation, so it induces a homomorphism on \(K_0\). The isomorphism (9) therefore proves (21) independent of \(F\).

For a sufficiently small coordinate ball \(B(x,\epsilon)\), the written costalk and small-ball comparisons give

\[
 (D_XF)_x\simeq (i_x^!F)^\vee,\qquad
 i_x^!F\simeq R\Gamma_c(B(x,\epsilon);F).
 \qquad\text{(22)}
\]

The complexes are perfect. Coefficient dual reverses degrees and preserves their Euler characteristic. Hence

\[
 (D_X\varphi)(x)
   =\int_X1_{B(x,\epsilon)}\varphi\,d\chi
   \qquad(0<\epsilon\ll1).
 \qquad\text{(23)}
\]

The cutoff has compact closed support. The comparisons in (22) prove that this integer is stable and independent of the coordinate chart. They also prove that it depends only on the germ of \(\varphi\). Thus \(D_X\) is an endomorphism of the sheaf of abelian groups \(\mathcal{CF}_X\).

Actual constructible biduality gives \(D_X^2\varphi=\varphi\). On an \(n\)-dimensional component, \(D_X1_X=(-1)^n1_X\), because the orientation line in \(\omega_X=\operatorname{or}_X[n]\) has rank one. No global orientation is required.

For \(f\) proper on \(|\psi|\), the realization (10) and its dual have that same closed support, by biduality. Both proper images are constructible. The normalized dual-sections comparison and equality \(Rf_*=Rf_!\) on these supports give

\[
 f_!D_Y\psi=D_Xf_!\psi.
 \qquad\text{(24)}
\]

This applies in particular to a compactly supported function and the map to a point:
\(\int_X D_X\varphi\,d\chi=\int_X\varphi\,d\chi\).

## The boundary Euler formula

Let \(Z\subset X\) be locally closed and subanalytic. Suppose that, at every \(x\in\overline Z\), there is a cofinal system of open neighborhoods \(U\) with \(U\cap Z\) homeomorphic to \(\mathbb R^d\), for one fixed \(d\). Then

\[
 D_X1_Z=(-1)^d1_{\overline Z}.
 \qquad\text{(25)}
\]

Here is the local argument, including boundary points. On these neighborhoods,
\(R\Gamma_c(U;k_Z)=R\Gamma_c(U\cap Z;k)=k[-d]\), after an orientation choice. At interior points the condition makes \(Z\) a topological \(d\)-manifold. Between nested members of the cofinal system, extension of compact support is the top orientation map for an open inclusion of two copies of \(\mathbb R^d\). It sends a local orientation generator to the same generator: choose a small ball contained in both and use its local class. Hence it is an isomorphism. The compact-section neighborhood system is consequently represented by \(k[-d]\). The cohomological constructibility comparison identifies its representative with \(i_x^!k_Z\), proving Euler value \((-1)^d\). Outside \(\overline Z\) a neighborhood is disjoint from \(Z\), giving zero. This proves (25).

If \(\overline Z\) is compact with \(\chi(\overline Z;k)=1\), duality-invariant integration gives
\(\chi_c(Z;k)=(-1)^d\). Since
\(1_{\overline Z}=1_Z+1_{\overline Z\setminus Z}\), we obtain

\[
 \chi_c(\overline Z\setminus Z;k)=1-(-1)^d.
 \qquad\text{(26)}
\]

This includes the usual boundary Euler characteristic of a closed ball.

## Exceptional inverse image and internal Hom

For \(f:Y\to X\), define

\[
 f^!\varphi=D_Y(f^*D_X\varphi),\qquad
 \operatorname{hom}_X(\psi,\varphi)
     =D_X(\psi\,D_X\varphi).
 \qquad\text{(27)}
\]

The written evaluation and tensor–Hom comparisons give

\[
 \begin{aligned}
 f^!\chi_X(F)&=\chi_Y(f^!F),\\
 \operatorname{hom}_X(\chi_X(G),\chi_X(F))
    &=\chi_X(R\mathcal Hom(G,F)).
 \end{aligned}
 \qquad\text{(28)}
\]

For the first, use \(f^!F\simeq D_Yf^{-1}D_XF\); for the second use
\(R\mathcal Hom(G,F)\simeq D_X(G\otimes D_XF)\).
All inputs and outputs are bounded constructible, so (9) applies. At a smooth submersion of relative dimension \(r\), the exceptional orientation line has rank one and shift \(r\), giving \(f^!\varphi=(-1)^rf^*\varphi\). At a critical map, (27) retains the full duality operation. Internal Hom also retains boundary information; its ordinary stalk need not be the Hom of the two ordinary stalks.

## Exercises with complete solutions

### Infinitely many values without an infinite group sum

*Difficulty: Intermediate.*

On \(\mathbb R\), let \(\varphi(n)=n\) for \(n\in\mathbb Z\) and let \(\varphi=0\) off the integers. Show that it is constructible, realize it by a bounded complex, and explain why its Euler integral is not supplied by (16).

**Solution.** The integer set is closed and locally finite, so each nonzero level set is a point. The zero level is \(\mathbb R\setminus(\mathbb Z\setminus\{0\})\), which is subanalytic and includes the integer zero. Any small bounded neighborhood meets finitely many integers. Let \(A=\bigoplus_{n>0}k_{\{n\}}^n\) and \(B=\bigoplus_{n<0}k_{\{n\}}^{-n}\). The actual sheaf complex \(A\oplus B[1]\) has finite stalks and Euler function \(\varphi\), in the same two global degrees as (10). Its closed support is noncompact, and its compact-section cohomology contains infinite-dimensional direct sums. There is no finite Euler characteristic for that complex. The construction creates one Grothendieck class; it uses no infinite sum of classes.

### Equal classes can retain different monodromy

*Difficulty: Intermediate.*

Let \(L\) be the rank-one local system on a circle with monodromy \(-1\), over the characteristic-zero field \(k\). Compare it with \(k_{S^1}\) as a sheaf, as a Grothendieck class, and under integration.

**Solution.** The two sheaves are not isomorphic, because their monodromy maps differ. Both Euler functions are \(1\), so (9) gives \([L]=[k_{S^1}]\). A cell cut with one vertex and one open edge writes each class as \([k_{\mathrm{vertex}}]+[k_{\mathrm{open\ edge}}]\), using one localization triangle. The circle cochain complex for \(L\) is \([k\xrightarrow{-2}k]\) in degrees zero and one, hence acyclic. The constant sheaf has \(k\) in both cohomology degrees. Both global Euler characteristics are zero, as is \(\int_{S^1}1\,d\chi=1-1\). Equality of classes preserves this additive measurement, while allowing different monodromy and cohomology.

### A weighted interval

*Difficulty: Introductory.*

Compute the Euler integrals of the open, closed and half-open unit intervals. Then integrate
\(\varphi=3\,1_{[0,1]}-2\,1_{(0,1)}+4\,1_{\{0\}}\).

**Solution.** The open interval has compact cohomology \(k[-1]\), hence integral \(-1\). The closed interval is contractible and compact, giving \(1\). The half-open interval is the closed interval minus one endpoint, giving \(0\). The weighted integral is \(3+2+4=9\). Equivalently the function has values \(7\) at zero, \(1\) in the interior and \(3\) at one; its open-cell sum is \(7-1+3=9\).

### Duality exchanges interval endpoints

*Difficulty: Intermediate.*

On \(\mathbb R\), calculate \(D1_{(0,1)}\), \(D1_{[0,1]}\) and \(D1_{\{0\}}\) using (23).

**Solution.** At an interior point of either interval, the small intersection is an open interval, giving \(-1\). For the open interval at an endpoint, that intersection is again an open interval, so its value is \(-1\). For the closed interval at an endpoint, the intersection is half-open, whose integral is zero. Outside the closed interval it is empty. Thus \(D1_{(0,1)}=-1_{[0,1]}\) and \(D1_{[0,1]}=-1_{(0,1)}\). A point remains a point with coefficient one. Applying \(D\) twice restores each function. Their integrals are also preserved. For the weighted function of the previous exercise, \(D\varphi=-3\,1_{(0,1)}+2\,1_{[0,1]}+4\,1_{\{0\}}\), again with integral \(9\).

### A branch point in a proper image

*Difficulty: Intermediate.*

Let \(f(t)=t^2:\mathbb R\to\mathbb R\) and \(\psi=1_{[-1,1]}\). Calculate \(f_!\psi\) and verify (24) at zero and at the image endpoints.

**Solution.** At \(x=0\) the fibre contains one included point. For \(0<x\leq1\) it contains two, and outside \([0,1]\) it contains none. Hence \(f_!\psi=2\,1_{[0,1]}-1_{\{0\}}\), whose integral is \(2-1=1\). Since \(D\psi=-1_{(-1,1)}\), its direct image is \(-2\,1_{(0,1)}-1_{\{0\}}\): the value at zero is \(-1\), while at one it is zero. Duality of the first formula gives precisely this same function. The branch point contributes one fibre point, and the source endpoints disappear in the dual; these facts account for both endpoint values.

### Ordinary and exceptional restriction have different signs

*Difficulty: Intermediate.*

For \(i:\{0\}\hookrightarrow\mathbb R\), calculate \(i^*1_{\mathbb R}\), \(i^!1_{\mathbb R}\) and \(i^!1_{\{0\}}\). Is exceptional restriction always \(-i^*\) for this embedding?

**Solution.** Ordinary restriction gives \(1\). Since \(D_{\mathbb R}1_{\mathbb R}=-1_{\mathbb R}\) and point duality is the identity, (27) gives \(i^!1_{\mathbb R}=-1\). This is the Euler characteristic of the constant-sheaf costalk \(k[-1]\). But \(D_{\mathbb R}1_{\{0\}}=1_{\{0\}}\), so \(i^!1_{\{0\}}=1\), the point-supported sheaf's own costalk. Thus the sign formula for an ambient locally constant coefficient does not extend to every constructible function across the point.

### Internal Hom sees the boundary

*Difficulty: Advanced.*

Take \(G=k_{[0,\infty)}\) and \(F=k_{\mathbb R}\). Calculate the Euler function of \(R\mathcal Hom(G,F)\) and compare its value at zero with \(\dim_k\operatorname{Hom}(G_0,F_0)\).

**Solution.** Small-ball calculation gives \(D1_{[0,\infty)}=-1_{(0,\infty)}\) and \(D1_{\mathbb R}=-1_{\mathbb R}\). Formula (27) yields
\(\operatorname{hom}(1_{[0,\infty)},1_{\mathbb R})
=D(-1_{[0,\infty)})=1_{(0,\infty)}\).
Its value at zero is zero, while both ordinary stalks are \(k\) and their vector-space Hom has dimension one. Internal Hom is a sheaf of local morphisms and derived local extensions, so its stalk is not computed by taking just those two stalks. Here closed-support localization also calculates its boundary stalk as the fibre of the identity restriction \(k\to k\), hence as zero.

### Euler characteristic of a ball boundary

*Difficulty: Introductory.*

Let \(Z\) be the open unit ball in \(\mathbb R^d\), with \(d\geq1\). Derive the Euler characteristic of its boundary using duality.

**Solution.** At every point of its closed ball, the small open intersection with \(Z\) is homeomorphic to \(\mathbb R^d\), so (25) gives \(D1_Z=(-1)^d1_{\overline Z}\). The closed ball has Euler characteristic one, and duality preserves the integral. Thus \(\chi_c(Z)=(-1)^d\). Subtract its indicator from that of the closed ball to obtain \(\chi(\partial Z)=1-(-1)^d\). It is zero for even \(d\) and two for odd \(d\); in dimension one this counts the two endpoints.

### A zero function with a noncompact representative

*Difficulty: Advanced.*

Let \(a:\mathbb R\to\{\mathrm{pt}\}\), let \(J:\mathbb Z\hookrightarrow\mathbb R\), and put \(G=J_*k_{\mathbb Z}\oplus J_*k_{\mathbb Z}[1]\). Its Euler function is zero. Explain why (16) does not calculate its integral by taking the Euler characteristic of \(Ra_!G\).

**Solution.** At an integer the two finite stalks contribute \(1-1=0\), and elsewhere both are zero. The function zero has the compactly supported representative \(0\), giving integral zero. However \(G\) has the noncompact closed support \(\mathbb Z\). The compact-section complex of \(J_*k_{\mathbb Z}\) is the infinite-dimensional vector space \(\bigoplus_{\mathbb Z}k\) in degree zero; its shifted copy is in degree minus one. Neither coefficient dimension is finite, so their signed difference is not a defined Euler characteristic. Equality of the class with zero in the full Grothendieck group does not make this nonproper image a perfect complex. The compact-support version (13) is the reason (16) is well-defined.

The next lesson treats positive-homogeneous functions, Fourier–Sato transformation and specialization. These operations lead to the correspondence with integral Lagrangian cycles.
