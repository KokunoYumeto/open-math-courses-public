# The marked Type II estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Statistical questions about the factorization of \(p-1\), for primes \(p\), lead to sums over factorizations \(p-1=de\) and hence to primes in arithmetic progressions to moduli \(d\) comparable with \(p\). Distribution theorems for primes in progressions stop far below that range. A standard substitute is a bilinear estimate: one bounds sums \(\sum_{m,n}\alpha_m\beta_n\,f(mn)\) in which \(\alpha\) is built from the primes and \(\beta\) is arbitrary. This course proves a bilinear estimate of this kind for the predecessors \(mn-1\) of products, weighted by small prime divisors of \(mn-1\) taken from fixed bands of primes. The estimate and its proof are due to OpenAI [PD, Theorem 3.1]; it is one of the two analytic inputs of their proof that the normalized logarithms of the prime factors of \(p-1\) follow the Poisson–Dirichlet law with parameter one.

The estimate compares the primes with the integers that have no small prime factors, weighted by their density. In an application one first counts integers \(d=mn\) whose predecessor has a prescribed shape, with \(m\) only required to be free of small primes; such counts can be done by sieve methods. The estimate then shows that requiring \(m\) to be prime changes the count by the expected density factor, up to an error smaller than every power of \(\log x\).

**Prerequisites.** [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1. The later lessons list their own prerequisites.

## 1. Marks and marked weights

Throughout the course \(x\) is a large real number, and

\[
\begin{gathered}
L=\log x,\qquad W=\exp(L^{0.24}),\\
V(W)=\prod_{p\le W}\Bigl(1-\frac1p\Bigr).\quad(1.1)
\end{gathered}
\]

The letter \(p\) always denotes a prime. A positive integer is **rough** if all its prime factors exceed \(W\); in particular \(1\) is rough. For \(n>1\), \(P^-(n)\) is the least prime factor of \(n\), and \(P^-(1)=\infty\), so \(n\) is rough exactly when \(P^-(n)>W\). We write \(e(\theta)=\exp(2\pi i\theta)\) and \(\|\theta\|\) for the distance from \(\theta\in\mathbb R\) to the nearest integer. Dirichlet characters, the principal ones included, are extended by zero on integers that are not coprime to the modulus.

Fix an integer \(K\ge1\) and real numbers \(0.1<a_1<a_2<\cdots<a_K<0.2\). For \(1\le i\le K\) the \(i\)th **group** is the band of primes

\[
\begin{gathered}
\mathcal P_i=\{p:\ L^{a_i}\le\log p\le2L^{a_i}\}.\quad(1.2)
\end{gathered}
\]

A prime in some \(\mathcal P_i\) is a **group prime**. For an integer \(h\ge1\), a group prime dividing \(h\) is a **mark** of \(h\). Put

\[
\begin{gathered}
V_i=\sum_{p\in\mathcal P_i}\frac1p,\\
\mu_i(p)=\frac1{pV_i}\quad(p\in\mathcal P_i),\\
\omega_i(h)=\#\{p\in\mathcal P_i:\ p\mid h\},\\
\omega(h)=\sum_{i=1}^K\omega_i(h).
\end{gathered}
\]

Thus \(\mu_i\) is a probability measure on \(\mathcal P_i\), the harmonic measure of the band. Fix also \(0<q<1\). The **marked weight** is

\[
\begin{gathered}
\mathcal W(h)=q^{\,\omega(h)-K}\prod_{i=1}^K\frac{\omega_i(h)}{V_i}.\quad(1.3)
\end{gathered}
\]

It rewards integers with at least one mark in every group and damps integers with many marks. A **marking product** is an integer \(b=p_1p_2\cdots p_K\) with \(p_i\in\mathcal P_i\) for every \(i\).

**Lemma 1.1.** For \(x\) larger than a constant depending on \(K\) and the \(a_i\):

1. the groups are pairwise disjoint, and every group prime satisfies \(\exp(L^{0.1})\le p\le\exp(2L^{0.2})<W\); in particular a rough integer has no marks;
2. \(V_i=\log2+O(L^{-a_i})\) for each \(i\);
3. a marking product determines its prime factors \(p_1,\dots,p_K\), and for every \(h\ge1\),
\[
\begin{gathered}
\prod_{i=1}^K\omega_i(h)\\
=\#\{b\ \text{marking product}:\ b\mid h\};
\end{gathered}
\]
4. \(0\le\mathcal W(h)\le C_{K,q}\) for a constant \(C_{K,q}\) depending only on \(K\) and \(q\), and \(\mathcal W(h)=0\) unless \(h\) has a mark in every group.

**Proof.** 1. Since \(a_i<a_{i+1}\), we have \(2L^{a_i}<L^{a_{i+1}}\) once \(L^{a_{i+1}-a_i}>2\), so the bands are disjoint. The bounds for group primes follow from \(0.1<a_i<0.2\), and \(2L^{0.2}<L^{0.24}\) for large \(L\). A rough integer has no prime factor up to \(W\), so it has no mark.

2. By Mertens' estimate (Theorem 3.1 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)), \(\sum_{p\le y}1/p\)\(=\log\log y+M+O(1/\log y)\) for \(y\ge2\). Taking the difference at \(y=\exp(2L^{a_i})\) and just below \(y=\exp(L^{a_i})\) gives \(V_i=\log(2L^{a_i})-\log(L^{a_i})\)\(+O(L^{-a_i})\). The prime \(p=\exp(L^{a_i})\) can occur only if that number is an integer, and its reciprocal is \(O(\exp(-L^{a_i}))\).

3. The \(p_i\) lie in disjoint bands, so they are distinct primes and \(b\) determines each \(p_i\) as its unique prime factor in \(\mathcal P_i\). The product \(\prod_i\omega_i(h)\) counts the tuples \((p_1,\dots,p_K)\in\mathcal P_1\times\cdots\times\mathcal P_K\) with every \(p_i\mid h\); since the \(p_i\) are distinct primes, this is the same as \(p_1\cdots p_K\mid h\).

4. Write \(\mathcal W(h)=q^{-K}\prod_i\bigl(\omega_i(h)q^{\omega_i(h)}\bigr)/V_i\). The function \(j\mapsto jq^j\) on nonnegative integers is bounded by a constant \(c_q\), and \(V_i\ge\frac12\) by part 2. So \(\mathcal W(h)\le(2c_q/q)^K\). If some \(\omega_i(h)=0\), the product vanishes. \(\square\)

A function \(F\) on the positive integers is **group-invariant** if \(F(ph)=F(h)\) for every group prime \(p\) and every \(h\ge1\). Equivalently, \(F(h)\) depends only on the part of \(h\) coprime to all group primes (Exercise 5.3).

## 2. The theorems

Fix \(\delta>0\) and \(c_*\ge1\). The two lengths \(H_m,H_n\) satisfy

\[
\begin{gathered}
H_m,\ H_n\ge x^\delta,\qquad X=H_mH_n,\\
x/c_*\le X\le c_*x.\quad(2.1)
\end{gathered}
\]

Consider complex coefficients \(\alpha_m\) and \(\beta_n\) and the marked bilinear form

\[
\begin{gathered}
\mathfrak B=\sum_{m,n}\alpha_m\beta_n\\
\times F(mn-1)\,\mathcal W(mn-1).\quad(2.2)
\end{gathered}
\]

**Definition 2.1.** A sequence \(\alpha\) supported on \([H_m,2H_m]\) has **twisted cancellation** if for every choice of fixed \(A_0,B,A>0\) there is a constant \(C_{\rm tc}=C_{\rm tc}(A_0,B,A)\) such that

\[
\begin{gathered}
\Bigl|\frac1{H_m}\sum_m\alpha_m\chi(m)m^{it}\Bigr|\\
\le C_{\rm tc}L^{-A}\quad(2.3)
\end{gathered}
\]

for every Dirichlet character \(\chi\) of modulus at most \(L^{A_0}\) and every real \(t\) with \(|t|\le2XL^B\).

**Theorem 2.2 (marked Type II estimate).** Fix \(\delta>0\), \(c_*\ge1\), \(C>0\), \(D_*>0\) and \(0<q<1\), and let (2.1) hold. Let \(\alpha\) be supported on rough integers in \([H_m,2H_m]\), with \(|\alpha_m|\le L^C\) and twisted cancellation. Let \(\beta\) be supported on rough integers in \([H_n,2H_n]\), with \(|\beta_n|\le L^C\). Let \(F\) be group-invariant with \(|F|\le1\). There is \(K_0\), depending only on \(C\) and \(D_*\), such that for \(K\ge K_0\) and every choice of band exponents \(a_1<\cdots<a_K\) in \((0.1,0.2)\),

\[
\begin{gathered}
|\mathfrak B|\le C'XL^{-D_*},\quad(2.4)
\end{gathered}
\]

where \(C'\) and the threshold for \(x\) depend on \(\delta,c_*,C,D_*,q\), on \(K\) and the \(a_i\), and on the constants \(C_{\rm tc}\) of (2.3).

The bound is uniform in \(F\), in the supports of \(\alpha,\beta\) and in the coefficients themselves; only their bounds and the constants of (2.3) enter.

**Theorem 2.3 (prime predecessors).** Under (2.1), let \(I\subseteq[H_m,2H_m]\) be an interval, \(|v|\le L^C\), and

\[
\begin{gathered}
\alpha_m=m^{iv}\Bigl(\mathbf 1_{m\ \text{prime}}\\
-\frac{\mathbf 1_{m\ \text{rough}}}{V(W)\log m}\Bigr)\quad(m\in I),\quad(2.5)
\end{gathered}
\]

with \(\alpha_m=0\) for \(m\notin I\). Then \(\alpha\) is supported on rough integers, \(|\alpha_m|\le2\), and \(\alpha\) has twisted cancellation with constants \(C_{\rm tc}\) depending only on \(\delta,c_*,C\) and on \(A_0,B,A\). Consequently (2.4) holds for this \(\alpha\) and every \(\beta,F\) as in Theorem 2.2, uniformly in \(I\) and \(v\).

The density factor in (2.5) has a simple origin: rough integers near \(m\) have density about \(V(W)\), and primes have density about \(1/\log m\). The coefficient (2.5) therefore has mean zero against smooth weights, and Theorem 2.3 says that it keeps mean zero against the marked predecessor weights. The trivial bound for (2.2) is \(|\mathfrak B|\le4C_{K,q}L^{2C}X\) by Lemma 1.1, so (2.4) is a saving of every fixed power of \(L\).

**Remark 2.4 (the role of the marks).** If \(F\) were allowed to be an arbitrary function with \(|F|\le1\), one could take \(F(h)\) to be the conjugate of the sign of \(\sum_{mn-1=h}\alpha_m\beta_n\mathcal W(h)\), and (2.2) would become a sum of absolute values without any cancellation. Group invariance forbids this choice: \(F\) cannot see the marks, while \(\mathcal W\) counts them. The proof exploits exactly this. It expands \(\mathcal W(mn-1)\) as a sum over marking products \(b\mid mn-1\), so that \(F\) depends only on the cofactor \(h=(mn-1)/b\), and then applies Cauchy's inequality in \(h\). What remains is a sum over pairs of marking products and quadruples \((m,n,r,s)\), in which \(F\) does not appear.

**Remark 2.5 (the number of groups).** Each group contributes a factor to the final saving in the minor-arc analysis of Lessons 14–16, and the required number of groups grows with \(C\) and \(D_*\). It does not depend on the band exponents \(a_i\), nor on \(\delta\), \(c_*\) or \(q\). In applications the groups are fixed first and \(x\) then tends to infinity.

## 3. Outline of the proof

**Analytic inputs (Lessons 2–6).** [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md) collects prime counts in short ranges, divisor moments, mean values of Dirichlet polynomials and counts of rough integers. [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md) bounds \(\sum n^{it}\) over progressions of length \(x^{\delta}\) or more. [*A mean value theorem and logarithmic phases at large height*](a-mean-value-theorem-and-logarithmic-phases-at-large-height.md) proves a mean value theorem of Vinogradov type with constants uniform in the degree, and deduces cancellation for much shorter progressions. [*A zero-free strip at large height*](a-zero-free-strip-at-large-height.md) converts this into a zero-free region for Dirichlet \(L\)-functions of small modulus up to height \(x^3\), and [*Long prime polynomials*](long-prime-polynomials.md) deduces cancellation in \(\sum_p\chi(p)p^{-1+it}\) and proves that (2.5) has twisted cancellation. This reduces Theorem 2.3 to Theorem 2.2.

**The reduction (Lesson 7).** [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md) expands the marks, applies Cauchy's inequality, and turns the resulting square into a count of solutions of \(bmn-ars=b-a\), where \(a,b\) are marking products. The indicator of this equation is split by a circle integral into a major-arc part and a minor-arc part. Theorem 2.2 follows from two propositions: the minor-arc part is small, and the major-arc part is small.

**The minor arcs (Lessons 8–16).** The minor-arc part is written as a matrix coefficient \(\langle f,\mathcal Tg\rangle\) of an operator on states consisting of a lattice point together with lists of marks dividing its first coordinate ([*Physical states and good positions*](physical-states-and-good-positions.md)). A high moment of this operator controls the matrix coefficient ([*From the moment to the pairing*](from-the-moment-to-the-pairing.md)). The moment is an average over starting points, which [*Root residues*](root-residues.md) and [*Independent residue lines*](independent-residue-lines.md) replace by independent uniformly distributed lines modulo the marks. A prime that leaves the lists and returns later is kept in a memory, so that its divisibility probability is paid once ([*Lifespans and the memory space*](lifespans-and-the-memory-space.md), [*Truncation, adjoints and absolute bounds*](truncation-adjoints-and-absolute-bounds.md)). Each step of the moment then contracts: steps without memory traffic by cancellation on a balanced lattice box ([*Clean edges and the lattice box*](clean-edges-and-the-lattice-box.md)), and steps with memory traffic by a separation property of good positions ([*Dirty edges*](dirty-edges.md)). The last lesson of this part restores the distinctness of all prime labels by an expansion in equality constraints and assembles the minor-arc bound ([*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md)).

**The major arcs (Lesson 17).** [*The major term and the theorem*](the-major-term-and-the-theorem.md) separates the variables by characters and Mellin transforms. Twisted cancellation of \(\alpha\) is used there, and only there; a sparse-frequency argument with one isolated group prime controls the remaining integral. The lesson ends with the proof of Theorems 2.2 and 2.3.

## 4. Conventions and the order of parameters

Constants implied by \(O(\cdot)\) and \(\ll\) may depend on the fixed data \(\delta,c_*,C,q\), on \(K\) and the \(a_i\), and on every exponent fixed earlier in the argument; a subscript records dependence that matters. A statement "for large \(x\)" holds for \(x\) larger than a threshold depending on the same data. We write \(n\asymp H\) when \(n\) lies in a fixed bounded enlargement of \([H,2H]\).

Two kinds of dependence on \(K\) must be distinguished. A constant factor \(C_K\) is harmless, because \(K\) is fixed before \(x\) grows. A loss \(L^{cK}\) would be harmful, because the final choice of \(K\) is made to beat a power of \(L\). The exponents of \(L\) chosen before \(K\) are therefore always independent of \(K\). The order of choices is

\[
\begin{gathered}
D_*\ \to\ D_1\ \to\ E_0\ \to\ G\\
\to\ A_0\ \to\ K\ \to\ x,
\end{gathered}
\]

where \(D_1\) is the precision of the Cauchy square (Lesson 7), \(E_0\) that of the minor-arc moment (Lesson 9), \(G\) the contraction exponent of one step (Lessons 14–15), and \(A_0\) the exponent defining the major arcs (Lesson 7). The minor-arc moment also uses parameters that grow slowly with \(x\):

\[
\begin{gathered}
J=\lfloor L^{0.01}\rfloor,\qquad M=J+1,\\
R=\lceil L^{0.5}/2\rceil,\qquad N=2R,\\
B=\lceil L^2\rceil .
\end{gathered}
\]

Here \(M\) is the length of the lists of marks carried by a state, \(J\) of them shared along each step, \(N\) is the number of steps in the moment, and \(B\) bounds the size of the memory.

## 5. Exercises

**5.1.** Show that every marking product \(b\) satisfies \(\exp(\sum_iL^{a_i})\le b\le\exp(2\sum_iL^{a_i})\), and deduce \(L^{0.1}\le\log b\le2KL^{0.2}\).

**5.2.** Let \(b\) be a marking product dividing \(h\). Show that \(\omega(h/b)\ge\omega(h)-K\), with equality when no prime of \(b\) divides \(h\) to the second power, and deduce \(q^{\omega(h/b)}\le q^{\omega(h)-K}\).

**5.3.** Show that \(F\) is group-invariant if and only if \(F(h)=F(h')\) whenever \(h/h'\) is a quotient of two products of group primes, that is, if and only if \(F(h)\) depends only on the largest divisor of \(h\) coprime to all group primes.

**5.4.** Prove the trivial bound \(|\mathfrak B|\le4C_{K,q}L^{2C}X\) under the hypotheses of Theorem 2.2.

**5.5.** For the coefficient (2.5), check \(|\alpha_m|\le2\) for large \(x\), using Mertens' product \(V(W)\gg L^{-0.24}\) from [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02), Theorem 4.2.

## 6. Solutions

**5.1.** Each \(p_i\) satisfies \(L^{a_i}\le\log p_i\le2L^{a_i}\); add over \(i\). Since \(0.1<a_i<0.2\) and \(K\ge1\), \(\sum_iL^{a_i}\ge L^{0.1}\) and \(2\sum_iL^{a_i}\le2KL^{0.2}\).

**5.2.** The marks of \(h/b\) include every mark of \(h\) other than \(p_1,\dots,p_K\), so \(h/b\) loses at most \(K\) marks. If \(p_i^2\nmid h\) for every \(i\), then no \(p_i\) divides \(h/b\), and exactly \(K\) marks are lost. Since \(0<q<1\), a larger exponent gives a smaller power.

**5.3.** If \(F\) is group-invariant, removing the group prime factors of \(h\) one at a time shows that \(F(h)=F(h^\flat)\), where \(h^\flat\) is the largest divisor of \(h\) coprime to all group primes; two integers whose quotient is a quotient of products of group primes have the same \(h^\flat\). Conversely, \(ph\) and \(h\) have the same \(h^\flat\) when \(p\) is a group prime.

**5.4.** By Lemma 1.1, \(|\mathfrak B|\le C_{K,q}\sum_{m,n}|\alpha_m\beta_n|\)\(\le C_{K,q}L^{2C}(H_m+1)(H_n+1)\), and \((H_m+1)(H_n+1)\le4X\).

**5.5.** Mertens' product gives \(V(W)=(1+o(1))e^{-\gamma}/\log W\), so \(V(W)\log m\ge V(W)\log H_m\)\(\gg L^{-0.24}\cdot\delta L\to\infty\). A prime \(m\ge H_m\) exceeds \(W\), so it is rough, and \(|\alpha_m|=|1-1/(V(W)\log m)|\le1\). A rough composite \(m\) has \(|\alpha_m|=1/(V(W)\log m)=o(1)\). Every other \(m\) has \(\alpha_m=0\). Hence \(|\alpha_m|\le2\), and \(\alpha\) is supported on rough integers.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Theorem 3.1 and Sections 2–5 and 9. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
