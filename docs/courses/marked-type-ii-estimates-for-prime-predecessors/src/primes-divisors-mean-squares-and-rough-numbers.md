# Primes, divisors, mean squares and rough numbers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson collects the elementary analytic facts used throughout the course: primes in short ranges and progressions of small modulus, sizes of the bands of Lesson 1, moments of the divisor function, mean values of Dirichlet polynomials, counts of rough integers, and the comparison of a sum of \(n^{it}\) over a progression with an integral. The mean value estimates are stated with constants that do not depend on the coefficients; Lesson 17 applies them to a polynomial raised to a power that grows with \(x\).

**Prerequisites.** [*The marked Type II estimate*](the-marked-type-ii-estimate.md), Section 1; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 3.1 and 4.2; [*The Siegel–Walfisz theorem*](course:NT-DIRL/NT-DIRL-11), Theorem 2.1; [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09), Theorem 3.1; [*Mean values of Dirichlet polynomials and zeta*](course:NT-ZETA/NT-ZETA-16), Theorem 2.1.

We keep the notation of Lesson 1: \(L=\log x\), \(W=\exp(L^{0.24})\), \(V(W)=\prod_{p\le W}(1-1/p)\), the groups \(\mathcal P_i\) and their masses \(V_i\).

## 1. Primes

**Lemma 1.1 (primes in progressions on short ranges).** Fix \(\delta_1>0\), \(A_0>0\) and \(A>0\). For large \(x\), uniformly for \(x^{\delta_1}\le N\le x^{1/\delta_1}\), moduli \(q\le L^{A_0}\), residues \(a\) with \((a,q)=1\), and intervals \(I\subseteq[N,2N]\),

\[
\begin{gathered}
\#\{p\in I:\ p\equiv a\ (q)\}=\frac1{\varphi(q)}\int_I\frac{dy}{\log y}\\
+O(NL^{-A}).\quad(1.1)
\end{gathered}
\]

For every Dirichlet character \(\chi\) of modulus \(q\le L^{A_0}\),

\[
\begin{gathered}
\sum_{p\in I}\chi(p)=\mathbf 1_{\chi\ \text{principal}}\int_I\frac{dy}{\log y}\\
+O(NL^{-A}).\quad(1.2)
\end{gathered}
\]

**Proof.** Put \(\theta(y;q,a)=\sum_{p\le y,\,p\equiv a\,(q)}\log p\) and let \(\psi(y;q,a)\) be the corresponding sum of \(\Lambda(n)\). The prime powers \(p^k\le y\) with \(k\ge2\) number at most \(\sqrt y\log_2y\), so \(0\le\psi-\theta\le2\sqrt y\log^2y\). For \(y\in[N,2N]\) we have \(\log y\ge\delta_1L\), hence \(q\le L^{A_0}\le(\log y)^{A_0+1}\) for large \(x\). The Siegel–Walfisz theorem (Theorem 2.1 of [*The Siegel–Walfisz theorem*](course:NT-DIRL/NT-DIRL-11)) therefore gives \(\theta(y;q,a)=y/\varphi(q)+E(y)\) with

\[
\begin{gathered}
|E(y)|\le E_*\quad(N\le y\le2N),\\
E_*:=C_{A_0}N\exp\bigl(-c\sqrt{\delta_1L}\bigr).
\end{gathered}
\]

Let \(I=(y_1,y_2]\); endpoints change the count by at most two. Stieltjes integration gives

\[
\begin{aligned}
\#\{p\in I:\ p\equiv a\}
&=\Bigl[\frac{\theta(y)}{\log y}\Bigr]_{y_1}^{y_2}\\
&\quad+\int_{y_1}^{y_2}\frac{\theta(y)\,dy}{y\log^2y}.
\end{aligned}
\]

The term \(y/\varphi(q)\) contributes exactly \(\varphi(q)^{-1}\int_I dy/\log y\), because \(y/\log y\) is an antiderivative of \(1/\log y-1/\log^2y\). The term \(E\) contributes at most \(2E_*/\log N\)\(+E_*\int_N^{2N}dy/(y\log^2y)\le3E_*\), which is \(O(NL^{-A})\). This proves (1.1).

For (1.2), every prime \(p\ge N\) exceeds \(q\), so \(\chi(p)=\sum_{a}\chi(a)\mathbf 1_{p\equiv a}\) over the reduced residues \(a\). Summing (1.1) with these weights, the main terms add up to \(\varphi(q)^{-1}\sum_a\chi(a)\int_Idy/\log y\), which is \(\int_Idy/\log y\) for the principal character and \(0\) otherwise. The \(\varphi(q)\le L^{A_0}\) error terms are absorbed by applying (1.1) with \(A+A_0\) in place of \(A\). \(\square\)

**Lemma 1.2 (bands and small primes).** For large \(x\):

1. \(V(W)=(1+o(1))e^{-\gamma}L^{-0.24}\); in particular \(1/V(W)\le2L^{0.24}\);
2. \(S_W:=\sum_{p\le W}1/p\le\log L\);
3. \(\sum_p p^{-2}\le2\exp(-L^{0.1})\), the sum over all group primes, and \(\mu_i(p)\le2\exp(-L^{0.1})\) for every group prime \(p\in\mathcal P_i\);
4. \(|\mathcal P_i|\le\exp(2L^{a_i})\) and \(\sum_{p\in\mathcal P_i}1/(p+1)\le V_i\).

**Proof.** Part 1 is Mertens' product (Theorem 4.2 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)) at \(\log W=L^{0.24}\). Part 2 follows from Mertens' estimate \(\sum_{p\le y}1/p=\log\log y+O(1)\) at \(\log\log W=0.24\log L\). For part 3, group primes are at least \(\exp(L^{0.1})\) by Lemma 1.1 of Lesson 1, and \(\sum_{n>y}n^{-2}\le2/y\) for \(y\ge2\); also \(\mu_i(p)=1/(pV_i)\) and \(V_i\ge\frac12\). Part 4 is immediate. \(\square\)

**Lemma 1.3 (primes in dyadic intervals).** There is an absolute \(y_0\) such that \([y,2y]\) contains at least \(y/(2\log y)\) primes for every \(y\ge y_0\).

**Proof.** By the prime number theorem (Theorem 3.1 of [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09)), \(\pi(2y)-\pi(y)\)\(=(1+o(1))(2y/\log2y-y/\log y)\)\(=(1+o(1))y/\log y\). \(\square\)

## 2. Divisor moments

Let \(\tau(n)\) be the number of divisors of \(n\) and \(\tau_j(n)\) the number of ordered factorizations \(n=d_1\cdots d_j\) into \(j\) positive integers.

**Lemma 2.1 (moments).** For every integer \(k\ge0\) and \(Y\ge1\),

\[
\begin{gathered}
\sum_{n\le Y}\frac{\tau(n)^k}n\ll_k(\log 2Y)^{2^k},\\
\sum_{n\le Y}\tau(n)^k\ll_kY(\log2Y)^{2^k}.\quad(2.1)
\end{gathered}
\]

Moreover \(\sum_{n\le Y}\tau_3(n)/n\le(1+\log Y)^3\) and \(\sum_{n\le Y}\tau_3(n)\le Y(1+\log Y)^2\).

**Proof.** By unique factorization and positivity,

\[
\begin{aligned}
\sum_{n\le Y}\frac{\tau(n)^k}n
&\le\prod_{p\le Y}\sum_{a\ge0}\frac{(a+1)^k}{p^a}\\
&\le\prod_{p\le Y}\Bigl(1+\frac{2^k}p+\frac{c_k}{p^2}\Bigr),
\end{aligned}
\]

where \(c_k=\sup_p\sum_{a\ge2}(a+1)^kp^{2-a}<\infty\). Taking logarithms and using \(\sum_{p\le Y}1/p\le\log\log(2Y)+O(1)\) gives the first bound. The second follows on multiplying each term by \(Y/n\ge1\). For \(\tau_3\), \(\sum_{n\le Y}\tau_3(n)/n\le(\sum_{d\le Y}1/d)^3\), and \(\sum_{n\le Y}\tau_3(n)\)\(=\sum_{d_1d_2\le Y}\lfloor Y/(d_1d_2)\rfloor\)\(\le Y(\sum_{d\le Y}1/d)^2\), with \(\sum_{d\le Y}1/d\le1+\log Y\). \(\square\)

**Lemma 2.2 (divisors in a progression).** Let \(l\ge1\), \(H'\ge1\) and \(Z\ge2\) with \(1+lH'\le Z\). Then

\[
\begin{aligned}
&\sum_{1\le h\le H'}\tau(1+lh)^2\\
&\quad\le4H'(1+\log Z)^3\\
&\qquad+4Z^{3/4}(1+\log Z)^2.\quad(2.2)
\end{aligned}
\]

**Proof.** First, \(\tau(n)^2\le\tau_4(n)\): both sides are multiplicative, and at a prime power \(p^e\) the inequality reads \((e+1)^2\le\binom{e+3}3\), that is \(6(e+1)\le(e+2)(e+3)\), which holds for all \(e\ge0\). In an ordered factorization \(n=d_1d_2d_3d_4\) choose an index \(j\) with \(d_j\) largest. Then \(d_j\ge n^{1/4}\), and the other three factors form an ordered factorization of \(d=n/d_j\le n^{3/4}\). Since \(d_j=n/d\) is determined by \(d\), this gives

\[
\begin{gathered}
\tau_4(n)\le4\sum_{d\mid n,\ d\le n^{3/4}}\tau_3(d).
\end{gathered}
\]

Apply this to \(n=1+lh\le Z\) and exchange the sums. If \(d\mid1+lh\), then \(d\) is coprime to \(l\), and \(h\) lies in one residue class modulo \(d\); there are at most \(H'/d+1\) such \(h\le H'\). Therefore the left side of (2.2) is at most \(4\sum_{d\le Z^{3/4}}\tau_3(d)(H'/d+1)\), and Lemma 2.1 finishes the proof. \(\square\)

## 3. Mean values of Dirichlet polynomials

Let \(P(t)=\sum_{n\le Y}c_n n^{it}\) with complex coefficients, and put \(\|c\|^2=\sum_n|c_n|^2\).

**Lemma 3.1 (continuous mean value).** For every real interval \(I\) of length \(T\ge0\),

\[
\begin{gathered}
\int_I|P(t)|^2dt\le(T+6\pi Y)\|c\|^2.\quad(3.1)
\end{gathered}
\]

**Proof.** Since \(|P(t)|=|\sum_n\overline{c_n}n^{-it}|\), this is Theorem 2.1 of [*Mean values of Dirichlet polynomials and zeta*](course:NT-ZETA/NT-ZETA-16) with \(a_n=\overline{c_n}\): the integral equals \(T\|c\|^2\) up to an error of absolute value at most \(6\pi\sum_nn|c_n|^2\le6\pi Y\|c\|^2\). \(\square\)

**Lemma 3.2 (well-spaced points).** Let \(I\) be an interval of length \(T\ge0\) and \(\mathcal T\subset I\) a finite set whose points are at mutual distance at least \(1\). Then

\[
\begin{aligned}
\sum_{t\in\mathcal T}|P(t)|^2
&\le2\bigl(T+1+6\pi Y\bigr)\\
&\quad\times\bigl(1+\log^2Y\bigr)\|c\|^2.\quad(3.2)
\end{aligned}
\]

**Proof.** For \(t\in\mathcal T\) and \(s\in J_t=[t-\frac12,t+\frac12]\), \(P(t)=P(s)+\int_s^tP'(u)\,du\), so \(|P(t)|\le|P(s)|+\int_{J_t}|P'|\). Averaging over \(s\in J_t\) and applying Cauchy's inequality on an interval of length one,

\[
\begin{gathered}
|P(t)|^2\le2\int_{J_t}|P|^2+2\int_{J_t}|P'|^2 .
\end{gathered}
\]

The intervals \(J_t\) overlap at most at endpoints and lie in an interval of length \(T+1\). The derivative \(P'(u)=\sum_n i(\log n)c_nn^{iu}\) is again a Dirichlet polynomial, with coefficient norm at most \((\log Y)\|c\|\). Lemma 3.1, applied to \(P\) and \(P'\), proves (3.2). \(\square\)

The constants in (3.1) and (3.2) are absolute: they do not depend on the coefficients, on their number, or on how they were produced.

## 4. Rough integers

For \(r\ge0\) and a set \(\mathcal Q\) of primes up to \(W\), let

\[
\begin{gathered}
T_r^{\mathcal Q}(m)=\sum_{\substack{d\mid m,\ d\mid P_{\mathcal Q}\\ \omega(d)\le r}}\mu(d),\qquad P_{\mathcal Q}=\prod_{p\in\mathcal Q}p,
\end{gathered}
\]

where \(\omega(d)\) is the number of prime factors of \(d\). If \(m\) has exactly \(s\) prime factors in \(\mathcal Q\), then \(T_r^{\mathcal Q}(m)=\sum_{j\le r}(-1)^j\binom sj\).

**Lemma 4.1 (Bonferroni truncation).** With \(s\) as above, \(T_r^{\mathcal Q}(m)-\mathbf 1_{s=0}=(-1)^r\binom{s-1}r\) for \(s\ge1\). Consequently

\[
\begin{gathered}
\bigl|T_r^{\mathcal Q}(m)-\mathbf 1_{s=0}\bigr|\le\binom s{r+1}\\
=\#\{d\mid m:\ d\mid P_{\mathcal Q},\ \omega(d)=r+1\}.
\end{gathered}
\]

**Proof.** The identity \(\sum_{j\le r}(-1)^j\binom sj=(-1)^r\binom{s-1}r\) follows by induction on \(r\) from Pascal's rule. If \(s\le r\), then \(\binom{s-1}r=0\). If \(s\ge r+1\), then \(\binom{s-1}r=\frac{r+1}s\binom s{r+1}\le\binom s{r+1}\). \(\square\)

**Lemma 4.2 (rough integers twisted by characters).** Fix \(\delta_1>0\), \(A_0>0\) and \(A>0\). For large \(x\), uniformly for \(x^{\delta_1}\le H\le x^{1/\delta_1}\), intervals \(I\subseteq[H,2H]\) and Dirichlet characters \(\chi\) of modulus \(k\le L^{A_0}\),

\[
\begin{gathered}
\sum_{\substack{n\in I\\ n\ \text{rough}}}\chi(n)=\mathbf 1_{\chi\ \text{principal}}V(W)|I|\\
+O(HL^{-A}).\quad(4.1)
\end{gathered}
\]

In particular the number of rough integers in \(I\) is \(V(W)|I|+O(HL^{-A})\).

**Proof.** The primes dividing \(k\) are at most \(L^{A_0}<W\), so a rough \(n\) is coprime to \(k\), and the principal character equals \(1\) on rough integers. Fix a residue \(b\) coprime to \(k\), let \(\mathcal Q\) be the set of primes \(p\le W\) not dividing \(k\), and put \(r=\lceil c\log L\rceil\), with \(c\) to be chosen. An integer \(n\equiv b\ (k)\) is rough exactly when it has no prime factor in \(\mathcal Q\). By Lemma 4.1,

\[
\begin{aligned}
&\Bigl|\#\{n\in I:\ n\equiv b\ (k),\ n\ \text{rough}\}\\
&\quad-\sum_{n\in I,\ n\equiv b}T_r^{\mathcal Q}(n)\Bigr|\\
&\quad\le\sum_{\substack{d\mid P_{\mathcal Q}\\ \omega(d)=r+1}}\Bigl(\frac{|I|}{kd}+1\Bigr).
\end{aligned}
\]

By the Chinese remainder theorem, for \(d\mid P_{\mathcal Q}\) the integers \(n\in I\) with \(n\equiv b\ (k)\) and \(d\mid n\) form one progression modulo \(kd\), so their number is \(|I|/(kd)+O(1)\). Hence

\[
\begin{gathered}
\sum_{n\in I,\ n\equiv b}T_r^{\mathcal Q}(n)=\frac{|I|}k\sum_{\substack{d\mid P_{\mathcal Q}\\ \omega(d)\le r}}\frac{\mu(d)}d\\
+O\Bigl(\sum_{\omega(d)\le r}1\Bigr).
\end{gathered}
\]

The full sum over \(d\mid P_{\mathcal Q}\) of \(\mu(d)/d\) is \(\prod_{p\in\mathcal Q}(1-1/p)=V(W)k/\varphi(k)\). The terms with \(\omega(d)=j\) have absolute sum at most \(S_W^j/j!\), where \(S_W\le\log L\) (Lemma 1.2). The number of squarefree \(d\mid P_{\mathcal Q}\) with \(\omega(d)\le r+1\) is at most \(W^{r+1}=\exp(O(L^{0.24}\log L))\), which is less than \(HL^{-A}/L^{A_0}\). Since \(n!\ge(n/e)^n\),

\[
\begin{gathered}
\sum_{j\ge r+1}\frac{S_W^j}{j!}\le2\Bigl(\frac{e\log L}{r+1}\Bigr)^{r+1}\\
\le2\Bigl(\frac ec\Bigr)^{c\log L},
\end{gathered}
\]

which is at most \(L^{-A-A_0}\) once \(c\) is large in terms of \(A+A_0\). Altogether the count in the class \(b\) is \(V(W)|I|/\varphi(k)+O(HL^{-A-A_0})\). Multiply by \(\chi(b)\) and sum over the \(\varphi(k)\le L^{A_0}\) classes; character orthogonality gives (4.1). \(\square\)

## 5. Phases compared with integrals

**Lemma 5.1 (sum and integral).** Let \(q\ge1\), let \(a\) be an integer, and let \(J\) be a bounded interval. For every function \(\phi\) of bounded variation \(V_J(\phi)\) on \(J\),

\[
\begin{gathered}
\Bigl|\sum_{\substack{n\in J\\ n\equiv a\ (q)}}\phi(n)-\frac1q\int_J\phi(y)\,dy\Bigr|\\
\le3\sup_J|\phi|+V_J(\phi).\quad(5.1)
\end{gathered}
\]

If \(J\subseteq[N,2N]\) and \(t\ne0\) is real, then

\[
\begin{gathered}
\Bigl|\sum_{\substack{n\in J\\ n\equiv a\ (q)}}n^{it}\Bigr|\le\frac{4N}{q|t|}+3+|t|.\quad(5.2)
\end{gathered}
\]

**Proof.** Let \(J\) have endpoints \(\alpha<\beta\). If the progression has no term in \(J\), then \(\beta-\alpha<q\) and the left side of (5.1) is at most \(\sup|\phi|\). Otherwise let \(n_1<\cdots<n_s\) be its terms in \(J\). Then

\[
\begin{aligned}
&\sum_{j=1}^s\phi(n_j)-\frac1q\int_J\phi\\
&\quad=\sum_{j<s}\frac1q\int_{n_j}^{n_{j+1}}\bigl(\phi(n_j)-\phi(y)\bigr)dy\\
&\qquad+\phi(n_s)-\frac1q\int_\alpha^{n_1}\phi-\frac1q\int_{n_s}^\beta\phi .
\end{aligned}
\]

Each integrand in the first sum is at most the variation of \(\phi\) on \([n_j,n_{j+1}]\), and these intervals do not overlap, so the first sum is at most \(V_J(\phi)\). The intervals \([\alpha,n_1]\) and \([n_s,\beta]\) have length at most \(q\), so the last three terms are at most \(3\sup|\phi|\). For (5.2), take \(\phi(y)=y^{it}\): its modulus is \(1\), its variation on \(J\) is at most \(\int_N^{2N}|t|\,dy/y\le|t|\), and \(\int_Jy^{it}dy=[y^{1+it}/(1+it)]\) has modulus at most \(4N/|t|\). \(\square\)

## 6. Exercises

**6.1.** Deduce from Lemma 1.1 that \(\sum_{p\in I}\log p=|I|+O(NL^{-A})\) for every interval \(I\subseteq[N,2N]\), with \(N\) as there.

**6.2.** Show that \(\tau_j(n)\le\tau(n)^{j-1}\) for all \(j\ge1\).

**6.3.** Let \(1\le l\le x^{0.01}\) and \(H'=x/l\). Show that \(\sum_{h\le H'}\tau(1+lh)^2\ll H'L^3\).

**6.4.** Prove directly, by expanding the square, that \(\int_I|P(t)|^2dt\le(T+4Y(1+\log Y))\|c\|^2\) for every interval \(I\) of length \(T\), a slightly weaker form of (3.1).

**6.5.** Prove the identity \(\sum_{j\le r}(-1)^j\binom sj=(-1)^r\binom{s-1}r\) for \(s\ge1\), and show that \(T_r^{\mathcal Q}\ge\mathbf 1_{s=0}\) when \(r\) is even and \(T_r^{\mathcal Q}\le\mathbf 1_{s=0}\) when \(r\) is odd.

## 7. Solutions

**6.1.** Write \(\sum_{p\in I}\log p=\int_I\log y\,d\pi(y)\) and integrate by parts with \(\pi(y)\) replaced by \(\int^y du/\log u+E(y)\), where \(|E|\ll NL^{-A-1}\) by (1.1) with \(q=1\) and \(A+1\) in place of \(A\). The main term is \(|I|\), and the error is \(O(NL^{-A-1}\log(2N))=O(NL^{-A})\).

**6.2.** By induction, \(\tau_{j+1}(n)=\sum_{d\mid n}\tau_j(d)\)\(\le\tau(n)\max_{d\mid n}\tau_j(d)\le\tau(n)\tau_j(n)\), because \(\tau_j\) is monotone along divisibility: a factorization of \(d\) extends to one of \(n\) by multiplying its last factor by \(n/d\).

**6.3.** Take \(Z=1+lH'=1+x\le2x\). Then \(\log Z\le2L\), and \(Z^{3/4}\le2x^{3/4}\le2x^{-0.24}H'\) because \(H'\ge x^{0.99}\). Both terms of (2.2) are therefore \(O(H'L^3)\).

**6.4.** Expanding, \(\int_I|P|^2=\sum_{m,n}c_m\overline{c_n}\int_I(m/n)^{it}dt\). The diagonal gives \(T\|c\|^2\). For \(m\ne n\), \(|\int_I(m/n)^{it}dt|\le2/|\log(m/n)|\), and \(|\log(m/n)|\)\(\ge|m-n|/\max(m,n)\)\(\ge|m-n|/Y\), because \(\log(1+u)\ge u/(1+u)\) for \(u>0\). With \(2|c_mc_n|\le|c_m|^2+|c_n|^2\), the off-diagonal terms are at most \(2Y\sum_m|c_m|^2\sum_{n\ne m}|m-n|^{-1}\)\(\le4Y(1+\log Y)\|c\|^2\).

**6.5.** For \(r=0\) both sides equal \(1\). If the identity holds for \(r-1\), then adding \((-1)^r\binom sr\) and using \(\binom sr-\binom{s-1}{r-1}=\binom{s-1}r\) gives it for \(r\). Since \(\binom{s-1}r\ge0\), the sign of \(T_r^{\mathcal Q}-\mathbf 1_{s=0}\) is \((-1)^r\) or zero.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
