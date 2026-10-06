# SH02-MD — Local orientations, dimension, and integration

Local unit: `SH02-MD`. Original programme text: CC0 1.0 Universal. The proofs are relative to the explicit foundational and exceptional-operation contracts below. 

An orientation records how a local compact-support class changes when its coordinates change. Keeping that record as a sheaf makes integration possible on a nonorientable manifold and makes the dimension shifts in exceptional inverse image unambiguous. We first determine the local cohomology that produces this record, then use the defining adjunction to construct the operations and their actual comparison maps.

## SH02-MD-CONTRACT — Conventions and the prerequisite boundary

Local identifier: `SH02-MD-CONTRACT`.

Except for an explicitly more general statement, $k$ is a commutative ring of finite global dimension, and all coefficients are arbitrary $k$-modules. No field, finite-generation, projectivity, constructibility or compact-support condition on the input sheaf is understood. A manifold is a finite-dimensional Hausdorff topological manifold without boundary, countable at infinity; its dimension is locally constant, and assertions involving a number $n$ concern a fixed-dimensional component or a uniform finite bound. Smoothness is imposed only in the paragraph concerning differential forms. All locally compact spaces are Hausdorff. We write

\[
H^j(K[r])=H^{j+r}(K),\qquad
\omega_f=f^!k_X\quad(f:Y\to X).
\tag{M1}
\]

Thus a compactly supported orientation class on an $n$-manifold lives in degree $n$, whereas its dualizing object lives in degree $-n$.

The [open prerequisites](open-prerequisites.md) supply sheaf exactness, injectives, derived sections and proper base change. We use the following precise additional contracts.

### SH02-MD-FOUND-SUPPORT — Proper-support foundation contract

Extension by zero for open inclusions; localization for a closed subset, also with compact supports; $Rf_!$ composition, its compact-fiber formula, and its projection formula for bounded-below coefficients over a ring of finite global dimension. For a sheaf the compact-fiber formula is $(R^qf_!F)_x=H_c^q(f^{-1}x;F)$. On a locally compact space, compactly supported cohomology is the filtered colimit of cohomology with compact closed supports. These are SH-01 foundations, with the full $!$ package also specified in [exceptional operations](exceptional-operations.md); an ordinary nonproper $*$ base-change assertion is not part of this contract.

The compact-support parts of this contract are proved in *Duality maps for constructible inverse and direct images*: open extension and the closed–open exact sequence, (C5)–(C6), the full bounded-below fibre calculation, (F6), and proper-image composition, (D2)–(D3). Those sections explicitly use locally compact Hausdorff spaces and arbitrary coefficient modules, without constructibility or finite generation. They do not depend on the later orientation or constructible-duality applications in that reading.

For completeness, compact-support localization applies to any closed subset, not only a compact one. If $i:Z\hookrightarrow X$ is closed and $j:X\setminus Z\hookrightarrow X$ is its open complement, the stalk calculation for (C6) gives $0\to j_!j^{-1}F\to F\to i_*i^{-1}F\to0$. Closed direct image is exact and preserves injectives, as the right adjoint of exact inverse image. Compact sections of $i_*G$ are precisely compact sections of $G$ on $Z$, since a compact subset of the closed subspace is compact in $X$. Applying derived compact sections to that exact sequence, and using (C5), gives the localization triangle with terms $R\Gamma_c(X\setminus Z;j^{-1}F)$, $R\Gamma_c(X;F)$ and $R\Gamma_c(Z;i^{-1}F)$. The same construction term by term gives the triangle for bounded-below complexes.

The comparison with closed supports uses one injective resolution. If $F\to I^\bullet$ is a bounded-below injective replacement, each compactly supported section of $I^r$ has a compact closed support, and finite unions make those supports a directed family. Therefore

\[
\Gamma_c(X;I^\bullet)
=\mathop{\mathrm{colim}}_{K\subset X\text{ compact}}
\Gamma_K(X;I^\bullet),
\qquad
H_c^q(X;F)=\mathop{\mathrm{colim}}_{K\subset X\text{ compact}}
H_K^q(X;F).
\tag{MC1}
\]

The second equality follows from exactness of filtered module colimits: kernels, images and the quotient giving cohomology commute with that colimit. Each closed-support complex uses the same injective replacement, so this comparison is natural in $F$ and in enlargement of the support. It neither assumes a countable cofinal sequence of compact supports nor replaces a derived inverse limit by an ordinary limit. The bounded-below projection formula is a separate operation contract, proved in the exceptional-operation reading, (EX.11), with its finite proper-support dimension and coefficient global-dimension hypotheses. It is not needed for the dimension argument (M2)–(M4).

### SH02-MD-FOUND-SOFT — Soft-resolution foundation contract

A c-soft sheaf is acyclic for compactly supported sections on open subsets; c-softness is local; on a countable-at-infinity locally compact space a c-soft sheaf is also acyclic for ordinary global sections. A flabby sheaf is c-soft and is acyclic for sections with any closed support. Their exact proof locations and the closed-support check are given next. Schapira’s *An Introduction to Sheaves on Grothendieck Topologies* (1 August 2026), §4.3, treats the same notion: its term “soft” means extension from compact subsets, which is called c-soft here. Propositions 4.3.3, 4.3.9–4.3.11 give the flabby implication, compact-support criterion, ordinary acyclicity under countability at infinity, and locality, respectively. 

The exact providers for the first three assertions are compact extension, lifting and acyclicity, (C1)–(C4), locality of c-softness, and ordinary-section lifting by a compact exhaustion, (B1). The last argument uses only a compact exhaustion and the compact lifting lemma; it applies to countable-at-infinity locally compact Hausdorff spaces, not only to the manifold applications following it. It first proves lifting across a c-soft kernel on each compact set, corrects successive lifts by global kernel sections, and glues on the exhaustion interiors. Repeating this along an injective resolution proves ordinary acyclicity. The quotient and restriction steps are proved in the same compact-support section.

Here is also the closed-support acyclicity check for a flabby sheaf $E$. Injective modules, flasque sheaves and bounded-below derived functors, Lemmas 1.1–1.2 and Proposition 1.3, prove that injectives are flabby and that a flabby sheaf has zero positive ordinary cohomology on every open subset. For a closed $Z\subset X$, put $U=X\setminus Z$ and take an injective resolution $E\to I^\bullet$. Flabbiness of each $I^r$ gives the short exact sequence of complexes

\[
0\longrightarrow\Gamma_Z(X;I^\bullet)
\longrightarrow\Gamma(X;I^\bullet)
\longrightarrow\Gamma(U;I^\bullet|_U)\longrightarrow0.
\tag{MC2}
\]

Open restriction preserves injectives, so all three complexes compute the indicated derived functors. In the long exact cohomology sequence, degrees above one vanish by the ordinary acyclicity of $E$ on $X$ and $U$. Degree one vanishes because $\Gamma(X;E)\to\Gamma(U;E)$ is surjective. This proves $H_Z^q(X;E)=0$ for every $q>0$. Apply the same argument on each open of $X$ to obtain acyclicity also for the sheaf-valued closed-support functor. The proof is valid for modules over any sheaf of associative unital rings; no coefficient-dimension bound or commutativity is used.

- `SH02-CA-INTERVAL` and `SH02-CA-CONSTANT`, proved in [extending sections on convex sets](convex-acyclicity.md), give the dimension-one bound for an arbitrary sheaf on a compact interval and the ordinary cohomology of a constant bounded-below complex on any nonempty locally closed convex set. The compact-convex extension criterion is owned and proved in that unit, not proved a second time here.
- `SH02-CON-CYLINDER`, in the cylinder-descent theorem, identifies $K\to Rq_*q^{-1}K$ for $q:B\times\mathbb R^r\to B$ and $K\in D^+(k_B)$. Only that theorem and its proof are imported here. Its proof uses compact strips, interval cohomology, proper base change and the closed-exhaustion comparison and its limit proofs; it does not use orientation or exceptional inverse image. This theorem-level dependency is therefore not circular even though later theorems in that unit use this unit.
- `SH02-EX-ADJOINT`, `SH02-EX-COMPOSITION`, `SH02-EX-BASECHANGE`, `SH02-EX-TENSOR`, `SH02-EX-HOM` and `SH02-EX-INTERNAL`, in [exceptional operations](exceptional-operations.md), construct $Rf_!\dashv f^!$, its coherent composition, its base-change morphisms, the tensor comparison and the derived internal duality isomorphism. In the internal-Hom identities the first input is $D^b$ and the second $D^+$; all uses below respect this. Closed embeddings satisfy $i_*i^!F=R\Gamma_{i(Y)}F$.

A missing verification of one of these named contracts remains a dependency obligation. The proofs below specify where it is used rather than silently replacing it by constructibility or by perfect coefficients.

## SH02-MD-DIMENSION — Dimension controls resolutions

Local identifier: `SH02-MD-DIMENSION`.

**Theorem.** Let $V$ be an $n$-dimensional real vector space. For every sheaf $F$ of abelian groups,

\[
H_c^j(V;F)=0\quad(j>n).
\tag{M2}
\]

Consequently, on an $n$-manifold $X$, every sheaf $F$ admits a c-soft resolution of length at most $n$ and a flabby resolution of length at most $n+1$. Moreover,

\[
H_c^j(X;F)=H^j(X;F)=0\quad(j>n),
\qquad
H_Z^j(X;F)=0\quad(j>n+1)
\tag{M3}
\]

for every locally closed subset $Z\subset X$. The same statements hold for sheaves of modules over any ring. No coefficient-dimension hypothesis is needed here.

*Proof.* In dimension zero the vector space is a point. In dimension one identify $V$ with $(0,1)$, and extend $F$ by zero to $[0,1]$. Its cohomology on this compact interval computes $H_c^*(V;F)$ by the compact-support localization formalism. The interval theorem gives the bound one.

For the induction step project $V\simeq\mathbb R\times\mathbb R^{n-1}$ onto the second factor. Compact-fiber base change shows that $R^bp_!F=0$ unless $b=0,1$. The spectral sequence for $R\Gamma_c\circ Rp_!$ has terms

\[
E_2^{a,b}=H_c^a(\mathbb R^{n-1};R^bp_!F)
\Longrightarrow H_c^{a+b}(V;F).
\]

Induction makes them zero for $a>n-1$; hence total degree exceeds at most $n$. This proves (M2), including its abelian-sheaf version, which is the version required for the existence theorem for $f^!$.

Take an injective, hence flabby, resolution of $F$. Let $C^n$ be its $n$th syzygy, so that its initial part is

\[
0\longrightarrow F\longrightarrow J^0\longrightarrow\cdots
\longrightarrow J^{n-1}\longrightarrow C^n\longrightarrow0.
\tag{M4}
\]

For $n=0$ read $C^0=F$. In a coordinate neighborhood $W\subset X$, every open $U\subset W$ is an open subset of $\mathbb R^n$. Open extension by zero and (M2) give $H_c^j(U;F)=0$ for $j>n$. Dimension shifting in (M4), using compact-support acyclicity of the $J^i|_U$, gives $H_c^1(U;C^n)=0$.

Here is the extension test needed at this step. If a sheaf $E$ on a locally compact space $W$ has $H_c^1(U;E)=0$ for every open $U\subset W$, then $E$ is c-soft. Given compact $K\subset W$, choose an open neighborhood $V$ with compact closure. The compact-support localization sequence for $K\subset V$ contains

\[
\Gamma_c(V;E)\longrightarrow\Gamma(K;E|_K)
\longrightarrow H_c^1(V\setminus K;E).
\]

The last group vanishes, so a section on $K$ extends with compact support in $V$ and then by zero to $W$. This proves the test. Therefore $C^n$ is c-soft in every coordinate neighborhood, and the local c-softness theorem makes it c-soft on $X$. Equation (M4) is the desired finite resolution. Its compact-support and ordinary acyclicity give both first vanishings in (M3); ordinary acyclicity here uses countability at infinity.

If $Z$ is closed in $X$, the localization sequence comparing $X$ and $X\setminus Z$ gives the supported vanishing in (M3). For locally closed $Z$, choose an open $U\subset X$ in which $Z$ is closed and use excision $H_Z^j(X;F)=H_Z^j(U;F|_U)$. This does not treat an arbitrary subset as a closed support.

Finally let $C^{n+1}$ be the next syzygy in the injective resolution. For any closed $Z\subset X$, dimension shifting with supported sections gives

\[
H_Z^1(X;C^{n+1})=H_Z^{n+2}(X;F)=0.
\]

The localization sequence consequently makes $\Gamma(X;C^{n+1})\to\Gamma(U;C^{n+1})$ surjective for every open $U$. This is flabbiness and provides a flabby resolution of length $n+1$. All arguments are module-linear and forgetting the module action preserves the relevant exactness. $\square$

On a countable-at-infinity locally compact space, c-softness also implies softness, meaning extension from every closed subset. The needed argument is useful for interpreting the sharp soft-dimension example. Choose compact sets $L_r\subset\operatorname{int}L_{r+1}$ whose interiors cover the space. Given a section $s$ on a closed subset $C$, construct compatible sections $s_r$ on $L_r$ equal to $s$ on $C\cap L_r$. If $s_r$ is constructed, it and $s|_{C\cap L_{r+1}}$ agree on the intersection of the two closed sets $L_r$ and $C\cap L_{r+1}$. Finite closed gluing, proved in `SH02-CA-CLOSED-MV`, gives a section on their compact union. C-softness extends it to the whole space; restrict the extension to $L_{r+1}$ to obtain $s_{r+1}$. Start with an extension from $C\cap L_1$. The compatible sections glue on the open cover by the interiors of the $L_r$, and the glued section restricts to $s$ on $C$. Conversely a soft sheaf is c-soft because compact subsets are closed. Thus soft and c-soft resolutions have the same minimum length on these spaces.

The dimension argument can be compared directly with [Schapira, §5.1, Lemma 5.1.1 and Proposition 5.1.2, pp. 105–106](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=105): both begin with the compact interval and project away one coordinate. Here the dimension-shifting step and the compact-support extension test are written out before truncating the resolution. The underlying support argument is module-linear, so the arbitrary-ring form of the theorem above is proved by that argument, not inferred from the source’s standing commutative coefficient convention.

These are upper bounds, not assertions of equality in every dimension. A zero-dimensional manifold is discrete, and every sheaf on it is already flabby and c-soft. A sharpness claim of $n+1$ for a point would be false.

## SH02-MD-EUCLIDEAN — The compact-support generator

Local identifier: `SH02-MD-EUCLIDEAN`.

**Theorem.** For $M\in D^+(k)$, a real vector space $V$ of dimension $n$, and $x\in V$, the evaluation map and the support-forgetting map are isomorphisms

\[
R\Gamma(V;M_V)\xrightarrow{\sim}M,
\qquad
R\Gamma_{\{x\}}(V;M_V)\xrightarrow{\sim}R\Gamma_c(V;M_V).
\tag{M5}
\]

An orientation of $V$ determines an isomorphism

\[
R\Gamma_c(V;M_V)\simeq M[-n].
\tag{M6}
\]

A linear automorphism acts on this complex by the sign of its determinant. This statement concerns the actual pullback automorphism, not just an unspecified automorphism of its cohomology groups.

*Proof.* The first assertion is the constant-coefficient convex theorem. For the compact-support calculation in dimension one, work on $I=[0,1]$ with $j:(0,1)\hookrightarrow I$. The exact localization triangle is

\[
j_!M_{(0,1)}\longrightarrow M_I\longrightarrow
M_{\{0\}}\oplus M_{\{1\}}\longrightarrow.
\]

After applying $R\Gamma(I;-)$, its middle map is the diagonal $M\to M\oplus M$. The difference map $(a,b)\mapsto b-a$ identifies its cokernel complex with $M$. It follows, functorially in a bounded-below complex $M$, that the first term is $M[-1]$. Reversing the coordinate exchanges the endpoints and changes this difference by $-1$.

For $\mathbb R^n$ use its ordered coordinate projections, compact-fiber base change and the $!$ projection formula. Integrating one coordinate at a time gives $M[-n]$. The generator is the external product, in coordinate order, of the degree-one generators just fixed. This specifies the Künneth convention and the shift, including coefficients that are neither flat nor finitely generated. Alternatively one may first perform the calculation for a module, and then use the bounded-below spectral sequence; the uniform dimension bound (M2) makes this passage legitimate.

We justify the support comparison in (M5). Translate $x$ to zero, and write $B_r$ for the closed ball of radius $r>0$. Both $V\setminus\{0\}$ and $V\setminus B_r$ retract onto a sphere of radius larger than $r$, so restriction between their constant-complex cohomologies is an isomorphism. The homotopy invariance used here follows from a proper argument: projection $T\times[0,1]\to T$ is proper and has constant-complex fiber cohomology $M$, by the natural bounded-below interval evaluation theorem; proper-fibre comparison with the section-restriction map identifies its unit with an isomorphism. Both endpoint restrictions are inverses to that unit. A homotopy therefore induces identical maps on constant-complex cohomology. No nonproper fiber base change is invoked.

Compare the two localization triangles for $\{0\}$ and $B_r$. The restriction just proved and the identity on $R\Gamma(V;M_V)$ show that $R\Gamma_{\{0\}}(V;M_V)\to R\Gamma_{B_r}(V;M_V)$ is an isomorphism. Compact balls are cofinal among compact subsets of $V$, so the compact-support colimit proves the second assertion of (M5).

The same homotopy argument says that the action on compact-support cohomology is constant along a path of linear automorphisms. Indeed their homotopy is proper over a compact path parameter: the norms of the inverse linear maps have a uniform bound. Positive-determinant matrices are path connected to the identity; negative-determinant matrices are path connected to reflection in one coordinate. One can see this through a positive-definite polar factor followed by elementary rotations of the orthogonal factor. The reflection acts by $-1$ in its one-dimensional factor, so the two actions are respectively $+1$ and $-1$. Any two positively oriented linear coordinate systems thus give the same (M6). $\square$

### SH02-MD-ORIENTATION-LINE — Orientation as a local system

For an $n$-manifold $X$, define its integral orientation sheaf by sheafifying

\[
U\longmapsto\operatorname{Hom}_{\mathbb Z}
\bigl(H_c^n(U;\mathbb Z),\mathbb Z\bigr),
\tag{M7}
\]

where restriction is dual to extension of compact supports. Denote it by $o_X^{\mathbb Z}$. On a coordinate ball the preceding theorem identifies it with $\mathbb Z$. This identification is compatible with passage to smaller coordinate balls: pick a point in the smaller ball and compare both compact-support groups with its local cohomology as in (M5). Those comparison maps are isomorphisms and commute with extension. Thus the transition functions are $\pm1$ and (M7) is locally constant of rank one.

There is a canonical perfect pairing $o_X^{\mathbb Z}\otimes o_X^{\mathbb Z}\to\mathbb Z_X$: for a local generator $e$ put $e\otimes e\mapsto1$. Replacing $e$ by $-e$ leaves the rule unchanged, so the rules glue. The resulting identification with its dual is canonical; it does not require choosing an orientation. The same argument proves this fact for every sheaf $L$ locally isomorphic to $\mathbb Z_X$ on an arbitrary topological space. Since internal Hom from $L$ is exact locally, its derived dual is concentrated in degree zero as well: $R\mathcal Hom(L,\mathbb Z_X)\simeq L$ canonically.

Put $o_X=k_X\otimes_{\mathbb Z}o_X^{\mathbb Z}$. There is no derived-Tor correction, since the integral line is locally free. We obtain

\[
o_X\otimes_k o_X\simeq k_X,
\qquad \mathcal Hom_k(o_X,k_X)\simeq o_X.
\tag{M8}
\]

The analogous claim would be false for an arbitrary invertible $k$-module local system: the integral sign structure, not merely rank one over $k$, supplies (M8).

At a point $x$ the same construction gives canonical identifications

\[
(o_X)_x\simeq\operatorname{Hom}_k(H^n_{\{x\}}(X;k),k)
\simeq H^n_{\{x\}}(X;k).
\tag{M9}
\]

The last isomorphism uses the integral square pairing; it is not a claim that arbitrary modules identify canonically with their duals. Sheafifying $U\mapsto\operatorname{Hom}_k(H_c^n(U;k),k)$ gives the same $o_X$, because the asserted agreement can be checked on coordinate balls.

## SH02-MD-SUBMERSION — Recovering the exceptional inverse image locally

Local identifier: `SH02-MD-SUBMERSION`.

A continuous map $f:Y\to X$ of locally compact spaces is a topological submersion of fiber dimension $d$ if each $y$ has a neighborhood $V$ mapped onto an open $U\subset X$ and a homeomorphism $V\simeq U\times\mathbb R^d$ over $U$. Surjectivity of $f$ itself is not required. A differentiable submersion has this property by the local submersion theorem.

**Theorem.** Such a map has proper direct image of cohomological dimension at most $d$ on abelian sheaves. Its relative dualizing object is a shifted sign line,

\[
\omega_f\simeq o_f[d],\qquad
H^j(\omega_f)=0\quad(j\ne-d),\qquad
H^{-d}(\omega_f)=o_f.
\tag{M10}
\]

For every $G\in D^+(k_X)$, the canonical tensor comparison is an isomorphism

\[
\omega_f\otimes_k^L f^{-1}G\xrightarrow{\sim}f^!G.
\tag{M11}
\]

Here $o_f$ is locally $k_Y$ with its integral sign structure. An integral orientation of $f$ is a trivialization of $o_f^{\mathbb Z}$; it induces a trivialization over $k$. A trivialization only over $k$ is a coefficient orientation and need not come from an integral orientation. In particular all tensor products with $o_f$ are exact.

*Proof.* The dimension bound is a compact-support statement on the manifold fibers. The proof of (M2) and the c-soft-resolution argument are local for compact supports and therefore apply to each locally Euclidean fiber; the ordinary-cohomology step in (M3) is unnecessary. Compact-fiber base change gives the claimed bound for $f_!$ on abelian sheaves. Hence the adjoint exists by SH02-EX-ADJOINT.

First take $a:\mathbb R^d\to\{\mathrm{pt}\}$. On any coordinate ball $B$ adjunction gives

\[
R\Gamma(B;a^!k)
\simeq R\operatorname{Hom}_k(R\Gamma_c(B;k),k)
\simeq k[d].
\tag{M12}
\]

These isomorphisms are natural for restriction in $B$, dual to extension of compact supports. The computation and naturality following (M7) show that $a^!k$ has just its locally constant orientation line in degree $-d$.

For the product projection $p:U\times\mathbb R^d\to U$, the exceptional base-change morphism and its defining transpose and the normalized tensor comparison give a canonical morphism

\[
\operatorname{pr}_{\mathbb R^d}^{-1}\omega_a
\otimes p^{-1}G\longrightarrow p^!G.
\tag{M13}
\]

We check this very morphism on a basis of rectangles $A\times B$, with $A\subset U$ open and $B$ a coordinate ball in $\mathbb R^d$. Bounded-first-input internal adjunction and the compact-support calculation identify the sections of the target with

\[
\begin{aligned}
R\Gamma(A\times B;p^!G)
&\simeq R\operatorname{Hom}_{k_U}(Rp_!k_{A\times B},G)\\
&\simeq R\operatorname{Hom}_{k_U}(k_A[-d],G)\\
&\simeq R\Gamma(A;G)[d].
\end{aligned}
\tag{M14}
\]

Here $k_A$ denotes open extension by zero. The $!$ projection formula and the ordered compact-support generator specify the middle isomorphism. On the source of (M13), the cylinder theorem and the local trivialization of $\omega_a$ give the same $R\Gamma(A;G)[d]$. By its construction as the mate of projection followed by trace, (M13) is identified under (M14) with the identity: its pairing with $k_A[-d]$ is evaluation of the chosen compact-support generator against its dual in (M12). Thus it is an isomorphism on all these rectangles, and hence on stalk cohomology.

Taking $G=k_U$ first identifies the exceptional-base-change arrow with $\omega_p\simeq\operatorname{pr}_{\mathbb R^d}^{-1}\omega_a$. Equation (M13) then proves that the actual tensor comparison (M11) is an isomorphism for $p$. The constructions commute with restriction, so product charts prove (M10) and (M11) for $f$ and glue their comparison maps without a global orientation choice. $\square$

The corresponding statement is [Schapira, Proposition 5.1.9, pp. 107–108](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=107), where the input is bounded below and the proof tests open rectangles. In (M12)–(M14) the compact-support generator also identifies the actual comparison map through its adjoint evaluation. This extra map check is needed later for the sign of trace and for composition; an abstract local isomorphism of objects alone would not determine those maps.

### SH02-MD-COEFFICIENTS — Changing coefficients

For a topological submersion, the same chart calculation over $\mathbb Z$ and over $k$ gives canonical coefficient-change identifications

\[
o_f\simeq k_Y\otimes_{\mathbb Z}o_f^{\mathbb Z},
\qquad
\omega_f\simeq k_Y\otimes_{\mathbb Z}^L\omega_f^{\mathbb Z}.
\tag{M15}
\]

They agree on overlaps because the transition is the same integral local-degree sign. Consequently $o_f\otimes o_f\simeq k_Y$ and $o_f^\vee\simeq o_f$, with the canonical square pairing just proved. These statements do not assert coefficient change for an arbitrary non-submersive map without further argument.

## SH02-MD-RELATIVE — Relative dimensions, graph supports, and coordinate changes

Local identifier: `SH02-MD-RELATIVE`.

Suppose $p_Y:Y\to S$ and $p_X:X\to S$ are topological submersions of dimensions $n$ and $m$, and $f:Y\to X$ satisfies $p_Xf=p_Y$. The map $f$ need not itself be a submersion. Its fibers are closed subsets of the $n$-dimensional fibers of $p_Y$: a fiber over $x$ lies in $p_Y^{-1}(p_X(x))$ and is closed there because $X$ is Hausdorff. Closed extension of a fiber sheaf and the compact-support bound therefore give cohomological dimension at most $n$ for $f_!$, so $f^!$ is defined. Then

\[
\begin{aligned}
\omega_f&\simeq\omega_{p_Y}\otimes f^{-1}\omega_{p_X}^{-1}\\
&\simeq o_{p_Y}\otimes f^{-1}o_{p_X}[n-m].
\end{aligned}
\tag{M16}
\]

Here the tensor inverse is also the internal derived dual: $\omega_f^{-1}=R\mathcal Hom_k(\omega_f,k_Y)$. The inverse of $L[r]$, for a sign line $L$, is $L[-r]$. We define

\[
o_{Y/X}=o_{p_Y}\otimes f^{-1}o_{p_X},
\qquad \dim(Y/X)=n-m.
\tag{M17}
\]

For maps of manifolds take $S$ to be a point. In particular the relative dimension is signed; for an embedding of codimension $c$ it is $-c$.

*Proof.* Composition gives $f^!\omega_{p_X}=\omega_{p_Y}$. An invertible shifted local system can be moved through $f^!$: the tensor comparison is an isomorphism locally where that local system is the tensor unit with a shift, hence everywhere. It follows that

\[
f^!\omega_{p_X}\simeq f^!k_X\otimes f^{-1}\omega_{p_X}.
\]

Cancel its invertible final factor. This proves (M16), with its actual isomorphism obtained from composition and tensor comparison. This cancellation never replaces an arbitrary complex by its double dual. $\square$

The same proof, before setting the input equal to $k$, gives a useful variant. If $f:Y\to X$ is a submersion of dimension $d$, $g:Z\to Y$ is continuous, and $fg$ is a submersion of dimension $e$, then for $F\in D^+(k_X)$,

\[
g^!f^{-1}F\simeq(fg)^{-1}F\otimes o_{fg}\otimes g^{-1}o_f[e-d].
\tag{M18}
\]

Indeed $f^{-1}F=f^!F\otimes o_f[-d]$; move the invertible final factor through $g^!$ and use $(fg)^!=g^!f^!$ and (M11).

For another map $g:Z\to Y$ over $S$, with $p_Z$ also a topological submersion, the composition identifications are

\[
\omega_{Z/X}\simeq\omega_{Z/Y}\otimes g^{-1}\omega_{Y/X},
\qquad
 o_{Z/X}\simeq o_{Z/Y}\otimes g^{-1}o_{Y/X}.
\tag{M19}
\]

Our order is fixed by (M16): write each dualizing factor as $\omega_{p_Z}\otimes g^{-1}\omega_{p_Y}^{-1}$ and cancel the adjacent $\omega_{p_Y}^{-1}\otimes\omega_{p_Y}$. All further rearrangements of shifted complexes use the Koszul symmetry; exchanging shifts $[a]$ and $[b]$ contributes $(-1)^{ab}$. The corresponding unshifted orientation-line formula is the one induced by this ordered convention. For three composable maps both cancellation orders agree, because the composed counit defining exceptional composition is associative. Thus (M19) is a coherent comparison, not a separately chosen isomorphism for each pair.

### SH02-MD-GRAPH — Graph support and relative orientation

Every continuous map of manifolds $f:Y\to X$ has graph factorization

\[
Y\xrightarrow{j}Y\times X\xrightarrow{p}X,
\qquad j(y)=(y,f(y)).
\]

The graph is closed because $X$ is Hausdorff. Let $q:Y\times X\to Y$ be the other projection. For every $F\in D^+(k_X)$,

\[
f^!F\simeq j^{-1}R\Gamma_{j(Y)}(p^{-1}F)
\otimes o_Y[\dim Y].
\tag{M20}
\]

*Proof.* The submersion formula gives $p^!F=p^{-1}F\otimes q^{-1}o_Y[\dim Y]$. Now $f^!=j^!p^!$, and $j^!=j^{-1}R\Gamma_{j(Y)}$. The orientation factor is locally free and can be taken out of this support functor. Restrict it along $j$, obtaining (M20). $\square$

Taking $F=k_X$ in (M20) and comparing with (M16) shows that the sheaf $R\Gamma_{j(Y)}k_{Y\times X}$, restricted to the graph, has a single nonzero cohomology sheaf, in degree $\dim X$, and

\[
o_{Y/X}\simeq j^{-1}\mathcal H^{\dim X}_{j(Y)}(k_{Y\times X})\otimes o_Y.
\tag{M21}
\]

For the identity map, whose graph is the diagonal $\Delta\subset X\times X$, this yields

\[
o_X\simeq\bigl(\mathcal H^n_\Delta(k_{X\times X})\bigr)|_\Delta,
\qquad n=\dim X.
\tag{M22}
\]

Thus orientation can be recovered from diagonal support without differentiability or a tubular-neighborhood choice.

### SH02-MD-CLOSED — The closed-embedding comparison

If $i:Y\hookrightarrow X$ is a closed submanifold of codimension $c$, (M16) gives

\[
i^!k_X\simeq o_{Y/X}[-c],
\qquad R\Gamma_Yk_X\simeq i_*o_{Y/X}[-c].
\tag{M23}
\]

For a locally closed submanifold, apply this formula in an open set where it is closed and use excision. The absolute dual of its extended constant sheaf is

\[
R\mathcal Hom_X(i_*k_Y,\omega_X)\simeq i_*\omega_Y
\tag{M24}
\]

for the closed inclusion. This is `SH02-EX-INTERNAL` together with $i^!\omega_X=\omega_Y$; it is not a biduality assertion about arbitrary sheaves. For a locally closed inclusion the corresponding statement uses its proper direct image on the left and ordinary derived direct image on the right, as required by that duality theorem.

### SH02-MD-SMOOTH-SIGN — Submersion signs

For an oriented differentiable $n$-manifold, the positively oriented coordinate generators trivialize $o_X$, and reversing the orientation multiplies the trivialization by $-1$. To verify that positive coordinate changes preserve the generator, it suffices to check a germ $h$ at zero with $h(0)=0$. Write $A=dh_0$. For a sufficiently small ball,

\[
|h(x)-Ax|\le\tfrac12\|A^{-1}\|^{-1}|x|.
\]

The straight interpolation $h_t(x)=Ax+t(h(x)-Ax)$ has no zero away from zero on that ball. It therefore gives a homotopy of maps of pairs into $(\mathbb R^n,\mathbb R^n\setminus\{0\})$. The proper-interval homotopy argument in (M5), applied to the corresponding localization triangles, makes the induced local-cohomology map constant in $t$. At $t=0$ the map is linear and acts by $\operatorname{sgn}\det A$. A positive determinant consequently acts by $+1$, and a negative determinant by $-1$. Notice that the intermediate maps need not be diffeomorphisms: their nonzero-away-from-zero property is exactly what the map of pairs requires.

## SH02-MD-TRACE — Trace, orientation of ray spheres, and ordinary descent

Local identifier: `SH02-MD-TRACE`.

For any map for which the adjoint is defined, trace means its counit

\[
\epsilon_f:Rf_!f^!G\longrightarrow G.
\tag{M25}
\]

For a submersion, (M11) and the projection formula express it as integration against $\omega_f$:

\[
Rf_!(f^{-1}G\otimes\omega_f)
\simeq G\otimes Rf_!\omega_f
\xrightarrow{1\otimes\epsilon_f(k)}G.
\tag{M26}
\]

The placement of the factors in this display is obtained from our fixed tensor order by the usual graded symmetry. On an oriented coordinate fiber $\mathbb R^d$, the generator from (M6) and its dual in (M12) identify $R\Gamma_c(\mathbb R^d;\omega_f)$ with $k$; (M25) is the identity on $k$ under that identification. In particular an increasing interval has $\omega=k[1]$ and trace $R\Gamma_c(I;k[1])\to k$ equal to $+1$.

These local normalizations determine the following compatibilities at the level of morphisms.

**Composition.** For $Z\xrightarrow{g}Y\xrightarrow{f}X$, identify $R(fg)_!=Rf_!Rg_!$ and $(fg)^!=g^!f^!$. Then

\[
\epsilon_{fg}=\epsilon_f\circ Rf_!(\epsilon_g(f^!G)).
\tag{M27}
\]

This follows directly by composing the two adjunction bijections: the identity of $g^!f^!G$ is sent first to $\epsilon_g(f^!G)$, then to the right side of (M27). The counit of the composite is, by definition, the image of that same identity. Thus iterated integration and one-step integration agree with the ordered relative-orientation identifications (M19).

**Base change for submersions.** In a cartesian square obtained by pulling back a topological submersion $f:Y\to X$ along $u:X'\to X$, write $v:Y'\to Y$ and $f':Y'\to X'$. The exceptional comparison

\[
v^{-1}\omega_f\longrightarrow\omega_{f'}
\tag{M28}
\]

is an isomorphism: in product charts it is the same integral fiber-orientation generator, as checked in (M14). Under $!$ base change, $u^{-1}Rf_!\omega_f\simeq Rf'_!v^{-1}\omega_f$, the pullback of $\epsilon_f(k)$ is $\epsilon_{f'}(k)$. Indeed the defining transpose (EX.18) says precisely that applying proper direct image to the exceptional comparison and then taking trace equals the pullback of the original trace, under the $!$ base-change isomorphism. Local coordinates confirm that it preserves the positive-interval normalization. This statement does not assert an orientation base-change isomorphism for a general non-submersive cartesian square.

**Open extension.** For an open inclusion $j:U\hookrightarrow Y$, the trace for $j$ is extension of compact supports. Equation (M27) consequently says that integration of an extended class from $U$ equals integration on $U$. No compactness of $U$ or properness of its inclusion is needed.

For the projection $a_X:X\to\{\mathrm{pt}\}$ of an $n$-manifold, trace gives the integration homomorphism

\[
\int_X:H_c^n(X;o_X)\longrightarrow k.
\tag{M29}
\]

It is available even when $X$ is nonorientable. An orientation is needed to replace the coefficient sheaf $o_X$ by the constant sheaf $k_X$, not to define (M29).

### SH02-MD-SPHERE — Orientations of ray spheres

Let $E\to B$ be a real vector bundle of rank $n\ge1$, and let $S(E)=(E\setminus0)/\mathbb R_{>0}$ be its bundle of rays. Its fibers are spheres of dimension $n-1$. Write $o(E)$ for the integral-sign local system on $B$ defined by vector-bundle frames, with coefficients in $k$; its pullback to $E$ is $o_{E/B}$. On a local choice of norm, represent rays by unit vectors and order the radial decomposition by

\[
\mathbb R\cdot e\ \oplus\ T_{[e]}S(E)\longrightarrow E_b,
\qquad (t,v)\longmapsto te+v,
\tag{M30}
\]

with the radial direction $e$ positive and placed first. This gives $o_{S(E)/B}\simeq\pi^{-1}o(E)$. Changing the norm moves between sections of the positive-ray bundle through positive radial rescaling and preserves the local-degree generator; hence the identification is independent of the auxiliary norm. In rank one it says that the two points of each ray sphere inherit opposite signs from an orientation of the line, in agreement with the boundary-orientation convention.

The dual-basis correspondence between frames of $E$ and $E^*$ identifies $o(E^*)$ with $o(E)$. A change of frame has determinant $a$ on $E$ and determinant $a^{-1}$ on its dual; both have the same sign, so the identifications glue and give a canonical pairing

\[
o(E)\otimes o(E^*)\longrightarrow k_B.
\tag{M31}
\]

For any nonzero vector $v\in E_b$, the positive ray hemisphere $\{[\xi]:\langle v,\xi\rangle>0\}\subset S(E_b^*)$ is an open $(n-1)$-ball. It inherits the orientation line of the sphere by open restriction. The trace-normalized compact-support identity is therefore

\[
R\Gamma_c\bigl(\{[\xi]:\langle v,\xi\rangle>0\};
\omega_{S(E_b^*)}\bigr)\xrightarrow{\sim}k,
\tag{M32}
\]

with trace $+1$. The same holds in families on any open locus where $v$ is a nonvanishing section. This follows from submersion base change and open-extension compatibility; it makes the degree $n-1$ of compact supports cancel the shift $[n-1]$ of the relative dualizing object. If a convolution moves an orientation factor past another shifted factor, that rearrangement still carries its Koszul sign. Equation (M32) does not license discarding that sign.

### SH02-MD-INTEGRAL-DETECTION — Detecting cohomology with integral coefficients

We record the algebraic fact needed to characterize trace by ordinary fiber cohomology. For a bounded complex $C$ of abelian groups,

\[
R\operatorname{Hom}_{\mathbb Z}(C,\mathbb Z)=0
\quad\Longrightarrow\quad C=0.
\tag{M33}
\]

This is a conservativity assertion; no evaluation $C\to C^{**}$ is asserted to be an isomorphism.

*Proof.* First suppose an abelian group $A$ has both $\operatorname{Hom}(A,\mathbb Z)=0$ and $\operatorname{Ext}^1(A,\mathbb Z)=0$. A finite cyclic subgroup $T\subset A$ would force a surjection $\operatorname{Ext}^1(A,\mathbb Z)\to\operatorname{Ext}^1(T,\mathbb Z)$, since $\mathbb Z$ has global dimension one; the latter group is nonzero. Thus $A$ is torsion free. For $m\ge1$, apply $\operatorname{Hom}(-,\mathbb Z)$ to

\[
0\longrightarrow A\xrightarrow{m}A\longrightarrow A/mA\longrightarrow0.
\]

The two vanishings give $\operatorname{Ext}^1(A/mA,\mathbb Z)=0$. A nonzero bounded torsion group has a nonzero finite cyclic subgroup, and the preceding surjection argument would again contradict this. Hence $A=mA$ for every $m$: $A$ is a rational vector space. If nonzero, it contains a direct summand isomorphic to $\mathbb Q$, so it remains to note that $\operatorname{Ext}^1(\mathbb Q,\mathbb Z)\ne0$.

Here is a direct verification of that last assertion. In the injective resolution $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$, the cokernel of

\[
\operatorname{Hom}(\mathbb Q,\mathbb Q)
\longrightarrow\operatorname{Hom}(\mathbb Q,\mathbb Q/\mathbb Z)
\]

is $\operatorname{Ext}^1(\mathbb Q,\mathbb Z)$. The left group is countable. The right group is uncountable: already maps from $\mathbb Z[1/2]$ sending $1$ to zero are specified by arbitrary compatible binary-root choices for the images of $1/2^r$, and these maps extend to $\mathbb Q$ because $\mathbb Q/\mathbb Z$ is divisible, hence injective. Thus that cokernel is nonzero. This proves $A=0$.

For a bounded complex, the universal-coefficient spectral sequence over $\mathbb Z$, of global dimension one, gives short exact sequences

\[
0\to\operatorname{Ext}^1(H^{1-j}(C),\mathbb Z)
\to H^jR\operatorname{Hom}(C,\mathbb Z)
\to\operatorname{Hom}(H^{-j}(C),\mathbb Z)\to0.
\]

If all middle groups vanish, both end groups vanish for every cohomology group of $C$. The group result then gives $H^r(C)=0$ for every $r$. $\square$

### SH02-MD-ACYCLIC-SUBMERSION — Descent along cohomologically acyclic submersions

**Theorem.** For a topological submersion $f:Y\to X$ of fixed finite fiber dimension, the following are equivalent over $\mathbb Z$:

1. The trace $Rf_!\omega_f^{\mathbb Z}\to\mathbb Z_X$ is an isomorphism.
2. For each $x\in X$, the fiber trace $R\Gamma_c(Y_x;\omega_{Y_x}^{\mathbb Z})\to\mathbb Z$ is an isomorphism.
3. For each $x\in X$, the constant-section unit $\mathbb Z\to R\Gamma(Y_x;\mathbb Z)$ is an isomorphism.

If these conditions hold, then for every $F\in D^+(k_X)$ the ordinary adjunction unit is an isomorphism

\[
F\xrightarrow{\sim}Rf_*f^{-1}F.
\tag{M34}
\]

*Proof.* Submersion base change identifies the stalks of the first trace with the second traces; hence 1 and 2 are equivalent. For a fiber $M=Y_x$, put $C=R\Gamma_c(M;\omega_M^{\mathbb Z})$. This is a bounded complex, by the compact-support dimension bound and the shift of the orientation line. Internal duality and invertibility of $\omega_M$ identify

\[
R\operatorname{Hom}_{\mathbb Z}(C,\mathbb Z)
\simeq R\Gamma\bigl(M;R\mathcal Hom(\omega_M,\omega_M)\bigr)
\simeq R\Gamma(M;\mathbb Z).
\tag{M35}
\]

Under this identification, the dual of the trace is the constant-section unit: this is the unit–counit identity in the internal adjunction, or directly the identity section of $R\mathcal Hom(\omega_M,\omega_M)$. If the trace is an isomorphism, so is its dual. Conversely, if its dual is an isomorphism, the cone of the trace has zero derived integral dual; (M33) makes that cone zero. This proves 2 equivalent to 3 without invoking arbitrary reflexivity.

Coefficient change (M15), the $!$ projection formula and condition 1 give $Rf_!\omega_f\simeq k_X$, with the resulting isomorphism still the trace. Invertibility of $\omega_f$ and (M11) yield

\[
\begin{aligned}
Rf_*f^{-1}F
&\simeq Rf_*R\mathcal Hom(\omega_f,f^!F)\\
&\simeq R\mathcal Hom(Rf_!\omega_f,F)\\
&\simeq F.
\end{aligned}
\tag{M36}
\]

The first internal-Hom argument $\omega_f$ is bounded, so the stated exceptional duality contract applies even for unbounded-above $F\in D^+$. Tracking evaluation through its adjunction shows that the composite of the unit in (M34) with (M36) is precomposition with the trace $Rf_!\omega_f\to k_X$, hence the identity after the trace identification. Thus (M34) is the actual isomorphism claimed. No ordinary nonproper fiber-base-change step appears in this proof. $\square$

Condition 3 excludes empty fibers, disconnected fibers, and higher integral cohomology. For a vector bundle, each fiber is a nonempty vector space and the conditions hold by (M5). For a sphere bundle of positive-dimensional fibers they fail, even when the bundle is locally trivial and oriented.

## SH02-MD-DENSITIES — Differential-form normalization and bounds for derived Hom

Local identifier: `SH02-MD-DENSITIES`.

Suppose $X$ is a smooth $n$-manifold and $k=\mathbb C$. The de Rham resolution, an explicit SH-01 prerequisite, identifies $o_X$ with the complex of smooth forms tensored with $o_X$. Its terms are c-soft, so

\[
H_c^n(X;o_X)\simeq
\frac{\Gamma_c(X;\Omega_X^n\otimes o_X)}
{d\Gamma_c(X;\Omega_X^{n-1}\otimes o_X)}.
\tag{M37}
\]

A top-degree twisted form is a density, and its ordinary analytic integral vanishes on the displayed exact forms by Stokes's theorem. Under the normalization in (M6), the induced functional in (M37) is exactly the trace (M29).

Here is the sign check. On an oriented real line, choose a smooth function $u$ equal to zero far to the left and one far to the right, with compactly supported derivative. The connecting class of endpoint values $(0,1)$ in the interval calculation is represented in de Rham cohomology by $du$, and its integral is $1$. Thus the difference convention $b-a$ in (M6) matches analytic integration. In $\mathbb R^n$ take the external product of $n$ such forms in the order $dx_1,\ldots,dx_n$. Its integral is $1$ by iterated integration, and it represents the ordered compact-support generator used in (M6). Pairing it with the dual orientation generator gives trace $1$ by (M12) and (M25). Therefore the two functionals agree on an oriented coordinate ball.

For a general compactly supported density, take a finite partition of unity on a finite coordinate-ball cover of its support and decompose the density into chart-supported densities. Both functionals are additive and commute with open extension, by (M27) for trace and by the definition of the analytic integral for densities. Equality on the chart pieces proves equality globally, including nonorientable $X$. This argument specifies the sign; saying only that the two nonzero functionals differ by a scalar would not determine it.

### SH02-MD-HOMOLOGICAL-DIMENSION — Bounds for derived Hom

**Theorem.** Let $X$ be an $n$-dimensional manifold and let $A$ be an associative unital ring, with left global dimension $g$. Then the homological dimension of the abelian category of sheaves of left $A$-modules satisfies

\[
\operatorname{hd}\operatorname{Mod}(A_X)\le 3n+g+1.
\tag{M38}
\]

If $g=\infty$, this is a vacuous inequality. No noetherian hypothesis is present. In particular the theorem retains its arbitrary-ring statement even though the later tensor calculus uses a commutative coefficient ring.

*Proof.* Assume $g<\infty$ and take sheaves $F,G$ of left $A$-modules. Write $q_1,q_2:X\times X\to X$ for the projections, $\delta:X\to X\times X$ for the diagonal, and set

\[
K=R\mathcal Hom_A(q_2^{-1}G,q_1^!F),
\]

a complex of abelian sheaves on $X\times X$. The exceptional construction and its adjunction apply to sheaves of left modules over an associative ring as well; the orientation factor is an integral rank-one local system and therefore requires only tensoring over $\mathbb Z$. No tensor product of two left $A$-modules is used in this argument.

Exceptional inverse-image compatibility with internal Hom gives

\[
\delta^!K\simeq R\mathcal Hom_A(G,F),
\tag{M39}
\]

because $q_2\delta=q_1\delta=\operatorname{id}_X$. The first internal-Hom input is a sheaf and hence bounded, as required. On a rectangle $U\times V$ the internal adjunction and the $!$ product formula give

\[
R\Gamma(U\times V;K)
\simeq R\operatorname{Hom}_A
\bigl(R\Gamma_c(V;G),R\Gamma(U;F)\bigr).
\tag{M40}
\]

More explicitly, push the internal Hom along $q_1$ using its exceptional adjunction. The object $Rq_{1!}q_2^{-1}(G|_V)$ is the constant complex on $U$ associated to $R\Gamma_c(V;G)$ by $!$ base change from a point. The adjunction between constant sheaves and global sections then gives (M40). This derivation works with $A$-linear Hom throughout and checks the associative-ring case directly.

Both coefficient complexes in (M40) have cohomology in degrees $0$ through $n$, by (M3). For modules, $\operatorname{Ext}_A^j$ vanishes for $j>g$. Filtering each bounded coefficient complex by its cohomology, or using bounded projective and injective resolutions, therefore shows that the right side of (M40) has no cohomology above $n+g$. The signs in this estimate are worth making explicit: a first-input group in degree $a\ge0$ and a second-input group in degree $b\le n$ can contribute only in degree $b-a+e\le n+g$, where $0\le e\le g$. Since rectangles form a basis, sheafification gives

\[
\mathcal H^j(K)=0\quad(j>n+g).
\tag{M41}
\]

The complex is also bounded below; for example $q_1^!F$ is a sheaf shifted by $[n]$, and internal Hom from a sheaf is left exact before deriving. We may thus use the supported hypercohomology spectral sequence.

By (M39), the groups we wish to bound are

\[
\operatorname{Ext}_{A_X}^j(G,F)
\simeq H_\Delta^j(X\times X;K).
\tag{M42}
\]

This is cohomology **with support in the diagonal**, not ordinary cohomology of the product. Applied to the $2n$-manifold $X\times X$, (M3) bounds the support-cohomology degree of any sheaf by $2n+1$. The spectral sequence with terms

\[
H_\Delta^a(X\times X;\mathcal H^b(K))
\Longrightarrow H_\Delta^{a+b}(X\times X;K)
\]

and (M41) therefore gives vanishing above $(2n+1)+(n+g)=3n+g+1$. This is precisely (M38). The bound is deliberately not claimed to be optimal. $\square$

### SH02-MD-BOUNDED-HOM — Boundedness for arbitrary bounded inputs

**Corollary.** For the course coefficient ring and an $n$-manifold, internal derived Hom preserves boundedness:

\[
R\mathcal Hom_k:D^b(k_X)^{\mathrm{op}}\times D^b(k_X)
\longrightarrow D^b(k_X).
\tag{M43}
\]

More quantitatively, if $F\in D^{[a,b]}$ and $G\in D^{[c,d]}$, it has cohomology only in

\[
[c-b,\ d-a+3n+\operatorname{gld}(k)+1].
\tag{M44}
\]

*Proof.* Every open subset of $X$ is again a countable-at-infinity manifold of dimension at most $n$, so (M38) applies with the same bound there. Internal Ext sheaves are the sheafifications of local Ext groups, computed by restricting an injective resolution to open subsets. Thus their positive degrees have the same uniform bound. Filtering $F,G$ by their finitely many cohomology sheaves now gives (M44); the lower bound is the usual left-exact-Hom bound. This argument neither imposes perfect stalks nor invokes biduality. $\square$

## SH02-MD-EXAMPLES — Worked examples and exercises

Local identifier: `SH02-MD-EXAMPLES`.

**A normal line with nontrivial orientation.** Let $L\to S^1$ be the real line bundle with transition $v\mapsto-v$ after one circuit. Its total space is the open Möbius strip. For the projection $p:L\to S^1$, the relative orientation line has monodromy $-1$ along the zero section. Therefore

\[
p^!k_{S^1}=o_p[1].
\]

Over $\mathbb Z$, this is not the globally constant sheaf shifted by $[1]$. For the zero section $i:S^1\hookrightarrow L$, $i^!k_L=o_{S^1/L}[-1]$ with the same sign monodromy. Nevertheless $pi=\operatorname{id}$, so

\[
i^!p^!k_{S^1}\simeq k_{S^1}.
\]

Indeed the two shifts cancel and the two sign lines pair to the tensor unit by (M8). This example checks both negative relative dimension for an embedding and the need to retain the orientation line.

**An embedding changes arbitrary coefficients by local support.** Let $i:\{0\}\hookrightarrow\mathbb R$. Then $i^!k_{\mathbb R}=k[-1]$. But for the skyscraper $F=i_*M$ one has $i^!F=M$, since every section is already supported at the point. The expression $i^{-1}F\otimes i^!k_{\mathbb R}=M[-1]$ consequently fails to equal $i^!F$ for nonzero $M$. The tensor comparison exists for every map; the theorem asserting it is invertible in (M11) really uses the submersion hypothesis.

**Infinite coefficients do not obstruct interval integration.** Let $M=\prod_{r\ge1}\mathbb Z/2^r\mathbb Z$, regarded as a $\mathbb Z$-module. For the increasing interval $I=(2,5)$,

\[
R\Gamma_c(I;M_I)=M[-1],
\qquad
R\Gamma_c(I;M_I[1])\xrightarrow{\int_I}M
\]

is the identity after the prescribed orientation identification. The proof is the two-endpoint localization calculation, applied directly to $M$; it never exchanges sheaf sections with an infinite product or identifies $M$ with its double dual.

### SH02-MD-EXERCISES — Solved checks

1. For a real rank-$r$ vector bundle $\pi:E\to B$ over a manifold, and its zero section $s$, compute $\omega_\pi$, $\omega_s$ and the composite trace of $\pi s$. Explain all shifts and orientation cancellations.

   *Solution.* With the sign local system $o(E)$ on $B$ from (M30),

   \[
   \omega_\pi=\pi^{-1}o(E)[r],\qquad
   \omega_s=o(E)[-r].
   \]

   The tensor product $\omega_s\otimes s^{-1}\omega_\pi$ has shift zero and pairs the two copies of $o(E)$ by (M8), giving $k_B$. Exceptional composition identifies it with $\omega_{\pi s}=k_B$. Equation (M27) makes the composite counit the identity. A choice of global bundle orientation is unnecessary.

2. Let $h:\mathbb R^2\to\mathbb R^2$ be $h(x,y)=(x+y^3,-y)$. Determine its action on $H_c^2(\mathbb R^2;M)$ for arbitrary $M$ and compare ordinary integration of forms with integration of densities.

   *Solution.* The maps $(x,y)\mapsto(x+t y^3,-y)$ form a proper homotopy of homeomorphisms for $0\le t\le1$: a bounded image forces $y$ bounded and then $x$ bounded uniformly in $t$. At $t=0$ the map is a coordinate reflection. Thus its compact-support cohomology action is $-1$ by (M6). An ordinary oriented top-degree form changes its integral by this sign under pullback. A density also carries the orientation line, on which $h$ acts by $-1$; the two signs cancel, as required for the coordinate-independent integral (M29).

3. For $p:\mathbb R\times S^1\to S^1$ and $F\in D^+(k_{S^1})$, identify the adjunction unit $F\to Rp_*p^{-1}F$. Compute $Rp_!p^{-1}F$ and type-check the proposed arrow $Rp_!p^{-1}F\to F$: does exceptional adjunction supply it as an unshifted trace? Give the actual trace domain.

   *Solution.* The first is an isomorphism by the cylinder theorem or (M34). The projection formula gives $Rp_!p^{-1}F=F[-1]$. The exceptional adjunction trace has domain $Rp_!p^!F=Rp_!p^{-1}F[1]=F$, and is the identity under increasing orientation. There is no corresponding unshifted exceptional trace from $F[-1]$ to $F$ supplied by this adjunction. Forgetting the relative shift changes the type of the map.

4. Show that the soft and c-soft dimensions of $\mathbb R^n$ are exactly $n$, and explain the zero-dimensional issue for a proposed sharp flabby bound.

   *Solution.* Equation (M4) gives the upper bound. For any nonzero module $M$, (M6) gives $H_c^n(\mathbb R^n;M)=M\ne0$. A shorter c-soft resolution would force that group to vanish, proving the lower bound. Softness and c-softness agree here by the compact-exhaustion gluing argument after (M4). For $n=0$ the space is a point, so the sections functor is exact and every sheaf is flabby; its flabby dimension is zero. The present argument supplies only the general flabby upper bound $n+1$ in positive dimension. A sharp lower bound there requires a different sheaf and is not claimed as proved by this exercise.

5. Let $L$ be locally isomorphic to $\mathbb Z_X$ on any space $X$. Prove that the canonical map $L\otimes L\to\mathbb Z_X$ needs no chosen local generators, and explain why the analogous assertion for an arbitrary rank-one local system of complex vector spaces is false.

   *Solution.* Any two generators of a rank-one free integral module differ by $\pm1$, so the rule $e\otimes e\mapsto1$ is unchanged by a change of generator and defines a sheaf morphism. It is an isomorphism on stalks. For a complex local system on $S^1$ with monodromy $2$, its tensor square has monodromy $4$, so it is not even isomorphic to the constant local system. The integral sign structure is essential.

6. In the proof of (M38), replace the supported group in (M42) by ordinary cohomology of $X\times X$. Identify the lost operation and explain why this replacement cannot be justified by the existence of a diagonal embedding.

   *Solution.* The operation in (M39) is $\delta^!$, whose pushforward is $R\Gamma_\Delta$. Taking global sections therefore yields diagonal-supported cohomology. Ordinary product cohomology corresponds to omitting this support functor. A closed embedding does not make its support condition vacuous on the ambient space. The supported bound $2n+1$ is precisely what controls the omitted operation.

## SH02-MD-ANTECEDENTS — Antecedents and the scope of this candidate

Local identifier: `SH02-MD-ANTECEDENTS`.

The source used for the present comparison is Pierre Schapira’s [*An Introduction to Sheaves on Grothendieck Topologies*, version dated 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). The following correspondence identifies the results and the additional arguments actually needed here. Page numbers are the printed numbers, which agree with PDF page numbers in this edition.

| Part of this unit | Approved source passage | What the present proof supplies |
|---|---|---|
| `SH02-MD-DIMENSION`, (M2)–(M4) | §3.5, Lemma 3.5.1, p. 72; §4.3, pp. 86–90; §5.1, Lemma 5.1.1 and Proposition 5.1.2, pp. 105–106 | The interval-to-vector-space induction, the explicit syzygy extension test, and compact-exhaustion gluing retain arbitrary sheaves. The result used here is the upper flabby bound; the source’s sharper assertion in Proposition 5.1.2(v) is not adopted, in particular at dimension zero. |
| `SH02-MD-EUCLIDEAN`, `SH02-MD-ORIENTATION-LINE`, (M5)–(M9) | §3.6, Theorem 3.6.3 and Lemmas 3.6.4–3.6.5, pp. 74–75; §5.1, Lemma 5.1.3, Definition 5.1.4 and Proposition 5.1.5, pp. 106–107; Exercises 5.1 and 5.3, p. 119 | The two-endpoint complex fixes the generator and its sign. Proper interval homotopy supplies the support comparison, and the integral sign structure makes the square pairing canonical. The exercises in the source are comparison targets, not substituted for these proofs. |
| `SH02-MD-SUBMERSION`, `SH02-MD-RELATIVE`, `SH02-MD-GRAPH`, `SH02-MD-CLOSED`, (M10)–(M24) | §4.6, Corollary 4.6.2 and Propositions 4.6.4–4.6.9, pp. 95–97; §4.7, equations (4.7.1)–(4.7.4), p. 97; §5.1, Definition 5.1.6 and Proposition 5.1.9, pp. 107–108 | Product-chart evaluation proves the submersion comparison. Composition and cancellation of invertible orientation complexes then prove the relative formula, including maps over a common locally compact base and signed relative dimensions. The graph computation is a supported calculation for arbitrary input, not a submersion formula asserted for an embedding. |
| `SH02-MD-TRACE`, `SH02-MD-SPHERE`, (M25)–(M32) | §4.6, adjunction (4.6.1), Corollary 4.6.2 and Proposition 4.6.6, pp. 94–96; §5.1, orientation identification, p. 107 | Trace is the specified counit. Its composition and submersion-base-change rules are checked as identities of mates. Ordered radial orientation and the dual-frame pairing supply the ray-sphere and hemisphere normalizations. |
| `SH02-MD-INTEGRAL-DETECTION`, `SH02-MD-ACYCLIC-SUBMERSION`, (M33)–(M36) | §4.6, Proposition 4.6.6, pp. 95–96; §4.7, equation (4.7.3), p. 97; the related field-coefficient exercise is Exercise 5.9, p. 120 | The displayed integral-dual conservativity proof is the additional algebraic step. It detects the cone of trace without imposing finite generation or assuming arbitrary biduality. This is why the integral acyclicity criterion proves descent for all the bounded-below coefficient inputs stated here. |
| `SH02-MD-DENSITIES`, (M37) | §5.5, Lemmas 5.5.1 and 5.5.4, pp. 115–116 | The de Rham resolution identifies the compactly supported classes. The increasing-interval generator, ordered products, Stokes theorem and a finite partition of unity identify analytic integration with the counit with sign fixed. The complex residue construction in §5.7 is a different comparison and is not a replacement for this real-density argument. |
| `SH02-MD-HOMOLOGICAL-DIMENSION`, `SH02-MD-BOUNDED-HOM`, (M38)–(M44) | §4.6, Propositions 4.6.8–4.6.9, pp. 96–97, supply the diagonal and rectangle identities in the source’s coefficient setting | The numerical bound is derived here from those operation mechanisms, coefficient Ext vanishing, and supported cohomology on the product. Its associative-ring statement is checked using left-module Hom and the integral orientation line. It is not attributed to a finite-rank or constructible duality theorem, and it does not require noetherian coefficients. |

The source’s tensor comparison in Proposition 4.6.4 and projection formula in Theorem 4.4.7 have their printed boundedness hypotheses. They are not, just by citation, the entire bounded-below contract of this unit. For the broader uses, the named exceptional-operation contract, the cylinder theorem and the uniform dimension bound remain explicit. Likewise, Proposition 5.1.5(d) refers elsewhere for the differentiable orientation identification; `SH02-MD-SMOOTH-SIGN` supplies the local interpolation proof used here. These distinctions retain the full mathematical scope while making the source of each step testable.

The [open prerequisite contracts](open-prerequisites.md) identify the actual Stacks statements and their GFDL-1.2-or-later license route. The c-soft resolution, compact-support fibre and composition contracts above now have the exact programme proofs linked at their statements; the supporting sheaf and derived-category foundations remain dependencies. The exceptional-operation construction retains its own stated ranges and prerequisites. The de Rham resolution and Stokes theorem are the explicitly named prerequisites for the smooth-density comparison alone. No unresolved import is closed by the existence of this lesson, and the sharper positive-dimensional flabby lower bound is not counted as resolved here.

Original AI programme expression and the new source comparison are CC0 1.0 Universal. Schapira’s mathematical results are credited above; the linked human source retains its own terms. Free reading access does not place the source text under the programme’s CC0 dedication. The earlier draft’s source attribution is retained in the private version history; this comparison records the exact edition consulted for the present repair.
