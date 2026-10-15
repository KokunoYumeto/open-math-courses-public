# Wulff bodies and the reduction to a variance bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(K\) and \(L\) be convex bodies in \(\mathbb R^n\) that are symmetric about the origin. In every direction \(u\) take the geometric mean \(h_K(u)^{1-\lambda}h_L(u)^\lambda\) of their support numbers, and intersect the half-spaces \(\langle x,u\rangle\le h_K(u)^{1-\lambda}h_L(u)^\lambda\). The *logarithmic Brunn-Minkowski inequality* says that the volume of this intersection is at least \(|K|^{1-\lambda}|L|^\lambda\). According to [OpenAI-L] it was conjectured by Böröczky, Lutwak, Yang and Zhang in 2012 and proved by them in the plane. [OpenAI-L] gives a proof in every dimension. Liu, Sun and Xiong extended it to convex bodies whose centroid is the origin, with the cases of equality [LSX]; Section 5 of [The variance bound and the inequality](the-variance-bound-and-the-inequality.md) states their results.

This lesson states the inequality, proves the facts about support functions that it needs, and reduces it to an inequality between a variance and a mean for explicit smooth probability densities, the *variance bound*.

- Support functions and Wulff bodies (Lemmas 1.1 and 1.2); boxes, an example with equality (Example 2.1).
- The inequality and the variance bound; the reduction (Theorem 2.2).
- Soft polytopes: the second derivative of the logarithm of an integral (Lemma 3.1).
- From soft polytopes to polytopes and to all bodies (Lemma 4.1 and Section 5).
- The additive inequality for \(0<p<1\) (Corollary 6.1).

The lesson follows [OpenAI-L, Sections 1, 2 and 8.1]. It uses the theorems of dominated and monotone convergence for the Lebesgue integral in \(\mathbb R^n\) (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

## 1. Support functions and Wulff bodies

A *convex body* in \(\mathbb R^n\) is a compact convex set with an interior point. Its *support function* is
\[
h_K(u)=\max_{x\in K}\langle x,u\rangle\qquad(u\in\mathbb R^n).
\]
We use it mostly on the unit sphere \(S^{n-1}\). The volume of \(K\) is written \(|K|\).

**Lemma 1.1.** Let \(K\) and \(L\) be convex bodies.

1. \(|h_K(u)-h_K(v)|\le\varrho\,|u-v|\), where \(\varrho\) is the largest norm of a point of \(K\). In particular \(h_K\) is continuous.
2. \(K\) is the set of the \(x\) with \(\langle x,u\rangle\le h_K(u)\) for all \(u\in S^{n-1}\).
3. If \(K=-K\), then \(h_K(-u)=h_K(u)\), a ball about \(0\) of some radius \(r>0\) lies in \(K\), and \(h_K\ge r\) on the sphere.
4. \(h_{aK+bL}=a\,h_K+b\,h_L\) for \(a,b\ge0\) with \(a+b>0\), and \(aK+bL\) is a convex body.

**Proof.** (1) If \(h_K(u)=\langle x,u\rangle\), then \(h_K(v)\ge\langle x,v\rangle\ge h_K(u)-\varrho|u-v|\); exchange \(u\) and \(v\).

(2) A point of \(K\) satisfies the inequalities by the definition of \(h_K\). Let \(y\notin K\), and let \(x_0\) be a point of \(K\) nearest to \(y\). For \(x\in K\) and \(0<s\le1\) the point \(x_0+s(x-x_0)\) lies in \(K\), so its distance to \(y\) is at least \(|y-x_0|\):
\[
-2s\,\langle y-x_0,x-x_0\rangle+s^2|x-x_0|^2\ge0 .
\]
Divide by \(s\) and let \(s\to0\): \(\langle y-x_0,x-x_0\rangle\le0\). With \(u=(y-x_0)/|y-x_0|\) this says \(\langle x,u\rangle\le\langle x_0,u\rangle\) for all \(x\in K\). So \(h_K(u)=\langle x_0,u\rangle\), and this is \(\langle y,u\rangle-|y-x_0|<\langle y,u\rangle\).

(3) The first statement follows from \(\langle x,-u\rangle=\langle-x,u\rangle\). If a ball of radius \(r\) about a point \(a\) lies in \(K\), then so does the ball of radius \(r\) about \(-a\), and the midpoints of the points of the two balls form the ball of radius \(r\) about \(0\). Then \(h_K(u)\ge\langle ru,u\rangle=r\).

(4) The maximum of \(\langle ax+by,u\rangle\) over \(x\in K\), \(y\in L\) is \(a\,h_K(u)+b\,h_L(u)\). The set \(aK+bL\) is compact and convex, and it contains a translate of a ball. \(\blacksquare\)

**Definition.** For a positive continuous function \(f\) on \(S^{n-1}\), the *Wulff body* \(\mathcal W[f]\) of \(f\) is the set of the \(x\in\mathbb R^n\) with
\[
\langle x,u\rangle\le f(u)\qquad\text{for all }u\in S^{n-1}.
\]

**Lemma 1.2.** Let \(f,g\) be positive continuous functions on the sphere.

1. \(\mathcal W[f]\) is a convex body. It contains the ball of radius \(\min f\) about \(0\) and lies in the ball of radius \(\max f\).
2. If \(f\le g\), then \(\mathcal W[f]\subset\mathcal W[g]\). For \(c>0\), \(\mathcal W[cf]=c\,\mathcal W[f]\).
3. \(\mathcal W[h_K]=K\) for a convex body \(K\) with \(0\) in its interior.
4. If \(f\) is even, then \(\mathcal W[f]\) is the set of the \(x\) with \(|\langle x,u\rangle|\le f(u)\) for all \(u\), and \(\mathcal W[f]=-\mathcal W[f]\).
5. For convex bodies \(K=-K\), \(L=-L\) and \(0\le\lambda\le1\),
\[
\mathcal W\bigl[h_K^{1-\lambda}h_L^\lambda\bigr]\subset(1-\lambda)K+\lambda L .
\]

**Proof.** (1) An intersection of closed half-spaces is closed and convex. If \(|x|\le\min f\), then \(\langle x,u\rangle\le|x|\le f(u)\). If \(x\in\mathcal W[f]\) and \(x\ne0\), take \(u=x/|x|\): \(|x|\le f(u)\le\max f\). (2) is clear from the definition. (3) is Lemma 1.1 (2); here \(h_K\) is positive because a ball about \(0\) lies in \(K\). (4) Apply the condition to \(u\) and to \(-u\). (5) For positive numbers, \(a^{1-\lambda}b^\lambda\le(1-\lambda)a+\lambda b\), because the logarithm is concave. So by Lemma 1.1 (4) the function \(h_K^{1-\lambda}h_L^\lambda\) is at most the support function of the convex body \((1-\lambda)K+\lambda L\), and (2) and (3) apply. \(\blacksquare\)

By the definition, the support function of \(\mathcal W[f]\) is at most \(f\). It can be smaller: \(f\) need not be a support function.

## 2. The inequality and the variance bound

**The logarithmic Brunn-Minkowski inequality in dimension \(n\).** For all convex bodies \(K=-K\) and \(L=-L\) in \(\mathbb R^n\) and all \(0\le\lambda\le1\),
\[
\Bigl|\mathcal W\bigl[h_K^{1-\lambda}h_L^\lambda\bigr]\Bigr|\ \ge\ |K|^{1-\lambda}\,|L|^\lambda .
\]
This statement is called (LBM) below.

By Lemma 1.2 (5) this is stronger, for symmetric bodies, than the inequality \(|(1-\lambda)K+\lambda L|\ge|K|^{1-\lambda}|L|^\lambda\) of Brunn and Minkowski.

**Example 2.1 (boxes).** Let \(K\) be the box of the \(x\) with \(|x_i|\le a_i\) and \(L\) the box with \(|x_i|\le b_i\), where \(a_i,b_i>0\). Then \(h_K(u)=\sum_ia_i|u_i|\). Let \(B\) be the box with \(|x_i|\le a_i^{1-\lambda}b_i^\lambda\). The conditions for the coordinate directions show \(\mathcal W[h_K^{1-\lambda}h_L^\lambda]\subset B\). Conversely, for \(x\in B\) and \(0<\lambda<1\), by Hölder's inequality with the exponents \(\tfrac1{1-\lambda}\) and \(\tfrac1\lambda\),
\[
\begin{aligned}
\langle x,u\rangle&\le\sum_i(a_i|u_i|)^{1-\lambda}(b_i|u_i|)^\lambda\\
&\le h_K(u)^{1-\lambda}\,h_L(u)^\lambda .
\end{aligned}
\]
So the Wulff body is \(B\), and its volume \(\prod_i2a_i^{1-\lambda}b_i^\lambda\) is equal to \(|K|^{1-\lambda}|L|^\lambda\): for boxes with the same axes (LBM) is an equality.

For a probability measure \(\mu\) write \(\mathbb E_\mu f=\int f\,d\mu\) and \(\operatorname{Var}_\mu(f)=\mathbb E_\mu(f-\mathbb E_\mu f)^2\).

**The variance bound in dimension \(n\).** Let \(N\ge1\), let \(q\ge2\) be an even integer, \(\varepsilon>0\), \(p_1,\dots,p_N\) nonzero vectors of \(\mathbb R^n\) and \(h_1,\dots,h_N>0\). Put
\[
\begin{gathered}
\psi_i(x)=\Bigl(\frac{\langle p_i,x\rangle}{h_i}\Bigr)^q,\\
V(x)=\frac\varepsilon2|x|^2+\sum_{i=1}^N\psi_i(x),\\
Z=\int_{\mathbb R^n}e^{-V(x)}\,dx,\\
d\mu=Z^{-1}e^{-V(x)}\,dx .
\end{gathered}
\]
Then for all real numbers \(b_1,\dots,b_N\)
\[
\operatorname{Var}_\mu\Bigl(\sum_{i=1}^Nb_i\psi_i\Bigr)\ \le\ \sum_{i=1}^Nb_i^2\,\mathbb E_\mu\psi_i .
\]
This statement is called (VB) below.

The term \(\tfrac\varepsilon2|x|^2\) makes \(Z\) finite, and all polynomials are integrable for \(\mu\). In words: the covariance matrix of the functions \(\psi_i\) is at most the diagonal matrix of their means.

**Theorem 2.2.** Let \(n\ge2\). If the variance bound holds in dimension \(n\), then the logarithmic Brunn-Minkowski inequality holds in dimension \(n\). In dimension \(1\) the inequality (LBM) holds with equality.

[OpenAI-L, Sections 3 to 7] proves the variance bound in every dimension \(n\ge2\). In this course it is Theorem 4.1 of the lesson [The variance bound and the inequality](the-variance-bound-and-the-inequality.md), which rests on two statements from the literature that the course names as hypotheses. Sections 3 to 5 of this lesson prove Theorem 2.2.

## 3. Soft polytopes

Let \(p_1,\dots,p_N\) be nonzero vectors and \(h_i^0,h_i^1>0\). For real \(t\) let
\[
h_i(t)=(h_i^0)^{1-t}(h_i^1)^t ,
\]
and let \(\psi_i(t,\cdot)\), \(V(t,\cdot)\), \(Z(t)\) and \(\mu_t\) be the objects of the variance bound for the widths \(h_i(t)\), with fixed \(q\) and \(\varepsilon\). The density \(e^{-V(t,x)}\) is a smooth replacement of the indicator of the set where \(|\langle p_i,x\rangle|\le h_i(t)\) for all \(i\).

**Lemma 3.1.** \(Z\) is twice continuously differentiable, and with \(b_i=-q\log(h_i^1/h_i^0)\)
\[
\begin{aligned}
&\frac{d^2}{dt^2}\log Z(t)\\
&\quad=\operatorname{Var}_{\mu_t}\Bigl(\sum_ib_i\psi_i\Bigr)-\sum_ib_i^2\,\mathbb E_{\mu_t}\psi_i .
\end{aligned}
\]

**Proof.** Since \(h_i(t)^{-q}=(h_i^0)^{-q}e^{b_it}\), we have \(\psi_i(t,x)=e^{b_it}\psi_i(0,x)\). So
\[
\dot V=\sum_ib_i\psi_i,\qquad\ddot V=\sum_ib_i^2\psi_i ,
\]
where the dots are derivatives in \(t\), and
\[
\begin{gathered}
\partial_te^{-V}=-\dot V\,e^{-V},\\
\partial_t^2e^{-V}=(\dot V^2-\ddot V)\,e^{-V}.
\end{gathered}
\]
For \(t\) in a bounded interval, \(|\dot V|\), \(\dot V^2\) and \(|\ddot V|\) are at most a polynomial in \(|x|\), and \(e^{-V}\le e^{-\varepsilon|x|^2/2}\). So the two derivatives of \(e^{-V}\) have an integrable bound that does not depend on \(t\), and by dominated convergence, applied to the difference quotients, \(Z\) may be differentiated twice under the integral:
\[
\begin{gathered}
Z'=-\int\dot V\,e^{-V}dx,\\
Z''=\int(\dot V^2-\ddot V)\,e^{-V}dx .
\end{gathered}
\]
Both are continuous in \(t\), again by dominated convergence. Hence
\[
\begin{aligned}
(\log Z)''&=\frac{Z''}Z-\Bigl(\frac{Z'}Z\Bigr)^2\\
&=\mathbb E_{\mu_t}\dot V^2-\mathbb E_{\mu_t}\ddot V-(\mathbb E_{\mu_t}\dot V)^2 .
\end{aligned}
\]
\(\blacksquare\)

**Corollary 3.2.** If the variance bound holds in dimension \(n\), then \(\log Z\) is concave, and for \(0\le\lambda\le1\)
\[
Z(\lambda)\ \ge\ Z(0)^{1-\lambda}\,Z(1)^\lambda .
\]

**Proof.** The variance bound for the widths \(h_i(t)\) says that the right side of Lemma 3.1 is at most \(0\). \(\blacksquare\)

## 4. From soft polytopes to polytopes

Let the vectors \(p_i\) span \(\mathbb R^n\), and let
\[
P(t)=\bigl\{x:\ |\langle p_i,x\rangle|\le h_i(t)\text{ for all }i\bigr\}.
\]
This set is closed and convex, and it is bounded, because \(x\mapsto\max_i|\langle p_i,x\rangle|\) is a norm when the \(p_i\) span.

**Lemma 4.1.** If the variance bound holds in dimension \(n\), then for \(0\le\lambda\le1\)
\[
|P(\lambda)|\ \ge\ |P(0)|^{1-\lambda}\,|P(1)|^\lambda .
\]

**Proof.** Write \(Z_{q,\varepsilon}(t)\) for the integral \(Z(t)\). Fix \(\varepsilon\) and \(t\), and let \(q\to\infty\) through the even integers. If \(|\langle p_i,x\rangle|<h_i(t)\) for all \(i\), every \(\psi_i(t,x)\) tends to \(0\), and \(e^{-V}\) tends to \(e^{-\varepsilon|x|^2/2}\). If \(|\langle p_i,x\rangle|>h_i(t)\) for some \(i\), this \(\psi_i\) tends to infinity and \(e^{-V}\) tends to \(0\). The other points \(x\) lie in the finitely many hyperplanes \(\langle p_i,x\rangle=\pm h_i(t)\), a set of measure \(0\). Since \(e^{-V}\le e^{-\varepsilon|x|^2/2}\), dominated convergence gives
\[
Z_{q,\varepsilon}(t)\ \longrightarrow\ Z_\varepsilon(t)=\int_{P(t)}e^{-\varepsilon|x|^2/2}\,dx .
\]
By Corollary 3.2, \(Z_\varepsilon(\lambda)\ge Z_\varepsilon(0)^{1-\lambda}Z_\varepsilon(1)^\lambda\). Now let \(\varepsilon\) decrease to \(0\). The integrands increase to the indicator of \(P(t)\), and by monotone convergence \(Z_\varepsilon(t)\to|P(t)|\). \(\blacksquare\)

## 5. All directions

**Proof of Theorem 2.2.** Let \(n\ge2\), and let \(K=-K\) and \(L=-L\) be convex bodies. For \(0\le t\le1\) let \(f_t=h_K^{1-t}h_L^t\); it is positive, continuous and even, by Lemma 1.1. The sphere has a countable dense subset \(u_1,u_2,\dots\). Let \(D_m\) consist of the coordinate vectors \(e_1,\dots,e_n\) and of \(u_1,\dots,u_m\), and let \(P_m(t)\) be the set of the \(x\) with
\[
|\langle p,x\rangle|\le f_t(p)\qquad\text{for all }p\in D_m .
\]
This is the set \(P(t)\) of Section 4 for the vectors of \(D_m\), which span, with the widths \(h_K(p)\) at \(t=0\) and \(h_L(p)\) at \(t=1\). By Lemma 4.1,
\[
|P_m(\lambda)|\ \ge\ |P_m(0)|^{1-\lambda}\,|P_m(1)|^\lambda .
\]
The sets \(P_m(t)\) decrease as \(m\) grows, and they lie in the bounded set \(P_1(t)\). Their intersection is \(\mathcal W[f_t]\): by Lemma 1.2 (4), \(\mathcal W[f_t]\) lies in every \(P_m(t)\); and a point of all the \(P_m(t)\) satisfies \(|\langle x,u\rangle|\le f_t(u)\) for a dense set of \(u\), hence for all \(u\), because both sides are continuous. So \(|P_m(t)|\) decreases to \(|\mathcal W[f_t]|\), since the measure of a decreasing sequence of sets of finite measure tends to the measure of the intersection. For \(t=0\) and \(t=1\) the intersections are \(\mathcal W[h_K]=K\) and \(\mathcal W[h_L]=L\), by Lemma 1.2 (3). The limit \(m\to\infty\) of the last display is (LBM).

In dimension \(1\) let \(K=[-a,a]\) and \(L=[-b,b]\). The sphere consists of \(\pm1\), \(h_K=a\) and \(h_L=b\), and the Wulff body is the interval of the radius \(a^{1-\lambda}b^\lambda\). Its length is \((2a)^{1-\lambda}(2b)^\lambda\). \(\blacksquare\)

The proof used the variance bound only through Lemma 4.1, for finitely many unit vectors that span.

## 6. The additive inequality for powers between 0 and 1

For \(0<p<1\) the geometric mean of the support functions is replaced by the mean \(((1-\lambda)h_K^p+\lambda h_L^p)^{1/p}\), which is larger.

**Corollary 6.1.** Let (LBM) hold in dimension \(n\). Let \(K=-K\), \(L=-L\) be convex bodies in \(\mathbb R^n\), \(0<p<1\) and \(0\le\lambda\le1\), and let \(g=((1-\lambda)h_K^p+\lambda h_L^p)^{1/p}\). Then
\[
|\mathcal W[g]|^{p/n}\ \ge\ (1-\lambda)\,|K|^{p/n}+\lambda\,|L|^{p/n}.
\]

**Proof.** For \(\lambda=0\) and \(\lambda=1\) both sides are equal. Let \(0<\lambda<1\). Let \(a=|K|^{1/n}\), \(b=|L|^{1/n}\), \(K_0=a^{-1}K\), \(L_0=b^{-1}L\); these bodies have the volume \(1\), and \(h_K=a\,h_{K_0}\), \(h_L=b\,h_{L_0}\). Let
\[
c=\bigl((1-\lambda)a^p+\lambda b^p\bigr)^{1/p},\qquad\theta=\frac{\lambda b^p}{c^p},
\]
so that \(0<\theta<1\) and \(1-\theta=(1-\lambda)a^p/c^p\). Then
\[
\begin{aligned}
g&=c\,\bigl((1-\theta)h_{K_0}^p+\theta h_{L_0}^p\bigr)^{1/p}\\
&\ge c\,h_{K_0}^{1-\theta}\,h_{L_0}^\theta ,
\end{aligned}
\]
by the inequality between the weighted arithmetic and geometric means of \(h_{K_0}^p\) and \(h_{L_0}^p\). By Lemma 1.2 (2), \(\mathcal W[g]\) contains \(c\,\mathcal W[h_{K_0}^{1-\theta}h_{L_0}^\theta]\), and by (LBM) the latter has a volume of at least \(c^n\). So \(|\mathcal W[g]|^{p/n}\ge c^p\), and \(c^p\) is the right side. \(\blacksquare\)

## 7. Exercises

**7.1.** In the plane let \(K\) be the box with \(|x_1|\le1\), \(|x_2|\le a\) and \(L\) the box with \(|x_1|\le a\), \(|x_2|\le1\), where \(a>0\), \(a\ne1\). Show that \(h_K^{1/2}h_L^{1/2}\) is not the support function of a convex body.

**7.2.** Let \(n=1\), \(N=1\), \(p_1=1\), and take \(\varepsilon=0\) in the definitions of Section 3, so that \(Z(t)=\int\exp(-(x/h(t))^q)\,dx\). Show that \(\log Z\) is an affine function of \(t\), and deduce that for the probability density proportional to \(e^{-y^q}\) the function \(y^q\) has the mean \(\tfrac1q\) and the variance \(\tfrac1q\). So the variance bound, read for \(\varepsilon=0\), is an equality here.

**7.3.** Let \(f\) be positive and continuous on the sphere, and \(M\) a convex body with \(0\) in its interior and \(h_M\le f\). Show that \(M\subset\mathcal W[f]\). So \(\mathcal W[f]\) is the largest such body.

**7.4.** For \(\varepsilon>0\) and a Borel set \(S\) let \(\gamma_\varepsilon(S)=\int_Se^{-\varepsilon|x|^2/2}dx\). Show that the variance bound in dimension \(n\) implies, with the notation of (LBM) and \(f_\lambda=h_K^{1-\lambda}h_L^\lambda\),
\[
\gamma_\varepsilon\bigl(\mathcal W[f_\lambda]\bigr)\ \ge\ \gamma_\varepsilon(K)^{1-\lambda}\,\gamma_\varepsilon(L)^{\lambda}.
\]

## 8. Solutions

**7.1.** Let \(f=h_K^{1/2}h_L^{1/2}\), so \(f(u)^2=(|u_1|+a|u_2|)(a|u_1|+|u_2|)\). By Example 2.1, \(\mathcal W[f]\) is the square with \(|x_i|\le\sqrt a\), whose support function is \(\sqrt a\,(|u_1|+|u_2|)\). At \(u=(1,1)/\sqrt2\) this is \(\sqrt{2a}\), while \(f(u)=(1+a)/\sqrt2\), and \(1+a>2\sqrt a\) for \(a\ne1\). If \(f\) were the support function of a convex body \(M\), then by Lemma 1.1 (2) the body \(M\) would be the set of the \(x\) with \(\langle x,u\rangle\le f(u)\) for all \(u\), which is \(\mathcal W[f]\); but the support function of \(\mathcal W[f]\) is not \(f\).

**7.2.** The substitution \(x=h(t)y\) gives \(Z(t)=h(t)\int e^{-y^q}dy\), and \(\log h(t)\) is affine in \(t\). The computation of Lemma 3.1 applies for \(\varepsilon=0\), because \(e^{-V}\) decays faster than every power. With \(s=\log(h^1/h^0)\) and \(b=-qs\): \((\log Z)'=-\mathbb E\dot V=qs\,\mathbb E\psi\) must be \(s\), so \(\mathbb E\psi=\tfrac1q\); and \((\log Z)''=b^2(\operatorname{Var}\psi-\mathbb E\psi)\) must be \(0\), so \(\operatorname{Var}\psi=\tfrac1q\). Under \(\mu_t\) the variable \(y=x/h(t)\) has the density proportional to \(e^{-y^q}\), and \(\psi=y^q\).

**7.3.** By Lemma 1.2 (3) and (2), \(M=\mathcal W[h_M]\subset\mathcal W[f]\).

**7.4.** In the proof of Lemma 4.1 stop before the limit \(\varepsilon\to0\): \(Z_\varepsilon(\lambda)\ge Z_\varepsilon(0)^{1-\lambda}Z_\varepsilon(1)^\lambda\) for the sets \(P_m(t)\) of Section 5. The measure with the density \(e^{-\varepsilon|x|^2/2}\) is finite, so its values on the decreasing sets \(P_m(t)\) tend to its value on \(\mathcal W[f_t]\).

## References

- [OpenAI-L] OpenAI, *The logarithmic Brunn-Minkowski conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 1, 2 and 8.1. https://github.com/openai/math/tree/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026
- [LSX] Y. Liu, Q. Sun and G. Xiong, *The centered logarithmic Brunn–Minkowski inequality*, arXiv:2610.10152 (October 2026). https://arxiv.org/abs/2610.10152
