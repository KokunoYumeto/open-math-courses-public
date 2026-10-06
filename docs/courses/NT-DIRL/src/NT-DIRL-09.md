# The prime number theorem for arithmetic progressions

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Original material is public domain (CC0).*

The character explicit formula separates the principal main term from the nonprincipal zeros. A classical zero-free region makes all but one possible zero harmless. Keeping that possible real zero visible gives a uniform prime number theorem with an exceptional term; suppressing it without a lower bound for its distance from 1 would destroy the claimed uniformity.

We use the classical region, Landau–Page theorem and effective zero-distance estimates from *Zero-free regions and the exceptional zero*, and the stable character explicit formula from the preceding lesson. These arguments do not use the still deeper Vinogradov–Korobov region. For the final prime-race discussion, the ordinary estimate \(\theta(u)\sim u\) is the exact input supplied by the planned zeta-course lesson *The prime number theorem with the classical error term*. The Gaussian Fourier identity needed there was proved in *Gauss sums*.

## 1. Removing every nonexceptional zero

Fix a sufficiently small effective constant \(c_0>0\) in the classical region. Decrease it, if necessary, below half the Page constant. For a modulus \(q\ge3\), an exceptional zero means a zero

\[
\beta_1>1-\frac{c_0}{\log(2q)}.
\tag{1.1}
\]

There is at most one character modulo \(q\) carrying such a zero. It is real and nonprincipal; the zero is real, simple, less than 1, and, by decreasing \(c_0\), greater than \(1/2\). Write \(\chi_1\) for that character when it exists. Its primitive conductor can be smaller than \(q\). The choice (1.1) is fixed throughout the lesson, independently of \(x\).

**Lemma 1.1.** For \(x\ge T\ge2\), put
\(\eta=c_0/\log(q(T+2))\), taking \(c_0\) small enough that \(\eta<1/2\). Uniformly for all characters modulo \(q\), the contribution of their nonexceptional zeros to the stable explicit formula is

\[
\sum_{|\gamma|<T\atop\rho\ne\beta_1}
\frac{x^\rho-1}{\rho}
\ll x^{1-\eta}\log^2(q(T+2))
+\sqrt x\log(2x)\log(2q).
\tag{1.2}
\]

Here \(\beta_1\) is excluded only for its own character.

**Proof.** The region gives \(\beta\le1-\eta\) for every zero being summed. A zero exactly on the boundary of the exceptional interval, if excluded by the strict definition (1.1), obeys that same inequality and can remain in this sum.

For \(|\gamma|>1\), use
\(|x^\rho-1|\le x^\beta+1\le2x^{1-\eta}\) and
\(|\rho|\ge|\gamma|\). The reciprocal-ordinate bound from the preceding lesson makes their total
\(O(x^{1-\eta}\log^2(q(T+2)))\).

For \(|\gamma|\le1\) and \(\beta\ge1/2\), the denominator has magnitude at least \(1/2\); the local count gives
\(O(x^{1-\eta}\log(2q))\). For the remaining low zeros, possibly extremely close to 0, use the integral identity

\[
\left|\frac{x^\rho-1}{\rho}\right|
=\left|\int_1^x u^{\rho-1}\,du\right|
\le\sqrt x\log x\quad(0<\beta<1/2).
\]

There are \(O(\log(2q))\) such zeros. This proves (1.2), including a possible reflected partner \(1-\beta_1\) close to the origin. No unsupported bound for its reciprocal is used. \(\square\)

The principal primitive factor is zeta and has no exceptional zero; its classical region is included in the constant \(c_0\). Thus the lemma and the preceding lesson's principal explicit formula apply to it too, with \(q\) enlarging its conductor logarithm if necessary.

## 2. A uniform theorem with the exceptional term visible

**Theorem 2.1.** There are absolute effective constants \(A,k>0\) such that, uniformly for

\[
x\ge3,\qquad q\le\exp(A\sqrt{\log x}),
\qquad (b,q)=1,
\]

we have

\[
\boxed{\psi(x;q,b)=
\frac{x-\chi_1(b)x^{\beta_1}/\beta_1}{\varphi(q)}
+O(xe^{-k\sqrt{\log x}}).}
\tag{2.1}
\]

The exceptional term is omitted when (1.1) has no zero. For \(q=1,2\) the same assertion holds without an exceptional term. The error constant is absolute.

**Proof.** Choose \(T=\exp(A\sqrt{\log x})\). For sufficiently large \(x\), \(2\le T\le x\). The finitely bounded remaining range of \(x\), and the resulting bounded range of \(q\), can be covered by increasing an absolute error constant.

For definiteness take \(A=\sqrt{c_0}/2\), or any smaller positive constant. In the stated modulus range,

\[
\log(q(T+2))\le2A\sqrt{\log x}+O(1).
\]

For all sufficiently large \(x\), this is at most \(3A\sqrt{\log x}\). Hence

\[
x^{1-\eta}\le x\exp\left(-\frac{c_0}{3A}\sqrt{\log x}\right).
\]

Lemma 1.1 and the stable explicit formula therefore give, for each character,

\[
\psi(x,\chi)=\mathbf1_{\chi=\chi_0}x
-\mathbf1_{\chi=\chi_1}\frac{x^{\beta_1}}{\beta_1}
+O(xe^{-k\sqrt{\log x}}).
\tag{2.2}
\]

Indeed the truncation error is
\(O(xT^{-1}\log^2(qx))\), and the low-zero remainder is
\(O(\sqrt x\log(2x)\log(2q))\). All fixed logarithmic powers are absorbed by decreasing \(k\) below the minimum of \(A\) and \(c_0/(3A)\). Replacing
\((x^{\beta_1}-1)/\beta_1\) by \(x^{\beta_1}/\beta_1\) costs at most 2 and is likewise absorbed.

Now use character orthogonality:

\[
\psi(x;q,b)=\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(b)}\psi(x,\chi).
\]

There is one principal main term and at most one exceptional term. Its character is real, so its conjugate value equals \(\chi_1(b)\). The \(\varphi(q)\) error bounds are divided by \(\varphi(q)\), retaining the same absolute error. This proves (2.1). Moduli 1 and 2 have only a principal inducing function; their missing prime powers are \(O(\log x)\), already covered by the error. \(\square\)

The sign in (2.1) has a concrete meaning. If \(\chi_1(b)=1\), the exceptional term reduces the predicted prime-power count. If \(\chi_1(b)=-1\), it increases it. Different residue classes are affected in opposite directions. The absolute error theorem does not alone assert a relative asymptotic for every modulus at the upper exponential endpoint of its range.

## 3. Passing from prime powers to primes

Write \(\theta(x;q,b)=\sum_{p\le x,\,p\equiv b\,(q)}\log p\), and let \(\pi(x;q,b)\) count those primes. Throughout,
\(\operatorname{li}(x)=\operatorname{PV}\int_0^x du/\log u\).

**Theorem 3.1.** In the range of Theorem 2.1,

\[
\theta(x;q,b)=
\frac{x-\chi_1(b)x^{\beta_1}/\beta_1}{\varphi(q)}
+O(xe^{-k_1\sqrt{\log x}})
\tag{3.1}
\]

for an absolute effective \(k_1>0\). After reducing the modulus range to
\(q\le\exp((A/2)\sqrt{\log x})\),

\[
\boxed{\pi(x;q,b)=
\frac{\operatorname{li}(x)-\chi_1(b)\operatorname{li}(x^{\beta_1})}{\varphi(q)}
+O\left(\frac{x}{\log x}e^{-k_2\sqrt{\log x}}\right)}
\tag{3.2}
\]

with an absolute effective \(k_2>0\). Again omit exceptional terms when absent.

**Proof.** The prime powers of exponent at least 2 contribute
\(O(\sqrt x\log^2(2x))\), uniformly in the progression. This is absorbed by the error in (2.1), proving (3.1).

Exact partial summation gives

\[
\pi(x;q,b)=\frac{\theta(x;q,b)}{\log x}
+\int_2^x\frac{\theta(u;q,b)}{u\log^2u}\,du.
\tag{3.3}
\]

Split at \(\sqrt x\). On the lower part, the Chebyshev bound \(\theta(u;q,b)\le\theta(u)\ll u\) makes the total \(O(\sqrt x)\). The lower portions of the proposed principal and exceptional main terms are also \(O(\sqrt x)\), uniformly since \(\beta_1>1/2\) and \(\varphi(q)\ge1\).

For \(u\ge\sqrt x\), the reduced modulus assumption implies
\(q\le\exp(A\sqrt{\log u})\). Hence (3.1) applies throughout this upper integration interval, with the same character and zero because (1.1) depends only on \(q\). Its integrated error is

\[
\ll\frac{x}{\log^2x}
e^{-(k_1/\sqrt2)\sqrt{\log x}},
\]

and its boundary error is
\(O(xe^{-k_1\sqrt{\log x}}/\log x)\).
The lower errors are absorbed by decreasing \(k_2\).

Integrating the main terms in (3.3) yields (3.2), up to uniformly bounded lower-end constants. For the exceptional term the needed derivative is

\[
\frac d{du}\operatorname{li}(u^{\beta_1})
=\frac{u^{\beta_1-1}}{\log u}.
\tag{3.4}
\]

Thus the factor \(1/\beta_1\) in the weighted formula disappears in the prime-counting formula. The lower-end constants are bounded uniformly for \(1/2\le\beta_1\le1\), because \(2^{\beta_1}\) stays away from 1. This completes the proof. \(\square\)

For every fixed \(q\), the possible \(\beta_1\) is a fixed number less than 1. Consequently
\(\operatorname{li}(x^{\beta_1})=o(\operatorname{li}(x))\), and the error in (3.2) is also of smaller order. We obtain

\[
\boxed{\pi(x;q,b)\sim\frac{\operatorname{li}(x)}{\varphi(q)}
\sim\frac{x}{\varphi(q)\log x}.}
\tag{3.5}
\]

The elementary estimate \(\operatorname{li}(x)\sim x/\log x\) follows by integration by parts, whose residual integral is \(O(x/\log^2x)\) after splitting at \(\sqrt x\). Thus (3.5) is an asymptotic count, stronger than the Dirichlet density established near the beginning of the course.

## 4. Uniformity before Siegel's theorem

**Theorem 4.1.** Fix \(0<\varepsilon<1\). Uniformly for
\(q\le(\log x)^{1-\varepsilon}\) and \((b,q)=1\),

\[
\psi(x;q,b)=\frac x{\varphi(q)}
+O_\varepsilon(xe^{-k_3\sqrt{\log x}}),
\tag{4.1}
\]

and the corresponding \(\theta\) and \(\pi\) estimates have no exceptional term. Their constants are effective. In particular the relative asymptotics hold uniformly in this range.

**Proof.** The exceptional-distance theorem gives

\[
1-\beta_1\gg q^{-1/2}(\log(2q))^{-2}.
\]

Hence, in the stated range,

\[
(1-\beta_1)\log x
\gg_\varepsilon
\frac{(\log x)^{(1+\varepsilon)/2}}
{(\log\log(3x))^2}.
\tag{4.2}
\]

Its ratio to \(\sqrt{\log x}\) tends to infinity. Thus, for all sufficiently large \(x\) depending effectively on \(\varepsilon\),
\(x^{\beta_1}\le xe^{-2k\sqrt{\log x}}\).
This absorbs the exceptional term in (2.1); the bounded lower range is covered by an effective \(O_\varepsilon\) constant. The same reasoning applies to (3.1)–(3.2). In the latter, \(\operatorname{li}(x^{\beta_1})\ll x^{\beta_1}/\log x\) uniformly for \(\beta_1\ge1/2\) and large \(x\). Finally multiplication of the error by \(\varphi(q)\le(\log x)^{1-\varepsilon}\) leaves it smaller than the main term. \(\square\)

The bound with logarithmic exponent 2 uses the precise internal quadratic class-number input identified in the values-at-one lesson. There is also a completely analytic route to the same range here: use
\(1-\beta_1\gg q^{-1/2}(\log(2q))^{-4}\), which was proved there using the analytic value bound and the derivative estimate. It changes the denominator in (4.2) to the fourth power, and its ratio to \(\sqrt{\log x}\) still tends to infinity. Thus the stated pre-Siegel range and effectivity can be obtained without algebraic class-number formulas.

For every fixed power \((\log x)^B\), with no restriction \(B<1\), a stronger uniform lower bound for \(1-\beta_1\) is needed to retain this classical exponential error. That is the work of the next two lessons on Siegel and Siegel–Walfisz.

**Corollary 4.2 (one inducing conductor in a dyadic range).** Among moduli \(Q\le q\le2Q\), \(Q\ge3\), all exceptional terms defined by (1.1), if any, arise from at most one primitive inducing character and hence from one conductor.

**Proof.** Its conductor is at most \(2Q\). Also
\(1-\beta_1<c_0/\log(2q)\le c_0/\log Q\).
Since \(\log(2Q)\le2\log Q\) and \(c_0\) was chosen below half the Page constant, this is at most \(c_P/\log(2Q)\). Page at bound \(2Q\) excludes two different primitive characters. Many moduli may still contain induced copies of the one allowed character. \(\square\)

## 5. A finite prime race

Define
\(\Delta(x)=\pi(x;4,3)-\pi(x;4,1)\).
Exact enumeration by the sieve of Eratosthenes gives:

| \(x\) | \(\pi(x;4,1)\) | \(\pi(x;4,3)\) | \(\Delta(x)\) |
|---:|---:|---:|---:|
| 10 | 1 | 2 | 1 |
| 100 | 11 | 13 | 2 |
| 1,000 | 80 | 87 | 7 |
| 10,000 | 609 | 619 | 10 |
| 100,000 | 4,783 | 4,808 | 25 |

The prime 2 belongs to neither class; the last two columns of counts sum to 9,591 at \(10^5\), one less than the total prime count. These finite samples exhibit the classical Chebyshev bias. They do not prove a density statement, and (3.5) gives both classes the same leading asymptotic. A smaller fluctuation can nevertheless have a persistent preference in sign. We now prove a precise conditional statement for this particular race.

![The exact difference of the prime counts in the residue classes 3 and 1 modulo 4 up to one hundred thousand, plotted against logarithmic x.](assets/prime-race-modulo-4.png)

*Figure 1. Exact sieve counts through \(10^5\) give this right-continuous step curve. The first negative value occurs at \(x=26861\), where \(\Delta(x)=-1\); the value at \(10^5\) is 25. A logarithmic horizontal scale shows the finite record clearly. This plot does not establish the logarithmic density in Theorem 6.1; that theorem requires the stated zero hypotheses and the proof below. Reproducible original CC0 drawing and enumeration source are included.*

## 6. A conditional proof of the modulo-4 bias

The logarithmic density of a set \(S\subset[2,\infty)\), when it exists, is

\[
\lim_{X\to\infty}\frac1{\log X}\int_2^X
\mathbf1_S(x)\,\frac{dx}x.
\tag{6.1}
\]

With \(x=e^y\), this is the long-interval average in \(y\). Assume the Riemann hypothesis for \(L(s,\chi_{-4})\) and assume that its positive zero ordinates, listed with multiplicity, are linearly independent over \(\mathbb Q\). The latter hypothesis implies simplicity; no zero at ordinate 0 occurs because the positivity argument in the zero-free lesson proved \(L(\sigma,\chi_{-4})>0\) for all real \(\sigma>0\).

**Theorem 6.1 (the modulo-4 case of Chebyshev's bias).** Under these hypotheses, the set
\(\{x\ge2:\pi(x;4,3)>\pi(x;4,1)\}\) has logarithmic density \(\delta\), with

\[
\boxed{\frac12<\delta<1.}
\tag{6.2}
\]

More precisely, let \(U_\gamma\) be independent uniform random variables on the unit circle. Then

\[
\delta=\mathbb P\left(
1+2\Re\sum_{\gamma>0}
\frac{U_\gamma}{1/2+i\gamma}>0\right),
\tag{6.3}
\]

where the random series converges in mean square. This is a special case of the prime-race framework of Rubinstein and Sarnak. We give the proof for this one race, including the mean-square justification that a formal zero sum alone would omit.

**Proof.** Put \(\rho_\gamma=1/2+i\gamma\) and

\[
E(y)=y e^{-y/2}\Delta(e^y),\qquad
P_T(y)=1+2\Re\sum_{0<\gamma<T}
\frac{e^{i\gamma y}}{\rho_\gamma}.
\]

We first show, for \(T\ge2\) avoiding zero ordinates,

\[
\limsup_{Y\to\infty}\frac1Y
\int_{\log2}^Y|E(y)-P_T(y)|^2\,dy
\ll\frac{\log^2(T+2)}T.
\tag{6.4}
\]

The constant may be fixed for this character. The argument has three steps.

*A bound for the high zero frequencies.* For any finite sublist of ordinates with \(T<|\gamma|<M\), \(T\ge2\), and coefficients \(c_\gamma=1/\rho_\gamma\), a Gaussian majorant gives, for \(Y\ge1\),

\[
\begin{aligned}
\frac1Y\int_0^Y\left|\sum_\gamma c_\gamma e^{i\gamma y}\right|^2dy
&\le\frac{e^{1/4}}Y\int_{\mathbb R}
e^{-(y-Y/2)^2/Y^2}
\left|\sum_\gamma c_\gamma e^{i\gamma y}\right|^2dy\\
&\ll\sum_\gamma|c_\gamma|^2
\sum_\nu e^{-Y^2(\gamma-\nu)^2/4}.
\end{aligned}
\tag{6.5}
\]

The first inequality uses \(e^{-(y-Y/2)^2/Y^2}\ge e^{-1/4}\) on \([0,Y]\). Expanding the finite square and using the Gaussian Fourier identity evaluates its integral as

\[
Y\sqrt\pi\sum_{\gamma,\nu}c_\gamma\overline{c_\nu}
e^{i(\gamma-\nu)Y/2}e^{-Y^2(\gamma-\nu)^2/4}.
\]

Take absolute values and use
\(2|c_\gamma c_\nu|\le|c_\gamma|^2+|c_\nu|^2\) to obtain the second inequality.

The local zero count implies, by unit-interval subdivision around \(\gamma\),

\[
\sum_\nu e^{-Y^2(\gamma-\nu)^2/4}
\ll\log(|\gamma|+2)\qquad(Y\ge1).
\]

Indeed the intervals at bounded distance contribute \(O(\log(|\gamma|+2))\); the intervals at integer distance \(k\ge2\) contribute at most
\(C\log(|\gamma|+k+2)e^{-(k-1)^2/4}\), whose sum has the same bound. Applying the local count once more to the outer sum in (6.5) gives

\[
\frac1Y\int_0^Y\left|\sum_{T<|\gamma|<M}
\frac{e^{i\gamma y}}{\rho_\gamma}\right|^2dy
\ll\sum_{k\ge T-1}\frac{\log^2(k+2)}{k^2}
\ll\frac{\log^2(T+2)}T.
\tag{6.6}
\]

This is uniform in the upper cutoff \(M\); arbitrarily close zero ordinates cause no problem because their local multiplicity is included in the count.

*From prime powers to a mean-square zero sum.* In the sharp explicit formula of the preceding lesson choose \(M=e^{2Y}\) as truncation height, and \(x=e^y\), for \(\log2\le y\le Y\). This sharp formula permits heights larger than \(x\). Since the character is odd, multiplication by \(e^{-y/2}\) gives

\[
e^{-y/2}\psi(e^y,\chi_{-4})
=-\sum_{|\gamma|<M}\frac{e^{i\gamma y}}{\rho_\gamma}
+r_Y(y),
\]

with
\( |r_Y(y)|\ll(1+y)e^{-y/2}+Y^2e^{y/2-2Y}\).
Here the constant \(b\), the trivial-zero tail, the half-endpoint correction and the nearest-prime-power error are bounded by the first term; the other truncation error gives the second. Both have mean square tending to zero on the displayed interval after division by \(Y\).

The square prime powers give

\[
\psi(x,\chi_{-4})-\theta(x,\chi_{-4})
=\sum_{p\le\sqrt x\atop p\ne2}\log p
+O(x^{1/3}\log^2(2x)).
\tag{6.7}
\]

This follows because \(\chi_{-4}(p^2)=1\) for every odd prime and the exponents at least 3 have the stated elementary total bound. The ordinary prime number theorem supplies
\(\sum_{p\le\sqrt x}\log p=\sqrt x+o(\sqrt x)\).
Thus the normalized difference in (6.7) tends to 1. It also tends in long-interval mean square, since it is bounded and converges pointwise as \(y\to\infty\).

Consequently, if
\(F(y)=e^{-y/2}\theta(e^y,\chi_{-4})\), then

\[
F(y)=-1-\sum_{|\gamma|<M}
\frac{e^{i\gamma y}}{\rho_\gamma}
+\text{a remainder of vanishing mean square}.
\tag{6.8}
\]

In particular \(Y^{-1}\int_{\log2}^Y|F(y)|^2dy\) stays bounded: retain a fixed finite initial sum and bound its tail by (6.6).

*From weighted primes to the race.* Let
\(\pi(x,\chi_{-4})=\sum_{p\le x}\chi_{-4}(p)=-\Delta(x)\).
Partial summation gives

\[
y e^{-y/2}\pi(e^y,\chi_{-4})
=F(y)+R_\pi(y),
\quad
R_\pi(y)=y\int_{\log2}^y
e^{-(y-v)/2}\frac{F(v)}{v^2}\,dv.
\tag{6.9}
\]

This integral term has vanishing long-interval mean square. To verify this rather than discard it pointwise, use the GRH estimate
\(F(v)\ll(1+v)^2\) for the early part \(v\le y/2\); its contribution is \(O(y e^{-y/4})\). For the late part \(y/2\le v\le y\), Cauchy–Schwarz gives

\[
|R_{\pi,\mathrm{late}}(y)|^2
\ll\frac1{y^2}\int_{y/2}^y
e^{-(y-v)/2}|F(v)|^2\,dv.
\]

For any fixed large \(H\), average this over \(H\le y\le Y\), replace \(1/y^2\) by \(1/H^2\), and interchange nonnegative integrals. The inner exponential integral in \(y\) is at most 2. The result is
\(O(H^{-2}Y^{-1}\int_{\log2}^Y|F(v)|^2dv)=O(H^{-2})\).
The fixed initial interval has vanishing average. Let \(H\to\infty\) to obtain the assertion. Since \(E=-y e^{-y/2}\pi(e^y,\chi_{-4})\), (6.8), (6.9) and (6.6) prove (6.4).

Now identify the limiting distribution. For a fixed finite set of positive ordinates, linear independence implies that
\((e^{i\gamma_1 y},\ldots,e^{i\gamma_m y})\)
is uniformly distributed on the product of unit circles. For a nonconstant torus monomial its average is
\(Y^{-1}\int e^{iy\sum n_j\gamma_j}dy\to0\), since
\(\sum n_j\gamma_j\ne0\). Constants average to 1. Finite trigonometric polynomials therefore have their Haar averages; the tensor product of the Fejér kernels proved earlier uniformly approximates every continuous torus function, extending the result to all such functions. Hence \(P_T\) has limiting law

\[
X_T=1+2\Re\sum_{0<\gamma<T}\frac{U_\gamma}{\rho_\gamma}.
\]

Independent uniform circle variables may, for example, be constructed from binary digits of a uniform point in \([0,1]\): partition the digit positions into countably many infinite sets and use each set as the digits of one independent uniform coordinate. Finite binary cylinders have the required product probabilities, which proves the claimed uniformity and independence. Each summand has mean zero and variance \(2/|\rho_\gamma|^2\). The reciprocal-square zero sum converges by the local count, so \(X_T\) converges in \(L^2\) to the variable \(X\) in (6.3).

For any bounded Lipschitz function \(h\), Cauchy–Schwarz and (6.4) bound the difference between the long-interval averages of \(h(E)\) and \(h(P_T)\) by
\(C_h\log(T+2)/\sqrt T\). The finite-sum equidistribution identifies the latter average with \(\mathbb E h(X_T)\); \(L^2\) convergence makes this tend to \(\mathbb E h(X)\). Letting \(T\to\infty\) proves convergence of these averages to the law of \(X\).

That law has no atom: separate any one nonzero summand. The variable
\(2\Re(U_\gamma/\rho_\gamma)\) has the arcsine density
\((\pi\sqrt{r^2-v^2})^{-1}\) on \((-r,r)\), with \(r=2/|\rho_\gamma|\), by the elementary cosine change of variables. Its convolution with the independent remaining random sum has no atoms. Thus Lipschitz upper and lower approximations to \(\mathbf1_{(0,\infty)}\), with their transition intervals shrinking to zero, prove that the logarithmic density of \(E(y)>0\) exists and equals \(\mathbb P(X>0)\). This sign is precisely the sign of \(\Delta(e^y)\).

Finally write \(X=1+V\). The law of \(V\) is symmetric because all circle variables can be replaced by their negatives. It is atomless, so

\[
\mathbb P(X>0)=\mathbb P(V>-1)
=\frac12+\frac12\mathbb P(|V|<1).
\]

The last probability is positive. Choose a finite cutoff so that the tail variance is less than \(1/16\). Chebyshev's inequality gives positive probability that the tail has magnitude less than \(1/2\). Independently, put every finitely many initial phases in small arcs where its real contribution is close to zero; their sum then has magnitude less than \(1/2\), an event of positive probability. Their intersection gives \(|V|<1\).

To see that the density is less than 1, note from the zero-count main term that
\(\sum_{0<\gamma<T}2/|\rho_\gamma|\to\infty\).
This follows, for example, by partial summation of the positive-ordinate count, which is half the two-sided count for this real character. Choose a large finite cutoff whose total amplitudes exceed 3 and whose tail variance is less than \(1/16\). Put all initial phases in small arcs near their most negative contributions; their sum is then less than \(-2\), with positive probability. Independently the tail lies in \((-1/2,1/2)\) with positive probability. Thus \(\mathbb P(V<-1)>0\). Together these observations prove (6.2) and (6.3). \(\square\)

The constant 1 in this limiting law comes from square prime powers in (6.7). It gives a bias in sign even though both prime counts have the same leading term. The independence hypothesis supplies uniform phase averages; the zero-frequency mean-square bound supplies the justified passage to infinitely many zeros. Both hypotheses and both steps matter. No assertion about an unconditional density, or about natural density with weight \(dx\), follows from this conditional argument.

## 7. Exercises

1. **Easy.** Deduce \(\pi(x;q,b)\sim\operatorname{li}(x)/\varphi(q)\) for fixed \(q\).
2. **Medium.** Use Page's theorem to show that all exceptional terms for \(Q\le q\le2Q\) come from at most one primitive conductor. Explain the possibility of several induced moduli.
3. **Medium.** Prove the uniform result for \(q\le(\log x)^{1-\varepsilon}\) without Siegel's theorem, retaining the classical exponential error.
4. **Hard.** Derive the formulas for \(\theta\) and \(\pi\) with the exceptional term. Explain the disappearance of \(1/\beta_1\), and ensure that the modulus hypothesis holds throughout the partial-summation integral.

## 8. Solutions

**1.** For a fixed \(q\), (3.2) eventually applies. Its error is \(o(x/\log x)\). If an exceptional term exists, its exponent is the fixed \(\beta_1<1\), so
\(\operatorname{li}(x^{\beta_1})/\operatorname{li}(x)
\sim x^{\beta_1-1}/\beta_1\to0\).
The integration-by-parts asymptotic \(\operatorname{li}(x)\sim x/\log x\) now proves the claim. Nonvanishing at 1, not a hypothesis ruling out all exceptional zeros, is enough to ensure \(\beta_1<1\).

**2.** A character modulo \(q\le2Q\) has conductor at most \(2Q\). Its exceptional distance is less than \(c_0/\log(2q)\le c_0/\log Q\). With \(c_0\le c_P/2\) and \(\log(2Q)\le2\log Q\), this is at most \(c_P/\log(2Q)\). Page at bound \(2Q\) permits at most one primitive character with that distance. If its conductor \(d\) divides several moduli in the dyadic range, its induced copies may appear at each of them; no second primitive conductor has been created. In a larger modulus it must also pass the narrower exceptional test (1.1) to appear as the explicit term.

**3.** Insert the effective distance
\(1-\beta_1\gg q^{-1/2}(\log(2q))^{-2}\).
For \(q\le(\log x)^{1-\varepsilon}\), its product with \(\log x\) is bounded below as in (4.2), which exceeds any fixed multiple of \(\sqrt{\log x}\) for sufficiently large \(x\). Thus the exceptional contribution is absorbed into the exponential error of Theorem 2.1. The relative error tends to zero uniformly because \(\varphi(q)\) is at most a fixed power of \(\log x\). If one wants to avoid the class-number inputs as well as Siegel's theorem, use the analytic exponent-4 distance bound. The same comparison works with \((\log\log(3x))^4\) in the denominator. All constants and the required threshold are effective.

**4.** Removing higher prime powers from (2.1) costs
\(O(\sqrt x\log^2x)\), already smaller than its error, giving (3.1). Apply the exact identity (3.3). Reduce the modulus range to \(q\le\exp((A/2)\sqrt{\log x})\) and split at \(\sqrt x\). Below that point the actual counts and proposed main-term integrals are \(O(\sqrt x)\); above it the hypothesis \(q\le\exp(A\sqrt{\log u})\) holds. Integration of the upper error gives
\(O(xe^{-k_1\sqrt{\log x}/\sqrt2}/\log^2x)\), and the boundary error is \(O(xe^{-k_1\sqrt{\log x}}/\log x)\). For the main exceptional expression,

\[
\frac{x^{\beta_1}}{\beta_1\log x}
+\int_2^x\frac{u^{\beta_1-1}}{\beta_1\log^2u}\,du
=\operatorname{li}(x^{\beta_1})+O(1),
\]

uniformly for \(1/2\le\beta_1\le1\), by (3.4) or integration by parts. This proves the sign and normalization of (3.2). Applying the formula at all smaller \(u\) without this range check would be an unjustified use of the uniform theorem.

## References

D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 12.4 and the discussion after Theorem 12.8, supplies comparison statements for the uniform range and effective lower bound. Our proof keeps the factor \(1/\beta_1\) until the correctly normalized partial summation. M. Rubinstein and P. Sarnak, [*Chebyshev's Bias*](https://doi.org/10.1080/10586458.1994.10504289), *Experimental Mathematics* 3 (1994), 173–197, develops the general conditional prime-race theory. Section 6 supplies a complete proof for the modulo-4 race considered here; no general-density theorem from that paper is used as an unproved input.
