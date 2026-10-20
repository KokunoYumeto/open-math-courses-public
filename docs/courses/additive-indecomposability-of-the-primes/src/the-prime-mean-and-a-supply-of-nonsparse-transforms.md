# The prime mean and a supply of nonsparse transforms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 10 assumed that the primes with sparse transforms carry most of the harmonic mass of the band, built from their sparse spectra a nonnegative weight \(W\), and proved that its average over pairs \((a,d)\in A_0\times D_0\) is small. This lesson computes the average of \(W\) over primes, \(\sum_p(\log p)\phi(p/X)W(p)\approx UX\int\phi\) (Proposition 3.2), by expanding \(W\) into Dirichlet characters of moderate conductor and using the zeros of their \(L\)-functions. Coverage then says that every large prime is a difference \(a-d\), which transfers the prime average to the pair average, and the two bounds are incompatible. This proves Theorem 1.1 of Lesson 10.

The analytic input is a uniform estimate for prime sums twisted by all primitive characters of conductor up to \(Q_b=\exp(2Ke^{0.9L})\), with the possible exceptional character removed (Lemma 2.1). It follows from a smoothed explicit formula, the classical zero-free region with Page's theorem, and a log-free zero-density estimate for the whole family, all proved in the programme course on Dirichlet \(L\)-functions.

**Prerequisites.** [*A tensor budget and a contracting kernel*](a-tensor-budget-and-a-contracting-kernel.md); [*The functional equation of Dirichlet L-functions*](course:NT-DIRL/NT-DIRL-05), Theorem 2.1; [*Zero-free regions and the exceptional zero*](course:NT-DIRL/NT-DIRL-07), Lemma 1.2; [*Counting zeros and the explicit formula for ψ(x, χ)*](course:NT-DIRL/NT-DIRL-08), Theorem 1.1; [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17), Section 1; [*The prime number theorem with the classical error term*](course:NT-ZETA/NT-ZETA-12), Theorem 1.1.

The notation of Lesson 10 is in force: \(\log X=e^L\), \(R=\sqrt X\), the set \(\mathcal S\) with \(H=\sum_{p\in\mathcal S}1/p\ge0.68L\), the kernels \(b_p\), \(K=\lceil C_KL\rceil\), the weight \(W\), and \(U=e^{O(\epsilon_0L)}\).

## 1. A smoothed explicit formula

Fix a nonzero nonnegative smooth function \(\phi\) supported in a compact subset of \((\frac12,1)\), and put
\[
\Phi(s)=\int_0^\infty\phi(t)\,t^{s-1}\,dt .
\]
It is entire, \(\Phi(1)=\int\phi\), and repeated integration by parts gives \(\Phi(s)\ll_{\phi,j}(1+|\Im s|)^{-j}\) uniformly for \(-\frac12\le\Re s\le2\), for every \(j\ge0\).

**Lemma 1.1** (smoothed explicit formula [OpenAI-013, (5.17)]). Let \(\chi\) be a primitive nonprincipal character of conductor \(q\), and \(X\ge2\). Then
\[
\begin{aligned}
&\sum_{n\ge1}\Lambda(n)\chi(n)\phi(n/X)\\
&\quad =-\sum_\rho X^\rho\Phi(\rho)\\
&\qquad -\mathbf 1_{\chi(-1)=1}\Phi(0)\\
&\qquad +O_\phi\bigl(X^{-1/2}\log(2q)\bigr),\quad(1.1)
\end{aligned}
\]
where \(\rho\) runs over the nontrivial zeros with multiplicity; the zero sum converges absolutely. The implied constant depends only on \(\phi\); in particular it does not depend on the position of any real zero.

*Proof.* Mellin inversion gives \(\phi(x)=\frac1{2\pi i}\int_{(2)}\Phi(s)x^{-s}ds\), so the left side equals \(\frac1{2\pi i}\int_{(2)}\bigl(-\frac{L'}L(s,\chi)\bigr)X^s\Phi(s)\,ds\). Shift the line of integration to \(\Re s=-\frac12\). The poles crossed are the nontrivial zeros, with residue \(-mX^\rho\Phi(\rho)\) for a zero of multiplicity \(m\), and, when \(\chi\) is even, the simple trivial zero at \(s=0\), with residue \(-\Phi(0)\); odd characters have no trivial zero in \(-\frac12<\Re s<2\). Take the limit through heights \(\pm T_n\to\infty\) at distance at least \(c/\log(qT_n)\) from every zero ordinate, which exist because each unit interval of heights contains \(O(\log(q(|t|+2)))\) ordinates ([*Zero-free regions and the exceptional zero*](course:NT-DIRL/NT-DIRL-07), (1.6)). On these horizontal segments, the local expansion (1.7) there, together with the functional equation below for \(\Re s\le\frac12\), gives \(|L'/L(s,\chi)|\ll\log^2(qT_n)\), and the rapid decay of \(\Phi\) makes these segments vanish in the limit.

On \(\Re s=-\frac12\), the functional equation ([*The functional equation of Dirichlet L-functions*](course:NT-DIRL/NT-DIRL-05), (2.5)) gives
\[
\begin{aligned}
\frac{L'}L(s,\chi)&=-\log\frac q\pi\\
&\quad -\frac12\frac{\Gamma'}\Gamma\Bigl(\frac{1-s+a}2\Bigr)\\
&\quad -\frac12\frac{\Gamma'}\Gamma\Bigl(\frac{s+a}2\Bigr)\\
&\quad -\frac{L'}L(1-s,\overline\chi),
\end{aligned}
\]
with \(a\in\{0,1\}\) the parity of \(\chi\). Here \(\Re(1-s)=\frac32\), so the last term is bounded by \(-\zeta'/\zeta(\frac32)\), and both Gamma terms are \(O(\log(|\Im s|+2))\), since their arguments stay at distance at least \(\frac14\) from the poles of \(\Gamma'/\Gamma\). So \(|L'/L(s,\chi)|\ll\log(q(|\Im s|+2))\) on this line, and with the decay of \(\Phi\) the shifted integral is \(O_\phi(X^{-1/2}\log(2q))\). Absolute convergence of the zero sum follows from the zero count \(N(T,\chi)\ll T\log(qT)\) ([*Counting zeros and the explicit formula for ψ(x, χ)*](course:NT-DIRL/NT-DIRL-08), Theorem 1.1) and the decay of \(\Phi\). \(\square\)

## 2. Prime sums over a family of characters

Put
\[
\log Q_b=2Ke^{0.9L}.
\tag{2.1}
\]
Products of at most \(2K\) primes of \(\mathcal S\) are at most \(Q_b\), because every prime of \(\mathcal S\) has \(\log p\le e^{0.9L}\). Note that \(\log Q_b=o(\log X)\).

**The exceptional character.** Apply Section 1 of [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17) with the parameter \(T_b=Q_b^5\). Its statement (1.1) gives an absolute \(a_0>0\) such that, among all primitive characters of conductor at most \(T_b\) (the conductor-one character included), the box \(\Re s>1-a_0/\log(2T_b)\), \(|\Im s|\le T_b\), contains at most one zero; if it exists, it is a simple real zero of a real nonprincipal character \(\chi_1\). Call \(\chi_1\) the *exceptional character*. Its statement (1.4) gives absolute constants \(c,C\) with
\[
\begin{gathered}
N^*(\sigma,T_b)\le CT_b^{c(1-\sigma)}\\
(\tfrac12\le\sigma\le1),\quad(2.2)
\end{gathered}
\]
where \(N^*(\sigma,T_b)\) counts the zeros, with multiplicity, of all these \(L\)-functions with real part at least \(\sigma\) and \(|\Im\rho|\le T_b\), excluding only the exceptional zero itself.

**Lemma 2.1** (the total prime error [OpenAI-013, Lemma 5.3]). Fix \(C_K\) and \(\phi\). Let \(\mathcal F\) be the set of primitive characters of conductor at most \(Q_b\), including the conductor-one character and excluding the exceptional character. For every fixed \(D_1>0\),
\[
\begin{aligned}
&\sum_{\chi\in\mathcal F}\Bigl|\sum_{n\ge1}\Lambda(n)\chi(n)\phi(n/X)\\
&\qquad -\mathbf 1_{\chi=1}X\Phi(1)\Bigr|\\
&\quad \ll_{D_1,\phi,C_K}Xe^{-D_1L}.\quad(2.3)
\end{aligned}
\]

*Proof.* Put \(M=\log X=e^L\) and \(u_0=a_0/\log(2T_b)\). Every zero of a nonprincipal \(\chi\in\mathcal F\) with \(|\Im\rho|\le T_b\) has \(1-\Re\rho\ge u_0\). Let \(F(y)\) be the number of these zeros with \(\Re\rho\ge1-y\), over all nonprincipal \(\chi\in\mathcal F\). They are among the zeros counted by \(N^*\), so (2.2) gives \(F(y)\le Ce^{Ay}\) with \(A=5c\log Q_b\), and \(F(y)=0\) for \(y<u_0\). Since \(\log Q_b=o(M)\), eventually \(M\ge2A\). Summation by parts gives
\[
\begin{aligned}
&\sum_{\substack{\chi,\rho\\\Re\rho\ge1/2,\ |\Im\rho|\le T_b}}X^{\Re\rho-1}\\
&\quad =e^{-M/2}F(\tfrac12)\\
&\qquad +M\int_{u_0}^{1/2}e^{-My}F(y)\,dy\\
&\quad \ll e^{-Mu_0/2}.
\end{aligned}
\]
Here \(Mu_0\gg e^L/(Ke^{0.9L})=e^{0.1L}/K\), so this is smaller than \(e^{-DL}\) for every fixed \(D\) once \(L\) is large.

Sum the absolute values of the terms of (1.1) over the nonprincipal \(\chi\in\mathcal F\):

- the zeros with \(\Re\rho\ge\frac12\) and \(|\Im\rho|\le T_b\) contribute \(O_\phi(Xe^{-Mu_0/2})\);
- there are \(O(Q_b^2T_b\log(Q_bT_b))\) zeros with \(\Re\rho<\frac12\) and \(|\Im\rho|\le T_b\), contributing \(O_\phi(X^{1/2}Q_b^2T_b\log(Q_bT_b))\);
- by \(|\Phi(\rho)|\ll(1+|\Im\rho|)^{-3}\) and the zero count in dyadic ranges of heights, the zeros above \(T_b\) contribute \(O_\phi(XQ_b^2T_b^{-2}\log(Q_bT_b))\);
- the terms \(\Phi(0)\) and the remainders contribute \(O_\phi(Q_b^2(1+X^{-1/2}\log(2Q_b)))\).

Each is \(O(Xe^{-D_1L})\): the second and fourth because \(Q_b^7=X^{o(1)}\), and the third because \(Q_b^2T_b^{-2}=Q_b^{-8}\) and \(\log Q_b\ge e^{0.9L}\). For the conductor-one character, the prime number theorem with the classical error term ([*The prime number theorem with the classical error term*](course:NT-ZETA/NT-ZETA-12), Theorem 1.1) and partial summation give \(\sum\Lambda(n)\phi(n/X)\)\(=X\Phi(1)+O_\phi(Xe^{-c\sqrt{\log X}})\), and \(\sqrt{\log X}=e^{L/2}\). \(\square\)

The density estimate is used here in its log-free form, valid for all heights up to \(T_b\) and all conductors up to \(T_b\) simultaneously. Only the factor \(e^{Ay}\) with \(A=O(\log Q_b)=o(\log X)\) matters; any density bound of the shape \(N^*(1-y,T)\ll T^{O(y)}(\log T)^{O(1)}\) would do.

**Deleting a prime for the exceptional character.** If the exceptional character exists and its conductor is a product of primes of \(\mathcal S\), delete one of those primes from \(\mathcal S\); otherwise make no deletion. Keep \(K\) and \(Q_b\), and redefine \(W\), \(\mathcal L\), \(\mathcal U\), \(U\), \(H\) with the new set. By Lesson 10, (4.1) and Proposition 4.2 there still hold. After the deletion, every primitive character whose conductor is a squarefree product of primes of \(\mathcal S\) differs from the exceptional character.

## 3. The prime mean of the weight

**Local multiplicative coefficients.** For \(j=1,2\) and a character \(\lambda\) of \(\mathbb F_p^\times\) put
\[
\begin{gathered}
\begin{aligned}
c_{p,j}(\lambda)&=\frac1{p-1}\sum_{x\ne0}b_p(x)^j\,\overline{\lambda(x)},
\end{aligned}\\
\text{so that}\\
\begin{aligned}
b_p(x)^j&=\sum_\lambda c_{p,j}(\lambda)\lambda(x)\quad(x\ne0).
\end{aligned}
\end{gathered}
\]

**Lemma 3.1.** With absolute constants,
\[
\begin{gathered}
|c_{p,j}(\lambda)|\ll p^{-1/2}\quad(\lambda\ne1),\\
|c_{p,j}(1)|\ll p^{-1}\\
(j=1,2).\quad(3.1)
\end{gathered}
\]

*Proof.* The principal coefficients are the means of \(b_p\) and \(b_p^2\) over the units, which are \(O(\epsilon_0/p)\) by (4.5) of Lesson 10. By Parseval on the group of units, every coefficient is at most the root mean square of \(b_p^j\) over the units; for \(j=1\) this is \(O(p^{-1/2})\) by (4.5), and for \(j=2\) the mean of \(b_p^4\) is at most \(\|b_p\|_\infty^2\) times the mean of \(b_p^2\), again \(O(1/p)\). \(\square\)

**The character expansion of the weight.** Expand (4.7) of Lesson 10 over the two subsets \(I,J\), so that \(W(n)\) is the sum over \(I,J\) of \(\prod_{p\in I\cap J}b_p(n)^2\prod_{p\in I\triangle J}b_p(n)\). For \(n\) coprime to every prime of \(\mathcal S\), expand each local factor multiplicatively and group the resulting terms by the primitive character they induce:
\[
\begin{gathered}
W(n)=\sum_{\substack{\chi\ \text{primitive}\\\operatorname{cond}(\chi)\le Q_b}}C(\chi)\chi(n)\\
\Bigl(\bigl(n,\prod_{p\in\mathcal S}p\bigr)=1\Bigr).\quad(3.2)
\end{gathered}
\]
Only squarefree conductors supported on \(\mathcal S\) occur, and the conductor bound holds because \(|I\cup J|\le2K\).

Fix a primitive \(\chi\) of conductor \(d\). Its local component at each \(p\mid d\) is a prescribed nonprincipal character, and \(p\) lies in \(I\) only, in \(J\) only, or in both; by (3.1) the absolute coefficients at \(p\) total at most \(C/\sqrt p\). At \(p\in\mathcal S\) with \(p\nmid d\), the prime is absent (coefficient \(1\)) or uses a principal coefficient, with total at most \(1+C/p\). Dropping the restriction \(|I|,|J|\le K\) only enlarges this nonnegative majorant, so even the sum of the absolute values of all terms grouped into \(C(\chi)\) is at most
\[
\begin{aligned}
&\prod_{p\mid d}\frac C{\sqrt p}\prod_{\substack{p\in\mathcal S\\ p\nmid d}}\Bigl(1+\frac Cp\Bigr)\\
&\quad \le e^{C'L},\quad(3.3)
\end{aligned}
\]
since \(C/\sqrt p\le1\) for large \(p\) and \(\sum_{p\in\mathcal S}1/p=O(L)\). The principal coefficient keeps its signs: it is the mean of \(W\) over independent uniform unit residues, so
\[
\begin{aligned}
C(1)&=\mathcal R_K\mathcal U=U+o(Ue^{-1.6H})\\
&=(1+o(1))U .
\end{aligned}
\]

**Proposition 3.2** (the prime mean [OpenAI-013, (5.21)]). As \(L\to\infty\) along the sequence,
\[
\begin{aligned}
&\sum_{p\ \text{prime}}(\log p)\,\phi(p/X)\,W(p)\\
&\quad =(1+o(1))\,UX\int_0^\infty\phi(t)\,dt .\quad(3.4)
\end{aligned}
\]

*Proof.* Every prime \(p\) with \(\phi(p/X)\ne0\) exceeds every prime of \(\mathcal S\), since \(\exp(e^{0.9L})=X^{o(1)}\); so (3.2) holds at these primes. Apply Lemma 2.1 to the grouped sum, with \(D_1\) larger than the constants in (3.3) and in \(U=e^{O(\epsilon_0L)}\). The exceptional character does not occur among the \(\chi\) of (3.2), by the deletion. The total error is \(e^{C'L}\cdot Xe^{-D_1L}=o(UX)\), and the principal term is \(C(1)X\Phi(1)=(1+o(1))UX\int\phi\).

It remains to pass from \(\Lambda\) to primes. The prime powers \(n\le X\) that are not prime have \(\sum\Lambda(n)\ll X^{1/2}(\log X)^2\). There are at most \(Q_b^2\) primitive characters of conductor at most \(Q_b\), so these prime powers contribute at most \(e^{C'L}Q_b^2X^{1/2}(\log X)^2=X^{1/2+o(1)}\) to the grouped character sums, and, by the uniform bound (4.1) below, at most \(X^{1/2+o(1)}\) to the left side of (3.4). This covers also the prime powers of primes of \(\mathcal S\), where (3.2) need not hold. \(\square\)

## 4. Coverage of every large prime

Since \(|b_p(n)|\le1\), the number of subsets in (4.7) of Lesson 10 bounds \(W\):
\[
\begin{aligned}
W(n)&\le(K+1)^2\bigl(1+|\mathcal S|\bigr)^{2K}\\
&\le\exp\bigl(O(Ke^{0.9L})\bigr)\\
&=X^{o(1)}\quad(4.1)
\end{aligned}
\]
uniformly in \(n\).

**Proposition 4.1** (the pair average from coverage [OpenAI-013, (5.22)]). For large \(L\) along the sequence, with \(c_\phi>0\) depending only on \(\phi\),
\[
\begin{aligned}
&\frac1{m_Am_D}\sum_{a\in A_0}\sum_{d\in D_0}W(a-d)\\
&\quad \ge c_\phi\,U\,\frac X{m_Am_D\log X}.\quad(4.2)
\end{aligned}
\]

*Proof.* By coverage, every prime \(p\) with \(\phi(p/X)\ne0\) has, for large \(L\), a representation \(p=a-d\) with \(a\in A\), \(d\in D\), and \(a,-d\le X\) because both are nonnegative and \(p<X\). Remove the primes having a representation with \(a\le R+N_*\) or \(-d\le R+N_*\). By Theorem 3.1 of Lesson 2 their number is at most
\[
\begin{aligned}
&A(R+N_*)B(X)\\
&\qquad +A(X)B(R+N_*)\\
&\quad =X^{3/4+o(1)},
\end{aligned}
\]
and by (4.1) their contribution to the left side of (3.4) is \(X^{3/4+o(1)}=o(UX)\). Every remaining prime has a representation by a pair in \(A_0\times D_0\). Choose one pair for each such prime; different primes give different pairs, and the other pairs have nonnegative weight. Using \((\log p)\phi(p/X)\le\|\phi\|_\infty\log X\) and (3.4),
\[
\begin{aligned}
&\sum_{a\in A_0,\,d\in D_0}W(a-d)\\
&\quad \ge\frac{(1-o(1))\,UX\int\phi}{\|\phi\|_\infty\log X}.
\end{aligned}
\]
\(\square\)

This is the only place in the course where coverage is used for all large primes at once, and it cannot be replaced by a density statement: the weight \(W\) may concentrate on a sparse set of primes, and every one of them must be represented.

## 5. Proof of the supply theorem

Put \(z=X/(m_Am_D)=R^2/(m_Am_D)\). By (3.3) of Lesson 10, \(z\ge e^{-o(L)}\). Comparing (4.2) with Proposition 4.2 of Lesson 10, cancelling the positive factor \(U\), and using \(\log X=e^L\),
\[
c_\phi\,z\,e^{-L}\le e^{-1.6H+o(L)}\sqrt z .
\]
Since \(H\ge0.68L\) and \(1.6\cdot0.68=1.088\),
\[
\sqrt z\le\exp\bigl(-0.088L+o(L)\bigr),
\]
which contradicts \(z\ge e^{-o(L)}\). So (1.1) of Lesson 10 cannot fail along an unbounded sequence of \(L\), and Theorem 1.1 of Lesson 10 is proved. \(\square\)

The numbers are tight in a useful way. The contraction \(1-1.6/p\) per prime of \(\mathcal S\) comes from \(2t_0=1.7\) in Lemma 4.1 of Lesson 10, slightly reduced; the loss \(e^{-L}=1/\log X\) is the density of primes. A contradiction needs \(1.6H>L\) up to \(o(L)\), and the hypothesis that (1.1) fails gives \(H\ge0.68L\), so that \(1.6H\ge1.088L\).

## 6. Exercises

**6.1.** Let \(\phi\) be smooth and supported in \([\frac12,1]\). Show that \(\Phi(s)=\int_0^\infty\phi(t)t^{s-1}dt\) satisfies \(|\Phi(\sigma+it)|\le C_j(\phi)(1+|t|)^{-j}\) for \(-\frac12\le\sigma\le2\).

**6.2.** Show that every primitive character induced by a monomial of the expansion (3.2) has conductor at most \(Q_b\), and that it is real only if each of its local components is quadratic.

**6.3.** In Proposition 4.1, why can the pairs \((a,d)\) with \(a\le R+N_*\) not simply be kept, with \(A_0\) replaced by all of \(A\cap[0,X]\)?

**6.4.** Show that the sum \(\sum_{n\le X,\ n=p^k,\ k\ge2}\Lambda(n)\) is \(O(X^{1/2}(\log X)^2)\).

## 7. Solutions

**6.1.** Integrating by parts \(j\) times, \(\Phi(s)=\frac{(-1)^j}{s(s+1)\cdots(s+j-1)}\int_0^\infty\phi^{(j)}(t)\)\(t^{s+j-1}dt\), with no boundary terms because \(\phi\) has compact support in \((0,\infty)\). For \(|t|\ge1\) the denominator has modulus at least \(|t|^j\), and the integral is bounded on the strip; for \(|t|\le1\) use \(j=0\).

**6.2.** The conductor is the product of the primes \(p\in I\cup J\) at which the local component is nonprincipal, so it is at most \(\prod_{p\in I\cup J}p\le Q_b\), since \(|I\cup J|\le2K\) and each \(p\le\exp(e^{0.9L})\). A character of a product of distinct primes is real exactly when each local component takes real values, that is, is the quadratic or the principal character.

**6.3.** The pair average must be compared with Proposition 4.2 of Lesson 10, whose proof uses the residue supports: the reductions of \(A_0\) lie in \(S_p\) for all \(p\le R\), which requires \(a>p+N_*\). Small elements of \(A\) need not lie in \(S_p\). Their pairs cover only \(X^{3/4+o(1)}\) primes, which is negligible.

**6.4.** A prime power \(p^k\le X\) with \(k\ge2\) has \(p\le X^{1/2}\) and \(k\le\log X/\log2\). So the sum is at most \(\sum_{p\le X^{1/2}}\log p\cdot\frac{\log X}{\log 2}\)\(\ll X^{1/2}\log X\cdot\log X\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 5: the prime mean of the weight, Lemma 5.3, the exceptional deletion, (5.15)–(5.21), and using coverage of every sufficiently large prime. At the density step the paper cites Montgomery's zero-density theorem; Lemma 2.1 uses the log-free density estimate of the Linnik lesson, which suffices. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
