# Real zeros and the prime bias

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a primitive Dirichlet character \(\chi\) of conductor \(q\), the classical zero-free region excludes zeros of \(L(s,\chi)\) with \(\operatorname{Re}s\ge1-c/\log(q(|\operatorname{Im}s|+2))\), for an absolute constant \(c>0\), with one possible exception: a simple real zero of a real character. This is Theorem 5.1 of [Zero-free regions and the exceptional zero](course:NT-DIRL/NT-DIRL-07#5-the-classical-product-region). Such a zero, if it exists, is called a *Landau–Siegel zero* or an *exceptional zero*. Three classical results limit how such zeros can occur.

- Page's theorem: for an absolute constant \(c_P>0\) and every \(Q\ge3\), at most one real primitive character of conductor at most \(Q\) has a real zero in \((1-c_P/\log Q,1)\). This is Corollary 4.2 of [Zero-free regions and the exceptional zero](course:NT-DIRL/NT-DIRL-07#4-landau-page-and-sparsity-of-conductors).
- An effective bound: an exceptional zero \(\beta\) satisfies \(1-\beta\gg q^{-1/2}(\log q)^{-2}\), Theorem 6.2 of the same lesson.
- Siegel's theorem of 1935: \(L(1,\chi)>c(\varepsilon)q^{-\varepsilon}\) for every \(\varepsilon>0\), with a constant \(c(\varepsilon)\) that the proof does not compute. This is Theorem 5.1 of [Siegel's theorem](course:NT-DIRL/NT-DIRL-10#5-absorbing-the-possible-exception).

None of them excludes a sequence of real characters with real zeros \(\beta\) for which \((1-\beta)\log q\to0\). Excluding such sequences is the logarithmic form of the Landau–Siegel problem.

## The theorem

This course proves the following theorem of OpenAI [OpenAI-LS].

**Theorem A** (OpenAI). There is an absolute constant \(c>0\) such that every real zero \(\beta\in(0,1)\) of the \(L\)-function of every primitive nonprincipal real Dirichlet character of conductor \(q\ge3\) satisfies
\[
(1-\beta)\log q\ge c .
\]

With the classical region it gives a zero-free region with no exception, Corollary B in [Two bounds for the determinant](two-bounds-for-the-determinant.md). The proof combines a short analytic lemma, proved in this lesson, with an algebraic argument: a determinant in the biquadratic field \(\mathbf Q(\sqrt d,\sqrt2)\) is divisible by more prime powers than its absolute value allows. The analytic lemma says that a real zero close to \(1\) leaves few primes with \(\chi(p)=1\). The algebraic argument uses the primes with \(\chi(p)=-1\), at which the Frobenius congruence \(\theta^p\equiv\sigma(\theta)\) or \(\theta^p\equiv\sigma\tau(\theta)\) holds in the ring \(\mathbf Z[\sqrt d,\sqrt2]\).

Banks [Banks] gives a detailed account of this proof with explicit constants: \((1-\beta)\log q\ge3.0\cdot10^{-3}\) for \(q\ge10^{10}\), and, with a computation of Lu, Zaman and Zhao for the smaller conductors, for all \(q\ge3\). Kerr [Kerr] gives a shorter proof in which a polynomial obtained by the pigeonhole principle, together with a zero estimate of Masser, replaces the interpolation determinant. Kimura [Kimura] makes the argument explicit with the constant \(5.8\cdot10^{-4}\) for all \(q\ge3\), checks its two main steps in Lean, and deduces the list of all imaginary quadratic fields of class number at most \(2000\). The same release of OpenAI contains manuscripts that state the zero-free half-plane \(\operatorname{Re}s>7/8\) for every Dirichlet \(L\)-function [OpenAI-QRH]. Such a half-plane gives Theorem A with \(c=(\log3)/8\), since it forces \(\beta\le7/8\), and \(q\ge3\). Those manuscripts are not treated in this course.

**The course.**

1. This lesson: the bias of the primes forced by a real zero close to \(1\), and the plan of the proof.
2. [Interpolation on a projected integer box](interpolation-on-a-projected-integer-box.md): polynomials with separately bounded degrees take arbitrary values on a linear image of an integer box in \(\mathbf C^4\).
3. [A weighted determinant in a biquadratic field](a-weighted-determinant-in-a-biquadratic-field.md): a nonzero determinant of products of conjugates, chosen so that most of its degree lies in one conjugate.
4. [Two bounds for the determinant](two-bounds-for-the-determinant.md): an upper bound from Hadamard's inequality, a lower bound from the Frobenius congruence, and the proof of Theorem A.

**What the course assumes.** Complex analysis and the theory of Dirichlet \(L\)-functions as developed in the programme courses *The Riemann zeta function* and *Dirichlet L-functions and primes in progressions*; each result used is cited at the place of use. Linear algebra over a field, including determinants and Hadamard's inequality. The convex geometry used in the second lesson is proved there.

## 1. Notation and inputs

Throughout, \(\chi\) is a primitive nonprincipal real Dirichlet character of conductor \(q\). By Theorem 4.1 of [Dirichlet characters](course:NT-DIRL/NT-DIRL-01#4-real-characters-and-quadratic-discriminants), \(\chi(n)\) is the Kronecker symbol \((D/n)\) of a fundamental discriminant \(D\ne1\) with \(|D|=q\), and \(\chi(-1)=\operatorname{sgn}D\). In particular \(q\ge3\), and \(\chi(p)=0\) exactly for the primes \(p\mid q\). Write \(\chi(-1)=(-1)^{\mathfrak a}\) with \(\mathfrak a\in\{0,1\}\). Let \(\beta\in(0,1)\) be a real zero of \(L(s,\chi)\), and put
\[
\ell=\log q,\qquad \delta=(1-\beta)\ell .
\]
Then \(\ell\ge\log3>1\). We use the following results of the programme.

- (I1) For \(\operatorname{Re}s>1\),
\[
\begin{aligned}
-\frac{\zeta'}{\zeta}(s)&=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\\
-\frac{L'}{L}(s,\chi)&=\sum_{n\ge1}\frac{\Lambda(n)\chi(n)}{n^s}.
\end{aligned}
\]
The first formula is Proposition 3.1 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01#3-three-ways-to-read-the-primes-in-zeta). The second follows in the same way by differentiating the logarithm (1.2) of \(L(s,\chi)\) in [Dirichlet's theorem on primes in arithmetic progressions](course:NT-DIRL/NT-DIRL-02#1-why-a-value-at-1-matters) term by term.
- (I2) The product formula (4.6), with \(\operatorname{Re}B(\chi)=-\sum_\rho\operatorname{Re}(1/\rho)\) from (4.3), in Proposition 4.1 of [The functional equation of Dirichlet L-functions](course:NT-DIRL/NT-DIRL-05#4-the-entire-function-product-and-its-constant):
\[
\begin{aligned}
\frac{L'}{L}(s,\chi)={}&B(\chi)-\frac12\log\frac q\pi\\
&-\frac12\frac{\Gamma'}{\Gamma}\Bigl(\frac{s+\mathfrak a}2\Bigr)\\
&+\sum_\rho\Bigl(\frac1{s-\rho}+\frac1\rho\Bigr).
\end{aligned}
\]
Here \(\rho\) runs over the nontrivial zeros with multiplicity, all of which satisfy \(0<\operatorname{Re}\rho<1\), and the zeros in \(\operatorname{Re}s\le0\) are the trivial zeros on the real axis at \(-\mathfrak a,-\mathfrak a-2,\dots\) [same lesson, Section 3](course:NT-DIRL/NT-DIRL-05#3-where-the-zeros-can-be). So \(\beta\) is a nontrivial zero.
- (I3) For real \(z>0\), \(\frac{\Gamma'}{\Gamma}(z)=-\gamma+\sum_{n\ge0}\bigl(\frac1{n+1}-\frac1{n+z}\bigr)\), and \(\frac{\Gamma'}{\Gamma}(1/2)=-\gamma-2\log2\): Proposition 5.1 of [The Gamma function and Stirling's formula](course:NT-ZETA/NT-ZETA-03#logarithmic-derivatives-and-a-continuous-phase).
- (I4) For \(\operatorname{Re}s>0\), \(s\ne1\), \(\zeta(s)=\frac s{s-1}-s\int_1^\infty\{u\}u^{-s-1}\,du\): Theorem 5.1 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01#5-subtracting-the-pole-of-zeta).
- (I5) Mertens' estimate \(\sum_{p\le x}(\log p)/p=\log x+O(1)\) for \(x\ge2\), Theorem 3.1 of [Counting primes by elementary means: Chebyshev and Mertens](course:NT-ZETA/NT-ZETA-02#3-factorials-determine-reciprocal-prime-averages). Fix an absolute constant \(c_M\ge0\) such that, for every \(x\ge2\),
\[
\Bigl|\sum_{p\le x}\frac{\log p}p-\log x\Bigr|\le c_M .
\]
- (I6) For a nonprincipal character, \(L(s,\chi)\) is holomorphic on \(\operatorname{Re}s>0\), by (2.1) of [Dirichlet's theorem on primes in arithmetic progressions](course:NT-DIRL/NT-DIRL-02#2-periodicity-gives-continuation), and \(L(1,\chi)>0\) when \(\chi\) is real, by Theorem 3.4 of the same lesson.

## 2. Two logarithmic derivatives on the real axis

**Lemma 1.1.** For real \(s>1\),
\[
-\frac{\zeta'}{\zeta}(s)<\frac1{s-1}+1 .
\]

*Proof.* Put \(I(s)=\int_1^\infty\{u\}u^{-s-1}\,du\) and \(F(s)=(s-1)\zeta(s)=s-s(s-1)I(s)\), by (I4). For real \(s>1\), \(0\le\{u\}<1\) gives \(0\le I(s)\le\int_1^\infty u^{-s-1}\,du=1/s\), hence \(F(s)\ge s-(s-1)=1\). The integral may be differentiated under the integral sign, as in the proof of (I4), and
\[
I'(s)=-\int_1^\infty\{u\}(\log u)\,u^{-s-1}\,du\le0 .
\]
Therefore
\[
\begin{aligned}
-F'(s)&=-1+(2s-1)I(s)\\
&\quad+s(s-1)I'(s)\\
&\le-1+\frac{2s-1}s=\frac{s-1}s<1 .
\end{aligned}
\]
Since \(\zeta(s)=F(s)/(s-1)\),
\[
-\frac{\zeta'}{\zeta}(s)=\frac1{s-1}-\frac{F'(s)}{F(s)} .
\]
If \(-F'(s)\ge0\), then \(-F'(s)/F(s)\le-F'(s)<1\) because \(F(s)\ge1\); otherwise \(-F'(s)/F(s)<0\). \(\square\)

**Lemma 1.2.** For real \(1<s\le2\),
\[
-\frac{L'}{L}(s,\chi)\le\frac12\ell-\frac1{s-\beta} .
\]

*Proof.* For real \(s>1\) the Euler product shows that \(L(s,\chi)\) is real and nonzero, so \(L'/L(s,\chi)\) is real, and so is \(\frac{\Gamma'}{\Gamma}((s+\mathfrak a)/2)\). Take real parts in (I2). The series \(\sum_\rho\operatorname{Re}(1/\rho)\) converges absolutely, so subtracting it term by term from \(\sum_\rho\operatorname{Re}(1/(s-\rho)+1/\rho)\) gives
\[
\begin{aligned}
-\frac{L'}{L}(s,\chi)={}&\frac12\log\frac q\pi+\frac12\frac{\Gamma'}{\Gamma}\Bigl(\frac{s+\mathfrak a}2\Bigr)\\
&-\sum_\rho\operatorname{Re}\frac1{s-\rho} .
\end{aligned}
\]
Each term satisfies
\[
\operatorname{Re}\frac1{s-\rho}=\frac{s-\operatorname{Re}\rho}{|s-\rho|^2}>0,
\]
since \(\operatorname{Re}\rho<1<s\). Keeping only one term for the zero \(\beta\) gives
\[
\begin{aligned}
-\frac{L'}{L}(s,\chi)\le{}&\frac12\log\frac q\pi+\frac12\frac{\Gamma'}{\Gamma}\Bigl(\frac{s+\mathfrak a}2\Bigr)\\
&-\frac1{s-\beta} .
\end{aligned}
\]
By (I3), every term of the series for \(\Gamma'/\Gamma\) increases with \(z\), so \(\Gamma'/\Gamma\) is increasing on \((0,\infty)\). Comparing the series at \(z\) and \(z+1\) term by term gives \(\frac{\Gamma'}{\Gamma}(z+1)=\frac{\Gamma'}{\Gamma}(z)+\frac1z\), a telescoping sum. As \(1/2<(s+\mathfrak a)/2\le3/2\),
\[
\begin{aligned}
\frac{\Gamma'}{\Gamma}\Bigl(\frac{s+\mathfrak a}2\Bigr)&\le\frac{\Gamma'}{\Gamma}\Bigl(\frac32\Bigr)\\
&=2-\gamma-2\log2<0.04 .
\end{aligned}
\]
Finally \(\frac12\log\pi>0.57>0.02\). \(\square\)

## 3. The prime bias

**Proposition 1.3** (OpenAI). For every real \(X\ge3\),
\[
\sum_{\substack{p\le X\\ \chi(p)=1}}\frac{\log p}p\le e\Bigl(\ell+\frac{\delta(\log X)^2}{\ell}\Bigr).
\]

*Proof.* Put \(s=1+1/\log X\); then \(1<s<2\). By (I1),
\[
\begin{aligned}
&-\frac{\zeta'}{\zeta}(s)-\frac{L'}{L}(s,\chi)\\
&\quad=\sum_{n\ge1}\frac{\Lambda(n)(1+\chi(n))}{n^s} .
\end{aligned}
\]
Every term is nonnegative, since \(\chi\) is real. For a prime \(p\le X\) with \(\chi(p)=1\) the term is \(2(\log p)p^{-s}\ge(2/e)(\log p)/p\), because \(p^{s-1}=p^{1/\log X}\le e\). Lemmas 1.1 and 1.2 therefore give
\[
\begin{aligned}
\frac2e\sum_{\substack{p\le X\\ \chi(p)=1}}\frac{\log p}p&<1+\frac12\ell\\
&\quad+\frac1{s-1}-\frac1{s-\beta} .
\end{aligned}
\]
Since \(s-\beta>s-1\),
\[
\begin{aligned}
\frac1{s-1}-\frac1{s-\beta}&=\frac{1-\beta}{(s-1)(s-\beta)}\\
&\le\frac{1-\beta}{(s-1)^2}\\
&=\frac{\delta(\log X)^2}{\ell} .
\end{aligned}
\]
Hence the sum is at most \(\frac e2(1+\frac12\ell+x)\) with \(x=\delta(\log X)^2/\ell\). This is at most \(e(\ell+x)\), because \(1\le\frac32\ell+x\). \(\square\)

For \(X=q^A\) the bound reads \(e(1+A^2\delta)\ell\), while all primes up to \(X\) carry the mass \(A\ell+O(1)\) by (I5). So if \(\delta\) is small compared with \(A^{-2}\), the primes with \(\chi(p)=1\) carry at most a fraction of order \(1/A\) of the mass up to \(q^A\).

**Corollary 1.4.** For every integer \(H\ge2\) and real \(X\ge3\),
\[
\begin{aligned}
&\sum_{\substack{H<p\le X\\ p\nmid2q,\ \chi(p)=-1}}\frac{\log p}p\\
&\quad\ge\log X-4\ell-\frac{3\delta(\log X)^2}{\ell}\\
&\qquad-\log H-2c_M .
\end{aligned}
\]

*Proof.* Split the primes \(p\le X\) into those dividing \(2q\), those with \(p\nmid2q\) and \(\chi(p)=1\), and those with \(p\nmid2q\) and \(\chi(p)=-1\); every prime \(p\nmid q\) has \(\chi(p)=\pm1\). By (I5) all of them together carry at least \(\log X-c_M\). The primes dividing \(2q\) carry at most
\[
\begin{aligned}
&\frac{\log2}2+\sum_{p\mid q}\frac{\log p}p\\
&\quad\le\frac{\log2}2+\frac12\sum_{p\mid q}\log p\le0.35+\frac12\ell,
\end{aligned}
\]
and the primes with \(\chi(p)=1\) at most \(e(\ell+\delta(\log X)^2/\ell)\), by Proposition 1.3. Removing the primes \(p\le H\) costs at most \(\log H+c_M\), by (I5). The claim follows, because \(0.35\le0.32\,\ell\), \(\frac12+e+0.32<4\) and \(e<3\). \(\square\)

## 4. Real zeros of bounded conductor

**Lemma 1.5.** For every \(Q\ge3\) there is \(\eta_Q>0\) such that no \(L(s,\chi)\), for \(\chi\) primitive, nonprincipal and real of conductor at most \(Q\), vanishes on the interval \([1-\eta_Q,1]\).

*Proof.* There are finitely many such characters, since there are finitely many characters modulo each \(q\le Q\). For each of them \(L(s,\chi)\) is continuous on \((0,\infty)\) and \(L(1,\chi)>0\), by (I6). So \(L(\sigma,\chi)>0\) on an interval \([1-\eta_\chi,1]\) with \(\eta_\chi>0\). Let \(\eta_Q\) be the least of the \(\eta_\chi\). \(\square\)

**Corollary 1.6.** If Theorem A is false, there are primitive nonprincipal real characters \(\chi_k\), of conductors \(q_k\), with real zeros \(\beta_k\in(0,1)\) such that
\[
q_k\to\infty,\qquad \delta_k=(1-\beta_k)\log q_k\to0 .
\]

*Proof.* If Theorem A is false, then for every \(k\ge1\) there are \(\chi_k\) and \(\beta_k\) with \(\delta_k<1/k\). If the \(q_k\) were bounded by some \(Q\) along a subsequence, Lemma 1.5 would give \(1-\beta_k\ge\eta_Q\), hence \(\delta_k\ge\eta_Q\log3\), along it. \(\square\)

## 5. The plan of the proof

Suppose \(\delta\) is small. By Corollary 1.4 with \(X=q^A\) for a large fixed \(A\), the primes \(p\le X\) with \(\chi(p)=-1\) carry nearly all of the logarithmic mass \(\log X\). The remaining lessons turn this into a contradiction.

Let \(d\) be the squarefree integer with \(\mathbf Q(\sqrt D)=\mathbf Q(\sqrt d)\), and let \(K=\mathbf Q(\sqrt d,\sqrt2)\); apart from \(d=2\) this field has degree \(4\). Let \(\sigma\) change the sign of \(\sqrt d\), and \(\tau\) the sign of \(\sqrt2\). For \(n\in\{0,\dots,N-1\}^4\) put \(\theta_n=n_1+n_2\sqrt d+n_3\sqrt2+n_4\sqrt{2d}\). For exponents \(\alpha\in\mathbf Z_{\ge0}^3\), the vectors
\[
\bigl(\theta_n^{\alpha_1}\,\sigma(\theta_n)^{\alpha_2}\,\sigma\tau(\theta_n)^{\alpha_3}\bigr)_n
\]
have \(N^4\) entries. The second lesson shows that enough of them span; the third chooses \(N^4\) of them by increasing weight \(\alpha_1+H\alpha_2+H\alpha_3\), so that their determinant \(\Delta\) is a nonzero element of \(\mathbf Z[\sqrt d,\sqrt2]\) whose degree lies mostly in \(\alpha_1\). The fourth lesson bounds the norm of \(\Delta\) twice.

- From above, by Hadamard's inequality: \(\theta_n\) has size about \(N\sqrt q\), and the main term is \(\log N\) per unit of degree.
- From below, by divisibility: at a prime \(p>H\) with \(\chi(p)=-1\), \(\theta^p\equiv\sigma(\theta)\) or \(\sigma\tau(\theta)\) modulo \(p\), and row operations extract a factor \(p\) from every block of \(p\) units of the exponent \(\alpha_1\). The primes up to \(U=N^{4/3}\) contribute about \(\log U\) per unit of \(\alpha_1\).

Since \(N^4=U^3\), the upper bound has \(\log N=\frac34\log U\) where the lower bound has \(\log U\). The factor \(\frac34\) comes from four coordinates of \(n\) against three conjugates in each row, and it is the gap that the argument exploits. The term \(\frac12\log q\) per unit of degree in the upper bound is made small by taking \(N\) a large power of \(q\).

## 6. Exercises

**1.1** (easy). Let \(A\ge1\) and suppose \(\delta\le A^{-2}\). Show that the primes \(p\le q^A\) with \(\chi(p)=1\) carry at most \(2e\ell\) of the logarithmic mass, while all primes up to \(q^A\) carry at least \(A\ell-c_M\).

**1.2** (medium). Show that \(-\frac{\zeta'}{\zeta}(s)-\frac1{s-1}\to-\gamma\) as \(s\to1^+\), where \(\gamma\) is Euler's constant. So the constant \(1\) in Lemma 1.1 cannot be replaced by a number below \(-\gamma\).

**1.3** (medium). Show that \(1-\beta\) is also a zero of \(L(s,\chi)\). Deduce that, if \(\beta\ne\frac12\), the bound of Lemma 1.2 improves to \(\frac12\ell-\frac1{s-\beta}-\frac1{s-1+\beta}\).

**1.4** (easy). Show from the definition of fundamental discriminants that \(8\) is the only fundamental discriminant \(D\) with \(\mathbf Q(\sqrt D)=\mathbf Q(\sqrt2)\). Thus the field \(K\) of Section 5 has degree \(4\) whenever \(q\ne8\).

## 7. Solutions

**1.1.** With \(X=q^A\), Proposition 1.3 gives at most \(e(\ell+A^2\delta\ell)\le2e\ell\). By (I5), \(\sum_{p\le q^A}(\log p)/p\ge A\ell-c_M\).

**1.2.** Let \(F(s)=(s-1)\zeta(s)\), holomorphic near \(1\) by (I4). Since \(F(s)=1+(s-1)\bigl(\zeta(s)-\frac1{s-1}\bigr)\) and \(\zeta(s)-\frac1{s-1}\to\gamma\) by Theorem 5.1 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01#5-subtracting-the-pole-of-zeta), \(F(1)=1\) and \(F'(1)=\gamma\). Hence \(-\frac{\zeta'}{\zeta}(s)-\frac1{s-1}=-\frac{F'(s)}{F(s)}\to-\gamma\).

**1.3.** The reflection \(\rho\mapsto1-\overline\rho\) maps nontrivial zeros to nontrivial zeros of the same multiplicity, by Theorem 3.2 of [The functional equation of Dirichlet L-functions](course:NT-DIRL/NT-DIRL-05#3-where-the-zeros-can-be). For the real zero \(\beta\) it gives the zero \(1-\beta\). If \(\beta\ne\frac12\), the two zeros are different, and the proof of Lemma 1.2 can keep both terms.

**1.4.** A fundamental discriminant is either a squarefree \(D\equiv1\pmod4\), or \(D=4m\) with \(m\) squarefree and \(m\equiv2,3\pmod4\). The field \(\mathbf Q(\sqrt D)\) equals \(\mathbf Q(\sqrt{D'})\), where \(D'\) is the squarefree part of \(D\), that is \(D\) or \(m\). Two squarefree integers define the same quadratic field only if they are equal, so \(D'=2\). As \(2\not\equiv1\pmod4\), \(D=4\cdot2=8\).

## References

- [OpenAI-LS] OpenAI, *Uniform exclusion of Landau–Siegel zeros*, OpenAI Math Release preprint, 1 October 2026. https://github.com/openai/math/tree/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026
- [OpenAI-QRH] OpenAI, *The quasi-Riemann hypothesis: a zero-free half-plane Re s > 7/8*, 30 September 2026, https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026, and *The quasi-Riemann hypothesis (alternate 11/12 proof)*, 5 October 2026, https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026. OpenAI Math Release preprints.
- [Banks] W. D. Banks, *On the OpenAI proof that Landau–Siegel zeros do not exist*, arXiv:2610.15483, October 2026. https://arxiv.org/abs/2610.15483
- [Kerr] B. Kerr, *A simpler proof that there are no Landau–Siegel zeros*, arXiv:2610.21099, October 2026. https://arxiv.org/abs/2610.21099
- [Kimura] I. Kimura, *Imaginary quadratic fields of class number at most 2000*, arXiv:2610.21511, October 2026. https://arxiv.org/abs/2610.21511
