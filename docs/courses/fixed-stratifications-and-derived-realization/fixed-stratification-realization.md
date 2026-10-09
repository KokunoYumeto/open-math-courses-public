# Fixed-stratification realization: strata and boundary links

A fixed stratification retains derived information precisely when its one-stratum realization functors and its boundary direct-image comparisons are equivalences. We prove the bounded-below criterion for arbitrary unital coefficient rings, calculate the obstruction on links, and work through a successful torus stratification of the projective line.

Ordinary sheaf adjunctions, injective and projective resolutions, truncation triangles and exact coproducts are prerequisites. The proof includes the needed finite gluing and comparison calculations. Equations 22–35 retain their locators in the parent lesson. This reading begins a new coefficient convention; its rings need not be commutative or have finite global dimension.

*Original AI teaching expression and solutions: GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0. Mathematical source and proof route: Lunts–Schnürer; see [Sources and reuse](#sources-and-reuse).*

## Realization for a fixed stratification

Allowing a new common triangulation and requiring one fixed stratification pose different realization questions. Valery A. Lunts and Olaf M. Schnürer's [*Categories of constructible sheaves*, Theorem 5.25](https://arxiv.org/abs/2601.05477v1) gives a criterion that separates the topology of each stratum from the derived information at its boundary. We prove that criterion here, including its bounded-below scope. These arguments concern ordinary sheaves of modules; they do not require microsupport estimates or the geometric analytic-manifold triangulation theorem.

In this section $R$ may be any associative unital ring, and modules are left modules. This broader coefficient convention applies to the results below, rather than changing the hypotheses of the earlier analytic or tensor statements. Write $\operatorname{Sh}_R(Y)$ for sheaves of $R$-modules, and $\operatorname{Loc}_R(Y)$ for locally constant sheaves with arbitrary stalk modules.

### Monodromy and the local extension condition

Suppose $Y$ is connected and locally simply connected. Fix a point and its universal covering $\pi:\widetilde Y\to Y$, with deck group $G=\pi_1(Y)$. Path transport of germs gives an exact equivalence

$$
\operatorname{Loc}_R(Y)\simeq R[G]\text{-}\operatorname{Mod}.
\tag{22}
$$

To verify it, pull a local system to the simply connected cover. A germ continues uniquely along paths, and continuation around a homotopy of paths changes nothing: cover the homotopy square by finitely many trivializing neighborhoods and compare along their edges. Thus the pullback is constant. Its deck action becomes an $R$-linear action of $G$ on the constant module. Conversely form the quotient of $\widetilde Y\times M$ by this diagonal action, and take its local sections. An evenly covered neighborhood identifies those sections with a constant module. The constructions recover the original germs and transport, and maps are precisely equivariant module maps. Kernels and cokernels are calculated in a trivializing neighborhood, proving exactness.

The inclusion into all sheaves preserves all limits and colimits. For products, use a simply connected connected neighborhood: every coordinate of a section of a product of constant sheaves is constant, so the section is a constant tuple. Colimits follow from exact constant-sheaf inverse image and sheafification on the same neighborhoods. In particular coproducts are exact.

If $Y$ has a basis of simply connected neighborhoods whose constant sheaves have zero first cohomology for every $R$-module, local systems are also closed under extensions. Indeed, on one such neighborhood $V$, apply sections to
$0\to M_V\to E\to N_V\to0$. The zero $H^1(V;M_V)$ makes the section sequence exact. Taking associated constant sheaves and comparing evaluation maps gives a morphism of short exact sequences whose two end maps are isomorphisms. Its middle map is consequently an isomorphism, so $E$ is constant there. A basis of acyclic neighborhoods suffices.

### The universal-cover criterion

**Theorem.** Let $Y$ be locally simply connected and locally acyclic for constant $R$-modules. The following conditions are equivalent:

1. Realization is an equivalence on bounded-below complexes of local systems.
2. Realization is an equivalence on bounded complexes of local systems.
3. Each component's universal covering is acyclic for every constant $R$-module.

Here acyclic means that higher sheaf cohomology is zero and degree-zero sections are the constant module. The functors in the first two conditions are

$$
D^+(\operatorname{Loc}_R(Y))\longrightarrow
D^+_{\operatorname{Loc}}(\operatorname{Sh}_R(Y)),
\qquad
D^b(\operatorname{Loc}_R(Y))\longrightarrow
D^b_{\operatorname{Loc}}(\operatorname{Sh}_R(Y)).
\tag{23}
$$

**Proof.** Components are open, so it suffices to prove the connected case. The covering direct image with finite support in its sheets, $\pi_!$, is exact and left adjoint to the exact $\pi^{-1}$. On an evenly covered neighborhood its stalk is the direct sum of the sheet stalks; this proves exactness, without pretending that an infinite covering is proper. The local system
$P=\pi_!R_{\widetilde Y}$ corresponds under (22) to the free module $R[G]$. It is a projective generator of the local-system category. Derived adjunction gives, for a local system $N$,

$$
\operatorname{Hom}_{D(\operatorname{Sh}_R(Y))}(P,N[q])
\simeq H^q(\widetilde Y;\pi^{-1}N).
\tag{24}
$$

The corresponding group in $D(\operatorname{Loc}_R(Y))$ is zero for $q>0$, by projectivity of $P$, and agrees in degree zero. Every constant module on the cover occurs among the $\pi^{-1}N$: use its trivial $G$-action. Therefore equivalence in (23), even only for bounded objects, implies condition 3.

Conversely assume condition 3. Formula (24) says that $P$ has no higher ambient Hom into any local system. A projective local system is a summand of a coproduct of copies of $P$. Derived Hom from that coproduct is the product of the individual derived Hom complexes; products of groups are exact. The same vanishing and comparison thus hold for every projective local system.

Resolve a bounded-above local-system complex by bounded-above projective local systems, and represent a bounded-below target by a bounded-below complex. The preceding vanishing computes its ambient derived Hom with the same projective resolution as its local-system derived Hom. In each total degree only finitely many degrees of a bounded-above source and a bounded-below target occur. The comparison of these double complexes, or their finite diagonal filtrations, therefore proves full faithfulness for such a source and target.

For any source complex $A$, exact coproducts give the truncation telescope

$$
\bigoplus_{n\geq0}\tau_{\leq n}A
\xrightarrow{\,1-\mathrm{shift}\,}
\bigoplus_{n\geq0}\tau_{\leq n}A
\longrightarrow A\longrightarrow
\left(\bigoplus_{n\geq0}\tau_{\leq n}A\right)[1].
\tag{25}
$$

The cohomology of its cone is $H^q(A)$: the map $1-\mathrm{shift}$ is injective on the direct sum, and its cokernel is the filtered union, eventually equal to $H^q(A)$. Realization preserves this triangle and its coproducts. Apply Hom into a bounded-below target in both categories. The already proved comparison for each bounded-above truncation, the universal property of the coproduct, and the two long exact sequences prove full faithfulness for every source with a bounded-below target.

Every bounded ambient complex with local-system cohomology is now in the image: lift its finite sequence of cohomology extensions using this full faithfulness. For a bounded-below ambient complex $F$, lift each bounded truncation $\tau_{\leq n}F$ and its transition morphism. Their telescope realizes $F$, by the same cohomology calculation as (25), and has the same lower cohomological bound. This proves essential surjectivity in $D^+$, and hence also in $D^b$. $\square$

This proof does not assert equivalence for arbitrary unbounded targets. It proves exactly the bounded and bounded-below statements, with arbitrary coefficient modules.

### The boundary comparison that must be checked

Let $\mathcal S$ be a finite stratification of a topological space $Y$ into locally closed strata, satisfying the frontier condition. Suppose each stratum is locally simply connected and locally $1$-acyclic: it has a basis of neighborhoods on which every constant module has zero first cohomology. Full local acyclicity is not required for the gluing criterion. Put
$\mathcal B_Y=\operatorname{Cons}_R(Y,\mathcal S)$. Assume also the following boundary condition:
for every stratum inclusion $s:S\hookrightarrow Y$ and every local system $L$ on $S$, the cohomology sheaves of $Rs_*L$ are $\mathcal S$-constructible. Denote realization by
$\mathcal R_Y:D^+(\mathcal B_Y)\to D^+_{\mathcal S}(Y)$.

The category $\mathcal B_Y$ is abelian with exact inclusion, by (22) on neighborhoods of the strata, and is closed under extensions by the local argument above. The boundary condition is inherited by locally closed unions: if $a:S\hookrightarrow Z$ and $e:Z\hookrightarrow Y$, then $Re_*Ra_*=Rs_*$ and $e^{-1}Re_*=\mathrm{id}$; restricting the constructible cohomology of $Rs_*L$ gives that of $Ra_*L$. It has enough injectives. For each stratum embed $F|_S$ into an injective local system $I_S$, and use adjunction to obtain

$$
F\longrightarrow\bigoplus_{S\in\mathcal S}s_*I_S.
\tag{26}
$$

At a point in $S$, the component for its own stratum is the chosen monomorphism; hence (26) is a monomorphism on every stalk. Each $s_*I_S$ is constructible by the degree-zero part of the boundary condition and injective in $\mathcal B_Y$, since restriction to $S$ is exact. The finite sum is injective. No ambient injectivity of $I_S$ is asserted.

Write $R_{\mathcal S}s_*$ for direct image derived within the constructible categories. Resolving in those categories, then comparing with an ambient injective resolution, defines the canonical map

$$
\sigma_s:\mathcal R_Y R_{\mathcal S}s_*
\longrightarrow Rs_*\mathcal R_S.
\tag{27}
$$

Both sides agree with the ordinary functor in degree zero. Their higher terms can differ.

We spell out the gluing facts needed to use (27). Restriction and extension by zero for a union of strata are exact and preserve constructibility. Direct image and exceptional restriction preserve bounded-below constructible complexes under the boundary condition. To prove the latter assertion, induct on the number of ambient strata and, inside that induction, on the number of source strata. A locally closed inclusion factors as open into its closure followed by closed. Closed direct image is exact. For an open source $Z$, choose a closed stratum $C$ of $Z$. The localization triangle on the smaller space $Z$ expresses a constructible complex by its exceptional restriction to $C$ and its restriction to $Z\setminus C$. Pushing this triangle uses inclusions with fewer source strata; the one-stratum case is the boundary condition. This proves direct-image closure. The complementary open direct image in the localization triangle then proves closed exceptional-restriction closure. For bounded-below input, truncate above any desired degree first: a right derived left-exact functor cannot carry terms above that degree into lower cohomology. The bounded argument therefore proves the same assertion degree by degree.

Consequently all four ordinary adjunctions restrict to the constructible hearts and derive there. For a closed-open pair $i:Z\hookrightarrow Y$, $j:U\hookrightarrow Y$, these derived categories have the two localization triangles

$$
j_!j^{-1}A\longrightarrow A\longrightarrow i_*i^{-1}A
\longrightarrow j_!j^{-1}A[1],
\tag{28}
$$

$$
i_*R_{\mathcal S}i^!A\longrightarrow A
\longrightarrow R_{\mathcal S}j_*j^{-1}A
\longrightarrow i_*R_{\mathcal S}i^!A[1].
\tag{29}
$$

For completeness, (28) comes from the stalkwise exact short sequence on every term. For (29), take a constructible injective $I$. The map $I\to j_*j^{-1}I$ is a split epimorphism: extend the natural map $j_!j^{-1}I\to I$ along the monomorphism $j_!j^{-1}I\to j_*j^{-1}I$, using injectivity of $I$. Restricting to $U$ identifies the extension with the inverse of the restriction unit; full faithfulness of $j_*$ shows that the resulting composite on $j_*j^{-1}I$ is the identity. Its kernel is $i_*i^!I$. Apply this degreewise to an injective resolution. All the restriction/direct/exceptional functors just used preserve the relevant injectives because their left adjoints are exact. This proves (29), including its actual adjunction maps.

The maps $\sigma$, and the analogous exceptional maps $\tau$, respect units and counits. A direct verification compares an internal injective resolution $I^\bullet$ to an ambient one $J^\bullet$: the maps are $e_*I^\bullet\to e_*J^\bullet$ and $e^!I^\bullet\to e^!J^\bullet$. Naturality of the ordinary adjunction units and counits gives the required commuting squares. Thus (29) maps to the ambient localization triangle. Its first and third terms have the canonical comparisons, and its middle map is the identity.

If $\sigma_s$ is invertible for every single stratum, it is invertible for every stratified locally closed inclusion. Here is the finite induction, to avoid assuming this extra conclusion. For an open union $Z$, split an internal injective complex and an ambient injective complex by a closed stratum $C\subset Z$ and its open complement $V$. Both decompositions are degreewise split short exact sequences as above. The comparison for $V$, already known by induction, also gives the exceptional comparison for $C$, by the morphism of localization triangles. Push the $V$-piece directly, and push the $C$-piece by open into the closed complement of $V$, followed by closed into $Y$. Both open pieces have fewer strata. Their comparisons are isomorphisms by induction; the two cohomology long exact sequences give the comparison for $Z$. Factor an arbitrary locally closed inclusion into open and closed. Derived composition is compatible with these comparisons, since the right adjoints preserve injectives. The same triangles give the exceptional comparisons.

### The full fixed-stratification criterion

**Theorem.** Under the preceding assumptions, $\mathcal R_Y$ is an equivalence if and only if, for every stratum $S$,

1. $D^+(\operatorname{Loc}_R(S))\to D^+_{\operatorname{Loc}}(S)$ is an equivalence;
2. the canonical map $\sigma_s$ in (27) is an isomorphism.

When these hold, realization on every locally closed union of strata is an equivalence too.

**Proof.** Suppose first that the two conditions hold. The localization triangles (28) filter every source object by extensions by zero $s_!A$, with $A\in D^+(\operatorname{Loc}_R(S))$. Triangles (29), iterated over a closed stratum and its complement, filter the second argument of Hom by terms $R_{\mathcal S}t_*B$. There are finitely many strata, so these are finite filtrations even for bounded-below complexes. For those two kinds of terms, adjunction gives

$$
\begin{aligned}
\operatorname{Hom}(s_!A,R_{\mathcal S}t_*B[q])
&\simeq\operatorname{Hom}(t^{-1}s_!A,B[q]),\\
\operatorname{Hom}(s_!\mathcal R_S A,Rt_*\mathcal R_T B[q])
&\simeq\operatorname{Hom}(t^{-1}s_!\mathcal R_S A,\mathcal R_T B[q]).
\end{aligned}
\tag{30}
$$

The two groups agree: restriction and zero extension commute with realization, $\sigma_t$ identifies the targets, and the one-stratum realization is fully faithful. For distinct strata the restriction $t^{-1}s_!A$ is zero; for the same stratum it is $A$. The identifications match the actual comparison maps by the unit/counit verification above. Applying the two long exact Hom sequences to the finite filtrations proves full faithfulness for arbitrary source objects.

For essential surjectivity, apply the ambient version of (28) successively. Each stratum restriction is realized by condition 1. Its zero extension is realized by the exact $s_!$, and every connecting morphism lifts by full faithfulness. Its cone lifts the next extension. The finite induction realizes the entire bounded-below object.

Conversely assume that $\mathcal R_Y$ is an equivalence. For a stratified locally closed $e:Z\hookrightarrow Y$, zero extension is fully faithful in both categories, by its open-closed factorization and adjunctions. Since it commutes with realization, realization on $Z$ is fully faithful. For an ambient object on $Z$, realize its zero extension on $Y$, then restrict the realizing object back to $Z$. This proves essential surjectivity on $Z$. Finally exact restriction $e^{-1}$ has right adjoints $R_{\mathcal S}e_*$ and $Re_*$ in the two equivalent categories. The compatibility of the adjunction bijections and Yoneda identify their canonical map $\sigma_e$ as an isomorphism. Taking $Z=S$ proves both necessary conditions. $\square$

### Links compute the obstruction

A normal structure means a finite stratification by connected manifolds with a basis of compatible local product charts

$$
V_x\simeq B_x\times\operatorname{Cone}(L_x),
\qquad
S\cap V_x\simeq B_x\times(0,\epsilon)\times L_{x,S}.
\tag{31}
$$

Here $x\in T$, $B_x\subset T$ is a ball, and each link piece $L_{x,S}$ is a manifold with finitely many connected components. The product chart is required to respect the strata. We use this as a stated topological structure; no claim that every stratification has it is implicit.

For a local system $M$ on $S$, restriction to a slice identifies it with a local system on $L_{x,S}$. The ball and open radial interval are contractible, so local-system sheaf cohomology and its restriction maps give

$$
(R^q s_*M)_x\simeq H^q(L_{x,S};M|_{L_{x,S}}).
\tag{32}
$$

One can calculate this by an acyclic cover on the link and product neighborhoods: the contractible factors change neither the local system nor the cohomology, and shrinking them induces the same comparison. The constant neighborhood system therefore computes the direct-image stalk. Within $B_x$ the same calculation is locally constant. This proves the boundary condition in this setting, rather than just assuming it.

The map $\sigma_s$ is invertible exactly when every injective local system $I$ on $S$ has

$$
H^{q}(L_{x,S};I|_{L_{x,S}})=0\qquad(q>0)
\tag{33}
$$

for all incident links. Necessity follows by applying the comparison to such an $I$: internal derived direct image is already $s_*I$. For sufficiency, (32) makes every $I$ ambient $s_*$-acyclic; its bounded-below internal injective resolution then calculates the ambient direct image as well. Thus contractible strata alone do not settle realization.

Suppose now that strata and connected link pieces have contractible universal coverings. Let $H=\pi_1(L_{x,S,i})$, $G=\pi_1(S)$, with the homomorphism induced by a slice inclusion. The universal-cover theorem identifies link cohomology with the derived invariants of the restricted $R[G]$-module. It follows from (33) that realization is an equivalence if restriction sends every injective $R[G]$-module to an $H$-invariant-acyclic module.

An injective homomorphism $H\hookrightarrow G$ satisfies this test: $R[G]$ is free as a right $R[H]$-module, so induction $R[G]\otimes_{R[H]}-$ is exact and its right adjoint, restriction, preserves injectives. Higher $H$-invariants of that injective restriction vanish.

More generally it suffices that the kernel $N$ be finite and its order be a unit in $R$. Factor through $Q=H/N\hookrightarrow G$. The restricted module is injective over $R[Q]$. The $N$-invariants functor is exact, using

$$
m\longmapsto |N|^{-1}\sum_{n\in N}n m.
\tag{34}
$$

It is also right adjoint to exact inflation from $R[Q]$, so sends $R[H]$-injectives to $R[Q]$-injectives. Apply $N$-invariants to an $R[H]$-injective resolution of the inflated $R[Q]$-injective module. Exactness gives an injective $R[Q]$-resolution, and taking $Q$-invariants has no positive cohomology. Since $H$-invariants are $Q$-invariants after $N$-invariants, the required vanishing follows. Over a field, the order-unit condition means characteristic does not divide $|N|$. For a general ring one must retain invertibility itself.

### A torus example with a genuine boundary

On $\mathbb P^1(\mathbb C)$, use the three torus-orbit strata $\mathbb C^*$, $0$, and $\infty$. A punctured disk is $(0,\epsilon)\times S^1$, providing (31) at either closed stratum. The open stratum and its link have contractible universal covers. The inclusion of the link into $\mathbb C^*$ induces an isomorphism $\mathbb Z\to\mathbb Z$, after choosing a generator. Thus the injective-homomorphism test proves

$$
D^+(\operatorname{Cons}_R(\mathbb P^1,\{\mathbb C^*,0,\infty\}))
\simeq D^+_{\{\mathbb C^*,0,\infty\}}(\mathbb P^1;R)
\tag{35}
$$

for every unital $R$, with arbitrary stalk modules. It also proves the bounded restriction of (35). A different stratification of this same space fails, as shown in [the missing-derived-classes lesson](projective-line-boundary-and-missing-classes.md). The distinction is in the actual boundary map of fundamental groups.

The general normal toric-variety result uses the same argument on each affine orbit star: a normal cone chart contracts to its closed orbit, and the orbit-link inclusion induces an injection on fundamental groups. These geometric cone charts are a separate toric-geometry input. Equation (35) supplies a complete explicit example without requiring that general input. Finite-stalk realization requires an additional finite-type argument; (35) by itself concerns the unrestricted constructible heart.

### Finite cohomology and the finite heart are different restrictions

Suppose $R$ is left Noetherian. Constructible sheaves with finitely generated stalks form an abelian subcategory closed under extensions and direct summands: take kernels, cokernels and extension sequences on stalks, where these closure properties hold for finitely generated modules over a left Noetherian ring.

An equivalence in the fixed-stratification theorem restricts to bounded objects with finitely generated cohomology stalks. Indeed realization is exact on hearts and commutes with cohomology. A source object therefore has precisely the same stalk modules in its cohomology as its realization, and essential surjectivity supplies a source object with those cohomology modules. Boundedness is detected in the same way.

This gives an equivalence between the finite-cohomology subcategory of the derived unrestricted heart and the finite-cohomology ambient category. It does not yet identify either with the derived category of the finite heart. That further comparison requires representing roofs, extensions and their relations through finite-stalk terms. The last exercise below shows why an apparently natural coefficient subcategory can lose an ambient extension.

## Further exercises on fixed realization

### A simply connected stratum can still have missing derived classes

*Difficulty: Intermediate.*

Give $S^2$ its single-stratum decomposition over a field $k$. Compute the degree-two self-morphism of the constant sheaf in the two categories in (23). Explain the failed hypothesis.

**Solution.** A local system on $S^2$ is constant, so its heart is vector spaces and the constant sheaf is projective. Its second self-morphism in the source is zero. Ambient derived adjunction identifies the target group with $H^2(S^2;k)=k$, computed by the sphere's zero- and two-cells. The universal cover is $S^2$ itself and is not acyclic. Simple connectivity supplies (22); it does not supply the higher vanishing required by (24).

### The circle retains its degree-one extension

*Difficulty: Intermediate.*

For a single-stratum circle over a field, calculate the degree-one self-extension of the trivial local system in its heart. Compare it with ambient cohomology.

**Solution.** The heart is modules over $A=k[t,t^{-1}]$. The trivial module is $k=A/(t-1)$, and
$0\to A\xrightarrow{t-1}A\to k\to0$ is a free resolution: $t-1$ is not a zero divisor, and evaluation at one is its quotient. Applying $\operatorname{Hom}_A(-,k)$ gives zero differential, hence $\operatorname{Ext}^1_A(k,k)=k$ and no higher extension. The circle's universal cover is the contractible line, so (23) identifies this with $H^1(S^1;k)=k$. A constant stalk does not remove the module's monodromy extensions.

### Averaging over a finite kernel needs an inverse

*Difficulty: Intermediate.*

Take $H=C_2\to G=\{1\}$, $R=\mathbb Z$, and the injective abelian group $I=\mathbb Q/\mathbb Z$, with trivial $H$-action. Compute $H^1(H;I)$. What algebraic hypothesis in (34) is missing?

**Solution.** A degree-one cocycle for a trivial action is a homomorphism $C_2\to I$, and all degree-one coboundaries are zero. Thus $H^1(C_2;I)=I[2]\simeq\mathbb Z/2$, nonzero, although $I$ is injective over $\mathbb Z$. Injectivity follows from divisibility, or directly from the ideal-extension criterion for $\mathbb Z$: a map from $n\mathbb Z$ extends by dividing its value by $n$. Averaging would require $1/2\in\mathbb Z$, which is absent. The example is an algebraic restriction test; it does not assert that this finite group is the fundamental group of an aspherical finite-dimensional link manifold.

### Annihilation by one ideal is different from ideal-power torsion

*Difficulty: Intermediate.*

Let $A=k[t]$, $J=(t)$, and $B=A/J=k$. Compare $\operatorname{Ext}^1_B(k,k)$ with $\operatorname{Ext}^1_A(k,k)$. Does the category of modules annihilated by $J$ inherit all its ambient derived morphisms? Does enlarging it to finite modules killed by some power of $J$ remove this particular obstruction?

**Solution.** The first group is zero because $B$ is a field. The free resolution
$0\to A\xrightarrow{t}A\to k\to0$ gives $\operatorname{Ext}^1_A(k,k)=k$. Its nonzero class is represented by
$0\to k\to A/(t^2)\to k\to0$, where the first map sends $1$ to the class of $t$. The middle module is not annihilated by $J$. Hence the subcategory of $B$-modules is not closed under ambient extensions, and its bounded realization is not full. The larger finite ideal-power-torsion category contains this middle module and the extension. This checks the distinction needed before using a finite-type realization criterion; it does not prove every higher comparison for that larger category.

## Sources and reuse

Valery A. Lunts and Olaf M. Schnürer, [*Categories of constructible sheaves*, arXiv:2601.05477v1](https://arxiv.org/abs/2601.05477v1), 9 January 2026, supplies the results and proof route: Theorem 4.1 (pp. 11–13) for one stratum; Proposition 5.24 and Theorem 5.25 (pp. 24–27) for boundary comparisons and fixed-stratification realization; Definition 6.2, Lemma 6.6, Corollary 6.8 and Theorem 6.10 (pp. 27–30) for the link test. The finite-cohomology distinction corresponds to Lemma 7.2 and Corollary 7.5 (pp. 31–32). The finite-kernel alternative here explicitly requires the kernel order to be a unit in the coefficient ring; a statement only about characteristic would not suffice for every ring allowed here.

The text, checks, exercises, solutions and reader code are dedicated under CC0. The results and the route of the proofs are those of Lunts–Schnürer, credited above; the wording, the expanded calculations and the exercises are written independently. The source and dependency notes identify the exact passages, changes and remaining prerequisites.

Ordinary derived-category formalism and the topological facts used to compute local-coefficient cohomology remain explicit prerequisites. The realization criteria use the Lunts–Schnürer results and proof route identified above; this reading does not supply a complete development of those underlying foundations.

[Reading index](README.md) · Source and dependency notes · [Reuse terms](LICENSE.txt) · Provenance
