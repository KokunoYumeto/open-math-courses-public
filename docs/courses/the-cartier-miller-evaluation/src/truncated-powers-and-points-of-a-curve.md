# Truncated powers and points of a curve

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(p\) be an odd prime and \(f\) a polynomial of degree three or four with coefficients in the field \(\mathbb F_p\) with \(p\) elements. The power \(f^{(p-1)/2}\) is a polynomial of degree up to \(2p-2\). This lesson is about the part of it of degree less than \(p\), evaluated at a point of \(\mathbb F_p\):
\[
\begin{gathered}
f(w)^{(p-1)/2}=\sum_m c_mw^m,\\
T_f(\mu)=\sum_{m=0}^{p-1}c_m\mu^m .
\end{gathered}
\]
Such truncated sums occur in congruences for sums of binomial coefficients (Exercise 6.5). Computing \(T_f(\mu)\) term by term takes about \(p\) operations. The lesson proves three elementary facts that connect the sum with the curve \(v^2=f(w)\).

- The last coefficient \(H=c_{p-1}\) is the residue modulo \(p\) of \(\tau=p+1-N\), where \(N\) is the number of points of the curve over \(\mathbb F_p\) (Theorem 3.1). This is classical.
- \(T_f(\mu)\) is, up to two explicit terms, a sum over the points of the curve (Theorem 4.1), and a sum of quadratic characters with rational weights (Corollary 4.2). These identities are from D. Jordan's manuscript [Jordan], where they serve as an independent check of its main theorem.

The main theorem of [Jordan] evaluates the same quantity with a number of operations proportional to \(\log p\), once \(\tau\) is known, through the arithmetic of the curve. Section 5 says what it states. Its proof needs differentials on the curve and is not part of this lesson.

The lesson uses the field \(\mathbb F_p\), polynomials over it, and the fact that a polynomial of degree \(n\) over a field has at most \(n\) roots (core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40)).

## 1. The sums

Throughout, \(p\) is an odd prime, \(h=(p-1)/2\), and
\[
f=f_0+f_1w+f_2w^2+f_3w^3+f_4w^4
\]
is a polynomial with coefficients in \(\mathbb F_p\). Write
\[
f(w)^h=\sum_{m=0}^{2p-2}c_mw^m .
\]
The degree of \(f^h\) is at most \(4h=2p-2\). Let
\[
\begin{gathered}
T_f(w)=\sum_{m=0}^{p-1}c_mw^m,\qquad H=c_{p-1},\\
G_f(w)=\sum_{m=p}^{2p-2}c_mw^m ,
\end{gathered}
\]
so that \(f^h=T_f+G_f\). For \(\lambda\in\mathbb F_p\) let \(S_f(\lambda)\) be the coefficient of \(w^{p-1}\) in the power series \(f(w)^h/(1-\lambda w)\).

**Lemma 1.1.**

1. \(S_f(\lambda)=\sum_{m=0}^{p-1}c_m\lambda^{p-1-m}\). In particular \(S_f(0)=H\).
2. If \(\lambda\ne0\), then \(S_f(\lambda)=T_f(1/\lambda)\).

**Proof.** (1) \(1/(1-\lambda w)=\sum_{j\ge0}\lambda^jw^j\), and the coefficient of \(w^{p-1}\) in the product with \(\sum_mc_mw^m\) is \(\sum_{m\le p-1}c_m\lambda^{p-1-m}\). For \(\lambda=0\) only \(m=p-1\) remains. (2) For \(\lambda\ne0\) in \(\mathbb F_p\) we have \(\lambda^{p-1}=1\), so \(\lambda^{p-1-m}=\lambda^{-m}\). \(\blacksquare\)

So the two notations describe the same numbers; \(S_f\) is the one used in [Jordan].

For \(a\in\mathbb F_p\) let \(\varepsilon(a)=a^h\). The next lemma is Euler's criterion.

**Lemma 1.2.** \(\varepsilon(a)=1\) if \(a\) is a nonzero square in \(\mathbb F_p\), \(\varepsilon(a)=-1\) if \(a\) is not a square, and \(\varepsilon(0)=0\). The number of \(v\in\mathbb F_p\) with \(v^2=a\) is \(1+\varepsilon(a)\), as an integer and hence in \(\mathbb F_p\).

**Proof.** Let \(a\ne0\). Then \((a^h)^2=a^{p-1}=1\), so \(a^h=\pm1\). If \(a=b^2\), then \(a^h=b^{p-1}=1\). The map \(b\mapsto b^2\) on the \(p-1\) nonzero elements takes each value twice, at \(b\) and \(-b\ne b\); so there are exactly \(h\) nonzero squares. The polynomial \(x^h-1\) has at most \(h\) roots, and the nonzero squares are \(h\) roots. So a non-square has \(a^h\ne1\), that is, \(a^h=-1\). The number of square roots is \(2\), \(0\) or \(1\) in the three cases. \(\blacksquare\)

**Corollary 1.3.** For every \(\mu\in\mathbb F_p\),
\[
T_f(\mu)=\varepsilon(f(\mu))-G_f(\mu).
\]

**Proof.** \(T_f(\mu)+G_f(\mu)=f(\mu)^h\). \(\blacksquare\)

**Example 1.4.** Let \(p=7\) and \(f=1+w^2+w^3\). Then \(h=3\) and, in \(\mathbb F_7[w]\),
\[
\begin{aligned}
f^3={}&1+3w^2+3w^3+3w^4+6w^5\\
&+4w^6+3w^7+3w^8+w^9 .
\end{aligned}
\]
So \(H=4\), and \(S_f(1)=T_f(1)\) is \(1+3+3+3+6+4=6\) in \(\mathbb F_7\). Here \(f(1)=3\) is not a square modulo \(7\), and indeed \(G_f(1)=3+3+1=0=-1-6\).

## 2. Power sums

**Lemma 2.1.** Let \(k\ge0\) be an integer, and read \(0^0\) as \(1\). If \(k>0\) and \(p-1\) divides \(k\), then
\[
\sum_{w\in\mathbb F_p}w^k=-1 .
\]
In all other cases the sum is \(0\).

**Proof.** For \(k=0\) the sum is \(p=0\). Let \(k>0\). If \(p-1\) divides \(k\), then \(w^k=1\) for the \(p-1\) nonzero \(w\) and \(0^k=0\); the sum is \(p-1=-1\). Otherwise write \(k=q(p-1)+r\) with \(0<r<p-1\). For \(w\ne0\), \(w^k=w^r\). The polynomial \(x^r-1\) has at most \(r<p-1\) roots, so there is \(a\ne0\) with \(a^r\ne1\). Since \(w\mapsto aw\) is a bijection of \(\mathbb F_p\),
\[
\sum_ww^k=\sum_w(aw)^k=a^r\sum_ww^k ,
\]
and so the sum is \(0\). \(\blacksquare\)

**Corollary 2.2.** Let \(Q=\sum_jq_jw^j\) be a polynomial over \(\mathbb F_p\) of degree at most \(2p-2\). Then
\[
\sum_{w\in\mathbb F_p}Q(w)=-q_{p-1}-q_{2p-2}.
\]

**Proof.** By Lemma 2.1 only the exponents \(p-1\) and \(2p-2\) contribute, each with the factor \(-1\). \(\blacksquare\)

## 3. The number of points

Let \(E\) be the curve with the equation \(v^2=f(w)\). Its *affine points* over \(\mathbb F_p\) are the pairs \((w,v)\in\mathbb F_p^2\) with \(v^2=f(w)\). For large \(w\) the curve is described by the coordinates \(u=1/w\) and \(t=v/w^2\), in which the equation reads
\[
t^2=f_4+f_3u+f_2u^2+f_1u^3+f_0u^4 .
\]
Its *points at infinity* are the solutions with \(u=0\), that is, the \(t\) with \(t^2=f_4\). For a cubic, \(f_4=0\) and there is one point at infinity; for a quartic there are two points at infinity over \(\mathbb F_p\) if \(f_4\) is a square and none if it is not. In all cases their number is \(1+\varepsilon(f_4)\), by Lemma 1.2. Let \(N_0\) be the number of affine points over \(\mathbb F_p\), and
\[
\begin{gathered}
N=N_0+1+\varepsilon(f_4),\\
\tau=p+1-N .
\end{gathered}
\]
The integer \(\tau\) is the *trace* of the curve over \(\mathbb F_p\). When \(f\) has degree three or four and no repeated root, \(E\) with its points at infinity is a curve of genus one, and \(N\) is the number of its points with coordinates in \(\mathbb F_p\). The next theorem and its proof do not use this.

**Theorem 3.1.** \(H\) is the residue of \(\tau\) modulo \(p\):
\[
H=\tau\quad\text{in }\mathbb F_p .
\]

**Proof.** By Lemma 1.2 the number of affine points with a given first coordinate \(w\) is \(1+\varepsilon(f(w))=1+f(w)^h\). So, in \(\mathbb F_p\),
\[
\begin{aligned}
N_0&=\sum_{w\in\mathbb F_p}\bigl(1+f(w)^h\bigr)\\
&=\sum_{w\in\mathbb F_p}f(w)^h .
\end{aligned}
\]
By Corollary 2.2 the sum is \(-c_{p-1}-c_{2p-2}\). The coefficient \(c_{2p-2}=c_{4h}\) of \(f^h\) is \(f_4^h=\varepsilon(f_4)\). Hence \(N_0=-H-\varepsilon(f_4)\) and \(N=N_0+1+\varepsilon(f_4)=1-H\) in \(\mathbb F_p\), and \(\tau=p+1-N=H\). \(\blacksquare\)

For a cubic the term \(\varepsilon(f_4)\) is zero on both sides: the polynomial \(f^h\) has degree \(3h<2p-2\), and there is one point at infinity. For a quartic the points at infinity cancel the top coefficient of \(f^h\).

**Example 3.2.** For \(p=7\) and \(f=1+w^2+w^3\) the values \(f(w)\), \(w=0,\dots,6\), are \(1,3,6,2,4,4,1\). The squares modulo \(7\) are \(0,1,2,4\). So there are two affine points over each of \(w=0,3,4,5,6\) and none over \(w=1,2\): ten affine points, and one point at infinity. \(N=11\), \(\tau=8-11=-3\), and \(-3=4=H\) in \(\mathbb F_7\).

## 4. The sum over the points

**Theorem 4.1.** Let \(\mu\in\mathbb F_p\), \(\mu\ne0\), with \(d=f(\mu)\ne0\). Let \(\lambda=1/\mu\) and \(\chi=\varepsilon(d)\in\{1,-1\}\). Then
\[
\begin{aligned}
S_f(\lambda)={}&\chi-\frac{\chi f'(\mu)}{2d\lambda}\\
&-\sum_{P}\frac1{1-\lambda w(P)} ,
\end{aligned}
\]
where the sum is over the affine points \(P=(w(P),v(P))\) of \(E\) over \(\mathbb F_p\) with \(w(P)\ne\mu\).

**Proof.** Let \(F=f^h\) and
\[
Q(w)=\frac{F(w)-F(\mu)}{w-\mu},
\]
a polynomial of degree at most \(2p-3\). The number of affine points with first coordinate \(w\) is \(1+F(w)\) in \(\mathbb F_p\), and \(1-\lambda w=-\lambda(w-\mu)\). So the sum over the points is
\[
\begin{aligned}
\Sigma&=-\mu\sum_{w\ne\mu}\frac{1+F(w)}{w-\mu}\\
&=-\mu\sum_{w\ne\mu}\Bigl(\frac{1+F(\mu)}{w-\mu}+Q(w)\Bigr).
\end{aligned}
\]
*The first part vanishes.* As \(w\) runs through the elements other than \(\mu\), \(u=1/(w-\mu)\) runs through the nonzero elements of \(\mathbb F_p\), and \(\sum_{u\ne0}u=0\) by Lemma 2.1 with \(k=1\); here \(p-1\ge2\) does not divide \(1\).

*The second part.* By Corollary 2.2, \(\sum_{w\in\mathbb F_p}Q(w)=-q_{p-1}\), where \(q_{p-1}\) is the coefficient of \(w^{p-1}\) in \(Q\). Since
\[
\frac{w^m-\mu^m}{w-\mu}=\sum_{j=0}^{m-1}w^j\mu^{m-1-j},
\]
this coefficient is
\[
q_{p-1}=\sum_{m\ge p}c_m\mu^{m-p}=\frac{G_f(\mu)}{\mu},
\]
because \(\mu^p=\mu\). The value at the excluded point is \(Q(\mu)=F'(\mu)\). So
\[
\begin{aligned}
\Sigma&=-\mu\Bigl(-\frac{G_f(\mu)}{\mu}-F'(\mu)\Bigr)\\
&=G_f(\mu)+\mu F'(\mu).
\end{aligned}
\]
*Conclusion.* By Corollary 1.3 and Lemma 1.1, \(G_f(\mu)=\chi-T_f(\mu)=\chi-S_f(\lambda)\). And
\[
F'(\mu)=hf(\mu)^{h-1}f'(\mu)=-\frac{\chi f'(\mu)}{2d},
\]
because \(h=-1/2\) in \(\mathbb F_p\) and \(f(\mu)^{h-1}=\chi/d\). Hence
\[
\Sigma=\chi-S_f(\lambda)-\frac{\chi f'(\mu)}{2d\lambda}.
\]
\(\blacksquare\)

**Corollary 4.2.** With the notation of Theorem 4.1,
\[
\begin{aligned}
S_f(\lambda)={}&\chi-\frac{\chi f'(\mu)}{2d\lambda}\\
&+\mu\sum_{w\ne\mu}\frac{\varepsilon(f(w))}{w-\mu} .
\end{aligned}
\]

**Proof.** In the first display of the proof of Theorem 4.1, \(1+F(w)=1+\varepsilon(f(w))\), and \(\sum_{w\ne\mu}1/(w-\mu)=0\). So \(\Sigma=-\mu\sum_{w\ne\mu}\varepsilon(f(w))/(w-\mu)\). \(\blacksquare\)

Theorem 4.1 and Corollary 4.2 do not use that \(f\) has no repeated root, nor a condition on \(f(0)\); they hold for every polynomial of degree at most four.

**Example 4.3.** Let \(p=7\), \(f=1+w^2+w^3\), \(\mu=\lambda=1\). Then \(d=3\), \(\chi=-1\), \(f'(1)=5\), and the middle term is \(-\chi f'(\mu)/(2d\lambda)=5/6=2\) in \(\mathbb F_7\). By Example 3.2 the affine points with \(w\ne1\) lie over \(w=0,3,4,5,6\), two over each. The values \(1/(1-w)\) there are \(1,3,2,5,4\), with sum \(15=1\); so \(\Sigma=2\). The theorem gives \(S_f(1)=-1+2-2=-1=6\), in agreement with Example 1.4.

## 5. What the sums cost

Expanding \(f^h\) up to degree \(p-1\) and evaluating \(T_f\) takes a number of operations in \(\mathbb F_p\) proportional to \(p\). Corollary 4.2 is a second method of the same order, in which no power of \(f\) is expanded: one quadratic character for each element of \(\mathbb F_p\).

The main theorem of [Jordan] is of a different kind. Let \(f\) have degree three or four, no repeated root and \(f(0)=1\), let \(p\ge7\), and let \(\lambda\ne0\) with \(f(1/\lambda)\ne0\). The two points of the curve over \(w=1/\lambda\), with second coordinates \(\pm v_0\), \(v_0^2=d\), differ by a class in the group of the curve, and this class is annihilated by the integer \(M=p+1-\chi\tau\). The theorem states
\[
S_f(\lambda)=H-\frac{\chi\,\Psi}{\lambda v_0},
\]
where \(\Psi\) is the value at the point \((0,1)\) of the logarithmic derivative, taken with respect to the differential \(dw/v\), of a function on the curve whose divisor is \(M\) times the difference of the two points. This value is computed by a recurrence of V. Miller along the binary digits of \(M\), with a number of operations proportional to \(\log p\). Together with Theorem 3.1, the sum \(S_f(\lambda)\) is then determined by \(\tau\) and about \(\log p\) operations. The statement is recorded here without proof; nothing in this lesson depends on it.

## 6. Exercises

**6.1.** Let \(f_0=f(0)\ne0\) and \(g=f/f_0\). Show that \(S_f(\lambda)=\varepsilon(f_0)S_g(\lambda)\).

**6.2.** Show that \(\sum_{\lambda\ne0}S_f(\lambda)=-H-f_0^h\), the sum being over the nonzero elements of \(\mathbb F_p\).

**6.3.** Let \(p\equiv2\pmod3\) and \(f=1+w^3\). Show that \(H=0\), and show directly that \(N=p+1\).

**6.4.** Let \(f=1+aw^4\) with \(a\ne0\). Show that \(H=\binom h{(p-1)/4}a^{(p-1)/4}\) if \(p\equiv1\pmod4\), and \(H=0\) if \(p\equiv3\pmod4\).

**6.5.** Let \(p\equiv1\pmod4\), \(n=(p-1)/4\) and \(f=1-w^4/2\). Show that the coefficient of \(w^{4i}\) in \(f^h\) is \(\binom{2i}i8^{-i}\) in \(\mathbb F_p\) for \(0\le i\le h\), and that
\[
S_f(1)=\sum_{i=0}^{n}\binom{2i}i8^{-i}.
\]

**6.6.** Verify Corollary 4.2 for \(p=7\), \(f=1+w^2+w^3\) and \(\mu=1\).

## 7. Solutions

**6.1.** \(f^h=f_0^hg^h\), and \(f_0^h=\varepsilon(f_0)\). The coefficient of \(w^{p-1}\) in \(f^h/(1-\lambda w)\) is \(\varepsilon(f_0)\) times that in \(g^h/(1-\lambda w)\).

**6.2.** By Lemma 1.1 the sum is \(\sum_{\mu\ne0}T_f(\mu)=\sum_{\mu}T_f(\mu)-T_f(0)\). The polynomial \(T_f\) has degree at most \(p-1\), so \(\sum_\mu T_f(\mu)=-c_{p-1}=-H\) by Corollary 2.2. And \(T_f(0)=c_0=f_0^h\).

**6.3.** The exponents that occur in \(f^h=(1+w^3)^h\) are multiples of \(3\), and \(p-1\equiv1\pmod3\) is not; so \(H=0\). Directly: \(3\) and \(p-1\) have no common factor, so there are integers \(x,y\) with \(3x+(p-1)y=1\), and \(b\mapsto b^x\) is inverse to \(w\mapsto w^3\) on the nonzero elements. So \(w\mapsto1+w^3\) is a bijection of \(\mathbb F_p\), and the number of affine points is the number of pairs \((a,v)\) with \(v^2=a\). There are \(h\) nonzero squares \(a\), each with two square roots, and \(a=0\) with one (proof of Lemma 1.2): \(2h+1=p\) pairs. With the point at infinity, \(N=p+1\) and \(\tau=0\).

**6.4.** \(f^h=\sum_i\binom hia^iw^{4i}\). The exponent \(p-1\) occurs exactly if \(4\) divides \(p-1\), with \(i=(p-1)/4\).

**6.5.** The coefficient of \(w^{4i}\) is \(\binom hi(-1/2)^i\). In \(\mathbb F_p\), \(h=-1/2\), so
\[
\begin{aligned}
\binom hi&=\frac{(-\frac12)(-\frac32)\cdots(-\frac{2i-1}2)}{i!}\\
&=\frac{(-1)^i}{4^i}\binom{2i}i ,
\end{aligned}
\]
because \(1\cdot3\cdots(2i-1)=(2i)!/(2^ii!)\). Multiplying by \((-1/2)^i\) gives \(\binom{2i}i8^{-i}\). The denominators \(i!\), \(i\le h\), are not divisible by \(p\). The terms of \(T_f\) are those with \(4i\le p-1\), that is \(i\le n\), and \(S_f(1)=T_f(1)\).

**6.6.** The values \(\varepsilon(f(w))\) for \(w=0,2,3,4,5,6\) are \(1,-1,1,1,1,1\) (Example 3.2), and \(1/(w-1)\) there is \(-1,1,4,5,2,3\). The sum is \(-1-1+4+5+2+3=12=5\). With \(\chi=-1\) and the middle term \(2\) of Example 4.3: \(S_f(1)=-1+2+5=6\).

## References

- [Jordan] D. Jordan, *Cartier–Miller evaluation of genus-one coefficient sums*, manuscript, revised 5 October 2026, the identities (1), (2), (8) and (38) and the paragraph after (8). Repository with the text, the programs and the checks: https://github.com/bbrhuft/Cartier-Miller-evaluation-of-genus-one-coefficient-sums
