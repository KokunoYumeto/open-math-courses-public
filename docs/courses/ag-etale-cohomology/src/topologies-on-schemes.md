# Topologies on schemes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

A change of topology changes what it means to solve a problem locally. Adjoining a separable algebraic element is allowed étale locally. Extracting a root of a unit is allowed fppf locally even when the exponent equals the characteristic. Faithfully flat descent explains why these additional local operations still preserve the familiar gluing rules for functions, morphisms and vector bundles.

For a quasi-coherent module, the larger topologies do not change cohomology. The reason is a concrete algebraic contraction, followed by the vanishing criterion of [Cohomology on sites](cohomology-on-sites.md). We prove the comparison for every scheme, including schemes whose affine open intersections are not affine. We then identify multiplicative torsors with line bundles and compare the big and small étale sites for arbitrary abelian coefficients.

The scheme-theoretic prerequisites are flat, étale and smooth morphisms, as treated in [Flat morphisms](course:AG-FSE/AG-FSE-01), [Étale morphisms and their local structure](course:AG-FSE/AG-FSE-04) and [Smooth morphisms](course:AG-FSE/AG-FSE-05) (see also [Stacks, Tag 01U2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-flat), [Tag 02GH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-etale) and [Tag 01V4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-smooth)). Faithfully flat descent for quasi-coherent modules and for morphisms is used without proof; its exact statement is in section 3. None of the arguments below requires the optional hypercovering lesson.

## 1. Which schemes and which covers?

Fix a scheme \(S\). An object of the **big category** is an arbitrary scheme \(T\to S\); arrows are \(S\)-morphisms. A topology on this category is specified by covering families of schemes over a fixed target \(T\). In contrast, the **small Zariski category** has the open subschemes of \(S\) as objects, and the **small étale category** has the schemes étale over \(S\). In the small étale category all \(S\)-morphisms are allowed; they are themselves étale. The coverings of these two small categories are, respectively, Zariski and étale coverings.

Here and throughout, the empty family covers the empty scheme. Nonempty targets have jointly surjective covering families. Fibre products are scheme fibre products, with all their points and residue-field extensions; the underlying set of a fibre product is generally not a set-theoretic fibre product.

**Size convention.** Choose Grothendieck universes \(\mathbb U\in\mathbb V\), with \(S\) defined in \(\mathbb U\). Take a skeleton of the category of \(\mathbb U\)-small schemes over \(S\), and allow covering families indexed by \(\mathbb U\)-small sets. This category and its coverings form sets in \(\mathbb V\). Sheaves take values in \(\mathbb V\)-sets, and cohomology is computed on this \(\mathbb V\)-small site. Use the same convention for all six topologies. Thus every use of enough injectives, products, covering colimits and the vanishing criterion has a set-sized presenting site in the working universe.

We write this big site as \((\mathrm{Sch}_{\mathbb U}/S)_\tau\), or simply \((\mathrm{Sch}/S)_\tau\) when the convention is understood. The notation \(S_{\mathrm{Zar}}\) and \(S_{\mathrm{ét}}\) refers to the small sites. The larger universe is particularly relevant for fpqc coverings: section 8 proves that one cannot replace all such coverings by an unrestricted set of cofinal coverings. We do not assert an arbitrary-sheaf fpqc comparison between different choices of universe. The quasi-coherent and degree-one multiplicative calculations below identify their groups with intrinsic groups of \(S\), and hence give independence for these specific coefficients.

A useful general construction starts with a class of morphisms containing isomorphisms and stable under composition and base change. Declare a family to cover when its members belong to the class and their images cover the target. Identity, base change and composition of covering families then hold. For the base change assertion about images, if a point of the new target lies over a point in an image, extend residue fields to obtain a point of the appropriate fibre product. Equivalently, the tensor product of two field extensions over their common subfield is a nonzero ring. This proves that a surjective scheme morphism remains surjective under arbitrary base change. The first five topologies below follow this construction. The fpqc condition needs one additional argument.

## 2. The six topologies and the affine test

A **Zariski covering** is a jointly surjective family of open immersions. An **étale**, **smooth** or **syntomic covering** is a jointly surjective family of morphisms of the indicated kind. An **fppf covering** is a jointly surjective family of flat morphisms locally of finite presentation. The word “locally” permits members which are not quasi-compact.

For clarity, a syntomic morphism is flat and locally of finite presentation, with local complete intersection fibres. Over a field, a local complete intersection is locally a quotient of a polynomial algebra by a regular sequence, allowing localization. The equivalence with the usual local definition, and permanence under composition and base change, are the scheme-theoretic results [Stacks, Tags 01UC–01UI]. Smooth morphisms are syntomic; syntomic morphisms are flat and locally of finite presentation. We use these morphism facts, together with the corresponding flat, étale and smooth permanence facts, as prerequisites. They do not contain the cohomological conclusions of this lesson.

**Definition 2.1.** A family \(\{f_i:T_i\to T\}_{i\in I}\) is an **fpqc covering** if each \(f_i\) is flat and, for every affine open \(U\subset T\), there are finitely many affine opens

\[
V_j\subset T_{i(j)},\qquad
f_{i(j)}(V_j)\subset U,\qquad
U=\bigcup_j f_{i(j)}(V_j).
\tag{2.1}
\]

Repetition of an index \(i(j)\) is allowed. This is the affine-refinement definition [Stacks, Tag 022B]. It implies joint surjectivity. It does not require each \(T_i\to T\) to be quasi-compact, and flatness plus joint surjectivity alone does not imply (2.1).

Call a finite jointly surjective family \(\{V_j\to U\}\), with \(U,V_j\) affine and every map flat, a **standard fpqc covering**. If \(U=\operatorname{Spec}A\), \(V_j=\operatorname{Spec}B_j\), put \(B=\prod_j B_j\). Then

\[
\coprod_j V_j=\operatorname{Spec}B,
\qquad A\longrightarrow B\text{ is faithfully flat}.
\tag{2.2}
\]

Indeed, a finite product of flat modules is flat, and the spectrum map is surjective. Conversely a faithfully flat ring map gives a singleton standard fpqc covering. Such an affine morphism satisfies (2.1): over \(D(a)\subset\operatorname{Spec}A\) use \(\operatorname{Spec}B_a\); a general affine open is covered by finitely many such principal opens. The same argument applies to finite families.

**Proposition 2.2.** All six classes of covering families define sites, and their topologies satisfy

\[
\mathrm{Zar}\ \subset\ \mathrm{étale}\ \subset\ \mathrm{smooth}
\ \subset\ \mathrm{syntomic}\ \subset\ \mathrm{fppf}
\ \subset\ \mathrm{fpqc}.
\tag{2.3}
\]

**Proof.** The first five satisfy the general construction of section 1. Open immersions are étale, étale morphisms are smooth, smooth morphisms are syntomic, and syntomic morphisms are flat and locally of finite presentation. This proves the first four inclusions at the level of covering families.

A flat morphism locally of finite presentation is open [Stacks, Tag 01UA]. Given an fppf covering and an affine open \(U\) in its target, cover each inverse image of \(U\) by affine opens. Their images are open and cover \(U\). Quasi-compactness of \(U\) selects finitely many of them. These are exactly the opens required by (2.1), proving the last inclusion.

We verify the fpqc covering axioms explicitly. Isomorphisms give singleton covers. For base change along \(T'\to T\), let \(W\subset T'\) be affine. Choose finitely many principal affine opens \(W_\ell\) covering \(W\), each mapping into an affine open \(U_\ell\subset T\). Apply (2.1) over \(U_\ell\). The schemes \(V_{\ell j}\times_{U_\ell}W_\ell\) are affine opens in the corresponding base-changed members and cover \(W_\ell\). Their finite union of images covers \(W\). Flatness is preserved by base change, so this is an fpqc covering. This proof also shows that it is enough to check (2.1) on a fixed affine open cover of the target: subdivide any other affine open into finitely many principal opens subordinate to that cover.

For composition, first choose finitely many \(V_j\subset T_{i(j)}\) over an affine \(U\subset T\) as in (2.1). Apply the second covering condition over each affine open \(V_j\). Its finitely many affine opens in the second-stage members jointly map onto \(V_j\), and thus their composite images jointly cover \(U\). The composite maps are flat. All families and selections remain in \(\mathbb U\). These arguments prove identity, composition and base change, including the empty target. The pretopologies therefore generate the stated sites. \(\square\)

No strictness assertion is intended by the inclusion symbols. They specify the comparison direction: an fpqc sheaf is a sheaf for every topology displayed to its left.

**Affine coverings.** For each \(\tau\), every cover of an affine target has a refinement by a finite cover with affine members of the same kind. For fpqc this is the definition. For the other topologies, choose affine charts in the sources and use openness of their maps to select finitely many images covering the affine target; for Zariski one may choose principal opens of the target. Flatness and the relevant local morphism property survive the restrictions. An affine-to-affine map locally of finite presentation is of finite presentation, so the fppf refinements are finite-presentation affine covers. Smooth and syntomic charts can also be chosen in their standard local forms, although we only need their flatness. Every finite iterated fibre product in these affine coverings is affine.

**Lemma 2.3 (sheaf test).** A presheaf of sets on the big category is an fpqc sheaf if and only if it is a Zariski sheaf and satisfies the sheaf condition for faithfully flat morphisms of affine schemes.

**Proof.** Necessity follows from Proposition 2.2. A Zariski sheaf carries a finite disjoint union to the product of its values. Consequently its matching diagram for a standard family is the matching diagram for the faithfully flat singleton (2.2), including the disjoint-union decomposition of the double overlap.

For sufficiency, take an fpqc cover \(\{T_i\to T\}\) and matching sections \(s_i\). On an affine open \(U\subset T\), choose a standard refinement \(\{V_j\to U\}\). The affine condition supplies a unique section \(s_U\). We must check it pulls back to the original \(s_i\), rather than merely to their restrictions on the refinement. On every affine open \(W\subset T_i\times_T U\), the finite affine cover \(\{W\times_U V_j\to W\}\) is standard. The two sections agree there by the original matching condition, and hence agree on \(W\). The Zariski condition gives agreement on all of \(T_i\times_T U\).

Uniqueness holds on \(U\), since the chosen standard refinement detects equality. On the intersection of two affine opens of \(T\), use an affine open cover of the intersection and the same uniqueness argument to see their sections agree. Zariski gluing produces \(s\in F(T)\), and the already verified pullbacks give \(s|_{T_i}=s_i\). Its uniqueness follows by the same affine restrictions. This proves the complete matching condition. \(\square\)

## 3. Descent makes representable presheaves into sheaves

We use the following scheme-theoretic descent theorem without proof. For an fpqc family \(\{T_i\to T\}\), quasi-coherent modules on \(T\) are equivalent to quasi-coherent modules on the \(T_i\) equipped with isomorphisms on \(T_i\times_T T_j\) satisfying the cocycle condition on triple overlaps. This includes descent of maps between modules, not only existence of the descended object. Moreover, for any scheme \(Z\),

\[
\operatorname{Mor}(T,Z)\ \longrightarrow\
\prod_i\operatorname{Mor}(T_i,Z)
\ \rightrightarrows\
\prod_{i,j}\operatorname{Mor}(T_i\times_T T_j,Z)
\tag{3.1}
\]

is an equalizer, and the assertion persists after every base change of the family. These are effective fpqc descent for quasi-coherent modules [Stacks, Tag 023T] and universal effective epimorphy for morphisms [Stacks, Tag 023Q]. No claim that arbitrary schemes or arbitrary sheaves descend effectively as schemes is included.

**Theorem 3.1 (subcanonicity).** For every \(S\)-scheme \(Z\), the presheaf \(h_Z(T)=\operatorname{Mor}_S(T,Z)\) is an fpqc sheaf, and hence a sheaf in all six topologies.

**Proof.** A matching family of \(S\)-morphisms descends uniquely as a morphism of schemes by (3.1). The descended map is over \(S\): its two composites to \(S\), the prescribed structure map and the composite through \(Z\), agree on all \(T_i\), so the uniqueness part of (3.1), now with target \(S\), makes them equal. This gives both existence and uniqueness in the relative matching diagram. Proposition 2.2 gives the remaining topologies. \(\square\)

Thus subcanonicity is a consequence of descent, not part of the definition of the topology. Three useful representable abelian sheaves are

\[
\begin{aligned}
\mathbf G_a(T)&=\Gamma(T,\mathcal O_T),
&\mathbf G_a&=\mathbf A^1_S,\\
\mathbf G_m(T)&=\Gamma(T,\mathcal O_T)^\times,
&\mathbf G_m&=\operatorname{Spec}_S\mathcal O_S[x,x^{-1}],\\
\mu_n(T)&=\{u\in\Gamma(T,\mathcal O_T)^\times:u^n=1\},
&\mu_n&=\operatorname{Spec}_S\mathcal O_S[x]/(x^n-1),\quad n\geq1.
\end{aligned}
\tag{3.2}
\]

In the first equality, maps from any scheme to relative affine space are global functions; no affineness of \(T\) is required. In the last, \(x\) is already invertible because \(x^n=1\). Addition or multiplication gives the indicated group law. The kernel description \(\mu_n=\ker(\mathbf G_m\xrightarrow{u\mapsto u^n}\mathbf G_m)\) is valid in every topology, even when the power map is not an epimorphism there.

For a \(\mathbb U\)-small set \(A\), the constant sheaf with fibre \(A\) is represented by \(A_S=\coprod_{a\in A}S\). A map \(T\to A_S\) is an open-and-closed partition \(T=\coprod_a T_a\), equivalently a locally constant function \(|T|\to A\) with \(A\) discrete. These maps form an fpqc sheaf by Theorem 3.1. Every such map is Zariski locally a constant label, and distinct labels over a nonempty open never become equal on a jointly surjective cover. Thus its natural map from the constant presheaf has exactly the local existence and local equality properties of associated sheafification. This identifies it with the constant sheaf in each of the six topologies. For an abelian group \(A\), addition of labels gives the constant abelian sheaf.

## 4. The algebra behind quasi-coherent descent

Let \(\mathcal F\) be a quasi-coherent \(\mathcal O_S\)-module. Its associated presheaf on the big category is

\[
\mathcal F^a(T\xrightarrow{f}S)=\Gamma(T,f^*\mathcal F).
\tag{4.1}
\]

For an arrow \(g:T'\to T\), pull back a section and use \(g^*f^*\mathcal F\simeq(fg)^*\mathcal F\). These canonical identifications satisfy the composition rule. This presheaf is a module over the structure presheaf \(\mathcal O(T)=\Gamma(T,\mathcal O_T)\).

**Lemma 4.1 (augmented Amitsur exactness).** If \(A\to B\) is faithfully flat and \(M\) is any \(A\)-module, the augmented complex

\[
0\longrightarrow M\longrightarrow M\otimes_A B
\longrightarrow M\otimes_A B^{\otimes_A2}
\longrightarrow M\otimes_A B^{\otimes_A3}\longrightarrow\cdots
\tag{4.2}
\]

is exact. In cohomological degree \(n\geq0\), the differential inserts \(1\) successively in the \(n+2\) possible positions among the \(B\)-factors, with signs \((-1)^j\), \(0\leq j\leq n+1\). The augmentation is \(m\mapsto m\otimes1\).

**Proof.** Put \(C^{-1}=M\) and \(C^n=M\otimes_A B^{\otimes(n+1)}\). Tensor the complex with \(B\), retaining the new factor first. Define

\[
h_n(b_0\otimes m\otimes b_1\otimes\cdots\otimes b_{n+1})
=b_0b_1\otimes m\otimes b_2\otimes\cdots\otimes b_{n+1}
\quad(n\geq0).
\tag{4.3}
\]

The codomain for \(n=0\) is \(B\otimes_A M\). In \(h_{n+1}d_n\), insertion in the first position gives the identity. Insertion in position \(j>0\) agrees with applying \(h_n\) and then inserting in position \(j-1\), with the opposite sign. Therefore

\[
h_{n+1}d_n+d_{n-1}h_n=1\quad(n\geq0),
\qquad h_0d_{-1}=1.
\tag{4.4}
\]

This contracts the entire augmented complex after base change. Flat tensor product preserves kernels and images and hence its cohomology; faithful flatness detects whether a module is zero. All augmented cohomology groups before base change are therefore zero. No finite generation condition on \(M\) was used. \(\square\)

**Proposition 4.2.** The presheaf \(\mathcal F^a\) is an fpqc sheaf of \(\mathcal O\)-modules. The positive Čech cohomology of every standard affine fpqc covering with these coefficients vanishes.

**Proof.** On a Zariski cover of \(T\), (4.1) is the ordinary sheaf condition for the quasi-coherent module \(f^*\mathcal F\) on \(T\). On \(T=\operatorname{Spec}A\), write \(f^*\mathcal F=\widetilde M\). For \(V=\operatorname{Spec}B\to T\), pullback of a quasi-coherent module gives
\(\mathcal F^a(V)=M\otimes_A B\).
Consequently the equalizer for a faithfully flat affine singleton is the beginning of (4.2). Lemma 2.3 proves the fpqc sheaf property. Its scalar multiplication is compatible with all restrictions, so it is a sheaf of modules.

For a finite standard family \(\{\operatorname{Spec}B_j\to\operatorname{Spec}A\}\), use \(B=\prod_jB_j\). Tensor powers of this finite product split into the products indexed by all ordered tuples \((j_0,\ldots,j_n)\), with repetitions. The same decomposition for \(M\otimes_A B^{\otimes(n+1)}\) identifies (4.2) with the augmented Čech complex of the family. The insertions of \(1\) become the alternating restrictions to the tuple overlaps. Lemma 4.1 proves exactness, including identification of degree-zero cohomology with \(\mathcal F^a(T)\). \(\square\)

This proof uses a disjoint union only to identify cochain complexes. For a Zariski cover, its finite disjoint union map to the target need not be an open immersion. The original finite family is still a Zariski cover, and its Čech complex is the one just identified with (4.2).

## 5. Cohomology does not change for quasi-coherent modules

Write \(H^q_\tau(T,G)\) for cohomology over the object \(T\) of the big site. It agrees with cohomology on the slice over \(T\), as proved in lesson 3. Ordinary scheme cohomology means cohomology on \(S_{\mathrm{Zar}}\).

**Theorem 5.1.** For every scheme \(S\), every quasi-coherent module \(\mathcal F\), every \(q\geq0\), and each of the six topologies, there is a natural isomorphism

\[
H^q_\tau(S,\mathcal F^a)
\simeq H^q(S_{\mathrm{Zar}},\mathcal F).
\tag{5.1}
\]

In particular \(H^q_\tau(T,\mathcal F^a)=0\) for \(q>0\) whenever \(T\to S\) is affine as a scheme; the structural map \(T\to S\) need not be affine or flat.

**Proof of affine vanishing.** Let \(\mathcal B\) consist of all affine objects of the big site. Let \(\mathrm{Cov}\) consist of their finite affine covering families of type \(\tau\). Section 2 proves cofinality among all covers of each such object and proves that every member and every finite tuple overlap belongs to \(\mathcal B\). Proposition 4.2 gives vanishing of positive Čech cohomology for all these covers: each is in particular a standard fpqc cover, with \(M\) the module of the pullback of \(\mathcal F\) to its affine target. These are sets in \(\mathbb V\). Theorem 4.1 of lesson 3 therefore gives the claimed positive derived-cohomology vanishing, simultaneously for all affine objects and all positive degrees.

**Proof of the global comparison.** Inclusion of the open subschemes of \(S\) into the big category induces a morphism of topoi

\[
p:\operatorname{Sh}((\mathrm{Sch}/S)_\tau)
\longrightarrow\operatorname{Sh}(S_{\mathrm{Zar}}),
\qquad (p_*G)(U)=G(U).
\tag{5.2}
\]

Here is a direct check of the morphism assertion. Restriction sends sheaves to sheaves because Zariski covers are \(\tau\)-covers. Its presheaf left adjoint, evaluated at \(T\to S\), is the colimit of the values on opens \(U\subset S\) through which \(T\to S\) factors. This index is nonempty, since it contains \(S\), and is filtered by shrinking: two such opens have their intersection as a common successor. There are no distinct parallel arrows. Filtered colimits of sets preserve finite limits. Applying \(\tau\)-sheafification, which preserves finite limits by lesson 1, gives a left exact left adjoint \(p^{-1}\) to (5.2). On abelian sheaves it is exact by lesson 2. Thus (5.2) is a geometric morphism and \(p_*\) preserves injective abelian sheaves.

Take an injective abelian resolution \(\mathcal F^a\to I^\bullet\). The sheaf \(R^qp_*\mathcal F^a\) is the Zariski sheaf associated to

\[
U\longmapsto H^q(I^\bullet(U))
=H^q_\tau(U,\mathcal F^a).
\tag{5.3}
\]

Indeed, the cohomology sheaf of the complex \(p_*I^\bullet\) is the sheafification of its sectionwise cohomology: kernels are objectwise and images are the associated sheaves of presheaf images. For \(q>0\), (5.3) vanishes on every affine open by the preceding proof. It therefore has zero associated sheaf, since affine opens cover every open of \(S\). In degree zero, \(p_*\mathcal F^a=\mathcal F\), by the ordinary restriction rule for pullback to an open subscheme.

The Leray spectral sequence from lesson 3 now has only the row \(q=0\). Its edge isomorphism is (5.1). This also proves its naturality in \(\mathcal F\), and identifies it with the canonical comparison from Zariski cohomology to the larger site. No assumption on intersections of affine opens of \(S\) entered the argument. No quasi-compactness or separation assumption on \(S\) entered either. \(\square\)

The same identification applies to the small Zariski and small étale sites, using the big/small comparison in section 7. For the universe-relative fpqc site, the affine-refinement and vanishing proofs above supply the comparison directly; the fpqc clause is not an appeal to a cohomology theorem whose stated scope only includes the other five topologies.

## 6. Multiplicative torsors are line bundles

Let \(\operatorname{Pic}(S)\) be the group of isomorphism classes of \(\mathcal O_S\)-modules locally free of rank one, with tensor product. We will need the following rank descent check in addition to effective quasi-coherent descent.

**Lemma 6.1.** If a quasi-coherent module \(L\) pulls back to a free rank-one module on every member of an fpqc cover, then \(L\) is Zariski locally free of rank one.

**Proof.** Over an affine open \(\operatorname{Spec}A\subset S\), choose a finite affine refinement of the cover. With \(B\) the product of its rings and \(M=\Gamma(\operatorname{Spec}A,L)\), we have a faithfully flat map \(A\to B\) and \(M\otimes_A B\simeq B\).

First \(M\) is finitely presented. Finitely many generators of \(M\otimes_A B\) use a finite list of elements of \(M\); that list generates \(M\), since its cokernel becomes zero after faithful flat base change. Choose a surjection \(A^r\to M\) with kernel \(N\). Flatness identifies \(N\otimes_A B\) with the kernel of \(B^r\to M\otimes_A B\). The latter is finitely generated because the quotient is finitely presented. The same generator descent makes \(N\) finitely generated. Hence \(M\) is finitely presented.

At a prime \(\mathfrak p\subset A\), choose \(\mathfrak q\subset B\) above it. The map \(A_{\mathfrak p}\to B_{\mathfrak q}\) is flat and local, hence faithfully flat. The dimension of \(M\otimes_A\kappa(\mathfrak p)\) is one, since extending it to \(\kappa(\mathfrak q)\) gives a one-dimensional vector space. Lift a basis element to \(M_{\mathfrak p}\). Nakayama gives a surjection \(A_{\mathfrak p}\to M_{\mathfrak p}\). After tensoring with \(B_{\mathfrak q}\), this map is multiplication by an element whose residue is nonzero, so it is an isomorphism. Faithful flatness gives an isomorphism before tensoring.

Finally this local isomorphism extends to a neighbourhood. Choose the generator on some \(D(f)\) about \(\mathfrak p\). Its finitely generated cokernel vanishes after another localization, making the map surjective. Its kernel is then finitely generated, since \(M\) is finitely presented, and vanishes at \(\mathfrak p\). Localize once more to kill that kernel. On this neighbourhood \(M\) is free of rank one. As \(\mathfrak p\) was arbitrary, \(L\) is a line bundle. \(\square\)

**Theorem 6.2 (Hilbert 90).** In each of the six topologies there is a natural group isomorphism

\[
H^1_\tau(S,\mathbf G_m)\simeq\operatorname{Pic}(S).
\tag{6.1}
\]

For Zariski and étale this may equally be computed on the small site. In particular the Zariski, étale and fppf groups requested here are canonically identical.

**Proof.** Lesson 3 identifies \(H^1\) of an abelian sheaf with isomorphism classes of its right torsors. For a line bundle \(L\), define its frame sheaf by

\[
P_L(T)=\operatorname{Isom}_{\mathcal O_T}(\mathcal O_T,f^*L).
\tag{6.2}
\]

Maps of quasi-coherent modules and their inverses descend uniquely by section 3, so (6.2) is an fpqc sheaf. Multiplication of a frame by a unit is a right \(\mathbf G_m\)-action. Two frames differ by a unique unit, and frames exist Zariski locally. Thus \(P_L\) is a torsor in every one of the six topologies.

Conversely, let \(P\) be a \(\mathbf G_m\)-torsor for \(\tau\). Choose a \(\tau\)-cover \(\{T_i\to S\}\) and sections \(p_i\). On the double overlaps there are unique units \(g_{ij}\) such that \(p_j=p_i g_{ij}\). On triple overlaps uniqueness gives \(g_{ij}g_{jk}=g_{ik}\); on the diagonal it gives \(g_{ii}=1\). Glue the trivial quasi-coherent modules with frames \(e_i\), prescribing \(e_j=e_i g_{ij}\). This is an fpqc descent datum because every \(\tau\)-cover is fpqc. Effective descent produces a quasi-coherent module \(L\). Its pullbacks are free of rank one, so Lemma 6.1 makes it a line bundle on \(S\).

The maps \(p_i u\mapsto e_i u\) identify \(P\) with \(P_L\) locally and respect \(g_{ij}\) on overlaps; sheaf gluing makes a global equivariant isomorphism. Changes of chosen sections change frames by exactly the same units, so descent of module maps makes the resulting \(L\) unique up to a unique isomorphism compatible with this identification. Isomorphic torsors give isomorphic line bundles. Starting with \(L\), this descent construction recovers it, since its local frames yield its original descent datum. We have proved both inverse constructions.

The sum of torsor classes is the contracted product: identify \((p a,q)\) with \((p,q a)\). Its local transition units are \(g_{ij}h_{ij}\). These are the transition units of \(L\otimes L'\); the frame map is \((e,e')\mapsto e\otimes e'\). Thus the bijection respects the group laws. Pullback of frames and descent data proves naturality under a scheme map. Section 7 supplies the small-site version. \(\square\)

In particular every fppf \(\mathbf G_m\)-torsor is Zariski locally trivial. Its fppf local trivializations might look more general, but the descended line bundle has ordinary Zariski frames.

**Why the group matters.** Let \(K=\mathbf F_p(t)\). On \(S_{\mathrm{ét}}\), the sheaf \(\mu_p\) is trivial: an étale \(K\)-scheme is reduced, and \(u^p=1\) implies \((u-1)^p=0\), hence \(u=1\). Consequently \(H^1_{\mathrm{ét}}(K,\mu_p)=0\). On the fppf site the sequence

\[
1\longrightarrow\mu_p\longrightarrow\mathbf G_m
\xrightarrow{u\mapsto u^p}\mathbf G_m\longrightarrow1
\tag{6.3}
\]

is exact. For a unit \(a\) on an affine \(\operatorname{Spec}A\), the algebra \(A[z]/(z^p-a)\) is free of positive rank \(p\), hence faithfully flat, and of finite presentation; \(z\) is a unit there. These covers give local roots, proving the last epimorphism. Since \(\operatorname{Pic}(\operatorname{Spec}K)=0\), the long exact sequence and (6.1) give

\[
H^1_{\mathrm{fppf}}(K,\mu_p)=K^\times/(K^\times)^p\ne0.
\tag{6.4}
\]

The class of \(t\) is nonzero because its \(t\)-adic valuation is one, whereas a \(p\)-th power has valuation divisible by \(p\). Thus Hilbert 90 for \(\mathbf G_m\) does not imply a comparison for all group sheaves. On the big étale site \(\mu_p\) also sees nonreduced objects; nevertheless section 7 identifies its cohomology over \(K\) with that of its trivial small-site restriction.

## 7. Big and small étale cohomology

**Theorem 7.1.** Let \(\tau\) be Zariski or étale. Restriction \(r\) from the big \(\tau\)-site to \(S_\tau\) gives, for every abelian sheaf \(G\) and \(q\geq0\), a natural isomorphism

\[
H^q((\mathrm{Sch}/S)_\tau,G)
\simeq H^q(S_\tau,rG).
\tag{7.1}
\]

**Proof.** Every big \(\tau\)-cover of a small-site object has its members in the small site. For étale, this is composition of the member's étale map to the target with the target's étale map to \(S\). For Zariski, it is composition of open immersions. The finite iterated fibre products are again small-site objects, and all these covers are the same covers on the two sites.

Restriction \(r\) is exact on abelian sheaves. Kernels are computed objectwise. If \(G\to H\) is an epimorphism on the big site, every section of \(H\) over a small object lifts on a big covering of that object. The preceding paragraph says this is already a small-site covering. The local epimorphism criterion gives surjectivity as a small-site sheaf map. This proves exactness.

Let \(I\) be a big-site injective abelian sheaf. Its augmented Čech complex is exact on every covering, by lesson 3, section 3. For a small-site cover this is precisely the augmented complex with coefficients \(rI\). Apply the vanishing criterion of that lesson with \(\mathcal B\) all small-site objects and \(\mathrm{Cov}\) all their covering families. Cofinality is automatic; all tuple overlaps stay in \(\mathcal B\); and every positive Čech group is zero. Hence

\[
H^q(S_\tau/U,rI)=0\quad(q>0)
\tag{7.2}
\]

for every small-site object \(U\), in particular for \(U=S\).

Now restrict a big injective resolution \(G\to I^\bullet\). Exactness of \(r\) makes this a resolution of \(rG\), and (7.2) makes all its terms acyclic for small-site global sections. The acyclic-resolution theorem therefore computes small-site cohomology from \(I^\bullet(S)\). The identical complex computes big-site cohomology. This gives (7.1) in every degree. Resolution comparison, or the natural comparison of the two cohomological delta functors under exact restriction, shows the isomorphism is canonical and natural. \(\square\)

The theorem concerns cohomology over \(S\) and does not identify the entire big and small topoi. Its proof did not assume that every big object is covered by small objects; arbitrary big objects need not have that property.

## 8. Covers that distinguish the definitions

**Finite products and separable extensions.** If \(A=\prod_{j=1}^r A_j\), the orthogonal idempotents of the factors give an open-and-closed decomposition

\[
\operatorname{Spec}A=\coprod_{j=1}^r\operatorname{Spec}A_j.
\tag{8.1}
\]

The factor inclusions are a Zariski covering. Finiteness is essential: for \(A=\prod_{j\in\mathbf N}\mathbf F_2\), a nonprincipal ultrafilter on \(\mathbf N\) gives a homomorphism \(A\to\mathbf F_2\) by taking the unique value on an ultrafilter-large set. Its kernel is a prime which is not a coordinate kernel, so the coordinate spectra do not cover. For a finite separable extension \(k'/k\), \(\operatorname{Spec}k'\to\operatorname{Spec}k\) is a surjective finite étale map, giving an étale singleton cover.

**Completion.** For every Noetherian local ring \((A,\mathfrak m)\), the map \(A\to\widehat A\) is faithfully flat [Stacks, Tag 00MC]. Thus completion alone gives an fpqc singleton cover, and adding the flat open immersion \(\operatorname{Spec}A\setminus\{\mathfrak m\}\to\operatorname{Spec}A\) still gives an fpqc family. To obtain a family which is not an fppf family, take

\[
A=\mathbf F_p[t]_{(t)},\qquad\widehat A=\mathbf F_p[[t]].
\tag{8.2}
\]

The punctured spectrum is \(D(t)=\operatorname{Spec}\mathbf F_p(t)\). The completion is uncountable, whereas every finite type algebra over the countable ring \(A\) is countable. Hence \(A\to\widehat A\) is not of finite type. An affine morphism locally of finite presentation is of finite presentation, so this completion morphism is not locally of finite presentation. The two-member family is fpqc but fails the member condition for fppf. No such failure is asserted for every Noetherian local ring: an already complete ring has completion map the identity.

**Flat and surjective can fail to be fpqc.** Let

\[
R=k[t_1,t_2,\ldots],\qquad
\mathfrak m=(t_1,t_2,\ldots),\qquad X_1=X_2=\operatorname{Spec}R.
\tag{8.3}
\]

Glue the two schemes along \(\operatorname{Spec}R\setminus\{\mathfrak m\}\), by the identity, obtaining \(X\). Consider

\[
Y=X_1\ \amalg\ \operatorname{Spec}R_{\mathfrak m}
\longrightarrow X,
\tag{8.4}
\]

with the local spectrum mapping through \(X_2\). Both components are flat, and the map is surjective: \(X_1\) contains all points except the second origin, which is supplied by the local spectrum. The source is quasi-compact.

If (8.4) were fpqc, over the affine open \(X_2\) there would be a quasi-compact open \(W\subset Y\) with image exactly \(X_2\): take the union of the finitely many affine opens in (2.1). Its part \(U\) in \(X_1\) is a quasi-compact open contained in \(X_1\setminus\{\mathfrak m\}\), because the first origin is not a point of \(X_2\). Its part in the local spectrum must contain the closed point to hit the second origin; an open containing the closed point of a local spectrum is the whole spectrum. In any case the image of that component consists of primes contained in \(\mathfrak m\).

Cover \(U\) by finitely many principal opens \(D(f_\ell)\), with \(f_\ell\in\mathfrak m\). All these polynomials use only \(t_1,\ldots,t_N\) for some \(N\). The closed point of \(X_2\) given by \(t_{N+1}=1\) and all other \(t_j=0\) lies in none of the \(D(f_\ell)\). Its maximal ideal is not contained in \(\mathfrak m\), because it contains \(t_{N+1}-1\). It is therefore also outside the image of \(\operatorname{Spec}R_{\mathfrak m}\). This contradicts surjectivity of \(W\to X_2\). Thus (8.4) is not fpqc [Stacks, Example 0H7E]. This is also why a quasi-compact source alone cannot replace the affine-target condition.

**The size obstruction.** Even over a fixed nonzero ring \(R\), there is no unrestricted set of fpqc covers of \(\operatorname{Spec}R\) refining every fpqc cover [Stacks, Tag 0BBK]. Over a field \(k\), adjoining independent variables indexed by an arbitrarily large set \(I\) gives the cover \(\operatorname{Spec}k(t_i:i\in I)\to\operatorname{Spec}k\). A refinement must admit a morphism to this field spectrum on every member. At a point of any nonempty member this embeds \(k(t_i)\) into its residue field. A fixed set of candidate covers has a common cardinal bound for all its residue fields, while \(|I|\) has no unrestricted bound. Solution 5 proves the assertion for nonzero \(R\), extends it to every nonempty scheme, and explains how the universes of section 1 resolve the site-size issue.

## 9. Exercises

1. **Easy.** Show that a Zariski covering is étale and that an étale covering is fppf. Identify which morphism properties, rather than covering axioms, enter the argument.
2. **Medium.** For a faithfully flat ring map \(A\to B\) and an arbitrary \(A\)-module \(M\), prove exactness of the augmented Čech complex directly. Write a contraction after tensoring with \(B\), and check its augmentation and signs.
3. **Medium.** Starting with an fppf \(\mathbf G_m\)-torsor, construct its line bundle and prove Zariski local triviality. Explain why this deduces fppf Hilbert 90 from the Zariski case, with the correct group law.
4. **Medium.** Give a scheme \(S\) and an abelian sheaf on its big étale site which is not isomorphic, even as an abelian sheaf, to \(\mathcal F^a\) for any quasi-coherent \(\mathcal F\). Compute its sections over \(S\).
5. **Hard.** Prove that no unrestricted set of fpqc covers of a fixed nonempty affine scheme is cofinal under refinement. For \(R\ne0\), use the localization of \(R[t_i:i\in I]\) by polynomials whose reductions are nonzero modulo every prime of \(R\). Prove faithful flatness and compute the fibre at a maximal ideal. Explain the empty-scheme exception and the universe convention used here. Can you extend the obstruction to every nonempty scheme?

## 10. Solutions

**Solution 1.** An open immersion is étale: near any source point it is a localization, which is flat and locally of finite presentation with zero relative differentials, equivalently a local isomorphism. Every étale morphism is flat and locally of finite presentation, hence has the fppf member property. The given covering families remain jointly surjective, so they are covers of the larger type. The facts about the individual morphisms are the input; surjectivity itself is unchanged. Neither implication adds a quasi-compactness requirement to an individual member.

**Solution 2.** For \(C^{-1}=M\) and \(C^n=M\otimes_A B^{\otimes(n+1)}\), insert \(1\) with sign \((-1)^j\) to define \(d\). Inserting twice in positions \(i<j\) can be done in the opposite order with the second index lowered by one. The two terms have opposite signs; this pairs all terms in \(d^2\), proving \(d^2=0\). In degree zero,

\[
d_0(m\otimes b)=m\otimes1\otimes b-m\otimes b\otimes1,
\tag{10.1}
\]

which is the difference of the two restrictions, and its composite with the augmentation is zero.

After tensoring with \(B\), distinguish the new first factor and use \(h\) in (4.3). In degree \(-1\), \(h_0(b_0\otimes m\otimes1)=b_0\otimes m\). In degree zero,

\[
\begin{aligned}
h_1d_0(b_0\otimes m\otimes b_1)
&=b_0\otimes m\otimes b_1-b_0b_1\otimes m\otimes1,\\
d_{-1}h_0(b_0\otimes m\otimes b_1)
&=b_0b_1\otimes m\otimes1.
\end{aligned}
\tag{10.2}
\]

Their sum is the original tensor. In arbitrary degree, the insertion before \(b_1\) contributes the original tensor; every other insertion contributes \(-d h\), because its index drops by one after multiplying \(b_0b_1\). This proves (4.4) in all degrees. A contracted augmented complex is exact. Flatness identifies its cohomology after base change with the tensor product of its original cohomology, and faithfulness makes every original group zero. This also proves injectivity of the augmentation, which would be missing if only positive degrees were checked.

**Solution 3.** Choose fppf local sections \(p_i\) of the torsor. Their unique comparison units \(g_{ij}\), defined by \(p_j=p_i g_{ij}\), satisfy \(g_{ij}g_{jk}=g_{ik}\). Apply effective quasi-coherent descent to the trivial modules with change of frames \(e_j=e_i g_{ij}\). The descended module \(L\) is locally free of rank one by Lemma 6.1, whose finite-presentation and local-generator proof works for this cover without assuming it is finite globally. The local maps \(p_i u\mapsto e_i u\) glue to an isomorphism with the frame torsor \(P_L\).

Choose a Zariski open trivialization of \(L\). Its frames give sections of \(P_L\), so the original torsor is Zariski locally trivial. Thus every fppf torsor comes from a Zariski torsor. Conversely a Zariski torsor is also an fppf torsor. If two Zariski frame torsors become isomorphic as fppf torsors, module descent of the local frame map gives an isomorphism of their line bundles; they were already isomorphic as Zariski torsors. The induced comparison on \(H^1\) is therefore bijective. Product of the units on overlaps corresponds to tensor product of line bundles, so it is a group isomorphism. Combining it with Zariski Hilbert 90 gives the fppf statement.

**Solution 4.** Take \(S=\operatorname{Spec}\mathbf F_p\) and the constant abelian sheaf \(\mathbf Z_S\), represented by the disjoint union of copies of \(S\) indexed by \(\mathbf Z\). Section 3 proves it is a sheaf on the big étale site. Since \(S\) is connected,

\[
\Gamma(S,\mathbf Z_S)=\mathbf Z.
\tag{10.3}
\]

If it were isomorphic as an abelian sheaf to \(\mathcal F^a\), evaluation at \(S\) would give \(\mathbf Z\simeq\Gamma(S,\mathcal F)\). The latter is an \(\mathbf F_p\)-module and is killed by \(p\); \(\mathbf Z\) is not. This is a contradiction. It does not depend on requiring a proposed isomorphism to respect a module structure.

**Solution 5.** Let \(R\ne0\), choose a maximal ideal \(\mathfrak m\), and put \(\kappa=R/\mathfrak m\). For a set \(I\), let \(P_I=R[t_i:i\in I]\) and

\[
D_I=\{f\in P_I: f\bmod\mathfrak p\ne0
\text{ in }(R/\mathfrak p)[t_i]\text{ for every prime }\mathfrak p\},
\qquad R_I=D_I^{-1}P_I.
\tag{10.4}
\]

The set \(D_I\) is multiplicative: each reduction is in a polynomial ring over a domain, where a product of nonzero polynomials is nonzero. It contains \(1\) and not \(0\). Polynomial extension and localization are flat, so \(R_I\) is flat over \(R\). Its fibre at any prime \(\mathfrak p\) is a localization of \(\kappa(\mathfrak p)[t_i]\) by nonzero elements and is therefore nonzero. Every fibre has a point, so \(\operatorname{Spec}R_I\to\operatorname{Spec}R\) is surjective and \(R\to R_I\) is faithfully flat. It gives an fpqc singleton cover.

At the chosen maximal ideal the fibre is exactly

\[
R_I\otimes_R\kappa=\kappa(t_i:i\in I).
\tag{10.5}
\]

To prove this, take any nonzero polynomial over \(\kappa\), and divide by one of its nonzero coefficients so that a selected coefficient is \(1\). Lift its other coefficients through the surjection \(R\to\kappa\), keeping that coefficient equal to \(1\). The lift belongs to \(D_I\), since a coefficient \(1\) survives every prime reduction. Thus every nonzero polynomial over \(\kappa\) becomes invertible in the fibre. Conversely all the inverted elements have nonzero reductions and are already invertible in the rational function field. These two inclusions give (10.5).

Suppose a set \(\mathcal A\) of candidate fpqc covers were cofinal. Base change all its families to \(\operatorname{Spec}\kappa\). The union of their members' points and residue fields is a set, so choose \(|I|\) strictly larger than the cardinality of every one of those residue fields. A candidate refining the cover from \(R_I\) would, after this base change, refine \(\operatorname{Spec}\kappa(t_i)\to\operatorname{Spec}\kappa\). At least one member is nonempty. A point of that member would admit an injection \(\kappa(t_i)\hookrightarrow\kappa(x)\), impossible since the distinct elements \(t_i\) already require cardinality at least \(|I|\). No such candidate exists. This proves the affine assertion with all the omitted fibre and flatness checks supplied.

There is also an obstruction over every nonempty scheme \(S\). Apply (10.4) to \(R=\mathbf Z\), obtaining \(\mathbf Z_I\), and base change its faithfully flat affine cover along \(S\to\operatorname{Spec}\mathbf Z\). Every residue field of \(\mathbf Z_I\) contains the rational function field in the \(t_i\) over its prime field. In characteristic \(p>0\) this is (10.5) for \((p)\). In characteristic zero, every nonzero rational-coefficient polynomial can be scaled to a primitive integral polynomial; its coefficients are not all divisible by any prime, so it belongs to \(D_I\). Hence the characteristic-zero fibre is \(\mathbf Q(t_i)\). At any point of a nonempty member factoring through \(S\times_{\mathbf Z}\operatorname{Spec}\mathbf Z_I\), one of these field embeddings therefore forces residue-field cardinality at least \(|I|\). A set of candidate covers of \(S\) again has a common cardinal bound, giving the same contradiction.

For \(S=\varnothing\), the empty family refines every family with that target, so it is a cofinal singleton collection; the nonempty hypothesis matters. In the convention of section 1, all \(\mathbb U\)-small fpqc covers form a set in \(\mathbb V\), so the site and the vanishing criterion are well-defined there. They generally have no \(\mathbb U\)-small cofinal subcollection: for such a subcollection its residue fields have a common bound in \(\mathbb U\), and Cantor's theorem supplies a still larger index set \(I\) in \(\mathbb U\) for the construction above. Thus the larger working universe resolves the size of the collection without erasing the obstruction inside the smaller universe.

## What this lesson does not prove

The algebraic and scheme-theoretic inputs are the equivalence between modules and quasi-coherent modules on affines, the pullback formula for those modules, flatness and its faithful detection properties, Nakayama's lemma, the affine characterization of finite presentation, the permanence facts for flat, étale, smooth and syntomic morphisms, and faithful flatness of Noetherian local completion. Most of them are proved in earlier lessons: faithful flatness in [Faithful flatness and the local criterion for flatness](course:AG-CA/AG-CA-08), Theorem 1.1; Nakayama's lemma in [Localization, local properties and support](course:AG-CA/AG-CA-02), Theorem 4.2; the affine characterization of finite presentation in [Finiteness of morphisms](course:AG-MO/AG-MO-02), Theorem 4.1; composition and base change of flat morphisms in [Flat morphisms](course:AG-FSE/AG-FSE-01), Proposition 2.1, of étale morphisms in [Étale morphisms and their local structure](course:AG-FSE/AG-FSE-04), Section 2, with Proposition 2.1 there for morphisms between étale schemes, and of smooth morphisms in [Smooth morphisms](course:AG-FSE/AG-FSE-05), Proposition 1.2; faithful flatness of completion in [Completion](course:AG-CA/AG-CA-19), Theorem 3.2. The same results are [Tag 00HP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ff), [Tag 00DV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-NAK), [Tag 01TQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-presentation-characterize), [Tag 01U7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-flat), [Tag 01U9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-flat), [Tag 02GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-etale), [Tag 02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale), [Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence), [Tag 01VA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-smooth), [Tag 01VB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-smooth) and [Tag 00MC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-faithfully-flat) of the Stacks project. Modules and quasi-coherent modules on affines, and the pullback formula, are cited from [Stacks, Tag 01IB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-equivalence-quasi-coherent) and [Tag 01I9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-widetilde-pullback), and syntomic morphisms from the references below.

We use without proof effective fpqc descent for quasi-coherent modules, including their maps, and universal descent of morphisms of schemes [Stacks, Tags 023T and 023Q]. We do prove the full augmented affine complex, the six covering axioms and inclusions, subcanonicity from that descent statement, the fpqc sheaf condition for \(\mathcal F^a\), affine vanishing, global comparison on arbitrary schemes, rank-one descent, Hilbert 90 and the big/small comparison here. The homological tools are precisely the vanishing criterion, Čech acyclicity of injectives, acyclic-resolution theorem, torsor interpretation of \(H^1\) and Leray from lesson 3.

The lesson does not construct a small fpqc site, claim universe independence for arbitrary fpqc coefficients, or identify the big and small étale topoi. Further structure of the small étale site and its points is the subject of the next lesson.

## References

- **[Stacks, topologies]** The Stacks Project Authors, *The Stacks Project*, [Tags 020L–020M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-procedure) for the general site construction; [Tags 020N–020O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-zariski), [0214–0215](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-etale), [021Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-smooth), [0224–0225](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-syntomic) and [021L–021M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-fppf) for the first five covering definitions. [Tags 022A–022C and 03L7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-fpqc) give the fpqc affine-refinement condition and inclusions. [Example 0H7E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-example-not-fpqc) is the gluing example in section 8; [Tags 022G–022H and 0BBK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-lemma-sheaf-property-fpqc) give the sheaf test and size obstruction. [Tag 022I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-section-change-alpha) discusses the partial-universe approach for the other topologies. Our explicit two-universe convention includes the fpqc site needed for Theorem 5.1.
- **[Stacks, descent]** [Tags 023F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-section-descent-modules), [023R–023T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-section-fpqc-descent-quasi-coherent) and [023P–023Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-section-fpqc-universal-effective-epimorphisms) are the exact descent prerequisites. They concern modules with descent data and descent of morphisms, and are used with that scope in section 3.
- **[Stacks, étale cohomology]** [Tags 03NV–03NW, 03O2–03O3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-fpqc) for the fpqc sheaf property; [Tags 03OF–03OG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-quasi-coherent) for \(\mathcal F^a\); [Tags 03OY–03P2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cohomology-quasi-coherent) for quasi-coherent comparison in the five ordinary big sites; [Tags 03P7–03P8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-picard-groups) for Hilbert 90; and [Tags 03X7–03YX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-big-small) and [03YZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-examples-sheaves) for big/small sites and sheaf examples. The affine contraction, global Leray proof, torsor inverses and exact-restriction proof used here are given in full above.
- **[Stacks, geometric prerequisites]** [Tags 01UC–01UI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-syntomic) for syntomic morphisms; [Tag 01UA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fppf-open) for openness of flat morphisms locally of finite presentation; [Tag 00MC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-faithfully-flat) for completion; and [Tag 03C4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-descend-properties-modules) for the generator-and-relation descent also proved in Lemma 6.1.

The linked AI Integrated Stacks Project reader contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
