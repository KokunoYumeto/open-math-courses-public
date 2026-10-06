# Characters and the orthogonality relations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Elementary prerequisite proofs and source comparisons by GPT-6 Astra (OpenAI), in Codex, Ultra. Each AI self-checked its own contributions; no independent human review is claimed. The independently authored lesson text is dedicated under CC0.*

A representation assigns a matrix to every group element. Can its traces retain enough information to identify the representation? For a finite group over the complex numbers, the answer is yes. Traces also turn decomposition into a calculation with functions: an inner product gives the number of copies of each irreducible representation.

This lesson develops that calculation, proves the two orthogonality relations, and constructs several small character tables. We then use the tables to detect kernels, normal subgroups and central elements. Begin with [Representations and complete reducibility](RT-FIN-01.md): [Proposition 2.1](RT-FIN-01.md#proposition-2-1) supplies invariant Hermitian forms, [Theorem 2.3](RT-FIN-01.md#theorem-2-3) supplies complete reducibility, and [Theorem 3.1](RT-FIN-01.md#theorem-3-1) supplies Schur's lemma. Throughout the character-theory sections, \(G\) is finite and every representation is finite-dimensional over \(\mathbb C\). The zero representation is allowed; an irreducible representation is nonzero.

For further reading, the free notes [Etingof et al.] and the author draft [Gruson–Serganova] treat characters and orthogonality; [Milne] treats group actions. [Frobenius] gives a historical treatment. The exposition and exercises below supply the arguments used in this lesson. The abelian viewpoint continues in Fourier analysis on finite abelian groups. An algebraic treatment, including the group determinant, appears in Representations, characters and the group determinant.

## 0. Three tools behind the character calculation

We first explain why traces respect a change of coordinates, why finite-order complex matrices can be diagonalized, and why centralizer orders measure conjugacy classes. The linear-algebra starting proofs are [Lemma 0.1 and Lemma 0.2 of the preceding lesson](RT-FIN-01.md#lemma-0-1), together with the programme's finite-dimensional Hermitian spaces.

**Lemma 0.1 (trace and projections).** For an \(a\)-by-\(b\) matrix \(A\) and a \(b\)-by-\(a\) matrix \(B\) over a field \(k\),
\[
\operatorname{tr}(AB)=\operatorname{tr}(BA).
\]
Consequently the trace of an endomorphism of a finite-dimensional space is independent of the chosen basis. If \(P^2=P\), then its trace is \(\dim(\operatorname{im}P)\cdot1_k\); over \(\mathbb C\) this is its rank as an ordinary nonnegative integer.

*Proof.* By the definition of matrix multiplication,
\[
\operatorname{tr}(AB)=\sum_{i=1}^a\sum_{j=1}^b A_{ij}B_{ji}
=\sum_{j=1}^b\sum_{i=1}^a B_{ji}A_{ij}=\operatorname{tr}(BA).
\]
For an invertible change-of-basis matrix \(S\), apply this identity to \(S^{-1}T\) and \(S\); it gives \(\operatorname{tr}(S^{-1}TS)=\operatorname{tr}T\). If \(P^2=P\), every vector has the expression \(v=Pv+(v-Pv)\), with the two terms in \(\operatorname{im}P\) and \(\ker P\). Their intersection is zero because \(P\) is the identity on its image. Choose bases of these two spaces and concatenate them. In that basis \(P\) is the identity on the first block and zero on the second, proving the trace formula. ∎

**Lemma 0.2 (distinct roots give eigenspace projections).** Let \(T:V\to V\) be linear over any field \(k\), and let
\[
p(t)=\prod_{j=1}^{s}(t-\lambda_j),\qquad \lambda_j\in k,
\]
where \(s\geq1\) and the \(\lambda_j\) are distinct. If \(p(T)=0\), then
\[
V=\bigoplus_{j=1}^{s}\ker(T-\lambda_j I).
\]
The projections are the explicitly defined operators
\[
E_j=\prod_{\ell\ne j}\frac{T-\lambda_\ell I}{\lambda_j-\lambda_\ell}.
\]
No finite-dimensional assumption is needed for this direct-sum formula. In finite dimension it supplies a basis in which \(T\) is diagonal.

*Proof.* Put \(q_j(t)=\prod_{\ell\ne j}(t-\lambda_\ell)/(\lambda_j-\lambda_\ell)\). Then \(q_j(\lambda_i)=\delta_{ji}\). A polynomial of degree at most \(s-1\) with \(s\) distinct roots is zero: if \(f(a)=0\), the identities \(t^n-a^n=(t-a)\sum_{r=0}^{n-1}t^{n-1-r}a^r\) show that \(t-a\) divides \(f\); successive distinct roots successively factor out, until a nonzero polynomial would have degree at least the number of roots. Apply this to \(\sum_jq_j-1\) to obtain \(\sum_jq_j=1\).

Moreover, \((t-\lambda_j)q_j(t)\) is a nonzero constant multiple of \(p(t)\). Hence \((T-\lambda_j I)E_j=0\), while \(\sum_jE_j=I\). Every vector is therefore a sum of vectors in the stated eigenspaces. On an eigenvector with eigenvalue \(\lambda_i\), \(E_j\) acts as multiplication by \(q_j(\lambda_i)=\delta_{ji}\). Applying \(E_j\) to any relation between these eigenspaces makes its \(j\)-th term zero, so the sum is direct. This also proves that the displayed operators are its projections. In finite dimension, concatenate bases of the eigenspaces. ∎

**Corollary 0.3 (finite order over the complex numbers).** If \(T\) is a complex linear operator with \(T^m=I\), where \(m\geq1\), then
\[
V=\bigoplus_{j=0}^{m-1}\ker(T-\zeta^j I),\qquad
\zeta=e^{2\pi i/m}.
\]
In particular, every finite-order complex matrix is diagonalizable and its eigenvalues have modulus one.

*Proof.* The complex exponential and the circle, Theorem 4 and worked Exercise 3, proves that \(\zeta^j\), \(0\leq j<m\), are precisely the distinct roots of \(t^m-1\). Equivalently, the exponential addition law and its exact kernel \(2\pi i\mathbb Z\) give these \(m\) distinct roots; repeated use of the factor argument in Lemma 0.2 factors the monic degree-\(m\) polynomial as their product. Apply that lemma. If \(\lambda^m=1\), then \(|\lambda|^m=1\), hence \(|\lambda|=1\). ∎

The distinct-root hypothesis cannot be dropped. Over a field of characteristic \(p>0\), the matrix
\[
J=\begin{pmatrix}1&1\\0&1\end{pmatrix}=I+N
\]
has \(N^2=0\), so induction gives \(J^r=I+rN\) and \(J^p=I\). Its only eigenvalue is \(1\), but its eigenspace has dimension one, so it is not diagonalizable. Likewise, a polynomial that does not split over the field need not give diagonalization there: over \(\mathbb R\), the quarter-turn matrix \(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) has fourth power \(I\) and no real eigenvalue, since its eigenvalue equation is \(t^2+1=0\).

**Lemma 0.4 (orbit–stabilizer).** For an action of any group \(G\) on a set and any point \(x\), write \(G_x=\{g:gx=x\}\). The map
\[
G/G_x\longrightarrow Gx,\qquad gG_x\longmapsto gx
\]
is a bijection. If \(G\) is finite, then
\[
|Gx|=[G:G_x]=\frac{|G|}{|G_x|}.
\]
For conjugation, \(G_x=C_G(x)\), so the class of \(x\) has size \(|G|/|C_G(x)|\).

*Proof.* The identity fixes \(x\), and products and inverses of elements fixing \(x\) also fix it, so \(G_x\) is a subgroup. The equivalence
\(gx=hx\Longleftrightarrow h^{-1}g\in G_x\Longleftrightarrow gG_x=hG_x\)
proves that the displayed map is well defined and injective. Every element of the orbit is \(gx\), so it is surjective. Left cosets partition \(G\), and multiplication by \(g\) bijects \(G_x\) with \(gG_x\). Counting this partition proves the finite formula. In the conjugation action, fixing \(x\) means \(gxg^{-1}=x\), equivalently \(gx=xg\). ∎

## 1. What a trace can tell us

For a representation \(\rho:G\to\operatorname{GL}(V)\), its **character** is

\[
\chi_V(g)=\operatorname{tr}(\rho(g)).
\]

Trace is independent of the basis by Lemma 0.1. Equivalent representations have the same character, since their matrices are conjugate by one invertible matrix. The converse will require a theorem.

**Proposition 1.1 (trace identities).** A character is constant on conjugacy classes, and

\[
\chi_V(1)=\dim V,\qquad
\chi_{V\oplus W}=\chi_V+\chi_W,\qquad
\chi_V(g^{-1})=\overline{\chi_V(g)},\qquad
\chi_{V^*}(g)=\overline{\chi_V(g)}.
\]

Also \(|\chi_V(g)|\leq\dim V\). If \(g\) has order \(m\), its character value is a sum of \(\dim V\) roots of unity of order dividing \(m\).

*Proof.* The equality
\(\rho(hgh^{-1})=\rho(h)\rho(g)\rho(h)^{-1}\)
gives constancy on conjugacy classes. The identity matrix has trace \(\dim V\); a block diagonal matrix has the sum of the traces of its blocks.

The operator \(\rho(g)\) satisfies \(\rho(g)^m=I\). Corollary 0.3 diagonalizes it, with eigenvalues \(\lambda_1,\ldots,\lambda_d\) satisfying \(\lambda_j^m=1\). Thus \(\chi_V(g)=\sum_j\lambda_j\), and \(|\chi_V(g)|\leq d\). The inverse has eigenvalues \(\lambda_j^{-1}=\overline{\lambda_j}\). Finally the dual action is \(\rho_{V^*}(g)=\rho(g^{-1})^{\mathsf T}\), whose trace is \(\chi_V(g^{-1})\). ∎

A function constant on conjugacy classes is called a **class function**. Write \(\operatorname{CF}(G)\) for their complex vector space. If the conjugacy classes are \(K_1,\ldots,K_c\), their indicator functions form a basis: a class function is determined by one arbitrary value on each class. In particular, \(\dim\operatorname{CF}(G)=c\).

We use the Hermitian inner product, linear in its first variable,

\[
\langle f,h\rangle=\frac1{|G|}\sum_{g\in G}f(g)\overline{h(g)}.
\tag{1.1}
\]

For representatives \(g_a\in K_a\), this becomes

\[
\langle f,h\rangle=\frac1{|G|}\sum_{a=1}^c |K_a|f(g_a)\overline{h(g_a)}.
\tag{1.2}
\]

The class sizes are weights, not optional factors.

**Example 1.2 (fixed points and the regular trace).** If \(G\) acts on a finite set \(X\), let \(\mathbb C[X]\) have basis \(e_x\), with \(g e_x=e_{gx}\). The diagonal entry at \(e_x\) is \(1\) exactly when \(gx=x\), so

\[
\chi_{\mathbb C[X]}(g)=|\{x\in X:gx=x\}|.
\]

For left multiplication on \(G\), \(gx=x\) forces \(g=1\). The **left regular representation** \(R=\mathbb C[G]\) therefore has

\[
\chi_R(g)=
\begin{cases}|G|,&g=1,\\0,&g\ne1.\end{cases}
\tag{1.3}
\]

This elementary trace will eventually list every irreducible representation, with its multiplicity.

## 2. Averaging turns matrix entries into orthogonal functions

Choose one representative of each irreducible isomorphism class, an invariant positive definite Hermitian form on it, and an orthonormal basis. Its matrices are unitary. For entries, the row index comes first: \(\rho(g)e_j=\sum_i\rho_{ij}(g)e_i\).

**Theorem 2.1 (Schur orthogonality for matrix coefficients).** For inequivalent irreducible unitary representations \(\rho,\sigma\),

\[
\sum_{g\in G}\rho_{ij}(g)\overline{\sigma_{kl}(g)}=0.
\]

For one irreducible representation \(\rho\) of dimension \(d\), in the same chosen basis on both sides,

\[
\sum_{g\in G}\rho_{ij}(g)\overline{\rho_{kl}(g)}
=\frac{|G|}{d}\delta_{ik}\delta_{jl}.
\tag{2.1}
\]

*Proof.* Given a linear map \(A:W\to V\), where \(W\) carries \(\sigma\) and \(V\) carries \(\rho\), put

\[
\mathcal P(A)=\frac1{|G|}\sum_{g\in G}\rho(g)A\sigma(g)^{-1}.
\]

For \(h\in G\), reindexing by \(g\mapsto hg\) gives

\[
\rho(h)\mathcal P(A)\sigma(h)^{-1}=\mathcal P(A).
\]

Thus \(\mathcal P(A)\) intertwines the two representations. Schur's lemma makes it zero when they are inequivalent. When \(\sigma=\rho\), it is a scalar multiple of the identity. Conjugation preserves trace, so in that case

\[
\mathcal P(A)=\frac{\operatorname{tr}A}{d}I.
\]

Take the matrix unit \(A=E_{jl}\), sending the \(l\)-th basis vector of \(W\) to the \(j\)-th basis vector of \(V\). The \((i,k)\) entry of the summand is

\[
\rho_{ij}(g)(\sigma(g)^{-1})_{lk}
=\rho_{ij}(g)\overline{\sigma_{kl}(g)},
\]

using unitarity. For equal representations \(\operatorname{tr}E_{jl}=\delta_{jl}\); taking the \((i,k)\) entry gives (2.1). ∎

The equal-representation formula concerns the same matrices. Equivalent representations written in unrelated bases need a change of basis before the Kronecker deltas take this form. The vanishing assertion is independent of that choice.

**Corollary 2.2 (row orthogonality).** Characters of pairwise inequivalent irreducible representations satisfy

\[
\langle\chi_i,\chi_j\rangle=\delta_{ij}.
\tag{2.2}
\]

*Proof.* Expand each trace into its diagonal entries and apply Theorem 2.1. For different representations every term vanishes. For a representation of dimension \(d\), the terms indexed by diagonal positions \(a,b\) contribute \(\delta_{ab}/d\). Summing gives \(d/d=1\). ∎

There are only finitely many irreducible isomorphism classes: their orthonormal characters are linearly independent in the finite-dimensional space \(\operatorname{CF}(G)\). Denote them by \(V_1,\ldots,V_r\), with characters \(\chi_1,\ldots,\chi_r\) and dimensions \(d_i\). We choose \(V_1\) to be the trivial representation, so \(\chi_1=1\).

**Proposition 2.3 (the inner product counts intertwining maps).** For any \(V,W\),

\[
\langle\chi_V,\chi_W\rangle=\dim\operatorname{Hom}_G(W,V).
\tag{2.3}
\]

In particular this inner product is a nonnegative integer, and

\[
\dim V^G=\frac1{|G|}\sum_{g\in G}\chi_V(g).
\]

*Proof.* On \(\operatorname{Hom}_{\mathbb C}(W,V)\), the averaging operator \(\mathcal P\) just used has image \(\operatorname{Hom}_G(W,V)\). It fixes every intertwiner, so \(\mathcal P^2=\mathcal P\), and Lemma 0.1 makes its trace the dimension of its image.

For matrices \(B,C\), the operator \(A\mapsto BAC\) on rectangular matrices has trace \((\operatorname{tr}B)(\operatorname{tr}C)\). Indeed, the coefficient of \(E_{ab}\) in \(BE_{ab}C\) is \(B_{aa}C_{bb}\), and summing these diagonal coefficients proves the identity. Consequently

\[
\operatorname{tr}\mathcal P
=\frac1{|G|}\sum_g\chi_V(g)\chi_W(g^{-1})
=\langle\chi_V,\chi_W\rangle.
\]

For \(W\) trivial, an intertwiner is determined by the image of \(1\), which can be any fixed vector. ∎

## 3. Extracting the irreducible pieces

**Theorem 3.1 (multiplicities and character determination).** Every representation has a decomposition

\[
V\simeq\bigoplus_{i=1}^r V_i^{\oplus m_i},\qquad
m_i=\langle\chi_V,\chi_i\rangle\in\mathbb Z_{\geq0}.
\tag{3.1}
\]

Furthermore,

\[
\langle\chi_V,\chi_V\rangle=\sum_i m_i^2.
\tag{3.2}
\]

Thus \(V\) is irreducible exactly when its character has norm squared \(1\), and two representations are isomorphic exactly when their characters agree.

*Proof.* Complete reducibility gives some decomposition with nonnegative integer multiplicities. Additivity of trace gives \(\chi_V=\sum_i m_i\chi_i\). Taking the inner product with \(\chi_j\) and using row orthogonality recovers \(m_j\). Applying orthogonality to both sums gives (3.2). A sum of squares of nonnegative integers is \(1\) precisely when one multiplicity is \(1\) and the others vanish. Equal characters give equal multiplicities and hence isomorphic direct sums; the reverse implication follows from trace invariance. ∎

The hypothesis that we are taking the character of a representation matters. A class function of norm \(1\) need not be a character. More precisely, completeness below will show that a class function is a character exactly when all its irreducible-character coefficients are nonnegative integers.

**Theorem 3.2 (regular multiplicities).** As a representation of \(G\),

\[
\mathbb C[G]\simeq\bigoplus_{i=1}^r V_i^{\oplus d_i},\qquad
\sum_{i=1}^r d_i^2=|G|.
\tag{3.3}
\]

*Proof.* Equations (1.3) and (3.1) give

\[
m_i(R)=\frac1{|G|}|G|\overline{\chi_i(1)}=d_i.
\]

Every \(d_i\) is positive, so every irreducible occurs. Comparing dimensions gives the sum of squares. ∎

This is a statement about the left regular representation. The corresponding decomposition of the group algebra into matrix algebras is developed in [The group algebra and Fourier analysis on a finite group](RT-FIN-03.md).

Characters can also locate the pieces inside \(V\). Define its **\(i\)-th isotypic component** to be the sum of all irreducible subrepresentations isomorphic to \(V_i\).

**Proposition 3.3 (isotypic projection).** For a representation \(\rho\) on \(V\),

\[
P_i=\frac{d_i}{|G|}\sum_{g\in G}\overline{\chi_i(g)}\rho(g)
\tag{3.4}
\]

is the projection onto the \(i\)-th isotypic component. Its rank is \(d_i m_i\), and

\[
P_iP_j=\delta_{ij}P_i,\qquad\sum_iP_i=I.
\]

*Proof.* Since \(\overline{\chi_i}\) is a class function, conjugating the sum by \(\rho(h)\) and reindexing by \(g\mapsto hgh^{-1}\) leaves it unchanged. Every irreducible subrepresentation \(U\) is preserved by each summand, and \(P_i|_U\) is an intertwiner. If \(U\simeq V_j\), Schur's lemma makes this restriction scalar. Its trace is

\[
\operatorname{tr}(P_i|_U)=d_i\langle\chi_j,\chi_i\rangle=d_i\delta_{ij}.
\]

Division by \(\dim U=d_j\) shows that the scalar is \(1\) when \(j=i\), and \(0\) otherwise. On any irreducible direct-sum decomposition, \(P_i\) is therefore the identity on exactly the copies of \(V_i\). Its image equals the sum of all such subrepresentations: each lies in the image, and the image itself is a sum of such copies. The identities and rank follow on each summand. ∎

The component is canonical even though a choice of its individual irreducible summands need not be. Formula (3.4) makes that distinction concrete.

## 4. Why every class function has a character expansion

**Theorem 4.1 (completeness).** The irreducible characters form an orthonormal basis of \(\operatorname{CF}(G)\). In particular, \(r=c\), and every class function has the unique expansion

\[
f=\sum_{i=1}^r\langle f,\chi_i\rangle\chi_i.
\tag{4.1}
\]

*Proof.* We already have orthonormality. Suppose \(f\) is orthogonal to every irreducible character. For any representation \(\rho\), consider

\[
T_f(\rho)=\sum_{g\in G}\overline{f(g)}\rho(g).
\]

Conjugation and reindexing, together with the class-function property, show that this operator commutes with \(\rho(G)\). On \(V_i\) it is scalar, and its trace is

\[
\operatorname{tr}T_f(\rho_i)
=|G|\langle\chi_i,f\rangle
=|G|\overline{\langle f,\chi_i\rangle}=0.
\]

Since \(d_i>0\), the scalar is zero. Complete reducibility now makes \(T_f(\rho)=0\) on every representation. On the regular representation, apply it to the basis vector \(e_1\):

\[
0=T_f(R)e_1=\sum_{g\in G}\overline{f(g)}e_g.
\]

The vectors \(e_g\) are independent, so \(f=0\). Thus the orthogonal complement of the irreducible characters is zero; in a finite-dimensional inner product space this means they span. Counting dimensions gives \(r=c\), and the orthonormal-basis formula gives (4.1). ∎

It follows that a class function is a character exactly when its coefficients in (4.1) are nonnegative integers. Necessity is Theorem 3.1; for sufficiency, form the direct sum containing that many copies of each \(V_i\).

A character table is now square. Let \(X=(\chi_i(g_a))_{i,a}\), and let \(D\) be the diagonal matrix with entries \(|K_a|\). Row orthogonality says

\[
XDX^*=|G|I.
\tag{4.2}
\]

The square matrix \(U=|G|^{-1/2}XD^{1/2}\) consequently satisfies \(UU^*=I\). It is invertible, with \(U^{-1}=U^*\), so \(U^*U=I\) as well.

**Corollary 4.2 (column orthogonality).** For \(g,h\in G\),

\[
\sum_{i=1}^r\chi_i(g)\overline{\chi_i(h)}=
\begin{cases}
|C_G(g)|,&g\text{ and }h\text{ are conjugate},\\
0,&\text{otherwise}.
\end{cases}
\tag{4.3}
\]

Here \(C_G(g)=\{x\in G:xg=gx\}\).

*Proof.* The \((a,b)\) entry of \(U^*U=I\) gives

\[
\sum_i\overline{\chi_i(g_a)}\chi_i(g_b)
=\frac{|G|}{\sqrt{|K_a||K_b|}}\delta_{ab}.
\]

Conjugate this identity to obtain the stated order of the factors. For \(a=b\), the value is \(|G|/|K_a|=|C_G(g_a)|\), by Lemma 0.4 applied to conjugation. Characters are constant on classes, so this proves the assertion for arbitrary \(g,h\). ∎

Completeness is essential in this proof: orthogonal rows of a rectangular matrix do not imply orthogonal columns. For calculations, the two identities to check are (4.2) and

\[
X^*X=|G|D^{-1}.
\tag{4.4}
\]

The latter displays centralizer orders directly on its diagonal.

## 5. Building character tables from representations

A reliable table calculation has three parts. Determine the conjugacy classes and their sizes. Construct actual representations and calculate their traces. Then prove that the resulting irreducible characters exhaust the possibilities, using either their number or the sum of squared dimensions. Orthogonality checks the entries, but arbitrary orthonormal functions are not automatically characters.

### Cyclic groups: the first model

If \(G\) is abelian and \(V\) irreducible, every \(\rho(g)\) commutes with the whole representation. Schur's lemma makes each a scalar. If \(\dim V>1\), every line would be invariant, a contradiction. Thus every irreducible is one-dimensional. There are \(|G|\) of them by Theorem 4.1.

For \(C_n=\langle t:t^n=1\rangle\), let \(\zeta=e^{2\pi i/n}\). Its characters are exactly

\[
\chi_k(t^a)=\zeta^{ka},\qquad 0\leq k<n.
\]

Each formula defines a representation. Conversely, a one-dimensional representation sends \(t\) to an \(n\)-th root of unity, so it occurs on the list. The finite geometric sum gives

\[
\sum_{a=0}^{n-1}\zeta^{(k-l)a}=n\delta_{kl}.
\]

Indeed the sum is \(n\) when \(k=l\); otherwise multiplication by \(1-\zeta^{k-l}\ne0\) makes it \(1-\zeta^{(k-l)n}=0\). Summing over \(k\) instead proves column orthogonality. For \(C_4\) the table is

| Class representative | \(1\) | \(t\) | \(t^2\) | \(t^3\) |
|---|---:|---:|---:|---:|
| Class size | 1 | 1 | 1 | 1 |
| \(\chi_0\) | 1 | 1 | 1 | 1 |
| \(\chi_1\) | 1 | \(i\) | \(-1\) | \(-i\) |
| \(\chi_2\) | 1 | \(-1\) | 1 | \(-1\) |
| \(\chi_3\) | 1 | \(-i\) | \(-1\) | \(i\) |

Here the regular representation contains every character once. The full Fourier inversion and duality theory belongs to *Fourier analysis on finite abelian groups*.

### The permutations of three objects

In \(S_3\), the identity, the three transpositions, and the two three-cycles are the conjugacy classes. Conjugating a permutation relabels its cycles, which proves these assertions directly. The trivial and sign representations give two characters.

The permutation representation on \(\mathbb C^3\) splits into the constant line and

\[
W=\{(x_1,x_2,x_3):x_1+x_2+x_3=0\}.
\]

Fixed-point counts are \(3,1,0\), so the character of \(W\) is \(2,0,-1\). Its norm squared is \((4+3\cdot0+2\cdot1)/6=1\), proving irreducibility. The three distinct irreducibles exhaust the three conjugacy classes.

| Class representative | \(1\) | \((12)\) | \((123)\) |
|---|---:|---:|---:|
| Class size | 1 | 3 | 2 |
| \(\chi_1\) | 1 | 1 | 1 |
| \(\varepsilon\) | 1 | \(-1\) | 1 |
| \(\chi_W\) | 2 | 0 | \(-1\) |

For the displayed matrix \(X\), direct multiplication gives

\[
X\operatorname{diag}(1,3,2)X^*=6I_3,
\qquad X^*X=\operatorname{diag}(6,2,3).
\]

For example, the weighted product of the first and last rows is \(2+3\cdot0+2(-1)=0\); the unweighted product of the identity and three-cycle columns is \(1+1+2(-1)=0\). The two Gram matrices verify every row and column relation. The dimension check is \(1^2+1^2+2^2=6\).

As a further decomposition calculation, let \(S_3\) act on the three unordered two-element subsets of \(\{1,2,3\}\). Taking complements identifies this action with its action on the three points, so its representation is \(\mathbf1\oplus W\). By contrast, the action on ordered pairs of distinct points is free and transitive: the image of one ordered pair uniquely determines a permutation. It is regular and decomposes as \(\mathbf1\oplus\varepsilon\oplus W^{\oplus2}\).

### Symmetries of a square

We write \(D_4\) for the group of order eight,

\[
D_4=\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle.
\]

Its classes are

\[
\{1\},\quad\{r^2\},\quad\{r,r^3\},\quad
\{s,r^2s\},\quad\{rs,r^3s\}.
\]

To check this, conjugation by \(s\) inverts \(r\), and conjugation by \(r\) sends \(r^as\) to \(r^{a+2}s\). Conjugation by \(s\) sends \(r^as\) to \(r^{-a}s\). These operations preserve the parity of \(a\), giving precisely the two reflection classes; \(1,r^2\) are central.

A one-dimensional representation sends \(r\) to \(a\) and \(s\) to \(b\). The relations force \(a=a^{-1}\) and \(b^2=1\), so \(a,b\in\{1,-1\}\). Conversely each choice satisfies every relation. Write this character as \(\lambda_{a,b}\).

For the remaining character use the concrete matrices

\[
\rho(r)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\rho(s)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

They satisfy the presentation. Their traces on the five classes are \(2,-2,0,0,0\). This character has norm squared \((4+4)/8=1\), so it is irreducible.

| Class representative | \(1\) | \(r^2\) | \(r\) | \(s\) | \(rs\) |
|---|---:|---:|---:|---:|---:|
| Class size | 1 | 1 | 2 | 2 | 2 |
| \(\lambda_{1,1}\) | 1 | 1 | 1 | 1 | 1 |
| \(\lambda_{1,-1}\) | 1 | 1 | 1 | \(-1\) | \(-1\) |
| \(\lambda_{-1,1}\) | 1 | 1 | \(-1\) | 1 | \(-1\) |
| \(\lambda_{-1,-1}\) | 1 | 1 | \(-1\) | \(-1\) | 1 |
| \(\psi\) | 2 | \(-2\) | 0 | 0 | 0 |

There are five rows for five classes, and \(4\cdot1^2+2^2=8\). With \(D=\operatorname{diag}(1,1,2,2,2)\), calculation gives

\[
XDX^*=8I_5,\qquad
X^*X=\operatorname{diag}(8,8,4,4,4).
\tag{5.1}
\]

For an explicit row check, two linear characters with parameter ratios \(u,v\in\{\pm1\}\) have weighted product

\[
2+2u+2v+2uv=2(1+u)(1+v),
\]

which is \(8\) for identical rows and \(0\) otherwise. Every linear row is orthogonal to \(\psi\), since \(2-2=0\); the latter has weighted norm squared \(8\). For columns, the first two have norms squared \(8\) and mutual product \(4-4=0\). Each remaining column has norm squared \(4\). Its signs sum to zero, making it orthogonal to the first two, and two different remaining columns have sign products summing to zero. This verifies both matrices in (5.1).

### The quaternion group

Write \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), with

\[
i^2=j^2=k^2=-1,\qquad ij=k=-ji.
\]

The classes are \(\{1\},\{-1\},\{\pm i\},\{\pm j\},\{\pm k\}\). The first two are central. For example, \(i\) commutes exactly with \(\{\pm1,\pm i\}\), and conjugation by \(j\) changes \(i\) to \(-i\). The same calculation applies to \(j,k\).

In a one-dimensional representation, \(i,j\) commute, so the relation \(ij=-ji\) forces the image of the group element \(-1\) to be \(1\). Hence the images of \(i,j\) can independently be \(a,b\in\{\pm1\}\), with the image of \(k\) equal to \(ab\). These give four representations of the quotient \(Q_8/\{\pm1\}\).

For a two-dimensional representation set

\[
I=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

They satisfy \(I^2=J^2=-I_2\) and \(IJ=-JI\). Send the quaternion generators \(i,j,k\) to \(I,J,IJ\), respectively, and \(-1\) to \(-I_2\). The relations define a representation, with trace \(2,-2,0,0,0\). Its norm squared is \(1\).

| Class representative | \(1\) | \(-1\) | \(i\) | \(j\) | \(k\) |
|---|---:|---:|---:|---:|---:|
| Class size | 1 | 1 | 2 | 2 | 2 |
| \(\lambda_{1,1}\) | 1 | 1 | 1 | 1 | 1 |
| \(\lambda_{1,-1}\) | 1 | 1 | 1 | \(-1\) | \(-1\) |
| \(\lambda_{-1,1}\) | 1 | 1 | \(-1\) | 1 | \(-1\) |
| \(\lambda_{-1,-1}\) | 1 | 1 | \(-1\) | \(-1\) | 1 |
| \(\psi\) | 2 | \(-2\) | 0 | 0 | 0 |

The displayed entries and class sizes agree with those of \(D_4\) under the column correspondence \(1,r^2,r,s,rs\leftrightarrow1,-1,i,j,k\). Thus (5.1) verifies both orthogonality relations for this table too, and the five irreducibles are complete.

The groups are nevertheless not isomorphic. In \(Q_8\) only \(-1\) has order two, whereas \(D_4\) has five elements of order two: \(r^2\) and its four reflections. An ordinary character table with class sizes does not determine the group. In particular the matched columns need not preserve element orders.

### Even permutations of four objects

The twelve elements of \(A_4\) are the identity, three double transpositions, and eight three-cycles. The subgroup

\[
N=\{1,(12)(34),(13)(24),(14)(23)\}
\]

is closed under multiplication and is preserved by conjugation: conjugation relabels double transpositions. Its three nonidentity elements are conjugate in \(A_4\), as conjugation by \((123)\) permutes them transitively.

Let \(t=(123)\). A permutation commuting with \(t\) must fix \(4\); on \(\{1,2,3\}\) it is a power of \(t\). Thus its centralizer in \(A_4\) has order three and its class \(K_+\) has size four. The inverse \(t^{-1}\) is not in that class. In \(S_4\), \((23)\) conjugates \(t\) to \(t^{-1}\); every other such conjugator differs from it by a power of \(t\), so all are odd. The other four three-cycles form the inverse class \(K_-\).

The quotient \(A_4/N\) has order three, with generator \(tN\). For \(\omega=e^{2\pi i/3}\), compose its characters \(tN\mapsto1,\omega,\omega^2\) with the quotient map. This gives the three one-dimensional characters \(1,\alpha,\overline\alpha\).

The permutation representation on four points splits as the constant line plus the coordinate-sum-zero subspace \(W\) of dimension three. Its fixed-point counts are \(4,0,1,1\), so \(\chi_W=3,-1,0,0\). Its norm squared is \((9+3)/12=1\), proving irreducibility.

| Class representative | \(1\) | \((12)(34)\) | \(t=(123)\) | \(t^{-1}\) |
|---|---:|---:|---:|---:|
| Class size | 1 | 3 | 4 | 4 |
| \(\chi_1\) | 1 | 1 | 1 | 1 |
| \(\alpha\) | 1 | 1 | \(\omega\) | \(\omega^2\) |
| \(\overline\alpha\) | 1 | 1 | \(\omega^2\) | \(\omega\) |
| \(\chi_W\) | 3 | \(-1\) | 0 | 0 |

These four distinct irreducibles exhaust the four classes; also \(1+1+1+9=12\). Using \(1+\omega+\omega^2=0\) and \(\overline\omega=\omega^2\), direct multiplication gives

\[
X\operatorname{diag}(1,3,4,4)X^*=12I_4,
\qquad X^*X=\operatorname{diag}(12,4,3,3).
\tag{5.2}
\]

For rows, each linear character has weighted norm squared \(12\); two distinct linear rows have product \(4+4\omega+4\omega^2=0\). Their products with the last row are \(3-3=0\), and its weighted norm squared is \(12\). For columns, the identity and double-transposition columns have product \(3-3=0\), while their products with either three-cycle column are \(1+\omega+\omega^2=0\). The two three-cycle columns have product \(1+\omega+\omega^2=0\) as well. Their squared norms are respectively \(12,4,3,3\). This proves both relations in (5.2), including the conjugation needed for the nonreal entries.

## 6. Recovering kernels, normal subgroups and the centre

**Proposition 6.1 (kernels from traces).** For a representation \(\rho\) with character \(\chi\),

\[
\ker\rho=\{g\in G:\chi(g)=\chi(1)\}.
\tag{6.1}
\]

We call this set \(\ker\chi\). It is a normal subgroup.

*Proof.* If \(\rho(g)=I\), its trace is the dimension \(d\). Conversely, all eigenvalues of \(\rho(g)\) have modulus one. If their sum is \(d\), their real parts sum to \(d\), and each real part is at most \(1\). Each must therefore be \(1\); an eigenvalue on the unit circle with real part \(1\) is \(1\). Diagonalizability gives \(\rho(g)=I\). For \(d=0\), both sides are all of \(G\). A homomorphism's kernel is normal, since \(\rho(hgh^{-1})=I\) whenever \(\rho(g)=I\). ∎

**Theorem 6.2 (all normal subgroups are visible).** Every normal subgroup \(N\) of \(G\) is an intersection of kernels of irreducible characters.

*Proof.* Let \(G\) act on \(\mathbb C[G/N]\) by left multiplication on cosets. An element acts trivially precisely when it belongs to \(N\): necessity follows by looking at the coset \(N\), and sufficiency follows from normality. Decompose this representation into irreducibles. An element acts trivially on the direct sum exactly when it acts trivially on every constituent. Hence \(N\) is the intersection of their kernels; repeated constituents do not affect that intersection. ∎

An absolute value detects a different condition.

**Theorem 6.3 (the centre from the table).** An element \(g\) is central if and only if

\[
|\chi_i(g)|=\chi_i(1)\quad\hbox{for every irreducible }\chi_i.
\tag{6.2}
\]

*Proof.* For unit complex numbers \(\lambda_1,\ldots,\lambda_d\),

\[
d^2-\left|\sum_j\lambda_j\right|^2
=\sum_{j<k}|\lambda_j-\lambda_k|^2.
\]

Thus equality in the character bound means all eigenvalues coincide, and diagonalizability means \(\rho_i(g)\) is scalar. If \(g\) is central, Schur's lemma gives precisely that scalar condition on each irreducible.

Conversely, suppose all \(\rho_i(g)\) are scalar. For every \(h\), the commutator \(ghg^{-1}h^{-1}\) acts trivially on every irreducible and hence on the regular representation. The regular representation is faithful, since \(x e_1=e_x\) can equal \(e_1\) only for \(x=1\). Therefore every such commutator is \(1\), so \(g\) is central. ∎

For \(D_4\), the centre consists of the first two columns: the two-dimensional character has absolute value \(2\) there and \(0\) elsewhere. The corresponding centre of \(Q_8\) is \(\{\pm1\}\). For \(A_4\), the three-dimensional row has values of absolute size less than \(3\) off the identity, so its centre is trivial. These conclusions also follow from the class sizes: a singleton conjugacy class is exactly a central element.

## 7. Exercises with complete solutions

**Exercise 7.1 (easy).** Construct the character table of \(S_3\) using its action on three points, and decompose its regular representation. If a representation has character values \(8,0,-1\) on \(1,(12),(123)\), determine its irreducible multiplicities and its fixed-space dimension.

*Solution.* The three classes have sizes \(1,3,2\). Trivial and sign characters are \((1,1,1)\) and \((1,-1,1)\). The permutation character is \((3,1,0)\); removing the constant line gives \((2,0,-1)\), whose norm squared is \((4+2)/6=1\). These three distinct irreducibles give the whole table. The regular character \((6,0,0)\) has multiplicities \(1,1,2\), so

\[
R\simeq\mathbf1\oplus\varepsilon\oplus W^{\oplus2}.
\]

For the given character, the three inner products are

\[
\frac{8-2}{6}=1,\qquad
\frac{8-2}{6}=1,\qquad
\frac{16+2}{6}=3.
\]

Thus the representation is \(\mathbf1\oplus\varepsilon\oplus W^{\oplus3}\). Its dimension is \(1+1+6=8\), and its fixed-space dimension is the trivial multiplicity \(1\). The proposed values do occur, since this direct sum has exactly that character.

**Exercise 7.2 (medium).** Match the character tables of \(D_4\) and \(Q_8\) by constructing their four linear characters and one two-dimensional character. Identify a matched pair of columns with different element orders.

*Solution.* In \(D_4\), assign \(r\mapsto a,s\mapsto b\), with \(a,b=\pm1\). On \(1,r^2,r,s,rs\), the row is \((1,1,a,b,ab)\). In \(Q_8\), assign \(i\mapsto a,j\mapsto b,-1\mapsto1\); on \(1,-1,i,j,k\), the row is again \((1,1,a,b,ab)\). The defining relations verify all eight assignments.

Use the square-rotation and reflection matrices for \(D_4\), and the matrices \(I,J\) of Section 5 for \(Q_8\). Both give the row \((2,-2,0,0,0)\). Both groups have class sizes \((1,1,2,2,2)\), so this row has norm squared \(1\). The four linear representations are irreducible, and the five rows exhaust the five classes. The two tables therefore coincide with those weights. But the column of \(s\), of order two, matches the column of \(j\), of order four. This correspondence is not a group isomorphism.

**Exercise 7.3 (medium).** Starting with row orthogonality and completeness, normalize the character table to a unitary matrix and derive column orthogonality. Explain why an incomplete list of irreducibles would not suffice.

*Solution.* Let \(k_a=|K_a|\) and \(U_{ia}=\sqrt{k_a/|G|}\,\chi_i(g_a)\). Row orthogonality is \(UU^*=I\). Completeness makes \(U\) square, hence invertible, so \(U^*=U^{-1}\) and \(U^*U=I\). Its entries give

\[
\sum_i\overline{\chi_i(g_a)}\chi_i(g_b)
=\frac{|G|}{\sqrt{k_ak_b}}\delta_{ab}.
\]

Conjugating and using \(|G|/k_a=|C_G(g_a)|\) gives column orthogonality. With fewer rows, \(UU^*=I\) only says that those rows are orthonormal. For example the single row \(U=(1,0)\) satisfies that identity, while \(U^*U=\operatorname{diag}(1,0)\ne I_2\).

**Exercise 7.4 (medium).** Prove criterion (6.2) using the eigenvalues of each irreducible matrix. Then explain why the condition for a single irreducible does not suffice, using \(S_3\).

*Solution.* The sum-of-squared-differences identity in Theorem 6.3 shows that the absolute trace equals the dimension precisely when all unit-modulus eigenvalues are equal. Each finite-order matrix is diagonalizable, so that condition is equivalent to being scalar. Central elements act scalarly by Schur's lemma. Conversely, if \(g\) acts scalarly on every irreducible, each commutator \([g,h]\) acts as the identity on all of them, hence on their regular direct sum. Faithfulness of the regular representation gives \([g,h]=1\) for every \(h\).

On the trivial representation of \(S_3\), every element has absolute character value \(1\), equal to its dimension. A transposition nevertheless fails to be central: conjugating \((12)\) by \((123)\) gives \((23)\). Its value on the two-dimensional irreducible is \(0\), so the full criterion excludes it.

**Exercise 7.5 (hard).** For a normal subgroup \(N\), use the regular representation of \(G/N\), regarded as a representation of \(G\), to express \(N\) as an intersection of irreducible-character kernels. Apply the result to list all normal subgroups of \(A_4\).

*Solution.* Compose the quotient map with the left regular representation of \(G/N\). Its kernel is \(N\), since the regular representation of the quotient is faithful. Complete reducibility expresses it as a direct sum of irreducible \(G\)-representations. Its kernel is the intersection of their kernels, proving the assertion for every \(N\), including \(N=G\).

In the \(A_4\) table, the trivial character has kernel \(A_4\). Each of \(\alpha,\overline\alpha\) has kernel
\(V_4=\{1,(12)(34),(13)(24),(14)(23)\}\):
their values equal \(1\) on those columns and differ from \(1\) on both three-cycle classes. The character of degree three has kernel \(\{1\}\), because only the identity column has value \(3\). All intersections of these kernels are therefore \(\{1\},V_4,A_4\). The theorem shows that no other normal subgroup is possible. Each listed subgroup is indeed normal, either by its kernel description or by conjugation.

## Prerequisites and further directions

The earlier proof providers are precise, rather than a general assumption that character theory is already known.

- [Complete reducibility](RT-FIN-01.md#theorem-2-3) decomposes each finite-dimensional complex representation into irreducibles.
- [Schur's lemma](RT-FIN-01.md#theorem-3-1) makes an intertwiner between irreducibles zero or an isomorphism, and an endomorphism of a complex irreducible scalar.
- [Invariant Hermitian forms](RT-FIN-01.md#proposition-2-1) and the finite Hermitian-space proofs supply unitary bases and orthogonal complements.
- The complex exponential and the circle supplies the exact roots of unity used here. This is a Jiří Lebl component with its own attribution and CC BY-SA 4.0 terms; the linked unit states its real-analysis starting assumptions.

Section 0 supplies the trace, diagonalization and orbit-counting proofs. The character calculation then enables the group-algebra and finite Fourier-transform lesson, while the isotypic projections and kernel tests will be useful when studying induced representations.

The field hypothesis is essential: in characteristic \(p\), adding \(p\) copies of a nonzero representation does not change its trace character, since multiplication by \(p\) vanishes in that field. Character determination here is a theorem over \(\mathbb C\), not a claim that traces classify all modular representations.

## References

- **[Etingof et al.]** Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob and Elena Yudovina, [*Introduction to representation theory*](https://arxiv.org/pdf/0901.0827), arXiv:0901.0827. The freely accessible PDF consulted has a title-page date of November 26, 2024.
- **[Gruson–Serganova]** Caroline Gruson and Vera Serganova, [*A sentimental journey through representation theory: from finite groups to quivers (via algebras)*](https://math.berkeley.edu/~serganov/math252/Bookrep.pdf), freely accessible author draft.
- **[Milne]** J. S. Milne, [*Group Theory*](https://www.jmilne.org/math/CourseNotes/gt.html), version 4.00, 2021, with downloadable LaTeX source.
- **[Frobenius]** G. Frobenius, [*Über Gruppencharaktere*](https://www.e-rara.ch/doi/10.3931/e-rara-18877), digitized copy held by ETH-Bibliothek Zürich, Rar 1524. The catalogue does not determine the imprint date of this copy.
