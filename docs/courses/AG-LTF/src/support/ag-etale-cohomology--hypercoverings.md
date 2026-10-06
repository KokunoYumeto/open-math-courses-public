# Hypercoverings

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

A covering chooses local pieces. Its Čech nerve uses every intersection of those pieces. A hypercovering allows a further choice: cover the intersections, then cover the compatible boundaries made from those covers, and continue. These extra choices let us lift a cochain locally without changing all earlier choices by hand. They are the reason that a colimit over hypercoverings computes every cohomology group.

We assume Cohomology on sites, especially enough injectives, local vanishing of positive cohomology classes, and first quadrant double complexes. We prove the simplicial facts needed for the site constructions below. Background on simplicial objects is in the chapter on simplicial methods of the Stacks project ([Tag 0163](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-introduction)). The rest of this course mainly uses ordinary Čech methods, so this lesson can be read separately before returning to étale topology. Hypercoverings are also the starting point of cohomological descent, which this course does not treat.

Throughout, \(\mathcal C\) is a small site **with all fibre products**, and \(X\in\mathcal C\). The small étale site will satisfy this hypothesis: fibre products of étale schemes over the base are again étale. This holds because a morphism between schemes étale over the base is itself étale, and base changes and composites of étale morphisms are étale: [Stacks, Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence), [Tag 02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale) and [Tag 02GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-etale). We work with two universes \(\mathbb U\in\mathbb V\): the site, covers, coefficient values and indexing families are small in \(\mathbb U\); the collections indexing our colimits are sets in \(\mathbb V\). No colimit over a proper class is intended.

## 1. Families and finite limits

A **semi-representable object over \(X\)** is a formal family
\[
A=\{U_i\longrightarrow X\}_{i\in I}.
\]
A map \(A\to B=\{V_j\to X\}_{j\in J}\) consists of a function \(\alpha:I\to J\) and maps \(U_i\to V_{\alpha(i)}\) over \(X\). These objects form \(\mathrm{SR}(\mathcal C,X)\). Write \(1_X=\{X\xrightarrow{1}X\}\), and associate to a family the presheaf
\[
\Phi(A)=\coprod_{i\in I}h_{U_i}\longrightarrow h_X.
\tag{1.1}
\]
The coproduct here is in presheaves. It is not an assertion that the objects \(U_i\) have a coproduct in \(\mathcal C\).

The functor \(\Phi\) is fully faithful. Indeed, a map \(h_U\to\coprod_jh_{V_j}\) is an element of that coproduct evaluated at \(U\), hence a unique choice of \(j\) and a map \(U\to V_j\). Applying this separately to the summands proves the assertion, including the condition of being over \(h_X\).

The category \(\mathrm{SR}(\mathcal C,X)\) has coproducts and finite limits. Coproducts concatenate the families; \(1_X\) is final. If maps \(A\to B\) and \(D=\{W_k\}\to B\) use index functions \(\alpha,\beta\), their fibre product is
\[
\{U_i\times_{V_j}W_k\to X\}_{\alpha(i)=j=\beta(k)}.
\tag{1.2}
\]
Its universal property follows by choosing the common target index and the two compatible component maps. A final object and fibre products give all finite limits: products are fibre products over the final object, and an equalizer is the fibre product of a pair map with the diagonal. Evaluation of \(\Phi(A)\) at \(T\) is \(\operatorname{Hom}_{\mathrm{SR}}(\{T\},A)\), with the given map \(T\to X\) when working in the slice. Consequently \(\Phi\) preserves finite limits, since both representable Hom and presheaf evaluation do. It also preserves coproducts by (1.1).

A morphism \(A\to B\) is a **covering** if, for each \(j\), the maps \(U_i\to V_j\) with \(\alpha(i)=j\) form a covering family of the site. Composition and base change of such maps are coverings: on each target component these are exactly composition and base change of site covers. A finite product of coverings in \(\mathrm{SR}(\mathcal C,X)\) is a covering, by replacing its factors one at a time and using those two rules. Its associated presheaf map becomes an epimorphism after sheafification, by the local description of sheaf images.

## 2. Boundaries, truncation and coskeleton

Let \(\Delta\) have objects \([n]=\{0,\ldots,n\}\) and increasing maps, allowing equal values. A **simplicial object** \(K\) is a functor \(\Delta^{\mathrm{op}}\to\mathrm{SR}(\mathcal C,X)\). Its face maps \(d_i:K_n\to K_{n-1}\) omit vertex \(i\); its degeneracies \(s_i:K_n\to K_{n+1}\) repeat it. For example, \(d_i d_j=d_{j-1}d_i\) for \(i<j\). All identities follow from equality of the corresponding increasing maps. The augmentation \(K\to1_X\) is automatic in this slice.

Write \(\operatorname{sk}_n K\) for the restriction to degrees at most \(n\), as in the Stacks convention. This is an \(n\)-truncated object. For simplicial sets the actual simplicial subset generated by degrees at most \(n\) will be denoted \(\operatorname{Sk}_n K\). Distinguishing these two meanings avoids a common ambiguity about “skeleton.”

The right adjoint of truncation is **coskeleton**. If \(T\) is \(n\)-truncated, then
\[
(\operatorname{cosk}_nT)_m
=\lim_{\substack{[j]\to[m]\\0\le j\le n}}T_j.
\tag{2.1}
\]
The diagram includes restrictions along maps between the indicated simplices. It is finite in each degree, so the limit exists. To check the adjunction, a map \(K\to\operatorname{cosk}_nT\) is a compatible family of maps \(K_m\to T_j\) for all \([j]\to[m]\). Such a family is determined by its maps in degrees \(j\le n\), and these are exactly a map \(\operatorname{sk}_nK\to T\). Conversely, compose these maps with the simplicial restrictions of \(K\) to obtain the family. The two constructions are inverse. For \(m\le n\), the identity simplex gives \((\operatorname{cosk}_nT)_m=T_m\). Coskeleton preserves finite limits, either by (2.1), or by this right-adjoint property.

The **matching object** in degree \(m\) is
\[
M_0K=1_X,\qquad
M_mK=(\operatorname{cosk}_{m-1}\operatorname{sk}_{m-1}K)_m
\quad(m>0).
\tag{2.2}
\]
Thus \(M_1K=K_0\times K_0\). For \(m\ge2\), its generalized elements are tuples of faces \((x_0,\ldots,x_m)\) satisfying
\[
d_{j-1}x_i=d_ix_j\qquad(0\le i<j\le m).
\tag{2.3}
\]
Here \(x_i\) is the proposed face opposite vertex \(i\). Every proper simplex of \(\Delta[m]\) factors through an omitted vertex. If it factors through two, its image misses both vertices, so (2.3) identifies the two restrictions. This proves that the tuples give precisely the compatible families in (2.1); restricting such a family to its codimension-one faces is the inverse. Naturality follows by composing all component maps. The matching morphism \(K_m\to M_mK\) records the boundary of an \(m\)-simplex.

We will also use a finite simplicial set \(A\). “Finite” means that it has finitely many nondegenerate simplices, rather than finitely many simplices in all degrees. For such an \(A\), let \(\langle A,K\rangle\) be the object representing
\[
T\longmapsto
\operatorname{Hom}_{\mathrm{SimpSets}}
\bigl(A,\operatorname{Hom}_{\mathrm{SR}}(T,K_\bullet)\bigr).
\tag{2.4}
\]
It is a finite limit: choose the images of the finitely many nondegenerate simplices and impose their face relations. Degeneracies then determine the other images.

For completeness, every simplex has a unique expression as a degeneracy of a nondegenerate simplex. Existence follows by reducing dimension until no degeneracy remains. If \(x=\varphi^*y=\psi^*z\) for surjections \(\varphi:[n]\twoheadrightarrow[k]\), \(\psi:[n]\twoheadrightarrow[l]\) and nondegenerate \(y,z\), choose a right inverse \(\xi\) of \(\psi\). Nondegeneracy of \(z=(\varphi\xi)^*y\) forces \(\varphi\xi\) to be surjective, so \(l\ge k\). Interchanging the roles gives equality. Thus \(\varphi\xi\) is the identity for every right inverse \(\xi\). Any element of a fibre of \(\psi\) can be chosen as the value of such a right inverse, since its fibres are ordered consecutive blocks. It follows that \(\varphi=\psi\); applying a right inverse gives \(y=z\). This proves the claim and the finite-limit description in (2.4).

In particular
\[
\langle\Delta[m],K\rangle=K_m,
\qquad \langle\partial\Delta[m],K\rangle=M_mK.
\tag{2.5}
\]
For \(m=0\), the boundary is empty and its representing object is final. If finite simplicial subsets are glued along their intersection, their representing objects form a fibre product, because compatible maps on the two subsets are exactly a map on their union. A simplicial homotopy from \(a\) to \(b\) is a map \(\Delta[1]\times K\to L\) restricting to these maps at the two endpoints; the product means degreewise coproducts of \(K_m\), indexed by \(\Delta[1]_m\).

The augmentation has remained fixed in \(\mathrm{SR}(\mathcal C,X)\) throughout these limits. Forgetting it would change the matching objects. Compare [Conrad, Definition 4.1 and Examples 4.4–4.5], which give a complementary formulation in a category with a class of covering morphisms.

## 3. Hypercoverings fill locally

A **hypercovering of \(X\)** is a simplicial object \(K\) of \(\mathrm{SR}(\mathcal C,X)\) for which every matching morphism
\[
K_m\longrightarrow M_mK
\tag{3.1}
\]
is a covering, including \(K_0\to1_X\). In degree one it covers every ordered pair of local vertices. In degree two it covers every triple of edges with compatible vertices. The higher conditions cover every compatible boundary, not just horns.

**Example 3.1 (the ordinary nerve).** Let \(\mathcal U=\{U_i\to X\}\) be a cover and put \(K=\operatorname{cosk}_0\mathcal U\). Then
\[
K_m=\{U_{i_0}\times_X\cdots\times_XU_{i_m}\to X\}_{(i_0,\ldots,i_m)}.
\tag{3.2}
\]
Faces forget a factor and degeneracies repeat one by its diagonal. A boundary in positive degree is determined by its vertices, so its matching map is an isomorphism. Together with the covering in degree zero this proves that \(K\) is a hypercovering. Indices may repeat and need not be ordered. Formula (3.2) is the Čech hypercovering.

**Lemma 3.2 (finite filling).** If \(A\subset B\) are finite simplicial sets and \(K\) is a hypercovering, then
\[
\langle B,K\rangle\longrightarrow\langle A,K\rangle
\tag{3.3}
\]
is a covering in \(\mathrm{SR}(\mathcal C,X)\).

**Proof.** Adjoin the nondegenerate simplices of \(B\setminus A\) in increasing dimension. Before adjoining a simplex, all its proper faces have already been adjoined. The new simplicial subset is the pushout of \(\partial\Delta[m]\to\Delta[m]\) along the map describing those faces: its remaining simplices are the distinct degeneracies of this new nondegenerate simplex, by the uniqueness just proved. By (2.5), the resulting restriction map of representing objects is a base change of \(K_m\to M_mK\). It is a covering. There are only finitely many attachments, so their composite is a covering. This includes attaching a vertex to an empty subset, using \(K_0\to1_X\). ∎

Let \(P_\bullet=\Phi(K_\bullet)\), with its augmentation to \(h_X\). Write \(\mathbf Z[P_m]\) for the free abelian presheaf on \(P_m\), and a superscript \(\#\) for associated sheaf. With the alternating face differential \(\partial=\sum_i(-1)^id_i\), we obtain an augmented complex
\[
\cdots\longrightarrow\mathbf Z[P_2]^\#
\longrightarrow\mathbf Z[P_1]^\#
\longrightarrow\mathbf Z[P_0]^\#
\longrightarrow\mathbf Z[h_X]^\#\longrightarrow0.
\tag{3.4}
\]
The last sheaf is denoted \(\mathbf Z_X^\#\). It is the free abelian sheaf on \(h_X^\#\); on the slice site \(\mathcal C/X\), it becomes the associated constant sheaf \(\mathbf Z\).

**Theorem 3.3 (acyclicity).** Complex (3.4) is exact.

**Proof.** Associated sheaf is exact for abelian presheaves. A section of a free abelian sheaf can locally be represented by a finite sum of presheaf generators. If its differential is zero in the associated sheaf, restrict further so that this finite sum has zero differential in the presheaf. Thus it suffices to make every finite presheaf cycle a boundary locally.

Over an object \(T\), the augmented simplicial set \(P_\bullet(T)\to h_X(T)\) splits into fibres indexed by maps \(u:T\to X\). A finite chain uses only finitely many such maps; its differential preserves them. In degree zero, the augmentation-zero condition says that the coefficient sum in each fibre is zero. In higher degrees, the cycle condition holds separately in each fibre. We may treat these finitely many fibres in turn and take a common covering refinement at the end.

Fix one fibre and its finite cycle \(z\). Let \(A\) be the finite simplicial subset generated by its supporting simplices and their faces. Adjoin a cone vertex and its cone simplices, giving the finite simplicial set \(CA\). The given map \(A\to P_\bullet(T)\) is a \(T\)-valued point of \(\langle A,K\rangle\), over the chosen \(u\). Here (2.4) and \(\Phi\)'s preservation of finite limits identify that point with its actual family of presheaf simplices. Pulling back the covering (3.3) gives a cover of \(T\) on which it extends to \(CA\). If the support is empty there is no chain to fill; to obtain a vertex alone use the same assertion for \(\varnothing\subset\Delta[0]\).

On the augmented free chain complex of a cone, putting the cone vertex first defines an operator \(c\) of degree one. The faces of the cone on a simplex \(\sigma\) satisfy \(d_0(c\sigma)=\sigma\) and \(d_i(c\sigma)=c(d_{i-1}\sigma)\) for \(i>0\). Send the augmented generator to the cone vertex. Hence
\[
\partial c+c\partial=1
\tag{3.5}
\]
in all augmented degrees, including degree zero. Degenerate simplices satisfy the same identities, so this uses the full, unnormalized complex. The chosen extension sends (3.5) into \(P_\bullet\) and gives \(z=\partial(cz)\) locally. This proves exactness at each nonnegative degree. Finally, every generator \(u\in h_X(T)\) lifts locally to \(P_0\), by the degree-zero cover; its finite integer combinations lift after a common refinement. The augmentation is therefore an epimorphism of sheaves. ∎

This proof uses local boundary fillers and finite supports, and requires no points of the topos. Its conclusion concerns the associated sheaves: the presheaf complex need not already be exact on sections over a fixed object.

## 4. The cochain complex and its comparison

For an abelian presheaf \(F\), set
\[
C^p(K,F)=F(K_p)=\prod_{i\in I_p}F(U_{p,i}),\qquad
d=\sum_{j=0}^{p+1}(-1)^jd_j^*.
\tag{4.1}
\]
The simplicial identities cancel each pair of successive faces with opposite signs, so \(d^2=0\). Define \(\check H^p(K,F)=H^p(C^\bullet(K,F))\). For (3.2), this is exactly the full Čech complex of the cover from lesson 3.

For a sheaf \(F\),
\[
\check H^0(K,F)=F(X).
\tag{4.2}
\]
Indeed, a zero cocycle is a family of sections on \(K_0\) whose two restrictions agree on \(K_1\). Since \(K_1\) covers \(K_0\times K_0\), separatedness makes them agree on the actual pairwise intersections. They glue uniquely on the covering \(K_0\to X\). The converse follows by restriction, so this is an inverse bijection.

The free abelian adjunction and (1.1) identify the complex in (4.1) with
\[
C^\bullet(K,F)=
\operatorname{Hom}\bigl(\mathbf Z[P_\bullet]^\#,F\bigr).
\tag{4.3}
\]
If \(I\) is an injective abelian sheaf, applying \(\operatorname{Hom}(-,I)\) to the exact augmented complex (3.4) is exact. For example, a functional vanishing on the incoming boundary descends to its cokernel, identified with the next boundary subobject, and extends to the next chain term by injectivity. Thus
\[
\check H^p(K,I)=0\ (p>0),\qquad
\check H^0(K,I)=I(X).
\tag{4.4}
\]

**Theorem 4.1 (comparison spectral sequence).** For an abelian sheaf \(F\) and a hypercovering \(K\), there is a canonical map
\[
C^\bullet(K,F)\longrightarrow R\Gamma(X,F)
\quad\text{in }D^+(\mathrm{Ab}),
\tag{4.5}
\]
and a first quadrant spectral sequence
\[
E_2^{p,q}=\check H^p(K,\mathcal H^q(F))
\ \Longrightarrow\ H^{p+q}(X,F),
\qquad \mathcal H^q(F)(U)=H^q(U,F).
\tag{4.6}
\]
Both constructions are natural in the coefficient sheaf and in maps of hypercoverings. Coefficient cohomology in this formula is a presheaf; its positive-degree associated sheaf is zero, but its groups of sections need not be zero.

**Proof.** Choose an injective resolution \(F\to I^\bullet\) and form
\[
D^{p,q}=I^q(K_p),\qquad
d_{\mathrm{Tot}}=d_h+(-1)^p d_v.
\tag{4.7}
\]
The two differentials commute before this sign is inserted. In each total degree there are finitely many summands. Taking horizontal cohomology first, (4.4) leaves the single column \(I^\bullet(X)\). The augmentation gives a quasi-isomorphism
\[
I^\bullet(X)\longrightarrow\operatorname{Tot}D.
\tag{4.8}
\]
Compose \(C^\bullet(K,F)\to\operatorname{Tot}D\), induced by \(F\to I^0\), with the inverse of (4.8) in the derived category. This gives (4.5).

Taking vertical cohomology first gives \(E_1^{p,q}=\prod_iH^q(U_{p,i},F)\): products of abelian groups are exact, and evaluation of the resolution computes each indicated group. Its first horizontal differential is (4.1) for the presheaf \(\mathcal H^q(F)\). This proves the page formula (4.6). The first quadrant bounds give convergence with a finite filtration in each total degree, by the double-complex theorem used in lesson 3.

A coefficient map extends to a comparison map of injective resolutions. Two such extensions are homotopic; applying the section functors gives the corresponding total homotopy, so (4.5) is independent of the extension and resolution. A hypercovering map acts by restriction on every \(D^{p,q}\), commutes with its differentials and augmentations, and preserves the filtration. This proves naturality of the comparison and spectral sequence. Resolution comparison gives the same identification for its pages from the cohomology pages onward. ∎

## 5. Changing a chosen degree

We next prove that a local choice in any one degree can be incorporated in a new hypercovering.

Call a simplicial morphism \(B\to A\) a **relative covering** if
\[
B_m\longrightarrow A_m\times_{M_mA}M_mB
\tag{5.1}
\]
is a covering for every \(m\), with \(M_0A=M_0B=1_X\). If \(K\) is a hypercovering and \(K\to A\) is any map, then \(K\times_A B\) is a hypercovering whenever (5.1) holds. To prove this, matching preserves fibre products, so its degree-\(m\) matching target is \(M_mK\times_{M_mA}M_mB\). The matching map factors as two coverings:
\[
K_m\times_{A_m}B_m
\longrightarrow K_m\times_{M_mA}M_mB
\longrightarrow M_mK\times_{M_mA}M_mB.
\tag{5.2}
\]
The first is a base change of (5.1), the second of the matching cover of \(K\). This also proves the assertion in degree zero.

**Lemma 5.1 (degree refinement).** Let \(r\ge0\) and let \(Z\to K_r\) be a covering in \(\mathrm{SR}(\mathcal C,X)\), with \(K\) a hypercovering. There is a hypercovering map \(L\to K\) whose degree-\(r\) map factors through \(Z\).

**Proof.** For an object \(W\) define the simplicial object
\[
(Q_rW)_m=\prod_{\alpha:[r]\to[m]}W.
\tag{5.3}
\]
For \(\beta:[l]\to[m]\), restriction sends the coordinate indexed by \(\gamma:[r]\to[l]\) to the coordinate indexed by \(\beta\gamma\). These rules compose, so define a simplicial object. A map \(K\to Q_rW\) is equivalent to a map \(K_r\to W\): its coordinate \(\alpha\) must be the latter map composed with \(\alpha^*:K_m\to K_r\). Projection to the identity coordinate recovers the original map, verifying both inverses.

The matching object of \(Q_rW\) in degree \(m\) is
\[
M_m(Q_rW)=\prod_{\substack{\alpha:[r]\to[m]\\\alpha\text{ not onto}}}W.
\tag{5.4}
\]
To check this for \(m>0\), a coordinate in a boundary face is an increasing map whose image misses that face's omitted vertex. If it occurs in two faces, its image misses both, and the common-face relation identifies the two copies. Conversely, every map missing a vertex occurs in that face; two presentations meet in the face missing both vertices, which proves there are no other coordinates or relations. For \(m=0\) the indexing set in (5.4) is empty, giving the final object, as required.

Put \(Y=K_r\) and use the map \(K\to Q_rY\) corresponding to the identity. The map \(Q_rZ\to Q_rY\) is a relative covering: its degree-\(m\) relative matching morphism is the identity on the factors with non-surjective \(\alpha\), and \(Z\to Y\) on the factors with surjective \(\alpha\). There are finitely many factors, so it is a covering. Define
\[
L=K\times_{Q_rY}Q_rZ.
\tag{5.5}
\]
It is a hypercovering by (5.2). Projection from \(L_r\) to the coordinate of \(Q_rZ\) indexed by \(\operatorname{id}_{[r]}\) factors its map to \(K_r=Y\) through \(Z\), by the defining fibre product square. ∎

Consequently a cochain \(\sigma\in H(K_r)\), for an epimorphism of sheaves \(G\to H\), lifts to \(G(L_r)\) after a refinement. On each component \(U_{r,i}\), choose a cover on which \(\sigma_i\) lifts. Concatenate these covers to a covering \(Z\to K_r\), with its chosen lifting cochain. Lemma 5.1 pulls it back to the required lift on \(L_r\). The same argument kills a specified cochain in \(\mathcal H^q(F)(K_r)\) when \(q>0\), using local vanishing from lesson 3. Finite sequences of such choices can be made by repeated refinement.

Every map between hypercoverings will be called a **refinement map** here. It need not be a covering in every degree, nor a relative covering as in (5.1). The latter are special maps used to build convenient refinements.

## 6. Maps become homotopic after refinement

Homotopic simplicial maps induce equal maps on cohomology. An explicit chain homotopy makes this statement useful. Suppose \(h:\Delta[1]\times K\to L\) has endpoints \(a,b\). For an \(n\)-simplex, triangulate its product with the interval into the \(n+1\) simplices whose vertex lists switch once from endpoint zero to endpoint one. Algebraically their maps are
\[
h_j=h\bigl(s_j(-),t_j\bigr):K_n\longrightarrow L_{n+1},
\quad 0\le j\le n,
\]
where \(t_j:[n+1]\to[1]\) has values zero through position \(j\) and one thereafter. Set \(P_n=\sum_{j=0}^n(-1)^j\mathbf Z[h_j]\). In the boundary of this sum, faces before or after the switching position cancel with the corresponding terms of \(P_{n-1}\partial\). The two faces on either side of each interior switch cancel with the adjacent prism simplex; the remaining endpoints are the top simplex \(b\) and the bottom simplex \(-a\). Thus
\[
\partial P+P\partial=b_*-a_*.
\tag{6.1}
\]
This is also true in degree zero, where it is the boundary of the single path. Applying Hom into \(F\) gives \(dS+Sd=b^*-a^*\) on (4.1). Hence the maps \(\check H^i(L,F)\to\check H^i(K,F)\) are equal. On (4.7), the same operator lowers the horizontal degree; its two vertical contributions have opposite signs, so the total homotopy also proves compatibility with (4.5).

**Theorem 6.1.** If \(a,b:K\to L\) are any two maps of hypercoverings, there exists a refinement \(c:K'\to K\) such that \(ac\) and \(bc\) are simplicially homotopic. In particular they induce equal maps after that refinement, and in the colimit of Čech cohomology.

**Proof.** Define the simplicial path object by
\[
(L^{\Delta[1]})_m=\langle\Delta[m]\times\Delta[1],L\rangle.
\]
Restrictions come from the first factor. The products of simplices here are finite: in a nondegenerate simplex of \(\Delta[m]\times\Delta[1]\), some coordinate strictly increases at each step, so its dimension is at most \(m+1\). Evaluation at the two endpoints gives \(L^{\Delta[1]}\to L\times L\). Its degree-\(m\) relative matching target represents maps on
\[
A_m=(\partial\Delta[m]\times\Delta[1])
\cup(\Delta[m]\times\partial\Delta[1]).
\tag{6.2}
\]
Indeed, the first part prescribes the boundary paths and the second their endpoints. Their intersection is exactly \(\partial\Delta[m]\times\partial\Delta[1]\), so agreeing on it is precisely the relative matching fibre product. Restricting from the full prism to (6.2) is a covering by Lemma 3.2. This proves that the endpoint map is a relative covering, including \(m=0\), when it is \(L_1\to L_0\times L_0\).

Set \(K'=K\times_{L\times L}L^{\Delta[1]}\), using \((a,b)\). Formula (5.2) makes it a hypercovering. Its projection to the path object supplies a homotopy with endpoints \(ac,bc\). To see this directly, evaluate a map on \(\Delta[m]\times\Delta[1]\) at each \(m\)-simplex \(t\) of the interval along \((\operatorname{id},t)\). These evaluations give the degree-\(m\) components of \(K'\times\Delta[1]\to L\), and commute with restrictions. They give the specified endpoint maps. ∎

Let \(\mathrm{HC}(\mathcal C,X)\) have hypercoverings as objects and maps modulo the equivalence relation **generated** by simplicial homotopies. Taking the generated relation avoids assuming that one-step simplicial homotopy is transitive. Composing a homotopy on either side gives another homotopy, so this quotient is a category. The cohomology functors factor through it by (6.1).

This category is cofiltered. It is nonempty, since the constant simplicial object \(1_X\) is a hypercovering. Two hypercoverings have the levelwise product over \(X\): its matching map is the product of the two matching covers, so it is a hypercovering with projections to both. Finally Theorem 6.1 equalizes any pair of parallel maps in the homotopy category after precomposition. These are exactly the cofiltered conditions. All objects, arrows and countable simplicial diagrams built from \(\mathbb U\)-small families form sets in \(\mathbb V\); taking a quotient still gives a \(\mathbb V\)-small category. We can therefore take an ordinary filtered colimit over its opposite.

The conclusion of Theorem 6.1 includes an essential refinement. Arbitrary maps of a fixed hypercovering need not act equally on its Čech cohomology. Section 8 gives an explicit example. Homotopic maps already act equally on the fixed complex's cohomology; arbitrary maps act equally after passing to a suitable refinement.

## 7. Cohomology is the colimit

Set
\[
T^i(F)=\underset{K\in\mathrm{HC}(\mathcal C,X)^{\mathrm{op}}}
{\operatorname{colim}}\check H^i(K,F).
\tag{7.1}
\]
A class is represented on a hypercovering, and two representatives agree if they agree after a common refinement. A class is zero if it becomes a boundary after a refinement. These assertions follow from filteredness: for any finite list of objects and arrows, the filtered conditions place them in a common target with the required equalities. Thus the usual quotient description of a colimit identifies exactly these representatives. By (4.2), \(T^0(F)=F(X)\), with all transition maps identified with the identity.

**Theorem 7.1 (hypercovering comparison).** The maps (4.5) induce natural isomorphisms
\[
T^i(F)\xrightarrow{\ \sim\ }H^i(X,F)
\qquad(i\ge0).
\tag{7.2}
\]

**Proof.** We construct the connecting maps and prove every part of their exactness. Given
\[
0\longrightarrow F\xrightarrow{u}G\xrightarrow{v}H\longrightarrow0,
\tag{7.3}
\]
represent \(\xi\in T^p(H)\) by a cocycle \(\sigma\in H(K_p)\). Lemma 5.1 permits a refinement on which it lifts to \(\tau\in G(K_p)\). Since \(v(d\tau)=d\sigma=0\), left exactness of sections identifies \(d\tau\) with a unique cochain \(z\in F(K_{p+1})\). It is a cocycle, because \(u(dz)=d^2\tau=0\) and \(u\) is injective on sections. Define
\[
\delta\xi=[z]\in T^{p+1}(F).
\tag{7.4}
\]

If the lift changes, the two lifts differ by a cochain in \(F\), so their differentials differ by a coboundary. If the representing cocycle changes by \(d\lambda\), first refine to lift \(\lambda\) to a cochain \(\mu\) of \(G\); changing the lift by \(d\mu\) leaves its differential unchanged. Two choices of refinement can be placed over a common hypercovering; their composites to the original one become homotopic after a further refinement by Theorem 6.1. Equation (6.1) changes the pulled back cocycles only by a coboundary, already covered by the previous argument. Finally equality of representatives in (7.1) means equality up to a coboundary after refinement, so the same reasoning establishes independence of the original representative. In degree zero there is no degree-minus-one cochain: the two zero-cocycle representatives simply agree after refinement.

For additivity, place two cocycles and chosen lifts on a common refinement and add them; the lift of their sum has differential the sum of the two differentials. Independence makes this the asserted addition law. A morphism of short exact sequences sends a chosen lift to a chosen lift of the image, so the maps \(\delta\) are natural.

The three exactness checks are as follows. First, if a \(G\)-cocycle maps to a boundary in \(H\), refine until that boundary has the form \(d\lambda\), and refine again to lift \(\lambda\) to \(\mu\) in \(G\). Subtracting \(d\mu\) leaves a \(G\)-cocycle whose image is zero, hence a cocycle in \(F\). This proves \(\ker(T^p(G)\to T^p(H))=\operatorname{im}T^p(F)\); in degree zero use zero image directly. Second, if (7.4) is zero, refine until \(z=da\) for a cochain \(a\) in \(F\). Then \(\tau-u(a)\) is a \(G\)-cocycle lifting \(\sigma\). Conversely a cocycle lift has zero connecting class. Third, if an \(F\)-cocycle \(z\) becomes a boundary in \(G\), refine until \(u(z)=d\tau\). Then \(v(\tau)\) is an \(H\)-cocycle and its connecting class is \([z]\). Conversely a connecting cocycle is the boundary of its lift in \(G\). In degree zero, injectivity of \(F(X)\to G(X)\) supplies the initial zero. These checks prove the full long exact sequence for \(T^\bullet\).

For every \(F\), embed it into an injective sheaf \(I\). By (4.4), \(T^i(I)=0\) for \(i>0\). Thus this delta-functor is effaceable, hence universal, by the ordinary homological algebra theorem used in lesson 3. The derived functors \(H^i(X,-)\) are also universal, and have the same degree-zero functor. The unique morphisms of delta-functors extending that identity in both directions have composites equal to the identity, by uniqueness. This gives (7.2).

It remains to check that this isomorphism is the comparison already constructed in (4.5), rather than an unrelated one. Choose compatible injective resolutions for (7.3) by the injective horseshoe lemma, with their sequence split in each resolution degree. Applying sections on each \(K_p\), or on \(X\), preserves this splitting. The resulting short exact sequences of total complexes and augmentation quasi-isomorphisms therefore commute with connecting maps. A chosen lift \(\tau\) in (7.4) maps into bidegree \((p,0)\) of the middle resolution double complex. Its vertical differential is zero, since it comes from \(G\); its total differential is exactly \(d_h\tau=u(z)\). Its connecting class in the first total complex is therefore the image of \(z\), with the same sign as (7.4). This proves compatibility with \(\delta\). The comparison is the identity in degree zero, so universality identifies it with the isomorphism above. ∎

The theorem does not say that a fixed hypercovering computes all cohomology by its zero-row Čech complex. It says that refinements eventually supply all classes and all relations. An acyclic hypercovering, whose every component is \(F\)-acyclic, is a useful special case: (4.6) then has only the zero row, so that fixed hypercovering already computes \(H^*(X,F)\).

## 8. Two explicit calculations

**An ordinary cover of the circle.** Take the two arcs \(U,V\) from lesson 3, whose intersection has two interval components. Its Čech hypercovering is (3.2). All its components are intervals or finite disjoint unions of intervals, so they are acyclic for \(F=\underline{\mathbf Z}\). Its full cochain complex has the same cohomology as the reduced two-open complex, by the repeated-index contraction proved there:
\[
\mathbf Z^2\longrightarrow\mathbf Z^2,
\qquad(a,b)\longmapsto(b-a,b-a).
\tag{8.1}
\]
It gives \(\mathbf Z\) in degrees zero and one, and zero in higher degrees. The fixed hypercovering computes the circle's sheaf cohomology because its components are acyclic, as verified in lesson 3.

**A hypercovering with an extra class.** On the same open-set site of \(X=S^1\), keep \(F=\underline{\mathbf Z}\). We construct a hypercovering \(K\) for which
\[
\check H^3(K,F)=\mathbf Z,
\qquad H^3(X,F)=0.
\tag{8.2}
\]
This will also exhibit two maps that act differently before refinement.

Set \(K_0=\{X\}\) and \(K_1=\{X_0,X_e\}\), two formal copies of \(X\). Both faces are the identity on the underlying open set, and \(s_0\) selects \(X_0\). Think of \(0\) as the degenerate edge and \(e\) as an extra loop. Since all vertices coincide, the degree-two matching object has eight components \(X\), indexed by triples \((a_0,a_1,a_2)\in\{0,e\}^3\).

The degenerate two-simplices supply copies of \(X\) over the three triples
\[
(0,0,0),\quad(e,e,0),\quad(0,e,e).
\tag{8.3}
\]
These are, respectively, the twice-degenerate vertex, \(s_0e\), and \(s_1e\), as the face-degeneracy identities verify. Over **each** of the other five matching components, take the two component opens \(U,V\) and their inclusions into that copy of \(X\). Let \(K_2\) be the resulting thirteen-member family: three copies of \(X\) and ten arc components. Its face maps are the inclusions into the components labelled by \(a_i\). The degeneracies are exactly the three copies specified in (8.3). Their faces satisfy all face-degeneracy identities; the two degeneracies of the zero edge both give the first copy. Thus we have a 2-truncated simplicial object. Put
\[
K=\operatorname{cosk}_2(K_{\le2}).
\tag{8.4}
\]
The covers in degrees zero and one contain identity components; in degree two, (8.3) gives identity covers on three matching components and the arc cover on each remaining one. In degrees at least three, the matching map is an isomorphism. To verify the last statement, compatible proper faces prescribe exactly the simplices of dimensions at most two in the full simplex. These already determine its unique simplex by (2.1), and agree on their intersections. Hence \(K\) is a hypercovering.

Each component in every degree of (8.4) is a finite intersection of \(X,U,V\), because coskeleton is formed by finite limits and maps of opens are inclusions. Such an intersection is \(X\), an arc, their two-component intersection, or the empty open. Lesson 3 proves
\[
H^q(W,F)=0\quad(q\ge2)
\]
for all these opens \(W\), and \(H^1(X,F)=\mathbf Z\), while the proper opens on this list have zero \(H^1\). Thus (4.6) has only its rows \(q=0,1\).

We can compute its \((1,1)\) entry without examining higher matching objects. In the row \(q=1\), the first two terms are \(\mathbf Z\) and \(\mathbf Z^2\), and their differential is zero since the two faces of each edge agree. Write an element of \(\mathbf Z^2\) as \((a_0,a_e)\). Its next differential has value \(a_0\) on each of the three \(X\)-components in (8.3): the three alternating sums are \(a_0\), \(a_e-a_e+a_0\), and \(a_0-a_e+a_e\). All its arc-component values lie in zero groups. Its kernel is therefore \(\{(0,a_e)\}\), and
\[
E_2^{1,1}=\mathbf Z.
\tag{8.5}
\]
No differential can enter this entry from page two onward. Its only possible outgoing differential is \(d_2:E_2^{1,1}\to E_2^{3,0}\). Since \(H^2(X,F)=0\), its kernel is zero. At \((3,0)\), there is no outgoing differential, the possible \(d_3\) source \((0,2)\) is zero, and the only incoming differential is that same \(d_2\). Since \(H^3(X,F)=0\), its cokernel is zero. It follows that
\[
d_2:\mathbf Z\xrightarrow{\sim}\check H^3(K,F),
\]
which proves (8.2). This is a calculation of the unnormalized cochain complex's cohomology, through its explicitly constructed spectral sequence; it makes no appeal to singular cohomology.

The vertex \(X=K_0\) gives a simplicial section \(s:1_X\to K\) by its degeneracies. Let \(\epsilon:K\to1_X\) be the augmentation. The maps \(a=1_K\) and \(b=s\epsilon\) are two maps of hypercoverings over \(X\). The first acts as the identity on the nonzero group (8.2). The second acts as zero, since its pullback factors through \(\check H^3(1_X,F)=0\). Indeed the constant hypercovering's complex has terms \(F(X)\) and differentials alternating between zero and the identity, and has no positive cohomology. These two maps do not act equally on the fixed group. After refining by \(s:1_X\to K\), the class vanishes and the maps coincide. This confirms the refinement in Theorem 6.1 and gives a concrete reason for the colimit in (7.2).

## 9. Hypercoverings from a basis of opens

Let \(\mathcal B\) be a basis of a space \(X\), and use its full open-set site. The basis need not be closed under intersection. Matching objects are formed in the full site, and we cover their component opens by basis opens. We prove that hypercoverings whose components are all in \(\mathcal B\) suffice in (7.2).

We first construct such a refinement of any given hypercovering \(K\). Use **split** simplicial objects: choose families \(N_r\) of new simplices, so that
\[
L_n=\coprod_{\substack{[n]\twoheadrightarrow[r]\\r\le n}}N_r.
\tag{9.1}
\]
Degenerate simplices are formal copies of earlier \(N_r\). Suppose a split truncation of \(L\to K\) has been constructed in degrees less than \(n\). Its forced degenerate part in degree \(n\) is the sum in (9.1) with \(r<n\); all its maps into \(K_n\) and \(M_nL\) are determined by the lower simplicial maps. Set
\[
T_n=K_n\times_{M_nK}M_nL.
\tag{9.2}
\]
Every component of this object is an open set, being a finite limit of families of opens. Choose a family \(N_n\) of basis opens covering every component of \(T_n\), and map them into (9.2). In degree zero this just chooses a basis refinement of \(K_0\).

Define \(L_n\) to be its forced degenerate part together with \(N_n\). The faces of a new simplex are supplied by its matching-boundary map in (9.2), hence satisfy (2.3). On the degenerate copies, use the face-degeneracy rules of the earlier degrees. These definitions obey all identities: an increasing map factors uniquely as a surjection followed by an injection; the surjection chooses the formal degeneracy copy, and the injection takes its specified face. Two ways of taking successive proper faces agree by the matching relations, while the earlier degrees already satisfy the relations involving those faces. For a new simplex, these are all possible relations except its identity map. The maps to \(K\) respect them because (9.2) requires the same boundary there. This completes the split truncation by one degree.

The map \(N_n\to T_n\) is a cover, and \(T_n\to M_nL\) is a base change of the matching cover of \(K\). Adding the degenerate components preserves an open covering. Consequently \(L_n\to M_nL\) is a covering. Continuing for all \(n\) gives a hypercovering \(L\to K\), with every component of every \(L_n\) a copy of a basis open. This construction proves the claimed existence, including the degeneracy compatibility that a mere degreewise replacement would miss.

These refinements suffice for classes and relations. A class represented on any \(K\) pulls back to a basis hypercovering. If two such representatives agree after a general refinement, apply the same construction to that refinement and they agree on a basis refinement. To justify common refinements within this restricted collection, first form the general product of two basis hypercoverings and then choose its basis refinement. To equalize parallel maps, first use the path refinement of Theorem 6.1 and then its basis refinement. For two maps into a common general \(K\), their composites from that product are parallel; the same path refinement makes them equal in the homotopy category. Thus the restricted diagram is filtered in the same sense and its colimit has exactly the same representatives and relations as (7.1). We have proved
\[
H^i(X,F)=\operatorname{colim}_{K\text{ with basis components}}\check H^i(K,F).
\tag{9.3}
\]

Verdier's variant permits an augmentation of a semi-representable simplicial presheaf to an arbitrary presheaf of sets \(G\), and requires its matching maps only to become epimorphisms after sheafification. The degree-zero and degree-one conditions are, respectively, local surjectivity onto \(G\) and onto the fibre product over \(G\). This is more flexible than specifying covers in \(\mathrm{SR}(\mathcal C,X)\). Our finite-cycle proof uses exactly those local surjections, so it also proves the associated free abelian complex resolves \(\mathbf Z[G]^\#\). The corresponding coefficient group is \(\operatorname{Ext}^i(\mathbf Z[G]^\#,F)\). We do not need a colimit theorem for this wider variant here; the object-based form (7.2) suffices for the course. See [Stacks, Tags 09VT–09VY].

## 10. Exercises

1. **A coskeleton — easy.** Show that \(\operatorname{cosk}_0\{U_i\to X\}\) has the terms (3.2), and identify every face, degeneracy and matching map. Check that its cochain complex is the ordinary full Čech complex.

2. **A common refinement — medium.** Show that the levelwise product over \(X\) of two hypercoverings is a hypercovering. Explain why an arbitrary levelwise fibre product over a third hypercovering needs an extra hypothesis such as (5.1).

3. **Split covers — medium.** Suppose every covering family of every object admits a section, meaning a section of its semi-representable covering map. Use the main theorem to prove \(H^i(X,F)=0\) for \(i>0\). Is it enough to assume this only for covers of \(X\)?

4. **Ordinary covers in degree two — hard.** Let \(\mathrm{Cov}(X)\) be a cofinal family of covers of \(X\). Suppose that, for every finite nonempty intersection \(W\) of members of every cover in this family, \(\check H^1(\mathcal V,F)=0\) for all covers \(\mathcal V\) in a cofinal family of covers of \(W\). Prove
\[
\operatorname{colim}_{\mathcal U\in\mathrm{Cov}(X)}
\check H^2(\mathcal U,F)\xrightarrow{\sim}H^2(X,F).
\tag{10.1}
\]
Use the ordinary Čech spectral sequence from lesson 3, and explain the two cofinality quantifiers. This gives the precise meaning of “Čech degree one vanishes on the finite intersections”; vanishing for one chosen cover of each intersection would be insufficient.

## 11. Solutions

**1.** For a zero-truncated family \(A\), a map from \(\operatorname{sk}_0\Delta[m]\) specifies a vertex in \(A\) for each of its \(m+1\) vertices, all over \(X\). Thus (2.1) is the product \(A^{m+1}\) in \(\mathrm{SR}(\mathcal C,X)\). Formula (1.2) identifies it with (3.2). Omitting a vertex gives the appropriate projection; repeating it gives the diagonal on that factor. For \(m=1\), the matching object is already the same pair product. For \(m\ge2\), every matching collection determines a consistent list of vertices; conversely that list gives all its faces. These inverse operations identify the matching map with an isomorphism. The only remaining matching condition is the original degree-zero cover. Evaluating \(F\) on this family gives the product over all tuples \((i_0,\ldots,i_m)\), and the alternating projection restrictions in (4.1) are exactly the ordinary Čech differential. This includes repeated indices and checks the claimed complex, not only its cohomology.

**2.** Write \(N=K\times L\) in the category over \(X\), so \(N_m=K_m\times L_m\). Formula (2.1) gives \(M_mN=M_mK\times M_mL\). The matching map is the product of the two covering maps; it is a cover because it factors into their two base changes. The degree-zero case is the same assertion over \(1_X\). Thus \(N\) is a hypercovering. For a fibre product \(K\times_A B\), matching still commutes with the product, but the source uses the actual \(A_m\) and the matching target uses \(M_mA\). The two absolute covering hypotheses alone do not identify those requirements. A relative covering \(B\to A\) supplies exactly the first arrow in (5.2); then its second arrow comes from \(K\). This proves the valid sufficient hypothesis without assuming every map of hypercoverings has it.

**3.** For a hypercovering \(K\), split its degree-zero cover by a map \(s_0:1_X\to K_0\). The unique map \([n]\to[0]\) defines, by degeneracies, maps \(s_n:1_X\to K_n\). They commute with every simplicial restriction, since all composites to \([0]\) are the same map. Thus they form a refinement \(s:1_X\to K\). The constant hypercovering's cochain differential in degree \(p\) is multiplication by \(\sum_{j=0}^{p+1}(-1)^j\): it is zero for even \(p\) and the identity for odd \(p\). Its positive cohomology is zero. Every positive-degree class represented on \(K\) therefore vanishes after the refinement \(s\). Formula (7.2) makes \(H^i(X,F)\) zero. Only the splitting of covering families of \(X\) was used, so that weaker assumption suffices. A section of a formal family is indeed a choice of one component with a retraction: apply Yoneda to \(h_X\to\coprod_i h_{U_i}\).

**4.** The degree-one comparison proved by torsors in lesson 3 identifies \(H^1(W,F)\) with the colimit of ordinary \(\check H^1\) over covers of \(W\). Cofinality at \(W\) and the stated vanishing therefore give \(H^1(W,F)=0\) for every indicated finite intersection. For any \(\mathcal U\in\mathrm{Cov}(X)\), row \(q=1\) of its \(E_1\)-page is consequently zero. In particular \(E_2^{0,1}=E_2^{1,1}=0\). The only possible incoming differential to \(E_2^{2,0}=\check H^2(\mathcal U,F)\) is \(d_2^{0,1}\), and it is zero; no differential leaves that entry. Thus the edge map to \(H^2(X,F)\) is injective, with image the filtration step \(F^2H^2\). The other positive-horizontal step has graded piece \(E_\infty^{1,1}=0\), so \(F^1H^2=F^2H^2\).

For surjectivity of (10.1), take \(\xi\in H^2(X,F)\). Local vanishing supplies a cover on which all its restrictions are zero. Cofinality at \(X\) supplies a cover \(\mathcal U\) in the specified family refining it. The edge of \(\xi\) in \(E_2^{0,2}=\check H^0(\mathcal U,\mathcal H^2(F))\) is zero, since it is the family of its local restrictions. This edge has kernel \(F^1H^2\): in a first quadrant sequence there are no incoming differentials at \((0,2)\), so \(E_\infty^{0,2}\) is a subgroup of \(E_2^{0,2}\), and it is the quotient \(H^2/F^1H^2\). Thus \(\xi\in F^1H^2=F^2H^2\), and comes from \(\check H^2(\mathcal U,F)\). This proves surjectivity. For injectivity in the colimit, a representative mapping to zero lies on a cover in the cofinal family, where the edge map just proved is injective, so the representative itself is zero. The two uses of cofinality are distinct: at each \(W\), it computes all degree-one classes; at \(X\), it lets a cover witnessing local vanishing be replaced by one whose intersections have the hypothesis.

## What this lesson does not prove

We use the sheafification, local image and fibre-product rules of lessons 1–2, and the cohomology, local vanishing, injective horseshoe, resolution comparison and universal delta-functor prerequisites stated in Cohomology on sites. We also use its first quadrant spectral-sequence theorem, with differential bidegree \((r,1-r)\), finite convergence in each total degree, and exactness of products of abelian groups. All simplicial matching, finite filling, free-complex acyclicity, degree refinement, homotopy equalization, connecting-map and basis-refinement arguments specific to this lesson are proved above.

The circle and interval groups used in section 8 were proved in lesson 3. We do not prove a general comparison with singular cohomology, a general theorem on cohomological descent, or a theory of derived simplicial spaces here. For historical orientation, the Stacks introduction locates hypercoverings in SGA 4, Exposé V, §7, and the wider descent formalism in Exposé Vbis. This distinguishes the two topics; no passage from SGA 4 is used as an unproved step in our arguments.

## References

- **[Stacks, Hypercoverings]** The Stacks Project Authors, *The Stacks Project*: [Tags 0DBB, 01G0 and 01G3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-semi-representable) for families and their associated presheaves; [Tags 01G5–01G6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-definition-hypercovering) for the object-based definition and ordinary nerve; [Tags 01GA–01GF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-acyclicity) for free-complex acyclicity; and [Tags 01GU–01GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-hyper-cech) for the cohomology comparison sequence. These are references for the statements; the finite-cone proof in section 3 supplies the complete local exactness argument used here.
- **[Stacks, refinement and comparison]** [Tags 01GH–01GK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-covering) for relative covers and changing a degree; [Tags 01GL–01GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-adding-simplices) for finite attachments; [Tags 01GO–01GS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-homotopies) for homotopy after refinement; [Tags 01GZ–01H0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-cohomology) for the colimit theorem; and [Tags 09VT–09VY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-section-hypercoverings-verdier) for Verdier's variant. The AI Integrated Stacks Project reader linked here contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
- **[Stacks, Simplicial Methods]** [Tags 017L and 017R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-exists-hom-from-simplicial-set-finite) for finite simplicial mapping objects and the nondegenerate-simplex decomposition; [Tag 0186](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-formula-limit) for matching tuples; [Tag 018S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-add-simplices) for finite simplex attachments; and [Tag 01A0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-Q) for homotopies on cochain complexes. The definitions, necessary identities and inverse verifications appear in sections 2 and 6 above.

- **[Conrad]** Brian Conrad, [*Cohomological descent*](https://math.stanford.edu/~conrad/papers/hypercover.pdf), January 24, 2003: Definition 4.1 and Examples 4.4–4.5 (pp. 23–25) for matching covers and coskeleta with a fixed augmentation; Definition 4.9 (p. 27) for split objects; and the opening of §5 (p. 31) for why the homotopy category is needed in the colimit formulation. They give an alternative exposition; the proofs above are complete without them.
