# A counterexample in dimension three

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that the Jacobian conjecture is false. An explicit polynomial map of three-dimensional space, with rational coefficients, has Jacobian determinant identically \(-2\) and takes the same value at three different points. So it is a Keller map without an inverse. Everything here is a finite computation, and we do it by hand. The key is a system of coordinates adapted to the map, in which its components become three short rational expressions. The same coordinates describe every fibre of the map through the roots of a cubic equation, and show that a general point has exactly three preimages.

We use [Keller maps and the Jacobian conjecture](keller-maps-and-the-jacobian-conjecture.md), and Gauss's lemma on primitive polynomials from [Integral extensions: lying over, going up and going down, Proposition 2.3 and its proof](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#2-integral-closure-survives-localization).

Basic references are [Alpöge], [AFP] and [Tao].

## 1. The map

Let \(k\) be a field of characteristic zero, and write points of \(k^3\) as \(z=(z_1,z_2,z_3)\). Define \(F=(F_1,F_2,F_3):k^3\to k^3\) by

\[
\begin{aligned}
F_1&=(1+z_1z_2)^3z_3+z_2^2(1+z_1z_2)(4+3z_1z_2),\\
F_2&=z_2+3z_1(1+z_1z_2)^2z_3+3z_1z_2^2(4+3z_1z_2),\\
F_3&=2z_1-3z_1^2z_2-z_1^3z_3 .
\end{aligned}
\tag{1.1}
\]

The components have degrees \(7\), \(6\) and \(4\). Two auxiliary polynomials organize them:

\[
t=1+z_1z_2,\qquad Q=t^2z_3+z_2^2(1+3t).
\tag{1.2}
\]

Since \(4+3z_1z_2=1+3t\), the definitions give

\[
F_1=t\,Q,\qquad F_2=z_2+3z_1Q,\qquad F_3=z_1\bigl(2-3z_1z_2-z_1^2z_3\bigr).
\tag{1.3}
\]

Levent Alpöge announced this map on 19 and 20 July 2026. He credited the AI model Claude Fable 5 with the work that led to it, and Akhil Mathew with suggesting the question [Alpöge]. Its two decisive properties were formally verified in the proof assistant Isabelle/HOL within days [AFP], and Terence Tao explained the geometry behind it [Tao].

## 2. Coordinates adapted to the map

Put

\[
u=z_1,\qquad t=1+z_1z_2,\qquad P=z_1^2\,Q .
\tag{2.1}
\]

**Lemma 2.1.** The following identities hold in \(k[z_1,z_2,z_3]\):

\[
z_1^2F_1=tP,\qquad z_1F_2=t-1+3P,\qquad t^2F_3=z_1\,(t+1-P).
\tag{2.2}
\]

**Proof.** The first is \(z_1^2\,tQ=tP\). For the second, \(z_1F_2=z_1z_2+3z_1^2Q=(t-1)+3P\). For the third, write \(s=z_1^2z_3\). Since \(z_1^2z_2^2=(t-1)^2\),

\[
P=t^2s+(t-1)^2(1+3t),\qquad F_3=z_1\bigl(2-3(t-1)-s\bigr)=z_1(5-3t-s).
\]

Hence \(t^2F_3=z_1\bigl(t^2(5-3t)-t^2s\bigr)=z_1\bigl(t^2(5-3t)+(t-1)^2(1+3t)-P\bigr)\). Expanding, \((t-1)^2(1+3t)=3t^3-5t^2+t+1\), so \(t^2(5-3t)+(t-1)^2(1+3t)=t+1\). \(\square\)

On the open set \(U=\{z\in k^3: z_1t\ne0\}\), the identities (2.2) express the map in the coordinates \(u,t,P\):

\[
F_1=\frac{tP}{u^2},\qquad F_2=\frac{t-1+3P}{u},\qquad F_3=\frac{u\,(t+1-P)}{t^2}.
\tag{2.3}
\]

## 3. The Jacobian determinant

We work in the field \(k(z_1,z_2,z_3)\) of rational functions. Partial derivatives extend to it by the quotient rule and still obey the chain rule.

**Theorem 3.1.** \(\det JF=-2\).

**Proof.** Let \(\Phi=(u,t,P)\) be the polynomial map (2.1), and let \(\Psi\) be the rational map

\[
\Psi(u,t,P)=\Bigl(\frac{tP}{u^2},\ \frac{t-1+3P}{u},\ \frac{u\,(t+1-P)}{t^2}\Bigr).
\]

By (2.3), \(F=\Psi\circ\Phi\) as tuples of rational functions, so the chain rule gives

\[
\det JF=(\det J\Psi\circ\Phi)\cdot\det J\Phi .
\tag{3.1}
\]

*The factor \(\det J\Phi\).* The partial derivatives of \(u\) are \((1,0,0)\), those of \(t\) are \((z_2,z_1,0)\), and \(\partial P/\partial z_3=z_1^2\,\partial Q/\partial z_3=z_1^2t^2\). The matrix \(J\Phi\) is lower triangular, so

\[
\det J\Phi=1\cdot z_1\cdot z_1^2t^2=u^3t^2 .
\]

*The factor \(\det J\Psi\).* With respect to \((u,t,P)\), the rows of \(J\Psi\) are

\[
\begin{aligned}
&\bigl(-2tP\,u^{-3},\ \ P\,u^{-2},\ \ t\,u^{-2}\bigr),\\
&\bigl(-(t-1+3P)\,u^{-2},\ \ u^{-1},\ \ 3u^{-1}\bigr),\\
&\bigl((t+1-P)\,t^{-2},\ \ u\,(2P-t-2)\,t^{-3},\ \ -u\,t^{-2}\bigr).
\end{aligned}
\]

For the middle entry of the last row, \(\partial_t\bigl(u(t+1-P)t^{-2}\bigr)=u\bigl(t-2(t+1-P)\bigr)t^{-3}\). Multiply the three rows by \(u^3\), \(u^2\) and \(t^3\), and then divide the second and third columns by \(u\). This multiplies the determinant by \(u^5t^3\cdot u^{-2}=u^3t^3\), and leaves

\[
M=\begin{pmatrix}-2tP&P&t\\-(t-1+3P)&1&3\\t(t+1-P)&2P-t-2&-t\end{pmatrix}.
\]

Expand along the first row. The three \(2\times2\) minors are

\[
\begin{aligned}
&1\cdot(-t)-3(2P-t-2)=2t-6P+6,\\
&(t-1+3P)\,t-3t(t+1-P)=t\,(6P-2t-4),\\
&-(t-1+3P)(2P-t-2)-t(t+1-P)=-6P^2+2tP+8P-2 .
\end{aligned}
\]

So

\[
\det M=-2tP(2t-6P+6)-P\cdot t(6P-2t-4)+t(-6P^2+2tP+8P-2).
\]

Collecting terms, the coefficients of \(t^2P\) are \(-4+2+2=0\), those of \(tP^2\) are \(12-6-6=0\), and those of \(tP\) are \(-12+4+8=0\). Only \(-2t\) survives: \(\det M=-2t\). Hence

\[
\det J\Psi=\frac{-2t}{u^3t^3}=\frac{-2}{u^3t^2}.
\]

By (3.1), \(\det JF=\dfrac{-2}{u^3t^2}\cdot u^3t^2=-2\). This is an identity of rational functions, and \(\det JF\) is a polynomial, so \(\det JF=-2\) as a polynomial. \(\square\)

## 4. Three points with one image

**Theorem 4.1.** The three points \((0,0,-\tfrac14)\), \((1,-\tfrac32,\tfrac{13}{2})\) and \((-1,\tfrac32,\tfrac{13}{2})\) all have image \((-\tfrac14,0,0)\).

**Proof.** Use (1.2) and (1.3). At \((0,0,-\tfrac14)\): \(t=1\) and \(Q=-\tfrac14\), so \(F=(-\tfrac14,0,0)\). At \((1,-\tfrac32,\tfrac{13}2)\): \(t=-\tfrac12\) and \(Q=\tfrac14\cdot\tfrac{13}2+\tfrac94\bigl(1-\tfrac32\bigr)=\tfrac12\). So \(F_1=tQ=-\tfrac14\), \(F_2=-\tfrac32+3\cdot\tfrac12=0\) and \(F_3=1\cdot\bigl(2+\tfrac92-\tfrac{13}2\bigr)=0\). At \((-1,\tfrac32,\tfrac{13}2)\): again \(t=-\tfrac12\) and \(Q=\tfrac12\). So \(F_1=-\tfrac14\), \(F_2=\tfrac32-\tfrac32=0\) and \(F_3=-\bigl(2+\tfrac92-\tfrac{13}2\bigr)=0\). \(\square\)

**Corollary 4.2.** The Jacobian conjecture is false in every dimension \(n\geq3\), over every field of characteristic zero.

**Proof.** By Theorem 3.1, \(F\) is a Keller map, and by Theorem 4.1 it is not injective. So no map at all, polynomial or not, is inverse to it. For \(n>3\), let \(G=F\times\mathrm{id}\) on \(k^3\times k^{n-3}\). Its Jacobian matrix is block diagonal, so \(\det JG=-2\), and \(G\) takes the same value at the three points of Theorem 4.1 extended by zeros. \(\square\)

In characteristic \(2\) the determinant \(-2\) vanishes, and in every positive characteristic the conjecture already fails by Example 1.3 of the previous lesson. The construction says nothing about dimension two.

## 5. Fibres and the degree

From now on \(k\) is algebraically closed of characteristic zero. The coordinates of Section 2 turn the equation \(F(z)=(a,b,c)\) into a cubic equation for one unknown,

\[
\lambda=\frac{z_1}{1+z_1z_2}=\frac ut .
\]

**Theorem 5.1.** Let \((a,b,c)\in k^3\). The points \(z\in U\) with \(F(z)=(a,b,c)\) correspond bijectively, by \(z\mapsto u/t\), to the roots \(\lambda\) of

\[
C(\lambda)=2a\lambda^3-b\lambda^2+2\lambda-c
\tag{5.1}
\]

with \(\lambda\ne0\) and \(1-b\lambda+3a\lambda^2\ne0\). The point belonging to such a root is given by

\[
t=\frac1{1-b\lambda+3a\lambda^2},\quad z_1=\lambda t,\quad z_2=\frac{t-1}{z_1},\quad
z_3=\frac{P-(t-1)^2(1+3t)}{z_1^2t^2},\quad\text{where } P=a\lambda^2t .
\tag{5.2}
\]

**Proof.** Let \(z\in U\) satisfy \(F(z)=(a,b,c)\), and put \(\lambda=u/t\ne0\). By (2.2), \(tP=au^2\), so \(P=a\lambda^2t\). Next, \(t-1+3P=bu=b\lambda t\), that is,

\[
t\,(1-b\lambda+3a\lambda^2)=1 ,
\tag{5.3}
\]

so \(1-b\lambda+3a\lambda^2\ne0\) and \(t\) is as in (5.2). Finally \(t^2c=u(t+1-P)\). Dividing by \(t\) gives \(tc=\lambda(t+1-a\lambda^2t)\), that is,

\[
t\,(c-\lambda+a\lambda^3)=\lambda .
\tag{5.4}
\]

Multiplying (5.4) by \(1-b\lambda+3a\lambda^2\) and using (5.3) gives \(c-\lambda+a\lambda^3=\lambda(1-b\lambda+3a\lambda^2)\), which is \(C(\lambda)=0\). The point \(z\) is recovered from \(\lambda\): \(z_1=u=\lambda t\), \(z_2=(t-1)/z_1\), and from \(P=z_1^2\bigl(t^2z_3+z_2^2(1+3t)\bigr)=z_1^2t^2z_3+(t-1)^2(1+3t)\) we get the formula for \(z_3\). So distinct points give distinct \(\lambda\).

Conversely, let \(\lambda\) be a root of \(C\) with \(\lambda\ne0\) and \(1-b\lambda+3a\lambda^2\ne0\), and define \(t,z_1,z_2,z_3,P\) by (5.2). Then \(z_1=\lambda t\ne0\), \(1+z_1z_2=t\ne0\), and \(z_1^2Q=P\) by the formula for \(z_3\). So \(z\in U\), and (2.2) holds with these values of \(u,t,P\). From \(tP=a\lambda^2t^2=az_1^2\) we get \(F_1(z)=a\). From (5.3), \(t-1+3P=t-1+3a\lambda^2t=b\lambda t=bz_1\), so \(F_2(z)=b\). Reversing the last computation, \(C(\lambda)=0\) gives (5.4), which says \(t^2c=z_1(t+1-P)\), so \(F_3(z)=c\). Finally \(z_1/t=\lambda\). \(\square\)

**Proposition 5.2 (outside \(U\)).** If \(z_1=0\), then \(F(z)=(z_3+4z_2^2,\ z_2,\ 0)\). If \(1+z_1z_2=0\), then \(F_1(z)=0\).

**Proof.** If \(z_1=0\), then \(t=1\) and \(Q=z_3+4z_2^2\), and (1.3) gives the formula. If \(t=0\), then \(F_1=tQ=0\). \(\square\)

**Corollary 5.3.** The fibre of \(F\) over \((-\tfrac14,0,0)\) consists of exactly the three points of Theorem 4.1.

**Proof.** Here \(a=-\tfrac14\ne0\), so by Proposition 5.2 no point of the fibre has \(1+z_1z_2=0\). Since \(c=0\), the points with \(z_1=0\) are those with \(z_2=b=0\) and \(z_3=a-4b^2=-\tfrac14\): only \((0,0,-\tfrac14)\). In \(U\), Theorem 5.1 applies with \(C(\lambda)=-\tfrac12\lambda^3+2\lambda=-\tfrac12\lambda(\lambda^2-4)\). The nonzero roots are \(\lambda=\pm2\), and for both \(1-b\lambda+3a\lambda^2=1-3=-2\ne0\). Formula (5.2) gives \(t=-\tfrac12\), \(P=\tfrac12\), and \(z=(-1,\tfrac32,\tfrac{13}2)\) for \(\lambda=2\), \(z=(1,-\tfrac32,\tfrac{13}2)\) for \(\lambda=-2\). \(\square\)

**Theorem 5.4.** The Keller map \(F\) has degree \(3\): the field \(k(z_1,z_2,z_3)\) has degree \(3\) over \(k(F_1,F_2,F_3)\). A general point of \(k^3\) has exactly three preimages.

**Proof.** Write \(K=k(z_1,z_2,z_3)\) and \(L=k(F_1,F_2,F_3)\), and let \(\lambda=z_1/(1+z_1z_2)\in K\). The first half of the proof of Theorem 5.1 used only the identities (2.2) and division by the nonzero elements \(u\) and \(t\). Carried out in \(K\), with \(a,b,c\) replaced by \(F_1,F_2,F_3\), it shows

\[
2F_1\lambda^3-F_2\lambda^2+2\lambda-F_3=0 ,
\]

and expresses \(t\), then \(z_1\), \(z_2\) and \(z_3\), rationally in \(\lambda\) and \(F_1,F_2,F_3\), by (5.2). Hence \(K=L(\lambda)\), and \(\lambda\) is a root of

\[
m(X)=2F_1X^3-F_2X^2+2X-F_3\in L[X].
\]

It remains to show that \(m\) is irreducible over \(L\). By Proposition 2.1 of the previous lesson, \(F_1,F_2,F_3\) are algebraically independent, so \(R=k[F_1,F_2,F_3]\) is a polynomial ring with fraction field \(L\). As an element of \(R[X]=k[F_1,F_2,F_3,X]\), the polynomial \(m\) has degree one in \(F_3\), with coefficient \(-1\). In a factorization \(m=gh\), the degrees in \(F_3\) add up to one, so one factor, say \(h\), does not involve \(F_3\). Comparing the coefficients of \(F_3\) gives \(-1=g_1h\), where \(g_1\) is the coefficient of \(F_3\) in \(g\). So \(h\) is a unit. Thus \(m\) is irreducible in \(R[X]\). Its coefficients \(2F_1,-F_2,2,-F_3\) have no common factor, because \(2\) is a unit. So \(m\) is primitive, and Gauss's lemma [Integral extensions: lying over, going up and going down, proof of Proposition 2.3](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#2-integral-closure-survives-localization) shows that \(m\) is irreducible in \(L[X]\). Hence \([K:L]=3\). The last assertion is Theorem 3.3 of the previous lesson. \(\square\)

So the counterexample is generically three-to-one, and its non-injectivity is not an accident of a special fibre. The size of the fibre still varies from point to point, as Exercises 7.2 and 7.4 show.

## 6. What happened next

The day after the announcement, Gallagher gave an infinite family of counterexamples, one of each degree \(d\geq3\), and three days later Speyer explained the geometric mechanism behind them, as recounted in [Gao]. Gao generalized that mechanism to counterexamples of arbitrarily large degree in every dimension above two [Gao]. Van den Essen gave an elementary way to find such maps [van den Essen]. All of these live in dimension three or more; the case of dimension two is not settled by them.

## 7. Exercises

**Exercise 7.1 (easy).** Write down two distinct points of \(k^4\) with the same image under \(F\times\mathrm{id}_k\), and check that its Jacobian determinant is \(-2\).

**Exercise 7.2 (medium).** Show that the fibre of \(F\) over the origin consists of the origin alone.

**Exercise 7.3 (medium).** Let \(a\ne0\) and \(c\ne0\). Suppose the cubic (5.1) has three distinct roots, none of which is a root of \(1-bX+3aX^2\). Show that \((a,b,c)\) has exactly three preimages.

**Exercise 7.4 (hard).** Show that the point \((\tfrac13,2,\tfrac23)\) has no preimage. So \(F\) is not surjective.

## 8. Solutions

**7.1.** The points \((0,0,-\tfrac14,0)\) and \((1,-\tfrac32,\tfrac{13}2,0)\) both map to \((-\tfrac14,0,0,0)\). The Jacobian matrix of \(F\times\mathrm{id}_k\) is block diagonal with blocks \(JF\) and \((1)\), so its determinant is \(-2\).

**7.2.** Let \(F(z)=(0,0,0)\). If \(z_1=0\), Proposition 5.2 gives \(z_2=0\) and \(z_3+4z_2^2=0\), so \(z=0\). If \(t=1+z_1z_2=0\), then \(Q=z_2^2(1+3t)=z_2^2\), and \(F_2=z_2+3z_1z_2^2=z_2(1+3z_1z_2)=-2z_2\). So \(z_2=0\), and then \(t=1\), a contradiction. If \(z\in U\), Theorem 5.1 applies with \(C(\lambda)=2\lambda\), whose only root \(\lambda=0\) is excluded. So the fibre is \(\{0\}\).

**7.3.** Since \(c\ne0\), Proposition 5.2 excludes points with \(z_1=0\). Since \(a\ne0\), it excludes points with \(t=0\). The roots of (5.1) are nonzero because \(C(0)=-c\ne0\). By hypothesis there are three of them, and each satisfies \(1-b\lambda+3a\lambda^2\ne0\). By Theorem 5.1 they give exactly three preimages, all in \(U\).

**7.4.** Here \(a=\tfrac13\), \(b=2\), \(c=\tfrac23\). Since \(a\ne0\) and \(c\ne0\), Proposition 5.2 excludes points outside \(U\). In \(U\), the cubic is

\[
C(\lambda)=\tfrac23\lambda^3-2\lambda^2+2\lambda-\tfrac23=\tfrac23(\lambda-1)^3,
\]

with the single root \(\lambda=1\). But \(1-b\lambda+3a\lambda^2=1-2+1=0\) at \(\lambda=1\). So Theorem 5.1 allows no point of \(U\) either. The same computation works for \(\bigl(\tfrac1{3r^2},\tfrac2r,\tfrac{2r}3\bigr)\) with any \(r\ne0\), where \(C(\lambda)=\tfrac2{3r^2}(\lambda-r)^3\) and \(1-b\lambda+3a\lambda^2=\tfrac1{r^2}(\lambda-r)^2\).

## References

- [AFP] A. Freitas Ramos, D. Barros Hulak, R. J. G. B. de Queiroz, Formal verification of an explicit counterexample to the Jacobian conjecture, Archive of Formal Proofs (Isabelle/HOL), July 2026. https://isa-afp.org/entries/Jacobian_Counterexample.html
- [Gao] S. Gao, Counterexamples to the Jacobian conjecture in dimensions greater than two, arXiv:2608.00222 (2026). https://arxiv.org/abs/2608.00222
- [Tao] T. Tao, A digestion of the Jacobian conjecture counterexample, What's new, 21 July 2026. https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
- [van den Essen] A. van den Essen, An elementary way to find a counterexample to the Jacobian Conjecture, arXiv:2609.17795 (2026). https://arxiv.org/abs/2609.17795
- [Alpöge] L. Alpöge, announcement of the counterexample, posts on X of 19 and 20 July 2026. https://x.com/__alpoge__
