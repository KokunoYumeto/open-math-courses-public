# SH02-NCD — Continuing cohomology through a moving boundary

A moving family of open sets gives restriction maps on cohomology. The theorem below identifies conditions under which those maps are isomorphisms.

The coefficient ring $k$ is unital; it need not be a field, commutative, or of finite global dimension. We use sheaves of left $k$-modules. All complexes in the deformation theorem are bounded below. Their cohomology sheaves may have infinite stalks and need not be constructible. The ambient space will be Hausdorff, with no local compactness, metrizability, manifold, or cohomological-dimension hypothesis.

The mechanism has two parts. Compactness prevents a change from arriving from arbitrarily far away. Vanishing of local cohomology prevents a change at the boundary that remains after taking all sufficiently small advances. Both parts are necessary, as the examples below show.

The source comparison is with Marco Robalo and Pierre Schapira, [*A lemma for microlocal sheaf theory in the infinity-categorical setting*, arXiv:1611.06789v1](https://arxiv.org/abs/1611.06789v1), Section 2. The theorem there treats unbounded complexes. Here the bounded-below proof exposes the compact-neighborhood comparison, the inverse-limit obstruction one degree below, and the interval argument separately. This separation keeps track of the actual restriction maps and explains exactly where the lower bound is used.

## SH02-NCD-FOUNDATIONS — The exact foundational interface

The [open prerequisite contracts](open-prerequisites.md) provide stalkwise exactness, exact inverse image, enough injectives, bounded-below derived functors, flabby acyclicity, and the localization triangle. We use their IDs `SH02-IMP-ABELIAN`, `SH02-IMP-INVERSE`, `SH02-IMP-INJECTIVE`, `SH02-IMP-DERIVE`, `SH02-IMP-FLABBY`, `SH02-IMP-LOCALIZATION`, `SH02-IMP-OPEN-ZERO`, and `SH02-IMP-HYPERCOH`. Although that overview uses commutative coefficients, each listed input is stated for modules on a ringed space, or has the same stalkwise proof for left modules. None of the arguments here uses tensor products.

For a closed subset $C\subset X$, $R\Gamma_C F$ denotes a sheaf complex on $X$. It is distinguished from the module complex $R\Gamma(X;R\Gamma_CF)$. If $j:U\hookrightarrow X$ is open, localization is the natural triangle

\[
R\Gamma_{X\setminus U}F\longrightarrow F
\longrightarrow Rj_*(F|_U)\xrightarrow{+1}.
\tag{N1}
\]

Restriction to an open set preserves injectives: its left adjoint is exact extension by zero. A direct image preserves injectives because inverse image of constant-ring module sheaves is exact. Thus composites of direct images can be calculated with one bounded-below injective resolution. For closed $C,D$, the analogous calculation gives

\[
R\Gamma_C R\Gamma_D F\simeq R\Gamma_{C\cap D}F.
\tag{N2}
\]

Here is a resolution-level justification for this last assertion. The underived support functors compose by intersection. For a closed embedding $i:C\hookrightarrow X$, the sheaf functor $\Gamma_C$ is $i_*i^!$, where $i^!$ is right adjoint to the exact $i_*$. Therefore $i^!$ preserves injectives, and $i_*$ preserves injectives by its exact left adjoint $i^{-1}$. Applying the underived identity to an injective resolution gives (N2). This justification uses $i^!$ only for a closed embedding of sheaf categories; it does not import manifold duality.

If $i:S\hookrightarrow X$ is closed and $F$ has zero cohomology stalks outside $S$, the restriction unit $F\to i_*i^{-1}F$ is an isomorphism, as can be checked on stalks. Closed direct image is exact. Combining it with (N1) identifies the local support tests and all the open-set cohomology of $F$ with those of $i^{-1}F$ on $S$. This permits a reduction to the closed support without imposing extra topology on $X$.

### SH02-NCD-COMPACT-CONTINUITY — A sufficient open theorem and its derived form

We import the exact compact-neighborhood theorem [Stacks, Tag 09V3](https://stacks.math.columbia.edu/tag/09V3). Its hypothesis is that $K\subset X$ is quasi-compact and distinct points of $K$ have disjoint open neighborhoods in $X$. Its conclusion for an abelian sheaf $G$ is

\[
\underset{V\supset K}{\operatorname{colim}}H^p(V;G)
\xrightarrow{\sim}H^p(K;G|_K),
\tag{N3}
\]

where $V$ runs through open neighborhoods, ordered by shrinking. In particular it applies to every compact subset of a Hausdorff space. Local compactness of the ambient space is not one of its hypotheses. For the present source comparison, the statement and proof were checked in the native Stacks chapter at [revision a04446e57ec1](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cohomology.tex), under the label `lemma-cohomology-of-closed`.

For a module sheaf, use its underlying abelian sheaf. A module-injective resolution consists of flabby abelian sheaves, which are acyclic for sections on every open set. Hence forgetting scalars computes the same cohomology; the comparison map retains its $k$-action. This proves (N3) for arbitrary left $k$-modules.

For $A\in D^+(k_X)$, the resulting form is

\[
\underset{V\supset K}{\operatorname{colim}}H^q(V;A)
\xrightarrow{\sim}H^q(K;A|_K).
\tag{N4}
\]

To check the extension, choose a uniform lower bound $N$ on the cohomology sheaves of $A$. Apply the natural hypercohomology spectral sequences to the restrictions to $V$ and to $K$. Formula (N3) identifies their $E_2$ terms after filtered colimit. Filtered colimits of modules are exact, so they commute with the kernels and quotients defining each later page. For a fixed total degree $q$, only $0\le p\le q-N$ contributes. Thus the convergence filtration in that degree is finite, and the comparison of its associated graded pieces proves (N4). This argument explains why bounded below is adequate even when $X$ has no finite cohomological dimension.

## SH02-NCD-OPEN-UNION — Increasing open sets and the degree below

Let $V_0\subset V_1\subset\cdots$ be open in an arbitrary topological space and let $V=\bigcup_nV_n$. For $A\in D^+(k_X)$ there is a natural short exact sequence

\[
0\longrightarrow\operatorname{lim}^{1}_n H^{q-1}(V_n;A)
\longrightarrow H^q(V;A)
\longrightarrow\lim_n H^q(V_n;A)\longrightarrow0.
\tag{N5}
\]

Here, for a tower of modules $(M_n)$ with transitions $r_n:M_{n+1}\to M_n$, $\lim^1 M_n$ means the cokernel of

\[
\prod_nM_n\longrightarrow\prod_nM_n,
\qquad (x_n)\longmapsto(x_n-r_nx_{n+1}).
\tag{N6}
\]

For completeness, resolve $A$ by a bounded-below complex $I$ of injective sheaves and put $C_n=\Gamma(V_n;I)$. Flabbiness makes every transition $C_{n+1}^d\to C_n^d$ surjective. Given $(y_n)$, choose $x_0$ and then recursively choose $x_{n+1}$ mapping to $x_n-y_n$. This proves degreewise surjectivity of (N6) for the complexes $C_n$. The kernel is $\lim C_n=\Gamma(V;I)$ by the sheaf gluing axiom. We obtain a short exact sequence of complexes

\[
0\longrightarrow\Gamma(V;I)\longrightarrow\prod_nC_n
\xrightarrow{1-\mathrm{shift}}\prod_nC_n\longrightarrow0.
\tag{N7}
\]

Products are exact in the category of modules, so their cohomology is the product of the cohomologies. The long exact cohomology sequence of (N7) gives (N5). This is also the countable Milnor sequence of [Stacks, Tag 0D60](https://stacks.math.columbia.edu/tag/0D60), with the geometric comparison here supplied by the displayed resolution.

If all transitions in degree $q-1$ are surjective, the same recursive choice proves $\lim^1 H^{q-1}(V_n;A)=0$. Eventual isomorphisms in that degree suffice as well, since deleting finitely many initial terms does not affect the cokernel in (N6). Constancy only in degree $q$ would leave the leftmost term of (N5) uncontrolled.

## SH02-NCD-INTERVAL-SYSTEM — Two one-sided continuities force constancy

Let $(M_t,r_{u,t})$ be an inverse system of modules indexed by the real numbers: $r_{u,t}:M_t\to M_u$ for $u\le t$. Suppose that for every $s$ both natural maps

\[
\underset{t>s}{\operatorname{colim}}M_t\xrightarrow{\sim}M_s,
\qquad
M_s\xrightarrow{\sim}\lim_{u<s}M_u
\tag{N8}
\]

are isomorphisms. In the first system, indices approach $s$ from above and arrows are restrictions to smaller indices. Then every $r_{u,t}$ is an isomorphism.

*Proof of injectivity.* Fix $a<b$ and $x\in M_b$ whose restriction to $M_a$ is zero. Consider the times $t\in[a,b]$ for which the restriction of $x$ to $M_t$ is zero. They form a downward-closed nonempty set. Let $c$ be its supremum. If $c=a$, vanishing at $c$ is already known. If $c>a$, the restrictions vanish at every $u<c$; the injectivity of the second map in (N8) gives vanishing at $c$ as well. If $c<b$, the element represented by $x$ in $\operatorname{colim}_{t>c}M_t$ maps to zero in $M_c$. Injectivity of the first map in (N8) implies that $x$ restricts to zero at some $d$ with $c<d\le b$, contradicting the supremum. Hence $c=b$ and $x=0$.

*Proof of surjectivity.* Fix $y\in M_a$. By the first map in (N8), it extends to some later time. All extensions, whenever they exist, are unique because the transitions are now known to be injective. Let $J\subset[a,b]$ be the times to which $y$ extends. It is downward closed. Put $c=\sup J$. If $c>a$, the unique extensions for $a\le u<c$, together with the restrictions of $y$ for $u<a$, form a compatible family for all $u<c$. Thus the surjectivity of the second map in (N8) extends them to $M_c$; their restriction to $M_a$ is $y$. If $c=a$, use $y$ itself. If $c<b$, the first map in (N8) extends this element to a time strictly beyond $c$, a contradiction. Thus $c=b$ and the extension at $b$ exists. The maps are therefore bijective. $\square$

This is an interval argument about systems of modules, not a local-system assertion about a sheaf on an interval. The two subjects have different hypotheses.

## SH02-NCD-COMPACT-FRONT — The shrinking boundary that must be tested

Let $X$ be Hausdorff, let $(U_t)_{t\in\mathbb R}$ be increasing open subsets, and fix $s$. Suppose $\overline{U_t\setminus U_s}$ is compact for every $t>s$. Define

\[
B_s=\bigcap_{t>s}\overline{U_t\setminus U_s}.
\tag{N9}
\]

The bars in (N9) are taken separately, before the intersection. Then $B_s$ is a compact subset of $X\setminus U_s$. If $V$ is an open neighborhood of $B_s$ and $t>s$, there exists $u$ with $s<u\le t$ such that

\[
\overline{U_u\setminus U_s}\subset V.
\tag{N10}
\]

Indeed, the closed sets $K_v=\overline{U_v\setminus U_s}$ for $s<v\le t$ lie in the compact set $K_t$ and decrease as $v$ decreases. If none were contained in $V$, the compact closed sets $K_v\setminus V$ would have the finite-intersection property: a finite intersection is the member with the smallest index. Their intersection would be nonempty, contradicting the definition of $B_s$. This also treats $B_s=\varnothing$, by taking $V=\varnothing$. Finally $K_v$ is disjoint from $U_s$ because $U_s$ is open.

## SH02-NCD-THEOREM — The deformation theorem

Let $X$ be Hausdorff, $F\in D^+(k_X)$, and put

\[
S=\operatorname{supp}(F)
=\overline{\bigcup_q\{x:H^q(F)_x\ne0\}}.
\]

Let $(U_t)_{t\in\mathbb R}$ be a family of open subsets satisfying the following conditions.

1. For every real $t$, $U_t=\bigcup_{s<t}U_s$. In particular the family is increasing.
2. If $s<t$, the set $\overline{U_t\setminus U_s}\cap S$ is compact.
3. Define $B_s$ by (N9). For every $s\le t$ and every $x\in B_s\setminus U_t$,
   \[
   (R\Gamma_{X\setminus U_t}F)_x=0.
   \tag{N11}
   \]

Then all natural restriction maps

\[
R\Gamma\!\left(\bigcup_tU_t;F\right)
\longrightarrow R\Gamma(U_s;F)
\tag{N12}
\]

are isomorphisms. Consequently restriction $R\Gamma(U_t;F)\to R\Gamma(U_s;F)$ is an isomorphism for $s\le t$.

The endpoint $s=t$ in (N11) is part of the hypothesis. At a point inside $U_t$, the sheaf complex $R\Gamma_{X\setminus U_t}F$ has zero stalk automatically. Thus (N11) is equivalently its vanishing on all of $B_s$; the stated form displays exactly where a test is required.

*Proof.* First reduce to $X=S$ using `SH02-NCD-FOUNDATIONS`. To check this reduction without confusing closures, write $W_t=U_t\cap S$. Then

\[
\overline{W_t\setminus W_s}^{\,S}
\subset S\cap\overline{U_t\setminus U_s}^{\,X}.
\tag{N13}
\]

The right side is compact by hypothesis; the left side is closed in it and is compact. The front computed in $S$ is a subset of $S\cap B_s$. The support tests identify under the closed embedding, so (N11) holds on that smaller front. Open-set cohomology agrees under the same embedding. We may therefore assume all the sets $\overline{U_t\setminus U_s}$ are compact.

Fix $s$ and put $Q_s=R\Gamma_{X\setminus U_s}F$. We claim

\[
\underset{t>s}{\operatorname{colim}}H^q(U_t;Q_s)=0
\quad\text{for every }q.
\tag{N14}
\]

Take a representative $\alpha\in H^q(U_t;Q_s)$, with $t>s$, and let $j_t:U_t\hookrightarrow X$. Apply (N1) to $Q_s$ and use (N2). Since $X\setminus U_t\subset X\setminus U_s$, this gives

\[
R\Gamma_{X\setminus U_t}F\longrightarrow Q_s
\longrightarrow Rj_{t*}(Q_s|_{U_t})\xrightarrow{+1}.
\tag{N15}
\]

Both of the first two terms restrict to zero on $B_s$, by (N11) for $(s,t)$ and for $(s,s)$. Hence the last term restricts to zero there as well. It is bounded below. Applying (N4) on the compact set $B_s$ shows that the restriction of $\alpha$ vanishes on $V\cap U_t$ for some open neighborhood $V$ of $B_s$: the identifications

\[
H^q(V;Rj_{t*}(Q_s|_{U_t}))=H^q(V\cap U_t;Q_s)
\]

are the natural direct-image identifications. This argument remains valid when the front is empty.

Choose $u$ as in (N10). Since $U_u\setminus U_s\subset V$, the two opens $U_s$ and $U_u\cap V$ cover $U_u$. The complex $Q_s$ restricts to zero on $U_s$ and on its intersection with $V$. The two-open Mayer-Vietoris triangle therefore identifies restriction

\[
R\Gamma(U_u;Q_s)\xrightarrow{\sim}R\Gamma(U_u\cap V;Q_s).
\tag{N16}
\]

One may obtain this triangle by applying an injective resolution to the ordinary two-open sheaf gluing sequence; flabbiness makes its last difference map surjective. The restriction of $\alpha$ is zero on the right of (N16), since $u\le t$, so it is zero on the left. This proves (N14).

Restrict the localization triangle $Q_s\to F\to Rj_{s*}(F|_{U_s})$ to $U_t$, take cohomology, and take the filtered colimit over $t>s$. The cohomology of its last term is constantly $H^q(U_s;F)$ and all its transitions are identities. Filtered colimits are exact, and (N14) holds in consecutive degrees. We obtain the natural right-continuity isomorphism

\[
\underset{t>s}{\operatorname{colim}}H^q(U_t;F)
\xrightarrow{\sim}H^q(U_s;F)
\quad(q\in\mathbb Z).
\tag{N17}
\]

Choose $N$ such that $F\in D^{\ge N}(k_X)$. Sections, being right derived from a left exact functor, have no cohomology below $N$ on any open set. We now prove by induction on $q\ge N$ that all restriction maps in degree $q$ are isomorphisms. For any fixed $s$, choose $s_n\uparrow s$ strictly from below. The first hypothesis gives $U_s=\bigcup_nU_{s_n}$. At $q=N$, the degree $q-1$ term of (N5) is zero. At each subsequent degree, the induction hypothesis makes the degree $q-1$ system constant. In either case (N5) gives

\[
H^q(U_s;F)\xrightarrow{\sim}\lim_{u<s}H^q(U_u;F),
\tag{N18}
\]

where the sequence is cofinal for this inverse limit. Equations (N17) and (N18) are precisely the hypotheses of `SH02-NCD-INTERVAL-SYSTEM`, which proves constancy in degree $q$ and completes the induction.

Finally $\bigcup_tU_t=\bigcup_{n\ge0}U_n$. Apply (N5) again. All transitions in every cohomology degree are now isomorphisms, so the $\lim^1$ term vanishes and the inverse limit identifies with any fixed $H^q(U_s;F)$, using indices $n\ge s$. Its comparison is restriction. Thus (N12) induces an isomorphism in every degree and is an isomorphism in $D^+(k)$. $\square$

### SH02-NCD-PARAMETERS — Open parameter intervals and locality in time

The same theorem holds with parameters in any nonempty open interval $I\subset\mathbb R$, bounded or unbounded, and with $\bigcup_{t\in I}U_t$ in its conclusion. Choose an increasing homeomorphism $\mathbb R\to I$. It preserves increasing unions, pairs $s<t$, the fronts (N9), and the inequalities $s\le t$ in the tests. Pulling the family back therefore satisfies the theorem.

Conditions can also be verified on overlapping parameter intervals. If the theorem applies on each member of an open cover of a parameter interval, every pair of times in a sufficiently small member has an isomorphic restriction. A compact segment between any two times has a finite subdivision subordinate to that cover: take a Lebesgue number for its finite subcover and subdivide into shorter segments. Composing the adjacent restriction isomorphisms gives the desired restriction for the endpoints. This use of compactness occurs in the parameter line and does not add compactness of $X$.

## SH02-NCD-SUBLEVELS — Checking the theorem for a real function

Let $f:X\to\mathbb R$ be continuous, $I=(a,b)$ a nonempty open interval with possibly infinite endpoints, and $F\in D^+(k_X)$. Assume, for every compact interval $[c,d]\subset I$, that

\[
f^{-1}([c,d])\cap\operatorname{supp}(F)\text{ is compact}.
\tag{N19}
\]

Assume also that for each $c\in I$ and every $x$ with $f(x)=c$,

\[
(R\Gamma_{\{f\ge c\}}F)_x=0.
\tag{N20}
\]

Then for each $c\in I$, the natural map

\[
R\Gamma(\{f<b\};F)\longrightarrow R\Gamma(\{f<c\};F)
\tag{N21}
\]

is an isomorphism, interpreting $\{f<+\infty\}=X$.

Indeed, set $U_t=\{f<t\}$ for $t\in I$. Continuity gives both $U_t=\bigcup_{s<t}U_s$ and

\[
\overline{U_t\setminus U_s}\subset f^{-1}([s,t]),
\qquad B_s\subset f^{-1}(s).
\tag{N22}
\]

The first inclusion and (N19) imply the required compactness because the supported closure is a closed subset of that compact slab. For $t>s$, the second inclusion puts $B_s$ inside $U_t$, where the support test vanishes automatically. For $t=s$, condition (N20) is exactly the remaining test. The union of the $U_t$ is $\{f<b\}$. Apply the parameter-interval version.

For the microsupport specialization, use the advanced course conventions: $k$ is commutative of finite global dimension, $X$ is a finite-dimensional real manifold countable at infinity, and $F\in D^b(k_X)$. The defining support test for microsupport gives a sufficient hypothesis for (N20): for a $C^1$ function $f$, require $(x,df_x)\notin\operatorname{SS}(F)$ at every point with $f(x)\in I$. Subtracting the level value identifies (N20) with that defining test. This last implication uses only the definition in `SH02-MST-TEST`, not the propagation theorems that depend on the present deformation result. The proof of `SH02-NCD-THEOREM` has no microsupport dependency.

## SH02-NCD-EXAMPLES — Two mechanisms that can defeat continuation

### SH02-NCD-MISSED-FRONT — A boundary point missed by the wrong intersection

Fix a nonzero $k$-module $M$, let $X=\mathbb R$, and let $F=M_{[0,\infty)}$, the constant sheaf on the closed half-line followed by closed direct image. Set

\[
U_t=\begin{cases}\varnothing,&t\le0,\\(0,t),&t>0.\end{cases}
\tag{N23}
\]

This family is left continuous and its supported closed increments are compact. For $s=0$, the intersection of the increments $U_t\setminus U_0=(0,t)$ is empty. Taking the closure after that intersection would therefore produce an empty test set. In contrast, (N9) gives $B_0=\{0\}$.

For $s>0$, the front is $\{s\}$ and the restriction of $F$ near $s$ is constant. Its restriction towards $x<s$ is an isomorphism on derived stalks, so the support test at $s$ vanishes. For $s<0$, the front is empty. Thus the version using the closure of the intersection would pass every test. Its proposed conclusion would identify $R\Gamma((0,\infty);F)=M$ with $R\Gamma(U_0;F)=0$, which is impossible. The correct test detects the failure: $R\Gamma_{\mathbb R\setminus U_0}F=F$ has stalk $M$ at $0$.

The interval cohomology used here is the constant-coefficient calculation `SH02-CA-CONSTANT`; equivalently, evaluate sections on a nonempty convex interval and use its vanishing of higher cohomology. No finite generation of $M$ is involved.

### SH02-NCD-INFINITY — A change arriving from infinity

Let $F=M_{\mathbb R}$ and put

\[
U_t=\begin{cases}\varnothing,&t\le0,\\(1/t,\infty),&t>0.\end{cases}
\tag{N24}
\]

Again the family is left continuous. Its corrected front at $s=0$ is empty, since the closed rays $[1/t,\infty)$ have empty intersection as $t\downarrow0$. At $s>0$ the front is $\{1/s\}$; the support test for a constant sheaf at an endpoint of a half-line is zero. At negative $s$ the front is empty. All the local tests hold, but the closure of $U_t\setminus U_0$ is unbounded and is not compact. The proposed restriction is again $M\to0$. Thus compact supported increments exclude a failure that no finite boundary point can detect.

## SH02-NCD-EXERCISES — Applications with solutions

1. **A strip with a persistent boundary face.** Let $M$ be an arbitrary $k$-module, let $X=\mathbb R^2$, let $F=M_{[0,1]\times\mathbb R}$ by closed direct image, and set $f(x,y)=y+x^2$. Prove that every restriction $R\Gamma(\{f<d\};F)\to R\Gamma(\{f<c\};F)$ for $c<d$ is an isomorphism. Verify the boundary faces $x=0,1$ as well as interior points.

   *Solution.* The supported slab $[0,1]\times\mathbb R\cap\{c\le y+x^2\le d\}$ is a closed and bounded subset of the plane, hence compact. Change coordinates by $(x,y)\mapsto(x,z=y+x^2)$. This is a homeomorphism and takes the support to $[0,1]\times\mathbb R$ and the sublevel to $z<c$. At a point $(x_0,c)$ with $x_0\in[0,1]$, use rectangle neighborhoods. Their intersection with the support is a product of a nonempty interval in $[0,1]$ and an interval around $c$; its intersection with $z<c$ is another nonempty convex set. Constant-coefficient cohomology on each is $M$ in degree zero, and restriction carries a constant value to the same value. The defining direct-image stalk is the filtered colimit over these rectangles, so the map from $F_{(x_0,c)}$ to the lower-side direct-image stalk is the identity on $M$. Localization proves (N20), including at $x_0=0,1$. Off the closed strip the complex is locally zero. Apply `SH02-NCD-SUBLEVELS` on $I=\mathbb R$; the individual restriction maps follow by composition with the common global complex. This example allows infinite and torsion modules and a support with boundary.

2. **Why the equal-time test matters.** Take $F=M_{[0,1]}$ on $\mathbb R$ and $U_t=(-\infty,t)$. Show that requiring (N11) only for $s<t$ gives no restriction at all, and find a restriction map that is not an isomorphism.

   *Solution.* Here $B_s=\{s\}$ and $s\in U_t$ whenever $s<t$, so every strict-time test has zero stalk automatically. The supported increments are compact and the family is left continuous. If $c<0<d<1$, the cohomology on $U_c$ is zero, whereas on $U_d$ it is $M$ in degree zero. The missing equal-time test is at $s=t=0$: the stalk of $R\Gamma_{[0,\infty)}F$ is $M$. Thus the equal-time part cannot be discarded.

3. **Local assumptions on an open parameter interval.** Suppose (N19) and (N20) hold only for levels in $(2,5)$. State exactly which conclusion follows without a test at level $5$.

   *Solution.* For every $2<c<5$, restriction from $\{f<5\}$ to $\{f<c\}$ is an isomorphism. The union of sublevels with parameter in $(2,5)$ is $\{f<5\}$. No conclusion about $\{f\le5\}$ follows: it is a different subset, and the theorem supplies no equal-time test at level $5$.

4. **Locate the obstruction degree.** For an arbitrary increasing open exhaustion, explain why stability of $H^q$ alone is not the stated sufficient condition for computing $H^q$ of its union.

   *Solution.* In (N5), the kernel of the comparison to $\lim H^q$ is $\lim^1H^{q-1}$. The condition must control the transitions one degree below. In the deformation proof this is why the induction begins at a uniform lower bound and proceeds upward: each completed degree removes the obstruction for the next one.

## SH02-NCD-PROVENANCE — Correspondence and limits of this bridge

The exact freely accessible comparison used here is Robalo and Schapira, [*A lemma for microlocal sheaf theory in the infinity-categorical setting*, arXiv:1611.06789v1](https://arxiv.org/abs/1611.06789v1), submitted 21 November 2016. The verified author-supplied source and its corresponding PDF were compared: Lemmas 2.1–2.2 appear on pp. 2–3, and Theorem 2.3 with its proof on pp. 4–5. Section 2 uses a unital coefficient ring. Theorem 2.3 has the same Hausdorff, left-continuity, supported-compactness and equal-time boundary conditions used above, and permits unbounded complexes. The earlier bounded-below version in Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Theorem 1.4.3, printed pp. 30–31, also places a closure on each increment before the intersection. This is the front in (N9); the examples here explain its necessity directly.

The compact-front mechanism is shared with those sources: restrict the localization triangle to the limiting front, kill a cohomology class on a neighborhood of that compact set, and shrink the advance until it lies in that neighborhood. In the present proof, (N13) verifies the passage to the closed support, (N15) types the direct-image comparison, and (N16) uses the actual two-open gluing triangle to carry the vanishing back to the whole smaller open set. The empty-front case is included. These details preserve the natural restriction map in (N17), not just an abstract equality of cohomology groups.

The subsequent constancy argument is given in full here. The source recalls the set-valued criterion without proving it in Section 2, and its proof of the complex-valued Lemma 2.2 invokes earlier inverse-limit results. `SH02-NCD-INTERVAL-SYSTEM` instead supplies the injectivity and unique-extension arguments for the module system. Equations (N5)–(N7) derive the required countable exact sequence from one flabby resolution, and induction from the common lower bound removes its degree-below obstruction. Thus no unbounded injective-resolution theorem or omitted proof of the source's constant-functor criterion is being silently imported. The unbounded and higher-category theorems remain worthwhile, separately stated extensions outside this unit's bounded-below assertion.

The Stacks comparisons have distinct roles. [Tag 09V3](https://stacks.math.columbia.edu/tag/09V3) proves compact-neighborhood continuity by finite neighborhood shrinking and a Cech-cohomology argument for restricted injectives. It supplies the sheaf-level input (N3); the scalar-action check and finite convergence filtration above supply (N4) for arbitrary left modules. [Tag 0BKM](https://stacks.math.columbia.edu/tag/0BKM) records the bounded-below hypercohomology spectral sequence. [Tag 0D60](https://stacks.math.columbia.edu/tag/0D60) concerns derived inverse limits of complexes on a fixed space. It does not by itself identify sections on an increasing union: the sheaf gluing and degreewise surjectivity in (N7) provide that comparison here. All three locators were checked at the same native Stacks revision linked above.

This unit keeps its own order of proof obligations, its two failure mechanisms, and all four solved applications.

The exact Stacks compact-neighborhood import is GFDL-1.2-or-later, with no invariant sections or cover texts, under the [Stacks license notice](https://raw.githubusercontent.com/stacks/stacks-project/master/introduction.tex). The independently authored exposition in this unit is dedicated under CC0 1.0 Universal. The identified human component retains its own terms.
