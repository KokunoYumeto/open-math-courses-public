# Limits of schemes and Noetherian approximation

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A polynomial, a finite list of relations, and a finite gluing diagram use only finitely much information. A ring may contain infinitely many elements, but a finitely presented algebra over it can be defined over a much smaller ring. This lesson develops the geometric version of that observation. It explains both what can be defined at a finite stage and why identities between the resulting objects eventually become true at a finite stage.

We use the finiteness conditions from Finiteness of morphisms. All rings have a unit, including the zero ring. A directed set is nonempty, and any finite subset has an upper bound. An inverse system has maps \(S_j\to S_i\) for \(j\geq i\). Its transition maps will be affine. The notation “eventually” means “at every stage beyond some stage”; it does not require a linearly ordered index set. Quasi-compact and quasi-separated will sometimes be abbreviated to **qcqs**. Neither word includes separatedness.

## 1. Constructing the limit

**Theorem 1.1 (affine transition maps).** An inverse system \((S_i)\) with affine transition maps has a limit \(S\) in schemes. Each projection \(p_i:S\to S_i\) is affine. The canonical map of topological spaces

\[
|S|\longrightarrow\varprojlim_i |S_i|
\]

is a homeomorphism. In particular, inverse images of opens from finite stages form a basis for the topology of \(S\). If the \(S_i\) are quasi-compact and nonempty, then \(S\) is nonempty.

**Proof.** Start with affine schemes \(S_i=\operatorname{Spec}A_i\). Put \(A=\varinjlim A_i\). The correspondence between maps to an affine scheme and maps from its coordinate ring gives

\[
\operatorname{Hom}(T,\operatorname{Spec}A)
=\varprojlim_i\operatorname{Hom}(T,\operatorname{Spec}A_i)
\]

for every scheme \(T\). Thus \(\operatorname{Spec}A\) is the scheme limit. A compatible family of prime ideals \(\mathfrak p_i\subset A_i\) determines a prime of \(A\): an element represented at stage \(i\) belongs to it exactly when its representative belongs to \(\mathfrak p_i\). Compatibility makes this independent of the representative. The ideal is proper and prime because any finite calculation can be made at a common stage. Conversely, a prime of \(A\) contracts to such a family. A basic open \(D(a)\) of \(\operatorname{Spec}A\) is the pullback of \(D(a_i)\) for a representative \(a_i\). This proves the topological assertion in the affine case.

For the general construction, fix an index \(i_0\) and work on the cofinal set \(i\geq i_0\). Cover \(S_{i_0}\) by affine opens \(U_\alpha\). Their inverse images \(U_{\alpha,i}\) are affine; construct their limits by the preceding paragraph. These limits glue. Indeed, an intersection \(U_\alpha\cap U_\beta\) is covered by distinguished opens of \(U_\alpha\) contained in \(U_\beta\). Localization commutes with filtered colimits, so the construction on each such distinguished open is the same from either chart. These canonical identifications satisfy the cocycle identity. No quasi-compactness of the intersections is needed for this construction.

Maps into the glued scheme satisfy the limit universal property because they do so on the chart inverse images and agree on their overlaps. The projection to \(S_{i_0}\) is affine by construction. Repeating the construction starting at any \(i\), uniqueness of a limit identifies the resulting scheme with \(S\); hence every projection is affine. The chart calculation of primes and basic opens proves the claimed homeomorphism globally.

For nonemptiness, take a finite affine cover \(U_1,\ldots,U_n\) of one stage \(S_{i_0}\). If each system of inverse images of \(U_a\) eventually had an empty member, a common later stage would be empty. Therefore some \(U_a\) has nonempty inverse image at every stage. Write these affine inverse images as \(\operatorname{Spec}B_i\). Their colimit ring is nonzero: an equality \(1=0\) in the colimit would hold at a finite stage. Its spectrum is nonempty and is an open of \(S\). \(\square\)

These are the limit results of [Stacks, Tags 01YW–01YY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-directed-inverse-system-has-limit) and [Tag 01Z2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-limit-nonempty). Notice that the nonemptiness argument needs quasi-compactness, but not quasi-separatedness or surjective transition maps.

We will repeatedly use the following consequence. If \(Z_i\subset S_i\) are compatible nonempty closed subsets and the \(S_i\) are quasi-compact, there is a point of \(S\) mapping into every \(Z_i\). Give each \(Z_i\) its reduced closed subscheme structure. A map from a reduced scheme whose image lies in a closed subset factors through that reduced closed subscheme: the defining functions vanish at all points, hence are zero. The induced transitions on the \(Z_i\) are affine, as is checked on the affine charts cut out by closed immersions. They are quasi-compact and nonempty, so Theorem 1.1 applies. In particular, a compatible system of closed subsets with empty limit has an empty member. This is [Stacks, Tag 01Z3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-limit-closed-nonempty).

## 2. Opens, sections, and affine charts at finite stages

For this section suppose \(S=\varprojlim S_i\), with qcqs stages and affine transitions. The limit is qcqs: it is affine over any qcqs stage. An affine morphism is quasi-compact and separated, and these conditions give quasi-compactness and quasi-separatedness of its source over a qcqs base.

**Lemma 2.1 (finite open data).** Every quasi-compact open \(W\subset S\) is the inverse image of a quasi-compact open \(W_i\subset S_i\). If two quasi-compact stage opens have equal inverse images in \(S\), their inverse images become equal at a common later stage. A finite collection of stage opens which covers \(S\) eventually covers the stage itself.

**Proof.** Cover one stage by finitely many affines \(U_a\). The intersections of \(W\) with their inverse images are quasi-compact because \(S\) is quasi-separated. Each is a finite union of distinguished opens in an affine limit. Their defining elements can be represented at one common stage. The union of the corresponding stage opens gives \(W_i\).

For equality, put both opens at the same stage. To prove eventual containment \(V_j\subset W_j\), consider the closed subsets \(V_j\setminus W_j\) of the quasi-compact schemes \(V_j\). These schemes form a system with affine transitions. If the containment failed at every later stage, the closed-subset consequence of Theorem 1.1 would give a point of \(V\setminus W\) at the limit. Reverse the roles to prove equality. Apply equality to the union of a finite collection of opens and to the whole scheme to get the covering assertion. \(\square\)

**Lemma 2.2 (sections).** Fix a quasi-coherent sheaf \(\mathcal F_{i_0}\) on a stage and pull it back to \(\mathcal F_i\) and \(\mathcal F\). Then

\[
\varinjlim_{i\geq i_0}\Gamma(S_i,\mathcal F_i)
\;\cong\;\Gamma(S,\mathcal F).
\]

**Proof.** Choose a finite affine cover of \(S_{i_0}\) and finite affine covers of its pairwise intersections. Pull all these opens back to every stage. They remain affine. On an affine chart, sections of the pullback are a module tensor product; tensor products commute with filtered colimits. Global sections are the equalizer of the two restriction maps from the finite product of chart sections to the finite product of overlap-chart sections. Filtered colimits of modules commute with finite products and kernels. Concretely, finitely many sections and finitely many agreement equations can all be represented and checked at one stage. This gives the assertion. \(\square\)

The same finite-cover calculation proves a useful identity on any qcqs scheme \(T\). If \(h\in\Gamma(T,\mathcal O_T)\), and \(T_h\) denotes the open where \(h\) is invertible, then

\[
\Gamma(T,\mathcal O_T)_h=\Gamma(T_h,\mathcal O_T).
\tag{2.1}
\]

On each affine in the finite cover this is ordinary ring localization; localization also commutes with the equalizer used above. The open \(T_h\) is quasi-compact, since its intersections with the finitely many affine charts are principal opens.

**Lemma 2.3 (eventual affineness).** If \(S\) is affine, then \(S_i\) is affine eventually. Consequently, an affine quasi-compact open of \(S\) has an affine model \(W_i\subset S_i\) eventually.

**Proof.** Choose a finite affine cover of one stage and let \(U_1,\ldots,U_n\) be its inverse images in \(S\). Since \(S\) is affine, choose finitely many global functions \(h_r\) for which the principal opens \(D(h_r)\) cover \(S\) and each lies in one \(U_a\). There are global functions \(c_r\) with \(\sum_r c_rh_r=1\). Lemma 2.2 represents all these functions and this equation at a stage.

The open \((S_i)_{h_{r,i}}\) is quasi-compact. At the limit it is contained in the selected chart \(U_a\). The closed-subset argument in Lemma 2.1 makes that containment true at a later stage. At that stage \((S_i)_{h_{r,i}}\) is a principal open inside the affine inverse image of the selected chart, hence is affine. Put \(C_i=\Gamma(S_i,\mathcal O_{S_i})\). The functions \(h_{r,i}\) generate its unit ideal, so the \(D(h_{r,i})\) cover \(\operatorname{Spec}C_i\). By (2.1), the canonical map \(S_i\to\operatorname{Spec}C_i\) identifies each of the affine opens \((S_i)_{h_{r,i}}\) with \(D(h_{r,i})\). It is therefore an isomorphism. Later stages remain affine over this affine stage.

For the final assertion, first descend the open by Lemma 2.1, then apply what we just proved to the system of its inverse images. \(\square\)

The corresponding source locators are [Stacks, Tag 01Z4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-opens), [Tag 01Z0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-section), and [Tag 01Z6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-limit-affine). Lemma 2.3 explains why choosing an affine chart at the limit is legitimate in a descent proof; the choice must be followed by this eventual-affineness step.

## 3. Finite presentation is detected by limits

**Lemma 3.1 (the algebraic criterion).** An \(A\)-algebra \(B\) is finitely presented if and only if, for every filtered system of \(A\)-algebras \(C_i\), the natural map

\[
\varinjlim_i\operatorname{Hom}_A(B,C_i)
\longrightarrow\operatorname{Hom}_A(B,\varinjlim_i C_i)
\tag{3.1}
\]

is bijective.

**Proof.** If \(B=A[t_1,\ldots,t_n]/(r_1,\ldots,r_m)\), a map out of \(B\) is specified by \(n\) elements satisfying \(m\) equations. Lift those elements to a stage and then move to a stage where the equations hold. Equality of two maps is equality on the finitely many generators, and also holds eventually. This proves bijectivity.

For the converse, present \(B\) with possibly infinite sets of generators and relations. Taking finite sets of generators together with finite sets of relations involving them gives a filtered system of finitely presented \(A\)-algebras with colimit \(B\). Surjectivity of (3.1) makes the identity of \(B\) factor through one of these algebras \(D\). Thus \(B\) is a retract of \(D\). If \(e:D\to D\) is the resulting idempotent and \(d_1,\ldots,d_n\) generate \(D\), then \(\ker e\) is generated by \(d_r-e(d_r)\). Indeed, in the quotient by these differences the maps \(e\) and the identity agree on generators and hence everywhere; an element killed by \(e\) is therefore zero in that quotient. The image of \(e\), which is \(B\), is a quotient of the finitely presented algebra \(D\) by a finitely generated ideal. It is finitely presented. \(\square\)

**Theorem 3.2.** For a morphism \(X\to S\), the following are equivalent:

1. \(X\to S\) is locally of finite presentation.
2. For every inverse system of affine \(S\)-schemes \(T_i\), the natural map

\[
\varinjlim_i\operatorname{Hom}_S(T_i,X)
\longrightarrow\operatorname{Hom}_S(\varprojlim_i T_i,X)
\tag{3.2}
\]

is bijective.

If these conditions hold, (3.2) is also bijective for systems of qcqs \(S\)-schemes with affine transition maps. No quasi-compactness or quasi-separatedness assumption on \(X\) is needed.

**Proof.** First suppose \(X\to S\) is locally of finite presentation. We prove uniqueness before existence. Suppose two maps from one stage agree on the limit \(T\). Around their common image at each point of \(T\), choose an affine \(U\subset X\) mapping into an affine \(V\subset S\). Around the image of this point in the stage, choose an affine open on which both maps land in \(U\). If necessary, refine by principal opens of affine stage charts. Finitely many such opens cover \(T\); Lemma 2.1 says they eventually cover the stage. On each open the equality of the two ring maps holds eventually by Lemma 3.1, since \(\Gamma(U)\) is finitely presented over \(\Gamma(V)\). There are finitely many opens, so the maps agree at a common stage. This argument works for qcqs stages as well as affine ones.

Now let \(g:T\to X\) be a map. Cover \(T\) by finitely many affine opens \(W_a\) whose images lie in compatible affine charts \(U_a\to V_a\) of \(X\to S\). By Lemmas 2.1 and 2.3 these opens have affine models \(W_{a,i}\) forming a cover eventually. Their structural maps eventually land in \(V_a\): otherwise the closed complements of the inverse images of \(V_a\) in the \(W_{a,i}\) would remain nonempty and give a point with image outside \(V_a\) at the limit. On \(W_{a,i}\), Lemma 3.1 descends the ring map defining \(g\) into \(U_a\). The resulting local maps agree on each overlap at the limit. Those overlaps form systems of qcqs schemes because the stages are quasi-separated. The uniqueness argument just proved makes their agreements true at a common later stage. The local maps then glue. This proves (3.2) for both kinds of system.

Conversely, assume (3.2) for affine systems. Choose affine \(V\subset S\) and affine \(U\subset X\) mapping to \(V\). The same limit property holds with \(U\) as target. A descended map to \(X\) whose limit lands in \(U\) eventually lands in \(U\), by applying the closed-subset argument to the complement of its inverse image. Equality follows from the equality assertion for \(X\) and the fact that an open immersion is a monomorphism. For systems of affine \(V\)-schemes this is exactly (3.1) with \(A=\Gamma(V)\) and \(B=\Gamma(U)\). Lemma 3.1 proves that every such chart ring map is finitely presented. The affine characterization in the preceding lesson gives local finite presentation. \(\square\)

This is [Stacks, Tag 01ZC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-proposition-characterize-locally-finite-presentation). Surjectivity in (3.2) means existence at a stage. Injectivity means eventual equality. The latter is indispensable: it is what makes a descended diagram commute.

## 4. Descending objects, maps, and properties

Continue with \(S=\varprojlim S_i\), qcqs stages and affine transitions. Once a scheme \(X_{i_0}\) over a stage has been chosen, write \(X_i=X_{i_0}\times_{S_{i_0}}S_i\) and \(X=X_{i_0}\times_{S_{i_0}}S\).

**Theorem 4.1 (finite-presentation descent).** Every scheme of finite presentation over \(S\) has a model of finite presentation over some \(S_i\). A map over \(S\) between two such models descends to a common later stage. Two stage maps that become equal over \(S\) become equal at a later stage.

**Proof for maps and equalities.** Put both models at one stage \(i_0\). The system \(X_i\) is qcqs with affine transitions, and \(Y_{i_0}\to S_{i_0}\) is locally of finite presentation. A map \(X\to Y\) over \(S\) is equivalent to a map \(X\to Y_{i_0}\) over \(S_{i_0}\). The qcqs assertion of Theorem 3.2 descends this map, and its injectivity proves eventual equality. In particular, an isomorphism descends by descending it and its inverse and then their two identity equations.

**Proof for objects.** Choose a finite affine cover of a stage. Pull it back to cover \(S\), and cover \(X\) by finitely many affines \(U_a\), each mapping into one of these affine base opens \(V_a\). Their coordinate rings are finitely presented over \(\Gamma(V_a)\). A finite presentation uses finitely many coefficients, so it gives affine models \(U_{a,i}\) over the corresponding \(V_{a,i}\) at a common stage. These are of finite presentation over \(S_i\), since a quasi-compact open immersion into a quasi-separated scheme is of finite presentation.

The intersections \(U_a\cap U_b\) are quasi-compact. Descend them as quasi-compact opens in both affine models by Lemma 2.1. Each of the resulting overlap models is of finite presentation over \(S_i\). The identification between its two copies descends by the maps assertion already proved; descend its inverse and the inverse identities as well. The domains on which triple-overlap compositions must be compared are quasi-compact opens. Their required identifications become true eventually by Lemma 2.1, and the cocycle identities become true eventually by the equality assertion. Only finitely many overlaps and triples occur, so all requirements hold at a common stage.

Glue the affine models along these identifications. The resulting \(X_i\) is locally of finite presentation over \(S_i\). It has a finite affine cover with quasi-compact pairwise intersections, so it is qcqs. Its morphism to the qcqs scheme \(S_i\) is quasi-compact and quasi-separated. Thus it is of finite presentation. Gluing commutes with the specified base change on its charts, giving \(X_i\times_{S_i}S\cong X\). \(\square\)

The source is [Stacks, Tag 01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation). The theorem can be expressed as an equivalence between the category of finitely presented schemes over \(S\) and the filtered colimit of the corresponding stage categories. The explicit assertions about maps and equalities specify what that categorical phrase means.

**Theorem 4.2 (four eventual properties).** Let \(f_{i_0}:X_{i_0}\to Y_{i_0}\) be a map between schemes of finite presentation over \(S_{i_0}\), and let \(f_i\) and \(f\) be its base changes. If \(f\) is affine, finite, a closed immersion, or separated, respectively, then \(f_i\) has the same property eventually.

**Proof.** Cover \(Y_{i_0}\) by finitely many affines \(V_a\). The inverse images \(f_i^{-1}(V_{a,i})\) are qcqs and have affine transition maps. If \(f\) is affine, their limits are affine. Lemma 2.3 makes all these inverse images affine at a common stage, proving that \(f_i\) is affine.

After that step, write one chart map as \(A_i\to B_i\), with colimit \(A\to B\). The algebra \(B_i\) is of finite type over \(A_i\): the finite-presentation cancellation result from the preceding lesson applies to the maps between the two finitely presented \(S_i\)-schemes. Fix finite algebra generators \(t_1,\ldots,t_n\) at a stage.

If \(B\) is finite as an \(A\)-module, select finitely many module generators \(b_1,\ldots,b_r\) and represent them later. Record finitely many equations expressing \(1\) as a combination of the \(b_a\), and each \(t_\ell b_a\) as a combination of the \(b_a\). Represent the coefficients and make the equations hold at a stage. The module spanned by the stage \(b_a\) contains \(1\) and is stable under every algebra generator. It therefore equals \(B_i\). The chart map is finite. Doing this on the finite cover proves eventual finiteness.

If \(A\to B\) is surjective, each image of \(t_\ell\) is the image of an element of \(A\). Choose stage representatives of those elements and make these finitely many equalities hold eventually. The generators of \(B_i\) then belong to the image of \(A_i\), so \(A_i\to B_i\) is surjective. This proves eventual closed immersion.

Finally, if \(f\) is separated, its diagonal is a closed immersion. Both \(X_{i_0}\) and \(X_{i_0}\times_{Y_{i_0}}X_{i_0}\) are of finite presentation over \(S_{i_0}\). Apply the closed-immersion assertion to the diagonal map and use the diagonal criterion from the first lesson. Each of the four properties survives base change, so truth at one stage implies truth at all later stages. \(\square\)

The precise source locators are [Stacks, Tags 01ZN–01ZQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-affine-finite-presentation).

There are further eventual-property theorems in the same setting: if \(f\) is flat, smooth, étale, or surjective, then \(f_i\) eventually is too. We use their openly licensed proofs at [Stacks, Tag 04AI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-flat-finite-presentation), [Tag 0C0C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-smooth), [Tag 07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale), and [Tag 07RR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-surjective). The first three reduce by finite affine covers to the algebra proofs at [Tag 02JO](https://stacks.math.columbia.edu/tag/02JO), [Tag 0C0B](https://stacks.math.columbia.edu/tag/0C0B), and [Tag 07RI](https://stacks.math.columbia.edu/tag/07RI). Surjectivity uses constructibility of the image, which will be taught with Chevalley’s theorem. These are exact open proof providers, rather than an assertion that every geometric property descends. Their original GNU Free Documentation License applies to those source texts; no source text is reproduced here.

## 5. Noetherian approximation and its use

**Theorem 5.1 (affine approximation).** Every ring \(R\) is the filtered union of its finitely generated \(\mathbf Z\)-subalgebras. Consequently \(\operatorname{Spec}R\) is an inverse limit, with affine transitions, of affine schemes of finite type over \(\mathbf Z\).

**Proof.** For each finite subset \(E\subset R\), take the subring generated by the image of \(\mathbf Z\) and by \(E\). Two such subrings are contained in the subring generated by the union of their finite generating sets. Every element of \(R\) belongs to one of them, and all the maps are inclusions. Thus their filtered colimit is \(R\). The affine part of Theorem 1.1 gives the scheme assertion. Each stage ring is a quotient of a polynomial ring in finitely many variables over \(\mathbf Z\), so it is Noetherian. \(\square\)

**Theorem 5.2 (absolute Noetherian approximation).** Every qcqs scheme \(S\) is an inverse limit of schemes of finite type over \(\mathbf Z\), with affine transition maps.

**Open proof and how to use it.** The full proof is [Stacks, Tag 01ZA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-proposition-approximate), using the extension-of-approximation lemma [Tag 07RN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-approximate) with the empty open. Both proofs are available under the [GNU Free Documentation License, version 1.2](https://github.com/stacks/stacks-project/blob/master/COPYING). The linked extension lemma includes the construction, its index set, the gluing maps, and the verification of the limit. This is the proof provider for the general theorem; the affine argument alone does not prove it.

Here is the geometric role of that construction. Build a scheme by successively adjoining members of a finite affine cover. In a step \(S=V\cup U\) with \(U\) affine, the intersection \(W=V\cap U\) is quasi-compact. Start with an approximation of \(V\), descend \(W\) as an open, and arrange that its models are quasi-affine. Write \(U=\operatorname{Spec}B\), \(R=\Gamma(W,\mathcal O_W)\), and \(R_i=\Gamma(W_i,\mathcal O_{W_i})\). The intermediate ring

\[
B_i=B\times_R R_i
\tag{5.1}
\]

retains both the affine-chart functions and their compatible restrictions on the overlap. Its colimit is \(B\). The extension lemma shows that \(W_i\) embeds as an open in \(\operatorname{Spec}B_i\) eventually, and then in spectra of suitably chosen finite type \(\mathbf Z\)-subalgebras. Gluing those spectra to \(V_i\) produces the next approximations. Quasi-separatedness is used in the quasi-compactness of \(W\); it is not an assumption that the original chart intersection is affine. Formula (5.1) explains why simply approximating chart rings independently would miss the compatibility needed for affine transition maps. This description guides reading the full open proof without replacing its technical gluing argument.

To apply approximation, first put the base in a system supplied by Theorem 5.1 or 5.2. Then use Theorem 4.1 to descend the finitely presented schemes and maps under discussion. Use eventual equality to descend every finite commutative diagram, and Theorem 4.2 or an exact further property theorem to retain the hypotheses needed for a Noetherian argument. Finally bring the conclusion back by a valid base-change or limit argument. Approximation supplies models; it does not by itself prove that an arbitrary conclusion survives passage to the limit.

For example, let \(R\) be a valuation ring, with no finiteness assumption. Its finitely generated \(\mathbf Z\)-subalgebras need not be valuation rings. Nevertheless, any finitely presented \(R\)-algebra has a model over one of them. This is useful when the argument needs a Noetherian model of the algebra, rather than a Noetherian valuation ring carrying all the original valuation data.

## 6. Neighbourhoods and spreading out

Let \(x\) be a point of a scheme \(X\). The affine open neighbourhoods of \(x\), ordered by shrinking, form an inverse system of open subschemes. It is directed because every intersection contains a smaller affine neighbourhood. The transition inclusion between two affine schemes is an affine morphism. The colimit of their coordinate rings is \(\mathcal O_{X,x}\), by the definition of the stalk. Hence

\[
\operatorname{Spec}\mathcal O_{X,x}
\cong\varprojlim_{x\in U\subset X,\ U\text{ affine}}U.
\tag{6.1}
\]

This is a scheme identity, not merely an assertion that the point \(x\) is an intersection of neighbourhoods. The local spectrum includes the generizations of \(x\).

If \(X\) is integral and \(\eta\) is its generic point, (6.1) becomes \(\operatorname{Spec}K(X)\). Finite-presentation descent then extends a finitely presented object over the function field to some affine neighbourhood of \(\eta\), hence to a dense open. Maps between finitely presented objects also extend after shrinking. An identity between two generic maps becomes an identity after another shrinking. The finiteness conditions govern exactly which part of this statement is justified.

For contrast, a finite type object may have infinitely many defining relations. Put \(A=k[x_1,x_2,\ldots]\) and \(B=A/(x_1,x_2,\ldots)=k\). The \(A\)-algebra \(B\) is of finite type but not of finite presentation. Let \(C_n=A/(x_1,\ldots,x_n)\). Then \(\varinjlim C_n=B\), but no \(A\)-algebra map \(B\to C_n\) exists: such a map would make the surviving element \(x_{n+1}\) vanish. The identity of \(B\) does not descend. This is the obstruction that finite presentation removes.

## 7. Exercises with solutions

**Exercise 7.1 (easy: the generic point of a line).** For a field \(k\), order the nonzero polynomials in \(k[t]\) by divisibility, identifying associates if desired. Show that the inverse system \(D(f)\subset\mathbf A^1_k\) has limit \(\operatorname{Spec}k(t)\). Identify its point in the topological limit.

**Solution.** The product of two nonzero polynomials is a common upper bound. The chart rings are \(k[t]_f\), and their filtered colimit inverts every nonzero polynomial, giving \(k(t)\). The affine calculation in Theorem 1.1 gives the limit. A prime ideal of \(k[t]\) occurring in every \(D(f)\) must contain no nonzero polynomial, so it is \((0)\). The unique point of the field spectrum is exactly this compatible generic point.

**Exercise 7.2 (medium: descending an algebra).** Let \(R=\varinjlim R_i\), and let \(B\) be a finitely presented \(R\)-algebra. Construct a finitely presented \(R_i\)-algebra \(B_i\) with \(B_i\otimes_{R_i}R\cong B\). Also explain why two specified maps between such models that agree over \(R\) agree eventually.

**Solution.** Write \(B=R[t_1,\ldots,t_n]/(r_1,\ldots,r_m)\). Lift the finitely many coefficients in the \(r_a\) to a common \(R_i\), and use the lifted polynomials to define \(B_i\). Right exactness of tensor product gives the asserted presentation after base change. For the maps, the images of the finite list of source algebra generators must agree. Each equality in a filtered colimit holds at a later stage, and a common upper bound makes them all hold. This gives equality on the whole algebra.

**Exercise 7.3 (medium: spreading out).** Let \(T\) be integral with function field \(K\). Show that a morphism \(Y_K\to Z_K\) of finite presentation, between schemes of finite presentation over \(K\), has models and a morphism of finite presentation over a dense open \(U\subset T\). If the models of \(Y_K\) and \(Z_K\) are already specified over \(T\), show that the generic morphism extends after shrinking. Preserve a specified generic isomorphism as an isomorphism after shrinking.

**Solution.** Choose an affine neighbourhood \(\operatorname{Spec}A\) of the generic point. Since \(T\) is integral, \(A\) is a domain, and \(K\) is the colimit of the rings \(A_f\) for \(f\ne0\). Theorem 4.1 gives models of the two objects and of their map over some \(A_f\). A morphism between two finitely presented schemes over a base is of finite presentation here: local finite presentation follows by the qualified cancellation result of the preceding lesson, and quasi-compactness and quasi-separatedness follow from the qcqs source and target over this affine base. Thus the extended map has the stated finiteness. If models were already given, restrict them to \(\operatorname{Spec}A\) and use the maps assertion directly. For an isomorphism, descend the inverse too and shrink until the two composite identities hold. The open \(D(f)\) is nonempty and dense. An assertion about an unspecified arbitrary target, without these finite-presentation hypotheses or another applicable theorem, would not follow from this argument.

**Exercise 7.4 (medium: detecting emptiness).** Suppose \(X_i\) are qcqs with affine transitions and \(\varprojlim X_i=\varnothing\). Prove that some \(X_i\) is empty. Is quasi-separatedness needed for this conclusion?

**Solution.** If every \(X_i\) were nonempty, the last assertion of Theorem 1.1 would make the limit nonempty. Its proof uses only a finite affine cover of one stage and the impossibility of \(1=0\) first appearing only in a ring colimit. Quasi-separatedness is therefore unnecessary. Quasi-compactness cannot simply be removed: take the discrete scheme consisting of points numbered \(n,n+1,\ldots\), with transition inclusions as \(n\) increases. These maps are affine, since inverse images of affine opens (finite sets of points) are affine. A compatible point would lie in every tail, and none does, so the limit is empty while each stage is nonempty.

**Exercise 7.5 (hard: a closed immersion at a stage).** Let \(S=\varprojlim S_i\) as above, and let \(X\to S\) be a closed immersion of finite presentation. Show that any finite-presentation model \(X_{i_0}\to S_{i_0}\) becomes a closed immersion eventually. Explain why surjectivity of a colimit ring map alone would not suffice without finite generation.

**Solution.** The inverse images of a finite affine cover of \(S_{i_0}\) have affine limits, so Lemma 2.3 makes them affine eventually. On a resulting chart the map is \(A_i\to B_i\), with \(B_i\) finitely generated as an \(A_i\)-algebra. Its colimit \(A\to B\) is surjective. For each of the finitely many algebra generators of \(B_i\), choose a preimage in \(A\), lift that preimage to a stage, and make the corresponding equality hold at a later stage. The chart map is then surjective. A finite number of charts permits a common stage, proving the claim for the specified model, not just the existence of some model.

For the limitation, use a constant base field \(k\) and \(B_n=k[x_{n+1},x_{n+2},\ldots]\), with the transition to \(B_{n+1}\) killing \(x_{n+1}\). Every element is a polynomial in finitely many variables, so \(\varinjlim B_n=k\). The colimit map from \(k\) is surjective, but no stage map \(k\to B_n\) is surjective. These stage algebras are not of finite type. There is no finite list of generators whose disappearance would prove stage surjectivity.

## Sources and proof dependencies

The primary source is *The Stacks project*, chapter *Limits of Schemes*, read in the AI Integrated Stacks Project edition. Exact open proof locators are supplied where each result is used. Sections 1–4, Theorem 5.1, the examples, and the exercise solutions are proved in this lesson. Absolute Noetherian approximation uses the full open proofs at Tags 01ZA and 07RN; the four additional eventual properties use the exact open proofs and algebra dependencies listed in Section 4. Those source documents retain their GNU Free Documentation License. This independently written teaching text is CC0.

The internal prerequisite is the preceding lesson’s affine descriptions of finite type and finite presentation, their stability under base change and composition, and its qualified cancellation theorem. Scheme gluing, quasi-coherent sheaves on affine schemes, localization, and the finite affine-cover description of quasi-separatedness are used in their usual foundational form. No result here depends on a later lesson. Chevalley’s theorem explains the imported surjectivity proof when it is taught later; that source proof already supplies its own exact openly licensed dependency.
