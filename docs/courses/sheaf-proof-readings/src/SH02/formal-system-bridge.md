# SH02-FSB — Formal stabilization over arbitrary neighborhood sets

Original programme text: CC0 1.0 Universal. This reading proves the displayed formal and derived comparison statements used in local sheaf duality. Basic category and derived-functor foundations remain explicit prerequisites; this scoped source repair does not certify all surrounding SH-01 foundations.

A neighborhood calculation often becomes constant only after transition maps have discarded temporary terms. The right notion of stabilization records those maps. This lesson first constructs that formal notion, then separates it from the derived inverse limit of an actual module diagram. The distinction allows the neighborhood set to be arbitrarily large and directed.

## SH02-FSB-SETUP — Indices, categories, and the two contracts

All indexing sets are small, nonempty directed partially ordered sets. An inverse system in a locally small category $\mathcal C$ is a functor $A:I^{\mathrm{op}}\to\mathcal C$; write $a_{ji}:A_j\to A_i$ for $j\geq i$. A direct system is a functor $I\to\mathcal C$. We use a fixed universe for these sets and a larger universe when forming functor categories. The categories needed below are $\operatorname{Mod}(k)$ and the ordinary derived category $D(k)$, where $k$ is a unital commutative ring. The categorical and inverse-limit results in this lesson do not require finite global dimension.

The formal calculus through SH02-FSB-FUNCTORS supports [SH02-CB-IMP-PRO-CALCULUS](../../SH02-cohomological-biduality.html#SH02-CB-IMP-PRO-CALCULUS). The derived module-diagram calculation in SH02-FSB-COFINALITY and SH02-FSB-PRISM supports [SH02-CB-IMP-DERIVED-COFINALITY](../../SH02-cohomological-biduality.html#SH02-CB-IMP-DERIVED-COFINALITY). Basic categories, complexes, projective or injective resolutions, and the derived functors they define remain prerequisite material. The proofs below identify the resolutions and comparison maps needed here.

## SH02-FSB-HOM — Formal maps and constant objects

For inverse systems $A:I^{\mathrm{op}}\to\mathcal C$ and $B:J^{\mathrm{op}}\to\mathcal C$, define

$$
\operatorname{Hom}_{\operatorname{Pro}(\mathcal C)}(A,B)
=\varprojlim_{j\in J}\varinjlim_{i\in I}
\operatorname{Hom}_{\mathcal C}(A_i,B_j).
$$

The inner colimit uses precomposition by $a_{i'i}$ when $i'\geq i$. Consequently a component at target $j$ is represented by a map $A_i\to B_j$, and two representatives agree precisely when their composites from some common later $A_{i'}$ agree. A formal map is a family of such classes compatible with every target transition. A finite number of equalities can always be witnessed after one further source index, by directedness.

Here is a construction that verifies composition rather than presuming it. Associate to $A$ the covariant functor

$$
L_A(W)=\varinjlim_i\operatorname{Hom}_{\mathcal C}(A_i,W).
$$

A formal map $f:A\to B$ defines a natural transformation $L_B\to L_A$: represent an element of $L_B(W)$ by $B_j\to W$, choose a representative $A_i\to B_j$ of $f_j$, and compose. Refining either representative gives the same class, by the compatibility just stated. Conversely, evaluate a natural transformation at the class of $\mathrm{id}_{B_j}$ in $L_B(B_j)$. These operations are inverse. Composition and identities of natural transformations therefore make the displayed Hom sets into a category. This also proves associativity without selecting simultaneous representatives for infinitely many components.

For direct systems, the dual construction gives

$$
\operatorname{Hom}_{\operatorname{Ind}(\mathcal C)}(A,B)
=\varprojlim_i\varinjlim_j
\operatorname{Hom}_{\mathcal C}(A_i,B_j),
\qquad
\operatorname{Ind}(\mathcal C)
=\operatorname{Pro}(\mathcal C^{\mathrm{op}})^{\mathrm{op}}.
$$

The constant-system functor $c:\mathcal C\to\operatorname{Pro}(\mathcal C)$ is fully faithful: substituting two one-object systems in the formula gives $\operatorname{Hom}(cP,cQ)=\operatorname{Hom}_{\mathcal C}(P,Q)$. The same is true for ind-objects. These are the conventions of [Stacks, Tag 05PW](https://stacks.math.columbia.edu/tag/05PW) and [Tag 05PX](https://stacks.math.columbia.edu/tag/05PX); the construction above supplies the composition details used here.

## SH02-FSB-REPRESENTED — What a representative actually supplies

A pro-system $A$ is represented by $Q\in\mathcal C$ when there is a specified isomorphism $cQ\simeq A$. It is equivalent to give a compatible cone $p_i:Q\to A_i$, an index $i_0$, and a map $q:A_{i_0}\to Q$ such that

$$
q p_{i_0}=\mathrm{id}_Q,
\qquad
a_{\ell j}=p_jq a_{\ell i_0}
\quad\text{for some }\ell\geq j,i_0\text{ for each }j.
$$

Indeed, the cone is precisely a map $p:cQ\to A$, and a map $A\to cQ$ is represented by one such $q$. The first identity says $qp=\mathrm{id}_{cQ}$; the eventual identities say $pq=\mathrm{id}_A$ by the Hom formula. This proves both directions of the criterion. Taking opposites gives its ind version, with a cocone and eventual equalities after advancing the target index.

For any $T\in\mathcal C$, applying $\operatorname{Hom}_{\operatorname{Pro}(\mathcal C)}(cT,-)$ to this isomorphism gives

$$
\operatorname{Hom}_{\mathcal C}(T,Q)
\simeq\varprojlim_i\operatorname{Hom}_{\mathcal C}(T,A_i).
$$

Thus $Q$ is also the ordinary categorical limit with the displayed cone. Dually an ind representative is the ordinary categorical colimit. The converse is false: merely being an ordinary limit does not produce the eventual inverse $q$. The corresponding representative characterizations are [Stacks, Tag 05PZ](https://stacks.math.columbia.edu/tag/05PZ) and its [ind version, Tag 05PY](https://stacks.math.columbia.edu/tag/05PY).

If $\mathcal C$ has a zero object, then

$$
A\simeq0\text{ in }\operatorname{Pro}(\mathcal C)
\quad\Longleftrightarrow\quad
\text{for every }i\text{ some }j\geq i\text{ has }a_{ji}=0.
$$

The identity of $A$ is zero exactly when its component at each $A_i$ becomes zero in the inner colimit. This is the displayed criterion. A zero identity makes the unique maps to and from the zero object inverse, proving the assertion. In the ind case the criterion is that every source term is killed by some later transition.

## SH02-FSB-REINDEX — Cofinal changes preserve the formal object

Call an order-preserving map $\phi:J\to I$ cofinal here when, for every $i\in I$, the upper comma set

$$
J_i=\{j\in J:i\leq\phi(j)\}
$$

is nonempty and directed. For maps between directed sets, nonemptiness already implies the directed condition: $J_i$ is upward closed in $J$. We retain both words to identify the exact indexing condition used later in the derived proof.

The transition maps give a canonical formal isomorphism between $A$ and its restriction $\phi^*A$. To check it, for each $i$ choose $j\in J_i$ and use $A_{\phi(j)}\to A_i$. Different choices become equal at a common upper index. This defines $\phi^*A\to A$. In the other direction, the component at target $j$ is represented by $\mathrm{id}_{A_{\phi(j)}}$. Both composites equal the identity after a further transition, so they are inverse formal maps. Their definition also shows naturality in $A$ and compatibility with successive reindexings. This is the directed-set instance of the ordinary cofinality statement [Stacks, Tag 04E7](https://stacks.math.columbia.edu/tag/04E7), applied also to opposite categories. No derived inverse-limit assertion has yet been used.

## SH02-FSB-STRICT — Finite acyclic diagrams can be made levelwise

**Proposition.** Let $D$ be a finite category admitting a degree function on its objects that strictly increases along every nonidentity arrow. Suppose a diagram $D\to\operatorname{Pro}(\mathcal C)$ is given, with each vertex $v$ represented by a specified directed system $A^v:I_v^{\mathrm{op}}\to\mathcal C$. There is a directed set $R$, cofinal maps $r_v:R\to I_v$, and a diagram $D\to\mathcal C^{R^{\mathrm{op}}}$ whose formal image is the given diagram. In particular this applies to a single morphism, composable morphisms, parallel maps with a prescribed equality, and finite commutative squares.

**Proof.** A level consists of indices $i_v\in I_v$ and, for every arrow $\alpha:v\to w$, a map

$$
f_\alpha:A^v_{i_v}\longrightarrow A^w_{i_w}
$$

representing the prescribed formal component at target $i_w$. Require identity and composition equations at that level. Levels exist with arbitrarily prescribed lower bounds on their indices. Choose the vertices in decreasing degree. When choosing $i_v$, all targets of its nonidentity arrows have already been fixed. Each of the finitely many formal components has a representative, and directedness supplies a common source index above their indices and the prescribed bound. For each composable pair starting at $v$, the proposed composite and the proposed map for the composite arrow represent the same formal component. A further source index makes that equality hold. There are finitely many such equations. This finishes the construction at $v$ without changing its already chosen targets.

Order levels by coordinatewise increase, requiring in addition that every square made from an arrow $f_\alpha$ and the original transition maps commute. This is a partial order. Any two levels have an upper level: repeat the decreasing-degree construction above, demanding indices above those of both old levels and demanding commutativity with both old arrow maps. Each new demand is equality between two representatives of the same formal component at a fixed old target. It is therefore achieved by a further source index. There are finitely many demands at each vertex. The same construction works while imposing an additional lower bound at any vertex.

Let $R$ be this set of levels. It is small because the index sets and the relevant Hom sets are small, and it is directed by the preceding construction. Each projection $r_v$ is order preserving; its upper comma set above any prescribed $i_v$ is nonempty and directed by the same construction. Hence $r_v$ is cofinal. The transition squares built into the order make every $f_\alpha$ a natural transformation of the reindexed systems. The required equations already hold at every level. This proves the proposition. $\square$

To impose equality between two given parallel formal maps, apply the construction to the diagram in which those arrows are identified; finite lists of compatible composition equations are handled the same way. Taking opposites proves the ind version. With $\mathcal C=D(k)$, the level maps and equations lie in $D(k)$. This does **not** assert that arbitrary diagrams in $D(k)$ lift to strictly commuting chain maps. In the application below, applying $H^q$ gives actual module maps and actual equations, which is all that is needed.

The acyclicity condition on $D$ matters. Let every term of an inverse sequence be a nonzero module $M$, with zero transition maps between distinct indices. This system is formally zero. Its formal isomorphism to the constant zero system has inverse equations, but no cofinal reindexing can turn its terms into modules isomorphic to zero. Thus one cannot require arbitrary inverse equations to hold levelwise. The next argument uses their correct eventual form.

## SH02-FSB-INVERSE — Kernels and cokernels of a pro-isomorphism

Let $f:A\to B$ be a strict morphism of inverse module systems on one directed set $I$, and suppose its formal pro-morphism is invertible. For each $i$ there are $j\geq i$ and a map $g:B_j\to A_i$ satisfying

$$
g f_j=a_{ji},\qquad f_i g=b_{ji}.
$$

To prove this, represent the component of the formal inverse at $A_i$ by $g_0:B_\ell\to A_i$. The equation $fg=\mathrm{id}_B$, at target $B_i$, holds after restricting $B_\ell$ to some later term. The equation $gf=\mathrm{id}_A$, at target $A_i$, similarly holds after restricting the composite $A_\ell\xrightarrow{f_\ell}B_\ell\xrightarrow{g_0}A_i$. A common later index $j\geq i,\ell$ makes both equalities hold, and $g=g_0b_{j\ell}$ has the required properties.

Now $a_{ji}$ kills $\ker(f_j)$, because it factors through $f_j$. Also $b_{ji}$ induces zero on $\operatorname{coker}(f_j)\to\operatorname{coker}(f_i)$, because it factors through $f_i$. The levelwise kernel and cokernel systems are therefore pro-zero. This proof uses kernels and cokernels in modules, not an assertion about kernels in a derived category.

For clarity, levelwise kernels and cokernels of any strict module-system morphism also have the formal universal properties. For an arbitrary pro-system $Z$, the Hom formula gives

$$
\begin{aligned}
\operatorname{Hom}_{\mathrm{Pro}}(Z,\{\ker f_i\})
&=\ker\bigl(\operatorname{Hom}_{\mathrm{Pro}}(Z,A)
\longrightarrow\operatorname{Hom}_{\mathrm{Pro}}(Z,B)\bigr),\\
\operatorname{Hom}_{\mathrm{Pro}}(\{\operatorname{coker}f_i\},Z)
&=\ker\bigl(\operatorname{Hom}_{\mathrm{Pro}}(B,Z)
\longrightarrow\operatorname{Hom}_{\mathrm{Pro}}(A,Z)\bigr).
\end{aligned}
$$

To verify the first equality, apply $\operatorname{Hom}(Z_j,-)$ to each kernel and then take $\varprojlim_i\varinjlim_j$. A filtered colimit commutes with this kernel: a class mapping to zero is represented by a map whose composite becomes zero at some later index, and two resulting kernel representatives become equal after a further index. Ordinary limits preserve kernels because the compatibility and zero equations can be imposed together. For the second equality use $\operatorname{Hom}(\operatorname{coker}f_i,Z_j)=\ker(\operatorname{Hom}(B_i,Z_j)\to\operatorname{Hom}(A_i,Z_j))$ and take $\varprojlim_j\varinjlim_i$. The same representative argument applies. These natural identities are exactly the kernel and cokernel universal properties; they do not presume an abelian-category theorem about all pro-objects.

## SH02-FSB-FUNCTORS — Applying a functor to the formal system

Every covariant functor $T:\mathcal C\to\mathcal E$ induces functors on ind- and pro-categories by applying $T$ to all terms and all representatives of morphisms. Eventual equality remains equality after applying $T$, and the description of composition in SH02-FSB-HOM shows functoriality. Natural transformations of functors extend termwise and preserve the same compositions. In particular, a specified formal isomorphism $A\simeq cQ$ is sent to a specified formal isomorphism $TA\simeq c(TQ)$. This is also [Stacks, Tag 05SH](https://stacks.math.columbia.edu/tag/05SH).

A contravariant functor $T:\mathcal C^{\mathrm{op}}\to\mathcal E$ instead gives

$$
\operatorname{Pro}(\mathcal C)^{\mathrm{op}}
\longrightarrow\operatorname{Ind}(\mathcal E),
\qquad
\operatorname{Ind}(\mathcal C)^{\mathrm{op}}
\longrightarrow\operatorname{Pro}(\mathcal E).
$$

Indeed, a representative $A_i\to B_j$ becomes $T(B_j)\to T(A_i)$, and the Hom formulas have exactly these reversed source and target indices. After the dual-sections adjunction identifies the terms, this explains why $R\operatorname{Hom}_k(-,k)$ converts a represented compact-support pro-system into a represented ordinary-section ind-system. That sheaf-theoretic identification is [SH02-EX-DUAL-SECTIONS](../../SH02-exceptional-operations.html#SH02-EX-DUAL-SECTIONS). The formal argument makes no claim that this functor commutes with an arbitrary ordinary or derived inverse limit.

## SH02-FSB-COFINALITY — A resolution for the derived comparison

**Theorem.** Let $A:I^{\mathrm{op}}\to\operatorname{Mod}(k)$ be an inverse module system and let $\phi:J\to I$ be order preserving. If every $J_i=\{j:i\leq\phi(j)\}$ is nonempty and directed, restriction induces a natural isomorphism

$$
r_\phi(A):R\varprojlim_I A
\xrightarrow{\sim}R\varprojlim_J\phi^*A.
$$

This isomorphism is the derived restriction of compatible families. It respects composition of indexing maps.

**Proof.** Work in the abelian diagram category $\mathcal A_I=\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Mod}(k))$, whose exact sequences are objectwise exact. For $i\in I$ define the free representable diagram

$$
P_i(h)=k[\operatorname{Hom}_I(h,i)]
=\begin{cases}k&h\leq i,\\0&h\nleq i.\end{cases}
$$

Its transition maps between nonzero terms are identities. The map sending a natural transformation to its value on $1\in P_i(i)$ gives $\operatorname{Hom}_{\mathcal A_I}(P_i,A)=A_i$. Hence $P_i$ is projective. Direct sums of these objects are projective, because products of surjections of modules are surjective. We use the usual axiom of choice here.

For completeness this diagram category has enough injectives. The right adjoint $E_i$ to evaluation at $i$ sends a module $M$ to the diagram with value $M$ at $h$ when $i\leq h$, and zero otherwise. Embed each $A_i$ into an injective module $Q_i$. Adjunction gives a monomorphism

$$
A\longrightarrow\prod_i E_i(Q_i):
$$

at $h$ its $i=h$ component is the chosen embedding of $A_h$. Each $E_i(Q_i)$ is injective because evaluation is exact, and a product of injectives is injective because its Hom functor is a product of exact functors. This constructs the resolutions defining the right derived inverse limit.

Consider the augmented chain complex in $\mathcal A_I$

$$
P^I_n=\bigoplus_{i_0\leq\cdots\leq i_n}P_{i_0}
\quad(n\geq0),
\qquad P^I_0\longrightarrow c k.
$$

Repeated indices are allowed. The boundary is the alternating sum of vertex deletions. Deleting the first vertex uses $P_{i_0}\to P_{i_1}$; the other faces keep the coefficient diagram. The augmentation sends each generator to $1$. The face identities give $\partial^2=0$. At $h$, this is the free augmented chain complex of the poset $\{i:h\leq i\}$. Prepending its initial element $h$ gives a contraction, including the augmentation degree. Thus $P^I_\bullet\to c k$ is a projective resolution.

Since $\varprojlim_I A=\operatorname{Hom}_{\mathcal A_I}(c k,A)$, this resolution computes the derived limit. Explicitly, for an injective resolution $A\to Q^\bullet$, the first-quadrant bicomplex $\operatorname{Hom}(P^I_p,Q^q)$ computes $\operatorname{Hom}(P^I_\bullet,A)$ by projectivity and $\varprojlim_I Q^\bullet$ by injectivity. There are finitely many terms in each total degree, so the two calculations identify the same derived object.

The resulting cochain model is

$$
\begin{aligned}
C^n(I,A)&=\prod_{i_0\leq\cdots\leq i_n}A_{i_0},\\
(dc)_{i_0,\ldots,i_{n+1}}
&=a_{i_1i_0}c_{i_1,\ldots,i_{n+1}}
+\sum_{r=1}^{n+1}(-1)^r
c_{i_0,\ldots,\widehat{i_r},\ldots,i_{n+1}}.
\end{aligned}
$$

In degree zero its cycles are the compatible families. This agrees with the product construction in [Stacks, Tag 08RZ](https://stacks.math.columbia.edu/tag/08RZ); the module Ext version in [Tag 08S0](https://stacks.math.columbia.edu/tag/08S0) applies with the first coefficient diagram equal to the objectwise projective module $k$. The construction here proves the required case and identifies its maps.

Now form another augmented complex in $\mathcal A_I$:

$$
Q^\phi_n=\bigoplus_{j_0\leq\cdots\leq j_n}P_{\phi(j_0)}.
$$

At $i$ its augmented chain complex is the nerve complex of $J_i$. To prove exactness, an augmented cycle involves only finitely many vertices. Choose $b\in J_i$ above those vertices. On chains using vertices at most $b$, appending $b$ with sign $(-1)^{n+1}$ in degree $n$, and sending the augmentation generator to $[b]$, gives $\partial h+h\partial=\mathrm{id}$. Therefore every such cycle bounds. Nonemptiness gives surjectivity of the augmentation. This finite-support argument proves exactness even when there is no single upper bound for all vertices. Thus $Q^\phi_\bullet\to c k$ is another projective resolution.

There is a specified augmented chain map

$$
F_\phi:Q^\phi_\bullet\longrightarrow P^I_\bullet,
\qquad
[j_0,\ldots,j_n]\longmapsto
[\phi(j_0),\ldots,\phi(j_n)],
$$

using the identity on $P_{\phi(j_0)}$. Allowing repeated vertices makes the formula valid for any order-preserving $\phi$. It commutes with every face and induces the identity on $c k$.

An augmented map between projective resolutions that induces the identity is a chain homotopy equivalence. Here are the lifting details. Lift a map in degree zero through the other augmentation. Once degrees below $n$ have been constructed, the required degree-$n$ boundary lands in the cycles at degree $n-1$; exactness and projectivity lift it through the next boundary. This constructs a reverse chain map. Two lifts of the same augmentation are homotopic: their difference in degree zero lifts through the degree-one boundary; at degree $n$, subtract the already constructed homotopy term, observe that the remainder lands in cycles, and lift through degree $n+1$. Applying this to both composites produces the two homotopies.

Applying $\operatorname{Hom}_{\mathcal A_I}(-,A)$ to $F_\phi$ therefore gives a cochain homotopy equivalence. Under the displayed cochain models it is precisely

$$
(r_\phi c)_{j_0,\ldots,j_n}
=c_{\phi(j_0),\ldots,\phi(j_n)}.
$$

This is natural in $A$, restricts compatible families in degree zero, and satisfies $r_{\phi\psi}=r_\psi r_\phi$ on the complexes themselves. It is the claimed natural derived comparison. $\square$

The ordinary initiality theorem, [Stacks, Tag 002R](https://stacks.math.columbia.edu/tag/002R), concerns ordinary limits. The two projective resolutions above supply the additional derived assertion under the stated upper-comma condition.

## SH02-FSB-PRISM — The comparison for a natural change of index

Let $u,v:J\to I$ be order preserving and suppose $u(j)\leq v(j)$ for every $j$. Transitions define a map of diagrams

$$
t:v^*A\longrightarrow u^*A,
\qquad t_j=a_{v(j),u(j)}.
$$

Then, without any cofinality assumption on $u$ or $v$,

$$
R\varprojlim_J(t)\,r_v=r_u.
$$

To prove the equality for the actual comparison maps, define, for $n\geq1$,

$$
(H^nc)_{j_0,\ldots,j_{n-1}}
=\sum_{r=0}^{n-1}(-1)^r
c_{u(j_0),\ldots,u(j_r),v(j_r),\ldots,v(j_{n-1})},
\qquad H^0=0.
$$

Every index string is increasing, and every term lies in $A_{u(j_0)}$. This defines a homotopy with

$$
dH+Hd=C(t)r_v-r_u.
$$

The verification is the prism boundary calculation, which can be seen before applying Hom. A string $[j_0,\ldots,j_n]$ with coefficient $P_{u(j_0)}$ is sent to

$$
\sum_{r=0}^n(-1)^r
[u(j_0),\ldots,u(j_r),v(j_r),\ldots,v(j_n)].
$$

A deletion strictly before or after the change from $u$ to $v$ cancels with the term obtained by first deleting the corresponding source vertex. The two faces at adjacent change positions cancel each other. The only outer faces left are the all-$v$ string, with coefficient map $P_{u(j_0)}\to P_{v(j_0)}$, and minus the all-$u$ string. Applying Hom gives the displayed formula. In degree zero it reads

$$
(H^1dc)_j=a_{v(j),u(j)}c_{v(j)}-c_{u(j)},
$$

which fixes the sign and the direction of $t$. This proves the identity in $D(k)$ as well as its cochain realization.

In particular, if $s:J\to J$ satisfies $\mathrm{id}\leq s$ and $z:s^*B\to B$ is the transition map, then $C(z)r_s$ is homotopic to the identity. If every component of $z$ is zero, the homotopy shows

$$
d(-H)+(-H)d=\mathrm{id}_{C(J,B)}.
$$

Thus this particular derived-limit complex is contractible. This conclusion needs no separate cofinality assertion about $s$.

## SH02-FSB-NET — Applying the bridge to a pro-zero net

**Theorem.** If an inverse module system $A$ is pro-zero, then $R^p\varprojlim_I A=0$ for every $p\geq0$. A formal pro-isomorphism of inverse module systems consequently induces an isomorphism on all derived inverse limits.

**Proof.** Let

$$
J=\{(S,n):S\subset I\text{ finite},\ n\in\mathbb N\},
\qquad
(S,n)\leq(T,m)\Longleftrightarrow S\subseteq T, n\leq m,
$$

with $0\in\mathbb N$. This is directed. The point $(S,n)$ has at most $2^{|S|}(n+1)$ predecessors, and every strict predecessor has smaller $|S|+n$. Construct $\phi:J\to I$ by induction on that nonnegative integer. At a point $p=(S,n)$, choose, for each strict predecessor $q$, an index $\kappa_q\geq\phi(q)$ that kills the map into $A_{\phi(q)}$. Choose $\phi(p)$ above the finite set consisting of $S$ and all these $\kappa_q$. At $(\varnothing,0)$ choose any element of $I$. Choices at the same rank do not depend on one another.

The map $\phi$ is order preserving, since the killing indices dominate the previous chosen indices. Moreover every transition $A_{\phi(p)}\to A_{\phi(q)}$ for $q<p$ is zero. For any $i\in I$, the point $(\{i\},0)$ lies in $J_i$, and $J_i$ is upward closed and directed. Therefore SH02-FSB-COFINALITY applies to $\phi$.

Put $B=\phi^*A$ and $s(S,n)=(S,n+1)$. Each point is a strict predecessor of its shift, so the transition map $s^*B\to B$ is zero. SH02-FSB-PRISM contracts $C(J,B)$, and the cofinality isomorphism gives $R\varprojlim_I A=0$. No countable cofinal subset has been chosen.

For a strict pro-isomorphism $f$, SH02-FSB-INVERSE makes its levelwise kernel and cokernel pro-zero. The two exact diagram sequences using $\operatorname{im}f$, together with the long exact sequences of right derived limits, prove that $R\varprojlim(f)$ is an isomorphism. A general formal morphism has a level representative after SH02-FSB-STRICT. Reindexing the source and target gives its derived map by composing this level map with the inverse cofinality comparisons. Two representations of the same formal map admit a common refinement on which their maps agree: apply the finite construction with that equality imposed. The formulas in SH02-FSB-COFINALITY and SH02-FSB-PRISM identify their induced maps. The same finite construction for two composable maps proves compatibility with composition. Thus the derived map depends only on the formal morphism, and the assertion for pro-isomorphisms follows. $\square$

A constant module system $cM$ has $R\varprojlim_I cM\simeq M$. Its cochain model is Hom from the augmented free nerve chains of $I$ into $M$. Those chains resolve $k$: every finite augmented cycle can be coned to a common upper bound. Since $k$ and all chain modules are projective, the comparison-lifting argument in SH02-FSB-COFINALITY makes this resolution homotopy equivalent to $k$ in degree zero. Applying Hom proves the asserted cohomology in all degrees.

This proves the complete arbitrary-directed step used in [SH02-CB-NET-ACYCLICITY](../../SH02-cohomological-biduality.html#SH02-CB-NET-ACYCLICITY). The finite-predecessor construction there is valid; the resolution and prism above provide its missing explicit categorical support. Surjective transitions are a different condition. For arbitrary directed systems they need not force higher inverse limits to vanish, as shown by [Stacks, Tag 0ANX](https://stacks.math.columbia.edu/tag/0ANX).

## SH02-FSB-COSTALK — What the sheaf argument needs from this bridge

We now specify how these facts enter [SH02-CB-COSTALK-CONTINUITY](../../SH02-cohomological-biduality.html#SH02-CB-COSTALK-CONTINUITY). Let $X$ be locally compact Hausdorff, let $x\in X$, and let $F\in D^b(k_X)$. For this compatibility argument a common lower bound is enough. Compact neighborhoods $K$ of $x$ are ordered by shrinking. Their intersection is $\{x\}$, and they form a directed set; neither assertion uses a countable basis.

The sheaf foundations used here are exact filtered colimits and stalks, Theorems 2.1 and 3.1, injective resolutions, Theorems 2.3 and 4.1, and the closed-support adjunction and its derived construction. Write $k_K$ for the constant sheaf on the closed set $K$ extended to $X$, and use the restriction map $k_K\to k_L$ when $L\subset K$. These sheaves form a direct system with

$$
\varinjlim_K k_K=k_{\{x\}}.
$$

At $x$ its stalk is always $k$; a different point is excluded by some compact neighborhood. Exactness of filtered colimits makes this an exact derived-colimit calculation as well.

Choose one bounded-below injective sheaf resolution $F\to I^\bullet$. The complexes

$$
A_K^\bullet=\operatorname{Hom}_{k_X}(k_K,I^\bullet)
=\Gamma_K(X;I^\bullet)
$$

and their support-inclusion maps form an actual diagram of complexes with a common lower bound. They compute $R\Gamma_K(X;F)$. The product bicomplex for this diagram is

$$
C^{p,q}=\prod_{K_0\leq\cdots\leq K_p}A_{K_0}^q,
\qquad D=d_{\mathrm{index}}+(-1)^p d_{\mathrm{complex}}.
$$

It computes the derived inverse limit of the strict complex diagram by the resolution proof above. We can also identify it directly with the costalk. The direct-sum complex

$$
L_p=\bigoplus_{K_0\leq\cdots\leq K_p}k_{K_0}
\longrightarrow k_{\{x\}}
$$

is an augmented resolution, with the first face given by $k_{K_0}\to k_{K_1}$ and the other faces by deletion. Here is a stalkwise verification. Any positive-degree cycle has finite support; a common later index supplies the coning argument for the finite diagram. In degree zero, an element in the kernel of the augmentation is a finite sum whose images add to zero in the filtered colimit. After one later index the sum already vanishes; coning there expresses it as a boundary. The augmentation is onto on stalks. Thus the augmented sheaf complex is exact.

Apply $\operatorname{Hom}_{k_X}(-,I^q)$ in each degree. Injectivity makes every augmented row exact, and

$$
\operatorname{Hom}_{k_X}(L_p,I^q)=C^{p,q}.
$$

After shifting the common lower bound to zero this is a first-quadrant bicomplex. Its augmentation consequently gives a canonical quasi-isomorphism

$$
R\Gamma_{\{x\}}(X;F)
\xrightarrow{\sim}
R\varprojlim_K R\Gamma_K(X;F).
$$

The map into its degree-zero components comes from $k_K\to k_{\{x\}}$, hence is the actual inclusion of supports. This identifies the comparison map, not merely the resulting cohomology groups.

Exactness of products of modules identifies vertical cohomology in the same bicomplex. The first-quadrant spectral sequence is therefore

$$
R^p\varprojlim_K H^q_K(X;F)
\Longrightarrow H^{p+q}_{\{x\}}(X;F).
$$

Its convergence uses the common lower bound, not a bound on the cardinality of the neighborhood set. If the formal support pro-system in $D(k)$ is represented by $Q$, applying the functor $H^q$ makes its module system pro-isomorphic to $cH^q(Q)$. SH02-FSB-NET and the constant-system calculation show that the spectral sequence has only the $p=0$ column.

There is a precise map to the representative even though a general object of $\operatorname{Pro}(D(k))$ has not been given a derived-limit realization. The support inclusions give a formal cone

$$
cR\Gamma_{\{x\}}(X;F)\longrightarrow\{R\Gamma_K(X;F)\}.
$$

Compose it with the specified representing isomorphism to $cQ$. Full faithfulness of the constant embedding makes this an actual morphism $R\Gamma_{\{x\}}(X;F)\to Q$ in $D(k)$. Its map on cohomology is the edge comparison just identified followed by the represented-system identification of the ordinary limit. It is an isomorphism in every degree, hence an isomorphism in $D(k)$.

To connect this diagram with compactly supported sections on open neighborhoods, choose $x\in V\subset K\subset U$, with $V,U$ open and $K$ compact. Proper-support extension and support inclusion give

$$
R\Gamma_c(V;F)\longrightarrow R\Gamma_K(X;F)
\longrightarrow R\Gamma_c(U;F).
$$

Such a triple can be inserted inside every prescribed neighborhood, by local compactness and the Hausdorff separation property. The composites are the original extension maps. Refining two triples inside their intersection proves that the resulting formal maps are independent of the choices and inverse to each other. Thus the two pro-systems have the same representative, and the cone above is the compact-support compatibility map used in CB. These are the proper-support extension maps already specified by that course contract.

For ordinary sections, the germ maps from the same injective resolution give a compatible cocone to $F_x$. Exact filtered colimits identify $\varinjlim_U H^q(U;F)$ with $H^q(F_x)$. A specified ind representative $P$ gives an actual map $P\to F_x$ by composing this cocone with $cP\simeq\{R\Gamma(U;F)\}$. Applying $H^q$ and SH02-FSB-REPRESENTED shows that this map is an isomorphism in every degree. This completes both compatibility statements with their original maps.

## SH02-FSB-CHECKS — Two tests for the boundary of the argument

**1. An ordinary zero limit.** Let $A_n=\bigoplus_{m\geq n}k$ with the inclusion transitions, and assume $k\ne0$. Its inverse limit is zero: a compatible element would lie in every tail of the direct sum. Nevertheless no transition map is zero, so SH02-FSB-REPRESENTED shows that the formal pro-object is nonzero. This explains why a calculation of the ordinary limit cannot replace formal stabilization.

**2. Changing coefficients.** Suppose $A\simeq cQ$ in $\operatorname{Pro}(D(k))$ and fix $M\in D(k)$. Determine the formal system obtained by applying $R\operatorname{Hom}_k(-,M)$. The answer is an ind-system represented by $R\operatorname{Hom}_k(Q,M)$, by SH02-FSB-FUNCTORS. This conclusion needs no perfectness hypothesis. Perfectness is needed for a later replacement of this Hom by $Q^\vee\otimes^L M$, and that separate statement is proved in [SH02-CB-PERFECT](../../SH02-cohomological-biduality.html#SH02-CB-PERFECT). No interchange with an ordinary inverse limit occurs in this calculation.

## SH02-FSB-REFERENCES — Scope of the supporting sources

The formal definitions and representative facts were compared with the native Stacks source at [revision a04446e57ec1](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14). Tags 05PW and 05PX specify the two Hom formulas; Tags 05PY and 05PZ characterize essentially constant systems; Tag 05SH records functorial preservation. The proof above supplies composition through natural transformations and the actual eventual inverse, including both identities. These are stronger data than the mere existence of an ordinary limit.

The ordinary cofinality statements in [Tag 04E7](https://stacks.math.columbia.edu/tag/04E7) and [Tag 002R](https://stacks.math.columbia.edu/tag/002R) have omitted proofs in that revision. SH02-FSB-REINDEX supplies the required directed-set comparison explicitly. Their ordinary-limit statements do not supply the derived comparison: SH02-FSB-COFINALITY constructs its projective resolution and comparison map, while SH02-FSB-PRISM gives the contraction needed for pro-zero systems without a countable-cofinality assumption.

[Tag 08RZ](https://stacks.math.columbia.edu/tag/08RZ) uses product cochains on strings of composable arrows to compute category cohomology. [Tag 08S0](https://stacks.math.columbia.edu/tag/08S0) describes the related Ext cochains under pointwise projective or injective hypotheses. Our proof uses the explicitly defined free representable module diagrams, their augmentation and the contraction of the upper comma sets, then proves the sheaf compatibility maps in the compact-neighborhood application below. 

For a warning about arbitrary indexing, [Tag 0ANX](https://stacks.math.columbia.edu/tag/0ANX) gives a surjective directed system with vanishing ordinary limit and nonzero first derived limit. The tail example in SH02-FSB-CHECKS has a different purpose: its transition maps are injective, and its elementary calculation separates an ordinary zero limit from a formally zero object. Neither example permits an unproved interchange of a derived functor with an inverse limit.

The application here is the exact neighborhood-system contract in SH02-CB-IMP-PRO-CALCULUS and SH02-CB-IMP-DERIVED-COFINALITY, with the actual compact-support and ordinary-section maps proved above. The prose and expanded arguments are independently written under CC0. Linked Stacks sources retain their own GFDL terms. No source chapter is incorporated, and the finite strictification, arbitrary-directed comparison and sheaf applications are not attributed wholesale to the shorter cited Stacks statements.
