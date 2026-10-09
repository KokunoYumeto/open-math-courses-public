# Representations of GL₂ over finite fields

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Independent AI review is not yet recorded. Public domain (CC0).*

The geometry of a two-dimensional vector space gives two ways to build representations of its general linear group. Rational lines lead to principal series and the Steinberg representation. Multiplication in a quadratic field extension supplies an elliptic torus. Combining induction from that torus with induction from an additive subgroup produces the remaining representations. Character orthogonality turns a difference of representations into an actual irreducible representation.

We construct every irreducible complex representation of \(G=\mathrm{GL}_2(\mathbf F_q)\), for every prime power \(q\), including even characteristic. We use character determination, orthogonality, completeness and the column relation from Characters and the orthogonality relations, Theorems 3.1–3.2 and 4.1 and Corollary 4.2. The induced-character formula, reciprocity and tensoring with a character are [Induced representations and Frobenius reciprocity](RT-FIN-06.md), formulas (3), (8), Theorem 3.1 and Proposition 4.1. Mackey's intertwining formula is [Mackey theory and Clifford's theorem](RT-FIN-07.md), Corollary 1.2. The final examples use the Frobenius–Schur indicator from [Tensor products, duals and real representations](RT-FIN-04.md), Theorems 2.1 and 3.1. Basic references are [Etingof et al.], [Gruson–Serganova], [Deligne–Lusztig 1976] and [Deligne–Lusztig 1982].

Representations are finite-dimensional over \(\mathbf C\). Write \(\widehat A\) for the complex linear characters of an abelian group \(A\), and use an inner product linear in the first variable. Set

\[
B=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:ad\ne0\right\},\quad
U=\{u(x):x\in\mathbf F_q\},\quad
u(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix},
\tag{1}
\]

and let \(T\) be the diagonal subgroup and \(Z=\{aI:a\ne0\}\). Distinguish \(T\) from the elliptic torus introduced below.

## 1. Fields, eigenvalues and rational lines

The elementary field facts needed for the elliptic construction can be obtained directly.

**Lemma 1.1 (quadratic extension and its characters).** There is a field \(K\) of \(q^2\) elements containing \(\mathbf F_q\). Its nontrivial \(\mathbf F_q\)-automorphism is \(\lambda\mapsto\lambda^q\). The groups \(H=\mathbf F_q^\times\) and \(E=K^\times\) are cyclic. The norm

\[
N:E\longrightarrow H,\qquad N(\lambda)=\lambda^{q+1}
\tag{2}
\]

is onto. Exactly \(q-1\) characters of \(E\) satisfy \(\theta^q=\theta\), where \(\theta^q(\lambda)=\theta(\lambda^q)\); they are the characters \(\chi\circ N\).

**Proof.** Among the \(q^2\) monic quadratic polynomials, exactly \(q(q+1)/2\) are products of two monic linear factors: an unordered pair of roots, with repetition, determines the product. Thus \(q(q-1)/2>0\) are irreducible. Quotienting \(\mathbf F_q[X]\) by any one gives \(K\).

The \(q\)-power map is an injective field homomorphism, hence an automorphism of this finite field. Lagrange's theorem gives \(x^{q^2}=x\) for all \(x\in K\), so its square is the identity. Its fixed elements are exactly \(\mathbf F_q\): they include that field and are roots of the polynomial \(X^q-X\), which has at most \(q\) roots. An element outside the base field generates the quadratic extension, and its minimal polynomial has exactly the two distinct roots \(\lambda,\lambda^q\). Every base-field automorphism must send it to one of these roots, so the identity and Frobenius are the only two automorphisms.

For any finite subgroup \(A\) of the multiplicative group of a field, let \(m\) be the least common multiple of the orders of its elements. For each prime power dividing \(m\), choose an element whose order contains that entire prime power and raise it to a suitable coprime-part power. Multiplying these commuting elements of coprime orders gives an element of order \(m\). Every element of \(A\) is a root of \(X^m-1\), so \(|A|\le m\); the element just constructed gives \(m\le|A|\). Consequently \(A\) is cyclic. This applies to \(H,E\).

If \(z\) generates \(E\), then \(z^{q+1}\) has order \(q-1\). It is fixed by the \(q\)-power map, so it generates \(H\), proving norm surjectivity. A character is determined by \(\theta(z)=\exp(2\pi i k/(q^2-1))\). The condition \(\theta^q=\theta\) is \((q^2-1)\mid k(q-1)\), or \((q+1)\mid k\). These are precisely the norm characters, and there are \(q-1\) of them. \(\square\)

Regard \(K\) as a two-dimensional \(\mathbf F_q\)-space. Multiplication by \(\lambda\) embeds \(E\) into \(G\) after choosing a basis. Denote this operator by \(e_\lambda\). Its determinant is \(N(\lambda)\); its eigenvalues over \(K\) are \(\lambda,\lambda^q\) when \(\lambda\notin\mathbf F_q\). Indeed its minimal polynomial is \((X-\lambda)(X-\lambda^q)\), which has coefficients in the fixed field and is irreducible over it.

**Proposition 1.2 (all conjugacy classes).** The four class types, their centralizer orders and their numbers are as follows. In the last two rows take unordered pairs and Frobenius pairs, respectively.

| Representative | Conditions | Centralizer order | Class size | Number of classes |
|---|---|---:|---:|---:|
| \(aI\) | \(a\in H\) | \(q(q+1)(q-1)^2\) | \(1\) | \(q-1\) |
| \(j_a=a u(1)\) | \(a\in H\) | \(q(q-1)\) | \(q^2-1\) | \(q-1\) |
| \(d_{a,b}=\operatorname{diag}(a,b)\) | \(a,b\in H, a\ne b\) | \((q-1)^2\) | \(q(q+1)\) | \((q-1)(q-2)/2\) |
| \(e_\lambda\) | \(\lambda\in E\setminus H\) | \(q^2-1\) | \(q(q-1)\) | \(q(q-1)/2\) |

There are \(q^2-1\) classes in total.

**Proof.** Choose the first column of an invertible matrix nonzero and its second column outside the first column's span. This gives

\[
|G|=(q^2-1)(q^2-q)=q(q+1)(q-1)^2.
\tag{3}
\]

If the characteristic polynomial has two distinct roots in the base field, eigenvectors give \(d_{a,b}\), and conjugacy forgets their order. For a repeated root \(a\), either the matrix is scalar or its nonzero nilpotent part has square zero. A vector outside its kernel and its image give a Jordan basis. Rescaling that basis makes it \(j_a\). Distinct roots \(a\) distinguish these classes.

For an irreducible characteristic polynomial \(f\), a nonzero vector \(v\) and \(gv\) are independent, since dependence would give a base-field eigenvalue. The action is therefore the cyclic module \(\mathbf F_q[X]/(f)\). The roots of every such quadratic lie in \(K\): the quotient field has \(q^2\) elements, so \(f\) divides \(X^{q^2}-X\); this polynomial splits into distinct linear factors in \(K\), by the preceding lemma and its nonzero derivative. Thus the action is \(e_\lambda\), with \(\lambda\) unique up to \(q\)-power. Conversely equal characteristic polynomials give the same cyclic module, so these pairs determine conjugacy exactly.

Commuting with \(j_a\) forces a matrix to have the form \(\begin{pmatrix}r&s\\0&r\end{pmatrix}\), with \(r\ne0\). Commuting with \(d_{a,b}\) preserves both eigenlines and gives the invertible diagonal matrices. Commuting with \(e_\lambda\) means being \(K\)-linear on the one-dimensional \(K\)-space; its invertible commutant is \(E\). Scalars commute with all of \(G\). Dividing (3) by these centralizer orders gives the sizes. Counting the labels gives the last column, and their sum is \(q^2-1\). \(\square\)

The projective line \(\mathbf P^1(\mathbf F_q)\) is the set of one-dimensional subspaces. A scalar fixes all \(q+1\) lines, \(j_a\) fixes its unique eigenline, \(d_{a,b}\) fixes two, and an elliptic element fixes none. These four counts will give the Steinberg character.

## 2. Two orbits produce principal series

The subgroup \(B\) stabilizes \(L_\infty=\mathbf F_q(1,0)\). The map \(gB\mapsto gL_\infty\) identifies \(G/B\) with the projective line. Its \(B\)-orbits are \(L_\infty\) and the \(q\) affine lines \(\mathbf F_q(x,1)\). The latter are one orbit because \(u(t)\) adds \(t\) to \(x\). With \(w=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), this proves

\[
G=B\sqcup BwB,\qquad B\cap wBw^{-1}=T.
\tag{4}
\]

Here is the same decomposition at the level of a basis of coset copies:

\[
\begin{array}{c|c|c}
G/B&\{B\}&\{u(x)wB:x\in\mathbf F_q\}\\\hline
\text{rational lines}&L_\infty&\mathbf F_q(x,1)\\
\text{number of copies}&1&q\\
u(t)&L_\infty\mapsto L_\infty&x\mapsto x+t
\end{array}
\tag{5}
\]

*Figure 1. The two actual orbits on rational lines. The affine orbit has \(q\) elements and is a free orbit for the additive group \(U\). Together with the fixed line it accounts for every coset and both terms in Mackey's formula.*

For \(\alpha,\beta\in\widehat H\), let \(\xi_{\alpha,\beta}\) be the character of \(B\) with value \(\alpha(a)\beta(d)\) on the matrix in (1). Define

\[
I(\alpha,\beta)=\operatorname{Ind}_B^G\xi_{\alpha,\beta},\qquad
D_\chi(g)=\chi(\det g).
\tag{6}
\]

We use the same symbol for a representation and its character when taking inner products.

**Theorem 2.1 (principal series and Steinberg).** The representation \(I(\alpha,\beta)\) has dimension \(q+1\). It is irreducible exactly when \(\alpha\ne\beta\), and then its isomorphism class determines the unordered pair \(\{\alpha,\beta\}\). The augmentation subspace

\[
\mathrm{St}=\left\{\sum_L c_L[L]\in\mathbf C[\mathbf P^1(\mathbf F_q)]:\sum_Lc_L=0\right\}
\tag{7}
\]

is irreducible of dimension \(q\), and

\[
I(\chi,\chi)\simeq D_\chi\oplus\mathrm{St}_\chi,
\qquad\mathrm{St}_\chi=\mathrm{St}\otimes D_\chi.
\tag{8}
\]

**Proof.** The dimension is the number of cosets. Mackey's formula and (4) give the full intertwining number

\[
\langle I(\alpha,\beta),I(\gamma,\delta)\rangle
=\delta_{\alpha,\gamma}\delta_{\beta,\delta}
+\delta_{\alpha,\delta}\delta_{\beta,\gamma}.
\tag{9}
\]

In the identity double coset we compare the two characters on \(B\). In the other we compare them on \(T\), where conjugating by \(w\) interchanges the diagonal entries. Characters of \(H\times H\) are equal exactly when both entries agree. This proves (9).

The norm is one for distinct entries and two for equal entries. Complete reducibility and character multiplicities therefore prove irreducibility in the former case. The nonzero Hom space between the two orders of a distinct pair is an isomorphism; (9) also proves the asserted uniqueness. For equal trivial entries, induction is the permutation representation. It is the direct sum of constants and the space (7), because \(q+1\ne0\) in \(\mathbf C\). Transitivity makes the constants occur once. A norm of two now forces the remaining summand to be one irreducible of multiplicity one. Tensoring with \(D_\chi\), whose restriction to \(B\) is \(\xi_{\chi,\chi}\), proves (8). \(\square\)

For an induced character, each fixed line contributes the character of the stabilizer on its coset copy. On a fixed eigenline with eigenvalue \(a\), the quotient eigenvalue is \(b\), and the contribution is \(\alpha(a)\beta(b)\). Thus

\[
\begin{array}{c|cccc}
g&aI&j_a&d_{a,b}&e_\lambda\\\hline
I(\alpha,\beta)(g)&(q+1)\alpha(a)\beta(a)&\alpha(a)\beta(a)&
\alpha(a)\beta(b)+\alpha(b)\beta(a)&0\\
\mathrm{St}(g)&q&0&1&-1
\end{array}
\tag{10}
\]

For the scalar and Jordan cases the two diagonal eigenvalues are \(a,a\). For \(\mathrm{St}\), subtract the constant character from the four fixed-line counts. This proves every entry of (10), independently of any table of irreducibles.

## 3. An elliptic torus and an additive character

The principal series do not yet fill the character space. Induction from \(E\) alone gives representations of degree \(q(q-1)\), too large for the missing types. A second induction will cancel most of that degree.

Choose a nontrivial additive character \(\psi:\mathbf F_q\to\mathbf C^\times\). For example choose a nonzero \(\mathbf F_p\)-linear functional \(\ell:\mathbf F_q\to\mathbf F_p\) and put \(\psi(x)=\exp(2\pi i\ell(x)/p)\). For \(\mu\in\widehat H\), define a linear character of \(ZU\) by

\[
\eta_{\mu,\psi}(a u(x))=\mu(a)\psi(x).
\tag{11}
\]

The expression is unique, \(Z\) commutes with \(U\), and \(u(x)u(y)=u(x+y)\), so this is a homomorphism. Let

\[
\Gamma_\mu=\operatorname{Ind}_{ZU}^G\eta_{\mu,\psi},\qquad
Y_\theta=\operatorname{Ind}_E^G\theta,\qquad
C_\theta=\Gamma_{\theta|_H}-Y_\theta.
\tag{12}
\]

The last expression is a virtual character: an integral difference of actual characters. It does not yet assert a representation exists with that character.

**Lemma 3.1 (the two induced tables).** The values are

\[
\begin{array}{c|cccc}
g&aI&j_a&d_{a,b}&e_\lambda\\\hline
\Gamma_\mu(g)&(q^2-1)\mu(a)&-\mu(a)&0&0\\
Y_\theta(g)&q(q-1)\theta(a)&0&0&\theta(\lambda)+\theta(\lambda^q)\\
C_\theta(g)&(q-1)\theta(a)&-\theta(a)&0&-\theta(\lambda)-\theta(\lambda^q)
\end{array}
\tag{13}
\]

In particular \(C_\theta(1)=q-1\), and \(\Gamma_\mu\) is independent, up to isomorphism, of the chosen nontrivial \(\psi\).

**Proof.** For a subgroup \(A\) and a linear character \(\eta\), regrouping the induced-character formula by its image under conjugation gives

\[
\operatorname{Ind}_A^G\eta(g)
=\frac{|C_G(g)|}{|A|}\sum_{h\in A\cap g^G}\eta(h).
\tag{14}
\]

Every element \(h\) in that intersection has exactly \(|C_G(g)|\) conjugators. For scalars the original formula gives \([G:A]\eta(g)\). Here \(|ZU|=q(q-1)\), so its index is \(q^2-1\). The intersection of the class of \(j_a\) with \(ZU\) consists exactly of \(a u(x)\), \(x\ne0\); all are conjugate by diagonal rescaling. Its centralizer has the same order as \(ZU\). Since a translate of the sum of \(\psi\) multiplies it by a nontrivial value, \(\sum_x\psi(x)=0\), and the sum over \(x\ne0\) is \(-1\). This proves the first row. Split noncentral and elliptic classes do not intersect \(ZU\).

The index of \(E\) is \(q(q-1)\). Jordan and split noncentral classes do not intersect it. An elliptic class intersects \(E\) precisely in \(e_\lambda,e_{\lambda^q}\), by its characteristic polynomial. Its centralizer is \(E\), so the factor in (14) is one. This gives the second row and then the third. The first row used only nontriviality of \(\psi\); equality of characters determines the induced representation. \(\square\)

*Reference:* [Etingof et al., §4.24.4] obtains the same virtual character using a tensor product involving \(\mathrm{St}\). Formula (12) exposes the additive induction directly.

## 4. Orthogonality makes the difference irreducible

Call \(\theta\in\widehat E\) **regular** if \(\theta\ne\theta^q\). All sums below are over actual elements, with a factor of two when replacing elliptic classes by elements of \(E\setminus H\).

For characters \(\theta,\phi\) of \(E\), put

\[
M=\sum_{a\in H}\theta(a)\overline{\phi(a)},\qquad
\Delta=\delta_{\theta,\phi}+\delta_{\theta,\phi^q}.
\tag{15}
\]

A character sum on a finite group is zero unless the character is trivial: translation by an element on which it is nontrivial proves this, as for \(\psi\). Expanding four products and changing \(\lambda\) to \(\lambda^q\) therefore gives

\[
\sum_{\lambda\in E}
(\theta(\lambda)+\theta(\lambda^q))
\overline{\phi(\lambda)+\phi(\lambda^q)}
=2(q^2-1)\Delta.
\tag{16}
\]

The part of that sum on \(H\) is \(4M\), since Frobenius fixes each \(a\in H\).

**Theorem 4.1 (cuspidal representations).** For every regular \(\theta\), \(C_\theta\) is the character of an irreducible representation \(\pi_\theta\) of degree \(q-1\). Its values are the third row of (13). Furthermore,

\[
\pi_\theta\simeq\pi_\phi
\quad\Longleftrightarrow\quad
\phi\in\{\theta,\theta^q\}.
\tag{17}
\]

It has no \(U\)-fixed vector.

**Proof.** Use the class sizes from Proposition 1.2 and (16). The central, Jordan and elliptic contributions give

\[
\begin{aligned}
|G|\langle C_\theta,C_\phi\rangle
&=((q-1)^2+q^2-1)M\\
&\quad+\frac{q(q-1)}2\bigl(2(q^2-1)\Delta-4M\bigr)\\
&=|G|\Delta.
\end{aligned}
\tag{18}
\]

The coefficient of \(M\) vanishes because \((q-1)^2+q^2-1=2q(q-1)\). For \(\phi=\theta\) regular, \(\Delta=1\). Expand the virtual character in the irreducible basis: \(C_\theta=\sum n_i\chi_i\), with integers \(n_i\), since (12) is a difference of representations. Norm one says \(\sum n_i^2=1\), so it is either an irreducible character or its negative. Its degree \(q-1>0\) chooses the positive sign. Formula (18) proves (17).

Finally, averaging the operators over \(U\) projects onto the fixed vectors. The dimension of that space is the average of the character. There is one identity and \(q-1\) elements \(u(x)\), \(x\ne0\), all conjugate to \(j_1\). Thus

\[
\dim\pi_\theta^U=\frac{(q-1)+(q-1)(-1)}q=0.
\tag{19}
\]

This completes the construction. \(\square\)

The use of virtual characters is essential to this argument. Norm one alone for an arbitrary class function would not prove it is a character: integrality of the coefficients came from (12).

An irreducible representation is called **cuspidal** here when it is not a constituent of any \(I(\alpha,\beta)\). This is equivalent to having no \(U\)-fixed vectors. Indeed \(V^U\) is stable under \(T\), and the abelian group \(T\) decomposes it into linear characters. A nonzero such component is exactly a nonzero \(B\)-map from a character trivial on \(U\) to \(V\). Frobenius reciprocity identifies that with occurrence in a principal series. This proves the equivalence and justifies the name for \(\pi_\theta\).

### Why regularity cannot be omitted

If \(\theta=\chi\circ N\), the third row of (13) is the character of

\[
C_{\chi\circ N}=\mathrm{St}_\chi-D_\chi.
\tag{20}
\]

To verify this, its scalar values are \((q-1)\chi(a^2)\), its Jordan values \(-\chi(a^2)\), its split values zero, and its elliptic values \(-2\chi(N\lambda)\). These are exactly the difference given by (10) and the determinant character. Its norm is two, also visible in (18). It is not an additional irreducible. Lemma 1.1 shows that these are all the nonregular parameters.

## 5. Completing the table and separating the families

**Theorem 5.1 (classification).** A complete list of mutually nonisomorphic irreducible representations consists of

- \(D_\chi\), for \(\chi\in\widehat H\), of degree \(1\);
- \(\mathrm{St}_\chi\), for \(\chi\in\widehat H\), of degree \(q\);
- \(I(\alpha,\beta)\), for unordered distinct \(\alpha,\beta\in\widehat H\), of degree \(q+1\);
- \(\pi_\theta\), for regular \(\theta\in\widehat E\) up to \(\theta\leftrightarrow\theta^q\), of degree \(q-1\).

**Proof of separation.** Determinant characters are distinct because the determinant is onto. Frobenius reciprocity gives

\[
\langle D_\chi,I(\alpha,\beta)\rangle
=\delta_{\chi,\alpha}\delta_{\chi,\beta}.
\tag{21}
\]

Substitute \(\mathrm{St}_\chi=I(\chi,\chi)-D_\chi\) in (9) and (21). It follows that the Steinberg twists have pairwise inner products \(\delta_{\chi,\eta}\), are orthogonal to all determinant characters, and are orthogonal to all unequal principal series. Formula (9) separates the latter among themselves.

For completeness, compute the remaining cross-inner-products directly. Put

\[
M_\chi=\sum_{a\in H}\theta(a)\overline{\chi(a^2)}.
\tag{22}
\]

When \(\theta\) is regular, character orthogonality on \(E\) gives

\[
\sum_{\lambda\in E\setminus H}
(\theta(\lambda)+\theta(\lambda^q))\overline{\chi(N\lambda)}
=-2M_\chi.
\tag{23}
\]

Indeed the full sum over \(E\) is zero: neither \(\theta\) nor \(\theta^q\) equals the norm character \(\chi\circ N\). Subtract its part on \(H\), which is \(2M_\chi\). The class contributions now yield

\[
\begin{aligned}
|G|\langle C_\theta,D_\chi\rangle
&=\bigl((q-1)-(q^2-1)+q(q-1)\bigr)M_\chi=0,\\
|G|\langle C_\theta,\mathrm{St}_\chi\rangle
&=q(q-1)M_\chi-q(q-1)M_\chi=0.
\end{aligned}
\tag{24}
\]

For \(I(\alpha,\beta)\), only central and Jordan classes contribute; their contributions cancel:

\[
|G|\langle C_\theta,I(\alpha,\beta)\rangle
=\bigl((q-1)(q+1)-(q^2-1)\bigr)
\sum_{a\in H}\theta(a)\overline{\alpha(a)\beta(a)}=0.
\tag{25}
\]

Together with (18), these computations prove all required orthogonality.

**Proof of completeness.** The numbers in the four families are

\[
q-1,\quad q-1,\quad\frac{(q-1)(q-2)}2,\quad\frac{q(q-1)}2.
\tag{26}
\]

For the last, Lemma 1.1 gives \(q^2-1-(q-1)=q(q-1)\) regular characters, each in a two-element Frobenius orbit. The sum of (26) is \(q^2-1\), the dimension of the class-function space. The orthonormal irreducible characters constructed above are therefore a basis, so there is no other irreducible. Their squared degrees also give

\[
(q-1)(1+q^2)
+\frac{(q-1)(q-2)}2(q+1)^2
+\frac{q(q-1)}2(q-1)^2
=q(q+1)(q-1)^2=|G|.
\tag{27}
\]

This agrees with the regular representation. \(\square\)

Here is the full table in symbolic form. Every column has the conditions of Proposition 1.2; every row has the parameter conditions of Theorem 5.1.

| Character | \(aI\) | \(j_a\) | \(d_{a,b}\) | \(e_\lambda\) |
|---|---|---|---|---|
| \(D_\chi\) | \(\chi(a^2)\) | \(\chi(a^2)\) | \(\chi(ab)\) | \(\chi(N\lambda)\) |
| \(\mathrm{St}_\chi\) | \(q\chi(a^2)\) | \(0\) | \(\chi(ab)\) | \(-\chi(N\lambda)\) |
| \(I(\alpha,\beta)\) | \((q+1)\alpha(a)\beta(a)\) | \(\alpha(a)\beta(a)\) | \(\alpha(a)\beta(b)+\alpha(b)\beta(a)\) | \(0\) |
| \(\pi_\theta\) | \((q-1)\theta(a)\) | \(-\theta(a)\) | \(0\) | \(-\theta(\lambda)-\theta(\lambda^q)\) |

The column relation follows too. Multiply the entry in column \(K\) by \(\sqrt{|K|/|G|}\). Row orthogonality makes the resulting square matrix unitary. Its columns are orthonormal, giving

\[
\sum_\rho\chi_\rho(g)\overline{\chi_\rho(h)}
=\begin{cases}|C_G(g)|,&g,h\text{ conjugate},\\0,&\text{otherwise}.
\end{cases}
\tag{28}
\]

This also explains why class sizes, rather than just class counts, enter a numerical table check.

For \(q>2\), the cuspidal degree exceeds one, so the only linear characters are determinant characters. For \(q=2\) the cuspidal degree is one; this gives the additional sign character below. The distinction matters when extending an odd-characteristic description to every finite field.

## 6. Two complete small tables

### Three nonzero vectors: the case \(q=2\)

The group acts on the three nonzero vectors of \(\mathbf F_2^2\). The action is faithful because fixing every vector fixes a basis. Both \(G\) and \(S_3\) have order six, so it is an isomorphism. Scalars give the identity class, nontrivial unipotents the three transpositions, and the elliptic class the two three-cycles.

Here \(H\) is trivial and \(E\) has order three. Its two nontrivial characters form one Frobenius pair. Their sum at either nonidentity element is \(-1\), so their cuspidal character takes values \(1,-1,1\).

| Character | \(1\) | Transposition | Three-cycle |
|---|---:|---:|---:|
| Class size | \(1\) | \(3\) | \(2\) |
| \(D_1\) | \(1\) | \(1\) | \(1\) |
| \(\mathrm{St}\) | \(2\) | \(0\) | \(-1\) |
| \(\pi_\theta\) | \(1\) | \(-1\) | \(1\) |

These are the trivial, standard and sign rows of the \(S_3\) table in Characters and the orthogonality relations, §5. They all have indicator one: sign and trivial are real lines, and the standard plane has indicator \((2+3\cdot2+2(-1))/6=1\), as in [Tensor products, duals and real representations](RT-FIN-04.md), Exercise 1. The sign row is cuspidal because the order-two group \(U\) acts nontrivially on it.

### Eight classes: the case \(q=3\)

Use \(K=\mathbf F_3[i]\), with \(i^2=-1\), and \(z=1+i\). Then \(z^2=-i\), \(z^4=-1\), so \(z\) generates \(E\) of order eight. A concrete multiplication matrix is

\[
e_{a+bi}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}.
\tag{29}
\]

Let \(\epsilon\) be the nontrivial character of \(\mathbf F_3^\times\), let \(\zeta=\exp(2\pi i/8)\), and define \(\theta_k(z)=\zeta^k\). Frobenius acts on indices by \(k\mapsto3k\) modulo eight. The nonregular indices are \(0,4\); the regular pairs are \(\{1,3\},\{2,6\},\{5,7\}\). Put \(r=i\sqrt2\) as a complex number, so \(\overline r=-r\) and \(r^2=-2\); this complex \(i\) is distinguished from the element of \(K\) by context.

| Character | \(I\) | \(-I\) | \(j_1\) | \(j_{-1}\) | \(d_{1,-1}\) | \(e_z\) | \(e_{z^2}\) | \(e_{z^5}\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Class size | \(1\) | \(1\) | \(8\) | \(8\) | \(12\) | \(6\) | \(6\) | \(6\) |
| \(D_1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(D_\epsilon\) | \(1\) | \(1\) | \(1\) | \(1\) | \(-1\) | \(-1\) | \(1\) | \(-1\) |
| \(\mathrm{St}\) | \(3\) | \(3\) | \(0\) | \(0\) | \(1\) | \(-1\) | \(-1\) | \(-1\) |
| \(\mathrm{St}_\epsilon\) | \(3\) | \(3\) | \(0\) | \(0\) | \(-1\) | \(1\) | \(-1\) | \(1\) |
| \(I(1,\epsilon)\) | \(4\) | \(-4\) | \(1\) | \(-1\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \(\pi_{\theta_1}\) | \(2\) | \(-2\) | \(-1\) | \(1\) | \(0\) | \(-r\) | \(0\) | \(r\) |
| \(\pi_{\theta_2}\) | \(2\) | \(2\) | \(-1\) | \(-1\) | \(0\) | \(0\) | \(2\) | \(0\) |
| \(\pi_{\theta_5}\) | \(2\) | \(-2\) | \(-1\) | \(1\) | \(0\) | \(r\) | \(0\) | \(-r\) |

For example, \(\zeta+\zeta^3=i\sqrt2\), which gives the first elliptic value \(-r\). Multiplication by \(z^2\) gives \(\zeta^4+\zeta^{12}=-2\) for \(\theta_2\), hence the entry \(2\). These signs follow the induced difference (12).

If \(X\) is the eight-by-eight matrix of character rows, the two orthogonality relations are explicitly

\[
X\operatorname{diag}(1,1,8,8,12,6,6,6)\overline X^{\,t}=48I_8,
\quad
\overline X^{\,t}X=\operatorname{diag}(48,48,6,6,4,8,8,8).
\tag{30}
\]

The proof in §5 applies to these entries. As illustrations of the cancellations, the first cuspidal row has weighted norm \((4+4+8+8+12+12)/48=1\). Its weighted product with the conjugate cuspidal row is \((4+4+8+8-12-12)/48=0\), since \(r^2=-2\). The split column has norm \(1+1+1+1=4\), its centralizer order. The squared degrees are \(1+1+9+9+16+4+4+4=48\).

### Real structures and the quaternion group

The square map sends the eight classes in the table, in order, to

\[
I,\ I,\ j_1,\ j_1,\ I,\ e_{z^2},\ -I,\ e_{z^2}.
\tag{31}
\]

For the Jordan classes, \(u(1)^2=u(2)\) is conjugate to \(u(1)\). Squaring \(e_{z^5}\) gives \(e_{z^{10}}=e_{z^2}\). Consequently the indicator of a row \(\chi\) is

\[
\nu(\chi)=\frac{14\chi(I)+16\chi(j_1)+12\chi(e_{z^2})+6\chi(-I)}{48}.
\tag{32}
\]

For \(\pi_{\theta_1}\) and \(\pi_{\theta_5}\) this is \((28-16-12)/48=0\). They are nonreal conjugate representations. For \(\pi_{\theta_2}\) it is \((28-16+24+12)/48=1\). Substitution gives one for each of the other five rows. Thus all the real-valued irreducibles in this particular table have real forms.

Nevertheless a restriction recovers the quaternionic example from [Tensor products, duals and real representations](RT-FIN-04.md), §6. In \(G\) take

\[
A=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
B_0=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\tag{33}
\]

Direct multiplication in \(\mathbf F_3\) gives \(A^2=B_0^2=-I\) and \(AB_0=-B_0A\). The eight distinct matrices \(\{\pm I,\pm A,\pm B_0,\pm AB_0\}\) therefore form \(Q_8\). Every noncentral element has characteristic polynomial \(X^2+1\) and lies in the class \(e_{z^2}\). Either nonreal cuspidal row restricts to values \(2,-2,0,0,0\) on its five classes. Its norm on \(Q_8\) is \((4+4)/8=1\), and its indicator is \((2\cdot2+6(-2))/8=-1\). Thus the restrictions are irreducible and quaternionic, although the two representations of \(G\) themselves have indicator zero.

## 7. Parabolic duality and the next geometric questions

There is already a full duality calculation available from the rational-line construction. For a \(G\)-representation \(V\), its fixed space \(V^U\) is a representation of \(T=B/U\). Inflate it to \(B\), and define on the group of virtual representations

\[
\mathcal D[V]=[\operatorname{Ind}_B^G V^U]-[V].
\tag{34}
\]

Taking \(U\)-invariants is exact over \(\mathbf C\), because averaging gives a projection and a map from an invariant vector lifts by averaging. Thus (34) is well-defined and additive.

**Proposition 7.1 (rank-one duality).** The operation satisfies

\[
\mathcal D(D_\chi)=\mathrm{St}_\chi,\quad
\mathcal D(\mathrm{St}_\chi)=D_\chi,\quad
\mathcal D(I(\alpha,\beta))=I(\alpha,\beta)\ (\alpha\ne\beta),\quad
\mathcal D(\pi_\theta)=-\pi_\theta.
\tag{35}
\]

It is an involution and preserves the character inner product.

**Proof.** In the induced coset basis (5), the fixed-line copy has \(T\)-character \(\alpha\otimes\beta\). On the affine copies \(U\) acts regularly by translation, so its fixed space is their sum, a single line. For \(t=\operatorname{diag}(a,d)\),

\[
t u(x)w=u((a/d)x)w\operatorname{diag}(d,a).
\tag{36}
\]

The affine sum therefore has character \(\beta\otimes\alpha\). Hence

\[
I(\alpha,\beta)^U\simeq
(\alpha\otimes\beta)\oplus(\beta\otimes\alpha).
\tag{37}
\]

The fixed space of \(D_\chi\) is \(\chi\otimes\chi\), and subtracting it from (37) with equal entries gives \(\mathrm{St}_\chi^U\simeq\chi\otimes\chi\). Equation (19) gives \(\pi_\theta^U=0\). Inducing each of these spaces and subtracting the original representation proves (35), using (8) and the symmetry of principal series. This permutes an orthonormal basis up to signs and has square the identity, proving both final assertions. \(\square\)

This is the rank-one parabolic operation underlying Alvis–Curtis and Deligne–Lusztig duality. The exchange of trivial and Steinberg representations has been proved here, including its signs on the other families. It differs from taking the contragredient: for example the contragredient exchanges \(\pi_{\theta_1}\) and \(\pi_{\theta_5}\) at \(q=3\), whereas (35) negates each virtual class. [Deligne–Lusztig 1982, §§1 and 5] constructs the broader operation from parabolic fixed spaces.

For the geometric comparison, let \(\mathbf G\) be a connected reductive group over \(\overline{\mathbf F}_q\), defined over \(\mathbf F_q\) with Frobenius \(F\), and let \(\mathbf T\) be an \(F\)-stable maximal torus. Choose a Borel subgroup \(\mathbf B\supset\mathbf T\), not necessarily \(F\)-stable, and write \(\mathbf U\) for its unipotent radical. The construction uses a variety with a torus action, not just its flag-space quotient:

\[
\widetilde X_{\mathbf T\subset\mathbf B}
=\{g\in\mathbf G:g^{-1}F(g)\in F(\mathbf U)\}/(\mathbf U\cap F(\mathbf U)),
\qquad
\widetilde X_{\mathbf T\subset\mathbf B}\longrightarrow X_{\mathbf T\subset\mathbf B}
=\widetilde X_{\mathbf T\subset\mathbf B}/\mathbf T^F.
\]

Left multiplication by \(\mathbf G^F\) commutes with right multiplication by \(\mathbf T^F\). The displayed projection is a \(\mathbf G^F\)-equivariant \(\mathbf T^F\)-torsor. Choose a prime \(\ell\ne\operatorname{char}\mathbf F_q\) and a compatible identification of the algebraic roots of unity in \(\overline{\mathbf Q}_\ell\) with their complex counterparts, so that finite-group characters can be compared. For a character \(\theta:\mathbf T^F\to\overline{\mathbf Q}_\ell^\times\), use the torus-action convention of [Deligne–Lusztig 1976, §1.20] and set

\[
R_{\mathbf T}^{\theta}
=\sum_i(-1)^i[H_c^i(\widetilde X_{\mathbf T\subset\mathbf B},\overline{\mathbf Q}_\ell)_\theta].
\]

Equivalently one uses the associated rank-one local system on the flag base. Ordinary cohomology of that base with constant coefficients is not, by itself, a construction of the indicated torus-isotypic part. Independence from the containing Borel is part of the geometric theory. For \(\mathrm{GL}_2\), the split and elliptic flag bases are respectively \(\mathbf P^1(\mathbf F_q)\) and \(\mathbf P^1(\overline{\mathbf F}_q)\setminus\mathbf P^1(\mathbf F_q)\).

**Geometric comparison theorems (stated here without their cohomological proofs).** Write \(\sigma(\mathbf H)\) for the \(\mathbf F_q\)-split rank of a connected reductive group or torus \(\mathbf H\). A torus character is in **general position** if its stabilizer in \((N_{\mathbf G}(\mathbf T)/\mathbf T)^F\) is trivial. It is **nonsingular** if its pairing with every coroot is nonzero, as in [Deligne–Lusztig 1976, Definition 5.15]. More concretely, choose \(d\) over which \(\mathbf T\) splits and a given coroot \(\alpha^\vee:\mathbf G_m\to\mathbf T\) is defined. The character

\[
\mathbf F_{q^d}^{\times}\xrightarrow{\alpha^\vee}\mathbf T^{F^d}
\xrightarrow{N_d}\mathbf T^F\xrightarrow{\theta}\overline{\mathbf Q}_\ell^{\times},
\qquad N_d(t)=tF(t)\cdots F^{d-1}(t),
\]

must be nontrivial for every coroot. This condition is unchanged on enlarging a splitting field. The following are established results, not conjectural comparison problems:

- If the centre of \(\mathbf G\) is connected, nonsingularity and general position are equivalent (Proposition 5.16). In general, general position implies nonsingularity (Corollary 5.18); the converse is not being asserted without the connected-centre hypothesis.
- For two \(F\)-stable maximal tori and their characters, the inner product is the number of rational Weyl transporters matching the characters (Theorem 6.8). Explicitly, with \(\operatorname{Ad}(g):\mathbf T'\to\mathbf T\),

\[
\langle R_{\mathbf T}^{\theta},R_{\mathbf T'}^{\theta'}\rangle_{\mathbf G^F}
=\frac{\#\{g\in\mathbf G^F:g\mathbf T'g^{-1}=\mathbf T,\ \theta\circ\operatorname{Ad}(g)=\theta'\}}{|\mathbf T^F|}.
\]

- If \(\theta\) is nonsingular, the virtual character \((-1)^{\sigma(\mathbf G)-\sigma(\mathbf T)}R_{\mathbf T}^{\theta}\) is the character of an actual representation; it is irreducible when \(\theta\) is in general position (Proposition 7.4). In the latter case the self-pairing in Theorem 6.8 is one, and the rank sign chooses the actual, rather than negative, irreducible character.
- If in addition \(\mathbf T\) is contained in no proper \(F\)-stable parabolic subgroup of \(\mathbf G\), that actual representation is cuspidal (Theorem 8.3). Cuspidal here means that its invariants under the rational unipotent radical of every proper rational parabolic vanish. Nonsingularity is essential to the stated theorem; ellipticity alone is not the assertion.

For \(\mathbf G=\mathrm{GL}_2\), these comparison results identify the split-torus character with \(I(\alpha,\beta)\) and the elliptic-torus character with \(-C_\theta\), in the parameter convention of (12). In particular the already constructed regular cuspidal representation satisfies

\[
[\pi_\theta]=-R_{\mathbf T}^{\theta},
\qquad \mathbf T^F=\mathbf F_{q^2}^{\times},\qquad \theta\ne\theta^q.
\]

The centre of \(\mathrm{GL}_2\) is connected, so Proposition 5.16 identifies regularity with nonsingularity here. Its rational Weyl group has the two actions \(\theta\mapsto\theta\) and \(\theta\mapsto\theta^q\). The split ranks are \(\sigma(\mathrm{GL}_2)=2\) and \(\sigma(\mathbf T)=1\), giving \((-1)^{2-1}=-1\). The elliptic torus is in no proper rational parabolic, since such a parabolic stabilizes a rational line. Thus the hypotheses give an irreducible cuspidal character for every prime power \(q\), including even characteristic. For a norm character the comparison instead gives \(R_{\mathbf T}^{\chi\circ N}=D_\chi-\mathrm{St}_\chi\), by (18); it must not be called the negative of a new cuspidal irreducible.

The cohomological construction, its general theorems, and its identification with the elementary character table are not proved in this lesson. Their complete geometric proofs are separate obligations; an external citation is not an internal proof provider. The elementary classification and Proposition 7.1 above do not use these assertions. The arithmetic checks below explain their hypotheses and sign, but do not replace the missing cohomological comparison proof.

The torus conditions can already be understood arithmetically here. The elliptic torus has no rational invariant line, by irreducibility of its quadratic action. Frobenius acts on its characters by \(\theta\mapsto\theta^q\). Moreover

\[
\theta=\theta^q
\quad\Longleftrightarrow\quad
\theta|_{\ker N}=1.
\tag{38}
\]

Indeed \(\ker N\) is generated by \(z^{q-1}\), of order \(q+1\); triviality there is exactly \((q^2-1)\mid k(q-1)\), the condition in Lemma 1.1. Thus the regularity test is the failure to factor through the norm. The split ranks of \(\mathrm{GL}_2\) and its elliptic torus are respectively two and one: the latter has the scalar split torus, and a two-dimensional split torus would have all its characters fixed by Frobenius, whereas the two eigencharacters of the elliptic torus are interchanged. Their rank difference again indicates the sign \(-1\) in the geometric comparison.

Over a nonarchimedean local field with residue field \(\mathbf F_q\), reduction gives a quotient \(\mathrm{GL}_2(\mathcal O)\to\mathrm{GL}_2(\mathbf F_q)\). A representation \(\pi_\theta\) therefore inflates to the compact subgroup, trivially on the kernel of reduction. This is the finite-group input for the depth-zero construction in the planned lesson *Supercuspidal representations of GL₂ over a local field: constructions*. Its exact next theorem is that, after extending the central action compatibly to \(F^\times\mathrm{GL}_2(\mathcal O)\), compact induction yields an irreducible supercuspidal representation. That local-field theorem belongs to that planned lesson; our proved contribution is the cuspidal input and its character, including the case of residue characteristic two.

## 8. Exercises with complete solutions

### Exercise 1 — Account for every small class

For \(q=2,3\), list the four types, their counts and sizes, and show that their total number of elements is \(|G|\). For \(q=3\), give explicit elliptic representatives using (29).

**Solution.** For \(q=2\) there is one scalar class of size one, one Jordan class of size three, no noncentral split class, and one elliptic class of size two. Their sizes sum to six and there are three classes. Multiplication by a root of \(X^2+X+1\) gives the elliptic representative.

For \(q=3\), there are two scalar classes of size one, two Jordan classes of size eight, one split class of size twelve and three elliptic classes of size six. The element count is \(2+16+12+18=48\), and the class count is eight. Besides \(I,-I,j_1,j_{-1},d_{1,-1}\), use

\[
e_z=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\quad
e_{z^2}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
e_{z^5}=\begin{pmatrix}-1&1\\-1&-1\end{pmatrix}.
\tag{39}
\]

The first and third have respectively traces \(-1,1\), determinant \(-1\), and discriminant \(-1\), a nonsquare in \(\mathbf F_3\). The middle has polynomial \(X^2+1\), also irreducible. Their root pairs are \(\{z,z^3\},\{z^2,z^6\},\{z^5,z^7\}\), so all three classes are distinct.

### Exercise 2 — Use both Bruhat cells

Derive (9) from Mackey and Frobenius reciprocity. Recover all irreducibility and isomorphism assertions of Theorem 2.1. At \(q=3\), decompose the three ordered parameter possibilities up to swapping.

**Solution.** The action on lines gives exactly the two double cosets \(B,BwB\). Their intersections are \(B\) and \(T\). Reciprocity followed by Mackey makes the Hom space between the two induced modules a direct sum of the Hom spaces of their linear characters on these intersections. On \(B\) equality means \(\alpha=\gamma,\beta=\delta\). On \(T\) conjugation by \(w\) swaps the entries, giving \(\alpha=\delta,\beta=\gamma\). These one-dimensional or zero-dimensional spaces give (9).

The endomorphism dimension is one for unequal entries and two for equal entries, so the first is irreducible and the second is reducible. A distinct swapped pair has a nonzero map between irreducibles and hence gives one isomorphism class. No other pair can do so by (9). For equal entries, \(D_\chi\) occurs once by reciprocity; subtracting its squared multiplicity from the norm two leaves exactly one other irreducible, of degree \(q\). Tensoring the trivial-entry decomposition gives (8).

For \(q=3\), the characters of \(H\) are \(1,\epsilon\). The resulting modules are \(I(1,1)=D_1\oplus\mathrm{St}\), \(I(\epsilon,\epsilon)=D_\epsilon\oplus\mathrm{St}_\epsilon\), and the irreducible \(I(1,\epsilon)=I(\epsilon,1)\). Their dimensions are four in each case, with summand dimensions \(1+3\) for the first two.

### Exercise 3 — Check the Steinberg norm directly

Compute the Steinberg character from fixed lines and verify its norm using all four class types. Why does the calculation remain valid at \(q=2\)?

**Solution.** The four fixed-line counts are \(q+1,1,2,0\). Removing the constants gives \(q,0,1,-1\). The sum of the weighted squared values is

\[
(q-1)q^2
+\frac{(q-1)(q-2)}2q(q+1)
+\frac{q(q-1)}2q(q-1)
=q(q+1)(q-1)^2.
\tag{40}
\]

Factor \(q(q-1)\) on the left; the remaining bracket is \(q+((q-2)(q+1)+q(q-1))/2=q^2-1\). Division by (3) gives norm one. At \(q=2\) the split term simply vanishes, and the weighted sum is \(4+2=6\). No step divides by \(q-2\) or requires a nonsquare in the base field.

### Exercise 4 — Turn a virtual character into a representation

For regular \(\theta\), construct the virtual character (12), calculate its norm and degree, and prove that it is an irreducible cuspidal character. Repeat the norm calculation for a norm character and identify the resulting virtual class.

**Solution.** Put \(\mu=\theta|_H\). The two induced degrees are \(q^2-1\) and \(q(q-1)\), giving difference \(q-1\). Formula (14), the sum \(\sum_{x\ne0}\psi(x)=-1\), and the two elliptic conjugates give (13).

Since \(\theta/\theta^q\) is nontrivial on \(E\) and trivial on \(H\), its sum over \(E\setminus H\) is \(-(q-1)\). The inverse character has the same sum. Therefore

\[
\sum_{\lambda\in E\setminus H}|\theta(\lambda)+\theta(\lambda^q)|^2
=2(q^2-q)-2(q-1)=2(q-1)^2.
\tag{41}
\]

Central and Jordan contributions are \((q-1)^3\) and \((q^2-1)(q-1)\). Elliptic classes contribute \(q(q-1)/2\) times (41). Their total is

\[
(q-1)^3+(q^2-1)(q-1)+q(q-1)^3
=q(q+1)(q-1)^2=|G|.
\tag{42}
\]

Thus the norm is one. Integral multiplicities of the virtual class leave exactly one coefficient \(\pm1\), and its positive degree fixes the plus sign. Averaging on \(U\) gives zero as in (19), so the irreducible is cuspidal.

For \(\theta=\chi\circ N\), the elliptic summand in (41) is instead \(4(q^2-q)\), since \(\theta=\theta^q\). The total weighted norm is twice \(|G|\), in agreement with (18). Comparing the four values identifies the virtual representation with \(\mathrm{St}_\chi-D_\chi\). It is a difference of two distinct irreducibles, not a new irreducible of degree \(q-1\).

## References

- **P. Etingof, O. Golberg, S. Hensel, T. Liu, A. Schwendner, D. Vaintrob and E. Yudovina**, *Introduction to Representation Theory*, [lecture notes](https://math.mit.edu/~etingof/replect.pdf), §4.24, particularly Theorem 4.71, §4.24.4 and Lemma 4.72. These give an odd-characteristic presentation of the principal and cuspidal character constructions. The field and induction arguments here cover every prime power.
- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Springer, 2018, Chapter 6 §9, especially Definition 9.3 and Example 9.22. The general positive self-adjoint Hopf-algebra discussion supplies context for the four families; the rank-two proof is given here directly.
- **P. Deligne and G. Lusztig**, *Representations of reductive groups over finite fields*, Annals of Mathematics 103 (1976), 103–161, [Institute for Advanced Study copy](https://publications.ias.edu/sites/default/files/Number27.pdf), §§1.17–1.20, Definition 5.15, Proposition 5.16, Corollary 5.18, Theorem 6.8, Proposition 7.4 and Theorem 8.3 (printed pages 114, 131–132, 138, 141 and 147). Section 7 states these geometric comparisons without importing their proofs into the elementary classification.
- **P. Deligne and G. Lusztig**, *Duality for representations of a reductive group over a finite field*, Journal of Algebra 74 (1982), 284–291, [author's deposited article](https://publications.ias.edu/sites/default/files/Number44.pdf), §§1 and 5. Proposition 7.1 proves the rank-one parabolic character operation used in this lesson.
