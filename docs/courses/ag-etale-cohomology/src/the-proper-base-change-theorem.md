# The proper base change theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

A higher direct image records cohomology near a point of the base. Proper base change says that, with torsion coefficients, its geometric stalk is already the cohomology of the fibre. The neighbourhood can be replaced by the fibre without losing a class. We prove this by making resolutions work on a projective-line fibre, then using finite maps and projective geometry to reach every proper morphism.

We use the actual finite-map and continuity results of [Pushforward, pullback and finite morphisms](pushforward-pullback-and-finite-morphisms.md), constructible approximation from [Constructible sheaves and extension by zero](constructible-sheaves-and-extension-by-zero.md), and the canonical field-extension comparisons in [Torsion sheaves on curves](torsion-sheaves-on-curves.md). The sheaf cohomology, torsor and Leray conventions are those of [Cohomology on sites](cohomology-on-sites.md). Section 2 identifies the additional geometric foundations. No proper base change theorem is used as a premise.

## 1. The comparison map and the theorem

For a cartesian square write

\[
\begin{matrix}
X'=X\times_Y Y'&\xrightarrow{a}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y.
\end{matrix}
\tag{1.1}
\]

All sheaves are on the small étale sites. The inverse image \(a^{-1}\) is exact; it means inverse image of a sheaf, including its coefficients. In degree zero the comparison

\[
g^{-1}f_*\mathcal F\longrightarrow f'_*a^{-1}\mathcal F
\tag{1.2}
\]

is adjoint to applying \(f_*\) to the unit \(\mathcal F\to a_*a^{-1}\mathcal F\). Its derived version is

\[
\beta_{f,g}(E):g^{-1}Rf_*E\longrightarrow Rf'_*a^{-1}E.
\tag{1.3}
\]

One construction uses an injective resolution on \(X\), followed by a resolution of its exact inverse image on \(X'\). Applying (1.2) and the resolution comparison gives (1.3). The uniqueness of resolution comparisons up to homotopy proves naturality in \(E\). Units for composite adjunctions show compatibility with successive base changes and with composition of direct images. In particular, the induced maps in long exact sequences commute with the connecting maps. These are statements about the canonical map, not choices of abstract isomorphisms between cohomology groups.

**Theorem 1.1 (proper base change).** If \(f\) is proper, \(g\) is arbitrary and \(\mathcal F\) is a torsion abelian sheaf, (1.3) is an isomorphism for \(E=\mathcal F[0]\). Equivalently, every map

\[
g^{-1}R^qf_*\mathcal F\longrightarrow R^qf'_*a^{-1}\mathcal F
\tag{1.4}
\]

is an isomorphism. No Noetherian hypothesis, finite presentation hypothesis beyond properness, common annihilator, or condition on the residue characteristics is imposed on \(\mathcal F\).

The same conclusion holds for \(E\in D^+(X_{\mathrm{ét}})\) whose cohomology sheaves are torsion. Moreover, for a geometric point \(\bar y\to Y\),

\[
(R^qf_*\mathcal F)_{\bar y}
\cong H^q(X_{\bar y},\mathcal F_{\bar y}),
\qquad \mathcal F_{\bar y}=\mathcal F|_{X_{\bar y}}.
\tag{1.5}
\]

Theorem 1.1 will be proved in section 11. Its degree-zero part holds for every sheaf of sets, with no torsion condition. That stronger assertion supplies the comparison of complexes in the proof.

## 2. Geometric foundations and henselian conventions

A **henselian pair** \((A,I)\) has \(I\) in the Jacobson radical and has the lifting property for relatively prime monic factorizations modulo \(I\). We use its equivalent idempotent formulation: for every integral \(A\)-algebra \(B\), idempotents of \(B\) and \(B/IB\) correspond bijectively. For finite algebras this follows by lifting the two factors of the characteristic polynomial determined by an idempotent; passage to integral algebras follows from their filtered finite subalgebras. Conversely an idempotent splitting of \(A[T]/(h)\) lifts a relatively prime factorization of a monic \(h\) by taking characteristic polynomials on the two finite projective summands. Their ranks are constant where specified modulo \(I\), because every closed point lies over \(V(I)\). Thus these formulations agree. The complete characterization, including arbitrary integral algebras, is [Tag 09XI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-characterize-henselian-pair); the lifting of idempotents in integral algebras over a henselian pair is also proved in [Étale neighbourhoods, henselization and quasi-finite morphisms](course:AG-FSE/AG-FSE-07), Lemma 5.3.

An integral \(A\)-algebra \(B\) again gives a henselian pair \((B,IB)\): every algebra integral over \(B\) is integral over \(A\), so the same idempotent criterion applies. In particular, if \(B\) is a nonzero domain integral over \(A\), then \(\operatorname{Spec}(B/IB)\) is nonempty and connected. It is nonempty since \(IB\) lies in the Jacobson radical; a nontrivial clopen decomposition would lift to a nontrivial idempotent in the domain \(B\).

The following geometric theorems are used in their indicated scope. They belong to the prerequisites on proper morphisms, finite morphisms and formal existence, rather than to the étale cohomology theorem being proved.

- **Stein factorization, including non-Noetherian bases.** A proper \(T\to S\) factors as a proper morphism with geometrically connected, nonempty fibres onto \(S'=\operatorname{Spec}_S(f_*\mathcal O_T)\), followed by an integral morphism \(S'\to S\). The latter need not be finite over an arbitrary base. This is [Tag 03H2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-stein-factorization-general).
- **Finite étale covers over a proper henselian base.** If \(A\) is henselian local and \(T\) is proper over \(A\), restriction gives an equivalence between finite étale covers of \(T\) and its closed fibre \(T_0\), [Tag 0A48](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian). Its proof is recalled below to specify the formal inputs and avoid a cohomological circularity.
- **Geometric approximation.** Quasi-compact, quasi-separated schemes admit absolute Noetherian approximation with affine transition maps. Schemes and maps of finite presentation, finite étale maps, finite constructible presentations and their morphisms descend to a sufficiently large stage. Integral maps are limits of finite maps of finite presentation. These are the finite-data geometry and sheaf approximation inputs already used in lessons 7 and 11.
- **Zariski's Main Theorem and Chow's lemma.** A separated quasi-finite morphism factors through an open subscheme of an integral scheme over its target; the finite-type finite version is used when available. For separated finite-type \(T\to S\), with \(S\) quasi-compact and quasi-separated, Chow gives \(T'\to T\) proper surjective and an immersion \(T'\to\mathbf P^n_S\). Chow's lemma is used without proof ([Tag 0202](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-chow-finite-type)). Zariski's Main Theorem in this form is proved in [Zariski's Main Theorem](course:AG-MO/AG-MO-12), Theorem 4.2 (also [Tag 05K0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite)), and proper quasi-finite morphisms are finite by Theorem 5.1 there (also [Stacks, Tag 02LS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-characterize-finite)).

Here is the geometric proof mechanism for the finite étale equivalence. If \(A\) is complete Noetherian local, a finite étale cover of \(T_0\) lifts uniquely through all nilpotent thickenings \(T_n\). Grothendieck's existence theorem for a coherent algebra finite over a proper scheme algebraizes that compatible system to a finite \(T\)-scheme. The algebra is étale near \(T_0\) by the infinitesimal criterion. Every point of a scheme proper over a local base specializes into the closed fibre, so the étale locus is the whole scheme. A morphism between two covers lifts by applying existence to its graph in their fibre product. The graph projection is finite étale of degree one on the closed fibre, hence is an isomorphism everywhere. Uniqueness follows from the uniqueness on all thickenings and existence's full faithfulness.

For a henselian Noetherian local G-ring, first pass to its completion. The cover there descends to an algebra of finite type over \(A\). Artin approximation supplies a map from that algebra to \(A\) agreeing with the completion map modulo the maximal ideal; the descended finite étale cover therefore has the required closed fibre. Full faithfulness follows by the graph argument. Finally an arbitrary henselian local ring is a filtered colimit of henselizations of local rings essentially of finite type over \(\mathbf Z\), which are Noetherian G-rings. Descend the proper scheme, the covers and the finite-presentation morphisms between covers, and apply the preceding equivalence at a stage. This proves the equivalence at the limit. This proof uses coherent formal existence, Artin approximation and the descent of finite data; no statement about higher étale direct images occurs in this proof.

We will also use the usual spectral topology of a quasi-compact, quasi-separated scheme. Quasi-compact opens form a basis closed under finite intersection, and the constructible topology is compact Hausdorff. A subset closed in that topology and stable under specialization is Zariski closed. These follow from the prime-spectrum finite-intersection argument and remain valid under a finite affine covering. They apply to closed subspaces as well.

## 3. Why sections on a spectral space can be recovered from a closed subset

**Lemma 3.1 (clopen extension).** Let \(W\) be spectral and \(Z\subset W\) closed. Suppose that

\[
Z\cap\overline{\{w\}}\text{ is nonempty and connected for every }w\in W.
\tag{3.1}
\]

Every clopen partition of \(Z\) extends uniquely to a clopen partition of \(W\).

*Proof.* For a partition \(Z=Z_1\amalg Z_2\), let \(W_i\) consist of points with a specialization in \(Z_i\). Condition (3.1) says that each point belongs to exactly one \(W_i\). These sets are closed in the constructible topology: the specialization relation is closed there, and its projection from the compact set with second coordinate in \(Z_i\) is closed. Each \(W_i\) is stable under specialization. Indeed a specialization \(w\leadsto v\) has a further specialization in \(Z\); its part is also the unique part met by \(\overline{\{w\}}\). Thus both \(W_i\) are Zariski closed and complementary, hence clopen. Any extending clopen partition must put a point in the same part as each of its specializations in \(Z\), proving uniqueness. Repetition gives every finite partition. ∎

**Lemma 3.2 (finite models of sheaves).** Every sheaf of sets on a spectral space is a filtered colimit of finite presentations made from finitely many sheaves \(j_{U!}\underline E\), with \(U\) quasi-compact open and \(E\) finite. Each such finite presentation embeds in a finite product of sheaves \(i_*\underline E\), with \(i\) a closed-subspace inclusion and \(E\) finite.

*Proof.* The extension \(j_!\) for sets means extension by the empty set. Every germ of a sheaf \(\mathcal F\) is represented by a section on some quasi-compact open. The corresponding maps from \(j_{U!}\underline{\{*\}}\) give an epimorphism \(P\to\mathcal F\). Apply the same construction to its relation sheaf \(P\times_{\mathcal F}P\). We obtain a coequalizer of two maps between coproducts of these generators. A section of a coproduct over a quasi-compact open uses only finitely many summands: its locally specified summands have a finite covering subfamily. Thus finitely many relations involve finitely many generators. Taking all finite such choices expresses \(\mathcal F\) as the stated filtered colimit.

A finite presentation descends to a finite sober space. To see the finite-data assertion, let finite sublattices of the lattice of quasi-compact opens grow to the whole lattice. Their finite spectra are finite sober spaces, and their inverse limit recovers \(W\): a point is determined by the quasi-compact opens containing it, and a compatible lattice-prime system is such a point. Finitely many opens in a presentation descend to one finite spectrum. Each of the finitely many sections defining its relation maps is locally specified on a finite cover; its finitely many equality conditions hold after adjoining finitely many further quasi-compact opens. The relation maps therefore also descend. Inverse image preserves coproducts and coequalizers, so the descended sheaf pulls back to the given one.

For a sheaf \(G\) with finite stalks on a finite sober space \(P\), the germ maps give

\[
G\lhook\joinrel\longrightarrow\prod_{p\in P}(i_p)_*G_p.
\tag{3.2}
\]

Injectivity follows because every germ is tested. The sheaf \((i_p)_*G_p\) is constant on \(\overline{\{p\}}\) and pushed forward from that closed set: every nonempty open of this irreducible finite space contains its generic point \(p\). Pullback of this closed pushforward is the closed pushforward of the constant sheaf from the inverse-image closed set, as can be checked on stalks. Pulling back (3.2) proves the embedding. ∎

**Proposition 3.3 (all Zariski sheaves).** Under (3.1), every sheaf of sets \(\mathcal F\) has a bijective restriction map

\[
\Gamma(W,\mathcal F)\longrightarrow\Gamma(Z,\mathcal F|_Z).
\tag{3.3}
\]

*Proof.* A specialization \(w\leadsto z\) gives a map of germs \(\mathcal F_z\to\mathcal F_w\). Hence agreement on \(Z\) implies agreement everywhere, proving injectivity. Sections on a quasi-compact, quasi-separated space commute with filtered colimits of sheaves: choose finite local representatives and a finite covering of the equality conditions on overlaps. The same holds on its closed subspace. Lemma 3.2 reduces surjectivity to a finitely presented sheaf \(\mathcal F\) embedded in a finite product \(G\) of closed pushforwards of finite constants.

For a closed subspace \(T\subset W\), condition (3.1) is inherited, since the closure of a point of \(T\) lies in \(T\). Lemma 3.1 identifies the finite locally constant maps \(T\to E\) with those on \(T\cap Z\). Thus (3.3) is bijective for every factor of \(G\), and for \(G\). A section of \(\mathcal F|_Z\) lifts uniquely to \(s\in\Gamma(W,G)\). Its germ at every \(z\in Z\) lies in the subsheaf \(\mathcal F\). Specializing any \(w\) to such a \(z\) shows that \(s_w\) also lies in \(\mathcal F_w\). Membership in a subsheaf is local, so \(s\) is a section of \(\mathcal F\). ∎

## 4. Proper henselian schemes and the degree-zero theorem

**Lemma 4.1.** If \(X\) is proper over a henselian pair \((A,I)\), put \(Z=X\times_A\operatorname{Spec}(A/I)\). Then (3.1) holds, also after every finite morphism \(T\to X\).

*Proof.* Give the closure of a point its reduced scheme structure and call it \(C\). It is irreducible and proper over \(A\). Its Stein factorization has integral \(A\)-algebra \(B=\Gamma(C,\mathcal O_C)\), a domain because \(C\) is reduced and irreducible. The pair \((B,IB)\) is henselian, and \(\operatorname{Spec}(B/IB)\) is nonempty and connected by section 2. The map

\[
C\times_A\operatorname{Spec}(A/I)\longrightarrow\operatorname{Spec}(B/IB)
\]

is closed, surjective and has connected fibres. Its source is therefore connected: a clopen separation would give, by closedness and connectedness of each fibre, a clopen separation of the target. This proves (3.1). A scheme finite over \(X\) is again proper over \(A\), so the same proof applies there. ∎

**Lemma 4.2 (finite refinement of an étale covering).** If \(X\) is quasi-compact and quasi-separated and \(U\to X\) is a surjective étale morphism, some finite surjective morphism of finite presentation \(T\to X\) factors Zariski locally through \(U\).

*Proof.* Choose finitely many affine pieces of \(U\) covering \(X\), so \(U\) can be taken quasi-compact and separated and its geometric fibre degrees have a bound \(d\). We prove the existence first with “finite” in place of “finite of finite presentation,” by induction on this bound. For \(d=1\), the surjective étale map with singleton geometric fibres is an isomorphism. Otherwise the finite form of Zariski's Main Theorem embeds \(U\) as a quasi-compact open in a finite \(Y\to X\). Replace \(Y\) by the schematic closure of \(U\); it is still finite and surjective over \(X\).

In \(U\times_XY\), the graph of \(U\to Y\) is both open and closed; call its complement \(V\). The image \(W\subset Y\) of \(V\to Y\) is a quasi-compact open containing \(Y-U\). Its étale fibre degrees are at most \(d-1\): over the dense \(U\) one lift has been removed, and the degree of a quasi-compact separated étale morphism is lower semicontinuous, so it cannot increase under specialization. By induction, a finite surjection \(T_W\to W\) locally factors through \(V\), hence \(U\). The composite \(T_W\to Y\) is quasi-finite and separated; apply the finite form of Zariski's Main Theorem again to embed it as an open in a finite \(T_Y\to Y\). Replace \(T_Y\) by the schematic closure of \(T_W\). Its inverse image over \(W\) equals \(T_W\), since that open is also closed there, being finite over \(W\).

Adjoin the reduced closed scheme \(Y-W\). The resulting finite map \(T_Y\amalg(Y-W)\to X\) is surjective: it covers \(W\) and its complement in \(Y\). It locally factors through \(U\); over \(W\) use the induction, and at a point over \(Y-W\subset U\) use the inverse image of the open \(U\). This proves the finite version.

Write that finite cover as a limit of finite covers of finite presentation. Choose a finite open covering on which the factorization exists. The opens, their maps to \(U\), and the covering condition descend to one stage, by finite presentation and quasi-compactness. This stage is surjective because the limit cover maps onto \(X\). It has all the required properties. ∎

**Lemma 4.3 (from Zariski to étale sections).** Suppose \(Z\subset X\) is closed, \(X\) is quasi-compact and quasi-separated, and (3.3) holds for all Zariski sheaves both on \(X\) and on every finite \(T\to X\), with the corresponding inverse-image closed set. Then

\[
\Gamma(X,\mathcal F)\longrightarrow\Gamma(Z,\mathcal F|_Z)
\tag{4.1}
\]

is bijective for every étale sheaf of sets \(\mathcal F\).

*Proof.* There is a monomorphism from the Zariski inverse image of the Zariski restriction of \(\mathcal F\) to the Zariski restriction of its étale inverse image. On a germ this follows from openness of an étale neighbourhood: equality after an étale pullback implies equality on its open image by the sheaf condition. Thus (3.3) gives injectivity in (4.1), also after finite covers.

Let \(t\) be a section on \(Z\). Locally it comes from sections \(s_i\) on étale schemes \(U_i\to X\). Shrinking \(U_i\) to the open images of the neighbourhoods realizing these lifts makes the pullback of \(s_i\) on \(U_i\times_X Z\) equal to \(t\). These \(U_i\) cover \(X\). Indeed their images cover \(Z\); if the closed complement in \(X\) were nonempty, (3.3) for its pushed-forward two-element constant sheaf would force it to meet \(Z\).

Choose the finite refinement \(T\to X\) of Lemma 4.2. On a Zariski covering of \(T\), the \(s_i\) provide lifts of \(t|_{Z_T}\). Their germs agree over \(Z_T\), so the section there belongs to the Zariski inverse-image subsheaf. By hypothesis it lifts to a global \(s_T\). Its two pullbacks to \(T\times_XT\) agree because they agree on \(Z\times_X(T\times_XT)\), and the injectivity already proved applies to that finite scheme.

Sections of an étale sheaf descend through a finite surjection. Here is a direct check: by lesson 7, the stalk of \(p_*p^{-1}\mathcal F\) at \(\bar x\) is the product of \(\mathcal F_{\bar x}\) over the finitely many geometric points of \(T_{\bar x}\). The analogous fibre product gives all pairs. Its two maps have equalizer the diagonal copy of \(\mathcal F_{\bar x}\), since the indexing set is nonempty. Enough points therefore identifies \(\mathcal F\) with that equalizer of sheaves. Apply global sections to descend \(s_T\). Its restriction is \(t\), by injectivity on the finite cover. ∎

**Theorem 4.4 (henselian degree zero).** For \(X\) proper over a henselian pair \((A,I)\), restriction to \(Z=X_{A/I}\) is bijective on sections of every étale sheaf of sets. In particular this holds for the closed fibre over a henselian local ring.

*Proof.* Lemma 4.1 and Proposition 3.3 supply precisely the hypotheses of Lemma 4.3. ∎

Taking a two-element constant sheaf shows that clopen subsets of \(X\) and \(Z\) correspond. In the Noetherian case this is the usual bijection of their finite sets of connected components. Finiteness of the component set is not asserted for an arbitrary non-Noetherian base.

**Corollary 4.5 (proper degree-zero base change).** If \(f:X\to Y\) is proper, then (1.2) is an isomorphism for every sheaf of sets.

*Proof.* Lesson 7's strict-local stalk formula for degree zero identifies \((f_*\mathcal F)_{\bar y}\) with sections on \(X_{\mathcal O^{\mathrm{sh}}_{Y,\bar y}}\). Theorem 4.4 replaces this by sections on its closed fibre, whose field is the separable closure \(\kappa(y)^{\mathrm{sep}}\) determined by \(\bar y\). Sections do not change on extending a separably closed field. Here is the relevant descent argument. For \(K/k\) with \(k\) separably closed, the projection \(T_K\to T\) is flat and quasi-compact, and its geometric fibres are connected: \(K\otimes_k\Omega\) has no nontrivial idempotents, the usual geometric-connectedness criterion for a field with no nontrivial separable algebraic constant extension. A section of the pulled sheaf is constant on each such fibre, whose coefficient sheaf has the single value at that geometric base point. Its two pullbacks to \(T_K\times_TT_K\) therefore agree on every geometric stalk. Sections of inverse images of an étale sheaf satisfy fpqc descent: the equality loci of local étale representatives are opens, their agreeing inverse images descend by fpqc descent of opens, and the sheaf condition on the resulting étale covering glues the representatives. Thus the section descends uniquely to \(T\). This proves the asserted invariance for every sheaf of sets. Thus these sections are \(\Gamma(X_{\bar y},\mathcal F_{\bar y})\).

For \(\bar y'\to Y'\) and its composite \(\bar y\to Y\), the two geometric fibres in (1.1) are the same scheme with the same pulled sheaf. The stalk map of (1.2) is restriction along this identification, by its adjunction construction. It is a bijection. ∎

## 5. Embedding constructible coefficients into finite direct images

**Lemma 5.1.** Let \(X\) be quasi-compact and quasi-separated. A constructible abelian sheaf \(C\) admits an embedding

\[
C\lhook\joinrel\longrightarrow\bigoplus_{i=1}^r(p_i)_*\underline{M_i},
\tag{5.1}
\]

where \(p_i:T_i\to X\) is finite of finite presentation and \(M_i\) is a finite abelian group. For a constructible \(\mathbf F_\ell\)-sheaf, the embedding and the \(M_i\) may be taken \(\mathbf F_\ell\)-linear.

*Proof.* First let \(X\) be Noetherian. Refine a constructible stratification into finitely many reduced irreducible locally closed pieces on which \(C\) is finite locally constant. Fix a piece \(S\), its generic point \(x\), and its reduced closure \(Z\). Choose a finite separable extension \(K/\kappa(x)\) trivializing \(C_x\), with value \(M\). The normalization \(T\) of \(Z\) in \(K\) is integral and normal, although it need not be finite. On a normal integral scheme, pushforward of a constant sheaf from its generic point is that constant sheaf: an étale chart is normal, and each connected component is integral, so its locally constant generic sections extend uniquely on that component. Adjunction therefore extends the generic trivialization to a map \(C|_T\to\underline M_T\), and then gives \(C\to p_*\underline M\).

This map is injective at every geometric point of \(S\). Indeed \(T_S\) is normal and its pulled local system has trivial generic monodromy, hence is constant on each connected component by the preceding generic-section argument. The map there is an isomorphism. A geometric point of \(S\) has a lift to the integral surjection \(T_S\to S\); evaluating the adjoint map at that lift proves injectivity at the original stalk.

Write \(T\) as the limit of finite integral schemes \(T_j\to Z\). Lesson 7's relative degree-zero continuity gives

\[
p_*\underline M=\mathop{\mathrm{colim}}_j(p_j)_*\underline M.
\]

The compactness of \(C\), proved in lesson 11, factors its map through one finite stage. The factor is still injective on \(S\), since its composite is injective there. Repeat for the finitely many pieces and take the direct sum of all maps; every geometric stalk is detected by at least one piece. Each resulting finite morphism is of finite presentation because \(X\) is Noetherian. All steps respect the module structure when present.

For general \(X\), descend the constructible sheaf and its finite presentation to an absolute Noetherian approximation \(X_j\). Apply the Noetherian assertion there and pull back the embedding. Inverse image is exact and finite pushforward commutes with every base change by lesson 7. The base-changed finite maps are still of finite presentation. This proves (5.1). ∎

This is an embedding, whereas the finite-cover dévissage of lesson 11 initially supplied generators. Embeddings let an injective target extend a map across (5.1), which is the direction we need below.

## 6. Killing constant-coefficient classes on closed affine schemes

**Lemma 6.1.** If \(R\) is a normal domain with separably closed fraction field \(K\), each separated étale scheme over \(\operatorname{Spec}R\) is a disjoint union of open subschemes of \(\operatorname{Spec}R\). All local rings of \(R\) are strictly henselian.

*Proof.* For an étale \(R\)-algebra \(B\), its generic algebra is a finite product of copies of \(K\). The corresponding idempotents lie in \(B\), because \(B\) is normal and they are integral elements of its total ring of fractions. On each factor \(B\) is a subring of \(K\), by flatness. The same flatness embeds \(B\otimes_RB\) in its generic algebra \(K\), so multiplication \(B\otimes_RB\to B\) is an isomorphism. Thus this factor is an étale monomorphism, hence an open immersion. For a separated étale scheme these local pieces belonging to a given generic point glue to an open immersion: separatedness prevents two points over the same base point from duplicating the generic branch. Pieces belonging to different generic points are disjoint and open and closed. The description of strict henselization as the limit of pointed étale neighbourhoods now shows that the local ring at any point is already strictly henselian. ∎

**Lemma 6.2.** If \(Z\) is closed in \(\operatorname{Spec}R\) as in Lemma 6.1, every finite étale surjection onto \(Z\) has a section. Consequently \(H^1(Z,\underline M)=0\) for a finite abelian group \(M\).

*Proof.* An affine étale algebra over \(R/J\) lifts to one over \(R\). In an étale standard smooth presentation, lift the finitely many equations and invert their Jacobian determinant; reducing the lifted presentation recovers the original algebra. Lemma 6.1 then makes its spectrum a finite disjoint union of opens of \(Z\). If the morphism is finite, these opens are also closed. For a finite étale surjection choose one of these opens on each part of the finite clopen partition determined by all their images. The selected inverse open immersions glue to a section. An \(M\)-torsor is represented by a finite étale surjection, by lesson 11, so is trivial. The torsor description of \(H^1\) proves the conclusion. ∎

**Lemma 6.3 (affine acyclicity criterion).** Suppose all local rings of a ring \(B\) are strictly henselian and an abelian étale sheaf \(F\) satisfies

\[
\ker\bigl(H^1(D(u+v),F)\longrightarrow
H^1(D(u(u+v)),F)\oplus H^1(D(v(u+v)),F)\bigr)=0
\tag{6.1}
\]

for every \(u,v\in B\). Then \(H^q(D(h),F)=0\) for every \(h\in B\) and \(q>0\).

*Proof.* Étale and Zariski cohomology agree here. For the map from the étale site to the Zariski site, a positive higher-direct-image stalk is the filtered cohomology over open neighbourhoods of a point. Continuity identifies this with cohomology of its strictly henselian local scheme, which vanishes by the local section argument of lesson 6. Leray proves the agreement, also on every open.

Induct on \(q\), simultaneously on all principal opens. After replacing \(B\) by \(B_h\), consider \(\xi\in H^q(\operatorname{Spec}B,F)\). Condition (6.1) survives localization: if \(u=a/h^m\) and \(v=b/h^m\), its three opens are the principal opens defined in \(B\) by \(h(a+b)\), \(ha(a+b)\) and \(hb(a+b)\). The defining condition applies to \(u'=ha\), \(v'=hb\), whose opens give exactly these supports.

Let \(J_\xi\) consist of \(b\in B\) for which \(\xi|_{D(b)}=0\). Positive cohomology classes are Zariski locally zero, so these principal opens cover \(\operatorname{Spec}B\). The set contains zero and is stable under multiplication by any element and under negatives. If \(u,v\in J_\xi\), cover \(D(u+v)\) by \(D(u(u+v))\) and \(D(v(u+v))\). For \(q=1\), (6.1) implies vanishing on \(D(u+v)\). For \(q>1\), Mayer–Vietoris gives the same implication because \(H^{q-1}(D(uv(u+v)),F)=0\) by induction. Thus \(J_\xi\) is an ideal. Its principal opens cover the spectrum, so it is the unit ideal. Hence \(\xi=0\). ∎

**Proposition 6.4.** For \(R\) as in Lemma 6.1, every closed \(Z\subset\operatorname{Spec}R\) satisfies

\[
H^q(Z,\underline M)=0\quad(q>0)
\tag{6.2}
\]

for finite abelian \(M\).

*Proof.* Quotients of strictly henselian local rings are strictly henselian. Each principal open of \(Z\) is a closed subscheme of a principal localization of \(\operatorname{Spec}R\). Lemma 6.2 therefore makes its \(H^1\) vanish. Apply Lemma 6.3. ∎

**Proposition 6.5 (finite effacement).** If \(X\) is affine, \(Z\subset X\) closed, \(M\) finite abelian and \(\xi\in H^q(Z,\underline M)\), \(q>0\), some finite surjective morphism \(p:X'\to X\) of finite presentation kills \(\xi\) on \(Z\times_XX'\).

*Proof.* Write \(X=\operatorname{Spec}A\) and \(A=\mathbf Z[x_i]_{i\in I}/J\), allowing any set of generators. Let \(R\) be the integral closure of this polynomial domain in an algebraic closure of its fraction field. It is a normal domain with algebraically closed fraction field. Lying over makes \(\operatorname{Spec}(R/JR)\to X\) integral and surjective. Every closed subscheme of its source has vanishing constant finite cohomology by Proposition 6.4. Thus it kills \(\xi\). Express this integral source as a limit of schemes finite and of finite presentation over \(X\). Cohomological continuity, lesson 7, kills \(\xi\) at one finite stage. Each stage is surjective because the surjective limit morphism factors through it. ∎

**Corollary 6.6 (effacement of arbitrary torsion sheaves).** For affine \(X\), closed \(Z\subset X\), torsion \(F\) and \(\xi\in H^q(Z,F|_Z)\), \(q>0\), there is a monomorphism of torsion sheaves \(F\to F'\) on \(X\) killing \(\xi\).

*Proof.* Constructible approximation and filtered cohomology express \(\xi\) as the image of a class for a constructible \(C\) mapping to \(F\). By Lemma 5.1 embed \(C\) in a finite sum of finite pushforwards of finite constants. Finite pushforward, its base change and its cohomology are exact as in lesson 7. For each summand Proposition 6.5 therefore kills the corresponding class by a finite surjection onto its affine source. Pulling back constants and pushing forward gives a monomorphism of the old summand into the new one: on stalks this repeats each coordinate on a nonempty set of lifts. The new finite sum \(C'\) consequently contains \(C\) and kills its class. Form

\[
F'=(F\oplus C')/\{(u(c),-v(c)):c\in C\}.
\tag{6.3}
\]

The map \(F\to F'\) is injective since \(v:C\to C'\) is injective; its stalks show this directly. It remains torsion, and its restriction to \(Z\) is the corresponding pushout because inverse image is exact. The image of \(\xi\) is zero. ∎

## 7. The affine henselian comparison and restricted injectives

**Theorem 7.1 (affine henselian comparison).** For a henselian pair \((A,I)\), \(X=\operatorname{Spec}A\), \(Z=\operatorname{Spec}(A/I)\) and a torsion sheaf \(F\), restriction induces

\[
H^q(X,F)\xrightarrow{\sim}H^q(Z,F|_Z)\quad(q\geq0).
\tag{7.1}
\]

*Proof.* The degree-zero case is Theorem 4.4, since the identity scheme is proper over \(A\). Suppose comparison is bijective for all torsion coefficients in degrees below \(q>0\). For a monomorphism \(F\to F'\) with torsion cokernel \(Q\), compare the two long exact sequences ending in

\[
H^{q-1}(F')\longrightarrow H^{q-1}(Q)
\xrightarrow{\partial}H^q(F)\longrightarrow H^q(F')
\tag{7.2}
\]

on \(X\) and \(Z\). If \(\xi\in H^q(X,F)\) restricts to zero, use Corollary 6.6 with the closed subset \(X\) itself to choose \(F'\) killing \(\xi\). Lift \(\xi\) to \(\eta\in H^{q-1}(X,Q)\). Its restriction comes from \(H^{q-1}(Z,F'|_Z)\), since its boundary is zero. Lift that class to \(H^{q-1}(X,F')\), subtract its image from \(\eta\), and use injectivity in degree \(q-1\). The difference is zero, so \(\xi=0\).

For a class on \(Z\), use Corollary 6.6 to choose \(F'\) killing it there. It is a boundary of \(H^{q-1}(Z,Q|_Z)\). Surjectivity of comparison in that degree lifts the preimage to \(X\); its boundary lifts the original class. This completes both parts of the induction. ∎

**Lemma 7.2.** Let \(X\) have affine diagonal and a covering by \(n+1\) affine opens. If \(J\) is injective in the category of \(\mathbf F_\ell\)-sheaves on \(X\) and \(Z\subset X\) is closed, then

\[
H^q(Z,J|_Z)=0\quad(q>n).
\tag{7.3}
\]

*Proof.* First let \(X=\operatorname{Spec}A\), \(Z=V(I)\). Its henselization along \(I\) is \(\operatorname{Spec}A^h\), where \(A^h\) is the filtered colimit of étale \(A\)-algebras \(B\) satisfying \(B/IB=A/I\), with the chosen identification. The pair \((A^h,IA^h)\) is henselian and has closed quotient \(A/I\). By (7.1) and continuity,

\[
\begin{aligned}
H^q(Z,J|_Z)&=H^q(\operatorname{Spec}A^h,J|_{A^h})\\
&=\mathop{\mathrm{colim}}_B H^q(\operatorname{Spec}B,J|_B)=0\quad(q>0).
\end{aligned}
\tag{7.4}
\]

The last equality holds because restriction to an étale object preserves injectives: its left adjoint, extension by zero, is exact. Cohomology of \(\mathbf F_\ell\)-modules agrees with underlying abelian-sheaf cohomology, as proved in lesson 12, so module injectives are acyclic for these groups.

For the induction write \(X=U\cup V\), with \(U\) covered by \(n\) affines and \(V\) affine. Affineness of the diagonal makes \(U\cap V\) covered by \(n\) affine intersections. The restrictions of \(J\) to these opens remain injective. The Mayer–Vietoris segment

\[
\begin{gathered}
H^{q-1}(Z\cap U\cap V,J)\longrightarrow H^q(Z,J)\\
\longrightarrow H^q(Z\cap U,J)\oplus H^q(Z\cap V,J)
\end{gathered}
\]

has both outside terms zero for \(q>n\), by the induction and affine case. ∎

Theorem 7.1 is often called Gabber's affine analogue of proper base change. Here its effacement proof is part of the argument, so it is not an invocation of the theorem we are trying to establish.

## 8. Acyclic resolutions on the projective-line fibre

**Lemma 8.1.** If \(A\) is henselian local and \(T\) is proper over \(A\), then for finite abelian \(M\),

\[
H^1(T,\underline M)\xrightarrow{\sim}H^1(T_0,\underline M).
\tag{8.1}
\]

*Proof.* These sets classify \(M\)-torsors. A torsor is a finite étale cover with an \(M\)-action for which \(M\times T'\to T'\times_TT'\) is an isomorphism. The finite étale equivalence of section 2 lifts the cover and all action maps. Full faithfulness lifts the action identities; it also lifts the inverse of the displayed isomorphism. Hence it is an equivalence on torsors and their isomorphisms. The induced bijection preserves the abelian group law, by compatibility with products and contracted products. ∎

**Proposition 8.2.** Let \(X=\mathbf P^1_A\) for henselian local \(A\), with closed fibre \(X_0\). For an injective \(\mathbf F_\ell\)-sheaf \(J\) on \(X\),

\[
H^q(X_0,J|_{X_0})=0\quad(q>0).
\tag{8.2}
\]

*Proof.* The projective line is separated and has its usual two affine charts, so Lemma 7.2 proves (8.2) for \(q>1\). Let \(\xi\in H^1(X_0,J|_{X_0})\). Write \(J\) as a filtered colimit of constructible \(\mathbf F_\ell\)-sheaves mapping to it, by lesson 11. The fibre is quasi-compact and quasi-separated, so filtered cohomology supplies a constructible \(C\to J\) and a class \(\zeta\in H^1(X_0,C|_{X_0})\) mapping to \(\xi\).

Embed \(C\) in \(C'=\bigoplus_i(p_i)_*\underline M_i\) by Lemma 5.1. Injectivity of \(J\) extends the map \(C\to J\) to \(C'\to J\). Each \(T_i\) is finite over \(X\), hence proper over \(A\). Finite-map cohomology identifies the summand of the image of \(\zeta\) with a class in \(H^1((T_i)_0,\underline M_i)\). By Lemma 8.1 this lifts to \(H^1(T_i,\underline M_i)\), hence to \(H^1(X,(p_i)_*\underline M_i)\). Sum the lifts. Their image in \(H^1(X,J)\) is zero by injectivity. Restricting that zero class to \(X_0\) gives precisely \(\xi\), by functoriality. Thus \(\xi=0\). ∎

**Theorem 8.3 (projective-line closed-fibre comparison).** With \(A\) henselian local, \(X=\mathbf P^1_A\) and any \(\mathbf F_\ell\)-sheaf \(F\), restriction gives a canonical isomorphism

\[
H^q(X,F)\xrightarrow{\sim}H^q(X_0,F|_{X_0})\quad(q\geq0).
\tag{8.3}
\]

*Proof.* Choose an injective resolution \(F\to J^\bullet\) in \(\mathbf F_\ell\)-sheaves. Restriction is exact, so \(J^\bullet|_{X_0}\) resolves \(F|_{X_0}\). Proposition 8.2 makes every term acyclic for fibre cohomology, so it computes the right-hand side of (8.3). The left-hand side is computed by \(\Gamma(X,J^\bullet)\). Theorem 4.4 identifies this complex, term by term and respecting differentials, with \(\Gamma(X_0,J^\bullet|_{X_0})\). Their cohomology comparison is exactly restriction. ∎

Strict henselianity will be used to turn this closed-fibre comparison into geometric stalks. The coefficient prime \(\ell\) was arbitrary throughout, including the residue characteristic.

## 9. An injective criterion and the formal reductions

For a proper morphism \(f\), call the conclusion of Theorem 1.1 for all torsion sheaves and all base changes the **base change property**.

**Proposition 9.1 (injective criterion).** A proper \(f:X\to Y\) has the base change property if and only if for every prime \(\ell\), every injective \(\mathbf F_\ell\)-sheaf \(J\) on \(X\), and every square (1.1),

\[
R^qf'_*a^{-1}J=0\quad(q>0).
\tag{9.1}
\]

*Proof.* The forward implication holds because \(R^qf_*J=0\); module injectives are also acyclic for the underlying cohomology. Conversely suppose (9.1). For a sheaf killed by \(\ell\), choose a resolution by such injectives. Its inverse image is an exact resolution of \(a^{-1}F\); (9.1) says it is \(f'_*\)-acyclic. Corollary 4.5 gives a termwise identification

\[
g^{-1}f_*J^\bullet=f'_*a^{-1}J^\bullet.
\]

The two complexes compute the two derived objects, and their identification induces the canonical comparison. This proves the property for sheaves killed by a prime.

If \(n=\ell m\) kills \(F\), the exact sequence

\[
0\longrightarrow F[\ell]\longrightarrow F
\longrightarrow F/F[\ell]\longrightarrow0
\tag{9.2}
\]

has last term killed by \(m\): \(m s\) is killed by \(\ell\). The map of long exact direct-image sequences and induction on \(n\) prove base change for \(F\). For general torsion \(F\), take the filtered colimit of \(F[n]\), ordered by divisibility of positive integers. Inverse images commute with colimits, and higher direct images of a quasi-compact, quasi-separated morphism commute with filtered colimits by lesson 7. Proper morphisms and their base changes have these finiteness properties. Passing to the colimit proves the assertion. ∎

**Lemma 9.2 (finite and local cases).** Finite morphisms have the base change property, even with arbitrary abelian coefficients. The property for proper morphisms is local on the base in the étale topology, and in particular in the Zariski topology.

*Proof.* For a finite morphism, lesson 7 gives exact direct image and arbitrary degree-zero base change; the higher direct images on both sides are zero. For localization, restriction to an étale object on the base computes the higher direct image using the corresponding base-changed scheme. On the source and target of (1.4), restriction therefore gives the comparison for that localized morphism. An isomorphism is detected on an étale covering. ∎

**Lemma 9.3 (composition).** If proper \(u:X\to Y\) and \(v:Y\to Z\) have the property, so does \(vu\).

*Proof.* Use Proposition 9.1. For an injective \(\mathbf F_\ell\)-sheaf \(J\) on \(X\), \(u_*J\) is injective because its left adjoint \(u^{-1}\) is exact. After an arbitrary base change of \(Z\), write the resulting maps as \(u',v'\) and the projections from \(X',Y'\) as \(a,b\). We have

\[
b^{-1}u_*J=u'_*a^{-1}J,
\quad R^qu'_*a^{-1}J=0\ (q>0).
\]

The property for \(v\) applied to \(u_*J\) also gives \(R^pv'_*b^{-1}u_*J=0\) for \(p>0\). In the relative Leray spectral sequence

\[
R^pv'_*R^qu'_*a^{-1}J\ \Longrightarrow\ R^{p+q}(v'u')_*a^{-1}J
\tag{9.3}
\]

only \((p,q)=(0,0)\) survives. All positive direct images of the composite vanish, as required. ∎

**Lemma 9.4 (sandwich).** Suppose \(u:X\to Y\) is proper surjective, \(v:Y\to Z\) is proper, and the property holds for \(u\) and \(vu\). Then it holds for \(v\).

*Proof.* For an injective \(\mathbf F_\ell\)-sheaf \(I\) on \(Y\), embed \(u^{-1}I\) in an injective \(J\) on \(X\). The adjoint map \(I\to u_*J\) is injective. Its inverse image followed by the counit is the chosen embedding, and \(u^{-1}\) detects monomorphisms because every geometric point of \(Y\) lifts through the surjective \(u\). Injectivity of \(I\) splits this map; \(I\) is a direct summand of \(u_*J\).

After an arbitrary base change of \(Z\), both \(R^qu'_*a^{-1}J\), \(q>0\), and \(R^r(v'u')_*a^{-1}J\), \(r>0\), vanish by the hypotheses and criterion. The spectral sequence (9.3) collapses to its row \(q=0\). Corollary 4.5 identifies that row with \(R^pv'_*b^{-1}u_*J\), so it vanishes for \(p>0\). It also vanishes for the direct summand \(b^{-1}I\). Proposition 9.1 proves the property for \(v\). ∎

Surjectivity in Lemma 9.4 is what detects the sheaf downstairs. A proper map missing part of \(Y\) cannot supply that step.

## 10. From the projective line to every proper morphism

**Lemma 10.1.** For every \(n\geq1\) and scheme \(S\) there is a finite surjection

\[
\rho:(\mathbf P^1_S)^n\longrightarrow\mathbf P^n_S.
\tag{10.1}
\]

*Proof.* Interpret \(\mathbf P^n\) as coefficients of homogeneous binary forms of degree \(n\). Send the \(n\) linear forms \(x_iT+y_iU\) to their product

\[
\prod_{i=1}^n(x_iT+y_iU)=\sum_{r=0}^n c_rT^{n-r}U^r.
\tag{10.2}
\]

The coefficients are sections of the same line bundle \(\mathcal O(1,\ldots,1)\). They have no simultaneous zero at a geometric point, because a product of nonzero linear forms over a field is nonzero. Thus they generate the line bundle everywhere and define (10.1) over \(\mathbf Z\), hence over every \(S\).

Over an algebraically closed field, every nonzero binary form factors into linear forms. Its factor lines, with multiplicities, determine all points of the fibre: there are at most \(n!\) possible orderings. Thus \(\rho\) is surjective on geometric points and has zero-dimensional geometric fibres. It is proper, since its source is proper over \(S\) and its target is separated over \(S\). It is of finite type, hence quasi-finite by those finite fibres, and proper quasi-finite implies finite. Surjectivity on geometric points gives surjectivity of schemes. This proof does not require division by \(n!\) and works in every characteristic. ∎

**Proposition 10.2 (projective-line reduction).** If \(\mathbf P^1_S\to S\) has the property for every scheme \(S\), every proper morphism has it.

*Proof.* The projections in the iterated product \((\mathbf P^1_S)^n\to S\) have the property; Lemma 9.3 proves it for their composite. The finite map \(\rho\) has the property. Lemma 9.4 then proves the property for \(\mathbf P^n_S\to S\). For \(n=0\) the projection is the identity and the assertion is immediate.

Now let \(f:X\to Y\) be proper. By Lemma 9.2 assume \(Y\) affine. Chow's lemma supplies a proper surjection \(\pi:T\to X\) and an immersion \(h:T\to\mathbf P^n_Y\). The map \(T\to Y\) is proper, so \(h\) is proper and hence a closed immersion. The map

\[
(\pi,h):T\longrightarrow X\times_Y\mathbf P^n_Y=\mathbf P^n_X
\tag{10.3}
\]

is also a closed immersion. Indeed the graph \(T\to X\times_YT\) of \(\pi\) is closed since \(X\to Y\) is separated, and \(X\times_YT\to X\times_Y\mathbf P^n_Y\) is the base change of the closed immersion \(h\).

Both \(\pi\) and \(T\to Y\) are therefore a finite closed immersion followed by a projective-space projection. Lemmas 9.2 and 9.3 give the property for both. Since \(\pi\) is surjective, the sandwich lemma gives it for \(f\). Localization finishes the proof. ∎

## 11. The theorem, its derived extension and the fibre formula

**Proposition 11.1.** The projection \(f:\mathbf P^1_S\to S\) has the base change property for every scheme \(S\).

*Proof.* First take an arbitrary \(\mathbf F_\ell\)-sheaf \(F\). For a geometric point \(\bar s\) over \(s\), set \(A=\mathcal O^{\mathrm{sh}}_{S,\bar s}\) and \(k_s=\kappa(s)^{\mathrm{sep}}\), its residue field. Strict-local continuity in lesson 7 and Theorem 8.3 give canonical restriction maps identifying

\[
\begin{aligned}
(R^qf_*F)_{\bar s}
&=H^q(\mathbf P^1_A,F|_{\mathbf P^1_A})\\
&\xrightarrow{\sim}H^q(\mathbf P^1_{k_s},F|_{\mathbf P^1_{k_s}}).
\end{aligned}
\tag{11.1}
\]

For \(g:T\to S\) and \(\bar t\to T\), its composite is \(\bar s\to S\). Compatible strict localizations induce a field inclusion \(k_s\to k_t=\kappa(t)^{\mathrm{sep}}\). With (11.1), the stalk of (1.4) is exactly the pullback

\[
H^q(\mathbf P^1_{k_s},F|_{k_s})\longrightarrow
H^q(\mathbf P^1_{k_t},F|_{k_t}).
\tag{11.2}
\]

Both fields are separably closed. The proper, dimension-one field-extension theorem proved in lesson 12 says that this canonical map is an isomorphism for torsion sheaves. Thus (1.4) is an isomorphism for every \(\mathbf F_\ell\)-sheaf. In particular it gives the vanishing (9.1) for injective \(J\). Proposition 9.1 supplies the property for every torsion sheaf. ∎

**Proof of Theorem 1.1 for sheaves.** Apply Proposition 10.2 to Proposition 11.1. The resulting isomorphisms are the maps (1.4): every reduction used their adjunction maps, their compatible Leray maps and their long exact sequences. In the derived category (1.3) is an isomorphism because it is one on every cohomology sheaf. ∎

**Proposition 11.2 (bounded below complexes).** For proper \(f\), arbitrary \(g\) and \(E\in D^+(X_{\mathrm{ét}})\) with torsion cohomology sheaves, (1.3) is an isomorphism.

*Proof.* Choose \(N\) with \(\mathcal H^r(E)=0\) for \(r<N\). Compare the hypercohomology spectral sequences, after applying exact \(g^{-1}\) to the first,

\[
\begin{aligned}
g^{-1}R^pf_*\mathcal H^r(E)&\ \Longrightarrow\ g^{-1}\mathcal H^{p+r}(Rf_*E),\\
R^pf'_*a^{-1}\mathcal H^r(E)&\ \Longrightarrow\ \mathcal H^{p+r}(Rf'_*a^{-1}E).
\end{aligned}
\tag{11.3}
\]

The sheaf theorem identifies their \(E_2\)-terms via the canonical comparison. In a fixed total degree \(m\), only \(p\geq0\), \(r\geq N\), \(p+r=m\) occur; there are finitely many such pairs. The convergent spectral sequences therefore give finite filtrations of the two degree-\(m\) objects with isomorphic associated graded objects. Exactness and induction on the filtration length give an isomorphism in that degree. All degrees are covered, proving the claim. The bounded-below hypothesis is what makes this convergence argument finite in each degree. ∎

**Corollary 11.3 (geometric fibres).** Formula (1.5) holds. For the complexes of Proposition 11.2 it reads

\[
(\mathcal H^q(Rf_*E))_{\bar y}
\cong H^q(X_{\bar y},E|_{X_{\bar y}}).
\tag{11.4}
\]

*Proof.* Apply base change with \(Y'=\operatorname{Spec}\Omega\), where \(\Omega\) is the separably closed field of \(\bar y\). Pullback to that point is the stalk functor. The étale topos of a separably closed field is the category of sets, and its abelian global-section functor is exact. Hence the derived direct image to that point has cohomology the displayed fibre groups. ∎

**Corollary 11.4 (a strictly henselian neighbourhood).** If \(S\) is strictly henselian local with closed point \(s\) and \(f:X\to S\) is proper, then for torsion \(F\),

\[
H^q(X,F)\xrightarrow{\sim}H^q(X_s,F|_{X_s}).
\tag{11.5}
\]

*Proof.* On a strictly henselian local scheme, sections of any étale sheaf are its stalk at a geometric closed point. Every pointed étale neighbourhood has a section, and every open containing the closed point is the whole local scheme; these two observations prove both injectivity and surjectivity of the germ map. This section functor is exact, so its positive cohomology vanishes. Leray for \(f\) consequently identifies \(H^q(X,F)\) with \(\Gamma(S,R^qf_*F)=(R^qf_*F)_{\bar s}\). Corollary 11.3 identifies that stalk with the right-hand side of (11.5). All identifications are restriction maps. ∎

For a proper map with fibres of dimension at most one, (1.5) and lesson 12 already imply \(R^qf_*F=0\) for \(q>2\). Higher-dimensional bounds require the additional dimension arguments of lesson 16; they are not assumptions in the present proof.

## 12. Three examples and the necessity of the hypotheses

**Example 12.1 (a puncture with an empty fibre).** Let \(k\) be algebraically closed, \(n\geq2\) invertible in \(k\), and \(j:\mathbf G_{m,k}\to\mathbf A^1_k\) the open immersion. Base-change to the geometric point \(0\). The fibre of \(j\) is empty, so every direct image from the base-changed source is zero.

Let \(A=\mathcal O^{\mathrm{sh}}_{\mathbf A^1,0}\) and \(K=\operatorname{Frac}A\). The strict-local stalk formula, which requires no properness, gives

\[
(R^1j_*\mathbf Z/n)_0=H^1(\operatorname{Spec}K,\mathbf Z/n).
\tag{12.1}
\]

Fix a primitive root \(\zeta\in\mu_n(k)\) to identify \(\mathbf Z/n\) with \(\mu_n\). Kummer and Hilbert 90 give \(H^1(K,\mu_n)=K^*/K^{*n}\). The ring \(A\) is a strictly henselian DVR with uniformizer \(t\). Every unit has an \(n\)-th root: first choose the root in its separably closed residue field, then apply Hensel's lemma to \(T^n-u\), whose derivative at that root is invertible. The valuation therefore identifies

\[
K^*/K^{*n}\cong\mathbf Z/n,
\tag{12.2}
\]

generated by \(t\). Thus degree-one base change is the nonisomorphism \(\mathbf Z/n\to0\). It already fails in degree zero, whose source stalk is \(\mathbf Z/n\) and whose target is zero. Properness removes this phenomenon: a missing fibre cannot be approached through points of a proper source lying over arbitrarily small étale neighbourhoods.

**Lemma 12.2 (normal schemes and rational first cohomology).** For a normal integral locally Noetherian scheme \(T\),

\[
H^1(T,\underline{\mathbf Q})=0.
\tag{12.3}
\]

*Proof.* For the generic-point inclusion \(i:\eta\to T\), we have \(i_*\underline{\mathbf Q}=\underline{\mathbf Q}_T\). On a connected normal étale chart there is one generic point and constant generic sections extend uniquely; a general chart is covered by such components. The low-degree Leray sequence injects \(H^1(T,i_*\mathbf Q)\) into \(H^1(\eta,\mathbf Q)\). By lesson 8, the latter consists of continuous homomorphisms from the profinite absolute Galois group to the discrete additive group \(\mathbf Q\), with trivial action. The image is finite by compactness, and \(\mathbf Q\) has no nonzero finite subgroup. Hence it is zero. ∎

**Example 12.3 (properness does not suffice for rational coefficients).** Let \(k\) be algebraically closed of characteristic zero, \(A=k[[t]]\), and \(S=\operatorname{Spec}A\). In \(\mathbf P^2_A\) define

\[
X:\quad y^2z=x^3+x^2z+t z^3.
\tag{12.4}
\]

The projection \(f:X\to S\) is projective and proper. Its generic fibre is a smooth cubic: on \(z=1\) a singularity would have \(y=0\), \(3x^2+2x=0\), forcing \(t=0\) or \(t=-4/27\), neither possible in \(k((t))\). The point at infinity \((0:1:0)\) is smooth because the derivative with respect to \(z\) is nonzero there. A smooth plane cubic is geometrically integral, since distinct positive-degree projective plane components would meet.

The total scheme is regular and integral. It is flat over \(A\): on each polynomial chart the equation is not divisible by \(t\), so reducing a relation \(th=Fg\) modulo \(t\) forces \(g\) to be divisible by \(t\); hence \(t\) is a non-zero-divisor in the quotient. At every smooth point of a fibre regularity follows from the smooth local presentation over the regular base. The only remaining point is the closed-fibre node \((0:0:1)\), where the completed local ring is

\[
k[[t,x,y]]/(y^2-x^3-x^2-t)\cong k[[x,y]].
\tag{12.5}
\]

This is regular. The total scheme is therefore reduced, and flatness makes every irreducible component dominate \(S\): in a reduced Noetherian scheme a component contained in \(t=0\) would make \(t\) a zero divisor. Since the generic fibre is integral, there is only one component. Thus \(X\) is normal integral and Lemma 12.2 gives \(H^1(X,\mathbf Q)=0\).

The closed fibre \(C\) is the irreducible rational nodal cubic \(y^2z=x^3+x^2z\). Its normalization \(\nu:\mathbf P^1_k\to C\) is parametrized on \(z=1\) by

\[
x=u^2-1,\qquad y=u(u^2-1).
\tag{12.6}
\]

In homogeneous parameters \((U:V)\), the map is \(((U^2-V^2)V:U(U^2-V^2):V^3)\); these coordinates never vanish simultaneously. The morphism is proper, has finite fibres and is birational, since \(u=y/x\) away from the node. Hence it is finite and is the normalization, with normal source \(\mathbf P^1\). The tangent cone at the node is \(y^2-x^2\), so its two branches are distinct.

The node \(c\) has two preimages, \(u=1\) and \(u=-1\); elsewhere the normalization is an isomorphism. Finite-map stalks give the exact sequence

\[
0\longrightarrow\mathbf Q_C\longrightarrow\nu_*\mathbf Q_{\mathbf P^1}
\xrightarrow{\delta}(i_c)_*\mathbf Q\longrightarrow0,
\tag{12.7}
\]

where \(\delta\) is the difference of the two branch values. On global sections \(\delta:\mathbf Q\to\mathbf Q\) is zero, since a constant has equal branch values. Also \(H^1(\mathbf P^1,\mathbf Q)=0\) by Lemma 12.2. The long exact sequence consequently gives

\[
H^1(C,\mathbf Q)\cong\mathbf Q.
\tag{12.8}
\]

The ring \(A\) is strictly henselian. The general strict-local stalk formula of lesson 7, valid for arbitrary abelian sheaves, identifies \((R^1f_*\mathbf Q)_s\) with \(H^1(X,\mathbf Q)=0\). Base change to its closed point therefore gives the map \(0\to\mathbf Q\) in degree one. This explicitly disproves the torsion-free variant of Theorem 1.1.

The same nodal mechanism appears in SGA 4, Exposé XII, section 2, with \(\mathbf Z\)-coefficients. The rational coefficient choice makes the Galois calculation particularly transparent. It also keeps the coefficient identification exact: inverse image of a constant \(\mathbf Q\)-sheaf is the constant \(\mathbf Q\)-sheaf on the fibre. An inverse image of \(\mathbf G_m\) under an arbitrary morphism cannot instead be replaced silently by the fibre's native sheaf of units.

**Example 12.4 (curve fibres).** For a proper \(f:X\to Y\) with curve fibres and an invertible prime \(\ell\),

\[
(R^1f_*\mathbf F_\ell)_{\bar y}=H^1(X_{\bar y},\mathbf F_\ell).
\tag{12.9}
\]

A smooth geometrically connected projective fibre of genus \(g\) has \(2g\)-dimensional first cohomology by lesson 10. An irreducible rational nodal cubic has one-dimensional first cohomology by lesson 12's normalization calculation. In (12.4) these dimensions are respectively two at a geometric generic point and one at the closed point. Thus proper base change computes the stalks but does not assert that the higher direct-image sheaf is locally constant. Smooth base change and local acyclicity, treated later, supply the additional hypotheses for such assertions.

## 13. Exercises

1. **Easy.** Deduce the geometric fibre formula, for torsion sheaves and bounded below complexes with torsion cohomology, directly from the theorem.
2. **Medium.** For \(j:\mathbf G_m\to\mathbf A^1\) over an algebraically closed field and invertible \(n\geq2\), calculate the degree-one comparison after base change to zero. Identify a generator, and also check degree zero.
3. **Medium.** Suppose \(f:X\to Y\) is proper with nonempty geometrically connected fibres. Prove that the unit map \(\mathbf Z/n_Y\to f_*\mathbf Z/n_X\) is an isomorphism.
4. **Medium.** Let \(X\) be proper over a strictly henselian local scheme \(S\). Derive the closed-fibre comparison in every degree for arbitrary torsion coefficients from proper base change and Leray.
5. **Hard.** Prove the henselian degree-zero theorem for arbitrary étale sheaves of sets, using Stein factorization. Identify the roles of closed subsets, finite covers and the spectral topology; do not restrict the argument to constant sheaves or a Noetherian base.

## 14. Worked solutions

**Solution 1.** Base-change along \(\bar y:\operatorname{Spec}\Omega\to Y\), with \(\Omega\) separably closed. Exact inverse image to this point is the geometric stalk functor. The theorem identifies the derived stalk of \(Rf_*F\) with \(Rf_{\bar y,*}(F|_{X_{\bar y}})\). On the étale topos of \(\Omega\), global sections are exact and the topos is just sets. Its degree-\(q\) value is \(H^q(X_{\bar y},F|_{X_{\bar y}})\), giving (1.5). For a bounded below complex use Proposition 11.2 in the same square. Exactness of the stalk functor commutes with its cohomology sheaves, giving (11.4). These identifications use the canonical base change morphism, so are functorial in coefficients.

**Solution 2.** The base-changed source \(\mathbf G_m\times_{\mathbf A^1}\{0\}\) is empty, so the target of every comparison is zero. Put \(A=\mathcal O^{\mathrm{sh}}_{\mathbf A^1,0}\), \(K=\operatorname{Frac}A\). The source of degree-one comparison is the strict-local stalk \(H^1(K,\mathbf Z/n)\). Choose a primitive root \(\zeta\) and identify the coefficients with \(\mu_n\). The Kummer sequence and \(H^1(K,\mathbf G_m)=0\) identify it with \(K^*/K^{*n}\).

Every element is \(t^r u\) with \(u\in A^*\). Since \(n\) is invertible and the residue field separably closed, Hensel lifts an \(n\)-th root of \(u\). The valuation is therefore an isomorphism from the quotient to \(\mathbf Z/n\). The torsor \(v^n=t\) represents its generator; it is not trivial because its valuation would require \(n\mid1\). Hence the comparison is \(\mathbf Z/n\to0\). In degree zero the source is \(H^0(K,\mathbf Z/n)=\mathbf Z/n\), since a field is connected, while the target is again zero. Both maps fail to be isomorphisms.

**Solution 3.** For a geometric point \(\bar y\), degree-zero proper base change identifies the stalk of \(f_*\mathbf Z/n\) with sections of the constant sheaf on \(X_{\bar y}\). Such sections are locally constant functions to \(\mathbf Z/n\). On a nonempty connected scheme they are exactly constants. The unit's stalk sends an element to that same constant function, so is a bijection. Enough geometric points makes the unit an isomorphism of sheaves. Nonemptiness is necessary: sections on an empty fibre form the zero group, whereas the constant stalk on the base is \(\mathbf Z/n\).

**Solution 4.** Every pointed étale neighbourhood of the closed point of \(S\) has a section through it. An open containing the closed point is all of \(S\). It follows that the germ map identifies \(\Gamma(S,G)\) with \(G_{\bar s}\) for every sheaf \(G\): a germ pulls back along the section to a global representative, and equality of germs pulls back to equality globally. Stalks are exact, so this global-section functor is exact. In the Leray spectral sequence \(H^p(S,R^qf_*F)\Rightarrow H^{p+q}(X,F)\), all terms with \(p>0\) vanish. Consequently

\[
\begin{aligned}
H^q(X,F)&=\Gamma(S,R^qf_*F)\\
&=(R^qf_*F)_{\bar s}=H^q(X_s,F|_{X_s}),
\end{aligned}
\]

where the final equality is Solution 1. The edge maps and base change map compose to restriction. No constructibility or fixed annihilator of \(F\) is required.

**Solution 5.** Let \(A\) be henselian local with maximal ideal \(\mathfrak m\), and \(Z=X_0\). For each point \(x\in X\), its reduced closure \(C\) is integral and proper over \(A\). Stein factorization gives a closed surjection with connected fibres from \(C\) to the spectrum of the integral domain \(B=\Gamma(C,\mathcal O_C)\), integral over \(A\). The henselian pair \((B,\mathfrak mB)\) has no nontrivial idempotents in its quotient and that quotient is nonzero. Its spectrum is connected. The closed-fibre base change of the Stein morphism is still closed and surjective with connected fibres, so \(C\cap Z\) is nonempty and connected. The identical argument works for every scheme finite over \(X\), because it is again proper over \(A\).

The underlying spaces are spectral. A clopen partition of their closed fibres lifts by assigning each point the unique part met by its closure; constructible compactness and specialization stability make the resulting parts closed and hence clopen. This proves equality of sections for finite constant Zariski sheaves on every closed subspace. Every Zariski sheaf is a filtered colimit of finite presentations on quasi-compact opens. Each finite presentation has a finite sober model and embeds in a finite product of closed pushforwards of finite constant sheaves, as in Lemma 3.2. Extend its fibre section in that product; membership in the subsheaf propagates from a specialization in \(Z\). Filtered sections on these quasi-compact spaces then give the assertion for every Zariski sheaf, on \(X\) and on each finite cover.

For an étale sheaf \(F\), first observe injectivity of the restriction map: equality in a pulled étale germ implies equality on the open image of its neighbourhood, and the just-proved Zariski assertion detects equality globally. A fibre section locally lifts to sections on étale \(U_i\to X\). Their images cover \(X\), since a nonempty closed complement would meet \(Z\). Lemma 4.2 replaces this étale covering by a finite surjection \(T\to X\) factoring through it on Zariski opens. The fibre section now comes from the Zariski inverse-image subsheaf on \(T\), and the Zariski result extends it to a section on \(T\). Its two pullbacks to \(T\times_XT\) agree on the closed fibre, hence everywhere by injectivity on that finite scheme. Finite-surjection descent for sections, verified by the diagonal equalizer on geometric stalks in Lemma 4.3, descends it to \(X\). Injectivity already proved gives uniqueness. This proves the required bijection for arbitrary étale sheaves of sets.

## 15. Sources and the proof's scope

The proof includes the spectral degree-zero argument, the finite-constant embeddings, affine effacement, the two-chart injective calculation, the projective-line case, the composition and sandwich criteria and the finite surjection onto projective space. In particular, the positive-degree calculation on the projective-line fibre is not inferred merely from exact inverse image or the dimension of that fibre. The bounded below derived extension uses a convergent finite-diagonal spectral sequence.

- **[Stacks, proper base change]** [Tags 095S, 0A0B–0A0C, 0A3S–0A3U, 0A4B–0A4F, 095T and 0DDE–0DDF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-proper-base-change) give the degree-zero, injective and geometric reductions. Sections 3–4 and 9–11 write out the maps and diagram chases.
- **[Stacks, first cohomology]** [Tags 0A5F–0A5H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-finite-etale-over-proper) supply the finite-torsor and fibre-effacement route of section 8, with the precise finite étale geometric foundation [0A48](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian).
- **[Stacks, affine comparison]** [The affine henselian comparison section](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-gabber-affine-proper) and [strictly henselian local rings](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-strictly-henselian-local-rings) contain the finite-cover effacement and restricted-injective arguments. These additional proof dependencies are fully developed in sections 5–7.
- **[Stacks, preliminary comparisons]** [Tags 0EZQ and 0F01](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-base-change-preliminaries) describe comparison maps and their localization. [Tags 0F07](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-base-change-does-not-hold-pre) and [0F08](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-base-change-does-not-hold) give finite-data witnesses for failure of base change, rather than non-torsion examples; Example 12.3 gives a counterexample with rational coefficients directly.
- **[SGA 4]** M. Artin, [SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XII, especially section 2 and the reductions in section 6, and Exposé XIII, sections 1–3, give the original nodal example and the completion of the proper theorem.
- **[SGA 4½]** P. Deligne, *[Cohomologie étale](https://publications.ias.edu/sites/default/files/Number32.pdf)*, the Arcata account, section IV, subsections 1–4, gives a complementary route through finite étale covers, constructible embeddings and lifting the Picard group of a curve. Our proof uses the affine effacement route for the higher-degree injective step.

The external geometric inputs are those precisely stated in section 2, the elementary algebraic lifting of étale presentations in Lemma 6.2, and the henselization along an ideal in Lemma 7.2. The proper base change theorem, its henselian degree-zero lemma and its reductions are proved here. Continuity, constructibility, finite-map exactness, torsors and proper curve field-invariance are proved in earlier lessons. No general finiteness theorem for proper direct images, smooth base change, duality or unbounded derived base change is assumed.
