# SH02-MSD — Comparing sheaves through local support tests

Local unit: `SH02-MSD`. This supplementary lesson gives the complete formal arguments behind microlocal comparison, finite truncation, forgetting scalars, and changes of $C^1$ coordinates. Original expression is dedicated under CC0 1.0.

## SH02-MSD-CONTRACT — What a comparison has to preserve

Local identifier: `SH02-MSD-CONTRACT`.

Throughout, $k$ is a commutative unital ring of finite global dimension, $X$ is a finite-dimensional real manifold countable at infinity, and sheaf complexes lie in $D^b(k_X)$. Coefficient modules can be arbitrary; no constructibility or finite-rank assumption is imposed. The zero ring is allowed. A cotangent subset $A\subset T^*X$ can be completely arbitrary.

We use the $C^1$ support test and the definition of microsupport from [the local experiment](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-TEST). If $f$ is defined on an open neighborhood $V$ of $x$, write
\[
\mathcal T_{x,f}(K)=
\bigl(R\Gamma_{\{f\geq f(x)\}}(K|_V)\bigr)_x.
\tag{MSD1}
\]
The support is closed in $V$; it need not be closed in $X$. Shrinking $V$ does not change this complex. The definition says that $p\notin\operatorname{SS}(K)$ precisely when one open cotangent neighborhood of $p$ makes every such test vanish. The neighborhood is chosen before the testing point and function.

For a morphism, the relevant question is whether these experiments give isomorphic complexes. This involves all cohomological degrees. We first show that one bounded cone records every failure of a comparison, then prove that the record is independent of the chosen cone.

## SH02-MSD-PREREQUISITES — The exact sheaf facts used below

Local identifier: `SH02-MSD-PREREQUISITES`.

The proofs use the following finite list of statements.

**Stalks.** Module sheaves form an abelian category, exactness is detected on stalks, and a stalk functor is exact. This is [the abelian-sheaf contract](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-ABELIAN), specialized to the constant ring sheaf $k_X$.

**Derived tests and acyclic resolutions.** Module sheaves have enough injectives, and bounded-below injective resolutions compute right derived functors of left exact additive functors. These are [the injective-resolution contract](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-INJECTIVE) and [the derived-functor contract](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-DERIVE). Applied to sheaf sections with closed support and then to a stalk, they make (MSD1) a triangulated functor into $D^+(k)$. Its output need not be asserted bounded. We also use the exact acyclic-resolution form: when the right derived functor is defined, a bounded-below complex of objects acyclic for it computes that functor by termwise application. This is [Leray's acyclicity lemma, Tag 015E](https://stacks.math.columbia.edu/tag/015E); the derived-support functors here are defined by the preceding injective construction.

**Localization and open restriction.** For a closed subset $Z\subset V$ with complementary open inclusion $j$, the functorial triangle is
\[
R\Gamma_Z K\longrightarrow K\longrightarrow Rj_*j^{-1}K\xrightarrow{+1}.
\tag{MSD2}
\]
This is [the localization contract](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-LOCALIZATION). Exact open restriction and the local stalk identifications give independence of the test domain in (MSD1). We also use [exact extension by zero for an open inclusion](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-OPEN-ZERO), whose adjunction with restriction makes the restriction of an injective sheaf to an open set injective.

**Triangles.** Distinguished triangles have long exact cohomology sequences. A commutative square on the first two objects extends to a morphism of distinguished triangles. A quasi-isomorphism becomes invertible in the derived category. These are the derived-category operations used in the cone argument below; that argument explicitly derives the cone-independence and zero-cone criteria it needs.

**Finite truncations.** For the finite-truncation argument alone, use the shift invariance and triangle bound already established in [the formal microsupport properties](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-FORMAL): for a distinguished triangle, the microsupport of any term is contained in the union for the other two terms, and a cohomological shift leaves microsupport unchanged.

**Flabby resolutions.** For the coefficient comparison alone, an injective module sheaf is flabby and a flabby module sheaf has zero higher direct images along any morphism of ringed spaces. These exact statements are [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX) and [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0), collected in [the flabby-sheaf contract](../../sheaf-proof-readings/SH02-open-prerequisites.html#SH02-IMP-FLABBY). The passage from them to sections with support is proved below.

The finite calculations in this lesson require no propagation theorem or cone projector. The equivalence between different regularities of test functions belongs to [the separate test-equivalence theorem](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-EQUIVALENCE).

## SH02-MSD-CONE — One object records the failure of a morphism

Local identifier: `SH02-MSD-CONE`.

Let $u:F\to G$ be a morphism in $D^b(k_X)$. Complete it to a distinguished triangle
\[
F\xrightarrow{u}G\longrightarrow C\longrightarrow F[1].
\tag{MSD3}
\]
The long exact cohomology sequence shows that $C$ is bounded: once the neighboring cohomology sheaves of $F$ and $G$ vanish, the cohomology sheaf of $C$ vanishes as well.

**Definition.** The morphism $u$ is a **microlocal isomorphism on $A$** if
\[
\operatorname{SS}(C)\cap A=\varnothing.
\tag{MSD4}
\]
No openness, closedness, compactness, or conicity condition on $A$ is part of this definition.

**Proposition.** Condition (MSD4) is independent of the distinguished triangle chosen in (MSD3).

**Proof.** Suppose $C'$ is the third object of another distinguished triangle with the same first map $u$. The identity maps of $F$ and $G$ give a commutative square, so the triangle axiom extends them to a map $c:C\to C'$ of third objects.

Fix a point $x$ and an integer $n$. The cohomology stalks give a commutative diagram with exact rows
\[
\begin{array}{ccccc}
\mathcal H^n(F)_x&\longrightarrow\mathcal H^n(G)_x
&\longrightarrow\mathcal H^n(C)_x
&\longrightarrow\mathcal H^{n+1}(F)_x
&\longrightarrow\mathcal H^{n+1}(G)_x\\
\big\Vert&\big\Vert&\downarrow\mathcal H^n(c)_x
&\big\Vert&\big\Vert\\
\mathcal H^n(F)_x&\longrightarrow\mathcal H^n(G)_x
&\longrightarrow\mathcal H^n(C')_x
&\longrightarrow\mathcal H^{n+1}(F)_x
&\longrightarrow\mathcal H^{n+1}(G)_x.
\end{array}
\tag{MSD5}
\]
Here is the short exactness argument for the middle map. An upper middle element that maps to zero below has zero boundary, hence comes from $\mathcal H^n(G)_x$. Its zero lower image means that this lift comes from $\mathcal H^n(F)_x$, so the original element is zero. Conversely, the boundary of a lower middle element lies in the kernel of the last arrow. Lift that boundary through the upper middle term. Subtracting its image from the original lower element leaves an element with zero boundary, which lifts from $\mathcal H^n(G)_x$. Adding the two lifts gives a preimage. Thus $\mathcal H^n(c)_x$ is bijective.

This holds for every $n$ and $x$, so $c$ is a quasi-isomorphism and hence an isomorphism in $D^b(k_X)$. The construction proves that an isomorphism between the cones exists; it does not specify a canonical one. Every support-test functor sends $c$ to an isomorphism. The tests of $C$ and $C'$ consequently vanish on exactly the same cotangent neighborhoods, giving $\operatorname{SS}(C)=\operatorname{SS}(C')$. This proves independence of (MSD4). $\square$

## SH02-MSD-TESTS — Uniform comparison near a cotangent subset

Local identifier: `SH02-MSD-TESTS`.

**Theorem.** For $u:F\to G$ and an arbitrary subset $A\subset T^*X$, the following conditions are equivalent.

1. The morphism $u$ is a microlocal isomorphism on $A$.
2. For every $p\in A$, there is an open neighborhood $W_p$ of $p$ such that $\mathcal T_{x,f}(u)$ is an isomorphism for every point $x$ and every real $C^1$ function $f$ defined near $x$ with $(x,df_x)\in W_p$.
3. There is an open set $W\supset A$ with the same property for every test whose cotangent point belongs to $W$.

**Proof.** Apply the triangulated functor $\mathcal T_{x,f}$ to (MSD3). Its image is a distinguished triangle with first map $\mathcal T_{x,f}(u)$ and third object $\mathcal T_{x,f}(C)$. In a derived category a triangle's first map is invertible exactly when the third object is zero. Indeed, if the third term has zero cohomology, the long exact sequence makes the first map a quasi-isomorphism. Conversely, if the first map is an isomorphism on cohomology in every degree, exactness forces every cohomology group of the third object to vanish. Therefore
\[
\mathcal T_{x,f}(u)\text{ is an isomorphism}
\quad\Longleftrightarrow\quad
\mathcal T_{x,f}(C)=0.
\tag{MSD6}
\]
The equivalence of 1 and 2 is now exactly the $C^1$ definition of $p\notin\operatorname{SS}(C)$, applied at every $p\in A$.

Assuming 2, set $W=\bigcup_{p\in A}W_p$. A cotangent point in $W$ belongs to one $W_p$, and every allowed function at that point passes the required morphism test. This proves 3. Conversely the same $W$ works at each point of $A$, so 3 implies 2. When $A=\varnothing$, take $W=\varnothing$. No finite subcover is used, and points of the zero section are included. $\square$

Subtracting $f(x)$ from a test function changes neither its differential nor the support set in (MSD1). The theorem is therefore unchanged if every test is normalized by $f(x)=0$. The word “every” and the order of the neighborhood quantifiers are essential; one successful test at a single covector does not imply any of the three conditions.

For a class of smoother tests, (MSD6) is still true for each individual function. To replace all $C^1$ tests in the theorem by $C^r$ tests for an integer $r>1$, smooth tests, or analytic tests on an analytic manifold, apply the separate regularity-equivalence theorem to the bounded cone $C$. That supplies exactly the extra implication from vanishing for the restricted class to vanishing for every $C^1$ test. The theorem proved here uses the original $C^1$ definition directly.

## SH02-MSD-TRUNCATION — A finite cohomology bound

Local identifier: `SH02-MSD-TRUNCATION`.

**Proposition.** For every $F\in D^b(k_X)$,
\[
\operatorname{SS}(F)\subset
\bigcup_j\operatorname{SS}(\mathcal H^jF).
\tag{MSD7}
\]

**Proof.** Choose integers $a\leq b$ such that $\mathcal H^jF=0$ outside $a\leq j\leq b$. For $a\leq m\leq b$ there is a canonical truncation triangle
\[
\tau_{\leq m-1}F\longrightarrow\tau_{\leq m}F
\longrightarrow\mathcal H^m(F)[-m]\xrightarrow{+1}.
\tag{MSD8}
\]
Begin with $\tau_{\leq a-1}F=0$. The microsupport triangle bound and shift invariance give, by induction on $m$,
\[
\operatorname{SS}(\tau_{\leq m}F)
\subset\bigcup_{j=a}^{m}\operatorname{SS}(\mathcal H^jF).
\]
At $m=b$ the truncated object is isomorphic to $F$, which proves (MSD7). There are only finitely many nonzero cohomology sheaves. $\square$

This proof provides an upper bound for $\operatorname{SS}(F)$. It does not put the microsupport of every cohomology sheaf inside $\operatorname{SS}(F)$: taking cohomology sheaves can change which directional obstructions cancel in the complex. A separate worked example in [the microsupport problems](../../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-PROBLEMS) investigates that failure using a cone projector.

## SH02-MSD-COEFFICIENTS — Forgetting the coefficient action

Local identifier: `SH02-MSD-COEFFICIENTS`.

Let $U$ forget the $k$ action on a sheaf or complex, leaving its underlying abelian sheaf. Kernels, images, and cokernels have the same underlying groups. Thus $U$ is exact and conservative: it detects zero sheaves and quasi-isomorphisms. In particular it gives a functor $D^b(k_X)\to D^b(\mathbb Z_X)$ without needing to derive $U$.

**Theorem.** There are natural isomorphisms
\[
U\bigl(\mathcal T_{x,f}(F)\bigr)
\simeq\mathcal T_{x,f}(UF),
\qquad
\operatorname{SS}(F)=\operatorname{SS}(UF).
\tag{MSD9}
\]

**Proof.** Underived sections with closed support, restriction, and stalks commute with forgetting the action: each is computed with the same sections or germs and the same zero conditions. We must justify the derived comparison. Forgetting the action need not preserve injective objects, so we use acyclic resolutions.

First let $J$ be a flabby sheaf on an open domain $V$, and let $Z\subset V$ be closed with complementary inclusion $j:V\setminus Z\hookrightarrow V$. The restriction $j^{-1}J$ is flabby because restriction maps between opens of $V\setminus Z$ are restriction maps between opens of $V$. By the flabby direct-image theorem, $R^qj_*j^{-1}J=0$ for $q>0$. Moreover $J\to j_*j^{-1}J$ is surjective on sections over every open subset $O\subset V$, since it is the flabby restriction $J(O)\to J(O\setminus Z)$.

Apply (MSD2) to $J$ in degree zero. Its middle and last derived terms are the sheaves $J$ and $j_*j^{-1}J$, and the map between them is surjective. The first term is therefore represented by the ordinary kernel $\Gamma_ZJ$ in degree zero. This proves that every such flabby sheaf is acyclic for the sheaf-support functor $\Gamma_Z$.

Now choose a bounded-below injective resolution $F|_V\to I^\bullet$ in $k$-module sheaves. Each $I^n$ is flabby. The underlying sheaf $UI^n$ has the same surjective restriction maps, so it too is flabby and therefore $\Gamma_Z$-acyclic in abelian sheaves. Exactness of $U$ makes $UI^\bullet$ a resolution of $UF|_V$. The bounded-below acyclic-resolution theorem then gives
\[
U\bigl(R\Gamma_Z(F|_V)\bigr)
\simeq U(\Gamma_Z I^\bullet)
=\Gamma_Z(UI^\bullet)
\simeq R\Gamma_Z(UF|_V).
\tag{MSD10}
\]
The maps are natural in $F$: a comparison of injective resolutions becomes the same comparison of acyclic resolutions after forgetting scalars. They also commute with restriction to smaller open test domains, since open restriction preserves injectives here by its exact left adjoint, extension by zero.

Take the stalk at $x$ in (MSD10). Stalks are exact and commute with $U$, giving the first assertion in (MSD9). Exact conservativity of $U$ says that this complex is zero exactly when the original $k$-module support test is zero. Thus precisely the same cotangent neighborhoods make every test vanish in the two coefficient categories. The $C^1$ definition proves the second assertion. $\square$

This theorem views the same complex after forgetting its action. It does not claim invariance under tensoring with a different ring, since such a tensor functor can kill a nonzero complex. No nonzero-ring assumption was needed in the proof.

## SH02-MSD-COORDINATES — Transport by a C1 diffeomorphism

Local identifier: `SH02-MSD-COORDINATES`.

Let $h:X\to Y$ be a $C^1$ diffeomorphism and define the induced cotangent homeomorphism by
\[
h^\#:T^*Y\longrightarrow T^*X,\qquad
(y,\eta)\longmapsto
\bigl(h^{-1}(y),(dh_{h^{-1}(y)})^*\eta\bigr).
\tag{MSD11}
\]
The derivatives of $h$ and $h^{-1}$ are continuous, and their differentials are inverse linear maps at corresponding points. This proves both invertibility and continuity in both directions of (MSD11).

**Theorem.** For $G\in D^b(k_Y)$,
\[
\operatorname{SS}(h^{-1}G)=h^\#\operatorname{SS}(G).
\tag{MSD12}
\]

**Proof.** Inverse image along the homeomorphism $h$ is an exact equivalence of sheaf categories. An exact equivalence preserves injectives. It also identifies sheaf sections supported in a subset with sections supported in its inverse image, so applying it to an injective resolution gives the same identification for derived supports and their local stalks.

Let $y=h(x)$ and let $f$ be a $C^1$ test near $y$. Its superlevel set pulls back to the superlevel set of $f\circ h$ at $x$, and the chain rule gives
\[
\mathcal T_{x,f\circ h}(h^{-1}G)
\simeq\mathcal T_{y,f}(G),
\qquad d(f\circ h)_x=(dh_x)^*df_y.
\tag{MSD13}
\]
Every $C^1$ test near $x$ arises in this way by composing it with $h^{-1}$. The homeomorphism (MSD11) transports open cotangent neighborhoods in both directions, and (MSD13) transports all tests in those neighborhoods. A neighborhood passes every test for one complex exactly when its corresponding neighborhood passes every test for the other. This proves (MSD12). $\square$

Applied to overlapping coordinate charts, the theorem shows that microsupport depends only on the $C^1$ structure. Analytic-test replacements, when an analytic structure is available, still use the separate test-regularity theorem.

## SH02-MSD-EXERCISES — Composing comparisons

Local identifier: `SH02-MSD-EXERCISES`.

**Exercise.** Let $F\xrightarrow{u}G\xrightarrow{v}H$ be morphisms of bounded complexes, and let $A\subset T^*X$ be arbitrary. Prove that if any two of $u$, $v$, and $vu$ are microlocal isomorphisms on $A$, then so is the third. Use local support tests to keep track of a single neighborhood on which the two known comparisons work.

**Solution.** Fix $p\in A$. For each of the two given comparisons, the uniform-test theorem supplies an open neighborhood of $p$. Intersect the two neighborhoods. Every support-test functor at a cotangent point of that intersection preserves composition, so its maps satisfy
\[
\mathcal T_{x,f}(vu)=\mathcal T_{x,f}(v)\,\mathcal T_{x,f}(u).
\]
Any two of these three maps are isomorphisms. The elementary two-out-of-three property for isomorphisms makes the third an isomorphism too: compose with the inverse of whichever factor is known when the composite is one of the given maps. The same neighborhood therefore works for every test of the third comparison. Apply the uniform-test theorem at each $p\in A$. The assertion for empty $A$ is vacuous. $\square$

## SH02-MSD-ANTECEDENTS — Scope and antecedents

Local identifier: `SH02-MSD-ANTECEDENTS`.

The micro-support and its equivalent definitions are due to Kashiwara and Schapira; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §3.1. The organization here follows the comparison morphism through its cone, tests, coefficient action and coordinates. The finite-truncation proof uses the earlier microsupport triangle bound; it does not establish a reverse inclusion for cohomology sheaves. The stronger theorem replacing $C^1$ tests by smoother or analytic tests has its own geometric proof and is a separate prerequisite whenever that replacement is used.
