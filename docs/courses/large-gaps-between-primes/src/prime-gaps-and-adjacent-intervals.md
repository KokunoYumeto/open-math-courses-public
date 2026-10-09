# Prime gaps and adjacent intervals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(p_n\) be the \(n\)-th prime and \(d_n=p_{n+1}-p_n\) the gap that follows it. By the prime number theorem the gaps near \(p\) have average size \(\log p\). This course proves that large gaps are not rare exceptions: for every fixed \(C>0\), a positive proportion of all gaps exceed \(C\log p_n\). The result is due to OpenAI (2026) [OpenAI-Gaps]. It answers a question of Erdős and Prachar about the increases of \(p_n/n\).

This lesson proves the elementary facts about averages, states the theorem, and reduces it to the construction of nonnegative weights on the integers with four moment properties (Proposition 4.1). The other five lessons construct the weights. The reduction rests on one observation: a prime that is followed by a long empty interval can be found from at most \(h\) starting points, however long its gap is.

We use the prime number theorem in the forms \(\theta(x)=\sum_{p\le x}\log p\sim x\) and \(\pi(x)\sim x/\log x\), Theorem 3.1 of [The prime number theorem](course:NT-ZETA/NT-ZETA-09#3-from-an-average-to-the-number-of-primes).

## 1. The average gap

**Proposition 1.1.** As \(N\to\infty\),

\[
\frac1N\sum_{n\le N}\frac{d_n}{\log p_n}\longrightarrow1 .
\]

**Proof.** The gaps telescope: \(\sum_{n\le N}d_n=p_{N+1}-2\). The prime number theorem gives \(N=\pi(p_N)\sim p_N/\log p_N\), hence \(p_N\sim N\log p_N\), and \(\log p_N=\log N+\log\log p_N+o(1)\sim\log N\). So \(p_N\sim N\log N\), and the same holds for \(p_{N+1}\).

Lower bound: \(\log p_n\le\log p_N\) for \(n\le N\), so the sum is at least \((p_{N+1}-2)/\log p_N\sim N\).

Upper bound: put \(N'=\lfloor N/(\log N)^2\rfloor\). The terms with \(n\le N'\) contribute at most \(\sum_{n\le N'}d_n/\log2\le p_{N'+1}/\log2=O(N'\log N)=o(N)\). For \(N'<n\le N\) we have \(\log p_n\ge\log p_{N'}\ge\log N'\ge\log N-3\log\log N\) for large \(N\), so these terms contribute at most \(p_{N+1}/(\log N-3\log\log N)\sim N\). \(\square\)

**Corollary 1.2.** For every \(C>0\),

\[
\limsup_{N\to\infty}\frac1N\#\{n\le N:d_n>C\log p_n\}\le\frac1C .
\]

**Proof.** Each such \(n\) contributes more than \(C\) to the sum in Proposition 1.1, and the other terms are nonnegative. \(\square\)

Corollary 1.2 bounds the proportion of large gaps from above. A lower bound is much harder: the average of Proposition 1.1 could in principle come from a sparse set of enormous gaps. The record gaps are indeed far larger than the average. Westzynthius showed that \(d_n/\log p_n\) is unbounded, and the methods of Erdős, Rankin, Ford, Green, Konyagin, Maynard and Tao give gaps of size at least a constant times \(\log p\,\log\log p\,\log\log\log\log p/\log\log\log p\) for infinitely many \(n\) [FGKMT]. Such results concern single gaps, not their frequency.

The primes below \(2.5\cdot10^7\) give the following proportions of \(n\) with \(d_n>C\log p_n\), next to the exponential prediction \(e^{-C}\) of Cramér's random model:

| \(C\) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| proportion, \(N=1\,565\,926\) | 0.382 | 0.113 | 0.032 | 0.009 |
| \(e^{-C}\) | 0.368 | 0.135 | 0.050 | 0.018 |

## 2. The theorem and the increases of \(p_n/n\)

**Theorem 2.1** (OpenAI, 2026). For every real \(C>0\) there are constants \(c(C)>0\) and \(N_0(C)\) such that for every integer \(N\ge N_0(C)\),

\[
\#\{1\le n\le N:\ p_{n+1}-p_n>C\log p_n\}\ \ge\ c(C)\,N .
\]

The statement concerns every long initial segment of the sequence of primes, with each gap counted once. In the language of densities: the set of \(n\) with \(d_n>C\log p_n\) has positive lower asymptotic density, where the lower density of a set \(A\) of positive integers is \(\liminf_{N\to\infty}|A\cap[1,N]|/N\).

Erdős and Prachar asked whether the indices at which \(p_n/n\) increases have positive lower density [Erdős–Prachar].

**Corollary 2.2.** The set \(\{n\ge1:\ p_n/n<p_{n+1}/(n+1)\}\) has positive lower density.

**Proof.** Multiplying by \(n(n+1)\), the inequality \(p_n/n<p_{n+1}/(n+1)\) is equivalent to \((n+1)p_n<np_{n+1}\), that is, to \(p_{n+1}-p_n>p_n/n\). From \(n=\pi(p_n)\sim p_n/\log p_n\) we get \(p_n/n\sim\log p_n\), so \(p_n/n<2\log p_n\) for all \(n\) beyond some \(n_1\). Every \(n>n_1\) with \(d_n>2\log p_n\) therefore satisfies \(d_n>p_n/n\). Theorem 2.1 with \(C=2\) gives at least \(c(2)N-n_1\) such \(n\le N\) for large \(N\). \(\square\)

Among the first \(1\,565\,926\) indices, the proportion with \(p_n/n<p_{n+1}/(n+1)\) is \(0.413\).

## 3. Counting gaps through adjacent intervals

Throughout the course \(X\) is an integer tending to infinity, \(\lambda>0\) is fixed, and

\[
L=\log X,\qquad h=\lfloor\lambda L\rfloor,\qquad J=\{1,\dots,h\},\qquad I=\{h+1,\dots,2h\}.
\]

The average over the integers \(m\) with \(X<m\le2X\) is written \(\mathbb E_XA=X^{-1}\sum_{X<m\le2X}A(m)\). Put \(\vartheta(n)=\log n\) if \(n\) is prime and \(\vartheta(n)=0\) otherwise, and for \(B=I\) or \(B=J\)

\[
V_B(m)=\frac1L\sum_{b\in B}\vartheta(m+b).
\]

So \(V_J(m)>0\) exactly when the interval \((m,m+h]\) contains a prime, and \(V_I(m)>0\) exactly when \((m+h,m+2h]\) does. Every prime counted here exceeds \(X\), so \(\vartheta(m+b)/L>1\) for a prime \(m+b\); in particular

\[
V_B(m)\ge\mathbf 1_{\{V_B(m)>0\}} .
\tag{3.1}
\]

Counting starting points \(m\) is not the same as counting gaps. If \(p<p^+\) are consecutive primes with \(p^+-p=G>2h\), then every \(m\) with \(p\le m\le p^+-2h-1\) has no prime in \((m,m+2h]\): one gap produces \(G-2h\) empty starts. A positive proportion of empty starts could therefore come from very few long gaps. The following lemma avoids this by requiring a prime just before the empty interval.

**Lemma 3.1** (adjacent intervals). Let \(h\ge1\). Suppose that for at least \(\delta X\) integers \(m\in(X,2X]\) the interval \((m,m+h]\) contains a prime and \((m+h,m+2h]\) contains none. Then at least \(\delta X/h\) distinct primes \(p\in(X,2X+h]\) are followed by a gap \(p^+-p>h\), where \(p^+\) is the next prime.

**Proof.** For each such \(m\), let \(p(m)\) be the largest prime in \((m,m+h]\). No prime lies in \((p(m),m+h]\) by maximality, and none lies in \((m+h,m+2h]\) by hypothesis. Hence \(p(m)^+>m+2h\ge p(m)+h\). A prime \(p\) can equal \(p(m)\) only if \(m<p\le m+h\), that is, \(p-h\le m\le p-1\): at most \(h\) values of \(m\). So at least \(\delta X/h\) distinct primes occur as \(p(m)\), and all of them lie in \((X,2X+h]\). \(\square\)

For \(X=4\cdot10^6\) and \(\lambda=2\) (so \(h=30\)), there are \(355\,630\) such starts \(m\), and they produce \(27\,374\) distinct primes followed by a gap longer than \(30\), comfortably more than the guaranteed \(355\,630/30\approx11\,854\).

## 4. Weights and the reduction

The lemma asks for many \(m\) with a prime in the first interval and none in the second. These will be found by weighting the integers \(m\) so that, on average, the weight sees a prime in \((m,m+h]\) often and a prime in \((m+h,m+2h]\) rarely.

**Proposition 4.1** (weights for adjacent intervals). For each \(\lambda>0\) there is a finite constant \(K_\lambda>0\) with the following property. For every \(\varepsilon>0\) there are weights \(W_X(m)\ge0\), defined for the integers \(X<m\le2X\), such that as \(X\to\infty\)

\[
\begin{aligned}
&\mathbb E_XW_X\to1,&&\mathbb E_X(W_XV_J)\to\lambda,\\
&\limsup_{X\to\infty}\mathbb E_X(W_XV_I)\le\varepsilon,&&\limsup_{X\to\infty}\mathbb E_X(W_XV_J^2)\le K_\lambda,\\
&\mathbb E_XW_X^2=O_{\lambda,\varepsilon}(1).
\end{aligned}
\]

The constant \(K_\lambda\) does not depend on \(\varepsilon\).

The proof occupies the rest of the course and ends in [Cancellation between adjacent dimensions](cancellation-between-adjacent-dimensions.md). Two features of the statement matter. First, the detector bound \(K_\lambda\) is fixed before the suppression level \(\varepsilon\) is chosen. Second, the bound for \(\mathbb E_XW_X^2\) may grow as \(\varepsilon\) decreases; it is used only after \(\varepsilon\) has been fixed.

**Proof of Theorem 2.1 from Proposition 4.1.** Fix \(C>0\) and put \(\lambda=C+1\). Let \(K=K_\lambda\), choose \(\varepsilon=\lambda^2/(2K)\), and fix the weights given by Proposition 4.1. There are \(M<\infty\) and \(X_1\) with \(\mathbb E_XW_X^2\le M\) for \(X\ge X_1\). Let

\[
A_X=\{m:V_J(m)>0\},\qquad B_X=\{m:V_I(m)>0\}.
\]

Since \(V_J\) vanishes outside \(A_X\), the Cauchy–Schwarz inequality for the nonnegative weight \(W_X\) gives

\[
\bigl(\mathbb E_X(W_XV_J)\bigr)^2=\bigl(\mathbb E_X(W_X\mathbf 1_{A_X}V_J)\bigr)^2\le\mathbb E_X(W_X\mathbf 1_{A_X})\,\mathbb E_X(W_XV_J^2).
\]

For large \(X\) the left side is positive, because it tends to \(\lambda^2\); so the last factor is positive and

\[
\liminf_{X\to\infty}\mathbb E_X(W_X\mathbf 1_{A_X})\ge\frac{\lambda^2}K .
\]

By (3.1), \(\mathbf 1_{B_X}\le V_I\), so \(\mathbb E_X(W_X\mathbf 1_{B_X})\le\mathbb E_X(W_XV_I)\) and

\[
\liminf_{X\to\infty}\mathbb E_X(W_X\mathbf 1_{A_X\setminus B_X})\ge\frac{\lambda^2}K-\varepsilon=\frac{\lambda^2}{2K}=:\Delta>0 .
\]

A second use of Cauchy–Schwarz gives \(\bigl(\mathbb E_X(W_X\mathbf 1_{A_X\setminus B_X})\bigr)^2\le\mathbb E_XW_X^2\cdot|A_X\setminus B_X|/X\). Hence, for all large \(X\),

\[
\frac{|A_X\setminus B_X|}X\ge\frac{(\Delta/2)^2}M=\frac{\Delta^2}{4M}=:\delta>0 .
\]

The integers in \(A_X\setminus B_X\) are exactly the starts in Lemma 3.1, which gives at least \(\delta X/h\) distinct primes \(p\in(X,2X+h]\) with \(p^+-p>h\). For these primes \(\log p\le L+\log3\), while \(h\ge\lambda L-1\), so

\[
h-C\log p\ge(\lambda-C)L-1-C\log3=L-1-C\log3>0
\]

for large \(X\). Each of them therefore begins a gap longer than \(C\log p\).

Let \(N\) be large and put \(X=\lfloor p_N/3\rfloor\). Then \(2X+h\le\frac23p_N+\lambda\log p_N<p_N\), so every prime found above is some \(p_n\) with \(n<N\), and distinct primes give distinct indices. Their number is at least \(\delta X/h\ge\delta X/(\lambda\log X)\). By the prime number theorem \(X/\log X\sim p_N/(3\log p_N)\sim N/3\), so \(X/\log X\ge N/4\) for large \(N\). Hence at least \(\delta N/(4\lambda)\) indices \(n\le N\) satisfy \(d_n>C\log p_n\), and \(c(C)=\delta/(4\lambda)\) works. \(\square\)

All the choices before \(X\) (\(\lambda\), \(K\), \(\varepsilon\), the weights, \(M\), \(\delta\)) depend only on \(C\).

## 5. The plan of the construction

The weight of Proposition 4.1 is \(W_X=Z^2/w\), where \(Z(m)\) is a signed sum, over subsets \(S\) of the second block \(I\), of smooth divisor sums

\[
\sum_{d_s\mid m+s\ (s\in S)}\ \prod_{s\in S}\mu(d_s)\;F\Bigl(\Bigl(\frac{\log d_s}L\Bigr)_{s\in S}\Bigr),
\]

with smooth functions \(F\) supported where \(\sum_s\log d_s/L\) is small. A divisor sum of this kind is large when all the numbers \(m+s\) are free of small prime factors, which is how such sums detect prime tuples. The construction proceeds in five steps, one per lesson.

1. [Divisor sums and primes in progressions](divisor-sums-and-primes-in-progressions.md): the average of a product of such sums, possibly multiplied by \(\vartheta(m+a)\), equals an explicit finite "density sum" up to a negligible error. The prime case uses the Bombieri–Vinogradov theorem.
2. [The singular series and its average](the-singular-series-and-its-average.md): the arithmetic factor \(\mathfrak S(\mathcal H)\) attached to a set of shifts, and Gallagher's theorem that its average over shifts in intervals of length \(h\) tends to \(1\).
3. [Correlations of smooth divisor sums](correlations-of-smooth-divisor-sums.md): the density sums are evaluated by Euler products. The answer is \(L^{-t}\) times \(\mathfrak S(\mathcal H)\) times a constant built from mixed derivatives of the functions \(F\).
4. [A square with little prime mass in the next interval](a-square-with-little-prime-mass-in-the-next-interval.md): the moments of \(Z^2\) against \(1\), \(V_J\), \(V_I\) and \(V_J^2\). A prime \(m+a\) with \(a\in I\) changes \(Z\) in a precise way, which couples neighbouring subset sizes.
5. [Cancellation between adjacent dimensions](cancellation-between-adjacent-dimensions.md): an alternating choice of functions makes these neighbouring terms cancel, so that the prime mass in \(I\) becomes arbitrarily small while the detector bound in \(J\) stays fixed. This proves Proposition 4.1.

## 6. Exercises

**Exercise 6.1.** Show that for every \(C>1\),

\[
\liminf_{N\to\infty}\frac1N\#\{n\le N:d_n\le C\log p_n\}\ge1-\frac1C .
\]

**Exercise 6.2.** Let \(p<p^+\) be consecutive primes with \(p^+-p=G\). Count the integers \(m\) such that \((m,m+h]\) contains a prime and \((m+h,m+2h]\) contains none, and such that the last prime in \((m,m+h]\) is \(p\). Show that the count is \(h\) when \(G>2h\), and \(G-h\) when \(h<G\le2h\).

**Exercise 6.3.** Show that Lemma 3.1 cannot be improved in general: give, for each \(h\ge2\), a configuration of primes (a finite set of integers playing their role) in which every selected prime is selected exactly \(h\) times.

**Exercise 6.4.** Let \(W\ge0\) be a function on a finite set with uniform probability, and let \(U\ge0\) with \(U\ge\mathbf 1_{\{U>0\}}\). Show that \(\mathbb E(W\mathbf 1_{\{U>0\}})\le\mathbb E(WU)\) and \(\mathbb P(U>0)\ge(\mathbb E(W\mathbf 1_{\{U>0\}}))^2/\mathbb E W^2\).

**Exercise 6.5.** Show that the conclusion of Theorem 2.1 for one \(C\) implies it for every \(C'<C\), and that necessarily \(c(C)\le1/C+o(1)\) in the sense of Corollary 1.2.

**Exercise 6.6 (hard).** Suppose only the weaker conclusion \(\limsup_{X\to\infty}|A_X\setminus B_X|/X>0\) were known. Show that the set of \(n\) with \(d_n>C\log p_n\) would then have positive upper density, and explain why the argument of Section 4 needs a lower bound for every large \(X\) to reach every large \(N\).

## 7. Solutions

**6.1.** The complement of the set counted has size at most \((1/C+o(1))N\) by Corollary 1.2.

**6.2.** The last prime in \((m,m+h]\) is \(p\) exactly when \(p-h\le m\le p-1\) and \(p^+>m+h\). An empty second interval means \(p^+>m+2h\). If \(G>2h\), every \(m\le p-1\) satisfies \(m+2h<p+2h<p^+\), so all \(h\) values \(m=p-h,\dots,p-1\) qualify. If \(h<G\le2h\), the condition \(m+2h<p^+=p+G\) means \(m<p+G-2h\), and together with \(m\ge p-h\) this gives \(m=p-h,\dots,p+G-2h-1\): exactly \(G-h\) values.

**6.3.** Take the "primes" \(p_1<p_2<\dots\) with \(p_{i+1}-p_i=3h\) for all \(i\). By Exercise 6.2 (with \(G=3h>2h\)) each \(p_i\) is selected by exactly \(h\) starts, and every start between two of them either has an empty first interval or selects one of them. So the number of selected primes is exactly the number of good starts divided by \(h\).

**6.4.** Since \(U\ge\mathbf 1_{\{U>0\}}\) and \(W\ge0\), \(W\mathbf 1_{\{U>0\}}\le WU\); take expectations. For the second claim, Cauchy–Schwarz gives \((\mathbb E(W\mathbf 1_{\{U>0\}}))^2\le\mathbb E W^2\,\mathbb E\mathbf 1_{\{U>0\}}\).

**6.5.** \(d_n>C\log p_n\) implies \(d_n>C'\log p_n\). The upper bound is Corollary 1.2.

**6.6.** If \(|A_X\setminus B_X|\ge\delta X\) only along a sequence \(X_i\to\infty\), put \(N_i=\pi(3X_i)\). The primes produced by Lemma 3.1 lie below \(2X_i+h<3X_i\), so their indices are at most \(N_i\), and their number is at least \(\delta X_i/h\ge\delta X_i/(\lambda\log X_i)\ge\delta N_i/(4\lambda)\) for large \(i\), by the prime number theorem. This gives \(\#\{n\le N_i:d_n>C\log p_n\}\ge\delta N_i/(4\lambda)\) along the sequence \(N_i\) only: positive upper density. For lower density one needs the count for every large \(N\); the proof chooses \(X=\lfloor p_N/3\rfloor\) as a function of \(N\), so it needs the bound for every large \(X\). This is why Proposition 4.1 is stated with limits as \(X\to\infty\) through all integers.

## References

- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
- [Erdős–Prachar] P. Erdős, K. Prachar, Sätze und Probleme über \(p_k/k\), Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 25 (1962), 251–256. https://www.renyi.hu/~p_erdos/1961-21.pdf
- [FGKMT] K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, Long gaps between primes, Journal of the American Mathematical Society 31 (2018), 65–105. https://arxiv.org/abs/1412.5029
- [BLZ] D. Bazzanella, A. Languasco, A. Zaccagnini, Prime numbers in logarithmic intervals, Transactions of the American Mathematical Society 362 (2010), 2667–2684. https://arxiv.org/abs/0809.2967
