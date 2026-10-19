# Artin's induction theorem and rationality

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A representation can have rational traces even when no choice of basis makes its matrices rational. The quaternion group supplies an example. This makes two questions worth separating: which character values are rational, and which representations have a model over \(\mathbb Q\)?

We first examine eigenvalues and the fields they generate. We then count irreducible rational models using permutation representations. Finally, a function supported on the generators of a cyclic group gives a constructive proof of Artin's induction theorem. The proof supplies the integer multiplier \(|G|\), for every virtual complex character.

Basic references are Igusa's *Algebra II: Representations of Groups* and Gruson–Serganova's *A Journey Through Representation Theory*. We use complete reducibility and Schur's lemma from [Representations and complete reducibility](RT-FIN-01.md), the character inner product from [Characters and the orthogonality relations](RT-FIN-02.md), central idempotents from [The group algebra and Fourier analysis on a finite group](RT-FIN-03.md), and the real-form criterion from [Tensor products, duals and real representations](RT-FIN-04.md). The arithmetic and induction tools come from [Integrality of characters and Burnside's \(p^a q^b\) theorem](RT-FIN-05.md) and [Induced representations and Frobenius reciprocity](RT-FIN-06.md).

Throughout, \(G\) is finite. Write \(R(G)\) for the ring of integer linear combinations of irreducible complex characters. A **rational model** is a representation on a finite-dimensional \(\mathbb Q\)-vector space. Write \(R_{\mathbb Q}(G)\subseteq R(G)\) for the integer span of the characters of rational models after extending scalars to \(\mathbb C\). An actual rational model has an actual character; allowing formal differences is what makes \(R_{\mathbb Q}(G)\) a group.

## 1. Powers of eigenvalues and powers of roots of unity

Let \(m\) be the exponent of \(G\), the least common multiple of its element orders. Each representing matrix satisfies \(A^m=I\). Since \(X^m-1\) has distinct complex roots, \(A\) is diagonalizable and all its eigenvalues belong to

\[
K=\mathbb Q(\zeta_m),\qquad \zeta_m=e^{2\pi i/m}.
\]

We need the cyclotomic automorphisms for composite \(m\) as well as prime \(m\). Here is the arithmetic argument.

**Lemma 1.1 (cyclotomic fields).** For every \(n\geq1\), the polynomial

\[
\Phi_n(X)=\prod_{\substack{1\leq a\leq n\\ \gcd(a,n)=1}}(X-e^{2\pi ia/n})
\]

belongs to \(\mathbb Z[X]\) and is irreducible over \(\mathbb Q\). Consequently \([\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n)\), and its automorphisms are exactly

\[
\sigma_a(\zeta_n)=\zeta_n^a,\qquad a\in(\mathbb Z/n\mathbb Z)^\times.
\tag{1}
\]

An element fixed by all these automorphisms belongs to \(\mathbb Q\).

**Proof.** Partitioning roots according to their exact orders gives

\[
X^n-1=\prod_{d\mid n}\Phi_d(X).
\tag{2}
\]

Induct on \(n\) to prove integrality of the coefficients. The product for proper divisors is a monic integer polynomial. Divide \(X^n-1\) by it using monic polynomial division in \(\mathbb Z[X]\). Equation (2) says that the remainder is zero over \(\mathbb C\), and the quotient is \(\Phi_n\). The base case is \(\Phi_1=X-1\).

Let \(f\in\mathbb Q[X]\) be the monic irreducible factor of \(\Phi_n\) having \(\zeta_n\) as a root. Put \(h=(X^n-1)/f\). Both \(f\) and \(h\) have rational coefficients; their coefficients are elementary symmetric functions of roots of unity and hence algebraic integers. The arithmetic lemma in the integrality lesson makes those coefficients integers.

Suppose \(\alpha\) is a root of \(f\) and \(p\nmid n\) is prime. If \(\alpha^p\) were not a root of \(f\), it would be a root of \(h\). The minimal polynomial property would then give \(f(X)\mid h(X^p)\) over \(\mathbb Q\), and monic division gives an integer quotient. Reduce modulo \(p\). In \(\mathbb F_p[X]\),

\[
\overline{h(X^p)}=\overline h(X)^p.
\]

Choose an irreducible factor of the nonconstant monic polynomial \(\overline f\). It divides \(\overline h\) as well. Thus its square divides \(\overline f\,\overline h=X^n-1\). This is impossible: the derivative \(nX^{n-1}\) is relatively prime to \(X^n-1\) when \(p\nmid n\). Therefore \(\alpha^p\) is a root of \(f\).

Every positive integer relatively prime to \(n\) is a product of primes not dividing \(n\). Repeatedly applying the preceding conclusion shows that every primitive \(n\)-th root is a root of \(f\). Hence \(f=\Phi_n\).

Sending \(\zeta_n\) to any primitive root now defines a field homomorphism by the presentation \(\mathbb Q[X]/(\Phi_n)\). It is onto: if \(ab\equiv1\pmod n\), then \((\zeta_n^a)^b=\zeta_n\). Conversely an automorphism preserves the exact order of \(\zeta_n\), so these are all the automorphisms. Their composition corresponds to multiplying \(a\)'s.

For completeness, the fixed-field assertion follows from a trace calculation. Use the basis \(1,\zeta_n,\ldots,\zeta_n^{\varphi(n)-1}\). The matrix with rows

\[
(1,\zeta_n^a,\ldots,(\zeta_n^a)^{\varphi(n)-1})
\]

is invertible by the Vandermonde determinant. If \(M_y\) is the rational matrix of multiplication by \(y\in\mathbb Q(\zeta_n)\), these rows conjugate \(M_y\) to the diagonal matrix with entries \(\sigma_a(y)\). Thus

\[
\sum_a\sigma_a(y)=\operatorname{tr}(M_y)\in\mathbb Q.
\]

If all the summands equal \(y\), this says \(\varphi(n)y\in\mathbb Q\), and hence \(y\in\mathbb Q\). The argument includes \(n=1\). \(\square\)

**Theorem 1.2 (Galois action on characters).** For any complex character \(\chi\) and any \(a\) relatively prime to \(m\),

\[
\sigma_a(\chi(g))=\chi(g^a).
\tag{3}
\]

Applying \(\sigma_a\) to values permutes the irreducible characters. The same operation preserves actual characters and virtual characters.

**Proof.** If the eigenvalues of \(g\) are \(\lambda_1,\ldots,\lambda_d\), all are \(m\)-th roots of unity. The two sides of (3) are both \(\sum_j\lambda_j^a\).

To verify irreducibility without assuming that \(K\) is a splitting field, use the central idempotents already proved in the group-algebra lesson:

\[
e_\chi=\frac{\chi(1)}{|G|}\sum_{g\in G}\chi(g^{-1})g
\qquad(\chi\in\operatorname{Irr}(G)).
\tag{4}
\]

All coefficients lie in \(K\). These idempotents form a \(K\)-basis of \(Z(K[G])\): they are linearly independent, and the dimension of the centre is the number of conjugacy classes, equal to \(|\operatorname{Irr}(G)|\). Their multiplication is \(e_\chi e_\psi=\delta_{\chi,\psi}e_\chi\). Therefore they are exactly the primitive idempotents of this centre over \(K\).

Applying \(\sigma_a\) to the coefficients is a semilinear algebra automorphism of \(K[G]\). It permutes those primitive central idempotents. Suppose it sends \(e_\chi\) to \(e_\psi\). The coefficient of the identity in (4) is \(\chi(1)^2/|G|\), a positive rational number. It follows that \(\chi(1)=\psi(1)\). Comparing the remaining coefficients now gives \(\sigma_a(\chi(g))=\psi(g)\) for every \(g\). This proves the permutation assertion. Applying it to a sum of irreducibles with nonnegative integer coefficients, or with arbitrary integer coefficients, proves the last assertion. \(\square\)

**Corollary 1.3 (generators have equal rational traces).** If \(\chi\) has rational values and \(\langle g\rangle=\langle h\rangle\), then \(\chi(g)=\chi(h)\). In particular this holds for the character of every rational model, whose values are integers.

**Proof.** Write \(h=g^b\), with \(b\) relatively prime to the order \(d\) of \(g\). Apply the eigenvalue argument of (3) in \(\mathbb Q(\zeta_d)\). Its automorphism \(\zeta_d\mapsto\zeta_d^b\) fixes the rational number \(\chi(g)\).

For a rational model, each trace is rational because the matrix is rational. It is an algebraic integer by character integrality, and therefore an integer. \(\square\)

Call two elements **rationally conjugate** when the cyclic subgroups they generate are conjugate in \(G\). This is an equivalence relation. Its classes correspond to conjugacy classes of cyclic subgroups, including the trivial subgroup. Corollary 1.3 says that a rational-valued character is constant on these classes.

## 2. Counting rational models with fixed cosets

The character of a rational irreducible need not have complex norm one. Its commuting algebra can have dimension greater than one. Nevertheless distinct rational irreducibles still give independent characters.

**Lemma 2.1 (intertwiners survive extension of scalars).** For rational models \(U,V\), put \(U_{\mathbb C}=\mathbb C\otimes_{\mathbb Q}U\), and similarly for \(V\). Then

\[
\mathbb C\otimes_{\mathbb Q}\operatorname{Hom}_{\mathbb Q[G]}(U,V)
\ \cong\
\operatorname{Hom}_{\mathbb C[G]}(U_{\mathbb C},V_{\mathbb C}).
\tag{5}
\]

Consequently

\[
\langle\chi_{V_{\mathbb C}},\chi_{U_{\mathbb C}}\rangle_G
=\dim_{\mathbb Q}\operatorname{Hom}_{\mathbb Q[G]}(U,V).
\tag{6}
\]

**Proof.** Choose rational bases. Intertwiners are precisely the solutions of

\[
T\rho_U(g)-\rho_V(g)T=0\qquad(g\in G),
\]

a finite system of homogeneous linear equations with rational coefficients in the entries of \(T\). Row reduction over \(\mathbb Q\) gives a rational basis of its kernel; the same pivot equations give the complex kernel after extending scalars. This proves (5). Complex character orthogonality and complete reducibility identify the dimension of the complex Hom space with the left side of (6). \(\square\)

There are finitely many rational irreducible types. Indeed, for a nonzero vector \(v\) in a rational irreducible \(S\), the map \(\mathbb Q[G]\to S\), \(a\mapsto av\), is onto. Maschke's theorem over \(\mathbb Q\) splits it, so \(S\) occurs in the rational regular representation.

Let the distinct rational irreducibles be \(S_1,\ldots,S_r\). By Schur's lemma and (6), their complexified characters are orthogonal for different indices, and each has positive squared norm

\[
\langle\chi_{S_i},\chi_{S_i}\rangle_G
=\dim_{\mathbb Q}\operatorname{End}_{\mathbb Q[G]}(S_i)\geq1.
\tag{7}
\]

Here and below \(\chi_{S_i}\) denotes the complexified character. These \(r\) characters are therefore linearly independent.

For a cyclic subgroup \(C\), the permutation module \(\mathbb Q[G/C]\) supplies the character

\[
P_C=\operatorname{Ind}_C^G1_C.
\]

Its value at \(g\) is the number of cosets fixed by \(g\), namely

\[
P_C(g)=\frac1{|C|}
\bigl|\{x\in G:x^{-1}gx\in C\}\bigr|.
\tag{8}
\]

**Theorem 2.2 (the rational irreducible count).** The number of irreducible rational models, up to isomorphism, is the number of conjugacy classes of cyclic subgroups of \(G\).

**Proof.** Let that latter number be \(k\). The space \(F\) of complex-valued functions constant on rational conjugacy classes has dimension \(k\). The \(r\) independent characters in (7) belong to \(F\), by Corollary 1.3. Thus \(r\leq k\).

Choose representatives \(C_1,\ldots,C_k\), ordered by increasing size, and a generator \(c_i\) of each \(C_i\). Consider the \(k\times k\) matrix

\[
M_{ij}=P_{C_j}(c_i).
\]

Equation (8) makes this zero unless \(C_i\) is conjugate to a subgroup of \(C_j\). In particular it is zero when \(|C_i|>|C_j|\). For distinct representatives of equal size it is also zero, since containment would imply conjugacy. On the diagonal,

\[
M_{ii}=\frac{|N_G(C_i)|}{|C_i|}>0:
\]

the condition \(x^{-1}c_ix\in C_i\) says exactly that \(x\) normalizes \(C_i\). The matrix is upper triangular with nonzero diagonal. Hence \(P_{C_1},\ldots,P_{C_k}\) are linearly independent.

Each is the character of a rational model. Complete reducibility over \(\mathbb Q\) expresses it as a nonnegative integer combination of \(\chi_{S_1},\ldots,\chi_{S_r}\). Therefore \(k\leq r\), proving equality. \(\square\)

**Corollary 2.3 (a rational permutation basis).** The characters \(P_{C_i}\) form a basis of \(F\). Every rational-valued class function constant on rational conjugacy classes is a rational linear combination of them.

**Proof.** They are \(k\) independent elements of the \(k\)-dimensional space \(F\). For the second assertion, evaluate at the chosen generators. The resulting system has integer matrix \(M\) with nonzero determinant and rational right side. Solving it gives rational coefficients. Equality at those generators implies equality everywhere by constancy on rational conjugacy classes. \(\square\)

This corollary concerns rational linear combinations. It does not promise a rational model with a specified character in its original dimension.

## 3. A cyclic function that selects generators

Define the arithmetic Möbius function by \(\mu(1)=1\), \(\mu(t)=0\) if a prime square divides \(t\), and \(\mu(t)=(-1)^s\) if \(t\) is a product of \(s\) distinct primes. Expansion of \(\prod_{p\mid t}(1-1)\) gives

\[
\sum_{e\mid t}\mu(e)=
\begin{cases}1&t=1,\\0&t>1.\end{cases}
\tag{9}
\]

For \(C=\langle c\rangle\) of order \(n\), define

\[
\theta_C(x)=
\begin{cases}
n&\langle x\rangle=C,\\
0&\langle x\rangle\ne C.
\end{cases}
\tag{10}
\]

For \(n>1\) this function is zero at the identity. It cannot be an actual nonzero character. We will need it as a virtual character.

**Lemma 3.1 (integral generator selector).** Let \(C_d\leq C\) have order \(d\), for every \(d\mid n\). Then

\[
\theta_C=\sum_{d\mid n}d\,\mu(n/d)\operatorname{Ind}_{C_d}^C1_{C_d}.
\tag{11}
\]

In particular \(\theta_C\) is an integral virtual character, even an integer combination of permutation characters. For \(\lambda_j(c)=e^{2\pi ij/n}\), its coefficient at \(\lambda_j\) is

\[
\langle\theta_C,\lambda_j\rangle_C
=\sum_{d\mid\gcd(n,j)}d\,\mu(n/d).
\tag{12}
\]

**Proof.** In the abelian group \(C\), every coset of \(C_d\) is fixed by \(x\in C_d\), and none is fixed by \(x\notin C_d\). Thus \(\operatorname{Ind}_{C_d}^C1=(n/d)1_{C_d}\). If \(x\) has order \(e\), the right side of (11) is

\[
n\sum_{\substack{d\mid n\\e\mid d}}\mu(n/d)
=n\sum_{t\mid n/e}\mu(t).
\]

Equation (9) makes this \(n\) exactly when \(e=n\), and zero otherwise. This proves (11) and its integral-character assertion.

By Frobenius reciprocity, the coefficient of \(\lambda_j\) in \(\operatorname{Ind}_{C_d}^C1\) is one if its restriction to \(C_d\) is trivial, and zero otherwise. The restriction is trivial exactly when \(d\mid j\). Substitution in (11) gives (12). \(\square\)

The same coefficient is the Ramanujan sum \(\sum_{(a,n)=1}e^{-2\pi iaj/n}\), by taking the inner product directly in (10). Formula (12) proves its integrality without a field-theoretic shortcut.

**Lemma 3.2 (the induced selectors add to a constant).** Summing over all cyclic subgroups, including the trivial subgroup, gives

\[
\sum_{\substack{C\leq G\\ C\text{ cyclic}}}
\operatorname{Ind}_C^G\theta_C=|G|\,1_G.
\tag{13}
\]

For a fixed \(C\), the summand takes the value \(|N_G(C)|\) at \(g\) if \(\langle g\rangle\) is conjugate to \(C\), and zero otherwise.

**Proof.** The induction formula cancels the factor \(|C|\) in (10):

\[
(\operatorname{Ind}_C^G\theta_C)(g)
=\bigl|\{x\in G:\langle x^{-1}gx\rangle=C\}\bigr|.
\tag{14}
\]

For each \(x\), there is exactly one cyclic subgroup in this condition, namely \(\langle x^{-1}gx\rangle\). Summing (14) over \(C\) therefore counts each of the \(|G|\) elements \(x\) once. If a particular \(C\) occurs, the \(x\)'s that carry \(\langle g\rangle\) to \(C\) form a coset of its normalizer and have cardinality \(|N_G(C)|\). \(\square\)

## 4. Artin's theorem with an explicit multiplier

**Theorem 4.1 (Artin induction).** For every \(\chi\in R(G)\), the virtual character \(|G|\chi\) is an integer linear combination of

\[
\operatorname{Ind}_C^G\lambda,\qquad
C\leq G\text{ cyclic},\quad \lambda:C\to\mathbb C^\times\text{ linear}.
\]

Consequently every virtual character is a rational linear combination of these induced characters.

**Proof.** Multiply (13) by \(\chi\) in the representation ring. The projection formula proved in the induction lesson yields the explicit identity

\[
|G|\chi=
\sum_{C\text{ cyclic}}
\operatorname{Ind}_C^G
\bigl(\theta_C\,\operatorname{Res}_C^G\chi\bigr).
\tag{15}
\]

By Lemma 3.1, \(\theta_C\in R(C)\). Restriction and multiplication preserve virtual characters. All complex irreducibles of the abelian group \(C\) are linear, so each product inside (15) is an integer linear combination of its linear characters. Expanding those products proves the first assertion. Dividing by the nonzero integer \(|G|\) proves the second. \(\square\)

The argument applies to arbitrary complex virtual characters; it imposes no rational-value hypothesis. It also gives a useful identity entirely in terms of permutation characters. Substitute (11) in (13), use induction in stages, and collect terms for the same subgroup \(D\):

\[
|G|\,1_G=
\sum_{D\text{ cyclic}}
|D|\left(\sum_{\substack{C\text{ cyclic}\\D\leq C}}
\mu([C:D])\right)P_D.
\tag{16}
\]

Every coefficient in this expression is an integer. Negative coefficients are essential in general.

There are two distinct rational statements here. Corollary 2.3 uses rational-valued functions and induced **trivial** characters. Theorem 4.1 uses all virtual complex characters and induced **linear** characters, which may have nonrational values.

## 5. Three examples of the distinction

### Cyclic groups over \(\mathbb Q\)

**Proposition 5.1.** If \(C_n=\langle c\rangle\), its irreducible rational models are

\[
V_d=\mathbb Q[X]/(\Phi_d(X))=\mathbb Q(\zeta_d),
\qquad d\mid n,
\tag{17}
\]

where \(c\) acts by multiplication by \(\zeta_d\). Their dimensions are \(\varphi(d)\). After complexification, \(V_d\) is the sum of the distinct linear characters that send \(c\) to a primitive \(d\)-th root.

**Proof.** A rational model of \(C_n\) is a rational vector space with an operator \(T\) satisfying \(T^n=I\). In an irreducible model, any nonzero \(v\) generates under \(\mathbb Q[T]\). It identifies the model with \(\mathbb Q[X]/I\), where \(I\) is the kernel of \(p\mapsto p(T)v\). Polynomial division makes \(I=(f)\) for a monic polynomial \(f\). Irreducibility says that this quotient has no proper nonzero submodules, hence \(f\) is irreducible: a proper factor would give a proper nonzero ideal in the quotient. Also \(f\mid X^n-1\).

By (2) and Lemma 1.1 the possible \(f\)'s are exactly the distinct \(\Phi_d\), \(d\mid n\). Conversely each quotient in (17) is a field, so a subspace stable under \(c\) and rational scalars is an ideal in that field. It is zero or the whole field. Different \(\Phi_d\)'s give different minimal polynomials, hence nonisomorphic models. The dimension is their degree. Over \(\mathbb C\), the operator has the distinct roots of \(\Phi_d\) as eigenvalues, each once, proving the last assertion. \(\square\)

Thus \(C_p\) for prime \(p\) has two rational irreducibles, of dimensions \(1\) and \(p-1\), although it has \(p\) complex irreducibles. The larger rational irreducible has trace \(p-1\) at the identity and \(-1\) elsewhere.

### The permutations of three objects

The trivial model, the sign model, and the rational plane

\[
U=\{(x_1,x_2,x_3)\in\mathbb Q^3:x_1+x_2+x_3=0\}
\]

are irreducible and pairwise nonisomorphic over \(\mathbb Q\). For the plane, its complexification has the irreducible standard character \(u\), so a proper rational submodule would give a proper complex submodule. The three conjugacy classes of cyclic subgroups are represented by \(1,C_2,C_3\). Theorem 2.2 now proves completeness.

Let \(\varepsilon\) be the nontrivial character of \(C_2\), and let \(\omega\) send a generator of \(C_3\) to \(e^{2\pi i/3}\). Write

\[
\begin{aligned}
R&=\operatorname{Ind}_1^{S_3}1,&
P&=\operatorname{Ind}_{C_2}^{S_3}1,&
Q&=\operatorname{Ind}_{C_2}^{S_3}\varepsilon,\\
T&=\operatorname{Ind}_{C_3}^{S_3}1,&
J&=\operatorname{Ind}_{C_3}^{S_3}\omega,&
J'&=\operatorname{Ind}_{C_3}^{S_3}\omega^2.
\end{aligned}
\]

Frobenius reciprocity, or the induction formula, gives the following values.

| Character | Identity | Transposition | Three-cycle |
|---|---:|---:|---:|
| \(R=1+\mathrm{sgn}+2u\) | \(6\) | \(0\) | \(0\) |
| \(P=1+u\) | \(3\) | \(1\) | \(0\) |
| \(Q=\mathrm{sgn}+u\) | \(3\) | \(-1\) | \(0\) |
| \(T=1+\mathrm{sgn}\) | \(2\) | \(0\) | \(2\) |
| \(J=J'=u\) | \(2\) | \(0\) | \(-1\) |

For example, \(u|_{C_2}=1+\varepsilon\) and \(u|_{C_3}=\omega+\omega^2\); the trivial and sign characters both restrict trivially to \(C_3\). These restrictions and reciprocity prove every decomposition in the table.

The three subgroups of order two and the single subgroup of order three turn (16) into

\[
6\,1=-3R+6P+3T.
\tag{18}
\]

This also follows by reading each column of the table. For the standard character, (15) gives

\[
6u=2R-2T+J+J'.
\tag{19}
\]

Indeed, the trivial subgroup contributes \(2R\). For an order-two subgroup, \(\theta=1-\varepsilon\), so \(\theta\,u|_{C_2}=(1-\varepsilon)(1+\varepsilon)=0\). For \(C_3\), \(\theta=2-\omega-\omega^2\); multiplying by \(\omega+\omega^2\) gives \(\omega+\omega^2-2\), which induces to the remaining terms of (19).

Here the multiplier can even be removed:

\[
u=J,\qquad 1=P-J,\qquad \mathrm{sgn}=Q-J.
\]

The universal multiplier \(|G|\) in Artin's theorem need not be minimal.

### The quaternion group

For \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), the degree-two complex irreducible \(\psi\) has values

\[
\psi(1)=2,\qquad \psi(-1)=-2,\qquad
\psi(\pm i)=\psi(\pm j)=\psi(\pm k)=0.
\]

Its values are integers. Its Frobenius–Schur indicator is nevertheless

\[
\nu(\psi)=\frac{2\psi(1)+6\psi(-1)}8=-1,
\]

because the six order-four elements square to \(-1\). The real-form theorem proves that \(\psi\) has no real model, and hence no rational model.

There is a rational model of character \(2\psi\). Take the four-dimensional rational quaternion algebra

\[
\mathbb H_{\mathbb Q}
=\mathbb Q\,1\oplus\mathbb Q\,i\oplus\mathbb Q\,j\oplus\mathbb Q\,k
\]

and let \(Q_8\) act by left multiplication. A nonzero quaternion \(q=a+bi+cj+dk\) has inverse

\[
q^{-1}=\frac{a-bi-cj-dk}{a^2+b^2+c^2+d^2}.
\]

The denominator is positive for rational \(a,b,c,d\) not all zero. An invariant rational subspace is stable under all rational linear combinations of \(Q_8\), so it is a left ideal of this division algebra. Any such ideal containing a nonzero \(q\) also contains \(q^{-1}q=1\), and is the whole algebra. The model is therefore rationally irreducible. Left multiplication has traces \(4,-4,0,0,0\) on the five complex conjugacy classes, giving \(2\psi\).

There are five cyclic subgroups up to conjugacy: \(1,\{\pm1\},\langle i\rangle,\langle j\rangle,\langle k\rangle\). The four rational linear characters and this four-dimensional model are consequently all the rational irreducibles. Its complex squared norm is \(4\), in agreement with (7). A full theory of Schur indices and central division algebras goes beyond this lesson; the concrete obstruction and its rational replacement are proved here.

## 6. Exercises with complete solutions

**Exercise 1.** Show that every character of \(S_n\) is rational-valued. Deduce integer values for virtual characters. Explain why this argument alone does not construct rational matrices.

**Solution.** If \(a\) is relatively prime to the exponent of \(S_n\), it is relatively prime to every cycle length of a permutation \(g\). Taking the \(a\)-th power of a cycle of length \(d\) leaves it a single cycle of length \(d\): addition by \(a\) on \(\mathbb Z/d\mathbb Z\) has one orbit. Thus \(g^a\) has the same cycle type as \(g\) and is conjugate to it. Theorem 1.2 gives \(\sigma_a(\chi(g))=\chi(g^a)=\chi(g)\) for every cyclotomic automorphism. Lemma 1.1 makes \(\chi(g)\) rational. Character integrality makes it an integer, and integer combinations preserve this property.

This determines traces. It gives no descent of a complex vector space or its matrices to \(\mathbb Q\). The quaternion example shows why a trace argument cannot supply that conclusion for general groups. Rational models for the irreducibles of \(S_n\) will be constructed in the lesson on Young symmetrizers. The cases \(n=0,1\) are the trivial group and satisfy the same conclusion directly.

**Exercise 2.** For a cyclic group of arbitrary order, prove that the generator selector is an integral virtual character and that its induced selectors sum to \(|G|1_G\). Then compute its full expansion for \(C_{12}=\langle c\rangle\).

**Solution.** If \(C\) has order \(n\), its permutation character from the subgroup of order \(d\) is \((n/d)1_{C_d}\). At an element of order \(e\), the combination

\[
\sum_{d\mid n}d\mu(n/d)\operatorname{Ind}_{C_d}^C1
\]

has value \(n\sum_{t\mid n/e}\mu(t)\), equal to \(n\) if \(e=n\) and zero otherwise. This proves the claimed selector formula with integer coefficients, hence integrality as a virtual character. Its linear-character coefficient is \(\sum_{d\mid\gcd(n,j)}d\mu(n/d)\), since \(\lambda_j|_{C_d}\) is trivial exactly when \(d\mid j\).

After induction to \(G\), the value at \(g\) counts \(x\in G\) for which \(x^{-1}gx\) generates the chosen cyclic subgroup. Each \(x\) chooses exactly one subgroup, so summing counts \(|G|\) elements, for every \(g\). This proves the required constant identity, including \(g=1\) and \(n=1\).

For \(n=12\), the only nonzero terms in (12) come from \(d=2,4,6,12\). Thus the coefficient at \(\lambda_j(c)=e^{2\pi ij/12}\) is

\[
2\,1_{2\mid j}-4\,1_{4\mid j}
-6\,1_{6\mid j}+12\,1_{12\mid j}.
\]

The full expansion is

\[
\theta_{C_{12}}
=4\lambda_0+2\lambda_2-2\lambda_4
-4\lambda_6-2\lambda_8+2\lambda_{10},
\]

with zero coefficients at all odd indices. It has degree \(4+2-2-4-2+2=0\), as required, and value \(12\) precisely at \(c,c^5,c^7,c^{11}\).

**Exercise 3.** Determine all irreducible rational models of \(C_{12}\), with dimensions and a rational matrix for its generator in the four-dimensional model.

**Solution.** Proposition 5.1 gives one model for each divisor \(d\) of \(12\). The complete list is:

| \(d\) | Minimal polynomial of the generator | Dimension |
|---:|---|---:|
| \(1\) | \(X-1\) | \(1\) |
| \(2\) | \(X+1\) | \(1\) |
| \(3\) | \(X^2+X+1\) | \(2\) |
| \(4\) | \(X^2+1\) | \(2\) |
| \(6\) | \(X^2-X+1\) | \(2\) |
| \(12\) | \(X^4-X^2+1\) | \(4\) |

These polynomials follow successively from (2), or by multiplying the displayed factors to obtain \(X^{12}-1\). Their irreducibility follows from Lemma 1.1. Distinct minimal polynomials distinguish the models, and the cyclic-module argument in Proposition 5.1 proves completeness.

On the basis \(1,\zeta_{12},\zeta_{12}^2,\zeta_{12}^3\), multiplication by \(\zeta_{12}\) has matrix

\[
\begin{pmatrix}
0&0&0&-1\\
1&0&0&0\\
0&1&0&1\\
0&0&1&0
\end{pmatrix}.
\]

The last column uses \(\zeta_{12}^4=\zeta_{12}^2-1\). The matrix satisfies \(\Phi_{12}(T)=0\) and \(T^{12}=I\). After complexification its eigenvalues are \(\zeta_{12},\zeta_{12}^5,\zeta_{12}^7,\zeta_{12}^{11}\). The six dimensions sum to \(12\). Each field quotient occurs once in the rational regular representation: its complexification contains each linear character once, and the six sets of eigencharacters partition those twelve characters.

**Exercise 4.** Prove the rational irreducible count for an arbitrary finite group using intertwiners and fixed cosets. Explain explicitly why replacing rational irreducibles by rational-valued complex irreducibles would invalidate the argument.

**Solution.** Let \(k\) be the number of conjugacy classes of cyclic subgroups. Rational model characters are constant on the corresponding \(k\) rational conjugacy classes, by applying cyclotomic automorphisms to their rational traces. For distinct rational irreducibles \(S,T\), Schur's lemma gives \(\operatorname{Hom}_{\mathbb Q[G]}(S,T)=0\); the self-Hom space contains the identity. The equations defining Hom are rational linear equations, so extending scalars preserves their dimensions. Complex character theory therefore makes the distinct rational irreducible characters orthogonal with positive self-norms. They are independent, so their number \(r\) is at most \(k\). All these types occur in the rational regular representation by the surjection \(a\mapsto av\) and Maschke's theorem, so the list is finite.

For the reverse inequality choose one cyclic subgroup \(C\) from each conjugacy class. The rational permutation character \(P_C\) counts fixed cosets. Evaluate these \(k\) characters at generators of the chosen subgroups \(D\), ordering by size. A value can be nonzero only if \(D\) is conjugate into \(C\). Equal sizes force the two representatives to coincide. The diagonal entry is \(|N_G(C)|/|C|>0\). This triangular matrix is invertible, so the \(k\) permutation characters are independent. Complete reducibility over \(\mathbb Q\) puts them in the span of the \(r\) rational irreducible characters. Thus \(k\leq r\) and \(r=k\).

The crucial second step decomposes rational permutation modules into rational irreducibles. A rational-valued complex irreducible need not be one of these models. For \(Q_8\), the rational-valued character \(\psi\) has no rational model; the corresponding rational irreducible has character \(2\psi\). Its positive self-norm is \(4\), rather than \(1\). The proof uses independence and positivity, and never replaces that norm by \(1\).

## 7. Earlier results used without proof

Complete reducibility over every characteristic-zero field and Schur's lemma are Theorems 2.3 and 3.1 of *Representations and complete reducibility*. Character multiplicities, the character basis and the inner-product description of Hom are proved in §§2–4 of *Characters and the orthogonality relations*. The primitive central idempotent formula is Theorem 3.1 of *The group algebra and Fourier analysis on a finite group*. The Frobenius–Schur real-form criterion is Theorem 3.1 of *Tensor products, duals and real representations*.

We use the algebraic-integer ring properties and rational-integral criterion of Lemma 1.1, and character-value integrality of Proposition 2.1, in *Integrality of characters and Burnside's \(p^a q^b\) theorem*. The induction formula, Frobenius reciprocity, induction in stages and the projection formula are proved in §§1–4 of *Induced representations and Frobenius reciprocity*. Polynomial division, row reduction, and the Vandermonde determinant are basic linear algebra and polynomial algebra. All further field and rational-representation assertions needed here have been proved above.

## References

- **K. Igusa**, [*Algebra II, Part D: Representations of Groups*](https://people.brandeis.edu/~igusa/Math101bS07/Math101b_notesD3c.pdf), §3.3, Theorem 3.18 and its proof, for induction from subgroup families meeting every conjugacy class.
- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Universitext, Springer, 2018, Chapter 2 §§11–12, for extension of scalars, rational models and Artin induction.
