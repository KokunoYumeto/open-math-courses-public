# SH02-CB-UNIT — Finite local data and sheaf biduality

Status: independently authored English draft. The proofs below retain arbitrary locally compact Hausdorff spaces of finite c-soft dimension.

A stalk records what a section can look like near a point. A costalk records what can be supported at that point. Verdier duality exchanges these two measurements. To recover a sheaf after two dualizations, we need both measurements to be finite in the derived sense, and we need the surrounding neighborhood systems to stabilize in the appropriate categorical sense. Neither a dimension count nor a statement about stalks alone supplies that condition.

Throughout, $k$ is a commutative unital ring of finite global dimension $d$. A space is locally compact Hausdorff and has finite c-soft dimension for sheaves of abelian groups. No countability condition on its neighborhood bases is imposed. Write $a_X:X\to\mathrm{pt}$, $\omega_X=a_X^!k$, and

$$
D_XF=R\mathcal Hom(F,\omega_X),\qquad
D'_XF=R\mathcal Hom(F,k_X).
$$

The costalk at $x$ is the complex $C_x(F)=R\Gamma_{\{x\}}(X;F)=i_x^!F$. Complexes and morphisms of complexes are cohomologically graded. Thus $k[-m]$ has its nonzero cohomology in degree $m$.

## SH02-CB-IMPORTS — The precise imported contracts

The [exceptional inverse-image lesson](exceptional-operations.md) supplies `SH02-EX-DUAL-SECTIONS`: for $F\in D^b(k_X)$,

$$
R\Gamma(U;D_XF)\simeq
R\operatorname{Hom}_k(R\Gamma_c(U;F),k)
$$

for every open $U$, and

$$
R\Gamma_K(X;D_XF)\simeq
R\operatorname{Hom}_k(R\Gamma(K;F|_K),k)
$$

for compact $K$. These are the adjunction identifications, with their evaluation morphisms; an arbitrary choice of an isomorphism is insufficient in the biduality proof. Its `SH02-EX-RECTANGLE` gives, for $F\in D^b(k_X)$ and $G\in D^+(k_Y)$,

$$
R\Gamma(U\times V;
 R\mathcal Hom(q_X^{-1}F,q_Y^!G))
\simeq
R\operatorname{Hom}_k(R\Gamma_c(U;F),R\Gamma(V;G)).
$$

The [manifold-duality lesson](manifold-duality.md) supplies `SH02-MD-SUBMERSION`, `SH02-MD-RELATIVE`, and `SH02-MD-CLOSED`: the orientation line and its shift, the formula $q_Y^!G\simeq q_X^{-1}\omega_X\otimes^Lq_Y^{-1}G$ when $X$ is a topological manifold, and the closed-submanifold costalk formula. These imported contracts are not replaced by a field-coefficient or finite-rank special case here.

For the local geometric models, `SH02-CA-CONSTANT` in the [convex acyclicity lesson](convex-acyclicity.md) proves that ordinary cohomology of a nonempty locally closed convex set with constant coefficients is exactly its coefficient module in degree zero. Compact-support cohomology of a ball is the orientation calculation in the manifold-duality lesson; proper-support base change and the projection formula give its product version.

We also use the following sheaf foundations, owned by the prerequisite course: exact filtered colimits of sheaves; injective resolutions; compact-neighborhood continuity of sheaf cohomology; proper-support extension maps for open embeddings; and derived tensor–Hom adjunction. In the continuity statement, compact sets form a directed family; a countable local basis is not required.

### SH02-CB-IMP-PRO-CALCULUS — Formal systems and their morphisms

This prerequisite contract has a limited supporting proof in [formal stabilization](formal-system-bridge.md); broader categorical foundations remain owned by SH-01. For systems indexed by arbitrary small directed posets or their opposites in the locally small categories used here, we require the formal ind/pro Hom formulas, the fully faithful constant-object embedding, and invariance under cofinal reindexing. In an additive category the zero criterion says that a system is formally zero exactly when every stage has a later transition equal to zero. A single pro-morphism, including a pro-isomorphism, and the finite acyclic diagrams used below admit simultaneous level representatives after common cofinal reindexing. A pro-isomorphism so represented need not be a levelwise isomorphism. For module systems, kernels and cokernels of such strict representatives compute the corresponding formal kernels and cokernels; hence a strict pro-isomorphism has pro-zero kernel and cokernel. A functor extends to formal systems, preserving their isomorphisms; a contravariant functor interchanges ind and pro. These are categorical assertions, separate from existence or exactness of ordinary limits. The net and duality arguments below use this contract. The supporting proofs `SH02-FSB-HOM` through `SH02-FSB-FUNCTORS` establish these formal assertions, with strictification restricted to the finite acyclic diagrams actually used. 

### SH02-CB-IMP-DERIVED-COFINALITY — Derived limits of module diagrams

The second contract, proved in `SH02-FSB-COFINALITY` and `SH02-FSB-PRISM` of the [formal stabilization lesson](formal-system-bridge.md), concerns small directed partially ordered sets $I,J$ and an order-preserving map $\phi:J\to I$. Suppose that for every $i\in I$ the upper comma category $J_i=\{j\in J:i\leq\phi(j)\}$ is nonempty and directed. For every inverse system $A:I^{\mathrm{op}}\to\operatorname{Mod}(k)$, the canonical restriction must induce

$$
R\varprojlim_I A\xrightarrow{\sim}R\varprojlim_J\phi^*A.
$$

We also require compatibility with natural relations between indexing maps: the natural transformation induced by such a relation agrees with the canonical comparison after these identifications. The product cochain resolution and its comma-category contraction described in `SH02-CB-NET-ACYCLICITY` specify the intended proof, including its actual comparison map. They are not an assertion that inverse limits are exact. The supporting lesson proves the derived comparison by a projective diagram resolution and proves relation compatibility by an explicit prism homotopy. Its application `SH02-FSB-NET` verifies the comparison used below for arbitrary directed index sets; ordinary inverse limits are not asserted exact.

## SH02-CB-SYSTEMS — What stabilization means

Let $\mathcal N_x$ be the open neighborhoods of $x$, ordered by shrinking. The restriction maps make $\{R\Gamma(U;F)\}$ an ind-system. The extension maps for compact supports make $\{R\Gamma_c(U;F)\}$ a pro-system. The words *ind* and *pro* retain more information than the ordinary colimit or limit of their cohomology modules.

For objects $A_i$ of a category $\mathcal D$, the ind-system is represented by $A$ when its formal ind-object is isomorphic to the constant object $A$; the analogous convention applies to a pro-system. For example, the morphism sets of pro-objects are

$$
\operatorname{Hom}_{\operatorname{Pro}(\mathcal D)}
 (\{A_i\},\{B_j\})
 =\varprojlim_j\varinjlim_i
   \operatorname{Hom}_{\mathcal D}(A_i,B_j).
$$

An isomorphism to a constant object allows transient terms. It does not say that every sufficiently small neighborhood has exactly the same cohomology. In the statements below, $\mathcal D=D(k)$, with the boundedness inherited from $F$ and the finite dimension assumptions.

A complex $P$ is **perfect** if it is isomorphic in $D(k)$ to a bounded complex of finitely generated projective $k$-modules. This is the finiteness condition we use. Over an arbitrary nonnoetherian ring, it must not be replaced without proof by a statement that its cohomology modules are finitely generated.

**Definition.** An object $F\in D^b(k_X)$ has cohomologically constructible local data if, at every $x$:

1. The ind-system $\{R\Gamma(U;F)\}$ and the pro-system $\{R\Gamma_c(U;F)\}$ are represented by objects of $D(k)$.
2. Their canonical comparisons with $F_x$ and $C_x(F)$ identify the representatives with these two complexes.
3. Both $F_x$ and $C_x(F)$ are perfect.

We abbreviate this condition by *cohomologically constructible*. The compatibility requirement in the second clause is part of the definition until the next argument proves it from the first clause. It is never discarded on the strength of an ordinary inverse-limit calculation alone.

## SH02-CB-NET-ACYCLICITY — A neighborhood argument without a countability assumption

Here is the homological fact that makes the arbitrary-neighborhood argument work.

**Lemma.** Let $I$ be a directed set and $A:I^{\mathrm{op}}\to\operatorname{Mod}(k)$ a pro-zero system: for every $i$ there is $j\geq i$ for which $A_j\to A_i$ is zero. Then $R^p\varprojlim_I A=0$ for every $p\geq0$. Consequently a pro-isomorphism of module systems induces an isomorphism on all derived inverse limits.

**Proof.** We spell out the reindexing because an arbitrary directed set need not have a countable cofinal subset. Form

$$
J=\{(S,n):S\subset I\text{ finite},\ n\in\mathbb N\},
$$

ordered by inclusion in the first variable and the ordinary order in the second. Each element of $J$ has only finitely many predecessors. Choose $\phi(S,n)\in I$ recursively on $|S|+n$. Require it to dominate every member of $S$, and, for every strict predecessor $(T,m)$, require the map

$$
A_{\phi(S,n)}\longrightarrow A_{\phi(T,m)}
$$

to be zero. Such a choice exists: each of the finitely many preceding targets has an index that kills it, and directedness gives a common upper bound for those indices and $S$. At the first step choose any element of $I$. This also makes $\phi$ order preserving. For each $i$, the set of $(S,n)$ with $\phi(S,n)\geq i$ is nonempty and directed. Thus $\phi$ is cofinal for computing inverse limits and their derived functors.

The shift $s(S,n)=(S,n+1)$ is another cofinal map, and there is a natural relation $\mathrm{id}_J\leq s$. Put $B=A\circ\phi$. Every component of $B\circ s\to B$ is zero. On derived inverse limits this map is nevertheless an isomorphism: cofinal restriction gives an inverse, and the natural relation between the two indexing maps identifies their composite with the identity. The resulting zero endomorphism of $R\varprojlim_JB$ is therefore invertible. This forces $R\varprojlim_JB=0$.

For clarity, the derived cofinality used here is the ordinary cofinality theorem for module-valued diagrams, not an assumption that inverse limits are exact. One proof uses the product cochain resolution of an inverse system, whose degree $p$ term is the product of the modules over strings of $p$ composable indexing arrows. For an order-preserving cofinal map, compare the two resolutions by the double complex of strings in the corresponding comma categories. Each such comma category is nonempty and directed. Its augmented chain complex is acyclic: every finite chain lies in a subcomplex that is coned off by a common upper bound. Exactness of products of modules then gives the claimed comparison of total complexes. The same comparison identifies the natural transformation $\mathrm{id}\leq s$ with the identity after restriction.

A constant module system has ordinary inverse limit equal to that module and zero positive derived inverse limits. In the same product resolution this is the cohomology of the directed indexing nerve with constant coefficients; its augmentation is acyclic by the common-upper-bound contraction just described.

Finally, kernels and cokernels of a strict morphism that is a pro-isomorphism are pro-zero. The long exact sequences for derived limits prove the last assertion. A general pro-isomorphism can be represented after cofinal reindexing by such a strict morphism, and derived cofinality makes the conclusion independent of that representation. $\square$

### SH02-CB-COSTALK-CONTINUITY — Stalk and costalk compatibility

**Proposition.** For $F\in D^b(k_X)$, representability of the two neighborhood systems in `SH02-CB-SYSTEMS` implies both of their canonical compatibility statements.

**Proof.** For ordinary sections, exactness of filtered colimits gives

$$
\varinjlim_{U\ni x}H^r(U;F)=H^r(F_x).
$$

A represented ind-system has these same colimits, so its comparison with the stalk is an isomorphism.

For compact supports, let $\mathcal K_x$ be all compact neighborhoods of $x$. There is a pro-isomorphism

$$
\{R\Gamma_c(U;F)\}_{U\ni x}
 \simeq
\{R\Gamma_K(X;F)\}_{K\in\mathcal K_x}.
$$

To see the actual maps, choose $V\subset K\subset U$ with $V$ open, $K$ compact, and $x\in V$. Extension of supports gives

$$
R\Gamma_c(V;F)\longrightarrow R\Gamma_K(X;F)
 \longrightarrow R\Gamma_c(U;F).
$$

One can insert such a triple inside every prescribed neighborhood, and the composites agree with the original transition maps. This proves the pro-isomorphism, without selecting a sequence.

There is also a canonical derived comparison

$$
R\Gamma_{\{x\}}(X;F)
 \simeq
R\varprojlim_{K\in\mathcal K_x}R\Gamma_K(X;F).
$$

Indeed, restriction $k_K\to k_L$ for $L\subset K$ gives the filtered colimit $\varinjlim_Kk_K=k_{\{x\}}$. Check it on stalks: at $x$ the value remains $k$, while any other point is excluded by a sufficiently small compact neighborhood. Filtered colimits of sheaves are exact, so this is also the derived colimit. Apply derived Hom into an injective resolution of $F$. The direct-sum resolution for that colimit becomes the product resolution computing the derived inverse limit of $R\operatorname{Hom}(k_K,F)=R\Gamma_K(X;F)$. This gives the displayed isomorphism and identifies its component maps with extension of supports.

Suppose the pro-system is represented by $Q$. After applying $H^q$, it is pro-isomorphic to the constant system $H^q(Q)$. The preceding lemma says that its positive derived limits vanish and its ordinary limit is $H^q(Q)$. All the support complexes are bounded below by the same lower bound for $F$. The derived-limit spectral sequence

$$
R^p\varprojlim_K H^q_K(X;F)
 \Longrightarrow H^{p+q}_{\{x\}}(X;F)
$$

therefore converges: after shifting that lower bound to zero, it is a first-quadrant spectral sequence. It collapses to its $p=0$ column. Consequently the canonical comparison from the costalk to the represented pro-object induces an isomorphism in every degree. $\square$

The use of pro-zero systems in this proof matters. Surjectivity of all transition maps in an arbitrary uncountable inverse system does not, by itself, imply vanishing of its higher inverse limits; [Stacks, Tag 0ANX](https://stacks.math.columbia.edu/tag/0ANX) gives an explicit example. The argument proves a stronger, precisely applicable stabilization statement.

## SH02-CB-PERFECT — Perfect complexes supply the algebraic duality

For a perfect $P$, put $P^\vee=R\operatorname{Hom}_k(P,k)$. There are natural isomorphisms

$$
P\xrightarrow{\sim}P^{\vee\vee},\qquad
P^\vee\otimes_k^L M\xrightarrow{\sim}
R\operatorname{Hom}_k(P,M)
$$

for every complex $M$ for which the expression is formed. To prove them, represent $P$ by a bounded complex of finite projectives. For a finite projective module, evaluation and the tensor–Hom map are isomorphisms: prove this for $k^r$ using coordinates, and then pass to a direct summand. Totalization involves only finitely many terms of $P$ in each degree. The module isomorphisms therefore assemble into the displayed isomorphisms of complexes, with the usual Koszul signs. They are precisely the evaluation maps, so their compatibility with morphisms of $P$ is built into the construction. In particular $P^\vee$ is perfect.

## SH02-CB-BIDUALITY — Duality exchanges the two local measurements

**Theorem.** If $F\in D^b(k_X)$ is cohomologically constructible, then $D_XF$ is cohomologically constructible. Its local measurements are canonically

$$
(D_XF)_x\simeq C_x(F)^\vee,
\qquad
C_x(D_XF)\simeq F_x^\vee.
$$

The evaluation morphism $F\to D_XD_XF$ is an isomorphism.

**Proof.** First $D_XF$ is bounded. If $F$ has cohomology in $[a,b]$ and the c-soft dimension is at most $c$, then $R\Gamma_c(U;F)$ has cohomology in $[a,b+c]$. The finite global dimension gives a uniform bound $[-b-c,d-a]$ for its dual. The dual-sections formula and exact filtered colimits give this bound on all stalks of $D_XF$.

Apply the contravariant functor $R\operatorname{Hom}_k(-,k)$ to the represented compact-support pro-system of $F$. A functor sends an isomorphism of formal systems to an isomorphism of formal systems; this step does not require duality to commute with an arbitrary ordinary inverse limit. The dual-sections formula therefore identifies the ind-system of ordinary sections of $D_XF$ with the constant ind-object $C_x(F)^\vee$. The stalk comparison gives the first displayed formula.

For the other direction, use compact neighborhoods and the second dual-sections formula. The ind-system $\{R\Gamma(K;F|_K)\}_{K\in\mathcal K_x}$ becomes the required support pro-system after applying duality. It is ind-isomorphic to $\{R\Gamma(U;F)\}_{U\ni x}$: restriction along the inclusions $K'\subset U\subset K$ supplies the comparison maps and their transition-compatible composites. It is consequently represented by $F_x$. Applying the same contravariant functor shows that the pro-system $\{R\Gamma_K(X;D_XF)\}$ is represented by $F_x^\vee$. The support interleaving and `SH02-CB-COSTALK-CONTINUITY` identify its representative with $C_x(D_XF)$.

Both representatives are perfect by `SH02-CB-PERFECT`. We have now checked boundedness, representability, compatibility, and perfectness separately, so $D_XF$ satisfies the full definition.

Repeat the stalk formula once. The stalk of the evaluation map is

$$
F_x\longrightarrow
R\operatorname{Hom}_k(R\operatorname{Hom}_k(F_x,k),k).
$$

This is the algebraic evaluation map: the identifications above came from the adjunction pairings, and extension or restriction of supports preserves those pairings. It is an isomorphism because $F_x$ is perfect. A morphism of sheaf complexes that is an isomorphism on every cohomology stalk is an isomorphism, proving biduality. $\square$

Tensoring by a locally constant rank-one projective sheaf and shifting preserve this constructibility condition. Here local constancy identifies the coefficient sheaf on a neighborhood with a constant finitely generated projective $k$-module $P$; it does not make $P$ free by shrinking the topological neighborhood. Choose a projective complement $Q$ with $P\oplus Q\simeq k^m$. Tensoring with $P$ is consequently the image of a fixed idempotent on the finite direct-sum functor $(-)^m$. Ordinary sections, compactly supported sections, sections with closed support, and stalks commute with this idempotent and with finite direct sums, including their derived versions. Their natural comparison maps do so as well. Each local formal ind- or pro-system for $P\otimes F$ is therefore the corresponding idempotent summand of the finite direct sum of the systems for $F$. Its representative is $P$ tensored with the old representative; the constant-system comparison and its inverse restrict to that summand. Perfect complexes are closed under finite direct sums and idempotent summands, so these representatives remain perfect. For duality, the finite-projective evaluation identity is

$$
R\operatorname{Hom}_k(P\otimes^L M,k)
\simeq P^\vee\otimes^L R\operatorname{Hom}_k(M,k),
\qquad P^\vee=\operatorname{Hom}_k(P,k).
$$

It follows by the same direct-summand argument from the free finite-rank identity and preserves the evaluation maps. Shifts simply shift the four systems and their representatives. This proves the preservation assertion without a freeness assumption on $P$.

## SH02-CB-EXTERNAL-HOM — A constructible factor in a product

Let $X,Y$ be as above, let $F\in D^b(k_X)$ be cohomologically constructible, and let $G\in D^+(k_Y)$. Write $F\boxtimes^LG=q_X^{-1}F\otimes^Lq_Y^{-1}G$. The evaluation pairing defines a morphism

$$
D_XF\boxtimes^LG\longrightarrow
R\mathcal Hom(q_X^{-1}F,q_Y^!G).
$$

**Theorem.** This morphism is an isomorphism. If $X$ is a topological manifold, so is the corresponding morphism

$$
D'_XF\boxtimes^LG\longrightarrow
R\mathcal Hom(q_X^{-1}F,q_Y^{-1}G).
$$

**Proof.** Test the first map at $(x,y)$. For a fixed open neighborhood $V$ of $y$, the rectangle contract identifies the section complex of its target over $U\times V$ with

$$
R\operatorname{Hom}_k(R\Gamma_c(U;F),R\Gamma(V;G)).
$$

The compact-support pro-system of $F$ is represented by the perfect complex $C_x(F)$. Applying the displayed contravariant Hom functor thus identifies the ind-system over $U$ with the constant object

$$
C_x(F)^\vee\otimes^LR\Gamma(V;G).
$$

Now take the ordinary stalk limit over $V$. A bounded complex of finite projectives commutes with this filtered colimit, giving

$$
C_x(F)^\vee\otimes^LG_y
 \simeq (D_XF)_x\otimes^LG_y.
$$

This is the stalk of the source. The map under these identifications is the finite-projective tensor–Hom evaluation from `SH02-CB-PERFECT`, hence is an isomorphism. Rectangles form a neighborhood basis in a product, so this proves the claim at every stalk. There is no constructibility requirement on $G$.

On a manifold, $\omega_X$ is an invertible shifted orientation line. Locally trivialize it. Then $D_XF=D'_XF\otimes\omega_X$ and $q_Y^!G=q_X^{-1}\omega_X\otimes q_Y^{-1}G$. The first result is the second result tensored by the same invertible factor. Cancelling that factor proves the second assertion, and the local identifications glue because all maps came from evaluation. $\square$

## SH02-CB-INTERNAL-HOM — Internal Hom and reversal of arrows

For two cohomologically constructible objects $F,G\in D^b(k_X)$, the canonical maps give

$$
R\mathcal Hom(G,F)
 \simeq R\mathcal Hom(D_XF,D_XG)
 \simeq D_X(D_XF\otimes^LG).
$$

Here is a direct proof that also checks the direction of the variables. Substitute the canonical isomorphism $F\simeq D_XD_XF$, then apply tensor–Hom adjunction:

$$
\begin{aligned}
R\mathcal Hom(G,F)
&\simeq R\mathcal Hom(G,R\mathcal Hom(D_XF,\omega_X))\\
&\simeq R\mathcal Hom(G\otimes^LD_XF,\omega_X)\\
&\simeq R\mathcal Hom(D_XF,R\mathcal Hom(G,\omega_X)).
\end{aligned}
$$

The middle expression is the stated dual tensor product, and the last is $R\mathcal Hom(D_XF,D_XG)$. The symmetry of derived tensor supplies its Koszul signs. On degree-zero morphisms this sends a map $G\to F$ to the dual map $D_XF\to D_XG$.

This theorem does not assert that the tensor product or the internal Hom of two cohomologically constructible sheaves is again cohomologically constructible. Its proof uses biduality for $F$ and $G$ separately; it supplies no stabilization theorem for their tensor product.

## SH02-CB-SUBMANIFOLDS — Closed submanifolds and arbitrary convex sets

Let $i:M\hookrightarrow X$ be a closed submanifold of dimension $m$ and codimension $p$ in a topological manifold. The sheaves $k_M=i_*k$ and $R\Gamma_Mk_X$ are cohomologically constructible. Moreover

$$
D_Xk_M\simeq i_*\omega_M,
\qquad
R\Gamma_Mk_X\simeq i_*\operatorname{or}_{M/X}[-p].
$$

To verify the local condition, use product coordinate neighborhoods at $x\in M$. Their intersections with $M$ are open $m$-balls. Ordinary cohomology is $k$ in degree zero, and compact-support cohomology is the orientation module in degree $m$. Shrinking balls induces the identity on the ordinary generator and the extension map on the orientation generator. These are isomorphisms, so both formal systems are represented by perfect complexes. Away from $M$ they are zero. The orientation formula for a closed embedding gives the second sheaf as a shifted rank-one local system on $M$, so the same calculation applies. Finally, proper-support adjunction for $i$ identifies the dual of $i_*k$ with $i_*i^!\omega_X=i_*\omega_M$; this is a statement about the trace-normalized map.

### SH02-CB-CONVEX-CHART — A boundary chart for every closed convex set

We need one elementary geometric fact to cover nonpolyhedral convex sets too. Let $C$ be a nonempty closed convex subset of a finite-dimensional real affine space, and let $L$ be its affine hull. At a relative boundary point, the pair $(L,C)$ is locally homeomorphic to Euclidean space with a closed half-space.

Here are details of a boundary chart. Translate the point to zero. Choose a relative interior point $a$ and a ball $B(a,r)\subset C$ in $L$. Choose a supporting linear functional $\ell$ at zero with $C\subset\{\ell\geq0\}$, and scale the direction $a$ to a vector $v$ with $\ell(v)=1$. Put $H=\ker\ell$. Convexity of the hull of $0$ and $B(a,r)$ shows that, for all small $h\in H$, the line $h+\mathbb Rv$ meets $C$ at some height bounded above by a constant times $\|h\|$. The supporting inequality bounds that height below by zero. Thus

$$
f(h)=\inf\{t:h+tv\in C\}
$$

is finite near zero, is attained by closedness, and is convex. A finite convex function on an open subset of a finite-dimensional vector space is continuous: on a small cube, convexity bounds it above by its values at the vertices, and applying that bound on a larger cube bounds its difference quotients on the smaller cube. In particular $f(0)=0$ and $f$ is continuous near zero.

Shrink the transverse neighborhood and choose a positive height $\delta$ so that $h+\delta v$ remains in $C$ for every $h$ in that neighborhood; this follows from the same interior ball, after scaling toward zero. Each vertical section of a convex set is an interval, so below $\delta$ the condition for membership is exactly $t\geq f(h)$. The coordinate change $(h,t)\mapsto(h,t-f(h))$ is a homeomorphism and sends this local portion of $C$ to a closed half-space. If $C$ lies in a proper affine subspace, add a complementary normal coordinate to view this chart in the original ambient space. The affine hull of a nonempty finite-dimensional convex set always has a relative interior point: a simplex of maximal affine dimension contained in the set supplies one.

### SH02-CB-CONVEX — Constructibility and duals of convex-set sheaves

**Proposition.** If $Z$ is closed or open and convex in a finite-dimensional real vector space $V$, then both $k_Z$ and $R\Gamma_Zk_V$ are cohomologically constructible.

**Proof and duals.** Let first $C$ be closed, nonempty, with affine hull $L$ of dimension $m$. At a relative interior point, the calculation is that for an $m$-plane. At a relative boundary point, use the chart just proved and product neighborhoods in it. For the closed half-line model, the compactly supported cohomology of $[0,\varepsilon)$ is zero: the compactification pair $([0,\varepsilon],\{\varepsilon\})$ has zero relative cohomology. Ordinary cohomology is $k$. Products with an open $(m-1)$-ball give the same zero compact-support complex and the ordinary complex $k$. These computations hold with arbitrary $k$; the interval pair is contracted explicitly, and the ball factor contributes its shifted orientation line. The transition maps are therefore isomorphisms. At points outside $C$, choose a neighborhood disjoint from $C$.

This verifies both represented systems and perfectness everywhere. The duality theorem gives

$$
D_Vk_C\simeq k_{\operatorname{ri}(C)}\otimes\operatorname{or}_L[m],
$$

where the relative interior is extended by zero first in $L$ and then along the closed inclusion of $L$ into $V$. Indeed, the dual has the stated orientation stalk in the relative interior and zero stalk at every other point. The adjunction map from that extension by zero is consequently an isomorphism on all stalks. Its restriction in the relative interior is fixed by the orientation trace, which specifies the isomorphism globally.

Now let $O$ be nonempty open convex. Its closure $C$ is closed convex of full dimension, and $O=\operatorname{int}C$. For completeness, a point in $\operatorname{int}C$ can be enclosed by a small simplex whose vertices lie in $O$, because $O$ is dense in $C$. Convexity then puts that point in $O$. The preceding formula gives $D_Vk_C\simeq k_O\otimes\omega_V$. Duality and the invertibility of the orientation line show that $k_O$ is cohomologically constructible and

$$
D_Vk_O\simeq k_C\otimes\omega_V.
$$

Finally, $R\Gamma_Zk_V=R\mathcal Hom(k_Z,k_V)=D_Vk_Z\otimes\omega_V^{-1}$. The duality theorem and invariance under an orientation twist give its cohomological constructibility. The empty set gives the zero complex; $C=V$ has no boundary and recovers $D_Vk_V=\omega_V$. $\square$

## SH02-CB-BOUNDARY-CRITERION — A boundary criterion and worked problems

Let $O\subset X$ be **open** in a topological manifold, with closure $C$. Call its boundary cohomologically regular if at every $x\in C\setminus O$ the canonical boundary calculations give

$$
(R\Gamma_Ck_X)_x=0,
\qquad
k\xrightarrow{\sim}(Rj_*k_O)_x,
\quad j:O\hookrightarrow X.
$$

This is equivalent to the two natural sheaf identifications

$$
D'_Xk_C\simeq k_O,
\qquad
D'_Xk_O\simeq k_C.
$$

To prove it, note that $D'_Xk_C=R\Gamma_Ck_X$ and $D'_Xk_O=Rj_*k_O$. On $O$ the two comparisons are the identity of $k$; off $C$ both sides vanish. Thus the boundary conditions are exactly the remaining stalk tests. For the second comparison, the map $k_C\to Rj_*k_O$ is restriction of the constant section. If one specifies only that the boundary stalk is abstractly isomorphic to $k[0]$, this map is still an isomorphism: its degree-zero target is a unital $k$-algebra free of rank one as a module. If $e$ is a basis, write $1=be$ and $e^2=ae$; the equality $1e=e$ gives $ab=1$, so $1$ itself is a basis.

Cohomological regularity forces $O=\operatorname{int}C$. If a point belonged to $\operatorname{int}C\setminus O$, its stalk in $R\Gamma_Ck_X$ would be $k$, contradicting the first boundary condition (for the zero coefficient ring all statements are vacuous; the topological conclusion is asserted for $k\ne0$). Every open convex subset of a real vector space has this regularity by `SH02-CB-CONVEX`.

### SH02-CB-PROBLEMS — Three worked problems

**Problem 1: a curved region in a plane inside three-space.** In $V=\mathbb R^3$, let

$$
C=\{(u,v,0):v\geq u^4\}.
$$

Find $D_Vk_C$ and $R\Gamma_Ck_V$, with orientations and degrees, using the standard ordered coordinates.

**Solution.** The affine hull is the oriented plane $L=\{w=0\}$ of dimension two, and the relative interior is $O=\{(u,v,0):v>u^4\}$. Hence $D_Vk_C=k_O[2]$. Since $\omega_V=k_V[3]$, we obtain $R\Gamma_Ck_V=k_O[-1]$. In particular the local-support complex vanishes on the curved boundary, even though $k_C$ has a nonzero stalk there. Reversing the plane orientation changes the displayed scalar trivialization, while the formulation with $\operatorname{or}_L$ remains canonical.

**Problem 2: why stalk finiteness alone is inadequate.** Take a field $k$, a countably infinite discrete set $S$, and its one-point compactification $X=S\cup\{\infty\}$. Let $j:S\hookrightarrow X$ and $F=j_!k_S$. Determine the local ordinary and compact-support systems at $\infty$ and decide whether $F$ is cohomologically constructible.

**Solution.** A basic neighborhood is $U_T=X\setminus T$ for a finite subset $T\subset S$. On this compact clopen neighborhood, sections of $F$ have finite support in $S\setminus T$, because a section must vanish near $\infty$. Thus

$$
R\Gamma(U_T;F)=R\Gamma_c(U_T;F)
 =\bigoplus_{s\in S\setminus T}k[0].
$$

Higher cohomology vanishes: the space has a basis of compact clopen sets, and sections on a compact clopen set are exact by refining a finite clopen cover into a disjoint one. The ordinary transition maps delete finitely many coordinates. Their ordinary colimit is zero, since each individual finitely supported section is eventually deleted, but the ind-system is not a constant zero ind-object: no transition map between two of these infinite-dimensional spaces is zero. Consequently the ordinary system is not representable by its stalk $F_\infty=0$. The compact-support transition maps are inclusions of cofinite direct sums. Their inverse limit is zero, but their pro-system is not pro-zero, since no transition is zero. It therefore cannot be represented by that zero limit. All stalks of $F$ are either $k$ or zero, yet $F$ fails the stabilization clauses. This also shows why replacing formal representability by an ordinary limit would lose essential information.

**Problem 3: an omitted openness hypothesis.** Explain why openness is necessary in the boundary criterion, and why a nonzero coefficient ring is necessary in its topological consequence.

**Solution.** If $O$ were allowed to be a closed affine hyperplane, then $\overline O\setminus O$ would be empty. Any condition tested only on that set would hold vacuously, although $O\ne\operatorname{int}(\overline O)$. Thus the criterion is a statement about open subsets. For the zero ring every sheaf complex is zero, so the boundary vanishing condition cannot distinguish any two open sets. These exceptions do not affect the convex-set or duality theorems, which remain valid for the zero ring.

## SH02-CB-ANTECEDENTS — Further directions and antecedents

An approved readable source is Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Definition 5.6.1 and Proposition 5.6.2. It formulates cohomological constructibility through formal local ordinary and compact-support systems represented by perfect complexes and gives the product-Hom comparison. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §4.8, presents the corresponding local systems, biduality and external-Hom statements, with an explicit Noetherian convention and a perfect-complex modification. Its biduality proof is left as an exercise and its external-Hom statement has bounded second input. Neither passage by itself proves this lesson’s larger locally compact, non-Noetherian and arbitrary-directed-neighbourhood scope.

The independent argument above supplies that scope by formal stabilization, a cofinal pro-zero construction, derived local pairings, and an evaluation check on stalks. It does not exchange an arbitrary derived inverse limit with a stalk without the uniform bound or replace formal representability by an ordinary limit. The convex-boundary calculation then uses the actual orientation and exceptional-operation contracts.

Two useful next questions require additional work. First, determine when proper direct image preserves this local constructibility condition, including the needed compactness argument for perfect global cohomology. Second, study tensor products at intersections whose topology changes infinitely often: biduality for each factor does not automatically provide stabilization for the intersection. Neither statement is assumed by the internal-Hom theorem in this lesson.
