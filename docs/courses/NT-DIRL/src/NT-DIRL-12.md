# The large sieve inequality

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An exponential sum cannot have large values at too many well-separated points unless its coefficients have large total energy. The large sieve makes this assertion precise. Its arithmetic form converts omitted residue classes into a bound on the size of a set of integers. We prove both the elementary analytic estimate and the sharp estimate, then retain local spacings to obtain the exact uniform Brun–Titchmarsh bound. These analytic and arithmetic forms will also be useful for averages of character sums in the next lesson.

We use finite Fourier orthogonality from *Dirichlet characters*, the elementary prime-reciprocal estimate from *Dirichlet's theorem on primes in arithmetic progressions*, and elementary real and complex analysis. Put \(e(t)=\exp(2\pi i t)\) and \(\|t\|=\min_{k\in\mathbb Z}|t-k|\). Let \(M\in\mathbb Z\), \(N\ge1\) be an integer, and

\[
T(t)=\sum_{M<n\le M+N}a_n e(nt).
\tag{0.1}
\]

Points \(x_1,\ldots,x_R\) are \(\delta\)-spaced modulo 1 if \(\|x_r-x_s\|\ge\delta\) whenever \(r\ne s\). We always take \(0<\delta\le1\); the upper restriction also covers the otherwise vacuous one-point case.

## 1. Gallagher's estimate

**Lemma 1.1 (the midpoint Sobolev inequality).** If \(f\) is continuously differentiable on \(I=[x_0-\delta/2,x_0+\delta/2]\), then

\[
|f(x_0)|\le\frac1\delta\int_I|f(u)|\,du
+\frac12\int_I|f'(u)|\,du.
\tag{1.1}
\]

**Proof.** Write \(a=x_0-\delta/2\), \(b=x_0+\delta/2\). Integration by parts on the two halves gives

\[
\delta f(x_0)=\int_a^b f(u)\,du
+\int_a^{x_0}(u-a)f'(u)\,du
+\int_{x_0}^b(u-b)f'(u)\,du.
\]

Both coefficients of \(f'\) have absolute value at most \(\delta/2\). Take absolute values and divide by \(\delta\). The midpoint is essential: for an arbitrary point of \(I\), the same argument only gives coefficient 1 in front of the derivative integral. \(\square\)

Center pairwise disjoint arcs of length \(\delta\) at the \(x_r\) on the unit circle. For a differentiable function \(U\) with periodic \(|U|^2\), apply (1.1) to \(f=|U|^2\), whose derivative satisfies \(|f'|\le2|U||U'|\). Summing over the arcs and then using Cauchy–Schwarz gives Gallagher's estimate

\[
\sum_r|U(x_r)|^2
\le\delta^{-1}\int_0^1|U|^2
+\left(\int_0^1|U|^2\int_0^1|U'|^2\right)^{1/2}.
\tag{1.2}
\]

Take \(c=M+(N+1)/2\) and \(U(t)=e(-ct)T(t)\). Even if \(c\) is a half-integer, both squared moduli in (1.2) are periodic. Differences between its frequencies are integers, so direct integration gives

\[
\int_0^1|U|^2=\sum|a_n|^2,
\qquad
\int_0^1|U'|^2
=4\pi^2\sum(n-c)^2|a_n|^2
\le\pi^2(N-1)^2\sum|a_n|^2.
\]

Thus

\[
\boxed{\sum_r|T(x_r)|^2
\le\bigl(\pi(N-1)+\delta^{-1}\bigr)\sum|a_n|^2.}
\tag{1.3}
\]

In particular the usually stated \(\pi N+\delta^{-1}\) bound follows. Multiplying \(T\) by a phase has removed dependence on its starting frequency \(M\).

## 2. Duality

**Lemma 2.1.** For a finite complex matrix \(A=(A_{rn})\) and \(C\ge0\), the following three assertions are equivalent:

\[
\|Aa\|_2^2\le C\|a\|_2^2,
\qquad
\|A^*b\|_2^2\le C\|b\|_2^2,
\qquad
|\langle Aa,b\rangle|\le\sqrt C\|a\|_2\|b\|_2.
\tag{2.1}
\]

Each assertion is understood for all vectors of the indicated size.

**Proof.** The first gives the third by Cauchy–Schwarz. Conversely, take \(b=Aa\) in the third and cancel \(\|Aa\|_2\) when it is nonzero. Interchanging the two vectors in the identity \(\langle Aa,b\rangle=\langle a,A^*b\rangle\) proves equivalence with the second. Zero vectors require no division. \(\square\)

For \(A_{rn}=e(nx_r)\), the adjoint contains \(e(-nx_r)\). Since conjugating the arbitrary coefficients changes the sign in the absolute square, the dual large sieve has the equivalent form

\[
\sum_{M<n\le M+N}\left|\sum_r b_r e(nx_r)\right|^2
\le C\sum_r|b_r|^2.
\tag{2.2}
\]

Proving either version with the same \(C\) proves the other.

## 3. An interval majorant with compact Fourier support

The sharp constant requires a function that lies above the interval indicator while having no Fourier frequencies outside a prescribed short interval. We construct it and prove the support assertion, including the endpoints. For an integrable function \(F\), use

\[
\widehat F(\xi)=\int_{\mathbb R}F(x)e(-\xi x)\,dx.
\]

Define the entire functions

\[
K(z)=\left(\frac{\sin\pi z}{\pi z}\right)^2,
\qquad
H(z)=\left(\frac{\sin\pi z}{\pi}\right)^2
\left(\sum_{n\ne0}\frac{\operatorname{sgn}(n)}{(z-n)^2}+\frac2z\right),
\qquad B=H+K.
\tag{3.1}
\]

The sum converges locally uniformly away from the integers. The sine square cancels every apparent double pole; at zero, \(H(0)=0\). Therefore these definitions extend to entire functions. Also \(H\) is odd, \(K\) is even, \(H(n)=\operatorname{sgn}(n)\), and \(K(n)=0\) for nonzero integers.

First establish the partial-fraction identity

\[
\sum_{n\in\mathbb Z}\frac1{(z-n)^2}=\frac{\pi^2}{\sin^2\pi z}.
\tag{3.2}
\]

Integrate \(\pi\cot(\pi w)/(w-z)^2\) over squares with vertical sides at \(\pm(J+1/2)\) and horizontal sides at imaginary heights \(\pm(J+1/2)\). For large \(J\), \(\cot\pi w\) is bounded on the boundary, its length is \(O(J)\), and \(|w-z|\gg J\); hence the integral tends to zero. The residues at integers are \((n-z)^{-2}\), and the residue at \(z\) is \((\pi\cot\pi z)'=-\pi^2\csc^2\pi z\). The residue theorem gives (3.2).

For real \(x>0\), (3.2) yields

\[
1-H(x)=K(x)\left(1+2x^2\sum_{n\ge1}\frac1{(x+n)^2}-2x\right).
\tag{3.3}
\]

The decreasing-function integral test gives

\[
\frac1x-\frac1{x^2}\le\sum_{n\ge1}(x+n)^{-2}\le\frac1x.
\]

Thus the parenthesis in (3.3) lies between \(-1\) and 1. Oddness handles \(x<0\); the values at zero and the integers follow by continuity. We have proved

\[
|H(x)-\operatorname{sgn}(x)|\le K(x),
\qquad B(x)\ge\operatorname{sgn}(x).
\tag{3.4}
\]

Moreover \(\int_{\mathbb R}K=1\). Here is a direct normalization check. Integrating by parts,

\[
\int_{\mathbb R}K(x)\,dx
=\frac2\pi\int_0^\infty\frac{\sin(2\pi x)}x\,dx=1.
\]

To evaluate the last integral, first insert \(e^{-\eta x}\). Differentiation with respect to the frequency shows
\(\int_0^\infty e^{-\eta x}\sin(ax)\,dx/x=\arctan(a/\eta)\).
An integration-by-parts estimate for the sine tail, uniform in \(\eta\ge0\), allows \(\eta\downarrow0\), giving \(\pi/2\) for \(a>0\). By (3.4), \(H-\operatorname{sgn}\) is absolutely integrable and odd, so its integral is zero.

Let \(a\le b\) and define

\[
S(x)=\frac12 B(\delta(x-a))+\frac12 B(\delta(b-x)).
\tag{3.5}
\]

Inequality (3.4) proves \(S(x)\ge\mathbf1_{[a,b]}(x)\) at interior and exterior points. At either endpoint, \(B(0)=1\) and \(B(t)\ge1\) for \(t>0\), so the closed-interval indicator is also majorized. If \(a=b\), then \(S(x)=K(\delta(x-a))\). Furthermore,

\[
0\le S(x)-\mathbf1_{[a,b]}(x)
\le K(\delta(x-a))+K(\delta(b-x))
\quad\text{away from the endpoints},
\]

and hence \(S\in L^1(\mathbb R)\). The integral of the two sign functions gives the interval length; the two \(H-\operatorname{sgn}\) terms have zero integral. Therefore

\[
\widehat S(0)=b-a+\delta^{-1}.
\tag{3.6}
\]

We now prove

\[
\widehat S(\xi)=0\qquad(|\xi|\ge\delta).
\tag{3.7}
\]

For \(\operatorname{Re}z\ge0\), \(z\ne0\), (3.2) gives

\[
B(z)-1=2\left(\frac{\sin\pi z}{\pi}\right)^2
\left(\frac1z-\sum_{n\ge1}(z+n)^{-2}\right).
\tag{3.8}
\]

Replace \(1/z\) by \(\int_0^\infty(z+t)^{-2}dt\). Comparing each unit interval with its right endpoint bounds the absolute value of the parenthesis by

\[
2\int_0^\infty|z+t|^{-3}dt\le\frac2{|z|^2}.
\]

The inequality follows by direct integration: writing \(z=u+iv\), the integral is \(1/(|z|(|z|+u))\) when \(v\ne0\), with the continuous limiting value at positive real \(z\). Thus

\[
B(z)=1+O\left(\frac{e^{2\pi|\operatorname{Im}z|}}{|z|^2}\right)
\quad(\operatorname{Re}z\ge0).
\tag{3.9}
\]

Since \(B(-z)=-B(z)+2K(z)\), the analogous estimate with constant \(-1\) holds in the left half-plane. In (3.5) these two constants cancel outside the vertical strip between \(a\) and \(b\). Consequently, on horizontal lines of height \(-Y\), for \(Y\ge\delta^{-1}\),

\[
\int_{\mathbb R}|S(x-iY)|\,dx
\ll_{a,b,\delta}1+\frac{e^{2\pi\delta Y}}Y.
\tag{3.10}
\]

Indeed, in the fixed strip the two constant terms are bounded, and the error terms everywhere integrate to \(O(e^{2\pi\delta Y}/Y)\). For \(\xi>\delta\), shift the integral defining \(\widehat S(\xi)\) down to height \(-Y\). The vertical sides tend to zero as their real parts tend to infinity, by (3.9), first with \(Y\) fixed. The shifted integral has absolute value at most

\[
e^{-2\pi\xi Y}\int_{\mathbb R}|S(x-iY)|\,dx\longrightarrow0.
\]

Shift upward for \(\xi<-\delta\). This proves vanishing outside the support interval. Since \(S\in L^1\), its Fourier transform is continuous by dominated convergence; hence it also vanishes at \(\pm\delta\). This proves (3.7) without a Paley–Wiener theorem.

Finally, the same complex estimate and Cauchy's derivative formula give \(S^{(j)}(x)=O_{a,b,\delta,j}((1+|x|)^{-2})\) for \(j=0,1,2\). For real \(t\), periodize \(S(x)e(tx)\). Its translates and their first two derivatives converge uniformly. The resulting continuous periodic function has Fourier coefficients \(\widehat S(\ell-t)\). Only finitely many of these are nonzero by (3.7). Subtract that finite Fourier polynomial; the difference has every Fourier coefficient zero. Convolution with the Fejér kernels tends uniformly to a continuous periodic function and is zero here: positivity, integral 1, and the bound \(O(1/(J\sin^2\pi x))\) outside a fixed neighborhood of zero prove this convergence directly. Therefore the difference vanishes. Evaluating at zero proves the exact identity

\[
\sum_{n\in\mathbb Z}S(n)e(nt)
=\sum_{\ell\in\mathbb Z}\widehat S(\ell-t).
\tag{3.11}
\]

Both sides are legitimate: the first converges absolutely and the second is finite.

## 4. The sharp analytic large sieve

**Theorem 4.1 (Selberg's sharp form).** For \(\delta\)-spaced points modulo 1,

\[
\boxed{\sum_r|T(x_r)|^2
\le\bigl(N-1+\delta^{-1}\bigr)\sum_{M<n\le M+N}|a_n|^2.}
\tag{4.1}
\]

**Proof.** By duality it is enough to prove (2.2). In Section 3 take \(a=M+1\), \(b=M+N\). Since \(S\ge0\) everywhere and \(S(n)\ge1\) on these \(N\) integers,

\[
\sum_{M<n\le M+N}\left|\sum_r b_r e(nx_r)\right|^2
\le\sum_{n\in\mathbb Z}S(n)\left|\sum_r b_r e(nx_r)\right|^2.
\]

Expand the square. For \(r\ne s\), the corresponding inner sum is, by (3.11),
\(\sum_\ell\widehat S(\ell-x_r+x_s)=0\), because every argument has absolute value at least \(\delta\). Vanishing at the boundary in (3.7) is needed if two points are exactly \(\delta\) apart. On the diagonal, \(0<\delta\le1\) eliminates all nonzero integers, leaving \(\widehat S(0)=N-1+\delta^{-1}\). Thus the whole right side equals this constant times \(\sum|b_r|^2\). \(\square\)

The case \(N=1\) says \(R\le\delta^{-1}\), as it should. For equally spaced points with \(\delta=1/R\), Parseval shows that the \(\delta^{-1}\) term cannot be discarded. The \(N\) term is already necessary at a single sampling point, by Cauchy–Schwarz with equal-phase coefficients.

## 5. Farey fractions

Use one representative of each reduced fraction \(b/q\) modulo 1, with \(q\le Q\); the denominator-one fraction is 0. If two such fractions are distinct, then

\[
\left\|\frac bq-\frac{b'}{q'}\right\|
=\min_{k\in\mathbb Z}\frac{|bq'-b'q-kqq'|}{qq'}
\ge\frac1{qq'}\ge Q^{-2}.
\tag{5.1}
\]

The numerator cannot be zero because distinct reduced fractions modulo 1 represent distinct circle points. For real \(Q\ge1\), Theorems 1.3 and 4.1 therefore give respectively

\[
\sum_{q\le Q}\sum_{b\bmod q}^{*}|T(b/q)|^2
\le\bigl(\pi(N-1)+Q^2\bigr)\sum|a_n|^2
\tag{5.2}
\]

and

\[
\boxed{\sum_{q\le Q}\sum_{b\bmod q}^{*}|T(b/q)|^2
\le\bigl(N-1+Q^2\bigr)\sum|a_n|^2.}
\tag{5.3}
\]

The stars mean \((b,q)=1\); modulo 1 this convention includes its unique residue class. One may replace \(N-1\) by \(N\) in applications.

## 6. The arithmetic large sieve

Let \(\mathcal A\subset\{M+1,\ldots,M+N\}\), and write \(Z=|\mathcal A|\). For each prime \(p\le Q\), suppose that all members of \(\mathcal A\) avoid a specified set \(\Omega_p\) of \(\omega(p)\) residue classes. If \(\omega(p)=p\), then \(Z=0\); hence assume \(0\le\omega(p)<p\). Put

\[
g(p)=\frac{\omega(p)}{p-\omega(p)},\qquad
g(q)=\prod_{p\mid q}g(p)\quad(q\text{ squarefree}),
\qquad
L(Q)=\sum_{q\le Q}\mu^2(q)g(q),
\tag{6.1}
\]

with \(g(1)=1\).

**Lemma 6.1.** For \(T(t)=\sum_{n\in\mathcal A}e(nt)\) and squarefree \(q\) built from primes at most \(Q\),

\[
\sum_{b\bmod q}^{*}|T(b/q)|^2\ge Z^2g(q).
\tag{6.2}
\]

**Proof.** For \(p\), define a function on \(\mathbb Z/p\mathbb Z\) by

\[
w_p(h)=
\begin{cases}
-1,&h\in\Omega_p,\\
g(p),&h\notin\Omega_p.
\end{cases}
\]

Its mean is zero, and its mean square is

\[
\frac1p\sum_h|w_p(h)|^2
=\frac{\omega(p)+(p-\omega(p))g(p)^2}{p}=g(p).
\]

Write its finite Fourier expansion as \(w_p(h)=\sum_{b=1}^{p-1}c_p(b)e(bh/p)\). Finite orthogonality gives \(\sum_b|c_p(b)|^2=g(p)\). For squarefree \(q\), multiply these expansions. By the Chinese remainder theorem, sums of the nonzero local frequencies correspond bijectively to the unit frequencies modulo \(q\). Thus

\[
W_q(h):=\prod_{p\mid q}w_p(h)
=\sum_{b\bmod q}^{*}c_q(b)e(bh/q),
\qquad
\sum_b^{*}|c_q(b)|^2=g(q).
\]

For \(n\in\mathcal A\), \(W_q(n)=g(q)\). Summing and applying Cauchy–Schwarz gives

\[
Z^2g(q)^2
=\left|\sum_b^{*}c_q(b)T(b/q)\right|^2
\le g(q)\sum_b^{*}|T(b/q)|^2.
\]

If \(g(q)>0\), divide by it; otherwise (6.2) is trivial. For \(q=1\), it is the identity \(|T(0)|^2=Z^2\). \(\square\)

Sum (6.2) over squarefree \(q\le Q\), enlarge to all denominators, and apply (5.3) with coefficients \(\mathbf1_{\mathcal A}\), whose square norm is \(Z\). If \(Z>0\), cancellation yields Montgomery's arithmetic large sieve:

\[
\boxed{Z\le\frac{N-1+Q^2}{L(Q)}.}
\tag{6.3}
\]

This also holds for \(Z=0\). Using (5.2) instead gives numerator \(\pi(N-1)+Q^2\).

A simpler prime-only version is useful. Put \(Z(p,h)=|\{n\in\mathcal A:n\equiv h\pmod p\}|\). Orthogonality gives the exact variance identity

\[
p\sum_{h\bmod p}\left|Z(p,h)-\frac Zp\right|^2
=\sum_{b=1}^{p-1}|T(b/p)|^2.
\tag{6.4}
\]

If \(\mathcal P\) consists of \(P\) primes at most \(Q\), and at least \(\tau p\) classes are empty for each \(p\in\mathcal P\), their contribution to the left side is at least \(\tau Z^2\). Summing and applying (5.3) proves

\[
Z\le\frac{N-1+Q^2}{\tau P}
\quad(P>0).
\tag{6.5}
\]

## 7. Primes in a short interval

For primes exceeding \(Q\), sieve out just 0 modulo each prime at most \(Q\). Then \(g(p)=1/(p-1)\), and

\[
L(Q)=\sum_{q\le Q}\frac{\mu^2(q)}{\varphi(q)}
=\log Q+O(1).
\tag{7.1}
\]

We prove the asymptotic and keep an explicit, deliberately coarse bound for its error. Define a multiplicative function \(h\) by

\[
h(p)=\frac1{p(p-1)},\qquad
h(p^2)=-\frac1{p(p-1)},\qquad h(p^j)=0\ (j\ge3).
\]

Checking the local coefficients gives \(\mu^2(n)/\varphi(n)=\sum_{d\mid n}h(d)/(n/d)\). The absolutely convergent Euler products show

\[
\sum_d h(d)=1,\qquad
A_0:=\sum_d|h(d)|\le e^2,
\qquad
A_1:=\sum_d|h(d)|\log d\le12e^2.
\tag{7.2}
\]

For the last bound, differentiating the product for the absolute sum, or expanding its local logarithmic contributions, gives
\(A_1\le3A_0\sum_p\log p/[p(p-1)]\).
To bound this last sum by 4, enlarge to all integers and use
\(1/[n(n-1)]\le2/n^2\); the positive function \(\log t/t^2\) is decreasing for \(t\ge2\), so its sum is at most its value at 2 plus \(\int_2^\infty\log t/t^2\,dt<2\). For \(A_0\), use \(\sum_{n\ge2}1/[n(n-1)]=1\).

Writing \(H_k=\sum_{m\le k}1/m\), finite rearrangement gives

\[
L(Q)=\sum_{d\le Q}h(d)H_{\lfloor Q/d\rfloor}.
\]

For \(t\ge1\), integral comparison bounds \(|H_{\lfloor t\rfloor}-\log t|\le2\). Hence

\[
|L(Q)-\log Q|
\le\sum_{d\le Q}|h(d)|\log d
+\log Q\sum_{d>Q}|h(d)|+2A_0
\le A_1+2A_0<200.
\tag{7.3}
\]

In particular all constants in (7.1) are effective.

For a simple bound valid even at small \(Q\), there is a better lower estimate:

\[
L(Q)\ge\sum_{m\le Q}\frac1m\ge\log Q.
\tag{7.7}
\]

Indeed, for squarefree \(q\), multiplying geometric series over its prime divisors gives
\(1/\varphi(q)=\sum_{\operatorname{rad}(m)=q}1/m\), where \(\operatorname{rad}(m)\) is the product of its distinct prime divisors. Consequently \(L(Q)=\sum_{\operatorname{rad}(m)\le Q}1/m\), an absolutely convergent sum: only the finitely many primes at most \(Q\) can occur. This includes all \(m\le Q\). Finally \(H_{\lfloor Q\rfloor}\ge\int_1^{\lfloor Q\rfloor+1}dt/t\ge\log Q\).

**Theorem 7.1 (Brun–Titchmarsh with asymptotic constant 2).** For every \(\varepsilon>0\), there is an effective \(y_0(\varepsilon)\) such that, uniformly for real \(x\ge0\) and \(y\ge y_0(\varepsilon)\),

\[
\pi(x+y)-\pi(x)\le(2+\varepsilon)\frac y{\log y}.
\tag{7.4}
\]

For all \(x\ge0\), \(y\ge2\), the explicit estimate

\[
\pi(x+y)-\pi(x)\le5\frac y{\log y}
\tag{7.5}
\]

holds.

**Proof.** The integers of \((x,x+y]\) lie in an integer block with \(N\le y+1\). The primes in this block exceeding \(Q\) avoid 0 modulo every prime at most \(Q\). Therefore

\[
\pi(x+y)-\pi(x)
\le Q+\frac{y+Q^2}{L(Q)}.
\tag{7.6}
\]

For large \(y\), choose \(Q=\sqrt y/(\log y)^2\). Then \(Q=o(y/\log y)\), \(Q^2=o(y)\), and \(\log Q=\tfrac12\log y-2\log\log y\). Equations (7.3) and (7.6) give

\[
\pi(x+y)-\pi(x)\le(2+o(1))y/\log y
\]

with a uniform effective \(o(1)\). This proves (7.4). For the explicit all-\(y\) constant, take \(Q=\sqrt y\) in (7.6), and use (7.7). The fraction is at most \(4y/\log y\). Also \(\sqrt y\le y/\log y\), since \(\log y\le\sqrt y\) for \(y\ge2\). One can check the latter inequality by maximizing \((\log y)/\sqrt y\): its maximum on \((1,\infty)\) is \(2/e<1\). This proves the constant 5. \(\square\)

If we used only Gallagher's bound, the same asymptotic argument would give \(2\pi+\varepsilon\) instead of \(2+\varepsilon\); the choice \(Q=\sqrt y\) and (7.7) would give the explicit all-\(y\) constant \(2\pi+3\). The interval length \(N-1\), the small extra term \(Q^2\), and the factor \(\tfrac12\log y\) in the denominator explain the sharp asymptotic constant 2.

## 8. Squares and the benefit of composite moduli

For squares, the forbidden classes at an odd prime are the \((p-1)/2\) quadratic nonresidues. At 2, there are no forbidden classes: both 0 and 1 occur as squares. Thus

\[
g(2)=0,\qquad g(p)=\frac{p-1}{p+1}\quad(p>2).
\tag{8.1}
\]

We show that the denominator in (6.3) satisfies \(L(Q)\sim cQ\), with \(c>0\). Let \(f(n)=\mu^2(n)g(n)\) and write \(f=\mathbf1*h\), where the star is Dirichlet convolution and \(\mathbf1(n)=1\). The local values are

\[
h(p)=g(p)-1,\qquad h(p^2)=-g(p),\qquad h(p^j)=0\ (j\ge3).
\]

Here \(g(2)=0\), so \(h(2)=-1\), \(h(4)=0\). For odd primes,
\(|h(p)|=2/(p+1)\), \(|h(p^2)|\le1\). Hence \(\sum_d|h(d)|/d<\infty\), by the Euler product and convergence of \(\sum_p p^{-2}\). Now

\[
\frac{L(Q)}Q=\sum_{d\le Q}h(d)\frac{\lfloor Q/d\rfloor}Q
\longrightarrow\sum_{d\ge1}\frac{h(d)}d
=\prod_p\left(1-\frac1p\right)\left(1+\frac{g(p)}p\right)=:c.
\tag{8.2}
\]

Dominated convergence applies because \(\lfloor Q/d\rfloor/Q\le1/d\). The factor at 2 is \(1/2\); at odd primes each factor is positive and is \(1+O(p^{-2})\). Their product therefore converges to a positive number. This proves the claim.

For a set of square integers in any block of \(N\) consecutive integers, take \(Q=\sqrt N\) in (6.3). By (8.2), adjusting the constant for bounded \(N\),

\[
Z\ll\sqrt N.
\tag{8.3}
\]

The elementary truth is at least as sharp in order: a block containing \(k\) distinct nonnegative squares has distance between its extreme squares at least \((k-1)^2\), so \(k\le1+\sqrt{N-1}\). The significance of (8.3) is that it uses only the local restrictions, without recognizing the actual integers as squares. The prime-only denominator would give a weaker \(\sqrt N\log N\) estimate; retaining squarefree composite moduli removes that logarithm.

## 9. A positive density of smooth integers

For Linnik's application we need many integers whose prime factors are small. Define \(\Psi(X,Y)\) to be the number of positive integers at most \(X\) with every prime factor at most \(Y\), including 1. For each fixed \(\alpha>0\),

\[
\Psi(X,X^\alpha)\ge c_\alpha X
\quad\text{for sufficiently large }X,
\tag{9.1}
\]

where \(c_\alpha>0\). We prove this rather than assume a smooth-number theorem.

Let \(\rho(u)=1\) for \(0\le u\le1\). On successive intervals of length 1 define it by the delay equation

\[
\rho(u)=1-\int_1^u\frac{\rho(v-1)}v\,dv
\quad(u\ge1).
\tag{9.2}
\]

On each new interval the integrand has already been defined. Thus this gives a unique continuous function, differentiable for \(u>1\), with \(u\rho'(u)=-\rho(u-1)\).

We prove by induction on integer \(U\ge1\) that

\[
\frac{\Psi(X,X^{1/u})}X\longrightarrow\rho(u)
\quad(1\le u\le U),
\tag{9.3}
\]

uniformly on that interval. For \(0<u\le1\), all integers at most \(X\) are counted, so the base case is immediate. The exact largest-prime-factor decomposition is

\[
\Psi(X,Y)=\lfloor X\rfloor-
\sum_{Y<p\le X}\Psi(X/p,p).
\tag{9.4}
\]

Every nonsmooth integer is counted once, at its largest prime factor \(p\); repeated copies of that prime are allowed in the remaining factor.

Suppose (9.3) is known uniformly up to \(U-1\), and fix \(1<u\le U\). In the summand of (9.4), put \(v=\log X/\log p\). Then \(1\le v<u\) and

\[
\frac{\log(X/p)}{\log p}=v-1\le U-1.
\]

If \(p\le X^{1-\eta}\), the argument \(X/p\) tends to infinity uniformly, and the inductive hypothesis gives
\(\Psi(X/p,p)/(X/p)=\rho(v-1)+o(1)\), uniformly. When \(v-1\le1\) this assertion is just the base case. The omitted upper range \(p>X^{1-\eta}\) contributes at most

\[
X\sum_{X^{1-\eta}<p\le X}\frac1p
=X\bigl(-\log(1-\eta)+o(1)\bigr).
\tag{9.5}
\]

Here and below we use the elementary estimate already proved earlier in the course,
\(\sum_{p\le t}1/p=\log\log t+B+O(1/\log t)\).
In particular, for fixed \(0<a<b\le1\),

\[
\sum_{X^a<p\le X^b}\frac1p\longrightarrow\log(b/a).
\]

Approximate a continuous function on a fixed closed subinterval of \((0,1]\) by step functions; the last identity then shows that these reciprocal-prime sums converge to integration against \(dw/w\), where \(w=\log p/\log X\). Using (9.4), first let \(X\to\infty\) with \(\eta\) fixed, then let \(\eta\downarrow0\). The bound (9.5), and boundedness of the continuous \(\rho\) on \([0,U-1]\), justify the second limit. The result is

\[
\lim_{X\to\infty}\frac{\Psi(X,X^{1/u})}X
=1-\int_{1/u}^1\rho\left(\frac{1-w}w\right)\frac{dw}w
=1-\int_1^u\frac{\rho(v-1)}v\,dv=\rho(u).
\]

This proves pointwise convergence on \([1,U]\). It is uniform there: each function on the left is nonincreasing in \(u\), and the limit is continuous. Given an error tolerance, choose a finite grid on which the limit varies by at most that tolerance; monotonicity traps the values between those at successive grid points, where pointwise convergence holds. This completes the induction.

Finally, \(\rho(u)>0\) for every finite \(u\). Differentiating shows that

\[
u\rho(u)=\int_{u-1}^u\rho(t)\,dt\qquad(u\ge1):
\tag{9.6}
\]

both sides have derivative \(\rho(u)-\rho(u-1)\) and agree at 1. If there were a first zero after 1, the right side at that zero would be positive, a contradiction. Before any such zero the derivative in (9.2) is negative, so no change of sign without a first zero is possible. Equation (9.3), with \(u=1/\alpha\) when \(\alpha<1\), gives (9.1) with \(c_\alpha=\rho(1/\alpha)/2\). For \(\alpha\ge1\), all integers are smooth and the assertion is immediate.

## 10. Linnik's sparsity theorem for quadratic nonresidues

For an odd prime \(p\), write \(n_2(p)\) for the least positive quadratic nonresidue modulo \(p\). Such a number exists because exactly \((p-1)/2\) nonzero classes are nonresidues.

**Theorem 10.1 (Linnik).** For every fixed \(\delta>0\),

\[
\#\{p\le x:p\text{ odd prime},\ n_2(p)>p^\delta\}
\ll_\delta\log\log x
\qquad(x\ge e^e).
\tag{10.1}
\]

**Proof.** It suffices to consider \(0<\delta<1\). For \(\delta\ge1\), \(n_2(p)\le p-1<p^\delta\), so the set is empty. Fix a large \(Q\) and consider exceptional primes \(\sqrt Q<p\le Q\). Put \(N=\lfloor Q^2\rfloor\) and

\[
Y=Q^{\delta/2},\qquad
\mathcal A=\{1\le n\le N:n\text{ is }Y\text{-smooth}\}.
\]

For every exceptional \(p\) in this block, each prime factor \(\ell\le Y\) satisfies \(\ell<p^\delta<n_2(p)\), and \(\ell<p\). Thus \(\ell\) is a nonzero quadratic residue modulo \(p\). Multiplicativity makes every \(n\in\mathcal A\) a nonzero quadratic residue modulo \(p\). In particular, at least \((p-1)/2\ge p/3\) classes are missed. All these sieving primes are at most \(Q\).

Since \(Y\ge N^{\delta/4}\), the smooth-number lemma gives \(Z=|\mathcal A|\gg_\delta N\). If the block contains \(P\) exceptional primes, (6.5) with \(\tau=1/3\) yields

\[
Z\le3(N-1+Q^2)/P,
\qquad P\ll_\delta1.
\tag{10.2}
\]

Every sufficiently large block \((\sqrt Q,Q]\) therefore contains only a bounded number, depending on \(\delta\). Apply this successively with \(Q=x,x^{1/2},x^{1/4},\ldots\), stopping when \(Q\) falls below a fixed sufficiently large threshold. There are \(O(\log\log x)\) blocks; the remaining finite primes are absorbed in the constant. This proves (10.1). \(\square\)

This is a statement about how rare primes with unusually large least nonresidues are. It does not bound the least nonresidue for every individual prime; the character-sum methods from *Character sums: the Pólya–Vinogradov inequality* address that different question.

## 11. The exact uniform Brun–Titchmarsh refinement

Keeping only the smallest Farey spacing loses useful information: a fraction with a small denominator is farther from its neighbours. We now retain each point's own spacing. This will remove the logarithmic loss in Section 7 and prove the exact uniform inequality.

### 11.1. A weighted Hilbert inequality

For distinct real numbers \(\lambda_r\), let
\(\delta_r=\min_{s\ne r}|\lambda_r-\lambda_s|\).
We first prove
\[
\left|\sum_{r\ne s}\frac{u_r\overline{u_s}}{\lambda_r-\lambda_s}\right|
\le\frac{3\pi}{2}\sum_r\frac{|u_r|^2}{\delta_r}.
\tag{11.1}
\]
The corresponding bilinear bound follows from the norm of the same skew-Hermitian matrix. A family consisting of one point has zero left side and can be omitted.

Here are the spacing estimates needed for the proof:
\[
\sum_{m\ne r}\frac{\delta_m}{(\lambda_m-\lambda_r)^2}
\le\frac4{\delta_r},
\qquad
\sum_{m\ne r}\frac{\delta_m}{(\lambda_m-\lambda_r)^4}
\le\frac8{3\delta_r^3},
\tag{11.2}
\]
and, for \(r\ne s\),
\[
\sum_{m\ne r,s}
\frac{\delta_m}{(\lambda_m-\lambda_r)^2(\lambda_m-\lambda_s)^2}
\le\frac4{(\lambda_r-\lambda_s)^2}
\left(\frac1{\delta_r}+\frac1{\delta_s}\right).
\tag{11.3}
\]

**Proof of the spacing estimates.** Order the \(\lambda_r\). The centred intervals
\(J_r=[\lambda_r-\delta_r/2,\lambda_r+\delta_r/2]\)
have disjoint interiors. For a positive convex function \(f\),
\(\delta_m f(\lambda_m)\le\int_{J_m}f(t)\,dt\).
On one side of \(\lambda_r\), separate its nearest neighbour at distance \(d\). Its contribution to the second-power sum is at most \(1/d\); all later centred intervals lie beyond that neighbour, so their total is at most
\(\int_d^\infty t^{-2}\,dt=1/d\).
The fourth-power calculation gives \(d^{-3}+\int_d^\infty t^{-4}\,dt=4/(3d^3)\). Sum both sides and use \(d\ge\delta_r\), obtaining (11.2).

For (11.3), the function
\(f(t)=(t-\lambda_r)^{-2}(t-\lambda_s)^{-2}\)
is positive and convex on every component away from its poles: indeed
\[
\frac{f''}{f}
=\left(\frac{-2}{t-\lambda_r}+\frac{-2}{t-\lambda_s}\right)^2
+\frac2{(t-\lambda_r)^2}+\frac2{(t-\lambda_s)^2}>0.
\]
Its centred integrals are bounded by its integral on
\(\mathbb R\setminus(J_r\cup J_s)\).
With \(d=\lambda_s-\lambda_r>0\),
\[
f(t)=d^{-2}\left((t-\lambda_r)^{-2}+(t-\lambda_s)^{-2}
-\frac2{(t-\lambda_r)(t-\lambda_s)}\right).
\]
The first two integrals are at most \(4/(d^2\delta_r)\) and \(4/(d^2\delta_s)\). The remaining integral has a nonpositive contribution. To check its sign exactly, the symmetric principal-value integral of
\(g(t)=1/((t-\lambda_r)(t-\lambda_s))\)
over the whole line is zero, by partial fractions. Its principal-value integral over \(J_r\) is
\[
\frac1d\log\frac{d-\delta_r/2}{d+\delta_r/2}<0,
\]
and the analogous integral over \(J_s\) is negative as well. Thus the integral of \(g\) on the complement is positive. Multiplication by \(-2/d^2\) proves the required sign, and hence (11.3). \(\square\)

**Proof of (11.1).** Put
\[
A_{rs}=\frac{\sqrt{\delta_r\delta_s}}{\lambda_r-\lambda_s}\quad(r\ne s),
\qquad A_{rr}=0.
\]
The matrix satisfies \(A^*=-A\); its norm is the largest absolute value of its eigenvalues. Choose a unit eigenvector \(v\) with \(Av=itv\), \(t\in\mathbb R\). Expanding \(\|Av\|^2\), the diagonal contribution is at most 4 by (11.2). For the off-diagonal part use
\[
\frac{\delta_m}{(\lambda_m-\lambda_r)(\lambda_m-\lambda_s)}
=\frac1{\lambda_r-\lambda_s}
\left(\frac{\delta_m}{\lambda_m-\lambda_r}
-\frac{\delta_m}{\lambda_m-\lambda_s}\right).
\]
Inserting the omitted terms \(m=s\) and \(m=r\) gives a contribution
\[
\sum_{r\ne s}
\frac{\sqrt{\delta_r\delta_s}(\delta_r+\delta_s)}
{(\lambda_r-\lambda_s)^2}v_r\overline{v_s},
\]
plus a difference of two separable sums. The latter cancel. More explicitly, write
\(B_r=\sum_{m\ne r}\delta_m/(\lambda_m-\lambda_r)\).
The difference is
\(\sum_{r\ne s}A_{rs}v_r\overline{v_s}(B_r-B_s)\);
the eigenvector equation and its conjugate make its two parts both
\(-it\sum_r|v_r|^2B_r\).

Consequently the off-diagonal contribution is bounded in absolute value by
\[
U=\sum_{r\ne s}
\frac{\sqrt{\delta_r\delta_s}(\delta_r+\delta_s)}
{(\lambda_r-\lambda_s)^2}|v_rv_s|.
\]
By symmetry, this is twice
\(\sum_r |v_r|\sqrt{\delta_r}
\sum_{s\ne r}\delta_s^{3/2}|v_s|/(\lambda_r-\lambda_s)^2\).
Cauchy–Schwarz, followed by expansion of the square and (11.2)–(11.3), gives
\[
(U/2)^2
\le\sum_{s,t}\delta_s^{3/2}\delta_t^{3/2}|v_sv_t|
\sum_{r\ne s,t}
\frac{\delta_r}{(\lambda_r-\lambda_s)^2(\lambda_r-\lambda_t)^2}
\le\frac83+4U.
\]
In the first sum the notation excludes \(r=s\) and \(r=t\); when \(s=t\), use the fourth-power estimate. The terms with \(s\ne t\) are exactly bounded by \(4U\).
Solving the quadratic yields
\(U\le8+4\sqrt{14/3}<17\).
Thus \(t^2\le4+U<21<(3\pi/2)^2\).
The last numerical comparison follows already from \(\pi>3.1\), for example from the perimeter of the inscribed regular twelve-sided polygon. This proves the matrix norm bound and (11.1) after setting \(v_r=u_r/\sqrt{\delta_r}\). \(\square\)

For circle points \(\alpha_r\), put
\(\delta_r=\min_{s\ne r}\|\alpha_r-\alpha_s\|\).
The line inequality implies
\[
\left|\sum_{r\ne s}u_r\overline{u_s}\csc\pi(\alpha_r-\alpha_s)\right|
\le\frac32\sum_r\frac{|u_r|^2}{\delta_r}.
\tag{11.4}
\]
To prove this implication, apply (11.1) to
\(\lambda_{nr}=n+\alpha_r\), \(1\le n\le K\), with coefficients
\((-1)^nu_r/\sqrt K\).
Their line spacings are at least \(\delta_r\), and the terms with the same \(r\) cancel in pairs. For \(r\ne s\) the resulting kernel is
\[
\sum_{|j|<K}\frac{(1-|j|/K)(-1)^j}{j+\alpha_r-\alpha_s}
\longrightarrow\pi\csc\pi(\alpha_r-\alpha_s).
\]
This is the partial-fraction identity for the cosecant. It follows by residues, just as the cotangent identity in Section 3; pairing \(j\) and \(-j\) gives absolutely convergent terms of size \(O(j^{-2})\), which also justifies the displayed limit. Divide the line bound by \(\pi\), obtaining (11.4).

### 11.2. The local-spacing sieve

For \(N\) consecutive integer frequencies, (11.4) gives
\[
\sum_r\frac{|T(\alpha_r)|^2}{N+\tfrac32\delta_r^{-1}}
\le\sum_{M<n\le M+N}|a_n|^2.
\tag{11.5}
\]
Indeed the dual Gram matrix has diagonal \(N\). Its off-diagonal kernel is
\[
\sum_{M<n\le M+N}e(nh)
=\frac{e((M+N+\tfrac12)h)-e((M+\tfrac12)h)}
{2i\sin\pi h}.
\]
Apply (11.4) separately to the two phase-modified coefficient vectors. Their norms and spacings agree, so the off-diagonal quadratic form is bounded by
\(\tfrac32\sum|u_r|^2/\delta_r\).
This proves the dual estimate with diagonal weights \(N+\tfrac32\delta_r^{-1}\); the duality argument of Section 2, after dividing each row by its square-root weight, gives (11.5).

For Farey fractions with denominators \(q\le z\), each local spacing is at least \(1/(qz)\). Combining (11.5) with the local Fourier selector calculation of Section 6 therefore gives
\[
Z\le\left(
\sum_{q\le z}\frac{\mu^2(q)g(q)}{N+\tfrac32qz}
\right)^{-1}.
\tag{11.6}
\]
If \(Z=0\) there is nothing to show; otherwise cancel one \(Z\) after applying the selector lower bound \(Z^2\mu^2(q)g(q)\). A single Farey point causes no difficulty: its estimate is immediate. For primes greater than \(z\), \(g(q)=1/\varphi(q)\).

### 11.3. An explicit denominator estimate

Write
\[
D(t)=\sum_{n\le t}\frac{\mu^2(n)}{\varphi(n)},
\qquad
S(z)=\sum_{n\le z}\frac{\mu^2(n)}{\varphi(n)(1+n/z)}.
\]
We shall prove the two bounds
\[
D(t)\ge\log t+1.07\quad(t\ge6),
\qquad
S(z)>\log z+0.36\quad(z\ge100).
\tag{11.7}
\]
The decimals here are exact rational constants.

First we need a uniformly explicit harmonic estimate. Put
\(B_2(u)=u^2-u+1/6\), and let \(\{v\}\) denote fractional part. Integration by parts on consecutive unit intervals gives, for \(v>0\),
\[
H_{\lfloor v\rfloor}
=\log v+\gamma+\frac{1/2-\{v\}}v
-\frac{B_2(\{v\})}{2v^2}
+\int_v^\infty\frac{B_2(\{u\})}{u^3}\,du.
\tag{11.8}
\]
For completeness, start with \(H_{\lfloor v\rfloor}-\log v\) and its limit \(\gamma\). On each open unit interval its derivative is \(-1/v\); its jump at an integer \(n\) is \(1/n\). Subtracting \((1/2-\{v\})/v\) cancels those jumps and leaves derivative \((1/2-\{v\})/v^2\). Integrate this derivative from \(v\) to infinity, then use \(B_2'(\{v\})=2(\{v\}-1/2)\). This proves (11.8), including integer endpoints and \(0<v<1\).
Since \(|B_2|\le1/6\), the last two terms together have absolute value at most \(1/(6v^2)\).

Let \(H_6(t)=\sum_{r\le t,(r,6)=1}1/r\).
Inclusion–exclusion applied to (11.8) gives
\[
H_6(t)=\frac13\log t+\frac{\gamma}{3}
+\frac{\log2}{3}+\frac{\log3}{6}
-\frac1t\sum_{d\mid6}\mu(d)\{t/d\}+E(t),
\qquad |E(t)|\le\frac2{t^2}.
\tag{11.9}
\]
Here \(\sum_{d\mid6}d=12\) bounds the error, and
\(\sum_{d\mid6}\mu(d)=0\) removes the half terms.

The radical decomposition of an integer proves
\[
\sum_{\substack{r\le t\\(r,6)=1}}\frac{\mu^2(r)}{\varphi(r)}
\ge H_6(t).
\]
Indeed \(1/\varphi(r)=r^{-1}\prod_{p\mid r}(1-p^{-1})^{-1}\) for squarefree \(r\); expanding the geometric factors assigns every positive integer its reciprocal, grouped by its radical. Restricting radicals to \(r\le t\) includes all the terms from integers at most \(t\).
Separating the part of a squarefree \(n\) that divides 6 now yields
\[
D(z)\ge\sum_{m\mid6}\frac{H_6(z/m)}{\varphi(m)}
\ge\log z+c-\frac{A(z,6)}z-\frac{55}{z^2},
\tag{11.10}
\]
where
\[
c=\gamma+\tfrac12\log2+\tfrac16\log3,
\quad
A(z,k)=\sum_{m\mid k}\frac m{\varphi(m)}
\sum_{d\mid k}\mu(d)\{z/(md)\}.
\]
The error coefficient is \(2\sum_{m\mid6}m^2/\varphi(m)=55\).
For \(p\nmid k\), expanding the divisors gives
\[
A(z,pk)=A(z,k)+\frac{A(z/p,k)}{p-1}
-\frac{pA(z/p^2,k)}{p-1}.
\]
The function \(A(z,2)=\{z\}+\{z/2\}-2\{z/4\}\) has absolute value at most 1, by examining the four unit intervals of its period 4. Thus \(|A(z,6)|\le3\).
Use \(\gamma>0.577\), \(\log2>0.693\), and \(\log3>1.098\).
At \(z\ge100\), (11.10) is greater than \(\log z+1.071\), proving the first part of (11.7) in that range.

Here is an explicit finite certificate for \(6\le z<100\). It suffices to check
\(D(Q)-\log(Q+1)>1.07\), \(6\le Q\le99\), because \(D\) is constant between its integer jumps. The following lower bounds are rounded down:

| Integers \(Q\) | Lower bound for \(D(Q)-\log(Q+1)\) |
|---|---:|
| 6–9 | 1.1140 |
| 10–19 | 1.2017 |
| 20–29 | 1.2045 |
| 30–39 | 1.2693 |
| 40–49 | 1.3314 |
| 50–59 | 1.2768 |
| 60–69 | 1.2762 |
| 70–79 | 1.3131 |
| 80–89 | 1.3213 |
| 90–99 | 1.3053 |

These are rational comparisons, and can be reproduced without numerical logarithms as follows. Factor each \(n\le99\) to compute \(\mu^2(n)/\varphi(n)\) exactly. Write \(Q+1=2^jt\), \(1\le t\le2\), and put \(w=(t-1)/(t+1)\). Use
\[
L_{150}(t)=2\sum_{h=0}^{149}\frac{w^{2h+1}}{2h+1},
\qquad
0\le\log t-L_{150}(t)
\le\frac{2w^{301}}{301(1-w^2)}.
\tag{11.11}
\]
Apply the same bound to \(\log2\), and subtract the resulting rational upper bound for \(j\log2+\log t\) from \(D(Q)\). Taking the minimum in each displayed group gives the table. The bounds on \(\log2,\log3\) above follow by the same series. For the Euler constant, the elementary integral comparison
\(\gamma\ge H_{10000}-\log10001>0.577\)
gives the stated rationally certified lower bound. Thus every finite comparison in (11.7) has an explicit error bound.

Partial summation and \(D(u)\ge\log u+1.07\) for \(u\ge6\) give
\[
\begin{aligned}
S(z)\ge{}&
\sum_{q\le5}\frac{\mu^2(q)}{\varphi(q)}
\left(\frac z{z+q}-\frac z{z+6}\right)\\
&+\frac z{z+6}(\log6+1.07)
+\int_6^z\frac z{z+u}\frac{du}{u}.
\end{aligned}
\tag{11.12}
\]
This follows directly by integrating against the step function \(D\), keeping its terms below 6 exact; hence there is no endpoint approximation.
For \(z\ge100\), the first line is at least
\[
\frac{0.9}{z+6}
\sum_{q\le5}\frac{\mu^2(q)(6-q)}{\varphi(q)}
=\frac{9.675}{z+6}.
\]
The integral equals
\(\log z+\log(1+6/z)-\log12\), and
\(\log(1+6/z)\ge6/(z+6)\).
Consequently
\[
S(z)\ge\log z+1.07-\log2
+\frac{15.675-6(\log6+1.07)}{z+6}
{}>\log z+0.36.
\]
For the final comparison use \(\log2<0.694\), \(\log6<1.792\), and \(z+6\ge106\). This completes (11.7). \(\square\)

### 11.4. All interval lengths

**Theorem 11.1 (Montgomery–Vaughan).** For all \(x\ge0\) and \(y>1\),

\[
\pi(x+y)-\pi(x)\le\frac{2y}{\log y}
\tag{11.13}
\]

**Proof for large \(y\).** Let
\(N=\lfloor x+y\rfloor-\lfloor x\rfloor\), the number of consecutive integers in the interval. Suppose \(y>20000\); then \(N\ge19999\). Take
\(z=\sqrt{2N/3}\ge100\).
The primes greater than \(z\) omit the zero class at every sieving prime. In (11.6),
\[
N+\tfrac32qz=N(1+q/z).
\]
The second part of (11.7) therefore bounds their number by \(N/S(z)\). Including primes at most \(z\) gives
\[
\pi(x+y)-\pi(x)\le\frac{N}{\tfrac12\log N+0.15}+\frac{\sqrt N}{3}.
\tag{11.14}
\]
We used \(0.36+\tfrac12\log(2/3)>0.15\).
Also \(\pi(z)\le z/3<\sqrt N/3\) for \(z\ge100\): the integers coprime to 6 number at most \(z/3+1\); remove 1 and the four composites \(35,49,55,65\), and add the primes 2 and 3.

Put \(l=\log N\). For \(N\ge15000\), \(l>9.6\), \(l^2<\sqrt N\), and
\[
\frac{2N}{l}-\frac{N}{l/2+0.15}
=\frac{0.6N}{l(l+0.3)}
\ge\frac{N}{2l^2}
{}>\frac{\sqrt N}{2}
{}>\frac{\sqrt N}{3}+\frac2l.
\]
The last inequality follows from \(\sqrt N\,l>12\).
To verify \(l^2<\sqrt N\) throughout this range, it holds already at \(N=10000\), and the ratio \((\log N)^2/\sqrt N\) decreases for \(\log N>4\).
Thus (11.14) is less than \(2(N-1)/\log N\).
Finally \(N-1<y<N+1\). If \(y\ge N\), use monotonicity of \(t/\log t\) for \(t>e\); if \(N-1<y<N\), use
\[
\frac{N-1}{\log N}
<\frac{N-1}{\log(N-1)}
\le\frac y{\log y}.
\]
This proves (11.13) for large \(y\).

**Proof for \(1<y\le20000\).** Sieve directly by the primes at most \(z\). Inclusion–exclusion, with at most one rounding error for each squarefree divisor, gives
\[
\pi(x+y)-\pi(x)
\le y\prod_{p\le z}(1-1/p)+2^{\pi(z)}+\pi(z).
\tag{11.15}
\]
The last term restores the primes at most \(z\); this also covers intervals starting at 0.
For \(z=2,3,5,13\), respectively, the ratio of the right side to \(2y/\log y\) is
\[
f(y;\alpha,\beta)=(\log y)(\alpha+\beta/y)
\]
with the parameters in this table. Both endpoint values are bounded by the displayed rational upper bounds:

| Range of \(y\) | \(z\) | \(\alpha\) | \(\beta\) | Upper bounds at the endpoints |
|---|---:|---:|---:|---:|
| \([1,20]\) | 2 | \(1/4\) | \(3/2\) | 0, 0.974 |
| \([20,270]\) | 3 | \(1/6\) | 3 | 0.949, 0.996 |
| \([270,1000]\) | 5 | \(2/15\) | \(11/2\) | 0.861, 0.960 |
| \([1000,20000]\) | 13 | \(96/1001\) | 35 | 0.905, 0.968 |

These endpoint comparisons use the rational series (11.11). They control every real point in the indicated intervals. Indeed
\[
y^2f'(y)=\alpha y+\beta(1-\log y).
\]
For the first row its global minimum occurs at \(y=6\), and is
\(3-\tfrac32\log6>0\); hence \(f\) is increasing. For each later row the interval starts beyond \(\beta/\alpha\), where the displayed derivative numerator is increasing. It can therefore change sign at most once there, from negative to positive. Thus \(f\) has no interior maximum, and its endpoint values bound the whole interval. Each bound is less than 1. The four ranges cover every \(1<y\le20000\), proving (11.13) and completing the theorem. \(\square\)

The global-spacing sieve already explains the asymptotic constant 2. Its exact uniform form uses the extra denominator gain in (11.6), the explicit positive margin in (11.7), and a separate elementary treatment of short intervals. None of these arguments assumes a prime number theorem for short intervals.

## 12. Exercises

1. **Easy.** Prove the spacing assertion for distinct reduced Farey fractions with denominators at most \(Q\), including spacing across the endpoint of the unit interval.

2. **Medium.** Starting from the arithmetic large sieve, prove a uniform bound \(Cy/\log y\) for the number of primes in \((x,x+y]\), with an explicit \(C\) for \(y\ge2\). Show where the sharp analytic inequality gives the asymptotic constant \(2+\varepsilon\), and what constant follows from Gallagher's estimate alone.

3. **Medium.** Prove the duality principle for a finite bilinear form \(\sum_{r,n}A_{rn}a_n\overline{b_r}\). State the dual sharp large sieve, keeping the coefficient norm and the range of \(n\) exact.

4. **Medium.** Apply the arithmetic large sieve to a set of square integers in a block of \(N\) consecutive integers. Prove the required denominator estimate, treat the prime 2, and compare the answer with the elementary count of actual squares.

5. **Hard.** Prove Linnik's estimate (10.1). Explain why a positive density of smooth integers is needed, why the interval of sieving primes is \((\sqrt Q,Q]\), and why ordinary dyadic intervals would give a weaker global count.

## 13. Complete solutions

**1.** For any integer \(k\),
\(b/q-b'/q'-k=(bq'-b'q-kqq')/(qq')\).
Its numerator is a nonzero integer for distinct points modulo 1. Therefore its absolute value is at least 1, and minimizing over \(k\) gives distance at least \(1/(qq')\ge Q^{-2}\). This minimization includes the arc crossing 0. Include 0 just once, as the reduced fraction with denominator 1; nonreduced duplicate fractions must be removed.

**2.** Discard at most \(Q\) primes at most \(Q\), and sieve the others with \(\omega(p)=1\). The convolution calculation (7.1)–(7.3) proves \(L(Q)=\log Q+O(1)\), with error less than 200; the radical decomposition in (7.7) also gives \(L(Q)\ge\log Q\) for every \(Q\ge1\). The block has \(N-1\le y\), so the sharp arithmetic bound is (7.6). For \(Q=\sqrt y/(\log y)^2\), its numerator is \(y(1+o(1))\), its denominator is \((\tfrac12+o(1))\log y\), and the discarded \(Q\) primes are \(o(y/\log y)\). All errors are uniform in \(x\), and the explicit error bound makes the threshold effective. This yields \(2+\varepsilon\) for large \(y\). Taking \(Q=\sqrt y\) instead and using \(L(Q)\ge\tfrac12\log y\) gives at most \(4y/\log y\) for the sieved primes; the discarded \(Q\) primes are at most \(y/\log y\). Thus \(C=5\) works for all \(y\ge2\). Gallagher's numerator is \(\pi(N-1)+Q^2\), so the same large-\(y\) computation gives \(2\pi+\varepsilon\), and the simple all-\(y\) calculation gives \(C=2\pi+3\). To obtain the exact uniform constant 2, retain individual Farey spacings and apply the separate denominator and short-interval arguments in Section 11.

**3.** For \(\mathcal B(a,b)=\langle Aa,b\rangle\), the assertion \(|\mathcal B(a,b)|\le\sqrt C\|a\|_2\|b\|_2\) follows from \(\|Aa\|_2^2\le C\|a\|_2^2\) by Cauchy–Schwarz. Taking \(b=Aa\) gives the converse after canceling a nonzero norm. The identity \(\mathcal B(a,b)=\langle a,A^*b\rangle\) gives the same equivalence with the adjoint estimate. Thus the sharp dual inequality is

\[
\sum_{M<n\le M+N}\left|\sum_{r=1}^R b_r e(nx_r)\right|^2
\le(N-1+\delta^{-1})\sum_{r=1}^R|b_r|^2,
\]

for \(M\in\mathbb Z\), integer \(N\ge1\), and \(\delta\)-spaced circle points with \(0<\delta\le1\). Sign reversal follows by conjugating the arbitrary \(b_r\); it does not change the norm.

**4.** At an odd prime the image of squaring consists of 0 and \((p-1)/2\) nonzero residues. Thus \(\omega(p)=(p-1)/2\), giving \(g(p)=(p-1)/(p+1)\). At 2 both classes occur, so \(g(2)=0\). Define \(h\) by \(f=\mathbf1*h\), where \(f=\mu^2g\). Its values are exactly those in Section 8; the series \(\sum|h(d)|/d\) converges because each odd-prime local contribution is \(O(p^{-2})\), and the factor at 2 is finite. Hence (8.2) proves \(L(Q)\sim cQ\), \(c>0\). Taking \(Q=\sqrt N\) in (6.3) gives \(Z\ll\sqrt N\), adjusting an absolute constant for small \(N\). If the smallest square in the block is \(m^2\), its \(k\)-th distinct square is at least \((m+k-1)^2\), so its distance from the smallest is at least \((k-1)^2\). Since the block's extreme integers differ by \(N-1\), the actual count is at most \(1+\sqrt{N-1}\). The local sieve reproduces this order for any set with those same residue restrictions.

**5.** For \(0<\delta<1\), fix \(Q\), and take the integers at most \(\lfloor Q^2\rfloor\) whose prime factors are at most \(Q^{\delta/2}\). Section 9 proves that their number is \(\gg_\delta Q^2\): the fixed parameter is \(u=4/\delta\), and the delay-function identity (9.6) proves its limiting density is positive. If \(\sqrt Q<p\le Q\) and \(n_2(p)>p^\delta\), all these small factors are less than \(p^\delta\) and less than \(p\), so the entire set lies in the nonzero quadratic residues modulo \(p\). At least \(p/3\) classes are omitted. The prime-only arithmetic inequality with \(N\asymp Q^2\) then bounds the number of such exceptional \(p\) by a constant depending only on \(\delta\). Positive smooth density is what cancels the \(Q^2\) numerator; merely constructing a sublinear number of smooth integers would leave a growing bound. Successive square-root blocks have only \(O(\log\log x)\) members, giving (10.1). Ordinary dyadic blocks have \(O(\log x)\) members and would give only that weaker count. For \(\delta\ge1\), the exceptional set is empty because \(n_2(p)\le p-1\).

## References and proof coverage

The large sieve originates with Linnik; Gallagher's midpoint argument gives the elementary analytic estimate. The sharp interval-majorant method is due to Selberg, using Beurling's sign majorant. Montgomery developed the general arithmetic denominator. The delay function in Section 9 is Dickman's function; its fixed-parameter asymptotic is proved here from the elementary reciprocal-prime theorem.

Koukoulopoulos, *The Distribution of Prime Numbers*, Chapter 25, Theorems 25.9, 25.11 and 25.16, treats these results and their normalizations. The local-spacing method and the exact uniform prime bound are due to Montgomery and Vaughan, [“The large sieve”](https://doi.org/10.1112/S0025579300004708), *Mathematika* 20 (1973), 119–134, Theorems 1–2 and Sections 2–6. Their [“Hilbert's inequality”](https://doi.org/10.1112/jlms/s2-8.1.73), *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, supplies the weighted Hilbert method. Section 11 gives the full supporting argument, with independent rational certificates and an explicit harmonic remainder sufficient for the stated constants.

The analytic bounds, sharp constant, Farey form, arithmetic denominator, weighted local-spacing refinement, exact all-interval prime constant 2, square example, smooth-number bridge, Linnik sparsity theorem, and all five exercise solutions are proved above.
