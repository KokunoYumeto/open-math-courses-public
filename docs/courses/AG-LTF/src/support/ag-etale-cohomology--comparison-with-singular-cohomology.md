# Comparison with singular cohomology

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Original text released under CC0.

An étale neighbourhood of a complex point becomes a local analytic chart. This observation gives a map on cohomology, but it does not prove that the map is an isomorphism. We prove the compact-support comparison by reducing proper maps to projective curves, where coverings and line bundles determine the answer. We then prove ordinary comparison for constructible coefficients. Keeping these arguments separate also reveals a simple degree-zero counterexample when constructibility is removed.

## 1. Scope and the inputs that remain inputs

Schemes are of finite type over \(\mathbf C\). A morphism \(f:X\to S\) under consideration is separated and of finite type. The notation \(X^{\mathrm{an}}\) means the associated complex analytic space with its classical topology. An arbitrary torsion sheaf means an étale sheaf of abelian groups whose geometric stalks are torsion; it need not have a common annihilator. A constructible torsion sheaf has finite stalks on a finite stratification, and therefore has a common annihilator. We first work with \(\Lambda=\mathbf Z/n\), \(n\geq2\), and then pass to arbitrary torsion.

For constant coefficients on a locally contractible analytic space, classical sheaf cohomology is singular cohomology. For a local system, it is singular cohomology with local coefficients. For a general constructible sheaf, the right side of the comparison is classical *sheaf* cohomology; one must retain its specialization maps. Ordinary singular cochains with a single coefficient group do not describe such a sheaf.

The lesson uses two inputs, stated without proof:

- **Riemann existence, stated:** analytification gives an equivalence between finite étale covers of any finite-type complex scheme and finite topological covering spaces of its analytic space. No normality assumption is required. We use full faithfulness as well as existence; this includes group actions on covers.
- **Projective-curve GAGA, stated:** for a projective complex curve, analytification identifies algebraic and holomorphic line bundles, their morphisms and tensor products. In particular, it identifies their Picard groups.

These are the interfaces of the planned prerequisite lessons qc-09, “Algebraic and analytic coherent sheaves,” and df-08, “Comparison with the topological fundamental group.” We state the interfaces here instead of claiming those prerequisite lessons have been written. Their verified modern locators are listed in Section 17.

The scheme-theoretic prerequisites are finite normalization over \(\mathbf C\), the projectivity of a proper normal complex curve, and the invariance of the étale topos under nilpotent thickening. These are the same geometric foundations used in Lessons 6 and 12. Lesson 11 supplies constructible presentations, their Serre property, and filtered-cohomology continuity on a Noetherian étale site. Lessons 13–14 supply proper base change, compactification and \(Rf_!\), including their natural maps. General proper constructibility retains the stated-input status recorded in Lesson 14. Lessons 17–18 supply normalized curve and smooth duality; their exact current versions are prerequisites.

For the ordinary comparison argument in Section 11 we also use **resolution of singularities as an external geometric prerequisite**: a reduced finite-type complex scheme has a proper map from a smooth scheme which is an isomorphism over a dense open. Temkin, Theorem 1.2.1, gives a sequence of blow-ups with regular final scheme and centers outside the regular locus; finite-type complex schemes satisfy its Noetherian, quasi-excellent, characteristic-zero hypotheses. This geometric theorem is not a cohomological comparison premise and is not proved in this course. The proper-support proof, Sections 5–9, does not use it. Classical manifold Poincaré duality, triangulation, the universal coefficient theorem, and the Dolbeault resolution on a Riemann surface are topological and analytic prerequisites. Section 10 explains the exact duality form and orientation needed here.

## 2. From analytic charts to a morphism of topoi

If \(u:U\to X\) is étale, the analytic inverse function theorem makes \(u^{\mathrm{an}}\) a local biholomorphism, hence a local homeomorphism. Surjective étale families give jointly surjective analytic families. Analytification preserves finite fibre products. The site of local homeomorphisms over a space presents its usual sheaf topos: an open subset is a local homeomorphism, and every local homeomorphism is covered by such opens.

Consequently the assignment \(U\mapsto U^{\mathrm{an}}\) induces a geometric morphism

\[
\epsilon_X:\operatorname{Sh}(X^{\mathrm{an}})
\longrightarrow\operatorname{Sh}(X_{\mathrm{\acute et}}),
\qquad F^{\mathrm{an}}=\epsilon_X^*F.
\tag{2.1}
\]

One can see its inverse image concretely: form local analytic sections from étale sections and sheafify. At a complex point \(x\), the associated fibre functor is the geometric étale point \(\bar x:\operatorname{Spec}\mathbf C\to X\). Thus

\[
(F^{\mathrm{an}})_x=F_{\bar x}.
\tag{2.2}
\]

**Lemma 2.1.** Analytification of abelian sheaves is exact, preserves colimits and tensor products, and sends finite locally constant sheaves to finite local systems. For an open immersion \(j\) and a closed immersion \(i\),

\[
(j_!F)^{\mathrm{an}}=j^{\mathrm{an}}_!F^{\mathrm{an}},
\qquad
(i_*G)^{\mathrm{an}}=i^{\mathrm{an}}_*G^{\mathrm{an}}.
\tag{2.3}
\]

*Proof.* Inverse image of a geometric morphism preserves finite limits and all colimits. For abelian sheaves this proves exactness. Tensor products are constructed from sums and relations, so they are preserved; exactness also gives the derived tensor compatibility. A finite local system is trivialized by a finite étale cover, which analytifies to a covering. For (2.3), at a point of the open the stalk is the original stalk and outside it the stalk is zero. The closed case has the same stalk test. Formula (2.2) proves the assertions, including the canonical maps. \(\square\)

For finite-type complex schemes, closed complex points give all analytic points. To prove a morphism of analytic sheaves is an isomorphism, their stalks suffice. We will therefore apply algebraic proper base change only at these geometric points; no comparison over a non-complex residue field is being assumed.

## 3. Constructing the comparison maps

The square of topoi associated with \(f\) commutes. For a bounded-below complex \(E\), the counit \(f^*Rf_*E\to E\), pulled back to the analytic space and transposed by adjunction, defines

\[
\alpha_f:\epsilon_S^*Rf_*E
\longrightarrow Rf^{\mathrm{an}}_*\epsilon_X^*E.
\tag{3.1}
\]

More explicitly, the map being transposed is

\[
(f^{\mathrm{an}})^*\epsilon_S^*Rf_*E
\simeq\epsilon_X^*f^*Rf_*E
\longrightarrow\epsilon_X^*E.
\]

For the structure map to a point this gives the canonical ordinary map \(R\Gamma(X,E)\to R\Gamma(X^{\mathrm{an}},E^{\mathrm{an}})\). It is a map, without a prior assertion that it is an isomorphism.

Choose a relative compactification \(X\xrightarrow{j}\overline X\xrightarrow{p}S\), with \(j\) open and \(p\) proper, as in Lesson 14. Using (2.3) and (3.1) defines

\[
\beta_f:\epsilon_S^*Rf_!E
=\epsilon_S^*Rp_*j_!E
\longrightarrow Rp^{\mathrm{an}}_*j^{\mathrm{an}}_!E^{\mathrm{an}}
=Rf^{\mathrm{an}}_!E^{\mathrm{an}}.
\tag{3.2}
\]

Algebraic proper maps analytify to proper continuous maps. The associated analytic compactification therefore defines the usual derived direct image with proper support. A common proper refinement of two compactifications identifies their \(j_!\) objects by the fibre calculation proved in Section 7. Naturality of the counits in (3.1) then identifies their maps (3.2). Thus \(\beta_f\) is independent of compactification.

**Lemma 3.1 (compatibilities).** The comparison maps are natural in coefficients, respect distinguished triangles, and commute with composition, base-change maps, and the ordinary action on compactly supported cohomology. In particular they respect cup products.

*Proof.* The maps arise from inverse image, units and counits. Transposing two counits in sequence gives the counit of their composite, by the two adjunction identities. Transposing around a base-change square gives its usual base-change map by the same identities. Exact inverse image preserves the localization sequences (2.3), so the constructions also commute with their boundary maps. Finally inverse image preserves the evaluation \(E\otimes^LG\to H\); the projection maps for pushforward are obtained by transposing that evaluation. Pulling back either construction gives the same evaluation on the analytic side. Applying ordinary or proper-support sections proves cup compatibility, including mixed ordinary/compact products. The derived symmetry is the usual Koszul symmetry on both sides, so the sign for exchanging degrees \(a,b\) is \((-1)^{ab}\). \(\square\)

This supplies comparison maps between Leray and hypercohomology spectral sequences. Their finite filtrations, rather than just numerical dimensions, will be used below.

## 4. The classical proper-support tools

Here are the classical facts corresponding to the algebraic theorems already proved in the course.

**Lemma 4.1 (compact continuity).** On a compact Hausdorff space \(K\), sheaf cohomology commutes with filtered colimits of abelian sheaves.

*Proof.* First global sections commute. A section of the colimit has local representatives. Choose a finite cover by compact neighbourhoods contained in the representative opens, with interiors covering \(K\). On each compact intersection, equality of two representatives is locally witnessed at later stages, and finitely many such witnesses suffice. A common stage makes the representatives equal on all intersections; they glue on the interiors. The same finite-cover argument makes a section which becomes zero vanish at a single later stage. This proves both surjectivity and injectivity of the degree-zero colimit map. It applies to every closed subset of \(K\), which is also compact Hausdorff.

Use functorial injective resolutions of the system. Injective sheaves are flasque and hence soft on a compact Hausdorff space. A filtered colimit of these terms is soft: sections on each closed subset and global sections commute with the colimit, and the extension map was surjective at every stage. Soft sheaves on a paracompact Hausdorff space are acyclic for global sections, by the usual finite shrinking-and-extension proof of Čech acyclicity. The colimit resolution is exact on stalks and consists of these acyclic terms. Global sections of the resolution commute with the colimit, and filtered colimits of groups are exact. Its cohomology gives the assertion in every degree. \(\square\)

**Lemma 4.2 (classical proper base change).** If \(p:T\to B\) is proper between locally compact Hausdorff spaces, then

\[
(Rp_*G)_b\simeq R\Gamma(T_b,G|_{T_b}).
\tag{4.1}
\]

It follows that proper pushforward satisfies arbitrary base change.

*Proof.* The stalk on the left is cohomology over the inverse images of shrinking neighbourhoods of \(b\). These are cofinal among neighbourhoods of the compact fibre: if \(W\supset T_b\), then \(B\setminus p(T\setminus W)\) is an open neighbourhood whose inverse image lies in \(W\), since \(p\) is closed. Restriction to a compact Hausdorff closed subset computes the colimit of cohomology over its neighbourhoods. To verify the latter assertion, lift a finite Čech representative on the subset to neighbourhoods, shrink a finite cover so that its overlap equations hold, and do the same for a coboundary. Čech and derived cohomology agree on a compact Hausdorff space and the restrictions of injective sheaves are acyclic by this same refinement argument. This proves (4.1). After base change the two fibres are homeomorphic and carry the same sheaf; the stalk map is their identity, proving base change. \(\square\)

The full neighbourhood-refinement proof is in the pinned cohomology chapter cited in Section 17; Anschütz, Lemma 4.20 and Theorem 4.16, provide an additional open account. These statements apply to arbitrary abelian sheaves, without constructibility. From (4.1) and Lemma 4.1, \(R^qp_*\) commutes with filtered colimits for a proper analytic map. Applying this to \(p_*j_!\) gives the same assertion for proper-support pushforward in our compactifiable setting.

## 5. The comparison on a smooth projective curve

Let \(C\) be a connected smooth projective complex curve. Choose \(\zeta_n=\exp(2\pi i/n)\), identifying \(\Lambda(1)=\mu_n\) with the constant analytic \(\Lambda\). We keep twists when no choice is intended.

**Theorem 5.1.** The canonical maps

\[
H^q(C,\Lambda)\longrightarrow
H^q(C^{\mathrm{an}},\Lambda)
\tag{5.1}
\]

are isomorphisms in all degrees.

*Proof in degree zero.* Sections of a finite constant set are sections of its trivial finite cover. Full faithfulness in Riemann existence identifies those sections on the two sides and their group operations. In particular a connected algebraic \(C\) has connected analytic space: a nontrivial analytic open-and-closed decomposition would give a nonconstant section of the trivial two-sheeted cover. Hence both groups in degree zero are \(\Lambda\), and (5.1) is the identity on constants.

*Proof in degree one.* \(H^1(-,\Lambda)\) classifies \(\Lambda\)-torsors. The algebraic torsors are finite étale covers with a specified simply transitive fibre action. Riemann existence identifies the covers, their actions, and equivariant isomorphisms. The action conditions can be checked on fibres and are preserved. Analytification of a torsor represents precisely the cohomological map (5.1), since the Čech transition cocycle pulls back to the same cocycle. This proves an additive isomorphism, without assuming that higher cohomology is group cohomology of the fundamental group.

*Proof in degree two.* Kummer is exact both étale locally and analytically locally; a nonvanishing holomorphic function has a local holomorphic \(n\)-th root. Naturality gives a diagram of Kummer sequences. On the algebraic curve, Lesson 10 gives \(H^2(C,\mathbf G_m)=0\), so

\[
H^2(C,\mu_n)=\operatorname{Pic}(C)/n.
\tag{5.2}
\]

On the Riemann surface, the exponential sequence

\[
0\longrightarrow\mathbf Z\longrightarrow\mathcal O_C
\xrightarrow{\exp(2\pi i\,\cdot)}\mathcal O_C^*
\longrightarrow1
\tag{5.3}
\]

has \(H^2(C^{\mathrm{an}},\mathcal O_C)=0\), by the Dolbeault resolution of complex length one, and \(H^3(C^{\mathrm{an}},\mathbf Z)=0\), since a compact surface has a two-dimensional CW structure. Its long exact sequence gives \(H^2(C^{\mathrm{an}},\mathcal O_C^*)=0\). Analytic Kummer therefore gives \(H^2(C^{\mathrm{an}},\mu_n)=\operatorname{Pic}(C^{\mathrm{an}})/n\). Curve GAGA identifies the two Picard groups. The map (5.1), transferred along \(\zeta_n\), is consequently an isomorphism in degree two. The algebraic groups vanish above two by Lesson 12; the analytic constant groups do by the surface CW calculation. This proves every degree. \(\square\)

The generator is also identified. \(\mathcal O_C(x)\) has degree one; its Kummer class maps to its analytic first Chern class modulo \(n\). Sequence (5.3) computes that class by the winding of a transition function. A positively oriented small circle around the zero of a local parameter has winding \(+1\). Thus the curve trace of Lesson 17 is integration over the complex orientation, with the same \(+1\) normalization.

## 6. Finite-cover resolutions of constructible sheaves

We need more than constant coefficients on a curve. The following embedding works in every dimension and will be used twice.

**Lemma 6.1.** For a reduced finite-type complex scheme \(X\) and a constructible \(\Lambda\)-sheaf \(F\), there is a monomorphism

\[
F\longrightarrow I=\bigoplus_{a=1}^m (\pi_a)_*\Lambda_{T_a}^{\,r_a},
\tag{6.1}
\]

where each \(\pi_a:T_a\to X\) is finite, \(T_a\) is normal, and \(\dim T_a\leq\dim X\). The cokernel is constructible. If \(X\) is proper of dimension at most one, the \(T_a\) are disjoint unions of smooth projective curves and points.

*Proof.* Choose a dense open \(U\) which is a disjoint union of normal opens of the irreducible components and on which \(F\) is finite locally constant. Write \(j:U\to X\) and \(i:Z=X\setminus U\to X\). The map

\[
F\longrightarrow j_*F|_U\oplus i_*i^*F
\tag{6.2}
\]

is injective: on \(U\) its first component is the identity, and at a point of \(Z\) its second component is the identity.

A finite local system on a connected normal \(U\) is trivialized by a finite étale cover \(r:V\to U\). Its finite fibre module \(M\) embeds in \(\Lambda^r\). To see this even for composite \(n\), decompose \(M\) into cyclic groups \(\mathbf Z/d\), \(d\mid n\), and embed \(1\) as \(n/d\) in a separate copy of \(\Lambda\). Equivalently, \(\Lambda\) is a finite injective cogenerator, as proved in Lesson 17. The unit \(F|_U\to r_*r^*F|_U\), followed by this embedding on the trivialized fibres, is injective and lands in \(r_*\Lambda_V^r\).

Normalize each component of \(X\) in the finitely many function fields of \(V\). Excellence makes the resulting map \(\pi:T\to X\) finite, and its restriction over \(U\) is \(V\). On a normal scheme \(T\), with dense open \(j':V\to T\),

\[
j'_*\Lambda_V=\Lambda_T.
\tag{6.3}
\]

Indeed a strict local normal connected scheme is integral; its intersection with the dense open is nonempty and irreducible, hence connected. Sections of the constant sheaf there are exactly \(\Lambda\). These are the geometric stalks of (6.3). Applying left exact \(j_*\) to the embedding on \(U\) now embeds \(j_*F|_U\) in \(\pi_*\Lambda_T^r\).

For the boundary term in (6.2), use the same construction by induction on \(\dim Z<\dim X\), beginning with finite sets of points. Composing its finite maps with the closed immersion \(i\) gives the remaining terms of (6.1). All terms and the cokernel are constructible by the constructible Serre property and finite pushforward. A proper normal complex curve is smooth and projective; zero-dimensional normal schemes are finite sets of complex points. This proves the final assertion. \(\square\)

Iterating (6.1) on its cokernel produces an exact right resolution \(0\to F\to I^0\to I^1\to\cdots\). It need not terminate. Both analytification and finite pushforward are exact; finite pushforward commutes with analytification by proper base change with zero-dimensional fibres. The hypercohomology spectral sequence is

\[
E_1^{a,b}=H^b(X,I^a)\Longrightarrow H^{a+b}(X,F).
\tag{6.4}
\]

It is first quadrant: each fixed total degree involves only finitely many pairs \((a,b)\). Thus if comparison is an isomorphism on every \(I^a\), it is an isomorphism on \(F\); there is no claim that an infinite resolution is an acyclic resolution. The same conclusion follows by truncating it beyond the fixed degree and noting the remaining cokernel shifts past that degree.

For a proper curve, Theorem 5.1, finite pushforward and (6.4) prove comparison for every constructible \(F\). Points contribute only degree zero. This includes singular and reducible curves.

## 7. Proper comparison by lowering the dimension

**Lemma 7.1 (proper modification over an open).** Suppose \(h:Y\to X\) is proper and is an isomorphism over \(U\subset X\). For \(j:U\to X\), \(j':h^{-1}U\to Y\), and any torsion \(G\) on \(U\), the unit gives

\[
j_!G\simeq Rh_*j'_!G.
\tag{7.1}
\]

The same statement holds analytically, and comparison commutes with these identifications.

*Proof.* At a geometric point of \(U\), the proper fibre is a single point and the map is the identity on its coefficient. At a point outside \(U\), the restriction of \(j'_!G\) to the entire fibre is zero. Algebraic proper base change therefore makes (7.1) an isomorphism on every stalk. Classical proper base change gives the same conclusion analytically. Both maps are units, so their comparison squares commute by Section 3. \(\square\)

**Theorem 7.2.** Proper comparison (3.1) is an isomorphism for every proper finite-type complex map and every constructible torsion sheaf.

*Proof.* Induct on a bound \(d\) for the dimensions of the proper fibres. For \(d=0\) the map is finite, and its stalk is a finite direct sum over points; this proves the assertion, including the vanishing of higher images. For \(d=1\), proper base change on both sides reduces the assertion at each analytic point of the base to a proper complex curve or a finite set of points. Section 6 proves that case.

Assume \(d\geq2\) and the result for smaller relative dimensions. Again proper base change reduces us to a proper scheme \(X/\mathbf C\) of dimension at most \(d\). Reduce \(X\) without changing its étale topos or underlying analytic topology. Zero-dimensional components separated from the others can be handled separately; on the remaining positive-dimensional components choose a rational function nonconstant on each component. On a dense open \(U\), where the components are disjoint, it defines \(\varphi:U\to\mathbf A^1\). Let \(Y\) be the reduced closure of its graph in \(X\times\mathbf P^1\). There are proper maps

\[
Y\xrightarrow{a}\mathbf P^1\xrightarrow{b}\operatorname{Spec}\mathbf C,
\qquad h:Y\to X,
\qquad h^{-1}U\simeq U.
\tag{7.2}
\]

Every irreducible component of \(Y\) dominates \(\mathbf P^1\), since the function was nonconstant. Its fibres are proper closed subsets of that component, so have dimension at most \(d-1\). The fibres of \(b\) have dimension one, also less than \(d\).

Put \(G=F|_U\) and \(E=j'_!G\). The induction hypothesis compares \(Ra_*E\) with \(Ra^{\mathrm{an}}_*E^{\mathrm{an}}\). Its cohomology sheaves are constructible by proper constructibility and vanish above the uniform fibre bound. The already known comparison for \(b\), applied to these sheaves and then their finite truncations, compares the two Leray spectral sequences. Their finite filtrations in each total degree give

\[
R\Gamma(Y,E)\simeq
R\Gamma(Y^{\mathrm{an}},E^{\mathrm{an}}).
\tag{7.3}
\]

Lemma 7.1 transfers (7.3) to \(R\Gamma(X,j_!G)\). For the closed complement \(Z=X\setminus U\), every component has dimension at most \(d-1\). The induction hypothesis compares \(R\Gamma(Z,i^*F)\). The exact localization sequence

\[
0\longrightarrow j_!G\longrightarrow F
\longrightarrow i_*i^*F\longrightarrow0
\tag{7.4}
\]

and its analytic counterpart now compare \(R\Gamma(X,F)\). Finally return to the original proper map: at each analytic point the comparison stalk is this comparison on its complex fibre. Stalks detect the desired isomorphism. This completes the induction. \(\square\)

Notice the two dimensions in this argument. It lowers *proper fibre dimension* through \(a\), and lowers *support dimension* on the boundary \(Z\). Merely choosing a curve inside \(X\) would accomplish neither reduction.

## 8. Arbitrary torsion in the proper theorem

**Theorem 8.1.** For proper \(p:X\to S\) and an arbitrary torsion sheaf \(F\),

\[
\epsilon_S^*Rp_*F\simeq Rp^{\mathrm{an}}_*F^{\mathrm{an}}.
\tag{8.1}
\]

*Proof.* On the Noetherian étale site of \(X\), \(F\) is a filtered colimit of constructible finite torsion sheaves, using their finite presentations as in Lesson 11. One may first write \(F=\varinjlim_nF[n]\), with divisibility indexing the annihilators, then use the finite presentations for each \(\mathbf Z/n\)-sheaf. The coherent-site continuity theorem makes \(R^qp_*\) commute with these filtered colimits. Inverse image and analytification commute with colimits. On the analytic side classical proper base change computes each stalk on the compact proper fibre, and Lemma 4.1 proves its continuity. Hence (8.1) is the filtered colimit in each degree of the isomorphisms in Theorem 7.2. Since the comparison maps themselves are natural in \(F\), the resulting isomorphism is the original map (3.1). \(\square\)

This passage does not replace an arbitrary torsion sheaf by one finite local system or assume a common integer kills it. Properness supplies the compactness on the analytic side that makes the passage legitimate.

## 9. Artin comparison with proper support

**Theorem 9.1.** For separated finite-type \(f:X\to S\), arbitrary torsion \(F\), and every \(q\geq0\), the canonical map is an isomorphism:

\[
(R^qf_!F)^{\mathrm{an}}
\xrightarrow{\ \sim\ }
R^qf^{\mathrm{an}}_!F^{\mathrm{an}}.
\tag{9.1}
\]

In particular, for a separated finite-type complex scheme,

\[
H^q_c(X,F)\simeq H^q_c(X^{\mathrm{an}},F^{\mathrm{an}}).
\tag{9.2}
\]

*Proof.* Use the compactification in (3.2). Theorem 8.1 applies to the arbitrary torsion sheaf \(j_!F\) on \(\overline X\), and Lemma 2.1 identifies its analytification with \(j^{\mathrm{an}}_!F^{\mathrm{an}}\). This is exactly (3.2), hence is an isomorphism. Taking cohomology sheaves proves (9.1); taking the base to be a point proves (9.2). If \(S\) is not separated, work over its affine open charts. The inverse image \(X_V\) over such a chart is separated over \(\mathbf C\), so the analytic proper-support argument applies there. The canonical maps agree on overlaps by naturality, and their isomorphisms glue. \(\square\)

For bounded constructible complexes the same theorem follows by finite truncations. Composition and all base-change diagrams retain the compatibilities of Section 3. The proof has used precisely the projective-curve comparison, finite-cover coefficient resolutions, proper fibre calculations, the graph reduction and continuity. It has not used an ordinary comparison theorem or a resolution of higher-dimensional singularities.

## 10. Cup products, point orientations and smooth ordinary comparison

The cup-product compatibility was proved in Lemma 3.1 before any isomorphism assertion. We now check the trace, which is an orientation assertion rather than a formal consequence of equal group sizes.

**Lemma 10.1 (orientation).** On a smooth complex scheme of pure dimension \(d\), comparison sends the compact cycle class of a complex point to its positively oriented topological point class. Consequently it identifies the smooth compact trace with integration over the complex orientation.

*Proof.* First consider a smooth divisor with local equation \(t\). The algebraic Thom class is the boundary of the Kummer class of \(t\), by the divisor normalization in Lesson 18, Lemma 12.2. Analytically, continuation of a chosen \(n\)-th root of \(t\) around a positively oriented transverse circle multiplies it by \(\zeta_n\). Its Kummer class is therefore the positive generator of that circle's \(H^1(-,\Lambda)\). The connecting map for the oriented disk and punctured disk sends this generator to the positive Thom class in \(H^2_{\{0\}}(-,\Lambda(1))\). Naturality of localization and Kummer makes the two boundary constructions commute with comparison.

Near a smooth point choose étale coordinates \(t_1,\ldots,t_d\). Analytically these are local biholomorphic coordinates, preserving the complex orientation. The point Gysin class is the iterated Gysin class, or product of the coordinate-divisor Thom classes, by Gysin transitivity in Lesson 18. The preceding one-coordinate computation compares each factor. Products of their real two-dimensional positive orientations give the complex \(2d\)-orientation; the shifts are even and contribute no exchange sign. Excision identifies this local class with the global point class, both with ordinary support and after mapping to compact support.

On a connected smooth \(X\), Lesson 18 identifies \(H^{2d}_c(X,\Lambda(d))\) with \(\Lambda\), sending the point class to \(1\). Classical manifold duality identifies \(H^{2d}_c(X^{\mathrm{an}},\Lambda)\) with \(\Lambda\), also sending the point class to \(1\). Compact comparison, already proved, therefore identifies the two trace homomorphisms. For disconnected schemes take the sum over their finitely many connected components. For a relative smooth \(f\), the same argument on each complex fibre, together with proper-support base change, identifies the relative maps \(R^{2d}f_!\Lambda(d)\to\Lambda_S\) on every analytic stalk. This proves relative trace compatibility as well. \(\square\)

**Theorem 10.2 (smooth constant ordinary comparison).** If \(X\) is smooth, separated and finite type over \(\mathbf C\), then

\[
H^r(X,\Lambda)\xrightarrow{\sim}
H^r(X^{\mathrm{an}},\Lambda)
\tag{10.1}
\]

for every \(r\).

*Proof.* Work on each pure-dimensional component, of dimension \(d\). Étale duality in Lesson 18 identifies \(H^r(X,\Lambda)\) with the \(\Lambda\)-dual of \(H^{2d-r}_c(X,\Lambda(d))\), by the compact-first trace pairing. The analogous classical statement holds on the oriented manifold \(X^{\mathrm{an}}\). Its cap-product form is \(H^{2d-r}_c(X^{\mathrm{an}},\Lambda)\simeq H_r(X^{\mathrm{an}},\Lambda)\). The singular chain complex is free over \(\Lambda\), and \(\operatorname{Hom}_\Lambda(-,\Lambda)\) is exact because \(\Lambda\) is self-injective. Thus ordinary cohomology is the dual of that homology, and cup evaluation gives precisely the stated classical pairing. The groups are finite: compact comparison identifies compact groups with the finite algebraic ones, and these dualities make the ordinary groups finite too.

The compact comparison for \(\Lambda(d)\) is an isomorphism. Lemma 3.1 and Lemma 10.1 give a commutative pairing square: evaluating an ordinary class against a compact class, then tracing, agrees on both sides. Hence the ordinary map (10.1) is the dual of the inverse compact map. It is an isomorphism. This proves the assertion without using ordinary comparison to justify the trace or either pairing. \(\square\)

Classical duality here is a topological prerequisite, not an étale comparison theorem in disguise. Hatcher's Theorem 3.35 gives its noncompact cap-product form with any coefficient ring. The exact \(\Lambda\)-dual argument just given is essential for composite \(n\); replacing it with vector-space duality would lose that generality.

## 11. Ordinary comparison for all constructible coefficients

**Theorem 11.1.** For separated finite-type complex \(X\), constructible torsion \(F\), and every \(q\),

\[
H^q(X,F)\xrightarrow{\sim}
H^q(X^{\mathrm{an}},F^{\mathrm{an}}).
\tag{11.1}
\]

The same holds for bounded constructible complexes.

*Proof.* We induct on \(d=\dim X\), allowing all finite annihilators at each stage. Dimension zero is a finite set of points after reduction, so is immediate. Nilpotents can be removed without changing either cohomology theory.

First prove the assertion for \(\Lambda_X\) on every reduced \(X\) of dimension at most \(d\). By the resolution prerequisite in Section 1 there is a proper \(p:Y\to X\), with \(Y\) smooth, which is an isomorphism over a dense open \(U\) meeting every component. Put

\[
C=\operatorname{Cone}(\Lambda_X\longrightarrow Rp_*\Lambda_Y).
\tag{11.2}
\]

Proper constructibility and the finite fibre cohomological bound make \(C\) a bounded constructible complex. Its restriction to \(U\) is zero, since the displayed map is the identity there. Thus it is supported on \(Z=X\setminus U\), of dimension less than \(d\). If \(i:Z\to X\), the unit \(C\to i_*i^*C\) is an isomorphism on stalks; hence the induction hypothesis, extended by finite truncations, compares its ordinary cohomology.

Proper comparison identifies \(C^{\mathrm{an}}\) with the cone of \(\Lambda_{X^{\mathrm{an}}}\to Rp^{\mathrm{an}}_*\Lambda_{Y^{\mathrm{an}}}\). Smooth ordinary comparison, Theorem 10.2, compares \(R\Gamma(Y,\Lambda)\); the derived identity \(R\Gamma(X,Rp_*\Lambda)=R\Gamma(Y,\Lambda)\) and its analytic version are natural. The map between the two triangles defined by (11.2) now has isomorphisms on the second and third terms. The long exact sequences prove that it is an isomorphism on \(R\Gamma(X,\Lambda)\) as well. This proves constant comparison in dimension \(d\), for every \(n\), without requiring \(X\) to be proper or smooth.

Now take an arbitrary constructible \(\Lambda\)-sheaf \(F\) on such an \(X\). Lemma 6.1 provides its right resolution by finite pushforwards of constant sheaves on normal finite-type schemes \(T_a\) of dimension at most \(d\). Constant comparison on each \(T_a\) has just been proved. Finite pushforward is exact and compares with its analytic counterpart, so the ordinary cohomology of every term \(I^a\) compares. The first-quadrant spectral sequences (6.4) prove (11.1). This also proves the induction claim for the next dimension. Every constructible torsion sheaf has some annihilator \(n\), so nothing is lost by the coefficient notation. Bounded constructible complexes follow by their finite cohomology-sheaf truncation triangles. \(\square\)

This identifies the substantive extra work for ordinary comparison: smooth duality, point orientation, and a proper resolution whose error cone lives on a smaller-dimensional closed set. Proper base change alone does not compute stalks of \(Rj_*\) for a nonproper open immersion.

## 12. Why ordinary comparison needs constructibility

Let \(X=\mathbf A^1_{\mathbf C}\), let \(i_m:\{m\}\to X\) for \(m\in\mathbf Z\), and set

\[
F=\bigoplus_{m\in\mathbf Z}(i_m)_*\Lambda.
\tag{12.1}
\]

This is a torsion sheaf annihilated by \(n\), but is not constructible. The sum is the filtered colimit of finite sums. On the quasi-compact Noetherian étale site, global sections commute with that filtered colimit, by Lesson 11. Consequently

\[
H^0(X,F)=\bigoplus_{m\in\mathbf Z}\Lambda.
\tag{12.2}
\]

Analytification preserves the sum. In the complex plane the integers form a closed discrete subset, and every compact set meets only finitely many of them. Any family \((a_m)_{m\in\mathbf Z}\) is locally a section of a finite sum of the skyscrapers: near any point choose a neighbourhood meeting only finitely many integers. These sections agree on overlaps and glue. Conversely a section is determined by these stalk values. Thus

\[
H^0(\mathbf C,F^{\mathrm{an}})=\prod_{m\in\mathbf Z}\Lambda.
\tag{12.3}
\]

The canonical ordinary comparison is the inclusion of the direct sum in the product, and is not surjective. A family with value \(1\) at every integer exhibits the failure. Compactly supported sections on either side have finite support, so both \(H^0_c\) groups are the direct sum and their comparison is an isomorphism, as Theorem 9.1 requires.

The analytic direct sum of skyscraper sheaves has product global sections here because infinite families are locally finite. Confusing a sheaf direct sum with its presheaf of finite-support global sections would erase the example.

## 13. Projective spaces, an elliptic curve and the punctured line

**Example 13.1 (projective space).** The analytic space of \(\mathbf P^N_{\mathbf C}\) is \(\mathbf{CP}^N\). Its standard filtration has one cell in each dimension \(0,2,\ldots,2N\) and no odd-dimensional cells; cellular differentials therefore vanish. On the algebraic side Lesson 18, Section 14, computes the same groups and their hyperplane generators. With \(h=c_1^{(n)}(\mathcal O(1))\), comparison identifies

\[
\bigoplus_i H^{2i}(\mathbf P^N,\Lambda(i))
\simeq\Lambda[h]/(h^{N+1}),\qquad \deg h=2,
\tag{13.1}
\]

with the corresponding singular cohomology ring. The algebraic hyperplane Gysin class is its Kummer Chern class; its analytic class is the usual positive hyperplane Chern class. Cup compatibility sends \(h^i\) to the cellular generator normalized by evaluation on \(\mathbf{CP}^i\). In particular \(\operatorname{Tr}(h^N)=1\). If twists are suppressed using \(\zeta_n\), each even group is \(\Lambda\); without that choice the untwisted algebraic group is canonically \(\Lambda(-i)\).

**Example 13.2 (elliptic curve).** For an elliptic curve \(E\), its analytic space is a compact oriented surface. Lesson 17 gives étale degree-one rank two, and Theorem 5.1 compares that group; the surface formula therefore makes its topological genus one. A CW structure has one vertex, two one-cells \(a,b\), and one two-cell attached by the commutator. Both cellular differentials are zero. Therefore

\[
H^0(E,\Lambda)=\Lambda,\qquad
H^1(E,\Lambda)=\Lambda^2,\qquad
H^2(E,\Lambda)=\Lambda(-1).
\tag{13.2}
\]

Choose the positively oriented basis with intersection \(a\cdot b=1\). Its dual classes \(\alpha,\beta\) satisfy \(\operatorname{Tr}(\alpha\cup\beta)=1\), \(\operatorname{Tr}(\beta\cup\alpha)=-1\), and \(\alpha^2=\beta^2=0\). The last assertion holds even when \(2\mid n\): these classes are reductions of integral degree-one classes with square zero, rather than a deduction from skew symmetry alone. Comparison transports this pairing to étale cohomology. Riemann existence also identifies \(\pi_1^{\mathrm{\acute et}}(E)\) with the profinite completion of the surface group \(\mathbf Z^2\). This calculation is compatible with the Jacobian description in Lesson 17; it does not require another proof of its separately stated Weil-pairing comparison.

**Example 13.3 (\(\mathbf C^*\)).** The analytic punctured line deformation retracts onto the unit circle, with positive counterclockwise generator \(\gamma\) of \(\pi_1^{\mathrm{top}}=\mathbf Z\). Riemann existence and the pointed fibre functors give

\[
\pi_1^{\mathrm{\acute et}}(\mathbf G_m,1)
\simeq\widehat{\mathbf Z}.
\tag{13.3}
\]

Indeed finite covers of the circle correspond to finite sets with a permutation, equivalently finite continuous \(\widehat{\mathbf Z}\)-sets; equivalence of their fibre functors identifies the automorphism groups. The connected cover \(z\mapsto z^r\) corresponds to the subgroup \(r\mathbf Z\), whose closures form a cofinal family of open subgroups. The Kummer class of \(t\) in \(H^1(\mathbf G_m,\mu_n)\) sends \(\gamma\) to \(\zeta_n\), since continuation of \(t^{1/n}\) once around the circle multiplies it by that root. Thus the comparison fixes both the generator and its orientation. The nonzero ordinary constant groups are \(H^0=\Lambda\), \(H^1=\Lambda(-1)\); the compact groups are \(H^1_c=\Lambda\), \(H^2_c=\Lambda(-1)\), in accordance with curve duality. These two different degree-one orientations should not be silently conflated.

## 14. Betti numbers and the coefficient limit

Let \(X\) be smooth projective over \(\mathbf C\), and \(\ell\) a prime. Write

\[
b_q(X^{\mathrm{an}})=\dim_{\mathbf Q}H^q(X^{\mathrm{an}},\mathbf Q).
\]

Its compact analytic space has a finite CW model. Let \(C^\bullet\) be its bounded finite free integral cellular cochain complex. For every \(m\), comparison naturally identifies the algebraic \(\mathbf Z/\ell^m\)-cohomology with \(H^q(C^\bullet\otimes\mathbf Z/\ell^m)\); these identifications commute with reduction of coefficients.

Define the integral étale coefficient-limit complex as \(R\varprojlim_m R\Gamma(X,\mathbf Z/\ell^m)\). Each finite-coefficient cohomology group is finite, so its tower is Mittag–Leffler: for a fixed target the descending images stabilize. Its \(\varprojlim^1\) vanishes, and the Milnor sequence identifies the limit cohomology with the inverse limit of the cohomology groups. On the cellular side the degreewise reduction maps are surjective, so derived inverse limit is the ordinary complex \(C^\bullet\otimes\mathbf Z_\ell\). Consequently

\[
H^q_{\mathrm{\acute et}}(X,\mathbf Z_\ell)
\simeq H^q(C^\bullet\otimes\mathbf Z_\ell).
\tag{14.1}
\]

Tensoring with the flat localization \(\mathbf Q_\ell\) gives

\[
H^q_{\mathrm{\acute et}}(X,\mathbf Q_\ell)
\simeq H^q(X^{\mathrm{an}},\mathbf Q)\otimes_{\mathbf Q}\mathbf Q_\ell,
\qquad
\dim_{\mathbf Q_\ell}H^q_{\mathrm{\acute et}}(X,\mathbf Q_\ell)=b_q.
\tag{14.2}
\]

The finite complex justifies each passage; this is not an application of the torsion theorem directly to the nontorsion sheaf \(\mathbf Q_\ell\). Nor does (14.2) say that \(\dim_{\mathbf F_\ell}H^q(X,\mathbf F_\ell)=b_q\) always. The integral universal coefficient sequence has contributions from \(\ell\)-torsion in integral cohomology in degrees \(q\) and \(q+1\). The rational Betti number is the rank, with those contributions removed.

## 15. Exercises

1. **Easy.** Compute both cohomologies of \(\mathbf P^1_{\mathbf C}\) with \(\Lambda\)-coefficients, and identify the canonical comparison in every degree, including the sign of its top generator.
2. **Medium.** Prove equality of étale and topological Betti numbers for a smooth projective complex variety. Explain why finite-coefficient dimensions need not equal rational Betti numbers.
3. **Medium.** Prove that ordinary and compact comparison preserve cup products and that the relative smooth trace corresponds to integration over the complex-oriented fibres. Specify the coefficient twists and the sign when two classes are exchanged.
4. **Hard.** Starting with the permitted Riemann existence and projective-curve Picard GAGA inputs, carry out the reduction of the arbitrary-torsion proper-support comparison to smooth projective curves. Identify every dimension induction, coefficient resolution and limit argument. Then give the extra argument for ordinary constructible comparison and identify its additional geometric prerequisite.

## 16. Complete solutions

**Solution 1.** Algebraically, Kummer, \(\operatorname{Pic}(\mathbf P^1)=\mathbf Z\), and the curve computation give \(H^0=\Lambda\), \(H^1=0\), \(H^2=\Lambda(-1)\), with all higher groups zero. Analytically \(\mathbf{CP}^1\simeq S^2\) has a vertex and an oriented two-cell, so the same groups are obtained after choosing \(\zeta_n\). The degree-zero comparison is the identity on constants. Degree one and all degrees above two compare zero groups. In degree two, naturality of Kummer and curve GAGA send \(c_1^{(n)}(\mathcal O(1))\) to its analytic Chern class modulo \(n\). A section of \(\mathcal O(1)\) has one simple zero; its transition function winds positively once, so that class evaluates to \(+1\) on the complex-oriented sphere. Both traces are therefore \(+1\). Without the chosen root this is a comparison of the canonically twisted groups, not a choice-free identification of \(\mu_n\) with \(\mathbf Z/n\).

**Solution 2.** Choose a finite free integral cellular cochain complex \(C^\bullet\) for the compact analytic variety. For every \(m\), Theorem 11.1 gives a natural, coefficient-compatible isomorphism \(H^q_{\mathrm{\acute et}}(X,\mathbf Z/\ell^m)\simeq H^q(C^\bullet/\ell^m)\). The finite cohomology towers satisfy Mittag–Leffler, so the Milnor \(\varprojlim^1\) term is zero. The degreewise surjective cellular tower has derived limit \(C^\bullet\otimes\mathbf Z_\ell\). This proves (14.1). Flat tensoring with \(\mathbf Q_\ell\) commutes with its cohomology; since the integral complex is finite free, the resulting group is \(H^q(C^\bullet\otimes\mathbf Q)\otimes_{\mathbf Q}\mathbf Q_\ell\). Its dimension is \(b_q\), proving the assertion. In contrast, the exact sequence

\[
0\to H^q(X^{\mathrm{an}},\mathbf Z)\otimes\mathbf F_\ell
\to H^q(X^{\mathrm{an}},\mathbf F_\ell)
\to\operatorname{Tor}_1^{\mathbf Z}
(H^{q+1}(X^{\mathrm{an}},\mathbf Z),\mathbf F_\ell)\to0
\]

shows the two torsion contributions. Comparison equates the two finite-coefficient theories, but cannot remove those terms from their dimension.

**Solution 3.** Pullback along \(\epsilon\) is exact and preserves tensor products and their symmetry. The ordinary comparison is the adjoint of the pulled-back counit, so evaluation and cup diagrams commute. The compact comparison is built with the same adjunction after exact \(j_!\); its projection diagram commutes as well. Thus mixed compact/ordinary products compare, and exchange of degrees \(a,b\) has the common Koszul sign \((-1)^{ab}\).

For the trace use \(\Lambda(d)\), not untwisted \(\Lambda\): the map is \(R^{2d}f_!\Lambda(d)\to\Lambda_S\). In relative dimension one, Kummer and the positive winding of a simple parameter give the \(+1\) point Thom class. In dimension \(d\), choose étale coordinates at a point of each smooth fibre and take the product of the \(d\) divisor Thom classes. Gysin transitivity and the even shifts identify it with the point class, and analytification sends it to the positive complex orientation. On every connected fibre the algebraic and topological top compact groups are generated by this class and both traces send it to \(1\); for disconnected fibres both traces sum these values. Proper-support base change identifies the relative stalks with these compact fibre groups. Equality on every analytic stalk proves the relative trace comparison. A compatible root \(\zeta_n\) translates the Tate twist to the usual analytic orientation convention; without it retain the twist. This establishes the trace compatibility actually used in smooth ordinary comparison.

**Solution 4.** For a smooth projective curve, degree zero follows by applying full faithfulness of Riemann existence to a trivial finite cover. Degree one follows by applying the equivalence to finite \(\Lambda\)-torsors with their group actions. Degree two follows from natural Kummer diagrams and Picard GAGA: algebraic \(H^2(\mathbf G_m)=0\); analytic \(H^2(\mathcal O^*)=0\) follows from the exponential sequence, Dolbeault vanishing above one and surface cohomology vanishing above two. Both Kummer cokernels are \(\operatorname{Pic}/n\). Higher constant groups vanish on both sides.

For every constructible sheaf on a proper curve, choose a dense normal open trivializing its finite monodromy. Embed its generic finite module into a finite sum of constant modules after a finite étale cover. Finite normalization extends the cover over the curve, and \(j'_*\Lambda=\Lambda\) on that normal cover. Add the boundary stalk sheaves to make the map injective on the whole curve. Repeat on the constructible cokernel. Finite pushforward is exact and comparison-compatible, so every term of this right resolution compares by the constant smooth projective curve theorem. In a fixed total degree the first-quadrant hypercohomology spectral sequence uses only finitely many terms and its comparison proves the assertion for the original sheaf.

Induct now on proper fibre dimension. Proper base change on both sides reduces a relative map to proper complex fibres. For a fibre of dimension \(d\geq2\), choose a rational function nonconstant on every positive-dimensional component and close its graph in \(X\times\mathbf P^1\). Its map \(a\) to \(\mathbf P^1\) has fibre dimension at most \(d-1\); the structural map \(b\) of \(\mathbf P^1\) has fibre dimension one. Induction compares \(Ra_*j'_!F_U\), proper constructibility permits comparison of its cohomology sheaves along \(b\), and the finite Leray filtrations compare its global cohomology on the graph. The proper graph projection is an isomorphism over \(U\); its pushforward of \(j'_!F_U\) is exactly \(j_!F_U\), because its other fibres carry zero coefficients. The boundary \(X\setminus U\) has smaller dimension, so localization finishes the comparison on \(X\). Proper base change then finishes the relative induction.

Express an arbitrary torsion sheaf as a filtered colimit of constructible finite torsion sheaves. Coherent étale continuity and compact Hausdorff continuity on the proper analytic fibres justify passage to that colimit on both sides. Finally compactify the given separated \(f\) and apply the proper result to \(j_!F\). This proves its arbitrary-torsion \(Rf_!\) comparison, independently of higher-dimensional resolution.

For ordinary constructible comparison, first use compact comparison, trace orientation and smooth Poincaré duality to compare constant coefficients on smooth schemes. Invoke the explicitly stated resolution-of-singularities prerequisite for a reduced \(X\). The cone of \(\Lambda_X\to Rp_*\Lambda_Y\) is bounded constructible and supported on the lower-dimensional complement of the open over which the proper resolution is an isomorphism. Proper comparison identifies its analytic cone; support induction and smooth constant comparison therefore prove constant comparison on \(X\). The finite-cover right resolution in arbitrary dimension then proves ordinary comparison for every constructible sheaf. Without constructibility this last argument does not apply, and the direct-sum/product example in Section 12 proves that its conclusion would be false.

## 17. Sources, proof dependencies and status

The historical comparison result is due to Artin; see [SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf), *Arcata*, IV, 6.3. Its concise reduction to proper smooth curves is expanded here into explicit coefficient resolutions, the proper graph induction, and filtered-colimit arguments. [SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XVI, Section 4, including Theorem 4.1 and Lemmas 4.2–4.6, proves a more general relative comparison and uses resolution of singularities for the nonproper case. This lesson proves the absolute statement; the relative theorem is not proved here.

- **[Riemann existence, stated input]** [AI Integrated Stacks Project, Riemann existence](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-riemann-existence). Its reference to SGA 1, Exposé XII, Theorem 5.1, supplies the full finite-cover equivalence. Its displayed “proof” cites that theorem; it is not a new owned proof of Riemann existence.
- **[Curve GAGA, stated input]** [GAGA comparison statements](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-section-gaga-statements), particularly theorem-gaga-fully-faithful and theorem-gaga-essential-surjectivity. The projective-curve Picard consequence is the allowed input used in Section 5; no general coherent analytic comparison is substituted for the torsion comparison proved here.
- **[Algebraic base change]** [Proper base change, Tag 095T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-proper-base-change) and [smooth base change, Tag 0EYU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-smooth-base-change). The first is used in every proper fibre calculation. The second checks the smooth framework from Lesson 15; it alone cannot compare a nonproper analytic boundary stalk.
- **[Classical sheaf tools]** [Proper base change in topology, cohomology chapter](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-proper-base-change), including the compact-neighbourhood refinement argument preceding it. [J. Anschütz, *Lecture notes on étale cohomology*](https://janschuetz.perso.math.cnrs.fr/skripte/lecture_notes_etale_cohomology.pdf), Theorem 4.16 and Lemma 4.20, PDF pages 25–27, give proper base change and compact Hausdorff continuity.
- **[Alternative comparison exposition]** [J. S. Milne, *Lectures on Étale Cohomology*, version 2.21](https://www.jmilne.org/math/CourseNotes/LEC.pdf), Section 21, PDF pages 130–134. Its analytic effacement through elementary fibrations is a useful alternative; the present proper-support proof instead uses graph modifications, so no elementary-fibration lemma is silently assumed.
- **[Geometric prerequisite for Section 11]** [M. Temkin, *Functorial desingularization of quasi-excellent schemes in characteristic zero: the non-embedded case*, Theorem 1.2.1, arXiv:0904.1592v2](https://arxiv.org/pdf/0904.1592v2), page 3. We verified the statement and its hypotheses. It gives the proper smooth resolution used in (11.2); the long resolution algorithm itself is outside this étale-cohomology course and is not claimed as proved here.
- **[Classical duality prerequisite]** [A. Hatcher, *Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Section 3.3, Theorem 3.35, gives the noncompact manifold cap-product theorem. The dual-cell discussion on printed page 232 also explains the orientation mechanism. Section 10 makes the exact coefficient-dual step needed over \(\mathbf Z/n\) explicit.

Within this course, Lesson 11 supplies the constructible and continuity machinery, Lesson 13 proper base change, and Lesson 14 compactification and proper support. Lesson 17 fixes the curve trace and coefficient self-injectivity. Lesson 18 supplies smooth duality, the point/divisor Gysin normalization and the projective-space computation. Their stated geometric and higher-trace inputs retain their stated status.

The Artin proper-support theorem and the ordinary constructible theorem are proved in Sections 5–11; neither is relegated to an unproved citation. Riemann existence and curve GAGA remain the two permitted analytic inputs. The resolution and classical topology prerequisites are expressly identified where they enter. All examples and all four exercises have full solutions.
