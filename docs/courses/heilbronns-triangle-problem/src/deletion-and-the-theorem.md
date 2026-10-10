# Deletion and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lessons bound the probability that two samples have the same projected point (Lemma 1.1 of [Sampling integer columns](sampling-integer-columns.md)) and that three samples form a bad triple, with distinct projections and a determinant of absolute value at most \(\tau\) (Corollary 3.2 there). This lesson takes about \(2n\) samples with \(n\approx r\sqrt{N^3/\tau}\), deletes one sample from every bad pair or triple, and keeps \(n\) points whose triangles all have area at least \(\tau/(16N^3)\). Comparing \(n\) with this area gives \(n^2\Delta\geq r^2/64\); since every parameter is a fixed power of the prime \(r\) up to constants, \(r^2\) is a fixed power of \(n\). A prime in an interval then passes from these special \(n\) to every large \(n\). This proves Theorem 1.3 of [Small triangles and the plan](small-triangles-and-the-plan.md).

## 1. Deleting the bad events

Keep the parameters of the previous lessons, with \(d=41\) and \(k=T^2+1\geq2\). Since \(B\) is an odd prime and \(k\geq2\), \(B^{k-1}\geq3\); so \(\tau\geq1\) and
\[
\frac{B^{k-1}}3\leq\tau\leq\frac{B^{k-1}}2 .\tag{1.1}
\]
Put
\[
\begin{gathered}
a_r=r\sqrt{N^3/\tau},\\
n_r=\lfloor a_r\rfloor .
\end{gathered}\tag{1.2}
\]
Take \(2n_r\) samples with the shared choices and conditional draws of the sixth lesson. Let \(Z\) be the number of unordered pairs of samples with equal projected points plus the number of unordered bad triples.

**Lemma 1.1.** \(\mathbb EZ=o(n_r)\) as \(r\to\infty\).

*Proof.* There are at most \(2n_r^2\) pairs and \(\frac43n_r^3\) triples, so by linearity of expectation (no independence between the events is needed) and the two bounds of the sixth lesson,
\[
\begin{aligned}
\frac{\mathbb EZ}{n_r}&\leq C\,n_r\frac{(hq)^6}{N^3}\\
&\quad+C\,n_r^2\bigl(\log(2N)\bigr)^2\frac h{N^3r^d}.
\end{aligned}
\]
For the first term, \(n_r\leq rN^{3/2}\tau^{-1/2}\) and \(N=(hq)^{10}\) give \(n_r(hq)^6N^{-3}\leq r(hq)^{-9}\to0\), as \(r\leq h\). For the second, \(n_r^2\leq r^2N^3/\tau\) gives the bound \((\log(2N))^2\frac h\tau r^{2-d}\). By (1.1), \(h/\tau\leq3B\leq600k^2r^{30}\). Also \(\log(2N)\leq C_k\log r\), since \(N=(hq)^{10}\), \(q\leq2h^{100}\) and \(h=B^k\leq(200k^2r^{30})^k\). With \(d=41\) the second term is at most \(C_k(\log r)^2r^{32-41}\to0\). \(\square\)

So for all large \(r\) some outcome of the random construction has \(Z<n_r\). Fix such an outcome. For every pair of samples with equal projections and every bad triple, *mark* one of its samples; at most \(Z<n_r\) samples are marked, so at least \(n_r\) unmarked samples remain. Keep \(n_r\) of them and let \(P_r\subseteq[0,1)^2\) be the set of their projections.

**Lemma 1.2.** \(|P_r|=n_r\) and
\[
\Delta(P_r)\geq\frac\tau{16N^3}.
\]

*Proof.* Two kept samples have different projections, since otherwise one of them would be marked; so \(|P_r|=n_r\). Three kept samples have pairwise distinct projections and do not form a bad triple, so their matrix \(A\) has \(|\det A|>\tau\). By the area formula (Lemma 2.1 of the first lesson) and \(N\leq A_{3j}<2N\),
\[
\operatorname{Area}=\frac{|\det A|}{2A_{31}A_{32}A_{33}}>\frac\tau{2(2N)^3}.\qquad\square
\]
In particular no three points of \(P_r\) are collinear.

Since \(N\geq h^{10}\) and \(\tau<h\), \(a_r>rh^{29/2}\to\infty\), so \(n_r\geq a_r/2\) for large \(r\). With Lemma 1.2,
\[
\begin{aligned}
n_r^2\Delta(P_r)&\geq\frac{a_r^2}4\cdot\frac\tau{16N^3}\\
&=\frac{r^2}{64}.
\end{aligned}\tag{1.3}
\]

## 2. The exponent

**Lemma 2.1 (size of \(n_r\)).** Put \(\beta=1515k-\frac{k-1}2=\frac{3029k+1}2\) and \(\alpha=1+30\beta=45435k+16\). There are constants \(A_k,D_k>0\) such that, for all large primes \(r\),
\[
A_kr^\alpha\leq n_r\leq D_kr^\alpha .\tag{2.1}
\]

*Proof.* \(N^{3/2}=(hq)^{15}\) with \(h^{100}<q\leq2h^{100}\), so \(h^{1515}<N^{3/2}\leq2^{15}h^{1515}=2^{15}B^{1515k}\); and by (1.1), \(\sqrt2\,B^{-(k-1)/2}\leq\tau^{-1/2}\leq\sqrt3\,B^{-(k-1)/2}\). Hence \(\sqrt2\,rB^\beta<a_r\leq2^{15}\sqrt3\,rB^\beta\). Since \(100k^2r^{30}<B\leq200k^2r^{30}\), \(B^\beta\) lies between two constant multiples of \(r^{30\beta}\). With \(a_r/2\leq n_r\leq a_r\) this gives (2.1). \(\square\)

Put
\[
\eta=\frac2\alpha=\frac2{45435k+16}.\tag{2.2}
\]
By (2.1), \(r^\alpha\geq n_r/D_k\), so \(r^2=(r^\alpha)^\eta\geq D_k^{-\eta}n_r^\eta\), and (1.3) becomes
\[
\Delta(P_r)\geq c_*\,n_r^{-2+\eta}\tag{2.3}
\]
with \(c_*=1/(64D_k^\eta)\).
With \(d=41\), \(M=\binom{163}{41}\approx10^{38.8}\), \(T=\binom M3\approx10^{115.6}\) and \(k=T^2+1\approx10^{231.1}\); so \(\eta\approx10^{-235.5}\). It is explicit and positive, and no attempt was made to make it large.

## 3. Every large number of points

*Proof of Theorem 1.3 of the first lesson.* Let \(n\) be large and put \(m=\lceil(n/A_k)^{1/\alpha}\rceil\). By Lemma 4.3 of the first lesson there is a prime \(r\) with \(m<r\leq2m\); for large \(n\) it is large enough for all the constructions above. Since \((n/A_k)^{1/\alpha}\geq1\), \(m\leq2(n/A_k)^{1/\alpha}\), and (2.1) gives
\[
\begin{aligned}
n&\leq A_km^\alpha\leq A_kr^\alpha\leq n_r\\
&\leq D_kr^\alpha\leq D_k(2m)^\alpha\leq\frac{4^\alpha D_k}{A_k}\,n .
\end{aligned}
\]
So \(n\leq n_r\leq C_kn\) with \(C_k=\max\{1,4^\alpha D_k/A_k\}\); this uses only the two-sided bounds, not any monotonicity of \(n_r\). Keep any \(n\) points of \(P_r\): deleting points cannot decrease the smallest triangle area. Since \(-2+\eta<0\), (2.3) gives
\[
\Delta(n)\geq c_*n_r^{-2+\eta}\geq c_*C_k^{-2+\eta}n^{-2+\eta}.
\]
Take \(c_1=c_*C_k^{-2+\eta}\). All constants depend only on \(k\), which is fixed. \(\square\)

**Remark 3.1 (the deletion argument).** Komlós, Pintz and Szemerédi needed a hypergraph independence lemma to delete the small triangles of a random set. Here the expected number of bad events is already \(o(n)\), and the elementary alteration (delete one point of each) suffices; the gain comes entirely from the arithmetic distribution of the sampled points.

**Remark 3.2 (formal verification).** OpenAI's release contains a Lean formalization. According to its scope document, it constructs an unbounded sequence of sizes \(n\) and point sets for which every triangle has area at least \(n^{-2+\eta}\) for one fixed \(\eta>0\), which already refutes the bound (1.1) of the first lesson for every \(\varepsilon>0\). The formal statement concerns an unbounded sequence of sizes, like the sizes \(n_r\) here. The statement for every large \(n\) (Section 3) is proved in the paper and in this course, but it is not part of the linked formal statement.

## 4. Exercises

**4.1.** Show that \(\lfloor x/2\rfloor\geq x/3\) for every integer \(x\geq3\), as used in (1.1).

**4.2.** Why does the argument need an outcome with \(Z<n_r\), rather than only \(\mathbb EZ\) small? What would go wrong with \(n_r\) samples instead of \(2n_r\)?

**4.3.** Check the computation of \(\alpha\) from \(\beta\): \(1+30\cdot\frac{3029k+1}2=45435k+16\).

**4.4.** Show that deleting points from a set \(P\) with at least three points cannot decrease \(\Delta(P)\).

**4.5.** Suppose the label field had \(r^d\) elements with \(d=31\) instead of \(41\). Which step of the proof fails?

## 5. Solutions

**4.1.** For even \(x\), \(\lfloor x/2\rfloor=x/2\geq x/3\). For odd \(x\geq3\), \(\lfloor x/2\rfloor=(x-1)/2\geq x/3\) because \(3(x-1)\geq2x\), that is \(x\geq3\).

**4.2.** A small expectation only says that *some* outcome has few bad events (if every outcome had \(Z\geq n_r\), the expectation would be at least \(n_r\)). The construction needs one concrete point set. With \(n_r\) samples, deleting up to \(Z\) of them would leave fewer than \(n_r\) points; doubling the number of samples changes \(\mathbb EZ/n_r\) only by a constant factor.

**4.3.** \(30\cdot\frac{3029k+1}2=15(3029k+1)\), which is \(45435k+15\); add \(1\).

**4.4.** \(\Delta(P)\) is a minimum over the triples of \(P\); a subset has fewer triples, and a minimum over a subset of a set of numbers is at least the minimum over the whole set.

**4.5.** The second term in Lemma 1.1 is \(C_k(\log r)^2r^{2-d}\cdot h/\tau\) with \(h/\tau\) of order \(r^{30}\); it tends to zero only if \(d>32\). With \(d=31\) the expected number of bad triples would not be \(o(n_r)\). The exponent \(30\) comes from \(B\approx L^3=r^{30}\); \(d=41\) leaves a margin of \(r^{-9}\).

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
- [OpenAI-Lean] OpenAI Math Release, *A power improvement in the Heilbronn triangle lower bound*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/191.md
- J. Komlós, J. Pintz and E. Szemerédi (1982) are named for credit for the earlier logarithmic improvement; the course does not use their results.
