# Galois categories

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite cover can be studied through its finite fibre. The fibre forgets the geometry, but its symmetries remember how different fibres fit together. A Galois category packages the operations on finite covers that make this recovery possible. Its group is recovered from natural automorphisms of the fibre functor, with a topology that records all finite observations.

We use basic category theory, finite Galois theory and compactness of products of finite discrete spaces. Covering-space classification will be an explicitly stated input in the topological example. We use the usual universe convention for products indexed by objects and pass to representatives of isomorphism classes when constructing inverse systems.

## 1. Finite actions and the topology of a fibre functor

A **profinite group** is a topological group isomorphic to an inverse limit of finite discrete groups. It is compact and Hausdorff, and the kernels of its finite-coordinate maps form a basis of open normal subgroups at the identity. Conversely a closed subgroup of a product of finite groups is the inverse limit of its images in finite subproducts: compatible coordinates give a point of the product, and closedness puts it in the subgroup. These facts explain both compactness and separation by finite quotients in the arguments below.

For a topological group \(G\), a **finite continuous \(G\)-set** is a finite set with a left \(G\)-action, whose stabilizers are open. This is equivalent to continuity of \(G\times E\to E\) with \(E\) discrete. Let \(\operatorname{Fin}(G)\) denote their category and \(\omega_G\) its forgetful functor.

Every such action has an open normal subgroup of finite index in its kernel: take the intersection of the stabilizers of its finitely many elements. Write

\[
\widehat G=\varprojlim_N G/N,
\tag{1.1}
\]

where \(N\) runs over open normal subgroups of finite index. This is the profinite completion of the topological group. For an abstract group we use its discrete topology. If \(G\) is already profinite, \(G\to\widehat G\) is an isomorphism. Injectivity follows because finite quotients separate points. For surjectivity, a compatible family of cosets is a family of closed subsets of the compact space \(G\) with the finite intersection property. It has a point in its intersection. The resulting continuous bijection is a homeomorphism, since its source is compact and target Hausdorff.

**Lemma 1.1.** The forgetful functor identifies

\[
\operatorname{Aut}(\omega_G)\simeq\widehat G
\tag{1.2}
\]

as topological groups. [Stacks, Tag 0BMU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-single-out-profinite)

*Proof.* On the left regular \(G\)-set \(G/N\), every right translation is \(G\)-equivariant. Naturality forces an automorphism \(\alpha\) of the forgetful functor to commute with all these right translations. It is therefore left multiplication by the element

\[
g_N=\alpha_{G/N}(N)\in G/N.
\]

Naturality for \(G/N'\to G/N\) makes the elements \(g_N\) compatible. Thus \(\alpha\) determines an element of (1.1).

Conversely, a compatible family \((g_N)\) acts on every finite continuous \(G\)-set \(E\): choose \(N\) acting trivially on \(E\), and act by \(g_N\). This does not depend on the choice, since the intersection of two possible \(N\)'s maps to both. It is natural in \(E\). The two constructions are inverse. In particular, an automorphism is completely determined by its action on the regular quotients, rather than by an arbitrary permutation of each fibre.

The topology on natural automorphisms is pointwise agreement on finitely many finite fibres. Every \(E\) is acted on by some finite quotient \(G/N\), so its coordinate action is continuous for the inverse-limit topology. Conversely the coordinate on \(G/N\) recovers \(g_N\). This proves the topological assertion. \(\square\)

More generally, if \(F:\mathcal C\to\operatorname{FinSets}\), define

\[
\operatorname{Aut}(F)\subset
\prod_{X\in\mathcal C}\operatorname{Sym}(F(X))
\tag{1.3}
\]

by the naturality equations \(\alpha_YF(f)=F(f)\alpha_X\). Each equation is closed in a product of finite discrete spaces. The subgroup (1.3) is therefore compact, Hausdorff and profinite, and its actions on all \(F(X)\) are continuous [Stacks, Tags [0BMR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-aut-inverse-limit), [0BMW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-example-from-C-F-to-G-sets)]. This is the topology we always use.

Finite limits and colimits in \(\operatorname{Fin}(G)\) are the usual finite-set constructions with their induced actions. For colimits, take the quotient of the finite disjoint union by the generated equivalence relation. A common open normal subgroup acts trivially on all the finitely many inputs, and hence on the construction. Thus all these actions remain continuous. The functor \(\omega_G\) is exact and reflects isomorphisms. Its connected objects, in the sense defined below, are precisely nonempty transitive \(G\)-sets.

We will need uniqueness of the finite fibre functor, not just (1.2).

**Proposition 1.2.** Every exact functor \(T:\operatorname{Fin}(G)\to\operatorname{FinSets}\) is naturally isomorphic to \(\omega_G\). [Stacks, Tag 0BMV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-second-fundamental-functor)

*Proof.* Exactness sends the terminal object to a singleton and the initial object to the empty set. If \(E\ne\varnothing\), the pushout of \(1\leftarrow E\to1\) is \(1\). If \(T(E)\) were empty, its image pushout would have two elements. Thus \(T(E)\ne\varnothing\).

For \(Q=G/N\), diagonal left translation splits \(Q\times Q\) into \(|Q|\) orbits, each isomorphic to \(Q\). Exactness gives

\[
|T(Q)|^2=|Q|\,|T(Q)|,
\]

so \(|T(Q)|=|Q|\). The right translations act freely on \(T(Q)\): for a nonidentity right translation, the equalizer with the identity is empty, and \(T\) preserves that equalizer. They therefore act transitively as well.

Maps \(G/N'\to G/N\) are epimorphisms. An exact functor preserves them here: the fold map \(Q\amalg_{Q'}Q\to Q\) is an isomorphism, and its image fold map can be an isomorphism only if \(T(Q')\to T(Q)\) is surjective. Hence the sets \(T(G/N)\) form a surjective inverse system of nonempty finite sets. Compactness gives a compatible family \(t_N\).

For \(e\in E\), choose \(N\) acting trivially on \(E\) and let \(f_e:G/N\to E\) send \(N\) to \(e\). Define

\[
\eta_E(e)=T(f_e)(t_N).
\tag{1.4}
\]

Refining to an intersection shows independence of \(N\), and composition with a \(G\)-map proves naturality. On \(G/N\), (1.4) is a bijection because the right translations move \(t_N\) freely through all \(|G/N|\) elements.

For a transitive set \(G/H\), choose \(N\subset H\), open and normal. It is the quotient of \(G/N\) by the right translations from \(H/N\). Both functors preserve this finite coequalizer, so the bijection for \(G/N\) induces a bijection for \(G/H\). Every finite \(G\)-set is a finite disjoint union of transitive ones; preservation of coproducts completes the proof. \(\square\)

## 2. The axioms and their immediate force

An object \(X\) of a category with an initial object \(0\) is **connected** if \(X\not\simeq0\) and every monomorphism into \(X\) is either an isomorphism or has initial source.

A **Galois category** is a pair \((\mathcal C,F)\), with \(F:\mathcal C\to\operatorname{FinSets}\), satisfying:

1. \(\mathcal C\) has finite limits and finite colimits.
2. Every object is a finite, possibly empty, coproduct of connected objects.
3. \(F\) is exact: it preserves finite limits and finite colimits.
4. \(F\) reflects isomorphisms.

These are the Stacks axioms [Stacks, Tag 0BMY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-definition-galois-category). We use this one axiom system throughout; we do not silently exchange it for another formulation from SGA 1.

**Proposition 2.1.** In a Galois category:

- \(F\) is faithful.
- A map is monic exactly when its fibre map is injective, and epic exactly when its fibre map is surjective.
- \(F(X)=\varnothing\) exactly when \(X\) is initial, and \(|F(X)|=1\) exactly when \(X\) is terminal.
- A map between connected objects is epic.
- Two maps from a connected object agree if their fibre maps agree on one element.
- A map from a connected object to a coproduct of connected objects lands in one summand.

*Proof.* If \(F(a)=F(b)\), their equalizer has the same fibre as their source. Reflection of isomorphisms makes the equalizer the whole source, so \(a=b\).

A map \(p:X\to Y\) is monic if and only if its diagonal \(X\to X\times_YX\) is an isomorphism. Applying \(F\) and reflection of isomorphisms gives the injectivity assertion. Dually, \(p\) is epic if and only if the fold map \(Y\amalg_XY\to Y\) is an isomorphism. Indeed epicness makes the two maps \(Y\to Y\amalg_XY\) equal, and then either is inverse to the fold; the converse follows from the pushout universal property. Exactness and reflection therefore give the surjectivity assertion.

The unique maps \(0\to X\) and \(X\to1\), together with \(F(0)=\varnothing\) and \(F(1)=\{*\}\), prove the initial and terminal assertions.

Suppose \(X,Y\) are connected and \(p:X\to Y\). The equalizer of the two maps \(Y\rightrightarrows Y\amalg_XY\) contains the image of \(X\), so its fibre is nonempty. It is a noninitial subobject of \(Y\), hence all of \(Y\). The two maps are equal; thus \(p\) is epic.

For maps \(a,b:X\to Y\) agreeing on a fibre element, their equalizer is a subobject of connected \(X\) with nonempty fibre. It is therefore \(X\). Finally, pull back each summand of a coproduct along a map from \(X\). These are subobjects of \(X\), hence initial or all of \(X\). On fibres they partition the nonempty set \(F(X)\), so precisely one is all of \(X\). This proves the last assertion. [Stacks, Tag 0BN0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-epi-mono) \(\square\)

The summand inclusions in a connected decomposition are monic, since their fibre maps are injective. In fact every subobject of \(X=\coprod X_i\) is a union of these summands: pull it back to each \(X_i\), use connectedness, and apply \(F\) and reflection to the resulting coproduct map. This proves uniqueness of the connected decomposition up to reordering and isomorphism.

For a connected \(X\), the group \(\operatorname{Aut}_{\mathcal C}(X)\) acts freely on \(F(X)\). An automorphism fixing one element is the identity by Proposition 2.1. Hence it is finite, of order at most \(|F(X)|\). Call \(X\) **Galois** if this action is transitive, and consequently simply transitive.

**Proposition 2.2 (Galois domination).** Every connected object admits an epimorphism from a Galois object. [Stacks, Tag 0BN2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-galois)

*Proof.* Let \(n=|F(X)|\), and list all fibre elements as \(x_1,\ldots,x_n\). Choose the connected component \(Y\subset X^n\) containing that ordered tuple.

Every tuple in \(F(Y)\) has pairwise distinct coordinates. Otherwise two coordinate maps \(Y\to X\) agree at a fibre element. Proposition 2.1 makes them equal everywhere, contradicting the distinct coordinates of the original tuple.

Permutations of coordinates act on \(X^n\) and permute its connected components. Given two tuples in \(F(Y)\), each lists every element of \(F(X)\), so a coordinate permutation takes one tuple to the other. This permutation preserves \(Y\): its image component and \(Y\) have a common fibre element, whereas distinct components have disjoint fibres. Its restriction is an automorphism of \(Y\). Thus automorphisms act transitively on \(F(Y)\), making \(Y\) Galois. Any coordinate projection \(Y\to X\) is a map of connected objects and hence epic. \(\square\)

## 3. Reconstructing every object and every map

Put \(\Pi=\operatorname{Aut}(F)\), with the topology (1.3). Naturality makes \(F\) a functor

\[
\mathcal C\longrightarrow\operatorname{Fin}(\Pi).
\tag{3.1}
\]

The central issue is that the action of all natural automorphisms is large enough to move any point of a connected fibre to any other point.

**Lemma 3.1.** For connected \(X\), \(\Pi\) acts transitively on \(F(X)\). Moreover \(\Pi\) is recovered from finite automorphism groups of Galois objects.

*Proof.* Choose a representative \(Y_i\) of each isomorphism class of Galois objects, and choose \(y_i\in F(Y_i)\). Order the classes by \(i\ge j\) when a map \(Y_i\to Y_j\) exists. It can be uniquely normalized to send \(y_i\) to \(y_j\): postcompose by an automorphism of \(Y_j\), then use the one-point uniqueness of Proposition 2.1. Denote this map \(p_{ij}\). The normalized maps compose as \(p_{jk}p_{ij}=p_{ik}\).

This is a directed partially ordered set. Maps both ways imply equal finite fibre sizes and therefore isomorphisms. For directedness, take a connected component of \(Y_i\times Y_j\), dominate it by a Galois object, and project to the two factors. Normalization gives the required two pointed maps.

Evaluation gives a natural bijection

\[
F(X)\simeq\varinjlim_i\operatorname{Hom}_{\mathcal C}(Y_i,X),
\qquad f\longmapsto F(f)(y_i).
\tag{3.2}
\]

For injectivity, compare two maps at a common dominating \(Y_k\); equality at \(y_k\) implies equality everywhere. For surjectivity, choose the connected component containing the desired point of \(F(X)\), dominate it by a Galois object, and precompose the domination map by an automorphism moving its chosen point to a suitable lift.

Write \(A_i=\operatorname{Aut}_{\mathcal C}(Y_i)\). For \(i\ge j\), every \(a\in A_i\) has a unique partner \(\rho_{ij}(a)\in A_j\) with

\[
p_{ij}a=\rho_{ij}(a)p_{ij}.
\tag{3.3}
\]

Choose the partner by its value at \(y_j\); equality then follows by checking at \(y_i\). Equation (3.3) proves that \(\rho_{ij}\) is a homomorphism and that transition homomorphisms compose. It is surjective, since \(F(p_{ij})\) is surjective and \(A_i,A_j\) act simply transitively on their fibres.

Let \(A=\varprojlim A_i\). Every projection \(A\to A_i\) is surjective. To justify this even for a large directed index set, fix a desired coordinate in \(A_i\). Any finitely many compatibility conditions can be solved at a common dominating index, using surjectivity onto \(A_i\). These conditions define closed subsets of a product of finite groups with the finite intersection property, so compactness supplies a compatible family.

Precomposition in (3.2) now gives an action of \(A^{\mathrm{op}}\) on \(F\). The opposite group is essential for this convention:

\[
(f\circ b)\circ a=f\circ(ba).
\]

The action is natural. On \(F(Y_i)\), it is the right regular action after identifying a point \(F(c)(y_i)\) with \(c\in A_i\). Surjectivity of \(A\to A_i\) makes this action transitive. Every connected \(X\) is an epic image of some \(Y_i\), so the induced action on \(F(X)\) is transitive too.

In fact

\[
\Pi\simeq\varprojlim_i A_i^{\mathrm{op}}.
\tag{3.4}
\]

For a natural automorphism \(\alpha\), let \(a_i\) be the unique element of \(A_i\) with \(F(a_i)(y_i)=\alpha_{Y_i}(y_i)\). Naturality for \(p_{ij}\) gives compatibility of these coordinates. Naturality for every map in (3.2) shows that precomposition by \((a_i)\) recovers \(\alpha\), proving bijectivity in (3.4).

Continuity follows because the action on any point of any finite \(F(X)\) is computed at one stage of (3.2); finitely many points use finitely many stages. A continuous bijection between these compact Hausdorff groups is a homeomorphism. One may replace all the opposite groups in (3.4) by \(A_i\) using inversion, provided the corresponding inverse convention is retained in the actions. [Stacks, Tag 0BN3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-tame) \(\square\)

**Theorem 3.2 (the Galois-category theorem).** The functor (3.1) is an equivalence. It sends connected components to \(\Pi\)-orbits, and Galois objects to regular finite quotients of \(\Pi\). [Stacks, Tag 0BN4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-galois)

*Proof.* Connected components have transitive fibres by Lemma 3.1, and their inclusions are \(\Pi\)-equivariant. Thus the connected components of any object correspond exactly to the orbits of its fibre.

Faithfulness is Proposition 2.1. To prove fullness, let \(s:F(X)\to F(Z)\) be a \(\Pi\)-equivariant map. Its graph is an invariant subset of \(F(X)\times F(Z)=F(X\times Z)\), hence a union of orbits. The corresponding union \(W\) of connected components of \(X\times Z\) has fibre equal to this graph. Its projection to \(X\) is a bijection on fibres, so is an isomorphism. Composing its inverse with \(W\to Z\) produces a morphism whose fibre map is \(s\). This proves fullness.

For essential surjectivity, it suffices to realize each transitive finite set \(\Pi/H\), with \(H\) open. By the definition of the topology, finitely many objects \(X_1,\ldots,X_r\) have a common fibre-action kernel contained in \(H\). Replace them by their connected components. Galois domination gives a Galois object \(Y\) mapping epically to every resulting connected object: choose a component of their product and dominate it.

The transitive \(\Pi\)-set \(F(Y)\) is \(\Pi/N\) for the stabilizer of a chosen point. Its automorphism group in \(\mathcal C\) acts transitively on \(F(Y)\) and commutes with \(\Pi\). All point stabilizers for \(\Pi\) are therefore equal, so \(N\) is normal. The action on \(F(Y)\) is the regular action of \(\Pi/N\). Since its maps onto all \(F(X_j)\) are surjective, \(N\) acts trivially on them. Hence \(N\subset H\).

Fullness already proved identifies \(\operatorname{Aut}_{\mathcal C}(Y)\) with the group of right translations of \(\Pi/N\), namely \((\Pi/N)^{\mathrm{op}}\). Let \(M\) be the subgroup of these automorphisms given by \(H/N\). Form the quotient object \(Y/M\) as the finite coequalizer of all the automorphisms in \(M\) and the identity. Exactness gives

\[
F(Y/M)=(\Pi/N)/(H/N)=\Pi/H
\]

as a left \(\Pi\)-set. Finite coproducts realize an arbitrary finite continuous \(\Pi\)-set. This completes the equivalence and the assertion about Galois objects. \(\square\)

The theorem proves that no extra maps or finite actions have been lost. Exactness supplies the quotient objects; connectedness supplies the orbit structure; reflection of isomorphisms turns fibrewise graphs into actual morphisms.

## 4. Functors become homomorphisms, in the reverse direction

Let \(T:(\mathcal C,F)\to(\mathcal D,E)\) be an exact functor. Write
\(\Pi_{\mathcal C}=\operatorname{Aut}(F)\) and
\(\Pi_{\mathcal D}=\operatorname{Aut}(E)\).

**Theorem 4.1.** There is a natural isomorphism \(t:E\circ T\simeq F\). Choosing it gives a continuous homomorphism

\[
a:\Pi_{\mathcal D}\longrightarrow\Pi_{\mathcal C},
\qquad
a(g)_X=t_Xg_{T(X)}t_X^{-1}.
\tag{4.1}
\]

Under the equivalences of Theorem 3.2, \(T\) is restriction of finite actions along \(a\). Changing \(t\) conjugates \(a\) by an element of \(\Pi_{\mathcal C}\). Conversely every continuous \(a\) produces such an exact functor. [Stacks, Tag 0BN5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-functoriality-galois)

*Proof.* Transport \(E\circ T\) across \(\mathcal C\simeq\operatorname{Fin}(\Pi_{\mathcal C})\). It is an exact functor with finite values, so Proposition 1.2 supplies \(t\). Formula (4.1) is natural in \(X\) and is a homomorphism. Its coordinate on \(F(X)\) depends only on the coordinate of \(g\) at \(T(X)\), so it is continuous.

The map \(t_X\) identifies the fibre of \(T(X)\) with \(F(X)\) carrying the restricted action. This gives the asserted functor identification on both objects and maps. Two choices of \(t\) differ by a natural automorphism \(c\) of \(F\), and replacing \(t\) by \(ct\) replaces \(a\) by \(cac^{-1}\). Conversely restriction of actions preserves all finite limits and colimits, since their underlying finite-set constructions are unchanged. Transport it across the two equivalences to obtain \(T\). \(\square\)

In particular, taking \(T\) to be the identity of \(\mathcal C\) shows that any two finite exact fibre functors on it are naturally isomorphic. The resulting isomorphism of their groups depends on that natural isomorphism only up to inner conjugation.

We now prove the group-theoretic tests that will make this translation useful. A continuous image of a profinite group is compact and hence closed in a profinite target. Finite quotients separate a point from a closed subgroup \(K\): if \(g\notin K\), choose an open normal \(N\) with \(gN\cap K=\varnothing\). Then \(KN\) is a proper open subgroup containing \(K\) and excluding \(g\). In particular,

\[
K=\bigcap_{H\supset K,\ H\ \mathrm{open}}H.
\tag{4.2}
\]

**Theorem 4.2 (surjectivity).** For \(a\) and \(T\) above, these conditions are equivalent:

1. \(a\) is surjective.
2. \(T\) is fully faithful.
3. \(T\) sends connected objects to connected objects.
4. If \(X\) is connected and \(T(X)\) has a map from the terminal object of \(\mathcal D\), then \(X\) has a map from the terminal object of \(\mathcal C\).
5. For every \(X\), \(T\) induces a bijection between its sets of maps from the respective terminal objects.

*Proof.* Use Theorem 4.1 to identify \(T\) with restriction of actions, and put \(K=a(\Pi_{\mathcal D})\). If \(a\) is surjective, equivariant maps, orbits and fixed points are all unchanged. This proves conditions 2, 3 and 5. Condition 5 implies 4.

Condition 3 also implies 4: a fixed point in a transitive set makes that set a singleton. The fibre of \(X\) then has one element, so \(X\) is terminal and has the required map. Condition 2 implies 5 because \(T\) preserves the terminal object.

If \(K\ne\Pi_{\mathcal C}\), choose a proper open subgroup \(H\supset K\) using (4.2). The transitive set \(\Pi_{\mathcal C}/H\) has more than one element and no \(\Pi_{\mathcal C}\)-fixed point, but its identity coset is fixed by \(K\). Thus condition 4 fails. Conditions 2, 3 or 5 therefore also force surjectivity by the implications already proved. [Stacks, Tag 0BN6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-functoriality-galois-surjective) \(\square\)

The use of compactness is important: for an arbitrary abstract group map, preservation of finite orbits can only detect density in the appropriate profinite completion.

**Theorem 4.3 (injectivity).** The homomorphism \(a\) is injective if and only if every connected \(Z\in\mathcal D\) admits a diagram

\[
Z\ \longleftarrow\ W\ \longrightarrow\ T(X),
\tag{4.3}
\]

with the left map epic and the right map monic, for some \(X\in\mathcal C\).

*Proof.* Suppose \(a\) is injective. It identifies \(\Pi_{\mathcal D}\) homeomorphically with a closed subgroup of \(\Pi_{\mathcal C}\). Write the transitive fibre of \(Z\) as \(\Pi_{\mathcal D}/H\). Choose an open normal subgroup \(N\subset\Pi_{\mathcal C}\) with \(a^{-1}(N)\subset H\), using the induced topology. Inside the restricted \(\Pi_{\mathcal C}\)-set \(\Pi_{\mathcal C}/N\), the orbit of the identity coset is

\[
\Pi_{\mathcal D}/a^{-1}(N).
\]

It is a subobject and maps surjectively to \(\Pi_{\mathcal D}/H\). The equivalences of Theorem 3.2 turn these maps into (4.3).

Conversely any element of \(\ker a\) acts trivially on every restricted set \(T(X)\), hence on each of its subobjects and quotients. Condition (4.3) makes it act trivially on every transitive finite \(\Pi_{\mathcal D}\)-set. Apply this to \(\Pi_{\mathcal D}/N'\) for every open normal \(N'\). Finite quotients separate points, so the element is the identity. [Stacks, Tag 0BN7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-functoriality-galois-injective) \(\square\)

Call an object **trivial** if it is a finite coproduct of terminal objects. Its group action is trivial. Suppose now that a second exact functor \(U:\mathcal D\to\mathcal E\) gives

\[
\Pi_{\mathcal E}\xrightarrow{b}
\Pi_{\mathcal D}\xrightarrow{a}
\Pi_{\mathcal C}.
\tag{4.4}
\]

Then \(ab=1\), the trivial homomorphism, exactly when \(U\circ T\) sends every object to a trivial object. One implication is immediate from restriction of actions. For the other, if an element of the composite image were nonidentity, a finite regular quotient of \(\Pi_{\mathcal C}\) would detect its nontrivial action. This proves the composition test [Stacks, Tag 0BS8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-composition-trivial). The composite is \(U\circ T\), which has domain \(\mathcal C\); \(T\circ U\) is generally not defined.

**Theorem 4.4 (the closed normal kernel test).** The following are equivalent:

1. \(a\) is surjective, \(ab\) is trivial, and \(\ker a\) is the smallest closed normal subgroup of \(\Pi_{\mathcal D}\) containing \(b(\Pi_{\mathcal E})\).
2. \(T\) is fully faithful, and \(Y\in\mathcal D\) belongs to its essential image exactly when \(U(Y)\) is trivial.
3. \(T\) is fully faithful, \(U\circ T\) sends every object to a trivial object, and every \(Y\) with \(U(Y)\) trivial admits an epimorphism \(T(X)\to Y\).

*Proof.* Theorem 4.2 and the composition test make \(a\) surjective and \(ab\) trivial under either categorical condition. Put

\[
L=\overline{\langle g\,b(\Pi_{\mathcal E})\,g^{-1}
\mid g\in\Pi_{\mathcal D}\rangle}.
\]

It is a closed normal subgroup of \(\ker a\). A finite \(\Pi_{\mathcal D}\)-set has trivial restricted \(\Pi_{\mathcal E}\)-action exactly when its action kernel contains \(L\). It comes from a finite \(\Pi_{\mathcal C}\)-set exactly when its action kernel contains \(\ker a\). In the latter assertion continuity of the factored action follows from the quotient topology of the compact surjection \(a\).

If \(L=\ker a\), the two classes of sets coincide, proving condition 2. Conversely, under condition 2, apply this coincidence to each regular quotient

\[
\Pi_{\mathcal D}/(LN'),
\qquad N'\subset\Pi_{\mathcal D}
\text{ open and normal}.
\]

Its restricted \(\Pi_{\mathcal E}\)-action is trivial, so \(\ker a\subset LN'\) for all \(N'\). The intersection of these open subgroups is \(L\), by the same closed-subgroup separation argument as (4.2). Thus \(\ker a=L\).

Condition 2 implies 3 by taking an object representing \(Y\). Under condition 3, \(\ker a\) acts trivially on \(T(X)\), and therefore on its epic image \(Y\). Hence every \(Y\) with trivial \(U(Y)\) is in the essential image. The converse direction follows from the triviality of \(U\circ T\), giving condition 2. [Stacks, Tag 0BS9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-functoriality-galois-ses) \(\square\)

This theorem tests a **closed normal closure**, rather than equality with the image of \(b\). For ordinary exactness in the middle, we still need the following condition.

**Theorem 4.5 (normality).** The closed subgroup \(b(\Pi_{\mathcal E})\) is normal in \(\Pi_{\mathcal D}\) if and only if, for every connected \(Y\in\mathcal D\), a map from the terminal object to \(U(Y)\) implies that \(U(Y)\) is trivial.

*Proof.* Put \(K=b(\Pi_{\mathcal E})\). If \(K\) is normal and fixes one point in a transitive \(\Pi_{\mathcal D}\)-set, it fixes all its translates: for \(k\in K\),

\[
k(gx)=g(g^{-1}kg)x=gx.
\]

Thus the whole restricted action is trivial.

Conversely let \(H\) be any open subgroup of \(\Pi_{\mathcal D}\) containing \(K\). The identity coset in \(\Pi_{\mathcal D}/H\) is \(K\)-fixed. The asserted condition makes every coset \(K\)-fixed, so

\[
g^{-1}Kg\subset H\qquad\text{for every }g.
\]

Intersect over all open \(H\supset K\), using (4.2), to obtain \(g^{-1}Kg\subset K\). Replace \(g\) by its inverse to get equality. This proves normality. [Stacks, Tag 0BTS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-functoriality-galois-normal) \(\square\)

Consequently (4.4), followed by \(\Pi_{\mathcal C}\to1\), is exact in the ordinary sense exactly when Theorem 4.4's categorical conditions and Theorem 4.5's normality condition both hold. If one also places \(1\) at the left, Theorem 4.3 supplies the additional injectivity condition. These distinctions will prevent a normal-generation statement from being mistaken for the full homotopy exact sequence.


## 5. Fields and spaces

### 5.1. Finite étale algebras over an arbitrary field

Fix a field \(K\) and a separable closure \(K^s\). Let \(\mathcal C_K\) be the **opposite** of the category of finite étale \(K\)-algebras, including the zero algebra. Its fibre functor is

\[
F_K(A)=\operatorname{Hom}_{K\text{-alg}}(A,K^s).
\tag{5.1}
\]

The opposite is necessary: an algebra map \(B\to A\) induces the fibre map \(F_K(A)\to F_K(B)\). Equivalently, we are studying finite étale schemes over \(\operatorname{Spec}K\). The zero algebra represents the empty scheme.

We use the field-theory prerequisites that a finite étale algebra is a finite product of finite separable field extensions [Stacks, Tag 02GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-over-field), and that a finite separable extension has a primitive element [Stacks, Tag 030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element). Thus every finite étale algebra becomes a finite product of copies of \(L\) over some finite Galois extension \(L/K\) in \(K^s\). Indeed take a finite splitting field for the finitely many separable minimal polynomials of its factors. The Chinese remainder theorem then gives

\[
L\otimes_K A\simeq
\prod_{e\in F_K(A)}L,
\qquad \ell\otimes a\longmapsto(\ell e(a))_e.
\tag{5.2}
\]

All embeddings \(e\) in this formula have image in the chosen \(L\).

Write \(G_K=\operatorname{Gal}(K^s/K)\). It is the inverse limit of the finite groups \(\operatorname{Gal}(L/K)\) over finite Galois subextensions, with its **Krull topology**. To see the inverse-limit identification directly, \(K^s\) is the union of these \(L\)'s. A compatible family of their automorphisms defines a field automorphism of the union; its compatible inverses define the inverse. Restrictions between finite Galois groups are surjective by finite Galois theory. Compactness of the surjective finite inverse system also shows that every coordinate projection from \(G_K\) is surjective. This constructs the profinite topology without using the categorical theorem to assume the desired answer.

**Theorem 5.1.** The functor (5.1), with the action \(g\cdot e=g\circ e\), is an equivalence

\[
\mathcal C_K\simeq\operatorname{Fin}(G_K).
\tag{5.3}
\]

Consequently \((\mathcal C_K,F_K)\) is a Galois category and
\(\operatorname{Aut}(F_K)\simeq G_K\) as profinite groups. [Stacks, Tag 03QR, restricted to finite objects](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-sheaves-point)

*Proof.* The action is continuous, since the finite set of embeddings is fixed by the subgroup fixing a suitable finite Galois \(L/K\).

Conversely let \(E\) be a finite continuous \(G_K\)-set. Its action factors through \(Q=\operatorname{Gal}(L/K)\) for some finite Galois subextension: its action kernel is open, and the kernels of the finite coordinate projections form a neighbourhood basis. Give \(L^E\), the algebra of functions from \(E\) to \(L\), the semilinear action

\[
(q\cdot f)(e)=q\bigl(f(q^{-1}e)\bigr),
\qquad B_E=(L^E)^Q.
\tag{5.4}
\]

This is an action by semilinear algebra automorphisms. The Galois form of faithfully flat algebra descent, proved in *Faithfully flat descent*, gives the isomorphism

\[
L\otimes_K B_E\longrightarrow L^E,
\qquad \ell\otimes b\longmapsto \ell b.
\tag{5.5}
\]

Finite local freeness descends by that lesson, and étaleness descends by *Descending properties of schemes and morphisms*, Theorem 2.1. Hence \(B_E\) is finite étale over \(K\). Its fibre is \(E\): after base change to \(K^s\), (5.5) is \((K^s)^E\), whose algebra maps to \(K^s\) are precisely the coordinate evaluations. For \(b\in B_E\), invariance says

\[
b(qe)=q(b(e)).
\]

If \(g\in G_K\) restricts to \(q\in Q\), this identity shows that \(g\) sends the evaluation at \(e\) to the evaluation at \(qe\). The identification of the fibre with \(E\) is therefore equivariant, including when \(E\) is empty.

We also check every morphism. An equivariant map \(h:E\to E'\) gives the algebra map

\[
L^{E'}\longrightarrow L^E,\qquad f\longmapsto f\circ h.
\tag{5.6}
\]

It commutes with (5.4), so descends uniquely to \(B_{E'}\to B_E\). Conversely every unital \(L\)-algebra map \(L^{E'}\to L^E\) has form (5.6). For each coordinate of the target, the primitive idempotents of \(L^{E'}\) must map to zeros and ones, with exactly one mapping to one. Thus that coordinate selects exactly one element of \(E'\). Commutation with (5.4) is exactly equivariance of \(h\). The same argument treats empty sets, with the usual zero-algebra convention. Faithfully flat descent makes the descended algebra map unique.

For two finite étale algebras, choose a common finite Galois splitting field. Formula (5.2) identifies its canonical descent action with (5.4): acting on the tensor factor sends a function \(f\) to \(e\mapsto q(f(q^{-1}e))\). Hence (5.5) recovers the original algebra, and the preceding morphism argument proves full faithfulness as well as essential surjectivity. Enlarging the splitting field does not change this conclusion, since descent recovers the same original algebra and maps.

Under (5.3), the fibre functor is the forgetful functor. Section 1 and the axioms in Section 2 therefore verify all Galois-category axioms and identify its natural automorphism group with \(G_K\). In particular the identification is topological. \(\square\)

Connected objects here are the finite separable field extensions, viewed oppositely. Galois objects are precisely the finite Galois extensions. For the latter assertion, a field embedding \(A\to K^s\) is moved simply transitively by the automorphisms of \(A/K\) exactly when \(A/K\) is Galois. Equivalently, its stabilizer in \(G_K\) is normal, by Theorem 3.2. This recovers finite Galois theory inside the category of finite étale algebras.

**Example 5.2 (finite fields).** For \(K=\mathbf F_q\), the roots of \(X^{q^n}-X\) in an algebraic closure form a field of \(q^n\) elements. The derivative is \(-1\), so there are exactly \(q^n\) distinct roots. Closure under sums, products and inverses follows from the Frobenius identities. Call this field \(\mathbf F_{q^n}\).

Every degree-\(n\) extension of \(\mathbf F_q\) has \(q^n\) elements, all satisfying \(a^{q^n}=a\), so is this field up to \(\mathbf F_q\)-isomorphism. The automorphism \(a\mapsto a^q\) has order exactly \(n\): its \(n\)th power is the identity, while a smaller positive power \(d<n\) cannot fix all \(q^n\) elements, since \(X^{q^d}-X\) has degree \(q^d\). Finite Galois theory then gives

\[
\operatorname{Gal}(\mathbf F_{q^n}/\mathbf F_q)
\simeq\mathbf Z/n\mathbf Z.
\]

Restrictions send Frobenius to Frobenius. Every algebraic element lies in a finite extension, so

\[
G_{\mathbf F_q}\simeq\varprojlim_n\mathbf Z/n\mathbf Z
=\widehat{\mathbf Z}.
\tag{5.7}
\]

Arithmetic Frobenius corresponds to \(1\) and topologically generates the group. The finite separable algebras over \(\mathbf F_q\) are thus encoded by a finite set and one permutation. A cycle of length \(n\) corresponds to \(\mathbf F_{q^n}\); a disjoint union of cycles corresponds to the product of their fields. For a separably closed field, the same construction gives the trivial group and only products of copies of the field.

### 5.2. Finite topological covering spaces

Let \(X\) be nonempty, connected, locally path-connected and semilocally simply connected, and choose \(x\in X\). Local path-connectedness makes connectedness equivalent to path-connectedness. Semilocal simple connectivity means that every point has a neighbourhood whose loops become null-homotopic in \(X\).

Let \(\operatorname{Cov}_f(X)\) be the category of covering spaces of \(X\) with finite fibres, allowing the empty covering, and continuous maps over \(X\). Put \(\Gamma=\pi_1^{\mathrm{top}}(X,x)\), with the discrete topology. For loops, we multiply by traversing the first loop and then the second. If \(L_\gamma\) is endpoint transport along a lifted loop, then

\[
L_{\gamma\delta}=L_\delta L_\gamma.
\]

We therefore use the left action

\[
[\gamma]\cdot y=L_{\gamma^{-1}}(y)
\quad\text{on }p^{-1}(x).
\tag{5.8}
\]

This avoids turning a right action into a left action without changing the convention.

Here are the lifting facts used in (5.8). A path has a unique lift from a chosen starting point: subdivide its compact parameter interval into finitely many pieces mapping to evenly covered neighbourhoods, and lift successively on sheets. A homotopy of paths with fixed endpoints has constant lifted endpoints. One can subdivide its parameter square into small rectangles mapping to evenly covered neighbourhoods; on each rectangle the chosen sheet gives the lift, and uniqueness on common edges makes these local lifts agree. The endpoints lie in discrete fibres and vary continuously, so are constant. Thus (5.8) depends only on the loop class. These are the path and homotopy lifting statements of Hatcher, §1.3, Proposition 1.30.

**Theorem 5.3.** Fibre with action (5.8) is an equivalence

\[
\operatorname{Cov}_f(X)\simeq\operatorname{Fin}(\Gamma).
\tag{5.9}
\]

Consequently this is a Galois category, and its fibre-functor group is
\(\widehat{\pi_1^{\mathrm{top}}(X,x)}\), with its profinite topology.

*Proof.* A map over \(X\) commutes with path lifting by uniqueness, so its fibre map is equivariant. The orbits in a fibre are exactly the path components of its covering space: a path between two points over \(x\) projects to a loop, and every lifted loop is such a path. Each component meets the fibre over \(x\), since \(X\) is path-connected and one can lift a path from any base point to \(x\). The covering space is locally path-connected, so these components are also connected components and are open. A finite covering consequently has finitely many of them.

For a point \(y\in p^{-1}(x)\), its stabilizer \(H_y\) consists of the loop classes lifting to loops at \(y\). Indeed inverse transport fixes \(y\) exactly when forward transport does. Thus

\[
H_y=p_*\pi_1(Y_0,y),
\tag{5.10}
\]

where \(Y_0\) is its component. Its transitive fibre is \(\Gamma/H_y\).

We use the following classification input from Hatcher, §1.3, Theorem 1.38: under the stated hypotheses on \(X\), every subgroup \(H\subset\Gamma\) is realized by a pointed connected covering with subgroup \(H\), uniquely up to pointed isomorphism. Without a chosen point, isomorphism classes correspond to conjugacy classes of subgroups. The preceding orbit calculation shows that the number of sheets is \([\Gamma:H]\). It follows that every finite transitive \(\Gamma\)-set is a fibre of a finite connected covering. Disjoint unions realize all finite \(\Gamma\)-sets, including the empty one.

For completeness, the morphism correspondence does not follow merely from a bijection on isomorphism classes. Let \(h:p^{-1}(x)\to q^{-1}(x)\) be equivariant. On a connected component \(Y_0\), choose \(y\) over \(x\), and put \(z=h(y)\). Equivariance implies \(H_y\subset H_z\). For any \(y'\in Y_0\), choose a path \(\lambda\) from \(y\) to \(y'\) and define \(f(y')\) as the endpoint of the lift of \(p\lambda\) starting at \(z\).

If another path is chosen, their concatenation with one reversed projects to an element of \(H_y\subset H_z\). Its lift at \(z\) closes, so the two candidate endpoints agree. This defines \(f\) unambiguously. It is continuous: near \(y'\), choose a path-connected sheet neighbourhood over an evenly covered path-connected neighbourhood for both covers. Extend the chosen path by paths within this neighbourhood. There \(f\) is the composition of one sheet projection and the inverse of another, hence continuous. The construction is over \(X\) and agrees with \(h\) on the fibre, because every point of that fibre is reached by loop transport from \(y\). It is unique, since any map over \(X\) must send lifted paths from \(y\) to the prescribed lifted paths from \(z\).

Doing this on every open component produces the unique map realizing \(h\). We have proved full faithfulness and essential surjectivity. The axioms follow from the equivalence and Section 1; Lemma 1.1 identifies the group as the profinite completion of \(\Gamma\). No assumption that \(\Gamma\) embeds in that completion is needed. \(\square\)

This proof also explains deck transformations. The automorphism group of the transitive fibre \(\Gamma/H\) is \((N_\Gamma(H)/H)^{\mathrm{op}}\), acting by right translations; inversion identifies this opposite group with \(N_\Gamma(H)/H\). The cover is Galois exactly when \(H\) is normal. To check the normality assertion directly, right translations are transitive on \(\Gamma/H\) exactly when \(N_\Gamma(H)=\Gamma\). This is the finite-cover case of Hatcher, §1.3, Proposition 1.39.

**Example 5.4 (the circle).** The covering

\[
\mathbf R\longrightarrow S^1,\qquad t\longmapsto e^{2\pi i t}
\]

computes \(\pi_1(S^1,1)\simeq\mathbf Z\). A loop based at \(1\) lifts from \(0\) to an integer, and that integer is invariant under based homotopy. Concatenation adds these integers, since a lift of the second loop is translated by the endpoint of the first. Every integer occurs. If the endpoint is \(0\), the lift is a loop in \(\mathbf R\) and contracts there, so its projection contracts in \(S^1\). This proves the isomorphism, including injectivity.

Its finite-index subgroups are \(n\mathbf Z\), \(n\ge1\). The degree-\(n\) connected cover is

\[
S^1\longrightarrow S^1,\qquad z\longmapsto z^n,
\tag{5.11}
\]

because the induced map on the computed fundamental groups multiplies winding number by \(n\). Classification proves these are all connected finite covers. Arbitrary finite covers are their finite disjoint unions. Equivalently, a finite \(\mathbf Z\)-set is a finite set with one permutation; its cycles are the connected covers. Lemma 1.1 gives the fibre group \(\widehat{\mathbf Z}\). Under convention (5.8), a positive loop sends \(e^{2\pi i j/n}\) to \(e^{2\pi i(j-1)/n}\).

**Example 5.5 (the punctured complex line).** The homotopy

\[
H(z,s)=z\bigl((1-s)+s/|z|\bigr)
\]

retracts \(\mathbf C^\times\) onto \(S^1\), fixing \(S^1\). Its scalar factor is positive, so the homotopy never meets zero. It follows that \(\pi_1(\mathbf C^\times,1)=\mathbf Z\). The maps \(z\mapsto z^n\) on \(\mathbf C^\times\) are degree-\(n\) coverings: locally choose a continuous logarithm and the \(n\) resulting branches of the root. Their source is connected and their fundamental-group image is \(n\mathbf Z\). Theorem 5.3 and classification therefore give all connected finite covers, all Galois, and the fibre group \(\widehat{\mathbf Z}\).

**Example 5.6 (two circles joined at a point).** Write \(W=S^1\vee S^1\), with loops labelled \(a,b\). Its universal cover can be described using the free group \(F_2\) of reduced words in \(a^{\pm1},b^{\pm1}\). Put a vertex at every reduced word \(w\), an oriented edge labelled \(a\) from \(w\) to \(wa\), and an oriented edge labelled \(b\) from \(w\) to \(wb\). Projection sends every vertex to the joining point and every labelled edge around the corresponding circle. At every vertex the four half-edges project bijectively onto the four half-edges of \(W\), so this is a covering.

The graph is connected by reading words. It has no non-backtracking closed edge path: such a path would give a nonempty reduced word representing the identity. It is therefore a tree. Contract it along the unique paths to its identity vertex; equivalently its finite subtrees contract and every loop has image in a finite subtree. In this locally finite graph this proves simple connectivity. Loop lifting identifies \(\pi_1(W)\) with \(F_2\): endpoints are reduced words, all occur, concatenation is multiplication of words, and a loop with identity endpoint lifts to a contractible loop in the tree. Thus Theorem 5.3 gives

\[
\operatorname{Aut}(\text{fibre on }\operatorname{Cov}_f(W))
\simeq\widehat{F_2}.
\tag{5.12}
\]

A finite cover is specified by two arbitrary permutations \(\sigma_a,\sigma_b\) of a finite set \(E\). With the left convention (5.8), draw the \(a\)-edge from \(e\) to \(\sigma_a^{-1}(e)\) and the \(b\)-edge from \(e\) to \(\sigma_b^{-1}(e)\). There is one incoming and one outgoing edge of each label at each vertex, so the resulting graph covers \(W\). Its inverse loop transports are exactly the specified permutations. The graph is connected if and only if those two permutations generate a transitive action on \(E\). Maps of covers are exactly functions commuting with both permutations.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Compute the automorphism group of the forgetful functor on finite \(\mathbf Z\)-sets, including its topology.

*Solution.* The regular quotient \(\mathbf Z/n\mathbf Z\) has commuting translations. A natural automorphism must therefore be translation by an element \(c_n\). Naturality for reduction modulo divisors gives \(c_m\bmod n=c_n\) whenever \(n\mid m\). Thus it determines \((c_n)\in\widehat{\mathbf Z}\).

Conversely a finite \(\mathbf Z\)-set is a finite set with a permutation \(s\). Choose \(n\) divisible by all its cycle lengths, so \(s^n=1\), and let \((c_m)\) act as \(s^{c_n}\). Compatibility makes this independent of \(n\), and it commutes with every equivariant map. On the regular quotients it recovers the translations, so these constructions are inverse group homomorphisms. The coordinate action on each finite set factors through some \(\mathbf Z/n\mathbf Z\); conversely the regular quotient recovers that coordinate. Hence the topology is precisely the inverse-limit topology, not the discrete topology.

**Exercise 6.2 (medium).** Prove that every morphism between connected objects of a Galois category is epic.

*Solution.* Let \(f:X\to Y\), and form \(P=Y\amalg_XY\) with inclusions \(i_1,i_2\). Their equalizer \(Z\to Y\) is monic. Exactness identifies its fibre with the equalizer of the two maps from \(F(Y)\) into \(F(P)\). This set contains \(F(f)(F(X))\), which is nonempty since \(X\) is connected. Thus \(Z\) is not initial. Connectedness of \(Y\) makes \(Z\to Y\) an isomorphism, so \(i_1=i_2\).

If two maps \(u,v:Y\to A\) satisfy \(uf=vf\), the pushout property supplies \(P\to A\) restricting to \(u,v\). Equality of \(i_1,i_2\) forces \(u=v\). Therefore \(f\) is epic. This argument uses neither a chosen Galois cover nor the reconstruction theorem.

**Exercise 6.3 (medium).** Verify the Galois-category axioms for the opposite of finite étale \(K\)-algebras and identify its fibre-functor group.

*Solution.* Theorem 5.1 establishes an equivalence with \(\operatorname{Fin}(G_K)\), where \(G_K=\operatorname{Gal}(K^s/K)\), and identifies the fibre with the forgetful functor. Here is the verification of each axiom under that equivalence. Finite limits are the finite-set limits with induced action; finite colimits are the finite disjoint unions modulo the relations defining the colimit. For any finite diagram, a common open normal subgroup acts trivially on every input, so these constructions are continuous finite actions. Every finite action decomposes into its finitely many nonempty orbits; these are connected because a subobject is an invariant subset. The forgetful functor preserves all these constructions, so is exact. A map bijective on underlying sets has an equivariant inverse, so this functor reflects isomorphisms. All four axioms hold.

In algebra language connected components correspond to the separable field factors; the zero algebra is the initial object of the opposite category, and \(K\) its terminal object. A natural automorphism on the regular finite quotient attached to a finite Galois extension \(L/K\) is determined by one element of \(\operatorname{Gal}(L/K)\), as in Lemma 1.1. These elements are compatible under restriction. The inverse limit is \(G_K\), and the coordinate topology is the Krull topology. Thus the identification is an isomorphism of profinite groups, with the action on embeddings given by postcomposition. The use of the opposite category is essential for this covariant fibre functor.

**Exercise 6.4 (medium).** Show that finite coverings of \(\mathbf C\setminus\{0\}\) form a Galois category and compute its fibre-functor group.

*Solution.* The space is connected, locally path-connected and locally simply connected. Example 5.5 computes its fundamental group as \(\mathbf Z\) by the displayed retraction and the lifted-loop argument for the circle. Theorem 5.3 identifies its finite-cover category with finite sets equipped with one permutation. The four axioms follow exactly as in Exercise 6.3, replacing \(G_K\) by the discrete group \(\mathbf Z\). Exercise 6.1 identifies the group with \(\widehat{\mathbf Z}\) in its inverse-limit topology.

A transitive permutation is a single cycle of length \(n\). Its corresponding connected cover has subgroup \(n\mathbf Z\), and is represented by \(z\mapsto z^n\). All finite covers are finite disjoint unions of these. Their maps are the equivariant maps between cycles. Explicitly, a map from an \(m\)-cycle to an \(n\)-cycle exists exactly when \(n\mid m\), and is then specified by the image of one element, with \(n\) choices. For the power covers these are the maps \(z\mapsto\zeta z^{m/n}\), where \(\zeta^n=1\). This also verifies the morphism correspondence concretely.

**Exercise 6.5 (hard).** An exact functor \(T:(\mathcal C,F)\to(\mathcal D,E)\) induces \(a:\Pi_{\mathcal D}\to\Pi_{\mathcal C}\), up to conjugacy. Prove that \(a\) is surjective exactly when \(T\) sends connected objects to connected objects.

*Solution.* Theorem 4.1 identifies \(T\) with restriction of actions along \(a\). If \(a\) is surjective, its image moves every point of a transitive \(\Pi_{\mathcal C}\)-set to every other point, so restriction preserves transitivity and hence connectedness.

Conversely the image \(K=a(\Pi_{\mathcal D})\) is closed by compactness. Suppose it is proper and choose \(g\notin K\). There is an open normal \(N\subset\Pi_{\mathcal C}\) with \(gN\cap K=\varnothing\). Then \(H=KN\) is open, contains \(K\), and excludes \(g\), so is proper. The finite transitive set \(\Pi_{\mathcal C}/H\) has more than one point. Its identity coset is fixed by \(K\). The restricted action consequently has a singleton orbit and at least one other orbit, so is not transitive. The corresponding connected object of \(\mathcal C\) becomes disconnected in \(\mathcal D\), a contradiction. Thus \(K=\Pi_{\mathcal C}\), proving surjectivity. The closed-image step explains why the conclusion is actual surjectivity for profinite groups.

## 7. What this lesson does not prove

The reconstruction theorem, uniqueness of the finite exact fibre functor and all functoriality tests are proved above. The field example uses the earlier course proofs of faithfully flat algebra descent, finite local freeness and étale permanence. Its elementary field-theory inputs are the description of étale algebras over a field as products of finite separable extensions [Stacks, Tag 02GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-over-field), the primitive element theorem for finite separable extensions [Stacks, Tag 030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element), and finite Galois theory: the fixed-field correspondence for a finite Galois extension, the order formula [Stacks, Tag 09I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-finite-Galois) and extension of embeddings to a finite normal splitting field [Stacks, Tag 0BME](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-lift-maps). Existence of separable closures is also a field-theory prerequisite. None of these inputs is the infinite Galois-category equivalence being proved here.

The topological example imports classification of pointed connected coverings by subgroups under connectedness, local path-connectedness and semilocal simple connectivity; after forgetting the point, conjugacy classes replace subgroups [Hatcher, *Algebraic Topology*, §1.3, Theorem 1.38, pp. 67–68]. The proof above supplies the finite categorical equivalence, its morphism correspondence and its profinite group. Basic compactness of products of finite discrete spaces and the usual existence of finite limits and colimits of sets are background inputs.

For further study, Borceux, *Galois Theories of Fields and Rings*, Chapters 2–3, develops the finite algebra correspondence and the topology behind inverse limits. The next lesson, *The étale fundamental group*, applies this categorical theorem to finite étale coverings of a connected scheme. The geometric work is to establish the axioms there; the reconstruction then supplies the group and its finite actions.
