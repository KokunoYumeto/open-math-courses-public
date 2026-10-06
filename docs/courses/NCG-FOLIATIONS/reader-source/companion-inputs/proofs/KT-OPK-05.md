# Matrix stability, stability and continuity of \(K_0\)

*Public domain (CC0).*
K-theory permits finite matrix enlargement in its definition. This makes the corner map into a matrix algebra invertible on \(K_0\). Passing from finite matrices to compact-operator stabilization also preserves the group, but that step requires a continuity theorem. We will prove continuity by realizing a finite number of relations at a sufficiently late stage of an inductive system.

We assume [Nonunital algebras: unitization, relative classes and half-exactness](KT-OPK-04.md), together with the matrix and group-completion results in [The Grothendieck group and \(K_0\) of a unital algebra](KT-OPK-03.md). We use the construction of C*-inductive limits and the density results of *AF-algebras*, §4 and Proposition 7.3. Every unitization below is external, even for an algebra already having an identity. The scalar map is \(\epsilon_A:A^+\to\mathbb C\).

## 1. Corners and the nonunital scalar quotient

Write \(j_n:A\to M_n(A)\) for \(a\mapsto a\otimes e_{11}\). The identity \((M_n(A))^+=M_n(A^+)\) is generally false: the scalar quotient on the left is \(\mathbb C\), while the quotient of the matrix algebra on the right by \(M_n(A)\) is \(M_n(\mathbb C)\). We use the latter extension to compare the two groups.

**Theorem 1.1 (matrix stability).** For every complex Banach algebra \(A\), every \(n\geq1\), and hence every C*-algebra, the corner homomorphism induces an isomorphism

\[
(j_n)_*:K_0(A)\longrightarrow K_0(M_n(A)).
\]

*Proof.* The scalar extensions

\[
\begin{gathered}
0\to A\to A^+\xrightarrow{\epsilon_A}\mathbb C\to0,\\
0\to M_n(A)\to M_n(A^+)\\
\xrightarrow{M_n(\epsilon_A)}M_n(\mathbb C)\to0.
\end{gathered}
\]

split by scalar inclusion. The preceding lesson therefore gives short exact sequences on \(K_0\). The corner maps between these sequences commute with inclusion and quotient. On their middle groups, the unital matrix-stability theorem of the third lesson gives

\[
K_0(A^+)\cong K_0(M_n(A^+));
\]

on the quotient groups it gives \(K_0(\mathbb C)\cong K_0(M_n(\mathbb C))\). Both maps are induced by the corner, which need not preserve identities. Consequently the middle isomorphism identifies the two kernels. Indeed it sends a kernel element into the second kernel by commutativity, and its inverse sends a second-kernel element into the first because the quotient corner is injective. Injectivity of the ideal maps in the split sequences identifies these kernels with \(K_0(A)\) and \(K_0(M_n(A))\). The resulting isomorphism is \((j_n)_*\), by the commutative ideal-inclusion square. \(\square\)

Here is its inverse on representatives. Take a normal form

\[
\begin{gathered}
x=[E]-[P_k]\in K_0(M_n(A)),\\
E\in M_l((M_n(A))^+),\quad\epsilon(E)=P_k.
\end{gathered}
\]

where \(P_k\) has \(k\) ones. Map each entry \(b+\lambda1\) to \(b+\lambda1_n\in M_n(A^+)\), then flatten the \(n\)-by-\(n\) blocks. If the resulting matrix is \(\widehat E\), the inverse is

\[
\begin{gathered}
x\longmapsto[\widehat E]-[P_k\otimes1_n]\\
\text{in }K_0(A).
\end{gathered}
\tag{1.1}
\]

Its scalar rank is zero. The unital flattening inverse and the two kernel identifications in the proof establish well-definedness and both inverse identities. In particular, this formula does not replace an arbitrary nonunital \(K_0\)-class by a difference of projections lying in the algebra.

Under the rank-one identification \(K_0(M_n(\mathbb C))=\mathbb Z\), the corner sends a rank-one class to a rank-one class, so it is the identity on \(\mathbb Z\). A unital multiplicity-\(n\) embedding of \(\mathbb C\) into \(M_n(\mathbb C)\) instead sends 1 to \(n\). Which homomorphism is used matters.

## 2. How a relation reaches a finite stage

Let \((A_i,\phi_{j,i})\), \(i\leq j\), be a sequential C*-inductive system. Write \(A=\varinjlim A_i\) and \(\phi_{\infty,i}:A_i\to A\). The construction in *AF-algebras*, §4, allows arbitrary *-homomorphisms and gives

\[
\|\phi_{\infty,i}(a)\|
=\lim_{j\to\infty}\|\phi_{j,i}(a)\|,
\tag{2.1}
\]

after quotienting the algebraic limit by the elements of seminorm zero and completing. Images of the stages have dense union. The same statements apply entrywise to finite matrices. In particular, an equation that holds in the limit need not hold at the first stage containing its entries. Equation (2.1) says its error can be made arbitrarily small at a later stage.

We also state the Banach version precisely. A normed inductive system of local Banach algebras has bounded connecting homomorphisms with

\[
\limsup_{j\to\infty}\|\phi_{j,i}\|<\infty\quad\hbox{for each }i.
\tag{2.2}
\]

A local Banach algebra is a normed algebra for which holomorphic functional calculus in its completion returns to the algebra, in every finite matrix size; in the nonunital case functions returning to the algebra have value zero at 0. Its normed limit is the algebraic limit modulo the zero set of the seminorm \(\limsup_j\|\phi_{j,i}(a)\|\); the Banach limit is its completion. For finite matrices in the Banach argument we may use the sum of the entry norms, so an eventual bound for a connecting homomorphism also bounds its matrix amplification. All the finite-relation arguments below work for such systems as well. Fixed elements and fixed finite matrices have eventually bounded norms. Small limit errors yield eventually small stage errors by the definition of limsup. C*-systems automatically satisfy (2.2).

**Lemma 2.1 (eventual inversion).** In a unital normed inductive system with unital connecting maps, if a stage element has invertible image in the completed limit, then its image is invertible at every sufficiently late stage.

*Proof.* Let \(a\in A_i\), and approximate the inverse of its limit image by the image of some \(b\in A_k\), with \(k\geq i\). Make both product errors in the limit smaller than \(1/4\). At a sufficiently late common stage \(j\), both

\[
\begin{gathered}
\|\phi_{j,i}(a)\phi_{j,k}(b)-1\|<1/2,\\
\|\phi_{j,k}(b)\phi_{j,i}(a)-1\|<1/2.
\end{gathered}
\]

Neumann inversion in the completion makes the first and second products invertible. The inverses belong to the local Banach algebra by inverse-closedness. The first equation supplies a right inverse of \(\phi_{j,i}(a)\), and the second supplies a left inverse. A left and a right inverse agree, giving invertibility. Its inverse is carried to an inverse at every later stage. Matrix sizes obey the same argument. \(\square\)

**Lemma 2.2 (functional calculus in the normed limit).** The normed, possibly incomplete, limit of a system satisfying (2.2) is a local Banach algebra.

*Proof.* Unitize to treat the unital case. Let \(a\) be a stage representative of a normed-limit element \(x\), and let \(f\) be holomorphic on a neighborhood of its spectrum in the completed limit. Choose a bounded open neighborhood \(U\) of that spectrum contained in the domain of \(f\). Choose a closed disc \(D\) of radius larger than the eventual bound on the norms of the stage images of \(a\), and containing \(U\).

For every \(\lambda\in D\setminus U\), the element \(\lambda-x\) is invertible. Lemma 2.1 makes \(\lambda-\phi_{j,i}(a)\) invertible at some late stage. Inversion is open there, so this holds on a neighborhood of \(\lambda\); the same neighborhood remains in the resolvent at later stages because unital homomorphisms preserve inverses. Compactness of \(D\setminus U\) gives a finite cover and one common late stage. Outside \(D\), the eventual norm bound gives resolvents by a Neumann series. Thus this stage image has spectrum in \(U\). Functional calculus there produces \(f(\phi_{j,i}(a))\), whose image is \(f(x)\) by naturality of the contour calculus. This belongs to the normed limit. If \(f(0)=0\), it belongs to the nonunital algebra rather than just its unitization. Apply the argument to every matrix size, where (2.2) still gives eventual bounds. \(\square\)

This lemma explains the role of the local Banach hypothesis. Merely choosing a dense subalgebra does not guarantee that a corrected approximate idempotent belongs to it.

**Lemma 2.3 (idempotents and equivalence at a late stage).** For a C*-system, and more generally a normed system of local Banach algebras, the natural map

\[
\varinjlim V_{\mathrm{id}}(A_i)\longrightarrow V_{\mathrm{id}}(A)
\]

is an isomorphism of monoids. In the C*-case this is equally an isomorphism for projection classes.

*Proof of surjectivity.* Let \(e\in M_m(A)\) be idempotent. Approximate it by \(\phi_{\infty,i}(a)\), with \(a\in M_m(A_i)\). For a sufficiently good approximation, its residual from being idempotent is small in the limit. Carry \(a\) to a later stage where \(\|a_j^2-a_j\|<1/4\), using (2.1) or the limsup construction. The spectral correction of the first lesson produces an exact idempotent \(e_j=\chi(a_j)\) in that stage. Its image is \(\chi(\phi_{\infty,i}(a))\).

As the original approximation tends to \(e\), this image tends to \(e\): the correction is continuous near an idempotent, with the explicit first-lesson residual estimate also giving convergence. Choose it within the close-idempotent equivalence radius of \(e\). Then it represents the class of \(e\). The correction satisfies \(\chi(0)=0\), so in a nonunital stage it belongs to the stage algebra. In a C*-system approximate a projection by a self-adjoint stage element, carry its residual forward, and take the self-adjoint cutoff. This gives a projection representative. Alternatively replace the lifted idempotent by its range projection. \(\square\)

*Proof of injectivity.* Put two stage idempotents \(e,f\) in a common stage and common finite matrix size, using zero padding and enlarging the size to include the equivalence witnesses. Suppose their limit images are algebraically equivalent. Normalize finite witnesses to the supported corners:

\[
\begin{gathered}
x\in e_\infty M_m(A)f_\infty,\\
y\in f_\infty M_m(A)e_\infty,\\
xy=e_\infty,\quad yx=f_\infty.
\end{gathered}
\]

Approximate \(x,y\) by stage images, and multiply their lifts by the exact stage idempotents on the two sides. At a later stage this gives supported \(X\in e_jM_m(A_j)f_j\), \(Y\in f_jM_m(A_j)e_j\) for which both \(XY-e_j\) and \(YX-f_j\) have norm less than \(1/2\). The limit errors can first be made arbitrarily small by the approximations; (2.1) or limsup then makes both stage errors small simultaneously.

Thus \(a=XY\) is invertible in the corner with identity \(e_j\), and \(b=YX\) is invertible in the corner with identity \(f_j\). One can verify this in the unitization: \(a+(1-e_j)\) and \(b+(1-f_j)\) differ from 1 by norms less than \(1/2\). Their inverses are in the stage by local inverse-closedness, and compression gives the corner inverses. Since \(bY=Ya\), multiplying by the two inverses gives \(b^{-1}Y=Ya^{-1}\). Define \(Y'=Ya^{-1}\). Then

\[
XY'=aa^{-1}=e_j,\qquad
Y'X=b^{-1}YX=f_j.
\]

The corrected witnesses prove stage equivalence. Zero corners cause no difficulty: the corresponding supported witnesses are zero and the same unitization formulas apply. This proves that every equality of limit monoid classes already holds at a late stage, which is injectivity of the algebraic monoid limit. Addition is respected by block sums. In C*-algebras the verified projection–idempotent monoid isomorphisms are natural, giving the projection version. \(\square\)

For an increasing union of C*-subalgebras, the projection approximation part specializes to the previously proved *AF-algebras*, Proposition 7.3. The additional stage-error argument above handles kernels of connecting maps. It does not assume that the stages are finite-dimensional or that their maps are injective.

## 3. Group completion and scalar kernels commute with the limit

**Lemma 3.1.** Group completion commutes with sequential direct limits of commutative monoids.

*Proof.* Every element of the group completion of a monoid limit is a difference of two monoid elements. Place representatives of both in a common stage; their difference comes from that stage group. If a stage difference becomes zero, the group-completion criterion gives a limit monoid element \(c\) such that \(a+c=b+c\). Represent \(c\) at a common later stage. Equality in the monoid direct limit holds at a further stage, where \(a+c=b+c\) is a group-completion witness that the stage difference is zero. The same argument applied to the difference of two elements proves injectivity. The sum agrees because both constructions use addition of representatives. \(\square\)

**Lemma 3.2.** External unitization commutes with a C*-inductive limit, including nonunital and noninjective connecting maps:

\[
\varinjlim(A_i^+,\phi_{j,i}^+)\cong A^+.
\]

*Proof.* The compatible extensions \(\phi_{\infty,i}^+\) induce a *-homomorphism from the left side to \(A^+\). Its image contains a dense union of the stage images of \(A_i\) and the new scalar unit. A C*-homomorphism has closed range, so it is onto.

For injectivity, on a stage element \(a+\lambda1\) its scalar coordinate is preserved at every stage and by the target map. If the image in \(A^+\) is zero, then \(\lambda=0\). The norm of this element in the unitized limit is therefore the limit of the norms of \(\phi_{j,i}(a)\), which is zero by (2.1). Hence the target map is injective on each stage image in the unitized limit. Each such image is a C*-algebra, and an injective C*-homomorphism is isometric. The map is consequently isometric on their dense union and, by continuity, on the whole limit. It is injective. The closed-range and isometry facts are proved in *C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, Corollaries 4.6 and 15.4. \(\square\)

For Banach systems satisfying (2.2), use the norm \(\|a+\lambda1\|=\|a\|+|\lambda|\). The defining limsup seminorm is then \(\limsup_j\|\phi_{j,i}(a)\|+|\lambda|\). Quotient and completion give the same unitization identification. In particular the extended system still satisfies the eventual boundedness condition.

**Theorem 3.3 (continuity).** For any sequential C*-inductive system with arbitrary *-homomorphisms, the canonical map is an isomorphism

\[
\varinjlim K_0(A_i)\ \cong\ K_0(A).
\]

Moreover, with \(K_0(A)^+\) defined as the image of \(V(A)\),

\[
K_0(A)^+=\bigcup_i(\phi_{\infty,i})_*K_0(A_i)^+.
\tag{3.1}
\]

The group-continuity assertion also holds for normed systems of local Banach algebras satisfying (2.2), with the completed or the normed limit.

*Proof.* Apply Lemmas 2.3 and 3.1 to the unitized system. They give continuity of the unital group-completion groups. Lemma 3.2 identifies the target with \(K_0(A^+)\).

Every class in its augmentation kernel comes from some \(K_0(A_i^+)\). The augmentation integer of that representative is the same at every stage and in the limit, because the extended homomorphisms fix the scalar quotient. Its integer must therefore already be zero at the representing stage. This proves surjectivity from \(\varinjlim K_0(A_i)\).

If a stage class in \(K_0(A_i)\) becomes zero, unital continuity makes it zero in \(K_0(A_j^+)\) at a later stage. Since \(K_0(A_j)\) is a subgroup of this group, it is zero there too. This proves injectivity. All maps are the originally specified maps by construction.

For (3.1), a positive class is represented by a projection in a finite matrix algebra over \(A\). Lemma 2.3 realizes its projection class at a stage, so its K-class is the image of a positive stage class. Conversely *-homomorphisms preserve projections and hence their positive classes. No cancellation or order-embedding assumption is needed. The local Banach argument is unchanged, using Lemma 2.2 to permit all functional-calculus corrections in the normed limit. \(\square\)

Thus the group completion \(G(V(A))\) itself also has continuity, even for nonunital limits. Its failure of half-exactness in the preceding lesson was a different property. Unitization is necessary for the correct ideal theory; it introduces no continuity obstruction here.

## 4. Compact-operator stabilization

Let \(A\) now be a C*-algebra and \(\mathcal K=\mathcal K(\ell^2(\mathbb N))\). Write \(P_n\) for the projection onto the first \(n\) basis vectors. Compactness implies \(\|k-P_nkP_n\|\to0\) for every \(k\in\mathcal K\): approximate \(k\) in norm by a finite-rank operator and use strong convergence of \(P_n\) uniformly on its finite-dimensional range and the range of its adjoint.

We need one estimate before completing the algebraic tensor product. A C*-seminorm means a submultiplicative seminorm with the C*-identity and an isometric involution; its completion after dividing by its null ideal is a C*-algebra. The positive square roots, norm monotonicity and contractive approximate identities used below are the complete proofs in [C*-algebras, Theorem 5.1, Proposition 8.5 and Corollary 11.5][CF].

**Lemma (the elementary-tensor estimate).** If \(A,B\) are arbitrary C*-algebras and \(\alpha\) is any C*-seminorm on \(A\odot B\), then

\[
\alpha(a\otimes b)\leq\|a\|\|b\|.
\tag{4.1}
\]

*Proof.* Let \(C\) be the completed quotient for \(\alpha\). For \(y=\sum_i a_i\otimes b_i\), define algebraically
\(L_a y=\sum_i aa_i\otimes b_i\). Put
\(c=(\|a\|^2 1-a^*a)^{1/2}\) in the C*-unitization of \(A\). Multiplication by \(c\) preserves \(A\), so \(L_c y\) is still an algebraic tensor, including when \(A\) has no identity. Expanding the finite sums gives

\[
\begin{gathered}
\|a\|^2 y^*y-(L_a y)^*(L_a y)\\
\qquad=(L_c y)^*(L_c y).
\end{gathered}
\tag{4.2}
\]

The right side is positive in \(C\). Norm monotonicity and the C*-identity therefore give
\(\alpha(L_a y)\leq\|a\|\alpha(y)\). In particular \(L_a\) preserves the null ideal and extends to a bounded operator on \(C\) of norm at most \(\|a\|\). Applying the same calculation to the second factor gives a commuting operator \(L_b\) of norm at most \(\|b\|\). On the dense algebraic tensors, \(L_aL_b\) is precisely left multiplication by the image of \(a\otimes b\).

Left multiplication by any \(x\in C\) has norm \(\|x\|\): submultiplicativity proves the upper bound, and a contractive approximate identity \(u_\lambda\) gives \(xu_\lambda\to x\), proving the lower bound. Thus
\(\alpha(a\otimes b)=\|L_aL_b\|\leq\|a\|\|b\|\), as required. If \(C=0\), the conclusion is immediate. No units or countability hypotheses were used. \(\square\)

The spatial norm exists for every pair \(A,B\), is faithful on their algebraic tensor product, and is independent of the faithful representations used to compute it. These are the complete [Hilbert-module tensor-product lesson, §5, opening lemma](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/hilbert-c-star-modules-and-morita-equivalence/tensor-products-and-c-star-correspondences.html#5-exterior-tensor-products-and-compact-operators). That proof constructs the Hilbert-space tensor norm and establishes the faithful-representation comparison; it uses no K-theory or stabilization theorem. This is our exact spatial-norm prerequisite.

For completeness the maximal norm can be constructed here as the supremum of all C*-seminorms on the algebraic tensor product. The lemma bounds that supremum on \(\sum_i a_i\otimes b_i\) by \(\sum_i\|a_i\|\|b_i\|\), so it is finite. Taking suprema preserves the triangle inequality, submultiplicativity, the involution and the C*-identity. The spatial norm is one of these seminorms and is definite, so the supremum is a norm. It dominates every other C*-tensor norm by construction. The historical tensor-norm reference is [Blackadar 2006, II.9.1–II.9.2].

We now apply this to \(B=\mathcal K\). In the completion for any C*-tensor norm, the inclusion of the algebra \(A\odot P_n\mathcal KP_n\cong M_n(A)\) is an injective *-homomorphism from the usual complete matrix C*-algebra. It is therefore isometric by the preceding C*-isometry prerequisite. Every C*-tensor norm consequently agrees on each finite corner. For \(x=\sum_{r=1}^s a_r\otimes k_r\), put \(x_n=\sum_r a_r\otimes P_nk_rP_n\). For every C*-tensor norm \(\alpha\),

\[
\|x-x_n\|_\alpha\leq\sum_{r=1}^s\|a_r\|\,
\|k_r-P_nk_rP_n\|\longrightarrow0.
\]

Since any two such norms agree on \(x_n\), they agree on \(x\) by this estimate. In particular the minimal and maximal norms agree: this proves nuclearity of \(\mathcal K\). It also proves that the increasing union of the corners \(M_n(A)\) is dense in \(A\otimes\mathcal K\). Thus the tensor product is their C*-inductive limit, for the spatial norm and equally for the maximal norm. The argument uses the cross-norm property and C*-isometry, and supplies the compact-operator case in full.

**Theorem 4.1 (stability).** The homomorphism \(a\mapsto a\otimes e_{11}\) induces

\[
K_0(A)\cong K_0(A\otimes\mathcal K).
\]

*Proof.* The tensor product is the inductive limit of \(M_n(A)\) under upper-left corner embeddings. Each connecting homomorphism induces an isomorphism on \(K_0\). Indeed if \(c_{m,n}:M_n(A)\to M_m(A)\), then \(c_{m,n}j_n=j_m\); both \((j_n)_*\) and \((j_m)_*\) are isomorphisms by Theorem 1.1, so \((c_{m,n})_*=(j_m)_*(j_n)_*^{-1}\). Under these identifications the group system is constant with value \(K_0(A)\). Theorem 3.3 identifies its limit with \(K_0(A\otimes\mathcal K)\), and the initial map is precisely the stated corner. \(\square\)

The same proof applies to a Banach completion of the finite matrix algebra whenever its corner system satisfies the normed-limit hypotheses above. The notation \(A\otimes\mathcal K\) without specifying a completion norm is used here for C*-algebras.

If \(p\) is a projection in a finite matrix algebra over \(A\otimes\mathcal K\), Lemma 2.3 gives an equivalent projection over some \(M_n(A)\). This describes its positive class under stability. It does not assert that every K-class is a single positive projection class. For example, the nonunital Bott class can require a difference of unitized projections even after its group is identified by stability.

For every locally compact Hausdorff space \(X\),

\[
K_0(C_0(X)\otimes\mathcal K)\cong K_0(C_0(X))=K_c^0(X).
\]

For \(A=\mathbb C\) we recover \(K_0(\mathcal K)=\mathbb Z\), with a rank-one generator as in the preceding lesson.

**Example 4.2.** A bijection \(\mathbb N\times\mathbb N\to\mathbb N\) determines a unitary \(W:\ell^2\otimes\ell^2\to\ell^2\). Conjugation by \(W\) gives

\[
\mathcal K\otimes\mathcal K\cong\mathcal K.
\]

To justify its range, elementary tensor rank-one operators are rank-one operators on tensor-product vectors; their finite spans are dense in the compact operators because algebraic tensor-product vectors are dense in the Hilbert tensor product. Under the rank-one generator identifications, this isomorphism induces the identity on \(\mathbb Z\): a tensor product of rank-one projections has rank one, and its unitary conjugate still has rank one. In particular the stabilization corner \(p\mapsto p\otimes e_{11}\) is consistent with that normalization.

## 5. Normalized ranks in UHF limits

For an integer \(d\geq2\), let \(A_d\) be the limit of \(M_{d^k}(\mathbb C)\), \(k\geq0\), with unital embeddings \(a\mapsto\operatorname{diag}(a,\ldots,a)\) having \(d\) copies. A rank-one generator at stage \(k\) goes to a rank-\(d\) projection, so its K-group system is

\[
\mathbb Z\xrightarrow{\times d}\mathbb Z
\xrightarrow{\times d}\mathbb Z\longrightarrow\cdots.
\]

**Proposition 5.1.** With its positive cone and unit,

\[
\begin{gathered}
(K_0(A_d),K_0(A_d)^+,[1])\\
\cong(\mathbb Z[1/d],\mathbb Z[1/d]_{\geq0},1).
\end{gathered}
\]

*Proof.* Send the integer \(r\) at stage \(k\) to \(r/d^k\). Compatibility is \(dr/d^{k+1}=r/d^k\). These images cover \(\mathbb Z[1/d]\). If two fractions agree, passing to a common denominator gives equality of the stage representatives; thus this is the group direct-limit isomorphism. Theorem 3.3 transfers it to \(K_0(A_d)\). Positive stage ranks give exactly the nonnegative fractions by (3.1). The stage identity has rank \(d^k\) and hence image 1. \(\square\)

For the CAR algebra, \(d=2\), this reproduces the dyadic group and normalization in *AF-algebras*, Example 5.3 and the UHF calculation in §6. For \(d=6\) the group is

\[
\mathbb Z[1/6]=\{a/(2^r3^s):a\in\mathbb Z,\ r,s\geq0\}.
\]

Every denominator on the right divides a sufficiently high power of 6, proving equality with the displayed localization. This includes nonnegative fractions as the cone and 1 as the unit. The calculation makes no classification claim about arbitrary inductive limits or arbitrary C*-algebras. The following product examples also distinguish direct-limit continuity from a statement about infinite products.

### Infinite products and the size of representatives

Continuity for a direct limit does not assert that K-theory commutes with an infinite product. A matrix over a product still has one finite size, common to every coordinate. The examples below isolate the resulting obstruction; compare [Willett–Yu, §2.7, “Direct products”]. All products here are C*-products: their elements are bounded families, with the supremum norm.

**Proposition 5.2 (scalar products).** For any index set \(I\), coordinate ranks identify

\[
\begin{gathered}
K_0(\ell^\infty(I))=\ell^\infty(I,\mathbb Z),\\
K_0(\ell^\infty(I))^+=\ell^\infty(I,\mathbb Z_{\geq0}),\\
[1]=(1)_{i\in I}.
\end{gathered}
\tag{5.1}
\]

In particular the coordinate map to \(\prod_I K_0(\mathbb C)=\mathbb Z^I\) is injective and has exactly the bounded integer families as its image.

*Proof.* A projection in \(M_n(\ell^\infty(I))\) is a family of projections \(p_i\in M_n(\mathbb C)\); its ranks lie between zero and \(n\). Two such families, padded to a common size, are equivalent exactly when their coordinate ranks agree. Necessity follows from a coordinate partial isometry. For sufficiency choose a partial isometry between the two ranges at each coordinate. Its norm is at most one, so the family belongs to that same matrix algebra and supplies the required equivalence. Every bounded nonnegative integer family is realized by diagonal projections in one sufficiently large matrix algebra. Thus the projection monoid is the monoid of bounded nonnegative integer families, with pointwise addition. It is cancellative. Its group completion consists exactly of their differences, namely the bounded integer families. This also proves the cone and unit statements. For an infinite \(I\), an unbounded integer family lies in the product of coordinate groups and has no representative in this K-group. \(\square\)

The stabilization of each coordinate changes this phenomenon. Let \(H\) be an infinite-dimensional Hilbert space and \(B=\prod_{i\in I}\mathcal K(H)\).

**Proposition 5.3 (products of compact-operator algebras).** Coordinate ranks give

\[
\begin{gathered}
K_0(B)\xrightarrow{\cong}\mathbb Z^I,\\
K_0(B)^+\xrightarrow{\cong}(\mathbb Z_{\geq0})^I.
\end{gathered}
\tag{5.2}
\]

There is no boundedness requirement on the ranks.

*Proof.* A projection in \(M_n(B)\) has finite rank at each coordinate, but these ranks may be arbitrarily large: an operator on the fixed infinite-dimensional space \(H^n\) can have any finite rank. Conversely every nonnegative integer family is represented already in \(B\), by choosing a finite-rank projection of the prescribed rank at each coordinate. All chosen projections have norm at most one. Coordinate partial isometries, again of norm at most one, show that the monoid of actual projection classes over \(B\) is \((\mathbb Z_{\geq0})^I\).

We must still check that group completion of these actual projections gives the *nonunital* K-group; this is false for general nonunital algebras. Here \(B\) has an approximate identity of projections. Indeed, for any finite set of elements and any positive error, choose at each coordinate a finite-dimensional subspace that approximates on both sides all their compact operators to that error. The coordinate projections form an element of \(B\). Ordering these choices by finite sets and errors gives the required approximate identity, uniformly in the supremum norm.

Here is the precise reduction. Let \(p\in M_n(B^+)\) be a projection and let its scalar projection be \(P\in M_n(\mathbb C)\). Take \(e\in B\) from that approximate identity, with \(E=\operatorname{diag}(e,\ldots,e)\), so that both \((1-E)(p-P)\) and \((p-P)(1-E)\) are as small as desired. Since \(E\) commutes with \(P\),

\[
r=EpE+(1-E)P
\tag{5.3}
\]

converges in norm to \(p\). Explicitly, putting \(x=p-P\), the difference is \(ExE-x\), whose norm is at most \(\|(1-E)x\|+\|x(1-E)\|\). The two summands in (5.3) are supported on orthogonal corners. Spectral correction at \(1/2\) therefore produces
\(p'=f+(1-E)P\), with \(f\) a projection in \(EM_n(B)E\); it is as close to \(p\) as desired. Lesson 1 identifies these close projections. Orthogonal addition, applied also to \(P=EP+(1-E)P\), gives

\[
[p]-[P]=[f]-[EP].
\tag{5.4}
\]

For a relative difference \([p]-[q]\), its two scalar projections have the same rank and hence the same scalar K-class; apply (5.4) to both terms. Every class of \(K_0(B)\) is consequently a difference of actual projections over \(B\). If its coordinate ranks vanish, those two actual projections are equivalent by the coordinate partial-isometry argument. Thus the coordinate map is injective. The arbitrary prescribed ranks above prove surjectivity and the cone assertion. The empty index set gives the zero algebra and zero group in both propositions. \(\square\)

The difference is a size issue, not a change in the norm of a projection. In the scalar product, a finite matrix size bounds every rank. In the product of compact-operator algebras, a rank may grow at each coordinate while every projection still has norm one. These examples explain why an infinite-product theorem needs a hypothesis such as the quasi-stability in Willett–Yu, Proposition 2.7.12.

## 6. Exercises with solutions

**Exercise 6.1 (basic).** Describe the inverse of the matrix-corner map on arbitrary nonunital K-classes, and test it on a projection lying inside the matrix algebra.

*Solution.* Use (1.1): insert the scalar part as \(\lambda1_n\) before flattening, and subtract the flattened scalar projection. The split-exact kernel diagram proves this is well defined and inverse to the corner. If \(E\) has entries in \(M_n(A)\), its scalar part is zero; its class maps to that of the ordinary flattened projection over \(A\). For a general relative class, the subtraction of \([P_k\otimes1_n]\) is essential. Sending a matrix-unitization scalar to just a first-corner scalar would be a different map and would not implement this inverse.

**Exercise 6.2 (basic).** Compute \(K_0\) for UHF type \(6^\infty\) and for the limit of \(M_{2^k}\) under \(a\mapsto\operatorname{diag}(a,0_{2^k})\). Specify the generator normalization in both cases.

*Solution.* The first answer is \(\mathbb Z[1/6]\), cone the nonnegative fractions, unit 1. A stage rank-one projection has value \(6^{-k}\). For the second system rank is unchanged, so the group maps are the identity on \(\mathbb Z\), and the limit group is \(\mathbb Z\) with its nonnegative cone. Its matrix corners form a dense union in \(\mathcal K(\ell^2)\), since any finite matrix is contained in a corner of size \(2^k\), and finite matrices are dense in the compact operators. The positive generator is a rank-one projection. The stage identities have classes \(2^k\), and their images do not define one fixed unit class: the limit algebra is nonunital. This is the difference between the multiplicity-two and zero-corner embeddings.

**Exercise 6.3 (intermediate).** Does \(G(V(\cdot))\) have continuity for these nonunital limits? Explain what the unitization changes.

*Solution.* Lemma 2.3 gives \(\varinjlim V(A_i)=V(A)\), and Lemma 3.1 gives \(\varinjlim G(V(A_i))=G(V(A))\). Thus continuity holds. This statement does not identify these groups with \(K_0\) in every nonunital algebra; the preceding lesson's \(C_0(\mathbb R^2)\) example distinguishes them. For \(K_0\), one instead uses the unitized systems. Their scalar augmentation group is the same \(\mathbb Z\) at every stage, and a zero augmentation in the limit is already a zero augmentation at the representing stage. The kernel argument of Theorem 3.3 shows exactly why unitization is harmless for continuity.

**Exercise 6.4 (intermediate).** Put \(A_k=M_{2^k}(C(S^1))\) and define the unital twice-around embeddings explicitly by

\[
\phi_{k+1,k}(f)(z)=\operatorname{diag}(f(z^2),f(z^2)).
\]

Given \(K_0(C(S^1))=\mathbb Z\), compute the limit group. Also determine the answer for \(f\mapsto\operatorname{diag}(f(z^2),0)\).

*Solution.* Every circle bundle is trivial, so the integer is fiber rank, including after matrix flattening. Pullback along \(z\mapsto z^2\) preserves fiber rank. Taking two diagonal copies multiplies it by two. Therefore the displayed unital system has group \(\mathbb Z[1/2]\), nonnegative cone, and unit 1; a stage rank-one projection has value \(2^{-k}\). If the second diagonal block is zero, rank is unchanged. The group system then has identity maps and the answer is \(\mathbb Z\), with the nonnegative cone and no distinguished limit identity. The degree-two map on the circle alone does not double \(K_0\); the multiplicity of the matrix embedding does. Specifying that multiplicity is necessary when stage matrix sizes change.

**Exercise 6.5 (advanced).** For unital C*-algebras and unital connecting homomorphisms, prove continuity of the triple consisting of \(K_0\), its positive cone and its distinguished unit class. Explain the order terminology when a cone is not proper.

*Solution.* Theorem 3.3 supplies the group isomorphism and equality of the cone with the union of the stage-cone images. Unitality carries every \([1_{A_i}]\) to every later \([1_{A_j}]\), and their common class goes to \([1_A]\). To verify the universal property, let compatible positive group homomorphisms from the stage groups into a group with a specified cone and unit be given, carrying the stage units to that unit. The group direct limit supplies a unique homomorphism. Each positive limit element comes from a positive stage element, so this homomorphism is positive, and the common stage-unit class proves it preserves the unit. This gives the claimed direct-limit triple.

The distinguished class is an order unit. For a unital algebra put \(u=[1]\). Write a general class as \(x=[p]-[1_m]\), with \(p\in M_l(A)\). The complementary projection gives \([p]+[1_l-p]=lu\), so \(0\leq[p]\leq lu\), and therefore \(-mu\leq x\leq(l-m)u\). Choosing an integer \(N\geq\max(m,l)\) gives \(-Nu\leq x\leq Nu\). This argument applies at the stages and in the unital limit, including when the cone defines only a preorder.

For complete generality, a specified cone defines a translation-invariant preorder \(x\leq y\) when \(y-x\) lies in the cone. Antisymmetry additionally requires the cone to meet its negative only at zero. K-theory's cone need not be proper for an arbitrary C*-algebra, so the universal statement uses these preordered groups with distinguished unit. If all stage cones are proper, the limit cone is proper: if both \(x\) and \(-x\) are positive, represent them by positive elements \(a,b\) at a common stage. Their sum is zero in the limit, hence zero at a later stage. There \(a+b=0\), so properness gives \(a=b=0\), and \(x=0\). Under this hypothesis the result is a direct limit of ordered groups with distinguished order unit in the usual sense. The UHF calculations satisfy it.

## Prerequisite and reference map

The construction and norm formula for C*-inductive limits are those of *AF-algebras*, §4, and [Blackadar 2006, II.8.2.1]. The injective-union projection approximation already appears in *AF-algebras*, Proposition 7.3. We have added the arbitrary-map realization argument and the precise normed Banach extension. The first lesson supplies the Riesz idempotent correction, local equivalence radius and projection–idempotent correspondence; the third supplies unital finite matrix flattening; the fourth supplies the scalar-kernel convention and split exactness.

Section 4 proves the elementary-tensor estimate for every C*-seminorm, constructs the maximal norm, and uses the exact written spatial-norm lemma in the Hilbert-module tensor-product lesson. It then proves nuclearity of \(\mathcal K\) and the realization of \(A\otimes\mathcal K\) by finite matrix corners. The continuity and stability of K-theory have been proved here. Ordered AF classification is not used in the UHF group computation.

## References

- Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §3.3, especially Lemma 3.3.1 and Theorem 3.3.2; §§4.5 and 5.2.4. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; author's revised 2017 text, II.8.2, II.9.2.2 and V.1.1.7–V.1.1.11.
- Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§1.7 and 8.2.
- *AF-algebras*, §4, Example 5.3, the UHF calculation in §6, and Proposition 7.3, in *Foundations of von Neumann algebras*.
- *C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, Corollaries 4.6 and 15.4, in the same foundations course.

[CF]: https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html

- **[Willett–Yu]** R. Willett and G. Yu, *Higher Index Theory*, author draft dated 9 December 2019, §2.7, Definition 2.7.11 and Proposition 2.7.12, printed pp. 94–95. [Freely available author draft](https://math.hawaii.edu/~rufus/higherindextheory#page=95). The full theorem concerns quasi-stable factors; Propositions 5.2–5.3 give independent complete proofs of the scalar obstruction and compact-operator case used here.

[Blackadar’s freely readable revised Operator Algebras](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
