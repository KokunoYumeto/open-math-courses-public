# The complex exponential and the circle

This prerequisite develops the exponential, trigonometric functions, their exact periods and polar coordinates from convergent series.

*The first-zero and unit-circle treatment follows Jiří Lebl's Basic Analysis, volume II, version 6.3, “Complex exponential and trigonometric functions.” The text, including the product-of-series argument, estimates and endpoint details, is by GPT-6 Astra (OpenAI), in Codex at Ultra; the present selection and local reading links are by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). The [source and edition notice](assets/notices/complex-exponential-source-notice.html) credits the source and links its native excerpt.*

## Starting knowledge

We use the complete ordered field \(\mathbb R\), finite complex arithmetic, natural-number induction and elementary sets and functions. The earlier proofs are in [Real analysis on closed intervals](real-analysis-on-closed-intervals.md): Proposition 1 gives the Archimedean property; Lemma 2 and Theorem 3 give limits and completeness; Theorems 5–6 give extreme and intermediate values; Theorem 8 and Corollary 9 give derivative rules; and Theorems 12–13 give integration. Its geometric-tail argument supplies the series bound used below. Neither Cauchy's integral theorem nor the complex identity theorem is an input.

These results supply the exact exponential kernel and circle parametrization used in [The scalar Cauchy formula and power series](scalar-cauchy.md).

## Convergent series and the exponential

**Lemma 1 (Absolute convergence and multiplication).** For every real \(R\geq0\), the series \(\sum_{n\geq0}R^n/n!\) converges. For complex \(z,w\), the two series with terms \(z^n/n!\) and \(w^n/n!\) may be multiplied and grouped by total degree.

**Proof.** Choose an integer \(N\geq 2R\). For \(n\geq N\), successive terms have ratio \(R/(n+1)\leq1/2\); thus every tail is bounded by a convergent geometric series. This proves convergence, uniformly for \(|z|\leq R\).

More generally, if \(\sum_j |a_j|=A<\infty\) and \(\sum_k |b_k|=B<\infty\), the sum of \(|a_jb_k|\) over any finite rectangle is at most \(AB\). The sum over pairs with \(j>M\) or \(k>M\) is at most
\[
B\sum_{j>M}|a_j|+A\sum_{k>M}|b_k|,
\]
which tends to zero. All finite sets of pairs containing a sufficiently large square therefore give the same limit. Both rectangular summation and grouping by total degree exhaust such squares, so both have that limit. Finite rectangular sums are products of finite sums; taking their limits proves the multiplication assertion. \(\square\)

Define
\[
E(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!},\qquad z\in\mathbb C.
\]

**Theorem 2 (Addition, inversion and differentiation).** For all complex \(z,w\),
\[
E(0)=1,\quad E(z+w)=E(z)E(w),\quad E(z)\ne0,
\quad E(-z)=E(z)^{-1},\quad E'(z)=E(z),
\quad \overline{E(z)}=E(\bar z).
\]
For real \(x\), \(E(x)>0\). Its restriction to the real line is strictly increasing and maps that line onto \((0,\infty)\).

**Proof.** The binomial theorem and Lemma 1 give
\[
E(z)E(w)=\sum_{n=0}^{\infty}\sum_{j=0}^{n}
\frac{z^jw^{n-j}}{j!(n-j)!}
=\sum_{n=0}^{\infty}\frac{(z+w)^n}{n!}=E(z+w).
\]
Taking \(w=-z\) proves inversion and nonvanishing. Conjugation commutes with limits of finite sums and gives the last identity.

Let \(C=\sum_{n=2}^{\infty}1/n!<\infty\). If \(|h|\leq1\),
\[
|E(h)-1-h|\leq C|h|^2.
\]
Consequently \(E(h)\to1\) and \((E(h)-1)/h\to1\). The addition law shows that \(E\) is continuous everywhere and that
\[
\frac{E(z+h)-E(z)}h
=E(z)\frac{E(h)-1}h\longrightarrow E(z).
\]
For real \(x\), the series is real and \(E(x)=E(x/2)^2>0\). Its derivative is therefore positive, so the mean value theorem gives strict increase. For \(x\geq0\), the series gives \(E(x)\geq1+x\); hence \(E(x)\to\infty\) as \(x\to\infty\). Inversion then gives \(E(x)\to0\) as \(x\to-\infty\). Continuity and the intermediate value theorem prove surjectivity onto \((0,\infty)\). \(\square\)

We write \(e^z=E(z)\). This agrees with the real exponential characterized by \(f'=f\), \(f(0)=1\): if a real differentiable \(f\) has those properties, differentiation gives \((f(x)E(-x))'=0\), so the product is identically one. Define \(\log r\), for \(r>0\), as the unique real \(x\) with \(E(x)=r\).

## Sine, cosine and elementary identities

For complex \(z\), define
\[
\cos z=\frac{E(iz)+E(-iz)}2,\qquad
\sin z=\frac{E(iz)-E(-iz)}{2i}.
\]

**Theorem 3 (Trigonometric identities).** For every complex \(z\),
\[
E(iz)=\cos z+i\sin z,\qquad
\cos^2z+\sin^2z=1,
\]
\[
\cos(-z)=\cos z,\quad\sin(-z)=-\sin z,
\quad\cos'(z)=-\sin z,\quad\sin'(z)=\cos z.
\]
Their values at zero are \(1,0\), respectively, and
\[
\cos z=\sum_{n=0}^{\infty}\frac{(-1)^nz^{2n}}{(2n)!},\qquad
\sin z=\sum_{n=0}^{\infty}\frac{(-1)^nz^{2n+1}}{(2n+1)!}.
\]
For real \(x\), sine and cosine are real, \(E(ix)\) has modulus one, \(|\sin x|,|\cos x|\leq1\), and \(\sin x\leq x\) when \(x\geq0\).

**Proof.** Euler's identity, the values at zero and parity follow by adding, subtracting or reversing the defining expressions. Set \(a=E(iz)\), \(b=E(-iz)\). Then \(ab=1\), and
\[
\left(\frac{a+b}{2}\right)^2+
\left(\frac{a-b}{2i}\right)^2=ab=1.
\]
This proves the square identity for complex as well as real arguments. Theorem 2 and the chain rule give
\[
\cos'(z)=\frac{iE(iz)-iE(-iz)}2=-\sin z,
\quad
\sin'(z)=\frac{iE(iz)+iE(-iz)}{2i}=\cos z.
\]
In the two defining series, even powers agree and odd powers cancel when adding; odd powers agree and even powers cancel when subtracting and dividing by \(i\). Absolute convergence justifies these operations and gives the displayed series.

For real \(x\), \(E(-ix)=\overline{E(ix)}\). Thus cosine and sine are its real and imaginary parts, while \(E(ix)\overline{E(ix)}=1\). Their absolute values are at most one. Finally \((x-\sin x)'=1-\cos x\geq0\) and the difference vanishes at zero. The real mean value theorem proves the last inequality. \(\square\)

Multiplication of \(E(iz)\) and \(E(iw)\) gives, by the definitions, the addition identities
\[
\cos(z+w)=\cos z\cos w-\sin z\sin w,
\quad
\sin(z+w)=\sin z\cos w+\cos z\sin w.
\]
These are identities for complex arguments; they do not require a geometric definition of angle.

## The exact period and polar coordinates

**Theorem 4 (The first zero and the circle).** Cosine has a smallest positive zero \(r\). Define \(\pi=2r\). Then
\[
E(i\pi/2)=i,\quad E(i\pi)=-1,\quad E(2\pi i)=1.
\]
The map \(t\mapsto E(it)\) is a bijection from \([0,2\pi)\) onto the unit circle. Moreover
\[
E(it)=1\quad\Longleftrightarrow\quad t\in2\pi\mathbb Z
\qquad(t\in\mathbb R).
\]
Both sine and cosine have least positive real period \(2\pi\), even when regarded as functions on \(\mathbb C\).

**Proof.** Cosine is positive near zero. If it had no positive zero, continuity would force it to be positive everywhere on \([0,\infty)\). Sine would then be strictly increasing there. Fix \(a>0\); then \(\sin a>0\), and for \(t>a\) the fundamental theorem gives
\[
\cos t=\cos a-\int_a^t\sin s\,ds
\leq\cos a-(t-a)\sin a,
\]
which is eventually negative. This contradiction proves existence of a positive zero. If \(T\) is such a zero, the zeros in \([0,T]\) form a nonempty closed set separated from zero. Its infimum is positive and is attained by continuity; call it \(r\). Cosine is positive on \([0,r)\). Sine is strictly increasing there, so \(\sin r>0\). The square identity and \(\cos r=0\) imply \(\sin r=1\). Hence \(E(ir)=i\), and the addition law gives \(E(2ir)=-1\) and \(E(4ir)=1\).

No \(t\in(0,4r)\) satisfies \(E(it)=1\). Indeed, \(u=E(it/4)\) has strictly positive real and imaginary parts, since \(0<t/4<r\). But \(u^4=1\) would imply
\[
(u-1)(u+1)(u-i)(u+i)=0,
\]
making \(u\) one of \(1,-1,i,-i\), none of which has both parts strictly positive. Since \(4r=2\pi\), division of any real \(t\) into \(2\pi n+s\), with \(n\in\mathbb Z\) and \(0\leq s<2\pi\), proves the asserted kernel. It also proves injectivity on the half-open interval.

For surjectivity, let \(a,b\geq0\) and \(a^2+b^2=1\). Cosine decreases continuously from \(1\) to \(0\) on \([0,r]\), so there is \(t\in[0,r]\) with \(\cos t=a\). Since \(\sin t\geq0\), the square identity gives \(\sin t=b\). Every point of the circle is \(i^k(a+ib)\) for a point in this closed quadrant and \(k\in\{0,1,2,3\}\). The addition law represents it as \(E(i(t+kr))\); subtract \(2\pi\) if the parameter equals \(2\pi\). This also covers the quadrant endpoints without excluding the point \(1\).

The equality \(E(z+2\pi i)=E(z)\) for all complex \(z\) proves that both trigonometric functions have real period \(2\pi\). If \(T>0\) is a period of cosine, then \(\cos T=1\), so the real square identity gives \(\sin T=0\), and \(E(iT)=1\). If \(T>0\) is a period of sine, then \(\sin T=0\) and
\[
1=\sin(r+T)=\sin r\cos T+\cos r\sin T=\cos T.
\]
Again \(E(iT)=1\). The kernel assertion proves that no smaller positive period exists. \(\square\)

**Corollary 5 (The exponential fibre and polar form).** Every nonzero complex \(w\) can be written
\[
w=|w|E(i\theta),\qquad 0\leq\theta<2\pi.
\]
This \(\theta\) is unique. All solutions of \(E(z)=w\) are
\[
z=\log|w|+i(\theta+2\pi n),\qquad n\in\mathbb Z.
\]
In particular \(E(z)=E(w)\) if and only if \(z-w\in2\pi i\mathbb Z\).

**Proof.** Apply Theorem 4 to \(w/|w|\). For real \(x,y\), the addition law and unit modulus give
\[
|E(x+iy)|=E(x),\qquad E(x+iy)=E(x)E(iy).
\]
Therefore any solution has \(x=\log|w|\), and its imaginary part is precisely one of the angles supplied by the kernel assertion. The final equivalence follows by applying this to \(E(z-w)=1\). \(\square\)

## Source and next reading

Jiří Lebl, [Basic Analysis](https://www.jirka.org/ra/), volume II, version 6.3, “Complex exponential and trigonometric functions.” See the [source and edition notice](assets/notices/complex-exponential-source-notice.html).

Continue with [The scalar Cauchy formula and power series](scalar-cauchy.md).
