# Character sums: the Pólya–Vinogradov inequality

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

How many quadratic residues can occur consecutively? More generally, how far can an interval sum of a nonprincipal character depart from zero? Completing the interval into a finite Fourier sum gives a bound independent of the interval's length. A smooth weight removes the logarithm in that bound, while a mean-square calculation shows that the square root of the conductor cannot disappear. Multiplicative shifts and complete-sum moments give Burgess's short-interval estimate for cubefree conductors. Its finite-field input is developed from the programme's existing curve proofs. A quadratic stationary calculation extends the fourth moment to every conductor, giving exponent 3/16. A cubic normal form then describes the stationary classes that arise in the sixth moment; additive cubic sums and a finite rescaling argument give their full cancellation bounds for primes greater than 3. Taking the logarithm on a disc of depth four extends the phase envelope to primes 2 and 3. A critical-value lemma and an integer determinant count control the higher-power arithmetic, while a lattice count handles root coincidences at primes of exponent one. Together they assemble the sixth moment at every conductor and give the full r = 3 exponent 1/9. Finally, assuming GRH for all Dirichlet L-functions, the explicit formula controls primes with an additive phase; factoring out the largest prime then yields the uniform maximal bound with log log q.

We use the primitive Fourier identity and Gauss-sum magnitude from Gauss sums. Write

\[
S_\chi(M,N)=\sum_{M<n\le M+N}\chi(n),\qquad
e(t)=\exp(2\pi it),\qquad
\widehat f(\xi)=\int_{\mathbb R}f(x)e(-x\xi)\,dx.
\]

Here \(M\) is real, \(N\ge0\), and logarithms are natural. Rounding the two endpoints reduces a sharp interval sum to integer endpoints. Nonprincipal characters have conductor greater than 1.

## 1. Completing an interval

If \(\chi\) is primitive modulo \(q>1\), finite Fourier inversion gives

\[
S_\chi(M,N)=\frac{\tau(\chi)}q
\sum_{r=1}^{q-1}\overline{\chi(r)}
\sum_{M<n\le M+N}e(-rn/q).
\tag{1.1}
\]

There is no zero-frequency term, because \(\chi(0)=0\). Let \(\|t\|\) denote the distance from \(t\) to the nearest integer. A geometric progression of \(L\) consecutive terms satisfies, when \(t\notin\mathbb Z\),

\[
\left|\sum_{j=1}^{L}e(tj)\right|
\le\min\left\{L,\frac2{|1-e(t)|}\right\}
\le\min\left\{L,\frac1{2\|t\|}\right\}.
\tag{1.2}
\]

Indeed, its numerator has modulus at most 2, and
\(|1-e(t)|=2\sin(\pi\|t\|)\ge4\|t\|\), by concavity of sine on \([0,\pi/2]\).

**Theorem 1.1 (Pólya–Vinogradov).** Every nonprincipal character modulo \(q\) satisfies, uniformly in \(M\) and \(N\),

\[
|S_\chi(M,N)|\le 2\sqrt q(1+\log q).
\tag{1.3}
\]

For a primitive character the factor 2 may be omitted.

**Proof for primitive characters.** Use \(|\tau(\chi)|=\sqrt q\) in (1.1), and pair the frequencies \(r\) and \(q-r\). The middle frequency when \(q\) is even contributes at most 1 to the sum of the geometric-progression bounds. Thus

\[
\begin{aligned}
|S_\chi(M,N)|
&\le\frac1{\sqrt q}\sum_{r=1}^{q-1}\frac1{2\|r/q\|}\\
&\le\sqrt q\sum_{r=1}^{\lfloor q/2\rfloor}\frac1r
\le\sqrt q(1+\log q).
\end{aligned}
\tag{1.4}
\]

The last inequality follows by comparing \(\sum_{r=2}^{R}1/r\) with \(\int_1^R dt/t\). This also explains the logarithm: the Fourier transform of an interval has only reciprocal-frequency decay. \(\square\)

### The conductor reduction and its constant

Suppose \(\chi\) modulo \(q\) is induced by a primitive \(\psi\) modulo \(q^*\), and put \(h=q/q^*\). The relation between their zero values is essential:

\[
\chi(n)=\psi(n)1_{(n,h)=1}
=\psi(n)\sum_{d\mid(n,h)}\mu(d).
\]

The elementary identity in the second equality follows by multiplying \(1-1\) over the distinct primes dividing \((n,h)\). Substituting \(n=dm\) and using complete multiplicativity gives the exact interval identity

\[
S_\chi(M,N)=\sum_{d\mid h}\mu(d)\psi(d)
\sum_{M/d<m\le(M+N)/d}\psi(m).
\tag{1.5}
\]

A term with \((d,q^*)>1\) is zero. For all remaining terms use (1.4), which applies to real endpoints too. The number of divisors of \(h\) is at most \(2\sqrt h\): pair a divisor \(d>\sqrt h\) with \(h/d<\sqrt h\), and count at most \(\lfloor\sqrt h\rfloor\) small divisors. Consequently

\[
|S_\chi(M,N)|
\le 2\sqrt h\sqrt{q^*}(1+\log q^*)
\le2\sqrt q(1+\log q).
\]

This proves Theorem 1.1 in full. Retaining a factor depending on the number of divisors and then claiming that the constant is uniform would miss this last step.

For comparison, orthogonality gives \(\sum_{n=1}^q\chi(n)=0\). Removing complete periods leaves fewer than \(q\) consecutive terms, of which at most \(\varphi(q)\) are nonzero. Hence the trivial uniform bound is \(\varphi(q)\). Pólya–Vinogradov improves it when the modulus is large and its totient is not unusually small.

## 2. Smoothing and the dual length

We first prove the continuous Fourier fact required for an exact smooth formula. Suppose \(f\in C^2(\mathbb R)\) and

\[
|f^{(j)}(x)|\le C_f(1+|x|)^{-2},\qquad j=0,1,2.
\tag{2.1}
\]

Twice integrating by parts, with the boundary terms zero by (2.1), yields

\[
|\widehat f(\xi)|\le\|f\|_1,\qquad
|\widehat f(\xi)|\le\frac{\|f''\|_1}{4\pi^2\xi^2}\quad(\xi\ne0).
\tag{2.2}
\]

**Lemma 2.1 (Poisson summation with a shift).** If \(L>0\) and \(a\in\mathbb R\), then

\[
\sum_{k\in\mathbb Z}f(a+kL)
=\frac1L\sum_{m\in\mathbb Z}\widehat f(m/L)e(ma/L).
\tag{2.3}
\]

Both sums converge absolutely.

**Proof.** The periodization \(P(x)=\sum_k f(x+kL)\) and its first two derivative series converge uniformly on \([0,L]\), since their tails are bounded by a constant times \(\sum_{|k|>K}k^{-2}\). Thus \(P\) is a continuous periodic function. Its \(m\)-th Fourier coefficient, calculated by termwise integration and then the substitutions \(y=x+kL\), is

\[
\frac1L\int_0^L P(x)e(-mx/L)\,dx
=\frac1L\widehat f(m/L).
\]

By (2.2) the proposed Fourier series converges absolutely and uniformly; it defines a continuous function with these same coefficients. Their difference has all Fourier coefficients zero. The Fejér-kernel uniqueness argument proved in Section 3 of *Gauss sums* shows that a continuous periodic function with zero Fourier coefficients is zero: its Fejér means vanish and converge uniformly to it. Evaluating at \(x=a\) proves (2.3). \(\square\)

**Theorem 2.2 (character Poisson summation).** Let \(\chi\) be primitive modulo \(q\), let \(N>0\), and assume (2.1). Then

\[
\boxed{\sum_{n\in\mathbb Z}\chi(n)f(n/N)
=\frac{\tau(\chi)N}{q}
\sum_{m\in\mathbb Z}\overline{\chi(m)}
\widehat f(mN/q).}
\tag{2.4}
\]

**Proof.** Split the integers into \(n=b+qk\), with \(b\bmod q\). Apply (2.3) to \(g(x)=f(x/N)\), whose Fourier transform is \(N\widehat f(N\xi)\). This gives

\[
\begin{aligned}
\sum_n\chi(n)f(n/N)
&=\frac Nq\sum_m\widehat f(mN/q)
\sum_{b\bmod q}\chi(b)e(mb/q)\\
&=\frac{\tau(\chi)N}q\sum_m
\overline{\chi(m)}\widehat f(mN/q).
\end{aligned}
\]

The last equality is the primitive Gauss identity, including nonunit \(m\). Absolute convergence justifies every rearrangement. The positive sign in the residue-class Fourier series is responsible for the conjugate character on the right. \(\square\)

If \(q=1\), formula (2.4) is ordinary Poisson summation, including its nonzero term at \(m=0\). For \(q>1\), a primitive character is nonprincipal and that term vanishes. This distinction matters for the following estimate.

**Corollary 2.3.** Under the hypotheses of Theorem 2.2, with \(q>1\),

\[
\left|\sum_n\chi(n)f(n/N)\right|\ll_f\sqrt q
\quad\hbox{for every }N>0.
\tag{2.5}
\]

**Proof.** Put \(T=q/N\). If \(T\ge1\), split the nonzero frequencies at \(|m|=T\) in (2.2). Their absolute sum is \(O_f(T)\), because
\(T^2\sum_{m>T}m^{-2}=O(T)\). Multiplication by \(N/\sqrt q\) proves (2.5). If \(T<1\), all nonzero frequencies lie in the decay range, and their sum is \(O_f(T^2)\). The resulting bound is \(O_f(q^{3/2}/N)\le O_f(\sqrt q)\). \(\square\)

For a smooth function supported in \([0,1]\), the original sum has length \(N\) and the important dual frequencies have size at most about \(q/N\). The decay outside this range is quadratic. Thus smoothing changes the mechanism behind (1.4), replacing a harmonic series with a summable tail. The implied constant depends on the weight, including its second derivative; approximating an interval by weights with increasingly steep edges does not preserve that constant.

## 3. Quadratic residues and a necessary square root

For an odd prime \(p\), let \(\chi_p(n)=(n/p)\), and let \(n_2(p)\) be the least positive integer with \(\chi_p(n_2(p))=-1\). This least nonresidue is prime. If it factored as \(ab\) with \(1<a,b<n_2(p)<p\), both factors would have character value 1 and so would their product. Its existence and \(n_2(p)<p\) follow because half of the nonzero classes are nonresidues.

**Corollary 3.1.** For odd primes,

\[
n_2(p)\le1+\sqrt p(1+\log p)\ll\sqrt p\log p.
\tag{3.1}
\]

**Proof.** All integers \(1\le n<n_2(p)\) have character value 1. Their sum is \(n_2(p)-1\), and the primitive case of (1.3) bounds it as claimed. \(\square\)

More generally, in any interval of fewer than \(p\) consecutive integers, let \(R\) and \(U\) count residues and nonresidues among the integers not divisible by \(p\). Then \(R-U=S_{\chi_p}(M,N)\) and \(R+U\) is the number of those integers. Formula (1.4) therefore bounds the discrepancy from an equal split.

The square-root scale also has a converse. Define \(S(n)=\sum_{j=1}^n\chi(j)\), for \(0\le n\le q\). Since \(S(0)=S(q)=0\), extend \(S\) periodically to integers. Its cyclic difference is \(S(n)-S(n-1)=\chi(n)\).

**Theorem 3.2.** For every primitive character modulo \(q>1\),

\[
\max_{0\le n<q}|S(n)|\ge\frac{\sqrt q}{2\pi}.
\tag{3.2}
\]

**Proof.** Use the unnormalized finite Fourier transform
\(F(k)=\sum_{n=0}^{q-1}S(n)e(-kn/q)\). The cyclic difference identity gives

\[
(1-e(-k/q))F(k)=\sum_{n\bmod q}\chi(n)e(-kn/q).
\]

At \(k=1\) the right side has modulus \(\sqrt q\), by the primitive Gauss identity. Consequently

\[
|F(1)|=\frac{\sqrt q}{2\sin(\pi/q)}
\ge\frac{q^{3/2}}{2\pi}.
\]

Finite Parseval, obtained by expanding and summing the geometric orthogonality identity, says
\(\sum_n|S(n)|^2=q^{-1}\sum_k|F(k)|^2\). Hence

\[
\frac1q\sum_{n=0}^{q-1}|S(n)|^2
\ge\frac{|F(1)|^2}{q^2}\ge\frac q{4\pi^2}.
\]

The maximum is at least the square root of the mean square. \(\square\)

### Three exact partial-sum examples

For each prime below, the displayed list is \((S(0),S(1),\ldots,S(p))\), computed by marking the nonzero squares modulo \(p\).

\[
\begin{aligned}
p=7:\quad& (0,1,2,1,2,1,0,0),\\
p=11:\quad& (0,1,0,1,2,3,2,1,0,1,0,0),\\
p=23:\quad& (0,1,2,3,4,3,4,3,4,5,4,3,4,\\
&\hspace{22mm}5,4,3,4,3,4,3,2,1,0,0).
\end{aligned}
\tag{3.3}
\]

Their maxima are respectively \(2,3,5\). The values \(\sqrt p\log p\) are approximately \(5.148,7.953,15.037\), so these examples are well below the uniform bound. Their least nonresidues are \(3,2,5\). A numerical sample does not decide whether the logarithm can be removed uniformly; the later large-sum construction addresses that question.

![Exact partial sums of the Legendre characters at primes 7, 11 and 23, with integer endpoints, maxima and least nonresidues labelled.](assets/character-partial-sums.png)

*Every point is an exact integer from (3.3); the horizontal segments indicate the same sum between consecutive integer endpoints. The displayed \(\sqrt p\log p\) values are numerical comparison scales. The proved upper bound is \(\sqrt p(1+\log p)\) in (1.4), and the universal lower bound is a statement about the maximum in (3.2). Original diagram; no source figure copied.*

## 4. A smooth-number argument for the least nonresidue

Vinogradov's argument improves (3.1) by exploiting multiplicativity, without improving the interval estimate itself. We need only an elementary consequence of the weighted Mertens theorem proved earlier.

**Lemma 4.1.** There is a constant \(C\) such that, for real \(x\ge3\),

\[
\sum_{\ell\le x\atop\ell\text{ prime}}\frac1\ell
=\log\log x+C+O(1/\log x).
\tag{4.1}
\]

**Proof.** Theorem 4.2 of Dirichlet's theorem on primes in arithmetic progressions, with \(q=1\), gives
\(A(t)=\sum_{\ell\le t}(\log\ell)/\ell=\log t+E(t)\), with \(E(t)=O(1)\) for \(t\ge2\). Partial summation, including the first prime at 2, yields

\[
\sum_{\ell\le x}\frac1\ell
=\frac{A(x)}{\log x}+\int_2^x\frac{A(t)}{t\log^2t}\,dt.
\]

The main terms give \(1+\log\log x-\log\log2\). The integral of \(E(t)/(t\log^2t)\) converges absolutely as its upper limit tends to infinity. Its tail and \(E(x)/\log x\) are both \(O(1/\log x)\). Combining the fixed terms proves the lemma. \(\square\)

**Theorem 4.2 (Vinogradov).** For every \(\varepsilon>0\),

\[
n_2(p)\ll_\varepsilon p^{1/(2\sqrt e)+\varepsilon}
\quad(p\text{ an odd prime}).
\tag{4.2}
\]

**Proof.** It suffices to consider \(0<\varepsilon<1/2-1/(2\sqrt e)\), since a smaller positive exponent bound implies every larger one. Put

\[
\beta=\frac1{2\sqrt e}+\varepsilon<\frac12.
\]

Choose a fixed \(\delta>0\), small enough that \(\alpha=1/2+\delta<1\) and \(\alpha/\beta<\sqrt e\). Let \(x=\lfloor p^\alpha\rfloor\) and \(y=p^\beta\). Suppose \(n_2(p)>y\). Every prime at most \(y\) is then a quadratic residue. Every \(y\)-smooth integer, meaning an integer all of whose prime factors are at most \(y\), has character value 1.

An integer \(n\le x\) that is not \(y\)-smooth is divisible by a prime \(\ell\) in \((y,x]\). Counting this union by the sum of the individual counts gives

\[
\#\{n\le x:n\text{ not }y\text{-smooth}\}
\le\sum_{y<\ell\le x}\left\lfloor\frac x\ell\right\rfloor
\le x\sum_{y<\ell\le x}\frac1\ell.
\tag{4.3}
\]

As \(x<p\), all the character values under consideration are \(1\) or \(-1\), never zero. Even if every nonsmooth integer contributed \(-1\), (4.1) and (4.3) would give

\[
\begin{aligned}
\sum_{n\le x}\chi_p(n)
&\ge x\left(1-2\sum_{y<\ell\le x}\frac1\ell\right)\\
&=x\left(1-2\log\frac{\log x}{\log y}
+O_\varepsilon(1/\log p)\right)\\
&=x\left(1-2\log(\alpha/\beta)+o(1)\right).
\end{aligned}
\tag{4.4}
\]

Our choice of \(\delta\) makes the limiting coefficient positive, because \(2\log\sqrt e=1\). The right side is therefore at least \(c_\varepsilon x\) for all sufficiently large \(p\). Pólya–Vinogradov, however, bounds its absolute value by \(\sqrt p(1+\log p)=o(x)\), since \(\alpha>1/2\). This contradiction proves \(n_2(p)\le p^\beta\) for all sufficiently large primes; enlarge the implied constant to include the remaining finitely many. \(\square\)

The value \(\sqrt e\) arises from a precise threshold: the union bound still forces a positive character average while \(\log x/\log y<\sqrt e\). No asymptotic formula for the count of smooth numbers is required here.

## 5. Beyond completion

The square-root lower bound (3.2) holds for every primitive character. There are also characters whose partial sums gain an unbounded factor. We first give that construction, using one precisely identified later theorem of this course: *The least prime in a progression: Linnik's theorem* proves that an absolute constant \(L\) satisfies \(p(Q,b)\le Q^L\) for every \(Q\ge2\) and every reduced class \(b\). The construction below uses The least prime in a progression: Linnik's theorem, Theorem 9.1, whereas none of the earlier arguments in this lesson does. That proof is written and publicly available; it uses the elementary Pólya–Vinogradov bound, not this construction.

### Large partial sums for real characters

**Theorem 5.1 (Paley's lower-bound scale).** Infinitely many primes \(q\equiv1\pmod4\) have

\[
\max_N\left|\sum_{n\le N}\left(\frac nq\right)\right|
\gg\sqrt q\log\log q.
\tag{5.1}
\]

In particular, these are primitive real characters with positive fundamental discriminant. We prove (5.1) from the later least-prime theorem just specified.

**Proof.** Let \(y>8\), put

\[
Q=4\prod_{3\le\ell\le y\atop\ell\text{ prime}}\ell,
\]

and use the Chinese remainder theorem to choose a reduced class \(b\bmod Q\) with

\[
b\equiv1\pmod4,\qquad b\equiv-1\pmod\ell
\quad(3\le\ell\le y).
\]

The least-prime theorem supplies a prime \(q\equiv b\pmod Q\), with \(q\le Q^L\). It has \(q>y\), because any odd prime at most \(y\) divides \(Q\), whereas \(q\) is coprime to \(Q\); also \(q\ne2\). For \(\chi(n)=(n/q)\), quadratic reciprocity and \(q\equiv1\pmod4\) give

\[
\chi(\ell)=\left(\frac q\ell\right)
=\left(\frac{-1}\ell\right)=\chi_{-4}(\ell)
\quad(3\le\ell\le y).
\]

Thus \(\chi(n)=\chi_{-4}(n)\) for every odd \(n\le y\), by multiplicativity. No condition on \(\chi(2)\) is needed.

Define the periodic step function
\(F(t)=\sum_{1\le n\le qt}\chi(n)\) for \(0\le t<1\), and put \(M=\max_{0\le n<q}|S(n)|\). Its mean is zero. Indeed,
\(\int_0^1F(t)\,dt=-q^{-1}\sum_{n=1}^{q-1}n\chi(n)\), and pairing \(n\) with \(q-n\) gives
\(\sum n\chi(n)=(q/2)\sum\chi(n)=0\), since \(\chi\) is even.

For a nonzero integer \(m\), integration of each step gives its Fourier coefficient

\[
\begin{aligned}
c_m
&=\sum_{n=1}^{q-1}\chi(n)\int_{n/q}^1e(-mt)\,dt\\
&=\frac1{2\pi im}\sum_{n\bmod q}\chi(n)e(-mn/q)
=\frac{\tau(\chi)\chi(m)}{2\pi im}.
\end{aligned}
\tag{5.2}
\]

Here \(\chi(-1)=1\) and \(\tau(\chi)=\sqrt q\), including its sign, by *Gauss sums*. Pairing positive and negative frequencies gives a sine series. Average it over \([1/4-h,1/4+h]\), with \(h=1/y\), to obtain

\[
\frac1{2h}\int_{1/4-h}^{1/4+h}F(t)\,dt
=\frac{\sqrt q}\pi\sum_{m\ge1}
\frac{\chi(m)\sin(\pi m/2)}m
\operatorname{sinc}(2\pi m/y),
\tag{5.3}
\]

where \(\operatorname{sinc}(u)=\sin(u)/u\) for \(u\ne0\), and its value at zero is 1. To justify this identity without pointwise convergence at jumps, take Fejér means first. They converge at every continuity point of \(F\), stay bounded by \(M\), and hence converge in the displayed integral by dominated convergence. Their integrated coefficients converge to the right side, an absolutely convergent series: (5.2) and \(|\operatorname{sinc}(2\pi m/y)|\le y/(2\pi m)\) bound its terms by a constant times \(\sqrt q\,y/m^2\). This proves (5.3).

For \(m\le y\), the numerator \(\chi(m)\sin(\pi m/2)\) is 1 when \(m\) is odd and zero when it is even. Since \(|\operatorname{sinc}(u)-1|\le u^2/6\),

\[
\sum_{m\le y}\frac{\chi(m)\sin(\pi m/2)}m
\operatorname{sinc}(2\pi m/y)
=\sum_{m\le y\atop m\text{ odd}}\frac1m+O(1)
=\frac12\log y+O(1).
\]

The last harmonic estimate follows by subtracting half the harmonic sum up to \(y/2\) from the sum up to \(y\). The tail in (5.3) is \(O(y\sum_{m>y}m^{-2})=O(1)\). Its left side has modulus at most \(M\), so

\[
M\ge\frac{\sqrt q}{2\pi}\log y-O(\sqrt q).
\tag{5.4}
\]

Finally, the elementary Chebyshev upper bound proved in *Dirichlet's theorem on primes in arithmetic progressions* gives
\(\log Q\le C y\). Therefore \(\log q\le CLy\), and
\(\log y\ge\log\log q-O_L(1)\). The primes obtained as \(y\to\infty\) are unbounded because \(q>y\). Formula (5.4) proves (5.1). \(\square\)

### Short intervals

The large sieve inequality, Section 10, proves the following distinct statement, also due to Linnik: for every fixed \(\delta>0\),

\[
\#\{p\le x:p\text{ odd prime},\ n_2(p)>p^\delta\}
\ll_\delta\log\log x\qquad(x\ge3).
\tag{5.5}
\]

This is a bound for the number of exceptional primes, rather than an interval estimate for each character. Its provider is that later lesson's arithmetic large sieve and smooth-number argument; its proof is written and publicly available, and is not used here.

We now turn to bounds for an individual short interval.

### Complete sums and the curve prerequisite

Short-interval estimates use cancellation in complete sums of products of shifted characters. The following form keeps its constant independent of the order of the character.

We use three existing lessons of the programme. Cycle classes and the Lefschetz fixed-point formula for curves, Theorem 4.1 and Corollary 5.1, give the fixed-point formula and identify the curve zeta numerator with Frobenius on first cohomology. The trace formula for curves, Theorem 1.1 and Section 6, give the compact-support trace formula and the Kummer character convention. Weil's proof for curves and what is missing over the integers, Theorem 3.12, proves that the Frobenius eigenvalues on a smooth projective curve have absolute value \(\sqrt p\). These are written prerequisite proofs. The geometric calculation below explains their exact application; it does not assume a general bound for character sums.

**Lemma 5.2 (Weil's complete character bound).** Let \(p\) be prime and let \(\chi\) be a nontrivial character of \(\mathbf F_p^\times\), of order \(m\). Let \(f\in\mathbf F_p(X)^\times\). Choose a finite set \(B\subset\mathbf P^1(\overline{\mathbf F}_p)\), stable under Frobenius, containing infinity and every zero or pole of \(f\), and write \(s=\#B\). Suppose that \(f\) is not a constant times an \(m\)-th power over \(\overline{\mathbf F}_p(X)\). Then

\[
\left|\sum_{x\in\mathbf F_p\setminus B}\chi(f(x))\right|
\le(s-2)\sqrt p.
\tag{5.6}
\]

In particular, for a polynomial with \(d\) distinct geometric roots, the bound is \((d-1)\sqrt p\), with \(\chi(0)=0\). In a product of shifted characters, cancelled roots must still belong to \(B\) if a factor at that root was originally zero.

**Proof.** Factor the divisor of \(f\). Put
\(a=\gcd(m,\operatorname{ord}_b f:b\in\mathbf P^1)\), and \(h=m/a>1\). Factoring into monic irreducible polynomials over \(\mathbf F_p\) gives \(f=cg^a\), with \(c\in\mathbf F_p^\times\), \(g\in\mathbf F_p(X)^\times\), and
\(\gcd(h,\operatorname{ord}_b g:b\in\mathbf P^1)=1\). Thus \(\chi(f(x))=\chi(c)\psi(g(x))\), where \(\psi=\chi^a\) has order \(h\). The constant has absolute value one. We may replace \(f,\chi,m\) by \(g,\psi,h\), so that this greatest common divisor is one.

Let \(U=\mathbf P^1-B\). The equation \(y^h=g(x)\) defines a finite étale \(G=\mu_h\)-torsor \(V\to U\), since \(h\mid p-1\). It is geometrically connected. Indeed, over \(K=\overline{\mathbf F}_p(X)\) its splitting field is \(K(y)\), as \(K\) contains \(\mu_h\). Its Galois group is a subgroup of \(\mu_h\), say of order \(e\mid h\). Then \(y^e\in K\), so \(g=(y^e)^{h/e}\). If \(e<h\), a prime dividing \(h/e\) divides every valuation of \(g\), contradicting the greatest common divisor just specified.

Let \(C\) be the smooth projective completion of \(V\), and \(D=C-V\). These objects and the deck transformations are defined over \(\mathbf F_p\). At \(b\in B\), put \(n_b=\operatorname{ord}_b g\) and
\(e_b=h/\gcd(h,n_b)\), with \(\gcd(h,0)=h\). There are \(h/e_b\) geometric points above \(b\), each with ramification index \(e_b\). To see this locally, remove the unit factor from \(g=t^{n_b}u(t)\) by taking an \(h\)-th root of \(u(t)\) in \(\overline{\mathbf F}_p[[t]]\). Its coefficients are solved successively because \(h\ne0\) in the residue field. The normalization of \(y^h=t^{n_b}\) has \(\gcd(h,n_b)\) branches, parametrized by \(t=z^{e_b}\). For negative \(n_b\), apply the same calculation to \(y^{-1}\). All ramification is tame.

For this cover the differential map
\(\pi^*\Omega_{\mathbf P^1}\to\Omega_C\) vanishes to order \(e_b-1\) at a point above \(b\): differentiate \(t=z^{e_b}\), whose leading coefficient is nonzero. Elsewhere it is invertible. Taking degrees, using \(\deg\Omega_C=2g_C-2\) and \(\deg\Omega_{\mathbf P^1}=-2\), gives the tame Riemann–Hurwitz calculation

\[
2g_C-2=-2h+\sum_{b\in B}\left(h-\frac h{e_b}\right),
\qquad \#D=\sum_{b\in B}\frac h{e_b}.
\tag{5.7}
\]

The differential argument is the special case of [Stacks, Tags 0C1D and 0C1F](https://stacks.math.columbia.edu/tag/0C1F) used here; the degree of the canonical bundle is the curve Riemann–Roch prerequisite. In particular,

\[
\chi_c(V,E)=2-2g_C-\#D=h(2-s),
\tag{5.8}
\]

where \(E/\mathbf Q_\ell\), \(\ell\ne p\), contains the character values. Here \(H_c^0(V,E)=0\), \(H_c^2(V,E)=E(-1)\), and localization gives the exact sequence

\[
0\longrightarrow E\longrightarrow E^D
\longrightarrow H_c^1(V,E)\longrightarrow H^1(C,E)
\longrightarrow0.
\tag{5.9}
\]

We also need the Euler characteristic as a \(G\)-representation. If \(t\in G\setminus\{1\}\), its fixed points on \(C\) lie in \(D\), since the action on \(V\) is free. Every such fixed point has multiplicity one. In the local parameter just constructed, a nonidentity inertia element acts by a nontrivial root of unity on \(z\), so \(z-t^*z\) has order one. The fixed-point formula therefore says that the alternating trace on \(H^*(C,E)\) is precisely the number of fixed points in \(D\). Subtract the permutation trace on \(E^D\) by (5.9). The alternating compact-support trace is zero for every \(t\ne1\), whereas its value at \(1\) is \(h(2-s)\), by (5.8). Consequently the virtual compact-support representation is
\((2-s)E[G]\): its character is \((2-s)h\) at the identity and zero elsewhere.

Write \(\psi(x)=\eta(x^{(p-1)/h})\), with \(\eta\) a faithful character of \(\mu_h\). Such \(\eta\) exists because the exponent map onto \(\mu_h\) is surjective. Character orthogonality extracts one copy from the regular representation. Since \(H_c^0=0\) and the deck action on \(H_c^2\) is trivial, the character space

\[
W=\bigl(H_c^1(V,E)\otimes E_\eta\bigr)_G
\quad\text{has dimension }s-2.
\tag{5.10}
\]

Coinvariants are exact over \(E\), because averaging by \(h^{-1}\) projects onto invariants. This is the same character construction and Frobenius convention as Section 6 of the curve trace-formula lesson. Its stalk trace at \(x\in U(\mathbf F_p)\) is \(\eta(g(x)^{(p-1)/h})=\psi(g(x))\). The trace formula thus gives

\[
\sum_{x\in U(\mathbf F_p)}\psi(g(x))
=-\operatorname{Tr}(F;W).
\tag{5.11}
\]

Finally, (5.9) puts the eigenvalues on \(H_c^1(V,E)\) among the boundary eigenvalues, which are roots of unity, and the eigenvalues on \(H^1(C,E)\), which have absolute value \(\sqrt p\). This uses the curve Riemann hypothesis and its cohomological identification stated above. Passing to a character summand introduces no new eigenvalue. The trace in (5.11) is a sum of \(s-2\) algebraic eigenvalues, counted with multiplicity, each of complex absolute value at most \(\sqrt p\). Its absolute value is at most \((s-2)\sqrt p\). Restore the unit constant \(\chi(c)\) to prove (5.6). \(\square\)

The argument separates the dimension of a single character space from the genus of the whole Kummer cover. Applying the point-count bound to that entire cover alone would introduce an unnecessary factor depending on the character's order.

### Moments at a cubefree modulus

**Lemma 5.3.** Let \(r\ge2\), let \(q\) be cubefree, and let \(\chi\) be primitive modulo \(q\). If \(b_1,\ldots,b_{2r}\) are integers and \(b_j\) occurs exactly once among them, put
\(A_j=\prod_{i\ne j}(b_i-b_j)\ne0\). Then

\[
\left|\sum_{x\bmod q}\prod_{i=1}^r\chi(x+b_i)
\prod_{i=r+1}^{2r}\overline{\chi(x+b_i)}\right|
\le(2r)^{\omega(q)}\sqrt q\,(A_j,q).
\tag{5.12}
\]

**Proof.** Split \(\chi\) into its primitive prime-power factors by the Chinese remainder theorem. Each local factor is primitive: otherwise its conductor could be reduced and so could the conductor of \(\chi\). The complete sum is the product of the local complete sums.

First suppose that \(p\mid q\) and \(p\nmid A_j\). At modulus \(p\), the rational function
\(F_1/F_2\), where \(F_1=\prod_{i\le r}(X+b_i)\) and \(F_2=\prod_{i>r}(X+b_i)\), has valuation \(1\) or \(-1\) at \(-b_j\). It cannot be a power of order equal to that of the local character. Apply Lemma 5.2 with all the original roots and infinity removed. There are at most \(2r+1\) such points, giving \((2r-1)\sqrt p\).

At modulus \(p^2\), primitivity means that the restriction to \(1+p\mathbf Z/p^2\mathbf Z\) has the form
\(\chi_p(1+pt)=e(ct/p)\), with \(c\not\equiv0\pmod p\). Indeed, this subgroup has order \(p\); triviality on it would make the character factor through modulus \(p\). This includes \(p=2\). For a residue \(a\bmod p\) at which every \(a+b_i\) is a unit, Taylor expansion modulo \(p^2\) gives

\[
\chi_p\!\left(\frac{F_1(a+pt)}{F_2(a+pt)}\right)
=\chi_p\!\left(\frac{F_1(a)}{F_2(a)}\right)
e\left(\frac{ct}{p}
\left(\frac{F_1'}{F_1}-\frac{F_2'}{F_2}\right)(a)\right).
\tag{5.13}
\]

Summing over \(t\bmod p\) gives zero unless
\(P(a)=0\), where \(P=F_1'F_2-F_1F_2'\). Its degree is at most \(2r-2\): the leading terms cancel since both products are monic of degree \(r\). It is a nonzero polynomial modulo \(p\), because its value at \(-b_j\) is the signed product of all the other differences and hence is nonzero. A nonzero polynomial over a field has at most its degree many roots, by successive division by its linear factors. The complete sum therefore has absolute value at most \((2r-2)p\). Residues at which a factor is not a unit contribute zero.

If \(p\mid A_j\), use the trivial local bound \(p^e\), for \(e=1\) or \(2\). This is at most \(p^{e/2}(A_j,p^e)\), since the greatest common divisor is at least \(p\). Combining the good and bad primes proves (5.12). \(\square\)

**Lemma 5.4 (complete moment).** For fixed \(r\ge2\) and \(\eta>0\), under the same modulus and character hypotheses, every integer \(B\ge1\) satisfies

\[
\sum_{x\bmod q}\left|\sum_{b=1}^B\chi(x+b)\right|^{2r}
\ll_{r,\eta}q^{1+\eta}B^r+q^{1/2+\eta}B^{2r}.
\tag{5.14}
\]

**Proof.** Expand the moment into \(2r\)-tuples. The tuples with at most \(r\) distinct entries number at most \(r^{2r}B^r\): choose an ordered list of \(r\) entries, allowing repetitions, and assign each of the \(2r\) positions to that list. Their total contribution is at most \(r^{2r}qB^r\). Every remaining tuple has a singleton entry, since \(r+1\) distinct entries cannot each occur twice in \(2r\) positions. Apply (5.12), allowing the sum over all possible singleton indices.

Here is the needed divisor average, with \(k=2r-1\):

\[
\sum_{1\le b_1,\ldots,b_{k+1}\le B\atop b_i\ne b_1\ (i>1)}
\left(q,\prod_{i=2}^{k+1}(b_i-b_1)\right)
\le 2^kB^{k+1}\tau_{k+1}(q).
\tag{5.15}
\]

Use \((q,a)=\sum_{d\mid(q,a)}\varphi(d)\), which follows by partitioning the integers in a cyclic group according to their order. If \(d\) divides a product of \(k\) nonzero differences, distribute each prime exponent of \(d\) among the differences. Thus some factorization \(d=d_1\cdots d_k\) has \(d_i\mid b_{i+1}-b_1\). Each \(d_i<B\). Once \(b_1\) is fixed, there are at most \(2B/d_i\) nonzero differences of the required congruence. The count for this factorization is at most \(2^kB^{k+1}/d\). Sum with weight \(\varphi(d)\le d\). The total number of factorizations over all \(d\mid q\) is \(\tau_{k+1}(q)\): append \(q/d\) as the last factor. This proves (5.15), including tuples whose nonsingleton entries repeat each other. For \(B=1\) the left side is empty.

For every fixed \(K,C,\eta>0\),

\[
C^{\omega(q)}\tau_K(q)\ll_{K,C,\eta}q^\eta.
\tag{5.16}
\]

Indeed, \(\tau_K(p^e)=\binom{e+K-1}{K-1}\le K^e\), by assigning \(e\) labelled copies of the prime to \(K\) boxes. At sufficiently large primes \(CK\le p^\eta\), so their factors satisfy the required bound. At each of the finitely many smaller primes, the polynomial growth of the binomial coefficient makes \(C\tau_K(p^e)p^{-\eta e}\) bounded uniformly in \(e\). Multiply these finitely many bounds. Apply (5.15)–(5.16) to the expanded moment to obtain (5.14). \(\square\)

### Averaging multiplicative shifts

**Lemma 5.5 (collision count).** Let \(M\) be an integer, let \(1\le A\le N\) be integers, and suppose \(AN\le q\). Let \(\mathcal A=\{1\le a\le A:(a,q)=1\}\), and define

\[
\nu(x)=\#\{(a,n):a\in\mathcal A, M<n\le M+N,
\ n\equiv ax\pmod q\}.
\]

Then

\[
\sum_{x\bmod q}\nu(x)=N\#\mathcal A,
\qquad \sum_{x\bmod q}\nu(x)^2
\le12AN(1+\log A).
\tag{5.17}
\]

**Proof.** The first identity counts each pair once, since \(a\) is invertible. The second counts pairs with
\(a_1n_2-a_2n_1=kq\). Put \(d=(a_1,a_2)\). Then \(d\mid k\), because \((d,q)=1\). Also

\[
|kq-(a_1-a_2)M|\le AN.
\]

There are at most \(2AN/(dq)+1\le3\) possible multiples \(k\) of \(d\). For a fixed \(k\), two solutions differ by an integer multiple of \((a_1/d,a_2/d)\), so the number in the interval box is at most \(Nd/\max(a_1,a_2)+1\le2Nd/\max(a_1,a_2)\). Allowing all \(a_1,a_2\le A\) only enlarges the count. Finally,

\[
\sum_{a_1,a_2\le A}\frac{(a_1,a_2)}{\max(a_1,a_2)}
\le2\sum_{b\le A}\frac1b\sum_{a\le b}(a,b)
\le2\sum_{b\le A}\tau(b)
\le2A(1+\log A).
\]

For the middle inequality use \((a,b)\le\sum_{d\mid(a,b)}d\), then count multiples of each \(d\). For the last one write \(\sum_{b\le A}\tau(b)=\sum_{d\le A}\lfloor A/d\rfloor\). Multiplying the estimates proves (5.17). The argument allows arbitrarily large or negative \(M\). \(\square\)

**Theorem 5.6 (Burgess for cubefree moduli).** Let \(\chi\) be primitive modulo a cubefree integer \(q>1\). For every integer \(r\ge1\) and every \(\varepsilon>0\), uniformly in integer \(M\) and integer \(N\ge1\),

\[
|S_\chi(M,N)|\ll_{r,\varepsilon}
N^{1-1/r}q^{(r+1)/(4r^2)+\varepsilon}.
\tag{5.18}
\]

**Proof.** For \(r=1\), Pólya–Vinogradov and \(1+\log q\ll_\varepsilon q^\varepsilon\) suffice. Fix \(r\ge2\) and put \(\alpha=(r+1)/(4r^2)\). It is enough to prove the assertion with a smaller positive \(\varepsilon\), so suppose \(\varepsilon<(r-1)/(100r^2)\). Choose \(0<\eta<\min(\varepsilon/10,(r-1)/(100r))\). All constants below may depend on \(r,\eta\).

If \(N\le q^{(r+1)/(4r)}\), the trivial bound \(N\) is at most \(N^{1-1/r}q^\alpha\). If \(N\ge q^{1/2+1/(4r)}\), Pólya–Vinogradov is at most a constant times \(N^{1-1/r}q^{\alpha+\varepsilon}\), since the product of the powers at the lower endpoint is exactly \(q^{1/2}\). These observations also cover intervals longer than a period. For bounded \(q\), increase the constant and use the trivial bound in the remaining finite range of \(N\). We can therefore assume that \(q\) is sufficiently large and

\[
q^{(r+1)/(4r)}<N<q^{1/2+1/(4r)}.
\tag{5.19}
\]

We use strong induction on \(N\), simultaneously for every starting point \(M\), with target \(C N^{1-1/r}q^{\alpha+\varepsilon}\). Choose
\(B=\lceil q^{1/(2r)}\rceil\), \(\theta=1/64\), and
\(A=\lfloor\theta N/B\rfloor\). For sufficiently large \(q\), (5.19) gives

\[
A\asymp_r N/B,\quad A\le N,\quad AN\le q,
\quad \#\mathcal A\gg_{r,\eta}Aq^{-\eta}.
\tag{5.20}
\]

Here is a proof of the last assertion, so that no density of small units is assumed. Inclusion–exclusion gives
\(\#\mathcal A=A\varphi(q)/q+O(2^{\omega(q)})\). Also
\(q/\varphi(q)=\prod_{p\mid q}(1-1/p)^{-1}\le2^{\omega(q)}\). Formula (5.16), with exponent \(\eta\), bounds both reciprocal density and the error by a constant times \(q^\eta\). Moreover \(A\gg_r q^{(r-1)/(4r)}\), and \(2\eta<(r-1)/(4r)\), so the main term dominates the error. The first assertions in (5.20) follow from (5.19) and \(B\ge q^{1/(2r)}\).

For \(a\in\mathcal A\), \(1\le b\le B\), the shift \(h=ab\le\theta N<N\) changes the interval sum by two sums of length \(h\). The induction hypothesis bounds their total by
\(2C(\theta N)^{1-1/r}q^{\alpha+\varepsilon}\), at most one quarter of the target. Average the shifted sums and use
\(\chi(n+ab)=\chi(a)\chi(a^{-1}n+b)\). With \(T(x)=\sum_{b\le B}\chi(x+b)\), this gives

\[
|S_\chi(M,N)|
\le\frac1{B\#\mathcal A}\sum_{x\bmod q}\nu(x)|T(x)|
+\frac C4N^{1-1/r}q^{\alpha+\varepsilon}.
\tag{5.21}
\]

Hölder, first against \(|T|^{2r}\) and then interpolating \(\nu\) between its first and second moments, gives

\[
\sum_x\nu(x)|T(x)|
\le\left(\sum_x\nu(x)\right)^{1-1/r}
\left(\sum_x\nu(x)^2\right)^{1/(2r)}
\left(\sum_x|T(x)|^{2r}\right)^{1/(2r)}.
\tag{5.22}
\]

For completeness, apply Hölder to
\(\nu^{1-1/r}\nu^{1/r}|T|\), with exponents \(r/(r-1),2r,2r\); their reciprocals sum to one. Lemmas 5.4–5.5 and \(B\asymp_r q^{1/(2r)}\) now bound the first term of (5.21) by

\[
\begin{aligned}
&\ll_{r,\eta}
N^{1-1/(2r)}A^{1/(2r)}(\#\mathcal A)^{-1/r}
B^{-1}q^{3/(4r)+\eta/(2r)}(1+\log A)^{1/(2r)}\\
&\ll_{r,\eta}
N^{1-1/r}q^{(r+1)/(4r^2)+3\eta/(2r)}
(1+\log q)^{1/(2r)}
\ll_{r,\varepsilon}N^{1-1/r}q^{\alpha+\varepsilon}.
\end{aligned}
\tag{5.23}
\]

The first line uses \(q^{1+\eta}B^r+q^{1/2+\eta}B^{2r}\ll_r q^{3/2+\eta}\). The second uses (5.20) and \(A\asymp_r N/B\). The last follows from \(3\eta/(2r)<\varepsilon\), with a fixed positive margin to absorb the logarithm. Choose \(C\) at least twice the final implied constant, and large enough for the initial ranges. Equation (5.21) is then at most three quarters of the induction target. This closes the induction and proves (5.18). \(\square\)

For every fixed \(\delta>0\), choosing \(r\) large enough makes this estimate \(o(N)\) whenever \(N\ge q^{1/4+\delta}\). At a prime modulus, combining it with the smooth-number argument of Section 4 gives

\[
n_2(p)\ll_\varepsilon p^{1/(4\sqrt e)+\varepsilon}.
\tag{5.24}
\]

Indeed, choose \(\beta=1/(4\sqrt e)+\varepsilon\) and a fixed \(\alpha_0>1/4\) with \(\alpha_0/\beta<\sqrt e\). If every prime at most \(p^\beta\) were a residue, (4.3)–(4.4) would force a positive fixed proportion of \(x=\lfloor p^{\alpha_0}\rfloor\) in its character sum. Choose \(r\) so large that \(\alpha_0>(r+1)/(4r)\), and then choose the exponent loss in (5.18) small enough. That estimate is \(o(x)\), giving the contradiction. If the desired \(\varepsilon\) is large, use a smaller positive one first.

The cubefree hypothesis in this proof concerns complete sums at prime powers. It cannot be removed by the Chinese remainder theorem alone. The general-modulus case with \(r=2\) follows from the additional prime-power argument below. The \(r=3\) case requires further support.

### The fourth moment at an arbitrary modulus

The preceding proof extends to \(r=2\) at every conductor. The new issue is a complete sum at \(p^e\) with \(e\ge3\). Its stationary equation is quadratic, so we can control its repeated roots explicitly.

**Lemma 5.7 (quadratic congruences).** Let \(P(X)=uX^2+vX+w\in\mathbf Z[X]\), with nonzero discriminant \(\Delta=v^2-4uw\). For a prime \(p\) and \(k\ge1\),

\[
\#\{x\bmod p^k:P(x)\equiv0\pmod{p^k}\}
\le4p^{\min(v_p(\Delta)/2,k)}.
\tag{5.25}
\]

For odd \(p\), the constant 4 can be replaced by 2.

**Proof.** Remove the common power \(p^t\) from the coefficients. If \(t\ge k\), the trivial count \(p^k\) suffices, since \(v_p(\Delta)\ge2k\). Otherwise every root of the divided polynomial modulo \(p^{k-t}\) has \(p^t\) lifts modulo \(p^k\), and its discriminant has valuation \(v_p(\Delta)-2t\). It is enough to treat a polynomial whose coefficients are not all divisible by \(p\).

If \(p\mid u\) and \(p\nmid v\), there is at most one root modulo \(p\), and each root lifts uniquely: among \(x+jp^a\), the value modulo \(p^{a+1}\) is \(P(x)+jp^aP'(x)\), with \(P'(x)\) a unit. If both \(u,v\) are divisible by \(p\), there are no roots because \(w\) is a unit. If \(p\nmid u\) and \(p\) is odd, complete the square:
\((2ux+v)^2\equiv\Delta\pmod{p^k}\). If \(d=v_p(\Delta)<k\), a root requires \(d\) even, and dividing by \(p^d\) leaves a unit square congruence with at most two roots, each having \(p^{d/2}\) lifts. If \(d\ge k\), the roots of \(z^2\equiv0\) are the multiples of \(p^{\lceil k/2\rceil}\), at most \(p^{k/2}\).

For \(p=2\) and odd \(u\), use
\((2ux+v)^2\equiv\Delta\pmod{2^{k+2}}\). The map from \(x\bmod2^k\) to \(2ux+v\bmod2^{k+1}\) is injective, and each latter residue has two lifts modulo \(2^{k+2}\). A unit square congruence modulo \(2^j\) has at most four roots. Indeed, if \(a,b\) are two odd square roots, \(2^j\mid(a-b)(a+b)\); one of these even factors has valuation exactly one, so \(a\equiv b\) or \(a\equiv-b\pmod{2^{j-1}}\), giving at most four classes modulo \(2^j\). Dividing off an even valuation of \(\Delta\) gives at most \(4\cdot2^{d/2}\) square roots; an odd valuation below the modulus gives none. If \(\Delta\equiv0\pmod{2^{k+2}}\), there are \(2^{\lfloor(k+2)/2\rfloor}\) square roots. The injection and the two lifts prove (5.25). Reinsert the coefficient content; the factor \(p^t\) changes \(p^{(d-2t)/2}\) to \(p^{d/2}\), and the trivial cap remains \(p^k\). \(\square\)

**Lemma 5.8 (complete fourth-moment support).** Let \(\chi\) be primitive modulo any \(q>1\). If at least three of \(b_1,b_2,b_3,b_4\) are distinct, there is a singleton index \(j\), with \(A_j=\prod_{i\ne j}(b_i-b_j)\ne0\), such that

\[
\left|\sum_{x\bmod q}\chi(x+b_1)\chi(x+b_2)
\overline{\chi(x+b_3)\chi(x+b_4)}\right|
\le8^{\omega(q)}\sqrt q\,(A_j,q).
\tag{5.26}
\]

**Proof.** First suppose the two multisets \(\{b_1,b_2\}\), \(\{b_3,b_4\}\) are disjoint. Put

\[
F_1=(X+b_1)(X+b_2),\quad F_2=(X+b_3)(X+b_4),
\quad P=F_1'F_2-F_1F_2'.
\]

This polynomial has degree at most two and

\[
\Delta(P)=4E,\qquad
E=(b_1-b_3)(b_1-b_4)(b_2-b_3)(b_2-b_4)\ne0.
\tag{5.27}
\]

The identity follows by expanding the two monic quadratics; it remains true when \(P\) is linear, with discriminant equal to the square of its linear coefficient.

Consider the local sum at \(p^e\), restricting throughout to \(x\) where \(F_1F_2\) is a unit. For \(e=1\), Lemma 5.2 gives at most \(3\sqrt p\) unless the reduced rational function is a power for the local character. The latter case is covered by the trivial bound whenever \(p\mid E\): if \(p\nmid E\), at least one of the singleton factors has valuation one modulo \(p\), as at most one within-side collision is possible with three distinct integer entries, unless both sides each collapse modulo \(p\). In that last case the reduced rational function can be a square, but its complete sum is at most \(p\); we treat it below using the within-side factors in \(A_j\), rather than asserting a square-root bound for it.

For \(e\ge2\), write \(f=F_1/F_2\), and \(H=f'/f=P/(F_1F_2)\). At an even exponent \(e=2a\), split \(x=y+p^az\). The restriction of a primitive character to \(1+p^a\mathbf Z\) is
\(\chi_p(1+p^az)=e(cz/p^a)\), with \(p\nmid c\). Multiplication of these units is additive modulo \(p^{2a}\); primitivity forces the coefficient to be a unit by testing \(1+p^{2a-1}\mathbf Z\). Taylor expansion and summing over \(z\bmod p^a\) give

\[
S_{p^{2a}}=p^a\sum_{y\bmod p^a\atop P(y)\equiv0\ (p^a)}^*
\chi_p(f(y)).
\tag{5.28}
\]

The star retains only unit factors. Lemma 5.7 bounds this by
\(4p^{e/2}p^{\min(v_p(\Delta)/2,e/2)}\).

For odd \(p\) and \(e=2a+1\ge3\), the map

\[
1+p^az\longmapsto z-\frac{p^a}2z^2\pmod{p^{a+1}}
\]

is an additive group isomorphism. To check additivity substitute
\(z+w+p^azw\) for the parameter of a product; the cross terms cancel, and the remaining terms vanish modulo \(p^{a+1}\). It is bijective by successive lifting, since its derivative is a unit. Hence the primitive character has phase \(c(z-p^az^2/2)/p^{a+1}\), with \(p\nmid c\). Taylor expansion gives

\[
S_{p^{2a+1}}
=p^a\sum_{y\bmod p^a\atop P(y)\equiv0\ (p^a)}^*
\chi_p(f(y))
\sum_{z\bmod p}e\left(\frac c p
\left(\frac{H(y)}{p^a}z+\frac{H'(y)}2z^2\right)\right).
\tag{5.29}
\]

This follows by splitting the shift parameter modulo \(p^{a+1}\) into a residue modulo \(p\) and its \(p^a\) lifts. The lifts vanish unless \(H(y)\equiv0\pmod{p^a}\). If \(H'(y)\) is a unit, the final sum is a quadratic Gauss sum of magnitude \(\sqrt p\), by the Gauss-sum lesson. Then \(P'(y)\) is a unit and the congruence has at most two roots. If \(H'(y)\equiv0\pmod p\), the final sum vanishes unless \(P(y)\equiv0\pmod{p^{a+1}}\), and otherwise equals \(p\). This latter condition is independent of the representative modulo \(p^a\), because \(P'(y)\equiv0\pmod p\). Its number of representatives is therefore the number of roots modulo \(p^{a+1}\), divided by \(p\).

At any root modulo \(p\), \(P'(y)^2\equiv\Delta\pmod p\). Thus the unit-derivative case can occur only when \(p\nmid\Delta\); all roots then have unit derivative. If \(d=v_p(\Delta)<e\) is positive, Lemma 5.7 bounds the second case by \(2p^{d/2-1}\) representatives, and (5.29) by \(2p^ap^{d/2}\). If \(d\ge e\), the trivial bound \(p^e\) suffices. Both cases are at most
\(4p^{e/2}p^{\min(d,e)/2}\).

For \(p=2\), even exponents use (5.28), and \(e\le3\) may use a fixed constant times the trivial bound. For \(e=2a+1\ge5\), the same additive parametrization uses
\(z-2^{a-1}z^2\pmod{2^{a+1}}\); it is additive and bijective since \(a\ge2\). On a unit residue every \(y+b_i\) is odd, and

\[
H'(y)=-\frac1{(y+b_1)^2}-\frac1{(y+b_2)^2}
+\frac1{(y+b_3)^2}+\frac1{(y+b_4)^2}
\equiv0\pmod8.
\]

Indeed the square of each odd unit is 1 modulo 8. The final two-term sum in (5.29) is consequently zero unless \(P(y)\equiv0\pmod{2^{a+1}}\), and is then 2. Lemma 5.7, with the same division by 2 between lifts, gives the bound \(4\cdot2^{e/2}2^{\min(v_2(\Delta),e)/2}\).

At prime exponent one, return to the exceptional power situation noted above. If one side has a repeated residue modulo \(p\) and the other does not, a simple factor still supplies Lemma 5.2. If both sides have repeated residues, then \(p\mid b_1-b_2\) and \(p\mid b_3-b_4\), so the trivial bound is at most \(\sqrt p\) times the square root of
\((b_1-b_2,p)(b_3-b_4,p)\). Combining the local estimates by the Chinese remainder theorem therefore gives

\[
|S_q|\le8^{\omega(q)}\sqrt q\,
\left((E,q)\,\prod_{p\mid q\atop v_p(q)=1,\ p\nmid E,
\ p\mid b_1-b_2,\ p\mid b_3-b_4}p^2\right)^{1/2}.
\tag{5.30}
\]

The factor 4 in \(\Delta=4E\) costs at most 2 globally, absorbed into \(8^{\omega(q)}\). For four distinct integers, the product of the four numbers \((A_j,q)\) is at least \((E,q)^2\). At each prime this follows by writing the valuations of the four cross differences: the two row sums and the two column sums, each capped at \(v_p(q)\), total at least \(2\min(v_p(E),v_p(q))\). The additional primes in (5.30) divide every \(A_j\), through its within-side difference, so their product contributes at least the fourth power of each such prime to that product. The largest \((A_j,q)\) is therefore at least the square-root factor in (5.30).

If exactly three integer entries are distinct and the repeated one is within a side, the singleton entries \(b,c\) are in the other side. In this case
\(E=(a-b)^2(a-c)^2\), and the product of their two \((A_j,q)\) is at least \((E,q)\), since
\(A_b=(a-b)^2(c-b)\), \(A_c=(a-c)^2(b-c)\). Any additional prime in (5.30) divides both singleton products. The larger product again supplies the needed square root.

It remains to treat a repeated entry across the two sides. The rational function cancels to \((X+b)/(X+c)\), with \(b\ne c\), but the common entry \(a\) still excludes its entire nonunit residue class. At modulus \(p^e\), \(e\ge2\), put \(\gamma=v_p(b-c)\). If \(\gamma=0\), the change \(t=(x+b)/(x+c)\) is bijective onto unit \(t\) subject to conditions depending only on \(t\bmod p\). The sum of a primitive character over each allowed unit class modulo \(p\) is zero, by its nontrivial restriction to \(1+p\mathbf Z/p^e\mathbf Z\). If \(1\le\gamma<e-1\), put \(z=(x+c)^{-1}\), so \(t=1+(b-c)z\). The excluded conditions again depend only on \(z\bmod p\). As \(z\) varies over the lifts of one such class, \(t\) runs, with constant multiplicity, over a coset of \(1+p^{\gamma+1}\mathbf Z/p^e\mathbf Z\). Primitivity makes its character sum zero. If \(\gamma\ge e-1\), the trivial bound \(p^e\) is at most \(p^{e/2}(b-c,p^e)\). At \(e=1\), Lemma 5.2 or the trivial bound gives \(2\sqrt p(b-c,p)\). Multiplication gives
\(|S_q|\le2^{\omega(q)}\sqrt q(b-c,q)\). Both singleton products contain \(b-c\), so this is bounded as in (5.26). This completes every possible tuple with at least three distinct entries. \(\square\)

**Theorem 5.9 (Burgess with \(r=2\)).** For every primitive character of conductor \(q>1\), every \(\varepsilon>0\), and all integer \(M\), \(N\ge1\),

\[
|S_\chi(M,N)|\ll_\varepsilon N^{1/2}q^{3/16+\varepsilon}.
\tag{5.31}
\]

**Proof.** Lemma 5.8 and the divisor-product average (5.15) prove (5.14) with \(r=2\) for every modulus: replace \((2r)^{\omega(q)}\) by \(8^{\omega(q)}\), then absorb it using (5.16). The rest of the proof of Theorem 5.6 uses only this complete moment, the arbitrary-modulus collision count, inclusion–exclusion for units and Pólya–Vinogradov. Repeat that induction with \(r=2\); its exponent is \((2+1)/(4\cdot2^2)=3/16\). \(\square\)

### The sixth moment at a general modulus

For the sixth moment, put \(F=f/g\), where \(f\) and \(g\) are monic cubics. The stationary equation is now quartic. Its roots modulo a large prime power can occur in thick congruence classes, so the quadratic discriminant calculation from the fourth moment is insufficient. The following normal form describes those classes for primes greater than 3.

**Lemma 5.10 (cubic stationary classes).** Let \(p>3\), \(n\ge1\), and let \(f,g\in\mathbf Z[X]\) be monic cubics. Suppose the minimum valuation of the coefficients of \(f-g\) is \(\mu<n\), and put \(m=n-\mu\). Consider

\[
\mathcal R_n=
\{x\in\mathbf Z\colon p\nmid f(x)g(x),\quad
f'(x)g(x)-f(x)g'(x)\equiv0\pmod{p^n}\}.
\tag{5.32}
\]

At most four residue classes modulo \(p\) meet this set. In each such class choose any \(t\in\mathcal R_n\). There are \(u,w,v\in\mathbf Z/p^m\mathbf Z\), with \(u\) a unit and \((w,v,p)=1\), and a unit \(\lambda\bmod p^n\), such that

\[
f(X)-\lambda g(X)
\equiv p^\mu u(X-t)^2\big(w(X-t)+v\big)
\pmod{p^n}.
\tag{5.33}
\]

Choose \(w=1\) when \(w\) is a unit, and \(v=1\) otherwise. Write \(\nu=\min(v_p(v),m)\), taking this to be \(m\) if \(v=0\bmod p^m\), and \(L=\lceil m/2\rceil\). The part of \(\mathcal R_n\) in the class \(t\bmod p\) is exactly:

- if \(\nu=0\), the class \(x\equiv t\pmod{p^m}\);
- if \(0<\nu<L\), the two classes
  \(x\equiv t\pmod{p^{m-\nu}}\) and
  \(x\equiv t+vz_0\pmod{p^{m-\nu}}\), where \(z_0\) is uniquely determined modulo \(p^{m-2\nu}\) and \(3z_0+2\equiv0\pmod p\);
- if \(\nu\ge L\), the class \(x\equiv t\pmod{p^L}\).

Thus \(\mathcal R_n\) is a union of at most eight congruence classes of the displayed kinds. In particular,

\[
\#(\mathcal R_n\bmod p^n)
\le8p^{\mu+\lfloor(n-\mu)/2\rfloor}.
\tag{5.34}
\]

**Proof.** Write \(f-g=p^\mu h\), where \(h\) has degree at most two and is nonzero modulo \(p\). The stationary numerator divided by \(p^\mu\) is
\(h'g-hg'\), of degree at most four. It is nonzero modulo \(p\). Indeed, if \((h/g)'=0\) as a rational function over \(\mathbf F_p\), every order of a zero or pole of \(h/g\) is divisible by \(p\). To verify this, at a zero or pole use a local parameter \(z\) and write the function as \(z^e a(z)\), with \(a(0)\ne0\). Its logarithmic derivative has coefficient \(e/z\), which must vanish in the field. All orders here have absolute value at most 3, hence are zero since \(p>3\). A rational function with no zeros or poles is constant. Then \(h=cg\), impossible for a nonzero polynomial of degree at most two and a monic cubic. A nonzero quartic has at most four roots modulo \(p\), proving the first assertion.

Choose \(t\) as stated and take
\(\lambda\equiv f(t)/g(t)\pmod{p^n}\). Both values are units. For \(H=f-\lambda g\), the two stationary conditions give
\(H(t)\equiv H'(t)\equiv0\pmod{p^n}\). The exact cubic Taylor expansion is therefore

\[
H(X)\equiv a(X-t)^3+b(X-t)^2\pmod{p^n},
\qquad a=1-\lambda,\quad b=H''(t)/2.
\]

Division by 2 is permitted. Also \(\lambda-1\equiv(f(t)-g(t))/g(t)\) is divisible by \(p^\mu\), so all coefficients of \(H\) are divisible by \(p^\mu\). They are not all divisible by \(p^{\mu+1}\): otherwise its leading coefficient \(1-\lambda\) would have that divisibility, and
\(f-g=H+(\lambda-1)g\) would too, contradicting the definition of \(\mu\). Translation by \(t\) preserves coefficient content, because its inverse is another integral translation. Thus \(\min(v_p(a),v_p(b))=\mu\), with valuations capped at \(n\). Extract \(p^\mu\) and a unit to obtain (5.33), with the specified normalization.

All \(x\equiv t\pmod p\) retain unit \(f(x)g(x)\). Set \(Y=X-t\) and
\(h_1=Y^2(wY+v)\). The original numerator modulo \(p^n\), after removing its unit and \(p^\mu\), has the same zeros as

\[
h_1g'-h_1'g
=Y\left(Y\big((wY+v)g'-3wg\big)-2vg\right)
\pmod{p^m}.
\tag{5.35}
\]

Here every \(g\) and \(g'\) is evaluated at \(t+Y\). We solve (5.35) with \(Y\equiv0\pmod p\).

If \(\nu=0\), the expression in the outer parentheses is a unit, since its reduction is \(-2v g(t)\). Hence precisely \(Y\equiv0\pmod{p^m}\) solves the congruence.

If \(\nu>0\), then \(w\) is a unit and has been normalized to 1. Put

\[
J(Y)=(Y+v)g'(t+Y)-3g(t+Y).
\]

It is a unit on \(Y\equiv0\pmod p\), with reduction \(-3g(t)\). For a \(Y\) whose valuation \(k\) is less than \(\nu\), the factor \(YJ(Y)-2vg(t+Y)\) has valuation \(k\); the full expression has valuation \(2k\). If \(k>\nu\), that factor instead has valuation \(\nu\), and the full valuation is \(k+\nu\). These statements also cover valuations capped at the modulus in the evident way.

First suppose \(0<\nu<L\), so \(2\nu<m\). No \(k<\nu\) can occur. The solutions with \(k>\nu\) are exactly the class \(Y\equiv0\pmod{p^{m-\nu}}\). For \(k=\nu\), put \(Y=vZ\); then \(Z\) is a unit. Removing \(v^2 Z\) reduces the congruence to

\[
K(Z):=ZJ(vZ)-2g(t+vZ)\equiv0\pmod{p^{m-2\nu}}.
\tag{5.36}
\]

Its reduction is \(-(3Z+2)g(t)\), and its derivative reduces to the unit \(-3g(t)\). The unique root \(Z\equiv-2/3\pmod p\) therefore lifts uniquely at every step: replacing a solution \(Z\bmod p^a\) by \(Z+jp^a\) changes \(K\) modulo \(p^{a+1}\) by \(jp^aK'(Z)\). Exactly one \(j\bmod p\) cancels the next digit. This gives \(z_0\) and the second class in the statement. Its difference from the first centre has valuation \(\nu<m-\nu\), so the two classes are disjoint.

Finally suppose \(\nu\ge L\). If \(k<L\), then \(k<\nu\) and \(2k<m\), so there is no solution. If \(k\ge L\), both terms in the bracketed product (5.35) have valuation at least \(2L\ge m\). Every such \(Y\) solves it. This proves the last case.

In the three cases, a displayed class has respectively \(p^\mu\), \(p^{\mu+\nu}\), or \(p^{\mu+\lfloor m/2\rfloor}\) representatives modulo \(p^n\). In the middle case \(\nu<L\) implies \(\nu\le\lfloor m/2\rfloor\). There are at most two classes over each of the at most four starting classes, proving (5.34). \(\square\)

The class with modulus \(p^{\lceil m/2\rceil}\) is the singular case that cannot be replaced by a bounded number of individual stationary roots. We next bound the character sum over each entire class, before taking the still-required arithmetic average over six shifts.

### Cancellation inside a stationary class

Counting stationary residues is insufficient when one class is thick. We now sum the character over the whole class. The finite-field starting point uses the same written curve fixed-point and Riemann-hypothesis prerequisites as Lemma 5.2.

**Lemma 5.11 (a cubic additive sum).** If \(p>3\) is prime, \(A\in\mathbf F_p^\times\), and \(B,C,D\in\mathbf F_p\), then

\[
\left|\sum_{x\bmod p}e\left(\frac{Ax^3+Bx^2+Cx+D}{p}\right)\right|
\le2\sqrt p.
\tag{5.37}
\]

**Proof.** Write \(P(X)=AX^3+BX^2+CX+D\) and work first over \(k=\overline{\mathbf F}_p\). The equation \(Y^p-Y=P(X)\) defines a connected cover of degree \(p\). Indeed, its splitting field has Galois group a subgroup of the translation group \(\mathbf F_p\); a proper subgroup is trivial. A rational-function solution would have a pole whose order is multiplied by \(p\) in \(Y^p-Y\), whereas the only pole of \(P\) has order 3. Thus no such solution exists.

The cover is étale over the affine line, since its derivative in \(Y\) is \(-1\). Let \(C_P\) be its smooth projective completion. There is one point above infinity, with valuations
\(v(X)=-p\), \(v(Y)=-3\). To check total ramification, let \(e_\infty\) be a ramification index there. The equation gives \(p v(Y)=-3e_\infty\); hence \(p\mid e_\infty\), so \(e_\infty=p\). Its degree exhausts the entire fibre.

Choose integers \(a,b\) with \(-ap-3b=1\) and \(1\le b<p\). The function \(z=X^aY^b\) has valuation one and is a local parameter. For the nonidentity deck translation \(t_c:Y\mapsto Y+c\),

\[
\frac{t_c^*z}{z}=\left(1+\frac cY\right)^b,
\qquad v(t_c^*z-z)=4\quad(c\ne0).
\tag{5.38}
\]

The first nonconstant coefficient is \(bc\ne0\), and \(v(1/Y)=3\), proving the second identity. This also computes the different exponent as \(4(p-1)\). Here is the local algebra behind that computation. A totally ramified extension of complete discrete valuation rings with the same residue field is generated by its uniformizer: the powers \(1,z,\ldots,z^{p-1}\) form a basis, by successive expansion in valuations modulo \(p\). The derivative of its minimal polynomial is \(\prod_{c\ne0}(z-t_c^*z)\). Its valuation is the length of the relative differential module, hence the order contributed by the differential map to Riemann–Hurwitz. Applying that map at infinity, and using its invertibility on the affine part, gives

\[
2g(C_P)-2=-2p+4(p-1),\qquad g(C_P)=p-1.
\tag{5.39}
\]

This is also the differential formulation of Riemann–Hurwitz used in Lemma 5.2, now with the explicitly computed wild different.

Use cohomology with coefficients in a field \(E/\mathbf Q_\ell\), \(\ell\ne p\), containing the \(p\)-th roots of unity. For \(c\ne0\), the only fixed point of \(t_c\) is infinity, and its intersection multiplicity is 4 by (5.38). The curve fixed-point formula therefore gives
\(\operatorname{Tr}(t_c;H^1(C_P,E))=-2\); the traces on \(H^0\) and \(H^2\) are both 1. At the identity the first-cohomology dimension is \(2p-2\), by (5.39). Consequently, as a translation-group representation,
\(H^1(C_P,E)=2(E[\mathbf F_p]-E)\). Every nontrivial character space has dimension 2.

For completeness we identify the desired trace without a sign convention for an Artin–Schreier sheaf. Let \(F\) be the Frobenius endomorphism used in the curve fixed-point formula and put \(N(u)=\#\{x\in\mathbf F_p:P(x)=u\}\). The affine fixed points of \(t_c\circ F\) are exactly the \(pN(-c)\) solutions with \(x\in\mathbf F_p\). Infinity has multiplicity one, because the derivative of Frobenius is zero. Thus
\(\operatorname{Tr}(t_cF;H^1)=p-pN(-c)\). If \(\eta(c)=e(c/p)\), averaging the projector onto the \(\eta\)-character space gives

\[
\operatorname{Tr}(F;H^1_\eta)
=\frac1p\sum_{c\in\mathbf F_p}\eta(c)^{-1}
\operatorname{Tr}(t_cF;H^1)
=-\sum_{x\in\mathbf F_p}\eta(P(x)).
\tag{5.40}
\]

Frobenius commutes with the translations. Its eigenvalues on \(H^1\), hence on this two-dimensional summand, have complex absolute value \(\sqrt p\) by the written curve Riemann hypothesis. Equation (5.40) proves (5.37). \(\square\)

**Lemma 5.12 (a nonsingular quadratic phase).** Let \(p>3\), \(l\ge1\), and \(P\in\mathbf Z[Y]\). If the coefficient of \(Y^2\) is a unit modulo \(p\) and every coefficient of degree at least 3 is divisible by \(p\), then

\[
\left|\sum_{y\bmod p^l}e(P(y)/p^l)\right|=p^{l/2}.
\tag{5.41}
\]

If instead the linear coefficient is a unit and every coefficient of degree at least 2 is divisible by \(p\), the sum is zero.

**Proof.** In the quadratic case \(P'\bmod p\) is linear with unit slope, so it has one root, and this root lifts uniquely to every \(p\)-power by the elementary lifting calculation in Lemma 5.7. For \(l=2j\), split \(y=u+p^jv\). Summation in \(v\) vanishes unless \(P'(u)\equiv0\pmod{p^j}\); the unique surviving class contributes \(p^j\) times a number of absolute value one. For \(l=2j+1\), \(j\ge1\), the same splitting first leaves that unique class modulo \(p^j\), then a quadratic Gauss sum modulo \(p\) with unit quadratic coefficient \(P''(u)/2\). Its magnitude is \(\sqrt p\), giving \(p^j\sqrt p\). The omitted Taylor terms vanish modulo \(p^l\); for \(j=1\) the cubic coefficient supplies the extra factor \(p\). At \(l=1\), use the ordinary quadratic Gauss sum. In the linear case \(P'\) is a unit everywhere. Summing the last digit of \(y\) gives zero for \(l\ge2\), and the linear geometric sum gives zero for \(l=1\). \(\square\)

**Lemma 5.13 (a cubic phase at a prime power).** Let \(p>3\), \(l\ge1\), and \(P\in\mathbf Z[Y]\). Suppose its cubic coefficient is a unit modulo \(p\), while every coefficient of degree at least 4 is divisible by \(p\). Then

\[
\left|\sum_{y\bmod p^l}e(P(y)/p^l)\right|
\le2p^{2l/3}.
\tag{5.42}
\]

**Proof.** We induct on \(l\). Lemma 5.11 proves \(l=1\), since \(2\sqrt p\le2p^{2/3}\). For \(l\ge2\), only the roots of \(P'\bmod p\) can contribute: summing the last digit annihilates every other residue class. This derivative is a quadratic with nonzero leading coefficient.

If it has simple roots, there are at most two. In each root class, the calculation of Lemma 5.12 applies with its unique lifted critical point and unit \(P''/2\); its contribution has magnitude \(p^{l/2}\). Their total is at most \(2p^{l/2}\), which suffices. This calculation is local to the root class: the even-exponent split has one critical lift in it, and the odd-exponent split has one quadratic Gauss sum in it.

Otherwise there is just one root \(t\bmod p\), and it is double. Expand
\(P(t+pY)-P(t)\). Its linear coefficient is divisible by \(p^2\), its quadratic coefficient by \(p^3\), its cubic coefficient has valuation exactly 3, and all higher coefficients have valuation at least 5. Thus its content has valuation either 2 or 3. If it is 2, division by \(p^2\) leaves a unit linear coefficient and all higher coefficients divisible by \(p\). The contribution is zero for \(l>2\), by the linear case of Lemma 5.12, and at most \(p\) for \(l=2\). If its content is 3, the contribution is at most \(p^{l-1}\) for \(l=2,3\), which satisfies (5.42). For \(l>3\), write it as \(p^3Q(Y)\). The polynomial \(Q\) again has unit cubic coefficient and higher coefficients divisible by \(p\). The entire root class contributes

\[
e(P(t)/p^l)\,p^2\sum_{Y\bmod p^{l-3}}e(Q(Y)/p^{l-3}).
\tag{5.43}
\]

The factor \(p^2\) counts the lifts, since \(Y\) initially runs modulo \(p^{l-1}\). Induction bounds (5.43) by \(2p^2p^{2(l-3)/3}=2p^{2l/3}\). A double root is unique, so this recursion creates no growing number of branches. \(\square\)

**Proposition 5.14 (the sum over one stationary class).** Let \(\chi\) be primitive modulo \(p^a\), where \(p>3\) and \(a\ge2\). Write

\[
a=2n+\epsilon,\quad \epsilon\in\{0,-1\},\quad
r=n+\epsilon,\quad m=n-\mu,\quad L=\lceil m/2\rceil.
\tag{5.44}
\]

Take \(f,g,\mu<n\) as in Lemma 5.10 and put \(F=f/g\). For one of its nonterminal stationary classes, write \(\sigma=\nu<L\), so its modulus is \(p^{m-\sigma}\). In the odd case omit the simple classes \(\mu=\sigma=0\). Then, choosing the representatives modulo \(p^r\) in that class,

\[
\left|\sum_{y\bmod p^r\atop y\text{ in the class}}\chi(F(y))\right|
\le p^{(\mu+\sigma+\epsilon)/2}.
\tag{5.45}
\]

For a terminal class of modulus \(p^L\),

\[
\left|\sum_{y\bmod p^r\atop y\text{ in the class}}\chi(F(y))\right|
\le2p^{(n+\mu+2\epsilon)/3}.
\tag{5.46}
\]

All the summands have unit numerator and denominator. The empty class is allowed. The complete sixth-moment arithmetic average is a further assertion, not a consequence of these individual bounds alone.

**Proof.** Taylor coefficients here mean the integral coefficients of the local expansion, rather than derivatives without their factorials. Since \(f-g=p^\mu h\) and \(g(T)\) is a unit, every positive-degree Taylor coefficient of \(F\) on the disc is divisible by \(p^\mu\). The finite expansion modulo \(p^a\) follows by a geometric expansion of \(1/g(T+Z)\); after a shift by \(p^k\), sufficiently high terms vanish. Thus there is no unproved infinite-series substitution.

Choose a centre \(T\) in the stationary class modulo \(p^n\). In a nonterminal class, its Taylor coefficients satisfy
\(v_p(F'(T))\ge n\) and \(v_p(F''(T)/2)=\mu+\sigma\).
To verify the latter equality, use the normal form of Lemma 5.10. At the first branch \(Y=0\), the quadratic coefficient is \(p^\mu uv/g(T)\). For the second branch put \(Y=vZ\), where \(Z\equiv-2/3\pmod p\). The leading part of the second derivative has factor \(2p^\mu uv(3Z+1)\); \(3Z+1\equiv-1\) is a unit. Differentiating the denominator adds only terms of larger valuation. Moving to another stationary centre in the same class changes this coefficient by a multiple of \(p^{\mu+m-\sigma}\), whose valuation exceeds \(\mu+\sigma\). The case \(\sigma=0\) has only the first branch and the same calculation.

Put \(k=m-\sigma\) and \(l=r-k=\mu+\sigma+\epsilon\ge0\). The class is parametrized by \(T+p^kY\), \(Y\bmod p^l\). The quotient \(F(T+p^kY)/F(T)\) has the form \(1+p^{a-l}P(Y)\), with a unit quadratic coefficient in \(P\). Its linear coefficient is integral because \(n+k=a-l\). For every \(j\ge3\), the valuation remaining after division by \(p^{a-l}\) is at least
\(\mu+jk-(a-l)\ge m-2\sigma\ge1\).
Thus all higher coefficients are divisible by \(p\). Also \(a-l=2n-\mu-\sigma> a/2\). The restriction of the primitive character to these units is
\(\chi(1+p^{a-l}z)=e(cz/p^l)\), with \(p\nmid c\) if \(l>0\): the unit group law is additive at this depth, and testing \(1+p^{a-1}\mathbf Z\) gives primitivity of the coefficient. Apply Lemma 5.12. If \(l=0\), there is one term and (5.45) is immediate.

In a terminal class, put \(k=L\) and \(l=r-L\ge0\); this last inequality follows from \(a\ge2\) and \(0\le\mu<n\). The same expansion gives
\(F(T+p^LY)/F(T)=1+p^{n+L}P(Y)\), with \(n+L>a/2\). The linear coefficient is integral since \(v_p(F'(T))\ge n\). The normal form has a unit cubic coefficient after removing \(p^\mu\), and a quadratic coefficient of valuation at least \(\mu+L\). Differentiating \(1/g\) preserves the unit cubic coefficient: the additional terms have at least one extra factor \(p^L\). The resulting cubic coefficient of \(P\) has valuation \(2L-m\), and every coefficient of degree \(j\ge4\) has valuation at least \((j-1)L-m\).

If \(m\) is even, \(2L=m\). Hence \(P\) has unit cubic coefficient and all higher coefficients divisible by \(p\). For \(l>0\), apply Lemma 5.13 to \(cP\) after the same character parametrization; for \(l=0\), use its one term. The exponent is \(2l/3=(n+\mu+2\epsilon)/3\).

If \(m\) is odd, \(2L=m+1\). Every coefficient of degree at least 2 is divisible by \(p\), and the cubic coefficient has valuation exactly one. A unit linear coefficient gives zero by Lemma 5.12. Otherwise divide \(P\) by \(p\); it has unit cubic coefficient, and its coefficients of degree at least 4 remain divisible by \(p\). For \(l\ge2\), the phase sum equals \(p\) times a sum modulo \(p^{l-1}\), bounded by \(2p^{1+2(l-1)/3}\). This is (5.46), since \(2l+1=n+\mu+2\epsilon\). For \(l=1\), its trivial bound \(p\) suffices; for \(l=0\), its one term suffices.

Finally, these parametrizations give the same character values as the representatives modulo \(p^r\). In the even case a shift by \(p^r\) has all positive Taylor terms divisible by \(p^a\). In the odd case this is still true on the retained classes: \(F'\) is divisible by \(p^n\) and \(F''\) by \(p\), so the linear and quadratic terms are divisible by \(p^{r+n}=p^a\) and \(p^{2r+1}=p^a\); the higher terms also vanish. This is exactly why the odd simple classes were excluded. \(\square\)

**Example.** Let \(f=X^3+2\), \(g=X^3+1\), and let \(\chi\) be primitive modulo \(p^{12}\), \(p>3\). Here \(n=6\), \(\mu=0\), and the stationary class at zero is \(y\equiv0\pmod{p^3}\). Write \(y=p^3z\), \(z\bmod p^3\). Then
\[
\frac{F(p^3z)}{F(0)}\equiv1-\frac{p^9z^3}{2}\pmod{p^{12}}.
\]
The character on \(1+p^9\mathbf Z\) has primitive additive coefficient. The class sum, after removing the unit \(\chi(2)\), is therefore a complete unit-coefficient cubic phase modulo \(p^3\). Its magnitude is exactly \(p^2\): nonzero residue classes modulo \(p\) cancel by the last-digit sum, while the zero class has \(p^2\) terms, all equal to one. The raw class contains \(p^3\) residues. This example shows both the needed cancellation and the unavoidable cubic scale.

The phase bounds control each class for \(p>3\). We next extend the phase envelope to primes 2 and 3, retaining its derivative witnesses. The arithmetic counts that follow treat both higher prime powers and the root coincidences at exponent one, then assemble them at every conductor.

### Cubic additive phases at 2 and 3

The large-prime recursion used that 2 and 3 were units. At these two primes we can instead keep the bounded denominator loss and require two powers of the prime in the higher coefficients. This gives a fixed constant independent of the exponent. It is an additive-phase result; the stationary-class and arithmetic use of it for a character sum is a separate step.

Write \(S_{p^l}(P)=\sum_{y\bmod p^l}e(P(y)/p^l)\) for a complete additive phase sum.

**Lemma 5.15 (quadratic phases at the small primes).** Let \(P\in\mathbf Z[Y]\) have unit quadratic coefficient.

- At \(p=2\), if every coefficient of degree at least three is even, the magnitude is at most \(8\,2^{l/2}\).
- At \(p=3\), the cubic coefficient may be arbitrary. If all coefficients of degree at least four are divisible by 3, then the complete sum has magnitude \(3^{l/2}\).

At either prime, a unit linear coefficient and prime-divisible coefficients in every degree at least two give a zero complete sum.

The two quadratic estimates can be recorded together as

\[
|S_{2^l}(P)|\le8\,2^{l/2},\qquad |S_{3^l}(P)|=3^{l/2},
\tag{5.47}
\]

under their respective hypotheses above.

**Proof.** The last assertion follows by summing the last digit: \(P'\) is a unit everywhere; for \(l=1\) it is the ordinary linear sum.

At 2, if the linear coefficient is odd, \(P'\) is a unit and the sum is zero for \(l\ge2\); the two-term sum at \(l=1\) satisfies the claimed bound. Otherwise \(Q=P'/2\) is integral and \(Q'=P''/2\) is odd on every integer, because the quadratic coefficient is odd and every higher coefficient is even. There are at most two roots of \(Q\bmod2\), and each lifts uniquely, by the proved unit-derivative lifting argument. Thus \(P'(y)\equiv0\pmod{2^k}\) has at most four roots modulo \(2^k\), and at most eight modulo \(2^{k+1}\), for \(k\ge2\). At \(k=1\) the same upper bounds hold trivially.

For \(l=2k\), write \(y=u+2^kv\). The sum in \(v\bmod2^k\) vanishes unless \(P'(u)\equiv0\pmod{2^k}\), and otherwise contributes \(2^k\). There are at most four such \(u\bmod2^k\), giving \(4\,2^{l/2}\). For \(l=2k+1\ge3\), write \(y=u+2^{k+1}v\), with \(u\bmod2^{k+1}\), \(v\bmod2^k\). The same argument gives at most \(8\,2^k\le8\,2^{l/2}\). All higher Taylor terms vanish in these splits, since the square of the step is divisible by \(2^l\). The case \(l=1\) is again trivial.

At 3 the derivative modulo 3 is linear with unit slope, since the cubic derivative vanishes and the higher coefficients are divisible by 3. It has exactly one root, with exactly one lift at every depth. The even-exponent split leaves one critical residue and magnitude \(3^{l/2}\). The odd-exponent split leaves one quadratic Gauss sum of magnitude \(\sqrt3\), with unit quadratic coefficient \(P''/2\). For the smallest odd case \(l=3\), the cubic Taylor term has the factor \(3^3\) and vanishes; larger exponents also vanish. At \(l=1\), the identity \(y^3=y\) in \(\mathbf F_3\) absorbs the cubic coefficient into the linear coefficient, leaving an ordinary unit-coefficient quadratic Gauss sum. This proves the exact magnitude for every \(l\). \(\square\)

**Lemma 5.16 (cubic phases at the small primes).** Let \(p\in\{2,3\}\), let \(l\ge1\), and let \(P\in\mathbf Z[Y]\) have unit cubic coefficient and all coefficients of degree at least four divisible by \(p^2\). Then

\[
\left|\sum_{y\bmod p^l}e(P(y)/p^l)\right|
\le C_p p^{2l/3},\qquad C_2=8,\quad C_3=3.
\tag{5.48}
\]

**Proof.** At either prime, the trivial bound suffices for \(l\le3\). We induct on \(l>3\). A noncritical residue class modulo \(p\) vanishes by its last-digit sum.

At 2 the derivative modulo 2 is \(c_1+c_3Y^2\), where \(c_i\) denotes the coefficient of \(Y^i\). Since \(c_3\) is odd and \(Y^2=Y\) on \(\mathbf F_2\), there is exactly one critical class \(t\). In \(P(t+2Y)-P(t)\), the linear and quadratic coefficients are divisible by \(2^2\), the cubic coefficient has valuation exactly 3, and the coefficients of degree at least four have valuation at least \(j+2\) in degree \(j\). Its coefficient content therefore has valuation \(v=2\) or 3.

If \(v=2\), division by four gives an even cubic coefficient and even coefficients in every higher degree. If the quadratic coefficient is odd, the preceding quadratic bound applies; if it is even, the linear coefficient is odd and the sum vanishes. The original class contains \(2^{l-1}\) parameters \(Y\), while the divided phase has modulus \(2^{l-2}\), so its contribution has magnitude at most
\[
2\cdot8\,2^{(l-2)/2}=8\,2^{l/2}
\le8\,2^{2l/3}.
\]
If \(v=3\), division by eight leaves a unit cubic coefficient and coefficients of degree at least four still divisible by four. The class sum is a unit phase times
\[
4\sum_{Y\bmod2^{l-3}}e(Q(Y)/2^{l-3}).
\]
Induction bounds it by \(4\cdot8\,2^{2(l-3)/3}=8\,2^{2l/3}\). There is only one critical class, so recursion introduces no growing number of branches.

At 3, if the quadratic coefficient is a unit, the preceding quadratic lemma already gives the result, even when the cubic coefficient is a unit. If the quadratic coefficient is divisible by 3 and the linear coefficient is a unit, the derivative is a unit, so the sum vanishes. We may therefore suppose \(3\mid c_1,c_2\).

In every class \(t\bmod3\), the positive-degree coefficients of \(P(t+3Y)-P(t)\) have content valuation 2 or 3: the linear coefficient is divisible by \(3^2\), the quadratic coefficient by \(3^3\), and the cubic coefficient has valuation exactly 3. All coefficients of degree \(j\ge4\) have valuation at least \(j+2\). A content-two class divides to a unit linear phase with every higher coefficient divisible by 3, so it gives zero.

A content-three class occurs precisely when \(P'(t)\equiv0\pmod9\). These \(t\) are the roots modulo 3 of the quadratic
\[
R(T)=c_1/3+2(c_2/3)T+c_3T^2.
\]
The terms of degree at least four in \(P\) vanish here after dividing the derivative by 3, by the assumed extra divisibility. After the shift and division by \(3^3\), the polynomial \(Q\) has unit cubic coefficient, higher coefficients still divisible by \(3^2\), and quadratic coefficient
\[
Q_2\equiv c_2/3+c_3t\equiv R'(t)/2\pmod3.
\]
The class contributes a unit phase times \(9S_{l-3}(Q)\).

If \(R\) has simple roots, there are at most two; in each associated \(Q\), the quadratic coefficient is a unit. Their total contribution is at most
\[
2\cdot9\,3^{(l-3)/2}
=2\,3^{(l+1)/2}\le2\,3^{2l/3}\qquad(l\ge4).
\]
If it has a double root, that root is unique. Its \(Q\) again satisfies the cubic hypotheses, so induction bounds its contribution by \(9\cdot3\,3^{2(l-3)/3}=3\,3^{2l/3}\). If it has no root, every class vanishes. A quadratic with unit leading coefficient cannot have both a simple and a double root, so these are all cases. This proves the bound with a constant independent of \(l\). \(\square\)

These are additive estimates with exact coefficient hypotheses. We next derive those hypotheses on the character discs and retain the stationary witnesses needed by the arithmetic count.

### From the small-prime phase to a character sum

We now derive the coefficient hypotheses of the preceding lemmas from a rational-character sum. The extra depth is fixed once and for all; it costs a constant at 2 and 3, rather than a power depending on the conductor exponent.

**Lemma 5.17 (logarithm on a unit disc).** Let \(p=2\) or 3, let \(a>24\), and put \(c=4\). If \(\chi\) is primitive modulo \(p^a\), its restriction to \(1+p^c\mathbf Z_p\) has the form

\[
\chi(u)=e\left(\frac{t\log u}{p^a}\right),\qquad p\nmid t,
\tag{5.49}
\]

where the numerator is read modulo \(p^a\). Let \(f,g\in\mathbf Z[X]\) be monic cubics, let the coefficient content of \(f-g\) have valuation \(\mu<\lceil a/2\rceil\), and choose a unit-factor disc \(X=T+p^cY\). Then

\[
\Psi(Y)=\log\frac{(f/g)(T+p^cY)}{(f/g)(T)}
=\sum_{j\ge1}B_jY^j
\tag{5.50}
\]

is a convergent restricted power series with

\[
v_p(B_j)\ge\mu+cj-v_p(j).
\]

Its positive-degree coefficient content \(\alpha\) is attained among \(B_1,B_2,B_3\), and
\(\mu+c\le\alpha\le\mu+3c<a\). Every coefficient of degree at least four of \(p^{-\alpha}\Psi\) is divisible by \(p^2\). If its cubic coefficient is a unit, then \(\alpha=\mu+3c\).

**Proof.** For \(v_p(z)\ge c\), the logarithm and exponential series converge. Their terms of degree at least two have valuation strictly larger than the first term: use \(v_p(j)\le j-1\) and \(v_p(j!)\le j-1\). The formal inverse and addition identities can be evaluated on this disc, because all series converge and their degree truncations tend to the same limits. Thus logarithm and exponential are inverse isometries between \(1+p^c\mathbf Z_p\) under multiplication and \(p^c\mathbf Z_p\) under addition. They respect quotients modulo \(p^a\). An additive character of the latter cyclic quotient is \(z\mapsto e(tz/p^a)\). Primitivity of \(\chi\), tested on \(1+p^{a-1}\mathbf Z_p\), forces \(t\) to be a unit. This proves the first assertion without assuming a logarithm parametrization of the entire unit group.

Write \(F=f/g\), \(\lambda=F(T)\), and
\(F(T+Z)/F(T)=1+\sum_{j\ge1}A_jZ^j\).
The polynomial \(f-\lambda g\) has zero constant coefficient at \(T\). Its coefficient content is exactly \(\mu\): otherwise its leading coefficient \(1-\lambda\) would be divisible by \(p^{\mu+1}\), and the identity
\(f-g=(f-\lambda g)+(\lambda-1)g\) would contradict the definition of \(\mu\). Translation preserves content. Division by the unit constant of \(g(T+Z)\) is triangular on its first three positive coefficients. Consequently all \(A_j\) are \(p^\mu\)-divisible, and the minimum valuation of \(A_1,A_2,A_3\) is \(\mu\).

The logarithmic derivative \(F'/F\) has integral Taylor coefficients all divisible by \(p^\mu\), because its numerator is \(f'g-fg'\) and its denominator \(fg\) is a unit on the disc. If \(b_j\) is the coefficient of \(Z^j\) in \(\log(F(T+Z)/F(T))\), differentiation gives \(jb_j\) equal to the corresponding coefficient of \(F'/F\). Therefore
\(v_p(b_j)\ge\mu-v_p(j)\), and \(B_j=p^{cj}b_j\) gives the displayed bound. In particular these valuations tend to infinity, so the power series is restricted.

For the first three coefficients, the formal identities are

\[
b_1=A_1,\qquad
b_2=A_2-\frac{A_1^2}{2},\qquad
b_3=A_3-A_1A_2+\frac{A_1^3}{3}.
\tag{5.51}
\]

If \(v_p(A_1)=\mu\), the first coefficient gives \(\alpha\le\mu+c\). If instead \(A_1\) has larger valuation and \(v_p(A_2)=\mu\), then \(v_p(b_2)=\mu\), giving \(\alpha\le\mu+2c\). Otherwise \(v_p(A_3)=\mu\) and the other terms in \(b_3\) have larger valuation, giving \(v_p(b_3)=\mu\) and \(\alpha\le\mu+3c\). At \(p=2,3\), the denominators in these identities lose at most one valuation; the strictly larger valuations in the latter two cases still suffice when \(\mu=0\).

For \(j\ge4\), \(cj-v_p(j)\ge3c+2\). To check this uniformly, \(v_p(j)\le j-2\) for \(j\ge4\), so \(4j-v_p(j)\ge3j+2\ge14\). Thus the minimum is attained in the first three coefficients, every higher coefficient after division by \(p^\alpha\) is \(p^2\)-divisible, and the lower bound \(\alpha\ge\mu+c\) follows from \(cj-v_p(j)\ge c\) for all \(j\ge1\). The upper bound is less than \(a\) because \(\mu<\lceil a/2\rceil\) and \(a>24\).

Finally suppose the cubic coefficient after division is a unit. If \(A_1\) has valuation \(\mu\), then \(b_3\) has valuation at least \(\mu-1\), so \(B_1\) has strictly smaller valuation than \(B_3\), a contradiction. If \(A_1\) has larger valuation and \(A_2\) has valuation \(\mu\), the same comparison between \(B_2\) and \(B_3\) gives a contradiction. Therefore \(A_3\) has valuation \(\mu\) and \(b_3\) has valuation \(\mu\); hence \(\alpha=\mu+3c\). \(\square\)

**Proposition 5.18 (a uniform local character envelope at 2 and 3).** Let \(p=2\) or 3, let \(a\ge1\), let \(\chi\) be primitive modulo \(p^a\), and let \(f,g\) be monic cubics. The complete sum, retaining any prescribed unit-factor exclusions depending only on \(x\bmod p\), is bounded by \(C p^{a/2}\) times a sum of the following nonnegative choices, for an absolute constant \(C\):

- a baseline of weight 1;
- a bad-content choice of weight \(p^{a/2}\), allowed only when every coefficient of \(f-g\) is divisible by \(p^{\lceil a/2\rceil}\);
- good choices indexed by \(0\le\mu<\lceil a/2\rceil\) and \(0\le\sigma\le a+4\), allowed only when every coefficient of \(f-g\) is \(p^\mu\)-divisible and there is a unit-factor witness \(T\) with
  \[
  (f/g)'(T)\equiv(f/g)''(T)\equiv0
  \pmod{p^{\mu+\sigma}}.
  \tag{5.52}
  \]
  Their weights may be taken as
  \[
  \min\{p^{\mu+\sigma},\,p^{a/6+\mu/3}\}.
  \tag{5.53}
  \]

There are \(O((a+1)^2)\) choices, with constants independent of \(a\). A witness modulus equal to 1 imposes no derivative condition.

**Proof.** For \(a\le24\), the trivial bound is at most \(3^{12}p^{a/2}\), so the baseline suffices with an absolute constant. For \(a>24\), let \(\mu\) be the actual content valuation. If \(\mu\ge\lceil a/2\rceil\), including \(f=g\), use the bad-content choice.

Otherwise partition the allowed residues into discs modulo \(p^c\), \(c=4\). There are at most \(p^c\le81\) discs. All exclusions are either satisfied everywhere or nowhere on each disc. The preceding lemma expresses its character as a unit constant times the additive phase \(t\Psi(Y)/p^a\); multiplication by the unit \(t\) changes none of the coefficient valuations. Restricted power series may be truncated modulo the phase modulus to integer polynomials. Thus Lemmas 5.15–5.16 apply, with the same coefficient hypotheses and complete sums. The integral representatives of each coefficient are chosen at that modulus; the full power series is retained when derivative divisibility is used below.

Put \(P=p^{-\alpha}t\Psi\) and \(l=a-\alpha\ge1\). If its cubic and quadratic coefficients are both nonunits, its linear coefficient is a unit, and the sum vanishes. If the cubic coefficient is a nonunit and the quadratic coefficient a unit, the quadratic lemma applies, with its exact hypothesis at 2 and its weaker hypothesis at 3. Since \(Y\) runs modulo \(p^{a-c}\), there are \(p^{\alpha-c}\) copies of the phase sum modulo \(p^l\). This bounds the disc contribution by
\[
C p^{\alpha-c+(a-\alpha)/2}
\le C p^{a/2}p^{\mu/2+c/2}.
\]
All derivatives \(F',F''\) on the unit disc are \(p^\mu\)-divisible, directly from \(F-1=(f-g)/g\). Hence the choice \(\sigma=0\) is allowed. Its required weight is at least \(p^{\mu/2}\), because \(\mu<a\); the fixed factor \(p^{c/2}\le9\) is absorbed into \(C\).

It remains to examine the unit-cubic case. Here \(\alpha=\mu+3c\). Follow the recursion in the small-prime cubic lemma. Each cubic continuation shifts into one residue class and divides its phase by \(p^3\). After \(h\) such continuations, the physical disc has depth \(d=c+h\), the removed phase content is \(\mu+3d\), and the remaining conductor exponent is
\[
l_h=a-\mu-3d\ge1.
\]
The polynomial still has unit cubic coefficient and \(p^2\)-divisible higher coefficients. At 2 there is at most one continuation or regular exit. At 3 a singular continuation is unique; a simple-root step gives at most two regular exits and no singular continuation. Thus one initial disc gives at most two regular leaves or one terminal leaf. There is no factor growing exponentially with \(h\).

A regular quadratic exit at 3, at depth \(d\), has contribution at most
\[
C p^{a/2}p^{(\mu+d)/2}.
\]
This follows by multiplying its normalized quadratic sum by \(p^{\mu+3c-c+2h}\), the lift factor already accumulated. At 2 a content-two exit has depth \(d+1\) and removed content \(\mu+3d+2\); the same multiplication gives exactly the same upper bound with \(\sigma=d\). A simple-root step at 3 is a content-three shift followed by a quadratic exit at depth \(d+1\), so it has the displayed bound with \(\sigma=d+1\).

These are allowed derivative witnesses. On a disc of depth \(e\) whose positive-degree logarithmic phase coefficients are all divisible by \(p^\beta\), the first and second physical derivatives of that phase are divisible by \(p^{\beta-e}\) and \(p^{\beta-2e}\). Differentiation multiplies coefficients by integers and hence never reduces those bounds. At the regular exits just described, these exponents are at least \(\mu+\sigma\). For instance at the 2-adic content-two exit, \(\beta=\mu+3d+2\), \(e=d+1\), and \(\beta-2e=\mu+d\). If \(L=\log(F/F_0)\), then
\(F'=FL'\) and \(F''=F(L''+(L')^2)\). The derivatives of \(F\) therefore have the same required divisibility on the exit disc. Choose any integral centre in it for the witness.

The regular normalized weight \(p^{(\mu+\sigma)/2}\) is at most \(p^{\mu+\sigma}\). Also every regular cubic stage has \(3\sigma\le a-\mu\), since its remaining conductor is positive; this includes a 3-adic simple-root child after its shift. Hence the weight is at most \(p^{a/6+\mu/3}\).

At a terminal stage \(1\le l_h\le3\), use the trivial count of its entire physical disc. Its normalized weight is
\[
p^{a/2-d}
=p^{a/6+\mu/3+l_h/3}
\le3p^{a/6+\mu/3}.
\]
The same derivative calculation, now with \(\beta=\mu+3d\) and \(e=d\), supplies a witness at modulus \(p^{\mu+d}\); take \(\sigma=d\). Moreover
\(a/2-d\le\mu+d\), since \(d=(a-\mu-l_h)/3\), \(l_h\le3\), and \(a>24\). Thus this weight also is at most \(p^{\mu+\sigma}\), apart from the fixed factor 3 already stated.

Each resulting \(\sigma\) is nonnegative and at most \(a+4\). Sum the at most 81 initial discs and their bounded number of leaves, enlarge the allowed sets to the displayed content and witness conditions, and include every possible \((\mu,\sigma)\). This gives the claimed envelope, with one absolute constant. \(\square\)

### Critical values and an arithmetic count

We next count the six-shift tuples that can produce a thick stationary class. Two different variables enter this count. The coefficient content says that the two cubics are close. A stationary point says that their ratio has a critical value. Fixing five shifts turns the sixth into such a value of a rational function of degree at most four.

The valued-field background used below is precisely the existence of \(\mathbf Q_p\), completeness of its finite extensions, and extension of its valuation to a splitting field. The completion is proved in *Local fields*, “Completions, the p-adic numbers and complete discretely valued fields,” Theorem 2.1; the extension and completeness are proved in “Extensions of complete valued fields,” Theorem 1.2 and Proposition 2.1. We normalize the extended valuation by \(v(p)=1\). We prove the polynomial-content and critical-value assertions here; no uniform polynomial-congruence estimate is a prerequisite.

**Lemma 5.19 (finitely many critical values).** Let \(N,D\in\mathbf Z[X]\) have degrees at most \(d\ge1\), and put \(\phi=N/D\). For every prime \(p\) and integer \(s\ge1\), the set

\[
\left\{\phi(x)\bmod p^s:
x\bmod p^s,\quad p\nmid D(x),\quad
\phi'(x)\equiv0\pmod{p^s}\right\}
\]

has at most

\[
\max\{1,d(2d-2)\}
\tag{5.54}
\]

elements. In particular the bound is 24 when \(d=4\). There is no restriction on coefficient content or on the prime. Congruences of rational functions are taken only where their denominators are units.

**Proof.** If there is no allowed \(x\), there is nothing to prove. Thus \(D\) has nonzero reduction modulo \(p\). Put \(W=N'D-ND'\); its degree is at most \(2d-2\), since the possible highest-degree terms cancel. If \(W=0\), the rational function is constant in characteristic zero, and its allowed values form one class. Suppose \(W\ne0\), let \(t\) be its coefficient-content valuation, and put \(c=\lfloor\log_p d\rfloor\).

We first record a content identity. For a polynomial over any finite extension of \(\mathbf Q_p\), let its content valuation be the minimum of its coefficient valuations. This minimum is additive under multiplication: after dividing each polynomial by a coefficient of minimum valuation, reduce the product in the residue field; the product of two nonzero polynomials is nonzero. If

\[
W(X)=C\prod_{j=1}^h(X-\beta_j)
\]

in a splitting field, with multiplicities included, this identity gives

\[
t=v(C)+\sum_j\min\{0,v(\beta_j)\}.
\tag{5.55}
\]

Suppose first that \(s>t\), and take an allowed integer \(x\). If \(W(x)=0\), assign its value to the root \(\beta=x\). Otherwise (5.55) and \(v(W(x))\ge s\) show that some integral root is closer than distance one to \(x\). Choose a nearest root \(\beta\), put \(\delta=x-\beta\), and write \(k=v(\delta)>0\). Nearest means that \(v(x-\beta_j)\le k\) for every root. The ultrametric inequality then gives

\[
\min\{v(\beta-\beta_j),k\}=v(x-\beta_j)
\]

for each \(j\), including \(j\) with \(\beta_j=\beta\). By the same content identity, \(W(\beta+\delta Z)\) has content valuation exactly \(v(W(x))\ge s\).

The value \(D(\beta)\) is a unit, because \(\beta-x\) has positive valuation. All nonconstant coefficients of \(D(\beta+\delta Z)\) have positive valuation. Its reciprocal therefore has a convergent power series on integral \(Z\), with integral coefficients. Set
\(\eta(Z)=\phi(\beta+\delta Z)-\phi(\beta)\). The coefficients of

\[
\eta'(Z)=\frac{\delta W(\beta+\delta Z)}{D(\beta+\delta Z)^2}
\]

have valuation at least \(s+k\). Hence its first \(d\) positive-degree coefficients satisfy

\[
v(\eta_j)\ge s+k-v_p(j)\ge s+k-c
\qquad(1\le j\le d).
\tag{5.56}
\]

The numerator
\(A(Z)=N(\beta+\delta Z)-\phi(\beta)D(\beta+\delta Z)\)
has degree at most \(d\), has zero constant coefficient, and equals \(D(\beta+\delta Z)\eta(Z)\). Each of its coefficients is a finite sum involving only \(\eta_j\) with \(j\le d\). Thus (5.56) bounds every coefficient of \(A\), and evaluation at \(Z=1\) gives

\[
v(\phi(x)-\phi(\beta))\ge s+k-c\ge s-c.
\tag{5.57}
\]

The exact-root case has the same last inequality. Values assigned to one root consequently differ by a multiple of \(p^{\max(0,s-c)}\). Although \(\phi(\beta)\) can lie in the splitting field, the differences of two allowed values lie in \(\mathbf Z_p\); this is all that is needed for the congruence. There are at most \(p^c\le d\) classes modulo \(p^s\) assigned to that root. Since \(h\le2d-2\), this proves (5.54) when \(s>t\). The use of only the first \(d\) coefficients in (5.56) is essential: division by the indices of an infinite series would give no fixed loss.

It remains to treat \(s\le t\). If \(p>d\), a rational function of degree at most \(d\) with zero derivative over \(\mathbf F_p\) is constant. Indeed, after cancelling common factors, the order of every zero or pole must be divisible by \(p\): the coefficient of \(1/Z\) in its logarithmic derivative is that order. All those orders have absolute value at most \(d<p\), so there are no zeros or poles. Choose an integral lift \(b\) of this constant. The polynomial \(N-bD\) is divisible coefficientwise by \(p\), and replacing it by \((N-bD)/p\) divides \(W\) by \(p\). Repeating this argument \(s\) times shows that \(\phi\) is constant modulo \(p^s\) wherever \(D\) is a unit.

If \(p\le d\), then \(c\ge1\). Split the allowed integers into their at most \(p\) classes modulo \(p\), with centres \(x_0\). On one such class use \(x=x_0+pZ\). The derivative of \(\phi(x_0+pZ)-\phi(x_0)\) has all coefficients of valuation at least \(s+1\). The finite-numerator argument just given, with this depth in place of \(s+k\), shows that all values in the class are congruent modulo \(p^{\max(0,s+1-c)}\). If \(s\ge c-1\), it contributes at most \(p^{c-1}\) values modulo \(p^s\); summing over its \(p\) classes gives at most \(p^c\le d\). If \(s<c-1\), the entire set has at most \(p^s<d\) values anyway. This completes the proof. \(\square\)

**Lemma 5.20 (an integer determinant count).** Let \(T\ge1\) be an integer. The number of integer quadruples \((r,s,h,j)\), each coordinate of absolute value at most \(T\), satisfying \(rs+hj=m\), is

\[
\ll
\begin{cases}
T^2\tau(|m|),&m\ne0,\\
T^2(1+\log T),&m=0.
\end{cases}
\tag{5.58}
\]

Consequently, for \(U\ge1\) and every \(\eta>0\), the number satisfying \(rs+hj\equiv0\pmod U\) is
\(\ll_\eta T^{2+\eta}(1+T^2/U)\).

**Proof.** Apart from \((r,h)=(0,0)\), put \(g=(r,h)>0\), \((r,h)=g(r_0,h_0)\), and \(R=\max(|r_0|,|h_0|)\). Necessarily \(g\mid m\), unless \(m=0\), in which case any \(1\le g\le T\) is permitted. There are at most \(8R\) primitive pairs with this value of \(R\). For a fixed pair the solutions for \((s,j)\), if any, form one affine integer line with step \((h_0,-r_0)\). A coordinate with step of absolute value \(R\) shows that at most \(2T/R+1\) of them lie in the square. Summing over \(1\le R\le T/g\) gives \(O(T^2/g)\) solutions for this \(g\). Sum over divisors of \(|m|\), or over every \(g\le T\) when \(m=0\). The omitted pair contributes only \((2T+1)^2\) solutions, and only when \(m=0\). This proves (5.58).

The possible values of \(m\) have \(|m|\le2T^2\), so at most \(1+4T^2/U\) are multiples of \(U\). Formula (5.16), applied with \(K=2\) and a smaller exponent, gives \(\tau(|m|)\ll_\eta T^\eta\) on this range. The same bound absorbs \(1+\log T\). Summing (5.58) proves the congruence assertion. \(\square\)

**Lemma 5.21 (counting six shifts).** Let \(H,U,V,S\) be positive integers, with \((V,S)=1\) and \(U\mid VS\). Put
\(f=\prod_{i=1}^3(X+b_i)\), \(g=\prod_{i=4}^6(X+b_i)\), where \(1\le b_i\le H\). Count the tuples for which:

- every coefficient of \(f-g\) is divisible by \(U\);
- every coefficient of \(f-g\) is divisible by \(V\);
- for each \(p^s\Vert S\), there is an integer \(x\) with \(p\nmid f(x)g(x)\) and \((f/g)'(x)\equiv(f/g)''(x)\equiv0\pmod{p^s}\).

Their number is, for every \(\eta>0\),

\[
\ll_\eta 24^{\omega(S)}H^\eta
\left(\frac{H^6}{UVS}+\frac{H^5}{U}+H^3\right).
\tag{5.59}
\]

The condition at \(S=1\) is empty. Repeated shifts, cancelled factors and the zero polynomial \(f-g\) are all included.

**Proof.** Fix \(a=b_1,b=b_2,c=b_3,d=b_4,t=b_5\), and put
\(A=a+b+c-d\), \(B=ab+ac+bc-dA\). The coefficients of \(X^2\) and \(X\) in \(f-g\) imply
\(t+b_6\equiv A\) and \(tb_6\equiv B\pmod U\). Thus \(Q(t)=t^2-At+B\equiv0\pmod U\). The integer change of variables

\[
\begin{aligned}
r&=a-t,&s&=b-t,&h&=c-d,&j&=a+b-d-t,\\
a-d&=j-s,&b-d&=j-r,&t-d&=j-r-s
\end{aligned}
\qquad Q(t)=rs+hj
\tag{5.60}
\]

is invertible after \(d\) is retained. Its four new coordinates have absolute value at most \(2H\). Lemma 5.20, and the \(H\) choices of \(d\), show that at most
\(O_\eta(H^{5+\eta}/U+H^{3+\eta})\) first-five tuples are possible.

For one such tuple define the polynomials

\[
K=\prod_{i=1}^5(X+b_i),\qquad
J=\sum_{i=1}^3\frac K{X+b_i}-\sum_{i=4}^5\frac K{X+b_i},
\qquad \phi=\frac{K-XJ}{J}.
\tag{5.61}
\]

The fractions defining \(J\) are polynomial quotients, so repeated factors cause no ambiguity. The polynomial \(J\) is monic of degree four: its leading coefficient is \(3-2=1\). The leading terms of \(K-XJ\) cancel, leaving degree at most four.

At a unit witness modulo \(p^s\), write
\(L=J/K\) and \(\mathcal H=(f/g)'/(f/g)=L-1/(X+b_6)\). The first stationary condition gives \(L(x)=1/(x+b_6)\), so both \(K(x)\) and \(J(x)\) are units and \(b_6=\phi(x)\pmod{p^s}\). The second gives \(\mathcal H'(x)=0\), since \((f/g)''/(f/g)=\mathcal H'+\mathcal H^2\). Direct differentiation now gives
\(\phi'(x)=-(L'(x)+L(x)^2)/L(x)^2=0\pmod{p^s}\). Lemma 5.19 allows at most 24 values of \(b_6\) at this prime power. The Chinese remainder theorem allows at most \(24^{\omega(S)}\) values modulo \(S\).

Independently, the coefficient of \(X^2\) modulo \(V\) fixes \(b_6\equiv A-t\pmod V\). Since \((V,S)=1\), there are at most \(24^{\omega(S)}(H/(VS)+1)\) possible last shifts in the interval. Multiply by the first-five bound. The resulting extra term \(H^4/(VS)\) is at most \(H^5/U\), because \(U\mid VS\) and \(H\ge1\). This proves (5.59). \(\square\)

### Root coincidences at a prime conductor

At exponent one a large complete sum can occur because the rational function is a character-order power, even when the two cubic polynomials have different coefficients. Such exceptions impose coincidences among the roots. The following elementary lattice count lets the coincidence pattern vary from prime to prime.

**Lemma 5.22 (five coordinates with two congruences at each prime).** Let \(D\ge1\) be squarefree. For each \(p\mid D\), choose a linear subspace \(E_p\subset\mathbf F_p^5\) of dimension at most three. If \(H\ge1\), then

\[
\#\{b\in\mathbf Z^5: |b_i|\le H,\ b\bmod p\in E_p\ (p\mid D)\}
\ll \frac{H^5}{D^2}+\frac{H^4}{D}+H^3,
\tag{5.62}
\]

with an absolute constant, independent of the subspaces and of the number of primes.

**Proof.** Let \(\Lambda\) be the lattice defined by these congruences. It contains \(D\mathbf Z^5\). The Chinese remainder theorem gives
\([\mathbf Z^5:\Lambda]=\prod_{p\mid D}p^{5-\dim E_p}\ge D^2\).
Moreover every four-by-four minor of four vectors of \(\Lambda\) is divisible by \(D\): modulo every \(p\mid D\) the four vectors lie in a subspace of dimension at most three.

Here is a lattice point bound with its elementary proof. Choose successively a shortest nonzero vector \(v_1\in\Lambda\), then a shortest vector outside its real span, and so on through \(v_5\). Put \(\lambda_i=|v_i|\), for the Euclidean norm. The choices exist because \(\Lambda\) is discrete and spans \(\mathbf R^5\), and \(1\le\lambda_1\le\cdots\le\lambda_5\). Write \(V_i=\operatorname{span}(v_1,\ldots,v_i)\), and choose an orthonormal basis adapted to this flag. Define a linear map \(T\) by dividing the \(i\)-th coordinate in that basis by \(\lambda_i\).

For \(v\in\Lambda\setminus\{0\}\), let \(j\) be the smallest index such that \(v\in V_j\). The greedy choice gives \(|v|\ge\lambda_j\). Its coordinates above \(j\) vanish, and all its remaining coordinates are divided by numbers at most \(\lambda_j\). Hence \(|Tv|\ge1\). Balls of radius \(1/2\) centred at the transformed lattice points therefore have disjoint interiors. A vector in \([-H,H]^5\) has Euclidean norm at most \(\sqrt5 H\), so these balls lie in a rectangular box with side lengths \(2\sqrt5 H/\lambda_i+1\). Comparing volumes gives

\[
\#(\Lambda\cap[-H,H]^5)
\ll \prod_{i=1}^5(1+H/\lambda_i).
\]

The determinant of \(v_1,\ldots,v_5\) is a nonzero integer multiple of \([\mathbf Z^5:\Lambda]\). Hadamard's inequality consequently gives \(\lambda_1\cdots\lambda_5\ge D^2\). The first four vectors are independent, so one of their four-by-four minors is nonzero and has absolute value at least \(D\). The Euclidean norm of their exterior product is at least that minor and at most \(\lambda_1\cdots\lambda_4\); thus \(\lambda_1\cdots\lambda_4\ge D\). This last inequality can equivalently be obtained by the Gram determinant identity, which expresses the square of that norm as the sum of the squared minors.

Expand the displayed product. For a term using \(k\) reciprocal lengths, the largest possible value uses \(\lambda_1,\ldots,\lambda_k\). The degree-five term is at most \(H^5/D^2\), the degree-four terms total at most \(5H^4/D\), and all terms of degree at most three are \(O(H^3)\), since every \(\lambda_i\ge1\). This proves (5.62), including \(D=1\). \(\square\)

**Lemma 5.23 (the prime-level exceptional patterns).** Let \(\chi\) be nontrivial modulo a prime \(p\), of order \(m\ge2\), and put \(f=\prod_{i=1}^3(X+b_i)\), \(g=\prod_{i=4}^6(X+b_i)\). Retain all original unit-factor exclusions in the complete sum \(S_p\). It is bounded by

\[
|S_p|\le 5\sqrt p+p\sum_{\mathcal P}\mathbf1_{\mathcal P}(b),
\tag{5.63}
\]

where there are at most sixteen patterns. Every pattern fixes \(b_6\) to one of the first five shifts modulo \(p\), and restricts the first five coordinates to a linear subspace of dimension at most three.

**Proof.** If \(f/g\) is not a constant times an \(m\)-th power over \(\overline{\mathbf F}_p(X)\), Lemma 5.2 gives \(5\sqrt p\): the set of excluded points consists of at most six roots and infinity. Cancelled roots remain excluded, as required there.

Otherwise every signed root multiplicity, the number of positive shifts minus the number of negative shifts at that residue, is divisible by \(m\). For \(m=2\), this says that the total multiplicity at every residue is even. Pair equal residues. There are precisely fifteen perfect matchings of six labelled positions. In any one matching, the pair containing position six fixes its value, while the two remaining disjoint pairs impose two independent equality congruences among the first five coordinates.

For \(m\ge4\), each signed multiplicity lies between \(-3\) and 3 and must be zero. The positive and negative multisets agree, so a matching consisting of three cross pairs exists; these are among the same fifteen matchings. For \(m=3\), either every signed multiplicity is zero, with the same conclusion, or all three positive shifts coincide at one residue and all three negative shifts coincide at another. The latter gives the additional pattern
\(b_1=b_2=b_3\), \(b_4=b_5=b_6\pmod p\). It fixes \(b_6=b_4\), while the first five coordinates satisfy three independent equalities. Enlarging a pattern to include coincident choices of its two residues is harmless.

In every exceptional case at least one of these patterns holds; its trivial bound is \(p\). Adding nonnegative indicators proves (5.63), uniformly in the character order and at the small primes as well. \(\square\)

### Assembling the moment at every conductor

The two arithmetic counts serve different purposes. Coefficient divisibility controls the stationary classes at higher prime powers. Root coincidences control the character-power exceptions at exponent one. Their moduli are coprime, so the restrictions on the last shift combine exactly. For the first five shifts we will use whichever of the two counts is stronger in the relevant range.

**Proposition 5.24 (the sixth moment at an arbitrary modulus).** Let \(q>1\), and let \(\chi\) be primitive modulo \(q\). For \(H=\lceil q^{1/6}\rceil\) and every \(\eta>0\),

\[
\sum_{x\bmod q}\left|\sum_{b=1}^H\chi(x+b)\right|^6
\ll_\eta q^{1+\eta}H^3.
\tag{5.64}
\]

**Proof.** Expanding the sixth power gives one complete rational-character sum for each six-shift tuple. The Chinese remainder theorem factors it into the local sums \(S_{p^a}\). Primitivity forces each local factor to be primitive; otherwise its smaller conductor, multiplied by the other prime powers, would induce the original character. In particular each prime-level factor is nontrivial. All original unit-factor exclusions are retained.

At \(p>3\), for exponents \(a\ge2\), we first extract a useful envelope from the already proved stationary calculation. Put \(n=\lceil a/2\rceil\), and let \(\mu\) be the coefficient-content valuation of \(f-g\). If \(\mu\ge n\), use the trivial bound \(|S_{p^a}|\le p^a\); call this the bad-content choice. Otherwise Lemma 5.10 and Proposition 5.14 give at most eight stationary classes. A nonterminal class has \(\sigma<\lceil(n-\mu)/2\rceil\) and normalized weight \(p^{(\mu+\sigma)/2}\); a terminal class has \(\sigma=\lceil(n-\mu)/2\rceil\) and weight \(2p^{(a+2\mu)/6}\).

Here normalization means division by \(p^{a/2}\). For even \(a\), this follows from (5.28) and (5.45)–(5.46). For odd \(a=2n-1\), use (5.29), now with the cubic-ratio logarithmic derivative. Its unit-derivative roots contribute at most \(4p^{a/2}\): the stationary numerator has degree at most four and a simple root has one lift at every step. At every other root the final Gauss sum is zero unless \((f/g)'\equiv0\pmod{p^n}\), and is then \(p\). The remaining prefactor is \(p^n\); combining it with the \(\epsilon=-1\) exponents of Proposition 5.14 gives exactly the normalized weights just stated. The odd simple classes are included in the \(4p^{a/2}\) contribution, rather than in that proposition.

Every retained class has a unit centre \(T\) with
\((f/g)'(T)\equiv(f/g)''(T)\equiv0\pmod{p^{\mu+\sigma}}\). Indeed the first derivative is divisible by \(p^n\), while the second has valuation \(\mu+\sigma\) in the nonterminal case and at least that valuation in the terminal case, as computed in Proposition 5.14. Also \(\mu+\sigma\le n\). Its normalized weight is at most twice

\[
w_p=\min\{p^{\mu+\sigma},\ p^{a/6+\mu/3}\}.
\tag{5.65}
\]

For a terminal class the second expression is its weight without the factor two, and it is at most the first because \(a\le4\mu+6\sigma\). For a nonterminal class the first bound is immediate, while \(\mu+\sigma\le(n+\mu)/2\) gives the second. At odd exponents \(n\ge2\), which ensures \((n+\mu)/4\le(2n-1+2\mu)/6\); at even exponents the inequality is automatic. Thus all constants here are absolute.

We can consequently bound each local sum by \(p^{a/2}\) times a fixed constant times a sum of choices: a baseline of weight 1; the bad-content choice of weight \(p^{a/2}\), allowed only when \(p^n\) divides every coefficient of \(f-g\); and good choices \((\mu,\sigma)\) of weight (5.65), allowed only when coefficient divisibility by \(p^\mu\) and the displayed stationary witness both hold. There are \(O((a+1)^2)\) choices. Enlarging their allowed sets in this way only increases the bound. At \(p=2,3\), Proposition 5.18 gives this same envelope, with an absolute local prefactor and \(O((a+1)^2)\) choices. Its good weights have exactly the form (5.65), and its bad-content divisor is the same \(p^{\lceil a/2\rceil}\). The arithmetic assembly below thus includes every higher prime power of the conductor.

Fix one product of local choices. At exponent one, choose either the baseline of weight 1 or one of the exceptional patterns of Lemma 5.23, of normalized weight \(\sqrt p\). Let \(D\) be the product of the primes with an exceptional pattern. At exponents \(a\ge2\), use the baseline, bad-content and good choices just established. Let \(q_b,q_g\) be the products of the prime powers at bad and good choices, and set

\[
\begin{aligned}
V&=\prod_{\mathrm{bad}}p^{\lceil a/2\rceil},&
U_g&=\prod_{\mathrm{good}}p^\mu,\\
S&=\prod_{\mathrm{good}}p^{\mu+\sigma},&
U&=VU_g,\qquad L=VS.
\end{aligned}
\tag{5.66}
\]

Thus \((V,S)=1\), \(U\mid L\), and \((D,L)=1\). Write \(W_h\) for the product of the higher-prime-power weights, and \(W=\sqrt D\,W_h\) for the total weight, before the fixed local constants. They satisfy

\[
\begin{aligned}
W_h&\le L,\\
W_h&\le(q/D)^{1/6}U^{2/3},\\
W&\le H D^{1/3}U^{2/3},\qquad W\le\sqrt q\le H^3.
\end{aligned}
\tag{5.67}
\]

The first bound uses the first expression in (5.65), and the fact that a bad weight \(p^{a/2}\) is at most \(p^{\lceil a/2\rceil}\). For the second, the other expression in (5.65) gives
\(W_h\le\sqrt{q_b}\,q_g^{1/6}U_g^{1/3}\).
Since \(q_b\le V^2\) and \(Dq_bq_g\mid q\), this is at most
\((q/D)^{1/6}V^{2/3}U_g^{1/3}\le(q/D)^{1/6}U^{2/3}\).
The third follows by multiplying by \(\sqrt D\) and using \(q^{1/6}\le H\). Finally every chosen weight is at most the square root of its local modulus. For a good choice, \(\mu<\lceil a/2\rceil\) ensures \(a/6+\mu/3\le a/2\); bad choices attain the square root, and prime-level exceptions have weight \(\sqrt p\). Their product is therefore at most \(\sqrt q\), regardless of how large the coefficient divisor \(U\) is.

For fixed first five shifts, the argument in Lemma 5.21 gives at most \(24^{\omega(S)}\) possibilities for the sixth modulo \(L\). Each chosen pattern fixes it to a specified earlier shift modulo its prime. The Chinese remainder theorem, using \((D,L)=1\), thus gives at most

\[
24^{\omega(S)}\left(\frac{H}{LD}+1\right)
\tag{5.68}
\]

last shifts in the interval. The choices of the specified earlier shift can vary from prime to prime; no global matching is being assumed.

First suppose \(D\le U\). Ignore the prime-level restrictions on the first five shifts. The determinant argument of Lemmas 5.20–5.21 bounds their number by \(O_\delta(H^\delta(H^5/U+H^3))\). Multiplication by (5.68), and absorption of \(H^4/(LD)\) into \(H^5/U\), give

\[
N_A\ll_\delta24^{\omega(S)}H^\delta
\left(\frac{H^6}{ULD}+\frac{H^5}{U}+H^3\right).
\tag{5.69}
\]

Every weighted term is bounded by \(H^6\):

\[
\begin{aligned}
\frac{WH^6}{ULD}&\le\frac{H^6}{U\sqrt D}\le H^6,\\
\frac{WH^5}{U}&\le H^6(D/U)^{1/3}\le H^6,\\
WH^3&\le H^6.
\end{aligned}
\tag{5.70}
\]

The first inequality uses \(W_h\le L\), the second the cubic bound in (5.67), and the third its unconditional square-root bound. This case includes \(D=1\), and hence every squarefull conductor.

Now suppose \(D>U\). Ignore coefficient divisibility on the first five shifts instead. At every \(p\mid D\), their chosen pattern restricts them to a subspace of dimension at most three, so Lemma 5.22 gives

\[
N_B\ll24^{\omega(S)}
\left(\frac{H^5}{D^2}+\frac{H^4}{D}+H^3\right)
\left(\frac{H}{LD}+1\right).
\tag{5.71}
\]

All six weighted terms are again \(O(H^6)\). For the three terms containing \(H/(LD)\), use \(W/L\le\sqrt D\). For the other three use \(W\le HD^{1/3}U^{2/3}\), \(U<D\), and \(W\le H^3\), respectively. Explicitly,

\[
\begin{aligned}
\frac{WH^6}{LD^3}&\le H^6D^{-5/2},&
\frac{WH^5}{LD^2}&\le H^5D^{-3/2},\\
\frac{WH^4}{LD}&\le H^4D^{-1/2},&
\frac{WH^5}{D^2}&\le H^6U^{2/3}D^{-5/3}\le H^6,\\
\frac{WH^4}{D}&\le H^5(U/D)^{2/3}\le H^5,&
WH^3&\le H^6.
\end{aligned}
\tag{5.72}
\]

Since \(H,D\ge1\), each right side is at most \(H^6\). In particular no boundary term requires a joint determinant-and-matching estimate: when the matching divisor is larger, its lattice count suffices; when the coefficient divisor is larger, its determinant count suffices.

The local constants, the critical-value factors, the pattern count and the number of higher-power choices are together bounded by \(\prod_{p^a\Vert q}C(a+1)^2\), for one absolute \(C\). Formula (5.16) bounds this by \(O_\delta(q^\delta)\). Choose \(\delta>0\) small enough to absorb it and \(H^\delta\) into the prescribed \(q^\eta\). Tuples with \(f=g\) as integer polynomials number at most \(6H^3\), because their two multisets agree; their complete sums are at most \(q\). Apply the two counts to all remaining tuples, sum the products of choices, and restore this diagonal contribution. The sixth moment is at most

\[
\ll_\eta qH^3+q^{1/2+\eta}H^6
\ll_\eta q^{1+\eta}H^3,
\tag{5.73}
\]

since \(H\le2q^{1/6}\). This proves (5.64) for every primitive conductor. \(\square\)

![An exact determinant fibre with five labelled lattice points and the three weighted-count terms at q equal to 5 to the fourth times 7 cubed.](assets/character-determinant-fibre.png)

*Figure 2.* Left: the fibre \(2s+3j=12\) in \([-8,8]^2\), used in Lemma 5.20, has exactly the five displayed integer points. Consecutive points differ by \((3,-2)\), up to orientation, so a line contributes \(O(T/R+1)\) points. Right: a choice in Proposition 5.24 with \(q=5^4 7^3\), \(H=8\), a bad-content choice at 5, and a terminal good choice \(\mu=\sigma=1\) at 7 gives \(U=175\), \(L=1225\), \(W=25\,7^{5/6}\). The bars display the three proved upper-bound terms in (5.70), before fixed local constants; they are not measured character sums. Each is below \(H^6\) in this example. The general inequalities, including all constants independent of the exponents, are (5.67) and the paragraph following (5.70).

**Theorem 5.25 (Burgess with r = 3 at every conductor).** Let \(q>1\), and let \(\chi\) be primitive modulo \(q\). Then for every \(\varepsilon>0\) and all integers \(M,N\), \(N\ge1\),

\[
|S_\chi(M,N)|\ll_\varepsilon N^{2/3}q^{1/9+\varepsilon}.
\tag{5.74}
\]

**Proof.** Use the strong induction of Theorem 5.6 with \(r=3\), \(B=H=\lceil q^{1/6}\rceil\), and \(A=\lfloor N/(64H)\rfloor\). Its trivial and Pólya–Vinogradov starting ranges are \(N\le q^{1/3}\) and \(N\ge q^{7/12}\). In between, \(A\asymp N/H\), \(AN\le q\), and the proved unit-density estimate gives \(\#\mathcal A\gg_\delta Aq^{-\delta}\). Lemma 5.5 supplies the same collision estimate without any conductor restriction. The moment bound (5.64) is \(O_\delta(q^{3/2+\delta})\), exactly the bound for \(\sum|T|^6\) used in (5.23) when \(r=3\). Substitution in (5.21)–(5.22) therefore gives its first term at most \(C_\varepsilon N^{2/3}q^{1/9+\varepsilon}\), after taking \(\delta\) small enough to absorb unit-density and logarithmic losses. The two shorter endpoint sums cost at most one quarter of the induction target, by the same choice \(1/64\). Increasing the target constant closes that induction simultaneously for all starting points. Bounded conductors are absorbed as in Theorem 5.6. Every step is thus available under the stated hypotheses. \(\square\)

### The maximal sum under GRH

Assume GRH for every Dirichlet \(L\)-function. The characters needed below include products of our character with characters of a smaller modulus; GRH for just the original factor would not suffice. The explicit formula in The explicit formula for Dirichlet \(L\)-functions, Theorem 5.1, and the local zero count in Zero-free regions and the exceptional zero, Lemma 1.2, will give cancellation over primes. We then remove the integers with a large prime factor from a harmonic sum. This proof uses neither the wider zero-free region nor a general exponential-sum theorem for multiplicative coefficients.

**Lemma 5.26 (an oscillatory zero term).** Let \(X\ge2\), \(X\le Y\le2X\), and \(\beta,\gamma\in\mathbb R\). Put \(B=1+|\beta|X\). For zeros \(1/2+i\gamma\) of a Dirichlet \(L\)-function of conductor \(d\), counted with multiplicity,

\[
\sum_{|\gamma|\le X}
\left|\int_X^Y t^{-1/2+i\gamma}e(\beta t)\,dt\right|
\ll \sqrt X\sqrt B\log^2(d(X+2)).
\tag{5.75}
\]

**Proof.** We first prove the two elementary integral estimates being used. If a real phase \(\phi\) has monotone derivative with \(|\phi'|\ge\lambda>0\) on an interval, integration by parts gives

\[
\left|\int a(t)e^{i\phi(t)}\,dt\right|
\ll \lambda^{-1}\left(\|a\|_\infty+\int|a'(t)|\,dt\right).
\]

Indeed, the boundary terms and the derivative of \(a\) have this bound. The remaining integral contains \(a\phi''/(\phi')^2\); monotonicity makes the integral of \(|\phi''|/(\phi')^2\) at most \(2/\lambda\). The same argument applies to each of two subintervals.

For our phase \(\phi(t)=\gamma\log t+2\pi\beta t\), the amplitude \(a(t)=t^{-1/2}\) has supremum plus total variation \(O(X^{-1/2})\). If \(|\gamma|\ge1\), then \(|\phi''(t)|=|\gamma|/t^2\ge |\gamma|/(4X^2)\). The interval where \(|\phi'|\le\sqrt{|\gamma|}/X\) has length at most \(8X/\sqrt{|\gamma|}\). Bound its integral directly, and use the preceding first-derivative estimate on its complement. We obtain

\[
\left|\int_X^Y t^{-1/2+i\gamma}e(\beta t)\,dt\right|
\ll \sqrt{X/|\gamma|}.
\]

When \(B\ge2\) and \(|\gamma|\le\pi|\beta|X\), the phase derivative instead has magnitude at least \(\pi|\beta|\); the first-derivative bound is \(O(\sqrt X/B)\). For \(\pi|\beta|X<|\gamma|\le16\pi B\), the second-derivative bound is \(O(\sqrt X/\sqrt B)\). When \(|\gamma|>16\pi B\), the first-derivative bound is \(O(\sqrt X/|\gamma|)\), since \(|\gamma|/t\) dominates \(2\pi|\beta|\). If \(B<2\), use the direct bound \(O(\sqrt X)\) for \(|\gamma|\le32\pi\) and the same reciprocal bound beyond it.

The local zero count gives \(O(U\log(d(U+2)))\) ordinates in \(|\gamma|\le U\), for \(U\ge1\). It also gives
\(\sum_{1<|\gamma|\le X}|\gamma|^{-1}\ll\log^2(d(X+2))\), by grouping the ordinates into unit intervals and summing \(\log(d(k+2))/k\). Apply these counts to the three ranges above. Their contributions are respectively \(O(\sqrt X\log(d(X+2)))\), \(O(\sqrt X\sqrt B\log(d(X+2)))\), and \(O(\sqrt X\log^2(d(X+2)))\). An empty range contributes zero. This proves (5.75), with an absolute constant. \(\square\)

**Lemma 5.27 (prime cancellation with an additive phase).** Suppose that \(\chi\) is primitive of conductor \(q>1\). Under GRH, uniformly for \(2\le X\le q\), \(X\le Y\le\min(2X,q)\), and every real \(\alpha\),

\[
\left|\sum_{X<p\le Y}\chi(p)(\log p)e(\alpha p)\right|
\ll X^{3/4}\log^2(3qX).
\tag{5.76}
\]

**Proof.** First let \(\theta\) be any nonprincipal character modulo \(D\), and suppose \(|\beta|X\le2\sqrt X\). Apply the stable explicit formula with height \(T=X\) throughout \([X,Y]\):

\[
\psi(t,\theta)=-\sum_{|\gamma|\le X}
\frac{t^{1/2+i\gamma}-1}{1/2+i\gamma}+E(t),
\qquad |E(t)|\ll\log^2(3DX).
\]

Here GRH puts every nontrivial zero on the stated line. The formula already includes the finite Euler-factor correction for an imprimitive character. At jumps either endpoint convention changes the formula by \(O(\log(2X))\), covered by the error. Stieltjes integration against \(e(\beta t)\), followed by ordinary integration by parts on the finite zero sum, gives

\[
\sum_{X<n\le Y}\theta(n)\Lambda(n)e(\beta n)
=-\sum_{|\gamma|\le X}\int_X^Y
t^{-1/2+i\gamma}e(\beta t)\,dt
+O\big((1+|\beta|X)\log^2(3DX)\big).
\]

To justify the error, use the two endpoint values of \(E\) and
\(2\pi|\beta|\int_X^Y|E(t)|\,dt\). No differentiation of an error term is required. Lemma 5.26 bounds the zero integrals. Since \(1+|\beta|X\le1+2\sqrt X\), their total and the error are

\[
\ll\sqrt X\sqrt{1+|\beta|X}\log^2(3DX).
\tag{5.77}
\]

Now let \(R=\lfloor\sqrt X\rfloor\). The pigeonhole principle applied to the fractional parts of \(0,\alpha,\ldots,R\alpha\) gives a reduced fraction \(a/r\), with \(1\le r\le R\), such that
\(|\alpha-a/r|\le1/(rR)\le2/(r\sqrt X)\). Set \(\beta=\alpha-a/r\). On the units modulo \(r\), expand the function \(u\mapsto e(au/r)\) in the orthonormal character basis:

\[
e(au/r)=\sum_{\eta\bmod r}c_\eta\eta(u),
\qquad
\sum_\eta|c_\eta|^2=1,
\qquad
\sum_\eta|c_\eta|\le\sqrt{\varphi(r)}\le\sqrt r.
\]

The convention at \(r=1\) is the single constant character, with coefficient 1. Each product \(\chi\eta\), considered modulo \(D=\operatorname{lcm}(q,r)\), is nonprincipal: a principal product would make the primitive conductor \(q\) divide \(r\), whereas \(r\le\sqrt X<q\). This is the uniqueness of the primitive inducing character proved in the first lesson. Consequently (5.77) applies to every product; \(D\le qr\).

The terms of the \(\Lambda\)-sum that are not units modulo \(r\) are powers of primes dividing \(r\). Their total absolute weight on \([X,2X]\) is \(O(\log(2r)\log(2X))\). After the character expansion, the other terms are bounded by

\[
\sqrt r\sqrt X\sqrt{1+2\sqrt X/r}\log^2(3qrX)
\ll X^{3/4}\log^2(3qX),
\]

because \(r\le\sqrt X\). Finally remove powers \(p^k\), \(k\ge2\). There are \(O(\sqrt X\log(2X))\) such integers in this interval and each has weight at most \(\log(2X)\); this contributes \(O(\sqrt X\log^2(2X))\). We have proved (5.76). \(\square\)

**Lemma 5.28 (a harmonic sum).** Under the same hypotheses, uniformly for \(1\le N\le q\) and \(\alpha\in\mathbb R\),

\[
\left|\sum_{n\le N}\frac{\chi(n)}n e(\alpha n)\right|
\ll\log\log(3q).
\tag{5.78}
\]

**Proof.** Partial summation in (5.76), with weight \(1/(t\log t)\), and then a division into dyadic intervals give, for \(2\le A\le B\le q\),

\[
\left|\sum_{A<p\le B}\frac{\chi(p)}p e(\alpha p)\right|
\ll A^{-1/4}\log^2(3q).
\tag{5.79}
\]

In detail, on \([X,2X]\) the partial prime sum with weight \(\log p\) is \(O(X^{3/4}\log^2(3q))\). The supremum plus total variation of \(1/(t\log t)\) is \(O(1/(X\log X))\). Their product is at most \(O(X^{-1/4}\log^2(3q))\). Summing this over \(X=A,2A,4A,\ldots\) is a convergent geometric series. Including either endpoint prime changes the estimate by at most \(1/A\), also covered.

Write \(P^+(m)\) for the largest prime factor of \(m\), with \(P^+(1)=1\), and put
\(y=\min(q,(\log(3q))^{16})\). The integers whose prime factors are all at most \(y\) have harmonic mass

\[
\sum_{P^+(m)\le y}\frac1m
=\prod_{p\le y}(1-1/p)^{-1}\ll\log(2y).
\]

This is a full infinite sum: it follows by multiplying finitely many convergent geometric series. The upper bound follows from Section 4's prime reciprocal estimate, since
\(-\log(1-1/p)=1/p+O(1/p^2)\). Moreover \(\log(2y)\ll\log\log(3q)\). If \(y=q\), this already proves (5.78).

Otherwise every integer \(n\le N\) with \(P^+(n)>y\) has the unique representation \(n=mp\), where \(p=P^+(n)>y\) and \(P^+(m)\le p\). Complete multiplicativity gives the exact contribution

\[
\sum_{m\le N/y}\frac{\chi(m)}m
\sum_{\substack{y<p\le N/m\\p\ge P^+(m)}}
\frac{\chi(p)}p e(m\alpha p).
\]

The representation remains unique when \(p^2\mid n\); its inner lower endpoint is inclusive at \(P^+(m)\). Apply (5.79), including its endpoint observation, to each inner interval. Its absolute value is at most
\(C\log^2(3q)\max(y,P^+(m))^{-1/4}\). This estimate is uniform in the new phase \(m\alpha\).

Here is the needed summation over \(m\), without a factor \(\log q\). For any fixed \(\delta>0\), the identity
\(v^{-\delta}=\delta\int_v^\infty t^{-1-\delta}\,dt\) and positivity give

\[
\begin{aligned}
\sum_{m\ge1}\frac{\max(y,P^+(m))^{-\delta}}m
&=\delta\int_y^\infty t^{-1-\delta}
\prod_{p\le t}(1-1/p)^{-1}\,dt\\
&\ll_\delta y^{-\delta}\log(2y).
\end{aligned}
\]

Interchanging this nonnegative sum and integral is justified by monotone convergence; the last integral is finite. At \(\delta=1/4\), the nonsmooth contribution is therefore
\(O(\log^2(3q)y^{-1/4}\log(2y))=O(1)\). Combine it with the smooth contribution to obtain (5.78). \(\square\)

**Theorem 5.29 (the GRH maximum).** Assuming GRH for all Dirichlet \(L\)-functions, every nonprincipal character modulo \(q\) satisfies

\[
\sup_{M\in\mathbb R,\ N\ge0}|S_\chi(M,N)|
\ll\sqrt q\log\log(3q),
\tag{5.80}
\]

with an absolute constant.

**Proof.** First let \(\chi\) be primitive. Use periodicity and rounding to take integer endpoints and \(0\le N\le q\). In the completed sum (1.1) the geometric progression is

\[
\frac{e(-r(M+1)/q)-e(-r(M+N+1)/q)}{1-e(-r/q)}.
\]

Represent the nonzero frequencies by signed integers with \(0<|r|\le q/2\), choosing the middle frequency only once. Uniformly on this range,

\[
\frac1{q(1-e(-r/q))}=\frac1{2\pi i r}+O(1/q).
\]

For completeness, the difference between \((1-e(-t))^{-1}\) and \((2\pi i t)^{-1}\) extends continuously at 0 by the Taylor expansion and is bounded on \([-1/2,1/2]\); this proves the estimate. The sum of the error terms is \(O(1)\), before multiplication by \(\tau(\chi)\). Pairing positive and negative frequencies, with \(\overline\chi(-r)=\chi(-1)\overline\chi(r)\), leaves four harmonic sums of the form (5.78), at the two endpoint phases and their negatives. Apply Lemma 5.28 to \(\overline\chi\), and use \(|\tau(\chi)|=\sqrt q\). Any unpaired middle frequency has size \(O(1)\) before this multiplication. This proves (5.80) for primitive characters.

For a character induced from primitive conductor \(d>1\), the exact divisor identity (1.5) expresses its interval sum as at most \(\tau(q/d)\) sums of the inducing character, each multiplied by a number of modulus at most 1. Since \(\tau(q/d)\le2\sqrt{q/d}\), the primitive bound gives
\(O(\sqrt q\log\log(3d))\), and hence (5.80). The inducing character of a nonprincipal character is nonprincipal. \(\square\)

The gain comes from a precise change in the Fourier estimate. Completion alone takes the absolute values of all reciprocal-frequency coefficients, giving \(\log q\). Under GRH, their character-weighted sum can be reduced to integers with prime factors at most a fixed power of \(\log q\); their entire harmonic mass is only \(O(\log\log q)\).

## 6. Exercises

1. **Easy.** Prove \(\sum_{n=1}^q\chi(n)=0\) for a nonprincipal character, and deduce the uniform trivial bound \(\varphi(q)\) for interval sums.
2. **Medium.** Complete the conductor reduction in Pólya–Vinogradov, with an absolute constant independent of \(q/q^*\).
3. **Medium.** Prove \(n_2(p)\ll\sqrt p\log p\) for odd primes.
4. **Medium.** Obtain a lower bound \(\max_N|\sum_{n\le N}\chi(n)|\gg\sqrt q\) for primitive characters by the mean square of their partial sums.
5. **Hard.** Prove \(n_2(p)\ll_\varepsilon p^{1/(2\sqrt e)+\varepsilon}\). Derive the prime reciprocal estimate you need from the weighted Mertens estimate; do not assume the prime number theorem.

6. **Medium.** For \(Y^p-Y=AX^3+BX^2+CX+D\), compute the ramification index, different exponent, genus and dimensions of the nontrivial translation-character spaces. Explain why the total genus alone gives the wrong constant in (5.37).
7. **Hard.** Compute \(\sum_{y\bmod p^3}e(cy^3/p^3)\) for \(p>3\), \(p\nmid c\), using only a last-digit sum. Explain the unique double-root branch in the proof of Lemma 5.13 and why its iteration does not introduce an exponential factor in the bound.
8. **Hard.** For \(f=X^3+2\), \(g=X^3+1\) and a primitive character modulo \(p^{12}\), determine the stationary class at zero and its character-sum magnitude. Compare the raw root count with (5.46), and identify the extra statement needed to turn that bound into a sixth moment.

9. **Medium.** Determine the critical values of \(X^2\) modulo \(2^s\) and of \(X^3\) modulo \(3^s\), for every \(s\ge1\). Explain why a proof of Lemma 5.19 cannot simply declare derivative-zero functions constant at these small primes.
10. **Hard.** Derive the integer change of variables (5.60), including its inverse after \(d\) is retained. For fixed \((r,h)\ne(0,0)\), prove the line count used in Lemma 5.20, including the cases where one of \(r,h\) vanishes.
11. **Hard.** Let \(p>7\), let \(\chi\) be the quadratic character modulo \(p\), and choose distinct residues \(a,b,c\). For \(f=(X+a)^2(X+c)\), \(g=(X+b)^2(X+c)\), compute the complete six-shift sum with all original unit exclusions retained. Show that \(f-g\) is nonzero modulo \(p\). Explain why the bad-content choice in Proposition 5.24 does not cover this prime-level case.
12. **Hard.** In the case \(D=1\), use \(W_h\le L\), \(W\le HU^{2/3}\) and \(W\le H^3\) to prove the three weighted bounds (5.70). For \(q=5^4 7^3\), take the bad-content choice at 5 and the terminal choice \(\mu=\sigma=1\) at 7; compute \(H,U,L,W\), before the fixed local constants.

13. **Medium.** Evaluate \(S_l=\sum_{y\bmod2^l}e(y^3/2^l)\) for every \(l\ge1\). Determine the first three values directly, and use the unique singular branch rather than assuming that an odd-degree polynomial always has zero complete sum.
14. **Hard.** In Lemma 5.17, prove that the first three positive coefficients of \(F(T+Z)/F(T)-1\) have minimum valuation \(\mu\), and show why unit-cubic dominance forces \(\alpha=\mu+12\). For \(g=X^3+1\), \(f=X^3+1+p^2\), \(a=36\), calculate the remaining phase exponents and physical depths along the singular branch at zero. Give its terminal normalized upper-bound weight and the derivative-witness modulus; do not identify that upper bound with the actual character sum.

15. **Medium.** At the primes 2 and 3, impose respectively the matchings \((1,2),(3,4),(5,6)\) and \((1,3),(2,5),(4,6)\). Show that the first-five lattice has index 36, that every four-by-four minor of its vectors is divisible by 6, and that exactly 216 first-five vectors occur in the residue box \(\{0,\ldots,5\}^5\). Determine the sixth-shift class modulo 6. Explain why no single matching is required at both primes.
16. **Hard.** Prove each of the six weighted bounds (5.72) directly from (5.67) and \(D>U\). For \(q=5^4 7^3 13\cdot17\), choose the same higher-power weights as in Exercise 12 and prime-level exceptional patterns at both 13 and 17. Calculate \(H,D,U,L,W\), and identify which arithmetic count applies. The weights are upper bounds, not evaluations of the actual sums.

## 7. Solutions

**1.** Choose a unit \(u\bmod q\) with \(\chi(u)\ne1\). Multiplication by \(u\) permutes all residue classes, so the sum over a period equals \(\chi(u)\) times itself and hence is zero. For an interval, subtract complete blocks of \(q\) terms. The remaining block has fewer than \(q\) consecutive terms and at most \(\varphi(q)\) units. Each unit contributes a complex number of modulus 1 and each nonunit contributes zero. The triangle inequality proves the bound. This works for negative starting points and real endpoints as well.

**2.** Put \(h=q/q^*\) and use
\(\chi(n)=\chi^*(n)\sum_{d\mid(n,h)}\mu(d)\).
Writing \(n=dm\) gives (1.5), with \(\psi=\chi^*\). Multiplicativity remains valid when \(d\) is not a unit: in that case its character value, and the whole term, are zero. Each inner sum is bounded by \(\sqrt{q^*}(1+\log q^*)\). Pairing complementary divisors gives at most \(2\sqrt h\) terms. Their sum is at most \(2\sqrt q(1+\log q)\), proving uniformity. The inducing character cannot be principal, because then the induced character would be principal too.

**3.** By definition the first \(n_2(p)-1\) values of \(\chi_p\) are all 1. The Legendre character is primitive modulo \(p\): a nonprincipal character at a prime modulus has no smaller conductor. Apply (1.4) to this initial interval to get \(n_2(p)-1\le\sqrt p(1+\log p)\). For \(p\ge3\), \(1+\log p\ll\log p\), which is the required estimate.

**4.** Define the periodic partial sum \(S(n)\) as in Theorem 3.2. Fourier transforming \(S(n)-S(n-1)=\chi(n)\) gives
\((1-e(-k/q))F(k)=\sum_n\chi(n)e(-kn/q)\).
At \(k=1\) the latter sum has modulus \(\sqrt q\). Since \(2\sin(\pi/q)\le2\pi/q\), we get \(|F(1)|\ge q^{3/2}/(2\pi)\). Parseval then gives
\(q^{-1}\sum_n|S(n)|^2\ge |F(1)|^2/q^2\ge q/(4\pi^2)\).
At least one partial sum is at least \(\sqrt q/(2\pi)\) in modulus. The primitive principal character at modulus 1 is excluded from this periodic zero-mean calculation; its ordinary partial sums grow without bound.

**5.** Write \(A(t)=\log t+O(1)\) for the weighted prime sum from the earlier lesson. Partial summation gives
\(\sum_{\ell\le t}1/\ell=A(t)/\log t+\int_2^t A(u)/(u\log^2u)\,du\).
The bounded error has a convergent integral, leaving (4.1), including its \(O(1/\log t)\) remainder. With \(\beta=1/(2\sqrt e)+\varepsilon<1/2\), choose \(1/2<\alpha<\min(1,\sqrt e\beta)\). If \(n_2(p)>p^\beta\), every integer at most \(p^\alpha\) whose prime factors are at most \(p^\beta\) has character value 1. The union bound (4.3) shows that at most
\(x(\log(\alpha/\beta)+o(1))\)
integers up to \(x=\lfloor p^\alpha\rfloor\) can fail this condition. Their values are at worst \(-1\), so the total sum is at least
\(x(1-2\log(\alpha/\beta)+o(1))\).
This is a positive fixed proportion of \(x\), whereas (1.4) gives \(o(x)\). This proves the bound for all sufficiently large primes. Increase the constant for the finitely many others. Larger \(\varepsilon\) follow from any smaller positive choice.

**6.** The cubic pole forces total ramification of index \(p\). A uniformizer \(z=X^aY^b\), with \(-ap-3b=1\), has \(v(z-t_cz)=4\) for every nonzero translation, so the different exponent is \(4(p-1)\). The differential degree calculation gives \(2g-2=-2p+4(p-1)\), hence \(g=p-1\). The nonidentity deck trace on \(H^1\) is \(-2\); its identity trace is \(2p-2\). Character orthogonality gives dimension 2 for every nontrivial character and zero for the trivial character. The desired additive sum is one of these two-dimensional traces, giving \(2\sqrt p\), whereas using all of \(H^1\) would give \(2(p-1)\sqrt p\).

**7.** In a class \(y=t\pmod p\), \(t\ne0\), shifting the last digit by \(p^2v\) adds \(3ct^2v/p\) to the phase, and its sum in \(v\bmod p\) is zero. In the zero class \(y=pu\), every phase is integral; its \(p^2\) terms give exactly \(p^2\). At a double root the derivative quadratic has no other root modulo \(p\). Division after the shift either gives a nonstationary linear phase or removes exactly three powers of \(p\) and leaves one cubic problem. The latter step contributes \(p^2\) while reducing the exponent by 3; this preserves \(p^{2l/3}\) with a constant independent of the number of steps.

**8.** The derivative numerator is \(-3X^2\), up to reversing its sign convention, and the factors are units on the disc at zero. Thus \(X^2\equiv0\pmod{p^6}\) gives \(X\equiv0\pmod{p^3}\). There are \(p^3\) representatives modulo \(p^6\). Substitution gives the displayed unit ratio \(1-p^9z^3/2\pmod{p^{12}}\). Primitivity makes its phase coefficient modulo \(p^3\) a unit. Exercise 7 therefore gives magnitude \(p^2\); (5.46) gives the consistent upper bound \(2p^2\). A moment additionally needs a uniform count of the occurrences and weights of these classes over six interval shifts, followed by a compatible Chinese-remainder assembly. Lemma 5.21, the prime-level lattice and pattern Lemmas 5.22–5.23, and Proposition 5.24 supply that step for every conductor.

**9.** The critical condition for the square is \(2x\equiv0\pmod{2^s}\), so \(v_2(x)\ge\max(0,s-1)\). At \(s=1\), the two values of \(x^2\) are 0 and 1. At \(s\ge2\), \(v_2(x^2)\ge2s-2\ge s\), so the only value is 0. For the cube the condition is \(3x^2\equiv0\pmod{3^s}\), or \(v_3(x)\ge\max(0,\lceil(s-1)/2\rceil)\). At \(s=1\), the values are 0, 1 and 2. At \(s\ge2\), \(3\lceil(s-1)/2\rceil\ge s\), so again the only value is 0. In characteristic 2 the square and in characteristic 3 the cube have zero derivative without being constant. The residue-ball and finite-numerator part of Lemma 5.19 handles this issue with a bounded loss.

**10.** Expand \(Q(t)=t^2-(a+b+c-d)t+ab+ac+bc-d(a+b+c-d)\). Put \(u=a-d,v=b-d,z=c-d,y=t-d\); it becomes \(y^2-(u+v+z)y+uv+uz+vz\). Substituting \(r=u-y,s=v-y,h=z,j=u+v-y\) gives \(rs+hj\). Conversely \(y=j-r-s,u=j-s,v=j-r,z=h\), proving that the integer map is invertible. If \(g=(r,h)\), Bézout's identity shows that \(rs+hj=m\) is solvable exactly when \(g\mid m\). One solution generates all others by \((s,j)\mapsto(s,j)+k(h/g,-r/g)\): subtract two solutions, divide by \(g\), and use coprimality. At least one step coordinate has absolute value \(R=\max(|r|,|h|)/g\), so at most \(2T/R+1\) choices of \(k\) stay in the square. If \(r=0\), then \(h/g=\pm1\) and \(j\) is fixed while \(s\) varies by unit steps; if \(h=0\), the same argument interchanges the coordinates. These cases satisfy exactly the same bound.

**11.** On each of the \(p-3\) allowed residues, the ratio is \(((x+a)/(x+b))^2\), a nonzero square, so its quadratic-character value is 1. At the three excluded residues the original product of six characters is zero. The complete sum is therefore \(p-3\). Yet
\[
f-g=(a-b)(X+c)(2X+a+b)
\]
is a nonzero polynomial modulo \(p\), since \(a-b\ne0\) and \(p\ne2\). Thus its coefficient content is zero. A weight 1 baseline would not give a uniform square-root bound for this family, while the bad-content choice demands positive content. The higher-prime-power bad-content choice therefore cannot cover this case. Lemma 5.23 instead uses root coincidences, and Lemma 5.22 supplies their arithmetic count in the full assembly.

**12.** The first term satisfies \(WH^6/(UL)\le H^6/U\le H^6\). The second satisfies \(WH^5/U\le H^6U^{-1/3}\le H^6\). The third satisfies \(WH^3\le H^6\) directly from \(W\le H^3\). For the stated conductor, \(q=214375\), and \(7^6<q\le8^6\), so \(H=8\). At 5, \(a=4,n=2\), and the bad-content divisor is \(V=25\), with normalized weight \(25\). At 7, \(a=3,n=2,\mu=1\), so \(n-\mu=1\) and the terminal parameter is \(\sigma=1\). Hence \(U_g=7,S=49,U=175,L=1225\); its weight in (5.65) is \(7^{5/6}\). Their product is \(W=25\,7^{5/6}\), as displayed in Figure 2. The omitted local factors and choice count are absorbed by \(q^\eta\) in the proof, rather than silently assigned value one in the theorem.

**13.** At modulus 2 the two values cancel, so \(S_1=0\). At modulus 4, the even residues contribute 2 and the odd residues have phases \(i,-i\), so \(S_2=2\). At modulus 8, the four even residues have integral cube phase; the odd cubes permute the four odd residues, whose phases sum to zero. Thus \(S_3=4\). For \(l>3\), the unique critical class modulo 2 is zero. Substitution \(y=2z\) gives \(S_l=4S_{l-3}\), with the two extra lifts counted as in Lemma 5.16. Consequently \(S_l=0\) for \(l\equiv1\pmod3\), and \(S_l=2^{\lfloor2l/3\rfloor}\) otherwise. These values obey the uniform bound (5.48).

**14.** Put \(\lambda=F(T)\). The cubic \(f-\lambda g\) has zero constant at \(T\) and exact coefficient content \(\mu\). If it had larger content, its leading coefficient \(1-\lambda\) would too, and \(f-g=(f-\lambda g)+(\lambda-1)g\) would contradict the definition of \(\mu\). Its three positive coefficients therefore have minimum \(\mu\). Dividing by the unit constant and the integral reciprocal series of \(g(T+Z)\) acts triangularly with unit diagonal on the first three coefficients, so preserves that minimum. If the linear one attains the minimum, its logarithmic coefficient at depth 4 is strictly shallower than the cubic; the quadratic one has the same effect when the linear one has larger valuation. Thus cubic dominance requires that the third one attain the minimum, giving \(v_p(b_3)=\mu\) and \(\alpha=\mu+12\).

For the specified example, \(F(X)/F(0)=1-p^2X^3/(1+p^2)+O(X^6)\), so \(\mu=2\), \(\alpha=14\), and the initial remaining phase exponent is \(36-14=22\). At zero the linear and quadratic phase coefficients vanish. The cubic continuation therefore follows the zero class at every step. Its depths are \(4,5,6,7,8,9,10,11\), with remaining exponents \(22,19,16,13,10,7,4,1\). The terminal disc has depth 11, hence its normalized trivial upper-bound weight is \(p^{36/2-11}=p^7\). The witness modulus is \(p^{\mu+11}=p^{13}\); in fact \(F'(0)=F''(0)=0\) exactly. The weight is an upper bound. At the remaining exponent one the unit cubic phase is a nonzero linear phase on both \(\mathbf F_2\) and \(\mathbf F_3\), so that terminal sum is actually zero in this example.

**15.** At 2 the first-five conditions are \(b_1=b_2\), \(b_3=b_4\); at 3 they are \(b_1=b_3\), \(b_2=b_5\). Both subspaces have dimension three. The Chinese remainder theorem gives index \(2^2 3^2=36\), and \(2^3 3^3=216\) residues in the complete box. At either prime four vectors have dependent reductions, so all their four-by-four minors vanish modulo that prime; every such minor is therefore divisible by 6. The last shift satisfies \(b_6=b_5\pmod2\), \(b_6=b_4\pmod3\), a unique class modulo 6. These prescriptions are compatible by CRT regardless of whether the two integer values agree. This is exactly the varying-subspace setting of Lemma 5.22.

**16.** For the first three bounds divide \(W\) by \(L\) and use \(W/L\le\sqrt D\); their remaining powers are \(D^{-3},D^{-2},D^{-1}\), giving \(D^{-5/2},D^{-3/2},D^{-1/2}\). For the fourth and fifth substitute \(W\le HD^{1/3}U^{2/3}\), giving \(H^6U^{2/3}D^{-5/3}\) and \(H^5(U/D)^{2/3}\). The condition \(U<D\) bounds these by \(H^6\) and \(H^5\). The sixth uses \(W\le H^3\). Since \(H,D\ge1\), all six bounds are at most \(H^6\).

Here \(q=47376875\), and \(19^6<q\le20^6\), so \(H=20\). The exceptional divisor is \(D=13\cdot17=221\), while \(U=175\), \(L=1225\) and \(W=25\sqrt{221}\,7^{5/6}\). Thus \(D>U\), and the first-five lattice count (5.71) applies. The same interval height is used for every local factor; none of these choices requires a separate interval at a prime modulus.

## References

G. Pólya and I. M. Vinogradov independently proved the interval bound in 1918. I. Schur's 1918 completion argument gives an elementary finite-Fourier route. D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorems 10.5 and 10.6, gives character Poisson summation and Pólya–Vinogradov. Our Fourier transform uses the negative exponential and \(\tau\) the positive exponential; with the alternate coefficient \(\chi(-1)/\tau(\overline\chi)\), the identity \(\tau(\chi)\tau(\overline\chi)=\chi(-1)q\) converts that coefficient to \(\tau(\chi)/q\).

D. A. Burgess established the short-interval bound in his papers *On character sums and primitive roots* (1962) and *On character sums and L-series, II* (1963). The complete-sum argument here uses Weil's curve theorem through the exact internal lessons specified in Lemma 5.2. The divisor-average and induction organization may be compared with E. Hasanalizade, H. Lin, G. Martin, A. Luna Martínez and E. Treviño, [*Explicit Burgess inequalities for cubefree moduli*, version 2](https://arxiv.org/abs/2511.17778v2), Sections 2–6. That article is available under CC BY 4.0; its complete-sum Lemma 2.1 is cited there without proof. We have supplied the cubefree complete-sum argument above and have not imported its expression or asserted that it proves the arbitrary-conductor extension.

The exposition above supplies the quadratic root counts, the odd-exponent calculation including powers of 2, the prime-level collision case and the global singleton selection explicitly. Burgess's [*The character sum estimate with r = 3*](https://doi.org/10.1112/jlms/s2-33.2.219), 1986, is the historical source for the separate general-modulus r = 3 extension; its proof is not supplied by the fourth-moment calculation.

H. L. Montgomery and R. C. Vaughan, [*Exponential sums with multiplicative coefficients*](https://doi.org/10.1007/BF01390204), *Inventiones Mathematicae* 43 (1977), 69–82, established the GRH refinement of the maximal character-sum bound. The proof here supplies all of its analytic and arithmetic steps through the own-course explicit formula, an oscillatory zero-integral estimate, character expansion on the units of a smaller modulus, and the exact largest-prime-factor decomposition. The original paper is credited for the result; no estimate from its proof is used as an external substitute.

J. H. H. Chalk, [*On a Congruence Related to Character Sums*](https://doi.org/10.4153/CMB-1985-052-x), *Canadian Mathematical Bulletin* 28 (1985), 431–439, develops the cubic-pencil treatment of stationary congruences. The independently written Lemma 5.10 gives an explicit classification inside each residue class and proves the bound needed for that classification, without importing a polynomial-congruence theorem. Chalk's [*On Incomplete Character Sums to a Prime-Power Modulus*](https://doi.org/10.4153/CMB-1987-037-4), 30 (1987), 257–266, was consulted for the separate class-phase and arithmetic-averaging stages. Lemmas 5.11–5.13 and Proposition 5.14 supply the full class-phase estimates for primes greater than 3 from the stated curve prerequisites and an elementary recursion. Chalk's arithmetic count invokes Burgess's separate theorem. Lemmas 5.19–5.21 here instead supply the critical-value and determinant arguments in full; Lemmas 5.22–5.23 count all prime-level root-coincidence patterns, and Proposition 5.24 assembles the full weighted average at every conductor. Lemmas 5.15–5.17 and Proposition 5.18 supply the small-prime additive phases, logarithmic-disc coefficients and derivative-witness envelope in full, so the assembly includes arbitrary powers of 2 and 3. The lattice packing argument and the split according to the two arithmetic divisors supply the remaining mixed-conductor step in full. Theorem 5.25 then proves the arbitrary-conductor r=3 interval bound using the already established shift induction.

The only valued-field input to Lemma 5.19 is supplied by the written internal lessons of *Local fields*: “Completions, the p-adic numbers and complete discretely valued fields,” Theorem 2.1, and “Extensions of complete valued fields,” Theorem 1.2 and Proposition 2.1. Their arguments construct the completion, extend its valuation to finite splitting fields, and establish completeness. The Gauss-content identity, finite-numerator estimate, critical-value cardinality and all arithmetic counting are proved in this lesson.
