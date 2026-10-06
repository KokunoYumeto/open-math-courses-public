# Dirichlet series and Euler products

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, Ultra. Public domain (CC0).*

Prime factorization becomes an analytic identity when we weight an integer $n$ by $n^{-s}$. The resulting function can encode divisors, squarefree integers or prime powers. This lesson explains when that encoding is valid, how to recover its coefficients, and why positivity sometimes forces a singularity. We then construct the first continuation of the Riemann zeta function.

We assume [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10), [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), and [Number Theory and Cryptology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C60). Lemma 2.0 below proves unique prime factorization and Möbius inversion. Appendix A supplies the integration, holomorphic-limit, Cauchy, residue, logarithm and argument-principle tools used here and in later lessons. Free comparison sources are Koukoulopoulos’s author preliminary version and the digitized Bohr–Cramér article listed below.

Write $s=\sigma+it$ and use the real logarithm in $n^{-s}=\exp(-s\log n)$. Thus $|n^{-s}|=n^{-\sigma}$. An arithmetic function is a function on the positive integers. Its Dirichlet series is

$$F(s)=\sum_{n=1}^{\infty}a(n)n^{-s}.$$

The order of summation here is increasing $n$. That convention matters when the convergence is conditional.

## 1. Moving a convergent series to the right

A power series converges in a disc. A Dirichlet series instead converges in a right half-plane. The elementary reason is that increasing the real part of $s$ adds a decreasing weight to a convergent series.

**Lemma 1.1 (summation by parts).** Put $A(u)=\sum_{N<n\le u}b(n)$, where $N,M$ are positive integers and $M\ge N$. For a continuously differentiable function $f$ on $[N,M]$,

$$\sum_{N<n\le M}b(n)f(n)=A(M)f(M)-\int_N^M A(u)f'(u)\,du.$$

**Proof.** Write $f(n)=f(M)-\int_n^M f'(u)\,du$. Substitute into the finite sum and interchange the finite sum and the integral. The inner sum consists exactly of the integers $n$ with $N<n\le u$. The choice of values at the finitely many endpoints does not affect the integral. $\square$

**Theorem 1.2 (convergence and holomorphy).** If $\sum a(n)n^{-s_0}$ converges, then $F$ converges at every $s$ with $\Re s>\Re s_0$. It converges uniformly on compact subsets of that half-plane. For each $0<\delta<\pi/2$, it also converges uniformly on the closed sector

$$s=s_0+w,\qquad |\arg w|\le \pi/2-\delta,$$

including its vertex $w=0$. Consequently $F$ is holomorphic to the right of its abscissa of convergence, and for every integer $k\ge0$,

$$F^{(k)}(s)=\sum_{n=1}^{\infty}a(n)(-\log n)^k n^{-s}$$

there, with uniform convergence on compact subsets.

**Proof.** Set $b(n)=a(n)n^{-s_0}$. Given $\varepsilon>0$, convergence gives an integer $N_0$ such that

$$\left|\sum_{N<n\le u}b(n)\right|\le\varepsilon\qquad(u\ge N\ge N_0).$$

Apply Lemma 1.1 to $f(u)=u^{-w}$. If $v=\Re w>0$, the tail is at most

$$\varepsilon M^{-v}+\varepsilon |w|\int_N^M u^{-v-1}\,du
\le \varepsilon N^{-v}\left(1+\frac{|w|}{v}\right).$$

On a compact subset of $\Re w>0$, $v$ is bounded below and $|w|$ is bounded above. This proves the uniform Cauchy criterion. In the sector, $|w|/v\le1/\sin\delta$; the same estimate is uniform over the whole sector. At $w=0$ the original tail is at most $\varepsilon$.

Each finite sum is entire. The locally uniform limit is therefore holomorphic. To justify differentiation, surround a compact set by a slightly larger compact set in the convergence half-plane. Cauchy's integral formula expresses each derivative of the tail by its values on circles of a fixed small radius. The uniform tail bound on those circles tends to zero. Hence the derivatives of the finite sums converge uniformly to the derivatives of $F$, giving the displayed series. $\square$

**Theorem 1.3 (the two abscissae).** There are extended real numbers $\sigma_c\le\sigma_a$ such that the series converges for $\sigma>\sigma_c$ and fails to converge for $\sigma<\sigma_c$, while it converges absolutely for $\sigma>\sigma_a$ and fails to converge absolutely for $\sigma<\sigma_a$. When they are finite,

$$0\le\sigma_a-\sigma_c\le1.$$

In extended-real notation the assertion is $\sigma_c\le\sigma_a\le\sigma_c+1$. The boundary lines require separate examination.

**Proof.** Define $\sigma_c$ as the infimum of the real parts of points where the series converges, and $\sigma_a$ as the infimum of the real numbers where $\sum |a(n)|n^{-\sigma}$ converges. Theorem 1.2 and comparison of nonnegative series prove the half-plane assertions. Absolute convergence implies convergence, so $\sigma_c\le\sigma_a$.

If the series converges at $s_0$, its terms are bounded: $|a(n)|n^{-\Re s_0}\le C$. Therefore

$$\sum |a(n)|n^{-\sigma}\le C\sum n^{-(\sigma-\Re s_0)}<\infty\qquad(\sigma>\Re s_0+1).$$

Taking infima gives $\sigma_a\le\sigma_c+1$. If $\sigma_c=-\infty$, this argument gives $\sigma_a=-\infty$. If $\sigma_c=+\infty$, absolute convergence nowhere follows from the first inequality. Thus the extended-real formulation covers both exceptional cases without subtracting infinities. $\square$

For zeta, both abscissae are $1$. Indeed $\sum n^{-\sigma}$ converges for $\sigma>1$ and diverges for real $\sigma\le1$. Theorem 1.2 rules out convergence anywhere with real part less than $1$: such convergence would force convergence at a real point between that real part and $1$.

**Theorem 1.4 (uniqueness of coefficients).** Suppose two Dirichlet series converge absolutely in a common half-plane. If their sums agree at points $s_j$ with $\Re s_j\to+\infty$, their coefficients agree.

**Proof.** Subtract the series. If a nonzero coefficient exists, let $m$ be the first one, called $c(m)$. Absolute convergence at a real number $\sigma_0$ gives

$$m^s\sum_{n\ge m}c(n)n^{-s}=c(m)+\sum_{n>m}c(n)(m/n)^s.$$

For $\Re s\ge\sigma_0$, the tail is dominated termwise by the summable sequence $|c(n)|(m/n)^{\sigma_0}$. Each term tends to zero as $\Re s\to\infty$, regardless of $\Im s$. Dominated convergence for this series gives a limit of $c(m)$. Along $s_j$ the left side is zero, so $c(m)=0$, a contradiction. $\square$

## 2. Multiplication remembers factorization

The Dirichlet convolution of arithmetic functions is

$$(a*b)(n)=\sum_{d\mid n}a(d)b(n/d).$$

Let $\mathbf1(n)=1$ and let $\varepsilon(1)=1$, $\varepsilon(n)=0$ for $n>1$.

**Lemma 2.0 (the arithmetic identities).** Every positive integer has unique prime factorization. Define $\mu(1)=1$, $\mu(n)=(-1)^r$ when $n$ is a product of $r$ distinct primes, and $\mu(n)=0$ when a prime square divides $n$. Then convolution is associative and commutative, has identity $\varepsilon$, and
$$
\mu*\mathbf1=\varepsilon,\qquad
 b=\mathbf1*a\ \Longleftrightarrow\ a=\mu*b.
$$
For $\varphi(n)=\#\{1\le k\le n:(k,n)=1\}$,
$$
\sum_{d\mid n}\varphi(d)=n.
$$

**Proof.** The Euclidean algorithm terminates because its nonzero remainders decrease. At each division, common divisors are unchanged; reversing the divisions expresses the greatest common divisor of $a,b$ as an integer combination of them. If a prime $p$ does not divide $a$, their greatest common divisor is one, so multiplying such a combination by $b$ shows that $p\mid ab$ implies $p\mid b$. Existence of prime factorization follows by strong induction, splitting a composite integer into two smaller factors. The preceding prime-divisor property proves uniqueness: match a prime in one factorization with a factor in the other, cancel it, and continue by induction.

Commutativity of convolution replaces $d$ by $n/d$. Both ways of associating three factors give the finite sum $\sum_{uvw=n}a(u)b(v)c(w)$, so they agree. The identity property of $\varepsilon$ is immediate from its sole nonzero value at one. In $\sum_{d\mid n}\mu(d)$ only squarefree divisors contribute; selecting their primes gives $\prod_{p\mid n}(1-1)$. This is zero for $n>1$ and one for $n=1$, proving the first identity. Multiplying by $\mu$ or $\mathbf1$ proves the two directions of inversion using associativity. Finally partition $1,\ldots,n$ by $d=(k,n)$. Writing $k=dj$ identifies the part indexed by $d$ with the integers $1\le j\le n/d$ coprime to $n/d$, of which there are $\varphi(n/d)$. Summing and reindexing proves the totient identity. $\square$

These are the convolution conventions used below.

**Proposition 2.1.** If $A(s)=\sum a(n)n^{-s}$ and $B(s)=\sum b(n)n^{-s}$ converge absolutely at $s$, then

$$A(s)B(s)=\sum_{n\ge1}(a*b)(n)n^{-s},$$

and the series on the right converges absolutely.

**Proof.** The sum of the absolute values of the double series is

$$\sum_{m,n\ge1}\frac{|a(m)b(n)|}{(mn)^\sigma}
=\left(\sum_m\frac{|a(m)|}{m^\sigma}\right)
 \left(\sum_n\frac{|b(n)|}{n^\sigma}\right)<\infty.$$

We may group the terms by $mn=k$. The grouped coefficient is $(a*b)(k)$, and the same double sum bounds the sum of the absolute values of the grouped terms. $\square$

A multiplicative function satisfies $a(1)=1$ and $a(mn)=a(m)a(n)$ when $(m,n)=1$. A completely multiplicative function satisfies that identity for all $m,n$.

**Theorem 2.2 (Euler products).** If $a$ is multiplicative and $\sum |a(n)|n^{-\sigma}<\infty$, then

$$\sum_{n\ge1}a(n)n^{-s}
=\prod_p\left(1+\sum_{k\ge1}a(p^k)p^{-ks}\right).$$

The product converges absolutely in the sense that the sum over $p$ of the absolute deviations of the factors from $1$ is finite. Its value is nonzero if and only if every local factor is nonzero.

**Proof.** Write $u_p=\sum_{k\ge1}a(p^k)p^{-ks}$. Then

$$\sum_p|u_p|\le\sum_p\sum_{k\ge1}|a(p^k)|p^{-k\sigma}<\infty.$$

The last terms are a subset of the absolutely convergent original series. For finitely many primes $p\le y$, multiplication of their absolutely convergent local series and unique factorization give

$$\prod_{p\le y}(1+u_p)=\sum_{P^+(n)\le y}a(n)n^{-s},$$

where the condition includes $n=1$, and $P^+(n)$ denotes the largest prime factor for $n>1$. Every fixed integer eventually belongs to this sum. The absolute tail outside any sufficiently large finite set is small, so the right side tends to the full series.

For large $p$, $|u_p|<1/2$ and the power-series logarithm satisfies $|\log(1+u_p)|\le2|u_p|$. Thus the tail product is the exponential of a convergent series and is nonzero. Only the finitely many initial factors can vanish. This proves the final assertion as well. $\square$

The distinction in the last sentence is useful. A multiplicative function supported on $1$ and powers of $2$, with $a(2)=-4$ and $a(2^k)=0$ for $k\ge2$, has the everywhere convergent series $1-4\cdot2^{-s}$. Its local factor vanishes at $s=2$. Absolute product convergence alone does not imply nonvanishing.

## 3. Three ways to read the primes in zeta

Define

$$\zeta(s)=\sum_{n\ge1}n^{-s}\qquad(\sigma>1).$$

Euler's product is

$$\zeta(s)=\prod_p(1-p^{-s})^{-1}.$$

Here every local factor is a convergent geometric series and is nonzero. Theorem 2.2 therefore proves $\zeta(s)\ne0$ for $\sigma>1$.

Define the von Mangoldt function by $\Lambda(p^k)=\log p$ for primes $p$ and integers $k\ge1$, and $\Lambda(n)=0$ otherwise. In particular $\Lambda(1)=0$. Factorization immediately gives

$$\sum_{d\mid n}\Lambda(d)=\log n,$$

since a prime $p$ appearing to exponent $r$ contributes $r\log p$. Thus $\log=\mathbf1*\Lambda$ and Möbius inversion gives $\Lambda=\mu*\log$.

**Proposition 3.1.** On $\sigma>1$,

$$\frac1{\zeta(s)}=\sum_{n\ge1}\frac{\mu(n)}{n^s},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},$$

and

$$\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}
=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}\,n^{-s}.$$

The logarithm is the holomorphic branch real on the real interval $(1,\infty)$.

**Proof.** Since $|\mu(n)|\le1$, Proposition 2.1 applies to the series of $\mu$ and $\mathbf1$. Their product is the series of $\varepsilon$, namely $1$. This proves the reciprocal formula.

For the logarithm, expand $-\log(1-z)=\sum_{k\ge1}z^k/k$ at $z=p^{-s}$. On $\sigma\ge1+\eta$, the double series converges absolutely and uniformly: it is bounded by $\sum_p p^{-1-\eta}/(1-p^{-1-\eta})$. Exponentiating finite prime sums and passing to the limit proves that its exponential is $\zeta$. Its value is real on $(1,\infty)$, so it selects the claimed branch. The replacement of $p^k$ by $n$ gives the last expression.

Local uniform convergence allows differentiation. The derivative of the double series is $-\sum_{p,k}(\log p)p^{-ks}$. Equivalently, use $\Lambda=\mu*\log$, Proposition 2.1 and $-\zeta'(s)=\sum (\log n)n^{-s}$. Either calculation gives the logarithmic derivative formula. $\square$

### Worked example: arithmetic functions as quotients of zeta

Let $d(n)$ count positive divisors, $\sigma_a(n)=\sum_{d\mid n}d^a$ for a real parameter $a$, and $\varphi(n)$ be Euler's totient. Let $\lambda(n)=(-1)^{\Omega(n)}$, where $\Omega$ counts prime factors with multiplicity. Then

| Function | Dirichlet series | Half-plane of absolute convergence |
| --- | --- | --- |
| $d$ | $\zeta(s)^2$ | $\sigma>1$ |
| $\sigma_a$ | $\zeta(s)\zeta(s-a)$ | $\sigma>1+\max(a,0)$ |
| $\varphi$ | $\zeta(s-1)/\zeta(s)$ | $\sigma>2$ |
| $\mu^2$ | $\zeta(s)/\zeta(2s)$ | $\sigma>1$ |
| $\lambda$ | $\zeta(2s)/\zeta(s)$ | $\sigma>1$ |

Here is a direct verification of every row. The first two follow from $d=\mathbf1*\mathbf1$ and $\sigma_a=\mathbf1*(n\mapsto n^a)$. For the totient, Lemma 2.0 gives $\sum_{d\mid n}\varphi(d)=n$, hence $\varphi=\mu*(n\mapsto n)$. A squarefree integer contributes $1$ to $\mu^2$, so its local factor is $1+p^{-s}=(1-p^{-2s})/(1-p^{-s})$. Complete multiplicativity gives the local factor for $\lambda$ as $(1+p^{-s})^{-1}=(1-p^{-s})/(1-p^{-2s})$.

The listed boundaries are exact as abscissae. For $d$ and $\sigma_a$, lower bounds $d(n)\ge1$, $\sigma_a(n)\ge1$ and, when $a>0$, $\sigma_a(n)\ge n^a$, prove divergence at and to the left of their stated real boundaries. For $\varphi$, the nonnegative series equals $\zeta(s-1)/\zeta(s)$ for real $s>2$, and tends to infinity as $s\downarrow2$; monotone convergence shows divergence at $2$. The same argument applied to $\zeta(s)/\zeta(2s)$ shows divergence of the series of $\mu^2$ at $1$. Finally $|\lambda(n)|=1$, so its absolute series is exactly the series of zeta on the real axis. This does not determine the conditional-convergence abscissa of the Liouville series.

## 4. What positivity prevents

A singularity of a sum need not occur at the boundary of convergence of its defining series. Nonnegative coefficients change that situation.

**Theorem 4.1 (Landau).** Suppose $a(n)\ge0$ and $\sigma_c$ is finite. Then $F$ has no holomorphic continuation to a neighbourhood of the real point $\sigma_c$. The conclusion also holds if the coefficients are eventually nonnegative.

**Proof.** Suppose there were such a continuation, holomorphic on $|s-\sigma_c|<r$ as well as on $\Re s>\sigma_c$. Choose $0<h<r/3$ and put $b=\sigma_c+h$. The disc $|s-b|<2h$ is contained in the continuation region. Therefore the Taylor series at $b$ converges at $b-z$ for real $h<z<2h$.

Positivity makes convergence at the real number $b$ absolute, and Theorem 1.2 gives

$$(-1)^k F^{(k)}(b)=\sum_n a(n)(\log n)^k n^{-b}\ge0.$$

All terms of the following double sum are nonnegative. Tonelli's theorem, or monotone convergence for finite rectangles, gives

$$\begin{aligned}
F(b-z)&=\sum_{k\ge0}\frac{(-1)^kF^{(k)}(b)}{k!}z^k\\
&=\sum_n a(n)n^{-b}\sum_{k\ge0}\frac{(z\log n)^k}{k!}
=\sum_n a(n)n^{-(b-z)}.
\end{aligned}$$

The finite value of the Taylor series proves convergence at $b-z<\sigma_c$, a contradiction. If only finitely many coefficients are negative, subtract their Dirichlet polynomial. Such a polynomial is entire and does not change convergence of the tail or the possibility of continuation. $\square$

*Reference:* [Bohr–Cramér 1923, §6], which attributes this singularity theorem to Landau.

### Worked example: cancellation in the alternating series

Put

$$\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}.$$

The coefficient partial sums are bounded. Lemma 1.1 proves convergence for $\sigma>0$. At $s=0$ the terms fail to tend to zero; at every point with $\sigma<0$ their absolute values tend to infinity. Thus $\sigma_c=0$. Its absolute series is zeta's, so $\sigma_a=1$.

For $\sigma>1$, separating even and odd integers is legitimate and gives

$$\eta(s)=(1-2^{1-s})\zeta(s).$$

The right side continues to an entire function: Exercise 5 proves that zeta has no pole except at $1$, and the factor $1-2^{1-s}$ cancels that simple pole. Hence the series has a finite convergence boundary although its sum is entire. This is exactly the phenomenon forbidden by Theorem 4.1 for nonnegative coefficients. The defining alternating series still does not converge everywhere.

## 5. Subtracting the pole of zeta

We can continue zeta partway without a functional equation. The useful device is to separate the integer-counting function into its linear part and its bounded error.

**Theorem 5.1.** For $\sigma>0$, $s\ne1$, the continuation of zeta is

$$\zeta(s)=\frac{s}{s-1}-s\int_1^{\infty}\{u\}u^{-s-1}\,du,$$

where $\{u\}=u-\lfloor u\rfloor$. It has a simple pole at $1$, of residue $1$, and

$$\zeta(s)=\frac1{s-1}+\gamma+O(|s-1|),$$

where $\gamma=\lim_{N\to\infty}(\sum_{n\le N}1/n-\log N)$. For real $0<\sigma<1$, $\zeta(\sigma)<0$.

**Proof.** For $\sigma>1$, summation by parts, followed by a limit, gives

$$\zeta(s)=s\int_1^{\infty}\lfloor u\rfloor u^{-s-1}\,du.$$

The boundary term vanishes because $\lfloor u\rfloor u^{-s}=O(u^{1-\sigma})$. Substitute $\lfloor u\rfloor=u-\{u\}$ and evaluate the first integral. Since $0\le\{u\}<1$, the second integral converges locally uniformly for $\sigma>0$, including after multiplication by any fixed power of $\log u$. It is holomorphic there. The rational term has residue $1$ at $1$, while the integral is holomorphic at $1$.

For an integer $N\ge1$, the same calculation applied to the tail gives

$$\zeta(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1}
-s\int_N^{\infty}\{u\}u^{-s-1}\,du.$$

Taking the constant term at $s=1$ yields

$$\lim_{s\to1}\left(\zeta(s)-\frac1{s-1}\right)
=H_N-\log N-\int_N^{\infty}\frac{\{u\}}{u^2}\,du.$$

The last integral is at most $1/N$. Integral comparison shows that $H_N-\log N$ has a finite limit: it is bounded below and decreasing, since $1/(N+1)<\log(1+1/N)$. Letting $N\to\infty$ identifies the constant as $\gamma$. Holomorphy of the pole-subtracted function gives the stated Laurent error.

For $0<\sigma<1$, the rational term $\sigma/(\sigma-1)$ is negative and the subtracted integral is nonnegative. This proves the strict sign claim. $\square$

**Corollary 5.2 (Euler's divergence of reciprocal primes).** As $\sigma\downarrow1$,

$$\sum_p p^{-\sigma}=\log\frac1{\sigma-1}+O(1).$$

In particular $\sum_p1/p$ diverges.

**Proof.** The Laurent expansion gives $\log\zeta(\sigma)=\log(1/(\sigma-1))+O(\sigma-1)$ for real $\sigma>1$. Proposition 3.1 shows that its difference from $\sum_pp^{-\sigma}$ is

$$\sum_p\sum_{k\ge2}\frac{p^{-k\sigma}}k,$$

which stays bounded as $\sigma\downarrow1$, since it is at most $\sum_{n\ge2}1/(n(n-1))$. If $\sum_p1/p$ were finite, it would dominate $\sum_pp^{-\sigma}$ for every $\sigma>1$, contradicting the divergence just proved. $\square$

This argument supplies more than infinitude of primes. The prime harmonic series diverges, although it has only one term for each prime.

## 6. Exercises

1. **Easy — squarefree divisors.** Let $\omega(n)$ count the distinct prime factors of $n$. Prove
   $$\sum_{n\ge1}2^{\omega(n)}n^{-s}=\frac{\zeta(s)^2}{\zeta(2s)}\qquad(\sigma>1).$$
   Explain why the coefficients count squarefree divisors.

2. **Medium — slow cancellation.** Determine both convergence abscissae of
   $$\sum_{n\ge1}\frac{(-1)^n}{n^s\log(n+1)}.$$
   Examine the real boundary points as well.

3. **Medium — an entire sum with positive coefficients.** Suppose a Dirichlet series with nonnegative coefficients converges somewhere and its sum continues to an entire function. Prove that the series converges absolutely for every complex $s$. Explain why the assumption of convergence somewhere is needed to speak of continuation of its sum.

4. **Medium — the alternating continuation.** Use $\eta$ to continue zeta to $\sigma>0$. Show that each apparent pole of $\eta(s)/(1-2^{1-s})$ at $s=1+2\pi ik/\log2$, $k\ne0$, is removable, and compute $\eta(1)$.

5. **Hard — continuation by Euler–Maclaurin.** Prove the following formula for integers $N,m\ge1$:
   $$\begin{aligned}
   \zeta(s)={}&\sum_{n<N}n^{-s}+\frac{N^{1-s}}{s-1}+\frac12N^{-s}\\
   &+\sum_{k=1}^{m}\frac{B_{2k}}{(2k)!}(s)_{2k-1}N^{1-s-2k}\\
   &-\frac{(s)_{2m}}{(2m)!}\int_N^{\infty}B_{2m}(\{u\})u^{-s-2m}\,du.
   \end{aligned}$$
   Here $(s)_j=s(s+1)\cdots(s+j-1)$, $(s)_0=1$, and the Bernoulli numbers use $B_1=-1/2$. Determine the exact half-planes of ordinary improper convergence and absolute convergence of the integral, with the upper endpoint tending to infinity through all real values. Specify the domain of this formula for each fixed $m$. Continue zeta to the whole plane and evaluate $\zeta(0)$ and $\zeta(-1)$.

## 7. Solutions

**Solution 1.** A squarefree divisor chooses, independently for each prime dividing $n$, whether that prime is included. There are $2^{\omega(n)}$ choices. Thus $2^{\omega}=\mathbf1*\mu^2$. Proposition 2.1 and the worked example give the identity. Alternatively the local series is

$$1+2\sum_{k\ge1}p^{-ks}=\frac{1+p^{-s}}{1-p^{-s}}
=\frac{1-p^{-2s}}{(1-p^{-s})^2}.$$

Absolute convergence for $\sigma>1$ follows from $2^{\omega(n)}\le d(n)$ and the absolute convergence of the divisor series. Either argument therefore justifies the multiplication rather than treating it merely formally.

**Solution 2.** At the real point $s=0$, the terms $1/\log(n+1)$ decrease to zero, so the alternating-series test gives convergence. Theorem 1.2 then gives convergence for $\sigma>0$. For $\sigma<0$, the term magnitudes $n^{-\sigma}/\log(n+1)$ tend to infinity, so no such point admits convergence. Therefore $\sigma_c=0$; the real point on this boundary is convergent.

Absolute convergence holds for $\sigma>1$ by comparison with $\sum n^{-\sigma}$. At $\sigma=1$, grouping $2^j\le n<2^{j+1}$ gives a lower bound $c/(j+1)$ for the contribution of the block, with an absolute $c>0$. The sum of these bounds diverges. For $\sigma<1$, the terms of the absolute series are no smaller than those at $1$. Hence $\sigma_a=1$, and the real absolute boundary point is divergent.

**Solution 3.** Convergence somewhere implies $\sigma_c<+\infty$. If $\sigma_c$ were a finite real number, Landau's theorem would contradict entire continuation. Thus $\sigma_c=-\infty$. For nonnegative coefficients, convergence at each real $\sigma$ is absolute and supplies absolute convergence at every point with that real part. The requirement of initial convergence excludes a purely formal series whose sum was never defined on any half-plane.

**Solution 4.** Theorem 1.2 shows that $\eta$ is holomorphic on $\sigma>0$. On $\sigma>1$, the quotient equals zeta wherever its denominator is nonzero. The zeros of $1-2^{1-s}$ are exactly $s=1+2\pi ik/\log2$, $k\in\mathbb Z$, and they are simple. Their derivative in that expression equals $\log2$.

To check the other apparent poles using alternating-type series themselves, define

$$\eta_3(s)=\sum_{n\ge1}(1-3\mathbf1_{3\mid n})n^{-s}.$$

Its coefficient partial sums are bounded, so it is holomorphic for $\sigma>0$. Separating multiples of $3$ for $\sigma>1$ gives $\eta_3=(1-3^{1-s})\zeta$. Eliminating zeta there and using the identity theorem gives, throughout $\sigma>0$,

$$(1-3^{1-s})\eta(s)=(1-2^{1-s})\eta_3(s).$$

At a nonreal zero $s_k$ of $1-2^{1-s}$, the factor $1-3^{1-s_k}$ cannot vanish. Otherwise $k\log3/\log2$ would be an integer, which would imply an equality between a nontrivial integer power of $2$ and one of $3$, contrary to unique factorization. Thus near $s_k$ the quotient of interest agrees off $s_k$ with the holomorphic function $\eta_3/(1-3^{1-s})$. This proves removability and constructs the continuation using the two bounded-coefficient series. It agrees with Theorem 5.1 by uniqueness of continuation. At $1$, using $1-2^{1-s}=(s-1)\log2+O((s-1)^2)$ and the residue of zeta gives $\eta(1)=\log2$. In particular the denominator zero at $1$ does not make the quotient removable: zeta retains its pole there.

**Solution 5.** Define the Bernoulli polynomials by the identity of power series near $t=0$,

$$\frac{te^{xt}}{e^t-1}=\sum_{j\ge0}B_j(x)\frac{t^j}{j!},\qquad B_j=B_j(0).$$

This gives $B_1(x)=x-1/2$, $B_2=1/6$, $B_j'(x)=jB_{j-1}(x)$, and $B_j(1)=B_j(0)$ for $j\ne1$. The endpoint difference follows by subtracting the generating series at $x=0$ from that at $x=1$, obtaining $t$. The generating identity also gives $B_{2k+1}=0$ for $k\ge1$: $t/(e^t-1)+t/2$ is even.

For a smooth function $f$ and integers $M>N$, integration on each interval $[n,n+1]$ gives

$$\sum_{N<n\le M}f(n)=\int_N^M f(u)\,du+\frac{f(M)-f(N)}2
+\int_N^M B_1(\{u\})f'(u)\,du.$$

Indeed integration by parts on that interval says that the last integral is $(f(n+1)+f(n))/2-\int_n^{n+1}f(u)\,du$. Summing telescopes to the displayed formula.

Integrate the last term by parts repeatedly, using $B_j'/j!=B_{j-1}/(j-1)!$ and the equality of endpoint values for $j\ge2$. The odd Bernoulli endpoint terms vanish. After $2m-1$ integrations this becomes

$$\begin{aligned}
\sum_{N<n\le M}f(n)={}&\int_N^M f(u)\,du+\frac{f(M)-f(N)}2\\
&+\sum_{k=1}^m\frac{B_{2k}}{(2k)!}
 \bigl(f^{(2k-1)}(M)-f^{(2k-1)}(N)\bigr)\\
&-\frac1{(2m)!}\int_N^M B_{2m}(\{u\})f^{(2m)}(u)\,du.
\end{aligned}$$

Apply this first for $\sigma>1$ to $f(u)=u^{-s}$. Its $j$th derivative is $(-1)^j(s)_j u^{-s-j}$. Let $M\to\infty$, add $\sum_{n\le N}n^{-s}$ and combine the $N$ endpoint term with that sum. This is precisely the formula in the exercise, including its negative remainder sign.

To determine the full convergence domain, put $z=s+2m$, $v=\Re z$, and

$$g(u)=B_{2m}(\{u\}),\qquad
G(u)=\frac{B_{2m+1}(\{u\})}{2m+1}.$$

The Bernoulli identities above show that $G'=g$ on each unit interval. Since $m\ge1$, its endpoint values are $G(k)=0$ at every integer $k$. Thus $G$ is bounded and continuous across the endpoints. Write $C_m=\max_{0\le x\le1}|B_{2m+1}(x)|/(2m+1)$. Piecewise integration by parts gives, for every real $T\ge N$,

$$\int_N^T g(u)u^{-z}\,du
=G(T)T^{-z}+z\int_N^T G(u)u^{-z-1}\,du.$$

If $v>0$, the boundary term tends to zero and the last integral converges absolutely. Hence the original remainder integral exists and satisfies

$$I_{m,N}(s):=\int_N^\infty g(u)u^{-z}\,du
=z\int_N^\infty G(u)u^{-z-1}\,du,\qquad
|I_{m,N}(s)|\le \frac{|z|C_m}{v}N^{-v}.$$

Its tail after a real endpoint $T$ is

$$-G(T)T^{-z}+z\int_T^\infty G(u)u^{-z-1}\,du,$$

of modulus at most $C_mT^{-v}(1+|z|/v)$. On a compact set $K$ in $v>0$, choose $\varepsilon>0$ with $v\ge\varepsilon$ on $K$; $|z|$ is also bounded there. Differentiating the last integral is justified by integrable bounds of the form $C_{K,j}u^{-1-\varepsilon}(1+(\log u)^j)$ for each derivative order $j\ge0$. The differentiated boundary term and tail integral are bounded by $C'_{K,j}T^{-\varepsilon}(1+(\log T)^j)$, which tends to zero. Consequently the original truncations and all their parameter derivatives converge locally uniformly, and $I_{m,N}$ is holomorphic on $\sigma>-2m$. In particular,

$$I_{m,N}^{(j)}(s)
=\int_N^\infty B_{2m}(\{u\})(-\log u)^j u^{-s-2m}\,du
\qquad(\sigma>-2m).$$

This domain is necessary for ordinary improper convergence. The generating identity shows that $B_{2m}(x)$ has leading coefficient $1$, so there are $0<a<b<1$ with $c=\int_a^b B_{2m}(x)\,dx\ne0$. For fixed complex $z$, uniformly on $[a,b]$, $(1+x/k)^{-z}=1+O_z(k^{-1})$. Thus

$$\int_{k+a}^{k+b}g(u)u^{-z}\,du
=k^{-z}\left(c+O_z(k^{-1})\right).$$

If $v\le0$, the modulus of this partial-period integral does not tend to zero. That contradicts the Cauchy criterion for an improper integral with arbitrary real truncation endpoints. It also excludes every point on $v=0$; taking only integer endpoints would be a different limit.

For absolute convergence, let $A_m=\int_0^1|B_{2m}(x)|\,dx>0$. On $[k,k+1]$, $u^{-v}$ is bounded above and below by positive constants depending on $v$ times $k^{-v}$. Therefore

$$\int_k^{k+1}|g(u)u^{-z}|\,du\asymp_v A_m k^{-v}.$$

Summing over $k\ge N$ proves absolute convergence exactly when $v>1$. The original integral thus converges ordinarily exactly for $\sigma>-2m$, absolutely exactly for $\sigma>1-2m$, and conditionally throughout $-2m<\sigma\le1-2m$.

Everything on the original Euler--Maclaurin right side except $N^{1-s}/(s-1)$ is holomorphic on $\sigma>-2m$. By the identity theorem, the formula derived for $\sigma>1$, with all its original factors and its negative remainder sign, remains valid on $\sigma>-2m$, $s\ne1$. Different values of $m$ give the same continuation on their overlaps. Since $m$ is arbitrary, these half-planes cover $\mathbb C$. The only possible pole is at $1$, and its residue is $1$.

For $s=0$, take $N=1$, $m=1$. The rising factorials in the correction and remainder vanish, leaving $-1+1/2=-1/2$. For $s=-1$, take $N=1$, $m=2$, so that the remainder integral itself converges at the point before its zero prefactor is used. The first correction is $(B_2/2!)(-1)=-1/12$, the higher correction and remainder have zero rising-factorial prefactors, and the integral and endpoint terms are $-1/2+1/2=0$. Hence

$$\zeta(0)=-\frac12,\qquad\zeta(-1)=-\frac1{12}.$$

The sharper convergence domain also allows $N=1$, $m=1$ at $s=-1$: the remainder integral then exists conditionally before its zero prefactor $(s)_2=s(s+1)$ is used. The same endpoint terms and first Bernoulli correction give $-1/12$. A vanishing prefactor would not by itself define a product with a divergent integral.

This is continuation of an analytic function. It does not assert ordinary convergence of $1+1+1+\cdots$ or $1+2+3+\cdots$.

## Appendix A. Analysis facts used in this course

This appendix proves the complex-analysis and integration tools used above and in subsequent lessons. A holomorphic function is complex differentiable on an open set; a contour is a piecewise continuously differentiable path. We use the real integral, countable additivity of measure, and the completeness of the real numbers from the real-analysis prerequisites. No theorem about zeta is used here.

### A.1. Interchanging limits and integrals

**Lemma A.1.** On the Lebesgue and counting measure spaces used here, increasing nonnegative measurable functions $g_j$ satisfy
$\int\lim_j g_j=\lim_j\int g_j$. If $f_j\to f$ almost everywhere and $|f_j|\le g$ with $\int g<\infty$, then $\int|f_j-f|\to0$, and consequently $\int f_j\to\int f$. These statements apply to counting measure and hence to series. Nonnegative double series can be summed in either order.

**Proof.** Define the nonnegative integral as the supremum of the integrals of nonnegative simple functions below the integrand. Write $g=\lim g_j$. Clearly $\int g_j\le\int g$. Given a nonnegative simple $h\le g$ with finite integral and $0<c<1$, the sets $E_j=\{g_j\ge ch\}$ increase and exhaust the set where $h>0$. Countable additivity gives continuity of measure from below: write an increasing union as the disjoint union of its successive differences. Apply that identity on each of the finitely many level sets of $h$. It gives $\int_{E_j}h\to\int h$, and therefore $\lim_j\int g_j\ge c\int h$. Take the supremum over such $h$, then let $c\uparrow1$. Simple functions with infinite integral are handled by finite-measure truncations of their level sets; this gives the same conclusion when the limiting integral is infinite. This proves monotone convergence.

For any nonnegative $v_j$, apply it to $\inf_{j\ge k}v_j$ to obtain
$\int\liminf v_j\le\liminf\int v_j$. Now set $v_j=2g-|f_j-f|\ge0$, after discarding the common null set. Since $|f|\le g$, the limiting function is $2g$. The last inequality and the finiteness of $\int g$ give
$\limsup\int|f_j-f|\le0$. The assertion about $\int f_j$ follows from the integral triangle inequality. For a nonnegative double series, both iterated sums and the sum over finite rectangles are the supremum of the sums over finite sets of index pairs: every such set fits in a rectangle. They are thus equal. For an absolutely convergent complex series the same conclusion follows by bounding the omitted terms by its nonnegative absolute series. $\square$

When the continuous integrands converge locally uniformly, a common integrable envelope gives a concrete alternative to the preceding argument: choose a finite interval with uniformly small tail integral, and then use uniform convergence on its compact subintervals. For series, choose a finite head with uniformly small absolute tail. These are the limiting operations in the gamma integrals and Dirichlet-series arguments. Two continuous integrations over a compact rectangle can be interchanged because their finite Riemann sums have the same double sum and converge uniformly. Nonnegative improper integrals are obtained by increasing compact rectangles; absolute integrable bounds give the same assertion for complex integrands by removing uniformly small tails. This proves the double-integral interchanges used in the gamma and beta calculations.

### A.2. Cauchy's theorem and its formula

**Lemma A.2.** A holomorphic function has zero integral around the boundary of any triangle whose closed interior is in its domain. It has a primitive on a simply connected domain. If $f$ is holomorphic on a neighbourhood of a closed disc and $z$ is in its interior, then
$$
 f(z)=\frac1{2\pi i}\int_{|\zeta-a|=r}
                  \frac{f(\zeta)}{\zeta-z}\,d\zeta.
\tag{A.1}
$$
It has a convergent power series in every disc on which it is holomorphic, with coefficient bound $|a_n|\le M_r/r^n$ at the centre. In particular
$|f^{(n)}(a)|\le n!M_r/r^n$.

**Proof.** Subdivide a triangle into four triangles with half the side lengths. The four oriented boundary integrals add to the original integral $I$, since interior sides cancel. One subtriangle has integral of modulus at least $|I|/4$. Repeat this choice; nested compact triangles have a common point $z_0$, their diameters and perimeters being $2^{-j}$ times those of the original triangle. Complex differentiability gives
$f(z)=f(z_0)+f'(z_0)(z-z_0)+o(|z-z_0|)$. The first two terms have zero boundary integral by direct integration of a constant and a linear function. On sufficiently small chosen triangles the remaining integral has modulus at most $\epsilon$ times perimeter times diameter. Since $|I|\le4^j|I_j|$, this bounds $|I|$ by a fixed multiple of $\epsilon$. Let $\epsilon\downarrow0$.

In a convex disc, integrals along two polygonal paths with the same endpoints agree by triangulating the region between them. The integral along a segment from a fixed base point therefore defines a primitive: comparison along the short segment from $z$ to $z+h$ makes its difference quotient tend to $f(z)$. Integrals of $f$ around paths in that disc are zero. In a simply connected domain a closed path is homotopic to a constant path. Cover the compact image of a homotopy by such discs, subdivide its parameter square finely enough that each small square maps into one disc, and connect its vertex images there by segments. Each small boundary integral is zero. Cancellation shows that the integrals on the two outside paths agree. Piecewise smooth paths are limits of these polygonal paths, and their integrals converge by uniform continuity on their compact images. Thus every closed contour has zero integral, and integration from a base point gives the global primitive.

To prove (A.1), integrate $f(\zeta)/(\zeta-z)$ between the outer circle and a small circle about $z$. Polygonal subdivision, with the inner boundary oppositely oriented, gives equality of the two integrals; smooth boundaries follow by polygonal approximation. On the small circle, write $\zeta=z+\epsilon e^{iu}$. Its integral is $i\int_0^{2\pi}f(z+\epsilon e^{iu})\,du$, tending to $2\pi i f(z)$. This proves (A.1) without assuming higher derivatives. At a disc centre expand
$1/(\zeta-z)=\sum_{n\ge0}(z-a)^n/(\zeta-a)^{n+1}$ on the outer circle. The expansion converges uniformly on each smaller disc. Integration gives the power series and $|a_n|\le M_r/r^n$; termwise differentiation gives the derivative bound. $\square$

The same subdivision argument works for a region with finitely many disjoint holes: its outer integral is the sum of the positively oriented inner integrals. We use this form for rectangles with deleted pole discs and for slit contours, taking their sides at positive distance from the slit before passing to a limit.

### A.3. Zeros, residues, logarithms and harmonic estimates

**Lemma A.3.** A nonzero holomorphic function on a connected domain has isolated zeros, each of a finite integer order. A meromorphic function has the residue formula on a bounded region with a finite piecewise smooth boundary and closure inside its meromorphicity domain, provided the boundary avoids its poles. If $f$ has no zeros or poles on that boundary, then
$$
\frac1{2\pi i}\int_{\partial D}\frac{f'(z)}{f(z)}\,dz
 =\#\{\text{zeros in }D\}-\#\{\text{poles in }D\},
\tag{A.2}
$$
with multiplicity. A zero-free holomorphic function on a simply connected domain has a holomorphic logarithm. Real parts of holomorphic functions have the circle mean-value property and the harmonic maximum principle. A holomorphic function has the maximum-modulus principle and Schwarz's disc estimate: if $f(0)=0$ and $|f|\le1$ on the unit disc, then $|f(z)|\le|z|$.

**Proof.** The first nonzero coefficient of the local power series gives $f(z)=(z-a)^m h(z)$ with $h(a)\ne0$. If every coefficient vanishes, $f$ vanishes on a disc. The set of points near which it vanishes is open and closed, by overlapping power-series discs, so it is the whole connected domain. This proves the assertion about zeros and also the identity theorem.

For a meromorphic function, delete small discs about its poles. Cauchy's theorem on the remaining region equates the outside integral with the sum of their circle integrals. At a pole, subtract its finite principal part; the holomorphic remainder has zero circle integral. Direct integration of $(z-a)^k$ around a circle is zero unless $k=-1$, when it is $2\pi i$. Thus the outside integral is $2\pi i$ times the sum of residues. If an annular Laurent expansion is needed, apply (A.1) to an annulus, subtracting the inner-boundary term, and expand both kernels in geometric series on a smaller concentric annulus. Uniform convergence gives the Laurent series and the same coefficient integrals.

The factorization at a zero gives $f'/f=m/(z-a)+h'/h$. At a pole its corresponding residue is the negative pole order. The residue formula now proves (A.2). Along a boundary where $f\ne0$, the imaginary part of $(f'/f)dz$ is the increment of a continuous argument, as follows by differentiating a local logarithm along each short arc. The increments add, so (A.2) also proves the change-of-argument form of the argument principle. For Rouché's theorem assume that $f$ and $g$ are holomorphic on a neighbourhood of the closure of such a region $D$. If $|g|<|f|$ on its boundary, $f+u g$ is nonzero there for $0\le u\le1$. Its argument-principle integral is continuous in $u$ and integer valued, hence constant. This proves the zero-count comparison usually called Rouché's theorem.

On a simply connected domain, Lemma A.2 gives a primitive $G$ of $f'/f$. The derivative of $f e^{-G}$ is zero, so it is a nonzero constant. Choosing a complex logarithm of that constant gives the required logarithm of $f$. Power-series integration on a circle shows that the mean of $\operatorname{Re}F$ equals its value at the centre. For a $C^2$ real harmonic function on a disc, the form $-u_y\,dx+u_x\,dy$ has zero integral around a rectangle: apply the fundamental theorem of calculus to the opposite sides and integrate $u_{xx}+u_{yy}=0$ over its interior. Subdivision, or the same calculation in coordinates on triangles, gives zero on polygonal loops in the disc. Integrating the form along paths gives a primitive, which is a harmonic conjugate by direct differentiation. Thus the same mean identity holds for such harmonic functions. If a harmonic function attains its maximum in the interior, its circle mean and the nonnegative difference from that maximum force equality on each sufficiently small circle and hence on a neighbourhood. Connectedness then makes it constant. Minimum statements follow by changing sign.

If $|f|$ attains a positive interior maximum at $a$, choose a unit complex number $c$ with $c f(a)=|f(a)|$. The harmonic function $\operatorname{Re}(c f)$ is bounded above by that same maximum and attains it, so it is constant. The Cauchy–Riemann equations then make $f$ constant. A zero maximum already means $f=0$. Finally $f(z)/z$ is holomorphic at zero by the power series. On $|z|=r<1$ it has modulus at most $1/r$. The maximum principle gives that bound inside; let $r\uparrow1$. $\square$

### A.4. Holomorphic limits and parameter integrals

**Lemma A.4.** Locally uniform limits of holomorphic functions are holomorphic, and their derivatives converge locally uniformly. A parameter integral whose integrand is jointly continuous on compact intervals of integration and compact parameter sets, and holomorphic in the parameter, is holomorphic if its absolute value has a common integrable bound on each compact parameter neighbourhood. Finitely many fixed interval break points do not affect the assertion. The same conclusion applies to sums. For holomorphic $u_n$, if $\sum_n|u_n(z)|$ converges locally uniformly, the product $\prod_n(1+u_n(z))$ converges locally uniformly. For each compact set $K$ inside the domain, a sufficiently late tail is holomorphic and zero-free on a neighbourhood of $K$. If no factor $1+u_n$ is identically zero, the product at each point has exactly the zero multiplicity contributed by the finitely many factors vanishing there.

**Proof.** On a closed circle within the domain, pass a uniformly convergent sequence through (A.1). The limiting integral is differentiable in each smaller disc: its kernel and every fixed derivative are uniformly bounded there. It gives both holomorphy and convergence of derivatives by the Cauchy derivative formula. On a compact interval of integration, uniform continuity makes Riemann sums converge uniformly on compact parameter sets. Each sum is holomorphic, so the first assertion proves holomorphy of the finite-interval integral. The common integrable envelope bounds the omitted tails uniformly; the same assertion gives holomorphy of the full integral. Split at the finitely many interval break points when necessary. The derivative conclusion follows on a smaller parameter disc from the Cauchy derivative formula. The argument applies about every parameter value.

For the product, choose a compact neighbourhood of the compact set under consideration. A sufficiently late tail has $|u_n|<1/2$ uniformly on that neighbourhood. The power series $\log(1+u)=\sum_{k\ge1}(-1)^{k+1}u^k/k$ has modulus at most $2|u|$ there. Its sum over the tail converges locally uniformly and is holomorphic by the first assertion. Exponentiating gives the limiting tail product, which is zero-free on this neighbourhood. The finitely many earlier factors account for the zero multiplicities there; this cutoff may depend on the compact neighbourhood. An identically zero factor makes the full product identically zero. $\square$

For free comparison of these elementary analysis proofs, see Jiří Lebl, [*Guide to Cultivating Complex Analysis: Working the Complex Field*](https://www.jirka.org/ca/ca.pdf), version 1.9 (11 July 2026), Sections 3.3–3.5, 4.3, 5.3–5.4 and 7.1. The proofs used by this course are written above.

## Freely readable sources

- D. Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), freely readable author preliminary version, 367 pages. Chapters 3–4: arithmetic convolution and Dirichlet series.
- H. Bohr and H. Cramér, [*Die neuere Entwicklung der analytischen Zahlentheorie*](https://archive.org/download/dieneuereentwick00bohruoft/dieneuereentwick00bohruoft.pdf) (1923), freely digitized complete primary article; Section 6.
