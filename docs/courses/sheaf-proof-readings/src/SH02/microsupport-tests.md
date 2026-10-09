# SH02-MST — Detecting and removing directional obstructions

Local unit: `SH02-MST`. The directional test equivalence, propagation theorem, and cone cutoff theorem are proved below relative to the explicitly stated sheaf-theoretic imports.

Throughout, $k$ is a commutative ring of finite global dimension, $X$ is a finite-dimensional real manifold countable at infinity, and $F\in D^b(k_X)$. No constructibility or finiteness of stalks is assumed. The notation $\operatorname{supp}(F)$ means the closure of the union of the supports of its cohomology sheaves. A closed convex cone contains its vertex $0$; it is **pointed** when it contains no nonzero vector together with its negative. For a cone $C\subset E$ put

\[
C^\circ=\{\xi\in E^*: \langle v,\xi\rangle\geq0\text{ for every }v\in C\},
\qquad C^{\circ a}=-C^\circ.
\]

The antipodal operation and the polar operation have different meanings. In particular, $C^{\circ a}$ consists of the functionals nonpositive on $C$.

The source for the three-test mechanism is [Kashiwara and Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Theorem 3.1.1, printed pp. 49–53; the cone-projector criterion is Proposition 3.2.2, printed pp. 58–60. The bounded-complex and coefficient conventions agree with [Schapira, *A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §2.2 and Theorem 2.6. We retain the explicit cap, proper-support, and neighborhood arguments below, so these references identify the mathematics being developed rather than replace a proof.

## SH02-MST-TEST — The local experiment

Local identifier: `SH02-MST-TEST`.

Let $x\in X$, and let $f$ be real valued and $C^1$ on a neighborhood of $x$. Subtracting its value at $x$ does not change its differential. Define its support test by

\[
\mathcal T_{x,f}(F)=
\bigl(R\Gamma_{\{f\geq f(x)\}}F\bigr)_x.
\tag{T1}
\]

This is a complex of $k$-modules, not just a group of sections. If $j:\{f<f(x)\}\hookrightarrow X$ denotes the local open inclusion, the localization triangle identifies it as

\[
\mathcal T_{x,f}(F)\longrightarrow F_x
\longrightarrow (Rj_*j^{-1}F)_x\xrightarrow{+1}.
\tag{T2}
\]

Thus its vanishing says that restriction towards the smaller values of $f$ loses neither sections nor their higher obstructions. It does not assert that either term in the middle is zero.

**Definition.** A covector $p$ is absent from $\operatorname{SS}(F)$ if there is an open neighborhood $W$ of $p$ in $T^*X$ such that

\[
\mathcal T_{x,f}(F)=0
\quad\text{whenever }(x,df_x)\in W.
\tag{T3}
\]

Every $C^1$ function defined near the testing point is allowed. The neighborhood is chosen before the function and the point. Testing only the single differential at $p$, or using only linear functions without a neighborhood argument, is not this definition.

For a morphism $u:F\to G$ and a subset $A\subset T^*X$, say that $u$ is a **microlocal isomorphism on $A$** when $\operatorname{SS}(\operatorname{Cone}(u))\cap A=\varnothing$. Different cones are isomorphic, so the definition is independent of that choice. Applying (T1) to a triangle proves the equivalent formulation: near each point of $A$, all the support-test morphisms $\mathcal T_{x,f}(u)$ are isomorphisms. The neighborhood can depend on the point of $A$.

## SH02-MST-IMPORTS — Exact dependencies of the geometric proofs

Local identifier: `SH02-MST-IMPORTS`.

The proofs use the following typed results. Their proofs belong to the foundational sheaf course or the directional-topology unit; stating them here does not close their independent verification.

1. **Localization and continuity.** Derived sections with support satisfy localization triangles, excision, and the composition rule for intersections of closed supports. For a compact subset of a locally compact Hausdorff space, cohomology of the restriction is the filtered colimit of cohomology over open neighborhoods. For an increasing sequence of open sets, an eventually constant system of cohomology groups computes the cohomology of the union. These assertions apply to bounded-below complexes, with no finite-rank assumption.
2. **Noncharacteristic deformation.** Suppose $Z$ is Hausdorff, $A\in D^+(\mathbb Z_Z)$, and $U_t$ is an increasing family of open sets indexed by $\mathbb R$. Assume $U_t=\bigcup_{s<t}U_s$, assume $\overline{U_t\setminus U_s}\cap\operatorname{supp}(A)$ is compact for $s<t$, and put
   \[
   B_s=\bigcap_{t>s}\overline{U_t\setminus U_s}.
   \]
   Assume $\bigl(R\Gamma_{Z\setminus U_t}A\bigr)_z=0$ for $s\leq t$ and $z\in B_s\setminus U_t$. Then restriction $R\Gamma(\bigcup_tU_t;A)\to R\Gamma(U_s;A)$ is an isomorphism for every $s$. An open parameter interval can be reparametrized monotonically by $\mathbb R$. Notice the closures, the support intersection in compactness, and the condition at points outside $U_t$.
3. **Directional projector.** For $q_C:E\to E_C$, where $E_C$ has the ordinary open sets stable under addition by $C$, put $P_C=q_C^{-1}Rq_{C*}$. The inverse image is fully faithful on the appropriate derived image, the unit $Rq_{C*}q_C^{-1}\simeq\mathrm{id}$ is an isomorphism, and the counit $P_C A\to A$ satisfies the usual adjunction identities. Localization by a locally closed subset of $E_C$ commutes with $Rq_{C*}$ in the manner proved in the directional-topology unit. The projector is bounded on bounded complexes in the present finite-dimensional setting.
4. **Proper cone fibers.** If a kernel correspondence is proper on the closed support of its coefficient complex over the base, its stalk is computed by derived sections on its fiber. We use this only after proving properness. An arbitrary ordinary direct image cannot be replaced by cohomology of a closed fiber.

The first two results now have an explicit limited prerequisite bridge: compact-neighborhood continuity, the open-union comparison, and the full deformation theorem. Their stated hypotheses above match those proofs, including arbitrary Hausdorff spaces and bounded-below complexes. The directional-topology construction is treated in [Directional neighborhoods and a sheaf projector](../../SH02-cone-topology.html). In the deformation import, the closure is taken before the intersection. This is the front used in Astérisque Theorem 1.4.3, printed pp. 30–31, including the endpoint condition. The cited internal proof supplies the stated version; the external theorem alone is not a prerequisite proof. All local identifications below use the natural restriction or adjunction maps supplied by these imports.

## SH02-MST-EQUIVALENCE — Three ways of removing one covector

Local identifier: `SH02-MST-EQUIVALENCE`.

Work in an open subset $X$ of a finite-dimensional vector space $E$, and fix $(x_0,\xi_0)\in T^*X$. The following conditions are equivalent.

- **Test vanishing:** (T3) holds at $(x_0,\xi_0)$.
- **A local representative killed by a cone:** there are a pointed closed convex cone $C$ and $A\in D^b(k_E)$ such that
  \[
  \langle v,\xi_0\rangle<0\quad(v\in C\setminus\{0\}),
  \qquad Rq_{C*}A=0,
  \tag{T4}
  \]
  and $A$ agrees with $F$ on a neighborhood of $x_0$.
- **A compact cap has no extra cohomology:** there are such a cone $C$, a neighborhood $V$ of $x_0$, and $h>0$ such that, for
  \[
  H=\{x:\langle x-x_0,\xi_0\rangle\geq-h\},
  \qquad L=\{x:\langle x-x_0,\xi_0\rangle=-h\},
  \tag{T5}
  \]
  one has $H\cap(V+C)\subset X$ and, for every $x\in V$, restriction is an isomorphism
  \[
  R\Gamma((x+C)\cap H;F)
  \xrightarrow{\sim}R\Gamma((x+C)\cap L;F).
  \tag{T6}
  \]

Moreover one obtains the same test condition by using $C^r$ functions for any integer $r\geq1$, smooth functions, or real analytic functions in analytic coordinates. In the analytic case this is a statement about an analytic manifold and its analytic charts, not an assertion that arbitrary smooth manifolds carry a chosen analytic atlas.

We prove the three implications in an order that separates the sheaf operations from the moving-boundary calculation.

### SH02-MST-CONE-TO-TEST — A cone-acyclic representative passes every $C^1$ test

Local identifier: `SH02-MST-CONE-TO-TEST`.

Suppose (T4) holds. For $\xi_0\ne0$, compactness of the unit section of $C$ implies that strict negativity persists for covectors in an open neighborhood of $\xi_0$. Hence it suffices to consider $f$ with $df_x\in\operatorname{Int}(C^{\circ a})$.

On a small convex coordinate ball, the derivative of $f$ in every unit direction of $C$ is bounded above by a negative constant. Therefore $f$ decreases along every cone segment contained in the ball. The local open set $\{f<f(x)\}$ is the germ of a $C$-open set $O$: take a smaller negative sublevel patch and add $C$. Near $x$, a point reached from that patch by a cone segment is still in the negative sublevel set; the segment stays in the original ball until it reaches the smaller ball. Conversely each nearby negative point already belongs to the patch.

We also need a cofinality statement. If $N_\epsilon=B_\epsilon(x)+C$, then $N_\epsilon\setminus O$ is contained in a ball of radius $K\epsilon$ about $x$, for a fixed $K$ and small $\epsilon$. Indeed $|f(y)-f(x)|\leq M\epsilon$ at a starting point $y\in B_\epsilon(x)$, while advancing a distance $(M/c+1)\epsilon$ along $C$ decreases $f$ by more than this error. That point enters the negative patch and every later point of the cone ray is in $O$. This argument uses a uniform negative directional bound $-c$ and compactness of the unit directions. Thus the differences $N_\epsilon\setminus O$ form a neighborhood basis at $x$ in the ordinary closed complement of $O$.

Localization on $E_C$, followed by this cofinality, identifies the support-test stalk with the corresponding stalk of

\[
q_C^{-1}R\Gamma_{E_C\setminus O}(Rq_{C*}A).
\tag{T7}
\]

One can check (T7) by writing the localization triangle on each $N_\epsilon$ and passing to the filtered colimit. No closed-fiber base-change assertion is involved. Its value is zero by (T4). Since $A$ and $F$ agree near $x_0$, they pass the same local tests there.

### SH02-MST-CAP-TO-CONE — Cap vanishing produces a cone-acyclic representative

Local identifier: `SH02-MST-CAP-TO-CONE`.

Assume (T6), and first extend $F$ by zero from $X$ to $E$. Let $B=F_{H\setminus L}$, with this extension understood. The triangle

\[
B\longrightarrow F_H\longrightarrow F_L\xrightarrow{+1}
\tag{T8}
\]

shows that $R\Gamma(x+C;B)=0$ for $x\in V$. This inference uses the natural restriction map in (T6).

Here is why these closed-cone sections compute the relevant projector stalks. On the kernel support, $y-x\in C$ and $y\in H$. Strict negativity in (T4) gives a constant $c>0$ with

\[
\langle y-x,\xi_0\rangle\leq-c\lVert y-x\rVert.
\]

When $x$ ranges in a compact set, the inequality $y\in H$ therefore bounds $y-x$. The kernel support over that compact set is closed and bounded. Its projection is proper. Proper base change and the directional kernel formula give

\[
(P_C B)_x\simeq R\Gamma(x+C;B)=0\qquad(x\in V).
\tag{T9}
\]

Shrink $V$ into the interior of $H$. Choose $C$-open sets $O_0\subset O_1$ so that $x_0\in\operatorname{Int}(O_1\setminus O_0)$ and $\overline{O_1\setminus O_0}\subset V$. Such a pair exists for every pointed $C$: enlarge it slightly to a full-dimensional pointed cone, take a small translate of that cone, and truncate its head by a strictly decreasing linear functional. Its head is bounded by the same inequality used above; shrinking both the aperture patch and the truncation keeps its closure in $V$.

Set

\[
A=R\Gamma_{O_1\setminus O_0}B.
\tag{T10}
\]

Near $x_0$, the locally closed support set has interior and $B=F$, so $A=F$. Directional localization, idempotence, and (T9) give

\[
Rq_{C*}A
\simeq R\Gamma_{O_1\setminus O_0}Rq_{C*}B
\simeq Rq_{C*}R\Gamma_{O_1\setminus O_0}P_CB=0.
\tag{T11}
\]

This proves (T4). Boundedness follows from the finite-dimensional cohomological bounds in the declared imports.

The support estimate before (T9) is indispensable in comparing this step with the proof of Astérisque Theorem 3.1.1. The closed support of the restricted coefficient complex is contained in the closed halfspace, even though the complex itself is extended by zero from its open part. Intersecting that closed support with the closed cone relation gives a closed set. Over any compact set of vertices the strict polar estimate bounds the cone displacement, so this whole support is compact over that set. Proper base change therefore computes the natural projector stalk and identifies its counit with restriction; an abstract isomorphism of the two cap cohomology groups would not establish (T11).

### SH02-MST-ANALYTIC-CAP — An analytic family that pushes a cap onto its base

Local identifier: `SH02-MST-ANALYTIC-CAP`.

It remains to obtain (T6) from analytic tests. This is the implication that prevents a hidden regularity restriction. Translate and linearly change coordinates so that $x_0=0$, $\xi_0=dx_1$, and write $x=(x_1,x')$. After shrinking the covector neighborhood, choose $h>0$ and $\delta>0$ so small that every cap used below lies in the coordinate domain and every positive multiple of a covector

\[
dx_1+\eta\cdot dx',\qquad |\eta|\leq\delta,
\tag{T12}
\]

based in that cap lies in the conic enlargement of the vanishing neighborhood. Multiplying a test function by a positive constant leaves its support set unchanged, so testing in that enlargement is legitimate. Put

\[
C=\{(v_1,v'):v_1\leq-\delta|v'|\}.
\tag{T13}
\]

For a point $a=(a_1,a')$ just above the base plane $L=\{x_1=-h\}$, set $R=h+a_1>0$, $q=\delta^2|x'-a'|^2$, and for $t>0$ define

\[
g_t(q)=q+(R^2-q)\tanh\!\left(\frac{R^2-q}{t}\right),
\qquad
D_t(a)=\{x:x_1<a_1-\sqrt{g_t(q)}\}.
\tag{T14}
\]

These are auxiliary domains for the proof; they do not redefine the cone projector. The function under the square root is positive: it is at least $q$, and at $q=0$ it is strictly positive. Thus each boundary is a real analytic graph. The domains increase continuously with $t$, are contained in $D(a)=a+\operatorname{Int}C$, and their union is $D(a)$.

On $L$, the inequality defining $D_t(a)$ is equivalent to $q<R^2$. This follows because for $q<R^2$ the added term in (T14) lies strictly between $0$ and $R^2-q$, whereas for $q\geq R^2$ one has $g_t(q)\geq q\geq R^2$. Consequently

\[
D_t(a)\cap L=D(a)\cap L.
\tag{T15}
\]

As $t\downarrow0$, the closures of the portions $D_t(a)\cap H$ decrease to the base disk $\overline{D(a)}\cap L$. The reason is that $g_t(q)\to R^2$ when $q\leq R^2$; no point with $x_1>-h$ remains. All these portions lie in the fixed compact closed cap $\overline{D(a)}\cap H$.

We check the conormals quantitatively. For $0\leq q\leq R^2$, put $u=(R^2-q)/t$. Then

\[
g_t'(q)=1-\tanh u-u\operatorname{sech}^2u,
\qquad |g_t'(q)|\leq1.
\tag{T16}
\]

For the inequality, both subtracted terms are nonnegative, $\tanh u\leq1$, and $u\operatorname{sech}^2u\leq1$; the last bound follows from $\cosh^2u\geq u$ for $u\geq0$. Hence the sum lies in $[0,2]$. The derivative of $\sqrt{g_t(\delta^2|x'-a'|^2)}$ has norm at most $\delta\sqrt{q/g_t(q)}\leq\delta$. The outward conormal is therefore of the form (T12), and the analytic support test vanishes at every moving boundary point in $H$.

To apply deformation without imposing behavior below the base, use

\[
\widetilde D_t(a)=D_t(a)\cup(D(a)\setminus H),
\qquad A=Rj_*j^{-1}F,
\tag{T17}
\]

where $j:D(a)\hookrightarrow E$. The closures of all differences in this family lie in the compact closed cap. At a moving boundary point inside $D(a)$, $A=F$ and (T16) supplies the required test. The only additional limiting-front points lie on $\partial D(a)\cap L$. At such a point both $D_t(a)$ and $D(a)$ have analytic smooth boundaries with outward conormal of type (T12). Thus

\[
\bigl(R\Gamma_{E\setminus D_t(a)}F\bigr)_y=0,
\qquad
\bigl(R\Gamma_{E\setminus D(a)}F\bigr)_y=0.
\tag{T18}
\]

Since $D_t(a)\subset D(a)$, the support-composition rule and the localization triangle for $j$ imply $\bigl(R\Gamma_{E\setminus D_t(a)}A\bigr)_y=0$. Inside $D(a)$, the closed set $D(a)\setminus D_t(a)$ separates into its portions above and below $L$: its intersection with $L$ is empty by (T15). Each portion is both open and closed in that support set. Derived sections supported in the upper portion are consequently a direct summand of those supported in the full set. After $Rj_*$ this proves the required vanishing for $E\setminus\widetilde D_t(a)$ at the rim as well. These checks cover every point in the limiting front of (T17).

This is the rim step in the analytic-cap mechanism of Astérisque Theorem 3.1.1, proof of the implication from analytic tests to caps, printed pp. 51–52. The family (T14) is a different analytic barrier: (T15) fixes its intersection with the base, and (T16) controls its conormals. The split into upper and lower support pieces occurs inside the open cone, where both pieces are relatively closed and disjoint. For two such support pieces the sections-with-support functor splits as a finite direct sum, also after deriving. The upper summand is the support functor for the complemented auxiliary domain. This proves the rim vanishing after direct image and prevents a boundary point on the base from being silently omitted.

Noncharacteristic deformation now gives

\[
R\Gamma(D(a);F)\xrightarrow{\sim}
R\Gamma(\widetilde D_t(a);F).
\tag{T19}
\]

The closure in $D(a)$ of $D(a)\setminus H$ is contained in $\widetilde D_t(a)$, again by (T15). Excision for the extension by zero from $D(a)\setminus H$, followed by its localization triangle, converts (T19) to

\[
R\Gamma(D(a)\cap H;F|_H)
\xrightarrow{\sim}
R\Gamma(D_t(a)\cap H;F|_H).
\tag{T20}
\]

Finally put $a=x+\rho e_1$ with $\rho>0$. The sets $D(a)\cap H$ form a cofinal system of relative open neighborhoods of the compact set $(x+C)\cap H$. As $\rho\downarrow0$ and then $t\downarrow0$, the sets $D_t(a)\cap H$ form a cofinal neighborhood system of $(x+C)\cap L$. To check the latter assertion, work in a fixed compact larger cap. Every point outside any prescribed neighborhood of the base disk is excluded for sufficiently small $\rho$ and $t$ by (T14); a finite subcover of that compact complement gives uniform choices. These latter sets need not be monotone in $\rho$ at fixed $t$. Choose recursively a nested cofinal diagonal $(\rho_n,t_n)$, shrinking both domains in (T20) inside their predecessors. The compact-complement argument supplies every such choice. Compact-neighborhood continuity applied to the resulting compatible restriction maps (T20) proves (T6).

This proves analytic-test vanishing implies the cap condition. The cap condition implies all $C^1$ tests by the preceding two arguments. Since analytic functions are among the $C^r$ functions, which in turn are among the $C^1$ functions, all the asserted test classes are equivalent.

If $\xi_0=0$, the argument is simpler and must be handled separately. A neighborhood of $(x_0,0)$ contains $(x,0)$ for all $x$ near $x_0$; the constant function tests give $F_x=0$ there. Thus $F$ vanishes near $x_0$. In (T4), strict negativity at $0$ forces $C=\{0\}$, and $Rq_{C*}A=A$; the zero representative works exactly when $F$ vanishes locally. In (T5), $H=E$ and $L=\varnothing$, so (T6) has the same meaning. This completes the equivalence, including the zero covector.

## SH02-MST-FORMAL — Consequences that do not require a propagation estimate

Local identifier: `SH02-MST-FORMAL`.

The complement of $\operatorname{SS}(F)$ is open by its definition. Multiplication of test functions by positive constants shows that it is invariant under positive scaling of covectors; hence $\operatorname{SS}(F)$ is a closed conic subset of $T^*X$. The zero-covector argument above gives

\[
\operatorname{SS}(F)\cap T_X^*X=\operatorname{supp}(F),
\qquad
\operatorname{SS}(F[m])=\operatorname{SS}(F).
\tag{T21}
\]

The first equality identifies the zero section with $X$. The closure in the definition of support is essential: a sheaf may have zero stalk at a boundary point while remaining nonzero in every neighborhood of it.

For a distinguished triangle $F_1\to F_2\to F_3\xrightarrow{+1}$, apply each exact test functor and use that two zero terms force the third to be zero. For distinct $i,j,k$ this proves

\[
\operatorname{SS}(F_i)\subset
\operatorname{SS}(F_j)\cup\operatorname{SS}(F_k).
\tag{T22}
\]

Equivalently, the portions of either of two microsupports outside the other must lie in the third. Finite induction on the truncation triangles of a bounded complex gives

\[
\operatorname{SS}(F)\subset
\bigcup_j\operatorname{SS}(\mathcal H^jF).
\tag{T23}
\]

The reverse inclusion can fail; an explicit example appears below. Truncation is therefore not a microlocally exact operation in the sense suggested by reversing (T23).

The forgetful functor from sheaves of $k$-modules to abelian sheaves commutes with the tests and detects their vanishing. One justification uses flabby resolutions: forgetting scalars preserves exactness and flabbiness, and flabby sheaves are acyclic for the support functors appearing in the localization triangles. Therefore microsupport is unchanged on forgetting the coefficient ring. This statement changes the category in which the same complex is viewed; it does not identify the microsupports of unrelated complexes obtained by a nonfaithful change of scalars.

Finally, the test definition uses only $C^1$ coordinate changes. The chain rule carries a test function and its covector to the corresponding test in another chart, while the support set and its local cohomology are topologically unchanged. Microsupport consequently depends only on the $C^1$ structure. The analytic equivalence does not add an analytic-constructibility assumption.

## SH02-MST-CUTOFF-FORWARD — What a cone projector already proves

Local identifier: `SH02-MST-CUTOFF-FORWARD`.

Let $X=Y\times E$, with $Y$ a manifold, and let $C\subset E$ be any closed convex cone. Lines are now permitted. Write $q_C:X\to Y\times E_C$ and $P_C=q_C^{-1}Rq_{C*}$. The full cutoff assertion is

\[
P_CF\xrightarrow{\sim}F
\quad\Longleftrightarrow\quad
\operatorname{SS}(F)\subset T^*Y\times(E\times C^{\circ a}).
\tag{T24}
\]

We first prove the forward implication and the microlocal accuracy of the counit. These parts do not use the propagation theorem whose localization is treated separately below.

Work locally on $Y$ and replace $C$ by $\{0\}\times C$ in the product vector space. If $\xi\notin C^{\circ a}$, choose $v\in C$ with $\langle v,\xi\rangle>0$. There is a full-dimensional pointed cone $D$ centered tightly around $-v$, with $\xi\in\operatorname{Int}D^{\circ a}$. Its aperture can be chosen so that $D+C$ is the entire vector space: a cone neighborhood of $-v$, translated by sufficiently large positive multiples of $v$, contains any prescribed vector. For any nonempty convex $D$-open set $O$, this gives $O+C=E$.

If $F=P_CF$, the directional section theorem gives

\[
R\Gamma(O;F)\simeq R\Gamma(O+C;F)=R\Gamma(E;F).
\tag{T25}
\]

The isomorphisms respect restriction. Choose nested convex $D$-open sets whose difference has $x$ in its interior and is locally bounded near $x$, as in (T10). The localization triangle and (T25), applied on a convex directional basis, show that $Rq_{D*}$ kills the corresponding localized representative of $F$. The implication `SH02-MST-CONE-TO-TEST` excludes $(x,\xi)$ from its microsupport. This proves the forward implication of (T24).

For an arbitrary $F$, let $B$ be the cone of the counit $P_CF\to F$. The adjunction identities and idempotence give $Rq_{C*}B=0$. If $C$ is pointed, `SH02-MST-CONE-TO-TEST` therefore gives

\[
\operatorname{SS}(B)\cap
\bigl(T^*Y\times(E\times\operatorname{Int}C^{\circ a})\bigr)=\varnothing.
\tag{T26}
\]

If $C$ contains a line, $C^{\circ a}$ lies in the hyperplane annihilating that line and has empty interior in $E^*$. Then (T26) is a statement on the empty set. It does not supply an artificial nonempty cutoff window. At the other extreme $C=\{0\}$ gives $P_C=\mathrm{id}$ and the counit is an isomorphism everywhere.

## SH02-MST-CONVEX-GEOMETRY — Extending cohomology across convex domains

Local identifier: `SH02-MST-CONVEX-GEOMETRY`.

We give the convex geometry behind the converse of (T24) separately. It is also useful when checking which support differences are legitimate in a directional topology.

Let $V\subset E$ be nonempty, open, and convex, and fix $x_0\in E$. For this paragraph translate $x_0$ to zero and put

\[
A=\bigcup_{t>0}tV,\qquad C=\overline A,\qquad
B_1=\bigcup_{0<t\leq1}tV,\qquad
B_3=\bigcup_{t>1}tV.
\tag{T30}
\]

The set $B_1$ is the interior of the convex hull of $V\cup\{0\}$. It also equals the union with $0<t<1$: openness lets one extend any vector of $V$ slightly further while staying in $V$. Adjoining the point $0$ adds no further interior point unless $0\in V$ already; separating $0$ from the open convex set $V$ proves this when $0\notin V$.

The open convex cone $A$ satisfies $A+C=A$. Moreover $B_3+C=B_3$. To see the latter, first observe $B_3+A\subset B_3$ by writing a sum $tu+sv$ with $t>1,s>0$ as $(t+s)$ times a convex combination in $V$. If $c\in C$, approximate it by points of $A$. A small ball about $b\in B_3$ remains in $B_3$; adding the approximating points shows that a ball about $b+c$ lies in $\overline{B_3}$. An open convex set equals the interior of its closure, so $b+c\in B_3$. The same argument applies to $A$. Both are consequently $C$-open.

One has

\[
A=B_1\cup B_3,\qquad B_1\cap B_3=V.
\tag{T31}
\]

For the intersection, if $z=tu=sv$ with $u,v\in V$ and $0<t\leq1<s$, then

\[
z=\frac{(s-1)t}{s-t}u+\frac{(1-t)s}{s-t}v.
\tag{T32}
\]

The coefficients are nonnegative and sum to one. Conversely, openness shows that every point of $V$ is $sv'$ for some $s>1$ and $v'\in V$. Translate back and write $V_i=x_0+B_i$ for $i=1,3$, and $V_2=x_0+A$. We have proved

\[
V_1\setminus V=V_2\setminus V_3,
\tag{T33}
\]

where $V_2,V_3$ are $C$-open and $V_1=\operatorname{Int}\operatorname{conv}(V\cup\{x_0\})$. Thus the difference on the left is locally closed for the $C$-topology. This conclusion does not require $C$ to be pointed. If $x_0\in\overline V$, the difference is empty. For the empty open set the statement is interpreted directly; in dimension zero the sole nonempty case has no extension to perform.

### SH02-MST-CUTOFF-CONVERSE — Recovering a cone projector from support tests

Assume now

\[
\operatorname{SS}(F)\subset E\times C_0^{\circ a}
\tag{T34}
\]

for an arbitrary closed convex cone $C_0$. We prove the converse cutoff assertion relative to the propagation theorem stated in `SH02-MST-PROPAGATION` below. In particular, this argument does not supply an independent proof of that theorem.

Fix a nonempty bounded open convex set $O$, and put $Q=O+C_0$. It is enough to prove

\[
R\Gamma(Q;F)\xrightarrow{\sim}R\Gamma(O;F).
\tag{T35}
\]

We first prove this with $Q$ replaced by any bounded open convex $W$ with $O\subset W\subset Q$. Consider the open convex sets $V$ between $O$ and $W$ whose restriction to $O$ is a cohomological isomorphism. This collection has upper bounds for every chain. Indeed second countability extracts a countable subfamily covering the union of a chain, and finite maxima turn it into an increasing sequence. For a bounded-below injective resolution $I$ of $F$, the degreewise restriction maps of $\Gamma(V_n;I)$ are surjective because injective sheaves are flabby. The difference map on products gives an exact sequence of complexes

\[
0\longrightarrow\Gamma(\bigcup_nV_n;I)
\longrightarrow\prod_n\Gamma(V_n;I)
\xrightarrow{1-\mathrm{shift}}\prod_n\Gamma(V_n;I)
\longrightarrow0.
\tag{T36}
\]

All cohomology transition maps identify with the identity of $H^*(O;F)$. The derived inverse-limit term vanishes, and (T36) proves the required assertion for the union. This is an application of the Mittag-Leffler argument, not an assertion that arbitrary inverse limits are exact. Zorn's lemma now gives a maximal $V$.

If $V\ne W$, choose $x_0\in W\setminus\overline V$. Such a point exists because $V=\operatorname{Int}\overline V$. Form $C=\overline{\operatorname{pos}(V-x_0)}$ and the sets $V_1,V_2,V_3$ from (T30)–(T33). In this step $V$ is bounded. If $y$ is a closest point of $\overline V$ to $x_0$, put $a=y-x_0$, $d=|a|>0$, and $M=\max_{u\in\overline V}|u-x_0|$. Convexity and the minimizing property give

\[
\langle a,u-x_0\rangle\geq d^2\quad(u\in\overline V),
\qquad
\langle a,z\rangle\geq\frac{d^2}{M}|z|\quad(z\in C).
\tag{T37}
\]

Thus $C$ is pointed. The use of bounded $V$ matters: the cone generated from an unbounded open halfspace and an exterior point can be a closed halfspace and contain lines. Distance from that unbounded set alone would not prove (T37).

Write $x_0=\omega+g$ with $\omega\in O$ and $g\in C_0$. Necessarily $g\ne0$. Then $v=\omega-x_0=-g$ lies in the interior of $C$ because $\omega\in V$. Every nonzero $\xi\in C^{\circ a}$ is strictly negative on $v$, whereas $\xi\in C_0^{\circ a}$ would give $\xi(v)=-\xi(g)\geq0$. Hence

\[
C^{\circ a}\cap C_0^{\circ a}=\{0\}.
\tag{T38}
\]

The zero covector is not in $\operatorname{Int}C^{\circ a}$ here. Equations (T34) and (T38) supply the microsupport avoidance required for propagation with the auxiliary cone $C$.

The compactness condition is also exact. Since $V_1\subset W$ is bounded and $V_2\setminus V_3=V_1\setminus V$, for every $x\in V_2$ the set

\[
(x+C)\setminus V_3
\tag{T39}
\]

is bounded. It is closed because $C$ is closed and $V_3$ is open. It is therefore compact. Apply propagation with the two $C$-open sets $V_3\subset V_2$, and with the avoidance region equal to all of $E$. We obtain $R\Gamma(V_2;F)\simeq R\Gamma(V_3;F)$. The open cover $V_2=V_1\cup V_3$, whose intersection is $V$, gives by Mayer-Vietoris

\[
R\Gamma(V_1;F)\xrightarrow{\sim}R\Gamma(V;F).
\tag{T40}
\]

But $V_1$ strictly contains $V$ and lies in $W$: short segments from $x_0$ toward $V$ lie in $V_1\setminus\overline V$. This contradicts maximality. Thus $V=W$.

Exhaust $Q$ by $W_n=Q\cap B_n$, where the increasing open balls contain $\overline O$. The bounded argument gives compatible restriction isomorphisms to $R\Gamma(O;F)$, and the same exact sequence (T36) proves (T35). Finally the sets $O+C_0$, as bounded convex ordinary neighborhoods $O$ of $x$ shrink, are cofinal among directional neighborhoods. The counit on the stalk at $x$ is the filtered colimit of the restriction maps (T35). Exactness of filtered colimits therefore proves $P_{C_0}F\simeq F$. For $Y\times E$, apply this argument locally in affine coordinates on $Y$ with the cone $\{0\}\times C_0$. No pointedness assumption on $C_0$ has entered the argument.

## SH02-MST-PROPAGATION — Propagation with only interior conormals excluded

Local identifier: `SH02-MST-PROPAGATION`.

Let $X\subset E$ be open, let $U\subset X$ be open, and let $C\subset E$ be a pointed closed convex cone. Let $O_0\subset O_1$ be $C$-open subsets of $E$. Assume

\[
\operatorname{SS}(F)\cap(U\times\operatorname{Int}C^{\circ a})=\varnothing,
\qquad O_1\setminus O_0\subset U,
\tag{T41}
\]

and assume that

\[
(x+C)\setminus O_0\text{ is compact for every }x\in O_1.
\tag{T42}
\]

Then restriction is an isomorphism

\[
R\Gamma(O_1\cap X;F)\xrightarrow{\sim}R\Gamma(O_0\cap X;F).
\tag{T43}
\]

More precisely, with $B=R\Gamma_{X\setminus O_0}F$, the directional derived direct image of $B$ vanishes over $O_1$. Concretely, for each $x\in O_1$,

\[
\underset{V\ni x\text{ $C$-open}}{\operatorname{colim}}
R\Gamma(V\cap X;B)=0.
\tag{T44}
\]

This formulation also covers points of $O_1$ outside $X$ without confusing $X_C$ with $E_C$. The cone need not have interior. The difference $O_1\setminus O_0$ need not be relatively compact. Compactness is exactly (T42).

For comparison, Astérisque Proposition 3.2.1, printed pp. 55–57, proves a halfspace case by distance neighborhoods and movement along an interior ray. Theorem 3.8 of the 2016 review states the general compact-truncated-cone form without an interior assumption, but does not supply its proof there. The following argument supplies the needed steps: rounded boundaries keep an interior polar term, movement uses any nonzero cone vector, and compact localization reduces a general directional open set to the halfspace case. The zero cone is treated separately at the end.

### SH02-MST-HALFSPACE — Rounded neighborhoods of a truncated cone

Local identifier: `SH02-MST-HALFSPACE`.

First suppose $C\ne\{0\}$ and $O_0=\{\ell<0\}$, where $\ell(y)=\langle y,\xi\rangle-c$ and $\xi\in\operatorname{Int}C^{\circ a}$. Put $H=\{\ell\geq0\}$. Fix a Euclidean norm. There is $a>0$ such that

\[
-\langle v,\xi\rangle\geq a|v|\qquad(v\in C).
\tag{T45}
\]

For $x\in O_1$, let $d_x(y)$ be the distance to $x+C$. Away from $x+C$ this distance is $C^1$ and its differential belongs to $C^{\circ a}$. Indeed, if $p$ is the nearest point of $x+C$, the minimizing inequality for $p+\epsilon v$, $v\in C$, gives $\langle y-p,v\rangle\leq0$, and the derivative is $(y-p)/|y-p|$.

For $t>0$ set

\[
N_t(x)=\{\ell<0\}\ \cup\
\{d_x<2t, (d_x-t)_+\ell<(2t-d_x)^2\},
\qquad r_+=\max(r,0).
\tag{T46}
\]

These open sets contain the entire tube $\{d_x\leq t\}$ and the lower halfspace. On the curved part their boundary is $\ell=b_t(d_x)$, where

\[
b_t(r)=\frac{(2t-r)^2}{r-t}\quad(t<r<2t),
\qquad b_t(r)=0\quad(r\geq2t).
\tag{T47}
\]

The pieces join $C^1$ at $2t$, with derivative zero; the height tends to infinity as $r\downarrow t$, so there is no finite boundary there. The derivative $b_t'(r)$ is nonpositive. Thus every boundary point has outward defining differential

\[
d(\ell-b_t(d_x))=\xi-b_t'(d_x)\,dd_x
\in\operatorname{Int}C^{\circ a}.
\tag{T48}
\]

Here an interior point of a convex cone plus any point of the cone remains interior. Its value cannot be zero, since $C$ contains a nonzero vector. This retained $\xi$ term is why no vanishing on the boundary of the polar cone is required.

The sets $N_t(x)$ increase and are left-continuous in $t$. On the curved part, increasing $t$ increases $b_t(r)$ at fixed $r$; on the tube and flat portions the assertion follows directly from (T46). Every moving-front point for parameter $s$ lies in $N_t(x)$ for $t>s$.

For $r\geq0$ put

\[
K_x(r)=\{y:\ell(y)\geq0, d_x(y)\leq r\}.
\tag{T49}
\]

This set is compact. Write $y=x+v+e$ with $v\in C$ and $|e|\leq r$. From $\ell(y)\geq0$ and (T45) one gets $a|v|\leq\ell(x)+|\xi|r$. Thus $y$ is bounded; the defining conditions are closed. The compact sets $K_x(r)$ decrease to $(x+C)\cap H$, which lies in $U\cap O_1$. Consequently, for sufficiently small $\epsilon>0$,

\[
K_x(2\epsilon)\Subset U\cap O_1.
\tag{T50}
\]

Only this supported moving part is required to be relatively compact. The whole $N_t(x)$ contains the lower halfspace and generally has no such property.

Apply the deformation import to $B=R\Gamma_{H\cap X}F$ and $N_t(x)\cap X$, $0<t<\epsilon$. Its supported increments are closed subsets of (T50). The corrected limiting front

\[
\bigcap_{r>s}\overline{N_r(x)\setminus N_s(x)}
\tag{T51}
\]

lies on $\partial N_s(x)$ in $H\cap\{d_x\leq2s\}$. At $t>s$ these front points already lie in $N_t(x)$; at $t=s$, the support condition reduces to the test (T48), since $X\setminus N_s(x)\subset H$ and hence

\[
R\Gamma_{X\setminus N_s(x)}B
\simeq R\Gamma_{X\setminus N_s(x)}F.
\tag{T52}
\]

Every requirement of deformation, including the endpoint $t=s$, is satisfied. We obtain compatible restriction isomorphisms for all $0<t<\epsilon$. The sets $N_t(x)\cap H$ are cofinal neighborhoods in $H$ of the compact set $(x+C)\cap H$: they contain it and lie in $K_x(2t)$. Compact-neighborhood continuity therefore gives

\[
R\Gamma(N_\epsilon(x)\cap X;B)
\xrightarrow{\sim}R\Gamma((x+C)\cap X;B).
\tag{T53}
\]

The right-hand complex is supported on the compact truncated cone, so this limit has no contribution from infinity.

### SH02-MST-RAY-PROPAGATION — Passing along a ray, including cones with empty interior

Local identifier: `SH02-MST-RAY-PROPAGATION`.

Choose any $v\in C\setminus\{0\}$ and write $x_b=x+bv$ for $b\geq0$. These points remain in $O_1$. For large $b$, $\ell(x_b)<0$ and $x_b+C$ misses $H$, so

\[
Q_b=R\Gamma((x_b+C)\cap X;B)=0.
\tag{T54}
\]

We show that this vanishing is locally constant in $b$. Near a fixed parameter, choose $\epsilon$ so that $K_{x_b}(6\epsilon)\Subset U\cap O_1$. Distances to two translates of the cone differ by at most the distance between their vertices. If $|b-b'|\,|v|<\epsilon$, all the preceding compactness checks apply at either center up to parameter $2\epsilon$.

There is also a useful quantitative inclusion. If $|d-d'|\leq\delta$ and $t'\geq t+\delta$, then $N_t(d)\subset N_{t'}(d')$. In the curved part, $d'-t'\leq d-t$ while $2t'-d'\geq2t-d$, so the inequality in (T46) persists; the tube and negative-halfspace cases are immediate. Hence

\[
x_{b'}+C\subset N_\epsilon(x_b)\subset N_{2\epsilon}(x_{b'}),
\tag{T55}
\]

and likewise with $b,b'$ exchanged. The restriction isomorphism (T53) at $b'$ factors through $R\Gamma(N_\epsilon(x_b)\cap X;B)$, which is zero if $Q_b=0$. Thus $Q_b=0$ implies $Q_{b'}=0$, and the converse follows symmetrically.

The factorization just used is a statement about the actual restriction maps. When the middle complex vanishes, their composite is the zero morphism; (T53) says the same composite is an isomorphism. Composing with its inverse makes the identity of the endpoint complex zero, so that endpoint is itself a zero object. This justifies the inference in the derived category without a choice of cohomology generators. The zero set in $[0,\infty)$ is open and closed, and is nonempty by (T54). Therefore $Q_0=0$.

No vector in $\operatorname{Int}C$ was chosen. In particular this argument applies to a ray in a higher-dimensional vector space.

The directional neighborhoods $(x+B_\delta)+C$ are cofinal at $x$. Their intersections with $H$ are cofinal neighborhoods of the same compact truncated cone, by the estimate (T49). Taking the filtered limit in (T53) therefore proves (T44) for a lower halfspace $O_0$. This is stronger than a version that additionally excludes every nonzero covector of $C^{\circ a}$; that stronger hypothesis is unnecessary for the rounded fronts (T46).

### SH02-MST-LOCAL-PROPAGATION — Compact localization without enlarging the cone

Local identifier: `SH02-MST-LOCAL-PROPAGATION`.

We now allow arbitrary $O_0$ satisfying (T41)–(T42). For $x\in O_1\setminus O_0$ and any prescribed directional neighborhood $A\subset O_1$, there is a smaller one of the form

\[
V=(x+B_\delta)+C\subset A,
\qquad \overline{V\setminus O_0}\Subset U.
\tag{T56}
\]

Here is the compactness proof. By (T42), all $x+v$ with $v\in C$ and $|v|\geq R$ lie in $O_0$ for a sufficiently large $R$. The compact sphere section $\{x+v:v\in C,|v|=R\}$ has a uniform ball radius $\delta_1$ contained in $O_0$. Every longer cone vector splits into its length-$R$ part and a further vector in $C$. Invariance of $O_0$ under $C$ therefore puts $x+v+B_{\delta_1}$ in $O_0$ for all $|v|\geq R$. Thus $V\setminus O_0$ is uniformly bounded for $\delta\leq\delta_1$. Any limit of points of its closure as $\delta\downarrow0$ lies in the compact set $(x+C)\setminus O_0\subset U$. It follows that the closure is eventually contained in $U$. A further shrink puts the starting ball in $A$, giving (T56).

Fix such a $V$ and let

\[
D=V\setminus O_0,
\qquad G=R\mathcal Hom(k_D,F).
\tag{T57}
\]

The locally closed set $D$ has compact closure in $U$. Consequently $G$ has compact support in $U$.

Indeed, on the open complement of the closure of the locally closed set, its extension-by-zero constant sheaf restricts to zero. Restriction to an open set commutes with derived sheaf Hom, so the derived Hom complex also vanishes there. Its closed support is therefore contained in that compact closure. This proves exactly the support condition used in the final deformation, without assuming that a derived Hom has the same stalkwise support as its first argument. Its natural global section complex is

\[
R\Gamma(X;G)\simeq
\operatorname{fib}\bigl(R\Gamma(V\cap X;F)
\longrightarrow R\Gamma(V\cap O_0\cap X;F)\bigr).
\tag{T58}
\]

Choose $\xi\in\operatorname{Int}C^{\circ a}$, and put $H_c=\{\langle -,\xi\rangle\geq c\}$. We claim

\[
\bigl(R\Gamma_{H_c\cap X}G\bigr)_z=0
\quad\text{for }\langle z,\xi\rangle=c.
\tag{T59}
\]

Only $z\in U$ matters. Choose a $C$-open neighborhood $W$ of $z$ with $W\cap H_c$ relatively compact in $U$. For example $W=(z+B_\delta)+C$ works: if $y=z+b+v\in H_c$, then (T45) gives $a|v|\leq|\xi|\delta$, and therefore $|y-z|\leq(1+|\xi|/a)\delta$.

Apply the halfspace result to $P_c=\{\langle -,\xi\rangle<c\}$ and $P_c\cup W$. Their difference is $W\cap H_c\subset U$, and every relevant truncated cone is compact by (T45). Thus the directional image of $B_c=R\Gamma_{H_c\cap X}F$ vanishes on $W$.

Tensor-Hom adjunction and the closed-support composition rule give

\[
R\Gamma_{H_c\cap X}G\simeq R\mathcal Hom(k_D,B_c).
\tag{T60}
\]

For any $C$-open $W'\subset W$, its derived sections are the fiber of

\[
R\Gamma(W'\cap V\cap X;B_c)
\longrightarrow R\Gamma(W'\cap V\cap O_0\cap X;B_c).
\tag{T61}
\]

Both terms are zero: before intersecting with $X$, their domains are $C$-open subsets of the region where the directional image of $B_c$ vanishes. The sets $W'\cap H_c$, for directional neighborhoods $W'$ of $z$, form a cofinal basis of ordinary neighborhoods of $z$ in $H_c$, by the quantitative estimate used to choose $W$. Since the object in (T60) is supported on $H_c$, its ordinary stalk is the filtered limit of these zero section complexes. This proves (T59). The argument passes from the directional topology to an ordinary stalk by a proved neighborhood comparison; it does not use nonproper closed base change.

Finally apply deformation to the compactly supported $G$ and the increasing halfspace opens $\{\langle -,\xi\rangle<t\}\cap X$. Their supported increments are compact, their limiting fronts are the level hyperplanes, and (T59) is exactly the required test. Their union is $X$. For a parameter below the minimum of $\langle -,\xi\rangle$ on $\operatorname{supp}(G)$, their section complex is zero. Deformation therefore gives $R\Gamma(X;G)=0$.

By (T58), $R\Gamma(V\cap X;B)=0$. Such $V$ are cofinal at every point of $O_1\setminus O_0$ by (T56); at points of $O_0$ the object $B$ already vanishes on a directional neighborhood. This proves (T44). Taking derived sections in the directional topology gives $R\Gamma(O_1\cap X;B)=0$, and its localization triangle proves (T43).

If $C=\{0\}$, its negative polar is all of $E^*$, including the zero covectors. Equation (T41) forces $F|_U=0$ by (T21). The conclusion follows immediately. This also deals with the zero-dimensional ambient space. Replacing (T41) by avoidance of only the nonzero covectors would not justify this exceptional case.

The proof establishes both the propagation theorem used in `SH02-MST-CUTOFF-CONVERSE` and its halfspace case. Together with that convex-extension argument, it completes (T24) at the stated generality, relative to the declared foundational imports.

## SH02-MST-PROBLEMS — Examples and problems with solutions

Local identifier: `SH02-MST-PROBLEMS`.

For the sheaf examples in this section, assume $k\ne0$. The preceding theorems and the purely geometric exercises retain the standing coefficient convention.

**A boundary stalk is not the zero-section criterion.** Let $j:(0,\infty)\hookrightarrow\mathbb R$ and $F=j_!k$. Its stalk at $0$ is zero, but $F$ is nonzero in every neighborhood of $0$. Hence $(0,0)\in\operatorname{SS}(F)$ by (T21). The point is the uniform neighborhood in (T3). Testing only $F_0$ misses it.

**Reversing a support test reverses its direction.** On $\mathbb R$, let $G=k_{[0,\infty)}$. At $0$, the test $f(x)=x$ has $\mathcal T_{0,f}(G)=k$: the restriction to $x<0$ is zero. For $f(x)=-x$, the map in (T2) is $k\to k$ and is the identity, so the test vanishes. On a small interval, the same calculation applies to every function with strictly negative derivative. Thus the positive covector is present and the negative covector is absent. This directly checks the sign in $C^{\circ a}$ for a cone of decreasing directions.

**Cohomology sheaves can restore an excluded covector.** Work in $E=\mathbb R^2$ with coordinates $(u,v)$, let $S$ be the unit circle, and take

\[
C=\{(a,b): b\leq-|a|\},\qquad G=k_S,
\qquad F=\operatorname{Cone}(P_CG\to G).
\tag{T62}
\]

The proper-support condition for the cone kernel holds because $S$ is compact. Its fiber at $x$ is $S\cap(x+C)$. A proper closed subset of the circle cut out by the two linear inequalities has no first cohomology, while the whole circle has first cohomology $k$. The whole circle is contained in $x+C$ exactly when

\[
x\in A=\{(u,v):v\geq\sqrt2+|u|\}.
\tag{T63}
\]

Indeed the two inequalities require $v-u\geq\max_S(v'-u')=\sqrt2$ and $v+u\geq\max_S(v'+u')=\sqrt2$. Restricting the global first cohomology class of the circle to these fibers identifies $\mathcal H^1(P_CG)$ with $k_A$. Evaluation $\mathcal H^0(P_CG)\to G$ is stalkwise surjective: at a point of $S$, the constant section on the fiber evaluates to $1$. The long exact cohomology sequence of (T62) therefore gives $\mathcal H^0F\simeq k_A$.

On the other hand, $Rq_{C*}F=0$. Hence $\operatorname{SS}(F)$ misses every covector in $E\times\operatorname{Int}C^{\circ a}$. At $x=(0,\sqrt2)$ the covector $dv$ lies in that interior, while the test $f(u,v)=v$ on $k_A$ has nonzero local cohomology at $x$, since the support of $k_A$ lies in $\{v\geq\sqrt2\}$. Thus

\[
(x,dv)\in\operatorname{SS}(\mathcal H^0F)
\setminus\operatorname{SS}(F).
\tag{T64}
\]

This example uses ordinary bounded complexes and works over every nonzero coefficient ring in the standing class.

**Problem: why must the cap cone be pointed?** Suppose $\xi$ is strictly negative on every nonzero vector of a cone $C$. Show that $C$ contains no line, and that $(x+C)\cap\{\langle y,\xi\rangle\geq-h\}$ is compact.

*Solution.* A line would contain $w$ and $-w$, contradicting strict negativity. On the compact unit section of $C$, $-\langle -,\xi\rangle$ has a positive minimum $c$. The displayed cap therefore satisfies $c\lVert y-x\rVert\leq h+\langle x,\xi\rangle$ and is closed. If the right side is negative it is empty; otherwise it is closed and bounded. This argument also explains why compactness is uniform for $x$ in a compact set.

**Problem: distinguish a line from the zero cone.** Compute the interior of $C^{\circ a}$ when $C$ is a nonzero linear subspace and when $C=\{0\}$.

*Solution.* In the first case $C^{\circ a}=C^\perp$, a proper linear subspace of $E^*$, whose ambient interior is empty. For the zero cone it is all of $E^*$. A relative interior in $C^\perp$ cannot be substituted into (T26).

**Problem: propagate across an unbounded difference.** In $\mathbb R^2$, take $C=\{(0,-t):t\geq0\}$, $O_0=\{v<0\}$, and $O_1=\{v<2\}$. Verify (T42), although $O_1\setminus O_0$ is unbounded, and state exactly which covectors must be absent over that difference.

*Solution.* A translated downward ray meets $O_1\setminus O_0$ in either the empty set or a compact vertical segment. The negative polar consists of covectors $\alpha\,du+\beta\,dv$ with $\beta\geq0$, and its ambient interior is $\beta>0$. Thus absence of all such covectors over an open neighborhood of the strip permits the restriction from $O_1$ to $O_0$. Neither a field hypothesis nor compactness of the whole horizontal strip is needed.

**Problem: identify the two compactness mechanisms.** Explain why compactness of each truncated cone in (T42) is insufficient by itself to justify every neighborhood limit used in the proof.

*Solution.* A compact fiber does not make an ordinary direct image satisfy closed base change. The halfspace proof instead obtains a uniform bound on the neighboring sets $K_x(r)$, and the general proof establishes the uniform tail estimate in (T56). Those estimates make the indicated open neighborhoods cofinal near compact sets. Once that extra fact is proved, compact-neighborhood continuity applies. The cap-to-projector proof uses a different mechanism: it proves the kernel projection proper on its support before invoking proper base change.

## SH02-MST-RESEARCH — Routes into local microlocal categories

Local identifier: `SH02-MST-RESEARCH`.

The counit $P_CF\to F$ is a useful first cutoff because its error is invisible on the interior of the negative polar. It gives a concrete object and a concrete morphism representing a local microlocal comparison. Stronger cutoffs, and the categories in which such comparisons become actual isomorphisms, belong to Detecting, transporting, and controlling a sheaf in cotangent directions. That unit's independent status must be checked before using its further assertions as an import.

A productive next calculation is to compare two nested cones. The natural maps between their directional topologies supply maps between their projectors; the support-test criterion identifies where the comparison is a microlocal isomorphism. Any claim that the two projectors agree globally must also account for the boundary of the polar cones. Another route is to apply the propagation proof to a family of bounded windows and track the compatible restriction maps. The compactness checks in (T50) and (T56) specify which window limits preserve the conclusion, and expose exactly where a limit escaping to infinity requires additional input.

## SH02-MST-STATUS — Sources and open verification

Local identifier: `SH02-MST-STATUS`.

The source mechanisms have been checked against Astérisque Theorem 1.4.3, Theorem 3.1.1, Proposition 3.2.1, Proposition 3.2.2, and Lemma 3.2.3, together with the 2016 review, Definition 2.3 and Theorems 2.6 and 3.8. The local account retains its explicit analytic barrier, the bounded convex-extension argument, the rounded fronts, the arbitrary-ray propagation, and the circle example. In particular the bounded step before exhaustion in (T35)–(T40) is what makes the pointedness estimate valid; it cannot be replaced by separation from an arbitrary unbounded convex domain.

This independently authored exposition, including its proofs and solved problems, is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The cited sources retain their own terms; no source text or figures are incorporated.

The local proofs are complete relative to the displayed dependency contracts. They include the bounded convex-extension repair, the rounded-front proof of propagation under interior-polar avoidance, and the passage from directional sections to ordinary support stalks. The declared imports are proved in the linked prerequisite lessons. Their coefficient and operation bounds remain in force throughout these arguments.
