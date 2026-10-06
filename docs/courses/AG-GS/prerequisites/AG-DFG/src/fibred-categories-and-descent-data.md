# Fibred categories and descent data

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A vector bundle can be described by vector bundles on open pieces and change-of-coordinate maps on their overlaps. The maps must agree after three pieces are compared. Two questions remain: does the local description produce a global bundle, and do compatible local maps produce a global map? Descent separates these questions and applies them to objects whose bases vary.

This lesson builds the language needed to ask those questions. We first study coherent restriction, then encode a local description, and finally construct the global quasi-coherent sheaf directly. We assume categories, natural transformations, fibre products of schemes, sheaves of modules, and the equivalence between modules over a ring and quasi-coherent sheaves on its affine scheme. Background on quasi-coherent sheaves belongs to *Schemes and sheaves*. The separate course [Categorical tools for analytic sheaves](https://kokunoyumeto.github.io/open-math-courses-public/courses/categorical-tools-for-analytic-sheaves/) studies categorical gluing on topological spaces; our base category consists of schemes, and the next lesson changes open coverings to faithfully flat coverings.

A basic reference is [Stacks], in the edition called AI Integrated Stacks Project Stacks. We use its strongly cartesian convention. Categories and schemes are taken in fixed universes; hom collections are sets, and a larger universe is allowed for categories of functors. This makes the constructions below legitimate without identifying a proper class with a set.

## 1. What restriction must remember

Let \(p:\mathcal E\to\mathcal C\) be a functor. Its fibre \(\mathcal E_U\) consists of objects mapped to \(U\) and morphisms mapped to \(\operatorname{id}_U\). A morphism in a fibre is called vertical.

Suppose \(f:V\to U\) and \(x\in\mathcal E_U\). A candidate restriction is an arrow \(\lambda:y\to x\) over \(f\). To behave as a pullback, it must solve the following problem for every \(z\): an arrow \(a:z\to x\) and an arrow \(h:p(z)\to V\) satisfying \(p(a)=fh\) should determine exactly one arrow \(b:z\to y\) over \(h\) with \(\lambda b=a\).

**Definition 1.1.** An arrow with this property is **strongly cartesian**. The functor \(p\) is a **fibred category** if such an arrow exists for every \(x\) and every \(f:V\to p(x)\). We write a chosen one as

\[
\lambda_{f,x}:f^*x\longrightarrow x.
\]

Equivalently, the function

\[
\operatorname{Hom}_{\mathcal E}(z,y)\longrightarrow
\operatorname{Hom}_{\mathcal E}(z,x)
\times_{\operatorname{Hom}_{\mathcal C}(p(z),U)}
\operatorname{Hom}_{\mathcal C}(p(z),V)
\]

given by \(b\mapsto(\lambda b,p(b))\) is bijective. The qualifier “strongly” means that test objects may lie over any base, rather than only over \(V\).

**Proposition 1.2.** Strongly cartesian arrows compose. Two strongly cartesian lifts of the same \(f\) with the same target have a unique vertical isomorphism commuting with their arrows to that target. A strongly cartesian arrow over an identity is an isomorphism.

**Proof.** For \(z\xrightarrow{\mu}y\xrightarrow{\lambda}x\), factor a test arrow to \(x\) uniquely through \(\lambda\), then factor the resulting arrow uniquely through \(\mu\). These two factorizations give exactly the universal property for \(\lambda\mu\).

For two lifts \(y\to x\) and \(y'\to x\), factor each arrow through the other over \(\operatorname{id}_V\). The composites are identities because the universal property gives only one endomorphism over \(\operatorname{id}_V\) that preserves the arrow to \(x\). This also proves uniqueness. For a lift over an identity, apply its universal property to \(\operatorname{id}_x\) to obtain an inverse; uniqueness verifies both inverse equations. More generally the same argument applies to a strongly cartesian arrow over any base isomorphism. \(\square\)

Choose all lifts, taking identity lifts to be identities. Such a choice is a **cleavage**. If \(a:x\to x'\) is vertical, define \(f^*a\) by

\[
\lambda_{f,x'}f^*a=a\lambda_{f,x}.
\]

Uniqueness proves that this assignment preserves identities and compositions, so \(f^*:\mathcal E_U\to\mathcal E_V\) is a functor. A cleavage selects representatives of pullbacks; it does not make iterated representatives equal.

For \(W\xrightarrow gV\xrightarrow fU\), the composite of the two chosen lifts is cartesian. Proposition 1.2 therefore gives a natural isomorphism

\[
c_{g,f}:g^*f^*\xrightarrow{\sim}(fg)^*.
\]

Naturality follows by composing either proposed naturality square with the cartesian arrow to \(x'\): both resulting arrows coincide, so their unique factorizations coincide. For a third arrow \(h:T\to W\), coherence says

\[
c_{h,fg}\circ h^*(c_{g,f})
=c_{gh,f}\circ(c_{h,g}f^*)
\quad\text{on }h^*g^*f^*.
\tag{1.1}
\]

Both sides are the unique isomorphism to \((fgh)^*\) compatible with the composite cartesian lift to \(x\), proving the equation. With our normalized cleavage, the comparisons involving an identity are identities. Without normalization there are unit isomorphisms \(\operatorname{id}\simeq(\operatorname{id}_U)^*\), and the same uniqueness argument proves the two unit equations.

An assignment of categories and pullback functors with these natural comparisons and unit equations is a contravariant **pseudofunctor**. Equation (1.1) is the associativity constraint. Omitting it would leave no assurance that a calculation with four bases is independent of its parenthesization.

## 2. Recovering a fibred category and making restrictions strict

Start with a normalized pseudofunctor \(F\). Form a category whose objects are pairs \((U,x)\), with \(x\in F(U)\). An arrow from \((V,y)\) to \((U,x)\) is a pair

\[
(f,a),\qquad f:V\to U,\quad a:y\to f^*x.
\]

For \((g,b):(W,z)\to(V,y)\), set

\[
(f,a)\circ(g,b)
=\bigl(fg,\ c_{g,f}(x)\circ g^*(a)\circ b\bigr).
\tag{2.1}
\]

Naturality of \(c\) and equation (1.1) make the two expansions of a triple composite equal. Identity arrows are \((\operatorname{id},\operatorname{id})\). Projection to \(\mathcal C\) is a functor, and \((f,\operatorname{id}):(V,f^*x)\to(U,x)\) is strongly cartesian: a test arrow over \(fh\) factors by applying \(c_{h,f}^{-1}\) to its vertical component. The factorization is unique because \(c_{h,f}\) is an isomorphism. This is the **Grothendieck construction**.

**Theorem 2.2.** A fibred category, together with a cleavage, is equivalent over \(\mathcal C\) to the Grothendieck construction of its pullback pseudofunctor.

**Proof.** Send \((U,x)\) to \(x\) and send \((f,a)\) to \(\lambda_{f,x}a\). Every arrow over \(f\) factors in exactly this way, so the functor is bijective on hom sets and surjective on objects. The defining equation of \(c_{g,f}\) shows that it respects (2.1). It preserves cartesian arrows, since the distinguished cartesian arrows go to chosen lifts, and every cartesian arrow differs from a distinguished one by a vertical isomorphism. It is therefore an equivalence as a fibred category. Changing the cleavage gives the same equivalence through the original category. \(\square\)

An equivalence of fibred categories means an equivalence over the base that preserves strongly cartesian arrows. More generally, such arrow-preserving functors are the 1-morphisms of their 2-category; natural transformations over the identity of the base are its 2-morphisms. Under Theorem 2.2 they become functors between the fibres equipped with compatible isomorphisms commuting with pullback. The compatibility is the same equation as (1.1), now with the functors inserted. This explains why ordinary natural transformations of strict functors are too rigid for arbitrary pullback choices.

There is a stronger replacement theorem. It changes the category rather than insisting that previously chosen pullbacks become equal.

**Theorem 2.3 (strictification).** Every fibred category is equivalent over \(\mathcal C\) to the fibred category of a strict contravariant functor to categories.

**Proof.** For \(U\), let \(H(U)\) be the category of cartesian sections on the slice \(\mathcal C/U\). Concretely, a section assigns to \(a:T\to U\) an object \(s(a)\) over \(T\). A slice arrow \(b:(T,a)\to(T',a')\), meaning \(a=a'b\), is sent to a strongly cartesian arrow \(s(a)\to s(a')\) over \(b\). The assignment is a functor. Morphisms of sections are natural transformations whose components are vertical.

For \(f:V\to U\), restriction means precomposition by

\[
\mathcal C/V\longrightarrow\mathcal C/U,
\qquad (a:T\to V)\longmapsto fa.
\]

These functors compose exactly and preserve identities exactly. Consequently \(H\) is a strict contravariant functor.

Evaluation at \(\operatorname{id}_U\) is an equivalence \(H(U)\to\mathcal E_U\). To see essential surjectivity, choose cartesian lifts of all arrows \(a:T\to U\) with target \(x\). For a slice arrow \(b\), define its image as the unique factorization between these lifts. The factor is cartesian: to factor an arbitrary test arrow through it, first factor through the lift to \(x\), then use uniqueness through the other lift. Uniqueness also proves identities and compositions, producing a cartesian section with value \(x\) at the terminal object.

For full faithfulness, a vertical map between the values of two sections at \(\operatorname{id}_U\) extends uniquely to each \(a:T\to U\) by factoring through the cartesian arrow of the target section to its terminal value. The components commute with slice arrows by uniqueness. Conversely, naturality along the arrow from \(a\) to the terminal object forces these components, so evaluation is bijective on hom sets.

Finally the Grothendieck construction of \(H\) maps to \(\mathcal E\). An arrow represented by \(f:V\to U\) and a transformation \(s\to f^*t\) is sent to the composite

\[
s(\operatorname{id}_V)\longrightarrow t(f)
\longrightarrow t(\operatorname{id}_U).
\]

The second arrow is cartesian over \(f\). Every arrow in \(\mathcal E\) over \(f\) factors uniquely through it, and the resulting vertical map extends uniquely to a transformation of sections. Thus the functor is fully faithful on the entire categories, not just on their fibres. It is essentially surjective by the evaluation equivalences. Composition follows from naturality of transformations and functoriality of sections; cartesian arrows are preserved. This proves the theorem. \(\square\)

For statements of these equivalences, see [Stacks, Tags [02XO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-fibred), [02XW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-split-fibred-category), [004A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-fibred-strict)]. Strictification is useful for formal reasoning. The original geometric pullbacks remain preferable for computations.

## 3. Geometric examples and their morphisms

For schemes over schemes, an object over \(S\) is \(Y\to S\). A morphism over \(f:T\to S\) is a commutative square with top arrow \(Z\to Y\). A cartesian lift is

\[
Y\times_ST\longrightarrow Y.
\]

The universal property of the fibre product is precisely Definition 1.1. This is the target projection of the arrow category of schemes. The subcategory of finite étale morphisms is fibred because finite étale morphisms remain finite étale after base change. Morphisms in its fibres need not be invertible: a map from a two-point cover to a one-point cover is an example.

The subcategory of closed subschemes is also fibred. Its fibres have at most one morphism between any two objects: such a morphism exists exactly when one closed subscheme is contained in the other. Pullback of a closed subscheme is defined by extending its ideal. The statement uses the scheme structure of the inverse image, not merely its underlying closed subset.

For quasi-coherent sheaves, an object over \(S\) is \(\mathcal M\in\operatorname{QCoh}(S)\). A morphism over \(f:T\to S\) is a map

\[
\mathcal N\longrightarrow f^*\mathcal M.
\]

Composition uses the canonical comparison \(g^*f^*\simeq(fg)^*\). The distinguished arrow from \(f^*\mathcal M\) to \(\mathcal M\) has identity vertical component and is cartesian. Pullback preserves quasi-coherence. Notice the variance: this description is the fibred category for pullback, and it does not describe a direct-image functor.

If every fibre is a groupoid, the category is **fibred in groupoids**. Every arrow then factors as a cartesian lift preceded by a vertical isomorphism, so every arrow is cartesian. Conversely, cartesian arrows over identities are isomorphisms, so if every arrow is cartesian the fibres are groupoids.

If every fibre is a discrete category, there is a unique cartesian lift of each base arrow to a fixed target, since the unique comparison between two lifts must be an identity. The fibres therefore form an honest presheaf of sets. Conversely, the category of elements of a presheaf is fibred in sets. For a scheme \(Z\), the presheaf \(S\mapsto\operatorname{Hom}(S,Z)\) gives an example. The Yoneda lemma says that transformations from this presheaf to another presheaf \(P\) correspond to elements of \(P(Z)\): evaluate a transformation at \(\operatorname{id}_Z\), and recover its value on \(a:S\to Z\) by restriction along \(a\).

## 4. Comparing local objects on two and three bases

Fix maps \(u_i:U_i\to U\), and suppose their double and triple fibre products exist. Put

\[
U_{ij}=U_i\times_UU_j,
\qquad U_{ijk}=U_i\times_UU_j\times_UU_k.
\]

A **descent datum** consists of objects \(x_i\in\mathcal E_{U_i}\) and isomorphisms

\[
\theta_{ij}:p_i^*x_i\xrightarrow{\sim}p_j^*x_j
\quad\text{over }U_{ij}
\]

such that

\[
p_{jk}^*\theta_{jk}\circ p_{ij}^*\theta_{ij}
=p_{ik}^*\theta_{ik}
\quad\text{over }U_{ijk}.
\tag{4.1}
\]

The comparisons from Section 1 are understood in this equation. Each side has the first pullback as its source and the third pullback as its target. There is no assertion that their chosen representatives are literally equal before those comparisons are made.

Pulling (4.1) back along the triple diagonal shows \(\Delta_i^*\theta_{ii}\) is an invertible idempotent, hence the identity. Pulling it back along \(U_{ij}\to U_{iji}\), with the first and third coordinates equal, shows that the interchange pullback of \(\theta_{ji}\) is \(\theta_{ij}^{-1}\). These consequences explain how the triple equation includes the identity and inverse requirements. It does not force \(\theta_{ii}\) to be the identity on all of \(U_i\times_UU_i\).

A morphism of descent data consists of vertical arrows \(a_i:x_i\to y_i\) satisfying

\[
\eta_{ij}\circ p_i^*a_i=p_j^*a_j\circ\theta_{ij}.
\tag{4.2}
\]

These objects and morphisms form a category \(\operatorname{Desc}(\{U_i\to U\})\). A global object \(x\in\mathcal E_U\) gives a canonical datum by restriction and the pullback comparisons. A datum is **effective** if it is isomorphic to one obtained this way.

For a map \(V\to U\), replace \(U_i\) by \(U_i\times_UV\) and pull back all objects and comparisons. Equation (4.1) pulls back to the new triple products, proving that this is again a datum. The same operation applies to morphisms. For a refinement \(V_a\to U_{i(a)}\to U\), restrict \(x_{i(a)}\) to \(V_a\) and restrict \(\theta_{i(a),i(b)}\) to \(V_a\times_UV_b\). The cocycle gives its triple equation. Successive restrictions or refinements agree up to the canonical coherent comparisons; strictification makes them strict if needed.

For quasi-coherent sheaves, \(\theta_{ij}\) is an isomorphism of pullback modules. For schemes over the base it is an isomorphism

\[
Y_i\times_UU_j\xrightarrow{\sim}U_i\times_UY_j
\]

over \(U_{ij}\), satisfying the same equation after one more base change. In the case of one map \(U'\to U\), there is still a potentially nontrivial comparison on \(U'\times_UU'\). A one-member family does not dispense with descent information.

**Proposition 4.3.** For schemes over schemes, descent relative to a family \(\{U_i\to U\}\) is equivalent to descent relative to the single map \(U'=\coprod_iU_i\to U\).

**Proof.** An \(U'\)-scheme \(Y'\) decomposes into the open-and-closed inverse images \(Y_i\) of the components \(U_i\); conversely, their disjoint union is an \(U'\)-scheme. Moreover,

\[
U'\times_UU'=\coprod_{i,j}U_{ij},
\qquad
U'\times_UU'\times_UU'=\coprod_{i,j,k}U_{ijk}.
\]

An isomorphism on the double product is therefore exactly a family of isomorphisms \(\theta_{ij}\), and its cocycle is exactly (4.1) on every component of the triple product. Equation (4.2) is componentwise as well. Decomposition and disjoint union are inverse functors up to their canonical identifications. Taking a family with one member gives precisely the ordinary single-morphism definition. The same argument works for quasi-coherent sheaves because quasi-coherent sheaves on a disjoint union are families of quasi-coherent sheaves on the components. For a general fibred category that last property is an additional hypothesis; it does not follow merely from being fibred. \(\square\)

## 5. When local descriptions constitute a stack

For \(x,y\in\mathcal E_U\), define the morphism presheaf on \(\mathcal C/U\) by

\[
(f:V\to U)\longmapsto
\operatorname{Hom}_{\mathcal E_V}(f^*x,f^*y).
\]

The pullback comparisons define its restriction maps. We call \(\mathcal E\) a **prestack** if each of these presheaves is a sheaf for the chosen coverings. We call it a **stack** if, in addition, every descent datum for a covering is effective. These are the conventions of [Stacks, Tag 026F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/stacks.html#stacks-definition-stack); they allow noninvertible arrows.

**Theorem 5.1.** A fibred category is a stack if and only if its restriction functor

\[
\mathcal E_U\longrightarrow
\operatorname{Desc}(\{U_i\to U\})
\tag{5.1}
\]

is an equivalence for every covering.

**Proof.** For global \(x,y\), an arrow between their descent data is exactly a collection of local arrows satisfying (4.2), hence a matching family in the morphism presheaf. The sheaf condition asserts that it has a unique global arrow. Thus the prestack condition is exactly full faithfulness of (5.1), with the same argument on every slice base. Effectivity is exactly essential surjectivity. A fully faithful, essentially surjective functor is an equivalence. The converse recovers those two conditions from the equivalence. \(\square\)

In categories fibred in groupoids all vertical arrows are isomorphisms, so one can use isomorphism sheaves. For general fibred categories that replacement is false. Here is an explicit example. Let \(U\) be the disjoint union of two points. To every nonempty open subset assign a category with one object and endomorphism monoid \((\mathbf N,+)\). Assign the terminal category to the empty set. Restrictions between nonempty opens are identities on the monoid. This is a strict presheaf of categories and hence gives a fibred category on the open subsets of \(U\). Its only invertible endomorphism is \(0\), so all isomorphism presheaves are one-point sheaves. All object descent data are effective, since every transition is the identity and there is one object on each base. Yet the endomorphism \(0\) on the first point and \(1\) on the second point cannot be the restrictions of one global natural number. Its morphism presheaf is not a sheaf, and (5.1) is not full.

Effectivity alone does not assert uniqueness of global maps. The distinction is essential for \(\operatorname{QCoh}\), whose fibre categories have many noninvertible arrows.

## 6. Constructing the glued quasi-coherent sheaf

Let \(S=\bigcup_iU_i\) be an arbitrary open covering. On intersections the two pullbacks are restrictions, so write the descent maps as

\[
\theta_{ij}:\mathcal M_i|_{U_i\cap U_j}
\xrightarrow{\sim}\mathcal M_j|_{U_i\cap U_j}.
\]

For every open \(W\subseteq S\), define

\[
\mathcal M(W)=
\left\{(m_i)_i\in\prod_i\mathcal M_i(W\cap U_i):
\theta_{ij}(m_i)=m_j\text{ on }W\cap U_i\cap U_j\right\}.
\tag{6.1}
\]

Restrictions are componentwise. Sections of \(\mathcal O_S(W)\) act by their restrictions on the components. The \(\mathcal O_S\)-linearity of \(\theta_{ij}\) ensures that the matching condition is preserved.

**Theorem 6.2 (Zariski descent).** Formula (6.1) defines a quasi-coherent \(\mathcal O_S\)-module with the prescribed restrictions and transition maps. Restriction gives an equivalence between \(\operatorname{QCoh}(S)\) and quasi-coherent descent data for \(\{U_i\to S\}\). There is no finiteness assumption on the covering or on the modules.

**Proof.** First verify the sheaf axioms. If two matching tuples agree after restriction to an open cover of \(W\), their \(i\)-components agree after restriction to the induced open cover of \(W\cap U_i\). The sheaf axiom for \(\mathcal M_i\) makes those components equal. Conversely, matching tuples given on an open cover of \(W\) glue in every \(\mathcal M_i\). Their glued components still satisfy the transition equations because those equations hold on a cover of every double intersection. Thus they form a tuple in (6.1), proving existence and uniqueness of gluing.

For \(W\subseteq U_j\), projection to the \(j\)-component gives a map \(\mathcal M(W)\to\mathcal M_j(W)\). Its inverse sends \(m_j\) to the tuple whose \(i\)-component on \(W\cap U_i\) is \(\theta_{ji}(m_j)\). The cocycle makes this tuple matching, and \(\theta_{jj}=\operatorname{id}\) on an open intersection makes the constructions inverse. Consequently \(\mathcal M|_{U_j}\simeq\mathcal M_j\); these identifications induce exactly \(\theta_{ij}\).

For completeness, quasi-coherence means local presentation by sheaves associated to modules on affine opens. Near any point choose \(j\), then an affine neighbourhood inside \(U_j\) on which \(\mathcal M_j\) has that form. The restriction isomorphism gives the same presentation for \(\mathcal M\). Thus \(\mathcal M\) is quasi-coherent. This argument uses the local definition and requires neither an affine total space nor a finite cover.

Compatible local maps \(a_i:\mathcal M_i\to\mathcal N_i\) send a matching tuple \((m_i)\) to \((a_i(m_i))\), which is matching by (4.2). They therefore define a global sheaf map. A global map is uniquely determined by its restrictions, since sections of the target are determined on a cover. The construction is inverse to restriction on both objects and morphisms: for a global sheaf the usual sheaf axiom identifies its sections with (6.1). Hence restriction is an equivalence. \(\square\)

This proves both effectivity and morphism gluing, so \(\operatorname{QCoh}\) is a Zariski stack. The result agrees with [Stacks, Tag 023E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-zariski-descent-effective).

Scheme-valued Zariski descent is effective too. Given schemes \(Y_i\to U_i\), identify their open inverse images of the overlaps by the transition isomorphisms. The cocycle makes these identifications an equivalence relation. Give the quotient the topology in which a subset is open when its inverse image in every \(Y_i\) is open. Each \(Y_i\) embeds as an open subset: overlap identifications show its inverse image in any other piece is open, and identity and inverse equations make its map injective. Glue the structure sheaves by the matching-section construction. The resulting locally ringed space is locally a scheme because every point has an open neighbourhood in some \(Y_i\); it is therefore a scheme. The maps to the \(U_i\) glue to a map to \(S\). Compatible morphisms of the pieces glue uniquely, first as continuous maps and then as maps of structure sheaves. This construction proves existence and full faithfulness for scheme-valued open descent as well.

## 7. A local restriction can lose a global object

Work over a field \(k\). Cover \(\mathbf P^1_k\) by \(U_0=\operatorname{Spec}k[t]\) and \(U_\infty=\operatorname{Spec}k[t^{-1}]\). Their overlap is \(\operatorname{Spec}k[t,t^{-1}]\). Choose frames \(e_0,e_\infty\) and the identification

\[
e_\infty=t e_0.
\tag{7.1}
\]

Glue the trivial modules with this rule. In the tautological line in \(k^2\), the local frames \((1,t)\) and \((t^{-1},1)\) satisfy \((1,t)=t(t^{-1},1)\). Their dual frames satisfy (7.1); thus the glued line bundle is \(\mathcal O(1)\).

It cannot be globally trivial. A change of frame on \(U_0\) multiplies by a unit of \(k[t]\), hence by a nonzero constant. The same is true on \(U_\infty\). These changes cannot turn the transition \(t\) into \(1\). A global trivialization would give exactly such two changes of frames, which is impossible.

The full fibred subcategory of globally trivial line bundles is a Zariski prestack: maps between two such bundles are maps between their underlying sheaves, and these glue uniquely. It is not a stack, because the datum (7.1) is locally in the subcategory but its effective object in \(\operatorname{QCoh}\) is not globally trivial. One must distinguish a local property, such as being a line bundle, from a global property, such as admitting one global frame.

As a positive example, on \(\operatorname{Spec}k[x,y]\) glue \(\mathcal O\) on \(D(x)\) and \(D(y)\) by the identity. Formula (6.1) produces \(\mathcal O\) on \(D(x)\cup D(y)\). The union need not be affine; Zariski descent concerns the union scheme and does not require it to be the spectrum of its global sections.

## 8. Exercises

**Exercise 8.1 (easy).** In a category fibred in groupoids, prove that every arrow is strongly cartesian. Explain why this does not imply that every arrow in the total category is an isomorphism.

**Exercise 8.2 (medium).** Write out the two parenthesizations of a triple composite in (2.1). Locate the naturality equation and the associativity constraint that make them equal. Recover the pullback pseudofunctor from the resulting fibred category.

**Exercise 8.3 (medium).** For each integer \(d\), glue trivial lines on the two standard affine opens of \(\mathbf P^1_k\) by \(e_\infty=t^d e_0\). Determine which of these descent data are effective inside the subcategory of globally trivial line bundles. Verify the prestack condition for that subcategory.

**Exercise 8.4 (medium).** In formula (6.1), replace the \(\mathcal M_i\) by quasi-coherent algebras and the transition maps by algebra isomorphisms. Prove that the result is a quasi-coherent algebra and that compatible algebra homomorphisms glue uniquely.

**Exercise 8.5 (hard).** Prove the family-to-single-map equivalence for schemes, including the triple product and the morphisms of data. Give a fibred category for which the same assertion fails without an additional disjoint-union property.

### Solutions

**8.1.** Factor an arrow \(a:y\to x\) over \(f\) through a chosen cartesian lift \(f^*x\to x\). Its vertical factor \(y\to f^*x\) lies in a groupoid, hence is an isomorphism. An isomorphism is cartesian, and a composite of cartesian arrows is cartesian by Proposition 1.2. A cartesian arrow over a noninvertible base arrow need not be invertible: in the category of elements of the terminal presheaf, the total category is the base category itself and every arrow is cartesian.

**8.2.** Use arrows with vertical components \(a:y\to f^*x\), \(b:z\to g^*y\), and \(d:w\to h^*z\). Composing the first two and then the third gives the vertical component

\[
c_{h,fg}(x)\,h^*c_{g,f}(x)\,h^*g^*a\,h^*b\,d.
\]

Composing the last two first gives

\[
c_{gh,f}(x)\,(gh)^*a\,c_{h,g}(y)\,h^*b\,d.
\]

Naturality of \(c_{h,g}\) moves \((gh)^*a\) across \(c_{h,g}(y)\), replacing that portion by \(c_{h,g}(f^*x)h^*g^*a\). Equation (1.1) identifies the remaining two initial comparison maps. Distinguished lifts \((f,\operatorname{id})\) give the original pullback categories and functors. Their composite differs from the distinguished lift for \(fg\) by exactly \(c_{g,f}\), recovering the comparison isomorphisms as well.

**8.3.** A global trivialization would change both frames by nonzero constants, turning \(t^d\) into a constant. In \(k[t,t^{-1}]\), this happens only when \(d=0\). Conversely the identity transition for \(d=0\) glues to the globally trivial line. For arbitrary globally trivial line bundles on any base, compatible local maps glue as sheaf maps; the global map is still a morphism between the given trivial bundles. This proves full faithfulness of restriction and hence the prestack property, while \(d=1\) proves failure of effectivity in this subcategory.

**8.4.** Add and multiply tuples componentwise. Because the transitions preserve multiplication and the unit, the result remains matching and gives a sheaf of algebras. Its restriction to each \(U_i\) is the prescribed algebra, by the inverse to projection in Theorem 6.2. Its underlying module is therefore quasi-coherent. Compatible algebra maps glue by the tuple construction; the algebra identities are local identities of sections and hence hold globally. Uniqueness follows from uniqueness for sheaf maps.

**8.5.** Decompose an \(\coprod_iU_i\)-scheme by inverse images of the components. Decompose its double base change by pairs \((i,j)\); an isomorphism on that base change is exactly the family \(\theta_{ij}\). Decompose the triple base change by triples \((i,j,k)\); equality of the two composites is precisely the cocycle on each triple. The commuting equations for a morphism likewise decompose by pairs. The inverse functor takes disjoint unions, proving equivalence. For failure in a general fibred category, use the category of open subsets of a two-point scheme \(U\). Assign a discrete two-object category to every nonempty open and the terminal category to the empty open. Restrictions between nonempty opens are identity functors; restrictions to the empty open are unique. This is a strict contravariant functor. On the cover by the two points, the two local objects can be chosen independently, giving four descent data. Their cross comparisons exist uniquely on the empty overlap. For the single map \(U=\coprod_iU_i\to U\), descent is instead the discrete two-object category: the cocycle forces its one transition to be the identity. The two descent categories are not equivalent. Thus fibredness alone does not supply the disjoint-union equivalence.

## What this lesson does not prove

We use the existence and universal property of fibre products of schemes, the local definition of quasi-coherence and its preservation by pullback, and the equivalence between modules and quasi-coherent sheaves on an affine scheme. These are the results of *Schemes and sheaves*: [Stacks, Tags [01JO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-fibre-products), [01BE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-definition-quasi-coherent), [01BG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-pullback-quasi-coherent), [01IB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-equivalence-quasi-coherent)]. Stability of finite étale morphisms under base change is a result of *Flat, smooth and étale morphisms*: [Stacks, Tags [01WL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-finite), [02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale)]. We do not develop stackification, gerbes, or the general theory of sites. All descent assertions and categorical replacement assertions used in this lesson are proved above.

## References

- **[Stacks]** The Stacks Project, *Categories*, sections on fibred categories and presheaves of categories; *Stacks*, descent data and stacks; *Descent*, descent of quasi-coherent sheaves and schemes. Tags [02XK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-cartesian-over-C), [02XO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-fibred), [004A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-fibred-strict), [026F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/stacks.html#stacks-definition-stack), [023E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-zariski-descent-effective), and [023X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-family-is-one). AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions; it is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
