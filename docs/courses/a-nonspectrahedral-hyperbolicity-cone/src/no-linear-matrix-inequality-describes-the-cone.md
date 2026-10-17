# No linear matrix inequality describes the cone

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the second half of Theorem A of Hyperbolic polynomials and spectrahedral cones. Suppose some linear matrix inequality \(L(X,Z,y)\succeq0\) of finite size describes the hyperbolicity cone \(K\). The slices of [A positive map and a hyperbolic polynomial](a-positive-map-and-a-hyperbolic-polynomial.md) force \(L\), after a normalization and a limit, into a Schur-complement form. Letting \(X^{-1}\) and \(Z^{-1}\) tend to rank-one projections turns it into an identity between the Choi–Lam form and the norms of certain matrices. Differentiating that identity produces a nonzero bilinear form whose square lies below \(b\), which [The Choi–Lam form](the-choi-lam-form.md) excludes. The proof follows OpenAI [OpenAI-NS, Sections 4 to 6]. It never compares the determinant of the pencil with \(p\).

Throughout, \(\|\cdot\|_{\mathrm{op}}\) is the operator norm for the Euclidean norms, and for \(u\in\mathbf R^4\) we write \(u=(u_0,u')\) with \(u'\in\mathbf R^3\).

## 1. A pencil gives a Schur-complement inequality

**Proposition 4.1** (OpenAI). Suppose \(K=\{x:L(x)\succeq0\}\) for a linear map \(L:\mathbb S^4\times\mathbb S^4\times\mathbf R^3\to\mathbb S^N\). Then there are integers \(a,c\ge1\), unital positive linear maps \(D:\mathbb S^4\to\mathbb S^a\) and \(E:\mathbb S^4\to\mathbb S^c\), and a linear map \(B:\mathbf R^3\to\mathbf R^{a\times c}\) such that for all \(X\succ0\), \(Z\in\mathbb S^4\) and \(y\in\mathbf R^3\),
\[
\begin{aligned}
&Z\succeq\Phi_y(X^{-1})\\
&\quad\iff E(Z)\succeq B(y)^{\mathsf T}D(X)^{-1}B(y).
\end{aligned}
\]

*Proof.* Write \(L(X,Z,y)=L_1(X)+L_2(Z)+L_3(y)\).

*Removing a common kernel.* Since \(e\) is an interior point of \(K\) (Proposition 3.3), for every \(x\) there is \(\varepsilon>0\) with \(e\pm\varepsilon x\in K\), so \(L(e)\pm\varepsilon L(x)\succeq0\), and \(\ker L(e)\subseteq\ker L(x)\) by Lemma 1.3(6) of the first lesson. A symmetric matrix maps into the orthogonal complement of its kernel. So in an orthonormal basis adapted to \(V\oplus\ker L(e)\), \(V=\ker L(e)^\perp\), every \(L(x)\) is block diagonal with lower block \(0\), and replacing \(L(x)\) by its upper block \(L_V(x)\) does not change the set \(\{x:L(x)\succeq0\}\). Moreover \(L_V(e)\succ0\). The space \(V\) is nonzero: otherwise \(L=0\) and \(K\) would be the whole space, while \((-I_4,I_4,0)\notin K\) by Proposition 3.3. We may therefore assume \(L(e)\succ0\).

*Splitting off a block.* By the second slice of Proposition 3.3, \((X,0,0)\in K\) and \((0,Z,0)\in K\) whenever \(X,Z\succeq0\); so \(L_1\) and \(L_2\) are positive maps. Let \(U=\ker L_1(I_4)\). For every \(X\in\mathbb S^4\) and small \(\varepsilon>0\), \(I_4\pm\varepsilon X\succeq0\), so \(L_1(I_4)\pm\varepsilon L_1(X)\succeq0\), and \(U\subseteq\ker L_1(X)\). In an orthonormal basis adapted to \(U^\perp\oplus U\),
\[
L_1(X)=\begin{pmatrix}D(X)&0\\0&0\end{pmatrix}.
\]
Both summands are nonzero. If \(U^\perp=0\), then \(L_1=0\) and \(L(-I_4,I_4,0)=L_2(I_4)\succeq0\), so \((-I_4,I_4,0)\in K\), which is false. If \(U=0\), then \(L_1(I_4)\succ0\), so \(L_1(I_4)-\varepsilon L_2(I_4)\succ0\) for small \(\varepsilon>0\), and \((I_4,-\varepsilon I_4,0)\in K\), which is false. Let \(a=\dim U^\perp\), \(c=\dim U\), and let \(E(Z)\) be the lower diagonal block of \(L_2(Z)\). The maps \(D\) and \(E\) are positive, as compressions of positive maps. \(D(I_4)\succ0\) by the choice of \(U\), and \(E(I_4)\succ0\) because it is the compression of \(L(e)=L_1(I_4)+L_2(I_4)\succ0\) to \(U\). Replacing \(L\) by \(S^{\mathsf T}LS\) with \(S=\operatorname{diag}(D(I_4)^{-1/2},E(I_4)^{-1/2})\) does not change the described set (Lemma 1.3(4) of the first lesson) and makes \(D(I_4)=I_a\) and \(E(I_4)=I_c\). Write
\[
\begin{aligned}
L_2(Z)&=\begin{pmatrix}F(Z)&C(Z)\\ C(Z)^{\mathsf T}&E(Z)\end{pmatrix},\\
L_3(y)&=\begin{pmatrix}A(y)&B(y)\\ B(y)^{\mathsf T}&G(y)\end{pmatrix}.
\end{aligned}
\]

*The block \(G\) vanishes.* Fix \(y\) and put \(Z_0=\Phi_y(I_4)\). For every real \(s\), \(\Phi_{sy}(I_4)=s^2Z_0\), so \((I_4,s^2Z_0,sy)\in K\) by the first slice of Proposition 3.3. The lower block of \(L(I_4,s^2Z_0,sy)\) is \(s^2E(Z_0)+sG(y)\), and it is positive semidefinite, as a compression of a positive semidefinite matrix. Dividing by \(|s|\) and letting \(s\to0\) through positive and through negative values gives \(G(y)\succeq0\) and \(-G(y)\succeq0\), so \(G(y)=0\).

*Rescaling.* Let \(X\succ0\), \(Z\in\mathbb S^4\), \(y\in\mathbf R^3\) and \(s\ne0\). Conjugating \(L(X,s^2Z,sy)\) by \(\operatorname{diag}(I_a,s^{-1}I_c)\) gives
\[
\begin{aligned}
M_s&=\begin{pmatrix}D_s&B_s\\ B_s^{\mathsf T}&E(Z)\end{pmatrix},\\
D_s&=D(X)+sA(y)+s^2F(Z),\\
B_s&=B(y)+sC(Z).
\end{aligned}
\]
As \(\Phi_{sy}=s^2\Phi_y\), the first slice gives \((X,s^2Z,sy)\in K\) if and only if \(Z\succeq\Phi_y(X^{-1})\). Hence, for every \(s\ne0\),
\[
M_s\succeq0\iff Z\succeq\Phi_y(X^{-1}).
\]
As \(s\to0\), \(M_s\) tends to
\[
M=\begin{pmatrix}D(X)&B(y)\\B(y)^{\mathsf T}&E(Z)\end{pmatrix}.
\]
If \(Z\succeq\Phi_y(X^{-1})\), all \(M_s\) are positive semidefinite, and so is their limit \(M\).

*The converse.* Suppose \(M\succeq0\). Since \(X\succeq\lambda_{\min}(X)I_4\) and \(D\) is positive and unital, \(D(X)\succeq\lambda_{\min}(X)I_a\succ0\). For \(\delta>0\), the matrix \(M+\operatorname{diag}(0,\delta I_c)\), which is the limit matrix for \(Z+\delta I_4\), is positive definite: on a vector \((w_1,w_2)\ne0\) its quadratic form is at least \(\delta\|w_2\|^2\), and equals \(w_1^{\mathsf T}D(X)w_1>0\) when \(w_2=0\). Positive definite matrices form an open set, so the matrices \(M_s\) formed with \(Z+\delta I_4\) are positive definite for small \(s\ne0\), and the equivalence for \(M_s\) gives \(Z+\delta I_4\succeq\Phi_y(X^{-1})\). Letting \(\delta\to0\) gives \(Z\succeq\Phi_y(X^{-1})\).

So \(Z\succeq\Phi_y(X^{-1})\) if and only if \(M\succeq0\), and by the Schur complement, Lemma 1.3(5) of the first lesson with \(P=D(X)\succ0\), if and only if \(E(Z)\succeq B(y)^{\mathsf T}D(X)^{-1}B(y)\). \(\square\)

## 2. Rank-one limits and a norm identity

For unit vectors \(u,v\in\mathbf R^4\) let \(P(v)\) be the orthogonal projection of \(\mathbf R^a\) onto \(\ker D(I_4-vv^{\mathsf T})\), and \(R(u)\) that of \(\mathbf R^c\) onto \(\ker E(I_4-uu^{\mathsf T})\).

**Lemma 4.2.** If \(H\in\mathbb S^n\) is positive semidefinite, then \([I+(t-1)H]^{-1/2}\) tends, as \(t\to\infty\), in operator norm to the orthogonal projection onto \(\ker H\).

*Proof.* In an orthonormal basis of eigenvectors of \(H\), with eigenvalues \(\mu\ge0\), the matrix is diagonal with entries \((1+(t-1)\mu)^{-1/2}\), which equal \(1\) for \(\mu=0\) and tend to \(0\) for \(\mu>0\). \(\square\)

**Proposition 4.3** (OpenAI). Under the conclusion of Proposition 4.1, for all unit vectors \(u,v\in\mathbf R^4\) and all \(y\in\mathbf R^3\),
\[
\begin{aligned}
&b(v_0u'-u_0v',\,y)\\
&\quad=\bigl\|P(v)B(y)R(u)\bigr\|_{\mathrm{op}}^2 .
\end{aligned}
\tag{4.3}
\]

*Proof.* For \(t\ge1\) put \(X_t=vv^{\mathsf T}+t(I-vv^{\mathsf T})\) and \(Z_t=uu^{\mathsf T}+t(I-uu^{\mathsf T})\). Their eigenvalues are \(1\) and \(t\), so \(X_t,Z_t\succeq I\), and positivity and unitality give \(D(X_t)\succeq I_a\) and \(E(Z_t)\succeq I_c\). Put
\[
\begin{aligned}
A_t&=Z_t^{-1/2}\,\Phi_y(X_t^{-1})\,Z_t^{-1/2}\succeq0,\\
C_t&=D(X_t)^{-1/2}\,B(y)\,E(Z_t)^{-1/2}.
\end{aligned}
\]
For real \(r\), congruence by \(Z_t^{-1/2}\) and Lemma 1.3(3) of the first lesson give: \(rZ_t\succeq\Phi_y(X_t^{-1})\) if and only if \(r\ge\lambda_{\max}(A_t)\). Congruence by \(E(Z_t)^{-1/2}\) and Lemma 1.3(7) give: \(E(rZ_t)\succeq B(y)^{\mathsf T}D(X_t)^{-1}B(y)\) if and only if \(r\ge\|C_t\|_{\mathrm{op}}^2\). By the equivalence of Proposition 4.1 for \((X_t,rZ_t,y)\), these two sets of \(r\) coincide, so
\[
\lambda_{\max}(A_t)=\|C_t\|_{\mathrm{op}}^2 .
\]
Let \(t\to\infty\). Since \(X_t^{-1}=vv^{\mathsf T}+t^{-1}(I-vv^{\mathsf T})\) and \(Z_t^{-1/2}=uu^{\mathsf T}+t^{-1/2}(I-uu^{\mathsf T})\),
\[
A_t\to uu^{\mathsf T}\,\Phi_y(vv^{\mathsf T})\,uu^{\mathsf T}=\alpha\,uu^{\mathsf T}
\]
with \(\alpha=u^{\mathsf T}\Phi_y(vv^{\mathsf T})u\ge0\), and \(\lambda_{\max}(A_t)\to\alpha\) by the continuity in Lemma 1.3(3). On the other side, unitality gives \(D(X_t)=I_a+(t-1)D(I-vv^{\mathsf T})\) and \(E(Z_t)=I_c+(t-1)E(I-uu^{\mathsf T})\), with \(D(I-vv^{\mathsf T})\succeq0\) and \(E(I-uu^{\mathsf T})\succeq0\). By Lemma 4.2, \(D(X_t)^{-1/2}\to P(v)\) and \(E(Z_t)^{-1/2}\to R(u)\), so \(C_t\to P(v)B(y)R(u)\), and \(\|C_t\|_{\mathrm{op}}^2\) tends to the right side of (4.3). By Lemma 3.1 of the previous lesson, \(\alpha=b(v_0u'-u_0v',y)\). \(\square\)

At \(u=v\) the left side of (4.3) is \(b(0,y)=0\), so for every \(y\in\mathbf R^3\)
\[
P(v)B(y)R(v)=0 .
\tag{4.4}
\]

## 3. The tangent obstruction

*Proof of Theorem A.* Proposition 3.2 of the previous lesson proves that \(p\) is homogeneous of degree \(20\), with \(p(e)=1\), and hyperbolic with respect to \(e\). Suppose \(K\) is described by a linear matrix inequality of some finite size, and let \(D,E,B\) be given by Proposition 4.1.

*A point where \(R\) is smooth.* Let \(S^3\) be the unit sphere of \(\mathbf R^4\) and \(\Omega=\{u\in S^3:u_0\ne0\}\). The matrices \(A(u)=E(I-uu^{\mathsf T})\), \(u\in\Omega\), have finitely many possible ranks; let \(\rho\) be the largest, attained at some \(v\in\Omega\). If \(\rho=0\), then \(R(u)=I\) on \(\Omega\). If \(\rho>0\), choose \(\rho\) linearly independent columns of \(A(v)\), and let \(W(u)\) be the matrix formed by the same columns of \(A(u)\). A \(\rho\times\rho\) minor of \(W\) is nonzero at \(v\), hence on a neighbourhood \(\mathcal U\) of \(v\) in \(\mathbf R^4\). For \(u\in\mathcal U\cap\Omega\), the columns of \(W(u)\) are independent and lie in the range of \(A(u)\), which has dimension at most \(\rho\); so they span it. As \(A(u)\) is symmetric, its kernel is the orthogonal complement of its range, and for \(u\in\mathcal U\cap\Omega\)
\[
\begin{aligned}
R(u)&=I-W(W^{\mathsf T}W)^{-1}W^{\mathsf T},\\
W&=W(u).
\end{aligned}
\]
The right side is a smooth function of \(u\in\mathcal U\); write \(dR_v\) for its differential at \(v\), a linear map from \(\mathbf R^4\) to matrices.

*Differentiating the identity.* For \(h=(h_0,h')\in v^\perp\) put
\[
\begin{aligned}
Jh&=v_0h'-h_0v',\\
u_s&=\frac{v+sh}{\sqrt{1+s^2\|h\|^2}} .
\end{aligned}
\]
For small \(s\), \(u_s\in\mathcal U\cap\Omega\), and
\[
v_0u_s'-(u_s)_0v'=\frac{s\,Jh}{\sqrt{1+s^2\|h\|^2}} .
\]
By (4.3) at the pair \((u_s,v)\), (4.4) and the homogeneity of \(b\) of degree \(2\) in its first argument, for \(s\ne0\),
\[
\begin{aligned}
&\frac{b(Jh,y)}{1+s^2\|h\|^2}\\
&\quad=\Bigl\|P(v)B(y)\,\frac{R(u_s)-R(v)}{s}\Bigr\|_{\mathrm{op}}^2 .
\end{aligned}
\]
As \(s\to0\), the difference quotient tends to \(dR_v(h)\), since \(u_s\) has velocity \(h\) at \(s=0\). Therefore, for all \(h\in v^\perp\) and \(y\in\mathbf R^3\),
\[
b(Jh,y)=\bigl\|P(v)B(y)\,dR_v(h)\bigr\|_{\mathrm{op}}^2 .
\]
We call this the *tangent identity*.

*The contradiction.* The linear map \(J:v^\perp\to\mathbf R^3\) is an isomorphism: if \(Jh=0\), then \(h'=(h_0/v_0)v'\), because \(v_0\ne0\), so \(h=(h_0/v_0)v\), and \(h\perp v\) forces \(h=0\); both spaces have dimension \(3\). The matrix
\[
F(z,y)=P(v)B(y)\,dR_v(J^{-1}z),
\]
defined for \(z,y\in\mathbf R^3\), depends bilinearly on \((z,y)\). In orthonormal bases each entry \(\ell_{ij}(z,y)\) is a bilinear form, and by the tangent identity with \(z=Jh\),
\[
\ell_{ij}(z,y)^2\le\|F(z,y)\|_{\mathrm{op}}^2=b(z,y).
\]
By Lemma 2.3 of [The Choi–Lam form](the-choi-lam-form.md), every \(\ell_{ij}\) vanishes, so \(F=0\), and the tangent identity gives \(b=0\), contradicting \(b(e_1,e_1)=1\). Hence no linear matrix inequality describes \(K\). \(\square\)

The proof uses four properties of the construction: the two slices of the cone, the positivity of \(\Phi_y\), the rank-one identity of Lemma 3.1, and the absence of dominated bilinear squares below \(b\). Replacing \(b\) by a form that dominates a nonzero bilinear square breaks only the last step (Exercise 4.3).

## 4. Exercises

**4.1** (easy). Where does the proof use that \(v_0\ne0\)? What goes wrong at a point \(v\) with \(v_0=0\)?

**4.2** (medium). For \(H\succeq0\) with least positive eigenvalue \(\mu\), show that the distance in operator norm between \([I+(t-1)H]^{-1/2}\) and the projection onto \(\ker H\) is \((1+(t-1)\mu)^{-1/2}\).

**4.3** (medium). Replace \(Q(y)\) by \(\|y\|^2I_3\), so that \(b\) becomes \(\|z\|^2\|y\|^2\). Show that \(\ell(z,y)=z_1y_1\) satisfies \(\ell^2\le\|z\|^2\|y\|^2\), so that the last step of the proof fails for the modified polynomial.

**4.4** (easy). Show that conjugating a pencil \(L\) by a fixed invertible matrix \(S\), \(x\mapsto S^{\mathsf T}L(x)S\), does not change the set \(\{x:L(x)\succeq0\}\).

## 5. Solutions

**4.1.** Only in showing that \(J\) is injective. If \(v_0=0\), then \(\|v'\|=1\) and \(Jh=-h_0v'\) for \(h\in v^\perp\). So \(J\) maps \(v^\perp\) onto the line \(\mathbf Rv'\), its kernel consists of the vectors \((0,w)\) with \(w\perp v'\), and the tangent identity controls \(b(z,y)\) only for \(z\) in the line \(\mathbf Rv'\).

**4.2.** In an eigenbasis the difference is diagonal with entries \(0\) on \(\ker H\) and \((1+(t-1)\mu')^{-1/2}\) for the positive eigenvalues \(\mu'\); the largest is at \(\mu'=\mu\).

**4.3.** By the Cauchy–Schwarz inequality, \(z_1^2y_1^2\le\|z\|^2\|y\|^2\). In the proof, the entries \(\ell_{ij}\) need not vanish, so no contradiction arises.

**4.4.** \(S^{\mathsf T}L(x)S\succeq0\) if and only if \(L(x)\succeq0\), by Lemma 1.3(4) of the first lesson.

## References

- [OpenAI-NS] OpenAI, *A nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 24 September 2026, Sections 4–6. https://github.com/openai/math/tree/main/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026
