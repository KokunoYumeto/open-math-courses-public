# SH02-PREREQ-PROOFS — Supporting verifications for open prerequisites

These proofs establish the elementary and coherence results specified in the prerequisite statements. They use the exact cited existence and localization theorems for derived categories and K-flat/K-injective resolutions. The proofs rely on those cited theorems and their prerequisites. Existence of unbounded operations does not establish preservation of bounded complexes.

The proof letters identify the results used below. E1–E8 concern ordinary sheaf operations, proper maps, the hypercohomology edge, and one projection/base-change diagram. DF-A–DF-F concern chain-Hom signs, ordinary derived internal Hom, and pullback coherence. These results do not construct nonproper direct image with proper support, exceptional inverse image, microlocal Hom, or course-specific kernel and trace diagrams.

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

Suppose now that $X,Y$ are locally compact Hausdorff and $f:X\to Y$ is continuous with compact inverse images of compact sets. Its fibres are compact. To prove that $f$ is closed, let $A\subset X$ be closed and choose $y\notin f(A)$. Choose a compact neighborhood $K$ of $y$ in $Y$. The set $A\cap f^{-1}K$ is compact, so its image $C$ is compact and closed in $Y$. The open neighborhood $\operatorname{Int}K\setminus C$ of $y$ is disjoint from $f(A)$. Thus $f(A)$ is closed. Tag 005R now gives universal closedness. Because $X$ is Hausdorff, its diagonal is closed in $X\times X$, and its intersection with $X\times_YX$ is closed there; hence $f$ is separated and proper in the Stacks sense.

Conversely, Tag 005R shows that a universally closed map takes inverse images of quasi-compact subsets to quasi-compact subsets. For Hausdorff $X$, those inverse images are compact. This proves the precise convention bridge used by the public proper-base-change contract. Compact fibres alone would not have supplied closedness.

## SH02-PRP-E4. The compact-neighborhood dimension-shifting step

The supporting [Tag 09V3](https://stacks.math.columbia.edu/tag/09V3) concerns a quasi-compact subset $Z\subset X$ whose distinct points have disjoint ambient open neighborhoods. Its proof establishes the degree-zero neighborhood comparison by finite gluing and proves that the restriction of an injective module sheaf to $Z$ is acyclic for sections on $Z$. The reduction from those assertions to all degrees is left implicit. Here is that reduction, with precisely those hypotheses.

For a module sheaf $F$ on $X$, set

\[
T^p(F)=\varinjlim_{U\supset Z}H^p(U,F|_U),\qquad
S^p(F)=H^p(Z,F|_Z),
\]

where $U$ runs through ambient open neighborhoods, with transition maps given by restriction. Inverse image to an open or to $Z$ is exact, and filtered colimits of modules are exact. Consequently both systems have the long exact sequences of cohomological delta functors. Restriction gives a morphism $T^p\to S^p$, and the finite-gluing argument identifies it in degree zero. If $I$ is injective, then $T^{p}(I)=0$ for $p>0$, since $I$ is acyclic on every open. The acyclicity conclusion proved in Tag 09V3 gives $S^{p}(I)=0$ for $p>0$.

Embed $F$ into an injective $I$ and write $Q=I/F$. The two long exact sequences identify $T^1(F)$ and $S^1(F)$ with the respective cokernels of the degree-zero map for $I\to Q$. Their comparison is an isomorphism. For $p>1$, the connecting maps identify $T^p(F)$ with $T^{p-1}(Q)$ and $S^p(F)$ with $S^{p-1}(Q)$. Induction proves the comparison in every degree, and all maps used commute with restriction and morphisms of short exact sequences. This closes that dimension-shifting step. It says nothing about an arbitrary closed exhaustion or about exactness of an inverse limit of sheaves.

## SH02-PRP-E5. Proper base change with arbitrary constant-ring coefficients

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

Its image consists of rational sequences with a common denominator. The sequence `(1/n!)_{n≥1}` has no common denominator, so the map is not surjective. All derived objects in this example are computed as stated: `A` is projective, `Q` is flat, and after scalar extension `⊕Q` is projective. Thus the comparison need not be an isomorphism for an arbitrary map.

## Antecedents and reuse

The Stacks Project supplies the mathematical antecedents identified by exact tags in these proofs. The cited source is official commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, and the [license notice](https://raw.githubusercontent.com/stacks/stacks-project/a04446e57ec1fbc252a871afcec7752fb2807b14/introduction.tex) specifies GFDL-1.2-or-later with no invariant sections or cover texts. The intended licence for this exposition is GFDL-1.2-or-later.
