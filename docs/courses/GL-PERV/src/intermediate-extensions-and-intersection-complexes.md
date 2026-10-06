# Intermediate extensions and intersection complexes

*Reconstructed by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

An intersection complex can be calculated by answering a local question: after extending across a stratum, which stalk degrees must be removed? The answer is one degree stricter than perversity alone. We first derive that cutoff and its costalk counterpart. We then use them to recognize simple objects and to calculate four singular varieties. The examples distinguish a perverse constant sheaf from an intersection complex, and a singular variety from one that fails the cohomological smoothness test.

Use the constructible categories of Constructible complexes on algebraic varieties and the t-structure of [The perverse t-structure](the-perverse-t-structure.md). Coefficients are a field; the classical examples use a characteristic-zero field \(\Lambda\). In the étale setting retain the coefficient and finiteness hypotheses of the preceding lessons. Ordinary shifts satisfy \(\mathcal H^a(K[b])=\mathcal H^{a+b}(K)\). A smooth stratum of complex dimension \(s\) places its local systems in perverse degree zero by shifting them by \([s]\).

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

on sufficiently small neighborhoods, with compatible generators giving the complex orientation. In terms of the dualizing complex this says \(\omega_X=\Lambda_X[2d]\). We call this the rational-smoothness condition when \(\Lambda\) has characteristic zero. It is a cohomological condition and does not require the variety to be smooth.

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

The retained Goresky–MacPherson comparison has the following normalization. Give a complex algebraic variety a compatible triangulated stratification. A stratum of complex codimension \(r\) has real codimension \(2r\), and middle perversity is \(\overline m(2r)=r-1\). The theorem identifies its middle-perversity intersection-chain sheaf, normalized to restrict to \(L[2d]\), with \(\operatorname{IC}(X,L)[d]\). Therefore our unshifted cohomological complex is \(\operatorname{IC}(X,L)[-d]\). In particular its degree-\(r\) hypercohomology is (3.1). In the chain convention this corresponds to locally finite intersection homology in degree \(2d-r\); compact supports correspond to finite chains.

There is an elementary uniqueness step behind that theorem. If a candidate complex starts with \(L[2d]\), has no stalk groups above \(\overline m(2r)-2d\) on the next real-codimension-\(2r\) stratum, and its attaching map is an isomorphism through that degree, the natural map to the truncated direct image is an isomorphism on every stalk. It is therefore an isomorphism of complexes. Iterating determines the candidate uniquely. Shifting by \([-d]\) changes its cutoff to
\((r-1)-2d+d=-\dim S-1\), exactly (1.6).

What is still required is a proof that the sheaf of allowable chains has these properties, including its local cone calculation, constructibility, coefficient conventions and global chain comparison. The uniqueness step does not prove them. The theorem remains stated at its full assigned scope with that explicit proof obligation; none of the four computations below uses the unproved allowable-chain identification.

## 4. Two local calculations used by the examples

### The link determines the retained stalk degrees

Let an affine complex cone \(X\) of dimension \(d\) be smooth away from its vertex \(o\), and let \(M\) be its link. Positive radial scaling gives \(X\setminus\{o\}\simeq(0,\infty)\times M\). Its restriction to a small punctured conical neighborhood has the same homotopy type and the same restriction map on cohomology. The sheaf–singular comparison and radial attaching calculation are proved in Lesson 1, Appendix C. With \(j\) the punctured inclusion and \(i\) the vertex,

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

has no simultaneous zero among its coordinates. Substitution verifies the equation, and \(t/s=y/x\) is its inverse on the nonnodal affine part. The points \([1:1]\) and \([1:-1]\) map to the node \(o\), while \([0:1]\) maps to the smooth point at infinity. The normalization and actual branch arguments, including the finite-map prerequisites, are supplied in Lesson 1, Appendix L.

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

The deck map extends to the linear map \(-1\) on \(\mathbf R^4\), of determinant \(+1\). It preserves the ball orientation and hence the boundary orientation on \(S^3\). Formula (4.3) shows that the link has \(\Lambda\) in degrees \(0,3\) and zero in all other degrees. Relative cohomology of a cone and its puncture shifts reduced link cohomology up by one, so its local relative group is \(\Lambda\) only in degree \(4\). The orientation descends from the sphere and agrees with the complex orientation on the punctured quotient. Smooth points have the same oriented local groups. Thus (3.3) holds, and

\[
\operatorname{IC}(X,\Lambda)=\Lambda_X[2],\qquad
IH^0(X)=\Lambda,\qquad IH_c^4(X)=\Lambda,
\tag{5.4}
\]

with other global groups zero. The vertex stalk is in degree \(-2\) and costalk in degree \(2\).

The integral obstruction is visible without averaging. The usual cell filtration of \(\mathbf{RP}^3\) has one cell in each dimension \(0,1,2,3\). The two hemispheres in the attaching sphere contribute degrees whose sum is \(1+(-1)^k\) for the boundary of the \(k\)-cell: the antipodal identification contributes the second degree. Its integral cellular differentials are therefore \(d_3=0,d_2=2,d_1=0\). Dualizing this finite free complex gives \(H^2(\mathbf{RP}^3,\mathbf Z)=\mathbf Z/2\). Consequently the vertex relative group in degree \(3\) is \(\mathbf Z/2\), and the integral cohomology-manifold assertion fails. This identifies precisely the torsion which the characteristic-zero calculation removes.

### The elliptic cone: a perverse constant sheaf can still be too large

Let \(C\) be a smooth embedded projective elliptic curve, with embedding line bundle \(A\) of degree \(e>0\), and let \(X\) be its affine cone. Sending a nonzero vector on a projective line to its direction identifies the punctured cone with \((A^{-1})^\times\). The link is the unit circle bundle of \(A^{-1}\). Write \(\eta\) for its positive base degree-two generator. The Euler class is \(-e\eta\).

The required circle-bundle sequence is proved in Lesson 1, Appendix D: it is the pair sequence for the line bundle and its nonzero part, transported through the oriented Thom isomorphism. The Euler map is cup product with the zero-section pullback of the Thom class, and dualizing the line reverses its sign. Here it reads

\[
\cdots\to H^{q-2}(C)\xrightarrow{-e\eta\smile}H^q(C)
\to H^q(M)\to H^{q-1}(C)\xrightarrow{-e\eta\smile}H^{q+1}(C)\to\cdots.
\tag{5.5}
\]

For an elliptic curve the needed base groups are \(\Lambda,\Lambda^2,\Lambda\) in degrees \(0,1,2\). For a smooth plane cubic, their geometric and topological proof, and the degree calculation, are in Lesson 1, Appendix E. For an arbitrary elliptic curve and an arbitrary very ample embedding, the identification of its complex topology as an oriented genus-one surface and of the bundle Euler number with \(e\) still needs the corresponding general curve proof. We retain that full case as a stated prerequisite, rather than identifying every embedding with the plane-cubic case.

Under these base inputs, \(-e:H^0(C)\to H^2(C)\) is invertible. Exactness of (5.5) gives link ranks \(1,2,2,1\) in degrees \(0,1,2,3\): the degree-one map from \(H^1(C)\) is an isomorphism, as is the degree-two map to \(H^1(C)\); the degree-three map to \(H^2(C)\) is an isomorphism. Formula (4.1) keeps only the first two link degrees. Thus the vertex stalk has

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

**Solution.** With the genus-one and degree inputs specified above, the Euler map is the nonzero scalar \(-e\) from base degree zero to degree two. Exactness leaves link degree-one and degree-two groups both isomorphic to \(H^1(C)=\Lambda^2\), with endpoint groups \(\Lambda\) in degrees zero and three. Shifting by two places these four groups in degrees \(-2,-1,0,1\). Intermediate extension removes the last two. The stalk is therefore \(\Lambda\) in degree \(-2\) and \(\Lambda^2\) in degree \(-1\); the dual costalk is \(\Lambda^2\) in degree one and \(\Lambda\) in degree two. The global restriction map for a cone is the same radial cohomology isomorphism, so (4.2) leaves \(IH^0=\Lambda\) and \(IH^1=\Lambda^2\). Duality puts the compactly supported groups in degrees four and three, with ranks one and two. This calculation has the same explicit general-elliptic-curve prerequisite as the example; a citation does not supply it.

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

## Proof dependencies

The construction and classification use the actual recollement, heart adjunctions and smooth local-subsystem proofs in Lessons 2–3. Their exact classical and étale constructibility, duality and coefficient foundations must hold at the scope used here. Lesson 1 supplies the classical cone comparison, finite-branch normalization and Thom–Gysin constructions cited above; its separate étale and normalized adic obligations are not removed by these computations. The orientation-to-dualizing-complex statement for cohomology manifolds, the cell comparison for the finite quotient calculation, and the transitive prerequisites of the used earlier lessons require their complete proof audit. The arbitrary elliptic-curve topology and degree comparison, and the allowable-chain comparison in Section 3, remain specifically identified proof obligations. The full assigned statements are retained. A conditional input or a freely accessible reference does not count as a completed prerequisite proof.

## References

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://www.numdam.org/item/AST_1982__100__1_0/), freely readable edition, 1.4.22–1.4.26, 2.1.7, 2.1.11, 4.0(b) and 4.3.1–4.3.4, for intermediate extension, the stratum cutoff and the field-coefficient classification.
- M. Goresky and R. MacPherson, [*Intersection Homology II*](https://www.math.ias.edu/~goresky/math2710/IH2.pdf), free author-hosted text, §§3.1–3.5, printed pp. 101–104, for the attaching characterization and the real-dimensional chain normalization. The chain-sheaf hypotheses remain to be proved here.
- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), free arXiv text, Examples 2.2.1 and 2.5.1, for cone calculations and the distinction between a perverse constant complex and an intersection complex. The computations above use the explicit link maps and boundary tests.
- A. Braverman, M. Finkelberg, D. Gaitsgory and I. Mirković, [*Intersection cohomology of Drinfeld's compactifications*](https://arxiv.org/abs/math/0012129), free arXiv text, conventions preceding §1, for the alternative half-Tate, weight-zero normalization.
