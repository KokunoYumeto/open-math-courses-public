# Grassmannians

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Grassmannian turns linear algebra into a family of geometric objects. Its points classify quotients of a vector space, while its maps from a parameter scheme classify quotients of a vector bundle on that scheme. The kernel must remain a subbundle after base change. This is what distinguishes a family of subspaces from a collection of subsheaves having the expected rank at some points.

We construct the Grassmannian with matrices, then use determinants to place it inside projective space. The same matrices compute infinitesimal motion. Finally, we examine equations, cells, and a first application to lines on a hypersurface. We also construct the functor for arbitrary quasi-coherent modules, separating representability from the stronger properties available for vector bundles.

The prerequisite is Representable functors and the functor of points, together with finite locally free modules, exterior powers, and smoothness of affine space over its base. Basic references are [Stacks], [AI Integrated Stacks Project], and [Vakil].

## 1 Matrices as families of quotients

Let \(S\) be a scheme, \(E\) a locally free module of rank \(n\), and \(0\leq r\leq n\). Define \(\operatorname{Gr}_r(E)(T)\), for \(f:T\to S\), to be isomorphism classes of surjections

\[
q:f^*E\twoheadrightarrow Q,
\qquad Q\text{ locally free of rank }r.
\]

The quotient convention is fixed throughout. An isomorphism preserves \(q\); because \(q\) is surjective it is unique if it exists. Pullback gives the functorial maps.

Locally \(Q\) is free and \(q\) splits. Its kernel \(K\) is therefore locally free of rank \(n-r\), and the exact sequence

\[
0\longrightarrow K\longrightarrow f^*E\longrightarrow Q\longrightarrow0
\]

remains exact after arbitrary pullback. Conversely, a rank-\((n-r)\) subbundle of \(f^*E\), meaning a subsheaf with locally free quotient, gives this quotient. Dualizing identifies rank-\(r\) quotients of \(E\) with rank-\(r\) subbundles of \(E^\vee\). There is no basis-free identification with rank-\(r\) subspaces of \(E\) itself.

Suppose first that \(E=\mathcal O_S^n\), with basis \(e_1,\ldots,e_n\). For an increasing \(r\)-subset \(I\), select the families for which the images of \(e_i\), \(i\in I\), form a basis of \(Q\). This condition defines an open subfunctor: the determinant of the corresponding map \(\mathcal O_T^r\to Q\) is invertible precisely on its required open. At each point some minor is nonzero, so these opens cover every family.

On such a chart, use those images as the basis of \(Q\). The quotient has a unique matrix \(M_I\) whose columns indexed by \(I\) form the identity. Its other \(r(n-r)\) entries are arbitrary functions. Conversely, every such matrix is a surjection. Thus the chart is \(\mathbb A_S^{r(n-r)}\). If another column set \(J\) is a basis, its determinant is a unit, and the change of chart is

\[
M_J=(M_I|_J)^{-1}M_I.
\]

These transitions satisfy the cocycle condition because they are changes of basis in the same quotient.

**Theorem 1.1.** The quotient functor \(\operatorname{Gr}_r(E)\) is represented by a scheme. It is smooth over \(S\), of relative dimension \(r(n-r)\), and commutes with arbitrary base change.

**Proof.** Quotient pairs glue as a Zariski sheaf: the unique isomorphisms preserving their quotient maps satisfy the cocycle condition, and locally free modules glue. For free \(E\), the representable open charts just constructed give a scheme by the gluing theorem of the preceding lesson. Their morphisms to \(S\) are smooth of the stated relative dimension. These properties are local on the source, so they hold for the Grassmannian.

For general \(E\), trivialize on a cover of \(S\). A change of frame induces, by precomposition of quotients, an isomorphism between the resulting Grassmannian functors and hence between their schemes. The cocycle equality follows either from matrix composition or from Yoneda. Glue these schemes over \(S\). The quotient description proves representability on all test schemes. It also shows that its pullback to \(S'\) represents \(\operatorname{Gr}_r(E|_{S'})\). Smoothness and dimension follow on the trivializing cover. When \(r=0\) or \(r=n\), the only quotient is respectively zero or the identity, so the scheme is \(S\). \(\square\)

There is a universal exact sequence on \(G=\operatorname{Gr}_r(E)\),

\[
0\longrightarrow\mathcal K\longrightarrow\pi^*E
\longrightarrow\mathcal Q\longrightarrow0.
\]

The matrices above are local descriptions of this sequence, not extra choices in the moduli problem.

## 2 Determinants recover the quotient

Taking the top exterior power of the universal quotient gives an invertible quotient

\[
\bigwedge^r\pi^*E\twoheadrightarrow\det\mathcal Q.
\]

The projective-space description from the preceding lesson therefore defines the **Plücker morphism**

\[
\iota:G\longrightarrow\mathbb P\!\left(\bigwedge^rE\right).
\]

For free \(E\), write \(p_I\) for the homogeneous coordinate indexed by an increasing \(r\)-subset. It is the determinant of the columns \(I\) of a quotient matrix. Thus \(\iota^{-1}(D_+(p_I))\) is exactly the chart used in Section 1.

**Theorem 2.1.** The Plücker morphism is a closed immersion. In particular \(G\to S\) is projective, and

\[
\iota^*\mathcal O(1)\simeq\det\mathcal Q.
\]

**Proof.** On the target chart \(D_+(p_I)\), normalize \(p_I=1\). Its coordinate algebra is a polynomial algebra on the ratios \(p_J/p_I\), for \(J\ne I\). The Grassmannian chart has coordinate algebra \(\mathcal O_S[a_{ij}]\), describing the columns outside \(I\). For each entry \(a_{ij}\), replace the corresponding identity column in \(I\) by column \(j\). The resulting determinant is \(a_{ij}\) times a sign fixed by reordering columns. Hence the homomorphism from the target coordinate algebra to the Grassmannian coordinate algebra contains every generator of the latter in its image. It is surjective, so the restricted morphism is a closed immersion.

The opens \(D_+(p_I)\) cover the entire target projective bundle, and closed immersions are local on the target. This proves the assertion when \(E\) is free; the argument on a trivializing cover proves it for \(E\). The target is the projectivization of a finite locally free module, so a closed subscheme is projective over \(S\). The identity of line bundles follows from the definition of the morphism by the displayed quotient. \(\square\)

This proof establishes the scheme structure of the image, including nilpotents, over an arbitrary base. A monomorphism that is injective on tangent spaces alone would not establish a closed immersion; for example, an open immersion can have both properties.

Properness also has an illuminating lattice interpretation. Let \(R\) be a valuation ring with fraction field \(F\), and let \(E_R\) be a finite free module. A quotient of \(E_F\) with kernel \(K_F\) extends by setting

\[
K_R=E_R\cap K_F,
\qquad Q_R=E_R/K_R.
\]

Here the intersection is taken inside \(E_F\). To verify local freeness even for a nondiscrete valuation, choose a matrix for the quotient over \(F\). Among its nonzero maximal minors choose one whose valuation is minimal. Divide by its submatrix to normalize those columns to the identity. Cramer's rule expresses every other entry as a signed ratio of a maximal minor to the chosen one. Its valuation is nonnegative, so all entries lie in \(R\). This normalized matrix is a surjection \(R^n\to R^r\), and its kernel is precisely \(K_R\). Thus the intersection construction gives a free quotient.

It is the only extension: any extending quotient is torsion-free, and its kernel is saturated, hence equals the intersection with its generic kernel. This gives existence and uniqueness in the valuative criterion, in agreement with projectivity. The choice of a minimal minor works because there are only finitely many minors and the value group is totally ordered.

## 3 Infinitesimal motion of a kernel

Let \(s:\operatorname{Spec}k\to S\) be a field-valued point and let \(q:E_s\to Q\) represent a point of the Grassmannian, with kernel \(K\). We compute the tangent space in the fibre over \(s\). A tangent vector is a quotient over \(D=k[\epsilon]/(\epsilon^2)\) reducing to \(q\).

**Proposition 3.1.** There is a canonical identification

\[
T_{[q]}\operatorname{Gr}_r(E_s)\simeq\operatorname{Hom}_k(K,Q).
\]

More generally the relative tangent bundle of \(G\to S\) is \(\mathcal H om(\mathcal K,\mathcal Q)\).

**Proof.** Let \(K_D\subset E_s\otimes_k D\) be the lifted kernel. For \(v\in K\), choose a lift \(v+\epsilon w\in K_D\). Send \(v\) to \(q(w)\). The choice of \(w\) changes by an element of \(K\): the difference of two lifts lies in \(\epsilon K_D\), since \(K_D\) is a direct summand and reduces to \(K\). Hence the map \(K\to Q\) is well defined and linear.

Choose a splitting \(E_s=K\oplus Q\) to check that this construction is a bijection. Given \(\phi:K\to Q\), the submodule generated by \(v+\epsilon\phi(v)\) is the graph of \(\epsilon\phi\), a direct summand with free quotient. It gives the inverse construction. Every lifted direct summand has this graph form, and the canonical map just defined reads off \(\phi\). Thus the answer is independent of the auxiliary splitting.

The same argument works locally on \(G\), with square-zero coefficients in any module. It identifies infinitesimal kernel changes with homomorphisms from the universal kernel to the universal quotient. These identifications are intrinsic, so they glue to the asserted tangent bundle. \(\square\)

If one instead identifies a deformation by the first-order change of the quotient map, its restriction to \(K\) has the opposite sign. Our convention reads the displacement of the kernel. The vector space is the same; fixing this sign avoids ambiguity when comparing descriptions.

On a normalized matrix chart a deformation is \([1\mid A+\epsilon B]\). Its kernel vectors change by \(-\epsilon Bv\), so the canonical homomorphism is \(-B\). There are \(r(n-r)\) independent entries, matching both the tangent dimension and the relative dimension of Theorem 1.1.

## 4 Equations of the Plücker image

Extend \(p_I\) to all ordered \(r\)-tuples by alternation, and set it to zero on repeated indices. For ordered tuples \(A=(a_1,\ldots,a_{r-1})\) and \(B=(b_1,\ldots,b_{r+1})\), the **Plücker relations** are

\[
\sum_{j=1}^{r+1}(-1)^j
p_{a_1\cdots a_{r-1}b_j}
p_{b_1\cdots\widehat b_j\cdots b_{r+1}}=0.
\]

They are identities among maximal minors over every commutative ring. One verification is to use the alternating relation among \(r+1\) vectors \(v_1,\ldots,v_{r+1}\) in a free rank-\(r\) module:

\[
\sum_{j=1}^{r+1}(-1)^j
\det(v_1,\ldots,\widehat v_j,\ldots,v_{r+1})v_j=0.
\]

Each coordinate is a determinant with a repeated row, hence zero. Apply the alternating linear form obtained by wedging against the columns indexed by \(A\) to obtain the stated relation. This is a polynomial identity, so it remains valid without assuming that any minor is a unit.

**Proposition 4.1.** These relations cut out the Plücker image as a closed subscheme of \(\mathbb P(\bigwedge^rE)\), on every trivializing open of \(E\).

**Proof.** Work in the chart \(p_I=1\). The single replacements of elements of \(I\) specify entries \(a_{ij}\), with the signs fixed by the minors of the normalized matrix. We show that every remaining \(p_J\) is forced to equal the corresponding minor of this matrix.

Induct on \(d=|J\setminus I|\). For \(d=0\), this is the normalization; for \(d=1\), it is the definition of the entries. If \(d>1\), choose \(i\in I\setminus J\) and use the relation with \(A=I\setminus\{i\}\) and \(B=(i,J)\), maintaining ordered indices and their alternating signs. The term belonging to \(i\) is \(\pm p_Ip_J\). Terms for indices in \(I\cap J\) vanish by repeated indices in the first factor. Every other term is a single-replacement coordinate times a coordinate indexed by \(\{i\}\cup(J\setminus\{j\})\). The latter has distance \(d-1\) from \(I\). Since \(p_I=1\), this relation determines \(p_J\) from coordinates already determined by induction.

The normalized matrix minors satisfy that same relation and the same initial values, so they are the forced values. Therefore the chart algebra defined by the relations is generated by the \(a_{ij}\), and its map to the polynomial algebra in those entries is inverse to the map assigning the single-replacement coordinates. There are no additional relations on those entries: an arbitrary normalized matrix satisfies all the displayed equations. These inverse maps identify the two chart schemes. The projective standard charts cover the scheme cut out by the relations, proving equality with the image. \(\square\)

For \(r=2,n=4\), the only needed equation is

\[
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0.
\]

On \(p_{12}=1\), write the quotient matrix as

\[
\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.
\]

Its other coordinates are

\[
p_{13}=c,\quad p_{14}=d,\quad p_{23}=-a,
\quad p_{24}=-b,\quad p_{34}=ad-bc.
\]

The quadratic equation eliminates \(p_{34}\), leaving the four free entries. Permuting indices gives the same verification on every chart, so this single quadric defines \(\operatorname{Gr}_2(k^4)\) over any field, including characteristic two. Its partial derivatives cannot all vanish at a projective point: they are the six coordinates, paired up with signs. Thus it is smooth.

For \(r=1\), the functor is the rank-one quotient functor, so \(\operatorname{Gr}_1(E)=\mathbb P(E)\). For \(r=n-1\), kernel lines give \(\operatorname{Gr}_{n-1}(E)=\mathbb P(E^\vee)\). These statements specify which dual appears.

## 5 General modules and equations on quotients

The quotient functor makes sense for an arbitrary quasi-coherent \(E\). It still has a representing scheme. However, its charts need not be affine spaces or of finite type, and no general smoothness or projectivity assertion follows.

**Proposition 5.1.** For a quasi-coherent module \(E\) on any scheme \(S\) and an integer \(r\geq0\), the functor of locally free rank-\(r\) quotients of \(f^*E\) is represented by a scheme.

**Proof.** On \(\operatorname{Spec}A\subset S\), write \(E=\widetilde M\). For \(r>0\), choose an ordered \(r\)-tuple \((m_1,\ldots,m_r)\) of elements of \(M\). Select the open condition that their images form a basis of the quotient. In this basis, a quotient is exactly an \(A\)-linear map \(M\to R^r\) sending \(m_j\) to the \(j\)-th standard basis vector, for every \(A\)-algebra \(R\).

Introduce symbols \(z_{i,m}\), linear in \(m\), for \(1\leq i\leq r\). The algebra representing such maps is

\[
C_{\boldsymbol m}
=\operatorname{Sym}_A(M^{\oplus r})/
(z_{i,m_j}-\delta_{ij})_{i,j}.
\]

The symmetric algebra already encodes additivity and \(A\)-linearity in each copy of \(M\). The specified images ensure surjectivity. This algebra represents the selected chart on affine tests; on general tests, its maps and the linear maps both glue, so it represents the chart there too.

The images of elements of \(M\) generate every quotient. At a point choose \(r\) of them forming a basis modulo the maximal ideal; the determinant remains invertible in a neighborhood. These charts therefore cover the functor. Their membership conditions are open and commute with base change. Quotient pairs form a Zariski sheaf by the uniqueness of their compatible isomorphisms. The gluing criterion represents the functor on this affine base. Applying the same argument over an affine cover of \(S\), the canonical functorial identifications glue the resulting schemes. For \(r=0\), the zero quotient gives \(S\). \(\square\)

For example, let \(E=\mathcal O_S/(t)\) and \(r=1\). A locally free rank-one quotient can exist only when \(t=0\) on the parameter scheme: multiplication by \(t\) annihilates a line bundle only if it is zero. Conversely, on \(V(t)\) the identity line quotient is unique. Thus the Grassmannian is \(V(t)\), which need not be smooth or flat over \(S\).

Suppose a finite locally free \(E_0\) surjects onto \(E\), with kernel \(N\). On \(\operatorname{Gr}_r(E_0)\), the quotient factors through \(E\) exactly when the composite \(N\to\mathcal Q\) is zero. Locally choose a frame of \(\mathcal Q\). The coordinates of the images of all local sections of \(N\) generate an ideal; its zero scheme represents this condition. The ideals agree when the frame changes. This gives a closed Grassmannian of quotients satisfying additional relations, a construction that will recur for Quot schemes.

## 6 Cells and lines on hypersurfaces

Over a field, dualize a rank-\(r\) quotient to its row space, an \(r\)-subspace of the dual \(n\)-space. Fix the ordered basis and write the unique reduced row-echelon form. For pivot positions

\[
1\leq i_1<\cdots<i_r\leq n,
\]

row \(a\) has pivot \(1\) at \(i_a\), zeros before it, and zeros in other pivot columns. The entries after its pivot in nonpivot columns are free. Their number is

\[
d_I=\sum_{a=1}^r(n-r+a-i_a).
\]

These descriptions also give locally closed subschemes: require the ranks of successive initial-column matrices to take prescribed values, using vanishing of larger minors and nonvanishing of chosen minors. Row reduction then identifies each stratum with \(\mathbb A^{d_I}\). These are the Schubert cells for the chosen flag. They are a stratification, rather than an open cover; the largest cell has dimension \(r(n-r)\), and the final pivot set gives a zero-dimensional cell.

For a finite field, each cell contributes \(q^{d_I}\) points. The resulting polynomial is the Gaussian binomial coefficient

\[
\#\operatorname{Gr}_r(\mathbb F_q^n)(\mathbb F_q)
=\begin{bmatrix}n\\r\end{bmatrix}_q
=\prod_{a=0}^{r-1}\frac{q^{n-a}-1}{q^{r-a}-1}.
\]

The counting interpretation and the limit at \(q=1\) are developed in Counting over finite fields and the limit q to one. Here the cells explain geometrically why this count is a polynomial with nonnegative coefficients.

A rank-two quotient \(V\to Q\) gives the line \(\mathbb P(Q)\subset\mathbb P(V)\). Thus lines in our quotient projective space \(\mathbb P(V)\) are parametrized by \(\operatorname{Gr}_2(V)\). A degree-\(d\) hypersurface has equation \(f\in\operatorname{Sym}^dV\), and contains this line exactly when the image of \(f\) in \(\operatorname{Sym}^dQ\) is zero. On the Grassmannian this is the zero scheme of a section of \(\operatorname{Sym}^d\mathcal Q\), a bundle of rank \(d+1\). It therefore defines a closed scheme of lines, including their infinitesimal families.

For a cubic in projective three-space, \(\operatorname{Gr}_2(V)\) has dimension four and the section has rank four. This suggests a zero-dimensional scheme when the section is sufficiently transverse; it does not yet prove transversality or the number of lines. Those questions belong to the lesson on Hilbert tangent spaces and obstructions.

## 7 Exercises

1. **Basic.** Compute the Grassmannians of rank zero, rank one, and full-rank quotients. Explain the duality relating a rank-\((n-1)\) quotient to a line subbundle.

2. **Intermediate.** In \(\operatorname{Gr}_2(k^4)\), take the chart \(p_{12}=1\) displayed in Section 4. Describe the overlap with \(p_{13}\ne0\) and write its normalized quotient matrix. Verify the quadratic equation on this overlap.

3. **Intermediate.** Extend a quotient over the fraction field of a valuation ring using a maximal minor of minimal valuation. Prove that the resulting kernel is saturated and that the extension is unique.

4. **Intermediate.** Deform the matrix \([1\mid A]\) to \([1\mid A+\epsilon B]\). Compute the tangent homomorphism \(K\to Q\), including its sign. Explain how the answer changes on switching matrix charts.

5. **Advanced.** Prove that the Plücker relations define the image over an arbitrary ring by reconstructing all coordinates from single replacements on \(p_I=1\). Explain why checking only geometric points would be insufficient.

6. **Intermediate.** Let \(V\) have dimension four and \(f\in\operatorname{Sym}^3V\). Write the four equations on the chart \([1\mid A]\) imposing that the associated line lie in \(V(f)\). Determine why these equations commute with every base change.

## 8 Solutions

**1.** The zero quotient and the identity quotient are unique, so their schemes are the base. A rank-one quotient is exactly the functor represented by \(\mathbb P(E)\). For a rank-\((n-1)\) quotient, the kernel is a line subbundle of \(E\); dualizing the split exact sequence makes its dual an invertible quotient of \(E^\vee\). Thus its scheme is \(\mathbb P(E^\vee)\). “Subbundle” is essential to preserve exactness after base change.

**2.** Here \(p_{13}=c\), so the overlap is \(D(c)\subset\mathbb A^4\). The columns numbered \(1,3\) form \(\begin{pmatrix}1&a\\0&c\end{pmatrix}\). Multiplying its inverse into the original matrix gives

\[
\begin{pmatrix}
1&-a/c&0&b-ad/c\\
0&1/c&1&d/c
\end{pmatrix}.
\]

Its minors are those of the original matrix divided by \(c\), since the change-of-basis determinant is \(1/c\). The quadratic expression is therefore divided by \(c^2\), and remains zero. Conversely, on the projective chart where \(p_{13}=1\), the equation solves for the missing complementary coordinate. Repeating by permutation on all six charts verifies the quadric scheme, rather than merely its field-valued points.

**3.** Cramer's rule gives entries that are ratios of maximal minors. Minimal valuation puts them all in the valuation ring, and identity columns make the matrix surjective there. Its quotient is free, so if \(a v\) is in the kernel for nonzero \(a\in R\), then \(a q(v)=0\) implies \(q(v)=0\); the kernel is saturated. Its generic kernel is the prescribed one, so it equals \(R^n\cap K_F\). For any other extending quotient, the same saturation argument gives the same kernel. Quotient pairs with the same kernel are canonically isomorphic, which proves uniqueness.

**4.** Identify the original kernel by \(v\mapsto(-Av,v)\). A lifted kernel vector is \((-(A+\epsilon B)v,v)\), whose first-order displacement has image \(-Bv\) in \(Q\). Thus the tangent homomorphism is \(-B\) in these bases. On another chart the quotient and kernel bases change, and the homomorphism changes by their induced precomposition and postcomposition. Its definition by lifting a kernel vector is intrinsic, so these changes glue exactly to \(\mathcal H om(\mathcal K,\mathcal Q)\).

**5.** The alternating determinant identity proves every relation on a quotient matrix. In the other direction, normalize \(p_I=1\), define matrix entries by single replacements, and induct on \(|J\setminus I|\). The relation with \(A=I\setminus\{i\}\), \(i\in I\setminus J\), and \(B=(i,J)\) expresses \(p_J\) in terms of closer coordinates. The minors of the constructed matrix obey that recurrence with the same initial values. Thus the normalized coordinate algebra is the polynomial algebra in its free entries. These algebra isomorphisms hold over arbitrary rings and glue over the projective charts. Equality on geometric points alone could miss a nilpotent thickening of the image; algebra isomorphisms rule it out.

**6.** Write the quotient basis as \(u,v\). Replace each of the four basis elements of \(V\) in \(f\) by its image, namely the corresponding linear form in \(u,v\) given by a column of \([1\mid A]\). The result is a binary cubic

\[
F_0(A)u^3+F_1(A)u^2v+F_2(A)uv^2+F_3(A)v^3.
\]

The four coefficient polynomials \(F_i(A)\) must vanish. A change of quotient basis changes this four-component vector by the invertible matrix of \(\operatorname{Sym}^3\) of that basis change, preserving its zero scheme. Symmetric powers and evaluating a polynomial commute with arbitrary base change, so these chart ideals glue to the required functorial closed subscheme.

## What this lesson does not prove

We use smoothness of affine space and locality of smoothness, as in [Stacks, Tags 01V4–01V5], and properness of projective morphisms, as in [Stacks, Tag 01W7 and the projective-morphism section]. The valuation computation supplies its own extension argument. We do not compute the degree of the scheme of lines on a cubic or its reducedness here. We also do not claim that the quadratic relations generate the unsaturated homogeneous ideal as a graded ideal; Proposition 4.1 proves the equality of the projective closed subschemes, which is the assertion needed for the closed immersion.

## References

- [Stacks] The Stacks project, *Constructions of Schemes*, Tags 089R, 089T, 089U and 089V, retained in the [Grassmannian section of AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#section-grassmannian).
- [AI Integrated Stacks Project] *Constructions of Schemes*, [Plücker closed-immersion lemma](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#lemma-grassmannian-pluecker). This edition has AI-proposed corrections and AI-written additions; they have not been reviewed by the Stacks project's maintainers.
- [Vakil] R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, sections 7.7 and 16.4.
