# Rational homotopy and the Hurewicz range

Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0.

The rational Thom computation needs a homotopy estimate with finite integral error groups. We prove its prerequisites here: one-group spaces and their finite-type homology, finite generation of homotopy, Hurewicz modulo finite groups, the complete higher product rule for the Serre cohomology spectral sequence, rational Eilenberg–MacLane rings, Serre sphere finiteness, and the Hurewicz range with its finite Thom-space consequence.

The exact earlier proofs are [Classifying maps](grassmannians-and-classifying-maps.md), [Thom and Euler classes](thom-classes-and-euler-classes.md), [Frame fields and primary obstructions](frame-fields-and-primary-obstructions.md), [The geometric Thom construction](thom-spaces-and-the-pontryagin-thom-construction.md), and [Homotopy fibres and the Serre spectral sequence](homotopy-fibres-and-the-serre-spectral-sequence.md). SectionsF–I continue the latter chapter's SectionsA–E. Six exercises have complete solutions. The [rational-bordism continuation](rational-oriented-bordism-and-projective-generators.md) proves the oriented cobordism rank, polynomial ring and torsion criterion.


## F. Spaces with one homotopy group

Write \(K(A,r)\) for a based, path-connected CW complex whose only nonzero positive-dimensional homotopy group is \(\pi_r=A\). For \(r\geq2\), the group \(A\) must be abelian. The models used here have \(A\) finitely generated. We construct them, prove the homology finiteness that is needed below, and realize the particular maps used to remove successive homotopy groups. None of these steps presupposes the rational cohomology ring of an Eilenberg–MacLane space.

References to Sections A–E in this section mean the [homotopy foundation companion](homotopy-fibres-and-the-serre-spectral-sequence.md). Its Theorems B.4–B.5 give homology comparison and CW models, its Theorem C.2 gives the homotopy sequence, and its Theorem D.1 and Exercise E.6 give the homology spectral sequence and all three finite-generation cases. The first Hurewicz theorem used here is the full proof in the frame-obstruction chapter, Lemma E.1.

### F.1. The integral algebra

**Lemma F.1.** A finitely generated abelian group is a direct sum
\[
A\cong\mathbb Z^s\oplus G,\qquad G\text{ finite}.
\tag{F.1}
\]
Its tensor product with \(\mathbb Q\) is \(\mathbb Q^s\). In particular such a group is finite if and only if its rational tensor product is zero.

**Proof.** A surjection \(\mathbb Z^m\to A\) has a free, finite-rank kernel, by the subgroup proof in the Thom-class chapter, Lemma 5.1. Choose its basis. The resulting integer matrix of relations can be diagonalized using integral row and column operations with integral inverses.

Here is the terminating procedure. Move a nonzero entry to the upper-left position and make it positive, say \(d\). Divide every other entry of its column and row by \(d\), subtracting the appropriate multiples of the pivot row or column. A nonzero remainder, moved to the pivot position, strictly decreases the positive pivot. Repeat. When all entries in the pivot row and column are multiples of \(d\), clear that column and then that row. If some remaining block entry \(b\) is not divisible by \(d\), add its row to the first row. The pivot is still \(d\), while the first row now contains \(b\). Division followed by a column interchange produces a positive pivot smaller than \(d\). Thus this also forces a strict decrease. Eventually the first row and column are cleared and \(d\) divides every entry in the remaining block. Apply the same procedure to the smaller block. The number of rows and columns decreases at each completed stage, so the procedure ends.

Every operation is a change of an integral basis and preserves the presented quotient. The diagonal entries contribute cyclic groups \(\mathbb Z/d\); the unpaired zero rows contribute copies of \(\mathbb Z\). Entries \(d=1\) contribute zero. Their finite direct sum gives (F.1). In a rational tensor product a finite-order element vanishes, whereas \(\mathbb Z\otimes\mathbb Q=\mathbb Q\), which proves the remaining assertions. ∎

We also make explicit why rational homology is integral homology tensored with \(\mathbb Q\). A rational tensor product can be described by fractions \(a/m\), \(m\) a positive integer, with the usual common-denominator equivalence. If \(A'\to A\to A''\) is exact, an element \(a/m\) mapping to zero has some positive multiple of \(a\) in the integral kernel. Replacing its denominator by that same multiple shows that it comes from \(A'\otimes\mathbb Q\). An integral injection stays injective by this fraction test, and a surjection stays surjective by lifting numerators. Thus tensoring with \(\mathbb Q\) is exact. Applying this to cycles, boundaries and their quotient gives, naturally,
\[
H_j(X;\mathbb Q)=H_j(X;\mathbb Z)\otimes\mathbb Q.
\tag{F.2}
\]
Tensoring vector spaces over \(\mathbb Q\) is likewise exact: choose a basis of a quotient and lift it, obtaining a splitting. These observations will also justify constant rational coefficients in the spectral sequence.

### F.2. General path covers and lifted cells

**Lemma F.2.** A connected CW complex has a simply connected covering. Coverings of CW complexes have the lifted-cell CW structure, and covering projection induces isomorphisms on \(\pi_i\) for \(i\geq2\).

**Proof.** Apply [Classifying maps, Theorem8.3](grassmannians-and-classifying-maps.md#8b-general-coverings-and-lifted-cw-cells). It constructs endpoint-fixed path classes, sheet charts on the explicitly proved simply connected neighbourhoods, interval/square and convex-cube lifts, and proves simple connectivity and the higher-group comparison. Its last part proves the actual weak topology and closure finiteness of lifted cells, using the characteristic quotient restricted to a sheet and compact attaching spheres. All coverings, rather than only double covers, occur in that proof.

The same theorem proves that prepending loop classes gives a free transitive deck action on each fibre of the path cover. These are the general covering facts used in the earlier local-coefficient cellular comparison and in the finite-group construction below. ∎

### F.3. A finite-group model in degree one

**Lemma F.3.** For a finite group \(G\), there is a one-vertex \(K(G,1)\) with \(|G|^j\) cells in dimension \(j\). Its integral homology is finitely generated in every degree, and its positive-dimensional rational homology is zero.

**Proof.** Form a cell complex \(EG\) with a simplex for every tuple
\[
(g_0,\ldots,g_j)\in G^{j+1}.
\]
Attach each face to the tuple obtained by deleting the corresponding entry. Keep repeated entries and their cells; no degeneracy identification is imposed. Face deletions satisfy the simplicial face identities, so all attaching identifications agree on intersections. Gluing disks in increasing dimensions gives the closure-finite Hausdorff CW complex with these open simplices and its weak topology.

There is a contraction, given in barycentric coordinates by
\[
[(g_0,\ldots,g_j);(t_0,\ldots,t_j)]
\longmapsto
[(1,g_0,\ldots,g_j);(u,(1-u)t_0,\ldots,(1-u)t_j)].
\tag{F.3}
\]
It agrees under face deletion. At \(u=0\) it is the original point, and at \(u=1\) it is the vertex labelled \(1\). Continuity on each characteristic simplex times \(I\), followed by the quotient-product lemma, proves continuity on \(EG\times I\). The vertex \(1\) may move along the cell \((1,1)\) during this contraction; a deformation retraction fixing that vertex is not being asserted.

Left multiplication by \(G\) acts on every entry of a tuple. Every point lies in a unique open simplex, and a nonidentity element preserves no such tuple, so the action on points is free. A finite free action on a Hausdorff space gives a covering quotient here, as follows. For \(x\) and each \(g\ne1\), separate \(x\) and \(gx\) by disjoint open sets \(O_g,V_g\). The intersection
\[
U=\bigcap_{g\ne1}(O_g\cap g^{-1}V_g)
\]
is a neighbourhood of \(x\) satisfying \(U\cap gU=\varnothing\) for every \(g\ne1\). Its translates are pairwise disjoint. The quotient map is open, since the saturation of an open set is the union of its translates. It consequently maps each translate homeomorphically onto the same open set in the quotient. This is an evenly covered neighbourhood.

Set \(BG=EG/G\). Cells in the quotient are tuple orbits, and each orbit has the unique representative with \(g_0=1\). Thus there is one vertex and \(|G|^j\) cells in dimension \(j\); the quotient weak topology is exactly that of these characteristic cells. The contractible cover shows that higher homotopy groups vanish, by Lemma F.2. A loop based at the quotient of \(1\) lifts from \(1\) and ends at a vertex \(g\). Every \(g\) occurs because \(EG\) is path connected. A lift ending at \(1\) contracts upstairs. Concatenation uses a translate of the second lift, so endpoints multiply in \(G\). The interval and square lifting proofs therefore give \(\pi_1(BG)=G\).

Its cellular chain groups are finite-rank free in each degree. The ordinary cellular-chain proof is the annular excision and skeleton-filtration argument already supplied in the frame-obstruction chapter, Lemma G.1 before applying \(\operatorname{Hom}\). Kernels and quotients of these finite-rank groups are finitely generated, proving the integral assertion.

For rational homology, define a transfer on a singular simplex by summing all its \(|G|\) lifts. A simplex lifts uniquely from any selected vertex, by Lemma F.2; restricting its lifts to a face enumerates exactly all the lifts of that face. The transfer is therefore a chain map, and its composition with projection is multiplication by \(|G|\). In positive degrees its target homology is zero because \(EG\) is contractible. Multiplication by the nonzero integer \(|G|\) is invertible over \(\mathbb Q\); consequently \(H_j(BG;\mathbb Q)=0\) for \(j>0\). ∎

For a finitely generated abelian \(A=\mathbb Z^s\oplus G\), take
\[
K(A,1)=(S^1)^s\times BG.
\tag{F.4}
\]
The covering \(\mathbb R^s\to(S^1)^s\) and its convex contraction give \(\pi_1=\mathbb Z^s\) and higher homotopy groups zero, by the same lifting argument. Maps and homotopies into a product are coordinatewise, so (F.4) has precisely the claimed homotopy groups.

We justify its CW and finiteness assertions. The finite torus has finitely many cells. A quotient map remains quotient after multiplication by a locally compact Hausdorff space: the compact-neighbourhood and tube argument in the earlier quotient-times-interval proof works with a compact neighbourhood of the chosen point in place of a compact subinterval. Thus the characteristic quotient for \(BG\), multiplied by the torus, is quotient. The finite characteristic quotient onto the torus is a continuous map from a compact space to a Hausdorff space and has compact fibres; its product with any space is closed. Indeed, if a closed set misses a fibre over a given pair, cover that compact fibre by finitely many product neighbourhoods missing the closed set, and intersect their neighbourhoods in the other factor. Then use closedness of the original map to shrink the neighbourhood downstairs. This proves product closedness and hence the quotient assertion for that second map. Combining the two quotients shows that the topology is the weak topology of the product characteristic disks. Their products are disks, and their faces are in preceding cells. Only finitely many cells occur in every dimension. Hence \(K(A,1)\) is a one-vertex CW complex and has finitely generated integral homology in all degrees.

### F.4. Higher models and comparison with any one-group space

**Lemma F.4.** For every finitely generated abelian group \(A\) and \(r\geq2\), there is an \((r-1)\)-connected one-vertex CW complex \(K(A,r)\).

**Proof.** Choose a finite free presentation
\[
0\longrightarrow R\longrightarrow\mathbb Z^m\longrightarrow A\longrightarrow0.
\tag{F.5}
\]
Start with a wedge of \(m\) positively oriented \(r\)-spheres. Its lower homotopy groups vanish by the proved cell-dimension connectivity statement. The first Hurewicz theorem identifies its \(\pi_r\) with its free cellular homology \(\mathbb Z^m\). For every basis element of the free, finite-rank group \(R\), attach an \((r+1)\)-cell along a sphere map representing that relation. The cellular boundary is the inclusion of \(R\): this is the Hurewicz class of its attaching sphere, expressed in the oriented \(r\)-cell basis. The resulting complex is still \((r-1)\)-connected and has \(H_r=A\), so its \(\pi_r\) is \(A\).

For \(j=r+1,r+2,\ldots\), attach a \((j+1)\)-cell for every element of the current \(\pi_j\). Choose cellular attaching representatives. Adjoining these cells preserves \(\pi_i\) for \(i<j\) and maps the old \(\pi_j\) onto the new one, by the cell-dimension assertion in Section B.2. Every old element bounds one of the attached disks, so the new \(\pi_j\) is zero. The same assertion preserves all lower groups already fixed.

Every attaching sphere has a finite cell carrier, and each attachment is therefore closure finite. At the union, every sphere map and every homotopy has a finite carrier, so lies in a finite construction stage. In each fixed degree the group has already been fixed at such a stage and subsequent higher-dimensional attachments preserve it. The union has the required homotopy groups. For \(A=0\), the point is also a permissible model. ∎

**Lemma F.5 — Comparison.** If \(Y\) is path connected and has only the homotopy group \(\pi_r(Y)=A\), with \(A\) finitely generated and abelian, the models above admit a map
\[
K(A,r)\longrightarrow Y
\tag{F.6}
\]
inducing any prescribed identification of that homotopy group. It is a weak homotopy equivalence and induces isomorphisms on all homology groups, with every abelian coefficient group.

**Proof.**

**Proof for \(r\geq2\).** Map the \(r\)-sphere generators in the finite starting wedge to representatives of their images in \(A\). Each relation in (F.5) then maps to zero in \(\pi_r(Y)\), so its \((r+1)\)-cell extends. Every subsequently attached cell has boundary dimension greater than \(r\), where \(Y\)'s homotopy group is zero; extend it as well. The characteristic weak topology gives a continuous based map. It is an isomorphism on \(\pi_r\) by its construction, and on all other groups because both sides have zero groups there. The homology assertion is Theorem B.4.

**Proof for \(r=1\).** We use the following elementary map construction. If \(C\) is a one-vertex connected CW complex, \(Y\) has \(\pi_i(Y)=0\) for \(i>1\), and \(\alpha:\pi_1(C)\to\pi_1(Y)\) is a homomorphism, map each edge loop to a representative of its image under \(\alpha\).

Every loop in the one-skeleton is a product of its edge loops and their inverses. To verify the assertion for continuous loops, first place the compact image in a finite graph. Cover that graph by small vertex stars and interior edge intervals, each a tree. A finite subdivision of the parameter interval makes each subpath lie in one such tree. Replace it, fixing its endpoints, by the unique reduced arc in that tree; contracting a tree gives the requisite path homotopy. These finitely many arcs form a finite piecewise edge path. When the endpoints are the vertex, reduction of adjacent partial segments gives an edge word. This proves the generation assertion without assuming a presentation theorem.

For the attaching loop of a two-cell, the edge map therefore induces \(\alpha\) composed with the map of the one-skeleton into \(C\). That attaching loop is zero in \(\pi_1(C)\), so its image is zero in \(\pi_1(Y)\); fill the disk. All later boundaries have dimension greater than one and fill because the corresponding homotopy group of \(Y\) is zero. The resulting map induces \(\alpha\) on every loop: cellular approximation moves a based loop of \(C\) into the one-skeleton, with its basepoint fixed. Apply this construction to the one-vertex model (F.4) and the prescribed isomorphism to \(\pi_1(Y)\). It gives (F.6), and Theorem B.4 again proves the homology assertion. ∎

There is no claim here of a full classification of maps from every CW complex by cohomology. The particular existence statement just proved will suffice for comparing loopspaces; the next realization lemma supplies the maps needed for connected covers.

### F.5. Finite-type homology of the models

**Theorem F.6.** For every finitely generated abelian group \(A\) and \(r\geq1\), all groups \(H_j(K(A,r);\mathbb Z)\) are finitely generated. If \(A\) is finite, then
\[
H_j(K(A,r);\mathbb Q)=0\quad(j>0).
\tag{F.7}
\]

**Proof.** The integral assertion for \(r=1\) was proved after (F.4). Induct on \(r\geq2\). The based path fibration has fibre \(\Omega K(A,r)\), total space the contractible space of paths starting at the basepoint, and simply connected CW base \(K(A,r)\). Currying cubes, as in Section C.1, identifies
\[
\pi_i(\Omega K(A,r))=\pi_{i+1}(K(A,r)),
\]
including the component statement \(\pi_0\Omega K(A,r)=\pi_1K(A,r)=0\). Thus the loopspace is path connected and has only \(\pi_{r-1}=A\). Lemma F.5 compares its homology with that of \(K(A,r-1)\). The induction hypothesis gives finite generation for the fibre, and the contractible total space has finitely generated homology. The missing-base case of Exercise E.6 now proves finite generation for \(K(A,r)\). This argument makes no assertion that the many cells in Lemma F.4 are finite in number.

For finite \(A\), the case \(r=1\) is Lemma F.3. Suppose the fibre in the same path fibration has rational homology only in degree zero, where it is \(\mathbb Q\). Its Serre second page is then only the bottom row \(H_p(K(A,r);\mathbb Q)\). Every higher differential is zero for degree reasons. Convergence to the contractible total space forces that row to be zero in every positive degree, proving (F.7) by induction. Together with (F.2), Lemma F.1 and the integral finite generation, it also proves that the integral homology groups in positive degrees are finite when \(A\) is finite. ∎

### F.6. Realizing a first homology homomorphism

**Lemma F.7.** Suppose \(r\geq2\), \(X\) is an \((r-1)\)-connected CW complex, \(A\) is finitely generated abelian, and \(\alpha:H_r(X;\mathbb Z)\to A\) is a homomorphism. There is a based map
\[
g:X\longrightarrow K(A,r)
\tag{F.8}
\]
whose homology map in degree \(r\), followed by the inverse first Hurewicz identification \(H_r(K(A,r))=A\), is \(\alpha\).

**Proof.** In the CW-model construction of Theorem B.5, all stages below \(r\) can be omitted because their target homotopy groups are zero. At stage \(r\), attach spheres representing \(\pi_r(X)\), and proceed with the kernel-killing and representative steps of that construction. This yields a CW complex \(C\), with one vertex and no cells in dimensions \(1,\ldots,r-1\), and a weak equivalence \(f:C\to X\). The CW Whitehead proof at the end of Section B.4 supplies a homotopy inverse. A basepoint path can be corrected using homotopy extension at the vertex; since the spaces are simply connected, the associated change on \(\pi_r\) is unique. We may use a based inverse.

The \(r\)-skeleton of \(C\) is a wedge of \(r\)-spheres. Map each of its positively oriented generators into \(K(A,r)\) with first Hurewicz class equal to its image under \(\alpha f_*\). For every \((r+1)\)-cell, its attaching sphere's Hurewicz class is its cellular boundary in this free \(r\)-cell group. That boundary vanishes in \(H_r(C)\). By naturality of the first Hurewicz isomorphism, its image in \(\pi_r(K(A,r))\) is therefore zero, and the map extends over the cell. All higher attaching spheres map to zero because the target has no higher homotopy groups. Extend cell by cell, using the weak topology.

In degree \(r\), cellular homology is the free group on the \(r\)-cells modulo these \((r+1)\)-cell boundaries. The constructed map has exactly the required value on every generator and hence on that quotient. Compose it with the based homotopy inverse \(X\to C\). Its induced map is \(\alpha\), as asserted. ∎

In particular, for \(\alpha\) equal to the inverse first Hurewicz isomorphism \(H_r(X)\to\pi_r(X)\), whenever this group is finitely generated, (F.8) induces the identity on \(\pi_r\). The homotopy fibre is \(r\)-connected and retains every homotopy group in dimensions greater than \(r\), by Theorem C.2. Passing to a CW model of that fibre preserves its homology and homotopy. Only finitely many such replacements will ever be made at a time.

### F.7. Finite generation of homotopy and Hurewicz modulo finite groups

**Theorem F.8.** If \(X\) is a simply connected CW complex and \(H_j(X;\mathbb Z)\) is finitely generated for every \(j\), then \(\pi_j(X)\) is finitely generated for every \(j\geq1\).

**Proof.** Its first group is zero, and the first Hurewicz theorem gives \(\pi_2(X)=H_2(X)\), which is finitely generated. More generally, let \(C\) be an \((r-1)\)-connected CW complex reached by the previous steps, with finitely generated integral homology and the same homotopy groups as \(X\) in dimensions at least \(r\). Its first Hurewicz isomorphism gives
\[
A=\pi_r(C)=H_r(C),
\]
so \(A\) is finitely generated. Use Lemma F.7 to choose \(g:C\to K(A,r)\) inducing the identity on \(\pi_r\). Its path-space replacement has total space homotopy equivalent to \(C\), simply connected CW base \(K(A,r)\), and \(r\)-connected homotopy fibre \(Y\), by Theorem C.2. The base has finitely generated homology by Theorem F.6. The missing-fibre case of Exercise E.6 consequently gives finitely generated homology for \(Y\).

Take a CW model \(C'\to Y\). Theorems B.4–B.5 preserve this homology and all homotopy groups, and \(C'\) is \(r\)-connected. The homotopy sequence identifies its homotopy groups in dimensions greater than \(r\) with those of \(C\), hence of \(X\). This is the next induction step. After finitely many steps, the first Hurewicz isomorphism computes any fixed \(\pi_j(X)\) as a finitely generated homology group. No limit of an infinite tower is needed. ∎

**Theorem F.9 — Hurewicz modulo finite groups in finite type.** Under Theorem F.8's hypotheses, let \(n\geq2\) and suppose that \(\pi_i(X)\) is finite for \(2\leq i<n\). Then the ordinary Hurewicz map has finite kernel and finite cokernel:
\[
h:\pi_n(X)\longrightarrow H_n(X;\mathbb Z).
\tag{F.9}
\]
Equivalently, \(h\otimes\mathbb Q\) is an isomorphism. Also \(H_i(X;\mathbb Q)=0\) for \(0<i<n\).

**Proof.** For \(n=2\) this is the first Hurewicz theorem. Otherwise perform the connected-cover construction in Theorem F.8 through dimensions \(2,\ldots,n-1\). Each group removed is the corresponding finite group of \(X\), because previous removals preserve the higher homotopy groups. Its base \(K(A,r)\) is rationally acyclic in positive degrees, by (F.7).

In such a step, for any rational vector space \(V\), the singular chain complex gives
\[
H_p(K(A,r);V)=H_p(K(A,r);\mathbb Q)\otimes_{\mathbb Q}V.
\]
Exactness of tensoring vector spaces, proved after (F.2), justifies this formula even for infinite-dimensional \(V\). Thus the path-replacement fibration has a Serre second page with only column zero, containing the rational homology of its fibre. There can be no differentials, and its finite filtration has a single nonzero quotient in each degree. The actual fibre edge in Section D.3 shows that fibre inclusion, followed by the total-space retraction to \(C\), is an isomorphism on rational homology in every degree.

At the end there is an \((n-1)\)-connected CW complex \(C\) and a composite map \(u:C\to X\). The homotopy sequence makes \(u_*\) an isomorphism on \(\pi_n\); the preceding edge argument makes it an isomorphism on all rational homology. Naturality of Hurewicz gives the commuting square
\[
\begin{array}{ccc}
\pi_n(C)\otimes\mathbb Q&\xrightarrow{\,h_C\otimes\mathbb Q\,}&H_n(C;\mathbb Q)\\
\downarrow u_*&&\downarrow u_*\\
\pi_n(X)\otimes\mathbb Q&\xrightarrow{\,h_X\otimes\mathbb Q\,}&H_n(X;\mathbb Q).
\end{array}
\tag{F.10}
\]
The top and both vertical arrows are isomorphisms, so the bottom arrow is an isomorphism. The first Hurewicz theorem also makes \(H_i(C;\mathbb Z)=0\) for \(0<i<n\); its rational comparison with \(X\) gives the asserted lower vanishing.

Both groups in (F.9) are finitely generated, by the hypotheses and Theorem F.8. Their kernel and cokernel are finitely generated by the subgroup and quotient assertions in Exercise E.6. Tensoring the exact kernel-image-cokernel sequences with \(\mathbb Q\) shows that these two groups have zero rational tensor product. Lemma F.1 therefore makes them finite. ∎

This is the precise form of the modulo-finite Hurewicz principle now proved. It still does not assert a stable Hurewicz range for every highly connected finite complex: establishing that range requires the rational calculation of \(K(A,r)\) for \(A\) with a free summand. That calculation, and the Serre sphere theorem used in the rational Thom argument, follow later.

**References.** Allen Hatcher's [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) develops the tuple model and cell-by-cell maps to \(K(G,1)\). His [*Spectral Sequences*](https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf) treats finite generation and Hurewicz modulo Serre classes. The proofs here use the covering theorem, the full three-case finite-generation argument of Exercise E.6, and the cell-level realization in Lemma F.7.

## G. The cohomology product and every higher differential

This section supplies the multiplicative step in the rational calculation. Its exact scope is a Hurewicz fibration \(p:E\to B\), with simply connected CW base \(B\), path-connected fibre \(F\), and finite-dimensional \(H_j(B;\mathbb Q)\) and \(H_j(F;\mathbb Q)\) in each degree. All chains and cochains in this section have coefficients in \(\mathbb Q\). The homology construction is Theorem D.1 of the foundation companion.

**Theorem G.1.** There is a cohomological spectral sequence
\[
E_2^{a,b}=H^a(B;\mathbb Q)\otimes H^b(F;\mathbb Q),
\qquad
d_r:E_r^{a,b}\longrightarrow E_r^{a+r,b-r+1},
\tag{G.1}
\]
converging to a finite filtration of \(H^{a+b}(E;\mathbb Q)\). From page two onward its product is associative, unital and graded commutative by total degree. On the second page it is
\[
(u\otimes v)(u'\otimes v')
=(-1)^{b a'}(u\smile u')\otimes(v\smile v').
\tag{G.2}
\]
Every differential satisfies
\[
d_r(xy)=d_r(x)y+(-1)^{a+b}x\,d_r(y),
\qquad x\in E_r^{a,b}.
\tag{G.3}
\]
The final product is the associated graded product of the ordinary cup product on \(H^*(E;\mathbb Q)\). Maps of fibrations give the usual maps on page two, after cellular approximation of the base map if necessary.

**Proof.**

### G.1. Dual filtration and convergence

Put \(E_a=p^{-1}(B^a)\), \(E_{-1}=\varnothing\), and
\[
C=C_*(E;\mathbb Q),\qquad F_aC=C_*(E_a;\mathbb Q).
\]
The filtration is exhaustive by the projected compact-cell-carrier argument in Section D.1. On \(C^*=\operatorname{Hom}_{\mathbb Q}(C,\mathbb Q)\) use the decreasing filtration
\[
\mathcal F^a C^*=\{c:c|_{F_{a-1}C}=0\},
\quad
\mathcal F^a C^*=C^*\text{ for }a\leq0.
\tag{G.4}
\]
Linear maps on a vector subspace extend to the ambient space by extending a basis. Hence the associated quotient of (G.4) is the dual of \(F_aC/F_{a-1}C\), and taking cohomology of that dual is the dual of its homology. The latter assertion also follows by splitting a chain complex into its homology and two-term contractible summands, using complements of boundaries in cycles and cycles in chains.

The actual relative groups computed in Section D.1 consequently give
\[
E_1^{a,b}
=\prod_{\text{\(a\)-cells of }B}H^b(F;\mathbb Q).
\tag{G.5}
\]
Transposing the signed cellular boundary of Section D.2 gives the cellular cochain differential with that constant coefficient vector space. The cellular comparison, including its passage to infinitely many cells, was proved in the frame-obstruction chapter, Lemma G.1. It follows that the second page is \(H^a(B;H^b(F;\mathbb Q))\). Since \(H^b(F;\mathbb Q)\) is finite dimensional, a basis identifies its coefficient cochain complex with a finite direct sum of the rational cochain complex of \(B\). Thus it is the tensor product in (G.1); this identification is natural in the coefficient vector space.

Here is the representative algebra and the convergence assertion. For a decreasing filtration define
\[
\begin{split}
Z_r^{a,n}&=\{x\in\mathcal F^a C^n:\delta x\in\mathcal F^{a+r}C^{n+1}\},\\
T_r^{a,n}&=\mathcal F^a C^n\cap\delta(\mathcal F^{a-r}C^{n-1}).
\end{split}
\]
For \(r\geq1\), its page is
\[
E_r^{a,n-a}
=Z_r^{a,n}/\bigl(Z_{r-1}^{a+1,n}+T_{r-1}^{a,n}\bigr).
\tag{G.6}
\]
The same kernel-and-image calculation as Theorem A.1, with the direction of the filtration reversed, defines \(d_r[x]=[\delta x]\) and gives \(E_{r+1}=H(E_r,d_r)\). Explicitly, if \(\delta x=w+\delta v\) is zero on its target page, then \(v\in\mathcal F^{a+1}\) and \(w\in\mathcal F^{a+r+1}\). Subtracting \(v\) gives a representative in \(Z_{r+1}^{a,n}\). The incoming images enlarge the boundary subgroup from \(T_{r-1}\) to \(T_r\); the remaining denominator is \(Z_r^{a+1,n}\). This is exactly (G.6) for the next page.

Relative groups in (G.5) vanish below total degree \(a\). Therefore, for fixed \(n\), the pair cohomology sequences show that \(H^n(E_a)\) stabilizes once \(a\geq n+1\), and restriction to \(E_n\) is injective on that stable value. There is no assumed inverse-limit formula here. Singular chains are the union of the \(C_*(E_a)\), so cochains are their inverse limit, and restrictions of cochains are degreewise onto. The short exact sequence of complexes
\[
0\longrightarrow C^*(E)
\longrightarrow\prod_a C^*(E_a)
\xrightarrow{\,D\,}\prod_a C^*(E_a)
\longrightarrow0,\qquad
D(c)_a=c_a-\operatorname{res}c_{a+1},
\tag{G.7}
\]
is exact: lift the coordinates successively to prove surjectivity. Cohomology of a product is the product of cohomology, since kernels, images and choices of preimages are coordinatewise. On the stabilized cohomology towers, \(D\) is onto: solve in the isomorphic tail and then solve backward through the finitely many earlier coordinates. The long exact sequence of (G.7) therefore identifies \(H^n(E)\) with the stabilized \(H^n(E_a)\).

The resulting filtration is
\[
\mathcal F^a H^n(E)
=\ker\bigl(H^n(E)\to H^n(E_{a-1})\bigr),
\quad
\mathcal F^0H^n(E)=H^n(E),\quad
\mathcal F^{n+1}H^n(E)=0.
\tag{G.8}
\]
Exactness of the cochain pair sequences identifies this kernel with the image of filtered cocycles. The first-quadrant page calculation on the finite skeleton \(E_{n+1}\), followed by that stabilized identification, gives
\[
E_\infty^{a,n-a}=\mathcal F^aH^n(E)/\mathcal F^{a+1}H^n(E).
\]
This is the asserted finite convergence. Naturality follows by transposing the filtered homology maps in Section D.3.

### G.2. A filtered inverse to the cross product

The ordinary Alexander–Whitney diagonal need not preserve the total base-cell filtration. We construct a chain diagonal which does preserve it.

First use the **weak product** \(P=B\mathbin{\boxtimes}B\): it has cells \(e^i\times e^j\), with the weak topology of their product characteristic disks, and skeleton
\[
P^a=\bigcup_{i+j\leq a}B^i\times B^j.
\]
Its cell closures are finite, so it is a CW complex. Its identity map to the ordinary product \(B\times B\) is continuous on every characteristic disk and hence continuous. A map from a compact space into the ordinary product has each coordinate in a finite subcomplex. The product of those two finite subcomplexes has its ordinary compact CW topology and is a finite subcomplex of \(P\). Hence that map is continuous into \(P\) as well. In particular singular simplices, cube maps and their homotopies are the same in these two products. This proves that \(P\) is simply connected. The diagonal \(B\to P\) is continuous: on each characteristic disk its image is in such a finite product, and the CW weak topology tests continuity there.

Pull the product fibration back along \(P\to B\times B\), and call its total space \(E^{(2)}\). Its underlying points are those of \(E\times E\), together with their base point in \(P\). The same compact-carrier observation shows that
\[
C_*(E^{(2)})=C_*(E\times E)
\tag{G.9}
\]
as singular complexes: a singular simplex in the ordinary product lifts continuously to the pullback because its projected base map is continuous into \(P\). Filter the left side by the inverse images of \(P^a\).

On \(C\otimes C\) use
\[
F_a(C\otimes C)=\sum_{i+j\leq a}F_iC\otimes F_jC.
\]
The lattice-path cross product proved in the Thom-class chapter, Lemma 4.1, is a filtered chain map
\[
\kappa:C\otimes C\longrightarrow C_*(E^{(2)}).
\tag{G.10}
\]
Indeed the cross product of a simplex over \(B^i\) and one over \(B^j\) lies over \(P^{i+j}\). Its relative first-page map is an isomorphism. To see this explicitly, over a product cell its map is the cross product of the two positive disk generators and the two fibre homology classes. Moving the first fibre factor of degree \(b\) past the second disk of degree \(j\) contributes \((-1)^{bj}\). The rational cross product
\[
H_*(F;\mathbb Q)\otimes H_*(F;\mathbb Q)
\longrightarrow H_*(F\times F;\mathbb Q)
\]
is an isomorphism: split each rational chain complex into homology and contractible pairs, tensor the splittings, and use the two natural chain homotopies between cross product and Alexander–Whitney from the Thom-class chapter. This proves the isomorphism on every relative cell summand. The same splitting argument computes the associated graded of \(C\otimes C\) as the tensor product of the associated graded complexes. Thus the associated graded of the mapping cone of \(\kappa\) is acyclic.

Here is why this yields an actual **filtered chain homotopy inverse**, rather than merely a map of pages. For any exhaustively, nonnegatively filtered rational chain complex \(L\) with acyclic associated graded, choose vector-space splittings of its filtration. In those coordinates its differential is \(d=d_0+\epsilon\), where \(d_0\) preserves the filtration degree and \(\epsilon\) lowers it. Contract each acyclic associated graded complex, and let \(h_0\) be the direct sum of those contractions. Then
\[
dh_0+h_0d=1+N,\qquad
N=\epsilon h_0+h_0\epsilon
\tag{G.11}
\]
lowers filtration by at least one. On every chain the finite series
\[
(1+N)^{-1}=1-N+N^2-\cdots
\]
terminates. Moreover \(1+N\) commutes with \(d\), directly from \(d^2=0\). Hence
\[
h=h_0(1+N)^{-1}
\quad\text{satisfies}\quad dh+hd=1
\tag{G.12}
\]
and preserves the filtration. This proves a filtered contraction.

Apply it to the cone of (G.10), with differential
\[
(v,u)\longmapsto(dv+\kappa u,-du).
\]
The lower-left block of its contraction is a filtered chain map
\[
\lambda:C_*(E^{(2)})\longrightarrow C\otimes C.
\tag{G.13}
\]
The upper-left block of \(dh+hd=1\) says that \(\kappa\lambda\) is homotopic to the identity by a filtered homotopy. The lower-right block says the same for \(\lambda\kappa\), with the corresponding sign in its homotopy. Thus (G.13) is the required filtered inverse. All series are finite on individual chains; no completion of chains or uniform filtration bound in each chain degree has been assumed.

### G.3. A filtered diagonal and the cup product

Use the full cellular approximation theorem in the geometric Thom chapter to deform the diagonal \(B\to P\) to a cellular map \(\delta:B\to P\), fixing the reference vertex. Lift this base homotopy into \(E^{(2)}\), with parameter space \(E\), starting with its ordinary diagonal. The endpoint is a map
\[
D:E\longrightarrow E^{(2)}
\quad\text{over }\delta.
\]
It sends \(E_a\) to the inverse image of \(P^a\), so its singular chain map is filtered. The composite
\[
\Delta_f=\lambda D_\#:C\longrightarrow C\otimes C
\tag{G.14}
\]
is therefore a filtered chain map. For cochains define
\[
\mu(c,c')=(c\otimes c')\Delta_f.
\]
Here a tensor cochain is evaluated directly on the matching two chain degrees, with the usual total tensor differential. Consequently
\[
\delta\mu(c,c')=\mu(\delta c,c')+(-1)^{|c|}\mu(c,\delta c'),
\qquad
\mu(\mathcal F^a,\mathcal F^{a'})\subset\mathcal F^{a+a'}.
\tag{G.15}
\]
The filtration assertion follows term by term: in filtration degree less than \(a+a'\), every tensor term has either its first degree less than \(a\) or its second degree less than \(a'\), so one cochain vanishes on it.

On ordinary cohomology, \(\mu\) is the usual cup product. The unfiltered Alexander–Whitney map \(A:C_*(E\times E)\to C\otimes C\) is a chain homotopy inverse to \(\kappa\), by the two proved homotopies in the Thom-class chapter. It is chain homotopic to \(\lambda\): composing the homotopy \(\kappa\lambda\simeq1\) with \(A\), and then using \(A\kappa\simeq1\), gives that comparison. The map \(D\) is homotopic to the ordinary diagonal by its defining lift. Thus (G.14) is chain homotopic to the ordinary Alexander–Whitney diagonal. Evaluating cocycles on a chain homotopy changes their product by a coboundary. This proves the assertion about ordinary cohomology.

We identify its second-page product as well. Naturality of the relative disk calculation in Section D.3 says that \(D\)'s first-page map is the cellular chain map of \(\delta\), with the fibre diagonal on homology. Over the fixed vertex the lifted homotopy stays in \(F\times F\), so its fibre map is homotopic to that diagonal. Over a source disk, trivialize both pullbacks; contracting the source disk makes the fibre part constant while retaining the base part, exactly as in Section D.2's signed local-degree proof. Hence each product-cell coefficient is its cellular degree times this fibre diagonal. The inverse (G.13) reverses the disk-first cross product and its sign \((-1)^{bj}\).

After dualizing and taking cellular cohomology, the base diagonal is ordinary cup product on \(H^*(B)\). This follows also by applying (G.10)–(G.14) to the identity fibration of \(B\): its cellular diagonal is homotopic to the ordinary diagonal and its cross product has the same unfiltered inverse comparison just proved. The fibre factor is ordinary cup product on \(H^*(F)\), by the original cross-product/Alexander–Whitney comparison. Moving the fibre class of degree \(b\) past the second base class of degree \(a'\) gives precisely (G.2).

### G.4. The product descends to all pages

We verify the point that cannot be inferred solely from a picture of an exact couple. If \(x\in Z_r^{a,n}\) and \(y\in Z_r^{a',n'}\), (G.15) makes their product an element of \(Z_r^{a+a',n+n'}\). A denominator change \(x\mapsto x+z\), with \(z\in Z_{r-1}^{a+1,n}\), changes the product by an element of \(Z_{r-1}^{a+a'+1,n+n'}\): its filtration is one higher, and (G.15) puts its derivative in \(\mathcal F^{a+a'+r}\).

For a boundary denominator write \(z=\delta v\in\mathcal F^a\), where \(v\in\mathcal F^{a-r+1}\). Then
\[
\mu(\delta v,y)
=\delta\mu(v,y)-(-1)^{n-1}\mu(v,\delta y).
\tag{G.16}
\]
The first term is in \(T_{r-1}^{a+a',n+n'}\): its primitive has filtration \(a+a'-r+1\), and its derivative has filtration at least \(a+a'\). The second term has filtration at least \(a+a'+1\), and its derivative has filtration at least \(a+a'+r\). It is therefore in \(Z_{r-1}^{a+a'+1,n+n'}\). Changes of the right factor obey the same calculation with the tensor sign. Thus the product is well-defined on (G.6).

Applying (G.15) to representatives now gives (G.3) exactly, with sign by total degree. The product on the next page is its induced product on the homology of the preceding page. Since the second-page product (G.2) is associative, unital and graded commutative, these properties pass successively to every later page. Strict associativity of the chosen chain map (G.14) is unnecessary. Its ordinary cohomology comparison, together with (G.8) and the filtration assertion in (G.15), proves that the limiting product is the associated graded of ordinary cup product.

Choices of cellular diagonal, lift and filtered inverse all give (G.2). Since every subsequent page product is induced from its predecessor, these choices give the same product on the naturally identified pages from page two onward. Naturality of the additive second-page maps is Section D.3, and there they are the actual base and fibre cohomology maps. They preserve (G.2); induction on pages therefore proves multiplicative naturality in the stated scope. This completes Theorem G.1. ∎

**Reference.** Allen Hatcher's [*Spectral Sequences*](https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf) discusses the cohomology sequence and its products. The construction above gives the filtered inverse, diagonal and representative-level product formulas used below.

## H. Rational one-group spaces, spheres and the Hurewicz range

We now use the complete multiplicative construction in Section G. All Eilenberg–MacLane groups in this section are finitely generated. Their finite-type homology, the required first-degree map realization and Hurewicz modulo finite groups were proved in Section F.

### H.1. Rational cohomology of \(K(A,n)\)

For a graded rational vector space concentrated in degree \(n\), its free graded-commutative algebra is a polynomial algebra when \(n\) is even and an exterior algebra when \(n\) is odd. In the odd case the square of a generator is zero because \(x^2=-x^2\) and \(2\) is invertible in \(\mathbb Q\).

**Theorem H.1.** If \(A\cong\mathbb Z^s\oplus G\), with \(G\) finite, then
\[
H^*(K(A,n);\mathbb Q)
\cong
\begin{cases}
\mathbb Q[x_1,\ldots,x_s],&n\text{ even},\\
\Lambda_{\mathbb Q}(x_1,\ldots,x_s),&n\text{ odd},
\end{cases}
\qquad |x_i|=n.
\tag{H.1}
\]
More precisely the cup-product map from the free graded-commutative algebra on \(H^n(K(A,n);\mathbb Q)=(A\otimes\mathbb Q)^*\) is an isomorphism. Consequently
\[
H_j(K(A,n);\mathbb Q)=0\quad(0<j<n\text{ or }n<j<2n),
\qquad H_n(K(A,n);\mathbb Q)=A\otimes\mathbb Q.
\tag{H.2}
\]

**Proof.**

**Proof: the first degree and induction setup.** For \(n=1\), use the model \((S^1)^s\times BG\). The rational homology of \(BG\) is concentrated in degree zero, by the transfer proof in Lemma F.3. The rational cross-product chain equivalence and vector-space splitting proof in Section G.2 give the tensor-product cohomology ring of this finite product. A circle has one generator in degree one and no positive cohomology in higher degrees; multiplying circle generators gives the exterior algebra. Graded commutativity gives its signs. This proves (H.1) for \(n=1\). If \(s=0\), the rational acyclicity of Theorem F.6 proves the assertion in every degree.

Induct on \(n\geq2\), with \(s>0\). Set
\[
R=H^*(K(A,n);\mathbb Q),\qquad
S=H^*(\Omega K(A,n);\mathbb Q).
\]
Lemma F.5 compares the loopspace with \(K(A,n-1)\), so the induction hypothesis says that \(S\) is the free graded-commutative algebra on \(s\) generators \(y_i\) of degree \(n-1\). The based path fibration has contractible total space. Its second page is \(R\otimes S\), with its actual tensor-product ring and every higher Leibniz identity from Theorem G.1.

The base is \((n-1)\)-connected, so \(R^a=0\) for \(0<a<n\) and \(R^n=(A\otimes\mathbb Q)^*\), by the first Hurewicz theorem and rational duality. No differential before page \(n\) can leave a \(y_i\): its target base degree is between one and \(n-1\). Nor can a differential leave the bottom-row ring \(R\). Since these elements generate \(R\otimes S\), the Leibniz identity shows that all differentials before \(d_n\) vanish.

The map
\[
d_n:E_n^{0,n-1}\longrightarrow E_n^{n,0}
\tag{H.3}
\]
is an isomorphism. Its source has no incoming differential and no possible later outgoing differential; its target has no outgoing differential, and no other incoming one. A kernel or cokernel would therefore survive to positive-degree cohomology of the contractible total space. Choose the generators so that
\[
d_n y_i=x_i,\qquad (x_1,\ldots,x_s)\text{ a basis of }R^n.
\tag{H.4}
\]
The entire \(d_n\) is then the derivation prescribed by (H.4).

**Proof: ruling out hidden generators and relations.** Let \(P\) be the free graded-commutative algebra on these \(x_i\), all of degree \(n\), and let \(\varphi:P\to R\) be cup product. Give \(P\otimes S\) the differential \(d y_i=x_i\), \(d x_i=0\). This complex has homology \(\mathbb Q\) in bidegree \((0,0)\) and zero elsewhere.

Here is the algebra proof. When \(n\) is even, a single factor is
\(\mathbb Q[x]\otimes\Lambda(y)\), with \(d(f(x)y)=f(x)x\); multiplication by \(x\) is injective and its quotient is \(\mathbb Q\). When \(n\) is odd, a single factor is
\(\Lambda(x)\otimes\mathbb Q[y]\), with
\[
d(y^j)=jxy^{j-1},\qquad d(xy^j)=0.
\tag{H.5}
\]
The derivative map on rational polynomials is onto, and its kernel is the constants. Again the homology is just \(\mathbb Q\). The many-generator complex is the tensor product of these factors, with the graded tensor differential. Splitting vector complexes into homology and contractible pairs, as in Section G.2, proves the same assertion for that tensor product.

Suppose \(m>n\) is the first degree in which \(\varphi\) is not an isomorphism. The coefficient groups of \(P\otimes S\to R\otimes S\) are then isomorphic whenever their base degree is less than \(m\). In particular, at every positive-total-degree bidegree with base degree \(a\) satisfying \(a+n<m\), the kernel and image calculation for \(d_n\) is identical to that of the free complex. Thus its \(E_{n+1}\) entry is zero.

First suppose \(0\ne f\in P^m\) is a relation, so \(\varphi(f)=0\). Since \(f\) has no constant term, write \(f=\sum_i f_i x_i\), with \(f_i\in P^{m-n}\), keeping the graded signs in this chosen order. There is an element \(z\) of bidegree \((m-n,n-1)\) with \(dz=f\): explicitly take
\[
z=\sum_i(-1)^{m-n}f_i y_i.
\]
Its image in \(R\otimes S\) is a \(d_n\)-cycle. It cannot be a boundary. A boundary primitive would have base degree \(m-2n\); all its coefficients, and all coefficients of \(z\), have degree less than \(m\). Lift that primitive to \(P\otimes S\) using the earlier isomorphisms. Equality with \(z\) lifts too, so differentiating would give \(f=0\), a contradiction.

This nonzero \(E_{n+1}^{m-n,n-1}\) class has no later outgoing differential, since \(r>n\) gives negative target fibre degree. A possible later incoming differential has source base degree \(m-n-r\), and that source satisfies \((m-n-r)+n=m-r<m\). Its \(E_{n+1}\) entry is already zero by the free-complex calculation; later pages remain zero there. Hence the class survives to \(E_\infty\) in positive total degree \(m-1\), a contradiction. There is therefore no relation in the first failure degree.

The remaining possibility is failure of surjectivity in degree \(m\). On the bottom row,
\[
E_{n+1}^{m,0}
=R^m/\sum_i x_iR^{m-n}.
\tag{H.6}
\]
The denominator is exactly the image of \(P^m\), because the lower-degree maps are isomorphisms and every positive monomial in \(P\) is divisible by one of its generators. The quotient is therefore nonzero. It has no outgoing differential. Every later incoming source has base degree \(m-r\), \(r>n\), again satisfying \((m-r)+n<m\); its entry is zero. This gives another nonzero positive-degree limiting class, a contradiction.

There is no first failure degree, so \(\varphi\) is an isomorphism. This proves (H.1), including more than one generator and possible simultaneous first relations and missing classes. The constant identification with \(H^n\) was the first Hurewicz identification, so the formulation independent of a basis also follows. Since integral homology is finitely generated by Theorem F.6, rational homology and its dual cohomology have finite dimension in each degree. Dualizing (H.1) gives (H.2). ∎

The first-failure argument matters: simply finding a transgressive generator would not exclude an extra later cohomology class or an extra relation among its products.

### H.2. Rationally acyclic spaces and Serre's sphere theorem

We will repeatedly use this consequence of Section F:

**Lemma H.2.** If \(X\) is a simply connected CW complex with finitely generated integral homology in every degree, and \(H_j(X;\mathbb Q)=0\) for every \(j>0\), then every \(\pi_j(X)\), \(j>0\), is finite.

**Proof.** The groups are finitely generated by Theorem F.8. The first Hurewicz theorem and (F.2) make \(\pi_2(X)\) finite. If its groups below \(j\) have already been shown finite, Theorem F.9 makes \(h:\pi_j(X)\to H_j(X;\mathbb Z)\) a rational isomorphism. Its target is rationally zero, so \(\pi_j(X)\) is a finitely generated group with zero rational tensor product. It is finite by Lemma F.1. Induction proves the result. ∎

**Theorem H.3 — Serre finiteness for spheres.** For \(n\geq2\) and \(i>n\), the group \(\pi_i(S^n)\) is finite, except when \(n\) is even and \(i=2n-1\). In that exception,
\[
\pi_{2n-1}(S^n)\cong\mathbb Z\oplus T,\qquad T\text{ finite}.
\tag{H.7}
\]

**Proof.**

**Proof: the first fibre.** The sphere's first Hurewicz group is \(\mathbb Z\), with its positive degree normalization proved in the frame-obstruction chapter. Lemma F.7 gives a map \(g:S^n\to K(\mathbb Z,n)\) inducing that identification. Its homotopy fibre \(Y\) is \(n\)-connected, and
\[
\pi_i(Y)=\pi_i(S^n)\quad(i>n),
\tag{H.8}
\]
by the homotopy sequence in Theorem C.2.

There is also a Hurewicz fibration
\[
\Omega K(\mathbb Z,n)\longrightarrow Y\longrightarrow S^n.
\tag{H.9}
\]
Indeed write points of \(Y\) as a sphere point together with a path from \(g(x)\) to the chosen basepoint, reverse that path, and identify (H.9) with the pullback of the based path fibration along \(g\). Its fibre has the homology of \(K(\mathbb Z,n-1)\), by Lemma F.5, hence finitely generated homology in each degree. Exercise E.6 gives the same property for \(Y\). We may take its CW model whenever applying Section F.

The rational cohomology second page of (H.9) has base generator \(a\) in degree \(n\), with \(a^2=0\). Its fibre generator \(y\) has degree \(n-1\); its algebra is polynomial if \(n\) is odd, exterior if \(n\) is even. Naturality with the based path fibration and \(g^*:H^n(K(\mathbb Z,n))\to H^n(S^n)\) gives
\[
d_n y=a
\tag{H.10}
\]
after fixing the sign of the generator. All earlier differentials vanish by generation and the two-column base.

If \(n\) is odd, the page is
\(\Lambda(a)\otimes\mathbb Q[y]\). Formula (G.3) gives
\[
d_n(y^j)=j a y^{j-1},\qquad d_n(a y^j)=0.
\]
Every positive-degree \(a y^j\) is a boundary and every positive power \(y^j\) has nonzero differential. The next page is only \(\mathbb Q\) at \((0,0)\). Thus \(Y\) is rationally acyclic. Its CW model satisfies Lemma H.2, which, with (H.8), proves finiteness for every \(i>n\).

If \(n\) is even, the page has just four entries \(1,a,y,ay\). The differential sends \(y\) to \(a\); the product \(ay\) is a cycle since \(a^2=0\). There is no other entry to hit it or receive a differential from it. It follows that
\[
H^*(Y;\mathbb Q)=\Lambda_{\mathbb Q}(b),\qquad |b|=m=2n-1.
\tag{H.11}
\]
There is a single associated graded summand in that degree, so no additive extension has been suppressed.

**Proof: the even-sphere exception and all later groups.** Take a CW model \(C\to Y\), preserving integral homology and homotopy. Its groups are finitely generated by Theorem F.8. Since \(H_i(C;\mathbb Q)=0\) for \(0<i<m\), induction using Theorem F.9 proves that \(\pi_i(C)\) is finite in those degrees: the first group is zero, and each next Hurewicz map is a rational isomorphism once the lower groups are finite. At degree \(m\), that theorem gives
\[
\pi_m(C)\otimes\mathbb Q=H_m(C;\mathbb Q)=\mathbb Q.
\]
Lemma F.1 makes \(\pi_m(C)\) a direct sum of \(\mathbb Z\) and a finite group. By (H.8), this is the group in (H.7).

Remove the finite groups below \(m\) by the connected-cover construction in Theorem F.9's proof. The result is an \((m-1)\)-connected CW complex \(Z\), with finitely generated integral homology, rational homology isomorphic to that of \(C\), and the same homotopy groups as \(C\) in dimensions at least \(m\). Set \(A=\pi_m(Z)\), a rank-one finitely generated abelian group. Lemma F.7 gives \(f:Z\to K(A,m)\) inducing the identity on \(\pi_m\). Both spaces have rational cohomology exterior on one degree-\(m\) generator, by (H.11) and Theorem H.1, and \(f^*\) is an isomorphism on that generator.

Its homotopy fibre \(W\) is \(m\)-connected and has finitely generated integral homology. The latter follows from Exercise E.6, using its path replacement with total space equivalent to \(Z\) and base \(K(A,m)\). Its other fibration
\[
\Omega K(A,m)\longrightarrow W\longrightarrow Z
\]
has the same rational calculation as the odd-\(n\) case of (H.9), with \(m\) in place of \(n\). The fibre has a polynomial generator of degree \(m-1\), the base has an exterior generator of degree \(m\), and naturality of the path transgression gives \(d_m y=a\). All positive-degree classes cancel by the displayed derivative formula. Thus \(W\) is rationally acyclic. Apply Lemma H.2 to its CW model.

The homotopy sequence gives \(\pi_i(W)=\pi_i(Z)\) for \(i>m\), and the connected-cover construction gives \(\pi_i(Z)=\pi_i(C)\) for \(i\geq m\). Equation (H.8) therefore makes all sphere groups above \(m\) finite. The groups between \(n\) and \(m\) were already proved finite by the earlier induction, completing the proof. ∎

This proof gives the group structure in the exception; it does not identify a specific integral generator with a Hopf-invariant normalization.

### H.3. The Hurewicz range required by the Thom theorem

**Theorem H.4 — Hurewicz modulo finite groups in the stable range.** Let \(X\) be a finite \((k-1)\)-connected CW complex, with \(k>2\). For
\[
k\leq r<2k-1
\tag{H.12}
\]
the ordinary Hurewicz map
\[
h:\pi_r(X)\longrightarrow H_r(X;\mathbb Z)
\tag{H.13}
\]
has finite kernel and cokernel. Thus it becomes an isomorphism after tensoring with \(\mathbb Q\). The same conclusion holds for a \((k-1)\)-connected CW complex whose integral homology is finitely generated in every degree.

**Proof.**

**Proof: one removal step.** Let \(C\) be \((s-1)\)-connected, \(s\geq3\), with finitely generated integral homology. Put \(A=\pi_s(C)=H_s(C)\); it is finitely generated. Choose \(g:C\to K(A,s)\) inducing the identity on \(\pi_s\), and let \(F\) be its homotopy fibre. It is \(s\)-connected. The path replacement has total space homotopy equivalent to \(C\), and Exercise E.6 gives finite generation of its fibre homology.

We claim that fibre inclusion followed by the total-space retraction gives
\[
H_j(F;\mathbb Q)\xrightarrow{\cong}H_j(C;\mathbb Q)
\quad\text{for }s<j\leq2s-2.
\tag{H.14}
\]
In its homology spectral sequence, (H.2) says that below base degree \(2s\) only degrees \(0\) and \(s\) can be nonzero. The fibre has \(H_q(F;\mathbb Q)=0\) for \(0<q\leq s\), by its connectivity and the first Hurewicz theorem. Thus on a total-degree-\(j\) diagonal in this range the only possible term is \(E_2^{0,j}=H_j(F;\mathbb Q)\): the potential term with base degree \(s\) has fibre degree \(j-s\leq s-2\) and is zero.

There are no outgoing differentials from column zero. An incoming source on page \(t\) is \(E_t^{t,j-t+1}\), with \(2\leq t\leq j+1\leq2s-1\). For \(t\ne s\) its base coefficient homology is zero by (H.2) and exact rational tensoring. For \(t=s\) its fibre degree is \(j-s+1\leq s-1\), again zero. Hence the column-zero term survives unchanged. The finite filtration has only that term, and its actual fibre edge is the map in (H.14), by Section D.3. This proves the claim as a statement about the induced map, rather than only a vector-space rank.

**Proof: iteration and the integral conclusion.** A finite CW complex has finite-rank cellular chain groups, hence finitely generated homology; Theorem F.8 gives finite generation of all its homotopy groups. The same applies to the more general hypothesis in the statement.

For \(r=k\), the first Hurewicz theorem already gives an integral isomorphism. For \(k<r\leq2k-2\), remove the successive first groups in dimensions \(s=k,k+1,\ldots,r-1\), each time taking a CW model of the fibre. Exercise E.6 and Theorems B.4–B.5 preserve finite generation of homology at every step. The homotopy sequence preserves \(\pi_r\) because \(r>s\).

At every step, \(r\leq2k-2\leq2s-2\), so (H.14) preserves \(H_r(-;\mathbb Q)\) as well. At the end the model is \((r-1)\)-connected; its first Hurewicz map is an integral isomorphism in dimension \(r\). The natural square for its composite map into \(X\), exactly as in (F.10), makes (H.13) a rational isomorphism.

Its source and target are finitely generated. Tensor exactness and Lemma F.1 therefore make its integral kernel and cokernel finite. This proves (H.12)–(H.13). ∎

**Rational connectivity and the endpoint.** Suppose that \(X\) is a simply connected CW complex with finitely generated integral homology in every degree, \(k\geq2\), and \(\pi_i(X)\otimes\mathbb Q=0\) for \(2\leq i<k\). Then the ordinary Hurewicz map has finite kernel and cokernel for \(1\leq r<2k-1\), and finite cokernel for \(r=2k-1\). Its rationalization is therefore an isomorphism below the endpoint and a surjection at the endpoint.

**Proof.** First consider an actually \((k-1)\)-connected complex. In the removal step of Theorem H.4, also take \(j=2s-1\). On that total-degree diagonal the second page still has only column zero: a term with base degree \(s\) would have fibre degree \(s-1\), and all other positive base degrees below \(2s\) vanish by (H.2). Thus the finite filtration has only its column-zero quotient. By the actual fibre-edge calculation, the map
\[
H_{2s-1}(F;\mathbb Q)\longrightarrow H_{2s-1}(C;\mathbb Q)
\]
is onto. Injectivity need not hold: an incoming differential from bidegree \((2s,0)\) is possible on page \(2s\). This is precisely why the earlier isomorphism estimate stops one degree sooner.

Fix \(r=2k-1\) and remove the first homotopy groups in dimensions \(s=k,\ldots,r-1\). The first removal gives the surjection just proved in degree \(r\); every later removal gives an isomorphism there, since \(r\leq2s-2\). All maps preserve \(\pi_r\), by their homotopy sequences. The final complex is \((r-1)\)-connected, so its first Hurewicz map is an integral isomorphism. The natural Hurewicz square then makes the original map onto after rationalization. Its integral cokernel is finitely generated and has zero rational tensor product, hence is finite by Lemma F.1.

These arguments also apply when \(k=2\): Lemma F.7 and the path-fibre construction require only \(s\geq2\); the vanishing and incoming-differential estimates in (H.14) have the same bounds for \(s=2\). The below-endpoint case is then just degree two, where the first Hurewicz theorem is integral. Degree one is zero on both sides because the space is simply connected.

For the stated rational-connectivity hypothesis, Theorem F.8 makes every homotopy group finitely generated. Lemma F.1 consequently makes the groups in dimensions \(2,\ldots,k-1\) finite. Remove them using the finite connected-cover steps in Theorem F.9's proof. Each removed one-group base is rationally acyclic, so the actual fibre edge makes the composite map \(u:C\to X\) an isomorphism on rational homology in every degree. Its homotopy sequence makes it an isomorphism on \(\pi_r\) for \(r\geq k\). The resulting CW complex \(C\) is \((k-1)\)-connected and still has finitely generated integral homology. Apply the preceding argument and the natural Hurewicz square to transfer both conclusions to \(X\) in those degrees.

Below degree \(k\), Theorem F.9, applied at degree \(k\), gives zero rational homology; the homotopy groups there are already finite. Integral homology is finitely generated and rationally zero, so is finite too. Every map between those finite groups has finite kernel and cokernel. At degree one both groups vanish. Finally, finite generation of the source and target and exactness of rational tensoring convert the rational isomorphisms and surjection into the asserted integral finiteness conclusions. For \(k=2\), no preliminary removal is needed. ∎

**Corollary H.5 — The finite Thom comparison (MS18.4).** If \(\xi\) is an oriented rank-\(k\) real bundle over a finite CW complex \(B\), \(k>2\), and \(0\leq n<k-1\), the composite
\[
\pi_{n+k}(T(\xi))
\xrightarrow{\,h\,}H_{n+k}(T(\xi);\mathbb Z)
\xrightarrow{\,\operatorname{Th}^{-1}\,}H_n(B;\mathbb Z)
\tag{H.15}
\]
has finite kernel and cokernel. Its rationalization is an isomorphism.

**Proof.** The geometric Thom chapter's Theorem C.1 gives a finite \((k-1)\)-connected CW complex \(T(\xi)\). The inequality \(n<k-1\) says \(n+k<2k-1\), so Theorem H.4 applies. Since \(n+k>0\), absolute homology agrees with homology relative to its basepoint. The full homological Thom isomorphism in that chapter, Theorem C.2, identifies it with \(H_n(B;\mathbb Z)\), using the stated orientation. Composing that integral isomorphism with the Hurewicz comparison preserves its finite kernel and cokernel. ∎

For the highly connected finite Thom complexes used in the next lesson continuation, (H.15) is the exact comparison required with \(k>n+1\). Both the finite-generation theorem and the sphere finiteness theorem have now been proved, including their prerequisites. The proof of Theorem H.4 uses the rational one-group calculation directly; it does not assume an unproved suspension theorem or a homology-theory uniqueness theorem.

**References.** Allen Hatcher's [*Spectral Sequences*](https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf) treats rational \(K(\mathbb Z,n)\) cohomology and Serre's sphere theorem. Its Proposition 5.23 shows that the stable Hurewicz map is a rational isomorphism; together with the Freudenthal suspension theorem, Corollary 4.24 of Hatcher's [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), this gives an alternative approach to the rational comparison for a \((k-1)\)-connected CW complex below degree \(2k-1\), including surjectivity at the endpoint. The one-group calculations here use finitely generated \(A\) and cohomology with \(\mathbb Q\) coefficients. The finite-generation hypotheses supply the additional integral finiteness conclusions.

## I. Exercises with complete solutions

**Exercise I.1 — Easy: a presentation and its rational models.** Let \(A\) be generated by \(e_1,e_2,e_3\), with relations \(2e_1=0\) and \(e_1+3e_2=0\). Determine \(A\), and compute the rational cohomology rings of \(K(A,2)\) and \(K(A,3)\).

**Solution.** The second relation gives \(e_1=-3e_2\), and the first then gives \(6e_2=0\). No relation involves \(e_3\). The map to \(\mathbb Z/6\oplus\mathbb Z\) taking \(e_2\) to \((1,0)\), \(e_1\) to \((-3,0)\) and \(e_3\) to \((0,1)\) respects both relations. In the other direction use the classes of \(e_2,e_3\); the preceding calculation respects the order-six relation and the composites are the identity on generators. Thus
\[
A=\mathbb Z/6\oplus\mathbb Z.
\]
Its rational rank is one. Theorem H.1 gives
\[
H^*(K(A,2);\mathbb Q)=\mathbb Q[t],\quad |t|=2,
\qquad
H^*(K(A,3);\mathbb Q)=\Lambda_{\mathbb Q}(u),\quad |u|=3.
\]
The finite direct summand has not been discarded integrally: its model is only rationally acyclic, and its positive integral homology is finite by Theorem F.6. These are rational rings, not an integral computation. ∎

**Exercise I.2 — Medium: the rational derivative and its signs.** Let \(x_1,x_2\) have degree three and \(y_1,y_2\) degree two. In
\(\Lambda(x_1,x_2)\otimes\mathbb Q[y_1,y_2]\), use the degree-one derivation \(d y_i=x_i\), \(d x_i=0\). Compute \(d(y_1y_2)\), \(d(x_1y_2)\), and \(d(x_2y_1)\). Prove that the entire complex has only constant cohomology. Explain why the proof requires rational coefficients.

**Solution.** The even degrees of the \(y_i\) and odd degrees of the \(x_i\) give
\[
d(y_1y_2)=x_1y_2+x_2y_1,\quad
d(x_1y_2)=-x_1x_2,\quad
d(x_2y_1)=x_1x_2.
\]
In particular \(x_1y_2+x_2y_1\) is a cycle, and the first formula exhibits its primitive.

For a single pair set
\[
h(xy^j)=\frac{y^{j+1}}{j+1},\qquad h(y^j)=0.
\]
Then \(dh+hd=1-\epsilon\), where \(\epsilon\) retains just the constant term. On \(y^j\), \(j>0\), this follows from \(d(y^j)=jxy^{j-1}\); on \(xy^j\), it follows by differentiating the displayed primitive. On constants both sides are zero. Tensor the two contractions, using
\[
h_{\mathrm{tot}}=h_1\otimes1+\epsilon_1\otimes h_2
\]
and the tensor homotopy sign \((-1)^{\deg c}\) in the second term on \(c\otimes c'\). Its boundary sum is \(1-\epsilon_1\otimes\epsilon_2\), by direct expansion. Thus all positive-degree cohomology vanishes.

The denominators \(j+1\) are invertible in \(\mathbb Q\). Over \(\mathbb F_2\), already \(d(y_i^2)=2x_i y_i=0\), and no derivative has a pure polynomial term, so \(y_i^2\) is not a boundary in this algebraic complex. The same rational cancellation argument therefore cannot be used in that characteristic. This last observation concerns the displayed algebraic complex, without asserting that it is the actual mod-two second page of the preceding fibrations. ∎

**Exercise I.3 — Hard: a locally finite inverse.** In the filtered contraction construction (G.11), prove that the series for \((1+N)^{-1}\) defines a linear map on the whole chain complex even if the filtration degrees of its generators are unbounded. Check both the contraction identity and the need to retain the inverse factor.

**Solution.** Each chain \(c\) lies in some \(F_p\) because the filtration is exhaustive. Since \(N\) lowers filtration, \(N^{p+1}c=0\); take \(F_{-1}=0\). Hence
\[
S(c)=\sum_{j=0}^{p}(-N)^j c
\]
is finite and independent of a larger choice of \(p\). For a sum of two chains take the larger of their two filtration bounds, so the same finite sum proves linearity. Multiplying the finite geometric series gives \((1+N)S(c)=c=S(1+N)c\).

The map \(A=dh_0+h_0d=1+N\) commutes with \(d\), since both \(dA\) and \(Ad\) are \(dh_0d\). Thus so does its inverse \(S\), and
\[
d(h_0S)+(h_0S)d=(dh_0+h_0d)S=1.
\]
This proves the contraction while preserving the filtration.

The inverse factor can be necessary. Use \(C_1=\mathbb Q e_1\oplus\mathbb Q e_2\), \(C_0=\mathbb Q f_1\oplus\mathbb Q f_2\), with \(e_i,f_i\) in filtration \(i-1\), and
\[
d e_1=f_1,\qquad d e_2=f_2+f_1.
\]
Its associated graded has the contraction \(h_0 f_i=e_i\). But \(dh_0 f_2=f_2+f_1\ne f_2\). Here \(Nf_2=f_1\), \(Nf_1=0\), and \(S=1-N\); consequently the corrected contraction has \(h f_2=e_2-e_1\), whose derivative is exactly \(f_2\). ∎

**Exercise I.4 — Medium: the strict endpoint.** For \(S^4\), determine which conclusions about \(\pi_4,\pi_5,\pi_6,\pi_7\) follow from the proved theorems, without calculating any finite group orders. Show why the upper endpoint of (H.12) is strict.

**Solution.** The sphere is three-connected and finite, so take \(k=4\). Its first Hurewicz map gives \(\pi_4(S^4)=\mathbb Z\). The range \(4\leq r<7\) and the zero homology in degrees five and six give finite \(\pi_5(S^4)\) and \(\pi_6(S^4)\). The even-sphere exception in Theorem H.3 gives
\[
\pi_7(S^4)=\mathbb Z\oplus T,\qquad T\text{ finite}.
\]
But \(H_7(S^4;\mathbb Z)=0\). Its degree-seven Hurewicz map has an infinite kernel, and its rationalization is not an isomorphism. It is onto the zero target, consistently with the separately proved endpoint surjectivity. Thus the bound cannot in general be extended from \(r<2k-1\) to \(r\leq2k-1\). No value of \(T\), or of the two earlier finite groups, is determined by this reasoning. ∎

**Exercise I.5 — Easy: finite generation is essential.** Explain why a rational isomorphism between abelian groups need not have finite kernel and cokernel. Contrast this with multiplication by a nonzero integer on \(\mathbb Z\).

**Solution.** Every element of \(\mathbb Q/\mathbb Z\) has finite order, so its tensor product with \(\mathbb Q\) is zero. The map
\[
0\longrightarrow\mathbb Q/\mathbb Z
\]
is therefore an isomorphism after rational tensoring, but its cokernel is infinite. This group is not finitely generated: finitely many rational classes have a common denominator, and the subgroup they generate is finite. Thus Lemma F.1 is inapplicable, exactly at the necessary hypothesis.

For multiplication by \(m\ne0\) on \(\mathbb Z\), the kernel is zero and the cokernel is \(\mathbb Z/|m|\), both finite. Its rationalization is invertible. For \(|m|>1\) it is not an integral isomorphism, so the conclusion of finite kernel and cokernel must also not be strengthened to an integral isomorphism. ∎

**Exercise I.6 — Hard: a mixed-dimensional finite complex.** Let \(X=S^4\vee S^6\). Determine \(\pi_4(X)\), whether \(\pi_5(X)\) is finite, and the rank and torsion form of \(\pi_6(X)\). Exhibit a rational kernel for its degree-seven Hurewicz map.

**Solution.** Its CW structure has one vertex and cells only in dimensions four and six. The proved cell-dimension connectivity makes it three-connected. Its reduced cellular homology is \(\mathbb Z\) in degrees four and six and zero otherwise. The first Hurewicz theorem gives \(\pi_4(X)=\mathbb Z\). Theorem H.4, with \(k=4\), makes \(\pi_5(X)\) finite and gives
\[
\pi_6(X)\otimes\mathbb Q=\mathbb Q.
\]
The group \(\pi_6(X)\) is finitely generated, by Theorem F.8, hence \(\mathbb Z\oplus T\) with finite \(T\).

In fact its degree-six Hurewicz map is onto: the inclusion of the \(S^6\) summand sends its positive degree-one homotopy class to the cellular generator of \(H_6(X)\). The collapse onto that summand splits the induced homotopy inclusion. It follows also that the finite subgroup \(T\) is the kernel of this Hurewicz map, with the positive sphere class providing a splitting.

Finally the inclusion \(S^4\hookrightarrow X\) has the collapse \(X\to S^4\) as a left inverse. Its map on \(\pi_7\) is consequently injective and remains injective after rationalization. By Theorem H.3 the source has rational rank one. Thus a nonzero rational homotopy class from \(\pi_7(S^4)\) survives in \(\pi_7(X)\), while \(H_7(X)=0\). It lies in the rational kernel. This argument makes no claim to compute all of \(\pi_7(X)\). ∎

The next chapter applies this rational-homotopy calculation. The [rational-bordism continuation](rational-oriented-bordism-and-projective-generators.md) applies these proofs to the finite oriented Thom complexes and proves the rank, rational polynomial ring and torsion criterion, completing the Thom-space lesson.
