# SH02-EXCEPTIONAL-OPERATIONS — Exceptional inverse image from a finite resolution

This lesson constructs the adjunction and proves its comparisons relative to those precisely stated foundations. The final support-comparison discussion identifies one further extension to unbounded operations which remains unfinished; its bounded case is proved and is not claimed to close the full extension.

The exceptional inverse image is determined by what can be integrated with proper support. To construct it, we first make proper direct image exact by tensoring with a suitable sheaf. The ordinary right adjoint of this exact functor can then be assembled into a bounded resolution model. This also fixes the trace maps used in subsequent formulas.

All spaces in this lesson are locally compact Hausdorff. Write a continuous map as $f:Y\to X$. Unless a statement says otherwise, $k$ is a commutative ring of finite global dimension $d$, all sheaves are $k$-module sheaves, and the inputs and outputs belong to $D^+$. Cohomological grading means $H^i(C[s])=H^{i+s}(C)$. No constructibility, finite generation, field assumption, or countability of a neighborhood basis is imposed.

## SH02-EX-FOUNDATIONS — The topological foundation being used

The following are exact prerequisite contracts for proper-support sheaf theory. They belong to the earlier foundations course. They are stated here so that the construction does not hide its prerequisites inside the phrase “six operations.” The existing [open prerequisite contracts](open-prerequisites.md) supply the abelian and derived-category foundations, but their proper-base-change theorem for proper maps alone does not supply this entire list.

### SH02-EX-IMP-SOFT — The compact-support resolution contract

A sheaf on a locally compact Hausdorff space is c-soft when its sections on every compact subset extend globally. Injective and flabby sheaves are c-soft. Open extension by zero and arbitrary coproducts preserve c-softness. A c-soft sheaf is acyclic for compactly supported sections. Conversely, $H_c^j(V;E|_V)=0$ for all open $V$ and all $j>0$ implies c-softness.

### SH02-EX-IMP-FIBRES — The proper-support fibre contract

Proper direct image $f_!$ is left exact, commutes with coproducts, and has stalk $(f_!E)_x=\Gamma_c(f^{-1}(x);E|_{f^{-1}(x)})$. Its derived stalks are the corresponding compactly supported cohomology groups. A sheaf whose restrictions to all fibres are c-soft is $f_!$-acyclic; bounded-below complexes of such sheaves compute $Rf_!$. These assertions also hold after restricting the source to an open subset.

### SH02-EX-IMP-COMPOSE — The proper-support composition contract

For composable maps, the natural proper-support comparison $Rf_!Rg_!\simeq R(fg)_!$ is an isomorphism on $D^+$, compatible with threefold composition and identities.

### SH02-EX-IMP-BC — The base-change boundary

The full proper-support base-change theorem for arbitrary locally compact Hausdorff maps belongs to the earlier foundations. Under the finite dimension assumption of this lesson, the required case and its pasting compatibility are proved below as `SH02-EX-BASECHANGE-BRIDGE`, using the fibre and soft contracts.

The soft, fibre, and composition contracts are used as imports, with their receipt still outstanding. The finite-dimensional case of nonproper base change and the projection formula required below are proved from those contracts. A theorem about a proper map or a perfect tensor factor is not used as a substitute for either assertion.

We will also use two elementary consequences of the stated compact-support contracts. A compact subset meets only finitely many members of a locally finite family of supports, after passage to a finite open cover. This explains why compactly supported sections of a sheaf coproduct are a coproduct, even though unrestricted sections need not commute with coproducts. Restriction to a closed subset preserves c-softness: a compact subset of the closed subset is compact in the ambient space, and restriction to that compact subset has the same sections.

## SH02-EX-RELATIVE-SOFT — Turning proper direct image into an exact functor

Call an abelian sheaf $E$ on $Y$ **$f$-soft** if $E|_{f^{-1}(x)}$ is c-soft for every $x\in X$. By the soft criterion and the fibre formula, this is equivalent to

\[
R^j f_!(E_U)=0\qquad(j>0,\ U\subset Y\text{ open}),
\]

where $E_U$ is restriction to $U$ followed by extension by zero. The use of every open $U$ matters: being merely $f_!$-acyclic does not express the full condition.

Assume henceforth that there is an integer $r\geq0$ such that

\[
R^j f_!E=0\qquad(j>r)
\tag{EX.1}
\]

for every **abelian sheaf** $E$ on $Y$. This is a condition over $\mathbb Z$, not only over the chosen coefficient ring. The fibre formula says equivalently that all fibres have compact-support cohomological dimension at most $r$. For the reverse implication in this equivalence, restrict to each fibre and use stalkwise detection of zero. For the forward implication, extend a sheaf on the closed fibre by zero to $Y$ and take the stalk at its image point. Hence the same bound applies after any change of base.

The bound yields a useful finite dimension-shifting rule. If

\[
E_0\longrightarrow E_1\longrightarrow\cdots\longrightarrow E_r
\longrightarrow0
\tag{EX.2}
\]

is exact and $E_0,\ldots,E_{r-1}$ are $f$-soft, then $E_r$ is $f$-soft. To see this, insert the successive kernels, apply open extension by zero, and use the long exact sequences of $R f_!$. For $j>0$, repeated connecting maps identify $R^jf_!((E_r)_U)$ with $R^{j+r}f_!(N_U)$ for the kernel at the left end; that group vanishes by (EX.1). For $r=0$ there are no middle sheaves and (EX.1) itself gives the assertion. The same argument shows that truncating an $f$-soft resolution after $r$ steps leaves an $f$-soft final cokernel.

The statements remain true for $k$-module sheaves after forgetting scalars. One can compute compact-support cohomology using a resolution by sheaves which are c-soft as abelian sheaves, so the underlying abelian and $k$-linear derived functors agree. Thus the integral dimension hypothesis bounds the coefficient versions without requiring $k$ to be flat over $\mathbb Z$.

### SH02-EX-FLAT-SOFT — The flat relative-soft tensor lemma

**Tensor lemma.** Let $S$ be a commutative coefficient ring and let $K$ be an $S_Y$-module which is flat and $f$-soft. Then $G\otimes_S K$ is $f$-soft for every $S_Y$-module $G$, and

\[
G\longmapsto f_!(G\otimes_S K)
\tag{EX.3}
\]

is exact. The underlying integral dimension bound (EX.1) is retained.

**Proof.** For every pair consisting of an open set $U$ and a section $s\in G(U)$ there is a morphism $S_U\to G$ taking $1$ to $s$. The coproduct of all these maps is surjective on every stalk. Repeating the construction for its kernel gives a resolution to the left by coproducts of the sheaves $S_U$. These are **coproduct** generators; their morphisms into a sheaf form a product of section modules.

After tensoring with $K$, the resolution stays exact by flatness. Every term is a coproduct of open extensions $K_U$, hence is $f$-soft. Apply (EX.2) to its final $r$ steps, with $G\otimes_S K$ at the right end. This proves the first assertion. For a short exact sequence of $G$'s, tensoring is exact and all three resulting sheaves are $f_!$-acyclic. The long exact derived-image sequence therefore proves exactness of (EX.3). $\square$

Only stalkwise flatness was used. No assertion that arbitrary products of open generators are free generators enters the proof.

## SH02-EX-FINITE-RESOLUTION — A finite universal resolution

There exists an exact sequence of abelian sheaves

\[
0\longrightarrow\mathbb Z_Y\longrightarrow K^0\longrightarrow\cdots
\longrightarrow K^r\longrightarrow0
\tag{EX.4}
\]

whose terms are both flat over $\mathbb Z$ and $f$-soft.

Here is a construction that works without a countability assumption. For an abelian sheaf $E$, let

\[
Q(E)(U)=\prod_{y\in U} E_y.
\]

This is a flabby sheaf, and the map $E\to Q(E)$ sends a section to its family of germs. It is injective. If $E$ has torsion-free stalks, then so does $Q(E)$: its stalks are filtered colimits of products of torsion-free groups. Moreover, the map $E_y\to Q(E)_y$ has a retraction given by evaluation at the coordinate $y$. Consequently its cokernel is a direct summand of the torsion-free group $Q(E)_y$, and is torsion-free. Over $\mathbb Z$, torsion-free means flat. Thus both $Q(E)$ and $Q(E)/E$ are flat whenever $E$ is flat.

Start with $C^0=\mathbb Z_Y$, set $K^j=Q(C^j)$ and $C^{j+1}=K^j/C^j$ for $0\leq j<r$, and finally set $K^r=C^r$. Flatness follows inductively from the preceding stalk argument. The first $r$ terms are flabby, hence $f$-soft; the last is $f$-soft by dimension shifting. If $r=0$, simply take $K^0=\mathbb Z_Y$: (EX.1) and the relative soft criterion say directly that it is $f$-soft. This proves (EX.4).

The augmented complex (EX.4) stays exact after tensoring with any abelian sheaf: its short exact constituent sequences have flat cokernels. It follows that $G\to G\otimes_{\mathbb Z}K^\bullet$ is a quasi-isomorphism for every bounded-below complex $G$. The total complexes here have finitely many $K$-degrees; there is no infinite-product convergence issue.

## SH02-EX-REPRESENTING-SHEAF — The sheaf representing the ordinary adjunction

Fix one flat $f$-soft abelian sheaf $K$. For an injective $k_X$-module $I$, define

\[
J_K(I)(U)=\operatorname{Hom}_{k_X}
   \bigl(f_!(k_U\otimes_{\mathbb Z}K),I\bigr).
\tag{EX.5}
\]

For $V\subset U$, the extension-by-zero map $k_V\to k_U$ gives the restriction map in (EX.5).

This presheaf is a sheaf. Indeed, for an open covering $U=\bigcup_i U_i$, there is the right-exact sheaf sequence

\[
\bigoplus_{i,j}k_{U_i\cap U_j}\longrightarrow
\bigoplus_i k_{U_i}\longrightarrow k_U\longrightarrow0.
\]

The first map is the difference of the two inclusions. Tensor with $K$ and apply the exact functor (EX.3); it also preserves coproducts. Applying $\operatorname{Hom}(-,I)$ gives exactly the equalizer expressing the sheaf axiom for (EX.5). There is no assumption that an infinite coproduct has its sections computed pointwise as a presheaf coproduct.

There is a natural isomorphism

\[
\operatorname{Hom}_{k_X}\bigl(f_!(G\otimes_{\mathbb Z}K),I\bigr)
\simeq \operatorname{Hom}_{k_Y}\bigl(G,J_K(I)\bigr).
\tag{EX.6}
\]

To construct its map, take a morphism on the left and precompose it with the morphism induced by each section $k_U\to G$. This produces a compatible map $G(U)\to J_K(I)(U)$ on every open $U$. When $G=k_U$, this is the identity identification in (EX.5). It is therefore an isomorphism for a coproduct of open generators. An arbitrary $G$ has a presentation $P_1\to P_0\to G\to0$ by such coproducts. Both sides of (EX.6), regarded as contravariant functors of $G$, send this presentation to the kernel of the corresponding map from their value on $P_0$ to their value on $P_1$. The isomorphisms on $P_0,P_1$ identify those kernels. This proves (EX.6), including its naturality, without a representability theorem.

The left side of (EX.6) is exact in $G$, by (EX.3) and injectivity of $I$. Hence $J_K(I)$ is injective. The construction is covariant in $I$ and contravariant in $K$.

## SH02-EX-ADJOINT — The derived adjunction and its normalization

**Existence theorem.** Under (EX.1), $Rf_!:D^+(k_Y)\to D^+(k_X)$ has a right adjoint

\[
f^!:D^+(k_X)\longrightarrow D^+(k_Y).
\]

More precisely, $f^!D^{\geq a}\subset D^{\geq a-r}$. No preservation of $D^b$ is asserted for an arbitrary map between the present spaces.

**Construction and proof.** Represent $F\in D^+(k_X)$ by a bounded-below injective complex $I$. Using (EX.4), form the finite-width Hom total complex

\[
(J_K I)^n=\bigoplus_{p=0}^r J_{K^p}(I^{n+p}).
\tag{EX.7}
\]

For a homogeneous map of total degree $n$, its differential is the usual Hom differential

\[
d(h)=d_I\circ h-(-1)^n h\circ d_K.
\]

Each degree of (EX.7) is a finite sum of injectives, hence injective. If $I$ starts in degree $a$, (EX.7) starts in degree $a-r$. The same formula sends chain homotopies to chain homotopies and commutes with the standard shift identifications.

For a bounded-below complex $G$, the tensor lemma says that every term of $G\otimes_{\mathbb Z}K^\bullet$ is $f$-soft. Its augmentation is a quasi-isomorphism, so

\[
Rf_!G\simeq f_!(G\otimes_{\mathbb Z}K^\bullet).
\]

Applying (EX.6) in every bidegree and the tensor–Hom sign convention gives an isomorphism of Hom complexes

\[
\operatorname{Hom}^\bullet
 \bigl(f_!(G\otimes_{\mathbb Z}K^\bullet),I\bigr)
\simeq \operatorname{Hom}^\bullet(G,J_K I).
\tag{EX.8}
\]

Taking degree-zero cohomology computes morphisms in the derived category on both sides, because the target complexes are bounded-below injectives. Thus $f^!F=J_KI$ has the desired adjunction. Bounded-below complexes of injectives model $D^+$, so this construction descends to a triangulated functor. The bound follows from (EX.7). $\square$

Define the unit $\eta_G:G\to f^!Rf_!G$ and the trace, or counit,

\[
\epsilon_F:Rf_!f^!F\longrightarrow F
\tag{EX.9}
\]

as the images of the identity morphisms under (EX.8). Naturality of that isomorphism gives the triangular identities

\[
\epsilon_{Rf_!G}\circ Rf_!(\eta_G)=1_{Rf_!G},\qquad
f^!(\epsilon_F)\circ\eta_{f^!F}=1_{f^!F}.
\tag{EX.10}
\]

For example, applying the adjunction bijection to the first composite reduces it to the definition of $\eta_G$; applying its inverse to the second reduces it to the definition of $\epsilon_F$. This is a proof of the normalization, not merely an assertion that some abstract right adjoint exists.

Any other construction with its adjunction is uniquely isomorphic to this one by the map whose transpose is its counit. The inverse is obtained by exchanging the two constructions; (EX.10) makes both composites identities. This identifies different choices of (EX.4), respects the trace, and satisfies the cocycle identity for three choices. Because (EX.8) is an isomorphism of complexes with the displayed Hom differential, simultaneously shifting source and target commutes with the adjunction. In particular, the trace of $F[1]$ is the shift of the trace of $F$ under the chosen triangulated identifications; no independent sign can be inserted.

The same construction also proves the ringed-space variant. Given sheaves of rings $\mathcal R$ on $X$, $\mathcal S$ on $Y$ and a homomorphism $f^{-1}\mathcal R\to\mathcal S$, replace $k_U$ in (EX.5) by $\mathcal S_U$ and take Hom in $\mathcal R$-modules. The functor $f_!(-\otimes_{\mathbb Z}K)$, followed by restriction of scalars, is exact. The generator and injectivity arguments are unchanged and give a right adjoint $D^+(\mathcal R)\to D^+(\mathcal S)$. Commutativity and finite global dimension are not needed for this existence construction; those hypotheses enter the tensor assertions below.

## SH02-EX-PROJECTION — Projection with arbitrary coefficients

For $G\in D^+(k_Y)$ and $B\in D^+(k_X)$, there is a canonical isomorphism

\[
Rf_!G\otimes_k^L B\xrightarrow{\sim}
Rf_!\bigl(G\otimes_k^L f^{-1}B\bigr).
\tag{EX.11}
\]

Here finite global dimension of $k$ ensures that all tensor products displayed in $D^+$ stay in $D^+$. The assertion allows arbitrary $B$, with no perfection assumption.

First suppose that $E$ is a flat $f$-soft $k_Y$-module. On a fibre, the functor

\[
M\longmapsto\Gamma_c(f^{-1}(x);E|_{f^{-1}(x)}\otimes_k M)
\]

is exact by the tensor lemma. It preserves coproducts. The natural map from $\Gamma_c(E|_{f^{-1}(x)})\otimes_k M$ to this functor is an isomorphism for free modules, hence for every module by a free presentation and right exactness. It follows in addition that $\Gamma_c(E|_{f^{-1}(x)})$ is flat. The stalk formula now proves both that $f_!E$ is flat and that

\[
f_!E\otimes_k B\simeq f_!(E\otimes_k f^{-1}B)
\tag{EX.12}
\]

for every sheaf $B$. The map is defined on sections by multiplying a properly supported section by a pulled-back local section. Its support remains proper.

For the derived statement, use a bounded-below flat resolution $P$ of $G$, starting at most $d$ degrees earlier, and one for $B$. Here is a precise way to obtain the required lower bound from `SH02-IMP-KFLAT`. Start with its termwise-flat complex $Q$ representing an object in $D^{\geq a}$. Put $C^m=\operatorname{coker}(Q^{m-1}\to Q^m)$. For $m<a$, exactness gives $0\to C^m\to Q^{m+1}\to C^{m+1}\to0$. On each stalk, $d$ successive Tor connecting isomorphisms identify $\operatorname{Tor}_1(C^{a-d},M)$ with $\operatorname{Tor}_{d+1}(C^a,M)=0$. Thus $C^{a-d}$ is flat, and replacing the part of $Q$ below degree $a-d$ by this cokernel gives the bounded-below flat resolution. When $d=0$, every stalk module is already flat and the same truncation works directly.

Tensor $P$ over $\mathbb Z$ with (EX.4). Its total complex $E$ is termwise flat over $k$, termwise $f$-soft, and quasi-isomorphic to $G$. All the double complexes used here lie in a translated first quadrant. Thus termwise flat resolutions calculate the derived tensor products of these bounded-below inputs, and termwise $f$-soft resolutions calculate $Rf_!$. Applying (EX.12) to the double complexes gives (EX.11).

The identity, associativity and symmetry compatibilities of this projection map can be checked before deriving: both ways of multiplying a supported section by two local coefficient sections give the same section, and interchanging homogeneous factors introduces exactly the usual Koszul sign. Flat resolutions preserve these equalities. Its compatibility with open restriction is immediate from the same description. These facts will fix the tensor comparisons of $f^!$.

## SH02-EX-COMPOSITION — Composition, restriction, and change of base

Suppose $Z\xrightarrow{g}Y\xrightarrow{f}X$ satisfy the integral dimension bounds $s$ and $r$. Then $(fg)_!$ has cohomological dimension at most $r+s$. Indeed, apply the composition import and filter $Rg_!E$ by its cohomology sheaves: their degrees lie between $0$ and $s$, and applying $Rf_!$ gives degrees at most $r+s$. This finite filtration is the usual derived-functor spectral-sequence argument, and does not require the spectral sequence to have infinitely many nonzero diagonals.

There is a canonical isomorphism

\[
(fg)^!\simeq g^!f^!.
\tag{EX.13}
\]

For every $H\in D^+(k_Z)$ and $F\in D^+(k_X)$, the successive adjunctions give

\[
\begin{aligned}
\operatorname{Hom}(H,g^!f^!F)
&\simeq\operatorname{Hom}(Rg_!H,f^!F)\\
&\simeq\operatorname{Hom}(Rf_!Rg_!H,F)\\
&\simeq\operatorname{Hom}(R(fg)_!H,F).
\end{aligned}
\]

Representing this natural bijection defines (EX.13). Its trace is exactly

\[
Rf_!Rg_!g^!f^!F\xrightarrow{Rf_!(\epsilon_g)}
Rf_!f^!F\xrightarrow{\epsilon_f}F.
\tag{EX.14}
\]

For three maps, either parenthesization has the trace obtained by successively applying the three traces in their order of composition. The associativity of the imported proper-support comparison identifies their sources. Uniqueness of an adjoint identification preserving the trace therefore proves the associativity of (EX.13). For the identity map the trace is the identity, so the unit coherence follows in the same way.

### SH02-EX-EMBEDDING — Open, closed, and locally closed inclusions

For an open embedding $j:U\hookrightarrow X$, the exact functor $j_!$ has exact right adjoint $j^{-1}$. The ordinary adjunction therefore gives $j^!=j^{-1}$, with its usual extension-by-zero counit. For a closed embedding $i:Z\hookrightarrow X$, its exact direct image has right adjoint $i^{-1}\Gamma_Z$ at the sheaf level. To prove this, a map $i_*A\to F$ lands in the subsheaf of sections supported on $Z$, and maps to that subsheaf are determined by their restriction to $Z$. Deriving the adjunction gives

\[
i^!F\simeq i^{-1}R\Gamma_ZF,
\qquad R\Gamma_ZF\simeq i_*i^!F.
\tag{EX.15}
\]

For a locally closed embedding, factor it as a closed embedding into an open subset and then use (EX.13). More explicitly, if $Z$ is closed in $U$ and $j:U\hookrightarrow X$, set $R\Gamma_ZF=Rj_*R\Gamma_Z^U(j^{-1}F)$, where the superscript marks closed support inside $U$. This object is also $R\mathcal Hom_X(k_Z,F)$, with $k_Z$ extended by zero from the locally closed subset: the ordinary extension/restriction and closed-support adjunctions identify both expressions. The result is $i^!F\simeq i^{-1}R\Gamma_ZF$. Independence of the chosen open ambient neighborhood follows from this intrinsic internal-Hom description, or by restricting the two factorizations to their intersection and applying their adjunctions. Ordinary direct image $Rj_*$, rather than extension by zero, is part of this support convention.

These formulas also identify the open restriction of $f^!$. If $V\subset X$ is open, write $j:V\to X$, $j':f^{-1}V\to Y$, and $f_V:f^{-1}V\to V$. The equality $fj'=jf_V$ and the composition isomorphisms give

\[
j'^{-1}f^!F\simeq f_V^!(F|_V).
\tag{EX.16}
\]

This isomorphism preserves the traces after restriction. One can also see it directly in (EX.5), since a section supported properly over $V$ is tested against $I|_V$ and open restriction preserves injectives.

### SH02-EX-BASECHANGE-BRIDGE — A finite-dimensional base-change proof

Here is the promised finite-dimensional base-change bridge. In a cartesian square with horizontal $f:Y\to X$, $f':Y'\to X'$ and vertical $g,g'$, pulling back a properly supported section gives the underived map $g^{-1}f_!E\to f'_!g'^{-1}E$: the pullback of its support is proper over the new base. The fibre contract identifies its two stalks with the same compactly supported sections on the same fibre, so the map is an isomorphism.

Choose (EX.4) for $f$. Its pullback $g'^{-1}K^\bullet$ is still flat, exact over $\mathbb Z$, and $f'$-soft: the fibre restrictions are precisely those of $K^\bullet$ under the fibre homeomorphisms. Thus $G\otimes K^\bullet$ computes $Rf_!G$, while $g'^{-1}(G\otimes K^\bullet)$ computes $Rf'_!g'^{-1}G$. Apply the underived base-change isomorphism term by term to obtain $g^{-1}Rf_!G\simeq Rf'_!g'^{-1}G$ on $D^+$. For two base changes, either composite is pullback of the same sections in this model. Thus identity squares, open restrictions and pasted squares have the asserted canonical compatibilities. No compactness of $f$ itself is used.

### SH02-EX-BASECHANGE — Two exceptional base-change comparisons

Consider the cartesian square described in `SH02-EX-IMP-BC`. If $f_!$ has integral cohomological dimension at most $r$, so does $f'_!$, since their fibres over corresponding points are homeomorphic. There are two different exceptional comparisons:

\[
f^!Rg_*\xrightarrow{\sim}Rg'_*f'^!,
\qquad
\beta:g'^{-1}f^!\longrightarrow f'^!g^{-1}.
\tag{EX.17}
\]

The first is an isomorphism; the second is at this stage only a morphism.

For the first map, take $A\in D^+(k_Y)$ and $B\in D^+(k_{X'})$. The following natural sequence of bijections gives its definition and proof:

\[
\begin{aligned}
\operatorname{Hom}(A,f^!Rg_*B)
&\simeq\operatorname{Hom}(Rf_!A,Rg_*B)\\
&\simeq\operatorname{Hom}(g^{-1}Rf_!A,B)\\
&\simeq\operatorname{Hom}(Rf'_!g'^{-1}A,B)\\
&\simeq\operatorname{Hom}(g'^{-1}A,f'^!B)\\
&\simeq\operatorname{Hom}(A,Rg'_*f'^!B).
\end{aligned}
\]

The third line is the proper-support base-change bridge just proved. Every other line is one of the already specified adjunctions.

Define the second map by the requirement that its $Rf'_!\dashv f'^!$ transpose be

\[
Rf'_!g'^{-1}f^!F
\xrightarrow{\sim}g^{-1}Rf_!f^!F
\xrightarrow{g^{-1}\epsilon_f}g^{-1}F.
\tag{EX.18}
\]

This explicit definition is useful in calculations: it fixes which way the map goes and its normalization. For an identity square it gives the identity, by (EX.10). For two successive base changes, transpose the composite of their $\beta$ maps. Inserting (EX.18) first for the inner square and then for the outer one cancels the intermediate unit–counit pair by (EX.10). The resulting map is the pasted proper-support comparison followed by the pulled-back trace of $f$. The pasting compatibility proved in `SH02-EX-BASECHANGE-BRIDGE` identifies it with the transpose for the composite square. Since transposition is a bijection, the two $\beta$ maps agree.

For open $g$, (EX.16) shows that $\beta$ is invertible. A general closed change of base can fail to be invertible; a worked example below detects this failure with a shift.

### SH02-EX-COEFFICIENTS — Forgetting the coefficient action

Let $\phi$ denote the forgetful functor from $k$-module sheaves to abelian sheaves. The exceptional inverse images constructed with the two coefficient systems satisfy

\[
\phi_Y f_k^!F\simeq f_{\mathbb Z}^!(\phi_XF).
\tag{EX.19}
\]

For $A\in D^+(\mathbb Z_Y)$, its proof is the following chain of adjunctions:

\[
\begin{aligned}
\operatorname{Hom}_{\mathbb Z}(A,f_{\mathbb Z}^!\phi_XF)
&\simeq\operatorname{Hom}_{\mathbb Z}(Rf_!A,\phi_XF)\\
&\simeq\operatorname{Hom}_k(k_X\otimes_{\mathbb Z}^LRf_!A,F)\\
&\simeq\operatorname{Hom}_k(Rf_!(k_Y\otimes_{\mathbb Z}^LA),F)\\
&\simeq\operatorname{Hom}_k(k_Y\otimes_{\mathbb Z}^LA,f_k^!F)\\
&\simeq\operatorname{Hom}_{\mathbb Z}(A,\phi_Yf_k^!F).
\end{aligned}
\]

The middle line is (EX.11) over $\mathbb Z$. The tensor products stay bounded below because $\mathbb Z$ has global dimension one. Thus this argument permits torsion in $k$. Its canonical identification preserves the traces, since its construction uses precisely those traces in the two adjunctions. It asserts compatibility with forgetting the coefficient action, not an unrestricted theorem about extension of coefficients.

## SH02-EX-INTERNAL — Internal adjunction and its tensor structure

For $F\in D^+(k_X)$ and $G\in D^b(k_Y)$, there are canonical isomorphisms

\[
R\mathcal Hom_X(Rf_!G,F)
\simeq Rf_*R\mathcal Hom_Y(G,f^!F),
\tag{EX.20}
\]

\[
\mathbf{RHom}_X(Rf_!G,F)
\simeq\mathbf{RHom}_Y(G,f^!F).
\tag{EX.21}
\]

Here $\mathbf{RHom}_X(A,B)=R\Gamma(X;R\mathcal Hom_X(A,B))$ is a complex of $k$-modules; the script Hom denotes a sheaf on $X$. The finite dimension bound makes $Rf_!G$ bounded. Both internal Hom objects in (EX.20) are therefore in $D^+$, which is essential for the operations currently constructed.

To define the map from right to left in (EX.20), put $H=R\mathcal Hom_Y(G,f^!F)$. Evaluation, the ordinary counit $f^{-1}Rf_*H\to H$, (EX.11), and the exceptional trace give

\[
\begin{aligned}
Rf_!G\otimes^L Rf_*H
&\longrightarrow Rf_!(G\otimes^L f^{-1}Rf_*H)\\
&\longrightarrow Rf_!(G\otimes^L H)
\longrightarrow Rf_!f^!F\longrightarrow F.
\end{aligned}
\tag{EX.22}
\]

Currying (EX.22), with the tensor symmetry where needed, gives the desired morphism.

There is also a direct resolution proof, which verifies the map and works for modules over an arbitrary associative coefficient ring. Represent $G$ by a bounded complex and $F$ by a bounded-below injective complex $I$. The finite complex $L=f_!(G\otimes_{\mathbb Z}K^\bullet)$ represents $Rf_!G$. For every open $V\subset X$, the chain-level adjunction (EX.8), applied on $V$, identifies

\[
\operatorname{Hom}^\bullet_{V}(L|_V,I|_V)
\simeq
\operatorname{Hom}^\bullet_{f^{-1}V}
 (G|_{f^{-1}V},(J_KI)|_{f^{-1}V}).
\tag{EX.20a}
\]

These maps commute with open restriction, so they give an isomorphism of complexes of sheaves. For an injective $A$-module sheaf $J$, the sheaf $\mathcal Hom_A(E,J)$ is flabby as an abelian sheaf: a map on a smaller open extends by injectivity from the corresponding open extension of $E$ into the extension on the larger open. Boundedness of $G$ and $L$ makes every degree of the Hom complexes in (EX.20a) a finite sum of such flabby sheaves. They are bounded below and therefore compute both derived internal Hom and the required ordinary derived direct image. This proves (EX.20) directly. Its adjunction is the one in (EX.8), so in the commutative case it agrees with the evaluated map (EX.22).

For an open $V\subset X$, restriction identifies $Rf_!G|_V$ with $R(f_V)_!(G|_{f^{-1}V})$ and identifies $f^!F|_{f^{-1}V}$ by (EX.16). Taking $H^nR\Gamma(V;-)$ of (EX.22) therefore gives the adjunction bijection

\[
\operatorname{Hom}_{D(k_{f^{-1}V})}
  (G|_{f^{-1}V}, f_V^!(F|_V)[n])
\simeq
\operatorname{Hom}_{D(k_V)}
  ((Rf_!G)|_V,F|_V[n]).
\]

It is the same bijection because the last arrow in (EX.22) is the chosen trace. It is an isomorphism for every $V$ and every $n$. The cone of (EX.20) thus has zero derived sections on every open set; passing to stalks, or using the lowest nonzero cohomology sheaf locally, shows that cone is zero. This proves (EX.20). Applying $R\Gamma(X;-)$ proves (EX.21).

### SH02-EX-TENSOR — The normalized tensor comparison

For $A,B\in D^+(k_X)$, define

\[
\theta_{A,B}:f^!A\otimes_k^L f^{-1}B
\longrightarrow f^!(A\otimes_k^L B)
\tag{EX.23}
\]

to be the transpose of

\[
Rf_!(f^!A\otimes^L f^{-1}B)
\xrightarrow{\sim}Rf_!f^!A\otimes^L B
\xrightarrow{\epsilon_A\otimes1}A\otimes^L B.
\tag{EX.24}
\]

There is no invertibility assertion in this generality. The following identities fix the module structure of this comparison. Under the usual unit identification, $\theta_{A,k_X}$ is the identity. For $A,B,C\in D^+$, the composite which applies $\theta_{A,B}$ and then $\theta_{A\otimes B,C}$ agrees with $\theta_{A,B\otimes C}$, after associating the three tensor factors. To prove the unit identity, transpose it and use the unit compatibility of (EX.11): both maps become $\epsilon_A$. To prove associativity, transpose both composites. The defining equation (EX.24) replaces the outer trace by $\epsilon_A\otimes1_B\otimes1_C$; the projection associativity proved above identifies the source maps. The resulting transposes are equal, so the original maps are equal. The same argument with tensor symmetry supplies its Koszul signs.

The comparison also respects composition (EX.13). For $Z\xrightarrow gY\xrightarrow fX$, the map for $fg$ equals the composite

\[
g^!f^!A\otimes g^{-1}f^{-1}B
\xrightarrow{\theta_g}
g^!(f^!A\otimes f^{-1}B)
\xrightarrow{g^!\theta_f}
g^!f^!(A\otimes B).
\tag{EX.25}
\]

Transposing successively along $g$ and $f$ turns this into the trace (EX.14) tensored with $B$. The same transpose defines the left side, using the proper-support composition identification and the projection formula. Thus they coincide. This proof keeps the normalization of the composite trace visible.

### SH02-EX-HOM — Exceptional inverse image of internal Hom

For $A\in D^b(k_X)$ and $B\in D^+(k_X)$, there is a canonical isomorphism

\[
f^!R\mathcal Hom_X(A,B)
\xrightarrow{\sim}
R\mathcal Hom_Y(f^{-1}A,f^!B).
\tag{EX.26}
\]

Define its map by applying (EX.23) to $R\mathcal Hom(A,B)$ and $A$, then applying $f^!$ to evaluation, and finally currying. To prove it is invertible, test against an arbitrary $C\in D^+(k_Y)$:

\[
\begin{aligned}
\operatorname{Hom}(C,f^!R\mathcal Hom(A,B))
&\simeq\operatorname{Hom}(Rf_!C,R\mathcal Hom(A,B))\\
&\simeq\operatorname{Hom}(Rf_!C\otimes^L A,B)\\
&\simeq\operatorname{Hom}(Rf_!(C\otimes^L f^{-1}A),B)\\
&\simeq\operatorname{Hom}(C\otimes^L f^{-1}A,f^!B)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(f^{-1}A,f^!B)).
\end{aligned}
\]

Each tensor belongs to $D^+$ because $A$ is bounded and the coefficient ring has finite global dimension. The map represented by this chain is the map just defined: tracing evaluation through the adjunction gives exactly (EX.24). Yoneda therefore proves (EX.26), including naturality. In particular, merely replacing the hypothesis $A\in D^b$ by $A\in D^-$ is not justified by this proof; tensoring such an $A$ with $C\in D^+$ can leave $D^+$.

Composition compatibility of (EX.26) follows by applying its definition to evaluation and using (EX.25). Both composites are the curry of the same evaluated tensor map. Open restriction compatibility follows from (EX.16) and the open restriction of internal Hom. These are the compatibilities needed when using the identity on a diagonal or on a small neighborhood.

## SH02-EX-DIAGONAL — Diagonals and product tests

Assume $X$ has finite compact-support cohomological dimension over $\mathbb Z$. For the projections $q_1,q_2:X\times X\to X$ and the diagonal $\Delta$, let $F\in D^+(k_X)$ and $G\in D^b(k_X)$. Then

\[
R\mathcal Hom_X(G,F)
\simeq
Rq_{1*}R\Gamma_\Delta
R\mathcal Hom_{X\times X}(q_2^{-1}G,q_1^!F).
\tag{EX.27}
\]

The dimension assumption makes $q_1^!$ available, because its fibres are copies of $X$. Let $\delta:X\to X\times X$ be the diagonal embedding, which is closed by the Hausdorff hypothesis, and abbreviate the internal Hom on the right by $H$. Formula (EX.15) rewrites $R\Gamma_\Delta H$ as $\delta_*\delta^!H$. Since $q_1\delta=\mathrm{id}$, its ordinary direct image is $\delta^!H$. Now apply (EX.26) to $\delta$:

\[
\delta^!H
\simeq R\mathcal Hom_X(\delta^{-1}q_2^{-1}G,\delta^!q_1^!F)
\simeq R\mathcal Hom_X(G,F).
\]

The last equality uses both projection–diagonal composites and (EX.13), with their identity normalizations. Thus there is no extra dimension shift in this abstract formula.

### SH02-EX-RECTANGLE — A product test for duality

Let $X,Y$ be locally compact Hausdorff, with $Y$ of finite compact-support cohomological dimension over $\mathbb Z$. Denote the projections of $X\times Y$ by $q_X,q_Y$. For $F\in D^+(k_X)$ and $G\in D^b(k_Y)$,

\[
R\Gamma\bigl(X\times Y;
R\mathcal Hom(q_Y^{-1}G,q_X^!F)\bigr)
\simeq
\mathbf{RHom}_k\bigl(R\Gamma_c(Y;G),R\Gamma(X;F)\bigr).
\tag{EX.28}
\]

No finite cohomological dimension of $X$ is required here. Apply (EX.20) to $q_X$ and then take derived global sections. Proper-support base change for the square over a point gives

\[
Rq_{X!}q_Y^{-1}G\simeq a_X^{-1}R\Gamma_c(Y;G),
\]

where $a_X:X\to\{\mathrm{pt}\}$. The usual inverse-image/direct-image adjunction, in its derived Hom form, identifies

\[
\mathbf{RHom}_X(a_X^{-1}A,F)
\simeq\mathbf{RHom}_k(A,R\Gamma(X;F)).
\]

Take $A=R\Gamma_c(Y;G)$, which is bounded by the finite dimension assumption. Combining these two identities proves (EX.28). Its map is fixed by the proper-support base-change map, evaluation, and the traces already constructed.

The product formula remains valid for left modules over an arbitrary associative ring $A$, when both sides are interpreted as complexes of abelian groups and all Hom functors are $A$-linear. Use the direct proof (EX.20a) and the ordinary $A$-linear inverse-image/direct-image adjunction. This extension does not use a tensor product of two left $A$-modules and does not require commutativity.

The same coefficient clarification applies to the diagonal formula needed for homological-dimension estimates. Its internal Hom is an abelian sheaf, and the supported operation is the integral one. For a closed embedding $i$ one has the mixed identity

\[
i_{\mathbb Z}^!R\mathcal Hom_A(P,Q)
\simeq R\mathcal Hom_A(i^{-1}P,i_A^!Q)
\tag{EX.28a}
\]

for bounded $P$ and bounded-below $Q$. Here is a proof specific to the closed inclusion, so no noncommutative tensor convention is implicit. If $I$ is injective as an $A$-module sheaf, a local $A$-linear map into $I$ is supported on the closed subset exactly when its image lies in $\Gamma_ZI$. Consequently $\Gamma_Z\mathcal Hom_A(P,I)=\mathcal Hom_A(P,\Gamma_ZI)$ at the sheaf level. The terms $\mathcal Hom_A(P^j,I^l)$ are flabby, as above; flabby sheaves are acyclic for sheaf local cohomology on a closed subset, as follows from the localization sequence and surjectivity of restriction to the complementary open. Also $i^{-1}\Gamma_ZI=i_A^!I$ is injective, since $i_*$ is exact. Resolve $Q$ by injectives and totalize; the boundedness of $P$ keeps this a bounded-below calculation. These observations derive the sheaf identity and prove (EX.28a). Applying it to the closed diagonal proves (EX.27) for arbitrary associative $A$, with the same identity normalizations and no added shift.

## SH02-EX-DUALIZING — Dualizing objects and supported dual sections

For a map satisfying (EX.1), define its relative dualizing complex by

\[
\omega_{Y/X}=f^!k_X.
\]

If $a_X:X\to\{\mathrm{pt}\}$ has finite cohomological dimension for compact support, set $\omega_X=a_X^!k$. For $F\in D^b(k_X)$ define

\[
D_XF=R\mathcal Hom_X(F,\omega_X),\qquad
D'_XF=R\mathcal Hom_X(F,k_X).
\tag{EX.29}
\]

The first is Verdier duality as an operation; the name does not assert that its square is the identity on arbitrary sheaves. The second uses the constant sheaf rather than the dualizing object.

Taking $A=k_X$ in (EX.23) and using tensor symmetry gives

\[
f^{-1}B\otimes^L\omega_{Y/X}\longrightarrow f^!B.
\tag{EX.30}
\]

Its trace is integration against the relative dualizing object, tensored with $B$. Invertibility for topological submersions is a further theorem; it is not part of the definition of $\omega_{Y/X}$.

For composable maps to a point, (EX.13) gives $f^!\omega_X\simeq\omega_Y$. For $F\in D^b(k_X)$, (EX.26) therefore gives the useful typed identity

\[
f^!D_XF\simeq D_Y(f^{-1}F),
\tag{EX.31}
\]

whenever the dualizing objects and $f^!$ are defined under the stated finite dimension assumptions. This identity does not assume biduality of $F$.

### SH02-EX-DUAL-SECTIONS — Duality of ordinary and supported sections

If $X$ has finite compact-support cohomological dimension and $F\in D^b(k_X)$, (EX.21) for $a_X$ gives

\[
R\Gamma(X;D_XF)
\simeq\mathbf{RHom}_k(R\Gamma_c(X;F),k).
\tag{EX.32}
\]

Taking degree zero yields its ordinary derived-category Hom version. Restricting to an open subset $U$ and using (EX.16), (EX.26) and $\omega_U\simeq\omega_X|_U$ gives

\[
R\Gamma(U;D_XF)
\simeq\mathbf{RHom}_k(R\Gamma_c(U;F|_U),k).
\tag{EX.33}
\]

The open subset inherits the finite dimension bound, since open extension by zero is exact and preserves compactly supported cohomology.

For a compact subset $K\subset X$, write $i:K\hookrightarrow X$. It is closed. Formula (EX.31) identifies $i^!D_XF$ with $D_K(i^{-1}F)$. Hence

\[
R\Gamma_K(X;D_XF)
\simeq\mathbf{RHom}_k(R\Gamma(K;i^{-1}F),k).
\tag{EX.34}
\]

Indeed, the left side is $R\Gamma(K;i^!D_XF)$ by (EX.15); apply (EX.32) on $K$ and use compactness to replace compact support by ordinary global sections. The finite dimension bound on $K$ follows from the exact closed direct image into $X$. Notice that (EX.34) uses the restriction of $F$ to $K$, whereas the left side uses sections of its dual supported on $K$. These are different operations.

Finally, for a locally closed subset $Z\subset X$, apply (EX.21) to its extension-by-zero constant sheaf. With $R\Gamma_Z(X;-)$ denoting derived global sections with that locally closed support convention, this gives

\[
R\Gamma_Z(X;\omega_X)
\simeq\mathbf{RHom}_k(R\Gamma_c(Z;k_Z),k).
\tag{EX.35}
\]

The equality is also obtained directly by factoring the inclusion and using $i^!\omega_X=\omega_Z$. Its definition and independence of the factorization are those fixed in (EX.15).

## SH02-EX-SUPPORT-ERASURE — Forgetting support and checking the resulting maps

Let $\pi_f:Rf_!\to Rf_*$ be the natural transformation which forgets the proper-support condition. It is the derived transformation induced by inclusion of properly supported sections in all sections. The identities below distinguish several maps that would otherwise look identical in a formula containing only stars and exclamation marks.

Keep the cartesian square of `SH02-EX-BASECHANGE`. Put

\[
b_!:g^{-1}Rf_!\xrightarrow{\sim}Rf'_!g'^{-1},
\qquad
b_*:g^{-1}Rf_*\longrightarrow Rf'_*g'^{-1}.
\]

Here $b_*$ is the ordinary base-change morphism from inverse-image/direct-image adjunction; it need not be invertible. There is the compatibility

\[
(\pi_{f'}g'^{-1})\circ b_!
=b_*\circ(g^{-1}\pi_f).
\tag{EX.36}
\]

At the sheaf level, both maps take a properly supported section to its pullback regarded as an unrestricted section. To derive this equality with the canonical maps, choose the flat-soft model (EX.4) for $Rf_!$ and an injective resolution of that model for the ordinary direct images. The comparison from the soft model to the injective one induces $\pi_f$; inverse image is exact, and the adjunction definition of $b_*$ applied to that comparison is pullback of the same sections. The sheaf-level equality is therefore an equality of the induced morphisms in the derived category. Changing resolutions leaves it unchanged by functoriality of derived transformations. This argument also proves that $\pi$ respects compositions: forgetting support in two stages is the same inclusion of sections as forgetting it for the composite map.

The mixed proper/ordinary exchange map

\[
e:Rf_!Rg'_*\longrightarrow Rg_*Rf'_!
\tag{EX.37}
\]

is defined as follows. Apply $g^{-1}$, use $b_!$, and then apply the ordinary counit $g'^{-1}Rg'_*\to\mathrm{id}$; transpose the resulting map along $g^{-1}\dashv Rg_*$. It satisfies a useful two-path identity from $Rf_!Rg'_!$ to the ordinary direct image of the composite $fg'=gf'$. One path forgets both supports immediately. The other first applies $Rf_!\pi_{g'}$, then $e$, and finally $Rg_*\pi_{f'}$. The ordinary composition isomorphism identifies their targets, and the paths agree.

For a proof, transpose the second path along $g^{-1}\dashv Rg_*$. Its defining $e$ becomes $b_!$ followed by the ordinary counit. Move the map $\pi_{f'}$ past $b_!$ by (EX.36); this gives $b_*$ followed by the same counit. The latter is exactly the adjunction description of the ordinary direct image of $fg'=gf'$. The remaining support-forgetting map is $\pi$ for the composite, by its composition compatibility. This is the transpose of the first path. The adjunction bijection proves the claimed equality.

We will use the slightly stronger intermediate identity

\[
e\circ(Rf_!\pi_{g'})
=(\pi_g Rf'_!)\circ\kappa,
\quad
\kappa:Rf_!Rg'_!\xrightarrow{\sim}Rg_!Rf'_!.
\tag{EX.37a}
\]

The isomorphism $\kappa$ is proper-support composition along the equality $fg'=gf'$. To check (EX.37a), transpose along $g^{-1}\dashv Rg_*$. The left transpose is proper-support base change followed by the map $g'^{-1}Rg'_!\to\mathrm{id}$ which evaluates a properly supported section at its pulled-back germ. The right transpose uses the same evaluation after proper-support composition. At the sheaf level they evaluate the identical section; support is only forgotten in the outer $g$ direction. The proper-support resolutions, their composition comparison and the finite base-change bridge derive this equality, since all maps used are these same section maps on the resolutions. This proves (EX.37a) before applying $Rg_*\pi_{f'}$, and in particular proves the preceding two-path identity.

For a further exchange involving exceptional inverse image in the vertical direction, assume **also** that $g_!$ has finite integral cohomological dimension. Then $g'^!$ and $g^!$ exist, because $g'$ is a base change of $g$. Define

\[
c:Rf'_!g'^!\longrightarrow g^!Rf_!
\tag{EX.38}
\]

by transposing along $Rg_!\dashv g^!$ the composite

\[
Rg_!Rf'_!g'^!\simeq Rf_!Rg'_!g'^!
\xrightarrow{Rf_!\epsilon_{g'}}Rf_!.
\]

Let $d:Rf'_*g'^!\xrightarrow{\sim}g^!Rf_*$ be (EX.17), applied with the horizontal and vertical directions exchanged and then inverted to the displayed direction. The compatibility is

\[
(g^!\pi_f)\circ c=d\circ(\pi_{f'}g'^!).
\tag{EX.39}
\]

To check it, transpose both maps along $Rg_!\dashv g^!$. The left transpose is the composite defining $c$ followed by $\pi_f$. The transpose of $d$ on the right is the exchange $Rg_!Rf'_*\to Rf_*Rg'_!$ followed by $Rf_*\epsilon_{g'}$. Apply (EX.37a) with the two directions exchanged: precomposing that exchange with $Rg_!\pi_{f'}$ is proper-support composition followed by $\pi_f Rg'_!$. Naturality of $\pi_f$ moves this map past the trace $\epsilon_{g'}$. The result is exactly the left transpose. Thus the transposes, and hence the maps, agree.

The extra hypothesis in (EX.38) is necessary for the functors in its statement to have been constructed. Finite cohomological dimension of $f_!$ alone, which suffices for (EX.17) and (EX.37), does not supply $g^!$.

### SH02-EX-HOM-SUPPORT-COMPATIBILITY — Evaluation when either support is forgotten

Let $F\in D^+(k_X)$, $G\in D^b(k_Y)$, and set $H=R\mathcal Hom_Y(G,f^!F)$. There is a second supported evaluation map

\[
u:Rf_!H\longrightarrow R\mathcal Hom_X(Rf_*G,F).
\tag{EX.40}
\]

It is defined by currying the pairing obtained from the ordinary counit $f^{-1}Rf_*G\to G$, evaluation into $f^!F$, the projection isomorphism, and the trace $\epsilon_F$. In detail, its transpose as a tensor pairing is

\[
Rf_!H\otimes^L Rf_*G
\longrightarrow Rf_!(H\otimes^L f^{-1}Rf_*G)
\longrightarrow Rf_!(H\otimes^LG)
\longrightarrow Rf_!f^!F\longrightarrow F.
\]

The two paths from $Rf_!H$ to $R\mathcal Hom_X(Rf_!G,F)$ agree:

\[
R\mathcal Hom(\pi_G,F)\circ u
=v\circ\pi_H,
\tag{EX.41}
\]

where $v:Rf_*H\xrightarrow{\sim}R\mathcal Hom_X(Rf_!G,F)$ is (EX.20). To verify the identity, curry both sides back against $Rf_!G$. The first path pairs a properly supported section of $H$ with a properly supported section of $G$, after forgetting support on the second factor. The second path uses the same evaluation but forgets support on the first factor. Both sections together give the same evaluation in $f^!F$, with support contained in the intersection of the two supports, and then the same trace. On soft and flat resolutions the two evaluations are the same chain map, with the tensor symmetry signs already fixed in (EX.22). The support-forgetting and projection compatibilities therefore give (EX.41) in the derived category.

There is a boundedness issue if one attempts to state this entire diagram for unrestricted $G\in D^+$. Its object $H$ can be unbounded below, so $Rf_!H$ is outside the domain of the $D^+$ functor constructed in this lesson. For example, on a point over a field, take $G=\bigoplus_{n\geq0}k[-n]$ and $F=k$. Then $G\in D^+$, whereas $R\operatorname{Hom}(G,k)$ has nonzero cohomology in every degree $-n$. An extension of (EX.40)–(EX.41) to all such inputs requires an unbounded proper-direct-image construction and its comparison proofs. That extension is an explicit outstanding prerequisite; the bounded diagram proved here is not counted as its replacement.

### SH02-EX-COEFFICIENT-ACTION — The coefficient action and the relative dualizing map

For $A,B\in D^b(k_X)$, put $P=f^{-1}R\mathcal Hom_X(A,B)$ and write $\tau_C:f^{-1}C\otimes\omega_{Y/X}\to f^!C$ for (EX.30). There are two ways to obtain a map

\[
P\longrightarrow
R\mathcal Hom_Y(f^{-1}A\otimes\omega_{Y/X},f^!B).
\tag{EX.42}
\]

The first pulls Hom back in the ordinary sense, obtaining $P\to R\mathcal Hom(f^{-1}A,f^{-1}B)$, then tensors the represented maps with $\omega_{Y/X}$ and postcomposes with $\tau_B$. The second uses the action

\[
P\longrightarrow R\mathcal Hom(f^!A,f^!B)
\]

defined by currying $f^!A\otimes P\xrightarrow{\theta}f^!(A\otimes R\mathcal Hom(A,B))\to f^!B$, and then precomposes with $\tau_A$.

These two maps agree. Curry both against $f^{-1}A\otimes\omega_{Y/X}$. In the second composite, replace $\tau_A$ by $\theta_{k_X,A}$ and use the associativity identity for $\theta$. It becomes the tensor comparison for the single coefficient object $A\otimes R\mathcal Hom(A,B)$, followed by its evaluation to $B$. Naturality of $\theta$ moves evaluation before that comparison, producing $\tau_B$ after ordinary pullback of evaluation. This is the first composite, including the symmetry used to place the factors in evaluation order. All applications of $f^!$ here have bounded-below inputs. The internal Hom targets may be viewed in the unbounded derived category already supplied by the open internal-Hom prerequisite; no unbounded $Rf_!$ is applied in this argument.

## SH02-EX-EXAMPLE-DISCRETE — Worked tests and exercises with solutions

**An arbitrary discrete fibre.** Let $S$ be any discrete set and let $a:S\to\{\mathrm{pt}\}$. A compact subset of $S$ is finite, so $a_!$ is the direct sum functor on families of modules. It is exact and has cohomological dimension zero. Its right adjoint sends a module to the constant family with that module in each component:

\[
\operatorname{Hom}_k\left(\bigoplus_{s\in S}M_s,N\right)
=\prod_{s\in S}\operatorname{Hom}_k(M_s,N).
\]

Thus $a^!N=N_S$ and $\omega_S=k_S$, with no shift, for finite or infinite $S$. The trace $\bigoplus_SN\to N$ adds the finitely many nonzero components of each vector. For $S=\varnothing$ the right adjoint is the zero object in the zero sheaf category and its trace is $0\to N$. This example tests coproducts, units and the zero-dimensional bound without any finite-rank hypothesis.

### SH02-EX-EXERCISE-BASECHANGE — A noninvertible base-change map

**Exercise.** Let $i:\{0\}\hookrightarrow\mathbb R$ and pull $i$ back along itself. For a nonzero coefficient ring $k$, compute the exceptional inverse-image base-change map (EX.17) on $k_{\mathbb R}$ and decide whether it is invertible.

**Solution.** The cartesian top map and left map are identities of a point. Formula (EX.15) identifies $i^!k_{\mathbb R}$ with the local-cohomology complex at zero. On a small interval $V$ about zero, the localization triangle has middle term $R\Gamma(V;k)=k$ and complementary term $R\Gamma(V\setminus\{0\};k)=k\oplus k$, both in degree zero. These elementary interval computations use the constant-sheaf interval acyclicity prerequisite. The intervening map is the diagonal $k\to k\oplus k$. Its kernel is zero and its cokernel is $k$, so the supported complex is $k[-1]$. The base-change map is consequently a map $k[-1]\to k$. Its degree-one source cohomology is $k$, whereas the target has no degree-one cohomology. It cannot be a quasi-isomorphism. This is the exceptional inverse-image comparison, not a counterexample to the proper-support base-change isomorphism used to define it.

### SH02-EX-EXERCISE-COMPONENTS — Open and closed components

**Exercise.** Let $X=U\sqcup Z$ be a disjoint union of two open and closed subspaces. Describe $j^!$, $i^!$ and the two traces for the inclusions. Check the localization triangle on an arbitrary $F\in D^+(k_X)$.

**Solution.** A sheaf or complex on $X$ is a pair $(F_U,F_Z)$. Both inclusions are open, so their exceptional inverse images are the corresponding restrictions. Both are closed, so supported local cohomology is the pair $(F_U,0)$ or $(0,F_Z)$. The traces are the inclusions of those summands. The localization triangle is the split triangle

\[
(0,F_Z)\longrightarrow(F_U,F_Z)\longrightarrow(F_U,0)
\longrightarrow(0,F_Z)[1],
\]

whose connecting map is zero. This directly reconciles the open and closed descriptions of an exceptional inverse image when both apply.

### SH02-EX-EXERCISE-AMPLITUDE — Dimension bounds under composition

**Exercise.** Suppose the integral dimensions of $g_!$ and $f_!$ are at most $s$ and $r$. Give a lower bound for $(fg)^!F$ if $F\in D^{\geq a}$, and compare the direct construction with successive exceptional inverse images. Explain why this is not a proof that $(fg)^!$ preserves bounded complexes.

**Solution.** The direct construction uses a finite flat-soft resolution of length at most $r+s$, hence gives $(fg)^!F\in D^{\geq a-r-s}$. The successive construction gives $f^!F\in D^{\geq a-r}$ and then $g^!f^!F\in D^{\geq a-r-s}$. Their normalized isomorphism (EX.13) identifies these conclusions. The construction uses an injective resolution of $F$, which need not terminate in the sheaf category, so no finite upper bound has been proved. Lower boundedness alone does not establish membership in $D^b$.

### SH02-EX-EXERCISE-TRACE — Testing the trace sign

**Exercise.** In (EX.23), replace the trace $\epsilon$ by $-\epsilon$ while retaining the same unit. Is this another normalized tensor comparison for the same adjunction? What changes if the coefficient ring has characteristic two?

**Solution.** The first triangle identity in (EX.10) becomes $-1$ rather than $1$, so this does not preserve the given adjunction unless $1=-1$ on all the relevant objects. It also makes $\theta_{A,k_X}$ equal to $-1$ instead of the required unit. In characteristic two these particular signs coincide, but that coincidence gives no freedom to alter formulas over a general coefficient ring. The question illustrates why identifying the underlying functor does not by itself fix an adjunction normalization.

## What this construction supports

The lesson supplies a resolution model for $f^!$, the trace and unit, restriction and composition, the two different base-change comparisons, tensor and internal-Hom identities, and the abstract dualizing objects. The exact topological imports are isolated in `SH02-EX-FOUNDATIONS`; the interval computation in the worked costalk test is a separate elementary acyclicity prerequisite. Identifying $\omega$ with an orientation local system, proving the submersion tensor comparison invertible, and proving a biduality theorem with its full finiteness hypotheses belong to the subsequent manifold and duality lessons.

The same results are treated in Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §§4.3–4.7: soft and compactly soft sheaves, finite cohomological dimension, projection, proper-support base change, exceptional adjunction, internal Hom and dual sections. The projection theorem there has bounded/ bounded-above input conventions, and the existence theorem for the exceptional right adjoint invokes Brown representability from a separate reference. It therefore does not replace the explicit finite soft resolution and representing-sheaf construction given here. Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §1.3.5, provides the manifold internal exceptional-Hom formulas with their bounded first input.

The construction above fixes every comparison by its adjoint evaluation or counit, retains finite cohomological dimension for proper-support image, and proves the stated bounded-below functor range with the finite flat/soft model. In particular the closed-embedding exceptional-to-ordinary map need not be invertible. The unbounded internal-Hom extension described earlier remains an open obligation in this lesson: these source passages do not establish an unbounded exceptional-image theory or remove the stated range restriction. Original exposition, examples and reader code are dedicated under CC0 1.0 Universal; human works retain their own rights.
