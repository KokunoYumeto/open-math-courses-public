# Determinants and changes of basis

Determinants describe how a linear change of coordinates acts on an alternating volume. That viewpoint gives both a formula and a multiplication law, including when a matrix is singular. It also explains the determinant factor in a change of basis for a three-dimensional Lie bracket.

This lesson develops the determinant and cofactor material of Jim Hefferon's *Linear Algebra*, the text of the core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40), which hosts the book with its editable sources. Original text of this lesson: public domain (CC0).

*Source followed: Jim Hefferon. Text, ring-level proofs, coordinate-change applications, examples and solutions: OpenAI GPT-6 Astra in Codex, Ultra reasoning effort, October 2026. Self-checked by the writing AI. These are standard results.*

## Scalars, coordinates and finite permutations

Let \(R\) be a commutative ring with identity, and let \(n\ge0\). A vector in \(R^n\) is an ordered list of scalars; its coordinates give the expansion \(v=\sum_i v_i e_i\) in the standard basis. Matrix multiplication means \((AB)_{ij}=\sum_k A_{ik}B_{kj}\). Distributing the finite sums proves \((AB)C=A(BC)\), and the identity matrix acts as the identity. Transposing a product gives \((AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}\), because both \((i,j)\)-entries are \(\sum_k B_{ki}A_{jk}\). No scalar division is used here.

A permutation \(\sigma\) of \(\{1,\ldots,n\}\) has an **inversion** at \((i,j)\) when \(i<j\) but \(\sigma(i)>\sigma(j)\). Write \(N(\sigma)\) for their number and \(\operatorname{sgn}(\sigma)=(-1)^{N(\sigma)}\), initially an integer sign.

**Lemma 1 (signs).** Swapping two positions reverses the sign. Moreover

\[
\operatorname{sgn}(\sigma\tau)
=\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau),
\qquad
\operatorname{sgn}(\sigma^{-1})=\operatorname{sgn}(\sigma).
\]

**Proof.** For adjacent positions only the inversion between those positions changes: comparisons with any third position have the same total before and after. Thus the inversion count changes by one. Swapping positions \(i<j\) can be performed in \((j-i)+(j-i-1)\) adjacent swaps, an odd number, by moving the later entry up and the earlier one back down.

Every permutation is obtained from the identity by adjacent swaps. Indeed, if its list is not increasing there is an adjacent descent; exchanging that pair reduces the nonnegative inversion count by one. Iterating reaches the increasing list, and reversing the swaps constructs the permutation. If a chosen sequence of \(m\) position swaps produces \(\tau\), its sign is \((-1)^m\). Apply the same position swaps to the list \(\sigma(1),\ldots,\sigma(n)\); it becomes the list of \(\sigma\tau\). Its sign is therefore \((-1)^m\operatorname{sgn}(\sigma)\), proving the product formula. Applying it to \(\sigma\sigma^{-1}\) proves the inverse formula. \(\square\)

The signs are mapped from the integers into \(R\). In characteristic two the values \(1\) and \(-1\) coincide, but the cancellation of a term with its additive inverse remains valid.

## The determinant and alternating multilinearity

For \(A=(a_{ij})\in M_n(R)\), define

\[
\det A=\sum_{\sigma\in S_n}
\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i,\sigma(i)}.
\]

For \(n=0\) there is one empty permutation and the empty product is \(1\), so the determinant of the empty matrix is \(1\).

A function of \(n\) vectors is **multilinear** if it is linear in each argument with the others fixed. It is **alternating** if it is zero whenever two arguments agree.

**Theorem 2 (existence and normalization).** The determinant is alternating and multilinear in its rows and in its columns, and \(\det I_n=1\). Also \(\det A^{\mathsf T}=\det A\). It is the unique alternating multilinear function of the columns with value \(1\) on \((e_1,\ldots,e_n)\).

**Proof.** Every term of the defining sum contains exactly one entry from each row and from each column. Distributivity gives multilinearity. In the identity matrix only the identity permutation has a nonzero product.

If rows \(i,j\) coincide, pair \(\sigma\) with the permutation obtained by swapping its values at positions \(i,j\). There are no fixed permutations in this pairing, their products are equal, and Lemma 1 gives opposite signs. Thus each pair contributes zero, including in characteristic two. The argument for equal columns pairs permutations by swapping the corresponding values. This proves alternation without dividing by \(2\).

In the sum for \(\det A^{\mathsf T}\), the product is \(\prod_i a_{\sigma(i),i}\). Reindexing by \(j=\sigma(i)\) makes it \(\prod_j a_{j,\sigma^{-1}(j)}\). Lemma 1 and the bijection \(\sigma\mapsto\sigma^{-1}\) identify the entire sum with \(\det A\).

For uniqueness, let \(F\) be any alternating multilinear function. Alternation and expansion of \(F(\ldots,u+v,\ldots,u+v,\ldots)=0\) show that swapping two arguments changes its value by a minus sign. Expand each vector in standard coordinates:

\[
F(v_1,\ldots,v_n)
=\sum_{i_1,\ldots,i_n}
(v_1)_{i_1}\cdots(v_n)_{i_n}
F(e_{i_1},\ldots,e_{i_n}).
\]

Terms with repeated indices vanish. Every remaining index list is a permutation, and its value of \(F\) is its sign times \(F(e_1,\ldots,e_n)\). Reindexing by the inverse permutation, as above, gives

\[
F(v_1,\ldots,v_n)
=F(e_1,\ldots,e_n)\det(v_1\ \cdots\ v_n).
\]

This identity proves uniqueness and will also prove multiplication. For \(n=0\), a zero-argument function is a constant, and the same normalization determines it. \(\square\)

**Consequences.** Adding a multiple of one row to a different row preserves the determinant: multilinearity gives the original value plus a term with two equal rows. Swapping rows negates it, and scaling a row by \(c\) multiplies it by \(c\). The same statements hold for columns. None requires \(c\) to be a unit.

For an upper-triangular matrix the determinant is the product of its diagonal entries. A potentially nonzero term must have \(\sigma(i)\ge i\) for every \(i\). Since the two sides have equal sums over \(i\), all these inequalities must be equalities. The lower-triangular assertion follows by transposition.

## Multiplication and inverses

**Theorem 3 (multiplication).** For all \(A,B\in M_n(R)\), including singular matrices,

\[
\det(AB)=\det(A)\det(B).
\]

**Proof.** Regard \(F(v_1,\ldots,v_n)=\det(Av_1\ \cdots\ Av_n)\) as a function of columns. Linearity of \(A\) and Theorem 2 make it alternating multilinear. Its value on the standard basis is \(\det A\). Apply the last identity in Theorem 2 to the columns of \(B\), whose images are the columns of \(AB\). This proves the formula without dividing by either determinant. \(\square\)

If \(A\) has an inverse, this gives \(\det A\det A^{-1}=1\). Thus \(\det A\) is a unit, and \(\det A^{-1}=(\det A)^{-1}\). To prove the converse over rings, we next construct an inverse.

For \(n\ge1\), let \(A_{\widehat i,\widehat j}\) denote the matrix obtained by deleting row \(i\) and column \(j\), and put \(C_{ij}=(-1)^{i+j}\det A_{\widehat i,\widehat j}\).

**Theorem 4 (cofactors and the adjugate).** Expansion along any row or column gives

\[
\det A=\sum_j a_{ij}C_{ij}
       =\sum_i a_{ij}C_{ij}.
\]

The two sums use a fixed row \(i\) and a fixed column \(j\), respectively. With \(\operatorname{adj}(A)_{ij}=C_{ji}\),

\[
A\operatorname{adj}(A)=\operatorname{adj}(A)A=(\det A)I_n.
\]

Consequently \(A\) is invertible exactly when \(\det A\) is a unit of \(R\), and then \(A^{-1}=(\det A)^{-1}\operatorname{adj}(A)\).

**Proof.** Group the defining permutation sum according to the column selected in row \(i\). For \(i=j=n\), the coefficient of the selected entry is the determinant of the upper-left \((n-1)\)-square submatrix: permutations fixing \(n\) have exactly the inversions of their restrictions. For general \(i,j\), move row \(i\) and column \(j\) to the last positions by adjacent swaps. Their deletion leaves all the remaining rows and columns in their original relative order. The number of swaps is \((n-i)+(n-j)\), with parity \(i+j\). Hence the corresponding grouped sum is \(a_{ij}(-1)^{i+j}\det A_{\widehat i,\widehat j}\). This is a grouping of terms, not division or cancellation by \(a_{ij}\); it is valid over arbitrary \(R\). Summing gives the row expansion. Transposition gives the column expansion.

The \((i,j)\)-entry of \(A\operatorname{adj}(A)\) is \(\sum_k a_{ik}C_{jk}\). If \(i=j\), it is \(\det A\). Otherwise it is the expansion along row \(j\) of the matrix obtained by replacing that row with row \(i\). Its cofactors along row \(j\) are unchanged, while its determinant is zero because two rows coincide. This proves the first matrix identity. Applying it to \(A^{\mathsf T}\) and transposing, with \(\operatorname{adj}(A^{\mathsf T})=\operatorname{adj}(A)^{\mathsf T}\), proves the second. The latter adjugate identity follows directly by transposing each deleted submatrix and using Theorem 2. Multiplying by the inverse of the scalar \(\det A\) now constructs a two-sided matrix inverse. Necessity was proved after Theorem 3. \(\square\)

The empty matrix is already the identity of the endomorphisms of \(R^0\); it is invertible and its determinant is \(1\). For fields, units are exactly the nonzero elements. For rings, “nonzero” is insufficient: the one-by-one matrix \((2)\) over \(\mathbb Z\) has nonzero determinant but no integral inverse.

**Corollary 5 (bases over a field).** For a square matrix over a field, its columns form a basis exactly when its determinant is nonzero.

**Proof.** If its columns form a basis, the linear map sending them to the standard basis is a two-sided inverse. Conversely, an invertible linear map takes the standard basis to an independent spanning list: apply its inverse to a relation to prove independence, and apply the map to the standard expansion of the inverse image to prove spanning. Combine this with Theorem 4. A list of \(n\) independent vectors in \(k^n\) is a basis by the programme's finite-basis theorem. Thus dependence, noninvertibility and zero determinant are equivalent over a field. \(\square\)

## Coordinate changes for forms and brackets

**Proposition 6 (bilinear forms).** If a bilinear form has matrix \(F\) and new basis vectors are the columns of an invertible matrix \(P\), its new matrix is \(P^{\mathsf T}FP\). In particular,

\[
\det(P^{\mathsf T}FP)=(\det P)^2\det F.
\]

For an endomorphism with new matrix \(X'=P^{-1}XP\), the condition \(X^{\mathsf T}F+FX=0\) is equivalent to \((X')^{\mathsf T}(P^{\mathsf T}FP)+(P^{\mathsf T}FP)X'=0\).

**Proof.** Vectors with new coordinates \(u,v\) have old coordinates \(Pu,Pv\). Their pairing is \((Pu)^{\mathsf T}F(Pv)=u^{\mathsf T}P^{\mathsf T}FPv\). The determinant identity follows from Theorems 2 and 3. Substituting \(X'\) into the final expression gives \(P^{\mathsf T}(X^{\mathsf T}F+FX)P\). Since \(P\) and \(P^{\mathsf T}\) are invertible, it vanishes exactly when the old expression vanishes. \(\square\)

On \(R^3\), define the coordinate cross product by

\[
u\times v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1)^{\mathsf T}.
\]

The scalar pairing is \(u\cdot v=\sum_i u_i v_i\), without complex conjugation. Expanding the three-by-three determinant gives \((u\times v)\cdot w=\det(u\ v\ w)\).

**Proposition 7 (the bracket coordinate rule).** For an invertible three-by-three matrix \(P\),

\[
(Pu)\times(Pv)=(\det P)P^{-\mathsf T}(u\times v).
\]

If an alternating bilinear bracket on a free module of rank three is written \([u,v]=M(u\times v)\), its new coefficient matrix is

\[
M'=(\det P)P^{-1}MP^{-\mathsf T}.
\]

**Proof.** Pair the first proposed identity with \(Pw\). On the left the value is \(\det(Pu\ Pv\ Pw)=\det P\det(u\ v\ w)\) by Theorem 3. On the right it is \((\det P)(u\times v)^{\mathsf T}P^{-1}Pw\), the same scalar. Since \(P\) is onto and pairing with the standard vectors determines every coordinate, equality of all these pairings proves the vector identity. The new bracket in coordinates is \(P^{-1}[Pu,Pv]\); substitution gives the matrix formula. Every alternating bilinear bracket has this form, with columns \([e_2,e_3],[e_3,e_1],[e_1,e_2]\). Jacobi is not required for this coordinate identity. \(\square\)

For completeness, trace is also invariant under a change of basis: \(\operatorname{tr}(AB)=\sum_{i,j}a_{ij}b_{ji}=\operatorname{tr}(BA)\), so \(\operatorname{tr}(P^{-1}XP)=\operatorname{tr}(XPP^{-1})=\operatorname{tr}X\). This argument uses commutativity of the scalar ring.

## Examples and exercises

**Exercise 1.** For \(A=\begin{pmatrix}1&t\\0&1\end{pmatrix}\) and \(B=\begin{pmatrix}0&1\\s&0\end{pmatrix}\), compute \(AB\) and check the product law, without assuming \(s\) or \(t\) is invertible.

**Solution.** Their product is \(\begin{pmatrix}ts&1\\s&0\end{pmatrix}\). Its determinant is \(-s\), while \(\det A=1\) and \(\det B=-s\). Thus the identity includes \(s=0\) and zero divisors in \(R\).

**Exercise 2.** Show that the matrix \(\begin{pmatrix}1&1\\1&1\end{pmatrix}\) has determinant zero in characteristic two. Why is the equation \(d=-d\) alone insufficient in that characteristic?

**Solution.** The defining sum is \(1\cdot1-1\cdot1=0\). In characteristic two, every scalar satisfies \(d=-d\), including \(d=1\) in the field with two elements. Alternation therefore requires the cancellation argument in Theorem 2, not division by \(2\).

**Exercise 3.** In \(\mathbb Z/6\mathbb Z\), decide whether \(\operatorname{diag}(2,1)\) and \(\operatorname{diag}(5,1)\) are invertible. Give an inverse when there is one.

**Solution.** The determinant \(2\) is not a unit: its multiples are \(0,2,4\), never \(1\). Thus the first matrix is not invertible. Since \(5^2=1\) modulo \(6\), the second matrix is its own inverse. Both determinants are nonzero; only the second is a unit.

**Exercise 4.** Put \(P=\operatorname{diag}(a,b,c)\), where \(a,b,c\) are units. Verify Proposition 7 on \(u=e_1,v=e_2\). Explain why conjugation alone is not the change-of-basis rule for a bracket matrix.

**Solution.** The left side is \(ab e_3\). The right side is \(abc P^{-\mathsf T}e_3=ab e_3\). Brackets have two input vectors and one output: both inputs change before the output is expressed in the new basis. The determinant and inverse transpose record the induced action on the pair of alternating inputs. For instance, \(P=dI_3\) transforms \(M\) to \(dM\), whereas conjugation would leave \(M\) unchanged.

## Programme connections

The complete arguments above supply the coordinate changes and matrix inverses in [Lie algebras: definitions, examples and first constructions](../../courses/RT-LIE/RT-LIE-01.html#section-5). The field-only basis statement uses the preceding basis and complement lesson. All other determinant, cofactor and coordinate identities here are proved over arbitrary commutative rings, including characteristic two.

Hefferon's source chapters treat the determinant definition, permutation signs and expansion, multilinearity, transpose, multiplication and cofactors. The presentation here includes full proofs in dependency order and distinguishes field and ring conditions. The exercises have their solutions above; none is an external prerequisite.

## Sources

- Jim Hefferon, *Linear Algebra*, programme source edition: [determinant construction and properties](https://kokunoyumeto.github.io/program-matematika-indonesia/en/readers/hefferon-linear-algebra/sources/det1.tex).
- Jim Hefferon, *Linear Algebra*, programme source edition: [cofactors and the adjugate](https://kokunoyumeto.github.io/program-matematika-indonesia/en/readers/hefferon-linear-algebra/sources/det3.tex).
