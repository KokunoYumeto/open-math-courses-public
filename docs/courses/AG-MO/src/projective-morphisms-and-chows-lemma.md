# Projective morphisms and Chow’s lemma

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A projective morphism comes with the possibility of embedding its source in a projective bundle over the base. Properness then follows from projective space, while ampleness explains when local projective coordinates can be assembled. Chow’s lemma goes in another direction: it replaces a separated finite-type scheme by a proper surjective modification that has projective coordinates, preserving a dense open part of the original scheme.

We use Proper morphisms, Very ample sheaves and embeddings, and Ample invertible sheaves. In particular projective space is already proper, arbitrary-module Segre embeddings are available, and the finite-type submodule theorem on qcqs schemes is proved in Affine cohomology and Serre’s criterion, Lemma 4.4. Our projective bundles use invertible quotients: \(\mathbf P(\mathcal E)=\operatorname{Proj}_S\operatorname{Sym}\mathcal E\). No local freeness of \(\mathcal E\) is implicit.

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

Use the qcqs finite-type submodule theorem, proved in Affine cohomology and Serre’s criterion, Lemma 4.4, on \(S\): \(\mathcal F_\infty\) is the directed union of finite-type quasi-coherent submodules. Some finite-type submodule \(\mathcal F\) still surjects after pullback. To justify that selection, at each point of \(Y\) finitely many germs suffice to generate the finite-type target module, and all come from one member of the directed union. The resulting generation locus is open, since the cokernel is of finite type. Quasi-compactness of \(Y\) selects finitely many such loci, and directedness selects one submodule containing their finite choices. Thus

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

The theorem has the precise hypotheses of [Stacks, Tag 0C4P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-projective). Its finite-submodule ingredient is the complete programme proof in Affine cohomology and Serre’s criterion, Lemma 4.4, also used in the ampleness lesson. The proof explains exactly where quasi-compactness and quasi-separatedness of the final base enter. The simpler H-projective theorem does not need that step or those hypotheses.

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

If two \(S\)-morphisms from such a closure to a scheme \(Q\) separated over \(S\) agree on \(U\), they agree everywhere. Their equalizer is the pullback of the closed relative diagonal \(\Delta_{Q/S}\), hence a closed subscheme; its defining ideal vanishes on \(U\), so injectivity of the structure-sheaf map makes that ideal zero. This is the version of the equalizer argument appropriate to possibly nonreduced schemes.

**Theorem 4.1 (Chow’s lemma).** Let \(S\) be Noetherian and \(X\to S\) separated and of finite type. There exist a proper surjection \(\pi:X'\to X\), a quasi-compact immersion \(X'\to\mathbf P^N_S\), and a dense open \(U\subset X\) such that \(\pi^{-1}(U)\to U\) is an isomorphism.

**Proof.** All schemes in the construction are Noetherian. The finitely many irreducible components of \(X\) have generic points \(\eta_1,\ldots,\eta_r\). Every point \(x\) has an affine neighbourhood containing all these generic points. Indeed, choose an affine neighbourhood \(W\) avoiding the components that do not contain \(x\); it contains the generic points of all components through \(x\). For each remaining component choose an affine neighbourhood of its generic point avoiding every other component. These extra opens are disjoint from \(W\) and from one another. Their finite disjoint union with \(W\) is affine and has the required points. Quasi-compactness now gives a finite affine cover \(U_1,\ldots,U_m\) with every generic point in every member. Their intersection \(U\) is dense and open.

Replace \(X\) temporarily by the scheme-theoretic closure \(X^*\) of \(U\) in \(X\). Its map to \(X\) is a surjective closed immersion and is an isomorphism on \(U\). The intersections \(U_i\cap X^*\) remain affine and cover it. Thus a solution for \(X^*\) gives one for \(X\), and we may assume \(U\) scheme-theoretically dense in \(X\).

Each affine \(U_i=\operatorname{Spec}B\) admits a quasi-compact immersion into a finite projective space over \(S\). Choose a finite principal cover \(D(f_a)\) of \(U_i\) such that each member maps into an affine \(S_a=\operatorname{Spec}A_a\subset S\). Each \(B_{f_a}\) is a finite-type \(A_a\)-algebra by the affine-chart finite-type theorem. Write a finite generating list as \(b_{aj}/f_a^{e_{aj}}\), with \(b_{aj}\in B\). Choose \(M_a\geq1\) at least all these exponents. Use, for every \(a\), the global functions
\[
f_a^{M_a},\quad f_a^{M_a-1},\quad
f_a^{M_a-e_{aj}}b_{aj}
\]
as one finite homogeneous coordinate tuple. They generate the unit ideal: no maximal ideal can contain all \(f_a^{M_a}\), because the \(D(f_a)\) cover. The projective-coordinate theorem in Projective space, relative Proj and maps to projective space, Theorem 1.1 therefore defines a map to \(\mathbf P^{n_i}_S\).

In the target chart for the coordinate \(f_a^{M_a}\), restricted over \(S_a\), the inverse image is precisely \(D(f_a)\). Its coordinate ratios include \(f_a^{-1}\) and every \(b_{aj}/f_a^{e_{aj}}\), so the homomorphism from that target affine chart to \(B_{f_a}\) is surjective. Thus the map is a closed immersion on every one of these charts. Their union is an open target neighbourhood of its whole image, since the \(D(f_a)\) cover its source. It is a closed immersion into that union and hence an immersion into the full projective space. Quasi-compactness follows from the finite source cover. This proof works with a nonaffine \(S\), arbitrary fields and nilpotents.

Let \(Z_i\subset\mathbf P^{n_i}_S\) be the scheme-theoretic closure of \(U_i\), so \(U_i\subset Z_i\) is a scheme-theoretically dense open. Each \(Z_i\) is proper over \(S\). The combined maps on \(U\) give an immersion

\[
U\longrightarrow\prod_{i=1}^m\mathbf P^{n_i}_S.
\]

It is an immersion because one component is an immersion and the remaining separated factors permit the closed-graph factorization. Let \(Z\) be its scheme-theoretic closure in this product. It is proper over \(S\), contains \(U\) as a scheme-theoretically dense open, and has projections \(p_i:Z\to Z_i\). The projections factor through \(Z_i\) because their defining ideals vanish on \(U\), hence on \(Z\) by schematic density. Each \(p_i\) is proper: it is a map from a proper \(S\)-scheme to a separated \(S\)-scheme.

Set \(V_i=p_i^{-1}(U_i)\), and \(X'=\bigcup_iV_i\subset Z\). The maps \(V_i\to U_i\subset X\) are proper over \(U_i\). On \(V_i\cap V_j\) these \(S\)-morphisms agree on \(U\). Pulling back the closed diagonal \(\Delta_{X/S}\), schematic density makes their equalizer the whole overlap. They glue to \(\pi:X'\to X\).

We verify that \(\pi^{-1}(U_i)=V_i\). There is an open inclusion \(V_i\subset\pi^{-1}(U_i)\) over \(U_i\). Its source is proper over \(U_i\), and its target is separated over \(U_i\): \(X'\) is separated over \(S\), so its morphism to \(X\) is separated by separatedness cancellation. Therefore the inclusion is proper and has closed image. It contains \(U\), which is dense in \(\pi^{-1}(U_i)\), so its image is the whole target. The two open subschemes are equal. Thus \(\pi\) is proper on the target cover \((U_i)\), hence proper globally. Its image on each \(U_i\) is closed and contains the dense \(U\); hence it is surjective.

The same argument, replacing \(V_i\to U_i\) by the identity \(U\to U\), proves \(\pi^{-1}(U)=U\). Finally \(X'\) is open in the closed subscheme \(Z\) of the product of projective spaces. The iterated Segre embedding places that product in a single finite projective space. Thus \(X'\) has the required immersion; it is quasi-compact because it is Noetherian. Compose with \(X^*\to X\) if the earlier replacement was necessary. Properness, surjectivity and the isomorphism on \(U\) are preserved. \(\square\)

This is [Stacks, Tag 0200](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-chow-Noetherian). The scheme-theoretic closure step is essential for nonreduced sources. Ordinary topological density alone would not make the maps on overlaps equal.

If \(X\to S\) is proper, then \(X'\to S\) is proper, and its immersion into projective space is closed. Thus \(X'\to S\) is H-projective. In this case \(\pi\) is H-projective too: its graph into \(X'\times_S X\) is closed, and the base change of \(X'\hookrightarrow\mathbf P^N_S\) embeds that product closedly in \(\mathbf P^N_X\). This is the familiar projective modification of a proper scheme.

The proof uses properness of projective space, graph and equalizer arguments, and amplification of affine coordinates. It uses neither the Noetherian DVR criterion nor a coherence theorem for proper direct images, so it supplies the noncircular Chow ingredient in the earlier properness lesson.

## 5. The forms over a qcqs base

**Theorem 5.1.** Let \(S\) be quasi-compact and quasi-separated and \(X\to S\) separated and of finite type. There are a proper surjection \(X'\to X\) and an immersion \(X'\to\mathbf P^N_S\). If \(X\) has finitely many irreducible components, they can be chosen with an isomorphism over a dense open of \(X\).

We first prove the finite-presentation ambient step. The limit results used in its proof are the complete programme proofs in Limits and Noetherian approximation: finite open data, sections and eventual affineness in Lemmas 2.1–2.3, maps to a locally finitely presented target in Theorem 3.2, finite-presentation descent and eventual separatedness in Theorems 4.1–4.2, and absolute Noetherian approximation, Theorem 5.2. No finite-presentation assumption on \(X\) will be introduced.

### A separated finitely presented ambient scheme

**Auxiliary lemma (a separated finitely presented ambient scheme).** A separated finite-type morphism \(X\to S\), with \(S\) qcqs, admits a closed immersion into a separated finitely presented \(S\)-scheme.

**Proof.** The scheme \(X\) is qcqs: finite type makes it quasi-compact over the quasi-compact base, and separatedness together with quasi-separatedness of the base makes it quasi-separated. Apply absolute approximation to \(S\), and fix a finite-type \(\mathbf Z\)-stage \(S_0\). Its projection \(S\to S_0\) is affine. Choose a finite affine cover \(V_{0a}\) of \(S_0\), and put \(V_a=S\times_{S_0}V_{0a}\), which is affine.

Apply absolute approximation independently to \(X\), writing \(X=\varprojlim_j T_j\), with the \(T_j\) of finite type over \(\mathbf Z\) and all transitions and projections affine. The composite \(X\to S_0\) descends to a map \(h_j:T_j\to S_0\) by the qcqs maps assertion of Theorem 3.2: \(S_0\) is finitely presented over \(\mathbf Z\). Choose finitely many affine opens \(U_a\) covering \(X\), each mapping into one \(V_a\). The index \(a\) may repeat a base chart. Lemmas 2.1 and 2.3 give affine opens \(U_{a,j}\subset T_j\) whose inverse images are \(U_a\), forming a cover eventually. Their images under \(h_j\) lie in the chosen \(V_{0a}\) eventually: the quasi-compact stage open \(U_{a,j}\cap h_j^{-1}(V_{0a})\) has inverse image all of \(U_a\), so the equality assertion of Lemma 2.1 applies.

Write
\[
A_{0a}=\Gamma(V_{0a},\mathcal O),\quad
A_a=\Gamma(V_a,\mathcal O),\quad
B_{a,j}=\Gamma(U_{a,j},\mathcal O),\quad
B_a=\Gamma(U_a,\mathcal O).
\]
The ring \(B_a\) is a finite-type \(A_a\)-algebra. Choose finitely many algebra generators. Since \(B_a=\varinjlim_j B_{a,j}\), those generators lift to a common stage. At that stage the natural map
\[
B_{a,j}\otimes_{A_{0a}}A_a\longrightarrow B_a
\tag{5.1}
\]
is surjective: its image contains \(A_a\) and every chosen generator. A common stage works for the finite cover. Consequently
\[
X\longrightarrow Y_0=T_j\times_{S_0}S
\]
is a closed immersion, because on the covering affine opens \(U_{a,j}\times_{V_{0a}}V_a\) it is exactly the spectrum of (5.1). The morphism \(T_j\to S_0\) is finitely presented: both schemes are of finite type over the Noetherian scheme \(\operatorname{Spec}\mathbf Z\), so its affine chart algebras are finite type over Noetherian rings and hence finitely presented; the Noetherian source makes the morphism quasi-compact and quasi-separated. Thus \(Y_0\to S\) is finitely presented. At this point \(Y_0\) need not be separated.

Let \(\mathcal I\) define \(X\) in \(Y_0\). The complete finite-type subsheaf theorem in Affine cohomology and Serre’s criterion, Lemma 4.4 writes
\[
\mathcal I=\bigcup_\lambda\mathcal I_\lambda
\]
as a directed union of quasi-coherent ideals of finite type. Put \(W_\lambda=V(\mathcal I_\lambda)\). Each \(W_\lambda\) is finitely presented over \(S\): a quotient of an affine algebra by a finitely generated ideal is finitely presented, and this description applies on each affine chart. The transitions \(W_\mu\to W_\lambda\) are closed immersions for \(\mu\geq\lambda\). On affine charts their ring colimit is the quotient by \(\mathcal I\); hence
\[
X=\varprojlim_\lambda W_\lambda.
\tag{5.2}
\]

We check separatedness at a stage without assuming that this system is obtained by base change from a fixed scheme over varying bases. Cover \(S\) by finitely many affines \(V_\gamma=\operatorname{Spec}A_\gamma\), and cover each \((Y_0)_{V_\gamma}\) by finitely many affine opens \(E_{\gamma a}\). Such finite covers exist because \(Y_0\to S\) is finitely presented. The closed subschemes
\[
E_{\gamma a,\lambda}=E_{\gamma a}\cap W_\lambda
\]
are affine and cover \((W_\lambda)_{V_\gamma}\). Their pairwise intersections
\[
Q_{\gamma ab,\lambda}
=E_{\gamma a,\lambda}\cap E_{\gamma b,\lambda}
\]
are qcqs and have closed, therefore affine, transition maps. Their limit is \(Q_{\gamma ab}=E_{\gamma a}\cap E_{\gamma b}\cap X\). This limit is affine: since \(X\to V_\gamma\) is separated, its diagonal realizes \(Q_{\gamma ab}\) as a closed subscheme of the affine product
\[
(E_{\gamma a}\cap X)\times_{V_\gamma}(E_{\gamma b}\cap X).
\]
Lemma 2.3 therefore makes every \(Q_{\gamma ab,\lambda}\) affine at a common stage. Empty limit intersections become empty by Theorem 1.1. There are only finitely many pairs.

At and beyond this stage set
\[
B_{\gamma a,\lambda}=\Gamma(E_{\gamma a,\lambda},\mathcal O),
\qquad C_{\gamma ab,\lambda}=\Gamma(Q_{\gamma ab,\lambda},\mathcal O).
\]
The ring \(C_{\gamma ab,\lambda}\) is a finite-type \(A_\gamma\)-algebra: this affine intersection is a quasi-compact open in a finitely presented scheme over \(V_\gamma\). Choose algebra generators at one stage. Every later \(C_{\gamma ab,\mu}\) is a quotient of this ring, since the transitions are now closed immersions between affine schemes, so the same generator images generate every later ring.

The diagonal of \(X/V_\gamma\) is closed. Its affine chart map is therefore surjective:
\[
\bigl(\varinjlim_\lambda B_{\gamma a,\lambda}\bigr)
 \otimes_{A_\gamma}
\bigl(\varinjlim_\lambda B_{\gamma b,\lambda}\bigr)
\longrightarrow
\varinjlim_\lambda C_{\gamma ab,\lambda}.
\tag{5.3}
\]
Express the images of the finitely many chosen generators by elements in the source of (5.3). Represent those elements at a stage and make the resulting finitely many equalities hold at a later stage. The map
\[
B_{\gamma a,\lambda}\otimes_{A_\gamma}B_{\gamma b,\lambda}
\longrightarrow C_{\gamma ab,\lambda}
\]
is then surjective, because its image contains \(A_\gamma\) and all the generator images. Doing this for the finite set of pairs makes every corresponding chart of the diagonal a closed immersion. The affine products cover
\((W_\lambda)_{V_\gamma}\times_{V_\gamma}(W_\lambda)_{V_\gamma}\), so the whole diagonal is closed. The \(V_\gamma\) cover \(S\), proving \(W_\lambda\to S\) separated. Taking \(Y=W_\lambda\) proves the lemma. \(\square\)

**Proof of the first assertion of Theorem 5.1.** Embed \(X\) closedly in the separated finitely presented \(S\)-scheme \(Y\) just constructed. Write \(S=\varprojlim_i S_i\) by absolute approximation. The finite-presentation descent theorem gives a finitely presented \(Y_i\to S_i\) with
\[
Y=Y_i\times_{S_i}S.
\]
The eventual separatedness theorem makes \(Y_i\to S_i\) separated after increasing \(i\). The scheme \(S_i\) is of finite type over \(\mathbf Z\), hence Noetherian. Theorem 4.1 supplies
\[
Y_i\longleftarrow Y_i'\longrightarrow\mathbf P^N_{S_i}
\]
with the first map proper and surjective and the second an immersion. Put \(Y'=Y_i'\times_{S_i}S\) and \(X'=X\times_Y Y'\). Then \(X'\to X\) is the base change of the proper surjection \(Y_i'\to Y_i\), so is proper and surjective. Surjectivity under base change can be seen fibrewise: a nonempty fibre remains nonempty after a residue-field extension, since tensoring a nonzero vector space with a field extension is nonzero and a nonzero ring has a prime. Finally \(X'\to Y'\) is a closed immersion, as the base change of \(X\to Y\). Composing it with the base-changed immersion \(Y'\to\mathbf P^N_S\) gives the required immersion. This proves the assertion for finite type, even when the ideal defining \(X\) has infinitely many generators.

**Proof of the dense-open assertion.** We give the construction directly over \(S\). This makes explicit why finitely many irreducible components suffice. If \(X\) is empty, use the empty \(X'\), \(N=0\), and the empty dense open. Otherwise let \(\eta_1,\ldots,\eta_r\) be the generic points of its finitely many irreducible components \(Z_1,\ldots,Z_r\).

Every point \(x\) has an affine open neighbourhood containing all the \(\eta_j\). Choose an affine neighbourhood \(W\) of \(x\) avoiding all the \(Z_j\) not containing \(x\). It contains the generic points of every component through \(x\). For each remaining component choose an affine open around its generic point avoiding all the other components. Since the list comprises all components, this extra open is contained in its own component; it is disjoint from \(W\) and from all the other extra opens. A finite disjoint union of affine schemes is affine, so their union with \(W\) is the required affine neighbourhood. Quasi-compactness of \(X\) gives a finite affine cover \(U_1,\ldots,U_m\) of this kind. The intersection
\[
U=\bigcap_{i=1}^m U_i
\]
is open and contains every generic point, hence is dense. It is quasi-compact because \(X\) is quasi-separated.

We will use a small quasi-compactness fact: a map from a quasi-compact scheme \(T\) to a quasi-separated scheme \(Q\) is quasi-compact. Its graph is the base change of the quasi-compact diagonal of \(Q\), and its projection to \(Q\) is the base change of the quasi-compact \(T\to\operatorname{Spec}\mathbf Z\); their composite is the given map. The schematic-closure facts preceding Theorem 4.1 therefore hold for a quasi-compact immersion into any qcqs scheme, not just a Noetherian one. Indeed, the immersion is quasi-compact and quasi-separated; the complete qcqs pushforward theorem in Affine cohomology and Serre’s criterion, Theorem 4.3 makes its structure-sheaf direct image quasi-coherent. The kernel ideal defining the closure is therefore quasi-coherent. Its support is the topological closure: a local function in the kernel has a distinguished nonvanishing open disjoint from the source, and an open disjoint from the source has the unit ideal as kernel. In an open target neighbourhood where the immersion is closed, the kernel recovers exactly that closed subscheme. The source is thus open in its closure. By definition, the closure's structure sheaf injects into the direct image of the source's structure sheaf. Both this injection and the construction restrict to opens. In particular, two \(S\)-morphisms from the closure, or an open in it, into a scheme \(Q\) separated over \(S\) agree if they agree on the source: pull back the closed relative diagonal \(\Delta_{Q/S}\); its equalizer ideal is zero by this injection.

Replace \(X\) by the schematic closure \(X^*\) of \(U\) in \(X\). The map \(X^*\to X\) is a surjective closed immersion, is proper, and is an isomorphism on \(U\). Its underlying space is all of \(X\); its affine opens \(U_i\cap X^*\) still cover it. Its morphism to \(S\) remains separated and finite type, since closed immersions are finite type without any finite-generation condition on their ideal. Rename this source and these affine opens \(X\) and \(U_i\) during the construction, so that \(U\) is now schematically dense in \(X\).

The finite-coordinate calculation in the proof of Theorem 4.1 applies to each \(U_i=\operatorname{Spec}B\) over our qcqs \(S\). To recall all its algebra, choose a finite principal cover \(D(f_a)\) of \(U_i\) with each member mapping to an affine \(S_a=\operatorname{Spec}A_a\). Choose finite generators \(b_{aj}/f_a^{e_{aj}}\) of \(B_{f_a}\) as an \(A_a\)-algebra and take \(M_a\geq1\) at least every \(e_{aj}\). The finite global coordinate tuple
\[
 f_a^{M_a},\qquad f_a^{M_a-1},\qquad
 f_a^{M_a-e_{aj}}b_{aj}
\]
generates the unit ideal, because the \(D(f_a)\) cover. It defines \(U_i\to\mathbf P^{n_i}_S\) by the projective-coordinate theorem. In the target chart belonging to \(f_a^{M_a}\), over \(S_a\), the inverse image is \(D(f_a)\); its coordinate ratios include \(f_a^{-1}\) and every chosen algebra generator. The chart ring map is surjective, hence the map is closed on each such target chart. These charts form an open target neighbourhood of the image. It follows that the map is an immersion, and it is quasi-compact because the source is quasi-compact and the target is quasi-separated. This argument needs only finite type; the relations in \(B_{f_a}\) need not be finitely generated.

Let \(Z_i\) be the schematic closure of \(U_i\) in \(\mathbf P^{n_i}_S\). It is proper over \(S\). The maps on \(U\) combine to an immersion into the finite product of these projective spaces: factor the combined map as the closed graph of the remaining separated factors followed by the base change of one immersion. Let \(Z\) be its schematic closure in that product. Then \(Z\) is proper over \(S\), and \(U\) is a schematically dense open in \(Z\). The projections factor through \(Z_i\): each defining ideal pulls back to an ideal zero on \(U\), hence zero on \(Z\). Denote the resulting maps by \(p_i:Z\to Z_i\). Each is proper. Its graph is closed, since \(Z_i\to S\) is separated, and the projection \(Z\times_S Z_i\to Z_i\) is the base change of the proper \(Z\to S\).

Put \(V_i=p_i^{-1}(U_i)\) and \(X'=\bigcup_iV_i\subset Z\). Each \(V_i\to U_i\) is proper, so \(V_i\) is quasi-compact; their finite union \(X'\) is quasi-compact. On \(V_i\cap V_j\), the two \(S\)-morphisms into \(X\) agree on \(U\). Their equalizer is the pullback of \(\Delta_{X/S}\); schematic density makes its defining ideal zero, so the maps agree on the whole overlap. They glue to \(\pi:X'\to X\).

We check \(\pi^{-1}(U_i)=V_i\). The inclusion \(V_i\hookrightarrow\pi^{-1}(U_i)\) is open and is over \(U_i\). Its source is proper over \(U_i\), while its target is separated over \(U_i\): \(X'\) is separated over \(S\), so its morphism to \(X\) is separated by diagonal cancellation. The graph factorization therefore makes the inclusion proper. Its image is closed and contains the dense \(U\), so it is all of \(\pi^{-1}(U_i)\). The open subschemes are equal. Thus \(\pi\) is proper on the target cover \(U_i\), hence globally. Its image on each \(U_i\) is closed and contains the dense \(U\), so it is surjective. Applying the same proper-graph argument to the open inclusion \(U\hookrightarrow\pi^{-1}(U)\), whose source is the proper identity \(U\to U\), proves \(\pi^{-1}(U)=U\).

Finally \(X'\) is open in the closed subscheme \(Z\) of the product of projective spaces. The iterated Segre closed immersion places this product in a single \(\mathbf P^N_S\). This gives the required quasi-compact immersion. Compose \(\pi\) with the earlier proper surjective closed immersion \(X^*\to X\), if necessary; it retains the isomorphism over the original \(U\). This proves the dense-open clause with its original hypotheses and scheme structure. \(\square\)

For comparison, the earlier generic-point approximation route also gives the dense-open conclusion; here are the missing details of that route. Start with the proved closed immersion \(X\hookrightarrow Y\) and a Noetherian model \(Y_i\to S_i\). The images of distinct \(\eta_j\) in \(Y\) have no specialization relations, because the closed immersion identifies their closures with distinct components of \(X\). For each ordered pair \(j\ne k\), there is an open of \(Y\) containing \(\eta_j\) and not \(\eta_k\). The topology of an affine-transition inverse limit has a basis of inverse images of stage opens. Choose such a basis open inside each of these opens; a common later stage then makes the images \(h_i(\eta_j)\) pairwise incomparable under specialization.

The composite \(h_i:X\to Y_i\) is affine, since \(X\to Y\) is closed and \(Y\to Y_i\) is affine. Its schematic image \(T_i\subset Y_i\) is defined by \(\ker(\mathcal O_{Y_i}\to(h_i)_*\mathcal O_X)\). It has underlying space \(\overline{h_i(X)}\): on an affine chart this is the fact that the closure of the image of \(\operatorname{Spec}B\to\operatorname{Spec}A\) is \(V(\ker(A\to B))\); a distinguished open has empty inverse image exactly when its defining element has nilpotent image in \(B\). Every point of \(X\) specializes from an \(\eta_j\), so
\[
|T_i|=\bigcup_{j=1}^r\overline{\{h_i(\eta_j)\}}.
\]
The incomparable points are exactly the generic points of its irreducible components. Theorem 4.1 applied to the Noetherian separated \(T_i\to S_i\) gives a proper surjection \(T_i'\to T_i\), an immersion into \(\mathbf P^N_{S_i}\), and an isomorphism over a dense open \(V\subset T_i\). This open contains every \(h_i(\eta_j)\), so \(h_i^{-1}(V)\) is a dense open of \(X\).

Set \(X'=X\times_{T_i}T_i'\). The map to \(X\) is proper and surjective and is an isomorphism over \(h_i^{-1}(V)\). To check its immersion into projective space, let \(T=T_i\times_{S_i}S\). The original closed immersion \(X\hookrightarrow Y_i\times_{S_i}S\) factors closedly through \(T\), since the ideal of \(T_i\) pulls back to zero on \(X\). Hence \(X'\) is a closed subscheme of \(T_i'\times_{S_i}S\); composing that closed immersion with the base change of \(T_i'\to\mathbf P^N_{S_i}\) gives the immersion into \(\mathbf P^N_S\). This completes the former approximation argument as well.

The free primary comparison references are [Stacks, Tag 0202](https://stacks.math.columbia.edu/tag/0202), [Tag 0203](https://stacks.math.columbia.edu/tag/0203) and [Tag 01ZJ](https://stacks.math.columbia.edu/tag/01ZJ). The general-base arguments, finite-presentation ambient step and generic-point control are proved above; the links identify comparison material rather than supply omitted proofs. This exposition is CC0.

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

The Stacks project, read in the AI Integrated Stacks Project edition, supplies the exact projectivity, stability, ample-base and Chow comparison statements cited above. The qcqs composition proof uses the complete programme proof in Affine cohomology and Serre’s criterion, Lemma 4.4 under the stated conditions. Both general-base Chow forms are proved in Section 5, including the separated finite-presentation ambient construction, the direct finite-components construction and the generic-point approximation argument. Their limit inputs are the complete earlier proofs in Limits and Noetherian approximation, Lemmas 2.1–2.3 and Theorems 3.2, 4.1–4.2 and 5.2. The linked Stacks sources retain GNU FDL 1.2; this lesson’s independently written exposition is CC0.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §§17.3 and 18.9, was consulted for projective-bundle conventions and the proper-scheme version of Chow’s lemma. The definitions here follow the quotient convention stated at the start. The central assertions and all five exercises are supported by the complete proofs and actual earlier programme providers specified above.
