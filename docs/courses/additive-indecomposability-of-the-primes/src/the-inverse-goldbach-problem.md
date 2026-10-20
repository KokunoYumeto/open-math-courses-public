# The inverse Goldbach problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Goldbach's conjecture asks whether every even number greater than \(2\) is a sum of two primes. Ostmann asked an inverse question: can the set of primes itself, up to finitely many exceptions, be written as a sum \(A+B\) of two sets of nonnegative integers? With \(A=\{0\}\) this is trivially possible, so the question is whether both summands can have at least two elements. This course proves that they cannot. The proof, from OpenAI's 2026 paper [OpenAI-013], uses the large sieve, sums of multiplicative characters, Heath-Brown's quadratic large sieve, zero-free regions of Dirichlet \(L\)-functions, and an estimate over finite fields for binary trees of rational maps.

This lesson states the theorem, proves a sieve bound for finitely many shifts, and uses it to show that a decomposition of the primes would need two infinite summands. It ends with the residue supports \(S_p\), which organize the rest of the course, and a map of the proof.

**Prerequisites.** [*The large sieve inequality*](course:NT-DIRL/NT-DIRL-12), Sections 5 and 6; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 2.1 and 3.1.

## 1. Sumsets and the theorem

Throughout the course \(\mathbb P\) denotes the set of positive primes and \(\mathbb N_0=\{0,1,2,\dots\}\). For \(A,B\subseteq\mathbb N_0\) the *sumset* is
\[
A+B=\{a+b:a\in A,\ b\in B\}.
\]
For \(C\subseteq\mathbb N_0\) and real \(Y\) write \(C(Y)=|C\cap[0,Y]|\) for the counting function. Two subsets of \(\mathbb N_0\) are *asymptotically equal* if their symmetric difference is finite, that is, if they agree outside a bounded interval.

**Theorem 1.1** (Ostmann's conjecture [OpenAI-013, Theorem 1.1]). If \(A,B\subseteq\mathbb N_0\) satisfy \(|A|\ge2\) and \(|B|\ge2\), then \((A+B)\mathbin{\triangle}\mathbb P\) is infinite.

Equivalently, no set asymptotically equal to \(\mathbb P\) is a sumset of two sets with at least two elements each: if \(\mathcal Q=A+B\) and \(\mathcal Q\mathbin\triangle\mathbb P\) is finite, then \((A+B)\mathbin\triangle\mathbb P\) is finite.

The condition \(|A|,|B|\ge2\) excludes the decomposition \(\mathbb P=\{0\}+\mathbb P\). Asymptotic equality of \(A+B\) and \(\mathbb P\) consists of two requirements, which the proof uses in different places:

- *coverage*: every sufficiently large prime lies in \(A+B\);
- *exclusion*: every sufficiently large element of \(A+B\) is prime.

Coverage alone is easy to arrange, for instance with \(A=\{0,1\}\) and \(B=\mathbb N_0\). Theorem 1.1 says that the two requirements are incompatible: if \(|A|,|B|\ge2\) and \(A+B\) contains every sufficiently large prime, then \(A+B\) contains infinitely many composite numbers. Neither requirement is replaced by a density condition anywhere in the proof.

The question appears in Ostmann's 1956 treatise on additive number theory, and Elsholtz and Harper record its asymptotic formulation [EH, Definition 1.1 and Conjecture 1.2]; it is also called the inverse Goldbach problem. Laffer and Mann proved that a decomposition must have two infinite summands [LM, Theorem 12]; Lemma 4.1 below gives a short sieve proof of this. Large-sieve arguments, beginning with Pomerance, Sárközy and Stewart [PSS], restricted a hypothetical decomposition further. Elsholtz combined the large sieve with Gallagher's larger sieve to place both counting functions within powers of \(\log x\) of \(\sqrt x\) [Els06, Theorem 1.9]; Lesson 2 proves these bounds. Elsholtz and Harper sharpened them to
\[
\begin{aligned}
\frac{\sqrt x}{\log x\,\log\log x}&\ll A(x),\,B(x)\\
&\ll\sqrt x\,\log\log x
\end{aligned}
\]
[EH, Theorem 2.6]. Bounds of this kind are compatible with the lower bound \(A(x)B(x)\gg x/\log x\) that coverage forces, so they do not by themselves exclude a decomposition. Green and Harper formulated an inverse conjecture for the large sieve and proved that it would imply Theorem 1.1 [GH, Conjecture 1.5 and Theorem 1.8]. Croot, Mao, Pohoata and Yip proved that each summand of a hypothetical decomposition has at least \(\exp(c\sqrt{\log N}/(\log\log N)^{3/2})\) elements of \([1,N]\) in an integral quadratic image \(m\pm\mathbb Z^2\) [CMPY, Theorem 1.10 and Corollary 1.11]. The proof in this course establishes no inverse sieve conjecture. It works directly with the residue restrictions of Section 6 and with coverage of every large prime.

## 2. The large sieve in the form used

Write \(e(x)=e^{2\pi ix}\). Two forms of the large sieve are proved in [*The large sieve inequality*](course:NT-DIRL/NT-DIRL-12). The first, its inequality (5.3), says that for complex numbers \(a_n\) supported on \(M<n\le M+N\) and real \(Q\ge1\),
\[
\begin{aligned}
&\sum_{q\le Q}\ \sum_{\substack{b\bmod q\\ (b,q)=1}}
\Bigl|\sum_n a_n\\
&\qquad \,e(nb/q)\Bigr|^2\\
&\quad \le\bigl(N-1+Q^2\bigr)\sum_n|a_n|^2.\quad(2.1)
\end{aligned}
\]
The second is Montgomery's arithmetic large sieve, inequality (6.3) there. Let \(\mathcal A\subseteq\{M+1,\dots,M+N\}\) have \(Z\) elements, and suppose that for every prime \(p\le Q\) the members of \(\mathcal A\) avoid a set of \(\omega(p)<p\) residue classes modulo \(p\). Put \(g(p)=\omega(p)/(p-\omega(p))\), extend \(g\) multiplicatively to squarefree integers with \(g(1)=1\), and let \(L(Q)=\sum_{q\le Q}\mu^2(q)g(q)\). Then
\[
Z\le\frac{N-1+Q^2}{L(Q)}.
\tag{2.2}
\]

## 3. A sieve for finitely many shifts

**Lemma 3.1** (fixed shifts [OpenAI-013, Lemma 2.1]). Let \(j\ge1\), let \(b_1,\dots,b_j\) be distinct nonnegative integers, and let \(C\subseteq\mathbb N_0\) be a set such that \(c+b_1,\dots,c+b_j\) are all prime for every sufficiently large \(c\in C\). Then
\[
C(Y)\ll\frac{Y}{(\log Y)^j}
\]
for all sufficiently large \(Y\). The implied constant depends only on \(b_1,\dots,b_j\); the threshold for \(Y\) may also depend on the point beyond which the primality holds.

*Proof.* Let \(c_0\) be such that \(c+b_i\) is prime for all \(c\in C\) with \(c>c_0\) and all \(i\). Put \(Q=\sqrt Y\) and \(\mathcal A=C\cap(Q+c_0,Y]\). Fix a prime \(p_0>j+\max_{i,k}|b_i-b_k|\); it depends only on the shifts.

*The avoided classes.* Let \(p\) be a prime with \(p_0<p\le Q\) and let \(c\in\mathcal A\). Each \(c+b_i\) is a prime larger than \(c>Q\ge p\), so \(p\nmid c+b_i\), that is, \(c\not\equiv-b_i\pmod p\). The classes \(-b_1,\dots,-b_j\) modulo \(p\) are distinct because \(p>|b_i-b_k|\) for \(i\ne k\). So \(\mathcal A\) avoids \(\omega(p)=j\) classes modulo \(p\) when \(p_0<p\le Q\); take \(\omega(p)=0\) for \(p\le p_0\). Then \(g(p)=j/(p-j)\) for \(p_0<p\le Q\) and \(g(p)=0\) for \(p\le p_0\). The set \(\mathcal A\) lies in an interval of at most \(Y+1\) integers, so (2.2) gives
\[
|\mathcal A|\le\frac{Y+Q^2}{L(Q)}=\frac{2Y}{L(Q)}.
\tag{3.1}
\]

*A lower bound for \(L(Q)\).* Put \(y=Q^{1/(10j)}\), and let \(\mathcal U\) be the set of squarefree integers all of whose prime factors lie in \((p_0,y]\), including \(1\). For large \(Y\) every prime factor of \(u\in\mathcal U\) is at most \(Q\), and \(g(u)=\prod_{p\mid u}j/(p-j)\). Let
\[
\begin{aligned}
G&=\sum_{u\in\mathcal U}g(u)=\prod_{p_0<p\le y}\bigl(1+g(p)\bigr)\\
&=\prod_{p_0<p\le y}\frac p{p-j}.
\end{aligned}
\]
Since \(-\log(1-x)\ge x\) for \(0\le x<1\), Mertens' estimate \(\sum_{p\le y}1/p=\log\log y+O(1)\) ([*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1) gives
\[
\log G\ge j\sum_{p_0<p\le y}\frac1p\ge j\log\log y-c_1,
\]
with \(c_1\) depending only on \(j\) and \(p_0\). Thus \(G\ge e^{-c_1}(\log y)^j\).

Consider the probability measure on \(\mathcal U\) that gives \(u\) the mass \(g(u)/G\). Because \(G\) is a product over the primes of \((p_0,y]\) and \(g\) is multiplicative, this is the law of a random product in which each prime \(p\in(p_0,y]\) is included independently with probability
\[
\frac{g(p)}{1+g(p)}=\frac jp.
\]
Mertens' estimate \(\sum_{p\le y}(\log p)/p=\log y+O(1)\) from the same theorem gives
\[
\begin{aligned}
\mathbb E\log u&=\sum_{p_0<p\le y}\frac jp\log p\\
&\le j\log y+O(j)\\
&=\frac{\log Q}{10}+O(j).
\end{aligned}
\]
By Markov's inequality, \(\Pr(u>Q)\le\mathbb E\log u/\log Q\)\(\le\frac1{10}+O(j/\log Q)\), which is at most \(\frac12\) for large \(Y\). Every \(u\in\mathcal U\) with \(u\le Q\) is a squarefree integer at most \(Q\), and the terms of \(L(Q)\) are nonnegative, so
\[
\begin{aligned}
L(Q)&\ge\sum_{\substack{u\in\mathcal U\\u\le Q}}g(u)\\
&=G\Pr(u\le Q)
\ge\frac G2\\
&\ge\frac{e^{-c_1}}2\left(\frac{\log Y}{20j}\right)^j.
\end{aligned}
\]

*Conclusion.* By (3.1), \(|\mathcal A|\ll Y/(\log Y)^j\) with a constant depending only on the shifts. The points of \(C\cap[0,Y]\) outside \(\mathcal A\) number at most \(Q+c_0+1=O(\sqrt Y)\) for large \(Y\), which is also \(O(Y/(\log Y)^j)\). \(\square\)

For \(j=1\) and \(b_1=0\), with \(C=\mathbb P\), the lemma is the upper bound \(\pi(Y)\ll Y/\log Y\). For \(j=2\) and the shifts \(0,2\) it is the upper bound \(\#\{p\le Y:p+2\in\mathbb P\}\ll Y/(\log Y)^2\) for twin primes.

## 4. Finite summands

**Lemma 4.1** (finite summands; Laffer and Mann [LM, Theorem 12], [OpenAI-013, Lemma 2.2]). If \(A,B\subseteq\mathbb N_0\) have at least two elements each and \(A+B\) is asymptotically equal to \(\mathbb P\), then \(A\) and \(B\) are infinite.

*Proof.* Suppose that \(A\) is finite. Coverage forces \(A+B\) to be infinite, so \(B\) is infinite. Choose \(a_1\ne a_2\) in \(A\), and a threshold \(N\) beyond which every element of \(A+B\) is prime and every prime lies in \(A+B\). For \(b\in B\) with \(b>N\), the numbers \(b+a_1\) and \(b+a_2\) lie in \(A+B\) and exceed \(N\), so both are prime. Lemma 3.1 with \(C=B\) and the shifts \(a_1,a_2\) gives
\[
B(Y)\ll\frac{Y}{(\log Y)^2}.
\]
On the other hand, every prime \(p\in(N,Y]\) has a representation \(p=a+b\) with \(a\in A\) and \(b\in B\), and \(b\le p\le Y\) because \(a\ge0\). So the map \((a,b)\mapsto a+b\) from \(A\times(B\cap[0,Y])\) covers all primes in \((N,Y]\), and
\[
\pi(Y)-\pi(N)\le|A|\,B(Y).
\]
Chebyshev's lower bound \(\pi(Y)\gg Y/\log Y\) ([*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 2.1) gives \(Y/\log Y\ll|A|\,B(Y)\ll Y/(\log Y)^2\), which fails for large \(Y\). If \(B\) is finite, exchange the roles of \(A\) and \(B\). \(\square\)

## 5. Two infinite summands

**Theorem 5.1** (two infinite summands [OpenAI-013, Theorem 2.3]). There are no infinite sets \(A,B\subseteq\mathbb N_0\) such that \((A+B)\mathbin{\triangle}\mathbb P\) is finite.

Theorem 5.1 and Lemma 4.1 together prove Theorem 1.1: a counterexample to Theorem 1.1 would have two infinite summands by Lemma 4.1, contradicting Theorem 5.1.

The remaining seventeen lessons prove Theorem 5.1 by contradiction.

**Standing assumption.** Throughout the rest of the course, \(A\) and \(B\) are infinite subsets of \(\mathbb N_0\) such that \((A+B)\mathbin\triangle\mathbb P\) is finite. Fix an integer \(N\ge1\) with
\[
\begin{gathered}
\mathbb P\cap(N,\infty)\subseteq A+B,\\
(A+B)\cap(N,\infty)\subseteq\mathbb P,\quad(5.1)
\end{gathered}
\]
fix an integer \(N_*>N+10\), and put
\[
D=-B=\{-b:b\in B\}.
\]
Thus \(A+B=A-D\)\(=\{a-d:a\in A,\ d\in D\}\). The first inclusion in (5.1) is coverage and the second is exclusion. Constants implied by \(O(\cdot)\) and \(\ll\) may depend on these fixed data. Where the order in which parameters are chosen matters, the additional dependence is stated.

## 6. Complementary residue supports

**Lemma 6.1.** For every prime \(p\), the residue sets
\[
\begin{gathered}
\begin{aligned}
\mathcal A_p&=\{a\bmod p:a\in A,\ a>p\\
&\quad +N_*\},
\end{aligned}\\
\begin{aligned}
\mathcal D_p&=\{d\bmod p:d\in D,\ -d>p\\
&\quad +N_*\}
\end{aligned}
\end{gathered}
\]
are nonempty and disjoint.

*Proof.* Both sets are nonempty because \(A\) and \(D\) are infinite. Suppose \(a\equiv d\pmod p\) with \(a\in A\), \(d\in D\), \(a>p+N_*\) and \(-d>p+N_*\). Then \(n=a-d\) lies in \(A+B\), is divisible by \(p\), and satisfies \(n>2p+2N_*>\max(p,N)\). By exclusion \(n\) is prime, and a prime divisible by \(p\) equals \(p\). This contradicts \(n>p\). \(\square\)

**Definition 6.2.** For every prime \(p\) fix a partition \(\mathbb F_p=S_p\sqcup S_p^c\) with \(\mathcal A_p\subseteq S_p\) and \(\mathcal D_p\subseteq S_p^c\). Residues in neither set may be put in either part. Put
\[
\sigma_p=\frac{|S_p|}p.
\]
By Lemma 6.1, \(0<\sigma_p<1\).

These partitions are fixed for the whole course; every later statement holds for any admissible choice. For \(p=2\) the partition is forced: the large elements of \(A\) all have one parity, and the large elements of \(B\) have the other, as they must, since \(a+b\) is an odd prime.

Two features of the supports drive the proof. First, the summands are close to uniformly distributed on them: by Lesson 2, the reductions modulo \(p\) of the large elements of \(A\) are nearly uniform on \(S_p\), those of \(D\) are nearly uniform on \(S_p^c\), and \(\sigma_p\) is close to \(\tfrac12\), all in an averaged sense over primes. Second, the normalized indicator
\[
F_p(x)=\frac{\mathbf 1_{S_p}(x)-\sigma_p}{\sqrt{\sigma_p(1-\sigma_p)}}
\]
has a Fourier transform with competing properties. It correlates with no translated multiplicative character (Lessons 3–9), but its \(L^1\) norm is bounded below for many primes (Lessons 10–11). Lessons 12–18 build from these transforms a positive quantity whose size is forced in two incompatible directions.

## 7. A map of the proof

- **Lesson 2.** Counting functions: \(\sqrt Y/(\log Y)^3\)\(\ll A(Y),B(Y)\)\(\ll\sqrt Y(\log Y)^2\). Collision stability: a weighted larger sieve showing that the summands are nearly uniform on \(S_p\) and \(S_p^c\).
- **Lessons 3–6.** Quadratic characters: for the quadratic character \(\chi_p\) of \(\mathbb F_p\), the maximal translated bias \(\max_t|\mathbb E_{x\in S_p}\chi_p(x-t)|\) is small on average over primes. The translations may differ from prime to prime; an amplified moment, Poisson summation and Weyl differencing force a common rational centre, and the quadratic large sieve then leads to a collision contradiction.
- **Lessons 7–9.** Characters of order greater than \(2\): the same conclusion, by repeated Cauchy–Schwarz transfers whose diagonal terms are controlled by anchor primes. Together these give the *mixed flatness* of the normalized transforms.
- **Lessons 10–11.** A supply of nonsparse transforms: coverage of every large prime forces many primes for which the normalized transform has \(L^1\) norm bounded below.
- **Lessons 12–13.** A comparison estimate for binary trees of rational maps over \(\mathbb F_q\), which uses only an \(L^2\) bound and mixed flatness.
- **Lessons 14–17.** A positive statistic built from the nonsparse transforms, its binary-tree transfers, and two comparison estimates proved by separating the arithmetic of all the prime variables.
- **Lesson 18.** Averaging over permutations of the variables gives an upper bound that contradicts the lower bound carried through the transfers.

The analytic inputs are proved in the programme courses on the Riemann zeta function and on Dirichlet \(L\)-functions. The one input from outside the programme is Heath-Brown's quadratic large sieve, used in Lesson 6 as named result N1.

## 8. Exercises

**8.1.** Under the standing assumption, show that for every prime \(p\), \(\min(|\mathcal A_p|,|\mathcal D_p|)\le p/2\). Deduce that the large elements of one of the two sets \(A,B\) lie in a single residue class modulo \(3\).

**8.2.** Under the standing assumption, show that for every fixed \(j\ge1\),
\[
\begin{gathered}
A(Y)\ll_j\frac{Y}{(\log Y)^j}\\
\text{and}\\
A(Y)\gg_j(\log Y)^j,
\end{gathered}
\]
and the same for \(B\).

**8.3.** Let \(h\ge1\). Show that \(\#\{p\le Y:p\in\mathbb P,\ p+2h\in\mathbb P\}\)\(\ll_h Y/(\log Y)^2\), with an implied constant depending on \(h\).

**8.4.** Let \(A\) be finite with \(|A|\ge2\) and suppose that every sufficiently large element of \(A+B\) is prime, where \(B\subseteq\mathbb N_0\) is infinite. Show that \(\sum_{b\in B,\,b\ge2}1/b\) converges.

## 9. Solutions

**8.1.** By Lemma 6.1, \(\mathcal A_p\) and \(\mathcal D_p\) are disjoint subsets of \(\mathbb F_p\), so \(|\mathcal A_p|+|\mathcal D_p|\le p\), and the smaller one has at most \(p/2\) elements. For \(p=3\) the smaller set has one element. If it is \(\mathcal A_3\), all elements \(a>3+N_*\) of \(A\) lie in one class modulo \(3\). If it is \(\mathcal D_3\), all elements \(d<-(3+N_*)\) of \(D\) lie in one class, and so do the corresponding elements \(-d\) of \(B\).

**8.2.** Choose distinct \(a_1,\dots,a_j\in A\), possible since \(A\) is infinite. For \(b\in B\) with \(b>N\), each \(b+a_i\) lies in \(A+B\) and exceeds \(N\), hence is prime. Lemma 3.1 gives \(B(Y)\ll_j Y/(\log Y)^j\), and by symmetry \(A(Y)\ll_jY/(\log Y)^j\). Every prime in \((N,Y]\) is \(a+b\) with \(a\in A\cap[0,Y]\), \(b\in B\cap[0,Y]\), so \(A(Y)B(Y)\ge\pi(Y)-\pi(N)\gg Y/\log Y\). Dividing by the upper bound for \(B\) with \(j+1\) in place of \(j\) gives \(A(Y)\gg_j(\log Y)^{j}\).

**8.3.** Apply Lemma 3.1 to \(C=\{p\in\mathbb P:p+2h\in\mathbb P\}\) with \(j=2\) and the shifts \(0,2h\): for every \(c\in C\), both \(c+0\) and \(c+2h\) are prime. The implied constant depends only on the shifts, that is, on \(h\).

**8.4.** By the proof of Lemma 4.1, \(B(Y)\le KY/(\log Y)^2\) for \(Y\ge Y_0\), with a constant \(K\). Partial summation gives, for \(Y\ge Y_0\),
\[
\begin{aligned}
\sum_{\substack{b\in B\\2\le b\le Y}}\frac1b&=\frac{B(Y)-B(1)}{Y}\\
&\quad +\int_2^Y\frac{B(t)-B(1)}{t^2}\,dt\\
&\le O(1)+K\int_{Y_0}^{Y}\frac{dt}{t(\log t)^2},
\end{aligned}
\]
and the last integral is bounded by \(1/\log Y_0\). So the series converges. (For \(Y_0\le t\), \(B(t)\le Kt/(\log t)^2\); the integral over \([2,Y_0]\) is a constant.)

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 1 and Sections 2.1–2.3. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [EH] C. Elsholtz and A. J. Harper, *Additive decompositions of sets with restricted prime factors*, Trans. Amer. Math. Soc. (2015), Definition 1.1, Conjecture 1.2 and Theorem 2.6; authors' version. https://www.math.tugraz.at/~elsholtz/WWW/papers/papers49selsholtz-harper.pdf
- [LM] W. B. Laffer and H. B. Mann, *Decomposition of sets of group elements*, Pacific J. Math. 14 (1964), no. 2, Theorem 12. https://msp.org/pjm/1964/14-2/pjm-v14-n2-p15-p.pdf
- [PSS] C. Pomerance, A. Sárközy and C. L. Stewart, *On divisors of sums of integers, III*, Pacific J. Math. 133 (1988). https://math.dartmouth.edu/~carlp/PDF/paper68.pdf
- [Els06] C. Elsholtz, *Additive decomposability of multiplicatively defined sets*, Funct. Approx. Comment. Math. 35 (2006), 61–77, Theorem 1.9. https://www.math.tugraz.at/~elsholtz/WWW/papers/papers22wirsing04.pdf
- [GH] B. Green and A. J. Harper, *Inverse questions for the large sieve*, Geom. Funct. Anal. 24 (2014), numbering of arXiv:1311.6176v1: Conjecture 1.5 and Theorem 1.8. https://arxiv.org/abs/1311.6176v1
- [CMPY] E. Croot, J. Mao, C. Pohoata and C. H. Yip, *A sharp inverse theorem for the quadratic large sieve*, arXiv:2607.15311v2 (2026), Theorem 1.10 and Corollary 1.11. https://arxiv.org/abs/2607.15311v2
