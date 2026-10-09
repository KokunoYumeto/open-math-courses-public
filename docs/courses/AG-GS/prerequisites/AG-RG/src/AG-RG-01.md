# Tori, maximal tori and their conjugacy

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A diagonal matrix is easy to understand because its eigenspaces separate the action into one-dimensional pieces. A torus is the group-scheme version of this diagonal action. Over a field that is not algebraically closed, or over a scheme, the eigenspaces may appear only after changing the base. We therefore keep track of which conclusions hold on the original base and which hold locally for the étale topology.

We assume affine group schemes, smooth morphisms, faithfully flat descent, and the character description of groups of multiplicative type. Basic references are Conrad's *Reductive group schemes*, SGA 3, and Milne's *Algebraic Groups*. The first two treat arbitrary bases; the third provides complementary field arguments.

## Diagonal actions and their descent

For a scheme $S$, a **torus** is a group scheme $T$ that is étale locally isomorphic to $\mathbf G_{m,S}^{r}$, with $r$ locally constant. Its character sheaf is

$$
X^*(T)=\underline{\operatorname{Hom}}_{S\text{-groups}}(T,\mathbf G_m).
$$

It is a locally constant sheaf of finite free abelian groups on the étale site. Its dual is the cocharacter sheaf $X_*(T)$. The pairing is fixed by

$$
\chi\circ\lambda(t)=t^{\langle\chi,\lambda\rangle}.
$$

For $T=\mathbf G_m^r$, the characters $e_i(t_1,\ldots,t_r)=t_i$ and coordinate cocharacters form dual bases. A representation of a split torus on a finite locally free module $M$ is a grading

$$
M=\bigoplus_{\chi\in\mathbb Z^r}M_\chi,
$$

with finitely many nonzero summands locally on $S$. Indeed, write its comodule map as $m\mapsto\sum_\chi m_\chi\otimes z^\chi$. Coassociativity implies that each $m_\chi$ has weight $\chi$, and the counit gives $m=\sum m_\chi$. Linear independence of the Laurent monomials makes the sum direct. Each summand is a direct summand of $M$, hence finite locally free.

**Example.** Multiplication on $\mathbb C$ gives an embedding

$$
\operatorname{Res}_{\mathbb C/\mathbb R}\mathbf G_m\longrightarrow\operatorname{GL}_{2,\mathbb R},\qquad
a+bi\longmapsto\begin{pmatrix}a&-b\\b&a\end{pmatrix}.
$$

After base change to $\mathbb C$, the two eigenvalues are $a+bi$ and $a-bi$, so this is a two-dimensional torus. Complex conjugation interchanges its two characters. A split real torus has trivial conjugation action on its character lattice, so this torus is not split. The descent action records a real distinction that disappears over $\mathbb C$.

The anti-equivalence between tori and locally constant free character sheaves follows by descent from the split case: a change of basis in $\mathbb Z^r$ gives the corresponding monomial automorphism of $\mathbf G_m^r$, and these constructions carry inverse descent data to inverse descent data. The alternative definition using an fpqc splitting cover gives the same tori; we prove this after Lemma 3.1. One cannot replace the character sheaf by a single lattice with trivial action on an arbitrary base.

## 1. What maximality means

A closed subtorus $T\subset G$ is **maximal** if $T_{\bar s}$ is a maximal torus of $G_{\bar s}$ at every geometric point of $S$. We always use this fibrewise definition. A **reductive group scheme** is a smooth affine group scheme of finite presentation whose geometric fibres are connected reductive algebraic groups. A connected smooth affine group over an algebraically closed field is reductive when it has no nontrivial smooth connected normal unipotent subgroup.

This definition of maximality is preserved by every base change. Over an algebraically closed field, maximality also persists on extending that algebraically closed field. To see this, spread a putative larger torus and its inclusion out over a finitely generated subalgebra of the extension field. The dimensions are locally constant after restricting to a suitable open subset. A closed point in that open subset has residue field the original algebraically closed field, and specialization would give a larger torus there.

**Example 1.1. Diagonal matrices.** In $\operatorname{GL}_{n,S}$, the diagonal torus $D=\mathbf G_m^n$ is maximal. For a matrix $A=(a_{ij})$ over an $S$-algebra $R$, commuting with the universal diagonal matrix says

$$
a_{ij}(z_i-z_j)=0\quad\text{in }R[z_1^{\pm1},\ldots,z_n^{\pm1}].
$$

Comparison of distinct Laurent monomials forces $a_{ij}=0$ for $i\ne j$. Thus $C_{\operatorname{GL}_n}(D)=D$ as group schemes over every base. Any torus containing $D$ centralizes it and is therefore equal to it.

**Example 1.2. Two real tori.** In $\operatorname{SL}_{2,\mathbb R}$, compare

$$
D=\{\operatorname{diag}(t,t^{-1})\},\qquad
K=\left\{\begin{pmatrix}a&-b\\b&a\end{pmatrix}:a^2+b^2=1\right\}.
$$

Over $\mathbb C$, the second group has characters $a+bi$ and its inverse, so both groups become the same type of one-dimensional torus. An eigenbasis gives a conjugation in $\operatorname{GL}_2(\mathbb C)$; rescaling one eigenvector makes its determinant one, giving a conjugation in $\operatorname{SL}_2(\mathbb C)$. They are maximal because their complex fibres are maximal. They are not conjugate over $\mathbb R$: the character lattice of $D$ has trivial conjugation action, while that of $K$ has the sign action. A real conjugation would be an isomorphism of real tori and would preserve these actions.

## 2. Moving tori over an algebraically closed field

We first establish the classical tools used in the conjugacy argument. The proofs work in every characteristic. Orbit representability and the closed-orbit lemma are the exact supporting results of the supporting lesson [Group schemes over a field](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-03.html); finite free-action quotients are provided by [Quotients and torsors](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-04.html).

**A line detecting a subgroup.** Every closed subgroup $H$ of an affine algebraic group $K$ is the stabilizer of a line in a finite-dimensional representation. To construct it, let $I$ be the defining ideal of $H$ in $k[K]$, with the right regular action. The coalgebra identities put any finite collection of functions in a finite-dimensional stable subspace: expand their coproducts in linearly independent first factors; coassociativity makes the second factors a stable finite-dimensional space. Choose such a space $W$ containing ideal generators, and put $V=I\cap W$. A group element stabilizes $V$ exactly when its right translation preserves the ideal generated by $V$, namely $I$, which is exactly the condition that it belongs to $H$. The line $\bigwedge^{\dim V}V$ in $\bigwedge^{\dim V}W$ has the same stabilizer. This is an identity on test algebras, since the ideal and exterior-power conditions are scheme-theoretic. Applying the same finite-dimensional construction to algebra generators of $k[K]$ gives a faithful representation: its matrix coefficients generate $k[K]$, so its map to a general linear group is a closed immersion. These observations prove the stabilizer and linearity statements used below.

**Triangularization.** Every finite-dimensional representation of a smooth connected solvable group $B$ has an invariant full flag. Induct on the derived length. The connected reduced derived subgroup $D$ has smaller derived length, so has common eigenspaces; the nonzero ones form a finite collection of linearly independent character spaces. Normality of $D$ makes $B$ permute them, and connectedness makes every permutation constant. Choose one, $V_\chi$. The subgroup $D$ acts on it by scalars. Its scalar character is trivial: each commutator has determinant one, so $\chi^d=1$, where $d=\dim V_\chi$; a smooth connected group has no nontrivial character with finite image. The last statement is valid when the finite image is nonreduced, because a map from a reduced scheme factors through its reduction. Thus the image of $B$ on $V_\chi$ is commutative. Commuting matrices have a common eigenvector: an eigenspace of a nonscalar member is a proper invariant space, and induction on its dimension finishes the argument. We have obtained an invariant line. Repeat on its quotient to obtain the full flag. This proves Lie–Kolchin triangularization directly, without using the fixed-point theorem.

**Fixed points on complete varieties.** A smooth connected solvable $B$ acting on a nonempty complete variety has a fixed point. Choose a closed orbit, using the closed-orbit lemma. Its stabilizer $H$ is detected by the preceding line construction, so this complete homogeneous orbit maps equivariantly to projective space as the orbit of that line. Its image is closed. Triangularize the representation, with flag $V_1\subset\cdots\subset V_n$. Choose the least $d$ for which the closed image meets $\mathbf P(V_d)$. The intersection avoids $\mathbf P(V_{d-1})$, so is both complete and contained as a closed subvariety in an affine chart. It is therefore finite. Connectedness makes $B$ fix its points. Since the image is one homogeneous orbit, that orbit is a point, and so was the original closed orbit. This proves the required fixed-point theorem.

**Solvable structure.** We prove that $B=U\rtimes T$ for a smooth connected solvable $B$ over our algebraically closed field, with $U$ smooth connected unipotent and $T$ a torus, and that all maximal tori are $U$-conjugate. Triangularize a faithful representation. Projection to its diagonal gives a torus $D$ and a kernel $U$ contained in the upper unitriangular group. Order the upper entries by increasing distance from the diagonal, refining equal distances in any order. Setting successive entries equal to zero gives a normal filtration of the unitriangular group with additive one-dimensional quotients: every cross term contributing to a given distance uses smaller distances, which have already vanished. Intersect it with $U$. Each successive quotient is a closed subgroup of $\mathbf G_a$, and diagonal conjugation on it is multiplication by a character of $D$; the upper unitriangular part acts trivially. Remove repeated terms.

Here is the splitting step, including finite additive kernels. A proper closed subgroup $N$ of $\mathbf G_a$ is finite and is the kernel of an additive polynomial $P$. Indeed its ideal has one monic generator of degree $d$, with $P(0)=0$. The subgroup identity makes $P(X+Y)$ vanish modulo $(P(X),P(Y))$. The polynomial $P(X+Y)-P(X)-P(Y)$ has degree less than $d$ in each variable, so its vanishing in that quotient, whose basis is $X^iY^j$ for $i,j<d$, makes it zero. Comparison of coefficients gives only powers $X^{p^i}$ in positive characteristic, or a linear polynomial in characteristic zero. The quotient is $\mathbf G_a$ via $P$. An action of a torus on this quotient is again linear, since automorphisms of the affine line fixing zero have degree one.

An extension of a torus $D$ by a vector line splits. Its torsor has a regular section because quasi-coherent first cohomology vanishes on the affine scheme $D$. The multiplication defect is a regular degree-two cocycle. Exactness of torus invariants makes the regular group cohomology in positive degrees vanish, so a correction makes the section a homomorphism. The same vanishing in degree one makes two sections conjugate by the vector line.

An extension by a finite $D$-stable $N\subset\mathbf G_a$ also splits. Push it out along $N\hookrightarrow\mathbf G_a$; concretely this is the finite free-action quotient of the product with $\mathbf G_a$. The resulting vector-line extension splits by the preceding paragraph. In these coordinates the original extension is described by a crossed homomorphism $D\to\mathbf G_a/N$: in each fibre its points are a coset of $N$. That crossed homomorphism is principal, by degree-one vanishing for the quotient vector line. Its conjugating element lifts from $(\mathbf G_a/N)(k)$ to $\mathbf G_a(k)$, since $k$ is algebraically closed. After conjugation the original extension is $N\rtimes D$. This also covers $N=\mathbf G_a$ by the preceding paragraph.

Induct on the filtration length of $U$. In $B/N$ a section of the diagonal quotient exists by induction; its inverse image is the extension by the last, central-in-$U$, additive subgroup $N$ just treated. Splitting that extension gives a section in $B$. Quotients by the possibly nonfinite unipotent terms are affine: for a normal unipotent subgroup, the line-stabilizer construction has trivial character on that subgroup, and its translates span a representation on which the subgroup acts trivially. The representation kernel is exactly the subgroup; its closed image realizes the quotient. The quotient map is faithfully flat, by generic flatness and translation over the field. Thus the induction uses actual algebraic groups.

We now have $B\simeq U\times D$ as varieties. Smoothness and connectedness of $B$ and $D$ imply smoothness and connectedness of $U$. The torus section is $T$. Replacing the terms of the unitriangular filtration by their reduced identity components gives a $B$-stable filtration of $U$ with smooth connected one-dimensional unipotent quotients. Such a quotient is $\mathbf G_a$. For completeness, a smooth connected one-dimensional affine group has a smooth projective completion $C$, and translations extend to $C$ and fix its finite boundary. If $g(C)\geq1$, the line bundle $T_C(-\partial C)$ has negative degree, so has no sections; this contradicts the nonzero tangent vector supplied by translations. Here $\deg T_C=2-2g$, from duality for curves, and the boundary is nonempty since the group is affine. Thus $g=0$, and $C\simeq\mathbf P^1$. Three boundary points would have zero-dimensional stabilizer; two give the diagonal torus; one gives the affine linear group, whose unipotent subgroup is the translation group. The unipotent case is therefore $\mathbf G_a$. The duality input is exactly the supporting lesson *Dualizing sheaves and Serre duality for projective schemes*; the degree-zero genus calculation is also written in the rank-one lesson, Section 2.

The filtration is central in $U$, and each $T$-action on a quotient is linear. A torus $M\subset B$ intersects $U$ trivially, as its diagonalizable representation cannot have a nontrivial unitriangular image. Its projection embeds in $D$. In $U\rtimes q(M)$ it is a complement. Successive vector-line degree-one vanishing through the central filtration conjugates this complement to the chosen section by an element of $U$. Maximality then makes $q(M)=D$. This proves both the structure theorem and conjugacy of maximal tori. In a commutative $B$, the action is trivial, so the decomposition is the direct product $T\times U$.

**Lemma 2.1.** If $G$ is smooth connected affine over an algebraically closed field $k$, its maximal connected solvable subgroups are conjugate, and $G/B$ is complete for each such subgroup $B$.

**Proof.** Choose a connected solvable subgroup $B$ of largest dimension. Chevalley's stabilizer theorem gives a faithful representation and a line whose stabilizer is $B$. Lie–Kolchin triangularization refines that line to a full flag stabilized by $B$, with the same stabilizer. Every full-flag stabilizer in $G$ has solvable identity component, hence has dimension at most $\dim B$. The orbit of our flag therefore has smallest possible dimension among all flag orbits. A boundary orbit of any orbit has smaller dimension, so this orbit has no boundary: it is closed in the projective full-flag variety. It is $G/B$, hence complete.

Let $B'$ be any maximal connected solvable subgroup. Its action on $G/B$ has a fixed point $gB$. Thus $B'\subset gBg^{-1}$, and maximality gives equality. This proves conjugacy and transfers completeness to every $B'$. The stabilizer theorem and boundary-dimension statement are available in Milne, Theorem 4.27 and Proposition 1.66. $\square$

**Theorem 2.2.** Any two maximal tori in a smooth connected affine group over an algebraically closed field are conjugate.

**Proof.** A torus is connected and solvable, so it lies in a maximal connected solvable subgroup; one obtains such a subgroup by increasing dimension until this is no longer possible. For maximal tori $T_1,T_2$, choose $B_1,B_2$ containing them. Lemma 2.1 gives $gB_2g^{-1}=B_1$. Both $T_1$ and $gT_2g^{-1}$ are maximal tori of the connected solvable group $B_1$. The solvable-group conjugacy theorem supplies $u\in B_1(k)$ with $u gT_2g^{-1}u^{-1}=T_1$. $\square$

No conclusion here asserts conjugacy under $G(k)$ when $k$ is not algebraically closed. Example 1.2 is already a counterexample.

## 3. Deforming an embedding rather than an eigenvalue

We need a mechanism that transports a torus from one fibre to nearby fibres. It uses the entire torus action, which retains information even when differentiating its characters loses information in positive characteristic.

For tori $T_1,T_2\subset G$, define

$$
\operatorname{Transp}_G(T_1,T_2)(R)
=\{g\in G(R):g(T_1)_R g^{-1}=(T_2)_R\}.
$$

The normalizer $N_G(T)$ is the transporter from $T$ to itself. The centralizer $C_G(T)$ asks that the induced automorphism of $T$ be the identity. Both conditions concern subgroup schemes after arbitrary base change, rather than just the rational points of a fibre.

**Lemma 3.1. Torus deformation.** Let $G$ be smooth affine of finite presentation over $S$.

1. The normalizer and centralizer of a subtorus are closed subgroup schemes of finite presentation. Transporters between tori of the same rank are schemes of finite presentation.
2. These normalizers, centralizers, and transporters are smooth over $S$.
3. A torus embedded in a fibre $G_s$ extends, after an étale neighbourhood with unchanged residue field, to a torus embedded in $G$.

**Proof.** We explain the equations, the deformation obstruction, and then the passage from formal to étale neighbourhoods.

After splitting a torus, its finite subgroups $T[n]$ are schematically dense, universally on the base. A Laurent polynomial has finite support; take $n$ larger than all differences between exponent coordinates. Its distinct monomials remain distinct modulo $n$, so a nonzero Laurent polynomial remains nonzero on $T[n]$. This works over any ring. The closed conditions on every $T[n]$ therefore detect both inclusion and equality of maps on $T$.

For a finite locally free scheme $Y$ and an affine finitely presented scheme $X$, maps $Y\to X$ are represented by an affine finitely presented scheme. On an affine chart choose a basis of $\mathcal O(Y)$; the images of generators of $\mathcal O(X)$ are coordinate vectors, and its finitely many relations become polynomial equations in those vectors. Factoring through a closed subscheme adds closed equations. Apply this construction to conjugation on $T[n]$. The resulting intersections represent the centralizer and the inclusion transporter. Reduction to a noetherian model makes the defining ideals finitely generated. Descent of the finitely many equations and their base-change interpretation then gives finite presentation over the original base. For equal-rank tori, an inclusion is an equality if it is so on one fibre, after restricting to a neighbourhood; the equality transporter is the corresponding open part. For the normalizer the two inclusion conditions give equality directly.

Now let $R\to R/I$ have $I^2=0$. Two liftings of a torus homomorphism $f_0:T_0\to G_0$ differ by a regular crossed homomorphism with values in

$$
M=\operatorname{Lie}(G_0)\otimes_{R/I}I,
$$

with the action through $\operatorname{Ad}\circ f_0$. More explicitly, lifting a scheme map first gives a multiplication defect $c(t,u)$, and associativity is exactly the degree-two cocycle equation. Correcting a lift by a function $b(t)$ changes $c$ by its coboundary. Once the defect vanishes, the difference between two homomorphisms is a degree-one cocycle. Conjugating by an element infinitesimally equal to one changes that cocycle by a degree-one coboundary.

Taking invariants for a torus is exact, by the weight decomposition. The regular group-cochain resolution computes its derived functors, so its cohomology in positive degrees is zero. One may see the contraction directly in the homogeneous bar resolution: integration in one torus variable means taking the coefficient of its trivial character. This normalized invariant projection commutes with translations, and the alternating face maps give $dh+hd=1$ in positive degrees. Thus the degree-two defect can be removed, and any two liftings are infinitesimally conjugate. This is the obstruction argument of SGA 3, Exposé III, §2, in the special case in which all obstructions vanish.

Lift a transporter point $g_0$ arbitrarily using smoothness of $G$. The transported torus and the target torus have the same reduction. The degree-one calculation corrects $g$ by an element reducing to one so that it transports the whole torus. For a centralizer point, the corrected element first normalizes $T$. Its action on the character lattice reduces to the identity. Automorphisms of a torus are étale locally integral matrices, with no infinitesimal deformations, so this action is the identity already over $R$. This proves formal smoothness of the three representing schemes, hence smoothness by finite presentation. In particular,

$$
\operatorname{Lie}(C_G(T))=\operatorname{Lie}(G)^T.
$$

For existence in (3), first take a noetherian local model essentially of finite type over $\mathbb Z$. Over its completion, lift the fibre torus as an abstract torus using its finite étale character splitting. The degree-two vanishing lifts its homomorphism to $G$ successively modulo the powers of the maximal ideal. We prove the effectivity statement needed to turn this formal homomorphism into an actual one.

Let $A$ be Noetherian and complete for an ideal $J$, and first let the source be $D_A(M)$. Its completed coordinate module consists of families $(a_m)_{m\in M}$ tending $J$-adically to zero, while its actual coordinate module consists of families of finite support. Compatible homomorphisms modulo $J^n$ give a map from $A[G]$ to the former. For $f\in A[G]$, write its coproduct as a finite sum $\sum_{i=1}^r f_i\otimes g_i$. Compatibility with the coproduct says that the coefficient matrix of its completed image has entries

$$
\delta_{m,n}a_m=\sum_{i=1}^r b_{i,m}c_{i,n},
\tag{3.1}
$$

where the right side consists of the coefficient families of the images of the $f_i$ and $g_i$. Regard these columns as elements of $A^M$. Every $a_ne_n$ belongs to the finite module spanned by the $r$ families $(b_{i,m})_m$. The submodule generated by all $a_ne_n$ is therefore finitely generated, since $A$ is Noetherian. It is the direct sum of the ideals $Aa_n$ in their distinct coordinate positions. Finite generation forces all but finitely many of these ideals to be zero. Thus the image of $f$ has finite support. This holds for every $f$, so the completed map takes values in $A[M]$ itself. Its algebra and Hopf identities hold because $A[M]$ and $A[M\times M]$ inject into their completions. This proves existence and uniqueness of the actual homomorphism. For a source split by a finite étale cover, the cover and its double overlap are also complete; apply the split proof there and use uniqueness to descend. This supplies the full effectivity statement, with its exceptional multiplicative-type hypothesis made visible.

The lift is an embedding. Its kernel meets each finite subgroup $T[n]$ in a finite scheme whose special fibre is trivial. The augmentation ideal of that finite algebra is a finite module over the complete local ring, and its reduction vanishes; Nakayama makes it zero. Hence the kernel is trivial on every $T[n]$. On each geometric fibre the kernel is a diagonalizable subgroup of a torus, so density of its torsion implies that the fibre kernel is trivial. The identity section into the kernel is a finitely presented closed immersion with flat source and is an isomorphism on every fibre. It is an isomorphism: for its ideal $I$ the exact sequence and flatness of the quotient give $I\otimes k(s)\hookrightarrow A_K\otimes k(s)$; fibre equality makes this zero, and Nakayama locally gives $I=0$.

Here is also the closed-immersion criterion used for this monomorphism. Split its multiplicative-type source $D_R(M)$ and grade the coordinate ring $C$ of its target by right translation. Pullback takes $C_m$ into $Rz^m$, with coefficient ideal $I_m\subset R$. On a field fibre, a monic multiplicative-type homomorphism is closed: triangularize its diagonalizable action in a faithful representation; the occurring weights generate $M$, since otherwise their common kernel would be nontrivial, and the matrix coefficients and the inverse determinant generate the full group algebra. Therefore the pullback on every field fibre is surjective. Weight projections commute with base change, so $I_m+k(s)=k(s)$ at every prime. Locally some coefficient is consequently a unit, and $I_m=R$. This holds for all $m$, so $C\to R[M]$ is surjective. Descent proves the criterion for a nonsplit source. Thus the lifted monomorphism is a closed immersion, with no unproved embedding criterion remaining.

All the completed data, including the closed embedding and a splitting cover, involve finitely many generators and relations. Spread them to a finite-type algebra over the local model. Artin approximation gives a solution over an étale neighbourhood agreeing on the residue field. The embedding and torus structure are part of the spread data, so this is an embedded torus with the required special fibre. Finally descend the finite data from the noetherian model to the original base. This establishes (3) without a noetherian assumption on $S$. $\square$

**Why fpqc tori split étale locally.** Suppose $T/S$ is fpqc locally $\mathbf G_m^r$. Affine descent makes it affine, smooth and of finite presentation, with geometric fibres tori; its relative dimension is locally constant. A fibre torus splits over a finite separable extension, by the field character classification in [Diagonalizable groups and groups of multiplicative type](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-05.html). After making that residue extension, apply Lemma 3.1(3) with target $G=T$ and source the entire fibre torus. We obtain an embedded étale torus $T'\subset T$ near the point. Shrink so that both groups have the same relative dimension. On every geometric fibre the closed subtorus $T'$ now has the dimension of the connected torus $T$, so is the entire fibre. The inclusion between these smooth groups has invertible differential, and is an étale monomorphism, hence an open immersion. Fibrewise surjectivity makes it an isomorphism. Finally split $T'$ by its étale character cover. This proves the asserted equivalence of definitions, using the deformation lemma for a general smooth affine target, rather than presupposing the splitting assertion.

**Theorem 3.2.** A reductive group scheme admits maximal tori étale locally. Any two maximal tori are conjugate étale locally.

**Proof.** At a point $s$, choose a geometrically maximal torus after a finite separable extension of $k(s)$. The existence of such a torus follows either from Theorem 4.2 below, which gives one over $k(s)$ itself, or from smoothness of the torus-embedding functor; we use Theorem 4.2 to keep one route. Make the residue extension by an étale neighbourhood and apply Lemma 3.1.

In the reductive special fibre a maximal torus is its own centralizer. The proof of this assertion and its relative extension is given in [Regular elements and centralizers](AG-RG-02.md#2-centralizers-and-weight-zero); it uses the geometry of Borel quotients and does not use the present existence theorem or the root-space classification. The centralizer of the lifted torus is smooth. Near the chosen fibre its identity component has the same dimension as the torus: a smooth subgroup containing the identity section has locally constant relative dimension near that section. On these neighbouring fibres the torus has no larger torus in its centralizer, hence is maximal in $G$. This proves local existence.

For two maximal tori, their geometric fibres are conjugate by Theorem 2.2. The transporter is therefore a smooth surjection onto $S$ by Lemma 3.1. Every smooth surjective morphism admits sections étale locally; a section of this transporter is the desired conjugating element. $\square$

The statement is local around every point, and the conjugating element belongs to the group over the chosen neighbourhood. It does not assert a global section of the transporter.

## 4. A torus over the ground field

The finite-field and infinite-field arguments have quite different mechanisms. The first adjusts descent by Lang's theorem. The second finds a semisimple infinitesimal direction and uses dimension induction. The infinitesimal argument is essential over imperfect fields.

**Lang's theorem in the form needed here.** If $G/\mathbf F_q$ is smooth and connected and $F$ is its Frobenius, the map $g\mapsto g^{-1}F(g)$ is surjective on geometric points. Consider the action $g\cdot x=gxF(g)^{-1}$ on $G_{\overline{\mathbf F}_q}$. The differential of $F$ is zero. Hence the orbit map at every point has invertible differential, and is étale. All its orbits are therefore open. Distinct orbits would give disjoint nonempty open subsets partitioning the connected variety, so there is only one. The orbit of the identity proves the assertion, after inversion. The same argument for the standard $p$-power map of $\operatorname{GL}_n$ works over any algebraically closed field of characteristic $p$.

**Jordan components and the height-one construction.** We give the algebraic tools in the infinite-field proof, so that no classification theorem is hidden in its infinitesimal step. Multiplicative Jordan components of a point of a closed linear algebraic group remain in that group. In characteristic $p$, a large $p$-power kills its unipotent part; multiplication by that power is an automorphism on the reduced diagonalizable closure of the semisimple part's powers. The semisimple part therefore belongs to the closure of the powers of the original point, and so does its unipotent part. In characteristic zero, matrix entries of the powers are exponential polynomials $\lambda^m P(m)$. Distinct nonzero $\lambda$ give linearly independent such sequences, as repeated application of the difference operators $f(m)\mapsto f(m+1)-\lambda f(m)$ shows. Consequently every polynomial equation holding on the powers holds separately on their diagonalizable and unipotent factors. This again puts both factors in their algebraic closure. The construction is compatible with homomorphisms, by uniqueness of the two matrix components.

Additive Jordan components of the Lie algebra of a smooth affine group also remain in its Lie algebra after algebraic closure. In characteristic $p$, the Lie algebra is closed under $p$-th matrix powers. For a matrix $X$, choose $p^r$ large enough to kill its nilpotent part. A linearized polynomial recovers the semisimple part from $X^{p^r}$. To verify this interpolation, let $V$ be the $\mathbf F_p$-span of the eigenvalues raised to $p^r$. The map $\lambda^{p^r}\mapsto\lambda$ extends to an $\mathbf F_p$-linear map on $V$, because Frobenius preserves exactly the $\mathbf F_p$-linear relations. If $v_1,\ldots,v_d$ is a basis of $V$, the equations $\sum_{j=0}^{d-1}a_jv_i^{p^j}=\lambda_i$ have an invertible coefficient matrix: a nonzero linearized polynomial of degree at most $p^{d-1}$ cannot vanish on the $p^d$ elements of $V$. Its solution gives the desired polynomial. Thus the semisimple part is a linear combination of higher restricted powers of $X$, and its difference from $X$ is the nilpotent part. In characteristic zero, the formal exponential of $X$ lies in the group: a defining equation is annihilated by all powers of its invariant derivation and hence vanishes on the formal exponential. Its entries have the form $e^{\lambda t}P(t)$. Applying differential operators $d/dt-\lambda$ gives their independence for distinct $\lambda$ just as for the preceding sequences. The algebraic closure of this formal one-parameter subgroup contains the separate semisimple and nilpotent one-parameter factors. Their derivatives are the required Lie components. Rationality over a perfect field follows from the polynomial construction and uniqueness. The same argument, or uniqueness in the adjoint representation, gives the adjoint Jordan components used below.

For a smooth group in characteristic $p$, its first Frobenius kernel is encoded by the restricted Lie algebra $\mathfrak g$. Explicitly, its distribution algebra is

$$
u(\mathfrak g)=T(\mathfrak g)/(xy-yx-[x,y],\ x^p-x^{[p]}).
$$

For an ordered basis, the restricted PBW monomials with exponents $0,\ldots,p-1$ form a basis. Here is the argument in arbitrary characteristic. In the ordinary enveloping algebra, rewrite $x_jx_i$ for $j>i$ as $x_ix_j+[x_j,x_i]$. Degree followed by the number of inversions decreases. The only overlapping reductions are triples of basis elements; their difference is the Jacobi identity, so ordered monomials give unique normal forms. Put $z_i=x_i^p-x_i^{[p]}$. The identity $[x_i^p,y]=(\operatorname{ad}x_i)^p(y)=[x_i^{[p]},y]$ makes $z_i$ central. Products of the $z_i$ times ordered monomials with all exponents below $p$ have distinct leading PBW monomials; division of each exponent by $p$ proves that they form a basis of the ordinary enveloping algebra. Quotienting by all $z_i$ therefore leaves exactly the asserted restricted basis. The restricted identities ensure that these basis relations impose $x^p=x^{[p]}$ for every $x$, not just the chosen basis. Its dimension is $p^{\dim\mathfrak g}$. Local smooth coordinates at the identity show that the first Frobenius kernel has precisely this length; successive invariant differentiations pair these PBW monomials with its truncated coordinate monomials, with nonzero factorials of orders below $p$. Hence the natural map of distribution algebras is an isomorphism. A restricted subalgebra $\mathfrak h\subset\mathfrak g$ gives an injective Hopf map $u(\mathfrak h)\hookrightarrow u(\mathfrak g)$ and, by duality, an actual closed height-one subgroup of $G$. Thus both the positive-characteristic PBW assertion and its group correspondence have been supplied here.

If $\mathfrak h$ is commutative and its semilinear $p$-operation is geometrically invertible, it has, over an algebraic closure, a basis fixed by that operation. Indeed write the operation as $v\mapsto A v^{(p)}$ and apply the preceding Lang argument in $\operatorname{GL}_d$ to change its matrix to the identity. In that basis, $u(\mathfrak h)$ is the tensor product of the primitive Hopf algebras $k[x]/(x^p-x)$; the dual groups are $\mu_p$. Thus the subgroup is geometrically $\mu_p^d$. Its Cartier dual is finite étale, so it is of multiplicative type over the original field and splits over a finite separable extension. This proves exactly the infinitesimal multiplicative-type assertion required in the argument.

**Lemma 4.1.** If a smooth connected affine $k$-group has a nontrivial $k$-torus, and geometrically maximal tori exist for groups of smaller dimension, then it has a geometrically maximal $k$-torus.

**Proof.** Let $M$ be a nontrivial $k$-torus and put $C=C_G(M)^0$. Smoothness is Lemma 3.1, and taking the identity component makes $C$ geometrically connected without requiring the connectedness theorem for the full centralizer. The quotient $C/M$ is smooth connected affine and has smaller dimension. Affineness can be seen directly from the line detecting the normal subgroup $M$: since $M$ is central, it acts by the same scalar on the span of the translates of that line. The resulting representation in a projective linear group has kernel exactly $M$, so its closed affine image is the quotient. By induction it has a geometrically maximal torus $Q$. The inverse image $E$ of $Q$ is an extension of tori by tori, hence a torus: after an algebraic closure, the solvable structure theorem shows that its unipotent radical maps trivially to $Q$ and lies in $M$, so is trivial; it is a connected solvable reductive group, which is a torus.

Over an algebraic closure, a maximal torus of $G$ containing $M$ lies in $C$. Thus the maximal torus dimensions in $C$ and $G$ agree. A torus of $C$ properly containing $E$ would yield a torus of $C/M$ properly containing $Q$, a contradiction. Therefore $E$ is geometrically maximal in $G$. $\square$

**Theorem 4.2 (Grothendieck).** Every smooth connected affine group over a field $k$ has a geometrically maximal torus defined over $k$.

**Proof.** We use induction on dimension and give the imperfect-field step explicitly. The classical inputs about connected commutative groups and Lie algebras are specified at the end of the lesson.

If $G_{\bar k}$ has a central maximal torus, it is unique, since all maximal tori are conjugate. Let $Z$ be the scheme-theoretic centre. For every integer $n$ prime to the characteristic, $Z[n]$ is finite étale: the derivative of multiplication by $n$ is invertible, so its kernel has zero tangent space. Over $\bar k$, the reduced connected part of $Z$ is a product of a torus and a connected unipotent group. Prime-to-characteristic torsion detects exactly the torus part. The identity component of the closure of all these $Z[n]$ therefore descends the unique maximal torus. Closure and extension commute here after passing to a separable closure: the finite étale torsion schemes become actual rational points, and the closure of rational points is geometrically reduced. This also proves the same descent assertion for any torus part of the reduced connected centre, when it is merely nontrivial.

Suppose $k$ is infinite and $G_{\bar k}$ has a noncentral torus. We will find a nontrivial $k$-torus and then use Lemma 4.1. Choose a faithful representation and regard $\mathfrak g=\operatorname{Lie}(G)$ inside a matrix algebra. Semisimple and nilpotent mean the additive Jordan components in this representation; these components belong to $\mathfrak g_{\bar k}$ and are functorial in algebraic-group homomorphisms.

First assume that $\mathfrak g(k)$ contains a semisimple element $X$ with $\operatorname{ad}(X)\ne0$. In characteristic zero its stabilizer $C_G(X)$ is smooth, with Lie algebra the kernel of $\operatorname{ad}(X)$. It is a proper subgroup and its identity component contains the nonzero semisimple tangent vector $X$. A unipotent group's Lie algebra consists of nilpotent matrices, so this identity component is not unipotent. Dimension induction supplies a nontrivial $k$-torus in it.

In characteristic $p>0$, a version of the same argument avoids smoothness questions for a Lie-element stabilizer. Put

$$
\mathfrak h=\operatorname{span}_k\{X,X^{[p]},X^{[p^2]},\ldots\}.
$$

This is a commutative restricted Lie subalgebra; its elements are commuting semisimple matrices, and its $p$-operation has no kernel after extending to $\bar k$. The equivalence between restricted Lie algebras and finite height-one group schemes turns it into a subgroup $H\subset\ker(F_{G/k})$ of multiplicative type. Indeed, over an algebraically closed field an invertible Frobenius-semilinear operation has a basis fixed by it, and each such line corresponds to $\mu_p$, rather than $\alpha_p$. Thus $H_{\bar k}\simeq\mu_p^d$ with $d>0$.

The centralizer $C_G(H)$ is smooth by the same invariant-cohomology argument as Lemma 3.1, which applies to all finite groups of multiplicative type. It is proper because the adjoint action on $\mathfrak h$ is not trivial. Its identity component contains $H$ and cannot be unipotent, since a smooth unipotent group cannot contain $\mu_p$. Dimension induction again gives a nontrivial $k$-torus.

It remains to find a usable semisimple direction or to remove the central directions that obstruct this method. Choose a noncentral $\mathbf G_m\subset G_{\bar k}$. Its adjoint action on $\mathfrak g_{\bar k}$ has a nonzero weight, since otherwise its smooth centralizer would have dimension $\dim G$. In characteristic zero its Lie generator has a nonzero eigenvalue under $\operatorname{ad}$. Consequently the characteristic polynomial of $\operatorname{ad}(Y)$ is not identically $t^{\dim G}$ as $Y$ varies in $\mathfrak g$. Since $k$ is infinite, some $Y\in\mathfrak g(k)$ also has this property. Its semisimple component is rational over the perfect field $k$ and has nonzero adjoint action. This is the situation just treated.

In characteristic $p$, the same conclusion about a noncentral Lie generator can fail: all weights may have zero differential. If there is any semisimple rational vector with nonzero adjoint action, we are already done. Otherwise all semisimple rational vectors are central in $\mathfrak g$. There is still a nonzero semisimple rational vector. A noncentral torus ensures that the Lie algebra is not a Lie algebra of nilpotent matrices. Hence some coefficient of the characteristic polynomial of the universal matrix $Y\in\mathfrak g$ is nonzero. Choose a rational $Y$ at which it is nonzero. Its semisimple part is nonzero and is defined over the perfect closure of $k$. For sufficiently large $r$, the matrix $Y^{p^r}$ kills the nilpotent part and brings all coefficients of the semisimple part back into $k$. It lies in $\mathfrak g(k)$ by the restricted operation and is the required vector.

Choose one nonzero semisimple rational vector $X$. It is central in $\mathfrak g$ by the case assumption, and so are all its restricted powers, since $\operatorname{ad}(X^{[p]})=(\operatorname{ad}X)^p$. Their span is a nonzero commutative restricted subalgebra with geometrically injective $p$-operation. Its height-one subgroup $M$ is of multiplicative type. Its centralizer is smooth by exactness of multiplicative-type invariants, and has the whole Lie algebra $\mathfrak g$: centralizing $M$ is equivalent to acting trivially on its distribution algebra, generated by this central subalgebra. Thus $C_G(M)$ has dimension $\dim G$. Connectedness of $G$ makes this centralizer all of $G$, so $M$ is central. No assertion about descent of the span of all semisimple vectors is needed.

Pass to $G/M$ and repeat if all its rational semisimple tangent vectors are central. The composite kernels remain central multiplicative infinitesimal groups. To check this assertion, an extension of two finite connected multiplicative-type groups has trivial conjugation action on the kernel. Its commutator is a bilinear map from the quotient to the kernel, hence a map to their étale Hom scheme; connectedness makes it zero. Cartier duality then makes the commutative extension multiplicative type.

If this procedure continues indefinitely, its strictly increasing kernels lie in $Z(G)$ and have unbounded orders. The finite infinitesimal quotient of $(Z(G)_{\bar k})^0$ by its reduced connected subgroup cannot absorb those orders. The reduced connected centre must therefore contain a nontrivial multiplicative infinitesimal group. Its unipotent factor cannot contain one, so its torus factor is nontrivial. Prime-to-$p$ torsion, as in the first paragraph, descends a nontrivial $k$-torus.

If the procedure stops, a quotient $G/M$ has a noncentral semisimple rational tangent vector and hence a nontrivial $k$-torus $Q$ by the earlier argument. Its inverse image $E$ in $G$ is a central extension of $Q$ by a finite multiplicative infinitesimal group. Its commutator descends to $Q\times Q\to M$, which is trivial because $Q\times Q$ is smooth and $M$ is infinitesimal. Thus $E$ is commutative. The reduced connected group $E_{\bar k,\mathrm{red}}$ maps onto $Q_{\bar k}$ with no unipotent part, so it is a nontrivial torus. Again prime-to-$p$ torsion descends this torus to $k$. This finishes the infinite-field induction.

Finally let $k=\mathbb F_q$, with Frobenius $F$. Over $\bar k$, choose a pair $(B,T)$ of a Borel subgroup and its maximal torus. Theorem 2.2 and Lemma 2.1 show that Borel–torus pairs are conjugate. Write $F(B,T)=g(B,T)g^{-1}$. Lang's theorem gives $h\in G(\bar k)$ with $h^{-1}F(h)=g^{-1}$. Then

$$
F(h(B,T)h^{-1})=h(B,T)h^{-1}.
$$

Galois descent therefore gives a Borel subgroup and a geometrically maximal torus over $k$. This closes the induction in every characteristic and over every field. $\square$

The infinitesimal step is needed because a noncentral group torus may have a central Lie algebra. In $\operatorname{SL}_2$ in characteristic two, the Lie algebra of the diagonal torus consists of scalar matrices. The torus itself still acts nontrivially on the upper and lower root groups.

## 5. The finite symmetry left after centralizing

For a maximal torus in a reductive group scheme, define the fppf quotient

$$
W_G(T)=N_G(T)/T.
$$

The quotient has group structure because $T$ is normal in its normalizer. It acts on $T$, and thus on both character and cocharacter sheaves.

**Theorem 5.1.** $W_G(T)$ is represented by a finite étale group scheme over $S$.

**Proof.** In this reductive case $C_G(T)=T$, as proved in the next lesson without using this theorem. Conjugation gives a map from $N_G(T)$ to the étale automorphism sheaf of $T$, with kernel $T$. The quotient is a separated étale algebraic space of finite presentation: the normalizer is smooth, and its relative Lie algebra modulo that of $T$ is zero by infinitesimal rigidity of torus automorphisms. Equivalently, one can use the quotient construction in Conrad, Theorem 2.3.1.

It remains to prove finiteness; finite geometric fibres alone would not suffice. Étale locally split $T$. The weights of its action on $\operatorname{Lie}(G)$ form a fixed finite collection of characters on a neighbourhood, since their summands are vector bundles and their ranks are locally constant. The nonzero weights are the roots of the geometric fibres. Consequently the isomorphism type of the fibre root system is locally constant. Its Weyl group, hence the number of geometric points of $W_G(T)$, is locally constant. The classical identification of this group with the reflection group is proved in [Root data, Weyl chambers and the Bruhat decomposition](AG-RG-04.md#4-borel-subgroups-are-positive-systems), independently of the present finiteness argument.

A separated étale algebraic space of finite presentation with locally constant finite fibre cardinality is finite étale. Indeed, over a strictly henselian local base, each point of the closed fibre has an open neighbourhood mapping isomorphically to the base. Separatedness makes these neighbourhoods disjoint; their number already equals the cardinality of every fibre. There are therefore no remaining points. This is a disjoint union of finitely many copies of the base, and finiteness descends. $\square$

**Example 5.2.** For $\operatorname{GL}_n$ and its diagonal torus, a normalizing matrix permutes the universal weight lines. Locally on the base it is a permutation matrix times an invertible diagonal matrix. Conversely every such matrix normalizes the torus. Hence

$$
N_{\operatorname{GL}_n}(D)=D\rtimes(\mathfrak S_n)_S,\qquad
W_{\operatorname{GL}_n}(D)=(\mathfrak S_n)_S.
$$

The permutation is locally constant; over a disconnected algebra it need not be a single global permutation.

## 6. Exercises and solutions

**Exercise 6.1 (first steps).** Over an arbitrary scheme, compute the centralizer and normalizer of the diagonal torus of $\operatorname{GL}_3$. Explain how the answer changes when the test algebra is disconnected.

**Solution.** The universal Laurent-polynomial computation in Example 1.1 makes the centralizer diagonal. A normalizer induces a permutation of the three rank-one character summands in the standard representation. After a decomposition by idempotents, the permutation is fixed on each piece. The normalizer is therefore $D\rtimes(\mathfrak S_3)_S$, with quotient the constant finite étale group $\mathfrak S_3$. Disconnected test algebras allow different permutations on different open and closed pieces, exactly as sections of a constant étale scheme do.

**Exercise 6.2 (descent).** Show that the two real tori in Example 1.2 are conjugate over $\mathbb C$ but not over $\mathbb R$. Show also that the multiplication torus $\operatorname{Res}_{\mathbb C/\mathbb R}\mathbf G_m$ in $\operatorname{GL}_{2,\mathbb R}$ is maximal and nonsplit.

**Solution.** The eigenvectors $(1,-i)$ and $(1,i)$ diagonalize the rotation matrix, with eigenvalues $a+bi$ and $a-bi$. On the norm-one subgroup these are inverse, so the eigenbasis carries it to the diagonal torus of $\operatorname{SL}_2$. Rescale a column to obtain a determinant-one change of basis. Conjugation on its character lattice is $m\mapsto-m$, whereas the diagonal real torus has trivial action, which rules out a real conjugation. For the multiplication torus, the two eigenvalues vary independently after complex base change; it becomes the full diagonal torus of $\operatorname{GL}_2$. It is therefore maximal. Its two character generators are exchanged by conjugation, so it is nonsplit over $\mathbb R$.

**Exercise 6.3 (finite fields).** For a smooth connected affine group over $\mathbb F_q$, construct a Borel–torus pair over $\mathbb F_q$ from one over $\overline{\mathbb F}_q$. The only cohomological input permitted is Lang's theorem.

**Solution.** Frobenius carries the chosen pair to a conjugate pair, so choose $g$ with $F(B,T)=g(B,T)g^{-1}$. Solve $h^{-1}F(h)=g^{-1}$ by Lang. Then $F(hBh^{-1})=hBh^{-1}$ and $F(hTh^{-1})=hTh^{-1}$. Their defining ideals descend by Galois descent. Their geometric fibres are the original Borel and maximal torus up to conjugation, so the descended pair has the required properties. Connectedness of $G$ is a condition of Lang's theorem and cannot be removed from this argument.

**Exercise 6.4 (a family).** Over $\mathbb Z$, let $D$ be the diagonal torus in $\operatorname{SL}_2$. Show that its nontrivial Weyl element is represented by $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ even in characteristic two, and explain why the quotient is étale there.

**Solution.** Conjugation by the displayed matrix sends $\operatorname{diag}(t,t^{-1})$ to $\operatorname{diag}(t^{-1},t)$. A normalizer permutes the two universal weight lines, giving two components, each a coset of $D$. Its quotient is the constant scheme with two points over $\mathbb Z$, not $\mu_2$. In characteristic two $\mu_2$ is nonreduced, whereas a constant two-point scheme is still the disjoint union of two copies of the field and remains étale. The representative squares to $-I\in D$; it need not itself have order two before taking the quotient.

## Exact supporting prerequisites and proof order

The classical triangularization, fixed-point, stabilizer, solvable structure and conjugacy arguments are in Section 2. Section 3 proves formal multiplicative-type homomorphism effectivity and the closed-immersion criterion. Section 4 proves Lang's theorem and supplies the Jordan and restricted-Lie arguments used in the field existence theorem. Their historical sources remain credited below.

The genuine internal geometric prerequisites are the supporting lessons [Group schemes over a field](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-03.html), for orbit representability and the closed-orbit lemma; [Quotients and torsors](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-04.html), for finite free-action quotients; Faithfully flat descent, for affine schemes, representations and character descent; [Diagonalizable groups and groups of multiplicative type](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/AG-GS-05.html), for the field character classification; Limits of schemes and Noetherian approximation, for finite-presentation spreading; Artin's axioms, for Artin approximation over local rings essentially of finite type over $\mathbb Z$; and *Dualizing sheaves and Serre duality for projective schemes*, for duality of curves. These are precise supporting dependencies, not claims that those other courses have already completed their proofs. The tori and reductive-group theorems assigned to this lesson are proved here.

The reductive centralizer equality and the reflection description used here are proved in the linked later lessons. Neither of those proofs uses the local existence or finiteness conclusion established from them here.

The course prerequisite guide records the exact supporting statements and which lessons are published or still planned.

## References

- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), in *Autour des schémas en groupes*, Panoramas et Synthèses 42–43, Société Mathématique de France, 2014: §§2.1–2.3 and 3.2, Appendix A and §§B.2–B.3.
- M. Demazure and A. Grothendieck, with the SGA 3 contributors, [*Schémas en groupes*](https://webusers.imj-prg.fr/~patrick.polo/SGA3/), re-edited by P. Gille and P. Polo: Exposés III, VII A, IX–X, XII and XIV.
- J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition, 2022: Chapters 16–17, especially §§17a–b, 17d, 17j–k. [Author's edition](https://www.jmilne.org/math/Books/iAG2022.pdf).
