# Square-root bounds and collision stability

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Under the standing assumption of Lesson 1, every large prime is a sum \(a+b\) with \(a\in A\), \(b\in B\), so \(A(Y)B(Y)\gg Y/\log Y\). This lesson proves the matching upper bounds: both counting functions lie within powers of \(\log Y\) of \(\sqrt Y\) (Theorem 3.1, due to Elsholtz). Two sieves are played against each other. The large sieve says that a set avoiding many residue classes is small; the *larger sieve*, which counts congruent pairs, says that a set occupying few residue classes is small. Exclusion makes the large elements of \(A\) avoid the classes occupied by \(-B\), so the two sieves bound each other.

The same congruent-pair count gives the main tool of the course, *collision stability* (Lemma 4.1). On a weighted average over primes, the reductions modulo \(p\) of the large elements of \(A\) are nearly uniform on the support \(S_p\) of Lesson 1, those of \(D=-B\) are nearly uniform on \(S_p^c\), and \(|S_p|\) is close to \(p/2\).

**Prerequisites.** [*The inverse Goldbach problem*](the-inverse-goldbach-problem.md), Sections 2, 5 and 6; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 2.1 and 3.1; [*The prime number theorem*](course:NT-ZETA/NT-ZETA-09), Theorem 3.1.

## 1. Conventions on finite fields

Write \(e(x)=e^{2\pi ix}\) and \(e_m(x)=e(x/m)\). An expectation over a finite set is its uniform average unless another probability measure is named. For a function \(f\) on \(\mathbb F_p\) the Fourier transform is
\[
\begin{gathered}
\widehat f(a)=\frac1p\sum_{x\in\mathbb F_p}f(x)\,e_p(-ax),\\
f(x)=\sum_{a\in\mathbb F_p}\widehat f(a)\,e_p(ax),
\end{gathered}
\]
and Parseval's identity reads \(\mathbb E_x|f(x)|^2=\sum_a|\widehat f(a)|^2\). Norms of functions on \(\mathbb F_p\) use the probability measure unless stated otherwise. For the mass function \(\mu\) of a probability measure on \(\mathbb F_p\), however, the *counting norm*
\[
\|\mu\|_2^2=\sum_{x\in\mathbb F_p}\mu(x)^2
\]
is used; it is the probability that two independent samples of \(\mu\) coincide. For a nonempty finite set \(E\), \(U_E\) denotes the uniform probability measure on \(E\). For a probability measure \(\mu\) on \(\mathbb Z\), \(\mu_p\) denotes its image modulo \(p\).

**Lemma 1.1** (energy of a measure avoiding classes). Let \(\mu\) be a probability measure on \(\mathbb F_p\) supported on a set of \(p-\nu\) residues, with \(0\le\nu<p\). Then
\[
\sum_{h\in\mathbb F_p^\times}\Bigl|\sum_{x}\mu(x)\,e_p(hx)\Bigr|^2\ge\frac{\nu}{p-\nu}.
\]

*Proof.* Expanding the square and summing over all \(h\in\mathbb F_p\) gives \(p\sum_x\mu(x)^2\), by orthogonality. By Cauchy–Schwarz on the support, \(1=(\sum_x\mu(x))^2\le(p-\nu)\sum_x\mu(x)^2\). So the sum over all \(h\) is at least \(p/(p-\nu)\); the term \(h=0\) equals \(1\), and \(p/(p-\nu)-1=\nu/(p-\nu)\). \(\square\)

## 2. Counting congruent pairs

The following count is the larger sieve of Gallagher in the form used by Green and Harper [GH]. Let \(\mu\) be a probability measure on integers in an interval of length at most \(X\), and let \(n,n'\) be independent samples of \(\mu\). For a prime \(p\), \(\|\mu_p\|_2^2=\Pr(n\equiv n'\pmod p)\). For any set \(\mathcal P\) of primes at most \(Q\),
\[
\begin{aligned}
&\sum_{p\in\mathcal P}(\log p)\,\|\mu_p\|_2^2\\
&\quad =\mathbb E\sum_{\substack{p\in\mathcal P\\p\mid n-n'}}\log p
\le\log X\\
&\qquad +\Pr(n=n')\\
&\qquad \sum_{p\le Q}\log p.\quad(2.1)
\end{aligned}
\]
Indeed, if \(n\ne n'\) the primes dividing \(n-n'\) have product at most \(|n-n'|\le X\); if \(n=n'\), every prime divides \(0\). Chebyshev's bound \(\sum_{p\le Q}\log p\ll Q\) ([*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 2.1) and \(\Pr(n=n')=\sum_n\mu(n)^2\le\max_n\mu(n)\) give
\[
\begin{aligned}
&\sum_{p\in\mathcal P}(\log p)\,\|\mu_p\|_2^2\\
&\quad \le\log X+O\bigl(Q\max_n\mu(n)\bigr).\quad(2.2)
\end{aligned}
\]
If \(\mu_p\) is supported on \(\nu\) residues, Cauchy–Schwarz gives \(\|\mu_p\|_2^2\ge1/\nu\). So a measure occupying few classes modulo many primes has a large left side in (2.2), and (2.2) bounds it.

## 3. Square-root bounds

**Theorem 3.1** (Elsholtz [Els06, Theorem 1.9]; [OpenAI-013, Lemma 2.4]). Under the standing assumption, for \(Y\ge3\),
\[
\begin{aligned}
\frac{\sqrt Y}{(\log Y)^3}&\ll A(Y),\,B(Y)\\
&\ll\sqrt Y(\log Y)^2.\quad(3.1)
\end{aligned}
\]

*Proof.* *Step 1: the product bound and polylogarithmic bounds.* Every prime \(p\in(N,Y]\) is \(a+b\) with \(a\in A\cap[0,Y]\) and \(b\in B\cap[0,Y]\), so Chebyshev's lower bound gives
\[
\begin{aligned}
&A(Y)\,B(Y)\ge\pi(Y)-\pi(N)\\
&\quad \gg\frac{Y}{\log Y}.\quad(3.2)
\end{aligned}
\]
By Exercise 8.2 of Lesson 1, for every fixed \(j\ge1\),
\[
\begin{gathered}
A(Y),B(Y)\ll_j\frac{Y}{(\log Y)^j},\\
A(Y),B(Y)\gg_j(\log Y)^{j}.\quad(3.3)
\end{gathered}
\]

*Step 2: a large-sieve lower bound for a collision sum.* Let \(x\) be large, put \(m=A(x)\), and suppose \(m\ge3\sqrt x\). The set \(U=A\cap(\sqrt x+N_*,x]\) has at least \(m-\sqrt x-N_*-1\ge m/2\) elements. For a prime \(p\) let \(\nu_p\) be the number of residue classes modulo \(p\) that meet \(B\).

Let \(p\in(\sqrt x/2,\sqrt x]\). *The set \(U\) avoids the \(\nu_p\) classes of \(-B\) modulo \(p\).* If \(a\equiv-b\pmod p\) with \(a\in U\) and \(b\in B\), then \(a+b\in A+B\) is divisible by \(p\) and \(a+b\ge a>\sqrt x+N_*>\max(p,N)\); by exclusion \(a+b\) is a prime divisible by \(p\) and larger than \(p\), which is impossible. Since \(U\) is nonempty, \(\nu_p<p\), and Lemma 1.1 applied to the image of \(U_U\) modulo \(p\) gives
\[
\sum_{h\in\mathbb F_p^\times}\Bigl|\mathbb E_{a\in U}e_p(ha)\Bigr|^2\ge\frac{\nu_p}{p-\nu_p}\ge\frac{\nu_p}p.
\]
Apply the large sieve (2.1) of Lesson 1 with \(Q=\sqrt x\) and \(a_n=\mathbf 1_U(n)/|U|\), supported on at most \(x+1\) consecutive integers, so that \(\sum|a_n|^2=1/|U|\). Retaining only the prime moduli in \((\sqrt x/2,\sqrt x]\),
\[
\sum_{\sqrt x/2<p\le\sqrt x}\frac{\nu_p}p\le\frac{2x}{|U|}\le\frac{4x}m.
\]
Let \(\mathcal P_x\) be the set of primes in \((\sqrt x/2,\sqrt x]\); by the prime number theorem \(|\mathcal P_x|\gg\sqrt x/\log x\). By Cauchy–Schwarz, \(|\mathcal P_x|^2\le\bigl(\sum_{p}\nu_p/p\bigr)\bigl(\sum_pp/\nu_p\bigr)\), with both sums over \(\mathcal P_x\). Hence \(\sum_{p\in\mathcal P_x}p/\nu_p\gg m/(\log x)^2\), and since \(p\le\sqrt x\) and \(\log p\ge\log(\sqrt x/2)\gg\log x\) on \(\mathcal P_x\),
\[
\begin{aligned}
H&:=\sum_{p\in\mathcal P_x}\frac{\log p}{\nu_p}\\
&\gg\frac{\log x}{\sqrt x}\sum_{p\in\mathcal P_x}\frac p{\nu_p}\\
&\gg\frac{m}{\sqrt x\,\log x}.\quad(3.4)
\end{aligned}
\]

*Step 3: a larger-sieve upper bound for the same sum.* Let \(Y\ge2\) with \(B(Y)\ge1\), and let \(\mu\) be the uniform measure on \(B\cap[0,Y]\). Its image modulo \(p\) occupies at most \(\nu_p\) classes, so \(\|\mu_p\|_2^2\ge1/\nu_p\). By (2.1) with \(\mathcal P=\mathcal P_x\), Chebyshev's bound \(\sum_{p\le\sqrt x}\log p\ll\sqrt x\), and \(\Pr(n=n')=1/B(Y)\),
\[
H\le\log Y+O\left(\frac{\sqrt x}{B(Y)}\right).
\tag{3.5}
\]

*Step 4: exponents.* Let \(\varepsilon>0\) and suppose that \(A(x)>x^{1/2+\varepsilon}\) for arbitrarily large \(x\). For such \(x\) the hypothesis \(m\ge3\sqrt x\) of Step 2 holds. Choose \(Y\) with \(\log Y=x^{\varepsilon/2}\). Then (3.4) gives \(H\gg x^{\varepsilon}/\log x\), which exceeds \(2\log Y\) for large \(x\), so (3.5) forces \(\sqrt x/B(Y)\gg H\gg x^{\varepsilon}/\log x\), that is,
\[
B(Y)\ll x^{1/2-\varepsilon}\log x.
\]
But (3.3) with an integer \(j>1/\varepsilon\) gives \(B(Y)\gg_j(\log Y)^j=x^{j\varepsilon/2}>x^{1/2}\) for large \(x\). This contradiction shows \(A(x)\le x^{1/2+\varepsilon}\) for all large \(x\). The argument is symmetric in \(A\) and \(B\): exclusion makes the large elements of \(B\) avoid the classes of \(-A\). So \(B(x)\le x^{1/2+\varepsilon}\) as well, and (3.2) gives the lower bounds \(A(x),B(x)\ge x^{1/2-\varepsilon}\) for large \(x\). Thus
\[
\begin{gathered}
A(x)=x^{1/2+o(1)},\\
B(x)=x^{1/2+o(1)}.\quad(3.6)
\end{gathered}
\]

*Step 5: the logarithmic bounds.* Take \(Y=x^2\) in (3.5). By (3.6), \(B(x^2)=x^{1+o(1)}\), so \(\sqrt x/B(x^2)=o(1)\) and \(H\le2\log x+o(1)\). If \(m=A(x)\ge3\sqrt x\), (3.4) gives \(m/(\sqrt x\log x)\ll\log x\), that is \(A(x)\ll\sqrt x(\log x)^2\); if \(m<3\sqrt x\) this bound is immediate. The same holds for \(B\). Finally (3.2) gives
\[
\begin{aligned}
A(x)&\gg\frac{x}{\log x\cdot B(x)}\\
&\gg\frac{x}{\log x\cdot\sqrt x(\log x)^2}\\
&=\frac{\sqrt x}{(\log x)^3},
\end{aligned}
\]
and the same for \(B\). \(\square\)

## 4. Collision stability

The congruent-pair count also measures how far a summand is from being uniform on its residue support. Recall from Lesson 1 the partition \(\mathbb F_p=S_p\sqcup S_p^c\) and \(\sigma_p=|S_p|/p\).

**Lemma 4.1** (collision stability [OpenAI-013, Lemma 2.5]). Let \(b\ge1\) be fixed and let \(X\) be large. Suppose that \(\mu\) and \(\nu\) are probability measures on
\[
\begin{gathered}
A\cap(\sqrt X+N_*,X]\\
\text{and}\\
D\cap[-X,-\sqrt X-N_*),
\end{gathered}
\]
respectively, with every point mass at most \((\log X)^b/\sqrt X\). Put \(Q=\sqrt X/(\log X)^{b+1}\). Then
\[
\begin{aligned}
&\sum_{p\le Q}\log p\biggl(\|\mu_p-U_{S_p}\|_2^2\\
&\qquad+\|\nu_p-U_{S_p^c}\|_2^2\\
&\qquad+\frac{\sigma_p^{-1}+(1-\sigma_p)^{-1}-4}{p}\biggr)\\
&\quad\ll_b\log\log X,\quad(4.1)
\end{aligned}
\]
and every term on the left is nonnegative.

*Proof.* *Supports.* Let \(p\le Q\). If \(a\in A\) and \(a>\sqrt X+N_*\), then \(a>p+N_*\), so \(a\bmod p\) lies in the set \(\mathcal A_p\subseteq S_p\) of Lemma 6.1 of Lesson 1. So \(\mu_p\) is supported on \(S_p\), and likewise \(\nu_p\) is supported on \(S_p^c\). For a probability measure supported on a set \(E\),
\[
\begin{aligned}
\|\mu_p-U_E\|_2^2&=\|\mu_p\|_2^2\\
&\quad -\frac2{|E|}\sum_{x\in E}\mu_p(x)\\
&\quad +\frac1{|E|}\\
&=\|\mu_p\|_2^2-\frac1{|E|}.
\end{aligned}
\]
With \(|S_p|=p\sigma_p\) and \(|S_p^c|=p(1-\sigma_p)\), the bracket in (4.1) therefore equals \(\|\mu_p\|_2^2+\|\nu_p\|_2^2-4/p\).

*Collision energies.* Both measures live on intervals of length at most \(X\), and \(Q\max_n\mu(n)\le1/\log X\). By (2.2),
\[
\begin{aligned}
&\sum_{p\le Q}(\log p)\bigl(\|\mu_p\|_2^2+\|\nu_p\|_2^2\bigr)\\
&\quad \le2\log X+O(1).
\end{aligned}
\]
Mertens' estimate gives
\[
\begin{aligned}
4\sum_{p\le Q}\frac{\log p}p&=4\log Q+O(1)\\
&=2\log X\\
&\quad -4(b+1)\log\log X\\
&\quad +O(1).
\end{aligned}
\]
Subtracting proves (4.1).

*Nonnegativity.* For \(0<\sigma<1\),
\[
\begin{aligned}
&\frac1\sigma+\frac1{1-\sigma}-4=\frac{(1-2\sigma)^2}{\sigma(1-\sigma)}\\
&\quad \ge0.\quad(4.2)
\end{aligned}
\]
\(\square\)

By (4.2) and \(\sigma(1-\sigma)\le\frac14\),
\[
\begin{aligned}
&\frac1{\sigma_p}+\frac1{1-\sigma_p}-4\\
&\quad \ge16\Bigl(\sigma_p-\frac12\Bigr)^2,\quad(4.3)
\end{aligned}
\]
and the left side is at least \(\tfrac12\) when \(\sigma_p\notin[\tfrac13,\tfrac23]\). So (4.1) bounds the \((\log p)/p\)-weight of the unbalanced primes.

**Corollary 4.2** (test functions). In the setting of Lemma 4.1, let \(f_p\colon\mathbb F_p\to\mathbb C\) be functions with \(\mathbb E_{x\in\mathbb F_p}|f_p(x)|^2\le1\), chosen separately at every prime. Then
\[
\begin{aligned}
&\sum_{p\le Q}\frac{\log p}p\Bigl|\mathbb E_{\mu}f_p\\
&\qquad -\mathbb E_{x\in S_p}f_p(x)\Bigr|^2\\
&\quad \ll_b\log\log X,\quad(4.4)
\end{aligned}
\]
where \(\mathbb E_\mu f_p=\sum_n\mu(n)f_p(n\bmod p)\), and the same holds for \(\nu\) with \(S_p^c\).

*Proof.* By Cauchy–Schwarz,
\[
\begin{aligned}
&\Bigl|\sum_x\bigl(\mu_p(x)-U_{S_p}(x)\bigr)f_p(x)\Bigr|^2\\
&\quad \le\|\mu_p-U_{S_p}\|_2^2\sum_x|f_p(x)|^2\\
&\quad \le p\,\|\mu_p-U_{S_p}\|_2^2 .
\end{aligned}
\]
Multiply by \((\log p)/p\), sum, and apply (4.1). \(\square\)

The corollary needs no pointwise bound on \(f_p\): only the probability \(L^2\) norm enters. This matters later, when the test functions are inverse Fourier transforms that can be as large as \(\sqrt p\) at single points.

## 5. The tails used in later lessons

For large \(X\) put
\[
\begin{gathered}
A_X=A\cap[X^{9/10},X],\\
D_X=D\cap[-X,-X^{9/10}].\quad(5.1)
\end{gathered}
\]

**Lemma 5.1.** For large \(X\), \(|A_X|,|D_X|\gg\sqrt X/(\log X)^3\), and the uniform measures on \(A_X\) and \(D_X\) satisfy the hypotheses of Lemma 4.1 with \(b=4\).

*Proof.* By Theorem 3.1, \(|A_X|\ge A(X)-A(X^{9/10})\)\(\ge c\sqrt X/(\log X)^3\)\(-CX^{9/20}(\log X)^2\gg\sqrt X/(\log X)^3\). Every point mass is \(1/|A_X|\ll(\log X)^3/\sqrt X\)\(\le(\log X)^4/\sqrt X\) for large \(X\), and \(X^{9/10}>\sqrt X+N_*\). The same holds for \(D_X\), using \(B\). \(\square\)

With \(b=4\), Lemma 4.1 and Corollary 4.2 apply to all primes \(p\le\sqrt X/(\log X)^5\). In particular, for any functions \(\phi_p\) with \(|\phi_p|\le1\),
\[
\begin{aligned}
&\sum_{p\le\sqrt X/(\log X)^5}\frac{\log p}p
\Bigl|\mathbb E_{x\in A_X}\phi_p(x)\\
&\qquad -\mathbb E_{x\in S_p}\phi_p(x)\Bigr|^2\ll\log\log X,\quad(5.2)
\end{aligned}
\]
and the same with \(D_X\) and \(S_p^c\). In words: for any choice of bounded test functions, one at each prime, the empirical mean over the tail \(A_X\) and the uniform mean over \(S_p\) agree up to an error whose square has \((\log p)/p\)-weighted sum \(O(\log\log X)\). Since \(\sum_{p\le y}(\log p)/p\sim\log y\), the two means agree for all primes outside a set of \((\log p)/p\)-weight \(O_\delta(\log\log X)\), up to any fixed tolerance \(\delta\).

## 6. Exercises

**6.1.** Show that (4.1) and (4.3) give, for \(2\le y\le\sqrt X/(\log X)^{b+1}\) and fixed \(\delta>0\),
\[
\sum_{\substack{p\le y\\|\sigma_p-1/2|>\delta}}\frac{\log p}p\ll_{b}\delta^{-2}\log\log X.
\]

**6.2** (Gallagher's larger sieve). Let \(\mathcal A\) be a finite set of integers in an interval of length \(X\ge2\), and let \(\mathcal P\) be a finite set of primes such that \(\mathcal A\) meets at most \(\nu_p\) classes modulo \(p\) for each \(p\in\mathcal P\). Show that
\[
|\mathcal A|\le\frac{\sum_{p\in\mathcal P}\log p-\log X}{\sum_{p\in\mathcal P}(\log p)/\nu_p-\log X}
\]
whenever the denominator is positive.

**6.3.** In Lemma 1.1, show that equality holds exactly when \(\mu\) is uniform on a set of \(p-\nu\) residues.

**6.4.** Let \(0<\alpha<\tfrac12\). Suppose that a set \(\mathcal A\subseteq[1,X]\) meets at most \(\alpha p+1\) classes modulo every prime \(p\le X\). Use Exercise 6.2 with the primes up to \(X^{\alpha+\varepsilon}\) to show \(|\mathcal A|\ll_{\alpha,\varepsilon}X^{\alpha+\varepsilon}\) for every \(\varepsilon>0\).

## 7. Solutions

**6.1.** By (4.3), each prime with \(|\sigma_p-\tfrac12|>\delta\) has \(\sigma_p^{-1}+(1-\sigma_p)^{-1}-4>16\delta^2\). All terms of (4.1) are nonnegative, so the \((\log p)/p\)-weight of these primes up to \(y\le Q\) is at most \((16\delta^2)^{-1}\) times the left side of (4.1).

**6.2.** Let \(\mu\) be the uniform measure on \(\mathcal A\). The equality in (2.1) and the bound \(\|\mu_p\|_2^2\ge1/\nu_p\) give
\[
\begin{aligned}
\sum_{p\in\mathcal P}\frac{\log p}{\nu_p}&\le\Bigl(1-\frac1{|\mathcal A|}\Bigr)\log X\\
&\quad +\frac1{|\mathcal A|}\sum_{p\in\mathcal P}\log p,
\end{aligned}
\]
because \(\Pr(n=n')=1/|\mathcal A|\) and the bound \(\log X\) applies only when \(n\ne n'\). Multiplying by \(|\mathcal A|\) and rearranging gives \(|\mathcal A|\bigl(\sum_p(\log p)/\nu_p-\log X\bigr)\)\(\le\sum_p\log p-\log X\).

**6.3.** Equality in Lemma 1.1 means equality in \(1\le(p-\nu)\sum_x\mu(x)^2\), which is Cauchy–Schwarz for the vectors \((\mu(x))\) and \((1)\) on the support; it holds exactly when \(\mu\) is constant on its support.

**6.4.** Let \(\mathcal P\) be the primes up to \(Q=X^{\alpha+\varepsilon}\), so \(\nu_p\le\alpha p+1\). The numerator in Exercise 6.2 is at most \(\sum_{p\le Q}\log p\ll Q\). For the denominator, \((\log p)/\nu_p\ge(\log p)/(\alpha p+1)\)\(\ge(\log p)/(\alpha p)-(\log p)/(\alpha^2p^2)\), and Mertens' estimate gives
\[
\begin{aligned}
\sum_{p\le Q}\frac{\log p}{\nu_p}&\ge\frac{\log Q}{\alpha}-O_\alpha(1)\\
&=\Bigl(1+\frac\varepsilon\alpha\Bigr)\log X-O_\alpha(1).
\end{aligned}
\]
So the denominator is at least \((\varepsilon/\alpha)\log X-O_\alpha(1)\gg_{\alpha,\varepsilon}\log X\) for large \(X\), and \(|\mathcal A|\ll Q/\log X\le X^{\alpha+\varepsilon}\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Sections 2.4 and 2.5. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [Els06] C. Elsholtz, *Additive decomposability of multiplicatively defined sets*, Funct. Approx. Comment. Math. 35 (2006), 61–77, Theorem 1.9. https://www.math.tugraz.at/~elsholtz/WWW/papers/papers22wirsing04.pdf
- [GH] B. Green and A. J. Harper, *Inverse questions for the large sieve*, Geom. Funct. Anal. 24 (2014), numbering of arXiv:1311.6176v1, the larger sieve in Section 2 and its quantitative use. https://arxiv.org/abs/1311.6176v1
