# Concentration and the discrete cube

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A sum of many independent or nearly independent random terms rarely strays far from its mean. This lesson proves the three forms of this principle that the Gaussian moat course uses: Chebyshev's inequality for a sum over a random subset of a fixed population, Hoeffding's inequality for sums of independent bounded variables, and an exponential bound for the lower tail of a binomial law. It also proves an isoperimetric inequality for the discrete cube \(\{0,1\}^r\), and deduces that neighbourhoods of small sets of vertices grow quickly. In the next lesson these facts show that reduction modulo a product of randomly chosen prime factors separates many lattice points at once.

We assume finite probability, as in the core course [Probability (B90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B90). The setting of the course is described in [Walks through Gaussian primes](walks-through-gaussian-primes.md).

Basic references are [Vershynin] and [OpenAI-moat].

## 1. Markov, Chebyshev, and sampling without replacement

For a nonnegative random variable \(X\) and \(t>0\), **Markov's inequality** \(\mathbb P(X\ge t)\le\mathbb EX/t\) follows from \(t\,\mathbf 1_{X\ge t}\le X\). Applied to \((X-\mathbb EX)^2\), it gives **Chebyshev's inequality**

\[
\mathbb P\bigl(|X-\mathbb EX|\ge t\bigr)\le\frac{\operatorname{Var}X}{t^2}.
\]

**Proposition 1.1** (sampling without replacement). Let \(x_1,\dots,x_N\) be real numbers with mean \(\bar x\), all lying in an interval of length \(\ell\). Let \(\mathcal S\) be a uniformly random subset of \(\{1,\dots,N\}\) with \(r\) elements, \(1\le r\le N\), and \(\Sigma=\sum_{j\in\mathcal S}x_j\). Then

\[
\mathbb E\Sigma=r\bar x,\qquad \operatorname{Var}\Sigma\le\frac{r\ell^2}4.
\]

**Proof.** Let \(\xi_j\) indicate \(j\in\mathcal S\). Then \(\mathbb E\xi_j=r/N\), which gives the mean. Replacing every \(x_j\) by \(x_j-\bar x\) changes \(\Sigma\) by the constant \(-r\bar x\), so we may assume \(\bar x=0\); then \(\sum_jx_j=0\) and \(\sum_{j\ne k}x_jx_k=-\sum_jx_j^2\). We have \(\operatorname{Var}\xi_j=\frac rN(1-\frac rN)\) and, for \(j\ne k\) and \(N\ge2\),

\[
\operatorname{Cov}(\xi_j,\xi_k)=\frac{r(r-1)}{N(N-1)}-\frac{r^2}{N^2}=-\frac{r(N-r)}{N^2(N-1)}.
\]

Hence

\[
\operatorname{Var}\Sigma=\sum_jx_j^2\Bigl(\frac{r(N-r)}{N^2}+\frac{r(N-r)}{N^2(N-1)}\Bigr)=\frac{r(N-r)}{N(N-1)}\sum_jx_j^2\le\frac rN\sum_jx_j^2.
\]

If \(m\) is the midpoint of the interval, then \(\sum_j(x_j-\bar x)^2\le\sum_j(x_j-m)^2\le N\ell^2/4\), because the mean minimizes the sum of squared deviations. For \(N=1\) the variance is \(0\). \(\square\)

## 2. Hoeffding's inequality

**Lemma 2.1** (Hoeffding's lemma). Let \(X\) be a random variable with \(a\le X\le b\) and \(\mathbb EX=0\). For every real \(\lambda\),

\[
\mathbb Ee^{\lambda X}\le e^{\lambda^2(b-a)^2/8}.
\]

**Proof.** If \(a=b\), then \(X=0\). Otherwise \(a\le0\le b\), and convexity of \(x\mapsto e^{\lambda x}\) on \([a,b]\) gives

\[
e^{\lambda X}\le\frac{b-X}{b-a}e^{\lambda a}+\frac{X-a}{b-a}e^{\lambda b}.
\]

Take expectations, put \(\theta=-a/(b-a)\in[0,1]\) and \(u=\lambda(b-a)\). The right side becomes \((1-\theta)e^{\lambda a}+\theta e^{\lambda b}=e^{\Lambda(u)}\), where \(\Lambda(u)=-\theta u+\log(1-\theta+\theta e^u)\). Then \(\Lambda(0)=0\), \(\Lambda'(0)=0\), and

\[
\Lambda''(u)=\frac{\theta e^u}{1-\theta+\theta e^u}\Bigl(1-\frac{\theta e^u}{1-\theta+\theta e^u}\Bigr)\le\frac14,
\]

since \(w(1-w)\le\frac14\). Taylor's theorem gives \(\Lambda(u)\le u^2/8\). \(\square\)

**Theorem 2.2** (Hoeffding's inequality). Let \(X_1,\dots,X_r\) be independent random variables with \(a_j\le X_j\le b_j\), and \(S=\sum_jX_j\). For every \(t\ge0\),

\[
\mathbb P(S-\mathbb ES\ge t)\le\exp\Bigl(-\frac{2t^2}{\sum_j(b_j-a_j)^2}\Bigr).
\]

**Proof.** We may assume the denominator \(\sigma^2=\sum_j(b_j-a_j)^2\) is positive, since otherwise \(S\) is constant. For \(\lambda>0\), Markov's inequality, independence and Lemma 2.1 applied to \(X_j-\mathbb EX_j\in[a_j-\mathbb EX_j,b_j-\mathbb EX_j]\) give

\[
\mathbb P(S-\mathbb ES\ge t)\le e^{-\lambda t}\prod_j\mathbb Ee^{\lambda(X_j-\mathbb EX_j)}\le\exp\Bigl(-\lambda t+\frac{\lambda^2\sigma^2}8\Bigr).
\]

Take \(\lambda=4t/\sigma^2\). \(\square\)

The inequality is due to Hoeffding (1963). *Reference:* [Vershynin, Theorem 2.2.6].

## 3. The lower tail of a binomial law

**Proposition 3.1.** Let \(B\) have the binomial law with \(n\) trials and success probability \(\lambda\in(0,1]\), and let \(0<v<1\). Then

\[
\mathbb P\bigl(B\le(1-v)n\lambda\bigr)\le\exp\Bigl(-\frac{n\lambda v^2}2\Bigr).
\]

**Proof.** For \(t>0\), independence and \(1+x\le e^x\) give \(\mathbb Ee^{-tB}=(1-\lambda+\lambda e^{-t})^n\le\exp\bigl(n\lambda(e^{-t}-1)\bigr)\). By Markov's inequality applied to \(e^{-tB}\),

\[
\mathbb P\bigl(B\le(1-v)n\lambda\bigr)\le\exp\bigl(n\lambda(e^{-t}-1)+t(1-v)n\lambda\bigr).
\]

Take \(t=-\log(1-v)\), so that \(e^{-t}=1-v\). The exponent becomes \(-n\lambda\,g(v)-n\lambda v^2/2\), where \(g(v)=v+(1-v)\log(1-v)-v^2/2\). Since \(g(0)=0\) and \(g'(v)=-\log(1-v)-v\ge0\), we have \(g\ge0\) on \([0,1)\). \(\square\)

*Reference:* [Vershynin, Section 2.3] treats these Chernoff bounds.

**Lemma 3.2** (comparison of success probabilities). Let \(B'\) be a sum of \(n\) independent indicators with success probabilities \(\lambda_j\ge\lambda\). Then \(\mathbb P(B'\le m)\le\mathbb P(B\le m)\) for every \(m\), where \(B\) is binomial with \(n\) trials and success probability \(\lambda\).

**Proof.** Let \(U_1,\dots,U_n\) be independent and uniform on \([0,1]\). The variables \(\sum_j\mathbf 1_{U_j\le\lambda_j}\) and \(\sum_j\mathbf 1_{U_j\le\lambda}\) have the laws of \(B'\) and \(B\), and the first is at least the second at every outcome. \(\square\)

## 4. The discrete cube

The **discrete cube** \(\{0,1\}^r\) is the graph whose vertices are the \(2^r\) binary vectors of length \(r\), two vectors being adjacent when they differ in exactly one coordinate. The **Hamming distance** \(\operatorname{dist}(x,y)\) is the number of coordinates in which \(x\) and \(y\) differ; it is the graph distance. For a set \(S\) of vertices:

- the **edge boundary** \(\partial_ES\) is the set of edges with exactly one endpoint in \(S\);
- the **outer vertex boundary** \(\partial_VS\) is the set of vertices outside \(S\) adjacent to a vertex of \(S\);
- the **\(h\)-neighbourhood** \(N_h(S)\) is the set of vertices at Hamming distance at most \(h\) from \(S\).

Thus \(N_1(S)=S\cup\partial_VS\) and \(N_{j+1}(S)=N_1(N_j(S))\). We write \(\log_2\) for the logarithm to base \(2\) and \(h_2(a)=-a\log_2a-(1-a)\log_2(1-a)\) for the binary entropy in bits.

**Theorem 4.1** (edge-isoperimetric inequality). For every nonempty set \(S\) of vertices of \(\{0,1\}^r\),

\[
|\partial_ES|\ge|S|\log_2\frac{2^r}{|S|}.
\]

**Proof.** Induction on \(r\). For \(r=0\) the cube has one vertex, and both sides vanish. Let \(r\ge1\), and split the cube according to the last coordinate into two copies of \(\{0,1\}^{r-1}\). Let \(S_0\) and \(S_1\) be the parts of \(S\) in the two copies, viewed as subsets of \(\{0,1\}^{r-1}\), with \(|S_0|=a|S|\) and \(|S_1|=(1-a)|S|\). The boundary edges inside the copies are those of \(S_0\) and \(S_1\). An edge between the copies joins \(x\) with last coordinate \(0\) to the same \(x\) with last coordinate \(1\); it is a boundary edge when \(x\) lies in exactly one of \(S_0\), \(S_1\). There are \(|S_0\triangle S_1|\ge\bigl||S_0|-|S_1|\bigr|=|1-2a|\,|S|\) such edges. By induction, with the term of an empty part read as \(0\),

\[
|\partial_ES|\ge|S_0|\Bigl(r-1-\log_2|S_0|\Bigr)+|S_1|\Bigl(r-1-\log_2|S_1|\Bigr)+|1-2a|\,|S|.
\]

Since \(|S_0|\log_2|S_0|+|S_1|\log_2|S_1|=|S|\bigl(\log_2|S|-h_2(a)\bigr)\), the right side equals

\[
|S|\Bigl(r-1-\log_2|S|+h_2(a)+|1-2a|\Bigr).
\]

Finally \(h_2(a)\ge1-|1-2a|\): the function \(h_2\) is concave with \(h_2(0)=h_2(1)=0\) and \(h_2(\frac12)=1\), so it lies above the two chords \(2a\) on \([0,\frac12]\) and \(2(1-a)\) on \([\frac12,1]\). Hence \(|\partial_ES|\ge|S|(r-\log_2|S|)\). \(\square\)

The inequality is sharp for subcubes (Exercise 5.3). It is a form of the edge-isoperimetric theorem for the cube, which goes back to Harper.

**Corollary 4.2.** For every nonempty \(S\), \(\displaystyle|\partial_VS|\ge\frac{|S|}r\log_2\frac{2^r}{|S|}\).

**Proof.** Each boundary edge has exactly one endpoint in \(\partial_VS\), and each vertex has \(r\) edges. \(\square\)

**Proposition 4.3** (growth of small sets). Let \(S\) be a nonempty set of vertices with \(|S|\le\mu2^r\), let \(\mu\le\theta<1\), and let \(h\ge1\) be an integer. Then

\[
|N_h(S)|\ge\min\Bigl\{\Bigl(1+\frac{\log_2(1/\theta)}r\Bigr)^h,\ \frac\theta\mu\Bigr\}\,|S|.
\]

**Proof.** Put \(s_j=|N_j(S)|\), a nondecreasing sequence. If \(s_j\le\theta2^r\), then \(\log_2(2^r/s_j)\ge\log_2(1/\theta)\), and Corollary 4.2 applied to \(N_j(S)\) gives \(s_{j+1}\ge s_j\bigl(1+\log_2(1/\theta)/r\bigr)\). If \(s_j\le\theta2^r\) for all \(j<h\), induction gives the first bound. Otherwise \(s_j>\theta2^r\ge(\theta/\mu)|S|\) for some \(j<h\), and then \(s_h\ge s_j\) gives the second. \(\square\)

**Corollary 4.4** (separated small sets). Let \(S_1,\dots,S_m\) be nonempty sets of vertices of \(\{0,1\}^r\), each with \(|S_l|\le\mu2^r\), such that any two vertices from different sets are at Hamming distance greater than \(2h\). Let \(\mu\le\theta<1\). Then

\[
\sum_l|S_l|\le2^r\Bigl/\min\Bigl\{\Bigl(1+\frac{\log_2(1/\theta)}r\Bigr)^h,\ \frac\theta\mu\Bigr\}.
\]

**Proof.** The neighbourhoods \(N_h(S_l)\) are pairwise disjoint: a vertex within distance \(h\) of two of the sets would give two vertices of different sets at distance at most \(2h\). So \(\sum_l|N_h(S_l)|\le2^r\). Apply Proposition 4.3 to each \(S_l\). \(\square\)

## 5. Exercises

**Exercise 5.1 (easy).** Let \(\varepsilon_1,\dots,\varepsilon_r\) be independent fair signs \(\pm1\). Show that \(\mathbb P(\sum_j\varepsilon_j\ge t)\le e^{-t^2/(2r)}\).

**Exercise 5.2 (easy).** In Proposition 1.1, show that the variance equals \(\frac{N-r}{N-1}\) times the variance of a sum of \(r\) independent uniform draws from the population, and that it vanishes when \(r=N\).

**Exercise 5.3 (easy).** Let \(S\) be a subcube of dimension \(d\), that is, the set of vectors with \(r-d\) prescribed coordinates. Show that equality holds in Theorem 4.1.

**Exercise 5.4 (medium).** Let \(r=2m+1\) be odd, and let \(S\) be the set of vertices with at most \(m\) coordinates equal to \(1\). Show that \(|S|=2^{r-1}\), that \(\partial_VS\) is the set of vertices with exactly \(m+1\) coordinates equal to \(1\), and that \(|\partial_VS|\le2|S|/\sqrt{3m+4}\). Use the bound \(\binom{2n}n\le4^n/\sqrt{3n+1}\), and prove it by induction on \(n\). Compare with the lower bound \(|\partial_VS|\ge|S|/r\) of Corollary 4.2.

**Exercise 5.5 (medium).** Let \(B\) be binomial with \(n\) trials and success probability \(\lambda\). Use Proposition 3.1 to show that \(\mathbb P(B=0)\le e^{-n\lambda/2}\), and compare with the exact value \((1-\lambda)^n\).

## 6. Solutions

**5.1.** Apply Theorem 2.2 with \(a_j=-1\), \(b_j=1\) and \(\mathbb ES=0\): the bound is \(\exp(-2t^2/(4r))\).

**5.2.** A single uniform draw has variance \(\sigma^2=\frac1N\sum_j(x_j-\bar x)^2\), so \(r\) independent draws have variance \(r\sigma^2\). The proof of Proposition 1.1 gives \(\operatorname{Var}\Sigma=\frac{r(N-r)}{N(N-1)}\sum_j(x_j-\bar x)^2=\frac{N-r}{N-1}\,r\sigma^2\), which vanishes for \(r=N\), when \(\Sigma\) is the constant \(\sum_jx_j\).

**5.3.** \(|S|=2^d\), and each vertex of \(S\) has exactly \(r-d\) edges leaving \(S\) (change one of the prescribed coordinates). So \(|\partial_ES|=2^d(r-d)=|S|\log_2(2^r/|S|)\).

**5.4.** Complementing all coordinates maps \(S\) bijectively onto the set of vertices with at least \(m+1\) ones, which is the complement of \(S\); so \(|S|=2^{r-1}\). A vertex outside \(S\) has at least \(m+1\) ones; it is adjacent to \(S\) exactly when changing one coordinate can bring the count to \(m\), that is, when it has exactly \(m+1\) ones. So \(|\partial_VS|=\binom r{m+1}=\frac12\binom{2m+2}{m+1}\).

For the bound on central binomial coefficients, \(\binom21=2=4/\sqrt4\). The ratio of consecutive coefficients is \(\binom{2n+2}{n+1}\big/\binom{2n}n=2(2n+1)/(n+1)\), so the induction step needs \(2(2n+1)/\bigl((n+1)\sqrt{3n+1}\bigr)\le4/\sqrt{3n+4}\). Squaring, this is \((2n+1)^2(3n+4)\le4(n+1)^2(3n+1)\), and the difference of the two sides is \(n\ge0\).

Hence \(|\partial_VS|\le\frac12\cdot4^{m+1}/\sqrt{3m+4}=2|S|/\sqrt{3m+4}\). Corollary 4.2 gives \(|\partial_VS|\ge|S|/(2m+1)\). So, for sets of half the size of the cube, the lower bound of Corollary 4.2 can be improved by at most a factor of order \(\sqrt r\).

**5.5.** \(\mathbb P(B=0)\le\mathbb P(B\le(1-v)n\lambda)\le e^{-n\lambda v^2/2}\) for every \(v<1\); let \(v\to1\). The exact value satisfies \((1-\lambda)^n\le e^{-n\lambda}\), which is smaller: Proposition 3.1 loses a factor \(2\) in the exponent at this extreme.

## References

- [Vershynin] R. Vershynin, High-Dimensional Probability: An Introduction with Applications in Data Science, first edition, Cambridge University Press, 2018; free version on the author's page. https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf
- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
