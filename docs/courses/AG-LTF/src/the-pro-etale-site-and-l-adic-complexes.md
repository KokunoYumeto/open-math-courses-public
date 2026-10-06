# The pro-étale site and ℓ-adic complexes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite locally constant sheaf becomes constant on a finite étale cover. A lisse adic sheaf can require a different cover at every level. The pro-étale topology permits the inverse limit of those covers to be a cover. It also makes the inverse limits used for coefficients behave much better than they do on the étale site.

The enlargement must pass two tests. It should preserve the cohomology already computed with étale sheaves, and it should handle completion without discarding torsion information. We prove both statements. We then prove proper base change for completed complexes by reducing it to torsion étale base change.

This lesson uses sheaves on sites, injective resolutions, the Čech acyclicity criterion, torsion proper base change and derived tensor products. The preceding lesson supplies strict adic systems, their uniform stratification and the compatible-perfect-complex theorem. The main reference is [Stacks, Pro-étale Cohomology]. The rest of the course can use the classical formalism without using this lesson's site constructions.

Write \(O=\mathbb Z_\ell\) and \(O_n=O/\ell^nO\). A constant sheaf with value \(O\) carries the discrete value group; its completion will be a different sheaf. Our schemes and sites lie in a fixed sufficiently large partial universe, closed under the fibre products and countable constructions used here. This is the size convention in [Stacks, Tag 0988]; “all objects” always means objects in that universe.

## 1. Enlarging the covers

**Definition 1.1.** A morphism \(f:Y\to X\) is *weakly étale* if \(f\) and its diagonal \(Y\to Y\times_XY\) are flat. A ring map is *ind-étale* if its target is a filtered colimit of étale algebras over its source.

Every étale morphism is weakly étale. It is flat, and its diagonal is an open immersion, hence flat. Weakly étale morphisms are closed under base change and composition: base change preserves both flatness conditions, and the diagonal of a composite factors through a base change of one diagonal and the other diagonal. Ind-étale ring maps are weakly étale, by passage to filtered colimits in these flatness statements. No finite-presentation condition occurs in the definition of weakly étale.

### 1.1. The algebra behind the affine basis

The two covering theorems need more than flatness of the original map. We prove them here. The basic henselian criteria are [Henselian local rings and henselization](course:AG-CA/AG-CA-20), Theorems 1.2 and 2.2 and Propositions 3.1–3.2; they apply to arbitrary local rings. General valuation domination is proved in [Valuation rings and separatedness](course:AG-MO/AG-MO-04), Theorem 2.1. No Noetherian assumption will enter the covering constructions.

**Lemma 1.1a (flat diagonal and local rigidity).** Let \(A\to B\) be weakly étale.

1. A \(B\)-module that is flat over \(A\) is flat over \(B\). Every map between weakly étale \(A\)-algebras is weakly étale.
2. The residue-field extensions of \(A\to B\) are separable algebraic.
3. If \(A,B\) are local, the map is local, and \(A\) is strictly henselian, then \(A\to B\) is an isomorphism.

**Proof.** For the first assertion, write the tensor functor on a \(B\)-module \(M\) as

\[
M\otimes_B N=
(M\otimes_A N)\otimes_{B\otimes_A B}B.
\tag{1.1}
\]

Both functors on the right are exact if \(M\) is \(A\)-flat. If \(B\to C\) is a map between weakly étale \(A\)-algebras, this gives its flatness. The diagonal condition follows by applying the same argument to the surjection \(C\otimes_A C\to C\otimes_B C\): \(C\), already flat over \(C\otimes_A C\), is flat over the quotient. This also proves permanence under filtered colimits, using exactness of filtered colimits and the finite-relation criterion for flatness.

We will use one elementary fact about a flat surjection \(R\to R/I\). For each \(i\in I\), there exists \(j\in I\) with \(i=ij\). Indeed, apply the flatness criterion to \(i\cdot1=0\) in \(R/I\). It gives \(1=\sum a_k\bar n_k\), with \(ia_k=0\). For lifts \(n_k\), put \(j=1-\sum a_kn_k\). Then \(j\in I\) and \(i=ij\). Consequently \(I=I^2\). Also \(R/I\) is a localization of \(R\): invert every element whose image is a unit in \(R/I\). This kills \(i\), because \(1-j\) becomes invertible; and a fraction with zero image has its numerator in \(I\), proving injectivity of the resulting map. In particular a flat surjection that is bijective on spectra is an isomorphism: its kernel is nil, and \(i=ij\) with nilpotent \(j\) forces \(i=0\).

For a field \(K\), suppose \(K\to R\) has flat diagonal. The first assertion makes every \(R\)-module flat. Each localization \(R_{\mathfrak q}\) is a field: its quotient by any ideal is flat, and the preceding identity in a local ring makes every proper ideal zero. Thus \(R\) is reduced with all primes maximal. Its local fields are separable algebraic over \(K\). To see this, a subfield \(K\subset L'\subset L\) inherits flat diagonal by faithfully flat descent along \(L'\to L\). The diagonal ideal has square equal to itself, so \(\Omega_{L'/K}=0\). For a field generated by \(x_1,\ldots,x_n\), write it as the fraction field of \(K[X_1,\ldots,X_n]/\mathfrak p\). Vanishing of differentials makes the conormal map from the cotangent space of \(K[X]_{\mathfrak p}\) onto \(L'^n\) surjective. This regular local ring has cotangent dimension \(\operatorname{ht}\mathfrak p\leq n\), so equality holds. The polynomial-ring height formula gives transcendence degree \(n-\operatorname{ht}\mathfrak p=0\). The extension is finite, and the triangular minimal-polynomial Jacobian makes it separable. These dimension and field steps are the written argument in [Formally smooth, unramified and étale ring maps](course:AG-CA/AG-CA-17), Lemma 7.1 and Theorem 7.2, using its specified regular-local and dimension providers. Apply this calculation to every finite list of field generators in \(L\).

It follows that \(R\) itself is ind-étale over \(K\). Here is why finite generation introduces no extra hypothesis. A finitely generated subalgebra \(D\subset R\) is reduced. Every minimal prime of \(D\) is the contraction of a prime of \(R\): localize away from that minimal prime, use the injection into \(R\) to see that the localized ring is nonzero, and take a prime there. The associated field embeds into a separable algebraic local field of \(R\). Thus each generic point of \(D\) is closed. The reduced Noetherian zero-dimensional ring \(D\) is a finite product of finite separable extensions of \(K\). It is étale. Taking the union of these subalgebras proves the assertion. Base change to \(\kappa(\mathfrak p)\) proves part 2.

For part 3 we need to control the fibres over every prime, rather than just the closed fibre. We first prove that a weakly étale algebra over a normal domain \(D\) is integrally closed in its localization over \(\operatorname{Frac}D\).

A normal domain is the intersection of the valuation rings of its fraction field containing it. In fact, if \(x\) is not integral, \((x^{-1})\) is a proper ideal of \(D[x^{-1}]\): an expression of 1 in that ideal, multiplied by a sufficiently high power of \(x\), would be a monic equation for \(x\). Dominate a localization at a maximal ideal containing \(x^{-1}\) by the valuation ring of Theorem 2.1 in the cited lesson. This valuation ring contains \(D\), and excludes \(x\), because \(x^{-1}\) is a nonunit. Normality gives the intersection assertion.

Choose such a family \(V_s\subset K=\operatorname{Frac}D\), and put \(V=\prod_sV_s\), \(L=\prod_sK\). Then \(D=K\times_L V\). The map \(V\to L\) is localization at tuples with every coordinate nonzero: denominators can be chosen separately in every coordinate. Every finitely generated ideal of \(V\) is projective. Indeed, its coordinate images are principal, and finite generation makes the ideal equal to the product of those images. If their generators are \(f_s\), write \((f_s)=g e\), where \(e_s\) is 1 when \(f_s\ne0\) and 0 otherwise, and \(g_s=f_s\) or 1 accordingly. Multiplication by the nonzerodivisor \(g\) identifies this ideal with the direct summand \(Ve\).

All ideals of \(V\) are therefore flat, being filtered unions of finitely generated ideals. Submodules of finite free modules are flat: successive coordinate projections give a finite filtration with ideals as quotients. The same holds for arbitrary free modules by taking their finite coordinate pieces. Every module consequently has a flat resolution of length one. This property ascends under a weakly étale map \(V\to E\): the first kernel of a free \(E\)-resolution is \(V\)-flat by dimension shifting, and is \(E\)-flat by (1.1).

If a ring \(E\) has this property and \(E\to H\) is an injective flat ring epimorphism, then \(E\) is integrally closed in \(H\). For an integral \(z\in H\), the finite subalgebra \(E[z]\) is flat over \(E\), as a submodule of the flat module \(H\). Tensoring its inclusions shows

\[
E[z]\otimes_E E[z]\ \hookrightarrow
H\otimes_E H=H.
\]

Multiplication therefore makes \(E\to E[z]\) a finite ring epimorphism. Such a map is surjective: over every residue field its finite-dimensional fibre has multiplication an isomorphism, so its dimension is 0 or 1; its unit generates in either case. Nakayama, applied to the finite cokernel of the unit map at every prime, proves surjectivity. Hence \(E[z]=E\).

Now tensor \(D=K\times_L V\) with a weakly étale \(D\)-algebra \(E\). Flatness preserves this kernel diagram. The lower map \(E\otimes_DV\to E\otimes_DL\) is an injective flat epimorphism, and its source has flat dimension at most one. The preceding paragraph makes its source integrally closed in its target. The kernel diagram then makes \(E\) integrally closed in \(E\otimes_DK\), as asserted.

Return to the local map \(A\to B\), and fix \(\mathfrak p\subset A\). Its fibre \(B\otimes_A\kappa(\mathfrak p)\) is a nonzero ind-étale algebra over \(\kappa(\mathfrak p)\); nonzero follows because a flat local map is faithfully flat. If this fibre has several points, it has a nontrivial idempotent. If it has one point but a nontrivial residue extension, a finite separable field extension \(L/\kappa(\mathfrak p)\) splits a nontrivial finite subextension and produces a nontrivial idempotent after tensoring with \(L\). In the first case take \(L=\kappa(\mathfrak p)\).

Let \(A'\) be the integral closure of \(A/\mathfrak p\) in this \(L\). Its fraction field is \(L\): clearing the denominators of a monic equation shows that a suitable nonzero multiple of any element of \(L\) is integral over \(A/\mathfrak p\). The henselian finite-algebra criterion makes every finite integral domain over \(A/\mathfrak p\) local and henselian. Filtered union makes \(A'\) strictly henselian local, with purely inseparable residue extension of that of \(A\). These are precisely the arbitrary-ring results in the cited henselian lesson.

The integral \(B\)-algebra \(B\otimes_AA'\) is local. Every maximal ideal lies over the maximal ideal of \(B\). Its fibre there has one prime, since a purely inseparable residue extension remains a one-point field extension, possibly with nilpotents, after any field base change. The normal-domain assertion just proved makes \(B\otimes_AA'\) integrally closed in \(B\otimes_AL\). An idempotent of the latter is integral, hence belongs to the former local ring, where it must be 0 or 1. This contradicts the idempotent constructed above.

Thus every fibre has one point with the unchanged residue field. Multiplication \(B\otimes_AB\to B\) is now a flat surjection bijective on spectra, hence an isomorphism. Finally, faithfully flat descent gives \(A=B\): the equalizer of \(B\rightrightarrows B\otimes_AB\) is \(A\), as follows by tensoring with \(B\), where the usual insertion-of-1 homotopy splits the descent sequence. The two arrows here are equal. This proves part 3, Olivier's local rigidity theorem. \(\square\)

### 1.2. Keeping every point while organizing the components

Call a ring map **ind-Zariski** if it is a filtered colimit of affine maps that locally are open immersions. Finite products of localizations are examples. Such maps are ind-étale and identify all local rings. For the latter assertion, at a prime of the colimit localize each stage at its contracted prime; each stage local ring is the same base local ring, so their colimit is that ring. Base change and composition preserve ind-Zariski maps. To check composition, descend the finite presentation of a stage and its finitely many open charts, together with their inverse maps, to one stage of the first system. The equations saying that these maps are inverse and that the charts cover use finitely many elements. They hold at a later stage; there the composite locally is an open immersion. The same finite-equation argument proves the corresponding composition statement for ind-étale maps.

An affine spectrum \(X\) is **w-local** if its closed points \(X_0\) form a closed subset and each point specializes to exactly one of them. Then \(X_0\) is profinite and is the space \(\pi_0(X)\) of connected components. For profiniteness, a reduced zero-dimensional ring has field localizations, hence is absolutely flat; its principal ideals are generated by idempotents, so its spectrum has a clopen basis and is compact Hausdorff. Reduction does not change the spectrum. Here and below the usual component space of an affine spectrum is profinite: finite clopen partitions, equivalently finite families of orthogonal idempotents summing to 1, give its inverse-limit description. In the w-local case a clopen partition of \(X_0\) extends uniquely to \(X\), by putting a point in the part containing its closed specialization. For example, these parts are closed in the constructible topology and stable under specialization, hence closed in the spectral topology; applying this to their complements makes them clopen. Thus each component is the spectrum of the local ring at its unique closed point.

**Lemma 1.1b (two explicit constructions).**

1. For every ring \(R\) there is a faithfully flat ind-Zariski map \(R\to R_w\) whose spectrum is w-local, and whose closed points map bijectively onto all points of \(\operatorname{Spec}R\).
2. If \(\operatorname{Spec}R\) is w-local and \(T\to\pi_0(\operatorname{Spec}R)\) is a map of profinite spaces, there is an ind-Zariski \(R\)-algebra \(R_T\) with

\[
\operatorname{Spec}R_T=
\operatorname{Spec}R\times_{\pi_0(\operatorname{Spec}R)}T,
\qquad \pi_0(\operatorname{Spec}R_T)=T.
\tag{1.2}
\]

Its local rings are the corresponding local rings of \(R\). A surjective map of component spaces gives a faithfully flat ring map.

**Proof.** For a locally closed subset \(Z=V(I)\cap D(f)\), invert in \(R\) every element that is a unit in \((R/I)_f\), and denote this localization by \(R_Z\). Its spectrum consists exactly of the points specializing to \(Z\). Indeed, if \(\mathfrak p\) has no such specialization, then \(\mathfrak p(R/I)_f=(R/I)_f\); clearing denominators gives \(f^n=g+h\), with \(g\in\mathfrak p\), \(h\in I\). The element \(g\) is inverted. Conversely, for \(\mathfrak p\subset\mathfrak q\in Z\), all inverted elements avoid \(\mathfrak q\). This also shows that the localization depends only on \(Z\), that \(Z\) is closed in it, and that inclusion of such subsets gives the compatible localization maps.

For a finite set \(E\subset R\), partition its spectrum by the vanishing pattern of the members of \(E\). The stratum indexed by \(E=E'\amalg E''\) is

\[
Z_{E',E''}=V(E'')\cap D\!\left(\prod_{e\in E'}e\right).
\]

Take the finite product of the rings \(R_{Z_{E',E''}}\). Enlarging \(E\) gives a compatible map of these products. Let \(R_w\) be their filtered colimit. Each product is flat over \(R\), and the strata exhaust its spectrum, so each product is faithfully flat. The colimit is faithfully flat as well: every proper ideal stays proper at every stage, and an equation making its extension contain 1 would already occur at a stage.

The disjoint unions of the closed strata form a compatible closed subset \(Z_w\subset\operatorname{Spec}R_w\), with one point over each prime of \(R\). Every point of \(\operatorname{Spec}R_w\) specializes to a point of \(Z_w\). One can check existence at the finite stages: the closure of its image meets the closed stratum there. These intersections are nonempty compact spaces for the constructible topology; their inverse limit is nonempty by the finite-intersection property. Distinct points of \(Z_w\) are separated by a clopen partition coming from a member of \(R\) in one prime and not the other. No point can specialize to both. Since \(Z_w\) is closed, this also makes its points closed and proves that it is exactly the closed-point set. This proves part 1.

For part 2, first realize a closed subset \(T\) of the component space by intersecting all its clopen neighborhoods. On rings this is the filtered colimit of localization at the associated idempotents. Now write a general profinite \(T\) as \(\varprojlim T_i\), with \(T_i\) finite. The image of \(T\) in \(\pi_0(\operatorname{Spec}R)\times T_i\) is closed, and the preceding construction realizes it on the finite product \(R^{T_i}\). Take the colimit of these rings. The associated spectra have inverse limit (1.2). The fibres over \(T\) are the original connected components; hence the component space is \(T\), and the closed-point set is the inverse image of the original one. This proves w-locality. Flatness and surjectivity on spectra prove the last assertion. \(\square\)

We need two consequences of these constructions. First, if a closed subset \(V(J)\) of \(\operatorname{Spec}R\) is profinite, apply part 1 and then retain the closed points lying over \(V(J)\), by the localization construction in its proof. The resulting ind-Zariski algebra has w-local spectrum, closed-point set \(V(J)\), and unchanged local rings there. We call this **localization along the closed profinite subset**. The quotient modulo \(J\) is unchanged: its spectrum is homeomorphic to \(\operatorname{Spec}(R/J)\) and all its local rings are unchanged, giving an isomorphism of locally ringed spaces.

Second, a map between w-local affine spectra that sends closed points to closed points and identifies local rings is ind-Zariski. Construct (1.2) using its source's component space. The map to that constructed affine is determined by the point map: when a morphism identifies local rings, its structure sheaf is the inverse image of the base structure sheaf, so continuous maps over the base lift uniquely to morphisms of locally ringed spaces. This new map identifies local rings and gives a bijection on closed points. It is an isomorphism. Indeed, on each component it identifies the spectra of the corresponding local rings, so it is bijective on all points. It is flat, as can be tested on these local-ring maps. Going down from the unique point above a base prime lifts every smaller prime; bijectivity then says that every point over such a smaller prime is a generization of that unique point. Localizing on the base therefore gives a local ring with just that point as maximal ideal, hence the given identical local ring. Kernel and cokernel of the ring map vanish after every such localization, and therefore vanish. This proves the consequence without assuming that an arbitrary map identifying local rings is already ind-Zariski.

### 1.3. Making the closed local rings strict

**Lemma 1.1c.** For every ring \(A\) there is a faithfully flat ind-étale map \(A\to C\) such that \(\operatorname{Spec}C\) is w-local, every local ring at a closed point is strictly henselian, and the closed points of \(C\) map onto all points of \(A\).

**Proof.** For a ring \(R\), form the tensor products of all finite families of faithfully flat étale \(R\)-algebras, using a set of finite-presentation representatives. Their filtered colimit \(T(R)\) is faithfully flat and ind-étale. Every faithfully flat étale \(R\)-algebra maps into it. Iterate this construction and put

\[
R_\infty=\varinjlim_{n\geq0}T^n(R).
\tag{1.3}
\]

Every faithfully flat étale \(R_\infty\)-algebra has a retraction. Its finite presentation descends to an étale algebra over a stage \(T^n(R)\). Faithful flatness of the colimit over that stage makes this descended algebra faithfully flat: its spectrum must cover the stage's spectrum. It maps into \(T^{n+1}(R)\), which gives the required retraction after extension to \(R_\infty\).

For any ring \(S\) with this retraction property, every \(S_{\mathfrak m}\), at a maximal ideal, is strictly henselian. Here are the localization details. Given an étale algebra and a point of its closed fibre, shrink by one element so that it is the only point above \(\mathfrak m\). The image is an open \(U\) containing \(\mathfrak m\). If its closed complement has ideal \(I\), then \(I+\mathfrak m=S\). Choose \(f\in\mathfrak m\) with \(1-f\in I\). The product of this étale algebra with \(S_f\) is faithfully flat over \(S\). A retraction, localized at \(\mathfrak m\), must select the first factor, since the second has zero closed fibre. It induces a retraction of the selected local étale algebra onto \(S_{\mathfrak m}\). This retraction is itself flat, by part 1 of Lemma 1.1a. A local flat map is faithfully flat and injective; an injective retraction makes the original map an isomorphism. Simple roots in the residue field therefore lift, and every finite separable residue extension is trivial. These are exactly henselianity and separable closedness. Étale algebras over \(S_{\mathfrak m}\) descend to a principal localization of \(S\), so the argument tests all of them.

Now start with \(R=A_w\) from Lemma 1.1b. Let \(I\) cut out its closed points. The spectrum of \(R_\infty/IR_\infty\) is profinite: over the zero-dimensional spectrum of \(R/I\), all residue extensions are algebraic, so all its primes are maximal. Localize \(R_\infty\) along this closed profinite subset, and call the result \(C\). Its maximal local rings are those of \(R_\infty\) at maximal ideals, hence strictly henselian. Its closed points cover the closed points of \(A_w\), and thus all points of \(A\). The map \(A\to C\) is flat and surjective on spectra, hence faithfully flat. It is ind-étale by construction. \(\square\)

**Theorem 1.1d (affine refinement).** If \(A\to B\) is weakly étale, there is a faithfully flat ind-étale map \(B\to B'\) for which \(A\to B'\) is ind-étale.

**Proof.** Choose \(A\to C\) as in Lemma 1.1c, and let \(I\) cut out the closed points of \(C\). Set \(D=B\otimes_A C\). Its map from \(C\) is weakly étale. By Lemma 1.1a, \(\operatorname{Spec}(D/ID)\) is profinite. Localize \(D\) along this closed subset, obtaining \(B'\). The map \(B\to B'\) is ind-étale and flat. It is surjective on spectra: for a prime \(\mathfrak q\) of \(B\), choose a closed point of \(C\) mapping to its contracted prime of \(A\). The tensor product of their residue fields over that field is nonzero and has a prime, retained by the localization. It lies over \(\mathfrak q\).

Both \(C\) and \(B'\) are w-local, and the latter's closed points map to those of \(C\). At any such pair of points, the weakly étale local map out of the strictly henselian local ring is an isomorphism by Lemma 1.1a. Localizing this isomorphism at the other primes in that component identifies every local ring. The second consequence of Lemma 1.1b now says that \(C\to B'\) is ind-Zariski. Thus \(A\to B'\) is ind-étale. \(\square\)

This proves the affine-basis theorem [Stacks, Tag 097Z], including its necessary refinement on the source. It does not assert that every weakly étale affine map is itself ind-étale.

### 1.4. Covers on which all lifts exist

**Lemma 1.1e (projective component spaces).** Every profinite space \(P\) admits a continuous surjection \(T\to P\), with \(T\) compact Hausdorff and extremally disconnected. Every continuous surjection from a compact Hausdorff space onto such a \(T\) has a continuous section.

**Proof.** Take the underlying set \(S\) of \(P\), with the discrete topology, and let \(T\) be its space of ultrafilters. For \(E\subset S\), the sets \([E]=\{\mathcal U:E\in\mathcal U\}\) form a clopen basis. Distinct ultrafilters are separated by complementary such sets; the ultrafilter extension lemma gives compactness by the finite-intersection property. The closure of a union \(\bigcup_i[E_i]\) is \([\bigcup_iE_i]\). To check this, intersect with an arbitrary basic neighborhood; a nonempty intersection contains the principal ultrafilter of an element of \(E_i\) for some \(i\). Thus closures of open sets are open. Each ultrafilter chooses one member of every finite clopen partition of \(P\). These choices give a compatible point of the inverse limit defining \(P\), and hence a continuous map \(T\to P\). Principal ultrafilters map to the original elements, proving surjectivity.

For the section assertion, let \(Y\to T\) be a continuous surjection with \(Y\) compact Hausdorff. Among its closed subsets still surjecting, choose a minimal one \(Z\) by Zorn: intersections of chains still meet each compact fibre. We claim \(Z\to T\) is injective. Otherwise choose disjoint open neighborhoods \(U,V\) of two points in one fibre. Put \(E_U=T\setminus f(Z\setminus U)\) and \(E_V=T\setminus f(Z\setminus V)\). These are disjoint open subsets, since a fibre cannot be wholly contained in both \(U,V\). The common image point belongs to the closure of each. Indeed, for any neighborhood \(N\) of it, \(U\cap f^{-1}N\) is nonempty; minimality says its closed complement cannot surject. A missed fibre lies in that open set, producing a point of \(N\cap E_U\). The same holds for \(V\). In an extremally disconnected space disjoint opens have disjoint closures: the open closure of one cannot meet the other, and then cannot meet its closure. This contradiction proves injectivity. A continuous bijection from compact to Hausdorff is a homeomorphism; its inverse gives the section. \(\square\)

**Theorem 1.1f (contractible affine covers).** Every affine scheme has a faithfully flat ind-étale cover by a w-contractible affine scheme.

**Proof.** Choose \(A\to C\) as in Lemma 1.1c. Apply Lemma 1.1e to its component space, and realize \(T\to\pi_0(\operatorname{Spec}C)\) by Lemma 1.1b. The resulting faithfully flat ind-Zariski algebra \(C\to R=C_T\) is w-local, has extremally disconnected component space \(T\), and has strictly henselian local rings at its closed points. Thus \(A\to R\) is faithfully flat ind-étale.

Let \(R\to E\) be faithfully flat weakly étale. Localize \(E\) along the inverse image of the closed points of \(R\), obtaining a w-local algebra \(E'\). Its closed points still cover those of \(R\). Lemma 1.1a identifies the corresponding maximal local rings, and hence every local ring in their components. Consequently \(R\to E'\) identifies local rings and is ind-Zariski, by Lemma 1.1b. The surjection of its compact component spaces onto \(T\) has a continuous section by Lemma 1.1e. This gives a continuous section on spectra: a chosen component of \(E'\) is the identical local spectrum of the corresponding component of \(R\). Formally, use the identification (1.2) to take \(x\mapsto(x,s(\pi_0(x)))\). Because the structure sheaf of \(E'\) is the inverse image of that of \(R\), this is a section of locally ringed spaces, and therefore of affine schemes. On rings it is a retraction \(E'\to R\). Compose with \(E\to E'\) to obtain a retraction of \(R\to E\). This proves w-contractibility and the theorem [Stacks, Tag 0983]. \(\square\)

The constructions use tensor products of finite-presentation representatives, their filtered colimits, and ultrafilters on the component set. They lie in the fixed sufficiently large universe stipulated at the start; no countable-size restriction on a cover is asserted. The arguments above use Olivier's local theorem and the Bhatt–Scholze/Stacks covering constructions, cited in the references.

**Definition 1.2.** The small site \(X_{\mathrm{pro\acute et}}\) has weakly étale \(X\)-schemes as objects. A family \(Y_i\to Y\) is a cover if its members are weakly étale and, for every affine open \(V\subset Y\), finitely many affine opens in the \(Y_i\) have images whose union is \(V\). In other words, the family is weakly étale and fpqc. On an affine basis, covers can be taken to be finite jointly surjective families of affine objects.

The finite condition is part of the definition. Joint surjectivity alone is not the covering condition for an arbitrary family. Fibre products and composition give a topology because the corresponding properties hold for fpqc covers and weakly étale maps. Étale covers are pro-étale covers.

For example, if \(k^{\mathrm{sep}}/k\) is a separable closure, then

\[
\operatorname{Spec}(k^{\mathrm{sep}})=
\varprojlim_{L/k\ \mathrm{finite\ separable}}\operatorname{Spec}(L)
\]

is an affine ind-étale cover of \(\operatorname{Spec}(k)\). A tower of finite étale torsors can likewise be replaced by its affine inverse limit, locally on the base.

**Definition 1.3.** An affine scheme \(W=\operatorname{Spec}(A)\) is *w-contractible* if every faithfully flat weakly étale ring map \(A\to B\) has an \(A\)-algebra retraction. Equivalently one can test faithfully flat ind-étale maps: Theorem 1.1d refines any weakly étale map by such a map, and a retraction of the composite restricts to a retraction of the original map. An object of a site is *weakly contractible* if evaluation there sends epimorphisms of sheaves of sets to surjections of sets.

A w-contractible affine is weakly contractible in the pro-étale site. Indeed, a section of the target of an epimorphism lifts on a covering. Refine the covering to finitely many affine weakly étale maps. Their disjoint union is a faithfully flat weakly étale affine over \(W\), and a retraction gives a section \(W\to\coprod W_i\). Restrict the local lifts along this section. They give the requested lift over \(W\).

Theorem 1.1f gives every affine scheme a faithfully flat ind-étale cover by a w-contractible affine. Applying it to affine objects gives enough weakly contractible objects [Stacks, Tags 099Q and 0F4N]. For abelian sheaves, evaluation on such an object is exact, so

\[
H^i(W,A)=0\quad(i>0)
\]

for every abelian sheaf \(A\). This follows directly by evaluating an injective resolution: exact evaluation preserves the exact resolution.

## 2. Lifting infinitely many compatible choices

**Definition 2.1.** A topos is *replete* if, for every tower of epimorphisms of sheaves of sets

\[
\cdots\longrightarrow A_3\longrightarrow A_2\longrightarrow A_1,
\]

the projection \(\varprojlim A_n\to A_1\) is an epimorphism.

Enough weakly contractible objects imply repleteness. Given a section of \(A_1\), first work over a weakly contractible cover of its domain. Evaluation turns all transitions into surjections. Successively choose a lift in \(A_2\), then in \(A_3\), and so on. The resulting compatible sequence is a section of the limit. This proves local surjectivity of the projection. In particular, the pro-étale topos is replete.

**Theorem 2.2.** In a replete topos, countable products of abelian sheaves are exact. For a tower \(A_n\) of abelian sheaves, its derived inverse limit is represented by

\[
\left[\prod_{n\geq1}A_n
\xrightarrow{\,1-s\,}\prod_{n\geq1}A_n\right],
\qquad s((a_n))_n=f_n(a_{n+1}),
\tag{2.1}
\]

in degrees zero and one. If the \(f_n:A_{n+1}\to A_n\) are epimorphisms, then \(R\varprojlim A_n=\varprojlim A_n\) in degree zero.

**Proof.** Products are left exact. To prove that a product of epimorphisms \(B_n\to C_n\) is onto, take a section of \(\prod C_n\). The sheaves of lifts of its first \(r\) components form a tower of epimorphisms: an additional component can be lifted locally. Repleteness supplies a compatible family of partial lifts locally. It lifts the whole section. Thus countable products are exact.

Here is the algebra behind (2.1). For an object \(A\), the tower with value zero before position \(j\), value \(A\) from position \(j\) onward, and identity later transitions is right adjoint to evaluation at position \(j\). Such a tower has limit \(A\) and no higher derived limit: resolve \(A\) injectively, apply this exact right adjoint, and take the unchanged limit resolution. Products of these towers have the same acyclicity because countable products are exact. Embed a given tower into \(B_n=\prod_{j\leq n}A_j\) using its maps to earlier terms. The quotient is the tower \(C_n=\prod_{j<n}A_j\), with drop-coordinate transitions: the quotient map sends a vector to its successive differences \(x_j-f_j(x_{j+1})\), for \(j<n\). Its kernel is the embedded \(A_n\), and it is onto by solving this finite list of equations backward. Thus \(B\) and \(C\) give a length-one limit-acyclic resolution. Their limits are both \(\prod A_n\), and the induced map is \(1-s\). This proves (2.1). For complexes it is the homotopy-limit triangle

\[
R\varprojlim A_n\longrightarrow\prod A_n
\xrightarrow{1-s}\prod A_n\longrightarrow(R\varprojlim A_n)[1].
\]

Exact products allow the products of degree-zero objects to be computed in degree zero, giving (2.1).

It remains to show surjectivity of \(1-s\) when transitions are onto. Fix a section \((b_n)\) of the right-hand product. Let \(P_r\) be the sheaf of tuples \(x_1,\ldots,x_r\) satisfying

\[
x_i-f_i(x_{i+1})=b_i\qquad(1\leq i<r).
\]

The map \(P_{r+1}\to P_r\) is onto: locally lift \(x_r-b_r\) through \(f_r\) to obtain \(x_{r+1}\). The first sheaf \(P_1=A_1\) has its zero section. Repleteness gives a compatible infinite tuple locally. It solves \((1-s)x=b\). Thus the degree-one cokernel vanishes, and the degree-zero kernel is the ordinary inverse limit. ∎

We will also use the Mittag–Leffler version. If the images of \(A_m\to A_n\) stabilize for each \(n\), replace each term by its eventual image. The replacement tower has onto transitions: choose a stage late enough to realize the stable images at both positions \(n\) and \(n+1\). The quotient tower is pro-zero: every fixed term receives the zero map from sufficiently late terms. On a pro-zero tower, \(1-s\) is invertible, with \(n\)-th component of its inverse given by the finite sum of all later components transported to position \(n\). Consequently its derived limit is zero. The replacement therefore has the same derived limit, concentrated in degree zero.

Repleteness concerns the existence of compatible lifts after a cover. It does not say that sections of every epimorphism lift on every object. Weakly contractible objects provide that stronger property.

## 3. Preserving étale cohomology

Inclusion of étale objects gives a morphism of topoi

\[
\nu:X_{\mathrm{pro\acute et}}\longrightarrow X_{\mathrm{\acute et}}.
\]

The direct image \(\nu_*\) restricts a pro-étale sheaf to étale objects. We first describe its left adjoint.

**Proposition 3.1.** For an étale sheaf of sets \(F\), its inverse image is the sheaf

\[
(\nu^{-1}F)(Y)=\Gamma(Y_{\mathrm{\acute et}},f_{\mathrm{\acute et}}^{-1}F),
\qquad f:Y\to X.
\tag{3.1}
\]

The unit \(F\to\nu_*\nu^{-1}F\) is an isomorphism. In particular, \(\nu^{-1}\) is fully faithful, including on sheaves of sets.

**Proof.** Étale sheaves descend along fpqc covers; applying that descent to their pullbacks to \(Y\) shows that (3.1) is a sheaf. For clarity, a section is locally represented by sections on étale neighbourhoods, with their compatibility relations. Faithfully flat descent of étale morphisms descends both these neighbourhoods and the matching relations. Thus the ordinary étale sheaf condition supplies exactly the gluing required for a pro-étale cover.

Call this sheaf \(aF\). On an étale object \(U\to X\), the right-hand side of (3.1) is \(F(U)\), so \(\nu_*aF=F\). For a pro-étale sheaf \(G\), restriction gives maps

\[
G(U)\longrightarrow G(Y\times_XU).
\]

They induce \(f_{\mathrm{\acute et}}^{-1}(\nu_*G)\to G|_{Y_{\mathrm{\acute et}}}\), hence a natural map \(a\nu_*G\to G\). Restricting this map to an étale object is the identity. Applying it to \(aF\) is also the identity: a section represented on an étale neighbourhood is sent to that same section restricted to \(Y\). These are the two triangle identities. Thus \(a\) is left adjoint to \(\nu_*\), and equals \(\nu^{-1}\). An invertible adjunction unit makes the left adjoint fully faithful. ∎

The cohomology statement needs more than this unit calculation. We use the étale continuity theorem with its hypotheses: if \(Y=\varprojlim Y_i\), the \(Y_i\) are quasi-compact and quasi-separated, and the transition maps are affine, then the cohomology of pulled-back abelian sheaves commutes with the corresponding filtered colimit [Stacks, Tags 09YQ and 03Q6]. In degree zero this also gives

\[
(\nu^{-1}F)(Y)=\varinjlim_i(\nu^{-1}F)(Y_i).
\tag{3.2}
\]

For sheaves of sets, the degree-zero assertion follows from descent of finitely presented étale neighbourhoods and their equalities to a finite stage.

**Lemma 3.2.** If \(X\) is affine and \(I\) is injective on \(X_{\mathrm{\acute et}}\), then \(\nu^{-1}I\) has no positive pro-étale cohomology on \(X\).

**Proof.** Use the basis of affine objects ind-étale over \(X\), with finite affine ind-étale covers. It is stable under the fibre products in a Čech nerve. Take such a cover \(U_j\to U\). Write each \(U_j\) as an inverse limit of étale affines \(U_{j,a}\to U\). Every finite-stage family covers \(U\), since its images contain those of the original family. Fibre products commute with these limits. Formula (3.2), finite products in each Čech degree, and exact filtered colimits give

\[
\check H^p(\{U_j\to U\},\nu^{-1}I)
=\varinjlim_a\check H^p(\{U_{j,a}\to U\},\nu^{-1}I).
\]

Next write \(U=\varprojlim_b U_b\), with \(U_b\) affine étale over \(X\). The finitely presented cover \(U_{j,a}\to U\) and its finite fibre products descend to some stage \(b\). Surjectivity descends after increasing that stage: this is the finite-presentation limit theorem for a finite jointly surjective family. Another use of (3.2) expresses its Čech cohomology as a filtered colimit of the Čech cohomologies of étale covers of \(U_b\).

Those last complexes are acyclic in positive degrees for \(I\). Indeed, the augmented Čech complex of free abelian sheaves on a cover is exact locally, where the cover has a section and the nerve has a contracting homotopy. Applying \(\operatorname{Hom}(-,I)\) preserves exactness. Hence all the original basis Čech cohomologies vanish.

We recall why this criterion computes derived cohomology. Embed a sheaf \(A\) with these Čech vanishings into an injective \(J\), and put \(B=J/A\). A section of \(B\) lifts on a basis cover. The differences of the lifts are an \(A\)-valued Čech 1-cocycle, so they can be corrected to glue. Thus \(J(U)\to B(U)\) is onto on every basis object. The resulting short exact sequence of Čech complexes shows that \(B\) has the same positive-degree Čech vanishings. It also gives \(H^1(U,A)=0\), and dimension shifting repeats the argument for every higher degree. This is [Stacks, Tag 03F9]. Apply it with \(A=\nu^{-1}I\) and the chosen basis. ∎

**Theorem 3.3.** For every scheme \(X\) and every abelian étale sheaf \(F\),

\[
R\nu_*\nu^{-1}F\simeq F,
\qquad
H^i(X_{\mathrm{pro\acute et}},\nu^{-1}F)
\simeq H^i(X_{\mathrm{\acute et}},F).
\tag{3.3}
\]

More generally \(K\to R\nu_*\nu^{-1}K\) is an isomorphism for \(K\in D^+(X_{\mathrm{\acute et}})\).

**Proof.** Restriction of an injective étale sheaf to an étale object is injective: its restriction functor has the exact extension-by-zero left adjoint on the localized site. Apply Lemma 3.2 to affine étale objects. It shows that \(R^q\nu_*\nu^{-1}I=0\) for \(q>0\), since the presheaf describing this higher direct image vanishes on an affine étale basis. Exactness of inverse image carries an injective resolution of \(F\) to a resolution by \(\nu_*\)-acyclic sheaves. Applying \(\nu_*\) recovers the original resolution by Proposition 3.1. This proves the first isomorphism. Derived composition of global sections with \(\nu_*\) proves the second. The same argument with a bounded-below injective complex proves the statement for \(K\). ∎

This proves comparison for all abelian étale sheaves. No torsion or constructibility restriction was introduced.

Two extensions of (3.3) will be needed. First, bounded-below complexes whose cohomology sheaves come from the étale site themselves come from that site. To see this, the essential image of \(\nu^{-1}\) is closed under kernels and cokernels of its morphisms, by full faithfulness and exactness. It is also closed under extensions: apply \(\nu_*\) to an extension, use \(R^1\nu_*\nu^{-1}F=0\), pull back, and compare the end terms. The middle terms then agree. For a bounded-below complex use the spectral sequence of \(R\nu_*\) on its cohomology sheaves. Every positive \(R^p\nu_*\) on those sheaves vanishes by (3.3); therefore the counit \(\nu^{-1}R\nu_*K\to K\) is an isomorphism. This also proves the claimed derived equivalence.

Second, if \(f:X\to Y\) is quasi-compact and quasi-separated, then for \(L\in D^+(X_{\mathrm{\acute et}})\),

\[
Rf_{\mathrm{pro\acute et},*}\nu_X^{-1}L
\simeq\nu_Y^{-1}Rf_{\mathrm{\acute et},*}L.
\tag{3.4}
\]

This can be checked locally on affine \(Y\). On an affine ind-étale \(V=\varprojlim V_i\) over \(Y\), comparison (3.3) identifies the left-hand cohomology with étale cohomology of \(X\times_YV\). Continuity identifies it with the filtered colimit of the étale cohomologies of \(X\times_YV_i\); quasi-compactness and quasi-separatedness are exactly the hypotheses needed for [Stacks, Tag 03Q6]. These are the values defining the right-hand cohomology sheaves. Sheafification gives (3.4), first for sheaves and then for bounded-below complexes by their convergent cohomology spectral sequences. Pullback commutes with \(\nu^{-1}\) by the pullback square of sites. Neither assertion involves completion yet.

## 4. Completion remembers a complex

Define the completed coefficient sheaf by

\[
\widehat O=\varprojlim_n\underline{O_n}
\quad\text{on }X_{\mathrm{pro\acute et}}.
\]

The underline means constant sheaf. On a weakly contractible object the limit is computed on sections, and Theorem 2.2 says that it is also the derived limit. We write \(\widehat E=\widehat O[1/\ell]\).

There is a concrete reason for the hat. Over a separably closed field, let \(S\) be a profinite set and form the ind-étale affine which is the limit of the finite disjoint unions of points indexed by finite quotients of \(S\). Its sections of \(\widehat O\) are

\[
\varprojlim_n C(S,O_n)=C(S,O),
\]

where the right-hand side means continuous functions for the adic topology. Sections of the discrete constant sheaf \(\underline O\) are locally constant functions to the discrete set \(O\). Taking \(S=\mathbb Z_\ell\), the identity function belongs to the first group and not the second. Thus a complete value ring need not give a complete constant sheaf.

**Definition 4.1.** A complex \(K\) of \(O\)-module sheaves is *derived complete* if

\[
R\varprojlim(\cdots\xrightarrow{\ell}K\xrightarrow{\ell}K)=0.
\tag{4.1}
\]

Equivalently, the derived internal Hom from \(\underline{O[1/\ell]}\) to \(K\) vanishes: express \(O[1/\ell]\) by the telescope of multiplication by \(\ell\). Its derived completion is

\[
K^\wedge=R\varprojlim_n
\bigl(K\otimes_O^{\mathbf L}\underline{O_n}\bigr).
\tag{4.2}
\]

These formulas agree because \(O_n\) is represented over \(O\) by \([O\xrightarrow{\ell^n}O]\) in degrees \(-1,0\). Take the inverse limit of the corresponding triangles

\[
K\xrightarrow{\ell^n}K\longrightarrow
K\otimes_O^{\mathbf L}O_n.
\]

The transition on the first term is multiplication by \(\ell\); on the second it is the identity. The resulting triangle is

\[
R\varprojlim(\cdots\xrightarrow{\ell}K)
\longrightarrow K\longrightarrow K^\wedge.
\]

It proves that (4.1) is equivalent to \(K\simeq K^\wedge\). It also shows the role of the derived tensor product: reduction is the cone of multiplication, including its kernel.

Objects annihilated by a power of \(\ell\) are derived complete. In (4.1), the shift operator has a power equal to zero, so \(1-s\) has inverse \(1+s+\cdots+s^{c-1}\) if \(\ell^cK=0\). Derived complete objects are closed under derived limits and cones, since the telescope/internal-Hom description commutes with these limits. In particular (4.2) is derived complete. Completion is left adjoint to inclusion of derived complete objects: the telescope term has no maps to a complete object in any degree, and applying \(\operatorname{Hom}(-,L)\) to the last triangle gives \(\operatorname{Hom}(K^\wedge,L)=\operatorname{Hom}(K,L)\). The orthogonality follows by localizing the source in that Hom complex: multiplication by \(\ell\) is invertible on the telescope limit term, while the derived internal Hom from \(O[1/\ell]\) into complete \(L\) vanishes. The telescope limit term has invertible multiplication by \(\ell\), since shifting the inverse system is cofinal and its transition is precisely that multiplication.

**Proposition 4.2 (strict sheaves).** Let \(X\) be Noetherian and \((F_n)\) a constructible strict adic system. Then

\[
F=R\varprojlim_n\nu^{-1}F_n=\varprojlim_n\nu^{-1}F_n
\]

is a sheaf in degree zero, is derived complete, and its *ordinary* quotients satisfy

\[
F/\ell^nF=\nu^{-1}F_n.
\tag{4.3}
\]

There is instead a derived-reduction sequence

\[
H^{-1}(F\otimes_O^{\mathbf L}O_n)=F[\ell^n],
\qquad H^0(F\otimes_O^{\mathbf L}O_n)=\nu^{-1}F_n.
\tag{4.4}
\]

In particular derived reduction is just \(\nu^{-1}F_n\) when \(F\) is torsion-free.

**Proof.** The transitions are onto, so Theorem 2.2 gives the first equality. Each term is derived complete, and that property is closed under derived limits; hence \(F\) is complete.

Fix \(n\). For \(m\geq n\), strictness gives

\[
0\longrightarrow\ell^nF_m\longrightarrow F_m\longrightarrow F_n\longrightarrow0.
\tag{4.5}
\]

Pullback by \(\nu^{-1}\) is exact. The first terms have onto transitions, so taking limits in (4.5) identifies the kernel of \(F\to\nu^{-1}F_n\) with \(\varprojlim\nu^{-1}(\ell^nF_m)\). We must still show that this kernel is \(\ell^nF\).

The obstruction to dividing compatibly by \(\ell^n\) is the tower \(B_m=\ker(\ell^n:F_m\to F_m)\). This tower is Mittag–Leffler as sheaves, with a uniform stabilization index for each target level. Indeed, the preceding lesson gives a finite stratification of \(X\) on which the system comes from a finite \(O\)-module \(M\). Write \(M=O^r\oplus T\), with \(\ell^cT=0\), and choose one \(c\) for all strata. At level \(m\geq n\), the free part of \(B_m\) is \(\ell^{m-n}O^r/\ell^mO^r\); its image in level \(a\) is zero once \(m\geq a+n\). The torsion part and its images stabilize once \(m\geq c\). Hence images in a fixed level stabilize uniformly. Equality of these constructible subsheaves is tested on étale geometric stalks, and exact \(\nu^{-1}\) preserves these images.

The Mittag–Leffler conclusion after Theorem 2.2 now applies to \(\nu^{-1}B_m\). Taking limits of

\[
0\to\nu^{-1}B_m\to\nu^{-1}F_m
\xrightarrow{\ell^n}\nu^{-1}(\ell^nF_m)\to0
\]

is exact on the right. Thus the limit of the images is the image \(\ell^nF\), proving (4.3). Finally the free resolution of \(O_n\) used above identifies its derived tensor with \([F\xrightarrow{\ell^n}F]\); its cohomology is exactly (4.4). If the system has torsion-free adic stalks, the same stable-kernel calculation makes \(F[\ell^n]=0\). ∎

For example, take every \(F_n=\mathbb F_\ell\), with identity transitions. This is a strict constructible system. Its limit is \(\underline{\mathbb F_\ell}\), whereas

\[
\underline{\mathbb F_\ell}\otimes_O^{\mathbf L}O_1
=\left[\underline{\mathbb F_\ell}\xrightarrow{0}\underline{\mathbb F_\ell}\right]
\]

has nonzero cohomology in degrees \(-1\) and zero. Ordinary compatible sheaves are therefore different from compatible *derived* reductions. This example is why torsion needs (4.4).

**Proposition 4.3 (compatible derived systems).** Suppose complexes \(K_n\) of \(O_n\)-sheaves are given with coherent derived identifications

\[
K_{n+1}\otimes_{O_{n+1}}^{\mathbf L}O_n\simeq K_n.
\tag{4.6}
\]

Then \(K=R\varprojlim K_n\) is derived complete and \(K\otimes_O^{\mathbf L}O_n\simeq K_n\). Conversely the derived reductions of a complete \(K\) recover \(K\) in this way.

Here “coherent” means an actual derived diagram, retaining the homotopies between composites and their compatibilities. Merely listing isomorphism classes in triangulated categories would not specify such a diagram or all its morphisms.

**Proof.** Every \(K_n\), viewed as an \(O\)-complex, is complete, so their derived limit is complete. For \(m>n\), tensor the exact sequence of \(O_m\)-modules

\[
0\to O_{m-n}\xrightarrow{\ell^n}O_m\to O_n\to0
\]

with \(K_m\). Compatibility gives triangles

\[
K_{m-n}\longrightarrow K_m\longrightarrow K_n\longrightarrow K_{m-n}[1].
\tag{4.7}
\]

These triangles form a diagram as \(m\) varies. The last terms \(K_n\) form a constant diagram. Both first and second limits identify with \(K\) by cofinality. The first map becomes multiplication by \(\ell^n\): composing it with the reduction \(K_m\to K_{m-n}\) is multiplication by \(\ell^n\) on \(K_m\). Taking derived limits in (4.7) therefore gives

\[
K\xrightarrow{\ell^n}K\longrightarrow K_n.
\]

Its cone is \(K\otimes_O^{\mathbf L}O_n\), as required. The converse is (4.2), together with associativity of derived tensor products for successive coefficient quotients. These constructions also recover coherent maps, since limits act on the entire diagrams. ∎

Thus the relevant inverse limit of derived categories is the category of coherent compatible diagrams, not a termwise inverse limit of sets of morphisms. Applying \(\nu^{-1}\) to diagrams on the étale site gives this construction on the pro-étale site.

## 5. Constructible complexes and classical sheaves

**Definition 5.1.** The category \(D_{\mathrm{cons}}(X,O)\) is the full subcategory of \(D(X_{\mathrm{pro\acute et}},O)\) consisting of derived complete \(K\) for which \(K\otimes_O^{\mathbf L}O_1\) has constructible cohomology sheaves and locally finite Tor amplitude. The finite coefficient sheaves here come from the étale site. This agrees with [Stacks, Tag 09C0].

For a Noetherian \(X\), “locally finite Tor amplitude” admits one finite degree interval on a finite open covering. Since \(O_1\) is a field, boundedness of the constructible reduction gives this Tor condition. On a non-quasi-compact scheme the definition is local and need not provide a single global interval.

**Proposition 5.2.** If \(X\) is quasi-compact and \(K\in D_{\mathrm{cons}}(X,O)\), there are integers \(a\leq b\) such that every derived reduction \(K_n\) has Tor amplitude in \([a,b]\), has constructible cohomology, and comes from a bounded étale complex. Also \(K\) itself has cohomology in \([a,b]\).

**Proof.** Choose \([a,b]\) for the first reduction on finitely many opens. Every \(O_n\)-module sheaf has a finite filtration by powers of \(\ell\), with \(O_1\)-module layers. For a layer \(A\), associativity gives

\[
K_n\otimes_{O_n}^{\mathbf L}A
=K_1\otimes_{O_1}^{\mathbf L}A.
\]

It has cohomology in \([a,b]\). The triangles from the filtration give the same interval for arbitrary \(A\); this proves the Tor assertion. The coefficient exact sequences give triangles \(K_{n-1}\to K_n\to K_1\). Induction, and the closure under extensions, kernels and cokernels of constructible finite étale sheaves, prove constructibility of every reduction. The derived equivalence after Theorem 3.3 shows that each comes from an étale complex.

Complete \(K\) is the derived limit of these reductions. Exact products on the pro-étale site give the Milnor sequences for its cohomology sheaves; initially they bound it in \([a,b+1]\). The top maps \(H^b(K_{n+1})\to H^b(K_n)\) are onto: right exactness of reduction in the top nonzero degree identifies the latter with \(H^b(K_{n+1})\otimes_{O_{n+1}}O_n\). Theorem 2.2 removes the possible \(R^1\varprojlim\) in degree \(b+1\). The claimed interval follows. ∎

Conversely, uniformly bounded constructible finite-Tor étale complexes satisfying (4.6) give objects of \(D_{\mathrm{cons}}\) by Proposition 4.3. These two constructions identify the category with the coherent compatible finite-coefficient systems. Flat classical adic sheaves fit as systems in degree zero. A torsion sheaf also fits as an \(O\)-complex, but its system consists of the two-degree reductions (4.4).

On a connected stratum where the cohomology of \(K_1\) is locally constant, \(K\) is pro-étale locally the completed constant sheaf of a bounded finite free \(O\)-complex. We give the compatibility argument, since separate trivializations at each level do not suffice. The finite-coefficient local-structure theorem says that a constructible finite-Tor complex with locally constant cohomology on a connected scheme is étale locally a constant perfect coefficient complex [Stacks, Tag 09BI]. Apply it to every \(K_n\); its cohomology is locally constant by the preceding filtration argument. The resulting perfect coefficient complexes \(M_n\) can be chosen with derived reduction identifications: their local isomorphism types are constant on the connected stratum, and the identifications can be read on a common neighbourhood. Theorem 6.1 of the preceding lesson gives a bounded finite free complex \(P\) with \(P/\ell^n\simeq M_n\).

Choose a weakly contractible affine cover \(W\). Each \(K_n|_W\) is isomorphic to the completed constant complex \(\underline{P/\ell^n}|_W\). To make the isomorphisms compatible, use the complexes

\[
H_n=R\mathcal Hom_{O_n}(\underline{P/\ell^n},K_n).
\]

At each geometric stalk the compatible perfect-complex argument identifies this cohomology tower with that of \(P^\vee\otimes_OP\) reduced modulo \(\ell^n\). Its cycles and boundaries are finite modules, and the Artin–Rees estimate bounds the images uniformly at each fixed level. The bound depends on the one coefficient complex \(P^\vee\otimes_OP\), common to the connected stratum. Thus the images stabilize as finite-coefficient sheaves, without having assumed a simultaneous trivialization. Exact evaluation on \(W\) preserves the images. Hence \(H^0(W,H_n)\) is a Mittag–Leffler tower. Its eventual image at level one contains an isomorphism: each finite-stage image contains an isomorphism, and these images eventually agree. Choose one and lift it compatibly in the eventual-image tower. Its derived limit is a map \(\widehat{\underline P}|_W\to K|_W\) whose first reduction is an isomorphism. Its complete cone has first reduction zero; all reductions then vanish by the coefficient filtration, and the cone itself vanishes by completeness. This is the required isomorphism.

A finite stratification makes the cohomology of \(K_1\) locally constant, so this proves the adic constructible description for Noetherian \(X\) [Stacks, Tag 09C7]. Restrictions to strata can be read through their finite reductions followed by derived limit, that is, through the completed pullback defined in §6. The topology changes, but no finite coefficient information disappears.

For a classical system \((F_n)\), Proposition 4.2 also recovers its ordinary cohomology in the usual geometric finiteness setting. Derived global sections commute with derived limits, being a derived right adjoint. Thus

\[
0\to\varprojlim{}^1 H^{i-1}(X_{\mathrm{\acute et}},F_n)
\to H^i(X_{\mathrm{pro\acute et}},F)
\to\varprojlim H^i(X_{\mathrm{\acute et}},F_n)\to0.
\tag{5.1}
\]

If \(X\) is separated of finite type over an algebraically closed field and \(\ell\) is invertible there, the finite-level groups are finite by the preceding lesson's torsion prerequisites. They are Mittag–Leffler, so the left term is zero. The right term is precisely its classical adic cohomology. For other bases one must retain the left term until its vanishing has been proved.

## 6. Proper base change after completion

We state the coefficient generality explicitly. Let \(\Lambda\) be a commutative Noetherian ring and \(I\subset\Lambda\) an ideal. Derived \(I\)-completeness means vanishing of the multiplication telescope for every element of \(I\). The Noetherian completion formula is

\[
C_I(K)=R\varprojlim_n
\bigl(K\otimes_\Lambda^{\mathbf L}\underline{\Lambda/I^n}\bigr).
\tag{6.1}
\]

It is left adjoint to inclusion of complete objects [Stacks, Tag 099L]. The following argument proves this formula for every Noetherian ideal.

### Completion for a Noetherian ideal

Here is the algebra behind (6.1), including the case where the quotient rings have infinite projective dimension. We use Artin–Rees in its finite-module form: if \(A\) is Noetherian, \(J\subset A\), and \(N\subset M\) are finite modules, then

\[
N\cap J^{n+c}M\subset J^nN
\qquad(n\geq0)
\tag{6.1a}
\]

for some \(c\). To recall its proof, the Rees ring \(A[Jt]\) is generated by finitely many degree-one elements over \(A\), hence is Noetherian by the Hilbert basis theorem. The Rees module \(\bigoplus_{n\geq0}J^nM\,t^n\) is finite over it. Its graded submodule \(\bigoplus_{n\geq0}(N\cap J^nM)t^n\) has finitely many homogeneous generators. If their degrees are at most \(c\), its degree \(n+c\) lies in \(J^nN\), proving (6.1a). In particular, taking quotients by \(J^n\) is exact as a functor from finite modules to pro-modules: its possible left-hand kernel disappears after passing to a sufficiently late level.

Let \(I=(x_1,\ldots,x_r)\subset\Lambda\). For one generator put

\[
T_x=[\Lambda\longrightarrow\Lambda[1/x]]
\quad\text{in degrees }0,1,
\qquad C_x(K)=R\mathcal Hom_\Lambda(T_x,K).
\]

All coefficient complexes in this paragraph are pulled back to the pro-étale site when used with sheaves. A free telescope resolution of \(\Lambda[1/x]\) uses countable sums of copies of \(\Lambda\); its Hom complex uses products. Thus the formulas make sense internally in the sheaf derived category, without treating an ordinary inverse limit as exact.

The triangle for \(T_x\) gives

\[
R\mathcal Hom_\Lambda(\Lambda[1/x],K)
\longrightarrow K\longrightarrow C_x(K).
\tag{6.1b}
\]

The last object is derived \(x\)-complete: applying
\(R\mathcal Hom_\Lambda(\Lambda[1/x],-)\) gives zero because
\(\Lambda[1/x]\otimes_\Lambda^LT_x=0\).
The first object has invertible multiplication by \(x\). A map from an object on which \(x\) is invertible to a derived \(x\)-complete object \(N\) is zero in every degree. Indeed, extension and restriction of scalars identify its derived Hom into \(N\) with derived Hom into \(R\mathcal Hom_\Lambda(\Lambda[1/x],N)=0\). Therefore (6.1b) identifies maps from \(C_x(K)\) to \(N\) with maps from \(K\) to \(N\). This proves the completion adjunction, rather than merely its effect on modules.

The functors \(C_{x_i}\) commute, by the Hom–tensor adjunction. Their composite is left adjoint to the objects complete for every \(x_i\), hence is \(C_I\). Equivalently it is
\(R\mathcal Hom_\Lambda(\bigotimes_i^LT_{x_i},K)\).
Writing \(T_x\) as the filtered colimit of
\([\Lambda\xrightarrow{x^n}\Lambda]\) in degrees \(0,1\), with identity transitions in degree zero and multiplication by \(x\) in degree one, gives

\[
C_I(K)=R\varprojlim_n(K\otimes_\Lambda^L Q_n),
\quad Q_n=\bigotimes_{i=1}^r
[\Lambda\xrightarrow{x_i^n}\Lambda]
\quad\text{in degrees }-r,\ldots,0.
\tag{6.1c}
\]

The sign in the dual two-term differential is removed by changing the sign of its degree-minus-one basis. The diagonal in the multiple index is cofinal, so (6.1c) uses one countable derived limit.

It remains to replace these Koszul complexes by quotient modules. Introduce
\(A=\Lambda[t_1,\ldots,t_r]\), mapping \(t_i\) to \(x_i\).
The \(A\)-module \(\Lambda=A/(t_i-x_i)_i\) is finite and has the finite free Koszul resolution for the regular sequence \(t_i-x_i\). Regularity follows successively by eliminating one polynomial variable; it does not require that the \(x_i\) be nonzerodivisors in \(\Lambda\). For \(J=(t_1,\ldots,t_r)\), (6.1a) shows that reduction of this resolution by \(J^n\) has pro-zero negative cohomology and degree-zero pro-cohomology \(\{\Lambda/I^n\}\). One way to see this explicitly is to apply exactness of the finite-module pro-quotient functor to its cycles and boundaries. The ideals \((t_1^n,\ldots,t_r^n)\) are cofinal with the \(J^n\), because

\[
J^{r(n-1)+1}\subset(t_1^n,\ldots,t_r^n)\subset J^n.
\]

Consequently the augmentation \(Q_n\to\Lambda/(x_1^n,\ldots,x_r^n)\) is a pro-isomorphism in the derived category. We justify the passage from pro-cohomology to pro-complexes, since it must precede tensoring with an arbitrary \(K\). For objects supported in a common interval \([a,b]\), a composite of \(b-a+1\) cohomologically zero maps is zero. Indeed, if \(f:E\to F\) is zero on cohomology, the composite
\[
\tau_{\leq q}E\longrightarrow\tau_{\leq q}F
\longrightarrow H^q(F)[-q]
\]
is zero. Its restriction to \(\tau_{\leq q-1}E\) is zero by the truncation orthogonality, so it factors through \(H^q(E)[-q]\); that map is zero by the hypothesis on \(f\). Exact Hom for the target truncation triangle therefore factors the first map through \(\tau_{\leq q-1}F\). Repeat this argument for successive maps, starting at \(q=b\). After \(b-a+1\) steps it factors through \(\tau_{\leq a-1}F=0\).

The augmentation cones have one fixed finite degree range and pro-zero cohomology by Artin–Rees. At a chosen target index, advance the source far enough to kill all their finitely many cohomology maps simultaneously. Repeat that choice as many times as the length of the common range. The resulting cone transition is zero by the preceding factorization. Thus the cone tower is pro-zero as a tower of derived objects, proving the asserted pro-isomorphism. For a map between two towers supported in \([a,b]\), its cones are supported in \([a-1,b]\), so \(b-a+2\) such transitions suffice. This argument does not assume exactness of products; that property is used in the next limit step.

Tensoring this pro-isomorphism with any \(K\) preserves its eventual zero maps. A pro-zero tower has zero derived limit on this site: its cohomology towers have zero ordinary limit and zero \(\varprojlim{}^1\), and the product description of a countable derived limit gives the Milnor sequences. Finally, \((x_i^n)_i\) and \(I^n\) are cofinal by the same displayed inclusions. Formula (6.1c) therefore becomes exactly (6.1). This proves the Noetherian completion formula and its adjunction for arbitrary complexes; neither a finite projective dimension of \(\Lambda/I^n\) nor a lower bound on \(K\) entered the proof.

For a morphism of schemes \(g:Y'\to Y\), write

\[
Lg_{\mathrm{comp}}^*K=C_I(Lg^*K).
\]

Here \(Lg^*=g^{-1}\) for constant coefficient rings; the notation also records the derived coefficient formalism. Completion supplies the left adjoint to \(Rg_*\) on the complete categories. Derived direct image preserves completeness: it commutes with the derived limit of every multiplication telescope, taking a vanishing telescope for \(K\) to a vanishing one for \(Rg_*K\). Also, since a derived right adjoint preserves derived limits,

\[
Rf_*K=R\varprojlim_n Rf_*K_n,\qquad
K_n=K\otimes_\Lambda^{\mathbf L}\underline{\Lambda/I^n},
\tag{6.2}
\]

when \(K\) is complete.

**Theorem 6.1 (proper base change).** Let \(f:X\to Y\) be proper, let \(g:Y'\to Y\) be arbitrary, and set \(X'=X\times_YY'\), with maps \(f':X'\to Y'\) and \(g':X'\to X\). Let \(\Lambda\) and \(I\) be as above, with \(\Lambda/I\) a torsion abelian group. Suppose \(K\in D(X_{\mathrm{pro\acute et}},\Lambda)\) satisfies:

1. \(K\) is derived \(I\)-complete.
2. For every \(n\), \(K_n\) is bounded below and its cohomology sheaves come from \(X_{\mathrm{\acute et}}\).
3. For every \(n\), \(\Lambda/I^n\) is perfect as a \(\Lambda\)-module.

Then the natural map

\[
Lg_{\mathrm{comp}}^*Rf_*K
\longrightarrow Rf'_*L(g')_{\mathrm{comp}}^*K
\tag{6.3}
\]

is an isomorphism. No Noetherian hypothesis on the schemes, constructibility condition on \(K\), or invertibility of the torsion primes on the schemes is required in this statement.

**Proof.** The map comes from adjunction. Pull back the counit \(Lf^*Rf_*K\to K\) along \(g'\), use the cartesian square to replace \(L(g')^*Lf^*\) by \(L(f')^*Lg^*\), and complete. Adjunction with \(Rf'_*\) gives (6.3).

Put \(A_n=\Lambda/I^n\). Each \(A_n\) is a bounded complex of finite projective \(\Lambda\)-modules in the derived category. Therefore the projection formula

\[
(Rf_*K)\otimes_\Lambda^{\mathbf L}A_n
\simeq Rf_*(K\otimes_\Lambda^{\mathbf L}A_n)
\tag{6.4}
\]

holds without an extra Tor bound on \(K\). To verify it, first take \(A_n\) finite free: it says that \(Rf_*\) commutes with finite sums. It then holds for finite projectives by taking direct summands, and for bounded complexes of them by successive cones. This proves (6.4) under precisely hypothesis 3.

Unwinding (6.1), using pullback's compatibility with tensor products, and then (6.4), the left side of (6.3) becomes

\[
\begin{aligned}
Lg_{\mathrm{comp}}^*Rf_*K
&=R\varprojlim_n
\bigl(Lg^*Rf_*K\otimes_\Lambda^{\mathbf L}A_n\bigr)\\
&=R\varprojlim_n Lg^*Rf_*K_n.
\end{aligned}
\tag{6.5}
\]

The right side becomes

\[
\begin{aligned}
Rf'_*L(g')_{\mathrm{comp}}^*K
&=Rf'_*R\varprojlim_n L(g')^*K_n\\
&=R\varprojlim_n Rf'_*L(g')^*K_n.
\end{aligned}
\tag{6.6}
\]

For the last equality use preservation of derived limits by \(Rf'_*\). No interchange of an ordinary inverse image with an inverse limit has been assumed.

Hypothesis 2 and the derived equivalence following Theorem 3.3 give \(K_n=\nu_X^{-1}L_n\) for a bounded-below étale \(A_n\)-complex \(L_n\). Its cohomology is torsion: some positive integer \(N\) kills \(1\) in the torsion ring \(\Lambda/I\), so \(N\in I\) and \(N^n\) kills \(\Lambda/I^n\) and its modules. Proper \(f\) is quasi-compact and quasi-separated, so (3.4) and pullback compatibility identify the level-\(n\) map between (6.5) and (6.6) with the pullback by \(\nu_{Y'}^{-1}\) of

\[
g_{\mathrm{\acute et}}^{-1}Rf_{\mathrm{\acute et},*}L_n
\longrightarrow Rf'_{\mathrm{\acute et},*}
(g')_{\mathrm{\acute et}}^{-1}L_n.
\tag{6.7}
\]

Torsion étale proper base change [Stacks, Tag 095T] makes (6.7) an isomorphism for a torsion sheaf. It also does so for a bounded-below torsion complex: its cohomology spectral sequence has only finitely many terms on any fixed total-degree diagonal, and the maps on all those terms are the sheaf base-change isomorphisms. Thus the complex map is an isomorphism. Taking the derived limit of these natural levelwise isomorphisms proves (6.3). ∎

This is the statement of [Stacks, Tag 09C9], including its perfect-quotient condition. For \(\Lambda=O\), \(I=(\ell)\), condition 3 is automatic from the two-term free resolution of \(O_n\). Proposition 5.2 verifies condition 2 for constructible adic complexes on quasi-compact schemes. The theorem therefore applies to the adic coefficients used in this course, including complexes with torsion. We now prove the broader constructible-coefficient theorem, which removes condition 3.

### Constructible coefficients without perfect quotient rings

The perfectness requirement in Theorem 6.1 concerns the coefficient ring, rather than the geometry. It can be removed for constructible complexes. Let \((\Lambda,\mathfrak m)\) be a complete Noetherian local ring with finite residue field \(\kappa\), of characteristic \(\ell\). Write \(\widehat\Lambda_X=\varprojlim\underline{\Lambda/\mathfrak m^n}\). Define \(D_{\mathrm{cons}}(X,\widehat\Lambda)\) by derived \(\mathfrak m\)-completeness and the requirement that
\(K_1=K\otimes^L_{\widehat\Lambda}\kappa\) comes from a constructible finite-Tor étale complex. This is the definition of §5 with a more general coefficient ring.

On a quasi-compact scheme, choose one Tor interval \([a,b]\) for \(K_1\). Filtering an arbitrary \(\Lambda/\mathfrak m^n\)-module by powers of \(\mathfrak m\), and using associativity of derived tensor product on the successive \(\kappa\)-module layers, proves that every \(K_n\) has Tor amplitude in \([a,b]\). The coefficient filtration itself has finite-dimensional layers over \(\kappa\); its triangles prove that the \(K_n\) are bounded constructible étale complexes. Completion and the surjective maps in top degree then give \(K\in D^{[a,b]}\), as in Proposition 5.2. These arguments use the Noetherian and quasi-compact hypotheses, and do not assert that every bounded complex of finite \(\Lambda\)-modules is constructible in this finite-Tor sense.

We need a projection formula for the finite modules \(\Lambda/\mathfrak m^n\), which may be nonperfect. The next lemma provides it with a uniform error estimate.

**Lemma 6.2.** Let \(f:X\to Y\) be a map of quasi-compact quasi-separated schemes. Suppose derived direct image on étale \(\kappa\)-sheaves has cohomological dimension at most \(d\). If \(K\in D_{\mathrm{cons}}(X,\widehat\Lambda)\) and \(M\) is a finite \(\Lambda\)-module, then

\[
Rf_*K\widehat\otimes_\Lambda M
\xrightarrow{\sim} Rf_*(K\widehat\otimes_\Lambda M),
\qquad
(Rf_*K)\otimes_\Lambda^L\Lambda/\mathfrak m^n
\xrightarrow{\sim}Rf_*K_n.
\tag{6.8}
\]

Here the hat means derived completion after tensor product. The last tensor product is already complete because its coefficients are killed by a power of \(\mathfrak m\).

**Proof.** Choose a finite-free resolution of \(M\), bounded above, by successively resolving its finite kernels. For every \(s\) retain finitely many terms to obtain a perfect complex \(P_s\to M\) whose homotopy fibre \(L_s\) lies in \(D^{\leq-s}(\Lambda)\). Such a complex need not be a finite resolution of \(M\).

For a coefficient complex \(L\in D^{\leq c}(\Lambda)\), the reductions of the completed tensor product are

\[
(K\widehat\otimes_\Lambda L)_n
\simeq K_n\otimes^L_{\Lambda/\mathfrak m^n}
(L\otimes^L_\Lambda\Lambda/\mathfrak m^n).
\]

The Tor bound puts these in \(D^{\leq b+c}\). The \(\mathfrak m\)-filtration extends the étale cohomological-dimension bound from \(\kappa\)-modules to \(\Lambda/\mathfrak m^n\)-modules, with the same \(d\). Some derived coefficient tensors here can be unbounded below; the bounded-below comparison theorem must not be applied directly to them. Instead write each reduction as the derived limit of its lower truncations. Exact products from §2 prove this left completeness: in any fixed cohomological degree the truncation tower is eventually constant, so the Milnor sequence identifies its limit with that cohomology sheaf. Each lower truncation has classical cohomology and belongs to the bounded-below comparison category of §3. Its direct image is bounded above by \(b+c+d\).

Direct image commutes with the limits over both the coefficient index and the truncation index. Combine them before estimating: the diagonal in \(\mathbb N\times\mathbb N\) is cofinal for this inverse limit, so there is only one countable derived-limit bound. It gives

\[
Rf_*(K\widehat\otimes_\Lambda L)
=R\varprojlim_n Rf_* (K\widehat\otimes_\Lambda L)_n
\in D^{\leq b+c+d+1}.
\tag{6.9}
\]

The extra \(1\) is the bound for the countable derived limit. Likewise \(Rf_*K\in D^{\leq b+d+1}\), so right exactness of derived tensor product and one further derived-limit bound give
\(Rf_*K\widehat\otimes L\in D^{\leq b+c+d+2}\).
Direct image is complete because it commutes with the multiplication telescopes used above.

The projection map is an isomorphism for \(P_s\): this is the finite-projective and finite-cone argument of (6.4), and tensoring with a perfect coefficient complex preserves completeness. In the natural square comparing \(P_s\) with \(M\), the homotopy fibres of both horizontal maps vanish above \(b+d+2-s\), by (6.9) and the preceding bound with \(L=L_s\). Thus the projection map for \(M\) is an isomorphism in each fixed degree, by choosing \(s\) large enough. This proves the first formula. Set \(M=\Lambda/\mathfrak m^n\) to get the second. \(\square\)

**Theorem 6.3 (constructible proper base change).** Let \(f:X\to Y\) be proper and finitely presented between quasi-compact quasi-separated schemes, and let \(g:Y'\to Y\) be any map with \(Y'\) quasi-compact and quasi-separated. For \(K\in D_{\mathrm{cons}}(X,\widehat\Lambda)\), (6.3) is an isomorphism. Both sides are constructible. No perfectness of \(\Lambda/\mathfrak m^n\) is required, and \(\ell\) need not be invertible on the schemes.

**Proof.** Torsion proper direct image for a finitely presented proper map has a finite cohomological-dimension bound on \(\kappa\)-sheaves and preserves constructible complexes. These are the torsion proper-base-change and finiteness prerequisites, with exactly the stated geometric hypotheses. Apply Lemma 6.2 to \(f\) and its proper base change \(f'\). It identifies the reductions of \(Rf_*K\) with \(Rf_*K_n\), naturally in \(n\). The latter are constructible, so the first reduction shows that \(Rf_*K\) is constructible. Completed pullback also preserves constructibility: its reduction is ordinary pullback of \(K_n\).

Using (6.8) in place of (6.4), formulas (6.5)–(6.7) now apply word for word. Each level is torsion proper base change and hence an isomorphism. Their derived limit is (6.3). Naturality of the finite-free approximation ensures that this is the adjunction base-change map, and not a separately chosen isomorphism. \(\square\)

For instance take \(\Lambda=\mathbb Z_\ell[\epsilon]/(\epsilon^2)\), with maximal ideal \((\ell,\epsilon)\). Its residue field is not perfect as a \(\Lambda\)-module. A free resolution of \(\Lambda/(\epsilon)=\mathbb Z_\ell\) has every positive differential multiplication by \(\epsilon\); taking the cone of multiplication by \(\ell\) resolves the residue field. After tensoring with \(\mathbb F_\ell\), every differential is zero, leaving nonzero Tor in arbitrarily high degrees. Nevertheless the constant complex \(\widehat\Lambda\) is constructible and Theorem 6.3 applies to its proper direct images. This is a real extension of Theorem 6.1's coefficient range.

The comparison is with Bhatt–Scholze, §§6.5–6.7, especially Lemmas 6.5.11 and 6.7.5. Properness permits the absence of an invertibility condition here. For ordinary direct image along a general finitely presented map, their finiteness theorem instead assumes a quasi-excellent base with \(\ell\) invertible. Compact-support direct image is built by an open immersion followed by a proper finitely presented map; the same reduction argument gives arbitrary base change for it. This keeps the distinct proper, smooth, and compact-support base-change statements separate.

These categories accommodate operations on a single complex rather than separately normalized cohomology systems. Completed pullback and derived direct image have the adjunction just proved. Tensor product is followed by completion; its reductions are the finite-coefficient derived tensor products. For separated finite-type morphisms in the usual torsion finiteness setting, \(Rf_!\) is similarly obtained from the coherent systems \(Rf_!K_n\), with scalar extension supplying their compatibility. Proper morphisms have \(Rf_!=Rf_*\), where Theorem 6.1 supplies base change. Verdier duality and \(f^!\) need their torsion duality prerequisites and finiteness hypotheses. Defining this category alone is not a proof of those further theorems.

## 7. Fields, twists and continuous representations

**The field site.** Put \(G=\operatorname{Gal}(k^{\mathrm{sep}}/k)\). Finite étale \(k\)-schemes correspond to finite continuous \(G\)-sets. Taking affine inverse limits adds profinite continuous \(G\)-sets. Over \(k^{\mathrm{sep}}\) these include the profinite disjoint unions of points from §4. Finite jointly surjective families give the covers on this affine basis. Descent with respect to \(\operatorname{Spec}(k^{\mathrm{sep}})\to\operatorname{Spec}(k)\) adds the \(G\)-action. This is the profinite-space description behind the site's resemblance to condensed sheaf theory. It is a description of a generating affine basis and its descent, rather than an assertion that every sheaf is a discrete \(G\)-module.

**Lisse coefficients.** Let \(X\) be connected and Noetherian and let a lisse adic sheaf correspond to a free finite \(O\)-module \(M\) with continuous \(\pi_1(X)\)-action. On an affine open, take the compatible tower of finite étale covers corresponding to the kernels of the representations on \(M/\ell^nM\). Its affine inverse limit is an ind-étale cover; every level becomes constant there, with compatible transitions. Thus the sheaf of Proposition 4.2 becomes \(\widehat O^{\,r}\) on that cover, where \(r=\operatorname{rank}M\). After inverting \(\ell\), the lisse rational sheaf becomes locally free of rank \(r\) over \(\widehat E\). A continuous representation with torsion coefficients yields the corresponding completed finite-module sheaf, rather than a free sheaf.

### Integral lattices are a local condition

For a finite extension \(E/\mathbb Q_\ell\), put
\(\widehat E=\widehat O_E[1/\ell]\) on the pro-étale site. An \(E\)-local system means a sheaf locally isomorphic to \(\widehat E^{\,r}\) in that topology. The classical category of Lesson 1 starts instead with a global strict integral system and then inverts \(\ell\). The distinction matters on a singular scheme.

We first record the descent fact needed to compare them. Call a pro-étale sheaf *classical* if it is pulled back from the étale site.

**Lemma 7.1.** Being classical is local for the pro-étale topology. In particular a sheaf pro-étale locally isomorphic to a constant discrete sheaf is classical. This assertion alone does not say that an infinite discrete sheaf becomes constant on an étale cover.

**Proof.** By Proposition 3.1 and (3.2), a sheaf \(F\) is classical precisely when, on every affine ind-étale presentation \(V=\varprojlim V_i\),
\[
F(V)=\varinjlim_i F(V_i).
\tag{7.2}
\]
Indeed (7.2) identifies the counit \(\nu^{-1}\nu_*F\to F\) on a generating basis. Locally on affine \(X\), refine a classicalizing cover to a faithfully flat ind-étale affine cover \(W\to X\). Such a refinement is allowed by the basis and cover constructions of §§1–2. Descent writes \(F(V)\) as the equalizer of
\[
F(V\times_XW)\rightrightarrows
F(V\times_XW\times_XW).
\]
Apply the analogous equalizer to each \(V_i\). Classicality over \(W\) identifies both entries of the first equalizer with the filtered colimits of those in the second: after base change they are ind-étale presentations over \(W\). Filtered colimits of sets commute with finite limits. Thus the equalizers agree, proving (7.2). The statement for a locally constant discrete sheaf follows because the constant discrete sheaf is classical on each trivializing piece. \(\square\)

**Proposition 7.2.** On a quasi-compact quasi-separated scheme \(X\), rationalization is fully faithful from finite-rank integral local systems with their morphisms tensored by \(E\) to \(E\)-local systems. Every \(E\)-local system has an integral lattice on an étale covering. It need not have one on \(X\).

**Proof of the first two assertions.** Strict torsion-free systems and integral local systems agree by Proposition 4.2 and the tower of finite étale trivializations used at the start of this section. For integral local systems \(M,N\), a rational map is, on an affine pro-étale cover trivializing them, a matrix of continuous \(E\)-valued functions on the profinite component space. A continuous function on a compact space has bounded denominator. Quasi-compactness gives finitely many such affine pieces, so one power of a uniformizer clears the denominators of every matrix entry. The resulting integral maps glue because their rationalizations agree and \(N\) has no torsion. Integral maps rationalize injectively for the same reason. This proves full faithfulness, including the uniform denominator needed for global Hom.

For a fixed rank-\(r\) local system \(L\), form the sheaf \(\mathscr L\) of integral lattices contained in \(L\). Over a trivializing cover it is the constant discrete sheaf
\[
S=\mathrm{GL}_r(E)/\mathrm{GL}_r(O_E).
\]
To verify this description, trivialize a proposed lattice too. Its basis gives a continuous invertible matrix. The quotient map to \(S\) is locally constant, since \(\mathrm{GL}_r(O_E)\) is open. Its coset determines the lattice, and every coset gives one. This is a statement of sheaves and allows the coset to vary on clopen pieces; it does not require one coset on a disconnected object.

Lemma 7.1 makes \(\mathscr L\) classical. It is locally inhabited in the pro-étale topology. Its corresponding étale sheaf is therefore locally inhabited in the étale topology: inverse image is fully faithful, and reflects the assertion that the image of \(\mathscr L\to1\) is all of \(1\). Thus an étale cover supplies a section, namely a lattice. \(\square\)

Here is a complete example proving the last assertion. Let \(k\) be algebraically closed and let \(X\) be the rational nodal curve obtained from \(\mathbb P^1_k\) by identifying \(0\) and \(\infty\). Form \(Y\) from copies \(P_i=\mathbb P^1_k\), \(i\in\mathbb Z\), joining \(\infty\in P_i\) to \(0\in P_{i+1}\). The map
\[
p:Y\longrightarrow X
\]
uses the normalization map on each \(P_i\). This is an étale covering with a shift action of \(\mathbb Z\), and
\[
Y\times_XY\simeq\coprod_{j\in\mathbb Z}Y,
\tag{7.3}
\]
where the \(j\)-th component compares a point with its shift by \(j\).

For the geometric construction, finite portions of the chain are schemes obtained by identifying pairs of \(k\)-rational points. Near a join their affine coordinate ring is the fibre product of the two branch rings over \(k\); functions are exactly pairs having the same value at the joining point. Removing the two outer joining points makes each finite portion open in the next one, and their union constructs \(Y\). Away from a join the map is the normalization isomorphism. At a join its completed local ring maps isomorphically from the nodal completed local ring of \(X\), namely \(k[[u,v]]/(uv)\), with one branch coming from each adjacent component. These local finite-presentation maps are étale: faithful flatness of local completion gives flatness, and the finite module of relative differentials has zero completion and hence is zero. Thus \(p\) is étale everywhere and is surjective. The shifts act freely and transitively on every geometric fibre. The comparison in (7.3) is consequently an isomorphism: it is a map between étale \(Y\)-schemes and is a bijection on every geometric fibre. A few adjacent components with their outer endpoints removed already give a quasi-compact open whose image covers \(X\), so this cover also satisfies the pro-étale covering condition.

Descend the trivial sheaf \(\widehat E_Y\) along (7.3), using multiplication by \(\ell^j\) on its \(j\)-th component. The identities \(\ell^{i+j}=\ell^i\ell^j\) are exactly the cocycle condition. Sheaf descent produces a rank-one \(E\)-local system \(L\) on \(X\).

Suppose \(M\subset L\) were an integral lattice. Pull it back to \(Y\), where \(L\) is trivial. Rank-one lattices in \(E\) are \(\varpi^aO_E\), indexed by \(a\in\mathbb Z\). The preceding description of the lattice sheaf makes \(p^*M\) a section of the constant discrete \(\mathbb Z\)-sheaf on \(Y\). By Proposition 3.1 its global sections are the ordinary locally constant functions on the connected scheme \(Y\), hence this section has one constant value \(a\). But the shift descent multiplies the lattice by \(\ell\), changing \(a\) by the positive ramification index \(v_\varpi(\ell)\). A constant value cannot satisfy that descent condition. This contradiction proves that \(L\) has no global lattice.

In particular \(L\) is absent from the global rationalization category of Lesson 1. A continuous representation of a profinite group has compact image and therefore a stable lattice, by that lesson's lattice argument. The loop with multiplier \(\ell\) cannot be represented that way. Bhatt–Scholze's refined fundamental group addresses this larger category; the example above proves the failure of the profinite classification without needing that classification theorem as an input. On the smooth curves used in the later trace and monodromy arguments the classical lattice category remains the stated coefficient category.

**Kummer completion.** Suppose \(\ell\neq\operatorname{char}k\). The transitions on \(\mu_{\ell^n}\) are raising to the \(\ell\)-th power. Set

\[
\widehat O(1)=\varprojlim_n\nu^{-1}\mu_{\ell^n}.
\]

The Kummer sequence and Hilbert 90 give

\[
H^1(k_{\mathrm{\acute et}},\mu_{\ell^n})
=k^\times/(k^\times)^{\ell^n}.
\]

Naturality of the Kummer sequences identifies the transitions on these groups with the quotient maps. To compute cohomology of the inverse limit, (5.1) also asks about

\[
\varprojlim{}^1\mu_{\ell^n}(k).
\]

Every \(\mu_{\ell^n}(k)\) is finite, so the tower is Mittag–Leffler even if its transitions on rational roots of unity are not onto. Its \(\varprojlim{}^1\) is zero. Consequently

\[
H^1(k_{\mathrm{pro\acute et}},\widehat O(1))
=\varprojlim_n k^\times/(k^\times)^{\ell^n}.
\tag{7.1}
\]

This is the group-theoretic \(\ell\)-adic completion of \(k^\times\), not a claim about completing the field's topology.

**Finite fields.** For constant coefficients and \(\ell\neq\operatorname{char}\mathbb F_q\), the absolute Galois group is \(\widehat{\mathbb Z}\), generated topologically by arithmetic Frobenius. Its finite-coefficient cohomology is

\[
H^0(\mathbb F_q,O_n)=O_n,\qquad
H^1(\mathbb F_q,O_n)=\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbb Z},O_n)=O_n,
\qquad H^i=0\ (i>1).
\]

The transition maps in degrees zero and one are reductions. Their limits are both \(O\), with zero \(\varprojlim{}^1\) terms. Hence \(H^0(\mathbb F_q,\widehat O)=O\), \(H^1(\mathbb F_q,\widehat O)=O\), and higher cohomology vanishes. This nonzero \(H^1\) is consistent with weakly contractible covers: the base object itself is not weakly contractible.

For the twist, \(\mathbb F_q^\times\) is cyclic of order \(q-1\), so (7.1) is its \(\ell\)-primary subgroup. Equivalently, arithmetic Frobenius acts on \(O(1)\) by \(q\), and the degree-one group is \(O/(q-1)O\). These constant and twisted calculations involve different Galois actions.

### Geometric coverings and component spaces

Write \(\mathrm{Loc}_X\) for pro-étale locally constant sheaves of sets. A **geometric covering** is an étale scheme \(Z\to X\) satisfying existence and uniqueness in the valuative criterion, for every valuation ring, without a quasi-compactness requirement. Write \(\mathrm{Cov}_X\) for these schemes. A sheaf is **locally weakly constant** if on a pro-étale cover by qcqs schemes \(Y\), it is pulled back from an ordinary sheaf on the profinite space \(\pi_0(Y)\); write \(\mathrm{wLoc}_X\). These definitions allow infinite fibres.

**Lemma 7.5a (sheaves on a component space).** An ordinary sheaf of sets on a profinite space \(P\) is a filtered colimit of finite locally constant sheaves. If \(Y\) is affine and w-local, with strictly henselian local rings at its closed points, pullback

\[
\pi^*:\mathrm{Sh}(\pi_0Y)\longrightarrow\mathrm{Sh}(Y_{\mathrm{\acute et}})
\]

is fully faithful and preserves colimits and finite limits. Its essential image consists precisely of sheaves whose restriction to every connected component of \(Y\) is constant.

**Proof.** Finite locally constant sheaves are finite disjoint unions of constant finite sheaves supported on clopen subsets, after a finite clopen partition. Maps and finite diagrams between them become maps and finite diagrams of finite sets on a common finite partition. Their finite colimits therefore remain finite locally constant. The category of maps from such sheaves to a fixed sheaf \(G\) is filtered: coproducts supply a common successor, and coequalizers equalize parallel arrows. Its colimit maps onto every germ of \(G\), since a germ extends over a clopen neighbourhood. If two germs in that colimit agree, shrink to a clopen neighbourhood on which their sections agree and coequalize the corresponding two maps from the sheaf supported on that neighbourhood. Thus the colimit is \(G\).

Clopen subsets of \(P=\pi_0Y\) correspond to idempotent decompositions of \(Y\). This defines pullback first for finite locally constant sheaves and then for their filtered colimits; equivalently it is inverse image along the component map. For a classical étale sheaf \(H\) on \(Y\), define \(\pi_*H\) on a clopen \(C\subset P\) by \(H(Y_C)\). The connected component at a closed point \(m\) is \(Y_m=\operatorname{Spec}R_m\), the inverse limit of its clopen neighbourhoods, as proved in Lemma 1.1b. Étale continuity in degree zero gives

\[
(\pi_*H)_m=H(Y_m).
\]

For a strictly henselian local scheme, sections of any étale sheaf equal its stalk at the closed geometric point: a representative étale neighbourhood of that point has a section, and equality of two sections near the closed point is equality everywhere on the local scheme. In particular \(H(Y_m)\) is that closed stalk. If \(H\) is constant on \(Y_m\), these sections map bijectively to every geometric stalk in the component. The counit \(\pi^*\pi_*H\to H\) is consequently an isomorphism on all geometric stalks. Conversely a pullback from \(P\) is constant on each component, and \(\pi_*\pi^*G\to G\) is a stalkwise isomorphism. This proves the essential-image description and full faithfulness. Inverse image preserves colimits and finite limits; the same operations within its image are detected on the component stalks. \(\square\)

**Lemma 7.5b (henselian splitting).** Over a strictly henselian local scheme, every geometric covering is a disjoint union of copies of the base. Over a henselian local scheme, it is a disjoint union of connected finite étale schemes lifting the connected components of its closed fibre.

**Proof.** First suppose the base is strictly henselian. Each point of the closed fibre has a section through it: choose a finitely presented étale neighbourhood in the covering and apply the section criterion for a strictly henselian local ring. Each section is an open immersion, since a section of an étale morphism is an étale monomorphism.

Every point \(z\) of the covering specializes to a point of the closed fibre. Indeed take the closure of its image in the base, and a valuation ring dominating its local ring at the closed point, with fraction field extended to contain \(\kappa(z)\). The valuation domination theorem, [AG-MO-04, Theorem 2.1](course:AG-MO/AG-MO-04), supplies this ring. Existence in the valuative criterion extends the generic lift through \(z\); its closed point is the required specialization. An open section containing that specialization contains \(z\). Thus the sections cover.

Two sections with different closed-fibre points are disjoint. If they met over a point \(p\), choose a valuation ring on an algebraic extension of \(\kappa(p)\) dominating the closure of \(p\) at the base's closed point. Their pullbacks agree at its generic point. Uniqueness in the valuative criterion makes them agree at its closed point, a contradiction. We obtain the asserted disjoint union. This argument does not assume quasi-compactness of the covering or use separatedness before proving the splitting.

For a henselian local base \(S\), its closed fibre is a disjoint union of spectra of finite separable residue extensions. Each such spectrum \(Z_i\) has a unique connected finite étale lift \(\widetilde Z_i\to S\), by [AG-CA-20, §§1–3](course:AG-CA/AG-CA-20). On the henselian local scheme \(\widetilde Z_i\), its distinguished closed-fibre map to the covering lifts by the same étale section criterion. These maps give \(\coprod_i\widetilde Z_i\to Z\). After the faithfully flat strict henselization of \(S\), the preceding disjoint-section argument makes this map an isomorphism: it is bijective on closed-fibre sections. Isomorphisms descend faithfully flat, proving the result. \(\square\)

**Proposition 7.5c (all colimits and the weakly constant test).** A sheaf is locally weakly constant if and only if its restriction to every affine w-contractible object \(Y\) is classical and is pulled back from \(\pi_0(Y)\). This subcategory is closed under all small colimits and finite limits in pro-étale sheaves.

**Proof.** A locally weakly constant sheaf is classical by Lemma 7.1: on its defining cover, the component sheaf is a filtered colimit of finite locally constant classical sheaves, by Lemma 7.5a. Fix an affine w-contractible \(Y\). Each component \(Y_m\) is strictly henselian local and itself w-contractible, by Theorem 1.1f. Pull back a defining weakly constant cover to it. Refine to an affine cover and choose a piece meeting its closed point. Flatness makes that piece surjective over the local base; w-contractibility gives a section. The component map from the connected scheme \(Y_m\) into this covering piece's profinite component space is constant. Pulling the weakly constant sheaf back along that section therefore makes it constant on \(Y_m\). Lemma 7.5a now identifies the restriction to \(Y\) with a component-space pullback. The converse follows by choosing enough affine w-contractible covers, supplied by Theorem 1.1f.

For any family of such sheaves, use this test on the same arbitrary w-contractible \(Y\). Classical pullback from the étale site preserves colimits and finite limits, as does \(\pi^*\); Lemma 7.5a identifies the resulting component sheaf. The colimit or finite limit thus satisfies the test. Enough such \(Y\)'s prove the claim. No common trivialization of the entire family was assumed. \(\square\)

**Theorem 7.5d (geometric classification).** If \(X\) is locally topologically Noetherian, then

\[
\mathrm{Loc}_X=\mathrm{wLoc}_X=\mathrm{Cov}_X.
\tag{7.5}
\]

The equality of the last two categories holds on an arbitrary scheme if their represented objects are required to be quasi-separated. Under that convention all three categories agree whenever \(X\) locally has finitely many irreducible components.

**Proof.** A constant sheaf is pulled back from the component space, so \(\mathrm{Loc}_X\subset\mathrm{wLoc}_X\). By the classicality argument in Proposition 7.5c, a weakly constant sheaf is an ordinary étale sheaf. Such a sheaf is represented by an étale algebraic space: take the disjoint union of its étale section charts, with equality relation on their pairwise products. Equality of two sections is an open condition on an étale chart, so this relation is a scheme étale equivalence relation. The quotient theorem, [AG-AS-01, Theorem 2.2](course:AG-AS/AG-AS-01), constructs the algebraic space. Its small étale sheaf is the original sheaf, and Proposition 3.1 identifies their pro-étale pullbacks.

Locally on a defining weakly constant cover \(Y\), Lemma 7.5a presents it as a filtered colimit of finite étale \(Y\)-schemes. On the product of two finite-stage charts its diagonal is the increasing union of clopen equalizers at common later stages. Thus its diagonal is locally an increasing union of clopen immersions. It also satisfies the valuative criterion on \(Y\): a map from the connected scheme \(\operatorname{Spec}V\), for a valuation ring \(V\), has one image in \(\pi_0Y\); both its generic and special pullbacks of the component sheaf are the same constant set. Sections over \(\operatorname{Spec}V\) and its fraction field consequently agree.

We first explain quasi-separatedness in the Noetherian-topology case. Every quasi-compact separated étale scheme over a topologically Noetherian affine scheme is topologically Noetherian. To prove this, there are finitely many generic points. Over the zero-dimensional local ring at each generic point, henselian finite-algebra decomposition and scheme Zariski main make a quasi-compact separated étale chart finite. Finitely presented equations descend this finiteness to an open neighbourhood of that generic point. Remove the intersections of distinct irreducible components first, to obtain a finite disjoint union of such dense opens. Repeat on the closed complement. Noetherian induction terminates, giving a finite locally closed stratification over which the chart is finite étale. For a finite étale map, a descending sequence of closed subsets stabilizes: their geometric-fibre cardinality functions are upper semicontinuous, bounded by the degree, and decreasing. Each closed locus where cardinality is at least an integer stabilizes downstairs. There are finitely many such integers; equality of the cardinalities in a decreasing sequence forces equality of the subsets. A finite stratification then proves the assertion.

For an arbitrary étale scheme the conclusion is **locally** topologically Noetherian; it is globally so if it is quasi-compact. An infinite disjoint union of copies of a point shows why that distinction is necessary in the printed Lemma 6.6.10(3).

Choose affine étale section charts \(U_i\) over an affine open of \(X\). Every \(U_i\times_XU_j\) has Noetherian topology, so its open equality locus is quasi-compact. This says that the algebraic space's diagonal is quasi-compact. For the general assertion, quasi-separatedness supplies exactly that hypothesis instead. It remains quasi-compact after the weakly constant base change. Its increasing union of clopen equalizers is therefore already a finite such union on each chart, and hence clopen. Closed immersions descend faithfully flat, so the diagonal is closed. The algebraic space is separated and étale over \(X\); [AG-AS-02, Theorem B.2](course:AG-AS/AG-AS-02), now makes it a scheme. This uses the actual internal recognition proof, rather than treating an external tag as that proof.

The valuative criterion descends as well. Here is the relevant descent argument for separated étale morphisms. For a valuation ring \(V\) mapping to \(X\), choose a point over its closed point in a faithfully flat affine defining cover. Flat going down gives a generalization over the generic point. A valuation ring in an algebraic closure of its residue field, dominating its local ring at the chosen closed point, gives \(V\subset V'\), with \(V'\) dominating \(V\), and a map \(\operatorname{Spec}V'\) into the cover. It is faithfully flat over \(V\): torsion-free modules over a valuation ring are flat, and the local map is faithfully flat. The generic section extends over \(V'\) by the criterion already proved on the cover. On \(V'\otimes_VV'\) the two extensions agree generically. Their equality locus is open and closed, since the target is separated and étale. This tensor product is flat over \(V\), so its generic fibre is dense; an open-and-closed equality locus containing it is the whole scheme. Faithfully flat descent of sections gives the extension over \(V\). Uniqueness follows by the same density argument. We have proved \(\mathrm{wLoc}_X\subset\mathrm{Cov}_X\).

Conversely take a geometric covering and pull it back to an affine w-contractible \(Y\). On each strictly henselian component it is constant by Lemma 7.5b. Lemma 7.5a identifies its classical étale sheaf with a component-space pullback. Proposition 7.5c gives weak constancy. This proves \(\mathrm{Cov}_X=\mathrm{wLoc}_X\), with quasi-separatedness in the general convention. A locally constant sheaf is quasi-separated: on a trivializing affine cover its diagonal is the diagonal of a disjoint union of copies of the base, which is quasi-compact; quasi-compactness of a morphism is fpqc local on its target.

It remains to turn weak constancy into local constancy when the base has locally finitely many irreducible components. Work on an affine such neighbourhood, with generic points \(\eta_1,\ldots,\eta_d\), and choose an affine w-contractible cover \(Y\to X\). Write \(F|Y=\pi^*G\). Put \(X_\eta=\coprod_i\operatorname{Spec}\kappa(\eta_i)\) and choose an affine w-contractible cover \(Y'_\eta\to Y\times_XX_\eta\). The map

\[
q:\pi_0(Y'_\eta)\longrightarrow\pi_0(Y)
\]

is surjective. Indeed, for any component \(\operatorname{Spec}R_m\) of \(Y\), the flat local map from its base local ring has, by going down, a prime above some generic point of \(X\). That point lifts into \(Y'_\eta\). Since \(\pi_0Y\) is extremally disconnected, Theorem 1.1e supplies a continuous section of \(q\).

Over a field, every ordinary étale sheaf is a disjoint union of finite separable field covers: continuous orbits of its absolute Galois group are finite. Pull each finite orbit back to \(Y'_\eta\). It is a finite étale covering of constant rank on the clopen piece lying over that field. Its frame torsor is finite étale and surjective, and w-contractibility splits that torsor. Thus it is a constant finite set there. Choosing such trivializations for the set of orbits makes the entire pullback constant on each of the finitely many field pieces. By Lemma 7.5a, \(q^*G\) is locally constant on \(\pi_0(Y'_\eta)\). Pulling it back along the continuous section makes \(G\) locally constant. Consequently \(\pi^*G\), and then \(F\), is pro-étale locally constant. This proves both the Noetherian-topology and the stated more general equality. \(\square\)

### Completing the automorphism group

For a Hausdorff topological group \(G\), let \(G\text{-}\mathrm{Set}\) mean discrete sets with continuous \(G\)-actions, and let \(F_G\) forget the action. The group \(\operatorname{Aut}(F_G)\) has the topology of pointwise convergence on every such set. Finite conditions on the images of specified points give a basis; inverse conditions give the same topology. A group is **Noohi** when its natural map to this automorphism group is an isomorphism of topological groups.

**Lemma 7.6a (completeness of permutations).** For every set \(S\), its permutation group, with pointwise convergence, is complete for the two-sided uniformity.

**Proof.** For each finite \(E\subset S\), a two-sided Cauchy filter has a member on which both \(h(s)\) and \(h^{-1}(s)\) are constant for all \(s\in E\). Indeed, \(h^{-1}k\) fixing \(E\) makes the images equal, and \(hk^{-1}\) fixing \(E\) makes the inverse images equal. Filter intersections make these eventual values compatible as \(E\) increases. They define functions \(a,b:S\to S\). For a given \(s\), intersect the members specifying \(b(s)\) and \(a(b(s))\), and choose one permutation there. It gives \(a(b(s))=s\); the other composition is identical. Thus \(a\) is a permutation with inverse \(b\), and every finite condition on it belongs to the filter. The filter converges to \(a\). Products of these complete groups are complete, by taking coordinate limits; a closed subgroup is complete because those limits stay in it. \(\square\)

**Theorem 7.6 (reconstruction and completion).** Suppose the open subgroups form a neighborhood basis at 1 in \(G\). The natural map

\[
G\longrightarrow H=\operatorname{Aut}(F_G)
\]

is a dense embedding, and \(H\) is complete for its two-sided uniformity. It is therefore the two-sided completion of \(G\). Restriction of actions gives an equivalence \(H\text{-}\mathrm{Set}\simeq G\text{-}\mathrm{Set}\). In particular \(G\) is Noohi precisely when it is complete. Every Noohi group has a basis of open subgroups, so this gives a characterization of all Noohi groups.

**Proof.** Every transitive discrete continuous \(G\)-set is \(G/U\) for some open subgroup \(U\). Take one coset object for each open subgroup, a set of representatives. Compatible permutations of these objects determine a natural automorphism on every action: write it as its disjoint union of orbits and transport the permutations through orbit identifications. Independence of the identifications and naturality follow from compatibility with all equivariant maps between the coset objects. Conversely every natural automorphism has precisely these compatible permutations. Hence \(H\) is the closed subgroup of

\[
\prod_{U\subset G\ \mathrm{open}}\operatorname{Sym}(G/U)
\]

defined by \(h_V(f(x))=f(h_U(x))\), for all equivariant \(f:G/U\to G/V\) and all \(x\in G/U\). Each equation is closed, since evaluation lands in a discrete set. The lemma proves completeness. This also proves that \(H\)'s topology has an open-subgroup basis.

The map from \(G\) is injective: an element acting trivially fixes the identity coset for every \(U\), hence lies in their intersection, which is \(\{1\}\) by Hausdorffness. Its induced topology is the original topology. The stabilizer of an identity coset is \(U\), and other point stabilizers are its conjugates; finite intersections give exactly the required open conditions.

To prove density, fix \(h\in H\) and finitely many conditions \(g x_i=h x_i\) on points of discrete continuous actions. Form their tuple in the finite product of these actions. Its \(G\)-orbit is itself a discrete continuous \(G\)-set, included equivariantly in that product. Naturality preserves this orbit, and naturality of the projections says that the tuple's image is \((h x_i)_i\). It is therefore \((g x_i)_i\) for one \(g\in G\). If inverse conditions \(g^{-1}y_j=h^{-1}y_j\) are also specified, add the direct conditions \(g(h^{-1}y_j)=y_j\). The same argument satisfies them simultaneously. Thus every neighborhood of \(h\) meets \(G\).

A dense uniform embedding into a complete Hausdorff uniform group is its completion. Explicitly, every Cauchy filter on \(G\) has a unique limit in \(H\), and each point of \(H\) is the limit of the traces of its neighborhood filter. A uniformly continuous homomorphism into another complete Hausdorff uniform group extends by taking these limits; the Cauchy property makes the value independent of the filter. Continuity and the group law follow by approximating pairs of points from \(G\). This proves the completion assertion without an external completion-existence theorem. Completeness of \(G\) is equivalent to its image being closed in \(H\): a Cauchy filter converges within a complete subgroup, so an ambient limit belongs to that subgroup. Density then makes the image all of \(H\).

Each original action has a continuous \(H\)-action by evaluation of natural automorphisms. Conversely restrict an \(H\)-action to \(G\). A map between such sets is \(H\)-equivariant if it is \(G\)-equivariant: for each point, the required equality is closed in \(H\), and holds on the dense subgroup. The reconstructed action agrees with the original action by the same argument. This proves the asserted equivalence. Applying it once more identifies \(H\) with \(\operatorname{Aut}(F_H)\). Finally, any Noohi group's topology, through this isomorphism, has the open-subgroup basis of finite point stabilizers. \(\square\)

Discrete and profinite groups are Noohi: their Cauchy filters respectively are eventually singletons or have a compact cluster point, which the Cauchy property makes their limit. More generally every locally compact group with an open-subgroup basis is Noohi. Choose a neighborhood of 1 with compact closure. A Cauchy filter has a member inside a translate of that neighborhood, so its closed filter traces in the compact closure have a common point. For any prescribed neighborhood of that point, the Cauchy property and one filter member meeting a sufficiently small neighborhood put a later member wholly in the prescribed neighborhood. Thus the filter converges. In particular the finite-extension coefficient groups \(\mathrm{GL}_r(E)\) used in this course are Noohi: they are locally compact, and congruence subgroups of \(\mathrm{GL}_r(O_E)\) give an open-subgroup basis.

**A distinction in the source example.** For \(G=\operatorname{Sym}(S)\), a transitive action is a quotient of \(G/U_E\), where \(U_E\) fixes a finite subset pointwise. It need not be equal to \(G/U_E\), or embed in a power of \(S\). Nevertheless this proves that \(G\) is Noohi directly. A natural automorphism has its permutation \(h_S\) on \(S\), acts by that permutation on finite powers, hence on the orbit of an injection \(E\hookrightarrow S\), which is \(G/U_E\), and then on every equivariant quotient. It therefore acts as \(h_S\) on every transitive action and on every disjoint union of them.

For an infinite \(S\), the action on its unordered two-element subsets exhibits the distinction. Its stabilizer includes the interchange of the two elements and arbitrary permutations of their complement; it fixes no point of \(S\). An equivariant embedding into \(S^n\), with \(n>0\), would supply a tuple fixed by that stabilizer, which is impossible. The case \(n=0\) has one point and cannot receive that transitive action injectively. The action is instead the equivariant quotient of ordered distinct pairs. The printed v2 Example7.1.2, physical63, asserts the stronger embedding; the quotient argument corrects that step while preserving its Noohi conclusion. The product in Proposition7.1.5's naturality equalizer is over \(\operatorname{Sym}(G/U)\), not permutations of the subgroup \(U\) itself; the printed physical64 notation is corrected accordingly.

**Corollary 7.6b (permanence).** Products and closed subgroups of Noohi groups are Noohi. A Hausdorff topological group with an open Noohi subgroup is Noohi.

**Proof.** Products are complete by coordinate limits, and finite intersections of coordinate open-subgroup conditions give their open-subgroup basis. Closed subgroups inherit completeness and that basis. For an open Noohi subgroup, a two-sided Cauchy filter on the larger group is eventually contained in one coset of it; translation gives a Cauchy filter on the complete subgroup and thus a limit. Its open-subgroup basis is also a basis for the larger group. In each case Theorem 7.6 gives the conclusion. \(\square\)

### Algebraic coefficient fields

For an algebraic extension of \(\mathbb Q_\ell\), the topology used in the coefficient sheaf is the colimit topology of its finite subextensions. The next arguments prove the required Noohi assertion and its stronger left-completeness form. The links identify the local-field proofs used in the ring and field arguments.

**Lemma 7.6c (countability of the finite subextensions).** In a fixed algebraic closure of \(\mathbb Q_\ell\), there are countably many finite subextensions. Thus every algebraic extension \(E/\mathbb Q_\ell\) is an increasing union \(\bigcup_iE_i\) of finite subextensions.

**Proof.** The extension \(L=\mathbb Q_\ell\) already has the rational generator 0. Otherwise put \(n=[L:\mathbb Q_\ell]>1\). In characteristic zero the extension is separable and has a primitive generator \(\alpha\). One can see the last assertion directly: choose finitely many generators \(x_j\) of \(L\), and choose coefficients \(c_j\in\mathbb Q_\ell\) avoiding the finitely many hyperplanes on which two distinct embeddings give the same value to \(\sum c_jx_j\). The base field is infinite, so such coefficients exist. This sum has \(n\) distinct conjugates and generates \(L\).

Let \(f\) be the separable monic minimal polynomial of \(\alpha\). The absolute value extends uniquely to each finite subextension, compatibly on their union, and every embedding over \(\mathbb Q_\ell\) is an isometry. Finite extensions are complete. These are [Theorem 1.2 and Proposition 2.1 of NT-LOC-04](course:NT-LOC/NT-LOC-04). Set \(\delta=\min_{\alpha'\ne\alpha}|\alpha-\alpha'|>0\), over the other conjugates. Choose a sufficiently small power \(\lambda\) of \(\ell\) that \(a=\lambda\alpha\) is integral and \(F(T)=\lambda^nf(T/\lambda)\) has integral coefficients. Put \(D=|F'(a)|>0\).

By density of \(\mathbb Q\) in its completion \(\mathbb Q_\ell\), choose a monic \(g\in\mathbb Q[T]\) so close to \(f\) that \(G(T)=\lambda^ng(T/\lambda)\) is integral and

\[
|G'(a)-F'(a)|<D,\qquad
|G(a)|<\min(D^2,D|\lambda|\delta).
\]

Then \(|G'(a)|=D\). For clarity, Newton lifting here is applied to the integral polynomial \(G\) at the integral point \(a\). If \(q=|G(a)|/D^2<1\), its iterates \(a_{j+1}=a_j-G(a_j)/G'(a_j)\) remain integral, have derivative of absolute value \(D\), and satisfy

\[
|G(a_j)|\le D^2q^{2^j},\qquad
|a_{j+1}-a_j|\le Dq^{2^j}.
\]

Taylor expansion gives the first bound at the next step because the linear term is cancelled and all higher coefficients are integral. The derivative changes by at most \(|a_{j+1}-a_j|<D\), so its absolute value remains \(D\). Completeness gives a root \(b\in L\) with \(|b-a|\le |G(a)|/D\). Thus \(\beta=b/\lambda\) is a root of \(g\) in \(L\), with \(|\beta-\alpha|<\delta\). This is the precise rescaling used in [NT-LOC-04, Corollary 4.2](course:NT-LOC/NT-LOC-04), based on [NT-LOC-03, Theorem 1.1](course:NT-LOC/NT-LOC-03).

The \(n\) embeddings of \(L\) over \(\mathbb Q_\ell\) give \(n\) distinct images of \(\beta\). Indeed, if two images of \(\beta\) were equal, their images of \(\alpha\) would be at distance less than \(\delta\), by the ultrametric inequality and the isometry property. Applying the inverse of one embedding in a finite normal closure shows that distinct such images of \(\alpha\) have distance at least \(\delta\). This is a contradiction. Hence \([\mathbb Q_\ell(\beta):\mathbb Q_\ell]\ge n\), and equality with \(L\) follows from \(\beta\in L\). Every finite subextension is therefore generated by a root of a rational polynomial. There are countably many such polynomials and finitely many roots of each in the fixed algebraic closure. Enumerate the finite subextensions contained in \(E\) and take successive composita to obtain the asserted tower. \(\square\)

Give \(E=\bigcup_iE_i\), \(O_E=\bigcup_iO_{E_i}\), and their matrix groups the final topology from the finite stages. A subset is open exactly when its intersection with every stage is open. This topology is usually finer than the ordinary \(\ell\)-adic topology on an infinite algebraic extension; these two coefficient topologies must not be interchanged.

**Lemma 7.6d (an increasing union of compact coefficient groups).** The additive group \(O_E\) and the group \(H=\mathrm{GL}_r(O_E)\), with these final topologies, have an open-subgroup basis and are complete even for their left uniformity. In particular they are Noohi.

**Proof.** Write either group as \(H=\bigcup_iH_i\), where \(H_i\) is respectively \(O_{E_i}\) or \(\mathrm{GL}_r(O_{E_i})\). These are increasing compact profinite groups. Here is the local-field justification: [NT-LOC-02, Proposition 2.2](course:NT-LOC/NT-LOC-02), proves compactness of \(\mathbb Z_\ell\); [NT-LOC-04, Theorem 3.1](course:NT-LOC/NT-LOC-04), gives a finite free \(\mathbb Z_\ell\)-basis of \(O_{E_i}\), and Proposition 2.1 identifies its coordinate and valued topologies. Thus \(O_{E_i}\) is compact, and its finite congruence quotients form its topology. The matrix group is the closed subset of \(O_{E_i}^{r^2}\) where the determinant is a unit; its congruence kernels are open normal subgroups of finite index and form a basis. The final topology is Hausdorff: its map to the ordinary valued coefficient or matrix topology is continuous and injective. Each stage's inclusion is continuous by definition, so compactness and Hausdorffness show that it has its original topology and is closed in \(H\). Fixed translations and inversion are continuous in the final topology. Indeed, their restrictions to any stage take values in a common larger finite stage and are continuous there.

Let \(W\) be an open neighbourhood of 1. Inductively construct compact open subgroups \(A_i\subset H_i\), increasing with \(i\), and contained in \(W\). Start with \(A_0=\{1\}\). At step \(i\), the compact subgroup \(A_{i-1}\) lies in the open \(W\cap H_i\). Choose an open normal subgroup \(N_i\subset H_i\) so small that \(A_{i-1}N_i\subset W\). Such a choice follows from compactness and the profinite normal-subgroup basis: finitely many translation neighbourhoods suffice. Set \(A_i=A_{i-1}N_i\), a compact open subgroup since \(N_i\) is normal. Their union \(A\) is a subgroup contained in \(W\). Its intersection with \(H_i\) contains the open subgroup \(A_i\), and is itself a subgroup, hence open. Thus \(A\) is final-open. This proves an open-subgroup basis. It also proves joint continuity of multiplication at 1, since \(A\cdot A\subset W\); translations then prove it everywhere. We have proved that the final topology really is a group topology.

Now let \(\mathcal F\) be a left Cauchy filter. Suppose it has no cluster point in \(H\). For each compact \(H_i\), choose \(F_i\in\mathcal F\) whose closure in \(H\) is disjoint from \(H_i\). This is possible by choosing a neighbourhood at each point excluding a filter member and then taking a finite subcover and the intersection of those members.

Construct increasing compact open \(A_i\subset H_i\) such that

\[
H_kA_i\cap\overline{F_k}=\varnothing\qquad(1\leq k\leq i).
\]

At step \(i\), each \(H_kA_{i-1}\) for \(k<i\) is a compact subset of \(H_i\) avoiding \(\overline{F_k}\), by induction. For \(k=i\), it is just \(H_i\), which avoids \(\overline{F_i}\). Choose an open normal \(N_i\subset H_i\) so small that all these finitely many compact products still avoid the corresponding closed sets after multiplication by \(N_i\). Set \(A_i=A_{i-1}N_i\). Compactness supplies the required simultaneous choice, just as in the preceding construction. The union \(A\) is again an open subgroup of \(H\).

For any \(h\in H_k\), the coset \(hA\) misses \(F_k\). Terms \(A_i\) with \(i\geq k\) miss it by the displayed condition; terms with \(i<k\) lie in \(H_k\), which already misses it. But the left Cauchy property gives a filter member all of whose pairwise differences lie in \(A\). Choosing one point \(h\) of that member puts it inside \(hA\). As \(h\) belongs to some \(H_k\), this contradicts intersection with \(F_k\in\mathcal F\). Hence the filter has a cluster point. A Cauchy filter with a cluster point converges: for any open subgroup \(A\), a Cauchy member lies in one closed coset of \(A\); that coset must contain the cluster point. These cosets form its neighbourhood basis. This proves left completeness and thus two-sided completeness. Theorem 7.6 gives the Noohi conclusion. \(\square\)

**Corollary 7.6e (algebraic coefficient Noohi groups).** For every algebraic extension \(E/\mathbb Q_\ell\), the groups \((E,+)\) and \(\mathrm{GL}_r(E)\), with the final coefficient topology, are Noohi and left complete.

**Proof.** The additive subgroup \(O_E\) and matrix subgroup \(H\) are final-open: their intersections with each finite field or matrix stage are open. Translations are homeomorphisms, since a fixed translating element belongs to one finite stage and translation on every other stage maps continuously into a common larger stage. Their open-subgroup bases therefore supply an open-subgroup basis for the whole group and joint continuity of multiplication. Every left Cauchy filter is eventually contained in one coset of the open subgroup. Translation identifies its tail with a Cauchy filter in the complete subgroup, so it converges. Theorem 7.6 again applies.

Consequently these groups also satisfy

\[
G\simeq\varprojlim_{U\subset G\ \mathrm{open}}G/U
\]

as spaces, with transition maps for inclusions of open subgroups. A compatible family of cosets is a left Cauchy filter base. Its unique limit belongs to every coset because cosets are closed. Point stabilizers describe the topology, giving the stated topological identification. This assertion uses the separately proved left completeness; two-sided completeness alone would not justify it for an arbitrary Noohi group. \(\square\)

**Lemma 7.6f (compact coefficient data have a finite field of definition).** Let \(E=\bigcup_i E_i\) have its final coefficient topology. Every compact subset of \(E\), \(O_E\), or \(\mathrm{GL}_r(E)\) is contained in one finite stage, with that stage's usual topology. Consequently, for a profinite space \(P\),

\[
\begin{aligned}
\operatorname{Map}_{\mathrm{cont}}(P,E)
&=\varinjlim_i\operatorname{Map}_{\mathrm{cont}}(P,E_i),\\
\operatorname{Map}_{\mathrm{cont}}(P,O_E)
&=\varinjlim_i\operatorname{Map}_{\mathrm{cont}}(P,O_{E_i}).
\end{aligned}
\tag{7.6a}
\]

**Proof.** Each finite field stage is closed in the ordinary valued topology on \(E\): it is complete, hence closed in any valued extension. It is therefore also closed in the finer final topology. The same argument applies to the integral and matrix stages. Their inclusions are topological embeddings. Indeed their original open subsets extend to open subsets of the ordinary valued coefficient or matrix space, whose topology is coarser than the final topology.

Suppose a compact subset \(C\) is contained in no stage. Inductively choose \(x_j\in C\) and increasing indices \(n_j\), with \(x_j\) outside the \(n_{j-1}\)-st stage and inside the \(n_j\)-th, and with \(n_j\geq j\). Each fixed stage contains only finitely many \(x_j\). Every subset of \(D=\{x_j:j\geq1\}\) thus has closed intersection with every stage, and is final-closed. In particular \(D\) is a closed discrete infinite subspace of \(C\): the complement of \(D\setminus\{x_j\}\) isolates \(x_j\). This contradicts compactness. Hence \(C\) lies in one stage. A continuous map from \(P\) has compact image, and its factorization through that stage is continuous by the embedding assertion. This proves (7.6a), including injectivity of its colimit maps. \(\square\)

Write \(E_X\) and \(O_{E,X}\) for the coefficient sheaves associated to these topological rings. On the affine component-space basis their sections are the continuous functions in (7.6a). Thus, as sheaves,

\[
\begin{aligned}
E_X&=\varinjlim_{F\subset E,\ [F:\mathbb Q_\ell]<\infty}\widehat F_X,\\
O_{E,X}&=\varinjlim_F\widehat O_{F,X},\\
E_X&=O_{E,X}[1/\ell].
\end{aligned}
\tag{7.6b}
\]

The last equality follows by bounding denominators after putting a compact image into one finite field. A sheaf locally free of finite rank over \(E_X\), respectively \(O_{E,X}\), is called an algebraic-coefficient local system.

### Infinite Galois reconstruction

An **infinite Galois category** is a category \(\mathcal C\), with a functor \(F:\mathcal C\to\mathrm{Set}\), such that: all small colimits and finite limits exist; every object is a coproduct of atoms; a set \(\{X_i\}\) of atoms generates under colimits; and \(F\) is faithful, conservative, and preserves these colimits and finite limits. Here an atom is a noninitial object whose only subobjects are the initial object and itself. Conservativity means that a morphism mapped to a bijection is an isomorphism. The group \(\Pi=\operatorname{Aut}(F)\) carries pointwise convergence on every fibre. The category is **tame** when \(\Pi\) acts transitively on the fibre of every atom.

**Lemma 7.7a (presentations by the generators).** Every object is a quotient of a coproduct of the \(X_i\), and every atom is a quotient of one \(X_i\). Compatible permutations of the \(F(X_i)\), commuting with every map between generators, extend uniquely to a natural automorphism of \(F\).

**Proof.** An object with empty fibre is initial: its map from the initial object becomes a bijection, so conservativity applies. A morphism whose fibre map is injective is monic, by faithfulness. To construct the image of \(f:A\to B\), coequalize the projections of its kernel pair \(A\times_B A\). The fibre of this coequalizer is the set-theoretic image of \(F(f)\), since \(F\) preserves that pullback and coequalizer. The induced map to \(B\) has injective fibre map, hence is monic. Likewise a morphism whose fibre map is surjective is the coequalizer of its kernel pair: the remaining map from that coequalizer to its target has bijective fibre, and conservativity makes it an isomorphism.

The class of objects covered in this sense by coproducts of generators is closed under colimits. For a diagram of such objects, compose all their generator maps with their maps to the colimit. The resulting coproduct has a surjective fibre map: every element of a set-theoretic colimit comes from a diagram object. It is therefore a quotient. Since the class contains the generators, colimit generation makes it all of \(\mathcal C\).

The nonempty image of an atom is an atom. For a nonempty subobject of that image, its pullback to the original atom is nonempty, because the map onto the image has surjective fibre map. That pullback is the whole atom. The subobject consequently has both injective and surjective fibre map onto the image, so is the entire image. In particular every nonempty map between atoms is a quotient. When an atom is covered by a coproduct of generators, one of their images is nonempty and therefore is the whole atom. This proves the first assertions.

Take a quotient \(q:X_i\to X\) onto an atom. Its kernel pair is covered by a coproduct of generators. The two composites from each of those generators to \(X_i\) are maps between generators. Their fibre images exhaust the kernel relation on \(F(X_i)\). Compatibility of the given permutations, and of their inverses, preserves this relation. The permutation of \(F(X_i)\) therefore descends to a permutation of \(F(X)\). Two choices of presentation give the same answer: their fibre product over \(X\) is covered by generators, whose two projections give the same compatibility argument. A map between atoms commutes with the descended permutations, by using a presentation of its source and the composite presentation of its target. A map from an atom into a coproduct factors through one component: choose a point of its nonempty fibre and pull back the component containing its image; that nonempty subobject is the whole atom. Thus the descended permutations extend naturally to all coproducts of atoms. Uniqueness follows from their quotient presentations. \(\square\)

**Theorem 7.7 (infinite Galois reconstruction).** The group \(\Pi\) is Noohi. If the category is tame, the natural fibre functor gives an equivalence

\[
\mathcal C\simeq\Pi\text{-}\mathrm{Set}.
\]

More generally a continuous homomorphism \(G\to\Pi\), for any topological group \(G\), is the same as a functor \(\mathcal C\to G\text{-}\mathrm{Set}\) whose underlying set functor is \(F\). Without chosen identifications of the underlying functors, this is an equivalence of groupoids, with conjugation on the homomorphism side.

**Proof.** The lemma identifies \(\Pi\) with the closed subgroup of

\[
\prod_i\operatorname{Sym}(F(X_i))
\]

defined by commuting with every generator map. Its topology agrees with pointwise convergence on all fibres. Indeed, to impose a condition on a point of \(F(X)\), choose its component and a lift to the fibre of a generator presenting that component. A condition on that lift implies the required condition on the original point. Thus all evaluation maps are continuous in the displayed product topology. This product is complete for its two-sided uniformity, and so is the closed subgroup. Its neighborhoods have a basis of finite point stabilizers. Theorem 7.6 proves that \(\Pi\) is Noohi. Its action on every fibre is continuous by the same stabilizer calculation.

Assume tameness. First, subobjects of any \(X\) correspond exactly to the \(\Pi\)-invariant subsets of \(F(X)\). Each component has one orbit in its fibre. A subobject intersects a component in either the empty object or that whole atom, and is therefore the coproduct of precisely those components. To verify the last assertion, the canonical map from that coproduct into the subobject becomes a bijection on fibres; conservativity proves it is an isomorphism. Conversely any union of components gives a subobject with that invariant fibre.

For full faithfulness, let \(f:F(X)\to F(Y)\) be an equivariant map. Its graph is an invariant subset of \(F(X\times Y)\), hence is the fibre of the corresponding union \(Z\) of components of \(X\times Y\). The projection \(Z\to X\) has bijective fibre map, so is an isomorphism. The other projection supplies the unique desired map \(X\to Y\). Faithfulness of \(F\) proves uniqueness.

For essential surjectivity, take an open subgroup \(U\subset\Pi\). There are finitely many generator-fibre points \(x_j\) whose simultaneous stabilizer \(V\) is contained in \(U\). Let \(Z\) be the component of \(\prod_j X_{i_j}\) containing their tuple. Tameness identifies \(F(Z)\), as a pointed action, with \(\Pi/V\). Consider the equivariant equivalence relation on \(\Pi/V\) that declares two cosets equivalent precisely when their images in \(\Pi/U\) agree. It is an invariant subset of the product and hence comes from a subobject \(R\subset Z\times Z\). Coequalize its two projections in \(\mathcal C\). Because \(F\) preserves colimits, the resulting object has fibre exactly \(\Pi/U\), with its natural action. This constructs every transitive continuous action; coproducts construct all of them. This step uses an invariant equivalence relation. It does not assume that the subgroup \(U\) acts equivariantly on \(\Pi/V\), which would fail for nonnormal stabilizers. Full faithfulness and essential surjectivity prove the equivalence.

Finally a fibre-preserving functor into \(G\)-sets gives, for each \(g\in G\), compatible automorphisms on all \(F(X)\), and thus a homomorphism \(G\to\Pi\). The actions are continuous, so preimages of finite point stabilizers are open; this proves continuity of the homomorphism. Conversely a continuous homomorphism defines the compatible actions by composition. These constructions are inverse. Changing a chosen identification of the underlying fibre functors changes the homomorphism by the corresponding natural automorphism, giving the asserted groupoid version. \(\square\)

For schemes, the following arguments verify all four category axioms and tameness. Lemma 7.8b supplies the complete set-of-generators argument, and valuation paths supply the required transitivity.

### Paths and the refined fundamental group

**Lemma 7.8a (a set of valuation paths).** Fix a connected locally topologically Noetherian scheme \(X\). Choose for each point \(p\) an algebraic closure \(\Omega_p\) of \(\kappa(p)\), with geometric point \(\bar p\). There is a set of natural isomorphisms between the fibre functors at these points such that its finite words and inverses act transitively on the geometric fibre of every connected geometric covering.

**Proof.** For each specialization \(p\leadsto q\), take all valuation subrings \(V\subset\Omega_p\) whose maps to \(X\) send generic point to \(p\) and closed point to \(q\). Their residue fields are algebraically closed. Indeed every monic polynomial over a valuation ring with algebraically closed fraction field splits into integral roots in that ring; reduction proves algebraic closedness of the residue field and the henselian factorization criterion. Such a ring is strictly henselian. Also allow every embedding \(\Omega_q\to\kappa(V)\) over \(\kappa(q)\), and every \(\kappa(p)\)-automorphism of \(\Omega_p\).

By Lemma 7.5b, a covering pulled to \(\operatorname{Spec}V\) is a constant set. Its generic and closed fibres are naturally identified. The closed fibre at \(\kappa(V)\) identifies with that at \(\Omega_q\) along the chosen embedding. Étale geometric fibres are unchanged by extensions of algebraically closed fields: their residue algebras are disjoint unions of copies of the field, with the same indexing set. This constructs natural isomorphisms of fibre functors; field automorphisms supply the allowed endpoint changes. All the rings are subsets of the chosen fields, and all embeddings and automorphisms are maps between sets. These paths therefore form a set.

To check that it suffices, take a specialization \(z\leadsto w\) in a geometric covering, with images \(p\leadsto q\). Its residue extension \(\kappa(z)/\kappa(p)\) is finite separable. Embed it into \(\Omega_p\). The local ring at \(w\) of the reduced closure of \(z\) is a domain with fraction field \(\kappa(z)\). A valuation ring of \(\Omega_p\) dominating that local ring exists by valuation domination. Explicitly, take its integral closure in the algebraic extension \(\Omega_p\), choose a prime over its maximal ideal by lying over, and localize there. Clearing the finitely many denominators in a monic equation shows that this integral closure has fraction field \(\Omega_p\). Apply the domination theorem to that local domain. The resulting valuation is one of the rings just listed, and its map into the covering takes generic point to the prescribed geometric lift of \(z\). Embed \(\Omega_q\) into its algebraically closed residue field compatibly with a prescribed geometric lift of \(w\). Such an embedding exists by extending the chosen embedding of the finite separable field \(\kappa(w)\). The resulting path sends the first geometric lift to the second. This argument uses extensions of the endpoint fields and fibre invariance, rather than claiming the valuation's residue field equals a preselected algebraic closure.

In a locally Noetherian topological space, the equivalence classes of finite specialization/generalization chains are open and closed. On an affine Noetherian neighbourhood there are finitely many irreducible components. Each point links to a component's generic point, and intersecting components link their generic points. The chain classes on this neighbourhood are therefore unions of the connected blocks of its finite component-intersection graph; each is clopen. The classes are consequently open and closed globally. A connected covering has one class. Any two points over \(\bar p\) can thus be linked by a finite chain in the covering, and the preceding valuation constructions lift that chain to natural isomorphisms of base fibre functors. At the endpoints, field automorphisms adjust the geometric lifts: the absolute Galois group acts transitively on the embeddings of a finite separable residue extension. Their composite is a natural automorphism of the fibre functor at \(\bar p\) sending one given fibre element to the other. \(\square\)

**Lemma 7.8b (set of connected generators).** The isomorphism classes of connected geometric coverings of \(X\) form a set. They generate \(\mathrm{Cov}_X\) under coproducts.

**Proof.** Choose an infinite cardinal \(\kappa\) bounding the set of points of \(X\), a fixed affine open cover and its rings, and all the fields \(\Omega_p\). A valuation subring of any \(\Omega_p\) has at most \(\kappa\) elements, as does its residue field. There are at most \(2^\kappa\) such rings, embeddings and endpoint automorphisms. Thus the path alphabet in Lemma 7.8a and the set of its finite words have cardinal at most \(\mu=2^\kappa\). On every connected covering they act transitively on every geometric fibre. After choosing one element, that fibre is consequently a quotient of a set of at most \(\mu\) words. Its cardinal is at most \(\mu\).

There are at most \(\mu\) underlying points in the covering: each is seen in a geometric fibre over one of at most \(\kappa\) base points. Take one affine étale chart around each point, over a member of the fixed affine base cover. An affine étale map to an affine scheme is finitely presented here: it is locally of finite presentation and is quasi-compact and quasi-separated. These charts come from a set of finite ring presentations over the fixed base rings. The covering is obtained by gluing at most \(\mu\) charts from that set. Open subsets of every chart and isomorphisms between such subsets are themselves sets. Indexing the charts by subsets of a fixed set of cardinal \(\mu\), all choices of charts, overlap opens, gluing isomorphisms and cocycle equalities lie in a set. Passing to their quotients or isomorphism classes still gives a set. Restrict to the gluing data that produce connected geometric coverings. This proves the first assertion without invoking the group classification to prove its own size axiom.

A locally topologically Noetherian étale scheme has open-and-closed connected components by the finite-chain argument above. Each clopen component retains the valuative criterion: the inverse image of that component under a valuation lift is clopen in the connected valuation spectrum, hence either empty or all. Thus every covering is the coproduct of its connected covering components. Representatives of the set just constructed give the asserted generators. \(\square\)

**Theorem 7.8 (the refined fundamental group).** For a connected locally topologically Noetherian scheme \(X\) and a geometric point \(\bar x\), the category \((\mathrm{Loc}_X,F_{\bar x})\) is a tame infinite Galois category. Its automorphism group

\[
\Pi=\pi_1^{\mathrm{pro\acute et}}(X,\bar x)=\operatorname{Aut}(F_{\bar x})
\]

is Noohi, and

\[
\mathrm{Loc}_X\simeq\mathrm{Cov}_X\simeq\Pi\text{-}\mathrm{Set}.
\tag{7.8}
\]

**Proof.** Theorem 7.5d and Proposition 7.5c give colimits and finite limits. Lemma 7.8b supplies a set of connected generators and the disjoint-component decomposition. A connected covering is an atom in this category. Indeed, a map of coverings is étale, by the usual permanence of étaleness for maps between étale objects, and satisfies the valuative criterion over its target: extend its generic lift over \(X\), and use uniqueness for the target covering to identify the resulting base map. Its image is open and stable under specialization. On a locally Noetherian space such a locally constructible subset is closed. For completeness, on an affine chart a constructible subset's closure consists of specializations of its points; this follows by compactness of the constructible topology, intersecting the basic neighbourhood conditions for a generalizing point. Specialization stability therefore makes the image closed. A monomorphism of coverings is an étale monomorphism, hence an open immersion. Its clopen image in a connected covering is empty or the whole, proving atomicity.

The geometric fibre preserves colimits and finite limits: all these sheaves are classical, these operations remain within the category, and ordinary étale stalks preserve colimits and finite limits. Lemma 7.8a gives natural paths between the fibres at any two base points. Hence a morphism bijective at \(\bar x\) is bijective at every geometric point and is an isomorphism; two morphisms equal at \(\bar x\) agree at every point and are equal. The fibre functor is conservative and faithful. The last assertion of Lemma 7.8a is exactly tameness. Theorem 7.7 now proves the Noohi assertion and the equivalence. Moreover the subgroup of valuation-path words based at \(\bar x\) is dense in \(\Pi\). Given finitely many specified fibre points and an automorphism \(h\), put them in a finite product of coverings. The tuple and its image under \(h\) lie in the same connected component, because the component inclusion is a morphism respected by \(h\). Lemma 7.8a supplies a path taking that tuple to its image. This satisfies every prescribed finite point condition; inverse conditions can be rewritten as direct conditions. Every size, conservativity and transitivity axiom has been checked explicitly. \(\square\)

**Corollary 7.8c (open-subgroup coverings and finite completion).** Each open subgroup \(U\subset\Pi\) gives a pointed connected covering \(X_U\to X\) with fibre \(\Pi/U\), and \(\pi_1^{\mathrm{pro\acute et}}(X_U,\bar x)=U\) with its subspace topology. The profinite completion of \(\Pi\) is the usual étale fundamental group.

**Proof.** Reconstruction produces the pointed object for \(\Pi/U\). The slice category of \(\Pi\)-sets over \(\Pi/U\) is equivalent to discrete continuous \(U\)-sets: take the fibre at the identity coset, with inverse \(T\mapsto\Pi\times_U T\). The corresponding geometric slice consists of coverings of \(X_U\), since the valuative criterion is stable under composition and is inherited by a morphism between coverings. The fibre functors agree. An open subgroup of a complete group is complete, since it is also closed; its point stabilizers give an open-subgroup basis. The Noohi theorem therefore recovers \(U\) with exactly its subspace topology.

Finite \(\Pi\)-sets correspond precisely to finite étale \(X\)-schemes. To verify finiteness geometrically, a finite-fibre covering becomes the constant finite covering after a pro-étale trivialization; finiteness descends faithfully flat. Conversely a finite étale scheme is a geometric covering and gives a finite action. Thus finite continuous quotients of \(\Pi\) and the pointed finite étale fibre category agree. Taking the inverse limit of their finite automorphism groups gives the usual étale fundamental group and the profinite completion of \(\Pi\). No assertion that all its infinite actions factor through that completion is made. \(\square\)

### Continuous representations and completions

**Proposition 7.9 (the étale locally constant subcategory).** Under Theorem 7.8, a discrete \(\Pi\)-set \(S\) is already locally constant for the étale topology precisely when one open subgroup of \(\Pi\) acts trivially on the whole set. Equivalently, its action has open normal kernel. For a discrete group \(D\), continuous homomorphisms \(\Pi\to D\), up to conjugation, classify étale \(D\)-torsors. The pro-discrete completion is

\[
\Pi^{\mathrm{pd}}=\varprojlim_{N\triangleleft\Pi\ \mathrm{open}}\Pi/N.
\tag{7.9}
\]

It has the same continuous homomorphisms to discrete groups as \(\Pi\).

**Proof.** If an open \(U\) acts trivially, restriction to the pointed covering \(X_U\) makes the corresponding sheaf constant, by the slice equivalence in Corollary 7.8c. This is an étale cover, so the sheaf is étale locally constant. Conversely let \(F\) be étale locally constant with fibre \(S\). Its frame sheaf \(\operatorname{Isom}(\underline S,F)\) is an étale torsor for the **discrete** group \(\operatorname{Sym}(S)\). Here a permutation-valued automorphism on an étale chart is constant on each connected component: that chart is locally topologically Noetherian and its components are open. Thus the usual automorphism sheaf of its constant set is the constant discrete group sheaf. The frame torsor is itself étale locally constant and hence a geometric covering by Theorem 7.5d. Choose a frame at \(\bar x\). Its open stabilizer \(U\) in \(\Pi\) fixes every element of \(S\), by naturality of evaluation of a frame. This proves the criterion. A subgroup acting trivially lies in the normal kernel, so that kernel is open, giving the equivalent formulation.

A \(D\)-torsor is described under (7.8) by the set \(D\), with commuting simply transitive right \(D\)-action and a left \(\Pi\)-action. Choosing a fibre point gives a homomorphism \(\Pi\to D\). Its kernel is the stabilizer of that point, so is open and the homomorphism is continuous to discrete \(D\). Changing the point conjugates it. Conversely such a homomorphism supplies that torsor. Its kernel acts trivially on the whole set, so the preceding criterion makes it an étale torsor.

Every map to a discrete group factors through the quotient by its open normal kernel. It therefore extends to (7.9), and the extension is unique because \(\Pi\)'s image is dense. To check density, any finitely many quotient coordinates are refined by their finite intersection of kernels. The coordinate at that intersection represents every compatible finite tuple by an element of \(\Pi\). Conversely restrict a continuous homomorphism from (7.9). The same argument works coordinatewise for targets that are inverse limits of discrete groups. This completion comparison concerns homomorphisms to such targets; the criterion on an infinite set \(S\) still requires an open kernel for the whole action. \(\square\)

**Theorem 7.10 (finite-extension coefficient classification).** Let \(X\) be connected and locally topologically Noetherian, fix \(\bar x\), and put \(\Pi=\pi_1^{\mathrm{pro\acute et}}(X,\bar x)\). Let \(E/\mathbb Q_\ell\) be finite. Finite-rank \(E\)-local systems on \(X_{\mathrm{pro\acute et}}\) correspond, by their fibre at \(\bar x\), to finite-dimensional continuous \(E\)-representations of \(\Pi\).

**Proof.** Integral local systems first correspond to representations into \(\mathrm{GL}_r(O_E)\). This group is profinite. Its finite quotients give the finite locally constant reductions of an integral local system, and conversely their compatible tower gives its completed integral sheaf, by Proposition 4.2. Corollary 7.8c identifies these finite actions with the ordinary étale finite-action category. This argument works on each connected covering \(X_U\), including a non-quasi-compact one; it uses finite-level sheaves rather than a global denominator bound.

Given \(\rho:\Pi\to\mathrm{GL}_r(E)\), put \(U=\rho^{-1}(\mathrm{GL}_r(O_E))\). It is open. The restricted representation gives an integral local system on \(X_U\), and rationalization gives an \(E\)-local system there. We describe its descent explicitly. Connected components of \(X_U\times_XX_U\) correspond to double cosets, with stabilizers \(U\cap gUg^{-1}\), by (7.8). On the component indexed by \(g\), the two rationalized integral systems are identified by the intertwining matrix \(\rho(g)\). A single power of a uniformizer makes this matrix integral on that component, so the finite-level correspondence gives the required map; rationalization makes it invertible. Changing a representative by elements of \(U\) changes the lattice frames by their integral action, and hence gives the same descent map. On triple overlaps, the maps compose by \(\rho(gh)=\rho(g)\rho(h)\). Components are clopen, so these maps glue even when the overlap has infinitely many components. Sheaf descent along \(X_U\to X\) constructs \(L(\rho)\). A representation intertwiner is treated on a common open subgroup preserving both chosen lattices, after clearing its constant matrix's denominators. The same overlap calculation descends it. We have a functor from representations to local systems.

For the converse, put \(G=\mathrm{GL}_r(E)\). On an affine w-contractible \(Y\), let \(\mathcal G(Y)\) be continuous functions \(\pi_0Y\to G\). This is the sheaf of automorphisms of \(\widehat E^r\): completed coefficient sections are continuous functions, and compactness bounds the denominators of each matrix and its inverse. The frame sheaf \(P=\operatorname{Isom}_{\widehat E}(\widehat E^r,L)\) is a torsor for \(\mathcal G\). For every discrete continuous \(G\)-set \(S\), its associated sheaf \(P\times^{\mathcal G}\underline S\) is pro-étale locally the constant set \(S\). The action is well-defined as a sheaf action: the stabilizer of each \(s\) is open, so a continuous matrix-valued function sends a locally constant section to a locally constant section. Choosing a frame of the fibre of \(L\) identifies the fibres of all these associated sheaves with their underlying sets. Applying \(\Pi\)'s natural automorphisms therefore gives a continuous map

\[
\Pi\longrightarrow\operatorname{Aut}(F_G)=G.
\]

The equality uses the Noohi theorem: \(G\) is locally compact with its congruence open-subgroup basis, and hence Noohi. Continuity is detected by the finite point stabilizers in discrete actions. Changing the fibre frame conjugates the representation by its change-of-basis matrix.

We verify that these constructions are inverse, rather than merely assigning a representation. Let \(K_m=1+\varpi^mM_r(O_E)\), for \(m\geq1\). There is an isomorphism of sheaves

\[
\mathcal G\simeq\varprojlim_m\underline{G/K_m}.
\tag{7.10}
\]

Pointwise, a compatible sequence of cosets is a decreasing family inside its first compact coset; compactness gives a unique intersection point, since \(\bigcap_mK_m=1\). The coset coordinates define exactly the topology of \(G\), so compatible locally constant coordinates on any component space give a continuous \(G\)-valued function. This proves (7.10) on a generating affine basis. After trivializing \(P\), the same identity identifies it with the inverse limit of its associated coset sheaves. The representation extracted from \(P\) has, by construction, precisely these associated \(\Pi\)-sets. The sheaf constructed from that representation has the same coset sheaves, so their inverse limits identify its frame torsor with \(P\), respecting the \(\mathcal G\)-action. The associated vector sheaves are therefore isomorphic. In the other direction, the overlap matrices of \(L(\rho)\) are \(\rho(g)\), so its action on every discrete \(G\)-set is the original action; the Noohi identification recovers \(\rho\).

Finally a linear map of fibres commuting with the representations gives a sheaf map by the common-open-subgroup construction above. For the converse, an \(E\)-local system is constant on a strictly henselian valuation scheme. Indeed Proposition 7.2 gives an étale local integral lattice; an étale piece meeting the closed point has a section over the strictly henselian local base, so the lattice is global there. Its finite reductions are constant and their compatible bases lift successively, giving the constant completed lattice. A sheaf map on such a scheme is therefore a constant matrix, since its component space is a point and its completed coefficient sections are \(E\). Consequently a sheaf map respects every valuation path and every algebraically closed endpoint extension. The path words are dense in \(\Pi\), by Theorem 7.8. The matrix intertwining equation is closed in the coefficient groups, and hence holds on all of \(\Pi\). This proves the converse.

A map is determined by its fibre. The same path argument determines its value at every geometric point of \(X\). On an affine cover trivializing both local systems it is a matrix of continuous functions on the component space, and each value of those functions is a geometric fibre value. If all those values vanish, the matrix vanishes. Thus no nonzero map has zero fibre map. The functors are fully faithful as well as inverse on objects. \(\square\)

**Corollary 7.11 (geometrically unibranch bases).** If \(X\) is also geometrically unibranch, then \(\Pi=\pi_1^{\mathrm{\acute et}}(X,\bar x)\). Every finite-extension \(E\)-local system has a global integral lattice.

**Proof.** Use the characterization of geometric unibranchness by irreducibility of the reduction of each strict henselian local scheme. It is preserved by étale maps: the corresponding strict henselian local rings are isomorphic. In particular each local ring has one minimal prime. On a Noetherian-topology affine chart, distinct irreducible components therefore cannot meet; there are finitely many, and each is clopen. Hence irreducible components are clopen globally. Connected \(X\) is irreducible, as is every connected geometric covering \(Y\).

The generic fibre \(Y_\eta\) is then a connected étale scheme over the generic field, and thus the spectrum of one finite separable field extension. Its geometric fibre has finite cardinality. The valuation paths in Lemma 7.8a identify that fibre with the fibre at every other base point. Thus \(Y\) has finite geometric fibres of that same cardinality. Corollary 7.8c makes it finite étale. All transitive discrete \(\Pi\)-actions are consequently finite. Each open subgroup has finite index, and its finite intersection of conjugates is open normal. The topology has an open normal subgroup basis with finite quotients. Two-sided completeness then identifies \(\Pi\) with the inverse limit of these finite quotients: the image is dense by the finite-coordinate argument, closed by completeness, and has the same topology. Its identification with the usual étale group follows from Corollary 7.8c.

The image of a continuous \(E\)-representation of this profinite group is compact. Given a basis lattice, compactness bounds the coordinates of all its translates inside one larger lattice. Their \(O_E\)-span is a finite module, contains the starting lattice and is torsion-free, hence is a lattice. It is stable under the group. Theorem 7.10 turns it into the claimed global integral local system. \(\square\)

### Finite fields of definition for algebraic coefficients

**Proposition 7.12 (finite scalar descent).** Let \(X\) be quasi-compact and quasi-separated and let \(E/\mathbb Q_\ell\) be algebraic with the final coefficient topology. Extension of scalars gives equivalences

\[
\begin{aligned}
\varinjlim_{F\subset E,\ [F:\mathbb Q_\ell]<\infty}
\mathrm{Loc}_X(F)&\simeq\mathrm{Loc}_X(E),\\
\varinjlim_F\mathrm{Loc}_X(O_F)&\simeq\mathrm{Loc}_X(O_E).
\end{aligned}
\tag{7.11}
\]

Here the filtered colimit of categories allows both objects and morphisms to acquire a larger finite field of definition. If \(X\) is also connected and locally topologically Noetherian, the fibre functor identifies \(\mathrm{Loc}_X(E)\) with the full subcategory of continuous finite-dimensional \(E\)-representations of \(\Pi\) that, in some basis, have image in \(\mathrm{GL}_r(F)\) for one finite \(F\subset E\). For geometrically unibranch such \(X\), this is the entire continuous representation category.

**Proof.** We first justify finite scalar descent without any fundamental-group assumption. A locally free sheaf of fixed rank becomes trivial on an affine w-contractible cover: refine a trivializing covering to a faithfully flat affine cover and pull a trivialization back along a section. If the covering uses several pieces, the section partitions the base into clopen subsets, on each of which it supplies a frame. The same argument handles varying rank; a quasi-compact base has only finitely many rank pieces.

Choose finitely many affine w-contractible pieces \(W_i\to X\) covering \(X\), with frames of the given local system. Their finite disjoint union \(W\) is affine. The overlaps \(W_i\times_XW_j\) and triple overlaps are quasi-compact and quasi-separated because \(X\) is. On finitely many affine w-contractible covers of each double overlap, the transition maps and their inverses are continuous matrices on compact component spaces. Lemma 7.6f puts their finitely many entries in one finite field \(F\). In the integral case their entries and inverse entries belong to \(O_F\). Entries on overlapping covering pieces agree already over \(F\): the map of coefficient sheaves for \(F\subset E\) is injective, as (7.6a) shows on the affine basis. They therefore glue to matrices over \(F\) on each double overlap. The same injectivity makes the cocycle identity hold over \(F\) on every triple overlap. Effective descent of sheaves gives the desired \(F\)-local system on \(X\).

For two local systems, take common finite trivializing data. A morphism between their scalar extensions is locally a matrix of coefficient sections. On the finitely many chosen affine pieces, Lemma 7.6f puts its entries in one larger finite field. Injectivity descends its compatibility with the transition matrices and its equality with any other map. This proves the Hom assertion, and hence both equivalences in (7.11). The argument supplies the actual frames, transitions, inverse matrices and cocycle, rather than only a field of definition for individual fibres.

Now impose the additional hypotheses on \(X\). Choose a finite field of definition \(F\) for a local system and apply Theorem 7.10 over \(F\). Include its continuous representation into \(\mathrm{GL}_r(E)\); that inclusion is continuous by the final topology. A larger field of definition gives the scalar extension of the same representation, so the construction is independent of the choice. An \(E\)-linear intertwiner has finitely many entries, which belong to a finite extension of the two fields of definition. Theorem 7.10 over that extension gives a unique sheaf map. Thus the functor is fully faithful. Conversely a continuous representation whose matrices lie in one finite \(F\) is continuous as an \(F\)-representation, because the finite-stage inclusion is a topological embedding. Theorem 7.10 constructs its \(F\)-local system, and scalar extension constructs the required \(E\)-local system. This proves the stated essential image.

If \(X\) is geometrically unibranch, Corollary 7.11 makes \(\Pi\) profinite. Every continuous representation has compact image, so Lemma 7.6f puts it in one finite matrix stage. The preceding argument then proves the full algebraic-coefficient classification in this case. \(\square\)

### Arbitrary algebraic-coefficient representations on singular bases

We now remove the finite-field-image restriction in Proposition 7.12 and the quasi-compactness restriction on the base. The existence step needs a coherent trivialization of all the associated coset sheaves. Completeness of the coefficient group identifies their inverse limit only after that local existence has been proved.

**Lemma 7.12a (simultaneous local fibre identifications).** Let \(X\) be connected and locally topologically Noetherian, with geometric point \(\bar x\). Fix a set of objects \(F_a\in\mathrm{Loc}_X\), together with any set of maps between them. There is a pro-étale cover by affine w-contractible schemes on which every \(F_a\) is identified with the constant sheaf of its fibre \((F_a)_{\bar x}\), and every specified map is identified with its fibre map. The identifications can be chosen on a w-contractible cover of each affine open of \(X\).

**Proof.** Take an affine open \(V\subset X\), its finitely many generic points \(\eta_1,\ldots,\eta_d\), and an affine w-contractible cover \(Y\to V\). Put \(P=\pi_0(Y)\). Proposition 7.5c and Lemma 7.5a write \(F_a|Y=\pi_Y^*H_a\), naturally also for all the specified maps. Choose separable closures \(K_i\) of \(\kappa(\eta_i)\), and an affine w-contractible cover

\[
\begin{gathered}
Z\longrightarrow
Y\times_V\coprod_{i=1}^d\operatorname{Spec}K_i,\\
q:\pi_0(Z)\longrightarrow P.
\end{gathered}
\tag{7.11a}
\]

The scheme on the right is affine, so Theorem 1.1f supplies \(Z\). The map \(q\) is surjective. Each component of \(Y\) is the local spectrum at a closed point. The flat local map from the corresponding base local ring has, by going down, a point above some \(\eta_i\); that point lifts after separable closure and then into the faithfully flat cover \(Z\). Thus every component of \(Y\) meets the image. The component spaces are profinite, and \(P\) is extremally disconnected. Lemma 1.1e gives a continuous section \(s:P\to\pi_0(Z)\).

Over \(\operatorname{Spec}K_i\), every classical étale sheaf is constant, canonically with its geometric fibre. Choose, once for each \(i\), a valuation path from \(\bar x\) to a geometric point above \(\eta_i\), as in Lemma 7.8a. Extending a separably closed endpoint to an algebraic closure does not change these fibres. The chosen path identifies the generic fibre functor with \(F_{\bar x}\), naturally for every object and map. Consequently, on the clopen part of \(Z\) lying over \(K_i\), all the \(F_a\) have simultaneous identifications with the constant sheaves \(\underline{(F_a)_{\bar x}}\). These identifications assemble over the finite disjoint union of the field pieces.

Pullback from the component space commutes with this restriction:
\(F_a|Z=\pi_Z^*q^*H_a\). One checks this first for finite locally constant component sheaves and then for their filtered colimits, using Lemma 7.5a. Full faithfulness of \(\pi_Z^*\), followed by Proposition 3.1, therefore descends all the preceding identifications to
\(q^*H_a\simeq\underline{(F_a)_{\bar x}}\) on \(\pi_0(Z)\). It descends their naturality as well. Pull these isomorphisms back along \(s\). Since \(q s=1_P\), they identify each \(H_a\) with the required constant component sheaf and every specified map with its fibre map. Pullback to \(Y\) proves the assertion on \(V\). Doing this for all affine opens gives the asserted cover of \(X\). We pulled back compatible isomorphisms individually; no interchange of inverse image with an infinite inverse limit was used. \(\square\)

**Theorem 7.12b (algebraic-coefficient classification).** Let \(X\) be connected and locally topologically Noetherian, let \(\bar x\) be a geometric point, and let \(E/\mathbb Q_\ell\) be any algebraic extension with the final coefficient topology. There are fibre equivalences

\[
\begin{aligned}
\mathrm{Loc}_X(E)&\simeq
\mathrm{Rep}_{E,\mathrm{cont}}\bigl(\pi_1^{\mathrm{pro\acute et}}(X,\bar x)\bigr),\\
\mathrm{Loc}_X(O_E)&\simeq
\mathrm{Rep}_{O_E,\mathrm{cont}}\bigl(\pi_1^{\mathrm{pro\acute et}}(X,\bar x)\bigr).
\end{aligned}
\tag{7.11b}
\]

The second line uses free finite-rank modules and continuity to \(\mathrm{GL}_r(O_E)\). There is no quasi-compactness, quasi-separatedness, normality or geometric unibranchness hypothesis. If \(X\) is qcqs, every continuous representation in either line has a finite coefficient field of definition, after choosing a fibre basis. For general \(X\), finite fields of definition and integral lattices exist locally; a single global field or a single global lattice is not needed for the equivalence.

**Proof: constructing the frame torsor.** Write \(\Pi=\pi_1^{\mathrm{pro\acute et}}(X,\bar x)\), and take a continuous \(\rho:\Pi\to G\), where \(G\) is either \(\mathrm{GL}_r(E)\) or \(\mathrm{GL}_r(O_E)\). Restricting discrete continuous \(G\)-actions along \(\rho\), then applying Theorem 7.8, gives a functor \(A_\rho:G\text{-}\mathrm{Set}\to\mathrm{Loc}_X\) preserving colimits and finite limits. Its fibres at \(\bar x\) are the original sets with the action prescribed by \(\rho\).

For every open subgroup \(U\subset G\), form \(A_\rho(G/U)\). Include in this set of objects every equivariant map between the coset objects. In particular include the transition maps for subgroup inclusions and the maps
\(aU\mapsto ag(g^{-1}Ug)\), for every \(g\in G\). Lemma 7.12a supplies simultaneous local identifications of this entire diagram with its diagram of constant coset sheaves. Define the sheaf

\[
\begin{aligned}
\mathscr P_\rho&=\varprojlim_{U\subset G\ \mathrm{open}} A_\rho(G/U),\\
\mathcal G(T)&=\operatorname{Map}_{\mathrm{cont}}(\pi_0(T),G).
\end{aligned}
\tag{7.11c}
\]

on the affine w-contractible basis for the second expression. Intersections of open subgroups make the first diagram cofiltered. Corollary 7.6e identifies \(G\), with its topology, with \(\varprojlim_U G/U\); for the integral group this is Lemma 7.6d. Hence on a cover supplied by Lemma 7.12a, \(\mathscr P_\rho\) is \(\mathcal G\). Indeed compatible locally constant coset coordinates on any profinite component space are precisely continuous functions to that inverse limit. In particular the identity element supplies a section there. This proves local inhabitation, including when the collection of open subgroups is uncountable.

The included maps for right translation give a right action of constant elements of \(G\) on this limit. Under each of the simultaneous identifications it is the usual right translation. Changes between two such identifications commute with these translations. On an affine w-contractible test object they must be left multiplication by a continuous \(G\)-valued function: evaluate at 1, and then at every component, where a map commuting with every right translation sends \(g\) to its value at 1 times \(g\). Equality on components detects equality of continuous functions. Thus the local right \(\mathcal G\)-actions glue, and \(\mathscr P_\rho\) is a \(\mathcal G\)-torsor. Its associated coset sheaf is exactly \(A_\rho(G/U)\), as is checked in these same local identifications. The quotient by an open subgroup is the constant discrete coset sheaf locally: a locally constant coset section lifts on clopen pieces by choosing a representative of each of its finitely many values. Colimits of coset objects then show that its associated sheaf for every discrete continuous \(G\)-set \(S\) is \(A_\rho(S)\).

For the rational group, \(\mathcal G\) is the automorphism sheaf of \(E_X^r\); for the integral group it is that of \(O_{E,X}^r\), by (7.6a)–(7.6b). Descend these free sheaves using the torsor's transition matrices. Their products are the torsor cocycle, so ordinary effective sheaf descent constructs respectively an \(E\)-local system \(L(\rho)\) or an \(O_E\)-local system \(M(\rho)\). The global definition (7.11c) fixes the object independently of the auxiliary generic points, paths and component sections.

**Local finite fields, lattices and gluing.** Each affine open \(V\) is qcqs. The scalar-descent part of Proposition 7.12, which did not use any representation-classification assertion, puts the constructed system on \(V\) into one finite field \(F_V\). In the rational case Proposition 7.2 then supplies integral lattices on an étale cover of \(V\). In the integral case the system itself descends to \(O_{F_V}\). There is also a direct generic-field check: the fibre functor at \(\eta_i\) gives a continuous map from the profinite absolute Galois group of \(\kappa(\eta_i)\) to \(\Pi\). Its image under \(\rho\) is compact, so Lemma 7.6f puts the generic matrices in one finite stage. In the rational case their compact group preserves a lattice, by the bounded-translates argument of Corollary 7.11. This check concerns a generic-field restriction, and does not assume compactness of the whole image of \(\Pi\).

No global finiteness is required to glue the affine constructions. They are restrictions of the same sheaf (7.11c), with the same coset maps. On an overlap, refine to affine w-contractible objects and compare their two torsor frames. The resulting continuous matrices are invertible and satisfy the cocycle on every triple overlap. Sheaf descent glues over the full open cover, even when there are infinitely many opens or an overlap is not qcqs. Finite fields and denominator bounds are chosen on the affine test pieces where they are needed; their choices do not enter the global descent identity.

**Recovering the representation and proving the inverses.** Given an algebraic-coefficient local system \(L\), its frame torsor \(\mathscr P\) associates to every discrete continuous \(G\)-set \(S\) a sheaf in \(\mathrm{Loc}_X\). A fibre frame identifies their fibres with \(S\). Theorem 7.7 and the Noohi identification of Corollary 7.6e give a continuous homomorphism \(\rho_L:\Pi\to G\), just as in Theorem 7.10. In the integral case use Lemma 7.6d. After a frame trivialization, left completeness identifies \(\mathscr P\) with the inverse limit of its associated coset sheaves. These sheaves, with all their maps, are precisely \(A_{\rho_L}(G/U)\). Equation (7.11c) therefore recovers \(\mathscr P\), and descent of its standard free module recovers \(L\). Conversely, the associated discrete actions of \(\mathscr P_\rho\) are \(A_\rho(S)\), as proved above. Their action at the chosen fibre is the original \(\rho\); Noohi reconstruction consequently recovers that homomorphism. Changing the fibre frame conjugates it, as usual.

**All linear morphisms.** A sheaf map respects valuation paths. To verify this for algebraic coefficients, pull its two systems and the map to an affine strictly henselian valuation scheme used in Lemma 7.8a. Proposition 7.12's scalar-descent argument puts these data in a finite field. The lattice and constant-matrix argument in Theorem 7.10 applies there: a pointed étale lattice neighbourhood has a section, its finite reductions split, and compatible bases make its completed lattice constant. Thus the map has one constant coefficient matrix on that valuation scheme. It respects the generic-to-closed fibre identification and all endpoint extensions. Path words are dense in \(\Pi\), and the matrix intertwining equation is closed in the Hausdorff coefficient topology. Hence its fibre map intertwines the two representations.

Conversely, let \(B\) be any linear intertwiner of their fibres, allowing different ranks. Choose a connected affine open cover, a geometric point on each member and a path from \(\bar x\) to that point. Transport \(B\) along those paths. Proposition 7.12 descends the two restricted systems to finite coefficient fields. The finitely many entries of the transported matrix lie in a common larger finite field; in the integral case they lie in its valuation ring. Restriction of the associated discrete actions shows that the restricted monodromy is the given global representation restricted to this affine's fundamental group, with the chosen path identification. The transported matrix is therefore an intertwiner there. The finite-field rational or integral correspondence in Theorem 7.10 produces a sheaf map on that affine open.

These maps agree on overlaps. At a geometric point of an overlap, two choices of transport differ by a loop in \(\Pi\), and \(B\)'s intertwining identity makes the two transported matrices equal. Maps of local systems are detected by these values: on a common affine w-contractible trivializing cover they are continuous coefficient matrices, and vanishing at every component makes such a matrix zero. Refining the overlap by such objects proves equality without a quasi-compactness assumption. The maps consequently glue. The same argument proves uniqueness of a map with given fibre value. This proves full faithfulness, as well as both object inverses, in (7.11b).

Finally, on qcqs \(X\), apply Proposition 7.12 to the constructed system and choose a frame of its finite-field fibre. Its monodromy lies in \(\mathrm{GL}_r(F)\), or \(\mathrm{GL}_r(O_F)\), for one finite \(F\subset E\), and its scalar extension is the original representation by the inverse just proved. This finite-stage property is a consequence of essential surjectivity and scalar descent, rather than a hypothesis of the construction. \(\square\)

This completes the algebraic-extension comparison in [Bhatt–Scholze, Remark 7.4.8](https://arxiv.org/html/1309.1198v2#S7.SS4.Thmtheorem8). The simultaneous component-space argument uses the generic-field and section construction in their Lemma 7.3.9, now with all the coset maps retained, to supply the local existence needed in that comparison. It also supplies the integral case without treating \(\mathrm{GL}_r(O_E)\) as profinite when \(E\) is infinite.

### Gluing across one node

Let \(k\) be algebraically closed, let \(Y\) be a smooth connected separated curve of finite type over \(k\), and let \(a,b\in Y(k)\) be distinct. Let \(\pi:Y\to X\) be the finite normalization map for the curve obtained by identifying \(a\) and \(b\), with \(c=\pi(a)=\pi(b)\). Thus \(\pi\) is an isomorphism off those points, and the completed local ring at \(c\) is

\[
\widehat{\mathcal O}_{X,c}
\simeq k[[u]]\times_k k[[v]]
\simeq k[[u,v]]/(uv).
\tag{7.12}
\]

The two branch coordinates fix the order \(a,b\).

**Proposition 7.13 (normalization gluing of local systems).** For a finite extension \(F/\mathbb Q_\ell\), an \(F\)-local system on \(X\) is equivalently a pair \((M,\alpha)\), where \(M\) is an \(F\)-local system on \(Y\) and

\[
\alpha:M_a\xrightarrow{\sim}M_b
\]

is an \(F\)-linear isomorphism. A morphism \((M,\alpha)\to(M',\alpha')\) is a sheaf map \(h:M\to M'\) satisfying \(h_b\alpha=\alpha'h_a\). The same equivalence holds for algebraic \(E/\mathbb Q_\ell\) with its final topology.

**Proof.** We give the local construction at the node. Two affine smooth curve neighbourhoods \(U_a,U_b\), each with one distinguished \(k\)-point, can be joined by the affine ring

\[
R=A_a\times_k A_b,
\qquad A_a=\Gamma(U_a,\mathcal O),\quad A_b=\Gamma(U_b,\mathcal O).
\]

Its functions are pairs with equal values at the distinguished points. The projections induce the normalization, and away from the join the two branches are unchanged. Completion at the join gives (7.12). If \(U_a,U_b\) are pointed étale neighbourhoods of \(a,b\) in \(Y\), their joined curve \(W\) maps étale to \(X\) near its node. Here is the local check. For its local map \(A\to D\), the completed map \(\widehat A\to\widehat D\) is an isomorphism. Since \(\widehat D\) is faithfully flat over \(D\) and is flat over \(A\), faithful flat descent makes \(D\) flat over \(A\). Completion also identifies the two cotangent spaces at the common residue field \(k\); the cotangent exact sequence gives \(\Omega_{D/A}\otimes_Dk=0\). The differentials are finite, so Nakayama gives \(\Omega_{D/A}=0\). The map is of finite presentation and has identical residue field, proving étaleness. The exactness and faithful flatness used here are [AG-CA-19, Theorems 3.1–3.2](course:AG-CA/AG-CA-19); its preceding Artin–Rees and flatness inputs remain its stated prerequisites. Away from the node étaleness is the original étaleness of the branches. Shrinking if needed gives an étale \(W\to X\) which meets \(c\); together with \(X\setminus\{c\}\) it covers \(X\).

We will use the following finite gluing calculation. Suppose \(D_a,D_b\) are finite étale schemes over \(U_a,U_b\), and identify their fibres at the distinguished points by a bijection of finite sets \(S\). In coordinate rings the joined scheme is

\[
\operatorname{Spec}(B_a\times_{k^S}B_b).
\tag{7.13}
\]

The maps to \(k^S\) are the fibre evaluations, with the stated bijection on the second one. This algebra is finite over \(R\): \(A_a\oplus A_b\) is finite over \(R\), each \(B_i\) is finite over \(A_i\), and their fibre-product algebra is a submodule of the resulting finite \(R\)-module. The ring \(R\) is Noetherian: \(A_a\oplus A_b\) is generated over \(R\) by \(1,(1,0)\), and the finite-subalgebra argument given explicitly in Example 7.14 makes \(R\) a finitely generated \(k\)-algebra. At each point above the join, the completed local ring is one copy of \(k[[u]]\times_k k[[v]]\); this follows from the splitting of each finite étale branch over its complete strictly henselian local ring. The same completion criterion just used proves étaleness at those points. Elsewhere it is inherited from \(D_a,D_b\). Thus (7.13) is finite étale over \(W\).

Here is also the branch pullback check. Let \(\mathfrak m_b\) be the distinguished-point ideal in \(A_b\). Projection of \(C=B_a\times_{k^S}B_b\) to \(B_a\) is onto, since \(B_b\to k^S\) is onto, and its kernel is \(0\oplus\mathfrak m_bB_b\). This kernel is \((0\oplus\mathfrak m_b)C\): lift the fibre value of each factor from \(B_b\) to \(B_a\) before multiplying by \(0\oplus\mathfrak m_b\). Thus \(C\otimes_RA_a=B_a\); the other branch is identical. Quotienting by both branch ideals gives \(k^S\), so the fibre at the join is exactly \(S\). Compatible maps glue uniquely by the fibre-product formula. This proves finite locally constant sheaf gluing, including its functoriality.

Choose an integral lattice in \(M_a\), and use \(\alpha\) to choose the lattice in \(M_b\). These particular lattices extend to integral local systems on pointed étale neighbourhoods \(U_a,U_b\): the lattice sheaf in Proposition 7.2 is classical, so a prescribed lattice germ extends on an étale neighbourhood. Remove any additional points lying above \(a\) or \(b\), and take affine neighbourhoods of the distinguished points. Now \(\alpha\) identifies the closed fibres of the two integral systems. Apply (7.13) to their finite reductions modulo a uniformizer to every power. Its functoriality glues the transition maps, the module operations and the strict reduction identities. Proposition 4.2, or its proof with that uniformizer, turns the resulting strict finite locally constant system on \(W\) into a free integral local system. Its rationalization is the desired local system near \(c\). The gluing equalizer commutes with the inverse limit because inverse limits commute with finite limits. It also commutes here with rationalization: on a quasi-compact affine test object the two branch systems can be tested on finitely many affine trivializing pieces, and one denominator bounds their finitely many coefficient matrices. Thus the rational branch equality is precisely the rationalization of the integral equalizer.

For a canonical global description, take \(\pi_*M\) on the pro-étale site and impose at \(c\) the equality of the two branch restrictions under \(\alpha\). In other words, define the equalizer sheaf

\[
L(M,\alpha)
=\{\,s\in\pi_*M:\ s_b=\alpha(s_a)
       \text{ on the inverse image of }c\,\}.
\tag{7.14}
\]

Restrictions to the branches are morphisms to the appropriate skyscraper coefficient sheaves; (7.14) is a sheaf equalizer, rather than a condition only on global sections. Finite pushforward in this formula commutes with étale restriction directly: its value on a test object is the value of \(M\) on that object's fibre product with \(Y\). On the étale chart \(W\), the finite gluing calculation and its compatible inverse limit identify (7.14) with the rationalized integral system constructed above. Off \(c\), (7.14) is \(M\). Hence it is locally free everywhere.

Its pullback to \(Y\) is \(M\): this is immediate off \(a,b\), and on \(U_a,U_b\) it is the branch identification in (7.13), passed to the compatible limit and rationalization. Its two pullback fibre maps at \(c\) have comparison \(\alpha\). Conversely, for a local system \(L\) on \(X\), pullback gives \(M\) and this fibre comparison. The natural map \(L\to L(M,\alpha)\) is an isomorphism. Check it on an affine pro-étale cover on which \(L\) is free and on the above étale chart: the finite gluing calculation identifies the constant system with the equalizer whose two branch values agree. The equality survives completion and rationalization. Thus the two constructions are inverse as sheaf constructions. A map of pairs respecting \(\alpha\) preserves (7.14); restriction to the branches determines every map of the glued systems by that equalizer. This proves the asserted equivalence on morphisms.

For algebraic \(E\), Proposition 7.12 defines \(M\) over one finite field. The finitely many entries of \(\alpha\) and its inverse lie in a larger finite field. Apply the finite-field construction there and extend scalars. The same proposition descends morphisms and their comparison equality to a finite field, proving the full gluing equivalence over \(E\). \(\square\)

### An explicit failure of the pro-discrete completion

The rational nodal example earlier only distinguishes \(\Pi\) from its profinite completion. The next example distinguishes it even from \(\Pi^{\mathrm{pd}}\). It is a direct variant of the gluing mechanism in Deligne's example recorded by Bhatt–Scholze, Example 7.4.9.

**Example 7.14 (Kummer monodromy and an expanding loop).** Let \(k\) be algebraically closed of characteristic different from \(\ell\). Choose \(q\in k^\times\setminus\{1\}\), put \(Y=\mathbb G_{m,k}\), and identify \(a=1\) and \(b=q\) to obtain \(X\). There is a rank-two \(\mathbb Q_\ell\)-local system on \(X\) whose representation of \(\Pi\) does not extend continuously to \(\Pi^{\mathrm{pd}}\).

**Construction and proof.** This particular pinched curve is affine. Set \(A=k[t,t^{-1}]\), \(I=(t-1)(t-q)A\), and

\[
B=\{f\in A:f(1)=f(q)\}=k+I,\qquad X=\operatorname{Spec}B.
\]

The inclusion \(B\subset A\) is finite. To see this without assuming the pinching, let \(d=(t-1)(t-q)\in B\) and \(z=dt^{-2}\in B\). The equations

\[
t^2-(1+q)t+(q-d)=0,\qquad
q(t^{-1})^2-(1+q)t^{-1}+(1-z)=0
\]

make both generators of \(A\) integral over \(B\); hence \(A\) is finite as a \(B\)-module. The elementary finite-subalgebra lemma also makes \(B\) finitely generated over \(k\): choose finite \(B\)-module generators of \(A\), put their multiplication coefficients and the coefficients expressing its finite \(k\)-algebra generators in a finitely generated \(k\)-subalgebra \(B_0\subset B\), including \(1\) among the module generators. Their \(B_0\)-span is closed under multiplication and contains the algebra generators, so it equals \(A\); hence \(A\) is a finite \(B_0\)-module. Then \(B\), a \(B_0\)-submodule of that finite module, is finite over the Noetherian ring \(B_0\). Thus \(X\) is a curve of finite type.

The ideal \(I\) is a conductor ideal, \(A/I=k\times k\), and \(B/I=k\) maps diagonally. Off \(I\) the rings agree: after inverting \(d\), every element of \(A\) is \(d^{-1}\) times an element of \(I\). At the single point defined by \(I\), completion of the finite conductor square gives

\[
\widehat B_I
=k[[t-1]]\times_k k[[t-q]].
\]

Indeed the completion of \(A\) over that point is the product of its two branch completions, and its quotient by the completed conductor is \(k\times k\); the defining equal-value condition persists because completion is exact on finite modules over a Noetherian ring. This proves the claimed node and verifies all hypotheses of Proposition 7.13.

Choose compatible primitive \(\ell^n\)-th roots of unity in \(k\). The covers

\[
Y_n=\operatorname{Spec}k[s,s^{-1}]
\longrightarrow Y,\qquad t=s^{\ell^n},
\]

are connected finite étale torsors for \(\mu_{\ell^n}\): the derivative is a unit on \(Y_n\), the Laurent polynomial algebra is free of rank \(\ell^n\) over \(A\), and the root-of-unity translations act simply transitively on each geometric fibre. Compatible choices of a point in their fibres identify the inverse-limit quotient of \(\pi_1^{\acute et}(Y)\) with \(\mathbb Z_\ell\). The map

\[
\tau:\pi_1^{\acute et}(Y)\twoheadrightarrow\mathbb Z_\ell
\]

is surjective. Its image is compact, hence closed, and it maps onto every finite quotient by connectedness of \(Y_n\); it is consequently also dense.

Put

\[
u(z)=\begin{pmatrix}1&z\\0&1\end{pmatrix},\qquad
T=\begin{pmatrix}\ell&0\\0&1\end{pmatrix}.
\]

The continuous integral representation \(g\mapsto u(\tau(g))\) gives a rank-two local system \(M\) on \(Y\). This uses the finite reductions and completion already proved in Theorem 7.10. Choose paths from a base point \(x\in Y\setminus\{a,b\}\) to \(a,b\), supplied by Lemma 7.8a, and use them to identify the two fibres with the fibre at \(x\). Glue them by \(T\), using Proposition 7.13. Let \(\rho:\Pi\to\mathrm{GL}_2(\mathbb Q_\ell)\) be the resulting representation. Pullback along \(Y\to X\) has action \(u\circ\tau\). The two branch paths through \(c\) give a loop \(\lambda\in\Pi\); choose its orientation so that \(\rho(\lambda)=T\). This is exactly the fibre comparison in (7.14).

Suppose \(\rho\) extended continuously to \(\Pi^{\mathrm{pd}}\). The inverse image of \(\mathrm{GL}_2(\mathbb Z_\ell)\) in that inverse limit is an open subgroup. A basic identity neighbourhood is the kernel of finitely many discrete quotient projections; the intersection of their open normal kernels is again an open normal kernel. Its pullback gives an open normal subgroup

\[
N\triangleleft\Pi,\qquad
N\subset\rho^{-1}\bigl(\mathrm{GL}_2(\mathbb Z_\ell)\bigr).
\]

The pullback \(K\) of \(N\) to the profinite group \(\pi_1^{\acute et}(Y)\) is open and has finite index. Therefore \(\tau(K)\) has finite index in \(\mathbb Z_\ell\), since it is the image of a finite-index subgroup under the surjection \(\tau\). In particular some \(g\in K\) has \(\tau(g)=z\ne0\). Its image in \(\Pi\) belongs to \(N\). Normality now puts all \(\lambda^{-m}g\lambda^m\), for \(m\geq0\), in \(N\), while

\[
\rho(\lambda^{-m}g\lambda^m)
=T^{-m}u(z)T^m
=u(\ell^{-m}z).
\tag{7.15}
\]

For \(m>v_\ell(z)\) this matrix does not belong to \(\mathrm{GL}_2(\mathbb Z_\ell)\), a contradiction. Thus the extension does not exist. The argument requires neither surjectivity of \(\rho\) onto a full matrix group nor a claim that the image of an open normal subgroup is closed. It supplies a concrete locally free sheaf on the nodal scheme, together with the exact obstruction to its proposed pro-discrete classification. \(\square\)

## 8. Exercises and complete solutions

**Exercise 8.1 (first check).** Prove that an étale morphism is weakly étale, and that base change preserves weakly étale morphisms.

**Solution.** An étale morphism is flat and its diagonal is an open immersion, hence flat. Under a base change, both the morphism and its diagonal are base changes of the original ones; flatness is preserved under base change. These two observations prove both assertions. ∎

**Exercise 8.2 (finite-field comparison).** Compute \(H^0\) and \(H^1\) of \(\widehat O\) on \(\operatorname{Spec}(\mathbb F_q)_{\mathrm{pro\acute et}}\), assuming \(\ell\neq\operatorname{char}\mathbb F_q\), and identify their maps to the limits of the finite-coefficient groups.

**Solution.** Finite-coefficient degree zero is \(O_n\). A degree-one class is a continuous additive character of \(\widehat{\mathbb Z}\); it is determined by the image of arithmetic Frobenius, any element of \(O_n\). Thus degree one is also \(O_n\), and transitions in both degrees are reduction. Formula (5.1) in degree zero has no negative cohomology term. In degree one its left term is \(\varprojlim{}^1O_n=0\), because the degree-zero transitions are onto. Hence both groups are \(O\). In degree one the limit map sends a class to its compatible finite characters, or equivalently to their compatible Frobenius values. This identifies it with \(\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbb Z},O)\). ∎

**Exercise 8.3 (full faithfulness for sets).** Using only the adjunction and its unit in Proposition 3.1, prove that every map \(\nu^{-1}F\to\nu^{-1}G\) of sheaves of sets comes uniquely from a map \(F\to G\).

**Solution.** Adjunction identifies its Hom set with \(\operatorname{Hom}(F,\nu_*\nu^{-1}G)\). The unit identifies the target with \(G\), giving \(\operatorname{Hom}(F,G)\). This bijection sends \(u:F\to G\) to \(\nu^{-1}u\), by the triangle identity. Thus existence and uniqueness both follow. No additive structure was used. ∎

**Exercise 8.4 (compatible infinite equations).** On a replete topos, let \(A_{n+1}\twoheadrightarrow A_n\) be a tower of abelian sheaves. Prove concentration of \(R\varprojlim A_n\) in degree zero by constructing local solutions of \(x_n-f_n(x_{n+1})=b_n\).

**Solution.** A partial solution of length \(r\) extends locally by lifting \(x_r-b_r\) through \(f_r\). Thus the sheaves of partial solutions form an epimorphism tower. Its first term has the zero section, and repleteness lifts that section to an infinite compatible partial-solution sequence locally. This is a full solution. Therefore \(1-s\) in (2.1) is onto. Its kernel is the inverse limit, so the two-term complex has only degree-zero cohomology. Exact countable products, established in Theorem 2.2 from repleteness, justify use of this complex for the derived limit. ∎

**Exercise 8.5 (torsion diagnostic).** Let \(F=\underline{O/\ell^2O}\). Compute the cohomology sheaves of \(F\otimes_O^{\mathbf L}O_n\) for \(n=1\) and \(n=3\). Does the ordinary strict system \(F/\ell^nF\) satisfy derived compatibility over the rings \(O_n\)?

**Solution.** The reduction is \([F\xrightarrow{\ell^n}F]\) in degrees \(-1,0\). For \(n=1\), its kernel is \(\ell F\simeq O_1\) and its cokernel is \(F/\ell F\simeq O_1\). For \(n=3\), the differential is zero, so both groups are \(F\). The ordinary quotients are \(O_1,O_2,O_2,\ldots\). They satisfy ordinary strictness. They cannot satisfy derived compatibility at every level: otherwise Proposition 4.3 would identify the first derived reduction of their limit \(F\) with \(O_1\) in degree zero, contradicting the nonzero degree-minus-one group just computed. ∎

**Exercise 8.6 (what completion tests).** Let \(K\) be a derived complete \(O\)-complex. Prove that \(K\otimes_O^{\mathbf L}O_1=0\) implies \(K=0\), and explain its use in §5.

**Solution.** Tensor the coefficient sequence \(0\to O_{n-1}\xrightarrow{\ell}O_n\to O_1\to0\) with \(K\). Induction makes every \(K\otimes_O^{\mathbf L}O_n\) zero. Completeness identifies \(K\) with their derived limit, so \(K=0\). Apply this to the complete cone of the compatible map \(\widehat{\underline P}\to K\). Its first reduction is zero because that map is an isomorphism modulo \(\ell\); hence its cone vanishes and the map is an isomorphism. The completeness hypothesis is essential: the \(O\)-module \(O[1/\ell]\) has zero reduction modulo \(\ell\) but is nonzero. ∎

**Exercise 8.7 (why strict local rings alone do not split covers).** Let \(k\) be separably closed and \(P=\mathbb Z_2\). Put \(R=C(P,k)\), the locally constant \(k\)-valued functions, with \(k\) discrete. Show that every local ring of \(R\) is \(k\), but that there is a faithfully flat ind-Zariski \(R\)-algebra with no retraction.

**Solution.** Finite clopen partitions give \(R=\varinjlim k^{P_i}\), with spectrum \(P\) and all local rings \(k\). Let \(U\) be the nonzero 2-adic integers of even valuation. Its closure is \(U\cup\{0\}\), which is not open: every neighborhood of zero also contains elements of arbitrarily large odd valuation. The profinite space \(T=\overline U\amalg(P\setminus U)\) surjects onto \(P\). Lemma 1.1b realizes it by a faithfully flat ind-Zariski algebra, here \(C(T,k)\). A retraction would give a continuous section \(P\to T\). The preimage of the first, clopen component would be a clopen subset \(V\) of \(P\), containing \(U\) and contained in \(\overline U\). Since \(V\) is closed, it must equal \(\overline U\), contradicting the latter's failure to be open. Thus the cover has no retraction. Extremal disconnectedness in Theorem 1.1f does necessary work even when all local rings already are strictly henselian fields.

**Exercise 8.8 (an infinite coproduct changes the topology of trivialization).** On \(X=\operatorname{Spec}\mathbb F_q\), let \(S_m=\mathbb Z/\ell^m\mathbb Z\) with the translation action of \(\widehat{\mathbb Z}\). Each associated finite sheaf is étale locally constant. Show that their coproduct is pro-étale locally constant but is not étale locally constant.

**Solution.** The profinite group is Noohi, and Corollary 7.11 identifies it with the refined group of this field. Theorem 7.8 associates the discrete continuous action on \(S=\coprod_{m\geq1}S_m\) to a pro-étale local system; continuity is pointwise because each point stabilizer contains \(\ell^m\widehat{\mathbb Z}\). Its kernel on the whole set is \(\bigcap_m\ell^m\widehat{\mathbb Z}\), whose \(\mathbb Z_\ell\)-coordinate is zero. This subgroup is not open: every open neighbourhood of 0 has a nonzero \(\ell\)-adic element. Proposition 7.9 therefore excludes an étale trivialization of the entire coproduct. This gives a concrete reason to distinguish all pro-étale local systems from the étale locally constant subcategory, even over a field.

## Proof scope and dependencies

Section 1 proves the ind-étale refinement theorem and existence of w-contractible affine covers, including Olivier's local rigidity theorem and the projective component-space argument. Its arbitrary-ring henselian criteria and valuation domination have the exact internal providers identified there. Étale fpqc descent and continuity [Tags 03Q6 and 09YQ], the finite-coefficient constant-complex local-structure theorem [Tag 09BI], and torsion proper base change, proper constructibility and the proper cohomological-dimension bound. Hilbert 90 and the cohomological-dimension-one calculation for finite fields enter the examples.

The proofs here establish the affine ind-étale basis and enough w-contractible covers, comparison for all abelian étale sheaves, the replete-limit lemma, strict-system reduction, and the derived-completion formula for arbitrary complexes over a Noetherian ring. They establish proper base change both under the explicit hypotheses of Theorem 6.1 and for the general constructible coefficients of Theorem 6.3; the latter proof does not require the coefficient quotients to be perfect. Section 7 proves full faithfulness of rationalization, étale-local existence of lattices and the failure of a global lattice on a nodal curve. Theorems 7.5d–7.11 prove the geometric-covering equivalence, complete Noohi and tame infinite Galois reconstruction, valuation paths and the set of connected generators, the finite and pro-discrete completion comparisons, and the representation classification for finite extensions of \(\mathbb Q_\ell\). They also recover the usual profinite group and global integral lattices on geometrically unibranch bases. Lemmas 7.6c–7.6f prove countability, the coefficient groups' Noohi property and left completeness, and the finite-stage property for compact coefficient data. Proposition 7.12 proves finite scalar descent on quasi-compact quasi-separated schemes. Lemma 7.12a supplies simultaneous natural local fibre identifications, and Theorem 7.12b proves the full rational and integral algebraic-coefficient representation classifications on connected locally topologically Noetherian bases, including singular and non-qcqs bases. It constructs the actual coset-limit frame torsor, proves local inhabitation, supplies local finite fields and lattices, and checks all linear morphisms and gluing. On qcqs bases it deduces a global finite field of definition for every continuous representation. Proposition 7.13 proves normalization gluing on a curve with one node, including the fibre comparisons and morphisms. Example 7.14 gives a Kummer local system which fails even pro-discrete classification. The algebraic-space quotient and recognition arguments have the exact internal providers AG-AS-01, Theorem 2.2, and AG-AS-02, Appendix B; those providers retain their stated scheme-descent prerequisites. A full six-operations and duality theory remains a further proof scope.

## References

- **[Stacks, Pro-étale Cohomology]** The Stacks Project, *Pro-étale Cohomology*. The chapter is available in the [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/proetale.html), an unofficial edition with AI-proposed corrections and additions. The [official Stacks Project](https://stacks.math.columbia.edu/) is the upstream reference. Relevant sections and labels are [comparison](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/proetale.html#proetale-section-comparison), [completed coefficients](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/proetale.html#proetale-section-derived-completion-proetale), [the constructible derived category](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/proetale.html#proetale-definition-Dbc), and [proper base change](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/proetale.html#proetale-theorem-proper-base-change). Tags 0966, 097H, 097Y–097Z, 0980, 0983, 0988, 099L, 099P–099R, 09AI, 09BS, 09C0, 09C7–09C9 and 0F4N locate the constructions used here.
- **[Stacks, Étale Cohomology]** The same project, *Étale Cohomology* and *Cohomology on Sites*: continuity, Čech acyclicity, constant perfect complexes, and torsion proper base change at the tags specified in the text.
- **[Bhatt–Scholze]** B. Bhatt and P. Scholze, *The pro-étale topology for schemes*, [arXiv:1309.1198](https://arxiv.org/abs/1309.1198), version 2. Sections 4–6 develop the site, étale comparison and constructible categories; §6.7 proves base change for general constructible coefficients. Sections 6.8 and 7 explain local lattices and the refined fundamental group. This lesson develops Noetherian completion, finite-free approximation, covering and Noohi reconstruction, the generator bound, finite-extension representation classification, algebraic coefficient topology and nodal examples. Lemma 7.6f and Proposition 7.12 compare with [Lemma 4.3.7](https://arxiv.org/html/1309.1198v2#S4.SS3.Thmtheorem7) and [Proposition 6.8.4](https://arxiv.org/html/1309.1198v2#S6.SS8.Thmtheorem4); the latter's proof is supplied here also for rational local systems. Normalization gluing and Example 7.14 develop the mechanism of [Deligne's example, 7.4.9](https://arxiv.org/html/1309.1198v2#S7.SS4.Thmtheorem9), using an explicit Kummer tower and diagonal conjugation. The finite-power embedding assertion in v2 Example 7.1.2 is replaced by its valid quotient argument; Proposition 7.1.5 uses coset-set permutation factors. The topology claim in Lemma 6.6.10 is stated locally for arbitrary étale schemes and globally under quasi-compactness.
- **[Derived truncation and limits]** The AI Integrated Stacks Project's [finite-degree truncation argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/ai-integrated/candidates/commons/stacks/errata/r61/evidence/review/PROOFS_12380_12604.md) and [exact-product limit argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/ai-integrated/candidates/commons/stacks/errata/r61/evidence/review/PROOFS_10435_10686.md) make the two distinct steps in §6 explicit. These editorial proofs are attributed to OpenAI Codex, GPT-6 Astra, Ultra, and preserve the human Stacks authors' credit and the source's GNU FDL terms.

- **[Olivier and covering geometry]** Olivier's local rigidity theorem appears in the AI Integrated Stacks Project [More on Algebra, weakly étale ring maps](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L30859), through Theorem `theorem-olivier`; the upstream locator is [Tag 092Z](https://stacks.math.columbia.edu/tag/092Z). The w-local, ind-Zariski and ind-étale constructions are in the same revision's [proetale chapter](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/proetale.tex), §§2–11. The projective compact-space argument is attributed there to Gleason and Rainwater and appears in [Topology, extremally disconnected spaces](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/topology.tex#L5407). These human source texts retain GNU FDL 1.2 or later. Section 1 proves the covering theorems, including the valuation-product and pure-quotient steps.
