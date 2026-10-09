# SH02-PREREQ-PROOFS — Supporting verifications for open prerequisites

These proofs discharge the specific elementary and coherence checks in the prerequisite contracts. They use the exact cited existence and localization theorems for derived categories and K-flat/K-injective resolutions. They do not reconstruct the complete upstream dependency graph. Existence of unbounded operations does not establish preservation of bounded complexes.

The sections below retain their proof letters for internal references. E1–E8 concern ordinary sheaf operations, proper maps, the hypercohomology edge, and one projection/base-change diagram. DF-A–DF-F concern chain-Hom signs, ordinary derived internal Hom, and pullback coherence. These results do not construct nonproper direct image with proper support, exceptional inverse image, microlocal Hom, or course-specific kernel and trace diagrams.

## SH02-PRP-E1. Finite sums and the limits contract

Let $(F_a)_{a\in A}$ be a finite family of module sheaves on a ringed space. The presheaf $U\mapsto\prod_{a\in A}F_a(U)$ is a sheaf: compatible local tuples have a unique glued tuple, obtained by gluing each coordinate. In modules a finite product is canonically the finite coproduct, including the empty family. Its coordinate injections and projections are morphisms of sheaves and satisfy the coproduct universal property, tested on every open set. Thus finite sums of module sheaves are already computed presheafwise. This supplies the finite-sum verification left unstated in [Tag 01AH](https://stacks.math.columbia.edu/tag/01AH).

For arbitrary limits, compatible tuples form a sheaf by the same coordinatewise gluing argument. Arbitrary coproducts, and hence general colimits, may require sheafification. Stalks commute with that sheafification and with colimits. A filtered diagram of short exact sequences therefore remains exact after sheaf colimit: at a point it is a filtered colimit of exact module sequences, and a finite relation witnessing a kernel or an image already holds at a later index. Stalk detection of exactness then applies. None of this asserts that sections on an arbitrary open commute with an infinite coproduct or a filtered colimit.

## SH02-PRP-E2. The constant-ring inverse-image bridge

Let $f:X\to Y$ be continuous and $k$ a commutative unital ring. The morphism of constant sheaves $f^{-1}k_Y\to k_X$ sends each locally represented constant to that same constant. At $x$ it is the identity $k\to k$, hence it is an isomorphism. The usual stalk map

\[
(f^{-1}F)_x\longrightarrow F_{f(x)}
\]

sends the germ represented by a section on a neighborhood of $f(x)$ to its germ at $f(x)$. Given two such representatives, restrict both to the intersection of their neighborhoods before adding them; the displayed map sends their sum to the sum of their germs. A scalar is handled on the same common neighborhood. Thus the stalk bijection in [Tag 008O](https://stacks.math.columbia.edu/tag/008O) is an isomorphism of $k$-modules, not just of sets. This checks the compatibility omitted there and expands the bridge already present in the public contract.

The ringed-space pullback has formula

\[
f^*F=k_X\otimes_{f^{-1}k_Y}f^{-1}F\simeq f^{-1}F.
\]

Exactness follows by evaluating stalks and using exactness at $f(x)$; it does not use flatness of $k$ over $\mathbb Z$. The morphism of constant-ring spaces is flat, because its local ring map is the identity of $k$. This also proves $Lf^*=f^{-1}$ on arbitrary complexes. Both horizontal maps in any square of constant-ring spaces meet the flatness hypotheses in [Tag 02N7](https://stacks.math.columbia.edu/tag/02N7). General morphisms of ringed spaces need not be flat, and their pullback need not be exact.

For an open inclusion $j:U\hookrightarrow X$, extension by zero is defined using the same $k$-linear sections and restrictions, with the usual support condition. Its stalk is $F_x$ if $x\in U$ and zero if $x\notin U$. Every short exact sequence therefore remains stalkwise exact. This discharges the coefficient specialization of [Tag 01AK](https://stacks.math.columbia.edu/tag/01AK).

## SH02-PRP-E3. Properness in the locally compact Hausdorff convention

For arbitrary topological spaces, [Section 5.17](https://stacks.math.columbia.edu/tag/005M) defines proper to mean separated and universally closed. [Tag 005R](https://stacks.math.columbia.edu/tag/005R) proves that universal closedness is equivalent to being closed with quasi-compact fibres. Separatedness remains an additional requirement.

Suppose now that $X,Y$ are locally compact Hausdorff and $f:X\to Y$ is continuous with compact inverse images of compact sets. Its fibres are compact. To prove that $f$ is closed, let $A\subset X$ be closed and choose $y\notin f(A)$. Choose a compact neighborhood $K$ of $y$ in $Y$. The set $A\cap f^{-1}K$ is compact, so its image $C$ is compact and closed in $Y$. The open neighborhood $\operatorname{Int}K\setminus C$ of $y$ is disjoint from $f(A)$. Thus $f(A)$ is closed. The [closed-map and quasi-compact-fibre criterion, Lemma 3](#general-proper-base-change), now gives universal closedness. Because $X$ is Hausdorff, its diagonal is closed in $X\times X$, and its intersection with $X\times_YX$ is closed there; hence $f$ is separated and proper in the Stacks sense.

Conversely, [Lemmas 2–3 below](#general-proper-base-change) prove that a universally closed map takes inverse images of quasi-compact subsets to quasi-compact subsets. For Hausdorff $X$, those inverse images are compact. This proves the precise convention bridge used by the public proper-base-change contract. Compact fibres alone would not have supplied closedness.

## SH02-PRP-E4. The compact-neighborhood dimension-shifting step

The supporting [Tag 09V3](https://stacks.math.columbia.edu/tag/09V3) concerns a quasi-compact subset $Z\subset X$ whose distinct points have disjoint ambient open neighborhoods. Its proof establishes the degree-zero neighborhood comparison by finite gluing and proves that the restriction of an injective module sheaf to $Z$ is acyclic for sections on $Z$. The [compact-germ and acyclicity proof below](#general-proper-base-change), GP2 and GP6, supplies both assertions with exactly these hypotheses, including a subset that is not closed in its ambient space. Here is the reduction from those assertions to all degrees.

For a module sheaf $F$ on $X$, set

\[
T^p(F)=\varinjlim_{U\supset Z}H^p(U,F|_U),\qquad
S^p(F)=H^p(Z,F|_Z),
\]

where $U$ runs through ambient open neighborhoods, with transition maps given by restriction. Inverse image to an open or to $Z$ is exact, and filtered colimits of modules are exact. Consequently both systems have the long exact sequences of cohomological delta functors. Restriction gives a morphism $T^p\to S^p$, and the finite-gluing argument identifies it in degree zero. If $I$ is injective, then $T^{p}(I)=0$ for $p>0$, since $I$ is acyclic on every open. The restricted-injective acyclicity proved in [GP6 below](#general-proper-base-change), also the conclusion used in Tag 09V3, gives $S^{p}(I)=0$ for $p>0$.

Embed $F$ into an injective $I$ and write $Q=I/F$. The two long exact sequences identify $T^1(F)$ and $S^1(F)$ with the respective cokernels of the degree-zero map for $I\to Q$. Their comparison is an isomorphism. For $p>1$, the connecting maps identify $T^p(F)$ with $T^{p-1}(Q)$ and $S^p(F)$ with $S^{p-1}(Q)$. Induction proves the comparison in every degree, and all maps used commute with restriction and morphisms of short exact sequences. This closes that dimension-shifting step. It says nothing about an arbitrary closed exhaustion or about exactness of an inverse limit of sheaves.

## SH02-PRP-E5. Proper base change with arbitrary constant-ring coefficients

The [general programme proof below](#general-proper-base-change) establishes proper base change directly for arbitrary constant-ring coefficients. The following comparison with the abelian-sheaf formulation records the coefficient and adjunction compatibility of the cited classical theorem.

Let a cartesian square of topological spaces have vertical maps $f:X\to Y$ and $f':X'\to Y'$, horizontal maps $g:Y'\to Y$ and $g':X'\to X$, and let $f$ be proper. Take $E\in D^+(k_X)$. By E2 this is a square of flat horizontal morphisms of constant-ring spaces, so the bounded-below comparison of [Tag 02N7](https://stacks.math.columbia.edu/tag/02N7) applies.

Write $U_X$ for forgetting the $k$-action on a sheaf on $X$. This functor is exact and detects exactness and quasi-isomorphisms, because the kernels, images, and cokernels have the same underlying groups. It commutes with inverse image and direct image. It need not take an injective $k_X$-module to an injective abelian sheaf. The appropriate replacement is acyclicity: an injective $k_X$-module is flabby by [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX), and the same surjective restriction maps make its underlying abelian sheaf flabby. By [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0), that sheaf is acyclic for direct image along every continuous map.

Choose a bounded-below injective resolution $E\to I$. The same underlying complex is an acyclic resolution for abelian-sheaf direct image. It follows that the natural comparison

\[
U_Y(Rf_*E)\simeq Rf_*(U_XE)
\]

is an isomorphism, and likewise for $f'$. These comparisons are natural: comparison maps of injective resolutions become comparison maps of acyclic resolutions and compute the derived map on the same underlying complex.

The underived unit and counit for $f^{-1}\dashv f_*$ are $k$-linear and become the ordinary abelian-sheaf unit and counit under $U$. On the resolutions just described, the derived unit and counit have the same property. Equivalently, the map for the square is the mate of

\[
(f')^{-1}g^{-1}Rf_*E
\simeq(g')^{-1}f^{-1}Rf_*E
\xrightarrow{(g')^{-1}\epsilon_f}(g')^{-1}E.
\]

Forgetting the action therefore takes this actual comparison, and not merely its source and target, to the comparison in [Tag 09V6](https://stacks.math.columbia.edu/tag/09V6). That theorem identifies the comparison on each stalk through the homeomorphism of fibres, using [Tag 09V5](https://stacks.math.columbia.edu/tag/09V5). It is an isomorphism for abelian sheaves; exact conservativity of $U$ proves the same for $k$-module sheaves.

The flabby input itself is checked as follows. [Tag 01EA](https://stacks.math.columbia.edu/tag/01EA) proves surjectivity of restrictions of an injective by applying $\operatorname{Hom}(-,I)$ to the inclusion of the two open extensions of the structure sheaf. [Tag 09SY](https://stacks.math.columbia.edu/tag/09SY) proves acyclicity of a flabby module on every open by extending a maximal locally lifted section; its quotient argument supplies the acyclic-resolution criterion. Finally [Tag 01E4](https://stacks.math.columbia.edu/tag/01E4) computes the higher direct-image sheaves from cohomology on inverse images of opens. Their positive degrees vanish for a flabby sheaf, which proves Tag 09T0. No restriction to a closed subset was asserted to preserve injectivity.

<a id="general-proper-base-change"></a>

## Proper base change for arbitrary topological spaces {#general-topological-proper-base-change}

Here **proper** means **separated and universally closed**. A continuous map \(f:X\to Y\) is separated when its diagonal \(X\to X\times_YX\) has closed image. It is universally closed when every base change is a closed map. No Hausdorff, local compactness, countability or dimension condition is imposed on \(X\) or \(Y\).

Let \(k\) be a commutative ring. All sheaves are sheaves of arbitrary \(k\)-modules. We prove that, for \(F\in D^+(k_X)\), the canonical map in every Cartesian square
\[
\begin{array}{ccc}
X'=X\times_YY'&\xrightarrow{g'}&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{g}&Y
\end{array}
\]
is an isomorphism:
\[
g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F.
\tag{GP1}
\]
The fibre formula and the construction of this particular map are included. The proof allows a fibre to be nonclosed in its ambient space.

### Compact subsets with ambient point separation

Say that a subset \(K\subseteq X\) has **ambient point separation** if any two distinct points of \(K\) have disjoint open neighborhoods in \(X\). This is stronger than merely saying that the subspace \(K\) is Hausdorff.

**Lemma 1.** Suppose \(K\subseteq X\) is compact and has ambient point separation.

1. The subspace \(K\) is compact Hausdorff.
2. Two disjoint compact subsets of \(K\) have disjoint open neighborhoods in \(X\).
3. Every finite open cover of \(K\) has a finite closed shrinking: if \(K\subseteq\bigcup_{i=1}^mU_i\), with \(U_i\) open in \(X\), there are compact subsets \(K_i\subseteq K\cap U_i\), closed in \(K\), whose union is \(K\).

**Proof.** Restricting the separating neighborhoods to \(K\) proves the first assertion.

For the second, let \(L,M\subseteq K\) be disjoint compact subsets. Empty sets cause no difficulty. For fixed \(x\in L\), choose disjoint ambient opens \(P_{xy}\ni x\), \(Q_{xy}\ni y\) for every \(y\in M\). Finitely many \(Q_{xy}\) cover \(M\). The intersection of their corresponding \(P_{xy}\), denoted \(P_x\), contains \(x\), and their union \(Q_x\) contains \(M\); these two opens are disjoint. Choose finitely many \(P_x\) covering \(L\). Their union \(P\) and the intersection of the corresponding \(Q_x\), denoted \(Q\), are disjoint ambient opens containing \(L\) and \(M\).

For the third, work inside the compact Hausdorff space \(K\). Given \(x\in K\cap U_i\), apply the second assertion inside \(K\) to \(\{x\}\) and \(K\setminus U_i\). Obtain disjoint relative opens \(O_x\ni x\) and \(B_x\supseteq K\setminus U_i\). Then
\[
\overline{O_x}^{\,K}\subseteq K\setminus B_x\subseteq K\cap U_i.
\]
Finitely many \(O_x\) cover \(K\). Assign each to a chosen index \(i\), and let \(K_i\) be the finite union of the corresponding closures. These closed compact sets have the required properties. \(\square\)

**Compact-germ lemma.** If \(K\subseteq X\) satisfies Lemma 1, then for every sheaf \(A\) the restriction map is an isomorphism
\[
\mathop{\mathrm{colim}}_{K\subseteq U,\ U\text{ open in }X}
\Gamma(U;A)\xrightarrow{\sim}\Gamma(K;A|_K).
\tag{GP2}
\]
Here \(A|_K\) is inverse image to the subspace; \(K\) need not be closed in \(X\).

**Proof.** A section \(s\) on \(K\) has local representatives \(s_i\in\Gamma(U_i;A)\): the inverse-image sheaf is obtained by sheafifying neighborhood representatives. After shrinking around each point and taking finitely many representatives, we may assume that \(K\cap U_i\) cover \(K\) and
\(s_i|_{K\cap U_i}=s|_{K\cap U_i}\).
Choose the closed shrinking \(K_i\subseteq K\cap U_i\) from Lemma 1.

For \(i<j\), let \(A_{ij}\subseteq U_i\cap U_j\) be the open equality locus of the germs of \(s_i\) and \(s_j\). It contains \(K_i\cap K_j\). The compact sets
\[
L_{ij}=K_i\setminus A_{ij},
\qquad K_j
\]
are disjoint. Notice that \(L_{ij}\) is closed in the compact space \(K_i\), although it need not be closed in \(X\). Lemma 1 supplies disjoint ambient opens \(P_{ij}\supseteq L_{ij}\) and \(Q_{ij}\supseteq K_j\). The opens
\[
N_i^{ij}=U_i\cap(A_{ij}\cup P_{ij}),
\qquad
N_j^{ij}=U_j\cap Q_{ij}
\]
contain \(K_i\) and \(K_j\), respectively, and satisfy
\[
N_i^{ij}\cap N_j^{ij}\subseteq A_{ij}.
\tag{GP3}
\]
For each index intersect its finitely many pairwise neighborhoods with \(U_i\), obtaining \(W_i\supseteq K_i\). The sections \(s_i|_{W_i}\) agree on all overlaps by (GP3), so glue on the open neighborhood \(\bigcup_iW_i\) of \(K\). Their restriction is \(s\), proving surjectivity.

For injectivity, take two representatives whose restrictions agree on \(K\). On their common ambient neighborhood their germ-equality locus is open and contains \(K\). They become equal on that smaller neighborhood, which is precisely equality in the colimit. When \(K=\varnothing\), the empty open neighborhood makes both sides zero. \(\square\)

The construction never takes the complement in \(X\) of a compact set as though that complement had to be open. All compactness and closed shrinking occur inside \(K\); all ambient shrinking uses proved point separation.

### What topological properness gives

**Lemma 2.** Let \(f:X\to Y\) be separated and universally closed.

1. Every fibre \(X_y=f^{-1}(y)\) is compact and has ambient point separation in \(X\), hence is compact Hausdorff.
2. Every open \(W\subseteq X\) containing \(X_y\) contains \(f^{-1}V\) for an open neighborhood \(V\) of \(y\).
3. Every base change of \(f\) is again separated and universally closed.

**Proof of ambient separation.** If \(x\ne z\) and \(f(x)=f(z)\), the pair \((x,z)\) lies outside the closed diagonal in \(X\times_YX\). Choose ambient opens \(U\ni x\), \(V\ni z\) with
\[
(U\times V)\cap(X\times_YX)
\]
disjoint from the diagonal. If \(w\in U\cap V\), the pair \((w,w)\) would belong to this intersection and the diagonal. Thus \(U\cap V=\varnothing\). This proves actual ambient separation, rather than separation only inside the fibre.

**Proof of compactness.** Put \(Z=X_y\). Base changing along the constant map \(T\to Y\) with value \(y\) shows that the projection \(Z\times T\to T\) is closed for every topological space \(T\).

Suppose an open cover \((U_i)_{i\in I}\) of \(Z\) had no finite subcover. Let \(\mathcal F\) be the set of finite subsets of \(I\), including the empty one. Give
\(T=\mathcal F\cup\{\infty\}\)
the topology in which every point of \(\mathcal F\) is isolated and the following sets are a neighborhood basis at \(\infty\):
\[
T_{F_0}=\{\infty\}\cup
\{F\in\mathcal F:F_0\subseteq F\}.
\tag{GP4}
\]
These are indeed a basis: two such tails intersect in the tail for the union of their finite indices. Every neighborhood of \(\infty\) contains finite-index points, so \(\mathcal F\) is not closed in \(T\).

Define
\[
C=\{(z,F)\in Z\times\mathcal F:
z\notin\textstyle\bigcup_{i\in F}U_i\}
\subseteq Z\times T,
\tag{GP5}
\]
with no points above \(\infty\). This set is closed. At a point \((z,F)\notin C\) with finite \(F\), the product
\((\bigcup_{i\in F}U_i)\times\{F\}\)
is a neighborhood missing \(C\). At \((z,\infty)\), choose \(i\) with \(z\in U_i\); then \(U_i\times T_{\{i\}}\) misses \(C\). Thus its complement is open. Since no finite subfamily covers \(Z\), every finite \(F\) occurs in its projection. That projection is exactly \(\mathcal F\), which is not closed. This contradicts universal closedness. Hence \(Z\) is compact. The empty fibre is compact from the outset.

**Proof of cofinality.** Universal closedness includes closedness of \(f\) itself. If \(X_y\subseteq W\) and \(W\) is open, the set \(X\setminus W\) is closed, and \(y\notin f(X\setminus W)\). Therefore
\[
V=Y\setminus f(X\setminus W)
\]
is an open neighborhood of \(y\) with \(f^{-1}V\subseteq W\). This proof does not require that \(\{y\}\) or \(X_y\) be closed. If the fibre is empty, take \(W=\varnothing\); then \(V=Y\setminus f(X)\) has empty inverse image.

**Proof of base-change stability.** Successive fibre products identify every base change of a base change with a base change of \(f\), so universal closedness is preserved. To check separatedness, recall the criterion just used: a map is separated exactly when distinct points of each fibre have disjoint ambient neighborhoods. The converse follows because these product neighborhoods cover the complement of its diagonal in the fibre product. Distinct points \((x,y'),(z,y')\) of a fibre of \(f'\) have \(x\ne z\) and \(f(x)=f(z)\). Pull back disjoint ambient neighborhoods of \(x,z\) along \(g'\). This proves the criterion for \(f'\). \(\square\)

### Closed maps with quasi-compact fibres and the usual properness convention

Here quasi-compact means that every open cover has a finite subcover; it carries no separation hypothesis.

**Lemma 3.** A continuous closed map with quasi-compact fibres is universally closed. Moreover, the inverse image of every quasi-compact subset of its target is quasi-compact.

**Proof.** Let \(f:X\to Y\) be such a map, let \(g:Y'\to Y\) be arbitrary, and let \(C\subseteq X'=X\times_YY'\) be closed. Fix \(y'\notin f'(C)\). For each \(x\in X_{g(y')}\), the pair \((x,y')\) belongs to the relative open complement of \(C\). Choose ambient product neighborhoods \(U_x\times V'_x\) whose intersections with \(X'\) miss \(C\). Quasi-compactness of the fibre supplies finitely many \(U_1,\ldots,U_m\) covering it. Set \(W=\bigcup_iU_i\) and
\[
N'=\left(\bigcap_iV'_i\right)
\cap g^{-1}\!\left(Y\setminus f(X\setminus W)\right).
\tag{GP12}
\]
Closedness makes this an open neighborhood of \(y'\). If \(z'\in N'\) and \((z,z')\in X'\), then \(z\in W\), so \(z\in U_i\) for some \(i\), while \(z'\in V'_i\). Hence \((z,z')\notin C\). Thus \(N'\) misses \(f'(C)\), proving that \(f'\) is closed. For an empty fibre use \(W=\varnothing\) and the empty intersection \(Y'\); the same formula applies.

Now let \(B\subseteq Y\) be quasi-compact. Base change to \(B\) gives a closed map \(f_B:f^{-1}B\to B\) with the same quasi-compact fibres. Given an open cover of \(f^{-1}B\), finitely many cover members cover each fibre; write their union as \(W_b\). Closedness gives an open neighborhood
\[
N_b=B\setminus f_B(f^{-1}B\setminus W_b)
\]
of \(b\), with \(f_B^{-1}N_b\subseteq W_b\). Finitely many \(N_b\) cover \(B\). The finite collections of original cover members chosen for these \(b\)'s consequently cover \(f^{-1}B\). The empty case uses the empty finite subcover. \(\square\)

Together with the finite-index test in Lemma 2, this proves that a continuous map is universally closed exactly when it is closed with quasi-compact fibres. The compactness part of that test did not use separatedness.

For maps between locally compact Hausdorff spaces, the present definition of properness agrees with compactness of inverse images of compact sets. One direction follows from Lemmas 2–3; the source being Hausdorff turns quasi-compact inverse images into compact Hausdorff subspaces. Conversely, suppose inverse images of compact sets are compact. The fibres are compact. To prove closedness, let \(C\subseteq X\) be closed and \(y\notin f(C)\). Choose a compact neighborhood \(L\) of \(y\) in \(Y\). The set \(C\cap f^{-1}L\) is compact, so its image is compact and closed in the Hausdorff target. The open neighborhood
\[
\operatorname{int}L\setminus f(C\cap f^{-1}L)
\]
of \(y\) misses \(f(C)\). Thus \(f\) is closed, and Lemma 3 proves universal closedness. Hausdorff separation in \(X\) gives separatedness of every continuous map from \(X\), by the relative-diagonal criterion. This proves both directions of the locally compact Hausdorff properness convention while retaining the earlier direct LCH fibre proof as a useful alternate route.

### Restricted injectives and compact-space acyclicity

An injective sheaf \(I\) on any space is flabby. Indeed, for an open inclusion \(j:U\hookrightarrow X\), extension by zero gives a monomorphism \(j_!k_U\to k_X\), as its stalks show. The identifications
\[
\operatorname{Hom}(j_!k_U,I)=\Gamma(U;I),
\qquad
\operatorname{Hom}(k_X,I)=\Gamma(X;I)
\]
and injectivity make restriction surjective. The same reasoning applies to any pair of nested opens.

If \(K\subseteq X\) is compact with ambient point separation, then \(I|_K\) is c-soft: every section on a compact subset \(L\subseteq K\) extends to all of \(K\). To see this, \(L\) is compact in \(X\) and inherits ambient separation. Its section is a section of \(I|_L\), by composition of inverse image. Apply (GP2) to extend it to an ambient neighborhood of \(L\), extend globally by flabbiness of \(I\), and restrict to \(K\). Neither \(L\) nor \(K\) was assumed closed in \(X\).

The required acyclicity now takes place entirely on a compact Hausdorff space. The existing programme proof is *Duality maps for constructible inverse and direct images*, compact lifting (C3) and the acyclicity argument after (C4). Its hypotheses are locally compact Hausdorff spaces and arbitrary \(k\)-modules. A compact Hausdorff fibre meets those hypotheses. Here is the needed compact argument.

On a compact Hausdorff space \(K\), a c-soft sheaf is one whose sections on every closed subset extend globally, since closed subsets are compact. In an exact sequence
\(0\to A\to B\to C\to0\)
with c-soft kernel \(A\), a section of \(C\) has local lifts. Choose finitely many compact closed sets subordinate to these local-lift neighborhoods. Glue the lifts successively: on the compact intersection of a new set with the union of the earlier sets, the difference of lifts is a section of \(A\), and c-softness extends it to a global section. Correct the new lift by that extension.

The finite closed gluing used here is valid for restricted sheaves. Near a point, discard the finitely many closed pieces that miss it. The remaining local representatives have equal germs there, so after a common shrinking they agree and represent the glued section. Thus the adjusted lifts give a global section of \(B\).

Consequently sections are exact on short exact sequences with c-soft kernel. If both \(A\) and \(B\) are c-soft, restrict to a closed subset \(L\subseteq K\), apply this lifting result there, and extend the resulting section of \(B|_L\) globally; its image proves that \(C\) is c-soft. Restrictions of a c-soft sheaf to such an \(L\) are c-soft by composition of restriction.

Embed a c-soft sheaf in an injective sheaf on \(K\). Injectives are c-soft by the preceding flabby and compact-germ argument, and the quotient is c-soft by the quotient result. Continue through an injective resolution. At every step the lifting result makes sections exact. This proves
\[
H^q(K;A)=0\qquad(q>0)
\quad\text{for every c-soft }A.
\tag{GP6}
\]
In particular, the restriction of an injective sheaf on \(X\) to any proper fibre is acyclic for ordinary sections.

We also use the bounded-below acyclic-complex comparison, proved in the same programme component at the derived fibre formula. For clarity, if a bounded-below complex has terms acyclic for a left exact functor \(T\), applying \(T\) termwise computes its right derived functor. A finite complex follows by its finite filtration by terms and the associated triangles. For a fixed cohomology degree \(n\), quotient a bounded-below complex by its brutal tail in degrees at least \(n+2\). Both termwise \(T\) and \(RT\) have zero cohomology below \(n+2\) on that tail: a bounded-below injective replacement can start in the same degree. Thus the quotient changes neither calculation in degree \(n\), and it is a finite complex of acyclic terms. This proves the comparison in every degree, naturally. No global upper cohomological-dimension bound is used.

### The fibre formula, with its restriction map

For any sheaf \(A\), the definition of the stalk, cofinality in Lemma 2 and (GP2) give a canonical isomorphism
\[
(f_*A)_y
=\mathop{\mathrm{colim}}_{y\in V}\Gamma(f^{-1}V;A)
\xrightarrow{\sim}\Gamma(X_y;A|_{X_y}).
\tag{GP7}
\]
Its map is restriction of sections. Choosing a bounded-below injective complex \(I^\bullet\) representing \(F\) applies (GP7) degree by degree. Inverse image to \(X_y\) is exact, so \(I^\bullet|_{X_y}\) represents \(F|_{X_y}\). Its terms are acyclic by (GP6). The acyclic-complex comparison therefore yields
\[
(Rf_*F)_y\xrightarrow{\sim}
R\Gamma(X_y;F|_{X_y}).
\tag{GP8}
\]
All identifications are induced by restriction and the natural resolution comparisons. This is the canonical fibre map, natural in \(F\).

For an ordinary sheaf \(A\), exactness of stalks gives
\[
(R^qf_*A)_y\simeq H^q(X_y;A|_{X_y})
\qquad(q\ge0).
\tag{GP9}
\]
If \(X_y\) is empty, the neighborhood with empty inverse image from Lemma 2 makes both sides of (GP7) and (GP8) zero. No argument identifying the fibre with a closed subspace of \(X\) has entered.

### The canonical base-change morphism

For a sheaf \(A\) on \(X\), the underived base-change map
\[
\beta_A:g^{-1}f_*A\longrightarrow f'_*g'^{-1}A
\tag{GP10}
\]
is the adjoint of
\[
f'^{-1}g^{-1}f_*A
\simeq g'^{-1}f^{-1}f_*A
\longrightarrow g'^{-1}A,
\]
where the last arrow is the inverse image of the section-evaluation counit. This specifies the map without choosing an abstract isomorphism.

At \(y'\in Y'\), put \(y=g(y')\). The projection \(g'\) restricts to a homeomorphism
\[
h:X'_{y'}\xrightarrow{\sim}X_y,
\qquad (x,y')\longmapsto x.
\tag{GP11}
\]
Its inverse is \(x\mapsto(x,y')\); both are continuous by the subspace and product topologies, even if the fibres are nonclosed. By (GP7), the stalk of (GP10) is the section pullback
\[
\Gamma(X_y;A|_{X_y})
\longrightarrow
\Gamma(X'_{y'};h^{-1}(A|_{X_y})),
\]
which is an isomorphism. This identification follows directly by restricting a representative section and pulling it back; these operations commute. Therefore \(\beta_A\) is an isomorphism of sheaves.

To derive this particular map, take the injective complex \(I^\bullet\) above. For each term \(I^j\), the sheaf \(g'^{-1}I^j\) need not be injective on \(X'\). What is needed, and what holds, is \(f'_*\)-acyclicity. Its restriction to a fibre \(X'_{y'}\), through (GP11), is the pullback of \(I^j|_{X_y}\) along a homeomorphism. It is therefore c-soft and acyclic for fibre sections. Apply (GP9) to the proper map \(f'\):
\[
(R^qf'_*g'^{-1}I^j)_{y'}=0
\qquad(q>0).
\]
Since stalks detect zero sheaves, \(g'^{-1}I^j\) is \(f'_*\)-acyclic.

Inverse image \(g'^{-1}\) is exact, so \(g'^{-1}I^\bullet\) represents \(g'^{-1}F\). The bounded-below acyclic-complex comparison shows that
\(f'_*g'^{-1}I^\bullet\)
represents \(Rf'_*g'^{-1}F\). Likewise \(g^{-1}f_*I^\bullet\) represents \(g^{-1}Rf_*F\), because \(g^{-1}\) is exact. Applying (GP10) termwise gives an isomorphism of these two representative complexes.

The actual-map identification can be expressed by a chain identity. Under \(f'^{-1}g^{-1}=g'^{-1}f^{-1}\), the definition of (GP10) gives
\[
\varepsilon_{f'}(g'^{-1}I^\bullet)
\circ f'^{-1}\beta_{I^\bullet}
=g'^{-1}\varepsilon_f(I^\bullet).
\tag{GP13}
\]
Here both \(\varepsilon\)'s are the ordinary section-evaluation counits, applied termwise. Pass to the derived categories using the proved acyclic comparisons. Their naturality carries (GP13) to the corresponding identity for the derived counits: this can also be checked by mapping \(g'^{-1}I^\bullet\) to an injective resolution and using naturality of ordinary evaluation. The resulting morphism is therefore the adjoint of the inverse image of the derived counit for \(f\), which is the defining canonical derived base-change morphism. Thus the isomorphism constructed above is precisely (GP1), not an independently chosen isomorphism. This proves the theorem.

The argument uses enough injectives for sheaves of modules, exactness of stalks and inverse image, and the bounded-below derived-functor construction. These hold for sheaves on arbitrary topological spaces. It imposes no finite-generation, flatness over \(\mathbb Z\), field or finite-global-dimension hypothesis on \(k\).

### A proper map with a nonclosed fibre

Let \(S=\{0,1\}\) have open sets \(\varnothing,\{1\},S\). The identity \(S\to S\) is universally closed, since every base change is an identity map. Its relative diagonal is an isomorphism, so it is separated. Thus it is proper in the present sense.

The fibre over \(1\) is the nonclosed subset \(\{1\}\subseteq S\). It is nevertheless a compact Hausdorff subspace, and ambient separation of distinct fibre points is vacuous. Formula (GP2) is the ordinary stalk formula at \(1\); (GP8) is the corresponding identity. This example explains why the general argument must not insert a closed-fibre or Hausdorff-ambient hypothesis.

The basic inputs have complete programme proofs: module sheaves and stalk exactness, Theorem 2.1, exact inverse image, Theorem 4.1, enough injectives, Theorem 2.3, and bounded-below derived functors, Theorem 4.1. The source credits and component terms of those readings remain attached to them. The general topological theorem and its classical route are credited above to the Stacks Project, Tags 09V3 and 09V6; the finite-index compactness test, ambient shrinking proof and actual-map calculation are written out here.

![Compact-germ gluing and the canonical proper-fibre comparison](figures/SH02-general-proper-base-change.svg)

The upper panel shows the compact-germ extension in GP2–GP3: ambient separation gives disjoint neighborhoods of $K_i\setminus A_{ij}$ and $K_j$, so the smaller representative neighborhoods overlap only where their sections agree. The lower panel shows cofinal fibre neighborhoods and the restriction square induced by the fibre homeomorphism, GP7–GP11. The shapes encode only the displayed set relations; the pieces are closed in $K$, without an ambient closedness assertion. Full-size diagram · Reproducible figure source.

<a id="proper-fibres-and-section-restriction"></a>

### Compact proper fibres and the section-restriction map

The general proof above applies to separated, universally closed maps of arbitrary topological spaces and arbitrary module coefficients. The following locally compact Hausdorff proof gives an alternative route to the exact specialization used for compact convex spaces and manifolds.

Let $k$ be a commutative ring, let $f:X\to Y$ be a continuous proper map of locally compact Hausdorff spaces, and let $F\in D^+(k_X)$. Here properness can equivalently be tested by compact inverse images, as in E3. Write $X_y=f^{-1}(y)$, with its subspace topology. The canonical restriction comparison is

\[
(Rf_*F)_y\xrightarrow{\sim}R\Gamma(X_y;F|_{X_y}).
\tag{PBC1}
\]

The needed programme proofs are compact-germ gluing and c-soft acyclicity, proper-fibre neighborhoods, and the derived fibre formula in *Duality maps for constructible inverse and direct images*, C1–C4, F1 and F6. Those sections explicitly work on locally compact Hausdorff spaces with arbitrary modules; the later standing manifold and finiteness conventions are unnecessary here.

To retain the actual comparison map, first note why the fibre neighborhoods are cofinal. Properness makes $f$ closed: if a closed $A\subset X$ misses $X_y$, choose a compact neighborhood $C$ of $y$. The compact set $A\cap f^{-1}C$ has closed image, so the interior of $C$ minus that image is a neighborhood of $y$ disjoint from $f(A)$. Applying this to $A=X\setminus W$ shows that every open neighborhood $W$ of $X_y$ contains $f^{-1}V$ for some open neighborhood $V$ of $y$. Compact-germ gluing therefore identifies, by restriction,

\[
\varinjlim_{y\in V}\Gamma(f^{-1}V;I)
\xrightarrow{\sim}\Gamma(X_y;I|_{X_y})
\]

for every sheaf $I$. Choose a bounded-below injective resolution $F\to I^\bullet$. An injective module sheaf is flabby and c-soft: a section on a compact subset first extends to a neighborhood by compact-germ gluing, and flabbiness extends it to the whole space. Its restriction to the closed compact fibre is c-soft, by C2. The compact lifting and acyclicity argument C3–C4 makes this restriction acyclic for ordinary sections on the compact fibre. Thus $I^\bullet|_{X_y}$ is a bounded-below acyclic resolution computing the right-hand side of (PBC1). Termwise compact-germ restriction identifies its sections complex with the stalk of $f_*I^\bullet$, which computes the left-hand side. All these identifications commute with resolution comparison maps, proving (PBC1) naturally in $F$. If $X_y$ is empty, closedness supplies a neighborhood with empty inverse image; both complexes are zero.

For a sheaf $F$ placed in degree zero this gives

\[
(R^qf_*F)_y\simeq H^q(X_y;F|_{X_y})\qquad(q\geq0).
\tag{PBC2}
\]

In degree zero the germ of a global section maps to its restriction to $X_y$. In particular the identification used in the compact-convex induction is the original evaluation map.

For a cartesian square of locally compact Hausdorff spaces

\[
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{g}&Y,
\end{array}
\]

the canonical comparison is

\[
g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F.
\tag{PBC3}
\]

Indeed, proper-support base change, D1 and D4, proves the bounded-below proper-support comparison for continuous maps of these spaces, using section pullback and acyclic resolutions. For a proper map $f_!=f_*$: the closed support of every section on $f^{-1}V$ is proper over $V$. The base-changed map $f'$ is also proper. Over compact $C\subset Y'$, its inverse image is a closed fibre-product subset of the compact space $f^{-1}(g(C))\times C$. Hence $f'_!=f'_*$ as well, giving (PBC3). In this specialization the section-pullback construction is the ordinary comparison described by the mate in E5. On stalks, (PBC1) identifies it with pullback along the homeomorphism $X'_{y'}\simeq X_{g(y')}$. No field, finite-generation, constructibility, finite-global-dimension, countability or finite-dimensional-space hypothesis is used.

## SH02-PRP-E6. The natural hypercohomology edge map

For $K\in D^+(k_X)$, [Tag 0BKM](https://stacks.math.columbia.edu/tag/0BKM) gives the spectral sequence of its canonical truncation filtration. Its indexing becomes

\[
E_2^{p,q}=H^p(X,H^qK)\Longrightarrow H^{p+q}R\Gamma(X,K).
\]

The bounded-below hypothesis means that for each fixed total degree only finitely many terms can occur: $p\geq0$ and $q$ has a lower bound. It does not impose an upper bound on all cohomology degrees of $X$. The detailed double-complex proof in [Tag 015J](https://stacks.math.columbia.edu/tag/015J) establishes convergence with a finite filtration in each total degree.

The edge morphism in degree $n$ can be specified without an arbitrary choice of a degeneration isomorphism. The canonical map $K\to\tau_{\geq n}K$ induces

\[
H^nR\Gamma(X,K)\longrightarrow
H^nR\Gamma(X,\tau_{\geq n}K)
\simeq\Gamma(X,H^nK).
\]

To justify the last isomorphism, use the truncation triangle from $H^nK[-n]$ to $\tau_{\geq n}K$ with third term $\tau_{\geq n+1}K$. The right derived functor of the left exact sections functor takes $D^{\geq n+1}$ into $D^{\geq n+1}$, so the terms in degrees $n-1$ and $n$ of that third term vanish after applying $R\Gamma$. This proves the displayed isomorphism. The construction is natural in $K$ and is the edge of the truncation filtration used in Tag 0BKM. If every $H^qK$ is acyclic for sections, the only nonzero spectral-sequence column is $p=0$; the finite filtration then identifies the displayed natural edge map as an isomorphism. For any other claimed comparison map one must still check agreement with this edge map.

<a id="bounded-below-hypercohomology-proof"></a>

### The full truncation construction and its finite convergence

For every topological space $X$, commutative ring $k$ and $K\in D^+(k_X)$ there is a natural spectral sequence

\[
E_2^{p,q}=H^p(X;H^qK)\Longrightarrow H^{p+q}R\Gamma(X;K),
\qquad d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}.
\tag{HC1}
\]

If $H^qK=0$ for $q<a$, only $p\geq0$ and $q\geq a$ occur, and the abutment in each total degree has a finite filtration. The following proof expands the exact-couple construction of *Derived pullback and pushforward*, Exercise 3, “Leray and convergence”, from its nonnegative complex to every bounded-below complex. Its other inputs are the good-truncation triangles proved in *Complexes, cones and localization*, §5, Lemma 5.3 and the lower-bound-preserving injective resolutions and acyclic-resolution comparison proved in *Injective modules and bounded-below derived functors*, §4. All three constructions apply to arbitrary module sheaves.

**HC1a. The exact couple and its pages.** First assume $H^qK=0$ for $q<0$ and represent $K$ by a nonnegative complex using good lower truncation. Put

\[
A_q=R\Gamma(X;\tau_{\leq q}K),\qquad
D_q^n=H^n(A_q),\qquad E_q^n=H^{n-q}(X;H^qK),
\]

where $A_q=0$ for $q<0$. Applying derived sections to the good-truncation triangles gives maps

\[
i:D_q^n\to D_{q+1}^n,\qquad
j:D_q^n\to E_q^n,\qquad
\partial:E_q^n\to D_{q-1}^{n+1}.
\]

Their long exact sequences state that $\ker j=\operatorname{im}i$, $\ker\partial=\operatorname{im}j$ and $\ker i=\operatorname{im}\partial$, at the indicated indices. For $r\geq2$ define

\[
\begin{aligned}
Z_r^{n,q}
 &=\partial^{-1}\!\left(\operatorname{im}
  (i^{r-2}:D_{q-r+1}^{n+1}\to D_{q-1}^{n+1})\right),\\
B_r^{n,q}
 &=j\ker(i^{r-2}:D_q^n\to D_{q+r-2}^n),\\
E_r^{p,q}&=Z_r^{p+q,q}/B_r^{p+q,q}.
\end{aligned}
\]

Here $B_r^{n,q}\subset Z_r^{n,q}$ because $\partial j=0$. At $r=2$ the power is the identity, so $Z_2^{n,q}=E_q^n$ and $B_2^{n,q}=0$. This is the asserted second page.

For $e\in Z_r^{n,q}$ choose $x\in D_{q-r+1}^{n+1}$ with $i^{r-2}x=\partial e$, and set

\[
d_r[e]=[jx]\in E_r^{n+1-(q-r+1),\,q-r+1}.
\]

Two choices of $x$ differ by a kernel of $i^{r-2}$, whose image under $j$ is the target boundary subgroup. Changing $e$ by an element of $B_r^{n,q}$ leaves $\partial e$ unchanged. Thus $d_r$ is well defined. Its target representative satisfies $\partial jx=0$, so it belongs to the target cycle subgroup; choosing zero as a lift of $\partial jx$ also proves $d_r^2=0$. Since the total degree increases by one and the second index decreases by $r-1$, its bidegree is $(r,1-r)$.

For completeness, its cohomology gives exactly the next stated quotient. If $d_r[e]=0$, write $jx=jy$ for $y\in D_{q-r+1}^{n+1}$ with $i^{r-2}y=0$. Exactness gives $x-y=iz$ for some $z\in D_{q-r}^{n+1}$. Hence $\partial e=i^{r-1}z$, so $e\in Z_{r+1}^{n,q}$. Conversely this last condition allows the choice $x=iz$, making $jx=0$. Thus the cycles on page $r$ are $Z_{r+1}^{n,q}/B_r^{n,q}$.

An incoming differential with value $[jx]$, where $x\in D_q^n$, has $i^{r-2}x=\partial e$ and consequently $i^{r-1}x=0$. Its image therefore lies in $B_{r+1}^{n,q}/B_r^{n,q}$. Conversely, if $i^{r-1}x=0$, exactness provides $e\in E_{q+r-1}^{n-1}$ such that $\partial e=i^{r-2}x$. This $e$ lies in the required incoming $Z_r$, and its differential is $[jx]$. The image is precisely $B_{r+1}^{n,q}/B_r^{n,q}$. Dividing cycles by images proves $H(E_r,d_r)=E_{r+1}$.

**HC1b. Convergence and the lower-bound shift.** Derived sections preserve cohomological lower bounds, since the bounded-below injective-resolution construction can start at the given lower bound. Therefore the triangle for $\tau_{\leq q}K\to K\to\tau_{\geq q+1}K$ gives

\[
D_q^n\xrightarrow{\sim}T^n:=H^nR\Gamma(X;K)\qquad(q\geq n).
\]

Give $T^n$ the filtration $F_qT^n=\operatorname{im}(D_q^n\to T^n)$. For fixed $(n,q)$ and sufficiently large $r$, the source $D_{q-r+1}^{n+1}$ in the definition of $Z_r$ is zero, and the target $D_{q+r-2}^n$ in the definition of $B_r$ is identified with $T^n$. Consequently

\[
E_\infty^{n-q,q}
\simeq\frac{\operatorname{im}j}{j\ker(D_q^n\to T^n)}
\simeq F_qT^n/F_{q-1}T^n.
\]

For the second isomorphism, $\ker j=\operatorname{im}(D_{q-1}^n\to D_q^n)$, and the inverse image of $F_{q-1}T^n$ in $D_q^n$ is this image plus $\ker(D_q^n\to T^n)$. The filtration starts with $F_{-1}=0$ and reaches $F_n=T^n$ for $n\geq0$; for $n<0$ the abutment is zero. This proves convergence with a finite filtration in each total degree without a dimension bound on $X$.

For a general lower bound $a$, apply the construction to $K[a]$, whose cohomology satisfies $H^q(K[a])=H^{q+a}K$. Replacing its second index by $q+a$ shifts the total degree by the same $a$ and gives (HC1) in the original grading. In total degree $n\geq a$ the filtration runs from $F_{a-1}=0$ to $F_n=T^n$; for $n<a$ it is zero. The good truncations, derived sections, exact-couple maps and quotient constructions are natural in $K$. They therefore give a natural spectral sequence and natural abutment filtration.

**HC2. The canonical edge and the section-to-germ map.** The edge is the morphism already displayed in E6:

\[
H^nR\Gamma(X;K)\longrightarrow
H^nR\Gamma(X;\tau_{\geq n}K)
\xrightarrow{\sim}\Gamma(X;H^nK).
\tag{HC2}
\]

The last arrow is the inverse of the isomorphism induced by $H^nK[-n]\to\tau_{\geq n}K$, as follows from its truncation triangle and preservation of lower bounds. To identify this particular morphism with the spectral-sequence edge, use the commuting square

\[
\begin{array}{ccc}
\tau_{\leq n}K&\longrightarrow&K\\
\downarrow&&\downarrow\\
H^nK[-n]&\longrightarrow&\tau_{\geq n}K.
\end{array}
\]

On a complex representing $K$ this square sends a degree-$n$ cycle to its class modulo boundaries; in the other degrees commutativity follows from the good-truncation maps. After applying $H^nR\Gamma$, the top arrow is $D_n^n\simeq T^n$, the left arrow is the exact-couple map $j$, and the bottom arrow is the preceding isomorphism. Hence (HC2) is exactly the edge. If all $H^qK$ are acyclic for sections, only the column $p=0$ survives, the finite filtration has $F_{n-1}T^n=0$, and (HC2) is an isomorphism.

For $x\in X$, the exact stalk functor commutes with good truncations. Applying section restriction to an injective resolution gives the natural map $R\Gamma(X;K)\to K_x$, and the same square commutes with this map. Thus (HC2), followed by the section-to-germ map $\Gamma(X;H^nK)\to(H^nK)_x=H^n(K_x)$, is the original map $H^nR\Gamma(X;K)\to H^n(K_x)$. This proves the compatibility used by the star-section counit with arbitrary module coefficients.

![The fibre restriction comparison and the finite truncation filtration](figures/SH02-fibres-and-hypercohomology.svg)

The fibre panel depicts the section-restriction map in (PBC1)–(PBC2); the truncation panel displays the finite filtration and edge proved in HC1a–HC2. The diagram illustrates these constructions; the hypotheses and maps are those of the proofs above. Full-size diagram · Reproducible figure source.

## SH02-PRP-E7. The exact projection/base-change compatibility

Let the square in E5 now be any commutative square of ringed spaces. Cartesian, flat, and proper hypotheses are not needed for the existence or the compatibility of the following morphisms. Put

\[
L=Lf^*,\quad R=Rf_*,\quad L'=L(f')^*,\quad R'=R(f')_*,
\quad A=Lg^*,\quad B=L(g')^*.
\]

The pullback composition isomorphism identifies $L'A$ with $BL$; denote it by $\alpha:L'A\simeq BL$. All tensor products in this paragraph are derived over the structure sheaf of the space on which their two factors live. In particular the tensor inside $R'$ is over $\mathcal O_{X'}$. We suppress the canonical monoidal isomorphisms for $L,L',A,B$, always keeping the $E$ factor before the $K$ factor.

Write $\epsilon:LR\to\operatorname{id}$ and $\epsilon':L'R'\to\operatorname{id}$ for the counits. For $E\in D(\mathcal O_X)$, the base-change map $\beta_E:ARE\to R'BE$ is defined by

\[
\epsilon'_{BE}\,L'\beta_E=B\epsilon_E\,\alpha_{RE}.
\tag{1}
\]

This is the adjunction construction in [Tag 08HY](https://stacks.math.columbia.edu/tag/08HY). For $K\in D(\mathcal O_Y)$, the projection map $\pi_f(E,K):RE\otimes K\to R(E\otimes LK)$ is characterized by

\[
\epsilon_{E\otimes LK}\,L\pi_f(E,K)
=\epsilon_E\otimes\operatorname{id}_{LK}.
\tag{2}
\]

That is the construction preceding [Tag 0B54](https://stacks.math.columbia.edu/tag/0B54).

There are two routes from $A(RE\otimes K)$ to $R'(BE\otimes L'AK)$. The first applies $A\pi_f$, then $\beta_{E\otimes LK}$, then the tensor isomorphism for $B$ and $\alpha_K^{-1}:BLK\to L'AK$. The second applies the tensor isomorphism for $A$, then $\beta_E\otimes\operatorname{id}_{AK}$, then $\pi_{f'}(BE,AK)$. These are the two routes in Remark 20.54.5 of [Tag 01E6](https://stacks.math.columbia.edu/tag/01E6).

Apply the bijection of morphism sets for $L'\dashv R'$. A map $u:S\to R'T$ is sent to $\epsilon'_T L'u$. For the first route, naturality of $\epsilon'$ moves the final map inside $R'$ outside the counit. Equation (1) applied to $E\otimes LK$, followed by naturality of $\alpha$ for $\pi_f(E,K)$ and equation (2), gives the mate

\[
L'A(RE\otimes K)
\simeq BLRE\otimes BLK
\xrightarrow{B\epsilon_E\otimes\operatorname{id}}BE\otimes BLK
\xrightarrow{\operatorname{id}\otimes\alpha_K^{-1}}BE\otimes L'AK.
\tag{3}
\]

For the second route, equation (2) for $f'$ first replaces the counit followed by $L'\pi_{f'}$ with $\epsilon'_{BE}\otimes\operatorname{id}_{L'AK}$. The remaining first-factor composite is $\epsilon'_{BE}L'\beta_E$, which is $B\epsilon_E\alpha_{RE}$ by (1). After the tensor and pullback-composition isomorphisms, this is exactly (3). Since the adjunction bijection is injective, the two original routes are equal. All identities are natural in $E,K$, so the verification applies to every object in the asserted unbounded derived categories.

This proves precisely the compatibility whose verification the cited remark omits. The saved official diagram writes $\mathcal O_{Y'}$ on the two tensor products inside $R'$; the present statement uses $\mathcal O_{X'}$, as their factor types require. The proof uses no invertibility of $\beta$ or $\pi$ and gives no projection formula for $Rf_!$.

## SH02-PRP-E8. The two projection isomorphisms retain their exact scopes

For the perfect projection formula, the map of E7 is local on $Y$ and is a natural transformation between exact functors of $K$. Locally a perfect complex is a bounded complex of finite projective modules. Each finite projective term is a direct summand of a finite free module; a bounded complex is built from its shifted terms by its finite stupid-truncation triangles. Both functors and the transformation respect shifts, finite sums, these triangles, and direct summands. It therefore suffices to check $K=\mathcal O_Y[n]$. After the tensor-unit and shift identifications, (2) identifies that projection map with the identity of $RE[n]$ by the adjunction triangle identity. This proves the scope of [Tag 0B54](https://stacks.math.columbia.edu/tag/0B54): arbitrary $E$, perfect $K$, arbitrary ringed-space morphism, unbounded ambient categories.

For a homeomorphism $i:X\to Y$ onto a closed subset, $i_*$ is exact and commutes with direct sums. On sheaf stalks these claims reduce respectively to exactness and direct sums at $x$ when $y=i(x)$, and to zero when $y\notin i(X)$. These stalk formulas also identify the ordinary projection map as an isomorphism: at $y=i(x)$ it is the canonical associativity map

\[
E_x\otimes_{\mathcal O_{Y,y}}P_y
\longrightarrow
E_x\otimes_{\mathcal O_{X,x}}
(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}P_y).
\]

Choose a K-flat representative $P$ for an arbitrary $K$. Its pullback is K-flat, so the derived projection comparison is computed by this degreewise isomorphism followed by the direct-sum totalization. Exactness of $i_*$ and its preservation of these sums make the totalized map an isomorphism. This verifies the arbitrary-$K$ scope of [Tag 0B55](https://stacks.math.columbia.edu/tag/0B55). Neither case establishes the arbitrary-$K$ projection isomorphism for a general map.

## SH02-PRP-DF-A — Coefficients, models and unbounded totalization

Let `k` be any commutative unital ring. A sheaf of `k`-modules is equivalently a module sheaf over `k_X`: multiplication by locally constant functions is defined on a cover where the functions are constant and glued. Conversely a `k_X`-module carries its constant scalar action. No topology restriction occurs in this equivalence.

For continuous `f:X→Y`, the canonical map `f^{-1}k_Y→k_X` is an isomorphism because its stalk at `x` is the identity of `k`. The inverse-image functor is exact. Hence its termwise application preserves quasi-isomorphisms, and `Lf^*=f^{-1}` on the entire unbounded derived category. This is a constant-ring statement; it does not assert exactness of extension of scalars for an arbitrary ringed-space morphism.

We use cohomological complexes. For a homogeneous element `a` of degree `p`, tensor totalization has differential

\[
d(a\otimes b)=d_Aa\otimes b+(-1)^p a\otimes d_Bb.
\]

The degree-`n` tensor term is the direct sum over `p+q=n`. The internal Hom complex has degree-`r` term

\[
\mathcal H^r(A,B)=\prod_{p\in\mathbb Z}
\mathcal{H}om(A^p,B^{p+r}),
\qquad d(h)=d_Bh-(-1)^r h d_A.
\]

The terms involving `d_B h d_A` cancel when this differential is applied twice; the two remaining terms contain `d_B^2` or `d_A^2`, hence vanish. The products here must not be replaced with direct sums. Conversely tensor totalization uses direct sums, so an element in one tensor degree is locally a finite sum of elementary tensors. The calculations below never commute an inverse-image functor with an arbitrary product.

## SH02-PRP-DF-B — Resolution independence and tensor coherence

For two termwise surjective K-flat resolutions `P_i→E`, form the ordinary fibre product complex `W=P_1×_E P_2`. Each projection `W→P_i` is a quasi-isomorphism: its kernel is the acyclic kernel of the other resolution, and the projection is termwise surjective. Choose a K-flat resolution `Q→W`. The resulting maps `Q→P_i` are quasi-isomorphisms of K-flat complexes. By `06YG`, tensoring these maps with any complex still gives quasi-isomorphisms. This gives explicit common comparison models without claiming there must be a direct quasi-isomorphism from one chosen resolution to the other.

The canonical comparison and its independence are expressed in the homotopy category localized at quasi-isomorphisms. In particular, when two roofs represent the same morphism, the common-refinement equivalence used by localization makes their induced tensor maps equal. K-flat models suffice for every object and every such refinement: replace the middle complex of a roof by a K-flat resolution. Thus tensor on K-flat complexes descends to the derived bifunctor, with the same comparison maps.

Associativity is already the chain isomorphism

\[
(A\otimes B)\otimes C\longrightarrow A\otimes(B\otimes C),
\qquad (a\otimes b)\otimes c\longmapsto a\otimes(b\otimes c).
\]

It commutes with the differential because both sides have the three terms with signs `1`, `(-1)^{|a|}`, and `(-1)^{|a|+|b|}`. For four factors, every route around the associativity pentagon sends a homogeneous tensor to the same ordered tensor. The unit is the structure sheaf in degree zero; both unit identities follow by scalar multiplication. Symmetry is

\[
a\otimes b\longmapsto (-1)^{|a||b|}b\otimes a.
\]

Moving a factor of degree `p` past degrees `q` and `r` gives sign `(-1)^{p(q+r)}`, the product of the two successive signs. This proves the symmetry coherence identities. Tensor products of K-flat complexes are K-flat, so all these diagrams descend on simultaneous K-flat models. This justifies the associators and symmetries used later without a boundedness assumption.

For a ringed-space map, the monoidal map on pullbacks is the map sending `(s⊗a)⊗(t⊗b)` to `st⊗(a⊗b)` in local extension-of-scalars notation. The coefficient factors are degree zero. Its associativity, unit and symmetry diagrams commute by multiplication in the structure sheaf and the same Koszul rule. Likewise the comparison for two successive pullbacks multiplies the two coefficient factors; three successive pullbacks give the same product under both parenthesizations. Applying these identities to K-flat models proves coherent composition and the strong symmetric monoidal structure of `Lf^*` used below.

## SH02-PRP-DF-C — Currying and the derived closed structure

For a degree-`n` homogeneous map `α:A→𝓗(B,C)`, define

\[
\Psi(\alpha)(a\otimes b)=\alpha(a)(b).
\]

If `|a|=p`, the differential of either side under this identification is

\[
d_C(\alpha(a)(b))
-(-1)^n\alpha(d_Aa)(b)
-(-1)^{n+p}\alpha(a)(d_Bb).
\]

Consequently `Ψ` is a chain map. Its inverse is currying each component. The component bijections use the ordinary sheaf tensor-Hom adjunction, Hom into products, and Hom out of direct sums. They are valid for all indices, so the map is an isomorphism for unbounded complexes. Its formula commutes with restriction and with pre- or postcomposition, proving functoriality as well.

For an open inclusion `j:U→X` and K-injective complex `I`, the complex `I|_U` is K-injective. Indeed, for every acyclic complex `A` on `U`, exactness of `j_!` makes `j_!A` acyclic, while the chain adjunction gives

\[
\operatorname{Hom}_{K(U)}(A,I|_U)
=\operatorname{Hom}_{K(X)}(j_!A,I)=0.
\]

This argument applies after every shift. For an acyclic complex `A` on `X`, therefore, every open `U` has zero cohomology in every degree for `Γ(U,𝓗(A,I))`: the degree-`n` group is the homotopy-category Hom from `A|_U` to `I|_U[n]`. Sheafifying these cohomology presheaves proves that `𝓗(A,I)` is acyclic. This proves that a quasi-isomorphism in the first Hom variable induces a quasi-isomorphism after reversing arrows. In the second variable, a quasi-isomorphism between K-injective complexes is a homotopy equivalence, and applying `𝓗(A,-)` preserves a homotopy equivalence. This supplies the all-degree step left implicit by the displayed degree-zero calculation in `0A8S`.

Choose a K-injective model `I` of `C` and a K-flat model `P` of `B`. Currying gives, for every acyclic `A`,

\[
\operatorname{Hom}_{K(X)}(A,\mathcal H(P,I))
=\operatorname{Hom}_{K(X)}(A\otimes P,I)=0.
\]

Here `A⊗P` is acyclic by K-flatness. Thus `𝓗(P,I)` is K-injective, so the preceding chain-currying isomorphism computes the derived one. In particular

\[
\operatorname{Hom}_{D(X)}(T,R\mathcal{H}om(B,C))
\simeq
\operatorname{Hom}_{D(X)}(T\otimes^L B,C).
\]

This establishes the precise closed structure used below. Its open-restriction comparison is an isomorphism because the chosen K-injective model remains K-injective on the open and chain internal Hom restricts there term by term. This proof uses open restriction; it says nothing analogous about arbitrary closed restriction or general inverse image of internal Hom.

## SH02-PRP-DF-D — The exact unbounded coefficient adjunction

Take `f:X→Y` continuous with constant coefficient ring `k`, and let `I` be a K-injective complex on `X`. Its direct image `f_*I` is K-injective on `Y`: for every acyclic complex `A` on `Y`,

\[
\operatorname{Hom}_{K(Y)}(A,f_*I)
=\operatorname{Hom}_{K(X)}(f^{-1}A,I)=0.
\]

Exact inverse image was essential here. With `E→I` a K-injective resolution and any complex `B` on `Y`, this gives

\[
\begin{aligned}
\operatorname{Hom}_{D(X)}(f^{-1}B,E)
&=\operatorname{Hom}_{K(X)}(f^{-1}B,I)\\
&=\operatorname{Hom}_{K(Y)}(B,f_*I)\\
&=\operatorname{Hom}_{D(Y)}(B,Rf_*E).
\end{aligned}
\]

The middle equality is the chain adjunction and commutes with precomposition in `B` and postcomposition between K-injective models of `E`. Derived morphisms of the latter models are homotopy classes; their representatives and homotopies are respected by the chain adjunction. A change of model gives a homotopy equivalence and hence the same comparison. This proves the bifunctorial unbounded adjunction actually needed after coefficient specialization.

For arbitrary ringed-space morphisms, use the exact general theorem `079W`; the preceding argument must not be copied with `f^*` in place of exact inverse image. To check the omitted naturality in its ultimate reference `0FND`, observe that the underlying adjunction sends a representative `P→F(I)` to its transpose `G(P)→I`. Naturality for maps of `P` and `I` is precisely ordinary adjunction naturality. Therefore it commutes with every refinement transition of the localization roofs. It descends through the two Hom-colimits and the canonical ind/pro identifications. Maps in the localized category are compositions of original maps and inverses of denominators; the descended naturality identities hold for both, because a commuting identity remains commuting after inversion of an invertible comparison. This fills the naturality step relative to the stated localization and representability lemmas, without asserting those lemmas' entire dependency trees have been independently re-proved here.

## SH02-PRP-DF-E — Evaluation, composition, signs and variance

In the closed category `D(𝒪_X)`, abbreviate `H(A,B)=R𝓗om(A,B)` and tensor by `⊗`. Let

\[
e_{A,B}:H(A,B)\otimes A\longrightarrow B
\]

be the transpose of the identity of `H(A,B)`. Define

\[
c_{A,B,C}:H(B,C)\otimes H(A,B)\longrightarrow H(A,C)
\]

as the unique transpose of

\[
H(B,C)\otimes H(A,B)\otimes A
\xrightarrow{\,1\otimes e_{A,B}\,}
H(B,C)\otimes B
\xrightarrow{\,e_{B,C}\,} C.
\tag{DF-EVAL}
\]

These are the actual Stacks evaluation and composition maps. To see this on models, take a complex representing `A`, K-injective complexes representing `B` and `C`, and K-flat resolutions of the Hom factors and of `A` when computing the tensor source. The complex-level map sends a homogeneous pair `(g,f)` to `g∘f`; evaluation sends `(h,a)` to `h(a)`. The differential identity is

\[
d(g\circ f)=d(g)\circ f+(-1)^{|g|}g\circ d(f).
\]

The two middle terms involving the differential of `B` cancel. There is no further sign in this ordered composition. The composite evaluated at `a` is `g(f(a))`, which is also the chain formula in `0A8V` after the K-flat comparison. Thus its transpose is exactly `c`, independent of all models by the derived adjunction. This identifies the imported arrow, rather than merely constructing a possibly different composition.

For `u:A'→A` and `w:C→C'`, ordinary outer naturality reads

\[
H(u,w)c_{A,B,C}
=c_{A',B,C'}\bigl(H(1_B,w)\otimes H(u,1_B)\bigr).
\tag{DF-OUTER}
\]

Here `H(u,w)` means precomposition by `u` and postcomposition by `w`. Tensor with `A'` and evaluate. Both sides successively apply `u`, evaluation into `B`, evaluation into `C`, and `w`; naturality of evaluation gives equality, and the adjunction detects equality of the original arrows.

The middle variable occurs with opposite variances in the two input factors. For `v:B→B'`, the correct assertion is the equality of two arrows with source `H(B',C)⊗H(A,B)`:

\[
c_{A,B,C}\bigl(H(v,1_C)\otimes 1\bigr)
=c_{A,B',C}\bigl(1\otimes H(1_A,v)\bigr).
\tag{DF-MIDDLE}
\]

After tensoring with `A`, both sides evaluate `A` into `B`, apply `v`, and then evaluate into `C`. They therefore have equal transposes. This is middle dinaturality. Calling the expression a covariant functor of three independent variables would not even type-check; the compatibility above is what is used by composition diagrams.

For four objects, the two parenthesizations of composition give arrows

\[
H(C,D)\otimes H(B,C)\otimes H(A,B)\longrightarrow H(A,D).
\]

After tensoring with `A`, both are the same ordered sequence of three evaluation maps, by applying `DF-EVAL` twice. Tensor associativity from B makes their parenthesizations identical. The closed adjunction then proves equality of the two arrows. Hence composition is associative without a boundedness, finite-rank, or perfectness assumption.

Let `i_A:𝒪_X→H(A,A)` be the transpose of `id_A`. The equation defining this transpose says that evaluation after `i_A⊗1_A` is the left unit map of `A`. Substituting it in `DF-EVAL` proves that inserting `i_A` on either side of a composition acts as the identity. These are the two unit laws. On degree-zero global derived Hom, this gives ordinary composition, since the defining evaluation of a transpose sends the corresponding morphism to itself. Homogeneous chain signs have already been fixed above; a sign appears only when factors are actually interchanged by the Koszul symmetry.

## SH02-PRP-DF-F — Compatibility with pullback and iterated pullback

Write `F=Lf^*`, and use the monoidal isomorphism in the direction

\[
\mu_{P,Q}:FP\otimes FQ\xrightarrow{\sim}F(P\otimes Q).
\]

Define `β_{A,B}:F H_Y(A,B)→H_X(FA,FB)` by the equation

\[
e^X_{FA,FB}(\beta_{A,B}\otimes 1_{FA})
=F(e^Y_{A,B})\mu_{H_Y(A,B),A}.
\tag{DF-PULL-EVAL}
\]

Existence and uniqueness follow from the closed adjunction. This is precisely the evaluation definition in `08I3`. It is natural contravariantly in `A` and covariantly in `B`: tensor a proposed naturality square with the appropriate source object and use evaluation naturality on each side. The defining transpose is unique, so the square commutes.

The composition identity is

\[
\beta_{A,C}\,F(c^Y_{A,B,C})\,
\mu_{H_Y(B,C),H_Y(A,B)}
=c^X_{FA,FB,FC}(\beta_{B,C}\otimes\beta_{A,B}).
\tag{DF-PULL-COMP}
\]

Both sides have source `F H_Y(B,C)⊗F H_Y(A,B)` and target `H_X(FA,FC)`. Tensor with `FA` and evaluate into `FC`. Substitute `DF-PULL-EVAL` for each `β` on the right. Monoidal associativity and naturality of `μ` reduce that side to

\[
F\!\left(e^Y_{B,C}(1\otimes e^Y_{A,B})\right)\mu_3,
\]

where `μ_3` is the canonical comparison from the tensor of the three pulled-back factors to the pullback of their tensor. The left side reduces to the same expression by `DF-EVAL` and `DF-PULL-EVAL`. Uniqueness of the transpose proves the identity.

If `μ_0:𝒪_X→F𝒪_Y` is the monoidal unit identification, then

\[
\beta_{A,A}F(i_A)\mu_0=i_{FA}.
\tag{DF-PULL-UNIT}
\]

To verify it, tensor with `FA` and use `DF-PULL-EVAL`; both sides become `id_{FA}`. This also proves compatibility with the ordinary identity endomorphism.

For another derived pullback `G`, identify `FG` with the pullback for the composite using `0D5S`. The comparison for the composite is

\[
\beta^{FG}_{A,B}
=\beta^F_{GA,GB}\,F(\beta^G_{A,B}).
\tag{DF-PULL-ITERATE}
\]

Indeed, evaluate the right side on `FGA`, use `DF-PULL-EVAL` first for `F` and then for `G`, and use the composite monoidal structure. The resulting evaluation is `FG(e_{A,B})` with the composite tensor comparison, exactly the defining evaluation of the left side. For an identity map the same equation gives the identity comparison. All equations remain true when a pullback is an open restriction; the corresponding `β` is then the restriction isomorphism from C.

None of these equations makes `β` invertible for a general map. For example, for the one-point ringed-space morphism associated to `Z→Q`, put `A=⊕_{n≥1}Z` and `B=Z` in degree zero. The degree-zero comparison is

\[
\mathbb Q\otimes_{\mathbb Z}\prod_{n\ge1}\mathbb Z
\longrightarrow\prod_{n\ge1}\mathbb Q.
\]

Its image consists of rational sequences with a common denominator. The sequence `(1/n!)_{n≥1}` has no common denominator, so the map is not surjective. All derived objects in this example are computed as stated: `A` is projective, `Q` is flat, and after scalar extension `⊕Q` is projective. This confirms why the original public comparison correctly refrains from an unconditional isomorphism claim.

<a id="SH02-PRP-WHITNEY-TUBE"></a>

<a id="sh02-prp-whitney-tube--the-rank-test-for-a-whitney-tube"></a>

## The rank test for a Whitney tube

Let \(V\) be closed in a finite-dimensional smooth manifold \(M\), with a locally finite smooth Whitney $(a,b)$ stratification and the frontier rule. Write \(S<T\) when \(S\subset\overline T\setminus T\). A smooth tubular chart for \(S\) has base projection \(\pi_S\) and squared normal norm \(\rho_S\); its zero set is \(S\). For an incident upper stratum \(T\), after shrinking this tube near every point of \(S\), the map

\[
(\pi_S,\rho_S)|_T:T\cap\mathcal T_S
\longrightarrow S\times(0,\infty)
\quad\text{is a submersion}.
\tag{WT1}
\]

**Proof.** In a local orthonormal trivialization of the normal bundle, use the tubular chart to write \(S=\mathbb R^d\times\{0\}\), \(\pi_S(u,w)=u\) and \(\rho_S(u,w)=|w|^2\). Whitney $(a,b)$ is invariant under this smooth change of coordinates: tangent planes transform by its derivative, and a secant difference transforms by the derivative at its limiting base plus \(o\) of the secant's length. At \(y=(u,w)\in T\), with \(w\ne0\), the kernel of \(d(\pi_S,\rho_S)\) is the orthogonal complement of

\[
E_y=(\mathbb R^d\times\{0\})
\oplus\mathbb R(0,w/|w|).
\tag{WT2}
\]

If (WT1) failed arbitrarily close to \(p\in S\), choose \(y_j\to p\) at which it fails. After subsequences, the fixed-dimensional planes \(T_{y_j}T\) and the unit normal secants \((0,w_j/|w_j|)\) converge to a plane \(L\) and a vector \(e\). Whitney $(a)$ puts \(T_pS\) in \(L\); Whitney $(b)$, using the lower point \(\pi_S(y_j)\), puts \(e\) in \(L\). Thus the limit of \(E_{y_j}\) lies in \(L\). Failure of surjectivity supplies a unit vector in \(E_{y_j}\cap(T_{y_j}T)^\perp\). A convergent subsequence would give a unit vector in both \(L\) and \(L^\perp\), a contradiction. This proves the local shrinking assertion. Local finiteness allows simultaneous shrinking for the finitely many upper strata near any given lower point. \(\square\)

This is a rank lemma for a given tube. It does not construct mutually compatible tubes for all strata, or tubes compatible with a prescribed stratified submersion.

<a id="SH02-PRP-CONTROLLED-FLOW"></a>
<a id="sh02-prp-controlled-flow--from-a-controlled-field-to-an-open-local-flow"></a>

## From a controlled field to an open local flow

Suppose tubular control data have been supplied. Their neighborhoods may be shrunk to meet only their base stratum and incident higher strata. A stratified field \(\eta\) is a \(C^1\) tangent vector field \(\eta_T\) on each stratum \(T\). It is **controlled** when, for every \(S\), there is an open tube \(\mathcal T'_S\) on which, for every \(T>S\),

\[
d\rho_S(\eta_T)=0,\qquad
 d\pi_S(\eta_T)=\eta_S\circ\pi_S.
\tag{CF1}
\]

The usual compatibility identities between different tubes remain part of the supplied data. For the flow argument we use their tubular norm, their incident-stratum neighborhoods, and precisely (CF1). No continuity of \(\eta\) as an ambient vector field is assumed.

**Compact tube observation.** If \(K\subset S\) is compact, a sufficiently small constant \(c>0\) gives a compact set

\[
C(K,c)=\{z\in V\cap\mathcal T'_S:
\pi_S(z)\in K,\ \rho_S(z)\le c\}.
\tag{CF2}
\]

Indeed choose a closed normal disk bundle over \(K\) of squared radius \(c\) entirely inside the open controlled tube. It is compact, and its tubular image is compact. Intersecting it with the closed set \(V\) remains compact and gives exactly (CF2). Compactness of \(K\) gives a common positive radius. This argument also shows that these tubes with radius tending to zero form a neighborhood basis over compact base pieces.

The intersection of a positive-radius level with one upper stratum need not be compact. For example, in the partition of \(\mathbb R^2\) into the origin, the punctured horizontal axis and its complement, a circle centered at the origin meets the open stratum in a circle with two points deleted. The compact set used below is the closed tube in \(V\), not that stratum intersection.

**Controlled-flow theorem.** The union of the ordinary maximal flows of the fields \(\eta_T\) defines a continuous stratum-preserving flow \(\alpha:J\to V\), where \(J\subset\mathbb R\times V\) is open and contains \(\{0\}\times V\). Its domain on each point is the ordinary maximal interval on that point's stratum. At every finite endpoint a trajectory leaves every compact subset of \(V\). Fixed-time maps are homeomorphisms between their open domains, with the opposite-time map as inverse.

**Finite endpoints.** Let a trajectory in \(T\) have finite positive endpoint \(b\). If it returned to a compact subset arbitrarily close to \(b\), a subsequence would converge to some \(y\in V\). Let \(S\) contain \(y\). If \(S=T\), ordinary \(C^1\) ODE existence near \(y\) gives a uniform extension time and contradicts maximality. Otherwise the frontier rule gives \(S<T\).

Choose a compact neighborhood of \(y\) in \(S\) on which the lower flow exists for a common small positive time \(\delta\). Its trajectories lie inside a larger compact base piece \(K\subset S\). Choose (CF2) inside the controlled tube, with room in both base and radius. For a sufficiently late trajectory point \(z_i\) tending to \(y\), its projection is in the chosen lower neighborhood, its positive radius is smaller than the chosen bound, and \(b-t_i<\delta\). As long as the upper trajectory stays in the tube, uniqueness of the lower ODE and (CF1) give

\[
\rho_S(\alpha(t_i+s,z))=\rho_S(z_i)>0,\qquad
\pi_S(\alpha(t_i+s,z))
=\alpha_S(s,\pi_S(z_i)).
\tag{CF3}
\]

Here \(z\) is the original starting point and \(z_i=\alpha(t_i,z)\). These identities hold all the way up to \(b\): a first exit before \(b\) is impossible because the base stays in the interior of the chosen compact base neighborhood and the radius stays strictly below its bound. The closed tube containing those points lies inside the open control neighborhood, so a first exit point would still be an interior tube point. The returning subsequence must therefore have constant positive \(\rho_S\), contradicting \(\rho_S(y)=0\). This proves escape from every compact set at \(b\). Replacing \(\eta\) by \(-\eta\) proves the assertion at a finite negative endpoint. No escape assertion is needed at an infinite endpoint.

**Openness and continuity across strata.** Fix \((t,x)\in J\), with \(x\in S\). Choose a slightly larger compact time interval \(I\) containing both \(0\) and \(t\) in its interior. Ordinary flow on \(S\) gives a compact neighborhood of \(x\) whose trajectories for times in \(I\) lie inside the interior of a compact base piece \(K\subset S\). For nearby points \(y\in V\), their projections lie in that neighborhood and their tube radii are sufficiently small. Until a possible endpoint, (CF1) gives

\[
\rho_S(\alpha(s,y))=\rho_S(y),\qquad
\pi_S(\alpha(s,y))=\alpha_S(s,\pi_S(y)).
\tag{CF4}
\]

The first-exit argument keeps these trajectories in a fixed compact controlled tube. An endpoint before the end of \(I\) would contradict the compact-escape assertion just proved. Thus \(I\times W\subset J\) for an open neighborhood \(W\) of \(x\) in \(V\), proving openness of \(J\).

For \((s_j,y_j)\to(t,x)\), the same compact tube applies. Equation (CF4) makes their output projections tend to \(\alpha_S(t,x)\) and their radii tend to zero. Every subsequential output limit is therefore the zero normal vector over that projected point, namely \(\alpha_S(t,x)\). Compactness then gives convergence of all outputs, proving continuity. The space is metrizable, so this sequential test suffices. This argument does not infer ambient continuity of the vector field from stratumwise smoothness.

Uniqueness on each stratum gives the group law and the translated maximal intervals

\[
J_{\alpha(s,x)}=J_x-s,\qquad
\alpha(-s,\alpha(s,x))=x.
\tag{CF5}
\]

Since \(J\) is open and \(\alpha\) is continuous, the fixed-time maps and these inverses are homeomorphisms of their open domains. The union of the maximal stratumwise domains is the domain just proved open; replacing that union by an intersection would be incorrect. Restrictions to smaller time-space neighborhoods are local flows as well, but the maximal flow is the one specified here. \(\square\)

<a id="SH02-PRP-STRATIFIED-PRODUCT"></a>
<a id="sh02-prp-stratified-product--the-actual-local-product-for-a-real-valued-lift"></a>

### The actual local product for a real-valued lift

Let \(f:V\to\mathbb R\) be continuous, smooth on each stratum, and let the supplied controlled field satisfy \(df(\eta_T)=1\) on each stratum. Subtract \(f(x)\) so that \(f(x)=0\). Along every trajectory,

\[
f(\alpha(t,y))=f(y)+t.
\tag{CF6}
\]

By openness of \(J\), choose \(\epsilon>0\) and an open neighborhood \(W\) of \(x\) with \((-2\epsilon,2\epsilon)\times W\subset J\). Put \(P=W\cap f^{-1}(0)\) and \(I=(-\epsilon,\epsilon)\). The map \(\Phi:P\times I\to V\), \(\Phi(p,t)=\alpha(t,p)\), has an open image. To verify that point rather than assume it, define

\[
\begin{aligned}
D&=\{y\in V:(-f(y),y)\in J\},&
g(y)&=\alpha(-f(y),y),\\
\Omega&=D\cap f^{-1}(I)\cap g^{-1}(P),&
\Phi^{-1}(y)&=(g(y),f(y)).
\end{aligned}
\tag{CF7}
\]

The map \(y\mapsto(-f(y),y)\) is continuous, so \(D\) is open. The function \(g:D\to f^{-1}(0)\) is continuous by the flow theorem and (CF6). The set \(P\) is relatively open in the fibre, so \(\Omega\) is open in \(V\). For \(y\in\Omega\), the positive or negative flow from \(g(y)\in P\subset W\) exists for time \(f(y)\in I\), and (CF5) gives \(\Phi(g(y),f(y))=y\). Conversely, for \(y=\Phi(p,t)\), (CF6) gives \(f(y)=t\) and (CF5) gives \(g(y)=p\), so \(y\in\Omega\). Thus (CF7) is the actual continuous inverse, and \(\Phi\) is a stratum-preserving homeomorphism. In particular each original stratum meets this product as \((T\cap P)\times I\). There is no properness hypothesis on \(f\) and no global product claim.

The smooth-ODE existence, uniqueness and dependence theorem, ordinary tubular neighborhoods and the displayed control data are the inputs of this proof. Mather’s *Notes on Topological Stability*, [Lemma 7.3 (typeset page 16)](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf#page=16) and [Proposition 10.1 (manuscript printed 53–56, PDF 133–136)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/matherj.pdf#page=133), are mathematical antecedents. The present argument spells out compact closed tubes, finite-endpoint trapping and continuity, with independently written exposition and calculations dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). No licence to adapt the manuscript's text is asserted. The [compatible-tube construction](#SH02-PRP-COMPATIBLE-TUBES) below supplies these data for a smooth ambient map submersive on each stratum, relative to explicit ordinary differential-topology inputs. The [lift construction](#SH02-PRP-CONTROLLED-LIFT) below supplies a controlled field once those data are given; neither the radius-rank lemma nor the conditional flow theorem constructs the data.

<a id="SH02-PRP-CONTROLLED-LIFT"></a>
<a id="sh02-prp-controlled-lift--lifting-a-field-after-control-data-are-given"></a>

## Lifting a field after control data are given

Keep the closed finite-dimensional Whitney-stratified space above. Suppose compatible smooth tubular control data are already given, with the rank property (WT1) on every incident upper stratum. Let \(f:V\to P\) be continuous and smooth and submersive on each stratum, where \(P\) is a smooth manifold. Assume that, near each lower stratum \(R\), the given data satisfy

\[
f=f\circ\pi_R.
\tag{CL1}
\]

For every smooth vector field \(\zeta\) on \(P\), there is a smooth stratumwise field \(\eta\) with \(df(\eta)=\zeta\circ f\) satisfying (CF1) on an open neighborhood of each lower stratum, common to all its incident upper strata. The field itself need not be continuous across strata. The proof must preserve the control identities when local fields are averaged.

**A neighborhood lemma.** Given open neighborhoods \(A_R\) inside the supplied tubes, shrink them so they meet only \(R\) and its incident upper strata. There are a locally finite family of open neighborhoods \(C_R\) and closed neighborhoods \(B_R\) of \(R\) such that

\[
\begin{gathered}
R\subset\operatorname{int}_V B_R\subset B_R\subset C_R\subset A_R,
\qquad B_R\text{ is closed in }V\setminus\partial R,\\
C_R\cap C_S=\varnothing\quad\text{if }R,S\text{ are incomparable},\\
\pi_S(C_S\cap B_R)\subset A_R\quad\text{if }R<S.
\end{gathered}
\tag{CL2}
\]

Here \(\partial R=\overline R\setminus R\) is closed. Local closedness of a stratum makes \(R\) closed in \(V\setminus\partial R\), and the frontier rule gives \(\partial R\subset\partial S\) for \(R<S\).

To prove the lemma, first enlarge the locally finite closed family \(\{\overline R\}\) to a locally finite open family \(\{H_R\}\). One direct construction is to cover \(V\) by open sets meeting only finitely many closures, take a locally finite refinement, and let \(H_R\) be the union of refinement sets that meet \(\overline R\). Each refinement set is assigned to only finitely many strata, so the resulting family is locally finite. Metrizability gives the required locally finite refinement.

In a compatible metric \(d\), let \(D_R\) be the union of the closures of strata incomparable with \(R\). This is closed by local finiteness, and disjoint from \(R\) by the frontier rule. Put \(\delta_R(z)=\min(1,d(z,D_R))\), taking \(\delta_R=1\) if \(D_R\) is empty. The open neighborhood

\[
N_R=\{z:d(z,\overline R)<\delta_R(z)/3\}
\tag{CL3}
\]

contains \(R\). If \(R,S\) are incomparable, membership in both \(N_R\) and \(N_S\) would give \(d(z,\overline R)<d(z,\overline S)/3\) and the reverse inequality, which is impossible.

Construct \(C_S,B_S\) in increasing stratum dimension. Previously chosen \(B_R\) with \(R<S\) are closed in \(V\setminus\partial S\), because \(\partial R\subset\partial S\). On this open space, intersect \(A_S\cap H_S\cap N_S\) with

\((V\setminus B_R)\cup\pi_S^{-1}(A_R)\) for every \(R<S\).

The intersection is open: locally only finitely many \(B_R\) occur, and every other condition is automatic. It contains \(S\), since \(s\in S\cap B_R\) implies \(s\in A_R\) and \(\pi_S(s)=s\). Call this intersection \(C_S\). Normality of \(V\setminus\partial S\) now gives a closed neighborhood \(B_S\) of its closed subset \(S\) contained in \(C_S\). This proves (CL2), including the open room \(C_S\) around \(B_S\). No smooth partition has yet been taken.

**Induction over the skeleton.** Suppose fields have been chosen on all strata of dimension at most \(k\), with the lift and control identities. Their union is a closed skeleton: the frontier rule and local finiteness retain all lower boundary strata. For each such \(R\), choose an open \(A_R\) on which its control identities with all already treated higher strata hold, and on which (CL1) holds. Relative open neighborhoods on the skeleton extend to open neighborhoods in \(V\). Apply the lemma once to this family, before constructing fields on any stratum of dimension \(k+1\).

Fix one such stratum \(X\) and \(v\in X\). The active lower strata \(R\) with \(v\in B_R\) form a finite chain by (CL2). Moreover \(B_R\cap X\) is closed in \(X\): the higher-dimensional \(X\) misses \(\partial R\). Local finiteness and closedness therefore give a neighborhood of \(v\) in \(X\) meeting no inactive \(B_R\).

If the active chain is nonempty, let \(Y\) be its largest member and take this neighborhood inside \(C_Y\cap X\). The submersion \((\pi_Y,\rho_Y)|_X\) has a smooth local right inverse for its differential; a smooth bundle metric supplies one by the adjoint and the inverse of the resulting positive definite operator. Thus choose a local field \(w\) with

\[
d\pi_Y(w)=\eta_Y\circ\pi_Y,\qquad d\rho_Y(w)=0.
\tag{CL4}
\]

For any other active \(R<Y\) at a nearby point in \(B_R\), (CL2) puts \(\pi_Y(v)\) in \(A_R\). The supplied tube identities \(\pi_R\pi_Y=\pi_R\), \(\rho_R\pi_Y=\rho_R\) are therefore defined on a neighborhood of that point. Differentiating them and using the already controlled field on \(Y\) gives

\[
\begin{aligned}
d\rho_R(w)&=d\rho_R(\eta_Y)\circ\pi_Y=0,\\
d\pi_R(w)&=d\pi_R(\eta_Y)\circ\pi_Y
=\eta_R\circ\pi_R,\\
df(w)&=df(\eta_Y)\circ\pi_Y=\zeta\circ f.
\end{aligned}
\tag{CL5}
\]

The final line uses (CL1) on \(C_Y\). These equalities apply to every active constraint on the local neighborhood, even when \(Y\) ceases to be active at a nearby point: that point is still in \(C_Y\). No new active lower stratum can enter, by the neighborhood choice. If the active chain at \(v\) is empty, instead use an ordinary local lift through the submersion \(f|_X\), on a neighborhood avoiding all \(B_R\).

These neighborhoods cover \(X\). Choose a smooth locally finite partition of unity \(\{\psi_i\}\) subordinate to them, with corresponding local fields \(w_i\), and set

\[
\eta_X=\sum_i\psi_iw_i,\qquad \sum_i\psi_i=1.
\tag{CL6}
\]

At a point in \(B_R\cap X\), every contributing field satisfies the same affine equations \(d\rho_R(w_i)=0\), \(d\pi_R(w_i)=\eta_R\circ\pi_R\) and \(df(w_i)=\zeta\circ f\). Equation (CL6) preserves them because the differentials are linear at that point and the weights sum to one. Derivatives of the weights do not occur when a differential is applied to the value of a vector field. The new field is therefore controlled on the open neighborhood \(\operatorname{int}_V B_R\). The same family works for every new stratum \(X\), so this is one neighborhood per lower stratum rather than separate neighborhoods for each pair.

Starting with the ordinary lifts on the lowest-dimensional strata and repeating finitely many dimension steps completes the construction. Later shrinkings preserve the earlier identities. For \(P=\mathbb R\) and \(\zeta=1\), this supplies the field used in (CF6); the preceding flow and product proofs then apply. No properness hypothesis or compactness of a stratum is used. \(\square\)

[Mather, *Notes on Topological Stability*, Proposition 9.1, manuscript printed 46–50 / PDF 126–130](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/matherj.pdf#page=127), is the mathematical antecedent. This independent proof makes the neighborhood shrinking, closed active constraints and affine averaging explicit; its new exposition and calculations are dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The [compatible-tube construction](#SH02-PRP-COMPATIBLE-TUBES) below supplies those data for a smooth ambient map submersive on each stratum. Its ordinary differential-topology inputs are proved in the smooth foundations below.

<a id="SH02-PRP-COMPATIBLE-TUBES"></a>
<a id="sh02-prp-compatible-tubes--constructing-compatible-whitney-tubes"></a>

## Constructing compatible Whitney tubes

Let \(V\) be closed in a finite-dimensional smooth manifold \(M\), with a locally finite smooth Whitney $(a,b)$ stratification satisfying the frontier rule. Let \(f:M\to P\) be smooth and submersive on **every stratum**. Then there are smooth tubular data \((\mathcal T_S,\pi_S,\rho_S)\) such that

\[
f\pi_S=f,\qquad
\pi_R\pi_S=\pi_R,\qquad \rho_R\pi_S=\rho_R\quad(R<S),
\tag{CTU1}
\]

where the last two identities are required wherever both sides are defined. The tubes can be shrunk to a locally finite family, to exclude nonincident strata, and to satisfy (WT1). The ambient map need only be a submersion near \(V\): its stratumwise submersivity already gives this after restriction to an open neighborhood. Properness of \(f\) is unnecessary.

The construction below uses the inverse function theorem, ordinary smooth ODE existence and dependence, smooth bundle metrics and connections, and smooth partitions of unity on manifolds. These are explicit ordinary differential-topology inputs. It constructs the compatible tubes directly; no relative tube-isotopy extension theorem is assumed.

### Shrinking a local normal map to an actual tube

Here is the needed injectivity lemma. Suppose \(X\) is a closed embedded submanifold of \(M\), \(E\to X\) is a smooth inner-product bundle, and \(F\) is defined on a neighborhood of its zero section, with \(F(x,0)=x\) and invertible differential there. Then a positive smooth radius \(\epsilon(x)\) makes \(F:B_\epsilon E\to M\) a diffeomorphism onto an open neighborhood of \(X\).

For the proof take a locally finite ambient cover \(\{O_i\}\) near \(X\), whose closures over \(X\) are compact and lie in inverse-function charts for \(F\), and add \(M\setminus X\) to cover \(M\). For each \(O_i\) choose \(a_i>0\) such that the entire bundle region over \(X\cap O_i\) of radius \(a_i\) lies in its one injectivity chart. Compactness of its zero-section base supplies that radius. In a compatible Riemannian distance, let \(r>0\) be a Lipschitz function with Lipschitz constant at most one and such that every \(B_{3r(x)}(x)\), for \(x\in X\), lies in some \(O_i\). Explicitly, one eighth of the supremum of \(\min(1,d(z,M\setminus O))\) over the ambient cover is positive, Lipschitz and has this property. An empty complement is assigned capped distance one.

Choose \(\epsilon\) small enough that \(F\) is defined and a local diffeomorphism on \(B_\epsilon E\), that \(\epsilon(x)<a_i\) whenever \(x\in O_i\), and that \(d(F(x,v),x)<r(x)/8\). The last condition is open around the zero section by continuity. Local finiteness and a smooth partition of unity give a positive smooth minorant satisfying all these restrictions. If \(F(x,v)=F(y,w)\), then

\[
d(x,y)<\frac{r(x)+r(y)}8
\le\frac{2r(x)+d(x,y)}8,
\qquad d(x,y)<\frac{2r(x)}7.
\tag{CTU2}
\]

Thus \(x,y\) lie in one \(O_i\), and both vectors lie in its same injectivity chart. They are equal. An injective local diffeomorphism has smooth inverse on its open image, proving the lemma. For a locally closed \(X\), first restrict the ambient manifold to \(M\setminus\partial X\), in which \(X\) is closed, and keep the image there by shrinking.

This also proves the ordinary tube theorem needed below. Choose a smooth Riemannian metric on \(M\), let \(E=(TX)^\perp\) over \(X\), and use the normal exponential map. The geodesic ODE gives a smooth map near the zero section whose differential there is \((a,v)\mapsto a+v\), an isomorphism. Apply the injectivity lemma. Consequently the following argument has no unproved ordinary-tube existence step beyond the stated calculus, ODE and metric inputs.

### A normal motion preserving the existing lower controls

Construct the data in increasing stratum dimension. Suppose data on the closed skeleton of dimensions less than \(k\) have already been made mutually compatible and compatible with \(f\). Shrink their tubes using (WT1) so \(q_R=(\pi_R,\rho_R)\) is submersive on every incident upper stratum. Local finiteness makes the simultaneous rank shrinking possible at each lower point.

Apply the proof of (CL2) in the ambient manifold to these lower strata. That proof uses only their locally finite closed closures, their frontier rule, their retractions and metric normality; it does not require them to partition the ambient space. Closedness of \(V\) makes their closure family locally finite in \(M\) as well. Obtain locally finite \(B_R\subset C_R\subset A_R\subset\mathcal T_R\), with \(B_R\) closed in \(M\setminus\partial R\), open room \(C_R\), no incomparable overlaps, and

\[
\pi_Y(C_Y\cap B_R)\subset A_R\quad(R<Y).
\tag{CTU3}
\]

Choose inner tubular restrictions \(I_R\) whose closures in \(M\setminus\partial R\) lie in \(\operatorname{int} B_R\). To do this first choose an open neighborhood of the closed subset \(R\) with closure inside \(\operatorname{int} B_R\), and then choose a positive smooth tube radius fitting inside it. This choice is made once for all strata of the new dimension.

Fix a new stratum \(X\) of dimension \(k\), and choose an ordinary tube \(\phi:E\supset U\to M\) for \(X\), with a metric connection on \(E\). At \(u\in E_x\), write \(b^H_u\) for the horizontal lift of \(b\in T_xX\) and \(v^V_u\) for the vertical vector corresponding to \(v\in E_x\). For a function or manifold map \(h\) on the image define \(d^Hh(b)=d(h\phi)(b^H)\) and \(d^Vh(v)=d(h\phi)(v^V)\).

Restrict \(U\) to an open neighborhood of the zero section whose image misses the old skeleton. On it \(d^Hf\) is surjective; whenever \(\phi(u)\in B_R\), also require \(d^Hq_R\) to be surjective. These are possible open restrictions: at the zero section they are respectively the submersion of \(f|_X\) and (WT1). Each \(B_R\) is closed off the old skeleton, and the family is locally finite, so inactive constraints can be excluded locally.

At a point \(u\), the active \(R\) with \(\phi(u)\in B_R\) form a finite chain. On a small neighborhood exclude every inactive \(B_R\). If the chain has largest member \(Y\), keep that neighborhood inside \(\phi^{-1}(C_Y)\) and use a smooth right inverse \(L_Y\) of \(d^Hq_Y\) to choose the base correction

\[
b_Y(u,v)=-L_Y(u)\,d^Vq_Y(v),\qquad
 d(q_Y\phi)(b_Y^H+v^V)=0.
\tag{CTU4}
\]

For every other active \(R<Y\), (CTU3) ensures that the old identities \(q_R=q_R\pi_Y\) are actually defined near the point. Hence \(q_R\) factors there through the \(\pi_Y\) component of \(q_Y\). Also \(f=f\pi_Y\). Thus the same corrected motion annihilates all these maps. If there is no active lower stratum, instead use a right inverse of \(d^Hf\) and set \(b_f=-L_f d^Vf(v)\).

A smooth locally finite partition of unity on \(U\) averages these local corrections. As in (CL6), every contributing correction satisfies the same active linear equations, now with the fixed inhomogeneous term \(d^Vh(v)\). The weights sum to one, so the average \(b(u,v)\), smooth and linear in \(v\), satisfies

\[
d(f\phi)(b^H+v^V)=0,\qquad
 d(q_R\phi)(b^H+v^V)=0\quad\text{on }\phi^{-1}(B_R).
\tag{CTU5}
\]

If the initially highest active constraint drops nearby, the local correction is still defined in the larger \(C_Y\); no previously inactive constraint can enter its local patch. This is why the closed constraint neighborhoods and their open room were chosen before taking the partition.

### The actual tubular chart and the commutation identities

On \(E\oplus E\) solve the smooth ODE

\[
\dot x=b(u,v),\qquad
\nabla_t u=v,\qquad \nabla_t v=0,
\qquad (x(0),u(0),v(0))=(x,0,v_0).
\tag{CTU6}
\]

The first equation and the connection define the horizontal parts of the last two equations, so this is an ordinary smooth vector field on the indicated bundle. At \(v_0=0\) its trajectory is constant. Smooth ODE dependence gives existence for \(0\le t\le1\) on an open neighborhood of all such initial states; shrink the starting radius so the trajectory remains in \(U\). Define \(F_X(x,v_0)=\phi(u(1))\). Equation (CTU5) gives \(fF_X(x,v_0)=f(x)\).

Linearizing (CTU6) at \((x,0,0)\) gives \(\delta v(t)=v_0\), \(\delta u(t)=t v_0\), and \(\delta x(t)=t b(0_x,v_0)\). Connection terms are quadratic in the varied normal variables there. Consequently the normal-quotient component of \(dF_X(v_0)\) is exactly \(v_0\); together with \(F_X(x,0)=x\) this makes the full differential invertible. The injectivity lemma supplies an actual tubular chart, with \(\pi_X(F_X(x,v_0))=x\) and \(\rho_X(F_X(x,v_0))=|v_0|^2\).

For each old \(R\), keep every trajectory starting at \(x\in X\cap I_R\) inside \(\operatorname{int} B_R\). This is a legitimate radius restriction. The closure of \(I_R\) along \(X\) is contained in that open set because \(X\) misses \(\partial R\). At \(v_0=0\) the whole unit-time trajectory is the fixed \(x\); compact-time ODE dependence gives a radius bound near every point of that closure. Away from it the constraint is absent locally. Only finitely many old neighborhoods occur locally, so a positive smooth minorant meets all these bounds simultaneously. Along the resulting trajectory (CTU5) then gives

\[
q_R(F_X(x,v_0))=q_R(x)\quad(x\in X\cap I_R).
\tag{CTU7}
\]

Replace the old tube domains by their fixed inner restrictions \(I_R\). Whenever \(m\in\mathcal T_X\cap I_R\) and \(\pi_X(m)\in I_R\), (CTU7) is precisely both old-new identities in (CTU1). Old-old identities survive restriction. The same \(I_R\) works for every \(X\) of dimension \(k\); their individual starting radii need not agree. There are no control identities between distinct strata of the same dimension.

Finally shrink each new tube into a locally finite open expansion of its stratum closure and away from nonincident strata. Such expansions exist by the construction preceding (CL3); the excluded closures miss the base stratum by the frontier rule. These restrictions preserve all established identities. Repeating the dimension step finitely many times constructs the whole family. Applying (WT1) again after later restrictions retains the rank property. There is no infinite sequence of global shrinkings at a fixed lower point. \(\square\)

For a smooth ambient real function submersive on the strata, this construction, the [controlled-lift proof](#SH02-PRP-CONTROLLED-LIFT), the [continuous-flow proof](#SH02-PRP-CONTROLLED-FLOW), and the [actual local product](#SH02-PRP-STRATIFIED-PRODUCT) now supply the complete geometric argument relative to the explicitly stated ordinary differential-topology inputs.

The mathematical antecedent is [Mather, *Notes on Topological Stability*, Proposition 7.1, manuscript printed 33–40 / PDF 113–120](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/matherj.pdf#page=113). Its original handwritten qualifier requires submersion on each stratum. Its proof uses relative tube extension; the direct normal-motion proof above states its own inputs instead. The new independent exposition and calculations are dedicated to [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); no licence to adapt manuscript prose is asserted.

<a id="SH02-PRP-SMOOTH-CONTROL"></a>
<a id="sh02-prp-smooth-control--smooth-foundations-for-the-control-construction"></a>

## Smooth foundations for the control construction

This supplies the ordinary manifold inputs used in the [compatible-tube construction](#SH02-PRP-COMPATIBLE-TUBES), the [controlled lift](#SH02-PRP-CONTROLLED-LIFT), and their [local flow](#SH02-PRP-CONTROLLED-FLOW). The manifolds here are finite dimensional, Hausdorff, smooth and second countable, without boundary. Countability at infinity also gives second countability: cover each compact member of a countable exhaustion by finitely many charts and take their countable coordinate bases. Vector bundles have finite rank. The elementary starting facts are completeness of the real numbers, compactness of closed bounded Euclidean sets, elementary linear algebra, and Euclidean differentiation and integration with the chain rule and Taylor remainder. No inverse-function, ODE, partition-of-unity or tubular-neighborhood theorem is assumed below.

### Contractions and local inverses

In a complete normed space let a map \(T\) send a nonempty closed ball into itself and have Lipschitz constant \(0\leq q<1\). Starting at any point of the ball and iterating gives

\[
\|u_{j+1}-u_j\|\leq q^j\|u_1-u_0\|,
\qquad
\|u_{j+m}-u_j\|\leq\frac{q^j}{1-q}\|u_1-u_0\|.
\tag{SCF1}
\]

The iterates are Cauchy, their limit remains in the ball, and continuity makes that limit a fixed point. Two fixed points have distance at most \(q\) times their own distance, so coincide. For the space of continuous functions on a compact interval with the supremum norm, completeness follows directly: a norm-Cauchy sequence has pointwise limits in Euclidean space, the same Cauchy bound implies uniform convergence, and an epsilon-over-three argument proves continuity of the limit.

We also need smooth dependence of this fixed point, without importing an implicit-function theorem. Suppose \(T(u,p)\) is smooth on an open neighborhood of the ball and a finite-dimensional parameter neighborhood, maps the ball into itself with the same contraction constant, and its fixed points lie in the interior. Smoothness in a normed function space means differentiability with a remainder small in norm; the concrete operator needed below is checked explicitly. Write the fixed point as \(u(p)\). Comparing the two fixed-point equations first proves continuity and then a local Lipschitz bound:

\[
\|u(p+h)-u(p)\|
\leq\frac{\|T(u(p),p+h)-T(u(p),p)\|}{1-q},
\qquad
D_pu=(I-D_uT)^{-1}D_pT.
\tag{SCF2}
\]

For the derivative formula, put \(\Delta u=u(p+h)-u(p)\). The first inequality and a bound on the parameter derivative near the fixed point give \(\Delta u=O(|h|)\). Taylor's formula for the joint variables then gives
\((I-D_uT)\Delta u=D_pT\,h+o(|h|)\).
The inverse is the norm-convergent series \(\sum_{j\geq0}(D_uT)^j\), of norm at most \((1-q)^{-1}\). Thus the derivative exists and is continuous. Inversion of invertible bounded operators is itself smooth: near \(A\) expand \((A+H)^{-1}\) by the geometric series in \(A^{-1}H\); its first derivative is \(-A^{-1}HA^{-1}\), and repeated differentiation gives continuous multilinear derivatives. The displayed derivative formula therefore upgrades \(u\) from \(C^1\) to \(C^2\), and inductively to every finite differentiability order.

Now let \(f\) be smooth between open subsets of \(\mathbb R^n\) and let \(A=Df(x_0)\) be invertible. On a sufficiently small closed ball of radius \(r\) about \(x_0\), continuity gives \(\|I-A^{-1}Df(x)\|\leq1/2\). For \(y\) near \(f(x_0)\) set

\[
T_y(x)=x-A^{-1}(f(x)-y),
\qquad
\|A^{-1}(y-f(x_0))\|<r/4.
\tag{SCF3}
\]

The mean-value integral along a segment gives contraction constant \(1/2\), and the image lies in the ball of radius \(3r/4\). Its interior fixed point solves \(f(x)=y\) and depends smoothly on \(y\) by SCF2. The same segment estimate proves injectivity of \(f\) on the original ball: if \(f(x)=f(z)\), then \(x-z=T_y(x)-T_y(z)\). Restrict the open ball to the inverse image of the chosen open \(y\)-neighborhood. This gives an actual diffeomorphism, with inverse derivative \(Df(x)^{-1}\). Charts transfer this result to manifolds.

### Smooth ODEs and compact time intervals

Let \(F(t,z,\lambda)\) be smooth on an open Euclidean domain, where \(\lambda\) is a finite-dimensional parameter. Choose a compact product box inside the domain about \((0,z_0,\lambda_0)\), using a closed \(z\)-ball of radius \(r\), with room to enlarge that ball. On the box let \(K\) bound \(|F|\) and \(L\) bound \(\|D_zF\|\). Choose \(h>0\) within the time box so that \(hK<r/2\) and \(hL<1/2\), and take \(|p-z_0|<r/4\). On the closed ball \(\|z-z_0\|_\infty\leq r\) in \(C([-h,h],\mathbb R^n)\) define

\[
(\Theta_{p,\lambda}z)(t)
=p+\int_0^t F(s,z(s),\lambda)\,ds,
\qquad
\|\Theta z-\Theta w\|_\infty\leq hL\|z-w\|_\infty.
\tag{SCF4}
\]

The image has distance less than \(3r/4\) from the constant function \(z_0\), so SCF1 gives a unique fixed point. The fundamental theorem of calculus identifies it with a solution of \(\dot z=F(t,z,\lambda)\) and \(z(0)=p\). Any other local solution enters this same ball on a shorter interval; contraction uniqueness there, followed by restarting at an equality point, proves local uniqueness wherever two solutions overlap.

Here the function-space smoothness used in SCF2 can be verified, rather than assumed. The pointwise substitution followed by integration has derivatives

\[
\bigl(D_z^m\Theta[z](v_1,\ldots,v_m)\bigr)(t)
=\int_0^t D_z^mF(s,z(s),\lambda)
       [v_1(s),\ldots,v_m(s)]\,ds
\quad(m\geq1).
\tag{SCF5}
\]

Mixed parameter derivatives have the same form, and the initial-value derivative adds the constant function. All the finite-dimensional derivatives are bounded and uniformly continuous on a slightly larger compact box. Taylor remainders there, integrated over an interval of length at most \(h\), tend to zero in the supremum norm with the required order. This proves all the asserted continuous multilinear derivatives. SCF2 gives smooth dependence on \((p,\lambda)\) with values in the continuous-function space. Evaluation at a fixed time preserves these derivatives and their continuity. The integral equation then gives \(\partial_tz=F(t,z,\lambda)\); differentiation in parameters and repeated differentiation in time prove joint smoothness, including every mixed derivative. This argument does not assume that evaluation at a variable time is smooth on the whole continuous-function space.

Initial time is included by replacing \(F(t,z,\lambda)\) with \(F(s+t,z,\lambda)\) and treating \(s\) as another parameter. In particular the derivatives of the solution are justified before writing the variational equation. For a direction \((a,b)\) in initial value and parameter, they satisfy

\[
\dot Z(t)=D_zF(t,z(t),\lambda)Z(t)
          +D_\lambda F(t,z(t),\lambda)b,
\qquad Z(0)=a.
\tag{SCF6}
\]

The same local proof works in charts, and uniqueness identifies the chart solutions. A given solution on a compact time interval has compact graph. Cover that graph by finitely many of the local solution boxes just constructed and subdivide time finely enough that each successive piece stays in an appropriate box. Starting near its initial point, the finitely many smooth solution maps compose; shrink the initial neighborhood successively to keep each endpoint in the next box. This proves that nearby solutions exist on the whole interval and depend smoothly there. The finite subdivision is justified by pulling the boxes back to an open cover of the compact time interval and taking a Lebesgue number. Because the original solution has local continuations at the two endpoints, the conclusion holds on a slightly larger interval too. Thus the domain of the maximal local solution is open in time, initial value, initial time and parameter; maximal solutions are the union of their compatible local solutions.

This also gives the compact nonescape criterion used for a smooth stratum. If a solution at a finite right endpoint has a subsequence converging to an interior point of the equation's domain, select a relatively compact chart ball there and a smaller concentric ball. A bound \(K\) for the vector field implies that traversing their fixed radial gap takes at least that gap divided by \(K\) (with the zero-field case immediate). For subsequence times sufficiently close to the endpoint, the solution cannot exit the larger ball before that endpoint. Its speed is then bounded, so it has a limit there. Solve at that endpoint and limit, and glue by uniqueness. For a solution confined in a compact subset of the domain, such a convergent subsequence exists. No global completeness assertion is needed.

### Partitions, variable radii and locally finite neighborhoods

A second-countable manifold has a countable cover by precompact coordinate balls. To see the countable-subcover step directly, for each member of a countable basis contained in some member of an open cover choose one such cover member; these choices cover the space. Starting with the precompact balls, form successive finite unions of their closures, choosing each next union large enough to contain the previous compact union in the union of the corresponding open balls and to include the next enumerated ball. This gives compact sets \(K_j\subset\operatorname{int}K_{j+1}\) whose interiors cover the manifold. Set \(K_j=\varnothing\) for \(j\leq0\).

Given any open cover, cover each compact band \(K_j\setminus\operatorname{int}K_{j-1}\) by finitely many inner coordinate balls, with larger coordinate balls whose closures lie both in an assigned cover member and in \(\operatorname{int}K_{j+1}\setminus K_{j-2}\). Such choices exist because the band lies in that open shell. All these inner balls cover the manifold. The family of larger closed balls is locally finite: a neighborhood inside \(\operatorname{int}K_N\) misses every shell with \(j\geq N+2\), and only finitely many balls came from each remaining band.

In each larger ball choose a nonnegative smooth bump positive on its inner ball and supported in a still smaller closed ball inside the larger one. For example in coordinates use \(b(\rho^2-|x|^2)\), where \(b(t)=e^{-1/t^2}\) for \(t>0\) and \(b(t)=0\) for \(t\leq0\). Every derivative for positive \(t\) is a polynomial in \(1/t\) times the exponential, tending to zero at the boundary; extension by zero is therefore smooth. Extending the coordinate bumps to the manifold gives functions \(b_i\) with locally finite supports and positive sum. Consequently

\[
\theta_i=\frac{b_i}{\sum_j b_j},
\qquad
\theta_i\geq0,\quad \sum_i\theta_i=1,\quad
\operatorname{supp}\theta_i\subset U_i
\tag{SCF7}
\]

is a smooth partition subordinate to the assigned cover. The local finiteness is neighborhood finiteness, not merely finiteness at each point. This is the scope needed for differentiating sums of local lifts.

For any positive lower-semicontinuous function \(a\), choose local neighborhoods on which \(a>c_i>0\), and a partition subordinate to them. Then

\[
\varepsilon(x)=\tfrac12\sum_i\theta_i(x)c_i
\quad\hbox{satisfies}\quad 0<\varepsilon(x)<a(x).
\tag{SCF8}
\]

In particular an open neighborhood \(G\) of the zero section of a metrized finite-rank bundle contains a variable-radius disk neighborhood. Define
\(a(x)=\sup\{0<r\leq1:\{v\in E_x:|v|\leq r\}\subset G\}\).
It is positive. If \(a(x)>c\), choose a larger admissible radius; compactness of that fiber disk and a local trivialization show that slightly smaller disks remain in \(G\) over a neighborhood of \(x\). Hence \(a\) is lower semicontinuous. SCF8 supplies a smooth positive radius with its closed fiber disk in \(G\). Finitely many open requirements can first be intersected. For a locally finite family of requirements imposed over closed base sets, their implications define an open neighborhood of the zero section: locally only finitely many closed sets occur, and failure of one implication is closed locally. Apply the same radius argument to that neighborhood. This explains the variable shrinkings in the tube proof without a uniform radius.

### Bundle metrics, connections and right inverses

On a finite-rank real bundle, use local frames to put Euclidean metrics \(h_i\) on each trivialization and set \(h=\sum_i\theta_i h_i\). At every base point at least one weight is positive, so \(h\) is a positive definite smooth bundle metric. Likewise the local frame connections give a connection \(D=\sum_i\theta_iD_i\). The sum extends smoothly because each support lies inside its frame domain. Its Leibniz rule follows from \(\sum_i\theta_i=1\); differentiating the weights is not part of this definition.

To make the connection metric compatible define the endomorphism-valued one-form \(A\) by

\[
h(A_Xs,t)=\tfrac12(D_Xh)(s,t),\qquad
\nabla_Xs=D_Xs+A_Xs,\qquad \nabla h=0.
\tag{SCF9}
\]

Here \((D_Xh)(s,t)=X(h(s,t))-h(D_Xs,t)-h(s,D_Xt)\) is a smooth symmetric tensor in \(s,t\). Nondegeneracy of \(h\) determines \(A\), and substituting the formula subtracts two halves of that tensor, proving the last identity.

If a smooth bundle map \(B:E\to F\) is surjective, the metrics define its adjoint and the smooth right inverse

\[
L=B^*(BB^*)^{-1},\qquad BL=I_F.
\tag{SCF10}
\]

Indeed \(\langle BB^*w,w\rangle=|B^*w|^2\) is positive for nonzero \(w\): surjectivity of \(B\) makes \(B^*\) injective. In a local frame its inverse is smooth by the determinant formula. This proves the right-inverse construction used in the affine lifting and horizontal correction equations.

### Metrics, closed-set shrinkings and ordinary tubes

Apply the bundle metric construction to the tangent bundle. Its Riemannian length distance \(d_g\) on each connected component is finite because a connected manifold is path connected by piecewise coordinate paths. It is positive off the diagonal and induces the given topology. For the local check, on a precompact coordinate ball the metric is bounded above and below by positive constants times the Euclidean metric. Straight segments give the upper distance bound near its center; any path exiting a smaller concentric ball has length at least the lower constant times its radial gap, and paths staying in the chart satisfy the Euclidean lower bound. This proves both positivity and the neighborhood comparison. A bounded compatible metric on the whole manifold is

\[
d(x,y)=
\begin{cases}
\min\{1,d_g(x,y)\},&x,y\text{ in the same component},\\
2,&x,y\text{ in different components}.
\end{cases}
\tag{SCF11}
\]

The triangle inequality follows from that for length and the truncation inequality; a triangle crossing components has two sides equal to \(2\). For a closed set \(F\) in an open set \(G\), distances give the shrinking
\(H=\{x:d(x,F)<\tfrac12d(x,M\setminus G)\}\).
It contains \(F\) and its closure lies in \(G\). At a point outside \(G\) the second distance is zero and the first is positive, because \(F\) is closed. Empty sets are handled by taking \(H=\varnothing\) or \(H=M\) as appropriate. Thus the required normality and closed-neighborhood shrinkings follow from this explicit metric.

For a locally finite family of closed sets \(F_i\), use the locally finite precompact ball cover above. Each closed ball meets only finitely many \(F_i\), by compactness and local finiteness. Let \(H_i\) be the union of the open balls meeting \(F_i\). It contains \(F_i\); the family of closures \(\overline H_i\) is locally finite, since locally only finitely many closed balls occur and each meets finitely many indices. Intersect with any assigned open neighborhood of \(F_i\), then apply the preceding metric shrinking to obtain open expansions whose closures remain inside those assigned neighborhoods and remain locally finite. All these arguments also apply in an open manifold obtained by deleting a frontier.

For completeness, the ordinary normal exponential used in the tube construction has the required differential without assuming a tube theorem. Given the tangent metric, define its torsion-free metric connection by the Koszul identity
\(2g(\nabla_XY,Z)=Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)-g(X,[Y,Z])+g(Y,[Z,X])+g(Z,[X,Y])\).
Expanding brackets and derivatives proves linearity in \(X,Z\) and the Leibniz rule in \(Y\); nondegeneracy defines the connection intrinsically. In coordinates its coefficients and geodesic equation are

\[
\Gamma^i_{jk}
=\tfrac12g^{i\ell}
(\partial_jg_{k\ell}+\partial_kg_{j\ell}-\partial_\ell g_{jk}),
\qquad
\dot q^i=v^i,\quad
\dot v^i=-\Gamma^i_{jk}(q)v^jv^k.
\tag{SCF12}
\]

Repeated indices are summed. SCF4–6 give a smooth local solution. At initial velocity zero it is the constant solution, defined throughout \([0,1]\); compact-time openness gives a neighborhood of each zero initial vector on which the time-one endpoint \(\exp_x(v)\) is defined smoothly. These neighborhoods together form an open neighborhood of the zero section, and SCF8 gives a positive variable radius inside it. At zero velocity the quadratic term in SCF12 has zero linearization. For initial variation \((a,w)\) the linearized solution is \(\delta v(t)=w\), \(\delta q(t)=a+tw\), so
\(d\exp_{(x,0)}(a,w)=a+w\).

For an embedded submanifold \(X\), take the normal bundle as the metric orthogonal complement of \(TX\). The restricted exponential fixes \(X\) and has invertible zero-section differential, since \(TX\oplus(TX)^\perp=TM|_X\). SCF3 supplies its local inverses. The [injective-radius lemma](#SH02-PRP-COMPATIBLE-TUBES) then produces a single variable-radius neighborhood on which it is an actual tube diffeomorphism; that lemma uses only these local inverses, a compatible metric and a smooth positive minorant, all proved here. For locally closed \(X\), delete its frontier first, making it closed in an open manifold. No geodesic completeness or fixed global radius has been used.

The same constructions apply to the bundle system used in the compatible tube proof: its connection coefficients are smooth, and its zero-velocity trajectories are equilibria. SCF6 justifies its zero-section endpoint differential; SCF8 justifies the accumulated open radius restrictions. Together with the earlier Whitney rank, finite-chain lifting and controlled-flow arguments, these proofs discharge that route's ordinary smooth inputs relative to the elementary starting facts stated above. The deeper subanalytic and microsupport statements are separate inputs.

The partition antecedent is Holger Brenner's lecture 22, Lemmas 22.6 and 22.9 and Theorem 22.10, in [the programme D50 reader](https://kokunoyumeto.github.io/program-matematika-indonesia/backend/d50/reader/index.html#o011-brenner-u22-l22). Its [exact captured edition and licence](https://github.com/KokunoYumeto/program-matematika-indonesia/blob/06be492fda092e4341f6286b2a7b081aecaa5d1a/docs/backend/d50/LICENSE.md) retain CC BY-SA 4.0 for that source and its translation. Its compact-exhaustion proof gives the neighborhood local finiteness needed here; the smooth specialization and flat-boundary check are made explicit above. For the ordinary ODE antecedents see Gerald Teschl, [*Ordinary Differential Equations and Dynamical Systems*, Theorems 2.1, 2.2, 2.10, 2.11 and 2.13–2.16](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf#page=46), printed pages 35–38, 46–48 and 51–53. His preliminary edition has its own redistribution restrictions. This new section is an independently written proof of standard mathematical facts; it reproduces no source prose, source images or PDF, and is dedicated under [CC0](https://creativecommons.org/publicdomain/zero/1.0/). It makes no new-research or independent-review claim.

## Antecedents and reuse

The Stacks Project supplies the mathematical antecedents identified by exact tags in these proofs. The [cited edition in the official repository](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14) has a [license notice](https://raw.githubusercontent.com/stacks/stacks-project/a04446e57ec1fbc252a871afcec7752fb2807b14/introduction.tex) specifies GFDL-1.2-or-later with no invariant sections or cover texts. The exposition and calculations here are original. The original programme exposition is dedicated under CC0 1.0 Universal.
