# The group algebra and Fourier analysis on a finite group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

Multiplication in a group algebra initially looks like a long convolution sum. Its irreducible representations turn that multiplication into independent matrix multiplications. This makes Fourier inversion a statement about finite-dimensional algebras and makes character theory a tool for counting solutions of equations in a group.

We use [Characters and the orthogonality relations](RT-FIN-02.md): matrix-coefficient orthogonality, the decomposition of the regular representation, and the character inner product. All vector spaces in this lesson are finite-dimensional over \(\mathbb C\). Write \(n=|G|\), choose one representative \(\rho_i:G\to\operatorname{GL}(V_i)\) of each irreducible isomorphism class, and put \(d_i=\dim V_i\), \(\chi_i=\operatorname{tr}\rho_i\). References and the exact boundary of the lesson appear at the end.

## 1. Convolution becomes matrix multiplication

Identify a function \(f:G\to\mathbb C\) with \(\sum_g f(g)g\in\mathbb C[G]\). Multiplication becomes

\[
(f*h)(g)=\sum_{x\in G}f(x)h(x^{-1}g).
\]

The delta function at the identity is the unit. Define the **Fourier transform**

\[
\widehat f(i)=\sum_{g\in G}f(g)\rho_i(g)\in\operatorname{End}(V_i).
\tag{1}
\]

Our convention uses \(\rho_i(g)\). For an abelian group, the convention using the conjugate of a character gives the same transform after replacing that character by its inverse. This change of index matters when comparing inversion formulas.

**Theorem 1.1 (Fourier decomposition).** The map

\[
\mathcal F:\mathbb C[G]\longrightarrow
\bigoplus_i\operatorname{End}(V_i),\qquad
f\longmapsto(\widehat f(i))_i
\tag{2}
\]

is an isomorphism of unital complex algebras.

**Proof.** Substitute \(g=xy\) in the convolution sum:

\[
\widehat{f*h}(i)=
\sum_{x,y}f(x)h(y)\rho_i(xy)
=\widehat f(i)\widehat h(i).
\]

The unit maps to the identity in every block. Suppose all blocks of \(f\) vanish. The preceding lesson gives the regular representation as \(\bigoplus_i V_i^{\oplus d_i}\). Therefore left multiplication by \(f\) vanishes on \(\mathbb C[G]\). Applying it to the unit gives \(f=0\). This proves injectivity. Finally,

\[
\dim\mathbb C[G]=n=\sum_i d_i^2
=\dim\bigoplus_i\operatorname{End}(V_i),
\]

so the injective linear map is surjective. \(\square\)

The crucial faithfulness here is faithfulness of the **algebra** acting on its regular module: \(a\cdot1=a\). A faithful action of the group on an arbitrary vector space does not by itself give an injective action of its group algebra. For example, a faithful character of a nontrivial cyclic group acts on a one-dimensional space, whereas its group algebra has larger dimension.

### Recovering coefficients

The regular character is \(n\) at the identity and zero elsewhere, and equals \(\sum_i d_i\chi_i\). Thus

\[
\frac1n\sum_i d_i\chi_i(g^{-1}x)=
\begin{cases}1&x=g,\\0&x\ne g.\end{cases}
\]

Multiplying by \(f(x)\) and summing gives:

**Proposition 1.2 (inversion).** For every \(g\in G\),

\[
f(g)=\frac1n\sum_i d_i
\operatorname{tr}\bigl(\rho_i(g^{-1})\widehat f(i)\bigr).
\tag{3}
\]

This also writes down the inverse of (2) on an arbitrary tuple of matrices. In particular, a matrix \(A\) in block \(i\), with all other blocks zero, corresponds to the function

\[
g\longmapsto\frac{d_i}{n}
\operatorname{tr}\bigl(\rho_i(g^{-1})A\bigr).
\tag{4}
\]

### The inner product

Choose invariant Hermitian inner products on the \(V_i\), so that their matrices are unitary. The adjoint of a group-algebra element is the function

\[
f^\star(g)=\overline{f(g^{-1})}.
\]

Directly from (1), \(\widehat{f^\star}(i)=\widehat f(i)^*\). Moreover,

\[
(f*h^\star)(1)=\sum_g f(g)\overline{h(g)}.
\]

Apply inversion at the identity to \(f*h^\star\). We obtain the polarized form of Plancherel:

**Proposition 1.3 (Plancherel).**

\[
\sum_g f(g)\overline{h(g)}
=\frac1n\sum_i d_i
\operatorname{tr}\bigl(\widehat f(i)\widehat h(i)^*\bigr).
\tag{5}
\]

In particular,

\[
\sum_g|f(g)|^2=\frac1n\sum_i d_i
\|\widehat f(i)\|_{\mathrm{HS}}^2.
\tag{6}
\]

The adjoint in these formulas refers to the chosen invariant inner products. In a nonorthonormal basis, taking the ordinary conjugate transpose of the displayed coordinate matrix need not compute that adjoint.

## 2. Seeing every block for the smallest nonabelian group

Let \(r=(123)\), \(s=(12)\) in \(S_3\); permutations act on the left and products act from right to left. The irreducibles are trivial, sign, and the standard plane

\[
W=\{(z_1,z_2,z_3):z_1+z_2+z_3=0\}.
\]

In the basis \(a=e_1-e_2,\ b=e_2-e_3\), their standard matrices are

\[
R=\rho_W(r)=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
S=\rho_W(s)=\begin{pmatrix}-1&1\\0&1\end{pmatrix}.
\tag{7}
\]

Indeed \(ra=b,\ rb=-a-b,\ sa=-a,\ sb=a+b\). One checks \(R^3=S^2=I\) and \(SRS=R^{-1}\). The basis is convenient for arithmetic but is not orthonormal.

Write a group-algebra element uniquely as

\[
f=\sum_{j=0}^2\bigl(a_j r^j+b_jr^js\bigr).
\]

The complete isomorphism \(\mathbb C[S_3]\cong\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)\) is

\[
f\longmapsto
\left(\sum_j(a_j+b_j),\
\sum_j(a_j-b_j),\
\sum_j(a_jR^j+b_jR^jS)\right).
\tag{8}
\]

Formula (3) recovers all six coefficients, so this is also an explicit description in both directions.

Now let \(S_3\) act on \(\mathbb C^3\) by permuting coordinates. Its trivial-isotypic projection is

\[
P_{\mathrm{triv}}(z)=
\frac{z_1+z_2+z_3}{3}(1,1,1).
\tag{9}
\]

There is no sign constituent, so \(P_{\mathrm{sign}}=0\). The standard-isotypic projection is \(I-P_{\mathrm{triv}}\). In the next section these projections arise from fixed elements of the group algebra, independently of this realization.

## 3. Central elements select representation types

For a conjugacy class \(C\), write \(K_C=\sum_{g\in C}g\). A group-algebra element \(\sum_g a_gg\) commutes with every \(h\in G\) exactly when \(a_g=a_{hgh^{-1}}\). Since the group elements span the algebra, this is exactly the condition for centrality. Thus the class sums form a basis of \(Z(\mathbb C[G])\).

The centre of \(M_d(\mathbb C)\) consists of scalar matrices: commuting with diagonal matrix units forces an operator to be diagonal, and commuting with off-diagonal units forces its diagonal entries to agree. The Fourier isomorphism therefore identifies the centre with \(\mathbb C^r\), where \(r\) is the number of irreducible types. Comparing the two bases again gives equality between the numbers of conjugacy classes and irreducibles. It supplies no distinguished bijection between those sets.

**Theorem 3.1 (central idempotents).** The elements

\[
e_i=\frac{d_i}{n}\sum_{g\in G}\chi_i(g^{-1})g
\tag{10}
\]

are all the primitive central idempotents of \(\mathbb C[G]\). They satisfy

\[
e_ie_j=\delta_{ij}e_i,\qquad \sum_i e_i=1.
\tag{11}
\]

On any representation, \(e_i\) acts as the projection onto its \(V_i\)-isotypic component.

**Proof.** The coefficient function in (10) is a class function, so \(e_i\) is central. On \(V_j\), Schur's lemma makes its action a scalar \(\lambda_{ij}I\). Its trace is

\[
d_j\lambda_{ij}
=\frac{d_i}{n}\sum_g\chi_i(g^{-1})\chi_j(g)
=d_i\delta_{ij}.
\]

Hence \(\lambda_{ij}=\delta_{ij}\). Under (2), \(e_i\) is exactly the tuple with identity in block \(i\) and zero in all other blocks. This proves (11). A central idempotent in \(\mathbb C^r\) has every coordinate equal to zero or one. The nonzero ones that cannot split into two nonzero orthogonal central idempotents have exactly one coordinate equal to one. These are precisely the \(e_i\). Finally decompose any representation into irreducibles. On every copy of \(V_j\), the action is \(\delta_{ij}I\), proving the isotypic assertion. \(\square\)

Here “primitive central” concerns splitting among **central** idempotents. It does not assert primitivity among all idempotents. If \(d_i>1\), the identity in its matrix block splits into diagonal matrix units.

**Proposition 3.2 (class sums).** For \(c\in C\), the class sum acts on \(V_i\) by

\[
\omega_i(C)=\frac{|C|\chi_i(c)}{d_i},\qquad
K_C=\sum_i\frac{|C|\chi_i(c)}{d_i}e_i.
\tag{12}
\]

**Proof.** The central operator is scalar by Schur's lemma. Its trace is \(|C|\chi_i(c)\), so division by \(d_i\) gives the scalar. Its scalars in all blocks uniquely determine it by (2), giving the expansion. \(\square\)

For \(S_3\), put \(T\) equal to the sum of its three transpositions and \(Q=r+r^2\). Then

\[
e_{\mathrm{triv}}=\frac{1+T+Q}{6},\qquad
e_{\mathrm{sign}}=\frac{1-T+Q}{6},\qquad
e_{\mathrm{std}}=\frac{2-Q}{3}.
\tag{13}
\]

On the permutation module the first is (9), the second is zero, and the third is its complementary standard projection. Their coefficients and (11) can also be checked from

\[
T^2=3\cdot1+3Q,\qquad Q^2=2\cdot1+Q,\qquad TQ=QT=2T.
\tag{14}
\]

For example, among the nine ordered products of transpositions, three are the identity and the other six give each 3-cycle three times.

## 4. Counting products and commutators

**Theorem 4.1 (class-product count).** For classes \(C,D\), representatives \(c,d\), and a fixed \(z\in G\), the number of ordered pairs \(x\in C,\ y\in D\) with \(xy=z\) is

\[
N_{C,D}(z)=\frac{|C||D|}{n}
\sum_i\frac{\chi_i(c)\chi_i(d)\chi_i(z^{-1})}{d_i}.
\tag{15}
\]

Over \(\mathbb C\), \(\chi_i(z^{-1})=\overline{\chi_i(z)}\).

**Proof.** The desired number is the coefficient of \(z\) in \(K_CK_D\). Multiplying (12) and using (11) gives

\[
K_CK_D=\sum_i
\frac{|C||D|\chi_i(c)\chi_i(d)}{d_i^2}e_i.
\]

The coefficient of \(z\) in (10) is \(d_i\chi_i(z^{-1})/n\); substituting it proves (15). \(\square\)

This counts pairs with one **fixed product**. To count pairs whose product lies anywhere in a third class, multiply by that class's size.

For instance, using the \(S_3\) rows \((1,1,1),(1,-1,1),(2,0,-1)\), ordered by identity, transposition, 3-cycle, formula (15) gives three products of two transpositions equal to the identity, zero equal to a transposition, and three equal to each 3-cycle, exactly as in (14).

**Theorem 4.2 (commutator count).** With \([x,y]=xyx^{-1}y^{-1}\),

\[
\#\{(x,y)\in G^2:[x,y]=z\}
=n\sum_i\frac{\chi_i(z)}{d_i}.
\tag{16}
\]

**Proof.** We first record the averaging identity

\[
\sum_{x\in G}\rho_i(x)A\rho_i(x^{-1})
=\frac{n\,\operatorname{tr}A}{d_i}I.
\tag{17}
\]

The left side commutes with \(G\) by a change of variable, so it is scalar; taking its trace computes that scalar.

Let \(B=\sum_{x,y}[x,y]\in\mathbb C[G]\). Conjugating both variables shows that \(B\) is central. In its \(i\)-th block, use (17) with \(A=\rho_i(y)\):

\[
\widehat B(i)=\frac n{d_i}\sum_y\chi_i(y)\rho_i(y^{-1}).
\]

This is scalar, and its trace is

\[
\frac n{d_i}\sum_y\chi_i(y)\chi_i(y^{-1})=\frac{n^2}{d_i}.
\]

Thus \(\widehat B(i)=n^2d_i^{-2}I\). Inversion yields the coefficient

\[
B(z)=n\sum_i\frac{\chi_i(z^{-1})}{d_i}.
\]

Duality permutes the irreducibles without changing their dimensions and replaces \(\chi_i(z)\) by \(\chi_i(z^{-1})\). Reindexing gives (16). Equivalently, swapping \(x,y\) sends the commutator to its inverse, so the count has the same value at \(z\) and \(z^{-1}\). \(\square\)

At \(z=1\), every quotient \(\chi_i(1)/d_i\) is one. Consequently the number of commuting ordered pairs is \(n\,k(G)\), where \(k(G)\) is the number of classes.

## 5. Exercises with solutions

### Exercise 1. The two generators of \(S_3\)

Give the images of \((12)\) and \((123)\) under the isomorphism with \(\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)\). Verify the relations and recover the coefficient of the identity from an arbitrary tuple.

**Solution.** In the conventions of (7), the images are

\[
s\longmapsto(1,-1,S),\qquad r\longmapsto(1,1,R).
\]

The matrices obey \(S^2=I,\ R^3=I,\ SRS=R^{-1}\), while the two scalar components obey the same relations. For a tuple \((u,v,A)\), inversion at the identity gives

\[
f(1)=\frac{u+v+2\operatorname{tr}A}{6}.
\]

More generally \(f(g)=(u+\operatorname{sgn}(g)v+
2\operatorname{tr}(\rho_W(g^{-1})A))/6\). These six coefficients exhibit the entire inverse, rather than only verifying a homomorphism on generators.

### Exercise 2. How often do elements commute?

Show that the commuting probability is \(k(G)/|G|\), and that for a nonabelian finite group it is at most \(5/8\).

**Solution.** For each \(x\), there are \(|C_G(x)|\) possible commuting \(y\). A class containing \(x\) has \(n/|C_G(x)|\) elements, so its total contribution is \(n\). Summing over classes gives \(nk(G)\) and division by \(n^2\) gives the probability.

Write \(Z=Z(G)\). If \(x\notin Z\), its centralizer is a proper subgroup and has size at most \(n/2\). Hence

\[
\operatorname{cp}(G)\le
\frac{|Z|n+(n-|Z|)n/2}{n^2}
=\frac12+\frac{|Z|}{2n}.
\]

If \(G/Z\) were cyclic, choose \(aZ\) generating it. Every element would have the form \(a^rz\), and any two such elements commute. Therefore a nonabelian \(G\) has noncyclic \(G/Z\). Groups of orders two and three are cyclic, so \(|G:Z|\ge4\). The bound is at most \(1/2+1/8=5/8\). For the dihedral group of order eight, the centre has size two and every noncentral centralizer has size four, giving equality.

### Exercise 3. The scalar hidden in a commutator sum

Prove (16) by computing the Fourier block of \(\sum_{x,y}[x,y]\). Explain both the factor \(d_i^{-2}\) in the block and the factor \(d_i^{-1}\) in the final count.

**Solution.** Averaging over \(x\) gives

\[
\sum_x\rho_i(xyx^{-1}y^{-1})
=\frac{n\chi_i(y)}{d_i}\rho_i(y^{-1}).
\]

Sum over \(y\). The result is central; its trace is \(n^2/d_i\), by row orthogonality. A scalar matrix on a \(d_i\)-dimensional space has trace \(d_i\) times its scalar, so the block is \(n^2/d_i^2\) times the identity. Inversion contributes \(d_i/n\) and the trace of \(\rho_i(z^{-1})\), producing \(n\chi_i(z^{-1})/d_i\). Summing over \(i\) and pairing each row with its dual gives (16). The second division by \(d_i\) occurs when passing from the block's trace to its scalar.

### Exercise 4. Every element of \(A_5\) is a commutator

Use (16) to prove the assertion. Supply the character information needed for the count.

**Solution.** The five classes are \(1\), double transpositions \(2A\), 3-cycles \(3A\), and two classes \(5A,5B\) of 5-cycles. Their sizes are

\[
1,\quad15,\quad20,\quad12,\quad12.
\]

The cycle counts give the first three sizes. The centralizer of a 5-cycle in \(A_5\) is its cyclic subgroup of order five, giving size twelve; the twenty-four 5-cycles therefore form two classes. Conjugation sending a generator to its inverse is even, whereas conjugation sending it to its square is odd: on its four nonidentity powers these permutations have signs \(+1\) and \(-1\), respectively. Thus a cycle and its inverse are in the same class, and its square is in the other. The other classes also equal their inverse classes.

Here is a derivation of the table, so the exercise does not presuppose a later lesson. The action on five letters has character \((5,1,2,0,0)\). Removing the invariant line gives

\[
\chi_4=(4,0,1,-1,-1).
\]

Its weighted norm is \((16+20+24)/60=1\), so it is irreducible.

There are six cyclic subgroups of order five, as counted in Lemma 6.1 below. Their normalizers have order ten and are dihedral: even automorphisms of a chosen 5-cycle induce exactly inversion and identity. Each normalizer contains five involutions. Double-counting incidences of involutions and these six normalizers gives \(6\cdot5/15=2\) fixed subgroups for each involution. A 3-cycle fixes none since it cannot belong to a normalizer of order ten. A 5-cycle fixes exactly its own subgroup: if it normalizes another cyclic group of order five, its induced automorphism has order dividing both five and four, so it centralizes that group, which then lies in its centralizer. The character of this six-point action is \((6,2,0,1,1)\). Removing its invariant line gives

\[
\chi_5=(5,1,-1,0,0),
\]

whose weighted norm is \((25+15+20)/60=1\).

We justify the remaining degree-three rows. The class sizes also prove simplicity of \(A_5\): the order of a normal subgroup is one plus a subset sum of \(15,20,12,12\), and no proper value greater than one divides sixty. There are no nontrivial one-dimensional representations, since a homomorphism from this nonabelian simple group to an abelian group cannot be injective. There are five irreducibles by the class count. After degrees \(1,4,5\), the squares of the two remaining degrees sum to \(60-1-16-25=18\); both degrees are at least two, so both are three.

Each of these representations is faithful, and its determinant is trivial. At an involution its eigenvalues must be \(1,-1,-1\), giving trace \(-1\). At a 3-cycle, determinant one permits either three equal cube roots or the three distinct cube roots. Three equal roots would make the operator scalar; faithfulness would then make the group element central, which it is not. The trace is therefore zero.

At a 5-cycle the character is real, since its class equals its inverse class. Write its three eigenvalues as powers of a primitive fifth root \(\zeta\). If \(m_j\) is the multiplicity of \(\zeta^j\), real trace gives \(\sum_j(m_j-m_{-j})\zeta^j=0\). The only rational relation among these five powers is a multiple of \(1+\zeta+\cdots+\zeta^4=0\); its coefficient at \(j=0\) is zero, so every difference vanishes. The multiset is inversion-stable. Faithfulness and dimension three force it to be \(1,\zeta^a,\zeta^{-a}\) with \(a\ne0\). Its trace is either

\[
\varphi=\frac{1+\sqrt5}{2}\quad\text{or}\quad
\varphi'=\frac{1-\sqrt5}{2}.
\]

Squaring the cycle interchanges these values. Orthogonality of the two remaining rows prevents their being equal. Up to naming them, the full table is

| Degree | \(1\) | \(2A\) | \(3A\) | \(5A\) | \(5B\) |
|---|---:|---:|---:|---:|---:|
| \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(3\) | \(3\) | \(-1\) | \(0\) | \(\varphi\) | \(\varphi'\) |
| \(3\) | \(3\) | \(-1\) | \(0\) | \(\varphi'\) | \(\varphi\) |
| \(4\) | \(4\) | \(0\) | \(1\) | \(-1\) | \(-1\) |
| \(5\) | \(5\) | \(1\) | \(-1\) | \(0\) | \(0\) |

Substitute these rows into (16). For a fixed element in the five respective classes, the counts are

\[
\begin{array}{c|ccccc}
\text{class}&1&2A&3A&5A&5B\\ \hline
\#\text{commutator pairs}&300&32&63&65&65.
\end{array}
\]

For example the \(2A\) count is \(60(1-1/3-1/3+1/5)=32\), and each 5-cycle count is \(60(1+(\varphi+\varphi')/3-1/4)=65\). Every count is positive, proving the assertion. Their size-weighted sum is \(300+15\cdot32+20\cdot63+24\cdot65=3600=|A_5|^2\), as required.

## 6. What this lesson uses and what it does not prove

The representation-theoretic prerequisites have the following proof locators. Complete reducibility is Theorem 2.3 and Schur's lemma is Theorem 3.1 in [Representations and complete reducibility](RT-FIN-01.md). Matrix-coefficient orthogonality, character determination and multiplicities, regular multiplicities and the degree-square identity, and character completeness are respectively Theorems 2.1, 3.1, 3.2 and 4.1 in [Characters and the orthogonality relations](RT-FIN-02.md).

Here are the elementary counting and arithmetic tools used in the examples. Their proofs are independent of the representation-theoretic conclusions above.

**Lemma 6.1 (cosets, orbits and quotient orders).** If \(H\leq G\) is finite, its left cosets partition \(G\), each has \(|H|\) elements, and \(|G|=[G:H]|H|\). An orbit of \(x\) in a finite \(G\)-set has size \([G:G_x]\). Consequently \(|g^G|=[G:C_G(g)]\), and the number of conjugates of \(H\) is \([G:N_G(H)]\). A homomorphism \(f:G\to K\) has \(|G|=|\ker f|\,|\operatorname{im}f|\). A group of prime order is cyclic.

**Proof.** Two left cosets that meet are equal: from \(ah=bk\), obtain \(b^{-1}a=kh^{-1}\in H\). Left multiplication gives a bijection \(H\to aH\). Counting the disjoint cosets proves the first formula. The map \(aG_x\mapsto ax\) is onto the orbit and is one-to-one, because \(ax=bx\) is equivalent to \(b^{-1}a\in G_x\). For conjugation of elements its stabilizer is the centralizer; for conjugation of subgroups its stabilizer is the normalizer. The fibers of \(f\) are precisely cosets of its kernel, and they are indexed by its image. Finally, the cyclic subgroup generated by a nonidentity element in a prime-order group has order greater than one dividing that prime, so it is the whole group. \(\square\)

Permutation matrices satisfy \(P_\sigma P_\tau=P_{\sigma\tau}\), by applying them to each coordinate basis vector. Multiplicativity of the determinant therefore makes \(\det P_\sigma\) a homomorphism, the sign. A transposition exchanges two columns of the identity and has determinant \(-1\).

Exercise 4 needs only cyclic subgroups of order five. There are \(24\) five-cycles, and each cyclic subgroup contains exactly four of them. Two distinct subgroups cannot share a nonidentity element, since that element generates both. Thus there are exactly six subgroups, without invoking a Sylow existence or conjugacy theorem. The normalizer of one acts on its generator by powers \(1,2,3,4\). The centralizer consists of its five powers: a commuting permutation is determined by the image of one letter. On the remaining four powers, multiplication by \(2\) or \(3\) is a four-cycle and odd, while multiplication by \(4\) is two transpositions and even. Hence the even normalizer has order ten, consisting of the cyclic subgroup and its inversion coset. Inversion is represented by an involution on the five letters. This is the dihedral group with five involutions. Conjugation is transitive on the six subgroups: any permutation conjugating two of them can, if odd, be multiplied on the right by an odd element of the first normalizer. The resulting conjugator is even. These facts justify all subgroup counts in that exercise.

**Lemma 6.2 (the fifth-root relation).** For a primitive fifth root \(\zeta\), the only rational linear relations among \(1,\zeta,\ldots,\zeta^4\) are multiples of \(1+\zeta+\cdots+\zeta^4=0\).

**Proof.** Set \(\Phi(X)=1+X+\cdots+X^4\). Its shift is
\[
\Phi(Y+1)=Y^4+5Y^3+10Y^2+10Y+5.
\]
This polynomial is irreducible over \(\mathbb Q\). Here is the needed Eisenstein argument, including its passage to integer factors. An integer polynomial is primitive when the greatest common divisor of its coefficients is one. The product of two primitive polynomials is primitive: otherwise a prime dividing every product coefficient would make the product of their two nonzero reductions in \(\mathbb F_p[Y]\) zero. That is impossible, since a product of nonzero polynomials over a field has degree the sum of their degrees. Clear denominators in a proposed rational factorization and divide each factor by its coefficient gcd. Primitivity then shows that a primitive integer polynomial factors over \(\mathbb Q\) only if it factors over \(\mathbb Z\), up to signs: a rational scalar carrying one primitive integer polynomial to another has numerator and denominator both units after reducing the fraction.

Suppose the displayed monic polynomial were a product of two nonconstant integer polynomials. Their leading coefficients are units. Reduction modulo five makes each factor a unit times a positive power of \(Y\), since their product is \(Y^4\). To see this last assertion without unique factorization, \(Y\) divides a product exactly when one factor has constant term zero; divide out powers of \(Y\) until the two remaining constant terms are nonzero. Their product must be constant. Thus both original factors have constant terms divisible by five. Their product has constant term divisible by \(25\), contradicting its value \(5\). Irreducibility is proved. Substitution \(Y=X-1\) preserves rational factorizations, so \(\Phi\) is irreducible too.

Since \(\zeta\ne1\) and \(\zeta^5=1\), it is a root of \(\Phi\). For a rational polynomial of degree at most four vanishing at \(\zeta\), divide by the monic \(\Phi\). A nonzero remainder of smaller degree would contradict irreducibility, by the Euclidean algorithm applied to that remainder and \(\Phi\). The remainder is zero, and the quotient is constant. \(\square\)

For the finite-order diagonalization used in the table, let \(T^r=I\) and let \(\omega\) be a primitive \(r\)-th root. The operators
\[
E_j=\frac1r\sum_{k=0}^{r-1}\omega^{-jk}T^k\qquad(0\leq j<r)
\]
satisfy \(TE_j=\omega^jE_j\) and \(\sum_jE_j=I\), by the finite geometric-sum identity. Their images lie in the distinct eigenspaces, whose sum is direct: applying the polynomial \(\prod_{a\ne j}(T-\omega^a I)\) to a relation isolates its \(j\)-th term. Hence \(T\) is diagonalizable. The earlier Lesson 1 complex-root provider supplies the roots of unity. No Sylow or later character theorem is needed for the \(A_5\) table.

The general structure theorem for finite simple algebras is contextual: a finite-dimensional simple algebra over a field \(k\) is a matrix algebra over a division algebra finite-dimensional over \(k\). See [Stacks, Tag 0747](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-theorem-wedderburn). We have proved the complex finite-group Fourier decomposition directly; no general density or structure theorem was needed for it. The [AI Integrated Stacks Project edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) contains AI-proposed material not reviewed by the official Stacks maintainers.

Fourier analysis on compact groups requires integration and infinite-dimensional convergence arguments. They lie beyond this finite algebra calculation.

## References

- **Stacks project**, *Brauer groups*, Tag 0747, Wedderburn's theorem; linked above through the English edition of the AI Integrated Stacks Project.
- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, 2018, Chapter 2 §1, Lemmas 1.11–1.12 and Theorem 1.13, and §3, items 3.1–3.6. The group-algebra blocks and central-idempotent formulas provide checks on (2), (10) and (12).

