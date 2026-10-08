# Zero-density estimates and primes in short intervals

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; Section 10.1 written and self-checked by Claude Opus 5.5 (Anthropic). Self-check is by the writing AI. Original exposition and proofs are public domain (CC0).*

A density estimate counts possible exceptions to RH. Combined with a zero-free region, even a comparatively weak density estimate can make the zero sum in a short-interval explicit formula smaller than its main term. We develop the zero detector, the mean-value count and the exponent bookkeeping before using these tools for primes.

The sharp explicit formula is proved in Perron's formula and prime counting, Theorem 2.2. We use the full polynomial mean value and fourth-moment bound in Mean values, Theorem 2.1, Theorem 6.1 and Corollary 6.2. The exponentially smoothed detector and discrete sampling argument were established, before any use of LH, in The Riemann hypothesis implies the Lindelöf hypothesis, equations (6.4)–(6.6) and Lemma 6.1. The Vinogradov–Korobov zero-free region and its complete qualitative exponential-sum input are proved in Growth bounds and wider zero-free regions, Lemma 3.0 and Sections 3–8. The local multiplicity bound is Nonvanishing and a zero-free region, Theorem 2.2. These are exact inputs, not extra hypotheses about zeros.

Write $N(\sigma,T)=\#\{\rho=\beta+i\gamma:\beta\ge\sigma,\ 0<\gamma\le T\}$, with multiplicities. All bounds below count zeros throughout the strip, including zeros on the indicated boundary. We write $d(n)$ for the ordinary divisor function.


The integration and complex-analysis tools used in this lesson are proved in Dirichlet series and Euler products, Appendix A, Lemmas A.1–A.4.

## 1. Detecting a zero by a polynomial or an integral

Let

$$
M_X(s)=\sum_{d\le X}\frac{\mu(d)}{d^s},\qquad
a_X(n)=\sum_{\substack{d\mid n\\d\le X}}\mu(d).
\tag{1.1}
$$

Multiplication of absolutely convergent series gives $\zeta(s)M_X(s)=\sum a_X(n)n^{-s}$. Möbius inversion says $a_X(1)=1$ and $a_X(n)=0$ for $2\le n\le X$; always $|a_X(n)|\le d(n)$.

**Lemma 1.1 (zero detector).** Suppose $T$ is sufficiently large, $X=\lfloor T\rfloor$, $T\le Y\le T^{3/2}$, and $\rho=\beta+i\gamma$ is a zero with

$$
T<\gamma\le2T,\qquad \beta\ge\tfrac12+\frac1{\log T}.
$$

Put $Z=\lceil Y\log^2T\rceil$. At least one of the following inequalities holds, with an absolute positive $c$:

$$
\left|\sum_{X<n\le Z}a_X(n)n^{-\rho}e^{-n/Y}\right|\ge c,
\tag{1.2}
$$


$$
Y^{1/2-\beta}\int_{\mathbb R}e^{-|v|}
|\zeta(1/2+i(\gamma+v))M_X(1/2+i(\gamma+v))|dv
\ge\frac c{\log T}.
\tag{1.3}
$$

**Proof.** The Gaussian Fourier-inversion proof of the gamma Mellin kernel in lesson eighteen gives

$$
\sum_{n\ge1}a_X(n)n^{-\rho}e^{-n/Y}
=\frac1{2\pi i}\int_{(2)}\zeta(\rho+w)M_X(\rho+w)\Gamma(w)Y^w dw.
$$

Shift to $\Re w=1/2-\beta\in[-1/2,-1/\log T]$. The gamma pole at zero has residue $\zeta(\rho)M_X(\rho)=0$. The pole of zeta contributes $M_X(1)\Gamma(1-\rho)Y^{1-\rho}=O(T^{-100})$, by vertical Stirling and $Y\le T^{3/2}$. There is no other pole between the two lines. The horizontal contours vanish by the same exponential decay, giving the integral (6.6) of lesson eighteen with this $Y$.

The left side starts with $e^{-1/Y}$. Its tail beyond $Z$ is $O(T^{-100})$: $d(n)\le n$ and exponential decay bound it by $C Y^2e^{-Z/(2Y)}$. Uniformly for $-1/2\le u\le-1/\log T$, gamma recurrence and Stirling give

$$
|\Gamma(u+iv)|\le C(\log T)e^{-|v|}.
$$

Near $v=0$ use $\Gamma(z)=\Gamma(z+1)/z$ and $|z|\ge1/\log T$; away from zero the fixed-strip Stirling estimate applies. Thus, if the polynomial is smaller than a fixed $c$, the integral must satisfy (1.3). This proves the alternative with constants independent of $\beta,T,X,Y$. $\square$

The factor $\log T$ records the possible proximity of the gamma line to its pole. We will absorb it in a stated logarithmic exponent, rather than use an estimate uniform through that pole.

## 2. Mean values at the detecting points

**Lemma 2.1 (weighted maximal sampling).** Let $t_j\in[T,2T]$ be one-separated and let $b_n$ be supported on $n\le Z$, where $Z\le T^2$. Then

$$
\sum_j\max_{u\le Z}\left|\sum_{n\le u}b_n n^{-it_j}\right|^2
\ll(\log T)^3\left(T\sum_n|b_n|^2+\sum_n n|b_n|^2\right).
\tag{2.1}
$$


**Proof.** Use disjoint intervals of length $1/2$ about the $t_j$. The fundamental theorem of calculus bounds the sum of sampled squares by $2\|P\|_2^2+2\|P\|_2\|P'\|_2$, exactly as in lesson eighteen, Lemma 6.1. Retain the weighted mean-value error from lesson sixteen instead of replacing every $n$ by $Z$. The mean-square bounds for $P$ and $P'$ are
$C(T\sum|b_n|^2+\sum n|b_n|^2)$ and the same quantity times $\log^2Z$, respectively. This gives one logarithm. Decompose an initial integer interval into at most $O(\log Z)$ binary blocks, use Cauchy–Schwarz, and apply this estimate to all blocks. At each level both weighted coefficient sums partition exactly, so the two additional logarithms prove (2.1). $\square$

We also need the following coefficient bounds, uniformly for $1/2\le\sigma\le1$, $X=\lfloor T\rfloor$ and $T\le Y\le T^{3/2}$:

$$
\begin{aligned}
\sum_{n>X}\frac{d(n)^2e^{-2n/Y}}{n^{2\sigma}}
 &\ll X^{1-2\sigma}\log^4 T,\\
\sum_{n>X}\frac{d(n)^2e^{-2n/Y}}{n^{2\sigma-1}}
 &\ll Y^{2-2\sigma}\log^4 T.
\end{aligned}
\tag{2.2}
$$

Here is a uniform proof, including the endpoints. On a dyadic interval $U<n\le2U$, the proved bound $\sum_{n\le2U}d(n)^2\ll U\log^3(2U)$ bounds the first sum by $C U^{1-2\sigma}\log^3(2U)e^{-2U/Y}$ and the second by $C U^{2-2\sigma}\log^3(2U)e^{-2U/Y}$. There are $O(\log T)$ intervals between $X$ and a constant multiple of $Y$; the first power never exceeds $X^{1-2\sigma}$ and the second never exceeds $C Y^{2-2\sigma}$. Beyond $Y$ the exponential makes the corresponding dyadic sums converge, with an additional polynomial in the dyadic index still dominated by exponential decay. This proves (2.2). The logarithm replacing a geometric denominator is what makes the estimate uniform as $\sigma$ approaches either endpoint.

**Lemma 2.2 (counting the alternatives).** Choose one-separated zeros in $T<\gamma\le2T$, all with $\beta\ge\sigma\ge1/2+1/\log T$. Let $R_1,R_2$ be their counts satisfying (1.2), (1.3), respectively. Then

$$
R_1\ll (\log T)^7
 \left(Y^{2-2\sigma}+T X^{1-2\sigma}\right),
\tag{2.3}
$$


$$
R_2\ll T Y^{(2-4\sigma)/3}(\log T)^5.
\tag{2.4}
$$


**Proof of (2.3).** Use $b_n=a_X(n)e^{-n/Y}n^{-\sigma}$ on $(X,Z]$, zero elsewhere. At a point with $\beta\ge\sigma$, partial summation against $n^{-(\beta-\sigma)}$ bounds the polynomial by its maximum initial partial sum at real part $\sigma$. The total variation plus terminal weight is at most the initial weight, which is at most one. Apply (2.1) and (2.2). Since $Z\le T^2$ for sufficiently large $T$, the stated logarithmic bound follows.

**Proof of (2.4).** Raise (1.3) to the power $4/3$ and use weighted Hölder in $v$. With constants absolute,

$$
1\ll (\log T)^{4/3}Y^{(2-4\sigma)/3}
\int_{\mathbb R}e^{-|v|}|\zeta M_X(1/2+i(\gamma+v))|^{4/3}dv.
\tag{2.5}
$$

Sum over the selected ordinates and apply Hölder to that finite sum:

$$
\sum_j|\zeta M_X(1/2+i(\gamma_j+v))|^{4/3}
\le
\left(\sum_j|\zeta(1/2+i(\gamma_j+v))|^4\right)^{1/3}
\left(\sum_j|M_X(1/2+i(\gamma_j+v))|^2\right)^{2/3}.
\tag{2.6}
$$

For $|v|\le T/4$, the points are still one-separated in $[3T/4,9T/4]$. Corollary 6.2 of lesson sixteen, applied to a fixed number of dyadic intervals, gives
$\sum_j|\zeta(1/2+i(\gamma_j+v))|^4\ll T\log^5T$. Its full proof uses the fourth-moment bound and Cauchy's derivative estimate; no bound for an individual zeta value is being assumed. The sampling proof of Lemma 2.1 without the maximal step gives
$\sum_j|M_X(1/2+i(\gamma_j+v))|^2\ll T\log^2T$, since $\sum_{n\le X}1/n\ll\log T$ and $\sum_{n\le X}n/n=X$.

Insert these estimates in (2.6). Their product is $O(T\log^3T)$. The outside factor in (2.5) raises this to at most $T\log^5T$. For $|v|>T/4$, use $|M_X|\le2\sqrt X$, polynomial growth of zeta, and the exponential weight; there are at most $T+1$ one-separated points, so this contribution is $O(T^{-100})$. This proves (2.4). $\square$

## 3. Ingham's unconditional density bound

**Theorem 3.1 (Ingham).** Uniformly for $T\ge2$ and $1/2\le\sigma\le1$,

$$
N(\sigma,T)\ll
T^{3(1-\sigma)/(2-\sigma)}\log^{16}(2T).
\tag{3.1}
$$

The logarithmic exponent here is an explicit convenient choice; no optimality for it is claimed.

**Proof.** Work first in $T<\gamma\le2T$ at sufficiently large $T$. If $\sigma\le1/2+1/\log T$, the exponent $3(1-\sigma)/(2-\sigma)$ is at least $1-2/\log T$. Thus $T$ is at most a fixed multiple of the claimed power of $T$, and the total zero count $O(T\log T)$ proves the bound.

Otherwise choose a maximal one-separated subset of the zeros with $\beta\ge\sigma$. Its unit neighborhoods cover all these zeros. The local count from lesson eight shows that the full count with multiplicities is at most $C\log T$ times the selected count. Apply Lemma 2.2 with

$$
X=\lfloor T\rfloor,\qquad Y=T^{3/(4-2\sigma)}.
\tag{3.2}
$$

The exponent of $Y$ is between one and $3/2$, so the detector's range is satisfied. Its three terms have sizes

$$
Y^{2-2\sigma}=T^{3(1-\sigma)/(2-\sigma)},\qquad
T Y^{(2-4\sigma)/3}=T^{3(1-\sigma)/(2-\sigma)},
$$

and
$T X^{1-2\sigma}\ll T^{2-2\sigma}\le T^{3(1-\sigma)/(2-\sigma)}$.
Thus the dyadic count is $O(T^{3(1-\sigma)/(2-\sigma)}\log^8T)$, after restoring the local factor. At $\sigma=1$ there are no zeros by the zero-free-line theorem, so this endpoint causes no exceptional case. Summing dyadic height intervals down to a fixed height costs at most one further logarithm, uniformly even when the power approaches zero. Their finite low-height remainder is absorbed. The larger exponent 16 therefore holds uniformly on the closed stated range. $\square$

The exponent can be written $A(\sigma)(1-\sigma)$ with $A(\sigma)=3/(2-\sigma)$. The values are

| $\sigma$ | $A(\sigma)$ | power of $T$ |
|---:|---:|---:|
| $1/2$ | $2$ | $1$ |
| $3/4$ | $12/5$ | $3/5$ |
| $1$ | $3$ | $0$ |

This theorem implies the uniform weaker estimate $N(\sigma,T)\ll T^{3(1-\sigma)}\log^{16}(2T)$. The density hypothesis would replace the factor 3 by $2+\varepsilon/(1-\sigma)$ in the exponent formulation; its usual precise form is $N(\sigma,T)\ll_\varepsilon T^{2(1-\sigma)+\varepsilon}$. It was proved under LH in lesson eighteen, Theorem 6.2, and is not asserted unconditionally here.

## 4. Converting density into short intervals

**Theorem 4.1.** Suppose that fixed $A\ge2$ and $B\ge0$ satisfy

$$
N(\sigma,T)\ll T^{A(1-\sigma)}\log^B(2T)
\qquad(1/2\le\sigma\le1,\ T\ge2)
\tag{4.1}
$$

uniformly. Then, using the proved Vinogradov–Korobov region, for every fixed $\theta>1-1/A$,

$$
\psi(x+h)-\psi(x)\sim h
\qquad(x\to\infty,\ h\ge x^\theta).
\tag{4.2}
$$

In the range $x^\theta\le h\le x$ the asymptotic is uniform in $h$, and
$\pi(x+h)-\pi(x)\sim h/\log x$.

**Proof.** For $h\ge x$, the ordinary PNT already gives (4.2), uniformly: its relative remainder on every argument at least $x$ tends to zero, and $x+h\le2h$. We may therefore assume $\theta<1$ and $x^\theta\le h\le x$. Choose a fixed $\eta>0$ such that

$$
1-\theta+\eta<1/2,\qquad A(1-\theta+\eta)<1,
$$

which is possible because $\theta>1-1/A\ge1/2$. Set $T=x^{1-\theta+\eta}$. The sharp explicit formula of lesson eleven, at $x$ and $x+h$, gives

$$
\psi(x+h)-\psi(x)-h
=-\sum_{|\gamma|<T}\int_x^{x+h}u^{\rho-1}du
 +O\left(\frac{x\log^2x}{T}+\log x\right).
\tag{4.3}
$$

If a contour height must avoid ordinates, take the available height in $[T,2T]$; all subsequent estimates hold with $2T$ in place of $T$. Prime-power half weights cost $O(\log x)$, already displayed. The error divided by $h$ is $O(x^{-\eta}\log^2x)+o(1)$.

Since $0<\beta<1$, each zero term in modulus is at most $h x^{\beta-1}$. The terms with $\beta<1/2$ have total divided by $h$ at most $C T x^{-1/2}\log T=o(1)$ by the total zero count. For the remaining zeros, the positive-weight identity gives

$$
\sum_{\substack{0<\gamma\le T\\\beta\ge1/2}}x^{\beta-1}
=x^{-1/2}N(1/2,T)
 +\log x\int_{1/2}^1x^{u-1}N(u,T)du.
\tag{4.4}
$$

Replacing the count with a strict inequality at its integration boundary changes no integral. Conjugate negative ordinates double the estimate.

The zero-free region gives $N(u,T)=0$ for

$$
u\ge1-\Delta_T,\qquad
\Delta_T\ge c(\log T)^{-2/3}(\log\log T)^{-1/3}.
\tag{4.5}
$$

Enlarge the lower height cutoff if needed; the finite low zeros stay a fixed positive distance from one and can be included by reducing $c$. Let $m=1-A(1-\theta+\eta)>0$. Insert (4.1) into the integral in (4.4) to bound it by

$$
(\log T)^B\log x\int_{1/2}^{1-\Delta_T}
 \left(\frac{T^A}{x}\right)^{1-u}du
\le\frac{(\log T)^B}{m}x^{-m\Delta_T}=o(1).
\tag{4.6}
$$

The last limit follows because $\Delta_T\log x\gg(\log x)^{1/3}/(\log\log x)^{1/3}$, which exceeds every fixed multiple of $\log\log x$. The first term in (4.4) was already $o(1)$. Therefore the entire zero sum in (4.3) is $o(h)$, proving (4.2).

Finally the prime-power comparison gives $\psi(x+h)-\psi(x)-\vartheta(x+h)+\vartheta(x)=O(\sqrt x)$ on $h\le x$. Since $\theta>1/2$, this is $o(h)$. All primes in the interval have $\log p=\log x+O(1)$, so their weighted count is their ordinary count times $\log x(1+O(1/\log x))$. This proves the assertion for $\pi$. $\square$

The hypothesis $A\ge2$ is natural: the total count at $\sigma=1/2$ already has order $T\log T$, which forbids a fixed exponent $A<2$. The shrinking zero-free strip in (4.5) is also essential to this deduction; a density bound alone would leave possible zeros arbitrarily close to one.

**Corollary 4.2.** Ingham's Theorem 3.1 gives $\psi(x+x^\theta)-\psi(x)\sim x^\theta$ for every fixed $\theta>2/3$.

**Proof.** Use $A=3$, $B=16$ in Theorem 4.1. Its threshold is $1-1/3=2/3$. $\square$

**Proposition 4.3 (the $12/5$ consequence).** If (4.1) holds with $A=12/5$ and some fixed $B$, then (4.2) holds for every $\theta>7/12$, and every sufficiently large interval $(n^3,(n+1)^3]$ contains a prime.

**Proof.** The threshold is $1-5/12=7/12$. Choose $7/12<\theta<2/3$. At $x=n^3$ the interval has length $h=3n^2+3n+1\ge3x^{2/3}\ge x^\theta$. Theorem 4.1 gives an ordinary prime count asymptotic to $h/\log x$, which tends to infinity and is positive eventually. The left endpoint $n^3$ is composite for $n\ge2$; if the right endpoint is included, it too is composite. Thus the prime is strictly between the cubes. $\square$

## 5. A large-value inequality with a full proof

The estimate needed beyond Ingham uses the functional equation inside a positive Gram sum. The divisor-weighted coefficient norm is essential: it controls the convolution introduced by the dual series.

**Lemma 5.1.** Suppose $t_1,\ldots,t_R$ lie in an interval of length $T\ge2$ and are one-separated. Let

$$
P(t)=\sum_{N<n\le2N}a_n n^{-it},\quad
G=\sum|a_n|^2,\quad G_2=\sum d(n)|a_n|^2,\quad
\ell=\log(2NT).
$$

Then

$$
\sum_j|P(t_j)|^2\ll
NG\ell+R^{2/3}(NT)^{1/3}G^{2/3}G_2^{1/3}\ell.
\tag{5.1}
$$

The same estimate for the sum of maximum initial partial sums holds with $\ell^3$ instead of $\ell$.

**Proof.** Translating all $t_j$ multiplies the coefficients by unit complex numbers, so take $0\le t_j\le T$. If $N\ge T$, discrete sampling from Lemma 2.1 before its maximal step gives $\sum|P(t_j)|^2\ll NG\ell$, which suffices. Suppose $N<T$. Put $b_j=P(t_j)$ and $B=\sum|b_j|^2$. Dual Cauchy–Schwarz gives

$$
B^2\le G\sum_{N<n\le2N}
 \left|\sum_j\overline{b_j}n^{-it_j}\right|^2.
\tag{5.2}
$$

Use $\omega(u)=\exp(-\log^2u)$. On $1\le u\le2$, $u^{-1/2}\omega(u)$ has a positive lower bound. Therefore the last sum is at most

$$
C\sqrt N\sum_{j,k}|b_jb_k|\,|\Phi_N(t_j-t_k)|,
\qquad
\Phi_N(d)=\sum_{n\ge1}\omega(n/N)n^{-1/2-id}.
\tag{5.3}
$$

To retain the signs before taking absolute values, first expand the nonnegative weighted sum; the triangle inequality then gives (5.3).

The Mellin transform of $\omega$ is $K(w)=\sqrt\pi e^{w^2/4}$: after $u=e^x$, its transform is $\int_{\mathbb R}e^{-x^2+wx}dx$, the Gaussian integral, and imaginary-axis Fourier inversion gives the inverse. The formula for complex $w$ follows from the real Gaussian integral by holomorphic continuation. Hence

$$
\Phi_N(d)=\frac1{2\pi i}\int_{(1)}
 \zeta(1/2+id+w)K(w)N^w dw.
$$

Shift to $\Re w=-1$. Polynomial vertical bounds for zeta and the Gaussian decay of $K$ justify the shift. The single residue is $N^{1/2-id}K(1/2-id)$. Its contribution to (5.3) is at most $CNB$: indeed $|K(1/2-id)|\le C e^{-d^2/4}$, and one-separation gives $\sup_j\sum_k e^{-(t_j-t_k)^2/4}\le C$; use $2|b_jb_k|\le|b_j|^2+|b_k|^2$.

Write $\zeta(s)=\chi(s)\zeta(1-s)$, where the functional equation and the gamma estimates of lessons three and four give

$$
|\chi(1/2+iu)|=1,\qquad
|\chi(-1/2+iu)|\le C(1+|u|).
\tag{5.4}
$$

Let $M=\lceil T/N\rceil$, so $T\le MN\le2T$. On the new line the dual series converges absolutely. Split it at $m=M$. For its finite part move the contour back to $\Re w=0$. No pole is crossed: $K$ is entire and $\chi$ is holomorphic in the strip of real parts $[-1/2,1/2]$. This finite part $I_1(d)$ satisfies

$$
|I_1(d)|\le C\int_{\mathbb R}|K(iv)|
 \left|\sum_{m\le M}m^{-1/2+i(d+v)}\right|dv.
\tag{5.5}
$$

For fixed $k,v$, conjugate the second factor before multiplying it by $P(t_j)$. The product is a polynomial in $(nm)^{-it_j}$, with coefficient

$$
c_q=\sum_{\substack{nm=q\\N<n\le2N\\m\le M}}
 a_n m^{-1/2+it_k-iv}.
$$

Cauchy–Schwarz over the divisors of $q$, followed by $d(nm)\le d(n)d(m)$, gives

$$
\sum_q|c_q|^2
\le G_2\sum_{m\le M}\frac{d(m)}m
\ll G_2\log^2(2M).
\tag{5.6}
$$

The last inequality follows by writing $d(m)=\sum_{ab=m}1$ and bounding two harmonic sums. The product polynomial has length at most $2NM\le4T$. Discrete sampling gives $\sum_j|\sum_qc_q q^{-it_j}|^2\ll TG_2\ell^3$, uniformly in $k,v$. Another Cauchy–Schwarz inequality proves

$$
\sum_j|b_j|\left|\sum_{m\le M}m^{-1/2+i(t_j-t_k+v)}\right|
\ll (RTG_2)^{1/2}\ell^{3/2}.
\tag{5.7}
$$

Since $\sum_k|b_k|\le\sqrt{RB}$ and $\int|K(iv)|dv$ is bounded, (5.5) contributes at most
$CR\sqrt{NTG_2B}\,\ell^{3/2}$ to (5.3).

For the remaining dual series retain $\Re w=-1$. By (5.4), its contribution $I_2(d)$ is bounded by

$$
\frac C N\int_{\mathbb R}(T+|v|+1)|K(-1+iv)|
 \left|\sum_{m>M}m^{-3/2+i(d+v)}\right|dv.
\tag{5.8}
$$

Split the $m$ sum into $U<m\le2U$, $U=2^jM$, $j\ge0$. The product with $P(t_j)$ after conjugating this factor has coefficient norm at most

$$
G_2\sum_{U<m\le2U}\frac{d(m)}{m^3}
\ll G_2 U^{-2}\log(2U).
$$

Its length is at most $4NU$, and $NU\ge T$. Sampling and Cauchy–Schwarz bound the sum of its absolute values over the $R$ points by
$C\sqrt{RNG_2}\,U^{-1/2}\log(2NU)$. Sum the dyadic series: $\sum_{j\ge0}(2^jM)^{-1/2}\log(2^{j+1}NM)\ll M^{-1/2}\log(2NM)$. The Gaussian integral of $(T+|v|+1)|K(-1+iv)|$ is $O(T)$. Since $MN\asymp T$, (5.8) gives

$$
\sum_j|b_j||I_2(t_j-t_k)|\ll\sqrt{RTG_2}\,\ell.
$$

Multiplication by $\sqrt N\sum_k|b_k|$ shows this is no larger than the bound for $I_1$.

Combining these estimates with (5.2) gives

$$
B^2\le C G\left(NB+R\sqrt{NTG_2B}\,\ell^{3/2}\right).
$$

If $B\le2CNG$ the first term in (5.1) suffices. Otherwise absorb $CNG B$ into the left side and divide by $\sqrt B$, obtaining $B\ll R^{2/3}(NT)^{1/3}G^{2/3}G_2^{1/3}\ell$. This proves (5.1).

For maximum initial partial sums, decompose every prefix into disjoint binary blocks. At most $O(\log(2N))$ blocks occur in a prefix, giving that factor by Cauchy–Schwarz. At each binary level the coefficient supports partition, so their $G$ and $G_2$ sums are exactly the original norms. Hölder gives $\sum G_{\rm block}^{2/3}G_{2,\rm block}^{1/3}\le G^{2/3}G_2^{1/3}$. Summing the $O(\log(2N))$ levels gives the other factor. Pad each block with zero coefficients in $(N,2N]$ when applying the already proved estimate. This proves the maximal assertion. $\square$

**Corollary 5.2.** Fix positive integers $l,k$ and a fixed $D\ge0$. Suppose $N\le T^D$, $1/2\le\theta\le1$, and $|a_n|\le d_l(n)n^{-\theta}$ on $(N,2N]$. The number $R$ of one-separated points where a maximum initial partial sum has modulus at least $\log^{-D}(2T)$ satisfies

$$
R\ll_{l,D}\log^{C_{l,D}}(2T)
 \left(N^{2-2\theta}+T N^{4-6\theta}\right).
\tag{5.9}
$$

For values of the full polynomial, applying this to its $k$th power instead gives

$$
R\ll_{l,k,D}\log^{C_{l,k,D}}(2T)
 \left(N^{k(2-2\theta)}+T N^{k(4-6\theta)}\right).
\tag{5.10}
$$

The conclusion remains true when $\beta_j\ge\theta$ replaces $\theta$ in the evaluation at each point.

**Proof.** First, $d_a(n)d_b(n)\le d_{ab}(n)$. At a prime power, map a pair of weak compositions of its exponent into a nonnegative $a$ by $b$ integer matrix with those row and column sums. Such a matrix exists by successively filling the first still nonzero row and column; fix this rule to make the map deterministic. Different pairs have different row or column sums, so the map is injective into all $ab$-part weak compositions. Multiply over primes. Consequently $d_l(n)^2\le d_{l^2}(n)$ and $d(n)d_l(n)^2\le d_{2l^2}(n)$. The repeated harmonic-sum argument gives $\sum_{n\le u}d_r(n)\le u(1+\log u)^{r-1}$ for fixed $r$: choose the first $r-1$ factors and bound the possible last factor by $u$ divided by their product.

It follows that $G,G_2\ll_l N^{1-2\theta}\log^{C_l}(2N)$. Lemma 5.1 gives
$R\ll\log^C(2T)[N^{2-2\theta}+R^{2/3}T^{1/3}N^{(4-6\theta)/3}]$ after dividing by the square of the stated threshold. If the first term does not suffice, absorb it and cube; this proves (5.9).

The $k$th power has coefficients bounded by $d_{lk}(n)n^{-\theta}$, by ordered divisor convolution. Its support is $(N^k,(2N)^k]$, a union of at most $k+1$ intervals $(U,2U]$ with $U\asymp_k N^k$. A large full value gives a large value on one of these pieces; apply (5.9) to each, adjusting the logarithmic threshold and constant. Finally a value at $\beta_j\ge\theta$ is bounded by the maximum partial sum at $\theta$, by partial summation against $n^{-(\beta_j-\theta)}$. For (5.10), first take the full polynomial's $k$th power at $\beta_j$ and then apply this partial-sum bound to each dyadic piece. All constant powers of two and threshold losses depend only on the displayed fixed parameters. $\square$

## 6. Balanced smoothing and Huxley's bound

The detector in section one has length at least $T$. A different smoothing kernel makes both halves of the functional equation have length $\sqrt T$ times powers of a logarithm. We supply its analytic bounds before using it.

**Lemma 6.1 (a smoothing kernel with only one pole).** Define

$$
\varpi=\int_0^\infty e^{-u-u^{-1}}\frac{du}{u},\qquad
f(x)=\frac1\varpi\int_x^\infty e^{-u-u^{-1}}\frac{du}{u},\qquad
g(w)=\frac1{\varpi w}\int_0^\infty u^{-w}e^{-u-u^{-1}}\frac{du}{u}.
\tag{6.1}
$$

The integral in $g$ is entire, and $g$ has just the simple pole at zero, of residue one. For $x>0$, $f(x)+f(1/x)=1$; for $x\ge1$,

$$
0\le f(x)\le C x^{-1}e^{-x}.
\tag{6.2}
$$

There is an absolute $C\ge1$ such that, with $w=u+iv$,

$$
|wg(w)|\le [C(1+|w|)]^{\max(1,|u|)}e^{-\pi|v|/2}.
\tag{6.3}
$$

For $c>0$ and $V>0$,

$$
\frac1{2\pi i}\int_{(c)}g(w)V^w dw=f(1/V).
\tag{6.4}
$$


**Proof.** Both ends of the defining integral decay faster than every fixed power, locally uniformly in $w$. This proves entire dependence and the residue assertion. The substitution $u\mapsto1/u$ proves the symmetry of its numerator and the identity for $f$. Bounding $u^{-1}$ by $x^{-1}$ in the defining tail proves (6.2).

For (6.3) use that symmetry to write
$\varpi wg(w)=\int_{\mathbb R}\exp(wx-e^x-e^{-x})dx$. By conjugation take $v\ge0$. Set $\delta=(1+|u|)/(2+|w|)$, so $0<\delta<1$, and move the $x$ contour to height $\pi/2-\delta$. On its vertical ends the modulus is bounded by $C_w\exp(|u|R-e^R\sin\delta)$, which tends to zero. Taking absolute values on the shifted line gives

$$
|\varpi wg(w)|\le
2e^{-\pi v/2+v\delta}\int_1^\infty t^{|u|-1}e^{-t\sin\delta}dt.
$$

If $|u|\le1$, the integral is at most $1/\sin\delta$, and $v\delta\le2$ gives the bound $C(1+|w|)e^{-\pi v/2}$. If $|u|\ge1$, the integral is at most $(\sin\delta)^{-|u|}\Gamma(|u|)$. Stirling, $\sin\delta\ge c\delta$, $v\delta\le1+|u|$, and $|u|/\delta\le2+|w|$ give (6.3). These constants are absolute, including the bounded transition range.

To justify inversion without interchanging a nonabsolute Perron integral, put $F(V)=f(1/V)$. For $\Re w>0$, integration by parts gives

$$
\int_0^\infty F(V)V^{-w-1}dV
=\frac1{\varpi w}\int_0^\infty V^{-w-1}e^{-V-V^{-1}}dV
=g(w).
$$

All boundary terms vanish. Thus $g(c+iv)$ is the Fourier transform, with kernel $e^{-ivx}$, of the integrable continuous function $e^{-cx}F(e^x)$. Insert a Gaussian multiplier $e^{-\epsilon v^2}$ in Fourier inversion. The Gaussian integral turns the inverse into convolution with the Gaussian approximate identity, which tends to this continuous function as $\epsilon\downarrow0$. Equation (6.3) supplies an integrable dominating function for the inverse side, so dominated convergence removes the multiplier. Multiplying back by $V^c$ proves (6.4). $\square$

**Lemma 6.2 (the balanced detector).** Fix $0<\eta<1/4$. There are absolute constants $C,C_0$ such that the following construction works for all sufficiently large $T$ (depending on $\eta$). Set

$$
P=C(T+2),\quad Y=P^{1/2}\log^2P,\quad
U=\left\lceil C_0 P^{1/2}\log^3P\right\rceil,\quad
K=\lfloor P^{\eta/5}\rfloor.
\tag{6.5}
$$

If $\rho=\beta+i\gamma$ is a zero with $T<\gamma\le2T$ and $\beta\ge\theta\ge7/10$, then

$$
1\le C\left(
\left|\sum_{K<n\le KU}a(n)n^{-\rho}\right|
+\int_{\mathbb R}e^{-|v|}
 \left|\sum_{K<n\le KU}b(n;v)n^{-\rho}\right|dv
\right),
\tag{6.6}
$$

where the coefficients are independent of $\beta,\gamma$ and satisfy

$$
|a(n)|\le d(n),\qquad
|b(n;v)|\le C\sqrt{\log P}\,d(n).
\tag{6.7}
$$

They may depend on $P,K,\theta$ and, in the second case, $v$.

**Proof.** Mellin inversion and absolute convergence first give, for $s=\beta+i\gamma$,

$$
\sum_{m\ge1}f(m/Y)m^{-s}
=\frac1{2\pi i}\int_{(2)}\zeta(s+w)Y^w g(w)dw.
$$

Shift to $\Re w=-1$. The residues are $\zeta(s)$ and $Y^{1-s}g(1-s)$. The exponential decay in (6.3), together with polynomial vertical bounds, makes the horizontal integrals tend to zero. On the new line apply the functional equation and expand the absolutely convergent dual series. With

$$
h(V;s)=\frac1{2\pi i}\int_{(-1)}\chi(s+w)V^w g(w)dw,
$$

the result is

$$
\sum_{m\ge1}f(m/Y)m^{-s}
=\zeta(s)+Y^{1-s}g(1-s)+\sum_{m\ge1}m^{s-1}h(mY;s).
\tag{6.8}
$$


Here is a bound that permits a finite dual sum. For every real $\lambda\ge3$, move the contour in $h$ to $\Re w=-\lambda$; no singularity is crossed. Uniform Stirling in the right half-plane, applied to
$\chi(z)=2^z\pi^{z-1}\sin(\pi z/2)\Gamma(1-z)$, gives

$$
|\chi(\beta-\lambda+i(\gamma+v))|
\le C(3+2T+\lambda+|v|)^{\lambda+1/2-\beta}.
$$

To see why there is no exponential growth left over, write $1-z=x+iy$, $x\ge1$. The exponential part after the sine factor is at most
$\exp[-x+|y|\arctan(x/|y|)]\le1$; the value at $y=0$ is obtained by continuity. The usual uniform Stirling remainder is bounded on this half-plane. Since $\beta\ge1/2$, (6.3) consequently bounds the integrand by
$C(P/V)^\lambda(\lambda+|v|)^{2\lambda}e^{-\pi|v|/2}$ after enlarging the absolute constant in $P$. Its integral is at most $C(P/V)^\lambda\lambda^{5\lambda}$. Indeed $(\lambda+v)^{2\lambda}\le2^{2\lambda}(\lambda^{2\lambda}+v^{2\lambda})$, and the gamma integral and Stirling give a bound $(C\lambda)^{2\lambda}$; its constant power is absorbed in $P^\lambda$.

For $V/P\ge(3e)^5$, choose the real value $\lambda=e^{-1}(V/P)^{1/5}\ge3$. The resulting estimate is

$$
|h(V;s)|\le C\exp\left[-\frac5e(V/P)^{1/5}\right].
\tag{6.9}
$$

The minus sign follows by substituting this $\lambda$ into
$5\lambda\log\lambda-\lambda\log(V/P)=-5\lambda$.
Choose $C_0$ so large that $(5/e)C_0^{1/5}\ge200$ and $C_0\ge300$. For $m\ge U$, the function
$q(m)=(5/e)(mY/P)^{1/5}-2\log m$ is increasing once $T$ is large, and $q(U)\ge100\log P$. Therefore the tail of the dual sum in (6.8) is $O(P^{-100})$, by $m^{\beta-1}\le1$ and comparison with $P^{-100}\sum m^{-2}$. Equation (6.2) gives the same bound for the main tail beyond $U$; here $U/Y\ge C_0\log P$. The pole term is $O(P^{-100})$ by (6.3) and $\gamma>T$.

For the retained finite dual sum, move its contour to

$$
u=\theta+1/2-2\beta\in[-4/5,-1/5].
$$

There is no pole between these negative lines. On this new contour,
$\Re(s+w)=\theta+1/2-\beta\in[1/5,1/2]$. The fixed-strip gamma estimates give
$|\chi(s+w)g(w)|\le C P^{\beta-\theta}e^{-|v|}$; powers of $1+|v|$ are absorbed by the remaining exponential decay. Thus the retained dual term is at most

$$
C Y^{\theta+1/2-2\beta}P^{\beta-\theta}
\int_{\mathbb R}e^{-|v|}
 \left|\sum_{m\le U}m^{\theta-1/2-\beta+i(\gamma+v)}\right|dv.
\tag{6.10}
$$

Since $Y^2\ge P$, the outside factor is at most $C Y^{1/2-\theta}$.

Multiply the finite identity by $M_K(s)=\sum_{d\le K}\mu(d)d^{-s}$ and set $s=\rho$. In its main sum the coefficient of $n^{-s}$ is

$$
a(n)=\sum_{\substack{dm=n\\d\le K,\ m\le U}}\mu(d)f(m/Y).
$$

For $n\le K$, $f(m/Y)=1+O((K/Y)e^{-Y/K})$, so Möbius inversion makes these terms equal to $1+o(1)$ in total, uniformly in $\beta$. Terms with $n>K$ have $|a(n)|\le d(n)$, because $0\le f\le1$.

In (6.10) take the complex conjugate of the finite $m$ sum before multiplying it by $M_K(s)$; its modulus is unchanged. The product then has frequency $(dm)^{-i\gamma}$, and its coefficient after factoring out $n^{-\beta}$ is $\sum_{dm=n}\mu(d)m^{\theta-1/2-iv}$. Put $r=\theta-1/2$. Normalize this coefficient by $U^r$. The remaining outside factor is at most
$C(U/Y)^r\le C\sqrt{\log P}$. Absorb it by defining

$$
b(n;v)=C_1\sqrt{\log P}
\sum_{\substack{dm=n\\d\le K,\ m\le U}}
 \mu(d)(m/U)^r m^{-iv},
$$

with one sufficiently large fixed $C_1$. This proves (6.7). The small terms $n\le K$, before this harmless enlargement, contribute at most
$C Y^{-r}\sqrt K\log(2K)=o(1)$: directly sum
$\sum_{d\le K}d^{-\beta}\sum_{m\le K/d}m^{\theta-1/2-\beta}\le C\sqrt K\log(2K)$, and use $r\ge1/5$, $K\le P^{\eta/5}$. After the enlargement the bound is $C\sqrt{\log P}\,U^{-r}\sqrt K\log(2K)\ll P^{-1/10+\eta/10}\log^2P=o(1)$. All $O(P^{-100})$ remainders remain negligible when multiplied by $|M_K(s)|\le K$. At a zero $\zeta(\rho)M_K(\rho)=0$, so the unit term must be supplied by one of the two remaining tails. Absorbing the small errors proves (6.6). $\square$

**Theorem 6.3 (Huxley's estimate).** For every fixed $0<\eta<1/4$, uniformly for $3/4\le\sigma\le1$ and $T\ge2$,

$$
N(\sigma,T)\ll_\eta
\log^{C_\eta}(2T)\left(
T^{(2+\eta)(1-\sigma)}
+T^{3(1-\sigma)/(3\sigma-1)}
\right).
\tag{6.11}
$$

Consequently an absolute fixed $B$ exists such that

$$
N(\sigma,T)\ll T^{(12/5)(1-\sigma)}\log^B(2T)
\qquad(1/2\le\sigma\le1,\ T\ge2).
\tag{6.12}
$$


**Proof.** Fix $\theta=\sigma\ge3/4$ and first count a maximal one-separated set of zeros in $T<\gamma\le2T$. Use Lemma 6.2. Divide $(K,KU]$ into $O(\log T)$ dyadic intervals $(N,2N]$, truncating the last interval. Assign each selected zero to one interval for which the corresponding main value plus the weighted dual integral in (6.6) is at least $c/\log T$. Let $R_N$ be the assigned count.

For any fixed positive integer $k$, weighted Hölder and
$(a+b)^{2k}\le2^{2k-1}(a^{2k}+b^{2k})$ give

$$
R_N\ll_k\log^{2k}(2T)\left(
\sum_j|A_j|^{2k}
+\int_{\mathbb R}e^{-|v|}\sum_j|B_j(v)|^{2k}dv
\right),
\tag{6.13}
$$

where the sum is over these assigned zeros and $A_j,B_j(v)$ are the full polynomials on this block, evaluated at $\beta_j+i\gamma_j$. This step keeps the integral intact; there is no claim that a single value of $v$ works for every zero.

Take the $k$th power of each polynomial. Its coefficients are bounded, up to a fixed power of $\log T$, by $d_{2k}(n)n^{-\theta}$, using (6.7) and divisor convolution. Split its support $(N^k,(2N)^k]$ into at most $k+1$ dyadic blocks, and use partial summation for $\beta_j\ge\theta$. The maximal form of Lemma 5.1 and the coefficient-norm calculation in Corollary 5.2 then give, uniformly in $v$,

$$
R_N\ll_k\log^{C_k}(2T)
\left(N^{k(2-2\theta)}
+R_N^{2/3}T^{1/3}N^{k(4/3-2\theta)}\right).
$$

The integral of $e^{-|v|}$ is finite, so it contributes only another constant. Absorbing the first term when necessary and cubing gives

$$
R_N\ll_k\log^{C'_k}(2T)
\left(N^{k(2-2\theta)}+T N^{k(4-6\theta)}\right).
\tag{6.14}
$$

If $N\le T^{1/[2(3\theta-1)]}$, choose the least $k$ such that $N^k\ge T^{1/(3\theta-1)}$. Then

$$
T^{1/(3\theta-1)}\le N^k\le T^{3/[2(3\theta-1)]}.
$$

Also $N\ge K\gg T^{\eta/5}$, so $k$ belongs to a finite set depending only on $\eta$. Since $2-2\theta\ge0$ and $4-6\theta<0$, both terms in (6.14) are at most $T^{3(1-\theta)/(3\theta-1)}$.

If $N>T^{1/[2(3\theta-1)]}$, take $k=2$. For sufficiently large $T$,
$N\le KU\le P^{1/2+\eta/4}$. The first term is at most $C_\eta T^{(2+\eta)(1-\theta)}$. The second is at most

$$
T\left(T^{1/[2(3\theta-1)]}\right)^{8-12\theta}
=T^{3(1-\theta)/(3\theta-1)}.
$$

Sum the $O(\log T)$ blocks. The local zero-count bound restores multiplicities and the discarded nearby zeros at a cost $O(\log T)$; a dyadic sum over heights costs at most one more logarithm. Finite low heights are absorbed uniformly, as in Theorem 3.1. This proves (6.11), with some fixed $C_\eta$ and without an unmentioned power loss in $T$.

For (6.12) fix $\eta=1/5$. On $1/2\le\sigma\le3/4$, Ingham gives $3/(2-\sigma)\le12/5$. On $3/4\le\sigma\le1$, the second factor in (6.11) has $3/(3\sigma-1)\le12/5$, while $2+\eta=11/5<12/5$. Taking the larger fixed logarithmic exponent proves the uniform estimate (6.12). $\square$

**Corollary 6.4.** For every fixed $\theta>7/12$,
$\psi(x+x^\theta)-\psi(x)\sim x^\theta$. Every sufficiently large integer $n$ has a prime strictly between $n^3$ and $(n+1)^3$.

**Proof.** Equation (6.12) supplies the actual unconditional hypothesis $A=12/5$ of Theorem 4.1 and Proposition 4.3. Their deductions now apply without an additional density assumption. $\square$

## 7. Ingham's earlier estimate and the historical $5/8$

Theorem 3.1 and the following theorem are different density estimates. The earlier one exploits a bound for each critical-line value, rather than the fourth moment.

**Theorem 7.1.** Suppose that fixed $c,D\ge0$ satisfy

$$
|\zeta(1/2+it)|\ll (|t|+2)^c\log^D(|t|+2).
\tag{7.1}
$$

Then, uniformly for $1/2\le\sigma\le1$ and $T\ge2$,

$$
N(\sigma,T)\ll_{c,D}
T^{\,2(1+2c)(1-\sigma)}\log^{16+2D}(2T).
\tag{7.2}
$$

**Proof.** If $c\ge1/4$, Ingham's unconditional theorem already suffices, since its exponent is at most $3(1-\sigma)\le2(1+2c)(1-\sigma)$. Suppose $0\le c<1/4$. In the detector of Lemma 1.1 take

$$
X=\lfloor T\rfloor,\qquad Y=T^{1+2c}\in[T,T^{3/2}].
$$

At $\sigma\le1/2+1/\log T$, the total zero count $O(T\log T)$ proves (7.2), since the displayed exponent is at least $1-C_c/\log T$. Otherwise select one-separated zeros as before. The polynomial alternative still has

$$
R_1\ll\log^7T\left(Y^{2-2\sigma}+T^{2-2\sigma}\right).
$$

For the integral alternative, square (1.3) and apply weighted Cauchy–Schwarz instead of the $4/3$ power:

$$
R_2\ll Y^{1-2\sigma}\log^2T
\int_{\mathbb R}e^{-|v|}
 \sum_j|\zeta(1/2+i(\gamma_j+v))M_X(1/2+i(\gamma_j+v))|^2dv.
$$

When $|v|\le T/4$, (7.1) and discrete polynomial sampling bound the sum by
$C T^{1+2c}\log^{2D+2}T$. For the remaining $v$, use polynomial growth and the exponential weight exactly as in Lemma 2.2; the contribution is smaller than every fixed negative power of $T$. Therefore

$$
R_2\ll T^{1+2c}Y^{1-2\sigma}\log^{4+2D}T.
$$

With the stated $Y$, both $Y^{2-2\sigma}$ and $T^{1+2c}Y^{1-2\sigma}$ equal $T^{2(1+2c)(1-\sigma)}$, and the other polynomial term is smaller. Restoring local multiplicity and summing dyadic heights costs at most two logarithms. The exponent $16+2D$ covers all these losses uniformly. The zero-free line handles $\sigma=1$, and bounded heights are absorbed. $\square$

**Corollary 7.2.** For every fixed $\theta>5/8$, $\psi(x+x^\theta)-\psi(x)\sim x^\theta$.

**Proof.** Weyl's estimate in Exponential sums, Theorem 4.1, is $|\zeta(1/2+it)|\ll (|t|+4)^{1/6}\log(|t|+4)$. Thus Theorem 7.1 applies with $c=1/6,D=1$, giving $A=2(1+1/3)=8/3$ and a fixed logarithmic factor. Theorem 4.1 now has threshold $1-3/8=5/8$. $\square$

The logarithm in Weyl's estimate has been retained in this argument. There is no need to assert the stronger pointwise bound $O(t^{1/6})$. The later unconditional $7/12$ result is sharper, while the $5/8$ deduction explains the historical use of a subconvex value estimate.

## 8. Almost all very short intervals under RH

An assertion for almost all starting points allows a sparse set of exceptions. It is substantially stronger than the prime-counting formula at every point with a fixed power length. Under RH, an elementary mean-square estimate for the zero sum already reaches lengths just larger than $\log^2x$.

**Lemma 8.1 (sampling the zero frequencies).** Let the zeros with $|\gamma|<T$ be listed with multiplicities, $T\ge2$. For any coefficients $a_\gamma$ and any real interval $I$ of length at most two,

$$
\int_I\left|\sum_{|\gamma|<T}a_\gamma e^{i\gamma u}\right|^2du
\le C\log(2T)\sum_{|\gamma|<T}|a_\gamma|^2.
\tag{8.1}
$$

This does not require RH.

**Proof.** If $u_0$ is the center of $I$, the Gaussian $\phi(u)=e^{1-(u-u_0)^2}$ is at least one on $I$. Expand the square in the integral with this weight. The Gaussian Fourier integral bounds it by

$$
e\sqrt\pi\sum_{\gamma,\gamma'}
 |a_\gamma a_{\gamma'}|e^{-(\gamma-\gamma')^2/4}.
$$

The unit-window zero count from lesson eight is $O(\log(2T))$ for all ordinates in this truncated set, including repetitions. Dividing the real line into unit intervals about each $\gamma$ therefore gives
$\sup_\gamma\sum_{\gamma'}e^{-(\gamma-\gamma')^2/4}\le C\log(2T)$. Apply $2|a_\gamma a_{\gamma'}|\le|a_\gamma|^2+|a_{\gamma'}|^2$ and sum. This proves (8.1) without separating coincident or nearby zeros. $\square$

**Theorem 8.2 (Selberg's mean-square estimate in a sufficient form).** Under RH, for $X\ge4$ and $1\le h\le X/2$,

$$
\int_X^{2X}|\psi(x+h)-\psi(x)-h|^2dx
\ll Xh\log^2(2X)+X\log^4(2X).
\tag{8.2}
$$

The same bound holds for the sum over integer $x\in[X,2X]$.

**Proof.** Use the sharp explicit formula of lesson eleven at one common admissible height $T\in[X,2X]$. Its remainders at $x$ and $x+h$ are $O(\log^2(2X))$, uniformly in this range; the half-weight corrections cost only $O(\log(2X))$. On RH its zero contribution to the difference is

$$
S(x)=\sum_{|\gamma|<T}
\frac{(x+h)^{1/2+i\gamma}-x^{1/2+i\gamma}}{1/2+i\gamma}.
\tag{8.3}
$$

It suffices to bound $\int_X^{2X}|S(x)|^2dx\ll Xh\log^2(2X)$, since the squared remainder contributes $O(X\log^4(2X))$.

Put $V=X/h\ge2$ and split (8.3) at $|\gamma|=V$. In the lower part use the exact integral

$$
S_{\rm low}(x)=\int_0^h(x+r)^{-1/2}
 \sum_{\substack{|\gamma|<T\\|\gamma|\le V}}
 e^{i\gamma\log(x+r)}dr.
$$

Cauchy–Schwarz in $r$ gives

$$
\int_X^{2X}|S_{\rm low}(x)|^2dx
\le h\int_0^h\int_{X+r}^{2X+r}
\left|\sum_{|\gamma|\le\min(V,T)}e^{i\gamma\log u}\right|^2\frac{du}{u}\,dr.
$$

After $u=e^v$, each inner interval has length at most $\log2$. Lemma 8.1 and the total zero count $N(V)\ll V\log(2V)$ give the bound
$C h^2 V\log^2(2X)=C Xh\log^2(2X)$.

For the upper part separate the two endpoint sums. For either endpoint $u=x$ or $u=x+h$, substitution $u=e^v$ and $u\le3X$ bound its mean square by

$$
C X^2\int_J
\left|\sum_{V<|\gamma|<T}
\frac{e^{i\gamma v}}{1/2+i\gamma}\right|^2dv
\le C X^2\log(2X)\sum_{V<|\gamma|<T}\frac1{\gamma^2},
$$

where $J$ has length less than two. A dyadic sum using $N(u)\ll u\log(2u)$ gives $\sum_{|\gamma|>V}\gamma^{-2}\ll\log(2V)/V$. Thus this is also $O(Xh\log^2(2X))$. The triangle-square inequality combines the two frequency ranges and endpoints, proving (8.2).

For integers, compare an integer $m$ with real $x\in[m,m+1]$. Each of the two endpoints moves by at most one, so its $\psi$ value changes by at most $C\log(2X)$: there are at most two integers in an interval of length one and each has von Mangoldt weight at most $\log(3X+2)$. Hence the square at $m$ is bounded by twice the square at $x$ plus $C\log^2(2X)$. Integrating over these unit intervals proves the discrete version, using (8.2) on the slightly enlarged range; the same zero-sum proof is uniform on that range. $\square$

**Theorem 8.3 (Selberg).** Assume RH. For every fixed $\epsilon,\delta>0$, all but $o(X)$ integers $x\in[2,X]$ satisfy

$$
(1-\epsilon)\frac{(\log x)^{2+\delta}}{\log x}
\le\pi\bigl(x+(\log x)^{2+\delta}\bigr)-\pi(x)
\le(1+\epsilon)\frac{(\log x)^{2+\delta}}{\log x}.
\tag{8.4}
$$


**Proof.** Work first on a dyadic range $X\le x\le2X$. Let
$h_-=(\log X)^{2+\delta}$ and $h_+=(\log(2X))^{2+\delta}$; both lie below $X/2$ for large $X$. Equation (8.2) and Chebyshev's inequality show that, for either fixed height, the number of integers where
$|\psi(x+h_\pm)-\psi(x)-h_\pm|>\epsilon h_\pm/20$
is at most

$$
C_{\epsilon,\delta}X\left((\log X)^{-\delta}
+(\log X)^{-2\delta}\right)=o(X).
\tag{8.5}
$$


Prime powers also have to be removed in mean, since a pointwise $O(\sqrt X)$ error would be too large here. The total von Mangoldt weight of proper prime powers up to $3X$ is $O(\sqrt X)$: Chebyshev bounds the square contribution, and powers of order at least three contribute $O(X^{1/3}\log X)=O(\sqrt X)$. Each such integer lies in at most $h_\pm+2$ of the integer-starting intervals. Therefore the sum, over these starting points, of the prime-power error is $O(h_\pm\sqrt X)$. Markov's inequality shows that it exceeds $\epsilon h_\pm/20$ at only $O_\epsilon(\sqrt X)=o(X)$ points.

Outside the union of these exceptional sets, the two prime-weight sums
$\vartheta(x+h_\pm)-\vartheta(x)$ are $(1+O(\epsilon/10))h_\pm$. Moreover
$h_+/h_-=1+O_\delta(1/\log X)$, and
$h_-\le(\log x)^{2+\delta}\le h_+$. Monotonicity squeezes the prime-weight sum at the varying target length between these two estimates. For sufficiently large $X$, it equals $(1+O(\epsilon/4))(\log x)^{2+\delta}$. In each such interval every prime has $\log p=\log x+o(1)$, uniformly, so dividing by $\log x$ gives (8.4), after starting with a smaller fixed error parameter if necessary.

Finally sum dyadic ranges up to the requested endpoint. The ranges below its square root contain $O(\sqrt X)$ integers. In all remaining ranges the relative upper bound in (8.5) tends uniformly to zero, and their total lengths are $O(X)$. The extra prime-power exceptional sets also sum to $o(X)$. This proves the stated count on $[2,X]$. $\square$

Almost-all is a statement about the density of the exceptional starting points, not a pointwise formula. It allows infinitely many exceptional intervals. We return to those intervals after developing the modern density estimate.

## 9. Polynomials on a difference set

The modern argument uses both large values and the additive structure of the points where they occur. The following estimate of Heath-Brown supplies its classical input. We give the supporting proof here, using the functional equation already established in the course.

**Theorem 9.1 (Heath-Brown's difference-set estimate).** Let $W$ be a one-separated set in an interval of length $T\ge3$, let $R=|W|$, let $N\ge1$, and let $|a_n|\le1$. For every $\epsilon>0$,

$$
\sum_{t,u\in W}\left|\sum_{N<n\le2N}a_n n^{i(t-u)}\right|^2
\ll_\epsilon T^\epsilon
\left(RN^2+R^2N+R^{5/4}T^{1/2}N\right).
\tag{9.1}
$$

The same statement, with a factor $T^{o(1)}$, holds for coefficients bounded by $T^{o(1)}$ and polynomially bounded $N$.

**Proof.** The empty set is immediate. Translating $W$ does not change its differences. If $N\ge T$, apply the mean-value theorem to the polynomial and its derivative after multiplying by $N^{-it}$. Its derivative coefficients are $i\log(n/N)a_n$, bounded by $\log2$ times the original majorant. Integrating the fundamental-theorem-of-calculus bound on disjoint quarter-length intervals about the sample points therefore gives $C(T+N)\sum|a_n|^2$ for each fixed $u$. Summing over $u$ gives $O(RN^2)$, proving this case even for arbitrarily large $N$. We can henceforth suppose $1\le N\le T$.

Put

$$
S(V)=\sum_{t,u\in W}
\left|\sum_{V<n\le2V}n^{-1/2+i(t-u)}\right|^2.
\tag{9.2}
$$

Here and throughout the proof, $V$ and other polynomial lengths can be real. Expanding the square gives the positive identity

$$
\sum_{t,u\in W}\left|\sum_n c_n n^{i(t-u)}\right|^2
=\sum_{m,n}c_m\overline{c_n}
\left|\sum_{t\in W}(m/n)^{it}\right|^2.
\tag{9.3}
$$

Consequently the expression on the left is bounded above if each coefficient is replaced by a nonnegative majorant of its absolute value. In particular $S(V/k)\le kS(V)$ for positive integers $k$, by embedding $n$ as $kn$.

We first establish a transfer bound. For $1\le V\le P/4$ and $P\le T^C$, with fixed $C$,

$$
S(V)\ll_C(\log(2T))^3 S(P).
\tag{9.4}
$$

Let $J=P/(2V)\ge2$, and multiply the polynomial in (9.2) by
$\sum_{J<p\le2J}p^{-1/2+i(t-u)}e(\alpha p)$, where $e(x)=e^{2\pi ix}$. Integrating its squared absolute value over $0\le\alpha\le1$ gives $S(V)\sum_{J<p\le2J}p^{-1}$. The product polynomial has coefficients

$$
c_\ell(\alpha)=\sum_{\substack{pn=\ell\\J<p\le2J\\V<n\le2V}}e(\alpha p),
\qquad P/2<\ell\le2P.
$$

They are bounded by the number of distinct prime divisors of $\ell$, hence by $C\log(2P)$. Apply (9.3), split this last interval into its two dyadic parts, and use $S(P/2)\le2S(P)$. For sufficiently large $J$, the prime number theorem in lesson nine gives $\sum_{J<p\le2J}p^{-1}\gg1/\log(2J)$. If $J$ is bounded, let $k=\lfloor P/V\rfloor$. It is a bounded positive integer, and $P/2\le kV\le P$. Embedding $n$ as $kn$ puts the block inside $(P/2,2P]$; (9.3) bounds its moment by $2k(S(P/2)+S(P))\ll S(P)$. Thus no assertion about primes in a small interval is needed. This proves (9.4). The same argument works for coefficients bounded by a fixed majorant; in particular it transfers any dyadic block with coefficients at most $B n^{-1/2}$ at a cost $B^2$.

We will use the elementary uniform bound $d(n)\ll_\eta n^\eta$, for any fixed $\eta>0$. To see it, write $d(n)=\prod_{p^\nu\parallel n}(\nu+1)$. For all sufficiently large primes, $\nu+1\le p^{\eta\nu/2}$. For each of the finitely many remaining primes, $(\nu+1)p^{-\eta\nu}$ is bounded as $\nu$ varies; multiply these finitely many bounds. Replacing $\eta$ by a smaller number proves the stated estimate.

Fix a small $\eta>0$, and put $T_0=T^{1+\eta}$. Two further inequalities, for lengths bounded by any fixed power of $T$, are

$$
S(V)\ll_\eta T^\eta\left(RV+S(T_0/V)\right),
\tag{9.5}
$$

when $T_0/V\ge1$, with the second term absent otherwise, and

$$
S(V)^2\ll_\eta T^\eta R^2 S(P)
\quad\hbox{if }P\ge8V^2.
\tag{9.6}
$$

The powers $T^\eta$ in these formulas can each be made arbitrarily small; increasing their numerical multiples below does not fix a new restriction on $\epsilon$.

Here are the analytic details of (9.5). Choose a nonnegative smooth function $\omega$, supported in $[1/2,3]$, that is at least one on $[1,2]$. By (9.3),

$$
S(V)\le \frac{2}{V}\sum_{t,u\in W}|A_V(t-u)|^2,
\qquad A_V(d)=\sum_n\omega(n/V)n^{id}.
$$

There are $O(RT^{\eta/4})$ ordered pairs with $|t-u|\le T^{\eta/4}$, since $W$ is one-separated. Their contribution is $O(RVT^{\eta/4})$.

For the remaining pairs let $H(s)=\int_0^\infty\omega(x)x^{s-1}dx$. It is entire and decays faster than every inverse power of $|\Im s|$ on each fixed vertical strip, by integration by parts after $x=e^v$. Mellin inversion, justified by the Gaussian Fourier inversion used in Lemma 6.1, gives

$$
A_V(d)=\frac1{2\pi i}\int_{(2)}
\zeta(s-id)V^sH(s)\,ds.
$$

Shift to $\Re s=-J$, for a sufficiently large fixed integer $J$. The only residue is $V^{1+id}H(1+id)$, which is $O(T^{-A})$ for $|d|>T^{\eta/4}$, for any desired fixed $A$, by choosing enough integrations by parts. Apply the functional equation on the new line, and truncate the absolutely convergent series for $\zeta(1-s+id)$ at $M=T_0/V$. Its tail has total contribution

$$
O_J\!\left(T^{1/2}\left(\frac{T}{VM}\right)^J\right)
=O_J(T^{1/2-\eta J}).
$$

This estimate follows directly from $\sum_{m>M}m^{-1-J}\ll M^{-J}$ and
$|\chi(-J+i(v-d))|\ll_J(1+|v-d|)^{J+1/2}$; the rapid decay of $H$ integrates the factors in $v$. Taking $J$ large makes the error $O(T^{-A})$. If $M<1$, truncate at zero instead and the same estimate applies. Move the finite-series integral to $\Re s=1/2$. No pole is crossed, since $\chi(s-id)$ is holomorphic for $\Re s\le1/2$. On this line $|\chi(s-id)|=1$. We obtain

$$
|A_V(d)|\le C\sqrt V
\int_{\mathbb R}|H(1/2+iv)|
\left|\sum_{m\le M}m^{-1/2+i(d-v)}\right|dv+O(T^{-A}).
$$

Cauchy–Schwarz in $v$, followed by (9.3), bounds the sum of its squares over all pairs by a constant times
$V\sum_{t,u}|\sum_{m\le M}m^{-1/2+i(t-u)}|^2$. Split at $M,M/2,\ldots$. The first block has moment $S(M/2)\le2S(M)$; all subsequent blocks with length at least one transfer directly to $M$ using (9.4). The final bounded-length remainder has moment $O(R^2)$, which is also $O(S(M))$: the diagonal terms $m=n$ in (9.3) give $S(M)\ge R^2\sum_{M<n\le2M}n^{-1}\ge cR^2$ for $M\ge1$. All losses are powers of $\log(2T)$. This proves (9.5), with arbitrarily small power losses.

For (9.6), Cauchy–Schwarz over the $R^2$ pairs gives

$$
S(V)^2\le R^2\sum_{t,u}
\left|\sum_{V<n\le2V}n^{-1/2+i(t-u)}\right|^4.
$$

The squared polynomial has coefficients $c_m m^{-1/2}$, where $0\le c_m\le d(m)$, supported in $(V^2,4V^2]$. Use the divisor bound, split into two dyadic blocks, apply (9.3) and (9.4), and absorb the logarithms into an arbitrarily small power of $T$. This proves (9.6).

Now suppose $V\ge2T_0^{2/3}$. Then $8(T_0/V)^2\le V$. Apply (9.6) with length $T_0/V$ and $P=V$ in (9.5). Absorbing the resulting square-root term gives

$$
S(V)\ll_\eta T^{C_1\eta}(RV+R^2).
\tag{9.7}
$$

If $V>T_0$, the absent-tail version of (9.5) gives this directly.

For $V<2T_0^{2/3}$, put $M=T_0/V$ and $P=8M^2$. Then $P\ge2T_0^{2/3}$, so (9.6) and (9.7) give

$$
S(M)\ll_\eta T^{C_2\eta}(R^{3/2}M+R^2).
$$

Using (9.5) again yields

$$
S(V)\ll_\eta T^{C_3\eta}
\left(RV+\frac{R^{3/2}T_0}{V}+R^2\right).
\tag{9.8}
$$

Therefore (9.7) holds whenever $V\ge V_0=R^{1/4}T_0^{1/2}$, whether $V$ lies above or below $2T_0^{2/3}$. If $V<V_0$, transfer to $P=4V_0$ and apply (9.7) there. We have proved

$$
S(V)\ll_\epsilon T^\epsilon
\left(RV+R^2+R^{5/4}T^{1/2}\right),
\tag{9.9}
$$

by choosing $\eta$ sufficiently small in terms of $\epsilon$. All auxiliary lengths are bounded by a fixed power of $T$, since $R\le T+1$. Lastly $|a_n|\le1\le\sqrt{2N}\,n^{-1/2}$ on the original block. Equation (9.3) bounds its difference-set moment by $2NS(N)$, giving (9.1). The assertion for subpower coefficients follows by the same majorization and a smaller initial error exponent. $\square$

## 10. Guth–Maynard's improvement

### 10.1. The large-value theorem of Guth and Maynard

**Theorem 10.1 (Guth–Maynard).** Let $T\ge2$ and $N\ge1$. Let $b_n$ $(N<n\le2N)$ be complex numbers with $|b_n|\le1$, and let $W\subset[0,T]$ be a one-separated set such that $\left|\sum_{N<n\le2N}b_nn^{it}\right|\ge V>0$ for every $t\in W$. Then for every $\delta>0$,

$$
|W|\ll_\delta T^\delta\left(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}\right).
\tag{10.1}
$$

The theorem and the strategy of its proof are due to Larry Guth and James Maynard, [*New large value estimates for Dirichlet polynomials*, arXiv:2405.20552v2](https://arxiv.org/pdf/2405.20552v2), Theorem 1.1. This section proves it completely along their lines. Some auxiliary steps use different arguments: the eigenvalue inequality of Lemma LV.8, the averaging kernels of Lemma LV.3, the smoothing step of Lemma LV.34 and the treatment of large common factors in Lemma LV.46.

#### 10.1.1. How the proof works

Write $V=N^\sigma$. For $N<T$, the mean-value estimate and the large-value inequality of Section 5 give

$$
|W|\preccurlyeq N^2V^{-2}+T\min\left(NV^{-2},N^4V^{-6}\right),
\tag{LV.1}
$$

where $\preccurlyeq$ (defined in §10.1.2) allows a factor $T^\delta$ for every $\delta>0$; Lemma LV.48 gives the deduction. At $\sigma=3/4$ both terms of the minimum equal $TN^{-1/2}$, while (10.1) gives $N^{1/2}+N^{3/5}+TN^{-3/5}$. If $V\le N^{7/10}$ then $NV^{-2}\le N^{12/5}V^{-4}$, and if $V\ge N^{4/5}$ then $N^4V^{-6}\le N^{12/5}V^{-4}$; in these ranges (10.1) follows from (LV.1). Comparing exponents, (10.1) is the stronger bound when $N^{7/10}<V<N^{4/5}$ and $N<T^{5/6}$, apart from arbitrarily small powers. The proof for the middle range has four stages.

*A cubic trace.* The values $D(t)$, $t\in W$, are the entries of a matrix applied to the coefficient vector. So $|W|N^{2\sigma}$ is at most $N$ times the top eigenvalue of the Gram matrix $G$, whose entries are the smoothed sums $\sum_nw(n/N)^2(n/N)^{i(t-t')}$. An elementary inequality bounds this eigenvalue by four times the average eigenvalue plus twice the cube root of $\operatorname{tr}G^3-(\operatorname{tr}G)^3/|W|^2$.

*Poisson summation.* Applying Poisson summation to the three summation variables in $\operatorname{tr}G^3$ produces a sum of oscillatory terms indexed by $\mathbf m\in\mathbb Z^3$. The term $\mathbf m=\mathbf0$ cancels against $(\operatorname{tr}G)^3/|W|^2$ up to a negligible error. When a coordinate of $\mathbf m$ vanishes, the separation of $W$ reduces the terms to a negligible quantity or to a mean square of a dual Dirichlet polynomial of length about $|t-t'|/N$. Heath-Brown's Theorem 9.1 controls that mean square.

*Three nonzero frequencies.* After the Poisson step, the sum over the three points of $W$ becomes a product of three values of $\Phi(v)=\sum_{t\in W}v^{it}$. Their arguments are the ratios $u_1/u_3$, $u_2/u_1$ and $u_3/u_2$ of the integration variables. The phase is linear in $(u_1,u_2,u_3)$, and integrating it along rays localizes the integral near a line in the plane of two such ratios. One is left with averages of $|\Phi|$ along affine images of a single variable. Two facts control them. First, $|\Phi|^2$ has average size $|W|$ and $|\Phi|^4$ has average size the additive energy $E(W)$. Second, a sparse nonnegative function cannot be concentrated on many images $u\mapsto(au+c)/b$ at once.

*Additive energy.* Large values on $W$ bound the additive energy $E(W)$ by moments of $\Phi$ at the rational points $n_1/n_2$. These moments are mean squares of Dirichlet polynomials over the difference set $W-W$, which Theorem 9.1 bounds.

The four stages combine at $N=T^{5/6}$ (Proposition LV.6). Removing the smooth weight and subdividing $[0,T]$ then give Theorem 10.1 in general.

#### 10.1.2. Conventions and tools

**The weight.** Fix a smooth $w:\mathbb R\to[0,1]$ supported in $[1,2]$ and equal to one on $[6/5,9/5]$. For instance, with $\beta(x)=e^{-1/x}$ for $x>0$ and $\beta(x)=0$ otherwise, put $\lambda(x)=\beta(x)/(\beta(x)+\beta(1-x))$ and $w(x)=\lambda(5x-5)\lambda(10-5x)$. Its derivatives are bounded by constants depending only on their order. Write $\|w\|_2^2=\int w^2$.

**Notation.** For $Y>0$, $x\sim Y$ means $Y<x\le2Y$, and $|m|\sim Y$ for an integer $m$ allows both signs. $A\asymp B$ means $A\ll B\ll A$. We write $A\preccurlyeq B$ if for every $\delta>0$ there is $C_\delta$ with $|A|\le C_\delta T^\delta B$. Implied constants never depend on $N$, $T$, $W$, $V$, $\sigma$ or the coefficients. They may depend on the fixed weights and on the auxiliary exponents $\epsilon$, $\kappa$, $k$ introduced below.

**Small losses.** Many steps truncate a sum or an integral at a power $T^{\kappa}$, where $\kappa>0$ is a small auxiliary exponent fixed at the start of the argument. Such a step bounds a quantity by $C_\kappa T^{c\kappa}$ times the main term, with an absolute constant $c$, plus an error $O_\kappa(T^{-100})$. Since $\kappa$ can be taken as small as desired, these losses are of the form allowed by $\preccurlyeq$. A quantity is *negligible* if it is $O(T^{-100})$. In each use below the main terms are bounded below by a fixed negative power of $T$, relative to the normalization in force, so negligible terms are absorbed into them.

**Fourier analysis.** Put $e(x)=e^{2\pi ix}$ and $\widehat f(\xi)=\int_{\mathbb R}f(x)e(-\xi x)\,dx$. For smooth compactly supported $f$, Fourier inversion $f(x)=\int\widehat f(\xi)e(\xi x)\,d\xi$ and the identity $\int|f|^2=\int|\widehat f|^2$ are proved by a Gaussian approximate identity in the proof of Lemma 7.2 of The Riemann hypothesis and its standard equivalents. If $f$ is supported in an interval of length $\ell$ and $|f^{(j)}|\le A_j$, then $j$ integrations by parts give $|\widehat f(\xi)|\le\ell A_j(2\pi|\xi|)^{-j}$. Hence such $f$ satisfy the hypotheses of Poisson summation, $\sum_{n\in\mathbb Z}f(n)=\sum_{k\in\mathbb Z}\widehat f(k)$, which is Fourier series and the theta function, Theorem 1.2. The same bounds hold for smooth functions all of whose derivatives are integrable, such as $(1+x^2)^{-20}$.

**Inequalities.** Cauchy–Schwarz for finite sums and integrals follows from $0\le\int|f-\lambda g|^2$ with the minimizing $\lambda$. Hölder's inequality with exponents $p_i>0$, $\sum1/p_i=1$, follows by normalizing the norms to one and integrating the pointwise inequality $\prod a_i\le\sum a_i^{p_i}/p_i$; the latter is the concavity of the logarithm, $\sum p_i^{-1}\log(a_i^{p_i})\le\log\sum p_i^{-1}a_i^{p_i}$. In particular $\left(\int kF\right)^3\le\left(\int k\right)^2\int kF^3$ for $k,F\ge0$. For an integrable kernel $K\ge0$, Fubini gives $\|K*f\|_1=\|K\|_1\|f\|_1$ when $f\ge0$. Cauchy–Schwarz with the weight $K(x-y)\,dy$ followed by Fubini gives $\|K*f\|_2\le\|K\|_1\|f\|_2$.

**Divisor functions.** Section 9 proves $d(n)\ll_\eta n^\eta$ for every $\eta>0$. Let $d_k(n)$ be the number of ordered factorizations $n=a_1\cdots a_k$. Choosing $a_1\mid n$ first gives $d_k(n)=\sum_{a\mid n}d_{k-1}(n/a)\le d(n)\max_{m\mid n}d_{k-1}(m)$. Since $d(m)\le d(n)$ for $m\mid n$, induction gives $d_k(n)\le d(n)^{k-1}$, so $d_k(n)\ll_{k,\eta}n^\eta$.

**Lemma LV.2 (Hermitian matrices).** Let $H$ be a Hermitian $r\times r$ matrix. It has an orthonormal basis of eigenvectors with real eigenvalues $\lambda_1,\dots,\lambda_r$, and $\operatorname{tr}H^j=\sum_i\lambda_i^j$. If $A$ is an $r\times s$ matrix, then $AA^*$ and $A^*A$ have nonnegative eigenvalues and the same largest eigenvalue $\lambda_{\max}$, and $\|A\mathbf b\|^2\le\lambda_{\max}\|\mathbf b\|^2$ for every $\mathbf b\in\mathbb C^s$.

**Proof.** The continuous function $x\mapsto x^*Hx$ attains its maximum on the unit sphere at some $x_0$. For any $y\perp x_0$ and real $\tau$, the vectors $(x_0+\tau y)/\|x_0+\tau y\|$ and $(x_0+i\tau y)/\|x_0+i\tau y\|$ lie on the sphere. Differentiating at $\tau=0$ gives $\operatorname{Re}\,y^*Hx_0=\operatorname{Im}\,y^*Hx_0=0$, so $Hx_0$ is a multiple $\lambda x_0$, real because $x_0^*Hx_0$ is real. The orthogonal complement of $x_0$ is mapped into itself by $H$, so induction on $r$ gives the orthonormal eigenbasis. In that basis $H^j$ is diagonal, which gives the trace formula. For $A$, $x^*AA^*x=\|A^*x\|^2\ge0$ and similarly for $A^*A$, so the eigenvalues are nonnegative. If $A^*Av=\lambda v$ with $\lambda>0$, then $Av\ne0$ and $AA^*(Av)=\lambda Av$; by symmetry the two matrices have the same positive eigenvalues. Expanding $\mathbf b$ in an eigenbasis of $A^*A$ gives $\|A\mathbf b\|^2=\mathbf b^*A^*A\mathbf b\le\lambda_{\max}\|\mathbf b\|^2$. $\square$

**Lemma LV.3 (local averages of band-limited sums).** There is a fixed integrable function $K_0\ge0$ with $K_0(u)\ll_j(1+|u|)^{-j}$ for every $j$, with the following property. Let $F(t)=\sum_jc_je^{i\lambda_jt}$ be a finite sum whose real frequencies $\lambda_j$ all lie in an interval of length $\Delta>0$. Then for every real $t$,

$$
|F(t)|\le\Delta\int_{\mathbb R}K_0(\Delta u)\,|F(t+u)|\,du,
\qquad
|F(t)|^2\le\|K_0\|_1\,\Delta\int_{\mathbb R}K_0(\Delta u)\,|F(t+u)|^2\,du.
\tag{LV.4}
$$

**Proof.** Fix a smooth $\theta$ supported in $[-1,2]$ with $\theta=1$ on $[0,1]$, and put $K_0(u)=(2\pi)^{-1}|\widehat\theta(u/(2\pi))|$; it decays faster than any power. First let all $\lambda_j\in[0,1]$. Fourier inversion gives $1=\theta(\lambda_j)=\int\widehat\theta(y)e(\lambda_jy)\,dy$, so

$$
F(t)=\int\widehat\theta(y)\sum_jc_je^{i\lambda_j(t+2\pi y)}\,dy=\int\widehat\theta(y)F(t+2\pi y)\,dy.
$$

Taking absolute values and substituting $u=2\pi y$ gives $|F(t)|\le\int K_0(u)|F(t+u)|\,du$. In general let the frequencies lie in $[a,a+\Delta]$ and write $F(t)=e^{iat}F_1(\Delta t)$, where $F_1$ has frequencies $(\lambda_j-a)/\Delta\in[0,1]$. Then $|F(t)|=|F_1(\Delta t)|\le\int K_0(u)|F(t+u/\Delta)|\,du$, which is the first inequality after the substitution $u\mapsto\Delta u$. The second follows from the first by Cauchy–Schwarz with the weight $\Delta K_0(\Delta u)\,du$, of total mass $\|K_0\|_1$. $\square$

Two cases occur below. A Dirichlet polynomial $\sum_{L<n\le2L}c_nn^{it}$ has frequencies $\log n\in(\log L,\log2L]$, so $\Delta=\log2$ for every length $L$. If $W$ lies in an interval of length $T$, the sum $x\mapsto\sum_{t\in W}e^{ixt}$ has frequencies in that interval, so $\Delta=T$.

**Lemma LV.5 (an oscillatory integral).** There is an absolute constant $C$ such that for real $\alpha$ with $|\alpha|\ge2$ and all $1\le a<b$,

$$
\left|\int_a^bv^{-1+i\alpha}e(-v)\,dv\right|\le C|\alpha|^{-1/2}.
$$

**Proof.** Write the integrand as $v^{-1}e^{i\phi(v)}$ with $\phi(v)=\alpha\log v-2\pi v$, so $\phi'(v)=\alpha/v-2\pi$ and $\phi''(v)=-\alpha/v^2$; $\phi'$ is monotone on $(0,\infty)$. Two standard estimates apply on an interval $[c,x]$. If $\phi'$ has constant sign and $|\phi'|\ge\lambda>0$ there, writing $e^{i\phi}=(e^{i\phi})'/(i\phi')$ and integrating by parts gives $|\int_c^xe^{i\phi}|\le3/\lambda$: the boundary terms contribute $2/\lambda$, and $\int|(1/\phi')'|=|1/\phi'(x)-1/\phi'(c)|\le1/\lambda$ by monotonicity. If instead $|\phi''|\ge\rho>0$ on $[c,x]$, the set where $|\phi'|<\sqrt\rho$ is an interval of length at most $2/\sqrt\rho$. On each of the at most two remaining intervals $\phi'$ has constant sign, and the first estimate gives $|\int_c^xe^{i\phi}|\le8/\sqrt\rho$. For the weight $v^{-1}$, put $F(x)=\int_c^xe^{i\phi}$. Integration by parts gives $\int_c^dv^{-1}e^{i\phi}\,dv=F(d)/d+\int_c^dF(v)v^{-2}\,dv$, so its absolute value is at most $c^{-1}\sup_{c\le x\le d}|F(x)|$.

Let $\alpha\ge2$ and $v_0=\alpha/(2\pi)$. On $(0,v_0/2]$ we have $\alpha/v\ge4\pi$, hence $\phi'\ge\alpha/(2v)$. On a dyadic interval $[V,2V]$ there, $\phi'\ge\alpha/(4V)$, so the weighted integral is at most $V^{-1}\cdot12V/\alpha=12/\alpha$. At most $1+\log_2\alpha$ dyadic intervals meet $[1,v_0/2]$, giving $O(\alpha^{-1}\log\alpha)$. On $[v_0/2,2v_0]$, $|\phi''|\ge\alpha/(4v_0^2)=\pi^2/\alpha$, so the integral is at most $(4\pi/\alpha)\cdot8\sqrt\alpha/\pi=32\alpha^{-1/2}$. On $[2v_0,\infty)$, $|\phi'|\ge\pi$, so the integral is at most $(2v_0)^{-1}\cdot3/\pi=3/\alpha$. If $\alpha\le-2$, then $|\phi'|\ge\max(2\pi,|\alpha|/v)$ on all of $(0,\infty)$. On $[V,2V]$ the weighted integral is at most $\min(6/|\alpha|,3/(2\pi V))$. The dyadic intervals with $V\le|\alpha|$ give $O(|\alpha|^{-1}\log|\alpha|)$, and the others give a geometric sum $O(1/|\alpha|)$. In all cases the total is $O(|\alpha|^{-1/2})$. $\square$

#### 10.1.3. The core estimate and the Gram matrix

**Proposition LV.6 (the core estimate).** Fix $\epsilon>0$. Let $N$ be sufficiently large, $T=N^{6/5}$ and $7/10\le\sigma\le4/5$. Let $|b_n|\le1$, put

$$
D_N(t)=\sum_nw(n/N)b_nn^{it},
$$

and let $W$ be a $T^\epsilon$-separated subset of an interval of length $T$ with $|D_N(t)|\ge N^\sigma$ for every $t\in W$. Then

$$
|W|\preccurlyeq TN^{(12-20\sigma)/5},
\tag{LV.7}
$$

with constants depending on $\epsilon$ but not on $\sigma$.

Sections 10.1.3–10.1.11 prove Proposition LV.6, and $N,T,\sigma,\epsilon,W,b_n$ keep this meaning there. We may assume $W\ne\varnothing$. Distinct points of $W$ satisfy $T^\epsilon\le|t-t'|\le T$, and $|W|\le T+1\le2T$. The truncation exponent $\kappa$ satisfies $0<\kappa\le\epsilon/4$.

Let $A$ be the matrix with rows indexed by $t\in W$ and columns by the integers $n\in(N,2N)$, at most $N$ of them, with entries $A_{t,n}=w(n/N)(n/N)^{it}$. With $\mathbf b=(b_n)$ we have $(A\mathbf b)_t=N^{-it}D_N(t)$. The Gram matrix $G=AA^*$ has entries

$$
G_{t,t'}=\sum_nw(n/N)^2(n/N)^{i(t-t')}.
$$

**Lemma LV.8 (top eigenvalue and cubic trace).** Let $H$ be a positive semidefinite Hermitian $r\times r$ matrix with largest eigenvalue $\lambda_{\max}$. Put $\mu=\operatorname{tr}H/r$ and $\Xi=\operatorname{tr}H^3-(\operatorname{tr}H)^3/r^2$. Then $\Xi\ge0$ and

$$
\lambda_{\max}\le4\mu+2\,\Xi^{1/3}.
\tag{LV.9}
$$

**Proof.** By Lemma LV.2, $H$ has eigenvalues $\lambda_1,\dots,\lambda_r\ge0$ with $\sum\lambda_i=r\mu$ and $\sum\lambda_i^3=\operatorname{tr}H^3$. For real $\lambda,\mu$ one checks $\lambda^3-\mu^3-3\mu^2(\lambda-\mu)=(\lambda-\mu)^2(\lambda+2\mu)$. Summing over the eigenvalues, the linear terms cancel because $\sum(\lambda_i-\mu)=0$, and therefore

$$
\Xi=\sum_{i=1}^r\left(\lambda_i^3-\mu^3\right)=\sum_{i=1}^r(\lambda_i-\mu)^2(\lambda_i+2\mu)\ge0.
$$

If $\lambda_{\max}\le4\mu$ there is nothing to prove. Otherwise $\lambda_{\max}-\mu>\tfrac34\lambda_{\max}$, and the term of an eigenvalue equal to $\lambda_{\max}$ alone gives $\Xi\ge\tfrac9{16}\lambda_{\max}^3$. Hence $\lambda_{\max}\le(16/9)^{1/3}\Xi^{1/3}\le2\Xi^{1/3}$. $\square$

**Lemma LV.10 (large values and the Gram matrix).** With $\Xi=\operatorname{tr}G^3-(\operatorname{tr}G)^3/|W|^2$,

$$
|W|\le N^{1-2\sigma}\left(4\operatorname{tr}G/|W|+2\,\Xi^{1/3}\right).
$$

**Proof.** By Lemma LV.2 and $|b_n|\le1$,

$$
|W|N^{2\sigma}\le\sum_{t\in W}|D_N(t)|^2=\|A\mathbf b\|^2\le\lambda_{\max}(G)\|\mathbf b\|^2\le N\lambda_{\max}(G).
$$

Lemma LV.8 with $H=G$ and $r=|W|$ completes the proof. $\square$

#### 10.1.4. Poisson expansion of the traces

For real $s$ let $q_s(x)=w(x)^2x^{is}$ for $x>0$ and $q_s(x)=0$ for $x\le0$; it is smooth and supported in $[1,2]$.

**Lemma LV.11 (the transforms $\widehat q_s$).** For real $s,\xi$ and integers $j\ge0$:

1. $|\widehat q_s(\xi)|\le\|w\|_2^2\le1$;
2. $|\widehat q_s(\xi)|\le C_j(1+|s|)^j|\xi|^{-j}$;
3. $|\widehat q_s(\xi)|\le C_j(1+|\xi|)^j|s|^{-j}$ if $s\ne0$;
4. $\widehat q_{-s}(\xi)=\overline{\widehat q_s(-\xi)}$.

**Proof.** Part 1 is immediate. The $j$-th derivative of $q_s$ is a sum of products of derivatives of $w^2$ with $s$-polynomials of degree at most $j$ times powers of $x$, so it is bounded on $[1,2]$ by $C_j(1+|s|)^j$; part 2 follows by integration by parts. For part 3 put $g_\xi(x)=w(x)^2e(-\xi x)$. Since $x^{is}=(x^{is+1})'/(is+1)$, integrating by parts $j$ times gives

$$
\widehat q_s(\xi)=\int g_\xi(x)x^{is}\,dx=\frac{(-1)^j}{(is+1)\cdots(is+j)}\int_1^2g_\xi^{(j)}(x)\,x^{is+j}\,dx.
$$

Each factor satisfies $|is+l|\ge|s|$, and $|g_\xi^{(j)}|\le C_j(1+|\xi|)^j$. Part 4 holds because $q_{-s}=\overline{q_s}$. $\square$

The Fourier transform of $x\mapsto q_s(x/N)$ is $\xi\mapsto N\widehat q_s(N\xi)$, so Poisson summation gives

$$
G_{t,t'}=\sum_nq_{t-t'}(n/N)=N\sum_{m\in\mathbb Z}\widehat q_{t-t'}(mN).
\tag{LV.12}
$$

Consequently $\operatorname{tr}G=|W|N\bigl(\|w\|_2^2+\sum_{m\ne0}\widehat q_0(mN)\bigr)$, and by part 2 of Lemma LV.11 the sum over $m\ne0$ is negligible. Expanding the cube of (LV.12) gives $\operatorname{tr}G^3=\sum_{\mathbf m\in\mathbb Z^3}\mathcal I_{\mathbf m}$, where

$$
\mathcal I_{\mathbf m}=N^3\sum_{t_1,t_2,t_3\in W}\widehat q_{t_1-t_2}(m_1N)\,\widehat q_{t_2-t_3}(m_2N)\,\widehat q_{t_3-t_1}(m_3N)
\tag{LV.13}
$$

and the series converges absolutely by Lemma LV.11.

**Lemma LV.14 (the main term cancels).** We have

$$
|W|\ll N^{2-2\sigma}+N^{1-2\sigma}\Bigl|\sum_{\mathbf m\in\mathbb Z^3\setminus\{\mathbf0\}}\mathcal I_{\mathbf m}\Bigr|^{1/3}.
\tag{LV.15}
$$

Moreover, the sum of $|\mathcal I_{\mathbf m}|$ over the $\mathbf m$ with $\max_i|m_i|>T^{1+\kappa}/N$ is negligible.

**Proof.** In $\mathcal I_{\mathbf0}$ the terms with $t_1=t_2=t_3$ contribute $N^3|W|\widehat q_0(0)^3=N^3|W|\|w\|_2^6$. Every other term contains a factor $\widehat q_{t-t'}(0)$ with $t\ne t'$, which is at most $C_jT^{-\epsilon j}$ by part 3 of Lemma LV.11, while the remaining factors are at most one. These terms total at most $8C_jN^3T^{3-\epsilon j}$, which is negligible. The expansion of $\operatorname{tr}G$ gives $(\operatorname{tr}G)^3/|W|^2=N^3|W|\|w\|_2^6$ up to a negligible error. Hence $\Xi=\sum_{\mathbf m\ne\mathbf0}\mathcal I_{\mathbf m}$ up to a negligible error. As $\Xi\ge0$ and $\operatorname{tr}G/|W|\le2N$, Lemma LV.10 gives (LV.15); the cube root of the error is absorbed by $N^{2-2\sigma}\ge1$.

For the second assertion let $|m_1|>T^{1+\kappa}/N$; the other coordinates are treated in the same way. Since $|t_1-t_2|\le T$, part 2 of Lemma LV.11 gives

$$
|\widehat q_{t_1-t_2}(m_1N)|\le C_j\Bigl(\frac{2T}{|m_1|N}\Bigr)^j\le C_j2^jT^{-\kappa(j-2)}\Bigl(\frac{T}{|m_1|N}\Bigr)^2.
$$

The sum of $(T/(|m_1|N))^2$ over these $m_1$ is at most $4T$. For the other two factors, $\sum_m|\widehat q_s(mN)|\le1+\sum_{m\ne0}C_2(1+T)^2(mN)^{-2}\le CT^2$ whenever $|s|\le T$. So these terms total at most $C_jN^3|W|^3T^{5-\kappa(j-2)}$, which is negligible for large $j$. $\square$

Split the nonzero frequencies according to how many coordinates vanish:

$$
\sum_{\mathbf m\ne\mathbf0}\mathcal I_{\mathbf m}=\Sigma_1+\Sigma_2+\Sigma_3,
$$

where $\Sigma_r$ is the sum over the $\mathbf m$ with exactly $r$ nonzero coordinates. Relabelling $t_1,t_2,t_3$ cyclically in (LV.13) shows $\mathcal I_{(m_1,m_2,m_3)}=\mathcal I_{(m_2,m_3,m_1)}$.

#### 10.1.5. Frequencies with a vanishing coordinate

**Lemma LV.16.** $\Sigma_1$ is negligible.

**Proof.** By the cyclic symmetry, $\Sigma_1=3\sum_{m_3\ne0}\mathcal I_{(0,0,m_3)}$. In a term with $t_1\ne t_2$ or $t_2\ne t_3$, one of the factors $\widehat q_{t_1-t_2}(0)$, $\widehat q_{t_2-t_3}(0)$ is at most $C_jT^{-\epsilon j}$. As in the proof of Lemma LV.14, the remaining sum over $m_3$ is at most $CT^2$, so these terms total at most $C_jN^3|W|^3T^{2-\epsilon j}$. If $t_1=t_2=t_3$, the factor $\sum_{m_3\ne0}|\widehat q_0(m_3N)|\le2\sum_{m\ge1}C_j(mN)^{-j}$ is negligible. $\square$

For real $s$ put

$$
H(s)=\sum_{m\ne0}\widehat q_s(mN).
$$

**Lemma LV.17 (dual sums).** If $(1+|s|)T^\kappa<N$, then $H(s)$ is negligible. If $T^\epsilon\le|s|\le T$ and $L$ is an integer with $T^\kappa(1+|s|)/N\le L\le T^2$, then

$$
|H(s)|\le C|s|^{-1/2}\int_{-T^\kappa}^{T^\kappa}\Bigl|\sum_{1\le m\le L}m^{-i(s-r)}\Bigr|\,dr+(\text{negligible}),
\tag{LV.18}
$$

where $C$ depends only on $w$.

**Proof.** By part 2 of Lemma LV.11, $|\widehat q_s(mN)|\le C_j((1+|s|)/(|m|N))^j$. In the first case this is at most $C_jT^{-\kappa j}|m|^{-j}$ for every $m\ne0$, and the sum is negligible. In the second case $(1+|s|)/N\le LT^{-\kappa}$, so the terms with $|m|>L$ contribute at most $C_jT^{-\kappa j}\sum_{|m|>L}(L/|m|)^j\le4C_jLT^{-\kappa j}$, again negligible.

For the terms $1\le m\le L$ we use the Mellin transform $\mathcal W(z)=\int_0^\infty w(x)^2x^{z-1}\,dx$, an entire function. The Fourier transform of the smooth compactly supported function $u\mapsto e^uw(e^u)^2$ is $\xi\mapsto\mathcal W(1-2\pi i\xi)$. Fourier inversion, followed by the substitutions $x=e^u$ and $r=-2\pi\xi$, gives

$$
w(x)^2=\frac1{2\pi}\int_{\mathbb R}\mathcal W(1+ir)\,x^{-1-ir}\,dr\qquad(x>0).
$$

Since $\mathcal W(1+ir)=\int w(x)^2x^{ir}\,dx$, we have $|\mathcal W(1+ir)|\le\int w^2\le1$, and integration by parts as in part 3 of Lemma LV.11 gives $|\mathcal W(1+ir)|\le C_j(1+|r|)^{-j}$. For $1\le m\le L$ the interval $[1/m,2L/m]$ contains $[1,2]$. So, with the order of integration interchanged on this compact range,

$$
\widehat q_s(mN)=\int_{1/m}^{2L/m}w(x)^2x^{is}e(-mNx)\,dx=\frac1{2\pi}\int_{\mathbb R}\mathcal W(1+ir)\int_{1/m}^{2L/m}x^{-1+i(s-r)}e(-mNx)\,dx\,dr.
$$

The substitution $v=mNx$ turns the inner integral into $(mN)^{-i(s-r)}\Gamma(s-r)$, where $\Gamma(\alpha)=\int_N^{2LN}v^{-1+i\alpha}e(-v)\,dv$ does not depend on $m$. Hence

$$
\sum_{1\le m\le L}\widehat q_s(mN)=\frac1{2\pi}\int_{\mathbb R}\mathcal W(1+ir)\,N^{-i(s-r)}\,\Gamma(s-r)\sum_{1\le m\le L}m^{-i(s-r)}\,dr.
\tag{LV.19}
$$

On $|r|>T^\kappa$ we use $|\Gamma|\le\log(2L)$ and $|\sum_m|\le L$; this part is at most $C_jL\log(2L)T^{-\kappa(j-1)}$, which is negligible. For $|r|\le T^\kappa$ the number $\alpha=s-r$ satisfies $|\alpha|\ge|s|-T^\kappa\ge|s|/2\ge2$, since $\kappa\le\epsilon/4$ and $T$ is large. Lemma LV.5 gives $|\Gamma(\alpha)|\le C\sqrt2|s|^{-1/2}$, which proves (LV.18) for the positive frequencies.

By part 4 of Lemma LV.11, $\sum_{-L\le m\le-1}\widehat q_s(mN)=\overline{\sum_{1\le m\le L}\widehat q_{-s}(mN)}$. Apply the positive case to $-s$ and substitute $r\mapsto-r$. This replaces $\sum_mm^{-i(-s-r)}$ by $\sum_mm^{i(s-r)}$, which has the same absolute value as $\sum_mm^{-i(s-r)}$. $\square$

**Proposition LV.20 (two nonzero frequencies).** For every integer $k\ge1$,

$$
\Sigma_2\preccurlyeq N^2|W|^2+TN|W|^{2-1/k}+N^2|W|^{2-3/(4k)}T^{1/(2k)},
\tag{LV.21}
$$

with constants depending also on $k$.

**Proof.** Consider the terms of $\Sigma_2$ with $m_3=0\ne m_1,m_2$. The factor $\widehat q_{t_3-t_1}(0)$ is at most $C_jT^{-\epsilon j}$ unless $t_3=t_1$. The sums of the other two factors over $m_1,m_2$ are at most $CT^2$ each. Up to a negligible error, only $t_3=t_1$ survives, and that part equals $N^3\|w\|_2^2\sum_{t_1,t_2}H(t_1-t_2)H(t_2-t_1)$. Part 4 of Lemma LV.11 gives $H(-s)=\overline{H(s)}$. The two other positions of the vanishing coordinate give the same expression after a cyclic relabelling. Therefore

$$
\Sigma_2=3N^3\|w\|_2^2\sum_{t,t'\in W}|H(t-t')|^2+(\text{negligible}).
\tag{LV.22}
$$

The diagonal $t=t'$ is negligible, because $|H(0)|\le2\sum_{m\ge1}C_j(mN)^{-j}$. For $t\ne t'$ the difference $s=t-t'$ satisfies $T^\epsilon\le|s|\le T$. Split this range into the $O(\log T)$ dyadic ranges $K\le|s|<2K$, with $K=2^iT^\epsilon\le T$. If $(1+2K)T^\kappa<N$, Lemma LV.17 shows that $H$ is negligible on the range. Otherwise $K\ge NT^{-\kappa}/4$. In that case put $L_K=\lceil(1+2K)T^\kappa/N\rceil\le6KT^\kappa/N$. Lemma LV.17 with $L=L_K$ and Cauchy–Schwarz in $r$ give, for $K\le|s|<2K$,

$$
|H(s)|^2\le CK^{-1}T^\kappa\int_{-T^\kappa}^{T^\kappa}\Bigl|\sum_{1\le m\le L_K}m^{ir}\,m^{-is}\Bigr|^2dr+(\text{negligible}).
$$

Cut $[1,L_K]$ into the block $\{1\}$ and the blocks $(P,2P]\cap[1,L_K]$ with $P<L_K$ a power of two. There are at most $2+\log_2L_K$ blocks, and Cauchy–Schwarz bounds the square of the sum by that number times the sum of the squares of the block sums. The block $\{1\}$ contributes $|W|^2$ to $\sum_{t,t'}$. Fix $r$ and a block $(P,2P]$, and put $X(\tau)=\sum_{P<m\le2P}a_mm^{-i\tau}$ with $a_m=m^{ir}$ on the block and $0$ off it. Hölder's inequality over the $|W|^2$ pairs gives

$$
\sum_{t,t'\in W}|X(t-t')|^2\le|W|^{2-2/k}\Bigl(\sum_{t,t'\in W}|X(t-t')|^{2k}\Bigr)^{1/k}.
$$

Now $X^k=\sum_{P^k<n\le2^kP^k}c_nn^{-i\tau}$ with $|c_n|\le d_k(n)\ll_\eta T^\eta$. Split the range of $n$ into $k$ dyadic blocks, apply Cauchy–Schwarz over them, and apply Theorem 9.1 in its version for coefficients bounded by $T^{o(1)}$ to each block. Note that $W$ is a one-separated set in an interval of length $T$. This gives

$$
\sum_{t,t'\in W}|X(t-t')|^{2k}\preccurlyeq|W|P^{2k}+|W|^2P^k+|W|^{5/4}T^{1/2}P^k,
$$

hence

$$
\sum_{t,t'\in W}|X(t-t')|^2\preccurlyeq|W|^{2-1/k}P^2+|W|^2P+|W|^{2-3/(4k)}T^{1/(2k)}P.
$$

With $P\le L_K\le6KT^\kappa/N$ and $N/K\le4T^\kappa$, the contribution of the range $K$ to (LV.22) is

$$
\preccurlyeq N^3K^{-1}\left(|W|^2+|W|^2L_K+|W|^{2-1/k}L_K^2+|W|^{2-3/(4k)}T^{1/(2k)}L_K\right)
\preccurlyeq N^2|W|^2+NK|W|^{2-1/k}+N^2|W|^{2-3/(4k)}T^{1/(2k)}.
$$

Since $K\le T$ and there are $O(\log T)$ ranges, (LV.21) follows. $\square$

#### 10.1.6. Three nonzero frequencies

For $v>0$ put

$$
\Phi(v)=\sum_{t\in W}v^{it}.
$$

Then $|\Phi(v)|\le|W|$ and $\Phi(1/v)=\overline{\Phi(v)}$. Translating $W$ by $\tau$ multiplies $\Phi(v)$ by $v^{i\tau}$, so $|\Phi|$ does not change. The additive energy of $W$ is

$$
E(W)=\#\left\{(t_1,t_2,t_3,t_4)\in W^4:|t_1+t_2-t_3-t_4|\le1\right\}.
$$

**Lemma LV.23 (integral form of $\mathcal I_{\mathbf m}$).** For $\mathbf m\in\mathbb Z^3$,

$$
\mathcal I_{\mathbf m}=N^3\int_0^\infty\!\!\int_0^\infty\Phi(v_1)\,\Phi(v_2/v_1)\,\Phi(1/v_2)\,K_{\mathbf m}(v_1,v_2)\,dv_1\,dv_2,
$$

where

$$
K_{\mathbf m}(v_1,v_2)=\int_{\mathbb R}u^2w(u)^2w(v_1u)^2w(v_2u)^2\,e\bigl(-N(m_1v_1+m_2v_2+m_3)u\bigr)\,du.
$$

$K_{\mathbf m}$ vanishes unless $v_1,v_2\in[1/2,2]$, and $|K_{\mathbf m}(v_1,v_2)|\le C_j(1+N|m_1v_1+m_2v_2+m_3|)^{-j}$ for every $j$. Moreover $\overline{\mathcal I_{(m_1,m_2,m_3)}}=\mathcal I_{(-m_1,-m_3,-m_2)}$.

**Proof.** Write each transform in (LV.13) as an integral over $u_i\in[1,2]$ and carry out the sums over the points first. The variable $t_1$ occurs in $(u_1/u_3)^{it_1}$, $t_2$ in $(u_2/u_1)^{it_2}$ and $t_3$ in $(u_3/u_2)^{it_3}$, so

$$
\mathcal I_{\mathbf m}=N^3\int_{[1,2]^3}\prod_{i=1}^3w(u_i)^2\;\Phi\Bigl(\frac{u_1}{u_3}\Bigr)\Phi\Bigl(\frac{u_2}{u_1}\Bigr)\Phi\Bigl(\frac{u_3}{u_2}\Bigr)e\bigl(-N(m_1u_1+m_2u_2+m_3u_3)\bigr)\,du.
\tag{LV.24}
$$

The substitution $u_1=v_1u$, $u_2=v_2u$, $u_3=u$ has Jacobian $u^2$. It turns the three ratios into $v_1$, $v_2/v_1$, $1/v_2$ and the phase into $N(m_1v_1+m_2v_2+m_3)u$, which gives the formula. The integrand of $K_{\mathbf m}$ vanishes unless $u\in[1,2]$ and $v_1u,v_2u\in[1,2]$, which forces $v_1,v_2\in[1/2,2]$. For such $v_1,v_2$ its $u$-derivatives are bounded by constants depending only on their order, and its integral is at most $8/3$. Integrating by parts $j$ times gives the bound for $K_{\mathbf m}$. For the last identity, conjugate (LV.24): each $\overline{\Phi(x)}$ becomes $\Phi(1/x)$ and the phase changes sign. Renaming $u_2$ as $u_3$ and $u_3$ as $u_2$ then gives (LV.24) for the frequency $(-m_1,-m_3,-m_2)$. $\square$

To state the reduction of $\Sigma_3$, fix smooth functions $\psi_2,\psi_0:\mathbb R\to[0,1]$ with $\psi_2=1$ on $[1/4,4]$, $\operatorname{supp}\psi_2\subset[1/8,8]$, $\psi_0=1$ on $[1/8,8]$ and $\operatorname{supp}\psi_0\subset[1/16,16]$. Put $k_0(z)=(1+z^2)^{-20}$. For a dyadic number $M\ge1/2$ let $B=NM$ and

$$
Q_M(x)=B\int_{\mathbb R}k_0\bigl(B(x-y)\bigr)\psi_2(y)|\Phi(y)|^2\,dy,\qquad f_M=\psi_0Q_M.
\tag{LV.25}
$$

For dyadic $M_1,M$ let $\mathfrak M=\mathfrak M(M_1,M)$ be the set of $\mathbf m\in\mathbb Z^3$ with $|m_1|\sim M_1$, $|m_2|\sim M$ and $M<|m_3|\le10M$, and put

$$
\beta_{\mathbf m}(v)=\frac{m_1v+m_3}{m_2},\qquad\alpha_{\mathbf m}(v)=\frac{m_1v+m_3}{m_2v}.
$$

**Lemma LV.26 (reduction of $\Sigma_3$).** There are dyadic numbers $1/2\le M_1\le M\le T^{1+\kappa}/N$ such that, with $f=f_M$,

$$
\Sigma_3\preccurlyeq\frac{N^2}{M}\sum_{\mathbf m\in\mathfrak M}\int_{1/2}^2|\Phi(v)|\,f\bigl(\beta_{\mathbf m}(v)\bigr)^{1/2}f\bigl(\alpha_{\mathbf m}(v)\bigr)^{1/2}\,dv+(\text{negligible}).
\tag{LV.27}
$$

**Proof.** By Lemma LV.14 the frequencies with a coordinate exceeding $T^{1+\kappa}/N$ in absolute value may be discarded. Apply the identity of Lemma LV.23 to $-\mathbf m$: it shows $|\mathcal I_{(m_1,m_3,m_2)}|=|\mathcal I_{-\mathbf m}|$. Together with the cyclic symmetry, every rearrangement $\mathbf m'$ of the coordinates of $\mathbf m$ satisfies $|\mathcal I_{\mathbf m}|\in\{|\mathcal I_{\mathbf m'}|,|\mathcal I_{-\mathbf m'}|\}$. Take $\mathbf m'$ with $|m_1'|\le|m_2'|\le|m_3'|$; each such $\mathbf m'$ comes from at most six $\mathbf m$. So $|\Sigma_3|$ is at most twelve times the sum of $|\mathcal I_{\mathbf m}|$ over the $\mathbf m$ with nonzero coordinates and $|m_1|\le|m_2|\le|m_3|$.

For these $\mathbf m$, if $|m_3|>5|m_2|$ then $|m_1v_1+m_2v_2+m_3|\ge|m_3|-4|m_2|\ge|m_3|/5$ for $v_1,v_2\in[1/2,2]$. Lemma LV.23 then gives $|\mathcal I_{\mathbf m}|\le C_jN^3|W|^3(N|m_3|)^{-j}$, and the sum of these terms is negligible. The remaining $\mathbf m$ satisfy $|m_2|\le|m_3|\le5|m_2|$. Group them by $|m_1|\sim M_1$ and $|m_2|\sim M$; then $M_1\le M$ and $M<|m_3|\le10M$, so $\mathbf m\in\mathfrak M(M_1,M)$. There are $O(\log^2T)$ such pairs, so it suffices to bound $\sum_{\mathbf m\in\mathfrak M}|\mathcal I_{\mathbf m}|$ for one pair.

Fix $\mathbf m\in\mathfrak M$ and $v_1\in[1/2,2]$, and put $c=-(m_1v_1+m_3)/m_2$, so that $m_1v_1+m_2v_2+m_3=m_2(v_2-c)$. If $\operatorname{dist}(c,[1/2,2])\ge1/8$, then $|K_{\mathbf m}(v_1,v_2)|\le C_jB^{-j}$ for all $v_2\in[1/2,2]$, because $N|m_2|\ge B$. The contribution of these $v_1$ to $\sum_{\mathbf m}|\mathcal I_{\mathbf m}|$ is at most $C_jN^3|W|^3T^{4}B^{-j}$, which is negligible since $B\ge N/2$. Otherwise $c\in[3/8,17/8]$ and $c/v_1\in[3/16,17/4]$, both in $[1/8,8]$, where $f_M=Q_M$. Since $(1+|z|)^2\ge1+z^2$, we have $(1+N|m_2||v_2-c|)^{-40}\le k_0(B(v_2-c))$. By Lemma LV.23 and Cauchy–Schwarz in $v_2$,

$$
\int_{1/2}^2|K_{\mathbf m}||\Phi(v_2/v_1)||\Phi(v_2)|\,dv_2\le C\Bigl(\int_{1/2}^2k_0(B(v_2-c))|\Phi(v_2/v_1)|^2dv_2\Bigr)^{1/2}\Bigl(\int_{1/2}^2k_0(B(v_2-c))|\Phi(v_2)|^2dv_2\Bigr)^{1/2}.
$$

The second factor is at most $(Q_M(c)/B)^{1/2}$, because $\psi_2=1$ on $[1/2,2]$ and $k_0$ is even. In the first substitute $y=v_2/v_1\in[1/4,4]$, so $dv_2\le2\,dy$. Since $v_1\ge1/2$ and $1+z^2/4\ge(1+z^2)/4$, we have $k_0(Bv_1(y-c/v_1))\le k_0(B(y-c/v_1)/2)\le4^{20}k_0(B(y-c/v_1))$. So the first factor is at most $(2\cdot4^{20}Q_M(c/v_1)/B)^{1/2}$. With $|\Phi(1/v_2)|=|\Phi(v_2)|$ and $N^3/B=N^2/M$ this gives

$$
|\mathcal I_{\mathbf m}|\le C\frac{N^2}{M}\int_{1/2}^2|\Phi(v_1)|\,f_M\Bigl(-\frac{m_1v_1+m_3}{m_2}\Bigr)^{1/2}f_M\Bigl(-\frac{m_1v_1+m_3}{m_2v_1}\Bigr)^{1/2}dv_1+(\text{negligible}).
$$

Finally $\mathfrak M$ is invariant under $m_2\mapsto-m_2$, which removes the signs and gives (LV.27). $\square$

#### 10.1.7. Integral moments of $\Phi$

**Lemma LV.28 (moments of $\Phi$).** Let $\psi\ge0$ be a fixed smooth function with compact support in $(0,\infty)$, and let $W$ be any finite one-separated set. Then

$$
\int_0^\infty\psi(v)|\Phi(v)|^2\,dv\ll_\psi|W|,\qquad\int_0^\infty\psi(v)|\Phi(v)|^4\,dv\ll_\psi E(W).
$$

Moreover $|W|^2\le E(W)\le3|W|^3$, and for every real $c$ at most $4E(W)$ quadruples in $W^4$ satisfy $|t_1+t_2-t_3-t_4-c|\le1$.

**Proof.** The quadruples $(t_1,t_2,t_1,t_2)$ show $E(W)\ge|W|^2$. Given $t_1,t_2,t_3$, the points $t_4$ with $|t_1+t_2-t_3-t_4|\le1$ lie in an interval of length two, which contains at most three points of $W$; so $E(W)\le3|W|^3$. For the shifted count let $\nu(a)$, $a\in\mathbb Z$, be the number of pairs $(t_1,t_2)$ with $t_1+t_2\in[a,a+1)$. Pairs of pairs in the same cell have sums differing by less than one, so $\sum_a\nu(a)^2\le E(W)$. If $t_1+t_2\in[a,a+1)$, $t_3+t_4\in[b,b+1)$ and $|t_1+t_2-t_3-t_4-c|\le1$, then $a-b$ is one of at most four integers determined by $c$. For each such difference $d$, Cauchy–Schwarz gives $\sum_a\nu(a)\nu(a-d)\le\sum_a\nu(a)^2$, which proves the count.

Substitute $v=e^x$ and put $\Psi(x)=e^x\psi(e^x)$, a fixed smooth compactly supported function, so that $|\widehat\Psi(\xi)|\ll(1+|\xi|)^{-2}$. Then

$$
\int\psi|\Phi|^2\,dv=\sum_{t,t'\in W}\int\Psi(x)e^{ix(t-t')}\,dx\ll\sum_{t,t'\in W}(1+|t-t'|)^{-2}\ll|W|,
$$

because a one-separated set has at most one point in each half-open unit interval. In the same way $\int\psi|\Phi|^4\,dv\ll\sum(1+|t_1+t_2-t_3-t_4|)^{-2}$ over $W^4$. The quadruples with $k\le|t_1+t_2-t_3-t_4|<k+1$ lie in two shifted windows of the kind just counted, so there are at most $8E(W)$ of them. Summing over $k\ge0$ with the weights $(1+k)^{-2}$ gives the bound $\ll E(W)$. $\square$

**Lemma LV.29 (the smoothed square function).** Let $1/2\le M\le T^{1+\kappa}/N$ be dyadic and put $\Lambda=T^{1+\kappa}$. The function $f=f_M$ of (LV.25) is smooth, nonnegative and supported in $[1/16,16]$. It satisfies $\|f\|_1\ll|W|$ and $\|f\|_2^2\ll E(W)$, and

$$
|\widehat f(\xi)|\le A_j\Bigl(\frac{\Lambda}{|\xi|}\Bigr)^j\|f\|_\infty\qquad(j\ge0,\ \xi\ne0),
$$

with $A_j$ depending only on $j$ and the fixed functions $\psi_0,\psi_2,k_0$.

**Proof.** $Q_M$ is the convolution of $K_B(x)=Bk_0(Bx)$, of mass $\|k_0\|_1$, with $g=\psi_2|\Phi|^2$. So $\|f\|_1\le\|Q_M\|_1=\|k_0\|_1\|g\|_1\ll|W|$ and $\|f\|_2\le\|Q_M\|_2\le\|k_0\|_1\|g\|_2\ll E(W)^{1/2}$ by Lemma LV.28, applied with $\psi_2$ and $\psi_2^2$. Differentiating under the integral shows that $Q_M$ is smooth.

For the Fourier bound, $\widehat Q_M(\zeta)=\widehat k_0(\zeta/B)\widehat g(\zeta)$ with $|\widehat g|\le\|g\|_1\le8|W|^2$ and $|\widehat k_0(\eta)|\le C_j(1+|\eta|)^{-j}$. Since $\widehat f=\widehat\psi_0*\widehat Q_M$ and $(1+|\zeta|/B)^{-j}\le(1+|\xi|/B)^{-j}(1+|\xi-\zeta|)^j$ for $B\ge1$, we get

$$
|\widehat f(\xi)|\le8|W|^2C_j\Bigl(1+\frac{|\xi|}B\Bigr)^{-j}\int|\widehat\psi_0(\eta)|(1+|\eta|)^j\,d\eta\le C_j'|W|^2\Bigl(\frac B{|\xi|}\Bigr)^j.
$$

Now we bound $\|f\|_\infty$ from below. Let $W\subset[T_0,T_0+T]$. If $|y-1|\le1/(4T)$, then $|\log y|\le1/(2T)$, and $|\Phi(y)|\ge\operatorname{Re}\bigl(y^{-iT_0}\Phi(y)\bigr)=\sum_{t\in W}\cos((t-T_0)\log y)\ge|W|\cos\tfrac12\ge|W|/\sqrt2$. As $\psi_0=\psi_2=1$ near $1$ and $k_0\ge2^{-20}$ on $[-1,1]$, integrating over $|y-1|\le\min(1/B,1/(4T))$ gives

$$
\|f\|_\infty\ge f(1)=Q_M(1)\ge2^{-20}|W|^2\min\left(1,\frac B{4T}\right).
$$

If $B\le4T$, then $|W|^2\le2^{22}(T/B)f(1)$, and for $j\ge1$, $(T/B)(B/|\xi|)^j=TB^{j-1}|\xi|^{-j}\le4^{j-1}(T/|\xi|)^j$. If $B>4T$, then $|W|^2\le2^{20}f(1)$ and $B=NM\le\Lambda$. In both cases the asserted bound holds for $j\ge1$. For $j=0$ it follows from $|\widehat f|\le\|f\|_1\le16\|f\|_\infty$. $\square$

**Corollary LV.30 (the energy form of the bound).** $\Sigma_3\preccurlyeq T^2|W|^{1/2}E(W)^{1/2}$.

**Proof.** Fix $\mathbf m\in\mathfrak M$. On $[1/2,2]$ the maps $\alpha_{\mathbf m}(v)=m_1/m_2+m_3/(m_2v)$ and $\beta_{\mathbf m}$ are monotone. Their derivatives satisfy $|\alpha_{\mathbf m}'(v)|=|m_3|/(|m_2|v^2)\ge1/8$ and $|\beta_{\mathbf m}'|=|m_1|/|m_2|\ge M_1/(2M)$. Hölder's inequality with exponents $2,4,4$ and these changes of variables give

$$
\int_{1/2}^2|\Phi|f(\beta_{\mathbf m})^{1/2}f(\alpha_{\mathbf m})^{1/2}\,dv\le\|\Phi\|_{L^2[1/2,2]}\left(8\|f\|_2^2\right)^{1/4}\left(\frac{2M}{M_1}\|f\|_2^2\right)^{1/4}\ll\Bigl(\frac M{M_1}\Bigr)^{1/4}|W|^{1/2}E(W)^{1/2}.
$$

Since $\mathfrak M$ has $O(M_1M^2)$ elements and $M_1\le M$, (LV.27) gives $\Sigma_3\preccurlyeq N^2M^2|W|^{1/2}E(W)^{1/2}$, and $NM\le T^{1+\kappa}$. $\square$

When $E(W)$ is close to its minimum $|W|^2$, this is as strong as square-root cancellation in $\Phi$ would give. For larger energies the next two sections improve the factor $T^2$ to $TN$ in front of $|W|^{1/2}E(W)^{1/2}$.

#### 10.1.8. Affine images of a sparse function

This section is self-contained. Fix a scale $\Lambda\ge2$ and a constant $C_0\ge2$, and put $C_1=12C_0$. For $1/2\le M\le\Lambda$ and a nonnegative function $f$ define

$$
\mathcal J_M(f)=\sup_{M_a,M_b,M_c\in[1/2,M]}\int_{\mathbb R}\Bigl(\sum_{|a|\sim M_a}\ \sum_{b\sim M_b}\ \sum_{|c|\le C_1M_c}f\Bigl(\frac{au+c}b\Bigr)\Bigr)^2du,
$$

where $a,b,c$ are integers and $b>0$. Applying Cauchy–Schwarz to the $O(M_aM_bM_c)$ terms and using $\int f((au+c)/b)^2\,du=(b/|a|)\|f\|_2^2$ gives the trivial bound

$$
\mathcal J_M(f)\ll M_aM_b^3M_c^2\|f\|_2^2\le M^6\|f\|_2^2\le\Lambda^2M^4\|f\|_2^2.
\tag{LV.31}
$$

The proposition below improves this when $f$ is sparse. Two examples show what to expect. If the images $(au+c)/b$ of a typical point $u$ behaved independently, the left side would be about $M^6\|f\|_1^2$. If $f$ is concentrated near rational numbers of small height, many images coincide, and the size $M^4\|f\|_2^2$ is attained.

**Proposition LV.32 (affine equidistribution).** Let $f$ be smooth and nonnegative, supported in $[1/C_0,C_0]$, and suppose that

$$
|\widehat f(\xi)|\le A_j\Bigl(\frac\Lambda{|\xi|}\Bigr)^j\|f\|_\infty\qquad(j\ge0,\ \xi\ne0).
$$

Then for every $\delta>0$ and $1/2\le M\le\Lambda$,

$$
\mathcal J_M(f)\le C\Lambda^\delta\left(M^6\|f\|_1^2+M^4\|f\|_2^2\right),
\tag{LV.33}
$$

with $C$ depending only on $\delta$, $C_0$ and the constants $A_j$.

The proof rests on one smoothing step. Fix a smooth even $\chi:\mathbb R\to[0,1]$ equal to one on $[-1,1]$ and supported in $[-2,2]$. For a function $f$ put

$$
\tilde f(u)=\Lambda\int_{\mathbb R}\chi\bigl(\Lambda(u-u')\bigr)f(u')\,du'.
$$

**Lemma LV.34 (one smoothing step).** Let $f$ satisfy the hypotheses of Proposition LV.32 with support in $[1/(2C_0),2C_0]$. Then for every $\delta>0$, all sufficiently large $\Lambda$ and $1/2\le M\le\Lambda$,

$$
\mathcal J_M(f)\le C\Lambda^\delta\left(M^6\|f\|_1^2+M^2\|f\|_2\,\mathcal J_M(\tilde f)^{1/2}\right),
\tag{LV.35}
$$

with $C$ depending only on $\delta$, $C_0$, $\chi$ and the constants $A_j$.

**Proof.** Both sides scale in the same way when $f$ is multiplied by a constant, so assume $\|f\|_\infty=1$. Let $\kappa=\delta/6$. All constants below may depend on $\kappa$, $C_0$, $\chi$ and the $A_j$. A term is called an error if it is $O_q(\Lambda^{20-\kappa q})$ for every $q$; this holds for each error term below after summing over the finitely many parameters. Fourier inversion and the hypothesis give

$$
|f'(x)|\le2\pi\int|\xi||\widehat f(\xi)|\,d\xi\le2\pi(A_0+2A_3)\Lambda^2.
$$

So $f\ge1/2$ on an interval of length $\gg\Lambda^{-2}$ around a point where $f=1$, and $\|f\|_1\gg\Lambda^{-2}$. Hence every error is at most $M^6\|f\|_1^2$ once $q$ is large.

Fix scales $M_a,M_b,M_c\in[1/2,M]$. Let $\phi$ be a smooth function, $0\le\phi$, equal to one on $[-C_1,C_1]$ and supported in $[-2C_1,2C_1]$. The inner sum is at most

$$
g(u)=\sum_{|a|\sim M_a}\sum_{b\sim M_b}\sum_{c\in\mathbb Z}\phi(c/M_c)\,f\Bigl(\frac{au+c}b\Bigr),
$$

a smooth compactly supported function, so the integral is at most $\int g^2=\int|\widehat g|^2$. In each term substitute $y=(au+c)/b$; then apply Poisson summation to the sum over $c$. The function $x\mapsto\phi(x/M_c)e(x\xi/a)$ has Fourier transform $\ell\mapsto M_c\widehat\phi(M_c(\ell-\xi/a))$. This gives

$$
\widehat g(\xi)=\sum_{|a|\sim M_a}F_a(\xi)\sum_{\ell\in\mathbb Z}M_c\,\widehat\phi\Bigl(M_c\Bigl(\ell-\frac\xi a\Bigr)\Bigr),\qquad F_a(\xi)=\sum_{b\sim M_b}\frac b{|a|}\widehat f\Bigl(\frac{b\xi}a\Bigr).
\tag{LV.36}
$$

Here $|F_a|\ll(M_b^2/M_a)\|f\|_1$ and $|\widehat\phi(\eta)|\ll_q(1+|\eta|)^{-q}$. Since $M_c\ge1/2$, the $\ell$-sum is $O(M_c)$ uniformly in $\xi/a$. Split the $\xi$-line into $\mathrm{I}:|\xi|\le4\Lambda^\kappa M_a/M_c$, $\mathrm{II}:4\Lambda^\kappa M_a/M_c<|\xi|\le\Lambda^3$ and $\mathrm{III}:|\xi|>\Lambda^3$.

*Range III.* Here $b/|a|\ge1/(4\Lambda)$, so $|b\xi/a|\ge|\xi|/(4\Lambda)\ge\Lambda^2/4$ and $|\widehat f(b\xi/a)|\le A_q(4\Lambda^2/|\xi|)^q$. Hence $|\widehat g(\xi)|\ll\Lambda^3A_q(4\Lambda^2/|\xi|)^q$, and $\int_{\mathrm{III}}|\widehat g|^2\ll_q\Lambda^{9-2q}$ is an error.

*Range I.* Here $|\xi/a|\le8\Lambda^\kappa$. The $\ell$ with $|\ell|\le16\Lambda^\kappa$ give $O(\Lambda^\kappa M_c)$. For the other $\ell$, $|\ell-\xi/a|\ge|\ell|/2$, and their terms total $O(1)$. So $|\widehat g(\xi)|\ll\Lambda^\kappa M_b^2M_c\|f\|_1$ and

$$
\int_{\mathrm I}|\widehat g|^2\ll\Lambda^{3\kappa}M_aM_b^4M_c\|f\|_1^2\le\Lambda^{3\kappa}M^6\|f\|_1^2.
$$

*Range II.* Call a pair $(a,\ell)$ near $\xi$ if $|\ell-\xi/a|<\Lambda^\kappa/M_c$, and far otherwise. The far pairs contribute $O_q(M_c\Lambda^{-\kappa(q-2)})$ to each $\ell$-sum. Their part of $\widehat g$ is therefore $O_q(\Lambda^{4-\kappa(q-2)})$, and its square integral over $|\xi|\le\Lambda^3$ is an error. For a near pair, $|a\ell-\xi|<|a|\Lambda^\kappa/M_c\le2M_a\Lambda^\kappa/M_c<|\xi|/2$. So $s=a\ell$ is a nonzero integer in an interval of length $4M_a\Lambda^\kappa/M_c$ around $\xi$, with $|s|<2\Lambda^3$. Each such $s$ has at most $2d(|s|)\ll\Lambda^\kappa$ factorizations $s=a\ell$, so there are $\ll\Lambda^{2\kappa}(1+M_a/M_c)$ near pairs. Apply Cauchy–Schwarz over the near pairs, use $|\widehat\phi|\le\|\phi\|_1$, and integrate over II:

$$
\int_{\mathrm{II}}|\widehat g_{\mathrm{near}}|^2\ll\Lambda^{2\kappa}(M_a+M_c)M_c\sum_{|a|\sim M_a}\sum_{\ell\in\mathbb Z}\int_{|\xi-a\ell|<|a|\Lambda^\kappa/M_c}|F_a(\xi)|^2\,d\xi.
$$

In the inner integral put $\xi=a\ell+a\tau/M_c$ with $|\tau|<\Lambda^\kappa$. Then $b\xi/a=b\ell+b\tau/M_c$, so $F_a(\xi)=|a|^{-1}G_\ell(\tau)$ with

$$
G_\ell(\tau)=\sum_{b\sim M_b}b\,\widehat f\Bigl(b\ell+\frac{b\tau}{M_c}\Bigr),
$$

which does not depend on $a$. Also $d\xi=(|a|/M_c)\,d\tau$. Since $\sum_{|a|\sim M_a}1/|a|\ll1$ and $M_a+M_c\le2M$,

$$
\int_{\mathrm{II}}|\widehat g_{\mathrm{near}}|^2\ll\Lambda^{2\kappa}M\sum_{\ell\in\mathbb Z}\int_{|\tau|<\Lambda^\kappa}|G_\ell(\tau)|^2\,d\tau.
\tag{LV.37}
$$

Put $\Lambda'=\Lambda^{1+2\kappa}$. If $|\ell|>\Lambda'/M_b$, then $|b\ell|>\Lambda'$ while $|b\tau/M_c|\le4M_b\Lambda^\kappa\le\Lambda'/2$. So $|b\ell+b\tau/M_c|\ge M_b|\ell|/2$ and $|G_\ell(\tau)|\ll M_b^2A_q(2\Lambda/(M_b|\ell|))^q$. These $\ell$ contribute an error. For the other $\ell$ we insert $\varphi_2(M_b\ell/\Lambda')$, where $\varphi_2\ge0$ is a fixed smooth function equal to one on $[-1,1]$ and supported in $[-2,2]$. Expand $|G_\ell|^2$ using $\widehat f(x)\overline{\widehat f(y)}=\iint f(u)f(u')e(yu'-xu)\,du\,du'$ (recall that $f$ is real):

$$
\sum_\ell\varphi_2\Bigl(\frac{M_b\ell}{\Lambda'}\Bigr)\int_{|\tau|<\Lambda^\kappa}|G_\ell(\tau)|^2d\tau=\sum_{b,b'\sim M_b}bb'\iint f(u)f(u')\,Z_1Z_2\,du\,du',
$$

where, with $x=b'u'-bu$,

$$
Z_1=\int_{|\tau|<\Lambda^\kappa}e(\tau x/M_c)\,d\tau,\qquad Z_2=\sum_{\ell\in\mathbb Z}\varphi_2\Bigl(\frac{M_b\ell}{\Lambda'}\Bigr)e(\ell x).
$$

Clearly $|Z_1|\le2\Lambda^\kappa$. By Poisson summation, $Z_2=(\Lambda'/M_b)\sum_{j\in\mathbb Z}\widehat\varphi_2((\Lambda'/M_b)(j-x))$. Put $\rho=M_b\Lambda^\kappa/\Lambda'\le\Lambda^{-\kappa}<1/2$. The terms with $|j-x|\ge\rho$ total $O_q((\Lambda'/M_b)\Lambda^{-\kappa(q-2)})$, which leads to an error. At most one $j$ has $|j-x|<\rho$, and for it $|\widehat\varphi_2|\le\|\varphi_2\|_1\le4$. Since the left side is nonnegative, we may bound it by the integral of $f(u)f(u')|Z_1||Z_2|$, and obtain, up to an error,

$$
\sum_\ell\varphi_2\int|G_\ell|^2\le8\Lambda^\kappa\frac{\Lambda'}{M_b}\sum_{b,b'\sim M_b}bb'\sum_{j\in\mathbb Z}\int f(u)\int_{|b'u'-bu-j|<\rho}f(u')\,du'\,du.
$$

The inner condition says $|u'-(bu+j)/b'|<\rho/b'\le\Lambda^{-1-\kappa}<1/\Lambda$. Since $\chi=1$ on $[-1,1]$, $\Lambda\int_{|u'-y|\le1/\Lambda}f(u')\,du'\le\tilde f(y)$. With $bb'\le4M_b^2$ and $\Lambda'/\Lambda=\Lambda^{2\kappa}$ we obtain

$$
\sum_\ell\varphi_2\int|G_\ell|^2\le32\Lambda^{3\kappa}M_b\int f(u)\sum_{b,b'\sim M_b}\sum_{j\in\mathbb Z}\tilde f\Bigl(\frac{bu+j}{b'}\Bigr)du+(\text{error}).
$$

For $\Lambda$ large, $\tilde f$ is supported in $[1/(4C_0),4C_0]$. So when $f(u)\ne0$, a nonzero term forces $|j|\le8C_0M_b\le C_1M_b$. By Cauchy–Schwarz in $u$, and since the sum over $b\sim M_b$ is part of a sum over $|a|\sim M_b$, the last integral is at most $\|f\|_2\,\mathcal J_M(\tilde f)^{1/2}$. Combining with (LV.37) and $M_b\le M$,

$$
\int_{\mathrm{II}}|\widehat g|^2\ll\Lambda^{5\kappa}M^2\|f\|_2\,\mathcal J_M(\tilde f)^{1/2}+(\text{error}).
$$

Adding the three ranges and taking the supremum over the scales gives (LV.35), since $5\kappa<\delta$. $\square$

**Proof of Proposition LV.32.** Let $0<\delta\le1$ and choose an integer $k\ge1$ with $2^{1-k}\le\delta/2$. For bounded $\Lambda$ the trivial bound (LV.31) suffices, so let $\Lambda$ be large. Put $c_\chi=\|\chi\|_1$, $h_0=f$ and $h_{i+1}=\tilde h_i/c_\chi$ for $0\le i<k$. Each $h_i$ is smooth and nonnegative with $\|h_i\|_1=\|f\|_1$ and $\|h_i\|_2\le\|f\|_2$, by the convolution inequalities of §10.1.2. Its support lies in $[1/C_0-4i/\Lambda,\,C_0+4i/\Lambda]\subset[1/(2C_0),2C_0]$. For $i\ge1$, $\widehat{h_i}(\xi)=\widehat{h_{i-1}}(\xi)\widehat\chi(\xi/\Lambda)/c_\chi$. Hence $|\widehat{h_i}(\xi)|\le\|f\|_1C_j(\Lambda/|\xi|)^j$, and $\|f\|_1=\|h_i\|_1\le2C_0\|h_i\|_\infty$. Therefore every $h_i$ satisfies the Fourier hypothesis, with constants $\max(A_j,2C_0C_j)$ independent of $i$.

Put $\mathcal B=M^6\|f\|_1^2+M^4\|f\|_2^2$ and $X_i=\mathcal J_M(h_i)/\mathcal B$. Lemma LV.34 with $\delta/8$ in place of $\delta$, the identity $\mathcal J_M(\tilde h_i)=c_\chi^2\mathcal J_M(h_{i+1})$ and $M^2\|f\|_2\le\mathcal B^{1/2}$ give

$$
X_i\le a\left(1+X_{i+1}^{1/2}\right)\qquad(0\le i<k),\qquad a=C\Lambda^{\delta/8}\ge1.
$$

The trivial bound (LV.31) gives $X_k\le C\Lambda^2$. If $X_{k-i}\le(2a)^{s_i}\max(1,X_k)^{2^{-i}}$ with $s_i=\sum_{l<i}2^{-l}$, then $X_{k-i-1}\le2a\max(1,X_{k-i})^{1/2}\le(2a)^{s_{i+1}}\max(1,X_k)^{2^{-i-1}}$. Hence

$$
X_0\le(2a)^2\left(C\Lambda^2\right)^{2^{-k}}\ll\Lambda^{\delta/4+2^{1-k}}\le\Lambda^{3\delta/4},
$$

which proves (LV.33). $\square$

#### 10.1.9. The refined bound for the three-frequency terms

**Proposition LV.38.** $\Sigma_3\preccurlyeq T^2|W|^{3/2}+TN|W|^{1/2}E(W)^{1/2}$.

**Proof.** Take $M_1,M,f=f_M$ from Lemma LV.26. By Cauchy–Schwarz in $v$, and then in the sum over $\mathbf m$,

$$
\sum_{\mathbf m\in\mathfrak M}\int_{1/2}^2|\Phi|f(\beta_{\mathbf m})^{1/2}f(\alpha_{\mathbf m})^{1/2}\,dv\le\|\Phi\|_{L^2[1/2,2]}\Bigl(\int_{1/2}^2S_\beta(v)^2dv\Bigr)^{1/4}\Bigl(\int_{1/2}^2S_\alpha(v)^2dv\Bigr)^{1/4},
$$

where $S_\beta=\sum_{\mathbf m\in\mathfrak M}f(\beta_{\mathbf m})$ and $S_\alpha=\sum_{\mathbf m\in\mathfrak M}f(\alpha_{\mathbf m})$. We apply the definitions of §10.1.8 with $C_0=16$, so $C_1=192$, scale $\Lambda=T^{1+\kappa}$, and $8M$ in place of $M$; here $8M\le8T^{1+\kappa}/N\le\Lambda$.

The set $\mathfrak M$ is invariant under $\mathbf m\mapsto-\mathbf m$, which leaves $\beta_{\mathbf m}$ and $\alpha_{\mathbf m}$ unchanged; so each of $S_\beta,S_\alpha$ is twice the sum over the $\mathbf m\in\mathfrak M$ with $m_2>0$. In $S_\beta$ the coordinates $m_1,m_2,m_3$ play the roles of $a,b,c$, with $|m_3|\le10M\le C_1M$, so $\int S_\beta^2\le4\mathcal J_{8M}(f)$. For $S_\alpha$ substitute $u=1/v$, so $dv\le4\,du$ on $[1/2,2]$ and $\alpha_{\mathbf m}(1/u)=(m_3u+m_1)/m_2$. Now $m_3,m_2,m_1$ play the roles of $a,b,c$. Split the range $M<|m_3|\le10M$ into the four ranges $|m_3|\sim2^iM$, $0\le i\le3$; the condition $|m_1|\le2M_1\le C_1M$ holds. Using $(\sum_{i=0}^3Y_i)^2\le4\sum Y_i^2$ we get $\int S_\alpha^2\le256\,\mathcal J_{8M}(f)$.

By Lemma LV.29, $f$ satisfies the hypotheses of Proposition LV.32. Hence $\mathcal J_{8M}(f)\preccurlyeq M^6|W|^2+M^4E(W)$, because $\Lambda^\delta\le T^{2\delta}$. With $\|\Phi\|_{L^2[1/2,2]}^2\ll|W|$ from Lemma LV.28, (LV.27) gives

$$
\Sigma_3\preccurlyeq\frac{N^2}M|W|^{1/2}\left(M^3|W|+M^2E(W)^{1/2}\right)=N^2M^2|W|^{3/2}+N^2M|W|^{1/2}E(W)^{1/2}.
$$

As $NM\le T^{1+\kappa}$ and $\kappa$ can be taken arbitrarily small, the proposition follows. $\square$

#### 10.1.10. Additive energy of a large-value set

**Proposition LV.39 (energy of a large-value set).** Let $T$ be large and $T^{3/4}\le N\le T$. Let $D(t)=\sum_{N<n\le2N}c_nn^{it}$ with $|c_n|\le1$, and let $W$ be a one-separated set in an interval of length $T$ with $|D(t)|\ge N^\sigma$ for every $t\in W$. Then

$$
E(W)\preccurlyeq|W|N^{4-4\sigma}+|W|^3N^{1-2\sigma}+|W|^{21/8}T^{1/4}N^{1-2\sigma}.
\tag{LV.40}
$$

**Lemma LV.41 (energy and a cubic moment).** Under the hypotheses of Proposition LV.39, without the restriction on $N$,

$$
E(W)\ll N^{-2\sigma}\sum_{N<n_1,n_2\le2N}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^3.
$$

**Proof.** Each quadruple counted by $E(W)$ has $|D(t_4)|\ge N^\sigma$, so $E(W)\le N^{-2\sigma}\sum|D(t_4)|^2$ over these quadruples. The frequencies $\log n$ of $D$ lie in an interval of length $\log2$, so by (LV.4), $|D(t_4)|^2\ll\int K_0(u\log2)|D(t_4+u)|^2\,du$. Write $t_4=s-x$ with $s=t_1+t_2-t_3$ and $|x|\le1$. Then

$$
\int K_0(u\log2)|D(s-x+u)|^2\,du\le\int K_1(y)|D(s+y)|^2\,dy,\qquad K_1(y)=\sup_{|x|\le1}K_0\bigl((y+x)\log2\bigr),
$$

and $K_1$ is integrable. Given $t_1,t_2,t_3$ there are at most three admissible $t_4$, so

$$
E(W)\ll N^{-2\sigma}\int K_1(y)\sum_{t_1,t_2,t_3\in W}|D(t_1+t_2-t_3+y)|^2\,dy.
$$

Expanding the square and summing over the points first gives

$$
\sum_{t_1,t_2,t_3\in W}|D(t_1+t_2-t_3+y)|^2=\sum_{n_1,n_2}c_{n_1}\overline{c_{n_2}}\Bigl(\frac{n_1}{n_2}\Bigr)^{iy}\Phi\Bigl(\frac{n_1}{n_2}\Bigr)^2\Phi\Bigl(\frac{n_2}{n_1}\Bigr).
$$

As $|c_n|\le1$ and $|\Phi(n_2/n_1)|=|\Phi(n_1/n_2)|$, this is at most $\sum_{n_1,n_2}|\Phi(n_1/n_2)|^3$. This is the step where the pointwise bound $|c_n|\le1$, rather than a bound for $\sum|c_n|^2$, is essential. $\square$

**Lemma LV.42 (discrete moments of $\Phi$).** Let $W$ be one-separated in an interval of length $T\ge3$, and let $1/2\le L\le T^{O(1)}$. Then

$$
\sum_{L<n_1,n_2\le2L}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^2\preccurlyeq|W|^2L+|W|L^2+|W|^{5/4}T^{1/2}L,
\tag{LV.43}
$$

$$
\sum_{L<n_1,n_2\le2L}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^4\preccurlyeq|W|^4L+E(W)L^2+E(W)^{3/4}|W|T^{1/2}L.
\tag{LV.44}
$$

**Proof.** If $L<1$, the only integer in $(L,2L]$ is $1$, and the sums are $|W|^2\le2L|W|^2$ and $|W|^4\le2L|W|^4$. Let $L\ge1$. Expanding $|\Phi(n_1/n_2)|^2=\sum_{t,t'}(n_1/n_2)^{i(t-t')}$ gives

$$
\sum_{n_1,n_2}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^2=\sum_{t,t'\in W}\Bigl|\sum_{L<n\le2L}n^{i(t-t')}\Bigr|^2,
$$

and Theorem 9.1 gives (LV.43).

For (LV.44) let $\nu(u)$, $u\in\mathbb Z$, be the number of pairs $(t,t')\in W^2$ with $\lfloor t-t'\rfloor=u$. Then $\sum_u\nu(u)=|W|^2$. If $\lfloor t_1-t_3\rfloor=\lfloor t_4-t_2\rfloor$, then $|t_1+t_2-t_3-t_4|<1$, so $\sum_u\nu(u)^2\le E(W)$. For $B$ running over the powers of two with $B\ge1/2$, let $U_B=\{u:B<\nu(u)\le2B\}$; only $O(\log T)$ of these sets are nonempty. Put $\Psi_B(x)=\sum_{u\in U_B}\sum_{\lfloor t-t'\rfloor=u}x^{i(t-t')}$, so that $|\Phi(x)|^2=\sum_B\Psi_B(x)$ and, by Cauchy–Schwarz, $|\Phi(x)|^4\ll\log T\sum_B|\Psi_B(x)|^2$. For fixed $B$, expanding the square gives

$$
\sum_{n_1,n_2}\Bigl|\Psi_B\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^2=\sum_{p,p'}\Bigl|P\bigl(d_p-d_{p'}\bigr)\Bigr|^2,\qquad P(\tau)=\sum_{L<n\le2L}n^{i\tau},
$$

where $p=(t,t')$ and $p'$ run over the pairs with $\lfloor t-t'\rfloor\in U_B$, and $d_p=t-t'$. Write $d_p=u+\theta$ with $u\in U_B$ and $0\le\theta<1$. Then the right side is at most $\sum_{u,u'\in U_B}\nu(u)\nu(u')\sup_{|\theta|\le1}|P(u-u'+\theta)|^2$. By (LV.4), $\sup_{|\theta|\le1}|P(\tau+\theta)|^2\ll\int K_1(y)|P(\tau+y)|^2\,dy$, with $K_1$ as in Lemma LV.41. For fixed $y$, $P(u-u'+y)=\sum_nn^{iy}n^{i(u-u')}$ has coefficients of modulus one. The set $U_B\subset\mathbb Z$ is one-separated and lies in $[-T-1,T]$, an interval of length $2T+1$. Theorem 9.1 therefore gives

$$
\sum_{n_1,n_2}\Bigl|\Psi_B\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^2\preccurlyeq B^2\left(|U_B|^2L+|U_B|L^2+|U_B|^{5/4}T^{1/2}L\right).
$$

Finally $B|U_B|\le|W|^2$ and $B^2|U_B|\le\sum\nu(u)^2\le E(W)$. Hence $B^2|U_B|^2\le|W|^4$, and $B^2|U_B|^{5/4}=(B^2|U_B|)^{3/4}(B|U_B|)^{1/2}\le E(W)^{3/4}|W|$. Summing over $B$ gives (LV.44). $\square$

In the next two lemmas $D_0=N^2/T$, and the pairs $(n_1,n_2)$ are split according to $d=\gcd(n_1,n_2)$. Write $n_1=dn_1'$, $n_2=dn_2'$, so that $|\Phi(n_1/n_2)|=|\Phi(n_1'/n_2')|$.

**Lemma LV.45 (pairs with a small common factor).** Under the hypotheses of Proposition LV.39,

$$
\sum_{\substack{N<n_1,n_2\le2N\\ \gcd(n_1,n_2)\le D_0}}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^3\ll N^2|W|^{1/2}E(W)^{1/2}+(\text{negligible}).
$$

**Proof.** Fix $d\le D_0$. The coprime pairs $n_1',n_2'\in(N/d,2N/d]$ give distinct fractions $q=n_1'/n_2'\in(1/2,2)$. Two of them differ by at least $d^2/(4N^2)$, so their logarithms differ by at least $d^2/(8N^2)$. The sum $x\mapsto\Phi(e^x)=\sum_{t\in W}e^{ixt}$ has its frequencies in an interval of length $T$. By (LV.4) and the case $(\int kF)^3\le(\int k)^2\int kF^3$ of Hölder's inequality,

$$
|\Phi(q)|^3\le\|K_0\|_1^2\,T\int_{\mathbb R}K_0\bigl(T(x-\log q)\bigr)|\Phi(e^x)|^3\,dx.
$$

For each $i\ge0$ and real $x$, at most $2+16N^2/(d^2T)$ of the numbers $\log q$ satisfy $i\le T|x-\log q|<i+1$. Since $K_0$ decays rapidly, $\sum_qTK_0(T(x-\log q))\ll T+N^2/d^2$. For $|x|\ge2$ we use instead that there are at most $4N^2$ fractions and $|x-\log q|\ge|x|/2$. Their contribution to the integral is $\ll_jN^2|W|^3T^{1-j}$, which is negligible. Hence

$$
\sum_q|\Phi(q)|^3\ll\Bigl(T+\frac{N^2}{d^2}\Bigr)\int_{-2}^2|\Phi(e^x)|^3\,dx+(\text{negligible}).
$$

By Cauchy–Schwarz and Lemma LV.28, applied in the variable $v=e^x$ with a bump that is at least $1/v$ on $[e^{-2},e^2]$, the integral is $\ll|W|^{1/2}E(W)^{1/2}$. Finally $\sum_{d\le D_0}(T+N^2/d^2)\le D_0T+2N^2=3N^2$. $\square$

**Lemma LV.46 (pairs with a large common factor).** Under the hypotheses of Proposition LV.39,

$$
\sum_{\substack{N<n_1,n_2\le2N\\ \gcd(n_1,n_2)>D_0}}\Bigl|\Phi\Bigl(\frac{n_1}{n_2}\Bigr)\Bigr|^3\preccurlyeq|W|^3N+|W|^{21/8}T^{1/4}N+E(W)^{1/2}|W|^{1/2}N^2.
$$

**Proof.** For $D_0<d\le2N$ drop the coprimality of $n_1',n_2'\in(N/d,2N/d]$. Here $N/d\ge1/2$. By Cauchy–Schwarz and Lemma LV.42 with $L=N/d$, the sum for one $d$ is $\preccurlyeq X_d^{1/2}Y_d^{1/2}$, with $E=E(W)$ and

$$
X_d=\frac{|W|^2N}d+\frac{|W|N^2}{d^2}+\frac{|W|^{5/4}T^{1/2}N}d,\qquad Y_d=\frac{|W|^4N}d+\frac{EN^2}{d^2}+\frac{E^{3/4}|W|T^{1/2}N}d.
$$

Apply Cauchy–Schwarz over $d$, using $\sum_{d\le2N}1/d\ll\log T$ and $\sum_{d>D_0}d^{-2}\le2/D_0=2T/N^2$. The sum is then

$$
\preccurlyeq\left(|W|^2N+|W|T+|W|^{5/4}T^{1/2}N\right)^{1/2}\left(|W|^4N+ET+E^{3/4}|W|T^{1/2}N\right)^{1/2}.
$$

Since $N\ge T^{3/4}\ge T^{1/2}$, the middle term of the first factor is at most the last one. By $E\le3|W|^3$, $E^{1/4}T^{1/2}\le3^{1/4}|W|^{3/4}T^{1/2}\le|W|N$, so the middle term of the second factor is at most the last one. So the sum is $\preccurlyeq(X_1+X_2)^{1/2}(Y_1+Y_2)^{1/2}$, with $X_1=|W|^2N$, $X_2=|W|^{5/4}T^{1/2}N$, $Y_1=|W|^4N$ and $Y_2=E^{3/4}|W|T^{1/2}N$. Now $\sqrt{X_1Y_1}=|W|^3N$ and $\sqrt{X_2Y_1}=|W|^{21/8}T^{1/4}N$. For the two products with $Y_2$ we use $E^{3/8}\le E^{1/2}|W|^{-1/4}$, from $E\ge|W|^2$. First,

$$
\sqrt{X_1Y_2}=|W|^{3/2}E^{3/8}T^{1/4}N\le E^{1/2}|W|^{1/2}N^2\cdot\frac{|W|^{3/4}T^{1/4}}N.
$$

If $|W|^{3/4}T^{1/4}\le N$, this is at most $E^{1/2}|W|^{1/2}N^2$. Otherwise $|W|^{3/4}>NT^{-1/4}\ge T^{1/2}$, so $|W|>T^{2/3}$. Then $E\le3|W|^3$ gives $\sqrt{X_1Y_2}\le3^{3/8}|W|^{21/8}T^{1/4}N$. Second,

$$
\sqrt{X_2Y_2}=|W|^{9/8}E^{3/8}T^{1/2}N\le E^{1/2}|W|^{1/2}N^2\cdot\frac{|W|^{3/8}T^{1/2}}N.
$$

If $|W|^{3/8}T^{1/2}\le N$, this is at most $E^{1/2}|W|^{1/2}N^2$. Otherwise $|W|^{3/8}>NT^{-1/2}\ge T^{1/4}$, so again $|W|>T^{2/3}$. Then $\sqrt{X_2Y_2}\le3^{3/8}|W|^{9/4}T^{1/2}N\le3^{3/8}|W|^3N$, because $|W|^{3/4}>T^{1/2}$. $\square$

**Proof of Proposition LV.39.** Lemmas LV.41, LV.45 and LV.46 give

$$
E(W)\preccurlyeq N^{-2\sigma}\left(N^2|W|^{1/2}E(W)^{1/2}+|W|^3N+|W|^{21/8}T^{1/4}N\right).
$$

If the first term dominates, then $E(W)^{1/2}\preccurlyeq N^{2-2\sigma}|W|^{1/2}$. Otherwise $E(W)\preccurlyeq N^{1-2\sigma}(|W|^3+|W|^{21/8}T^{1/4})$. In both cases (LV.40) holds. $\square$

For $T^{2/3}\le N\le T$ the same ingredients give a simpler bound. By Lemma LV.41, $|\Phi|\le|W|$ and (LV.43) with $L=N$,

$$
E(W)\preccurlyeq N^{-2\sigma}|W|\left(|W|^2N+|W|N^2+|W|^{5/4}T^{1/2}N\right)\preccurlyeq|W|^3N^{1-2\sigma}+|W|^2N^{2-2\sigma}.
$$

The term containing $T^{1/2}$ is absorbed because $|W|^{1/4}T^{1/2}\le|W|+N$. Indeed, $|W|^{1/4}T^{1/2}\le|W|$ if $|W|\ge T^{2/3}$, and $|W|^{1/4}T^{1/2}\le T^{2/3}\le N$ otherwise. In particular, if $\sigma>1/2$ and $E(W)\ge|W|^3T^{-\theta}$ with $0\le\theta<2(2\sigma-1)/3$, then $N^{1-2\sigma}\le T^{-2(2\sigma-1)/3}$ makes the first term too small, and $|W|\preccurlyeq T^\theta N^{2-2\sigma}$.

**Corollary LV.47.** In the setting of Proposition LV.6,

$$
\Sigma_3\preccurlyeq T^2|W|^{3/2}+T|W|N^{3-2\sigma}+T|W|^2N^{3/2-\sigma}+T^{9/8}|W|^{29/16}N^{3/2-\sigma}.
$$

**Proof.** The polynomial $D_N$ has coefficients $w(n/N)b_n$ of modulus at most one, supported in $(N,2N)$. Also $N=T^{5/6}\in[T^{3/4},T]$, so Proposition LV.39 applies to $W$. Insert (LV.40) into Proposition LV.38 and use $\sqrt{x+y+z}\le\sqrt x+\sqrt y+\sqrt z$. The three energy terms give $T|W|N^{3-2\sigma}$, $T|W|^2N^{3/2-\sigma}$ and $T^{9/8}|W|^{29/16}N^{3/2-\sigma}$. $\square$

#### 10.1.11. Proof of the core estimate

**Proof of Proposition LV.6.** By Lemmas LV.14 and LV.16, either $|W|\ll N^{2-2\sigma}$ or $|W|^3N^{6\sigma-3}\ll|\Sigma_2|+|\Sigma_3|+T^{-100}$. Proposition LV.20 with $k=4$ and Corollary LV.47 therefore give

$$
\begin{aligned}
|W|^3N^{6\sigma-3}\preccurlyeq{}&N^3+N^2|W|^2+TN|W|^{7/4}+N^2|W|^{29/16}T^{1/8}+T^2|W|^{3/2}\\
&+T|W|N^{3-2\sigma}+T|W|^2N^{3/2-\sigma}+T^{9/8}|W|^{29/16}N^{3/2-\sigma}.
\end{aligned}
$$

The left side is at most eight times the largest of the eight terms. Solving the corresponding inequality for $|W|$ in each case gives

$$
|W|\preccurlyeq N^{2-2\sigma},\ N^{5-6\sigma},\ \bigl(TN^{4-6\sigma}\bigr)^{4/5},\ \bigl(N^{5-6\sigma}T^{1/8}\bigr)^{16/19},\ T^{4/3}N^{2-4\sigma},\ T^{1/2}N^{3-4\sigma},\ TN^{9/2-7\sigma},\ T^{18/19}N^{(72-112\sigma)/19}.
$$

With $T=N^{6/5}$ these are powers of $N$ with the exponents

$$
\frac{10-10\sigma}5,\quad5-6\sigma,\quad\frac{104-120\sigma}{25},\quad\frac{412-480\sigma}{95},\quad\frac{18-20\sigma}5,\quad\frac{18-20\sigma}5,\quad\frac{57-70\sigma}{10},\quad\frac{468-560\sigma}{95}.
$$

Subtracting each from the target exponent $(18-20\sigma)/5$ leaves

$$
\frac{8-10\sigma}5,\quad\frac{10\sigma-7}5,\quad\frac{20\sigma-14}{25},\quad\frac{100\sigma-70}{95},\quad0,\quad0,\quad\frac{30\sigma-21}{10},\quad\frac{180\sigma-126}{95}.
$$

All are nonnegative for $7/10\le\sigma\le4/5$, including both endpoints. Hence $|W|\preccurlyeq N^{(18-20\sigma)/5}=TN^{(12-20\sigma)/5}$. No constant in the argument depends on $\sigma$. $\square$

#### 10.1.12. Proof of Theorem 10.1

**Lemma LV.48 (the classical bounds).** In the setting of Theorem 10.1:

1. if $N\ge T$, then $|W|\ll N^2V^{-2}$;
2. if $N<T$, then $|W|\preccurlyeq N^2V^{-2}+T\min\left(NV^{-2},N^4V^{-6}\right)$.

**Proof.** Let $D(t)=\sum_{N<n\le2N}b_nn^{it}$. For part 1, (LV.4) with $\Delta=\log2$ gives

$$
\sum_{t\in W}|D(t)|^2\ll\int_{\mathbb R}\Bigl(\sum_{t\in W}K_0\bigl((u-t)\log2\bigr)\Bigr)|D(u)|^2\,du.
$$

Since $W\subset[0,T]$ is one-separated and $K_0$ decays rapidly, the weight is $\ll(1+\operatorname{dist}(u,[0,T]))^{-2}$. Mean values, Theorem 2.1, applied to the coefficients $\overline{b_n}$, bounds the integral of $|D|^2$ over an interval of length $h$ by $h\sum|b_n|^2+6\pi\sum n|b_n|^2\le2Nh+24\pi N^2$. Applying this on $[-1,T+1]$ and on the unit intervals outside it gives $\sum_{t\in W}|D(t)|^2\ll N(T+N)\ll N^2$. Since $|D|\ge V$ on $W$, part 1 follows.

For part 2, the points $t+T$, $t\in W$, lie in $[T,2T]$, and $|D(t)|=|\sum_nc_nn^{-i(t+T)}|$ with $c_n=\overline{b_n}n^{iT}$. Lemma 2.1 with $Z=2N\le T^2$ gives $|W|V^2\ll(\log T)^3(TN+N^2)$, so $|W|\preccurlyeq(N^2+TN)V^{-2}$. Lemma 5.1 with $a_n=\overline{b_n}$, $G\le2N$ and $G_2\le\sum_{n\le2N}d(n)\le2N(1+\log2N)$ gives

$$
|W|V^2\ll N^2\ell+|W|^{2/3}T^{1/3}N^{4/3}\ell^{4/3},\qquad\ell=\log(2NT).
$$

If the first term dominates, $|W|\preccurlyeq N^2V^{-2}$. Otherwise $|W|^{1/3}V^2\ll T^{1/3}N^{4/3}\ell^{4/3}$, that is, $|W|\preccurlyeq TN^4V^{-6}$. Combining the two bounds gives part 2. $\square$

**Proof of Theorem 10.1.** Fix $\delta\in(0,1)$. Since $|\sum b_nn^{it}|\le N+1\le2N$, $W$ is empty if $V>2N$. For bounded $N$ or $T$ the theorem holds with a suitable constant, because $|W|\le T+1$ and $TN^{12/5}V^{-4}\ge TN^{-8/5}/16$. If $N\ge T$, part 1 of Lemma LV.48 gives (10.1). Let $N<T$.

Split $(N,2N]$ into $I_1=(N,3N/2]$ and $I_2=(3N/2,2N]$, and put $N_1=5N/6$, $N_2=10N/9$. Then $I_j\subset(N_j,2N_j]$. Since $[6N_1/5,9N_1/5]=[N,3N/2]$ and $[6N_2/5,9N_2/5]=[4N/3,2N]$, we have $w(n/N_j)=1$ for $n\in I_j$. So $D_j(t)=\sum_{n\in I_j}b_nn^{it}$ is the smoothed polynomial of Proposition LV.6 at length $N_j$, with coefficients $b_n\mathbf 1_{I_j}(n)$. At each $t\in W$ at least one of $|D_1(t)|,|D_2(t)|$ is at least $V/2$. Let $W_j$ be the set of those $t$ for which $|D_j(t)|\ge V/2$, and put $V_j=V/2$.

If $N_j\ge T$, part 1 of Lemma LV.48 gives $|W_j|\ll N^2V^{-2}$. If $N_j<T$ and $V_j\le N_j^{7/10}$, part 2 gives $|W_j|\preccurlyeq N_j^2V_j^{-2}+TN_jV_j^{-2}$, and $TN_jV_j^{-2}\le TN_j^{12/5}V_j^{-4}$. If $N_j<T$ and $V_j\ge N_j^{4/5}$, part 2 gives $|W_j|\preccurlyeq N_j^2V_j^{-2}+TN_j^4V_j^{-6}$, and $TN_j^4V_j^{-6}\le TN_j^{12/5}V_j^{-4}$. In these cases $|W_j|$ is bounded by the right side of (10.1).

There remains the case $N_j<T$ and $N_j^{7/10}<V_j<N_j^{4/5}$; write $V_j=N_j^{\sigma_j}$ with $7/10<\sigma_j<4/5$. Let $\eta=\delta/4$. Choose points of $W_j$ from left to right, each at distance at least $T^\eta$ from the previously chosen one. Each chosen point excludes at most $T^\eta+1$ later points, so the chosen set $W_j'$ satisfies $|W_j|\le3T^\eta|W_j'|$. Put $T_j=N_j^{6/5}$. As $N_j<T$, we have $T_j\le T^{6/5}$, so $W_j'$ is $T_j^{\eta/2}$-separated. Cover $[0,T]$ by at most $1+T/T_j$ consecutive intervals of length $T_j$. In each, Proposition LV.6, with separation exponent $\eta/2$ and $N_j,\sigma_j$ in place of $N,\sigma$, bounds the number of points of $W_j'$ by $\preccurlyeq T_jN_j^{(12-20\sigma_j)/5}=N_j^{18/5}V_j^{-4}$. Hence

$$
|W_j|\ll T^{2\eta}\left(1+\frac T{T_j}\right)N_j^{18/5}V_j^{-4}\ll T^{\delta/2}\left(N^{18/5}V^{-4}+TN^{12/5}V^{-4}\right),
$$

where the loss of Proposition LV.6 was taken at most $T_j^{\eta/2}\le T^\eta$. Adding the bounds for $W_1$ and $W_2$ proves (10.1). $\square$

### 10.2. Applying the new estimate to zeros

We give the density deduction directly from our balanced detector. In particular we do not need to import a separate unproved estimate for the second class of zeros in a different detector.

**Theorem 10.2.** For every $\epsilon>0$, uniformly for $7/10\le\sigma\le4/5$,

$$
N(\sigma,T)\ll_\epsilon
T^{15(1-\sigma)/(3+5\sigma)+\epsilon}.
\tag{10.7}
$$

Consequently, uniformly for $1/2\le\sigma\le1$,

$$
N(\sigma,T)\ll_\epsilon
T^{(30/13)(1-\sigma)+\epsilon}.
\tag{10.8}
$$

At $\sigma=3/4$, (10.7) has exponent $5/9$, whereas Ingham's exponent is $3/5$.

**Proof.** Take $\theta=\sigma$ in Lemma 6.2 and select one-separated zeros in $T<\gamma\le2T$. A selected zero belongs to a dyadic block $(N,2N]$, with
$T^{\eta/6}\le N\le T^{1/2+\eta/3}$ for sufficiently large $T$, on which the main value plus the weighted dual integral is at least $c/\log T$. The slight enlargement of the exponents absorbs the fixed constants and logarithms in $K$ and $U$. Write $R_N$ for a block's assigned count.

We explain how to keep the coefficient sequences fixed when removing the varying $\beta$. If $A_v(s)=\sum_{N<n\le2N}a_v(n)n^{-s}$, choose a smooth function $\psi_\beta(y)$ equal to $e^{(\theta-\beta)y}$ on $[0,\log2]$ and supported in a fixed larger interval. Its derivatives are uniformly bounded for $\theta\le\beta\le1$, so its Fourier transform is bounded by $C_A(1+|w|)^{-A}$, uniformly in $\beta$. Fourier inversion gives

$$
|A_v(\beta+i\gamma)|
\le C_A\int_{\mathbb R}(1+|w|)^{-A}
|A_v(\theta+i(\gamma+w))|\,dw.
\tag{10.9}
$$

The omitted factor $N^{\theta-\beta}$ is at most one. The index $v$ denotes the original dual integration variable; it is absent for the main polynomial. In either case the coefficients are independent of $\gamma,\beta$ and bounded by $C\sqrt{\log T}\,d(n)$.

Raise the detecting inequality to the power $2k$, use weighted Hölder in both $v$ and $w$, and sum over the selected zeros. For each fixed $v,w$, the points $\gamma+w$ remain one-separated. The polynomial $A_v(\theta+it)^k$ has coefficients bounded by $\log^C T\,d_{2k}(n)n^{-\theta}$ and support in $(N^k,2^kN^k]$. Split it into at most $k+1$ dyadic blocks, padding incomplete blocks by zero coefficients. For bounded $k$, the elementary divisor bound proved above, applied also to $d_{2k}$, makes these coefficient bounds $T^{o(1)}$. Its proof is the same prime-factor argument: $d_{2k}(p^\nu)=\binom{\nu+2k-1}{2k-1}$ grows polynomially in $\nu$.

Here is the moment form of (10.1) needed under the integrals. For such a block of length $Q\asymp_k N^k$, let $F(t)$ denote its polynomial with coefficients $c_n n^{-\theta}$. By normalizing coefficients, (10.1) gives, for $z>0$,

$$
\#\{j:|F(\gamma_j+w)|\ge z\}
\le T^{o(1)}
\left(Q^{2-2\theta}z^{-2}
+(Q^{18/5-4\theta}+TQ^{12/5-4\theta})z^{-4}\right).
$$

For $0<z\le z_0$ use the trivial bound $R_N$. For $z>z_0$ integrate the displayed estimate against $2z\,dz$ up to the trivial polynomial maximum. It follows that

$$
\sum_j|F(\gamma_j+w)|^2
\le R_Nz_0^2+
T^{o(1)}\left(
Q^{2-2\theta}
+(Q^{18/5-4\theta}+TQ^{12/5-4\theta})z_0^{-2}\right).
$$

The logarithm arising from the first integral is absorbed into $T^{o(1)}$. Choose $z_0$ to be a sufficiently small fixed multiple of $(c/\log T)^k$, taking account of the finite Hölder constants. All the integral weights have finite mass. The term involving $R_Nz_0^2$ can therefore be absorbed on the left of the detecting inequality. We obtain

$$
R_N\le T^{o(1)}
\left(N^{k(2-2\theta)}
+N^{k(18/5-4\theta)}
+TN^{k(12/5-4\theta)}\right).
\tag{10.10}
$$

The ordinary mean-value theorem, applied inside the same integrals, similarly gives

$$
R_N\le T^{o(1)}
\left(N^{k(2-2\theta)}+TN^{k(1-2\theta)}\right).
\tag{10.11}
$$

All estimates are uniform in $v,w$. For very large $|w|$, use the rapidly decreasing majorant in (10.9); a common translation of the sample points changes only coefficient phases, so no height restriction is lost. The dual coefficient bounds are uniform for every real $v$.

Let

$$
f(\theta)=\frac{15(1-\theta)}{3+5\theta},
\qquad
\alpha=\frac{f(\theta)}{18/5-4\theta}.
$$

Choose a bounded positive integer $k$ such that

$$
T^{10/(6+10\theta)}
\le N^k\le T^{15/(6+10\theta)}.
\tag{10.12}
$$

If $N\le T^{5/(6+10\theta)}$, take the least $k$ exceeding the lower threshold; its product is no more than the lower threshold times $N$. It is bounded in terms of $\eta$. Otherwise take $k=2$. The upper bound then holds for sufficiently small fixed $\eta$, because $15/(6+10\theta)\ge15/14>1$ throughout the stated range.

If $N^k\le T^\alpha$, (10.10) bounds all three terms by $T^{f(\theta)+o(1)}$: use respectively the upper bound in (10.12), the definition of $\alpha$, and the lower bound in (10.12), noting $12/5-4\theta<0$. If $N^k>T^\alpha$, use (10.11). Its first term is bounded by the same upper threshold. Its second is at most $T^{1+(1-2\theta)\alpha}$, and direct subtraction gives

$$
1+(1-2\theta)\alpha-f(\theta)
=-\frac{250(\theta-3/4)^2+3/8}
{2(3+5\theta)(9-10\theta)}<0.
$$

Thus $R_N\le T^{f(\theta)+o(1)}$. The number of dyadic blocks, the local zero multiplicities and the subdivision of height cost logarithms. First choose $\eta$ and all subpower losses sufficiently small in terms of the final $\epsilon$. Then sum the height ranges to prove (10.7).

For $\sigma\le7/10$, Ingham gives $3/(2-\sigma)\le30/13$. For $7/10\le\sigma\le4/5$, (10.7) has $15/(3+5\sigma)\le30/13$. For $\sigma\ge4/5$, Theorem 6.3 with $\eta=1/5$ has both coefficients at most $30/13$, since $11/5<30/13$ and $3/(3\sigma-1)\le15/7<30/13$. This proves the uniform (10.8). $\square$

**Corollary 10.3.** For every fixed $\theta>17/30$,

$$
\psi(x+h)-\psi(x)\sim h,\qquad
\pi(x+h)-\pi(x)\sim h/\log x
$$

uniformly for $x^\theta\le h\le x$.

**Proof.** Choose $A>30/13$ so close to $30/13$ that $\theta>1-1/A$. For $\sigma\le9/10$, take the error exponent in (10.8) smaller than $(A-30/13)/10$. It is then absorbed by $(A-30/13)(1-\sigma)$. For $\sigma\ge9/10$, Theorem 6.3 with $\eta=1/5$ gives the stronger uniform bound $N(\sigma,T)\ll T^{(11/5)(1-\sigma)}\log^B T$, since $3/(3\sigma-1)\le30/17<11/5$. Hence the whole strip satisfies a bound $T^{A(1-\sigma)}\log^B T$ with fixed $B$. Apply Theorem 4.1. This near-one step matters: a fixed additive $T^\epsilon$ loss cannot by itself be absorbed uniformly as $\sigma$ tends to one. $\square$

![Leading zero-density exponents and strict thresholds for prime intervals.](figures/NT-ZETA-19/density_intervals.png)

*Figure 1.* The left panel plots the powers in (3.1), (6.12) and (10.7), alongside the conjectural density-hypothesis power. At $\sigma=3/4$, the change is from $3/5$ to $5/9$. The right panel shows the strict thresholds from Corollaries 4.2, 7.2, 6.4 and 10.3 and Exercise 1. Logarithmic factors and arbitrary positive epsilon losses are omitted only in this comparison of leading powers. The density-hypothesis curve and its interval consequence are explicitly conditional. Original CC0 figure; its formulas and marked fractions are computed in the supplied figure source. The comparisons use the theorems proved in this lesson.

## 11. Maier's exceptional short intervals

We need one precise Dirichlet-function input. The written lesson The least prime in a progression: Linnik's theorem, Section 8, equation (8.12) and its proof, supplies Gallagher's estimate. For each sufficiently small fixed $b>0$, there are positive constants $a_b,K_b,C_b$ such that, if the primitive factors of modulus $q$ have no real zero greater than $1-b/\log q$, then

$$
\vartheta(x;q,r)=\frac{x}{\varphi(q)}
\left(1+O_b\left(e^{-a_b v}+v^2/q\right)\right),
\quad v=\frac{\log x}{\log q},\quad x\ge q^{K_b},
\tag{11.1}
$$

uniformly for $(r,q)=1$. The dependence on $b$ follows from the same proof there: use the classical zero-free width, decreased to $\min(b,c)\!/\log q$ up to height $q^{10}$, in its zero-sum estimate (8.5). Its log-free density theorem is Theorem 7.1. That written argument uses character, local analytic and sieve inputs and does not use Maier's theorem or the present lesson's later conclusions.

We also use the unique possible real exception in the product of characters modulo $q$, and its effective distance bound. Their written provider is *Zero-free regions and the exceptional zero*, Proposition 3.1 and Theorems 4.1–5.1, for the conductor-qualified unique simple real exception; its Lemma 6.1 and equation (6.4) give the effective analytic distance bound. Equation (6.4) uses the fully written analytic value bound in *Values of Dirichlet L-functions at $s=1$*, Theorem 4.1, and does not require the separate algebraic class-number input. The statements are: at most one primitive real character whose conductor divides $q$ can have a zero in $\beta>1-c/\log q$, and $1-\beta\gg f^{-1/2}\log^{-4}(2f)$ for its conductor $f$. The weaker logarithmic power here is the effective analytic bound used in Section 1 of the written Linnik lesson. Both required character statements and the analytic value-bound proof are present in those programme lessons. Our use keeps their full conductor conditions. No dependency on Maier or on the prime-interval conclusions of this section is involved.

### 11.1. Rough numbers and the Buchstab function

Let $\Phi(x,z)$ count positive integers at most $x$ having no prime factor at most $z$, including $1$. Define $\omega(u)=1/u$ on $1\le u\le2$, and then successively by

$$
u\omega(u)=1+\int_1^{u-1}\omega(v)\,dv\quad(u\ge2).
\tag{11.2}
$$

This defines a continuous positive function, with $(u\omega(u))'=\omega(u-1)$ for $u>2$.

**Lemma 11.1 (Buchstab).** As $z\to\infty$,

$$
\Phi(z^u,z)=\frac{z^u}{\log z}\bigl(\omega(u)+o(1)\bigr),
\tag{11.3}
$$

uniformly when $u$ belongs to a fixed compact subset of $(1,\infty)$.

**Proof.** Separating a composite integer by its least prime factor gives

$$
\Phi(x,z)=1+\pi(x)-\pi(z)
+\sum_{z<p\le\sqrt x}\bigl(\Phi(x/p,p^-)-1\bigr).
$$

The notation $p^-$ means that factors strictly smaller than $p$ are excluded. Replacing $p^-$ by $p$ loses at most $\sum_{p>z}x/p^2\ll x/z$ terms, those divisible by $p^2$. Dropping the subtracted ones costs at most $\pi(\sqrt x)$. Consequently

$$
\Phi(x,z)=\pi(x)-\pi(z)
+\sum_{z<p\le\sqrt x}\Phi(x/p,p)
+O(1+\sqrt x+x/z).
\tag{11.4}
$$

For $1<u\le2$, the sum is empty, and the prime number theorem proves (11.3) uniformly away from $u=1$.

First prove the auxiliary bound $\Phi(z^u,z)\ll_L z^u/\log z$ for $1\le u\le L$, for each fixed $L$. The base range follows from $\Phi(x,z)=1+\pi(x)-\pi(z)\le1+\pi(x)\ll x/\log z$. In (11.4), the new parameter $\log(x/p)/\log p$ is at most $u-1$. The inductive bound gives
$\Phi(x/p,p)\ll_L x/(p\log p)$. Partial summation from $\pi(t)\ll t/\log t$ gives
$\sum_{z<p\le\sqrt x}(p\log p)^{-1}\ll1/\log z$. The remainder in (11.4) is also $O_L(x/\log z)$ when $u\ge2$. This proves the auxiliary bound by successive unit ranges.

For the asymptotic induction, discard first the primes for which $1\le\log(x/p)/\log p\le1+\delta$. Their contribution, by the auxiliary bound and partial summation, is $O_L(\delta x/\log z)+o(x/\log z)$. On the remaining range the parameter lies in a compact subset of $(1,u-1]$, so the inductive error is uniformly $o(1)$ as $p\ge z\to\infty$. The prime number theorem, in Stieltjes partial summation, then gives

$$
\begin{aligned}
\sum_{z<p\le\sqrt x}\Phi(x/p,p)
&=\;x\int_z^{\sqrt x}
\frac{\omega(\log x/\log t-1)}{t\log^2t}\,dt
+o(x/\log z)\\
&=\frac{x}{\log x}\int_1^{u-1}\omega(v)\,dv
+o(x/\log z).
\end{aligned}
$$

For rigor at the discarded endpoint, first keep $\delta>0$ fixed, use the uniform PNT and the bounded piecewise continuously differentiable integrand, and then let $\delta\downarrow0$. The same procedure works uniformly on each fixed compact range of $u$. Since $\pi(z)=o(x/\log z)$ there, (11.4) and (11.2) give (11.3). $\square$

**Lemma 11.2 (oscillation of $\omega$).** The limit of $\omega(u)$ is $e^{-\gamma}$, and $\omega(u)-e^{-\gamma}$ takes both positive and negative values in every interval $[t-1,t]$, $t\ge2$.

**Proof.** The differential equation gives

$$
u\omega'(u)=\omega(u-1)-\omega(u)
=-\int_{u-1}^u\omega'(v)\,dv.
$$

Let $M_j=\sup_{j\le u\le j+1}|\omega'(u)|$ for integers $j\ge2$, using one-sided derivatives at $2$. For $j\ge3$ this identity implies
$M_j\le j^{-1}\max(M_{j-1},M_j)$, hence $M_j\le M_{j-1}/j$. Thus $\omega'$ is integrable at infinity, and $\omega$ has a finite limit $\ell$.

To identify it, put $F(s)=\int_1^\infty\omega(u)e^{-su}du$, $s>0$. Integration by parts in (11.2) gives
$sF'(s)=-e^{-s}(1+F(s))$. Since $F(s)\to0$ as $s\to\infty$,

$$
1+F(s)=\exp\left(\int_s^\infty e^{-v}\frac{dv}{v}\right).
$$

The constant in the integral at zero is $-\gamma$: integration by parts gives
$\int_s^\infty e^{-v}\log v\,dv=e^{-s}\log s+\int_s^\infty e^{-v}dv/v$, and its limit is $\Gamma'(1)=-\gamma$, proved in lesson three. It follows that $sF(s)\to e^{-\gamma}$. On the other hand, the existence of $\ell$ implies $sF(s)\to\ell$ by splitting off a bounded initial interval. Hence $\ell=e^{-\gamma}$.

For the strict oscillation, define for $u>-1$

$$
\xi_0(u)=\int_0^\infty
\exp\left(-(u+1)x+\int_0^x\frac{e^{-y}-1}{y}dy\right)dx.
$$

The inner integral lies strictly between $-x$ and $0$, so
$(u+2)^{-1}<\xi_0(u)<(u+1)^{-1}$. Differentiation and integration of the derivative of $x$ times the integrand give
$u\xi_0'(u-1)+\xi_0(u)=0$ for $u>0$; the exponential bounds justify both operations.

For $t>2$, differentiate
$\int_{t-1}^t\omega(u)\xi_0(u)du+t\omega(t)\xi_0(t-1)$.
The two delay equations make the derivative zero. Its limit at infinity is $\ell$, using the displayed bounds on $\xi_0$. The same calculation without $\omega$ gives
$\int_{t-1}^t\xi_0(u)du+t\xi_0(t-1)=1$. Subtracting $\ell$ times this equality yields

$$
\int_{t-1}^t(\omega(u)-\ell)\xi_0(u)du
+t(\omega(t)-\ell)\xi_0(t-1)=0.
\tag{11.5}
$$

Since the weights are positive, a constant weak sign on the whole interval would force $\omega=\ell$ throughout it. Such a constant unit interval is impossible: the delay equation would force the preceding unit interval to be constant too, and repeated descent reaches the range $1<u<2$, where $\omega(u)=1/u$. Therefore both signs occur. Continuity extends (11.5) to $t=2$, completing the proof. $\square$

### 11.2. A primorial with no exceptional factor

**Lemma 11.3.** There is a fixed $b>0$ and an unbounded sequence of primorials $q=\prod_{p\le z}p$ for which (11.1) holds.

**Proof.** Choose $2b<c$, where $c$ is the uniqueness constant in the stated character prerequisite, and decrease $b$ further as needed for (11.1). Write $q_n=\prod_{j\le n}p_j$. If arbitrarily large $q_n$ have no real exception in $\beta>1-b/\log q_n$, they already give the sequence.

Otherwise take bad $q_n$ tending to infinity, with exceptional conductor $f_n\mid q_n$ and zero $\beta_n$. The effective lower bound for $1-\beta_n$, together with $1-\beta_n<b/\log q_n\to0$, forces $f_n\to\infty$. Let $l$ be minimal with $f_n\mid q_l$. Then $l\to\infty$, and $f_n\nmid q_{l-1}$. The same zero lies within $b/\log q_l$ of one, because $q_l\le q_n$.

For large $l$, the PNT gives $\log q_l=\log q_{l-1}+\log p_l\le2\log q_{l-1}$. If $q_{l-1}$ had a real exception within $b/\log q_{l-1}$, its primitive conductor would differ from $f_n$, but both characters would occur modulo $q_l$ with zeros greater than $1-2b/\log q_l$. This contradicts uniqueness. Therefore the unbounded sequence $q_{l-1}$ has no such exception, and (11.1) applies to it. $\square$

### 11.3. Counting the matrix by columns and by rows

**Theorem 11.4 (Maier).** For every fixed $\lambda>1$,

$$
\liminf_{x\to\infty}
\frac{\pi(x+(\log x)^\lambda)-\pi(x)}
{(\log x)^{\lambda-1}}
<1<
\limsup_{x\to\infty}
\frac{\pi(x+(\log x)^\lambda)-\pi(x)}
{(\log x)^{\lambda-1}}.
\tag{11.6}
$$

Both inequalities hold already along integer starting points.

**Proof.** Choose $u>\lambda+1$ with $e^\gamma\omega(u)>1$, using Lemma 11.2. Let $q=\prod_{p\le z}p$ run through Lemma 11.3, set $X=q^A$ and $H=\lfloor(A\log q)^u\rfloor$, and fix $A>\max(2,K_b)$, to be made sufficiently large. Consider the integer matrix

$$
mq+j,\qquad X/q<m\le2X/q,\quad1\le j\le H.
\tag{11.7}
$$

Mark an entry if it is prime. A column with $(j,q)>1$ has no marked entries, since its integers exceed $q$. In every other column, (11.1) at $X$ and $2X$ gives

$$
\#\{\hbox{marked entries in column }j\}
=\frac{X}{\varphi(q)\log X}
\left(1+O_b(e^{-a_b A})+o(1)\right).
\tag{11.8}
$$

Moving either endpoint by $j\le H$ costs at most $O(H\log(3X))$ in prime weight, negligible relative to $X/\varphi(q)$ as $q\to\infty$. Dividing by $\log X$ incurs only relative $O(1/\log X)$, since the primes lie in $[X,2X+H]$. The $A^2/q$ error also tends to zero. Thus (11.8) is uniform in the columns.

There are $\Phi(H,z)$ reduced columns. The PNT gives $\log q=\vartheta(z)\sim z$, so $\log H/\log z\to u$. Lemma 11.1 and the Mertens product in lesson two, Theorem 3.1 and Solution 5, give

$$
\Phi(H,z)=\frac H{\log z}(\omega(u)+o(1)),
\qquad
\frac q{\varphi(q)}=e^\gamma\log z(1+o(1)).
$$

The number of rows is $X/q+O(1)$. Hence the average number of marks per row is

$$
\frac H{\log X}
\left(e^\gamma\omega(u)+O_b(e^{-a_b A})+o(1)\right).
\tag{11.9}
$$

Choose $A$ sufficiently large that the fixed error is less than one quarter of $e^\gamma\omega(u)-1$. For sufficiently large $q$, some row interval $(mq,mq+H]$ therefore contains at least $(1+\delta)H/\log X$ primes, for a fixed $\delta>0$.

Put $D_-=\lfloor(\log X)^\lambda\rfloor$. Partition that row into $\lfloor H/D_-\rfloor$ full consecutive intervals of length $D_-$, followed by a remainder. Its remainder contains at most $D_-+1$ primes, and this is $o(H/\log X)$ because $u>\lambda+1$. At least one full interval, starting at an integer $y$, contains at least $(1+\delta/2)D_-/\log X$ primes. Since $X\le y\le2X+H$, we have $\log y=\log X+O(1)$ and $(\log y)^\lambda\ge D_-$. Enlarge the interval to this prescribed length. Its denominator $(\log y)^{\lambda-1}$ is $(D_-/\log X)(1+o(1))$. This proves the strict upper inequality in (11.6).

For the lower inequality choose instead $u>\lambda+1$ with $e^\gamma\omega(u)<1$, and choose $A$ in the same way. A row then contains at most $(1-\delta)H/\log X$ primes. Put $D_+=\lceil(\log(2X+H))^\lambda\rceil$ and use its full consecutive subintervals of length $D_+$. Their count is $(1+o(1))H/D_+$, and their total primes are at most the row count; no estimate of the remainder is needed. One full subinterval therefore contains at most $(1-\delta/2)D_+/\log X$ primes. At its integer starting point $y$, shrink the length to $(\log y)^\lambda\le D_+$. Shrinking cannot increase the prime count, and $D_+/\log X=(\log y)^{\lambda-1}(1+o(1))$. This proves the strict lower inequality. Both chosen primorial sequences are unbounded, so the starting points tend to infinity. $\square$

Selberg's theorem concerns almost all starting points under RH. Maier's theorem produces exceptional sequences unconditionally. The two conclusions are compatible: an infinite exceptional sequence can have density zero.

## 12. Exercises with checked solutions

**Exercise 1 (easy).** Assume the density hypothesis: for every $\delta>0$, uniformly for $1/2\le\sigma\le1$,
$N(\sigma,T)\ll_\delta T^{2(1-\sigma)+\delta}$. Prove the prime number theorem in short intervals of length $x^\theta$ for every fixed $1/2<\theta<1$.

**Solution.** Fix a small $\kappa>0$. For $\sigma\le5/6$, apply the hypothesis with $\delta=\kappa/6$. Since $1-\sigma\ge1/6$, this gives $N(\sigma,T)\ll_\kappa T^{(2+\kappa)(1-\sigma)}$. For $\sigma\ge5/6$, apply Theorem 6.3 with $0<\eta<\min(\kappa,1/4)$. Its first exponent is at most $(2+\kappa)(1-\sigma)$, and its second has $3/(3\sigma-1)\le2$. Thus a single fixed logarithmic exponent $B_\kappa$ gives

$$
N(\sigma,T)\ll_\kappa
T^{(2+\kappa)(1-\sigma)}\log^{B_\kappa}(2T)
$$

throughout the strip. Choose $\kappa$ so small that $1-1/(2+\kappa)<\theta$. Theorem 4.1 yields
$\psi(x+x^\theta)-\psi(x)\sim x^\theta$ and
$\pi(x+x^\theta)-\pi(x)\sim x^\theta/\log x$.
This covers, in particular, every $\theta>1/2+\epsilon$ for a prescribed $\epsilon>0$. The near-one estimate is necessary: taking a single fixed $\delta$ in the density hypothesis does not produce the required uniform exponent as $\sigma\to1$.

**Exercise 2 (medium).** Prove that a uniform bound
$N(\sigma,T)\ll T^{A(1-\sigma)}\log^B(2T)$, with fixed $A\ge2$, implies the prime number theorem in every interval $[x,x+h]$ with $x^\theta\le h\le x$ and $\theta>1-1/A$.

**Solution.** The case $\theta=1$ follows from the ordinary PNT, and $\theta>1$ gives an empty stated range. For $\theta<1$, choose $\eta>0$ so that $p=1-\theta+\eta<1/2$ and $Ap<1$, and use the sharp explicit formula with $T=x^p$. Its two endpoint remainders, divided by $h$, are
$O(x^{-\eta}\log^2x+\log x/h)=o(1)$. The difference of each zero term is $\int_x^{x+h}u^{\rho-1}du$, bounded by $h x^{\beta-1}$. The zeros with $\beta\le1/2$ contribute, after division by $h$, at most
$x^{-1/2}N(T)\ll x^{p-1/2}\log x=o(1)$.

For $\beta>1/2$, write
$x^{\beta-1}=x^{-1/2}+(\log x)\int_{1/2}^{\beta}x^{u-1}du$ and sum. The required bound is

$$
x^{-1/2}N(1/2,T)+
(\log x)\int_{1/2}^1 x^{u-1}N(u,T)\,du.
$$

The Vinogradov–Korobov region cuts off the integral at $1-\delta_T$, where

$$
\delta_T\gg(\log T)^{-2/3}(\log\log T)^{-1/3}.
$$

The density bound and $m=1-Ap>0$ bound the integral term by

$$
(\log x)\log^B(2T)
\int_{1/2}^{1-\delta_T}x^{-m(1-u)}du
\le \frac{\log^B(2T)}m\,x^{-m\delta_T}=o(1).
$$

The last assertion follows because $\delta_T\log x$ grows faster than $\log\log x$. This proves $\psi(x+h)-\psi(x)=h(1+o(1))$, uniformly in $h$. The proper prime powers have total weight $O(\sqrt x)=o(h)$ on $[x,2x]$, so the same holds for the prime-weight sum. Every prime in the interval has $\log p=\log x+O(1)$; dividing by $\log x$ proves the assertion for $\pi$.

**Exercise 3 (medium).** Deduce a prime strictly between each pair of sufficiently large consecutive cubes from the interval theorem with every $\theta>7/12$.

**Solution.** Choose, for example, $\theta=5/8$, which lies strictly between $7/12$ and $2/3$. Put $x=n^3$ and $h=(n+1)^3-n^3=3n^2+3n+1$. For sufficiently large $n$, $x^\theta\le3x^{2/3}\le h\le x$. Corollary 6.4 gives

$$
\pi((n+1)^3)-\pi(n^3)
\sim\frac{3n^2+3n+1}{3\log n}.
$$

The right side tends to infinity, so the difference is positive. Both endpoints are composite when $n\ge2$. Thus the counted prime is strictly between them. This argument uses the uniform version for $h\ge x^\theta$; it does not identify the cube interval's length with $x^\theta$.

**Exercise 4 (hard).** Assuming LH, prove the density hypothesis using the exponential zero detector and mean-value estimates.

**Solution.** Fix $0<\epsilon<1$; larger error exponents follow by weakening this bound. If $\sigma\le1/2+\epsilon/4$, the total zero count already gives
$N(\sigma,T)\ll T\log(2T)\ll_\epsilon T^{2(1-\sigma)+\epsilon}$. Suppose instead $\sigma>1/2+\epsilon/4$. Repeat the proof of Lemma 1.1 with $X=\lfloor T\rfloor$ and $Y=T$. The displacement of the gamma contour is bounded away from its pole by $\epsilon/4$, so the constants depend only on $\epsilon$. The truncation length is $Z=\lceil T\log^2 T\rceil$.

For a one-separated set of zeros in $T<\gamma\le2T$, the polynomial alternative, partial summation from $\beta$ to $\sigma$, and Lemma 2.1 give

$$
R_1\ll_\epsilon
(\log T)^3
\left(T\sum_{n>X}d(n)^2n^{-2\sigma}e^{-2n/T}
+\sum_{n>X}d(n)^2n^{1-2\sigma}e^{-2n/T}\right)
\ll_\epsilon T^{2(1-\sigma)}\log^C T.
$$

For the integral alternative, LH gives
$|\zeta(1/2+iu)|\ll_\epsilon(1+|u|)^{\epsilon/4}$. Square the detecting inequality and use weighted Cauchy–Schwarz. Its sum over the integral-class points is bounded by

$$
C_\epsilon T^{1-2\sigma+\epsilon/2}
\int_{\mathbb R}e^{-|v|/2}
\sum_j|M_X(1/2+i(\gamma_j+v))|^2\,dv.
$$

The polynomial factor $(1+|v|)^{\epsilon/2}$ has been absorbed into the weaker exponential weight. For each fixed $v$ the points are still one-separated, in an interval of length $T$. Sampling and the polynomial mean-value theorem bound the inner sum by

$$
C\left(T\sum_{d\le X}d^{-1}+\sum_{d\le X}1\right)
\log^C T\ll T\log^{C+1}T.
$$

Thus $R_2\ll_\epsilon T^{2(1-\sigma)+\epsilon/2}\log^C T$. Local multiplicities and the dyadic height sum cost only further logarithms, which fit in the remaining $\epsilon/2$ for sufficiently large $T$; enlarge the constant for bounded $T$. This proves the uniform density hypothesis. No part of this proof assumes RH; LH supplies only the stated bound on critical-line values. The same implication was proved in lesson eighteen, Theorem 6.2, and the present calculation exhibits the detector's two classes explicitly.

**Exercise 5 (hard).** Prove Ingham's estimate in full for $1/2\le\sigma\le3/4$.

**Solution.** If $\sigma\le1/2+1/\log T$, use the total zero count. With
$f(\sigma)=3(1-\sigma)/(2-\sigma)$, one has $f(\sigma)\ge1-C/\log T$ on this range, so $T\log T\ll T^{f(\sigma)}\log^{16}(2T)$.

For the other values use Lemma 1.1 with

$$
X=\lfloor T\rfloor,\qquad
Y=T^{3/(4-2\sigma)}.
$$

This lies between $T$ and $T^{6/5}$ on the required range. The proof of Lemma 2.1, using disjoint sample intervals and binary partial sums, together with the divisor square bound, gives

$$
R_1\ll\log^7(2T)
\left(Y^{2-2\sigma}+T^{2-2\sigma}\right).
$$

For integral-class zeros, raise the detecting inequality to the power $4/3$ and use weighted Hölder. At each integration variable, the critical-line zeta fourth moment at one-separated points is $O(T\log^5(2T))$, by lesson sixteen, Corollary 6.2. The mollifier second moment there is $O(T\log^2(2T))$. Hölder over the points therefore gives

$$
R_2\ll
Y^{(2-4\sigma)/3}
\left(T\log^5(2T)\right)^{1/3}
\left(T\log^2(2T)\right)^{2/3}
\log^{4/3}(2T)
\ll T Y^{(2-4\sigma)/3}\log^5(2T).
$$

The exponential integration tails are handled as in Section 2 by the polynomial growth bound; the displayed logarithmic exponent includes the detector's $1/\log T$ distance from the gamma pole.

The choice of $Y$ makes the two leading powers equal:

$$
Y^{2-2\sigma}
=TY^{(2-4\sigma)/3}
=T^{3(1-\sigma)/(2-\sigma)}.
$$

Also $2-2\sigma\le3(1-\sigma)/(2-\sigma)$, so the remaining polynomial term is weaker. Every unselected zero is within distance one of a selected one and the local zero count is $O(\log T)$, including multiplicities. Hence
$N(\sigma,2T)-N(\sigma,T)\ll T^{f(\sigma)}\log^8(2T)$, with room in the logarithmic exponent for all sampling factors. In this range $f(\sigma)\ge3/5$, so summing dyadic heights is a uniformly convergent geometric sum times the stated logarithmic bound. The final, deliberately generous exponent $16$ gives

$$
N(\sigma,T)\ll
T^{3(1-\sigma)/(2-\sigma)}\log^{16}(2T).
$$

This includes the boundary $\sigma=1/2$, all multiplicities and the bounded initial heights.

## 13. Proof scope and references

The zero detectors, discrete sampling and divisor norms, both Ingham estimates, the classical large-value bound, the smoothing-kernel inversion and balanced Huxley detector, the uniform $12/5$ consequence and primes between consecutive cubes, Selberg's RH variance and almost-all theorem, Heath-Brown's difference-set estimate, the balanced-detector Guth–Maynard density application, and the Buchstab and Maier matrix arguments are supplied with proofs. Section 10.1 supplies complete proofs of the matrix, reflection, affine-equidistribution, energy and assembly steps of the Guth–Maynard argument, with exact internal providers for the reused facts.

The exact Dirichlet-function support for Maier is identified at the start of Section 11: the written Gallagher estimate in the programme's Linnik lesson, and the written classical exception in *Zero-free regions and the exceptional zero*, Proposition 3.1 and Theorems 4.1–5.1, and its independently analytic effective distance bound (6.4), based on Lemma 6.1 and *Values of Dirichlet L-functions at $s=1$*, Theorem 4.1. The Dirichlet-function proof used here does not depend on Maier, so this is an acyclic mathematical dependency. These character facts are taught by their owning course. The density hypothesis is a conjecture; Exercises 1 and 4 identify the additional assumptions under which their deductions hold.

- Larry Guth and James Maynard, [*New large value estimates for Dirichlet polynomials*, arXiv:2405.20552v2](https://arxiv.org/pdf/2405.20552v2), 7 April 2026. Theorem 10.1 is their Theorem 1.1, proved in Section 10.1 along the lines of their §§3–12; Theorem 10.2 contains their zero-density estimate, Theorem 1.2; the exponent $17/30$ of Corollary 10.3 is their Corollary 1.3.
