# The singular series and its average

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite set \(\mathcal H\) of shifts carries an arithmetic weight \(\mathfrak S(\mathcal H)\), the singular series. It compares how often the integers \(m+h\), \(h\in\mathcal H\), avoid each prime with what independent random integers would do. In Hardy and Littlewood's conjecture on prime tuples, \(\mathfrak S(\mathcal H)\,x/(\log x)^{|\mathcal H|}\) is the predicted number of \(m\le x\) for which all \(m+h\) are prime. That conjecture is not used here. In this course the singular series appears as a factor in correlations of divisor sums, proved in [Correlations of smooth divisor sums](correlations-of-smooth-divisor-sums.md), and it must be summed over the shifts in the blocks \(I\) and \(J\) of [Prime gaps and adjacent intervals](prime-gaps-and-adjacent-intervals.md).

Individual values of \(\mathfrak S\) fluctuate: \(\mathfrak S(\{0,1\})=0\) while \(\mathfrak S(\{0,2\})\approx1.32\). This lesson proves Gallagher's theorem that the average over shifts in intervals of length \(h\) tends to \(1\), in a form that allows different coordinates to range over different intervals.

We use Chebyshev's bound \(\theta(x)<(2\log2)x\), Theorem 2.1 of [Counting primes by elementary means](course:NT-ZETA/NT-ZETA-02#2-a-binomial-coefficient-measures-primes), Mertens's estimate \(\sum_{p\le x}1/p=\log\log x+O(1)\), Theorem 3.1 there, and the Chinese remainder theorem.

## 1. Definition and first properties

For a finite set \(\mathcal H\subset\mathbb Z\) and a prime \(p\), let \(\nu_p(\mathcal H)\) be the number of residue classes modulo \(p\) that meet \(\mathcal H\).

**Definition 1.1.** The *singular series* of a finite set \(\mathcal H\) with \(s=|\mathcal H|\) elements is

\[
\mathfrak S(\mathcal H)=\prod_p\Bigl(1-\frac{\nu_p(\mathcal H)}p\Bigr)\Bigl(1-\frac1p\Bigr)^{-s},\qquad\mathfrak S(\varnothing)=1 .
\]

The factor at \(p\) is the probability that a random residue avoids all classes \(-h\bmod p\), divided by the probability \((1-1/p)^s\) that \(s\) independent random residues are all nonzero.

**Lemma 1.2.** Let \(s=|\mathcal H|\ge1\) and \(\Delta=\prod_{h<h'}(h'-h)\) over pairs from \(\mathcal H\) (\(\Delta=1\) if \(s=1\)). There is \(C_s\) such that for every prime \(p>2s\):

1. if \(p\nmid\Delta\), then \(\nu_p(\mathcal H)=s\) and the factor at \(p\) is \(e^{\eta}\) with \(|\eta|\le C_s/p^2\);
2. if \(p\mid\Delta\), the factor at \(p\) is \(e^{\eta}\) with \(|\eta|\le C_s/p\).

Consequently the product converges absolutely, \(\mathfrak S(\mathcal H)\ge0\), \(\mathfrak S(\mathcal H)=0\) exactly when \(\nu_p(\mathcal H)=p\) for some prime \(p\) (necessarily \(p\le s\)), and \(\mathfrak S(\mathcal H)=1\) when \(s=1\).

**Proof.** If \(p\nmid\Delta\), the elements of \(\mathcal H\) are distinct modulo \(p\), so \(\nu_p=s\). For \(p>2s\),

\[
\log\Bigl(1-\frac sp\Bigr)-s\log\Bigl(1-\frac1p\Bigr)=\sum_{k\ge2}\frac{s-s^k}{kp^k},
\]

whose absolute value is at most \(\sum_{k\ge2}s^k/p^k\le2s^2/p^2\). If \(p\mid\Delta\), then \(1\le\nu_p\le s\) and the factor lies between \(1-s/p\ge1/2\) and \((1-1/p)^{-s}\); both logarithms are at most \(2s/p\) in absolute value. Only finitely many \(p\) divide \(\Delta\), so the logarithms are summable over \(p>2s\). Each factor is nonnegative, and it vanishes exactly when \(\nu_p=p\), which needs \(p\le s\). For \(s=1\) every factor is \((1-1/p)(1-1/p)^{-1}=1\). \(\square\)

A set with \(\mathfrak S(\mathcal H)>0\) is called *admissible*. For example \(\{0,1\}\) meets both classes modulo \(2\), and \(\{0,2,4\}\) meets all three classes modulo \(3\), so both have singular series \(0\).

**Lemma 1.3** (pairs). Let \(C_2=\prod_{p>2}\bigl(1-(p-1)^{-2}\bigr)=0.6601618\ldots\). For \(\delta\ne0\),

\[
\mathfrak S(\{0,\delta\})=\begin{cases}0,&\delta\text{ odd},\\[2pt]2C_2\displaystyle\prod_{p\mid\delta,\ p>2}\frac{p-1}{p-2},&\delta\text{ even}.\end{cases}
\]

**Proof.** At \(p=2\) the factor is \(0\) if \(\delta\) is odd (two classes) and \((1/2)(1/2)^{-2}=2\) if \(\delta\) is even. For \(p>2\) with \(p\nmid\delta\) the factor is \((1-2/p)(1-1/p)^{-2}=p(p-2)/(p-1)^2=1-(p-1)^{-2}\). For \(p>2\) with \(p\mid\delta\) it is \((1-1/p)^{-1}=p/(p-1)\), which is the generic factor times \(\frac p{p-1}\cdot\frac{(p-1)^2}{p(p-2)}=\frac{p-1}{p-2}\). \(\square\)

So \(\mathfrak S(\{0,2\})=2C_2=1.3203\ldots\), the twin-prime constant. A numerical evaluation gives \(\mathfrak S(\{0,2,6\})=\mathfrak S(\{0,4,6\})=2.8582\ldots\).

## 2. The mean value modulo small primes

**Lemma 2.1.** Let \(p\) be prime and \(s\ge0\). If \(a_1,\dots,a_s\) are independent uniformly distributed residues modulo \(p\), and \(\nu\) is the number of distinct classes among them, then \(\mathbb E\,(1-\nu/p)=(1-1/p)^s\).

**Proof.** \(1-\nu/p\) is the proportion of residues \(x\) modulo \(p\) different from every \(a_i\). Averaging over the \(a_i\) as well, it is the probability that a uniform residue \(x\), independent of the \(a_i\), differs from all of them, which is \((1-1/p)^s\). \(\square\)

For a tuple \(\mathbf a=(a_1,\dots,a_s)\) of integers, possibly with repeated entries, and \(y\ge2\), define the truncated series

\[
\mathfrak S_y(\mathbf a)=\prod_{p\le y}\Bigl(1-\frac{\nu_p(\{a_1,\dots,a_s\})}p\Bigr)\Bigl(1-\frac1p\Bigr)^{-s}.
\]

The exponent is \(s\), the length of the tuple, even if entries repeat. The value depends only on the residues of the \(a_i\) modulo \(Q_y=\prod_{p\le y}p\).

**Corollary 2.2.** The average of \(\mathfrak S_y\) over all \(\mathbf a\in(\mathbb Z/Q_y\mathbb Z)^s\) is exactly \(1\).

**Proof.** By the Chinese remainder theorem, a uniform element of \((\mathbb Z/Q_y)^s\) has independent uniform reductions modulo the primes \(p\le y\). The factor at \(p\) depends only on the reduction modulo \(p\), so the average of the product is the product of the averages, each equal to \(1\) by Lemma 2.1. \(\square\)

**Lemma 2.3.** There is \(C_s\) with \(0\le\mathfrak S_y(\mathbf a)\le\prod_{p\le y}(1-1/p)^{-s}\le C_s(\log y)^s\) for all tuples of length \(s\) and \(y\ge3\).

**Proof.** Each factor lies in \([0,(1-1/p)^{-s}]\). Further \(\log\prod_{p\le y}(1-1/p)^{-1}=\sum_{p\le y}\sum_{k\ge1}1/(kp^k)\le\sum_{p\le y}1/p+\sum_p1/(p(p-1))\le\log\log y+O(1)\) by Mertens's estimate. \(\square\)

## 3. The tail of the product

For a tuple \(\mathbf a\) of \(s\ge2\) distinct integers and \(y>2s\), put

\[
T_y(\mathbf a)=\prod_{p>y}\Bigl(1-\frac{\nu_p}p\Bigr)\Bigl(1-\frac1p\Bigr)^{-s},\qquad\text{so that}\qquad\mathfrak S(\{a_1,\dots,a_s\})=\mathfrak S_y(\mathbf a)\,T_y(\mathbf a).
\]

The identity holds even when a factor of \(\mathfrak S_y\) vanishes; no division takes place.

**Lemma 3.1.** Let \(\Delta=\prod_{i<j}|a_i-a_j|\). Then, with the constant \(C_s\) of Lemma 1.2,

\[
|\log T_y(\mathbf a)|\le C_s\Bigl(\frac2y+\frac{\log\Delta}{y\log y}\Bigr).
\]

**Proof.** By Lemma 1.2 the primes \(p>y\) with \(p\nmid\Delta\) contribute at most \(C_s\sum_{n>y}n^{-2}\le2C_s/y\). Each prime \(p>y\) dividing \(\Delta\) contributes at most \(C_s/p<C_s/y\), and there are at most \(\log\Delta/\log y\) of them, because their product divides \(\Delta\) and each exceeds \(y\). \(\square\)

## 4. Gallagher's average in boxes

**Theorem 4.1.** Fix integers \(s\ge0\) and \(K\ge1\). For \(h\ge1\), let \(I_1,\dots,I_s\) be sets of \(h\) consecutive integers, all contained in one interval of length at most \(Kh\). Then

\[
\sum_{\substack{a_i\in I_i\ (1\le i\le s)\\a_1,\dots,a_s\ \text{distinct}}}\mathfrak S(\{a_1,\dots,a_s\})=h^s\Bigl(1+O_{s,K}\Bigl(\frac1{\log\log h}\Bigr)\Bigr)
\]

as \(h\to\infty\), uniformly in the intervals.

For \(I_1=\dots=I_s=\{1,\dots,h\}\) this is Gallagher's theorem; see [Montgomery–Soundararajan] for its history and for a second-order term.

**Proof.** For \(s=0\) both sides are \(1\), and for \(s=1\) both are \(h\), since \(\mathfrak S\) of a single point is \(1\). Let \(s\ge2\), put \(y=\frac14\log h\) and \(Q=Q_y=\prod_{p\le y}p\). By Chebyshev's bound, \(Q=e^{\theta(y)}\le4^y=h^{(\log4)/4}\le h^{1/2}\).

*Step 1: the truncated sum over all tuples.* Each residue class modulo \(Q\) contains \(\lfloor h/Q\rfloor\) or \(\lceil h/Q\rceil\) elements of each \(I_i\), so a uniform element of \(I_i\) lies in a given class with probability \(Q^{-1}(1+\eta Q/h)\), \(|\eta|\le1\). For the uniform tuple on \(I_1\times\dots\times I_s\) the probability of a given class tuple \(\mathbf c\in(\mathbb Z/Q)^s\) is therefore \(Q^{-s}(1+\eta_{\mathbf c})\) with \(|\eta_{\mathbf c}|\le(1+Q/h)^s-1\le2^sQ/h\). As \(\mathfrak S_y\ge0\), Corollary 2.2 gives

\[
h^{-s}\sum_{\mathbf a\in I_1\times\dots\times I_s}\mathfrak S_y(\mathbf a)=Q^{-s}\sum_{\mathbf c}(1+\eta_{\mathbf c})\mathfrak S_y(\mathbf c)=1+O\Bigl(\frac{2^sQ}h\Bigr)=1+O_s(h^{-1/2}).
\]

*Step 2: distinct tuples.* At most \(\binom s2h^{s-1}\) tuples have two equal entries, and \(\mathfrak S_y\le C_s(\log y)^s\) on each by Lemma 2.3. Removing them changes the normalized sum by \(O_s(h^{-1}(\log\log h)^s)\).

*Step 3: the tail.* For distinct entries in an interval of length \(Kh\), \(\log\Delta\le\binom s2\log(Kh)\). With \(y=\frac14\log h\), Lemma 3.1 gives \(T_y(\mathbf a)=1+O_{s,K}(1/\log\log h)\), uniformly over the distinct tuples.

*Conclusion.* By the factorization \(\mathfrak S=\mathfrak S_yT_y\) and \(\mathfrak S_y\ge0\),

\[
\sum_{\text{distinct}}\mathfrak S(\{a_i\})=\Bigl(1+O\Bigl(\frac1{\log\log h}\Bigr)\Bigr)\sum_{\text{distinct}}\mathfrak S_y(\mathbf a)=h^s\Bigl(1+O_{s,K}\Bigl(\frac1{\log\log h}\Bigr)\Bigr).\qquad\square
\]

Numerically, for \(s=2\) and \(I_1=I_2=\{1,\dots,h\}\), the normalized sum is \(0.94017\), \(0.98148\), \(0.99451\) for \(h=100,400,1600\). The second-order formula \(1-h^{-1}\log h+(1-\gamma-\log2\pi)h^{-1}\) of [Montgomery–Soundararajan], with Euler's constant \(\gamma\), gives \(0.93980\), \(0.98148\), \(0.99450\).

The blocks of [Prime gaps and adjacent intervals](prime-gaps-and-adjacent-intervals.md) satisfy the hypothesis with \(K=2\): \(J=\{1,\dots,h\}\) and \(I=\{h+1,\dots,2h\}\) lie in \(\{1,\dots,2h\}\). The following form is the one used later.

**Corollary 4.2.** Fix \(s\ge0\) and assign each coordinate \(i\le s\) to one of the blocks \(J\) or \(I\), with \(h=\lfloor\lambda\log X\rfloor\). Then the sum of \(\mathfrak S(\{a_1,\dots,a_s\})\) over distinct tuples with each \(a_i\) in its assigned block is \(h^s(1+o(1))\) as \(X\to\infty\). In particular it is \(O_s(h^s)\).

## 5. Exercises

**Exercise 5.1.** Show that \(\mathfrak S(\{0,2,6\})=\frac92\prod_{p\ge5}(1-3/p)(1-1/p)^{-3}\), and that \(\mathfrak S(\{0,2,6\})=\mathfrak S(\{0,4,6\})\).

**Exercise 5.2.** Show that for every \(s\ge1\) the first \(s\) primes larger than \(s\) form an admissible set.

**Exercise 5.3.** Check Corollary 2.2 by hand for \(y=2\) (so \(Q=2\)) and \(s=2\).

**Exercise 5.4.** Show that \(\mathfrak S(\mathcal H)\le C_s(1+\log\log\Delta)^s\) for every set of \(s\ge2\) elements with \(\Delta\ge3\).

**Exercise 5.5.** Deduce from Theorem 4.1 that \(\sum_{1\le\delta<h}(1-\delta/h)\,\mathfrak S(\{0,\delta\})\sim h/2\).

**Exercise 5.6.** The proof of Theorem 4.1 truncates at \(y=\frac14\log h\). Show that Step 1 would fail for \(y=h\), and that the bound of Step 3 would fail for fixed \(y\).

## 6. Solutions

**5.1.** At \(p=2\): one class, factor \((1/2)(1/2)^{-3}=4\). At \(p=3\): the residues \(0,2,0\) give two classes, factor \((1/3)(3/2)^3=9/8\). For \(p\ge5\) the differences \(2,4,6\) are not divisible by \(p\), so there are three classes. The product of \(4\) and \(9/8\) is \(9/2\). For \(\{0,4,6\}\) the residues modulo \(3\) are \(0,1,0\) and the differences \(4,6,2\) are the same, so every factor agrees.

**5.2.** Let \(q_1<\dots<q_s\) be the first \(s\) primes larger than \(s\). For a prime \(p\le s\), no \(q_i\) is divisible by \(p\), so the class \(0\) is missed and \(\nu_p<p\). For \(p>s\), \(\nu_p\le s<p\). No factor vanishes.

**5.3.** Modulo \(2\) the four tuples \((0,0),(0,1),(1,0),(1,1)\) have \(\nu=1,2,2,1\), so the factors \((1-\nu/2)\cdot4\) are \(2,0,0,2\), with average \(1\).

**5.4.** Take \(y=\max(\log\Delta,2s+1)\) in \(\mathfrak S=\mathfrak S_yT_y\). Lemma 2.3 gives \(\mathfrak S_y\le C_s(\log y)^s\le C'_s(1+\log\log\Delta)^s\). Since \(y\ge\log\Delta\), Lemma 3.1 gives \(\log T_y\le C_s(2/y+1/\log y)\le3C_s\).

**5.5.** For \(s=2\) and \(I_1=I_2=\{1,\dots,h\}\), the pairs with difference \(\pm\delta\) number \(2(h-\delta)\), and \(\mathfrak S(\{a,a+\delta\})=\mathfrak S(\{0,\delta\})\). So the sum in Theorem 4.1 is \(2\sum_{\delta<h}(h-\delta)\mathfrak S(\{0,\delta\})=h^2(1+o(1))\). Divide by \(2h\).

**5.6.** For \(y=h\), the modulus \(Q_h=e^{\theta(h)}\) grows exponentially in \(h\), by Chebyshev's lower bound \(\psi(x)\ge(\log2)x-C\log x\) together with \(\psi(x)-\theta(x)=O(\sqrt x\log x)\). A set of \(h\) consecutive integers meets only \(h\) of the \(Q_h\) classes, so its residues are far from equidistributed and the error \(2^sQ/h\) of Step 1 is huge. For fixed \(y\), the bound of Lemma 3.1 contains \(\log\Delta/(y\log y)\), which grows like \(\log h\). Indeed \(T_y\) is not uniformly close to \(1\): by Lemma 1.3, \(T_y(\{0,\delta\})\) contains the factor \(\prod_{y<p\mid\delta}(p-1)/(p-2)\), which is large when \(\delta\) is divisible by many primes above \(y\).

## References

- [Montgomery–Soundararajan] H. L. Montgomery, K. Soundararajan, Primes in short intervals, Communications in Mathematical Physics 252 (2004), 589–617. https://arxiv.org/abs/math/0409258
- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
