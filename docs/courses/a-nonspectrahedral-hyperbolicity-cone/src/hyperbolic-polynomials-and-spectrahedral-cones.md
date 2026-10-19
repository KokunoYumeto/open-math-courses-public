# Hyperbolic polynomials and spectrahedral cones

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A real symmetric matrix depending linearly on a parameter, \(L(x)=\sum_ix_iA_i\), defines the convex cone \(\{x:L(x)\succeq0\}\) of parameters at which it is positive semidefinite. Such cones are called *spectrahedral*; they are the feasible sets of semidefinite programming. The polynomial \(\det L(x)\) has a special property: restricted to every line in a direction where \(L\) is positive definite, it has only real roots. Polynomials with this property are called *hyperbolic*, and each of them defines a convex cone, its *hyperbolicity cone*. Every spectrahedral cone with an interior point is a hyperbolicity cone. Whether the converse holds is the geometric form of the *generalized Lax conjecture*. This course proves the theorem of OpenAI [OpenAI-NS] that it fails: an explicit polynomial of degree \(20\) in \(23\) variables has a hyperbolicity cone that no linear matrix inequality, of any size, describes.

## The theorem

Write \(\mathbb S^N\) for the real symmetric \(N\times N\) matrices, \(A\succeq0\) for positive semidefinite and \(A\succ0\) for positive definite. For \(z,y\in\mathbf R^3\), with indices read modulo \(3\), let
\[
\begin{aligned}
b(z,y)={}&\sum_{i=1}^3z_i^2y_i^2-2\sum_{i<j}z_iy_iz_jy_j\\
&+\sum_{i=1}^3z_i^2y_{i+1}^2 ,
\end{aligned}
\]
the *Choi–Lam form*. Let \(Q(y)\in\mathbb S^3\) have the entries \(Q(y)_{ii}=y_i^2+y_{i+1}^2\) and \(Q(y)_{ij}=-y_iy_j\) for \(i\ne j\), so that \(b(z,y)=z^{\mathsf T}Q(y)z\). Write a matrix of \(\mathbb S^4\) in blocks of sizes \(1\) and \(3\), and define the linear map \(\Phi_y:\mathbb S^4\to\mathbb S^4\) by
\[
\begin{aligned}
&\Phi_y\begin{pmatrix}a&r^{\mathsf T}\\ r&T\end{pmatrix}\\
&\quad=\begin{pmatrix}\operatorname{tr}(Q(y)T)&-r^{\mathsf T}Q(y)\\ -Q(y)r&a\,Q(y)\end{pmatrix}.
\end{aligned}
\]
With \(\operatorname{adj}X\) the adjugate of \(X\), put
\[
\begin{aligned}
p(X,Z,y)&=\det W,\\
W&=(\det X)Z-\Phi_y(\operatorname{adj}X)
\end{aligned}
\]
for \((X,Z,y)\in\mathbb S^4\times\mathbb S^4\times\mathbf R^3\), a real vector space of dimension \(10+10+3=23\).

**Theorem A** (OpenAI). The polynomial \(p\) is homogeneous of degree \(20\) and hyperbolic with respect to \(e=(I_4,I_4,0)\), with \(p(e)=1\). Its closed hyperbolicity cone \(K\) is not spectrahedral: for no \(N\ge1\) and no linear map \(L:\mathbb S^4\times\mathbb S^4\times\mathbf R^3\to\mathbb S^N\) is
\[
K=\{(X,Z,y):L(X,Z,y)\succeq0\}.
\]

**Corollary B** (OpenAI). The quotient \(q=p/\det X\) is a polynomial, homogeneous of degree \(16\) and hyperbolic with respect to \(e\), and its closed hyperbolicity cone is \(K\). So \(K\) is the hyperbolicity cone of a polynomial of degree \(16\) in \(23\) variables and is not spectrahedral.

The theorem concerns the cone, not the polynomial: no pencil of any size defines \(K\), even one whose determinant has other factors than \(p\). Hermitian pencils are included, since a Hermitian matrix \(A+iB\) is positive semidefinite exactly when the real symmetric matrix \(\bigl(\begin{smallmatrix}A&-B\\B&A\end{smallmatrix}\bigr)\) is.

**History.** Lax conjectured in 1958 that every hyperbolic polynomial in three variables is the determinant of a definite pencil of real symmetric matrices of matching size. Helton and Vinnikov proved the corresponding representation theorem [HV], and Lewis, Parrilo and Ramana observed that it implies Lax's statement. In more variables a polynomial need not be a determinant: Brändén found hyperbolic polynomials none of whose powers has a definite determinantal representation [Brä]. This does not decide whether the *cone* is spectrahedral, since a different pencil with more factors might define it. Kummer showed that this happens for the specialized Vámos polynomial, whose cone has a representation of size \(7\) although no power of the polynomial is a definite determinant [Kum]. Raghavendra, Ryder, Srivastava and Weitz proved exponential lower bounds for the size of such representations [RRSW]. Netzer and Sanyal proved that hyperbolicity cones whose boundary points are smooth points of the polynomial are linear images of spectrahedra [NS], and Kummer and Netzer proved that cones of *strictly* hyperbolic polynomials are spectrahedral [KuNe]. The polynomial \(p\) is not strictly hyperbolic (Exercise 1.4). Scheiderer found convex sets that are not even linear images of spectrahedra, by local obstructions from sums of squares [Sch].

Two later manuscripts of OpenAI continue the theorem. One exhibits the cone \(K\) as a linear image of a spectrahedron of size \(100\) with \(307\) auxiliary variables [OpenAI-LIFT]; this is Theorem C, proved in the last two lessons. So \(K\) separates the two forms of the conjecture: it is not spectrahedral, but it is a *spectrahedral shadow*, a linear image of a spectrahedron. The other manuscript gives hyperbolicity cones that are not even spectrahedral shadows, disproving the *projected* form of the conjecture [OpenAI-PROJ]; it is not treated in this course.

**The course.**

1. This lesson: hyperbolic polynomials, Gårding's theorem on the convexity of their cones, and spectrahedral cones.
2. [The Choi–Lam form](the-choi-lam-form.md): \(b\) is nonnegative, but no nonzero bilinear form \(\ell\) satisfies \(\ell^2\le b\).
3. [A positive map and a hyperbolic polynomial](a-positive-map-and-a-hyperbolic-polynomial.md): \(\Phi_y\) preserves positive semidefiniteness; \(p\) is hyperbolic; the slice of \(K\) with \(X\succ0\) is \(Z\succeq\Phi_y(X^{-1})\); Corollary B.
4. [No linear matrix inequality describes the cone](no-linear-matrix-inequality-describes-the-cone.md): a pencil for \(K\) would give a bilinear form \(\ell\ne0\) with \(\ell^2\le b\).
5. [Angular slices of the cone](angular-slices-of-the-cone.md): on each plane \(y=\eta(\cos\theta,\sin\theta,0)+\xi(0,0,1)\), a Gram factorization of \(Q(y)\) describes the slice of \(K\) by a linear matrix inequality of size \(20\).
6. [A finite semidefinite lift](a-finite-semidefinite-lift.md): a matching identity of degree two replaces the angle by \(307\) auxiliary variables; Theorem C.

**What the course assumes.** Linear algebra over \(\mathbf R\) and \(\mathbf C\), including determinants, adjugates and the spectral theorem for real symmetric matrices, whose consequences are collected in Section 3 below; continuity and derivatives of matrix-valued functions; Rouché's theorem from complex analysis.

## 1. Hyperbolic polynomials

Let \(p\in\mathbf R[x_1,\dots,x_m]\) be homogeneous of degree \(d\ge1\) and \(e\in\mathbf R^m\). The polynomial \(p\) is *hyperbolic with respect to* \(e\) if \(p(e)\ne0\) and, for every \(x\in\mathbf R^m\), all roots of the polynomial \(t\mapsto p(te-x)\) are real. By homogeneity this polynomial has degree \(d\) and leading coefficient \(p(e)\), so
\[
p(te-x)=p(e)\prod_{j=1}^d\bigl(t-\lambda_j(x)\bigr)
\]
with real numbers \(\lambda_1(x)\le\dots\le\lambda_d(x)\), the *eigenvalues* of \(x\). The *closed* and *open hyperbolicity cones* are
\[
\begin{aligned}
\Lambda_+(p,e)&=\{x:\lambda_j(x)\ge0\text{ for all }j\},\\
\Lambda_{++}(p,e)&=\{x:\lambda_j(x)>0\text{ for all }j\}.
\end{aligned}
\]

**Lemma 1.1.** Let \(p\) be hyperbolic with respect to \(e\).

1. For \(x\in\mathbf R^m\), \(s>0\) and \(r\in\mathbf R\), the eigenvalues of \(sx+re\) are \(s\lambda_j(x)+r\).
2. As polynomials in \(u\in\mathbf C\), \(p(x+ue)=p(e)\prod_j\bigl(u+\lambda_j(x)\bigr)\). In particular \(p(x)=p(e)\prod_j\lambda_j(x)\).
3. \(x\in\Lambda_+(p,e)\) if and only if \(p(x+te)\ne0\) for every real \(t>0\).

*Proof.* (1) \(p(te-sx-re)=s^dp\bigl(\frac{t-r}se-x\bigr)\) vanishes exactly at \(t=r+s\lambda_j(x)\), with the same multiplicities. (2) Substitute \(t=-u\) in the factorization and use \(p(-w)=(-1)^dp(w)\). (3) By (2), the roots of \(t\mapsto p(x+te)\) are the numbers \(-\lambda_j(x)\). \(\square\)

**Examples.** (a) The determinant on \(\mathbb S^n\) is hyperbolic with respect to the identity: \(\det(tI-X)\) has the eigenvalues of \(X\) as roots. Its closed cone is the cone of positive semidefinite matrices. (b) \(x_1x_2\cdots x_m\) is hyperbolic with respect to \((1,\dots,1)\), with cone the nonnegative orthant. (c) \(x_0^2-x_1^2-\dots-x_m^2\) is hyperbolic with respect to \((1,0,\dots,0)\); its roots along a line are \(x_0\pm(x_1^2+\dots+x_m^2)^{1/2}\), and its cone is the Lorentz cone \(x_0\ge(x_1^2+\dots+x_m^2)^{1/2}\).

## 2. Convexity of hyperbolicity cones

**Theorem 1.2** (Gårding). Let \(p\) be hyperbolic with respect to \(e\).

1. \(\Lambda_{++}(p,e)\) is the connected component of \(\{x:p(x)\ne0\}\) that contains \(e\).
2. \(p\) is hyperbolic with respect to every \(x\in\Lambda_{++}(p,e)\), and \(\Lambda_{++}(p,x)=\Lambda_{++}(p,e)\).
3. \(\Lambda_{++}(p,e)\) and \(\Lambda_+(p,e)\) are convex cones.

*Proof.* (1) Let \(x\in\Lambda_{++}\) and \(0\le s\le1\). By Lemma 1.1(1) the eigenvalues of \((1-s)e+sx\) are \(1-s+s\lambda_j(x)>0\), so the segment from \(e\) to \(x\) lies in \(\Lambda_{++}\), and \(\Lambda_{++}\) is connected. By Lemma 1.1(2), \(p\ne0\) on \(\Lambda_{++}\). The eigenvalues are continuous functions of \(x\), as the roots of a polynomial of fixed degree whose coefficients depend continuously on \(x\) (Rouché's theorem, Corollary 5.4.3 of the guide of Lebl in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50)). So \(\Lambda_{++}\) is open. It is also closed in \(\{p\ne0\}\): a limit \(x\) of points of \(\Lambda_{++}\) has \(\lambda_j(x)\ge0\), and \(\lambda_j(x)\ne0\) when \(p(x)\ne0\). A connected subset that is open and closed in \(\{p\ne0\}\) is a connected component.

(2) Let \(x\in\Lambda_{++}\); then \(p(x)\ne0\). Fix \(w\in\mathbf R^m\) and, for \(\alpha\ge0\), let
\[
f_\alpha(\tau)=p(w+\tau x+i\alpha e),
\]
a polynomial in \(\tau\) of degree \(d\) with leading coefficient \(p(x)\). For real \(\tau\) and \(\alpha>0\), Lemma 1.1(2) at the real point \(w+\tau x\) gives \(f_\alpha(\tau)=p(e)\prod_j(i\alpha+\lambda_j(w+\tau x))\ne0\). So for \(\alpha>0\) no root of \(f_\alpha\) is real.

Let \(n(\alpha)\) be the number of roots of \(f_\alpha\), with multiplicity, in the open lower half-plane. It is constant on \((0,\infty)\). Indeed, fix \(\alpha_0>0\) and choose disjoint closed discs around the distinct roots of \(f_{\alpha_0}\), each disjoint from the real axis. On their boundary circles \(|f_{\alpha_0}|\) has a positive minimum, and \(f_\alpha\to f_{\alpha_0}\) uniformly there as \(\alpha\to\alpha_0\). By Rouché's theorem, for \(\alpha\) close to \(\alpha_0\), \(f_\alpha\) has as many roots in each disc as \(f_{\alpha_0}\); these are all its \(d\) roots, and each lies on the same side of the real axis as the roots of \(f_{\alpha_0}\) in its disc.

For large \(\alpha\), \(n(\alpha)=d\). Put \(g_\alpha(\sigma)=\alpha^{-d}f_\alpha(\alpha\sigma)\), so that \(g_\alpha(\sigma)=p(w/\alpha+\sigma x+ie)\). As \(\alpha\to\infty\), \(g_\alpha\) converges, uniformly on compact sets, to \(g(\sigma)=p(\sigma x+ie)\), a polynomial of degree \(d\) with leading coefficient \(p(x)\). Its roots are the numbers \(\sigma=-i/\lambda_j(x)\): indeed \(g(0)=i^dp(e)\ne0\), and for \(\sigma\ne0\), Lemma 1.1(2) gives \(g(\sigma)=\sigma^dp(e)\prod_j(i/\sigma+\lambda_j(x))\). These roots lie in the open lower half-plane, because \(\lambda_j(x)>0\). By Rouché's theorem on small circles around them, for large \(\alpha\) all \(d\) roots of \(g_\alpha\), hence of \(f_\alpha\), lie in the open lower half-plane.

So every root of \(f_\alpha\), \(\alpha>0\), lies in the open lower half-plane. Suppose \(f_0(\tau)=p(w+\tau x)\) had a root \(\tau_0\) with \(\operatorname{Im}\tau_0>0\). Rouché's theorem on a small circle around \(\tau_0\) in the upper half-plane, avoiding the other roots of \(f_0\), gives a root of \(f_\alpha\) inside it for small \(\alpha>0\), which is impossible. Since \(f_0\) has real coefficients, it has no root with \(\operatorname{Im}\tau<0\) either. So all roots of \(\tau\mapsto p(w+\tau x)\) are real; replacing \(w\) by \(-w\) and \(\tau\) by \(-\tau\), so are those of \(t\mapsto p(tx-w)\). Thus \(p\) is hyperbolic with respect to \(x\). By part 1, applied to \(x\), the set \(\Lambda_{++}(p,x)\) is the connected component of \(\{p\ne0\}\) containing \(x\); as \(x\in\Lambda_{++}(p,e)\), this is \(\Lambda_{++}(p,e)\).

(3) By part 1, applied with \(x\) in place of \(e\), \(\Lambda_{++}(p,x)\) contains the segment from \(x\) to each of its points. By part 2, for every \(x\in\Lambda_{++}(p,e)\) this set is \(\Lambda_{++}(p,e)\). So \(\Lambda_{++}(p,e)\) contains every segment between two of its points: it is convex. It is a cone by Lemma 1.1(1). If \(x,x'\in\Lambda_+\) and \(0\le s\le1\), then \(x+\varepsilon e\) and \(x'+\varepsilon e\) lie in \(\Lambda_{++}\) for \(\varepsilon>0\), hence so does \((1-s)x+sx'+\varepsilon e\); by Lemma 1.1(1) the eigenvalues of \((1-s)x+sx'\) are therefore at least \(-\varepsilon\) for every \(\varepsilon>0\). \(\square\)

Gårding's theorem is classical; Pemantle's survey [Pem] presents it with the theory of stable polynomials.

## 3. Symmetric matrices

We collect the facts about real symmetric matrices used in the course. The spectral theorem says that every \(A\in\mathbb S^n\) has an orthonormal basis of eigenvectors \(u_1,\dots,u_n\) with real eigenvalues \(\mu_1,\dots,\mu_n\), so \(A=\sum_k\mu_ku_ku_k^{\mathsf T}\). For completeness, a proof: the continuous function \(x\mapsto x^{\mathsf T}Ax\) attains a maximum \(\mu_1\) on the unit sphere at some \(u_1\). For \(v\perp u_1\), the function \(\varepsilon\mapsto(u_1+\varepsilon v)^{\mathsf T}A(u_1+\varepsilon v)/\|u_1+\varepsilon v\|^2\) has a maximum at \(\varepsilon=0\), and its derivative there is \(2v^{\mathsf T}Au_1\). So \(Au_1\perp v\) for all \(v\perp u_1\), that is, \(Au_1=\mu_1u_1\). As \(A\) is symmetric, it maps \(u_1^\perp\) into itself, and induction on \(n\) applied to \(u_1^\perp\) gives the rest.

**Lemma 1.3.** Let \(A,B\in\mathbb S^n\).

1. \(A\succeq0\) if and only if every \(\mu_k\ge0\), and \(A\succ0\) if and only if every \(\mu_k>0\). A positive semidefinite matrix is a sum of matrices \(vv^{\mathsf T}\).
2. If \(A\succeq0\), there is a unique \(A^{1/2}\succeq0\) with \((A^{1/2})^2=A\). If \(x^{\mathsf T}Ax=0\), then \(Ax=0\).
3. \(\lambda_{\max}(A)=\max_{\|x\|=1}x^{\mathsf T}Ax\), and \(|\lambda_{\max}(A)-\lambda_{\max}(B)|\le\|A-B\|_{\mathrm{op}}\). For every real \(r\), \(rI\succeq A\) if and only if \(r\ge\lambda_{\max}(A)\).
4. For an invertible real matrix \(S\), \(A\succeq0\) if and only if \(S^{\mathsf T}AS\succeq0\).
5. (Schur complement.) If \(P\succ0\), then \(\bigl(\begin{smallmatrix}P&C\\C^{\mathsf T}&R\end{smallmatrix}\bigr)\succeq0\) if and only if \(R-C^{\mathsf T}P^{-1}C\succeq0\).
6. If \(A+H\succeq0\) and \(A-H\succeq0\), then \(\ker A\subseteq\ker H\).
7. For an \(a\times c\) real matrix \(C\), \(rI_c\succeq C^{\mathsf T}C\) if and only if \(r\ge\|C\|_{\mathrm{op}}^2\).

*Proof.* (1) \(x^{\mathsf T}Ax=\sum_k\mu_k(u_k^{\mathsf T}x)^2\), and \(A=\sum_k\mu_ku_ku_k^{\mathsf T}\) with \(\mu_ku_ku_k^{\mathsf T}=(\sqrt{\mu_k}u_k)(\sqrt{\mu_k}u_k)^{\mathsf T}\) when \(\mu_k\ge0\). (2) \(A^{1/2}=\sum_k\mu_k^{1/2}u_ku_k^{\mathsf T}\); a positive semidefinite square root acts on each eigenspace of \(A\) as the square root of its eigenvalue, which gives uniqueness. If \(x^{\mathsf T}Ax=\|A^{1/2}x\|^2=0\), then \(Ax=A^{1/2}A^{1/2}x=0\). (3) The formula follows from the expansion in (1); for unit \(x\), \(x^{\mathsf T}Ax\le x^{\mathsf T}Bx+\|A-B\|_{\mathrm{op}}\), and symmetrically. Also \(rI-A\) has eigenvalues \(r-\mu_k\). (4) \(x^{\mathsf T}S^{\mathsf T}ASx=(Sx)^{\mathsf T}A(Sx)\) and \(S\) is bijective. (5) With \(S=\bigl(\begin{smallmatrix}I&-P^{-1}C\\0&I\end{smallmatrix}\bigr)\), \(S^{\mathsf T}\bigl(\begin{smallmatrix}P&C\\C^{\mathsf T}&R\end{smallmatrix}\bigr)S=\operatorname{diag}(P,R-C^{\mathsf T}P^{-1}C)\); apply (4). (6) For \(w\in\ker A\), the nonnegative numbers \(w^{\mathsf T}(A\pm H)w\) have sum \(0\), so both vanish, and by (2) \((A+H)w=(A-H)w=0\); hence \(Hw=0\). (7) By (3), \(rI\succeq C^{\mathsf T}C\) means \(r\ge\max_{\|x\|=1}\|Cx\|^2=\|C\|_{\mathrm{op}}^2\). \(\square\)

## 4. Spectrahedral cones

A cone \(K\subseteq\mathbf R^m\) is *spectrahedral* if \(K=\{x:L(x)\succeq0\}\) for a linear map \(L(x)=\sum_ix_iA_i\) with \(A_i\in\mathbb S^N\), some \(N\ge1\).

**Proposition 1.4.** Let \(L(x)=\sum_ix_iA_i\) with \(A_i\in\mathbb S^N\) and \(L(e)\succ0\). Then \(p(x)=\det L(x)\) is hyperbolic with respect to \(e\), and \(\Lambda_+(p,e)=\{x:L(x)\succeq0\}\).

*Proof.* Put \(P=L(e)^{1/2}\), invertible, and \(S_x=P^{-1}L(x)P^{-1}\), a symmetric matrix. Then
\[
\begin{aligned}
p(te-x)&=\det\bigl(tL(e)-L(x)\bigr)\\
&=\det(P)^2\det(tI-S_x),
\end{aligned}
\]
so the eigenvalues of \(x\) are those of \(S_x\). They are real, and all are nonnegative exactly when \(L(x)\succeq0\), by Lemma 1.3(1) and (4). \(\square\)

So a spectrahedral cone \(\{L\succeq0\}\) with \(L(e)\succ0\) is a hyperbolicity cone. The *geometric generalized Lax conjecture* asserts the converse: every hyperbolicity cone \(\Lambda_+(p,e)\) is spectrahedral. Theorem A disproves it. Note that the pencil may have any size and its determinant need not be \(p\); the conjecture for cones is weaker than the statement that \(p\), or some power of \(p\), is the determinant of a definite pencil.

## 5. Exercises

**1.1** (easy). Show that \(x_0^2-x_1^2-\dots-x_m^2\) is the determinant of a definite pencil for \(m=2\): \(\det\bigl(\begin{smallmatrix}x_0+x_1&x_2\\x_2&x_0-x_1\end{smallmatrix}\bigr)\). Deduce from Proposition 1.4 that the Lorentz cone in \(\mathbf R^3\) is spectrahedral.

**1.2** (easy). Show that \(p(x)=x_1^2-x_2^2\) is hyperbolic with respect to \((1,0)\) and that \(\Lambda_{++}(p,(1,0))\) is one of the four components of \(\{p\ne0\}\). Check Theorem 1.2(2) for \(x=(2,1)\).

**1.3** (medium). Show that \(p(x)=x_1x_2-x_3^2\) is hyperbolic with respect to \(e=(1,1,0)\) and that its closed cone is \(\{x_1\ge0,\ x_2\ge0,\ x_1x_2\ge x_3^2\}\).

**1.4** (medium). Using \(\Phi_0=0\), show that \(p(te-w)=(t-1)^{16}t^4\) for \(w=(I_4,0,0)\). Conclude that \(p\) is not strictly hyperbolic, where *strictly hyperbolic* means that \(p(te-x)\) has distinct roots for every \(x\notin\mathbf Re\).

## 6. Solutions

**1.1.** The determinant is \(x_0^2-x_1^2-x_2^2\), and at \(e=(1,0,0)\) the matrix is \(I_2\succ0\).

**1.2.** \(p(te-x)=(t-x_1)^2-x_2^2\) has the real roots \(x_1\pm x_2\). So \(\Lambda_{++}=\{x_1>|x_2|\}\), one of the four open sectors cut out by the lines \(x_1=\pm x_2\). For \(x=(2,1)\), \(p(tx-w)=(2t-w_1)^2-(t-w_2)^2\) factors as \((t-w_1+w_2)(3t-w_1-w_2)\), with real roots.

**1.3.** \(p(te-x)=(t-x_1)(t-x_2)-x_3^2\) has discriminant \((x_1-x_2)^2+4x_3^2\ge0\). Its roots are nonnegative exactly when their sum \(x_1+x_2\) and product \(x_1x_2-x_3^2\) are nonnegative, which is the stated set. Alternatively, \(p=\det\bigl(\begin{smallmatrix}x_1&x_3\\x_3&x_2\end{smallmatrix}\bigr)\) and Proposition 1.4 applies.

**1.4.** \(te-w=((t-1)I_4,tI_4,0)\). Since \(\Phi_0=0\), the matrix in the definition of \(p\) at this point is \((t-1)^4t\,I_4\), so
\[
p\bigl((t-1)I_4,tI_4,0\bigr)=(t-1)^{16}t^4 .
\]
The point \(w\) is not a multiple of \(e\), and the roots \(1\) and \(0\) are multiple.

## References

- [OpenAI-NS] OpenAI, *A nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026
- [OpenAI-LIFT] OpenAI, *An exact semidefinite lift of a nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026
- [OpenAI-PROJ] OpenAI, *Hyperbolicity cones without semidefinite lifts*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026
- [HV] J. W. Helton and V. Vinnikov, *Linear matrix inequality representation of sets*, Communications on Pure and Applied Mathematics 60 (2007), 654–674; arXiv:math/0306180. https://arxiv.org/abs/math/0306180
- [Brä] P. Brändén, *Obstructions to determinantal representability*, Advances in Mathematics 226 (2011), 1202–1212; arXiv:1004.1382. https://arxiv.org/abs/1004.1382
- [Kum] M. Kummer, *A note on the hyperbolicity cone of the specialized Vámos polynomial*, Acta Applicandae Mathematicae 144 (2016), 11–15; arXiv:1306.4483. https://arxiv.org/abs/1306.4483
- [RRSW] P. Raghavendra, N. Ryder, N. Srivastava and B. Weitz, *Exponential lower bounds on spectrahedral representations of hyperbolicity cones*, arXiv:1711.11497. https://arxiv.org/abs/1711.11497
- [NS] T. Netzer and R. Sanyal, *Smooth hyperbolicity cones are spectrahedral shadows*, Mathematical Programming 153 (2015), 213–221; arXiv:1208.0441. https://arxiv.org/abs/1208.0441
- [KuNe] M. Kummer and T. Netzer, *The generalized Lax conjecture for strictly hyperbolic polynomials*, arXiv:2609.24542, September 2026. https://arxiv.org/abs/2609.24542
- [Sch] C. Scheiderer, *Spectrahedral shadows*, SIAM Journal on Applied Algebra and Geometry 2 (2018), 26–44; arXiv:1612.07048. https://arxiv.org/abs/1612.07048
- [Pem] R. Pemantle, *Hyperbolicity and stable polynomials in combinatorics and probability*, arXiv:1210.3231. https://arxiv.org/abs/1210.3231
