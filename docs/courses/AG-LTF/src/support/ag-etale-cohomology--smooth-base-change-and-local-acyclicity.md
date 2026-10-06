# Smooth base change and local acyclicity

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

A class on a fibre need not extend to nearby fibres. Properness and smoothness control different parts of this problem. Proper base change computes the stalk of a higher direct image from a whole fibre. Smooth base change compares neighbourhoods after a smooth change of base, even when the direct-image morphism is not proper. Combining the two makes the cohomology of a proper smooth family a local system, provided the coefficients are finite and their orders avoid the residue characteristics.

We first prove smooth base change by an effacement argument on affine curves. We then use that theorem to examine the small geometric fibres of strict localizations. This yields universal local acyclicity, canonical cospecialization maps and the specialization theorem. A nodal degeneration at the end shows precisely what can go wrong.

The prerequisites are Pushforward, pullback and finite morphisms, Constructible sheaves and extension by zero, Torsion sheaves on curves, The proper base change theorem, and the constructibility theorem stated at its exact scope in Cohomology with compact support. All cohomology is étale cohomology. The geometric prerequisites about smooth morphisms are specified below; no smooth base change or local acyclicity theorem is assumed.

## 1. Which morphism is smooth?

Our square is

\[
\begin{matrix}
Y=X\times_S T&\xrightarrow{e}&T\\
h\downarrow&&\downarrow g\\
X&\xrightarrow{f}&S.
\end{matrix}
\tag{1.1}
\]

Here \(f\) is the change of base and \(g\) is the morphism whose higher direct images we compare. Thus the hypothesis is **\(f\) smooth**, with **\(g\) quasi-compact and quasi-separated**. The canonical comparison is

\[
\beta_{g,f}(E):f^{-1}Rg_*E\longrightarrow Rh_*e^{-1}E.
\tag{1.2}
\]

As in the previous lesson, it comes from the degree-zero adjunction map and resolutions. Exact inverse image makes it a map of cohomological functors. Adjunction units show that it commutes with connecting homomorphisms, étale localization, successive base changes and composition of direct images. These compatibilities concern the actual comparison, not merely an isomorphism between two groups of the same size.

**Theorem 1.1 (smooth base change).** In (1.1), suppose \(f\) is smooth and \(g\) is quasi-compact and quasi-separated. Let \(F\) be an abelian sheaf on \(T\) whose stalks are torsion of orders invertible on \(S\). Then

\[
f^{-1}R^qg_*F\xrightarrow{\sim}R^qh_*e^{-1}F
\qquad(q\geq0).
\tag{1.3}
\]

“Orders invertible on \(S\)” means that each germ is killed by a positive integer which is a unit on \(S\). In particular, \(nF=0\) with \(n\) invertible on \(S\) suffices. A common annihilator is unnecessary. On a mixed-characteristic base, the coefficient condition must be checked; a torsion sheaf is not automatically admissible. Later, for a locally constant sheaf near a fixed geometric point, we work on a strict local base, where an integer prime to the closed residue characteristic is a unit everywhere.

The theorem also holds for \(E\in D^+(T_{\mathrm{ét}})\) whose cohomology sheaves satisfy this coefficient condition. Section 7 proves that extension. The proof of (1.3) occupies Sections 2–6.

## 2. Degree zero and the geometric inputs

We use these geometric facts about smooth morphisms.

* A smooth morphism is flat and locally of finite presentation. Étale-locally it admits an étale map to affine space over the base. Smoothness is preserved by base change and composition.
* A smooth \(X\to S\) has an étale covering by affine \(U\)'s factoring through an affine étale \(V\to S\), with \(U\to V\) smooth, geometrically connected fibres and a section. To obtain this form, use a separable closed point in a fibre, an étale slice through it, and the open connected component along the resulting section. A nonempty open of a connected smooth geometric fibre is connected: that fibre is regular, so its connected components are irreducible.
* Finite-presentation schemes, morphisms, sections, finite étale covers and their finite group actions descend along affine inverse limits. Smoothness and properness hold at a sufficiently late stage when they hold on the limit. Finite locally constant sheaves of finitely presented modules descend by a finite trivializing covering and its descent data.
* Schemes of finite type over \(\mathbf Z\) are Nagata. Their normalizations in finite extensions of function fields are finite. Normalizing the closure of the image of a map from a normal integral scheme gives the factorization used in Section 5.

These are prerequisites from algebraic geometry, rather than cohomological assertions. The local forms and their proofs are recorded in the [smooth covering lemma](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-cover-smooth-by-special). The finite-cover extension theorem needed in Section 5 is stated there separately, with all of its hypotheses.

**Lemma 2.1 (sections along connected fibres).** Let \(a:U\to V\) be flat and quasi-compact, with nonempty geometrically connected fibres. For every étale sheaf of sets \(A\) on \(V\), the adjunction map gives

\[
\Gamma(V,A)\xrightarrow{\sim}\Gamma(U,a^{-1}A).
\tag{2.1}
\]

*Proof.* The map is injective because the surjective \(a\) detects equality on geometric stalks. For surjectivity take a section \(b\) upstairs. Étale sheaves, and their sections, have faithfully flat descent, so it suffices to compare the two pullbacks of \(b\) on \(U\times_V U\). Over a geometric point \(\bar v\) the coefficient sheaf is constant with value \(A_{\bar v}\). A section on the connected \(U_{\bar v}\) has a single value in this set. Both pullbacks therefore have that same value. Every geometric point of \(U\times_V U\) lies in such a fibre, so the two sections agree. They descend uniquely. □

**Proposition 2.2 (degree-zero smooth base change).** If \(f\) is smooth, the map \(f^{-1}g_*F\to h_*e^{-1}F\) is an isomorphism for every sheaf of sets \(F\).

*Proof.* It suffices to check on an étale covering of each object of \(X_{\mathrm{ét}}\). By the smooth local form just stated, such a covering consists of \(U\to X\) with a factorization \(U\xrightarrow{a}V\to S\), where \(V\to S\) is étale and \(a\) is flat and quasi-compact with geometrically connected fibres. Restrictions of inverse images and direct images to these localized sites have their usual meaning. Lemma 2.1, first for \(a\) and then for its base change to \(V\times_S T\), gives

\[
\begin{aligned}
\Gamma(U,f^{-1}g_*F)
&=\Gamma(V,g_*F)\\
&=\Gamma(V\times_S T,F)\\
&=\Gamma(U\times_S T,e^{-1}F)\\
&=\Gamma(U,h_*e^{-1}F).
\end{aligned}
\tag{2.2}
\]

The equalities are induced by pullback of sections, so the resulting map is the adjunction comparison. They hold on a covering basis and thus identify the sheaves. No torsion hypothesis was used. □

The same argument works for a flat morphism whose étale objects locally have the connected-fibre factorization. In particular, when the maps on strict localizations are flat with geometrically connected fibres, comparison on a stalk reduces to Lemma 2.1 for the corresponding base-changed strict local schemes. This explains the degree-zero criterion often used alongside smooth base change.

## 3. A class on an affine curve can be killed

The curve theorem from lesson 12 supplies two facts for coefficients of order prime to the characteristic: positive cohomology above degree one vanishes on a smooth affine curve over a separably closed field, and the canonical degree-one comparison is invariant under extensions of separably closed fields. Both facts were proved there without smooth base change.

**Lemma 3.1 (pointed curve effacement).** Let \(K/k\) be a field extension. Let \(C\) be a geometrically connected smooth affine curve over \(k\), with \(x\in C(k)\). Suppose \(M\) is an étale abelian sheaf on \(\operatorname{Spec}K\), killed by an integer \(n\) invertible in \(k\). For \(q>0\) and

\[
\xi\in H^q(C_K,M|_{C_K}),
\]

there are finite extensions \(k'/k\), \(K'/K\), with compatible embeddings \(k'\subset K'\), and a finite étale Galois cover \(D\to C_{k'}\) such that:

* its group has order dividing a power of \(n\);
* it splits over \(x_{k'}\);
* the pullback of \(\xi\) to \(D_{K'}\) is zero.

*Proof.* Choose compatible algebraic closures \(\bar k\subset\bar K\). If \(q>1\), the class restricts to zero on \(C_{\bar K}\) by the affine-curve theorem. Continuity then kills it over a finite extension \(K'/K\); take \(k'=k\) and the identity cover.

For \(q=1\), the sheaf on \(K\) is a discrete continuous Galois module. Each element has a finite Galois orbit. A finite collection of such orbits generates a finite subgroup because the module is killed by \(n\). Thus the module is the filtered union of finite Galois-stable subgroups. Cohomology commutes with that union on the quasi-compact, quasi-separated curve. The class comes from a finite subgroup, whose action becomes trivial over a finite separable extension of \(K\). It remains to kill a class with constant finite abelian coefficient group.

Write that group as a finite direct sum of cyclic groups \(\mathbf Z/d\), \(d\mid n\). Treat their finitely many classes successively. For one cyclic group, the class on \(C_{\bar K}\) is the pullback of a class on \(C_{\bar k}\), by the canonical curve invariance theorem. Its torsor \(P\to C_{\bar k}\) is finite étale. A connected component \(D_0\) is a Galois cover whose group is the stabilizer of that component in \(\mathbf Z/d\). To see this, the group permutes the components transitively, and the stabilizer acts simply transitively on the fibre of \(D_0\); each component surjects onto the connected base. Its order divides \(d\). Pulling the torsor back to \(D_0\) gives a section, so the class dies.

Descend the finite cover, its action and the torsor comparison to a finite extension \(k'/k\). Enlarge \(k'\) until a point above \(x\) is rational. The group action then splits the whole fibre above \(x_{k'}\). The class dies after pullback over \(\bar K\); continuity supplies a finite \(K'/K\) containing the image of \(k'\) where it already dies. For several cyclic factors, take a connected component of the fibre product of their covers after common finite field extensions. Its Galois group is a subgroup of the product of their groups, so its order divides a power of \(n\). A tuple of the chosen rational points retains the splitting over \(x\). All the original classes die on this refinement. □

The rational point is useful. It removes a constant-field obstruction to extending the generic cover over the base of a smooth family.

## 4. Reduce the theorem to injectives over finite models

We prove (1.3) by induction on \(q\). Degree zero is Proposition 2.2. Assume all degrees below \(q>0\) are known for every smooth change of base.

First reduce to a common annihilator. For positive integers \(n\) invertible on \(S\), ordered by divisibility, the subsheaves \(F[n]\) have filtered colimit \(F\). Both inverse-image functors commute with colimits. Higher direct images along the quasi-compact, quasi-separated \(g\) and \(h\) commute with filtered colimits by lesson 7. It therefore suffices to work with \(\mathbf Z/n\)-sheaves, for a fixed \(n\) invertible on \(S\). The case \(n=1\) is zero; assume \(n>1\).

The problem is étale-local on \(X\) and \(S\). In smooth local coordinates we factor through \(\mathbf A^r_S\). Étale change of base is formal localization. Write the projection from affine space as a succession of relative affine lines, and paste the canonical comparisons. It is enough to handle a smooth affine morphism \(X\to S\) of relative dimension one, with \(S\) affine.

Next reduce to affine \(T\). Over affine \(S\), a quasi-compact, quasi-separated \(T\) has a finite affine covering; intersections have finite affine coverings. The relative Mayer–Vietoris triangle for \(T=W\cup W'\) compares, on both sides of (1.2), the direct images from \(W\), \(W'\), and \(W\cap W'\). The five consecutive terms ending with the degree-\(q\) image from \(W\cap W'\) show that degree-\(q\) comparison on these three schemes, together with the already known lower-degree comparisons, proves it on \(T\). No degree-\(q+1\) result is needed. Induction on a finite affine covering, first for quasi-compact opens of an affine scheme and then for a general finite affine covering, proves the reduction. Since \(X,S,T\) are affine, so is \(Y\).

**Lemma 4.1 (injective test in degree \(q\)).** Under the induction hypothesis, it suffices to prove

\[
R^qh_*e^{-1}I=0
\tag{4.1}
\]

for every injective \(\mathbf Z/n\)-sheaf \(I\) on \(T\).

*Proof.* Embed \(F\) in an injective \(I\), and let \(Q=I/F\). Compare the exact sequences

\[
f^{-1}R^{q-1}g_*I\longrightarrow f^{-1}R^{q-1}g_*Q
\longrightarrow f^{-1}R^qg_*F\longrightarrow0
\]

and

\[
R^{q-1}h_*e^{-1}I\longrightarrow R^{q-1}h_*e^{-1}Q
\longrightarrow R^qh_*e^{-1}F\longrightarrow R^qh_*e^{-1}I.
\]

The first two vertical maps are isomorphisms by induction. If (4.1) holds, the two cokernels coincide under the canonical map. This proves degree \(q\). Cohomology of module injectives computes the underlying abelian-sheaf direct images, as proved in lesson 12. □

**Lemma 4.2 (finite-model reduction).** For (4.1), we may assume \(S\) and \(T\) are affine of finite type over \(\mathbf Z[1/n]\).

*Proof.* Write \(S=\operatorname{Spec}A\), \(T=\operatorname{Spec}B\). The map \(A\to B\) is a filtered colimit of maps \(A_i\to B_i\) between finite-type \(\mathbf Z[1/n]\)-algebras. Include finitely many coefficients defining the smooth affine curve and descend it to smooth affine curves \(X_i\to S_i\) of relative dimension one. Set \(Y_i=X_i\times_{S_i}T_i\).

For \(\pi_i:T\to T_i\), the sheaf \(I_i=\pi_{i,*}I\) is injective: its left adjoint \(\pi_i^{-1}\) is exact. Moreover

\[
I=\varinjlim_i\pi_i^{-1}I_i.
\tag{4.2}
\]

One can check this equality on a basis of finitely presented étale objects: an object and a finite compatibility condition descend to a stage, and the adjunction maps recover its sections after passage to the limit. Equivalently, the stalk computation is the filtered system of these descended pointed objects. This works for arbitrary sheaves, not just constructible ones.

Apply exact inverse image and continuity for the inverse system of quasi-compact, quasi-separated morphisms \(Y_i\to X_i\). It gives

\[
R^qh_*e^{-1}I
=\varinjlim_i(X\to X_i)^{-1}R^qh_{i,*}e_i^{-1}I_i.
\tag{4.3}
\]

Thus vanishing for the finite models implies vanishing for the original square. This limit argument uses the continuity theorem from lesson 7; it does not assume smooth base change. □

## 5. Make a generic class vanish

We now have affine finite-type \(\mathbf Z[1/n]\)-schemes \(S,T\), an affine smooth relative curve \(X\to S\), and an injective \(I\) on \(T\). We prove (4.1) by induction on \(d=\dim T\), beginning with the empty scheme.

A local section of \(R^qh_*e^{-1}I\), after an étale covering of \(X\), is represented by

\[
\xi\in H^q(Y,e^{-1}I).
\tag{5.1}
\]

This is the description of a higher direct image as the sheafification of the cohomology presheaf. It is enough to kill this representative on an étale covering of \(X\). The smooth local form of Section 2 lets us replace \(X\) and an étale neighbourhood of \(S\) until \(X\to S\) has a section and geometrically connected fibres. The corresponding étale replacement of \(T\) has dimension at most \(d\). We still have an affine smooth relative curve.

Two finite replacements are legitimate.

**Lemma 5.1 (finite replacements).** We may replace \(T\) by a finite surjective \(\pi:T'\to T\), replacing \(I\) by an injective containing \(\pi^{-1}I\). We may also replace \(S\) by a finite \(S'\to S\) through which \(T\to S\) factors.

*Proof.* For the first replacement choose \(\pi^{-1}I\hookrightarrow I'\). The adjoint \(I\to\pi_*I'\) is injective because \(\pi\) is surjective and inverse image detects this on stalks. It splits because \(I\) is injective. Finite direct image is exact and commutes with arbitrary base change by lesson 7. For \(\pi':Y'=Y\times_T T'\to Y\) we get

\[
R\pi'_*e'^{-1}I'=e^{-1}\pi_*I'.
\tag{5.2}
\]

Hence \(H^q(Y,e^{-1}I)\) is a direct summand of \(H^q(Y',e'^{-1}I')\), and this remains true after every étale localization on \(X\). Killing the latter class kills the former. A finite map does not increase dimension.

For the second replacement, put \(X'=X\times_S S'\). The map \(X'\to X\) is finite and \(h\) factors as \(Y\to X'\to X\). Exact finite direct image and Leray identify \(R^qh_*e^{-1}I\) with the finite direct image of the corresponding sheaf on \(X'\). Vanishing of that sheaf proves vanishing on \(X\). Sections and geometrically connected fibres of \(X\to S\) survive this base change. □

Reduce and normalize \(T\), using the first replacement. Normalize the closure of its image in \(S\) inside its function field, using the second replacement. Finiteness follows from the Nagata property. Work on one component at a time. We may assume \(T\to S\) is dominant and both schemes are normal and integral. Let \(t,s\) be their generic points.

Apply Lemma 3.1 to the class on the generic curve \(Y_t\), with coefficient \(I|_t\) and the rational point supplied by the section. Normalize \(T\) and \(S\) in the resulting finite field extensions. Lemma 5.1 again permits these replacements. The class now dies on a finite étale Galois cover \(D\to X_s\), whose group order divides a power of \(n\), split along the generic point of the section.

Here we use a theorem of finite-cover geometry:

**Geometric cover extension.** If \(S\) is normal integral Noetherian, \(X\to S\) is smooth with geometrically connected fibres and a section \(\sigma\), and \(D\to X_s\) is a finite étale Galois cover of group order invertible on \(S\), split over \(\sigma(s)\), then \(D\) extends to a finite étale Galois cover \(U\to X\).

The [full geometric proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-extend-covering) uses tame ramification, purity for finite covers and depth-two extension. Over a discrete valuation base, splitting along the section kills the tame ramification along the irreducible special fibre; purity extends the cover. In higher base dimension, extend across a maximal punctured local base by the depth-two finite-algebra construction. Near the section the completion is \(A[[z_1,\ldots,z_r]]\). A cover split along the section is split on the punctured formal neighbourhood by the finite-cover extension theorem for power series over a depth-two normal local ring. It is therefore étale at the generic point of the special fibre; the smooth depth-two purity criterion makes it étale throughout. Descent from the local base contradicts maximality of the open where extension existed. This is an exact geometric prerequisite, including the section, splitting and invertible group-order conditions. No cohomological base change result is part of it.

Replace \(X\) by this finite étale covering \(U\), and \(Y\) accordingly. The representative \(\xi\) vanishes on \(Y_t\). We no longer need connected fibres or the section. The generic point is the inverse limit of nonempty affine opens of \(T\). Continuity gives a nonempty open \(V\subset T\) such that

\[
\xi|_{Y_V}=0.
\tag{5.3}
\]

The remaining work is supported over the smaller-dimensional complement.

## 6. Finish the induction and the theorem

Let \(Z=T\setminus V\), with its reduced closed structure. Write \(j:V\hookrightarrow T\), \(i:Z\hookrightarrow T\), and \(j',i'\) for their inverse images in \(Y\). Embed \(i^{-1}I\) in an injective \(J\) on \(Z\). The adjunction maps give

\[
I\hookrightarrow j_*I|_V\oplus i_*J.
\tag{6.1}
\]

It is a monomorphism: on \(V\) its first component is the identity, and on \(Z\) its second component is the chosen embedding. Since \(I\) is injective, (6.1) splits. Therefore it suffices to kill the images of \(\xi\) with coefficients in the two summands after inverse image to \(Y\).

The map \(e:Y\to T\) is smooth. Degree-zero smooth base change, applied to \(e\) and \(j\), and finite base change for \(i\), yield

\[
e^{-1}j_*I|_V=j'_*e_V^{-1}I|_V,
\qquad
e^{-1}i_*J=i'_*e_Z^{-1}J.
\tag{6.2}
\]

Restriction of an injective to an open is injective, because extension by zero is an exact left adjoint. Thus \(I|_V\) is injective. By the induction on cohomological degree, applied to the smooth change of base \(e\),

\[
R^aj'_*e_V^{-1}I|_V=e^{-1}R^aj_*I|_V=0
\quad(1\leq a<q).
\tag{6.3}
\]

The last equality follows because direct image of an injective is acyclic. In the Leray spectral sequence for \(j'\), no differential can enter \(E_r^{q,0}\): its possible source has second index \(r-1\), which is either between \(1\) and \(q-1\) and zero by (6.3), or has negative first index. No differential leaves that term. Its edge map is therefore injective:

\[
H^q(Y,j'_*e_V^{-1}I|_V)
\hookrightarrow H^q(Y_V,e_V^{-1}I|_V).
\tag{6.4}
\]

By (5.3) the image of our class in the right side is zero, so its image in the first summand of (6.1) is zero already.

For the closed summand, exact finite direct image gives

\[
H^q(Y,i'_*e_Z^{-1}J)=H^q(Y_Z,e_Z^{-1}J).
\tag{6.5}
\]

The morphism \(Z\to S\) is affine of finite type over \(\mathbf Z[1/n]\), and \(\dim Z<d\). The induction on dimension, applied to the square with \(Z\) in place of \(T\), says that the corresponding \(R^q\) vanishes. Consequently this class dies on an étale covering of \(X\). The split injection (6.1) then kills \(\xi\) on that covering.

This proves (4.1) in dimension \(d\), and induction from \(T=\varnothing\) proves it for every finite model. Lemma 4.2 removes the finite-model assumption; Lemma 4.1 proves degree \(q\). Induction on \(q\), followed by the filtered-colimit argument and the affine/local-coordinate reductions, proves Theorem 1.1 at its stated generality. □

Notice the two inductions: the lower cohomological degrees justify (6.3), while the lower dimension treats (6.5). Confusing them would make the argument circular.

## 7. Complexes and limits of smooth changes of base

**Proposition 7.1.** Let \(S'=\varprojlim S_i\), where the \(S_i\to S\) are smooth and the transition maps are affine. Let \(g:T\to S\) be quasi-compact and quasi-separated, and form \(T'=T\times_S S'\). For \(E\in D^+(T_{\mathrm{ét}})\) whose cohomology sheaves have torsion stalks of orders invertible on \(S\), the canonical map is an isomorphism:

\[
(S'\to S)^{-1}Rg_*E
\xrightarrow{\sim}
R(T'\to S')_*(E|_{T'}).
\tag{7.1}
\]

*Proof.* For a single smooth change of base, compare the hypercohomology spectral sequences

\[
R^pg_*H^r(E)\ \Longrightarrow\ H^{p+r}(Rg_*E)
\tag{7.2}
\]

and the corresponding sequence after base change. Exact inverse image commutes with cohomology sheaves. Theorem 1.1 identifies the \(E_2\) pages by their canonical maps. Because \(p\geq0\) and \(E\) is bounded below, only finitely many terms contribute to a fixed total degree. The induced maps on the abutments are isomorphisms.

For the inverse limit, apply the continuity theorem of lesson 7 to the systems of direct images after the \(S_i\). It gives the sheaf-level comparison for each \(H^r(E)\) on \(S'\). The same finite-diagonal spectral-sequence argument gives (7.1). Étale-local affine charts suffice for this continuity calculation. All identifications come from pullback, hence yield the canonical map and respect refinements of the inverse system. □

Bounded below is doing actual work here. We have not asserted that the displayed spectral sequence proves base change for an arbitrary unbounded complex.

## 8. Field extensions and canonical invariance

**Lemma 8.1 (field models).** If \(L/K\) is a separable field extension, \(L\) is the filtered union of smooth \(K\)-subalgebras. In particular this holds for every extension of perfect fields.

*Proof.* A finite subset of \(L\) lies in a finitely generated subfield \(L_0/K\). Separability means that \(L_0\) admits a separating transcendence basis: over a rational function field it is finite separable. Choose a finite-type domain with fraction field \(L_0\). At its generic point the algebra is smooth, by the separable generic-point criterion. Invert a nonzero element to obtain a smooth affine algebra, and invert finitely many further denominators to include the given finite subset. Localization preserves smoothness. Applying this construction to the union of two finite sets makes the collection filtered. □

**Proposition 8.2 (all field extensions).** Let \(L/K\) be any field extension, and \(g:T\to S\) a quasi-compact, quasi-separated morphism of \(K\)-schemes. If \(E\in D^+(T_{\mathrm{ét}})\) has torsion cohomology stalks of orders invertible in \(K\), then

\[
(S_L\to S)^{-1}Rg_*E
\xrightarrow{\sim}Rg_{L,*}(E|_{T_L}).
\tag{8.1}
\]

*Proof.* When \(L/K\) is separable, write \(\operatorname{Spec}L\) as the inverse limit of spectra of the smooth algebras of Lemma 8.1 and apply Proposition 7.1. For general \(L/K\), pass to compatible perfect closures \(K^{\mathrm{perf}}\subset L^{\mathrm{perf}}\). Both maps from the perfect closures are purely inseparable universal homeomorphisms. By lesson 7 they induce equivalences of the relevant étale topoi, compatible with inverse images, direct images and the canonical comparison. The extension of perfect fields is separable, so the preceding case proves the comparison there. Transport it back through those equivalences. □

The proposition compares **higher direct images as sheaves**. If \(K\) is not separably closed, taking global sections also involves its Galois cohomology; cohomology groups over different fields are not thereby identified.

**Theorem 8.3 (separably closed invariance).** Let \(k'/k\) be an extension of separably closed fields. Let \(X\) be quasi-compact and quasi-separated over \(k\), and let \(E\in D^+(X_{\mathrm{ét}})\) have torsion cohomology stalks of orders prime to \(\operatorname{char}k\). For \(\pi:X_{k'}\to X\), the canonical maps

\[
H^q(X,E)\xrightarrow{\sim}H^q(X_{k'},\pi^{-1}E),
\qquad
E\xrightarrow{\sim}R\pi_*\pi^{-1}E
\tag{8.2}
\]

are isomorphisms.

*Proof.* Apply Proposition 8.2 to \(X\to\operatorname{Spec}k\). Étale sheaves on each of the two separably closed fields are simply abelian groups, and global sections are exact. Their inverse-image functor sends a group to the same group. Thus the comparison of higher direct images gives the first isomorphism in (8.2). The argument includes imperfect separably closed fields, since their algebraic closures are purely inseparable and were handled in Proposition 8.2.

For the second assertion restrict to a quasi-compact, quasi-separated étale \(U\to X\). The first assertion applied to \(U\) says that the adjunction unit induces

\[
R\Gamma(U,E)\xrightarrow{\sim}R\Gamma(U_{k'},\pi^{-1}E).
\]

These are the hypercohomology presheaves of the source and target of the unit. Sheafifying in each degree shows the unit is an isomorphism. Such \(U\)'s form a covering basis. This also proves that the cohomological comparison is the canonical pullback, rather than a choice of bases. □

Finite type over a field implies quasi-compact and quasi-separated, so the theorem includes the invariance for varieties. It also covers singular varieties and nonconstructible admissible torsion sheaves.

## 9. Local fibres and universal local acyclicity

Let \(a:X\to S\) be a morphism, \(\bar x\) a geometric point, and \(\bar s=a(\bar x)\). Write

\[
X_{(\bar x)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x},
\qquad
S_{(\bar s)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}.
\]

A geometric point \(\bar t\to S_{(\bar s)}\) specifies a geometric generization together with its specialization to \(\bar s\). The relevant local fibre is

\[
F_{\bar x,\bar t}
=X_{(\bar x)}\times_{S_{(\bar s)}}\bar t.
\tag{9.1}
\]

It is often called a variety of vanishing cycles; it is an affine scheme and need not be a variety of finite type. The coordinate ring of the strict localization retains all sufficiently small étale neighbourhoods of \(\bar x\).

For \(E\in D^+(X_{\mathrm{ét}})\), exact global sections on a strictly henselian local scheme identify

\[
E_{\bar x}=R\Gamma(X_{(\bar x)},E).
\]

Restriction to (9.1) gives

\[
\alpha_{E,\bar x,\bar t}:E_{\bar x}
\longrightarrow R\Gamma(F_{\bar x,\bar t},E).
\tag{9.2}
\]

We call \(a\) **locally acyclic relative to \(E\)** if (9.2) is an isomorphism for every such pair. It is **universally locally acyclic relative to \(E\)** if the same holds after every change of base, with the inverse image of \(E\). Without naming \(E\), local acyclicity means this condition for each constant \(\mathbf Z/n\) at \(\bar x\), where \(n\) is prime to the residue characteristic at \(\bar x\). For a constant group the condition is explicitly

\[
H^0(F_{\bar x,\bar t},\mathbf Z/n)=\mathbf Z/n,
\qquad
H^q(F_{\bar x,\bar t},\mathbf Z/n)=0\quad(q>0),
\tag{9.3}
\]

with the first equality induced by the constant-section map.

**Theorem 9.1.** Every smooth morphism is universally locally acyclic for torsion coefficients prime to the residue characteristics.

*Proof.* Smoothness survives arbitrary base change, so it suffices to prove local acyclicity for one smooth \(a\). Replace the base by \(S_{(\bar s)}\). The strict localization at \(\bar x\) and its local fibres are unchanged. An integer \(n\) prime to the closed residue characteristic is a unit on this local base. Apply Theorem 1.1 to the smooth morphism \(X\to S_{(\bar s)}\) and the quasi-compact, quasi-separated morphism \(\bar t\to S_{(\bar s)}\), with coefficient \(\mathbf Z/n\) on \(\bar t\).

On the stalk at \(\bar x\), the smooth base change comparison is

\[
H^q(\bar t,\mathbf Z/n)
\xrightarrow{\sim}H^q(F_{\bar x,\bar t},\mathbf Z/n).
\tag{9.4}
\]

Indeed the source is computed by the strictly localized base and the target by the strictly localized source, using the higher-direct-image stalk formula of lesson 7. The field of \(\bar t\) is separably closed, so the left group is \(\mathbf Z/n\) in degree zero and zero otherwise. In degree zero the map is the constant-section map. This proves (9.3) and hence (9.2). Apply the same argument to each base-changed smooth morphism to obtain universality. □

**Lemma 9.2 (locally constant coefficients).** If \(a\) is locally acyclic and \(F\) is locally constant with torsion stalks whose element orders are prime to the corresponding residue characteristics, then \(a\) is locally acyclic relative to \(F[0]\). For smooth \(a\), it is universally so.

*Proof.* On \(X_{(\bar x)}\), the locally constant sheaf is constant with group \(M=F_{\bar x}\): a pointed trivializing étale neighbourhood admits a section over the strict localization. The group \(M\) is the filtered union of its finite subgroups, each of order prime to the residue characteristic. Decompose each finite subgroup into cyclic groups. Equation (9.3) gives the cohomology for each cyclic summand. Since (9.1) is affine, its cohomology commutes with the filtered union by lesson 7. The resulting comparison is \(M\) in degree zero and zero in higher degrees. This is precisely (9.2). Under base change, local constancy persists; a residue field extension has the same characteristic, so the coefficient condition persists as well. Apply Theorem 9.1 after each base change. □

Universal local acyclicity does not say that an entire smooth affine fibre is acyclic. It says that the local fibres of its strict localizations have (9.3). A smooth proper curve of positive genus has substantial degree-one cohomology on the whole fibre.

## 10. Specialization and cospecialization

Fix \(\bar s\) and \(\bar t\to S_{(\bar s)}\). After replacing the base by its strict localization write

\[
X_{\bar t}\xrightarrow{u}\widetilde X
\xleftarrow{v}X_{\bar s},
\qquad
\widetilde X=X\times_S S_{(\bar s)}.
\tag{10.1}
\]

Suppose \(a\) is locally acyclic relative to the bounded-below \(E\). This property persists for the present strict-local base change: pointed strict localizations are computed by the same cofinal systems of étale neighbourhoods. Equivalently one may use universal local acyclicity in all the smooth applications below.

**Lemma 10.1.** The adjunction unit \(b:E|_{\widetilde X}\to Ru_*(E|_{X_{\bar t}})\) becomes an isomorphism after \(v^{-1}\).

*Proof.* At a geometric point \(\bar x\) of the closed fibre its stalk is

\[
E_{\bar x}\longrightarrow
R\Gamma(X_{(\bar x)}\times_{S_{(\bar s)}}\bar t,E).
\]

This is (9.2), by the stalk formula for \(Ru_*\). Local acyclicity says it is an isomorphism. Stalks detect isomorphisms of cohomology sheaves, so \(v^{-1}b\) is an isomorphism in the derived category. □

Define **cospecialization** by

\[
\begin{aligned}
R\Gamma(X_{\bar t},E)
&=R\Gamma(\widetilde X,Ru_*E|_{X_{\bar t}})\\
&\longrightarrow R\Gamma(X_{\bar s},v^{-1}Ru_*E|_{X_{\bar t}})\\
&\xrightarrow{(v^{-1}b)^{-1}}R\Gamma(X_{\bar s},E).
\end{aligned}
\tag{10.2}
\]

It points from general-fibre cohomology to special-fibre cohomology. The specialization map of the sheaf complex \(Ra_*E\) points in the other direction:

\[
\operatorname{sp}:(Ra_*E)_{\bar s}\longrightarrow(Ra_*E)_{\bar t}.
\tag{10.3}
\]

For a quasi-compact, quasi-separated \(a\), the stalk formula identifies the source of (10.3) with \(R\Gamma(\widetilde X,E)\). The composition of (10.3) with the fibre comparison at \(\bar t\) is restriction along \(u\).

**Lemma 10.2 (comparison identity).** The following square, with its right arrow pointing upwards, commutes:

\[
\begin{matrix}
(Ra_*E)_{\bar s}&\longrightarrow&R\Gamma(X_{\bar s},E)\\
\operatorname{sp}\downarrow&&\uparrow\operatorname{cosp}\\
(Ra_*E)_{\bar t}&\longrightarrow&R\Gamma(X_{\bar t},E).
\end{matrix}
\tag{10.4}
\]

*Proof.* Under the strict-local description, restriction along \(u\) is the map on derived global sections induced by the unit \(b\). Cospecialization first regards those sections as sections of \(Ru_*E\), restricts them by \(v\), and applies the inverse of \(v^{-1}b\). Naturality of restriction identifies this composite with restriction of \(E\) along \(v\). That is exactly the upper fibre-comparison map. □

Units, restriction maps and their inverses also prove functoriality in \(E\) and compatibility with long exact cohomology sequences. The direction of cospecialization must be retained when using (10.4).

## 11. Properness makes the two maps inverse

**Lemma 11.1 (torsion direct images).** For a quasi-compact, quasi-separated \(w:Z\to W\), \(Rw_*\) takes \(D^+\) complexes with torsion cohomology sheaves to complexes of the same kind.

*Proof.* For a torsion sheaf \(A\), write \(A=\varinjlim A[n]\). On every quasi-compact, quasi-separated inverse image of an affine étale object, continuity identifies \(H^q(A)\) with the colimit of \(H^q(A[n])\). Each class from the latter group is killed by \(n\). Thus the cohomology groups, and the higher-direct-image sheaves obtained by sheafifying them, are torsion. For a bounded-below complex, the spectral sequence (7.2) has a finite filtration in each total degree with torsion subquotients. An extension of finitely many torsion groups is torsion. Right derived image preserves the lower bound. □

**Theorem 11.2 (proper locally acyclic specialization).** Suppose \(a:X\to S\) is proper, \(E\in D^+(X_{\mathrm{ét}})\) has torsion cohomology sheaves, and \(a\) is locally acyclic relative to \(E\). Then the specialization and cospecialization maps in (10.4) are inverse isomorphisms, under the canonical proper fibre identifications.

*Proof.* Proper base change from lesson 13 makes both horizontal maps in (10.4) isomorphisms. We prove that (10.2) is an isomorphism. Its last arrow is one by Lemma 10.1. Its first equality is derived composition of global sections with \(u_*\). Its middle arrow is restriction to the closed fibre with coefficient complex

\[
L=Ru_*(E|_{X_{\bar t}}).
\]

The map \(u\) is affine, hence quasi-compact and quasi-separated: it is the base change of the map from a field spectrum to the affine strict-local base. Lemma 11.1 shows that \(L\) is bounded below with torsion cohomology sheaves. Apply proper base change to \(\widetilde X\to S_{(\bar s)}\), with coefficient \(L\). Since global sections on the strictly henselian local base equal the closed geometric stalk, its comparison is

\[
R\Gamma(\widetilde X,L)\xrightarrow{\sim}
R\Gamma(X_{\bar s},v^{-1}L).
\tag{11.1}
\]

This is the middle arrow of (10.2). Cospecialization is therefore an isomorphism. Commutativity of (10.4), with both horizontal maps isomorphisms, identifies specialization with its inverse. □

**Corollary 11.3 (proper smooth specialization).** If \(a\) is smooth and proper and \(F\) is locally constant with torsion stalks prime to the corresponding residue characteristics, then

\[
\operatorname{sp}:(Ra_*F)_{\bar s}\xrightarrow{\sim}(Ra_*F)_{\bar t}.
\tag{11.2}
\]

*Proof.* Lemma 9.2 makes \(a\) locally acyclic relative to \(F\), including the required strict-local base change. Apply Theorem 11.2. No finiteness of the stalk group is required for (11.2). □

## 12. Finite coefficients give a local system

A finite locally constant abelian sheaf has finite stalk groups. More generally, for a Noetherian ring \(\Lambda\), “finite type locally constant” means locally constant with finitely generated \(\Lambda\)-module stalks; their underlying sets need not be finite.

**Lemma 12.1 (a local constancy test).** Let \(S\) be locally Noetherian, \(\Lambda\) Noetherian, and \(A\) a constructible \(\Lambda\)-sheaf. If every specialization map between geometric stalks of \(A\) is an isomorphism, then \(A\) is finite type locally constant.

*Proof.* At \(\bar s\), the finitely generated stalk \(M=A_{\bar s}\) has a finite presentation because \(\Lambda\) is Noetherian. Lift its finitely many generators to sections on a pointed étale neighbourhood. Shrink that neighbourhood until the finitely many defining relations vanish. These sections define

\[
\varphi:\underline M\longrightarrow A|_U
\tag{12.1}
\]

which is an isomorphism at the distinguished geometric point. We may take \(U\) affine and Noetherian. The locus where its geometric stalk maps are isomorphisms is preserved under specialization and generization: the stalk maps for \(\underline M\) and \(A\) are isomorphisms, and naturality makes the corresponding squares commute. The existence of lifts of a geometric specialization follows by passing to strict localizations; different choices conjugate the maps and do not change whether they are isomorphisms.

Remove the finitely many irreducible components of \(U\) not passing through the distinguished point. In each remaining component, its generic point is a generization of that point, so belongs to the isomorphism locus. Every point on the component is a specialization of its generic point, so also belongs. Thus \(\varphi\) is an isomorphism on every stalk and hence is an isomorphism of sheaves. It trivializes \(A\) near \(\bar s\). Repeat at every geometric point. □

**Theorem 12.2 (proper smooth local constancy).** Let \(a:X\to S\) be smooth and proper. Let \(\Lambda\) be Noetherian and \(F\) a finite type locally constant \(\Lambda\)-sheaf such that each stalk is killed by an integer prime to its residue characteristic. Then every \(R^qa_*F\) is finite type locally constant. In particular, for finite abelian \(F\) of order prime to the residue characteristics, every \(R^qa_*F\) is finite locally constant.

*Proof.* Work on an affine open of \(S\). Since \(X\) is quasi-compact, a finite étale covering trivializes \(F\) on its members. Its stalk modules are finitely generated and torsion, so each has a finite positive annihilator. The smallest positive integer annihilator is locally constant on \(X\), with finitely many values. Decompose \(X\) into the finitely many open and closed pieces carrying a fixed value \(n\). Cohomology of this finite disjoint union is the direct sum of the cohomologies of the pieces, so treat one piece.

Its smooth proper image in \(S\) is open and closed, because smooth maps are open and proper maps are closed. Restrict to that image; on its complement all its direct images are zero. On the image, \(n\) is invertible: every base residue field is the base of a fibre where the coefficient annihilator is prime to the characteristic. We therefore have a smooth proper family over \(\mathbf Z[1/n]\), with \(nF=0\).

Write the affine base algebra as the filtered union of its finite-type \(\mathbf Z[1/n]\)-subalgebras. Descend the family to a smooth proper \(a_i:X_i\to S_i\) at some stage. Descend the finite type locally constant \(\Lambda\)-sheaf as well. For completeness, choose a finite affine étale trivializing covering of \(X\). Its finitely presented objects and covering property descend; the coefficient modules are finitely presented, and their transition isomorphisms are determined by finitely many generators and relations on a finite covering of each quasi-compact overlap. The finitely many cocycle identities hold at a sufficiently late stage. This gives a finite type locally constant \(F_i\). Replacing it by \(\ker(n:F_i\to F_i)\) retains that property, since \(\Lambda\) is Noetherian, and makes it \(n\)-torsion with pullback \(F\).

The base \(S_i\) is Noetherian. The constructibility theorem stated in lesson 14 applies to the proper finite-presentation \(a_i\) and the constructible \(F_i\): \(R^qa_{i,*}F_i\) is a constructible \(\Lambda\)-sheaf with finitely generated stalks. Corollary 11.3 makes every specialization map an isomorphism. Lemma 12.1 makes the sheaf finite type locally constant. Proper base change identifies its pullback to \(S\) with \(R^qa_*F\), so the latter has the same property. Sum over the finitely many annihilator pieces.

For a finite abelian coefficient group one may use \(\Lambda=\mathbf Z/n\) on each piece. A finitely generated module over this finite ring has finite cardinality. This proves the finite version. □

The finite hypothesis is part of the local-system deduction. Specialization maps alone do not force an infinite sheaf to be étale locally constant. For example on \(\operatorname{Spec}\mathbf Q\), the sheaf \(\bigoplus_{\ell}\mu_\ell\), summed over primes, has isomorphisms for all specialization maps. There is only one underlying point, and the geometric-point maps act by automorphisms. But no finite field extension trivializes the sheaf: it would contain primitive roots of unity of every prime order, whereas the degrees \(\ell-1\) of their cyclotomic fields are unbounded. An étale trivializing neighbourhood of a field point would supply just such a finite separable extension. Thus this sheaf is not locally constant. For arbitrary infinite locally constant input in Corollary 11.3, the conclusion proved here is the specialization isomorphism; Theorem 12.2 gives the local constancy assertion with its finite type hypothesis.

## 13. Three examples

**Example 13.1 (projective space).** Let \(k'/k\) be an extension of algebraically closed fields and \(\ell\) a prime invertible in \(k\). For every \(r\geq0\), canonical pullback gives

\[
H^q(\mathbf P^r_k,\mathbf Z/\ell)
\xrightarrow{\sim}H^q(\mathbf P^r_{k'},\mathbf Z/\ell)
\quad\text{for all }q.
\tag{13.1}
\]

This follows directly from Theorem 8.3, applied to the finite-type scheme \(\mathbf P^r_k\). Pullback commutes with cup products, so (13.1) is an isomorphism of graded cohomology rings. It also respects the Kummer class of \(\mathcal O(1)\), since that line bundle pulls back to \(\mathcal O(1)\). For \(r=1\), lesson 10 computed \(H^0=\mathbf Z/\ell\), \(H^1=0\), \(H^2=(\mathbf Z/\ell)(-1)\) and zero groups in higher degrees; these particular computations transport with their canonical maps. No projective-space computation in arbitrary dimension is needed to prove (13.1).

Projective space is proper, so lesson 13 in fact gives its separably closed field invariance for all torsion coefficients, including characteristic torsion. The prime-to-characteristic restriction in smooth base change becomes indispensable for nonproper examples.

**Example 13.2 (new Artin–Schreier classes).** Let \(k\) be algebraically closed of characteristic \(p>0\). The Artin–Schreier sequence and vanishing of cohomology of the quasi-coherent sheaf \(\mathcal O\) on the affine line give

\[
H^1(\mathbf A^1_k,\mathbf F_p)
=k[z]/\{b^p-b:b\in k[z]\}.
\tag{13.2}
\]

Here the quotient is one of additive groups. Constants disappear because \(b\mapsto b^p-b\) is onto \(k\). For a monomial of positive degree divisible by \(p\),

\[
[c z^{pm}]=[c^{1/p}z^m].
\]

Repeatedly lower the exponents in this way. Each class has a representative involving only positive exponents not divisible by \(p\). It is unique: a nonconstant \(b\) has \(\deg(b^p-b)=p\deg b\), whereas the leading exponent of a nonzero reduced representative is not divisible by \(p\). Thus, as \(\mathbf F_p\)-vector spaces with their canonical coefficient coordinates,

\[
H^1(\mathbf A^1_k,\mathbf F_p)
\cong\bigoplus_{\substack{m\geq1\\ p\nmid m}}k.
\tag{13.3}
\]

If \(k'\supsetneq k\) is algebraically closed, pullback acts on each coordinate by \(k\hookrightarrow k'\). Choose \(u\in k'\setminus k\); the class \([uz]\) in degree-one cohomology over \(k'\) is not in its image. “Growth” here means the appearance of new classes under the specified comparison, not a claim that two infinite abstract dimensions must differ. The torsor is given by \(w^p-w=uz\).

**Example 13.3 (a family of curves).** Let \(a:C\to S\) be smooth proper of relative dimension one, with geometrically connected fibres, and let \(\ell\) be invertible on \(S\). Theorem 12.2 makes

\[
R^1a_*\mathbf F_\ell
\]

a finite locally constant \(\mathbf F_\ell\)-sheaf. Proper base change identifies its geometric stalk with \(H^1(C_{\bar s},\mathbf F_\ell)\). The smooth proper curve computation in lessons 10–12 gives its dimension \(2g_{\bar s}\). Local constancy makes this integer locally constant on \(S\). On a connected base, all genera are therefore the same \(g\), and the local system has rank \(2g\). Specialization maps are the isomorphisms of Corollary 11.3. Global transport between two arbitrary points involves a choice of étale path and can have monodromy.

## 14. Exercises

In these exercises \(\ell\) denotes a prime.

1. **Easy — affine space.** Let \(k\) be separably closed and \(\ell\) invertible in \(k\). Prove \(H^q(\mathbf A^r_k,\mathbf F_\ell)=0\) for \(q>0\), by induction on \(r\), using the affine-line computation and smooth base change. Then prove the stronger statement \(H^q(\mathbf A^r_k,\mathbf F_\ell)\cong H^q(k,\mathbf F_\ell)\) for an arbitrary field \(k\) with \(\ell\) invertible. Explain why the vanishing statement needs a condition on \(k\).

2. **Medium — characteristic torsion.** Over an algebraically closed field \(k\) of characteristic \(p\), exhibit failure of the canonical cohomology comparison for \(\mathbf A^1\) after a separably closed field extension, with coefficient \(\mathbf F_p\). Also exhibit failure in a square whose change-of-base morphism is actually smooth of finite presentation.

3. **Medium — constant fibre cohomology.** Let \(a:X\to S\) be proper smooth with geometrically connected fibres, \(S\) connected, and \(\ell\) invertible on \(S\). Prove that all \(H^1(X_{\bar s},\mathbf F_\ell)\) are isomorphic as vector spaces. Explain the roles of connectedness of the base and monodromy. Apply this to a family of curves.

4. **Medium, with an algebraic construction — the node.** Let \(k\) be algebraically closed, \(\ell\) invertible in \(k\), and \(a:\mathbf A^2_k\to\mathbf A^1_k\) the map \(t=xy\). Show that \(a\) is not locally acyclic at the origin for \(\mathbf F_\ell\). In the local geometric generic fibre, find a nonzero Kummer class of \(x\). An irrational Gauss valuation can detect that \(x\) is not an \(\ell\)-th power. Also explain the literal alternative with source \(\operatorname{Spec}k[x,y]/(xy)\) and \(t\) sent to zero.

5. **Hard — finite local systems on the base.** Prove that \(R^qa_*\mathbf F_\ell\) is finite locally constant for a proper smooth \(a:X\to S\) and \(\ell\) invertible on \(S\). Give the generator-and-relation argument that turns constructibility and specialization isomorphisms into local constancy on a Noetherian base, and explain the descent that removes the Noetherian hypothesis.

The first exercise includes the separably closed hypothesis absent from an unqualified affine-space vanishing assertion. In exercise 3, connectedness is a condition on the base as well as on the fibres. In exercise 4 the smoothing is defined by \(k[t]\to k[x,y]\), \(t\mapsto xy\); imposing \(xy=0\) before defining the map makes it a constant map instead.

## 15. Full solutions

**Solution 1.** Write \(b:\mathbf A^1_k\to\operatorname{Spec}k\). On a separably closed field the affine-line computation from lesson 12 gives \(R^qb_*\mathbf F_\ell=0\) for \(q>0\), and \(b_*\mathbf F_\ell=\mathbf F_\ell\), with the latter identified by constant sections. Consider the square with change of base \(\mathbf A^{r-1}_k\to\operatorname{Spec}k\), which is smooth. Theorem 1.1 gives, for the projection \(p:\mathbf A^r_k\to\mathbf A^{r-1}_k\),

\[
Rp_*\mathbf F_\ell=\mathbf F_\ell[0].
\tag{15.1}
\]

The Leray spectral sequence has only its row of degree zero and identifies \(H^q(\mathbf A^r_k,\mathbf F_\ell)\) with \(H^q(\mathbf A^{r-1}_k,\mathbf F_\ell)\), through the canonical pullback. Induct down to \(\operatorname{Spec}k\). Its positive cohomology vanishes, proving the first assertion, including \(r=0\).

For an arbitrary \(k\), the geometric stalk of \(R^qb_*\mathbf F_\ell\) is the affine-line cohomology over a separable closure of \(k\), by the stalk formula and continuity. The same affine-line computation therefore says \(Rb_*\mathbf F_\ell=\mathbf F_\ell[0]\) as a complex on \(\operatorname{Spec}k\). Its degree-zero Galois action is trivial, since the constant-section map is an isomorphism. The same smooth squares and Leray induction give

\[
H^q(k,\mathbf F_\ell)\xrightarrow{\sim}
H^q(\mathbf A^r_k,\mathbf F_\ell).
\tag{15.2}
\]

For a finite field with \(\ell\) different from its characteristic, \(H^1(k,\mathbf F_\ell)=\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbf Z},\mathbf F_\ell)=\mathbf F_\ell\). It does not vanish. The origin gives a section of the structure map, so even without (15.2), pullback of that nonzero class could not vanish. □

**Solution 2.** Take \(k'\) to be an algebraic closure of \(k(u)\), with \(u\) transcendental. Formula (13.3) shows that the pullback from \(k\) to \(k'\) is not surjective: the first coordinate of \([uz]\) is \(u\notin k\). This proves failure of the field-extension consequence when the prime-to-characteristic hypothesis is removed.

To see failure for an actual smooth change of base, take

\[
\begin{matrix}
\mathbf A^2_{k,(u,z)}&\xrightarrow{e}&\mathbf A^1_{k,z}\\
h\downarrow&&\downarrow g\\
\mathbf A^1_{k,u}&\xrightarrow{f}&\operatorname{Spec}k,
\end{matrix}
\tag{15.3}
\]

where both horizontal maps are the evident base changes and \(h\) is projection to \(u\). The morphism \(f\) is smooth of finite presentation and \(g\) is affine of finite type. On the stalk at a geometric generic point of the \(u\)-line, the degree-one comparison with coefficient \(\mathbf F_p\) is

\[
H^1(\mathbf A^1_k,\mathbf F_p)
\longrightarrow H^1(\mathbf A^1_{k'},\mathbf F_p).
\tag{15.4}
\]

The strict-local stalk initially uses a separable closure of \(k(u)\); its purely inseparable algebraic closure induces the same étale topos and hence the same groups, by lesson 7. Thus (15.4) is indeed the stalk comparison. The global Artin–Schreier torsor \(w^p-w=uz\) on \(\mathbf A^2\) induces the class just found. It is absent from the source. Consequently \(f^{-1}R^1g_*\mathbf F_p\to R^1h_*e^{-1}\mathbf F_p\) is not an isomorphism. All geometric finiteness and smoothness conditions hold; the failed condition is that \(p\) be invertible. □

**Solution 3.** Theorem 12.2 makes \(R^1a_*\mathbf F_\ell\) finite locally constant. Proper base change identifies its stalk with the degree-one cohomology of the geometric fibre. The dimension of a finite locally constant vector-space sheaf is a locally constant integer-valued function. On connected \(S\) it is constant. Thus all the vector spaces have the same finite dimension and are isomorphic.

For points linked by a specified geometric specialization, Corollary 11.3 gives the actual canonical isomorphism. For arbitrary points a transport map uses an étale path. Two choices can differ by the monodromy representation; the statement does not supply one canonical global identification of every stalk. Connected geometric fibres alone would not force equality across different components of the base: a disjoint union of a projective-line family over one point and a positive-genus curve over another is smooth proper with connected geometric fibres, but has different degree-one dimensions. For a connected family of curves the common dimension is \(2g\), by the earlier curve computation, so the genus is constant and the local system has rank \(2g\). □

**Solution 4.** The whole geometric generic fibre of \(t=xy\) is \(\mathbf G_m\), but that observation alone does not compute the fibre of the strict localization at the origin. We give a direct obstruction in the correct local fibre.

Set

\[
A=(k[t]_{(t)})^{\mathrm{sh}},\qquad
B=(k[x,y]_{(x,y)})^{\mathrm{sh}},\qquad t\mapsto xy.
\]

Let \(\bar K\) be an algebraic closure of \(\operatorname{Frac}A\). The local geometric generic fibre is

\[
F=\operatorname{Spec}(B\otimes_A\bar K).
\tag{15.5}
\]

Since \(xy=t\) and \(t\) is a nonzero scalar in \(\bar K\), \(x\) is a unit on \(F\). We prove that it is not an \(\ell\)-th power there.

Embed \(A\) in \(k[[t]]\) by the pointed henselian lifting property, and embed \(\bar K\) in an algebraic closure \(\Omega\) of \(k((t))\). Give \(\Omega\) the extended \(t\)-adic valuation, normalized by \(v(t)=1\). Its value group is \(\mathbf Q\) and its residue field is \(k\): every finite extension has rational ramification index, and the algebraically closed residue field has no nontrivial finite algebraic residue extension.

Choose an irrational real \(c\) with \(0<c<1\). On \(\Omega(X)\) put the Gauss valuation

\[
v\!\left(\sum_i a_iX^i\right)=\min_i\{v(a_i)+ic\}.
\tag{15.6}
\]

Distinct nonzero terms have different valuations because \(c\) is irrational and the coefficient valuations are rational. The term attaining the minimum is unique; multiplication multiplies those leading terms, proving multiplicativity. Extend to rational functions by subtracting valuations. The value group is \(\mathbf Q+\mathbf Zc\) and the residue field is \(k\). For the latter assertion, a rational function of value zero has numerator and denominator leading exponents equal, since their difference times \(c\) is rational. Their leading coefficient ratio has residue in \(k\).

Complete this valued field to \(L\), and let \(V\) be its valuation ring. Completion changes neither its value group nor its residue field: a sequence converging to a nonzero element has eventually the same valuation as its limit, and a convergent sequence of units has eventually the same residue. A complete real-valued field is henselian, by the convergent simple-root lifting argument. Thus \(V\) is a henselian local ring with separably closed residue field \(k\).

Map

\[
x\longmapsto X,\qquad y\longmapsto t/X.
\tag{15.7}
\]

Their valuations are \(c\) and \(1-c\), both positive. A polynomial with nonzero constant term maps to a unit. Hence (15.7) defines a local map \(k[x,y]_{(x,y)}\to V\) inducing the identity on \(k\). The pointed henselian lifting property extends it to \(B\to V\): every pointed étale neighbourhood defining the strict henselization lifts uniquely. Its restriction to \(A\) agrees with the chosen map through \(\Omega\), again by uniqueness of these pointed lifts. We obtain a compatible ring map

\[
B\otimes_A\bar K\longrightarrow L.
\tag{15.8}
\]

If a unit \(z\) on \(F\) satisfied \(z^\ell=x\), its image in \(L\) would have valuation \(c/\ell\). But

\[
c/\ell\notin\mathbf Q+\mathbf Zc:
\quad c/\ell=q+mc\Longrightarrow(1/\ell-m)c=q
\]

would make \(c\) rational, since the integer \(m\) cannot equal \(1/\ell\). This contradiction proves the claim.

The Kummer sequence, with \(\ell\) invertible, injects the quotient of the unit group by its \(\ell\)-th powers into \(H^1(F,\mu_\ell)\). The class of \(x\) is therefore nonzero. Over the algebraically closed \(k\), choosing a primitive \(\ell\)-th root identifies \(\mu_\ell\) with the constant \(\mathbf F_\ell\). Thus \(H^1(F,\mathbf F_\ell)\ne0\), whereas the stalk of that coefficient sheaf at the origin is concentrated in degree zero. Map (9.2) is not an isomorphism. This nonzero local class is the required vanishing-cycle obstruction; no comparison with singular cohomology was used.

Finally, for the literal map \(k[t]\to k[x,y]/(xy)\), \(t\mapsto xy=0\), the local generic fibre is empty: tensoring with \(\bar K\) makes the scalar \(t\) both zero and invertible. Its degree-zero cohomology is zero. The coefficient stalk at the origin is \(\mathbf F_\ell\), so even the degree-zero comparison fails. That map is not a nodal smoothing. □

**Solution 5.** First let \(S\) be Noetherian. The constant \(\mathbf F_\ell\)-sheaf is constructible, and the proper finite-presentation constructibility theorem from lesson 14 makes \(R^qa_*\mathbf F_\ell\) constructible with finite-dimensional stalks. Corollary 11.3 proves that all its specialization maps are isomorphisms. At \(\bar s\), choose a basis of its stalk and lift the finitely many basis vectors to a pointed étale neighbourhood \(U\). They define \(\underline{\mathbf F_\ell^m}\to R^qa_*\mathbf F_\ell|_U\), an isomorphism at the distinguished point. Naturality and invertible specialization maps make its isomorphism locus stable under both specialization and generization. Remove the finitely many irreducible components of the Noetherian affine \(U\) not passing through that point. The generic point of every remaining component is in the locus; all its specializations are too. Thus every stalk map is an isomorphism, and the sheaf is constant on \(U\). This is the field-coefficient instance of Lemma 12.1. With general Noetherian coefficient modules, lift generators and their finitely many relations instead of a basis.

For arbitrary \(S\), work on an affine open and descend the proper smooth finite-presentation morphism to a finite-type \(\mathbf Z[1/\ell]\)-model. Properness and smoothness hold at a sufficiently late stage. The constant coefficient sheaf descends automatically. The model has finite locally constant higher direct images by the Noetherian case. Proper base change identifies their pullbacks with \(R^qa_*\mathbf F_\ell\), and inverse image preserves finite local constancy. This covers \(S\) and proves the result. □

## 16. Sources, scope and the historical route

The modern proof targets are the [smooth base change section](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-smooth-base-change), including the pointed curve effacement lemma and both full proofs; the [field-extension applications](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-applications-smooth-base-change); the [degree-zero preliminaries](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-base-change-f-star); the [local acyclicity section](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-local-acyclicity); the [cospecialization construction and proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cospecialization); and the [finite type locally constant proper smooth theorem](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-proposition-loc-cst-torsion). They retain the quasi-compact, quasi-separated and coefficient conditions.

Additional actual targets include the [connected-fibre sections lemma](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-sections-upstairs), the [finite-module local constancy criterion](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-characterize-locally-constant-module), and the [field smooth-algebra approximation](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-colimit-syntomic). Section 2 identifies the smooth geometric inputs; Section 5 isolates the exact prime-to-characteristic finite-cover extension prerequisite. The owned cohomological argument supplies the degree and dimension inductions, limits, local-fibre calculation and proper specialization proof.

For the historical account, M. Artin's **[SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XV**, Sections 1–3, develops acyclic and locally acyclic morphisms and proves smooth local acyclicity using henselian local affine lines, tame ramification and finite-cover extension. **Exposé XVI**, Sections 1–2, derives smooth base change and specialization. The order here follows the modern direct effacement proof, then deduces local acyclicity. It does not assume a historical local acyclicity theorem to prove smooth base change and then use smooth base change to prove the same premise.

P. Deligne's **[SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf), Cohomologie étale: les points de départ (Arcata), V**, §§1–3, gives the vanishing-cycle and cospecialization viewpoint and its applications. Its prime-to-characteristic coefficient convention is essential. It is used as a historical statement and mechanism comparison; the proofs needed for this course are supplied above.

In SGA 4, XVI.1.1 has finiteness conditions on the direct-image morphism, and XVI.2.1 requires locally constant **and** constructible coefficients: for arbitrary constructible input the assertion fails, already for the identity morphism and a constructible sheaf that is not locally constant. We keep the necessary input condition. In the affine-curve reduction the higher vanishing holds for \(q>1\); degrees zero and one are treated separately.

The exercised corrections are mathematical: separably closedness for affine-space vanishing, connectedness of the base for a common fibre rank, finite type coefficients for the local-system deduction, the correct nodal-family coordinate ring, and the prime-to-characteristic condition wherever smooth base change or smooth local acyclicity is used.
