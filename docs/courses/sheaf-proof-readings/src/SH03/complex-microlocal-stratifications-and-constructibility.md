# Complex microlocal stratifications and constructibility

Complex constructibility requires a common analytic decomposition for all cohomology sheaves. We will construct such decompositions with the microlocal compatibility needed at their boundaries, then prove four equivalent tests for weak complex constructibility. One test only asks for a complex-conic isotropic bound on microsupport. We explain why that bound forces microsupport itself to be complex-conic; invariance of a containing set does not by itself imply invariance of its arbitrary subsets.

Let \(X\) be a complex manifold of complex dimension \(n\), Hausdorff and countable at infinity. All families below are locally finite in the ambient manifold, including at points outside their members. An analytic piece means a locally closed subset whose closure and frontier are closed complex analytic. Strata are smooth analytic pieces of fixed complex dimension and may be disconnected. Use the holomorphic cotangent bundle, \(\alpha=\sum\xi_jdz_j\), \(\Omega=d\alpha\), and its real identification with symplectic form \(\operatorname{Re}\Omega\).

The geometric prerequisites are Analytic normal cones through complex deformation, Analytic conormal covers and singular involutivity, and the full real limiting-sum and refinement proofs in Limiting cotangent sums and Microlocal stratifications by removing bad loci. We give the additional complex analytic closure arguments here. Their primitive analytic and subanalytic inputs remain explicit open dependencies.

For the sheaf statements, let \(k\) be a commutative ring of finite global dimension and \(F\in D^b(k_X)\). Boundedness means one finite global cohomological interval. The fixed real μ-stratification criterion and the real constructibility equivalences are those proved in Constructibility from microsupport and perfect stalks. Involutivity of the full microsupport is the exact existing microlocal prerequisite. Weak constructibility has no finite-generation requirement. Noetherian or field hypotheses are not added silently.

The freely readable comparison is Kashiwara and Schapira, *Microlocal study of sheaves*, Theorem 8.5.2 and Lemma 8.5.3, printed 151–152: weak real constructibility together with complex cotangent conicity characterizes weak complex constructibility. The full microlocal refinement and analytic-closure arguments are supplied below with their stated geometric prerequisites. General derived realization, including any failure of equivalence, remains a separate teaching obligation.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## The ordered complex μ-condition

For smooth analytic pieces \(M,N\subset X\), write \(T_M^*X\) for the ordinary conormal. The ordered pair \((M,N)\) is μ when

\[
(T_M^*X\widehat+T_N^*X)\cap\pi^{-1}N\subset T_N^*X.
\tag{1}
\]

The limiting sum retains sequences at different moving base points and unbounded cancelling covectors. In a coordinate chart its criterion is

\[
\begin{gathered}
(x_j,\xi_j)\in T_M^*X,\quad (y_j,\eta_j)\in T_N^*X,
\quad x_j,y_j\to x\in N,\\
\xi_j+\eta_j\to\sigma,\qquad
|x_j-y_j|\,|\xi_j|\to0
\quad\Longrightarrow\quad \sigma|_{T_xN}=0.
\end{gathered}
\tag{2}
\]

Norms are underlying real norms. Complex multiplication multiplies norms by its absolute value; hence it preserves this criterion. The sum is symmetric, while (1) is ordered because the target base is \(N\). An ordinary conormal closure check only tests bounded covectors and cannot replace (2).

A complex μ-stratification is a locally finite partition \(X=\bigsqcup_aS_a\) into smooth analytic pieces, with the frontier rule

\[
S_b\cap\overline{S_a}\ne\varnothing\quad\Longrightarrow\quad
S_b\subset\overline{S_a},
\tag{3}
\]

and condition (1) for every distinct incident pair \(S_b\subset\overline{S_a}\setminus S_a\). It is also a real subanalytic μ-stratification under the real cotangent identification.

## Why the full limiting conormal sum is analytic

An ordinary conormal \(T_M^*X\) is an analytic piece, not necessarily a closed analytic subset of \(T^*X\). Indeed, if \(\Sigma_{\overline M}\) is the analytic regular conormal closure from the preceding lesson, then

\[
T_M^*X=\Sigma_{\overline M}\cap\pi^{-1}M.
\tag{4}
\]

Its closure is \(\Sigma_{\overline M}\); its frontier is the intersection of that analytic set with the inverse image of \(\overline M\setminus M\). The smooth piece is open dense in the regular part of its pure-dimensional closure, so ordinary conormal density justifies this assertion also when the piece omits additional regular base points.

We need the normal cone of an analytic piece \(S\) along a smooth closed complex submanifold \(L\) of a complex manifold \(P\). In adapted coordinates \((y,z)\) with \(L=\{z=0\}\), take the complex deformation map

\[
q(y,v,t)=(y,tv).
\tag{5}
\]

Its accessible subset is \(t\ne0\) with \(q(y,v,t)\in S\). This is an analytic set with an analytic deletion: use \(\overline S\), delete its frontier inverse image and \(t=0\), then retain the component closure. The resulting deformation closure is analytic. Its central fibre is the positive-real normal cone \(C_L(S)\) in the normal bundle. A real cone witness substitutes \(z=hv\), \(t=h>0\). Conversely, a finite holomorphic arc through a central point, avoiding the deleted analytic set, has parameter \(t=s^m b(s)\) with \(b(0)\ne0\). The root and inverse reparameterization already proved in the normal-cone lesson makes \(t=u^m>0\) for positive real \(u\). This gives actual points of \(S\) with \(z/t\to v\) and proves the reverse inclusion. Holomorphic adapted-coordinate transitions glue the central fibres. Thus

\[
C_L(S)\text{ is closed complex analytic in }N_LP.
\tag{6}
\]

Apply this to \(P=T^*(X\times X)\), \(L=T^*_{\Delta}(X\times X)\), and \(S=T_M^*X\times T_N^*X\). The conormal to the diagonal is a smooth complex Lagrangian. Its holomorphic normal identification and the zero-normal-section embedding are

\[
K:N_LP\longrightarrow T^*L,\qquad K([w])(v)=\Omega_P(w,v),
\qquad e:T^*X\longrightarrow T^*L.
\tag{7}
\]

Here \(e(x,\sigma)=(j(x),(dr_{j(x)})^t\sigma)\), where \(r:L\to X\) is the diagonal-base projection and \(j\) its zero covector section. These are holomorphic maps, and \(K\) is a bundle isomorphism. The exact full limiting-sum identity proved with positive scales and unbounded covectors in the real lesson is

\[
T_M^*X\widehat+T_N^*X=e^{-1}\bigl(KC_L(S)\bigr).
\tag{8}
\]

The same maps agree under realification, including the inverse normal identification induced by \(-H\). Formula (6) and holomorphic inverse image therefore make (8) closed complex analytic. Complex fibre conicity also follows directly by multiplying both covectors in its sequence criterion by one \(\lambda\in\mathbb C^*\). The real theorem gives real isotropy. On a complex regular tangent space, vanishing of \(\operatorname{Re}\alpha\) also gives vanishing of \(\operatorname{Im}\alpha\), by testing a tangent vector and its imaginary multiple. Hence this limiting sum is complex isotropic. Analyticity here comes from the exact normal-cone slice, not merely from isotropy.

## Analytic bad loci for a pair

Put \(L_{M,N}=T_M^*X\widehat+T_N^*X\). Its points over \(N\) which are not conormal to \(N\) form

\[
Q_{M,N}=
\bigl(L_{M,N}\cap\pi^{-1}\overline N\bigr)
\setminus\bigl(\Sigma_{\overline N}\cup
\pi^{-1}(\overline N\setminus N)\bigr).
\tag{9}
\]

This formula uses only a closed analytic set and a closed analytic deletion. Over \(N\), (4) identifies the removed conormal correctly. Thus its ambient closure is analytic by component selection. It is complex-conic. Its projected closure is consequently

\[
D_{M,N}=\pi(\overline{Q_{M,N}})
=\{x:(x,0)\in\overline{Q_{M,N}}\}
=\overline{\pi(Q_{M,N})}^{\,X},
\tag{10}
\]

and is closed analytic. The last equality uses covector rescaling towards zero if covectors escape to infinity; this is the same exact projection-closure argument used for critical loci in the preceding lesson.

The actual bad points in the target base are \(B_{M,N}=\pi(Q_{M,N})\subset N\). The generic analytic-base theorem, applied to the isotropic cone \(L_{M,N}\) and smooth base \(N\), proves that \(D_{M,N}\cap N\) is nowhere dense in \(N\). Therefore

\[
N\setminus D_{M,N}
\tag{11}
\]

is an open dense analytic piece on which the pair is μ in a neighborhood of every point. Neighborhood locality follows from (2): a sequence converging to a point in an ambient open neighborhood eventually lies in that neighborhood. Conversely a neighborhood with no failure points avoids their closure at its interior points. The analytic set (10) can include frontier points outside \(N\); it need not be nowhere dense in a different lower stratum.

## Ordinary analytic refinement with every frontier checked

First we construct ordinary analytic strata. Let \(Y\subset X\) be closed analytic, with a locally finite cover by analytic pieces. We require the stronger compatibility that every stratum lies wholly in, or is disjoint from, each cover member.

Replace the cover-membership questions by membership in their closures and frontiers, all closed analytic. These families remain locally finite. Exact membership cells for this closed analytic family are intersections of the finitely many sets containing a cell, with the union of all other sets deleted. That union is locally a finite closed analytic union. Include \(Y\) among the closed sets and restrict to it. The cells form a locally finite partition \((P_i)\) of \(Y\), and each is an analytic piece by component selection. Original cover membership is determined by these cells.

We stratify this partition by induction on \(d=\dim_{\mathbb C}Y\). The empty case is immediate. Choose a closed analytic set \(R\subset Y\) containing the following:

- the singular locus of \(Y\) and its irreducible components of dimension less than \(d\);
- every cell frontier, the singular locus of every \(\overline{P_i}\), and every component of \(\overline{P_i}\) of dimension less than \(d\).

Take the union of exactly those sets. All families are locally finite, so this union is closed analytic. Every listed set has dimension less than \(d\); a cell frontier has smaller dimension than its closure because no component of that closure is contained in its deleted frontier. Hence

\[
\dim_{\mathbb C}R<d.
\tag{12}
\]

Outside \(R\), each point belongs to a smooth dimension-\(d\) part of its cell and to the smooth dimension-\(d\) part of \(Y\). A smooth inclusion of equal-dimensional complex manifolds is open. Thus \(U_i=P_i\setminus R\) is a smooth analytic piece open in \(Y\), and the disjoint \(U_i\) cover \(Y\setminus R\). Their closures are analytic by the component-deletion rule and remain locally finite.

Before stratifying \(R\) inductively, impose membership both in every original cell and in every \(R\cap\overline{U_i}\). For cell membership use its closure and frontier. These are again locally finite analytic membership questions. The induction gives lower strata \(T_b\) compatible with all of them. Combine \(U_i\) and \(T_b\). Lower-to-lower frontiers hold inductively. Lower-stratum closures cannot meet any \(U_i\), since \(R\) is closed. Distinct \(U_i\) cannot approach one another inside \(Y\setminus R\): each is open and its complement there is open. If a \(T_b\) meets \(\overline{U_i}\), the additional frontier membership forces all of \(T_b\) into that closure. These are all the frontier incidences. The result is a locally finite ordinary complex stratification compatible with every original membership. All dimension drops in this argument are complex dimension drops; no real simplex was introduced.

## Removing only the analytic microlocal failure set

**Refinement theorem.** Every locally finite analytic-piece covering of \(X\) admits a compatible complex μ-stratification.

**Proof.** Begin with the ordinary analytic refinement just constructed. For its ordered incident pairs form all the actual bad sets \(B_{S_a,S_b}\). Their closures (10) form a locally finite analytic family. Indeed a bad limit must lie in \(\overline{S_a}\cap\overline{S_b}\); near an ambient point only finitely many such stratum closures occur. Consequently

\[
D=\overline{\bigcup_{(a,b)\text{ incident}}B_{S_a,S_b}}
=\bigcup_{(a,b)\text{ incident}}D_{S_a,S_b}
\tag{13}
\]

is closed analytic. By locality, \(\Omega=X\setminus D\) is precisely the largest open set on which this stratification is μ.

Suppose a closed analytic union of strata \(Y\) contains all possible failures, and the stratification is already μ on \(X\setminus Y\). Then \(D\subset Y\). We check that \(\Omega\cap Y\) is dense in \(Y\), including near a lower-dimensional component. Take any nonempty relatively open part of \(Y\), shrink near a regular point of one of its components, and use local finiteness. A finite union of strata of smaller dimension cannot fill that smooth local component. A full-dimensional stratum there is open in it. Shrinking once more makes \(Y\) locally equal to a part of one target stratum \(S_b\).

All failure points in that neighborhood now have target \(S_b\), since there are no failures outside \(Y\). Only finitely many upper strata occur. Each has an open dense good locus (11) in \(S_b\); their finite intersection is open dense. Choose a point in it and a smaller ambient neighborhood avoiding all those failure sets. No other failure set is present there, so that point lies in \(\Omega\). This proves density in every chosen part of \(Y\).

Thus the new bad set \(Y'=D\subset Y\) is nowhere dense in \(Y\) and satisfies

\[
\dim_{\mathbb C}Y'<\dim_{\mathbb C}Y
\tag{14}
\]

when nonempty. Keep the outside pieces \(S_a\cap\Omega\), and stratify only \(Y'\) by the ordinary analytic construction. Impose all old stratum memberships and membership in \(Y'\cap\overline{S_a\cap\Omega}\). These closures are analytic and locally finite. The resulting lower strata and retained outside pieces have the frontier rule: inside \(Y'\) it holds by construction; outside it follows by open locality; a lower closure cannot meet the outside; and an outside closure meeting a lower stratum contains that entire stratum by the imposed membership. The new decomposition refines the old one and is μ on \(X\setminus Y'\).

Start with \(Y=X\). Every nonempty bad set has strictly smaller complex dimension. After at most \(n+1\) rounds the bad set is empty. Each round preserves local finiteness and original cover memberships, so the final complex μ-stratification has the required properties. \(\square\)

This bound counts refinement rounds, not global strata. Even in complex dimension one, a single analytic base can have infinitely many isolated components.

## The closed analytic total conormal

For a complex μ-stratification, put

\[
\Lambda_{\mathcal S}=\bigcup_aT_{S_a}^*X.
\tag{15}
\]

This set is closed. A convergent cotangent sequence has, by local finiteness, a subsequence over one fixed stratum \(S_a\). At a limit in the same stratum ordinary conormal closedness applies. At a limit in another stratum \(S_b\), the frontier rule gives an incident pair. In (2) take the second base constantly equal to that limiting point and the second covector zero. The first covectors converge and are bounded, so the product condition holds; the limit is conormal to \(S_b\).

The same argument puts every ordinary conormal closure into (15). Therefore

\[
\Lambda_{\mathcal S}=\bigcup_a\Sigma_{\overline{S_a}}.
\tag{16}
\]

The family on the right is locally finite because its bases lie in the locally finite stratum closures. Each member is closed analytic, complex-conic and pure Lagrangian of dimension \(n\), by the conormal lesson. Thus (16) is closed analytic, complex-conic and pure Lagrangian; the real singular involutivity theorem applies too. Formula (16) proves analyticity of the total conormal without assuming that an arbitrary closed union of nonclosed analytic pieces is analytic.

If \(\Lambda\) is any closed analytic complex-conic isotropic set, the finite analytic conormal cover supplies closed bases \(X_d\) with \(\Lambda\subset\bigcup_d\Sigma_{X_d}\). Refine the cover consisting of those bases and \(X\), retaining membership compatibility. On a regular point of \(X_d\), its containing stratum lies inside \(X_d\), so its tangent is contained in \(TX_d\). Every ordinary covector conormal to \((X_d)_{\mathrm{reg}}\) is therefore conormal to that stratum. Closedness of (15) includes the whole \(\Sigma_{X_d}\). We have proved

\[
\Lambda\subset\Lambda_{\mathcal S}
\quad\text{for a complex μ-stratification }\mathcal S.
\tag{17}
\]

## A complex-conic bound forces complex-conic microsupport

We need a consequence of the real Lagrangian recovery theorem. Suppose \(A\subset T^*X\) is closed, complex-conic, subanalytic and real-isotropic, and \(S\subset A\) is closed and involutive. Then \(S\) itself is complex-conic.

**Proof.** The full real recovery proof gives more than subanalyticity. Let \(R\) be the real dimension-\(2n\) regular part of \(A\). An involutive subset cannot meet a regular isotropic part of smaller dimension. On \(R\), the closed involutive subset is open by the smooth isotropic-subset theorem. Thus

\[
B=S\cap R\text{ is a union of connected components of }R,
\qquad S=\overline B.
\tag{18}
\]

The latter equality is the no-small-involutive-residue step of the recovery proof, and uses its explicit singular and subanalytic dimension prerequisites.

Complex dilation is a real analytic diffeomorphism preserving \(A\), hence preserving \(R\). The group \(\mathbb C^*\) is path connected. Along any path from 1 to \(\lambda\), the image of a point of \(R\) moves continuously inside \(R\), so remains in its same connected component. Each component, and consequently the union \(B\), is preserved by every complex dilation. Their ambient closure \(S\) is preserved as well. Empty sets and zero covectors cause no exception. \(\square\)

For \(S=\operatorname{SS}(F)\), closedness and involutivity are available. This argument proves the missing invariance step from a bound; it does not infer it just by taking an arbitrary subset.

## Four equivalent geometric tests

**Theorem.** For \(F\in D^b(k_X)\), the following conditions are equivalent:

1. There is a common locally finite analytic-piece cover of \(X\) on which every \(H^j(F)\) is locally constant.
2. \(\operatorname{SS}(F)\) is contained in a closed complex-conic subanalytic real-isotropic subset of \(T^*X\).
3. \(\operatorname{SS}(F)\) is a closed complex analytic conic Lagrangian subset of \(T^*X\), with the real singular involutivity condition included.
4. \(F\) is weakly real constructible and \(\operatorname{SS}(F)\) is complex-conic.

**Proof of 1 implies 2.** Refine the common cover to a compatible complex μ-stratification. Restriction of a locally constant sheaf to any subspace remains locally constant, so all cohomology restrictions to its strata are locally constant. The fixed real μ-stratification criterion gives \(\operatorname{SS}(F)\subset\Lambda_{\mathcal S}\). Formula (16) supplies the required closed complex-conic real-isotropic bound.

**Proof of 2 implies 3.** Apply microsupport involutivity and real Lagrangian recovery inside the given bound. The whole microsupport becomes subanalytic and real Lagrangian. The lemma (18) makes it complex-conic. The analytic Lagrangian closure theorem from the earlier lesson now applies with its actual complex-conicity hypothesis, proving complex analyticity and complex Lagrangian regular tangents. Real singular involutivity already came from the full microsupport theorem. Every premise has now been supplied, including conicity of the microsupport itself.

**Proof of 3 implies 4 and 4 implies 3.** A conic closed complex analytic set is complex-conic, as shown by the holomorphic orbit identity theorem. Its Lagrangian geometry provides a subanalytic real-isotropic bound, so the real criterion gives weak real constructibility. Conversely, weak real constructibility makes microsupport a subanalytic real Lagrangian by the real equivalence. Assumed complex conicity and its involutivity allow the analytic closure theorem to give condition 3.

**Proof of 3 implies 1.** Use (17) to place microsupport inside the total conormal of a complex μ-stratification. The converse direction of the fixed real μ-stratification criterion makes every cohomology sheaf locally constant on its strata. These strata are the required common locally finite analytic cover. The criterion concerns every cohomological degree at once; boundedness remains the original global boundedness hypothesis. \(\square\)

All implications include zero microsupport and the zero object. The isotropy qualification retained in the conormal-cover theorem is exactly what is needed in the proof of 3 implies 1.

## Perfect stalks and the full triangulated categories

Call \(F\) **weakly complex constructible** when it satisfies the four equivalent geometric tests. Call it **complex constructible** when, in addition, every stalk \(F_x\) is a perfect \(k\)-complex: it is isomorphic in the derived category to a bounded complex of finitely generated projective modules.

These are full subcategories of \(D^b(k_X)\), with all ambient morphisms. They are triangulated. To verify the assertion for a cone, take the locally finite analytic covers for two weakly complex constructible objects. Their common intersections are analytic pieces: intersect the closed analytic closures and delete the union of the frontiers, then retain the accessible components. The intersection cover is locally finite, since finitely many members of either original cover occur near a point. A compatible complex μ-stratification makes both objects' cohomology sheaves locally constant on its strata. The triangle microsupport estimate places a cone in the same closed total conormal bound. The four-test theorem proves weak complex constructibility of the cone. Shifts are immediate. For the perfect class, stalks of the triangle are triangles of \(k\)-complexes, and perfect complexes are closed under shifts and cones. This gives the additional stalk condition. No Noetherian assumption is required for this argument.

A constant sheaf on a locally closed analytic piece, extended by zero, is complex constructible: a compatible complex μ-stratification gives constant restrictions of value \(k\) or zero, and those stalks are perfect. Replacing \(k\) by an arbitrary module gives a weakly complex constructible object, with perfection decided separately by that module.

## Why a real triangulation proof cannot be transferred

The real derived comparison used strata given by interiors of simplices of every real dimension. A positive-dimensional complex manifold has even real dimension and complex-invariant tangent planes. The interior of a real one-simplex has real dimension one, so cannot be a positive-dimensional complex analytic stratum. Even a real simplex of even dimension does not become complex analytic merely by parity: its tangent must be a complex subspace, and an arbitrary real triangulation does not impose that condition.

Thus the real proof through common simplicial resolutions does not produce resolutions inside the complex constructible sheaf category. This identifies the precise failure of that proof transfer. It is not, on its own, a proof of a general derived realization comparison or a counterexample to it. The general nonequivalence assertion remains a separate teaching target requiring its own argument. Fixed-stratification realization functors must also be distinguished from the category allowing all analytic stratifications.

## Exercises with complete solutions

### The order of an analytic μ-pair

*Difficulty: Introductory.*

Compare \((M,N)=(\mathbb C,\{0\})\) and \((M,N)=(\{0\},\mathbb C)\). Compute the analytic closure of the bad locus in the latter target base.

**Solution.** The conormal to \(\mathbb C\) is zero, and that to the point is the full vertical fibre. Their full limiting sum is that vertical fibre over zero: a point-side base is always zero, the other must approach it, and the zero-section covector contributes nothing. Every finite vertical covector is realized with both bases zero. For the first pair the target conormal is that same full fibre, so the pair is μ. For the second, a nonzero vertical covector violates the zero-section target at zero. The bad locus and its analytic closure are \(\{0\}\); its neighborhood-good locus is \(\mathbb C\setminus\{0\}\). This pair example is not a partition into disjoint strata.

### Cover membership and a crossing

*Difficulty: Intermediate.*

In \(\mathbb C^2\), refine the cover consisting of the two coordinate axes and \(\mathbb C^2\) into compatible complex μ-strata. Compute its total conormal at the crossing and compare it with the limiting conormal of the union of axes.

**Solution.** Use the four strata: the complement of the axes, the punctured horizontal axis, the punctured vertical axis, and the origin. Each is an analytic piece and smooth of fixed dimension. Every stratum lies inside or outside each axis. The open stratum has zero conormal, so its incident pairs are μ. The punctured axes only approach the point stratum, whose conormal is the whole fibre, so those pairs are μ as well. These are all distinct frontier incidences; each meets an entire lower stratum.

At the origin the total conormal is the whole \(\mathbb C^2\) fibre because of the point stratum. The limiting conormal of the union of axes only has the two lines \(a=0\) or \(b=0\). Thus the total conormal can strictly enlarge the original isotropic set while preserving a valid microsupport bound.

### A bad locus approaching a lower stratum

*Difficulty: Intermediate.*

Take the analytic-piece pair \(M=\{(z,0):z\ne0\}\) and \(N=\mathbb C^2\). Determine its bad base points and their ambient analytic closure. Explain why the closure in (13) must retain points outside the original target portion containing the bad points.

**Solution.** The target conormal is zero. The first conormal over \(M\) has arbitrary \(dy\) covectors; the limiting sum with the zero section is its closure, the full \(dy\) conormal over the entire horizontal axis. Thus the bad locus for this particular target \(N\) is the whole horizontal axis, already closed, including zero through limiting covectors. If instead the target is \(N'=\mathbb C^2\setminus\{0\}\), the same failure points in the target are the punctured horizontal axis. Their ambient closure is the full axis, and the added origin belongs to its frontier rather than to \(N'\). Formula (10) retains it by analytic closure; formula (13) must retain it when making an ambient open good set. Omitting the closure would leave an ambient boundary point which every neighborhood meets bad points. Both targets are smooth analytic pieces, and the target dimension is two, so a horizontal nonzero conormal does violate their zero conormal.

### Closed subsets of invariant sets

*Difficulty: Intermediate.*

Inside a single complex cotangent fibre, take the closed positive real ray. Explain why the elementary set inclusion into a complex-conic fibre does not prove complex conicity, and identify the failed hypothesis needed for (18).

**Solution.** Multiplication by \(i\) takes a nonzero positive real covector off the ray, so the ray is not complex-conic although its containing fibre is. At its zero endpoint its point cone is one real ray, while its two-set cone is the full real line. The real smooth fibre is a Lagrangian plane in the real cotangent manifold of \(\mathbb C\), and its closed ray is not open in that plane. Involutivity fails: annihilators of the ray's real line would force all symplectically orthogonal directions of that line into the point cone, which has only one real dimension and one sign. Thus the involutive-subset hypothesis needed for (18) is absent. Ordinary closedness and conicity of the bound cannot replace it.

### Weak complex constructibility without perfect coefficients

*Difficulty: Introductory.*

Over \(k=\mathbb Z\), let \(M=\bigoplus_{r\ge1}\mathbb Z\), and take the constant sheaf \(M_X\) on a nonempty complex manifold. Determine its weak and perfect complex constructibility.

**Solution.** The one-member cover \(X\) makes its only cohomology sheaf locally constant, so it is weakly complex constructible. Every stalk is \(M\) in degree zero. A bounded complex of finitely generated projective abelian groups has finitely generated cohomology, whereas \(M\) is not finitely generated. Therefore that stalk is not perfect, and the sheaf is not complex constructible in the perfect sense. Its geometric microsupport, the zero section, supplies no missing finite-generation condition.

### A real boundary fails the complex test

*Difficulty: Intermediate.*

In \(X=\mathbb C\), let \(F=\mathbb Z_{\mathbb R}\) be the constant sheaf on the closed real axis extended by zero. Use its conormal microsupport to decide its real and complex constructibility.

**Solution.** The real axis is a closed real analytic submanifold, and the sheaf has perfect stalks \(\mathbb Z\) on it and zero elsewhere. A compatible real μ-stratification makes it real constructible. Its microsupport is the real conormal \(\mathbb R\,dy\) over \(y=0\). Under the real covector identification, \(b\,dy\) corresponds to \(-ib\,dz\), so those nonzero complex covectors form the imaginary real line in each fibre. Multiplication by \(i\) moves them to real nonzero covectors, which are absent. Microsupport is not complex-conic. Condition 4 therefore fails, and the object is not weakly complex constructible, despite its perfect stalks.

### A puncture keeps perfect stalks and a conormal bound

*Difficulty: Intermediate.*

Let \(j:\mathbb C^*\hookrightarrow\mathbb C\) and \(F=j_!\mathbb Z_{\mathbb C^*}\). Give a common analytic μ-stratification, a closed total conormal bound, and the stalk perfection check. Does the criterion require that the bound equal the microsupport?

**Solution.** Take \(\mathbb C^*\) and \(\{0\}\). Both are analytic pieces; the open piece only approaches the point, and that target conormal is full, so this is μ. The total conormal is the zero section together with the full fibre at zero. Cohomology restriction to the open stratum is constant \(\mathbb Z\), and to the point is zero because extension by zero has zero boundary stalk. The fixed criterion bounds microsupport by that closed analytic conormal union. Both kinds of stalks are perfect, so the object is complex constructible. Equality of the bound with microsupport is not needed for this argument; the four-test theorem proves that the actual microsupport has the claimed analytic geometry separately.

### Taking a cone with torsion coefficients

*Difficulty: Introductory.*

On a complex manifold, form the cone \(C\) of multiplication by \(m\ne0\) on \(\mathbb Z_X\), using a triangle \(\mathbb Z_X\xrightarrow{m}\mathbb Z_X\to C\to\mathbb Z_X[1]\). Determine its degrees and verify complex constructibility without imposing projectivity on its degree-zero cohomology.

**Solution.** The cone has the two-term stalk complex \([\mathbb Z\xrightarrow{m}\mathbb Z]\) in degrees \(-1,0\). Injectivity of multiplication by \(m\) gives only \(H^0=\mathbb Z/m\), locally constant. The one analytic stratum \(X\) verifies the geometric condition. The displayed finite free complex is a perfect representative, so every stalk is perfect even though its torsion cohomology module need not be projective. The category condition concerns a perfect complex, not projectivity of each individual cohomology module.

### Parity is not a complex triangulation

*Difficulty: Advanced.*

Explain why a real one-simplex cannot be a complex stratum. In \(\mathbb C^2\), also check that an open real two-dimensional patch in the plane \(\{y_1=y_2=0\}\) is not a complex stratum even though its dimension is even. State exactly what these examples prove about derived comparisons.

**Solution.** A nonempty real one-simplex interior has real dimension one; a complex manifold has real dimension twice its complex dimension, so the simplex cannot be a positive-dimensional complex manifold. For the two-dimensional plane, its real tangent is spanned by \(\partial_{x_1},\partial_{x_2}\), while multiplication by \(i\) gives \(\partial_{y_1},\partial_{y_2}\), outside that tangent. Thus it is not a complex submanifold despite even dimension. These facts prevent a general real simplicial resolution argument from staying inside the analytic-stratum constructible category. They prove failure of that particular proof transfer. They do not alone prove nonequivalence of the unrestricted complex derived realization, and do not license replacing it by a comparison for one fixed stratification.

## Remaining dependencies and targets

The analytic bad-set construction, ordinary and microlocal refinements, total conormal, conicity-recovery lemma, all four geometric criteria and triangulated-category proof are complete relative to the specified current geometry and microsupport prerequisites. The general complex derived realization phenomenon, every complex weak/perfect functor application and the nonproper complex-curve cutoff theorem remain further substantive targets; none follows merely from a real triangulation.

## Readable source and dependency account

An invariant isotropic containing set does not make all its subsets invariant. The proof uses the involutive microsupport and its dense regular components, then takes ambient closure; connectedness of the complex dilation group preserves those components. The real cotangent convention here is the real part, whereas the 1985 text uses twice the real part. A positive scalar change does not alter conicity, but the written symplectic convention is kept throughout. The primitive analytic refinement and closure inputs remain explicit. The real triangulation proof is not transferred to a complex analytic category.

Checked editions: [Kashiwara–Schapira, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf); [Schapira, sheaf lecture notes](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf); [Schapira, microlocal review (2016)](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf). The locators above identify the passages used; these links do not claim that all three works prove every statement or every prerequisite of this lesson. Original programme exposition remains CC0; the human works retain their own rights.
