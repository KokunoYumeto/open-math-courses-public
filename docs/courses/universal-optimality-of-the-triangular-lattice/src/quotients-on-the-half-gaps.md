# Quotients on the half-gaps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By [Exact interpolation](exact-interpolation.md), for every \(k\ge2.36\) there are entire functions \(H_1,H_2\) that touch \(T_k\) and \(0\) at every node. The normalized statement \((\mathrm N_k)\) follows once \(H_1\le T_k\) and \(H_2\ge0\) on \([0,\infty)\). These two inequalities are strict between the nodes and equalities of second order at the nodes, so they cannot be read off from approximate values of \(H_1,H_2\). This lesson divides out the double zeros and reduces the inequalities on the interval \([0,89.5]\) to a statement about explicit polynomials of degree \(40\).

- The interval \([0,89.5]\) is covered by \(91\) *half-gaps*, each reaching from a node to the midpoint of a neighbouring gap. On a half-gap with centre \(m>0\) the function \(F(s)/(s-m)^2\) is studied in place of \(F\) (Section 1).
- The quotient changes by less than \(0.00011\) when the exact lists are replaced by the reference lists (Proposition 2.1), and by less than \(10^{-6}\) when the quotient of the reference functions is replaced by a polynomial of degree \(40\) with explicitly defined coefficients (Proposition 2.2).
- The quotient of the target \(T_k\) is bounded below, for all \(k\) in an interval \(K\le k\le J\), by a polynomial that depends only on \(K\) and \(J\) (Proposition 2.3).
- Hence it suffices that certain polynomials \(\Phi_i(x;k)\) are larger than \(0.001\) on \([0,1]\) (Theorem 3.1).

The lesson follows [OpenAI-T, Section 5, the parts on the quotients and on the lower supports of the target, and Section 3, the part on polynomial rows].

## 1. Slack functions, half-gaps and quotients

Fix \(k\ge2.36\). Let \(\ell_1,\ell_2\) be the lists of Theorem 3.1 of the lesson on exact interpolation, and \(H_1,H_2\) the functions of its Corollary 3.2. The *slack functions* are
\[
F_1=T_k-H_1,\qquad F_2=H_2 .
\]
With \(\sigma_1=-1\), \(\sigma_2=1\), \(\delta_1=1\), \(\delta_2=0\) they are \(F_i=\sigma_iH_i+\delta_iT_k\). They are entire, real on the real axis, and
\[
F_i(m)=F_i'(m)=0\qquad(m\in\mathcal N).
\]
The aim is \(F_1\ge0\) and \(F_2\ge0\) on \([0,\infty)\).

The set \(\mathcal N_0\) of the nodes together with \(0\) consists of the integers \(n\ge0\) congruent to \(0,1,3,4,7,9\) modulo \(12\). The gaps between consecutive elements have the lengths \(1,2,1,3,2,3\), repeating. A *half-gap* is given by a *centre* \(m\in\mathcal N_0\) with \(m\le88\) and a neighbour \(m'\) of \(m\) in \(\mathcal N_0\): it is the interval between \(m\) and the midpoint of \(m\) and \(m'\). With
\[
y=\frac{m'-m}2
\]
it consists of the points \(s=m+yx\), \(0\le x\le1\). The number \(y\) is positive for the half-gap to the right of \(m\) and negative for the one to the left, and \(\tfrac12\le|y|\le\tfrac32\).

**Lemma 1.1.** There are \(91\) half-gaps, and their union is the interval \([0,s_0]\) with \(s_0=89.5\).

**Proof.** The centres are the elements of \(\mathcal N_0\) up to \(88\): six in each of the seven blocks of twelve integers from \(0\) to \(83\), and \(84,85,87,88\), together \(46\). Each has a right half-gap, and each except \(0\) has a left one; this gives \(91\). Two consecutive centres share the gap between them, which is the union of the right half-gap of the smaller and the left half-gap of the larger. The successor of \(88\) in \(\mathcal N_0\) is \(91\), so the last right half-gap is \([88,89.5]\). \(\blacksquare\)

For a function \(u\) that is twice continuously differentiable, and \(m>0\), let
\[
\begin{aligned}
&\mathcal D_mu(s)\\
&\quad=\frac{u(s)-u(m)-(s-m)\,u'(m)}{(s-m)^2}
\end{aligned}
\]
for \(s\ne m\), and \(\mathcal D_mu(m)=\tfrac12u''(m)\). At the centre \(0\) nothing is divided out: \(\mathcal D_0u=u\). Let \(\nu=2\) for \(m>0\) and \(\nu=0\) for \(m=0\).

**Lemma 1.2.** Let \(m>0\).

1. For all \(s\), with \(w=s-m\),
\[
\begin{aligned}
&\mathcal D_mu(s)\\
&\quad=\int_0^1(1-v)\,u''(m+vw)\,dv .
\end{aligned}
\]
In particular \(|\mathcal D_mu(s)|\) is at most half the maximum of \(|u''|\) between \(m\) and \(s\).
2. If \(u(m)=u'(m)=0\), then \(u(s)=(s-m)^2\,\mathcal D_mu(s)\).
3. If \(u\) is entire, then for all \(x\) and \(y\)
\[
\begin{aligned}
&\mathcal D_mu(m+yx)\\
&\quad=\sum_{r\ge0}\frac{y^r}{(r+2)!}\,u^{(r+2)}(m)\,x^r .
\end{aligned}
\]

For \(m=0\) the corresponding expansion is \(u(yx)=\sum_r\tfrac{y^r}{r!}u^{(r)}(0)x^r\). So in both cases
\[
\begin{aligned}
&\mathcal D_mu(m+yx)\\
&\quad=\sum_{r\ge0}\frac{y^r}{(r+\nu)!}\,u^{(r+\nu)}(m)\,x^r .
\end{aligned}
\]

**Proof.** (1) is the formula of Taylor with the remainder as an integral, and \(\int_0^1(1-v)\,dv=\tfrac12\). (2) is the definition. (3) follows from the Taylor series of \(u\) at \(m\), in which the terms of degree \(0\) and \(1\) are removed and the others divided by \((yx)^2\). \(\blacksquare\)

By (2), \(F_i(s)=(s-m)^2\,\mathcal D_mF_i(s)\) for every centre \(m>0\). So \(F_i\ge0\) on a half-gap as soon as \(\mathcal D_mF_i\ge0\) there. The quotient is formed for each function separately,
\[
\mathcal D_mF_i=\sigma_i\,\mathcal D_mH_i+\delta_i\,\mathcal D_mT_k ,
\]
and each term is then approximated. In this way no approximation error is ever divided by \((s-m)^2\).

## 2. Three comparisons

Let \(\ell_i^{\mathrm{ref}}=X_iq(k)\) be the reference lists, \(p_i^{\mathrm{ref}}\) their cardinal functions, and
\[
\begin{gathered}
H_1^{\mathrm{ref}}=p_1^{\mathrm{ref}}+K_{p_2^{\mathrm{ref}}},\\
H_2^{\mathrm{ref}}=p_2^{\mathrm{ref}}+K_{p_1^{\mathrm{ref}}},
\end{gathered}
\]
formed with the exact spectral integrals. These functions need not have any zeros.

**Proposition 2.1.** On every half-gap, with centre \(m\),
\[
|\mathcal D_m(H_i-H_i^{\mathrm{ref}})(s)|<0.00011 .
\]

**Proof.** Let \(\Delta_i=\ell_i-\ell_i^{\mathrm{ref}}\). Its extra entries are \(0\), and \(\|\Delta_1\|_1+\|\Delta_2\|_1<2\cdot10^{-8}\) by Theorem 3.1 of the lesson on exact interpolation. By linearity \(H_i-H_i^{\mathrm{ref}}=p_{\Delta_i}+K_{p_{\Delta_j}}\), with \(j\) the other index. For a list with \(C=0\) and \(W=\|\Delta\|_1\), Corollary 2.3 of the lesson on cardinal functions and Theorem 3.2 of the lesson on Gaussian damping give, for real \(s\ge0\) and \(a\ge0\),
\[
\begin{gathered}
|p_\Delta^{(a)}(s)|\le36\,\pi^a\,\|\Delta\|_1,\\
|K_{p_\Delta}^{(a)}(s)|\le36\cdot3\,(3\pi)^a\,\|\Delta\|_1 .
\end{gathered}
\]
So for \(s\ge0\)
\[
\begin{aligned}
&|(H_i-H_i^{\mathrm{ref}})^{(a)}(s)|\\
&\quad<108\,(3\pi)^a\cdot2\cdot10^{-8}.
\end{aligned}
\]
For \(m=0\) the claim is the case \(a=0\): the bound is \(2.16\cdot10^{-6}\). For \(m>0\), Lemma 1.2(1) with \(a=2\) gives the bound \(\tfrac12\cdot108\,(3\pi)^2\cdot2\cdot10^{-8}<9.6\cdot10^{-5}\), because \((3\pi)^2<88.83\). \(\blacksquare\)

Next the quotient of \(H_i^{\mathrm{ref}}\) is replaced by a polynomial. Fix a half-gap, with \(m\), \(y\) and \(\nu\). By Lemma 1.2 and the remark after it,
\[
\begin{gathered}
\sigma_i\,\mathcal D_mH_i^{\mathrm{ref}}(m+yx)=\sum_{r\ge0}\beta_{i,r}\,x^r,\\
\beta_{i,r}=\sigma_i\,y^{-\nu}\,\gamma_{i,r},\\
\gamma_{i,r}=\frac{y^{r+\nu}}{(r+\nu)!}\,(H_i^{\mathrm{ref}})^{(r+\nu)}(m).
\end{gathered}
\]
The scaled derivative \(\gamma_{i,r}\) is the sum of the scaled derivatives of order \(a=r+\nu\) of \(p_i^{\mathrm{ref}}\) and of \(K_{p_j^{\mathrm{ref}}}\) at \(s=m\). Let \(\widetilde\beta_{i,r}\) be the number obtained when both are replaced by their quadrature forms ([A positive quadrature rule](a-positive-quadrature-rule.md), Section 3). The quadrature forms are linear in the lists, and the lists are \(X_1q(k)\) and \(X_2q(k)\). So there is a row \(l_{i,r}\) of ten real numbers, not depending on \(k\), with
\[
\widetilde\beta_{i,r}=l_{i,r}\,q(k).
\]
The row \(l_{i,r}\) is obtained by applying the same operations to the ten columns of \(X_i\) and of \(X_j\) in place of the lists. It depends on the half-gap, on \(i\) and on \(r\).

**Proposition 2.2.** On every half-gap, for \(i=1,2\) and \(0\le x\le1\),
\[
\begin{gathered}
\Bigl|\sigma_i\,\mathcal D_mH_i^{\mathrm{ref}}(m+yx)-\sum_{r=0}^{40}l_{i,r}\,q(k)\,x^r\Bigr|\\
<10^{-6}.
\end{gathered}
\]

**Proof.** *The coefficients with \(r\le40\).* By Theorem 3.3 of the lesson on the quadrature rule, which applies because \(0\le m\le88\) and \(|y|\le\tfrac32\), and by linearity, the scaled derivatives of \(p_i^{\mathrm{ref}}\) and \(K_{p_j^{\mathrm{ref}}}\) differ from their quadrature forms by less than \(10^{-31}\) times \(\|\ell_i^{\mathrm{ref}}\|_1\) and \(\|\ell_j^{\mathrm{ref}}\|_1\). The sum of these norms is less than \(4.8\), and \(|y|^{-\nu}\le4\). So \(|\beta_{i,r}-\widetilde\beta_{i,r}|<20\cdot10^{-31}\), and the \(41\) coefficients together contribute less than \(10^{-28}\).

*The coefficients with \(r\ge41\).* Let \(Y=|y|\) and \(l=41+\nu\). Then
\[
\begin{aligned}
&\sum_{r\ge41}|\beta_{i,r}|\\
&\quad\le Y^{-\nu}\sum_{a\ge l}\frac{Y^a}{a!}\,\bigl|(H_i^{\mathrm{ref}})^{(a)}(m)\bigr| .
\end{aligned}
\]
The function \(H_i^{\mathrm{ref}}\) is a superposition of exponentials \(e^{i\pi ts}\), from \(p_i^{\mathrm{ref}}\), and \(\lambda(t)e^{i\pi z(t)s}\), from \(K_{p_j^{\mathrm{ref}}}\), with frequencies \(|t|\le1\) and with total weight at most \(36\,(\|\ell_1^{\mathrm{ref}}\|_1+\|\ell_2^{\mathrm{ref}}\|_1)<180\); a derivative of order \(a\) multiplies them by \((i\pi t)^a\) and \((i\pi z(t))^a\). For one exponential of the first kind,
\[
\begin{gathered}
\sum_{a\ge l}\frac{Y^a}{a!}\,(\pi|t|)^a\le\frac{(\pi Y)^l}{l!\,(1-\rho)},\\
\rho=\frac{3\pi Y}{l+1},
\end{gathered}
\]
because the ratio of consecutive terms is at most \(\pi Y/(l+1)\le\rho\); here \(\rho<0.34\). For one of the second kind let \(t_{j-1}\le|t|\le t_j\) with \(1\le j\le6\) and \(t_j=j/6\). Since \(|z(t)|\) and \(\operatorname{Im}z(t)\) decrease in \(|t|\), and \(|\lambda|<3\), \(|z|<3\), the sum is at most
\[
3\,e^{-\pi m\operatorname{Im}z(t_j)}\,\frac{(\pi|z(t_{j-1})|\,Y)^l}{l!\,(1-\rho)} .
\]
Hence \(\sum_{r\ge41}|\beta_{i,r}|\le E(m,Y,\nu)\), where
\[
\begin{gathered}
E(m,Y,\nu)=\frac{180\,Y^{-\nu}}{l!\,(1-\rho)}\,\bigl((\pi Y)^l+3\,\varepsilon\bigr),\\
\varepsilon=\sum_{j=1}^6e^{-\pi m\operatorname{Im}z(t_j)}\bigl(\pi|z(t_{j-1})|\,Y\bigr)^l .
\end{gathered}
\]
For fixed \(\nu\) this expression decreases when \(m\) increases, and increases with \(Y\), because \(Y^{-\nu}Y^l=Y^{41}\) and \(\rho\) increases with \(Y\). For \(m=0\) we have \(Y=\tfrac12\); for \(m=1\) and \(m=3\) the half-gaps have \(Y\le1\); for \(m\ge4\), \(Y\le\tfrac32\). So \(E\) is at most the largest of the four numbers \(E(0,\tfrac12,0)\), \(E(1,1,2)\), \(E(3,1,2)\), \(E(4,\tfrac32,2)\). The numbers \(|z(t_j)|\) for \(j=0,\dots,5\) are at most \(2.934\), \(2.713\), \(2.268\), \(1.859\), \(1.548\), \(1.320\), and the numbers \(\pi\operatorname{Im}z(t_j)\) for \(j=1,\dots,6\) are at least \(7.666\), \(4.923\), \(2.829\), \(1.515\), \(0.704\), \(0.187\). With these values the four numbers are less than \(3.1\cdot10^{-20}\), \(2.5\cdot10^{-12}\), \(5.7\cdot10^{-17}\) and \(2\cdot10^{-11}\). \(\blacksquare\)

The third comparison concerns the target. The parameter range is divided by the *endpoints*
\[
2.36,\quad2.65,\quad3.2,\quad4,\quad6,\quad\infty .
\]
For two consecutive endpoints \(K<J\) and a half-gap, define numbers \(a_0^*,\dots,a_{40}^*\) as follows:

- for the centre \(m=0\): \(a_r^*=\dfrac{e^K}K\,\dfrac{(-Ky)^r}{r!}\);
- for the centre \(m=1\): \(a_r^*=K\,\dfrac{(-Ky)^r}{(r+2)!}\);
- for the centre \(m=3\), if \(J<\infty\): \(a_0^*=\dfrac J2\,e^{-13J/6}\) and \(a_r^*=0\) for \(r\ge1\);
- in all other cases \(a_r^*=0\) for all \(r\).

**Proposition 2.3.** Let \(K<J\) be consecutive endpoints and \(K\le k\le J\), or \(k\ge K\) if \(J=\infty\). On every half-gap, for \(0\le x\le1\),
\[
\mathcal D_mT_k(m+yx)\ge\sum_{r=0}^{40}a_r^*\,x^r-10^{-6}.
\]

**Proof.** *The centre \(0\).* Here \(0\le s\le\tfrac12\). Since \(T_k(s)=k^{-1}e^{-k(s-1)}\),
\[
\frac{\partial T_k(s)}{\partial k}=T_k(s)\Bigl(1-s-\frac1k\Bigr)>0
\]
for \(k>2\). So \(T_k(s)\ge T_K(s)=\tfrac{e^K}Ke^{-Ks}\), and with \(s=yx\) the Taylor coefficients of the right side are the numbers \(a_r^*\). The terms of degree above \(40\) are bounded in absolute value by
\[
\begin{aligned}
\frac{e^K}K\sum_{r\ge41}\frac{(K|y|)^r}{r!}&\le\frac{e^6}6\cdot\frac{3^{41}}{41!\,(1-\frac3{42})}\\
&<8\cdot10^{-29},
\end{aligned}
\]
because \(K\le6\) for every pair of consecutive endpoints, \(K|y|\le3\), and \(e^K/K\) increases for \(K>1\).

*The centre \(1\).* With \(u=s-1\) we have \(T_k(1)=1/k\), \(T_k'(1)=-1\), and
\[
\mathcal D_1T_k(1+u)=\frac{e^{-ku}-1+ku}{k\,u^2}.
\]
Its derivative with respect to \(k\) is
\[
\frac{1-(1+ku)\,e^{-ku}}{k^2u^2}\ge0,
\]
by \(e^{ku}\ge1+ku\); this holds for positive and negative \(u\), and the value \(k/2\) at \(u=0\) increases with \(k\) as well. So the quotient is at least its value for \(k=K\), whose expansion in powers of \(u=yx\) has the coefficients \(K(-Ky)^r/(r+2)!\). Here \(|y|\le1\), and the terms of degree above \(40\) are bounded by
\[
\begin{aligned}
\sum_{r\ge41}\frac{K\,(K|y|)^r}{(r+2)!}&\le\frac{6\cdot6^{41}}{43!\,(1-\frac6{44})}\\
&<10^{-20}.
\end{aligned}
\]

*All centres \(m>0\).* By Lemma 1.2(1) and \(T_k''(s)=k\,e^{-k(s-1)}\),
\[
\begin{aligned}
&\mathcal D_mT_k(m+u)\\
&\quad=k\int_0^1(1-v)\,e^{-k(m-1+vu)}\,dv\ge0 .
\end{aligned}
\]
This is the claim in all cases in which the numbers \(a_r^*\) are \(0\).

*The centre \(3\) with \(J<\infty\).* Here \(-1\le u\le\tfrac12\), so the exponent is \(-ka\) with \(a=2+vu\ge1\). The function \(k\mapsto k\,e^{-ak}\) decreases for \(k\ge1/a\), in particular for \(k\ge2.36\). So the quotient is at least
\[
J\int_0^1(1-v)\,e^{-J(2+vu)}\,dv .
\]
The function \(2(1-v)\) is a probability density on \([0,1]\) with mean \(\tfrac13\), and the exponential function is convex. By the inequality of Jensen the integral is at least \(\tfrac12e^{-J(2+u/3)}\), and \(2+u/3\le\tfrac{13}6\). \(\blacksquare\)

## 3. The reduction

For a half-gap, \(i=1,2\), and \(k\) in the parameter interval from \(K\) to \(J\), let
\[
\Phi_i(x;k)=\sum_{r=0}^{40}\bigl(l_{i,r}\,q(k)+\delta_i\,a_r^*\bigr)\,x^r .
\]
This is a polynomial of degree at most \(40\) in \(x\). Its coefficients are given by explicit finite formulas: the rows \(l_{i,r}\) through the matrices \(X_1,X_2\) and the quadrature rule, the numbers \(a_r^*\) through \(K\) and \(J\), and \(q(k)\) through \(k\).

**Theorem 3.1.** Let \(k\ge2.36\), and let \(K<J\) be consecutive endpoints with \(K\le k\le J\), or \(k\ge K\) if \(J=\infty\). On every half-gap, for \(i=1,2\) and \(0\le x\le1\),
\[
\mathcal D_mF_i(m+yx)>\Phi_i(x;k)-0.000112 .
\]
Consequently, if \(\Phi_i(x;k)\ge0.001\) for all \(0\le x\le1\), on all half-gaps and for \(i=1,2\), then \(F_1\ge0\) and \(F_2\ge0\) on \([0,89.5]\).

**Proof.** By the formula for \(\mathcal D_mF_i\) at the end of Section 1,
\[
\begin{aligned}
\mathcal D_mF_i={}&\sigma_i\,\mathcal D_m(H_i-H_i^{\mathrm{ref}})\\
&+\sigma_i\,\mathcal D_mH_i^{\mathrm{ref}}+\delta_i\,\mathcal D_mT_k .
\end{aligned}
\]
By Proposition 2.1 the first term is larger than \(-0.00011\). By Proposition 2.2 the second is larger than \(\sum_{r\le40}l_{i,r}q(k)x^r-10^{-6}\). By Proposition 2.3 the third is at least \(\delta_i(\sum_{r\le40}a_r^*x^r-10^{-6})\). Adding gives the inequality. If \(\Phi_i\ge0.001\), then \(\mathcal D_mF_i>0\) on the half-gap. For \(m=0\) this is \(F_i>0\); for \(m>0\) it gives \(F_i(s)=(s-m)^2\mathcal D_mF_i(s)\ge0\). The half-gaps cover \([0,89.5]\) by Lemma 1.1. \(\blacksquare\)

So the two sign conditions on \([0,89.5]\), for all \(k\ge2.36\), are reduced to lower bounds for \(91\cdot2\) families of polynomials of degree \(40\), each family depending on the parameter \(k\) through the ten numbers \(q(k)\).

## 4. Exercises

**4.1.** List the half-gaps with the centres \(0,1,3,4\), with their numbers \(y\).

**4.2.** Let \(u(s)=(s-m)^2g(s)\) with a twice continuously differentiable function \(g\). Show \(\mathcal D_mu=g\).

**4.3.** Verify the formula
\[
\mathcal D_1T_k(1+u)=\frac{e^{-ku}-1+ku}{k\,u^2}
\]
and its expansion in powers of \(u\).

**4.4.** Why is the quotient \(\mathcal D_m\) applied to \(H_i-H_i^{\mathrm{ref}}\), which need not vanish at \(m\), and not the division of \(H_i-H_i^{\mathrm{ref}}\) by \((s-m)^2\)?

## 5. Solutions

**4.1.** Centre \(0\): the half-gap \([0,\tfrac12]\), \(y=\tfrac12\). Centre \(1\): \([\tfrac12,1]\) with \(y=-\tfrac12\) and \([1,2]\) with \(y=1\). Centre \(3\): \([2,3]\) with \(y=-1\) and \([3,3.5]\) with \(y=\tfrac12\). Centre \(4\): \([3.5,4]\) with \(y=-\tfrac12\) and \([4,5.5]\) with \(y=\tfrac32\).

**4.2.** \(u(m)=0\) and \(u'(m)=0\), so \(\mathcal D_mu(s)=u(s)/(s-m)^2=g(s)\) for \(s\ne m\). At \(s=m\), \(u''(m)=2g(m)\), so \(\mathcal D_mu(m)=g(m)\).

**4.3.** \(T_k(1+u)=e^{-ku}/k\), \(T_k(1)=1/k\) and \(T_k'(1)=-1\), so the numerator of the quotient is \((e^{-ku}-1+ku)/k\). Since \(e^{-ku}-1+ku=\sum_{j\ge2}(-ku)^j/j!\), division by \(ku^2\) gives \(\sum_{r\ge0}K_r\,u^r\) with \(K_r=k\,(-k)^r/(r+2)!\).

**4.4.** The difference \(H_i-H_i^{\mathrm{ref}}\) is small, of the order \(10^{-7}\), but it does not vanish at \(m\); divided by \((s-m)^2\) it would be unbounded near \(m\). The quotient \(\mathcal D_m\) first removes the value and the slope at \(m\), and is bounded by half the second derivative. The exact slack \(F_i\) has zero value and slope at \(m\), so for it the quotient is the true division, and \(\mathcal D_m\) is linear.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 5. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
