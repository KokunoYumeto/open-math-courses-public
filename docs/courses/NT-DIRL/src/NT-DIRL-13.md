# The multiplicative large sieve and bilinear forms with characters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Gauss sums connect additive and multiplicative Fourier analysis. They transfer the sharp large sieve to primitive Dirichlet characters. Cauchy–Schwarz then controls bilinear sums, and a truncated Mellin integral separates the product cutoff while allowing a different maximizing endpoint for every character. Hybrid estimates add a height variable; family moments apply those estimates to the functional equation.

The prerequisites are *Gauss sums* and *The large sieve inequality*. The scalar truncated Perron kernel used in *Counting zeros and the explicit formula for character sums over prime powers* is the precise Mellin inversion input below. The family moment argument uses the entire completed function, functional equation and uniform fixed-strip gamma estimates from *The functional equation of Dirichlet L-functions*. Write \(\sum_\chi^*\) for primitive characters, and include the unique primitive character of conductor 1. Implied constants are effective and absolute unless a dependence is indicated.

## 1. Transferring the additive inequality

Let \(M\in\mathbb Z\), let \(N\ge1\) be an integer, and put

\[
S(\chi)=\sum_{M<n\le M+N}a_n\chi(n),
\qquad T(t)=\sum_{M<n\le M+N}a_n e(nt).
\]

For primitive \(\chi\pmod q\), the Gauss identity, with \(\tau(\chi)=\sum_{b\bmod q}\chi(b)e(b/q)\), is

\[
\chi(n)=\frac1{\tau(\overline\chi)}
\sum_{b\bmod q}\overline\chi(b)e(bn/q).
\tag{1.1}
\]

This holds even when \((n,q)>1\), and \(|\tau(\overline\chi)|=\sqrt q\). Consequently

\[
q\sum_\chi^*|S(\chi)|^2
=\sum_\chi^*\left|\sum_{b\bmod q}^{*}\overline\chi(b)T(b/q)\right|^2
\le\varphi(q)\sum_{b\bmod q}^{*}|T(b/q)|^2.
\tag{1.2}
\]

The inequality enlarges the character sum to all characters modulo \(q\); character orthogonality then gives the expression on the right. This explains the weight \(q/\varphi(q)\).

**Theorem 1.1 (the multiplicative large sieve).** For real \(Q\ge1\),

\[
\boxed{\sum_{q\le Q}\frac q{\varphi(q)}\sum_{\chi\bmod q}^{*}|S(\chi)|^2
\le(N-1+Q^2)\sum_{M<n\le M+N}|a_n|^2.}
\tag{1.3}
\]

**Proof.** Divide (1.2) by \(\varphi(q)\), sum over \(q\), and apply the sharp Farey inequality from the preceding lesson. With Gallagher's additive estimate the same argument gives \(\pi(N-1)+Q^2\). \(\square\)

Primitivity is required in (1.1). Induced characters do not have a Gauss sum of magnitude \(\sqrt q\); some have Gauss sum zero. Repeated induced principal characters would also invalidate an unrestricted version of (1.3).

For \(a_n=1\) on \(1\le n\le N\), the conductor-one term is \(N^2\). Subtract it from (1.3) to obtain

\[
\sum_{1<q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\left|\sum_{n\le N}\chi(n)\right|^2\le(Q^2-1)N.
\tag{1.4}
\]

Bounding every primitive nonprincipal character separately by Pólya–Vinogradov instead gives \(O(Q^3\log^2(2Q))\) after summing. Estimate (1.4) gains in many ranges by averaging, without asserting a bound for each individual character.

Here are four exact constant-coefficient examples. The energy column is the left side of (1.4).

| \(Q\) | \(N\) | Weighted nonprincipal energy | Bound \((Q^2-1)N\) |
|---:|---:|---:|---:|
| 3 | 5 | 0 | 40 |
| 5 | 12 | 5 | 288 |
| 8 | 12 | \(113/6\) | 756 |
| 12 | 25 | \(734/15\) | 3575 |

They can be computed without numerical roots of unity. If \(c_{q,d}(h)\) counts the \(n\le N\) with \((n,q)=1\) and \(n\equiv h\pmod d\), then primitive-character inclusion–exclusion and ordinary orthogonality give
\(\sum_\chi^*|\sum_{n\le N}\chi(n)|^2=\sum_{d\mid q}\mu(q/d)\varphi(d)\sum_{h\bmod d}c_{q,d}(h)^2\).
Multiply by \(q/\varphi(q)\) and sum \(2\le q\le Q\). For example, \((Q,N)=(8,12)\) receives 5 from conductor 5, \(35/6\) from conductor 7, and 8 from conductor 8; the other nonprincipal conductors contribute zero. The large sieve bound is uniform, not an assertion that every example comes close to equality.

## 2. Large values and rectangular bilinear sums

Write \(E=\sum|a_n|^2\). For \(V>0\), (1.3) immediately implies

\[
\sum_{\substack{q\le Q,\ \chi\bmod q\text{ primitive}\\ |S(\chi)|>V}}
\frac q{\varphi(q)}\le\frac{(N-1+Q^2)E}{V^2}.
\tag{2.1}
\]

The same expression bounds the unweighted number of those characters because every weight is at least 1. The family consists of pairs \((q,\chi)\), with \(q\) the primitive conductor.

Let \(a_m\) be supported on \(1\le m\le M\) and \(b_n\) on \(1\le n\le N\), with integer \(M,N\ge1\). Put \(A(\chi)=\sum_{m\le M}a_m\chi(m)\) and \(B(\chi)=\sum_{n\le N}b_n\chi(n)\). Complete multiplicativity gives \(\sum_{m,n}a_mb_n\chi(mn)=A(\chi)B(\chi)\), including nonunits, where the character vanishes. Cauchy–Schwarz in the weighted family and two applications of (1.3) give

\[
\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\left|\sum_{m\le M}\sum_{n\le N}a_mb_n\chi(mn)\right|
\le\sqrt{(M-1+Q^2)(N-1+Q^2)}\,\|a\|_2\|b\|_2.
\tag{2.2}
\]

It is the character average that makes this useful. For a single chosen character, coefficients \(a_m=\overline{\chi(m)}\), \(b_n=\overline{\chi(n)}\) can align every nonzero term.

## 3. Separating a product cutoff, including the maximum

**Theorem 3.1.** With these supports,

\[
\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\max_{u\ge0}\left|\sum_{\substack{m\le M,\ n\le N\\ mn\le u}}a_mb_n\chi(mn)\right|
\ll\sqrt{(M+Q^2)(N+Q^2)}\,\|a\|_2\|b\|_2\log(2MN).
\tag{3.1}
\]

The maximizing endpoint may differ for every character.

**Proof.** Let \(P=MN\). Only thresholds \(K\in\{0,\ldots,P\}\) matter. Replace each by \(y=K+1/2\), including exactly the same positive integer products. Set \(c=1/\log(2P)\), \(H=4P^2\). The scalar Perron kernel gives

\[
\mathbf1_{k<y}
=\frac1{2\pi}\int_{-H}^H\frac{(y/k)^{c+it}}{c+it}\,dt
+O\left((y/k)^c\min\left(1,\frac1{H|\log(y/k)|}\right)\right).
\tag{3.2}
\]

This is the exact truncated inversion lemma used in the earlier explicit-formula lesson. There is no equality-endpoint term at a half-integer. For \(1\le k\le P\), \(1/2\le y\le P+1/2\), we have \((y/k)^c\le e\) and \(|\log(y/k)|\ge|y-k|/\max(y,k)\ge1/(3P)\); therefore each scalar error is \(O(P/H)\).

Put

\[
A_t(\chi)=\sum_{m\le M}\frac{a_m\chi(m)}{m^{c+it}},
\qquad B_t(\chi)=\sum_{n\le N}\frac{b_n\chi(n)}{n^{c+it}}.
\]

Multiply (3.2) by the coefficients and sum. Cauchy–Schwarz in the two finite ranges bounds the accumulated error by \(O(P\sqrt P\,\|a\|_2\|b\|_2/H)=O(\|a\|_2\|b\|_2)\). Since \(y^c\le e\),

\[
\max_u\left|\sum_{mn\le u}a_mb_n\chi(mn)\right|
\ll\int_{-H}^H\frac{|A_t(\chi)B_t(\chi)|}{|c+it|}\,dt
+\|a\|_2\|b\|_2.
\tag{3.3}
\]

The right side no longer depends on the endpoint. Its summed error is \(O(Q^2\|a\|_2\|b\|_2)\), because \(\sum_{q\le Q}(q/\varphi(q))\sum_\chi^*1\le\sum_{q\le Q}q\le Q^2\). At every \(t\), (2.2) applies to \(a_mm^{-c-it}\), \(b_nn^{-c-it}\), whose norms do not increase. Finally \(\int_{-H}^Hdt/|c+it|\ll\log(2H/c)\ll\log(2P)\), and \(\sqrt{(M+Q^2)(N+Q^2)}\ge Q^2\) absorbs the error. This also covers \(P=1\). \(\square\)

The logarithm comes from a kernel of size \(1/|t|\), rather than a union bound over all endpoints. Removing the endpoint from the majorant is what permits a different maximum for each character.

For a restricted maximum \(0\le u\le x\), \(x\ge1\), first truncate both supports to indices at most \(\lfloor x\rfloor\). Their norms cannot increase, and their new support product is at most \(x^2\). Thus (3.1) also holds with \(\log(2x)\) in place of \(\log(2MN)\), retaining the original support factors \(M+Q^2\), \(N+Q^2\). This version is valid at \(x=1\) as well.

## 4. Fixed-modulus orthogonality and inducing characters

For \(\chi\pmod q\), let \(\chi^*\) be its unique primitive inducing character. Each primitive character with conductor dividing \(q\) occurs exactly once. On one period modulo \(q\), the functions \(\chi^*(n)\) are pairwise orthogonal: the product of two distinct ones, extended to the least common multiple of their conductors, is nonprincipal, since uniqueness of primitive induction would otherwise identify them. Its complete sum, including the multiple \(q\), is zero. A function with conductor \(d\mid q\) has squared norm \(q\varphi(d)/d\le q\).

Bessel's inequality for these orthogonal vectors, equivalently the norm identity for their linear combinations and duality, therefore gives

\[
\sum_{\chi\bmod q}\left|\sum_{n=1}^q a_n\chi^*(n)\right|^2
\le q\sum_{n=1}^q|a_n|^2.
\tag{4.1}
\]

This includes the conductor-one function, with squared norm \(q\). Evaluating \(\chi^*\) differs from evaluating the imprimitive \(\chi\), which vanishes at every nonunit modulo \(q\).

For a block of \(N\) consecutive integers, put \(k=\lfloor(N-1)/q\rfloor+1\). Group its coefficients into residue classes. Each contains at most \(k\) terms, so Cauchy–Schwarz and ordinary character orthogonality give

\[
\sum_{\chi\bmod q}\left|\sum_{M<n\le M+N}a_n\chi(n)\right|^2
\le k\varphi(q)\sum_{\substack{M<n\le M+N\\(n,q)=1}}|a_n|^2.
\tag{4.2}
\]

Using (4.1) in place of ordinary orthogonality gives

\[
\sum_{\chi\bmod q}\left|\sum_{M<n\le M+N}a_n\chi^*(n)\right|^2
\le kq\sum_{M<n\le M+N}|a_n|^2.
\tag{4.3}
\]

Empty blocks contribute zero. These are the fixed-modulus inputs for the hybrid estimates.

## 5. Gallagher's logarithmic window

For a finite Dirichlet polynomial \(D(t)=\sum_n c_n n^{-it}\) and \(h>0\), define \(W(u)=\sum_{|\log n-u|\le h/2}c_n\). Its Fourier transform with kernel \(e^{-itu}\) is \(h\operatorname{sinc}(th/2)D(t)\), where \(\operatorname{sinc}(v)=\sin v/v\). We have the exact identity

\[
\int_{\mathbb R}|h\operatorname{sinc}(th/2)D(t)|^2\,dt
=2\pi\int_{\mathbb R}|W(u)|^2\,du.
\tag{5.1}
\]

Here no general Plancherel theorem is needed. Expand both finite quadratic forms. The overlap of two intervals of length \(h\), centered at \(\log m\) and \(\log n\), is \((h-|\log(m/n)|)_+\). For their separation \(d\), the integral on the left is

\[
\int_{\mathbb R}\frac{4\sin^2(th/2)}{t^2}\cos(dt)\,dt
=\pi\bigl(|h+d|+|h-d|-2|d|\bigr)=2\pi(h-|d|)_+.
\]

Rewrite its numerator as a sum of \(1-\cos(at)\) terms, and use \(\int_{\mathbb R}(1-\cos(at))dt/t^2=\pi|a|\), obtained by integration by parts and the sine-integral normalization in the preceding lesson. Absolute convergence justifies the finite expansions.

For \(|t|\le1/h\), \(|\operatorname{sinc}(th/2)|\ge1/2\). Center a time interval by replacing \(c_n\) with \(c_nn^{-i(A+T/2)}\), preserving magnitudes, and take \(h=1/T\). Setting \(y=e^{u-h/2}\) in (5.1) proves

\[
\int_A^{A+T}|D(t)|^2\,dt
\ll T^2\int_0^\infty
\left|\sum_{y<n\le e^{1/T}y}c_nn^{-i(A+T/2)}\right|^2\frac{dy}y.
\tag{5.2}
\]

This holds for every \(T>0\). Changing window endpoints affects a set of \(y\) of measure zero.

## 6. Continuous hybrid large sieves

Put \(D(t,\chi)=\sum_{n\le N}a_n\chi(n)n^{-it}\).

**Theorem 6.1.** Uniformly for real \(A\), \(T>0\),

\[
\sum_{\chi\bmod q}\int_A^{A+T}|D(t,\chi)|^2\,dt
\ll\frac{\varphi(q)}q\sum_{\substack{n\le N\\(n,q)=1}}|a_n|^2(qT+n),
\tag{6.1}
\]

\[
\sum_{\chi\bmod q}\int_A^{A+T}|D(t,\chi^*)|^2\,dt
\ll\sum_{n\le N}|a_n|^2(qT+n),
\tag{6.2}
\]

and, for \(Q\ge1\),

\[
\boxed{\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\int_A^{A+T}|D(t,\chi)|^2\,dt
\ll\sum_{n\le N}|a_n|^2(Q^2T+n).}
\tag{6.3}
\]

**Proof for \(T\ge1\).** Apply (5.2) to each character. Put \(\tau=e^{1/T}\), so \(\tau-1\asymp1/T\). The integer window \((y,\tau y]\) has span at most \((\tau-1)y\). Equations (4.2), (4.3) and (1.3) bound its summed energy, respectively, by

\[
\frac{\varphi(q)}q\bigl(q+(\tau-1)y\bigr)
\sum_{\substack{y<n\le\tau y\\(n,q)=1}}|a_n|^2,
\]

\[
\bigl(q+(\tau-1)y\bigr)\sum_{y<n\le\tau y}|a_n|^2,
\qquad
\bigl(Q^2+(\tau-1)y\bigr)\sum_{y<n\le\tau y}|a_n|^2.
\]

The span \(N_y-1\) in the sharp large sieve avoids an extra unit in the last expression. Interchange the nonnegative sum and integral. Index \(n\) occurs for \(n/\tau\le y<n\), and

\[
T^2\int_{n/\tau}^n\bigl(Q^2+(\tau-1)y\bigr)\frac{dy}y
=Q^2T+T^2(\tau-1)n(1-\tau^{-1})\ll Q^2T+n.
\]

The other two cases have the same calculation with \(q\) in place of \(Q^2\). The constants are absolute for \(T\ge1\).

**The small-height range.** The logarithmic window becomes too long if \(T<1\). A three-range argument gives all the same estimates. Treat (6.3) first; write \(B=Q^2\), \(H=BT\), and use the \(L^2\) norm over the weighted family and the interval \([A,A+T]\).

For indices \(n\le H\), the pointwise large sieve, integrated over this interval, gives squared norm at most \(T(B+H)\sum_{n\le H}|a_n|^2\le2H\sum_{n\le H}|a_n|^2\). For \(n>B\), enlarge the time interval to length 1 and apply the already proved case of (6.3). Since \(B+n\le2n\), this gives squared norm \(\ll\sum_{n>B}n|a_n|^2\).

Partition the middle indices \(H<n\le B\) into blocks \((x_j,2x_j]\), where \(x_j=2^jH\), clipping the last at \(B\). The pointwise large sieve gives squared norm on a block at most \(T(B+x_j)E_j\), where \(E_j\) is its coefficient energy. The triangle inequality for the family-time \(L^2\) norm and Cauchy–Schwarz therefore bound the total middle norm by

\[
\sum_j\sqrt{T(B+x_j)E_j}
\le\left(\sum_j(2^{-j}+T)\right)^{1/2}
\left(\sum_jx_jE_j\right)^{1/2}
\ll\left(\sum_{H<n\le B}n|a_n|^2\right)^{1/2}.
\]

There are at most \(1+\log_2(1/T)\) blocks, and \(T(1+\log_2(1/T))\) is uniformly bounded. The geometric sum is bounded as well. Empty blocks, including initial blocks below 1 when \(H<1\), contribute zero. Add the three norms and square, using \((u+v+w)^2\le3(u^2+v^2+w^2)\); this proves (6.3) for \(0<T<1\).

For (6.1) use the same argument with \(B=q\), restrict to units, and retain the common factor \(\varphi(q)/q\). For (6.2) again use \(B=q\), now with (4.3) and no unit restriction. Their pointwise block bounds are precisely the bounds required above. This finishes all positive heights. \(\square\)

## 7. Sampling at separated heights and to the right

Let \(T\ge2\), \(0<\delta\le1\). For each character, choose points \(t_r(\chi)\in[A,A+T]\), separated by at least \(\delta\) for that character. Points belonging to different characters need not be separated. The midpoint inequality proved in the analytic large sieve lesson, applied to \(|D(t,\chi)|^2\) on an interval of length \(\delta\), gives

\[
|D(t_r,\chi)|^2\le\delta^{-1}\int_{t_r-\delta/2}^{t_r+\delta/2}|D(t,\chi)|^2dt
+\int_{t_r-\delta/2}^{t_r+\delta/2}|D(t,\chi)D_t'(t,\chi)|dt.
\tag{7.1}
\]

The intervals have disjoint interiors for each character. Sum (7.1), then use Cauchy–Schwarz for the character-time measure. Theorem 6.1 applies on \([A-1,A+T+1]\), of length at most \(2T\), both to \(a_n\) and to \(-ia_n\log n\). Consequently

\[
\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*\sum_r
\left|\sum_{n\le N}a_n\chi(n)n^{-it_r(\chi)}\right|^2
\ll\left(\delta^{-1}+\log(2N)\right)
\sum_{n\le N}|a_n|^2(Q^2T+n).
\tag{7.2}
\]

The corresponding fixed-modulus estimates have, respectively, right sides

\[
\begin{aligned}
\left(\delta^{-1}+\log(2N)\right)\frac{\varphi(q)}q
\sum_{\substack{n\le N\\(n,q)=1}}|a_n|^2(qT+n),\\
\left(\delta^{-1}+\log(2N)\right)\sum_{n\le N}|a_n|^2(qT+n).
\end{aligned}
\tag{7.3}
\]

for evaluation at \(\chi\) and \(\chi^*\), respectively. This proves the separated-height hybrid bounds, including their coefficientwise weights.

One can also sample \(s_r=\sigma_r+it_r\) anywhere in \(\sigma_r\ge0\). The exact loss is a slowly varying weight

\[
W_N(n)=1+\log\left(\frac{\log(2N)}{\log(2n)}\right)\ge1.
\tag{7.4}
\]

**Theorem 7.1.** Under the preceding separation assumptions, with arbitrary \(\sigma_r\ge0\),

\[
\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*\sum_r
\left|\sum_{n\le N}a_n\chi(n)n^{-s_r(\chi)}\right|^2
\ll\left(\delta^{-1}+\log(2N)\right)
\sum_{n\le N}|a_n|^2(Q^2T+n)W_N(n).
\tag{7.5}
\]

The two fixed-modulus forms are obtained from (7.3) by multiplying every coefficient energy by the same \(W_N(n)\).

**Proof.** Write \(D_u(t,\chi)=\sum_{n\le u}a_n\chi(n)n^{-it}\). Partial summation gives, for \(\sigma\ge0\),

\[
\sum_{n\le N}a_n\chi(n)n^{-\sigma-it}
=N^{-\sigma}D_N(t,\chi)+\sigma\int_1^N D_u(t,\chi)u^{-\sigma-1}du.
\]

The nonnegative weights on the right have total mass 1, including the case \(\sigma=0\). Jensen's inequality therefore bounds its squared modulus by the same average of \(|D_u|^2\). For \(1\le u<2\), only \(a_1\) occurs; for \(u\ge2\),
\(\sup_{\sigma\ge0}\sigma u^{-\sigma}=1/(e\log u)\). Hence, uniformly in the real part,

\[
\left|\sum_{n\le N}a_n\chi(n)n^{-\sigma-it}\right|^2
\le |a_1|^2+|D_N(t,\chi)|^2
+\frac1e\int_2^N\frac{|D_u(t,\chi)|^2}{u\log u}\,du,
\tag{7.6}
\]

where the integral is omitted if \(N<2\). Apply (7.2) to each truncated polynomial, enlarging its logarithmic factor to \(\log(2N)+\delta^{-1}\). The constant term costs at most \(O(Q^2T\delta^{-1}|a_1|^2)\), since each character has at most \(1+T/\delta\) sample points and the total weighted character count is at most \(Q^2\). Interchanging the remaining nonnegative integrals and sums, coefficient \(n\) acquires

\[
\int_{\max(2,n)}^N\frac{du}{u\log u}
=\log\left(\frac{\log N}{\log\max(2,n)}\right)
\ll W_N(n)
\]

when the integration interval is nonempty. For \(n\ge2\), use \(\log(2n)\le2\log n\); for \(n=1\), absorb the bounded change of logarithm into the added 1. The \(|D_N|^2\) term supplies the other part of that 1. The fixed-modulus cases use their own versions of (7.3); their character counts are \(\varphi(q)\le q\), compatible with both stated energies. This proves all three assertions. \(\square\)

The outer logarithm in (7.4) is essential: this is \(1+\log(\log(2N)/\log(2n))\), not a quotient with only the numerator inside a second logarithm.

## 8. The divisor energy for fourth moments

Squaring an \(L\)-function replaces the coefficients 1 by \(d(n)\), the number of divisors of \(n\). We need the following elementary estimates, with \(X\ge1\):

\[
\sum_{n\le X}d(n)^2\ll X\log^3(2X),\qquad
\sum_{n\le X}\frac{d(n)^2}{n}\ll\log^4(2X).
\tag{8.1}
\]

Indeed \(d(n)^2\le d_4(n)\): at a prime power, this is
\((k+1)^2\le\binom{k+3}{3}\), equivalent for \(k\ge0\) to \(k(k-1)\ge0\). Multiply over primes. Counting ordered products of four positive integers then gives

\[
\sum_{n\le X}d_4(n)
=\sum_{abc\le X}\left\lfloor\frac X{abc}\right\rfloor
\le X\left(\sum_{m\le X}\frac1m\right)^3,
\]

and

\[
\sum_{n\le X}\frac{d_4(n)}n
=\sum_{abcd\le X}\frac1{abcd}
\le\left(\sum_{m\le X}\frac1m\right)^4.
\]

Partial summation, or summation over dyadic blocks, further yields

\[
\begin{aligned}
\sum_{n\le X}d(n)^2n^{-1+\theta}&\ll_\theta X^\theta\log^3(2X),\\
\sum_{n>X}d(n)^2n^{-1-\theta}&\ll_\theta X^{-\theta}\log^3(2X).
\end{aligned}
\tag{8.2}
\]

for every fixed \(\theta>0\). The constants can be chosen uniformly when \(\theta\) ranges in a compact subinterval of \((0,\infty)\): the geometric block sums, including the factors \((1+j)^3\) in the tail, converge uniformly. These estimates will also control the two remainders of our smoothing formula.

## 9. A smoothed functional equation, with its remainders

Here is a self-contained bridge from the functional equation in lesson 05 to the fourth moment. For a primitive character of conductor \(q\) and parity \(a\in\{0,1\}\), put

\[
G_\chi(s)=\left(\frac q\pi\right)^{s+a}\Gamma\left(\frac{s+a}{2}\right)^2.
\]

Thus \(G_\chi(s)L(s,\chi)^2=\Lambda(s,\chi)^2\), and the completed functional equation reads
\(\Lambda(s,\chi)^2=\varepsilon_\chi^2\Lambda(1-s,\overline\chi)^2\), with \(|\varepsilon_\chi|=1\). Throughout this section take \(3/10\le\Re s\le7/10\). Define the absolutely convergent integral

\[
I_\chi(s)=\frac1{2\pi i}\int_{(1)}
\frac{G_\chi(s+w)}{G_\chi(s)}L(s+w,\chi)^2\frac{e^{w^2}}w\,dw.
\tag{9.1}
\]

The notation \(\int_{(c)}\) means upward integration on \(\Re w=c\). For \(q>1\) the completed function is entire. Shift the line from 1 to \(-1\); its only pole is the factor \(1/w\), of residue \(L(s,\chi)^2\). The functional equation followed by \(w\mapsto-w\) turns the new integral into
\(-\varepsilon_\chi^2G_\chi(1-s)I_{\overline\chi}(1-s)/G_\chi(s)\). Hence

\[
L(s,\chi)^2=I_\chi(s)
+\varepsilon_\chi^2\frac{G_\chi(1-s)}{G_\chi(s)}I_{\overline\chi}(1-s)-P_\chi(s).
\tag{9.2}
\]

Here \(P_\chi=0\) for \(q>1\). For \(q=1\), the primitive character is the zeta function, and \(P_\chi\) is exactly the sum of the residues of
\(\Lambda(s+w)^2 e^{w^2}/(wG_\chi(s))\) at \(w=-s,1-s\). They are double poles. Neither is \(w=0\) in our strip. All shifts are justified by the Gaussian decay on horizontal sides, the functional equation, and the fixed-strip growth established in lesson 05.

For later use,

\[
|P_1(\sigma+it)|\ll e^{-t^2/2}
\quad(3/10\le\sigma\le7/10).
\tag{9.3}
\]

To verify this, write the two fixed Laurent expansions of \(\Lambda(z)^2\) at \(z=0,1\). Each residue is a linear combination of the value and derivative of \(e^{w^2}/w\) at \(w=-s\) or \(1-s\), divided by \(G_1(s)\). Their real parts stay a distance at least \(3/10\) from zero. The values are bounded by a fixed polynomial in \(1+|t|\) times \(e^{-t^2}\); the reciprocal gamma square is bounded by another such polynomial times \(e^{\pi|t|/2}\), by Stirling's formula. The resulting expression is \(O(e^{-t^2/2})\) for large \(|t|\), and is bounded on the remaining compact set. This proves (9.3), rather than discarding the principal character.

Let \(b=1/4\) and \(X\ge1\). On the line in (9.1), expand the absolutely convergent series
\(L(s+w,\chi)^2=\sum_{n\ge1}d(n)\chi(n)n^{-s-w}\), and split it at \(X\). Shift only the finite part to \(\Re w=-b\), crossing the residue at zero. Since \(\Re(s-b)>0\), no gamma pole is crossed. We obtain the exact decomposition

\[
I_\chi(s)=\sum_{n\le X}d(n)\chi(n)n^{-s}+E^-_\chi(s;X)+E^+_\chi(s;X),
\tag{9.4}
\]

where

\[
E^-_\chi(s;X)=\frac1{2\pi i}\int_{(-b)}
\frac{G_\chi(s+w)}{G_\chi(s)}\frac{e^{w^2}}w
\sum_{n\le X}d(n)\chi(n)n^{-s-w}\,dw,
\tag{9.5}
\]

\[
E^+_\chi(s;X)=\frac1{2\pi i}\int_{(1)}
\frac{G_\chi(s+w)}{G_\chi(s)}\frac{e^{w^2}}w
\sum_{n>X}d(n)\chi(n)n^{-s-w}\,dw.
\tag{9.6}
\]

The positive line remains at 1 so that the infinite tail is absolutely convergent throughout the prescribed strip.

To estimate these formulas in a family, group conductors in \(R/2<q\le R\), where \(R\ge1\), and heights in \([U,2U]\), where \(U\ge1\). We may instead use \([0,2]\) when \(U=1\), or shorten any of these intervals. Set \(X=R(U+1)\), so \(X\asymp q(1+|t|)\). Uniformly in these blocks, for \(u=-b\) or \(u=1\),

\[
\left|\frac{G_\chi(s+u+iv)}{G_\chi(s)}\right|
\ll X^u(1+|v|)^C e^{C|v|},
\qquad
\left|\frac{G_\chi(1-s)}{G_\chi(s)}\right|
\ll\bigl(q(1+|t|)\bigr)^{1-2\sigma}.
\tag{9.7}
\]

Here and below \(C\) denotes an absolute fixed constant, not necessarily the same at different occurrences. For completeness, fixed-strip Stirling bounds the modulus of a gamma square at height \(t\) by constants times
\((1+|t|)^{\Re z-1}e^{-\pi|t|/2}\), where \(z\) is its unsplit argument \(s+a\). On \(|v|\le(1+|t|)/2\), the polynomial factors in the ratio are comparable to \((1+|t|)^u\), and the exponential ratio is at most \(e^{\pi|v|/2}\). On the complementary range, \(1+|t|\ll1+|v|\); any extra polynomial factors are absorbed into \((1+|v|)^C\), while the same exponential bound still holds. On bounded heights, the gamma arguments have positive real parts and no poles or zeros, so compactness supplies the bounds. The conductor factor contributes \((q/\pi)^u\). The second assertion follows directly by comparing the arguments \(1-s+a\) and \(s+a\) at opposite heights. This proves (9.7) using the Stirling estimates imported in lesson 05.

Use the weighted family-time norm

\[
\|F\|_{R,U}^2=
\sum_{R/2<q\le R}\frac q{\varphi(q)}\sum_\chi^*
\int_J |F(t,\chi)|^2dt,
\]

where \(J\) is one of the preceding intervals. If \(s=\sigma+it\), the continuous hybrid sieve, including translated intervals, gives

\[
\left\|\sum_n c_n\chi(n)n^{-it-iv}\right\|_{R,U}^2
\ll\sum_n|c_n|^2(R^2U+n)
\tag{9.8}
\]

for every real \(v\). Infinite coefficient sequences with finite right side follow by completing finite partial sums in this \(L^2\) norm.

Write \(\eta=\sigma-1/2\), and assume
\(|\eta|\le1/(4\log(QT))\), where \(Q,T\ge2\), \(R\le Q\), \(U\le T\). This places \(\sigma\) strictly between \(3/10\) and \(7/10\). Moreover \(X^{2|\eta|}\ll1\), uniformly: \(X\le Q(T+1)\le(3/2)QT\). Equations (8.1), (8.2), and (9.8) imply

\[
\left\|\sum_{n\le X}d(n)\chi(n)n^{-\sigma-it}\right\|_{R,U}^2
\ll(R^2U+X)\log^4(2X)
\ll R^2U\log^4(2X).
\tag{9.9}
\]

In the last inequality \(X=R(U+1)\le2R^2U\). For the first, the \(R^2U\) term uses \(n^{-2\eta}\le X^{2|\eta|}\) and the second part of (8.1); the term with \(n\) uses (8.2) with \(\theta=2-2\sigma>0\).

Minkowski's integral inequality in (9.5), combined with (9.7) and the Gaussian, gives

\[
\|E^-_\chi(\sigma+it;X)\|_{R,U}^2
\ll X^{-2b}\sum_{n\le X}d(n)^2n^{-2\sigma+2b}(R^2U+n)
\ll(R^2U+X)\log^3(2X).
\tag{9.10}
\]

Indeed the \(v\) kernel is bounded by a constant times
\(e^{-v^2+C|v|}(1+|v|)^C/|{-b+iv}|\), with a finite integral. In (8.2) the head exponent \(\theta=2b-2\eta\) stays in a compact positive interval, and after multiplication by \(X^{-2b}\) leaves the bounded factor \(X^{-2\eta}\). The additional \(n\) leaves \(X^{1-2\eta}\). Thus all constants in (9.10) are uniform in the stated strip.

Likewise the absolutely convergent tail in (9.6) satisfies

\[
\|E^+_\chi(\sigma+it;X)\|_{R,U}^2
\ll X^2\sum_{n>X}d(n)^2n^{-2\sigma-2}(R^2U+n)
\ll(R^2U+X)\log^3(2X).
\tag{9.11}
\]

For the two tail sums, use (8.2) with \(\theta=2\sigma+1\) and \(\theta=2\sigma\). They leave respectively \(X^{-2\eta}\) and \(X^{1-2\eta}\). The \(v\) kernel on the line 1 is again integrable. Finite tail truncations prove the bound first; their bounds and convergence pass it to the infinite tail. Equations (9.9)–(9.11) therefore control the exact integral (9.1), with no unspecified approximation error.

## 10. Family fourth moments and their two consequences

**Theorem 10.1.** For \(Q,T\ge2\) and
\(|\sigma-1/2|\le1/(4\log(QT))\),

\[
\sum_{q\le Q}\sum_\chi^*\int_0^T|L(\sigma+it,\chi)|^4dt
\ll Q^2T\log^4(QT).
\tag{10.1}
\]

**Proof.** In each conductor-height block of section 9, (9.4) and (9.9)–(9.11) give \(\|I_\chi(s)\|_{R,U}^2\ll R^2U\log^4(2X)\). The same estimate holds for \(I_{\overline\chi}(1-s)\): replace \(\sigma\) by \(1-\sigma\), conjugate the character, and reflect the height interval. The hybrid estimate permits every translated interval, so reflection causes no change. In the prescribed strip the second bound in (9.7) is \(O(1)\), because \(q(1+|t|)\le Q(T+1)\). Thus the functional equation decomposition (9.2), the triangle inequality, and (9.3) imply

\[
\sum_{R/2<q\le R}\frac q{\varphi(q)}\sum_\chi^*
\int_J|L(\sigma+it,\chi)|^4dt
\ll R^2U\log^4(2X).
\]

The principal conductor-one residue contributes an absolutely bounded integral, compatible with this bound if it lies in the block. Cover \(q\le Q\) by disjoint descending dyadic conductor blocks, the last of which contains 1. Cover \([0,T]\) by \([0,\min(2,T)]\) and successive dyadic height intervals, shortening the last. The sums of \(R^2\) and \(U\) over these blocks are \(O(Q^2)\) and \(O(T)\), respectively. Also \(\log(2X)\ll\log(QT)\). Summing gives the asserted bound, even with the weights \(q/\varphi(q)\); dropping them proves (10.1). \(\square\)

**Corollary 10.2.** For \(Q,T\ge2\),

\[
\sum_{q\le Q}\sum_\chi^*\int_0^T
|L(1/2+it,\chi)L'(1/2+it,\chi)|^2dt
\ll Q^2T\log^6(QT).
\tag{10.2}
\]

**Proof.** Put \(F(s)=L(s,\chi)^2\), so \(F'=2LL'\), and take
\(r=1/(16\log(Q(T+1)))\). Every circle of radius \(r\) centered at \(1/2+it\), \(0\le t\le T\), avoids the principal pole at 1. Cauchy's integral formula and Cauchy–Schwarz on the circle give

\[
|F'(1/2+it)|^2\le r^{-2}\frac1{2\pi}\int_0^{2\pi}
|L(1/2+it+re^{i\theta},\chi)|^4d\theta.
\]

For each \(\theta\), the real part is within \(r\) of \(1/2\), and the translated heights lie in \([-1,T+1]\). Apply (10.1) with height \(T+1\), and use \(L(\sigma-it,\chi)=\overline{L(\sigma+it,\overline\chi)}\) to cover negative heights. The radius lies within the required strip at that height. Integrate, sum, and use \(r^{-2}\ll\log^2(QT)\). Dividing by 4 proves (10.2). \(\square\)

**Corollary 10.3.** Let \(\delta>0\), \(Q,T\ge2\). For every primitive character choose points in \([\delta/2,T-\delta/2]\), separated by at least \(\delta\) for that character. Then

\[
\sum_{q\le Q}\sum_\chi^*\sum_r|L(1/2+it_r(\chi),\chi)|^4
\ll\left(\delta^{-1}+\log(QT)\right)Q^2T\log^4(QT).
\tag{10.3}
\]

**Proof.** The midpoint intervals of length \(\delta\) have disjoint interiors and lie in \([0,T]\). Apply the midpoint inequality to \(f(t)=|L(1/2+it,\chi)^2|^2\). Its derivative has modulus at most \(4|L|^2|LL'|\), so their summed bound is

\[
\delta^{-1}\sum_{q\le Q}\sum_\chi^*\int_0^T|L|^4dt
+2\sum_{q\le Q}\sum_\chi^*\int_0^T|L|^2|LL'|dt.
\]

Cauchy–Schwarz and (10.1), (10.2) bound the second term by
\(O(Q^2T\log^5(QT))\). This proves (10.3) for every positive \(\delta\); if \(\delta>T\), there are no sample points. \(\square\)

The fourth power of the logarithm comes from the energy of the divisor coefficients. Differentiation costs two further logarithms in the integrated square, and sampling takes the geometric mean of those two moment bounds.

## 11. A Type II estimate for the prime-sum decomposition

Let \(x,Q\ge2\), \(1\le U,V\le x\), and let \(r\ge1\) be an integer. Define

\[
\alpha(m)=\sum_{\substack{d\mid m\\d>U}}\Lambda(d),\qquad
\beta(n)=\mu(n)\mathbf1_{n>V},\qquad
\Lambda^\flat=\alpha*\beta.
\]

Here \(*\) is Dirichlet convolution. We have \(0\le\alpha(m)\le\log m\), because
\(\sum_{d\mid m}\Lambda(d)=\log m\): at each prime power \(p^k\Vert m\), the contributing divisors are \(p,\ldots,p^k\), whose values sum to \(k\log p\). Also \(\alpha(m)=0\) for \(m\le U\), and \(|\beta(n)|\le1\).

**Corollary 11.1.** Uniformly in \(r\),

\[
\sum_{q\le Q}\frac q{\varphi(q)}\sum_\chi^*
\max_{0\le y\le x}\left|\sum_{k\le y}\Lambda^\flat(k)\chi(k)\mathbf1_{(k,r)=1}\right|
\ll\left(x+\frac{Qx}{\sqrt U}+\frac{Qx}{\sqrt V}+Q^2\sqrt x\right)\log^3(2x).
\tag{11.1}
\]

**Proof.** If \(UV\ge x\), the sum is empty. Otherwise partition \(U<m\le x/V\) into dyadic blocks \((L,2L]\), \(L=2^jU\), clipping the last block. For a fixed block define
\(a_m=\alpha(m)\mathbf1_{L<m\le2L}\mathbf1_{(m,r)=1}\) and
\(b_n=\beta(n)\mathbf1_{n\le x/L}\mathbf1_{(n,r)=1}\). These selectors correctly represent \((mn,r)=1\). Their support lengths satisfy
\(M\ll L\), \(N\le x/L\), and
\(\|a\|_2\|b\|_2\ll\sqrt{x}\log(2x)\). Theorem 3.1, with \(MN\ll x\), bounds this block's weighted maximal sum by

\[
\ll\bigl(x+Q\sqrt{xL}+Qx/\sqrt L+Q^2\sqrt x\bigr)\log^2(2x).
\]

Since \(U\le L<x/V\), the middle two terms are at most constant multiples of \(Qx/\sqrt V\) and \(Qx/\sqrt U\). There are \(O(\log(2x))\) blocks. The triangle inequality bounds the maximum of their sum by the sum of their maxima, proving (11.1). Rounding support lengths changes only absolute constants. \(\square\)

This is the Type II consequence needed in the Bombieri–Vinogradov argument. The next lesson explains why \(\Lambda^\flat\) is one term of Vaughan's identity; this estimate itself required only its displayed convolution and coefficient bounds.

## 12. Exercises

1. **Easy.** Derive the factor \(q/\varphi(q)\) in the multiplicative large sieve, keeping both orthogonality and the Gauss sum normalization explicit.
2. **Medium.** For \(V>0\), bound the number of primitive pairs \((q,\chi)\), \(q\le Q\), for which \(\left|\sum_{n\le N}a_n\chi(n)\right|>V\). Give also a weighted count.
3. **Medium.** Prove the rectangular bilinear estimate without a maximum, and explain why the double sum factors when some indices are nonunits.
4. **Hard.** Prove the bilinear estimate with a different maximizing product cutoff for each character. State the half-integer choice, the truncation height, and how the summed truncation error is absorbed.

## 13. Complete solutions

**1.** The identity \(\chi(n)=\tau(\overline\chi)^{-1}\sum_b\overline\chi(b)e(bn/q)\) gives
\(q\sum_\chi^*|S(\chi)|^2=\sum_\chi^*|\sum_b^*\overline\chi(b)T(b/q)|^2\). Enlarge the last sum to all characters. Expanding the square and using
\(\sum_{\chi\bmod q}\overline\chi(b)\chi(c)=\varphi(q)\mathbf1_{b=c\bmod q}\) for unit \(b,c\) gives \(\varphi(q)\sum_b^*|T(b/q)|^2\). Divide by \(\varphi(q)\), then sum the additive Farey bound. The numerator \(q\) is the squared Gauss sum modulus; the denominator \(\varphi(q)\) is the orthogonality normalization. No imprimitive Gauss identity is used.

**2.** In the subfamily where \(|S|>V\), each energy term exceeds \(V^2\). Thus its weighted size is at most
\((N-1+Q^2)\sum_{n\le N}|a_n|^2/V^2\), by (1.3). Its ordinary size is no greater, since \(q/\varphi(q)\ge1\). If all coefficients vanish the subfamily is empty; if the bound is nonintegral, its integer part is a valid bound for the ordinary size. The parameter \(V\) must be positive.

**3.** Complete multiplicativity gives \(\chi(mn)=\chi(m)\chi(n)\) for all positive integers: if a prime dividing \(q\) divides either factor, both sides are zero. Hence the sum is \(A(\chi)B(\chi)\). In the measure assigning weight \(q/\varphi(q)\) to each primitive character, Cauchy–Schwarz bounds its first absolute moment by the product of the square roots of the two second moments. Applying (1.3) to the supports \(1\le m\le M\), \(1\le n\le N\) gives exactly
\(\sqrt{(M-1+Q^2)(N-1+Q^2)}\,\|a\|_2\|b\|_2\). Replacing \(M-1,N-1\) by \(M,N\) gives the stated coarser version.

**4.** Set \(P=MN\), \(c=1/\log(2P)\), \(H=4P^2\). A product threshold depends only on an integer \(K\in[0,P]\); use \(y=K+1/2\). Then \(|\log(y/(mn))|\ge1/(3P)\), and the scalar Perron error is \(O(P/H)\) per coefficient. Its total for one character is at most
\(O(P\sqrt{MN}\,\|a\|_2\|b\|_2/H)=O(\|a\|_2\|b\|_2)\). The integral is bounded independently of \(K\) by
\(O(\int_{-H}^H|A_t(\chi)B_t(\chi)|dt/|c+it|)\), because \(y^c\le e\). Taking a maximum now is legitimate for each character separately. Sum that common majorant over the family, use solution 3 at every \(t\), and integrate the kernel, whose integral is \(O(\log(2P))\). The total error is \(O(Q^2\|a\|_2\|b\|_2)\), because the weighted primitive count is at most \(Q^2\). It is absorbed by \(\sqrt{(M+Q^2)(N+Q^2)}\log(2P)\,\|a\|_2\|b\|_2\). This proves (3.1), including \(P=1\); a union bound over endpoints is unnecessary.

## 14. Proof scope and references

The multiplicative and maximal bilinear estimates, all three continuous hybrid forms for every positive height, their separated-height and right-half-plane versions, the family fourth moment in its full stated strip, both moment corollaries, and the Type II consequence are proved above. The imported inputs are the sharp additive large sieve and midpoint inequality proved in *The large sieve inequality*, the primitive Gauss identity proved in *Gauss sums*, the scalar Perron kernel used in *Counting zeros and the explicit formula for character sums over prime powers*, and the completed functional equation and fixed-strip gamma bounds used in *The functional equation of Dirichlet L-functions*.

- D. Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), AMS, 2019, author's preliminary version, Theorem 25.15, Theorem 26.6 and Corollary 26.7: the character transfer, maximal product-cutoff estimate and Type II consequence.
- P. X. Gallagher, “A large sieve density estimate near \(\sigma=1\),” [*Inventiones Mathematicae* 11 (1970), 329–339](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0011/LOG_0035.pdf): the logarithmic short-window method underlying the hybrid large sieve.

The cutoff and fourth moment arguments here retain their explicit truncation and smoothing remainders. The final cited work supplies historical attribution for Gallagher's method; its density theorem is not an input to this lesson.
