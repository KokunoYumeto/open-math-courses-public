# Consequences of Brauer's theorem: characterization of characters and splitting fields

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A character is a class function, but being constant on conjugacy classes does not make a function a character. Its coefficients in the irreducible character basis must be nonnegative integers. A virtual character allows negative integers as well. Brauer's induction theorem gives a way to detect this integer condition by passing to particular subgroups. It also answers a different question: over which field can we choose the matrices of a representation?

The two applications use the same feature of Brauer's theorem. Its coefficients are integers. For the first application, this preserves the lattice of virtual characters. For the second, it lets a norm-one argument extract an actual representation from a difference of representations.

We assume the results of Representations and complete reducibility, Characters and the orthogonality relations, Induced representations and Frobenius reciprocity, Artin's induction theorem and rationality, and Brauer's induction theorem. In particular, we use Maschke's theorem over fields of characteristic zero, the complex character inner product, induction, and the full integer form of Brauer's theorem. The induction comparison is [Kramár]. The exact course proof routes for the algebraic results and the arithmetic application are identified below.

Throughout, \(G\) is a finite group. All representations are finite-dimensional. A coefficient field \(F\) is a subfield of \(\mathbb C\), with its inclusion fixed.

## 1. Recognizing the integer character lattice

Write \(\operatorname{Irr}(G)\) for the irreducible complex characters and
\[
R(G)=\bigoplus_{\chi\in\operatorname{Irr}(G)}\mathbb Z\chi.
\tag{1}
\]
The elements of \(R(G)\) are virtual characters. Addition comes from direct sums; multiplication comes from tensor products. Thus \(R(G)\) is a ring of class functions, with identity \(1_G\). Restriction and induction carry virtual characters to virtual characters, since they do so for actual representations and are additive.

Our convention is
\[
\langle\alpha,\beta\rangle_G
=\frac1{|G|}\sum_{g\in G}\alpha(g)\overline{\beta(g)}.
\tag{2}
\]
The irreducible characters are an orthonormal basis of the complex vector space of class functions. Therefore a class function \(\theta\) is virtual precisely when every \(\langle\theta,\chi\rangle_G\) is an integer. It is an actual character precisely when these integers are all nonnegative.

An elementary subgroup means a subgroup isomorphic to \(C\times P\), where \(P\) is a \(p\)-group and \(C\) is cyclic of order prime to \(p\), for some prime \(p\). The prime may vary with the subgroup. Both factors may be trivial. Brauer's theorem from the preceding lesson supplies elementary subgroups \(E_i\), linear characters \(\lambda_i\) of \(E_i\), and integers \(a_i\) such that
\[
1_G=\sum_i a_i\operatorname{Ind}_{E_i}^G\lambda_i.
\tag{3}
\]
We first explain why this particular identity can test arbitrary class functions.

**Lemma 1.1 (projection formula for class functions).** If \(H\leq G\), \(\eta\) is a class function on \(H\), and \(\theta\) is a class function on \(G\), then
\[
\theta\,\operatorname{Ind}_H^G\eta
=\operatorname{Ind}_H^G\bigl((\operatorname{Res}_H^G\theta)\eta\bigr).
\tag{4}
\]
Neither function needs to be a character.

**Proof.** The normalized induction formula is
\[
(\operatorname{Ind}_H^G\eta)(g)
=\frac1{|H|}
\sum_{\substack{x\in G\\x^{-1}gx\in H}}\eta(x^{-1}gx).
\]
In the right side of (4), each summand is multiplied by \(\theta(x^{-1}gx)\). This equals \(\theta(g)\), since \(\theta\) is a class function on \(G\). Factoring it out proves the equality at each \(g\). \(\square\)

**Theorem 1.2 (Brauer's characterization).** A complex class function \(\theta\) on \(G\) is a virtual character if and only if its restriction to every elementary subgroup is a virtual character.

**Proof.** Restricting an actual representation gives an actual representation, so restricting an integer difference gives a virtual character. This proves one direction.

For the other, multiply (3) by \(\theta\). Lemma 1.1 gives
\[
\theta
=\sum_i a_i\operatorname{Ind}_{E_i}^G
\bigl((\operatorname{Res}_{E_i}^G\theta)\lambda_i\bigr).
\tag{5}
\]
By hypothesis, each restricted function belongs to \(R(E_i)\). Its product with the character \(\lambda_i\) also belongs to \(R(E_i)\): tensoring actual representations with the line \(\lambda_i\), then taking integer differences, describes this product. Induction takes it into \(R(G)\). Since every \(a_i\) is an integer, the sum belongs to \(R(G)\). \(\square\)

It is enough to check the elementary subgroups appearing in one identity (3). This does not say that proper subgroups always suffice. For example, a \(p\)-group is itself elementary.

The characterization also recognizes irreducible characters without assuming in advance that a proposed function is a character.

**Corollary 1.3 (recognition at norm one).** Suppose that a class function \(\theta\) restricts to a virtual character on every elementary subgroup, that \(\langle\theta,\theta\rangle_G=1\), and that \(\theta(1)\) is a positive real number. Then \(\theta\) is an irreducible character.

**Proof.** Theorem 1.2 gives
\[
\theta=\sum_{\chi\in\operatorname{Irr}(G)}b_\chi\chi,
\qquad b_\chi\in\mathbb Z.
\]
Orthogonality gives \(1=\sum_\chi b_\chi^2\). Exactly one coefficient is nonzero, and it is \(1\) or \(-1\). Hence \(\theta=\chi\) or \(-\chi\). Since \(\chi(1)>0\), the degree condition chooses the positive sign. \(\square\)

The condition on the sign cannot be dropped: \(-1_G\) is virtual and has norm one. Also, even when a function is virtual, a positive value at the identity alone does not make it an actual character. One must test the signs of all its irreducible coefficients.

*Proof route:* [Brauer's induction theorem, Theorem 5.1](RT-FIN-11.md#theorem-5-1) supplies the integer identity (3). Lemma 1.1 and the character norm calculation above prove both conclusions from that identity.

## 2. What changes when the coefficient field changes?

Let \(U\) be an \(F\)-representation. Its complexification is
\[
U_{\mathbb C}=\mathbb C\otimes_F U,
\qquad g(z\otimes u)=z\otimes gu.
\tag{6}
\]
The character \(\phi_U\) of \(U_{\mathbb C}\) is computed by the same matrices as that of \(U\). In particular,
\[
\phi_U(g)=\operatorname{Tr}_F(\rho_U(g))\in F,
\qquad \phi_U(1)=\dim_F U.
\]
An irreducible \(F\)-representation need not have irreducible complexification. To handle this issue we compare maps over the two fields, rather than assume that irreducibility is preserved.

**Lemma 2.1 (intertwining maps and extension of scalars).** For \(F\)-representations \(U,V\), the natural map
\[
\mathbb C\otimes_F\operatorname{Hom}_{F[G]}(U,V)
\longrightarrow
\operatorname{Hom}_{\mathbb C[G]}(U_{\mathbb C},V_{\mathbb C})
\tag{7}
\]
is an isomorphism. Consequently
\[
\langle\phi_V,\phi_U\rangle_G
=\dim_F\operatorname{Hom}_{F[G]}(U,V).
\tag{8}
\]

**Proof.** Choose \(F\)-bases of \(U,V\). An intertwining map is a rectangular matrix \(T\) satisfying
\[
T\rho_U(g)-\rho_V(g)T=0
\qquad(g\in G).
\tag{9}
\]
These are finitely many homogeneous linear equations in finitely many entries of \(T\), with coefficients in \(F\). Row-reduce the coefficient matrix over \(F\). Its pivot entries stay nonzero in \(\mathbb C\), and its zero rows stay zero. The same pivot and free-variable description therefore gives the kernel over \(\mathbb C\). A basis of solutions over \(F\), obtained by setting one free variable at a time equal to \(1\), becomes a basis of all solutions over \(\mathbb C\). This proves (7), including surjectivity.

For complex representations, the character inner-product formula gives
\[
\dim_{\mathbb C}\operatorname{Hom}_{\mathbb C[G]}(U_{\mathbb C},V_{\mathbb C})
=\langle\phi_V,\phi_U\rangle_G.
\]
For clarity, this follows by decomposing the two complex representations into irreducibles: if their multiplicities are \(u_\chi,v_\chi\), both sides are \(\sum_\chi u_\chi v_\chi\). The dimension of the left side of (7) is the \(F\)-dimension of its Hom space. This proves (8). \(\square\)

**Lemma 2.2 (orthogonality over \(F\)).** There are finitely many isomorphism classes of irreducible \(F\)-representations. Choose representatives \(U_1,\ldots,U_t\), and put \(\phi_j=\phi_{U_j}\). Then
\[
\langle\phi_j,\phi_k\rangle_G=0\quad(j\ne k),
\qquad
\langle\phi_j,\phi_j\rangle_G
=e_j:=\dim_F\operatorname{End}_{F[G]}(U_j)\geq1.
\tag{10}
\]
Every \(F\)-representation has a character that is a nonnegative integer combination of the \(\phi_j\).

**Proof.** Maschke's averaging argument applies over \(F\), because the nonzero integer \(|G|\) is invertible there. Explicitly, if \(W\subseteq U\) is invariant, choose an \(F\)-linear projection \(p:U\to W\) and average it:
\[
P=\frac1{|G|}\sum_{g\in G}\rho_U(g)p\rho_U(g)^{-1}.
\]
Each summand has image in \(W\) and restricts to its identity. Hence so does \(P\), and reindexing the sum proves equivariance. Thus \(\ker P\) is an invariant complement of \(W\). Induction on dimension gives complete reducibility.

If \(U\) is irreducible and \(u\ne0\), the map \(F[G]\to U\), \(a\mapsto au\), is surjective: its image is a nonzero invariant subspace. Maschke splits its kernel, so \(U\) occurs among the irreducible summands of the finite-dimensional regular representation \(F[G]\). There are consequently only finitely many possible isomorphism classes. More explicitly, a simple quotient of a finite direct sum of simple modules must be isomorphic to one summand, because at least one summand maps nontrivially to that quotient.

A nonzero homomorphism between simple modules is an isomorphism, by its kernel and image. Therefore the Hom space between nonisomorphic \(U_j,U_k\) is zero. Lemma 2.1 proves their orthogonality. The same lemma identifies the self-inner-product with the \(F\)-dimension of the endomorphism algebra. This dimension is a positive integer, since the identity endomorphism is nonzero. Finally complete reducibility gives the asserted nonnegative integer character expansion. \(\square\)

Define
\[
R_F(G)=\sum_{U\text{ an }F\text{-representation}}\mathbb Z\phi_U
=\bigoplus_{j=1}^t\mathbb Z\phi_j
\subseteq R(G).
\tag{11}
\]
The second sum is direct by (10). Its norm has the particularly useful form
\[
\left\langle\sum_j n_j\phi_j,\sum_j n_j\phi_j\right\rangle_G
=\sum_j n_j^2e_j,
\qquad n_j\in\mathbb Z.
\tag{12}
\]
The numbers \(e_j\) need not all be \(1\). They measure precisely the obstruction that this argument must remove.

For example, a generator of \(C_3\) can act on \(\mathbb Q^2\) by
\[
T=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad T^2+T+I=0.
\tag{13}
\]
This rational representation is irreducible. An invariant rational line would supply a rational eigenvalue, whereas \(x^2+x+1\) has no rational root. Its complexification has the two distinct eigenvalues \(\zeta_3,\zeta_3^{-1}\), and is the sum of the corresponding linear characters. Its character is \((2,-1,-1)\), with norm \((4+1+1)/3=2\). One can also solve \(AT=TA\) directly: the commuting rational matrices are \(aI+bT\), a two-dimensional space. This example explains why Lemma 2.2 asserts a positive integer norm, rather than automatically asserting norm one.

## 3. Cyclotomic fields give actual models

A complex representation has an \(F\)-model if it is isomorphic to \(U_{\mathbb C}\) for some \(F\)-representation \(U\). We call \(F\) a splitting field in this lesson if every complex representation of \(G\) has an \(F\)-model.

Let \(m\) be the exponent of \(G\), the least common multiple of its element orders. Write
\[
K=\mathbb Q(\mu_m),
\tag{14}
\]
where \(\mu_m\) is the set of \(m\)-th roots of unity in \(\mathbb C\). In the trivial-group case \(m=1\) and \(K=\mathbb Q\).

**Lemma 3.1 (induced lines over \(K\)).** For every subgroup \(H\leq G\) and every linear complex character \(\lambda\) of \(H\), the induced character \(\operatorname{Ind}_H^G\lambda\) belongs to \(R_K(G)\). In fact it has an actual \(K\)-model.

**Proof.** For each \(h\in H\), we have \(h^m=1\), so \(\lambda(h)^m=1\). Thus \(\lambda(h)\in\mu_m\subset K\). Let \(K_\lambda\) be the one-dimensional \(K\)-space on which \(h\) acts by \(\lambda(h)\), and form
\[
K[G]\otimes_{K[H]}K_\lambda.
\tag{15}
\]
Choose representatives \(x_1,\ldots,x_r\) for the left cosets \(G/H\). The vectors \(x_i\otimes1\) form a \(K\)-basis. If \(gx_i=x_jh\), then
\[
g(x_i\otimes1)=\lambda(h)(x_j\otimes1).
\]
Every matrix entry is \(0\) or a value of \(\lambda\), and lies in \(K\). After extending scalars to \(\mathbb C\), the same basis and action describe the complex induced representation from the induction lesson. Its character is therefore \(\operatorname{Ind}_H^G\lambda\). \(\square\)

**Theorem 3.2 (Brauer's splitting-field theorem).** Every complex representation of \(G\) has a model over \(K=\mathbb Q(\mu_m)\), where \(m\) is the exponent of \(G\).

**Proof.** Brauer's induction theorem expresses each irreducible complex character as an integer combination of characters induced from linear characters of elementary subgroups. Lemma 3.1 gives \(K\)-models of all those induced representations. Hence
\[
R_K(G)=R(G).
\tag{16}
\]
This equality concerns groups of virtual characters. We still have to prove that an irreducible character has an actual model.

Apply Lemma 2.2 with \(F=K\), and let \(\phi_1,\ldots,\phi_t\) be the characters of its simple modules. Take \(\chi\in\operatorname{Irr}(G)\). Equality (16) and complete reducibility over \(K\) give an expansion
\[
\chi=\sum_j n_j\phi_j,\qquad n_j\in\mathbb Z.
\]
Taking norms and using (12), we obtain
\[
1=\langle\chi,\chi\rangle_G=\sum_j n_j^2e_j.
\tag{17}
\]
Every \(e_j\) is a positive integer. Exactly one summand in (17) is nonzero, with \(n_j=\pm1\) and \(e_j=1\). Thus \(\chi=\phi_j\) or \(-\phi_j\). Since both \(\chi(1)\) and \(\phi_j(1)=\dim_K U_j\) are positive, the sign is positive.

The complexification \((U_j)_{\mathbb C}\) has character \(\chi\). Complete reducibility over \(\mathbb C\) and character orthogonality show that it is the desired irreducible representation. Equivalently, its norm one means that the sum of the squares of its irreducible multiplicities is one.

Finally, decompose any complex representation as a finite direct sum of irreducibles, with their nonnegative integer multiplicities. Take the same direct sum of the corresponding \(K\)-models. Its complexification is isomorphic to the original representation. \(\square\)

The proof does not require the coefficients in Brauer's expression to be nonnegative. It first works in the integer group \(R_K(G)\), and then uses (17) and positive degree to recover an actual simple module. Replacing the integers \(n_j\) by rational numbers would destroy this last step.

**Corollary 3.3.** The field \(\mathbb Q(\mu_{|G|})\) is a splitting field. More generally, every subfield \(F\subseteq\mathbb C\) containing \(\mu_m\) is a splitting field.

**Proof.** Lagrange's theorem makes every element order divide \(|G|\), hence \(m\mid |G|\) and \(\mu_m\subseteq\mu_{|G|}\). If \(K\subseteq F\), extend each \(K\)-model to \(F\) by \(F\otimes_K U\). Its subsequent complexification is the same complex representation. \(\square\)

*Proof route:* The full integer linear-character form of [Brauer's theorem](RT-FIN-11.md#theorem-5-1), Lemma 3.1, and the intertwining-map comparison in Lemmas 2.1–2.2 give the model. In particular (17) extracts an actual representation from a virtual one; rational coefficients would not suffice.

## 4. Character values do not determine the smallest coefficient field

### The quaternion group

Write
\[
Q_8=\{1,-1,a,-a,b,-b,ab,-ab\},
\qquad a^2=b^2=-1,\quad ba=-ab.
\]
Its exponent is \(4\), so Theorem 3.2 gives the field \(\mathbb Q(i)\). The two-dimensional irreducible representation can be written there explicitly:
\[
\rho(a)=A=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad
\rho(b)=B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{18}
\]
We have \(A^2=B^2=-I\) and \(BA=-AB\), so the relations hold. The eight matrices \(\pm I,\pm A,\pm B,\pm AB\) are distinct. Over \(\mathbb C\), an invariant line for \(A\) must be one of its two eigenlines, the coordinate axes. The matrix \(B\) exchanges these axes, so no line is invariant under both. The representation is irreducible.

Its character takes the values
\[
\chi(1)=2,\qquad \chi(-1)=-2,\qquad
\chi(\pm a)=\chi(\pm b)=\chi(\pm ab)=0.
\tag{19}
\]
These values are integers. Nevertheless, this irreducible representation has no two-dimensional real model, and consequently no rational model.

Here is a direct proof. In a proposed real model, write \(J=\rho(a)\) and \(D=\rho(b)\). Then \(J^2=D^2=-I\) and \(DJ=-JD\). For any nonzero real vector \(v\), the vectors \(v,Jv\) are independent: dependence would give a real eigenvalue of \(J\), whose square would have to be \(-1\). In this basis,
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Solving \(DJ=-JD\) gives
\[
D=\begin{pmatrix}r&s\\s&-r\end{pmatrix},
\qquad D^2=(r^2+s^2)I,
\quad r,s\in\mathbb R.
\tag{20}
\]
This cannot equal \(-I\). A rational model would become such a real model after extension of scalars, so it is also impossible.

Thus having a character with values in \(F\) is necessary for an \(F\)-model, but need not be sufficient. Theorem 3.2 establishes a model by constructing a character lattice and controlling its positive integer norms. It does not identify the field of character values with a splitting field.

### Symmetric groups

For \(S_n\), disjoint-cycle decomposition gives
\[
\operatorname{exp}(S_n)=\operatorname{lcm}(1,2,\ldots,n).
\tag{21}
\]
Every permutation order divides this least common multiple. Conversely, each \(r\leq n\) occurs as the order of an \(r\)-cycle, so the exponent is divisible by every such \(r\). Lagrange's theorem also gives \(\operatorname{exp}(S_n)\mid n!\).

The cyclotomic field in Theorem 3.2 is therefore sufficient, but it need not be the smallest choice. The next lesson on Young symmetrizers will construct all irreducible representations of \(S_n\) over \(\mathbb Q\). This is a further construction, not a consequence of rational character values alone.

For \(S_3\) we can already see the smaller field directly. Its standard plane has a rational basis \(e_1-e_3,e_2-e_3\). In that basis, the transpositions \((12),(23)\) act by
\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
T=\begin{pmatrix}1&0\\-1&-1\end{pmatrix}.
\tag{22}
\]
Both square to \(I\), and \((ST)^3=I\). The two eigenlines of \(S\) are spanned by \((1,1)\) and \((1,-1)\). The matrix \(T\) takes these vectors to \((1,-2)\) and \((1,0)\), respectively, neither on its original line. Hence the plane is irreducible over \(\mathbb C\). Together with the rational trivial and sign representations, its degree squares sum to \(1+1+4=6\), so these are all irreducibles. Here \(\mathbb Q\) splits the group, whereas the exponent is \(6\).

## 5. Why integer induction matters for Artin L-functions

This section is a pointer to number theory. Let \(L/F\) be a finite Galois extension of number fields, with group \(G\). The notation \(F\) here denotes a number field; it is separate from the coefficient fields in the preceding sections. The Artin L-function \(L(s,\chi;L/F)\) is initially defined by its Euler product in \(\operatorname{Re}s>1\).

The following arithmetic facts are additional premises for this application. They are not used in the finite-group theorems of §§1–4:

1. Addition of virtual characters becomes multiplication of their Artin L-functions. Integer coefficients become integer powers. [Artin L-functions, conductors and discriminants, Proposition 21.1](../../NT-CFT/src/artin-l-functions-conductors-and-discriminants.md#1-euler-factors-and-induction) proves this by the Euler-factor determinant.
2. If \(H\leq G\), \(F_H=L^H\), and \(\lambda\) is a character of \(H\), then
   \[
   L(s,\operatorname{Ind}_H^G\lambda;L/F)
   =L(s,\lambda;L/F_H).
   \tag{23}
   \]
   The same Proposition 21.1 proves this at ramified as well as unramified primes, using inertia invariants and a cyclic-block determinant.
3. For a linear character \(\lambda\), the latter function is the Hecke L-function of the associated finite-order ray class character. It has meromorphic continuation to \(\mathbb C\). The rank-one identification is [Theorem 21.2](../../NT-CFT/src/artin-l-functions-conductors-and-discriminants.md#2-rank-one-and-primitive-hecke-characters), with arithmetic Frobenius and the primitive Euler product. The analytic input is Theorem 10.1 of *Hecke L-functions and the Dedekind zeta function*. Its [exact provider record](../../NT-CFT/proof-dependencies.html#NT-ADL-10) records an owner-supplied proof not yet included in the selected reader. Thus the continuation deduction here is conditional on that analytic input; a provider record itself is not its proof.

Now let \(\chi\) be any complex character. Brauer's theorem gives
\[
\chi=\sum_i a_i\operatorname{Ind}_{E_i}^G\lambda_i,
\qquad a_i\in\mathbb Z,
\]
with each \(\lambda_i\) linear. The preceding identities give, initially in the Euler-product half-plane,
\[
L(s,\chi;L/F)
=\prod_i L(s,\lambda_i;L/L^{E_i})^{a_i}.
\tag{24}
\]
Every factor on the right has meromorphic continuation. It is not identically zero: its convergent Euler product is nonzero in \(\operatorname{Re}s>1\). Its reciprocal is therefore also meromorphic. Equation (24) constructs a meromorphic continuation of the left side. The same argument works for virtual characters.

The integer exponents are essential to this deduction. An \(N\)-th root of a meromorphic function need not be meromorphic on the whole plane: a zero of order not divisible by \(N\) would require a noninteger order for the root. Brauer's theorem avoids this issue. On the other hand, negative exponents can turn zeros of the Hecke factors into poles. This argument proves meromorphy; it does not establish a general absence of poles for nontrivial irreducible characters.

*Further proof route:* [Artin L-functions, conductors and discriminants, Theorem 21.3](../../NT-CFT/src/artin-l-functions-conductors-and-discriminants.md#5-meromorphy-and-the-functional-equation-over-number-fields) gives the same deduction with completed factors and a functional equation, under the analytic input recorded there. The finite representation-theoretic result used by that argument is the complete integer Brauer theorem of this course.

## 6. Exercises with complete solutions

### Exercise 1. When a cyclic group needs all its roots

Let \(C_m=\langle c\rangle\). Show first that a subfield \(F\subseteq\mathbb C\) is a splitting field for \(C_m\) if and only if it contains \(\mu_m\). If \(m\not\equiv2\pmod4\), prove that \(\mathbb Q(\mu_d)\) is not a splitting field for any proper positive divisor \(d\mid m\). Explain the exception when \(m=2u\) with \(u\) odd.

**Solution.** The faithful complex line on which \(c\) acts by a primitive root \(\zeta_m\) must have an \(F\)-model if \(F\) splits \(C_m\). The dimension of a model equals the complex dimension, so that model is a line over \(F\). The action of \(c\) is a scalar in \(F\), and after complexification it must be \(\zeta_m\). Hence \(\zeta_m\in F\), which implies \(\mu_m\subset F\).

Conversely, on any complex representation the generator satisfies \(T^m=I\). The polynomial \(x^m-1\) has distinct roots, so \(T\) is diagonalizable with eigenvalues in \(\mu_m\). If these roots lie in \(F\), take an \(F\)-basis of the same size and prescribe the same diagonal matrix. This gives an \(F\)-model of the representation.

Now suppose \(d\mid m\). The inclusion \(\mu_d\subseteq\mu_m\) gives
\[
\mathbb Q(\mu_d)\subseteq\mathbb Q(\mu_m).
\]
The cyclotomic degree calculation from the rationality lesson gives
\[
[\mathbb Q(\mu_r):\mathbb Q]=\varphi(r),
\qquad
\varphi(p^a)=p^{a-1}(p-1)\quad(a\geq1),
\quad \varphi(1)=1.
\tag{25}
\]
Here the prime-power formula counts the \(p^a\) residue classes and removes the \(p^{a-1}\) multiples of \(p\). To see multiplicativity directly, let \(u,v\) be coprime. Reduction maps an invertible residue modulo \(uv\) to a pair of invertible residues modulo \(u,v\). This map is injective, since divisibility by both coprime integers implies divisibility by their product. It is surjective: if \(au+bv=1\), the integer \(s bv+t au\) has prescribed residues \(s\) modulo \(u\) and \(t\) modulo \(v\), and is invertible modulo \(uv\) when both prescribed residues are invertible. Counting gives \(\varphi(uv)=\varphi(u)\varphi(v)\).

Write \(m=\prod_p p^{a_p}\), \(d=\prod_p p^{b_p}\), where \(0\leq b_p\leq a_p\). The multiplicative formula expresses \(\varphi(d)/\varphi(m)\) as the product of the corresponding prime-power ratios.

If \(0<b_p<a_p\), the ratio is \(p^{b_p-a_p}<1\). If \(b_p=0<a_p\), it is \(1/(p^{a_p-1}(p-1))\). For odd \(p\) this is less than \(1\); for \(p=2\) it is less than \(1\) when \(a_p\geq2\). The only decrease of an exponent that leaves the ratio equal to \(1\) is the removal of a single factor \(2\) when \(a_2=1\).

If \(m\not\equiv2\pmod4\), then \(a_2\ne1\). Every proper divisor decreases at least one prime exponent, and at that prime the ratio is strictly less than \(1\). All other ratios are at most \(1\). Therefore \(\varphi(d)<\varphi(m)\). The two nested cyclotomic fields have different degrees, so they are different. In particular, \(\mathbb Q(\mu_d)\) cannot contain \(\zeta_m\), and the first part shows that it does not split \(C_m\). For \(m=1\) there is no proper positive divisor, so the assertion is vacuous.

If \(m=2u\) with \(u\) odd, choose the usual complex roots. Then
\[
\zeta_u=\zeta_{2u}^2,
\qquad
\zeta_{2u}=-\zeta_u^{(u+1)/2}.
\tag{26}
\]
Thus \(\mathbb Q(\mu_{2u})=\mathbb Q(\mu_u)\). The proper divisor \(u\) already supplies a splitting field, including \(u=1\), where both fields equal \(\mathbb Q\).

### Exercise 2. An explicit quaternion model

Construct the two-dimensional irreducible representation of \(Q_8\) over \(\mathbb Q(i)\). Verify the relations, irreducibility after complexification, and its character. Show directly why its integer character values do not yield a rational model.

**Solution.** On \(\mathbb Q(i)^2\), define
\[
A=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Their products satisfy
\[
A^2=B^2=-I,\qquad
AB=\begin{pmatrix}0&i\\i&0\end{pmatrix},
\qquad BA=-AB.
\]
Sending \(a\) to \(A\), \(b\) to \(B\), and the central element \(-1\) to \(-I\) therefore respects the quaternion relations. The matrices \(\pm I,\pm A,\pm B,\pm AB\) are distinct, giving the eight group elements faithfully.

A complex invariant line would have to be an eigenline of \(A\). Since its eigenvalues \(i,-i\) are distinct, these are exactly the two coordinate lines. The matrix \(B\) takes each into the other. No line is invariant under the group, so the two-dimensional complexification is irreducible.

The traces are \(2\) on \(I\), \(-2\) on \(-I\), and \(0\) on the other six matrices. Its norm is
\[
\frac18\bigl(2^2+(-2)^2+6\cdot0^2\bigr)=1,
\]
also confirming irreducibility by complex character theory.

For a rational model, extension to \(\mathbb R\) would produce real matrices \(J,D\) with \(J^2=D^2=-I\) and \(DJ=-JD\). For a nonzero vector \(w\), the pair \(w,Jw\) is a real basis, since \(J\) has no real eigenvalue. In this basis \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\). Solving the anticommutation relation gives \(D=\left(\begin{smallmatrix}r&s\\s&-r\end{smallmatrix}\right)\), whose square is \((r^2+s^2)I\). It cannot have square \(-I\). Hence no rational model exists. The character values describe traces, while a model must satisfy all the matrix relations simultaneously.

### Exercise 3. Why cyclic subgroups do not detect the integer lattice

Let \(G=C_2\times C_2=\{1,a,b,ab\}\), and define the class function \(\theta=2\delta_1\), where \(\delta_1\) is \(1\) at the identity and \(0\) elsewhere. Prove that the restriction of \(\theta\) to every cyclic subgroup is a virtual character, but \(\theta\notin R(G)\).

**Solution.** Every element has order \(1\) or \(2\). For an order-two subgroup \(C=\{1,x\}\), let \(\varepsilon_C\) be its nontrivial linear character. Then
\[
\theta|_C(1)=2,\qquad\theta|_C(x)=0,
\qquad \theta|_C=1_C+\varepsilon_C.
\tag{27}
\]
This is an actual character, namely the regular character of \(C\). On the trivial subgroup, the restriction is twice its trivial character. These exhaust the cyclic subgroups.

The four irreducible characters of \(G\) are its four linear characters. Explicitly, choose \(\lambda(a),\lambda(b)\) independently in \(\{1,-1\}\) and put \(\lambda(ab)=\lambda(a)\lambda(b)\). Their pairwise inner products are \(0\) for distinct choices and \(1\) for equal choices; for example the sum over \(G\) factors into the two sums over \(C_2\). Their degree squares sum to \(4\), so the list is complete.

For each of these four \(\lambda\),
\[
\langle\theta,\lambda\rangle_G
=\frac14\theta(1)\overline{\lambda(1)}
=\frac12.
\tag{28}
\]
Thus \(\theta=\frac12\sum_\lambda\lambda\), and its irreducible coefficients are not integers. It is not a virtual character. The full group \(G\) is itself \(2\)-elementary, so Theorem 1.2 detects the failure upon restricting to \(G\). Checking only its cyclic subgroups misses it.

This example distinguishes the two induction theorems: rational combinations induced from cyclic subgroups do not force membership in the integer lattice.

### Exercise 4. A complete splitting-field proof using supports

Prove that \(K=\mathbb Q(\mu_m)\) splits \(G\), where \(m=\operatorname{exp}(G)\). Include the comparison of intertwining maps under scalar extension and the orthogonality of characters of distinct irreducible \(K\)-representations. Finish using the supports of their complex character decompositions.

**Solution.** Let \(U,V\) be finite-dimensional \(K\)-representations. Choose bases. An equivariant matrix \(T\) is a solution of the finite system \(T\rho_U(g)=\rho_V(g)T\), with all coefficients in \(K\). Row-reducing over \(K\) gives pivot and free variables. The pivots remain nonzero after extension to \(\mathbb C\), so the same free-variable basis spans all complex solutions. Hence
\[
\mathbb C\otimes_K\operatorname{Hom}_{K[G]}(U,V)
\simeq\operatorname{Hom}_{\mathbb C[G]}(U_{\mathbb C},V_{\mathbb C}).
\tag{29}
\]
Complex character theory then gives
\[
\langle\phi_V,\phi_U\rangle_G
=\dim_K\operatorname{Hom}_{K[G]}(U,V).
\]
If \(U,V\) are nonisomorphic simple \(K\)-modules, any nonzero homomorphism would be an isomorphism, so this inner product is zero. For \(U=V\), the self-inner-product is the positive integer \(\dim_K\operatorname{End}_{K[G]}(U)\). This proves the required orthogonality without assuming that the endomorphism algebra is just \(K\).

Maschke's averaging gives complete reducibility over \(K\). There are only finitely many simple isomorphism classes: each simple module is a quotient of \(K[G]\), by choosing one nonzero generating vector, and a quotient splits. Therefore it occurs among the finitely many simple summands of \(K[G]\). Let these simple classes have characters \(\phi_1,\ldots,\phi_t\). Each complexification is completely reducible, so write
\[
\phi_j=\sum_{\alpha\in\operatorname{Irr}(G)}m_{j,\alpha}\alpha,
\qquad m_{j,\alpha}\in\mathbb Z_{\geq0}.
\tag{30}
\]
For \(j\ne k\), orthogonality says
\[
0=\langle\phi_j,\phi_k\rangle_G
=\sum_\alpha m_{j,\alpha}m_{k,\alpha}.
\tag{31}
\]
All summands are nonnegative. Thus no complex irreducible can occur in two distinct \(\phi_j\): their supports are disjoint.

For every subgroup \(H\) and linear character \(\lambda\) of \(H\), the values satisfy \(\lambda(h)^m=1\). They lie in \(K\). With left coset representatives \(x_i\), prescribe the induced action \(g(x_i\otimes1)=\lambda(h)(x_j\otimes1)\) whenever \(gx_i=x_jh\). These are matrices over \(K\), and their complexification is the usual induced representation. Thus every character induced from a linear character has a \(K\)-model.

Take any \(\chi\in\operatorname{Irr}(G)\). The full integer Brauer theorem and the preceding induced models express \(\chi\) as an integer combination of characters of \(K\)-representations. Decomposing those representations over \(K\) gives
\[
\chi=\sum_j n_j\phi_j,\qquad n_j\in\mathbb Z.
\tag{32}
\]
At least one \(n_j\) is nonzero. For any such \(j\), every constituent \(\alpha\) of \(\phi_j\) contributes \(n_jm_{j,\alpha}\ne0\) to (32). By disjointness of supports, no other term can cancel it. The left side is supported only on \(\chi\), so \(\phi_j\) is supported only on \(\chi\). There is exactly one such \(j\), again by disjointness, and \(\phi_j=a\chi\) for an integer \(a>0\). Comparing the coefficient of \(\chi\) gives \(1=n_ja\). Since \(n_j\) is an integer and \(a>0\) is an integer, \(n_j=a=1\).

Thus \(\phi_j=\chi\), and its complexification is irreducible and isomorphic to the representation with character \(\chi\). Taking direct sums with the multiplicities in any complex representation gives its \(K\)-model. This completes the proof, including both scalar-extension orthogonality and the recovery of an actual model from integer induction.

## 7. Results used without proof

From the earlier character lessons we use complex complete reducibility, Schur's lemma, orthonormality and completeness of irreducible characters, character determination, the regular-representation degree-square sum, and the Hom interpretation of inner products. The averaging proof over an arbitrary coefficient subfield is also given in Lemma 2.2 above.

From the induction lesson we use the coset model and its normalized character formula. Lemma 1.1 proves the projection formula for arbitrary class functions directly. From Artin's induction theorem and rationality, Lemma 1.1, we use cyclotomic irreducibility and \([\mathbb Q(\mu_r):\mathbb Q]=\varphi(r)\) in Exercise 1. From Brauer's induction theorem, Theorem 5.1, we use the full integer combination of characters induced from linear characters of elementary subgroups.

The arithmetic facts used only in Section 5 are explicitly listed there: the virtual-character multiplication and induction identities, the class-field identification of a linear Artin character with a finite-order Hecke character, and meromorphic continuation of its Hecke L-function. They are not premises for either of the algebraic theorems.

The general rational construction for \(S_n\) is a forward result of the next lesson. No Schur-index theorem or classification of general semisimple algebras is needed here.

## References

[Kramár] János Kramár, *Artin's and Brauer's Theorems on Induced Characters* (2005), Section 3. [Open exposition](https://www.math.utoronto.ca/murnaghan/courses/mat445/artinbrauer.pdf).
