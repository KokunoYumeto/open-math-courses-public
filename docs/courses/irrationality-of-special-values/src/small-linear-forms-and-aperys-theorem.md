# Small linear forms and Apéry's theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A real number \(x\) is irrational as soon as there are integers \(a_n,b_n\) with \(a_n+b_nx\ne0\) and \(a_n+b_nx\to0\). Producing such linear forms is the whole difficulty: natural approximations to a constant come with denominators, and clearing them can destroy the decay. In 1978 Apéry showed that \(\zeta(3)=\sum_{k\ge1}k^{-3}\) is irrational, with an explicit recurrence whose denominators grow just slowly enough; shortly afterwards Beukers found a short proof by double and triple integrals. This lesson proves the irrationality of \(\zeta(2)\) and \(\zeta(3)\) along Beukers' lines. The argument is organized around two facts: zeta values are integrals of powers of a logarithm against \(dt/(1-t)\), and an involution of the unit interval transports Beukers' triple integral into a form whose size is easy to bound.

The last section explains why the same idea does not prove the irrationality of Catalan's constant \(G=\sum_{j\ge0}(-1)^j(2j+1)^{-2}\), and how the rest of this course overcomes the obstacle.

We use the prime number theorem, Theorem 3.1 of [The prime number theorem](course:NT-ZETA/NT-ZETA-09#3-from-an-average-to-the-number-of-primes), and integration of nonnegative functions with monotone convergence and Fubini's theorem, as in the core course [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10).

Basic references are [Fischler] and [Zudilin 2003].

## 1. Irrationality from small linear forms

**Lemma 1.1.** Let \(x\) be a real number. Suppose there are integers \(a_n,b_n\) with \(a_n+b_nx\ne0\) for every \(n\) and \(a_n+b_nx\to0\). Then \(x\) is irrational.

**Proof.** If \(x=u/v\) with integers \(u\) and \(v\ge1\), then \(v(a_n+b_nx)=va_n+b_nu\) is a nonzero integer, so \(|a_n+b_nx|\ge1/v\) for every \(n\). \(\square\)

The linear forms below arise as \(d_n^k\) times an integral, where

\[
d_n=\operatorname{lcm}(1,2,\dots,n).
\]

Every fraction \(1/j\) with \(1\le j\le n\) becomes an integer after multiplication by \(d_n\), and every fraction \(1/(jk)\) with \(1\le j,k\le n\) after multiplication by \(d_n^2\). The size of \(d_n\) is governed by the primes.

**Lemma 1.2.** \(\log d_n=\psi(n)=\sum_{p^k\le n}\log p\). Consequently, for every \(\varepsilon>0\), \(d_n\le e^{(1+\varepsilon)n}\) for all sufficiently large \(n\).

**Proof.** The exponent of a prime \(p\) in \(d_n\) is the largest \(k\) with \(p^k\le n\), which is the number of powers \(p^k\le n\) with \(k\ge1\). Taking logarithms gives \(\psi(n)\). The prime number theorem gives \(\psi(n)\sim n\). \(\square\)

## 2. Zeta values as integrals

**Proposition 2.1** (logarithmic integrals). For integers \(m\ge1\) and \(N\ge0\),

\[
\int_0^1\frac{t^N(-\log t)^m}{1-t}\,dt=m!\sum_{k>N}\frac1{k^{m+1}}.
\]

In particular \(\int_0^1(-\log t)^m\,dt/(1-t)=m!\,\zeta(m+1)\).

**Proof.** For \(a>-1\), the substitution \(t=e^{-u/(a+1)}\) gives \(\int_0^1t^a(-\log t)^m\,dt=(a+1)^{-m-1}\int_0^\infty u^me^{-u}\,du=m!/(a+1)^{m+1}\), the last integral by \(m\) integrations by parts. Expand \(1/(1-t)=\sum_{j\ge0}t^j\); all terms are nonnegative, so monotone convergence permits termwise integration, and \(\sum_{j\ge0}m!/(N+j+1)^{m+1}\) is the stated sum. \(\square\)

Double integrals over the unit square reduce to single integrals when the integrand depends only on the product of the variables.

**Lemma 2.2** (integration over the product). For every measurable \(F:(0,1)\to[0,\infty]\),

\[
\iint_{[0,1]^2}F(xy)\,dx\,dy=\int_0^1F(t)\,(-\log t)\,dt.
\]

The same holds for integrable \(F\) of either sign.

**Proof.** For fixed \(x\in(0,1]\), substituting \(t=xy\) gives \(\int_0^1F(xy)\,dy=\int_0^xF(t)\,dt/x\). Integrate over \(x\) and exchange the order of integration on \(\{0<t<x<1\}\), which is allowed for nonnegative integrands: the result is \(\int_0^1F(t)\int_t^1dx/x\,dt\), and \(\int_t^1dx/x=-\log t\). For integrable \(F\), apply this to the positive and negative parts. \(\square\)

**Proposition 2.3** (monomial integrals). For integers \(r,s\ge0\),

\[
\iint_{[0,1]^2}\frac{x^ry^s}{1-xy}\,dx\,dy=
\begin{cases}
\zeta(2)-\sum_{k=1}^r\frac1{k^2},&r=s,\\[4pt]
\frac1{|r-s|}\sum_{k=\min(r,s)+1}^{\max(r,s)}\frac1k,&r\ne s,
\end{cases}
\]

and

\[
\iint_{[0,1]^2}\frac{-\log(xy)\,x^ry^s}{1-xy}\,dx\,dy=
\begin{cases}
2\Bigl(\zeta(3)-\sum_{k=1}^r\frac1{k^3}\Bigr),&r=s,\\[4pt]
\frac1{|r-s|}\sum_{k=\min(r,s)+1}^{\max(r,s)}\frac1{k^2},&r\ne s.
\end{cases}
\]

**Proof.** Expand \(1/(1-xy)=\sum_{j\ge0}(xy)^j\) and integrate termwise (all terms are nonnegative). The first integral becomes \(\sum_{j\ge0}1/(AB)\) with \(A=r+j+1\), \(B=s+j+1\). If \(r=s\) this is \(\sum_{k>r}k^{-2}\). If \(r>s\), then \(A-B=r-s\) and \(1/(AB)=(1/B-1/A)/(r-s)\); the sum telescopes to \(\sum_{k=s+1}^rk^{-1}/(r-s)\).

For the second, \(\int_0^1x^a(-\log x)\,dx=1/(a+1)^2\) (Proposition 2.1's computation with \(m=1\)), and \(-\log(xy)=-\log x-\log y\). So the integral is \(\sum_{j\ge0}\bigl(1/(A^2B)+1/(AB^2)\bigr)=\sum_j(A+B)/(A^2B^2)\). If \(r=s\) this is \(2\sum_{k>r}k^{-3}\). If \(r>s\), then \((A+B)/(A^2B^2)=(1/B^2-1/A^2)/(r-s)\), which telescopes to \(\sum_{k=s+1}^rk^{-2}/(r-s)\). \(\square\)

For \(r=s\) the second formula is also Lemma 2.2 with \(F(t)=t^r(-\log t)/(1-t)\), followed by Proposition 2.1 with \(m=2\) and \(N=r\).

**Corollary 2.4.** Let \(Q(x,y)\) be a polynomial with integer coefficients and degree at most \(n\) in each variable. Then

\[
d_n^2\iint\frac{Q(x,y)}{1-xy}\,dx\,dy\in\mathbb Z+\mathbb Z\,\zeta(2),\qquad
d_n^3\iint\frac{-\log(xy)\,Q(x,y)}{1-xy}\,dx\,dy\in\mathbb Z+2\mathbb Z\,\zeta(3).
\]

**Proof.** In Proposition 2.3 with \(r,s\le n\), every denominator \(|r-s|\cdot k\) and \(k^2\) divides \(d_n^2\), and every \(|r-s|\cdot k^2\) and \(k^3\) divides \(d_n^3\). \(\square\)

## 3. Legendre polynomials

For \(n\ge0\) put

\[
P_n(x)=\frac1{n!}\frac{d^n}{dx^n}\bigl(x^n(1-x)^n\bigr).
\]

**Lemma 3.1.** \(P_n(x)=\sum_{j=0}^n(-1)^j\binom nj\binom{n+j}nx^j\). In particular \(P_n\) has integer coefficients and degree \(n\).

**Proof.** \(x^n(1-x)^n=\sum_j(-1)^j\binom njx^{n+j}\), and \(\frac1{n!}\frac{d^n}{dx^n}x^{n+j}=\binom{n+j}nx^j\). \(\square\)

**Lemma 3.2** (integration by parts). For every \(g\) that is \(n\) times continuously differentiable on \([0,1]\),

\[
\int_0^1P_n(x)g(x)\,dx=\frac{(-1)^n}{n!}\int_0^1x^n(1-x)^ng^{(n)}(x)\,dx.
\]

**Proof.** Integrate by parts \(n\) times. The boundary terms involve derivatives of \(x^n(1-x)^n\) of order less than \(n\), which vanish at \(0\) and \(1\) because each has the factor \(x(1-x)\). \(\square\)

## 4. The irrationality of \(\zeta(2)\)

**Lemma 4.1.** For \(0\le x,y\le1\),

\[
\frac{x(1-x)y(1-y)}{1-xy}\le\varphi^5,\qquad\varphi=\frac{\sqrt5-1}2,
\]

with the left side read as \(0\) at \(x=y=1\).

**Proof.** Put \(u=\sqrt{xy}\). Since \(x+y\ge2u\), we have \((1-x)(1-y)=1-(x+y)+xy\le(1-u)^2\). Hence the left side is at most \(u^2(1-u)^2/(1-u^2)=g(u)\), where \(g(u)=u^2(1-u)/(1+u)\) on \([0,1)\). Now

\[
g'(u)=\frac{2u(1-u-u^2)}{(1+u)^2},
\]

so \(g\) increases up to the root \(u=\varphi\) of \(u^2+u-1=0\) and decreases after it. Using \(1-\varphi=\varphi^2\) and \(1+\varphi=1/\varphi\), the maximum is \(g(\varphi)=\varphi^2\cdot\varphi^2\cdot\varphi=\varphi^5\). \(\square\)

**Theorem 4.2.** \(\zeta(2)\) is irrational. Consequently \(\pi^2\) is irrational, because \(\zeta(2)=\pi^2/6\).

**Proof.** For \(n\ge1\) put

\[
I_n=\iint_{[0,1]^2}\frac{(1-y)^nP_n(x)}{1-xy}\,dx\,dy.
\]

By Lemma 3.1 and Corollary 2.4, \(d_n^2I_n=a_n+b_n\zeta(2)\) with integers \(a_n,b_n\). For fixed \(y\in[0,1)\), the function \(g(x)=1/(1-xy)\) has \(g^{(n)}(x)=n!\,y^n/(1-xy)^{n+1}\), so Lemma 3.2 gives

\[
I_n=(-1)^n\iint_{[0,1]^2}\frac{x^n(1-x)^ny^n(1-y)^n}{(1-xy)^{n+1}}\,dx\,dy.
\]

The integrand is positive inside the square, so \(I_n\ne0\). By Lemma 4.1 the integrand is at most \(\varphi^{5n}/(1-xy)\), and \(\iint dx\,dy/(1-xy)=\zeta(2)\) by Proposition 2.3. Therefore

\[
0<|a_n+b_n\zeta(2)|\le d_n^2\varphi^{5n}\zeta(2).
\]

Since \(e^2\varphi^5<0.67\), Lemma 1.2 with a small \(\varepsilon\) makes the right side tend to \(0\). Lemma 1.1 proves the theorem. \(\square\)

## 5. An involution of the unit interval and \(\zeta(3)\)

Beukers' proof for \(\zeta(3)\) uses a third variable. By Proposition 2.1 and Lemma 2.2,

\[
\frac{-\log t}{1-t}=\int_0^1\frac{dz}{1-(1-t)z}\qquad(0<t<1),
\tag{5.1}
\]

as one checks directly: the integral equals \(-\log(1-(1-t))/(1-t)\). Thus the measure \(dz/(1-(1-t)z)\) on \([0,1]\) has total mass \(-\log t/(1-t)\), and the logarithmic kernel of Proposition 2.3 is an integral over this family of measures, indexed by \(t=xy\).

**Lemma 5.1** (a projective involution). Fix \(0<t\le1\) and put \(c=1-t\). The map

\[
f_t(z)=\frac{1-z}{1-cz}
\]

is a decreasing bijection of \([0,1]\) onto itself with \(f_t(f_t(z))=z\), and

\[
1-f_t(z)=\frac{tz}{1-cz},\qquad 1-cf_t(z)=\frac t{1-cz},\qquad f_t'(z)=-\frac t{(1-cz)^2}.
\]

Consequently, for every integer \(n\ge0\) and every bounded measurable \(\phi\) on \([0,1]\),

\[
\int_0^1\frac{t^nz^n\,\phi(z)}{(1-cz)^{n+1}}\,dz=\int_0^1\frac{(1-w)^n\,\phi(f_t(w))}{1-cw}\,dw.
\tag{5.2}
\]

**Proof.** The three identities are direct computations: \(1-f_t(z)=(1-cz-1+z)/(1-cz)=tz/(1-cz)\); \(1-cf_t(z)=(1-cz-c+cz)/(1-cz)=t/(1-cz)\); and the quotient rule gives \(f_t'(z)=(-(1-cz)+c(1-z))/(1-cz)^2=-t/(1-cz)^2\). Then \(f_t(f_t(z))=(1-f_t(z))/(1-cf_t(z))=z\). Since \(f_t(0)=1\), \(f_t(1)=0\) and \(f_t'<0\), it is a decreasing bijection. In the left side of (5.2) substitute \(z=f_t(w)\):

\[
\frac{t^nf_t(w)^n}{(1-cf_t(w))^{n+1}}\,|f_t'(w)|
=t^n\frac{(1-w)^n}{(1-cw)^n}\cdot\frac{(1-cw)^{n+1}}{t^{n+1}}\cdot\frac t{(1-cw)^2}
=\frac{(1-w)^n}{1-cw},
\]

using \(f_t(w)=(1-w)/(1-cw)\) and the second identity applied at \(w\). \(\square\)

Applied with \(\phi(z)=(1-z)^n\), (5.2) shows that each measure \(z^n(1-z)^n\,dz/(1-cz)^{n+1}\) is invariant under \(f_t\).

**Lemma 5.2.** For \(0\le x,y,z\le1\), with the left side read as \(0\) where its denominator vanishes,

\[
\frac{x(1-x)y(1-y)z(1-z)}{1-(1-xy)z}\le(\sqrt2-1)^4.
\]

**Proof.** Put \(c=1-xy\) and \(u=\sqrt{xy}\), and assume \(0<u<1\) (otherwise the left side is \(0\)). The function \(z\mapsto z(1-z)/(1-cz)\) on \([0,1]\) has derivative with numerator \(1-2z+cz^2\), which vanishes at \(z_*=1/(1+\sqrt{1-c})=1/(1+u)\), the only root in \([0,1]\). There \(1-z_*=u/(1+u)\) and \(1-cz_*=1-(1-u)=u\), so the maximum is \(1/(1+u)^2\). As in Lemma 4.1, \(x(1-x)y(1-y)\le u^2(1-u)^2\). Hence the left side is at most \(k(u)^2\) with \(k(u)=u(1-u)/(1+u)\). Now \(k'(u)=(1-2u-u^2)/(1+u)^2\) vanishes at \(u=\sqrt2-1\), where \(k(u)=(\sqrt2-1)(2-\sqrt2)/\sqrt2=(\sqrt2-1)^2\). \(\square\)

**Theorem 5.3** (Apéry). \(\zeta(3)\) is irrational.

**Proof.** For \(n\ge1\) put

\[
J_n=\iint_{[0,1]^2}\frac{-\log(xy)\,P_n(x)P_n(y)}{1-xy}\,dx\,dy.
\]

By Lemma 3.1 and Corollary 2.4, \(d_n^3J_n=a_n+b_n\zeta(3)\) with integers \(a_n,b_n\). By (5.1) with \(t=xy\),

\[
J_n=\iiint_{[0,1]^3}\frac{P_n(x)P_n(y)}{1-(1-xy)z}\,dx\,dy\,dz,
\]

the triple integral being absolutely convergent because \(P_n\) is bounded and \(\iiint dx\,dy\,dz/(1-(1-xy)z)=2\zeta(3)\). For fixed \(y,z\) with \(yz<1\), the function \(g(x)=1/(1-z+xyz)\) has \(g^{(n)}(x)=(-1)^nn!\,(yz)^n/(1-(1-xy)z)^{n+1}\). Lemma 3.2 in \(x\) gives

\[
J_n=\iiint\frac{(xyz)^n(1-x)^nP_n(y)}{(1-(1-xy)z)^{n+1}}\,dx\,dy\,dz.
\]

Now apply (5.2) in the variable \(z\), with \(t=xy\) and \(\phi=1\), for fixed \(x,y\):

\[
J_n=\iiint\frac{(1-x)^n(1-w)^nP_n(y)}{1-(1-xy)w}\,dx\,dy\,dw.
\]

For fixed \(x,w\), the function \(y\mapsto1/(1-w+xyw)\) has \(n\)-th derivative \((-1)^nn!\,(xw)^n/(1-(1-xy)w)^{n+1}\), and Lemma 3.2 in \(y\) gives

\[
J_n=\iiint_{[0,1]^3}\frac{x^n(1-x)^ny^n(1-y)^nw^n(1-w)^n}{(1-(1-xy)w)^{n+1}}\,dx\,dy\,dw.
\]

This integrand is positive inside the cube, so \(J_n>0\); by Lemma 5.2 it is at most \((\sqrt2-1)^{4n}/(1-(1-xy)w)\), whose integral is \(2\zeta(3)\). Hence

\[
0<a_n+b_n\zeta(3)\le2\zeta(3)\,d_n^3(\sqrt2-1)^{4n}.
\]

Since \(e^3(\sqrt2-1)^4<0.6\), Lemma 1.2 makes the right side tend to \(0\), and Lemma 1.1 applies. \(\square\)

*Reference:* Apéry's original proof used an explicit recurrence; the integrals are Beukers'. Both are explained in [Fischler].

## 6. Why Catalan's constant resists

Catalan's constant is

\[
G=\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^2}=1-\frac19+\frac1{25}-\frac1{49}+\cdots=0.9159655\dots
\]

Zudilin found Apéry-like recurrences for it [Zudilin 2003]: rational numbers \(u_n,v_n\) with \(v_n/u_n\to G\) very quickly, such that \(|u_nG-v_n|^{1/n}\to\varphi^5\), as for \(\zeta(2)\), and with a double integral representation of \(u_nG-v_n\) in the style of Section 4. But the known common denominator of \(u_n\) and \(v_n\) is \(2^{4n+3}d_{2n-1}^3\), which grows roughly like \(e^{8.8n}\), while the forms decay only like \(e^{-2.4n}\); after clearing these denominators the integer linear forms do not tend to zero. This is the typical obstruction: the decay of the analytic approximation must beat the arithmetic cost of its denominators.

The rest of this course proves that \(G\) is irrational, following OpenAI's proof of September 2026 [OpenAI-Catalan]. Instead of one linear form, it uses determinants \(\Delta_N\) of size \(48N\) whose entries are rational combinations of \(1\), \(G\) and \(\zeta(2)\). Polynomial rows with high contact at the origin cancel \(\zeta(2)\) from every entry, so that if \(G\) were rational, every \(\Delta_N\) would be rational. A prime-by-prime analysis of denominators, a separate argument for nonvanishing, and an integral bound for \(|\Delta_N|\) then give incompatible estimates for \(\log|\Delta_N|\).

## 7. Exercises

**Exercise 7.1 (easy).** Compute \(P_1,P_2,P_3\) and check Lemma 3.1.

**Exercise 7.2 (easy).** Compute \(I_1\) in the proof of Theorem 4.2 exactly, as \(a+b\zeta(2)\) with rational \(a,b\), and check that \(|I_1|\le\varphi^5\zeta(2)\).

**Exercise 7.3 (medium).** Prove \(\int_0^1\int_0^1\frac{dx\,dy}{1-xy}=\zeta(2)\) using Lemma 2.2 and Proposition 2.1.

**Exercise 7.4 (medium).** Show that \(e\) is irrational by Lemma 1.1, using the integers \(a_n=-n!\sum_{k\le n}1/k!\) and \(b_n=n!\).

**Exercise 7.5 (medium).** Show that the bound of Lemma 5.2 is attained, at \(x=y=\sqrt2-1\) and \(z=1/\sqrt2\).

**Exercise 7.6 (hard).** Check that, with the denominators \(d_n\) estimated only by Chebyshev's bound \(\psi(n)\le(2\log2+o(1))n\) instead of the prime number theorem, the argument of Theorem 4.2 fails. Which inequality would be needed?

## 8. Solutions

**7.1.** \(P_1=1-2x\), \(P_2=1-6x+6x^2\), \(P_3=1-12x+30x^2-20x^3\). For \(P_2\): \(\binom21\binom31=6\) and \(\binom22\binom42=6\).

**7.2.** \(I_1=\iint(1-y)(1-2x)/(1-xy)\). Expand \((1-y)(1-2x)=1-2x-y+2xy\) and use Proposition 2.3: the monomials \(1,x,y,xy\) give \(\zeta(2)\), \(1\), \(1\), \(\zeta(2)-1\). So \(I_1=\zeta(2)-2-1+2(\zeta(2)-1)=3\zeta(2)-5\approx-0.0652\), and \(\varphi^5\zeta(2)\approx0.148\).

**7.3.** Lemma 2.2 with \(F(t)=1/(1-t)\) gives \(\int_0^1(-\log t)/(1-t)\,dt\), which is \(1!\,\zeta(2)\) by Proposition 2.1.

**7.4.** \(a_n+b_ne=n!\sum_{k>n}1/k!\), which is positive and at most \(\sum_{j\ge1}(n+1)^{-j}=1/n\).

**7.5.** At \(x=y=\sqrt2-1\) we have \(u=\sqrt{xy}=\sqrt2-1\), and the inequality \(x(1-x)y(1-y)\le u^2(1-u)^2\) of the proof is an equality. The maximizing value of \(z\) found in the proof is \(z_*=1/(1+u)=1/\sqrt2\), where the \(z\)-factor equals \(1/(1+u)^2\). So the left side equals \(u^2(1-u)^2/(1+u)^2=k(u)^2=(\sqrt2-1)^4\).

**7.6.** With \(\psi(n)\le(2\log2+\varepsilon)n\), the bound becomes \(\bigl(e^{2\cdot2\log2}\varphi^5\bigr)^n=(16\varphi^5)^n\approx1.44^n\), which does not tend to zero. One needs \(\limsup\psi(n)/n<\frac52\log(1/\varphi)\approx1.203\), which the prime number theorem provides.

## References

- [Fischler] S. Fischler, Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, …), Séminaire Bourbaki, exposé 910, Astérisque 294 (2004), 27–62. https://arxiv.org/abs/math/0303066
- [Zudilin 2003] W. Zudilin, An Apéry-like difference equation for Catalan's constant, Electronic Journal of Combinatorics 10 (2003), R14. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v10i1r14
- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
