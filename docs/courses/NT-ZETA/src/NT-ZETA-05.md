# Entire functions of order one and the Hadamard product of xi

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An entire function can contain information in two ways: through its zeros and through a zero-free exponential factor. Growth restricts the second possibility. We will prove that for order at most one, the exponential factor has an affine exponent. Applied to the completed zeta function, this converts the zeros into a convergent product and then into the partial fractions that drive prime-counting arguments.

We use the entire function $\xi$, its symmetries, the location of its zeros and its theta integral proved in Poisson summation, theta, and the functional equation, Theorems 3.1–3.3. We use Stirling and the gamma logarithmic derivative from The Gamma function and Stirling's formula, Theorem 3.1 and Proposition 5.1. Cauchy's formula, harmonic mean values, the maximum principle and holomorphic logarithms on simply connected domains come from [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). Free comparison sources are McMullen’s 2023 lecture notes and the Wilkins transcription of Riemann’s memoir listed below. The factorization proof below includes its growth estimate for the quotient; that estimate cannot be inferred merely by dividing two entire functions of finite order.

For a nonconstant entire function $f$, write
$$
M_f(r)=\max_{|z|=r}|f(z)|,\qquad
\rho(f)=\limsup_{r\to\infty}\frac{\log\log M_f(r)}{\log r}.
\tag{1}
$$
For sufficiently large $r$, the double logarithm is defined. Constants have order zero by convention. Thus order at most one means that, for every $\eta>0$,
$$
\log M_f(r)\le C_\eta r^{1+\eta}\quad(r\ge1).
\tag{2}
$$
Order one does not assert a bound $\log M_f(r)=O(r)$; that stronger condition is finite exponential type. Polynomials have order zero.

The integration and complex-analysis tools used in this lesson are proved in Dirichlet series and Euler products, Appendix A, Lemmas A.1–A.4.

## Averaging the logarithm counts zeros

**Theorem 1.1 (Jensen's formula).** Suppose $f$ is holomorphic on a neighbourhood of $|z|\le R$, $f(0)\ne0$, and $f$ has no zero on $|z|=R$. List its zeros $a_j$ in $|z|<R$ with multiplicity. Then
$$
\log|f(0)|+\sum_{|a_j|<R}\log\frac R{|a_j|}
=\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta.
\tag{3}
$$

**Proof.** Factor $f(z)=g(z)\prod_j(z-a_j)$ in the disk. The function $g$ is holomorphic and nonzero there, so $\log|g|$ is harmonic and its boundary average is $\log|g(0)|$. For $|a|<R$, the convergent series for $\log(1-(a/R)e^{-i\theta})$ has zero average. Consequently the average of $\log|Re^{i\theta}-a|$ is $\log R$. Add the means of the factors and use $|f(0)|=|g(0)|\prod_j|a_j|$. $\square$

If $f$ vanishes to order $m$ at zero, apply (3) to $f(z)/z^m$; this is how the origin zero is accounted for. Let $n_f(r)$ count the other zeros with $|a_j|\le r$. When $f(0)\ne0$, (3) gives
$$
n_f(r)\log2\le\log M_f(2r)-\log|f(0)|.
\tag{4}
$$
If $2r$ is a zero modulus, first use zero-free radii decreasing to $2r$ and then continuity of $M_f$. Every zero with $|a_j|\le r$ contributes at least $\log2$ in this limit. Applying the same argument to $f/z^m$ proves the corresponding estimate in the general case.

**Corollary 1.2.** If $f\not\equiv0$ has finite order $\rho$, then for every $\eta>0$,
$$
n_f(r)=O_\eta(r^{\rho+\eta}),\qquad
\sum_j|a_j|^{-\rho-\varepsilon}<\infty
\quad(\varepsilon>0).
\tag{5}
$$

**Proof.** The first bound follows from (4) and the definition of order; removing the finite origin factor does not increase order. For the second, take $\eta=\varepsilon/2$ and split the zeros of modulus at least one into $2^k\le|a_j|<2^{k+1}$. Their contribution is at most
$C_\eta2^{(k+1)(\rho+\eta)}2^{-k(\rho+\varepsilon)}$, a convergent geometric series. The remaining nonzero zeros form a finite set. $\square$

## Controlling a holomorphic function by its real part

The next estimate will turn an upper bound for a logarithm's real part into bounds for all its Taylor coefficients.

**Theorem 2.1 (Borel–Carathéodory).** Suppose $h$ is holomorphic on a neighbourhood of $|z|\le R$, $h(0)=0$, and $\Re h\le M$ on $|z|=R$. Then $M\ge0$ and
$$
\max_{|z|\le r}|h(z)|\le\frac{2rM}{R-r}
\quad(0<r<R).
\tag{6}
$$
For every integer $k\ge1$,
$$
|h^{(k)}(0)|\le\frac{2k!M}{R^k}.
\tag{7}
$$
More generally, for $|z|\le r<q<R$,
$$
|h^{(k)}(z)|\le
\frac{k!}{(q-r)^k}\frac{2qM}{R-q}.
\tag{8}
$$

**Proof.** The real part has mean zero on the boundary, so $M\ge0$. The harmonic maximum principle gives $\Re h\le M$ inside. If $M=0$, the real part attains its maximum at zero and is constant; then $h=0$. Suppose $M>0$. The function
$$
w(z)=\frac{h(z)}{2M-h(z)}
$$
is holomorphic, satisfies $w(0)=0$, and has modulus at most one, since
$|2M-h|^2-|h|^2=4M(M-\Re h)\ge0$. Schwarz's lemma in the radius-$R$ disk gives $|w(z)|\le|z|/R$. Inverting this expression gives $h=2Mw/(1+w)$ and proves (6).

For (7), write $h(z)=\sum_{k\ge1}c_kz^k$ and $u(\theta)=\Re h(Re^{i\theta})$. Fourier coefficient extraction gives
$$
c_kR^k=2\frac1{2\pi}\int_0^{2\pi}u(\theta)e^{-ik\theta}d\theta
=-2\frac1{2\pi}\int_0^{2\pi}(M-u(\theta))e^{-ik\theta}d\theta.
$$
The nonnegative function $M-u$ has average $M$, so $|c_k|R^k\le2M$. Multiplication by $k!$ proves (7). Finally, (6) bounds $h$ on the radius-$q$ disk; apply Cauchy's derivative estimate on a circle of radius $q-r$ centred at the given point to obtain (8). $\square$

For a general $h(0)$, apply this theorem to $h-h(0)$ with $M$ replaced by the boundary supremum of $\Re h-\Re h(0)$.

## A canonical product and the remaining exponential

Put $E_1(w)=(1-w)e^w$. Its logarithm near zero satisfies
$$
\log E_1(w)=-\sum_{k=2}^\infty\frac{w^k}{k},
\qquad |\log E_1(w)|\le C|w|^2\quad(|w|\le1/2).
\tag{9}
$$
By (5), the nonzero zeros of a function of order at most one satisfy $\sum_j|a_j|^{-2}<\infty$. Therefore
$$
P(z)=\prod_jE_1(z/a_j)
\tag{10}
$$
converges locally uniformly: on a fixed compact set, all but finitely many factors can be treated with (9). It is entire, has the specified zeros with their multiplicities, and has no additional zeros, because every nonvanishing tail is the exponential of a convergent logarithmic series. Finite and empty products are allowed.

**Lemma 3.1 (circles avoiding zeros).** Suppose the discrete nonzero sequence $a_j$ satisfies $n(r)=O_\eta(r^{1+\eta})$ for every $\eta>0$. For each fixed $0<\eta<1$ and every sufficiently large $r$, there exists $R\in[r,2r]$ such that the product (10) satisfies
$$
\log|P(z)|\ge-C_\eta r^{1+2\eta}
\quad(|z|=R).
\tag{11}
$$

**Proof.** Exclude the intervals of radius $r^{-2}$ about the numbers $|a_j|\le4r$. Their total length is at most
$2r^{-2}n(4r)=O_\eta(r^{-1+\eta})<r$. Some $R\in[r,2r]$ remains outside them. Hence for $|z|=R$ and $|a_j|\le4r$,
$$
|z-a_j|\ge\bigl||z|-|a_j|\bigr|\ge r^{-2},
\qquad |1-z/a_j|\ge\frac1{4r^3}.
$$
Consequently this part of the product has logarithm at least
$$
-n(4r)\log(4r^3)-2r\sum_{|a_j|\le4r}|a_j|^{-1}.
\tag{12}
$$
There is a positive lower bound for the moduli of the nonzero $a_j$. Summation by parts and the counting estimate give
$$
\sum_{|a_j|\le4r}|a_j|^{-1}=O_\eta(r^\eta),
\qquad
\sum_{|a_j|>4r}|a_j|^{-2}=O_\eta(r^{-1+\eta}).
\tag{13}
$$
For instance the first sum is its endpoint term $n(4r)/(4r)$ plus the integral of $n(u)/u^2$ from that positive lower bound to $4r$, up to a fixed lower endpoint term. For the second, integrate $2n(u)/u^3$ from $4r$ to infinity and subtract the lower endpoint term; convergence uses $\eta<1$.

For $|a_j|>4r$, $|z/a_j|\le1/2$, so (9) bounds the absolute sum of tail logarithms by $Cr^2\sum_{|a_j|>4r}|a_j|^{-2}=O_\eta(r^{1+\eta})$. Equations (12)–(13) bound the head from below by $-C_\eta r^{1+\eta}\log r$. Since $\log r=O_\eta(r^\eta)$, these bounds give (11). $\square$

**Theorem 3.2 (Hadamard factorization, order at most one).** If $f\not\equiv0$ is entire of order at most one and vanishes to order $m\ge0$ at zero, then
$$
f(z)=z^m e^{A+Bz}\prod_j(1-z/a_j)e^{z/a_j},
\tag{14}
$$
where $a_j$ are its nonzero zeros with multiplicity. The product is locally uniformly convergent and independent of its ordering. The zero-free factor has an affine exponent.

**Proof.** Corollary 1.2 constructs the product (10) and gives the hypotheses of Lemma 3.1. The quotient $f/(z^mP)$ has removable singularities at every zero, and is entire and nonzero. It therefore equals $e^{h(z)}$ for an entire $h$.

Fix $0<\eta<1/4$. On the circles in Lemma 3.1, (2) and (11) give
$$
\Re h(z)=\log|f(z)|-m\log R-\log|P(z)|
\le C_\eta r^{1+2\eta}.
$$
The harmonic maximum principle gives this bound on the enclosed disk. Apply (6) to $h-h(0)$ on that disk and then Cauchy's estimate on its radius-$R/2$ circle. For each $k\ge2$ this bounds the $k$th Taylor coefficient by
$C_{\eta,k}r^{1+2\eta-k}$. Letting $r\to\infty$ forces that coefficient to vanish, since $1+2\eta<2$. Thus $h=A+Bz$.

The tail logarithms in (9) are absolutely summable on compact sets, so permuting them does not change the product. This establishes the convergence assertion as well as the factorization. $\square$

The origin factor in (14) is essential: $f(z)=z$ cannot be represented by a nonvanishing exponential and a product over nonzero zeros alone. The genus-one factors used here are always sufficient for order at most one. A lower genus may suffice for a particular zero set.

**Corollary 3.3.** If in addition $\sum_j|a_j|^{-1}<\infty$, then $f$ has finite exponential type: there exist $C_0,C_1>0$ with
$$
|f(z)|\le C_0e^{C_1|z|}\quad(z\in\mathbb C).
\tag{15}
$$

**Proof.** For every complex $w$, $|E_1(w)|\le(1+|w|)e^{|w|}\le e^{2|w|}$. Bound the product in (14) by $\exp(2|z|\sum_j|a_j|^{-1})$. The affine exponential has the same form of bound, and $|z|^m\le C_me^{|z|}$. This proves (15). $\square$

## Why xi has infinitely many zeros

Write $\rho=\beta+i\gamma$ for the zeros of $\xi$, equivalently the nontrivial zeros of zeta, counted with multiplicity. The preceding lesson proves $0\le\beta\le1$ and $\xi(0)=\xi(1)=1/2$.

**Theorem 4.1.** The entire function $\xi$ has order exactly one and infinite exponential type. For every $\varepsilon>0$,
$$
\sum_\rho|\rho|^{-1-\varepsilon}<\infty,
\qquad \sum_\rho|\rho|^{-1}=\infty.
\tag{16}
$$
In particular, it has infinitely many zeros.

**Proof.** Multiplication of the theta formula (11) in the preceding lesson gives
$$
\xi(s)=\frac12+\frac{s(s-1)}2
\int_1^\infty\omega(x)
\left(x^{s/2}+x^{(1-s)/2}\right)\frac{dx}{x}.
\tag{17}
$$
For $|s|\le r$, $r\ge2$, the two powers are bounded in modulus by $2x^{(r+1)/2}$, and $\omega(x)\le Ce^{-\pi x}$. Thus
$$
|\xi(s)|\le\tfrac12+Cr^2\int_1^\infty e^{-\pi x}x^{(r+1)/2}\frac{dx}{x}
\le\tfrac12+Cr^2\pi^{-v}\Gamma(v),\qquad v=(r+1)/2.
$$
Real Stirling bounds the last expression by $\exp(Cr\log r)$, proving order at most one.

On the positive real axis, the defining expression (3) from the preceding lesson is positive for $s=x>1$. Also $\zeta(x)\to1$: bound its tail by $2^{-x}+\int_2^\infty u^{-x}du$. Real Stirling then gives
$$
\log\xi(x)=\frac x2\log x
-\frac x2(1+\log(2\pi))+O(\log x).
\tag{18}
$$
This proves that its order is at least one and that it cannot satisfy (15). Corollary 1.2 now proves the convergent sums in (16). If the reciprocal-modulus sum converged, Corollary 3.3 would imply (15), contradicting (18). A finite zero set would also give a convergent reciprocal-modulus sum. $\square$

## Partial fractions and the constant in the product

Hadamard's theorem yields
$$
\xi(s)=\frac12e^{Bs}\prod_\rho(1-s/\rho)e^{s/\rho}.
\tag{19}
$$
The constant prefactor is $\xi(0)=1/2$. Logarithmic differentiation is justified locally uniformly away from zeros, since for bounded $s$ and large $|\rho|$,
$$
\frac1{s-\rho}+\frac1\rho
=\frac{s}{\rho(s-\rho)}=O_s(|\rho|^{-2}).
$$
Thus
$$
\frac{\xi'}{\xi}(s)
=B+\sum_\rho\left(\frac1{s-\rho}+\frac1\rho\right),
\qquad B=\frac{\xi'(0)}{\xi(0)}\in\mathbb R.
\tag{20}
$$
The series of paired terms is absolutely convergent on compact subsets avoiding zeros. The two fractions within each term are kept together.

**Theorem 5.1.** The product constant is
$$
B=-\sum_\rho\Re\frac1\rho
=-1-\frac\gamma2+\frac12\log(4\pi).
\tag{21}
$$
The real-part sum is absolutely convergent. For every $s$ away from the zeros,
$$
\frac{\xi'}{\xi}(s)
=\lim_{T\to\infty}\sum_{|\Im\rho|<T}\frac1{s-\rho}.
\tag{22}
$$
This limit is locally uniform away from zeros. The corresponding product without exponential factors is
$$
\xi(s)=\frac12\lim_{T\to\infty}
\prod_{|\Im\rho|<T}(1-s/\rho),
\tag{23}
$$
locally uniformly on the plane.

**Proof.** Since $0\le\beta\le1$,
$$
0\le\Re(1/\rho)=\frac\beta{|\rho|^2}\le|\rho|^{-2}.
$$
Its sum $S$ converges absolutely. Reflection of $\xi$ gives $\xi'(1)/\xi(1)=-B$. Take real parts of (20) at one. Reflection permutes the zero multiset, so
$$
\sum_\rho\Re\frac1{1-\rho}=S.
$$
This latter real-part sum is also absolutely convergent: $1-\rho$ runs through the same zero set. Hence $-B=B+2S$, proving $B=-S$.

For a finite height cutoff, all zeros of height $|\Im\rho|<T$ form a finite set because they lie in a bounded rectangle. It is closed under conjugation. The imaginary parts of $1/\rho$ cancel in conjugate pairs, and every real zero contributes its real reciprocal. Consequently
$$
\sum_{|\Im\rho|<T}\frac1\rho
=\sum_{|\Im\rho|<T}\Re\frac1\rho\longrightarrow S=-B.
\tag{24}
$$
Subtract this sum from the convergent partial sums of (20) to obtain (22), with local uniform convergence. Removing the exponential factors from the finite products in (19) introduces the factor $\exp((B+\sum_{|\Im\rho|<T}1/\rho)s)$, which tends locally uniformly to one by (24). This proves (23). No arbitrary ordering of the unpaired fractions or factors is asserted.

To evaluate $B$, logarithmically differentiate the defining expression for $\xi$ near one:
$$
\frac{\xi'}{\xi}(s)
=\frac1s+\frac1{s-1}-\tfrac12\log\pi
+\tfrac12\frac{\Gamma'}{\Gamma}(s/2)+\frac{\zeta'}{\zeta}(s).
\tag{25}
$$
The Laurent expansion (1) from the preceding lesson gives
$\zeta'/\zeta(s)=-1/(s-1)+\gamma+O(s-1)$. The gamma lesson gives $\Gamma'/\Gamma(1/2)=-\gamma-2\log2$. Taking the limit in (25) gives
$$
\frac{\xi'(1)}{\xi(1)}
=1+\frac\gamma2-\log2-\tfrac12\log\pi
=1+\frac\gamma2-\tfrac12\log(4\pi).
$$
Negation gives the numerical expression in (21). $\square$

**Corollary 5.2 (zeta partial fractions).** As a meromorphic identity,
$$
\frac{\zeta'}{\zeta}(s)
=B-\frac1{s-1}+\frac12\log\pi
-\frac12\frac{\Gamma'}{\Gamma}(s/2+1)
+\sum_\rho\left(\frac1{s-\rho}+\frac1\rho\right).
\tag{26}
$$

**Proof.** Solve (25) for $\zeta'/\zeta$ and substitute (20). Recurrence gives
$\Gamma'/\Gamma(s/2+1)=\Gamma'/\Gamma(s/2)+2/s$, absorbing the $-1/s$ term. This gives (26) away from its poles and then meromorphically. $\square$

The pole at one is displayed explicitly. The nontrivial zeros are in the sum, and the trivial zeros appear in the gamma term. More explicitly, (27) in the gamma lesson gives
$$
-\frac12\frac{\Gamma'}{\Gamma}(s/2+1)
=\frac\gamma2+\sum_{n=1}^\infty
\left(\frac1{s+2n}-\frac1{2n}\right).
\tag{27}
$$
This series is also locally uniformly convergent away from its poles and shows their residue one.

**Example 5.3 (the first reciprocal-zero sum).** With the symmetric height convention,
$$
\lambda_1:=\lim_{T\to\infty}\sum_{|\Im\rho|<T}\frac1\rho
=-B=1+\frac\gamma2-\frac12\log(4\pi)
\simeq0.0230957089661.
\tag{28}
$$
This is the first of Li's coefficients, studied later in *Explicit formulas and positivity*. Its equality with the absolutely convergent real-part sum follows from (24), while $\sum|1/\rho|$ diverges by Theorem 4.1.

## Two products with visible zeros

**Example 6.1 (sine and Wallis).** The function $\sin\pi z$ has order one: $|\sin\pi z|\le e^{\pi|z|}$, while $|\sin\pi(ir)|=\sinh\pi r$. Its zeros are the integers, all simple. Hadamard factorization gives
$$
\sin\pi z=z e^{A+Bz}
\prod_{n=1}^\infty E_1(z/n)E_1(-z/n).
$$
Pairing is legitimate by the normal convergence of the canonical product. Each pair is $1-z^2/n^2$. The product is even, as is $\sin\pi z/z$, so $e^{Bz}=e^{-Bz}$ for all $z$; differentiation at zero gives $B=0$. The value of $\sin\pi z/z$ at zero is $\pi$, so
$$
\sin\pi z=\pi z\prod_{n=1}^\infty\left(1-\frac{z^2}{n^2}\right).
\tag{29}
$$
Setting $z=1/2$ gives Wallis's product
$$
\frac\pi2=\prod_{n=1}^\infty
\frac{(2n)^2}{(2n-1)(2n+1)}.
\tag{30}
$$

**Example 6.2 (a product of genus zero).** The notation $\cos\sqrt z$ means the entire power series
$\sum_{k\ge0}(-1)^kz^k/(2k)!$; it does not require a square-root branch. The estimate $|\cos\sqrt z|\le e^{\sqrt{|z|}}$ and the value $\cos\sqrt{-r}=\cosh\sqrt r$ prove order $1/2$. Its zeros are $a_n=\pi^2(n-1/2)^2$, so $\sum_n1/|a_n|<\infty$. The product can be written with genus-zero factors:
$$
\cos\sqrt z=\prod_{n=1}^\infty
\left(1-\frac{4z}{\pi^2(2n-1)^2}\right).
\tag{31}
$$
To derive it, divide (29) at $2w$ by twice (29) at $w$. The even-indexed numerator factors cancel the denominator factors, leaving $\cos\pi w=\prod_{n\ge1}(1-4w^2/(2n-1)^2)$. All products in $w^2$ converge absolutely on compact sets, so this cancellation is valid away from the zeros of the denominator. Removability extends it everywhere. Set $w^2=z/\pi^2$ to obtain the identity of entire power series (31).

## Exercises

1. **Easy.** Show that $e^{z^2}$ has order two. Describe its factorization and explain why its exponent cannot be affine.

2. **Medium.** Derive the sine product from Theorem 3.2, determine both constants, and deduce Wallis's product.

3. **Medium.** Starting with (19), prove the symmetric partial-fraction formula (22). Explain why absolute convergence of its individual fractions is unavailable.

4. **Medium.** Evaluate $B=\xi'(0)/\xi(0)$ using reflection, the Laurent expansion of zeta at one and $\Gamma'/\Gamma(1/2)$.

5. **Hard.** Prove that an entire function of order one whose nonzero zeros satisfy $\sum_j1/|a_j|<\infty$ has finite exponential type. Include a possible zero at the origin. Use this to prove again that $\xi$ has infinitely many zeros.

## Solutions

**Solution 1.** On $|z|=r$, $|e^{z^2}|=e^{\Re z^2}\le e^{r^2}$, with equality at $z=r$. Thus $M(r)=e^{r^2}$ and (1) gives order two. There are no zeros, so the product is empty and the factorization is simply $e^{z^2}$. If it equalled $e^{A+Bz}$, logarithmic differentiation would give $2z=B$ for every $z$, an impossibility. The order-at-most-one hypothesis of Theorem 3.2 cannot be discarded.

**Solution 2.** The zeros are zero and $\pm n$ for positive integers $n$, and the origin zero has multiplicity one. The upper bound $e^{\pi r}$ and lower bound $\sinh\pi r$ show order one. Formula (14) therefore gives $z e^{A+Bz}\prod_{n\ge1}(1-z^2/n^2)$. Both the paired product and $\sin\pi z/z$ are even. Their quotient $e^{A+Bz}$ must be even, whose derivative at zero is zero; hence $B=0$. The value at zero gives $e^A=\pi$. At $z=1/2$ the formula reads $1=(\pi/2)\prod_n(1-1/(4n^2))$. Taking the reciprocal gives (30); the positive convergent product has nonzero limit because $\sum_n1/(4n^2)$ converges.

**Solution 3.** Differentiating the normally convergent genus-one product gives $\xi'/\xi=B+\sum_\rho(1/(s-\rho)+1/\rho)$, with absolute local uniform convergence of these paired terms by $\sum_\rho|\rho|^{-2}<\infty$. Because conjugation preserves the zero multiset and the height cutoff, $\sum_{|\Im\rho|<T}1/\rho$ is the real sum of $\Re(1/\rho)$ and tends to $-B$ by (21). Subtracting it proves (22). For fixed $s$ and large $|\rho|$, $|s-\rho|\le2|\rho|$, so
$$
\sum_\rho\left|\frac1{s-\rho}\right|
\ge\frac12\sum_{|\rho|\text{ large}}|\rho|^{-1}=\infty.
$$
Thus the specified grouping is necessary for the unpaired partial fractions.

**Solution 4.** Reflection gives $B=-\xi'(1)/\xi(1)$. Near one, (25) and the pole-subtracted Laurent expansion give
$$
\frac{\xi'(1)}{\xi(1)}
=1+\gamma-\tfrac12\log\pi
+\tfrac12(-\gamma-2\log2)
=1+\tfrac12\gamma-\tfrac12\log(4\pi).
$$
Negate this number. Since $\xi(0)=1/2$, the result is also exactly the coefficient $B$ in the product normalized at zero, rather than an unspecified additive logarithm constant.

**Solution 5.** Use the proved factorization (14), with $m$ the origin multiplicity. For each factor, $(1+|z|/|a_j|)e^{|z|/|a_j|}\le e^{2|z|/|a_j|}$. Hence
$$
|f(z)|\le |z|^m e^{\Re A+|B||z|}
\exp\left(2|z|\sum_j|a_j|^{-1}\right).
$$
The reciprocal sum is finite, and $|z|^m\le C_me^{|z|}$ for all $z$. This proves a bound $C_0e^{C_1|z|}$. A multiplicative constant is needed for an arbitrary value of $f(0)$; equivalently it can be absorbed into the exponent when $|z|\ge1$. If $\xi$ had finitely many zeros, its reciprocal sum would be finite, forcing this bound. But (18) has $\log\xi(x)/x\to\infty$, a contradiction. The same argument proves the stronger divergence assertion in (16).

## What this lesson assumes

The preceding lessons supply the entire completion, its symmetries and its theta integral, together with gamma's Stirling expansion and its logarithmic derivative. Jensen, Borel–Carathéodory, the required Hadamard theorem, infinite zero count and all product and partial-fraction formulas are proved here. The sharper count of zeros by height is developed later in *The Riemann–von Mangoldt formula*.

## Freely readable sources

- C. T. McMullen, [*Advanced Complex Analysis*](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/23/html/home/course/course.pdf), Harvard Math 213a lecture notes, 30 November 2023, 163 pages. Chapter 3, Theorems 3.7, 3.10, 3.15 and 3.17–3.18: finite order, Jensen and Hadamard.
- B. Riemann, [*Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-transcription.pdf) (1859), freely readable D. R. Wilkins transcription, December 1998, 10 pages. Transcription page 5 contains the product assertion; the factorization proof is supplied here.
