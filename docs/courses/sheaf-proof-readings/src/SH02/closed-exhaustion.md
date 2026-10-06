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

## SH02-EXH-DEPENDENCIES — Dependencies and attribution

This is a short independent bridge built from standard derived-sheaf facts,
not a claim of a new research theorem. The exact Stacks inputs are
[0D60](https://stacks.math.columbia.edu/tag/0D60) (derived sections and the Milnor
sequence) and [02UV](https://stacks.math.columbia.edu/tag/02UV) (closed pushforward
and cohomology). The proof also uses the derived extension-by-zero/restriction
adjunction, the countable homotopy-limit triangle, invariance under removing a
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
underlying 0D60. These contracts, including the stated
coefficient interpretation, must accompany integration into a course dependency map.

Original text is dedicated under CC0 1.0 Universal. No private source text or images are included. Course
integration, exact dependency registration, mathematical audit and rendering
remain separately recorded states.
