# SH02-UR — Finite resolutions without a lower bound

This unit proves an unbounded classical proper-support adjunction and its support-comparison square. It also proves an unbounded deformation theorem on finite-dimensional manifolds. The full unbounded microsupport estimates are a separate obligation, identified at the end; they are not consequences claimed here.

Write $D(k_X)$ for the classical derived category of all complexes of sheaves of $k$-modules on $X$. Cohomological differentials have degree $1$. Tensor totalizations use direct sums, and Hom complexes use products. An unbounded complex of flat sheaves need not be K-flat, and an unbounded complex of injective sheaves need not be K-injective. We will verify the required stronger properties where they occur.

The proper-support results concern a continuous map $f:Y\to X$ between locally compact Hausdorff spaces and a commutative unital ring $k$. Assume one integer $r\geq0$ satisfies

\[
R^qf_!A=0\qquad(q>r)
\tag{UR1}
\]

for every sheaf of **abelian groups** $A$ on $Y$. The bound is integral and uniform; a bound only for selected coefficient sheaves is not being substituted. No manifold, constructibility, rank, or finite-global-dimension assumption is needed for these results. The deformation statements use a finite-dimensional manifold, and allow an arbitrary unital coefficient ring because they do not use tensor products.

## SH02-UR-IMPORTS — The unbounded classical prerequisites

A Grothendieck abelian category has K-injective replacements with injective terms: [Tag 079P](https://stacks.math.columbia.edu/tag/079P). The complete programme construction is *K-injective resolutions in Grothendieck abelian categories*, Theorem 4.1, with the size and extension arguments in Sections 2–3. Here K-injective means that $\operatorname{Hom}^{\bullet}(A,I)$ is acyclic for every acyclic complex $A$. Secondly, if a left exact additive functor has enough acyclic objects and finite cohomological dimension, its right derived functor exists on the entire derived category; **every complex of acyclic objects for that functor computes it**, with no boundedness assumption: [Tag 07K7](https://stacks.math.columbia.edu/tag/07K7). The programme proof of the acyclic-model assertion for every functor used here is Proposition 5.5 of that same reading. Its source category is Grothendieck and its target is any abelian category, so it covers both module-valued and sheaf-valued operations below. The uniform bound also gives cohomological amplitude on arbitrary complexes; the [argument below](#finite-cohomological-amplitude) proves that deduction explicitly. The uniform dimension hypothesis is indispensable to this use of acyclic resolutions.

Sheaves of $k$-modules form a Grothendieck abelian category: filtered colimits are exact on stalks, and the coproduct of the open generators $k_U$, one for each open subset $U$, is a generator. Indeed a nonzero sheaf morphism is nonzero on some section of some open set, and such a section defines a morphism from $k_U$. This checks the category hypothesis of the first import.

The other unbounded inputs are already exact contracts in the prerequisite lesson: `SH02-IMP-KFLAT` and `SH02-IMP-TENSOR` give termwise-flat K-flat replacements and derived tensor; `SH02-IMP-ADJUNCTION` gives $f^{-1}\dashv Rf_*$; `SH02-IMP-RHOM` gives internal derived Hom, tensor–Hom adjunction, and open restriction. For constant coefficients inverse image is exact, so its left derived functor is itself. These are imports about classical module sheaves, not an identification with all sheaves valued in a non-hypercomplete infinity-category. The programme proofs are *Flat modules and K-flat resolutions*, Theorem 3.1, *The derived tensor product and Tor sheaves*, Theorem 2.2, *Derived pullback and pushforward*, Theorem 2.2 and Corollary 2.3, and *Hom complexes, internal derived Hom and Ext sheaves*, Theorems 2.2 and 3.1. These constructions act on the full unbounded categories; their finite-rank or bounded variants are not being substituted.

The topological inputs are exactly those used in [exceptional operations](exceptional-operations.md): `SH02-EX-FLAT-SOFT`, `SH02-EX-FINITE-RESOLUTION`, `SH02-EX-REPRESENTING-SHEAF`, and the underived flat-soft projection calculation in `SH02-EX-PROJECTION`. Their compact-support and fibre prerequisites remain visible there. In particular they provide an augmented complex

\[
0\longrightarrow\mathbb Z_Y\longrightarrow K^0\longrightarrow\cdots
\longrightarrow K^r\longrightarrow0,
\tag{UR2}
\]

with every $K^p$ flat over $\mathbb Z$ and $f$-soft. Each constituent short exact sequence has flat cokernel. For every $k_Y$-module $M$, the sheaf $M\otimes_{\mathbb Z}K^p$ is $f$-soft and the functor

\[
T_p(M)=f_!(M\otimes_{\mathbb Z}K^p)
\tag{UR3}
\]

is exact and preserves coproducts. The integral bound (UR1) also bounds the $k$-linear derived functor after forgetting scalars. More directly, for every $k_Y$-module $M$, the pure exact augmentation (UR2) makes $M\otimes_{\mathbb Z}K^\bullet$ a resolution in degrees $0,\ldots,r$. Its terms are $f$-soft and hence $f_!$-acyclic by the stated flat-soft input. The bounded-below acyclic-resolution theorem computes $Rf_!M$ from this length-$r$ complex, proving $R^qf_!M=0$ for $q>r$ over $k$. This verifies the uniform dimension hypothesis directly; it requires no preservation of injectives by forgetting scalars. In particular injectives are $f_!$-acyclic, so the finite-dimensional acyclic-model comparison applies to $f_!$.

<a id="finite-cohomological-amplitude"></a>

### The uniform cohomological amplitude bound

Let $T:\mathcal A\to\mathcal B$ be left exact and additive, with $\mathcal A$ Grothendieck and $\mathcal B$ abelian. Assume $R^qT(M)=0$ for every object $M$ and every $q>d$, for one integer $d\geq0$. The right derived functor exists on all complexes by the K-injective construction just linked. We prove

\[
RT(D^{\geq a})\subset D^{\geq a},
\qquad RT(D^{\leq b})\subset D^{\leq b+d}.
\tag{URA1}
\]

For the lower bound, an object with no cohomology below $a$ has a bounded-below representative starting in degree $a$. The bounded-below injective construction, Theorem 4.1, resolves it by injectives with no terms below $a$. That complex is K-injective, so it also computes the unbounded derived functor. Applying $T$ leaves its terms below $a$ zero.

For the upper bound, let $I$ be a K-injective representative with injective terms and $H^j(I)=0$ for $j>b$. Write $Z^j=\ker(d_I^j)$. For every $j>b$ the cycle sequence

\[
0\longrightarrow Z^{j-1}\longrightarrow I^{j-1}
\longrightarrow Z^j\longrightarrow0
\tag{URA2}
\]

is exact. Left exactness identifies the degree-$j$ cycles of $T(I)$ with $T(Z^j)$. The long exact sequence of (URA2), and acyclicity of the injective middle term, therefore identify

\[
H^j(T(I))\simeq R^1T(Z^{j-1}),
\qquad
R^qT(Z^j)\simeq R^{q+1}T(Z^{j-1})\quad(q>0).
\tag{URA3}
\]

If $j>b+d$, all the cycle sequences with indices $j,j-1,\ldots,j-d$ lie in that exact tail. Applying the second identification $d$ times gives

\[
H^j(T(I))\simeq R^{d+1}T(Z^{j-d-1})=0.
\tag{URA4}
\]

For $d=0$ the first identification in (URA3) already vanishes by the dimension hypothesis. This proves the upper bound without a lower cohomological bound on $I$: only $d$ successive dimension shifts are used for each $j$. All identifications come from kernels and the natural connecting maps of the cycle sequences, so they are compatible with resolution comparisons. Infinite endpoints impose no extra assertion on the corresponding side. Together with Proposition 5.5, this proves the acyclic-complex computation and amplitude used in this reading.

## SH02-UR-PROPER-IMAGE — A finite model for unbounded proper direct image

**Theorem.** For every $G\in D(k_Y)$, represented by any complex with the same name,

\[
Rf_!G\simeq\operatorname{Tot}_{\oplus}
 f_!(G\otimes_{\mathbb Z}K^\bullet).
\tag{UR4}
\]

This is the right derived functor of the usual proper direct image. It restricts to the previously constructed functor on $D^+$, and takes $D^{[a,b]}$ into $D^{[a,b+r]}$, allowing infinite endpoints.

**Proof.** Put $E(G)=\operatorname{Tot}(G\otimes_{\mathbb Z}K^\bullet)$. The augmentation $G\to E(G)$ is a quasi-isomorphism. To check convergence explicitly, include the augmentation as an extra column. Filter its total complex by horizontal degree; there are at most $r+2$ columns, so this filtration converges with finitely many steps in every total degree. Its first page is vertical cohomology. Flatness of the augmented terms identifies that page with $H^i(G)\otimes_{\mathbb Z}K^p$, including $H^i(G)$ in the augmentation column. The horizontal complexes on this page are exact because (UR2) is pure exact. Thus the second page is zero, and finite convergence makes the augmentation cone acyclic even when the vertical degree ranges over all integers.

Every term of $E(G)$ is a finite sum of sheaves of the form $G^i\otimes_{\mathbb Z}K^p$, hence is $f$-soft and $f_!$-acyclic. By Proposition 5.5, applying $f_!$ to this complex computes $Rf_!G$. Since $f_!$ is additive, this is (UR4). The amplitude is [URA1](#finite-cohomological-amplitude), applied to the uniform bound (UR1). On bounded-below complexes this is the identical augmented resolution used for the earlier construction, so the comparison is the usual derived comparison. $\square$

There is also a useful direct check: the functor on complexes in (UR4) sends acyclic complexes to acyclic complexes. Each $T_p$ is exact, and totalization has only finitely many $p$-columns. Consequently it sends quasi-isomorphisms to quasi-isomorphisms. The natural comparison in Proposition 5.5 identifies this explicit complex functor with the right derived functor, rather than merely producing some functor with similar values.

## SH02-UR-EXCEPTIONAL-ADJOINT — A K-injective model for the right adjoint

For an arbitrary $k_X$-module $I$, define a sheaf on $Y$ by

\[
J_p(I)(U)=\operatorname{Hom}_{k_X}
       \bigl(T_p(k_U),I\bigr).
\tag{UR5}
\]

The construction in `SH02-EX-REPRESENTING-SHEAF` works without assuming that $I$ is injective. To make that point explicit, an open cover of $U$ gives a right-exact presentation of $k_U$ by the coproducts of $k_{U_i}$ and $k_{U_i\cap U_j}$. Exactness and preservation of coproducts by $T_p$, followed by the left exact contravariant functor $\operatorname{Hom}(-,I)$, turn this presentation into the sheaf equalizer. Presenting an arbitrary sheaf by open generators then gives

\[
\operatorname{Hom}(T_pM,I)=\operatorname{Hom}(M,J_pI).
\tag{UR6}
\]

Injectivity of $I$ is needed only for the further conclusion that $J_pI$ is injective. That conclusion follows because $T_p$ is exact.

Let $I$ now be a K-injective complex representing $F\in D(k_X)$. Form the finite Hom totalization $J(I)$ with

\[
J(I)^n=\bigoplus_{p=0}^r J_p(I^{n+p}).
\tag{UR7}
\]

The differential is the Hom differential: for a homogeneous family $h$ of degree $n$, it is $d_Ih-(-1)^n h d_K$. In the second term $d_K$ acts by precomposition, using contravariance in $K$. The componentwise adjunctions (UR6) give an isomorphism of Hom complexes

\[
\operatorname{Hom}^{\bullet}
 \left(\operatorname{Tot}T_\bullet(G),I\right)
\simeq\operatorname{Hom}^{\bullet}(G,J(I)).
\tag{UR8}
\]

For each $p$ the ordinary Hom complex has a product over the degrees of $G$. Interchanging that product with the **finite** sum over $p$ is valid. The displayed Hom differential gives the signs in (UR8); there is no replacement of an infinite product by a sum.

**Theorem.** The assignment $f^!F=J(I)$ defines a right adjoint to $Rf_!$ on the full unbounded derived categories. Its unit and counit restrict to the earlier ones, and $f^!D^{\geq a}\subset D^{\geq a-r}$.

**Proof.** If $A$ is acyclic, the direct check following (UR4) makes $\operatorname{Tot}T_\bullet(A)$ acyclic. K-injectivity of $I$ and (UR8) therefore show that $J(I)$ is K-injective. Hence (UR8), in degree-zero cohomology, identifies derived morphisms on both sides:

\[
\operatorname{Hom}_{D(k_X)}(Rf_!G,F)
\simeq\operatorname{Hom}_{D(k_Y)}(G,f^!F).
\tag{UR9}
\]

Replacing $I$ by another K-injective representative gives the same object and adjunction, since quasi-isomorphisms between K-injectives are homotopy equivalences and (UR7) preserves such equivalences. The unit and trace $\epsilon_F:Rf_!f^!F\to F$ are the transposes of identities in (UR9); they satisfy the two adjunction identities by the usual inverse transposition calculation. If $F\in D^{\geq a}$, use a bounded-below injective representative with no terms below $a$. Formula (UR7) then has no terms below $a-r$. It is precisely the earlier finite model, which proves both the amplitude assertion and compatibility with the bounded-below adjunction. Uniqueness of a right adjoint, with its counit retained, makes the comparison independent of the chosen resolution (UR2). $\square$

## SH02-UR-PROJECTION — Checking K-flatness after proper direct image

**Theorem.** For arbitrary $G\in D(k_Y)$ and $B\in D(k_X)$, the canonical projection map is an isomorphism

\[
Rf_!G\otimes_k^L B
\xrightarrow{\sim}Rf_!(G\otimes_k^L f^{-1}B).
\tag{UR10}
\]

**Proof.** Choose a termwise-flat K-flat complex $P\to G$. Put $E=E(P)$ as in (UR4). Every term of $E$ is flat over $k$ and $f$-soft. The first assertion follows on stalks: $P^i\otimes_{\mathbb Z}K^p$ tensors a $k$-module with a flat abelian group, so tensoring it over $k$ preserves exact sequences. The second assertion is the flat-soft tensor lemma over $\mathbb Z$.

The complex $E$ is K-flat over $k$. Indeed, if $A$ is an acyclic complex of $k_Y$-modules, then $P\otimes_k A$ is acyclic by K-flatness of $P$. Tensoring with each flat $K^p$ is exact; the finite totalization over $p$ is still acyclic. This totalization is $E\otimes_k A$.

The underived projection calculation for a flat $f$-soft sheaf, applied to each term and then to direct-sum tensor totalizations, gives a natural identity of complexes for every complex $B$:

\[
(f_!E)\otimes_k B\simeq
f_!(E\otimes_k f^{-1}B).
\tag{UR11}
\]

Here $f_!$ commutes with the coproducts in each tensor degree. Each term on the right is $f$-soft: it is a sum of sheaves
$(P^i\otimes_k f^{-1}B^j)\otimes_{\mathbb Z}K^p$, to which the same flat-soft lemma applies. The terms of $B$ need not be flat.

We must prove that $f_!E$ is K-flat; termwise flatness alone would not suffice. If $B$ is acyclic, exact inverse image and K-flatness of $E$ make $E\otimes_k f^{-1}B$ acyclic. It is a complex of $f_!$-acyclic terms, so Proposition 5.5 makes the right side of (UR11) acyclic. Thus the left side is acyclic for every such $B$, which is exactly K-flatness of $f_!E$.

Now let $B$ be arbitrary. On the left of (UR11), $f_!E$ represents $Rf_!G$ and is K-flat. On the right, $E$ is K-flat and represents $G$, and Proposition 5.5 permits application of $f_!$ to the displayed soft-term complex. Thus both sides compute the derived objects in (UR10). The map is multiplication of supported sections, the same map as in the bounded calculation. Its compatibility with tensor associativity and symmetry follows from those identities on these complexes, with the ordinary cohomological Koszul signs. $\square$

## SH02-UR-INTERNAL-DUALITY — Evaluation with unbounded inputs

For every $G\in D(k_Y)$ and $F\in D(k_X)$ there is a canonical isomorphism

\[
v:Rf_*R\mathcal Hom_Y(G,f^!F)
\xrightarrow{\sim}R\mathcal Hom_X(Rf_!G,F).
\tag{UR12}
\]

**Proof.** For every $C\in D(k_X)$, the unbounded adjunctions and (UR10) give natural bijections

\[
\begin{aligned}
\operatorname{Hom}(C,Rf_*R\mathcal Hom(G,f^!F))
&=\operatorname{Hom}(f^{-1}C,R\mathcal Hom(G,f^!F))\\
&=\operatorname{Hom}(G\otimes^L f^{-1}C,f^!F)\\
&=\operatorname{Hom}(Rf_!(G\otimes^L f^{-1}C),F)\\
&=\operatorname{Hom}(Rf_!G\otimes^L C,F)\\
&=\operatorname{Hom}(C,R\mathcal Hom(Rf_!G,F)).
\end{aligned}
\tag{UR13}
\]

Yoneda gives (UR12). This also fixes its normalization: its transpose is obtained from the ordinary counit, evaluation into $f^!F$, the projection isomorphism, and the trace $\epsilon_F$. In particular its restriction is the map of `SH02-EX-INTERNAL`, with the same evaluation order. $\square$

## SH02-UR-SUPPORT-SQUARE — Forgetting either support gives the same map

There is a canonical transformation $\pi_A:Rf_!A\to Rf_*A$ for every unbounded $A$. Choose a K-injective representative $I$ with injective terms. The complex $f_!I$ computes $Rf_!A$ by Proposition 5.5, while $f_*I$ computes $Rf_*A$ by K-injectivity. The inclusion $f_!I\to f_*I$ defines $\pi_A$. This construction is independent of the representative by the derived comparison, and agrees with the usual inclusion on bounded-below objects.

For later normalization, write $e_A:f^{-1}Rf_!A\to A$ for $f^{-1}\pi_A$ followed by the ordinary counit. There is a natural pairing

\[
\beta_{A,B}:Rf_!A\otimes^L Rf_!B
\longrightarrow Rf_!(A\otimes^L B),
\tag{UR14}
\]

given by projection followed by $1\otimes e_B$. It is symmetric in the graded sense. Here is a resolution check that also identifies the maps. Choose termwise-flat K-flat representatives and their finite soft resolutions $E_A,E_B$ from the preceding proof. Their proper images are K-flat. The complex $E_A\otimes E_B$ has soft terms and is K-flat, so all proper images in (UR14) are computed on these complexes. Multiplication of two properly supported sections gives a section supported in the intersection of their supports. The resulting map

\[
f_!E_A\otimes f_!E_B\longrightarrow f_!(E_A\otimes E_B)
\tag{UR15}
\]

is unchanged if the two factors are exchanged with their Koszul sign. It represents (UR14). To verify this last assertion against the derived $e_B$, map $E_B$ to a K-injective representative $I_B$. The derived support inclusion is represented by $f_!E_B\to f_*I_B$, and its counit is represented by $f^{-1}f_*I_B\to I_B$. Naturality of multiplication identifies the resulting composite with (UR15) after $E_B\to I_B$. The target proper image is still computed by this mixed tensor complex: every term has a flat-soft $K^p$ factor from $E_A$, and K-flatness of $E_A$ preserves the quasi-isomorphism. This proves the claimed identification without treating $f_*E_B$ as a derived direct image. It also proves compatibility of (UR14) with $\pi$ in either factor.

Set $H=R\mathcal Hom_Y(G,f^!F)$ for arbitrary $F,G$ as above. Define

\[
u:Rf_!H\longrightarrow R\mathcal Hom_X(Rf_*G,F)
\tag{UR16}
\]

as the transpose of the pairing

\[
\begin{aligned}
Rf_!H\otimes^L Rf_*G
&\longrightarrow Rf_!(H\otimes^L f^{-1}Rf_*G)\\
&\longrightarrow Rf_!(H\otimes^L G)
\longrightarrow Rf_!f^!F\xrightarrow{\epsilon_F}F.
\end{aligned}
\tag{UR17}
\]

**Support-comparison theorem.** The following equality holds on all of $D(k_Y)\times D(k_X)$:

\[
R\mathcal Hom_X(\pi_G,F)\circ u
=v\circ\pi_H.
\tag{UR18}
\]

**Proof.** Transpose both sides against $Rf_!G$. Substituting $\pi_G$ in (UR17) gives

\[
Rf_!H\otimes^L Rf_!G
\xrightarrow{\beta_{H,G}}Rf_!(H\otimes^LG)
\xrightarrow{Rf_!(\mathrm{ev})}Rf_!f^!F
\xrightarrow{\epsilon_F}F.
\tag{UR19}
\]

The transposed definition of $v$ in (UR13), after precomposition by $\pi_H$, gives the same sequence with the two properly supported factors first exchanged: it uses projection on $G$, the counit $e_H$, then evaluation. By the graded symmetry and support-inclusion compatibility verified in (UR15), this is exactly (UR19). No sign is added: the symmetry moving $H$ back to the first evaluation position is the same symmetry used to compare the two beta pairings. Tensor–Hom transposition is a bijection, so equality of these pairings proves (UR18). $\square$

This proves the full bounded-below input case of the support-Hom exercise, even when its intermediate Hom is unbounded below. It does not settle a different issue in a base-change diagram: writing $g^!$ still requires an adjoint for $g$. Condition (UR1) for $f$ alone is not a hypothesis about $g$. Thus the separate definedness issue in `SH02-EX-SUPPORT-ERASURE` is unchanged.

## SH02-UR-LOCAL-WINDOW — Uniform dimension bounds for local tests

Manifolds here have the course convention: Hausdorff, without boundary, and countable at infinity. Now let $X$ be an $n$-dimensional manifold, or a closed subset of one, with $n<\infty$. Use arbitrary unital coefficients. The cohomological dimension theorem `SH02-MD-DIMENSION` in [manifold duality](manifold-duality.md) gives $H^q(V;M)=0$ for $q>n$, every open subset $V$ of the manifold, and every sheaf $M$. A closed subset inherits the bound on each of its opens: realize that open as a closed subset of an ambient open set and use exact closed direct image, which preserves injectives as a right adjoint to exact inverse image.

For an open embedding $j:U\hookrightarrow X$, $R^qj_*=0$ for $q>n$. Indeed, its stalk is the filtered colimit of $H^q(V\cap U;-)$ over open neighborhoods $V$, as follows by taking stalks of an injective resolution. For a closed subset $Z$, the localization triangle

\[
R\Gamma_Z A\longrightarrow A\longrightarrow Rj_*(A|_{X\setminus Z})\xrightarrow{+1}
\tag{UR20}
\]

gives cohomological dimension at most $n+1$ for the sheaf support functor $\Gamma_Z$. The module-valued functor of global sections supported on $Z$ has the same bound, using $R\Gamma(X;A)\to R\Gamma(X\setminus Z;A)$ instead. These functors have the uniform bounds just proved and a Grothendieck source, so they admit the unbounded computation of Proposition 5.5.

For clarity, (UR20) is valid unboundedly. Use a K-injective resolution with injective terms. The termwise localization sequence is exact, since injectives are flabby. Open restriction preserves K-injectives because its left adjoint $j_!$ is exact; direct image preserves them because inverse image is exact. Thus its third term computes $Rj_*$, and the first is computed by Proposition 5.5. This proves the triangle. The same argument gives two-open Mayer–Vietoris and successive closed-support identities. Alternatively $\Gamma_Z$ is right adjoint to the exact functor $k_Z\otimes_k(-)$, so it preserves K-injectives; the underived identity $\Gamma_Z\Gamma_W=\Gamma_{Z\cap W}$ then derives with one resolution.

**Finite-window lemma.** Let $T$ be any of these left exact functors with cohomological dimension at most $d$. For every $A\in D(k_X)$ and integer $q$, natural truncation maps give

\[
H^q(RT A)\simeq
H^q\!\left(RT\bigl(\tau^{\geq q-d}\tau^{\leq q}A\bigr)\right).
\tag{UR21}
\]

**Proof.** The amplitude assertion [proved in URA1](#finite-cohomological-amplitude) is
$RT(D^{\geq a})\subset D^{\geq a}$ and
$RT(D^{\leq b})\subset D^{\leq b+d}$.
Apply it first to the triangle cutting off $\tau^{\geq q+1}A$; this tail contributes neither in degree $q-1$ nor in degree $q$, so $\tau^{\leq q}A\to A$ gives the first isomorphism in degree $q$. Next remove the part in degrees at most $q-d-1$. Its image lies in degrees at most $q-1$, so it contributes neither in degree $q$ nor in degree $q+1$. This gives the second isomorphism, now from $\tau^{\leq q}A$ to the displayed finite window. The comparisons are a natural zigzag, not a claim of a canonical map $A$ into that window. $\square$

The lemma controls one output degree of one operation. It says nothing about the microsupport of a truncation. A support-test vanishing in every degree cannot be transferred to a truncation by this formula alone.

## SH02-UR-CONTINUITY — Compact neighborhoods and increasing opens

**Compact-neighborhood continuity.** For a compact subset $K\subset X$ and arbitrary $A\in D(k_X)$,

\[
\underset{V\supset K}{\operatorname{colim}}H^q(V;A)
\xrightarrow{\sim}H^q(K;A|_K).
\tag{UR22}
\]

Here $V$ runs through open neighborhoods of $K$. Both $V$ and $K$ have cohomological dimension at most $n$, by the preceding section. Formula (UR21) therefore reduces both sides, for fixed $q$, to the same bounded truncation window. Restriction is exact and commutes with these truncations. The bounded comparison `SH02-NCD-COMPACT-CONTINUITY`, based on [Stacks, Tag 09V3](https://stacks.math.columbia.edu/tag/09V3), applies to that window. Naturality of its comparison and of (UR21) proves (UR22). The section-germ and dimension-shifting inputs of the bounded comparison are proved in *Supporting verifications for open prerequisites*, E4 and GP2–GP6; its bounded-below hypercohomology construction supplies the finite convergence comparison for bounded complexes. This explains the uniform dimension hypothesis; separate finite bounds growing with $V$ would not justify a fixed window.

**Increasing-open continuity.** On any topological space, if $V=\bigcup_m V_m$ for an increasing sequence of opens and $A\in D(k_X)$, then

\[
0\longrightarrow\lim_m^1 H^{q-1}(V_m;A)
\longrightarrow H^q(V;A)
\longrightarrow\lim_m H^q(V_m;A)\longrightarrow0.
\tag{UR23}
\]

Use a K-injective representative $I$ with injective terms and put $C_m=\Gamma(V_m;I)$. Restriction preserves K-injectives, so these compute derived sections. Termwise flabbiness makes all maps $C_{m+1}^j\to C_m^j$ surjective. The sheaf axiom identifies $\Gamma(V;I)$ with $\lim_m C_m$, term by term. Consequently there is a short exact sequence of complexes

\[
0\to\Gamma(V;I)\to\prod_m C_m
\xrightarrow{1-\mathrm{shift}}\prod_m C_m\to0.
\tag{UR24}
\]

Surjectivity of the last map follows recursively: given $(y_m)$ and $x_m$, choose $x_{m+1}$ restricting to $x_m-y_m$. Products of modules are exact, so cohomology of these products is the product of their cohomologies. The long exact sequence of (UR24) gives (UR23), where $\lim^1$ is the cokernel of $1-\mathrm{shift}$ on the product of cohomology modules. No lower bound has been used.

## SH02-UR-INTERVAL — Constancy without induction from a lowest degree

**Surjective extension lemma.** Let $M_t$ be an inverse system of modules indexed by $\mathbb R$. Suppose, for every $s$, both natural maps

\[
\underset{t>s}{\operatorname{colim}}M_t\longrightarrow M_s,
\qquad M_s\longrightarrow\lim_{u<s}M_u
\tag{UR25}
\]

are surjective. Then all transition maps $M_b\to M_a$, $a<b$, are surjective.

**Proof.** Fix $x_a\in M_a$. Consider coherent extensions $(x_t)_{t\in I}$, where $I$ is an initial segment of $[a,b]$ containing $a$, with the prescribed value at $a$. Order them by extension of the domain and of the family. A chain has its union as an upper bound, so a maximal family exists. Write $c=\sup I$. If $c\notin I$, then $c>a$ and the family, together with restrictions of $x_a$ at times below $a$, defines an element of $\lim_{u<c}M_u$. The second surjection in (UR25) extends it to $c$, contradicting maximality. Hence $c\in I$.

If $c<b$, the first surjection in (UR25) extends $x_c$ to some $d>c$. Restrict to $d\leq b$ if necessary. Using the restrictions of that extension at every intermediate time extends the coherent family through $d$, again a contradiction. Thus $c=b\in I$, and $x_b$ lifts $x_a$. $\square$

**Complex criterion.** Let $C_t$ be complexes of modules with degreewise surjective transitions. Suppose $C_s=\lim_{u<s}C_u$ termwise, with a countable cofinal sequence allowed in this limit, and suppose

\[
\underset{t>s}{\operatorname{colim}}H^q(C_t)
\xrightarrow{\sim}H^q(C_s)
\tag{UR26}
\]

for every $s,q$. Then every transition $C_b\to C_a$ is a quasi-isomorphism.

**Proof.** The complex calculation (UR24) shows, without any induction, that $H^q(C_s)\to\lim_{u<s}H^q(C_u)$ is surjective. Apply the surjective extension lemma in each degree, using (UR26) for its first map. All cohomological transitions are therefore surjective, simultaneously in every degree. Their countable $\lim^1$ groups vanish by the same recursive calculation as in (UR24). Hence the comparison to the left limit is now an isomorphism in every degree. Together with (UR26) this satisfies the two-sided interval criterion `SH02-NCD-INTERVAL-SYSTEM` in [the deformation lesson](noncharacteristic-deformation.md), which proves every cohomological transition is an isomorphism. That elementary criterion uses a supremum argument, not a cohomological lower bound. This proves the assertion. $\square$

The order matters: first obtain surjectivity in all degrees, then eliminate all $\lim^1$ terms, then obtain injectivity. Starting an induction at degree $-\infty$ would not be a proof.

## SH02-UR-DEFORMATION — An unbounded deformation theorem on manifolds

Let $X$ be a finite-dimensional Hausdorff manifold without boundary, countable at infinity, let $F\in D(k_X)$, and put
$S=\overline{\bigcup_q\{x:H^q(F)_x\ne0\}}$.
Let $U_t$ be open subsets indexed by $\mathbb R$ such that:

1. $U_t=\bigcup_{s<t}U_s$ for every $t$.
2. $\overline{U_t\setminus U_s}\cap S$ is compact whenever $s<t$.
3. With $B_s=\bigcap_{v>s}\overline{U_v\setminus U_s}$, for every $s\leq t$ and $x\in B_s\setminus U_t$ one has $(R\Gamma_{X\setminus U_t}F)_x=0$.

Then restriction gives isomorphisms in $D(k)$

\[
R\Gamma\!\left(\bigcup_t U_t;F\right)
\xrightarrow{\sim}R\Gamma(U_s;F)
\tag{UR27}
\]

for every $s$. No cohomological lower bound on $F$ is required.

**Proof.** First restrict to the closed support $S$. Exact closed direct image identifies cohomology and local support tests, since $F$ vanishes on the complement. The front computed inside $S$ lies in $S\cap B_s$, and
$\overline{(U_t\cap S)\setminus(U_s\cap S)}^{\,S}
\subset S\cap\overline{U_t\setminus U_s}^{\,X}$.
Thus the hypotheses persist, all closed increments are compact, and the uniform bounds and (UR22) remain valid by the closed-subset form proved above. Work on that closed subset from now on.

Fix $s$ and set $Q_s=R\Gamma_{X\setminus U_s}F$. We claim $\operatorname{colim}_{t>s}H^q(U_t;Q_s)=0$ for all $q$. Let $\alpha$ be represented at time $t>s$. Localizing $Q_s$ and using successive closed supports gives a triangle

\[
R\Gamma_{X\setminus U_t}F\longrightarrow Q_s
\longrightarrow Rj_{t*}(Q_s|_{U_t})\xrightarrow{+1}.
\tag{UR28}
\]

The first two terms vanish on $B_s$ by hypothesis, including its endpoint case $s=t$ for the second term. At points already in $U_t$ the first vanishes automatically. Hence the third vanishes on $B_s$. This front is compact, and (UR22) applied to the third term implies that $\alpha$ vanishes on $V\cap U_t$ for some open neighborhood $V$ of $B_s$.

There exists $u$ with $s<u\leq t$ and $\overline{U_u\setminus U_s}\subset V$. To see this, the closed increments for $s<v\leq t$ are nested compact subsets of $\overline{U_t\setminus U_s}$. If none were contained in $V$, their complements of $V$ would be nonempty nested compact sets with nonempty intersection, contrary to the definition of $B_s$. This argument also treats an empty front.

Now $U_s$ and $U_u\cap V$ cover $U_u$. The complex $Q_s$ vanishes on the first and on the intersection. The unbounded two-open Mayer–Vietoris triangle therefore identifies $R\Gamma(U_u;Q_s)$ with $R\Gamma(U_u\cap V;Q_s)$. The restriction of $\alpha$ is zero there, proving the claim.

Apply sections on $U_t$ to the localization triangle $Q_s\to F\to Rj_{s*}(F|_{U_s})$ and take the filtered colimit for $t>s$. The last term has the constant cohomology $H^q(U_s;F)$, and the first term has zero colimit in every degree by the claim. Exactness of filtered colimits gives (UR26) for $C_t=\Gamma(U_t;I)$, where $I$ is a K-injective representative with injective terms. These complexes have surjective termwise restrictions by flabbiness. The equality $U_s=\bigcup_{u<s}U_u$, computed on a sequence increasing to $s$, gives their termwise left-limit equality by the sheaf axiom. The complex criterion proves that all restrictions between times are quasi-isomorphisms.

Finally $\bigcup_tU_t=\bigcup_{m\geq0}U_m$. Apply (UR23). All cohomological transitions are isomorphisms, so the $\lim^1$ term vanishes and the inverse limit is the value at any fixed time. Its comparison map is restriction. This proves (UR27) in every degree. $\square$

This result is sufficient for deformation on the finite-dimensional spaces of local manifold arguments. A more general unbounded theorem on Hausdorff spaces is proved by Marco Robalo and Pierre Schapira, [*A lemma for microlocal sheaf theory in the infinity-categorical setting*](https://doi.org/10.4171/PRIMS/54-2-5), Theorem 2.3; despite the title, that theorem concerns the classical unbounded derived category. Their complex criterion motivates the separation of surjectivity from injectivity above. We have supplied the extension argument and the finite-dimensional continuity proof explicitly, and do not import an unspecified extension of every microsupport theorem from that paper.

## SH02-UR-MICROSUPPORT — Unbounded local tests and the characteristic estimates

For $F\in D(k_X)$ on a $C^1$ manifold, define $\operatorname{SS}_{\mathrm{u}}(F)$ by the usual support test: $(x,\xi)$ is outside it if there is an open neighborhood $W$ of $(x,\xi)$ in $T^*X$ such that

\[
\left(R\Gamma_{\{\varphi\geq\varphi(y)\}}F\right)_y=0
\tag{UR29}
\]

for every point $y$ and every real $C^1$ function $\varphi$ defined near $y$ with $(y,d\varphi(y))\in W$. All local functors are the unbounded classical ones of (UR20); the equality is vanishing in every degree. On bounded complexes this agrees with `SH02-MST-TEST` in [the local-test lesson](microsupport-tests.md). It uses the same $C^1$ tests. An equivalence with other differentiability classes on unbounded complexes is not needed or asserted here.

This definition gives a closed positive-conic subset, is invariant under shifts, and satisfies the triangle inequality

\[
\operatorname{SS}_{\mathrm{u}}(F_2)
\subset\operatorname{SS}_{\mathrm{u}}(F_1)
\cup\operatorname{SS}_{\mathrm{u}}(F_3)
\tag{UR30}
\]

for a distinguished triangle $F_1\to F_2\to F_3\xrightarrow{+1}$. Indeed the complement is a union of open testing neighborhoods; multiplying $\varphi$ by a positive constant rescales its covector without changing its support set; and each test functor is triangulated. Intersect two testing neighborhoods to prove (UR30). The same argument gives the other two triangle inequalities. Open restriction is compatible with all tests, so the definition is local in $X$.

Its intersection with the zero section is exactly the closed support $S$ used in the deformation theorem. Outside $S$, the complex vanishes on a neighborhood and so do all its tests. Conversely, if $(x,0)$ has a testing neighborhood, that neighborhood contains $(y,0)$ for every $y$ sufficiently near $x$. Testing the constant function makes (UR29) equal to $F_y$. Thus all cohomology stalks vanish on one common neighborhood, placing $x$ outside $S$. These arguments use no boundedness or constructibility.

**The characteristic estimate.** The internal-Hom statement, on a smooth manifold $X$, for the source's commutative coefficient ring of finite global dimension and $F,G\in D^+(k_X)$, is

\[
\operatorname{SS}_{\mathrm{u}}(R\mathcal Hom(G,F))
\subset\operatorname{SS}_{\mathrm{u}}(F)
\widehat+\operatorname{SS}_{\mathrm{u}}(G)^a.
\tag{UR31}
\]

The tensor counterpart has $F\otimes^LG$ and omits the antipode. The operation $\widehat+$ is the asymptotic sum defined in [characteristic estimates](characteristic-estimates.md); it includes covectors obtained by cancellation of unbounded covectors at approaching base points.

The constructions above make every object and local test in (UR31) meaningful. The geometric proof is supplied in [the unbounded characteristic supplement](unbounded-characteristic-estimates.md), at the stronger range $F,G\in D(k_X)$. Its three parts are:

1. [SH02-UCE-EXTERNAL-HOM](unbounded-characteristic-estimates.md#SH02-UCE-EXTERNAL-HOM) proves the external estimate for $R\mathcal Hom(q_2^{-1}G,q_1^!F)$ with its possibly unbounded output. It uses open rectangles and an explicit opposite-cone lens, retaining both restriction maps.
2. [SH02-UCE-RESTRICTION](unbounded-characteristic-estimates.md#SH02-UCE-RESTRICTION) proves the closed-embedding estimate $\operatorname{SS}_{\mathrm{u}}(\delta^!A)\subset\delta^\#\operatorname{SS}_{\mathrm{u}}(A)$ using raw specialization and radial cutoff. The preceding window and test lemmas keep the geometric neighborhoods uniform in all degrees.
3. [SH02-UCE-DIAGONAL-HOM](unbounded-characteristic-estimates.md#SH02-UCE-DIAGONAL-HOM) identifies $\delta^!R\mathcal Hom(q_2^{-1}G,q_1^!F)\simeq R\mathcal Hom(G,F)$ by its adjunction maps. The external tensor estimate and ordinary restriction give the tensor assertion; both deductions are completed in [SH02-UCE-SUM](unbounded-characteristic-estimates.md#SH02-UCE-SUM).

The unbounded deformation theorem above is one prerequisite of that proof. Formula (UR21) alone would not suffice: its window varies with the output degree, and cohomological truncation need not preserve microsupport. The supplement first proves uniform amplitude bounds for the required families of functors, and then applies the geometric tests directly to the original complex. This supplies the full estimates discussed in `SH02-CHE-RANGE`, relative to the named prerequisites. The bounded classical comparison in [the six-operations bridge](six-operations-import-bridge.md) retains its stated bounded scope. Neither this extension nor the supplement assumes hypercompleteness or settles the independent Fourier normalization.

## SH02-UR-PROBLEMS — Three checks that separate the issues

**Problem 1.** On a point over a field, put $G=\bigoplus_{m\geq0}k[-m]$ and $F=k$. Determine the range of $R\operatorname{Hom}(G,F)$ and check (UR18).

**Solution.** $G$ has one copy of $k$ in every nonnegative degree. Its Hom into $k$ has one copy in every nonpositive degree, with zero differential; equivalently it is $\prod_{m\geq0}k[m]$. It is unbounded below. For the identity map, proper and ordinary image and exceptional inverse image are identities, both $\pi$ maps are identities, and both sides of (UR18) are the identity on this Hom. The diagram is true, but the bounded-below construction alone could not type all its objects.

**Problem 2.** Let $f:D\to\{*\}$ for an arbitrary discrete set $D$. Give the unbounded adjunction explicitly, including the trace.

**Solution.** The integral cohomological dimension is zero. Proper direct image is $\bigoplus_{d\in D}G_d$, ordinary image is $\prod_{d\in D}G_d$, and $f^!F$ has stalk $F$ at every point. The adjunction is $\operatorname{Hom}(\bigoplus_dG_d,F)=\prod_d\operatorname{Hom}(G_d,F)$, also for derived morphisms. The trace $\bigoplus_d F\to F$ is the finite-sum map. Support forgetting is the canonical inclusion of the direct sum in the product. In (UR19), two finitely supported families evaluate coordinatewise and their values are added. Either route has this same finite sum. No map adding infinitely many coordinates is introduced.

**Problem 3.** Explain why right-continuity of cohomology and degreewise surjectivity of the complex restrictions do not justify the sentence “start with the lowest nonzero degree” for an unbounded deformation problem. Give the replacement argument.

**Solution.** There may be a nonzero cohomology group in every negative degree, so a lowest degree need not exist. Degreewise surjectivity yields the Milnor sequence and therefore surjectivity of the cohomological comparison to the left limit. The extension lemma then gives surjectivity of all cohomological restrictions in every degree at once. These restrictions kill the $\lim^1$ obstruction, giving bijective left-continuity. Combining that with right-continuity proves constancy. None of these steps starts an induction over all integers.

## SH02-UR-HOM-PULLBACK — The full exceptional internal-Hom comparison

Retain the locally compact Hausdorff spaces, map $f:Y\to X$, and uniform integral proper-support dimension bound $r$ from this lesson. Let $k$ be the course coefficient ring. For arbitrary $A,B\in D(k_X)$, there is a natural isomorphism

\[
f^!R\mathcal Hom(A,B)
\xrightarrow{\sim}R\mathcal Hom(f^{-1}A,f^!B).
\tag{UR32}
\]

**Proof.** For every $C\in D(k_Y)$, the unbounded exceptional adjunction and projection isomorphism proved above give the following natural chain:

\[
\begin{aligned}
\operatorname{Hom}(C,f^!R\mathcal Hom(A,B))
&\simeq\operatorname{Hom}(Rf_!C,R\mathcal Hom(A,B))\\
&\simeq\operatorname{Hom}(Rf_!C\otimes^L A,B)\\
&\simeq\operatorname{Hom}(Rf_!(C\otimes^Lf^{-1}A),B)\\
&\simeq\operatorname{Hom}(C\otimes^Lf^{-1}A,f^!B)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(f^{-1}A,f^!B)).
\end{aligned}
\]

Yoneda proves UR32. No intermediate tensor is required to be bounded below.
To identify the actual arrow, put $H=R\mathcal Hom(A,B)$. The inverse projection map followed by the adjunction trace defines, by transposition,
$f^!H\otimes^Lf^{-1}A\to f^!(H\otimes^LA)$. Apply $f^!$ to evaluation $H\otimes^LA\to B$ and curry. Tracking a map from $C$ through the displayed chain gives exactly this arrow. Thus UR32 uses the same tensor comparison and trace as `SH02-EX-HOM`; it is not an unspecified isomorphism between the endpoints. $\square$

In particular, take $A\in D^{\le a}(k_X)$ and $B\in D^{\ge b}(k_X)$, with no lower bound on $A$. Represent $A$ by a complex zero above degree $a$, and $B$ by a bounded-below K-injective complex zero below degree $b$. The internal Hom complex has no term below $b-a$, so its derived object lies in $D^{\ge b-a}$. The lower-amplitude bound for $f^!$ places the left side of UR32 in $D^{\ge b-a-r}$. On the right, exact inverse image preserves the upper bound $a$, and $f^!B\in D^{\ge b-r}$, giving the same Hom lower bound. Both endpoints therefore belong to $D^+$, and UR32 restricts to the full $D^-\times D^+$ assertion. On the older bounded-first-input range, the adjunctions, projection and trace restrict to those of the exceptional-operations lesson, so the comparison is exactly its previously defined map.
