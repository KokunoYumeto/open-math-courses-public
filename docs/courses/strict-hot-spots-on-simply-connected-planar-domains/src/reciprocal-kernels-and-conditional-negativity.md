# Reciprocal kernels and conditional negativity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the kernel theorem behind the hot-spots theorem: for every interior point \(p\) of the disc, the kernel \(K(p,s)K(p,t)/N(s,t)\) on the circle is conditionally negative semidefinite. The kernels \(K\) and \(N\) are those of [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md), built from any bounded nonnegative potential satisfying the subcritical inequality (2.1) there. The proof works with matrices that have at most one positive eigenvalue: it regularizes the Green function of the disc, adds integration nodes one at a time by rank-one updates, and passes to the singular kernel and then to the boundary by monotone limits.

- Matrices with at most one positive eigenvalue (Section 1).
- The theorem (Section 2).
- A bounded regularization of the Green function (Section 3).
- A rank-one update (Section 4).
- The interior resolvent kernel (Section 5).
- The boundary limit and the proof of the theorem (Section 6).

All matrices in this lesson are real and symmetric, and the *reciprocal* of a matrix with nonzero entries is always taken entrywise, never as a matrix inverse.

## 1. Matrices with at most one positive eigenvalue

A real symmetric matrix has *property (P)* if it has at most one positive eigenvalue, counted with multiplicity. A subspace \(W\) is *positive* for \(M\) if \(x^TMx>0\) for all \(0\ne x\in W\).

**Lemma 1.1.**

1. \(M\) has (P) if and only if no two-dimensional subspace is positive for \(M\).
2. Property (P) is preserved by congruence \(M\mapsto S^TMS\) with \(S\) invertible (in particular by positive diagonal congruence), by subtracting a positive semidefinite matrix, by passing to a principal submatrix, and by limits of matrices of a fixed size.
3. If \(v\) is a vector and \(U\) is positive semidefinite, then \(vv^T-U\) has (P).

*Proof.* (1) Two orthonormal eigenvectors for positive eigenvalues span a positive plane. Conversely, if \(M\) has at most one positive eigenvalue and \(W\) is a positive plane, then \(W\) meets the orthogonal complement of the eigenvector of that eigenvalue (or the whole space, if there is none) in a nonzero vector \(x\), and \(x^TMx\le0\) because \(x\) is a combination of eigenvectors with eigenvalues \(\le0\).

(2) \(W\) is positive for \(S^TMS\) if and only if \(SW\) is positive for \(M\). A plane positive for \(M-U\) is positive for \(M\). A plane positive for a principal submatrix, extended by zeros, is positive for \(M\). If \(W\) is a positive plane for \(M\), then \(x^TMx\ge c>0\) on the unit circle of \(W\), so \(W\) is positive for every matrix close to \(M\).

(3) Every plane contains \(x\ne0\) with \(v^Tx=0\), and \(x^T(vv^T-U)x=-x^TUx\le0\). \(\square\)

**Lemma 1.2** (Schur products). If \(A\) and \(B\) are positive semidefinite (real symmetric, or complex Hermitian), so is the entrywise product \(A\circ B\). Hence entrywise powers \(A^{\circ n}\) and convergent series \(\sum_nc_nA^{\circ n}\) with \(c_n\ge0\) are positive semidefinite, and a real symmetric matrix that is positive semidefinite as a Hermitian matrix is positive semidefinite.

*Proof.* By the spectral theorem \(A_{ij}=\langle a_i,a_j\rangle\) and \(B_{ij}=\langle b_i,b_j\rangle\) for vectors \(a_i,b_i\). Then \((A\circ B)_{ij}=\langle a_i\otimes b_i,a_j\otimes b_j\rangle\) is a Gram matrix. The last statement holds because \(x^TAx=x^*Ax\) for real \(x\). \(\square\)

## 2. The theorem

A real symmetric kernel \(D\) on a set, with zero diagonal, is *conditionally negative semidefinite* if
\[
\sum_{i,j}a_ia_jD(s_i,s_j)\le0
\]
for every finite family of points \(s_i\) and real \(a_i\) with \(\sum_ia_i=0\).

**Theorem 2.1** ([OpenAI-HS, Theorem 5.1]). Let \(dq=a\,dx\) on \(\mathbb D\) with \(a\in L^\infty(\mathbb D)\), \(a\ge0\), and suppose that for some \(0<d<1\)
\[
\begin{gathered}
\int_{\mathbb D}|\psi|^2\,dq\le d\int_{\mathbb D}|\nabla\psi|^2\\
(\psi\in H^1_0(\mathbb D)).
\end{gathered}
\]
For the associated kernels \(K,N\) and every \(p\in\mathbb D\), the kernel
\[
\begin{gathered}
D_p(s,t)=\frac{K(p,s)K(p,t)}{N(s,t)}\quad(s\ne t),\\
D_p(s,s)=0,
\end{gathered}
\]
is conditionally negative semidefinite on \(\mathbb S^1\).

**Remark 2.2** ([OpenAI-HS, Remark 5.2]). For \(q=0\), \(K(p,s)=P_s(p)\) and \(N=N_0\). With the disc automorphism \(\varphi_p(z)=(z-p)/(1-\bar pz)\),
\[
\begin{gathered}
\varphi_p(s)-\varphi_p(t)=\frac{(s-t)(1-|p|^2)}{(1-\bar ps)(1-\bar pt)},\\
|1-\bar ps|=|s-p|\quad(s\in\mathbb S^1),
\end{gathered}
\]
so \(D_p(s,t)=\pi P_s(p)P_t(p)|s-t|^2\), which equals \(\frac1{4\pi}|\varphi_p(s)-\varphi_p(t)|^2\), a multiple of a squared Euclidean distance. Such kernels are conditionally negative semidefinite: if \(\sum a_i=0\), then \(\sum_{i,j}a_ia_j|x_i-x_j|^2=-2|\sum_ia_ix_i|^2\). Theorem 2.1 says that a squared-distance description survives the addition of a subcritical potential; the last lesson realizes \(D_p\) as a squared distance in a Hilbert space.

The matrix condition behind the proof has a classical meaning. For a positive definite kernel \(k\) whose values never vanish, the condition that every finite matrix \((1/k(x_i,x_j))\) has exactly one positive eigenvalue characterizes the complete Nevanlinna–Pick property; this is the McCullough–Quiggin theorem [AM00, Corollary 1.12]. The arguments below are self-contained.

The fixed point \(p\) links (P) to conditional negativity. Adjoining \(p\) to boundary points gives a bordered reciprocal matrix with zero diagonal, boundary block \(1/N(s_i,s_j)\) and border \(1/K(p,s_i)\) (Lemma 6.1); property (P) of that matrix is exactly what the theorem needs. The bordered matrix is reached through four limits: refinement of a quadrature for a regularized kernel with a compactly supported potential \(\rho\le q\); removal of the regularization; radial passage of evaluation points to the circle; and increase of \(\rho\) to \(q\).

## 3. A bounded regularization of the Green function

For \(x,y\in\mathbb D\) put
\[
\begin{gathered}
h(x,y)=\frac{|x-y|^2}{(1-|x|^2)(1-|y|^2)},\\
L(h)=\frac1{\log(1+1/h)}\ (h>0),\\
L(0)=0,
\end{gathered}
\]
and \(f(h)=h+\frac12-L(h)\). By the second formula for \(G\) in Section 1 of the previous lesson, \(G=\frac1{4\pi}\log(1+1/h)\), so \(1/G(x,y)=4\pi L(h(x,y))\), with value \(0\) on the diagonal.

**Lemma 3.1** ([OpenAI-HS, Lemma 5.3]). There are bounded continuous strictly positive kernels \(C_\varepsilon\) on \(\mathbb D\times\mathbb D\), \(0<\varepsilon\le1\), such that \(C_\varepsilon\le G\), \(C_\varepsilon\uparrow G\) as \(\varepsilon\downarrow0\) (also on the diagonal), and every finite matrix \((1/C_\varepsilon(x_i,x_j))\) has (P).

*Proof.* *The kernel \(h+\frac12\) has (P).* Multiplying the \(x\)- and \(y\)-entries by \(1-|x|^2\) and \(1-|y|^2\) turns \(h+\frac12\) into
\[
\tfrac12(1+|x|^2)(1+|y|^2)-2\,x\cdot y,
\]
a rank-one positive kernel minus a Gram kernel; Lemma 1.1(3) and (2) apply.

*A formula for \(f\).* For \(h>0\),
\[
\begin{aligned}
&\int_0^1h^{1-\alpha}(h+1)^\alpha\,d\alpha\\
&\quad=h\Bigl[\frac{(1+1/h)^\alpha}{\log(1+1/h)}\Bigr]_0^1=L(h).
\end{aligned}
\] For \(0<\alpha<1\) let \(\mathbb E_\alpha\) be the expectation for the probability measure \(c_\alpha v^{\alpha-1}(1+v)^{-1}\,dv\) on \((0,\infty)\), and put \(r=1/(1+v)\in(0,1)\). Integration by parts gives
\[
\mathbb E_\alpha(1-r)=c_\alpha\int_0^\infty\frac{v^\alpha}{(1+v)^2}\,dv=\alpha .
\]
The substitution \(v=\frac{h+1}hw\) gives \(c_\alpha\int_0^\infty\frac{h(h+1)v^{\alpha-1}}{(h+1)+vh}\,dv=h^{1-\alpha}(h+1)^\alpha\). Since \((h+1)+vh=(h+r)/r\) and \(c_\alpha v^{\alpha-1}dv=(1+v)\cdot c_\alpha v^{\alpha-1}(1+v)^{-1}dv\),
\[
\begin{aligned}
&h^{1-\alpha}(h+1)^\alpha=\mathbb E_\alpha\frac{h(h+1)}{h+r}\\
&\quad=\mathbb E_\alpha\Bigl[h+(1-r)-\frac{r(1-r)}{h+r}\Bigr],
\end{aligned}
\]
and this also holds at \(h=0\), where both sides vanish. Integrating over \(\alpha\in(0,1)\),
\[
\begin{gathered}
f(h)=\int_0^1\mathbb E_\alpha\tfrac{r(1-r)}{h+r}\,d\alpha,\\
0\le f(h)\le f(0)=\tfrac12,
\end{gathered} \tag{3.1}
\]
because \(r(1-r)/(h+r)\le1-r\).

*The kernel \(f(h)\) is positive semidefinite.* The kernel
\[
\begin{aligned}
k(x,y)&=\frac1{1+h(x,y)}\\
&=\frac{(1-|x|^2)(1-|y|^2)}{|1-x\bar y|^2}
\end{aligned}
\]
is positive semidefinite: \((1-x\bar y)^{-1}=\sum_n x^n\bar y^n\) is a Gram kernel, and so is its product with its complex conjugate (Lemma 1.2), and with the factors \((1-|x|^2)(1-|y|^2)\). For fixed \(0<r<1\),
\[
\frac1{h+r}=\sum_{n\ge0}(1-r)^nk^{n+1}
\]
with entrywise powers, because \(\sum_n(1-r)^nk^{n+1}=k/(1-(1-r)k)\) and \(0<k\le1\). By Lemma 1.2 this is positive semidefinite, and so is the positive mixture (3.1).

*The kernels \(C_\varepsilon\).* Define
\[
\begin{aligned}
\frac1{C_\varepsilon}&=4\pi\Bigl[h+\frac12-(1-\varepsilon)f(h)\Bigr]\\
&=4\pi\bigl[L(h)+\varepsilon f(h)\bigr].
\end{aligned}
\]
Its finite matrices are a matrix with (P) minus a positive semidefinite one, so they have (P). Since \(L+\varepsilon f=\varepsilon(h+\frac12)+(1-\varepsilon)L\ge\varepsilon/2\), the kernel \(C_\varepsilon\) is bounded by \(1/(2\pi\varepsilon)\); it is continuous and positive. As \(\varepsilon\downarrow0\), \(1/C_\varepsilon\) decreases to \(4\pi L(h)=1/G\), so \(C_\varepsilon\le G\) and \(C_\varepsilon\uparrow G\); on the diagonal \(C_\varepsilon(x,x)=1/(2\pi\varepsilon)\uparrow\infty\). \(\square\)

## 4. A rank-one update

**Lemma 4.1** ([OpenAI-HS, Lemma 5.4]). Let \(M\) be a symmetric matrix with strictly positive entries whose reciprocal has (P). For every index \(z\) and every \(c\ge0\), the matrix
\[
\widetilde M_{ij}=M_{ij}+c\,M_{iz}M_{zj}
\]
also has a reciprocal with (P).

*Proof.* Congruence by the positive diagonal matrix \(\operatorname{diag}(M_{iz})\) turns the reciprocal of \(M\) into \(H_{ij}=M_{iz}M_{zj}/M_{ij}\), which has (P). Its \(z\)-th row and column are constant, equal to \(a=M_{zz}>0\). Order \(z\) last and let \(H_0\) be the remaining principal block. Subtracting the last row from the other rows, and the last column from the other columns, is a congruence:
\[
H\ \sim\ \begin{pmatrix}H_0-a\mathbf 1\mathbf 1^T&0\\0&a\end{pmatrix}.
\]
Since \(a>0\) and \(H\) has (P), the block \(H_0-a\mathbf 1\mathbf 1^T\) has no positive eigenvalue. So \(U=a\mathbf 1\mathbf 1^T-H\), whose \(z\)-th row and column vanish, is positive semidefinite. Since \(H_{ii}>0\), \(0\le U_{ii}<a\), and the Cauchy–Schwarz inequality for \(U\) gives \(|U_{ij}|<a\).

The same congruence turns the reciprocal of \(\widetilde M\) into the matrix with entries \(H_{ij}/(1+cH_{ij})\). With \(H_{ij}=a-U_{ij}\),
\[
\begin{aligned}
&\frac a{1+ca}-\frac{H_{ij}}{1+cH_{ij}}\\
&\quad=\frac{U_{ij}}{(1+ca)(1+ca-cU_{ij})}\\
&\quad=\sum_{n\ge0}\frac{c^nU_{ij}^{n+1}}{(1+ca)^{n+2}},
\end{aligned}
\]
the series converging because \(|cU_{ij}|<1+ca\). By Lemma 1.2 the right side is a positive semidefinite matrix, so the transformed reciprocal of \(\widetilde M\) is \(\frac a{1+ca}\mathbf 1\mathbf 1^T\) minus a positive semidefinite matrix, and it has (P) by Lemma 1.1. \(\square\)

## 5. The interior resolvent kernel

Let \(0\le\rho\le q\) be a measure supported in a compact subset of \(\mathbb D\), let \(T_\rho\) be its Green operator on \(L^2(\rho)\), with \(\|T_\rho\|\le d\) (Lemma 2.2 of the previous lesson), put \(S_\rho=(I-T_\rho)^{-1}\), and define for \(x\ne y\) in \(\mathbb D\)
\[
\begin{aligned}
&M^\rho(x,y)=G(x,y)\\
&\quad+\bigl\langle G(x,\cdot),S_\rho G(y,\cdot)\bigr\rangle_\rho,
\end{aligned} \tag{5.1}
\]
and \(M^\rho(x,x)=+\infty\). Expanding the Neumann series, \(M^\rho(x,y)\) is the sum over \(n\ge0\) of the nonnegative chain integrals
\[
\begin{aligned}
&\int\!\cdots\!\int G(x,z_1)G(z_1,z_2)\cdots G(z_n,y)\\
&\qquad d\rho(z_1)\cdots d\rho(z_n),
\end{aligned}
\]
and it is finite for \(x\ne y\): the correction is at most \(\|G(x,\cdot)\|_\rho\|G(y,\cdot)\|_\rho/(1-d)\).

**Proposition 5.1** ([OpenAI-HS, Proposition 5.5]). For distinct points \(x_1,\dots,x_m\in\mathbb D\), the matrix \((1/M^\rho(x_i,x_j))\), with zero diagonal, has (P).

*Proof.* *Step 1: regularization.* Fix \(\varepsilon\) and write \(C=C_\varepsilon\). Let \(M_C\) be defined by (5.1) with \(G\) replaced by \(C\) throughout, including in the operator: \(T_Cf(x)=\int C(x,z)f(z)\,d\rho(z)\). Since \(0<C\le G\), \(|T_Cf|\le T_\rho|f|\) pointwise, so \(\|T_C\|\le d\), and \(M_C(x,y)\) is the sum of the chain integrals of \(C\), finite for all \(x,y\).

*Step 2: quadrature.* Let \(Q\) be the support of \(\rho\). Partition it into finitely many Borel cells of diameter less than \(\eta\) and positive \(\rho\)-mass (cells of mass zero are discarded); choose a node \(z_\beta\) in each cell \(Q_\beta\), put \(w_\beta=\rho(Q_\beta)\), and let \(\pi(y)=z_\beta\) for \(y\in Q_\beta\). By uniform continuity of \(C\) on \(Q\times Q\), as \(\eta\to0\) the operators \(T_\pi\) with kernel \(C(\pi(\cdot),\pi(\cdot))\) converge to \(T_C\) in norm (the norm difference is at most \(\rho(\mathbb D)\sup|C(\pi(y),\pi(z))-C(y,z)|\)), and \(C(x,\pi(\cdot))\to C(x,\cdot)\) in \(L^2(\rho)\) for each \(x\). For fine partitions \(\|T_\pi\|<1\); with \(S_\pi=(I-T_\pi)^{-1}\) and \(c_x=C(x,\pi(\cdot))\in L^2(\rho)\),
\[
\begin{aligned}
&M_\pi(x,y)\\
&\quad=C(x,y)+\langle c_x,S_\pi c_y\rangle_\rho\\
&\quad\longrightarrow M_C(x,y).
\end{aligned} \tag{5.2}
\]
The functions \(e_\beta=\mathbf 1_{Q_\beta}/\sqrt{w_\beta}\) are orthonormal, \(T_\pi\) maps \(L^2(\rho)\) into their span and vanishes on its orthogonal complement, and its matrix there is \(\mathsf T_{\beta\gamma}=\sqrt{w_\beta}\,C(z_\beta,z_\gamma)\sqrt{w_\gamma}\). With \((\xi_x)_\beta=\sqrt{w_\beta}\,C(x,z_\beta)\), the correction in (5.2) equals \(\xi_x^T(I-\mathsf T)^{-1}\xi_y\), and \(\|\mathsf T\|<1\).

*Step 3: adding nodes one at a time.* Let \(S\) be the finite set consisting of the points \(x_i\) and the nodes \(z_\beta\). For a set \(A\) of nodes let \(M^A\) be the matrix on \(S\times S\) whose \((x,y)\) entry is the sum over all chains \(x,z_{\beta_1},\dots,z_{\beta_n},y\) (\(n\ge0\)) with internal nodes in \(A\) of
\[
C(x,z_{\beta_1})w_{\beta_1}C(z_{\beta_1},z_{\beta_2})\cdots w_{\beta_n}C(z_{\beta_n},y).
\]
For \(A\) the set of all nodes this is \(C(x,y)+\sum_{n\ge0}\xi_x^T\mathsf T^n\xi_y=M_\pi(x,y)\), which is finite; for smaller \(A\) the sum is a subseries, hence finite. For \(A=\emptyset\), \(M^A\) is the restriction of \(C\) to \(S\), whose reciprocal has (P) by Lemma 3.1. Add a node \(z\notin A\) of weight \(w\). The chains with exactly \(k\ge1\) internal occurrences of \(z\) contribute \(w^kM^A_{xz}(M^A_{zz})^{k-1}M^A_{zy}\); all factors are positive, and finiteness forces \(wM^A_{zz}<1\). Summing over \(k\),
\[
M^{A\cup\{z\}}_{xy}=M^A_{xy}+\frac w{1-wM^A_{zz}}\,M^A_{xz}M^A_{zy},
\]
so Lemma 4.1 propagates (P) of the reciprocal from \(M^A\) to \(M^{A\cup\{z\}}\). After all nodes are added, the reciprocal of \(M_\pi\) on \(S\) has (P), and so does its principal submatrix on the points \(x_i\).

*Step 4: the quadrature limit.* By (5.2) and Lemma 1.1(2), the reciprocal matrix of \(M_C\) at the points \(x_i\) has (P).

*Step 5: removing the regularization.* As \(\varepsilon\downarrow0\), each chain integral of \(C_\varepsilon\) increases to the corresponding chain integral of \(G\) by monotone convergence, and so do their sums. Off the diagonal the limit is \(M^\rho(x_i,x_j)<\infty\). On the diagonal \(M_{C_\varepsilon}(x_i,x_i)\ge C_\varepsilon(x_i,x_i)\), which is \(1/(2\pi\varepsilon)\to\infty\), so its reciprocal tends to \(0\). Lemma 1.1(2) gives the assertion. \(\square\)

## 6. The boundary limit and the proof of the theorem

For a compactly supported \(0\le\rho\le q\), let \(K^\rho\), \(R^\rho\), \(N^\rho=N_0+R^\rho\) be the kernels of Section 4 of the previous lesson built from \(\rho\).

**Lemma 6.1** ([OpenAI-HS, Lemma 5.6]). For distinct \(s_1,\dots,s_m\in\mathbb S^1\) and \(p\in\mathbb D\), the bordered matrix
\[
\begin{gathered}
\begin{pmatrix}B&\ell\\\ell^T&0\end{pmatrix},\qquad\ell_i=\frac1{K(p,s_i)},\\
B_{ij}=\begin{cases}1/N(s_i,s_j),&i\ne j,\\0,&i=j,\end{cases}
\end{gathered}
\]
has (P).

*Proof.* Fix a compactly supported \(0\le\rho\le q\). For \(|p|<r<1\), apply Proposition 5.1 to the distinct points \(rs_1,\dots,rs_m,p\). From the second formula for \(G\),
\[
\begin{gathered}
\frac{G(rs,x)}{1-r}\longrightarrow P_s(x),\\
\frac{G(rs,rt)}{(1-r)^2}\longrightarrow N_0(s,t)\quad(s\ne t),
\end{gathered}
\]
as \(r\uparrow1\), the first uniformly for \(x\) in compact subsets of \(\mathbb D\); for the second use \(G(rs,rt)=\frac1{4\pi}\log\bigl(1+\frac{(1-r^2)^2}{r^2|s-t|^2}\bigr)\). On the support of \(\rho\) these convergences are uniform and \(P_s\) is bounded. Expanding \((I-T_\rho)^{-1}\) in (5.1), and using \(R^\rho(s,t)=\sum_n\langle P_s,T_\rho^nP_t\rangle_\rho\) and \(\langle G(p,\cdot),T_\rho^nP_s\rangle_\rho=(T_\rho^{n+1}P_s)(p)\), we get
\[
\begin{gathered}
\frac{M^\rho(rs_i,rs_j)}{(1-r)^2}\to N^\rho(s_i,s_j)\quad(i\ne j),\\
\frac{M^\rho(p,rs_i)}{1-r}\to K^\rho(p,s_i).
\end{gathered}
\]
Congruence by the diagonal matrix with entries \(1-r\) at the moving points and \(1\) at \(p\) turns the reciprocal matrix of Proposition 5.1 into a matrix converging to the bordered matrix built from \(K^\rho\), \(N^\rho\); the zero diagonal stays zero. By Lemma 1.1(2), that bordered matrix has (P).

Now let \(\rho_n=\mathbf 1_{\{|x|\le r_n\}}q\) with \(r_n\uparrow1\). Every term of \(K^{\rho_n}\) and \(R^{\rho_n}\) is a chain integral of nonnegative functions, so by monotone convergence \(K^{\rho_n}(p,s)\uparrow K(p,s)\) and \(N^{\rho_n}(s,t)\uparrow N(s,t)\) for \(s\ne t\). The limits are finite (Lemma 4.1 of the previous lesson), so the bordered matrices converge, and Lemma 1.1(2) concludes. No boundary value of a Poisson kernel in \(L^2(q)\) has been used: the boundary passage is made for the compactly supported \(\rho\). \(\square\)

*Proof of Theorem 2.1.* Let \(\mathcal B\) be the bordered matrix of Lemma 6.1. First, \(x^TBx\le0\) whenever \(\ell^Tx=0\). Otherwise, choose \(y\) with \(\ell^Ty\ne0\) (possible since \(\ell\ne0\)) and replace it by \(y-\frac{x^TBy}{x^TBx}x\); then \(x^TBy=0\) and still \(\ell^Ty\ne0\). The vectors \((x,0)\) and \((y,c)\) are \(\mathcal B\)-orthogonal, and for a suitable \(c\ne0\)
\[
(y,c)\,\mathcal B\,(y,c)^T=y^TBy+2c\,\ell^Ty>0 .
\]
They span a positive plane for \(\mathcal B\), contradicting (P).

Now let \(a_1,\dots,a_m\) be real with \(\sum a_i=0\), for distinct \(s_i\), and put \(x_i=K(p,s_i)a_i\). Then \(\ell^Tx=\sum_ia_i=0\), and
\[
\sum_{i,j}a_ia_jD_p(s_i,s_j)=x^TBx\le0 .
\]
If some points coincide, combine their coefficients. \(\square\)

## 7. Exercises

**7.1.** Show that \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) has (P) and the identity matrix of size two does not. Show that a sum of two matrices with (P) need not have (P).

**7.2.** Check numerically or by hand that \(L(1)=1/\log2\) agrees with \(\int_0^12^\alpha\,d\alpha\).

**7.3.** Verify the formula for \(\varphi_p(s)-\varphi_p(t)\) in Remark 2.2.

**7.4.** Let \(M=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\). Check that its reciprocal has (P), compute \(\widetilde M\) of Lemma 4.1 for \(z=2\) and \(c=1\), and check that its reciprocal has (P).

**7.5.** Show that a kernel \(D\) with zero diagonal on a set with at least two points, all of whose finite matrices are positive semidefinite, is identically zero; so conditional negativity is a genuinely weaker condition than negative semidefiniteness of \(-D\).

## 8. Solutions

**7.1.** The eigenvalues of \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) are \(\pm1\); the identity has two eigenvalues \(1\). The identity is the sum of \(\operatorname{diag}(1,0)\) and \(\operatorname{diag}(0,1)\), each with (P).

**7.2.** \(\int_0^12^\alpha\,d\alpha=1/\log2\), and \(L(1)=1/\log(1+1)\).

**7.3.** The difference \((s-p)(1-\bar pt)-(t-p)(1-\bar ps)\) equals \((s-t)(1-|p|^2)\) after cancellation of \(-\bar pst+\bar pst\). For \(|s|=1\), \(|1-\bar ps|=|\bar s-\bar p|=|s-p|\).

**7.4.** The reciprocal \(\begin{pmatrix}1&2\\2&1\end{pmatrix}\) has eigenvalues \(3\) and \(-1\). \(\widetilde M=\begin{pmatrix}5/4&1\\1&2\end{pmatrix}\), with reciprocal \(\begin{pmatrix}4/5&1\\1&1/2\end{pmatrix}\), whose determinant \(2/5-1<0\) shows one positive and one negative eigenvalue.

**7.5.** For two points \(s,t\), positive semidefiniteness of \(\begin{pmatrix}0&D(s,t)\\D(s,t)&0\end{pmatrix}\) forces \(D(s,t)=0\).

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Section 5 (Theorem 5.1, Remark 5.2, Lemmas 5.3, 5.4, 5.6, Proposition 5.5). https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
- [AM00] J. Agler, J. E. McCarthy, *Complete Nevanlinna–Pick kernels*, J. Funct. Anal. 175 (2000), 111–124; arXiv:1610.01997, Corollary 1.12. https://arxiv.org/abs/1610.01997
