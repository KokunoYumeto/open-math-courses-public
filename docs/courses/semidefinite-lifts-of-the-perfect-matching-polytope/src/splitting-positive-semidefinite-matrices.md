# Splitting positive semidefinite matrices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two positive semidefinite matrices \(A_1,A_2\) have \(\langle A_1,A_2\rangle=0\) exactly when \(A_1A_2=0\), that is, when their ranges are orthogonal (Lemma 1.1(2) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md)). Then the whole space splits orthogonally into a part that carries \(A_1\) and a part that carries \(A_2\). This lesson proves a quantitative version for any finite family: if the pairwise overlaps \(\langle A_z,A_{z'}\rangle\) are small, the space splits orthogonally into summands, one for each matrix, such that every matrix is small on the summands of the others. The bound depends on the number of matrices but not on the dimension [OpenAI-PSD, Section 3]. In [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md) the lemma is applied to Gram matrices of Fourier coefficients.

- Block decompositions, and the case of two matrices (Section 1).
- The splitting lemma (Section 2).

Throughout, \(E\) is a finite-dimensional real inner product space, matrices are linear operators on \(E\) written in an orthonormal basis, and \(\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)\) with \(\|X\|_{\mathrm F}^2=\langle X,X\rangle\). An *orthogonal projection* is a symmetric \(P\) with \(P^2=P\); the zero operator is allowed.

## 1. Block decompositions, and two matrices

Let \(P\) be an orthogonal projection and \(Q=I-P\). For an operator \(X\) write
\[
\begin{gathered}X_{11}=PXP,\quad X_{12}=PXQ,\\ X_{21}=QXP,\quad X_{22}=QXQ .\end{gathered}
\]

**Lemma 1.1.** For operators \(X,Y\) on \(E\),
\[
\begin{aligned}\langle X,Y\rangle&=\langle X_{11},Y_{11}\rangle+\langle X_{12},Y_{12}\rangle\\&\quad+\langle X_{21},Y_{21}\rangle+\langle X_{22},Y_{22}\rangle .\end{aligned}
\]
If \(X\) and \(Y\) are symmetric, the two middle terms are equal. If \(X\succeq0\), then \(X_{11}\succeq0\) and \(X_{22}\succeq0\).

*Proof.* We have \(X=X_{11}+X_{12}+X_{21}+X_{22}\), and the four parts are mutually orthogonal: for instance \(\langle PXP,PYQ\rangle=\operatorname{tr}(PX^{\mathsf T}PYQ)\), which equals \(\operatorname{tr}(QPX^{\mathsf T}PY)=0\) because \(QP=0\), and the other cases are the same. For symmetric \(X,Y\) we have \(X_{21}=X_{12}^{\mathsf T}\) and \(Y_{21}=Y_{12}^{\mathsf T}\), so \(\langle X_{21},Y_{21}\rangle=\langle X_{12},Y_{12}\rangle\). The last statement is Lemma 1.1(6) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md). \(\square\)

**Lemma 1.2** (two matrices; [OpenAI-PSD, Section 3]). Let \(A,B\succeq0\), let \(P\) be the orthogonal projection onto the span of the eigenvectors of \(A-B\) with nonnegative eigenvalues, and \(Q=I-P\). Then
\[
\langle A,B\rangle\ge\|PBP\|_{\mathrm F}^2+\|QAQ\|_{\mathrm F}^2 .
\]

*Proof.* The projection \(P\) commutes with \(A-B\), so \(P(A-B)Q=0\), that is \(A_{12}=B_{12}\). For every \(x\), the vector \(Px\) lies in the span of eigenvectors of \(A-B\) with nonnegative eigenvalues, so \(x^{\mathsf T}P(A-B)Px\ge0\); thus \(A_{11}-B_{11}\succeq0\). In the same way \(B_{22}-A_{22}\succeq0\). By Lemma 1.1,
\[
\begin{aligned}\langle A,B\rangle&=\langle A_{11},B_{11}\rangle+\langle A_{22},B_{22}\rangle\\&\quad+2\|A_{12}\|_{\mathrm F}^2 .\end{aligned}
\]
Since \(B_{11}\succeq0\) and \(A_{11}-B_{11}\succeq0\), Lemma 1.1(2) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md) gives
\[
\begin{aligned}\langle A_{11},B_{11}\rangle&=\langle A_{11}-B_{11},B_{11}\rangle\\&\quad+\|B_{11}\|_{\mathrm F}^2\ge\|B_{11}\|_{\mathrm F}^2 .\end{aligned}
\]
Likewise \(\langle A_{22},B_{22}\rangle\ge\|A_{22}\|_{\mathrm F}^2\). As \(B_{11}=PBP\) and \(A_{22}=QAQ\), the inequality follows. \(\square\)

## 2. The splitting lemma

**Theorem 2.1** (orthogonal splitting; [OpenAI-PSD, Lemma 3.1]). Let \(A_1,\ldots,A_L\) be positive semidefinite operators on \(E\). There are mutually orthogonal projections \(P_1,\ldots,P_L\), some of which may be zero, with \(\sum_{s=1}^LP_s=I\) and
\[
\begin{aligned}&\sum_{z=1}^L\sum_{s\ne z}\|P_sA_zP_s\|_{\mathrm F}^2\\&\quad\le C_L\sum_{z\ne z'}\langle A_z,A_{z'}\rangle,\\&C_L=2^{L-1}.\end{aligned}\tag{2.1}
\]
The sum on the right runs over ordered pairs of distinct indices.

*Proof.* We prove (2.1), for every finite-dimensional \(E\), by induction on \(L\). For \(L=1\) take \(P_1=I\); both sides vanish.

Let \(L\ge2\). Put \(B=\sum_{j=2}^LA_j\), let \(P\) and \(Q=I-P\) be as in Lemma 1.2 for \(A=A_1\) and this \(B\), and put \(P_1=P\). The operators \(QA_jQ\), \(2\le j\le L\), restrict to positive semidefinite operators on the range of \(Q\), an inner product space with the induced inner product. The induction hypothesis gives mutually orthogonal projections of the range of \(Q\) with sum the identity there; extended by zero on the range of \(P\), they are mutually orthogonal projections \(P_2,\ldots,P_L\) of \(E\) with \(\sum_{s\ge2}P_s=Q\), and
\[
\begin{aligned}&\sum_{z\ge2}\sum_{\substack{s\ge2\\ s\ne z}}\|P_s(QA_zQ)P_s\|_{\mathrm F}^2\\&\quad\le C_{L-1}\sum_{\substack{j\ne j'\\ j,j'\ge2}}\langle QA_jQ,QA_{j'}Q\rangle .\end{aligned}
\]
Then \(P_1,\ldots,P_L\) are mutually orthogonal projections with sum \(P+Q=I\). We split the left side of (2.1) into three parts.

*The terms with \(s=1\) or \(z=1\).* By Lemma 1.1(2) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md), \(\langle PA_jP,PA_{j'}P\rangle\ge0\), so
\[
\begin{aligned}\sum_{j\ge2}\|PA_jP\|_{\mathrm F}^2&\le\Bigl\|\sum_{j\ge2}PA_jP\Bigr\|_{\mathrm F}^2\\&=\|PBP\|_{\mathrm F}^2 .\end{aligned}
\]
The operators \(P_sA_1P_{s'}\), \(s,s'\ge2\), are mutually orthogonal and have sum \(QA_1Q\), so \(\sum_{s\ge2}\|P_sA_1P_s\|_{\mathrm F}^2\le\|QA_1Q\|_{\mathrm F}^2\). With Lemma 1.2, the terms with \(s=1\) or \(z=1\) have sum at most
\[
\begin{aligned}&\|PBP\|_{\mathrm F}^2+\|QA_1Q\|_{\mathrm F}^2\\&\quad\le\langle A_1,B\rangle .\end{aligned}\tag{2.3}
\]

*The remaining terms.* For \(s\ge2\) we have \(P_s=P_sQ=QP_s\), so \(P_sA_zP_s=P_s(QA_zQ)P_s\), and the inequality of the induction hypothesis displayed above bounds these terms. For distinct \(j,j'\ge2\),
\[
\begin{aligned}&\langle QA_jQ,QA_{j'}Q\rangle\\&\quad=\operatorname{tr}(A_jQA_{j'}Q)=\|A_j^{1/2}QA_{j'}^{1/2}\|_{\mathrm F}^2\\&\quad\le2\|A_j^{1/2}A_{j'}^{1/2}\|_{\mathrm F}^2\\&\qquad+2\|A_j^{1/2}PA_{j'}^{1/2}\|_{\mathrm F}^2\\&\quad=2\langle A_j,A_{j'}\rangle+2\langle PA_jP,PA_{j'}P\rangle ,\end{aligned}
\]
by \(Q=I-P\) and \(\|X-Y\|_{\mathrm F}^2\le2\|X\|_{\mathrm F}^2+2\|Y\|_{\mathrm F}^2\). As all \(\langle PA_jP,PA_{j'}P\rangle\) are nonnegative,
\[
\begin{aligned}\sum_{\substack{j\ne j'\\ j,j'\ge2}}\langle PA_jP,PA_{j'}P\rangle&\le\|PBP\|_{\mathrm F}^2\\&\le\langle A_1,B\rangle ,\end{aligned}
\]
the last step by (2.3).

*Collecting.* The left side of (2.1) is at most
\[
\begin{aligned}&(1+2C_{L-1})\langle A_1,B\rangle\\&\quad+2C_{L-1}\sum_{\substack{j\ne j'\\ j,j'\ge2}}\langle A_j,A_{j'}\rangle .\end{aligned}
\]
The full sum on the right of (2.1) is \(2\langle A_1,B\rangle+\sum_{j\ne j',\,j,j'\ge2}\langle A_j,A_{j'}\rangle\). Since \(C_{L-1}\ge1\), we have \(1+2C_{L-1}\le2C_{L-1}\cdot2\), so the left side is at most \(2C_{L-1}\) times that sum. With \(C_L=2C_{L-1}\) and \(C_1=1\), this proves (2.1) with \(C_L=2^{L-1}\). \(\square\)

The constant \(C_L\) grows quickly with \(L\), but it does not depend on the dimension of \(E\). In the application, \(L=2^{d-1}\) is fixed while the dimension grows with \(n\).

## 3. Exercises

**3.1.** Show that for \(L=2\) the projections \(P_1=P\), \(P_2=Q\) of Lemma 1.2, applied to \(A=A_1\) and \(B=A_2\), satisfy (2.1) with the constant \(\tfrac12\) in place of \(C_2\).

**3.2.** In \(\mathbb R^2\) let \(A_1=e_1e_1^{\mathsf T}\) and \(A_2=uu^{\mathsf T}\) with \(u=(\cos\varphi,\sin\varphi)\), \(0<\varphi<\pi/2\). Compute \(\langle A_1,A_2\rangle\), the projection \(P\) of Lemma 1.2, and the two terms on the right of Lemma 1.2.

**3.3.** Show that if the ranges of \(A_1,\ldots,A_L\) are mutually orthogonal, there are projections as in Theorem 2.1 for which the left side of (2.1) vanishes.

**3.4.** Let \(P_1,\ldots,P_L\) be mutually orthogonal projections with sum \(I\). Show that \(\|X\|_{\mathrm F}^2=\sum_{s,t}\|P_sXP_t\|_{\mathrm F}^2\) for every operator \(X\), and deduce \(\|P_sXP_s\|_{\mathrm F}\le\|X\|_{\mathrm F}\).

**3.5.** Show that the left side of (2.1) is not changed if the \(A_z\) are replaced by \(UA_zU^{\mathsf T}\) and the \(P_s\) by \(UP_sU^{\mathsf T}\) for an orthogonal operator \(U\), and that the right side is not changed either.

## 4. Solutions

**3.1.** For \(L=2\) the left side of (2.1) is \(\|P_2A_1P_2\|_{\mathrm F}^2+\|P_1A_2P_1\|_{\mathrm F}^2\), that is \(\|QA_1Q\|_{\mathrm F}^2+\|PA_2P\|_{\mathrm F}^2\), which is at most \(\langle A_1,A_2\rangle\) by Lemma 1.2. The right side of (2.1) is \(C_2\cdot2\langle A_1,A_2\rangle\), so \(C_2=\tfrac12\) suffices.

**3.2.** \(\langle A_1,A_2\rangle=(e_1^{\mathsf T}u)^2=\cos^2\varphi\). A computation gives
\[
A_1-A_2=\sin\varphi\begin{pmatrix}\sin\varphi&-\cos\varphi\\ -\cos\varphi&-\sin\varphi\end{pmatrix},
\]
and the last matrix is the reflection in the line spanned by \(p=(\cos\psi,\sin\psi)\) with \(\psi=\varphi/2-\pi/4\), because \(\cos2\psi=\sin\varphi\) and \(\sin2\psi=-\cos\varphi\). So \(A_1-A_2\) has the eigenvalues \(\pm\sin\varphi\), \(P=pp^{\mathsf T}\), and \(Q=qq^{\mathsf T}\) with \(q=(-\sin\psi,\cos\psi)\). Then \(\|PA_2P\|_{\mathrm F}^2=(p^{\mathsf T}u)^4=\cos^4(\varphi/2+\pi/4)\) and \(\|QA_1Q\|_{\mathrm F}^2=(q^{\mathsf T}e_1)^4=\sin^4(\varphi/2-\pi/4)\). Both equal \(\bigl(\tfrac{1-\sin\varphi}2\bigr)^2\), and their sum \(\tfrac12(1-\sin\varphi)^2\) is at most \(\cos^2\varphi=(1-\sin\varphi)(1+\sin\varphi)\).

**3.3.** Let \(P_s\) be the orthogonal projection onto the range of \(A_s\) for \(s\ge2\), and \(P_1=I-\sum_{s\ge2}P_s\), which contains the range of \(A_1\). These are mutually orthogonal projections with sum \(I\). For \(s\ne z\), the range of \(A_z\) is orthogonal to the range of \(P_s\), so \(P_sA_z=0\) and every term on the left vanishes.

**3.4.** The operators \(P_sXP_t\) are mutually orthogonal for the trace inner product, by the computation in the proof of Lemma 1.1, and their sum is \(X\). The norm identity follows, and dropping all terms except one gives the inequality.

**3.5.** We have
\[
\begin{aligned}&\|UP_sU^{\mathsf T}\,UA_zU^{\mathsf T}\,UP_sU^{\mathsf T}\|_{\mathrm F}\\&\quad=\|U(P_sA_zP_s)U^{\mathsf T}\|_{\mathrm F}=\|P_sA_zP_s\|_{\mathrm F},\end{aligned}
\]
and \(\langle UA_zU^{\mathsf T},UA_{z'}U^{\mathsf T}\rangle=\operatorname{tr}(UA_zA_{z'}U^{\mathsf T})\), which is \(\langle A_z,A_{z'}\rangle\). The new projections are again mutually orthogonal with sum \(I\).

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
