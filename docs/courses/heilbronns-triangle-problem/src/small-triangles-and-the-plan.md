# Small triangles and the plan

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Heilbronn asked how large the smallest triangle formed by \(n\) points of the unit square can be made. Simple constructions give order \(n^{-2}\); Komlós, Pintz and Szemerédi improved this by a logarithmic factor in 1982, and it was asked whether \(n^{-2+\varepsilon}\) is the truth for every \(\varepsilon>0\). This course proves OpenAI's 2026 theorem that the answer is no: there is a fixed \(\eta>0\) such that \(n\) points can be placed with every triangle of area at least a constant times \(n^{-2+\eta}\).

This lesson defines the problem, proves the classical lower bound from a parabola over a finite field, relates triangle areas of rational points to determinants of integer columns, proves the form of Bertrand's postulate used throughout, and explains the plan. The proof uses lattices (second lesson), field norms written in a large base (third), matrices over residue rings (fourth), a cap in a three-dimensional space over a finite field (fifth), a probabilistic count of small determinants (sixth and seventh), and a deletion argument (eighth).

We use from the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (Lebl, *Basic Analysis*) the extreme value theorem for continuous functions on compact metric spaces ([Theorem 7.5.6](https://www.jirka.org/ra/html/sec_metcont.html)).

## 1. The problem

For points \(p,q,r\in\mathbb R^2\) put
\[
\operatorname{Area}(pqr)=\tfrac12|\det(q-p,r-p)|,
\]
the area of the triangle they span (zero if they are collinear). For a finite set \(P\subseteq[0,1]^2\) with at least three points let
\[
\Delta(P)=\min\{\operatorname{Area}(pqr):\{p,q,r\}\subseteq P\text{ three distinct points}\},\qquad\Delta(n)=\sup\{\Delta(P):P\subseteq[0,1]^2,\ |P|=n\}.
\]

**Lemma 1.1.** For \(n\geq3\) the supremum \(\Delta(n)\) is attained and positive.

*Proof.* The function \(F(x_1,\ldots,x_n)=\min_{i<j<l}\operatorname{Area}(x_ix_jx_l)\) is continuous on the compact space \(([0,1]^2)^n\), so it attains a maximum (Lebl, Theorem 7.5.6). An \(n\)-tuple with a repeated point has \(F=0\), and an \(n\)-tuple of distinct points is a set \(P\) with \(F=\Delta(P)\); so \(\Delta(n)=\max F\). Distinct points on the parabola \(y=x^2\) have no three on a line (a line meets the parabola at most twice), so \(\max F>0\). \(\square\)

The problem was posed by Heilbronn; Roth proved the first upper bound \(o(1/n)\) in 1951, and later work of Schmidt, Roth, Komlós, Pintz and Szemerédi, and Cohen, Pohoata and Zakharov reduced it to \(n^{-7/6+o(1)}\). On the lower side, the classical bound is of order \(n^{-2}\):

**Proposition 1.2 (Erdős's parabola).** For every prime \(p\), the \(p\) points
\[
P_p=\Bigl\{\Bigl(\frac xp,\frac{\{x^2\}_p}p\Bigr):0\leq x<p\Bigr\}\subseteq[0,1)^2,
\]
where \(\{x^2\}_p\) is the remainder of \(x^2\) modulo \(p\), satisfy \(\Delta(P_p)\geq\frac1{2p^2}\).

*Proof.* Let \(x_1,x_2,x_3\) be distinct in \(\{0,\ldots,p-1\}\) and \(y_i=\{x_i^2\}_p\). The triangle with vertices \((x_i,y_i)/p\) has area \(|\det M|/(2p^2)\), where \(M\) is the integer matrix with rows \((1,x_i,y_i)\) (subtract the first row from the others and expand). Modulo \(p\), \(y_i\equiv x_i^2\), so \(\det M\) is congruent to the Vandermonde determinant \(\prod_{i<j}(x_j-x_i)\), which is not divisible by the prime \(p\). So \(\det M\) is a nonzero integer. \(\square\)

With Bertrand's postulate (Section 4) this gives \(\Delta(n)\geq c\,n^{-2}\) for all large \(n\): take a prime \(n<p\leq2n\) and any \(n\) points of \(P_p\). Random points with a few deletions give the same order. Komlós, Pintz and Szemerédi proved \(\Delta(n)\geq c\,(\log n)/n^2\) in 1982, and the question became whether, for every \(\varepsilon>0\) and all large \(n\),
\[
\Delta(n)\leq C_\varepsilon n^{-2+\varepsilon}.\tag{1.1}
\]

**Theorem 1.3 (OpenAI, 2026).** There are constants \(\eta,c_1>0\) and an integer \(n_0\) such that
\[
\Delta(n)\geq c_1n^{-2+\eta}\qquad\text{for every }n\geq n_0 .
\]

In particular \(\Delta(n)\geq n^{-2+\eta/2}\) for all large \(n\), since \(c_1n^{\eta/2}\to\infty\); this contradicts (1.1) for \(\varepsilon=\eta/2\). The proof gives an explicit, extremely small, \(\eta\) (eighth lesson).

## 2. Points from integer columns

The construction works with integer *columns* \(u=(u_1,u_2,u_3)^{\mathsf T}\) whose third coordinate is positive, and their *projections*
\[
\pi(u)=\Bigl(\frac{u_1}{u_3},\frac{u_2}{u_3}\Bigr).
\]
Two such columns have the same projection exactly when they are proportional.

**Lemma 2.1 (area of projected points).** For columns \(u,v,w\in\mathbb R^3\) with positive third coordinates, and \(A\) the matrix with columns \(u,v,w\),
\[
\operatorname{Area}\bigl(\pi(u)\pi(v)\pi(w)\bigr)=\frac{|\det A|}{2\,u_3v_3w_3}.
\]

*Proof.* Dividing each column by its third coordinate divides the determinant by \(u_3v_3w_3\) and gives the columns \((\pi(u),1)\), \((\pi(v),1)\), \((\pi(w),1)\). Subtracting the first of these from the other two does not change the determinant, which becomes \(\pm\det(\pi(v)-\pi(u),\pi(w)-\pi(u))\), that is, \(\pm2\operatorname{Area}\). \(\square\)

So if all columns lie in the box \([0,N)^2\times[N,2N)\) and all determinants of three distinct columns have absolute value greater than \(\tau\), every triangle of the projected points has area at least \(\tau/(2(2N)^3)=\tau/(16N^3)\). Small areas come from small determinants. Erdős's parabola is the case where all determinants are nonzero multiples of \(p\)-adic units; the new construction makes *most* determinants large and then deletes the few exceptions.

## 3. The plan

Columns are sampled at random in the box \(\mathcal B=([0,N)^2\times[N,2N))\cap\mathbb Z^3\) with prescribed residues modulo two coprime numbers \(h\) and \(q\).

*The main modulus \(h=B^k\)* (third and fourth lessons). Every column carries a random *label* \(\xi\) in a finite field \(K=\mathbb F_{r^d}\). Over \(K\) the columns \((1,\xi,\xi^2)\) have nonzero determinant whenever their labels are distinct, as in Erdős's parabola. Taking a field norm turns this into a polynomial identity over \(\mathbb F_r\), and writing the polynomial in base \(B\) places it at one digit of the determinant of the residue columns. Distinct labels then force the determinant modulo \(h\) to have no representative of absolute value at most \(\tau\approx B^{k-1}/2\): small determinants occur only when two labels coincide, which has probability about \(r^{-d}\). A random matrix of determinant one modulo \(h\) mixes the rows, so that the residues of the sampled columns are spread over an orbit whose size is controlled by a diagonal form.

*The auxiliary modulus \(q\)* (fifth lesson). Determinant zero needs separate control: three integer columns can be dependent while their residues modulo \(h\) are not. At a large prime \(q\), the residues are taken from a set with no three points on a line (an affine piece of an elliptic quadric), moved by a random translation and a random linear map. This excludes short integer relations among three columns.

*Counting* (second, sixth and seventh lessons). The probability that three sampled columns have a small determinant is written exactly as a weighted count of integer matrices with rows in a lattice and a fixed determinant; lattice counts with three different scales bound it, the case of determinant zero being organized by the null vector of the matrix.

*Deletion* (eighth lesson). With \(n\approx r\sqrt{N^3/\tau}\) samples, the expected number of bad pairs and triples is \(o(n)\); deleting one point from each leaves \(n\) points whose triangles all have area at least \(\tau/(16N^3)\). Since all parameters are powers of the prime \(r\), this area exceeds \(n^{-2}\) by a power of \(n\).

## 4. Primes in intervals

The parameters are chosen among primes in intervals \((n,2n]\). We prove the needed form of Bertrand's postulate by Erdős's argument with binomial coefficients. For a real \(x\geq1\) let \(\Theta(x)=\prod_{p\leq x}p\), the product over primes.

**Lemma 4.1.** \(\Theta(x)<4^x\) for every real \(x\geq1\).

*Proof.* It suffices to treat integers \(x\), by induction. For \(x=1,2\) the claim is clear. For even \(x>2\), \(x\) is not prime and \(\Theta(x)=\Theta(x-1)<4^{x-1}\). For \(x=2m+1\), every prime \(p\) with \(m+1<p\leq2m+1\) divides \((2m+1)!\) but not \(m!\,(m+1)!\), hence divides \(\binom{2m+1}m\). The two equal binomial coefficients \(\binom{2m+1}m=\binom{2m+1}{m+1}\) occur in the expansion of \((1+1)^{2m+1}\) together with other positive terms, so \(\binom{2m+1}m<2^{2m}=4^m\). Hence \(\Theta(2m+1)\leq\Theta(m+1)\binom{2m+1}m\), which is less than \(4^{m+1}4^m=4^{2m+1}\). \(\square\)

**Lemma 4.2 (Legendre).** For a prime \(p\) and an integer \(m\geq1\), the exponent of \(p\) in \(m!\) is \(\sum_{j\geq1}\lfloor m/p^j\rfloor\).

*Proof.* The exponent of \(p\) in \(m!=\prod_{i\leq m}i\) is \(\sum_{i\leq m}\#\{j\geq1:p^j\mid i\}\). Counting the pairs \((i,j)\) with \(p^j\mid i\) by \(j\) instead, this equals \(\sum_{j\geq1}\#\{i\leq m:p^j\mid i\}\), and there are \(\lfloor m/p^j\rfloor\) multiples of \(p^j\) up to \(m\). \(\square\)

**Lemma 4.3 (prime intervals).** For every sufficiently large integer \(n\) there is a prime \(p\) with \(n<p\leq2n\).

*Proof.* The binomial coefficient \(\binom{2n}n\) is the largest of the \(2n+1\) terms of \((1+1)^{2n}\), so \(\binom{2n}n\geq4^n/(2n+1)\). By Lemma 4.2 the exponent of a prime \(p\) in \(\binom{2n}n=(2n)!/(n!)^2\) is \(\sum_{j\geq1}(\lfloor2n/p^j\rfloor-2\lfloor n/p^j\rfloor)\); each term is \(0\) or \(1\) (since \(\lfloor2y\rfloor-2\lfloor y\rfloor\in\{0,1\}\)), and terms with \(p^j>2n\) vanish. So \(p\) contributes at most \(2n\) in total; a prime \(p>\sqrt{2n}\) has exponent at most one; and a prime with \(2n/3<p\leq n\) (and \(n\geq5\)) has exponent \(\lfloor2n/p\rfloor-2\lfloor n/p\rfloor=2-2=0\), because \(p^2>2n\).

Suppose there is no prime in \((n,2n]\). Then the primes \(p\leq\sqrt{2n}\), at most \(\sqrt{2n}\) of them, contribute at most \((2n)^{\sqrt{2n}}\), and the other prime factors of \(\binom{2n}n\) are distinct primes at most \(2n/3\). With Lemma 4.1,
\[
\frac{4^n}{2n+1}\leq\binom{2n}n\leq(2n)^{\sqrt{2n}}\,\Theta(2n/3)<(2n)^{\sqrt{2n}}\,4^{2n/3},
\]
that is, \(\frac n3\log4<\sqrt{2n}\log(2n)+\log(2n+1)\). This fails for all large \(n\), since the left side grows linearly and the right side like \(\sqrt n\log n\). \(\square\)

## 5. Exercises

**5.1.** Show that \(\Delta(3)=\frac12\).

**5.2.** For \(p=5\) list the points of \(P_5\) and check that the smallest triangle has area at least \(\frac1{50}\). Is the bound attained?

**5.3.** Deduce from Proposition 1.2 and Lemma 4.3 that \(\Delta(n)\geq\frac1{8n^2}\) for all large \(n\).

**5.4.** Show that if \(u,v\) have positive third coordinates and \(\pi(u)=\pi(v)\), then \(u\) and \(v\) are proportional, and conversely.

**5.5.** Show that Theorem 1.3 contradicts (1.1), and explain why a bound \(\Delta(n)\geq c(\log n)^{100}n^{-2}\) would not.

## 6. Solutions

**5.1.** For fixed \(q,r\), the function \(p\mapsto\operatorname{Area}(pqr)=\frac12|\det(q-p,r-p)|\) is the absolute value of an affine function of \(p\), hence convex, so on the square it is largest at a corner. Moving the three vertices to corners one at a time never decreases the area, and a triangle with vertices at corners of the unit square has area \(0\) or \(\frac12\). Three corners of the square give \(\frac12\).

**5.2.** \(P_5\) consists of \((0,0),(1,1),(2,4),(3,4),(4,1)\), divided by \(5\). The ten values of \(|\det M|\) are \(1,2,3,3,3,4,9,9,13,14\); the value \(1\) occurs for \(x=0,1,3\) (rows \((1,0,0),(1,1,1),(1,3,4)\)). So \(\Delta(P_5)=\frac1{50}\), and the bound of Proposition 1.2 is attained.

**5.3.** For a prime \(n<p\leq2n\), any \(n\) points of \(P_p\) have all triangles of area at least \(1/(2p^2)\geq1/(8n^2)\).

**5.4.** \(\pi(u)=\pi(v)\) means \(u_1/u_3=v_1/v_3\) and \(u_2/u_3=v_2/v_3\), that is \(u=(u_3/v_3)v\). Conversely, proportional columns with positive third coordinates have a positive ratio and the same projection.

**5.5.** Theorem 1.3 gives \(\Delta(n)/n^{-2+\eta/2}\geq c_1n^{\eta/2}\to\infty\), while (1.1) with \(\varepsilon=\eta/2\) bounds this ratio. A bound \(c(\log n)^{100}n^{-2}\) is smaller than \(C_\varepsilon n^{-2+\varepsilon}\) for every \(\varepsilon>0\) and large \(n\), so it does not contradict (1.1).

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
- [OpenAI-Lean] OpenAI Math Release, *A power improvement in the Heilbronn triangle lower bound*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/191.md
- [CPZ] A. Cohen, C. Pohoata and D. Zakharov, *A new upper bound for the Heilbronn triangle problem*, arXiv:2305.18253 (https://arxiv.org/abs/2305.18253), and *Lower bounds for incidences*, arXiv:2409.07658 (https://arxiv.org/abs/2409.07658).
- K. F. Roth (1951), P. Erdős (the parabola, recorded by Roth, and the 1932 proof of Bertrand's postulate), W. M. Schmidt (1972), J. Komlós, J. Pintz and E. Szemerédi (1981, 1982) and D. Zakharov's survey (2026) are named for credit; the course does not use their results.
