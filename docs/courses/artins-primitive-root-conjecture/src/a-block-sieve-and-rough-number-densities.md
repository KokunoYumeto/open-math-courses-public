# A block sieve and rough-number densities

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lessons 16–19 prove Proposition 5.1 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md): many primes \(p\le 2x\) have \(p-1=crQ\) with \(Q\) a large prime and all prime factors of \(r\) in a middle range. The construction counts integers \(d\) with a controlled predecessor and removes the composite \(d\). This lesson supplies the two elementary tools. The first is a block form of the Brun–Hooley sieve, due in this form to Ford and Halberstam, whose error terms carry no divisor weights. The second is Buchstab's least-prime-factor identity for the densities of rough numbers, together with an upper bound for these densities that comes from the block sieve.

**Prerequisites.** [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 3.1 and 4.2; [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09), Theorem 3.1.

## 1. Notation

Let \(x\) be large and put
\[
\begin{gathered}
L=\log x,\\
W=\exp(L^{0.24}),\\
V(y)=\prod_{p\le y}\Bigl(1-\frac1p\Bigr).\quad(1.1)
\end{gathered}
\]
For an integer \(m>1\) let \(P^-(m)\) be its least prime factor, and \(P^-(1)=\infty\); \(m\) is **\(y\)-rough** if \(P^-(m)>y\). By Mertens' product theorem (Theorem 4.2 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)),
\[
\begin{gathered}
V(y)\sim\frac{e^{-\gamma_E}}{\log y}\\
(y\to\infty),\quad(1.2)
\end{gathered}
\]
with Euler's constant \(\gamma_E\).

For \(w>\gamma>0\) define the **rough-number densities**
\[
\begin{aligned}
&D_\gamma(w)=\sum_{j\ge1}D_{\gamma,j}(w),\\
&D_{\gamma,1}(w)=\frac1w,\\
&D_{\gamma,j}(w)=\frac1{j!}\int_{\substack{t_i\ge\gamma\ (i<j)\\ \sum_{i<j}t_i\le w-\gamma}}\frac1{w-\sum_{i<j}t_i}\\
&\qquad\times\prod_{i<j}\frac{dt_i}{t_i}\quad(j\ge2).\quad(1.3)
\end{aligned}
\]
The term \(D_{\gamma,j}(w)\) vanishes unless \(w\ge j\gamma\), so the sum is finite. The \(j\)th term is the density of products of \(j\) primes larger than \(x^\gamma\), in logarithmic coordinates \(t=\log p/L\), the factor \(1/j!\) removing the order of the primes.

**Lemma 1.1** (meaning and regularity [OpenAI-029, (10.10)]). For an interval \(I\) with closure in \((x^\gamma,\infty)\) and every \(j\ge1\),
\[
\begin{aligned}
&\frac1{j!}\int_{\substack{y_i>x^\gamma\\ \prod_iy_i\in I}}\prod_{i=1}^j\frac{dy_i}{\log y_i}\\
&\quad =\frac1L\int_ID_{\gamma,j}\Bigl(\frac{\log y}L\Bigr)dy .\quad(1.4)
\end{aligned}
\]
The functions \(D_{\gamma,j}\) and \(D_\gamma\) are jointly continuous on compact subsets of \(\{w>\gamma>0\}\) and, for fixed \(\gamma\), Lipschitz in \(w\) on compact intervals; in particular \(wD_\gamma(w)\) has bounded total variation on every compact interval above \(\gamma\).

*Proof.* For \(j=1\) both integrands are \(1/\log y\). For \(j\ge2\) change variables to \(y=\prod_iy_i\) and \(t_i=\log y_i/L\) for \(i<j\), with \(w=\log y/L\); then \(\log y_j=L(w-\sum_{i<j}t_i)\) and
\[
\prod_{i=1}^j\frac{dy_i}{\log y_i}=\frac{dy}L\,\frac{\prod_{i<j}dt_i/t_i}{w-\sum_{i<j}t_i},
\]
because \(dy_i=Ly_i\,dt_i\) and \(\log y_i=Lt_i\) for \(i<j\), while for fixed \(y_1,\dots,y_{j-1}\), \(dy_j=dy/\prod_{i<j}y_i\) and \(\log y_j=L(w-\sum_{i<j}t_i)\); the factors \(y_i\) cancel. The strict and weak inequalities differ on null sets. For the regularity at the points \(w=j\gamma\), put \(s=w-j\gamma\ge0\), \(t_i=\gamma+sy_i\) for \(i<j\), and \(y_j=1-\sum_{i<j}y_i\):
\[
\begin{aligned}
&D_{\gamma,j}(w)=\frac{s^{j-1}}{j!}\\
&\quad\int_{\substack{y_i\ge0\\ \sum_{i<j}y_i\le1}}\ \prod_{i\le j}\frac1{\gamma+sy_i}\ \prod_{i<j}dy_i ,
\end{aligned}
\]
with every denominator bounded below by \(\gamma\); extended by zero for \(s<0\), this is continuous and Lipschitz on compact sets. \(\square\)

## 2. A block sieve with bounded coefficients

**Lemma 2.1** (block sieve [OpenAI-029, Lemma 11.1]). Let \(\mathcal A\) be a finite set with nonnegative weights, \(z\ge2\), and \(\mathcal P\) a set of primes at most \(z\); for each \(p\in\mathcal P\) let a **bad condition** on \(\mathcal A\) be given. Suppose that for every squarefree \(d\) composed of primes of \(\mathcal P\) the weight of the objects satisfying the bad conditions at all \(p\mid d\) is
\[
A(d)=X'g(d)+E(d),
\]
with \(X'\ge0\), \(g\) multiplicative, \(g(1)=1\), and, for fixed \(\eta_0>0\) and \(C_0\),
\[
\begin{gathered}
0\le g(p)\le1-\eta_0,\\
\sum_{\substack{v<p\le v^2\\ p\in\mathcal P}}g(p)\le C_0\quad(v>1).\quad(2.1)
\end{gathered}
\]
Then for every sufficiently large even integer \(H\) the weight \(S\) of the objects satisfying no bad condition is
\[
\begin{aligned}
S&=X'\prod_{p\in\mathcal P}(1-g(p))\bigl(1+O(e^{-H})\bigr)\\
&\quad+O\Bigl(\sum_{\substack{d\le z^{4H+2}\\ d\mid\prod_{p\in\mathcal P}p}}|E(d)|\Bigr),\quad(2.2)
\end{aligned}
\]
and for \(H=2\)
\[
\begin{aligned}
S&\le C\,X'\prod_{p\in\mathcal P}(1-g(p))\\
&\quad +\sum_{\substack{d\le z^{10}\\ d\mid\prod_{p\in\mathcal P}p}}|E(d)|.\quad(2.3)
\end{aligned}
\]
The constants and the threshold for \(H\) depend only on \(\eta_0\) and \(C_0\).

*Proof.* Let \(b_p\in\{0,1\}\) indicate the bad condition at \(p\). Divide \(\mathcal P\) into the blocks \(\mathcal B_j=\{p\in\mathcal P:z^{2^{-j-1}}<p\le z^{2^{-j}}\}\), \(j\ge0\), and put \(h_j=(j+1)H\), which is even. Let \(I_j\) indicate that no condition of block \(j\) holds, and
\[
\begin{gathered}
U_j=\sum_{\substack{J\subseteq\mathcal B_j\\ |J|\le h_j}}(-1)^{|J|}\prod_{p\in J}b_p,\\
T_j=\sum_{\substack{J\subseteq\mathcal B_j\\ |J|=h_j+1}}\prod_{p\in J}b_p .
\end{gathered}
\]
If exactly \(t\) conditions of block \(j\) hold, then \(U_j=\sum_{a=0}^{h_j}(-1)^a\binom ta\), which is \(1\) for \(t=0\) and \(\binom{t-1}{h_j}\) for \(t\ge1\), because \(h_j\) is even; and \(T_j=\binom t{h_j+1}\ge\binom{t-1}{h_j}\). Hence \(0\le I_j\le U_j\) and \(U_j-I_j\le T_j\). Telescoping the product of nonnegative factors,
\[
0\le\prod_jU_j-\prod_jI_j\le\sum_jT_j\prod_{k\ne j}U_k ,
\]
so the polynomials \(U=\prod_jU_j\) and \(B=U-\sum_jT_j\prod_{k\ne j}U_k\) in the \(b_p\) satisfy \(B\le\mathbf 1_{\text{no bad condition}}\le U\).

*Coefficients and supports.* A monomial of \(U\) has degree at most \(h_j\) in block \(j\); a monomial of the \(j\)th correction has degree exactly \(h_j+1\) in block \(j\) and at most \(h_k\) in the others. So these sets of monomials are pairwise disjoint, each monomial occurs once, and every coefficient of \(U\) and \(B\) is \(0\) or \(\pm1\). The product of the primes of a monomial of \(U\) has logarithm at most \(\log z\sum_j(j+1)H2^{-j}=4H\log z\), and a correction adds at most \(\log z\); so every monomial corresponds to a squarefree \(d\le z^{4H+2}\).

*Main terms.* Let the \(b_p\) be independent Bernoulli variables with means \(g(p)\), and write \(\mathbb E\) for this auxiliary expectation; by multiplicativity, \(\mathbb E\prod_{p\mid d}b_p=g(d)\). Each block lies in an interval \((v,v^2]\), so by (2.1) and \(-\log(1-u)\le u/\eta_0\) for \(0\le u\le1-\eta_0\),
\[
\begin{gathered}
\begin{aligned}
a_j&=\mathbb EI_j=\prod_{p\in\mathcal B_j}(1-g(p))\\
&\ge e^{-C_0/\eta_0}=:a_*,
\end{aligned}\\
t_j=\mathbb ET_j\le\frac{C_0^{h_j+1}}{(h_j+1)!},\\
a_j\le\mathbb EU_j\le a_j+t_j .
\end{gathered}
\]
Put \(R_H=\sum_jt_j/a_j\). Since \(C_0^n/n!\le e^{-2n}\) for large \(n\), \(R_H\le Ce^{-H}\) for large even \(H\); for \(H=2\), \(R_H\) is bounded. By independence of the blocks,
\[
\begin{gathered}
\prod_ja_j\le\mathbb EU\le e^{R_H}\prod_ja_j,\\
\mathbb E(U-B)\le R_He^{R_H}\prod_ja_j ,
\end{gathered}
\]
and \(\prod_ja_j=\prod_{p\in\mathcal P}(1-g(p))\).

*Back to \(\mathcal A\).* Summing a polynomial \(\sum_Jc_J\prod_{p\in J}b_p\) over \(\mathcal A\) with the weights gives \(\sum_Jc_JA(d_J)\)\(=X'\sum_Jc_Jg(d_J)+\sum_Jc_JE(d_J)\), that is, \(X'\) times its expectation plus at most \(\sum_{d\le z^{4H+2}}|E(d)|\). Since \(S\) lies between the sums of \(B\) and of \(U\), (2.2) and (2.3) follow. \(\square\)

## 3. Rough-number densities

**Lemma 3.1** (Buchstab's identity and an upper bound [OpenAI-029, Lemma 11.2]). For \(0<b<\frac12\),
\[
\begin{aligned}
&\int_b^{1/2}D_t(1-t)\,\frac{dt}t\\
&\quad =D_b(1)-1,\quad(3.1)
\end{aligned}
\]
the integrand at \(\frac12\) taken as its left limit. There are absolute constants \(b_0,C_d>0\) such that for \(0<b<b_0\),
\[
\begin{aligned}
D_b(1)&\le\frac{e^{-\gamma_E}}b\bigl(1+C_de^{-1/(20b)}\bigr).\quad(3.2)
\end{aligned}
\]

*Proof.* *The identity.* Write the \(j\)th term of \(D_b(1)\), \(j\ge2\), as the integral of the measure \(\frac1{j!}\frac{dt_1\cdots dt_{j-1}}{t_1\cdots t_j}\) over \(t_1+\cdots+t_j=1\), \(t_i\ge b\), where \(t_j=1-\sum_{i<j}t_i\). This measure is invariant under permutations of all \(j\) coordinates: exchanging \(t_j\) with an independent coordinate is a linear change of variables with determinant \(\pm1\). Off a null set the smallest coordinate is unique; select it in \(j\) ways and call its value \(t\le\frac12\). The other \(j-1\) coordinates sum to \(1-t\) and are at least \(t\), and their measure is the \((j-1)\)st term of \(D_t(1-t)\) times \(dt/t\), since \(j/j!=1/(j-1)!\). Summing over \(j\ge2\) gives (3.1); the term \(j=1\) of \(D_b(1)\) is \(1\).

*A lower bound by rough integers.* Let \(R_b(x)\)\(=\#\{n:x<n\le2x,\ P^-(n)>x^b\}\). We show \(D_b(1)\le\liminf_{x\to\infty}\frac LxR_b(x)\). Fix \(j\ge2\) and \(\eta>0\), and count ordered lists of primes \((p_1,\dots,p_j)\), each with weight \(1/j!\), with \(p_i>x^b\) for \(i<j\), \(Q=p_1\cdots p_{j-1}<x^{1-b-\eta}\), and \(x/Q<p_j\le2x/Q\). Then \(p_j>x^{b+\eta}\), so the product lies in \(R_b(x)\); an integer with prime multiplicities \(e_1,e_2,\dots\) receives total weight \(1/\prod e_i!\le1\), and its number of prime factors determines \(j\). With the primes in \((x,2x]\) this gives a lower bound for \(R_b(x)\). By the prime number theorem (Theorem 3.1 of [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09)), uniformly for \(Q<x^{1-b-\eta}\), the number of \(p_j\) is \((1+o(1))x/(Q\log(x/Q))\). By Mertens' estimate (Theorem 3.1 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)), \(\sum_{x^\alpha<p\le x^\beta}1/p\to\log(\beta/\alpha)\) for fixed \(0<\alpha<\beta\), so the measures \(\sum_p p^{-1}\delta_{\log p/L}\) converge to \(dt/t\) on compact subsets of \((0,\infty)\), and so do their finite products. On the truncated simplex \(t_i\ge b\), \(\sum_{i<j}t_i<1-b-\eta\), the function \((1-\sum_{i<j}t_i)^{-1}\) is bounded and the boundary is null. Hence \(\frac Lx\) times the weighted count tends to
\[
\frac1{j!}\int_{\substack{t_i\ge b\ (i<j)\\ \sum_{i<j}t_i<1-b-\eta}}\frac1{1-\sum_{i<j}t_i}\prod_{i<j}\frac{dt_i}{t_i},
\]
and the primes in \((x,2x]\) contribute \(1\). Only finitely many \(j\) occur. Letting \(x\to\infty\) and then \(\eta\downarrow0\) gives the claim.

*An upper bound by the block sieve.* Apply Lemma 2.1 to the integers \(n\in(x,2x]\) with weight \(1\), \(z=x^b\), \(\mathcal P\) the primes up to \(z\), and the bad conditions \(p\mid n\). Then \(X'=x\), \(g(d)=1/d\), \(|E(d)|\le1\), and (2.1) holds with \(\eta_0=\frac12\) and an absolute \(C_0\), by Mertens' estimate. Take \(H=2\lfloor1/(40b)\rfloor\); for small \(b\) it is admissible, and \(b(4H+2)\le\frac15+2b<1\). Lemma 2.1 gives
\[
\begin{gathered}
\begin{aligned}
R_b(x)&\le xV(x^b)\bigl(1+Ce^{-H}\bigr)\\
&\quad +C\,x^{1/5+2b},
\end{aligned}\\
e^{-H}\le e^2e^{-1/(20b)} .
\end{gathered}
\]
Multiply by \(L/x\) and let \(x\to\infty\); by (1.2), \(LV(x^b)\to e^{-\gamma_E}/b\). With the lower bound this proves (3.2). \(\square\)

In (3.1), the term \(1\) is the contribution of the primes, and the integral is the contribution of the composite rough numbers, organized by their least prime factor \(x^t\). This is the subtraction used in Lesson 19: after the composites are removed, a positive mass of primes remains.

## 4. Exercises

**4.1.** Verify \(\sum_{a=0}^h(-1)^a\binom ta=(-1)^h\binom{t-1}h\) for \(t\ge1\).

**4.2.** Compute \(D_b(1)\) for \(\frac13<b<\frac12\), and check (3.1) in this range.

**4.3.** Show that \(\sum_{j\ge0}(j+1)2^{-j}=4\).

**4.4.** For \(b=1/100\), compute \(H=2\lfloor1/(40b)\rfloor\) and the exponent \(b(4H+2)\).

**4.5.** Explain why \(e^{-\gamma_E}/b\) is the natural size of \(D_b(1)\), using the heuristic that an integer near \(x\) is \(x^b\)-rough with probability about \(V(x^b)\).

## 5. Solutions

**4.1.** By induction on \(h\): the case \(h=0\) is \(1=\binom{t-1}0\), and \((-1)^{h-1}\binom{t-1}{h-1}+(-1)^h\binom th\)\(=(-1)^h\bigl(\binom th-\binom{t-1}{h-1}\bigr)\)\(=(-1)^h\binom{t-1}h\).

**4.2.** For \(b>\frac13\) only \(j=1,2\) occur, and \(D_{b,2}(1)=\frac12\int_b^{1-b}\frac{dt}{t(1-t)}=\log\frac{1-b}b\). So \(D_b(1)=1+\log\frac{1-b}b\). On the left of (3.1), for \(t\in(b,\frac12)\) one has \(1-t<2t\), so \(D_t(1-t)=\frac1{1-t}\), and \(\int_b^{1/2}\frac{dt}{t(1-t)}=\log\frac{1-b}b\).

**4.3.** \(\sum_{j\ge0}(j+1)y^j=(1-y)^{-2}\), which is \(4\) at \(y=\frac12\).

**4.4.** \(1/(40b)=2.5\), so \(H=4\), and \(b(4H+2)=18/100=0.18\).

**4.5.** The density of \(x^b\)-rough integers near \(x\) is \(V(x^b)\sim e^{-\gamma_E}/(bL)\) by (1.2); \(D_b(1)/L\) is the density of rough integers in the logarithmic normalization of (1.4), so \(D_b(1)\approx LV(x^b)\approx e^{-\gamma_E}/b\) for small \(b\). The sieve bound (3.2) makes the upper half of this precise.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 10 and 11. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [FH] K. Ford and H. Halberstam, *The Brun–Hooley sieve*, J. Number Theory 81 (2000), 335–350, Section 1, Lemma 1. https://doi.org/10.1006/jnth.1999.2479
- [Buchstab] A. Buchstab, *Asymptotische Abschätzung einer allgemeinen zahlentheoretischen Funktion*, Mat. Sbornik 2(44) (1937), 1239–1246. https://www.mathnet.ru/eng/sm5649
- [OpenAI-WDG] OpenAI, *Weighted dilation graphs, smooth shifted primes and totient fibers*, OpenAI Math Release preprint, 24 September 2026, Lemmas 2.9 and 7.4. https://github.com/openai/math/tree/main/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026
