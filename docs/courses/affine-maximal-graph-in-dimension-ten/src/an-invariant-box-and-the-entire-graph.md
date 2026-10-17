# An invariant box and the entire graph

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[A radial solution through the origin](a-radial-solution-through-the-origin.md) produced a solution of the radial system near \(r=0\). This lesson shows that in the dimension \(m=9\), that is for graphs in ten variables, the solution exists for all \(r>0\) with \(F,P>0\), and proves Theorem A of [The affine maximal equation](the-affine-maximal-equation.md), following OpenAI [OpenAI-AM, Section 4]. The danger is that \(P\) reaches \(0\) at a finite radius, as it does when \(m=1\) (Exercise 3.4 of [A radial solution through the origin](a-radial-solution-through-the-origin.md)). It is excluded by following three logarithmic derivatives, which satisfy an autonomous system and stay in a box whose upper corner comes from the singular profile \(r^{9/2}\).

Section 1 collects the facts on ordinary differential equations that are used, with proofs. Results of the core courses Real Analysis I and II are cited from the text of Lebl [Lebl] by number.

## 1. Solutions of ordinary differential equations

Let \(U\subseteq\mathbb R\times\mathbb R^N\) be open and \(G:U\to\mathbb R^N\) continuously differentiable. A *solution* on an interval \(I\) is a continuously differentiable \(Y:I\to\mathbb R^N\) with \((r,Y(r))\in U\) and \(Y'(r)=G(r,Y(r))\) for \(r\in I\); at an endpoint of \(I\) that belongs to \(I\) the derivative is one-sided. Integrals of vector-valued functions are taken componentwise, and \(|\cdot|\) is the Euclidean norm.

**Lemma 1.1** (local existence and uniqueness). For \((r_0,Y_0)\in U\) there are \(h>0\) and a solution on \([r_0-h,r_0+h]\) with \(Y(r_0)=Y_0\). Two solutions on an interval \(I\) that agree at one point agree on \(I\).

*Proof.* Choose \(a,b>0\) with \(C=[r_0-a,r_0+a]\times\bar B(Y_0,b)\subseteq U\). On the compact set \(C\), \(|G|\le M_G\) and the derivative of \(G\) in \(Y\) has norm at most some \(L\). As \(\bar B(Y_0,b)\) is convex, with \(Z_\theta=Z+\theta(Y-Z)\),
\[
\begin{aligned}
&G(r,Y)-G(r,Z)\\
&\quad=\int_0^1D_YG(r,Z_\theta)(Y-Z)\,d\theta ,
\end{aligned}
\]
which gives \(|G(r,Y)-G(r,Z)|\le L|Y-Z|\) on \(C\). Let \(h=\min\bigl(a,\,b/(M_G+1),\,1/(2L+1)\bigr)\) and let \(E\) be the set of continuous \(Y:[r_0-h,r_0+h]\to\bar B(Y_0,b)\) with the supremum norm, a complete metric space [Lebl, Propositions 7.4.5 and 7.4.6]. The map
\[
T(Y)(r)=Y_0+\int_{r_0}^rG(\rho,Y(\rho))\,d\rho
\]
sends \(E\) to itself, since \(|T(Y)(r)-Y_0|\le hM_G\le b\), and \(\|T(Y)-T(Z)\|\le hL\|Y-Z\|\), which is at most \(\frac12\|Y-Z\|\). Its fixed point [Lebl, Theorem 7.6.2] is a solution, by the fundamental theorem of calculus [Lebl, Theorem 5.3.3].

For uniqueness, let \(Y,\hat Y\) be solutions on \(I\) and \(S=\{r\in I:Y(r)=\hat Y(r)\}\), which is nonempty and closed in \(I\). If \(r_1\in S\), apply the construction at \((r_1,Y(r_1))\), with constants \(h_1,b_1\). By continuity there is \(h'\in(0,h_1]\) such that on \(J=I\cap[r_1-h',r_1+h']\) both \(Y\) and \(\hat Y\) stay within \(b_1\) of \(Y(r_1)\). Both satisfy \(Y(r)=Y(r_1)+\int_{r_1}^rG(\rho,Y(\rho))\,d\rho\) on \(J\) [Lebl, Theorem 5.3.1], so both are fixed points of the corresponding contraction on the continuous maps \(J\to\bar B(Y(r_1),b_1)\), and they agree on \(J\). So \(S\) is open in \(I\), and \(S=I\) because \(I\) is connected. \(\square\)

**Lemma 1.2** (maximal solutions). For \((r_0,Y_0)\in U\) there is a solution \(Y\) on an open interval \((\alpha,\omega)\ni r_0\) with \(Y(r_0)=Y_0\) of which every solution through \((r_0,Y_0)\) is a restriction. If \(\omega<\infty\) and \(\mathcal C\subseteq U\) is compact, there is no \(r_1<\omega\) with \((r,Y(r))\in\mathcal C\) for all \(r\in[r_1,\omega)\).

*Proof.* By Lemma 1.1 all solutions through \((r_0,Y_0)\) agree where their intervals overlap, so together they define a solution on the union \(I^*\) of their intervals. If \(I^*\) contained its supremum \(\omega\), Lemma 1.1 at \((\omega,Y(\omega))\) and uniqueness would give a solution on a longer interval; so \(I^*\) is open on the right, and likewise on the left.

Suppose \(\omega<\infty\) and \((r,Y(r))\in\mathcal C\) for \(r\in[r_1,\omega)\). Then \(|Y'|\le\max_{\mathcal C}|G|\) there, so \(Y\) is Lipschitz on \([r_1,\omega)\) and \(Y(r)\) has a limit \(Y_\omega\) as \(r\to\omega\), with \((\omega,Y_\omega)\in\mathcal C\subseteq U\). Setting \(Y(\omega)=Y_\omega\), the identity \(Y(r)=Y(r_1)+\int_{r_1}^rG(\rho,Y(\rho))\,d\rho\) extends to \(r=\omega\), so \(Y\) is a solution on \((\alpha,\omega]\). Lemma 1.1 at \((\omega,Y_\omega)\) gives a solution on \([\omega-h,\omega+h]\), which agrees with \(Y\) on \([\omega-h,\omega]\); joined with \(Y\) it is a solution on \((\alpha,\omega+h)\), contradicting the first part. \(\square\)

**Lemma 1.3.** If \(G\) is smooth, every solution is smooth.

*Proof.* If \(Y\in C^\ell\), then \(r\mapsto G(r,Y(r))\) is of class \(C^\ell\), so \(Y'\in C^\ell\) and \(Y\in C^{\ell+1}\). \(\square\)

## 2. The radial system as a regular system

From here on
\[
m=9,\qquad k=11,\qquad\gamma=\tfrac{12}{11} .
\]
On the open set \(U\subseteq\mathbb R\times\mathbb R^4\) of the points \((r,F,P,y,Z)\) with \(r,F,P,y>0\) define the smooth map
\[
\begin{gathered}
G(r,F,P,y,Z)=(y,\ Z,\ g,\ G_4),\\
g=\frac{r^8FP^{-12/11}}{y^8},\\
G_4=-8\frac gyZ-\frac{11r^8P^{-1/11}}{y^8} .
\end{gathered}
\]

**Lemma 2.1.** Let \(F,P\) be profiles of class \(C^2\) on an interval \((a,b)\subseteq(0,\infty)\) with \(F,P,y>0\), where \(y=F'\). They solve the radial system of [Graphs over a convex profile](graphs-over-a-convex-profile.md) if and only if \(Y=(F,P,y,P')\) solves \(Y'=G(r,Y)\).

*Proof.* The first radial equation, \(y^8y'=r^8FP^{-12/11}\), says \(y'=g\). Expanding the second, \(8y^7y'P'+y^8P''=-11r^8P^{-1/11}\); given \(y'=g\), it says \(P''=-8\frac gyP'-11r^8P^{-1/11}/y^8\). \(\square\)

Let \(F,P\) be the solution of Proposition 2.1 of [A radial solution through the origin](a-radial-solution-through-the-origin.md), on \(0<r<\varepsilon\). Fix \(r_1\in(0,\varepsilon)\) and let \(Y=(F,P,y,Z)\) be the maximal solution of \(Y'=G(r,Y)\) through \((r_1,(F,P,F',P')(r_1))\), on \((\alpha,\omega)\) (Lemma 1.2). By Lemma 2.1 the local solution is a solution through the same point, so it is a restriction of \(Y\); as solutions stay in \(U\), where \(r>0\), \(\alpha=0\). Thus the local solution extends to \((0,\omega)\), with \(F,P,y>0\), \(Z=P'\), and \(y'=g>0\); it is smooth by Lemma 1.3. It remains to show \(\omega=\infty\).

## 3. Logarithmic derivatives

On \((0,\omega)\) define
\[
\begin{gathered}
A=\frac{ry}F,\qquad B=\frac{ry'}y,\\
C=-\frac{rP'}P,\qquad D=\frac CB ,
\end{gathered}
\]
which is possible because \(B>0\). A dot denotes \(r\,\frac d{dr}\), the derivative with respect to \(\log r\).

**Lemma 3.1** (OpenAI). On \((0,\omega)\), \(A>0\), \(B>0\), and
\[
\begin{aligned}
\dot A&=A(1+B-A),\\
\dot B&=B\bigl(9+A+\tfrac{12}{11}BD-9B\bigr),\\
\dot D&=(11-D)A-8D+BD\bigl(1-\tfrac D{11}\bigr).
\end{aligned}
\]
Moreover \((A,B,D)\to(0,1,0)\) as \(r\to0\), and \(A,B,D>0\) for all sufficiently small \(r>0\).

*Proof.* The computation is the same for every \(m\), with \(k=m+2\) and \(\gamma=\frac{m+3}{m+2}\). Positivity of \(F,y,y'\) gives \(A,B>0\). By the first radial equation,
\[
B=\frac{r^mFP^{-\gamma}}{y^m},\qquad AB=\frac{r^{m+1}P^{-\gamma}}{y^{m-1}} .
\]
Taking \(r\frac d{dr}\log\) of \(A\) and of \(B\),
\[
\begin{aligned}
\dot A&=A\Bigl(1+\frac{ry'}y-\frac{rF'}F\Bigr)\\
&=A(1+B-A),\\
\dot B&=B\Bigl(m+\frac{rF'}F-\gamma\frac{rP'}P-m\frac{ry'}y\Bigr)\\
&=B(m+A+\gamma C-mB).
\end{aligned}
\]
Next \(\dot C=C+C^2-r^2P''/P\), and the second radial equation gives
\[
\begin{aligned}
P''={}&-(m-1)\frac{y'}yP'\\
&-\frac{kr^{m-1}P^{1-\gamma}}{y^{m-1}},
\end{aligned}
\]
so
\[
\begin{gathered}
-\frac{r^2P''}P=-(m-1)BC+kAB,\\
\dot C=C\bigl(1+C-(m-1)B\bigr)+kAB .
\end{gathered}
\]
With \(C=BD\),
\[
\begin{aligned}
\dot D&=\frac{\dot C}B-D\frac{\dot B}B\\
&=(k-D)A-(m-1)D\\
&\quad+BD\bigl(1+(1-\gamma)D\bigr),
\end{aligned}
\]
and \(m=9\), \(k=11\), \(\gamma=\frac{12}{11}\) give the stated system.

Near \(r=0\), Proposition 1.3 of [A radial solution through the origin](a-radial-solution-through-the-origin.md) gives, with \(s=r^2/2\), \(F=f(s)=1+O(r^2)\), \(y=rq(s)=r+O(r^3)\), \(y'=q(s)+r^2q'(s)=1+O(r^2)\), \(P=1+O(r^2)\) and \(P'=rp'(s)=-\frac{11}9r+O(r^3)\). Hence \(A=r^2+O(r^4)\), \(B=1+O(r^2)\) and \(C=\frac{11}9r^2+O(r^4)\), so \((A,B,D)\to(0,1,0)\). Since \(P'<0\) for small \(r>0\), \(C\) and \(D\) are positive there. \(\square\)

## 4. The invariant box

Write \(V=(V_1,V_2,V_3)\) for the right side of the system in Lemma 3.1, a polynomial vector field on \(\mathbb R^3\), and let
\[
\mathcal B=[0,\tfrac92]\times[0,\tfrac72]\times[0,\tfrac{33}7].
\]

**Lemma 4.1** (OpenAI). (a) \(V(\frac92,\frac72,\frac{33}7)=0\).

(b) On the faces of \(\mathcal B\):
\[
\begin{aligned}
V_1(\tfrac92,B,D)&=\tfrac92\bigl(B-\tfrac72\bigr)\le0,\\
V_2(A,\tfrac72,D)&=\tfrac72\bigl(A+\tfrac{42}{11}D-\tfrac{45}2\bigr)\le0,\\
V_3(A,B,\tfrac{33}7)&=\tfrac{44}7A-\tfrac{264}7+\tfrac{132}{49}B\le0,
\end{aligned}
\]
and \(V_1=0\) where \(A=0\), \(V_2=0\) where \(B=0\), \(V_3=11A\ge0\) where \(D=0\), for \((A,B,D)\in\mathcal B\).

(c) If \(z:[s_0,s_1)\to\mathbb R^3\), with \(s_1\le\infty\), is continuously differentiable with \(\dot z=V(z)\) and \(z(s_0)\in\mathcal B\), then \(z(s)\in\mathcal B\) for all \(s\in[s_0,s_1)\).

*Proof.* (a) and the face formulas are direct substitutions; for instance \(V_2(\frac92,\frac72,\frac{33}7)=\frac72(\frac92+18-\frac{45}2)=0\). On the box, \(B\le\frac72\) gives the first inequality, \(A\le\frac92\) and \(D\le\frac{33}7\) give \(A+\frac{42}{11}D\le\frac92+18=\frac{45}2\), and \(A\le\frac92\), \(B\le\frac72\) give \(\frac{44}7A+\frac{132}{49}B\le\frac{198}7+\frac{66}7=\frac{264}7\).

(c) Let \(\Pi z\) be the point of \(\mathcal B\) obtained by clamping each coordinate of \(z\) to its interval. For every \(z\in\mathbb R^3\),
\[
(z-\Pi z)\cdot V(\Pi z)\le0 .
\]
Indeed, the coordinates in which \(z\) and \(\Pi z\) differ are those where \(z\) lies above or below the interval; for such a coordinate \(\Pi z\) lies on the corresponding upper or lower face, where by (b) the component of \(V\) is \(\le0\) on an upper face and \(\ge0\) on a lower face, opposite in sign to \(z_i-(\Pi z)_i\). The function \(\Delta(z)=|z-\Pi z|^2\) is continuously differentiable with gradient \(2(z-\Pi z)\), since in each coordinate it is the squared distance to an interval.

Let \(\mathcal N\) be the set of points within distance \(1\) of \(\mathcal B\), a compact convex set; on it \(|V(z)-V(z')|\le L_V|z-z'|\) for some \(L_V\), by the mean value inequality for the polynomial \(V\). Suppose \(z\) leaves \(\mathcal B\), and let \(s_*\) be the supremum of the \(s\) with \(z([s_0,s])\subseteq\mathcal B\); then \(s_*<s_1\) and \(z(s_*)\in\mathcal B\). Choose \(s_2\in(s_*,s_1)\) with \(z([s_*,s_2])\subseteq\mathcal N\). For \(s\) in that interval, with \(z=z(s)\),
\[
\begin{aligned}
\frac d{ds}\Delta(z)&=2(z-\Pi z)\cdot V(\Pi z)\\
&\quad+2(z-\Pi z)\cdot\bigl(V(z)-V(\Pi z)\bigr)\\
&\le2L_V\Delta(z),
\end{aligned}
\]
so \(e^{-2L_V(s-s_*)}\Delta(z(s))\) is nonincreasing and vanishes at \(s_*\). Hence \(z(s)\in\mathcal B\) on \([s_*,s_2]\), contradicting the choice of \(s_*\). \(\square\)

## 5. The entire solution and the proof of Theorem A

**Proposition 5.1** (OpenAI). \(\omega=\infty\): the radial solution exists for all \(r>0\), with \(F,P,y,y'>0\).

*Proof.* By Lemma 3.1 there is \(r_0\in(0,\varepsilon)\) with \((A,B,D)(r_0)\in\mathcal B\). The curve \(s\mapsto(A,B,D)(e^s)\) satisfies \(\dot z=V(z)\), so by Lemma 4.1 it stays in \(\mathcal B\) for \(r_0\le r<\omega\). Suppose \(\omega<\infty\). For \(r_0\le r<\omega\),
\[
\begin{gathered}
0\le A\le\tfrac92,\qquad0\le B\le\tfrac72,\\
0\le C=BD\le\tfrac{33}2 .
\end{gathered}
\]
Since \(r\frac d{dr}\log F=A\), \(r\frac d{dr}\log y=B\) and \(r\frac d{dr}\log P=-C\), integration from \(r_0\) to \(r\) gives
\[
\begin{gathered}
F(r_0)\le F(r)\le F(r_0)(\omega/r_0)^{9/2},\\
y(r_0)\le y(r)\le y(r_0)(\omega/r_0)^{7/2},\\
P(r_0)(r_0/\omega)^{33/2}\le P(r)\le P(r_0),
\end{gathered}
\]
and \(|P'(r)|=CP/r\le\frac{33}2P(r_0)/r_0\). So \((r,F,P,y,P')\) stays in a compact box contained in \(U\), as all its lower bounds for \(r,F,P,y\) are positive. This contradicts Lemma 1.2. \(\square\)

*Proof of Theorem A.* Let \(F,P\) be the radial functions on \(\mathbb R^9\) with the profiles of Proposition 5.1. On the ball \(|x|<\varepsilon\) they coincide with the smooth functions of Proposition 2.1 of [A radial solution through the origin](a-radial-solution-through-the-origin.md), and on \(\mathbb R^9\setminus\{0\}\) they are compositions of smooth maps; so they are smooth and positive on \(\mathbb R^9\). Their Hessian \(D^2F\) is positive definite: for \(x\ne0\) its eigenvalues are \(y'>0\) and \(y/r>0\) (Lemma 3.1 of [Graphs over a convex profile](graphs-over-a-convex-profile.md)), and \(D^2F(0)=I\). By Lemma 2.1 and Corollary 3.2 of [Graphs over a convex profile](graphs-over-a-convex-profile.md), the two equations
\[
\begin{gathered}
\det D^2F=FP^{-12/11},\\
\operatorname{tr}\bigl((D^2F)^{-1}D^2P\bigr)+11\frac PF=0
\end{gathered}
\]
hold on \(\mathbb R^9\setminus\{0\}\); both sides are continuous on \(\mathbb R^9\), so they hold at \(0\) as well. Proposition 2.1 of [Graphs over a convex profile](graphs-over-a-convex-profile.md) shows that
\[
\begin{gathered}
u(x,t)=\sqrt{F(x)^2+t^2},\\
(x,t)\in\mathbb R^9\times\mathbb R ,
\end{gathered}
\]
is smooth, has positive definite Hessian everywhere, and solves the affine maximal equation on \(\mathbb R^{10}\). Finally \(u(0,t)=\sqrt{1+t^2}\), whose second derivative \((1+t^2)^{-3/2}\) is not constant, while the restriction of a polynomial of degree at most two to the line \(x=0\) has constant second derivative. So \(u\) is not a polynomial of degree at most two. \(\square\)

## 6. Exercises

**6.1** (easy). Check that \(V(\frac92,\frac72,\frac{33}7)=0\) for all three components.

**6.2** (medium). For the singular profiles \(F=r^{9/2}\), \(P=cr^{-33/2}\) of Exercise 4.2 of [Graphs over a convex profile](graphs-over-a-convex-profile.md), show that \(A,B,C,D\) are the constants \(\frac92,\frac72,\frac{33}2,\frac{33}7\). So the upper corner of \(\mathcal B\) is the constant value of \((A,B,D)\) along the singular example \(u_0\) of [The affine maximal equation](the-affine-maximal-equation.md).

**6.3** (medium). Show that \((0,1,0)\) is a zero of \(V\), and that the matrix of derivatives of \(V\) there has eigenvalues \(2\), \(-9\) and \(-7\). Relate the eigenvalue \(2\) to the behaviour \(A=r^2+O(r^4)\) found in Lemma 3.1.

**6.4** (medium). Show that for \(r\ge1\)
\[
F(1)+y(1)(r-1)\le F(r)\le F(1)\,r^{9/2},
\]
so the solution \(u\) of Theorem A grows at least linearly and at most like \(|x|^{9/2}\) in the \(x\) directions.

## 7. Solutions

**6.1.** At the corner,
\[
\begin{aligned}
V_1&=\tfrac92\bigl(1+\tfrac72-\tfrac92\bigr)=0,\\
V_2&=\tfrac72\bigl(9+\tfrac92+\tfrac{12}{11}\cdot\tfrac72\cdot\tfrac{33}7-\tfrac{63}2\bigr)\\
&=\tfrac72\bigl(\tfrac{27}2+18-\tfrac{63}2\bigr)=0,\\
V_3&=\tfrac{44}7\cdot\tfrac92-\tfrac{264}7+\tfrac72\cdot\tfrac{33}7\cdot\tfrac47\\
&=\tfrac{198-264+66}7=0 .
\end{aligned}
\]

**6.2.** \(y=\frac92r^{7/2}\) and \(y'=\frac{63}4r^{5/2}\) give \(A=ry/F=\frac92\) and \(B=ry'/y=\frac72\); \(P'=-\frac{33}2P/r\) gives \(C=\frac{33}2\), and \(D=C/B=\frac{33}7\).

**6.3.** At \(A=0\), \(B=1\), \(D=0\): \(V_1=0\), \(V_2=1\cdot(9-9)=0\), \(V_3=0\). The derivatives there are \(\partial_AV_1=1+B-2A=2\), \(\partial_BV_1=\partial_DV_1=0\); \(\partial_AV_2=B=1\), \(\partial_BV_2=9+A+\frac{24}{11}BD-18B=-9\), \(\partial_DV_2=\frac{12}{11}B^2=\frac{12}{11}\); \(\partial_AV_3=11-D=11\), \(\partial_BV_3=D(1-\frac D{11})=0\), \(\partial_DV_3=-A-8+B(1-\frac{2D}{11})=-7\). The matrix
\[
\begin{pmatrix}2&0&0\\1&-9&\tfrac{12}{11}\\11&0&-7\end{pmatrix}
\]
has characteristic polynomial \((2-\lambda)(-9-\lambda)(-7-\lambda)\), by expanding along the first row. The solution leaves \((0,1,0)\) as \(\log r\) increases, along the direction of the eigenvalue \(2\): \(A\) grows like \(e^{2\log r}=r^2\).

**6.4.** Since \(B>0\), \(y\) is increasing, so \(F(r)=F(1)+\int_1^ry\), which is at least \(F(1)+y(1)(r-1)\). Since \(r\frac d{dr}\log F=A\le\frac92\) on \([1,\infty)\) (the solution stays in \(\mathcal B\) for \(r\ge r_0\), and \(r_0\) may be taken below \(1\)), \(\log F(r)-\log F(1)\le\frac92\log r\). The function \(u\) satisfies \(F(|x|)\le u(x,t)\le F(|x|)+|t|\).

## References

- [OpenAI-AM] OpenAI, *A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026
- [Lebl] J. Lebl, *Basic Analysis I and II*, version 6.3; the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/
