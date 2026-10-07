# Complete positivity: finite matrix tests and compression

*Written by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A positive map carries a positive matrix to a positive matrix. Complete positivity asks for the same property when the entries of a larger positive matrix are themselves matrices. Compression has this stronger property because its quadratic form can be tested before compression. Transpose preserves positivity of individual matrices, but reversing one of two matrix coordinates can produce a negative quadratic form.

We prove the finite matrix criterion first, then apply it to compression, transpose and explicit maps. All finite-dimensional facts needed in the arguments are proved below. The final reference is optional reading.

<a id="cp-positive-factorization"></a>

## 1. Positive matrices and Gram factorizations

Vectors are columns, \(x^*y\) is the usual inner product, and \(A^*\) is conjugate transpose. A matrix \(A\in M_d(\mathbb C)\) is **positive** if \(A=A^*\) and \(x^*Ax\geq0\) for every \(x\in\mathbb C^d\).

**Lemma 1.1.** A Hermitian matrix has an orthonormal eigenbasis with real eigenvalues. Consequently a matrix is positive exactly when it can be written
\[
A=RR^*=\sum_{\alpha=1}^r w_\alpha w_\alpha^*.
\tag{1.1}
\]
The columns \(w_\alpha\) can be chosen with \(r\leq d\). For any rectangular matrix \(V\), positivity of \(A\) implies positivity of \(V^*AV\).

**Proof.** The unit sphere in \(\mathbb C^d\) is compact: a bounded sequence has a convergent subsequence in each of its finitely many real and imaginary coordinates, by repeatedly selecting a half of a bounded interval containing infinitely many terms. A diagonal choice gives convergence of all coordinates, and \(x^*x=1\) passes to the limit. The continuous real function \(x\mapsto x^*Ax\) therefore has a maximum on this sphere: a sequence approaching its supremum has a convergent subsequence.

Choose a maximizing unit vector \(u\), and put \(\lambda=u^*Au\in\mathbb R\). For \(y\perp u\), the derivative at zero of
\[
\frac{(u+ty)^*A(u+ty)}{1+t^2\|y\|^2}
\]
is \(2\operatorname{Re}(y^*Au)\), so it vanishes. Replacing \(y\) by \(iy\) also makes the imaginary part vanish. Hence \(Au=\lambda u\). Hermitian symmetry makes \(u^\perp\) invariant: \(u^*Ay=(Au)^*y=0\). Induction gives the eigenbasis. Its eigenvalues are real because \(v^*Av\) is real for each unit eigenvector.

In this basis, \(x^*Ax=\sum_j\lambda_j|x_j|^2\), so positivity is equivalent to every \(\lambda_j\geq0\). Taking \(w_j=\sqrt{\lambda_j}v_j\) for positive eigenvalues proves (1.1). Conversely, \(x^*RR^*x=\|R^*x\|^2\geq0\). Finally,
\[
z^*V^*AVz=(Vz)^*A(Vz)\geq0,
\]
and \(V^*AV\) is Hermitian. \(\square\)

This is also the **Gram test**. A matrix is positive exactly when its entries have the form \(A_{ij}=u_i^*u_j\) for finitely many vectors \(u_i\). In fact, take \(u_i\) to be the columns of \(R^*\) in (1.1). Conversely, the quadratic form of this Gram matrix is
\[
\sum_{i,j}\overline z_i\,u_i^*u_jz_j
=\left\|\sum_j z_ju_j\right\|^2\geq0.
\]
Finite sums of positive matrices are positive because their quadratic forms add.

## 2. Amplification and the finite Choi test

Let \(\Phi:M_n(\mathbb C)\to M_m(\mathbb C)\) be complex linear. Its \(k\)-th **amplification** applies \(\Phi\) to each block:
\[
\Phi^{(k)}([A_{ab}])=[\Phi(A_{ab})],
\qquad
M_k(M_n(\mathbb C))\longrightarrow M_k(M_m(\mathbb C)).
\tag{2.1}
\]
These are operators on \(\mathbb C^k\otimes\mathbb C^n\) and \(\mathbb C^k\otimes\mathbb C^m\), respectively. The map is **\(k\)-positive** if this amplification preserves positivity, and **completely positive** if it is \(k\)-positive for every positive integer \(k\).

Write \(E_{ij}=e_ie_j^*\in M_n(\mathbb C)\). The **Choi matrix** is the single \(nm\)-by-\(nm\) matrix
\[
C_\Phi=[\Phi(E_{ij})]_{i,j=1}^n
       =\sum_{i,j=1}^n E_{ij}\otimes\Phi(E_{ij}).
\tag{2.2}
\]

<a id="cp-choi-test"></a>

**Theorem 2.1.** The following are equivalent:

1. \(\Phi\) is completely positive.
2. \(\Phi\) is \(n\)-positive.
3. \(C_\Phi\) is positive.
4. There are finitely many matrices \(V_\alpha:\mathbb C^n\to\mathbb C^m\) such that
   \[
   \Phi(A)=\sum_\alpha V_\alpha A V_\alpha^*.
   \tag{2.3}
   \]

At most \(nm\) matrices are needed in (4). Equivalently, (3) requires Hermitian symmetry of the blocks and
\[
\sum_{i,j=1}^n y_i^*\Phi(E_{ij})y_j\geq0
\quad\text{for every }y_1,\ldots,y_n\in\mathbb C^m.
\tag{2.4}
\]

**Proof.** Complete positivity implies \(n\)-positivity. Put \(\Omega=\sum_i e_i\otimes e_i\). The \((i,j)\)-block of the positive matrix \(\Omega\Omega^*\) is \(E_{ij}\). Applying \(\Phi^{(n)}\) gives \(C_\Phi\), proving (2) implies (3).

If \(C_\Phi\geq0\), Lemma 1.1 gives
\[
C_\Phi=\sum_\alpha w_\alpha w_\alpha^*,
\qquad
w_\alpha=\sum_{i=1}^n e_i\otimes v_{\alpha i},
\quad v_{\alpha i}\in\mathbb C^m.
\]
There are at most \(nm\) vectors. Define \(V_\alpha e_i=v_{\alpha i}\). Equality of the \((i,j)\)-blocks says
\[
\Phi(E_{ij})=\sum_\alpha v_{\alpha i}v_{\alpha j}^*
            =\sum_\alpha V_\alpha E_{ij}V_\alpha^*.
\]
Linearity on the matrix units proves (2.3). Conversely, (2.3) gives at every size \(k\)
\[
\Phi^{(k)}(X)
=\sum_\alpha (I_k\otimes V_\alpha)
                   X(I_k\otimes V_\alpha)^*.
\tag{2.5}
\]
Each summand is positive when \(X\) is positive, by Lemma 1.1; their sum is positive. This proves complete positivity. Finally a vector of \(\mathbb C^n\otimes\mathbb C^m\) is uniquely \(\sum_i e_i\otimes y_i\), and its quadratic form for (2.2) is (2.4). \(\square\)

The factorization (2.3) is often called a **Kraus representation**. Factoring the Choi matrix constructs it. Also,
\[
\Phi(I_n)=\sum_\alpha V_\alpha V_\alpha^*,
\tag{2.6}
\]
so this map is unital exactly when the sum is \(I_m\).

<a id="cp-compression"></a>

## 3. Compression preserves every matrix level

**Proposition 3.1.** Let \(H,K\) be complex Hilbert spaces and let \(V:K\to H\) be bounded with adjoint \(V^*\). The map
\[
\Psi:\mathcal B(H)\longrightarrow\mathcal B(K),
\qquad \Psi(A)=V^*AV
\tag{3.1}
\]
is completely positive. It is unital when \(V^*V=I_K\). These conclusions also hold on a concrete operator algebra containing \(I_H\), with its inherited matrix positivity.

**Proof.** Let \(X=[A_{ab}]\) be a positive operator matrix on \(H^k\). Set \(W(z_1,\ldots,z_k)=(Vz_1,\ldots,Vz_k)\). Block multiplication gives
\[
[V^*A_{ab}V]=W^*XW.
\]
Its quadratic form at \(z\in K^k\) is the nonnegative quadratic form of \(X\) at \(Wz\). It is self-adjoint because \(X\) is. This proves positivity at every level, without an infinite-dimensional spectral theorem. Equation (3.1) gives \(\Psi(I_H)=V^*V\). Restricting the same computation proves the assertion for a concrete algebra. \(\square\)

For finite coordinate spaces, a single summand \(A\mapsto QAQ^*\) in (2.3) is a compression with \(V=Q^*\). Finite sums are completely positive by addition of quadratic forms at every level. Compositions are completely positive because the amplified composition is \(\Psi^{(k)}\Phi^{(k)}\): it preserves positivity through two successive applications.

For an orthogonal projection \(P=P^*=P^2\) on \(H\), include \(PH\) in \(H\) by \(V\). Then \(V^*AV\) is \(PAP\) restricted to \(PH\), and \(V^*V=I_{PH}\). The range \(PH\) is closed: a limit \(x\) of vectors fixed by \(P\) still satisfies \(Px=x\). This explains the matrix-level positivity of compression used in [*Extensions of C\*-algebras and the Busby invariant*](../KT-KK-01.html), Proposition 3.2. Its extension and section assertions are proved there.

<a id="cp-transpose"></a>

## 4. Transpose and the exchange of two coordinates

For \(n\geq1\), let \(T_n(A)=A^t\), transpose without conjugation. This is a complex linear map.

**Theorem 4.1.** \(T_n\) is positive for every \(n\). It is completely positive for \(n=1\), and fails to be two-positive for every \(n\geq2\).

**Proof.** For \(A\geq0\), Lemma 1.1 gives \(A=RR^*\). Hence
\[
A^t=\overline R\,R^t
   =\overline R\,(\overline R)^*\geq0.
\tag{4.1}
\]
For \(n=1\), transpose and all its amplifications are identity maps.

For \(n\geq2\), take the first two standard vectors \(p_1,p_2\in\mathbb C^n\), and let \(f_1,f_2\) be the basis of the block coordinate \(\mathbb C^2\). The vector
\[
w=f_1\otimes p_1+f_2\otimes p_2
\]
defines a positive rank-one operator \(X=ww^*\). Its \((a,b)\)-block is \(p_ap_b^*\). Amplified transpose sends it to \(p_bp_a^*\). On the span of the four vectors \(f_a\otimes p_b\), the resulting operator sends
\[
f_a\otimes p_b\longmapsto f_b\otimes p_a.
\]
It vanishes on the other coordinate vectors. The unit vector
\[
\zeta=\frac{f_1\otimes p_2-f_2\otimes p_1}{\sqrt2}
\]
therefore has image \(-\zeta\). Its quadratic form is \(-1\), so \(T_n^{(2)}(X)\) is not positive. \(\square\)

The full Choi matrix acts the same way:
\[
C_{T_n}(e_a\otimes e_b)=e_b\otimes e_a,
\tag{4.2}
\]
since \(C_{T_n}=\sum_{i,j}E_{ij}\otimes E_{ji}\), and only the term with \(j=a,\ i=b\) acts nontrivially. Symmetric vectors have eigenvalue \(+1\), and nonzero antisymmetric vectors have eigenvalue \(-1\). Theorem 2.1 thus also detects the failure of complete positivity. The two-dimensional corner proof establishes the specific failure at level two.

## 5. Exercises with complete solutions

**Exercise 5.1.** The diagonal map \(D:M_n(\mathbb C)\to M_n(\mathbb C)\) removes all off-diagonal entries. Prove that it is completely positive, unital and idempotent. Compute its Choi matrix.

**Solution.** With \(P_i=E_{ii}\), multiplication gives \(P_iAP_i=A_{ii}P_i\), so \(D(A)=\sum_iP_iAP_i\). This is (2.3), hence completely positive. Since \(\sum_iP_i=I_n\), it is unital. Removing off-diagonal entries twice has the same effect as removing them once, so \(D^2=D\). As \(D(E_{ij})=0\) for \(i\ne j\) and \(D(E_{ii})=E_{ii}\),
\[
C_D=\sum_iE_{ii}\otimes E_{ii}.
\]
This is the sum of the rank-one positive operators on \(e_i\otimes e_i\).

**Exercise 5.2.** For \(H=[h_{ij}]\in M_n(\mathbb C)\), define entrywise multiplication \(S_H(A)=[h_{ij}A_{ij}]\). Prove that \(S_H\) is completely positive exactly when \(H\geq0\). Determine when it is unital.

**Solution.** Let \(\mathbf1\) be the column with every entry \(1\). The matrix \(J=\mathbf1\mathbf1^*\) is positive. If \(S_H\) is completely positive, its first level gives \(H=S_H(J)\geq0\).

Conversely, write \(H=\sum_\alpha c_\alpha c_\alpha^*\) by Lemma 1.1, and let \(Q_\alpha\) be diagonal with entries \(c_{\alpha i}\). Then
\[
(Q_\alpha A Q_\alpha^*)_{ij}
=c_{\alpha i}\overline{c_{\alpha j}}A_{ij},
\qquad
S_H(A)=\sum_\alpha Q_\alpha A Q_\alpha^*.
\]
Theorem 2.1 proves complete positivity. The diagonal entries of \(S_H(I_n)\) are \(h_{ii}\), so the map is unital exactly when every \(h_{ii}=1\). No separate entrywise-product theorem is used.

**Exercise 5.3.** On \(M_2(\mathbb C)\), let
\[
\Phi_\lambda(A)=\lambda A+(1-\lambda)A^t,
\qquad 0\leq\lambda\leq1.
\]
Prove that every \(\Phi_\lambda\) is positive and unital, but is completely positive only for \(\lambda=1\).

**Solution.** Identity and transpose are positive and unital. Nonnegative linear combinations preserve positivity by addition of quadratic forms, and the coefficients here sum to one. With \(\Omega=e_1\otimes e_1+e_2\otimes e_2\) and \(F\) the exchange of tensor coordinates, (2.2) and (4.2) give
\[
C_{\Phi_\lambda}
=\lambda\Omega\Omega^*+(1-\lambda)F.
\]
For \(\eta=(e_1\otimes e_2-e_2\otimes e_1)/\sqrt2\), one has \(\Omega^*\eta=0\) and \(F\eta=-\eta\). Its Choi quadratic form is \(-(1-\lambda)\), negative if \(\lambda<1\). Theorem 2.1 rules out complete positivity there. At \(\lambda=1\) the map is the identity and is completely positive.

**Exercise 5.4.** For \(R\in M_m(\mathbb C)\), set \(\Theta_R(A)=\operatorname{Tr}(A)R\) on \(M_n(\mathbb C)\), where \(\operatorname{Tr}(A)=\sum_iA_{ii}\). Determine when it is completely positive, and when it is both completely positive and unital.

**Solution.** Complete positivity implies \(R=\Theta_R(E_{11})\geq0\). Conversely, factor \(R=\sum_\alpha w_\alpha w_\alpha^*\) by Lemma 1.1, and set \(V_{\alpha i}=w_\alpha e_i^*:\mathbb C^n\to\mathbb C^m\). Direct multiplication gives
\[
\sum_{\alpha,i}V_{\alpha i}A V_{\alpha i}^*
=\sum_{\alpha,i}A_{ii}w_\alpha w_\alpha^*
=\operatorname{Tr}(A)R.
\]
Theorem 2.1 proves complete positivity. Since \(\Theta_R(I_n)=nR\), it is unital exactly when \(R=I_m/n\), a positive matrix. Its Choi matrix is \(I_n\otimes R\), because off-diagonal matrix units have trace zero and diagonal ones have trace one.

## Further reading

John M. Erdman, *Functional Analysis and Operator Algebras: An Introduction*, author version dated October 4, 2015, Section 16.4. [Freely accessible author PDF](https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf). This is optional further reading; no external result is required for the proofs above. The linked work retains its author's attribution and licence.

