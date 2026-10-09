# Positive solutions and their potentials

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson reduces the theorem of [Spherical means and Newton potentials](spherical-means-and-newton-potentials.md) to a bound, uniform over all solutions, for a localized energy (Proposition 5.1). It follows [OpenAI-LE, Section 2]. Fix an integer \(n\ge2\), exponents \(p,q>0\) and weights \(A,B\in\mathbb R\). A *solution* is a pair of functions \(u,v\) that are continuous and positive on \(\mathbb R^n\), twice continuously differentiable on \(\mathbb R^n\setminus\{0\}\), and satisfy
\[
-\Delta u=|x|^Av^p,\qquad-\Delta v=|x|^Bu^q\qquad\text{on }\mathbb R^n\setminus\{0\}.\tag{0.1}
\]
Results of [Spherical means and Newton potentials](spherical-means-and-newton-potentials.md) are cited as "Lemma 2.1 of the first lesson" and so on, and its notation is kept. A constant is *universal* if it depends only on \(n,p,q,A,B\) and on auxiliary parameters named explicitly, but not on the solution.

## 1. Reductions at the origin

**Lemma 1.1** (OpenAI). If a solution exists, then \(n\ge3\), \(A>-2\) and \(B>-2\).

**Proof.** By Lemma 2.1 of the first lesson, the flux \(F_u(r)=r^{n-1}\overline u\,'(r)\) satisfies
\[
F_u'(r)=-r^{n-1+A}\,\overline{v^p}(r)<0\qquad(r>0),\tag{1.1}
\]
since \(|x|^A\) is constant on spheres; so \(F_u\) is strictly decreasing, and its limit \(L\in(-\infty,\infty]\) as \(r\downarrow0\) exists. If \(L\neq0\), then for small \(r\) the flux has a fixed sign and \(|F_u|\ge\kappa>0\); integrating \(\overline u\,'(r)=F_u(r)r^{1-n}\) against \(\int_0r^{1-n}\,dr=\infty\) shows that \(\overline u(r)\) is unbounded as \(r\downarrow0\), contradicting \(\overline u(r)\to u(0)\). So \(L=0\), and \(F_u(r)<0\) for every \(r>0\). The same holds for \(v\).

If \(n=2\), then \(r\overline u\,'(r)\le F_u(1)<0\) for \(r\ge1\), so \(\overline u(r)\le\overline u(1)+F_u(1)\log r\), which becomes negative; this contradicts \(u>0\).

Let \(n\ge3\). Since \(v\) is continuous and \(v(0)>0\), there are \(c>0\) and \(r_0>0\) with \(v^p\ge c\) on \(B_{r_0}\). For \(r<r_0\), integrating (1.1) over \([r/2,r]\) and using \(F_u(r/2)<0\),
\[
-\overline u\,'(r)=-r^{1-n}F_u(r)\ge c\,r^{1-n}\int_{r/2}^rs^{n-1+A}\,ds=c_A\,r^{1+A}
\]
with a constant \(c_A>0\) (the integral is \(r^{n+A}\) times a positive constant, which is \(\log2\) when \(n+A=0\)). If \(A\le-2\), then \(\int_0r^{1+A}\,dr=\infty\), and \(\overline u(r)=\overline u(r_0)+\int_r^{r_0}(-\overline u\,')\to\infty\) as \(r\downarrow0\), contradicting the continuity of \(u\) at \(0\). So \(A>-2\), and in the same way \(B>-2\). \(\square\)

From now on \(n\ge3\) and \(A,B>-2\). Define the *sources*
\[
f(x)=|x|^Bu(x)^q,\qquad g(x)=|x|^Av(x)^p\quad(x\neq0),\qquad f(0)=g(0)=0,
\]
so that \(-\Delta u=g\) and \(-\Delta v=f\) off the origin. Near \(0\), \(f\le C|x|^B\) and \(g\le C|x|^A\) with a constant depending on the solution, and \(n+A,n+B>0\); so \(f\) and \(g\) are locally integrable.

## 2. Potentials

**Proposition 2.1.** For every solution, \(-\Delta u=g\) and \(-\Delta v=f\) in distributions on \(\mathbb R^n\), and
\[
K*g\le u,\qquad K*f\le v\qquad\text{on }\mathbb R^n .
\]
There are constants \(c_u,c_v\ge0\) with \(u=c_u+K*g\) and \(v=c_v+K*f\) on \(\mathbb R^n\setminus\{0\}\). The potentials are continuously differentiable off the origin, with
\[
\nabla u(x)=\int\nabla K(x-y)g(y)\,dy,\qquad\nabla v(x)=\int\nabla K(x-y)f(y)\,dy,\qquad\nabla K(z)=-(n-2)\frac{z}{|z|^2}K(z),
\]
both integrals converging absolutely for \(x\neq0\).

**Proof.** The sources are nonnegative, locally integrable, and continuous off the origin, so Lemma 3.2 and Proposition 3.3 of the first lesson apply to \((u,g)\) and to \((v,f)\). \(\square\)

For \(x,y\in B_R\) we have \(|x-y|<2R\), hence \(K(x-y)\ge c_n(2R)^{2-n}\). With Proposition 2.1 this gives the *ball bounds*
\[
u(x)\ge c\,R^{2-n}\int_{B_R}g,\qquad v(x)\ge c\,R^{2-n}\int_{B_R}f\qquad(x\in B_R),\tag{2.1}
\]
with \(c>0\) depending only on \(n\).

## 3. Small products and scaling

**Lemma 3.1** (OpenAI). Every solution has \(pq>1\).

**Proof.** Let \(m_u(R)=\min_{\overline B_R}u>0\) and \(m_v(R)=\min_{\overline B_R}v>0\). Inserting \(g\ge|x|^Am_v(R)^p\) and \(f\ge|x|^Bm_u(R)^q\) on \(B_R\) into (2.1), and using \(\int_{B_R}|x|^A\,dx=\frac{|S|}{n+A}R^{n+A}\),
\[
m_u(R)\ge c\,R^{2+A}m_v(R)^p,\qquad m_v(R)\ge c\,R^{2+B}m_u(R)^q .
\]
Combining them, \(m_u(R)^{1-pq}\ge c\,R^{2+A+p(2+B)}\), and the exponent on the right is positive. If \(pq<1\), the left side is at most \(u(0)^{1-pq}\); if \(pq=1\), it is \(1\). Either way \(R\to\infty\) gives a contradiction. \(\square\)

From now on also \(pq>1\). Define
\[
\alpha=\frac{2+A+p(2+B)}{pq-1},\qquad\beta=\frac{2+B+q(2+A)}{pq-1},\qquad a=\frac1{q+1},\qquad b=\frac1{p+1}.\tag{3.1}
\]
Then \(\alpha,\beta>0\), and
\[
p\beta=\alpha+2+A,\qquad q\alpha=\beta+2+B .\tag{3.2}
\]

**Lemma 3.2** (scaling). For every solution and every \(R>0\), the pair \(u_R(x)=R^\alpha u(Rx)\), \(v_R(x)=R^\beta v(Rx)\) is a solution, with sources \(f_R(x)=R^{\beta+2}f(Rx)\) and \(g_R(x)=R^{\alpha+2}g(Rx)\).

**Proof.** \(-\Delta u_R(x)=R^{\alpha+2}g(Rx)=R^{\alpha+2+A}|x|^Av(Rx)^p=R^{\alpha+2+A-p\beta}|x|^Av_R(x)^p=|x|^Av_R(x)^p\) by (3.2), and similarly for \(v_R\); also \(f_R(x)=|x|^Bu_R(x)^q=R^{q\alpha-B}f(Rx)=R^{\beta+2}f(Rx)\). \(\square\)

The dilations are centered at the origin, where the weights are centered; translations do not preserve (0.1).

## 4. Centered estimates

**Proposition 4.1** (OpenAI). There is a universal constant \(C\) such that every solution satisfies, for all \(R>0\),
\[
\int_{B_R}f\le C\,R^{n-2-\beta},\qquad\int_{B_R}g\le C\,R^{n-2-\alpha}.\tag{4.1}
\]
The constants of Proposition 2.1 vanish: \(u=K*g\) and \(v=K*f\) on \(\mathbb R^n\setminus\{0\}\). Moreover
\[
\int_{B_4}(f+g+u+v)\le C,\qquad\int_{|x-y|\ge\ell}K(x-y)\bigl(f(y)+g(y)\bigr)\,dy\le C\ell^{2-n}\quad(x\in B_2,\ 0<\ell\le1).\tag{4.2}
\]

**Proof.** *Unit ball.* Let \(M_f=\int_{B_1}f\) and \(M_g=\int_{B_1}g\), both positive. By (2.1) with \(R=1\), \(u\ge cM_g\) and \(v\ge cM_f\) on \(B_1\), so \(M_f\ge c_fM_g^q\) and \(M_g\ge c_gM_f^p\) with universal \(c_f,c_g>0\). Hence \(M_f\ge c_fc_g^qM_f^{pq}\), and since \(pq>1\) this bounds \(M_f\) by a universal constant; likewise \(M_g\). Applied to the scaled solution of Lemma 3.2, \(\int_{B_1}f_R=R^{\beta+2-n}\int_{B_R}f\le C\), which is (4.1).

*No constants.* If \(c_u>0\), then \(u\ge c_u\) off the origin, so \(\int_{B_R}f\ge c_u^q\frac{|S|}{n+B}R^{n+B}\). Since \((n+B)-(n-2-\beta)=\beta+2+B=q\alpha>0\), this contradicts (4.1) for large \(R\). So \(c_u=0\), and likewise \(c_v=0\).

*Far sources.* Let \(x\in B_4\) and \(j\ge3\). On the shell \(2^j\le|y|<2^{j+1}\) we have \(|x-y|\ge2^{j-1}\), so its contribution to \(K*f(x)\) is at most \(c_n2^{(j-1)(2-n)}\int_{B_{2^{j+1}}}f\le C2^{-j\beta}\), and its contribution to \(K*g(x)\) is at most \(C2^{-j\alpha}\). Summing over \(j\), the potentials of \(f\mathbf 1_{\{|y|\ge8\}}\) and \(g\mathbf 1_{\{|y|\ge8\}}\) are bounded by a universal constant on \(B_4\).

*Near sources.* Since \(\int_{B_4}K(x-y)\,dx\le\int_{B_{12}}K\) for \(y\in B_8\), Tonelli's theorem and (4.1) bound \(\int_{B_4}K*(g\mathbf 1_{B_8})\) and \(\int_{B_4}K*(f\mathbf 1_{B_8})\). With \(u=K*g\) and \(v=K*f\), this proves the bound on \(\int_{B_4}(u+v)\), and (4.1) bounds \(\int_{B_4}(f+g)\).

*Tails.* For \(|x-y|\ge\ell\), \(K(x-y)\le c_n\ell^{2-n}\), so the sources in \(B_8\) contribute at most \(C\ell^{2-n}\); the sources outside \(B_8\) contribute at most \(C\le C\ell^{2-n}\), because \(\ell\le1\) and \(n\ge3\). \(\square\)

The estimates are centered at the origin; a ball \(B_\ell(x)\subseteq B_4\) has source mass at most that of \(B_4\). For each solution, the *energy densities* \(fu=|x|^Bu^{q+1}\) and \(gv=|x|^Av^{p+1}\) are locally integrable, but no bound on them uniform over solutions is known at this point.

## 5. The energy and the plan

Let
\[
\gamma=a(n+B)+b(n+A)-(n-2)=\frac{n+B}{q+1}+\frac{n+A}{p+1}-(n-2),
\]
so that the hypothesis of the theorem is \(\gamma>0\). A computation with (3.1) gives
\[
\gamma=(1-a-b)\,(\alpha+\beta+2-n),\qquad1-a-b=\frac{pq-1}{(p+1)(q+1)}>0,\tag{5.1}
\]
so \(\gamma>0\) implies \(\alpha+\beta+2-n>0\). Changing variables in Lemma 3.2,
\[
\int_{B_1}\bigl(f_Ru_R+g_Rv_R\bigr)=R^{\alpha+\beta+2-n}\int_{B_R}(fu+gv).\tag{5.2}
\]

**Proposition 5.1** (uniform energy bound; OpenAI). Let \(n\ge3\), \(A,B>-2\), \(pq>1\) and \(\gamma>0\). There is a universal constant \(C\) such that every solution satisfies
\[
\int_{B_1}\bigl(|x|^Bu^{q+1}+|x|^Av^{p+1}\bigr)\,dx\le C .
\]

Proposition 5.1 is proved in [Pressure and the energy bound](pressure-and-the-energy-bound.md), after [A localized virial identity](a-localized-virial-identity.md) and [Intervals and source layers](intervals-and-source-layers.md).

**Theorem 5.2** (OpenAI 2026). Let \(n\ge2\), \(p,q>0\), \(A,B\in\mathbb R\) and \(\gamma>0\). Then (0.1) has no solution.

**Proof, given Proposition 5.1.** Lemmas 1.1 and 3.1 exclude \(n=2\), weights \(A\le-2\) or \(B\le-2\), and \(pq\le1\). In the remaining range, apply Proposition 5.1 to every scaled solution of Lemma 3.2. By (5.2), \(R^{\alpha+\beta+2-n}\int_{B_R}(fu+gv)\le C\) for all \(R>0\). For \(R\ge1\) the integral is at least \(\int_{B_1}(fu+gv)>0\), and \(\alpha+\beta+2-n>0\) by (5.1), so the left side tends to infinity, a contradiction. \(\square\)

**Corollary 5.3** (the Lane–Emden conjecture). For \(n\ge3\) and \(p,q>0\) with \(\frac1{p+1}+\frac1{q+1}>\frac{n-2}n\), the system \(-\Delta u=v^p\), \(-\Delta v=u^q\) has no positive twice continuously differentiable solution on \(\mathbb R^n\).

**Proof.** Take \(A=B=0\); the condition is \(\gamma>0\) divided by \(n\). \(\square\)

## 6. Exercises

**Exercise 6.1** (easy). Verify (3.2) and (5.1).

**Exercise 6.2** (easy). Show that \(n=5\), \(p=q=4\), \(A=B=3\) satisfies \(\gamma>0\), although \(\frac1{p+1}+\frac1{q+1}<\frac{n-2}n\). Why can the weighted theorem not be deduced from the unweighted one at the same exponents?

**Exercise 6.3** (medium). Show that the strict inequality \(\gamma>0\) cannot be weakened to \(\gamma\ge0\): for \(A=B=0\), \(n\ge3\) and \(p=q=\frac{n+2}{n-2}\), check that \(\gamma=0\) and that \(u=v=\bigl(n(n-2)\bigr)^{(n-2)/4}(1+|x|^2)^{-(n-2)/2}\) is a positive solution.

**Exercise 6.4** (medium). Let \(pq>1\). Show from the two inequalities in the proof of Lemma 3.1 that \(\min_{\overline B_R}u\le CR^{-\alpha}\) for all \(R>0\), with a universal \(C\), and explain why this agrees with the scaling of Lemma 3.2.

## 7. Solutions

**6.1.** \(p\beta-\alpha=\frac{p(2+B)+pq(2+A)-(2+A)-p(2+B)}{pq-1}=2+A\), and symmetrically \(q\alpha-\beta=2+B\). Next \((1-a-b)(\alpha+\beta)=\frac{(q+1)(2+A)+(p+1)(2+B)}{(p+1)(q+1)}=b(2+A)+a(2+B)\), and \((1-a-b)(2-n)=(2-n)-a(2-n)-b(2-n)\); adding gives \(a(n+B)+b(n+A)-(n-2)=\gamma\).

**6.2.** \(\gamma=\frac85+\frac85-3=\frac15>0\), while \(\frac15+\frac15=\frac25<\frac35\). The unweighted theorem at \(p=q=4\) in dimension \(5\) is not available (those exponents are not subcritical without weights), and the weights change the equation, so neither statement implies the other at these exponents.

**6.3.** \(\gamma=\frac{2n}{p+1}-(n-2)=\frac{2n(n-2)}{2n}-(n-2)=0\). For \(U=(1+r^2)^{-k}\) with \(k=\frac{n-2}2\), \(U''+\frac{n-1}rU'=(1+r^2)^{-k-2}\bigl(-2kn(1+r^2)+4k(k+1)r^2\bigr)=-n(n-2)(1+r^2)^{-(n+2)/2}\), since \(2kn=4k(k+1)=n(n-2)\). So \(-\Delta U=n(n-2)U^{(n+2)/(n-2)}\), and \(u=\lambda U\) with \(\lambda^{4/(n-2)}=n(n-2)\) satisfies \(-\Delta u=u^{(n+2)/(n-2)}\).

**6.4.** From \(m_u(R)\ge cR^{2+A}m_v(R)^p\) and \(m_v(R)\ge cR^{2+B}m_u(R)^q\) we get \(m_u(R)\ge c\,R^{2+A+p(2+B)}m_u(R)^{pq}\), that is, \(m_u(R)^{pq-1}\le CR^{-(2+A+p(2+B))}\), or \(m_u(R)\le CR^{-\alpha}\). The scaled solution \(u_R(x)=R^\alpha u(Rx)\) has \(\min_{\overline B_1}u_R=R^\alpha m_u(R)\), and the bound says exactly that this is at most \(C\), the same estimate for the solution \(u_R\) on the unit ball.

## References

- [OpenAI-LE] OpenAI, *The subcritical Hénon–Lane–Emden conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
