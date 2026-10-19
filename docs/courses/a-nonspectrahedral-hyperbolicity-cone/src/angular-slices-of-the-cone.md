# Angular slices of the cone

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Theorem A of [Hyperbolic polynomials and spectrahedral cones](hyperbolic-polynomials-and-spectrahedral-cones.md), no linear matrix inequality in the \(23\) coordinates of \((X,Z,y)\) describes the cone \(K\). With auxiliary variables the situation changes: \(K\) is the image under a linear projection of a spectrahedron. This and the next lesson prove this theorem of OpenAI [OpenAI-LIFT].

## The theorem

**Theorem C** (OpenAI). Identify \(\mathbb S^4\times\mathbb S^4\times\mathbf R^3\) with \(\mathbf R^{23}\) through the entries \(X_{ij}\) and \(Z_{ij}\), \(i\le j\), and \(y_1,y_2,y_3\). There are matrices \(A_1,\dots,A_{23},G_1,\dots,G_{307}\in\mathbb S^{100}\) such that, for every \(x\in\mathbf R^{23}\),
\[
\begin{aligned}
x\in K\iff{}&\text{there is }v\in\mathbf R^{307}\text{ with}\\
&\textstyle\sum_\nu x_\nu A_\nu+\sum_jv_jG_j\succeq0 .
\end{aligned}
\]
The equivalence holds on the whole closed cone, including the points with singular \(X\).

So \(K\) is a *spectrahedral shadow*. Netzer and Sanyal proved that hyperbolicity cones whose nonzero boundary points are smooth points of the polynomial are spectrahedral shadows [NS]; Theorem C is proved by an explicit construction that does not use such a hypothesis. This lesson cuts \(K\) by a family of planes in the \(y\)-coordinates and describes each slice by a linear matrix inequality of size \(20\) whose coefficients depend on an angle. The next lesson replaces the angle by finitely many auxiliary variables.

Throughout, \(Q(y)\), \(b\), \(\Phi_y\) and \(p\) are as in the first lesson.

## 1. A Gram factorization on planes

For \(\theta\in\mathbf R\) write \(c=\cos\theta\), \(s=\sin\theta\), \(w=e^{i\theta}\), \(d(\theta)=(c,s,0)\) and \(k=(0,0,1)\), and put
\[
Y_\theta(\eta,\xi)=\eta\,d(\theta)+\xi\,k\qquad(\eta,\xi\in\mathbf R).
\]
Every \(y\in\mathbf R^3\) lies on such a plane: write \((y_1,y_2)=\eta(\cos\theta,\sin\theta)\) in polar coordinates and take \(\xi=y_3\).

For a complex matrix \(F=(f_1,f_2)\in\mathbf C^{3\times2}\) let \(\widetilde F=(\operatorname{Re}f_1,\operatorname{Im}f_1,\operatorname{Re}f_2,\operatorname{Im}f_2)\in\mathbf R^{3\times4}\). Then \(\widetilde F\widetilde F^{\mathsf T}=\operatorname{Re}(FF^*)\), since for a column \(f\)
\[
\begin{aligned}
\operatorname{Re}(ff^*)={}&(\operatorname{Re}f)(\operatorname{Re}f)^{\mathsf T}\\
&+(\operatorname{Im}f)(\operatorname{Im}f)^{\mathsf T}.
\end{aligned}
\]
Define
\[
\begin{aligned}
U(\theta)&=\frac1{\sqrt2}\begin{pmatrix}-w^{-1}&-w\\ s\,w^{-2}&s\,w^2\\ c\,w^{-2}&-c\,w^2\end{pmatrix},\\
V_0&=\frac1{\sqrt2}\begin{pmatrix}0&0\\ i&i\\ 1&1\end{pmatrix},
\end{aligned}
\]
and \(F_\theta(\eta,\xi)=\eta\,U(\theta)+\xi\,V_0\).

**Lemma 5.1** (OpenAI). For all \(\theta,\eta,\xi\in\mathbf R\),
\[
\widetilde F_\theta(\eta,\xi)\,\widetilde F_\theta(\eta,\xi)^{\mathsf T}=Q\bigl(Y_\theta(\eta,\xi)\bigr).
\]
In particular \(Q(y)\succeq0\) for every \(y\in\mathbf R^3\).

*Proof.* Expand \(\operatorname{Re}(F_\theta F_\theta^*)\) in \(\eta,\xi\). Using \(|w|=1\), \(w+\bar w=2c\) and \(w-\bar w=2is\), the three coefficient matrices are
\[
\begin{aligned}
\operatorname{Re}(UU^*)&=\begin{pmatrix}1&-sc&0\\-sc&s^2&0\\0&0&c^2\end{pmatrix},\\
\operatorname{Re}(V_0V_0^*)&=\begin{pmatrix}0&0&0\\0&1&0\\0&0&1\end{pmatrix},\\
\operatorname{Re}(UV_0^*+V_0U^*)&=\begin{pmatrix}0&0&-c\\0&0&-s\\-c&-s&0\end{pmatrix}.
\end{aligned}
\]
For example, the \((1,2)\) entry of \(UU^*\) is \(\frac12\bigl(-\bar w\,s\,w^2-w\,s\,\bar w^2\bigr)=-sc\), and the \((2,3)\) entry of the last matrix is \(s\cos2\theta-c\sin2\theta=-s\). With the coefficients \(\eta^2\), \(\xi^2\) and \(\eta\xi\), the sum is \(Q(\eta c,\eta s,\xi)\): its diagonal is \(\eta^2\), \(\eta^2s^2+\xi^2\), \(\xi^2+\eta^2c^2\) and its entries off the diagonal are \(-\eta^2sc\), \(-\eta\xi c\), \(-\eta\xi s\). A matrix \(\widetilde F\widetilde F^{\mathsf T}\) is positive semidefinite, and every \(y\) lies on some plane. \(\square\)

Lemma 5.1 gives a second proof that the Choi–Lam form \(b(z,y)=z^{\mathsf T}Q(y)z\) of [The Choi–Lam form](the-choi-lam-form.md) is nonnegative, and writes it on each plane as a sum of four squares of forms that are linear in \(z\) and in \((\eta,\xi)\) separately. By Corollary 2.4 of that lesson, no such expression exists with coefficients independent of the plane.

## 2. The slice pencils

For \(r\in\mathbf R^3\) and \(u=(u_0,u')\in\mathbf R\times\mathbf R^3\) put
\[
\begin{aligned}
B(r)&=\begin{pmatrix}0&r^{\mathsf T}\\ -r&0\end{pmatrix}\in\mathbf R^{4\times4},\\
J_u&=\begin{pmatrix}u'&-u_0I_3\end{pmatrix}\in\mathbf R^{3\times4}.
\end{aligned}
\]
Then \(B(r)u=(r^{\mathsf T}u',-u_0r)=J_u^{\mathsf T}r\).

**Lemma 5.2** (OpenAI). Let \(y=Y_\theta(\eta,\xi)\) and let \(r_1,\dots,r_4\) be the columns of \(\widetilde F_\theta(\eta,\xi)\). For every \(W\in\mathbb S^4\),
\[
\sum_{j=1}^4B(r_j)^{\mathsf T}WB(r_j)=\Phi_y(W).
\]
Moreover, \(u^{\mathsf T}\Phi_y(W)u=\operatorname{tr}\bigl(J_uWJ_u^{\mathsf T}Q(y)\bigr)\) for all \(u\in\mathbf R^4\), \(W\in\mathbb S^4\) and \(y\in\mathbf R^3\).

*Proof.* For \(W=\bigl(\begin{smallmatrix}a&v^{\mathsf T}\\v&T\end{smallmatrix}\bigr)\), multiplying out gives
\[
\begin{aligned}
&B(r)^{\mathsf T}WB(r)\\
&\quad=\begin{pmatrix}r^{\mathsf T}Tr&-(r^{\mathsf T}v)\,r^{\mathsf T}\\ -(r^{\mathsf T}v)\,r&a\,rr^{\mathsf T}\end{pmatrix}.
\end{aligned}
\]
Summing over \(j\) and using \(\sum_jr_jr_j^{\mathsf T}=Q(y)\) (Lemma 5.1) gives the blocks \(\operatorname{tr}(Q(y)T)\), \(-v^{\mathsf T}Q(y)\), \(-Q(y)v\) and \(aQ(y)\) of \(\Phi_y(W)\). For the second statement,
\[
\begin{aligned}
u^{\mathsf T}\Phi_y(W)u&=\sum_j(J_u^{\mathsf T}r_j)^{\mathsf T}W(J_u^{\mathsf T}r_j)\\
&=\operatorname{tr}\Bigl(J_uWJ_u^{\mathsf T}\sum_jr_jr_j^{\mathsf T}\Bigr);
\end{aligned}
\]
both sides depend only on \(y\), and every \(y\) lies on some plane. \(\square\)

For \(\theta\in\mathbf R\), \(\mathcal X,\mathcal Z\in\mathbb S^4\) and \(\eta,\xi\in\mathbf R\), let \(r_j\) be the columns of \(\widetilde F_\theta(\eta,\xi)\) and define the symmetric matrix of size \(20\)
\[
\begin{aligned}
L_\theta(\mathcal X,\mathcal Z,\eta,\xi)&=\begin{pmatrix}I_4\otimes\mathcal X&\mathcal B\\ \mathcal B^{\mathsf T}&\mathcal Z\end{pmatrix},\\
\mathcal B&=\begin{pmatrix}B(r_1)\\ \vdots\\ B(r_4)\end{pmatrix},
\end{aligned}
\]
where \(I_4\otimes\mathcal X\) is block diagonal with four blocks \(\mathcal X\). For fixed \(\theta\), it is linear in \((\mathcal X,\mathcal Z,\eta,\xi)\), and its entries are trigonometric polynomials in \(\theta\) of degree at most \(3\), since the entries of \(U(\theta)\) involve only \(w^{\pm1}\), \(s\,w^{\pm2}\) and \(c\,w^{\pm2}\).

**Proposition 5.3** (OpenAI). For all \(\theta,\eta,\xi\in\mathbf R\) and \(\mathcal X,\mathcal Z\in\mathbb S^4\), with \(x=(\mathcal X,\mathcal Z,Y_\theta(\eta,\xi))\),
\[
p(te-x)=\det\bigl(tI_{20}-L_\theta(\mathcal X,\mathcal Z,\eta,\xi)\bigr),
\]
and \(x\in K\) if and only if \(L_\theta(\mathcal X,\mathcal Z,\eta,\xi)\succeq0\).

*Proof.* For invertible \(\mathcal X\), the determinant formula for block matrices (Section 4 of [A positive map and a hyperbolic polynomial](a-positive-map-and-a-hyperbolic-polynomial.md)) and Lemma 5.2 give, with \(B_j=B(r_j)\),
\[
\begin{aligned}
\det L_\theta&=(\det\mathcal X)^4\\
&\quad\cdot\det\Bigl(\mathcal Z-\sum_jB_j^{\mathsf T}\mathcal X^{-1}B_j\Bigr)\\
&=(\det\mathcal X)^4\\
&\quad\cdot\det\bigl(\mathcal Z-\Phi_y(\mathcal X^{-1})\bigr),
\end{aligned}
\]
with \(y=Y_\theta(\eta,\xi)\), which is \(p(x)\) by the inverse formula of Proposition 3.2 of that lesson. Both sides are polynomials in \((\mathcal X,\mathcal Z,\eta,\xi)\), so \(\det L_\theta=p(x)\) for all \(\mathcal X\). For \(\eta=\xi=0\) the matrix \(\mathcal B\) vanishes, so \(L_\theta(I_4,I_4,0,0)=I_{20}\). The point \(te-x\) is \((tI-\mathcal X,tI-\mathcal Z,Y_\theta(-\eta,-\xi))\), on the same plane, and linearity gives \(L_\theta\) at that point equal to \(tI_{20}-L_\theta(\mathcal X,\mathcal Z,\eta,\xi)\). Taking determinants proves the formula. So the eigenvalues of \(x\) with respect to \(p\) are the eigenvalues of the symmetric matrix \(L_\theta(\mathcal X,\mathcal Z,\eta,\xi)\), and they are all nonnegative exactly when this matrix is positive semidefinite. \(\square\)

Proposition 5.3 gives a second proof that \(p\) is hyperbolic, since every \(y\) lies on some plane. It also shows that each slice \(\{x\in K:y\in\text{plane }\theta\}\) is a spectrahedral cone in the \(22\) coordinates \((\mathcal X,\mathcal Z,\eta,\xi)\), described by \(L_\theta\succeq0\). If \(\mathcal X\succ0\), the Schur complement (Lemma 1.3(5) of the first lesson) turns \(L_\theta\succeq0\) into \(\mathcal Z\succeq\Phi_y(\mathcal X^{-1})\), the slice of Proposition 3.3. The cone \(K\) itself is the union of these slices over all angles, and by Theorem A it is not spectrahedral.

## 3. Exercises

**5.1** (easy). Check the \((1,3)\) entries in the proof of Lemma 5.1: \(\operatorname{Re}\bigl((UU^*)_{13}\bigr)=0\) and \(\operatorname{Re}\bigl((UV_0^*+V_0U^*)_{13}\bigr)=-c\).

**5.2** (easy). Let \(y=(0,0,\xi)\). Show that \(y=Y_\theta(0,\xi)\) for every \(\theta\), and that \(L_\theta(\mathcal X,\mathcal Z,0,\xi)\) does not depend on \(\theta\).

**5.3** (medium). Show that \(B(r)^{\mathsf T}=-B(r)\) and \(B(r)^2=-\operatorname{diag}(\|r\|^2,rr^{\mathsf T})\), and use this to compute \(\sum_jB(r_j)^{\mathsf T}I_4B(r_j)=\Phi_y(I_4)\).

**5.4** (medium). Compute \(p(te-x)\) for \(x=(0,I_4,k)\) from the definition of \(p\), and decide whether \(x\in K\). Which matrix \(L_\theta\) of Proposition 5.3 has these roots as eigenvalues?

## 4. Solutions

**5.1.** The rows of \(\sqrt2\,U\) give
\[
\begin{aligned}
(UU^*)_{13}&=\tfrac12\bigl(-c\,\bar ww^2+c\,w\bar w^2\bigr)\\
&=\tfrac c2(\bar w-w)=-ics,
\end{aligned}
\]
with real part \(0\). \((UV_0^*)_{13}=\frac12(-\bar w-w)=-c\), and \((V_0U^*)_{13}\) is the conjugate of \((UV_0^*)_{31}=0\), because the first row of \(V_0\) is zero.

**5.2.** \(Y_\theta(0,\xi)=\xi k\). Then \(F_\theta(0,\xi)=\xi V_0\), which does not involve \(\theta\), and so neither does \(L_\theta\).

**5.3.** \(B(r)^{\mathsf T}=\bigl(\begin{smallmatrix}0&-r^{\mathsf T}\\r&0\end{smallmatrix}\bigr)=-B(r)\), and \(B(r)^2=\bigl(\begin{smallmatrix}-r^{\mathsf T}r&0\\0&-rr^{\mathsf T}\end{smallmatrix}\bigr)\). Hence
\[
\begin{aligned}
&\textstyle\sum_jB(r_j)^{\mathsf T}B(r_j)=-\sum_jB(r_j)^2\\
&\quad=\operatorname{diag}\bigl(\textstyle\sum_j\|r_j\|^2,\sum_jr_jr_j^{\mathsf T}\bigr)\\
&\quad=\operatorname{diag}\bigl(\operatorname{tr}Q(y),Q(y)\bigr),
\end{aligned}
\]
which is \(\Phi_y(I_4)\) by Exercise 3.1.

**5.4.** Here \(te-x=(tI_4,(t-1)I_4,-k)\). By the definition of \(p\), with \(\operatorname{adj}(tI_4)=t^3I_4\), \(\Phi_{-k}=\Phi_k\) and \(P_k=\Phi_k(I_4)\),
\[
\begin{aligned}
p(te-x)&=\det\bigl(t^4(t-1)I_4-t^3P_k\bigr)\\
&=t^{12}\det\bigl((t^2-t)I_4-P_k\bigr).
\end{aligned}
\]
Since \(Q(k)=\operatorname{diag}(0,1,1)\), Exercise 3.1 of the third lesson gives \(P_k=\operatorname{diag}(2,0,1,1)\), so
\[
\begin{aligned}
p(te-x)={}&t^{13}(t-1)(t-2)(t+1)\\
&\cdot(t^2-t-1)^2 .
\end{aligned}
\]
The roots \(-1\) and \((1-\sqrt5)/2\) are negative, so \(x\notin K\). The point lies on the plane \(\theta=0\) with \(\eta=0\) and \(\xi=1\), and these roots are the eigenvalues of \(L_0(0,I_4,0,1)\), which is therefore not positive semidefinite.

## References

- [OpenAI-LIFT] OpenAI, *An exact semidefinite lift of a nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026
- [NS] T. Netzer and R. Sanyal, *Smooth hyperbolicity cones are spectrahedral shadows*, Mathematical Programming 153 (2015), 213–221; arXiv:1208.0441. https://arxiv.org/abs/1208.0441
