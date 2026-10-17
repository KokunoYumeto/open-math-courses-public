# Interpolation on a projected integer box

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The determinant of [A weighted determinant in a biquadratic field](a-weighted-determinant-in-a-biquadratic-field.md) is formed from evaluation rows: monomials \(z_1^{\alpha_1}z_2^{\alpha_2}z_3^{\alpha_3}\) evaluated at the \(N^4\) points \(An\in\mathbf C^3\), where \(n\) runs over the integer box \(\{0,\dots,N-1\}^4\) and \(A:\mathbf C^4\to\mathbf C^3\) is linear. For that determinant to be nonzero, enough of the rows must be linearly independent. This lesson proves that polynomials with separately bounded degrees \(t_1,t_2,t_3\) take arbitrary values at these points once \(\prod_j(t_j-3(N-1)+1)>(4N-3)^4\), provided the kernel of \(A\) is spanned by a vector whose coordinates are linearly independent over \(\mathbf Q\). The three degrees may be very unequal. The proof, which follows OpenAI [OpenAI-LS, Section 3], combines a dimension count, a nearest-point argument for an integer polytope, and Lagrange interpolation on one of its faces.

## 1. Convex sets

For a finite set \(S\subset\mathbf R^k\), \(\operatorname{conv}(S)\) is the set of convex combinations of points of \(S\); it is compact and convex. For a convex set \(P\) and \(t\ge0\), put \(tP=\{tv:v\in P\}\). If \(s,t\ge0\) and \(s+t>0\), then
\[
sP+tP=(s+t)P,
\]
because \(sv+tw=(s+t)\bigl(\tfrac s{s+t}v+\tfrac t{s+t}w\bigr)\) and \((s+t)v=sv+tv\) for \(v,w\in P\).

**Lemma 2.1** (nearest points). Let \(\mathcal K\subset\mathbf R^k\) be nonempty, compact and convex, and \(m\in\mathbf R^k\). Some point \(y\in\mathcal K\) is nearest to \(m\), and \(h=m-y\) satisfies \(h\cdot(x-y)\le0\) for every \(x\in\mathcal K\).

*Proof.* The distance to \(m\) is continuous on the compact set \(\mathcal K\), so it has a minimum at some \(y\). For \(x\in\mathcal K\) and \(0<t\le1\), the point \(y+t(x-y)\) lies in \(\mathcal K\), so
\[
\begin{aligned}
&\|h-t(x-y)\|^2-\|h\|^2\\
&\quad=-2t\,h\cdot(x-y)+t^2\|x-y\|^2\ge0 .
\end{aligned}
\]
Divide by \(t\) and let \(t\to0\). \(\square\)

**Lemma 2.2** (faces). Let \(S\subset\mathbf R^k\) be finite and nonempty, \(P=\operatorname{conv}(S)\), \(h\in\mathbf R^k\), and
\[
G=\{v\in P:h\cdot v=\max_{w\in P}h\cdot w\}.
\]
Then \(G=\operatorname{conv}(S\cap G)\). If \(h\ne0\), then \(G\) lies in an affine hyperplane.

*Proof.* Put \(\mu=\max_Ph\cdot w\). If \(v=\sum_i\lambda_is_i\) is a convex combination of points \(s_i\in S\) with all \(\lambda_i>0\) and \(v\in G\), then \(\sum_i\lambda_i(\mu-h\cdot s_i)=0\) with nonnegative terms, so every \(s_i\) lies in \(G\). Hence \(G\subset\operatorname{conv}(S\cap G)\). Conversely \(G\) is convex and contains \(S\cap G\). If \(h\ne0\), then \(G\) lies in the hyperplane \(\{v:h\cdot v=\mu\}\). \(\square\)

**Lemma 2.3** (Carathéodory). Let \(T\subset\mathbf R^k\) lie in an affine subspace of dimension \(e\). Every convex combination of points of \(T\) is a convex combination of at most \(e+1\) points of \(T\).

*Proof.* Write \(v=\sum_{i=1}^r\lambda_it_i\) with \(t_i\in T\), \(\lambda_i>0\), \(\sum_i\lambda_i=1\) and \(r\) least. If \(r>e+1\), the points \(t_i\) are affinely dependent: there are real \(\mu_i\), not all zero, with \(\sum_i\mu_it_i=0\) and \(\sum_i\mu_i=0\). Some \(\mu_i\) is positive. Let \(\kappa\) be the least value of \(\lambda_i/\mu_i\) over the indices with \(\mu_i>0\). The coefficients \(\lambda_i-\kappa\mu_i\) are nonnegative, have sum \(1\), represent \(v\), and at least one of them is zero. This contradicts the minimality of \(r\). \(\square\)

## 2. Polynomials

**Lemma 2.4.** A polynomial in \(k\) variables with complex coefficients that vanishes at every point of \(\mathbf Z^k\) is zero.

*Proof.* Induction on \(k\); for \(k=0\) there is nothing to prove. Write \(f=\sum_jf_j(x_1,\dots,x_{k-1})x_k^j\). For each \(x'\in\mathbf Z^{k-1}\), the polynomial \(f(x',x_k)\) in one variable has infinitely many roots, so all \(f_j(x')\) vanish. By induction every \(f_j\) is zero. \(\square\)

The polynomials \(B\in\mathbf C[z_1,z_2,z_3]\) with \(\deg_{z_j}B\le b_j\) for \(j=1,2,3\) form a vector space with basis the monomials \(z^\alpha=z_1^{\alpha_1}z_2^{\alpha_2}z_3^{\alpha_3}\), \(0\le\alpha_j\le b_j\), of dimension \(\prod_j(b_j+1)\). Translating the variable, \(B(z)\mapsto B(z+w)\), preserves each separate degree, and a polynomial of total degree at most \(D\) has each separate degree at most \(D\).

## 3. The interpolation theorem

Write \(E_N=\{0,\dots,N-1\}^4\). For integers \(t_1,t_2,t_3\ge0\), let \(\mathcal P_t\) be the space of \(B\in\mathbf C[z_1,z_2,z_3]\) with \(\deg_{z_j}B\le t_j\) for \(j=1,2,3\).

**Theorem 2.5** (OpenAI). Let \(A:\mathbf C^4\to\mathbf C^3\) be a surjective linear map whose kernel is spanned by a vector \(c\) whose four coordinates are linearly independent over \(\mathbf Q\). Let \(N\ge1\) and \(t_1,t_2,t_3\) be integers with \(t_j\ge3(N-1)\) for \(j=1,2,3\) and
\[
\prod_{j=1}^3\bigl(t_j-3(N-1)+1\bigr)>(4N-3)^4 .
\]
Then the evaluation map \(\mathcal P_t\to\mathbf C^{E_N}\), \(B\mapsto(B(An))_{n\in E_N}\), is surjective.

*Proof.* Suppose the image is a proper subspace. A nonzero linear form vanishes on it: there are complex numbers \(v_n\), not all zero, such that for every \(B\in\mathcal P_t\)
\[
\sum_{n\in E_N}v_nB(An)=0 .
\tag{2.1}
\]
Let \(S=\{n\in E_N:v_n\ne0\}\), \(P=\operatorname{conv}(S)\subset\mathbf R^4\) and \(\mathcal K=4P\).

*Step 1: an auxiliary polynomial.* Put \(b_j=t_j-3(N-1)\ge0\). Since \(\mathcal K\subset[0,4(N-1)]^4\), it contains at most \((4N-3)^4\) integer points. Vanishing at the points \(Am\), \(m\in\mathcal K\cap\mathbf Z^4\), imposes at most \((4N-3)^4\) linear conditions on the space of polynomials with \(\deg_{z_j}\le b_j\), whose dimension \(\prod_j(b_j+1)\) is larger. So there is a nonzero \(R\) with \(\deg_{z_j}R\le b_j\) such that, for every \(m\in\mathcal K\cap\mathbf Z^4\),
\[
R(Am)=0 .
\tag{2.2}
\]

*Step 2: the nearest nonzero value.* The polynomial \(R\circ A\) on \(\mathbf C^4\) is nonzero: otherwise \(R\) would vanish on \(A(\mathbf C^4)=\mathbf C^3\). By Lemma 2.4 some \(m\in\mathbf Z^4\) has \(R(Am)\ne0\). Choose such an \(m\) at least distance from \(\mathcal K\); this is possible because only finitely many integer points lie within a given distance of the bounded set \(\mathcal K\). By Lemma 2.1 some \(y\in\mathcal K\) is nearest to \(m\), and \(h=m-y\) satisfies \(h\cdot(x-y)\le0\) for \(x\in\mathcal K\). By (2.2), \(m\notin\mathcal K\), so \(h\ne0\).

*Step 3: a face and one of its points.* Let \(G=\{v\in P:h\cdot v=\max_Ph\cdot w\}\). For \(v\in P\), \(4v\in\mathcal K\) gives \(h\cdot v\le h\cdot(y/4)\), and \(y/4\in P\); so \(y/4\in G\). By Lemma 2.2, \(G=\operatorname{conv}(S\cap G)\), and \(S\cap G\) lies in an affine hyperplane. By Lemma 2.3,
\[
\frac y4=\sum_{i=1}^r\lambda_iu_i,\qquad r\le4,\quad u_i\in S\cap G,
\]
with \(\lambda_i>0\) and \(\sum_i\lambda_i=1\). Some \(\lambda_i\) is at least \(\frac14\); let \(u\) be its point. In
\[
y-u=(4\lambda_u-1)u+\sum_{u_i\ne u}4\lambda_iu_i
\]
the coefficients are nonnegative with sum \(3\). Therefore
\[
u\in S\cap G,\quad y-u\in3P .
\tag{2.3}
\]

*Step 4: vanishing off the face.* Let \(n\in S\setminus G\). By (2.3), \(y'=y+n-u\) lies in \(3P+P=\mathcal K\), and \(m'=m+n-u=y'+h\) is an integer point. Since \(u\in G\) and \(n\notin G\), \(h\cdot(u-n)>0\). For \(0<\eta\le1\) the point \(y'+\eta(y-y')\) lies in \(\mathcal K\), and as \(y-y'=u-n\),
\[
\begin{aligned}
&\|m'-y'-\eta(y-y')\|^2\\
&\quad=\|h\|^2-2\eta\,h\cdot(u-n)\\
&\qquad+\eta^2\|u-n\|^2 .
\end{aligned}
\]
For small \(\eta\) this is less than \(\|h\|^2\). So \(m'\) is closer to \(\mathcal K\) than \(m\), and the choice of \(m\) gives, for every \(n\in S\setminus G\),
\[
R\bigl(A(m+n-u)\bigr)=0 .
\tag{2.4}
\]

*Step 5: a rational hyperplane through the face.* Fix \(u_0\in S\cap G\). The integer vectors \(w-u_0\), \(w\in S\cap G\), span a real subspace of dimension at most \(3\); since they are rational, their span over \(\mathbf Q\) has the same dimension. Choose \(0\ne r\in\mathbf Z^4\) orthogonal to all of them, and put \(k=r\cdot u_0\in\mathbf Z\). The complex hyperplane
\[
\Pi=\{x\in\mathbf C^4:r\cdot x=k\}
\]
contains \(S\cap G\). As \(r\) is a nonzero integer vector and the coordinates of \(c\) are linearly independent over \(\mathbf Q\), \(r\cdot c\ne0\). Consequently \(A\) maps \(\Pi\) bijectively onto \(\mathbf C^3\). Indeed, two points of \(\Pi\) with the same image differ by a multiple \(tc\) with \(t\,(r\cdot c)=0\), hence coincide. And for \(z\in\mathbf C^3\), choose \(x\) with \(Ax=z\); the point \(x+tc\) with \(t=(k-r\cdot x)/(r\cdot c)\) lies in \(\Pi\) and maps to \(z\). The inverse is affine: if \(x_0\in\Pi\) and \(L\) is the inverse of the linear bijection \(A\) from \(\{r\cdot x=0\}\) onto \(\mathbf C^3\), the inverse sends \(z\) to \(x_0+L(z-Ax_0)\). Let \(\lambda_1(z),\dots,\lambda_4(z)\) be its coordinates, polynomials of degree at most \(1\) in \(z\). Then \(\lambda_i(An)=n_i\) for \(n\in\Pi\).

*Step 6: Lagrange interpolation on the face.* Choose \(i_0\) with \(r_{i_0}\ne0\), and put
\[
Q(z)=\prod_{i\ne i_0}\ \prod_{\substack{0\le a<N\\ a\ne u_i}}\frac{\lambda_i(z)-a}{u_i-a},
\]
with empty products equal to \(1\). Its total degree is at most \(3(N-1)\). Let \(n\in S\cap G\). Then \(n\in\Pi\) and
\[
Q(An)=\prod_{i\ne i_0}\ \prod_{a\ne u_i}\frac{n_i-a}{u_i-a}.
\]
If \(n_i\ne u_i\) for some \(i\ne i_0\), then \(n_i\in\{0,\dots,N-1\}\) is one of the excluded values \(a\), and \(Q(An)=0\). Otherwise \(n\) and \(u\) agree outside the coordinate \(i_0\), and \(r\cdot n=k=r\cdot u\) forces \(n=u\). Thus
\[
Q(An)=\begin{cases}1,&n=u,\\0,&n\in(S\cap G)\setminus\{u\}.\end{cases}
\]

*Step 7: the contradiction.* Let \(B(z)=Q(z)R(z+A(m-u))\). By Section 2, \(\deg_{z_j}B\le3(N-1)+b_j=t_j\), so \(B\in\mathcal P_t\). Since \(B(An)=Q(An)R(A(m+n-u))\), (2.1) gives
\[
0=\sum_{n\in S}v_nQ(An)R\bigl(A(m+n-u)\bigr).
\]
By (2.4) the terms with \(n\notin G\) vanish, and by Step 6 so do the terms with \(n\in G\), \(n\ne u\). The remaining term is \(v_uR(Am)\ne0\). \(\square\)

The proof never bounds the coefficients of \(R\) or \(Q\); the theorem is a statement of linear algebra, uniform in \(A\).

## 4. Rectangular boxes of exponents

**Corollary 2.6** (OpenAI). Let \(A\) be as in Theorem 2.5, and let \(H,N\) be integers with \(1\le H\le N\). Put
\[
\begin{aligned}
U&=N^{4/3},\qquad T_1=32H^{2/3}U,\\
T_2&=T_3=32H^{-1/3}U .
\end{aligned}
\]
The vectors \(\bigl((An)^\alpha\bigr)_{n\in E_N}\), for \(\alpha\in\mathbf Z_{\ge0}^3\) with \(\alpha_j\le T_j\) for \(j=1,2,3\), span \(\mathbf C^{E_N}\). Here \((An)^\alpha=(An)_1^{\alpha_1}(An)_2^{\alpha_2}(An)_3^{\alpha_3}\).

*Proof.* Put \(t_j=\lfloor T_j\rfloor\). Since \(H\le N\),
\[
\begin{aligned}
T_1&\ge32N^{4/3}\ge32N,\\
T_2&=32H^{-1/3}N^{4/3}\ge32N,
\end{aligned}
\]
and \(T_1T_2T_3=32^3N^4\). As \(32N\) is an integer, \(t_j\ge32N\ge3(N-1)\). Also \(t_j+1>T_j\) and \(T_j\ge6(N-1)\), so
\[
\begin{aligned}
&\prod_{j=1}^3\bigl(t_j-3(N-1)+1\bigr)\\
&\quad>\prod_{j=1}^3\bigl(T_j-3(N-1)\bigr)\\
&\quad\ge\frac{T_1T_2T_3}8=4096N^4\\
&\quad=(8N)^4>(4N-3)^4 .
\end{aligned}
\]
By Theorem 2.5 the evaluation map on \(\mathcal P_t\) is surjective. Its image is spanned by the images of the monomials \(z^\alpha\) with \(\alpha_j\le t_j\), and for integers \(\alpha_j\le t_j\) is the same as \(\alpha_j\le T_j\). \(\square\)

With \(H\) large, the box is long in the first exponent and short in the other two: \(T_1/T_2=H\), while the number of exponents stays of order \(N^4\). This is what the third lesson uses.

**Remark 2.7** (derivations on a torus). On \((\mathbf C^\times)^4\) put \(D_j=\sum_iA_{ji}x_i\,\partial/\partial x_i\) for \(j=1,2,3\). For the monomial \(x^n=x_1^{n_1}\cdots x_4^{n_4}\), \(x_i\partial x^n/\partial x_i=n_ix^n\), so \(D_jx^n=(An)_jx^n\) and
\[
\bigl(D_1^{\alpha_1}D_2^{\alpha_2}D_3^{\alpha_3}x^n\bigr)(1,1,1,1)=(An)^\alpha .
\]
Corollary 2.6 therefore says that no nonzero combination of the monomials \(x^n\), \(n\in E_N\), vanishes at \((1,1,1,1)\) together with all derivatives \(D^\alpha\), \(\alpha_j\le T_j\). Statements of this kind are multiplicity estimates; Philippon [Philippon] proved general multiplicity estimates on commutative algebraic groups.

## 5. Exercises

**2.1** (easy). Suppose the kernel of \(A\) is spanned by a nonzero integer vector \(w\) with \(\max_i|w_i|\le N-1\). Show that the evaluation map of Theorem 2.5 is not surjective, whatever \(t\) is.

**2.2** (easy). For \(N=1\), show that the evaluation map is surjective for all \(t_1,t_2,t_3\ge0\), although the hypothesis \(\prod_j(t_j+1)>1\) of Theorem 2.5 fails for \(t=(0,0,0)\). So the hypothesis is sufficient, not necessary.

**2.3** (easy). Show that \(P+P=2P\) can fail for a set \(P\) that is not convex.

**2.4** (medium). Suppose the first row \((A_{11},\dots,A_{14})\) of \(A\) has entries that are linearly independent over \(\mathbf Q\). Show that the numbers \((An)_1\), \(n\in E_N\), are pairwise distinct and that the vectors \(\bigl((An)_1^j\bigr)_{n\in E_N}\), \(0\le j<N^4\), span \(\mathbf C^{E_N}\). Thus a single exponent of size \(N^4\) suffices; Corollary 2.6 keeps every exponent of order \(N^{4/3}H^{2/3}\) at most.

## 6. Solutions

**2.1.** Choose \(n\in E_N\) with \(n+w\in E_N\): take \(n_i=0\) if \(w_i\ge0\) and \(n_i=-w_i\) otherwise. Then \(A(n+w)=An\), so every vector in the image has equal entries at \(n\) and \(n+w\), two different points of \(E_N\).

**2.2.** \(E_1=\{0\}\), and the constant polynomial \(1\) lies in every \(\mathcal P_t\) and has the value \(1\) at \(A0\).

**2.3.** For \(P=\{0,1\}\subset\mathbf R\), \(P+P=\{0,1,2\}\) and \(2P=\{0,2\}\).

**2.4.** If \((An)_1=(An')_1\), then \(\sum_iA_{1i}(n_i-n'_i)=0\) with integer coefficients, so \(n=n'\). The matrix \(\bigl((An)_1^j\bigr)\) is a Vandermonde matrix in \(N^4\) distinct numbers, and its determinant is nonzero.

## References

- [OpenAI-LS] OpenAI, *Uniform exclusion of Landau–Siegel zeros*, OpenAI Math Release preprint, 1 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026
- [Philippon] P. Philippon, *Lemmes de zéros dans les groupes algébriques commutatifs*, Bulletin de la Société Mathématique de France 114 (1986), 355–383. https://www.numdam.org/item/BSMF_1986__114__355_0/
