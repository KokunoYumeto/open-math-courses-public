# Mean square distribution: the Barban–Davenport–Halberstam theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Bombieri–Vinogradov theorem takes the worst residue class for each modulus. A mean square averages over the classes as well. This extra averaging changes the scale: the expected total is \(Qx\log Q\), and a sharp bound remains available when \(Q\) is nearly as large as \(x\).

We use the character orthogonality of *Dirichlet characters*, the sharp primitive large sieve of *The multiplicative large sieve and bilinear forms with characters*, and *The Siegel–Walfisz theorem*. Lemma 1.1 of *The Bombieri–Vinogradov theorem* supplies elementary totient estimates, not that lesson's distribution theorem. For the smoothed calculation in Section 4, the exact zeta functional equation and \(\zeta(0)=-1/2\) are Corollary 3.2 of *Poisson summation, theta, and the functional equation* in *The Riemann zeta function*. The gamma estimate used there is Theorem 3.1 and Corollary 4.1 of *The Gamma function and Stirling's formula* in the same course.

Throughout, \(x\ge3\), \(1\le Q\le x\), \(L=\log(2x)\), and

\[
V(x,Q)=\sum_{q\le Q}\sum_{\substack{b\bmod q\\(b,q)=1}}
\left(\psi(x;q,b)-\frac{x}{\varphi(q)}\right)^2.
\tag{0.1}
\]

The errors inside this expression are real. Character sums below are complex and are squared by taking their absolute values. Bounds involving Siegel–Walfisz have ineffective constants; the finite identities and the totient calculations are effective.

## 1. From residue classes to primitive characters

Center every character, including the principal one:

\[
\psi'(x,\chi)=\psi(x,\chi)-\mathbf1_{\chi=\chi_0}x.
\]

Orthogonality gives the exact identity

\[
V(x,Q)=\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\psi'(x,\chi)|^2.
\tag{1.1}
\]

Indeed, the error in class \(b\) is
\(\varphi(q)^{-1}\sum_\chi\overline{\chi(b)}\psi'(x,\chi)\).
Expanding its absolute square and summing over unit classes kills every off-diagonal character pair. The principal term is essential: \(\psi(x,\chi_0)\) is not exactly \(x\).

Let \(\chi\) be induced by a primitive character \(\chi^*\) of conductor \(d\mid q\). Then

\[
\psi(x,\chi^*)-\psi(x,\chi)
=\sum_{\substack{p\mid q\\ p\nmid d}}
\log p\sum_{1\le j\le\log x/\log p}\chi^*(p)^j.
\tag{1.2}
\]

Both characters are principal precisely when \(d=1\), so their subtracted terms agree. The absolute difference of their centered sums is at most
\(\omega(q)\log x\ll L^2\). Applying \(|u+v|^2\le2|u|^2+2|v|^2\) in (1.1), and assigning each character to its unique primitive ancestor, gives

\[
V(x,Q)\ll QL^4+
\sum_{d\le Q}\frac{\log(2Q/d)}{\varphi(d)}
\sum_{\chi\bmod d}^{*}|\psi'(x,\chi)|^2.
\tag{1.3}
\]

Here we used the previously proved bound

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll\frac{\log(2Q/d)}{\varphi(d)}.
\tag{1.4}
\]

For completeness, \(\varphi(dm)\ge\varphi(d)\varphi(m)\) follows at every prime, and
\(\sum_{m\le z}1/\varphi(m)\ll\log(2z)\); these give (1.4).
The error \(QL^4\) arises because there are exactly \(\varphi(q)\) characters modulo \(q\), cancelling the factor \(1/\varphi(q)\). There is no additional factor \(q\).

## 2. The mean-square upper bound

**Theorem 2.1 (Barban–Davenport–Halberstam).** For every fixed \(A>0\),

\[
V(x,Q)\ll_A xQ\log x
\qquad
\left(x(\log x)^{-A}\le Q\le x\right).
\tag{2.1}
\]

The constant is ineffective. The same proof works with the slightly smaller lower endpoint \(xL^{-A}\).

**Proof.** Put \(R=L^{A+2}\). For sufficiently large \(x\), \(R<Q\). For conductors \(d\le R\), Siegel–Walfisz gives
\[
|\psi'(x,\chi)|\ll_A x e^{-c_A\sqrt{\log x}}.
\]
For \(d>1\) a primitive character is nonprincipal; for \(d=1\) this is the usual prime number theorem. Since the number of primitive characters is at most \(\varphi(d)\), their contribution to (1.3) is
\[
\ll_A x^2RL e^{-2c_A\sqrt{\log x}}\ll_A xQ.
\tag{2.2}
\]

For \(r<d\le2r\), with \(r\ge R\), there is no centering term. Also
\[
\frac{\log(2Q/d)}{\varphi(d)}
\ll\frac{\log(2Q/r)}r\frac d{\varphi(d)}.
\]
The primitive large sieve, applied to \(a_n=\Lambda(n)\mathbf1_{n\le x}\), therefore bounds this block by
\[
\ll\frac{\log(2Q/r)}r(x+r^2)\sum_{n\le x}\Lambda(n)^2
\ll \left(\frac{x^2}r+xr\right)L\log(2Q/r).
\tag{2.3}
\]
The last step uses \(\Lambda(n)^2\le(\log x)\Lambda(n)\) and the elementary Chebyshev bound \(\psi(x)\ll x\).

Choose \(r=2^jR\) until \(Q\) is reached, truncating the final block if necessary. Geometric summation gives
\[
\sum_r\frac{\log(2Q/r)}r\ll\frac L R,
\qquad
\sum_r r\log(2Q/r)\ll Q.
\tag{2.4}
\]
For the second bound, read the blocks backwards from \(Q\): the terms are at most a constant times
\(Q\,2^{-k}(k+1)\).
Thus the large conductors contribute
\[
\ll\frac{x^2L^2}R+xQL
\le xQ+xQL.
\]
Finally \(QL^4\ll xQL\) for large \(x\). This proves (2.1); increasing the ineffective constant covers the remaining bounded range. \(\square\)

The split is by conductor, not by the displayed modulus. A character of small conductor can recur at many large moduli. The logarithmic weight in (1.3) counts those recurrences.

**Corollary 2.2 (almost all pairs).** Fix \(A>0\) and \(\varepsilon>0\), and put
\[
Q=x(\log x)^{-A-2}.
\]
Among the pairs \((q,b)\) with \(q\le Q\) and \((b,q)=1\), all but
\(o(\sum_{q\le Q}\varphi(q))\) satisfy
\[
\left|\psi(x;q,b)-\frac{x}{\varphi(q)}\right|
\le\frac{\varepsilon x}{\varphi(q)}.
\tag{2.5}
\]

**Proof.** A failing pair contributes at least
\(\varepsilon^2x^2/Q^2\) to \(V\). By Theorem 2.1 with parameter \(A+2\), the number of failures is at most
\[
\ll_A\frac{Q^3\log x}{\varepsilon^2x}.
\tag{2.6}
\]
We need a lower bound for the number of pairs. For an integer \(N\), at most
\[
N^2\sum_p\frac1{p^2}
\le N^2\sum_{n\ge2}\frac1{n^2}
\le\frac34N^2
\]
ordered pairs in \([1,N]^2\) have a common prime divisor; the last inequality follows from
\(1/4+\int_2^\infty t^{-2}dt=3/4\).
The number of coprime ordered pairs is \(2\sum_{q\le N}\varphi(q)-1\), so
\(\sum_{q\le Q}\varphi(q)\gg Q^2\). Dividing (2.6) by this lower bound gives
\[
\ll_A\varepsilon^{-2}\frac{Q\log x}{x}
=O_A\!\left(\varepsilon^{-2}(\log x)^{-A-1}\right)=o(1).
\]
\(\square\)

One can even take \(\varepsilon=(\log x)^{-(A+1)/4}\): the exceptional proportion is then \(O_A((\log x)^{-(A+1)/2})\).
This is an assertion about most pairs. It does not assert that every reduced class is good for most moduli.

## 3. Two sums involving the totient

The upper bound is already proved. To obtain an asymptotic, we need more precision in an elementary sum. Write

\[
\mathcal C=\frac{\zeta(2)\zeta(3)}{\zeta(6)},
\qquad
a_d=\frac{\mu^2(d)}{d\varphi(d)},
\qquad
c_1=\mathcal C\gamma-\sum_{d\ge1}a_d\log d.
\tag{3.1}
\]

The last series converges absolutely. Indeed,
\(\sum_{d\le z}d^2a_d\le\sum_{d\le z}d/\varphi(d)\ll z\).
Dyadic summation then gives
\[
\sum_{d>Y}a_d\ll Y^{-1},
\qquad
\sum_{d>Y}a_d\log(d/Y)\ll Y^{-1}.
\tag{3.2}
\]

**Lemma 3.1.** Uniformly for \(Y\ge1\),
\[
\sum_{n\le Y}\frac1{\varphi(n)}
=\mathcal C\log Y+c_1+
O\!\left(\frac{\log(2Y)}Y\right).
\tag{3.3}
\]

**Proof.** The identity
\(n/\varphi(n)=\sum_{d\mid n}\mu^2(d)/\varphi(d)\) gives
\[
\sum_{n\le Y}\frac1{\varphi(n)}
=\sum_{d\le Y}a_d H_{\lfloor Y/d\rfloor}.
\]
Use \(H_{\lfloor t\rfloor}=\log t+\gamma+O(1/t)\), valid for real \(t\ge1\). The accumulated error is
\[
\ll \frac1Y\sum_{d\le Y}\frac{\mu^2(d)}{\varphi(d)}
\ll\frac{\log(2Y)}Y.
\]
Extending the main terms to all \(d\), (3.2) bounds the tails. Finally
\(\sum_da_d=\prod_p(1+1/[p(p-1)])=\mathcal C\). \(\square\)

Define the quadratic smoothing
\[
W(Y)=\sum_{n\le Y}\frac{(1-n/Y)^2}{\varphi(n)}.
\tag{3.4}
\]
It has two secondary terms of size \(1/Y\), one containing \(\log Y\).
That logarithm will change the main term of the variance from \(Qx\log x\) to \(Qx\log Q\).

## 4. The smoothed totient sum, with its secondary term

**Lemma 4.1.** There are absolute real constants \(a,b\) such that, for every fixed \(\eta>0\),
\[
W(Y)=\mathcal C\log Y+a+\frac{\log Y+b}{Y}
+O_\eta(Y^{-3/2+\eta})
\qquad(Y\ge1).
\tag{4.1}
\]
In particular, one may take
\[
\begin{aligned}
F(s)&=\prod_p\left(1+\frac1{(p-1)p^{s+2}}
-\frac1{(p-1)p^{2s+3}}\right),\\
a&=\mathcal C\left(\gamma+\frac{\zeta'(2)}{\zeta(2)}
+\frac{F'(0)}{F(0)}-\frac32\right),\\
&=c_1-\frac32\mathcal C,\\
b&=\gamma-2\zeta'(0)+F'(-1).
\end{aligned}
\tag{4.2}
\]

**Proof.** It suffices to treat \(0<\eta<1/4\), since a smaller positive exponent gives every weaker stated remainder. For \(\Re s>0\), direct multiplication of local factors gives
\[
D(s):=\sum_{n\ge1}\frac1{\varphi(n)n^s}
=\zeta(s+1)\zeta(s+2)F(s).
\tag{4.3}
\]
The coefficients of \(F\) at \(p,p^2\) are
\(1/[p^2(p-1)]\) and \(-1/[p^3(p-1)]\), respectively.
Thus its Dirichlet series is absolutely convergent, uniformly bounded and holomorphic in
\(\Re s\ge-3/2+\eta\): the two local absolute sums are bounded by constant multiples of
\(p^{-3+u}\) and \(p^{-4+2u}\), where \(u=3/2-\eta\), and both exponents are less than \(-1\).
Furthermore,
\[
F(0)=\prod_p(1+p^{-3})=\frac{\zeta(3)}{\zeta(6)},
\qquad F(-1)=1,
\qquad
F'(-1)=\sum_p\frac{\log p}{p(p-1)}.
\tag{4.4}
\]
These assertions follow at each prime; differentiating the uniformly convergent product near \(-1\) is legitimate.

The Mellin kernel for a quadratic weight is
\[
(1-r^{-1})_+^2
=\frac1{2\pi i}\int_{(c)}
\frac{2r^s}{s(s+1)(s+2)}\,ds
\qquad(r>0,\ c>0).
\tag{4.5}
\]
For \(r>1\), closing the contour to the left picks up residues
\(1,-2/r,1/r^2\). For \(r<1\), closing to the right encloses no poles and gives zero. On horizontal segments the denominator is \(O(|t|^3)\); the outer vertical integral tends to zero because \(r^{\Re s}\) decays in the chosen direction. The case \(r=1\) follows by continuity and absolute convergence. This proves (4.5).

Insert \(r=Y/n\), sum on a line \(c>0\), and interchange sum and integral absolutely:
\[
W(Y)=\frac1{2\pi i}\int_{(c)}
\frac{2\zeta(s+1)\zeta(s+2)F(s)Y^s}
{s(s+1)(s+2)}\,ds.
\tag{4.6}
\]
Move the line to \(\sigma=-3/2+\eta\). We justify both the move and its remainder explicitly. On this line, the zeta functional equation and vertical Stirling estimate give
\[
|\zeta(s+1)|\ll_\eta(1+|t|)^{1-\eta}.
\]
The reflected zeta factor has real part \(3/2-\eta>1\) and is bounded by its absolutely convergent series.
For \(\Re z>0\), partial summation of \(\lfloor u\rfloor=u-\{u\}\) gives the continuation
\[
\zeta(z)=\sum_{n\le N}n^{-z}
+\frac{N^{1-z}}{z-1}
-z\int_N^\infty\{u\}u^{-z-1}\,du
\tag{4.7}
\]
when \(N\) is a positive integer. Initially this follows for \(\Re z>1\), and the integral continues it to \(\Re z>0\). With \(N\asymp1+|t|\) and \(z=s+2\), the finite sum and the integral are
\(O_\eta((1+|t|)^{1/2-\eta})\), as is the remaining term. Consequently the integrand on the new line is
\[
\ll_\eta Y^{-3/2+\eta}(1+|t|)^{-3/2-2\eta},
\]
which is integrable.

For the horizontal edges, (4.7) uniformly gives
\(\zeta(z)\ll (1+|t|)^{\max(1-\Re z,0)}\log(2+|t|)\) on any fixed positive strip. For \(-1/2+\eta\le\Re z\le1/4\), apply the functional equation to \(z\) and use this same estimate on \(1-z\). These two bounds together give, throughout the strip of the contour,
\[
\zeta(s+1)\zeta(s+2)
\ll_{\eta,c}(1+|t|)^{3/2-2\eta}\log^2(2+|t|).
\]
The factor \(|t|^{-3}\) makes both horizontal integrals tend to zero. The bounded segment with \(|t|\le1\) on the new line has no pole. Thus the remainder in (4.6) is \(O_\eta(Y^{-3/2+\eta})\).

The crossed poles are double poles at \(s=0\) and \(s=-1\). At zero,
\[
\frac2{s(s+1)(s+2)}=\frac1s-\frac32+O(s),
\]
so the residue is \(\mathcal C\log Y+a\). At \(s=-1+w\),
\[
\frac2{s(s+1)(s+2)}=-\frac2w+O(w).
\]
Using \(\zeta(w)=-1/2+\zeta'(0)w+O(w^2)\),
\(\zeta(1+w)=1/w+\gamma+O(w)\), and \(F(-1)=1\), the residue is
\[
\frac{\log Y+\gamma-2\zeta'(0)+F'(-1)}Y.
\]
This proves (4.1)–(4.2). The identity \(a=c_1-3\mathcal C/2\) follows by comparing the constant term at \(s=0\) in
\(D(s)=\zeta(s+1)\sum_d a_dd^{-s}\); termwise differentiation is justified by (3.2). \(\square\)

The factor \(s+2\) in (4.5)–(4.6) is required. Omitting it gives a different weight, a different convergence rate and incorrect residues.

## 5. Switching a large modulus to a small complementary variable

For \(1\le y\le x\), let
\[
S(y)=\sum_{y<q\le x}
\sum_{\substack{m<n\le x\\m\equiv n\pmod q}}
\Lambda(m)\Lambda(n).
\tag{5.1}
\]
There is no coprimality restriction in this definition. Write \(n-m=kq\). This gives the exact finite rearrangement
\[
S(y)=\sum_{k\le x/y}\sum_{m\le x-ky}\Lambda(m)
\left(\psi(x;k,m)-\psi(m+ky;k,m)\right).
\tag{5.2}
\]
The strict condition \(q>y\) corresponds to \(n>m+ky\), including when \(ky\) is not an integer. A term with \(m=x-ky\) contributes zero.

**Lemma 5.1.** For every fixed \(D>0\), uniformly for
\(xL^{-D}\le y\le x\),
\[
S(y)=\frac{x^2}{2}W(x/y)+O_D(xy).
\tag{5.3}
\]
The constant is ineffective.

**Proof.** The complementary modulus is small:
\(k\le x/y\le L^D\). If \((m,k)>1\) and both weights in (5.2) are nonzero, then \(m=p^a\), \(n=p^b\) for the same prime \(p\mid k\). Thus these pairs contribute at most
\[
\sum_{k\le L^D}\sum_{p\mid k}
\left\lfloor\frac{\log x}{\log p}\right\rfloor^2(\log p)^2
\ll_D L^{D+3}\ll_D xy.
\tag{5.4}
\]

For the remaining \(m\), apply Siegel–Walfisz to the two endpoints in (5.2). Both are at least \(y\ge xL^{-D}\ge\sqrt{x}\) for sufficiently large \(x\). Hence
\(k\le L^D\le(\log t)^{2D+2}\) at either endpoint \(t\), and
\[
\psi(x;k,m)-\psi(m+ky;k,m)
=\frac{x-m-ky}{\varphi(k)}
+O_D\!\left(xe^{-c_D\sqrt{\log x}}\right).
\tag{5.5}
\]
Since \(\sum_{m\le x}\Lambda(m)\ll x\), the summed error is
\(O_D(x^2L^D e^{-c_D\sqrt{\log x}})=O_D(xy)\).

Set \(z=x-ky\). Removing \((m,k)=1\) from the main term of (5.5) costs at most
\[
\sum_{k\le L^D}\frac{x}{\varphi(k)}
\sum_{\substack{p^a\le x\\p\mid k}}\log p
\ll_D xL^{D+2}\ll_D xy.
\tag{5.6}
\]
This deliberately generous bound follows from \(\varphi(k)\ge1\) and
\(\sum_{p^a\le x,p\mid k}\log p\le\omega(k)\log x\).

The ordinary prime number theorem also gives, uniformly for every \(0\le z\le x\),
\[
\sum_{m\le z}\Lambda(m)(z-m)
=\int_0^z\psi(u)\,du
=\frac{z^2}{2}
+O\!\left(x^2e^{-c'\sqrt{\log x}}\right).
\tag{5.7}
\]
To see the uniformity when \(z\) is small, split the integral at \(\sqrt{x}\). Below that point the error is \(O(x)\) by Chebyshev; above it the prime number theorem bounds
\(|\psi(u)-u|\) by \(O(xe^{-c'\sqrt{\log x}})\).
Shrinking \(c'\) absorbs \(O(x)\). Thus no distribution assertion at a tiny endpoint is being used.

Insert (5.7) in the main term of (5.5). Summing its error uses
\(\sum_{k\le L^D}1/\varphi(k)\ll\log(2L^D)\), and again gives \(O_D(xy)\). The main term is exactly
\[
\frac12\sum_{k\le x/y}\frac{(x-ky)^2}{\varphi(k)}
=\frac{x^2}{2}W(x/y).
\]
\(\square\)

With \(\eta=1/4\) in Lemma 4.1, (5.3) becomes
\[
S(y)=
\frac{\mathcal Cx^2}{2}\log(x/y)
+\frac{ax^2}{2}
+\frac{xy}{2}\log(x/y)
+O_D(xy).
\tag{5.8}
\]
Indeed, the \(bxy/2\) term is included in the error, and
\(x^2(y/x)^{5/4}\le xy\).

## 6. The full asymptotic

**Theorem 6.1 (Montgomery–Hooley mean-square asymptotic).** For every fixed \(A>0\),
\[
V(x,Q)=Qx\log Q+O_A(Qx)
\qquad
\left(x(\log x)^{-A}\le Q\le x\right).
\tag{6.1}
\]
The error constant is ineffective. In particular,
\(V(x,Q)\sim Qx\log Q\), uniformly in this range.

**Proof.** Put \(Q_1=xL^{-A-2}\). Applying Theorem 2.1 with parameter \(A+3\) gives
\[
V(x,Q_1)\ll_A xQ_1L\ll_A Qx.
\tag{6.2}
\]
The slightly enlarged parameter is harmless and ensures that \(Q_1\) lies above the theorem's stated lower endpoint for large \(x\).
We may therefore compute the variance over \(Q_1<q\le Q\).

Let
\[
B_q=\sum_{(b,q)=1}\psi(x;q,b)^2,
\qquad
A_q=\sum_{(b,q)=1}\psi(x;q,b).
\]
Expanding the square gives
\[
V(x,Q)-V(x,Q_1)
=\sum_{Q_1<q\le Q}
\left(B_q-\frac{x^2}{\varphi(q)}
-\frac{2x}{\varphi(q)}(A_q-x)\right).
\tag{6.3}
\]
The principal sum is
\[
A_q=\psi(x)-
\sum_{p\mid q}\left\lfloor\frac{\log x}{\log p}\right\rfloor\log p
=x+O\!\left(xe^{-c\sqrt{\log x}}+L^2\right).
\]
Using \(\sum_{q\le Q}1/\varphi(q)\ll L\), the last term of (6.3), summed over \(q\), is
\[
O\!\left(x^2Le^{-c\sqrt{\log x}}+xL^3\right)=O_A(Qx).
\tag{6.4}
\]

The sum \(B_q\) counts weighted pairs \(m,n\le x\), congruent modulo \(q\), with \((mn,q)=1\).
Omitting this coprimality condition costs at most
\[
\sum_{p\mid q}\left\lfloor\frac{\log x}{\log p}\right\rfloor^2(\log p)^2
\ll L^3
\tag{6.5}
\]
for each \(q\). To justify this, a removed pair with nonzero weights must have both \(m,n\) powers of a common prime dividing \(q\). The total cost \(O(QL^3)\) is \(O(Qx)\).

The diagonal \(m=n\) contributes
\[
(Q-Q_1+O(1))\sum_{n\le x}\Lambda(n)^2
=Qx\log x+O_A(Qx).
\tag{6.6}
\]
Here
\[
\sum_{n\le x}\Lambda(n)^2=x\log x+O(x).
\tag{6.7}
\]
Indeed, partial summation gives
\(\sum_{p\le x}(\log p)^2=\theta(x)\log x-\int_2^x\theta(u)\,du/u
=x\log x+O(x)\);
the prime number theorem makes the errors \(O(x)\), and the proper prime powers contribute
\(O(\sqrt{x}L^2)=O(x)\).
The discarded \(Q_1x\log x\) and rounding error in (6.6) are also \(O_A(Qx)\).

The off-diagonal pairs contribute exactly
\(2(S(Q_1)-S(Q))\). Both endpoints satisfy the range of Lemma 5.1 with \(D=A+2\). Equation (5.8) gives
\[
\begin{aligned}
2(S(Q_1)-S(Q))
={}&\mathcal Cx^2\log(Q/Q_1)
+xQ_1\log(x/Q_1)\\
&-xQ\log(x/Q)+O_A(Qx).
\end{aligned}
\tag{6.8}
\]
The constant term \(ax^2\) cancels exactly. The term
\(xQ_1\log(x/Q_1)\ll_A xQ_1\log L\) is \(O_A(Qx)\).

By Lemma 3.1,
\[
x^2\sum_{Q_1<q\le Q}\frac1{\varphi(q)}
=\mathcal Cx^2\log(Q/Q_1)
+O_A\!\left(\frac{x^2L}{Q_1}\right)
=\mathcal Cx^2\log(Q/Q_1)+O_A(Qx).
\tag{6.9}
\]
The last comparison uses \(Q\ge x(\log x)^{-A}\) and
\(x^2L/Q_1=xL^{A+3}=o_A(Qx)\).
The \(c_1\) terms also cancel. Combining (6.2)–(6.9), the two terms containing \(\mathcal Cx^2\log(Q/Q_1)\) cancel, leaving
\[
Qx\log x-Qx\log(x/Q)+O_A(Qx)
=Qx\log Q+O_A(Qx).
\]
Finally \(\log Q\sim\log x\) uniformly in the stated range, so the error is \(o(Qx\log Q)\). \(\square\)

The auxiliary cutoff is of size \(x\) divided by a power of \(\log x\). A cutoff of size \(x^2\) divided by such a power would exceed \(Q\) and could not be discarded by (6.2).

## 7. A direct count and the meaning of the main term

At \(Q=x\), Theorem 6.1 reads
\[
V(x,x)=x^2\log x+O(x^2).
\tag{7.1}
\]
This includes the requested direct-count bound \(O(x^2\log x)\). The count in its proof has a useful concrete interpretation. Each diagonal prime-power weight \(\Lambda(n)^2\) is counted once per modulus, giving \(x^2\log x+O(x^2)\). For an off-diagonal pair, write \(n-m=kq\), sum first over \(k\le L^{A+2}\) after removing \(q\le Q_1\), and use (5.2). Its large \(x^2\log L\) term cancels the same term from the subtracted class means. Bounding the off-diagonal and mean terms separately by their absolute sizes would lose this cancellation.

For numerical examples, the following values use every reduced class and the definition (0.1). The class sum is independently checked by counting divisors of each prime-power difference; (1.1) is also checked at small moduli. The data illustrate convergence; they do not certify the asymptotic error constant.

| \(x\) | \(Q\) | \(V(x,Q)\) | \(V(x,Q)/(Qx\log Q)\) |
|---:|---:|---:|---:|
| \(100\) | \(100\) | \(11948.9255\) | \(0.259468\) |
| \(500\) | \(500\) | \(587693.0382\) | \(0.378266\) |
| \(1000\) | \(500\) | \(1147453.8125\) | \(0.369276\) |
| \(1000\) | \(1000\) | \(2967554.8484\) | \(0.429598\) |

A diagonal-only heuristic gives \(Qx\log x\), because
\(\sum_{n\le x}\Lambda(n)^2\sim x\log x\).
Congruent distinct prime powers are correlated with the subtracted mean. Their net contribution is
\(-Qx\log(x/Q)+O_A(Qx)\), as (6.8)–(6.9) show.
This explains both the constant \(1\) and the occurrence of \(\log Q\).
In the present range \(\log Q=\log x+O_A(\log\log x)\), so the diagonal heuristic has the right first-order size, but it misses the more precise correction.

For comparison, GRH gives individual errors \(O(\sqrt{x}\log^2(qx))\). Squaring and summing that estimate over all \(\varphi(q)\) classes yields a much larger bound of order \(xQ^2L^4\). The mean-square theorem comes from orthogonality and averaging before estimating the character sums.

## 8. Exercises

1. **Easy.** Deduce the almost-all-pairs assertion for \(Q=x(\log x)^{-A-2}\), and give a possible tolerance tending to zero.
2. **Medium.** Compute the variance at \(Q=x\) by weighted pair counting, up to an error bound sufficient to prove \(V(x,x)=O(x^2\log x)\). Identify the cancellation that prevents an extra \(\log\log x\) term.
3. **Medium.** Explain why a diagonal heuristic predicts \(Qx\log x\), and how the complementary-variable calculation changes this to \(Qx\log Q\).
4. **Hard.** Give the full mean-square upper-bound argument, including the principal character, passage to conductors, and summation of the large-conductor blocks.

## 9. Solutions

1. A bad pair contributes at least \(\varepsilon^2x^2/Q^2\), since \(\varphi(q)\le Q\). Theorem 2.1 with parameter \(A+2\) therefore gives at most
\(O_A(\varepsilon^{-2}Q^3\log x/x)\) such pairs. The elementary coprime-pair count in Corollary 2.2 gives \(\sum_{q\le Q}\varphi(q)\gg Q^2\). Thus the bad proportion is
\(O_A(\varepsilon^{-2}(\log x)^{-A-1})\), tending to zero for fixed \(\varepsilon\). Taking \(\varepsilon=(\log x)^{-(A+1)/4}\) also works and gives proportion \(O_A((\log x)^{-(A+1)/2})\).

2. Take \(Q_1=xL^{-3}\). Theorem 2.1, with parameter \(4\), bounds the small-modulus variance by \(O(x^2/L^2)\). Expanding the remaining squares gives the unrestricted weighted pair count minus
\(x^2\sum_{Q_1<q\le x}1/\varphi(q)\), with error \(O(x^2)\) by (6.4)–(6.5). The diagonal is
\(x^2\log x+O(x^2)\) by (6.7). The off-diagonal is \(2S(Q_1)\), since \(S(x)=0\). From (5.8),
\[
2S(Q_1)=\mathcal Cx^2\log(x/Q_1)+ax^2
+xQ_1\log(x/Q_1)+O(xQ_1).
\]
Lemma 3.1 gives
\[
x^2\sum_{Q_1<q\le x}\frac1{\varphi(q)}
=\mathcal Cx^2\log(x/Q_1)+O(x^2L/Q_1).
\]
The latter error is \(O(xL^4)=O(x^2)\), and
\(xQ_1\log(x/Q_1)=O(x^2)\). The common
\(\mathcal Cx^2\log(x/Q_1)\) terms cancel. The \(ax^2\) term is part of \(O(x^2)\), giving the stronger result (7.1), hence the requested bound. Every pair rearrangement is finite; the distribution input is used only at the short complementary moduli.

3. The diagonal contributes about \(Q\sum_{n\le x}\Lambda(n)^2\sim Qx\log x\). Switching \(n-m=kq\), the quadratic weight in the short \(k\)-sum creates the secondary term \(x y\log(x/y)\) in \(2S(y)\). Subtracting its values at \(Q_1\) and \(Q\), then subtracting the mean square, leaves \(-Qx\log(x/Q)+O_A(Qx)\). Adding it to the diagonal gives \(Qx\log Q+O_A(Qx)\). The identity of the two logarithms is exact; the initial description of the diagonal as a random variance is a heuristic.

4. Define \(\psi'=\psi-\mathbf1_{\chi=\chi_0}x\). Orthogonality gives (1.1) for every \(q\). If \(\chi\) is induced from conductor \(d\), its centered sum differs from the primitive centered sum by (1.2), bounded by \(O(L^2)\). Squaring with \(|u+v|^2\le2|u|^2+2|v|^2\), summing over characters, and then summing \(q\) yields \(O(QL^4)\) plus primitive sums with weight
\(\sum_{q\le Q,d\mid q}1/\varphi(q)\).
The inequality \(\varphi(dm)\ge\varphi(d)\varphi(m)\) and the totient sum bound give (1.4), hence (1.3). Split at \(R=L^{A+2}\). For \(d\le R\), Siegel–Walfisz bounds each centered sum by \(O_A(xe^{-c_A\sqrt{\log x}})\), including the conductor-one principal sum. There are at most \(\varphi(d)\) primitive characters, so this portion is
\(O_A(x^2RL e^{-2c_A\sqrt{\log x}})=O_A(xQ)\).
For \(r<d\le2r\), \(r\ge R\), there is no principal term. The sharp primitive large sieve gives
\[
\sum_{r<d\le2r}\frac d{\varphi(d)}
\sum_\chi^*|\psi(x,\chi)|^2
\ll (x+r^2)\sum_{n\le x}\Lambda(n)^2
\ll (x+r^2)xL.
\]
Multiplying by \(\log(2Q/r)/r\) gives (2.3). Sum over \(r=2^jR\). The decreasing part is \(O(x^2L^2/R)\le O(xQ)\); the increasing part is \(O(xQL)\) by the backwards geometric sum in (2.4). The induction error \(QL^4\) is \(O(xQL)\). Thus \(V(x,Q)\ll_A xQ\log x\) throughout the stated range, with ineffective constant only from Siegel–Walfisz.

## 10. Proof scope and references

All mean-square results stated here, including the asymptotic (6.1), have been proved. The prerequisite results named in the introduction are internal inputs with exact locators. No external asymptotic is being used in their place. A range such as \(Q=x^{1-\delta}\), with fixed \(\delta>0\), is outside Theorems 2.1 and 6.1; no assertion about that smaller range is made here.

The historical names refer to the development of the upper bound by Barban, Davenport and Halberstam, and the asymptotic by Montgomery and Hooley.

