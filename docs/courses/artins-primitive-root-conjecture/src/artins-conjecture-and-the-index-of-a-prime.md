# Artin's conjecture and the index of a prime

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An integer \(a\) is a primitive root modulo a prime \(p\) when its powers run through all nonzero residues modulo \(p\). Artin conjectured in 1927 that every integer other than \(-1\) and the squares is a primitive root modulo infinitely many primes. This course proves that conjecture in the following quantitative form, after OpenAI's 2026 paper [OpenAI-029]: for every such \(a\), every sufficiently large dyadic interval \((x,2x)\) contains at least a constant times \(x/(\log x)^2\) primes with primitive root \(a\). This lesson reduces the theorem to two propositions. The first supplies many primes \(p\) for which \(p-1\) has a very restricted factorization; the second bounds, uniformly in a growing prime \(q\), the number of primes that split completely in the Kummer field \(\mathbb Q(\mu_q,a^{1/q})\). The second rests on a zero-free strip of fixed width for all Hecke \(L\)-functions of finite order over cyclotomic fields containing \(\mu_{12}\), which occupies Lessons 2–14.

**Prerequisites.** [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions), Theorem 6.2, Proposition 6.3 and Corollary 6.5; [*Decomposition of primes in extensions*](course:NT-ANT/decomposition-of-primes-in-extensions), Theorem 5.4; [*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields), Theorems 12.1, 12.3 and 12.5 with the supplements (22).

## 1. The order and the index

Let \(a\) be an integer and \(p\) a prime not dividing \(a\). The **order** \(\operatorname{ord}_p(a)\) is the least \(k\ge1\) with \(a^k\equiv1\pmod p\); it divides \(p-1\). The **index** of \(a\) at \(p\) is
\[
i_p(a)=\frac{p-1}{\operatorname{ord}_p(a)} .
\]
Thus \(a\) is a primitive root modulo \(p\) exactly when \(i_p(a)=1\). Call \(a\) **admissible** if \(a\ne-1\) and \(a\) is not the square of an integer. Both conditions are necessary for primitive roots at infinitely many primes: \(-1\) has order at most \(2\), and for an odd prime \(p\nmid b\) the square \(b^2\) has order dividing \((p-1)/2\).

**Lemma 1.1.** Let \(p\nmid a\) and let \(q\) be a prime. Then \(q\mid i_p(a)\) if and only if
\[
\begin{gathered}
p\equiv1\pmod q\\
\text{and}\\
a^{(p-1)/q}\equiv1\pmod p .
\end{gathered}
\]

*Proof.* If \(q\mid i_p(a)\), then \(q\mid p-1\) and \(\operatorname{ord}_p(a)\) divides \((p-1)/q\), so \(a^{(p-1)/q}\equiv1\). Conversely, if \(q\mid p-1\) and \(a^{(p-1)/q}\equiv1\), then \(\operatorname{ord}_p(a)\mid(p-1)/q\), so \(q\) divides \(i_p(a)\). \(\square\)

## 2. The theorem

**Theorem 2.1** (primitive roots for every admissible base [OpenAI-029, Theorem 1.1]). For every admissible integer \(a\) there are constants \(c_a>0\) and \(x_a\ge2\) such that for every real \(x\ge x_a\),
\[
\begin{aligned}
&\#\Bigl\{p\ \text{prime}:x<p<2x,\ p\nmid a,\\
&\qquad\operatorname{ord}_p(a)=p-1\Bigr\}\ge c_a\frac{x}{(\log x)^2}.
\end{aligned}
\]

The constants depend on \(a\). In particular every admissible integer, for instance \(2\), is a primitive root modulo infinitely many primes. The predicted count is of order \(x/\log x\), larger by a factor \(\log x\) than the bound of the theorem. Earlier unconditional results allowed a finite choice of bases: Gupta and Murty (1984) exhibited a set of thirteen integers containing one with the property, and Heath-Brown (1986) proved that at most two primes fail it. Hooley (1967) proved Artin's asymptotic under the generalized Riemann hypothesis for the Dedekind zeta functions of the fields \(\mathbb Q(\mu_n,a^{1/n})\).

## 3. Kummer fields and complete splitting

For a prime \(q\) put
\[
\begin{gathered}
E_q=\mathbb Q(\mu_q),\\
K_q=\mathbb Q(\mu_q,a^{1/q}).\quad(3.1)
\end{gathered}
\]
The field \(K_q\) is the splitting field of \(T^q-a\) over \(\mathbb Q\), so it is Galois over \(\mathbb Q\) and does not depend on the choice of the root \(a^{1/q}\).

**Lemma 3.1** (splitting test [OpenAI-029, Lemma 2.3]). Let \(a\ne0\) and let \(p,q\) be primes with \(p\nmid aq\). Then \(p\) is unramified in \(K_q\), and \(p\) splits completely in \(K_q\) if and only if
\[
\begin{gathered}
p\equiv1\pmod q\\
\text{and}\\
a^{(p-1)/q}\equiv1\pmod p.\quad(3.2)
\end{gathered}
\]

*Proof.* Let \(\alpha\) be a root of \(T^q-a\) and \(\zeta\) a primitive \(q\)th root of unity; the roots are \(\alpha_i=\alpha\zeta^i\), \(0\le i<q\), and they are algebraic integers. Fix a prime \(\mathfrak P\) of \(K_q\) above \(p\). The discriminant of \(T^q-a\) is \(\pm q^qa^{q-1}\), and it equals \(\pm\prod_{i\ne j}(\alpha_i-\alpha_j)\). Since \(p\nmid qa\), no difference \(\alpha_i-\alpha_j\) with \(i\ne j\) lies in \(\mathfrak P\): the roots have distinct reductions modulo \(\mathfrak P\).

An element \(\tau\) of the inertia group \(I_{\mathfrak P}\) acts trivially on the residue field (Theorem 6.2 of [*Hilbert's ramification theory in Galois extensions*](course:NT-ANT/hilberts-ramification-theory-in-galois-extensions)), so \(\tau(\alpha_i)\equiv\alpha_i\pmod{\mathfrak P}\). Since \(\tau\) permutes the roots and their reductions are distinct, \(\tau(\alpha_i)=\alpha_i\) for every \(i\). The roots generate \(K_q\), so \(\tau=1\). Hence \(I_{\mathfrak P}\) is trivial and \(p\) is unramified.

Let \(\sigma=\operatorname{Frob}_{\mathfrak P}\) (Proposition 6.3 there), so \(\sigma(x)\equiv x^p\pmod{\mathfrak P}\) for integral \(x\). The \(q\)th roots of unity also have distinct reductions modulo \(\mathfrak P\), because \(\prod_{i=1}^{q-1}(1-\zeta^i)=q\) is prime to \(p\). From \(\sigma(\zeta)\equiv\zeta^p\) and \(\sigma(\zeta)\in\mu_q\) we get \(\sigma(\zeta)=\zeta^p\). So \(\sigma\) fixes \(E_q\) exactly when \(p\equiv1\pmod q\).

Suppose \(p\equiv1\pmod q\). The element \(\sigma(\alpha)/\alpha\) is a root of unity of order dividing \(q\), and
\[
\begin{aligned}
\frac{\sigma(\alpha)}\alpha&\equiv\alpha^{p-1}=(\alpha^q)^{(p-1)/q}\\
&=a^{(p-1)/q}\pmod{\mathfrak P},
\end{aligned}
\]
where division is allowed because \(p\nmid a\). Reduction modulo \(\mathfrak P\) is injective on \(\mu_q\), and \(\mathfrak P\cap\mathbb Z=p\mathbb Z\). Therefore \(\sigma(\alpha)=\alpha\) if and only if \(a^{(p-1)/q}\equiv1\pmod p\).

Together, \(\sigma\) fixes the generators \(\zeta,\alpha\) of \(K_q\) exactly when (3.2) holds. By Corollary 6.5 there, an unramified prime splits completely exactly when its Frobenius is trivial. \(\square\)

By Lemma 1.1, a prime \(q\) divides \(i_p(a)\) exactly when \(p\) splits completely in \(K_q\) (for \(p\nmid aq\)). Hooley's approach to Artin's conjecture counts the primes up to \(x\) with these splitting conditions; the obstacle is that \(q\) ranges up to about \(\sqrt x\) while unconditional prime ideal theorems in \(K_q\) are only uniform for very small \(q\). The proof below avoids most of this range: it constructs primes \(p\) for which every prime factor of \(p-1\) other than \(2\) lies either in a short range \((\exp((\log x)^{0.1}),\exp((\log x)^{0.3}))\) or is a single prime larger than \(x^{0.9}\).

## 4. A progression of quadratic nonresidues

The index at the prime \(2\) is controlled by Euler's criterion: if \(\bigl(\tfrac ap\bigr)=-1\), then \(a^{(p-1)/2}\equiv-1\), so \(i_p(a)\) is odd. The next lemma finds an arithmetic progression of such primes with the side conditions needed in Proposition 5.1.

**Lemma 4.1** (a progression of quadratic nonresidues [OpenAI-029, Lemma 2.4]). Let \(a\) be admissible and put
\[
M=8\prod_{\substack{\ell\mid a\\ \ell\ \text{odd prime}}}\ell .
\]
There are \(c\in\{2,4\}\) and an integer \(u\) with
\[
\begin{gathered}
(u,M)=1,\\
c\mid u-1,\\
\Bigl(\frac{u-1}c,\frac Mc\Bigr)=1,\quad(4.1)
\end{gathered}
\]
such that every prime \(p\equiv u\pmod M\) satisfies \(p\nmid a\) and \(\bigl(\tfrac ap\bigr)=-1\).

*Proof.* Write \(a=d_0t^2\) with \(t\ge1\) and \(d_0\) squarefree (possibly negative). Since \(a\) is not a square, \(d_0\ne1\). We choose \(u\) to be a unit modulo \(M\) with
\[
\begin{gathered}
u\not\equiv1\pmod\ell\quad(\ell\mid M\ \text{odd}),\\
u\bmod 8\in\{3,5,7\}.\quad(4.2)
\end{gathered}
\]
Every prime \(p\equiv u\pmod M\) is then odd and different from every odd prime \(\ell\mid a\), so \(p\nmid a\), and \(\bigl(\tfrac ap\bigr)=\bigl(\tfrac{d_0}p\bigr)\) because \(p\nmid t\).

*Case 1: an odd prime \(j\ge5\) divides \(d_0\).* Quadratic reciprocity and the supplements (Theorem 12.5 and (22) of [*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields)) write \(\bigl(\tfrac{d_0}p\bigr)\) as a sign depending only on \(p\bmod 8\) and on \(p\) modulo the odd primes of \(d_0\) other than \(j\), times \(\bigl(\tfrac pj\bigr)\). Fix \(u\bmod 8\) and \(u\) modulo the odd primes of \(M\) other than \(j\) within (4.2). Among the residues modulo \(j\) other than \(0\) and \(1\) there are \((j-3)/2\ge1\) squares and \((j-1)/2\ge2\) nonsquares, so \(u\bmod j\) can be chosen with \(u\not\equiv1\) and \(\bigl(\tfrac{d_0}p\bigr)=-1\).

*Case 2: no prime \(j\ge5\) divides \(d_0\).* Then \(d_0\in\{-1,\pm2,\pm3,\pm6\}\). Take \(u\bmod 8\) from the table, and \(u\equiv2\pmod 3\) whenever \(3\mid M\):

| \(d_0\) | \(-1\) | \(2\) | \(-2\) | \(3\) | \(-3\) | \(6\) | \(-6\) |
|---|---|---|---|---|---|---|---|
| \(u\bmod 8\) | \(3\) | \(3\) | \(7\) | \(5\) | \(5\) | \(3\) | \(7\) |

The supplements give \(\bigl(\tfrac{-1}p\bigr)=-1\) for \(p\equiv3\pmod 4\), \(\bigl(\tfrac2p\bigr)=-1\) for \(p\equiv3,5\pmod 8\), and \(\bigl(\tfrac{-2}p\bigr)=\bigl(\tfrac{-1}p\bigr)\bigl(\tfrac2p\bigr)=-1\) for \(p\equiv7\pmod 8\). For the last four columns the class of \(p\) modulo \(24\) is \(5,5,11,23\). Reciprocity gives \(\bigl(\tfrac3p\bigr)=\bigl(\tfrac p3\bigr)=-1\) and \(\bigl(\tfrac{-3}p\bigr)=\bigl(\tfrac p3\bigr)=-1\) for \(p\equiv5\pmod{24}\). For \(p\equiv11\pmod{24}\), \(\bigl(\tfrac2p\bigr)=-1\) and \(\bigl(\tfrac3p\bigr)=-\bigl(\tfrac p3\bigr)=1\), so \(\bigl(\tfrac6p\bigr)=-1\). For \(p\equiv23\pmod{24}\), \(\bigl(\tfrac{-1}p\bigr)=-1\), \(\bigl(\tfrac2p\bigr)=1\) and \(\bigl(\tfrac3p\bigr)=-\bigl(\tfrac p3\bigr)=1\), so \(\bigl(\tfrac{-6}p\bigr)=-1\). The odd primes of \(M\) not dividing \(d_0\) divide \(t\) only; give \(u\) any residue allowed by (4.2) there. The Chinese remainder theorem combines the choices into a class \(u\bmod M\).

*The divisor \(c\).* If \(u\equiv3\) or \(7\pmod 8\) take \(c=2\); if \(u\equiv5\pmod 8\) take \(c=4\). In both cases \((u-1)/c\) is odd, and for odd \(\ell\mid M\) it is prime to \(\ell\) because \(u\not\equiv1\pmod\ell\). This gives (4.1). \(\square\)

For \(a=2\) one can take \((M,c,u)=(8,4,5)\): primes \(p\equiv5\pmod 8\) have \(\bigl(\tfrac2p\bigr)=-1\).

## 5. Two propositions and the proof of the theorem

Write \(L=\log x\). The following two propositions are proved in the rest of the course.

**Proposition 5.1** (primes with controlled predecessors [OpenAI-029, Proposition 2.1]). Let \(M\) be a fixed positive multiple of \(8\), \(c\in\{2,4\}\), and \(u\) an integer satisfying (4.1). For all sufficiently large \(x\) there are \(\gg_{M,c,u}x/L^2\) primes \(p\in(x,2x)\) with
\[
\begin{gathered}
p\equiv u\pmod M,\\
p-1=crQ,\\
Q>x^{0.9}\ \text{prime},\quad(5.1)
\end{gathered}
\]
where every prime divisor of the integer \(r\) lies in \(\bigl(\exp(L^{0.1}),\exp(L^{0.3})\bigr)\).

Lessons 16–19 prove Proposition 5.1 with a sieve and bilinear estimates.

**Proposition 5.2** (uniform complete splitting [OpenAI-029, Proposition 2.2]). Fix an integer \(a\) with \(|a|>1\) and put \(\delta_0=10^{-6}\). For all sufficiently large \(x\) and all primes \(q\) that are sufficiently large in terms of \(a\) and satisfy \(q\le\exp(L^{0.3})\),
\[
\begin{aligned}
&\#\{p\ \text{prime}:x<p\le2x,\\
&\qquad p\ \text{splits completely in}\ K_q\}\\
&\quad\ll_a\frac{x}{q(q-1)L}+x^{1-\delta_0}.\quad(5.2)
\end{aligned}
\]
The implied constant and the threshold for \(x\) do not depend on \(q\).

Lesson 15 deduces Proposition 5.2 from the following theorem, proved in Lessons 2–14. A **finite-order Hecke character** of a number field \(F\) is a continuous character of the idèle class group \(F^\times\backslash\mathbb A_F^\times\) with finite image.

**Theorem 5.3** (a zero-free strip [OpenAI-029, Theorem 1.2]). Let \(F\) be a cyclotomic field containing \(\mu_{12}\). For every finite-order Hecke character \(\eta\) of \(F\), the \(L\)-function \(L_F(s,\eta)\) has no zero in the half-plane \(\operatorname{Re}s>1-10^{-6}\).

The principal character is included, with its pole at \(s=1\). The width \(10^{-6}\) is the same for all such fields and characters; this uniformity is what makes (5.2) uniform in \(q\).

*Proof of Theorem 2.1.* Fix an admissible \(a\); then \(|a|>1\). Choose \(M,c,u\) by Lemma 4.1 and let \(\mathcal R(x)\) be the set of \(\gg_ax/L^2\) primes given by Proposition 5.1. For \(p\in\mathcal R(x)\) we have \(p\nmid a\) and \(\bigl(\tfrac ap\bigr)=-1\), so Euler's criterion gives \(a^{(p-1)/2}\equiv-1\pmod p\) and \(i_p(a)\) is odd: an even index would make \(\operatorname{ord}_p(a)\) divide \((p-1)/2\).

Suppose \(i_p(a)>1\) and let \(q\) be a prime factor of \(i_p(a)\). Then \(q\) is odd and divides \(p-1=crQ\) with \(c\) a power of \(2\), so \(q=Q\) or \(q\mid r\). By Lemma 1.1, \(a^{(p-1)/q}\equiv1\pmod p\).

*The case \(q=Q\).* Then \(j=(p-1)/Q=cr\) satisfies \(1\le j<2x^{0.1}\), and \(p\) divides \(a^j-1\), hence the positive integer
\[
B_a(x)=\prod_{1\le j\le2x^{0.1}}|a^j-1| .
\]
No factor vanishes because \(|a|>1\), and \(\log B_a(x)\)\(\le\sum_{j\le2x^{0.1}}(j\log|a|+\log2)\)\(\ll_ax^{0.2}\). Each prime \(p>x\) dividing \(B_a(x)\) contributes at least \(L\) to this logarithm, so at most \(O_a(x^{0.2}/L)=o(x/L^2)\) primes of \(\mathcal R(x)\) arise in this case.

*The case \(q\mid r\).* Then \(\exp(L^{0.1})<q<\exp(L^{0.3})\), so \(q\) is large enough for Proposition 5.2 once \(x\) is large, and \(p\nmid aq\). By Lemmas 1.1 and 3.1, \(p\) splits completely in \(K_q\). Summing (5.2) over all such \(q\),
\[
\begin{aligned}
&\#\{p\in\mathcal R(x):\text{this case}\}\\
&\quad\ll_a\frac xL\sum_{m>\exp(L^{0.1})}\frac1{m(m-1)}\\
&\qquad+x^{1-\delta_0}\exp(L^{0.3})\\
&\quad\ll_a\frac xL\exp(-L^{0.1})\\
&\qquad+x\exp(-\delta_0L+L^{0.3}),
\end{aligned}
\]
where the first sum runs over all integers and telescopes. Both terms are \(o(x/L^2)\).

Removing the two exceptional sets leaves \(\gg_ax/L^2\) primes in \((x,2x)\) with \(i_p(a)=1\). \(\square\)

When \(a=b^h\) with \(h>1\) odd, no separate treatment is needed: for large \(x\) every prime factor of \(h\) is smaller than every odd prime factor of \(p-1=crQ\), so \((h,p-1)=1\) and the power map \(y\mapsto y^h\) is a bijection of \(\mathbb F_p^\times\). Exercise 8.1 makes this precise.

## 6. Several prime bases at once

The same two propositions give primes at which several prime bases are primitive roots simultaneously. The bases must be multiplicatively independent modulo squares for such a statement: Exercise 8.3 shows that \(2\), \(3\) and \(6\) are never primitive roots modulo the same prime \(p>3\).

**Theorem 6.1** (simultaneous primitive roots [OpenAI-029S, Theorem 1.1]). Let \(q_1,\dots,q_k\) be distinct positive primes. There are \(c>0\) and \(x_0\) such that for \(x\ge x_0\) at least \(cx/(\log x)^2\) primes \(p\in(x,2x)\) satisfy \(p\nmid q_1\cdots q_k\) and \(\operatorname{ord}_p(q_i)=p-1\) for every \(i\).

*Proof.* Let \(M=8\prod_{q_i\ \text{odd}}q_i\). Choose \(u\) with \(u\equiv5\pmod 8\) and, for each odd \(q_i\), \(u\) congruent modulo \(q_i\) to a quadratic nonresidue. Then \((u,M)=1\), \(4\mid u-1\), \((u-1)/4\) is odd, and \(u\not\equiv1\pmod{q_i}\); so \((M,4,u)\) satisfies (4.1). Proposition 5.1 gives \(\gg x/L^2\) primes \(p\equiv u\pmod M\) with \(p-1=4rQ\). For such \(p\), \(p\equiv5\pmod 8\), so \(\bigl(\tfrac2p\bigr)=-1\) and, for odd \(q_i\), reciprocity with \(p\equiv1\pmod 4\) gives \(\bigl(\tfrac{q_i}p\bigr)=\bigl(\tfrac p{q_i}\bigr)=\bigl(\tfrac u{q_i}\bigr)=-1\). For each fixed base \(q_i\) the proof of Theorem 2.1 applies verbatim with \(a=q_i\) and removes \(o(x/L^2)\) primes. There are finitely many bases, so \(\gg x/L^2\) primes remain at which every \(q_i\) has index \(1\). \(\square\)

OpenAI's second paper [OpenAI-029S] states Theorem 6.1 conditionally on four inputs; Theorem 5.3, Proposition 5.1 and the sieve lemmas of Lesson 16 are those inputs, and this course proves them.

## 7. A map of the proof

- **Lessons 2–4** set up the arithmetic of a cyclotomic field \(F\supseteq\mu_{12}\): \(S\)-integers, sextic residue symbols with a reciprocity law free of supplementary factors, Kummer characters, and the Hecke characters that describe the phases of cubic and sextic Gauss sums.
- **Lesson 5** defines a family of coefficient sums \(B_m(Z)\) built from cubic Gauss sums and states the two estimates of the same average that prove Theorem 5.3: an upper bound from a reflected second moment, and an asymptotic from Poisson summation whose main term involves \(1/L^S(s,\eta)\).
- **Lessons 6–10** prove the second moment: the cubic theta representation of Kazhdan and Patterson supplies the coefficients, a Weyl reflection turns the twisted sums into quadratic symbols, and a quadratic large sieve bounds them.
- **Lessons 11–14** carry out the Poisson summation, the Euler product of the main term, the zero detection for the other frequencies, and the Mellin continuation that gives Theorem 5.3.
- **Lesson 15** proves Proposition 5.2 from Theorem 5.3 with an explicit formula whose error depends on the field only through its degree and discriminant.
- **Lessons 16–19** prove Proposition 5.1: weights on the integers \(crQ+1\), a block sieve, Bombieri–Vinogradov, marked bilinear estimates and Buchstab's densities remove the composite values.

## 8. Exercises

**8.1.** Let \(a=b^h\) with \(b\) an integer and \(h>1\) odd, and let \(p\) be a prime with \(p-1=crQ\) as in (5.1), \(p\nmid a\), and \(x\) large. Show that \((h,p-1)=1\), and deduce that \(a\) is a primitive root modulo \(p\) if and only if \(b\) is.

**8.2.** Check the table of Lemma 4.1 in the column \(d_0=-3\) directly: if \(p\equiv5\pmod{24}\), then \(\bigl(\tfrac{-3}p\bigr)=-1\).

**8.3.** Let \(p>3\) be prime. Show that \(2\), \(3\) and \(6\) are not all primitive roots modulo \(p\).

**8.4.** For \(a=2\) and \((M,c,u)=(8,4,5)\), verify (4.1), and show that \(p-1=4rQ\) forces \(r\) odd for every prime \(p\equiv5\pmod 8\).

**8.5.** Let \(|a|>1\). Show that the number of primes \(p\in(x,2x)\) dividing \(B_a(x)\) is at most \(\log B_a(x)/\log x\), and that this is \(O_a(x^{0.2}/\log x)\).

## 9. Solutions

**8.1.** For large \(x\), every prime factor of \(h\) is smaller than \(\exp(L^{0.1})\), so it divides none of \(r\) and \(Q\); it is odd, so it does not divide \(c\). Hence \((h,p-1)=1\). Then \(y\mapsto y^h\) is an automorphism of the cyclic group \(\mathbb F_p^\times\), and it maps generators to generators; so \(b^h\) generates exactly when \(b\) does.

**8.2.** For \(p\equiv5\pmod{24}\) we have \(p\equiv1\pmod 4\) and \(p\equiv2\pmod 3\). Then \(\bigl(\tfrac{-1}p\bigr)=1\) and \(\bigl(\tfrac3p\bigr)=\bigl(\tfrac p3\bigr)=\bigl(\tfrac23\bigr)=-1\), so \(\bigl(\tfrac{-3}p\bigr)=-1\).

**8.3.** A primitive root modulo an odd prime is a quadratic nonresidue. If \(2\) and \(3\) are nonresidues, then \(\bigl(\tfrac6p\bigr)=\bigl(\tfrac2p\bigr)\bigl(\tfrac3p\bigr)=1\), so \(6\) is a residue and not a primitive root.

**8.4.** \((5,8)=1\), \(4\mid 5-1\), and \((u-1)/c=1\) is prime to \(M/c=2\). If \(p\equiv5\pmod 8\), then \(p-1\equiv4\pmod 8\), so \((p-1)/4=rQ\) is odd and \(r\) is odd.

**8.5.** Distinct primes \(p_1,\dots,p_n>x\) dividing the positive integer \(B_a(x)\) satisfy \(x^n<p_1\cdots p_n\le B_a(x)\), so \(n<\log B_a(x)/\log x\). The bound \(\log B_a(x)\)\(\le\sum_{j\le2x^{0.1}}(j\log|a|+\log 2)\)\(\le(2x^{0.1})^2\log|a|+2x^{0.1}\log2\) gives the second claim.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [OpenAI-029S] OpenAI, *Simultaneous primitive roots: a conditional lower bound for prime bases*, OpenAI Math Release preprint, 4 October 2026. https://github.com/openai/math/tree/main/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026
