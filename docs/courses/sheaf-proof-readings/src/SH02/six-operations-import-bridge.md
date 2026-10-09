# SH02-SIX-BRIDGE — Proper supports and the bounded classical comparison

This lesson compares actual classical proper supports with the modern compact-support construction, retaining the coefficient and category ranges below.

The purpose of this lesson is to identify a modern six-operations theorem with the classical operations used in this course. It also supplies the compact-support argument needed for that identification. All spaces are locally compact Hausdorff, all maps are continuous, and $k$ is an arbitrary commutative ring unless a tensor statement explicitly imposes finite global dimension. There are no rank, constructibility, countability, or dimension assumptions on the spaces. We use cohomological grading.

The principal reference is Marco Volpe, [*The six operations in topology*](https://doi.org/10.1112/topo.70050), Journal of Topology 18 (2025), e70050. We use the [published version](https://epub.uni-regensburg.de/78207/), whose relevant results have been compared with [arXiv v3](https://arxiv.org/html/2110.10212v3). The theorem is about ordinary sheaves with values in a stable infinity-category. Identifying that category with every unbounded classical derived category would be an additional, generally invalid step.

## SH02-SIX-COMPACT-GLUE — Lifting across a soft kernel

For a sheaf $A$ on a compact Hausdorff space $P$, call $A$ **soft** if every section on a closed subset of $P$ extends to $P$. Sections on a subset always mean sections of the inverse-image sheaf.

**Lemma.** If $0\to A\to B\to C\to0$ is an exact sequence of sheaves of $k$-modules on $P$ and $A$ is soft, then $\Gamma(P;B)\to\Gamma(P;C)$ is surjective.

**Proof.** Let $c$ be a section of $C$. Local surjectivity provides an open cover on which $c$ has lifts. Compactness and normality give a finite closed cover $K_1,\ldots,K_m$ whose interiors cover $P$, with each $K_i$ contained in an open set carrying a lift. We construct a lift near $K_1\cup\cdots\cup K_i$ by induction.

Suppose that $b$ is a lift near $L=K_1\cup\cdots\cup K_{i-1}$ and $b_i$ a lift near $K_i$. Their difference is a section of $A$ wherever both are defined. Its restriction to the closed set $L\cap K_i$ extends to a section $a$ on $P$. Replace $b_i$ by $b_i+a$, choosing the sign so that it agrees with $b$ on $L\cap K_i$. The two sections then agree on an open neighborhood $W$ of that intersection.

Here the neighborhoods must be shrunk before gluing. The closed sets $L\setminus W$ and $K_i\setminus W$ are disjoint. Choose disjoint open neighborhoods of them by normality. Their unions with $W$, intersected with the original domains of the two lifts, give neighborhoods of $L$ and $K_i$ whose intersection lies in $W$. On these smaller domains the lifts glue. The induction ends with a section on a neighborhood of all of $P$, hence on $P$. $\square$

The elementary topological ingredients used here can be obtained without a metric. To shrink a finite open cover of a compact Hausdorff space, choose for each point an open neighborhood whose closure lies in one member of the cover, take finitely many such neighborhoods, and group their closures according to that member. Sections also glue over a finite closed cover: the assertion reduces on each stalk to the ordinary sheaf gluing assertion, since a closed member that does not contain the point is absent on some neighborhood.

## SH02-SIX-SOFT-ACYCLIC — Compact acyclicity and extension by zero

On a locally compact Hausdorff space $X$, call $E$ **c-soft** if every section on a compact subset extends to $X$.

We use the degree-zero compact-neighborhood continuity statement of [Stacks, Tag 09V3](https://stacks.math.columbia.edu/tag/09V3): a section on a compact subset of a Hausdorff space is represented on an open neighborhood of that subset. Consequently every flabby sheaf is c-soft. In particular, injective $k$-module sheaves are c-soft by [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX). Restricting a c-soft sheaf to a closed subset preserves c-softness, because its compact subsets are still compact in $X$.

**Compact acyclicity.** A soft sheaf on a compact Hausdorff space has no positive sheaf cohomology.

To prove this, embed a soft sheaf $A$ in an injective sheaf $I$ and write $C=I/A$. For a closed subset $K$, the restriction $A|_K$ is soft. Apply the preceding lifting lemma on $K$ to lift any section of $C|_K$ to $I|_K$. Since $I$ is soft, that lift extends to $I(P)$, and its image extends the original section of $C$. Thus $C$ is soft. Repeating injective embeddings gives an injective resolution all of whose successive cokernels are soft. The lifting lemma makes its complex of global sections exact in positive degrees. This proves the assertion using the definition of derived cohomology.

**Open extension.** If $j:X\hookrightarrow Z$ is an open inclusion, then $j_!$ carries c-soft sheaves to c-soft sheaves.

Let $s$ be a section of $j_!E$ on a compact set $A\subset Z$. Its support $K$ is a closed subset of $A$ contained in $X$, hence is compact. If $K$ is empty, extend by zero. Otherwise choose compact neighborhoods in $X$ with

\[
K\subset\operatorname{Int} B\subset B\subset\operatorname{Int} C\subset C\subset X.
\]

On the compact subset

\[
D=(A\cap C)\cup(C\setminus\operatorname{Int} B)
\]

of $X$, prescribe $s$ on the first member and zero on the second. They agree on the intersection, which is disjoint from $K$, so finite closed gluing gives a section of $E|_D$. Extend it to $e\in\Gamma(X;E)$ by c-softness. The sections $e$ on $\operatorname{Int} C$ and zero on $X\setminus B$ agree on their overlap. They therefore give a section supported in $B$, which extends by zero to $Z$ and restricts to $s$ on $A$. This proves the assertion.

Coproducts of c-soft sheaves are c-soft. A section of a sheaf coproduct on a compact subset is locally represented in finitely many summands. A finite open cover of that compact subset therefore involves only finitely many indices altogether. Extend the corresponding component sections and add them. This argument concerns a compact restriction; it does not assert that unrestricted sections commute with sheaf coproducts.

## SH02-SIX-COMPACTIFICATION — The actual classical proper direct image

For $f:X\to Y$, define $f_!E$ as the subsheaf of $f_*E$ consisting, on an open $V\subset Y$, of sections whose support is proper over $V$. Support is closed in $f^{-1}V$. This is a left exact functor and therefore has a right derived functor $Rf_!$ on $D^+(k_X)$.

There is a compactification adequate for every such map. Let $X^+$ be the one-point compactification; if $X$ is compact, take a disjoint isolated point. In $X^+\times Y$, take the closure $\overline X$ of the graph of $f$. The graph is closed in $X\times Y$, which is open in $X^+\times Y$. It is therefore open in $\overline X$. This gives

\[
X\xrightarrow{j}\overline X\xrightarrow{p}Y,
\qquad f=pj,
\]

with $j$ open and $p$ proper. Indeed, $\overline X$ is closed in $X^+\times Y$, and the projection of a product with a compact space is proper.

There is a canonical equality of left exact functors

\[
f_!=p_*j_!.
\tag{SB.1}
\]

A section of $j_!E$ over $p^{-1}V$ has closed support there, contained in $X$; this support is proper over $V$. Conversely, a properly supported section on $f^{-1}V$ extends by zero across the boundary of $X$ in $p^{-1}V$. To check this last point near a boundary point over $y$, choose a compact neighborhood $L\subset V$ of $y$. The section's support over $L$ is compact in $X$; its graph is therefore closed in $X^+\times L$ and misses the boundary. The zero extension is consequently locally zero there. These constructions are inverse and commute with restriction in $V$.

The derived equality requires a proof: deriving a composite does not automatically give the composite of derived functors.

**Theorem.** On $D^+(k_X)$, the canonical comparison is an isomorphism

\[
Rf_!\simeq Rp_*j_!.
\tag{SB.2}
\]

**Proof.** Let $I$ be injective on $X$. The preceding lemma makes $j_!I$ c-soft on $\overline X$. Each fibre of $p$ is compact Hausdorff, and the restriction of $j_!I$ to that fibre is soft. Its positive cohomology vanishes. The proper-fibre theorem [Stacks, Tag 09V5](https://stacks.math.columbia.edu/tag/09V5), with the constant-ring specialization explained in [our prerequisite contracts](open-prerequisites.md), now gives $R^qp_*(j_!I)=0$ for $q>0$.

Take a bounded-below injective resolution of the input. Since $j_!$ is exact and sends each term to a $p_*$-acyclic sheaf, applying $p_*j_!$ computes both sides of (SB.2). The comparison is the identity on this resolution and extends (SB.1). $\square$

Taking $Y$ to be a point proves that a c-soft sheaf is acyclic for $\Gamma_c$. In fact, its open extension to $X^+$ is soft and hence acyclic for $\Gamma(X^+;-)$, and (SB.2) computes $R\Gamma_c(X;-)$ there. This argument also applies after restricting the source to any open subset.

## SH02-SIX-BOUNDED — The coefficient and category comparison

Write $\mathcal C=D_\infty(k)$ for the infinity-category of complexes of $k$-modules with quasi-isomorphisms inverted. It is stable, presentable, complete and cocomplete, and its derived tensor is closed symmetric monoidal. The coefficient identification with modules over the Eilenberg–Mac Lane ring spectrum is the symmetric monoidal equivalence in Jacob Lurie's [*Higher Algebra*, Theorem 7.1.2.13](https://www.math.ias.edu/~lurie/papers/HA.pdf), with its construction and proof on pages 1212–1213 of the September 18, 2017 version.

Let

\[
\mathcal S_k(X)=\operatorname{Shv}(X;D_\infty(k)).
\]

These are sheaves satisfying ordinary covering descent; hyperdescent is not imposed on the entire ambient category. Objectwise module structures identify this category with modules over the constant discrete ring object $k_X$ in spectral sheaves: the forgetful functor from module spectra creates limits, so the sheaf condition on a module object is the sheaf condition on its underlying spectrum, with its action maps retained.

[Bounded section recognition from injective mapping complexes](../../../SH-02/bounded-section-recognition.html) proves the exact bounded recognition used here. Its mathematical antecedent is [*Derived Algebraic Geometry VIII*, Proposition 2.1.8](https://www.math.ias.edu/~lurie/papers/DAG-VIII.pdf), in the November 5, 2011 version. Its hypotheses are a 1-localic infinity-topos and a discrete commutative ring sheaf. The topological open-set site has those properties. Its heart is the ordinary category of $k_X$-module sheaves, as identified in Remark 2.1.5. The statement is on page 32 and its proof, including the injective calculation, is on pages 33–35.

In our grading it gives a fully faithful comparison

\[
T_X:D^+_\infty(k_X)\longrightarrow\mathcal S_k(X),
\qquad T_XK(U)=R\Gamma(U;K).
\tag{SB.3}
\]

Its image is the union of the actual bounded parts of the sheaf t-structure. Concretely, there is an integer $a$ such that

\[
H^q(T_XK(U))=0\quad(q<a)
\tag{SB.4}
\]

for every open $U$. We call this a **uniform section bound**. This is stronger than merely imposing a lower bound on the cohomology sheaves in the non-hypercomplete ambient category. Lurie's homological notation writes the image as $\bigcup_n\mathcal S_k(X)_{\leq n}$; reversing the grading gives (SB.4). No assertion about the whole unbounded classical derived category is used.

Here is the concrete model fixing the maps. For a bounded-below injective resolution $I^\bullet$ of $K$, use $U\mapsto\Gamma(U;I^\bullet)$. Restriction of an injective to an open subset stays injective, since open extension by zero is exact. Injective Čech acyclicity and the bounded-below total complex show covering descent. Its stalk is $K_x$, since filtered colimits of $k$-modules are exact. Thus this model realizes (SB.3), including its action on morphisms.

It follows that the following comparisons are the usual classical ones:

\[
T_X f^{-1}K\simeq f^*T_YK,
\qquad
T_Y Rf_*L\simeq f_*T_XL,
\qquad
T_Z j_!L\simeq j_!T_XL.
\tag{SB.5}
\]

For the middle formula evaluate on an open $V$: both sides are $R\Gamma(f^{-1}V;L)$. For pullback, the sheafified inverse-image presheaf has the same stalk $K_{f(x)}$ as the exact classical pullback. For open extension, the presheaf is the given sheaf on opens contained in $X$ and zero on the other opens; its sheafification has the original stalk on $X$ and zero outside. Sheafification and these pullbacks preserve the actual t-structure bounds. Both sides of each comparison therefore satisfy a common bound (SB.4). A stalk equivalence between these bounded objects is an equivalence by (SB.3) and ordinary stalkwise detection of quasi-isomorphisms. This uses bounded recognition, not a stalkwise Whitehead assertion for all non-hypercomplete sheaves.

If $k$ has finite global dimension $d$, the same argument compares tensor products:

\[
T_X(K\otimes_k^L L)\simeq T_XK\otimes_k T_XL.
\tag{SB.6}
\]

The tensor is obtained by sheafifying the coefficientwise derived tensor. Inputs with bounds $a,b$ give bound $a+b-d$; the stalk comparison is the ordinary derived tensor comparison. The finite global dimension assumption is used precisely to retain a uniform lower bound for arbitrary $D^+$ inputs. It does not impose finite rank or perfection.

## SH02-SIX-IMPORT — Which six-operations formulas transfer

The [compact-support construction and its composition maps](../../../SH-02/modern-proper-support-construction.html) give the operations compared with Volpe below. Use those operations on $\mathcal S_k(X)$. Lemmas 6.2, 6.3 and 6.5 identify their proper direct image along a compactification with $p_*j_!$. Combining (SB.2) and (SB.5) gives the natural identification

\[
T_Y Rf_!K\simeq f_!T_XK.
\tag{SB.7}
\]

In particular the modern operation preserves the bounded classical subcategory on these inputs. This proves that the imported operation is the right derived functor of actual sections with proper support, with its map to $Rf_*$ fixed by inclusion of supports.

The relevant published results are Lemma 6.2 (page 53), Proposition 6.9 (pages 54–55), and Propositions 6.13–6.14 (page 56). They respectively transfer composition, change of base, and the tensor projection formula. The following records the maps, since an abstract isomorphism alone does not fix them.

### SH02-SIX-COMPOSE — Composition

For $X\xrightarrow{g}Y\xrightarrow{f}Z$, the comparison is

\[
Rf_!Rg_!K\xrightarrow{\sim}R(fg)_!K.
\tag{SB.8}
\]

On ordinary properly supported sections it is their identification under successive pushforward. Volpe's construction transports pushforward of compact-support cosheaves; successive inverse images of an open set agree with the inverse image for the composite. Consequently the composition map fixes this degree-zero identification, identities, and the associativity for three maps. Under (SB.7) these are exactly the classical comparisons. One can also check the derived normalization on an injective input $I$: the equivalence identifies $Rf_!(g_!I)$ with $(fg)_!I$ in degree zero, so $g_!I$ is $f_!$-acyclic. The usual composition comparison computed on injective resolutions is then the same map.

### SH02-SIX-BASECHANGE — The proper-support base-change map

In a cartesian square, write $f:X\to Y$, $g:Y'\to Y$, $f':X'\to Y'$ and $g':X'\to X$. The comparison is

\[
g^{-1}Rf_!K\xrightarrow{\sim}Rf'_!(g')^{-1}K.
\tag{SB.9}
\]

For a concrete construction, compactify $f=pj$ as above and pull that compactification back along $g$, obtaining $\overline g$, $p'$ and $j'$. Then (SB.9) is the composite

\[
g^{-1}Rp_*j_!K
\longrightarrow Rp'_*\overline g^{-1}j_!K
\xrightarrow{\sim}Rp'_*j'_!(g')^{-1}K.
\tag{SB.10}
\]

The first arrow is proper base change; the second is the open-extension comparison. It is an isomorphism on stalks, with the identity map on the surviving stalks. These are exactly the proper and open maps used in Volpe's Proposition 6.9. This also gives a wholly classical proof of invertibility from [Stacks, Tag 09V6](https://stacks.math.columbia.edu/tag/09V6) and (SB.2). Proper base change is the adjunction comparison, so identity squares and successive changes of base satisfy the usual pasting equalities. The open comparison does too, as is seen on its defining zero extensions. Using the same compactification and its repeated pullbacks proves these equalities for (SB.10).

Change of base to a point gives the actual fibre formula

\[
(Rf_!K)_y\simeq R\Gamma_c(f^{-1}(y);K|_{f^{-1}(y)}).
\tag{SB.11}
\]

Consequently a sheaf c-soft on every fibre is $f_!$-acyclic, and bounded-below complexes of such sheaves compute $Rf_!$. The statements remain true on an open restriction of the source. The degree-zero fibre formula also proves that $f_!$ commutes with coproducts: compactly supported sections involve only finitely many summands locally on a compact support, and a finite cover then involves only finitely many altogether.

### SH02-SIX-SOFT-CRITERION — The converse c-soft criterion

A sheaf $E$ is c-soft if and only if $H_c^q(U;E|_U)=0$ for every open $U\subset X$ and $q>0$.

The forward implication follows from open extension preserving c-softness and compact acyclicity. Conversely, let $K\subset X$ be compact and choose an open neighborhood $V$ of $K$. On $V$ the open-closed sequence is

\[
0\longrightarrow E_{V\setminus K}\longrightarrow E|_V
\longrightarrow i_*(E|_K)\longrightarrow0,
\]

where $i:K\hookrightarrow V$ is closed and the first term is open extension by zero within $V$. Composition for proper direct image identifies its compact-support cohomology with that on $V\setminus K$. Its first cohomology is zero by assumption. The long exact sequence therefore makes $\Gamma_c(V;E|_V)\to\Gamma(K;E|_K)$ surjective. Extend such a compactly supported lift by zero to $X$. Every section on $K$ extends, as required.

### SH02-SIX-PROJECTION — Arbitrary bounded-below tensor factors

Assume now that $k$ has finite global dimension. For $K\in D^+(k_X)$ and $L\in D^+(k_Y)$, the canonical map is an isomorphism

\[
Rf_!K\otimes_k^L L\xrightarrow{\sim}
Rf_!(K\otimes_k^L f^{-1}L).
\tag{SB.12}
\]

Equations (SB.6)–(SB.7) identify this with Volpe's Proposition 6.14, specialized using the coefficient tensor $D_\infty(k)\otimes D_\infty(k)\to D_\infty(k)$. The map multiplies a supported section by a pulled-back coefficient section. Its derived version is obtained from this multiplication using flat resolutions and the compactification model. Volpe's proof obtains precisely this projection map by external product and diagonal pullback. Associativity, the unit, and Koszul symmetry are the ones for derived tensor. This permits arbitrary sheaves and arbitrary $D^+$ factors under the stated ring hypothesis; the perfect-factor projection formula for $Rf_*$ alone would not establish it.

## SH02-SIX-EXCEPTIONAL-BOUND — The range of exceptional pullback

The modern right adjoint does not by itself supply a $D^+$-valued classical right adjoint for every map. Suppose that $f_!$ has cohomological dimension at most $r$ on all sheaves of $k$-modules on $X$. If $B\in D^{\geq a}(k_Y)$ and $U\subset X$ is open, adjunction identifies sections of the modern $f^!T_YB$ with

\[
R\operatorname{Hom}_{k_Y}(Rf_!k_U,B),
\tag{SB.13}
\]

where $k_U$ is extended by zero to $X$. The first input belongs to $D^{[0,r]}$, so this complex has no cohomology below $a-r$, by the t-structure orthogonality for derived Hom. The bound is uniform in $U$. Bounded recognition therefore puts $f^!T_YB$ in the image of $T_X$, and full faithfulness transfers its adjunction to the classical categories. The resulting $f^!$ has

\[
f^!D^{\geq a}\subset D^{\geq a-r}.
\]

The unique adjoint identification preserving its counit identifies it with the construction in [Exceptional inverse image](exceptional-operations.md). The finite cohomological-dimension hypothesis is retained; preservation of $D^b$ by an arbitrary $f^!$ is not inferred. Similarly, $Rf_!$ sends $D^{[a,b]}$ into $D^{[a,b+r]}$ when such a bound $r$ is available, by its bounded hypercohomology spectral sequence.

## SH02-SIX-EXERCISES — Two checks on the bridge

**Exercise 1.** Let $X$ be an infinite discrete set and $a:X\to\{*\}$. For a family of arbitrary $k$-modules $(M_x)$, compute $a_!M$ and $a_*M$. Explain why the map $a_!\to a_*$ cannot be replaced by an identity.

**Solution.** Every compact subset of a discrete space is finite. Thus $a_!M=\bigoplus_xM_x$, whereas $a_*M=\prod_xM_x$. The comparison is the inclusion of finitely supported families. If every $M_x=k\ne0$, the constant family with value $1$ is not in its image. This distinguishes proper support from unrestricted sections even in degree zero and with no cohomological complication.

**Exercise 2.** In a finite composition $X\xrightarrow{g}Y\xrightarrow{f}Z$, assume the cohomological dimensions of $g_!$ and $f_!$ are at most $s$ and $r$. Establish a bound for $(fg)_!$ and the corresponding lower bound for $(fg)^!$.

**Solution.** For an ordinary sheaf $E$, $Rg_!E$ has cohomology only in $[0,s]$. Applying $Rf_!$ to this finite cohomological filtration produces degrees only in $[0,r+s]$. Composition (SB.8) gives cohomological dimension at most $r+s$ for $(fg)_!$. Applying (SB.13) to the composite shows $(fg)^!D^{\geq a}\subset D^{\geq a-r-s}$. No tensor hypothesis is used in this calculation.

## SH02-SIX-SOURCE-CONTRACT — Import boundary and attribution

The original compact gluing, soft-sheaf, compactification, and coefficient-matching arguments above are course text. Volpe's proofs are imported by reference. The published paper's first-page license link and institutional record specify [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Its arXiv v3 has an arXiv distribution license; the institutional published version is the identified licensed version. No published PDF, source prose, diagrams, or extracted text is included in this lesson. Identified human adaptations retain their applicable terms, separately from the CC0 dedication of independently authored programme text.

The [bounded recognition proof](../../../SH-02/bounded-section-recognition.html) and [coefficient comparison](../../../SH-02/derived-module-coefficients.html) supply the respective actual topological all-module and algebraic statements. Their independently written CC0 proofs use the ambient categorical models specified in those lessons, with the cited Lurie results as mathematical antecedents. Their infinity-categorical prerequisites remain explicit: module spectra and their sheaf t-structure, bounded derived recognition, and the symmetric monoidal coefficient equivalence. Volpe's composition proof uses covariant Verdier duality (Theorem 5.10); its base-change proof reduces to proper base change for sheaves of spaces; its projection proof uses the external-product theorem. These imported proofs have been inspected at those steps, rather than treated as a heading-level replacement for a foundation course. The [compact-presentation and covariant-duality proof](../../../SH-02/modern-proper-support-construction.html#SH02-SXM-2) supplies the full compact-support composition construction. General nonabelian proper base change and the arbitrary-coefficient external-product theorem retain their separately specified categorical foundations; the full bounded classical maps and coefficient ranges above are preserved.

The formulas in this lesson supply precise candidates for `SH02-EX-IMP-SOFT`, `SH02-EX-IMP-FIBRES`, `SH02-EX-IMP-COMPOSE`, and `SH02-EX-IMP-BC`.
