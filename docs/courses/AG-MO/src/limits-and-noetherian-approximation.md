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

### Eventual flatness, smoothness, étaleness and surjectivity

**Theorem 4.3 (flatness, smoothness, étaleness and surjectivity).** Keep exactly the setting of Theorem 4.2: the stages \(S_i\) are qcqs with affine transitions, \(X_{i_0}\) and \(Y_{i_0}\) are of finite presentation over \(S_{i_0}\), and \(f_i,f\) are the base changes of the specified map \(f_{i_0}\). If \(f\) is flat, smooth, étale, or surjective, respectively, then \(f_i\) has that property eventually.

We prove each assertion. None needs Theorem 5.2 or the later lesson on Chevalley's theorem.

**The local algebra needed for flatness.** We use two proved results of Flatness criteria, dimension and the flat locus. Its Lemma 6.2 gives the following finite-model statement. For a local map \(A\to B\), with \(B\) essentially of finite presentation over \(A\), a finitely presented \(B\)-module that is flat over \(A\) becomes flat in some sufficiently large local Noetherian model. The models are obtained from finite type \(\mathbf Z\)-subrings of \(A\), fixed finite equations for \(B\) and the module, and localization at contracted primes. Its Theorem 5.2 says that the flat locus of a finite module over a finite type algebra over a Noetherian ring is open.

Here is why these are substantive flatness inputs rather than a finite-equations assertion about flatness. At a fixed local Noetherian model \(A_\lambda\to B_\lambda,M_\lambda\), the module

\[
H_\lambda=\operatorname{Tor}_1^{A_\lambda}
(A_\lambda/\mathfrak m_\lambda,M_\lambda)
\]

is finite over \(B_\lambda\): a resolution of the residue field starts with finite free modules, and the tensor homology is a subquotient of finite modules over the Noetherian ring \(B_\lambda\). Each of its finitely many generators has zero image in the kernel of \(\mathfrak m_\lambda A\otimes_A M\to M\), by flatness of the final module. The extended ideal and this tensor product commute with the model colimit, so these generator images vanish at a common stage. Lemma 6.1 of that lesson proves that killing this map of Tor obstructions, together with flatness of the old residue quotient, makes the new module flat. Its proof uses a free presentation and the written ideal local criterion, not a limit-flatness theorem. The openness proof in its Section 5 uses the written domain generic-freeness proof in Flat morphisms and the same ideal criterion. The residue-field local criterion is completely proved in Faithful flatness and the local criterion for flatness, Theorem 4.2. These precise earlier proofs close the local algebra input.

**Affine flatness descent for the specified models.** Suppose \(A=\varinjlim A_i\), \(B_i=B_{i_0}\otimes_{A_{i_0}}A_i\), and \(B_{i_0}\) is finitely presented over \(A_{i_0}\). Put \(B=B_{i_0}\otimes_{A_{i_0}}A\) and suppose \(B\) is flat over \(A\). Fix \(\mathfrak q\in\operatorname{Spec}B\), contracting to \(\mathfrak p\subset A\). Choose finite type \(\mathbf Z\)-subrings \(A_\lambda\subset A\) containing the coefficients of a fixed finite presentation of \(B\), and use the same equations to define \(B_\lambda\). Thus \(B_\lambda\otimes_{A_\lambda}A=B\). Their localizations at \(\mathfrak p_\lambda,\mathfrak q_\lambda\) have colimits \(A_\mathfrak p,B_\mathfrak q\), with transitions given by localizations of base changes. Apply the finite-model statement to \(M_\lambda=(B_\lambda)_{\mathfrak q_\lambda}\). At some stage this module is flat over \((A_\lambda)_{\mathfrak p_\lambda}\), hence also over \(A_\lambda\). Noetherian openness supplies \(g_\lambda\notin\mathfrak q_\lambda\) such that every stalk of \((B_\lambda)_{g_\lambda}\) is flat over \(A_\lambda\). The algebra itself is flat over \(A_\lambda\): for an ideal of \(A_\lambda\), the kernel of its tensor multiplication map localizes to zero at every prime of \((B_\lambda)_{g_\lambda}\), hence is zero. Apply the ideal test for flatness from Tor and flat modules, Theorem 2.1.

We must put this flat neighbourhood into the given system \(A_i\), rather than replacing that system by the Noetherian one. The ring \(A_\lambda\) is finitely presented over \(\mathbf Z\), by the Hilbert basis theorem. Lemma 3.1 lifts its map to \(A\) to a map \(A_\lambda\to A_j\). The finitely many coefficient equalities with the chosen presentation over \(A_{i_0}\) hold at a later stage. There \(B_j=B_\lambda\otimes_{A_\lambda}A_j\). The image \(g_j\) of \(g_\lambda\) therefore satisfies that \((B_j)_{g_j}\) is flat over \(A_j\); its limit open contains \(\mathfrak q\). This argument at every prime gives a principal-open cover of \(\operatorname{Spec}B\). Take a finite subcover \(D(g_1),\ldots,D(g_r)\). Their unit-ideal identity \(1=\sum c_\nu g_\nu\) is a finite equation, so after representing the coefficients and enlarging the stage it holds in \(B_j\). Thus the stage opens cover \(\operatorname{Spec}B_j\), and each has flat coordinate algebra. The ideal test and localization now prove that \(B_j\) is flat over \(A_j\). If \(B=0\), the equation \(1=0\) holds at a stage, and the same conclusion holds for the zero algebra. Base change proves flatness at all subsequent stages.

For the scheme assertion take a finite affine cover of \(Y_{i_0}\), and a finite affine cover of \(X_{i_0}\) subordinate to its inverse images. Their pullbacks to every stage are affine, because the transition maps are affine. The induced chart algebras are finitely presented by the finiteness and cancellation results of the preceding lesson. Flatness of the limit map gives flatness of each limit chart algebra; the affine argument makes every chart flat at one common stage. Since they cover the stage source, \(f_j\) is flat. The equivalence of sheaf and affine module flatness used here is also proved in Flat morphisms, Proposition 1.1: the kernel of a tensor injection is detected by its localizations on the source.

**Finite identities for smoothness and étaleness.** Let

\[
C=A[t_1,\ldots,t_n]/I,\qquad I=(F_1,\ldots,F_m),
\quad P=A[t_1,\ldots,t_n].
\]

The conormal map is

\[
d:I/I^2\longrightarrow C^n,
\qquad [F]\longmapsto
\left(\frac{\partial F}{\partial t_j}\bmod I\right)_j.
\]

For finite presentations, smoothness is equivalent to this map having a left inverse, and étaleness is equivalent to it being an isomorphism. These equivalences, including their comparison with the square-zero lifting definitions, are fully proved in Formally smooth, unramified and étale ring maps, Theorem 3.1 and Section 4. They can also be seen directly as follows. A formal lift of \(\operatorname{id}_C\) across \(P/I^2\to C\) gives a section. Subtract its composite \(P\to C\to P/I^2\) from the quotient \(P\to P/I^2\). Their difference is a derivation into \(I/I^2\), and on \(I\) it is the class map. Its values on the variables define a left inverse of \(d\). Conversely a left inverse gives such a derivation \(D\); the algebra map \(p\mapsto p-D(p)\) into \(P/I^2\) kills \(I\) and gives a section. Any square-zero lifting problem is solved by first lifting the variables to obtain a map from \(P/I^2\), then composing this section. Uniqueness of square-zero lifts is equivalent to the vanishing of the module generated by the \(dt_j\) modulo the \(dF_\ell\): differences of lifts are derivations, and the two maps \(c\mapsto(c,0),(c,dc)\) into \(C\oplus\Omega_{C/A}\) detect every generator of that module. Thus in the formally smooth case uniqueness is exactly surjectivity of \(d\), and hence invertibility of its already split injection.

The useful point is that all the required identities are finite even when relations among the generators of \(I/I^2\) are not known to be finite. Choose polynomials \(U_j\in I\) representing the images of the coordinate basis under a left inverse. Write each \(U_j\) as a finite combination of the \(F_\ell\). A left inverse is equivalent to the finitely many identities

\[
F_\ell-\sum_j
\frac{\partial F_\ell}{\partial t_j}U_j\in I^2
\qquad(1\leq\ell\leq m).
\tag{4.1}
\]

Express each membership by a finite sum of products \(F_aF_b\) with polynomial coefficients. All these polynomials and identities descend through a filtered base colimit. At that stage the map \(C_i^n\to I_i/I_i^2\), sending the coordinate basis to \([U_{j,i}]\), is well defined, and (4.1) makes its composite with \(d_i\) the identity on the generating classes \([F_{\ell,i}]\). Thus the stage algebra is smooth. For étaleness also descend

\[
\frac{\partial U_j}{\partial t_k}-\delta_{jk}\in I
\qquad(1\leq j,k\leq n),
\tag{4.2}
\]

again with finite membership witnesses. These make the opposite composite the identity on \(C_i^n\), so \(d_i\) is an isomorphism and the stage algebra is étale. Empty lists and the zero algebra are allowed. For a specified original presentation the descended equations are obtained by mapping its fixed defining equations to the later stage; eventual coefficient equality keeps the resulting algebra equal to the specified base-change model.

To apply this to schemes, choose finitely many smooth, or étale, affine neighbourhoods covering the limit source and mapping to affine opens pulled back from a finite affine cover of \(Y_{i_0}\). Such chart rings have the above algebraic property, by the affine definitions and their locality in the cited algebra lesson. Lemmas 2.1 and 2.3 descend these source opens as affine opens which eventually cover \(X_i\). Their eventual containment in the inverse images of the chosen target affines follows from Lemma 2.1 as well: both the source open and that inverse image are quasi-compact stage opens, and the containment holds at the limit. Thus their maps to those target affines are defined at a common stage and are finitely presented; fix their presentations at a common stage and apply (4.1), or (4.1)–(4.2). A finite number of charts and identities gives a common stage where the morphism is smooth or étale. Each property survives base change, so all later stages work as well.

**The constructible-image input, proved here.** On \(\operatorname{Spec}A\), call a set constructible when it is a finite Boolean combination of principal opens. Equivalently it is a finite union of pieces

\[
D(a)\cap V(b_1,\ldots,b_s).
\tag{4.3}
\]

First let \(A\) be a domain and \(A\hookrightarrow B\) an injective finite type map. There is a nonzero \(a\in A\) for which \(D(a)\) is in the image of \(\operatorname{Spec}B\). Indeed, over \(K=\operatorname{Frac}A\), the nonzero algebra \(B\otimes_AK\) is finite over an embedded polynomial algebra \(K[z_1,\ldots,z_d]\), by the complete Noether-normalization proof in Krull dimension and Noether normalization, Corollary 3.2. That result allows nilpotents and finite ground fields. Represent the \(z_j\) after inverting finitely many nonzero elements of \(A\). Each member of a finite algebra generating list for \(B\) satisfies a monic equation over \(K[z]\). Invert further denominators to represent all coefficients and to make all the equations true in \(B_a\). An equation that vanishes over \(K\) is killed by a nonzero denominator, so this also handles \(A\)-torsion in \(B\). Independence of the \(z_j\) gives an inclusion \(A_a[z]\hookrightarrow B_a\); the monic equations make it integral. Lying over, proved in Integral extensions, Theorem 3.2, makes its spectrum surject onto the polynomial-ring spectrum, which surjects onto \(\operatorname{Spec}A_a\) because every residue-field polynomial algebra is nonzero. This proves the assertion.

If \(A\) is Noetherian and \(B\) is finite type, its image \(E\) is constructible. For every irreducible closed subset \(Z=V(\mathfrak p)\) in which \(E\cap Z\) is dense, the map \(A/\mathfrak p\to B/\mathfrak pB\) is injective: an element of its kernel vanishes on the dense image, and \(A/\mathfrak p\) is a domain. The preceding argument gives a nonempty relatively open subset of \(Z\) contained in \(E\cap Z\). This condition proves constructibility by Noetherian induction. Explicitly, if some closed \(F\) has nonconstructible intersection with \(E\), choose a minimal such \(F\) by the descending-chain condition. A Noetherian space has finite irreducible decompositions: a minimal closed set without one would be reducible and split into two proper closed sets which already have finite decompositions. Thus, if \(F\) is reducible, its finitely many proper components have constructible intersections by minimality, a contradiction. If \(F\) is irreducible and the intersection is not dense, apply minimality to its proper closure. If it is dense, remove the nonempty open just obtained and apply minimality to the proper closed complement. In every case \(E\cap F\) is a finite union of locally closed subsets, the final contradiction. On a Noetherian affine scheme all opens are quasi-compact and are finite unions of principal opens, so these sets have form (4.3).

For an arbitrary finitely presented map \(A\to B\), choose a finite type \(\mathbf Z\)-subring \(A_0\subset A\) containing its finitely many coefficients, and use those equations to define \(B_0\). Both rings are Noetherian and \(B=B_0\otimes_{A_0}A\). The image at the new base is exactly the inverse image of the old image. To verify the nontrivial direction, a nonempty fibre over \(\kappa(y)\) stays nonempty after the field extension \(\kappa(y)\subset\kappa(y')\): take a nonzero affine fibre ring; tensoring its nonzero vector space with a field extension is nonzero, and a nonzero ring has a prime. Conversely a nonempty new fibre maps to the old fibre. Thus the constructible description of the Noetherian image pulls back to the desired finite description over \(A\). A quasi-compact, locally finitely presented scheme morphism has constructible image on each affine target open: its inverse image has a finite affine cover, each chart has a finitely presented algebra, and the full image is the finite union of the chart images. This proof used affine approximation only; it does not import a later Chevalley theorem or absolute approximation.

**Detecting a constructible condition at a stage.** Let \(T=\varprojlim T_i\) with qcqs stages and affine transitions. Suppose \(E\subset T_{i_0}\) is constructible on each affine of a finite cover, and every point of \(T\) maps into \(E\). Then all points of \(T_j\) map into \(E\) at some stage \(j\). On an affine chart the complement of \(E\) is a finite union of pieces (4.3). For a piece, use the closed subschemes defined by \((b_1,\ldots,b_s)\) inside the inverse images of \(D(a)\) at each stage. These are affine schemes with affine transitions. Their limit is the corresponding closed subscheme in the limit chart, and is empty. Theorem 1.1 makes a stage empty. A common stage handles the finitely many pieces on the finitely many charts. This proves the detection assertion, with no separatedness assumption.

Now take \(E=f_{i_0}(X_{i_0})\subset Y_{i_0}\). The constructible-image proof applies because the specified map is of finite presentation. Base-change equality of images gives \(f_i(X_i)=p_i^{-1}(E)\), where here \(p_i:Y_i\to Y_{i_0}\). The same holds at the limit. If \(f\) is surjective, every point of \(Y\) maps into \(E\). Detection makes \(p_j^{-1}(E)=Y_j\), so \(f_j\) is surjective. Surjectivity survives every base change by the fibre argument above, and therefore holds at every later stage. This finishes the proof of Theorem 4.3. \(\square\)

The free primary comparisons are [Stacks, Tag 04AI](https://stacks.math.columbia.edu/tag/04AI), [Tag 0C0C](https://stacks.math.columbia.edu/tag/0C0C), [Tag 07RP](https://stacks.math.columbia.edu/tag/07RP), and [Tag 07RR](https://stacks.math.columbia.edu/tag/07RR). The proofs above and the precisely named, already written algebra and flatness lessons supply the arguments within the programme.

## 5. Noetherian approximation and its use

**Theorem 5.1 (affine approximation).** Every ring \(R\) is the filtered union of its finitely generated \(\mathbf Z\)-subalgebras. Consequently \(\operatorname{Spec}R\) is an inverse limit, with affine transitions, of affine schemes of finite type over \(\mathbf Z\).

**Proof.** For each finite subset \(E\subset R\), take the subring generated by the image of \(\mathbf Z\) and by \(E\). Two such subrings are contained in the subring generated by the union of their finite generating sets. Every element of \(R\) belongs to one of them, and all the maps are inclusions. Thus their filtered colimit is \(R\). The affine part of Theorem 1.1 gives the scheme assertion. Each stage ring is a quotient of a polynomial ring in finitely many variables over \(\mathbf Z\), so it is Noetherian. \(\square\)

### Absolute Noetherian approximation

**Theorem 5.2 (absolute Noetherian approximation).** Every qcqs scheme \(S\) is an inverse limit of schemes of finite type over \(\mathbf Z\), with affine transition maps.

**Proof.** We construct an approximation by adding one affine open at a time. The following three facts make the gluing precise.

*Principal-open criterion.* If a qcqs scheme \(T\) has global functions \(h_1,\ldots,h_r\) such that its opens \(T_{h_\nu}\) are affine and cover \(T\), the canonical map

\[
T\longrightarrow\operatorname{Spec}\Gamma(T,\mathcal O_T)
\]

is an open immersion with image \(\bigcup_\nu D(h_\nu)\). Indeed (2.1) identifies the coordinate algebra of each affine \(T_{h_\nu}\) with the corresponding localized global algebra. The chart isomorphisms agree on intersections and glue. This also proves the target-local test for an affine morphism used below. If a morphism is affine over the members of an open target cover, cover any affine target open by finitely many principal opens subordinate to that cover. Their inverse images are affine and cover the inverse image of the target open. Their pairwise intersections are principal inside these affine inverse images, so that source is qcqs. The pulled-back functions generate the unit ideal, since they do so on the affine target. The criterion identifies the source with its entire global spectrum, proving that this inverse image is affine. Hence the morphism is affine. In particular, a quasi-compact open in an affine scheme has such a finite cover, by principal opens of the ambient affine. If \(T=\varprojlim T_i\) is quasi-affine, choose such functions at the limit, descend them by Lemma 2.2, make them a cover by Lemma 2.1, and make each resulting open affine by Lemma 2.3. Thus \(T_i\) is quasi-affine eventually. This conclusion uses only Section 2, before absolute approximation.

*Finite type affine ambient rings.* Let a scheme \(W\) of finite type over \(\mathbf Z\) be embedded as the quasi-compact open \(\bigcup_{\nu=1}^rD_R(h_\nu)\) in \(\operatorname{Spec}R\). There are arbitrarily large finitely generated \(\mathbf Z\)-subrings \(A\subset R\), containing all \(h_\nu\), such that

\[
A_{h_\nu}\xrightarrow{\sim}R_{h_\nu}\quad\text{for every }\nu.
\tag{5.2}
\]

Each \(R_{h_\nu}\) is a finite type \(\mathbf Z\)-algebra, being the coordinate ring of the affine open \(D_R(h_\nu)\) in the Noetherian finite type scheme \(W\). Choose a finite algebra generating list and write its members as \(y/h_\nu^e\) with \(y\in R\). Adjoin all these numerators and the \(h_\nu\) to the image of \(\mathbf Z\). The resulting ring has surjective localization maps in (5.2). They are injective: an element of a subring killed in the ambient localization is already killed by the same power of \(h_\nu\) in the subring. Thus (5.2) holds. Any finitely generated enlargement inside \(R\) still has the same localized rings. The choices therefore form a directed collection, include any specified finite subset of \(R\), and exhaust \(R\). The identifications (5.2) and their further localizations embed \(W\) as \(\bigcup_\nu D_A(h_\nu)\subset\operatorname{Spec}A\).

*Localizing a fibre product.* For ring maps \(B\xrightarrow{s}R\xleftarrow{t}R'\), put \(B'=B\times_RR'\). Suppose \(h=(g,f)\in B'\), so \(s(g)=t(f)\). Then

\[
(B')_h\cong B_g\times_{R_{s(g)}}R'_f.
\tag{5.3}
\]

View \(B\oplus R'\to R\), \((b,r')\mapsto s(b)-t(r')\), as a map of \(B'\)-modules. Its kernel is \(B'\). Localization is exact, and localization by \(h\) on the three modules is respectively localization by \(g,f,s(g)\). Consequently its localized kernel is precisely the fibre product on the right of (5.3); the identification respects ring multiplication. If \(B_g\to R_{s(g)}\) is an isomorphism, (5.3) reduces to \((B')_h\cong R'_f\). This proves the algebraic compatibility we will need, without any injectivity assumption on either map to \(R\).

Now suppose \(S=V\cup U\), with \(U=\operatorname{Spec}B\) affine and \(V\) quasi-compact open, and suppose we have already constructed

\[
V=\varprojlim_{i\in I}V_i
\]

with finite type \(\mathbf Z\)-schemes \(V_i\) and affine transitions. Quasi-separatedness of \(S\) makes \(W=V\cap U\) quasi-compact. Descend it to an open \(W_{i_0}\subset V_{i_0}\) by Lemma 2.1, and for \(i\geq i_0\) let \(W_i\) be its inverse image. Thus \(W_j\) is exactly the inverse image of \(W_i\) in \(V_j\), their transitions are affine, and \(W=\varprojlim W_i\). The \(W_i\) are of finite type over \(\mathbf Z\), since they are quasi-compact opens in Noetherian finite type schemes. Put

\[
R=\Gamma(W,\mathcal O_W),\qquad R_i=\Gamma(W_i,\mathcal O_{W_i}),
\qquad B_i=B\times_R R_i.
\tag{5.1}
\]

Lemma 2.2 gives \(R=\varinjlim R_i\). Projection gives \(\varinjlim B_i\cong B\): for \(b\in B\), lift its restriction in \(R\) to some \(R_i\), obtaining the pair \((b,r_i)\); a pair mapping to zero in \(B\) has second coordinate eventually zero in the \(R_i\), so is eventually zero. This also proves injectivity, even if the restriction map \(B\to R\) is not injective.

Choose \(g_1,\ldots,g_r\in B\) with \(W=\bigcup_\nu D_B(g_\nu)\), every displayed principal open being contained in \(W\). Lift their restrictions \(s(g_\nu)\) to global functions \(f_{\nu,i}\in R_i\) at one common stage and pull them back at subsequent stages. At the limit the opens \(W_{s(g_\nu)}=D_B(g_\nu)\) are affine and cover \(W\). Lemmas 2.1 and 2.3 make the opens \((W_i)_{f_{\nu,i}}\) affine and a cover at a common later stage. The principal-open criterion therefore embeds \(W_i\) as

\[
\bigcup_\nu D_{R_i}(f_{\nu,i})\subset\operatorname{Spec}R_i.
\tag{5.4}
\]

By (2.1), \(B_{g_\nu}\cong R_{s(g_\nu)}\). Apply (5.3) to \(h_{\nu,i}=(g_\nu,f_{\nu,i})\in B_i\). It gives

\[
(B_i)_{h_{\nu,i}}\cong (R_i)_{f_{\nu,i}}.
\tag{5.5}
\]

These identifications are compatible on pairwise intersections: localizing once more by any \(h_{\mu,i}\) corresponds to localizing by \(f_{\mu,i}\) on \(R_i\). They embed \(W_i\) as the open \(\bigcup_\nu D_{B_i}(h_{\nu,i})\) in \(\operatorname{Spec}B_i\). If \(W\) is empty, first make \(W_i\) empty by Theorem 1.1; then \(R_i=0\), \(B_i=B\), and the same construction uses an empty list of opens.

Apply the finite type affine ambient-ring fact to this embedding of \(W_i\). Let \(\mathcal A_i\) be the collection of finitely generated \(\mathbf Z\)-subrings \(A\subset B_i\) containing the \(h_{\nu,i}\) and satisfying

\[
A_{h_{\nu,i}}\xrightarrow{\sim}(B_i)_{h_{\nu,i}}.
\tag{5.6}
\]

The collection is directed and contains a member containing any finite subset of \(B_i\). Glue \(V_i\) and \(U_{i,A}=\operatorname{Spec}A\) along the identified open \(W_i\). Denote the result by \(S_{i,A}\). Both pieces are of finite type over \(\mathbf Z\), and they are a finite open cover, so \(S_{i,A}\) is of finite type over \(\mathbf Z\). No separatedness is imposed by this gluing.

For completeness we specify the directed index set and the transitions. Let

\[
J=\{(i,A): i\geq i_0,\ A\in\mathcal A_i\},
\]

ordered by \((i,A)\leq(j,A')\) when \(i\leq j\) and the image of \(A\) under \(B_i\to B_j\) is contained in \(A'\). It is a directed set: choose a common later \(j\) for finitely many indices, then an ambient ring containing the images of all their finite generating lists and the \(h_{\nu,j}\). The projection \(J\to I_{\geq i_0}\) is cofinal. The ring map \(A\to A'\) and the scheme map \(V_j\to V_i\) agree on \(W_j\to W_i\), by (5.5)–(5.6), so glue to a map \(S_{j,A'}\to S_{i,A}\).

These maps are affine, which is the crucial extra requirement. The inverse image of \(W_i\) in \(U_{j,A'}\) is exactly \(W_j\): the image of \(h_{\nu,i}\) is \(h_{\nu,j}\), and both opens are the indicated finite unions of principal opens. The inverse image of \(W_i\) in \(V_j\) is also exactly \(W_j\), by the original descended-open construction. Hence the inverse images of the two target opens \(V_i\) and \(U_{i,A}\) are precisely \(V_j\) and \(U_{j,A'}\), respectively. On them the map is respectively the original affine transition and a map between affine schemes. Affineness is local on the target, so the glued transition is affine. The same description proves compatibility of all transition compositions. In particular, no chart intersection has been presumed affine inside \(V_i\).

There are compatible maps \(S\to S_{i,A}\), induced on \(V\) by its original projections and on \(U\) by \(A\to B_i\to B\). They agree on \(W\), by (5.5). Their inverse images of \(V_i,U_{i,A}\) are exactly \(V,U\): on \(U\), the relevant principal opens are \(D_B(g_\nu)\), whose union is \(W\); on \(V\) the overlap is the inverse image of \(W_i\). The affine-chart ring colimit \(\varinjlim_J A\) is \(B\). Every element of \(B\) lifts to some \(B_i\), then belongs to an ambient subring there. An element of some \(A\) whose image in \(B\) is zero becomes zero in a later \(B_j\), and in a suitable later ambient subring its image is therefore zero. This verifies both surjectivity and injectivity of the colimit map, without pretending the maps \(B_i\to B_j\) are inclusions.

Finally fix one pair in \(J\) and restrict to its cofinal upper cone. Theorem 1.1 constructs the limit on the inverse images of the covering opens \(V_i\) and \(U_{i,A}\). These limits are \(V\) and \(\operatorname{Spec}B=U\), by cofinality and the ring calculation. Their overlap limit is \(W\), with its actual given identifications into both pieces. The resulting glued limit is thus \(V\cup_WU=S\). This proves extension of an approximation across one affine open, including the affineness of every transition.

A qcqs scheme has a finite affine open cover. Start with the constant empty approximation, and successively add the affines of such a cover. Each partial union is a quasi-compact open in \(S\), hence is qcqs, and each overlap needed above is quasi-compact. The extension construction applies a finite number of times. The final system proves Theorem 5.2. \(\square\)

The free primary references for the theorem and the extension construction are [Stacks, Tag 01ZA](https://stacks.math.columbia.edu/tag/01ZA) and [Tag 07RN](https://stacks.math.columbia.edu/tag/07RN); the affine ambient and fibre-product comparisons are [Tags 01Z7](https://stacks.math.columbia.edu/tag/01Z7) and [01Z9](https://stacks.math.columbia.edu/tag/01Z9). All required construction and verification have been given above.

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

The free primary reference is *The Stacks project*, chapter *Limits of Schemes*. Tags 01YW–01YY, 01Z2–01Z4, 01Z0, 01Z6, 01ZC and 01ZM–01ZQ identify the original limit and finite-presentation results. Tags 04AI, 0C0C, 07RP and 07RR identify the four further eventual properties; their algebra comparisons are [02JO](https://stacks.math.columbia.edu/tag/02JO), [0C0B](https://stacks.math.columbia.edu/tag/0C0B) and [07RI](https://stacks.math.columbia.edu/tag/07RI). Tags 01ZA, 07RN, 01Z7 and 01Z9 identify the approximation theorem and its construction. These are mathematical references, not external substitutes for the proofs now supplied in the lesson. Stacks source expression retains its GNU Free Documentation License; this independently expressed lesson is CC0.

All original results, examples, formulas and exercise solutions have been retained. Sections 1–4, both approximation theorems, all examples and all five exercises are proved here. The flatness proof uses the already written local Noetherian-model and openness proofs of *Flatness criteria, dimension and the flat locus*, Section 6, Lemmas 6.1–6.2 and Section 5, Theorem 5.2. Only those proof scopes are used: their local criterion comes from *Faithful flatness and the local criterion for flatness*, Section 4, Theorem 4.2, and their generic-freeness input from *Flat morphisms*, Section 5, Lemma 5.1. They do not use this lesson's new eventual-property theorem or its absolute-approximation theorem. The local criterion in turn has actual complete Artin–Rees and Krull-intersection proofs in *Noetherian and Artinian rings*, Theorems 5.1 and 6.1; the Hilbert basis theorem is its Theorem 2.1. The flat module ideal test and stability are proved in *Tor and flat modules*, Theorem 2.1 and Section 3. The smooth/étale algebra input is also proved directly in the present finite-identity argument and matches *Formally smooth, unramified and étale ring maps*, Theorem 3.1 and Section 4. The constructible-image argument is proved here from the complete Noether-normalization proof in *Krull dimension and Noether normalization*, Corollary 3.2, and the complete lying-over proof in *Integral extensions*, Theorem 3.2. It uses neither a later Chevalley lesson nor absolute approximation.

The preceding finiteness lesson supplies the affine finite-presentation characterizations, base-change and composition rules, and qualified cancellation theorem. Scheme and morphism gluing have complete earlier proofs in Schemes, gluing and immersions, Theorem 2.1. The affine quasi-coherent correspondence and the correspondence for maps into a spectrum are proved in Affine schemes, Theorems 3.2 and 4.1. The finite affine-cover description of quasi-separatedness is proved in the first morphisms lesson, Proposition 2.2; intersections of quasi-compact opens are then finite unions of affine-open intersections, as proved in Quasi-coherent sheaves on schemes, Section 2. The Noetherian scheme locality and finite-cover assertions have the full proof in Properties of schemes, Theorem 3.2. Localization is exact by *Localization, local properties and support*, Theorem 2.1. In the new approximation proof, every extra localization, overlap, directedness, transition and colimit step is proved explicitly. Arbitrary qcqs schemes, nonseparated overlaps, nonreduced algebras, empty opens and noninjective transition maps remain within the stated scope.
