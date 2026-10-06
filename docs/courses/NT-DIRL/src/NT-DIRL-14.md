# Vaughan's identity and sums over primes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An exponential phase is simple on an arithmetic progression, but primes do not form a progression. Vaughan's identity expresses the prime weight as a sum of convolutions. Some have a short coefficient sequence and a smooth second factor; others have two long variables. Geometric sums handle the first type. Cauchy–Schwarz and separation of phases handle the second.

We use the elementary Chebyshev and divisor estimates from *Counting primes by elementary means*, the divisor-square energy proved in *The multiplicative large sieve and bilinear forms with characters*, and the prime and Möbius forms of *The Siegel–Walfisz theorem*. All implied constants below are effective and absolute, except where an epsilon dependence or the ineffectivity of Siegel–Walfisz is explicitly indicated. Write \(e(t)=e^{2\pi it}\), \(\|t\|=\min_{k\in\mathbb Z}|t-k|\), and \(f_{\le Y}=f\mathbf1_{n\le Y}\), \(f_{>Y}=f-f_{\le Y}\).

## 1. The convolution identity

Let \(\mathbf1(n)=1\), \(\ell(n)=\log n\), and \(\epsilon(n)=\mathbf1_{n=1}\). Dirichlet convolution has identity \(\epsilon\). Prime factorization gives

\[
\mu*\mathbf1=\epsilon,\qquad \Lambda*\mathbf1=\ell,\qquad \mu*\ell=\Lambda.
\tag{1.1}
\]

For \(U,V\ge1\), split \(\mu\) at \(V\) and \(\Lambda\) at \(U\). Since
\(\mu_{>V}*\mathbf1=\epsilon-\mu_{\le V}*\mathbf1\), associativity gives

\[
\begin{aligned}
\Lambda
&=\mu_{\le V}*\ell+\mu_{>V}*\mathbf1*(\Lambda_{\le U}+\Lambda_{>U})\\
&=\mu_{\le V}*\ell-(\Lambda_{\le U}*\mu_{\le V})*\mathbf1
+(\Lambda_{>U}*\mathbf1)*\mu_{>V}+\Lambda_{\le U}.
\end{aligned}
\tag{1.2}
\]

This proves **Vaughan's identity** at every integer, without convergence qualifications. Set
\(c=\Lambda_{\le U}*\mu_{\le V}\), \(\alpha=\Lambda_{>U}*\mathbf1\), \(\beta=\mu_{>V}\). Then

\[
\begin{aligned}
\operatorname{supp}c&\subset[1,UV],& |c(d)|&\le\log d,\\
\alpha(m)&=0\ (m\le U),&0\le\alpha(m)&\le\log m,\\
\beta(n)&=0\ (n\le V),&|\beta(n)|&\le1.
\end{aligned}
\tag{1.3}
\]

The bound for \(c\) uses \(|\mu|\le1\) and \(\sum_{d\mid n}\Lambda(d)=\log n\). The same divisor identity proves the bound for \(\alpha\). Thus the first two convolutions in (1.2) are Type I; \(\alpha*\beta\) is Type II. These labels describe the support and smoothness available to an estimate, rather than additional identities.

Take \(n=12\), \(U=V=2\). The four terms in their displayed order are

\[
\log12-\log6=\log2,\qquad
-\log2+\log2=0,\qquad-\log2,\qquad0.
\tag{1.4}
\]

For the third term, the possible second factors \(n>2\) dividing 12 are 3,4,6,12; their paired first factors are 4,3,2,1. Only 3 contributes: \(\mu(3)=-1\), \(\alpha(4)=\Lambda(4)=\log2\). The factor 4 has Möbius value zero, and \(\alpha(2)=\alpha(1)=0\). Their total is zero, as required by \(\Lambda(12)=0\).

## 2. Geometric sums and the spacing lemma

For a sum with at most \(L\) consecutive integer terms, the geometric-series identity and \(|\sin\pi t|\ge2\|t\|\) give

\[
\left|\sum_{a<n\le b}e(tn)\right|\le\min\left(L,\frac1{2\|t\|}\right).
\tag{2.1}
\]

At \(\|t\|=0\) interpret the second bound as infinity. Let \((b,q)=1\) and \(|\alpha-b/q|\le q^{-2}\). If \(q\ge2\), any block of \(\lfloor q/2\rfloor\) consecutive indices has its phases \(\alpha n\) separated on the circle by at least \(1/(2q)\). Indeed a nonzero difference \(h\), \(|h|\le q/2\), satisfies \(\|bh/q\|\ge1/q\), while \(|h(\alpha-b/q)|\le1/(2q)\).

For such a block, and any added phase \(\eta\), list the distances \(r_j\) of its phases from zero in increasing order. An interval of radius \(r\) contains at most \(1+4qr\) separated points, so \(r_j\ge(j-1)/(4q)\). It follows that

\[
\sum_{n\le Y}\min\bigl(Z,\|\alpha n+\eta\|^{-1}\bigr)
\ll\left(\frac{YZ}q+Y+Z+q\right)\log(2q),
\tag{2.2}
\]

uniformly for \(Y,Z\ge1\), \(\eta\in\mathbb R\). In each block, allow \(Z\) for its closest point and sum \(4q/(j-1)\) for the others. Multiply by \(O(Y/q+1)\). If \(q=1\), the trivial bound \(YZ\) proves (2.2).

A varying cutoff gives a sharper first-moment estimate:

\[
\sum_{d\le D}\min\bigl(x/d,\|\alpha d\|^{-1}\bigr)
\ll(x/q+D+q)\log(2qx),\qquad x\ge2,
\tag{2.3}
\]

where \(d>x\) may be omitted. To prove it for \(2\le q\le x\), put \(h=\lfloor q/2\rfloor\). In the initial block \(1\le d\le h\), all distances are at least \(1/(2q)\), by comparison to \(bd/q\). Its whole reciprocal sum is \(O(q\log(2q))\). In block \(jh<d\le(j+1)h\), \(j\ge1\), the closest point costs at most \(x/(jh)\ll x/(jq)\), and the rest cost \(O(q\log(2q))\). Summing these terms over \(O(D/q+1)\) blocks proves (2.3). If \(q=1\), or \(q>x\), use \(\sum_{d\le x}x/d\ll x\log(2x)\); the right side of (2.3) is then at least a constant multiple of this bound.

## 3. Type I and Type II estimates

**Type I.** For \(a_d\) supported on \(d\le D\), \(|a_d|\le A\), and \(v=0\) or 1,

\[
\left|\sum_{dm\le x}a_d(\log m)^v e(\alpha dm)\right|
\ll A\log^v(2x)(x/q+D+q)\log(2qx).
\tag{3.1}
\]

For \(v=0\), use (2.1) and (2.3). For \(v=1\), partial summation on the inner sum bounds it by \(O(\log(2x)\min(x/d,\|\alpha d\|^{-1}))\): every partial geometric sum has the indicated geometric bound, and the boundary term and the integral of \(dt/t\) each cost at most \(O(\log(2x))\). Then apply (2.3). This proves (3.1), including logarithmic coefficients in Vaughan's first Type I term.

**Type II.** Suppose \(a_m,b_n\) have supports in \(1\le m\le M\), \(1\le n\le N\). For every product cutoff \(x\ge1\),

\[
\left|\sum_{mn\le x}a_mb_n e(\alpha mn)\right|
\ll\left(M+N+q+\frac{MN}q\right)^{1/2}
\log^{1/2}(2q)\,\|a\|_2\|b\|_2.
\tag{3.2}
\]

**Proof.** Cauchy–Schwarz in \(m\) removes \(a_m\). Expanding the remaining square gives inner geometric sums over
\(m\le\min(M,x/n_1,x/n_2)\). Their moduli are bounded by \(\min(M,\|\alpha(n_1-n_2)\|^{-1})\); at equal indices use \(M\). For each fixed \(n_1\), (2.2), with \(Y=N\), \(Z=M\) and \(\eta=-\alpha n_1\), bounds the sum of these moduli by
\(O((MN/q+M+N+q)\log(2q))\). Finally
\(|b_{n_1}b_{n_2}|\le(|b_{n_1}|^2+|b_{n_2}|^2)/2\), so the full expanded sum is bounded by this quantity times \(\|b\|_2^2\). Multiply by \(\|a\|_2^2\) and take a square root. The same proof allows a consecutive interval for the \(m\) support: its intersection with each upper product cutoff is still an interval. \(\square\)

The product cutoff remains inside the geometric sum. No separation by a Mellin integral, and hence no extra Mellin logarithm, is required for this individual additive-phase estimate.

## 4. The exponential sum over prime powers

**Theorem 4.1 (Vinogradov–Vaughan bound).** For \(x\ge2\), \((b,q)=1\), \(|\alpha-b/q|\le q^{-2}\),

\[
\boxed{\sum_{n\le x}\Lambda(n)e(\alpha n)
\ll\left(\frac{x}{\sqrt q}+x^{4/5}+\sqrt{xq}\right)\log^4(2x).}
\tag{4.1}
\]

**Proof.** If \(q>x\), the trivial bound \(\sum_{n\le x}\Lambda(n)\ll x\) is already enough. Suppose \(q\le x\). The two Type I terms of (1.2), estimated by (3.1) and (1.3), contribute
\(O((x/q+UV+q)\log^2(2xUV))\). The short term contributes \(O(U)\), by Chebyshev.

For the Type II term partition \(U<m\le x/V\) into blocks \((L,2L]\), \(L=2^jU\), clipping the last. On a block \(\|\alpha\|_2\ll\sqrt L\log(2x)\), \(\|\beta_{\le x/L}\|_2\le\sqrt{x/L}\). Apply (3.2) with \(M\ll L\), \(N\le x/L\), so \(MN\ll x\). Its contribution is

\[
\ll\left(\frac{x}{\sqrt q}+\sqrt{xL}+\frac{x}{\sqrt L}+\sqrt{xq}\right)\log^{3/2}(2x).
\]

Here \(U\le L<x/V\); the middle terms are \(O(x/\sqrt V+x/\sqrt U)\). There are \(O(\log(2x))\) blocks. Combining all four terms yields

\[
\ll\left(U+UV+\frac{x}{\sqrt q}+\frac{x}{\sqrt U}
+\frac{x}{\sqrt V}+\sqrt{xq}\right)\log^{5/2}(2xUV),
\tag{4.2}
\]

where \(x/q\le x/\sqrt q\) and \(q\le\sqrt{xq}\). Choose \(U=V=x^{2/5}\). Then \(UV=x^{4/5}\), and \(x/\sqrt U=x/\sqrt V=x^{4/5}\). This proves (4.1); in fact the displayed argument proves the stronger power \(5/2\) of the logarithm, with \(\log(2x)\). \(\square\)

Both variables must be long for the Type II gain. Balancing their losses \(x/\sqrt U,x/\sqrt V\) against the Type I support \(UV\) explains the exponent \(4/5\).

## 5. A Möbius version, with its epsilon stated

The direct Möbius variant has divisor coefficients in its Type I term. We prove the precise estimate

\[
\sum_{n\le x}\mu(n)e(\alpha n)
\ll_\varepsilon\left(\frac{x}{\sqrt q}+x^{4/5+\varepsilon}+\sqrt{xq}\right)\log^3(2x),
\qquad\varepsilon>0.
\tag{5.1}
\]

The epsilon is in the middle term; it is not silently transferred to the denominator or the square-root terms.

For \(W\ge1\), elementary convolution algebra gives

\[
\mu=2\mu_{\le W}-\mu_{\le W}*\mu_{\le W}*\mathbf1
+\mu_{>W}*\mathbf1*\mu_{>W}.
\tag{5.2}
\]

Indeed expand its right side, use \(\mu*\mathbf1=\epsilon\), and cancel the two mixed terms. In the last term, \(\mu_{>W}*\mathbf1=\epsilon-\mu_{\le W}*\mathbf1\) vanishes on \(n\le W\) and has modulus at most \(d(n)\) elsewhere. Thus its square energy on \(n\le Y\) is \(O(Y\log^3(2Y))\). The other factor has modulus at most 1. Take \(W=x^{2/5}\); dyadic Type II estimation by (3.2) then gives
\(O((x/\sqrt q+x^{4/5}+\sqrt{xq})\log^3(2x))\). The short term is \(O(W)\).

It remains to justify the divisor-weighted Type I bound. For its coefficient sequence \(|c_d|\le d(d)\), \(d\le D_0=W^2=x^{4/5}\), it is enough to bound
\(\sum_{d\le D_0}d(d)\min(x/d,\|\alpha d\|^{-1})\). We give the details, since replacing \(d(d)\) by a logarithm would be false.

For a dyadic block \(D<d\le2D\), Cauchy–Schwarz, \(\sum d(d)^2\ll D\log^3(2D)\), and the spacing argument of section 2 yield

\[
\sum_{D<d\le2D}d(d)\min(x/d,\|\alpha d\|^{-1})
\ll\left(\frac{x}{\sqrt q}+\frac{x}{\sqrt D}+\sqrt{xD}+\sqrt{xq}\right)\log^{3/2}(2x).
\tag{5.3}
\]

To see the squared spacing bound used here, set \(Z=x/D\). Each block of \(\lfloor q/2\rfloor\) indices contributes at most
\(O(Z^2+qZ)\) to \(\sum\min(Z,\|\alpha d\|^{-1})^2\): allow \(Z^2\) for its closest point, then sum \(\min(Z,4q/j)^2\), splitting at \(j=q/Z\). With \(O(D/q+1)\) blocks, multiplying by \(D\log^3(2D)\) and taking a square root proves (5.3). The finitely many initial indices are included by enlarging dyadic blocks or bounding them separately.

On a block wholly within \(1\le d\le q/2\), there is no exceptional closest point, because all distances are at least \(1/(2q)\). The squared sum is instead
\(O(\min(q^2,qZ))\). The corresponding weighted bound is
\(O(\min(q\sqrt D,\sqrt{xq})\log^{3/2}(2x))\).

If \(q\le x^{1/5}\), use this initial-block bound up to \(q/2\), and (5.3) above it. In the latter blocks \(D\gg q\), while \(D\le D_0\); all four terms in (5.3) are \(O(x/\sqrt q)\), since \(\sqrt{xD}\le x^{9/10}\le x/\sqrt q\). Summing \(O(\log(2x))\) blocks is acceptable in (5.1).

If \(q\ge D_0\) and \(q\le x\), the initial-block bound and (5.3) for the possible remaining block above \(q/2\) give \(O(\sqrt{xq}\log^{5/2}(2x))\), because \(q\ge x^{4/5}\) and \(D\ll q\).

In the remaining range \(x^{1/5}<q<D_0\), use the elementary divisor bound \(d(d)\ll_\eta d^\eta\), with \(0<\eta\le\min(\varepsilon,1/10)\). Its proof is short: for sufficiently large primes \(p\), \(k+1\le p^{\eta k}\) for all \(k\ge1\); the finitely many smaller primes have uniformly bounded \((k+1)p^{-\eta k}\). Multiply those finite constants. Equation (2.3) now bounds the weighted Type I sum by
\(O_\eta(x^\eta(x/q+D_0+q)\log(2x))\). Since \(q>x^{1/5}\ge x^{2\eta}\), its first term is at most \(x/\sqrt q\); its other terms are at most \(2x^{4/5+\varepsilon}\). Finally \(q=1\) or \(q>x\) is handled directly by the trivial bound for the original Möbius sum. These cases prove (5.1) completely.

## 6. The classical three-primes theorem

**Theorem 6.1 (Vinogradov).** Every sufficiently large odd integer is a sum of three primes. More precisely, the weighted count defined below satisfies
\(R(N)=\tfrac12\mathfrak S(N)N^2+O_A(N^2(\log N)^{-A})\) for every fixed \(A>0\). The argument here gives no effective numerical threshold, because it uses Siegel–Walfisz.

We give the full special circle-method argument needed for this statement. Let \(N\) be an integer tending to infinity and put
\(S(\theta)=\sum_{n\le N}\Lambda(n)e(n\theta)\). Orthogonality gives the exact weighted count

\[
R(N)=\sum_{n_1+n_2+n_3=N}\Lambda(n_1)\Lambda(n_2)\Lambda(n_3)
=\int_0^1 S(\theta)^3e(-N\theta)d\theta,
\tag{6.1}
\]

where the indices are positive integers. Fix \(A>0\), set \(B=2A+12\), and put \(P=(\log N)^B\). For every reduced \(b/q\) with \(q\le P\), take the interval on the circle of radius \(2P/N\) about \(b/q\). These **major arcs** are disjoint for large \(N\): distinct reduced centers have circle distance at least \(P^{-2}\), and \(4P^3<N\). Their complement consists of the minor arcs.

**Minor arcs.** The elementary Dirichlet approximation lemma follows by placing \(L+1\) fractional parts \(0,\theta,\ldots,L\theta\) into \(L\) equal intervals: two are at distance at most \(1/L\), giving a reduced \(b/q\) with \(q\le L\), \(|\theta-b/q|\le1/(qL)\). Choose \(L=\lfloor N/P\rfloor\). On a minor arc its denominator must exceed \(P\), since otherwise the distance is at most \(1/L\le2P/N\). Also \(q\le N/P\) and \(|\theta-b/q|\le q^{-2}\). Theorem 4.1 gives

\[
\sup_{\mathrm{minor}}|S(\theta)|
\ll\bigl(N/\sqrt P+N^{4/5}\bigr)\log^4(2N).
\]

Orthogonality and Chebyshev give \(\int_0^1|S|^2=\sum_{n\le N}\Lambda(n)^2\ll N\log(2N)\). Thus
\(\left|\int_{\mathrm{minor}}S^3e(-N\theta)d\theta\right|\ll_A N^2(\log N)^{-A}\): the two errors are \(O(N^2\log^{5-B/2}N)\) and \(O(N^{9/5}\log^5N)\), and \(5-B/2=-A-1\).

**Major arcs.** Define \(V(\beta)=\int_0^N e(\beta u)du\). Uniformly for \(q\le P\), \((b,q)=1\), \(|\beta|\le2P/N\), Siegel–Walfisz and partial summation yield

\[
S(b/q+\beta)=\frac{\mu(q)}{\varphi(q)}V(\beta)
+O\bigl(NP^2e^{-c\sqrt{\log N}}\bigr)
\tag{6.2}
\]

for a fixed positive \(c\), with an ineffective threshold. Here are the uniformity details. For every unit class \(h\pmod q\), the estimate
\(\psi(u;q,h)=u/\varphi(q)+O(Ne^{-c\sqrt{\log N}})\) holds simultaneously for \(0\le u\le N\). For \(u\ge\sqrt N\), use Siegel–Walfisz with exponent \(2B\) and decrease its decay constant; for smaller \(u\), the elementary bound \(O(\sqrt N\log N)\), including the proposed main term, is smaller than the displayed error. Partial summation costs \(1+N|\beta|\ll P\), and summing the unit classes costs \(\varphi(q)\le P\). The sum of their phases is \(\sum_{h\bmod q}^*e(bh/q)=\mu(q)\). Nonunit prime powers have primes dividing \(q\) and contribute at most \(O(\log q\log N)\), absorbed in the error. The Ramanujan identity used here follows by inserting \(\mathbf1_{(h,q)=1}=\sum_{d\mid(h,q)}\mu(d)\) into the complete exponential sum.

The total major-arc measure is \(O(P^3/N)\). Since \(|S|,|V|\ll N\), cubing (6.2) and integrating introduces only \(O(N^2P^5e^{-c\sqrt{\log N}})=o(N^2)\). All arcs have the same \(\beta\) interval. Their main contribution is therefore

\[
\left(\sum_{q\le P}\frac{\mu(q)^3c_q(-N)}{\varphi(q)^3}\right)
\int_{-2P/N}^{2P/N}V(\beta)^3e(-N\beta)d\beta,
\tag{6.3}
\]

where \(c_q(k)=\sum_{h\bmod q}^*e(hk/q)\).

**The singular integral.** Since \(|V(\beta)|\le\min(N,1/(\pi|\beta|))\), the omitted integral tail is \(O(N^2/P^2)\). The full integral is exactly \(N^2/2\). Indeed it is the Fourier inversion value at \(N\) of the threefold convolution of \(\mathbf1_{[0,N]}\); that value is the area of \(\{(u_1,u_2):u_1,u_2\ge0,\ u_1+u_2\le N\}\), namely \(N^2/2\). One can justify inversion directly by first inserting \(e^{-\pi\varepsilon\beta^2}\): the Gaussian Fourier identity makes the resulting integral the convolution with a Gaussian approximate identity. The threefold interval convolution is continuous, and \(|V|^3\) is integrable, so both sides converge to the asserted values as \(\varepsilon\downarrow0\). This supplies the required inversion without a distributional endpoint convention.

**The singular series.** The series in (6.3) converges absolutely, uniformly in \(N\). In fact \(|c_q(N)|\le\varphi(q)\), and for squarefree \(q\),
\(\varphi(q)\gg q^{3/4}\): for all sufficiently large primes \(p\), \(p/(p-1)\le p^{1/4}\), while the finitely many smaller primes supply only a fixed factor. Thus the tail beyond \(P\) is \(O(P^{-1/2})\). The Chinese remainder theorem makes \(c_q(N)\) multiplicative in \(q\), and direct complete sums give
\(c_p(N)=p-1\) if \(p\mid N\), and \(-1\) otherwise. Consequently the full series is

\[
\mathfrak S(N)=\prod_p\left(1-\frac{c_p(N)}{(p-1)^3}\right).
\tag{6.4}
\]

Absolute Euler-product convergence also follows from
\(\prod_p(1+(p-1)^{-2})<\infty\). For odd \(N\), the factor at 2 is 2; every odd-prime factor is at least \(1-(p-1)^{-2}\). Their product has a positive absolute lower bound, since \(\sum_{p>2}(p-1)^{-2}<\infty\). Thus \(\mathfrak S(N)\ge c_0>0\), uniformly over odd \(N\). For even \(N\), the factor at 2 vanishes; this is the parity obstruction to three odd primes.

Equations (6.1)–(6.4) prove
\(R(N)=\tfrac12\mathfrak S(N)N^2+O_A(N^2(\log N)^{-A})\). Indeed the singular-series and integral tails are \(O(N^2P^{-1/2})\) and \(O(N^2P^{-2})\), while the exponential major-arc error is smaller than every fixed logarithmic power. Finally remove representations involving a prime power \(p^k\), \(k\ge2\). There are \(O(\sqrt N\log N)\) such values up to \(N\); for any fixed one, at most \(N\) pairs of positive integers have the remaining sum. All three weights are at most \(\log N\). Their total weighted contribution, allowing any of the three positions, is \(O(N^{3/2}\log^4 N)=o(N^2)\). The positive remaining weighted count proves the theorem. \(\square\)

## 7. A finite Heath-Brown identity

Vaughan's decomposition is one way to choose short and long variables. A useful alternative, usually called Heath-Brown's identity, follows from the same convolution algebra. For an integer \(k\ge1\), \(z=x^{1/k}\), and \(n\le x\),

\[
\Lambda(n)=\sum_{j=1}^k(-1)^{j-1}\binom kj
\bigl(\mu_{\le z}^{*j}*\ell*\mathbf1^{*(j-1)}\bigr)(n).
\tag{7.1}
\]

The zeroth convolution power is \(\epsilon\). To prove the identity, set \(B=\epsilon-\mathbf1*\mu_{\le z}=\mathbf1*\mu_{>z}\), supported on integers strictly greater than \(z\). Its \(k\)-fold convolution vanishes on \(n\le z^k=x\). Expand
\(\epsilon-B^{*k}=\sum_{j=1}^k(-1)^{j-1}\binom kj\mathbf1^{*j}*\mu_{\le z}^{*j}\), convolve with \(\Lambda\), and use \(\Lambda*\mathbf1=\ell\). Since \(\Lambda*B^{*k}\) also vanishes on \(n\le x\), this gives (7.1). The identity itself is elementary; choosing its many variables for a particular application is a separate optimization.

## 8. Exercises

1. **Easy.** Verify Vaughan's identity by absolutely convergent Dirichlet series in \(\Re s>1\).
2. **Medium.** Prove \(\sum_{d\le D}|\sum_{m\le x/d}e(\alpha dm)|\ll(x/q+D+q)\log(2qx)\) under the rational-approximation hypothesis.
3. **Medium.** Establish the Möbius analogue (5.1), specifying the epsilon in the middle term and controlling the divisor-weighted Type I contribution.
4. **Hard.** Complete the exponential prime-sum estimate with the exponents \(1/2,4/5,1/2\) in (4.1), checking the support lengths after dyadic partition and the threshold choice.

## 9. Complete solutions

**1.** Put \(Z=\zeta(s)\), \(M=\sum_{n\le V}\mu(n)n^{-s}\), \(H=\sum_{n\le U}\Lambda(n)n^{-s}\), and \(A=-Z'/Z\). In \(\Re s>1\), the series of \(\ell\) is \(-Z'\), the series of \(\mu\) is \(1/Z\), and products are absolutely convergent convolutions. The series for the right side of (1.2) is
\(-MZ'-HMZ+(A-H)Z(1/Z-M)+H\). Since \(-Z'=AZ\), this equals
\(AMZ-HMZ+(A-H)(1-ZM)+H=A\). Uniqueness of coefficients of an absolutely convergent Dirichlet series proves the identity. Alternatively all cancellations take place in finite divisor sums, as in section 1.

**2.** Bound each geometric sum by \(\min(x/d,1/(2\|\alpha d\|))\). If \(q=1\) or \(q>x\), the harmonic bound \(x\sum_{d\le x}1/d\) suffices. For \(2\le q\le x\), split into blocks of \(h=\lfloor q/2\rfloor\). Their phases are \(1/(2q)\)-separated. The first block's closest distance is at least \(1/(2q)\); its whole contribution is \(O(q\log(2q))\). In the \(j\)-th following block the closest point contributes at most \(x/(jh)\), and all others have total \(O(q\log(2q))\). Sum the harmonic closest-point costs and the \(O(D/q+1)\) block costs. This is \(O((x/q+D+q)\log(2qx))\). The endpoint \(d>x\) contributes an empty inner sum.

**3.** Expand \(\mu=2\mu_{\le W}-\mu_{\le W}^{*2}*\mathbf1+\mu_{>W}*\mathbf1*\mu_{>W}\), using \(\mu*\mathbf1=\epsilon\), and take \(W=x^{2/5}\). The short part is \(O(W)\). The Type II factor \(\mu_{>W}*\mathbf1\) has square energy \(O(Y\log^3(2Y))\), while the other factor has square energy at most \(Y\). On each dyadic block their norm product is \(O(\sqrt x\log^{3/2}(2x))\). Equation (3.2) and the \(O(\log x)\) blocks give the three terms with power \(\log^3(2x)\). For Type I, the coefficient bound is \(d(d)\), not \(\log d\). The squared spacing sum on a block is \(O((D/q+1)((x/D)^2+qx/D))\); Cauchy–Schwarz gives (5.3). For \(q\le x^{1/5}\), that estimate and its initial-block refinement are bounded by \(x/\sqrt q\); for \(q\ge x^{4/5}\) they are bounded by \(\sqrt{xq}\). In the middle range use \(d(d)\ll_\eta d^\eta\), \(\eta\le\min(\varepsilon,1/10)\), and solution 2: \(x^\eta x/q\le x/\sqrt q\), and \(x^\eta(D_0+q)\le2x^{4/5+\varepsilon}\). These are precisely the three cases proved in section 5. The trivial bound handles \(q=1\) and \(q>x\). No epsilon-free assertion follows merely by setting \(\varepsilon=0\).

**4.** The first Type I sequence has support \(V\), norm bound 1 and logarithmic smooth factor; the second has support \(UV\) and coefficient bound \(\log(UV)\). Their combined size is \(O((x/q+UV+q)\log^2(2xUV))\). In a Type II block \(L<m\le2L\), the other support has length at most \(x/L\); the product of the two coefficient norms is \(O(\sqrt x\log(2x))\). Equation (3.2) therefore produces \(x/\sqrt q\), \(\sqrt{xL}\), \(x/\sqrt L\), and \(\sqrt{xq}\). Since \(U\le L<x/V\), the middle terms are at most \(x/\sqrt V\) and \(x/\sqrt U\). Sum the blocks, add the short \(O(U)\) contribution, and choose \(U=V=x^{2/5}\). The three parameter terms \(UV,x/\sqrt U,x/\sqrt V\) all become \(x^{4/5}\). If \(q\le x\), absorb \(x/q\) and \(q\) into the two square-root terms. If \(q>x\), the trivial \(O(x)\) bound suffices. The resulting power \(5/2\) of \(\log(2x)\) is smaller than the requested power 4, so (4.1) follows in its full stated range.

## 10. Proof scope and references

The convolution identities, both exponential Type I and Type II estimates, the prime-power bound, the stated Möbius analogue, and the classical sufficiently-large three-primes theorem are proved here. The three-primes argument imports the earlier proved Siegel–Walfisz theorem; it does not give a numerical exceptional range or a proof of the stronger every-odd-integer formulation. The elementary Chebyshev bound and divisor-square energy are the other named prerequisites.

- D. Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), AMS, 2019, author's preliminary version, Lemma 23.1, Theorems 23.5–23.6 and Theorem 23.8: the exact convolution normalization, phase spacing, bilinear bound, and the sharper logarithmic power \(5/2\).

Vaughan's identity packages Vinogradov's cancellation mechanism into four exact terms. In a character average, the same Type II coefficient structure feeds the maximal multiplicative bound proved in the preceding lesson.
