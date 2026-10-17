# A positive map and a hyperbolic polynomial

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the first half of Theorem A of Hyperbolic polynomials and spectrahedral cones: the polynomial \(p\) defined there is hyperbolic with respect to \(e=(I_4,I_4,0)\). It also describes two slices of its closed hyperbolicity cone \(K\), which are what the last lesson uses, and proves Corollary B. The key is that \(\Phi_y\) is a *positive map*: it sends positive semidefinite matrices to positive semidefinite matrices, because the Choi–Lam form of [The Choi–Lam form](the-choi-lam-form.md) is nonnegative. The proofs follow OpenAI [OpenAI-NS, Sections 3 and 7].

## 1. The positive map

A linear map \(\Psi:\mathbb S^n\to\mathbb S^k\) is *positive* if \(T\succeq0\) implies \(\Psi(T)\succeq0\). It then preserves the order: \(T\preceq T'\) implies \(\Psi(T)\preceq\Psi(T')\). It is *unital* if \(\Psi(I_n)=I_k\).

For \(u\in\mathbf R^4\) write \(u=(u_0,u')\) with \(u_0\in\mathbf R\) and \(u'\in\mathbf R^3\), matching the blocks in the definition of \(\Phi_y\).

**Lemma 3.1.** For \(u,v\in\mathbf R^4\) and \(y\in\mathbf R^3\),
\[
u^{\mathsf T}\Phi_y(vv^{\mathsf T})u=b(v_0u'-u_0v',\,y).
\]
Consequently \(\Phi_y\) is a positive map, and \(\Phi_{sy}=s^2\Phi_y\) for \(s\in\mathbf R\); in particular \(\Phi_0=0\) and \(\Phi_{-y}=\Phi_y\).

*Proof.* The matrix \(vv^{\mathsf T}\) has blocks \(a=v_0^2\), \(r=v_0v'\), \(T=v'v'^{\mathsf T}\). By the definition of \(\Phi_y\),
\[
\begin{aligned}
u^{\mathsf T}\Phi_y(vv^{\mathsf T})u={}&u_0^2\,v'^{\mathsf T}Q(y)v'\\
&-2u_0v_0\,u'^{\mathsf T}Q(y)v'\\
&+v_0^2\,u'^{\mathsf T}Q(y)u' ,
\end{aligned}
\]
using \(\operatorname{tr}(Q(y)v'v'^{\mathsf T})=v'^{\mathsf T}Q(y)v'\). This is \(w^{\mathsf T}Q(y)w=b(w,y)\) with \(w=v_0u'-u_0v'\). By Lemma 2.2 of the previous lesson it is nonnegative, so \(\Phi_y(vv^{\mathsf T})\succeq0\). Every positive semidefinite matrix is a sum of matrices \(vv^{\mathsf T}\) (Lemma 1.3(1) of the first lesson), and \(\Phi_y\) is linear. Finally \(Q(sy)=s^2Q(y)\). \(\square\)

Through this identity, nonnegative biquadratic forms correspond to positive maps; the correspondence is classical.

## 2. Hyperbolicity

**Proposition 3.2** (OpenAI). The polynomial \(p\) is homogeneous of degree \(20\) on the \(23\)-dimensional space \(\mathbb S^4\times\mathbb S^4\times\mathbf R^3\), \(p(e)=1\), and \(p\) is hyperbolic with respect to \(e\). For invertible \(X\), real or complex, the *inverse formula*
\[
\begin{aligned}
p(X,Z,y)={}&(\det X)^4\\
&\cdot\det\bigl(Z-\Phi_y(X^{-1})\bigr)
\end{aligned}
\]
holds.

*Proof.* The adjugate of \(X\) has entries of degree \(3\) in \(X\), and \(\Phi_y\) is quadratic in \(y\), so every entry of \((\det X)Z-\Phi_y(\operatorname{adj}X)\) is homogeneous of degree \(5\), and its determinant is homogeneous of degree \(20\). Since \(\Phi_0=0\), \(p(e)=\det I_4=1\). Extend \(\Phi_y\) complex linearly to complex symmetric matrices. For invertible \(X\), \(\operatorname{adj}X=(\det X)X^{-1}\) gives
\[
\begin{aligned}
&(\det X)Z-\Phi_y(\operatorname{adj}X)\\
&\quad=(\det X)\bigl(Z-\Phi_y(X^{-1})\bigr),
\end{aligned}
\]
and the inverse formula follows.

Fix real \(X,Z,y\) and \(t=\alpha+i\eta\) with \(\eta>0\). Diagonalize \(X=\sum_k\xi_ku_ku_k^{\mathsf T}\) with an orthonormal basis. Then
\[
\begin{aligned}
(tI-X)^{-1}&=\sum_k\frac{u_ku_k^{\mathsf T}}{t-\xi_k},\\
\operatorname{Im}(tI-X)^{-1}&=-\sum_k\frac{\eta\,u_ku_k^{\mathsf T}}{|t-\xi_k|^2}\prec0 ,
\end{aligned}
\]
where \(\operatorname{Im}\) is taken entrywise. The map \(\Phi_y\) commutes with taking entrywise real and imaginary parts, as it has real coefficients. So the matrix
\[
H=tI-Z-\Phi_y\bigl((tI-X)^{-1}\bigr)
\]
has \(\operatorname{Im}H=\eta I-\Phi_y\bigl(\operatorname{Im}(tI-X)^{-1}\bigr)\succeq\eta I\), since \(\Phi_y\) maps the positive definite matrix \(-\operatorname{Im}(tI-X)^{-1}\) to a positive semidefinite one. Here \(\operatorname{Im}H\) is real symmetric. If \(Hw=0\) for a nonzero \(w\in\mathbf C^4\), then \(w^*Hw=0\); but \(H=\operatorname{Re}H+i\operatorname{Im}H\) with real symmetric parts, so \(\operatorname{Im}(w^*Hw)=w^*(\operatorname{Im}H)w\ge\eta\|w\|^2>0\). So \(H\) is invertible. Since \(\Phi_{-y}=\Phi_y\), the inverse formula at the invertible matrix \(tI-X\) gives, with \(x=(X,Z,y)\),
\[
p(te-x)=\det(tI-X)^4\det H\ne0 .
\]
So the polynomial \(t\mapsto p(te-(X,Z,y))\) has no root with \(\operatorname{Im}t>0\). Its coefficients are real, so it has none with \(\operatorname{Im}t<0\) either. It has degree \(20\) with leading coefficient \(p(e)=1\), so all its roots are real. \(\square\)

## 3. Two slices of the cone

**Proposition 3.3** (OpenAI). Let \(K=\Lambda_+(p,e)\), and let \(X,Z\in\mathbb S^4\) and \(y\in\mathbf R^3\).

1. If \(X\succ0\), then \((X,Z,y)\in K\) if and only if \(Z\succeq\Phi_y(X^{-1})\).
2. \((X,Z,0)\in K\) if and only if \(X\succeq0\) and \(Z\succeq0\).

Moreover, \(e\) is an interior point of \(K\).

*Proof.* By Lemma 1.1(3) of the first lesson, \(x\in K\) if and only if \(p(x+te)\ne0\) for every \(t>0\).

Let \(X\succ0\), and for \(t\ge0\) put
\[
F(t)=Z+tI-\Phi_y\bigl((X+tI)^{-1}\bigr).
\]
By the inverse formula, with \(x=(X,Z,y)\),
\[
p(x+te)=\det(X+tI)^4\det F(t),
\]
and \(\det(X+tI)>0\). If \(F(0)\succeq0\), then for \(t>0\), since \(X^{-1}\succeq(X+tI)^{-1}\) and \(\Phi_y\) preserves the order,
\[
\begin{aligned}
F(t)&=F(0)+tI\\
&\quad+\Phi_y\bigl(X^{-1}-(X+tI)^{-1}\bigr)\\
&\succeq tI\succ0 ,
\end{aligned}
\]
so \(p((X,Z,y)+te)\ne0\) and \((X,Z,y)\in K\). Here \(X^{-1}\succeq(X+tI)^{-1}\) because the two matrices are diagonal in the same orthonormal basis, with entries \(1/\xi_k\ge1/(\xi_k+t)\). Conversely, suppose \(F(0)\) has a negative eigenvalue. For \(t>0\), \(0\preceq(X+tI)^{-1}\preceq t^{-1}I\), so \(0\preceq\Phi_y((X+tI)^{-1})\preceq t^{-1}\Phi_y(I)\), and \(F(t)\succ0\) for large \(t\). The least eigenvalue of \(F(t)\) depends continuously on \(t\) (Lemma 1.3(3) of the first lesson, applied to \(-F(t)\)), so it vanishes at some \(t>0\). There \(\det F(t)=0\), so \(p((X,Z,y)+te)=0\) for some \(t>0\), and \((X,Z,y)\notin K\). This proves the first statement; note that \(Z\succeq\Phi_y(X^{-1})\) means \(F(0)\succeq0\).

For \(y=0\), \(\Phi_0=0\) gives, directly from the definition and also for singular matrices,
\[
\begin{aligned}
&p\bigl(te-(X,Z,0)\bigr)\\
&\quad=\det(tI-X)^4\det(tI-Z).
\end{aligned}
\]
Its roots are the eigenvalues of \(X\), each four times, and those of \(Z\). They are all nonnegative exactly when \(X\succeq0\) and \(Z\succeq0\).

Finally, the set of \((X,Z,y)\) with \(X\succ0\) and \(Z-\Phi_y(X^{-1})\succ0\) is open, contains \(e\), and lies in \(K\) by the first statement. \(\square\)

The first slice is the bridge to the Choi–Lam form. A pencil describing \(K\) would describe in particular the inequality \(Z\succeq\Phi_y(X^{-1})\), and the rank-one identity of Lemma 3.1 would bring \(b\) into the pencil. The last lesson makes this precise.

## 4. A factor of degree four

The matrices \(K_i\in\mathbf R^{4\times4}\) below are not related to the cone \(K\). For the standard unit vectors \(e_i\) of \(\mathbf R^3\) put
\[
\begin{aligned}
K_i&=\begin{pmatrix}0&e_i^{\mathsf T}\\ -e_i&0\end{pmatrix}\in\mathbf R^{4\times4},\\
C&=\begin{pmatrix}K_1&K_2&K_3\end{pmatrix}\in\mathbf R^{4\times12}.
\end{aligned}
\]
For matrices \(U\) and \(V\), \(U\otimes V\) denotes the block matrix with blocks \(U_{ij}V\).

**Lemma 3.4.** For every \(T\in\mathbb S^4\),
\[
\begin{aligned}
\Phi_y(T)&=\sum_{i,j=1}^3Q(y)_{ij}K_iTK_j^{\mathsf T}\\
&=C\bigl(Q(y)\otimes T\bigr)C^{\mathsf T}.
\end{aligned}
\]

*Proof.* Write \(\epsilon_0,\dots,\epsilon_3\) for the standard basis of \(\mathbf R^4\), so that \(K_i=\epsilon_0\epsilon_i^{\mathsf T}-\epsilon_i\epsilon_0^{\mathsf T}\). Then
\[
\begin{aligned}
K_iTK_j^{\mathsf T}={}&T_{ij}\,\epsilon_0\epsilon_0^{\mathsf T}-T_{i0}\,\epsilon_0\epsilon_j^{\mathsf T}\\
&-T_{0j}\,\epsilon_i\epsilon_0^{\mathsf T}+T_{00}\,\epsilon_i\epsilon_j^{\mathsf T}.
\end{aligned}
\]
Multiply by \(Q(y)_{ij}\) and sum: the \((0,0)\) entry is \(\operatorname{tr}(Q(y)T')\) for the lower block \(T'\) of \(T\), the first row is \(-r^{\mathsf T}Q(y)\), the first column \(-Q(y)r\), and the lower block \(T_{00}Q(y)\), which is the definition of \(\Phi_y\). The second formula is the first written with block matrices. \(\square\)

*Proof of Corollary B.* Define the polynomial \(q(X,Z,y)\) by
\[
q=\det\begin{pmatrix}I_3\otimes X&C^{\mathsf T}\\ C\bigl(Q(y)\otimes I_4\bigr)&Z\end{pmatrix}.
\]
For invertible \(X\), the block \(I_3\otimes X\) is invertible with determinant \((\det X)^3\), and the determinant of a block matrix with invertible upper left block \(P\) is \(\det P\) times the determinant of the Schur complement. Since \(\bigl(Q(y)\otimes I_4\bigr)\bigl(I_3\otimes X^{-1}\bigr)=Q(y)\otimes X^{-1}\), Lemma 3.4 gives
\[
q=(\det X)^3\det\bigl(Z-\Phi_y(X^{-1})\bigr).
\]
With the inverse formula, \(p=(\det X)\,q\) wherever \(X\) is invertible, hence everywhere, as both sides are polynomials. So \(q\) is homogeneous of degree \(20-4=16\), \(q(e)=1\), and \(q=p/\det X\).

For real \(x=(X,Z,y)\), \(p(te-x)=\det(tI-X)\,q(te-x)\), so the roots of \(t\mapsto q(te-x)\) are among the real roots of \(t\mapsto p(te-x)\): \(q\) is hyperbolic with respect to \(e\). The roots of \(\det(tI-X)\) are the eigenvalues of \(X\), so, writing \(K_q=\Lambda_+(q,e)\),
\[
K=\{(X,Z,y):X\succeq0\}\cap K_q .
\]
It remains to show \(K_q\subseteq\{X\succeq0\}\). Since \(Q(-y)=Q(y)\), \(q\) is even in \(y\), so \((X,Z,y)\in K_q\) implies \((X,Z,-y)\in K_q\). By Gårding's theorem, Theorem 1.2(3) of the first lesson, \(K_q\) is convex, so \((X,Z,0)\in K_q\). But \(q(X,Z,0)=(\det X)^3\det Z\), so
\[
\begin{aligned}
&q\bigl(te-(X,Z,0)\bigr)\\
&\quad=\det(tI-X)^3\det(tI-Z),
\end{aligned}
\]
whose roots are nonnegative only if \(X\succeq0\). Hence \(K_q=K\), and Theorem A shows that it is not spectrahedral. \(\square\)

The determinant identity for block matrices used here is \(\bigl(\begin{smallmatrix}P&B'\\C'&D'\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}I&0\\C'P^{-1}&I\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}P&B'\\0&D'-C'P^{-1}B'\end{smallmatrix}\bigr)\), with determinants \(1\) and \(\det P\det(D'-C'P^{-1}B')\).

## 5. Exercises

**3.1** (easy). Compute \(\Phi_y(I_4)\) and show that \(\Phi_y(I_4)=\operatorname{diag}\bigl(\operatorname{tr}Q(y),Q(y)\bigr)\), with \(\operatorname{tr}Q(y)=2\|y\|^2\).

**3.2** (medium). Show that \(\Phi_y\) is not *completely positive* in the following weak sense: there are no linear maps \(V_k:\mathbf R^4\to\mathbf R^4\), depending linearly on \(y\), with \(\Phi_y(T)=\sum_kV_kTV_k^{\mathsf T}\) for all \(T\). (Hint: with \(T=vv^{\mathsf T}\), Lemma 3.1 would write \(b\) as a sum of squares of bilinear forms; use Corollary 2.4.)

**3.3** (easy). Check the slice description for \(X=I_4\), \(y=e_1\): show that \((I_4,Z,e_1)\in K\) if and only if \(Z\succeq\Phi_{e_1}(I_4)\), and compute \(Q(e_1)\).

**3.4** (easy). Show that \(p(X,Z,y)=0\) whenever \(X\) has rank at most two, using that \(\operatorname{adj}X\) then vanishes.

## 6. Solutions

**3.1.** With \(a=1\), \(r=0\) and \(T=I_3\), the definition gives the stated block diagonal matrix. The diagonal of \(Q(y)\) is \(y_i^2+y_{i+1}^2\), with sum \(2\|y\|^2\).

**3.2.** Suppose \(\Phi_y(T)=\sum_kV_k(y)TV_k(y)^{\mathsf T}\) with \(V_k\) linear in \(y\). By Lemma 3.1, \(b(v_0u'-u_0v',y)=\sum_k\bigl(u^{\mathsf T}V_k(y)v\bigr)^2\). Take \(v=\epsilon_0\), so that \(v_0u'-u_0v'=u'\): then \(b(u',y)=\sum_k(u^{\mathsf T}V_k(y)\epsilon_0)^2\) with \(u=(0,u')\), a sum of squares of bilinear forms in \((u',y)\). This contradicts Corollary 2.4.

**3.3.** \(Q(e_1)=\operatorname{diag}(1,0,1)\): its diagonal entries are \(y_1^2+y_2^2=1\), \(y_2^2+y_3^2=0\) and \(y_3^2+y_1^2=1\), and its off-diagonal entries vanish. By Proposition 3.3 with \(X^{-1}=I_4\), \((I_4,Z,e_1)\in K\) if and only if \(Z\succeq\Phi_{e_1}(I_4)=\operatorname{diag}(2,1,0,1)\).

**3.4.** If \(X\) has rank at most two, all its minors of order three vanish, so \(\operatorname{adj}X=0\); also \(\det X=0\). Then \((\det X)Z-\Phi_y(\operatorname{adj}X)=0\) and \(p=0\).

## References

- [OpenAI-NS] OpenAI, *A nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 24 September 2026, Sections 3 and 7. https://github.com/openai/math/tree/main/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026
