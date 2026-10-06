# Unitary groups: characters, dimensions and branching

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

The irreducible characters of \(U(n)\) are quotients of alternating determinants. Their apparent singularities at repeated eigenvalues cancel. The integration formula turns these determinants into orthogonal Fourier sums, and integer coefficients then force each irreducible character to be a single quotient. This also yields existence, provided the cancellation and completeness steps are both supplied.

We use [Weyl integration](RT-CPT-08.md), complete reducibility and Schur orthogonality from the first lessons, and the complete \(L^2\) character basis from [Fourier analysis and class functions](RT-CPT-03.md). Our classification uses the analytic argument. The Schur–Weyl theorem is subsequently proved from that classification and the branching rule below; it is not a prerequisite for either. The determinant-to-tableau identity used for branching is proved below.

Differentiating a continuous finite-dimensional representation uses the smoothness result in [Compact matrix Lie groups](RT-CPT-05.md). The matrix-coefficient version of Stone–Weierstrass used below is the same precise density theorem used in the Peter–Weyl lesson.

Let \(T\) be the diagonal torus of \(U(n)\), with coordinates \(z_1,\ldots,z_n\in S^1\). Put
\[
\delta=(n-1,n-2,\ldots,0),\qquad
D_a(z)=\det[z_j^{a_i}]_{i,j=1}^n,\qquad
D_\delta(z)=\prod_{i<j}(z_i-z_j). \tag{1.1}
\]
Rows contain the exponents, in decreasing order. This fixes the determinant sign.

## Alternants and their removable singularities

**Lemma 1.2.** If \(a_1>\cdots>a_n\) are integers, the quotient \(D_a/D_\delta\) is a symmetric Laurent polynomial with integer coefficients. Consequently it defines a continuous class function on \(U(n)\). The functions \(D_a/\sqrt{n!}\), indexed by these decreasing integer tuples, are orthonormal in torus measure.

*Proof.* Multiply \(D_a\) by \((z_1\cdots z_n)^M\), with \(M\) large enough to make all exponents nonnegative. The resulting integer polynomial changes sign under every transposition of variables, so vanishes when \(z_i=z_j\). Polynomial division by the monic factor \(z_i-z_j\) therefore gives zero remainder and an integer polynomial quotient. The factors for distinct unordered pairs are nonassociate prime elements of the unique factorization domain \(\mathbb Z[z_1,\ldots,z_n]\). Their product divides the polynomial. Dividing back by the monomial proves Laurent integrality. The numerator and denominator have the same transposition sign, so the quotient is symmetric. This is an identity of Laurent polynomials, including where the displayed denominator vanishes.

Continuous symmetric functions on \(T\) extend uniquely to continuous class functions by the torus conjugacy theorem in the roots lesson. For orthogonality, expand \(D_a\). Its \(n!\) monomials have distinct exponent tuples and coefficients \(\pm1\). Different decreasing tuples give disjoint monomial supports. Torus characters \(z^m\), \(m\in\mathbb Z^n\), are orthonormal, so the claimed determinant norms and orthogonality follow. \(\square\)

We shall also need their value when all variables equal one.

**Lemma 1.3 (evaluation at the identity).** For every strictly decreasing integer tuple \(a\),
\[
\left.\frac{D_a}{D_\delta}\right|_{z_1=\cdots=z_n=1}
=\prod_{i<j}\frac{a_i-a_j}{j-i}>0. \tag{1.4}
\]

*Proof.* Choose distinct real \(x_1,\ldots,x_n\) and put \(z_j=e^{\varepsilon x_j}\). Expand each entry as
\[
e^{\varepsilon a_i x_j}
=\sum_{k\geq0}\frac{\varepsilon^k a_i^k x_j^k}{k!}.
\]
In the determinant expansion, repeated power indices give zero. The lowest possible sum of \(n\) distinct nonnegative indices is \(N=n(n-1)/2\), obtained uniquely from \(0,\ldots,n-1\). Multilinearity, or the finite Cauchy–Binet formula applied to a truncated series, consequently gives
\[
D_a(e^{\varepsilon x})
=\frac{\varepsilon^N}{\prod_{k=0}^{n-1}k!}
\det[a_i^k]_{\substack{1\leq i\leq n\\0\leq k<n}}
\det[x_j^k]_{\substack{0\leq k<n\\1\leq j\leq n}}
+O(\varepsilon^{N+1}).
\]
Both displayed determinants are nonzero Vandermonde determinants. The same calculation for \(\delta\) cancels the \(x\)-determinant, factorial and power of \(\varepsilon\). The ratio is
\(\prod_{i<j}(a_i-a_j)/(\delta_i-\delta_j)\), with \(\delta_i-\delta_j=j-i\). Lemma 1.2 makes the quotient continuous at the identity, so this limit is its value there. Each factor is positive. For \(n=1\) both products are empty and equal one. \(\square\)

## The character classification

For every nonincreasing integer tuple \(\lambda=(\lambda_1,\ldots,\lambda_n)\), define
\[
s_\lambda(z)=\frac{D_{\lambda+\delta}(z)}{D_\delta(z)}, \tag{2.1}
\]
using its Laurent-polynomial extension.

**Theorem 2.2 (Weyl's character formula for \(U(n)\)).** The irreducible continuous complex representations of \(U(n)\) are in bijection with
\[
\lambda\in\mathbb Z^n,\qquad \lambda_1\geq\cdots\geq\lambda_n.
\]
The character of the representation \(\pi_\lambda\) is \(s_\lambda\) on the torus. This formula remains valid at repeated eigenvalues through the extension in Lemma 1.2.

*Proof.* Every irreducible is finite-dimensional and can be made unitary. Its restriction to \(T\) is a direct sum of torus characters. Therefore its character is a Laurent polynomial
\[
\chi(z)=\sum_{m\in\mathbb Z^n}b_m z^m,
\qquad b_m\in\mathbb Z_{\geq0},
\]
with finite support. It is symmetric, since permutation matrices conjugate diagonal matrices. Thus \(\chi D_\delta\) is alternating with integer coefficients.

Every alternating Laurent polynomial has a unique finite expression
\[
\chi D_\delta=\sum_{a_1>\cdots>a_n}c_aD_a,\qquad c_a\in\mathbb Z. \tag{2.3}
\]
Indeed a monomial with repeated exponents has zero coefficient: its stabilizing transposition negates that coefficient. On every other permutation orbit, alternating signs determine all coefficients from the coefficient of the decreasing tuple, exactly as in \(D_a\).

Character orthogonality and Weyl integration give
\[
1=\int_{U(n)}|\chi|^2
=\frac1{n!}\int_{T^n}|\chi D_\delta|^2
=\sum_a|c_a|^2.
\]
Since the coefficients are integers, precisely one is nonzero, and it equals \(1\) or \(-1\). Thus \(\chi=\pm D_a/D_\delta\). The character value \(\chi(1)=\dim\pi\) is positive, and Lemma 1.3 says the quotient's identity value is positive. The sign is therefore plus. Put \(\lambda_i=a_i-(n-i)\); strict decrease of integer \(a_i\) makes \(\lambda\) nonincreasing. Every irreducible is now in the proposed list.

Existence is a separate step. Lemma 1.2 and Weyl integration show that all \(s_\lambda\) are continuous class functions of norm one and satisfy
\[
\langle s_\lambda,s_\mu\rangle_{L^2(U(n))}=\delta_{\lambda\mu}. \tag{2.4}
\]
If a proposed \(\lambda\) did not occur, the classification just proved would make \(s_\lambda\) orthogonal to every irreducible character. The complete \(L^2\) character basis would then force \(s_\lambda=0\) in \(L^2\), contradicting its norm one. Hence every \(\lambda\) occurs. Orthogonality proves inequivalence of different labels; equality of characters determines the representation by complete reducibility and Schur orthogonality. \(\square\)

The label is the highest weight for upper-triangular positive roots. For completeness, order exponent tuples lexicographically. The leading monomial in \(D_a\) is \(z_1^{a_1}\cdots z_n^{a_n}\), with coefficient one; the same holds for \(D_\delta\). The leading term of their Laurent quotient is therefore \(z^\lambda\), with coefficient one. Thus \(\lambda\) is the lexicographically largest weight and its weight space is one-dimensional. The complexified differential of \(E_{ij}\), \(i<j\), raises a weight by \(\varepsilon_i-\varepsilon_j\), which is lexicographically positive. It must annihilate that weight space. This identifies a highest-weight vector without using a prior highest-weight classification.

**Corollary 2.5 (dimension).**
\[
\dim\pi_\lambda
=\prod_{1\leq i<j\leq n}
\frac{\lambda_i-\lambda_j+j-i}{j-i}. \tag{2.6}
\]

*Proof.* A character at the identity is its dimension. Apply Lemma 1.3 to \(a=\lambda+\delta\). \(\square\)

For any integer \(k\), determinant twisting gives
\[
s_{\lambda+k(1,\ldots,1)}(z)
=(z_1\cdots z_n)^k s_\lambda(z),\qquad
\pi_{\lambda+k(1,\ldots,1)}\simeq\det^k\otimes\pi_\lambda. \tag{2.7}
\]
Negative weights are therefore essential to the full unitary classification. The dual defining representation has label \((0,\ldots,0,-1)\), for instance.

## Branching and Gelfand–Tsetlin lines

**Proposition 3.1 (tableau identity).** For a partition \(\kappa_1\geq\cdots\geq\kappa_n\geq0\), the bialternant \(s_\kappa(z_1,\ldots,z_n)\) equals
\[
\sum_Q\prod_{i=1}^n z_i^{\,\#\{\text{entries }i\text{ in }Q\}}, \tag{3.1}
\]
where \(Q\) runs over the semistandard tableaux of shape \(\kappa\), with entries \(1,\ldots,n\), weakly increasing in rows and strictly increasing in columns. Stanley's Definition 7.10.1 and Theorem 7.15.1 give the same identity. Here is an internal determinant proof.

*Proof.* Put \(a_i=\kappa_i+n-i\), so \(a_1>\cdots>a_n\geq0\), and denote \(\det[z_j^{a_i}]\) by \(D_a\). For each interlacing partition \(\nu\) of length \(n-1\), put \(b_i=\nu_i+n-1-i\). The interlacing conditions are exactly the independent intervals
\[
a_{i+1}\leq b_i\leq a_i-1,\qquad 1\leq i<n.
\]
These intervals automatically make \(b_1>\cdots>b_{n-1}\geq0\).
Multilinearity in the determinant's rows gives
\[
\sum_b D_b(z)\,w^{\,|a|-|b|-(n-1)}
=w^{a_n}\det\left[
\sum_{b=a_{i+1}}^{a_i-1}z_j^b w^{a_i-1-b}
\right]_{i,j=1}^{n-1}.
\]
All exponents of \(w\) in these finite sums are nonnegative. Multiplying by \(\prod_{j<n}(z_j-w)\) and using the telescoping geometric identity in each column gives
\[
w^{a_n}\det\left[
z_j^{a_i}-w^{a_i-a_{i+1}}z_j^{a_{i+1}}
\right]_{i,j=1}^{n-1}.
\]
This is \(D_a(z_1,\ldots,z_{n-1},w)\): in its \(n\)-by-\(n\) determinant replace row \(i\) by row \(i\) minus \(w^{a_i-a_{i+1}}\) times row \(i+1\), in increasing order \(i=1,\ldots,n-1\). The last column becomes zero except for its last entry \(w^{a_n}\); expansion down that column gives the displayed determinant with positive sign.

The Vandermonde denominator satisfies
\[
D_{\delta_n}(z,w)=D_{\delta_{n-1}}(z)\prod_{j<n}(z_j-w).
\]
Dividing first at distinct variables, and then using the polynomial extension already proved, shows
\[
s_\kappa(z,w)=
\sum_{\nu\prec\kappa}w^{|\kappa|-|\nu|}s_\nu(z).
\tag{3.1a}
\]
The exponent identity follows from
\(|a|-|b|-(n-1)=|\kappa|-|\nu|\).

The tableau sum satisfies exactly the same recursion. All entries \(n\) lie at row ends, and column strictness permits at most one in a column. Removing them leaves a partition \(\nu\) with \(\kappa_i\geq\nu_i\geq\kappa_{i+1}\), and a tableau with entries at most \(n-1\). Conversely each such tableau extends uniquely by filling the removed horizontal strip with \(n\). These new entries contribute \(w^{|\kappa|-|\nu|}\). When \(n=1\), both expressions are \(z_1^{\kappa_1}\). Induction on \(n\), using (3.1a), proves their equality for every partition. This uses no Schur–Weyl theorem or algebraic representation classification. \(\square\)

**Theorem 3.2 (unitary branching).** For \(n\geq2\), under the embedding \(U(n-1)\to U(n)\), \(h\mapsto\operatorname{diag}(h,1)\),
\[
\pi_\lambda|_{U(n-1)}
\simeq\bigoplus_{\mu\prec\lambda}\pi_\mu,\qquad
\lambda_i\geq\mu_i\geq\lambda_{i+1}\quad(1\leq i<n), \tag{3.3}
\]
with multiplicity one. The \(\mu\)'s are integer tuples of length \(n-1\).

*Proof.* First let \(\lambda=\kappa\) be a partition. The entries \(n\) of a tableau are at row ends and cannot share a column, by column strictness. Removing them leaves a partition \(\nu\) and a semistandard tableau with entries at most \(n-1\). The removed shape \(\kappa/\nu\) has at most one box in each column, equivalently
\[
\kappa_i\geq\nu_i\geq\kappa_{i+1}\quad(1\leq i<n).
\]
In detail, \(\nu\subset\kappa\) gives the first inequality. If \(\nu_i<\kappa_{i+1}\), a column between these two lengths has removed boxes in both rows \(i,i+1\), contradicting the condition. Conversely the inequalities place each removed box below all remaining boxes in its column and permit at most one removed box there. Also \(\nu\) has no \(n\)-th row: a column of height \(n\) in the original tableau must end in \(n\).

For any such \(\nu\), filling all removed boxes with \(n\) gives a unique inverse construction. Existing entries above them are smaller, and row weak increase is preserved. The tableau formula consequently gives the full identity
\[
s_\kappa(z_1,\ldots,z_{n-1},w)
=\sum_{\nu\prec\kappa}
w^{|\kappa|-|\nu|}s_\nu(z_1,\ldots,z_{n-1}). \tag{3.4}
\]
For general integer \(\lambda\), put \(k=\lambda_n\), \(\kappa=\lambda-k(1,\ldots,1)\). This is a partition. Multiply (3.4) by \((z_1\cdots z_{n-1}w)^k\) and put \(\mu=\nu+k(1,\ldots,1)\). Interlacing is unchanged, and \(|\lambda|-|\mu|=|\kappa|-|\nu|+k\), so
\[
s_\lambda(z,w)=\sum_{\mu\prec\lambda}
w^{|\lambda|-|\mu|}s_\mu(z). \tag{3.5}
\]
Here \(|\lambda|\) means the sum of its entries, even when negative. Setting \(w=1\) gives the restricted character. Complete reducibility and character independence then give precisely (3.3). The interlacing inequalities themselves imply that \(\mu\) is nonincreasing. \(\square\)

Repeated branching along \(U(1)\subset\cdots\subset U(n)\) decomposes the representation into one-dimensional mutually orthogonal lines labeled by integer arrays
\[
\begin{matrix}
\lambda_1^{(n)}&\lambda_2^{(n)}&\cdots&\lambda_n^{(n)}\\
\lambda_1^{(n-1)}&\cdots&\lambda_{n-1}^{(n-1)}\\
\vdots\\
\lambda_1^{(1)}
\end{matrix},
\qquad
\lambda_i^{(r)}\geq\lambda_i^{(r-1)}\geq\lambda_{i+1}^{(r)}.
\]
The top row is \(\lambda\). Multiplicity one makes the summands intrinsic at each step; \(U(1)\) irreducibles are one-dimensional. Choosing a unit vector on each final line gives a Gelfand–Tsetlin basis. Phases of those vectors require a choice. Counting the patterns gives the dimension; this does not assert unexplained explicit formulas for Lie-algebra generator matrices.

## Restricting to the special unitary group

**Corollary 4.1.** The irreducible representations of \(SU(n)\) are the restrictions of \(\pi_\lambda\) with \(\lambda_n=0\), pairwise inequivalent.

*Proof.* First every \(U(n)\) irreducible remains irreducible on \(SU(n)\). Its scalar central circle acts by scalars, by Schur's lemma. Since \(U(n)=S^1 SU(n)\), any \(SU(n)\)-invariant subspace is invariant under all of \(U(n)\), so is zero or the whole space.

We also prove exhaustion. On \(SU(n)\), the unital algebra generated by matrix entries and their complex conjugates separates points and is closed under conjugation. Stone–Weierstrass makes it uniformly dense in \(C(SU(n))\). Each of its monomials is a coefficient of a tensor product of the defining \(U(n)\) representation and its dual. Decomposing that tensor product into \(U(n)\) irreducibles shows that restrictions of their coefficient spaces span a dense subspace. Any additional \(SU(n)\) irreducible would have nonzero matrix coefficients orthogonal to all these spaces, by Schur coefficient orthogonality, contradicting density. Thus every irreducible is a restriction.

Finally suppose two restrictions are equivalent. Their intertwiner space is one-dimensional. Conjugating an intertwiner by the two \(U(n)\) actions gives a continuous character of \(U(n)\), trivial on \(SU(n)\). It factors through determinant \(U(n)/SU(n)\simeq S^1\), and is therefore \(\det^k\) for an integer \(k\). The two \(U(n)\) representations differ by that determinant twist. Conversely determinant twists restrict identically. Formula (2.7) consequently identifies labels exactly modulo integer multiples of \((1,\ldots,1)\). Subtracting \(\lambda_n\) gives a unique nonincreasing label with last entry zero. When \(n=1\), \(SU(1)\) is trivial and the normalized label is \(0\), as asserted. \(\square\)

For \(U(2)\), write \(\lambda=(a,b)\), \(m=a-b\geq0\). Direct division gives
\[
s_{(a,b)}(z_1,z_2)
=(z_1z_2)^b\sum_{j=0}^m z_1^{m-j}z_2^j,
\qquad \pi_{(a,b)}\simeq\det^b\otimes\operatorname{Sym}^m\mathbb C^2.
\]
Its dimension is \(m+1\), and the scalar \(zI\) acts as \(z^{a+b}\). In the earlier \(SU(2)\times S^1\) description, the central exponent is \(a+b=m+2b\), exactly the required parity condition.

For \(U(3)\), conjugation on \(\operatorname{End}(\mathbb C^3)\) has character \(|z_1+z_2+z_3|^2\). Its scalar line splits off; the trace-zero summand has character
\[
\chi_0=|z_1+z_2+z_3|^2-1.
\]
The trace moments from the preceding lesson give \(\|\chi_0\|^2=2-2+1=1\), so this genuine representation is irreducible. Its highest monomial is \(z_1z_3^{-1}\), hence its label is \((1,0,-1)\) and its dimension is eight. The full complexified adjoint representation has dimension nine and includes the trivial scalar summand.

The tableau formula for a single row and a single column gives
\[
\operatorname{Sym}^k\mathbb C^n\simeq\pi_{(k,0,\ldots,0)},\qquad
\bigwedge^k\mathbb C^n\simeq\pi_{(1^k,0^{n-k})}\quad(0\leq k\leq n).
\]
Indeed their standard tensor bases have respectively weakly increasing and strictly increasing index sequences, giving exactly those characters. Exterior powers with \(k>n\) are zero.

## Permutations explain the multiplicity spaces in tensor powers

On \(E_{N,d}=(\mathbb C^N)^{\otimes d}\), \(U(N)\) acts on every factor while \(S_d\) permutes the factors. Write
\[
P_\sigma(v_1\otimes\cdots\otimes v_d)
=v_{\sigma^{-1}(1)}\otimes\cdots\otimes v_{\sigma^{-1}(d)}.
\]
The inverse makes \(P_\sigma P_\tau=P_{\sigma\tau}\), and this action commutes with \(U(N)\).

**Theorem 5.1 (Schur–Weyl duality).** For \(N,d\geq1\), there are irreducible \(S_d\)-modules \(S^\lambda\), indexed by partitions \(\lambda\) of \(d\), such that
\[
E_{N,d}\simeq
\bigoplus_{\substack{\lambda\vdash d\\\ell(\lambda)\leq N}}
\pi_\lambda^{U(N)}\otimes S^\lambda
\]
as a representation of \(U(N)\times S_d\). The \(S^\lambda\)'s are pairwise inequivalent, independent of \(N\), and exhaust the irreducibles of \(S_d\). The two actions generate each other's commutants. For \(d=0\), the tensor space and both actions are trivial one-dimensional ones.

*Proof.* We first prove the commutant statement when \(N\geq d\), using only matrices. If \(A\) commutes with the \(U(N)\)-action, differentiation makes it commute with the tensor action of \(\mathfrak u(N)\), and complex linearity with that of \(\mathfrak{gl}_N(\mathbb C)=\mathfrak u(N)+i\mathfrak u(N)\). It therefore commutes with tensor powers of every \(g\in GL_N(\mathbb C)\). Here no density theorem for algebraic groups is needed: polar decomposition writes \(g=u\exp H\), with \(u\) unitary and \(H\) Hermitian, by diagonalizing the positive matrix \(g^*g\).

Set \(v=e_1\otimes\cdots\otimes e_d\). The diagonal matrices' joint weight space with weight \(z_1\cdots z_d\) is spanned by the \(d!\) distinct vectors \(P_\sigma v\). Consequently \(Av=\sum_\sigma a_\sigma P_\sigma v\). The commuting operator \(A-\sum a_\sigma P_\sigma\) annihilates every tensor \(gv\), hence every tensor of \(d\) linearly independent vectors. Such tuples are dense in \((\mathbb C^N)^d\): perturb a tuple by \(t(e_1,\ldots,e_d)\); a suitable \(d\)-row minor is a polynomial in \(t\) with leading coefficient one, so is nonzero for arbitrarily small \(t\). Continuity gives annihilation of all pure tensors, which span the tensor space. Thus
\[
\operatorname{End}_{U(N)}(E_{N,d})
=\operatorname{span}_{\mathbb C}\{P_\sigma:\sigma\in S_d\}.
\]
The permutation operators are linearly independent when \(N\geq d\), by applying them to \(v\).

Complete reducibility gives \(E_{N,d}=\bigoplus_\lambda\pi_\lambda\otimes M_{\lambda,N}\), where \(M_{\lambda,N}=\operatorname{Hom}_{U(N)}(\pi_\lambda,E_{N,d})\). Every weight in this tensor space has nonnegative integer coordinates summing to \(d\). The classification in Theorem 2.2 therefore permits only partitions of \(d\). Schur's lemma identifies its commutant with \(\bigoplus_\lambda\operatorname{End}(M_{\lambda,N})\). The just-proved equality says that the permutation algebra realizes every matrix in every one of these blocks independently. Each nonzero \(M_{\lambda,N}\) is consequently irreducible for \(S_d\), and different blocks are inequivalent. Moreover every \(S_d\)-irreducible occurs: otherwise its central isotypic projection
\[
e_\tau=\frac{\dim\tau}{d!}\sum_{\sigma\in S_d}
\overline{\chi_\tau(\sigma)}\,\sigma
\]
would act by zero, contrary to the linear independence of the permutation operators. This is exactly the finite-group projector proved in lesson three. The number of irreducibles of \(S_d\) equals its number of conjugacy classes, also by that lesson. Cycle types identify those classes with the partitions of \(d\). Since there are at most that many possible \(U(N)\)-labels, every partition occurs once as a label of a multiplicity block. Put \(S^\lambda=M_{\lambda,N}\).

We now check both independence of \(N\) and the case \(N<d\). Inside \(E_{K,d}\), the subspace on which the last coordinate circle acts trivially is exactly \(E_{K-1,d}\): its exponent counts the occurrences of \(e_K\), so is zero exactly when none occur. In the full branching identity (3.5), the corresponding exponent for \(\pi_\lambda^{U(K)}\) is \(|\lambda|-|\mu|\). For a partition, interlacing gives \(\mu_i\leq\lambda_i\), so this exponent is zero precisely when \(\lambda_K=0\) and \(\mu\) is the truncated tuple \((\lambda_1,\ldots,\lambda_{K-1})\). That component is one copy of the appropriate \(U(K-1)\)-irreducible. Taking the zero-weight subspace thus keeps exactly the labels with \(\ell(\lambda)\leq K-1\), without changing their \(S_d\)-multiplicity modules. Repeated truncation from any \(K\geq\max(N,d)\) proves the displayed decomposition and compatibility for every \(N\).

Finally, for any finite-dimensional unitary representation with inequivalent irreducible blocks \(V_i\), its group operators span \(\bigoplus_i\operatorname{End}(V_i)\). To see this directly, Schur coefficient orthogonality makes their individual matrix coefficients linearly independent; the map taking a linear functional on the block matrix space to the corresponding coefficient function is injective. Its finite-dimensional dual therefore says that the evaluation vectors, which are the block group matrices, span that whole space. Applied separately to \(U(N)\) and \(S_d\), this proves the two commutant assertions for all \(N\). \(\square\)

For tensor cubes, \(S^{(3)}\) is trivial, \(S^{(1,1,1)}\) is the sign representation, and the remaining \(S^{(2,1)}\) is the two-dimensional standard representation of \(S_3\). The first two identifications follow by symmetric and alternating tensors. The standard module is the sum-zero plane in the three-point permutation representation; its character is \(2,0,-1\) on the identity, transpositions and three-cycles, with squared norm \((4+0+2)/6=1\), proving irreducibility. These three modules exhaust the three conjugacy classes. Hence
\[
(\mathbb C^2)^{\otimes3}\simeq
\pi_{(3,0)}\oplus2\pi_{(2,1)},
\qquad8=4+2\cdot2.
\]
For dimension three,
\[
\begin{aligned}
(\mathbb C^3)^{\otimes3}&\simeq
\pi_{(3,0,0)}\oplus2\pi_{(2,1,0)}\\
&\hspace{1em}\oplus\pi_{(1,1,1)},\\
27&=10+2\cdot8+1.
\end{aligned}
\]
On \(SU(2)\), the first line becomes \(\pi_3\oplus2\pi_1\). The factor of two is now an actual permutation-module dimension, rather than an unexplained repeated highest weight. This construction supplements the analytic classification already proved; it is not an assumption used to obtain that classification.

## Exercises with complete solutions

**Exercise 1 (easy).** Compute dimensions for \((2,1,0)\) in \(U(3)\) and \((1,1,0,0)\) in \(U(4)\).

*Solution.* The three factors for \((2,1,0)\) are \(2,2,2\), giving dimension eight. For \((1,1,0,0)\), the six factors in pair order \((12),(13),(14),(23),(24),(34)\) are
\[
1,\quad\tfrac32,\quad\tfrac43,\quad2,\quad\tfrac32,\quad1.
\]
Their product is six, also \(\dim\bigwedge^2\mathbb C^4=\binom42\). The first representation restricts to the \(SU(3)\) adjoint representation; its unitary label differs from \((1,0,-1)\) by a determinant twist.

**Exercise 2 (medium).** Prove the one-box Pieri rule
\[
\pi_\lambda\otimes\mathbb C^n
\simeq\bigoplus_{\substack{1\leq i\leq n\\\lambda+e_i\text{ nonincreasing}}}
\pi_{\lambda+e_i}.
\]

*Solution.* Let \(p(z)=z_1+\cdots+z_n\). Expanding determinants, as in the previous lesson, gives
\[
pD_a=\sum_iD_{a+e_i}.
\]
For \(a=\lambda+\delta\), raising row \(i>1\) creates a collision precisely when \(\lambda_{i-1}=\lambda_i\); that determinant is zero. Otherwise the exponents remain strictly decreasing, so no reordering sign occurs. Row one always contributes. Dividing by \(D_\delta\) yields
\[
ps_\lambda=\sum_{\lambda+e_i\text{ nonincreasing}}s_{\lambda+e_i}.
\]
The left side is the tensor-product character. The right side is a sum of distinct irreducible characters with coefficient one. Complete reducibility and character independence prove the rule for all integer labels, including determinant twists.

**Exercise 3 (medium).** Recover the complete \(SU(2)\) classification and its character formula.

*Solution.* Corollary 4.1 normalizes every label to \((m,0)\), \(m\geq0\). Restricting the \(U(2)\) formula to \(z_1=z\), \(z_2=z^{-1}\) gives
\[
\chi_m(z)=z^m+z^{m-2}+\cdots+z^{-m}.
\]
For \(z=e^{i\theta}\) and \(\sin\theta\neq0\), the geometric sum is
\[
\chi_m(t_\theta)=\frac{\sin((m+1)\theta)}{\sin\theta}.
\]
At \(\theta=0\) the continuous value is \(m+1\), its dimension; at \(\theta=\pi\) it is \((-1)^m(m+1)\). These are the polynomial representations previously constructed. The central element \(-I\) acts as \((-1)^m\), so precisely the even \(m\)'s descend to \(SO(3)\).

**Exercise 4 (hard).** Prove the interlacing identity with final torus coordinate one, and deduce the branching decomposition without a multiplicity assumption.

*Solution.* For a partition \(\kappa\), remove all maximal entries \(n\) from its semistandard tableaux. They occupy a horizontal strip, and the remaining shape \(\nu\) satisfies \(\kappa_i\geq\nu_i\geq\kappa_{i+1}\). Conversely every tableau on such a \(\nu\) extends uniquely by filling the strip with \(n\). Weights of remaining boxes contribute \(s_\nu\), while removed entries contribute the factor \(w^{|\kappa|-|\nu|}\). Summing the bijection gives (3.4); at \(w=1\) each strip contributes once.

For an arbitrary integer label \(\lambda\), subtract \(k=\lambda_n\) from each entry to get a partition \(\kappa\). Multiply the identity by the determinant monomial \((z_1\cdots z_{n-1}w)^k\). The remaining labels become \(\mu=\nu+k(1,\ldots,1)\), preserving interlacing, so at \(w=1\)
\[
s_\lambda(z_1,\ldots,z_{n-1},1)
=\sum_{\mu\prec\lambda}s_\mu(z_1,\ldots,z_{n-1}).
\]
Restriction is completely reducible. Pairing its character with each \(U(n-1)\) irreducible character reads off its multiplicity: one for each interlacing \(\mu\), zero otherwise. This proves both the list and multiplicity one. It also covers negative labels, which a partition-only identity would leave untreated.

## Source comparisons

Stanley, *Enumerative Combinatorics*, Volume 2, Sections 7.10 and 7.15, gives the independently proved identity (3.1); Appendix 2 states the rational \(GL(n,\mathbb C)\) counterpart. That algebraic theorem is not used as a substitute for existence in the compact analytic argument.

The symmetric-power generating series is infinite:
\[
\sum_{k\geq0}\chi_{\operatorname{Sym}^k}(g)u^k
=\det(1-ug)^{-1}.
\]
Only the exterior-power series terminates at \(N\). Already for \(g=1\) in \(U(1)\), the symmetric series is \(1/(1-u)\).

Schur's 1927 paper [59] begins by treating polynomial matrix coefficients, in the terminology of its time, and its first footnote extends to determinant denominators. His 1928 paper [62] studies continuous representations of several noncompact general and special linear groups; its symbol \(U_n\) denotes the complex unimodular group, not our compact unitary group. These distinctions matter when comparing historical classifications. No original passage is reproduced here.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §27. The general character and dimension formulas give a comparison after specializing the type-A roots. The full determinant and branching proofs above also retain negative analytic labels; no source classification replaces them.

Constantin Teleman, [*Representation Theory*, Lent 2005](https://math.berkeley.edu/~teleman/math/RepThry.pdf), §§23.14–24.10, pages 57–60 (accessed 3 October 2026), supplies the Schur–Weyl and cycle-trace comparison. Theorem 5.1 here has a full elementary commutant proof followed by the already proved branching rule, so its proof does not assume the source’s outlined Cauchy determinant argument.
