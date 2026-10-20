# Scales, cells and a positive statistic for higher characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lessons 3–6 showed that translated quadratic characters do not bias the residue supports \(S_p\). This lesson and the next two prove the same for multiplicative characters of every order greater than \(2\), with the character also allowed to vary from prime to prime (Theorem 1.1). Lesson 9 combines both results into the *mixed flatness* of the normalized Fourier transforms of the supports, the form used in the rest of the course.

The quadratic proof does not extend: there is no large sieve for characters of higher order strong enough to classify kernels. The argument here is a sequence of Cauchy–Schwarz *transfers* that copy the prime variables in a binary tree, together with *anchor* primes whose characters distinguish the copies. This lesson prepares the transfers. It chooses the scales, finds a rich block of primes by a density increment, selects good cells of primes for every role, realizes prescribed logarithmic sizes exactly by Kneser's addition theorem, and builds a positive statistic whose Poisson dual is a lower bound \(|\eta_0|\ge e^{-B_0m}\) for an amplitude (Proposition 6.1). Kneser's theorem is proved in full in Section 3.

**Prerequisites.** [*Square-root bounds and collision stability*](square-root-bounds-and-collision-stability.md), Sections 4 and 5; [*A biased block and an amplified moment*](a-biased-block-and-an-amplified-moment.md), Section 3 (the weight \(\psi\)); [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1; [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09), Theorem 3.1.

## 1. The statement and the contradiction hypothesis

In this lesson and the next two, the *harmonic mass* of a set \(\mathcal Q\) of primes is \(\sum_{p\in\mathcal Q}1/p\). Multiplicative characters are extended by zero at zero, and \(\operatorname{ord}(\lambda)\) is the order of a character \(\lambda\) of \(\mathbb F_p^\times\).

**Theorem 1.1** (higher characters [OpenAI-013, Proposition 4.1]). For fixed \(0<\alpha<\beta\), as \(L\to\infty\),
\[
\begin{aligned}
&\sum_{\alpha L\le\log\log p\le\beta L}\frac1p\\
&\qquad\max_{\substack{t\in\mathbb F_p\\\operatorname{ord}(\lambda)>2}}\Bigl|\mathbb E_{x\in S_p}\lambda(x-t)\Bigr|\\
&\quad=o(L).\quad(1.1)
\end{aligned}
\]

The proof occupies this lesson and Lessons 8–9. Suppose (1.1) fails. Passing to a sequence \(L\to\infty\), there are constants \(c,\delta>0\), sets \(\mathcal E\) of primes in the band \(\alpha L\le\log\log p\le\beta L\) with harmonic mass at least \(cL\), and functions
\[
\begin{gathered}
f_p(x)=z_p\,\chi^{(p)}(x-t_p),\\
|z_p|=1,\\
\operatorname{ord}(\chi^{(p)})>2,\\
\operatorname{Re}\mathbb E_{x\in S_p}f_p(x)\ge\delta\\
(p\in\mathcal E).
\end{gathered}
\]
(Rotate the maximizing mean by a unit \(z_p\) to make it real and positive.) All constants below may depend on \(\alpha,\beta,c,\delta\). When labels are sampled from a specified set of primes, their prior is the harmonic measure on that set, normalized to a probability. Restrictions on a tuple of labels, such as distinctness or a size window, are imposed by indicators and do not renormalize the prior.

Throughout, \(u=\log\log p\) is the *level* of a prime \(p\). By Mertens' estimate \(\sum_{p\le x}1/p\)\(=\log\log x+M+O(1/\log x)\), the harmonic mass of the primes with level in an interval \([u_1,u_2]\) is \(u_2-u_1+o(1)\), uniformly for \(u_1\ge\alpha L\).

## 2. Selection of scales

Set \(\epsilon=10^{-4}\). A large constant \(B_D\) is chosen first, then a large lower bound \(K_0\) for an integer depth \(k\). The constants multiplying \(m\) in the estimates below are independent of \(B_D\) and \(k\), except for the explicitly displayed multiples of \(\log z\). The notation \(O_k(1)\) and \(o_k(m)\) allows dependence on these fixed choices; its limit variable is \(L\).

**Three separated intervals.** Partition the band \([\alpha L,\beta L]\) of levels into \(q\) equal intervals, \(q\) a large fixed integer. The intervals with \(\mathcal E\)-mass below \(cL/(2q)\) carry less than \(cL/2\) in total, and each of the others has mass at most \((\beta-\alpha)L/q+o(1)\). So at least \(cq/(3(\beta-\alpha))\) intervals have mass at least \(cL/(2q)\), and for large \(q\) there are at least five of them. Choose three of these, with at least one partition interval between successive choices. Their lengths and the gaps between them are fixed positive multiples of \(L\).

- All \(\mathcal E\)-primes of the *middle* interval are the *bulk labels*.
- The *lower* interval has length \(\asymp L\) and mass \(\gg L\), so it contains a unit interval of levels whose \(\mathcal E\)-mass is bounded below by a positive constant. Fix one such *shell* for the *small anchors*.

**A uniformly rich block.** In the *upper* interval we need more structure.

**Lemma 2.1** (density increment). There are a constant \(c_1>0\), independent of \(K_0\), and an integer \(k\ge K_0\) bounded independently of \(L\), together with a block \([U,U+5k]\) of levels inside the upper interval, such that every subinterval of length \(\epsilon k\) of the block has \(\mathcal E\)-mass at least \(c_1\epsilon k\).

*Proof.* Choose an integer \(M_d>100/\epsilon\). The *density* of a block is its \(\mathcal E\)-mass divided by its length; by Mertens' estimate it is at most \(1+o(1)\) for blocks of length at least \(1\). The upper interval has density at least some fixed \(d_0>0\), so, averaging over a partition into blocks of length \(5K_0M_d^{h}\), one of them has density at least \(d=d_0/2\); here \(h\) is a fixed integer chosen below. Put \(c_1=d/5\).

Let the current block have length \(5\kappa\) and density at least \(d\), and suppose it contains a subinterval \(I_f\) of length \(\epsilon\kappa\) with mass less than \(c_1\epsilon\kappa\). Split the block into \(M_d\) children of length \(5\kappa/M_d<\epsilon\kappa/20\). The children contained in \(I_f\) have total length \(\ell\ge\epsilon\kappa-10\kappa/M_d\ge\epsilon\kappa/2\) and total mass less than \(c_1\epsilon\kappa\le2c_1\ell<\frac d2\ell\). So the other children have total length \(5\kappa-\ell\) and total mass more than \(5\kappa d-\frac d2\ell\), and one of them has density at least
\[
\begin{aligned}
\frac{5\kappa d-\frac d2\ell}{5\kappa-\ell}&=d+\frac{d\ell/2}{5\kappa-\ell}\\
&\ge d\Bigl(1+\frac\epsilon{20}\Bigr).
\end{aligned}
\]
Make it the current block. The density cannot exceed \(1+o(1)\), so this step occurs at most \(h_0=\lceil\log(2/d)/\log(1+\epsilon/20)\rceil\) times; take \(h=h_0\). The process therefore stops at a block of length \(5k\) with \(k\in\{K_0,K_0M_d,\dots,K_0M_d^{h}\}\), all of whose subintervals of length \(\epsilon k\) have mass at least \(c_1\epsilon k\). Neither \(h\) nor \(c_1\) depends on \(K_0\). \(\square\)

Since \(k\) takes finitely many values, pass to a subsequence of \(L\) on which \(k\) is fixed.

**Rich shells.** Increase \(K_0\) so that \(2(1+o(1))<\frac12c_1\epsilon k\). The grid \(U+\mathbb Z\) cuts the block into unit shells. Every interval of length \(\epsilon k\) in the block contains at least \(\epsilon k-2\) whole grid shells, of total mass at least \(c_1\epsilon k-2(1+o(1))\ge\frac12c_1\epsilon k\), so one of them has mass at least \(c_0=c_1/2\). Call grid shells of mass at least \(c_0\) *rich*. Fix one rich shell inside \([U,U+2\epsilon k]\): it supplies the *top* labels and the *big anchors*. Let \(\tau=e^{u_0}\), where \(u_0\) is its lower endpoint, so that its primes satisfy \(\tau\le\log p<e\tau\). Set
\[
\begin{gathered}
\log X=10^3\cdot4^k\,\tau,\\
z=\exp(3\epsilon k),\\
m=\lfloor zL\rfloor .\quad(2.1)
\end{gathered}
\]

**Typical endpoints.** The *tested sets* are: the bulk labels, the small-anchor shell, the top shell, and all rich grid shells of the block whose primes satisfy \(\log p<(\log X)/4\). Their number is bounded for fixed \(k\), and each has harmonic mass bounded below. Let \(\mathcal A_X=A\cap[X^{9/10},X]\).

**Lemma 2.2.** All but \(o(|\mathcal A_X|)\) elements \(a\in\mathcal A_X\) satisfy \(\operatorname{Re}\mathbb E_{p\in\mathcal T}f_p(a)\ge\delta/2\) for every tested set \(\mathcal T\), the expectation being over the harmonic prior of \(\mathcal T\).

*Proof.* Let \(\mathcal A'\subseteq\mathcal A_X\) have at least \(\sqrt X/(\log X)^{10}\) elements. Its uniform measure has point masses at most \((\log X)^{10}/\sqrt X\), so Lemma 4.1 and Corollary 4.2 of Lesson 2 apply with \(b=10\), and every tested prime lies below their cutoff \(\sqrt X/(\log X)^{11}\). Since \(|f_p|\le1\) and \(\log p\ge e^{\alpha L}\) for tested primes,
\[
\begin{aligned}
&\sum_{\text{tested }p}\frac1p\Bigl|\mathbb E_{a\in\mathcal A'}f_p(a)\\
&\qquad -\mathbb E_{x\in S_p}f_p(x)\Bigr|^2\\
&\quad \le e^{-\alpha L}\sum_{p}\frac{\log p}p|\cdot|^2\\
&\quad \ll e^{-\alpha L}\log\log X=o(1),
\end{aligned}
\]
because \(\log\log X=O(L)\). If the set \(\mathcal A'\) of elements failing the conclusion for a given \(\mathcal T\) had at least \(\sqrt X/(\log X)^{10}\) elements, then \(\mathbb E_{p\in\mathcal T}\operatorname{Re}\mathbb E_{a\in\mathcal A'}f_p(a)<\delta/2\), while \(\operatorname{Re}\mathbb E_{S_p}f_p\ge\delta\) for all \(p\in\mathcal T\subseteq\mathcal E\). Cauchy–Schwarz over the harmonic prior of \(\mathcal T\) would then give \((\delta/2)^2\le o(1)/\mathrm{mass}(\mathcal T)\), which is false for large \(L\). There are boundedly many tested sets, and \(|\mathcal A_X|\gg\sqrt X/(\log X)^3\) by Lemma 5.1 of Lesson 2. \(\square\)

Call the elements of Lemma 2.2 *typical endpoints*.

**Good cells.** For a rich shell whose primes satisfy \(b\le\log p<eb\), partition its \(\mathcal E\)-primes into the *cells*
\[
\begin{gathered}
\mathcal E_h=\{p\in\mathcal E:h\le\log p<h+1\},\\
h\in\mathbb Z\cap[b,eb].
\end{gathered}
\]
Each cell has harmonic mass at most \(C/b\), by the prime number theorem.

**Lemma 2.3.** At a typical endpoint \(a\), every tested rich shell with parameter \(b\) has at least \(c'b\) *good* cells, those with
\[
\sum_{p\in\mathcal E_h}\frac1p\ge\frac{c''}b,
\qquad
\operatorname{Re}\mathbb E_{p\in\mathcal E_h}f_p(a)\ge\frac\delta4,
\]
where \(c',c''>0\) are uniform over all tested shells.

*Proof.* Let \(m_h\) be the mass of \(\mathcal E_h\), \(r_h=\operatorname{Re}\mathbb E_{\mathcal E_h}f_p(a)\in[-1,1]\), and \(M=\sum_hm_h\ge c_0\). By Lemma 2.2, \(\sum_hm_hr_h\ge\frac\delta2M\), so \(\sum_{r_h\ge\delta/4}m_h\ge\sum_hm_hr_h-\frac\delta4M\ge\frac\delta4M\). The cells with \(m_h<c''/b\) have total mass at most \(2c''\), which is at most \(\frac\delta8M\) if \(c''=\delta c_0/16\). The remaining cells with \(r_h\ge\delta/4\) carry mass at least \(\frac\delta8M\), and each has mass at most \(C/b\); so there are at least \(\delta c_0b/(8C)\) of them. \(\square\)

**Words and a bin.** A *word* consists of \(m\) independent bulk labels and one independent top label. For an integer \(J\) put
\[
\begin{aligned}
G_J(n)&=\mathbb E_{\text{word}}\Bigl[\mathbf 1\Bigl\{\Bigl\lfloor\sum_{p\in\text{word}}\log p\Bigr\rfloor\\
&=J\Bigr\}\prod_{p\in\text{word}}f_p(n)\Bigr].
\end{aligned}
\]
Every bulk prime has level at most that of the middle interval, which is separated from the top shell by \(\gg L\) levels; so the bulk part of a word has \(\sum\log p\le me^{-c_2L}\tau=o(\tau)\), and every nonempty bin satisfies \((1-o(1))\tau\le J\le4\tau\). There are at most \(e^{CL}\) bins. At a typical endpoint, independence gives \(|\sum_JG_J(a)|\)\(=|\mathbb E_{\text{bulk}}f_p(a)|^m\,|\mathbb E_{\text{top}}f_p(a)|\)\(\ge(\delta/2)^{m+1}\). Pigeonholing first a bin for each typical endpoint and then the endpoints among the bins gives a fixed \(J\) such that
\[
\begin{gathered}
|G_J(a)|\ge e^{-Cm}\\
\begin{aligned}
&\text{for at least }\sqrt Xe^{-Cm}\\
&\quad \text{ typical endpoints }a.
\end{aligned}\quad(2.2)
\end{gathered}
\]
The constant \(C\) is independent of large \(k\): the bin count and the logarithmic loss in \(|\mathcal A_X|\) have logarithms \(O(L)+O_k(1)\), and \(L\le m\).

## 3. Kneser's addition theorem

Let \(G\) be an abelian group. For \(A,B\subseteq G\), \(A+B=\{a+b\}\), and the *stabilizer* of a set \(C\) is the subgroup \(\operatorname{St}(C)=\{g\in G:C+g=C\}\). Note \(\operatorname{St}(B)\subseteq\operatorname{St}(A+B)\).

**Theorem 3.1** (Kneser's addition theorem, with the proof of DeVos [DeV, Theorem 1]). If \(A,B\subseteq G\) are finite and nonempty and \(K=\operatorname{St}(A+B)\), then
\[
|A+B|\ge|A+K|+|B+K|-|K|.
\]

*Proof.* Induct on \(|A+B|+|A|\).

*Reduction to a trivial stabilizer.* Suppose \(K\ne\{0\}\) and let \(\phi\colon G\to G/K\) be the quotient map. If \(\phi(g)\) stabilizes \(\phi(A)+\phi(B)\), then \(g+A+B\subseteq A+B+K=A+B\), so \(g\in K\); thus \(\phi(A)+\phi(B)\) has trivial stabilizer. Since \(|\phi(A+B)|=|A+B|/|K|<|A+B|\) and \(|\phi(A)|\le|A|\), induction gives \(|\phi(A)+\phi(B)|\ge|\phi(A)|+|\phi(B)|-1\), and multiplying by \(|K|\) gives the claim, because \(A+B\), \(A+K\), \(B+K\) are unions of \(K\)-cosets.

So assume \(K=\{0\}\); we must show \(|A+B|\ge|A|+|B|-1\). If \(|A|=1\) this is clear. Otherwise choose \(a\ne a'\) in \(A\). Since \(a'-a\notin\operatorname{St}(B)\subseteq K\), there is \(b\in B\) with \(b+a'-a\notin B\). Replacing \(B\) by its translate \(B-b+a\) changes nothing, and afterwards \(a\in A\cap B\) and \(a'\in A\setminus B\). So \(\emptyset\ne A\cap B\ne A\).

*Convergents.* Call \(C\subseteq A+B\), with \(H=\operatorname{St}(C)\), a *convergent* if
\[
|C|+|H|\ge|A\cap B|+|(A\cup B)+H|.
\]
The set \(C_0=(A\cap B)+(A\cup B)\) lies in \(A+B\). Since \(|C_0|\le|A+B|\) and \(|A\cap B|<|A|\), the induction hypothesis applies to \(A\cap B\) and \(A\cup B\), and with \(H_0=\operatorname{St}(C_0)\) it gives \(|C_0|\ge|(A\cap B)+H_0|\)\(+|(A\cup B)+H_0|-|H_0|\ge|A\)\(\cap B|+|(A\cup B)+H_0|-|H_0|\). So \(C_0\) is a convergent. Choose a convergent \(C\) whose stabilizer \(H\) has the least possible order. If \(H=\{0\}\), then \(|A+B|\ge|C|\)\(\ge|A\cap B|+|A\cup B|-1\)\(=|A|+|B|-1\), as required. Suppose, for a contradiction, that \(H\ne\{0\}\).

*A coset outside the sumset.* A convergent is nonempty, since \(|C|\ge|A\cap B|\ge1\). If \(a+b+H\subseteq A+B\) for all \(a\in A\), \(b\in B\), then \(H\subseteq\operatorname{St}(A+B)=\{0\}\). So choose \(a\in A\), \(b\in B\) with \(a+b+H\not\subseteq A+B\). Since \(C\subseteq A+B\) is a union of \(H\)-cosets, \(C\) is disjoint from \(a+b+H\). Put
\[
\begin{gathered}
A_1=A\cap(a+H),\\
A_2=A\cap(b+H),\\
B_1=B\cap(b+H),\\
B_2=B\cap(a+H),
\end{gathered}
\]
so \(a\in A_1\) and \(b\in B_1\). For \(i=1,2\) with \(A_i,B_i\ne\emptyset\), the set \(A_i+B_i\) lies in the coset \(a+b+H\), is a proper subset of it, and is contained in \(A+B\). Let \(H_i=\operatorname{St}(A_i+B_i)\) and \(C_i=C\sqcup(A_i+B_i)\). Then \(H_i\) is a proper subgroup of \(H\), because a proper nonempty subset of one \(H\)-coset is not \(H\)-periodic. Also \(\operatorname{St}(C_i)=H_i\): an element stabilizing \(C_i\) must map the only partially filled \(H\)-coset to itself, so it lies in \(H\) and stabilizes \(A_i+B_i\); conversely \(H_i\subseteq H\) stabilizes \(C\).

*Inequality (A).* Let \(i\) be such that \(A_i,B_i\ne\emptyset\). By the minimality of \(|H|\), \(C_i\) is not a convergent. Subtracting this from the convergent inequality for \(C\), and using \(|C_i|=|C|+|A_i+B_i|\),
\[
\begin{aligned}
&|(A\cup B)+H|-|(A\cup B)+H_i|\\
&\quad <|H|-|A_i+B_i|-|H_i|\\
&\quad \le|H|-|A_i+H_i|-|B_i\\
&\qquad +H_i|,\quad(A)
\end{aligned}
\]
where the last step is the induction hypothesis for \(A_i,B_i\), applicable since \(A_i+B_i\subsetneq A+B\) (it misses \(C\)) and \(A_i\subseteq A\).

*The case \(B_2=\emptyset\).* The set \(((A\cup B)+H_1)\cap(a+H)\) equals \((A_1\cup B_2)+H_1=A_1+H_1\), and outside \(a+H\), \((A\cup B)+H_1\subseteq(A\cup B)+H\). Since \(a+H\subseteq(A\cup B)+H\), the left side of (A) for \(i=1\) is at least \(|H|-|A_1+H_1|\), contradicting (A). Symmetrically, using the coset \(b+H\) and \(((A\cup B)+H_1)\cap(b+H)=B_1+H_1\), the case \(A_2=\emptyset\) is impossible. So (A) holds for \(i=1,2\).

*The case \(a+H=b+H\).* Then \(A_1=A_2\), \(B_1=B_2\), and the left side of (A) is at least \(|H|-|(A_1\cup B_1)+H_1|\)\(\ge|H|-|A_1+H_1|-|B_1+H_1|\), again contradicting (A). So \(a+H\ne b+H\).

*Inequality (B).* The left side of (A) is nonnegative, and every term on its right side is a multiple of \(|H_i|\), because \(H_i\le H\) and the sets are \(H_i\)-periodic. So the right side of (A) is at least \(|H_i|\):
\[
\begin{aligned}
|H|&\ge|A_i+H_i|+|B_i+H_i|\\
&\quad +|H_i|\\
&\ge|A_i|+|B_i|+|H_i|.\quad(B)
\end{aligned}
\]

*Inequality (C).* Let \(S=(a+H)\setminus(A_1\cup B_2)\) and \(T=(b+H)\setminus(A_2\cup B_1)\); they are disjoint, lie in \((A\cup B)+H\), and miss \(A\cup B\). So \(|(A\cup B)+H|\ge|A\cup B|+|S|+|T|\). The set \(A+B\) has stabilizer \(\{0\}\), of order less than \(|H|\), so it is not a convergent: \(|A+B|+1<|A\cap B|+|A\cup B|\). Using the convergent inequality for \(C\), \(|C|\le|A+B|-|A_i+B_i|\), and the induction hypothesis for \(A_i,B_i\),
\[
\begin{aligned}
|H|&\ge|(A\cup B)+H|+|A\cap B|\\
&\quad -|C|
\ge|S|+|T|+\bigl(|A\\
&\quad \cup B|+|A\cap B|-|A+B|\bigr)\\
&\quad +|A_i+B_i|
>|S|+|T|\\
&\quad +|A_i|+|B_i|-|H_i|.\quad(C)
\end{aligned}
\]

*Conclusion.* Adding (B) and (C) for \(i=1\) and \(i=2\) and halving gives
\[
\begin{aligned}
2|H|&>|A_1|+|B_2|+|S|+|A_2|\\
&\quad +|B_1|+|T|.
\end{aligned}
\]
But \(a+H=S\cup A_1\cup B_2\) and \(b+H=T\cup A_2\cup B_1\), so \(2|H|\) is at most the right side. This contradiction proves the theorem. \(\square\)

**Corollary 3.2.** Let \(U\subseteq G\) be finite and nonempty, \(r\ge1\), and \(H=\operatorname{St}(rU)\), where \(rU=U+\cdots+U\) (\(r\) terms). Then \(|rU|\ge r|U+H|-(r-1)|H|\).

*Proof.* In \(G/H\) the image \(\overline U\) satisfies \(\operatorname{St}(r\overline U)=\{0\}\), as in the first step above. For \(j<r\), \(\operatorname{St}((j+1)\overline U)\subseteq\operatorname{St}(r\overline U)\), so Theorem 3.1 gives \(|(j+1)\overline U|\ge|j\overline U|+|\overline U|-1\), and by induction \(|r\overline U|\ge r|\overline U|-(r-1)\). Multiply by \(|H|\). \(\square\)

**Corollary 3.3** (covering by bounded sumsets). Let \(G\) be a finite abelian group and \(U\subseteq G\) a generating set with \(0\in U\) and \(|U|\ge\rho|G|\). If \(r\ge2/\rho\), then \(rU=G\).

*Proof.* Let \(H=\operatorname{St}(rU)\) and suppose \(H\ne G\). Since \(U\) generates \(G\) and \(0\in U\), \(U\) is not contained in one \(H\)-coset, so \(|U+H|\ge2|H|\). By Corollary 3.2, \(|rU|\)\(\ge r|U+H|-(r-1)|U+H|/2\)\(=\frac{r+1}2|U+H|\ge\frac{r+1}2\rho|G|>|G|\), which is impossible. So \(H=G\), and the nonempty \(G\)-periodic set \(rU\) is \(G\). \(\square\)

## 4. Realizing prescribed sizes

**Lemma 4.1.** Let \(c'>0\). There are \(r_0\) and \(C_g\), depending only on \(c'\), with the following property. Let \(b\) be large and \(I\subseteq\mathbb Z\cap[b,eb]\) with \(|I|\ge c'b\). Put \(h_-=\min I\), \(h_+=\max I\), \(s=h_+-h_-\) and \(g=\gcd(I-h_-)\). Then \(s\ge c'b/2\), \(g\le C_g\), and for every integer \(n\ge2r_0\), every integer \(y\equiv nh_-\pmod g\) with
\[
nh_-+r_0s\le y\le nh_-+(n-r_0)s
\]
is the sum of an ordered list of \(n\) elements of \(I\).

*Proof.* Since \(I-h_-\subseteq g\mathbb Z\cap[0,s]\), \(c'b\le|I|\le s/g+1\), which gives both bounds. Put \(N'=s/g\) and let \(\mathcal U\subseteq\mathbb Z/N'\) be the image of \((I-h_-)/g\). It contains \(0\); it generates \(\mathbb Z/N'\), because the integers \((I-h_-)/g\) have greatest common divisor \(1\); and \(|\mathcal U|\ge|I|-1\ge\rho N'\) with \(\rho=c'/(2e)\). By Corollary 3.3, \(r_0\mathcal U=\mathbb Z/N'\) for \(r_0=\lceil2/\rho\rceil\).

Let \(y\) be as stated and \(Y=(y-nh_-)/g\in[r_0N',(n-r_0)N']\). Choose \(e_1,\dots,e_{r_0}\in(I-h_-)/g\) with \(\sum e_i\equiv Y\pmod{N'}\). Then \(0\le\sum e_i\le r_0N'\), so \(Y-\sum e_i=jN'\) with \(0\le j\le n-r_0\). Hence
\[
\begin{aligned}
y&=nh_-+g\sum_{i=1}^{r_0}e_i+j\,s\\
&\quad +(n-r_0-j)\cdot0
\end{aligned}
\]
is the sum of the \(n\) elements \(h_-+ge_i\) (\(i\le r_0\)), \(j\) copies of \(h_+\), and \(n-r_0-j\) copies of \(h_-\). \(\square\)

## 5. Gaps, targets and the selected lists

**Gaps and frequency bounds.** Define
\[
\begin{gathered}
\Delta_0=(B_D+20\log z)\,m,\\
\begin{aligned}
\Delta_j&=2^{j-1}\Delta_0\\
&\quad +4^j\sqrt m\quad(1\le j\le k),
\end{aligned}
\end{gathered}
\]
\[
\begin{gathered}
E_j=2^j\Delta_0+2\cdot4^j\sqrt m,\\
V_j=e^{E_j}\quad(0\le j\le k).\quad(5.1)
\end{gathered}
\]
Then \(E_{j-1}+\Delta_j=E_j-2\cdot4^{j-1}\sqrt m\), a margin used in Lesson 8.

**Anchors.** For each typical endpoint in (2.2) choose, for every \(j=1,\dots,k\), a good cell of the small-anchor shell and a good cell of the top shell (Lemma 2.3); the primes drawn from them are the *small anchor* and the *big anchor* of step \(j\). Let \(a_j\) be the sum of the two cell indices. Since the small-anchor shell lies far below the top shell, \(a_j\le4\tau\).

**Targets.** The transfers of Lesson 8 remove, at step \(j\), a group \(K_j\) of primes (a *pivot group*) of logarithmic size \(T_j\); a *filler* group of size \(T_F\) completes the list. At step \(j\) the part to be copied consists of \(2^{j-1}\) copies of the word, one group of each later pivot type, and the two anchors of step \(j\), and its logarithmic size must exceed \(T_j\) by \(\Delta_j\). The full list, counted in a positive and a conjugate copy, must have logarithmic size \(\log X+\Delta_0\). This forces the backward definitions
\[
\begin{gathered}
\begin{aligned}
T_j&=2^{j-1}J+\sum_{l>j}T_l+a_j\\
&\quad -\Delta_j,
\end{aligned}\\
\begin{aligned}
T_F&=\frac{\log X+\Delta_0}2-J\\
&\quad -\sum_{j=1}^k(T_j+a_j).
\end{aligned}\quad(5.2)
\end{gathered}
\]

**Lemma 5.1.** For large \(L\), all \(T_j\) and \(T_F\) are positive, and \(c_*2^k\tau\le T_j,T_F\le600\cdot4^k\tau\) with an absolute \(c_*>0\).

*Proof.* Put \(c_j=2^{j-1}J+a_j-\Delta_j\). Since \(\Delta_j=O_k(m)=O_k(L)\) and \(\tau\ge e^{\alpha L}\), \(c_j\ge2^{j-1}(1-o(1))\tau>0\). The recursion gives \(T_j=c_j+\sum_{l>j}T_l\ge c_k\)\(\ge2^{k-1}(1-o(1))\tau\), and \(\sum_jT_j=\sum_j2^{j-1}c_j\)\(\le\frac{4^k-1}3J+2^k\cdot4\tau\le2\cdot4^k\tau\), using \(J\le4\tau\). Then \(T_F\ge500\cdot4^k\tau-4\tau-2\cdot4^k\tau-4k\tau>0\), and \(T_F\le\frac12(\log X+\Delta_0)\le501\cdot4^k\tau\). \(\square\)

**Lists of cells.** Let \(T\) be one of the targets. The interval of levels \([\log T-2\epsilon k,\log T-\epsilon k]\) lies in the block \([U,U+5k]\) when \(K_0\) is large, because \(\log T-u_0\in[k\log2\)\(+\log c_*,\,k\log4+\log600]\) and \(u_0\le U+2\epsilon k\). So it contains a rich grid shell, whose primes satisfy \(\log p\le Te^{-\epsilon k}<(\log X)/4\); this shell was tested in Lemma 2.2. At each typical endpoint, apply Lemma 4.1 to its good cell indices \(I\subseteq[b,eb]\), with \(n\) the integer nearest to \(T/\frac{h_-+h_+}2\). Since \(b\in[Te^{-2\epsilon k},Te^{-\epsilon k}]\), \(c''e^{\epsilon k}\le n\le Ce^{2\epsilon k}\). The quantity \(T-nh_-\) differs from \(ns/2\) by at most \(eb\le(2e/c')s\), so it lies in \([r_0s,(n-r_0)s]\) once \(K_0\) is large. Rounding \(T\) to the class of \(nh_-\) modulo \(g\) costs \(O(1)\). So there is an ordered list of \(n\) good cell indices with sum \(T+O(1)\).

Choose such lists for every pivot target \(T_j\) and for \(T_F\). The total number \(n_c\) of cell labels, anchors included, satisfies \(n_c\le n_{\max}\ll ke^{2\epsilon k}\). Every cell index has at most \(e^{CL}\) possible values, so fixing all list lengths, all ordered lists and all anchor cells, by pigeonhole over the typical endpoints of (2.2), costs a factor at most \(\exp(Cn_{\max}L+O_k(1))\). Since \(n_{\max}/z\ll ke^{-\epsilon k}\to0\), this is \(e^{o(m)}\) uniformly, with a constant independent of \(k\) and \(B_D\). No further loss comes from the dependence of the targets on the endpoint: every rich shell that can occur was tested at every typical endpoint.

## 6. A positive statistic and the first amplitude

Let \(\psi\) be the weight of Section 3 of Lesson 3: a nonnegative even Schwartz function, bounded below on \([0,1]\), whose Fourier transform is smooth and supported in \([-\frac14,\frac14]\). For a selected cell put \(R_h(n)=\mathbb E_{p\in\mathcal E_h}f_p(n)\). The fixed endpoints give the statistic
\[
\begin{aligned}
I_*&=\sum_{n\in\mathbb Z}\psi(n/X)\,|G_J(n)|^2\\
&\quad \prod_h|R_h(n)|^2\ge\sqrt X\,e^{-Cm},\quad(6.1)
\end{aligned}
\]
where the cells occur with their selected multiplicities. Indeed, at each of the \(\sqrt Xe^{-Cm-o(m)}\) retained endpoints, \(|G_J(a)|^2\ge e^{-2Cm}\) by (2.2) and \(|R_h(a)|^2\ge(\delta/4)^2\) for every selected cell by Lemma 2.3, while \((\delta/4)^{2n_c}=e^{-o(m)}\).

**The expansion.** Expand \(|G_J(n)|^2\) and each \(|R_h(n)|^2\) using an independent positive copy and an independent conjugate copy of every role. The formal product \(M\) of all prime labels, with multiplicity, satisfies on the bins
\[
\begin{aligned}
\log M&=2\Bigl(J+\sum_{j=1}^k(T_j+a_j)\\
&\quad +T_F\Bigr)+O_k(1)\\
&=\log X+\Delta_0+O_k(1).\quad(6.2)
\end{aligned}
\]

**Repeated primes.** Consider the terms in which some prime occurs more than once. As a function of \(n\), such a term has period \(Q\), the product of its distinct primes, and \(Q\le M/p_{\min}\)\(\le Xe^{\Delta_0+O_k(1)}/\exp(e^{\alpha L})\)\(=o(X)\). Poisson summation, as in Lemma 3.1 of Lesson 3, shows that \(\sum_n\psi(n/X)F(n)=X\widehat\psi(0)\,\mathbb E_{n\bmod Q}F(n)\) for such a periodic \(F\). By the Chinese remainder theorem the mean factors over the distinct primes, and it vanishes if some prime occurs exactly once, since \(\mathbb E_xf_p(x)=0\) for a nonprincipal character. So only tuples in which every prime occurs at least twice remain, and each contributes at most \(O(X)\) before its prior weight. A prescribed ordered tuple has prior weight at most \(M^{-1}L^{-2m}\exp(Cm+O_k(1))\): the \(2m\) bulk positions each have normalization \(O(1/L)\), the \(2n_c\) cell positions cost at most \(e^{Cn_cL}=e^{o(m)}\), and the top positions a bounded factor. Extract \(M^{-1/2}\le X^{-1/2}e^{-\Delta_0/2+O_k(1)}\) using (6.2). There are \(b_*=2m+O_k(1)\) positions; if the tuple has \(d\le b_*/2\) distinct primes, the remaining factor \(M^{-1/2}\) is at most the product of \(1/p\) over the distinct primes, and summing over the assignments of positions to \(d\) distinct primes gives at most
\[
\sum_{d\le b_*/2}\frac{d^{b_*}(CL)^d}{d!}\le b_*^{b_*}e^{CL},
\]
since the union of all prime ranges has harmonic mass \(O(L)\). With \(b_*\log b_*-2m\log L=2m\log z+o_k(m)\), the repeated-prime terms total at most
\[
\begin{aligned}
&\sqrt X\exp\Bigl(-\frac{\Delta_0}2+(2\log z+C)m\\
&\qquad +o_k(m)\Bigr)\\
&\quad =\sqrt X\exp\Bigl(-\Bigl(\frac{B_D}2+8\log z\\
&\qquad -C\Bigr)m+o_k(m)\Bigr).
\end{aligned}
\]
For \(B_D\) large this is negligible against (6.1).

**Proposition 6.1** ([OpenAI-013, (4.4)]). Let \(\eta_0\) be the sum of the terms of \(I_*\) with all prime labels distinct, divided by \(\sqrt X\). If \(B_D\) is large enough, then for large \(L\)
\[
|\eta_0|\ge e^{-B_0m},
\tag{6.3}
\]
where \(B_0\) does not depend on \(B_D\) or \(k\). \(\square\)

Lesson 8 rewrites \(\eta_0\) by Poisson summation as a sum over a dual frequency, and transfers the lower bound (6.3) through \(k\) steps of Cauchy–Schwarz, each of which doubles the number of copies of the word.

## 7. Exercises

**7.1.** Show that Kneser's theorem implies the Cauchy–Davenport inequality: for nonempty \(A,B\subseteq\mathbb Z/p\) with \(p\) prime, \(|A+B|\ge\min(p,|A|+|B|-1)\).

**7.2.** In \(G=\mathbb Z/10\), let \(U=\{0,2,4,6,8,5\}\). Compute \(2U\) and its stabilizer, and verify Corollary 3.2 for \(r=2\).

**7.3.** Show that the hypothesis "\(U\) generates \(G\)" cannot be dropped from Corollary 3.3, and that the bound \(r\ge2/\rho\) cannot be replaced by \(r\ge c/\rho\) with \(c<1\).

**7.4.** In Lemma 4.1, let \(I=\{b,b+2,b+4,\dots\}\cap[b,eb]\). Compute \(g\), and describe which integers are sums of \(n\) elements of \(I\).

## 8. Solutions

**7.1.** The stabilizer \(K\) of \(A+B\) is a subgroup of \(\mathbb Z/p\), so \(K=\{0\}\) or \(K=\mathbb Z/p\). In the second case \(A+B=\mathbb Z/p\). In the first, Kneser gives \(|A+B|\ge|A|+|B|-1\).

**7.2.** \(U+U\) contains all even residues (sums of two even elements), and \(5+\{0,2,4,6,8\}\) gives all odd residues; so \(2U=\mathbb Z/10\), with stabilizer \(H=\mathbb Z/10\). Then \(U+H=\mathbb Z/10\) and the bound reads \(10\ge2\cdot10-10=10\).

**7.3.** If \(U\) lies in a proper subgroup \(H\), so does every \(rU\). For the second point, take \(U=\{0,1,\dots,t-1\}\subseteq\mathbb Z/N\) with \(t=\lceil\rho N\rceil\): then \(rU=\{0,\dots,r(t-1)\}\), which is all of \(\mathbb Z/N\) only if \(r(t-1)\ge N-1\), that is \(r\gtrsim1/\rho\). So \(r\) must be at least about \(1/\rho\), and no bound \(c/\rho\) with \(c<1\) suffices for large \(N\).

**7.4.** All elements of \(I\) have the parity of \(b\), and differences \(2\) occur, so \(g=2\). A sum of \(n\) elements of \(I\) is congruent to \(nb\pmod2\), lies between \(nb\) and \(nh_+\), and every such integer with the right parity occurs, since increasing one summand by \(2\) increases the sum by \(2\). Lemma 4.1 asserts this for the middle range only, with \(r_0\) depending on the density.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 4: Proposition 4.1, selection of scales and positive statistics, (4.2)–(4.4). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [DeV] M. DeVos, *A short proof of Kneser's addition theorem for abelian groups*, in *Combinatorial and Additive Number Theory*, Springer (2014), numbering of arXiv:1303.3539v1: Theorem 1, a short proof of the theorem of M. Kneser (Math. Z. 58, 1953). https://arxiv.org/abs/1303.3539v1
