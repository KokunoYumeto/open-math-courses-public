# PSD factorizations and semidefinite lifts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The perfect matching polytope \(P_n\) of the complete graph \(K_n\) is the convex hull of the indicator vectors of its perfect matchings. Edmonds described the convex hull of the matchings of a graph by linear inequalities [Edmonds 1965]; for the perfect matchings of \(K_n\) his description consists of the nonnegativity of the coordinates, one equation for each vertex and one inequality for each set of vertices of odd size. There are exponentially many odd sets, and one may ask whether \(P_n\) is the projection of a simpler convex set in a higher dimension. Yannakakis related the projections of polyhedra onto a polytope to nonnegative factorizations of a matrix of slacks (see [Braun–Pokutta 2015, Section 2.2.3]), and Rothvoss proved that every polyhedron projecting onto \(P_n\) has \(2^{\Omega(n)}\) facets [Rothvoss 2017]. Semidefinite lifts, which are projections of affine slices of the cone of positive semidefinite matrices, can be much smaller than polyhedral ones. Gouveia, Parrilo and Thomas related them to factorizations by positive semidefinite matrices [GPT 2013], and Lee, Raghavendra and Steurer proved the first exponential lower bounds for semidefinite lifts, for the cut, traveling salesman and stable set polytopes, through sums of squares [LRS 2015].

This course presents OpenAI's proof that every semidefinite lift of \(P_n\) has size \(2^{\Omega(n)}\) [OpenAI-PSD]. The proof bounds the positive semidefinite rank of a matrix built from odd cuts and perfect matchings and shifted by a fixed positive constant. For the same shifted matrices, Braun and Pokutta proved an exponential lower bound for the nonnegative rank [Braun–Pokutta 2015], and Braun and collaborators proved exponential lower bounds for semidefinite lifts that respect the symmetries of \(K_n\) [Braun et al. 2017]. Exactness matters: Kaniewski, Lee and de Wolf approximated the slack matrix of \(P_n\) entrywise up to an exponentially small error by matrices of positive semidefinite rank \(2^{n^{1/2+\varepsilon}}\) [KLdW 2015].

This lesson sets up the objects of the course.

- Positive semidefinite matrices (Section 1).
- PSD factorizations, and a normalization of their traces (Section 2).
- Semidefinite lifts, and the factorizations they give (Section 3).
- Perfect matchings, the shifted matrices and the main theorem (Section 4).

We use the spectral theorem for real symmetric matrices: a real symmetric matrix has an orthonormal basis of eigenvectors, and its eigenvalues are real.

## 1. Positive semidefinite matrices

Write \(\mathbb S^r\) for the space of real symmetric \(r\times r\) matrices, with the inner product \(\langle A,B\rangle=\operatorname{tr}(AB)\). For a real rectangular matrix \(B\), the Frobenius norm \(\|B\|_{\mathrm F}=\operatorname{tr}(B^{\mathsf T}B)^{1/2}\) is the Euclidean norm of its entries, and \(\|B\|_{\mathrm{op}}\) is its operator norm for the Euclidean norms. A matrix \(A\in\mathbb S^r\) is *positive semidefinite*, written \(A\succeq0\), if \(x^{\mathsf T}Ax\ge0\) for all \(x\in\mathbb R^r\), and *positive definite* if \(x^{\mathsf T}Ax>0\) for all \(x\ne0\). The positive semidefinite matrices form a closed convex cone \(\mathbb S^r_+\). We write \(A\preceq B\) when \(B-A\succeq0\).

By the spectral theorem, every \(A\in\mathbb S^r\) can be written \(A=\sum_i\lambda_iu_iu_i^{\mathsf T}\) with an orthonormal basis \((u_i)\) and real numbers \(\lambda_i\). Then \(A\succeq0\) if and only if every \(\lambda_i\ge0\), and \(A\) is positive definite if and only if every \(\lambda_i>0\).

**Lemma 1.1.** Let \(A,B\in\mathbb S^r_+\).

1. There is exactly one \(S\in\mathbb S^r_+\) with \(S^2=A\); it is written \(A^{1/2}\). If \(A\) is positive definite, so is \(A^{1/2}\), and we put \(A^{-1/2}=(A^{1/2})^{-1}\).
2. \(\langle A,B\rangle=\|A^{1/2}B^{1/2}\|_{\mathrm F}^2\ge0\), with equality if and only if \(AB=0\).
3. \(\|A\|_{\mathrm{op}}\le\|A\|_{\mathrm F}\le\operatorname{tr}A\) and \(\operatorname{tr}A\le\sqrt{\operatorname{rank}A}\,\|A\|_{\mathrm F}\).
4. \(\ker(A+B)=\ker A\cap\ker B\), and the range of \(A+B\) is \(\operatorname{range}A+\operatorname{range}B\).
5. If \(P\) is an orthogonal projection on \(\mathbb R^r\) and \(X\) is a real \(r\times r\) matrix, then \(\|PX\|_{\mathrm F}\le\|X\|_{\mathrm F}\) and \(\|PXP\|_{\mathrm F}\le\|X\|_{\mathrm F}\).
6. For every real \(r\times s\) matrix \(V\), the matrix \(V^{\mathsf T}AV\) is positive semidefinite.

*Proof.* (1) With a spectral decomposition as above, \(S=\sum_i\lambda_i^{1/2}u_iu_i^{\mathsf T}\) is positive semidefinite and \(S^2=A\). Let \(S'\succeq0\) with \(S'^2=A\), and write \(S'=\sum_j\sigma_jv_jv_j^{\mathsf T}\) with \(\sigma_j\ge0\) and an orthonormal basis \((v_j)\). Then \(A=\sum_j\sigma_j^2v_jv_j^{\mathsf T}\), so for each eigenvalue \(\lambda\) of \(A\) the eigenspace is spanned by the \(v_j\) with \(\sigma_j^2=\lambda\), that is, with \(\sigma_j=\lambda^{1/2}\). Thus \(S'\) acts as \(\lambda^{1/2}\) on every eigenspace of \(A\), and \(S'=S\). If every \(\lambda_i>0\), the eigenvalues \(\lambda_i^{1/2}\) of \(S\) are positive.

(2) By the cyclicity of the trace and \((A^{1/2}B^{1/2})^{\mathsf T}=B^{1/2}A^{1/2}\),
\[
\begin{aligned}\operatorname{tr}(AB)&=\operatorname{tr}\bigl(B^{1/2}A^{1/2}A^{1/2}B^{1/2}\bigr)\\&=\|A^{1/2}B^{1/2}\|_{\mathrm F}^2 .\end{aligned}
\]
If this vanishes, then \(A^{1/2}B^{1/2}=0\) and \(AB=A^{1/2}(A^{1/2}B^{1/2})B^{1/2}=0\). Conversely \(AB=0\) gives \(\operatorname{tr}(AB)=0\).

(3) With the eigenvalues \(\lambda_i\ge0\) of \(A\), we have \(\|A\|_{\mathrm{op}}=\max_i\lambda_i\), \(\|A\|_{\mathrm F}=(\sum_i\lambda_i^2)^{1/2}\) and \(\operatorname{tr}A=\sum_i\lambda_i\). This gives the first two inequalities, and the Cauchy–Schwarz inequality over the \(\operatorname{rank}A\) nonzero eigenvalues gives the third.

(4) If \((A+B)x=0\), then \(x^{\mathsf T}Ax+x^{\mathsf T}Bx=0\) with two nonnegative terms, so \(\|A^{1/2}x\|^2=x^{\mathsf T}Ax=0\), whence \(Ax=A^{1/2}A^{1/2}x=0\); likewise \(Bx=0\). The reverse inclusion is clear. Since a symmetric matrix \(C\) has \(\operatorname{range}C=(\ker C)^\perp\), taking orthogonal complements gives the statement on ranges.

(5) The number \(\|PX\|_{\mathrm F}^2\) is the sum of \(\|Px_c\|^2\le\|x_c\|^2\) over the columns \(x_c\) of \(X\). Applied to \(X^{\mathsf T}\), this gives \(\|XP\|_{\mathrm F}=\|PX^{\mathsf T}\|_{\mathrm F}\le\|X\|_{\mathrm F}\), and the two bounds combine.

(6) For \(x\in\mathbb R^s\), \(x^{\mathsf T}V^{\mathsf T}AVx=(Vx)^{\mathsf T}A(Vx)\ge0\). \(\square\)

## 2. PSD factorizations

Let \(S\) be a finite matrix with nonnegative real entries, with rows indexed by a set \(I\) and columns by a set \(J\).

**Definition 2.1.** A *PSD factorization of size \(r\)* of \(S\) consists of matrices \(F_i\in\mathbb S^r_+\) (\(i\in I\)) and \(G_j\in\mathbb S^r_+\) (\(j\in J\)) with
\[
S_{ij}=\langle F_i,G_j\rangle\qquad(i\in I,\ j\in J).
\]
The \(F_i\) are the *row factors* and the \(G_j\) the *column factors*. The *PSD rank* \(\operatorname{rank}_{\mathrm{psd}}S\) is the least \(r\ge1\) for which \(S\) has a PSD factorization of size \(r\).

Factorizations exist: the diagonal matrices \(F_i=\operatorname{diag}(S_{ij})_{j\in J}\) and \(G_j=e_je_j^{\mathsf T}\) give one of size \(|J|\). The entries must be reproduced exactly, and no symmetry, sparsity or precision condition is imposed on the factors.

**Lemma 2.2.** Let \(S\) be as above.

1. If \(S'\) consists of some of the rows of \(S\), or of some of its columns, then \(\operatorname{rank}_{\mathrm{psd}}S'\le\operatorname{rank}_{\mathrm{psd}}S\).
2. If every row of a matrix \(S'\) is a linear combination with nonnegative coefficients of rows of \(S\), then \(\operatorname{rank}_{\mathrm{psd}}S'\le\operatorname{rank}_{\mathrm{psd}}S\).
3. If \(\rho\ge0\) and \(\mathbf 1\) is the matrix of the same shape with all entries one, then \(\operatorname{rank}_{\mathrm{psd}}(S+\rho\mathbf 1)\le\operatorname{rank}_{\mathrm{psd}}S+1\).
4. If \(S_{ij}=\sum_{k=1}^ra_{ik}b_{kj}\) with all \(a_{ik},b_{kj}\ge0\), then \(\operatorname{rank}_{\mathrm{psd}}S\le r\).

*Proof.* (1) Restrict a factorization of \(S\). (2) If row \(i'\) of \(S'\) is \(\sum_ic_{i'i}\) times row \(i\) of \(S\), with \(c_{i'i}\ge0\), use the row factors \(\sum_ic_{i'i}F_i\succeq0\). (3) Use the block diagonal matrices \(F_i\oplus(\rho)\) and \(G_j\oplus(1)\) of size \(r+1\). (4) Use the diagonal matrices \(\operatorname{diag}(a_{ik})_{k\le r}\) and \(\operatorname{diag}(b_{kj})_{k\le r}\). \(\square\)

The least \(r\) in part 4 is the *nonnegative rank* \(\operatorname{rank}_+S\); thus \(\operatorname{rank}_{\mathrm{psd}}S\le\operatorname{rank}_+S\). The next lemma bounds the traces of the factors; it is used in [The lower bound for perfect matching](the-lower-bound-for-perfect-matching.md).

**Lemma 2.3** (normalization; [OpenAI-PSD, Lemma 6.1]). Let \(S\ne0\) be a finite nonnegative matrix whose entries are at most \(B\). If \(S\) has a PSD factorization of size \(r_0\), then it has one of some size \(r\le r_0\) with
\[
\begin{gathered}\operatorname{tr}F_i\le B,\qquad\operatorname{tr}G_j\le r\\ (i\in I,\ j\in J).\end{gathered}
\]

*Proof.* *Compression.* Let \(W\subseteq\mathbb R^{r_0}\) be the sum of the ranges of the column factors, put \(r=\dim W\), and let \(V\) be an \(r_0\times r\) matrix whose columns form an orthonormal basis of \(W\). Since \(S\ne0\), some \(G_j\ne0\), so \(r\ge1\). The matrix \(VV^{\mathsf T}\) is the orthogonal projection onto \(W\), which contains the range of each \(G_j\), so \(G_j=VV^{\mathsf T}G_jVV^{\mathsf T}\). Put \(F'_i=V^{\mathsf T}F_iV\) and \(G'_j=V^{\mathsf T}G_jV\); they are positive semidefinite by Lemma 1.1(6), and
\[
\langle F'_i,G'_j\rangle=\operatorname{tr}\bigl(F_iVV^{\mathsf T}G_jVV^{\mathsf T}\bigr)=S_{ij}.
\]
Since \(G_j=VG'_jV^{\mathsf T}\) and \(V^{\mathsf T}\) maps onto \(\mathbb R^r\), the range of \(G_j\) is the image under \(V\) of the range of \(G'_j\). As \(V\) is injective, the ranges of the \(G'_j\) span \(\mathbb R^r\), and by Lemma 1.1(4) their average \(\bar G\) is positive definite.

*A matrix of largest determinant.* The convex hull \(\mathcal K\) of the finitely many \(G'_j\) is compact and the determinant is continuous, so the determinant attains its maximum on \(\mathcal K\) at some \(Z\in\mathcal K\). As \(\det Z\ge\det\bar G>0\) and \(Z\succeq0\), the matrix \(Z\) is positive definite. Fix \(j\), and let \(\mu_1,\ldots,\mu_r\) be the eigenvalues of the symmetric matrix \(N=Z^{-1/2}(G'_j-Z)Z^{-1/2}\). For \(0<s\le1\) the matrix \(Z+s(G'_j-Z)=Z^{1/2}(I+sN)Z^{1/2}\) lies in \(\mathcal K\), so
\[
\begin{aligned}\det Z&\ge\det\bigl(Z+s(G'_j-Z)\bigr)\\&=\det Z\,\prod_{k=1}^r(1+s\mu_k).\end{aligned}
\]
For small \(s>0\) all factors are positive, and \(\sum_k\log(1+s\mu_k)\le0\). Dividing by \(s\) and letting \(s\to0^+\) gives \(\sum_k\mu_k\le0\). Since \(\operatorname{tr}N=\operatorname{tr}(Z^{-1}G'_j)-r\), this says
\[
\operatorname{tr}(Z^{-1}G'_j)\le r .
\]

*New factors.* Put \(G''_j=Z^{-1/2}G'_jZ^{-1/2}\) and \(F''_i=Z^{1/2}F'_iZ^{1/2}\). They are positive semidefinite by Lemma 1.1(6), the cyclicity of the trace gives \(\langle F''_i,G''_j\rangle=\langle F'_i,G'_j\rangle=S_{ij}\), and \(\operatorname{tr}G''_j=\operatorname{tr}(Z^{-1}G'_j)\le r\). Writing \(Z=\sum_jc_jG'_j\) as a convex combination,
\[
\operatorname{tr}F''_i=\langle F'_i,Z\rangle=\sum_jc_jS_{ij}\le B. \qquad\square
\]

## 3. Semidefinite lifts

**Definition 3.1.** Let \(P\subseteq\mathbb R^m\) be convex. A *semidefinite lift of size \(r\)* of \(P\) consists of an affine subspace \(L\subseteq\mathbb S^r\) and an affine map \(\pi\colon\mathbb S^r\to\mathbb R^m\) with
\[
P=\pi\bigl(L\cap\mathbb S^r_+\bigr).
\]

A linear function is then maximized over \(P\) by a semidefinite program over the slice \(L\cap\mathbb S^r_+\). The next results show that a lift supplies certificates by positive semidefinite matrices for the affine functions that are nonnegative on \(P\).

**Lemma 3.2** (a slice with an interior point). Let \(P\) be a convex set with at least two points and with a semidefinite lift \((L,\pi)\) of size \(r\). Then \(P\) has a semidefinite lift \((L',\pi')\) of some size \(w\le r\) such that \(L'\) contains a positive definite matrix.

*Proof.* The set \(Q=L\cap\mathbb S^r_+\) is convex and has at least two points. Let \(W\subseteq\mathbb R^r\) be the sum of the ranges of all elements of \(Q\). Since \(\mathbb R^r\) has finite dimension, \(W\) is the sum of the ranges of finitely many \(Y_1,\ldots,Y_k\in Q\), and their average \(\bar Y\in Q\) has range \(W\) by Lemma 1.1(4). As \(Q\) contains a nonzero matrix, \(w=\dim W\ge1\). Let \(V\) be an \(r\times w\) matrix whose columns form an orthonormal basis of \(W\). Every \(Y\in Q\) satisfies \(Y=VV^{\mathsf T}YVV^{\mathsf T}\), because \(VV^{\mathsf T}\) is the orthogonal projection onto a space containing the range of the symmetric matrix \(Y\). Put
\[
\begin{gathered}
L'=\{Y'\in\mathbb S^w:VY'V^{\mathsf T}\in L\},\\
\pi'(Y')=\pi(VY'V^{\mathsf T}).
\end{gathered}
\]
Then \(L'\) is an affine subspace of \(\mathbb S^w\) and \(\pi'\) is affine. If \(Y'\in L'\cap\mathbb S^w_+\), then \(VY'V^{\mathsf T}\in Q\) by Lemma 1.1(6), so \(\pi'(Y')\in P\). Conversely, for \(Y\in Q\) the matrix \(Y'=V^{\mathsf T}YV\) is positive semidefinite, \(VY'V^{\mathsf T}=Y\in L\), and \(\pi'(Y')=\pi(Y)\). Hence \(P=\pi'(L'\cap\mathbb S^w_+)\). Finally, \(\bar Y'=V^{\mathsf T}\bar YV\) lies in \(L'\), and \(V\bar Y'V^{\mathsf T}=\bar Y\) has range \(W\) of dimension \(w\). As in the proof of Lemma 2.3, the range of \(\bar Y'\) has dimension \(w\), so \(\bar Y'\) is invertible and therefore positive definite. \(\square\)

**Lemma 3.3** (affine certificates). Let \(L\subseteq\mathbb S^w\) be an affine subspace containing a positive definite matrix \(Y_0\), and let \(\ell\colon\mathbb S^w\to\mathbb R\) be an affine function with \(\ell(Y)\ge0\) for all \(Y\in L\cap\mathbb S^w_+\). Then there are \(F\in\mathbb S^w_+\) and \(\mu\ge0\) with
\[
\ell(Y)=\langle F,Y\rangle+\mu\qquad(Y\in L).
\]

*Proof.* Write \(L=Y_0+U\) with a linear subspace \(U\), let \(\Pi\) be the orthogonal projection of \(\mathbb S^w\) onto \(U\), and write \(\ell(Y)=c+\langle A,Y-Y_0\rangle\) with \(c=\ell(Y_0)\ge0\) and \(A\in\mathbb S^w\). On \(U\times\mathbb R\) use the inner product \(\langle(X,\beta),(X',\beta')\rangle=\langle X,X'\rangle+\beta\beta'\), and consider
\[
\begin{aligned}\mathcal Q=\bigl\{&(\Pi F,\ \langle F,Y_0\rangle+t):\\&F\in\mathbb S^w_+,\ t\ge0\bigr\}.\end{aligned}
\]
Suppose that \((\Pi A,c)\in\mathcal Q\), say \(\Pi A=\Pi F\) and \(c=\langle F,Y_0\rangle+t\). For \(Y\in L\) we have \(Y-Y_0\in U\), so \(\langle A,Y-Y_0\rangle=\langle\Pi A,Y-Y_0\rangle\), which equals \(\langle F,Y-Y_0\rangle\), and
\[
\ell(Y)=c+\langle F,Y-Y_0\rangle=\langle F,Y\rangle+t .
\]
Then \(\mu=t\) has the required property. It remains to show that \((\Pi A,c)\in\mathcal Q\).

*The set \(\mathcal Q\) is a closed convex cone.* It is a convex cone because \(\mathbb S^w_+\) is one. Let \(\lambda_0>0\) be the least eigenvalue of \(Y_0\). For \(F\succeq0\), Lemma 1.1(2) applied to \(F\) and \(Y_0-\lambda_0I\succeq0\), and Lemma 1.1(3), give
\[
\langle F,Y_0\rangle\ge\lambda_0\operatorname{tr}F\ge\lambda_0\|F\|_{\mathrm F}.
\]
Hence, if a sequence \((\Pi F_k,\langle F_k,Y_0\rangle+t_k)\) in \(\mathcal Q\) converges, the \(F_k\) and \(t_k\) are bounded. A subsequence has \(F_k\to F\succeq0\) and \(t_k\to t\ge0\), and the limit equals \((\Pi F,\langle F,Y_0\rangle+t)\in\mathcal Q\).

*Separation.* Suppose that \(z=(\Pi A,c)\notin\mathcal Q\). The distance to \(z\) attains a minimum on the closed set \(\mathcal Q\), at some \(q\): minimize over the compact intersection of \(\mathcal Q\) with a large ball. For \(x\in\mathcal Q\) and \(0<s\le1\), the point \(q+s(x-q)\) lies in \(\mathcal Q\), so \(\|q+s(x-q)-z\|^2\ge\|q-z\|^2\); dividing by \(s\) and letting \(s\to0\) gives \(\langle q-z,x-q\rangle\ge0\). The choices \(x=0\) and \(x=2q\) give \(\langle q-z,q\rangle=0\). Therefore \(\omega=q-z\ne0\) satisfies
\[
\begin{gathered}\langle\omega,x\rangle\ge0\quad(x\in\mathcal Q),\\ \langle\omega,z\rangle=-\|\omega\|^2<0 .\end{gathered}
\]
Write \(\omega=(X,\beta)\) with \(X\in U\). As \(\langle X,\Pi F\rangle=\langle X,F\rangle\), the first property says
\[
\begin{gathered}\langle F,X+\beta Y_0\rangle+\beta t\ge0\\ (F\succeq0,\ t\ge0).\end{gathered}
\]
With \(F=0\) and \(t=1\) this gives \(\beta\ge0\); with \(t=0\) and \(F=xx^{\mathsf T}\) it gives \(X+\beta Y_0\succeq0\). Since \(\langle X,\Pi A\rangle=\langle X,A\rangle\), the second property says \(\langle A,X\rangle+\beta c<0\).

If \(\beta>0\), the matrix \(Y=Y_0+X/\beta\) lies in \(L\) and equals \((X+\beta Y_0)/\beta\succeq0\), so \(0\le\ell(Y)=c+\langle A,X\rangle/\beta\), a contradiction. If \(\beta=0\), then \(X\succeq0\), so \(Y_0+sX\in L\cap\mathbb S^w_+\) for every \(s\ge0\). Then \(0\le\ell(Y_0+sX)=c+s\langle A,X\rangle\) for all \(s\ge0\), which forces \(\langle A,X\rangle\ge0\), again a contradiction. \(\square\)

**Proposition 3.4** (lifts give factorizations). Let \(P\subseteq\mathbb R^m\) be a convex set with at least two points that has a semidefinite lift of size \(r\). Let \(v_j\in P\) (\(j\in J\)) be finitely many points, and let \(\ell_i\) (\(i\in I\)) be finitely many affine functions on \(\mathbb R^m\) that are nonnegative on \(P\). Then the matrix \(S_{ij}=\ell_i(v_j)\) satisfies
\[
\operatorname{rank}_{\mathrm{psd}}S\le r+1 .
\]

*Proof.* Lemma 3.2 gives a lift \((L',\pi')\) of some size \(w\le r\) such that \(L'\) contains a positive definite matrix. Choose \(Y_j\in L'\cap\mathbb S^w_+\) with \(\pi'(Y_j)=v_j\). The affine function \(\ell_i\circ\pi'\) is nonnegative on \(L'\cap\mathbb S^w_+\), so Lemma 3.3 gives \(F_i\succeq0\) and \(\mu_i\ge0\) with \(\ell_i(\pi'(Y))=\langle F_i,Y\rangle+\mu_i\) for \(Y\in L'\). Hence
\[
\begin{aligned}
S_{ij}&=\langle F_i,Y_j\rangle+\mu_i\\
&=\bigl\langle F_i\oplus(\mu_i),\,Y_j\oplus(1)\bigr\rangle,
\end{aligned}
\]
a PSD factorization of size \(w+1\le r+1\). \(\square\)

Gouveia, Parrilo and Thomas proved, for full-dimensional polytopes, that conversely a factorization of a slack matrix by a cone yields a lift to that cone [GPT 2013, Section 3]. Thus PSD rank measures the size of semidefinite lifts; this course needs only Proposition 3.4.

## 4. Perfect matchings and the shifted matrices

Let \(n\ge4\) be even. Write \(K_n\) for the complete graph on \([n]=\{1,\ldots,n\}\), \(E_n\) for its edges, \(\mathcal M_n\) for its perfect matchings and \(\mathcal O_n\) for the subsets of \([n]\) of odd size. For \(U\subseteq[n]\), let \(\delta(U)\) be the set of edges with exactly one endpoint in \(U\).

**Lemma 4.1.** For \(M\in\mathcal M_n\) and \(U\in\mathcal O_n\), the number \(|M\cap\delta(U)|\) is odd; in particular it is at least one.

*Proof.* The edges of \(M\) with both endpoints in \(U\) cover an even number of vertices of \(U\). Each other vertex of \(U\) is matched by an edge of \(\delta(U)\), and distinct vertices use distinct edges. So \(|M\cap\delta(U)|\) is \(|U|\) minus an even number, and it is odd. \(\square\)

**Definition 4.2.** For \(0\le\rho\le1\), the matrix \(A_n(\rho)\) has rows indexed by \(\mathcal O_n\), columns indexed by \(\mathcal M_n\), and entries
\[
A_n(\rho)_{U,M}=|M\cap\delta(U)|-1+\rho .
\]
The matrix \(T_n(\rho)\) is obtained from \(A_n(\rho)\) by adding the rows \(T_n(\rho)_{e,M}=\mathbf 1_{\{e\in M\}}\) for \(e\in E_n\).

By Lemma 4.1 these matrices are nonnegative, and the entries of \(A_n(\rho)\) are positive when \(\rho>0\). Let
\[
P_n=\operatorname{conv}\{\mathbf 1_M:M\in\mathcal M_n\}\subseteq\mathbb R^{E_n},
\]
where \(\mathbf 1_M\) is the indicator vector of \(M\). For \(U\in\mathcal O_n\) and \(e\in E_n\), the affine functions
\[
\ell_U(x)=\sum_{f\in\delta(U)}x_f-1,\qquad \ell_e(x)=x_e
\]
are nonnegative at every vertex \(\mathbf 1_M\) by Lemma 4.1, hence on the convex hull \(P_n\). Their values at the vertices are the entries of \(T_n(0)\): \(\ell_U(\mathbf 1_M)=A_n(0)_{U,M}\) and \(\ell_e(\mathbf 1_M)=\mathbf 1_{\{e\in M\}}\). By Edmonds's theorem [Edmonds 1965, Theorem (P)], the inequalities \(\ell_U\ge0\) and \(\ell_e\ge0\), together with the equations \(\sum_{f\ni v}x_f=1\) for the vertices \(v\), describe \(P_n\), so \(T_n(0)\) is a slack matrix of a description of \(P_n\); the arguments below use only that the \(\ell_U\) are nonnegative on \(P_n\).

For \(\rho=1\) the entries are \(|M\cap\delta(U)|=\sum_{e\in E_n}\mathbf 1_{\{e\in\delta(U)\}}\mathbf 1_{\{e\in M\}}\), so Lemma 2.2(4) gives \(\operatorname{rank}_{\mathrm{psd}}A_n(1)\le\binom n2\). An exponential lower bound therefore needs \(\rho<1\).

**Theorem 4.3** ([OpenAI-PSD, Theorem 1.1]). There is a constant \(c>0\) such that for every \(0<\rho<1\) there is \(n_0(\rho)\) with
\[
\operatorname{rank}_{\mathrm{psd}}A_n(\rho)\ge2^{cn}
\]
for every even \(n\ge n_0(\rho)\).

**Corollary 4.4** ([OpenAI-PSD, Corollary 1.2]). There are \(c_0>0\) and \(n_1\) such that for every even \(n\ge n_1\), the matrices \(A_n(0)\) and \(T_n(0)\) have PSD rank at least \(2^{c_0n}\), and every semidefinite lift of \(P_n\) has size at least \(2^{c_0n}\).

Both are proved in [The lower bound for perfect matching](the-lower-bound-for-perfect-matching.md). The rate \(c\) does not depend on \(\rho\); only the threshold \(n_0(\rho)\) does. Since \(\operatorname{rank}_{\mathrm{psd}}\le\operatorname{rank}_+\), Theorem 4.3 also bounds the nonnegative rank of \(A_n(\rho)\) from below; for the matrices with entries \((|M\cap\delta(U)|-1+\rho)/2\), which have the same nonnegative rank, an exponential lower bound was proved by Braun and Pokutta with methods from information theory [Braun–Pokutta 2015, Theorem 3.1].

*The plan of the proof.* The obstruction is a system of parity conditions on an expanding graph \(H\) with \(t\) vertices: each vertex carries \(d\) bits, one for each incident edge, with prescribed parities whose sum is odd, so that some edge has different bits at its two ends. A linear functional built from cuts of \(H\) is nonnegative on squares of functions of low degree but negative on the number of disagreeing edges minus \(1-\rho\) ([An expanding parity system](an-expanding-parity-system.md)). Each vertex of \(H\) becomes a cell of \(k\) vertices of \(K_n\), for a large constant \(k\), and odd cuts restricted to the cells realize the disagreement count exactly. Averaging a row factor over these restrictions ([Averaging within a cell](averaging-within-a-cell.md)) and splitting the averages into squares ([Splitting positive semidefinite matrices](splitting-positive-semidefinite-matrices.md) and [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md)) turns a small factorization into an approximate representation of that function by squares of low degree, which the functional rules out. A further smoothing theorem for averages over perfect matchings is proved in [Uniform smoothing of matching averages](uniform-smoothing-of-matching-averages.md).

## 5. Exercises

**5.1.** Show that the identity matrix \(I_r\) has PSD rank \(r\).

**5.2.** Show that every entry of \(A_4(\rho)\) equals \(\rho\), and determine \(\operatorname{rank}_{\mathrm{psd}}A_4(\rho)\).

**5.3.** Let \(P=\operatorname{conv}\{v_1,\ldots,v_N\}\subseteq\mathbb R^m\). Show that the diagonal matrices of trace one in \(\mathbb S^N\) form an affine subspace \(L\), and that \(L\) with \(\pi(Y)=\sum_jY_{jj}v_j\) is a semidefinite lift of \(P\) of size \(N\).

**5.4.** Show that a nonnegative matrix \(S\) with \(\operatorname{rank}_{\mathrm{psd}}S=r\) has rank at most \(r(r+1)/2\).

**5.5.** Let \(S=I_2\), \(B=1\), and consider the factorization \(F_1=\operatorname{diag}(2,0)\), \(F_2=\operatorname{diag}(0,\tfrac12)\), \(G_1=\operatorname{diag}(\tfrac12,0)\), \(G_2=\operatorname{diag}(0,2)\). Carry out the proof of Lemma 2.3 for it.

## 6. Solutions

**5.1.** The diagonal factorization has size \(r\). Conversely, let \(F_i,G_j\in\mathbb S^s_+\) satisfy \(\langle F_i,G_j\rangle=\delta_{ij}\). For \(i\ne j\), Lemma 1.1(2) gives \(F_iG_j=0\). Since \(\langle F_i,G_i\rangle=1\), we have \(F_iG_i\ne0\), so there is \(y_i\) in the range of \(G_i\) with \(F_iy_i\ne0\); and \(F_iy_j=0\) for \(j\ne i\). If \(\sum_jc_jy_j=0\), applying \(F_i\) gives \(c_iF_iy_i=0\), so \(c_i=0\). Thus \(y_1,\ldots,y_r\) are linearly independent in \(\mathbb R^s\), and \(s\ge r\).

**5.2.** An odd subset of \([4]\) has one or three elements, and \(\delta(U)=\delta([4]\setminus U)\). So \(\delta(U)\) is the set of edges at one vertex \(v\), and every perfect matching has exactly one edge at \(v\). Hence every entry is \(1-1+\rho=\rho\). The factors \(F_U=(\rho)\) and \(G_M=(1)\) have size one, so the PSD rank is one (also for \(\rho=0\), with \(F_U=(0)\)).

**5.3.** The diagonal matrices of trace one form an affine subspace. A diagonal matrix is positive semidefinite exactly when its diagonal entries are nonnegative, so \(L\cap\mathbb S^N_+\) consists of the matrices \(\operatorname{diag}(p)\) with \(p\ge0\) and \(\sum_jp_j=1\), and \(\pi(\operatorname{diag}(p))=\sum_jp_jv_j\) runs through all convex combinations of the \(v_j\).

**5.4.** Choose a basis of the space \(\mathbb S^r\), of dimension \(r(r+1)/2\), and write \(F_i\) and \(G_j\) as coordinate vectors \(f_i,g_j\). The bilinear form \(\langle\cdot,\cdot\rangle\) has a matrix \(\Gamma\) in this basis, so \(S_{ij}=f_i^{\mathsf T}\Gamma g_j\). Thus \(S=X^{\mathsf T}\Gamma Y\), where the columns of \(X\) and \(Y\) are the \(f_i\) and the \(g_j\), and \(\operatorname{rank}S\le r(r+1)/2\).

**5.5.** The column factors already span \(\mathbb R^2\), so no compression occurs. The convex hull of \(G_1,G_2\) consists of the matrices \(\operatorname{diag}(s/2,2(1-s))\), \(0\le s\le1\), with determinant \(s(1-s)\), largest at \(s=1/2\); so \(Z=\operatorname{diag}(\tfrac14,1)\). Then \(G''_1=\operatorname{diag}(2,0)\) and \(G''_2=\operatorname{diag}(0,2)\) have trace \(2=r\), and \(F''_1=\operatorname{diag}(\tfrac12,0)\) and \(F''_2=\operatorname{diag}(0,\tfrac12)\) have trace \(\tfrac12\le B\). The pairings \(\langle F''_i,G''_j\rangle=\delta_{ij}\) are unchanged.

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
- [Edmonds 1965] J. Edmonds, *Maximum matching and a polyhedron with 0,1-vertices*, J. Res. Nat. Bur. Standards Sect. B 69B (1965), 125–130. https://doi.org/10.6028/jres.069B.013
- [Rothvoss 2017] T. Rothvoss, *The matching polytope has exponential extension complexity*, J. ACM 64 (2017). https://arxiv.org/abs/1311.2369
- [GPT 2013] J. Gouveia, P. A. Parrilo, R. R. Thomas, *Lifts of convex sets and cone factorizations*, Math. Oper. Res. 38 (2013). https://arxiv.org/abs/1111.3164
- [LRS 2015] J. R. Lee, P. Raghavendra, D. Steurer, *Lower bounds on the size of semidefinite programming relaxations*, Proc. 47th ACM Symposium on Theory of Computing (2015). https://arxiv.org/abs/1411.6317
- [Braun–Pokutta 2015] G. Braun, S. Pokutta, *The matching problem has no fully polynomial size linear programming relaxation schemes*, IEEE Trans. Inform. Theory 61 (2015); preprint title *The matching polytope does not admit fully-polynomial size relaxation schemes*. https://arxiv.org/abs/1403.6710
- [Braun et al. 2017] G. Braun, J. Brown-Cohen, A. Huq, S. Pokutta, P. Raghavendra, A. Roy, B. Weitz, D. Zink, *The matching problem has no small symmetric SDP*, Math. Program. 165 (2017). https://arxiv.org/abs/1504.00703
- [KLdW 2015] J. Kaniewski, T. Lee, R. de Wolf, *Query complexity in expectation*, ICALP 2015. https://arxiv.org/abs/1411.7280
