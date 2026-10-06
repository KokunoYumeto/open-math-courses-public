# Projective morphisms and Chow’s lemma

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A projective morphism comes with the possibility of embedding its source in a projective bundle over the base. Properness then follows from projective space, while ampleness explains when local projective coordinates can be assembled. Chow’s lemma goes in another direction: it replaces a separated finite-type scheme by a proper surjective modification that has projective coordinates, preserving a dense open part of the original scheme.

We use Proper morphisms, Very ample sheaves and embeddings, and Ample invertible sheaves. In particular projective space is already proper, arbitrary-module Segre embeddings are available, and the finite-type submodule theorem on qcqs schemes has an exact open proof provider. Our projective bundles use invertible quotients: \(\mathbf P(\mathcal E)=\operatorname{Proj}_S\operatorname{Sym}\mathcal E\). No local freeness of \(\mathcal E\) is implicit.

## 1. Projective bundles and properness

A morphism \(f:X\to S\) is **projective** if there are a finite-type quasi-coherent \(\mathcal E\) on \(S\) and a closed immersion \(X\hookrightarrow\mathbf P(\mathcal E)\) over \(S\). It is **H-projective** if there is a closed immersion into some \(\mathbf P^N_S\). It is **locally projective** if it becomes projective on the members of an open cover of \(S\). These are [Stacks, Tag 01W8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-projective). A quasi-projective morphism, as in the previous lesson, is of finite type and admits a relatively ample invertible sheaf.

**Theorem 1.1.** Every H-projective morphism is projective; every projective or locally projective morphism is proper. A projective morphism is quasi-projective.

**Proof.** Finite projective space is \(\mathbf P(\mathcal O_S^{N+1})\), giving the first assertion. For a finite-type quasi-coherent \(\mathcal E\), restrict to an affine base open \(V\). Its finite module of sections is a quotient of a finite free module, say \(\mathcal O_V^{r+1}\twoheadrightarrow\mathcal E|_V\). The induced symmetric-algebra quotient gives a closed immersion

\[
\mathbf P(\mathcal E)|_V\hookrightarrow\mathbf P^r_V.
\tag{1.1}
\]

On standard charts this is the spectrum of a surjective degree-zero localization map, so the closed-immersion assertion includes the scheme structure. Projective space is proper by the preceding properness lesson, and its closed subschemes are proper. Thus \(X_V\to V\) is proper. Properness is target-local, proving both the projective and locally projective assertions.

For projective \(f\), the tautological pullback \(\mathcal L\) is relatively very ample. The morphism is now known to be quasi-compact. Over each affine base open, Lemma 4.1 of *Ample invertible sheaves* makes \(\mathcal L\) ample. Hence it is \(f\)-ample, and \(f\) is of finite type because it is proper. This is quasi-projectivity. \(\square\)

The properness and quasi-projectivity assertions are [Stacks, Tags 01WC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-projective-proper) and [07RL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-projective-quasi-projective). Finite type of the module matters: an arbitrary projective bundle need not be proper.

This includes \(\mathbf P(\mathcal E)\to S\) for every finite locally free \(\mathcal E\). Its fibre at \(s\), for rank \(r+1\), is \(\mathbf P^r_{\kappa(s)}\). A finite-type module that is not locally free also gives a projective morphism, but its fibre dimensions can vary with the dimension of \(\mathcal E\otimes\kappa(s)\).

**Theorem 1.2.** A proper morphism admitting an \(f\)-ample invertible sheaf is locally projective. In fact, over each affine base open it is H-projective.

**Proof.** On \(V=\operatorname{Spec}A\subset S\), the previous lesson produces an immersion \(X_V\to\mathbf P^N_V\) from a sufficiently large power of \(\mathcal L|_{X_V}\). The source is proper over \(V\), and the target is separated over \(V\), so this map is proper. Its image is closed. An immersion with closed image is a closed immersion, proving H-projectivity over \(V\). These opens cover \(S\). \(\square\)

This is [Stacks, Tag 0B5N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-proper-ample-locally-projective). It is a local conclusion and should not be promoted to an unqualified global finite-space embedding.

## 2. Base change and the two composition theorems

**Theorem 2.1.** Projective, H-projective, and locally projective morphisms are stable under arbitrary base change. A composite of H-projective morphisms is H-projective, with no quasi-compactness assumption on the base.

**Proof.** Base change preserves a closed immersion and identifies the changed bundle with \(\mathbf P(h^*\mathcal E)\). Pullback preserves finite-type quasi-coherent modules. This proves projective stability; finite free modules give H-projective stability, and pulling back the target cover gives local stability.

For composition, suppose \(X\hookrightarrow\mathbf P^n_Y\) and \(Y\hookrightarrow\mathbf P^m_S\) are closed. Base change of the second closed immersion gives

\[
X\hookrightarrow\mathbf P^n_Y
\hookrightarrow\mathbf P^n_S\times_S\mathbf P^m_S
\hookrightarrow\mathbf P^{(n+1)(m+1)-1}_S.
\tag{2.1}
\]

The last map is Segre. Every arrow is closed, so their composite proves H-projectivity. \(\square\)

These are [Stacks, Tags 01WF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-H-projective-base-change), [02V6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-projective), and [01WE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-H-projective-composition).

For general projective morphisms, the first bundle's module lives on the intermediate scheme. Moving its generators to the final base is the extra step.

**Theorem 2.2.** If \(S\) is quasi-compact and quasi-separated and \(X\xrightarrow fY\xrightarrow gS\) are projective morphisms, then \(gf\) is projective.

**Proof.** Choose closed immersions \(X\hookrightarrow\mathbf P_Y(\mathcal E)\) and \(Y\hookrightarrow\mathbf P_S(\mathcal H)\), with both modules of finite type. Let \(\mathcal M\) on \(Y\) be the second tautological pullback. Theorem 1.1 makes it \(g\)-ample, and makes \(g\) proper. In particular \(Y\) is qcqs.

Choose a finite affine cover \(V_i\) of \(S\). The global-generation characterization of ampleness, applied on each \(Y_i=g^{-1}(V_i)\), says that \(\mathcal E\otimes\mathcal M^{\otimes n}\) is generated by its sections on \(Y_i\) for all sufficiently large \(n\). Take one bound across this finite cover. Since \(g\) is qcqs, its direct image

\[
\mathcal F_\infty=g_*(\mathcal E\otimes\mathcal M^{\otimes n})
\]

is quasi-coherent, and the evaluation \(g^*\mathcal F_\infty\to\mathcal E\otimes\mathcal M^{\otimes n}\) is surjective.

Use the qcqs finite-type submodule theorem on \(S\): \(\mathcal F_\infty\) is the directed union of finite-type quasi-coherent submodules. Some finite-type submodule \(\mathcal F\) still surjects after pullback. To justify that selection, at each point of \(Y\) finitely many germs suffice to generate the finite-type target module, and all come from one member of the directed union. The resulting generation locus is open, since the cokernel is of finite type. Quasi-compactness of \(Y\) selects finitely many such loci, and directedness selects one submodule containing their finite choices. Thus

\[
g^*\mathcal F\twoheadrightarrow\mathcal E\otimes\mathcal M^{\otimes n}.
\tag{2.2}
\]

Twisting by an invertible sheaf leaves the projective bundle unchanged: tensoring an invertible quotient of \(\mathcal E\) with \(\mathcal M^{\otimes n}\) is a bijection with the quotients of the twisted module, functorially on test schemes. Consequently (2.2) supplies closed immersions

\[
X\hookrightarrow\mathbf P_Y(\mathcal E)
\cong\mathbf P_Y(\mathcal E\otimes\mathcal M^{\otimes n})
\hookrightarrow Y\times_S\mathbf P_S(\mathcal F)
\hookrightarrow\mathbf P_S(\mathcal H)\times_S\mathbf P_S(\mathcal F).
\tag{2.3}
\]

The arbitrary-module Segre embedding of the eighth lesson embeds the last product into \(\mathbf P_S(\mathcal H\otimes\mathcal F)\). Its module is finite type and quasi-coherent. This is the required projective embedding of \(X\) over \(S\). \(\square\)

The theorem has the precise hypotheses of [Stacks, Tag 0C4P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-projective). Its finite-submodule ingredient is the full open proof at [Tag 01PG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-coherent-colimit-finite-type), already used in the ampleness lesson. The proof explains exactly where quasi-compactness and quasi-separatedness of the final base enter. The simpler H-projective theorem does not need that step or those hypotheses.

## 3. When an ample base supplies finite projective coordinates

**Theorem 3.1.** If \(S\) admits an ample invertible sheaf, every projective morphism to \(S\) is H-projective.

**Proof.** Write \(X\hookrightarrow\mathbf P_S(\mathcal E)\), with \(\mathcal E\) finite type, and let \(\mathcal A\) be ample on \(S\). The ampleness criterion says \(\mathcal E\otimes\mathcal A^{\otimes n}\) is globally generated for large \(n\). Quasi-compactness of \(S\) selects finitely many global generators, giving a quotient \(\mathcal O_S^{N+1}\twoheadrightarrow\mathcal E\otimes\mathcal A^{\otimes n}\). It induces a closed immersion into \(\mathbf P^N_S\). Twist invariance of the projective bundle identifies its source with \(\mathbf P_S(\mathcal E)\), so composing with \(X\)'s closed immersion proves the claim. \(\square\)

This is the projective assertion of [Stacks, Tag 087S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-projective-over-quasi-projective-is-H-projective). In particular it applies to affine bases, whose structure sheaf is ample. The twist can change the tautological invertible sheaf while leaving the scheme unchanged; the theorem claims an embedding, not preservation of a previously specified \(\mathcal O(1)\).

A closed subscheme of a quasi-projective \(S\)-scheme is quasi-projective: its map to \(S\) is of finite type, and the ample sheaf restricts to an ample sheaf on each affine-base inverse image. Similarly a closed subscheme of a projective \(S\)-scheme is projective, by composition with its closed embedding into the original bundle. We will meet a further class in *Blowing up*, the sixteenth lesson: for a finite-type quasi-coherent ideal \(\mathcal I\), the Rees algebra is generated in degree one by \(\mathcal I\), so its blow-up embeds in \(\mathbf P_S(\mathcal I)\). The blow-up construction, charts and universal property will be proved there; this bundle implication is already the homogeneous-quotient argument of (1.1).

## 4. Chow’s lemma over a Noetherian base

We first record how schematic closures retain information that a reduced closure would discard. For a quasi-compact immersion \(U\to T\) into a Noetherian scheme, its **scheme-theoretic closure** is defined by

\[
\mathcal I=\ker(\mathcal O_T\to j_*\mathcal O_U).
\tag{4.1}
\]

The ideal is quasi-coherent by the qcqs pushforward fact. Its closed subscheme has underlying space \(\overline{U}\), and \(U\) is open in it: inside an open where the immersion is closed, (4.1) recovers that closed subscheme. The map from the closure's structure sheaf into \(j_*\mathcal O_U\) is injective. We call this **scheme-theoretic density** of \(U\). The construction commutes with restriction to opens, directly from (4.1).

If two maps from such a closure to a separated scheme agree on \(U\), they agree everywhere. Their equalizer is a closed subscheme; its defining ideal vanishes on \(U\), so injectivity of the structure-sheaf map makes that ideal zero. This is the version of the equalizer argument appropriate to possibly nonreduced schemes.

**Theorem 4.1 (Chow’s lemma).** Let \(S\) be Noetherian and \(X\to S\) separated and of finite type. There exist a proper surjection \(\pi:X'\to X\), a quasi-compact immersion \(X'\to\mathbf P^N_S\), and a dense open \(U\subset X\) such that \(\pi^{-1}(U)\to U\) is an isomorphism.

**Proof.** All schemes in the construction are Noetherian. The finitely many irreducible components of \(X\) have generic points \(\eta_1,\ldots,\eta_r\). Every point \(x\) has an affine neighbourhood containing all these generic points. Indeed, choose an affine neighbourhood \(W\) avoiding the components that do not contain \(x\); it contains the generic points of all components through \(x\). For each remaining component choose an affine neighbourhood of its generic point avoiding every other component. These extra opens are disjoint from \(W\) and from one another. Their finite disjoint union with \(W\) is affine and has the required points. Quasi-compactness now gives a finite affine cover \(U_1,\ldots,U_m\) with every generic point in every member. Their intersection \(U\) is dense and open.

Replace \(X\) temporarily by the scheme-theoretic closure \(X^*\) of \(U\) in \(X\). Its map to \(X\) is a surjective closed immersion and is an isomorphism on \(U\). The intersections \(U_i\cap X^*\) remain affine and cover it. Thus a solution for \(X^*\) gives one for \(X\), and we may assume \(U\) scheme-theoretically dense in \(X\).

Each affine \(U_i\) admits an immersion into some \(\mathbf P^{n_i}_S\). Here is the finite-coordinate reason, also the exact open proof [Stacks, Tag 01VS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-quasi-projective-finite-type-over-S). Cover \(U_i\) by finitely many distinguished affine opens mapping into affine base opens. On each, choose finitely many algebra generators over that base ring. Clear their denominators in the functions on the affine \(U_i\). Together with powers of the functions defining those distinguished opens, these give a finite globally generating tuple of the trivial sheaf. Its ratios surject onto each chosen affine chart ring, proving an immersion as in the eighth lesson. This argument permits a nonaffine \(S\).

Let \(Z_i\subset\mathbf P^{n_i}_S\) be the scheme-theoretic closure of \(U_i\), so \(U_i\subset Z_i\) is a scheme-theoretically dense open. Each \(Z_i\) is proper over \(S\). The combined maps on \(U\) give an immersion

\[
U\longrightarrow\prod_{i=1}^m\mathbf P^{n_i}_S.
\]

It is an immersion because one component is an immersion and the remaining separated factors permit the closed-graph factorization. Let \(Z\) be its scheme-theoretic closure in this product. It is proper over \(S\), contains \(U\) as a scheme-theoretically dense open, and has projections \(p_i:Z\to Z_i\). The projections factor through \(Z_i\) because their defining ideals vanish on \(U\), hence on \(Z\) by schematic density. Each \(p_i\) is proper: it is a map from a proper \(S\)-scheme to a separated \(S\)-scheme.

Set \(V_i=p_i^{-1}(U_i)\), and \(X'=\bigcup_iV_i\subset Z\). The maps \(V_i\to U_i\subset X\) are proper over \(U_i\). On \(V_i\cap V_j\) they agree on \(U\), and hence agree by schematic density and separatedness of \(X\). They glue to \(\pi:X'\to X\).

We verify that \(\pi^{-1}(U_i)=V_i\). There is an open inclusion \(V_i\subset\pi^{-1}(U_i)\) over \(U_i\). Its source is proper over \(U_i\), and its target is separated over \(U_i\): \(X'\) is separated over \(S\), so its morphism to \(X\) is separated by separatedness cancellation. Therefore the inclusion is proper and has closed image. It contains \(U\), which is dense in \(\pi^{-1}(U_i)\), so its image is the whole target. The two open subschemes are equal. Thus \(\pi\) is proper on the target cover \((U_i)\), hence proper globally. Its image on each \(U_i\) is closed and contains the dense \(U\); hence it is surjective.

The same argument, replacing \(V_i\to U_i\) by the identity \(U\to U\), proves \(\pi^{-1}(U)=U\). Finally \(X'\) is open in the closed subscheme \(Z\) of the product of projective spaces. The iterated Segre embedding places that product in a single finite projective space. Thus \(X'\) has the required immersion; it is quasi-compact because it is Noetherian. Compose with \(X^*\to X\) if the earlier replacement was necessary. Properness, surjectivity and the isomorphism on \(U\) are preserved. \(\square\)

This is [Stacks, Tag 0200](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-chow-Noetherian). The scheme-theoretic closure step is essential for nonreduced sources. Ordinary topological density alone would not make the maps on overlaps equal.

If \(X\to S\) is proper, then \(X'\to S\) is proper, and its immersion into projective space is closed. Thus \(X'\to S\) is H-projective. In this case \(\pi\) is H-projective too: its graph into \(X'\times_S X\) is closed, and the base change of \(X'\hookrightarrow\mathbf P^N_S\) embeds that product closedly in \(\mathbf P^N_X\). This is the familiar projective modification of a proper scheme.

The proof uses properness of projective space, graph and equalizer arguments, and amplification of affine coordinates. It uses neither the Noetherian DVR criterion nor a coherence theorem for proper direct images, so it supplies the noncircular Chow ingredient in the earlier properness lesson.

## 5. The forms over a qcqs base

**Theorem 5.1.** Let \(S\) be quasi-compact and quasi-separated and \(X\to S\) separated and of finite type. There are a proper surjection \(X'\to X\) and an immersion \(X'\to\mathbf P^N_S\). If \(X\) has finitely many irreducible components, they can be chosen with an isomorphism over a dense open of \(X\).

The exact full open proofs are [Stacks, Tag 0202](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-chow-finite-type) for the first assertion and [Tag 0203](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-chow-EGA) for the dense-open assertion. These are the proof providers for the general-base forms. They use the Noetherian construction just proved together with the descent and Noetherian approximation developed in Limits and Noetherian approximation.

For the first form, the source is first embedded closedly in a separated finitely presented scheme over \(S\); this accommodates a finite-type morphism whose relations need not be finitely generated. That finitely presented ambient scheme and its separatedness descend to a Noetherian approximation of \(S\). Apply Theorem 4.1 there and pull the modification back, first to \(S\) and then to \(X\). Properness, surjectivity and the projective-space immersion survive these base changes. The closed ambient finite-presentation embedding is proved in the same open treatment, so no finite-presentation assumption on \(X\) is hidden in this reduction.

For the second form, one also keeps the finitely many generic points distinct and without specialization relations in a sufficiently late approximation. Take the scheme-theoretic image there and choose the Noetherian modification to be an isomorphism near all its generic points. The inverse image of that open contains every original generic point, hence is dense. The full argument at Tag 0203 verifies this control of generic points and the resulting immersion; it is stronger than merely pulling back an unspecified dense open of an approximation.

## 6. Exercises with solutions

**Exercise 6.1 (easy).** Show that a closed subscheme of a quasi-projective \(S\)-scheme is quasi-projective.

**Solution.** Let \(Z\hookrightarrow X\to S\) be the maps and let \(\mathcal L\) be relatively ample on \(X\). Closed immersions are of finite type, so the composite is of finite type. Over every affine \(V\subset S\), closed restriction of ampleness makes \(\mathcal L|_{Z_V}\) ample. The composite is quasi-compact, as finite type includes quasi-compactness. Thus this restriction is relatively ample on \(Z\), proving the claim.

**Exercise 6.2 (medium).** Prove projective implies proper using valuation diagrams, retaining finite type and uniqueness.

**Solution.** Over an affine base open, a finite generating tuple for \(\mathcal E\) gives (1.1), so the source is a closed subscheme of finite projective space. It is separated and of finite type. In a valuation diagram the base map lands in such an affine open: choose one containing the closed-point image; its inverse image contains the closed point of the local spectrum and is the whole spectrum. Extend the generic point in projective space by choosing a least-value homogeneous coordinate. Every local equation of the closed source vanishes on the generic point and thus vanishes in the valuation ring, which injects into its fraction field. The extension factors through the source. Separatedness gives uniqueness, and the general valuative criterion gives properness. This avoids treating existence alone as a finite-type assertion.

**Exercise 6.3 (medium).** Show that a composite of H-projective morphisms is H-projective, and decide whether quasi-compactness of the final base is necessary for this proof.

**Solution.** Given the two closed embeddings into \(\mathbf P^n_Y\) and \(\mathbf P^m_S\), use their base-changed closed embeddings to obtain \(X\hookrightarrow\mathbf P^n_S\times_S\mathbf P^m_S\). Segre gives a closed embedding into \(\mathbf P^{(n+1)(m+1)-1}_S\). These constructions commute with arbitrary base change and use no finite choice of an affine cover of \(S\). Thus quasi-compactness of \(S\) is unnecessary in this H-projective case. For arbitrary projective bundles, Theorem 2.2 instead uses its explicit qcqs hypothesis.

**Exercise 6.4 (medium).** In the Noetherian Chow construction, show that \(\pi\) can be an isomorphism over a dense open when \(X\) is irreducible. Why does merely taking a reduced closure not give the same conclusion for nonreduced \(X\)?

**Solution.** Every nonempty affine open contains the unique generic point. Choose a finite affine cover and take its intersection \(U\), a nonempty dense open. Theorem 4.1's construction gives \(\pi^{-1}(U)=U\) as schemes, by the proper closed-image argument for the identity \(U\to U\). For an integral source this also identifies the function fields, so the modification is birational. A reduced closure can discard nilpotents that are already present on \(U\); its map would then fail to be an isomorphism there. The scheme-theoretic closure retains precisely the functions seen on \(U\), including its nilpotents, and makes restriction injective so that the gluing argument works.

**Exercise 6.5 (hard).** Let \(f:X\to S\) be proper and \(\mathcal L\) \(f\)-ample. Prove local projectivity, and identify the actual hypotheses used to convert the local immersion into a closed immersion.

**Solution.** For each affine \(V\subset S\), properness gives finite type, and \(\mathcal L|_{X_V}\) is ample. The affine-base very-ample power theorem produces \(i:X_V\to\mathbf P^N_V\) as an immersion. The map is proper because its source is proper over \(V\) and its target is separated over \(V\), by the proper graph factorization. Hence its image is closed. An immersion with closed image is a closed immersion, proving H-projectivity of \(X_V\to V\) and therefore local projectivity of \(f\). No coherence theorem and no Noetherian assumption occur in these steps. The integer \(N\) and power of \(\mathcal L\) may depend on \(V\); the local conclusion alone does not claim a single global embedding into \(\mathbf P^N_S\).

## References and proof providers

The Stacks project, read in the AI Integrated Stacks Project edition, supplies the exact projectivity, stability, ample-base and Chow statements cited above. The qcqs composition proof uses its full finite-type submodule theorem under the stated conditions. General-base Chow forms have the exact complete open providers at Tags 0202 and 0203, including the finite-presentation ambient construction and generic-point control. These linked works retain GNU FDL 1.2; their text is not reproduced.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §§17.3 and 18.9, was consulted for projective-bundle conventions and the proper-scheme version of Chow’s lemma. The definitions here follow the quotient convention stated at the start. All assigned central assertions and all five exercises have the complete proofs or exact open proof providers specified above.
