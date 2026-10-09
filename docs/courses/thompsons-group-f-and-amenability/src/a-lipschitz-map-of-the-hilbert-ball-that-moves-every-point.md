# A Lipschitz map of the Hilbert ball that moves every point

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Brouwer's fixed-point theorem, every continuous map of the closed unit ball of \(\mathbb R^n\) into itself has a fixed point. In an infinite-dimensional Hilbert space this fails: Kakutani gave a continuous map of the closed unit ball of \(\ell^2\) into itself without fixed points [Ka] (Exercise 7.1). His map still has points that it moves arbitrarily little. Benyamini and Sternfeld proved much more: the closed unit ball of every infinite-dimensional normed space carries a Lipschitz map into itself that moves every point by at least a fixed positive distance [BS]. This lesson constructs such a map on a concrete Hilbert space, following the explicit construction in [OpenAI-F, Appendix A]. The lesson [Thompson's group F is not amenable](thompsons-group-f-is-not-amenable.md) uses it.

**Theorem 5.1.** Let \(H=L^2([0,1];\mathbb R^2)\) and let \(B\) be its closed unit ball. There is a Lipschitz map \(f:B\to B\) with
\[
\|f(x)\|=1\quad\text{and}\quad\|f(x)-x\|\ge\tfrac12\qquad(x\in B).
\]

*The idea.* It suffices to find a Lipschitz map \(G:B\to H\) that is bounded away from \(0\) and equals the identity on the vectors of norm at least \(\tfrac12\); then \(f=-G/\|G\|\) works. The identity itself fails only near \(0\). We pass a curve \(\gamma\) through \(0\) and move the points of a thin tube around \(\gamma\) along the curve's direction, away from \(0\). In finite dimensions this cannot work, since such a \(G\) would contradict Brouwer's theorem. The curve escapes the obstruction by running forever inside a bounded set while points with distant parameters stay uniformly apart, which is possible only in infinite dimensions (Exercise 7.4). This uniform separation lets the tube have one fixed radius along the whole curve.

We use Brouwer's fixed-point theorem only in this introduction and in Section 6, from the core course [Algebraic Topology (D60)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), Lecture 30, Theorem 30.1. Otherwise the lesson uses the definition of a real Hilbert space, the mean value theorem of one-variable calculus, and the Bolzano–Weierstrass theorem.

## 1. Curves in a real Hilbert space

Let \(H\) be a real Hilbert space. A map \(\gamma:\mathbb R\to H\) is *differentiable* at \(t\) if \((\gamma(t+h)-\gamma(t))/h\) converges in norm as \(h\to0\); the limit is \(\gamma'(t)\). Products of differentiable real functions and differentiable \(H\)-valued maps, and compositions of differentiable \(H\)-valued maps with differentiable real functions, are differentiable with the usual formulas; the proofs are the one-variable ones.

**Lemma 1.1.** Let \(\gamma:\mathbb R\to H\) be differentiable.

(a) If \(\|\gamma'(\tau)-\gamma'(s)\|\le K|\tau-s|\) for all \(\tau,s\), then \(\|\gamma(t)-\gamma(s)-(t-s)\gamma'(s)\|\le\frac K2(t-s)^2\) for all \(s,t\).

(b) If \(\|\gamma'(\tau)\|\le M\) for all \(\tau\), then \(\gamma\) is \(M\)-Lipschitz.

(c) For \(x\in H\), the function \(\varphi(t)=\|x-\gamma(t)\|^2\) is differentiable, with \(\varphi'(t)=-2\langle x-\gamma(t),\gamma'(t)\rangle\).

**Proof.** (a) Fix \(s\neq t\) and put \(w=\gamma(t)-\gamma(s)-(t-s)\gamma'(s)\). If \(w\neq0\), let \(y=w/\|w\|\) and \(\psi(\tau)=\langle\gamma(\tau)-\gamma(s)-(\tau-s)\gamma'(s),y\rangle\). Then \(\psi\) is a differentiable real function with \(\psi(s)=0\), \(\psi(t)=\|w\|\), and \(|\psi'(\tau)|=|\langle\gamma'(\tau)-\gamma'(s),y\rangle|\le K|\tau-s|\). The functions \(\frac K2(\tau-s)^2\pm\psi(\tau)\) vanish at \(\tau=s\) and are monotone between \(s\) and \(t\), nondecreasing if \(s<t\) and nonincreasing if \(t<s\), by the mean value theorem; so they are nonnegative at \(\tau=t\), and \(\|w\|=\psi(t)\le\frac K2(t-s)^2\).

(b) The same argument with \(\psi(\tau)=\langle\gamma(\tau)-\gamma(s),y\rangle\), \(y\) the unit vector in the direction of \(\gamma(t)-\gamma(s)\), and \(|\psi'|\le M\) gives \(\|\gamma(t)-\gamma(s)\|\le M|t-s|\).

(c) \(\varphi(t+h)-\varphi(t)=-2\langle x-\gamma(t),\gamma(t+h)-\gamma(t)\rangle+\|\gamma(t+h)-\gamma(t)\|^2\). Divide by \(h\) and let \(h\to0\); the last term divided by \(h\) tends to \(0\) because \((\gamma(t+h)-\gamma(t))/h\) stays bounded. \(\square\)

**Lemma 1.2.** If \(y,z\in H\) and \(\|y\|,\|z\|\ge r>0\), then \(\bigl\|\frac y{\|y\|}-\frac z{\|z\|}\bigr\|\le\frac2r\|y-z\|\).

**Proof.**
\[
\frac y{\|y\|}-\frac z{\|z\|}=\frac{y-z}{\|y\|}+\frac{z\,(\|z\|-\|y\|)}{\|y\|\,\|z\|},
\]
and both terms have norm at most \(\|y-z\|/\|y\|\le\|y-z\|/r\). \(\square\)

We also use the product estimate \(\|\alpha(x)\beta(x)-\alpha(y)\beta(y)\|\le\|\alpha(x)-\alpha(y)\|\,\|\beta(x)\|+\|\alpha(y)\|\,\|\beta(x)-\beta(y)\|\), for scalar, vector or operator valued \(\alpha,\beta\): a product of bounded Lipschitz maps is Lipschitz.

## 2. A curve with a bounded tail

From now on \(H=L^2([0,1];\mathbb R^2)\) with \(\langle x,y\rangle=\int_0^1x(w)\cdot y(w)\,dw\). Let \(J(\xi_1,\xi_2)=(-\xi_2,\xi_1)\) be the rotation by a right angle in \(\mathbb R^2\). For \(\phi\in\mathbb R\) define \(E(\phi)\in H\) by
\[
E(\phi)(w)=(\cos\phi w,\ \sin\phi w)\qquad(0\le w\le1).
\]
Put \(\operatorname{sinc}(0)=1\) and \(\operatorname{sinc}(q)=\sin q/q\) for \(q\neq0\). Then \(|\operatorname{sinc}(q)|<1\) for \(q\neq0\), because \(|\sin q|<|q|\), and \(|\operatorname{sinc}(q)|\le1/|q|\).

**Lemma 2.1.** (a) \(\|E(\phi)\|=1\) and \(\langle E(\phi),E(\psi)\rangle=\operatorname{sinc}(\psi-\phi)\).

(b) \(E\) is differentiable, with \(E'(\phi)(w)=w\,J\bigl(E(\phi)(w)\bigr)\). Moreover \(\|E'(\phi)\|^2=\frac13\), \(\langle E'(\phi),E(\phi)\rangle=0\), \(\|E(\phi)-E(\psi)\|\le|\phi-\psi|/\sqrt3\) and \(\|E'(\phi)-E'(\psi)\|\le|\phi-\psi|\).

**Proof.** (a) Pointwise, \(\cos\phi w\cos\psi w+\sin\phi w\sin\psi w=\cos((\psi-\phi)w)\), and \(\int_0^1\cos(qw)\,dw=\operatorname{sinc}(q)\).

(b) Fix \(w\in[0,1]\) and write \(e_w(\phi)=E(\phi)(w)\in\mathbb R^2\). This is a point moving on the unit circle with angle \(\phi w\), so \(|e_w(\phi)-e_w(\psi)|\le w|\phi-\psi|\), and its derivative \(wJe_w(\phi)\) satisfies \(|wJe_w(\phi)-wJe_w(\psi)|\le w^2|\phi-\psi|\). Lemma 1.1(a) in \(\mathbb R^2\) gives \(|e_w(\phi+h)-e_w(\phi)-h\,wJe_w(\phi)|\le\frac{w^2h^2}2\le\frac{h^2}2\). Squaring and integrating over \(w\),
\[
\bigl\|E(\phi+h)-E(\phi)-h\,E'(\phi)\bigr\|\le\tfrac{h^2}2,
\]
which proves differentiability. The remaining statements follow by integrating the pointwise facts \(|wJe_w|^2=w^2\), \(Je_w\cdot e_w=0\), \(|e_w(\phi)-e_w(\psi)|^2\le w^2(\phi-\psi)^2\) and \(|wJe_w(\phi)-wJe_w(\psi)|^2\le w^4(\phi-\psi)^2\le(\phi-\psi)^2\). \(\square\)

Define real functions
\[
a(t)=\begin{cases}t/8,&t\le2,\\ \frac5{16}-\frac{(3-t)^2}{16},&2\le t\le3,\\ \frac5{16},&t\ge3,\end{cases}\qquad
\theta(t)=\begin{cases}0,&t\le1,\\ \frac{(t-1)^2}2,&1\le t\le2,\\ t-\frac32,&t\ge2.\end{cases}
\]
The formulas agree at the junctions. Both functions are continuously differentiable, with
\[
a'(t)=\begin{cases}\frac18,&t\le2,\\ \frac{3-t}8,&2\le t\le3,\\ 0,&t\ge3,\end{cases}\qquad
\theta'(t)=\begin{cases}0,&t\le1,\\ t-1,&1\le t\le2,\\ 1,&t\ge2;\end{cases}
\]
\(a'\) is \(\frac18\)-Lipschitz and \(\theta'\) is \(1\)-Lipschitz. The function \(a\) is nondecreasing, negative on \((-\infty,0)\), positive on \((0,\infty)\), at most \(\frac5{16}\) everywhere, and \(\frac18\le a(t)\le\frac5{16}\) for \(t\ge1\). The function \(\theta\) vanishes on \((-\infty,1]\), is strictly increasing on \([1,\infty)\), and \(0\le\theta'\le1\).

Put
\[
v(t)=E(\theta(t)),\qquad\gamma(t)=a(t)\,v(t).
\]
For \(t\le1\), \(v(t)=v_0\), the constant function \((1,0)\), and \(\gamma(t)=\frac t8v_0\) runs along a straight line through \(\gamma(0)=0\). For \(t\ge1\) the curve stays in the ball of radius \(\frac5{16}\), while its direction \(v(t)\) keeps turning: \(\langle v(s),v(t)\rangle=\operatorname{sinc}(\theta(t)-\theta(s))\) tends to \(0\) as \(t\to\infty\).

**Lemma 2.2.** (a) \(\gamma\) is differentiable, \(\gamma'(t)=a'(t)v(t)+a(t)\theta'(t)E'(\theta(t))\), and
\[
\|\gamma'(t)\|^2=a'(t)^2+\tfrac13a(t)^2\theta'(t)^2.
\]
(b) \(\inf_t\|\gamma'(t)\|=\frac18\) and \(\sup_t\|\gamma'(t)\|\le\frac14\).

(c) \(\gamma'\) is \(1\)-Lipschitz.

(d) The unit tangent \(u(t)=\gamma'(t)/\|\gamma'(t)\|\) is \(16\)-Lipschitz, \(v\) is \(\frac1{\sqrt3}\)-Lipschitz, \(\langle u(t),v(t)\rangle=a'(t)/\|\gamma'(t)\|\ge0\), and \(u(t)=v(t)=v_0\) for \(t\le1\).

**Proof.** (a) The derivative comes from the product and chain rules and Lemma 2.1(b); the norm from \(\|v(t)\|=1\), \(\|E'\|^2=\frac13\) and \(\langle E'(\theta(t)),v(t)\rangle=0\).

(b) For \(t\le2\), \(a'(t)=\frac18\), so \(\|\gamma'(t)\|\ge\frac18\), with equality for \(t\le1\), where \(\theta'(t)=0\). For \(t\ge2\), \(a(t)\ge\frac14\) and \(\theta'(t)=1\), so \(\|\gamma'(t)\|^2\ge\frac1{48}>\frac1{64}\). For the upper bound: for \(t\le1\), \(\|\gamma'(t)\|=\frac18\); for \(t\ge1\), \(\|\gamma'(t)\|^2\le\frac1{64}+\frac13\cdot\frac{25}{256}<\frac1{16}\).

(c) On \((-\infty,1]\), \(\gamma'=\frac18v_0\) is constant. On \([1,\infty)\) write \(\gamma'=a'\cdot(E\circ\theta)+(a\theta')\cdot(E'\circ\theta)\). There \(|a'|\le\frac18\) with Lipschitz constant \(\frac18\); \(|a\theta'|\le\frac5{16}\) with Lipschitz constant at most \(\frac18\cdot1+\frac5{16}\cdot1=\frac7{16}\); \(\theta\) is \(1\)-Lipschitz; so by Lemma 2.1(b), \(E\circ\theta\) has norm \(1\) and Lipschitz constant \(\frac1{\sqrt3}\), and \(E'\circ\theta\) has norm \(\frac1{\sqrt3}\) and Lipschitz constant \(1\). The product estimate gives the Lipschitz constant
\[
\tfrac18+\tfrac18\cdot\tfrac1{\sqrt3}+\tfrac7{16}\cdot\tfrac1{\sqrt3}+\tfrac5{16}<1
\]
on \([1,\infty)\). A map that is \(1\)-Lipschitz on \((-\infty,1]\) and on \([1,\infty)\) is \(1\)-Lipschitz on \(\mathbb R\): split a pair \(s\le1\le t\) at \(1\).

(d) Lemma 1.2 with \(r=\frac18\) and part (c) give \(\|u(t)-u(s)\|\le16|t-s|\). The map \(v=E\circ\theta\) is constant on \((-\infty,1]\) and \(\frac1{\sqrt3}\)-Lipschitz on \([1,\infty)\). Next, \(\langle\gamma'(t),v(t)\rangle=a'(t)\ge0\) by (a). For \(t\le1\), \(\gamma'(t)=\frac18v_0\), so \(u(t)=v_0=v(t)\). \(\square\)

**Lemma 2.3.** The curve \(\gamma\) is injective, and for every \(d>0\)
\[
\sigma(d)=\inf\{\|\gamma(t)-\gamma(s)\|:|t-s|\ge d\}>0.\tag{2.1}
\]

**Proof.** *Injectivity.* Let \(s<t\) with \(\gamma(s)=\gamma(t)\). If \(\theta(s)\neq\theta(t)\), the unit vectors \(v(s),v(t)\) are not proportional, since \(|\langle v(s),v(t)\rangle|<1\) by Lemma 2.1(a); then \(a(s)v(s)=a(t)v(t)\) forces \(a(s)=a(t)=0\), so \(s=t=0\), a contradiction. If \(\theta(s)=\theta(t)\), then \(s<t\le1\), because \(\theta\) is strictly increasing on \([1,\infty)\) and \(\theta>0\) on \((1,\infty)\); then \(v(s)=v(t)=v_0\) and \(a(s)=s/8\neq t/8=a(t)\), a contradiction.

*Separation.* Suppose \(\sigma(d)=0\). Choose \(s_n<t_n\) with \(t_n-s_n\ge d\) and \(\|\gamma(t_n)-\gamma(s_n)\|\to0\). Passing to a subsequence, \(s_n\to s\) and \(t_n\to t\) in \([-\infty,\infty]\), with \(s\le t\).

- If \(s,t\) are finite, then \(t-s\ge d\) and \(\gamma(t)=\gamma(s)\) by continuity, contradicting injectivity.
- If \(s=t=-\infty\), then eventually \(t_n\le1\) and \(\|\gamma(t_n)-\gamma(s_n)\|=(t_n-s_n)/8\ge d/8\).
- If \(s=-\infty<t\), then \(t_n\) is bounded below, so \(\|\gamma(t_n)\|=|a(t_n)|\) stays bounded, while \(\|\gamma(s_n)\|=|s_n|/8\to\infty\).
- If \(s\) is finite and \(t=\infty\), then \(\theta(t_n)-\theta(s_n)\to\infty\), so \(\langle v(s_n),v(t_n)\rangle\to0\), and
\[
\|\gamma(t_n)-\gamma(s_n)\|^2=a(t_n)^2+a(s_n)^2-2a(t_n)a(s_n)\langle v(t_n),v(s_n)\rangle\to\bigl(\tfrac5{16}\bigr)^2+a(s)^2>0.
\]
- If \(s=t=\infty\), then eventually \(s_n\ge3\), where \(a=\frac5{16}\) and \(\theta(\tau)=\tau-\frac32\), so
\[
\|\gamma(t_n)-\gamma(s_n)\|^2=2\bigl(\tfrac5{16}\bigr)^2\bigl(1-\operatorname{sinc}(t_n-s_n)\bigr).
\]
The function \(\operatorname{sinc}\) is continuous and below \(1\) on the compact interval \([d,\max(d,2)]\), and at most \(\frac12\) on \([2,\infty)\); so \(\sup_{q\ge d}\operatorname{sinc}(q)<1\), and these distances stay away from \(0\).

Every case contradicts \(\|\gamma(t_n)-\gamma(s_n)\|\to0\). \(\square\)

Write \(c=\frac18\) for the minimal speed and put \(d=\frac c2\). For \(|t-s|\le d\), Lemma 1.1(a), with the Lipschitz constant \(1\) of \(\gamma'\), gives \(\gamma(t)-\gamma(s)=(t-s)\gamma'(s)+w\) with \(\|w\|\le\frac12(t-s)^2\le\frac d2|t-s|=\frac c4|t-s|\). Since \(\langle\gamma'(s),u(s)\rangle=\|\gamma'(s)\|\ge c\),
\[
\bigl|\langle\gamma(t)-\gamma(s),u(s)\rangle\bigr|\ge|t-s|\,\|\gamma'(s)\|-\|w\|\ge\tfrac{3c}4|t-s|\qquad(|t-s|\le d).\tag{2.2}
\]

## 3. The tube around the curve

For \(x\in H\) let \(r(x)=\inf_{t\in\mathbb R}\|x-\gamma(t)\|\) be the distance from \(x\) to the curve. It is \(1\)-Lipschitz, as an infimum of \(1\)-Lipschitz functions, and \(r(x)\le\|x-\gamma(0)\|=\|x\|\). Fix a radius \(\rho\) with
\[
0<\rho<\tfrac1{32},\qquad4\rho<\sigma(d),\qquad16\rho<\tfrac c4,\tag{3.1}
\]
where \(d=\frac c2=\frac1{16}\) is the number fixed before (2.2) and \(16\) is the Lipschitz constant of \(u\) from Lemma 2.2(d). Let \(U=\{x\in H:r(x)<\rho\}\).

**Lemma 3.1.** (a) Every \(x\in U\) has exactly one parameter \(t(x)\) with \(\|x-\gamma(t(x))\|=r(x)\).

(b) The residual \(e(x)=x-\gamma(t(x))\) satisfies \(\|e(x)\|=r(x)<\rho\) and \(\langle e(x),u(t(x))\rangle=0\).

(c) If \(x,y\in U\) and \(\|x-y\|<\rho\), then \(|t(x)-t(y)|\le16\|x-y\|\) and \(\|e(x)-e(y)\|\le5\|x-y\|\).

(d) If \(x=\gamma(t)+e\) with \(e\perp u(t)\) and \(\|e\|<\rho\), then \(x\in U\), \(t(x)=t\) and \(e(x)=e\).

**Proof.** *Existence.* Let \(\|x-\gamma(t_n)\|\to r(x)\). For \(n\ge N\) we have \(\|x-\gamma(t_n)\|<\rho\), so \(\|\gamma(t_n)-\gamma(t_N)\|<2\rho<\sigma(d)\) and \(|t_n-t_N|<d\). A subsequence of \((t_n)\) converges in \([t_N-d,t_N+d]\), and by continuity its limit \(t\) satisfies \(\|x-\gamma(t)\|=r(x)\).

*Orthogonality.* At such a minimizing \(t\), the function \(\varphi(\tau)=\|x-\gamma(\tau)\|^2\) has a minimum, so \(\varphi'(t)=0\), and Lemma 1.1(c) gives \(\langle x-\gamma(t),u(t)\rangle=0\).

*The estimate.* Let \(x,y\in H\) with \(\|x-y\|<\rho\), and suppose \(x=\gamma(t)+e_t\) and \(y=\gamma(s)+e_s\) with \(\|e_t\|,\|e_s\|<\rho\), \(e_t\perp u(t)\) and \(e_s\perp u(s)\). This holds for minimizing parameters \(t,s\) of points \(x,y\in U\), by the orthogonality just proved. Then \(\|\gamma(t)-\gamma(s)\|<3\rho<\sigma(d)\), so \(|t-s|<d\). Since \(\langle e_s,u(s)\rangle=0\) and \(\langle e_t,u(s)\rangle=\langle e_t,u(s)-u(t)\rangle\), (2.2) gives
\[
\|x-y\|\ge|\langle x-y,u(s)\rangle|\ge\bigl|\langle\gamma(t)-\gamma(s),u(s)\rangle\bigr|-\|e_t\|\,\|u(s)-u(t)\|\ge\bigl(\tfrac{3c}4-16\rho\bigr)|t-s|\ge\tfrac c2|t-s|.
\]
Taking \(y=x\) and two minimizing parameters shows that the minimizing parameter is unique, which proves (a) and then (b). Taking \(y=x\), the given decomposition \(x=\gamma(t)+e\), and the minimizing one proves (d); note that \(x\in U\) because \(r(x)\le\|e\|<\rho\). For general \(x,y\) the inequality reads \(|t(x)-t(y)|\le\frac2c\|x-y\|=16\|x-y\|\). Finally \(e(x)-e(y)=(x-y)-(\gamma(t(x))-\gamma(t(y)))\), and \(\gamma\) is \(\frac14\)-Lipschitz by Lemma 1.1(b) and Lemma 2.2(b); so \(\|e(x)-e(y)\|\le(1+16\cdot\frac14)\|x-y\|\). \(\square\)

## 4. Rotations carrying the tangent to the direction

**Lemma 4.1.** Let \(u,v\in H\) be unit vectors with \(\kappa=\langle u,v\rangle\ge0\). Define operators on \(H\) by
\[
Ah=\langle u,h\rangle v-\langle v,h\rangle u,\qquad R=1+A+\frac{A^2}{1+\kappa}.
\]
Then \(R\) is orthogonal (\(R^*R=RR^*=1\)) and \(Ru=v\). If \((u',v')\) is another such pair, with operators \(A',R'\), then \(\|R-R'\|\le14(\|u-u'\|+\|v-v'\|)\).

**Proof.** The operator \(A\) satisfies \(\langle Ah,k\rangle=-\langle h,Ak\rangle\), maps \(H\) into \(V=\operatorname{span}\{u,v\}\) and vanishes on \(V^\perp\). If \(u,v\) are linearly dependent, then \(v=u\), because \(\kappa\ge0\); so \(A=0\) and \(R=1\). Otherwise \(Au=v-\kappa u\) and \(Av=\kappa v-u\), so \(A^2u=-(1-\kappa^2)u\) and \(A^2v=-(1-\kappa^2)v\), and \(R\) acts on \(V\) as \(\kappa+A\). There \((\kappa+A)^*(\kappa+A)=\kappa^2-A^2=1\). So \(R\) is an isometry of the finite-dimensional space \(V\) onto itself and the identity on \(V^\perp\); hence it is orthogonal. Also \(Ru=\kappa u+v-\kappa u=v\).

For the estimate put \(\Delta=\|u-u'\|+\|v-v'\|\). Each of the two rank-one terms of \(A-A'\) has norm at most \(\Delta\), so \(\|A-A'\|\le2\Delta\); \(\|A\|,\|A'\|\le2\); \(\|A^2-A'^2\|\le4\|A-A'\|\); and \(\bigl|\frac1{1+\kappa}-\frac1{1+\kappa'}\bigr|\le|\kappa-\kappa'|\le\Delta\). Hence
\[
\|R-R'\|\le\|A-A'\|+\|A^2-A'^2\|+\|A'^2\|\,\Delta\le2\Delta+8\Delta+4\Delta.\qquad\square
\]

Let \(R_t\) be the operator of Lemma 4.1 for the pair \((u(t),v(t))\), which is allowed by Lemma 2.2(d). Then \(R_tu(t)=v(t)\), \(R_t=1\) for \(t\le1\), and \(t\mapsto R_t\) is Lipschitz in operator norm, with constant at most \(14(16+\frac1{\sqrt3})\).

## 5. The map

Put \(b(t)=\min\{a(t),-\frac18\}\) and
\[
q(t)=b(t)-a(t)=-\max\{a(t)+\tfrac18,\,0\}.
\]
Then \(|q|\le\frac7{16}\), \(q\) is \(\frac18\)-Lipschitz, and \(q(t)=0\) when \(a(t)\le-\frac18\). Let \(\beta,\chi:[0,\infty)\to[0,1]\) be the continuous piecewise linear cutoffs with
\[
\beta=1\text{ on }[0,\tfrac\rho4],\quad\beta=0\text{ on }[\tfrac\rho2,\infty),\qquad\chi=1\text{ on }[0,\tfrac\rho2],\quad\chi=0\text{ on }[\rho,\infty),
\]
linear in between; \(\beta\) is \(\frac4\rho\)-Lipschitz and \(\chi\) is \(\frac2\rho\)-Lipschitz, and for \(0\le r<\rho\)
\[
\beta(r)\le\chi(r)\le\frac{2(\rho-r)}\rho.\tag{5.1}
\]
Define \(G:B\to H\) by \(G(x)=x\) if \(x\notin U\), and for \(x\in B\cap U\), with \(t=t(x)\), \(e=e(x)\), \(r=r(x)\),
\[
G(x)=x+\beta(r)\,q(t)\,v(t)+\chi(r)\,(R_t-1)\,e.\tag{5.2}
\]
Since \(x=a(t)v(t)+e\), formula (5.2) can be read as
\[
G(x)=\bigl(a(t)+\beta(r)q(t)\bigr)v(t)+\bigl((1-\chi(r))e+\chi(r)R_te\bigr).\tag{5.3}
\]
Near the core of the tube, \(\beta=\chi=1\) and \(G(x)=b(t)v(t)+R_te\): the coefficient along \(v(t)\) is replaced by \(b(t)\le-\frac18\), and the residual is turned perpendicular to \(v(t)\).

**Proof of Theorem 5.1.** *Step 1: \(\|G(x)\|\le\frac32\) on \(B\).* By (5.2), \(\|G(x)\|\le1+\frac7{16}+2\rho<\frac32\), since \(\|R_t-1\|\le2\) and \(\|e\|<\rho<\frac1{32}\).

*Step 2: \(G\) is Lipschitz on \(B\).* Let \(x,y\in B\). If neither lies in \(U\), then \(\|G(x)-G(y)\|=\|x-y\|\). If \(\|x-y\|\ge\rho\), then \(\|G(x)-G(y)\|\le3\le\frac3\rho\|x-y\|\) by Step 1.

Let \(x\in U\), \(y\notin U\) and \(\|x-y\|<\rho\). By (5.2), (5.1), \(|q|\le\frac7{16}\), \(\|R_t-1\|\le2\) and \(\|e\|\le\rho\),
\[
\|G(x)-x\|\le\frac{2(\rho-r(x))}\rho\Bigl(\frac7{16}+2\rho\Bigr)=\Bigl(\frac7{8\rho}+4\Bigr)(\rho-r(x)).
\]
Since \(r(y)\ge\rho\) and \(r\) is \(1\)-Lipschitz, \(\rho-r(x)\le\|x-y\|\). Hence \(\|G(x)-G(y)\|\le\|x-y\|+\|G(x)-x\|\le\bigl(5+\frac7{8\rho}\bigr)\|x-y\|\).

Let \(x,y\in U\) with \(\|x-y\|<\rho\). By Lemma 3.1(c) and the Lipschitz properties of \(r\), \(\beta\), \(\chi\), \(q\), \(v\) and \(t\mapsto R_t\), each of the functions \(\beta(r(x))\), \(\chi(r(x))\), \(q(t(x))\), \(v(t(x))\), \(R_{t(x)}\) and \(e(x)\) changes by at most a fixed constant times \(\|x-y\|\) between \(x\) and \(y\); and \(|\beta|\le1\), \(|\chi|\le1\), \(|q|\le\frac7{16}\), \(\|v\|=1\), \(\|R_{t(x)}-1\|\le2\) and \(\|e(x)\|<\rho\). The product estimate of Section 1 bounds \(\|G(x)-G(y)\|\) by a fixed constant times \(\|x-y\|\). These cases cover all pairs, so \(G\) is Lipschitz on \(B\).

*Step 3: \(\|G(x)\|\ge\frac\rho4\) on \(B\).* If \(x\notin U\), then \(\|G(x)\|=\|x\|\ge r(x)\ge\rho\). Let \(x\in U\), with \(t,e,r\) as above. The residual \(e\) is perpendicular to \(u(t)\), and \(R_t\) is orthogonal with \(R_tu(t)=v(t)\); so \(R_te\perp v(t)\) and \(\|R_te\|=r\).

- If \(r\le\frac\rho2\), then \(\chi(r)=1\) and \(G(x)=(a(t)+\beta(r)q(t))v(t)+R_te\) with \(R_te\perp v(t)\), so \(\|G(x)\|^2=(a(t)+\beta(r)q(t))^2+r^2\). If \(r\le\frac\rho4\), then \(\beta(r)=1\) and \(a(t)+q(t)=b(t)\le-\frac18\), so \(\|G(x)\|\ge\frac18>\frac\rho4\). If \(\frac\rho4\le r\le\frac\rho2\), then \(\|G(x)\|\ge r\ge\frac\rho4\).
- If \(\frac\rho2\le r<\rho\), then \(\beta(r)=0\) and \(G(x)=\gamma(t)+\bigl((1-\chi(r))e+\chi(r)R_te\bigr)\), where the bracket has norm at most \(r<\rho\). If \(t>1\), then \(\|\gamma(t)\|=a(t)\ge\frac18\) and \(\|G(x)\|\ge\frac18-\rho>\frac\rho4\). If \(t\le1\), then \(R_t=1\), the bracket equals \(e\), and \(e\perp u(t)=v(t)\) while \(\gamma(t)\) is a multiple of \(v(t)\); so \(\|G(x)\|\ge\|e\|=r\ge\frac\rho2\).

*Step 4: \(G(x)=x\) when \(\|x\|\ge\frac12\).* This holds by definition if \(x\notin U\). If \(x\in U\), then \(|a(t)|=\|\gamma(t)\|\ge\|x\|-r>\frac12-\frac1{32}>\frac5{16}\). As \(a\le\frac5{16}\) everywhere, \(a(t)<-\frac5{16}<-\frac18\); hence \(q(t)=0\), and \(t<0\), so \(R_t=1\). Formula (5.2) gives \(G(x)=x\).

*Step 5: the map \(f\).* Put \(f(x)=-G(x)/\|G(x)\|\). By Step 3 and Lemma 1.2 with \(r=\frac\rho4\), \(f\) is Lipschitz with constant \(\frac8\rho\) times that of \(G\), and \(\|f(x)\|=1\). If \(\|x\|<\frac12\), then \(\|f(x)-x\|\ge\|f(x)\|-\|x\|>\frac12\). If \(\|x\|\ge\frac12\), then \(G(x)=x\) by Step 4, so \(f(x)=-x/\|x\|\) and \(\|f(x)-x\|=1+\|x\|\ge\frac32\). \(\square\)

## 6. Remarks

**Finite dimensions.** No map as in Theorem 5.1 exists on the closed unit ball \(D\) of \(\mathbb R^n\): by Brouwer's fixed-point theorem, every continuous \(f:D\to D\) has a fixed point. In the construction above, the place where infinite dimension enters is Lemma 2.3: by Exercise 7.4, no curve in \(\mathbb R^n\) with a bounded tail has the separation property (2.1).

**General normed spaces.** Benyamini and Sternfeld proved that the unit sphere of every infinite-dimensional normed space is Lipschitz contractible, and that the closed unit ball of every such space admits a Lipschitz self-map whose displacement \(\|f(x)-x\|\) is bounded below by a positive constant [BS]. For the application to Thompson's group only the Hilbert space case is needed, and only through the two properties in Theorem 5.1.

**The size of the Lipschitz constant.** The construction gives an explicit but large Lipschitz constant. No construction can reach Lipschitz constant \(1\) (Exercise 7.2).

## 7. Exercises

**Exercise 7.1** (Kakutani's map; medium). In real \(\ell^2\) define \(k(x)=\bigl(\sqrt{1-\|x\|^2},\,x_1,\,x_2,\,\dots\bigr)\) for \(\|x\|\le1\). Show that \(k\) is continuous, maps the closed unit ball into the unit sphere, and has no fixed point, but that \(\inf_{\|x\|\le1}\|k(x)-x\|=0\).

**Exercise 7.2** (medium). Let \(f\) be a map of the closed unit ball \(B\) of a real Hilbert space into itself with Lipschitz constant \(L\) and \(\inf_{x\in B}\|f(x)-x\|=\delta>0\). Show that \(L>1\).

**Exercise 7.3** (easy). Show that for \(s,t\ge3\) the distance \(\|\gamma(t)-\gamma(s)\|\) depends only on \(t-s\), and compute its limit as \(t-s\to\infty\).

**Exercise 7.4** (easy). Let \(\Gamma:[0,\infty)\to\mathbb R^n\) be a map with bounded image and \(d>0\). Show that \(\inf\{|\Gamma(t)-\Gamma(s)|:|t-s|\ge d\}=0\).

## 8. Solutions

**7.1.** Continuity: \(x\mapsto\|x\|\) is continuous and the shift \(x\mapsto(0,x_1,x_2,\dots)\) is an isometry. Also \(\|k(x)\|^2=1-\|x\|^2+\|x\|^2=1\). If \(k(x)=x\), then \(\|x\|=1\), so the first coordinate gives \(x_1=0\), and \(x_{j+1}=x_j\) for all \(j\) gives \(x=0\), a contradiction. For \(x^{(n)}=n^{-1/2}(e_1+\dots+e_n)\) we have \(\|x^{(n)}\|=1\), \(k(x^{(n)})=n^{-1/2}(e_2+\dots+e_{n+1})\), and \(\|k(x^{(n)})-x^{(n)}\|=\|n^{-1/2}(e_{n+1}-e_1)\|=\sqrt{2/n}\to0\).

**7.2.** Suppose \(L\le1\) and let \(0<\varepsilon<\delta\). The map \(g=(1-\varepsilon)f\) sends \(B\) into \(B\) and has Lipschitz constant \(\lambda=(1-\varepsilon)L<1\). For any \(x_0\in B\), the iterates \(x_{m+1}=g(x_m)\) satisfy \(\|x_{m+1}-x_m\|\le\lambda^m\|x_1-x_0\|\), so they form a Cauchy sequence; its limit \(x\in B\) satisfies \(g(x)=x\) by continuity. Then \(\|f(x)-x\|=\|f(x)-(1-\varepsilon)f(x)\|=\varepsilon\|f(x)\|\le\varepsilon<\delta\), a contradiction.

**7.3.** For \(s,t\ge3\), \(a(s)=a(t)=\frac5{16}\) and \(\theta(t)-\theta(s)=t-s\), so \(\|\gamma(t)-\gamma(s)\|^2=2(\frac5{16})^2(1-\operatorname{sinc}(t-s))\). As \(t-s\to\infty\) this tends to \(2(\frac5{16})^2\), so the distance tends to \(\frac{5\sqrt2}{16}\): the far parts of the tail become orthogonal.

**7.4.** The points \(\Gamma(md)\), \(m=0,1,2,\dots\), lie in a bounded subset of \(\mathbb R^n\), so by the Bolzano–Weierstrass theorem some subsequence converges. For every \(\eta>0\), two terms of this subsequence with indices \(m\neq m'\) satisfy \(|\Gamma(md)-\Gamma(m'd)|<\eta\), while \(|md-m'd|\ge d\).

## References

- [BS] Y. Benyamini and Y. Sternfeld, *Spheres in infinite-dimensional normed spaces are Lipschitz contractible*, Proc. Amer. Math. Soc. 88 (1983), 439–445. https://doi.org/10.1090/S0002-9939-1983-0699410-7
- [Ka] S. Kakutani, *Topological properties of the unit sphere of a Hilbert space*, Proc. Imp. Acad. Tokyo 19 (1943), 269–271.
- [OpenAI-F] OpenAI, *Thompson's group F is nonamenable*, OpenAI Math Release preprint, 23 September 2026, Appendix A. https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026
