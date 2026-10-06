# SH02-UCE — Uniform tests for an unbounded Hom complex

Working programme proof with explicit prerequisite contracts; complete transitive proof review remains unfinished. The purpose of this supplement is to justify the full input range in the tensor and Hom estimates, including a Hom complex with cohomology in arbitrarily negative degrees. The proof uses normal deformation before Fourier transformation. Consequently its inverse-image argument requires no Fourier adjunction normalization.

All manifolds below are finite dimensional, Hausdorff, countable at infinity and smooth. A submanifold is locally closed; work in an open ambient neighborhood where it is closed. The coefficient ring $k$ is commutative, unital and of finite global dimension. No constructibility, finite generation, perfectness or field hypothesis is imposed. Write $D(k_X)$ for the classical unbounded derived category. Write $\operatorname{SS}_{\mathrm u}$ for the neighborhood-uniform $C^1$ support-test definition in [the unbounded bridge](unbounded-range-bridge.md#SH02-UR-MICROSUPPORT). A vanishing test means vanishing in every cohomological degree on the same prescribed cotangent neighborhood.

The geometric operations $f^\#$ and $\widehat+$ have the smooth-coordinate sequence definitions in [characteristic estimates](characteristic-estimates.md#SH02-CHE-OPERATIONS). In particular,

\[
(x_0;\zeta_0)\in A\widehat+B
\Longleftrightarrow
\begin{cases}
(x_n;\xi_n)\in A,\ (y_n;\eta_n)\in B,\\
x_n,y_n\to x_0,\quad \xi_n+\eta_n\to\zeta_0,\\
|x_n-y_n|\,|\xi_n|\to0
\end{cases}
\tag{UCE1}
\]

for suitable sequences in a chart. The covectors need not remain bounded. Negating all cotangent components without moving their base point is denoted by a superscript $a$.

## SH02-UCE-WINDOWS — Extending a functor identity without truncating a microsupport bound

We use the following exact prerequisites from [UR](unbounded-range-bridge.md): the finite flat-soft model of $Rf_!$, its unbounded right adjoint, the unbounded projection formula, K-injective representatives with injective terms, finite ordinary and supported cohomological bounds on manifolds and their closed subsets, compact-neighborhood continuity, the unbounded open-union Milnor sequence, and the unbounded noncharacteristic deformation theorem. The finite-cohomological-dimension acyclic-complex theorem is the exact import [Stacks, Tag 07K7](https://stacks.math.columbia.edu/tag/07K7). The existing bounded proper base-change, localization and constant-sheaf adjunction comparisons retain their actual natural maps.

Here is a useful precise extension rule. Suppose triangulated functors $T_i$ have one common finite cohomological amplitude $[a,b]$. For a fixed output degree $q$, choose integers $l,u$ with

\[
l+b<q-1,\qquad u+a>q+1.
\tag{UCE2}
\]

The two truncation triangles give natural isomorphisms, in degree $q$, from $T_iF$ through $T_i\tau^{\leq u}F$ to $T_i\tau^{\geq l}\tau^{\leq u}F$. Indeed the removed lower tail has outputs only below $q-1$, and the removed upper tail has outputs only above $q+1$. The same window works for every $i$. Therefore a natural comparison between these functors which is an isomorphism on bounded objects is an isomorphism on all objects. The assertion also applies to a filtered colimit of their cohomology groups, since filtered colimits of modules are exact and the window is independent of the index.

We apply this rule only to identities and amplitude bounds for sheaf functors. We never assert that $\tau^{\geq l}\tau^{\leq u}F$ has microsupport contained in that of $F$. The geometry below is applied directly to the original unbounded object, using the unbounded deformation theorem.

For example, proper-support base change on finite-dimensional manifolds extends this way. Both sides of its natural comparison are compositions of exact inverse image and a proper-support direct image of uniformly bounded integral cohomological dimension. The comparison on bounded complexes is the existing proper-support comparison. The same finite window computes both sides in any specified degree. This proves unbounded proper-support base change, including its naturality, without a claim about the microsupport of a truncation. For a map proper on a fixed closed support, the same reasoning gives proper base change on that support, since its ordinary and proper images agree.

Two further comparisons will be used with their indices visible. For $U$ an open subset of a $d$-manifold and $\Omega\subset U$ open, ordinary extension by zero gives

\[
H^q(U;j_!j^{-1}F)
\simeq\underset{K}{\operatorname{colim}}H^q_K(U;F),
\tag{UCE3}
\]

where $K$ runs over subsets closed in $U$ and contained in $\Omega$. This is the bounded support-family identity used in `SH02-MO-CONE-AC`, with its canonical inclusion-of-support maps. Its extension is legitimate: the functor on the left has amplitude contained in $[0,d]$, while every functor on the right has amplitude contained in $[0,d+1]$, independently of $K$, by the localization triangle. Choose the one window (UCE2) for all $K$, apply the bounded identity there, and pass through its natural comparisons. This proves (UCE3) for arbitrary unbounded $F$; exactness of a colimit by itself would not have proved it.

Similarly, if $O_n$ increase to $O$ and $K$ is compact in a manifold, then

\[
\underset{n}{\operatorname{colim}}H^q(K;j_{n!}F|_{O_n})
\simeq H^q(K;j_!F).
\tag{UCE4}
\]

The bounded comparison is the compact-support comparison `SH02-AE-LIMITS`: on the compact space $K$, these groups are compactly supported cohomology of $K\cap O_n$ and $K\cap O$. A compact support is contained in some $O_n$. For the unbounded comparison, restriction and open extension are exact and the ordinary cohomological dimension of every closed subset $K$ is uniformly at most the ambient dimension. Thus one finite window works for all $n$. This also proves naturality for restriction between compact cap and base tests.

## SH02-UCE-DIRECTIONAL — The directional projector on the full derived category

Let $E$ be a finite-dimensional real vector space, let $C\subset E$ be a closed convex cone, and let $q:E\to E_C$ be the identity into the topology of ordinary opens invariant under addition by $C$. The cone may contain lines. The following assertions of [the directional-topology lesson](cone-topology.md) hold with $D$ in place of $D^+$:

\[
A\xrightarrow{\sim}Rq_*q^{-1}A,
\qquad P_C=q^{-1}Rq_*,\qquad P_C^2\simeq P_C,
\tag{UCE5}
\]

and, for an ordinary convex open $U$,

\[
R\Gamma(U+C;A)\xrightarrow{\sim}R\Gamma(U;q^{-1}A).
\tag{UCE6}
\]

The left side uses the directional topology. The kernel expression is

\[
P_CF\simeq Rp_{1*}\bigl((p_2^{-1}F)_{\{y-x\in C\}}\bigr),
\tag{UCE7}
\]

and directional locally closed support commutes with $Rq_*$ as in `SH02-GAM-SUPPORT`.

**Proof.** Put $d=\dim E$. For a sheaf $A$ on $E_C$, the bounded theorem (G6), applied with $A$ in degree zero, identifies its cohomology on the directional open $U+C$ with the ordinary cohomology of $q^{-1}A$ on $U$. Consequently $\Gamma(U+C;-)$ has cohomological dimension at most $d$. Also $q_*$ has cohomological dimension at most $d$: its higher derived sheaves have stalks given by filtered colimits of ordinary cohomology on directional neighborhoods, which are ordinary open subsets of $E$.

Choose a K-injective complex $I$ of injective sheaves representing an arbitrary $A\in D(k_{E_C})$. This exists on the directional space: module sheaves on every topological space form a Grothendieck category. Each $q^{-1}I^n$ is acyclic on ordinary locally closed convex sets by `SH02-GAM-FLABBY-ACYCLIC`. The ordinary functors in question have finite cohomological dimension. Tag 07K7 therefore allows their computation on the entire complex $q^{-1}I$, without a bound on $n$. Applying the underived convex continuation map term by term proves (UCE6). The same argument with the finite-cohomological-dimension functor $q_*$ proves (UCE5): $q^{-1}I^n$ is $q_*$-acyclic, and the underived unit is an isomorphism on each term. The adjunction identities give projector idempotence with its counit.

For (UCE7), use the actual comparison of `SH02-GAM-KERNEL`. On an ordinary convex open $U$, its correspondence space over $U+C$ has the explicitly constructed section and fibrewise convex contraction in that proof. The relative contraction argument uses the proper projection with fibre $[0,1]$. Its base-change comparison extends by (UCE2); cohomology of the constant complex on the compact interval is the complex itself, by the same finite-dimensional window argument. The two endpoint pullbacks are consequently inverse to the same interval pullback. Thus the relative contraction proof applies to every unbounded coefficient complex. It identifies the constructed comparison on sections over $U$; the colimit over ordinary convex neighborhoods identifies its stalks. This proves (UCE7) with the same map. Finally, the closed-support and locally closed-support proofs of `SH02-GAM-SUPPORT` use localization, open restriction and composition of right adjoints. These hold unboundedly, so their functorial fibre comparisons give the stated support identity. $\square$

The discussion also extends ordinary convex continuation on closed convex subsets: use the same injective-term acyclicity and the ordinary finite dimension bound. No finite-dimensional or Hausdorff assumption has been made about the directional topology itself. Its required bounds were proved from the ordinary-space calculation.

## SH02-UCE-TESTS — The same geometric neighborhoods work in every degree

The support-test, cone-representative and compact-cap conditions in `SH02-MST-EQUIVALENCE` remain equivalent for $F\in D(k_X)$ and $\operatorname{SS}_{\mathrm u}$. Explicitly, for $(x_0;\xi_0)$ outside that microsupport there is a pointed closed convex cone $C$, with

\[
\langle v,\xi_0\rangle<0\quad(v\in C\setminus\{0\}),
\tag{UCE8}
\]

and an unbounded complex $H$ on the coordinate vector space which agrees with $F$ near $x_0$ and satisfies $Rq_{C*}H=0$. Conversely such a representative excludes the covector. The equivalent cap restriction is an isomorphism of entire complexes. The directional propagation assertion `SH02-MST-PROPAGATION`, including its supported-projector conclusion, and the full cutoff assertion

\[
P_CF\xrightarrow{\sim}F
\quad\Longleftrightarrow\quad
\operatorname{SS}_{\mathrm u}(F)\subset E\times C^{\circ a}
\tag{UCE9}
\]

also hold in this range. In (UCE9), lines in $C$ are allowed.

**Proof, with the range checks.** We use the geometric constructions of the cited proofs, keeping their formulas, domains and maps. The following verifies every step at which the old boundedness convention could enter.

For the cone-to-test implication, strict negativity on the compact unit section of $C$ gives a uniform negative derivative bound on a smaller coordinate ball. For each testing function its negative sublevel germ is $C$-open. The sets $(B_\epsilon(x)+C)$ minus that germ shrink inside a ball of radius $K\epsilon$. Localization and this cofinality identify the test stalk with a stalk of the directional localization of $Rq_{C*}H$, exactly as in (T7). This argument uses only localization and exact filtered colimits, so is valid in every degree at once. The zero covector is treated by constant tests, which force the original complex to vanish on a neighborhood.

For cap-to-cone, form $B=F_{H_0\setminus L}$ using the halfspace and its base in (T5). The cap restriction and its localization triangle make the closed-cone sections of $B$ zero. Inequality (UCE8) makes the kernel correspondence proper on its support over compact base sets: the halfspace gives a uniform bound on the length of a cone segment. Unbounded proper base change and (UCE7) therefore identify these sections with $(P_CB)_x$. The supported representative $R\Gamma_{O_1\setminus O_0}B$ in (T10) is killed by $Rq_{C*}$, by (UCE5) and directional support compatibility, and agrees with $F$ near $x_0$. There is no need to prove this representative bounded.

For test-to-cap, use the analytic domains (T14), their fixed base disk (T15), and the uniform outward-conormal calculation (T16). These depend only on the initial cotangent neighborhood. The compact set controlling every moving increment is the same closed cap. The rim tests (T18), the support-composition identity and the decomposition into upper and lower supported portions are localization identities on entire complexes. Apply `SH02-UR-DEFORMATION` to (T17), giving the restriction isomorphisms (T19) and (T20) in all degrees. Finally the cofinal nested diagonal of domain parameters constructed after (T20) uses only compact geometry. Unbounded compact-neighborhood continuity from UR passes its restriction maps to the cap and its base. Thus one geometric cap works simultaneously in every degree. This proves the test equivalence, also with the stated $C^1$, smooth and analytic test classes.

For propagation, the halfspace proof uses the explicit rounded neighborhoods (T46). Their outward differentials (T48) lie in the interior of the negative polar; their supported increments lie in the fixed compact set (T50). The limiting-front and endpoint checks (T51)–(T52) therefore permit the unbounded deformation theorem. Compact continuity proves (T53). The two inclusions (T55) propagate vanishing along a ray by factorization of restriction isomorphisms, without a cohomological induction and without requiring that $C$ have interior.

For general directional opens, the compact localization (T56) produces the entire complex $G=R\mathcal Hom(k_D,F)$ with compact support. It may be unbounded; that is allowed. The closed-support identity (T60) and the section fibre (T61) follow from unbounded tensor–Hom adjunction and localization. The proved cofinality of directional neighborhoods inside the testing halfspace makes their vanishing an ordinary support-test stalk vanishing. The unbounded deformation theorem then applies directly to this $G$ and the moving linear halfspaces. Below its compact support the section complex is zero, so (T58) vanishes. This proves the full supported propagation assertion (T44), hence (T43). The case $C=\{0\}$ uses the zero-covector test exactly as stated there.

The forward cutoff proof now uses (UCE6), the localized cone test and projector idempotence. For the converse, the convex enlargement proof (T30)–(T40) uses (T36) both for an increasing union in the maximal-convex-domain argument and for the final exhaustion of $Q$. In each application the cohomological transitions have already been proved isomorphisms. The UR Milnor sequence applies in each integer degree and its $\lim^1$ term is zero. The maximal-convex-domain argument and each of its propagation applications are therefore unchanged. This proves (UCE9). All geometric neighborhoods and cone choices preceded any passage to a cohomological degree. $\square$

In particular, a family of complexes avoiding the same cotangent neighborhood admits the same small cone, cap tests and supported directional lens used in this proof. There is no assertion that independent pointwise neighborhoods for different complexes have a common refinement.

## SH02-UCE-OPPOSITE — Compact supports in an opposite cone

Let $C$ be pointed, $Rq_{C*}H=0$, and suppose $\Omega$ is $(-C)$-open with $\Omega\cap(L+C)$ relatively compact for every compact $L$. Then

\[
Rq_{C*}(H_\Omega)=0.
\tag{UCE10}
\]

If $\Omega'\subset\Omega$ is also $(-C)$-open and $\Omega\setminus\Omega'$ is relatively compact, then the extension map is an isomorphism

\[
R\Gamma_c(\Omega';H)\xrightarrow{\sim}R\Gamma_c(\Omega;H).
\tag{UCE11}
\]

**Proof.** It suffices to use the basis $U=B_\epsilon(x)+C$ of the directional topology. Here $U\cap\Omega$ is relatively compact. In (UCE3), let $K$ be closed in $U$ and contained in $\Omega$, and put $D=\overline K-C$. The closure is compact, so $D$ is closed, and it is closed in the $C$-topology. If $z=w-v\in D\cap U$ with $v\in C$, then $w=z+v\in U$, so $w\in\overline K\cap U=K$. Since $\Omega$ is $(-C)$-open, this gives

\[
K\subset D\cap U\subset\Omega.
\tag{UCE12}
\]

These enlargements are cofinal supports in (UCE3). Directional support compatibility identifies their cohomology with cohomology of the corresponding support in $Rq_{C*}H$, hence zero. This proves (UCE10) using the uniform support-family comparison already justified above.

The cone of $H_{\Omega'}\to H_\Omega$ is $H_{\Omega\setminus\Omega'}$ and has compact closed support. Its ordinary global cohomology vanishes by (UCE10) and the triangle. Proper and ordinary cohomology agree for a complex with that compact support, also unboundedly. Thus its compactly supported cohomology vanishes. The compact-support triangle proves (UCE11) with its extension map. $\square$

## SH02-UCE-RECTANGLE — A Hom calculation before shrinking either variable

Let $q_X,q_Y$ be the projections from $X\times Y$, let $F\in D(k_X)$ and $G\in D(k_Y)$, and put

\[
K=R\mathcal Hom(q_Y^{-1}G,q_X^!F).
\tag{UCE13}
\]

For ordinary open sets $U\subset X$ and $V\subset Y$, there is a natural isomorphism

\[
R\Gamma(U\times V;K)
\simeq R\operatorname{Hom}_k
\bigl(R\Gamma_c(V;G),R\Gamma(U;F)\bigr).
\tag{UCE14}
\]

**Proof.** Open restriction is compatible with exceptional inverse image by its unbounded adjunction. Apply the proper-support adjunction to $p:U\times V\to U$. Proper-support base change gives
$Rp_!q_V^{-1}(G|_V)\simeq(R\Gamma_c(V;G))_U$.
Adjunction with $p^!$ identifies the left side of (UCE14) with
$R\operatorname{Hom}_{k_U}((R\Gamma_c(V;G))_U,F|_U)$.
The constant-sheaf/sections adjunction gives the right side. All three comparisons are the canonical ones already fixed by the unbounded proper-support calculus. Thus restriction in $U$ acts on the second Hom argument; restriction from $V$ to $V'$ acts by precomposition with extension $R\Gamma_c(V';G)\to R\Gamma_c(V;G)$. $\square$

Both variables are still ordinary open sets in (UCE14). A subsequent filtered colimit must retain both shrinking systems. In particular we do not replace $R\Gamma(U;F)$ by sections on a compact subset inside Hom. An infinite free first argument already prevents that replacement for some degree-zero sheaves.

## SH02-UCE-EXTERNAL-HOM — One lens for each input variable

For the kernel (UCE13),

\[
\operatorname{SS}_{\mathrm u}(K)
\subset\operatorname{SS}_{\mathrm u}(F)
\times\operatorname{SS}_{\mathrm u}(G)^a.
\tag{UCE15}
\]

**Proof in the first variable.** Suppose $(x_0;\xi_0)$ is absent from $\operatorname{SS}_{\mathrm u}(F)$. If $\xi_0=0$, constant tests force $F$ to vanish near $x_0$, and $K$ vanishes on the corresponding product neighborhood by open restriction. Otherwise choose the cone-acyclic representative $H$ of $F$ from (UCE8). Replace $F$ by $H$ in (UCE13), obtaining a kernel $K_H$ agreeing with $K$ near the point under consideration. For every $C$-open $U$ and ordinary open $V$,

\[
R\Gamma(U\times V;K_H)
\simeq R\operatorname{Hom}_k
\bigl(R\Gamma_c(V;G),R\Gamma(U;H)\bigr)=0.
\tag{UCE16}
\]

The last section complex vanishes by composition of derived direct images and $Rq_{C*}H=0$. These rectangles form a basis of the $(C\times\{0\})$-topology: saturating an ordinary rectangle by this cone gives such a rectangle. Hence $Rq_{C\times\{0\}*}K_H=0$. To check this for an unbounded object, use a K-injective representative; direct image preserves K-injectives because inverse image is exact. Derived sections on the indicated basis are zero, and exact filtered colimits then make every cohomology stalk zero. For every $\eta$, the cone $C\times\{0\}$ pairs strictly negatively with $(\xi_0,\eta)$ on its nonzero vectors. The cone test excludes all these covectors from $K_H$, hence from $K$ locally.

**Proof in the second variable.** Suppose $(y_0;\eta_0)$ is absent from $\operatorname{SS}_{\mathrm u}(G)$. The zero case again gives local vanishing. Otherwise replace $G$ near $y_0$ by $H$ with $Rq_{C*}H=0$ and $\langle v,\eta_0\rangle<0$ for nonzero $v\in C$. Write $D=-C$.

Here is a bounded lens which will be used in the second variable. Choose a linear functional $\ell$ strictly positive on $C\setminus\{0\}$, a compact closed ball $B$ about $y_0$, and $a>\sup_B\ell$. Put

\[
\Omega=\{\ell<a\},\qquad
\Omega'=\Omega\setminus(B+C),\qquad
S=\Omega\cap(B+C).
\tag{UCE17}
\]

Both $\Omega$ and $\Omega'$ are $D$-open. The sum $B+C$ is closed and stable under $C$, so its complement is $D$-open. The point $y_0$ is in the ordinary interior of $S$. There is $c>0$ with $\ell(v)\geq c|v|$ on $C$. Thus $S$ is relatively compact, and so is $\Omega\cap(L+C)$ for every compact $L$: its cone component has length at most $(a-\inf_L\ell)/c$.

Use $H$ in the kernel, and let $K'=R\Gamma_{X\times S}K_H$. This agrees with $K_H$, hence with $K$, on a product neighborhood of $(x_0,y_0)$. For every ordinary open $U\subset X$ and every $D$-open $W$ in the second coordinate, localization gives

\[
R\Gamma(U\times W;K')\simeq
\operatorname{fib}\left[
R\Gamma(U\times(W\cap\Omega);K_H)
\longrightarrow
R\Gamma(U\times(W\cap\Omega');K_H)
\right].
\tag{UCE18}
\]

The opposite-cone result applies to both intersected opens: the difference is contained in the relatively compact $S$, and the forward-slice bound follows from that for $\Omega$. It makes
$R\Gamma_c(W\cap\Omega';H)\to R\Gamma_c(W\cap\Omega;H)$
an isomorphism. By (UCE14), the map inside the fibre of (UCE18) is therefore an isomorphism. This proves $Rq_{\{0\}\times D*}K'=0$ on a basis of directional rectangles. Since every nonzero $(0,v)\in\{0\}\times D$ pairs strictly negatively with $(\xi,-\eta_0)$, the cone test excludes $(x_0,y_0;\xi,-\eta_0)$ for every $\xi$.

These two exclusions prove (UCE15). Strict negativity on each compact unit cone section persists on an open cotangent neighborhood, as required by the definition. No Hom/filtered-colimit interchange occurs. $\square$

## SH02-UCE-EXTERNAL-TENSOR — Tensoring a compact test with a stalk

For arbitrary $F\in D(k_X)$ and $G\in D(k_Y)$,

\[
\operatorname{SS}_{\mathrm u}(F\boxtimes^LG)
\subset\operatorname{SS}_{\mathrm u}(F)\times\operatorname{SS}_{\mathrm u}(G).
\tag{UCE19}
\]

**Proof.** If $(x_0;\xi_0)$ is absent from the first microsupport, take its uniform compact cap and base tests $C_x,L_x$. The cone $C\times\{0\}$ gives product tests $C_x\times\{y\}$ and $L_x\times\{y\}$. Exact restriction, proper base change on the compact cap, and the unbounded projection formula identify their section complexes with

\[
R\Gamma(C_x;F)\otimes^L_kG_y,
\qquad R\Gamma(L_x;F)\otimes^L_kG_y.
\tag{UCE20}
\]

The cap restriction is an isomorphism before tensoring, hence after tensoring with any stalk complex. This excludes all product covectors with the prescribed first component, uniformly near it. Interchanging the two factors gives the other exclusion. The projection used here has a compact source, and its comparison was proved on arbitrary unbounded inputs in UR; this is not a finite-rank Künneth assertion. $\square$

The same argument with a constant second factor proves the submersion inclusion for arbitrary unbounded objects. The reverse inclusion follows by pulling a local test function back along a local product projection. Open-product base change in its localization triangle identifies the resulting stalk tests. Thus the submersion equality holds as well. A locally constant invertible coefficient line and a shift do not change microsupport, since locally their tensor operation is an invertible constant tensor on every support test.

## SH02-UCE-BOUNDARY — Boundary estimates with unbounded coefficients

The proper-image estimate, closed-embedding equality, noncharacteristic open-boundary estimates, arbitrary-open extension estimates, and missing-submanifold trace estimate of MO and AE remain valid for $\operatorname{SS}_{\mathrm u}$ on arbitrary unbounded inputs. The argument is as follows, in dependency order.

For proper images, the local test identity (MO9) uses only localization and proper base change on the closed support. Its sheaf on the compact fibre is zero because every stalk is a vanishing test. These identities are now available unboundedly. Properness and closedness provide the same initial cotangent neighborhood. For a closed embedding the converse cap test intersects the compact cap with the submanifold; exact closed pushforward identifies the sections. Thus the equality also extends.

For the two noncharacteristic open-boundary estimates (AE.2), use the local angular separation and directional caps (MO11)–(MO12). The separation is purely geometric. The ordinary-image proof applies the supported propagation conclusion and directional open restriction to $Rj_*j^{-1}F$. The extension-by-zero proof applies the same propagation to a localized representative, followed by (UCE10) on an opposite directional cap. These operations were proved above for unbounded complexes. The two closed-boundary estimates follow from the respective localization triangles. No duality or cohomology-sheaf truncation is used.

For arbitrary open extension, keep the moved domains (AE.32) and their common separation (AE.34). They yield one cotangent neighborhood avoiding the microsupport of every approximating extension $K_t$, for both signs, by the preceding noncharacteristic boundary result. The ordinary-image limit is

\[
Rj_*F\simeq R\!\varprojlim_n Rj_{n*}(F|_{O_n}).
\tag{UCE21}
\]

Here is the unbounded verification. Resolve $F$ by a K-injective complex $I$ with injective terms. Open restriction and open direct image preserve K-injectives. Products of K-injectives are K-injective: their Hom complex from an acyclic complex is the product of acyclic module complexes, which is acyclic. Thus the categorical derived product is computed by these products. Flabbiness makes restriction onto each smaller open degreewise surjective on sections of every ambient open. The map $1-\mathrm{shift}$ on the product is degreewise surjective by recursive lifting, with kernel $j_*I$ by sheaf gluing. Its homotopy fibre is therefore $j_*I$, proving (UCE21).

The fixed supported directional lens from (UCE8) and propagation is killed for every $K_t$. Both $Rq_*$ and $R\Gamma_S$ are right adjoints, so preserve the homotopy limit in (UCE21). They kill the limit too. The local cone test gives the required ordinary-image exclusion. For extension by zero, use the one fixed cap and base for all $K_t$, and apply (UCE4) to both. Their restriction comparison remains an isomorphism in every degree. The cap test gives the second exclusion. This proves (AE.37) unboundedly with its two signs.

The missing-submanifold proof now uses exactly the explicit doubled real blowup (AE.42), which is proper, the preceding open-boundary estimate on its positive chamber, and proper direct image. The sequence calculation (AE.44)–(AE.46) gives the same control $|u_n|\,|a_n|\to0$ of the large normal covectors. Finally the localization triangle (AE.47) and the closed-embedding microsupport equality give the trace estimate. These steps are independent of any cohomological endpoints. In particular, for $M=\{u=0\}$, $j:X\setminus M\hookrightarrow X$, and $A=\operatorname{SS}_{\mathrm u}(F)$, the latter is

\[
\operatorname{SS}_{\mathrm u}(i^{-1}Rj_*F)
\subset T^*M\cap C_{T_M^*X}(A).
\tag{UCE22}
\]

The normal-cone identification here is the one specified in AE; it retains the growth condition on the normal components. This proves the boundary statements by actual uniform tests, rather than by a claim that an arbitrary inverse limit preserves a microsupport bound.

## SH02-UCE-RADIAL — A conic image can be cut off at its zero section

Let $\tau:E\to M$ be a finite-rank vector bundle and $H\in D(k_E)$ be equivariant for positive fibre dilation. Then

\[
\operatorname{SS}_{\mathrm u}(R\tau_*H),\
\operatorname{SS}_{\mathrm u}(R\tau_!H)
\subset\{(z;\zeta):(z,0;\zeta,0)\in\operatorname{SS}_{\mathrm u}(H)\}.
\tag{UCE23}
\]

**Proof.** Equivariance and the submersion equality imply that every covector of $\operatorname{SS}_{\mathrm u}(H)$ annihilates the Euler field. Indeed, compare pullbacks by the action and by the projection on $E\times\mathbb R_{>0}$. At parameter $1$ their parameter-covector components are respectively pairing with the Euler field and zero. Equality of their microsupports forces that pairing to vanish. Fixed positive dilations also preserve this microsupport.

Work locally with a bundle metric and let $\varphi(v)=|v|^2$. It is proper over the base on each closed sublevel. At a nonzero vector, both $d\varphi$ and $-d\varphi$ fail to lie in the sum of microsupport with horizontal covectors: all terms of that sum annihilate the Euler field, whereas $d\varphi$ pairs with it as $2|v|^2$.

We verify the unbounded cutoff needed to apply this observation. For a map $f$ and exhaustion $\varphi$ as in `SH02-MO-RELATIVE-CUTOFF`, the proper map $(f,\varphi)$ reduces the problem to a complex on $X\times\mathbb R$. Proper direct image gives the one-sided vertical covector condition (MO28). The directional cutoff (UCE9) and convex continuation (UCE6) prove the restriction isomorphism (MO29) on each coordinate rectangle. For the opposite sign, the localization triangle on the difference of two upper tails gives the supported comparison (MO30), without dualizing the complex.

The ordinary closed endpoint is computed by compact-neighborhood continuity on the compact support sublevel over a shrinking base neighborhood, exactly as in `SH02-MO-CUTOFF-PROOF`. For the proper-support endpoint, the support-family colimit uses functors with one uniform finite bound, so the argument of (UCE3) extends the bounded comparison; proper supports are cofinal among sublevel supports after shrinking to a compact base neighborhood. The endpoint at the limiting level uses the UR Milnor sequence for an increasing family of upper-tail opens, whose cohomological restrictions are already isomorphisms. It has zero $\lim^1$ in every degree.

Finally the boundary estimate applied to a cutoff adds a vertical covector of the same sign as those already present. A horizontal output therefore has both vertical components zero. Proper image gives a lift over each slightly larger sublevel. Letting the level decrease uses compactness of a fixed support sublevel and closedness of microsupport; it gives a lift at the limiting level. This proves the localized estimate (MO27) unboundedly. With $f=\tau$, $\varphi=|v|^2$ and limiting level zero, the only remaining points lie on the zero section, giving (UCE23). Rank zero makes every map an identity and requires no punctured-fibre argument. $\square$

## SH02-UCE-SPECIALIZATION — Normal deformation with no cohomological endpoints

For a closed embedding $i:M\hookrightarrow X$, set $E=N_MX$ and use the deformation maps of [specialization](specialization.md). Define

\[
\nu_MF=s^{-1}Rj_*p_+^{-1}F\in D(k_E).
\tag{UCE24}
\]

This is equivariant for positive normal dilation. In the normal-cotangent identification, it satisfies

\[
\operatorname{SS}_{\mathrm u}(\nu_MF)
\subset C_{T_M^*X}\bigl(\operatorname{SS}_{\mathrm u}(F)\bigr).
\tag{UCE25}
\]

Moreover the usual natural recovery maps give

\[
R\tau_*\nu_MF\simeq i^{-1}F,
\qquad R\tau_!\nu_MF\simeq i^!F.
\tag{UCE26}
\]

**Proof.** Smooth base change for the action square and open restriction give equivariance. Its comparison extends from the bounded comparison by (UCE2): all ordinary direct images here have finite cohomological amplitude, and inverse images are exact. This is an extension of the natural functor comparison, not of a microsupport assertion.

For the bound, in coordinates $(u,z)$ with $M=\{u=0\}$, write $p_+(v,z,t)=(tv,z)$ for $t>0$. The submersion equality gives covectors

\[
(\alpha,\beta,\tau)=(t\xi,\zeta,\langle v,\xi\rangle).
\tag{UCE27}
\]

Apply the unbounded missing-hypersurface trace estimate (UCE22) to $t=0$, extending the positive-chamber object by zero to the other component of the complement. A covector $(v_0,z_0;\alpha_0,\beta_0)$ of the specialization therefore gives a sequence of covectors (UCE27) with $t_n\downarrow0$,
$(v_n,z_n;\alpha_n,\beta_n)\to(v_0,z_0;\alpha_0,\beta_0)$ and $t_n|\tau_n|\to0$.
Conicity of the original microsupport gives

\[
(t_nv_n,z_n;\alpha_n,t_n\beta_n)
\in\operatorname{SS}_{\mathrm u}(F).
\tag{UCE28}
\]

Relative to the conormal point $(0,z_n;\alpha_n,0)$, divide its normal displacement by $t_n$. The result tends to $(v_0,\beta_0)$, which is precisely the normal-cone membership (UCE25). This uses the raw specialization coordinates $(v,z;\alpha,\beta)$; no Fourier sign is inserted.

The recovery comparisons in (UCE26) are those in `SH02-SP-ZERO` and the radial contraction maps of CON. They extend by the functor-identity rule. All functors in (UCE24) and $R\tau_*$, $R\tau_!$ have finite cohomological amplitudes on these finite-dimensional spaces. For a closed embedding, $i_*i^!=R\Gamma_M$ has amplitude in a finite interval by localization, and exact $i^{-1}$ gives the same bound for $i^!$. Thus the bounded natural recovery comparisons extend to arbitrary $F$ using one window for all compositions.

For clarity, the auxiliary radial comparisons on an arbitrary equivariant $H$ extend in the same way: truncations of an equivariant complex remain equivariant because the action and projection inverse images are exact. Apply the bounded conic identities to its bounded windows. This argument concerns preservation of equivariance; it does not assert preservation of an arbitrary microsupport set by truncation. The ordinary recovery is restriction of the counit to the zero section. The proper recovery uses the closed-support counit and the connecting map of the positive-chamber localization triangle, as in SP. Thus (UCE26) retains its specified maps and introduces no orientation shift beyond those already built into $i^!$. $\square$

## SH02-UCE-RESTRICTION — Characteristic restriction from a normal-cone slice

For every $F\in D(k_X)$ and closed embedding $i:M\hookrightarrow X$,

\[
\operatorname{SS}_{\mathrm u}(i^{-1}F),\
\operatorname{SS}_{\mathrm u}(i^!F)
\subset i^\#\operatorname{SS}_{\mathrm u}(F).
\tag{UCE29}
\]

**Proof.** Apply (UCE23) to $\nu_MF$, then (UCE25) and (UCE26). The resulting geometric bound is the zero-section, zero-vertical-covector slice of $C_{T_M^*X}(A)$, where $A=\operatorname{SS}_{\mathrm u}(F)$. We check its meaning directly. In adapted coordinates it consists exactly of $(z_0;\beta_0)$ for which

\[
(u_n,z_n;a_n,b_n)\in A,
\quad u_n\to0,\ z_n\to z_0,\ b_n\to\beta_0,
\quad |u_n|\,|a_n|\to0.
\tag{UCE30}
\]

One direction follows from normal-cone coordinates by rescaling the conic covectors: if $u_n=t_nv_n$, $v_n\to0$, $\alpha_n\to0$ and the tangential normal displacement tends to $\beta_0$, use $a_n=\alpha_n/t_n$. Then $|u_n||a_n|=|v_n||\alpha_n|\to0$. Conversely, for (UCE30), choose $t_n>0$ tending to zero so that $|u_n|/t_n\to0$ and $t_n|a_n|\to0$. Such choices exist from the product condition: with $r_n=|u_n|$ and $s_n=|a_n|$, take

\[
t_n=\sqrt{\frac{r_n+n^{-2}(1+s_n)^{-1}}{1+s_n}}.
\tag{UCE31}
\]

Then $t_n\to0$, $r_n/t_n\leq\sqrt{r_n(1+s_n)}\to0$, and $t_ns_n\leq\sqrt{r_ns_n}+n^{-1}\to0$. Rescale the covector by $t_n$; its conormal base tends to zero and its normal displacement divided by $t_n$ tends to $(0,\beta_0)$. This is the stated slice. Criterion (UCE30) is exactly the embedding case of $i^\#$, proving (UCE29). The argument includes a zero normal component, codimension zero and an empty submanifold. $\square$

For an arbitrary smooth map, factoring through its graph and using the submersion inverse-image equality also gives $\operatorname{SS}_{\mathrm u}(f^{-1}F)\subset f^\#\operatorname{SS}_{\mathrm u}(F)$. The exceptional statement needed below is the closed-embedding statement (UCE29) for the diagonal. No extension of a general-map exceptional comparison is needed for that application.

## SH02-UCE-DIAGONAL-HOM — The unbounded exceptional Hom comparison

For a manifold map $f:Y\to X$ with its unbounded proper-support adjoint, arbitrary $P,Q\in D(k_X)$ admit the canonical isomorphism

\[
f^!R\mathcal Hom(P,Q)
\simeq R\mathcal Hom(f^{-1}P,f^!Q).
\tag{UCE32}
\]

**Proof.** For each $C\in D(k_Y)$, transposition, tensor–Hom adjunction and the UR projection formula give

\[
\begin{aligned}
\operatorname{Hom}(C,f^!R\mathcal Hom(P,Q))
&=\operatorname{Hom}(Rf_!C\otimes^LP,Q)\\
&=\operatorname{Hom}(Rf_!(C\otimes^Lf^{-1}P),Q)\\
&=\operatorname{Hom}(C\otimes^Lf^{-1}P,f^!Q)\\
&=\operatorname{Hom}(C,R\mathcal Hom(f^{-1}P,f^!Q)).
\end{aligned}
\tag{UCE33}
\]

Yoneda proves (UCE32). Its transpose is evaluation followed by the proper-support trace, with the projection comparison just used; hence it is the canonical exceptional Hom comparison. Composition of exceptional inverse images is the composition of the corresponding right adjunctions to proper image, retaining their counits. For the diagonal $\delta:X\hookrightarrow X\times X$, this gives

\[
\delta^!R\mathcal Hom(q_2^{-1}G,q_1^!F)
\simeq R\mathcal Hom(G,F),
\tag{UCE34}
\]

because $q_2\delta=q_1\delta=1_X$. This verifies the actual map on possibly unbounded Hom objects, without replacing the first input by its dual or assuming it perfect. $\square$

## SH02-UCE-SUM — The full tensor and Hom estimates

For $F,G\in D(k_X)$,

\[
\begin{aligned}
\operatorname{SS}_{\mathrm u}(F\otimes^LG)
&\subset\operatorname{SS}_{\mathrm u}(F)\widehat+
\operatorname{SS}_{\mathrm u}(G),\\
\operatorname{SS}_{\mathrm u}(R\mathcal Hom(G,F))
&\subset\operatorname{SS}_{\mathrm u}(F)\widehat+
\operatorname{SS}_{\mathrm u}(G)^a.
\end{aligned}
\tag{UCE35}
\]

**Proof.** Exact diagonal inverse image identifies the tensor with $\delta^{-1}(F\boxtimes^LG)$. Apply (UCE19) and the ordinary part of (UCE29). For Hom, apply (UCE15), the exceptional part of (UCE29), and the canonical identification (UCE34).

In each case the resulting set is $\delta^\#(A\times B)$. It equals $A\widehat+B$: a diagonal sequence has $x_n,y_n,z_n\to x_0$, sum covector tending to $\zeta_0$, and $|(x_n-z_n,y_n-z_n)|\,|(\xi_n,\eta_n)|\to0$. This implies (UCE1) by the triangle inequality. Conversely take $z_n=y_n$ in (UCE1); boundedness of the sum gives $|\eta_n|\leq|\xi_n|+C$, so the required product with the full pair norm also tends to zero. Monotonicity permits the external microsupport inclusions. This proves (UCE35).

In particular two bounded-below inputs are allowed, even when their internal Hom is unbounded below. The proof is a stronger-range deduction with the exact stated classical operations and neighborhood-uniform tests. $\square$

## SH02-UCE-PROBLEMS — Three checks on what the proof actually uses

**Problem 1.** Over a field on a point, set $G=\bigoplus_{n\geq0}k[-n]$ and $F=k$. Compute the Hom range and explain why the diagonal argument is well typed.

**Solution.** The input $G$ has one copy of $k$ in every nonnegative degree. Its Hom into $k$ has one copy in every nonpositive degree, and is unbounded below. On a point all geometric maps in (UCE34) are identities; the unbounded tensor–Hom adjunction still identifies their actual evaluation maps. No lower bound on the Hom output is used by either (UCE32) or the definition of $\operatorname{SS}_{\mathrm u}$.

**Problem 2.** In $E=\mathbb R^2$, let $C$ be the upward vertical ray. Choose the lens (UCE17) explicitly and verify that the argument does not require a cone with interior.

**Solution.** Use $\ell(x,y)=y$, a closed ball $B$ centered at the testing point, and a horizontal level $a$ above that ball. The set $B+C$ is the upward extrusion of the ball. Its portion below $a$ is bounded and contains the center in its ordinary interior. The halfplane below $a$ and its complement of that extrusion are both invariant under downward vertical translation. Their intersection with any downward-invariant open set has the same properties needed in (UCE18). Strict positivity of $\ell$ on unit vectors in $C$ remains true, although $C$ has empty interior in the plane.

**Problem 3.** Which finite-window arguments in this proof would become invalid if their bounds depended on the support index or the shrinking neighborhood?

**Solution.** The support-family comparison (UCE3), the increasing-open compact comparison (UCE4), and the base-change comparison would no longer admit one bounded input window computing a specified output degree for every index. Passing the bounded identity through the index limit would then be unjustified. In this proof the bounds come from one ambient finite dimension. The geometric estimates are subsequently proved on the original complexes; the windows never supply a microsupport bound for their truncations.

## SH02-UCE-SOURCES — The classical estimates and the larger derived range

Kashiwara and Schapira's freely available [Microlocal study of sheaves, Astérisque 128 (1985), §4.2, printed pp. 63–66](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) supplies the classical external tensor and Hom proof mechanisms. Proposition 4.2.1 treats two bounded-below tensor inputs with finite weak global dimension. Proposition 4.2.2 takes a bounded first Hom input and a bounded-below second input. Its proof uses duality on a rectangle, directional tests in one factor, and compactly supported sections of opposite-directional opens in the other. Those mechanisms are credited here. Their printed input bounds do not prove the full unbounded statement of this supplement.

Schapira's [A short review on microlocal sheaf theory, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) provides a compact comparison under the same commutative finite-global-dimension coefficient convention (p. 6). Definition 2.3 and Theorem 2.6, pp. 7–9, give the uniform test, cap and directional formulations for bounded inputs. Theorem 2.8, p. 10, states the external estimates. Corollary 2.12, p. 13, obtains noncharacteristic tensor and Hom estimates by restriction to the diagonal. Its inverse-image input, Theorem 2.11, includes only a sketch, explicitly referring elsewhere for its harder inclusion. The present proof therefore retains its own raw-normal restriction argument and all the prerequisite obligations on which that argument depends.

**Acyclic complexes and finite windows.** The exact general result is [Stacks Project, Tag 07K7](https://stacks.math.columbia.edu/tag/07K7), checked in derived.tex at official revision [a04446e5](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14). Given enough acyclic objects and a uniform finite cohomological-dimension bound, its proof constructs the unbounded derived functor and proves that complexes of acyclic terms compute it. Its truncation conclusions concern derived functors, not microsupport. UCE2–UCE4 use those finite bounds with one input window for all support or neighborhood indices.

**Directional tests and propagation.** Astérisque §3.2.1, printed pp. 55–56, propagates bounded-below sections by rounded neighborhoods and noncharacteristic deformation. The review's Theorem 3.8, pp. 18–19, states the bounded version. UCE-TESTS instead fixes the cone, cap and covector neighborhood on the original unbounded object and invokes the explicitly named unbounded deformation provider. Truncation never supplies a microsupport bound.

**Rectangle Hom and the opposite cone.** The rectangle identity and opposite-cone mechanism in Astérisque Proposition 4.2.2 are the relevant antecedents. UCE13–UCE18 retain the unbounded adjunction maps on ordinary open rectangles and use a compact lens to test the other factor. They do not interchange an arbitrary Hom with a compact-neighborhood colimit. The full unbounded proper-support adjunction and projection formula are prerequisites, rather than consequences of the bounded source formula.

**Passing from external to internal operations.** The review's Corollary 2.12 gives the diagonal strategy under noncharacteristic hypotheses. Here UCE23–UCE31 supply the radial, specialization and restriction steps needed for the asymptotic bound, retaining the product-growth condition. UCE32–UCE34 identify the actual exceptional Hom comparison by adjunction, and UCE35 applies the diagonal calculation. These stronger claims require the supplied arguments and their exact foundations.

There is a second range distinction in the deformation argument. The review's proof of Lemma 3.5, pp. 16–17, starts induction at a vanishing low cohomological degree. That starting point is unavailable for a general unbounded complex. The use here of the UR unbounded deformation theorem and the open-union Milnor sequence is therefore substantive. It cannot be justified merely by citing the review's bounded proof. Likewise the support-index bounds in UCE3 and UCE4 must be uniform; exactness of a filtered colimit alone would not suffice.

This supplement is organized by the obstacles to a larger derived range: finite windows for functor identities, uniform geometry for the original complex, ordinary-open rectangle duality, compact lenses, raw-normal recovery, and finally the diagonal. The three solved checks test an unbounded Hom on a point, a cone with empty interior and dependence on the support index. Classical mechanisms are attributed above; their reuse as mathematics is not a claim that the stronger-range theorem appears in the cited sources.

The independently written programme text is CC0. The linked human works retain their own terms, including the Stacks Project's [GFDL terms](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/COPYING). The exact Stacks theorem proves the acyclic-complex step only. Full proofs and review of the UR proper-support model, exceptional adjoint, projection formula, cohomological-dimension bounds, compact continuity and unbounded deformation; the GAM and MST geometry; and the MO and AE boundary comparisons remain part of the programme's transitive prerequisite work. 
