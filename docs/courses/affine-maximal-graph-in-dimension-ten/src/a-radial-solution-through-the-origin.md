# A radial solution through the origin

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Graphs over a convex profile](graphs-over-a-convex-profile.md) reduced the affine maximal equation for \(\sqrt{F(x)^2+t^2}\) to the radial system
\[
\begin{aligned}
y^{m-1}y'&=r^{m-1}FP^{-\gamma},\\
(y^{m-1}P')'&=-k\,r^{m-1}P^{1-\gamma},\qquad F'=y,
\end{aligned}
\]
for profiles \(F,P\) of radial functions, with \(k=m+2\) and \(\gamma=\frac{m+3}{m+2}\). The system divides by powers of \(y\), and \(y=F'\) vanishes at \(r=0\) for a smooth radial \(F\). This lesson constructs a solution with \(F(0)=P(0)=1\) that is smooth as a function of \(x\) near the origin, following OpenAI [OpenAI-AM, Section 3]. The idea is to integrate the system once from \(r=0\), to write it in the variable \(s=r^2/2\), and to solve the resulting integral equations with the contraction mapping principle.

Throughout, \(m\ge1\). Results of the core courses Real Analysis I and II are cited from the text of Lebl [Lebl] by number.

## 1. The fixed-point problem

Fix \(\delta\in(0,1]\). Let \(X=C([-\delta,\delta])^2\), the pairs \((f,p)\) of continuous functions, with the norm \(\|(f,p)\|=\max(\|f\|_\infty,\|p\|_\infty)\). It is complete: a Cauchy sequence has Cauchy components, which converge uniformly [Lebl, Proposition 7.4.5]. The set
\[
\begin{aligned}
\mathcal K=\bigl\{(f,p)\in X:{}&\|f-1\|_\infty\le\tfrac12,\\
&\|p-1\|_\infty\le\tfrac12\bigr\}
\end{aligned}
\]
is closed in \(X\), hence complete [Lebl, Proposition 7.4.6]. For \((f,p)\in\mathcal K\) and \(s\in[-\delta,\delta]\) put
\[
\begin{aligned}
Q(s)&=m\int_0^1v^{m-1}f(v^2s)\,p(v^2s)^{-\gamma}\,dv,\\
j(s)&=\int_0^1v^{m-1}p(v^2s)^{1-\gamma}\,dv ,
\end{aligned}
\]
\(q=Q^{1/m}\),
and define \(T(f,p)=(\tilde f,\tilde p)\) by
\[
\begin{aligned}
\tilde f(s)&=1+\int_0^sq(a)\,da,\\
\tilde p(s)&=1-k\int_0^sj(a)\,q(a)^{1-m}\,da .
\end{aligned}
\]
For \(v\in[0,1]\) the point \(v^2s\) lies in \([-\delta,\delta]\), so the integrands are defined.

**Lemma 1.1** (bounds). For \((f,p)\in\mathcal K\), the functions \(q\) and \(j\) are continuous on \([-\delta,\delta]\), and
\[
\begin{gathered}
\lambda\le q\le\Lambda,\\
\tfrac1m(\tfrac32)^{1-\gamma}\le j\le\tfrac1m2^{\gamma-1},\\
\lambda=\bigl(\tfrac12(\tfrac32)^{-\gamma}\bigr)^{1/m},\qquad\Lambda=\bigl(\tfrac32\,2^\gamma\bigr)^{1/m}.
\end{gathered}
\]

*Proof.* The integrands are continuous on \([0,1]\times[-\delta,\delta]\), so \(Q\) and \(j\) are continuous [Lebl, Proposition 7.5.12]. Since \(f,p\) take values in \([\frac12,\frac32]\) and \(a\mapsto a^{-\gamma}\) is decreasing, \(\frac12(\frac32)^{-\gamma}\le fp^{-\gamma}\le\frac32\,2^\gamma\); as \(m\int_0^1v^{m-1}dv=1\), \(Q\) lies between the same bounds, and \(q=Q^{1/m}\) between \(\lambda\) and \(\Lambda\). Since \(1-\gamma<0\), \(p^{1-\gamma}\) lies between \((\frac32)^{1-\gamma}\) and \(2^{\gamma-1}\), and \(\int_0^1v^{m-1}dv=\frac1m\). \(\square\)

**Lemma 1.2** (contraction). There are constants \(M\) and \(L\), depending only on \(m\), such that for every \(\delta\in(0,1]\) and all \((f,p),(\hat f,\hat p)\in\mathcal K\),
\[
\begin{aligned}
&\|T(f,p)-(1,1)\|\le M\delta,\\
&\|T(f,p)-T(\hat f,\hat p)\|\\
&\quad\le L\delta\,\|(f,p)-(\hat f,\hat p)\| .
\end{aligned}
\]

*Proof.* By Lemma 1.1, \(|\tilde f(s)-1|\le\Lambda|s|\) and \(|\tilde p(s)-1|\le\frac km2^{\gamma-1}\lambda^{1-m}|s|\), which gives the first bound with \(M=\max(\Lambda,\frac km2^{\gamma-1}\lambda^{1-m})\).

For the second, write \(\Delta=\|(f,p)-(\hat f,\hat p)\|\). On \([\frac12,\frac32]\) the derivatives of \(a\mapsto a^{-\gamma}\) and \(a\mapsto a^{1-\gamma}\) are bounded in absolute value by \(c_1=\gamma2^{\gamma+1}\) and \(c_2=(\gamma-1)2^\gamma\), so by the mean value theorem [Lebl, Theorem 4.2.4] these functions are Lipschitz there with those constants. Hence, at every point,
\[
\begin{aligned}
&|fp^{-\gamma}-\hat f\hat p^{-\gamma}|\\
&\quad\le|f-\hat f|\,p^{-\gamma}+\hat f\,|p^{-\gamma}-\hat p^{-\gamma}|\\
&\quad\le\bigl(2^\gamma+\tfrac32c_1\bigr)\Delta ,
\end{aligned}
\]
so \(|Q-\hat Q|\le(2^\gamma+\frac32c_1)\Delta\), and \(|j-\hat j|\le\frac{c_2}m\Delta\). The functions \(b\mapsto b^{1/m}\) on \([\lambda^m,\Lambda^m]\) and \(b\mapsto b^{1-m}\) on \([\lambda,\Lambda]\) are Lipschitz, again by the mean value theorem, and products of bounded Lipschitz functions are Lipschitz. So \(|q-\hat q|\le c_3\Delta\) and \(|jq^{1-m}-\hat j\hat q^{1-m}|\le c_4\Delta\) with constants depending only on \(m\). Integrating over an interval of length \(|s|\le\delta\) gives the second bound with \(L=\max(c_3,kc_4)\). \(\square\)

**Proposition 1.3.** Choose \(\delta\in(0,1]\) with \(M\delta\le\frac12\) and \(L\delta\le\frac12\). Then \(T\) maps \(\mathcal K\) into itself and has exactly one fixed point \((f,p)\in\mathcal K\). The functions \(f\) and \(p\) are smooth on \((-\delta,\delta)\), with
\[
\begin{gathered}
f'=q,\qquad p'=-k\,j\,q^{1-m},\\
f(0)=p(0)=1,\\
f'(0)=1,\qquad p'(0)=-\frac km .
\end{gathered}
\]

*Proof.* The functions \(\tilde f,\tilde p\) are continuous, and the first bound of Lemma 1.2 gives \(T(\mathcal K)\subseteq\mathcal K\). The second makes \(T\) a contraction with constant \(\frac12\), so the contraction mapping principle [Lebl, Theorem 7.6.2] gives a unique fixed point.

At the fixed point, \(f=1+\int_0^sq\) and \(p=1-k\int_0^sjq^{1-m}\) with continuous integrands, so by the fundamental theorem of calculus [Lebl, Theorem 5.3.3] \(f\) and \(p\) are continuously differentiable with the stated derivatives.

*Smoothness.* Suppose \(f,p\in C^\ell((-\delta,\delta))\) for some \(\ell\ge1\), and fix \(\delta'<\delta\). The integrand \(v^{m-1}f(v^2s)p(v^2s)^{-\gamma}\) has partial derivatives in \(s\) up to order \(\ell\), continuous on \([0,1]\times[-\delta',\delta']\): by the chain rule \(\partial_s^i[f(v^2s)]=v^{2i}f^{(i)}(v^2s)\), and \(p\ge\frac12\). Differentiating under the integral sign \(\ell\) times [Lebl, Theorem 9.1.1], \(Q\in C^\ell([-\delta',\delta'])\), and \(q=Q^{1/m}\in C^\ell\) because \(Q\ge\lambda^m>0\). In the same way \(j\) and \(q^{1-m}\) are of class \(C^\ell\). So \(f'\) and \(p'\) are of class \(C^\ell\) on \((-\delta',\delta')\), and \(f,p\in C^{\ell+1}\) there. As \(\delta'<\delta\) is arbitrary, induction gives \(f,p\in C^\infty((-\delta,\delta))\).

*Values at \(0\).* \(Q(0)=m\int_0^1v^{m-1}f(0)p(0)^{-\gamma}\,dv=1\), so \(f'(0)=q(0)=1\); and \(j(0)=\frac1m\), so \(p'(0)=-\frac km\). \(\square\)

## 2. The radial functions

**Proposition 2.1** (OpenAI). Let \((f,p)\) be the fixed point of Proposition 1.3, \(\varepsilon=\sqrt{2\delta}\), and on the ball \(B=\{x\in\mathbb R^m:|x|<\varepsilon\}\) define
\[
\begin{gathered}
F(x)=f\bigl(\tfrac12|x|^2\bigr),\\
P(x)=p\bigl(\tfrac12|x|^2\bigr).
\end{gathered}
\]
Then \(F,P\in C^\infty(B)\) are positive, \(F(0)=P(0)=1\),
\[
D^2F(0)=I,\qquad D^2P(0)=-\frac kmI ,
\]
and \(D^2F(x)\) is positive definite for every \(x\in B\). Their profiles satisfy, for \(0<r<\varepsilon\) and with \(y=F'\),
\[
y>0,\qquad y'>0,\qquad P'<0,
\]
and the radial system.

*Proof.* The map \(x\mapsto\frac12|x|^2\) is smooth with values in \([0,\delta)\), so \(F\) and \(P\) are smooth, and they take values in \([\frac12,\frac32]\). With \(s=\frac12|x|^2\), \(\partial_iF=f'(s)x_i\) and \(\partial_{ij}F=f''(s)x_ix_j+f'(s)\delta_{ij}\), so \(D^2F(0)=f'(0)I=I\), and in the same way \(D^2P(0)=p'(0)I\).

The profile of \(F\) is \(F(r)=f(r^2/2)\), so \(y(r)=rf'(r^2/2)=rq(r^2/2)>0\) for \(0<r<\varepsilon\). Fix such \(r\) and put \(s=r^2/2\). Since \(f(v^2s)=F(rv)\) and \(p(v^2s)=P(rv)\), the substitution \(\rho=rv\) [Lebl, Theorem 5.3.5] gives
\[
\begin{aligned}
y(r)^m&=r^mQ(s)\\
&=m\int_0^r\rho^{m-1}F(\rho)P(\rho)^{-\gamma}\,d\rho,\\
r^mj(s)&=\int_0^r\rho^{m-1}P(\rho)^{1-\gamma}\,d\rho .
\end{aligned}
\]
Moreover \(P'(r)=rp'(s)=-krj(s)q(s)^{1-m}\), and \(y^{m-1}=r^{m-1}q(s)^{m-1}\), so
\[
\begin{aligned}
y^{m-1}P'&=-kr^mj(s)\\
&=-k\int_0^r\rho^{m-1}P(\rho)^{1-\gamma}\,d\rho .
\end{aligned}
\]
Differentiating both integral identities [Lebl, Theorem 5.3.3] gives \(my^{m-1}y'=mr^{m-1}FP^{-\gamma}\) and \((y^{m-1}P')'=-kr^{m-1}P^{1-\gamma}\), which is the radial system. The first identity shows \(y'>0\), and the last integral shows \(P'<0\).

For \(0<|x|<\varepsilon\), the eigenvalues of \(D^2F(x)\) are \(y'\) and \(y/r\) by Lemma 3.1 of [Graphs over a convex profile](graphs-over-a-convex-profile.md), both positive; at \(x=0\), \(D^2F(0)=I\). \(\square\)

## 3. Exercises

**3.1** (easy). Show that \(f''(0)=\dfrac{m+\gamma k}{m(m+2)}\). For \(m=9\) deduce \(f''(0)=\frac7{33}\) and
\[
F(r)=1+\tfrac12r^2+\tfrac7{264}r^4+O(r^6).
\]

**3.2** (easy). Show that \(|a^{-\gamma}-b^{-\gamma}|\le\gamma2^{\gamma+1}|a-b|\) for \(a,b\in[\frac12,\frac32]\).

**3.3** (medium). Let \(F,P\) be positive radial functions of class \(C^2\) on a ball around \(0\) in \(\mathbb R^m\), \(m\ge2\), whose profiles satisfy the radial system on \((0,\varepsilon)\) with \(y=F'>0\) there. Show that \(y(r)^m=m\int_0^r\rho^{m-1}FP^{-\gamma}\,d\rho\). (So the integral form used above is forced by the radial system.)

**3.4** (medium). Let \(m=1\), so \(k=3\) and \(\gamma=\frac43\), and suppose the solution of Proposition 2.1 extends to a solution of the radial system on an interval \((0,R)\) with \(F,P,y>0\). Show that \(R\le\sqrt{2/3}\). So in two variables this construction does not produce an entire solution, in accordance with the theorem of Trudinger and Wang quoted in [The affine maximal equation](the-affine-maximal-equation.md).

## 4. Solutions

**3.1.** Differentiating under the integral sign at \(s=0\),
\[
\begin{aligned}
Q'(0)&=m\int_0^1v^{m+1}\bigl(f'(0)-\gamma p'(0)\bigr)\,dv\\
&=\frac{m}{m+2}\Bigl(1+\frac{\gamma k}m\Bigr).
\end{aligned}
\]
Since \(Q=q^m\) and \(q(0)=1\), \(q'(0)=Q'(0)/m=\frac{m+\gamma k}{m(m+2)}\), and \(f''=q'\). For \(m=9\), \(\gamma k=12\) and \(f''(0)=\frac{21}{99}=\frac7{33}\). By Taylor's theorem \(f(s)=1+s+\frac7{66}s^2+O(s^3)\), and \(s=r^2/2\) gives the expansion.

**3.2.** The derivative of \(a^{-\gamma}\) is \(-\gamma a^{-\gamma-1}\), of absolute value at most \(\gamma2^{\gamma+1}\) on \([\frac12,\frac32]\); apply the mean value theorem.

**3.3.** A radial function of class \(C^1\) has \(\nabla F(0)=0\) (its gradient at \(0\) is invariant under all rotations), so \(y(r)\to0\) as \(r\to0\). On \((0,\varepsilon)\), \((y^m)'=my^{m-1}y'=mr^{m-1}FP^{-\gamma}\). Integrate over \([r_0,r]\) and let \(r_0\to0\).

**3.4.** For \(m=1\) the factor \(y^{m-1}\) is \(1\), and the second equation reads \(P''=-3P^{-1/3}<0\). Near \(0\), \(P'(r)=rp'(r^2/2)\), so \(P'(0)=0\), and \(P'(r)=\int_0^rP''<0\) for \(0<r<R\). Hence \(P\le1\) on \([0,R)\), so \(P^{-1/3}\ge1\) and \(P''\le-3\). Integrating twice from \(0\) gives \(P'(r)\le-3r\) and \(P(r)\le1-\frac32r^2\) for \(0<r<R\). If \(R>\sqrt{2/3}\), this gives \(P(\sqrt{2/3})\le0\), contradicting \(P>0\).

## References

- [OpenAI-AM] OpenAI, *A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten*, OpenAI Math Release preprint, 5 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026
- [Lebl] J. Lebl, *Basic Analysis I and II*, version 6.3; the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/
