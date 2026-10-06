# Representations, characters and the group determinant

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Matrices are coordinates for modules. For a finite group in characteristic zero, the simple module types can be recognized by their traces, and the same types factor the determinant of the regular representation. This lesson connects those two calculations. At the end, a trace pairing tests semisimplicity for every finite-dimensional algebra in characteristic zero.

The prerequisites are Groups with operators and Semisimple rings and Wedderburn's theorem, together with determinants and polynomial rings. Basic references are [Etingof et al.], [MIT], [Noether] and [Frobenius]. Representations are unital, and their vector spaces are finite-dimensional unless explicitly stated otherwise. The character calculations use \(\mathbb C\); the ring and averaging statements specify their more general fields.

## 1. The module behind a matrix representation

A representation of a \(k\)-algebra \(A\) on \(V\) is a \(k\)-algebra map \(A\to\operatorname{End}_k(V)\). It is equivalent to a left \(A\)-module structure on \(V\) agreeing with the given scalar action. Choosing a basis identifies the endomorphism algebra with \(M_n(k)\). A linear isomorphism \(V\to W\) intertwines the two representations exactly when it is an \(A\)-module isomorphism. In coordinates, this is simultaneous conjugacy of the representing matrices.

A subrepresentation is a submodule. **Irreducible** means simple; **indecomposable** means not a direct sum of two nonzero submodules. They are different notions, as the nilpotent two-dimensional example in the first lesson shows. Finite-dimensional modules have finite length: every strict submodule inclusion increases dimension. Thus Jordan–Hölder determines their simple composition factors, and Krull–Remak–Schmidt determines their indecomposable direct summands. These factors need not coincide unless the module is semisimple.

### Theorem 1.1. All modules over a semisimple ring

Let \(R=\prod_{i=1}^t M_{n_i}(D_i)\), with division rings \(D_i\). Every left \(R\)-module, of any cardinality, is a direct sum of simple modules. There is one simple type for each factor, namely its column module \(D_i^{n_i}\), on which the other factors act by zero. Every simple module is isomorphic to a minimal left ideal of \(R\).

**Proof.** Semisimplicity of every module was proved in Theorem 3.1 of the preceding lesson. For the type classification, the central factor identities \(c_i\) give \(M=\bigoplus_i c_iM\), and a simple module can have just one nonzero component. In \(M_n(D)\), its \(n\) column left ideals are simple, and their sum is the regular module. Every simple module is cyclic, hence a quotient of that regular module; at least one column has nonzero image in the quotient. Schur's lemma makes that column map an isomorphism.

One can also see arbitrary multiplicities concretely. Put \(e=E_{11}\), and regard \(eM\) as a left vector space over \(eRe\simeq D\). The map

\[
D^n\otimes_D eM\longrightarrow M,
\qquad (d_i)_i\otimes m\longmapsto\sum_i E_{i1}(d_i)m
\]

is well defined; here \(D^n\) has its usual right \(D\)-action, and \(E_{ij}(d)\) denotes the matrix with entry \(d\) at \((i,j)\). Its inverse is

\[
m\longmapsto\sum_i e_i\otimes E_{1i}(1)m,
\]

where \(e_i\) are the standard columns. The matrix-unit identities verify both compositions and \(R\)-linearity. A left \(D\)-basis of \(eM\) therefore gives a direct sum of copies of the column module. \(\square\)

If \(A\) is finite-dimensional over an algebraically closed field \(k\) and semisimple, the division rings in its Wedderburn decomposition equal \(k\). Indeed, every element \(d\) of such a division ring satisfies a polynomial over \(k\). Factor that polynomial into linear factors. Since a division ring has no zero divisors and the scalars commute with \(d\), one factor \(d-\lambda\) must be zero. Thus

\[
A\simeq\prod_i M_{n_i}(k),\qquad \dim_k A=\sum_i n_i^2.
\]

## 2. Averaging an arbitrary complement

For a group \(G\), its group algebra \(k[G]\) has a basis of group elements, with multiplication extended linearly. Representations \(G\to\operatorname{GL}(V)\) and modules over \(k[G]\) are equivalent: extend the group action linearly, or restrict an algebra action to the basis units.

### Theorem 2.1. Maschke's theorem

If \(G\) is finite and \(\operatorname{char}k\) does not divide \(\lvert G\rvert\), every \(k[G]\)-module is semisimple.

**Proof.** Let \(N\) be a submodule of \(M\), with no finite-dimensional assumption. Choose a \(k\)-linear projection \(p:M\to N\), using a vector-space basis extending a basis of \(N\). Define

\[
P=\frac1{\lvert G\rvert}\sum_{g\in G} gpg^{-1}.
\]

Each term has image in \(N\) and restricts to the identity on \(N\). Reindexing the sum shows that \(P\) commutes with each element of \(G\), so it is a module homomorphism. It satisfies \(P|_N=1\); hence \(P^2=P\) and \(M=N\oplus\ker P\). Complete reducibility in the first lesson gives the conclusion. \(\square\)

The characteristic restriction is necessary. If \(G\) is cyclic of order \(p\) over a field of characteristic \(p\), then

\[
k[G]\simeq k[t]/(t^p-1)=k[t]/((t-1)^p),
\]

whose nonzero ideal \((t-1)\) is nilpotent. It is not semisimple.

### Theorem 2.2. The two counting formulas

Let \(V_1,\ldots,V_t\) represent the irreducible complex representations of a finite group \(G\), with \(n_i=\dim V_i\). Then

\[
\mathbb C[G]\simeq\prod_i M_{n_i}(\mathbb C),\qquad
\lvert G\rvert=\sum_i n_i^2,
\]

and \(t\) is the number of conjugacy classes of \(G\). The left regular representation is \(\bigoplus_i V_i^{n_i}\).

**Proof.** Maschke and Wedderburn–Artin give the displayed product, and comparing dimensions gives the sum of squares. Each matrix factor has its regular module decomposed into \(n_i\) simple columns, proving the regular-representation assertion. The centre of the product has dimension \(t\). In the group basis, an element \(\sum_g a_g g\) is central exactly when \(a_g=a_{hgh^{-1}}\) for all \(g,h\). The sums over distinct conjugacy classes form a basis of the centre. Comparing its two dimensions gives the second counting formula. \(\square\)

## 3. Traces distinguish the simple types

The **character** of \(V\) is \(\chi_V(g)=\operatorname{Tr}(\rho_V(g))\). It is constant on conjugacy classes, additive on direct sums, and multiplicative on tensor products. These statements follow respectively from similarity invariance of trace, block-diagonal matrices, and \(\operatorname{Tr}(A\otimes B)=\operatorname{Tr}(A)\operatorname{Tr}(B)\).

Since each \(g\) has finite order, its eigenvalues over \(\mathbb C\) are roots of unity and it is diagonalizable: \(t^m-1\) has distinct roots in characteristic zero. Consequently

\[
\chi_V(g^{-1})=\overline{\chi_V(g)}.
\]

For class functions, use the inner product

\[
\langle f,h\rangle=\frac1{\lvert G\rvert}\sum_{g\in G} f(g)\overline{h(g)}.
\]

### Theorem 3.1. Orthogonality and character determination

For finite-dimensional complex representations \(V,W\),

\[
\langle\chi_W,\chi_V\rangle=\dim_{\mathbb C}\operatorname{Hom}_G(V,W).
\]

The irreducible characters form an orthonormal basis of class functions. The multiplicity of \(V_i\) in \(V\) is \(\langle\chi_V,\chi_i\rangle\), and equal characters give isomorphic representations.

**Proof.** Let \(G\) act on \(\operatorname{Hom}_{\mathbb C}(V,W)\) by \(T\mapsto\rho_W(g)T\rho_V(g^{-1})\). The average \(P\) of these operators is a projection onto the invariant subspace, which is exactly \(\operatorname{Hom}_G(V,W)\). A projection has trace equal to its image dimension. The trace of \(T\mapsto BTA\) on a matrix space is \(\operatorname{Tr}(B)\operatorname{Tr}(A)\): on the basis matrix \(E_{ab}\), its coefficient at that same basis vector is \(B_{aa}A_{bb}\). Summing the coefficients and then averaging over \(G\) gives the displayed formula.

Schur's lemma makes this Hom dimension one for equal irreducible types and zero for distinct types. Hence the irreducible characters are orthonormal and linearly independent. Their number equals the dimension of class functions by Theorem 2.2, so they are a basis. Maschke writes \(V\) as \(\bigoplus_i V_i^{m_i}\); taking inner products recovers each \(m_i\). Equal characters recover equal multiplicities and therefore isomorphic modules. \(\square\)

There are two useful refinements. For representatives \(g,h\) of conjugacy classes, expansion of the indicator function of the class of \(h\) in this orthonormal basis gives **column orthogonality**:

\[
\sum_i\chi_i(g)\overline{\chi_i(h)}=
\begin{cases}
\lvert C_G(g)\rvert,&g\text{ is conjugate to }h,\\
0,&\text{otherwise}.
\end{cases}
\]

Indeed, the inner product of that indicator with \(\chi_i\) is \(\lvert\operatorname{Cl}(h)\rvert\overline{\chi_i(h)}/\lvert G\rvert\), and \(\lvert G\rvert/\lvert\operatorname{Cl}(h)\rvert=\lvert C_G(h)\rvert\). This proves the formula, including its normalization.

For irreducibles \(\rho_i,\rho_j\), the same average on matrices is zero if \(i\ne j\). If \(i=j\), it is a scalar matrix by Schur, and preservation of trace makes it \(\operatorname{Tr}(T)I/n_i\). Taking \(T\) to be a matrix unit gives **matrix-coefficient orthogonality**:

\[
\frac1{\lvert G\rvert}\sum_g
\rho_i(g)_{ab}\rho_j(g^{-1})_{cd}
=\frac{\delta_{ij}}{n_i}\delta_{ad}\delta_{bc}.
\]

### Proposition 3.2. Central idempotents from characters

The identity of the \(i\)-th simple factor in \(\mathbb C[G]\) is

\[
e_i=\frac{n_i}{\lvert G\rvert}\sum_{g\in G}\chi_i(g^{-1})g.
\]

**Proof.** Its coefficients are constant on conjugacy classes, so it is central. On \(V_j\) it acts by a scalar \(\lambda_j\), by Schur's lemma. Taking traces gives

\[
n_j\lambda_j=\frac{n_i}{\lvert G\rvert}\sum_g\chi_i(g^{-1})\chi_j(g)=n_i\delta_{ij}.
\]

Thus its action is the identity on \(V_i\) and zero on every other simple type. The faithful Wedderburn product identifies it with the claimed factor identity. In particular \(e_i^2=e_i\), \(e_ie_j=0\) for \(i\ne j\), and \(\sum_i e_i=1\). \(\square\)

Character determination also holds for finite-dimensional modules over any finite-dimensional semisimple algebra \(A\) over a characteristic-zero field \(k\), with the character defined on all of \(A\) by \(a\mapsto\operatorname{Tr}_k(a|_V)\). To prove it, evaluate at the central factor identities. If \(S_i\) is the simple type of that factor, then

\[
\chi_V(e_i)=m_i\dim_k S_i.
\]

The positive integer \(\dim_k S_i\) is nonzero in \(k\), so this determines \(m_i\). In a nonsemisimple algebra traces may determine only the composition factors. On \(k[t]/(t^2)\), the two-dimensional regular module and the sum of two copies of \(k[t]/(t)\) both have character \(a+bt\mapsto2a\); they are not isomorphic, since \(t\) acts nontrivially on the former and trivially on the latter.

## 4. Factoring the determinant of the regular action

Introduce one variable \(x_g\) for each \(g\in G\). The **group determinant** is

\[
\Theta_G(x)=\det\left(\sum_g x_g\rho_{\mathrm{reg}}(g)\right).
\]

With group elements indexing rows and columns, the matrix entry at \((h,k)\) is \(x_{hk^{-1}}\). This fixes the left-regular convention.

### Lemma 4.1. A generic matrix determinant is irreducible

For every field \(k\), the determinant of an \(n\times n\) matrix of independent variables is irreducible in \(k[x_{ij}]\), for \(n\geq1\).

**Proof.** Suppose \(\det(x_{ij})=fg\), with nonzero factors. Grade polynomials by the degree in one chosen row. The determinant is homogeneous of degree one in that row. In a domain, the lowest and highest nonzero homogeneous pieces of a product are the products of the corresponding extreme pieces. Thus their degrees cannot cancel. The difference between highest and lowest degrees for the product is the sum of those differences for the factors. Here it is zero. Therefore \(f\) and \(g\) are each homogeneous in that row, of degrees zero and one in some order. Repeat for every row and every column.

Let \(I\) be the rows of degree one in \(f\), and \(J\) its columns of degree one. The other rows and columns have degree zero in \(f\) and degree one in \(g\). If both factors are nonconstant, \(I\) is a nonempty proper row set and \(J\) is a nonempty proper column set. A polynomial of degree zero in a row or column cannot involve its variables. Choose \(i\in I\) and \(j\notin J\). The variable \(x_{ij}\) occurs in neither factor: its column excludes it from \(f\), and its row excludes it from \(g\). But the determinant contains a permutation monomial using \(x_{ij}\), with coefficient \(1\) or \(-1\), so it depends on that variable. This is a contradiction. Hence one factor is constant. For \(n=1\), the single variable is irreducible directly. \(\square\)

### Theorem 4.2. Frobenius's factorization

For the irreducibles of a finite group over \(\mathbb C\), define

\[
\Phi_i(x)=\det\left(\sum_g x_g\rho_i(g)\right).
\]

Then

\[
\Theta_G(x)=\prod_i\Phi_i(x)^{n_i}.
\]

Each \(\Phi_i\) is irreducible, homogeneous of degree \(n_i\), and no two are associates.

**Proof.** The regular module is \(\bigoplus_i V_i^{n_i}\). A basis adapted to this decomposition makes its generic action block diagonal, with the \(i\)-th block repeated \(n_i\) times. Taking determinants proves the product with precisely these exponents.

For irreducibility, the linear map

\[
\mathbb C[G]\longrightarrow\bigoplus_i M_{n_i}(\mathbb C),
\qquad a\longmapsto(\rho_i(a))_i,
\]

is a vector-space isomorphism by Wedderburn–Artin. Change the \(\lvert G\rvert\) independent coordinates \(x_g\) to the individual entries \(y_{i,ab}\) of these matrix factors. This is an invertible linear change of polynomial variables. In the new variables, \(\Phi_i\) is a generic determinant in the \(i\)-th block, so Lemma 4.1 proves irreducibility. It remains irreducible after adjoining the other independent variables: the quotient by its prime ideal is still a polynomial ring over a domain. The polynomial rings here are unique factorization domains, so irreducible elements generate prime ideals.

The determinants for different blocks cannot be scalar multiples. Set one block to a singular matrix and a different block to the identity; its determinant is then zero while the other's is one. This also proves the nonassociation assertion after the inverse coordinate change. Homogeneity and the degree follow from the determinant formula. \(\square\)

**A cyclic group of order three.** Let its generator be \(r\), and put \(\omega=\exp(2\pi\mathrm i/3)\). Its three irreducibles are the characters \(r\mapsto1,\omega,\omega^2\), giving

\[
\Theta_{C_3}(x)=\prod_{j=0}^2(x_1+\omega^j x_r+\omega^{2j}x_{r^2}).
\]

The product is \(x_1^3+x_r^3+x_{r^2}^3-3x_1x_rx_{r^2}\).

**The symmetric group on three letters.** The conjugacy classes have sizes \(1,3,2\), represented by \(1,s,r\). The two linear representations and the two-dimensional matrices from the preceding lesson give the character table:

| Representation | \(1\) | \(s\) | \(r\) |
|---|---:|---:|---:|
| Trivial | \(1\) | \(1\) | \(1\) |
| Sign | \(1\) | \(-1\) | \(1\) |
| Two-dimensional | \(2\) | \(0\) | \(-1\) |

For variables \(a_0,a_1,a_2\) on \(1,r,r^2\) and \(b_0,b_1,b_2\) on \(s,sr,sr^2\), set \(A=a_0+a_1+a_2\), \(B=b_0+b_1+b_2\). The two linear determinant factors are \(A+B\) and \(A-B\). Using the same two-dimensional matrices gives

\[
\begin{aligned}
Q={}&a_0^2+a_1^2+a_2^2-a_0a_1-a_0a_2-a_1a_2\\
&-b_0^2-b_1^2-b_2^2+b_0b_1+b_0b_2+b_1b_2.
\end{aligned}
\]

Thus \(\Theta_{S_3}=(A+B)(A-B)Q^2\). Theorem 4.2 proves that \(Q\) is irreducible over \(\mathbb C\), even though this quadratic has a large radical as a quadratic form in six variables: after the matrix-coordinate change it is the determinant of four independent entries. Its exponent two is the multiplicity of the two-dimensional representation in the regular module.

## 5. A trace test for semisimplicity

For a finite-dimensional \(k\)-algebra \(A\), write \(L_a\) for left multiplication by \(a\), and define

\[
T(a)=\operatorname{Tr}_k(L_a),\qquad B(a,b)=T(ab).
\]

The form is symmetric because \(\operatorname{Tr}(L_aL_b)=\operatorname{Tr}(L_bL_a)\). In a basis \(a_1,\ldots,a_d\), its **discriminant** is the determinant of \((B(a_i,a_j))\). Changing basis multiplies this determinant by the square of the basis-change determinant, so its vanishing is independent of the basis.

### Theorem 5.1. The regular trace criterion

If \(\operatorname{char}k=0\), a finite-dimensional \(k\)-algebra is semisimple if and only if its regular trace form is nondegenerate.

**Proof.** The algebra is Artinian, so its Jacobson radical \(J\) is nilpotent. For \(x\in J\) and \(y\in A\), the product \(xy\) belongs to \(J\) and is nilpotent. Thus \(L_{xy}\) is nilpotent and has trace zero. Hence \(J\) is contained in the radical of \(B\). Nondegeneracy implies \(J=0\), and Wedderburn–Artin makes \(A\) semisimple.

Conversely, on a simple factor \(A_i\), the radical \(N_i\) of its trace pairing is a two-sided ideal. For \(x\in N_i\), the identity \(T(ax y)=T(x y a)\) gives closure under left multiplication, while \(T(xa y)=0\) gives closure under right multiplication. Simplicity makes \(N_i\) either zero or the entire factor. But

\[
B(1,1)=\dim_k A_i\ne0
\]

in characteristic zero, so it is not the entire factor. The pairing on each factor is nondegenerate. The product decomposition of \(A\) is orthogonal for \(B\), because products between distinct factors vanish and the regular trace restricts to the trace of each factor. Therefore the whole pairing is nondegenerate. \(\square\)

For \(A=M_n(k)\), left multiplication acts identically on the \(n\) column spaces, so \(T(a)=n\operatorname{tr}(a)\). In characteristic \(p\), the regular trace on \(M_p(k)\) is identically zero although the algebra is simple. The ordinary matrix trace, which is its reduced trace, still gives a nondegenerate pairing: \(\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}\). This explains why regular and reduced trace must be distinguished in positive characteristic. For arbitrary imperfect fields, even the existence of a suitable reduced trace requires attention to the centre and separability; the characteristic-zero criterion above makes none of those extra claims.

## 6. Exercises

### Exercise 6.1. Easy: four cyclic characters

Compute the character table of a cyclic group generated by \(z\) with \(z^4=1\), and verify all row inner products.

### Exercise 6.2. Medium: the symmetric-group table

Recover the character table of \(S_3\) from its algebra decomposition. Use the class sizes to check all row inner products and all column norms. Decompose the permutation representation on three letters and the tensor square of its two-dimensional irreducible.

### Exercise 6.3. Medium: two abelian group determinants

Verify the order-three determinant directly. For \(G=\{1,a,b,ab\}\) with \(a^2=b^2=1\) and \(ab=ba\), give all four determinant factors and their product formula.

### Exercise 6.4. Medium: the positive-characteristic trace

Calculate the regular trace pairing on \(M_p(\mathbb F_p)\), and exhibit an explicit dual basis for its reduced trace pairing. Explain exactly which step of Theorem 5.1 would fail if one used regular trace in this case.

### Exercise 6.5. Hard: irreducibility without a geometry argument

Supply the grading argument in Lemma 4.1 for a polynomial factorization in every row and column, including the justification that the extreme pieces cannot cancel. Then use the full Wedderburn coordinate change to prove irreducibility and nonassociation of the \(\Phi_i\), not just the product formula for \(\Theta_G\).

## 7. Solutions

### Solution 6.1

The four characters are \(\chi_j(z^a)=\mathrm i^{ja}\), for \(j,a=0,1,2,3\). Their rows are

\[
(1,1,1,1),\quad(1,\mathrm i,-1,-\mathrm i),\quad
(1,-1,1,-1),\quad(1,-\mathrm i,-1,\mathrm i).
\]

The inner product of rows \(j,l\) is \(\frac14\sum_{a=0}^3\mathrm i^{(j-l)a}\). It equals one when \(j=l\). Otherwise the ratio is a nontrivial fourth root of unity, and the geometric sum is zero. The four one-dimensional types exhaust the irreducibles, either by the cyclic algebra decomposition or by the sum-of-squares formula.

### Solution 6.2

The two field factors give the trivial and sign lines. On the matrix factor, identity has trace two, \(\rho(s)\) has trace zero, and \(\rho(r)\) has trace minus one. This gives the displayed table. The row norms are \((1+3+2)/6=1\), \((1+3+2)/6=1\), and \((4+0+2)/6=1\). The cross inner products have numerators \(1-3+2=0\), \(2+0-2=0\), and \(2+0-2=0\). Column norms are \(1+1+4=6\), \(1+1+0=2\), and \(1+1+1=3\), agreeing with the centralizer orders of \(1,s,r\); cross-column inner products are zero.

The permutation representation has character \((3,1,0)\), by counting fixed letters. This is the sum of the trivial character and \((2,0,-1)\), so the representation is a trivial line plus the two-dimensional type. The tensor square has character \((4,0,1)\). It equals the sum of the trivial, sign and two-dimensional characters. Character determination gives

\[
V\otimes V\simeq\mathbf1\oplus\operatorname{sgn}\oplus V.
\]

### Solution 6.3

For order three the regular matrix is

\[
\begin{pmatrix}x_1&x_{r^2}&x_r\\x_r&x_1&x_{r^2}\\x_{r^2}&x_r&x_1\end{pmatrix}.
\]

Expansion gives \(x_1^3+x_r^3+x_{r^2}^3-3x_1x_rx_{r^2}\). Factoring with the three Fourier characters gives the product in Section 4. For the four-element group, a character is determined by independent choices \(\epsilon,\eta\in\{1,-1\}\) for its values on \(a,b\). Its value on \(ab\) is \(\epsilon\eta\). Thus

\[
\Theta_G=\prod_{\epsilon,\eta\in\{1,-1\}}
(x_1+\epsilon x_a+\eta x_b+\epsilon\eta x_{ab}).
\]

Each factor has degree one and occurs once. These four characters exhaust the group-algebra factors because their degree squares already sum to four.

### Solution 6.4

There are \(p\) columns, and left multiplication by \(x\) acts on each by the matrix \(x\). Hence \(T(x)=p\operatorname{tr}(x)=0\) in \(\mathbb F_p\), and \(B(x,y)=0\) for all \(x,y\). Nevertheless, \(M_p(\mathbb F_p)\) is simple by the matrix-unit argument in the preceding lesson. For the reduced trace \(\operatorname{tr}\), the dual of \(E_{ij}\) is \(E_{ji}\): the product formula gives \(\operatorname{tr}(E_{ij}E_{lk})=\delta_{jl}\delta_{ik}\). The simple-factor proof of Theorem 5.1 used \(B(1,1)=\dim_k A_i\ne0\) to exclude a wholly radical pairing. Here \(\dim_k A_i=p^2=0\) as a scalar in the field, and in fact the entire regular trace vanishes. Simplicity alone therefore does not rescue that argument in positive characteristic.

### Solution 6.5

Fix a row and write \(f=\sum_{a=r}^s f_a\), \(g=\sum_{b=u}^v g_b\), where the endpoint homogeneous pieces are nonzero. The pieces of the product in degrees \(r+u\) and \(s+v\) are respectively \(f_rg_u\) and \(f_sg_v\), with no other contributions at those degrees. They are nonzero because the polynomial ring is a domain. Homogeneity of the determinant gives \(r+u=s+v=1\), so \((s-r)+(v-u)=0\). Both terms are nonnegative, hence zero. Thus the factors are homogeneous for this row and have degrees zero and one in some order. Apply this to every row and column. If both are nonconstant, choose a row assigned to \(f\) and a column assigned to \(g\). Their intersecting variable occurs in neither factor but occurs in the determinant, a contradiction. This proves generic determinant irreducibility, including all fields.

The representation map from the group algebra to the product of its full matrix factors is an isomorphism, so its entries are a full independent coordinate system, not just a set of selected linear forms. It induces an automorphism of the polynomial ring on \(\lvert G\rvert\) variables. In these coordinates each \(\Phi_i\) is precisely a generic determinant in its own block. Its irreducibility remains after adjoining the remaining variables because its quotient ring is a domain. Two such determinants are not associates, since one can vanish while the other equals one. Apply the inverse polynomial automorphism to recover irreducibility and nonassociation in the original \(x_g\) variables. Combined with the regular-module decomposition, this proves every part of Frobenius's factorization theorem.

## What this lesson does not prove

The theory of Schur indices and minimal splitting fields over non-algebraically-closed fields is not developed here. A simple factor over such a field can involve a noncommutative division ring, as explained by Wedderburn–Artin. Brauer and Noether's work on minimal splitting fields is a historical reference, rather than an additional theorem used in these proofs. The general reduced trace for central simple algebras belongs to the next lesson. All six central results of this lesson, including generic determinant irreducibility and the characteristic-zero trace criterion, have been proved.

## References

- **[Etingof et al.]** Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob and Elena Yudovina, *Introduction to Representation Theory*, 2011 revision, especially §§3.1–3.8. [arXiv:0901.0827](https://arxiv.org/abs/0901.0827).
- **[MIT]** *Noncommutative Algebra*, MIT OpenCourseWare, Spring 2023, instructor Roman Bezrukavnikov, lectures 1–3. [Course notes](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/resources/mit18_706_s23_full_lec_pdf/).
- **[Noether]** Emmy Noether, *Hyperkomplexe Größen und Darstellungstheorie*, written up by B. L. van der Waerden, *Mathematische Zeitschrift* **30** (1929), 641–692, §§15–26, especially §25 for the discriminant viewpoint.
- **[Frobenius]** Ferdinand Georg Frobenius, *Über die Darstellung der endlichen Gruppen durch lineare Substitutionen*, *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin* (1897), 994–1015; and *Theorie der hyperkomplexen Größen*, the same proceedings (1903), 504–537.
- **[Brauer–Noether]** Richard Brauer and Emmy Noether, *Über minimale Zerfällungskörper irreduzibler Darstellungen*, *Sitzungsberichte der Preussischen Akademie der Wissenschaften* (1927), 221–228.
