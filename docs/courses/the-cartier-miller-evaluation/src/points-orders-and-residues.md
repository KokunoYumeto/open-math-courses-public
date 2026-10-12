# Points, orders and residues

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A function on the curve \(v^2=f(w)\) has zeros and poles at points of the curve, and a differential has poles and residues. This lesson makes these notions precise for a polynomial \(f\) of degree three or four without repeated root, over an algebraically closed field of odd characteristic, by expanding functions in a parameter at each point. Three results are proved.

- A function without poles is constant (Theorem 4.2). So a function is determined, up to a constant factor, by the orders of its zeros and poles.
- The differential \(\omega=dw/v\) has neither zeros nor poles, and a differential without poles is a constant multiple of \(\omega\) (Proposition 5.2, Corollary 5.3).
- A logarithmic differential \(dF/F\) has at most simple poles, and its residue at a point is the order of \(F\) there (Proposition 5.4).

With the Cartier operator of [The Cartier operator](the-cartier-operator.md) these are the tools for comparing the differential \(dw/((1-\lambda w)v)\), which carries the coefficient sums, with logarithmic differentials.

The lesson treats one family of curves directly. It uses formal power series and Laurent series over a field (core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40)) and Sections 1, 2 and 4 of the lesson on the Cartier operator.

## 1. The points

Let \(k\) be an algebraically closed field of odd characteristic \(p\), and
\[
\begin{aligned}
f={}&f_0+f_1w+f_2w^2\\
&+f_3w^3+f_4w^4
\end{aligned}
\]
a polynomial in \(k[w]\) of degree three or four without repeated root. Let \(K\) be the field of functions \(A+Bv\), \(A,B\in k(w)\), \(v^2=f\), with its derivative \(D\), as in the lesson on the Cartier operator.

The *points* of the curve are the following.

- The *affine points*: the pairs \((a,b)\in k^2\) with \(b^2=f(a)\). Such a point is a *branch point* if \(b=0\), that is, if \(a\) is a root of \(f\), and an *ordinary* point otherwise. Over every \(a\in k\) there are two ordinary points, or one branch point.
- The *points at infinity*. In the coordinates \(u=1/w\), \(t=v/w^2\) the equation is \(t^2=f^*(u)\) with
\[
\begin{aligned}
f^*(u)={}&f_4+f_3u+f_2u^2\\
&+f_1u^3+f_0u^4 .
\end{aligned}
\]
The points at infinity are the points \((0,t)\) of this curve. If \(f\) has degree four, there are two of them, \(\infty_+\) and \(\infty_-\), with \(t=\pm c\), where \(c^2=f_4\); they are ordinary points of \(t^2=f^*(u)\). If \(f\) has degree three, \(f_4=0\) and \(f_3\ne0\); there is one point at infinity, \(\infty\), with \(t=0\), a branch point of \(t^2=f^*(u)\).

## 2. Expansions

Let \(k((z))\) be the field of Laurent series in a variable \(z\). The *order* of a nonzero series is its lowest exponent; a series of order \(0\) is a *unit* of \(k[[z]]\).

**Lemma 2.1.**

1. Let \(e\in k[[z]]\) have constant term \(b^2\) with \(b\ne0\). There is exactly one \(s\in k[[z]]\) with \(s^2=e\) and constant term \(b\).
2. Let \(g\in k[[x]]\) have constant term \(g_0\ne0\). There is exactly one \(\varphi\in k[[y]]\) with constant term \(0\) such that
\[
\varphi(y)\,g(\varphi(y))=y .
\]
It has the form \(\varphi=y/g_0+\cdots\).

**Proof.** (1) Write \(s=b+s_1z+\cdots\). The coefficient of \(z^n\) in \(s^2\) is \(2bs_n\) plus a polynomial in \(s_1,\dots,s_{n-1}\); since \(2b\ne0\), the \(s_n\) are determined one after another. (2) Write \(\varphi=\varphi_1y+\varphi_2y^2+\cdots\). The coefficient of \(y\) in \(\varphi\,g(\varphi)\) is \(g_0\varphi_1\), and for \(n\ge2\) the coefficient of \(y^n\) is \(g_0\varphi_n\) plus a polynomial in \(\varphi_1,\dots,\varphi_{n-1}\). So \(\varphi_1=1/g_0\), and the \(\varphi_n\) are determined one after another. \(\blacksquare\)

To every point \(P\) we attach two series \(w_P,v_P\in k((z))\) with \(v_P^2=f(w_P)\).

- *Ordinary affine point \(P=(a,b)\).* \(w_P=a+z\), and \(v_P\) is the square root of \(f(a+z)\) with constant term \(b\) (Lemma 2.1(1)).
- *Affine branch point \(P=(a,0)\).* Then \(f(a+x)=x\,g(x)\) with a polynomial \(g\), \(g(0)=f'(a)\ne0\). Let \(\varphi\) be the series of Lemma 2.1(2), so that \(f(a+\varphi(y))=y\). Put \(w_P=a+\varphi(z^2)\) and \(v_P=z\).
- *\(\infty_\pm\), for \(f\) of degree four.* \(w_P=1/z\) and \(v_P=z^{-2}s\), where \(s\) is the square root of \(f^*(z)\) with constant term \(\pm c\).
- *\(\infty\), for \(f\) of degree three.* Then \(f^*(u)=u\,g^*(u)\) with \(g^*(0)=f_3\ne0\). Let \(\varphi\) be the series with \(f^*(\varphi(y))=y\). Put \(w_P=1/\varphi(z^2)\) and \(v_P=z/\varphi(z^2)^2\).

In each case \(v_P^2=f(w_P)\); at infinity this follows from \(f(1/u)=f^*(u)/u^4\).

**Lemma 2.2.** For every point \(P\) there is exactly one homomorphism of fields
\[
\iota_P\colon K\to k((z))
\]
that is the identity on \(k\) and maps \(w\) to \(w_P\) and \(v\) to \(v_P\). It is injective.

**Proof.** For \(a'\in k\) the series \(w_P-a'\) is not zero. Every nonzero polynomial in \(w\) is a constant times a product of factors \(w-a'\), because \(k\) is algebraically closed; so substituting \(w_P\) for \(w\) maps nonzero polynomials to nonzero series, and extends to a homomorphism \(k(w)\to k((z))\). Since \(v_P\) is a root of \(X^2-f(w_P)\), it extends to \(K=k(w)[X]/(X^2-f)\). A homomorphism of fields is injective. It is unique because \(K\) is generated by \(k\), \(w\) and \(v\). \(\blacksquare\)

The series \(\iota_P(g)\) is the *expansion of \(g\) at \(P\)*. For \(g\ne0\) its order is the *order* \(\operatorname{ord}_P(g)\) of \(g\) at \(P\). So
\[
\begin{gathered}
\operatorname{ord}_P(gg')=\operatorname{ord}_P(g)+\operatorname{ord}_P(g'),\\
\operatorname{ord}_P(g+g')\ge\min(\operatorname{ord}_P(g),\operatorname{ord}_P(g')).
\end{gathered}
\]
The function \(g\) has a *zero* at \(P\) if \(\operatorname{ord}_P(g)>0\) and a *pole* if \(\operatorname{ord}_P(g)<0\). If \(\operatorname{ord}_P(g)\ge0\), \(g\) is *regular* at \(P\), and the constant term of its expansion is its *value* \(g(P)\). At an affine point \((a,b)\), \(w(P)=a\) and \(v(P)=b\). When \(f(0)=1\), the expansion at \(O=(0,1)\) is the one of Section 5 of the lesson on the Cartier operator, with \(z\) written for \(w\).

The definitions give the following *list of orders*.

- At an ordinary affine point over \(a\): \(\operatorname{ord}_P(w-a)=1\) and \(\operatorname{ord}_P(v)=0\).
- At an affine branch point over \(a\): \(\operatorname{ord}_P(w-a)=2\) and \(\operatorname{ord}_P(v)=1\).
- At \(\infty_\pm\), for degree four: \(\operatorname{ord}_P(w)=-1\) and \(\operatorname{ord}_P(v)=-2\).
- At \(\infty\), for degree three: \(\operatorname{ord}_P(w)=-2\) and \(\operatorname{ord}_P(v)=-3\).

For the branch points this uses \(\varphi(z^2)=z^2/g_0+\cdots\).

## 3. Functions of w

Let \(e_P=2\) if \(P\) is an affine branch point or the point \(\infty\) of a cubic, and \(e_P=1\) for the other points. For a nonzero \(r\in k(w)\) and \(a\in k\) let \(n_a(r)\) be the exponent of \(w-a\) in the factorization of \(r\), and \(\deg r\) the degree of the numerator minus that of the denominator.

**Lemma 3.1.** Let \(r\in k(w)\), \(r\ne0\).

1. If \(P\) is an affine point over \(a\), then \(\operatorname{ord}_P(r)=e_P\,n_a(r)\).
2. If \(P\) is a point at infinity, then \(\operatorname{ord}_P(r)=-e_P\deg r\).
3. If \(r\) is regular at all affine points, it is a polynomial. If \(r\) is regular at all points, it is constant.

**Proof.** Write \(r=c\prod_i(w-a_i)^{n_i}\) with distinct \(a_i\). At an affine point over \(a\), \(w_P-a'\) has the nonzero constant term \(a-a'\) for \(a'\ne a\), so \(\operatorname{ord}_P(w-a')=0\), and \(\operatorname{ord}_P(w-a)=e_P\) by the list of orders. At infinity, \(\operatorname{ord}_P(w-a')=\operatorname{ord}_P(w)=-e_P\) for every \(a'\). This gives (1) and (2). For (3): over every \(a\in k\) there is a point, because \(f(a)\) has a square root in \(k\). So regularity at all affine points gives \(n_a(r)\ge0\) for all \(a\), and \(r\) is a polynomial; regularity at infinity gives \(\deg r\le0\). \(\blacksquare\)

## 4. Functions without poles

Let \(\tau\) be the automorphism of \(K\) with \(\tau(A+Bv)=A-Bv\). For a point \(P\) let \(\bar P\) be the point \((a,-b)\) if \(P=(a,b)\) is affine, \(\infty_\mp\) if \(P=\infty_\pm\), and \(\infty\) if \(P=\infty\).

**Lemma 4.1.** \(\operatorname{ord}_{\bar P}(\tau g)=\operatorname{ord}_P(g)\) for every point \(P\) and every \(g\ne0\).

**Proof.** If \(P\) is an ordinary affine point or one of \(\infty_\pm\), then \(w_{\bar P}=w_P\) and \(v_{\bar P}=-v_P\). So \(\iota_{\bar P}\) and \(\iota_P\circ\tau\) agree on \(w\) and \(v\), hence are equal, and \(\iota_{\bar P}(\tau g)=\iota_P(g)\). If \(P\) is a branch point or the point \(\infty\) of a cubic, then \(\bar P=P\); the series \(w_P\) contains only even powers of \(z\) and \(v_P\) only odd powers. Let \(\epsilon\) be the automorphism \(z\mapsto-z\) of \(k((z))\). Then \(\iota_P\circ\tau\) and \(\epsilon\circ\iota_P\) agree on \(w\) and \(v\), hence are equal, and \(\epsilon\) preserves orders. \(\blacksquare\)

**Theorem 4.2.** A function \(g\in K\) that is regular at all points is constant: \(g\in k\).

**Proof.** Let \(g=A+Bv\). By Lemma 4.1, \(\tau g=A-Bv\) is regular at all points. So \(g+\tau g=2A\) and \(g\cdot\tau g=A^2-B^2f\) are elements of \(k(w)\) that are regular at all points, and they are constants by Lemma 3.1(3). Hence \(A\in k\) and \(B^2f=c\) with \(c\in k\). If \(B\ne0\), then \(c\ne0\) and \(f=cB^{-2}\); at a root \(a\) of \(f\) this gives \(1=n_a(f)=-2n_a(B)\), which is impossible. So \(B=0\) and \(g=A\in k\). \(\blacksquare\)

**Corollary 4.3.** If two nonzero functions have the same order at every point, their quotient is a constant.

**Proof.** The quotient and its inverse have order \(0\) at every point. \(\blacksquare\)

## 5. Differentials

For a Laurent series \(\ell=\sum_nb_nz^n\) let \(\ell'=\sum_nnb_nz^{n-1}\). The *expansion at \(P\)* of a differential \(\eta=g\,dw\) is
\[
\iota_P(\eta)=\iota_P(g)\,w_P'\;dz .
\]
The series \(w_P'\) is not zero: it is \(1\) at an ordinary affine point, \(2z\varphi'(z^2)\) at an affine branch point, \(-z^{-2}\) at \(\infty_\pm\), and \(-2z\varphi'(z^2)/\varphi(z^2)^2\) at the point \(\infty\) of a cubic; here \(\varphi'\) has a nonzero constant term and \(2\ne0\) in \(k\). The order of the series \(\iota_P(g)w_P'\) is the *order* \(\operatorname{ord}_P(\eta)\), and its coefficient of \(z^{-1}\) is the *residue* \(\operatorname{res}_P(\eta)\). The differential has a *pole* at \(P\) if \(\operatorname{ord}_P(\eta)<0\), a *simple* pole if the order is \(-1\). For a function \(g\),
\[
\operatorname{ord}_P(g\eta)=\operatorname{ord}_P(g)+\operatorname{ord}_P(\eta).
\]

**Lemma 5.1.** For every function \(g\) and every point \(P\),
\[
\iota_P(dg)=\iota_P(g)'\,dz .
\]

**Proof.** We have to show \(\iota_P(D(g))\,w_P'=\iota_P(g)'\). Let \(\delta_1(g)=\iota_P(D(g))\) and \(\delta_2(g)=\iota_P(g)'/w_P'\). Both maps \(\delta\colon K\to k((z))\) are additive, vanish on \(k\), have \(\delta(w)=1\), and satisfy
\[
\delta(gg')=\delta(g)\iota_P(g')+\iota_P(g)\delta(g').
\]
Two such maps agree on polynomials in \(w\), by the product rule and induction on the degree, then on \(k(w)\), since \(\delta(A)=\delta(B\cdot A/B)\) determines \(\delta(A/B)\). They agree on \(v\), because \(2\iota_P(v)\delta(v)=\delta(f)\) and \(2\iota_P(v)\ne0\). So they agree on all \(A+Bv\). \(\blacksquare\)

**Proposition 5.2.** The differential \(\omega=dw/v\) has order \(0\) at every point.

**Proof.** \(\iota_P(\omega)=(w_P'/v_P)\,dz\), and \(w_P'/v_P\) is

- \(1/v_P\) at an ordinary affine point, where \(v_P\) is a unit;
- \(2z\varphi'(z^2)/z=2\varphi'(z^2)\) at an affine branch point;
- \(-z^{-2}/(z^{-2}s)=-1/s\) at \(\infty_\pm\), where \(s\) is a unit;
- \(-2\varphi'(z^2)\) at the point \(\infty\) of a cubic.

Each of these is a unit of \(k[[z]]\). \(\blacksquare\)

**Corollary 5.3.** A differential that has no pole is \(c\,\omega\) with \(c\in k\).

**Proof.** Let \(\eta=g\,dw=(gv)\,\omega\). By Proposition 5.2, \(\operatorname{ord}_P(gv)=\operatorname{ord}_P(\eta)\ge0\) for all \(P\). By Theorem 4.2, \(gv\in k\). \(\blacksquare\)

So the differentials without poles form a vector space of dimension one over \(k\). This is the statement that the curve has genus one.

**Proposition 5.4.** Let \(F\in K\), \(F\ne0\), and let \(P\) be a point with \(n=\operatorname{ord}_P(F)\). Then \(\operatorname{ord}_P(dF/F)\ge-1\), and
\[
\operatorname{res}_P(dF/F)=n\quad\text{in }k .
\]
In particular \(dF/F\) has no pole at \(P\) if \(p\) divides \(n\).

**Proof.** By Lemma 5.1, \(\iota_P(dF/F)=(\ell'/\ell)\,dz\) with \(\ell=\iota_P(F)=z^ne\), \(e\) a unit. Then \(\ell'/\ell=n/z+e'/e\), and \(e'/e\in k[[z]]\). \(\blacksquare\)

The residue of \(dF/F\) is the integer \(n\) reduced modulo \(p\). A zero or pole of \(F\) whose order is divisible by \(p\) is not seen by \(dF/F\).

## 6. Exercises

**6.1.** Let \(P=(a,b)\) be an ordinary affine point. Determine the order of the function \(w-a\) at every point of the curve, for \(f\) of degree three and of degree four, and check that the sum of the orders over all points is \(0\).

**6.2.** Determine the order of \(v\) at every point, and check that the sum of the orders is \(0\).

**6.3.** Determine \(\operatorname{ord}_P(dw)\) at every point, and check that the sum is \(0\).

**6.4.** Show that a function that is regular at all affine points is \(A+Bv\) with polynomials \(A,B\in k[w]\).

**6.5.** Let \(f(0)=1\), \(O=(0,1)\) and \(\bar O=(0,-1)\). Show that \(dw/(wv)\) has simple poles at \(O\) and \(\bar O\) with residues \(1\) and \(-1\), and no other pole.

## 7. Solutions

**6.1.** By Lemma 3.1 the order is \(1\) at \(P\) and at \(\bar P=(a,-b)\), and \(0\) at the other affine points. At infinity it is \(-1\) at each of \(\infty_+,\infty_-\) for degree four, and \(-2\) at \(\infty\) for degree three. The sum is \(1+1-2=0\) in both cases.

**6.2.** At an affine point \((a,b)\) the value of \(v\) is \(b\); so the order is \(0\) at ordinary points and \(1\) at the branch points (the list of orders in Section 2). There are four branch points and order \(-2\) at each of \(\infty_\pm\) for degree four: \(4-4=0\). There are three branch points and order \(-3\) at \(\infty\) for degree three: \(3-3=0\).

**6.3.** The order of \(dw\) is the order of \(w_P'\): \(0\) at ordinary affine points, \(1\) at affine branch points, \(-2\) at \(\infty_\pm\), and \(1-4=-3\) at the point \(\infty\) of a cubic. The sums are \(4-2-2=0\) and \(3-3=0\). This agrees with Exercise 6.2 and Proposition 5.2, since \(dw=v\,\omega\).

**6.4.** Let \(g=A+Bv\) be regular at all affine points. By Lemma 4.1 so is \(\tau g\), hence so are \(2A\) and \(A^2-B^2f\). By Lemma 3.1(3), \(A\) and \(B^2f\) are polynomials. If \(B\) had a pole at some \(a\), then \(n_a(B)\le-1\) and \(n_a(f)\le1\), because \(f\) has no repeated root; so \(n_a(B^2f)\le-1\), and \(B^2f\) would not be a polynomial. So \(B\) is a polynomial.

**6.5.** \(dw/(wv)=w^{-1}\omega\). By Proposition 5.2 its order at \(P\) is \(-\operatorname{ord}_P(w)\): \(-1\) at the two points \(O,\bar O\) over \(w=0\), which are ordinary because \(f(0)\ne0\); \(0\) at the other affine points; and positive at infinity. At \(O\) the expansion is \(dz/(z\,v_O)\) with \(v_O=1+\cdots\), so the residue is \(1\); at \(\bar O\), \(v_{\bar O}=-1+\cdots\) and the residue is \(-1\).

## References

- [Jordan] D. Jordan, *Cartier–Miller evaluation of genus-one coefficient sums*, manuscript, revised 5 October 2026, the section "Cartier evaluation and the regular identity". https://github.com/bbrhuft/Cartier-Miller-evaluation-of-genus-one-coefficient-sums
