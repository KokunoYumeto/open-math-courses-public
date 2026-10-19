# Intermediate extensions and intersection complexes

*AI-generated exposition by GPT-6 Astra (OpenAI), October 2026. Public domain (CC0).*

An intersection complex can be calculated by answering a local question: after extending across a stratum, which stalk degrees must be removed? The answer is one degree stricter than perversity alone. We first derive that cutoff and its costalk counterpart. We then use them to recognize simple objects and to calculate four singular varieties. The examples distinguish a perverse constant sheaf from an intersection complex, and a singular variety from one that fails the cohomological smoothness test.

Use the constructible categories of [Constructible complexes on algebraic varieties](constructible-complexes-on-algebraic-varieties.md) and the t-structure of [The perverse t-structure](the-perverse-t-structure.md). Coefficients are a field; the classical examples use a characteristic-zero field \(\Lambda\). In the étale setting retain the coefficient and finiteness hypotheses of the preceding lessons. Ordinary shifts satisfy \(\mathcal H^a(K[b])=\mathcal H^{a+b}(K)\). A smooth stratum of complex dimension \(s\) places its local systems in perverse degree zero by shifting them by \([s]\).

## 1. Construct the extension one stratum at a time

Let \(j:V\hookrightarrow W\) have closed complement \(i:F\hookrightarrow W\). Suppose \(F\) is a disjoint union of smooth strata of dimension \(s\), and the complexes under discussion are locally constant on those strata. Start with a perverse object \(A\) on \(V\). The earlier [boundary construction](gluing-t-structures.md#3-cut-away-the-unwanted-boundary-degrees) forms

\[
P=\operatorname{Fib}\left(Rj_*A\longrightarrow
i_*{}^p\tau^{\geq0}i^*Rj_*A\right).
\tag{1.1}
\]

Here the arrow is restriction followed by truncation in the closed perverse category. Put \(B=i^*Rj_*A\). Applying the open restriction, closed restriction and closed exceptional restriction gives, respectively,

\[
j^*P=A,\qquad
i^*P={}^p\tau^{\leq-1}B,\qquad
i^!P=({}^p\tau^{\geq0}B)[-1].
\tag{1.2}
\]

For the last equality use \(i^!Rj_*A=0\) in the triangle (1.1). The shift \([-1]\) raises the lower cohomological degree by one. Thus the last two terms satisfy the strict perverse bounds \(\leq-1\) and \(\geq1\). Together with the perverse open restriction, the gluing tests show that \(P\) is perverse.

These inequalities have a precise meaning. For any perverse \(Q\), adjunction and truncation give

\[
\begin{aligned}
\operatorname{Hom}(Q,i_*E)&=\operatorname{Hom}({}^pH^0i^*Q,E),\\
\operatorname{Hom}(i_*E,Q)&=\operatorname{Hom}(E,{}^pH^0i^!Q)
\end{aligned}
\tag{1.3}
\]

for every perverse \(E\) on \(F\). A nonzero map in either line has a nonzero boundary-supported image. Conversely, if the indicated degree-zero object is nonzero, its identity supplies such a map. Hence (1.2) says exactly that \(P\) has no nonzero boundary quotient and no nonzero boundary subobject. The construction in the earlier lesson proves that there is a unique such extension with its given identification on \(V\). It is denoted \(j_{!*}A\). Its equivalent image formula is

\[
j_{!*}A=\operatorname{im}_{\operatorname{Perv}(W)}
\left({}^pH^0j_!A\longrightarrow{}^pH^0Rj_*A\right).
\tag{1.4}
\]

In particular the image is taken in the perverse heart, rather than degree by degree in ordinary sheaves.

We can make (1.1) an ordinary truncation in a useful situation. Suppose \(A\in D^{\leq-s-1}(V)\). Write

\[
Q=\tau^{\leq-s-1}Rj_*A,\qquad
C=\tau^{\geq-s}Rj_*A.
\]

The restriction of \(C\) to \(V\) vanishes, since restriction is ordinary t-exact and \(A\) already lies below the cutoff. Localization gives \(C=i_*i^*C=i_*\tau^{\geq-s}B\). On the locally constant category of \(F\), perverse degree zero is ordinary degree \(-s\), so this is \(i_*{}^p\tau^{\geq0}B\). The truncation triangle for \(Q\) is therefore the actual fibre triangle (1.1), with the same restriction and truncation map. We have proved

\[
j_{!*}A=\tau^{\leq-s-1}Rj_*A,
\quad i^*j_{!*}A=\tau^{\leq-s-1}B,
\quad i^!j_{!*}A=(\tau^{\geq-s}B)[-1].
\tag{1.5}
\]

### Deligne's successive truncations

Let \(X\) be pure of dimension \(d\), and choose a compatible finite stratification with the frontier condition. Let \(U\) be the smooth dense union of its top-dimensional strata and let \(L\) be a local system there. Denote by \(V_s\) the union of strata of dimension at least \(s\). Then \(V_d=U\), \(V_0=X\), and \(F_s=V_s\setminus V_{s+1}\) is closed in \(V_s\) and consists of disjoint smooth \(s\)-dimensional strata. If there are none of that dimension, simply omit that step. For \(j_s:V_{s+1}\hookrightarrow V_s\), form

\[
K_d=L[d],\qquad K_s=\tau^{\leq-s-1}Rj_{s*}K_{s+1}.
\tag{1.6}
\]

Every truncation here is ordinary. We prove that these are successive intermediate extensions. The initial object is perverse and concentrated in degree \(-d\). If \(K_{s+1}\) is perverse, its restriction to any stratum of dimension \(t\geq s+1\) has ordinary cohomology only in degrees at most \(-t\). Stalk detection therefore gives \(K_{s+1}\in D^{\leq-s-1}\). Formula (1.5) applies, showing both that \(K_s\) is perverse and that \(K_s=j_{s!*}K_{s+1}\). This proves the induction, including the required bound for its next step.

For composable open immersions \(U\xrightarrow{k}V\xrightarrow{j}X\), intermediate extension satisfies

\[
(jk)_{!*}A=j_{!*}k_{!*}A.
\tag{1.7}
\]

Indeed a subobject of the right side supported outside \(U\) restricts to a boundary subobject of \(k_{!*}A\) on \(V\), hence restricts to zero. It is then supported outside \(V\), where \(j_{!*}\) excludes it. Exact restriction gives the identical argument for a quotient. Both exclusion properties and the specified open restriction determine the extension. Thus (1.6) ends at \((U\hookrightarrow X)_{!*}L[d]\). This is Deligne's formula, proved from the closed truncation rather than assumed as an additional construction.

## 2. Support, simple objects and the dual coefficient system

For an irreducible reduced closed subvariety \(Z\subset X\) of dimension \(d\), choose a smooth connected dense open \(j:U\hookrightarrow Z\), a finite-rank local system \(L\) on \(U\), and the closed inclusion \(b:Z\hookrightarrow X\). Define

\[
\operatorname{IC}_X(Z,L)=b_*j_{!*}L[d].
\tag{2.1}
\]

The dimension is that of the support \(Z\). On a pure-dimensional variety with several components, its constant intersection complex is the direct sum of the constant intersection complexes of those components. For components of different dimensions, each retains its own shift.

Shrinking \(U\) does not change (2.1) when \(L\) is restricted from the larger open. The [smooth local-system argument](the-perverse-t-structure.md#5-finite-chains-of-subobjects) proves that \(L[d]\) has no perverse subobject or quotient supported on a proper closed subset of the smooth \(U\). Hence it is itself the intermediate extension from the smaller open, and (1.7) applies. Refining the compatible stratification has the same consequence. The uniqueness assertion always includes the chosen identification on a common dense open.

**Simple-object theorem.** With field coefficients, the simple perverse objects are exactly the objects (2.1) with \(L\) irreducible.

First let \(L\) be irreducible. On its smooth connected open, the local-subsystem criterion from the preceding lesson says that \(L[d]\) is simple. If \(B\) is a subobject of \(j_{!*}L[d]\), its restriction is either zero or all of \(L[d]\). In the first case \(B\) is a forbidden boundary subobject. In the second case its quotient is a forbidden boundary quotient, so \(B\) is the whole object. Closed pushforward preserves simplicity, proving this direction.

Conversely, let \(P\ne0\) be simple. Replace its ambient variety by the closed support, using localization and the fully faithful closed pushforward. Choose an adapted stratification and the nonempty open union of the top-dimensional strata of that support. Its restriction \(j^*P\) is a direct sum of shifted local systems. It is simple: a proper nonzero perverse subobject \(A\subset j^*P\) would, by the heart adjunction, give \({}^pH^0j_!A\to P\) with nonzero image. Simplicity forces that image to be \(P\), while exact restriction makes its image equal to the proper subobject \(A\), a contradiction. A simple object on a disjoint union occupies a single connected component, with an irreducible local system on it. A boundary subobject or quotient of \(P\) is impossible by simplicity and its nonzero open restriction. Thus \(P\) is the intermediate extension of this irreducible shifted local system. Its closed support is the irreducible closure \(Z\) of that component, giving (2.1).

The support is intrinsic to \(P\), and restriction to a common smooth dense open recovers \(L\). An isomorphism of those restrictions extends uniquely by full faithfulness of intermediate extension. This proves the asserted uniqueness of the pair, with the local system understood up to shrinking its domain. No exactness of the functor \(j_{!*}\) on arbitrary short exact sequences was used.

The field hypothesis matters. On a point, \(\mathbf Z_\ell\) has the strictly descending subobjects \(\ell^n\mathbf Z_\ell\), so the finite-length statement for field-valued perverse sheaves cannot be transferred to integral coefficients. This is the obstruction singled out by BBD, 4.0(b), in its freely readable edition.

On a smooth \(d\)-dimensional support, ordinary duality gives

\[
D(L[d])=L^\vee[d]\quad\hbox{classically},\qquad
D(L[d])=L^\vee(d)[d]\quad\hbox{étale-locally}.
\tag{2.2}
\]

Duality on the perverse heart exchanges boundary subobjects and boundary quotients. It therefore carries the defining extension to the unique extension of the dual system in (2.2). Duality also commutes with the proper closed pushforward. Consequently

\[
D_X\operatorname{IC}_X(Z,L)=
\begin{cases}
\operatorname{IC}_X(Z,L^\vee),&\text{classically},\\
\operatorname{IC}_X(Z,L^\vee(d)),&\text{in the étale setting}.
\end{cases}
\tag{2.3}
\]

In particular our constant intersection complex is classically self-dual. Étale duality twists it by \((d)\). Our normalization is \(L[d]\), with no weight-normalizing twist. For comparison, the free Braverman–Finkelberg–Gaitsgory–Mirković paper chooses a square root of the finite-field cardinality and uses \(\Lambda(d/2)[d]\) on a smooth variety. Such a convention does not remove the twist from (2.3) with our normalization.

## 3. Global degrees and the cohomological smoothness test

For pure \(d\)-dimensional \(X\), set

\[
IH^r(X,L)=H^{r-d}(X,\operatorname{IC}(X,L)),\qquad
IH_c^r(X,L)=H_c^{r-d}(X,\operatorname{IC}(X,L)).
\tag{3.1}
\]

The same definition on a support uses its dimension and its own cohomology. For a smooth variety this recovers ordinary cohomology, because its intersection complex is \(L[d]\). Under the constructible finiteness and Verdier-duality hypotheses, (2.3) gives

\[
IH^r(X,L)^\vee=IH_c^{2d-r}(X,L^\vee).
\tag{3.2}
\]

To check both indices, the dual of \(H^{r-d}(X,K)\) is \(H_c^{d-r}(X,D_XK)\), and \(d-r=(2d-r)-d\). For geometric étale cohomology the coefficient on the right is \(L^\vee(d)\); equivalently, pairing with \(L^\vee\) takes values in \(\Lambda(-d)\). Over a finite field this statement respects Frobenius on geometric cohomology. It makes no assertion about the additional Galois-cohomology step for arithmetic cohomology. When \(X\) is proper, compact supports may be omitted, giving intersection-cohomology Poincaré duality.

Assume now that \(X\) is a classical oriented \(\Lambda\)-cohomology manifold of real dimension \(2d\). The local condition is

\[
H^a(B,B\setminus\{x\};\Lambda)=
\begin{cases}\Lambda,&a=2d,\\0,&a\ne2d,
\end{cases}
\tag{3.3}
\]

on sufficiently small neighborhoods, with compatible generators giving the complex orientation. [Appendix G.1–G.2](#appendix-g-local-orientations-and-the-integral-quotient-calculation) proves that these local groups and their compatible orientation generators identify the dualizing complex with \(\Lambda_X[2d]\), including the restriction maps. We call this the rational-smoothness condition when \(\Lambda\) has characteristic zero. It is a cohomological condition and does not require the variety to be smooth.

Put \(P=\Lambda_X[d]\). For a smooth stratum \(a:S\hookrightarrow X\) of dimension \(s\), its stalk restriction is \(\Lambda_S[d]\). Since \(D_XP=P\), dual exchange gives

\[
a^!P=D_Sa^*P=\Lambda_S[2s-d].
\tag{3.4}
\]

The two nonzero ordinary degrees are \(-d\) and \(d-2s\). They satisfy the perverse bounds at dimension \(s\). If \(s<d\), they satisfy the strict bounds \(-d\leq-s-1\) and \(d-2s\geq-s+1\). Thus \(P\) has no boundary subobjects or quotients and extends the constant system on the smooth locus. We obtain

\[
\operatorname{IC}(X,\Lambda)=\Lambda_X[d].
\tag{3.5}
\]

The étale counterpart assumes cohomological smoothness with the actual oriented dualizing complex \(\Lambda_X(d)[2d]\). Then (3.4) becomes \(\Lambda_S(s-d)[2s-d]\), with the same degree inequalities. That hypothesis requires its own étale proof; a classical link calculation does not establish it.

### The comparison with allowable chains

The retained Goresky–MacPherson comparison has the following normalization. Give a pure complex algebraic variety a finite algebraic Whitney stratification compatible with the chosen dense open and coefficient system, using Lesson 1, K.6. A stratum of complex codimension \(r\) has real codimension \(2r\), and middle perversity is \(\overline m(2r)=r-1\). The theorem identifies its singular middle-perversity intersection-chain sheaf, normalized to restrict to \(L[2d]\), with \(\operatorname{IC}(X,L)[d]\). Therefore our unshifted cohomological complex is \(\operatorname{IC}(X,L)[-d]\). In particular its degree-\(r\) hypercohomology is (3.1). In the chain convention this corresponds to locally finite intersection homology in degree \(2d-r\); compact supports correspond to finite chains. Appendix E proves this singular-chain comparison from Whitney neighborhoods and compact constructible cohomology. Appendix H constructs a global compatible filtered model from a finite affine atlas and the earlier Euclidean relative triangulation theorem; Appendix F identifies its simplicial and PL chain conventions with these same groups.

There is an elementary uniqueness step behind that theorem. If a candidate complex starts with \(L[2d]\), has no stalk groups above \(\overline m(2r)-2d\) on the next real-codimension-\(2r\) stratum, and its attaching map is an isomorphism through that degree, the natural map to the truncated direct image is an isomorphism on every stalk. It is therefore an isomorphism of complexes. Iterating determines the candidate uniquely. Shifting by \([-d]\) changes its cutoff to
\((r-1)-2d+d=-\dim S-1\), exactly (1.6).

The coefficient complex, allowable subdivision, excision, cone calculations and chain-sheaf normalization are constructed in [Appendix B](#appendix-b-allowable-chains-subdivision-and-cones). [Appendix C](#appendix-c-product-neighborhoods-and-sections-of-the-chain-sheaf) supplies product-neighborhood formulas, local constancy along strata, the identification of ordinary sheaf sections with chains, and homotopical fineness. [Appendix D](#appendix-d-derived-sections-of-the-chain-sheaf) identifies derived global and compactly supported sections with the respective chain complexes, using a finite-length resolution for the initially unbounded complex. [Appendix E](#appendix-e-finite-links-and-the-attaching-morphism) proves compact-link finiteness, bounded finite-rank constructibility, and the actual attaching-map isomorphism for the Whitney models of complex varieties as well as the conically stratified triangulated models. [Appendix F](#appendix-f-simplicial-chains-and-pl-refinement) proves agreement with simplicial and PL intersection chains through the actual affine inclusion and subdivision maps, for both support conventions. The four computations below use their stated local sheaf calculations.

## 4. Two local calculations used by the examples

### The link determines the retained stalk degrees

Let an affine complex cone \(X\) of dimension \(d\) be smooth away from its vertex \(o\), and let \(M\) be its link. Positive radial scaling gives \(X\setminus\{o\}\simeq(0,\infty)\times M\). Its restriction to a small punctured conical neighborhood has the same homotopy type and the same restriction map on cohomology. The sheaf–singular comparison and radial attaching calculation are proved in [Lesson 1, Appendix C](constructible-complexes-on-algebraic-varieties.md#appendix-c-sheaf-cohomology-of-the-cone-and-local-orientation-groups). With \(j\) the punctured inclusion and \(i\) the vertex,

\[
i^*Rj_*\Lambda[d]=R\Gamma(M,\Lambda)[d],\qquad
\operatorname{IC}(X,\Lambda)=\tau^{\leq-1}Rj_*\Lambda[d].
\tag{4.1}
\]

The second equality is the single boundary step in (1.6). Thus a link class in degree \(q\) survives in the intersection stalk exactly when \(q-d\leq-1\), or \(q<d\). The global fibre triangle has last term \(i_*\tau^{\geq0}R\Gamma(M,\Lambda)[d]\). Since the punctured cone-to-neighborhood restriction is the radial cohomology isomorphism, its global sections give the same truncation fibre. Hence

\[
IH^q(X,\Lambda)=
\begin{cases}H^q(M,\Lambda),&0\leq q<d,\\0,&q<0\text{ or }q\geq d.
\end{cases}
\tag{4.2}
\]

Self-duality gives the vertex costalk by dualizing the vertex stalk and reversing degrees. Formula (3.2) determines the compactly supported global groups. Notice that the argument used the restriction map in the fibre triangle; contractibility of the cone alone would compute only its ordinary cohomology.

### Finite coverings and averaging

For a finite regular covering \(p:\widetilde M\to M\) with deck group \(G\), each singular simplex downstairs has exactly \(|G|\) lifts. A lift is determined by the point above its first vertex: lift paths by subdividing them into evenly covered neighborhoods, and lift a homotopy by subdividing its parameter square. A simplex contracts to that vertex, so this gives a lift on the whole simplex independent of the paths. Define a chain map \(t:C_*(M)\to C_*(\widetilde M)\) by summing all lifts. Taking the faces permutes the complete list of lifts, so \(\partial t=t\partial\). On chains,

\[
p_*t=|G|\,1,\qquad tp_*=\sum_{g\in G}g_*.
\tag{4.3}
\]

Precomposing cochains gives \(p^*:H^*(M,\Lambda)\to H^*(\widetilde M,\Lambda)\) and \(t^*\) in the other direction with the same identities. If \(|G|\) is invertible in \(\Lambda\), the first identity proves injectivity of \(p^*\). Its image is invariant. Conversely an invariant class \(a\) equals \(p^*(|G|^{-1}t^*a)\) by the second identity. This proves the invariant-cohomology formula used below, with its maps and its coefficient restriction.

## 5. Four singular varieties

### The nodal cubic: two branches give two stalk values

Take \(X:\ y^2z=x^2(x+z)\). The map

\[
\nu:\mathbf P^1\longrightarrow X,\qquad
[s:t]\longmapsto[s(t^2-s^2):t(t^2-s^2):s^3]
\tag{5.1}
\]

has no simultaneous zero among its coordinates. Substitution verifies the equation, and \(t/s=y/x\) is its inverse on the nonnodal affine part. The points \([1:1]\) and \([1:-1]\) map to the node \(o\), while \([0:1]\) maps to the smooth point at infinity. The normalization and actual branch arguments, including the finite-map prerequisites, are supplied in [Lesson 1, Appendix L](constructible-complexes-on-algebraic-varieties.md#appendix-l-nodes-normalization-and-the-actual-branches).

Proper base change for the finite fibres gives \(R\nu_*\Lambda=\nu_*\Lambda\). The object \(P=\nu_*\Lambda[1]\) has vertex stalk \(\Lambda^2[1]\). Smooth curve duality and proper duality make it self-dual, so its vertex costalk is \((\Lambda^2)^\vee[-1]\), concentrated in degree \(1\). These strict degrees and its smooth-open restriction prove

\[
\operatorname{IC}(X,\Lambda)=\nu_*\Lambda[1].
\tag{5.2}
\]

The projective line is a two-sphere: on its affine chart, stereographic coordinates send \(z\) to \((2\Re z,2\Im z,|z|^2-1)/(1+|z|^2)\), and infinity maps to the remaining pole. The sphere calculation of Lesson 1 gives intersection Betti numbers \(1,0,1\). The ordinary sheaf sequence is

\[
0\longrightarrow\Lambda_X\longrightarrow\nu_*\Lambda
\xrightarrow{\text{difference at the two branches}}i_*\Lambda
\longrightarrow0.
\tag{5.3}
\]

It is exact on every stalk: at the node it is the diagonal inclusion followed by subtraction, and off the node the last stalk is zero. Global constants have equal branch values, so their difference is zero. The long exact sequence then gives ordinary Betti numbers \(1,1,1\). Intersection cohomology does not retain the degree-one class introduced by joining the two normalization points.

### A singular quotient that passes the smoothness test

The invariants of the sign action on \(\mathbf C^2\) are generated by \(a=z_1^2,b=z_1z_2,c=z_2^2\), with relation \(ac=b^2\). Indeed every invariant monomial has even total degree and is a product of these generators; reducing powers of \(b\) by the relation leaves distinct monomials in \(z_1,z_2\). Thus \(X=\mathbf C^2/\{\pm1\}\) is the quadric surface, singular only at its vertex. Its link is \(S^3/\{\pm1\}=\mathbf{RP}^3\).

The deck map extends to the linear map \(-1\) on \(\mathbf R^4\), of determinant \(+1\). It preserves the ball orientation and hence the boundary orientation on \(S^3\). Formula (4.3) shows that the link has \(\Lambda\) in degrees \(0,3\) and zero in all other degrees. Relative cohomology of a cone and its puncture shifts reduced link cohomology up by one, so its local relative group is \(\Lambda\) only in degree \(4\). Smooth points have the same oriented local groups. [Appendix G.3](#g-3-compatibility-of-the-quotient-orientation) proves compatibility across the vertex using proper pullback and the two positive point-support generators above every regular point. Thus (3.3) holds, and

\[
\operatorname{IC}(X,\Lambda)=\Lambda_X[2],\qquad
IH^0(X)=\Lambda,\qquad IH_c^4(X)=\Lambda,
\tag{5.4}
\]

with other global groups zero. The vertex stalk is in degree \(-2\) and costalk in degree \(2\).

The integral obstruction is visible without averaging. [Appendix G.4–G.5](#g-4-integral-cellular-chains-and-cochains) constructs the cell filtration of \(\mathbf{RP}^3\), proves its singular homology and cohomology comparisons, and computes the attaching degrees. There is one cell in each dimension \(0,1,2,3\), with integral differentials \(d_3=0,d_2=2,d_1=0\). The corresponding cochain complex gives \(H^2(\mathbf{RP}^3,\mathbf Z)=\mathbf Z/2\). The cone pair sequence therefore gives a vertex relative group \(\mathbf Z/2\) in degree \(3\), so the integral cohomology-manifold assertion fails. This identifies the torsion removed by the characteristic-zero calculation.

### The elliptic cone: a perverse constant sheaf can still be too large

Let \(C\) be a smooth embedded projective elliptic curve, with embedding line bundle \(A\) of degree \(e>0\), and let \(X\) be its affine cone. Sending a nonzero vector on a projective line to its direction identifies the punctured cone with \((A^{-1})^\times\). The link is the unit circle bundle of \(A^{-1}\). Write \(\eta\) for its positive base degree-two generator. The Euler class is \(-e\eta\).

The required circle-bundle sequence is proved in [Lesson 1, Appendix D](constructible-complexes-on-algebraic-varieties.md#appendix-d-integral-thom-classes-and-the-circle-bundle-sequence): it is the pair sequence for the line bundle and its nonzero part, transported through the oriented Thom isomorphism. The Euler map is cup product with the zero-section pullback of the Thom class, and dualizing the line reverses its sign. Here it reads

\[
\cdots\to H^{q-2}(C)\xrightarrow{-e\eta\smile}H^q(C)
\to H^q(M)\to H^{q-1}(C)\xrightarrow{-e\eta\smile}H^{q+1}(C)\to\cdots.
\tag{5.5}
\]

For every smooth projective elliptic curve the base groups are \(\Lambda,\Lambda^2,\Lambda\) in degrees \(0,1,2\). [Appendix A](#appendix-a-elliptic-curves-and-the-degree-of-an-embedding) proves this by constructing a degree-three plane embedding, then computes the Euler class of the original embedding line bundle from its own zero divisor. The original embedding may have any projective dimension and any very ample line bundle; its degree \(e\) need not be three.

Over the characteristic-zero field \(\Lambda\), \(-e:H^0(C)\to H^2(C)\) is invertible. Exactness of (5.5) gives link ranks \(1,2,2,1\) in degrees \(0,1,2,3\): the degree-one map from \(H^1(C)\) is an isomorphism, as is the degree-two map to \(H^1(C)\); the degree-three map to \(H^2(C)\) is an isomorphism. Formula (4.1) keeps only the first two link degrees. Thus the vertex stalk has

\[
\mathcal H^{-2}(i^*\operatorname{IC})=\Lambda,\qquad
\mathcal H^{-1}(i^*\operatorname{IC})=\Lambda^2,
\tag{5.6}
\]

and no other groups. Its costalk has ranks two and one in degrees \(1,2\). The smooth-open complex is \(\Lambda[2]\). The global answers are

\[
IH^0(X)=\Lambda,\quad IH^1(X)=\Lambda^2,\qquad
IH_c^3(X)=\Lambda^2,\quad IH_c^4(X)=\Lambda,
\tag{5.7}
\]

with all unlisted groups zero.

The constant complex \(\Lambda_X[2]\) is perverse here. Its point stalk has degree \(-2\); its costalk is obtained from the reduced cohomology of the connected link, shifted first up by one for relative cohomology and then by \([2]\). Its possible degrees are \(0,1,2\), which pass the point costalk test. The map from this constant complex to \(Rj_*\Lambda[2]\) factors through the truncation (4.1). On the vertex it is the identity on the degree-\(-2\) group. Its cone is therefore \(i_*\Lambda^2[1]\). The rotated triangle gives the perverse exact sequence

\[
0\longrightarrow i_*\Lambda^2\longrightarrow\Lambda_X[2]
\longrightarrow\operatorname{IC}(X,\Lambda)\longrightarrow0.
\tag{5.8}
\]

It cannot split: the stalk of a split middle object would have a nonzero degree-zero group from \(i_*\Lambda^2\), whereas the constant stalk has only degree \(-2\). Thus boundary subobjects, rather than failure of perversity, explain the difference between the two complexes.

### The threefold quadric: compare a link with a resolution

Write the threefold \(xy=zw\) as the variety of rank-at-most-one matrices
\(M=\left(\begin{smallmatrix}x&z\\w&y\end{smallmatrix}\right)\). Its projectivization is the Segre surface \(B=\mathbf P^1\times\mathbf P^1\), and the punctured cone is \(\mathcal O_B(-1,-1)^\times\). The two factors are spheres. Their cell products have one cell in degrees \(0,4\) and two in degree \(2\), with zero differentials. The singular cross and cup products constructed in Lesson 1, Appendix D identify the ring as

\[
H^*(B,\Lambda)=\Lambda[a,b]/(a^2,b^2),\qquad |a|=|b|=2.
\tag{5.9}
\]

Here \(a,b\) are pulled back from the oriented factors and \(ab\) evaluates to one on their product. The Euler class of the link line is \(-(a+b)\): restricting it to either factor gives the tautological line of Euler number \(-1\), and these two restrictions determine a degree-two class. Cup product takes \(1\) to \(-(a+b)\) and \(\alpha a+\beta b\) to \(-(\alpha+\beta)ab\). The kernel of the latter map is \(\Lambda(a-b)\), and it is surjective. The Gysin sequence gives link rank one in degrees \(0,2,3,5\), with all other groups zero.

Cutting at link degree \(d=3\) gives vertex stalk rank one in degrees \(-3,-1\), and dual costalk rank one in degrees \(1,3\). Globally,

\[
IH^0(X)=IH^2(X)=\Lambda,\qquad
IH_c^4(X)=IH_c^6(X)=\Lambda,
\tag{5.10}
\]

with all other groups zero. There is also an explicit geometric realization of the whole complex. Set

\[
Y=\{(M,\ell)\in X\times\mathbf P^1:\operatorname{im}M\subset\ell\},
\qquad \pi:Y\to X.
\tag{5.11}
\]

For a fixed line \(\ell\), the two matrix columns are arbitrary vectors in that line; therefore \(Y\) is the total space of \(\mathcal O_{\mathbf P^1}(-1)^{\oplus2}\), smooth of dimension three. The incidence equations make it closed in \(X\times\mathbf P^1\), so its projection is proper. A nonzero rank-one matrix determines its image line, and the usual nonzero-column charts give the regular inverse there. Only the origin has a larger fibre, namely \(\mathbf P^1\). This locus has codimension three, strictly greater than twice its fibre dimension one, so \(\pi\) is small.

For \(P=R\pi_*\Lambda_Y[3]\), proper base change gives \(i^*P=R\Gamma(\mathbf P^1,\Lambda)[3]\), with exactly the stalk degrees \(-3,-1\) just calculated. Proper duality makes \(P\) self-dual, giving costalk degrees \(1,3\). These strict boundary tests and its smooth-open restriction show directly that

\[
R\pi_*\Lambda_Y[3]=\operatorname{IC}(X,\Lambda).
\tag{5.12}
\]

This proof does not invoke the general small-map theorem. Fibre scaling retracts \(Y\) to its zero section \(\mathbf P^1\), so its global cohomology yields (5.10) a second way. The general smallness criterion belongs to the later semismall-map lesson.

## 6. Exercises with complete solutions

**Exercise 1 (easy).** Determine the constant intersection complex on a smooth pure \(d\)-dimensional variety, and the version with a local system \(L\).

**Solution.** There is no boundary when the chosen smooth dense open is the whole variety. The two heart functors in (1.4) are both the identity, as is their comparison. Its image is therefore \(L[d]\). Taking \(L=\Lambda\) gives \(\Lambda[d]\). If the variety is connected, the object is simple exactly when \(L\) is irreducible, by the sub-local-system test; simplicity is not needed for this calculation.

**Exercise 2 (easy).** Compute the intersection complex of the irreducible nodal cubic and compare its ordinary and intersection Betti numbers.

**Solution.** The normalization has one point above each smooth point and two above the node. Push forward the shifted constant system from \(\mathbf P^1\). Its stalks at the node have only degree \(-1\) and rank two; proper duality gives only degree \(1\) and rank two in its costalks. Hence it passes the strict boundary tests and equals the intersection complex. Global sections give \(H^*(\mathbf P^1)\), of ranks \(1,0,1\). For ordinary cohomology, the stalk-exact sequence (5.3) has a zero map from global constants to the branch-difference value. The connecting map from that value contributes one copy of \(\Lambda\) to \(H^1(X)\). The remaining groups agree with the normalization in degrees zero and two. Thus ordinary ranks are \(1,1,1\), and all groups outside these ranges vanish.

**Exercise 3 (medium).** Use the link Gysin sequence to compute the intersection stalk, costalk and global groups of the elliptic cone.

**Solution.** Appendix A proves that the Euler map is the nonzero scalar \(-e\) from base degree zero to degree two for the given embedding. Exactness leaves link degree-one and degree-two groups both isomorphic to \(H^1(C)=\Lambda^2\), with endpoint groups \(\Lambda\) in degrees zero and three. Shifting by two places these four groups in degrees \(-2,-1,0,1\). Intermediate extension removes the last two. The stalk is therefore \(\Lambda\) in degree \(-2\) and \(\Lambda^2\) in degree \(-1\); the dual costalk is \(\Lambda^2\) in degree one and \(\Lambda\) in degree two. The global restriction map for a cone is the same radial cohomology isomorphism, so (4.2) leaves \(IH^0=\Lambda\) and \(IH^1=\Lambda^2\). Duality puts the compactly supported groups in degrees four and three, with ranks one and two. Integrally the Euler map has cokernel \(\mathbf Z/e\), as (A.7) records; the characteristic-zero calculation uses its invertibility.

**Exercise 4 (medium).** Show that \(\mathbf C^2/\{\pm1\}\) is rationally smooth, determine its intersection complex, and locate the integral failure.

**Solution.** Apply (4.3) to \(S^3\to\mathbf{RP}^3\). Orientation preservation makes the deck action trivial on the degree-three class, so over a characteristic-zero field the link has only degrees zero and three. The cone pair then has only local relative degree four, with its compatible orientation. Away from the origin the surface is smooth, so the same cohomology-manifold condition holds everywhere. Formula (3.5) gives \(\operatorname{IC}=\Lambda[2]\). Integrally, the cell cochain complex dual to \(d_3=0,d_2=2,d_1=0\) has \(H^2=\mathbf Z/2\). It produces a vertex relative class in degree three. Thus the failure is an actual torsion group, and division by the covering degree two is the invalid step in an attempted integral averaging argument.

**Exercise 5 (hard).** Prove Deligne's formula by induction on stratum dimension, checking preservation of the old open restriction and both boundary exclusions.

**Solution.** Suppose \(A\) is the perverse object already constructed on \(V_{s+1}\). Its stratum upper bounds give ordinary degrees at most \(-s-1\). For \(R=Rj_{s*}A\), take \(Q=\tau^{\leq-s-1}R\). Restriction to \(V_{s+1}\) is \(A\), so the discarded term \(C=\tau^{\geq-s}R\) is supported on \(F_s\). Ordinary t-exactness of restriction identifies it with \(i_*\tau^{\geq-s}i^*R\). Applying \(i^*\) and \(i^!\) to the truncation triangle gives

\[
i^*Q=\tau^{\leq-s-1}i^*R,\qquad
i^!Q=(\tau^{\geq-s}i^*R)[-1].
\tag{6.1}
\]

The ordinary upper and lower bounds are \(-s-1\) and \(-s+1\), respectively. These are strict perverse bounds \(-1\) and \(1\) on the \(s\)-dimensional closed strata. The gluing tests make \(Q\) perverse, and (1.3) excludes its boundary quotient and subobject. It is therefore \(j_{s!*}A\). Begin with \(L[d]\) on \(V_d\), repeat through the finitely many dimensions, and use (1.7) to identify the resulting object with extension directly from \(U\) to \(X\). This verifies each degree cutoff and each map used by the induction.

## Appendix A. Elliptic curves and the degree of an embedding

Let \(C\) be a smooth connected projective curve over \(\mathbf C\) with algebraic genus \(h^1(C,\mathcal O_C)=1\). Fix a point \(p\in C(\mathbf C)\). The argument uses the divisor and finite-map proofs of [Lesson 1, Appendix X](constructible-complexes-on-algebraic-varieties.md#appendix-x-valuations-rational-functions-and-divisor-degree), the Euler-characteristic calculation of [Q.1](constructible-complexes-on-algebraic-varieties.md#q-1-euler-degree-and-vanishing-at-one-point), and the explicit plane-curve topology of [Appendix E](constructible-complexes-on-algebraic-varieties.md#appendix-e-the-compact-plane-curve-its-degree-and-its-genus). Coherent cohomology in A.1 is algebraic; the cohomology in A.2–A.4 is singular cohomology of the complex points.

### A.1. Sections of positive-degree line bundles

For every line bundle \(L\), the point exact sequences and finite coherent cohomology in Q.1 give

\[
h^0(C,L)-h^1(C,L)=\deg L.
\tag{A.1}
\]

If \(\deg L=1\), this gives a nonzero section. Its effective zero divisor has degree one, so it is one point \(q\) with multiplicity one, and X.2 identifies \(L\) with \(\mathcal O_C(q)\). If this line bundle had two independent sections, a section independent of the constant rational function \(1\) would give a nonconstant rational function \(f\) whose only possible pole is a simple pole at \(q\). A function with no pole is constant by X.1, so that pole occurs. By X.3–X.4, the morphism \(f:C\to\mathbf P^1\) is finite and its degree is the degree of its pole divisor, namely one.

A finite morphism of integral curves of degree one onto \(\mathbf P^1\) is an isomorphism. Indeed, over an affine open of \(\mathbf P^1\) its finite coordinate algebra lies in the same function field and is integral over the coordinate ring of that open. This ring is integrally closed, being a localization of the polynomial ring in one variable, so the two rings coincide. This would give \(h^1(C,\mathcal O_C)=0\): the two affine charts of \(\mathbf P^1\) give the cokernel
\(\mathbf C[t,t^{-1}]/(\mathbf C[t]+\mathbf C[t^{-1}])=0\), by the affine Čech comparison of Lesson 1, W.1–W.2. The contradiction proves \(h^0(L)=1\) and \(h^1(L)=0\) in degree one.

For any line bundle of degree \(d\geq1\), the bundle \(L(-(d-1)p)\) has degree one. At each successive addition of \(p\), the point exact sequence gives a surjection on \(H^1\), since its skyscraper quotient has no positive cohomology. Starting with zero proves

\[
H^1(C,L)=0,\qquad h^0(C,L)=d\quad(d\geq1).
\tag{A.2}
\]

Put \(B=\mathcal O_C(3p)\). For any points \(q,r\), including \(q=r\), formula (A.2) gives

\[
h^0(B)=3,\qquad h^0(B(-q))=2,\qquad
h^0(B(-q-r))=1.
\tag{A.3}
\]

Thus \(B\) has no base point. If \(q\ne r\), the two kernels of evaluation are distinct: otherwise their common kernel would have dimension two instead of one. A section vanishes at one point and not the other, so the sections separate points. At \(q=r\), there is a section vanishing at \(q\) but not to order two. Divide it by a section nonzero at \(q\). The quotient is a local parameter, so the corresponding projective-coordinate functions have nonzero differential at \(q\).

### A.2. A plane cubic and the integral topology

Choose a basis of \(H^0(C,B)\). Its evaluations define \(f:C\to\mathbf P^2\); on a chart where one section is nonzero, the coordinate functions are the ratios of the other sections to it. These same ratios identify \(f^*\mathcal O_{\mathbf P^2}(1)\) with \(B\). We verify that \(f\) is a closed immersion, including its scheme structure.

The reduced closure \(Z\) of its image is an integral projective curve. It is not a point by point separation; its function field embeds in \(\mathbf C(C)\), so its transcendence degree is one. The factorization \(C\to Z\) is a nonconstant morphism of integral projective curves, hence finite by X.3; that proof does not require the target curve to be smooth. Composing with \(Z\hookrightarrow\mathbf P^2\) makes \(f\) finite.

For a closed point \(y\) in the image, put \(R=\mathcal O_{\mathbf P^2,y}\) and \(S=(f_*\mathcal O_C)_y\). This is a finite \(R\)-algebra. Point separation gives exactly one point \(q\) above \(y\), so \(S\) is local, with maximal ideal \(\mathfrak n\), and its residue field is \(\mathbf C\). The parameter constructed in A.1 makes the map on cotangent spaces surjective. Thus, writing \(\mathfrak m\) for the maximal ideal of \(R\),
\(\mathfrak n=\mathfrak m S+\mathfrak n^2\).
Apply Nakayama to the finite \(S\)-module \(\mathfrak n/\mathfrak m S\), using the determinant proof in [Lesson 1, U.1](constructible-complexes-on-algebraic-varieties.md#u-1-exact-tensoring-and-a-finite-replacement). It gives \(\mathfrak n=\mathfrak m S\). Hence \(S/\mathfrak m S=\mathbf C\), generated by \(1\), and Nakayama over \(R\), now applied to \(S/(R\cdot1)\), shows that \(R\to S\) is surjective. Off the image the target stalk is zero. The coherent cokernel of \(\mathcal O_{\mathbf P^2}\to f_*\mathcal O_C\) therefore vanishes: if its support were nonempty it would contain a closed point, by the finite-type Nullstellensatz proved in Lesson 1, K.1. A finite morphism with this surjection is a closed immersion on every affine chart.

For completeness, its image is cut out by one irreducible homogeneous polynomial \(F\). Choose a nonzero homogeneous equation of the image and an irreducible factor vanishing on \(Z\). Polynomial unique factorization and strict dimension decrease are proved in [Lesson 1, K.1](constructible-complexes-on-algebraic-varieties.md#k-1-the-elementary-algebraic-tools). The projective hypersurface of that factor is an integral curve: projection from a point where \(F\ne0\) makes its equation monic in the remaining coordinate, giving finite nonempty fibres over \(\mathbf P^1\). Since it contains the one-dimensional closed integral subset \(Z\), strict dimension decrease makes it equal to \(Z\). Both schemes are reduced, so the radical form of the same Nullstellensatz gives equality as schemes. Since \(Z\simeq C\) is smooth, an affine equation has a nonzero linear term at every point: otherwise its cotangent space would have dimension two. Euler's homogeneous identity then gives the nonvanishing-gradient hypothesis of Appendix E.

Here algebraic and analytic orders agree explicitly. At a smooth plane-curve point, choose an affine coordinate \(z\), centred at the point, whose differential on the tangent line is nonzero. The algebraic cotangent space has dimension one, so Nakayama makes \(z\) a uniformizer of its discrete valuation local ring. The implicit-function construction E.1 also makes \(z\) an analytic local coordinate. An algebraic unit is an analytic function nonzero at the point. Consequently a local algebraic expression \(z^m u\) has analytic zero order exactly \(m\).

Let \(n=\deg F\). The regular projection fibre in E.2–E.5 is a hyperplane section with exactly \(n\) simple zeros. The preceding local comparison makes its algebraic divisor degree \(n\). Its pullback is a section of \(B\), which has degree three. Thus \(n=3\), and \(f\) identifies \(C\) with a smooth plane cubic. This identification is also analytic in both directions, since the algebraic maps are expressed by regular coordinate functions.

Apply the finite triangulation, chain comparison and positive-point-class calculation E.3–E.6 to this cubic. They give a compact oriented surface, with the complex orientation, and

\[
H^j(C;\mathbf Z)=
\begin{cases}
\mathbf Z,&j=0,2,\\
\mathbf Z^2,&j=1,\\
0,&j\notin\{0,1,2\}.
\end{cases}
\qquad
\langle\eta,[C]\rangle=1.
\tag{A.4}
\]

Every positive local point class maps to \(\eta\). The chain calculation in E.4 also gives \(G,G^2,G\) in these degrees for any constant abelian coefficient group \(G\). In particular it supplies the characteristic-zero field groups used in Section 5. This topological conclusion concerns the curve itself, independently of the embedding used to form its cone.

### A.3. The line bundle of the given embedding

Return to any closed embedding \(i:C\hookrightarrow\mathbf P^N\) with \(A=i^*\mathcal O(1)\). Choose a hyperplane not containing \(i(C)\); its restriction is a nonzero section \(s\) of \(A\). Its zero divisor is a finite sum \(D=\sum_q m_q[q]\), with
\(\deg A=\sum_q m_q=e\), by X.2 and (A.1). The divisor is nonempty. Otherwise the embedded curve would lie in the complementary affine space, and its coordinate functions would all be global regular functions on \(C\), hence constants by X.1, contradicting the embedding.

The cubic identification in A.2 provides analytic coordinate discs on this same curve. In an algebraic frame for \(A\), the local expression of \(s\) at \(q\) is \(z^{m_q}u(z)\), with \(u(0)\ne0\), by the algebraic–analytic order comparison above. The local-zero formula in [Lesson 1, D.6](constructible-complexes-on-algebraic-varieties.md#d-6-local-zeros-and-the-euler-class) assigns this zero the positive multiplicity \(m_q\). All its positive point classes have the common absolute image \(\eta\), so

\[
e(A)=\sum_q m_q\eta=e\eta,\qquad e(A^{-1})=-e\eta.
\tag{A.5}
\]

The second sign is the conjugate-linear dual-line calculation D.5: a Hermitian metric identifies a complex line with its dual by a real orientation-reversing fibre map. Thus (A.5) uses the degree of the original line bundle \(A\), regardless of the auxiliary cubic embedding.

### A.4. The cone link and its actual maps

In the given projective coordinates the tautological bundle \(A^{-1}\) has fibre the line in \(\mathbf C^{N+1}\) represented by \(i(q)\). The maps

\[
(q,v)\longmapsto v,\qquad
v\longmapsto([v],v)
\tag{A.6}
\]

identify its nonzero vectors with the affine cone minus its vertex. On a chart where \(v_j\ne0\), the second map uses the regular ratios \(v_k/v_j\), so the maps are inverse in coordinates as well as on points. This argument uses the geometric affine cone and does not require projective normality of the embedding. Restricting the Euclidean norm to the tautological fibres identifies the link with the unit circle bundle \(M=S(A^{-1})\); positive radial scaling gives the punctured cone its product with \((0,\infty)\).

Use the pair connecting map and oriented Thom isomorphism of Lesson 1, D.5, with (A.4)–(A.5). Integrally the only nonzero Euler multiplication is \(-e:\mathbf Z\to\mathbf Z\). Its injectivity and its cokernel give

\[
\begin{gathered}
H^0(M;\mathbf Z)=H^3(M;\mathbf Z)=\mathbf Z,\qquad
\pi^*:H^1(C;\mathbf Z)\xrightarrow{\sim}H^1(M;\mathbf Z),\\
0\longrightarrow\mathbf Z/e\longrightarrow H^2(M;\mathbf Z)
\xrightarrow{\pi_!}H^1(C;\mathbf Z)\longrightarrow0.
\end{gathered}
\tag{A.7}
\]

There are no other cohomology groups. The last sequence splits as abelian groups by lifting a basis of its free quotient, although that choice is not canonical. The isomorphism in degree three is \(\pi_!:H^3(M;\mathbf Z)\to H^2(C;\mathbf Z)\). For characteristic-zero field coefficients, multiplication by \(e>0\) is invertible. The same Gysin sequence makes \(\pi^*\) in degree one and \(\pi_!\) in degrees two and three isomorphisms, giving precisely the link groups and maps in (5.5). The cone truncation and duality calculations (5.6)–(5.8) therefore apply to every embedding specified in the example.

## Appendix B. Allowable chains, subdivision and cones

We work with finite-dimensional local systems over the coefficient field \(\Lambda\). Let \(Y\) be a locally compact metrizable filtered space, with a finite closed filtration
\(\varnothing=Y^{-1}\subset Y^0\subset\cdots\subset Y^n=Y\),
and \(Y^{n-1}=Y^{n-2}\), with \(Y^j=\varnothing\) for \(j<0\). The regular part is \(U=Y\setminus Y^{n-2}\), on which the local system \(L\) is given. In dimensions zero and one the conditions below are empty and the chains are ordinary local-coefficient chains. For the comparison theorem \(Y\) is the stratified variety or one of its conical neighborhoods. The chain constructions themselves use the indicated filtration, rather than an invariance assertion about changing it.

A traditional perversity \(p\) has \(p(2)=0\) and \(p(k+1)-p(k)\in\{0,1\}\); in particular \(0\leq p(k)\leq k-2\). Middle perversity is \(p(k)=\lfloor(k-2)/2\rfloor\), so it has the value \(r-1\) on a complex-codimension-\(r\) stratum. Write \(\Delta^i_a\) for the \(a\)-skeleton of the standard ordered \(i\)-simplex, with empty skeleton if \(a<0\).

### B.1. Coefficients and the boundary condition

For any singular simplex \(\sigma:\Delta^i\to Y\), put \(V_\sigma=\sigma^{-1}(U)\). Its coefficient module is the module of sections of the pulled-back local system on \(V_\sigma\). On the complementary set we assign the zero coefficient; this does not assert that the local system extends across the singular locus. Restricting a section to a face gives its coefficient section there. The alternating sum of these restrictions defines the boundary in the module of finite formal sums of such decorated simplices. Equal simplex maps have their coefficients added as sections before zero terms are discarded. Every codimension-two face occurs twice with opposite signs and the same restricted section, so \(\partial^2=0\).

Call a simplex allowable when

\[
\sigma^{-1}(Y^{n-k})\subset\Delta^i_{\,i-k+p(k)}
\quad(2\leq k\leq n).
\tag{B.1}
\]

Using the individual strata instead of their closed unions gives the same condition: \(k-p(k)\) is nondecreasing, so the permitted skeleton for every deeper stratum is contained in the one in (B.1). An allowable simplex meets the singular set only in its codimension-two skeleton. The set \(V_\sigma\) is therefore nonempty and contracts to the barycenter by straight segments: at every positive time the segment lies in the interior of \(\Delta^i\). The usual local-system path lifting is explicit here. Subdivide a path into intervals on which the system is constant, and transport successively; subdivision does not change the result. A homotopy can be divided into small rectangles in constant neighborhoods, whose opposite-edge transports agree. Thus the contraction makes a coefficient section on \(V_\sigma\) uniquely determined by its value at one point. This also explains the compatibility of the restrictions to faces.

Let \(A_i^c(Y;L)\) be the submodule generated by allowable \(i\)-simplices with these coefficients. The intersection chain group is

\[
I^pC_i^c(Y;L)
=\{\,\xi\in A_i^c(Y;L):\partial\xi\in A_{i-1}^c(Y;L)\,\}.
\tag{B.2}
\]

Its boundary belongs to the same complex because \(\partial^2=0\). The condition concerns the boundary after cancellation; an individual face of a simplex in \(\xi\) need not be allowable.

The superscript \(\infty\) permits formal sums that are locally finite in \(Y\): every point has a neighborhood meeting the images of only finitely many simplices with nonzero coefficient. Finite faces preserve this property, so (B.2) defines \(I^pC_*^\infty(Y;L)\) as well. Its support is closed, since a locally finite union of compact subsets is closed: near any point it is a finite union of closed subsets. On a compact space a locally finite chain is finite, by a finite subcover of the neighborhoods in this definition.

For an open set \(V\subset Y\), define \(I^pC_*^\epsilon(V_Y;L)\) to be the subcomplex of chains in \(Y\) supported in \(V\), where \(\epsilon=c\) or \(\infty\), and define the relative complex by quotienting by this subcomplex. For finite chains this is the ordinary complex of \(V\) with the restricted filtration. For locally finite chains, local finiteness is still required in \(Y\); a family accumulating on \(Y\setminus V\) is excluded. The short exact sequence of complexes gives the relative long exact sequence: its connecting map sends a relative cycle represented by \(\xi\) to \(\partial\xi\) in the subcomplex. Lifting representatives and boundaries proves exactness at each of its three kinds of term.

### B.2. Subdivision and the allowable prism

Subdivide the model simplices by finite simplicial subdivisions compatible on all common parametrized faces. Orient each new top simplex by the old orientation and restrict coefficient sections along its affine parametrization. This defines a subdivision chain map \(T\). Internal faces cancel and the subdivisions agree on the boundary, so \(\partial T=T\partial\). If \(\delta\) is a simplex of a subdivision, its intersection with the old \(a\)-skeleton is a subcomplex of dimension at most \(a\). Consequently restriction to \(\delta\) carries the condition (B.1) to the same condition in its model simplex. Applying this to \(\xi\) and \(\partial\xi\) proves that \(T\) preserves intersection chains.

Here is a chain homotopy with the same control. Triangulate each prism \(\Delta^i\times[0,1]\), with the original triangulation at time zero and the chosen subdivision at time one. Construct its side faces inductively from the already triangulated lower-dimensional prisms. A finite triangulation of the boundary of a convex prism extends to its interior by coning to an interior point. Order and parametrize the new simplices compatibly on their faces, orienting the prism so that its boundary is the final face minus the initial face minus the prism on the boundary. Projection to \(\Delta^i\), followed by \(\sigma\), gives an operator \(D\) with

\[
\partial D+D\partial=T-1,\qquad
|T\xi|\cup|D\xi|\subset|\xi|.
\tag{B.3}
\]

For each \(a\), the triangulation contains \(\Delta^i_a\times[0,1]\) as a subcomplex of dimension at most \(a+1\). Thus the inverse image of \(Y^{n-k}\) on a prism simplex lies in its \((i+1-k+p(k))\)-skeleton. Its simplices are allowable. Formula (B.3), and the same argument on \(\partial\xi\), prove boundary allowability as well. All these sums are finite on each original simplex and remain within its image. Hence \(T,D\) preserve both finite chains and chains locally finite in the ambient space, as well as every subcomplex specified by support.

The same proof gives homotopy invariance in the form needed here. Suppose \(F:Y\times[0,1]\to Z\) sends each \(\{y\}\times[0,1]\) into one stratum of the same codimension as the stratum of \(y\), and the coefficient systems are identified along \(F\). Triangulate the ordinary prism and transport coefficients in its regular part. The inverse-image condition is (B.1) times the interval, so its prism is allowable and satisfies \(\partial P+P\partial=F_{1*}-F_{0*}\). This proves invariance for finite chains. It proves the corresponding assertion for locally finite chains when \(F\) is proper: the projection to \(Y\) of \(F^{-1}(K)\) is compact for every compact \(K\), so only finitely many original simplices contribute near \(K\). An arbitrary nonproper contraction is not asserted to preserve locally finite homology.

### B.3. Subdivision into allowable pieces

For an open cover \(\mathcal U=\{U_\alpha\}\), write \(I^pC_*^c(Y;\mathcal U,L)\) for the sum of the subcomplexes \(I^pC_*^c(U_\alpha;L)\). We prove that its inclusion into \(I^pC_*^c(Y;L)\) is a chain homotopy equivalence. It is insufficient merely to make each simplex small, because separating incident simplices could destroy cancellation of a nonallowable face.

We first give the finite geometric subdivision fact that will control those faces. Let \(K\) be a fixed triangulation of the boundary of a simplex, and extend it to the simplex by coning. Relative barycentric subdivision keeps \(K\) fixed and subdivides the other faces, inductively coning each subdivided boundary to that face's barycenter. After one such subdivision, the vertices lying in \(K\) in any simplex span a face in \(K\). On this finite triangulation define a piecewise affine function \(\rho\), zero at the vertices in \(K\) and one at the other vertices.

Fix a face \(\beta\) in \(K\). In a later relative subdivision, any new vertex in a simplex containing \(\beta\), unless it already lies in \(K\), is the barycenter of a face containing \(\beta\). At least one vertex of that face has \(\rho=0\), and it has at most \(i+1\) vertices if the ambient simplex has dimension \(i\). The maximum of \(\rho\) on the closed star of \(\beta\) consequently decreases by at least the factor \(i/(i+1)\) at each stage. Within each initial simplex, normalize the barycentric coordinates on its vertices in \(K\); their face lies in the closed star of \(\beta\) in \(K\). The distance from a point to that face is at most the initial diameter times \(\rho\). It follows that the closed star of \(\beta\) eventually lies in any prescribed neighborhood of its closed star in \(K\).

This also gives smallness relative to any finite list of open neighborhoods covering the simplex, provided each simplex in \(K\) already lies in a cover member. Indeed a descendant that meets \(K\) remains in an arbitrarily thin neighborhood of the appropriate initial face in \(K\), by the preceding estimate. A descendant disjoint from \(K\) undergoes ordinary barycentric subdivision, whose diameter decreases by the factor \(i/(i+1)\). Split the stages into two equal blocks: an ancestor still meeting \(K\) after the first block lies in the prescribed collar of one initial face, while an ancestor already disjoint from \(K\) acquires arbitrarily small diameter during the second block. Compactness and a Lebesgue number for the remaining cover give the assertion. Taking the maximum of finitely many stage bounds imposes smallness and finitely many closed-star conditions simultaneously.

Well-order the cover. For a simplex map \(\tau\) whose image lies in a cover member, let \(\psi(\tau)\) be the least such member; this depends only on the image. Construct subdivisions of all singular simplices by induction on dimension, independently of their coefficients. The choices on faces have already been made. Hold that boundary subdivision fixed and use the preceding fact to make the interior small. Impose also the following condition for every face \(\beta\) of the boundary subdivision whose dimension is \(a\) and which lies in the old \(a\)-skeleton:

\[
|\sigma(\operatorname{star}\beta)|\subset U_{\psi(\sigma|_\beta)}.
\tag{B.4}
\]

The closed star in the already fixed boundary satisfies this condition by induction. For a top boundary simplex itself the assertion is simply its smallness. Thus its compact star has a neighborhood in the indicated inverse image of \(U_{\psi(\sigma|_\beta)}\), and the finite geometric fact extends all these conditions to the interior. Every new top simplex \(\eta\) containing \(\beta\) then has label \(\psi(\eta)=\psi(\sigma|_\beta)\): containment in that cover member gives one inequality, and containment of the image of \(\beta\) in \(|\eta|\) gives the other. Compatibility of the choices on parametrized faces gives a subdivision chain map \(T\), with the support-preserving homotopy (B.3).

For an allowable \(i\)-chain \(\xi\), group the terms of \(T\xi\) by their label \(\psi\), writing \(T\xi=\sum_\alpha\xi_\alpha\). Each summand is supported in \(U_\alpha\), and all its top simplices are allowable. To check its boundary, consider a nonallowable \((i-1)\)-simplex map \(\mu\) occurring as a face of \(T\xi\). For some \(k\), put \(a=i-k+p(k)\). Nonallowability gives a point in \(\mu^{-1}(Y^{n-k})\) outside the \((a-1)\)-skeleton. Allowability of each incident top simplex puts that point in its old \(a\)-skeleton. Therefore the point lies in the relative interior of an \(a\)-face \(\beta\) of the model of \(\mu\), and, in every incident model subdivision, that entire face is in the old \(a\)-skeleton. This last assertion follows because the old skeleton is a subcomplex: meeting the relative interior of a subdivided face forces it to contain that face.

Condition (B.4) now labels every incident top simplex by the same \(\psi(\mu|_\beta)\). The same face \(\beta\) is used for all contributions to the identical map \(\mu\); its coefficient sections restrict to the same regular part. Thus all contributions to this nonallowable boundary face remain in a single summand. Their sum was zero in \(\partial T\xi\), and is still zero in the boundary of that summand. Every \(\xi_\alpha\) is therefore an intersection chain.

We have obtained a chain map \(T\) into \(I^pC_*^c(Y;\mathcal U,L)\). The homotopy \(D\) preserves that subcomplex: apply its support inclusion to each allowable summand supported in one \(U_\alpha\). Consequently (B.3) restricts to a homotopy in the small subcomplex as well, proving the asserted equivalence. For a locally finite chain the same constructions on its simplices and their faces are locally finite in \(Y\), since their supports remain inside the original images. For a finite cover they give a finite sum of allowable locally finite pieces, with the same homotopy. The two-member case will be used below; C.7 treats the locally finite family of cover operators.

### B.4. Excision and the two-open exact sequence

Let \(V\subset Y\) be open and \(F\subset V\) closed in \(Y\). Use the cover \(\{V,Y\setminus F\}\). Its small complex is
\(I^pC_*^c(V)+I^pC_*^c(Y\setminus F)\), and the intersection of the two summands is \(I^pC_*^c(V\setminus F)\), by the support condition. Quotienting by the first summand identifies the small relative complex with \(I^pC_*^c(Y\setminus F,V\setminus F)\). Both \(T\) and \(D\) preserve the first summand, so the homotopy equivalence descends to quotients. This proves

\[
I^pH_*^c(Y,V;L)
\simeq I^pH_*^c(Y\setminus F,V\setminus F;L).
\tag{B.5}
\]

For two open sets \(V,W\) covering \(Y\), the sequence

\[
\begin{aligned}
0&\longrightarrow I^pC_*^c(V\cap W)
\xrightarrow{a\mapsto(a,-a)}
I^pC_*^c(V)\oplus I^pC_*^c(W)\\
&\xrightarrow{(b,c)\mapsto b+c}
I^pC_*^c(Y;\{V,W\})\longrightarrow0
\end{aligned}
\tag{B.6}
\]

is exact degree by degree. The last complex computes \(I^pH_*^c(Y)\) by B.3, so its long exact sequence is the Mayer–Vietoris sequence for finite intersection chains. Explicitly, subdivide a cycle as \(\xi_V+\xi_W\); the connecting class is represented by \(\partial\xi_V=-\partial\xi_W\) on the intersection. The construction proves both the map and its independence of the representative through the short exact sequence.

### B.5. The finite-chain cone formula

Let \(K\) be a compact filtered space of dimension \(n-1\), with no codimension-one singular stratum, and \(n\geq2\). Give \(cK=(K\times[0,1))/(K\times\{0\})\) its conical filtration, with vertex \(v\), and pull the local system on the regular part of \(K\) back along the radial coordinate. The nonvertex strata have the same codimension as their strata in \(K\); the vertex has codimension \(n\). Put
\(b=n-1-p(n)\), which is at least one.

If \(i<b\), both an allowable \(i\)-chain and an allowable \((i+1)\)-chain avoid \(v\), since even the latter has vertex bound \(i+1-n+p(n)<0\). Thus the inclusion of the punctured cone induces an isomorphism in degree \(i\). Radial deformation to \(K\times\{1/2\}\) preserves the nonvertex codimensions and the pulled-back coefficients, so B.2 identifies this group with \(I^pH_i^c(K;L)\).

If \(i\geq b\), cone a finite allowable \(i\)-cycle \(\xi\) radially to \(v\). On a simplex this sends \((x,t)\) in the closed cone on \(\Delta^i\) to the point of radius \(t\) times the radius of \(\sigma(x)\), in the same direction. Coefficients are pulled back from \(x\) wherever the image is regular. The inverse image of a nonvertex codimension-\(k\) stratum lies in the cone on the old \((i-k+p(k))\)-skeleton, hence in the \((i+1-k+p(k))\)-skeleton. The inverse image of \(v\) is the cone on its old inverse image, together with the apex; its bound is valid because \(i+1-n+p(n)\geq0\). With the apex first in the vertex order, the cone identity is \(\partial(v*\xi)=\xi-v*(\partial\xi)=\xi\). Here \(i\geq b\geq1\), so the extra endpoint term for a cone on a zero-chain never enters this argument. This allowable cone bounds \(\xi\), proving

\[
I^pH_i^c(cK;L)=
\begin{cases}
I^pH_i^c(K;L),&i<n-1-p(n),\\
0,&i\geq n-1-p(n).
\end{cases}
\tag{B.7}
\]

The low-degree isomorphism is the actual inclusion of a radial slice. Apply the relative long exact sequence to \(cK\) and its puncture, using that inclusion and B.7. At the borderline degree \(b\), the subsequent map \(I^pH_{b-1}^c(K)\to I^pH_{b-1}^c(cK)\) is still an isomorphism. This gives the different cutoff

\[
I^pH_i^c(cK,cK\setminus\{v\};L)=
\begin{cases}
0,&i<n-p(n),\\
I^pH_{i-1}^c(K;L),&i\geq n-p(n).
\end{cases}
\tag{B.8}
\]

In the second range the isomorphism is the relative connecting map, followed by radial deformation of the puncture. In particular the equality case in (B.7) is a vanishing degree, whereas the equality case in (B.8) is a retained degree.

### B.6. Locally finite chains and the cone vertex

First suppose \(V\subset Y\) is open and \(Y\setminus V\) is compact. Choose an open \(W\) with compact closure containing this complement; finitely many relatively compact neighborhoods supply it. Apply B.3 to \(\{W,V\}\). For any allowable locally finite chain, the summand supported in \(W\) is finite, because local finiteness in \(Y\) bounds the number of simplices meeting \(\overline W\). For a relative cycle \(\xi\), write \(T\xi=\xi_W+\xi_V\). The boundary of \(\xi_W\) lies in \(V\), since \(T\partial\xi\) and \(\partial\xi_V\) are supported there. Formula (B.3) makes \(\xi\) and the finite relative cycle \(\xi_W\) homologous modulo \(V\).

If a finite relative cycle \(\xi\) bounds a locally finite chain \(\zeta\) modulo \(V\), the same decomposition gives a finite chain \(\zeta_W\) with \(\partial\zeta_W=T\xi\) modulo \(V\). The chain \(D\xi\) is finite and \(\partial D\xi=T\xi-\xi\) modulo \(V\). Thus \(\zeta_W-D\xi\) is a finite relative bounding chain. Surjectivity and injectivity have both been proved, giving

\[
I^pH_*^c(Y,V;L)\xrightarrow{\sim}
I^pH_*^\infty(Y,V;L)
\quad\text{if }Y\setminus V\text{ is compact}.
\tag{B.9}
\]

For \(Y=cK\), let \(V=cK\setminus\{v\}\), still requiring its chains to be locally finite in \(cK\). This subcomplex is acyclic. To see this, a chain in it has closed support avoiding \(v\), and compactness of \(K\) gives a radius \(\varepsilon>0\) below all its supported points. Set \(a_j=1-2^{-j}\) and move a radius \(r\) to
\(r_j=a_j+(1-a_j)r\). Interpolate from \(r_j\) to \(r_{j+1}\) by the stratum-preserving prism of B.2. Sum these prisms over \(j\geq0\).

The sum is locally finite in the ambient cone. Indeed a compact subset of \(cK\) has all radii at most some \(R<1\). Only finitely many \(j\) have \(a_j\leq R\). For each such \(j\), contributing original simplices meet a compact radial band \(\varepsilon\leq r\leq R_j<1\); compactness of \(K\) and local finiteness of the original chain leave only finitely many of them. The same argument applies near the vertex, where the support stays away. All prism pieces are allowable. Their boundary identities telescope locally, with the final translated chain eventually absent on each compact set. The negative of the summed prism operator consequently satisfies \(\partial Q+Q\partial=1\). This proves acyclicity without applying a nonproper contraction to all locally finite chains of the punctured cone.

The relative sequence and (B.9), followed by (B.8), now give

\[
I^pH_i^\infty(cK;L)=
\begin{cases}
0,&i<n-p(n),\\
I^pH_{i-1}^c(K;L),&i\geq n-p(n).
\end{cases}
\tag{B.10}
\]

The comparison map is the quotient to relative chains, the inverse of the finite-to-locally-finite isomorphism, and the connecting map in B.8. Thus the locally finite formula and its coefficient convention are determined together with their maps.

### B.7. The chain-sheaf stalk and its normalization

On relatively compact open sets \(W\subset Y\), sheafify the complex of presheaves

\[
W\longmapsto I^pC^c_{-q}(Y,Y\setminus\overline W;L)
\quad\text{in cohomological degree }q,\qquad d=\partial.
\tag{B.11}
\]

For a smaller open set the denominator increases, giving the restriction map. At a point \(y\), the union of those denominators is exactly the subcomplex of finite chains supported in \(Y\setminus\{y\}\). One inclusion is immediate. For the other, the support of a finite chain is compact and closed, so a sufficiently small neighborhood of \(y\), with compact closure, misses it. Filtered colimits of modules are exact: any representative equality, vanishing or finite boundary equation already holds at a later index. Hence the resulting sheaf complex \(\mathcal I_p^\bullet\) has

\[
H^q(\mathcal I_{p,y}^\bullet)
=I^pH_{-q}^c(Y,Y\setminus\{y\};L).
\tag{B.12}
\]

Excision (B.5) permits replacing \(Y\) on the right by any open neighborhood of \(y\). Replacing finite chains by locally finite chains in (B.11) gives a naturally quasi-isomorphic sheaf complex: for each relatively compact \(W\), (B.9) applies to the complement of \(\overline W\), and exact filtered colimits preserve that cohomology isomorphism.

On a regular real \(n\)-manifold chart, all chains are allowable and the coefficients become constant on a sufficiently small ball. The relative ball calculation of [Lesson 1, D.1](constructible-complexes-on-algebraic-varieties.md#d-1-integral-small-chains-pairs-and-covers), using its small-chain excision and sphere computation, gives a single local homology group in degree \(n\), with coefficient \(L_y\). The same hemisphere induction works directly with \(\Lambda\)-coefficients; no tensor-exactness assumption on an arbitrary integral complex is needed. For \(n=0\) this is the homology of a point.

These generators give local sections, not only pointwise isomorphisms. In a coordinate ball choose a closed cube \(Q\) whose interior contains the closure of a smaller ball \(W\). Triangulate the cube by ordering its coordinates, and sum its oriented top simplices. Interior faces cancel, so this finite chain is a cycle modulo \(Y\setminus\overline W\). Its class maps to a generator at every point \(y\in W\): the relative connecting map sends it to the oriented boundary of the cube, and radial retraction from \(y\) identifies that boundary with \(S^{n-1}\). The hemisphere connecting generators of D.1 agree with this boundary generator by splitting the oriented cube along a coordinate midplane; their signs are the signs of its two boundary faces. The radial identification can be varied continuously as \(y\) moves in the interior, so the prism preserves the generator. Multiplying this cycle by a constant coefficient section therefore gives a stalkwise isomorphism from the constant coefficient sheaf on \(W\) to the degree-\(-n\) cohomology sheaf. The point case uses its zero-simplex.

On overlapping differentiable charts the sign is that of the coordinate-change determinant: [Lesson 1, C.4](constructible-complexes-on-algebraic-varieties.md#c-4-spheres-local-orientation-and-coordinate-changes) proves this by the homotopy to the derivative, the path for a positive-determinant matrix, and a single reflection; D.1 proves the same sign for homology. Thus the only cohomology sheaf on the regular part is \(L\otimes\operatorname{or}_U\) in degree \(-n\). Canonical truncations identify the complex there with \((L\otimes\operatorname{or}_U)[n]\). For a complex variety of pure dimension \(d\), the real determinant of a complex-linear change is \(|\det_{\mathbf C}|^2>0\), so complex orientation trivializes this orientation system and \(n=2d\). The restriction is precisely \(L[2d]\), as used in Section 3.

At the vertex of the cone in B.5, equations (B.8) and (B.12) show that the stalk vanishes for \(q>p(n)-n\); below and at that cutoff it is \(I^pH_{-q-1}^c(K;L)\). These statements establish the actual coefficient complex, the cone stalk cutoff and its normalization. C.1–C.4 supply the product-neighborhood formulas and local constancy along strata. Appendices D–E establish the derived global and compact-support comparisons, bounded finite-rank constructibility, and the actual attaching-map assertion. Appendix F supplies the simplicial and PL comparisons. The global conclusions use these arguments together, not merely the stalk computation.

## Appendix C. Product neighborhoods and sections of the chain sheaf

Keep the coefficients, filtration and perversity of Appendix B. Products with a Euclidean space have the product filtration, so a stratum keeps its codimension. Coefficients are pulled back from the other factor. This also describes any local system on the regular part of a conical product after an identification on a radial slice: transport along the straight contractions of the Euclidean and radial coordinates supplies the identification, and the homotopy-of-paths argument in B.1 makes it independent of the contractions' subdivisions.

### C.1. The relative suspension and its map

For a closed subset \(A\subset Y\), write
\(J_*(Y,A)=I^pC_*^c(Y,Y\setminus A;L)\).
The subset \(A\) need not be a union of strata. We claim

\[
H_iJ_*(Y\times\mathbf R,A\times\{0\})
\simeq H_{i-1}J_*(Y,A).
\tag{C.1}
\]

Here and below the coefficient system on a product is understood. Put
\(C=I^pC_*^c(Y\times\mathbf R)\),
\(B=I^pC_*^c((Y\setminus A)\times\mathbf R)\), and
\(D=I^pC_*^c(Y\times\mathbf R^*)\), where
\(\mathbf R^*=\mathbf R\setminus\{0\}\).
The intersection \(B\cap D\) is the complex supported in
\((Y\setminus A)\times\mathbf R^*\). There is a short exact sequence

\[
0\longrightarrow D/(B\cap D)
\longrightarrow C/B
\longrightarrow C/(B+D)\longrightarrow0.
\tag{C.2}
\]

The two open sets \((Y\setminus A)\times\mathbf R\) and
\(Y\times\mathbf R^*\) cover the complement of \(A\times\{0\}\).
B.3 makes \(B+D\) chain homotopy equivalent to the full chain complex of that complement. Consequently the quotient map from the last term of (C.2) to \(J_*(Y\times\mathbf R,A\times\{0\})\) is a quasi-isomorphism: its kernel is the quotient of that full complement complex by \(B+D\), which is acyclic by the short exact sequence and the small-chain equivalence.

Projection and contraction of the real coordinate give stratum-preserving homotopies of pairs. By B.2,
\(H_i(C/B)=H_iJ_*(Y,A)\), whereas
\(H_i(D/(B\cap D))=H_iJ_*(Y,A)\oplus H_iJ_*(Y,A)\).
Order the two summands by negative and positive real coordinate. Under these identifications the inclusion in (C.2) is \((a,b)\mapsto a+b\), since both slices project by the identity on \(Y\). It is surjective in every degree. Its long exact sequence therefore identifies the homology of the last term with
\(\{(-z,z):z\in H_{i-1}J_*(Y,A)\}\).
Projection to the positive summand proves (C.1).

This describes the isomorphism and its inverse on representatives. If \(\gamma\) is a relative \(j\)-cycle for \((Y,Y\setminus A)\), triangulate
\([-1,1]\times\Delta^j\) compatibly on faces and orient the interval first. The product chain \(S\gamma\) in \(Y\times\mathbf R\) satisfies

\[
\partial S\gamma=\gamma_+-\gamma_--S(\partial\gamma).
\tag{C.3}
\]

Each inverse image of a singular stratum lies in the product of an allowed skeleton with the interval, of dimension at most one more than the old bound. Thus \(S\gamma\) is allowable, including its boundary after cancellation. Its endpoint terms lie in \(D\), and \(S(\partial\gamma)\) lies in \(B\). The connecting map of (C.2) consequently sends its relative class to \((-[\gamma],[\gamma])\), exactly the inverse just specified. On relative complexes the same construction satisfies \(\partial S=-S\partial\), as required for a shift by one.

All these maps commute with inclusions of closed subsets and with the induced quotient maps of relative complexes. Repeating the construction in an ordered list of real coordinates gives

\[
\begin{aligned}
&I^pH_i^c(Y\times\mathbf R^s,
 (Y\times\mathbf R^s)\setminus(A\times\{0\});L)\\
&\qquad\simeq I^pH_{i-s}^c(Y,Y\setminus A;L).
\end{aligned}
\tag{C.4}
\]

The order of the suspension steps fixes its orientation sign. There is no Künneth assumption in this argument.

### C.2. Radial contraction of the ambient support subcomplex

Two cases will be used. In the first, \(Z=K\times\mathbf R^s\), where \(K\) is compact and \(s\geq1\), and \(E=K\times\{0\}\). In the second, \(Z=cK\times\mathbf R^s\), \(s\geq0\), and \(E=\{(v,0)\}\). Use the infinite-radius model
\(cK=(K\times[0,\infty))/(K\times\{0\})\), which is homeomorphic to the open cone of B.5 by an increasing change of radius. Put
\(\rho=\|u\|\) in the first case and
\(\rho=(r^2+\|u\|^2)^{1/2}\) in the second. The sets \(\{\rho\leq R\}\) are compact: they are closed subsets of \(K\times[-R,R]^s\), or continuous images of closed subsets of \(K\times[0,R]\times[-R,R]^s\).

Consider chains supported in \(Z\setminus E\) but locally finite in all of \(Z\). Such a chain has closed support disjoint from \(E\). Its support has \(\rho\geq\varepsilon\) for some \(\varepsilon>0\): otherwise supported points with \(\rho\to0\) would have an accumulation point in the compact set \(\{\rho\leq1\}\), lying in \(E\) and in the closed support.

Dilate the Euclidean coordinate, and in the cone case its radius as well, by \(1+t\), leaving the \(K\)-direction fixed. For each integer interval \(j\leq t\leq j+1\), form the prism of B.2, with coefficients transported in this direction-preserving homotopy. The formal sum of these prisms is locally finite in \(Z\). Indeed a compact target set lies in \(\{\rho\leq R\}\). A contributing prism has \(j\leq R/\varepsilon\), and its original simplex meets the compact set \(\{\rho\leq R\}\). There are only finitely many such original simplices and only finitely many such intervals, each producing finitely many prism simplices.

The homotopy preserves every stratum and its codimension, so the same skeleton argument proves allowability. On each compact target set the terminal translated chain disappears for sufficiently large \(j\). The prism boundary formula therefore telescopes to
\(\partial P+P\partial=-1\).
Thus \(-P\) contracts the ambiently locally finite subcomplex supported in \(Z\setminus E\). The identical construction contracts the subcomplex supported in \(\{\rho>a\}\) for any \(a>0\); dilations stay in that set.

The relative long exact sequence and B.9 now yield actual isomorphisms

\[
\begin{aligned}
I^pH_i^\infty(Z)&\xrightarrow{\sim}I^pH_i^\infty(Z,Z\setminus E),\\
I^pH_i^c(Z,Z\setminus E)&\xrightarrow{\sim}I^pH_i^\infty(Z,Z\setminus E).
\end{aligned}
\tag{C.5}
\]

The first arrow is quotienting chains; the second is inclusion of finite chains. Compactness of \(E\) is exactly what is required for the second arrow. The same statements hold with \(E\) replaced by the compact radial set \(\{\rho\leq a\}\).

### C.3. The product formulas and their representatives

Apply (C.4) with \(Y=K,A=K\), and then (C.5). For compact \(K\),

\[
I^pH_i^\infty(K\times\mathbf R^s;L)
\simeq I^pH_{i-s}^c(K;L),\qquad s\geq0.
\tag{C.6}
\]

The case \(s=0\) follows because locally finite chains on \(K\) are finite. For \(s>0\) an inverse sends a finite cycle \(\gamma\) to its product with the oriented, locally finite fundamental chain of \(\mathbf R^s\). To construct it, triangulate each product of its model simplex with the unit cubes in \(\mathbf R^s\), using the same triangulation on common faces. Internal faces cancel. A compact target set meets finitely many cubes and finitely many original simplices. The inverse-image skeleton bound increases by \(s\), so the resulting product and its boundary are allowable. Cutting the product along an integral cube containing \(0\) gives a finite relative representative. Repeated use of (C.3) sends it back to \(\gamma\), including the chosen coordinate-order sign.

Now let \(K\) have dimension \(n-1\), with conical filtration as in B.5, and let \(N=cK\times\mathbf R^s\), of dimension \(n+s\). Applying (C.4) with \(Y=cK,A=\{v\}\), and then B.8, gives

\[
I^pH_i^\infty(N;L)=
\begin{cases}
0,&i<n+s-p(n),\\
I^pH_{i-s-1}^c(K;L),&i\geq n+s-p(n).
\end{cases}
\tag{C.7}
\]

In particular it equals \(I^pH_{i-s}^\infty(cK;L)\), with the maps specified by the relative quotient, the finite-chain inclusion, and the successive connecting maps.

These retained classes also have direct locally finite representatives. If \(\gamma\) is a finite \(j\)-cycle on \(K\), with \(j\geq n-1-p(n)\), cone its model simplices over the initial radial interval \([0,1]\), then use product prisms on the intervals \([1,2],[2,3],\ldots\). The common radial faces cancel, giving an open-cone chain \(c\gamma\). Its intersection with the vertex is permitted precisely because \(j+1-n+p(n)\geq0\). Nonvertex strata obey the cone skeleton estimate of B.5. Compact sets meet finitely many radial pieces. The product \(c\gamma\times\mathbf R^s\) is therefore allowable and locally finite. Its finite truncation and the connecting maps in B.8 and (C.4) recover \(\gamma\); its dimension is \(j+s+1\), as in (C.7).

For the deleted product neighborhood, increasing logarithmic radial coordinate identifies
\((cK\setminus\{v\})\times\mathbf R^s\) with \(K\times\mathbf R^{s+1}\). Hence

\[
\begin{gathered}
I^pH_i^\infty((cK\setminus\{v\})\times\mathbf R^s;L)
\simeq I^pH_{i-s-1}^c(K;L)\\
\text{in every degree}.
\end{gathered}
\tag{C.8}
\]

Its representative is the product of \(\gamma\) with the full radial line and the \(s\) other real coordinates. Equations (C.7)–(C.8) give the groups and explicit cycles; identifying the actual derived attaching map with their correspondence requires the sheaf comparison, not merely equality of these groups.

### C.4. Shrinking neighborhoods and local constancy along a stratum

Let \(x=(v,0)\) in \(N=cK\times\mathbf R^s\), and put
\(E_a=\{\rho\leq a\}\) and \(N_a=\{\rho<a\}\) for \(a>0\), with the radius of C.2. The \(N_a\), as \(a\to0\), form a neighborhood basis of \(x\). To check cofinality, pull an open neighborhood back to \(K\times[0,\infty)\times\mathbf R^s\). It contains \(K\times\{0\}\times\{0\}\); a finite subcover over compact \(K\) gives a common positive radial and Euclidean bound.

For \(0<a<b\), the inclusion \(N\setminus E_b\to N\setminus E_a\) is a stratum-preserving homotopy equivalence for finite chains. On \(\rho>a\), the inverse map increases \(\rho\) by \(b-a\), multiplying \((r,u)\) by \((\rho+b-a)/\rho\). Interpolating this multiplier with \(1\) gives the two homotopies; the one starting in \(\rho>b\) stays there. The coefficient identifications are the radial ones. The relative exact sequences with ambient space \(N\) therefore show that the natural quotient maps

\[
I^pH_i^c(N,N\setminus E_b)
\longrightarrow I^pH_i^c(N,N\setminus E_a)
\tag{C.9}
\]

are isomorphisms. Equivalently, this follows from the commuting quotients (C.5) for \(E_a\) and \(E_b\).

Write \(\mathcal J_{p,Y}^\bullet\) for the locally finite version of the sheaf in B.11; its degree \(q\) presheaf is
\(W\mapsto I^pC_{-q}^\infty(Y,Y\setminus\overline W)\).
B.9 and B.7 give a natural quasi-isomorphism
\(\mathcal I_{p,Y}^\bullet\to\mathcal J_{p,Y}^\bullet\).
If \(N\) is an open conical neighborhood in a larger space \(Y\), finite-chain excision removes \(Y\setminus N\) from the pairs with \(E_a\subset N\). Thus (C.9), exact filtered colimits, and (C.5) identify the stalk cohomology with the homology of the whole local product. In the cohomological indexing used here this is

\[
\mathcal H^q(\mathcal I_{p,Y}^\bullet)_x =
\begin{cases}
0,&q>p(n)-(n+s),\\
I^pH_{-q-s-1}^c(K;L),&q\leq p(n)-(n+s).
\end{cases}
\tag{C.10}
\]

The same formula holds for \(\mathcal J_{p,Y}^\bullet\), and the map from a locally finite cycle on \(N\) to its germ is the displayed isomorphism. At a stratum of complex codimension \(r\), \(n=2r\), \(n+s=2d\), and \(p(n)=r-1\); the cutoff is therefore \(r-1-2d\), the cutoff needed in Section 3.

This also proves local constancy of the cohomology sheaves along each conical stratum chart. First work with the native chain sheaf on the product neighborhood; the open comparison proved in C.6 transfers the conclusion to the ambient chain sheaf. Indeed recenter the Euclidean coordinate at any \(u_0\) on \(\{v\}\times\mathbf R^s\). The same argument identifies the germ there with \(I^pH_{-q}^\infty(N)\). A cycle representing any element of that group gives a section of the cohomology sheaf throughout \(N\), and a boundary gives its zero section. These sections induce a map from the constant sheaf with that group on the vertex stratum. Its stalk maps at every \(u_0\) are the isomorphisms just proved, so it is a sheaf isomorphism. This proves local constancy. The finite-rank and boundedness assertions follow from the compact-link induction in E.2.

### C.5. Global sections are actual chains

We next identify ordinary sections of \(\mathcal J_{p,Y}^\bullet\), retaining the distinction from derived sections. There are natural isomorphisms of complexes

\[
\begin{aligned}
I^pC_{-q}^\infty(Y;L)&\xrightarrow{\sim}
 \Gamma(Y,\mathcal J_{p,Y}^q),\\
I^pC_{-q}^c(Y;L)&\xrightarrow{\sim}
 \Gamma_c(Y,\mathcal J_{p,Y}^q).
\end{aligned}
\tag{C.11}
\]

A global chain gives its relative class on every relatively compact open set and hence a sheaf section. This map is injective: if the germ is zero at \(y\), the chain is supported outside the closure of some neighborhood of \(y\). A nonzero simplex coefficient cannot satisfy this at any point of that simplex's image. Thus a chain with all germs zero has all coefficients zero.

Here is a direct gluing proof of surjectivity. Let \(s\) be a global section of the sheaf. Near any point it is represented by a relative chain, hence by some globally locally finite chain \(\xi\) on \(Y\). For any allowable simplex map \(\sigma:\Delta^i\to Y\), its coefficient takes values in the module \(E_\sigma\) of sections on \(\sigma^{-1}(U)\) defined in B.1. If two local representatives have the same germ at a point of \(|\sigma|\), their difference is supported away from a smaller neighborhood of that point, so their coefficients of the entire map \(\sigma\) are equal in \(E_\sigma\).

Consequently the local representatives assign a well-defined locally constant \(E_\sigma\)-valued function on \(|\sigma|\). This image is connected, being the continuous image of a simplex, so the function has one constant value \(g_\sigma\). Use zero when that simplex does not occur in the representative. Form the formal chain \(\xi_s=\sum_\sigma g_\sigma\sigma\). It is locally finite: choose a neighborhood \(V\) on which \(s\) is represented by one \(\xi\), and then a smaller neighborhood on which \(\xi\) has only finitely many incident simplices. Every simplex of \(\xi_s\) meeting that neighborhood has exactly its coefficient in \(\xi\), by evaluation at a point of its image there.

All top simplices of \(\xi_s\) are allowable. Its boundary is allowable as well. For a nonallowable face map \(\mu\), choose one point in \(|\mu|\) and a local representative \(\xi\) of \(s\) there. Every top simplex contributing to the coefficient of \(\mu\) meets that point, so its coefficient in \(\xi_s\) equals its coefficient in \(\xi\). There are only finitely many such simplices by local finiteness. The whole coefficient of \(\mu\) in the two boundaries is therefore identical, and is zero because \(\xi\) is an intersection chain. This also handles coefficient sections on a face with disconnected regular preimage: the equality concerns their entire restricted sections, not only their values at one regular point.

Thus \(\xi_s\) is an intersection chain. Near a point where \(s\) is represented by \(\xi\), their coefficients agree on all simplex images meeting a smaller neighborhood with closure in that representing neighborhood. The difference is supported outside that closure, so their germs agree. This proves surjectivity and identifies the inverse. Boundaries commute with the construction since they commute with every relative restriction.

The sheaf support of the section of a chain is exactly its chain support. If a point is outside the chain support, local finiteness makes that support closed and gives a neighborhood missing it. If it is in a simplex image with nonzero coefficient, no relative germ there can be zero. A locally finite family with compact union is finite, by covering that compact union with finitely many local-finiteness neighborhoods. Conversely a finite chain has compact support. This proves the second line of (C.11), including its support convention.

### C.6. The chain complex on an open subspace

For an open inclusion \(j:V\hookrightarrow Y\), there is a natural quasi-isomorphism

\[
\mathcal I_{p,V}^\bullet\longrightarrow
j^{-1}\mathcal I_{p,Y}^\bullet.
\tag{C.12}
\]

Use the basis of relatively compact \(W\) with \(\overline W\subset V\); its closures are the same whether taken in \(V\) or \(Y\). Inclusion of finite chains defines
\(I^pC_*^c(V,V\setminus\overline W)\to
I^pC_*^c(Y,Y\setminus\overline W)\).
Excision B.5, with the closed set \(Y\setminus V\) inside the open complement of \(\overline W\), makes this a homology isomorphism. The maps commute with all smaller-neighborhood quotients. Exact filtered colimits therefore give a cohomology isomorphism at every stalk, proving (C.12).

Together with the natural finite-to-locally-finite quasi-isomorphisms, (C.12) identifies \(\mathcal J_{p,V}^\bullet\) and \(j^{-1}\mathcal J_{p,Y}^\bullet\) in the derived category. This uses finite chains for the inclusion: extension by zero of an arbitrary chain locally finite only in \(V\) need not be locally finite in \(Y\). Nor does a quasi-isomorphism of these sheaves alone prove that ordinary sections compute their derived sections.

### C.7. Endomorphisms subordinate to a cover

Let \(\{V_\alpha\}\) be a locally finite open cover of \(Y\). Perform the construction of B.3, with its fixed ordering of the cover, on all singular simplices. For a locally finite chain \(\xi\), let \(P_\alpha\xi\) be the subchain of \(T\xi\) consisting of terms with label \(\alpha\). The same bad-face argument proves that each \(P_\alpha\xi\) is an intersection chain. It is locally finite because its terms are among those of \(T\xi\), and its support is contained both in \(|\xi|\) and in \(V_\alpha\).

These are linear operators in each degree. Individual \(P_\alpha\) need not commute with the boundary; their sum does, because it is \(T\). The family is locally finite: near any point only finitely many cover members can meet, and all the other output chains have zero germs there. The formal sum agrees with \(T\xi\) coefficient by coefficient. The operator \(D\) of B.2 is also defined on these chains and preserves their supports.

Every one of \(P_\alpha,T,D\) preserves the subcomplex of chains supported outside \(\overline W\), for every open \(W\). They therefore induce morphisms on the relative presheaves and then on their sheafifications. Denote the induced degree-zero maps by \(p_\alpha\), and the degree-minus-one map by \(h\). Their supports are contained in \(\overline{V_\alpha}\): outside that closed set they vanish on an open neighborhood. The family is locally finite as sheaf morphisms, and (B.3) gives

\[
\sum_\alpha p_\alpha=1+dh+hd
\quad\hbox{on }\mathcal J_{p,Y}^\bullet.
\tag{C.13}
\]

The same assertion follows on \(\mathcal I_{p,Y}^\bullet\) from finite chains. If the cover refines another cover with
\(\overline{V_\alpha}\subset U_{\lambda(\alpha)}\), grouping its operators gives the same identity subordinate to the \(U\)'s. This explicit endomorphism-and-homotopy property is called homotopical fineness.

Appendix D proves that this property computes derived global and compactly supported sections at the present, initially unbounded chain-complex scope. Appendix E proves bounded finite-rank constructibility and the actual attaching-map isomorphism. Equations (C.10)–(C.13) are inputs to those arguments. Appendix F supplies agreement with simplicial and PL intersection chains, including the refinement maps.

## Appendix D. Derived sections of the chain sheaf

We now prove the derived-section assertion left open in C.7. The coefficients are the field \(\Lambda\). The spaces in this appendix are locally compact and metrizable, admit a countable compact exhaustion, and have a uniform finite compact cohomological dimension on their open subsets: for some \(N\),

\[
H_c^a(V,F)=0\quad(a>N)
\tag{D.1}
\]

for every open \(V\subset Y\) and every sheaf of \(\Lambda\)-vector spaces on \(V\). These hypotheses hold for the varieties in Section 3 and their open conical neighborhoods. Indeed their finite affine atlases give second countability and local compactness, and [Lesson 1, F.1–F.2](constructible-complexes-on-algebraic-varieties.md#f-1-compact-extension-and-exact-lifting) proves the uniform bound for locally closed Euclidean charts and finite atlases. The dimension bound concerns all sheaves, not only constructible ones. No boundedness of the chain complex is assumed.

### D.1. Compact exhaustions and ordinary sections

We use the compact-extension and compact-lifting statements of Lesson 1, F.1: sections over a compact set are germs of sections on a neighborhood; a c-soft kernel permits lifting over compact sets and exact compactly supported sections; and a quotient of two c-soft sheaves is c-soft. We first supply the corresponding assertion for ordinary sections.

Choose compact sets \(K_m\) with \(K_m\subset\operatorname{int}K_{m+1}\) and union \(Y\). Such an exhaustion exists in every locally compact second-countable space: choose a countable cover by relatively compact open sets, and inductively cover the previous compact set and the closures of the first finitely many of these opens by finitely many relatively compact neighborhoods. Their closed union is the next compact set. The same construction applies to every open subset of \(Y\). More generally, the stated countable compact-exhaustion hypothesis gives second countability here: each compact metric set has finite \(1/m\)-nets for all positive integers \(m\), and balls about their countably many centers with positive rational radii give a countable base. The interiors of the compact sets cover the space.

Suppose \(0\to A\to B\to C\to0\) is exact and \(A\) is c-soft. Given \(s\in C(Y)\), lift its restriction over \(K_1\). If \(t_m\in B(K_m)\) is chosen, first lift \(s|_{K_{m+1}}\) over \(K_{m+1}\). The difference from \(t_m\) over \(K_m\) lies in \(A(K_m)\). Extend that difference to a section of \(A(Y)\) by c-softness and subtract it. This gives \(t_{m+1}\) restricting to \(t_m\). On the interiors of the \(K_m\) the compatible sections glue to a lift in \(B(Y)\). Thus \(\Gamma(Y,-)\) is exact on such a sequence. Embedding a c-soft sheaf into an injective and repeating the c-soft quotient assertion gives a resolution that remains exact on ordinary sections. Hence c-soft sheaves are \(\Gamma\)-acyclic as well as \(\Gamma_c\)-acyclic, on every open subset.

The exhaustion also provides the precise cover refinement needed below. For any open cover \(\{U_\lambda\}\), cover each compact annulus \(K_m\setminus\operatorname{int}K_{m-1}\) by finitely many open sets \(V_\alpha\) whose compact closures lie both in a chosen \(U_{\lambda(\alpha)}\) and in \(\operatorname{int}K_{m+1}\setminus K_{m-2}\); take \(K_j=\varnothing\) for \(j\leq0\). Local compactness and the metric allow these choices. The resulting cover is locally finite: a neighborhood inside \(\operatorname{int}K_j\) meets no annulus neighborhoods from sufficiently large indices. Its closures are locally finite too, since an open set meeting a closure also meets the original open set. In particular a compact set meets only finitely many of these closures.

### D.2. A functorial resolution of finite length

For a sheaf \(F\), define

\[
G(F)(V)=\prod_{x\in V}F_x,\qquad
Q(F)=\operatorname{coker}(F\longrightarrow G(F)).
\tag{D.2}
\]

The first sheaf allows all assignments of germs, with no continuity requirement. Its restriction maps are projections. The natural map from \(F\) is monic because a section with all germs zero is zero. The functor \(G\) is additive and exact: a short exact sequence is exact on stalks, and products of vector-space exact sequences are exact. It takes values in injectives. Explicitly, \(G(F)=\prod_x i_{x*}F_x\), and
\(\operatorname{Hom}(A,i_{x*}F_x)=\operatorname{Hom}_\Lambda(A_x,F_x)\)
is exact in \(A\); products of these Hom functors remain exact. This also proves the asserted injectivity without a choice of injective envelopes. The cokernel sequence and its kernel-cokernel diagram show that \(Q\) is an additive exact functor.

Both functors commute with restriction to an open subset. For \(G\) this follows directly from the product in (D.2); for \(Q\) it follows from exactness of restriction. They therefore preserve the property that a sheaf morphism vanishes on a specified open set. They also preserve locally finite sums of morphisms: near each point the sum is finite, where the assertion is just additivity.

Iterating (D.2) gives the functorial exact resolution

\[
0\longrightarrow F\longrightarrow G(F)
\longrightarrow GQ(F)\longrightarrow\cdots
\longrightarrow GQ^{N-1}(F)\longrightarrow Q^N(F)
\longrightarrow0.
\tag{D.3}
\]

When \(N=0\), use just \(F\) in degree zero. For \(N\geq1\), dimension shifting on any open \(V\) gives
\(H_c^1(V,Q^N(F)|_V)=H_c^{N+1}(V,F|_V)=0\).
The c-softness criterion proved in Lesson 1, F.1, shows that \(Q^N(F)\) is c-soft. When \(N=0\), the same criterion makes every sheaf c-soft. Write \(R^a(F)=GQ^a(F)\) for \(a<N\), and \(R^N(F)=Q^N(F)\), for the terms of (D.3). Every \(R^a(F)\) is c-soft, and hence acyclic for both section functors by D.1. We have also proved an ordinary cohomological bound \(H^a(Y,F)=0\) for \(a>N\).

Let \(\Phi\) mean either \(\Gamma(Y,-)\) or \(\Gamma_c(Y,-)\). Each functor \(\Phi R^a\) is exact. In fact \(R^a\) is exact, and in the resulting short exact sequence the kernel \(R^a(F')\) is \(\Phi\)-acyclic. The long exact cohomology sequence therefore gives surjectivity on sections as well as left exactness.

For an arbitrary, possibly unbounded, cochain complex \(A^\bullet\), set

\[
T_\Phi(A)^m=
\bigoplus_{a=0}^N\Phi R^a(A^{m-a}),
\qquad D=\delta+(-1)^a d_A.
\tag{D.4}
\]

Here \(\delta\) is the resolution differential. It commutes with \(R^a(d_A)\) by naturality, so the two mixed terms in \(D^2\) cancel. Every displayed sum is finite. Filtering by \(a\) shows that \(T_\Phi\) sends quasi-isomorphisms to quasi-isomorphisms: on a comparison cone, each fixed-\(a\) complex is the exact functor \(\Phi R^a\) applied to an acyclic complex; the finite filtration then gives zero total cohomology. This last finite-filtration argument follows successively from the long exact sequence for a subcomplex and its quotient, and has no lowest-degree requirement.

To identify (D.4) with the derived functor, take a termwise injective K-injective replacement \(A\to I\). Its existence for this sheaf category is proved in [Sheaves of modules and their derived categories, Theorem 7.2 and its five lemmas](course:derived-categories-and-sheaf-operations/sheaves-of-modules-and-their-derived-categories#7-k-injective-resolutions-of-unbounded-complexes); Lesson 1, BF.1, gives comparison of maps into it. Every \(I^b\) is \(\Phi\)-acyclic, so applying \(\Phi\) to (D.3) for \(I^b\) gives an exact augmented resolution. Therefore \(\Phi I\to T_\Phi(I)\) is a quasi-isomorphism. To justify this for unbounded \(b\), filter the augmented double complex by \(b\): in a fixed total degree its resolution indices range only from \(-1\) to \(N\). Successively removing an exact-resolution leading component takes at most \(N+2\) steps; all corrections are finite sums. Thus the exact augmented columns give an acyclic total complex. Together with the quasi-isomorphism \(T_\Phi(A)\to T_\Phi(I)\), this proves that (D.4) computes \(R\Phi(A)\), compatibly with the natural map \(\Phi A\to R\Phi(A)\).

### D.3. What the cover homotopy does to higher cohomology

Suppose a complex \(A^\bullet\) has the property proved in C.7: for every locally finite cover \(\{V_\alpha\}\) there are graded degree-zero sheaf maps \(p_\alpha\), supported in \(\overline{V_\alpha}\), and a degree-minus-one map \(h\), with
\(P=\sum_\alpha p_\alpha=1+dh+hd\).
The sum is locally finite; individual \(p_\alpha\) need not be chain maps. We claim

\[
H^b\bigl(H_\Phi^a(Y,A^\bullet),d\bigr)=0
\quad\text{for }a>0,
\tag{D.5}
\]

where \(H_\Phi^a\) is ordinary or compactly supported sheaf cohomology. For \(a>N\) this follows from (D.3). Otherwise take a horizontal cocycle \(\eta\in H_\Phi^a(Y,A^b)\), and represent it by a resolution cocycle
\(u\in\Phi R^a(A^b)\).
Exactness of the sheaf resolution gives an open cover \(\{U_\lambda\}\) and sections \(v_\lambda\) of \(R^{a-1}(A^b)\) on those opens with \(\delta v_\lambda=u|_{U_\lambda}\). Choose the locally finite refinement of D.1 with compact \(\overline{V_\alpha}\subset U_{\lambda(\alpha)}\), and the operators for that refinement.

On \(U_{\lambda(\alpha)}\), apply \(R^{a-1}(p_\alpha)\) to \(v_{\lambda(\alpha)}\). The result has support in \(\overline{V_\alpha}\), because the resolution functors preserve vanishing on opens. It extends by zero to a global section \(w_\alpha\): on the overlap with \(Y\setminus\overline{V_\alpha}\) it is zero. The family is locally finite, and

\[
\delta\Bigl(\sum_\alpha w_\alpha\Bigr)
=R^a(P)u.
\tag{D.6}
\]

For compact supports, let \(K=\operatorname{supp}u\). Only finitely many \(\overline{V_\alpha}\) meet \(K\). Keep those terms in the sum. Every omitted \(R^a(p_\alpha)u\) is zero: its support lies both in \(K\) and in \(\overline{V_\alpha}\). Each retained \(w_\alpha\) has compact support, so (D.6) is then an equality of compactly supported sections as well. This is why the support control is needed, rather than an unrestricted sum of local primitives.

Equation (D.6) says that the endomorphism induced by \(P\) sends \(\eta\) to zero. Additivity and functoriality of the resolution carry \(P=1+dh+hd\) to the same homotopy identity on the complexes \(H_\Phi^a(Y,A^\bullet)\). Since \(d\eta=0\), it follows that
\(0=\eta+d(H_\Phi^a(h)\eta)\).
Thus \(\eta\) is a horizontal boundary, proving (D.5). The cover and the homotopy may depend on this cocycle; no single contraction for all cohomology classes is required.

### D.4. The comparison for the unbounded complex

In (D.4), taking resolution cohomology and then the differential of \(A\) gives

\[
E_1^{a,b}=H_\Phi^a(Y,A^b),\qquad
E_2^{a,b}=H^b\bigl(H_\Phi^a(Y,A^\bullet)\bigr).
\tag{D.7}
\]

The horizontal differential on \(E_1\) has the sign \((-1)^a\), which does not change its kernel or image. By (D.5) only \(a=0\) remains after taking that cohomology, where it is \(H^b(\Phi A)\). Here is a finite argument identifying the actual comparison map, without assuming convergence for an unbounded double complex.

The cone of the augmentation \(\Phi A\to T_\Phi(A)\) is the total complex obtained by adding \(\Phi A^b\) in resolution degree \(a=-1\). Its differential there is \(-d_A\), and its map to degree zero is the augmentation. In the resolution direction its cohomology vanishes at \(a=-1\) and \(a=0\), by left exactness; for \(a>0\) it is \(H_\Phi^a(Y,A^b)\).

Take a total cocycle \(z\), and let \(a\) be the largest resolution index with a nonzero component \(z_a\), lying in bidegree \((a,b)\). The next component of the cocycle equation says \(\delta z_a=0\). The equation one step below says that \(d_A[z_a]=0\) in resolution cohomology. If \(a>0\), (D.5) supplies a resolution cocycle \(y_a\) of bidegree \((a,b-1)\) such that
\([z_a]=(-1)^a d_A[y_a]\).
Choose \(w_{a-1}\) of bidegree \((a-1,b)\) with
\(\delta w_{a-1}=z_a-(-1)^a d_Ay_a\).
Subtracting the total boundary \(D(y_a+w_{a-1})\) removes the entire \(a\)-component. It creates no higher component, because \(\delta y_a=0\); only a lower resolution component can change.

If the largest index is \(a=0\), the zero resolution cohomology there supplies \(w_{-1}\) with \(\delta w_{-1}=z_0\), and the same subtraction with \(y_0=0\) removes it. Finally, at \(a=-1\), the equation \(\delta z_{-1}=0\) forces \(z_{-1}=0\), since the augmentation is monic. There are only the indices \(-1,0,\ldots,N\). The process therefore terminates after finitely many steps and expresses \(z\) as a boundary. It uses neither a lowest cochain degree nor any infinite sum of corrections. The comparison cone is acyclic, proving the actual natural comparison

\[
\Phi A^\bullet\xrightarrow{\sim}R\Phi(A^\bullet)
\tag{D.8}
\]

for every complex with the cover-homotopy property, including initially unbounded ones. This does not assert that each term \(A^b\) is acyclic; it is the higher-cohomology complexes in (D.5) that are acyclic.

### D.5. Applying the comparison to allowable chains

For \(A^\bullet=\mathcal J_{p,Y}^\bullet\), C.7 supplies the required operators, and C.5 identifies its ordinary sections and its compactly supported sections. The quasi-isomorphism \(\mathcal I_{p,Y}^\bullet\to\mathcal J_{p,Y}^\bullet\) therefore gives natural identifications

\[
\begin{aligned}
R\Gamma(Y,\mathcal I_{p,Y}^\bullet)
&\simeq I^pC_{-\bullet}^\infty(Y;L),\\
R\Gamma_c(Y,\mathcal I_{p,Y}^\bullet)
&\simeq I^pC_{-\bullet}^c(Y;L).
\end{aligned}
\tag{D.9}
\]

They use the maps from chains to relative germs in C.5 and the derived-section augmentation just proved, together with the derived image of \(\mathcal I\to\mathcal J\). They are not unspecified isomorphisms between groups of the same size. In particular
\(H^qR\Gamma(Y,\mathcal I_p)=I^pH_{-q}^\infty(Y;L)\)
and the compactly supported version has \(I^pH_{-q}^c\). For a complex \(d\)-dimensional variety, substituting \(q=r-2d\) gives the chain degree \(2d-r\) in Section 3.

The same proof applies on every open subset, since the space hypotheses and the compact cohomological bound pass to those subsets. This establishes the derived global and compact-support part of the comparison. Appendix E supplies the compact-link finiteness, bounded finite-rank constructibility and actual attaching-map arguments. Appendix F proves the simplicial and PL comparisons with both support conventions and explicit refinement homotopies. None of these assertions follows merely from (D.9).

## Appendix E. Finite links and the attaching morphism

We keep the field, finite-rank coefficient system and traditional perversity of Appendix B. All dimensions in this appendix are real. We treat two classes of spaces with the dimension filtration and no codimension-one strata. The first consists of pure-dimensional locally closed spaces in finite-dimensional smooth manifolds, with a finite Whitney stratification and dense regular part. The second consists of compatible conically stratified triangulated pseudomanifolds. In each case, a point on an \(s\)-dimensional stratum of a pure \(m\)-dimensional space has neighborhoods \(cK\times\mathbf R^s\), where \(K\) is a compact stratified space of dimension \(m-s-1\). The same type of local description holds recursively for its links. We now verify this assertion for the first class; for the second it is the stated conically stratified hypothesis.

For the Whitney class, [Lesson 1, I.6](constructible-complexes-on-algebraic-varieties.md#i-6-proper-stratified-submersions-and-normal-cones) constructs the actual product homeomorphism. It also proves that the compact link, as a closed fiber in a smooth level manifold, inherits a finite Whitney stratification with the frontier condition. If an incident upper stratum has dimension \(t\), its link piece has dimension \(t-s-1\). The codimension of that piece in \(K\) is therefore

\[
(m-s-1)-(t-s-1)=m-t.
\]

Thus the filtration preserves the original codimensions on the punctured normal factor, and the absence of codimension-one strata passes to the link. Density of the regular part passes to the link through the product homeomorphism: an open subset of the link missing its top pieces would give a nonempty open product missing the regular part of the original space. Its top pieces all have dimension \(m-s-1\), so the same pure-dimensional condition holds. The vertex stratum of the normal cone has codimension \(m-s\), as required in B.5 and C.4. Repeating the link construction strictly lowers dimension and stays in this class.

The coefficient system on the regular part of a normal product is pulled back from its restriction to a fixed base point and a positive radial slice. Transport along the convex base and radial factors gives this identification; the path and homotopy argument of B.1 proves independence of the chosen paths and agreement on local trivializations. Its restriction on the regular part of \(K\) is still finite-rank. Hence the coefficient systems in the cone and product formulas are precisely the systems induced by the Whitney charts.

A pure complex algebraic variety meets these hypotheses by the finite algebraic Whitney refinement in Lesson 1, K.6, applied also to its specified dense open. Every algebraic stratum has even real dimension, so a smaller stratum has real codimension at least two. Each point lies in an affine embedding, where the variety is locally closed in a Euclidean space and I.6 applies. The links and their smooth level manifolds have the same local Euclidean properties. Lesson 1, F.2, gives a uniform all-sheaf compact-cohomological-dimension bound on their open subsets; compact links use a finite coordinate cover, and the original variety uses its finite affine atlas. Local compactness, second countability and metrizability give the countable compact exhaustions constructed in D.1. Thus Appendix D applies to these spaces before any chain-sheaf constructibility assertion is proved.

We establish finite-dimensional link groups by dimension induction. For the triangulated class we use the finite-simplex argument below. For the Whitney class we use the compact constructible-cohomology argument that follows it. Neither route assumes agreement between singular and simplicial intersection chains.

### E.1. Cohomology on a finite triangulation

Let \(T\) be a finite simplicial complex of dimension \(t\), and let \(F\) be a complex of sheaves whose cohomology sheaves vanish outside \([a,b]\) and are locally constant of finite rank on every open simplex. Then

\[
\begin{gathered}
\dim_\Lambda H_c^v(T,F)<\infty,\\
H_c^v(T,F)=0\quad\text{if }v<a\text{ or }v>b+t.
\end{gathered}
\tag{E.1}
\]

Here is a proof including the cohomological inputs. A local system on an open simplex is constant. Transport a vector along a path by subdividing it into constant neighborhoods; subdividing a homotopy square shows that transport depends only on the path class. Straight-line contraction in the simplex makes all paths with the same endpoints homotopic, and supplies a trivialization. For a finite-dimensional constant coefficient space \(V\) on a real \(h\)-cell, [Lesson 1, C.1–C.5](constructible-complexes-on-algebraic-varieties.md#c-1-the-prism-and-small-chains) proves

\[
R\Gamma_c(\mathbf R^h,V)=V[-h].
\tag{E.2}
\]

In that proof the flabby singular-cochain resolution gives the sheaf comparison; the two-hemisphere sequence computes the sphere; and the support fiber for a closed ball, followed by the exact colimit over increasing balls, gives (E.2). The assertion for \(V\) follows either from the same cochain proof or from a finite basis and the result for \(\Lambda\). In dimension zero it is the point calculation.

Write \(T_h\) for the closed \(h\)-skeleton and \(U_h=T_h\setminus T_{h-1}\). For the open inclusion \(j_h\) and closed inclusion \(i_h\), the sequence
\(0\to j_{h!}j_h^*A\to A\to i_{h*}i_h^*A\to0\)
is exact for every sheaf \(A\): its stalk sequence is the identity sequence on one of the two pieces. The three functors are exact, so applying it degreewise gives the corresponding triangle for complexes. The compact-support identities for open extension by zero and closed pushforward are proved using c-soft resolutions in [Lesson 1, F.1](constructible-complexes-on-algebraic-varieties.md#f-1-compact-extension-and-exact-lifting). Applying derived compact sections to this triangle therefore relates the complexes on \(T_h\), \(T_{h-1}\) and \(U_h\).

The set \(U_h\) is a finite disjoint union of \(h\)-cells. On each one, apply the finite sequence of canonical truncation triangles with successive terms \(\mathcal H^q(F)[-q]\), \(a\leq q\leq b\). Equation (E.2) shows that these terms have finite-dimensional compact cohomology, in degree \(q+h\). The long exact sequences then give finite-dimensional groups on \(U_h\), vanishing outside \([a+h,b+h]\). Induction over the finitely many skeleta gives (E.1). This argument uses a finite number of triangles; it requires no convergence statement for an unbounded spectral sequence. Since \(T\) is compact, ordinary and compact sections, and their derived functors, agree.

We will also use the following elementary lower bound. If a complex \(A\) has no cohomology below degree \(a\), then \(R\Gamma_c(A)\) has no cohomology below \(a\) on the spaces of Appendix D. Replace \(A\) by its canonical truncation in degrees at least \(a\). The finite resolution model (D.4) has only nonnegative resolution degrees, so its total complex has no terms below \(a\). Its quasi-isomorphism invariance in D.2 proves the assertion for the original \(A\).

### E.1a. Compact Whitney spaces

For a compact space \(T\) of the Whitney class, let \(F\) be bounded with finite-rank locally constant cohomology sheaves on every stratum. Then every \(H^q(T,F)\) is finite-dimensional. The exact earlier proof is [Lesson 1, J.1–J.3](constructible-complexes-on-algebraic-varieties.md#j-1-the-coefficient-comparison-along-an-interval), together with its [local biduality criterion, G.1](constructible-complexes-on-algebraic-varieties.md#g-1-a-local-biduality-criterion-with-its-actual-comparison-maps). We recall the argument and the direction of its prerequisites.

The proper interval projection identifies a bounded complex constant along each interval fiber with the pullback of its direct image: proper base change reduces the counit's stalk map to evaluation on the contractible interval, and finite truncation triangles prove that map is an isomorphism. Applying this to a stratum-preserving homotopy identifies its two pullback maps. Shrinking a fixed normal product box by positive scaling is such a homotopy. Restriction between the nested boxes is therefore an isomorphism on derived sections. Their exact filtered colimit is the stalk, so the actual map \(R\Gamma(U,F)\to F_x\) is an isomorphism on every sufficiently small box. These section complexes are perfect because the stalk cohomology is bounded and finite-dimensional.

The local criterion G.1, proved by interleaving compact support neighborhoods with these open boxes and using the compact-support adjunction, now identifies the canonical evaluation \(F\to D_TD_TF\). It does not assume finite cohomology on the intervening compact neighborhoods. Compactness of \(T\) identifies ordinary and compact supports, so structural duality carries that evaluation to

\[
P\longrightarrow P^{\vee\vee},\qquad P=R\Gamma(T,F),
\]

and this is an isomorphism. The equality with the actual vector-complex evaluation, including its degree sign, is checked in G.1 and J.3. Linear dual is exact over a field, by extension of a linear functional from a subspace. Thus the evaluation of every \(H^q(P)\) into its algebraic double dual is onto.

For completeness, an infinite-dimensional vector space cannot have surjective evaluation. Choose a basis \(\{e_i\}\) with distinct members \(e_{i_n}\), and let \(W\subset V^\vee\) be the span of the coordinate functionals. The functional \(a\) taking value one on all \(e_{i_n}\) and zero on the remaining basis vectors is not in \(W\). On \(W+\Lambda a\), take the linear functional zero on \(W\) and one on \(a\), and extend it to \(V^\vee\) by a basis extension. Evaluation at a vector that vanishes on every coordinate functional is zero, so this extension is not evaluation at any vector. This contradiction proves finite-dimensionality. Applied degree by degree, it gives the assertion about \(F\). Its global cohomology is also bounded by the finite resolution in D.2.

All hypotheses in this argument concern ordinary constructible sheaves, the Whitney product neighborhoods, and the earlier sheaf operations. Its proof uses neither an intersection-chain comparison nor finite intersection homology of a link. In the induction below we apply it only after the chain sheaf in that dimension has been shown to be bounded with finite-rank cohomology on each stratum.

### E.2. Dimension induction for the link and the sheaf

For a compact space with a locally finite triangulation, that triangulation is finite. Each point has a neighborhood meeting finitely many simplices, and a finite collection of those neighborhoods covers the compact space. A finite complex embeds as a closed subset of \(\mathbf R^v\), where \(v\) is its number of vertices: send a point to its barycentric coordinates and realize the complex as the finite union of the corresponding standard simplices. This union is closed and compact, and the coordinate map and its inverse are continuous on each of finitely many closed simplices. Thus its open subsets satisfy the all-sheaf compact-cohomological-dimension bound of Lesson 1, F.2. In particular Appendix D applies to every triangulated compact link used below.

We prove together, by induction on the dimension \(m\), the following two assertions:

\[
\begin{aligned}
&\mathcal H^q(\mathcal I_{p,Y})=0
  &&\text{for }q\notin[-m,0],\\
&\mathcal H^q(\mathcal I_{p,Y})|_S
  &&\text{is locally constant of finite rank on each stratum }S;
\end{aligned}
\tag{E.3}
\]

and, when \(Y\) is compact,

\[
\begin{gathered}
\dim_\Lambda I^pH_i^c(Y;L)<\infty,\\
I^pH_i^c(Y;L)=0\quad\text{for }i<0\text{ or }i>m.
\end{gathered}
\tag{E.4}
\]

For \(m=0,1\) there is no singular stratum. B.7 gives the sole cohomology sheaf \(L\otimes\operatorname{or}_Y\) in degree \(-m\); it has finite rank. If \(Y\) is compact, E.1 in the triangulated case, or E.1a in the Whitney case, gives finite-dimensional hypercohomology. Equation (D.9) identifies this with its finite-chain homology. The lower bound just proved gives vanishing for \(i>m\); negative homological degrees have no chains. This proves both assertions at the start of the induction. No orientation of a link is assumed: an orientation local system still has rank one.

Suppose the assertions hold in all smaller dimensions. At a regular point of \(Y\), use B.7 again. At a point of a singular stratum of dimension \(s\), put \(k=m-s\). Its compact link \(K\) has dimension \(k-1<m\), so its finite-chain intersection homology is finite-dimensional and vanishes above \(k-1\), by the induction hypothesis. Formula (C.10) expresses each retained stalk group as
\(I^pH_{-q-s-1}^c(K;L)\).
If \(q<-m\), then \(-q-s-1>m-s-1=k-1\), so that group vanishes. The groups with \(q>0\) vanish already at the chain level. Every remaining stalk group is finite-dimensional, and the actual local sections in C.4 show that these groups form locally constant sheaves along the stratum. This proves (E.3), uniformly in \(q\), on \(Y\).

If \(Y\) is compact and triangulated, its finite compatible triangulation has each open simplex inside a stratum. The just-proved (E.3) therefore meets the hypotheses of E.1, with \(a=-m,b=0\). If \(Y\) is in the Whitney class, (E.3) instead meets the hypotheses of E.1a on its given finite stratification. Both arguments give finite-dimensional \(H^qR\Gamma_c(Y,\mathcal I_{p,Y})\). The lower bound gives zero for \(q<-m\), and (D.9) identifies these groups with \(I^pH_{-q}^c(Y;L)\). Negative homological degrees vanish directly. This proves (E.4) in dimension \(m\), closing the induction. The order matters: boundedness and finite stalk ranks in dimension \(m\) use compact-link homology only in smaller dimensions; compact homology in dimension \(m\) is obtained afterwards.

Consequently the singular allowable-chain sheaf is bounded and constructible in both classes, including the algebraic Whitney stratifications in Section 3. The finite-dimensional result also applies to every compact link, including disconnected links and arbitrary finite-rank local coefficients. There is no assertion here that an individual singular chain group is finite-dimensional.

### E.3. Restricting the cone representatives to its puncture

Let \(N=cK\times\mathbf R^s\), \(Z=\{v\}\times\mathbf R^s\), and \(W=N\setminus Z\), with \(\dim cK=n\). We identify the actual restriction on derived sections in the range

\[
i\geq n+s-p(n),\qquad j=i-s-1\geq n-1-p(n).
\tag{E.5}
\]

Every class of \(I^pH_i^\infty(N;L)\) has the representative
\(\xi=c\gamma\times\mathbf R^s\)
of C.3, where \(\gamma\) is a finite allowable \(j\)-cycle on \(K\). We use the radial coordinate \(0\leq r<\infty\). The initial cone piece occupies \([0,1]\); outside it the chain consists of the radial product pieces of C.3. Coefficients are transported radially, and the Euclidean factors use their oriented cube triangulation.

For each \(l\geq0\), subdivide the initial cone models by the radial levels \(2^{-h}\), \(0\leq h\leq l\). Retain the smaller cone below \(2^{-l}\), and triangulate each intervening truncated-cone polytope. These are finite polytopes in the barycentric coordinates of a cone simplex. Triangulate their faces first and cone their boundary triangulations to interior points. Use identical choices on equal parametrized faces, and then on their products with the Euclidean cubes. At stage \(l+1\), only the inner cone is changed. The old skeletons are subcomplexes of these cuts, so the inverse-image estimates of B.2 preserve allowability. Nonallowable boundary faces still cancel because the face subdivisions agree.

Write \(\xi_l\) for the resulting cycle. Before multiplying by the Euclidean fundamental chain, the difference between two consecutive subdivisions is a finite cycle \(\eta_l\) of dimension \(j+1\) on the cone: the exterior radial pieces agree and cancel. It is supported in \(r\leq2^{-l}\). Cone this difference to the vertex, using B.5, and then multiply by the Euclidean fundamental chain. The resulting allowable locally finite chain \(h_l\) satisfies

\[
\partial h_l=\xi_{l+1}-\xi_l,
\qquad |h_l|\subset\{r\leq2^{-l}\}.
\tag{E.6}
\]

Indeed \(\partial(v*\eta_l)=\eta_l\) by the cone boundary formula. The new vertex bound is \(j+2-n+p(n)\geq1\), and the nonvertex bounds are precisely the cone estimates of B.5. Coning can only decrease the radius. The product boundary is \(\partial(v*\eta_l)\times[\mathbf R^s]\), because the locally finite Euclidean fundamental chain has zero boundary; its unit-cube faces cancel. This proves (E.6) with its sign and support bound. The outer radius-one triangulation can initially be chosen as this same model; thus \(\xi_0=\xi\).

On \(W\) the cycles \(\xi_l\) stabilize locally to a locally finite allowable radial-cylinder cycle \(\beta\). Indeed a compact subset of \(W\) has a positive minimum radius and bounded Euclidean coordinates; it meets finitely many annuli, cubes and original simplices. For the same reason \(\sum_l h_l|_W\) is a locally finite sum of sections of the ambient sheaf \(\mathcal J_{p,N}|_W\). No local finiteness at \(Z\) is asserted for this sum. Telescoping (E.6), now as an equality of sections on \(W\), gives

\[
\beta_{\mathrm{amb}}-\xi|_W
 =\partial\Bigl(\sum_{l\geq0}h_l|_W\Bigr).
\tag{E.7}
\]

The notation \(\beta_{\mathrm{amb}}\) has a precise finite-chain meaning. Around a relatively compact open subset of \(W\), choose a finite radial band with dyadic endpoints and a finite Euclidean cube box containing its closure in their interiors. The restriction of \(\beta\) to the whole band and box is a finite intersection chain: its exposed boundary faces are copies of \(\gamma\) times faces of the interval and box, so they are allowable. Its boundary is away from the chosen closure. Enlarging the band and box changes this representative only away from that closure. These representatives define a section of \(\mathcal I_{p,W}\), whose image under the finite-chain inclusion (C.12) and \(\mathcal I_{p,N}\to\mathcal J_{p,N}\) is exactly \(\beta_{\mathrm{amb}}\). They also map to the ordinary section of \(\mathcal J_{p,W}\) represented by the locally finite chain \(\beta\). Thus (E.7) compares the native and ambient sheaves through their actual maps.

Under (C.8), the class of \(\beta\) is the link class \([\gamma]\), with the same connecting-map orientation convention as for \(\xi\) in (C.7). One can check this on a finite band and box: perform the successive relative connecting maps of C.1; the oriented radial boundary is the upper slice minus the lower slice, and the selected slice is the original \(\gamma\). Cutting the Euclidean coordinates gives the remaining successive connecting maps. A geometric slice of a cone model has barycentric coordinates \(b_a=r u_a\); at a fixed positive \(r\), its parametrization is the original base simplex in the \(u_a\)'s. Hence these slices are the actual chain \(\gamma\), not merely cycles with equal dimensions. Equivalently, put the increasing radial coordinate before the \(j\) base coordinates and then the Euclidean coordinates. Moving the radial coordinate after the base coordinates multiplies the representative by \((-1)^j\); use the same specified convention in both comparisons.

### E.4. The derived attaching map

The comparison (D.9) takes the chain \(\xi\) to its relative-germ section and then to derived sections. The derived restriction
\(R\Gamma(N,\mathcal I_{p,N})\to R\Gamma(W,\mathcal I_{p,N}|_W)\)
is compatible with restriction of those sections. The open comparison (C.12) identifies its target with \(R\Gamma(W,\mathcal I_{p,W})\). Equation (E.7) says that the restricted class is the image of the native class of \(\beta\): a boundary of ordinary sections maps to a boundary under the natural map to derived sections. This argument does not require ordinary sections of an arbitrary restricted complex to compute its derived sections.

By (C.7)–(C.8), the source and target in homological degree \(i\) are both the link group in (E.5), and their representative maps are isomorphisms. The preceding computation shows that the actual derived restriction carries the representative of each \([\gamma]\) to its corresponding representative. It is therefore an isomorphism for every \(i\) in (E.5), including equality. In cohomological indices its range is \(q\leq p(n)-(n+s)\).

For the inclusion \(a:U\hookrightarrow V\) adding a stratum of real codimension \(n\) to the previously included strata, the stalk of \(Ra_*\mathcal I_{p,U}\) at a point of that new stratum is the exact filtered colimit of the derived sections on the deleted distinguished neighborhoods. This follows by taking an injective resolution and then stalks: restriction to an open preserves injectives by the exact extension-by-zero adjunction of Lesson 1, A.1, and filtered colimits commute with cohomology. Boundedness from E.2 allows a bounded-below resolution here. The source stalk is the analogous colimit on the full neighborhoods, or the stable group in C.4. Naturality of the finite-chain inclusion and of the section-to-derived-section map makes the preceding restriction computation the stalk map of the unit \(\mathcal I_{p,V}\to Ra_*\mathcal I_{p,U}\). Distinguished neighborhoods are cofinal, and the computation applies after every shrinking. Consequently

\[
\mathcal H^q(\mathcal I_{p,V})_x
 \xrightarrow{\ \sim\ }
\mathcal H^q(Ra_*\mathcal I_{p,U})_x
\quad(q\leq p(n)-m).
\tag{E.8}
\]

On \(U\) the unit is already an isomorphism. The upper stalk cutoff is (C.10). At every earlier stratum it is no larger than the new cutoff, because \(p\) is nondecreasing; the regular degree is \(-m\). Thus the candidate on \(V\) has no cohomology above \(p(n)-m\), and the unit factors through that canonical truncation of \(Ra_*\). Equation (E.8) and the upper cutoff make this factor a quasi-isomorphism on every stalk. This is the actual successive-truncation comparison used in Section 3.

### E.5. Normalization and the two support conventions

For the pure complex \(d\)-dimensional variety, B.7 fixes the regular restriction as \(L[2d]\). Applying E.4 successively at complex codimension \(r\), with \(p(2r)=r-1\), identifies the singular allowable-chain sheaf with the successive extension having cutoff \(r-1-2d\). Section 1 and the uniqueness argument of Section 3 identify that complex with \(\operatorname{IC}(X,L)[d]\). Together with (D.9), this gives

\[
\begin{aligned}
H^{r-d}(X,\operatorname{IC}(X,L))
 &\simeq I^{\overline m}H_{2d-r}^{\infty}(X;L),\\
H_c^{r-d}(X,\operatorname{IC}(X,L))
 &\simeq I^{\overline m}H_{2d-r}^{c}(X;L).
\end{aligned}
\tag{E.9}
\]

Indeed \(H^{r-2d}(\operatorname{IC}[d])=H^{r-d}(\operatorname{IC})\), and the chain degree in (D.9) is the negative of \(r-2d\). The chain-to-section and attaching maps determine these identifications with the chosen regular normalization.

This proves the singular allowable-chain comparison for the algebraic Whitney models in Section 3 as well as the conically stratified triangulated models. The Whitney route uses the proved normal product charts and E.1a for compact-link finiteness. The subdivisions in E.3 triangulate polytopes in the model domains of individual singular simplices; they impose no triangulation on the link itself. Appendix F separately compares singular and simplicial allowable chains for a compatible triangulated model and proves compatibility with PL refinement, giving the remaining chain conventions in Section 3. Appendix H constructs the required global filtered realization at the separated finite-type algebraic scope.


## Appendix F. Simplicial chains and PL refinement

We compare the singular chains of Appendix B with oriented simplicial chains, keeping the coefficient system and the support convention throughout. Let \(K\) be a finite-dimensional locally finite simplicial complex, with a finite filtration by subcomplexes \(K_j\), where \(K_n=K\) and \(K_{n-1}=K_{n-2}\). Write \(X=|K|\). The local system \(L\) is defined on \(X\setminus|K_{n-2}|\), and \(p\) is a traditional perversity. Restrictions to subcomplexes keep these same filtration indices and the same numbers \(k-p(k)\). In particular, the geometric dimension of a subcomplex does not replace the ambient index \(n\).

### F.1. The inclusion and the role of fullness

A filtered triangulation is **full** if every \(K_j\) is a full subcomplex: the vertices of a simplex that belong to \(K_j\) span a face in \(K_j\). Equivalently, the intersection of a simplex with \(|K_j|\) is one face, possibly empty. One barycentric subdivision makes any compatible triangulation full. Its vertices are old faces, and a new simplex is a nested chain of such faces. Those belonging to \(K_j\) form an initial segment, since \(K_j\) contains every face of any one of its simplices. That segment spans exactly the required face.

Order the vertices, compatibly on faces. Decorate an oriented simplex by a section of \(L\) on its regular part, with the boundary restriction convention of B.1. Call an \(i\)-simplex simplicially allowable if
\(\dim(\sigma\cap K_{n-k})\leq i-k+p(k)\) for every \(k\geq2\), interpreting the dimension of the empty face as \(-\infty\). An intersection chain has allowable top simplices and allowable boundary after cancellation. Denote these complexes by \(I^pC_*^{\epsilon,\mathrm{sim}}(K;L)\), where \(\epsilon=c\) means finite chains and \(\epsilon=\infty\) means locally finite chains. Use the ordered affine parametrization of each simplex to define

\[
\iota_K:I^pC_*^{\epsilon,\mathrm{sim}}(K;L)
\longrightarrow I^pC_*^\epsilon(X;L).
\tag{F.1}
\]

The parametrizations agree on every ordered face, so this is a chain map. Fullness turns the dimension inequality into the skeleton condition (B.1). Local finiteness of the triangulation ensures that a locally finite simplicial chain is locally finite as a singular chain. We will prove that (F.1) induces an isomorphism on homology for either support convention. No comparison for a triangulation that is not full is assumed.

### F.2. A join calculation with its actual maps

Suppose \(q<n\) is the least index with \(K_q\ne\varnothing\), and let \(b=\dim K_q\). Choose a \(b\)-simplex \(\beta\) of \(K_q\), put \(M=\operatorname{link}_K\beta\), and write
\(J=\beta*M\). This is the closed star of \(\beta\). The link has no vertex in \(K_q\): such a vertex, together with \(\beta\), would span a \((b+1)\)-simplex in the full subcomplex \(K_q\). Thus \(J\cap K_q=\beta\). Put \(a=n-q\) and \(t=a-1-p(a)\). Since \(K_{n-1}=K_{n-2}\), we have \(a\geq2\) and \(t\geq1\).

For a nonempty face \(\alpha\subset\beta\) and a simplex \(\eta\subset M\), the join \(\alpha*\eta\) is allowable precisely when \(\eta\) is allowable with the inherited filtration and \(\dim\eta\geq t\). Indeed, writing \(u=\dim\alpha\) and \(v=\dim\eta\), the inequality at \(K_q\) is
\(u\leq u+v+1-a+p(a)\), or \(v\geq t\). At any larger filtration step, its intersection is \(\alpha*(\eta\cap K_j)\); subtracting \(u+1\) gives the link inequality. If that link intersection is empty, the condition is weaker than the one at \(K_q\), since \(k-p(k)\) is nondecreasing. A simplex wholly in \(\beta\) is never allowable.

For both simplicial and singular finite chains, inclusion of the link gives

\[
\begin{aligned}
I^pH_i(J;L)&\simeq I^pH_i(M;L)&& (i<t),\\
I^pH_i(J;L)&=0&& (i\geq t).
\end{aligned}
\tag{F.2}
\]

Here the notation in each line is taken entirely in either chain convention. For simplicial chains of degree \(i<t\), neither degree \(i\) nor degree \(i+1\) has an allowable simplex meeting \(\beta\): such a simplex has dimension at least \(t+1\). Consequently the relevant chains and boundaries are those of \(M\). For \(i\geq t\), cone an \(i\)-cycle to a fixed vertex \(v_0\) of \(\beta\). The oriented simplicial cone is zero on a simplex already containing \(v_0\), and on the other simplices it is \(v_0*\sigma\), with the usual alternating orientation. If \(\sigma\) meets \(\beta\), coning increases the intersection dimension and total dimension together. If it lies in \(M\), the new bottom vertex is permitted exactly because \(i\geq t\). Thus the cone is allowable. The identity \(\partial(v_0*z)=z\) for a positive-degree cycle proves vanishing; \(t\geq1\) excludes the augmentation exception in degree zero.

For singular chains in degrees \(i,i+1\) with \(i<t\), condition (B.1) excludes \(\beta\), because \(i+1-a+p(a)=i-t<0\). The complement \(J\setminus\beta\) retracts to \(M\) by increasing the total link barycentric weight to one. Every point stays in its original filtration stratum. The finite-chain prism of B.2 gives the same low-degree isomorphism, induced by the actual inclusion. In degrees \(i\geq t\), cone a finite singular cycle straight to \(v_0\). For the bottom stratum, the preimage in the cone model is the new vertex together with the cone on the old preimage. Its permitted skeleton has dimension \(i+1-a+p(a)=i-t\geq0\). For the other strata, the old permitted skeleton gains at most one dimension, and their bounds are weaker at the new vertex. The boundary computation of B.5 is therefore valid with this ambient codimension \(a\), and again bounds the cycle.

These operations respect the given local coefficients. The regular part of the join retracts to the regular part of \(M\) by the same radial paths. Transport identifies the restricted local system with its pullback from that link. Each coning path remains regular except possibly at its final vertex in \(\beta\), where the coefficient is zero by B.1. The path and rectangle argument in B.1 makes these identifications compatible on faces. No global trivialization of \(L\) on the link is needed.

The low-degree maps in (F.2) commute with \(\iota\). The high-degree groups vanish in both conventions. It follows that a comparison isomorphism for \(M\) gives the comparison for \(J\). The star \(J\) is finite, since local finiteness gives finitely many simplices incident to any vertex of \(\beta\); thus its locally finite chains are also finite.

### F.3. Removing the largest bottom faces

For any nonempty filtered complex, let \(q\) be its lowest nonempty filtration index and \(b=\dim K_q\). We induct on the ordered pair \((n-q,b)\), first on \(n-q\), then on \(b\). The empty complex is already settled. Induced subcomplexes always retain the ambient filtration indices.

Let \(\mathcal B\) be the family of \(b\)-simplices in \(K_q\). Define a residual subcomplex \(R\) to consist of those simplices \(\sigma\) for which \(\dim(\sigma\cap K_q)<b\). It is a subcomplex because passing to a face cannot increase that dimension. For \(\beta\in\mathcal B\), set
\(J_\beta=\beta*\operatorname{link}_K\beta\) and
\(A_\beta=\partial\beta*\operatorname{link}_K\beta\). Then
\(K=R\cup\bigcup_\beta J_\beta\),
\(J_\beta\cap R=A_\beta\), and distinct stars intersect only inside \(R\). These assertions follow by assigning a simplex outside \(R\) its unique full face of dimension \(b\) in \(K_q\). In particular \(R\) and each \(A_\beta\) have smaller induction pair. If \(\beta\) is a vertex, the convention gives \(A_\beta=\operatorname{link}_K\beta\).

The family of closed stars is locally finite. A compact set meets finitely many simplices of a locally finite triangulation: choose at each point a neighborhood meeting finitely many simplices and take a finite subcover. Each of those simplices has finitely many vertices and finitely many incident simplices, so it meets only finitely many of these stars. Every star is compact and finite.

For simplicial chains the natural sum of pair inclusions is an isomorphism of relative chain complexes:

\[
\begin{aligned}
I^pC_*^{c,\mathrm{sim}}(K,R)
 &\simeq\bigoplus_{\beta\in\mathcal B}
 I^pC_*^{c,\mathrm{sim}}(J_\beta,A_\beta),\\
I^pC_*^{\infty,\mathrm{sim}}(K,R)
 &\simeq\prod_{\beta\in\mathcal B}
 I^pC_*^{c,\mathrm{sim}}(J_\beta,A_\beta).
\end{aligned}
\tag{F.3}
\]

We check the boundary condition, since arbitrary separation of an intersection chain need not preserve it. Group its terms outside \(R\) by their unique face \(\beta\), obtaining \(c_\beta=\beta*e_\beta\), and put the remaining terms in \(f\). When \(q<n\), F.2's inequality says that every term in \(e_\beta\) is allowable and has degree at least \(t\). The boundary terms \(\partial\beta*e_\beta\) are allowable by the same inequality. For a vertex \(\beta\) this boundary contribution is simply \(e_\beta\). The other terms are \((-1)^{b+1}\beta*\partial e_\beta\). A nonallowable face among these still contains the full \(\beta\), so it cannot cancel against \(f\) or a term with another bottom face. Its total coefficient must already be zero in \(\partial c_\beta\). Hence \(c_\beta\) is an intersection chain, and subtracting these chains shows that \(f\) is one as well. At the limiting degree \(\deg e_\beta=t\), this says \(\partial e_\beta=0\), since its join would otherwise violate the bottom bound. If \(q=n\), there is no allowability restriction and the same grouping is immediate.

This proves surjectivity in (F.3). If a sum of star chains belongs to \(R\), every coefficient outside \(R\) is zero in its unique star, so every summand belongs to \(A_\beta\). That proves injectivity. For locally finite chains each individual star contribution is finite. Conversely any family of finite star chains is locally finite in \(K\), because the stars are a locally finite family of compact sets. This proves the product assertion as well as its compatibility with the differential.

### F.4. The singular relative decomposition and its support

Let \(z_\beta\) be the barycenter of \(\beta\), let \(P=\{z_\beta:\beta\in\mathcal B\}\), and put \(W=X\setminus P\). This is open, since \(P\) is a locally finite set of closed points. Each star is the geometric cone \(z_\beta*A_\beta\). On its puncture a point has unique coordinates
\(x=(1-r)z_\beta+r y\), with \(0<r\leq1\) and \(y\in A_\beta\). Increasing \(r\) to one retracts that puncture to \(A_\beta\). The maps fix \(R\), agree on intersections, and form a continuous homotopy on \(W\): the closed-star family is locally finite, so the usual finite closed-set pasting argument applies near every point. If \(A_\beta\) is empty, the puncture is empty and requires no map.

This homotopy preserves every original stratum. On a ray whose link coordinate is nonzero, that coordinate remains nonzero and its filtration index does not change. A ray inside \(\beta\) ends on \(\partial\beta\), still in the lowest stratum. Thus B.2, with coefficient transport along these rays, gives a finite-chain equivalence between \(R\) and \(W\).

For locally finite chains we use \(I^pC_*^\infty(W_X)\), the subcomplex defined in B.1 by local finiteness in \(X\). The homotopy also preserves this condition. Given a compact target set \(C\subset X\), only finitely many stars meet \(C\). Every original simplex whose image during the homotopy meets \(C\) either already meets \(C\) in the fixed residual part, or meets one of those finitely many compact stars. The original chain is locally finite in \(X\), so there are only finitely many such simplices. Each supplies finitely many prism simplices. Their union is locally finite in \(X\), as required. This argument supplies the support control directly; properness of the punctured-space retraction is unnecessary. Since \(R\) is closed, its native locally finite chains have exactly this ambient support condition.

The resulting chain equivalence for the subcomplexes implies that
\(I^pH_*^\epsilon(X,R)\to I^pH_*^\epsilon(X,W_X)\)
is an isomorphism. This follows from their relative long exact sequences, using the identity on the ambient complex. Now put \(V=X\setminus|R|\). The two open sets \(V,W\) cover \(X\), and B.3's support-preserving subdivision and homotopy identify the latter relative group with the homology of
\(I^pC_*^\epsilon(V_X)/I^pC_*^\epsilon((V\cap W)_X)\).

The space \(V\) is the disjoint union of the sets \(V_\beta=|J_\beta|\setminus|A_\beta|\), each open and closed in \(V\). A singular simplex has connected image, so one supported in \(V\) lies in a single \(V_\beta\). Every ambient locally finite chain in a fixed \(V_\beta\) is finite, because its support is contained in the compact \(J_\beta\). Conversely a family of finite chains in these sets is ambient locally finite, by local finiteness of the stars. Thus this quotient complex is the direct sum, for finite support, or product, for locally finite support, of the finite relative complexes
\(I^pC_*^c(V_\beta,V_\beta\setminus\{z_\beta\})\).

Apply the same two-open excision within the finite star \(J_\beta\). It identifies these relative groups with those of \((J_\beta,J_\beta\setminus\{z_\beta\})\). The radial retraction identifies the latter with \((J_\beta,A_\beta)\). All maps just used come from inclusions of pairs, quotient maps, or their proved inverse maps on homology. Consequently the natural sum of pair inclusions induces

\[
\begin{aligned}
I^pH_*^c(X,R;L)
 &\simeq\bigoplus_{\beta\in\mathcal B}
 I^pH_*^c(J_\beta,A_\beta;L),\\
I^pH_*^\infty(X,R;L)
 &\simeq\prod_{\beta\in\mathcal B}
 I^pH_*^c(J_\beta,A_\beta;L).
\end{aligned}
\tag{F.4}
\]

Products commute with homology here. Kernels are computed coordinatewise; a family of boundaries has a family of preimages, chosen coordinatewise, so the image of the product differential is the product of its images. Direct sums have the same property, choosing zero preimages outside a finite set. These facts also prove exactness of the products and sums used above. The constructions show that (F.3), (F.4), and the maps induced by \(\iota\) form a commuting diagram.

### F.5. Induction proving the comparison

Assume the assertion has been proved for smaller pairs \((n-q,b)\), in both support conventions. It holds for \(R\) and every \(A_\beta\) by F.3. If \(q<n\), the link of \(\beta\) has no \(K_q\)-vertex and hence has smaller first coordinate, or is empty. Its comparison and the actual link inclusions in F.2 give the comparison for \(J_\beta\).

If \(q=n\), the complex is wholly regular and each \(\beta\) is a top-dimensional simplex of \(K\). Its star is that simplex itself. Transport to a chosen vertex trivializes \(L\) on it: straight segments and straight homotopies in the simplex give path independence by B.1. The ordinary cone contracts each chain complex to that coefficient fiber; equivalently, it contracts the corresponding augmented complex. Hence the unaugmented homology is the coefficient fiber in degree zero and zero in higher degrees, and \(\iota\) is the identity on that fiber. This proves the needed star comparison, including the zero-dimensional induction base. A singular point complex need not have zero chain groups in positive degrees; it is the cone contraction that proves their acyclicity.

The short exact sequences of the two chain conventions for \((J_\beta,A_\beta)\) now give the relative comparison. For clarity, the long-exact-sequence argument used here has the following representative description. For surjectivity on relative homology, lift a target relative class's boundary through the isomorphism on \(A_\beta\). Its image in \(J_\beta\) is zero, since that map is injective on homology and the target boundary dies there. Exactness gives a source relative lift. The difference of its image from the target class has zero boundary, hence comes from absolute homology of the star; lift that difference through the star isomorphism and correct the relative lift. For injectivity, a source relative class mapping to zero has zero boundary by injectivity on \(A_\beta\), so it comes from a star class. Its target star image comes from \(A_\beta\); lift that class through the isomorphism on \(A_\beta\). Subtracting it leaves a star class with zero image, which vanishes by injectivity for the star. Thus the original relative class is zero.

Applying sums or products to these relative isomorphisms, F.3–F.4 give the relative comparison for \((K,R)\). The same exact-sequence argument with the already established comparison for \(R\) proves

\[
H_i(\iota_K):I^pH_i^{\epsilon,\mathrm{sim}}(K;L)
\xrightarrow{\ \simeq\ }I^pH_i^\epsilon(X;L),
\qquad \epsilon\in\{c,\infty\}.
\tag{F.5}
\]

Both coordinates of the induction pair are finite nonnegative integers and strictly decrease at each invocation. Local finiteness, rather than a finite exhaustion argument, justifies all infinite products. This proves (F.5) for the entire locally finite triangulation.

### F.6. Refinement and the PL chain complex

Let \(K'\) be a full compatible subdivision of \(K\), extending the chosen order to the new vertices. An old oriented simplex is the signed sum of the new top-dimensional simplices contained in it, each given the restricted coefficient. This defines the subdivision map \(S_{K'K}\). Internal faces cancel, and the subdivisions agree on the old boundary, so \(S\partial=\partial S\). Each new simplex meets an old filtration face in a face of dimension no larger than the original intersection. The allowability bound and, by the chain-map identity, the boundary condition are preserved. There are finitely many new pieces in each old simplex because it is compact and the subdivision is locally finite. Their supports stay in that simplex, so the map preserves both support conventions.

In the singular chain complex, compare the ordered affine parametrizations before and after subdivision by B.2's prism. On each old simplex choose the prism triangulation with prescribed subdivisions on its faces; the inductive coning construction in B.2 supplies compatible choices. It gives an operator \(D_{K'K}\) satisfying

\[
\partial D_{K'K}+D_{K'K}\partial
=\iota_{K'}S_{K'K}-\iota_K.
\tag{F.6}
\]

The old filtration faces times the interval are subcomplexes of the prism; their dimensions increase by one. Thus its top simplices are allowable, and the identity proves boundary allowability. Its support lies inside the old simplex, so this homotopy is defined for locally finite as well as finite chains. By (F.5) and (F.6), every such subdivision induces an isomorphism on intersection homology.

Fix the PL structure of the given compatible triangulation. Its admissible triangulations have common locally finite subdivisions; this is the common-refinement convention in the definition of a PL structure. Concretely, on compatible affine pieces a common subdivision is obtained by intersecting the simplices, triangulating the faces of the resulting convex polytopes in increasing dimension, and coning each triangulated boundary to an interior point. The choices agree on shared faces. Local finiteness makes the construction finite on each compact piece. Requiring the filtration subcomplexes to be subdivided as well preserves compatibility. Full compatible triangulations are cofinal among these triangulations, by F.1's barycentric subdivision argument.

Define the PL intersection chain complex by oriented geometric chains modulo this subdivision identification:

\[
I^pC_*^{\epsilon,\mathrm{PL}}(X;L)
=\underset{K'}{\operatorname{colim}}\,
I^pC_*^{\epsilon,\mathrm{sim}}(K';L).
\tag{F.7}
\]

The transition maps are the actual oriented subdivisions just constructed. They compose exactly: a final small simplex occurs once with its induced orientation and restricted coefficient. This is also the description by allowable PL supports and allowable boundary supports. In a common compatible triangulation, open simplices in a geometric chain are disjoint; the bound on the dimension of its intersection with each filtration subspace is exactly the bound on each simplex with nonzero coefficient. Impose the same condition after boundary cancellation. Conversely these inequalities make that geometric chain an element of the simplicial intersection complex. A locally finite PL chain is represented on a locally finite subdivision compatible with its pieces; on each compact set there are finitely many pieces, and the preceding face-by-face refinement makes them simultaneous simplices. Thus (F.7) retains the locally finite convention as well.

Filtered colimits of these complexes commute with homology. A cycle in the colimit is represented at one stage; its boundary is zero at a later stage because equality in a filtered colimit is witnessed at a common later index. If a represented cycle becomes a boundary, the bounding chain and that equality likewise occur at a common later stage. This proves the assertion directly, without commuting a colimit with an infinite product. In conjunction with (F.5)–(F.6), it gives

\[
I^pH_i^{\epsilon,\mathrm{PL}}(X;L)
\simeq I^pH_i^\epsilon(X;L),
\qquad \epsilon\in\{c,\infty\}.
\tag{F.8}
\]

The map sends a class represented on any full triangulation to the class of its ordered affine singular chain. Formula (F.6) proves independence of refinement. The affine inclusions are compatible up to that explicit homotopy; a literal chain map out of the colimit is not being inferred from strict compatibility. Combining (F.8) with (E.9) proves the simplicial and PL versions of the intersection-chain comparison with the same shifts, coefficient system, and finite or locally finite support convention.


## Appendix G. Local orientations and the integral quotient calculation

This appendix supplies the classical dualizing-complex identification in Section 3 and the integral cell calculation in Section 5. We first work over the field \(\Lambda\). In G.4–G.5 the singular chains and cochains instead have integral coefficients, so that the torsion is retained.

### G.1. From point support to compact support

We first construct a basis of relatively compact neighborhoods \(U=C_{<1}(T)\) centered at a given point, where \(T\) is compact and metrizable. For a complex algebraic variety, use the finite Whitney stratification constructed in [Lesson 1, K.6](constructible-complexes-on-algebraic-varieties.md#k-6-finite-compatible-whitney-refinements). Its [normal local-triviality proof, I.6](constructible-complexes-on-algebraic-varieties.md#i-6-proper-stratified-submersions-and-normal-cones), gives a neighborhood of a point \(x\) in the form

\[
B\times c_{<\delta}L,\qquad x=(0,v),
\]

where \(B\subset\mathbf R^s\) is a coordinate neighborhood of its stratum and \(L\) is a compact link. The link is metrizable because it is the closed fiber in the Euclidean tube used in that construction. Let \(r\) denote the cone parameter of this product. Choose \(\epsilon>0\) with \(\overline B_{2\epsilon}(0)\subset B\) and \(2\epsilon<\delta\). Put \(\rho=(\|u\|^2+r^2)^{1/2}\).

If \(s>0\) and \(L\) is nonempty, form the compact join \(T=S^{s-1}*L\): take \(S^{s-1}\times L\times[0,\pi/2]\), collapse the \(L\)-coordinate at \(\theta=0\), and collapse the sphere coordinate at \(\theta=\pi/2\). The map

\[
\bigl([a,l,\theta],\rho\bigr)
\longmapsto
\bigl(\rho\cos\theta\,a,[l,\rho\sin\theta]\bigr)
\]

identifies the closed cone of radius \(\epsilon\) on \(T\) with the subset \(\rho\leq\epsilon\) of the product neighborhood. It is continuous and onto. Away from the cone vertex, the two lengths determine \(\rho\) and \(\theta\); the nonzero coordinates determine \(a\) and \(l\), and exactly the prescribed join identifications handle a zero coordinate. Thus it is injective after the vertex and join collapses. Its domain is compact and its target is Hausdorff, so its inverse is continuous: images of closed subsets are compact, hence closed. Restricting gives an open cone for \(\rho<\epsilon\), and rescaling its radius gives \(C_{<1}(T)\).

If \(s=0\) and \(L\ne\varnothing\), take \(T=L\). If \(L=\varnothing\), the normal neighborhood in I.6 is just \(B\); for \(s>0\) its centered balls are cones on \(S^{s-1}\). When both are absent, the point is isolated: its supported and compactly supported cohomology are both \(\Lambda\) in degree zero, with the identity comparison. These cases cover smooth points and zero-dimensional components as well. Smaller radii are cofinal among neighborhoods of the center: an open set about \((0,v)\) contains a product of a small base ball and a sufficiently short full cone, the latter assertion following from compactness of \(L\). Each closed radial subcone is compact and lies inside the original chart. This proves the required relatively compact neighborhood basis.

For a locally finite finite-dimensional polyhedron the same basis also has a simplicial construction. If the point lies inside a simplex \(\sigma\), subdivide its closed star by replacing \(\sigma*\operatorname{link}\sigma\) with \(x*\partial\sigma*\operatorname{link}\sigma\). Radial linear maps on the constituent simplices fix the boundary and give the same underlying space. Only finitely many simplices are involved, by local finiteness. The open star of the new vertex is an open cone on its finite link. Taking smaller radii gives the same centered-cone basis.

Write \(H_x^a(U;\Lambda)=H^a(U,U\setminus\{x\};\Lambda)\). The centered cones contract by radial scaling. Repeating the construction at every point gives a basis of contractible open neighborhoods, also on each open puncture. The neighborhoods are locally compact, second countable and metrizable, as open subsets of the displayed product charts; the polyhedral case has the same properties. Thus [Lesson 1, C.1–C.3](constructible-complexes-on-algebraic-varieties.md#appendix-c-sheaf-cohomology-of-the-cone-and-local-orientation-groups) applies to their sheaf and singular relative cohomology, including the restriction maps defining the support fiber. For \(0<t<1\), let \(K_t\) be the closed cone of radius \(t\). These sets are compact and cofinal among compact subsets of \(U\): the continuous radius has maximum less than one on every compact subset. The inclusion
\(U\setminus K_t\hookrightarrow U\setminus\{x\}\)
is a homotopy equivalence: both retract radially to \(T\), and a map moving radii into \((t,1)\) gives an inverse up to radial homotopy. The support fiber sequence therefore identifies inclusion of supports with an isomorphism
\(H_x^a(U)\to H_{K_t}^a(U)\).

Compactly supported cohomology is the filtered colimit of these supported groups. Indeed, apply the equality \(\Gamma_c=\operatorname{colim}_{K}\Gamma_K\) to an injective resolution and use exactness of filtered colimits, as in Lesson 1, C.5. We obtain the actual support map

\[
H_x^a(U;\Lambda)\xrightarrow{\ \simeq\ }H_c^a(U;\Lambda).
\tag{G.1}
\]

If \(V\subset U\) is a smaller centered cone, support excision identifies \(H_x^a(V)\) with \(H_x^a(U)\). Under (G.1), this is exactly extension by zero \(H_c^a(V)\to H_c^a(U)\). The reason is that all maps are induced by including the same point support into a compact support; excision extends a supported section by zero. The resulting square commutes already on the complexes of supported sections. This verifies the transition maps, not just the dimensions of the groups.

### G.2. The orientation determines the dualizing complex

Suppose that the local relative groups in (3.3) are \(\Lambda\) in degree \(m\) and zero otherwise, with \(m=2d\) in the variety case. We make the compatibility of its orientation generators explicit. A local orientation chooses generators \(u_y\in H_y^m(X;\Lambda)\). Around each point choose a cone neighborhood \(U\) on which their images under
\(H_y^m(U)\to H_c^m(U)\)
are one common class \(u_U\), for all \(y\in U\). These are support-inclusion maps, with the source identified by excision. The common class generates \(H_c^m(U)\), because at the center (G.1) is an isomorphism. This is the precise local compatibility required of the generators in (3.3). On overlapping neighborhoods it also gives compatibility under extension by zero: choose a still smaller neighborhood of a point in the overlap and use that point's support class in both maps. The complex orientation supplies these generators on the regular part; G.3 verifies their extension for the singular quotient example.

Use the structural dualizing complex \(\omega_X\) constructed in [Lesson 1, F.1–F.5](constructible-complexes-on-algebraic-varieties.md#appendix-f-the-classical-compact-support-right-adjoint). Its finite c-soft resolution and explicit injective adjoint give, naturally for open subsets,

\[
R\Gamma(U,\omega_X)
\simeq R\operatorname{Hom}_\Lambda
\bigl(R\Gamma_c(U,\Lambda),\Lambda\bigr).
\tag{G.2}
\]

Restriction on the left is the dual of extension by zero on the right. Over a field, splitting cycles and boundaries in a complex proves
\(H^q\operatorname{Hom}(A^\bullet,\Lambda)=\operatorname{Hom}(H^{-q}(A^\bullet),\Lambda)\): split each term into a boundary, a representative of its cohomology, and a complement mapping isomorphically to the next boundary. The identity pairs contract after dualization as well. Thus (G.1) and (G.2) show on a centered cone basis that the only nonzero stalk cohomology of \(\omega_X\) is in degree \(-m\). Taking stalks is legitimate on the injective model: a stalk is the filtered colimit of sections, and that colimit is exact.

Put \(\mathcal O_X=\mathcal H^{-m}(\omega_X)\). Canonical truncation gives \(\omega_X\simeq\mathcal O_X[m]\). In particular,
\(H^{-m}R\Gamma(U,\omega_X)=\Gamma(U,\mathcal O_X)\).
The functional on \(H_c^m(U)\) that sends \(u_U\) to one therefore defines a section of \(\mathcal O_X\). Its germ at any \(y\in U\) is the corresponding nonzero functional on \(H_y^m(U)\). To see this with the correct map, take a small centered cone about \(y\) inside \(U\); (G.1), extension by zero, and the compatibility of the classes \(u_y\) identify the restriction of the functional with evaluation on that generator. Hence this section is a basis at every stalk, and \(\Lambda_U\to\mathcal O_X|_U\) is an isomorphism.

The same support calculation makes these local bases agree on overlaps. The chosen orientation consequently gives

\[
\mathcal O_X\simeq\Lambda_X,
\qquad \omega_X\simeq\Lambda_X[m].
\tag{G.3}
\]

More generally, local orientation choices give the orientation line \(\mathcal O_X\), with transition scalars dual to the transition scalars of the compact cohomology generators. Equation (G.3) uses the globally compatible orientation specified in (3.3). Its shift is \(m\), because the unique cohomology sheaf of the dual complex lies in degree \(-m\).

For \(m=2d\), let \(P=\Lambda_X[d]\). Internal Hom out of the constant rank-one sheaf is the identity functor, so (G.3) gives \(D_XP=\omega_X[-d]=P\). For a smooth complex \(s\)-dimensional stratum \(a:S\hookrightarrow X\), factor its locally closed inclusion into a closed inclusion in an open set. Open restriction of the dualizing model is Lesson 1, F.5; the closed tensor-Hom adjunction in F.6 gives \(a^!D_XP=D_Sa^*P\). Smooth orientation on \(S\), also proved in F.5, yields
\(a^!P=\Lambda_S[2s-d]\), the actual identification in (3.4). The degrees \(-d\) and \(d-2s\) then give the perverse and strict boundary bounds stated in Section 3. This derives (3.5) from the local cohomology and its orientation without using a classical calculation as an étale duality assertion.

### G.3. Compatibility of the quotient orientation

Let \(X=\mathbf C^2/\{\pm1\}\), let \(o\) be its vertex, and assume that \(2\) is invertible in \(\Lambda\). The quotient map \(\pi:\mathbf C^2\to X\) is proper: the Euclidean norm descends to the quotient, and the inverse image of a compact set is a closed bounded subset of \(\mathbf R^4\). Proper pullback therefore acts on compactly supported cohomology, by pulling a relative cochain with compact support back to the compact inverse image of that support. It also acts on point-support cohomology, whose support becomes the finite fiber, and commutes with inclusion of supports.

Radial coordinates identify \(X\) with the open cone on \(\mathbf{RP}^3\), and identify \(\pi\) with the cone on the covering \(S^3\to\mathbf{RP}^3\). Section 4's transfer and the orientation-preserving antipodal action show that pullback is an isomorphism on the top link cohomology over \(\Lambda\). The relative cone sequence and the compact-support calculation in G.1 therefore show that
\(\pi^*:H_c^4(X;\Lambda)\to H_c^4(\mathbf C^2;\Lambda)\)
is an isomorphism. Both groups are one-dimensional, and the other compact-support groups vanish. The argument uses the natural cone connecting maps, so this is the proper pullback just described.

Let \(b\) be the standard complex-oriented generator of \(H_c^4(\mathbf C^2;\Lambda)\). For \(x\ne o\), the quotient is locally biholomorphic at each of the two points of \(\pi^{-1}(x)\). The positive point-support generator at \(x\) pulls back to the positive generator at each of those points. Their images in \(H_c^4(\mathbf C^2)\) are both \(b\), by the ball orientation and support-excision calculation of Lesson 1, C.4–C.5. Consequently the image of every such point generator in \(H_c^4(X)\) is the same class
\(u=(\pi^*)^{-1}(2b)\). This class is nonzero since \(2\) is invertible.

At \(o\), the support map \(H_o^4(X)\to H_c^4(X)\) is an isomorphism by the centered cone calculation; choose its generator mapping to \(u\). For a smaller vertex cone, extension by zero to \(X\) is an isomorphism by the same radial argument. Thus all point-support generators in that neighborhood have the same compact-support image there. On smooth balls the corresponding compatibility is the ordinary complex orientation. This proves the compatibility required in G.2 across the vertex, not merely the rank-one local group assertion. Hence \(\omega_X=\Lambda_X[4]\) with that orientation, and the intersection complex and the groups in (5.4) follow.

### G.4. Integral cellular chains and cochains

We prove the finite-cell comparison needed for the integral obstruction. Let \(Y\) be a finite CW complex with skeleta \(Y^k\), and put \(Y^{-1}=\varnothing\). Its characteristic discs may identify boundary points; no embedding of each closed cell is assumed. For \(k\geq1\), take \(Y^{k-1}\) together with an outer collar in every attached \(k\)-disc. Radial motion to the boundary gives a deformation retraction of this open neighborhood to \(Y^{k-1}\). It descends through all attaching maps, since the boundary points remain fixed, and is continuous by the quotient topology of the finite attachment.

Replace \(Y^{k-1}\) by this neighborhood in the relative groups. Cover the complement by the open cell interiors, enlarged to overlap the collars. The relative small-chain homotopy and its integral cochain dual, proved in [Lesson 1, D.1](constructible-complexes-on-algebraic-varieties.md#appendix-d-integral-thom-classes-and-the-circle-bundle-sequence), split the relative calculation into one ball-with-outer-annulus pair for each cell. Radial retraction, the integral sphere calculation and the split free-chain argument in D.1–D.3 give
\(H_i(Y^k,Y^{k-1};\mathbf Z)=0\) for \(i\ne k\), and a free group on the oriented \(k\)-cells for \(i=k\). Relative cohomology is likewise zero outside degree \(k\); evaluation identifies its degree-\(k\) group with the dual of that free group. For \(k=0\), these assertions are the direct sum of the point calculations.

Set \(C_k=H_k(Y^k,Y^{k-1};\mathbf Z)\), with groups outside the cell range equal to zero, and define \(d_k\) as the pair connecting map into \(H_{k-1}(Y^{k-1})\), followed by its map to \(C_{k-1}\). Two consecutive boundaries compose to zero by the exact sequence of the middle pair. We now verify that this complex computes singular homology. The pair sequences inductively give \(H_i(Y^j)=0\) for \(i>j\). Therefore \(H_k(Y^k)\to C_k\) is injective and has image \(\ker d_k\): the further map \(H_{k-1}(Y^{k-1})\to C_{k-1}\) is also injective. Attaching the \((k+1)\)-cells quotients \(H_k(Y^k)\) by the image of their relative boundary. Under its injection into \(C_k\), that image is \(\operatorname{im}d_{k+1}\). Higher attachments do not change degree \(k\), because both adjacent relative groups vanish. Hence

\[
H_k(Y;\mathbf Z)=\ker d_k/\operatorname{im}d_{k+1}.
\tag{G.4}
\]

The cochain assertion also follows from the pair sequences, without dualizing a mere isomorphism of homology groups. Put \(C^k=H^k(Y^k,Y^{k-1};\mathbf Z)\), and let \(\delta_k:C^k\to C^{k+1}\) be restriction to \(H^k(Y^k)\) followed by the connecting map for \((Y^{k+1},Y^k)\). Induction gives \(H^i(Y^j)=0\) for \(i>j\). Thus \(C^k\to H^k(Y^k)\) is onto, with kernel \(\operatorname{im}\delta_{k-1}\); the equality of this kernel with that image uses the surjection \(C^{k-1}\to H^{k-1}(Y^{k-1})\). Next \(H^k(Y^{k+1})\) injects into \(H^k(Y^k)\) with image the kernel of its map to \(C^{k+1}\). All higher attachments preserve \(H^k\). These statements identify
\(H^k(Y;\mathbf Z)=\ker\delta_k/\operatorname{im}\delta_{k-1}\).

Under the relative-cell evaluation pairing, \(C^k=\operatorname{Hom}(C_k,\mathbf Z)\) and \(\delta_k=d_{k+1}^{\vee}\). Indeed, the cochain connecting map is represented by extending a cocycle and taking its differential, while the chain connecting map takes a representative's boundary. The defining identity \((d\varphi)(z)=\varphi(\partial z)\) identifies their evaluations with no additional sign. This proves the claimed cellular cochain comparison integrally, including its differential.

### G.5. The attaching degrees for real projective space

The subspaces \(\mathbf{RP}^0\subset\cdots\subset\mathbf{RP}^3\) give one cell in each dimension. For the \(k\)-cell, use the closed upper hemisphere of \(S^k\) as a characteristic disc. Its interior maps homeomorphically to the projective lines whose last coordinate is nonzero; normalize that coordinate to be positive. On the equator, its attaching map is the antipodal quotient
\(S^{k-1}\to\mathbf{RP}^{k-1}\). This constructs the cell structure and its topology from the compact quotient by the sign action.

For \(k\geq2\), to read the coefficient of the \((k-1)\)-cell in \(d_k\), take the boundary of the oriented characteristic disc and collapse \(\mathbf{RP}^{k-2}\). Naturality of the pair connecting map identifies this coefficient with the degree of
\(S^{k-1}\to\mathbf{RP}^{k-1}/\mathbf{RP}^{k-2}\), whose target is a sphere: the closed \((k-1)\)-disc has its entire boundary collapsed. The preimage of the open top cell has two hemispheres. Choose the cell orientation so that the first contributes \(+1\). The second parametrization differs by the antipodal map on \(S^{k-1}\). Its degree is \((-1)^k\), because it is the boundary of the linear map \(-1\) on \(\mathbf R^k\), and the integral determinant sign rule was proved in Lesson 1, D.1. Relative excision splits the two hemispheres' contributions, so their degrees add. For \(k=1\), the same assertion is the boundary of an interval with both endpoints attached to one point, giving zero. We obtain

\[
0\longrightarrow\mathbf Z
\xrightarrow{\ 0\ }\mathbf Z
\xrightarrow{\ 2\ }\mathbf Z
\xrightarrow{\ 0\ }\mathbf Z\longrightarrow0,
\tag{G.5}
\]

in chain degrees \(3,2,1,0\). By G.4 the cochain differentials in degrees \(0\to1\to2\to3\) are \(0,2,0\). Thus

\[
H^a(\mathbf{RP}^3;\mathbf Z)=
\begin{cases}
\mathbf Z,&a=0,3,\\
\mathbf Z/2,&a=2,\\
0,&\text{otherwise}.
\end{cases}
\tag{G.6}
\]

The ordinary cone contracts, and its puncture retracts onto the link. Its integral relative cohomology in degree \(a>1\) is therefore the reduced link cohomology in degree \(a-1\), by the pair sequence. In particular \(H^3(X,X\setminus\{o\};\mathbf Z)=\mathbf Z/2\), while the top local group in degree four is \(\mathbf Z\). This proves the integral obstruction asserted in Section 5. With coefficients in a field in which \(2\) is invertible, the middle differential in (G.5) is invertible and only degrees zero and three remain on the link, in agreement with the transfer calculation.


## Appendix H. A global filtered realization from an affine atlas

The chain comparison in Appendix F needs one locally finite triangulation of the whole filtered space. We construct its input from a finite affine atlas. This applies to every separated finite-type complex algebraic variety, including varieties without a global locally closed algebraic embedding in projective space. The Euclidean triangulation input is the [relative polyhedron theorem](course:subanalytic-triangulations-on-analytic-manifolds/subanalytic-triangulations-on-analytic-manifolds#how-a-compatible-triangulation-is-assembled). Its proof and lower subanalytic inputs belong to that earlier reading; H.5 supplies its generic-center and generic-direction arguments using analytic rank partitions. The atlas construction and the passage from the Euclidean theorem to the filtered chain complexes are proved here.

### H.1. A proper topological embedding

Choose a finite affine open cover \(X=\bigcup_{i=1}^k U_i\) and closed algebraic embeddings
\(\psi_i:U_i\hookrightarrow\mathbf C^{n_i}=\mathbf R^{N_i}\), with \(N_i=2n_i\). The empty variety needs the empty complex, so assume \(k\geq1\). Finite generation of each affine coordinate algebra gives the embeddings. The polynomial Noetherianity argument in [Lesson 1, W.4](constructible-complexes-on-algebraic-varieties.md#w-4-finite-generation-descending-induction-and-the-fixed-curve) gives finite equations and the Noetherianity of every chart.

The classical topology on \(X\) is Hausdorff. Indeed, separatedness makes the diagonal a closed algebraic subvariety of \(X\times X\). On every product of affine charts its defining polynomial equations have a closed common zero set in the classical topology. These product charts are open and cover the product, so the whole diagonal is closed. A product neighborhood of any pair outside the diagonal gives disjoint neighborhoods of the two points. Each chart is locally compact and has a countable basis, as a closed subset of a finite Euclidean space. The finite open cover transfers local compactness and second countability to \(X\).

Define a scalar function \(a_i\) and a vector-valued function \(b_i\) by

\[
\begin{aligned}
a_i(x)&=\frac{1}{1+\|\psi_i(x)\|^2},&
b_i(x)&=\frac{\psi_i(x)}{1+\|\psi_i(x)\|^2}
&& (x\in U_i),\\
a_i(x)&=0,&b_i(x)&=0&& (x\notin U_i).
\end{aligned}
\tag{H.1}
\]

Both extensions are continuous. For \(R\geq0\), the set
\(C_i(R)=\{x\in U_i:\|\psi_i(x)\|\leq R\}\) is compact: its image is a closed bounded subset of \(\mathbf R^{N_i}\), and \(\psi_i^{-1}\) is continuous. It is therefore closed in the Hausdorff space \(X\). At a point outside \(U_i\), the open set \(X\setminus C_i(R)\) is a neighborhood. On its intersection with \(U_i\), the bounds
\(a_i\leq(1+R^2)^{-1}\) and \(\|b_i\|\leq1/R\), for \(R>0\), tend to zero. Outside \(U_i\) both functions already vanish. This proves continuity at the boundary without assuming that a chart has compact closure in \(X\).

Put \(a=\sum_i a_i>0\), \(\tau=1/a\), and

\[
\begin{aligned}
F:X&\longrightarrow\mathbf R^M,\qquad M=1+\sum_i(1+N_i),\\
F(x)&=\bigl((a_i(x),b_i(x))_{i=1}^k,\tau(x)\bigr).
\end{aligned}
\tag{H.2}
\]

This map is injective. If two images agree, choose \(j\) with their common \(a_j>0\). Both points belong to \(U_j\), and their common quotient \(b_j/a_j\) is their affine coordinate \(\psi_j\). On the open part of the image where \(a_j>0\), the inverse is exactly \(\psi_j^{-1}(b_j/a_j)\). These open parts cover the image, proving that \(F\) is a homeomorphism onto its image.

The last coordinate makes \(F\) proper. If a compact set \(D\subset\mathbf R^M\) has last coordinate at most \(B\), choose \(B\geq1\). For every \(x\in F^{-1}D\), the inequality \(\tau(x)\leq B\) gives \(a(x)\geq1/B\). Some index then satisfies \(a_i(x)\geq1/(kB)\), and consequently

\[
F^{-1}D\ \subset\
\bigcup_{i=1}^k C_i\bigl(\sqrt{kB-1}\bigr).
\tag{H.3}
\]

The right side is compact. The left side is closed in \(X\), by continuity and the closedness of \(D\), and is thus compact. The image \(F(X)\) is closed as well. For a convergent sequence of image points, their last coordinates are bounded. By (H.3) all their preimages lie in one finite compact union. Its image is compact and hence closed in Euclidean space, so it contains the limit. Sequential closedness is closedness in \(\mathbf R^M\).

### H.2. Finite equations for the image and its marked subsets

We show directly that \(F(X)\), and the image of every algebraically constructible subset, is semialgebraic. Here semialgebraic means a finite Boolean combination of real polynomial equalities and inequalities. The argument uses finite rational formulas, without a projection or elimination theorem.

Fix the affine chart \(U_j\). For each \(i\), the overlap \(U_i\cap U_j\) is a Zariski open subset \(W_{ij}\) of \(U_j\). It is a finite union of principal opens. More generally every Zariski open subset of a Noetherian affine chart is quasi-compact: a cover with no finite subcover would give, by successively adding a member, an infinite strictly increasing chain of open subsets, contradicting the descending chain condition for closed subsets. The principal opens form a basis, so a finite such subcover exists.

On \(W_{ij}\), the coordinates of \(\psi_i\) are regular functions. By the definition of a regular function they are fractions of polynomial coordinate functions on a neighborhood of each point. Refine to principal opens inside these neighborhoods, and use quasi-compactness and the finite number of coordinates to obtain finitely many pieces on which the whole transition \(\psi_i\psi_j^{-1}\) is given by rational functions with nonzero denominators. The same argument describes any constructible subset of \(U_j\) by finite Boolean polynomial conditions. Complex polynomial equalities become real and imaginary equalities, and a nonvanishing condition becomes \(|h|^2>0\). A complex fraction has real rational coordinates after multiplication by the conjugate of its denominator.

Write a prospective ambient point as \(y=((\alpha_i,\beta_i)_i,t)\). On the patch \(\alpha_j>0\), set \(z=\beta_j/\alpha_j\). Require that \(z\) satisfy the real polynomial equations of \(\psi_j(U_j)\). For every \(i\), impose the following finite alternative:

- If \(z\notin\psi_j(W_{ij})\), require \(\alpha_i=0\) and \(\beta_i=0\).
- If \(z\) lies in a principal piece of \(\psi_j(W_{ij})\) with transition formula \(R_{ij}(z)\), require
  \(\alpha_i(1+\|R_{ij}(z)\|^2)=1\) and \(\beta_i=\alpha_iR_{ij}(z)\).

Finally impose \(t\sum_i\alpha_i=1\). The transitions agree on overlapping pieces, so the alternatives assign the same coordinates there. These conditions describe exactly \(F(U_j)\): the point \(x=\psi_j^{-1}(z)\) exists uniquely, every pair \((\alpha_i,\beta_i)\) is its pair in (H.1), and the final equation fixes \(t=\tau(x)\). Conversely every \(F(x)\), \(x\in U_j\), satisfies the conditions.

There are only finitely many rational expressions and pieces. Their denominators are required to be nonzero. Clearing equalities by these denominators, and inequalities by their squares, expresses all the conditions as finite Boolean polynomial conditions, including after substitution \(z=\beta_j/\alpha_j\). Thus \(F(U_j)\) is semialgebraic. A finite union over \(j\) gives \(F(X)\). For a constructible subset \(A\subset X\), add the condition \(z\in\psi_j(A\cap U_j)\) on this same patch. The identical argument proves that \(F(A)\) is semialgebraic. In particular a closed algebraic subset has an image which is both semialgebraic and closed: \(F\) is a homeomorphism onto the closed set \(F(X)\).

### H.3. A locally finite full filtered triangulation

Use the finite algebraic Whitney stratification of [Lesson 1, K.6](constructible-complexes-on-algebraic-varieties.md#k-6-finite-compatible-whitney-refinements), compatible with the chosen regular open and coefficient system. Let \(X_j\) be the union of strata of real dimension at most \(j\), with \(X_{-1}=\varnothing\). The frontier condition makes each \(X_j\) closed: the closure of each of its finitely many strata is a union of strata of no greater dimension. These are algebraic closed subsets. For a pure complex \(d\)-dimensional variety put \(n=2d\); then \(X_n=X\) and \(X_{n-1}=X_{n-2}\), since the strata have even real dimension.

Give \(\mathbf R^M\) its integer-cube triangulation. On each cube, order its coordinate fractions and take the simplices for all coordinate orders, including their faces. On a common cube face, fixing a coordinate at zero or one leaves exactly the orders on the other coordinates, so these triangulations agree. Every bounded set meets finitely many cubes, and each cube has finitely many simplices. This is a countable, finite-dimensional, locally finite linear complex \(Q\) with closed support \(|Q|=\mathbf R^M\).

Apply the relative polyhedron theorem to the finite family consisting of \(F(X)\), all \(F(X_j)\), all images of the original strata, and all \(F(U_i)\). H.2 gives semialgebraicity, hence local semianalyticity and subanalyticity. A finite family is locally finite in the ambient space, as the theorem requires. We obtain a locally finite subdivision \(Q'\) and a homeomorphism \(T:\mathbf R^M\to\mathbf R^M\) such that each open simplex image is either contained in or disjoint from every marked set. The theorem's exact input is Euclidean; no embedding of an arbitrary analytic manifold is needed here.

Let \(K\) consist of the simplices \(\sigma\) of \(Q'\) for which \(T(\sigma^\circ)\subset F(X)\). It is a subcomplex. Indeed, \(F(X)\) is closed, so continuity puts \(T(\sigma)\) in \(F(X)\); all faces therefore have the same membership. Every point of \(T^{-1}F(X)\) lies in a unique open simplex whose membership must be in \(F(X)\). Hence

\[
|K|=T^{-1}F(X),\qquad
h=F^{-1}T|_{|K|}:|K|\xrightarrow{\ \sim\ }X.
\tag{H.4}
\]

The same construction for \(F(X_j)\) gives subcomplexes \(K_j\subset K\) with \(h(|K_j|)=X_j\). Local finiteness and countability pass from \(Q'\) to its subcomplexes. The map \(h\) is a homeomorphism, and it and its inverse send compact sets to compact sets.

One can also check the dimension bounds without assuming a dimension theorem for arbitrary topological spaces. An open simplex \(\sigma^\circ\) is sent into one original stratum \(S\), and compatibility with the chart images puts it entirely in some \(U_i\). Its coordinate map
\(\psi_i h|_{\sigma^\circ}=\beta_i(T(-))/\alpha_i(T(-))\) is analytic and injective. Locally its image lies in the smooth real manifold \(S\cap U_i\). Choose a point of maximal differential rank; near it that rank is constant, since the relevant nonzero minor remains nonzero and maximality excludes a larger rank. The analytic constant-rank theorem used in the relative triangulation reading then gives fibres of dimension \(\dim\sigma-\operatorname{rank}d(\psi_i h)\). Injectivity forces this dimension to be zero. Thus \(\dim\sigma\leq\dim_{\mathbf R}S\), and in particular \(\dim K_j\leq j\).

Now barycentrically subdivide \(K\) and all \(K_j\) simultaneously. The initial-segment argument in F.1 makes every filtration subcomplex full, and local finiteness is preserved because each old simplex has finitely many faces. The underlying map (H.4) does not change. The filtration indices remain the original real dimensions of the algebraic strata: the new simplices do not become new singular strata. In particular \(K_{n-1}=K_{n-2}\) still holds. These are precisely the filtered-complex hypotheses of Appendix F.

### H.4. Transport of coefficients, chains and supports

Put \(L_K=h^*L\) on \(|K|\setminus|K_{n-2}|\). For an allowable singular simplex \(s:\Delta^q\to|K|\), composition with \(h\) gives a simplex in \(X\) with exactly the same filtered preimages:

\[
(h\circ s)^{-1}(X_{n-k})=s^{-1}(|K_{n-k}|).
\tag{H.5}
\]

The regular coefficient sections identify by pullback, and this identification commutes with face restriction. Consequently composition with \(h\) preserves the allowable model skeletons, the boundary formula, and the cancellations needed for an allowable boundary. Composition with \(h^{-1}\) gives its inverse. Finite chains stay finite. For locally finite chains, a compact subset of \(X\) pulls back to a compact subset of \(|K|\), so only finitely many simplex images meet it; the reverse implication follows using \(h\). We have actual chain isomorphisms for both supports, followed by the comparison of Appendix F:

\[
\begin{aligned}
I^pC_*^{\epsilon,\mathrm{sim}}(K;L_K)
&\xrightarrow{\ \iota_K\ }I^pC_*^\epsilon(|K|;L_K)
\xrightarrow{\ h_*\ }I^pC_*^\epsilon(X;L),\\
&\hspace{18mm}\epsilon\in\{c,\infty\}.
\end{aligned}
\tag{H.6}
\]

The first arrow is a quasi-isomorphism by F.2–F.5; the second is the chain isomorphism just proved. F.6 supplies the compatible homology identification for PL refinement. Thus each such global model gives the singular intersection homology of \(X\), with its original local system, filtration and support convention. Two independently chosen models can be compared through this singular group; that assertion does not require their transition homeomorphism to be PL. For middle perversity, combine (H.6) with E.5 to obtain (E.9) for the simplicial and PL conventions as well.

### H.5. Generic centers from analytic rank partitions

Here is a direct proof of the center and direction choices in the Euclidean relative triangulation construction. We use the [compatible analytic partition and restriction-rank theorem](course:subanalytic-triangulations-on-analytic-manifolds/subanalytic-triangulations-on-analytic-manifolds#compatible-locally-finite-analytic-partitions) and the [analytic constant-rank coordinates](course:sheaf-proof-readings/SH03-subanalytic-sets-and-limiting-tangent-directions#real-analytic-inverse-implicit-and-constant-rank-coordinates). Subanalyticity in this argument is the bounded local projection class of [analytic finiteness](course:analytic-finiteness-and-preparation/analytic-finiteness-for-preparation#local-subanalytic-sets-and-bounded-charts). Its finite-cell, Boolean and projection results are the inputs to the partition theorem. The argument below does not use a representation by proper images of analytic manifolds.

**Deficient-rank images.** Let \(f:M\to N\) be an analytic map of finite-dimensional Hausdorff second-countable real analytic manifolds, with \(\dim N=q>0\), and suppose \(\operatorname{rank}df<q\) everywhere. Then \(f(M)\) is a countable union of compact nowhere dense subsets of \(N\).

To prove this, use the partition theorem with the map \(f\). On each of its countably many analytic members \(S\), the restriction has constant rank \(r<q\): restriction of the differential cannot increase its rank. Constant-rank coordinates give, near every point of \(S\), source and target charts in which the image is contained in the coordinate slice \(\mathbf R^r\times\{0\}\subset\mathbf R^q\). Choose a small closed source-coordinate ball contained in such a chart and mapped into that target chart. Its image is compact, hence closed in \(N\), and has empty interior because it is contained in that slice. It is therefore nowhere dense. The interiors of the chosen source balls cover \(S\). Second countability gives a countable subcover: for every basis element contained in some covering set, choose one such set. These choices cover all points. Repeat for the countably many \(S\). Their compact-ball images cover \(f(M)\), proving the assertion. Neither \(f\) nor the partition inclusions need be proper.

**The line incidence.** Let \(A\subset\mathbf R^m\) be subanalytic of dimension less than \(m\). Call a line singular for \(A\) if it contains a nontrivial interval in \(A\). A compatible locally finite analytic partition reduces the problem to its countably many members contained in \(A\), each of dimension less than \(m\). Indeed, on a compact subinterval only finitely many members occur; their intersections with the line are subanalytic. The one-dimensional cell theorem says that these intersections are finite unions of points and intervals, so at least one member contains a nontrivial interval. Work on a small ambient open set \(U\) where such a member is the zero set of an analytic function \(g\). Analytic submanifold coordinates supply defining functions, and the sum of their squares supplies \(g\). Countably many such neighborhoods suffice.

Choose a chart of unit directions \(v\). For the directional derivative \(L=v\cdot\partial_x\), put \(g_j=L^jg\). The [real-analytic Noetherianity proof](course:subanalytic-triangulations-on-analytic-manifolds/subanalytic-triangulations-on-analytic-manifolds#real-analytic-noetherianity) makes the ascending chain of ideals generated by \(g_0,\ldots,g_j\) stationary at every parameter germ \((x,v)\). Hence, on a neighborhood of that germ, there are finitely many analytic coefficients with

\[
g_{r+1}(x,v)=\sum_{j=0}^{r}c_j(x,v)g_j(x,v).
\tag{H.7}
\]

The equations \(g_0=\cdots=g_r=0\) describe precisely the local incidence \(\mathcal I\) of line germs contained in \(g^{-1}(0)\). One implication follows by differentiation along a line interval. For the converse set \(u_j(t)=g_j(x+tv,v)\). Then \(u'_j=u_{j+1}\) for \(j<r\), and (H.7) supplies the final row of a homogeneous linear system \(u'=C(t)u\). On a smaller compact parameter box choose \(\epsilon>0\) so all segments stay in the relation's domain and \(\|C(t)\|\le B\). If \(u(0)=0\), integration gives

\[
\sup_{|t|\le\epsilon}\|u(t)\|
\le B\epsilon\sup_{|t|\le\epsilon}\|u(t)\|.
\tag{H.8}
\]

Take \(B\epsilon<1\), with no restriction from this inequality if \(B=0\). The supremum is finite and must vanish. Thus \(g(x+tv)=0\) on that interval. This argument is uniform on the smaller parameter box. In particular \(\mathcal I\) is locally analytic, defined there by a finite list of equations.

Apply the analytic partition theorem to \(\mathcal I\) inside \(U\times V\), where \(V\) is the direction chart. Its members contained in \(\mathcal I\) are countably many analytic manifolds \(W\); write their inclusion as \(w\mapsto(x(w),v(w))\). Define

\[
F_W:W\times\mathbf R\longrightarrow\mathbf R^m,
\qquad F_W(w,s)=x(w)+s\,v(w).
\tag{H.9}
\]

Near any \(w_0\), the uniform argument for (H.8) puts the image of \(O\times(-\epsilon,\epsilon)\), for some neighborhood \(O\) of \(w_0\), in the chosen submanifold of dimension less than \(m\). Thus \(dF_W\) has rank less than \(m\) there. In coordinates on \(W\), its columns are \(dx+s\,dv\) together with \(v\). Each \(m\)-rowed minor is a polynomial in \(s\). For fixed \(w\) it vanishes on an interval about zero, so all its coefficients vanish and it is zero for every real \(s\). If the source has fewer than \(m\) coordinates, the rank bound is automatic. Hence \(dF_W\) is deficient everywhere. The preceding image argument shows that \(F_W(W\times\mathbf R)\) is meagre, meaning a countable union of nowhere dense sets. Taking all incidence charts and all \(W\) proves that the union of all points on singular lines for \(A\) is meagre.

**Parallel directions.** For \(m\ge2\), the map \(d_W:W\to\mathbf{RP}^{m-1}\), \(w\mapsto[v(w)]\), also has deficient rank everywhere. Otherwise analytic submersion coordinates give a local analytic section over a direction chart. Choose the corresponding analytic unit representative \(v=v(z)\), \(z\in\mathbf R^{m-1}\), and let the section supply \(x=x(z)\). The map \((z,s)\mapsto x(z)+sv(z)\) factors through (H.9), so its differential has rank less than \(m\). Its determinant, however, is a polynomial in \(s\) with leading coefficient

\[
\det\bigl(\partial_1v,\ldots,\partial_{m-1}v,v\bigr)\ne0.
\tag{H.10}
\]

The first \(m-1\) vectors form a basis of the tangent plane of the unit sphere, and the last is its nonzero normal. This is a contradiction. Apply the deficient-rank image argument to \(d_W\) and take the countable union over incidence charts. Thus singular parallel directions are meagre in projective direction space. When \(m=1\), a zero-dimensional subanalytic set contains no interval, so there are no singular directions or lines to avoid.

**Choosing outside the exceptional sets.** The required category fact has an elementary coordinate proof. If \(C_1,C_2,\ldots\) are closed nowhere dense subsets of a Euclidean open set and \(O\) is a nonempty open subset, choose a closed ball \(B_0\subset O\) of positive radius. Inductively choose a closed ball \(B_j\) of positive radius at most \(2^{-j}\) inside \(\operatorname{int}B_{j-1}\setminus C_j\). Such a ball exists because a closed nowhere dense set contains no nonempty open set. Compactness of \(B_0\) gives a point in all the nested balls. It lies in \(O\) and avoids every \(C_j\). The same proof in a coordinate chart works in projective direction space. A nowhere dense set can first be replaced by its nowhere dense closure.

Apply this to the singular-line or direction sets for any countable family of lower-dimensional subanalytic sets. The sets themselves are meagre as well: partition each into countably many lower-dimensional analytic members and apply the deficient-rank argument to their inclusions in \(\mathbf R^m\). Thus one may choose a center in any prescribed open simplex outside the obstacles and every singular line, and a parallel direction in any prescribed open direction chart outside every singular direction. For compact obstacles every resulting line intersection is finite: it is a compact subanalytic subset of a line, hence a finite union of points and intervals, and an interval has been excluded.

These are the two choices used by the local compact enlargement and radial-completion arguments in the relative polyhedron theorem. The finite analytic graph partitions, the doubled compact radial sets, and the ordered branches of that theorem then apply unchanged. This proves its generic-center and generic-direction inputs from analytic rank partitions, real-analytic Noetherianity and constant-rank coordinates. The finite-cell, Boolean/projection, bounded-chart and frontier results remain the lower analytic inputs.

### H.6. Dimension from finite grids

The dimension argument in [analytic finiteness](course:analytic-finiteness-and-preparation/analytic-finiteness-for-preparation#why-cell-dimension-is-intrinsic) needs the following covering fact. We prove it by counting separated points, using the nested-ball argument in H.5 for the passage to countably many images.

**Covering lemma.** Let \(d\ge1\). For each positive integer \(i\), let \(V_i\subset\mathbf R^{k_i}\) be open, with \(0\le k_i<d\), and let \(f_i:V_i\to\mathbf R^d\) be continuously differentiable. No nonempty open subset of \(\mathbf R^d\) is contained in \(\bigcup_i f_i(V_i)\).

First fix a closed cube \(Q\) of side \(\ell>0\) contained in one \(V_i\), with \(k=k_i>0\). The continuous derivative is bounded on \(Q\); choose a bound \(L>0\) for its operator norm. Integration along the segment from \(x\) to \(y\), component by component, gives

\[
\|f_i(x)-f_i(y)\|\le L\|x-y\|,\qquad x,y\in Q.
\tag{H.11}
\]

The scalar fundamental theorem used here is proved in [Lemma 0.1, parts 1–2](course:foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences#OA-FND-CT-07). Divide each edge of \(Q\) into \(N\) equal parts. There are \(N^k\) smaller closed cubes, and each image has diameter at most \(D/N\), where \(D=L\sqrt{k}\,\ell>0\).

Suppose \(f_i(Q)\) contained an open cube of side \(a>0\) in \(\mathbf R^d\), with lower corner \(b\). Inside it take the grid whose coordinate values are \(b_j+2Dr/N\), for integers \(1\le r\le q_N\), where

\[
q_N=\left\lfloor\frac{aN}{4D}\right\rfloor,
\qquad q_N^d\le N^k.
\tag{H.12}
\]

For sufficiently large \(N\), the grid is nonempty and lies strictly inside the cube: every displacement is positive and at most \(a/2\). Distinct grid points have distance at least \(2D/N\). Thus each of the \(N^k\) small-cube images contains at most one grid point, which explains the inequality in (H.12). But \(q_N\ge aN/(8D)\) once \(aN/(4D)\ge2\). The inequality would imply \((a/(8D))^dN^{d-k}\le1\) for arbitrarily large \(N\), impossible because \(d>k\). Hence \(f_i(Q)\) has empty interior. It is compact, therefore closed and nowhere dense. When \(k_i=0\), a nonempty \(V_i\) is a point and its image has the same conclusion.

Every open \(V_i\) of positive dimension is covered by countably many closed cubes contained in it: choose rational endpoints around each point inside a sufficiently small open ball. Consequently \(\bigcup_i f_i(V_i)\) is a countable union of compact nowhere dense sets. The nested closed balls of H.5 give a point outside this union in every prescribed nonempty open set. This proves the covering lemma.

**Application to cell dimension.** Let a cell \(C\) have dimension \(d\), and refine it into finitely many cells \(D_j\). The inclusion of tangent spaces gives \(\dim D_j\le d\). The projection \(\pi\) forgetting the graph coordinates of \(C\) identifies \(C\) with a nonempty open subset of \(\mathbf R^d\). Each \(D_j\) has an analytic parametrization \(\sigma_j\) by its free coordinates. If all \(\dim D_j<d\), the maps \(\pi\sigma_j\) contradict the covering lemma. Thus at least one refined cell has dimension \(d\). For \(d=0\), the cell is a point and the conclusion is immediate. Common finite refinements now show that

\[
\dim A=\max_{C\subset A}\dim C
\tag{H.13}
\]

is independent of the compatible cell decomposition. The maximum for the empty set is taken to be \(-1\). This supplies the covering input to the earlier proofs of the image inequality, fibre dimension and strict frontier decrease. Their selection step uses the explicit [compact-fibre proof of definable choice](course:analytic-finiteness-and-preparation/curve-selection-and-lojasiewicz#definable-choice); it requires only the finite cell theorem and Boolean/projection calculus, not the frontier theorem. The resulting dimension statements are those of Valette, §2.3.

### H.7. Arithmetic beneath the analytic arguments

The real and complex scalars in H.5–H.6 can be obtained from natural numbers. We take as axioms a natural-number system with zero, an injective successor \(S\), zero outside the image of \(S\), induction and recursion; we also use sets, functions and equivalence classes. The following construction supplies the ordered rational field that starts Constructing the real numbers.

**Natural-number arithmetic.** Define addition and multiplication by recursion:

\[
a+0=a,\qquad a+Sb=S(a+b),\qquad
a0=0,\qquad a(Sb)=ab+a.
\tag{H.14}
\]

Induction on \(b\) gives \(0+b=b\) and \((Sa)+b=S(a+b)\). Induction on the last variable then gives commutativity and associativity of addition: the successor step for commutativity reads \(a+Sb=S(a+b)=S(b+a)=(Sb)+a\); for associativity, both sides of \((a+b)+Sc=a+(b+Sc)\) are the successor of the corresponding expression with \(c\). The zero cases follow from (H.14). Cancellation in \(a+c=b+c\) follows by induction on \(c\), using injectivity of \(S\) at the successor step. An equation \(a+b=0\) forces \(a=b=0\): a nonzero natural number is a successor, by induction, and a sum with a successor is a successor.

Put \(a\le b\) when \(b=a+c\) for some natural number \(c\). This difference is unique by cancellation. The relation is reflexive and transitive by addition, and antisymmetric because \(a+c+d=a\) forces \(c=d=0\). It is total: zero is at most every number; when both numbers are successors, comparing \(Sa,Sb\) reduces to comparing \(a,b\). Formally, induction on \(a\), with all \(b\) in the induction assertion, proves this reduction covers every pair. The two strict alternatives are mutually exclusive by antisymmetry. Thus \(a<b\) means \(b=a+c\) with \(c\ne0\). Adding a fixed number preserves and reflects these comparisons by cancellation. A nonempty subset of \(\mathbf N\) has a least member: induction on \(n\) shows that any subset meeting \(\{0,\ldots,n\}\) has a least member, and one may take \(n\) to be any of its members. The induction step retains the earlier least member if one exists; otherwise the new point \(n+1\) is the least member.

For multiplication, induction on \(b\) first gives \(0b=0\) and \((Sa)b=ab+b\). In the latter successor step, \((Sa)(Sb)=ab+b+Sa=a(Sb)+Sb\), using the addition laws already proved. Induction on \(b\) now gives \(ab=ba\), since \(a(Sb)=ab+a=ba+a=(Sb)a\). Induction on \(c\) gives \(a(b+c)=ab+ac\): its successor step adds \(a\) on both sides. Commutativity gives the other distributive law. Finally, induction on \(c\) proves \((ab)c=a(bc)\), because its successor step is
\((ab)c+ab=a(bc)+ab=a(bc+b)\).
Writing \(1=S0\), (H.14) gives \(a1=a\), hence \(1a=a\). A product of two nonzero numbers is nonzero: write the second as \(Sb\); then \(a(Sb)=ab+a\), whose last summand is nonzero. These arguments establish a commutative cancellative additive monoid and a commutative semiring on \(\mathbf N\).

**Signed differences.** On \(\mathbf N^2\) set \((a,b)\sim(c,d)\) if \(a+d=c+b\). Reflexivity and symmetry follow from equality. For transitivity, add \(a+d=c+b\) and \(c+f=e+d\), then cancel \(c+d\) to obtain \(a+f=e+b\). Denote the equivalence class by \([a,b]\), and define

\[
\begin{aligned}
{[a,b]}+[c,d]&=[a+c,b+d],& -[a,b]&=[b,a],\\
[a,b][c,d]&=[ac+bd,ad+bc].
\end{aligned}
\tag{H.15}
\]

These definitions are independent of the representatives. If \(a+b'=a'+b\), addition respects that equality after adding \(c+d\), and negation respects its reversed form. For multiplication by \([c,d]\), the required equality is
\((ac+bd)+(a'd+b'c)=(a'c+b'd)+(ad+bc)\).
Its two sides are \(c(a+b')+d(b+a')\) and \(c(a'+b)+d(b'+a)\), which agree. Commutativity of the displayed multiplication handles a change of the second representative as well.

Addition is associative and commutative coordinatewise, with zero \([0,0]\), and \([a,b]+[b,a]=[a+b,a+b]=0\). Multiplication is commutative with identity \([1,0]\). For three representatives \((a,b),(c,d),(e,f)\), both associations of multiplication give the positive coordinate \(ace+adf+bcf+bde\) and the negative coordinate \(acf+ade+bce+bdf\). Distributivity follows by expanding the coordinates: those of \([a,b]([c,d]+[e,f])\) are \(ac+ae+bd+bf\) and \(ad+af+bc+be\), exactly the coordinates of the sum of the two products. Consequently these classes form a commutative ring \(\mathbf Z\). The map \(n\mapsto[n,0]\) is injective and preserves zero, one, sums and products by (H.15).

Every integer class is exactly one of zero, \([n,0]\), or \(-[n,0]\) for a unique \(n>0\): compare \(a\) and \(b\), subtract the smaller using the unique natural-number difference, and apply the defining equivalence. Positive integers are the classes \([n,0]\) with \(n>0\). Their sums and products are positive, and no class is both positive and negative. Define \(x<y\) by positivity of \(y-x\). The three alternatives just proved give trichotomy; closure under addition gives transitivity, and subtraction shows translation invariance. Multiplication by a positive integer preserves strict inequalities, since the product of two positive integers is positive. This order restricts to the order on \(\mathbf N\). Every nonzero integer has a sign and a positive natural-number magnitude, so a product of nonzero integers is nonzero. In particular multiplication by a nonzero integer is cancellative: \(ux=uy\) implies \(u(x-y)=0\), hence \(x=y\).

**Fractions with positive denominators.** Take pairs \((a,b)\), with \(a\in\mathbf Z\) and \(b\in\mathbf N\), \(b>0\), and identify \((a,b)\) with \((c,d)\) when \(ad=cb\). Reflexivity and symmetry are immediate. If \(ad=cb\) and \(cf=ed\), multiplication gives \(adf=c bf=edb\); cancellation of \(d\ne0\) gives \(af=eb\). Thus these pairs have a quotient set \(\mathbf Q\), whose classes we write \(a/b\). Define

\[
\frac ab+\frac cd=\frac{ad+cb}{bd},\qquad
\frac ab\frac cd=\frac{ac}{bd},\qquad
-\frac ab=\frac{-a}{b}.
\tag{H.16}
\]

If \(ab'=a'b\), then \((ad+cb)b'=(a'd+cb')b\) and \(acb'=a'cb\); multiplying these equalities by \(d\) verifies the equivalences for the displayed sum and product. Negation preserves the defining equality as well. Commutativity handles changes of the other representative. Fractions can be scaled by any positive integer \(u\), because \((au)b=a(bu)\). One can therefore put any finite collection over the product of its denominators.

For three fractions \(a/b,c/d,e/f\), both associations of addition have numerator \(adf+cbf+edb\) over \(bdf\), and both associations of multiplication have numerator \(ace\) over \(bdf\). Commutativity follows from the formulas. Distributivity has numerator \(acf+aed\) over \(bdf\) on both sides, after scaling the two products to that denominator. Zero is \(0/1\), one is \(1/1\), and the displayed negative is an additive inverse. A fraction vanishes exactly when its numerator vanishes. For \(a>0\), the inverse of \(a/b\) is \(b/a\); for \(a<0\), it is \((-b)/(-a)\). Both denominators are positive natural numbers under the identification of positive integers, and the products are one by (H.16). Hence \(\mathbf Q\) is a field.

A fraction is positive when its numerator is positive. This is independent of its representative: \(ab'=a'b\), with \(b,b'>0\), forces \(a\) and \(a'\) to have the same sign. The three signs, positive sums, and positive products follow from the integer statements and (H.16). As for \(\mathbf Z\), defining \(x<y\) by positivity of \(y-x\) gives a total, translation-invariant order preserved by multiplication by positive elements. In particular

\[
\frac ab<\frac cd\quad\Longleftrightarrow\quad ad<cb
\qquad(b,d>0).
\tag{H.17}
\]

The embedding \(a\mapsto a/1\) preserves the ring operations and the order and is injective. The rational field is Archimedean: for \(a/b\), its absolute value is at most the natural-number magnitude \(|a|\), since \(b\ge1\), so \(|a|+1\) is a strict integer bound. If \(r=a/b>0\), then \(a\ge1\), and \(1/(b+1)<1/b\le r\). This supplies arbitrarily small positive rational scales. Finally, listing \(\pm a/b\) by increasing \(a+b\), with \(a\ge0,b>0\), gives a sequence containing every rational: each level has finitely many pairs, and every pair occurs at its finite level.

**Real and complex arithmetic.** With this ordered rational field as input, the earlier real-number construction proves the field and order laws for rational Cauchy sequences modulo null sequences, and its nested-interval argument proves the least-upper-bound property. The elementary closed-interval analysis then proves completeness, compactness, the differentiation rules and the fundamental theorem of calculus. These proofs use induction and the rational arithmetic supplied above.

Set \(\mathbf C=\mathbf R^2\), add coordinatewise, and put \((x,y)(u,v)=(xu-yv,xv+yu)\). To verify associativity, represent \((x,y)\) by the real matrix with rows \((x,-y)\), \((y,x)\). Matrix multiplication is associative because both orders of multiplication have entries \(\sum_{j,k}a_{ij}b_{jk}c_{k\ell}\); the displayed matrices are closed under multiplication with exactly the stated formula. Commutativity and distributivity follow directly from that formula, and \((1,0)\) is the identity. A nonzero pair has inverse \((x,-y)/(x^2+y^2)\), since the denominator is positive. Conjugation \((x,y)\mapsto(x,-y)\) preserves sums and products. Thus the usual notation \(x+iy\), with \(i^2=-1\), defines a field containing \(\mathbf R\).

The positive square root, proved by the intermediate-value argument in the closed-interval reading, defines the Euclidean norm. Its inequalities also follow from the real field laws. For real vectors \(u,v\), expand \(\sum_j(v_j-tu_j)^2\ge0\) at \(t=(\sum_j u_jv_j)/(\sum_j u_j^2)\) when \(u\ne0\); this gives \(|\sum_j u_jv_j|\le\|u\|\|v\|\). The zero-vector case is immediate. Expanding \(\|u+v\|^2\) now gives the triangle inequality. In two coordinates, expansion of the multiplication formula gives \(|zw|^2=|z|^2|w|^2\), hence \(|zw|=|z||w|\).

For the complex exponential and circle, the remaining finite binomial identity follows by induction as well. Define \(0!=1\), \((n+1)!=(n+1)n!\), and \(c_{n,k}=n!/(k!(n-k)!)\) for \(0\le k\le n\), with zero outside this range. For interior indices, putting the two terms over a common denominator gives \(c_{n,k}+c_{n,k-1}=c_{n+1,k}\), because \((n+1-k)+k=n+1\); the endpoint coefficients equal one. Multiplying \(\sum_k c_{n,k}z^kw^{n-k}\) by \(z+w\) and grouping its finite sum proves \((z+w)^n=\sum_k c_{n,k}z^kw^{n-k}\), starting with \(n=0\). The earlier circle proof can therefore apply its convergent-series estimates and this finite identity to obtain the exponential law and its exact period. Together with the scalar Cauchy and polydisc arguments linked in H.5–H.6, these constructions provide the scalar arithmetic used by the analytic preparations.

## Proof dependencies

The construction and classification use the actual recollement, heart adjunctions and smooth local-subsystem proofs in Lessons 2–3. Their exact classical and étale constructibility, duality and coefficient foundations must hold at the scope used here. Lesson 1 supplies the classical cone comparison, finite-branch normalization and Thom–Gysin constructions cited above; Appendix A uses its divisor, coherent-cohomology and plane-curve arguments to treat arbitrary elliptic-curve embeddings. Appendix B supplies the allowable-chain complex, subdivision and excision, cone formulas and chain-sheaf normalization. Appendix C proves the product-neighborhood calculations, local constancy, global chain-section identifications and homotopical fineness. Appendix D uses Lesson 1, F.1–F.2 and BF.1, together with the explicit K-injective construction linked there, to prove the derived global and compact-support comparisons without a lower bound on the chain complex. Appendix E uses Lesson 1, A.1–A.3, C.1–C.5 and F.1–F.2, to prove compact-link finiteness and bounded finite-rank constructibility, and computes the actual attaching map by cutting cone representatives into radial annuli. It identifies the singular allowable-chain sheaf with the successive-truncation complex. For the algebraic Whitney models, E.1a uses the actual local biduality and compact-cohomology proofs of Lesson 1, G.1 and J.1–J.3; the link and coefficient reductions use I.6 and K.6. Appendix F proves the simplicial and PL comparisons with both support conventions and explicit refinement homotopies. Appendix H constructs a proper semialgebraic embedding from a finite affine atlas, applies the earlier relative polyhedron theorem with the filtration and chart images as marks, and transports the coefficients and both chain supports. For the Euclidean triangulation input, H.5 proves the generic-center and generic-direction choices through analytic rank partitions, finite jet equations, constant-rank coordinates and nested compact balls. H.6 gives the covering and intrinsic-dimension arguments by finite grids and nested balls. H.7 constructs the ordered rational field from the natural-number axioms, verifies complex arithmetic and its finite binomial identity, and connects the earlier real-number, closed-interval and complex-circle proofs to these arithmetic inputs. The finite analytic cell and set calculus, analytic Noetherianity, frontier, radial completion and graph-gluing proofs remain the specified lower inputs. The étale and normalized adic statements also require the earlier lessons' coefficient hypotheses. Appendix G proves the oriented cohomology-manifold identification with the dualizing complex, verifies the compatible orientation on the singular quotient, and proves the integral cellular chain and cochain comparison used for its torsion calculation. The compact-support, singular-cochain, local-duality, cone, normalization and Thom–Gysin comparisons use the earlier geometric foundations. These computations do not prove every lower input, including the analytic finiteness and triangulation results specified above.

## References

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://www.numdam.org/item/AST_1982__100__1_0/), freely readable edition, 1.4.22–1.4.26, 2.1.7, 2.1.11, 4.0(b) and 4.3.1–4.3.4, for intermediate extension, the stratum cutoff and the field-coefficient classification.
- M. Goresky and R. MacPherson, [*Intersection Homology II*](https://www.math.ias.edu/~goresky/math2710/IH2.pdf), free author-hosted text, §§3.1–3.5, printed pp. 101–104, for the attaching characterization and the real-dimensional chain normalization.
- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), free arXiv text, Examples 2.2.1 and 2.5.1, for cone calculations and the distinction between a perverse constant complex and an intersection complex. The computations above use the explicit link maps and boundary tests.
- A. Braverman, M. Finkelberg, D. Gaitsgory and I. Mirković, [*Intersection cohomology of Drinfeld's compactifications*](https://arxiv.org/abs/math/0012129), free arXiv text, conventions preceding §1, for the alternative half-Tate, weight-zero normalization.
- The Stacks Project, [very ampleness in degree at least \(2g+1\)](https://stacks.math.columbia.edu/tag/0H2V) and [separation by length-two subschemes](https://stacks.math.columbia.edu/tag/0E8T), for the general curve statements. Appendix A gives the genus-one section calculation and the finite-local-algebra proof of its closed immersion.
- G. Friedman, [*Singular chain intersection homology for traditional and super-perversities*](https://arxiv.org/abs/math/0407301v1), free arXiv version, §§2.3–2.6 and 3.1–3.2, for singular allowable chains, subdivision, excision, conical product calculations and the chain sheaf with its two support conventions.
- D. Chataur, M. Saralegi-Aranguren and D. Tanré, [*Simplicial intersection homology revisited*](https://arxiv.org/abs/2109.00261v3), free arXiv version 3, Sections 1–3 and 6, for full triangulations, residual complexes, the direct simplicial-to-singular comparison and PL refinement. Appendix F supplies the join, excision and support arguments for the local coefficients and both chain-support conventions used here.
- A. Mathew, [*Verdier duality*](https://math.uchicago.edu/~amathew/verd.pdf), free author notes, 29 July 2011, §§5.1–5.2, for the compact-support description of the orientation sheaf. Appendix G uses the explicit adjoint construction in Lesson 1 and proves its cone-neighborhood support comparison.
- A. Hatcher, [*Algebraic Topology*, Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf), free author-hosted text, Lemma 2.34, Theorem 2.35, the cellular boundary formula and Example 2.42, printed pp. 137–141 and 144. Appendix G proves the finite-cell chain and cochain comparisons and the projective-space attaching degrees used here.
- M. Shiota, [*Piecewise linearization of real analytic functions*](https://content.ems.press/assets/public/full-texts/serials/prims/20/4/3179/online/10.2977-prims-1195181110.pdf), freely readable journal text, Proposition 3.1, p. 733, and Proposition 3.1′, p. 738, for the Euclidean relative triangulation statement; Lemmas 3.2–3.3′, pp. 734–735, for generic centers and parallel directions. Appendix H gives the affine-atlas realization and the rank-partition proof of these choices, using the linked programme construction.
- G. Valette, [*On subanalytic geometry*](https://arxiv.org/abs/2507.23622v1), free arXiv version 1, §2.3, for dimension, generic fibre closure and the frontier inequality. H.6 proves the covering and refinement argument used with the linked analytic-finiteness reading.
- The Open Logic Project, Tim Button’s *Open Set Theory*, the freely accessible sections [From \(\mathbf N\) to \(\mathbf Z\)](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/integers.tex), [From \(\mathbf Z\) to \(\mathbf Q\)](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/rationals.tex), and [Checking the details](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/checking-details.tex), for the quotient constructions of the scalar fields. H.7 supplies the natural-number calculations, well-defined operations, order and field proofs used here.
