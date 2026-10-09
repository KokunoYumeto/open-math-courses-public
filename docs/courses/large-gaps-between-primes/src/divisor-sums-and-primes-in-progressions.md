# Divisor sums and primes in progressions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The weights of [Prime gaps and adjacent intervals](prime-gaps-and-adjacent-intervals.md) are built from smooth divisor sums: Möbius-weighted sums over divisors of the shifted integers \(m+b\), cut off smoothly at a small power of \(X\). Their moments are averages over \(X<m\le2X\) of products of such sums, sometimes multiplied by \(\vartheta(m+a)\), which detects a prime at a further shift \(a\). This lesson replaces every such average by an explicit finite sum, the density sum, with an error smaller than any fixed power of \(1/\log X\). Without the prime factor the replacement is elementary counting in residue classes. With it, the replacement is an application of the Bombieri–Vinogradov theorem, extended here to intervals with moving endpoints and to moduli weighted by \(K^{\omega(q)}\).

We use the Möbius function and the identity \(\sum_{d\mid n}\mu(d)=[n=1]\), Lemma 2.0 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01#2-multiplication-remembers-factorization); Mertens's estimate \(\sum_{p\le x}1/p=\log\log x+O(1)\), Theorem 3.1 of [Counting primes by elementary means](course:NT-ZETA/NT-ZETA-02#3-factorials-determine-reciprocal-prime-averages); and the Bombieri–Vinogradov theorem for \(\theta\), Corollary 4.1 of [The Bombieri–Vinogradov theorem](course:NT-DIRL/NT-DIRL-15#4-prime-weights-prime-counts-and-exceptional-moduli). Notation: \(X\) is an integer tending to infinity, \(L=\log X\), \(\mathbb E_X\) is the average over \(X<m\le2X\), \(\vartheta(n)=\log n\) for prime \(n\) and \(0\) otherwise, \(\omega(q)\) is the number of prime factors of \(q\) and \(\varphi\) is Euler's function.

## 1. Smooth divisor sums

**Definition 1.1.** Let \(j\ge1\) and \(\rho\ge0\). A *test function of dimension \(j\) and budget \(\rho\)* is a real function \(F\) on the closed orthant \([0,\infty)^j\) which is the restriction of a smooth compactly supported function on \(\mathbb R^j\) and satisfies \(F(v)=0\) whenever \(v_1+\dots+v_j>\rho\). A test function of dimension \(0\) is a real number, with budget \(0\).

**Definition 1.2.** For a test function \(F\) of dimension \(j\), an integer \(m\) and integer shifts \(\mathbf b=(b_1,\dots,b_j)\) with all \(m+b_i\ge1\),

\[
D_F(m;\mathbf b)=\sum_{d_1\mid m+b_1}\cdots\sum_{d_j\mid m+b_j}\mu(d_1)\cdots\mu(d_j)\,F\Bigl(\frac{\log d_1}L,\dots,\frac{\log d_j}L\Bigr),
\]

the sums running over positive divisors. For \(j=0\), \(D_F=F\).

Only squarefree \(d_i\) contribute, because of the Möbius factors, and only tuples with \(d_1\cdots d_j\le X^\rho\), because of the budget: \(F\) vanishes once \(\sum_i\log d_i/L>\rho\). So \(D_F(m;\mathbf b)\) is a finite sum over small divisors, and \(|D_F(m;\mathbf b)|\le\|F\|_\infty\prod_i\tau(m+b_i)\), where \(\tau\) counts divisors.

For \(j=1\) and \(F(0)=1\), the sum \(D_F(m;b)\) is a smoothed version of \(\sum_{d\mid m+b}\mu(d)\), which is \(1\) if \(m+b=1\) and \(0\) otherwise. If \(m+b\) has no prime factor up to \(X^\rho\), only \(d=1\) survives and \(D_F(m;b)=F(0)=1\). Squares of such sums are therefore large on integers whose shifts are free of small prime factors. This is how they detect prime tuples, as in the work of Selberg and of Goldston, Pintz and Yıldırım.

The budget gives an exact rule for a coordinate whose shifted integer is a large prime.

**Lemma 1.3** (a prime coordinate). Let \(F\) have dimension \(j\ge1\) and budget \(\rho\), and suppose \(m+b_j\) is a prime with \(\log(m+b_j)/L>\rho\). Then

\[
D_F(m;b_1,\dots,b_j)=D_{F(\cdot,0)}(m;b_1,\dots,b_{j-1}),
\]

where \(F(\cdot,0)(v_1,\dots,v_{j-1})=F(v_1,\dots,v_{j-1},0)\) is a test function of dimension \(j-1\) and budget \(\rho\).

**Proof.** The divisors of the prime \(m+b_j\) are \(1\) and \(m+b_j\). A term with \(d_j=m+b_j\) evaluates \(F\) at a point of the orthant whose last coordinate exceeds \(\rho\), so the coordinate sum exceeds \(\rho\) and the term vanishes. The terms with \(d_j=1\) form the right side. The restriction \(F(\cdot,0)\) is smooth, compactly supported after the same extension, and vanishes when \(v_1+\dots+v_{j-1}>\rho\). \(\square\)

## 2. Three elementary estimates

**Lemma 2.1** (counting tuples). For \(M\ge1\) and \(Y\ge1\), the number of \(M\)-tuples of positive integers with \(d_1\cdots d_M\le Y\) is at most \(Y(1+\log Y)^{M-1}\).

**Proof.** Fix \(d_1,\dots,d_{M-1}\) with product \(P\le Y\). There are at most \(Y/P\) choices of \(d_M\). Summing, and enlarging each of the first \(M-1\) ranges to \([1,Y]\), the count is at most \(Y\bigl(\sum_{d\le Y}1/d\bigr)^{M-1}\le Y(1+\log Y)^{M-1}\). \(\square\)

**Lemma 2.2.** For every \(T\ge1\) there is \(C_T\) such that for \(Q\ge3\)

\[
\sum_{q\le Q}\frac{\mu^2(q)T^{\omega(q)}}q\le\prod_{p\le Q}\Bigl(1+\frac Tp\Bigr)\le C_T(\log Q)^T .
\]

**Proof.** Every squarefree \(q\le Q\) is a product of distinct primes \(p\le Q\), and \(\mu^2(q)T^{\omega(q)}/q\) is the product of \(T/p\) over those primes; so the sum is at most the expanded product. Then \(\log\prod_{p\le Q}(1+T/p)\le T\sum_{p\le Q}1/p=T\log\log Q+O(T)\) by Mertens's estimate. \(\square\)

**Lemma 2.3.** For squarefree \(q\), \(q/\varphi(q)=\prod_{p\mid q}p/(p-1)\le2^{\omega(q)}\).

**Proof.** Each factor \(p/(p-1)\) is at most \(2\). \(\square\)

## 3. The Bombieri–Vinogradov theorem with moving endpoints

Fix \(D>0\) and \(B\ge0\), and put \(H_X=DL^B\). For \(q\ge1\) define

\[
E_X(q)=\max_{\substack{a\in\mathbb Z\\|a|\le H_X}}\ \max_{(c,q)=1}\ \Bigl|\sum_{\substack{X+a<n\le2X+a\\n\equiv c\ (\mathrm{mod}\ q)}}\vartheta(n)-\frac X{\varphi(q)}\Bigr| .
\]

**Proposition 3.1.** Fix \(0\le\sigma<1/2\), \(K\ge1\) and \(A>0\). Then

\[
\sum_{q\le X^\sigma}\mu^2(q)\,K^{\omega(q)}\,E_X(q)\ll_{\sigma,K,A,D,B}XL^{-A}.
\]

**Proof.** *Step 1: reduction to fixed cutoffs.* Write \(\theta(y;q,c)=\sum_{p\le y,\ p\equiv c}\log p\) and

\[
E_\theta(x,q)=\max_{0\le y\le x}\ \max_{(c,q)=1}\Bigl|\theta(y;q,c)-\frac y{\varphi(q)}\Bigr|,
\]

as in (0.1) of the Bombieri–Vinogradov lesson. For large \(X\) we have \(H_X\le X\), so for \(|a|\le H_X\) both endpoints \(X+a\) and \(2X+a\) lie in \([0,3X]\). The sum in the definition of \(E_X(q)\) equals \(\theta(2X+a;q,c)-\theta(X+a;q,c)\), and

\[
\theta(2X+a;q,c)-\theta(X+a;q,c)-\frac X{\varphi(q)}=\Bigl[\theta(2X+a;q,c)-\frac{2X+a}{\varphi(q)}\Bigr]-\Bigl[\theta(X+a;q,c)-\frac{X+a}{\varphi(q)}\Bigr].
\]

Hence \(E_X(q)\le2E_\theta(3X,q)\). Corollary 4.1 of the Bombieri–Vinogradov lesson, (4.2), states that for every \(A_0>0\), \(\sum_{q\le Q}E_\theta(x,q)\ll_{A_0}x(\log x)^{-A_0}\) whenever \(1\le Q\le\sqrt x/(\log x)^{A_0+3}\). Since \(\sigma<1/2\), the choice \(x=3X\), \(Q=X^\sigma\) is admissible for large \(X\), and

\[
\sum_{q\le X^\sigma}E_X(q)\ll_{A_0}XL^{-A_0}.
\tag{3.1}
\]

*Step 2: a trivial bound.* Let \(q\le X^\sigma\) be squarefree. An interval of length \(X\) contains at most \(X/q+1\le2X/q\) integers of one residue class, each with \(\vartheta(n)\le\log(3X)\le2L\). By Lemma 2.3, \(X/\varphi(q)\le2^{\omega(q)}X/q\). Hence

\[
E_X(q)\le\frac Xq\bigl(4L+2^{\omega(q)}\bigr)\le\frac{5L\,2^{\omega(q)}X}q .
\tag{3.2}
\]

*Step 3: Cauchy–Schwarz.* For nonnegative numbers \(E_X(q)\),

\[
\Bigl(\sum_{q\le X^\sigma}\mu^2(q)K^{\omega(q)}E_X(q)\Bigr)^2\le\sum_{q\le X^\sigma}E_X(q)\cdot\sum_{q\le X^\sigma}\mu^2(q)K^{2\omega(q)}E_X(q).
\]

By (3.2) and Lemma 2.2 with \(T=2K^2\), the second factor is at most \(5LX\sum_{q\le X^\sigma}\mu^2(q)(2K^2)^{\omega(q)}/q\ll_KXL^{1+2K^2}\). With (3.1) for \(A_0=2A+1+2K^2\), the product is \(\ll X^2L^{-2A}\). \(\square\)

## 4. The exact density sum

The following data are fixed while \(X\to\infty\): a number \(R\ge1\) of factors; dimensions \(j_1,\dots,j_R\ge0\); test functions \(F_r\) of dimension \(j_r\) and budget \(\rho_r\); constants \(D>0\), \(B\ge0\); and \(\delta\in\{0,1\}\). Let \(\Gamma=\{(r,\ell):1\le r\le R,\ 1\le\ell\le j_r\}\) be the set of divisor coordinates, \(M=|\Gamma|\), and \(\sigma=\rho_1+\dots+\rho_R\). Assume

\[
\sigma<1\ \text{ if }\delta=0,\qquad\sigma<\tfrac12\ \text{ if }\delta=1 .
\]

The shifts may vary with \(X\): integers \(b_\gamma\) for \(\gamma\in\Gamma\) with \(|b_\gamma|\le H_X\), and, if \(\delta=1\), a mark \(a_0\) with \(|a_0|\le H_X\) and \(a_0\ne b_\gamma\) for all \(\gamma\). Write \(\mathbf b^{(r)}=(b_{r,1},\dots,b_{r,j_r})\) and

\[
\chi_\delta(m)=\begin{cases}1,&\delta=0,\\\vartheta(m+a_0),&\delta=1.\end{cases}
\]

**Definition 4.1.** For a tuple \(\mathbf d=(d_\gamma)_{\gamma\in\Gamma}\) of squarefree positive integers, let \(q=\operatorname{lcm}(d_\gamma)\), with \(q=1\) if \(M=0\). The tuple is *compatible* if for every prime \(p\mid q\) the shifts \(b_\gamma\) with \(p\mid d_\gamma\) are all congruent modulo \(p\), and, when \(\delta=1\), their common residue differs from \(a_0\) modulo \(p\). Put

\[
\rho_\delta(\mathbf d)=\begin{cases}\prod_{p\mid q}(p-\delta)^{-1},&\mathbf d\text{ compatible},\\0,&\text{otherwise},\end{cases}
\]

and define the *density sum*

\[
\mathcal A_\delta=\sum_{\mathbf d}\rho_\delta(\mathbf d)\prod_{\gamma\in\Gamma}\mu(d_\gamma)\prod_{r=1}^RF_r\Bigl(\Bigl(\frac{\log d_{r,\ell}}L\Bigr)_{\ell=1}^{j_r}\Bigr),
\]

the sum over all tuples of squarefree positive integers. Empty products are \(1\).

The sum is finite: a nonzero term has \(\prod_\ell d_{r,\ell}\le X^{\rho_r}\) for each \(r\), hence

\[
q\le\prod_{\gamma}d_\gamma\le X^\sigma .
\tag{4.1}
\]

**Proposition 4.2** (density sums). For every \(A>0\), uniformly in the shifts allowed above,

\[
\mathbb E_X\Bigl[\chi_\delta(m)\prod_{r=1}^RD_{F_r}(m;\mathbf b^{(r)})\Bigr]=\mathcal A_\delta+O_A(L^{-A}).
\]

For \(\delta=0\) and \(M\ge1\) the error is at most a constant times \(X^{\sigma-1}(1+L)^{M-1}\prod_r\|F_r\|_\infty\). For \(\delta=0\) and \(M=0\) both sides equal \(\prod_rF_r\). The implied constants depend only on the fixed data.

**Proof.** Expand the product of divisor sums. It becomes a sum over tuples \(\mathbf d\) of squarefree integers, each with the weight \(\prod_\gamma\mu(d_\gamma)\prod_rF_r(\cdots)\), of the average of \(\chi_\delta(m)\) over those \(m\) with \(d_\gamma\mid m+b_\gamma\) for all \(\gamma\).

*Residue classes.* Since the \(d_\gamma\) are squarefree, the conditions \(d_\gamma\mid m+b_\gamma\) say: for every prime \(p\mid q\) and every \(\gamma\) with \(p\mid d_\gamma\), \(m\equiv-b_\gamma\pmod p\). These congruences are consistent at \(p\) exactly when the \(b_\gamma\) with \(p\mid d_\gamma\) agree modulo \(p\). If they are consistent at every \(p\mid q\), the Chinese remainder theorem gives exactly one residue class \(m\equiv m_{\mathbf d}\pmod q\); otherwise there is no such \(m\).

*The case \(\delta=0\).* Compatibility is exactly consistency, and the number of \(m\in(X,2X]\) in one class modulo \(q\) is \(X/q+\eta\) with \(|\eta|\le1\). Dividing by \(X\), the term of \(\mathbf d\) contributes its weight times \(1/q+\eta/X=\rho_0(\mathbf d)+\eta/X\). The main parts add up to \(\mathcal A_0\). The errors are at most \(X^{-1}\prod_r\|F_r\|_\infty\) times the number of tuples with nonzero weight, which by (4.1) and Lemma 2.1 is at most \(X^\sigma(1+\sigma L)^{M-1}\).

*The case \(\delta=1\).* Put \(n=m+a_0\). On the class \(m\equiv m_{\mathbf d}\pmod q\), at each prime \(p\mid q\) we have \(n\equiv a_0-b_\gamma\pmod p\) for the \(\gamma\) with \(p\mid d_\gamma\). So the class of \(n\) is reduced modulo \(q\) exactly when the common residue of these \(b_\gamma\) differs from \(a_0\) at every \(p\mid q\): exactly when \(\mathbf d\) is compatible. If the class of \(n\) is not reduced, a prime \(n\) in it would be divisible by some \(p\mid q\), hence equal to \(p\le q\le X^\sigma\); but \(n>X-H_X>X^\sigma\) for large \(X\), so \(\vartheta(n)=0\) on the whole class and the term vanishes exactly. On a reduced class, the sum of \(\vartheta(m+a_0)\) over \(m\in(X,2X]\) in the class is the sum of \(\vartheta(n)\) over \(n\in(X+a_0,2X+a_0]\) in a reduced class modulo \(q\), which is \(X/\varphi(q)+O(E_X(q))\) with the \(E_X\) of Section 3. Since \(q\) is squarefree, \(1/\varphi(q)=\prod_{p\mid q}(p-1)^{-1}=\rho_1(\mathbf d)\). The main parts add up to \(\mathcal A_1\).

For the errors, group the tuples by \(q\). A tuple of squarefree integers with least common multiple \(q\) is determined by choosing, for each prime \(p\mid q\), the nonempty set of coordinates \(\gamma\) with \(p\mid d_\gamma\); so at most \((2^M)^{\omega(q)}\) tuples have a given \(q\). The total error is therefore at most

\[
\frac{\prod_r\|F_r\|_\infty}X\sum_{q\le X^\sigma}\mu^2(q)(2^M)^{\omega(q)}E_X(q)\ll_AL^{-A}
\]

by Proposition 3.1 with \(K=2^M\). For \(M=0\) the same argument applies with \(q=1\). \(\square\)

The proposition separates the two sources of difficulty. The density sum \(\mathcal A_\delta\) does not involve primes or integers near \(X\); it depends on \(X\) only through \(L\) in the arguments of the test functions, and on the shifts only through their residues modulo small primes. [Correlations of smooth divisor sums](correlations-of-smooth-divisor-sums.md) evaluates it.

## 5. Exercises

**Exercise 5.1.** Let \(F\) have dimension \(1\), budget \(\rho\) and \(F(0)=1\). Show that \(D_F(m;b)=1\) whenever every prime factor of \(m+b\) exceeds \(X^\rho\), and that \(D_F(m;b)=1-F(\log p/L)\) when \(m+b=p\) is a prime with \(p\le X^\rho\).

**Exercise 5.2.** Show that the number of pairs of positive integers with \(d_1d_2\le Y\) is \(Y\log Y+O(Y)\), so Lemma 2.1 is sharp up to a constant factor for \(M=2\).

**Exercise 5.3.** For \(M=1\) and \(\delta=0\), show directly that \(\mathbb E_XD_F(m;b)=\sum_{d}\mu(d)F(\log d/L)/d+O(X^{\rho-1}\|F\|_\infty)\).

**Exercise 5.4.** Show that \(\mathbb E_X\vartheta(m+a)=1+O_A(L^{-A})\) uniformly for \(|a|\le DL^B\).

**Exercise 5.5.** Take two coordinates with shifts \(b_1=0\), \(b_2=2\). Describe the compatible tuples \((d_1,d_2)\) when \(\delta=0\), and when \(\delta=1\) with the mark \(a_0=4\).

**Exercise 5.6.** Explain where the assumption \(\sigma<1/2\) enters the proof of Proposition 4.2 in the case \(\delta=1\), and why \(\sigma<1\) suffices when \(\delta=0\).

## 6. Solutions

**5.1.** The squarefree divisors \(d>1\) of \(m+b\) have a prime factor \(>X^\rho\), so \(\log d/L>\rho\) and \(F(\log d/L)=0\); only \(d=1\) contributes \(\mu(1)F(0)=1\). For \(m+b=p\le X^\rho\) the divisors are \(1\) and \(p\), giving \(F(0)-F(\log p/L)\).

**5.2.** The count is \(\sum_{d_1\le Y}\lfloor Y/d_1\rfloor=Y\sum_{d\le Y}1/d+O(Y)=Y\log Y+O(Y)\).

**5.3.** \(\mathbb E_XD_F(m;b)=\sum_{d\le X^\rho}\mu(d)F(\log d/L)\,X^{-1}\#\{X<m\le2X:d\mid m+b\}\), and the count is \(X/d+\eta\) with \(|\eta|\le1\); the errors add up to at most \(X^{\rho-1}\|F\|_\infty\).

**5.4.** This is Proposition 4.2 with \(R=1\), \(j_1=0\), \(F_1=1\) and \(\delta=1\): the density sum is \(1\). Directly, the sum of \(\vartheta(n)\) over \((X+a,2X+a]\) is \(X+O(E_X(1))\), and \(E_X(1)\ll XL^{-A}\) by Proposition 3.1.

**5.5.** For \(\delta=0\): a prime dividing both \(d_1\) and \(d_2\) must divide \(b_2-b_1=2\), so compatibility means \(\gcd(d_1,d_2)\mid2\). For \(\delta=1\) and \(a_0=4\): additionally a prime \(p\mid d_1\) needs \(0\not\equiv4\pmod p\), so \(d_1\) is odd; a prime \(p\mid d_2\) needs \(2\not\equiv4\pmod p\), so \(d_2\) is odd. Then the common-factor condition forces \(\gcd(d_1,d_2)=1\). Compatible tuples are the coprime pairs of odd squarefree integers.

**5.6.** In the marked case the moduli \(q\) go up to \(X^\sigma\), and the Bombieri–Vinogradov theorem controls the errors \(E_X(q)\) on average only for \(q\le X^{1/2-\varepsilon}\) (Step 1 of Proposition 3.1 needs \(X^\sigma\le\sqrt{3X}/(\log3X)^{A_0+3}\)); the bound \(n>X^\sigma\) for nonreduced classes also uses \(\sigma<1\). In the unmarked case one only counts integers in residue classes, with error \(1\) per class, and the total error \(X^{\sigma-1}(1+L)^{M-1}\) is small as soon as \(\sigma<1\).

## References

- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
- [GY] D. A. Goldston, C. Y. Yıldırım, Higher correlations of divisor sums related to primes I: triple correlations, Integers 3 (2003), A5. https://math.colgate.edu/~integers/d5/d5.pdf
- [Maynard] J. Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), 383–413. https://arxiv.org/abs/1311.4600
