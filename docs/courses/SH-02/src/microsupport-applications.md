# Directional constraints under algebraic and geometric constructions

This lesson develops applications of the local support tests, including operations for which a tempting commutation statement fails. The applications accompanying the microsupport theory go back to M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapters 3–5. Public domain (CC0).

## SH02-MSA-CONVENTIONS — Objects, limits, and dependencies

Unless a statement says otherwise, $k$ is a commutative unital ring of finite global dimension and manifolds are finite dimensional, Hausdorff, and countable at infinity. Complexes belong to $D^b(k_X)$; stalk modules need not be finite, and no constructibility is implicit. A sheaf means an object in degree zero. A limit of sheaves means the ordinary limit in the abelian category unless $R\varprojlim$ is written. For a subset $A$, $k_A$ denotes the constant sheaf on $A$ extended by zero through its locally closed embedding. Tensor products and exterior products of complexes are derived.

We use the [support tests](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-TEST), their [cone characterization](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-EQUIVALENCE), the [finite triangle rules](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-FORMAL), and the [functorial estimates](../../sheaf-proof-readings/SH02-microsupport-operations.html). Exact operation names below refer to the morphisms proved in those lessons. The [Fourier convention](../../sheaf-proof-readings/SH02-fourier-sato.html), [specialization](../../sheaf-proof-readings/SH02-specialization.html), [microlocalization](../../sheaf-proof-readings/SH02-microlocalization.html), [cohomological biduality](../../sheaf-proof-readings/SH02-cohomological-biduality.html), and [orientation formulas](../../sheaf-proof-readings/SH02-manifold-duality.html) are treated in their own lessons, with their own prerequisites; they are not proved here.

The realization proof additionally uses [contractible-parameter descent](../../sheaf-proof-readings/SH02-conic-descent.html#SH02-CON-CYLINDER), [enhanced closed exhaustion](../../sheaf-proof-readings/SH02-closed-exhaustion.html#SH02-EXH-COMPARISON), effective descent of ordinary sheaves along a covering map, and injective resolutions in module-sheaf categories. The moving-cap arguments use the [corrected noncharacteristic-deformation theorem](../../sheaf-proof-readings/SH02-noncharacteristic-deformation.html#SH02-NCD-THEOREM). The support-erasure applications use the [Thom, Euler, and Gysin constructions](../duality-applications.html#sh02-da-thom-the-supported-generator-of-a-vector-bundle) with their specified adjunction maps. These are limited imports, with no claim that the prerequisite course or its source chapters have been completed.

For a covector $(x,\xi)$, the antipode is $(x,-\xi)$, denoted by a superscript $a$. For a subset of a cotangent bundle, a bar always means closure in the entire indicated cotangent bundle. This is essential in the limit statements.

## SH02-MSA-COMPLEX-ORBITS — Two real vector fields describe complex scaling

Let $X=\mathbb C^n$. Regard a complex covector $\zeta$ as the real covector $2\operatorname{Re}\langle\zeta,dz\rangle$, and put

$$
\Lambda=\{(z,\zeta):\textstyle\sum_{j=1}^n z_j\zeta_j=0\}.
\tag{MSA28}
$$

A sheaf $A$ satisfies $\operatorname{SS}(A)\subset\Lambda$ exactly when its restriction to each $\mathbb C^*$-orbit is locally constant. No triviality of the monodromy on a punctured complex line is asserted.

**Proof.** The real radial and angular fields are $R(z)=z$ and $I(z)=iz$. Pairing the real covector with them gives respectively twice the real part and minus twice the imaginary part of $\sum z_j\zeta_j$. Thus MSA28 is exactly their common annihilator. Off the origin, the projection

$$
\pi:\mathbb C^n\setminus\{0\}\longrightarrow\mathbb P^{n-1}(\mathbb C)
$$

is locally a product with the fibre $\mathbb C^*$; its vertical tangent is spanned by $R,I$. In a sufficiently small fibre chart it is a projection with a contractible open ball as fibre. The submersion theorem and its local-descent converse, `SH02-MO-SUBMERSION`, say precisely that a sheaf has microsupport in this horizontal cotangent set if and only if it is locally pulled back from the transverse factor. Local pullback is equivalent here to local constancy on the connected pieces of the fibres. One direction is immediate by restriction. In the converse, continuation on a compact smaller fibre ball gives the pullback comparison: a local section at one fibre point extends along a finite cover of each compact path, and overlap uniqueness supplies compatibility; shrinking the transverse neighborhood makes these finitely many continuations into sections there. Contractibility removes path monodromy within the chart. This is the interval/ball descent in the stated submersion contract and does not require a finite stalk module.

These local assertions glue on the punctured space and allow arbitrary monodromy around the full $\mathbb C^*$ fibre. At the origin both vector fields vanish, so $\Lambda$ contains the whole cotangent fibre; the orbit is a point. Neither side of the claimed equivalence imposes an additional condition there. For $n=0$ the space is itself a point and the assertion is the same tautology. $\square$

The corresponding class of sheaves is an abelian category: kernels, cokernels, and extensions remain locally constant on the orbit charts. For a bounded complex, the same submersion descent identifies $\operatorname{SS}(F)\subset\Lambda$ with orbitwise local constancy of its cohomology sheaves. The natural realization functor from the bounded derived category of this abelian category consequently lands in the full subcategory $D^b_\Lambda(k_X)$. Whether realization is an equivalence requires an additional Ext comparison; it does not follow merely by identifying its cohomology sheaves. The following argument supplies that comparison without a finiteness restriction.

## SH02-MSA-ORBIT-REALIZATION — When the orbitwise heart recovers the derived category

Let $A_X$ be the abelian category in the preceding orbit criterion. The realization functor is an equivalence

$$
D^b(A_X)\xrightarrow{\sim}D^b_\Lambda(k_X).
\tag{MSA29}
$$

For $n=0$ this is the identity on $D^b(k)$. Assume $n\geq1$, put $U=X\setminus\{0\}$, and write $A_U$ for the sheaves on $U$ locally constant on the fibres of $\pi:U\to P=\mathbb P^{n-1}(\mathbb C)$. The orbit criterion identifies $A_X$ with sheaves whose restriction is in $A_U$, and identifies the target of MSA29 with bounded complexes whose cohomology sheaves are in $A_X$. We prove the required comparison of every Ext group before using those identifications to deduce the derived equivalence.

### SH02-MSA-ORBIT-PRODUCT — The local monodromy category

Let $B$ be an open manifold (the argument also works for the spaces covered by the cited cylinder theorem), put $W=B\times\mathbb C^*$, and let $A_W$ be its fibrewise locally constant sheaves. Set

\[
 R=k[t,t^{-1}].
\]

We first obtain an exact equivalence

\[
 A_W\simeq\operatorname{Mod}(R_B).
 \tag{R5}
\]

The right side consists of arbitrary sheaves of modules over the constant ring sheaf $R_B$, equivalently a sheaf $M$ of $k$-modules on $B$ with an invertible $k$-linear sheaf endomorphism $T$.

Let

\[
 q:B\times\mathbb R^2\longrightarrow B\times\mathbb C^*,
 \qquad (b,s,\theta)\longmapsto(b,e^{s+2\pi i\theta}),
 \qquad p:B\times\mathbb R^2\to B.
\]

If $F$ belongs to $A_W$, $q^{-1}F$ has locally constant restrictions to the $\mathbb R^2$ fibres. Applying the contractible-cylinder theorem twice identifies it canonically with $p^{-1}M$, with $M$ obtained by restriction to a fixed section. The deck generator $\theta\mapsto\theta+1$ is an automorphism of $p^{-1}M$. Full faithfulness of $p^{-1}$ identifies it with an automorphism $T$ of $M$. Conversely the deck action induced by $T$ on $p^{-1}M$ is effective descent data for the covering $q$, and yields a sheaf $F$ on $W$. These constructions are inverse on objects and morphisms, and are exact. No basis, finiteness, or semisimplicity of $M$ is used.

Choose the generator convention in (R5) so that $q_!p^{-1}M$ corresponds to the induced module sheaf $R_B\otimes_{k_B}M$. Replacing $t$ by $t^{-1}$ everywhere gives the other harmless deck convention.

The contractible comparison needed below is

\[
 N\xrightarrow{\sim} Rp_*p^{-1}N
 \tag{R6}
\]

for any sheaf $N$ on $B$. This is not inferred from ordinary fibre cohomology for a nonproper map. It follows from the already proved cylinder comparison. Equivalently, exhaust $\mathbb R^2$ by closed squares with interiors covering $\mathbb R^2$, use proper base change on every square to obtain the unit isomorphism there, and use the enhanced closed-exhaustion comparison. The resulting constant inverse system has no derived-limit obstruction. Naturality with respect to $N$ fixes the unit map in (R6).

### SH02-MSA-ORBIT-RESOLUTION — Two induced objects resolve arbitrary monodromy

For an $R_B$-module $M$ with monodromy $T$ there is a natural exact sequence in sheaves of $R_B$-modules

\[
 0\longrightarrow R_B\otimes_{k_B}M
 \xrightarrow{d}R_B\otimes_{k_B}M
 \xrightarrow{e}M\longrightarrow0,
 \tag{R7}
\]

where on local Laurent polynomials

\[
 d(r\otimes m)=rt\otimes m-r\otimes Tm,
 \qquad e(r\otimes m)=r(T)m.
\]

This is exact for arbitrary underlying modules. It can be checked on stalks. The map $e$ is surjective through $1\otimes m$. The relations imposed by $d$ identify $t\otimes m$ with $1\otimes Tm$; since $T$ is invertible, they reduce every finite Laurent sum to its image under $e$. They therefore give precisely the kernel of $e$. To see that $d$ is injective, write a finite Laurent sum with largest exponent $b$. The coefficient at exponent $b+1$ in its image under $d$ is the original coefficient at $b$. Vanishing forces it to be zero; downward induction kills the entire finite sum. No torsion or finite-generation argument is involved.

Under (R5), both induced terms in (R7) are

\[
 E(M)=q_!p^{-1}M.
\]

The covering functor $q_!$ is exact: locally its stalks are direct sums indexed by the discrete covering fibre. Thus the realization of (R7) is an exact sequence of ordinary sheaves on $W$ as well.

### SH02-MSA-ORBIT-LOCAL-EXT — Comparing extensions on a product chart

For a second object $G$ of $A_W$ corresponding to an $R_B$-module $N$, derived adjunction and (R6) give

\[
 R\operatorname{Hom}_{k_W}(q_!p^{-1}M,G)
 \simeq R\operatorname{Hom}_{k_{B\times\mathbb R^2}}
                 (p^{-1}M,q^{-1}G)
 \simeq R\operatorname{Hom}_{k_B}(M,N).
 \tag{R8}
\]

Here $q^{-1}G$ is $p^{-1}N$. The first adjunction is valid because $q_!$ is exact; the second uses the exact inverse image $p^{-1}$ and the actual derived unit (R6).

On the module-sheaf side, induction $R_B\otimes_{k_B}-$ is exact because $R$ is free as a $k$-module. It is left adjoint to the exact restriction-of-scalars functor. Consequently restriction of scalars preserves injectives, and

\[
 R\operatorname{Hom}_{R_B}(R_B\otimes_{k_B}M,N)
 \simeq R\operatorname{Hom}_{k_B}(M,N).
 \tag{R9}
\]

The two identifications respect the degree-zero Hom correspondence of (R5), its adjunction units, and the maps in (R7). They therefore identify the natural realization comparison for induced objects in every Ext degree.

Apply the two long exact Ext sequences obtained from (R7), or the corresponding two-column resolution spectral sequences. Since the comparison is an isomorphism for both induced terms in every degree, it is an isomorphism for $M$ itself. We have proved

\[
 \operatorname{Ext}^q_{A_W}(F,G)
 \xrightarrow{\sim}\operatorname{Ext}^q_{\operatorname{Sh}(k_W)}(F,G)
 \qquad(q\geq0)
 \tag{R10}
\]

for all $F,G$ in $A_W$. This is the place where the aspherical orbit $\mathbb C^*$ is used. It is a concrete Laurent-module calculation; no assertion about arbitrary higher-homotopy orbits is being substituted for it.

### SH02-MSA-ORBIT-GLUING — Keeping the transition functions of the bundle

The standard $n$ affine opens $P_a=\{z_a\ne0\}$ cover $P$. On $\pi^{-1}P_a$ the coordinate $z_a$ supplies a trivialization with $P_a\times\mathbb C^*$. Every nonempty finite intersection is contained in one $P_a$, so the bundle is trivial there too. These opens and all their intersections are saturated: each fibre is wholly inside or wholly outside.

The category $A_U$ is a Grothendieck abelian category. Here are the checks needed for the injective argument. Kernels, cokernels and colimits are computed in ordinary sheaves and remain fibrewise locally constant. This follows either by restricting to a fibre and using the representation description of local systems on $\mathbb C^*$, or locally from (R5). Filtered colimits are exact because they are exact in module sheaves. Each local category on $\pi^{-1}P_a$ has a set of generators by (R5). Extension by zero from a saturated open is exact and preserves $A_U$: its restriction to each fibre is either the given local system or zero. Extend the local generators by zero and take their union. They detect any nonzero morphism, since one of its restrictions to this cover is nonzero. Hence $A_U$ has a generator and enough injectives.

If $J$ is injective in $A_U$, its restriction to any saturated open is injective in that local orbit category. Indeed restriction is right adjoint to exact extension by zero. In particular, for $F$ in $A_U$ and every nonempty finite intersection $U_I$ of the finite trivializing cover, (R10) gives

\[
 \operatorname{Ext}^q_{\operatorname{Sh}(k_{U_I})}
      (F|_{U_I},J|_{U_I})=0\qquad(q>0).
 \tag{R11}
\]

Use the ordinary augmented finite Čech resolution of $F$ by the sheaves $(U_I\hookrightarrow U)_!(F|_{U_I})$. It is exact both in $\operatorname{Sh}(k_U)$ and in $A_U$. Its derived-Hom spectral sequence in ordinary sheaves has first page given by the Ext groups on the intersections in (R11). Only degree zero remains. That row is the complex obtained by applying $\operatorname{Hom}_{A_U}(-,J)$ to the same augmented resolution. It is exact in positive degrees because $J$ is injective in $A_U$. Therefore

\[
 \operatorname{Ext}^q_{\operatorname{Sh}(k_U)}(F,J)=0
 \qquad(q>0).
 \tag{R12}
\]

An injective resolution in $A_U$ is thus an acyclic resolution for the ordinary-sheaf Hom functor from any $F$ in $A_U$. It follows that

\[
 \operatorname{Ext}^q_{A_U}(F,G)
 \xrightarrow{\sim}\operatorname{Ext}^q_{\operatorname{Sh}(k_U)}(F,G)
 \qquad(q\geq0)
 \tag{R13}
\]

for all $F,G$ in $A_U$.

This argument retains the actual transition functions of the principal bundle. It does not replace $A_U$ globally by untwisted sheaves of $k[t,t^{-1}]$-modules on projective space.

### SH02-MSA-ORBIT-ORIGIN — Acyclicity at the closed orbit

Write $j:U\hookrightarrow X$ and $i:\{0\}\hookrightarrow X$. Let $J$ be injective in $A_U$. We claim

\[
 Rj_*J\simeq j_*J.
 \tag{R14}
\]

There is nothing to check away from the origin. At the origin, use the radial product

\[
 U\simeq S^{2n-1}\times\mathbb R,
 \qquad (v,s)\longmapsto e^s v.
\]

The sheaf $J$ is locally constant on radial fibres because it is locally constant on $\mathbb C^*$-orbits. The cylinder theorem identifies it with the pullback of its restriction $H$ to the unit sphere. It supplies natural quasi-isomorphisms

\[
 R\Gamma(U;J)\simeq R\Gamma(S^{2n-1};H)
 \simeq R\Gamma(U\cap B_\epsilon;J)
 \tag{R15}
\]

for every $\epsilon>0$, and the restriction maps between punctured balls are the corresponding isomorphisms. The last product has radial coordinate $s<\log\epsilon$, still a contractible interval diffeomorphic to $\mathbb R$. This verifies invariance under shrinking rather than assuming that a stalk commutes with an inverse limit.

The constant sheaf $k_U$ lies in $A_U$. Equation (R13), with source $k_U$ and target the injective $J$, gives

\[
 H^q(U;J)
 =\operatorname{Ext}^q_{\operatorname{Sh}(k_U)}(k_U,J)=0
 \qquad(q>0).
\]

Together with (R15), the stalk formula for $Rj_*$ proves (R14). In particular, the higher cohomology of the sphere has not been discarded: it vanishes for these specific injectives because the punctured-space Ext comparison has already been proved. It would be false to claim the same acyclicity for arbitrary orbitwise locally constant $J$.

### SH02-MSA-ORBIT-INJECTIVES — Injectives that compute ambient extensions

Take $F$ in $A_X$. Choose monomorphisms

\[
 j^{-1}F\hookrightarrow J\quad(J\text{ injective in }A_U),
 \qquad i^{-1}F\hookrightarrow I\quad(I\text{ injective as a }k\text{-module}).
\]

Adjunction gives a map

\[
 F\longrightarrow j_*J\oplus i_*I.
 \tag{R16}
\]

This map is a monomorphism. At every point of $U$ its first component is injective, and at the origin its second component is injective. Both target summands belong to $A_X$.

Both summands are injective in $A_X$. Indeed

\[
 \operatorname{Hom}_{A_X}(F,j_*J)
 =\operatorname{Hom}_{A_U}(j^{-1}F,J),
 \qquad
 \operatorname{Hom}_{A_X}(F,i_*I)
 =\operatorname{Hom}_{k}(i^{-1}F,I),
\]

and both inverse-image functors are exact. This proves that $A_X$ has enough injectives. Every injective of $A_X$ is a direct summand of one of the targets in (R16).

For $F$ in $A_X$, derived adjunction and (R14) identify

\[
 \operatorname{Ext}^q_{\operatorname{Sh}(k_X)}(F,j_*J)
 \simeq\operatorname{Ext}^q_{\operatorname{Sh}(k_U)}(j^{-1}F,J)=0
 \qquad(q>0),
 \tag{R17}
\]

where the last equality is (R12). The sheaf $i_*I$ is injective even in the full sheaf category: $i_*$ is right adjoint to the exact stalk inverse-image functor. Consequently its higher Ext groups also vanish. Finite sums and direct summands preserve this acyclicity. All $A_X$-injectives are therefore acyclic for the ordinary-sheaf Hom functor from every object of $A_X$.

Resolve the second argument within $A_X$. This proves the natural comparisons

\[
 \operatorname{Ext}^q_{A_X}(F,G)
 \xrightarrow{\sim}\operatorname{Ext}^q_{\operatorname{Sh}(k_X)}(F,G)
 \qquad(q\geq0)
 \tag{R18}
\]

for all $F,G$ in $A_X$. No global upper bound on injective resolution length is required. Injective resolutions may be bounded below; the objects whose realization is at issue remain bounded.

### SH02-MSA-ORBIT-DERIVED — Recovering every attaching morphism

The inclusion $A_X\hookrightarrow\operatorname{Sh}(k_X)$ is exact and full. By (R18) it preserves every Ext group between objects of the heart. Finite truncation triangles and the long exact Hom sequences then show, by induction on the cohomological lengths of two bounded complexes, that

\[
 D^b(A_X)\longrightarrow D^b(\operatorname{Sh}(k_X))
\]

is fully faithful.

Its essential image is exactly the bounded complexes whose cohomology sheaves lie in $A_X$. One direction follows from exactness. For the other, build a bounded complex $K$ from its finite sequence of standard truncation triangles. Inductively represent the lower truncation and its top cohomology sheaf in $D^b(A_X)$. Their attaching morphism in the ambient derived category lifts by full faithfulness; its cone gives the next truncation in $D^b(A_X)$. The finite induction represents $K$ itself. This keeps all extension data, rather than replacing $K$ by the direct sum of its cohomology sheaves.

The orbit criterion identifies this essential image with $D^b_\Lambda(k_X)$. Thus MSA29 is an equivalence for every $n\geq0$.

## SH02-MSA-IND-VANISHING — A support test vanishes as a formal system

Let $\varphi$ be real valued and $C^1$ near $x_0$, with $\varphi(x_0)=0$ and $(x_0,d\varphi_{x_0})\notin\operatorname{SS}(F)$. Set $H=\{\varphi\geq0\}$ locally. Then

$$
\underset{U\ni x_0}{\text{``}\varinjlim\text{''}}
R\Gamma_H(U;F)=0
\quad\text{in }\operatorname{Ind}(D^b(k)).
\tag{MSA17}
$$

In concrete terms, for every sufficiently small $U$ there is a smaller neighborhood $W$ such that the restriction $R\Gamma_H(U;F)\to R\Gamma_H(W;F)$ is the zero morphism in the derived category. This is stronger than the vanishing of the ordinary colimit of cohomology groups: an infinite-dimensional group can have every element eventually killed without any transition morphism being zero.

**Proof.** If $d\varphi_{x_0}=0$, the zero-section support criterion implies $F=0$ on some neighborhood of $x_0$, and the assertion follows. Otherwise use the cone characterization to choose a bounded representative $A$ on a vector-space chart, agreeing with $F$ near $x_0$, and a pointed cone $C$ with $Rq_{C*}A=0$ and $d\varphi$ strictly negative on its nonzero directions. The cap construction permits a full-dimensional such cone. The geometric argument of `SH02-MST-CONE-TO-TEST` supplies a directionally open set $O$ whose germ at $x_0$ is $\{\varphi<0\}$. For

$$
N_\epsilon=B_\epsilon(x_0)+C
$$

it also supplies a fixed constant $M$ such that

$$
N_\epsilon\setminus O\subset B_{M\epsilon}(x_0)
\tag{MSA18}
$$

for small $\epsilon$. To recall the estimate, the change in $\varphi$ on the starting $\epsilon$-ball is at most a constant times $\epsilon$, while motion along a unit cone direction decreases $\varphi$ at a fixed positive rate. After a length bounded by $M\epsilon$ the ray has entered the negative patch, and its entire remaining tail is in its directional saturation $O$. Strict negativity on the compact unit section of $C$ supplies the uniform rate. These are geometric bounds on neighborhoods, independent of any finite generation of cohomology.

Let $Z=E\setminus O$, which is closed in the directional topology. Directional support compatibility gives an exact zero complex

$$
R\Gamma_Z(N_\epsilon;A)
\simeq R\Gamma(N_{\epsilon,C};
R\Gamma_{Z_C}Rq_{C*}A)=0.
\tag{MSA19}
$$

Here $N_{\epsilon,C}$ is the same directional open set regarded in $E_C$. Fix an ordinary open $U$ sufficiently small that $A=F$ and $Z=H$ on $U$. Choose $\epsilon$ with $N_\epsilon\cap Z\subset U$, using MSA18. Excision for the closed support $Z\cap N_\epsilon$ identifies MSA19 with

$$
R\Gamma_H(N_\epsilon\cap U;F)=0.
$$

Choose an ordinary neighborhood $W$ of $x_0$ contained in $N_\epsilon\cap U$. The restriction from $U$ to $W$ factors through the displayed zero object, proving the concrete assertion and hence MSA17. For a larger initial neighborhood, first restrict into the chart. All complexes have a uniform finite cohomological range by the finite-dimensional manifold bounds, so the asserted formal system does lie in $\operatorname{Ind}(D^b(k))$. $\square$

## SH02-MSA-FILTERED-LIMITS — Compact tests commute with a filtered colimit

Let $(F_i)$ be a small filtered diagram of sheaves on $X$. Then

$$
\operatorname{SS}(\varinjlim_iF_i)
\subset\overline{\bigcup_i\operatorname{SS}(F_i)}.
\tag{MSA20}
$$

The same result holds for a filtered diagram of complexes with a common bounded cohomological range. The colimit is taken in an enhanced complex model, or equivalently as the exact filtered colimit; this statement does not attempt to define a diagram using only unspecified arrows in a triangulated category.

**Compact continuity used in the proof.** On a compact Hausdorff space $K$, sections of module sheaves commute with filtered colimits. A section of the colimit is represented on finitely many open sets by compactness. Choose one common stage and shrink this finite cover so its member closures lie in the original members. Equality of two represented germs on an overlap is witnessed locally at a later stage. The intersection of the corresponding closures is compact, so finitely many witnesses suffice; there are only finitely many pairs of cover members. At a single further stage all represented sections agree and glue. Applying the same argument to a section mapping to zero proves injectivity as well as surjectivity of the section comparison.

This applies to every closed subset of $K$. A filtered colimit of soft sheaves on $K$ is therefore soft: represent a section on the closed subset at one stage and extend it at that stage. Resolve a diagram of sheaves by injectives in its diagram category. Evaluation preserves injectives, because its left adjoint is an exact coproduct indexed by arrows of the indexing category. The colimit of this resolution is a resolution since filtered colimits are exact; its terms are soft since injective sheaves are flabby. Soft sheaves on a compact Hausdorff space are acyclic. Computing with these resolutions proves

$$
\varinjlim_iH^q(K;F_i|_K)
\simeq H^q(K;(\varinjlim_iF_i)|_K).
\tag{MSA21}
$$

For uniformly bounded-below complexes the natural hypercohomology spectral sequences extend MSA21 to all cohomology of derived sections. In each fixed total degree only finitely many terms occur, because the sheaf-cohomology degree is nonnegative and the complex degree has a common lower bound. Exact filtered colimits therefore commute with the successive kernels, quotients, and finite filtrations. This use of cohomology sheaves computes hypercohomology; it does not claim that their microsupports are bounded by that of the original complex.

**Proof of MSA20.** Choose a covector outside the closed union on the right. If it is a zero covector, a common base neighborhood misses the support of every $F_i$, so all these sheaves, and their colimit, vanish there. Otherwise choose a coordinate product $B\times\Omega$ around it that misses every stage microsupport. The compact-cap criterion and its analytic-cap proof choose one pointed cone, one height, and one neighborhood of the moving vertex using only this product window. More explicitly, after identifying the covector with $dx_1$, choose $\delta>0$ so that the positive multiples of $dx_1+\eta\,dx'$ with $|\eta|\leq\delta$ lie in $\Omega$. Take

$$
C=\{v_1\leq-\delta|v'|\},\qquad
K_x=(x+C)\cap\{x_1\geq-h\},\qquad
L_x=(x+C)\cap\{x_1=-h\}.
$$

Take $h$ and the vertex neighborhood small enough that the caps and the slightly enlarged rounded caps in that proof lie in $B$. Their moving normals all lie in the fixed window. Thus the same noncharacteristic-deformation proof gives

$$
R\Gamma(K_x;F_i)\xrightarrow{\sim}R\Gamma(L_x;F_i)
\tag{MSA22}
$$

for every $i$ and every vertex in that neighborhood. This is a common choice of caps, not an intersection of infinitely many neighborhoods chosen separately for different sheaves. Both cap and base are compact. Apply MSA21 and its complex version to MSA22; naturality makes the resulting isomorphism the restriction map for the colimit. The converse compact-cap criterion excludes the chosen covector from the colimit microsupport. $\square$

## SH02-MSA-CONE-RESOLUTION — A proper resolution separates a complex from its cohomology

Let $E=\mathbb R^3$, with coordinates $(u,v,t)$, and put

$$
C=\{(u,v,t):u^2+v^2=t^2,\ t>0\},\qquad
j:C\hookrightarrow E,\qquad F=Rj_*k_C.
$$

For nonzero $k$ we will prove

$$
(0,-dt)\notin\operatorname{SS}(F),\qquad
\mathcal H^1(F)=k_{\{0\}},\qquad
(0,-dt)\in\operatorname{SS}(\mathcal H^1F).
\tag{MSA1}
$$

Consider the smooth map

$$
q:S^1\times\mathbb R\longrightarrow E,
\qquad q(\theta,r)=(r\cos\theta,r\sin\theta,r).
$$

Its restriction to $S^1\times(0,\infty)$ is a diffeomorphism onto $C$, and $q$ is proper on $S^1\times[0,\infty)$. Indeed a bound for the last coordinate bounds $r$, while the angular factor is compact. If $h:S^1\times(0,\infty)\hookrightarrow S^1\times\mathbb R$, then

$$
Rh_*k=k_{S^1\times[0,\infty)}.
\tag{MSA2}
$$

To check MSA2, take product neighborhoods. At $r=0$, the positive interval has constant cohomology $k$ in degree zero, and restriction of the constant generator gives the asserted stalk map. At positive $r$ the assertion is the identity, and at negative $r$ both sides vanish. The interval calculation also eliminates every higher direct image. Composition of direct images now gives

$$
F\simeq Rq_*k_{S^1\times[0,\infty)}.
\tag{MSA3}
$$

The boundary microsupport calculation on the cylinder is explicit: at $r>0$ only zero covectors occur, and at $r=0$ its covectors are $\lambda\,dr$ with $\lambda\geq0$. The proper-image estimate therefore bounds the fibre of $\operatorname{SS}(F)$ at the vertex by those $(\xi,\eta,\tau)$ for which some $\theta$ satisfies

$$
\xi\cos\theta+\eta\sin\theta+\tau\geq0.
$$

Their union is $\tau\geq-\sqrt{\xi^2+\eta^2}$. In particular it excludes $-dt$. This use of the estimate is legitimate for the noncompact cylinder: properness is needed on its closed support over compact target sets, and that was verified before applying the estimate.

Proper base change in MSA3 gives the cohomology of a point on $C$, the cohomology of $S^1$ at the vertex, and zero off the closed cone. Thus the only positive cohomology sheaf is $\mathcal H^1F=k_{\{0\}}$. The generator is the oriented circle class; changing that orientation changes the identification by a unit and does not change the sheaf or its support. A nonzero sheaf supported at a point has every cotangent direction at that point in its microsupport: each local support test compares its stalk with zero. This proves MSA1.

The finite truncation triangles always give the opposite, correctly directed estimate

$$
\operatorname{SS}(F)\subset
\bigcup_j\operatorname{SS}(\mathcal H^jF).
\tag{MSA4}
$$

Only finitely many terms occur. Applying the triangle inequality successively to $\tau_{\leq j-1}F\to\tau_{\leq j}F\to\mathcal H^jF[-j]$ proves MSA4, including the zero complex. MSA1 shows why one cannot reverse it term by term. The [cone-projector example](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-PROBLEMS) gives another construction of the same failure in a different dimension.

## SH02-MSA-INVERSE-LIMIT — A countable ordinary limit can acquire a new direction

An ordinary inverse limit has a different behavior. Use the closed cone $\overline C=\{u^2+v^2=t^2,\ t\geq0\}$ from MSA1 and put

$$
Z_n=\overline C\cap\{t\geq1/n\},\qquad
F_n=k_{Z_n},\qquad F_{n+1}\longrightarrow F_n.
\tag{MSA23}
$$

The arrows are restriction to the smaller closed subset. They are epimorphisms of sheaves: on that subset the stalk map is the identity and elsewhere its target is zero. Nevertheless

$$
(0,-dt)\notin\overline{\bigcup_n\operatorname{SS}(F_n)},
\qquad
(0,-dt)\in\operatorname{SS}(\varprojlim_nF_n).
\tag{MSA24}
$$

**The stage covectors.** At a point of $Z_n$, let $r=\sqrt{u^2+v^2}>0$ and $e=(u/r,v/r)$. Local coordinates consisting of angle, $t$, and $r-t$ identify the set with a closed half-line times a point times an open interval. Hence its microsupport covectors are

$$
(\lambda e,-\lambda)\quad(t>1/n),\qquad
(\lambda e,-\lambda+\mu)\quad(t=1/n),
\qquad \lambda\in\mathbb R,\ \mu\geq0.
\tag{MSA25}
$$

The last sign is the positive conormal of the closed lower endpoint, and the free parameter $\lambda$ is the conormal to $r=t$. Every such covector $(\eta,\tau)$ satisfies $\tau\geq-|\eta|$. This closed inequality also contains the closure of the union. It excludes the open cone $\tau<-|\eta|$, in particular the covector $-dt$ at the vertex. No stage is supported at that vertex.

**The actual sheaf limit.** Limits of sheaves are computed on open-set sections. A compatible family of locally constant functions on $U\cap Z_n$ determines a locally constant function on $U\cap C$, where $C=\overline C\setminus\{0\}$. Near any point of $C$, the inequality $t>1/n$ holds for some $n$, so that one stage already proves local constancy. Restriction gives the inverse construction. Thus

$$
\varprojlim_nF_n=j_*k_C=k_{\overline C},
\tag{MSA26}
$$

where the first direct image is ordinary. For the second equality, the natural map from the closed-cone constant sheaf is already an isomorphism away from the vertex. At the vertex, punctured conical neighborhoods are connected, so their locally constant functions are exactly $k$, compatibly under shrinking. The stalk map there is also the identity. This argument computes the sheaf limit first; commuting a stalk with that inverse limit would incorrectly give zero at the vertex.

**The local obstruction.** For $\varphi=-t$, the support condition $\varphi\geq0$ meets $\overline C$ only at its vertex. On a small ball the closed cone is contractible, while its punctured part retracts to $S^1$. The localization triangle for $k_{\overline C}$ is therefore

$$
R\Gamma_{\{t\leq0\}}(B_\epsilon;k_{\overline C})
\longrightarrow k\longrightarrow R\Gamma(S^1;k)\xrightarrow{+1}.
$$

The degree-zero restriction is the identity. Its supported complex is consequently $k[-2]$. Shrinking the ball preserves the angular circle class, so the supported stalk is still $k[-2]\ne0$. The single test at the vertex proves the second assertion in MSA24.

The example even permits a common compact bound on the supports: replace $Z_n$ by $\{r=t,\ 1/(n+1)\leq t\leq1\}$. The additional upper boundary covectors are based away from the vertex and do not affect the microsupport-free neighborhood used in MSA24. Every stage can thus be a rank-one semialgebraically constructible sheaf, all transition maps epimorphic, and all closed supports contained in a fixed compact set. None of those extra conditions fixes the ordinary-limit assertion.

In this particular tower the derived limit has a useful exact description. The closed exhaustion of $C$ by the $Z_n$ has interiors covering $C$ and satisfies the hypotheses of `SH02-EXH-COMPARISON`. Since derived direct image preserves derived limits,

$$
R\varprojlim_nF_n\simeq Rj_*k_C.
\tag{MSA27}
$$

Its degree-zero sheaf is $k_{\overline C}$ and its degree-one sheaf is $k_{\{0\}}$, by MSA3. The full complex has no $-dt$ direction, by MSA1. Its higher term carries information that the ordinary limit discards. This computation is not an assertion that every derived inverse limit satisfies MSA20, and epimorphic sheaf transitions do not by themselves identify derived and ordinary inverse limits: infinite products of sheaves need not be exact.

The literal countable ordinary-limit inclusion in the checked edition is contradicted by MSA24. The surviving mathematical lesson is the precise distinction between the two limits exhibited above.

## SH02-MSA-NONCONVEX-CUTOFF — An angular open set defines a cutoff kernel

Let $V$ have dimension $d$ and let $\Omega\subset V^*$ be an arbitrary open set invariant under positive scaling. Convexity and connectedness are not assumed. Write $T_{V^*}$ for the Fourier functor from $V^*$ to $V$ with the closed nonpositive pairing convention, and $a(v)=-v$. Define

$$
G=a^{-1}T_{V^*}(k_\Omega)\otimes\omega_V,
\qquad K=\mu^{-1}G,\qquad \mu(x,y)=y-x.
\tag{MSA5}
$$

Here $\omega_V=\operatorname{or}_V[d]$. The antipode is on the output vector space; no orientation factor is silently trivialized. The inverse-Fourier formula identifies $G$ with $S_V(k_\Omega)$, the inverse transform from $V^*$ to $V$. With $p_1,p_2:V\times V\to V$, put

$$
Q_\Omega F=Rp_{2!}(p_1^{-1}F\otimes K).
$$

Then there is a natural morphism

$$
Q_\Omega F\longrightarrow F,
\qquad
\operatorname{SS}(Q_\Omega F)\subset V\times\overline\Omega,
\qquad
\operatorname{SS}(\operatorname{Cone}(Q_\Omega F\to F))
\cap(V\times\Omega)=\varnothing.
\tag{MSA6}
$$

**Proof.** We first record an integration argument that addresses the possible noncompact support of $F$. Suppose $H$ is a bounded conic complex on $V$ and $\operatorname{SS}(H)\subset V\times A$ for a closed cone $A\subset V^*$. Write $s(x,z)=x+z$. If $F$ has compact support, $s$ is proper on $\operatorname{supp}(F)\times\operatorname{supp}(H)$: for $x$ in the compact first factor and $x+z$ in a compact set, $z$ is bounded; closedness finishes the argument. The exterior-product and proper-image estimates give

$$
\operatorname{SS}(Rs_!(F\boxtimes H))\subset V\times A.
\tag{MSA7}
$$

Indeed the pullback of a target covector $\eta$ is $(\eta,\eta)$, so the second factor already forces $\eta\in A$.

For general $F$, take increasing relatively compact open balls $B_n$ whose union is $V$. The open extensions $F_{B_n}$ have compact closed support and $\varinjlim F_{B_n}=F$, with one uniform cohomological bound. Proper-support direct image and tensor commute with filtered colimits. The filtered-colimit microsupport estimate in `SH02-MSA-FILTERED-LIMITS`, in its uniformly bounded complex version, passes MSA7 to $F$. That version uses compact hypercohomology continuity directly; it does not impose a false microsupport bound on the individual cohomology sheaves. This is the reason arbitrary support is allowed; applying a proper-image theorem directly to $s$ would leave a gap.

For any bounded conic $A_0$ on $V^*$, the Fourier microsupport formula sends $(\eta,\zeta)$ to $(\zeta,-\eta)$ under $T_{V^*}$. Antipodal pullback then sends it to $(-\zeta,\eta)$. A locally constant orientation twist changes no microsupport. Consequently

$$
\operatorname{SS}(S_VA_0)
\subset V\times\operatorname{supp}(A_0).
\tag{MSA8}
$$

Closed support is intended on the right. Apply MSA7 to MSA8 for $A_0=k_\Omega$ to obtain the first estimate in MSA6.

The open-extension map $k_\Omega\to k_{V^*}$ gives, after inverse Fourier transformation, a morphism $G\to k_{\{0\}}$. Here $S_V(k_{V^*})\simeq k_{\{0\}}$ is the orientation-normalized inverse-transform identification. Convolution with this morphism defines the map in MSA6, because convolution with $k_{\{0\}}$ is the identity by the diagonal unit. Its cone is convolution with $S_V(k_{V^*\setminus\Omega})$, by the open-closed localization triangle. MSA8 and MSA7 place its microsupport in $V\times(V^*\setminus\Omega)$, proving the second estimate. All maps were obtained from the open-extension map and the fixed Fourier and kernel units. No assertion about equality of two independently chosen Fourier adjunction normalizations is needed. $\square$

For $\Omega=\varnothing$, the functor is zero and its microlocal assertion is empty. For $\Omega=V^*$ it is the identity. If an open conic set contains zero, it is all of $V^*$; this includes the dimension-zero case. In dimension one, choosing the positive covector ray gives $G=k_{[0,\infty)}$, which checks both the sign of the antipode and the shift in MSA5.

## SH02-MSA-TIME-CONDITION — Families with no pure temporal obstruction

Let $k$ be the course's commutative unital coefficient ring of finite global dimension. All manifolds have the course's finite-dimensional, countable-at-infinity hypotheses. Write a covector on $X\times\mathbb R_t$ as $(x,t;\xi,\tau)$. Call a bounded complex $K$ **regular in the time direction** here if

\[
(x,t;0,\tau)\in\operatorname{SS}(K)\quad\Longrightarrow\quad\tau=0.
\tag{HT1}
\]

This condition permits arbitrary spatial singularities, including spatial covectors with a nonzero time component. It is not the stronger assertion that all time components of microsupport vanish. The support below is the closed support of the complex. In particular, $k_{[0,1)}$ has closed support $[0,1]$.

The proofs use these exact previously stated results: submersion pullback of microsupport (`SH02-MO-SUBMERSION`); proper direct image (`SH02-MO-PROPER-PUSH`); the noncharacteristic tensor and Hom estimates (`SH02-MO-DIAGONAL`); noncharacteristic inverse image and its canonical exceptional comparison (`SH02-MO-PULLBACK`); the recognition of zero microsupport as local constancy, including bounded derived interval descent; proper base change; open localization; and manifold duality with `SH02-MD-BOUNDED-HOM`.

### SH02-MSA-TIME-CORNER — A corner in a time graph

Put $c(s)=\max(s,0)$ and

\[
S=\{(t,s):t=c(s)\}\subset\mathbb R_t\times\mathbb R_s.
\]

The only singular point of this graph is the origin. Along its negative branch its conormal covectors satisfy $b=0$, and along its positive branch they satisfy $a+b=0$, where a covector is written $a\,dt+b\,ds$. At the origin we have the sufficient bound

\[
\operatorname{SS}(k_S)\cap T^*_{(0,0)}\mathbb R^2
\subset\{(a,b):b(a+b)\leq0\}.
\tag{HT2}
\]

Here is a test-function proof, so that the corner is not treated as a differentiable graph. Suppose $b$ and $a+b$ have the same strict sign. On sufficiently small neighborhoods of the origin and of this covector, every admissible $C^1$ test function $f$ has derivatives along the two branches, parameterized by $s$, with this same strict sign:

\[
\frac{d}{ds}f(0,s)=\partial_sf(0,s),\qquad
\frac{d}{ds}f(s,s)=(\partial_t+\partial_s)f(s,s).
\]

Consequently $f(c(s),s)$ is strictly monotone, also across $s=0$. A level through any nearby graph point cuts this topological line into two intervals. The local-cohomology test for the closed upper side is the cone, shifted by $[-1]$, of the restriction from constant-complex cohomology on a small interval to that on one open half-interval. That restriction is the identity of $k$, so the test vanishes. Points off the graph give zero stalks automatically. The signs are uniform in the chosen neighborhoods, which is the neighborhood requirement in the definition of microsupport, and proves HT2. On either smooth branch the same argument is the usual conormal computation. In particular, everywhere on the graph,

\[
(0,b)\in\operatorname{SS}(k_S)\quad\Longrightarrow\quad b=0.
\tag{HT3}
\]

We only need the upper bound HT2; no assertion of equality at the corner enters the argument.

### SH02-MSA-TIME-CLAMP — Clamping preserves temporal regularity

Let $F\in D^b(k_{X\times\mathbb R_t})$ satisfy HT1. On $X\times\mathbb R_t\times\mathbb R_s$, denote the projections to the $(x,t)$ and $(x,s)$ variables by $q_1$ and $q_2$, and set $c_X=\mathrm{id}_X\times c$. The graph embedding

\[
i:X\times\mathbb R_s\longrightarrow X\times\mathbb R_t\times\mathbb R_s,
\qquad i(x,s)=(x,c(s),s)
\]

is a closed topological embedding and $q_2i=\mathrm{id}$. Closed-embedding localization and the projection formula therefore give an identification of the specified functors,

\[
c_X^{-1}F
\simeq Rq_{2*}\bigl(q_1^{-1}F\otimes^L k_{X\times S}\bigr).
\tag{HT4}
\]

Indeed, the tensor product is $i_*i^{-1}q_1^{-1}F$. The map $q_2$ is proper on its closed support: it is a homeomorphism on the entire closed graph, and the support is a closed subset of that graph.

The submersion formulas identify the two microsupports used in the tensor product with sets of covectors of the forms

\[
(\xi,\tau,0),\quad (x,t;\xi,\tau)\in\operatorname{SS}(F),
\qquad
(0,a,b),\quad(t,s;a,b)\in\operatorname{SS}(k_S).
\]

They satisfy the no-cancellation hypothesis for the tensor estimate. In fact, a vector in their intersection after antipodal reversal has $\xi=0$; HT1 forces $\tau=0$, and hence the whole vector is zero. Thus the microsupport of the tensor product is contained in their ordinary sum, with all components evaluated at the same base point.

For a pure nonzero time covector $(x,s;0,b)$ to belong to the proper direct-image upper bound for HT4, its pullback $(0,0,b)$ would have to be such a sum. The spatial component again forces $\xi=0$, whence $\tau=0$. The $dt$ component then forces $a=0$, and HT3 forces $b=0$, a contradiction. This proves HT1 for $c_X^{-1}F$ at the corner as well as elsewhere.

There is no hypothesis of properness of $F$ in this argument. The proper map used in HT4 is the graph projection, which is proper for every $F$. Inverse image is exact, so the resulting complex is still bounded.

Affine changes of the time coordinate with nonzero slope preserve HT1 by the diffeomorphism formula. Applying such changes before and after the preceding clamp also proves the result for $s\mapsto\min(s,a)$ and for $s\mapsto\max(s,a)$ at any real $a$. Composition gives it for the two-sided clamp

\[
e(s)=\min(\max(s,0),1).
\tag{HT5}
\]

For completeness, a smooth scalar change $u$ also preserves HT1, even where $u'=0$. The map $(x,s)\mapsto(x,u(s))$ is noncharacteristic for $\operatorname{SS}(F)$: any covector in the kernel of its transpose differential has $\xi=0$, so HT1 makes it zero. Its noncharacteristic pullback estimate then excludes nonzero pure time covectors in the result. This observation is not substituted for the corner argument, where $c$ is not differentiable.

### SH02-MSA-TIME-PROPER — Compact support bounds over compact time sets

Write $p:X\times\mathbb R\to\mathbb R$ for time projection. Suppose $p$ is proper on the closed support $Z$ of $F$. For any continuous $u:\mathbb R\to\mathbb R$, the closed support of $u_X^{-1}F$ is contained in $u_X^{-1}Z$. If $J$ is a compact set of new times, $u(J)$ is compact. The set $Z\cap p^{-1}(u(J))$ is compact, and its projection to $X$ is a compact set $B$. Therefore

\[
u_X^{-1}Z\cap(X\times J)\subset B\times J
\]

is closed in a compact space. Thus the new support is again proper over time. This is stronger than checking compactness of the individual spatial fibers: the argument supplies the needed uniform bound over each compact set of times.

In particular, if $H$ is a homotopy between its fibers at $0$ and $1$, pulling it back by $s\mapsto\min(s,1)$ leaves these two fibers unchanged and makes it the constant product of its time-$1$ fiber on the whole closed region $s\geq1$. Its restriction to $X\times[1,2]$ is thus

\[
H_1\boxtimes k_{[1,2]}.
\tag{HT6}
\]

This is a statement on that closed subspace; extension by zero to $X\times\mathbb R$ is not being asserted. HT3-HT5 establish regularity in time at the boundary as well. Applying the two-sided clamp HT5 makes the family constant for all $s\leq0$ and all $s\geq1$, with the appropriate two endpoint fibers.

## SH02-MSA-HOMOTOPY — Gluing families into an equivalence relation

Consider compactly supported objects of $D^b(k_X)$. Declare two such objects related when they occur at times $0,1$ in a time-regular bounded complex whose closed support is proper over time.

Reflexivity is witnessed by the inverse image of $F$ under $X\times\mathbb R\to X$. Its microsupport has zero time component, and its support is the product of a compact set with $\mathbb R$, which is proper over time. Symmetry is obtained by the diffeomorphism $s\mapsto1-s$.

For transitivity let $H$ join $F_0$ to $F_1$ and let $K$ join $F_1$ to $F_2$, with a chosen isomorphism between the two displayed middle fibers. First replace each family by its two-sided-clamped version. Set

\[
A=(\mathrm{id}_X\times(3s))^{-1}H,
\qquad
B=(\mathrm{id}_X\times(3s-2))^{-1}K.
\]

Both complexes are time regular and proper over time. On the overlap

\[
W=X\times(1/3,2/3)
\]

they are the same constant product $C=F_1\boxtimes k_{(1/3,2/3)}$, under the chosen isomorphism. Put

\[
U=X\times(-\infty,2/3),\qquad
V=X\times(1/3,\infty).
\]

These two opens cover the whole product. There is an explicit bounded derived gluing object, so gluing the cohomology sheaves alone is unnecessary. If $j_U,j_V,j_W$ denote the open embeddings, take the cone of

\[
j_{W!}C\longrightarrow
j_{U!}(A|_U)\oplus j_{V!}(B|_V),
\qquad c\longmapsto(c,-c),
\tag{HT7}
\]

where each component is the adjunction map after identifying the restriction with $C$. More precisely, choose representatives of this morphism in a dg model of sheaf complexes and take its ordinary cone. The resulting distinguished triangle defines an object $L\in D^b(k_{X\times\mathbb R})$.

On $U$ the second summand restricts to the extension by zero of $C$ from $W$, and the corresponding component in HT7 is its negative identity. Cancelling this split identity identifies $L|_U$ with $A|_U$. The identical argument on $V$ gives $L|_V\simeq B|_V$. This proves gluing of the complete derived objects and their extension data. Since microsupport is local, $L$ is time regular. Its closed support is contained in the union of the closed supports of $A$ and $B$: at any point outside that union, one of the two local descriptions is zero on a neighborhood. Over a compact set of times this union is compact by `SH02-MSA-TIME-PROPER`; therefore the support of $L$ is proper over time. Finally $L_0\simeq F_0$ and $L_1\simeq F_2$. This proves transitivity without a uniqueness claim about the gluing cone.

### SH02-MSA-HOMOTOPY-DUAL — Duality and its time shift

Let $D_XF=R\mathcal Hom(F,\omega_X)$ be Verdier duality. The bounded-Hom theorem for manifolds and the finite-global-dimension coefficient hypothesis ensure that $D_X$ and $D_{X\times\mathbb R}$ take the bounded objects here to bounded objects; finite rank, perfect stalks, and constructibility are not required for this assertion.

Given a homotopy $H$, use the usual increasing orientation of $\mathbb R$ and put

\[
\widehat H=D_{X\times\mathbb R}H[-1].
\tag{HT8}
\]

The Hom estimate with second target $\omega_{X\times\mathbb R}$ gives

\[
\operatorname{SS}(D_{X\times\mathbb R}H)
\subset\operatorname{SS}(H)^a,
\tag{HT9}
\]

because the microsupport of the orientation complex is the zero section. The no-cancellation hypothesis for this Hom estimate is automatic. Thus HT1 is preserved. The closed support of the dual is contained in the closed support of $H$, so time properness is preserved too. Neither assertion uses biduality or equality in HT9.

For the closed slice $i_t:X\hookrightarrow X\times\mathbb R$, the exceptional internal-Hom adjunction and $i_t^!\omega_{X\times\mathbb R}=\omega_X$ give

\[
i_t^!D_{X\times\mathbb R}H\simeq D_X(i_t^{-1}H).
\tag{HT10}
\]

The embedding $i_t$ is noncharacteristic for the dual by HT9 and HT1. Its relative orientation complex is $\omega_{i_t}=k_X[-1]$ for the fixed orientation of the time line. The canonical noncharacteristic comparison consequently identifies

\[
i_t^{-1}D_{X\times\mathbb R}H[-1]
\simeq i_t^!D_{X\times\mathbb R}H.
\tag{HT11}
\]

Combining HT10 and HT11 shows that the fibers of HT8 are $D_XH_t$. In particular they are $D_XF_0$ and $D_XF_1$ at the endpoints. These fibers have compact supports because the original endpoints do. The shift $[-1]$ in HT8 is necessary: the ambient product dualizing complex contains the oriented time factor $k_{\mathbb R}[1]$.

### SH02-MSA-HOMOTOPY-COHOMOLOGY — The endpoint cohomology objects

Let $P=Rp_*H$. Because $p$ is proper on the closed support, $Rp_*H=Rp_!H$, and the finite cohomological-dimension bound for manifolds keeps $P$ bounded. The proper direct-image estimate says that a covector $(t;\tau)$ in $\operatorname{SS}(P)$ is induced by a covector $(x,t;0,\tau)$ of $\operatorname{SS}(H)$. HT1 therefore gives

\[
\operatorname{SS}(P)\subset T^*_{\mathbb R}\mathbb R.
\]

The zero-microsupport criterion and bounded derived descent on an interval identify $P$ with a locally constant derived object on $\mathbb R$. All its fibers are isomorphic; equivalently, either endpoint restriction from its constant-complex cohomology on $[0,1]$ is an isomorphism. Proper base change identifies its fiber at time $t$ with

\[
P_t\simeq R\Gamma(X;H_t).
\tag{HT12}
\]

Hence the two endpoint derived cohomology objects are isomorphic, and so are their groups in each integer degree. Time properness is used both to invoke the proper microsupport estimate and to identify the correct fibers. Local constancy of individual cohomology sheaves of $H$ on time lines has not been substituted for these assertions.

### SH02-MSA-HOMOTOPY-COLLAPSE — A dilation family and three endpoint calculations

There is a useful stronger construction on a real vector space $E$. Let $A\in D^b(k_E)$ have compact closed support, and consider

\[
g:E_u\times\mathbb R_t\longrightarrow E_x\times\mathbb R_t,
\qquad g(u,t)=((1-t)u,t),
\qquad
H_A=Rg_*(A\boxtimes k_{\mathbb R}).
\tag{HT13}
\]

Although $g$ ceases to be a submersion at $t=1$, it is a smooth map and is proper on the closed support of its argument. Indeed, the spatial source coordinate lies in the fixed compact set $\operatorname{supp}(A)$, and a compact target set bounds $t$; the relevant inverse image is closed in the resulting compact product. The proper image of this support is a closed set proper over time. The support of $H_A$ is contained in it. The finite manifold cohomological-dimension bound makes $H_A$ bounded.

There are no nonzero pure time covectors in $\operatorname{SS}(H_A)$. To see this at the singular time as well, write a target covector as $(\xi,\tau)$. Its transpose differential is

\[
{}^tdg_{(u,t)}(\xi,\tau)
=((1-t)\xi,\ \tau-\langle u,\xi\rangle).
\tag{HT14}
\]

For a pure time covector $\xi=0$, this is $(0,\tau)$. The submersion formula for $A\boxtimes k_{\mathbb R}$ says that every one of its microsupport covectors has zero time component. Thus HT14 cannot lie in that microsupport if $\tau\ne0$. The proper direct-image estimate proves the assertion. No noncharacteristic inverse image through the collapsing map is used.

At $t=0$, proper base change identifies the fiber of HT13 with $A$, since the spatial map is the identity. At $t=1$, it is the direct image under the constant map $E\to E$, $u\mapsto0$, so

\[
(H_A)_1\simeq i_{0*}R\Gamma(E;A),
\tag{HT15}
\]

where $i_0$ includes the origin. Ordinary and compact-support cohomology agree here because the closed support of $A$ is compact. In particular this is an actual sheaf homotopy from $A$ to a skyscraper whose coefficient complex is its derived cohomology. The support remains proper over all real times, even though it need not remain in one spatial compact set as $|t|\to\infty$.

For $E=\mathbb R$, compute the three coefficient complexes directly on $I=[0,1]$. The constant sheaf on this compact convex interval has cohomology $k$ in degree zero and no higher cohomology. The localization sequence at the right endpoint is

\[
0\longrightarrow k_{[0,1)}\longrightarrow k_{[0,1]}
\longrightarrow k_{\{1\}}\longrightarrow0.
\]

On derived global sections the last arrow is the identity of $k$, so $R\Gamma(\mathbb R;k_{[0,1)})=0$. At both endpoints the localization sequence is

\[
0\longrightarrow k_{(0,1)}\longrightarrow k_{[0,1]}
\longrightarrow k_{\{0\}}\oplus k_{\{1\}}\longrightarrow0.
\]

It identifies $R\Gamma(\mathbb R;k_{(0,1)})$ with the two-term complex

\[
[\,k\xrightarrow{a\mapsto(a,a)}k\oplus k\,],
\]

placed in degrees $0$ and $1$. The difference map $(a,b)\mapsto b-a$ identifies its cokernel with $k$; its kernel is zero. Thus this coefficient complex is $k[-1]$, with its positive interval generator fixed by the increasing orientation.

Substitution into HT13-HT15 gives, respectively,

\[
k_{[0,1]}\ \leadsto\ k_{\{0\}},\qquad
k_{[0,1)}\ \leadsto\ 0,\qquad
k_{(0,1)}\ \leadsto\ k_{\{0\}}[-1].
\tag{HT16}
\]

The convention is $H^j(C[m])=H^{j+m}(C)$; hence the last skyscraper has its nonzero cohomology in degree $1$. The localization calculation is valid for the coefficient ring itself without a field or finite-rank assumption. More generally it works with any bounded coefficient complex in place of $k$.

## SH02-MSA-ERASING-SUPPORT — A missing conormal direction kills a restriction morphism

Let $i:Y\hookrightarrow X$ be a closed submanifold. Suppose the projection

$$
N_Y^*X\setminus\operatorname{SS}(F)\longrightarrow Y
$$

has a continuous section $\sigma$. Then the canonical composite

$$
i^!F\longrightarrow i^{-1}F
\tag{MSA9}
$$

is zero in $D^b(k_Y)$. The arrow means the restriction of the support-forgetting map $i_*i^!F\to F$, followed by the identification $i^{-1}i_*\simeq1$.

**Proof.** For every $A\in D^b(k_Y)$ there is a natural identification

$$
\mu_Y(i_*A)\simeq\pi^{-1}A,
\qquad\pi:N_Y^*X\to Y.
\tag{MSA10}
$$

Specialization of $i_*A$ is the zero-section sheaf on the normal bundle, by the deformation-space description and base change. Its Fourier transform is $\pi^{-1}A$: the Fourier kernel over the zero vector imposes no inequality and its remaining projection is the identity. Both identifications are natural in $A$.

Apply $\mu_Y$ to $i_*i^!F\to F\to i_*i^{-1}F$. Under MSA10 the composite is $\pi^{-1}$ of MSA9. By `SH02-MO-MICROLOCAL-SUPPORT`, the support of $\mu_YF$ lies in $N_Y^*X\cap\operatorname{SS}(F)$. Pullback by $\sigma$ therefore kills the middle object. On the two outer objects, $\sigma^{-1}\pi^{-1}=1$ since $\pi\sigma=1_Y$. The composite is MSA9, so it is zero. Continuity suffices: ordinary inverse image is exact for continuous maps. The section need not be differentiable or integrable. $\square$

For $F=k_X$, a nowhere-zero section of the conormal bundle avoids the zero-section microsupport of $k_X$. Thus MSA9 vanishes. The [Thom and Euler identifications](../duality-applications.html#sh02-da-euler-what-remains-after-support-is-forgotten) identify this with the vanishing of the normal Euler class, including its coefficient and orientation conventions. For an oriented normal bundle of rank $c$, the [Gysin morphism](../duality-applications.html#sh02-da-gysin-removing-a-closed-submanifold) followed by restriction is therefore zero:

$$
H^r(Y;k)\longrightarrow H^{r+c}(X;k)
\longrightarrow H^{r+c}(Y;k).
\tag{MSA11}
$$

The first arrow comes from the supported adjunction map, and the second is ordinary restriction. Hence this conclusion concerns the specified maps, not just an equality of characteristic classes. A nowhere-zero normal vector section and a nowhere-zero conormal section are equivalent after choosing a bundle metric. Without orientation the same assertion holds with the normal orientation local system retained. Rank zero over a nonempty base has no nowhere-zero conormal section, so the hypothesis does not mistakenly force the identity map to vanish.

## SH02-MSA-MORSE-EULER — Counting local quadratic jumps

Assume in this section that $k$ is a field. Let $\varphi:X\to\mathbb R$ be smooth, every set $\{\varphi\leq t\}$ compact, and the critical set finite. Suppose its points $x_1,\ldots,x_N$ are nondegenerate, with Morse indices $\lambda_1,\ldots,\lambda_N$. Then

$$
R\Gamma(X;k_X)\in D^b(\operatorname{Mod}^{\mathrm{fd}}k),
\qquad
\sum_r(-1)^r\dim_k H^r(X;k)
=\sum_{j=1}^N(-1)^{\lambda_j}.
\tag{MSA12}
$$

No compactness of $X$ is assumed. Empty $X$ gives two zero sums.

**Proof of the local calculation.** Near a critical point translate its value to zero. Taylor's formula with integral remainder writes $\varphi(x)=x^{\mathsf T}A(x)x$, where $A$ is smooth symmetric and $A(0)$ is nonsingular. After a fixed linear change of variables, its value at zero is the diagonal matrix $J$ with $\lambda$ entries $-1$ and the remaining entries $1$. Smooth indefinite Gram–Schmidt on a neighborhood of this matrix gives a smooth invertible $L(x)$ with $A(x)=L(x)^{\mathsf T}JL(x)$. Explicitly, eliminate the off-diagonal entries successively using the nonzero diagonal pivot at zero, then divide each diagonal entry by the square root of its positive absolute value. Shrinking preserves every pivot sign. The map $x\mapsto L(x)x$ has invertible derivative at zero; the inverse-function theorem gives local coordinates $(u,v)$ in which

$$
\varphi=-|u|^2+|v|^2,
\qquad u\in\mathbb R^\lambda.
\tag{MSA13}
$$

On a small ball the negative set $|v|<|u|$ deformation retracts onto the sphere $S^{\lambda-1}$: first contract $v$ to zero, then radially normalize the nonzero $u$. These homotopies remain in the negative set. The local support triangle for $\{\varphi\geq0\}$ is the relative cohomology triangle of the ball and that negative set. The ball is contractible, so its relative complex is $k[-\lambda]$. For $\lambda=0$ the negative set is empty and the relative complex is $k$; this agrees with the same formula. The sphere cohomology computation can be made by two hemispheres and their overlap, so it is valid over any ring at this local step. Thus the local Morse group has one generator in degree $\lambda$.

**Passage to the whole manifold.** If $X$ is nonempty, $\varphi$ is bounded below and attains its infimum. To see this, a sequence of values approaching an infimum of $-\infty$ or a finite unattained infimum would eventually lie in one fixed nonempty compact sublevel; a convergent subsequence gives respectively an impossibility or a minimum. Its minimum is a critical value. Choose finitely many regular levels separating the distinct critical values, with one below all of them and one above. The microsupport of $k_X$ is the zero section, so precisely the critical points can contribute to the local tests. The finite Morse filtration of `SH02-MO-MORSE-INEQUALITIES` gives triangles whose jump objects are the direct sums of the complexes $k[-\lambda_j]$ at the intervening critical value. Compact sublevels supply the properness on each finite strip required by that theorem. The same deformation argument above the last critical level, together with the open-union comparison for the exhaustion by sublevels, identifies the terminal object with $R\Gamma(X;k_X)$.

The initial object is zero. Induction through finitely many triangles shows that the terminal object is bounded with finite-dimensional cohomology. In a triangle of such objects Euler characteristics add: split the long exact sequence into its finite-dimensional kernels and images, and cancel the dimensions of each image in its two adjacent degrees. Each local summand contributes $(-1)^{\lambda_j}$, giving MSA12. $\square$

For a concrete model, on $\mathbb R^m$ take a positive definite quadratic form. There is one critical point, of index zero, and the conclusion is $H^0=k$, all other cohomology zero. The same argument applies to a proper Morse exhaustion on a noncompact manifold with finitely many handles; no compactification term is added to the ordinary Euler characteristic.

## SH02-MSA-DUAL-DETECTION — Coefficient duality detects every missing direction

Keep the course's commutative unital ring $k$ of finite global dimension and its finite-dimensional manifolds. Assume in addition that

\[
M\in D^b(\operatorname{Mod}k),\qquad
R\operatorname{Hom}_k(M,k)=0
\quad\Longrightarrow\quad M=0.
\tag{DD1}
\]

For every $F\in D^b(k_X)$, the claim is

\[
\operatorname{SS}(D_XF)=\operatorname{SS}(F)^a,
\qquad D_XF=R\mathcal Hom(F,\omega_X).
\tag{DD2}
\]

The usual bounded-Hom theorem for manifolds ensures that $D_XF$ and all internal Hom objects below are bounded. No constructibility, finite stalk rank, finite generation, or biduality is assumed under DD1.

The already proved Hom upper bound gives

\[
\operatorname{SS}(D_XF)\subset\operatorname{SS}(F)^a.
\tag{DD3}
\]

Indeed the orientation complex has microsupport in the zero section, so the no-cancellation hypothesis of the Hom estimate is automatic. The task is to prove the reverse inclusion. The key is to dualize a bounded complex attached to a finite compact cap, not the limit of local tests.

### SH02-MSA-DUAL-CAP-ADJUNCTION — The actual dual of a cap restriction

Let $U$ be an open coordinate domain, $F_U=F|_U$, and $Q=D_UF_U=(D_XF)|_U$. For a compact subset $K\subset U$, the dual-sections adjunction gives a natural isomorphism

\[
R\Gamma_K(U;Q)
\simeq
R\operatorname{Hom}_k\bigl(R\Gamma(K;F_U|_K),k\bigr).
\tag{DD4}
\]

This formula holds for an arbitrary bounded $F_U$. It does not assert that the stalk of $Q$ is the algebraic dual of the stalk of $F_U$. One derivation of DD4 is to use the closed embedding $i_K:K\hookrightarrow U$: exceptional internal-Hom adjunction identifies $i_K^!Q$ with the Verdier dual on $K$ of $i_K^{-1}F_U$, and the proper-support adjunction identifies its global sections with the dual of compact-support cohomology on $K$. Since $K$ is compact, that cohomology is ordinary cohomology. This also describes the actual maps in DD4.

In particular, for compact $B\subset K\subset U$, duality takes restriction

\[
r:R\Gamma(K;F_U|_K)\longrightarrow R\Gamma(B;F_U|_B)
\tag{DD5}
\]

to the natural extension of supports

\[
R\Gamma_B(U;Q)\longrightarrow R\Gamma_K(U;Q).
\tag{DD6}
\]

Both complexes in DD5 are bounded. For example, $i_{K*}i_K^{-1}F_U$ is a bounded sheaf complex on the manifold $U$, and its ordinary global sections are those on $K$; the course's uniform finite-dimensional cohomology bound applies. This avoids imposing any manifold or regularity hypothesis on the compact subset itself.

If DD6 is an isomorphism, the bounded cone $N=\operatorname{Cone}(r)$ has $R\operatorname{Hom}_k(N,k)=0$, because derived Hom is exact as a contravariant functor of triangulated categories. DD1 then gives $N=0$. We shall prove DD6 for the precise family of caps in the microsupport criterion.

### SH02-MSA-DUAL-CAP-GEOMETRY — One uniform family of compact caps

Suppose $\xi_0\ne0$ and

\[
(x_0,-\xi_0)\notin\operatorname{SS}(D_XF).
\tag{DD7}
\]

Trivialize the cotangent bundle on a coordinate domain near $x_0$, viewed as an open set in a vector space $E$. Closedness and conicity of microsupport give an open coordinate neighborhood $U$ and a closed pointed convex cone $D\subset E^*$ such that

\[
-\xi_0\in\operatorname{Int}D,\qquad
D\text{ has nonempty interior},\qquad
\operatorname{SS}(Q)\cap\bigl(U\times(D\setminus\{0\})\bigr)=\varnothing.
\tag{DD8}
\]

To choose $D$, take a sufficiently small closed angular convex cone around the ray $\mathbb R_{>0}(-\xi_0)$ inside the open conic region excluded by DD7, and shrink the base neighborhood. In particular $D$ may be chosen pointed as well as full dimensional.

Use the course's positive-polar convention and put

\[
C=D^\circ
=\{v\in E:\langle v,d\rangle\geq0\text{ for every }d\in D\},
\qquad
\ell(y)=\langle y-x_0,\xi_0\rangle.
\tag{DD9}
\]

The cone $C$ is closed, convex and pointed, and $C^\circ=D$. The fact that $-\xi_0$ is in the interior of $D$ gives

\[
\langle v,\xi_0\rangle<0\quad(v\in C\setminus\{0\}).
\tag{DD10}
\]

More quantitatively, there is $a>0$ such that $-\langle v,\xi_0\rangle\geq a|v|$ for $v\in C$. Take the positive minimum on the compact unit section of $C$; if a nonzero vector gave equality in the pairing with an interior point of $D$, perturb that interior covector slightly in the opposite direction to contradict membership in $D^\circ$.

Choose $h>0$ small and then a neighborhood $V$ of $x_0$ small enough that every set

\[
K_x=(x+C)\cap\{\ell\geq-h\},
\qquad
B_x=(x+C)\cap\{\ell=-h\},
\qquad x\in V,
\tag{DD11}
\]

is compact and contained in $U$. The estimate is explicit: for $y=x+v\in K_x$,

\[
a|v|\leq h+\ell(x).
\tag{DD12}
\]

First choose a ball about $x_0$ with closure in $U$, then make $h$ and the radius of $V$ sufficiently small in DD12. This also proves the uniform containment required by the cap criterion, namely $(V+C)\cap\{\ell\geq-h\}\subset U$. We may arrange $|\ell(x)|<h/2$ on $V$; nothing in the argument depends on an empty-cap convention.

### SH02-MSA-DUAL-CAP-PROOF — Moving the dual support to the base

Fix $x\in V$ and abbreviate $K=K_x$, $B=B_x$. On $U$ form the bounded object

\[
G=R\Gamma_KQ.
\tag{DD13}
\]

Its closed support lies in the compact set $K$. We shall show

\[
R\Gamma_B(U;Q)\xrightarrow{\sim}R\Gamma_K(U;Q).
\tag{DD14}
\]

Consider the open part $Y=U\cap\{\ell>-h\}$. Here imposing $K$ as support is the same as imposing $x+C$, so

\[
G|_Y\simeq
R\mathcal Hom(k_{x+C},Q)|_Y.
\tag{DD15}
\]

The closed-convex-set microsupport bound gives

\[
\operatorname{SS}(k_{x+C})\subset (x+C)\times D.
\tag{DD16}
\]

For clarity, this also follows directly from the supporting-hyperplane formula: a supporting covector at $y\in x+C$ is nonnegative on every vector of $C$, because $y+tv\in x+C$ for all $v\in C$ and $t\geq0$. Thus it belongs to $C^\circ=D$.

By DD8, the microsupports of $k_{x+C}$ and $Q$ have no common nonzero covector in $U$. The precise Hom hypothesis is therefore satisfied, and the Hom estimate applied to DD15 gives, over $Y$,

\[
\operatorname{SS}(G)\subset\operatorname{SS}(Q)-D.
\tag{DD17}
\]

This is used only above the base $B$. No estimate is asserted at the corners on $B$, where the second inequality defining the cap introduces additional directions.

The covector $-d\ell=-\xi_0$ is absent from the right side of DD17. Indeed an equality $-\xi_0=\eta-d$ with $d\in D$ would force

\[
\eta=-\xi_0+d\in\operatorname{Int}D\subset D\setminus\{0\}.
\]

Here addition of a vector of $D$ preserves its interior, and pointedness rules out zero. DD8 excludes such an $\eta$ from $\operatorname{SS}(Q)$. Therefore

\[
(y,-d\ell)\notin\operatorname{SS}(G)\qquad(y\in Y).
\tag{DD18}
\]

We now apply noncharacteristic deformation with every compactness and front condition visible. On the ambient open set $U$ use the increasing family

\[
U_s=U\cap\{\ell>-h+e^{-s}\},\qquad s\in\mathbb R.
\tag{DD19}
\]

It is left continuous in the required sense, $U_s=\bigcup_{r<s}U_r$, and its union is $Y$. The closure of each increment, intersected with the support of $G$, is compact because it is a closed subset of $K\Subset U$. The corrected limiting front at parameter $s$ is contained in the level $\ell=-h+e^{-s}$. For a later parameter $t>s$ that front already lies in $U_t$, so there is no test point outside $U_t$. At $t=s$ the complement is locally the upper support of the test function $-\ell$ through the front point, and DD18 gives exactly the required vanishing. These are the hypotheses of the course's noncharacteristic-deformation theorem with the closure taken before the intersection.

For $s$ sufficiently negative the threshold $-h+e^{-s}$ exceeds the maximum of $\ell$ on the compact set $K$, so $G|_{U_s}=0$. Deformation thus yields

\[
R\Gamma(Y;G)=0.
\tag{DD20}
\]

Finally the localization triangle for the closed set $\{\ell\leq-h\}\cap U$ gives an isomorphism

\[
R\Gamma_{\{\ell\leq-h\}}(U;G)
\xrightarrow{\sim}R\Gamma(U;G).
\tag{DD21}
\]

Composition of closed-support functors identifies its source with $R\Gamma_B(U;Q)$, because $K\cap\{\ell\leq-h\}=B$, and its target with $R\Gamma_K(U;Q)$. Its map is extension of supports. This proves DD14 with the specified morphism.

### SH02-MSA-DUAL-CAP-DETECTION — Returning from the dual test

Apply DD4-DD6 to $B_x\subset K_x$ for every $x\in V$. DD14 is the dual of the restriction

\[
R\Gamma(K_x;F|_{K_x})\longrightarrow R\Gamma(B_x;F|_{B_x}).
\tag{DD22}
\]

Its cone is bounded, so DD1 makes DD22 an isomorphism. The cone $C$, the neighborhood $V$, the constant $h$, strict inequality DD10, and uniform containment DD12 are precisely the data of the finite-cap criterion `SH02-MST-EQUIVALENCE`. That criterion consequently gives

\[
(x_0,\xi_0)\notin\operatorname{SS}(F).
\]

This proves the desired reverse inclusion at every nonzero covector. The algebraic detector was applied to each actual finite-cap cone. We neither passed duality through a filtered limit nor argued that duality detects a stalk of the original support-test system.

At a zero covector, suppose $(x_0,0)\notin\operatorname{SS}(D_XF)$. The zero-section criterion gives a neighborhood $U$ on which $Q=(D_XF)|_U=0$. For every $x\in U$, apply DD4 to the compact singleton $K=\{x\}$:

\[
0=R\Gamma_{\{x\}}(U;Q)
\simeq R\operatorname{Hom}_k(F_x,k).
\]

Since $F_x$ is bounded, DD1 implies $F_x=0$. All cohomology stalks of $F|_U$ vanish, so $F|_U=0$ and $(x_0,0)\notin\operatorname{SS}(F)$. This singleton argument concerns the **costalk** of $Q$, as DD4 explicitly states, not its stalk. It therefore does not invoke the generally false stalk-duality formula.

Together with DD3, this completes DD2 under the exact coefficient hypothesis DD1.

### SH02-MSA-DUAL-FIELDS — Arbitrary vector spaces are detected

Let $k$ be a field. Every short exact sequence of vector spaces splits, including infinite-dimensional ones, so $\operatorname{Hom}_k(-,k)$ is exact. Every nonzero vector space has a nonzero functional: extend a nonzero vector to a basis and send that basis vector to $1$, the others to $0$.

Thus for a bounded complex $M$,

\[
H^nR\operatorname{Hom}_k(M,k)
\simeq\operatorname{Hom}_k(H^{-n}(M),k).
\tag{DD23}
\]

If the derived dual is zero, each right side is zero, and hence every $H^{-n}(M)$ is zero. This proves DD1 for fields with no finite-dimensional restriction. The basis-extension statement uses the usual choice principle implicit in the module theory of the course.

### SH02-MSA-DUAL-INTEGERS — Detecting arbitrary abelian groups

First prove the algebraic module statement

\[
\operatorname{Hom}_{\mathbb Z}(A,\mathbb Z)=0,
\qquad
\operatorname{Ext}^1_{\mathbb Z}(A,\mathbb Z)=0
\quad\Longrightarrow\quad A=0.
\tag{DD24}
\]

We use the standard fact that $\mathbb Z$ has global dimension one. In particular all second Ext groups in the following argument vanish, even for infinitely generated abelian groups.

**First, $A$ is torsion free.** If $N\subset A$ is any subgroup, the long Ext sequence of $0\to N\to A\to A/N\to0$ makes

\[
\operatorname{Ext}^1(A,\mathbb Z)
\longrightarrow\operatorname{Ext}^1(N,\mathbb Z)
\]

surjective, since the next group is $\operatorname{Ext}^2(A/N,\mathbb Z)=0$. A nonzero torsion element would provide $N\simeq\mathbb Z/n$ with $n>1$. Its two-term free resolution gives $\operatorname{Ext}^1(\mathbb Z/n,\mathbb Z)\simeq\mathbb Z/n\ne0$, contradicting the assumed vanishing. The same argument shows that any group with vanishing first Ext against $\mathbb Z$ is torsion free.

**Next, $A$ is divisible.** For $n\geq1$, torsion freeness gives an exact sequence

\[
0\longrightarrow A\xrightarrow{n}A\longrightarrow A/nA\longrightarrow0.
\]

The relevant part of the Hom-Ext sequence is

\[
\operatorname{Hom}(A,\mathbb Z)
\longrightarrow\operatorname{Ext}^1(A/nA,\mathbb Z)
\longrightarrow\operatorname{Ext}^1(A,\mathbb Z).
\]

Both outer groups vanish, so the middle group vanishes. The preceding paragraph makes $A/nA$ torsion free. But it is annihilated by $n$, hence is zero. Multiplication by every positive integer is therefore surjective on $A$.

**A nonzero divisible torsion-free group cannot satisfy DD24.** Such a group has a unique $\mathbb Q$-vector-space structure. If it is nonzero, a vector-space basis gives a direct summand $\mathbb Q$, so $\operatorname{Ext}^1(\mathbb Q,\mathbb Z)$ is a retract of $\operatorname{Ext}^1(A,\mathbb Z)$. It remains to justify, without a finite-generation assumption, that

\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q,\mathbb Z)\ne0.
\tag{DD25}
\]

Here is an explicit witness for that last fact. Let $L=\mathbb Z[1/2]\subset\mathbb Q$. For $n\geq0$ define the integer

\[
a_n=\sum_{0\leq2j<n}2^{2j}.
\]

Then $a_{n+1}\equiv a_n\pmod{2^n}$, so the prescriptions

\[
f(2^{-n})=a_n2^{-n}\pmod{\mathbb Z}
\]

define a homomorphism $f:L\to\mathbb Q/\mathbb Z$. It has no lift to a homomorphism $L\to\mathbb Q$. Indeed such a lift is multiplication by some $r\in\mathbb Q$; since $f(1)=0$, it would have $r\in\mathbb Z$. Its values at $2^{-n}$ would then require $r\equiv a_n\pmod{2^n}$ for every $n$. At $n=2m$ the formula $a_{2m}=(4^m-1)/3$ would make the integer $3r+1$ divisible by $4^m$ for every $m$. Hence $3r+1=0$, impossible for an integer $r$.

In the long exact sequence induced by $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$, the connecting map sends this nonliftable $f$ to a nonzero element of $\operatorname{Ext}^1(L,\mathbb Z)$; its kernel is exactly the liftable maps. Finally, the long Ext sequence for $0\to L\to\mathbb Q\to\mathbb Q/L\to0$ gives a surjection

\[
\operatorname{Ext}^1(\mathbb Q,\mathbb Z)
\twoheadrightarrow\operatorname{Ext}^1(L,\mathbb Z),
\]

because $\operatorname{Ext}^2(\mathbb Q/L,\mathbb Z)=0$. This proves DD25, and completes the proof of DD24.

To pass from arbitrary groups to bounded complexes, use the hyper-Ext spectral sequence. Global dimension one leaves only its columns $0$ and $1$; since $M$ is bounded it converges with finite filtrations and has no possible nonzero higher differential. It yields, for every $n$, an exact sequence

\[
0\longrightarrow\operatorname{Ext}^1_{\mathbb Z}(H^{1-n}(M),\mathbb Z)
\longrightarrow H^nR\operatorname{Hom}_{\mathbb Z}(M,\mathbb Z)
\longrightarrow\operatorname{Hom}_{\mathbb Z}(H^{-n}(M),\mathbb Z)
\longrightarrow0.
\tag{DD26}
\]

If the derived dual vanishes, all Hom and all first Ext groups of each cohomology group vanish. Apply DD24 to every $H^r(M)$. Thus all cohomology groups are zero, proving DD1 for $\mathbb Z$ and arbitrary bounded complexes of arbitrary abelian groups.

### SH02-MSA-DUAL-CONSTRUCTIBLE — The separate biduality hypothesis

If $F$ has the precise cohomologically constructible local data required by `SH02-CB-BIDUALITY`, that theorem gives the canonical isomorphism $F\simeq D_XD_XF$. Applying DD3 to both $F$ and $D_XF$ gives

\[
\operatorname{SS}(D_XF)\subset\operatorname{SS}(F)^a,
\qquad
\operatorname{SS}(F)
=\operatorname{SS}(D_XD_XF)
\subset\operatorname{SS}(D_XF)^a.
\]

This proves DD2 in the other source case. It is a separate sufficient condition; it was not used in the finite-cap argument or in the coefficient tests and must not be added to their hypotheses.

## SH02-MSA-PRODUCT-LIMIT — Simultaneous normal limits retain correlations

Take $k=\mathbb Q$, $B=\{0\}\cup\{1/n:n\geq1\}\subset\mathbb R$, and $F=k_B$. There is a natural specialization comparison

$$
\nu_{\{0\}}F\boxtimes\nu_{\{0\}}F
\longrightarrow\nu_{\{(0,0)\}}(F\boxtimes F).
\tag{MSA14}
$$

It is not an isomorphism. In fact the two sides are not even isomorphic as sheaf complexes near the positive diagonal in the normal plane.

**The one-variable limit.** Write $x=tv$, with $t>0$, for the deformation coordinates. Near a positive normal vector $v_0$, the inverse image of $B$ is the disjoint union of the curves $tv=1/n$. On a rectangle

$$
v\in(v_0-\epsilon,v_0+\epsilon),\qquad 0<t<\delta,
\qquad0<\epsilon<v_0,
$$

every curve that meets the rectangle does so in a connected interval, and all sufficiently large $n$ occur. The curves form a locally finite family away from $t=0$. Sections of the pulled-back sheaf are arbitrary families of constants on those intervals, and there is no positive cohomology: the domain is a disjoint union of intervals, their constant sheaves are acyclic, and products of module surjections are surjective. Shrinking $\delta$ removes finitely many indices. Consequently the specialization is locally constant on the positive normal ray, concentrated in degree zero there, with fibre

$$
A=\left(\prod_{n\geq1}\mathbb Q\right)
\big/\left(\bigoplus_{n\geq1}\mathbb Q\right).
\tag{MSA15}
$$

The same description on overlapping positive rectangles uses the same tail restrictions, hence proves local constancy as a sheaf, not only equality of stalk dimensions. On the negative ray it is zero. We do not need its zero-vector gluing for the argument. Since coefficients are a field, the left side of MSA14 is a degree-zero locally constant sheaf with fibre $A\otimes A$ on the positive quadrant.

**A section seen by the simultaneous limit.** In two variables the deformation coordinates are $(x,y)=(tv,tw)$ with one common positive parameter $t$. Over the positive quadrant, the inverse image of $B\times B$ is the disjoint union of curves

$$
tv=1/n,\qquad tw=1/m,
\qquad\frac{w}{v}=\frac{n}{m}.
\tag{MSA16}
$$

On this inverse image define a section to be $1$ on the curves with $n=m$ and $0$ on every other curve. It is a valid section: near a point with $t>0$, both original coordinates are positive, so only finitely many points of $B\times B$ occur locally and each is isolated. Thus each curve has a neighborhood disjoint from all the others. The section defines, by ordinary direct image and restriction to $t=0$, a section $e$ of $\mathcal H^0$ of the right side of MSA14 near $(v,w)=(1,1)$.

Every neighborhood of $(1,1,0)$ contains a tail of the curves with $n=m$, so the germ of $e$ at $(1,1)$ is nonzero. At a positive vector with $w/v\ne1$, a sufficiently small angular neighborhood avoids those curves, and the germ of $e$ is zero. Hence $e$ is a nonzero local section supported on the diagonal within an open positive quadrant. A locally constant sheaf on a connected open ball has no such section: a section that vanishes on a nonempty open subset vanishes throughout that ball. This proves that the cohomology sheaf on the right is not locally constant at $(1,1)$ and therefore cannot be isomorphic to the left side.

One can also see the failure of the specified map. A local element of $A\otimes A$ is represented by a finite sum of separated arrays $a_n b_m$. If its image were $e$, then on some angular neighborhood of ratio $1$ and after deleting finitely many indices that finite-rank array would equal the matrix $\delta_{nm}$. Let the number of separated summands be $r$. Choose $r+1$ consecutive, sufficiently large indices so that every ratio of two chosen indices belongs to that angular neighborhood. Restriction to this square block would identify a matrix of rank at most $r$ with the identity matrix of rank $r+1$, a contradiction. Thus the comparison is not surjective on this degree-zero stalk.

**An additional model.** Replace $1/n$ by $3^{-n}$. The separate positive limits still have fibre MSA15, but in the simultaneous deformation the possible positive ratios are powers of $3$. Near $(1,2)$ no such ratio occurs, so the simultaneous specialization is zero while the exterior product has the nonzero fibre $A\otimes A$. This example isolates the role of a common scaling parameter without requiring densely accumulating ratios. The preceding proof covers the reciprocal sequence as well.

## SH02-MSA-PROBLEMS — Further constructions with worked solutions

**Problem: move the limit obstruction to any higher degree.** For an integer $m\geq1$, replace the circle in MSA23 by the unit $m$-sphere and work in $\mathbb R^{m+1}\times\mathbb R_t$. Compute the new degree of the support obstruction at the vertex. Explain why the same ordinary-limit identification needs modification for $m=0$.

*Solution.* Set $C_m=\{(x,t):|x|=t>0\}$ and $Z_{m,n}=\{(x,t):|x|=t\geq1/n\}$. The local smooth-boundary computation is unchanged: all stage covectors satisfy $\tau\geq-|\eta|$. For $m\geq1$ the punctured cone is connected, so the ordinary limit is $k_{\overline C_m}$. A punctured vertex neighborhood retracts to $S^m$, and the cone is contractible. The relative complex is therefore $k[-(m+1)]$. Its class survives shrinking and detects $-dt$, now in degree $m+1$. The proper cylinder resolution has the compensating cohomology sheaf $\mathcal H^m(Rj_*k_{C_m})=k_{\{0\}}$. When $m=0$ the punctured cone has two components. The stalk of $j_*k_{C_0}$ at the vertex is $k\oplus k$, while that of $k_{\overline C_0}$ is $k$. Thus the equality of these two ordinary sheaves used in the counterexample is false in that case; connectivity was a real hypothesis in its proof.

**Problem: separate two angular windows.** Let $\Omega_1,\Omega_2\subset V^*$ be disjoint open conic sets. Express the cutoff for their union in terms of the two cutoffs, and specify the resulting morphism to $F$.

*Solution.* Since the two sets are open and closed in their union, extension by zero gives $k_{\Omega_1\cup\Omega_2}=k_{\Omega_1}\oplus k_{\Omega_2}$. The inverse Fourier functor and proper-support convolution are additive. Hence

$$
Q_{\Omega_1\cup\Omega_2}F
\simeq Q_{\Omega_1}F\oplus Q_{\Omega_2}F.
$$

The map to $F$ is the sum of the two maps induced by $k_{\Omega_i}\to k_{V^*}$; its signs are fixed by these actual inclusions and the common Fourier normalization. MSA6 places the microsupport in the closure of the union and makes this sum an isomorphism microlocally on either open window. The windows need not be convex. For infinitely many disjoint windows one must additionally invoke the filtered-colimit and boundedness arguments, rather than replace a finite sum by an unexamined infinite operation.

**Problem: classify the compactly supported objects up to this homotopy on a vector space.** Let $A,B\in D^b(k_E)$ have compact closed support. Show that they are homotopic if and only if $R\Gamma(E;A)$ and $R\Gamma(E;B)$ are isomorphic as derived $k$-module objects.

*Solution.* Necessity is `SH02-MSA-HOMOTOPY-COHOMOLOGY`, which proves the isomorphism of derived objects as well as of their individual cohomology groups. Conversely the dilation construction gives a homotopy from each object to the skyscraper with its derived cohomology as coefficient. A chosen isomorphism between those coefficient complexes gives an isomorphism of the two skyscrapers. Reflexivity, symmetry, and the derived gluing construction concatenate these families. Compact support on the vector space and the finite-dimensional cohomological bound keep every coefficient object bounded. An isomorphism of graded cohomology modules alone is insufficient over a general ring, because it need not preserve the extension classes of a complex.

**Problem: distinguish the two zero statements for a shrinking system.** Explain why $\varinjlim H^q(U;K)=0$ for all $q$ does not prove MSA17.

*Solution.* In the compact accumulation-space example of `SH02-CB-SYSTEMS` and the later worked example in [cohomological biduality](../../sheaf-proof-readings/SH02-cohomological-biduality.html), the transition maps delete finitely many coordinates from a direct sum over an infinite tail. Every individual vector is eventually deleted, so the ordinary colimit is zero, but no transition map is zero. The corresponding formal ind-object is therefore nonzero. MSA19 supplies a zero intermediate complex through which an entire restriction morphism factors; this extra uniform factorization is exactly what the ind-object statement requires.

## SH02-MSA-RESEARCH — Questions suggested by these constructions

The cutoff for an arbitrary angular open set allows local microlocal arguments to be assembled from several convex windows while keeping one specified morphism to the original object. The inverse-limit example asks for conditions on a system in the enhanced derived category that retain this control; conditions only on its ordinary degree-zero limit can discard the term carrying a cancellation. The specialization example asks a different question: when does a pair of independently varying normal parameters give the same data as one simultaneous parameter? Constructibility and geometric control of the relevant deformation correspondence are substantive hypotheses to investigate, rather than consequences of having a tensor comparison map.

The homotopy relation remembers the full derived cohomology of a compactly supported object on a vector space. Its collapsing family supplies an explicit test for proposed homotopy invariants: any such invariant must be unchanged when the spatial geometry is replaced by its cohomology object at a point. The Euler/Gysin vanishing result, by contrast, concerns a specified morphism of sheaves and can be checked by a section of a conormal complement without constructing a homotopy of supports.

## SH02-MSA-CORRESPONDENCE — What the shared examples and imports establish

The cone-resolution construction proves the cohomology-sheaf failure phenomenon independently of the [other cone-projector construction](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-PROBLEMS). The finite truncation argument MSA4 is the exact bounded statement already proved in `SH02-MST-FORMAL`; it is repeated here only to explain the contrast in one place. The closed- and open-convex microsupport formulas are supplied by `SH02-SUB-CONVEX-SETS` in [subset microsupport](../../sheaf-proof-readings/SH02-subset-microsupport.html#SH02-SUB-CONVEX-SETS). The conic neighborhood support test belongs to `SH02-MO-CONIC-NEIGHBORHOOD-TEST` in [microsupport operations](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-CONIC-NEIGHBORHOOD-TEST), including its explicit counterexample to the weaker single-direction formulation.

Every application discussed here now has a proof or an exact link to its owning theorem, relative to the declared prerequisites. The two corrected source formulations remain explicit correspondence findings.
