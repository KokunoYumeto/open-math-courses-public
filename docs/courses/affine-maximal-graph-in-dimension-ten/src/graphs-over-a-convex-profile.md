# Graphs over a convex profile

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The example \(u_0=\sqrt{|x|^9+t^2}\) of [The affine maximal equation](the-affine-maximal-equation.md) has the form \(\sqrt{F(x)^2+t^2}\). This lesson computes the Hessian of such functions and shows, following OpenAI [OpenAI-AM, Section 2], that the affine maximal equation for them follows from two second-order equations for \(F\) and an auxiliary function \(P\) of one variable fewer. For radial \(F\) and \(P\) these become ordinary differential equations.

Throughout, \(m\ge1\), the variables are \((x,t)\in\mathbb R^m\times\mathbb R\), so \(n=m+1\), and
\[
k=m+2,\qquad\gamma=\frac{m+3}{m+2} .
\]
For a function \(F\) on an open set \(\Omega\subseteq\mathbb R^m\) write \(H=D^2F\) for its Hessian in \(x\) and \(F_i,F_{ij}\) for its partial derivatives.

## 1. The Hessian and its determinant

**Lemma 1.1.** Let \(F\in C^2(\Omega)\) be positive and \(u(x,t)=\sqrt{F(x)^2+t^2}\) on \(\Omega\times\mathbb R\). As a quadratic form in \((\xi,\tau)\in\mathbb R^m\times\mathbb R\),
\[
\begin{aligned}
D^2u(\xi,\tau)={}&\frac Fu\,\xi^{\mathsf T}H\xi\\
&+\frac{F^2}{u^3}\Bigl(\tau-\frac tF\nabla F\cdot\xi\Bigr)^2 .
\end{aligned}
\]

*Proof.* Differentiating \(u^2=F^2+t^2\): \(u_t=t/u\) and \(u_i=FF_i/u\). Then
\[
\begin{aligned}
u_{tt}&=\frac1u-\frac{t^2}{u^3}=\frac{F^2}{u^3},\\
u_{it}&=-\frac{tFF_i}{u^3},\\
u_{ij}&=\frac{F_iF_j+FF_{ij}}u-\frac{F^2F_iF_j}{u^3}\\
&=\frac Fu F_{ij}+\frac{t^2}{u^3}F_iF_j .
\end{aligned}
\]
Expanding \(\frac{F^2}{u^3}(\tau-\frac tF\nabla F\cdot\xi)^2\) gives \(\frac{F^2}{u^3}\tau^2-\frac{2tF}{u^3}\tau\,\nabla F\cdot\xi+\frac{t^2}{u^3}(\nabla F\cdot\xi)^2\), which together with \(\frac Fu\xi^{\mathsf T}H\xi\) has exactly these coefficients. \(\square\)

**Corollary 1.2.** In the situation of Lemma 1.1, put \(\zeta=t/F\) and
\[
X_i=e_i+\zeta F_i\,e_t\quad(1\le i\le m),\qquad e_t ,
\]
where \(e_1,\dots,e_m,e_t\) is the standard basis. In the basis \(X_1,\dots,X_m,e_t\) the form \(D^2u\) is block diagonal, with blocks \(\frac FuH\) and \(\frac{F^2}{u^3}\). If \(H>0\), then \(D^2u>0\), and in all cases
\[
\det D^2u=F^{m+2}u^{-(m+3)}\det H .
\]

*Proof.* The linear form \(\tau-\zeta\nabla F\cdot\xi\) vanishes on each \(X_i\) and equals \(1\) on \(e_t\), and \(\xi^{\mathsf T}H\xi\) only sees the \(\mathbb R^m\) component, which is \(e_i\) for \(X_i\) and \(0\) for \(e_t\). This gives the blocks. The matrix \(S\) with columns \(X_1,\dots,X_m,e_t\) is triangular with ones on the diagonal, so \(\det S=1\) and \(\det D^2u=\det(S^{\mathsf T}D^2uS)\), which is \((F/u)^m\det H\cdot F^2/u^3\). If \(H>0\), both blocks are positive definite. \(\square\)

**Lemma 1.3.** If \(M\), \(N\) and \(S\) are square matrices of the same size, with \(M\) and \(S\) invertible, then \(\operatorname{tr}\bigl((S^{\mathsf T}MS)^{-1}S^{\mathsf T}NS\bigr)=\operatorname{tr}(M^{-1}N)\).

*Proof.* The left side is \(\operatorname{tr}(S^{-1}M^{-1}NS)\), and the trace is invariant under conjugation. \(\square\)

## 2. The reduction

**Proposition 2.1** (OpenAI). Let \(F\in C^4(\Omega)\) and \(P\in C^2(\Omega)\) be positive, with \(H=D^2F>0\), and suppose
\[
\begin{gathered}
\det H=FP^{-\gamma},\\
\operatorname{tr}(H^{-1}D^2P)+k\frac PF=0
\end{gathered}
\]
on \(\Omega\). Then \(u(x,t)=\sqrt{F(x)^2+t^2}\) has positive definite Hessian on \(\Omega\times\mathbb R\) and solves the affine maximal equation there, in \(n=m+1\) variables.

*Proof.* \(D^2u>0\) by Corollary 1.2, and \(u\in C^4\).

*The function \(w\).* By Corollary 1.2 and the first equation, \(\det D^2u=F^{m+3}u^{-(m+3)}P^{-\gamma}\). Since \(\gamma\cdot\frac{m+2}{m+3}=1\),
\[
\begin{aligned}
w&=(\det D^2u)^{-\frac{m+2}{m+3}}\\
&=\Bigl(\frac uF\Bigr)^{m+2}P=P\,h(\zeta),
\end{aligned}
\]
with \(h(\zeta)=(1+\zeta^2)^{k/2}\), because \(u/F=\sqrt{1+\zeta^2}\).

*Second derivatives of \(\zeta\).* From \(\zeta=t/F\),
\[
\begin{aligned}
\zeta_i&=-\frac{tF_i}{F^2},\qquad\zeta_t=\frac1F,\qquad\zeta_{tt}=0,\\
\zeta_{it}&=-\frac{F_i}{F^2},\\
\zeta_{ij}&=-\frac{tF_{ij}}{F^2}+\frac{2tF_iF_j}{F^3} .
\end{aligned}
\]
Hence \(d\zeta(X_i)=\zeta_i+\zeta F_i\zeta_t=0\), and
\[
\begin{aligned}
D^2\zeta(X_i,X_j)&=\zeta_{ij}+\zeta F_j\zeta_{it}+\zeta F_i\zeta_{jt}\\
&=-\frac\zeta FF_{ij} .
\end{aligned}
\]

*Second derivatives of \(w\).* As quadratic forms,
\[
\begin{aligned}
&D^2(Ph(\zeta))=h\,D^2P+Ph'D^2\zeta\\
&\quad+h'(dP\otimes d\zeta+d\zeta\otimes dP)\\
&\quad+Ph''\,d\zeta\otimes d\zeta .
\end{aligned}
\]
Since \(P\) does not depend on \(t\), \(D^2P(X_i,X_j)=P_{ij}\) and \(dP(e_t)=0\), \(D^2P(e_t,e_t)=0\). With \(d\zeta(X_i)=0\) this gives
\[
\begin{gathered}
D^2w(X_i,X_j)=hP_{ij}-\frac PF\zeta h'F_{ij},\\
D^2w(e_t,e_t)=\frac P{F^2}h'' .
\end{gathered}
\]

*The trace.* By Lemma 1.3, \(\operatorname{tr}((D^2u)^{-1}D^2w)\) can be computed in the basis of Corollary 1.2. There \(D^2u\) is block diagonal, so only the diagonal blocks of \(D^2w\) enter:
\[
\begin{aligned}
&\operatorname{tr}\bigl((D^2u)^{-1}D^2w\bigr)\\
&\quad=\frac uF\Bigl(h\operatorname{tr}(H^{-1}D^2P)\\
&\qquad\quad-m\frac PF\zeta h'\Bigr)+\frac{u^3}{F^2}\cdot\frac{Ph''}{F^2}.
\end{aligned}
\]
Multiplying by \(F/u\) and using \(u^2/F^2=1+\zeta^2\),
\[
\begin{aligned}
&\frac Fu\operatorname{tr}\bigl((D^2u)^{-1}D^2w\bigr)\\
&\quad=h\operatorname{tr}(H^{-1}D^2P)\\
&\qquad+\frac PF\bigl((1+\zeta^2)h''-m\zeta h'\bigr).
\end{aligned}
\]

*The function \(h\).* With
\[
\begin{aligned}
h'&=k\zeta(1+\zeta^2)^{k/2-1},\\
h''&=k(1+\zeta^2)^{k/2-1}\\
&\quad+k(k-2)\zeta^2(1+\zeta^2)^{k/2-2},
\end{aligned}
\]
one finds
\[
\begin{aligned}
&(1+\zeta^2)h''-m\zeta h'\\
&\quad=k(1+\zeta^2)^{\frac k2-1}\\
&\qquad\times\bigl(1+(k-1-m)\zeta^2\bigr)=kh,
\end{aligned}
\]
since \(k-1-m=1\). Hence \(\frac Fu\operatorname{tr}((D^2u)^{-1}D^2w)\) equals \(h\bigl(\operatorname{tr}(H^{-1}D^2P)+kP/F\bigr)\), which is \(0\) by the second equation. Finally
\[
\begin{aligned}
&\sum_{i,j}U^{ij}\partial_{ij}w\\
&\quad=\det(D^2u)\operatorname{tr}\bigl((D^2u)^{-1}D^2w\bigr)\\
&\quad=0 .\qquad\square
\end{aligned}
\]

**Remark 2.2.** The computation also gives a converse. For a positive \(F\in C^4(\Omega)\) with \(D^2F>0\), define \(P=(F/\det D^2F)^{1/\gamma}\), so that the first equation holds. The steps above are identities, so \(u=\sqrt{F^2+t^2}\) solves the affine maximal equation exactly when \(\operatorname{tr}(H^{-1}D^2P)+kP/F=0\).

## 3. Radial profiles

A function on a set of the form \(\{a<|x|<b\}\) is *radial* if it depends only on \(r=|x|\); its *profile* is the function of \(r\), written with the same letter.

**Lemma 3.1.** Let \(0\le a<b\), \(F\in C^2((a,b))\), and \(F(x)=F(|x|)\) on \(\{a<|x|<b\}\subseteq\mathbb R^m\), \(m\ge2\). With \(y=F'\),
\[
\begin{aligned}
D^2F(x)={}&y'(r)\frac{xx^{\mathsf T}}{r^2}\\
&+\frac{y(r)}r\Bigl(I-\frac{xx^{\mathsf T}}{r^2}\Bigr).
\end{aligned}
\]
So \(x\) is an eigenvector with eigenvalue \(y'\), and every vector orthogonal to \(x\) is an eigenvector with eigenvalue \(y/r\). For \(m=1\) the Hessian is \(y'\).

*Proof.* \(\partial_iF=F'(r)x_i/r\), and \(\partial_j(x_i/r)=\delta_{ij}/r-x_ix_j/r^3\), so
\[
\begin{aligned}
\partial_{ij}F={}&F''\frac{x_ix_j}{r^2}\\
&+F'\Bigl(\frac{\delta_{ij}}r-\frac{x_ix_j}{r^3}\Bigr).\qquad\square
\end{aligned}
\]

**Corollary 3.2** (the radial system). Let \(F,P\) be positive radial functions on \(\{a<|x|<b\}\), with profiles of class \(C^2\), and suppose \(y=F'>0\) and \(y'>0\). Then \(H=D^2F>0\), and the two equations of Proposition 2.1 hold on \(\{a<|x|<b\}\) if and only if, on \((a,b)\),
\[
\begin{aligned}
y^{m-1}y'&=r^{m-1}FP^{-\gamma},\\
(y^{m-1}P')'&=-k\,r^{m-1}P^{1-\gamma},\qquad F'=y .
\end{aligned}
\]

*Proof.* By Lemma 3.1, \(H\) has eigenvalues \(y'>0\) and \(y/r>0\), so \(H>0\) and \(\det H=y'(y/r)^{m-1}\). The Hessian of \(P\) has the same eigenvectors, with eigenvalues \(P''\) and \(P'/r\), so \(\operatorname{tr}(H^{-1}D^2P)=P''/y'+(m-1)P'/y\). The first equation of Proposition 2.1 is \(y'(y/r)^{m-1}=FP^{-\gamma}\), the first line above. Multiplying the second equation, \(P''/y'+(m-1)P'/y+kP/F=0\), by \(y'y^{m-1}>0\) gives
\[
(y^{m-1}P')'+kP\,\frac{y^{m-1}y'}F=0 ,
\]
and by the first line \(y^{m-1}y'/F=r^{m-1}P^{-\gamma}\). \(\square\)

The radial system is singular at \(r=0\): there \(y=F'(0)=0\) for a smooth radial \(F\), and the equations divide by powers of \(y\). [A radial solution through the origin](a-radial-solution-through-the-origin.md) constructs a solution that is smooth in \(x\) at the origin.

## 4. Exercises

**4.1** (easy). Show that at the points with \(t=0\) the Hessian of \(u=\sqrt{F^2+t^2}\) is the block matrix with blocks \(D^2F(x)\) and \(1/F(x)\).

**4.2** (medium). Let \(m=9\). Show that the profiles \(F(r)=r^{9/2}\) and \(P(r)=cr^{-33/2}\), with \(c>0\) given by \(c^{12/11}=4/\bigl(63\,(9/2)^8\bigr)\), solve the radial system for \(r>0\). Deduce that \(u_0(x,t)=\sqrt{|x|^9+t^2}\) solves the affine maximal equation on \(\{x\ne0\}\), and show that its Hessian at a point \((0,t)\), \(t\ne0\), is singular.

**4.3** (medium). For \(h(\zeta)=(1+\zeta^2)^{k/2}\) with any \(k>0\), compute \((1+\zeta^2)h''-m\zeta h'\), and show that it equals \(kh\) for all \(\zeta\) only when \(k=m+2\).

**4.4** (easy). For a radial \(F\) as in Lemma 3.1, show that \(\Delta F=F''+(m-1)F'/r\).

## 5. Solutions

**4.1.** At \(t=0\), \(u=F\) and \(\zeta=0\), so Lemma 1.1 gives \(D^2u(\xi,\tau)=\xi^{\mathsf T}H\xi+\tau^2/F\).

**4.2.** Here \(y=\frac92r^{7/2}\) and \(y'=\frac{63}4r^{5/2}\), so \(y^8y'=(\frac92)^8\frac{63}4r^{61/2}\), while \(r^8FP^{-12/11}=c^{-12/11}r^{8+9/2+18}\), which is \(c^{-12/11}r^{61/2}\). The first equation holds because \(c^{-12/11}=\frac{63}4(\frac92)^8\). Next \(P'=-\frac{33}2cr^{-35/2}\), so
\[
\begin{aligned}
(y^8P')'&=-\tfrac{33}2\cdot\tfrac{21}2\bigl(\tfrac92\bigr)^8c\,r^{19/2},\\
-11r^8P^{-1/11}&=-11c^{-1/11}r^{19/2}.
\end{aligned}
\]
These agree when \(c^{12/11}=11/\bigl(\frac{33}2\cdot\frac{21}2(\frac92)^8\bigr)\), that is \(c^{12/11}=4/\bigl(63(\frac92)^8\bigr)\), the same condition. On \(\Omega=\mathbb R^9\setminus\{0\}\) the functions \(F=|x|^{9/2}\) and \(P\) are smooth and positive with \(y,y'>0\), so Corollary 3.2 and Proposition 2.1 apply, and \(u_0=\sqrt{F^2+t^2}\) solves the equation on \(\Omega\times\mathbb R\). Near \((0,t)\) with \(t\ne0\), write \(u_0=\sqrt{G+t^2}\) with \(G=|x|^9\), a function of class \(C^8\) with \(G(0)=0\), \(\nabla G(0)=0\) and \(D^2G(0)=0\). The \(x\)-block of \(D^2u_0\) is \(D^2G/(2u_0)-\nabla G\nabla G^{\mathsf T}/(4u_0^3)\), which vanishes at \(x=0\); so \(D^2u_0(0,t)\) is singular.

**4.3.** As in the proof of Proposition 2.1, \((1+\zeta^2)h''-m\zeta h'\) equals \(k(1+\zeta^2)^{k/2-1}(1+(k-1-m)\zeta^2)\). Dividing by \(k(1+\zeta^2)^{k/2-1}\), equality with \(kh\) means \(1+(k-1-m)\zeta^2=1+\zeta^2\) for all \(\zeta\), that is \(k=m+2\).

**4.4.** The trace of the matrix in Lemma 3.1 is \(y'+(m-1)y/r\).

## References

- [OpenAI-AM] OpenAI, *A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten*, OpenAI Math Release preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026
