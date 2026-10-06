# Finite-rank traces and the exact ideal bounds

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

## Finite trace ideals

All Hilbert pairings are linear in the first variable. For finite-rank maps, singular values reduce trace and ideal estimates to finite sums, even when the ambient Hilbert spaces have arbitrary dimension. We first construct orthogonal projections and adjoints, then diagonalize finite self-adjoint matrices and derive the estimates.

The scalar and finite-dimensional prerequisites are proved in [Euclidean measure and product integration](finite-derivative-l2.md#euclidean-products), [The finite linear algebra and differential rules](coordinate-inverses-and-integration.md#coordinate-linear-algebra), and [Elementary functions, angular coordinates and smooth cutoffs](elementary-functions-and-cutoffs.md). The complex-polynomial argument below uses the angle-addition and polar-coordinate identities from the last reading.

### Elementary Hilbert tools

Expanding $\|x-cy\|^2\ge0$ with $c=(x,y)/\|y\|^2$ proves $|(x,y)|\le\|x\|\|y\|$ when $y\ne0$; the zero case is immediate. For a closed linear subspace $M$ and fixed $x$, put $d=\inf_{m\in M}\|x-m\|$. Choose $m_j$ with $\|x-m_j\|\to d$. The parallelogram identity gives
\[
 \|m_j-m_k\|^2
 \le2\|x-m_j\|^2+2\|x-m_k\|^2-4d^2\longrightarrow0.
\]
Completeness and closedness give a limit $m\in M$ attaining the distance. Comparing $m$ with $m+tv$ for real $t$, and then with $m+itv$, shows $(x-m,v)=0$ for every $v\in M$, by the linear terms in the squared norm. This characterizes $m$ uniquely. It also shows that the map $\Pi_M:x\mapsto m$ is linear and has norm at most one; the orthogonal decomposition gives $\|x\|^2=\|m\|^2+\|x-m\|^2$.

For a nonzero bounded linear functional $\ell$, its kernel is closed. Project a vector outside the kernel onto it and subtract the projection, then rescale the residual to get $v\perp\ker\ell$ with $\ell(v)=1$. Since $x-\ell(x)v\in\ker\ell$,
\[
 \ell(x)=(x,v)/\|v\|^2.
\]
This proves the representing-vector statement; the zero functional has representing vector zero. Cauchy–Schwarz and evaluation on the normalized representing vector prove equality of its norm with $\|\ell\|$. Apply this construction to $x\mapsto(Tx,y)$ to define the unique bounded adjoint $T^*$, with $(Tx,y)=(x,T^*y)$. Uniqueness proves linearity and $(AB)^*=B^*A^*$. Taking suprema over unit vectors in this identity gives $\|T^*\|=\|T\|$; applying it twice gives $T^{**}=T$.

For a finite orthonormal family, subtracting $\sum_j(x,e_j)e_j$ gives the orthogonal residual and hence Bessel's inequality. Subtracting these projections successively from any finite linearly independent list and normalizing the nonzero residuals produces an orthonormal basis of its span. Such a span is closed: if its vectors converge in norm, their finitely many coordinates converge, and the limit is their finite coordinate sum. For a complete orthonormal family, finite linear combinations are dense by definition. Approximation by such combinations makes the residual norm tend to zero, giving Parseval's identity. Thus every basis-sum identity used below follows from this projection calculation; it does not presuppose a spectral theorem.

<a id="finite-spectral-decomposition"></a>

### Finite spectral and singular decompositions

Here is the finite-dimensional compactness step. A bounded sequence in $\mathbb R^d$ lies in a closed box. Bisect that box in every coordinate and choose a subbox containing infinitely many terms; repeat. Their diameters tend to zero. Taking one later sequence term from each chosen box gives a Cauchy subsequence, which converges by completeness. For a sequence on the unit sphere its limit still has norm one. A maximizing sequence for a continuous real quadratic form therefore attains its maximum on that sphere.

Let $A=A^*$ on a nonzero finite-dimensional complex Hilbert space. The real function $(Av,v)$ on the unit sphere has a maximum $\lambda$ at some unit $v$ by the preceding real-coordinate argument. For $w\perp v$, compare the normalized vectors $(v+tw)/\|v+tw\|$ and $(v+itw)/\|v+itw\|$, with real $t$. The first derivatives at zero vanish and give respectively the real and imaginary parts of $(Av,w)$ equal to zero. Hence $Av=\lambda v$. The orthogonal complement of $v$ is $A$-invariant because $(Aw,v)=(w,Av)=0$. Induction on dimension gives an orthonormal eigenbasis, with real eigenvalues; if $(Ax,x)\ge0$, these eigenvalues are nonnegative. The zero-dimensional case is empty. This proves the finite spectral assertion in the generality used for each compressed matrix.

<a id="finite-singular-decomposition"></a>

Let now $T:H\to K$ be bounded and finite rank. Its range $V$ is finite-dimensional and closed, and $T^*=T^*\Pi_V$. Thus $S=\operatorname{ran}T^*$ is finite-dimensional. From the adjoint identity, $\ker T=S^\perp$. The positive self-adjoint operator $T^*T$ maps $S$ into $S$ and has zero kernel there: $(T^*Tv,v)=\|Tv\|^2$, while $S\cap S^\perp=0$. The finite theorem supplies an orthonormal eigenbasis $v_j$ of $S$ with eigenvalues $s_j^2>0$. Put $u_j=s_j^{-1}Tv_j$. Then $(u_j,u_k)=\delta_{jk}$. Since $T$ vanishes on $S^\perp$, this proves the finite singular decomposition
\[
 Tx=\sum_{j=1}^d s_j(x,v_j)u_j,
 \qquad s_j>0,
\]
where both finite families are orthonormal. Define $\|T\|_1=\sum_js_j$ and $\|T\|_{\rm HS}^2=\sum_js_j^2$. Parseval shows the latter equals $\sum_e\|Te\|^2$ in any orthonormal basis of $H$, since this is a finite sum after interchanging the $j$ indices. The decomposition proves invariance of both norms under unitary changes of source and target coordinates, and under extension by zero on extra orthogonal source directions or isometric inclusion of the target. Taking its adjoint interchanges the two orthonormal families and preserves the $s_j$, so both norms equal those of the adjoint. If $d\leq r$, Cauchy–Schwarz and $s_j\leq\|T\|$ give
\[
 \|T\|_1\leq\sqrt r\,\|T\|_{\rm HS},
 \qquad \|T\|_1\leq r\|T\|.
\]

<a id="finite-trace-inequalities"></a>

For a rank-one operator $x\mapsto(x,v)u$ on one Hilbert space, its trace is $(u,v)$: summing diagonal coefficients in any orthonormal basis gives this value by Parseval. By the finite singular expansion,
\[
 \operatorname{Tr}T=\sum_js_j(u_j,v_j),
 \qquad |\operatorname{Tr}T|\leq\|T\|_1.
\]
For a bounded map $C:K\to H$, the same rank-one calculation gives
\[
 \operatorname{Tr}_H(CT)=\sum_js_j(Cu_j,v_j)
 =\operatorname{Tr}_K(TC).
 \tag{1}
\]
It proves cyclicity for the actual unequal source and target spaces as well as the equality of a compressed finite-dimensional trace with the whole-space trace after extension by zero.

The finite trace duality is
\[
 \|T\|_1=\sup_{\|C\|\leq1}|\operatorname{Tr}(CT)|.
 \tag{2}
\]
The preceding expansion proves the upper bound. Equality is attained by the contraction taking $u_j$ to $v_j$ and vanishing on the orthogonal complement of their span. For arbitrary bounded $A:K\to K'$ and $B:H'\to H$, (1)–(2) therefore give
\[
 \|ATB\|_1
 =\sup_{\|C\|\leq1}|\operatorname{Tr}(CATB)|
 =\sup_{\|C\|\leq1}|\operatorname{Tr}(BCAT)|
 \leq\|A\|\,\|T\|_1\,\|B\|.
 \tag{3}
\]
The supremum formula also gives the triangle inequality and trace continuity in this finite-rank norm, including differences of finite-rank operators.

Parseval gives $\|AT\|_{\rm HS}\leq\|A\|\|T\|_{\rm HS}$, and adjoint equality gives $\|TB\|_{\rm HS}\leq\|T\|_{\rm HS}\|B\|$. For finite-rank maps $R:K\to L$ and $S:H\to K$, test $RS$ in (2), with $C:L\to H$ a contraction. Put $U=CR:K\to H$. Choose finite-dimensional subspaces $H_0\subset H$ containing $\operatorname{ran}U+\operatorname{ran}S^*$ and $K_0\subset K$ containing $\operatorname{ran}U^*+\operatorname{ran}S$. Both maps vanish on the corresponding orthogonal complements. For orthonormal bases $(e_i)$ of $H_0$ and $(f_j)$ of $K_0$, the pairing convention gives
\[
 \operatorname{Tr}(US)
 =\sum_{i,j}(Se_i,f_j)(Uf_j,e_i)
 =\sum_{i,j}\overline{(S^*f_j,e_i)}(Uf_j,e_i).
\]
Finite Cauchy–Schwarz bounds this by $\|U\|_{\rm HS}\|S^*\|_{\rm HS}\leq\|R\|_{\rm HS}\|S\|_{\rm HS}$. Taking the supremum in (2) proves
\[
 \|RS\|_1\leq\|R\|_{\rm HS}\|S\|_{\rm HS}.
 \tag{4}
\]
Every identity above is a finite singular or rank-one sum, so the estimates apply to finite-dimensional compressions inside arbitrary Hilbert spaces.

<a id="finite-complex-spectra"></a>

## Complex matrices and polynomial traces

Polynomial traces of a complex matrix depend only on its eigenvalues with algebraic multiplicity. We prove this by triangularization, starting with the existence of complex polynomial roots.

A nonconstant complex polynomial $p$ satisfies $|p(z)|\to\infty$ as $|z|\to\infty$: divide by its nonzero leading term and the remaining finite sum tends to one. It therefore attains its minimum modulus, by taking a bounded minimizing sequence and using the finite-dimensional compactness proved above. Suppose the minimum at $z_0$ were nonzero. For the first nonconstant coefficient in the translated polynomial write
\[
 \frac{p(z_0+w)}{p(z_0)}=1+a w^k+w^{k+1}r(w),
 \qquad a\ne0,
\]
where $r$ is a polynomial, possibly zero. Write $a=|a|(\cos\theta+i\sin\theta)$ and take $u=\cos((\pi-\theta)/k)+i\sin((\pi-\theta)/k)$. Repeated multiplication using the angle-addition identities gives $au^k=-|a|$. For small $t>0$, boundedness of $r(tu)$ and $|a|t^k<1$ give
\[
 \left|\frac{p(z_0+tu)}{p(z_0)}\right|
 \le 1-|a|t^k+C t^{k+1}<1,
\]
a contradiction. Hence $p$ has a root. If $p(\lambda)=0$, the identity
\[
 z^j-\lambda^j=(z-\lambda)\sum_{a=0}^{j-1}z^{j-1-a}\lambda^a
\]
factors out $z-\lambda$ term by term. Induction factors every nonconstant polynomial completely into linear factors, counting repetitions.

Let $T$ act on a nonzero $d$-dimensional complex vector space and choose $v\ne0$. The $d+1$ vectors $v,Tv,\ldots,T^dv$ are dependent, so some nonconstant polynomial $p$ satisfies $p(T)v=0$. Factor $p$ as just proved. Apply its linear factors successively to $v$; at the first step producing zero the preceding vector is nonzero and is an eigenvector of $T$. Normalize that vector and extend it to an orthonormal basis using the projection construction above. The matrix is
\[
 \begin{pmatrix}\lambda&*\\0&C\end{pmatrix}.
\]
Induct on the dimension of the compression $C$ to triangularize the whole matrix by an orthonormal change of basis. For an upper triangular matrix, products remain upper triangular and multiply diagonal entries. Thus a polynomial $q(T)$ has diagonal $q(\lambda_1),\ldots,q(\lambda_d)$ and trace their sum.

These diagonal entries list the eigenvalues with algebraic multiplicity. To see that this statement is basis independent, define the determinant by the alternating permutation sum. Expanding each column of a product in the columns of the first matrix, multilinearity and vanishing for repeated columns leave exactly the terms of the second determinant, proving $\det(AB)=\det A\det B$. This proves invariance of $\det(zI-T)$ under similarity. For a triangular matrix its permutation sum is the product $\prod_j(z-\lambda_j)$: a nonzero permutation term must select a row no larger than each column, which forces equality in every column. This proves the asserted multiplicities and the polynomial trace identity even for a nonnormal matrix. An eigenvector also gives $|\lambda_j|\le\|T\|$.

If $T$ is normal, $S=T-\lambda I$ is normal and
\[
 \|Sx\|^2=(x,S^*Sx)=(x,SS^*x)=\|S^*x\|^2.
\]
Consequently $Te=\lambda e$ implies $T^*e=\overline\lambda e$. The orthogonal complement of $e$ is invariant under both $T$ and $T^*$, and their restrictions remain adjoints and commute. Induction gives an orthonormal eigenbasis. In that basis the mixed trace is exactly $\sum_j\lambda_j^r\overline{\lambda_j}^{\,s}$ for nonnegative integers $r,s$.

<a id="finite-minmax"></a>

## The finite eigenvalue perturbation bound

Let $A=A^*$ have eigenvalues $\lambda_1\le\cdots\le\lambda_d$, with the orthonormal eigenbasis already proved above. Then
\[
 \lambda_j=
 \min_{\dim F=j}\ \max_{\substack{x\in F\\\|x\|=1}}(Ax,x).
\]
The span of the first $j$ eigenvectors gives the upper bound. In any $j$-dimensional $F$, the $j-1$ linear constraints of orthogonality to the first $j-1$ eigenvectors have a nonzero solution: elementary elimination leaves at least one free coordinate. Normalize that solution; its eigenbasis expansion has Rayleigh quotient at least $\lambda_j$. Compactness of each finite unit sphere gives the displayed maximum, and the first span attains the minimum. If $E=E^*$, Cauchy–Schwarz gives $|(Ex,x)|\le\|E\|$ for unit $x$. Applying both inequalities through this formula yields
\[
 |\lambda_j(A+E)-\lambda_j(A)|\le\|E\|,
 \qquad 1\le j\le d.
\]
This proves the ordered-eigenvalue estimate used for smoothing perturbations; no infinite-dimensional min–max theorem is required.

## References

- Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, second author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Section 6.2, Theorem 6.7, and Section 6.3, printed pages 161–166, for singular values and operator ideals.
- Sheldon Axler, [*Linear Algebra Done Right*, fourth author edition](https://linear.axler.net/LADR4e.pdf), 4.12–4.13, printed pages 125–126; 6.37–6.38, pages 203–204; and 7.31, page 246, for polynomial roots, triangularization and the complex spectral theorem.
