# Exponentials, angles and the exact period

*Original programme exposition by GPT-6 Astra (OpenAI), Ultra, October 2026. CC0-1.0.*

This prerequisite proves the scalar facts about exponentials and angles used in the [complex-analysis lesson](scalar-complex-programme.md), its [closed-boundary supplement](scalar-complex-boundaries.md), and [polar integration](scalar-product-integration.md#pi6-polar-integration-with-its-exceptional-set). Read it before those arguments. The only analytic input is [scalar integration, Sections 0 and 6](scalar-integration-programme.md): completeness of the real field, interval compactness, the real mean value theorem, and the fundamental theorem and oriented substitution for continuous integrands. We do not use a complex contour theorem, a spectral theorem or polar integration to construct the angle.

## EF1. A series and its derivative

For a complex number \(z\), define
\[
E(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}.
\tag{EF.1}
\]
This converges absolutely, uniformly for \(|z|\leq M\), for every finite \(M\): once \(n+1\geq2M\), successive majorants \(M^n/n!\) have ratio at most \(1/2\). A finite initial sum and a geometric tail suffice; no power-series theorem is assumed.

The same reasoning permits multiplication of two such series. More explicitly, the sum of absolute values of their products is bounded by the product of the two convergent nonnegative sums. Terms omitted by a sufficiently large finite square have arbitrarily small total absolute value. We may therefore regroup by the finitely many pairs with a fixed sum of indices. The finite binomial theorem gives
\[
\begin{gathered}
E(z+w)=E(z)E(w),\\
E(0)=1,\\
E(-z)=E(z)^{-1},\\
E(\bar z)=\overline{E(z)}.
\end{gathered}
\tag{EF.2}
\]

We also prove differentiability directly. If \(|z|,|w|\leq M\) and \(z\ne w\), factoring differences of powers twice gives, for \(n\geq2\),
\[
\begin{gathered}
\left|\frac{z^n-w^n}{z-w}-nw^{n-1}\right|\\
\leq \frac{n(n-1)}2M^{n-2}|z-w|.
\end{gathered}
\]
The constant term contributes zero to the difference quotient, and the linear term has zero remainder. Summing the displayed inequality after division by \(n!\) gives
\[
\begin{gathered}
\left|\frac{E(z)-E(w)}{z-w}-E(w)\right|\\
\leq \frac{|z-w|}{2}\sum_{m\geq0}\frac{M^m}{m!}.
\end{gathered}
\tag{EF.3}
\]
Consequently \(E\) is complex differentiable everywhere, with \(E'=E\). Uniform convergence on each disk proves continuity independently. These arguments also justify its derivatives along real paths by the chain rule proved in the preceding integration lesson.

For real \(x\), the series is real, and \(E(x)=E(x/2)^2>0\) by nonvanishing in (EF.2). Since its derivative is positive, the real mean value theorem makes it strictly increasing. For \(x\geq0\), its nonnegative series gives \(E(x)\geq1+x\); thus it tends to infinity at the positive end, and (EF.2) makes it tend to zero at the negative end. It follows that \(E:\mathbb R\to(0,\infty)\) is a continuous increasing bijection. Here the intermediate-value implication follows from real completeness: take the supremum of points below a proposed intermediate value and use continuity to rule out either strict inequality at that supremum. We write \(e^z=E(z)\), and write \(\log\) for the inverse of its real restriction. This is the same series and inverse used in QF-08.

## EF2. Sine and cosine before choosing a period

For real \(t\), put
\[
\begin{gathered}
c(t)=\operatorname{Re}E(it),\\
s(t)=\operatorname{Im}E(it).
\end{gathered}
\]
Conjugation and multiplication in (EF.2) give
\[
\begin{gathered}
|E(it)|=1,\\
c(t)^2+s(t)^2=1,\\
c(-t)=c(t),\\
s(-t)=-s(t).
\end{gathered}
\tag{EF.4}
\]
Indeed, the squared modulus is \(E(it)E(-it)=1\). Real differentiation using (EF.3) gives
\[
\begin{gathered}
c'=-s,\qquad s'=c,\\
c(0)=1,\qquad s(0)=0.
\end{gathered}
\tag{EF.5}
\]
Multiplying \(E(it)E(iu)\) gives the addition identities for \(c\) and \(s\). In particular
\(c(2t)=c(t)^2-s(t)^2\), \(s(2t)=2s(t)c(t)\), and
\(c(t)^2=(1+c(2t))/2\). No period has yet been assumed.

## EF3. Constructing a quarter turn by an integral

Define
\[
\begin{gathered}
a(x)=\int_0^x\frac{du}{1+u^2}\\
(x\in\mathbb R).
\end{gathered}
\tag{EF.6}
\]
The earlier fundamental theorem gives \(a'(x)=1/(1+x^2)>0\). Hence \(a\) is continuous and strictly increasing; substitution \(u\mapsto-u\) gives oddness. For \(x\geq1\),
\[
\begin{gathered}
0<a(1)\leq a(x)\\
\leq1+\int_1^x u^{-2}\,du\\
=2-1/x<2.
\end{gathered}
\]
Thus \(\alpha=\sup_{x\geq0}a(x)\) exists, is positive, and is the limit as \(x\to\infty\). Oddness gives the negative-end limit \(-\alpha\). Strict increase shows that neither endpoint is attained. Continuity and the supremum argument from EF1 therefore identify the range as \((-\alpha,\alpha)\).

For positive \(x\), direct differentiation gives
\[
\frac{d}{dx}\bigl(a(x)+a(1/x)\bigr)=0.
\]
The mean value theorem makes the sum constant. Letting \(x\to\infty\) identifies that constant as \(\alpha\), and setting \(x=1\) yields
\[
\begin{gathered}
\alpha=2a(1),\\
\pi=2\alpha=4a(1).
\end{gathered}
\tag{EF.7}
\]
This defines \(\pi\); the circle and length interpretation will follow from the construction.

To find the corresponding point on the circle, set
\(v(x)=(1+ix)/(1+x^2)^{1/2}\). Differentiating gives
\(v'(x)=i v(x)/(1+x^2)\). The square-root differentiation here follows directly from
\((\sqrt b-\sqrt a)/(b-a)=1/(\sqrt b+\sqrt a)\) for positive \(a,b\); product and quotient rules follow by subtracting the products and taking limits. Existence of the nonnegative real square root follows by taking the supremum of the nonnegative numbers whose squares are at most its argument. We use no implicit inverse-function theorem.

The real derivative of \(E(-ia(x))v(x)\) is consequently zero. Apply the real mean value theorem to its real and imaginary parts. Its value at zero is one, so
\[
E(ia(x))=\frac{1+ix}{\sqrt{1+x^2}}.
\tag{EF.8}
\]
Let \(x\to\infty\). Continuity of \(E\) gives
\[
\begin{gathered}
E(i\alpha)=i,\\
E(i\pi)=-1,\\
E(2\pi i)=1.
\end{gathered}
\tag{EF.9}
\]
The latter two equalities are multiplication identities, not assumptions about angles.

## EF4. The exact exponential kernel and the whole circle

Every \(t\in(0,\alpha)\) is \(a(x)\) for a unique positive \(x\). Formula (EF.8) shows that \(E(it)\) lies in the open first quadrant. It covers that arc exactly once: if \(u+iv\) has \(u,v>0\) and \(u^2+v^2=1\), put \(x=v/u\) in (EF.8); then \(u=1/\sqrt{1+x^2}\), \(v=x/\sqrt{1+x^2}\).

For \(q=0,1,2,3\) and \(0<t<\alpha\), (EF.2) and (EF.9) give
\(E(i(q\alpha+t))=i^q E(it)\). The four intervals thus cover the four open quadrants, once each, and the four endpoints give \(1,i,-1,-i\). Since \(4\alpha=2\pi\), the map
\[
\begin{gathered}
{}[0,2\pi)\longrightarrow\mathbb T,\\
t\longmapsto E(it),\\
\mathbb T=\{z\in\mathbb C:|z|=1\}.
\end{gathered}
\tag{EF.10}
\]
is a bijection. It takes the value one only at zero on this interval. Multiplication by \(E(2\pi i)=1\) supplies the period on all of \(\mathbb R\). Given any real \(t\), choose an integer \(n\) with \(t-2\pi n\in[0,2\pi)\); the Archimedean property of the complete real field guarantees such an integer. Hence
\[
\begin{gathered}
E(it)=1\\
\Longleftrightarrow\quad t\in2\pi\mathbb Z.
\end{gathered}
\tag{EF.11}
\]

For \(z=x+iy\), (EF.2) and (EF.4) give \(|E(z)|=E(x)\). Strict increase of the real exponential shows that \(E(z)=1\) forces \(x=0\). Equation (EF.11) then proves the full complex assertion
\[
\begin{gathered}
E(z)=1\\
\Longleftrightarrow\quad z\in2\pi i\mathbb Z.
\end{gathered}
\tag{EF.12}
\]
In particular \(E(z)=E(w)\) exactly when \(z-w\in2\pi i\mathbb Z\). This is the precise fact used in the index calculation of the complex-analysis lesson.

## EF5. Radians, the inverse angle and polar coordinates

We now write \(\cos t=c(t)\), \(\sin t=s(t)\), and \(\arctan x=a(x)\). The circle path \(t\mapsto E(it)\) has derivative \(iE(it)\) of modulus one. Its length on a parameter interval is therefore the length of that interval. Thus this parametrization measures angle in radians, and a full turn has length \(2\pi\). The circle of radius \(R\) has length \(2\pi R\).

On \((-\pi/2,\pi/2)=(-\alpha,\alpha)\), formula (EF.8) shows that cosine is positive and sine divided by cosine runs bijectively over the real line. Thus \(a\) is the inverse tangent on that interval. At the endpoints the limiting circle values are \(-i,i\); consequently sine maps \([-\pi/2,\pi/2]\) increasingly onto \([-1,1]\), with nonnegative cosine. These are the endpoint and sign facts used in the disk-area substitution. Oddness and (EF.7) also give the exact square-index integral
\[
\int_{-1}^1\frac{dt}{1+t^2}
=2a(1)=\frac\pi2.
\tag{EF.13}
\]

Squaring (EF.8) proves the half-angle identities with their actual branch:
\[
\begin{gathered}
\cos(2a(u))=\frac{1-u^2}{1+u^2},\\
\sin(2a(u))=\frac{2u}{1+u^2},\\
2a(u)\in(-\pi,\pi).
\end{gathered}
\tag{EF.14}
\]
If \((x,y)\) is outside the ray \(\{(x,0):x\leq0\}\), put
\(r=\sqrt{x^2+y^2}\). Then \(r>0\) and \(r+x>0\). Substitute \(u=y/(r+x)\) in (EF.14). The identity \(x^2+y^2=r^2\) gives cosine \(x/r\) and sine \(y/r\). Uniqueness in (EF.10), using the half-open period and excluding its negative-real endpoint, makes
\[
\begin{gathered}
(x,y)\longmapsto(r,\theta),\\
r=\sqrt{x^2+y^2},\\
\theta=2a\!\left(\frac{y}{r+x}\right)
\end{gathered}
\tag{EF.15}
\]
the inverse of \((r,\theta)\mapsto(r\cos\theta,r\sin\theta)\) on
\((0,\infty)\times(-\pi,\pi)\). Both maps are continuous by the displayed formulas. This proves the homeomorphism used in polar integration, including its excluded ray, before any assertion about planar area.

## EF6. The zeros used in contour kernels

For complex \(z\), define
\[
\begin{gathered}
\sin z=\frac{E(iz)-E(-iz)}{2i},\\
\cos z=\frac{E(iz)+E(-iz)}2.
\end{gathered}
\]
They agree with EF2 on the real line, and EF1 proves that they are holomorphic with derivatives cosine and minus sine. Nonvanishing of \(E\) and (EF.12) give
\[
\begin{gathered}
\sin(\pi z)=0\\
\Longleftrightarrow\quad z\in\mathbb Z,\\
E(\pi z)-E(-\pi z)=0\\
\Longleftrightarrow\quad z\in i\mathbb Z.
\end{gathered}
\tag{EF.16}
\]
Indeed, the first equation is \(E(2\pi iz)=1\), and the second is \(E(2\pi z)=1\). The derivative of the first denominator at zero is \(\pi\), and the derivative of the second at zero is \(2\pi\), by EF1. At every other listed zero, multiplication by the corresponding nonzero exponential gives the same nonzero derivative up to a sign. Thus the zeros are simple. These facts justify exactly the pole locations and normalizations of SC5 and IK1; the contour integrals themselves are proved in those later units.
