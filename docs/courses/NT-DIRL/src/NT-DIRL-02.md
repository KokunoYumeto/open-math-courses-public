# Dirichlet's theorem on primes in arithmetic progressions

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Public domain (CC0).*

For coprime integers \(b,q\), Dirichlet's theorem says that infinitely many primes satisfy \(p\equiv b\pmod q\). The obstacle is not the character detector from Dirichlet characters, but a possible zero of an associated series at 1. This lesson removes that obstacle by two positivity arguments, and then obtains both Dirichlet density and a weighted Mertens estimate.

We use partial summation, locally uniform convergence of holomorphic functions, and unique factorization. Here \(\Lambda(p^k)=\log p\) and \(\Lambda(n)=0\) otherwise. The short Chebyshev bound needed for the weighted estimate is proved at its point of use. Basic references for the character method are Koukoulopoulos's book and Sutherland's lectures. The proofs below do not require algebraic number theory or a prime number theorem.

## 1. Why a value at 1 matters

Define

\[
L(s,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^s},\qquad s=\sigma+it.
\]

For \(\sigma>1\), absolute convergence and unique factorization give

\[
L(s,\chi)=\prod_p(1-\chi(p)p^{-s})^{-1}.
\tag{1.1}
\]

The associated logarithm, normalized by tending to zero as real \(s\to+\infty\), is

\[
\ell_\chi(s)=\sum_p\sum_{k\ge1}\frac{\chi(p)^k}{k p^{ks}}.
\tag{1.2}
\]

This series converges absolutely on \(\sigma>1\), and \(L=\exp\ell_\chi\). Thus \(L\) has no zero there. Uniformly for real \(\sigma>1\), the terms with \(k\ge2\) in (1.2) are bounded in absolute value by \(\sum_p\sum_{k\ge2}p^{-k}/k<\infty\). Consequently

\[
\sum_{p\equiv b\pmod q}p^{-\sigma}
=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(b)}\ell_\chi(\sigma)+O_q(1).
\tag{1.3}
\]

The principal character contributes the divergent logarithm of the zeta function. We need to show that all the other terms stay bounded.

## 2. Periodicity gives continuation

For \(\chi\ne\chi_0\), a complete period sums to zero by orthogonality. Hence

\[
A_\chi(x)=\sum_{n\le x}\chi(n),\qquad |A_\chi(x)|\le\varphi(q).
\]

Partial summation gives, for \(\sigma>0\),

\[
L(s,\chi)=s\int_1^\infty A_\chi(u)u^{-s-1}\,du.
\tag{2.1}
\]

More explicitly, the tail after an integer \(N\) is

\[
\sum_{n>N}\chi(n)n^{-s}
=-A_\chi(N)N^{-s}+s\int_N^\infty A_\chi(u)u^{-s-1}\,du.
\]

Its absolute value is at most \(\varphi(q)N^{-\sigma}(1+|s|/\sigma)\). This bound is uniform on every compact subset of \(\sigma>0\). The defining series therefore converges there and gives a holomorphic function. Differentiation is justified locally uniformly by the analogous tail estimate with a factor \(\log u\).

For the principal character,

\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}).
\tag{2.2}
\]

The zeta function has a simple pole at 1 of residue 1, and is holomorphic elsewhere on \(\sigma>0\). One can see exactly the continuation needed here from

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{u\}u^{-s-1}\,du.
\tag{2.3}
\]

Initially this follows from \(\zeta(s)=s\int_1^\infty\lfloor u\rfloor u^{-s-1}\,du\) on \(\sigma>1\). The integral with \(\{u\}\) is holomorphic on \(\sigma>0\). Thus (2.2) has residue \(\prod_{p\mid q}(1-1/p)=\varphi(q)/q\) at 1.

## 3. Two different positivity arguments

**Proposition 3.1.** For every real \(\sigma>1\),

\[
P_q(\sigma):=\prod_{\chi\bmod q}L(\sigma,\chi)\ge1.
\]

**Proof.** Sum (1.2) over the characters and apply the detector to \(p^k\). This gives

\[
\log P_q(\sigma)
=\varphi(q)\sum_{\substack{p,k\ge1\\p^k\equiv1\pmod q}}
\frac1{k p^{k\sigma}}\ge0.
\]

This logarithm is real, so exponentiation proves the assertion. \(\square\)

**Proposition 3.2.** If \(\chi\) is nonreal, then \(L(1,\chi)\ne0\).

**Proof.** The conjugation identity \(L(\overline s,\overline\chi)=\overline{L(s,\chi)}\) follows first from the series, then throughout \(\sigma>0\) by continuation. If \(L(1,\chi)=0\), the distinct factor \(L(s,\overline\chi)\) also vanishes at 1. All nonprincipal factors are holomorphic there; the principal factor has only a simple pole. The product would consequently tend to zero as \(\sigma\downarrow1\), contradicting Proposition 3.1. \(\square\)

For a real nonprincipal character, the product \(\zeta(s)L(s,\chi)\) has a different positivity property. Write

\[
r(n)=\sum_{d\mid n}\chi(d),\qquad
\zeta(s)L(s,\chi)=\sum_{n\ge1}r(n)n^{-s}\quad(\sigma>1).
\]

The function \(r\) is multiplicative. At a prime power,

\[
r(p^k)=\begin{cases}
k+1,&\chi(p)=1,\\
1_{k\text{ even}},&\chi(p)=-1,\\
1,&\chi(p)=0.
\end{cases}
\tag{3.1}
\]

Thus \(r(n)\ge0\) for all \(n\), and \(r(m^2)\ge1\).

**Lemma 3.3 (positivity principle).** If a Dirichlet series with nonnegative coefficients converges absolutely for \(\sigma>1\) and its sum extends holomorphically to \(\sigma>0\), the series converges at every positive real argument.

**Proof.** Fix a real \(a>1\). Termwise differentiation gives

\[
(-1)^jF^{(j)}(a)=\sum_n c_n(\log n)^j n^{-a}\ge0.
\]

The disk \(|s-a|<a\) lies in the half-plane of holomorphy. For \(0<h<a\), the Taylor series at \(a\), evaluated at \(a-h\), converges. All its terms in the displayed representation are nonnegative, so Tonelli's theorem permits the exchange

\[
F(a-h)=\sum_{j\ge0}\frac{h^j}{j!}\sum_n c_n(\log n)^j n^{-a}
=\sum_n c_n n^{-a}e^{h\log n}
=\sum_n c_n n^{-(a-h)}.
\]

Choosing \(a-h\) to be any positive real number proves the claim. This is the form of Landau's positivity theorem needed here. \(\square\)

**Theorem 3.4 (nonvanishing at 1).** Every nonprincipal Dirichlet character satisfies \(L(1,\chi)\ne0\). For a real nonprincipal character, \(L(1,\chi)>0\).

**Proof.** Only real characters remain. If \(L(1,\chi)=0\), its zero cancels the only pole of \(\zeta\) on \(\sigma>0\). Hence \(\zeta(s)L(s,\chi)\) is holomorphic on that half-plane. Lemma 3.3 forces its series to converge at \(s=1/2\), but

\[
\sum_n\frac{r(n)}{\sqrt n}\ge\sum_{m\ge1}\frac{r(m^2)}m\ge\sum_{m\ge1}\frac1m=\infty.
\]

This contradiction proves nonvanishing. Each Euler factor of \(L(\sigma,\chi)\) is positive for real \(\sigma>1\), so continuity and nonvanishing make the limit at 1 positive. \(\square\)

## 4. From nonvanishing to primes

For a nonprincipal character, \(L\) has a nonzero value at 1 and is holomorphic near 1. It therefore has a holomorphic logarithm in a small disk about 1. On the real interval immediately to the right of 1, this logarithm and \(\ell_\chi\) differ by a constant multiple of \(2\pi i\). Thus \(\ell_\chi(\sigma)=O_q(1)\) as \(\sigma\downarrow1\).

For the principal character, (2.2) gives

\[
\ell_{\chi_0}(\sigma)=\log\frac1{\sigma-1}+O_q(1).
\]

Substitution in (1.3) proves the following theorem.

**Theorem 4.1 (Dirichlet).** If \((b,q)=1\), then

\[
\boxed{\sum_{p\equiv b\pmod q}p^{-\sigma}
=\frac1{\varphi(q)}\log\frac1{\sigma-1}+O_q(1)}
\qquad(\sigma\downarrow1).
\]

In particular there are infinitely many such primes. Their **Dirichlet density**, defined as the limit of the ratio of this sum to \(\sum_p p^{-\sigma}\), is \(1/\varphi(q)\).

This density weights primes by \(p^{-\sigma}\); it does not assert an asymptotic for their unweighted counting function. The latter is proved in the lesson on the prime number theorem for progressions.

### A weighted Mertens theorem without a prime number theorem

We first establish the upper bound used in the error term. Every prime \(n<p\le2n\) divides \(\binom{2n}{n}\), and \(\binom{2n}{n}\le4^n\). Taking logarithms, summing over dyadic intervals, and comparing a real \(x\) to the next power of 2 gives \(\theta(x)=\sum_{p\le x}\log p\le Cx\) for an absolute \(C\). Moreover,

\[
\psi(x)=\sum_{k\le\log x/\log2}\theta(x^{1/k})
\le Cx+C\frac{\log x}{\log2}\sqrt x\ll x,
\]

since \((\log x)/\sqrt x\) is bounded on \(x\ge2\). This proves the needed form of Chebyshev's estimate directly.

**Theorem 4.2.** For fixed \(q\) and \((b,q)=1\),

\[
\sum_{\substack{p\le x\\p\equiv b\pmod q}}\frac{\log p}{p}
=\frac{\log x}{\varphi(q)}+O_q(1)\qquad(x\ge2).
\tag{4.1}
\]

**Proof.** First let \(\chi\ne\chi_0\). Periodicity and partial summation show

\[
\sum_{m\le y}\frac{\chi(m)}m=L(1,\chi)+O_q(y^{-1}),
\qquad
\sum_{n\le x}\frac{\chi(n)\log n}{n}=O_q(1).
\]

The identity \(\log n=\sum_{d\mid n}\Lambda(d)\), with complete multiplicativity, now gives

\[
\begin{aligned}
\sum_{n\le x}\frac{\chi(n)\log n}{n}
&=\sum_{d\le x}\frac{\chi(d)\Lambda(d)}d
  \sum_{m\le x/d}\frac{\chi(m)}m\\
&=L(1,\chi)\sum_{d\le x}\frac{\chi(d)\Lambda(d)}d
  +O_q\left(\frac1x\sum_{d\le x}\Lambda(d)\right).
\end{aligned}
\]

Chebyshev's bound makes the error \(O_q(1)\), and Theorem 3.4 lets us divide by \(L(1,\chi)\). Thus the twisted sum of \(\Lambda(d)/d\) is bounded.

For the untwisted sum, the same divisor identity gives

\[
\sum_{n\le x}\log n
=\sum_{d\le x}\Lambda(d)\lfloor x/d\rfloor
=x\sum_{d\le x}\frac{\Lambda(d)}d+O(x).
\]

The left side is \(x\log x-x+O(\log x)\), by integral comparison or Stirling's formula. Hence \(\sum_{d\le x}\Lambda(d)/d=\log x+O(1)\). Restricting to \((d,q)=1\) deletes only the bounded sum \(\sum_{p\mid q}\sum_{k\ge1}(\log p)/p^k\). Apply the character detector to obtain

\[
\sum_{\substack{n\le x\\n\equiv b\pmod q}}\frac{\Lambda(n)}n
=\frac{\log x}{\varphi(q)}+O_q(1).
\]

Finally the terms with \(n=p^k\), \(k\ge2\), have total weight at most \(\sum_p(\log p)/(p(p-1))<\infty\). Removing them proves (4.1). \(\square\)

**Example 4.3.** For the odd character modulo 4,

\[
L(1,\chi_{-4})=\sum_{k\ge0}\left(\frac1{4k+1}-\frac1{4k+3}\right)
=\int_0^1\frac{dt}{1+t^2}=\frac\pi4.
\]

For the character modulo 3,

\[
L(1,\chi_{-3})
=\int_0^1\frac{1-t}{1-t^3}\,dt
=\int_0^1\frac{dt}{1+t+t^2}
=\frac{\pi}{3\sqrt3}.
\]

The integral expressions follow by integrating finite geometric sums and taking their limit. The paired summands are positive, so monotone convergence also justifies the exchange directly. These values give explicit instances of the positivity conclusion in Theorem 3.4.

## 5. Exercises

**Exercise 5.1 (easy).** Evaluate the alternating series \(1-1/3+1/5-1/7+\cdots\), carefully justifying its expression as an integral.

**Exercise 5.2 (medium).** Give elementary proofs that each of the classes 1 and 3 modulo 4 contains infinitely many primes.

**Exercise 5.3 (medium).** Explain why the boundedness of the prime-power tail in Theorem 4.2 suffices even though \(p^k\equiv b\pmod q\) does not imply \(p\equiv b\pmod q\). Deduce \(\sum_{p\le x,\ p\equiv b(q)}1/p=\varphi(q)^{-1}\log\log x+O_q(1)\).

**Exercise 5.4 (hard).** Give a proof of real-character nonvanishing using a weighted Dirichlet hyperbola decomposition, without Lemma 3.3. Apply it to \(H(x)=\sum_{n\le x}r(n)/\sqrt n\).

**Exercise 5.5 (medium).** Show directly from Euler factors that \(\prod_{\chi\bmod q}L(s,\chi)\) has nonnegative Dirichlet-series coefficients.

### Solutions

**5.1.** The sum paired in consecutive terms is \(\sum_{k\ge0}(1/(4k+1)-1/(4k+3))\). Each term equals \(\int_0^1t^{4k}(1-t^2)\,dt\), whose integrand is nonnegative. Monotone convergence gives the integral of \((1-t^2)/(1-t^4)=1/(1+t^2)\). This is \(\arctan1=\pi/4\). The paired limit agrees with the ordinary alternating-series limit, since its omitted last term tends to zero.

**5.2.** Suppose the primes 3 modulo 4 form a finite list, with product \(P\) (take \(P=1\) for an empty list). The integer \(4P-1\) is 3 modulo 4. Its prime factorization must contain a prime 3 modulo 4 to an odd exponent, and no prime in the list divides it. This is a contradiction. For the class 1, let \(P\) be the product of its supposed finite list. The odd number \((2P)^2+1>1\) has a prime divisor \(r\). The class of \(2P\) modulo \(r\) has square \(-1\), hence order 4, so \(4\mid r-1\). But no listed prime divides this number, another contradiction.

**5.3.** The absolute weight of *all* higher prime powers is bounded independently of \(x\); every subset, whatever its residue condition, has weight at most that bound. Thus deleting exactly the powers in the progression changes the sum by \(O(1)\). Put \(B(x)=\sum_{p\le x,\ p\equiv b(q)}(\log p)/p\). Partial summation gives

\[
\sum_{\substack{p\le x\\p\equiv b(q)}}\frac1p
=\frac{B(x)}{\log x}+\int_2^x\frac{B(t)}{t(\log t)^2}\,dt.
\]

Substitute \(B(t)=\log t/\varphi(q)+O_q(1)\). The error integral is bounded, while the main integral is \(\varphi(q)^{-1}(\log\log x-\log\log2)\). The boundary term is bounded. This proves the assertion, and Theorem 4.2 supplies the weighted estimate used in it.

**5.4.** Suppose \(L(1,\chi)=0\), and write \(y=\lfloor\sqrt x\rfloor\), with \(x\ge4\). Define

\[
C(v)=\sum_{n\le v}\frac{\chi(n)}{\sqrt n},\qquad
A(v)=\sum_{n\le v}\frac1{\sqrt n}.
\]

Bounded character partial sums give \(C(v)=L(1/2,\chi)+O_q(v^{-1/2})\). Also \(A(v)=2\sqrt v+c+O(v^{-1/2})\) for an absolute constant \(c\); this follows by summing the integrable differences between \(n^{-1/2}\) and its integral on successive unit intervals. The hyperbola identity is

\[
H(x)=\sum_{a\le y}\frac{C(x/a)}{\sqrt a}
 +\sum_{b\le y}\frac{\chi(b)A(x/b)}{\sqrt b}
 -A(y)C(y).
\]

Every pair \(ab\le x\) has \(a\le y\) or \(b\le y\), and their intersection is the square \(a,b\le y\), which proves the identity. The first sum is \(L(1/2,\chi)A(y)+O_q(y/\sqrt x)\). Subtracting \(A(y)C(y)\) leaves \(O_q(1)\). The second sum equals

\[
2\sqrt x\sum_{b\le y}\frac{\chi(b)}b+cC(y)+O(y/\sqrt x).
\]

The assumed vanishing and the tail estimate at 1 imply \(\sum_{b\le y}\chi(b)/b=O_q(1/y)\), so this too is \(O_q(1)\). Thus \(H(x)=O_q(1)\). But positivity and the squares give \(H(x)\ge\sum_{m\le\sqrt x}1/m\to\infty\), a contradiction.

**5.5.** If \(p\nmid q\) and \(f\) is the order of \(p\) in \(U_q\), restriction of characters to \(\langle p\rangle\) is onto by the extension lemma. Each \(f\)-th root of unity consequently occurs \(\varphi(q)/f\) times among \(\chi(p)\). Hence the Euler factor of the product is

\[
\prod_{\chi\bmod q}(1-\chi(p)z)^{-1}
=(1-z^f)^{-\varphi(q)/f}.
\]

Its coefficients are nonnegative by the binomial expansion for a positive integral exponent. For \(p\mid q\) the factor is 1. Absolute convergence on \(\sigma>1\) permits multiplication of these series, giving nonnegative global coefficients.

## What this lesson does not prove

The elementary tools of complex and real analysis are prerequisites. The character results used here are proved in the preceding lesson. All analytic continuation, positivity, nonvanishing, Chebyshev support and progression estimates stated in this lesson have been proved above. No assertion about natural density or uniformity as \(q\) grows is made here; those are the subject of later lessons.

## References

- Andrew V. Sutherland, [*Dirichlet L-functions, primes in arithmetic progressions*](https://math.mit.edu/classes/18.785/2019fa/LectureNotes18.pdf), MIT 18.785, 2019; for characters, Euler products and the distinction between densities.
- Dimitris Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), Graduate Studies in Mathematics 203, American Mathematical Society, 2019; Chapters 2, 9, 11 and 12.
