# Large prime factors of p − 1 and the endpoint of the method

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Theorem 6.1 of [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md) gives \(\gg x/L^2\) primes \(p\in(x,2x)\) with \(p-1=crQ\), where \(Q>x^{0.9}\) is prime and every prime factor of \(r\) lies in \((e^{L^{0.1}},e^{L^{0.3}})\). This lesson shows two things:
- the exponent \(0.9\) can be replaced by any fixed \(\theta<1\), with the same counting function;
- the exponent \(1\) cannot be reached.

The tool is a harmonic tail estimate. Integers composed of primes below \(e^T\) have a convergent moment \(\sum r^{-(1-1/T)}\), so few primes have a large cofactor \(r\). Deleting those primes after the count leaves \(r\le x^\varepsilon\), and therefore \(Q>x^{1-\varepsilon-o(1)}\). No sieve, distribution or Type II estimate is repeated. The endpoint is the inequality \(Q=(p-1)/(cr)<x\).

**Prerequisites.** [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), (4.1) and Proposition 5.1; [*Primes with controlled predecessors*](primes-with-controlled-predecessors.md), Lemma 3.1, Proposition 5.1, Theorem 6.1 and its proof; [*Weights, mass and distribution in a progression*](weights-mass-and-distribution-in-a-progression.md), Section 1, Lemmas 1.1 and 2.1; [*Marked Type II estimates and rough factors*](marked-type-ii-estimates.md), Section 1; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1.

Throughout, \(L=\log x\), \(P^+(n)\) is the largest prime factor of an integer \(n\ge2\), and \(q\) runs over primes. A triple \((M,c,u)\) is **admissible** if \(M\) is a positive multiple of \(8\), \(c\in\{2,4\}\) and \(u\) satisfies (4.1) of Lesson 1.

## 1. A harmonic tail

For a finite set \(\mathcal Q\) of primes let \(\mathcal T(\mathcal Q)\) be the set of positive integers all of whose prime factors lie in \(\mathcal Q\); it contains \(1\).

**Lemma 1.1** (harmonic tail). Let \(T\ge2\) and let \(\mathcal Q\) be a finite set of primes with \(e^2<q\le e^T\) for \(q\in\mathcal Q\). For every real \(R\ge1\),
\[
\begin{aligned}
&\sum_{\substack{r\in\mathcal T(\mathcal Q)\\ r>R}}\frac1r\\
&\quad\le R^{-1/T}\exp\Bigl(2e\sum_{q\in\mathcal Q}\frac1q\Bigr).\quad(1.1)
\end{aligned}
\]

*Proof.* Put \(s=1/T\). For \(r>R\), \(1/r=r^{-s}r^{-(1-s)}\le R^{-s}r^{-(1-s)}\). For \(q\in\mathcal Q\) we have \(q^s\le e\), so \(y_q=q^{-(1-s)}=q^s/q\le e/q<1/e<\frac12\). Hence \(\sum_{j\ge1}y_q^j=y_q/(1-y_q)\le2y_q\le2e/q\). By unique factorization, expanding a finite product of convergent series of nonnegative terms,
\[
\begin{aligned}
\sum_{r\in\mathcal T(\mathcal Q)}r^{-(1-s)}&=\prod_{q\in\mathcal Q}\Bigl(1+\sum_{j\ge1}y_q^j\Bigr)\\
&\le\prod_{q\in\mathcal Q}\Bigl(1+\frac{2e}q\Bigr),
\end{aligned}
\]
and \(1+t\le e^t\) gives (1.1). \(\square\)

**Lemma 1.2** (primes with a large cofactor). Let \(c\in\{2,4\}\), let \(T,\mathcal Q\) be as in Lemma 1.1, and let \(x\ge2\), \(R\ge1\) and \(Y\ge1\). Count the primes \(p\in(x,2x)\) with \(p-1=crn\), where \(r\in\mathcal T(\mathcal Q)\), \(R<r\le Y\) and \(n\ge1\) is an integer. Their number is at most
\[
\frac x2\,R^{-1/T}\exp\Bigl(2e\sum_{q\in\mathcal Q}\frac1q\Bigr)+Y .\quad(1.2)
\]

*Proof.* For fixed \(r\), at most \(x/(cr)+1\le x/(2r)+1\) integers of \((x,2x)\) are \(\equiv1\pmod{cr}\). Sum over the at most \(Y\) values of \(r\) and apply (1.1). \(\square\)

Put
\[
\begin{gathered}
\mathcal Q_x=\{q:e^{L^{0.1}}<q<e^{L^{0.3}}\},\\
S_x=\sum_{q\in\mathcal Q_x}\frac1q .
\end{gathered}
\]
Mertens' estimate \(\sum_{q\le y}1/q=\log\log y+B+O(1/\log y)\) (Theorem 3.1 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)) gives \(S_x=0.2\log L+o(1)\). So for large \(x\)
\[
\exp(2eS_x)\le e^{2e}L^{0.4e}.\quad(1.3)
\]

## 2. Every exponent below 1

For an admissible \((M,c,u)\), let \(\mathcal S(x)\) be the set of all primes \(p\in(x,2x)\) satisfying (6.1) of Lesson 19. By Theorem 6.1 there, there are \(c_S>0\) and \(x_S\) with \(\#\mathcal S(x)\ge c_Sx/L^2\) for \(x\ge x_S\).

**Theorem 2.1** (structured primes with \(Q>x^\theta\)). Let \((M,c,u)\) be admissible and let \(\theta<1\) be fixed. For all sufficiently large \(x\), at least \((c_S/2)\,x/L^2\) primes \(p\in(x,2x)\) satisfy
\[
\begin{gathered}
p\equiv u\pmod M,\\
p-1=crQ,\quad Q>x^\theta\ \text{prime},\quad(2.1)
\end{gathered}
\]
where every prime divisor of \(r\) lies in \((e^{L^{0.1}},e^{L^{0.3}})\). Each of these primes has \(Q=P^+(p-1)\). Moreover, at least \((c_S/2)x/L^2\) primes of the form (2.1) satisfy \(P^+(p-1)>p^\theta\).

*Proof.* Put \(\varepsilon=\min\bigl(0.1,(1-\theta)/2\bigr)\). Then \(\varepsilon>0\) and \(1-\varepsilon-\theta\ge(1-\theta)/2>0\).

*The cofactor bound.* Each \(p\in\mathcal S(x)\) has \(p-1=crQ\) with \(r\in\mathcal T(\mathcal Q_x)\) and \(Q>x^{0.9}\) prime. Hence \(r<2x/(2x^{0.9})=x^{0.1}\).

*The deletion.* For large \(x\), \(e^{L^{0.1}}>e^2\). Apply Lemma 1.2 with \(T=L^{0.3}\), \(R=x^\varepsilon\), \(Y=x^{0.1}\), and use (1.3). The primes \(p\in\mathcal S(x)\) with \(r>x^\varepsilon\) number at most
\[
\begin{aligned}
&\frac x2\,e^{2e}L^{0.4e}e^{-\varepsilon L^{0.7}}+x^{0.1}\\
&\quad=o\Bigl(\frac x{L^2}\Bigr),
\end{aligned}
\]
since \(\varepsilon L^{0.7}-(0.4e+2)\log L\to\infty\).

*The surviving primes.* For large \(x\), at least \((c_S/2)x/L^2\) primes of \(\mathcal S(x)\) have \(r\le x^\varepsilon\). For them
\[
\begin{aligned}
Q&=\frac{p-1}{cr}>\frac{x/2}{4x^{\varepsilon}}\\
&=x^\theta\cdot\frac{x^{1-\varepsilon-\theta}}8>x^\theta
\end{aligned}
\]
for large \(x\). The prime factors of \(c\) and \(r\) are below \(e^{L^{0.3}}<x^{0.9}<Q\), so \(Q=P^+(p-1)\).

*The form \(P^+(p-1)>p^\theta\).* Let \(\theta\ge0\) and apply the first part with \(\vartheta=(1+\theta)/2<1\) in place of \(\theta\). For large \(x\) we have \(x^{\vartheta-\theta}>2\ge2^\theta\), so \(Q>x^\vartheta>(2x)^\theta>p^\theta\). For \(\theta<0\), \(P^+(p-1)\ge2>1>p^\theta\) for every prime of the first part. \(\square\)

**Corollary 2.2** (a moving threshold). Let \((M,c,u)\) be admissible and let \(0.3<\beta<1\) be fixed. For all sufficiently large \(x\), at least \((c_S/2)x/L^2\) primes satisfy (2.1) with \(Q>x\exp(-L^\beta)\) in place of \(Q>x^\theta\), and with \(r\le\exp(L^{(0.3+\beta)/2})\).

*Proof.* Put \(\alpha=(0.3+\beta)/2\), so \(0.3<\alpha<\beta\). Repeat the proof of Theorem 2.1 with \(R=e^{L^\alpha}\). Then \(R^{-1/T}=\exp(-L^{\alpha-0.3})\), and \(L^{\alpha-0.3}-(0.4e+2)\log L\to\infty\), so the deleted primes number \(o(x/L^2)\). The remaining primes satisfy \(Q>(x/2)/(4e^{L^\alpha})>xe^{-L^\beta}\) for large \(x\), since \(L^\beta-L^\alpha-\log8\to\infty\). \(\square\)

In particular \(\log Q/\log x>1-L^{\beta-1}\to1\) on a set of \(\gg x/L^2\) primes.

## 3. Moving thresholds down to the scale \(L^{0.1}\)

**Proposition 3.1.** Let \((M,c,u)\) be admissible and let \(0.1<\beta<1\) be fixed. For all sufficiently large \(x\) there are \(\gg_{M,c,u,\beta}x/L^2\) primes satisfying (2.1) with \(Q>x\exp(-L^\beta)\) in place of \(Q>x^\theta\).

*Proof.* *The new exponents.* Put
- \(b_*=\min(\beta,0.2)\),
- \(\alpha_0=(0.1+b_*)/2\),
- \(\alpha=(\alpha_0+\beta)/2\).

Then \(0.1<\alpha_0<b_*\le\beta\) and \(\alpha_0<\alpha<\beta\). Run the proof of Theorem 6.1 of Lesson 19 with steps 1–4 unchanged, and replace step 5 by
\[
\begin{aligned}
a_i&=0.1+\frac{(b_*-0.1)\,i}{2(K+1)}\\
&\qquad(1\le i\le K).
\end{aligned}
\]
These satisfy \(0.1<a_1<\cdots<a_K<\alpha_0\le0.15\).

*Why the proof still applies.* Lessons 18 and 19 are written for arbitrary fixed \(0.1<a_1<\cdots<a_K<0.2\) (Section 1 of Lesson 18). The thresholds for \(K\) in step 4 are independent of the \(a_i\):
- Lemma 2.1 of Lesson 18 provides \(K_0\) independent of the \(a_i\);
- Lemma 3.1 of Lesson 19 has a bound depending on \(b,\gamma,\kappa\) only;
- Proposition 5.1 of Lesson 19 has a bound depending on \(b\) only.

The final count of that proof is at least \(\mathfrak S_MX_0/(4B_KL)\), where \(X_0\gg xJ_0/L\ge x/L\). So it gives \(\gg x/L^2\) primes \(p\in(x,2x)\) with \(p\equiv u\pmod M\), \(p-1=crQ\) and \(Q>x^{0.9}\) prime. By Lemma 1.1 of Lesson 18, \(r\) is a group integer. Group primes lie in \([e^{L^{a_1}},e^{2L^{a_K}}]\subset(e^{L^{0.1}},e^{L^{0.3}})\) for large \(x\).

*The deletion.* Let \(\mathcal Q\) be the set of group primes. For large \(x\), \(\sum_{q\in\mathcal Q}1/q=\sum_iV_i\le K\), since \(V_i\to\log2\) (Section 1 of Lesson 17). Apply Lemma 1.2 with \(T=2L^{a_K}\), \(R=e^{L^\alpha}\) and \(Y=x^{0.1}\). The primes with \(r>R\) number at most
\[
\begin{aligned}
&\frac x2\,e^{2eK}\exp\Bigl(-\tfrac12L^{\alpha-a_K}\Bigr)+x^{0.1}\\
&\quad=o\Bigl(\frac x{L^2}\Bigr),
\end{aligned}
\]
because \(a_K<\alpha\). The remaining primes have \(Q>(x/2)/(4e^{L^\alpha})>xe^{-L^\beta}\) for large \(x\). \(\square\)

## 4. The endpoint

**Proposition 4.1** (the obstruction). Let \(x>1\) and \(p<2x\), and let \(p-1=crQ\) with integers \(c\ge2\), \(r\ge1\) and \(Q\ge1\). Then \(Q<x\). Consequently no prime \(p\in(x,2x)\) satisfies (2.1) with \(\theta\ge1\).

*Proof.* \(Q=(p-1)/(cr)<2x/(cr)\le x\le x^\theta\) for \(\theta\ge1\). \(\square\)

Let \(\mathcal E\) be the set of fixed real \(\theta\) such that, for all large \(x\), \(\gg x/L^2\) primes in \((x,2x)\) satisfy (2.1). By Theorem 2.1 and Proposition 4.1, \(\mathcal E=(-\infty,1)\): the supremum is \(1\) and it is not attained. The conditions (2.1) together with \(crQ=p-1<2x\) force \(cr<2x^{1-\theta}\). At \(\theta\ge1\) this contradicts \(cr\ge2\).

The exponent \(0.9\) of Theorem 6.1 of Lesson 19 is the cutoff in the weight (1.2) of Lesson 18. It gives the support bound \(r\le x^{0.11}\), and it guarantees that no odd prime \(j\le x^{0.002}\) equals \(Q\) in Lemma 4.1 of Lesson 19. Theorem 2.1 keeps that cutoff and uses Theorem 6.1 only as a count; the gain comes from Lemma 1.1, applied after the count. Inserting \(r\le x^\varepsilon\) into the weight itself would break the group invariance of \(F\) that Lemma 2.1 of Lesson 18 requires. This is why the condition is imposed by deletion.

**Remark 4.2** (unstructured counts). OpenAI's preprint [PD, Theorem 1.1] states that the normalized logarithms of the prime factors of \(p-1\) follow the Poisson–Dirichlet law. For fixed \(\theta\in(0,1)\) it gives
\[
\begin{aligned}
&\#\{x<p\le2x:P^+(p-1)>p^\theta\}\\
&\quad\sim(1-\rho(1/\theta))\,\frac x{\log x},
\end{aligned}
\]
with \(\rho\) the Dickman function. Since \(\rho(u)=1-\log u\) on \([1,2]\), the proportion at \(\theta=0.9\) is \(-\log0.9=0.10536\ldots\). This count is larger than that of Theorem 2.1, but it carries none of the structure (2.1). This lesson does not use it.

## 5. Exercises

**5.1.** Show that \(\sum_{e^{L^{0.1}}<q<e^{L^{0.3}}}1/q=0.2\log L+o(1)\).

**5.2.** For \(\theta=0.99\), find \(\varepsilon\) in the proof of Theorem 2.1 and the exponent of \(x\) in the lower bound for \(Q/x^\theta\).

**5.3.** Show that for large \(x\) a prime \(p\in(x,2x)\) has at most one decomposition \(p-1=crQ\) with \(c\in\{2,4\}\) fixed, \(Q>x^{0.9}\) prime, and all prime factors of \(r\) below \(e^{L^{0.3}}\).

**5.4.** Apply Lemma 1.1 with \(T=L\), \(\mathcal Q\) the primes in \((e^2,x]\) and \(R=x^\varepsilon\), \(\varepsilon<1\). Show that it gives no saving, and explain why the upper end \(e^{L^{0.3}}\) of the range matters.

## 6. Solutions

**5.1.** By Mertens' estimate the sum is \(0.3\log L-0.1\log L+O(L^{-0.1})\). A possible prime at an endpoint changes it by \(o(1)\).

**5.2.** \(\varepsilon=\min(0.1,0.005)=0.005\), and \(Q/x^\theta>x^{1-\varepsilon-\theta}/8=x^{0.005}/8\).

**5.3.** Every prime factor of \(cr\) is below \(e^{L^{0.3}}<x^{0.9}\), so \(Q=P^+(p-1)\). Then \(r=(p-1)/(cQ)\) is determined.

**5.4.** Here \(R^{-1/T}=e^{-\varepsilon}\), while \(\exp(2e\sum_{e^2<q\le x}1/q)\) grows like \(L^{2e}\). So the bound (1.2) exceeds \(x/L^2\). With \(T=L^{0.3}\), the factor \(R^{-1/T}=e^{-\varepsilon L^{0.7}}\) beats every power of \(L\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Proposition 2.1 and Section 12. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
- The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
