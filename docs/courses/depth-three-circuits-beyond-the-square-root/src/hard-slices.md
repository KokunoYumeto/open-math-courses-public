# Hard slices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The language of [An explicit language](an-explicit-language.md) has, at each length, many *slices*: the functions of the data bits obtained by fixing the parameter bits. This lesson shows that some slice is *hard* in the following sense: after a random restriction that leaves about \(\sqrt d\) of the \(d\) data bits live, its sign has correlation at most \(2^{-|T|/8}\) with *every* CNF of a fixed width \(b\), with high probability over the restriction. The proof chooses the parameter bits at random and combines three facts: the limited independence of a random slice on a small subcube, the sparse partition of [Sunflowers and a disjoint sparse partition](sunflowers-and-a-disjoint-sparse-partition.md), and a moment bound.

Notation: \(d,r,t\), the hash \(h\), the bits \(u\), the polynomial \(P\) and the elements \(\beta_j\) are those of the previous lesson; \(\mathcal C_b(T)\) and \(\operatorname{corr}_b\) are those of [Depth-three circuits and the square-root barrier](depth-three-circuits-and-the-square-root-barrier.md).

## 1. The statement

**Proposition 1.1 (hard slices).** Fix an integer \(b\geq1\) and a real \(B>0\). For every sufficiently large \(n\) there is a setting of the parameter bits such that, with
\[
p=\frac B{\sqrt d},\qquad m_0=pd=B\sqrt d,
\]
the sign \(g:\{0,1\}^d\to\{-1,1\}\) of the resulting slice has the following property. Call a restriction \((T,\rho)\) of the \(d\) data coordinates *exceptional* if \(|T|\notin[\frac{m_0}2,2m_0]\) or \(\operatorname{corr}_b(g_{T,\rho})>2^{-|T|/8}\). Then, for a \(p\)-random restriction,
\[
\Pr_{T,\rho}[\text{exceptional}]\leq4\cdot2^{-m_0/16}.
\]

The setting may depend on \(b\), \(B\) and \(n\). On a restriction that is not exceptional, the bound \(2^{-|T|/8}\) holds for all CNFs of width at most \(b\) on the live variables at once, whatever their number of clauses.

Throughout, \(P\) is a polynomial as in Lemma 1.1 of the previous lesson, so that \(F=R_P\) is a field; the hash bits \(u\) and the elements \(\beta_0,\ldots,\beta_{t-1}\in F\) are uniformly random and independent, and \(d\) is large enough that \(0<p<1\). At the end one good choice of \((u,\beta)\) is fixed.

## 2. Counting sparse tests

Let \(M=M(b,\frac18)\) be the constant of the sparse partition lemma for \(\eta=\frac18\). Call a CNF on \(\{0,1\}^T\), \(|T|=m\geq1\), a *sparse test* if its clauses have width at most \(b\) and it has at most \(Mm\) clauses.

**Lemma 2.1.** The number of sparse tests on \(m\) variables is at most
\[
2^{Mm\,[\,1+b\log_2(2m+1)\,]} .
\]

*Proof.* A clause of width at most \(b\) is a set of at most \(b\) literals. Listing its literals in a fixed order and filling up to length \(b\) with a padding symbol encodes it by a word of length \(b\) over \(2m+1\) symbols; so there are at most \((2m+1)^b\) clauses, the false clause included. A sparse test is encoded by a list of \(Mm\) entries, each a clause or a padding symbol: at most \(((2m+1)^b+1)^{Mm}\leq(2(2m+1)^b)^{Mm}\) lists. \(\square\)

The count is \(2^{O(m\log m)}\), far less than the \(2^{2^m}\) functions on the cube. This is what the sparse partition buys.

## 3. One test: a moment bound

Fix a restriction \((T,\rho)\) with \(m=|T|\geq1\), and hash bits \(u\) for which \(h\) is injective on the restricted cube. By Proposition 5.2 of the previous lesson, over the random \(\beta\) the signs \(g_{T,\rho}(z)\), \(z\in\{0,1\}^T\), are unbiased and \(t\)-wise independent. Recall that \(t\) is even.

**Lemma 3.1.** For every function \(J:\{0,1\}^T\to\{0,1\}\), the sum \(Y=\sum_zg_{T,\rho}(z)J(z)\) satisfies
\[
\begin{gathered}
\mathbb E_\beta\,Y^t\leq t^t\,2^{mt/2},\\
\Pr_\beta\bigl[\,|Y|>2^{3m/4}\bigr]\leq t^t\,2^{-mt/4}.
\end{gathered}
\]

*Proof.* Expand \(Y^t\) as a sum over ordered \(t\)-tuples \((z_1,\ldots,z_t)\) of points of the cube; the term of a tuple is \(\prod_ig(z_i)J(z_i)\). A tuple involves at most \(t\) distinct points, and their signs are independent. If some point occurs exactly once in the tuple, its sign appears to the first power and has mean zero, so the term has expectation zero. In the other tuples every point occurs at least twice, so at most \(t/2\) distinct points occur. Such a tuple is described by a list of \(t/2\) points of the cube (repeating points if fewer occur) and, for each of the \(t\) positions, an entry of the list: at most \(2^{mt/2}(t/2)^t\) descriptions. Each term has absolute value at most \(1\). This gives the first bound. Since \(t\) is even, \(Y^t=|Y|^t\geq0\), and Markov's inequality gives
\[
\Pr\bigl[\,|Y|>2^{3m/4}\bigr]\leq\frac{\mathbb EY^t}{2^{3mt/4}},
\]
which is at most \(t^t\,2^{-mt/4}\). \(\square\)

Note that \(|Y|>2^{3m/4}\) says exactly that \(|\mathbb E_zg_{T,\rho}(z)J(z)|>2^{-m/4}\).

## 4. All narrow tests

**Lemma 4.1.** Let \((T,\rho)\) and \(u\) be as in Section 3, and suppose
\[
\frac{M\,[\,1+b\log_2(2m+1)\,]}t+\frac{\log_2t}m\leq\frac18.
\]
Call this inequality the *growth condition*. Then with probability at least \(1-2^{-mt/8}\) over \(\beta\),
\[
\operatorname{corr}_b(g_{T,\rho})\leq2^{-m/8}.
\]

*Proof.* By Lemma 2.1, Lemma 3.1 and the union bound, the probability that some sparse test \(J\) has \(|\mathbb E_zg_{T,\rho}J|>2^{-m/4}\) is at most
\[
2^{Mm[1+b\log_2(2m+1)]+t\log_2t-mt/4}\leq2^{-mt/8},
\]
the inequality being the growth condition multiplied by \(mt\). Suppose no sparse test fails, and let \(J\in\mathcal C_b(T)\) be arbitrary. By the sparse partition lemma with \(\eta=\frac18\), \(J=\sum_aH_a\) pointwise, with at most \(2^{m/8}\) sparse tests \(H_a\). Hence
\[
\begin{aligned}
\bigl|\mathbb E_zg_{T,\rho}J\bigr|&\leq\sum_a\bigl|\mathbb E_zg_{T,\rho}H_a\bigr|\\
&\leq2^{m/8}\cdot2^{-m/4}=2^{-m/8}.
\end{aligned}
\]
So \(\operatorname{corr}_b(g_{T,\rho})\leq2^{-m/8}\). \(\square\)

The probability estimate concerns only the sparse tests. Once they are all under control, the bound for the other CNFs of width \(b\), of which there may be vastly more, follows deterministically.

**Lemma 4.2.** For fixed \(b\) and \(B\), the growth condition holds for all \(m\in[\frac{m_0}2,2m_0]\), once \(d\) is large enough.

*Proof.* In this range \(m\leq2B\sqrt d\) and \(m\geq\frac12B\sqrt d\), while \(d^{1/6}-2<t\leq d^{1/6}\) by Lemma 2.2 of the previous lesson. So the first term of the growth condition is at most \(M[1+b\log_2(4B\sqrt d+1)]/(d^{1/6}-2)\) and the second at most \(2\log_2(d^{1/6})/(B\sqrt d)\). Both tend to \(0\) as \(d\to\infty\). \(\square\)

Here the growth of \(t\) is used: a bounded amount of independence would not beat the \(2^{O(m\log m)}\) sparse tests (Exercise 7.3).

## 5. The size of the live set

**Lemma 5.1.** Let \(m=|T|\) for a \(p\)-random live set \(T\subseteq[d]\), and \(m_0=pd\). Then
\[
\begin{gathered}
\Pr\bigl[m<\tfrac{m_0}2\bigr]\leq2^{-m_0/16},\\
\Pr[m>2m_0]\leq2^{-m_0/16}.
\end{gathered}
\]

*Proof.* The coordinates are independent, so with \(1+v\leq e^v\),
\[
\begin{gathered}
\mathbb E\,2^{-m}=\bigl(1-\tfrac p2\bigr)^d\leq e^{-m_0/2},\\
\mathbb E\,2^{m}=(1+p)^d\leq e^{m_0}.
\end{gathered}
\]
By Markov's inequality,
\[
\begin{aligned}
\Pr\bigl[m<\tfrac{m_0}2\bigr]&=\Pr\bigl[2^{-m}>2^{-m_0/2}\bigr]\\
&\leq2^{m_0/2}e^{-m_0/2}\\
&=2^{-\frac12(\log_2e-1)m_0},\\
\Pr[m>2m_0]&=\Pr\bigl[2^{m}>2^{2m_0}\bigr]\\
&\leq2^{-2m_0}e^{m_0}\\
&=2^{-(2-\log_2e)m_0}.
\end{aligned}
\]
Since \(\frac1x\) is convex, comparing \(\ln2=\int_1^2\frac{dx}x\) with the tangent at \(x=\frac32\) and with the chord gives \(\frac23<\ln2<\frac34\), so \(\frac43<\log_2e<\frac32\). Hence \(\frac12(\log_2e-1)>\frac16\) and \(2-\log_2e>\frac12\); both exceed \(\frac1{16}\). \(\square\)

## 6. Fixing the parameters

**Proof of Proposition 1.1.** Take \(d\) so large that \(0<p<1\), that Lemma 4.2 applies, and that \(r\geq(2+\frac1{16})m_0\); the last is possible because \(r\geq d^{2/3}\) and \(m_0=B\sqrt d\). Consider \(u\), \(\beta\) and \((T,\rho)\) all random and independent, and the event \(\mathcal E\) that \((T,\rho)\) is exceptional for the slice given by \((u,\beta)\): that \(|T|\notin[\frac{m_0}2,2m_0]\) or \(\operatorname{corr}_b(g_{T,\rho})>2^{-|T|/8}\). By Lemma 5.1 the first alternative has probability at most \(2\cdot2^{-m_0/16}\). Fix a restriction with \(m=|T|\) in the range; then \(m\geq1\). By Lemma 4.2 of the previous lesson, \(h\) fails to be injective on the restricted cube with probability at most
\[
2^{m-r}\leq2^{2m_0-r}\leq2^{-m_0/16}
\]
over \(u\). For each \(u\) with \(h\) injective, Lemma 4.1 bounds the probability over \(\beta\) of \(\operatorname{corr}_b(g_{T,\rho})>2^{-m/8}\) by
\[
2^{-mt/8}\leq2^{-m_0/16},
\]
because \(m\geq\frac{m_0}2\) and \(t\geq1\). So for every restriction in the range, the second alternative has probability at most \(2\cdot2^{-m_0/16}\) over \((u,\beta)\). Altogether
\[
\Pr_{u,\beta,T,\rho}[\mathcal E]\leq4\cdot2^{-m_0/16}.
\]
For each fixed \((u,\beta)\) let \(\phi(u,\beta)\) be the probability of \(\mathcal E\) over \((T,\rho)\). The average of the finitely many numbers \(\phi(u,\beta)\) is the probability just bounded, so some \((u,\beta)\) has \(\phi(u,\beta)\leq4\cdot2^{-m_0/16}\). Fix it, together with \(P\) and arbitrary values of the unused input bits. \(\square\)

The argument does not say *which* setting is good, and the algorithm for the language never needs to know: a good setting is just one particular input prefix. The two probability spaces are used in different ways. The parameter bits are averaged out and then fixed; the restriction stays random and reappears in the last lesson.

## 7. Exercises

**7.1.** For \(b=1\), list the clauses of width at most \(1\) on \(m\) variables and compare their number with the bound \((2m+1)^b\) in the proof of Lemma 2.1.

**7.2.** Let the signs \(g(z)\) be fully independent and unbiased, \(J=1\) and \(N=2^m\). Compute \(\mathbb EY^4\) exactly and compare with the bound of Lemma 3.1 for \(t=4\).

**7.3.** Suppose the signs were only \(t\)-wise independent for a *fixed* even \(t\), not growing with \(d\). Explain why the union bound in Lemma 4.1 would fail for large \(m\).

**7.4.** Where is the *disjointness* of the pieces in the sparse partition used in Lemma 4.1?

**7.5.** Prove \(\mathbb E\,2^{-m}=(1-\frac p2)^d\) and \(\mathbb E\,2^m=(1+p)^d\) for the size \(m\) of a \(p\)-random subset of \([d]\).

**7.6.** Why does the proof need \(t\) to be even?

## 8. Solutions

**7.1.** The false clause, and the \(2m\) single literals: \(2m+1\) clauses, which is exactly \((2m+1)^1\).

**7.2.** In \(\mathbb E(\sum_zg(z))^4\) a \(4\)-tuple contributes \(1\) if every point occurs an even number of times and \(0\) otherwise. There are \(N\) tuples with one point and \(3N(N-1)\) with two points occurring twice each. So \(\mathbb EY^4=3N^2-2N\), against the bound \(4^4N^2=256N^2\). The bound is crude in its constant; only the factor \(2^{mt/2}=N^{t/2}\) matters.

**7.3.** One test fails with probability at most \(t^t2^{-mt/4}\), and there are up to \(2^{Mm[1+b\log_2(2m+1)]}\) sparse tests. The product is small only if \(mt/4\) exceeds \(Mm[1+b\log_2(2m+1)]\), that is, \(t>4M[1+b\log_2(2m+1)]\), which fails for large \(m\) when \(t\) is fixed. With \(t\) about \(d^{1/6}\) and \(m\) about \(\sqrt d\), the condition holds for large \(d\).

**7.4.** In the identity \(J=\sum_aH_a\) between indicators. For pieces with overlapping supports, \(J\) would be the maximum of the \(H_a\), not their sum, and \(\mathbb E_zgJ\) could not be split into the terms \(\mathbb E_zgH_a\) without inclusion and exclusion.

**7.5.** \(m=\sum_i\xi_i\) with independent indicators \(\xi_i\) of probability \(p\). So \(\mathbb E\,2^{-m}=\prod_i\mathbb E\,2^{-\xi_i}=(1-p+\frac p2)^d\) and \(\mathbb E\,2^m=\prod_i\mathbb E\,2^{\xi_i}=(1-p+2p)^d\).

**7.6.** For even \(t\), \(Y^t=|Y|^t\) is nonnegative, so Markov's inequality applies to it and bounds the probability that \(|Y|\) is large. Also a tuple in which every point occurs at least twice then has at most \(t/2\) distinct points, with \(t/2\) an integer.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
