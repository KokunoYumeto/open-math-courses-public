# SH02-SUP-EXH-001 — Recovering sheaf cohomology from closed pieces

Support item: SH02-SUP-EXH-001.

This note supplies the geometric comparison needed before applying a
Mittag-Leffler argument. Its proof does not require the closed pieces to be
compact. In particular it applies to strips with a noncompact horizontal base.

## SH02-EXH-COMPARISON — The comparison

Let T be a topological space and k a fixed unital coefficient ring. Let

\[
T_0\subset T_1\subset\cdots\subset T,
\qquad T_n\text{ closed},\qquad
T_n\subset\operatorname{Int}_T(T_{n+1}),\qquad
\bigcup_nT_n=T.
\]

Write \(i_n:T_n\hookrightarrow T\). For \(K\) in the bounded-below derived category of
sheaves of left \(k\)-modules on \(T\), put \(K_n=i_{n*}i_n^{-1}K\). Restriction to the smaller
closed piece gives the transition \(K_{n+1}\to K_n\). Then the restriction maps
induce an equivalence

\[
K\simeq\operatorname*{holim}_n K_n.                 \tag{1}
\]

Here holim means the homotopy inverse limit, or derived inverse limit. It is
not an ordinary categorical inverse limit in the triangulated derived category.
One may work in the enhanced derived category. Concretely, represent \(K\) by a
bounded-below complex \(C\) and use the strict tower \(i_{n*}i_n^{-1}C\). For
\(h_n:T_n\hookrightarrow T_{n+1}\), the transition is \(i_{n+1*}\) applied to
the restriction unit into \(h_{n*}h_n^{-1}i_{n+1}^{-1}C\). The resulting strict
map from the constant tower defines the map in (1) after derived inverse limit.

For an explicit resolution, use the Grothendieck category of inverse sequences
of sheaves. Evaluation at index n preserves injectives: its left adjoint places
the given sheaf at indices at most n, zero at later indices, and has identity
transitions where applicable; it is exact. A bounded-below injective resolution
of the tower consequently evaluates to K-injective complexes \(I_n\).
The cone of \(1-\mathrm{shift}\) on their product, shifted by minus one,
computes the homotopy limit. Strict compatibility provides the zero null-homotopy
needed for the comparison map. This agrees with the enhanced-derived-category
construction, without asserting uniqueness of a cone in a bare triangulated category.

**Proof.** Fix an open inclusion \(j:U\hookrightarrow T\). Restriction \(j^{-1}\) is
exact and has the exact extension-by-zero functor \(j_!\) as a left adjoint. The
adjunction therefore passes to derived categories, and \(j^{-1}\) preserves derived
products. It is exact on distinguished triangles as well. Apply it to the
derived-product triangle defining the countable homotopy limit,

\[
\operatorname*{holim}_n K_n\longrightarrow
\prod_n^{\mathrm D} K_n
\xrightarrow{\,1-\mathrm{shift}\,}\prod_n^{\mathrm D}K_n.
\]

It follows that restriction commutes with this homotopy limit. The products
here are derived products; termwise products of arbitrary complexes must not
be substituted without justification.

The open sets \(U_N=\operatorname{Int}_T(T_N)\) cover \(T\): a point of \(T_n\)
lies in \(U_{n+1}\). On \(U_N\), every \(K_n\) with \(n\geq N\) restricts to \(K|_{U_N}\), with identity transition
maps under the restriction identifications. Discarding a finite initial segment
does not change a homotopy inverse limit. The homotopy limit of this remaining
constant tower is \(K|_{U_N}\), and the map in (1) restricts to that equivalence.
For clarity, the latter constant-tower computation is elementary: the map
\(x\mapsto(x_0,(1-\mathrm{shift})x)\) identifies \(\prod L\) with
\(L\oplus\prod L\). Its inverse has nth component
\(a-\sum_{0\leq r<n}y_r\), a finite sum. Thus the homotopy fibre of the second
projection is \(L\), with the diagonal comparison. Finite initial factors are
removed by the same finite triangular elimination.
Equivalences of complexes of sheaves can be checked on an open cover, by their
cohomology sheaves. This proves (1). No compactness or Hausdorff assumption was
used. \(\square\)

## SH02-EXH-UNBOUNDED — The comparison on all unbounded complexes

The comparison (1), and the Milnor sequence (2) below, also hold for every
\(K\in D(k_T)\). The space and exhaustion have exactly the preceding
hypotheses. The ring may be noncommutative, with sheaves of left modules.
Neither finite cohomological dimension nor exact products of sheaves are
assumed. Here is the model construction needed to justify the larger range.

Let \(\mathcal A\) be the category of module sheaves on \(T\) and
\(\mathcal A^{\mathbf N^{\mathrm{op}}}\) its category of inverse sequences.
This is a Grothendieck category: kernels and filtered colimits are computed
at each index, so AB5 is inherited. If \(G\) is a generator of \(\mathcal A\),
the coproduct of the sheaves \(L_nG\) is a generator of the sequence category.
The exact functor \(L_n\), left adjoint to evaluation at index \(n\), puts
\(G\) at indices \(m\leq n\), zero at later indices, and uses identity
transitions where both terms are nonzero. The adjunction detects every
nonzero component of a morphism, which proves the generator assertion.

Apply the [complete unbounded K-injective construction, Theorem 4.1](../../../derived-categories-and-sheaf-operations/src/k-injective-resolutions-in-grothendieck-categories.md#4-constructing-the-unbounded-resolution)
to the strict tower \(S_n=i_{n*}i_n^{-1}C\), where \(C\) is any complex
representing \(K\). Obtain a quasi-isomorphism of sequence complexes
\(S\to I\) into a K-injective complex of injective sequences. Each
\(I_n\) is K-injective in \(\mathcal A\). Indeed, for any acyclic complex
\(B\) in \(\mathcal A\),

\[
\operatorname{Hom}^{\bullet}_{\mathcal A}(B,I_n)
\simeq
\operatorname{Hom}^{\bullet}_{\mathcal A^{\mathbf N^{\mathrm{op}}}}
(L_nB,I).
\tag{EXH1}
\]

The right side is acyclic because \(L_n\) is exact. The same adjunction shows
that each term of \(I_n\) is injective. Products of K-injective complexes
are K-injective: their Hom complexes are products of the corresponding Hom
complexes of modules, whose products are exact. Consequently the degreewise
product of the \(I_n\) computes the **derived** product in
\(D(\mathcal A)\), even when ordinary products in \(\mathcal A\) are not
exact. This is also the product argument in Propositions 5.3–5.4 of the
linked programme lesson.

The tower resolution also computes the full right derived limit. The constant-tower functor \(\mathrm{const}:\mathcal A\to\operatorname{Tow}(\mathcal A)\) is exact and left adjoint to limit. For an acyclic complex \(B\) of sheaves, its Hom-complex adjunction identifies

\[
\operatorname{Hom}^{\bullet}_{\mathcal A}(B,\lim I)
\simeq\operatorname{Hom}^{\bullet}_{\operatorname{Tow}(\mathcal A)}(\mathrm{const}\,B,I).
\tag{EXHU1}
\]

Thus \(\lim I\) is K-injective. The same adjunction on abelian objects shows that its terms are injective. Apply main E3–E4 degree by degree to the injective towers \(I^a\): their transitions split, and the kernel of \(1-s\) is \(\lim I\). These degreewise splittings need not commute with the differential. They give a short exact sequence of complexes and hence a quasi-isomorphism

\[
R\lim S=\lim I\longrightarrow\operatorname{Cone}(1-s)[-1].
\tag{EXHU2}
\]

With the cone convention of E4, a kernel element \(x\) is sent to \((0,x)\), and the fibre differential sends it to \((0,dx)\). This proves the kernel-to-fibre comparison on unbounded complexes without assuming exact products of sheaves.

Write \(s\) for the map whose \(n\)th component is the transition from
\(I_{n+1}\) after projection onto that factor. The strict restrictions
\(C\to S_n\to I_n\) commute with the transitions. They give the actual
chain map into the fibre model

\[
C\longrightarrow
\operatorname{Cone}\!\left(
1-s:\prod_n I_n\longrightarrow\prod_n I_n
\right)[-1].
\tag{EXH2}
\]

Its component in the target product is zero; strict compatibility makes the
chain-map identity hold. Thus the map is fixed before passing to the derived
category. A compatible comparison of replacements induces the same derived
restriction map. No uniqueness of a cone in a bare triangulated category is
being asserted.

Open restriction preserves these products and K-injective models. For the
first assertion, restriction is right adjoint to exact extension by zero.
For the second, apply the Hom-complex adjunction to that exact functor.
It therefore preserves the fibre in (EXH2).
Applied componentwise to tower complexes, open restriction likewise has the exact componentwise extension-by-zero left adjoint. It preserves their K-injective replacements, so the preceding derived-limit model commutes with open restriction. Removing finitely many indices is justified by the finite coordinate elimination in E5; its formulas use only finitely many terms in each output coordinate.
 On each open set
\(U_N=\operatorname{Int}_T(T_N)\), the source tower is the constant
\(C|_{U_N}\) from index \(N\) onward. To compare this tail through the resolution, choose a K-injective representative \(P\) of \(C|_{U_N}\). The constant tower of \(C|_{U_N}\) is quasi-isomorphic to the constant tower of \(P\). Resolve the latter by a K-injective complex \(J\) of injective towers. Its evaluated maps \(P\to J_n\) are quasi-isomorphisms between K-injective complexes, hence chain homotopy equivalences: the acyclic K-injective cone is contractible by testing its own identity in its Hom complex. Products of these homotopy equivalences are homotopy equivalences, since their homotopies are coordinatewise. The resulting strictly commuting square of difference maps therefore gives an equivalence of fibres. E5 computes the fibre for the constant tower of \(P\) by finite coordinate sums, obtaining \(P\) with its diagonal comparison. This proves the constant-tail assertion at the actual unbounded tower model. The restricted map in (EXH2) is consequently an equivalence. Since
these open sets cover \(T\), the stalk criterion proves (1) on all of
\(D(k_T)\).

Finally, derived sections preserve this fibre and its products. Sections
commute with ordinary products, module products are exact, and the preceding
K-injective calculation proves the derived assertion. Taking cohomology of
the module-product fibre gives (2) in every degree. A cohomological lower
bound was not used in this argument. The Mittag-Leffler condition in degree
\(q-1\) still governs whether the lim-one obstruction vanishes; enlarging
the derived input category does not remove that obstruction.

## SH02-EXH-MILNOR — The precise cohomological obstruction

Closed pushforward \(i_{n*}\) is exact and is right adjoint to the exact inverse-image
functor. Thus it preserves injectives, and

\[
R\Gamma(T,K_n)\simeq R\Gamma(T_n,i_n^{-1}K).
\]

The derived-sections functor commutes with homotopy inverse limits. Applying
the Milnor exact sequence to (1) gives, for every integer q,

\[
0\longrightarrow
\lim{}^1_n H^{q-1}(T_n,i_n^{-1}K)
\longrightarrow H^q(T,K)
\longrightarrow \lim_n H^q(T_n,i_n^{-1}K)
\longrightarrow0.                                            \tag{2}
\]

Consequently, the inverse-limit description of \(H^q(T,K)\) holds if the tower in
degree \(q-1\) is Mittag-Leffler: for each n, the images in its nth term from all
sufficiently late terms stabilize. Surjective transition maps in that degree
are one sufficient condition. The relevant condition is on degree \(q-1\);
Mittag-Leffler in degree \(q\) alone does not remove the left term in (2).
For all-degree continuity, check the required condition in every degree.

If every transition is an isomorphism in every degree, global cohomology is
identified with that on every piece. If transitions are eventually isomorphisms
in every degree, this conclusion holds in each degree on its stable tail. The
stabilization index may depend on the degree; a common tail requires a uniform
index. In degree q the obstruction also uses degree q-1, so take a tail beyond
both stabilization indices. No identification with arbitrary early pieces follows.

## SH02-EXH-TOWER-PROOFS — Tower resolutions, sections and the Milnor sequence

Here are proofs of the inverse-limit facts used above. They apply to the same bounded-below complexes and to left modules over any unital ring. Neither exactness of products of sheaves nor compactness of the closed pieces is assumed.

### Resolving the whole tower

Let \(\mathcal A\) be the category of sheaves of left \(k\)-modules on \(T\), and let \(\operatorname{Tow}(\mathcal A)\) consist of sequences \(F_{n+1}\xrightarrow{u_n}F_n\), indexed by the nonnegative integers. Its morphisms commute with all transitions. Kernels, cokernels and colimits are computed at each index, so it is abelian and has exact filtered colimits. These sheaf-category facts are proved in [Sheaves of modules on a ringed space, Theorems 2.1 and 3.1](../../../derived-categories-and-sheaf-operations/src/sheaves-of-modules-on-a-ringed-space.md#3-limits-colimits-stalks-and-sections-of-sums).

For an object \(M\) of \(\mathcal A\), define \(L_nM\) to have value \(M\) at indices \(0,\ldots,n\), zero at later indices, and identity transitions between its nonzero terms. A tower map \(L_nM\to F\) is determined by its component \(M\to F_n\): earlier components are its composites with the transitions. Thus \(L_n\) is an exact left adjoint of evaluation at \(n\). If \(U\) is a generator of \(\mathcal A\), then \(\bigoplus_{n\geq0}L_nU\) is a generator of the tower category: a nonzero tower morphism has a nonzero component, detected by a map from the corresponding \(L_nU\). The sheaf generator and its detection property are proved in [Proposition 1.1 of K-injective resolutions in Grothendieck abelian categories](../../../derived-categories-and-sheaf-operations/src/k-injective-resolutions-in-grothendieck-categories.md#1-the-grothendieck-hypotheses). Hom collections in the tower category are subsets of products of Hom sets, hence sets. Therefore it is a locally small Grothendieck abelian category.

The [injective embedding construction, Theorem 2.4](../../../derived-categories-and-sheaf-operations/src/k-injective-resolutions-in-grothendieck-categories.md#2-sizes-and-functorial-injective-embeddings), applies to this category. The [degree-by-degree resolution construction, Theorem 4.1](../../../derived-categories-and-sheaf-operations/src/injective-modules-and-bounded-below-derived-functors.md#4-right-derived-functors-on-bounded-below-complexes), consequently resolves any bounded-below complex of towers by a bounded-below complex \(J^\bullet\) of injective towers. In particular it applies to the strict tower \(i_{n*}i_n^{-1}C\) above. Evaluation preserves injectives, because its left adjoint \(L_n\) is exact: extending a map into an evaluated injective is the same as extending the adjoint map from the corresponding monomorphism of towers. Hence each evaluated complex \(J_n^\bullet\) is a bounded-below injective resolution of \(K_n\). All these resolutions have the same lower bound.

An injective tower \(J\) has split-surjective transitions. Indeed, \(L_n(J_n)\to L_{n+1}(J_n)\) is a monomorphism. The tower map from its source to \(J\) corresponding to \(1_{J_n}\) extends by injectivity. At index \(n+1\), the extension is a map \(\sigma_n:J_n\to J_{n+1}\) satisfying \(u_n\sigma_n=1_{J_n}\). For any family of morphisms \(y_n:M\to J_n\), set \(x_0=0\) and recursively set \(x_{n+1}=\sigma_n(x_n-y_n)\). This gives \(x_n-u_nx_{n+1}=y_n\). Applied to the projections from the product, the construction gives a right inverse of

\[
\delta:\prod_{n\geq0}J_n\longrightarrow\prod_{n\geq0}J_n,
\qquad \delta(x)_n=x_n-u_nx_{n+1}.
\tag{E3}
\]

Each coordinate of that right inverse uses only finitely many projections and splittings. It is a genuine morphism of sheaves, not an assumed ability to lift infinitely many local sections on a common neighbourhood. Its kernel is \(\lim_n J_n\), by the defining compatibility equations. The limit is also injective: limit is right adjoint to the exact constant-tower functor, so the same extension argument proves preservation of injectives.

Apply these facts separately in every degree of \(J^\bullet\). The splittings need not commute with its differential; they establish degreewise split exactness of

\[
0\longrightarrow\lim_n J_n^\bullet
\longrightarrow\prod_n J_n^\bullet
\xrightarrow{\delta}\prod_n J_n^\bullet\longrightarrow0.
\tag{E4}
\]

The kernel-to-fibre comparison is a quasi-isomorphism, by the cohomology sequence of this short exact sequence of complexes. In the cone convention \(d(y,x)=(dy+\delta x,-dx)\), the fibre is \(\operatorname{Cone}(\delta)[-1]\), its differential is \((y,x)\mapsto(-dy-\delta x,dx)\), and the comparison sends a kernel element \(x\) to \((0,x)\). This checks the actual comparison map and its signs.

The termwise limit of \(J^\bullet\) computes the right derived limit by the cited bounded-below derived-functor construction. Each product in (E4) represents the derived product of the \(K_n\): products of K-injective complexes are K-injective and represent derived products, as proved in [Proposition 5.4 of the K-injective lesson](../../../derived-categories-and-sheaf-operations/src/k-injective-resolutions-in-grothendieck-categories.md#5-derived-functors-adjoints-and-products). Thus (E4) proves the homotopy-limit triangle used in the geometric comparison, not merely a formula for an ordinary inverse limit. Comparison maps between tower resolutions are unique up to homotopy by the same bounded-below comparison theorem. The construction is therefore independent of the chosen resolution and natural in maps of strict towers.

### Restriction, finite initial segments and sections

For an open inclusion \(j:V\hookrightarrow T\), restriction is exact and has the exact left adjoint \(j_!\), proved in [Lemma 5.1 of the module-sheaf lesson](../../../derived-categories-and-sheaf-operations/src/sheaves-of-modules-on-a-ringed-space.md#5-extension-by-zero-and-skyscrapers). It therefore preserves injectives and K-injectives by the adjunction argument. Restriction also commutes with ordinary products: both products have sections on an open of \(V\) equal to the product of the same sections on that open in \(T\). Apply this to the resolved products in (E4). It proves commutation of restriction with the derived-product fibre, even though arbitrary products of sheaves need not be exact.

To remove the first \(N\) terms of a tower, split its resolved product into the first \(N\) factors and the tail. In these coordinates \(\delta\) is block upper triangular. Its head block is upper triangular with identity diagonal; backward substitution gives its inverse using only finite sums of transition maps. Eliminating this block identifies its cone with the cone of the tail block plus the contractible cone of an identity. Thus deleting the head preserves the homotopy fibre and its comparison maps. For a constant tail use one K-injective model \(I\) of its value. The coordinate transformation

\[
\prod_{n\geq0} I\longrightarrow I\oplus\prod_{n\geq0}I,
\qquad x\longmapsto\bigl(x_0,(x_n-x_{n+1})_n\bigr)
\tag{E5}
\]

is a chain isomorphism. Its inverse has coordinate \(a-\sum_{r<n}y_r\). It changes \(\delta\) into projection onto the second factor, whose homotopy fibre is \(I\). The diagonal map gives this identification. These computations justify precisely the local constant-tail step in (1).

Sections commute with products by the module-sheaf limit construction. The complexes in (E4), and their fibre, are K-injective; alternatively its kernel is a bounded-below complex of injectives by the limit argument above. Applying ordinary sections to these models therefore computes derived sections. Applying sections also commutes with the cone, since it commutes with finite sums and the displayed differentials. Consequently

\[
R\Gamma\bigl(T,\operatorname{holim}_nK_n\bigr)
\simeq\operatorname{Cone}\!\left(
\prod_n R\Gamma(T,K_n)\xrightarrow{1-\mathrm{shift}}
\prod_n R\Gamma(T,K_n)\right)[-1].
\tag{E6}
\]

Here the products on the right are represented by complexes of \(k\)-modules. Products of modules are exact: kernels are coordinatewise, and a product of surjections is surjective by choosing a lift in each coordinate. Hence cohomology of these products is the product of their cohomologies. The long exact sequence of the fibre (E6) gives a natural short exact sequence with left term the cokernel of \(1-\mathrm{shift}\) on the degree-\((q-1)\) product and right term its kernel on the degree-\(q\) product. For the present closed embeddings, exactness of \(i_{n*}\) follows on stalks: its stalks are the original stalks on \(T_n\), and zero off the closed set. Its exact left adjoint \(i_n^{-1}\) shows that it preserves injectives. The equality of ordinary sections then identifies \(R\Gamma(T,K_n)\) with \(R\Gamma(T_n,i_n^{-1}K)\), as used in (2).

For completeness, the cokernel just obtained is the first right derived limit of a module tower, not a new notation for a different obstruction. Resolve a module tower by injective towers and use (E4) in the module category. Exactness of products says that the products of the resolutions resolve the products of the original modules. Passing to their cones therefore identifies derived limit with the two-term complex \(\prod M_n\xrightarrow{1-\mathrm{shift}}\prod M_n\) in degrees zero and one. Its degree-zero cohomology is \(\lim M_n\), its degree-one cohomology is \(\lim^1 M_n\), and its higher cohomology is zero. Substitution into the preceding fibre sequence proves (2), with exactly the degree-\((q-1)\) obstruction asserted there.

### Why the Mittag–Leffler hypothesis kills that obstruction

Let \(M=(M_n,u_n)\) be a countable inverse sequence of left \(k\)-modules with stabilizing images. Let \(S_n\subset M_n\) be the eventual image in \(M_n\). The transitions carry \(S_{n+1}\) onto \(S_n\): choose an index beyond stabilization at both positions; a lift from that index of an element of \(S_n\) maps into \(S_{n+1}\). Put \(Q_n=M_n/S_n\). For every fixed \(n\), the transition \(Q_m\to Q_n\) is zero for all sufficiently large \(m\), since the corresponding image in \(M_n\) has become \(S_n\).

The difference map \(\delta_S\) on \(\prod S_n\) is onto. For a prescribed \(y\), start with \(x_0=0\) and choose \(x_{n+1}\) mapping to \(x_n-y_n\), using the surjective transitions. The difference map on \(\prod Q_n\) is invertible: if \(v_{n,m}:Q_m\to Q_n\) denotes the composite transition and \(v_{n,n}=1\), its inverse sends \(y\) to

\[
x_n=\sum_{m\geq n}v_{n,m}(y_m).
\tag{E7}
\]

For each \(n\) only finitely many summands can be nonzero, by the preceding eventual-zero property. Subtracting the shifted expression leaves \(y_n\). Conversely a compatible family in \(Q\) is zero because each coordinate is the image of an arbitrarily late coordinate and that transition eventually vanishes. This proves both inverse identities.

Products of the short exact sequences \(0\to S_n\to M_n\to Q_n\to0\) remain exact. Given \(y\in\prod M_n\), solve its image under \(\delta_Q\), lift that solution to \(x'\in\prod M_n\), and observe that \(y-\delta_Mx'\) lies in \(\prod S_n\). Surjectivity of \(\delta_S\) supplies \(z\) with this difference, and \(x'+z\) solves \(\delta_Mx=y\). Thus \(\lim^1 M_n=\operatorname{coker}\delta_M=0\). This proof uses the same classical choice convention as the injective constructions. It does not require finite generation, commutativity, a field, or a uniform stabilization index. Applied to the degree-\((q-1)\) tower it gives exactly the continuity criterion following (2), including all noncompact-strip restrictions.

## SH02-EXH-STRIPS — Noncompact-strip application

For an arbitrary topological space \(V\), take \(T=V\times\mathbb R\) and
\(T_n=V\times[-n,n]\) for positive integers n. These are closed, satisfy the interior
condition, and cover T. Thus (1) and (2) apply without requiring V to be compact.
Any claimed vanishing of the lim-one term still needs a separate proof for
the actual sheaf or complex under consideration. The geometry of the exhaustion
alone does not prove that condition.

## SH02-EXH-COUNTEREXAMPLE — Why the interior condition is substantive

A closed increasing cover alone does not suffice. Let \(T=[0,1]\),
\(T_n=\{0\}\cup[1/n,1]\) for \(n\geq2\), and \(K=\mathbb Z_T\). Each piece
has two components, hence degree-zero sections \(\mathbb Z^2\), and its
restriction transitions are identities. Global sections on the connected
interval are \(\mathbb Z\), with diagonal restriction. The degree-zero limit
comparison is therefore not an isomorphism. The interiors fail to cover zero,
exactly where the local proof cannot apply.

## SH02-EXH-LIMONE-EXAMPLE — A nonzero lim-one term on a half-line

Here the exhaustion has the required interiors and all its pieces are
compact. Nevertheless, the ordinary inverse limit misses global cohomology.
Take \(T=[0,\infty)\), \(T_n=[0,n]\) for \(n\geq0\), and integer
coefficients. Define a sheaf \(F\) with stalk \(\mathbb Z\) at every
integer \(m\) and with constant stalk \(\mathbb Z\) on every edge
\((m,m+1)\). The germ map from an integer to the edge on its right is the
identity; its germ map to the edge on its left is multiplication by two.
At zero only the right map exists.

Explicitly, a section on an open subset consists of one integer value at
each integer it contains and a locally constant integer-valued function on
each open-edge component. Near an included vertex the function on its right
has the vertex value, and the function on its left has twice that value.
Restrictions retain these data. Local compatible data glue uniquely, so this
description defines a sheaf. It also verifies its stated stalks and germ
maps; no abstract correspondence with a diagram category is needed.

Put \(F_n=F|_{T_n}\). A global section of \(F_n\) has vertex values
\(a_0,\ldots,a_n\) satisfying

\[
a_m=2a_{m+1}\qquad(0\leq m<n).
\tag{EXH3}
\]

Thus the last value identifies \(\Gamma(T_n;F_n)\) with \(\mathbb Z\).
Restriction from \(T_{n+1}\) to \(T_n\) becomes multiplication by two.
We also need the higher cohomology of the pieces, rather than just this
degree-zero computation.

For a closed interval or a point \(Z\subset T_n\), write
\(\mathbb Z_Z\) for exact closed pushforward of its constant sheaf. There
is a two-term acyclic resolution

\[
0\longrightarrow F_n\longrightarrow P_n^0
\xrightarrow{\delta_n}P_n^1\longrightarrow0,
\quad
\begin{aligned}
P_n^0&=\bigoplus_{m=0}^n\mathbb Z_{\{m\}}
\oplus\bigoplus_{m=0}^{n-1}\mathbb Z_{[m,m+1]},\\
P_n^1&=\bigoplus_{m=0}^{n-1}
\bigl(\mathbb Z_{\{m\}}\oplus\mathbb Z_{\{m+1\}}\bigr).
\end{aligned}
\tag{EXH4}
\]

For the \(m\)th edge, the two endpoint components of \(\delta_n\) are
\(e_m-a_m\) and \(e_m-2a_{m+1}\). At a nonvertex its target stalk is
zero and its source stalk is the edge copy. At an interior vertex, its two
endpoint components can be prescribed independently by the two edge germs;
the kernel consists of the vertex value and its two prescribed edge germs.
At a terminal vertex there is just one such equation. These stalk
calculations prove exactness and identify the kernel with \(F_n\).
They also define its inclusion by the vertex values and the edge functions
extended to their endpoints. For \(n=0\) the assertion is just the identity
of the point sheaf.

All the summands of \(P_n^0\) and \(P_n^1\) are acyclic for sections on
\(T_n\): points have exact sections, and closed constant intervals are
acyclic by [the interval criterion and its constant-coefficient calculation](../../SH02-convex-acyclicity.html#SH02-CA-INTERVAL).
Closed pushforward preserves that calculation. The sums are finite.
On global sections, eliminating the edge variables reduces the cokernel
of \(\delta_n\) to the cokernel of

\[
\mathbb Z^{n+1}\longrightarrow\mathbb Z^n,
\qquad(a_m)\longmapsto(a_m-2a_{m+1})_{0\leq m<n}.
\tag{EXH5}
\]

This map is onto: choose \(a_n=0\) and solve backward for any prescribed
right-hand side. The acyclic resolution now proves
\(H^q(T_n;F_n)=0\) for \(q>0\). Its degree-zero kernel is exactly (EXH3).

For the resulting tower, the ordinary limit is zero: each compatible
\(a_m\) is divisible by every power of two. Its derived first limit is the
cokernel of

\[
\Delta:\prod_{m\geq0}\mathbb Z\longrightarrow\prod_{m\geq0}\mathbb Z,
\qquad(x_m)\longmapsto(x_m-2x_{m+1}).
\tag{EXH6}
\]

Define \(\mathbb Z_2=\lim_r\mathbb Z/2^r\mathbb Z\). The sum
\(\sigma(y)=\sum_{m\geq0}2^my_m\) converges in \(\mathbb Z_2\) for
every integer sequence. The telescoping identity gives
\(\sigma(\Delta x)=x_0\). Hence it induces a map from the cokernel to
\(\mathbb Z_2/\mathbb Z\), using the ordinary integer embedding.
Every two-adic integer has a binary digit sequence, so that map is onto.
If \(\sigma(y)=c\) is an ordinary integer, put

\[
x_m=\frac{c-\sum_{r<m}2^ry_r}{2^m}.
\tag{EXH7}
\]

The numerator is an ordinary integer divisible by \(2^m\), because its
image in \(\mathbb Z/2^m\mathbb Z\) is zero. Thus each \(x_m\) is an
integer, and (EXH7) satisfies \(\Delta x=y\). This proves injectivity of
the cokernel map. The Milnor sequence therefore gives

\[
H^0(T;F)=0,\qquad
H^1(T;F)\simeq\mathbb Z_2/\mathbb Z,\qquad
H^q(T;F)=0\quad(q\geq2).
\tag{EXH8}
\]

The middle group is nonzero. For example, three is invertible in every
\(\mathbb Z/2^r\mathbb Z\), and its compatible inverses give a two-adic
integer satisfying \(3z=1\); no ordinary integer satisfies that equation.
The images in any fixed term of the tower are the strictly decreasing
subgroups \(2^r\mathbb Z\), so the tower is not Mittag-Leffler. In degree
one it is exactly the degree-zero lim-one term that survives. Compactness of
every closed piece and vanishing of all its positive cohomology have not
supplied the missing condition.

## SH02-EXH-DEPENDENCIES — Dependencies and attribution

This is a short independent bridge built from standard derived-sheaf facts,
not a claim of a new research theorem. The exact Stacks inputs are
[0D60](https://stacks.math.columbia.edu/tag/0D60) (derived sections and the Milnor
sequence) and [02UV](https://stacks.math.columbia.edu/tag/02UV) (closed pushforward
and cohomology). The internal tower proof supplies the derived extension-by-zero/restriction
comparison, the countable homotopy-limit triangle, invariance under removing a
finite initial segment, and the countable Mittag-Leffler vanishing theorem.
Their precise supporting tags are [00A7](https://stacks.math.columbia.edu/tag/00A7),
[01AK](https://stacks.math.columbia.edu/tag/01AK),
[01AX](https://stacks.math.columbia.edu/tag/01AX),
[08TC](https://stacks.math.columbia.edu/tag/08TC),
[07D9](https://stacks.math.columbia.edu/tag/07D9),
[0BK7](https://stacks.math.columbia.edu/tag/0BK7) and
[07KW](https://stacks.math.columbia.edu/tag/07KW). The nonunique-cone caution is
[0H9J](https://stacks.math.columbia.edu/tag/0H9J).

For noncommutative \(k\), the same additive arguments apply to left modules:
no tensor-product exactness, commutativity or finite global dimension is used.
For these coefficients, commutation of derived sections with derived inverse
limits follows from [08U1](https://stacks.math.columbia.edu/tag/08U1). Exact products
of modules then give the Milnor sequence by the same product-triangle argument
underlying 0D60. The internal tower and module proofs above establish these facts with this
coefficient interpretation; the links also provide source credit and further reading.

Original text is dedicated under CC0 1.0 Universal. 
