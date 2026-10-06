# The least prime in a progression: Linnik's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Dirichlet's theorem guarantees a prime in every reduced progression. It does not give a uniform scale at which the first prime must occur. Linnik's theorem supplies such a scale: one absolute, effectively computable power of the modulus works for every reduced class.

Three principles enter the proof. A classical zero-free region prevents an ordinary zero from approaching \(1\) too closely. A log-free density estimate counts the remaining zeros without a spare power of a logarithm. If one real zero approaches \(1\), an improved density estimate contains its distance from \(1\); this gives Deuring–Heilbronn repulsion and controls the particularly small main term in some residue classes. We prove that density estimate and its repulsion consequence here.

The inputs are the character identities in *Dirichlet characters* and *Gauss sums*, the explicit formula in *Counting zeros and the explicit formula for \(\psi(x,\chi)\)*, the classical results in Sections 1–6 of *Zero-free regions and the exceptional zero*, and the sharp and hybrid sieves in *The multiplicative large sieve and bilinear forms with characters*. We use the fully analytic effective value bound, Theorem 4.1 of *Values of Dirichlet L-functions at \(s=1\)*; no ineffective Siegel constant is needed. Chebyshev's bounds and the Mertens estimate used below were proved in *Dirichlet's theorem on primes in arithmetic progressions* and *The Siegel–Walfisz theorem*.

## 1. The family and the exceptional zero

Let \(T\ge2\), \(H=\log(2T)\), and consider all primitive characters of conductor at most \(T\), including the principal character of conductor \(1\). The classical region and Page's theorem give an absolute effective \(a_0>0\) such that the box
\[
\Re s>1-\frac{a_0}{H},
\qquad |\Im s|\le T
\tag{1.1}
\]
contains at most one nontrivial zero among the whole family. If present, it is simple and real, belongs to a real nonprincipal character \(\chi_1\), and is denoted by
\(\beta_1=1-\delta\), of conductor \(d_1\le T\).
For different real conductors the Page argument uses their common modulus, at most \(T^2\); decreasing the effective constant gives (1.1).
The height restriction is part of this statement.

Put \(E=1\) if this zero exists and \(E=0\) otherwise. Let
\[
N^*(\sigma,T)=
\sum_{d\le T}\sum_{\chi\bmod d}^{*}
\#\{\rho:\Re\rho\ge\sigma,\ |\Im\rho|\le T,\ \rho\ne\beta_1\}.
\tag{1.2}
\]
Exclusion is by this single zero with its multiplicity one, not by its entire character.
When \(E=1\), the independently analytic bound (6.4) of *Zero-free regions and the exceptional zero* gives
\[
\delta\ge c_0d_1^{-1/2}\log^{-4}(2d_1)
\ge c_1T^{-1/2}H^{-4}.
\tag{1.3}
\]
Both constants are effective. The weaker logarithmic power \(4\), rather than the algebraic value bound's power \(2\), is sufficient.

Our main support theorem is
\[
N^*(\sigma,T)\le C T^{c(1-\sigma)}
\quad(1/2\le\sigma\le1),
\tag{1.4}
\]
and, if \(E=1\),
\[
N^*(\sigma,T)\le C\delta H T^{c(1-\sigma)}.
\tag{1.5}
\]
The constants \(c,C\) will be absolute and effective. The extra factor in (1.5) is indispensable.

## 2. A finite power-sum lemma

**Lemma 2.1.** Suppose \(N\ge1\), \(\max_j|z_j|=R>0\), and \(\ell\ge N\) is an integer. For some integer \(k\) with \(\ell+1\le k\le2\ell\),
\[
\left|\sum_{j=1}^Nz_j^k\right|
\ge2(16e)^{-\ell}R^k
\ge2(50)^{-k}R^k.
\tag{2.1}
\]
Repeated values are allowed.

**Proof.** Scale to \(R=1\), and first suppose the \(z_j\) are distinct. We need an elementary polynomial fact: if a real monic polynomial \(f\) has degree \(N\), then on any real interval of length \(l\),
\[
\max |f|\ge2(l/4)^N.
\tag{2.2}
\]
To prove it on \([-1,1]\), use \(T_N(\cos u)=\cos Nu\). Its recurrence
\(T_{n+1}=2tT_n-T_{n-1}\) shows that its leading coefficient is \(2^{N-1}\).
At \(t_j=\cos(j\pi/N)\), \(T_N(t_j)=(-1)^j\).
If a monic \(f\) had supremum less than \(2^{1-N}\), then
\(f-2^{1-N}T_N\), a polynomial of degree at most \(N-1\), would change sign in all \(N\) intervals between these points. This is impossible. An affine change of variable proves (2.2).

Apply (2.2) to \(f(t)=\prod_j(t-|z_j|)\) on
\([a,1]\), where \(a=\ell/(\ell+N)\). Some \(r\in[a,1]\) satisfies
\[
r^\ell\prod_j|r-|z_j||
\ge2e^{-N}\left(\frac{N}{4(\ell+N)}\right)^N.
\tag{2.3}
\]
Here \(a^\ell=(1+N/\ell)^{-\ell}\ge e^{-N}\).
The product is nonzero and \(|z_1|=1\), so \(r<1\).
Order the \(z_j\) by decreasing modulus and let \(J\ge1\) be the number outside the circle \(|z|=r\).

Choose a polynomial \(P(z)=\sum_{h=0}^{N-1}b_hz^h\) with
\[
P(z_j)=z_j^{-\ell-1}\ (j\le J),
\qquad P(z_j)=0\ (j>J).
\]
Distinct-node interpolation gives existence. In the Newton basis
\(Q_h(z)=\prod_{j\le h}(z-z_j)\), write
\(P=\sum_{h=0}^{N-1}c_hQ_h\).
Contour integration, or the usual divided-difference formula, gives
\[
c_h=-\frac1{2\pi i}\int_{|z|=r}
\frac{z^{-\ell-1}}{Q_{h+1}(z)}\,dz.
\tag{2.4}
\]
For completeness, integrate \((P-z^{-\ell-1})/Q_{h+1}\) first on a circle containing all nodes. Its integral is \(c_h\), because all higher Newton terms are polynomials and all lower terms decay at infinity. Its poles outside \(|z|=r\) are removable by the interpolation conditions. Inside this circle \(P/Q_{h+1}\) has only removable singularities at the inside nodes, where \(P\) vanishes. This proves (2.4).

Each \(|r-|z_j||\le1\), so the partial denominator in (2.4) is at least the product in (2.3). Hence
\[
|c_h|\le\frac12\left(\frac{4e(\ell+N)}N\right)^N.
\]
The sum of absolute coefficients of \(Q_h\) is at most \(2^h\); thus
\[
\sum_h|b_h|
\le\frac12\left(\frac{8e(\ell+N)}N\right)^N.
\tag{2.5}
\]
On the other hand, with \(p_k=\sum_jz_j^k\),
\[
J=\sum_jz_j^{\ell+1}P(z_j)
=\sum_{h=0}^{N-1}b_hp_{\ell+1+h}.
\]
Since \(J\ge1\), (2.5) gives
\[
\max_{\ell+1\le k\le\ell+N}|p_k|
\ge2\left(\frac{N}{8e(\ell+N)}\right)^N
\ge2(16e)^{-\ell}.
\]
The last inequality follows because
\(\log(8e(1+y))/y\) decreases for \(y\ge1\), and take \(y=\ell/N\).
For repeated nodes, approximate by distinct nodes of maximum modulus one and pass to a subsequence with the same \(k\) in this finite range. Rescale by \(R\). Finally \(16e<50\) and \(k\ge\ell\), giving the second inequality in (2.1). \(\square\)

## 3. Local zeros and derivatives

**Lemma 3.1.** If a character has modulus at most \(T^2\), \(|v|\le T+2\), and \(H^{-1}\le\lambda\le2\), then
\[
\#\{\rho:|\rho-1-iv|\le\lambda\}\ll\lambda H.
\tag{3.1}
\]
The zeros in this formula belong to its primitive factor.

**Proof.** At \(s=1+\lambda+iv\), each counted zero contributes at least
\(1/(5\lambda)\) to \(\Re(1/(s-\rho))\): its real displacement is between \(\lambda\) and \(2\lambda\), and its imaginary displacement has magnitude at most \(\lambda\).
The positive-kernel identity in Lemma 1.1 of *Zero-free regions and the exceptional zero*, together with
\[
|L'/L(1+\lambda+iv,\chi)|
\le-\zeta'/\zeta(1+\lambda)\ll1+\lambda^{-1},
\]
bounds the kernel sum by \(O(H+\lambda^{-1})\). The principal pole obeys the same \(O(\lambda^{-1})\) bound. The result is
\(O(\lambda H+1)=O(\lambda H)\). \(\square\)

For a real exceptional character, we also need
\[
\frac{L'}L(1,\chi_1)=\frac1\delta+O(\log(2d_1)).
\tag{3.2}
\]
Here is a derivation with its uniformity exposed. Set \(h=a_1/\log(2d_1)\), where \(a_1>0\) is a sufficiently small effective constant. Every other zero has
\(|1-\rho|\ge a_2/\log(2d_1)\), by the classical region and simplicity of the exception.
At \(s=1+h\) the Euler series bounds \(L'/L\) by \(O(h^{-1})\), and \(1/(s-\beta_1)\le h^{-1}\).
Subtract the Hadamard logarithmic derivatives at \(1\) and \(1+h\), after removing \(\beta_1\).
For every remaining zero,
\[
\left|\frac1{1-\rho}-\frac1{1+h-\rho}\right|
\le C\frac{h}{|1+h-\rho|^2}
\le C\Re\frac1{1+h-\rho}.
\]
The first comparison uses \(|1+h-\rho|\le(1+a_1/a_2)|1-\rho|\); the second uses \(\Re(1+h-\rho)\ge h\).
The positive-kernel identity bounds the sum by \(O(\log(2d_1))\). The gamma terms are bounded as well. This proves (3.2).

We will use a derivative consequence of the same local expansion. Fix a sufficiently small effective \(r_0>0\). Suppose
\[
H^{-1}\le r\le r_0,\quad
w=1+iv,\quad s_0=w+r,
\]
and a nonexceptional zero \(\rho_0\) of \(L(s,\chi)\) satisfies
\(|\rho_0-w|\le r\), with primitive conductor at most \(T\).
Define
\[
f(s)=\frac{L'}L(s,\chi)
+E\frac{L'}L(s+\delta,\chi\chi_1).
\tag{3.3}
\]
The product character is interpreted at the least common multiple of the moduli, at most \(T^2\); its finite Euler factors are retained.
For \(\chi=\chi_1\), the zero pole at \(s=\beta_1\) cancels the shifted principal pole at \(s=1-\delta\).
For principal \(\chi\), the classical zeta region permits \(r_0\) to be chosen so small that a zero this close to \(1\) has \(|v|>2\); hence both relevant poles lie outside the local disc.
There are no other principal poles in (3.3).

Set \(\lambda=200r\), decreasing \(r_0\) so that \(\lambda<1/8\).
Let \(\mathcal Z\) be the multiset of ordinary zeros \(\rho\) of the first factor and shifted zeros \(\rho'-\delta\) of the second factor with
\(|s_0-z|\le\lambda\), after the just described cancellation. Lemma 3.1 gives
\(|\mathcal Z|\ll rH\). This multiset contains \(\rho_0\).
For every integer \(h\ge1\),
\[
\frac{(-1)^hf^{(h)}(s_0)}{h!}
=\sum_{z\in\mathcal Z}(s_0-z)^{-h-1}
+O(H\lambda^{-h}).
\tag{3.4}
\]

To justify the error, start with the local expansion of Lemma 1.2 of *Zero-free regions and the exceptional zero*. In a disc about \(s_0\) of fixed radius \(1/4\), remove all zero poles lying within radius \(1/2\). The remaining holomorphic function is \(O(H)\) there: nearby omitted terms are bounded by their fixed distance, and the far-zero difference and gamma estimates are exactly those in that lemma. Cauchy's formula bounds its \(h\)-th normalized derivative by \(O(4^hH)\).
For omitted zeros at distances \(2^j\lambda<|s_0-z|\le2^{j+1}\lambda\), Lemma 3.1 gives \(O(2^j\lambda H)\) terms, so their total normalized derivative is
\[
\ll H\lambda^{-h}\sum_{j\ge0}2^{-jh}\ll H\lambda^{-h}.
\]
The shifts by \(\delta\ll H^{-1}\le r\) change only absolute constants in the count. The finite Euler factors are holomorphic on this disc and are \(O(H)\) in logarithmic derivative on a slightly larger disc. Thus their derivatives obey the same Cauchy bound. This proves (3.4).

## 4. A hybrid sieve with a logarithmic gain

**Lemma 4.1.** Suppose \(Q\ge2\), \(J\ge1\), and \(a_n=0\) whenever \(n\) has a prime factor at most \(Q\). For a finite Dirichlet polynomial \(D(t,\chi)=\sum_na_n\chi(n)n^{-it}\) and any real \(A\),
\[
\sum_{d\le Q}\log(Q/d)\sum_{\chi\bmod d}^{*}
\int_A^{A+J}|D(t,\chi)|^2\,dt
\ll\sum_n|a_n|^2(n+Q^2J).
\tag{4.1}
\]

**Proof.** First consider coefficients supported on an integer interval of span \(M\), and put \(F(\alpha)=\sum_na_ne(n\alpha)\).
All supported indices are coprime to every \(q\le Q\). The finite Gauss identity for arbitrary characters gives
\[
\sum_{\substack{a\bmod q\\(a,q)=1}}|F(a/q)|^2
=\frac1{\varphi(q)}\sum_{\chi\bmod q}|\tau(\chi)|^2
\left|\sum_na_n\chi(n)\right|^2.
\tag{4.2}
\]
If \(\chi\) is induced from \(\chi^*\) of conductor \(d\), the imprimitive Gauss formula gives
\(|\tau(\chi)|^2=d\mu^2(m)\) when \(q=dm\) and \((d,m)=1\), and zero otherwise.
Also the supported sums for \(\chi\) and \(\chi^*\) agree. Summing (4.2) over \(q\le Q\), the coefficient of each primitive squared sum is
\[
\frac d{\varphi(d)}
\sum_{\substack{m\le Q/d\\(m,d)=1}}\frac{\mu^2(m)}{\varphi(m)}
\ge\log(Q/d).
\tag{4.3}
\]

Here are the details of this lower bound, including its dependence on \(d\).
For every \(R\ge1\),
\[
\sum_{\substack{m\le R\\(m,d)=1}}\frac{\mu^2(m)}{\varphi(m)}
\ge \sum_{\substack{m\le R\\(m,d)=1}}\frac1m.
\]
Indeed, on the squarefree integer \(v=\operatorname{rad}(m)\),
\(\sum_{\operatorname{rad}(m)=v}1/m=1/\varphi(v)\); restricting \(m\le R\) can only decrease this positive sum.
Write each integer as a product of a \(d\)-smooth part and a part coprime to \(d\). Then
\[
H_{\lfloor R\rfloor}
\le\prod_{p\mid d}(1-p^{-1})^{-1}
\sum_{\substack{m\le R\\(m,d)=1}}\frac1m.
\]
Since \(H_{\lfloor R\rfloor}\ge\log R\), this proves (4.3).
The factor \(d/\varphi(d)\) cannot be dropped from this reasoning.

The sharp additive large sieve at the reduced fractions \(a/q\) bounds (4.2), summed over \(q\), by
\((M+Q^2)\sum_n|a_n|^2\). Thus the primitive character sum with weight \(\log(Q/d)\) has this same interval bound.
Apply the logarithmic-window inequality (5.2) of *The multiplicative large sieve and bilinear forms with characters*, with \(\tau=e^{1/J}\).
The interval \((y,\tau y]\) has span at most \((\tau-1)y\), and retains the rough-support condition.
Interchanging its positive sum and integral, the contribution of index \(n\) is
\[
J^2\int_{n/\tau}^n\bigl(Q^2+(\tau-1)y\bigr)\frac{dy}y
\ll Q^2J+n.
\]
This proves (4.1). \(\square\)

## 5. Detecting a near-1 zero by a prime polynomial

Fix \(\sigma\), put \(r=c_2(1-\sigma)\), and take \(c_2\ge\max(2,a_0^{-1})\).
If \(N^*(\sigma,T)>0\), (1.1) implies \(r\ge H^{-1}\).
We first treat \(r\le r_0\). Choose a large absolute effective \(D\), to be increased below, and set
\[
P=T^D,\qquad U=P^{1/1000},\qquad V=P^{100}.
\tag{5.1}
\]
For a counted zero \(\rho_0=\beta_0+i\gamma_0\), and every
\(|v-\gamma_0|\le r/2\), we have
\(|\rho_0-(1+iv)|\le r\).
Thus Section 3 applies.

Choose \(\ell=\lceil r\log P\rceil\). By increasing \(D\), it satisfies
\(\ell\ge|\mathcal Z|\) and \(\ell\ge C_2rH\), with \(C_2\) large enough for the derivative error below.
Lemma 2.1 applied to the numbers \((s_0-z)^{-1}\), \(z\in\mathcal Z\), gives some \(h=k-1\) such that
\[
\ell\le h\le2\ell-1\le3r\log P,\qquad
\left|\sum_{z\in\mathcal Z}(s_0-z)^{-h-1}\right|
\ge2(100r)^{-h-1}.
\]
Here the largest modulus is at least \((2r)^{-1}\).
The error in (3.4), divided by this lower bound, is at most a constant times
\(rH\,2^{-h}\). The choice \(\ell\ge C_2rH\), with \(rH\ge1\), makes it at most \(1/2\). Hence
\[
\frac{|f^{(h)}(s_0)|}{h!}\ge(100r)^{-h-1}.
\tag{5.2}
\]
The upper bound \(3r\log P\) retains the rounding in \(\ell\); no exact unrounded identity for \(h\) is being assumed.

For \(u\ge0\), put \(\varpi_h(u)=u^he^{-u}/h!\). Absolute differentiation of the Euler series on \(\Re s_0>1\) gives
\[
\frac{r^hf^{(h)}(s_0)}{h!}
=(-1)^{h+1}\sum_{n\ge1}
\frac{\Lambda(n)\chi(n)}{n^{1+iv}}
\varpi_h(r\log n)b(n),
\quad
b(n)=1+E\chi_1(n)n^{-\delta}.
\tag{5.3}
\]
We have \(|b(n)|\le2\) and \(0\le\varpi_h(u)\le1\).
Also \(h!\ge(h/e)^h\), for example by integrating \(\log t\) from \(1\) to \(h\). Consequently
\[
\varpi_h(u)\le300^{-h}\quad(u\le h/1000),
\qquad
\varpi_h(u)\le300^{-h}e^{-u/2}\quad(u\ge20h).
\tag{5.4}
\]
For the second inequality, \(h(1+\log(u/h))-u/2\) decreases for \(u\ge2h\), and its value at \(20h\) is less than \(-h\log300\).

The indices \(n\le U\) lie in the first tail of (5.4), and \(n>V\) in the second, since \(h\le3r\log P\).
Chebyshev and partial summation bound their total by
\[
\ll300^{-h}(\log P+r^{-1}).
\]
Compared with the lower bound \(r^h(100r)^{-h-1}\) in (5.2), this is bounded by a constant times
\((r\log P+1)3^{-h}\). Since \(r\log P\ge D/2\), increasing \(D\) makes it less than \(1/4\) of that lower bound, uniformly in \(T,r\).

The proper prime powers \(U<p^j\le V\), \(j\ge2\), contribute at most
\[
2\sum_{\substack{p^j>U\\j\ge2}}\frac{\log p}{p^j}
\ll U^{-1/2}=P^{-1/2000}.
\tag{5.5}
\]
This follows by partial summation from the previously proved bound
\(\sum_{p^j\le z,j\ge2}\log p\ll\sqrt z\).
Decrease \(r_0\) so that \(3r_0\log100<1/4000\).
Then \(100^h\le P^{3r\log100}\), and (5.5) is also less than \(1/4\) of the lower bound when \(D\) is large. We obtain
\[
\left|\sum_{U<p\le V}\frac{\log p}{p^{1+iv}}
\chi(p)b(p)\varpi_h(r\log p)\right|
\gg\frac1{r100^h}.
\tag{5.6}
\]

Let
\[
F(y,v,\chi)=\sum_{U<p\le y}\frac{\log p}{p^{1+iv}}\chi(p)b(p).
\]
Partial summation turns (5.6) into a lower bound for the integral of \(|F|\).
The endpoint \(F(V,v,\chi)\varpi_h(r\log V)\) is negligible by
\(|F(V,v,\chi)|\ll\log P\) and (5.4).
Moreover,
\(\varpi_h'=\varpi_{h-1}-\varpi_h\), so \(|\varpi_h'|\le1\).
Thus
\[
\int_U^V|F(y,v,\chi)|\frac{dy}y\gg\frac1{r^2\,100^h}.
\]
Cauchy–Schwarz gives
\[
\int_U^V|F(y,v,\chi)|^2\frac{dy}y
\gg\frac1{r^4\,100^{2h}\log P}
\gg(\log P)^3P^{-C_3r}.
\tag{5.7}
\]
For the last step write \(z=r\log P\): the middle expression is at least
\((\log P)^3z^{-4}P^{-6r\log100}\).
Since \(z\ge D/2\), \(z^4\le e^z\) once \(D\) is large; take, for example, \(C_3=6\log100+1\).
This proves (5.7) for each \(v\) in an interval of length \(r\) about every counted zero, with absolute effective constants.

## 6. What the exceptional character does to the prime coefficients

When \(E=0\), \(b(p)=1\). When \(E=1\), the stronger estimate needed in (5.7) is
\[
\sum_{U<p\le V}\frac{|b(p)|^2}{p}\ll\delta\log V.
\tag{6.1}
\]
We prove it rather than assume a character prime number theorem in a power range.

For \(c(n)=(1*\chi_1)(n)\), every coefficient is nonnegative and \(c\) is multiplicative. If \(Z/\log(2Z)\) is sufficiently large compared with \(d_1\), a weighted hyperbola calculation gives
\[
A(Z):=\sum_{n\le Z}\frac{c(n)}n
=(\log Z+\gamma)L(1,\chi_1)+L'(1,\chi_1)
+O\!\left(\sqrt{\frac{d_1\log(2Z)}Z}\right).
\tag{6.2}
\]

Here is the calculation. Write \(n=ab\), and split at
\(a\le W=\sqrt{d_1Z\log(2Z)}\), taking \(W\le Z\).
The first portion is
\(\sum_{a\le W}\chi_1(a)H_{\lfloor Z/a\rfloor}/a\).
Replace the harmonic number by \(\log(Z/a)+\gamma+O(a/Z)\); the total error is \(O(W/Z)\).
The second portion is
\[
\sum_{b\le Z/W}\frac1b
\sum_{W<a\le Z/b}\frac{\chi_1(a)}a.
\]
Periodicity bounds every partial character sum by \(d_1\), so partial summation bounds this portion by
\(O(d_1\log(2Z)/W)\). Extending the first portion to \(L(1,\chi_1)\) and \(-L'(1,\chi_1)\) costs the same amount: the tails of
\(\sum\chi_1(a)/a\) and \(\sum\chi_1(a)\log a/a\) are
\(O(d_1/W)\) and \(O(d_1\log(2W)/W)\).
The choice of \(W\) proves (6.2).

By (3.2), after decreasing \(a_0\) in (1.1),
\[
A(U)\ge\frac{L(1,\chi_1)}{2\delta},
\qquad
A(UV)-A(U)\ll L(1,\chi_1)\log V.
\tag{6.3}
\]
The error terms in (6.2) are absorbed effectively: the analytic value bound gives
\(L(1,\chi_1)\gg T^{-1/2}H^{-2}\), whereas \(U=T^{D/1000}\).
Increasing \(D\) makes \(\sqrt{T\log(2U)/U}\) smaller than both
\(L(1,\chi_1)/(4\delta)\) and a fixed fraction of \(L(1,\chi_1)\log V\), uniformly for \(T\ge2\).
For the first inequality, use \(\delta\le a_0/H\); for the second, the constant \(L'\) cancels in the difference. In the main term of the first inequality,
\(L'/L=1/\delta+O(\log(2d_1))\), and the latter error is dominated by \(1/(4\delta)\).

Products \(np\), with \(n\le U<p\le V\), are distinct as \(n,p\) vary, unless both entries agree: two different primes exceeding \(U\) cannot divide an integer \(n\le U\).
They lie in \((U,UV]\), and \(c(np)=c(n)c(p)\).
Nonnegativity therefore gives
\[
A(U)\sum_{U<p\le V}\frac{1+\chi_1(p)}p
\le A(UV)-A(U).
\]
Together with (6.3), this proves
\[
\sum_{U<p\le V}\frac{1+\chi_1(p)}p\ll\delta\log V.
\tag{6.4}
\]
All these primes exceed \(d_1\), so \(\chi_1(p)=\pm1\).
If \(\chi_1(p)=1\), then \(|b(p)|^2\le4=2(1+\chi_1(p))\).
If \(\chi_1(p)=-1\), then
\[
|b(p)|^2=(1-p^{-\delta})^2\le\delta\log p,
\]
using \((1-e^{-u})^2\le u\) for \(u\ge0\).
The elementary bound \(\sum_{p\le V}\log p/p\ll\log V\), and (6.4), prove (6.1).

Thus an exceptional zero makes the prime coefficients of the combined logarithmic derivative small in mean square. This is the source of the factor \(\delta H\) in the density theorem.

## 7. Log-free density and Deuring–Heilbronn repulsion

**Theorem 7.1.** The effective bounds (1.4)–(1.5) hold.

**Proof.** Continue first with \(H^{-1}\le r\le r_0\).
Integrate (5.7) over the interval \(|v-\gamma_0|\le r/2\), of length \(r\), then sum over counted zeros and primitive characters.
For any fixed \(\chi,v\), Lemma 3.1 bounds the number of these intervals covering \(v\) by \(O(rH)\).
Cancelling \(r\) gives
\[
(\log P)^3P^{-C_3r}N^*(\sigma,T)
\ll H\int_U^V
\sum_{d\le T}\sum_\chi^*
\int_{-T-r}^{T+r}|F(y,v,\chi)|^2\,dv\,\frac{dy}y.
\tag{7.1}
\]
The time interval includes both signs of the zero ordinate.

Take \(Q=T^2\) in Lemma 4.1. For \(d\le T\),
\(\log(T^2/d)\ge\log T\asymp H\).
Choose \(D\) large enough that \(U>T^6\); every prime in \(F\) then exceeds \(Q\).
The logarithmic gain cancels the factor \(H\) in (7.1), giving
\[
\begin{aligned}
N^*(\sigma,T)
&\ll\frac{P^{C_3r}}{(\log P)^3}
\int_U^V\sum_{U<p\le y}
\frac{(\log p)^2|b(p)|^2}{p^2}(p+T^5)\frac{dy}y\\
&\ll\frac{P^{C_3r}}{(\log P)^2}
\sum_{U<p\le V}\frac{(\log p)^2|b(p)|^2}{p}.
\end{aligned}
\tag{7.2}
\]
Here the height interval has length \(O(T)\), and \(T^5/p<1\).

When \(E=0\), partial summation from Chebyshev gives
\(\sum_{p\le V}(\log p)^2/p\ll(\log V)^2\ll(\log P)^2\).
Thus (7.2) is \(O(P^{C_3r})\).
When \(E=1\), (6.1) and \(\log p\le100\log P\) make it
\(O(\delta\log P\,P^{C_3r})\).
Since \(P=T^D\) and \(r=c_2(1-\sigma)\), both desired estimates follow in this near-1 range, with exponent \(c=DC_3c_2\), or any larger one.

It remains to cover \(r>r_0\), including bounded \(T\). The elementary zero count in the explicit-formula lesson gives at most
\[
\ll T^3H
\]
zeros for the whole primitive family: there are \(O(T^2)\) characters and \(O(TH)\) zeros per character.
Increase \(c\) until \(c r_0/c_2\ge5\).
If \(E=0\), \(T^{c(1-\sigma)}\ge T^5\) dominates this count.
If \(E=1\), (1.3) gives
\(\delta H T^{c(1-\sigma)}\gg T^{9/2}H^{-3}\), which also dominates \(T^3H\) after increasing an absolute effective constant.
If \(r<H^{-1}\), (1.1) says \(N^*=0\), so nothing remains.
Every choice of constant was made from effective local estimates, finite power-sum inequalities, the analytic value bound and explicit elementary tails. No Siegel lower constant has entered. \(\square\)

**Corollary 7.2 (Deuring–Heilbronn).** If \(E=1\), every other zero in the family with \(\beta\ge1/2\), \(|\gamma|\le T\), satisfies
\[
\beta\le1-\frac{\log(1/(C\delta H))}{c\log T}.
\tag{7.3}
\]
When the numerator is nonpositive, this is simply a vacuous bound; the classical region still applies.

**Proof.** Such a zero contributes at least one to \(N^*(\beta,T)\).
Thus \(1\le C\delta H T^{c(1-\beta)}\). Take logarithms. \(\square\)

## 8. Gallagher's effective lower bound

For a fixed modulus \(q\ge2\), let \(\delta_q=1\) if its primitive factors of conductors dividing \(q\) have no real zero
\(\beta>1-a_0/\log(2q)\).
Otherwise let \(\delta_q=1-\beta_q\) for that unique simple real zero. Decrease \(a_0\) once for all so that it is valid both here and in (1.1).

**Theorem 8.1.** There are absolute, effectively computable \(\kappa\ge4\) and \(c_*>0\) such that, for every \(q\ge2\), \((b,q)=1\), and \(x\ge q^\kappa\),
\[
\theta(x;q,b)\ge
c_*\frac{x}{\varphi(q)}
\min(1,\delta_q\log x).
\tag{8.1}
\]
Consequently the same lower bound holds for \(\psi(x;q,b)\).

**Proof.** We give the choices in an order that preserves effectiveness.
Fix \(B=10\), and choose a small effective \(h_0>0\) such that
\[
h_0\le\min(a_0B/2,1/2),
\qquad Ch_0\le e^{-2c},
\tag{8.2}
\]
where \(C,c\) are from Theorem 7.1.
Choose a large fixed \(K\ge\max(2Bc,60)\), to be increased below.
For the moment take \(x=Q^K\), \(Q\ge q\), and put \(T=Q^B\).
Apply (1.1)–(1.5) at this height \(T\), to the whole larger family of conductors up to \(T\).
Its exceptional character, when present, need not induce a character modulo \(q\).

The stable explicit formula in Theorem 5.1 of *Counting zeros and the explicit formula for \(\psi(x,\chi)\)*, and the proper-prime-power bound \(O(\sqrt x)\), give
\[
\sum_{d\le Q}\sum_\chi^*
\left|\theta(x,\chi)-\mathbf1_{\chi=\chi_0}x
+\mathbf1_{\chi=\chi_1}\frac{x^{\beta_1}}{\beta_1}\right|
\ll
\sum_{\substack{d\le Q,\ \chi\ {\rm primitive}\\
|\gamma|\le T,\ \beta\ge1/2,\ \rho\ne\beta_1}}x^\beta
+\mathcal R.
\tag{8.3}
\]
The exceptional term is included only if that character belongs to this smaller family.
There are \(O(Q^2)\) characters and \(O(TH)\) zeros per character.
For \(\beta<1/2\), the stable quotient satisfies
\[
\left|\frac{x^\rho-1}{\rho}\right|
\le\int_1^x u^{\beta-1}\,du\le\sqrt x\log x.
\]
For \(\beta\ge1/2\), replacing the quotient by \(x^\rho/\rho\) costs \(O(1)\) per zero, and \(|\rho|^{-1}\le2\).
Hence the complete remaining error in (8.3) is bounded by
\[
\mathcal R\ll K^2x
\left(Q^{2-B}+Q^{2+B-K/2}\right)\log^2(2Q).
\tag{8.4}
\]
The first term sums the \(xT^{-1}\log^2(Qx)\) errors, and the second covers all low zeros, the constant terms and the removed proper prime powers. The formula's condition \(x\ge T\) holds because \(K\ge B\).

For later passage to modulus \(q\), replacing the inducing primitive prime sums by the original character sums costs at most
\(\varphi(q)\log q\le Q\log Q\): each character differs only at primes dividing \(q\), of total weight at most \(\log q\). We include this error in \(\mathcal R\); (8.4) still holds.

To bound the zero sum, put \(M=\log x-c\log T\ge(\log x)/2\).
If the relevant zeros satisfy \(\beta\le1-w\) and
\(N(\sigma)\le C_4e_0T^{c(1-\sigma)}\), partial summation of the positive zero count gives
\[
\begin{aligned}
\sum x^\beta
&\le x^{1/2}N(1/2)
+\log x\int_{1/2}^{1-w}x^\sigma N(\sigma)\,d\sigma\\
&\le C_5e_0x e^{-Mw}.
\end{aligned}
\tag{8.5}
\]
Indeed the integral becomes
\(C_4e_0x\log x\int_w^{1/2}e^{-Mu}\,du\), and
\(\log x/M\le2\). If \(w>1/2\), there are no such zeros and the estimate is automatic.

There are two cases.

**No deep exception.** Either \(E=0\), or \(E=1\) and \(\delta H\ge h_0\).
Including the possible exceptional zero, the density is at most
\((C+1)T^{c(1-\sigma)}\), and every zero has
\[
\beta\le1-\frac{\min(a_0,h_0)}H.
\]
Since \(H=\log(2Q^B)\le(B+1)\log Q\), (8.5) bounds their sum by
\[
C_6x\exp\!\left(-\frac{\min(a_0,h_0)K}{2(B+1)}\right).
\tag{8.6}
\]
Choose \(K\) effectively so large that this is less than \(x/8\), with the constant in (8.3) included. For \(Q\) above a computable \(Q_0(K)\), (8.4) is also less than \(x/8\).
Character orthogonality therefore gives
\(\theta(x;q,b)\ge x/(2\varphi(q))\).

**Deep exception.** Here \(E=1\) and \(\delta H<h_0\).
By (8.2) and Corollary 7.2, every other zero has
\[
\beta\le1-\frac2{\log T}.
\]
Apply (8.5) with \(e_0=\delta H\) and \(w=2/\log T\).
The zero sum in (8.3) is at most
\[
C_7\delta(\log x)x e^{-K/B}.
\tag{8.7}
\]
We used \(H\le\log x\), increasing \(K\) if needed.
Moreover, (1.3), now with \(T=Q^{10}\), and (8.4) give
\[
\mathcal R\ll K\delta(\log x)x\,Q^{-2}.
\tag{8.8}
\]
For clarity, the first error divided by \(\delta x\log x\) is
\(O(KQ^{-3}\log^5(2Q))=O(KQ^{-2})\);
the second is still smaller since \(K\ge60\).

If \(d_1\mid q\), the main term after orthogonality is
\(x-\chi_1(b)x^{\beta_1}/\beta_1\), before division by \(\varphi(q)\).
Its smallest value occurs when \(\chi_1(b)=1\). As \(\beta_1>3/4\) and \(\log x\ge4\),
\[
x-\frac{x^{\beta_1}}{\beta_1}
=\int_{\beta_1}^1
\frac{x^u(u\log x-1)}{u^2}\,du
\ge\frac12\delta(\log x)x e^{-\delta\log x}
\ge\frac12\delta(\log x)x e^{-h_0K/B}.
\tag{8.9}
\]
Increase \(K\) again until the constant in (8.7) obeys
\[
C_7e^{-K/B}\le\frac18e^{-h_0K/B}.
\]
This is possible since \(h_0\le1/2\).
Then increase the computable \(Q_0(K)\) until (8.8), with all constants included, is at most
\(\frac18\delta(\log x)x e^{-h_0K/B}\).
The error is at most half the lower bound (8.9).
This gives
\[
\theta(x;q,b)\ge\frac14e^{-h_0K/B}
\frac{\delta(\log x)x}{\varphi(q)}.
\tag{8.10}
\]
This deep zero, if \(d_1\mid q\), is exactly the one defining \(\delta_q\):
\(\delta<h_0/H\le a_0/\log(2q)\) by (8.2).

If \(d_1\nmid q\), no exceptional main term occurs at all.
The same error bound is at most
\(\frac14x(h_0K/B)e^{-h_0K/B}\le x/(4e)\).
Thus \(\theta(x;q,b)\ge x/(2\varphi(q))\) also in this case.
Both cases prove (8.1), with
\[
c_*=\min\left(\frac12,\frac14e^{-h_0K/B}\right),
\]
whenever \(Q=x^{1/K}\ge\max(q,Q_0(K))\).

Finally choose the absolute effective exponent
\[
\kappa\ge
\max\left(K,\frac{K\log(\max(2,Q_0(K)))}{\log2}\right).
\tag{8.11}
\]
For every \(q\ge2\), \(x\ge q^\kappa\) ensures both required inequalities for \(Q=x^{1/K}\). This proves the theorem for the full claimed range, not just one chosen value of \(x\). \(\square\)

At the no-exception stage, keeping \(Q=q\) and writing \(u=\log x/\log q\) also gives the familiar Gallagher estimate
\[
\theta(x;q,b)=\frac{x}{\varphi(q)}
\left(1+O\!\left(e^{-c_8u}+\frac{u^2}{q}\right)\right)
\tag{8.12}
\]
for \(x\ge q^{K_1}\), provided the primitive factors of conductors dividing \(q\) have no exceptional real zero within \(c_9/\log q\) of \(1\).
Here \(K_1,c_8,c_9\) and the error constant are absolute and effective.
To verify this precise form, their other zeros have classical width at least a constant divided by \(\log q\) up to height \(q^{10}\); the possible real zero is excluded by the hypothesis. Use (8.5) with that width and \(\log x-c\log(q^{10})\ge(\log x)/2\).
The two errors in (8.4), now with \(u\) in place of \(K\), are at most
\(Cx u^2/q\) once \(K_1\ge\max(2Bc,60)\), since
\(q^{-8}\log^2(2q)\ll q^{-1}\).
The passage to inducing characters has already been included.
This is the no-exception statement; (8.1) additionally gives the effective lower bound in the exceptional case.

## 9. Linnik's theorem and effectiveness

**Theorem 9.1 (Linnik).** There is an absolute, effectively computable \(L_0\) such that
\[
p(q,b)\le q^{L_0}
\qquad(q\ge2,\ (b,q)=1).
\tag{9.1}
\]

**Proof.** Set \(x=q^\kappa\) in Theorem 8.1. Its right side is strictly positive, because \(\delta_q>0\). Hence the sum of the positive weights \(\log p\) in this progression is nonzero, so at least one prime occurs below \(x\). We may take \(L_0=\kappa\). \(\square\)

The passage from a theorem for prime powers alone needs a little more work. Suppose only the \(\psi\) version of (8.1) is available. The effective bound (1.3), with conductor at most \(q\), gives
\[
\min(1,\delta_q\log x)\gg q^{-1/2}\log^{-3}(2q)
\qquad(x\ge q^\kappa).
\]
Since \(\varphi(q)\le q\), the lower bound for \(\psi\) is
\(\gg xq^{-3/2}\log^{-3}(2q)\).
Subtracting the global \(O(\sqrt x)\) contribution of proper prime powers is sufficient at \(x=q^L\) for every fixed
\[
L>\max(\kappa,3).
\tag{9.2}
\]
For instance start with \(L=\max(\kappa,4)\), and enlarge it effectively to cover a finite, effectively bounded set of small moduli. This explains the extra exponent condition when one starts from \(\psi\).

All constants in this proof are effective. If a proof first inserted Siegel's lower bound with an unspecified ineffective constant, its finite cutoff could not be computed. Here the exceptionally small factor is retained in the error as well as in the main term, and the elementary effective lower bound is enough for the remaining truncation errors.

## 10. The sharper conditional scale under GRH

**Theorem 10.1.** Under GRH for the relevant Dirichlet L-functions,
\[
p(q,b)\ll\bigl(\varphi(q)\log(2q)\bigr)^2
\qquad(q\ge2,\ (b,q)=1).
\tag{10.1}
\]
In particular \(p(q,b)\ll_\varepsilon q^{2+\varepsilon}\) for every \(\varepsilon>0\).

**Proof.** A smooth weight saves one logarithm from the unsmoothed character estimate. For a primitive character, put
\[
\Psi_1(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n)(1-n/x).
\]
The Mellin identity for \((1-u)_+\), proved by taking the two residues at \(s=0,-1\), gives
\[
\Psi_1(x,\chi)=\frac1{2\pi i}\int_{(c)}
-\frac{L'}L(s,\chi)\frac{x^s}{s(s+1)}\,ds
\qquad(c>1).
\tag{10.2}
\]
Interchange with the absolutely convergent Euler series to obtain this identity.
Shift to \(\Re s=-1/2\) at the good heights used in the explicit-formula proof. On the horizontal edges \(L'/L=O(\log^2(qT))\) and the kernel is \(O(T^{-2})\), so they tend to zero for fixed \(x\).
On the left line the functional equation and its gamma derivative give
\(L'/L=O(\log(q(|t|+2)))\): the reflected Euler logarithmic derivative is on \(\Re s=3/2\).
Thus its integral is \(O(x^{-1/2}\log(2q))\).

The pole at \(1\), when present, has residue \(x/2\).
Each nontrivial zero contributes
\(-x^\rho/[\rho(\rho+1)]\).
For an odd nonprincipal character the origin contributes \(-L'/L(0,\chi)\); for an even nonprincipal character it contributes
\(-\log x+1-b(\chi)\), with \(b\) as in the explicit-formula lesson.
Under GRH both constants at the origin are \(O(\log(2q))\).
Indeed, at \(s=1\) every zero in the local logarithmic-derivative expansion has distance at least \(1/2\), so \(L'/L(1,\bar\chi)=O(\log(2q))\). The functional equation then gives the stated bound at \(0\), with the simple even zero removed. The conductor-one zeta origin constant is a fixed absolute constant.
Consequently
\[
\Psi_1(x,\chi)=\mathbf1_{\chi=\chi_0}\frac x2
-\sum_\rho\frac{x^\rho}{\rho(\rho+1)}
+O(\log(2qx)).
\tag{10.3}
\]
The zero series converges absolutely under GRH.
The local zero count gives
\[
\sum_\rho\frac1{|\rho(\rho+1)|}\ll\log(2q):
\]
for \(|\gamma|\le1\) the denominators are bounded below, and on successive unit intervals the sum is bounded by
\(\sum_{j\ge1}\log(q(j+2))/j^2\ll\log(2q)\).
Hence
\[
\Psi_1(x,\chi)=\mathbf1_{\chi=\chi_0}\frac x2
+O\!\left(\sqrt x\log(2q)+\log(2qx)\right).
\tag{10.4}
\]

For an imprimitive character, omitting prime powers at primes dividing \(q\) costs at most
\(\omega(q)\log x\ll\log(2q)\log(2x)\).
Average (10.4) by orthogonality to obtain
\[
\sum_{\substack{n\le x\\n\equiv b\pmod q}}\Lambda(n)(1-n/x)
=\frac{x}{2\varphi(q)}
+O\!\left(\sqrt x\log(2q)+\log(2q)\log(2x)\right).
\tag{10.5}
\]
Subtract the proper-prime-power weights, whose total is \(O(\sqrt x)\).
Choose \(x=A(\varphi(q)\log(2q))^2\), with one sufficiently large absolute \(A\).
Since \(\log(2x)\ll\log A+\log(2q)\), the main term exceeds the two error terms uniformly in \(q\) when \(A\) is large: its size is
\(A\varphi(q)\log^2(2q)/2\), while the square-root term is \(O(\sqrt A\varphi(q)\log^2(2q))\), and the last term is \(O((1+\log A)\log^2(2q))\).
The weighted prime sum is therefore positive, proving (10.1).
Finally \(\varphi(q)\le q\) and \(\log^2(2q)\ll_\varepsilon q^\varepsilon\). \(\square\)

## 11. Least-prime examples and the necessary size of an exponent

For the class \(1\bmod q\), trial division gives the following complete list through \(q=50\). Every displayed prime has been checked, and all smaller positive integers in its progression have been checked composite.
The entry for \(q=1\) is included as an arithmetic convention; Theorem 9.1 starts at \(q=2\).

| \(q\) | \(p(q,1)\) | \(q^2\) |
|---:|---:|---:|
| \(1\) | \(2\) | \(1\) |
| \(2\) | \(3\) | \(4\) |
| \(3\) | \(7\) | \(9\) |
| \(4\) | \(5\) | \(16\) |
| \(5\) | \(11\) | \(25\) |
| \(6\) | \(7\) | \(36\) |
| \(7\) | \(29\) | \(49\) |
| \(8\) | \(17\) | \(64\) |
| \(9\) | \(19\) | \(81\) |
| \(10\) | \(11\) | \(100\) |
| \(11\) | \(23\) | \(121\) |
| \(12\) | \(13\) | \(144\) |
| \(13\) | \(53\) | \(169\) |
| \(14\) | \(29\) | \(196\) |
| \(15\) | \(31\) | \(225\) |
| \(16\) | \(17\) | \(256\) |
| \(17\) | \(103\) | \(289\) |
| \(18\) | \(19\) | \(324\) |
| \(19\) | \(191\) | \(361\) |
| \(20\) | \(41\) | \(400\) |
| \(21\) | \(43\) | \(441\) |
| \(22\) | \(23\) | \(484\) |
| \(23\) | \(47\) | \(529\) |
| \(24\) | \(73\) | \(576\) |
| \(25\) | \(101\) | \(625\) |
| \(26\) | \(53\) | \(676\) |
| \(27\) | \(109\) | \(729\) |
| \(28\) | \(29\) | \(784\) |
| \(29\) | \(59\) | \(841\) |
| \(30\) | \(31\) | \(900\) |
| \(31\) | \(311\) | \(961\) |
| \(32\) | \(97\) | \(1024\) |
| \(33\) | \(67\) | \(1089\) |
| \(34\) | \(103\) | \(1156\) |
| \(35\) | \(71\) | \(1225\) |
| \(36\) | \(37\) | \(1296\) |
| \(37\) | \(149\) | \(1369\) |
| \(38\) | \(191\) | \(1444\) |
| \(39\) | \(79\) | \(1521\) |
| \(40\) | \(41\) | \(1600\) |
| \(41\) | \(83\) | \(1681\) |
| \(42\) | \(43\) | \(1764\) |
| \(43\) | \(173\) | \(1849\) |
| \(44\) | \(89\) | \(1936\) |
| \(45\) | \(181\) | \(2025\) |
| \(46\) | \(47\) | \(2116\) |
| \(47\) | \(283\) | \(2209\) |
| \(48\) | \(97\) | \(2304\) |
| \(49\) | \(197\) | \(2401\) |
| \(50\) | \(101\) | \(2500\) |

In these finite examples \(p(q,1)<q^2\) for \(2\le q\le50\), with largest ratio \(7/9\), at \(q=3\). This finite check does not prove a uniform quadratic bound.
At \(q=1\), the least prime is \(2>1^L\) for every \(L\); this explains the lower restriction \(q\ge2\) in a bound with coefficient exactly \(1\).

**Proposition 11.1.** As \(q\to\infty\),
\[
\max_{(b,q)=1}p(q,b)\ge(1+o(1))\varphi(q)\log q.
\tag{11.1}
\]
Consequently no absolute exponent \(L<1\) can satisfy (9.1).

**Proof.** Let the maximum be \(P_q\). The \(\varphi(q)\) reduced classes require distinct primes at most \(P_q\), so
\(\pi(P_q)\ge\varphi(q)\).
The totient estimate \(q/\varphi(q)\ll\log(2q)\) implies
\[
\varphi(q)\to\infty,\qquad
\log\varphi(q)=\log q+O(\log\log(2q)).
\]
By the ordinary prime number theorem, the \(n\)-th prime is
\((1+o(1))n\log n\). To verify the inversion, compare
\(\pi((1\pm\varepsilon)n\log n)\sim(1\pm\varepsilon)n\), then let \(\varepsilon\downarrow0\).
Thus
\[
P_q\ge p_{\varphi(q)}
=(1+o(1))\varphi(q)\log\varphi(q)
=(1+o(1))\varphi(q)\log q.
\]
Moreover \(\varphi(q)\log q\gg q\) by the same totient bound, so \(P_q/q^L\to\infty\) for any fixed \(L<1\). \(\square\)

Numerical refinements of Linnik's exponent require considerably sharper constants than those retained above.
For precise historical comparison, Xylouris's [2011 article](https://www.impan.pl/shop/publication/transaction/download/product/83078) states the exponent \(5.18\) in Theorem 1.1; the [2018 article *Linniks Konstante ist kleiner als 5*](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&paperid=681&what=fullt&option_lang=eng) states the exponent \(5\) in Theorem 1.
These statements use \(p(q,b)\le Cq^L\) with an effective coefficient \(C\). Absorbing \(C\) into a pure power uniformly for \(q\ge2\) changes the exponent; it does not preserve the number \(5\).
Our proof supplies an effective absolute power, with no optimization of its numerical value. The two sharper numerical analyses are further literature, not estimates used in this proof.

## 12. Exercises

1. **Medium.** Under GRH, use a smooth explicit formula to prove \(p(q,b)\ll_\varepsilon q^{2+\varepsilon}\). Explain the logarithm saved by the smooth weight.
2. **Medium.** Explain how an exceptionally small \(1-\beta_1\) helps the other character factors, and how this compensates for the small main term in the classes with \(\chi_1(b)=1\).
3. **Medium.** Prove (11.1) and deduce that a uniform exponent smaller than \(1\) is impossible.
4. **Hard.** Starting only from the \(\psi\) lower bound in Theorem 8.1, deduce Linnik's theorem and state an explicit condition on the exponent in terms of \(\kappa\). Explain how the finite small-modulus adjustment can be computed.

## 13. Solutions

1. Use the weight \((1-n/x)_+\), whose Mellin transform is \(1/[s(s+1)]\).
The contour calculation (10.2)–(10.3) has zero terms \(x^\rho/[\rho(\rho+1)]\), rather than \(x^\rho/\rho\).
On GRH the weighted reciprocal sum over all zeros is \(O(\log(2q))\), because its ordinate tail is summable like
\(\sum_j\log(q(j+2))/j^2\). Thus the averaged character error is
\(O(\sqrt x\log(2q)+\log(2q)\log(2x))\), with main term \(x/(2\varphi(q))\).
The total proper-prime-power weight is \(O(\sqrt x)\).
At \(x=A(\varphi(q)\log(2q))^2\), a sufficiently large absolute \(A\) makes the prime sum positive. Therefore
\(p(q,b)\ll(\varphi(q)\log(2q))^2\ll_\varepsilon q^{2+\varepsilon}\).
The additional kernel factor \(s+1\) makes the zero series absolutely convergent; this is the logarithmic saving compared with summing the unsmoothed absolute reciprocals.

2. If a nonexceptional zero has real part \(\beta\), then (1.5) gives
\(1\le C\delta H T^{c(1-\beta)}\), so
\(1-\beta\ge\log(1/(C\delta H))/(c\log T)\).
As \(\delta\) decreases, this forces every other near-1 zero to the left.
At the coefficient level, the two logarithmic derivatives in (3.3) have prime coefficient
\(b(p)=1+\chi_1(p)p^{-\delta}\).
The positive convolution in Section 6 gives
\(\sum|b(p)|^2/p\ll\delta\log V\); this is the quantitative mechanism.
After integration of the zero density, the error is \(O(\delta(\log x)x e^{-K/B})\), whereas the smallest class main term is at least
\(\frac12\delta(\log x)x e^{-h_0K/B}\).
Since \(h_0<1\), choosing \(K\) sufficiently large makes the error a fixed fraction of the main term, independently of how small \(\delta\) is.
For classes with \(\chi_1(b)=-1\), the exceptional term adds to the principal contribution; for those with \(\chi_1(b)=1\), it subtracts, but the same repulsion controls the error. If its conductor does not divide the modulus, there is no exceptional class term, while the repulsion still helps.

3. Each reduced class has its own least prime, and primes in different classes are distinct. Hence
\(\pi(P_q)\ge\varphi(q)\).
The ordinary prime number theorem gives
\(P_q\ge(1+o(1))\varphi(q)\log\varphi(q)\).
From \(q/\varphi(q)\ll\log(2q)\), we have
\(\log\varphi(q)/\log q\to1\), giving (11.1).
The same totient estimate makes its right side at least a fixed positive multiple of \(q\), eventually. For \(L<1\), that multiple of \(q\) exceeds \(q^L\) for all sufficiently large \(q\), so a uniform such exponent is impossible.

4. The effective exceptional distance, or \(\delta_q=1\) in its absence, gives
\[
\psi(x;q,b)\ge c_{10}xq^{-3/2}\log^{-3}(2q)
\quad(x\ge q^\kappa).
\]
Let \(C_{10}\sqrt x\) bound the total proper-prime-power contribution. At \(x=q^L\), a prime must occur once
\[
q^{L/2-3/2}\log^{-3}(2q)>C_{10}/c_{10}.
\tag{13.1}
\]
Choose first \(L_1=\max(\kappa,4)\), so \(L_1/2-3/2>0\).
The function on the left eventually increases and tends to infinity.
All constants are effective, so find a computable \(q_0\) beyond which (13.1) holds by elementary exponential-versus-polynomial bounds in \(\log q\).
For every \(2\le q<q_0\) and every unit class, enumerate integers in that progression and test primality until its first prime is found. Dirichlet's theorem proves that this finite collection of searches terminates.
If \(M\) is the largest least prime found, take
\[
L=\max\left(L_1,\frac{\log(\max(2,M))}{\log2}\right),
\]
rounded up if an integer is wanted.
For small \(q\), \(q^L\ge2^L\ge M\); for large \(q\), increasing \(L\) preserves (13.1). This proves (9.1) with a fully effective exponent.
If one uses the \(\theta\) lower bound itself, positivity already gives \(L=\kappa\), since no prime-power subtraction is then required.

## 14. Proof scope and references

The finite power-sum lemma, logarithmic-gain hybrid sieve, complete near-1 zero detector, positive-convolution prime estimate, both log-free density bounds, Deuring–Heilbronn repulsion, both cases of Gallagher's effective lower bound, Linnik's theorem, the smooth-weight GRH bound and the necessary lower scale are proved here.
The internal prerequisites in the introduction supply their previously proved exact character, analytic and sieve inputs. This argument does not use the wider Vinogradov–Korobov region or an ineffective Siegel constant.

The optimized numerical exponents reported in Section 11 are not proved here. Their exact external theorem locators are given there; they play no role in any proof above.
Koukoulopoulos's Chapter 27 gives another complete route, using sieve and multiplicative-function methods; it is a comparison reference, not an omitted step in the Gallagher route developed here.

- D. Koukoulopoulos, [*The Distribution of Prime Numbers*](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), AMS, 2019, author's preliminary version, Chapter 27, Theorems 27.1–27.2, Lemmas 27.4–27.9 and Proposition 27.8, for the alternative sieve organization.
- P. X. Gallagher, “A large sieve density estimate near \(\sigma=1\),” [*Inventiones Mathematicae* 11 (1970), 329–339](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0011/LOG_0035.pdf), for the density method and its prime-distribution consequences.
- T. Xylouris, [*On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet L-functions*](https://www.impan.pl/shop/publication/transaction/download/product/83078), *Acta Arithmetica* 150 (2011), 65–91, Theorem 1.1, for the stated numerical comparison.
- T. Xylouris, [*Linniks Konstante ist kleiner als 5*](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&paperid=681&what=fullt&option_lang=eng), *Chebyshevskii Sbornik* 19 (2018), 80–94, Theorem 1 and introduction, for the later numerical comparison.
