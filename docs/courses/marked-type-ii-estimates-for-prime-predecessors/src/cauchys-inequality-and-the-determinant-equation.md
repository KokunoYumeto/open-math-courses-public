# Cauchy's inequality and the determinant equation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson removes the unknown function \(F\) from the marked bilinear form of [*The marked Type II estimate*](the-marked-type-ii-estimate.md). The marks are expanded into a sum over marking products \(b\mid mn-1\); invariance lets \(F\) depend only on the cofactor \(h=(mn-1)/b\); and Cauchy's inequality in \(h\) leaves a nonnegative square in which \(F\) is absent. For two coprime marking products \(a,b\), the condition that \((mn-1)/a=(rs-1)/b\) is a single linear relation \(bmn-ars=b-a\), the *determinant equation*. Its indicator is split by a circle integral into a major-arc part and a minor-arc part, and Theorem 2.2 of Lesson 1 is reduced to two estimates proved in Lessons 8–17.

**Prerequisites.** [*The marked Type II estimate*](the-marked-type-ii-estimate.md), Sections 1–2 and 4; [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemmas 1.2, 2.1 and 2.2.

Throughout, the hypotheses of Theorem 2.2 of Lesson 1 hold: \(H_m,H_n\ge x^\delta\), \(x/c_*\le X=H_mH_n\le c_*x\), \(\alpha\) and \(\beta\) are supported on rough integers in \([H_m,2H_m]\) and \([H_n,2H_n]\) with \(|\alpha_m|,|\beta_n|\le L^C\), and \(F\) is group-invariant with \(|F|\le1\). Twisted cancellation of \(\alpha\) is not used in this lesson. Implied constants may depend on \(K\), the \(a_i\), \(q\), \(\delta\), \(c_*\) and \(C\).

## 1. Expanding the marks

By Lemma 1.1 of Lesson 1, \(\prod_i\omega_i(h)\) is the number of marking products dividing \(h\), so

\[
\begin{gathered}
\mathcal W(h)=\frac1{V_1\cdots V_K}\\
\times\sum_{\substack{b\ \text{marking}\\ b\mid h}}q^{\omega(h)-K}.\quad(1.1)
\end{gathered}
\]

If \(b\mid h\), invariance gives \(F(h)=F(h/b)\). If moreover no prime of \(b\) divides \(h\) to the second power, then \(\omega(h/b)=\omega(h)-K\); in general \(\omega(h/b)\ge\omega(h)-K\) (Exercise 5.2 of Lesson 1). Define

\[
\begin{gathered}
\mathfrak B'=\frac1{V_1\cdots V_K}\sum_{m,n}\alpha_m\beta_n\\
\times\sum_{\substack{b\ \text{marking}\\ b\mid mn-1}}F\Bigl(\frac{mn-1}b\Bigr)q^{\,\omega((mn-1)/b)} .
\end{gathered}
\]

**Lemma 1.1.** For every fixed \(A>0\), \(|\mathfrak B-\mathfrak B'|\ll_AXL^{-A}\).

**Proof.** For fixed \(m,n\) with \(h=mn-1\), the terms of \(\mathfrak B\) (expanded by (1.1)) and of \(\mathfrak B'\) agree for every marking \(b\mid h\) unless some group prime \(p\) has \(p^2\mid h\). Both \(q^{\omega(h)-K}\) and \(q^{\omega(h/b)}\) lie in \([0,q^{\omega(h)-K}]\), so the difference for this pair \((m,n)\) is at most \(\mathcal W(h)\le C_{K,q}\), and it vanishes unless \(p^2\mid mn-1\) for some group prime \(p\). For fixed \(m\) and \(p\), the condition \(mn\equiv1\ (p^2)\) fixes at most one residue class of \(n\) modulo \(p^2\), and \(p^2\le\exp(4L^{0.2})\le H_n\), so at most \(2H_n/p^2\) values of \(n\) qualify. Summing over \(m\) and over group primes, with Lemma 1.2(3) of Lesson 2,

\[
\begin{gathered}
|\mathfrak B-\mathfrak B'|\le C_{K,q}L^{2C}\cdot4X\sum_p\frac1{p^2}\\
\le8C_{K,q}L^{2C}X\,e^{-L^{0.1}} . \ \square
\end{gathered}
\]

## 2. A dyadic partition and Cauchy's inequality

Fix a smooth nonincreasing \(\phi_0:[0,\infty)\to[0,1]\) equal to \(1\) on \([0,1]\) and to \(0\) on \([2,\infty)\), and put \(\eta(y)=\phi_0(y/2)-\phi_0(y)\). Then \(\eta\) is smooth, supported in \([1,4]\), \(0\le\eta\le1\), and \(\sum_{j\in\mathbb Z}\eta(y/2^j)=1\) for every \(y>0\), because the partial sums telescope. A marking product satisfies \(L^{0.1}\le\log b\le2KL^{0.2}\) (Exercise 5.1 of Lesson 1), so \(\eta(b/Y)\ne0\) for some marking \(b\) only for the powers of two \(Y\) with

\[
\begin{gathered}
L^{0.1}-2\le\log Y\le2KL^{0.2};\quad(2.1)
\end{gathered}
\]

there are at most \(3KL^{0.2}\) of them. For such \(Y\) put

\[
\begin{gathered}
c_Y(h)=\frac1{V_1\cdots V_K}\sum_{a\ \text{marking}}\eta\Bigl(\frac aY\Bigr)\\
\times\sum_{mn-1=ah}\alpha_m\beta_n .
\end{gathered}
\]

Then \(\mathfrak B'=\sum_Y\sum_hF(h)q^{\omega(h)}c_Y(h)\), and \(c_Y(h)=0\) unless \(1\le h\le4X/Y\), since \(mn\le4X\) and \(a\ge Y\) on the support. Cauchy's inequality in \(h\), with \(|F(h)q^{\omega(h)}|\le1\), gives

\[
\begin{gathered}
\Bigl|\sum_hF(h)q^{\omega(h)}c_Y(h)\Bigr|^2\\
\le\frac{4X}Y\,\mathcal Q_Y,\\
\mathcal Q_Y=\sum_h|c_Y(h)|^2.\quad(2.2)
\end{gathered}
\]

Expanding the square,

\[
\begin{aligned}
\mathcal Q_Y&=\frac1{(V_1\cdots V_K)^2}\sum_{a,b}\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
&\quad\times\sum_h\sum_{\substack{mn-1=ah\\ rs-1=bh}}\alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s},\quad(2.3)
\end{aligned}
\]

with \(a,b\) running over marking products. The function \(F\) has disappeared.

**Proposition 2.1 (the Cauchy reduction).** Let \(D_1>0\). If \(\mathcal Q_Y\le C_1XYL^{-D_1}\) for every \(Y\) in (2.1), then \(|\mathfrak B|\ll XL^{0.2-D_1/2}+XL^{-D_1}\), with an implied constant depending on \(C_1\) and the fixed data. In particular, Theorem 2.2 of Lesson 1 follows once \(\mathcal Q_Y\ll XYL^{-2D_*-2}\).

**Proof.** By (2.2), each \(Y\) contributes at most \((4X\cdot C_1XL^{-D_1})^{1/2}\), and there are at most \(3KL^{0.2}\) values of \(Y\). Lemma 1.1 accounts for \(\mathfrak B-\mathfrak B'\). \(\square\)

## 3. Pairs with a common prime

**Lemma 3.1.** The part of \(\mathcal Q_Y\) from pairs \((a,b)\) that share a prime is \(O_A(XYL^{-A})\) for every fixed \(A\).

**Proof.** For fixed \(a,b\le4Y\), the number of pairs \((m,n)\) with \(mn=1+ah\) is at most \(\tau(1+ah)\). By Cauchy's inequality and Lemma 2.2 of Lesson 2, applied with \(l\le4Y\), \(H'=4X/Y\) and \(Z=17c_*x\ge1+lH'\),

\[
\begin{aligned}
&\sum_{h\le4X/Y}\tau(1+ah)\tau(1+bh)\\
&\quad\le\max_{l\in\{a,b\}}\sum_{h\le4X/Y}\tau(1+lh)^2\\
&\quad\ll\frac XYL^3+X^{3/4}L^2\ll\frac XYL^3,
\end{aligned}
\]

because \(Y\le\exp(2KL^{0.2})=x^{o(1)}\). The coefficients contribute at most \(L^{4C}\), and \((V_1\cdots V_K)^{-2}\ll1\). A pair sharing a prime \(p\) has \(p\mid a\) and \(p\mid b\); there are at most \(4Y/p\) multiples of \(p\) up to \(4Y\), so the number of such pairs is at most \(\sum_p16Y^2/p^2\le32Y^2e^{-L^{0.1}}\), the sum over group primes. Altogether the part is \(O(XYL^{4C+3}e^{-L^{0.1}})\). \(\square\)

## 4. The determinant equation

**Lemma 4.1.** Let \(a,b\) be coprime positive integers and \(m,n,r,s\) positive integers with \(mn\ge2\). There is an integer \(h\) with \(mn-1=ah\) and \(rs-1=bh\) if and only if

\[
\begin{gathered}
t\mathrel{:=}bmn-ars=b-a.\quad(4.1)
\end{gathered}
\]

In that case \(h=(mn-1)/a\ge1\).

**Proof.** If \(mn-1=ah\) and \(rs-1=bh\), then \(bmn-ars\)\(=b(1+ah)-a(1+bh)=b-a\). Conversely, (4.1) says \(b(mn-1)=a(rs-1)\). Since \((a,b)=1\), \(a\mid mn-1\); writing \(mn-1=ah\) gives \(abh=a(rs-1)\), so \(rs-1=bh\), and \(h\ge1\) because \(mn-1\ge1\). \(\square\)

So the coprime part of \(\mathcal Q_Y\) is

\[
\begin{gathered}
\mathcal Q_Y^{\rm cop}=\frac1{(V_1\cdots V_K)^2}\\
\times\sum_{(a,b)=1}\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
\times\sum_{m,n,r,s}\alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}\,\mathbf 1_{bmn-ars=b-a}.\quad(4.2)
\end{gathered}
\]

The name comes from the lattice point \((bm,s)\), whose determinant with \((ar,n)\) is \(bmn-ars\). Lessons 8–16 study (4.2) through these lattice points.

## 5. Major arcs

Fix \(A_0>0\). Let \(\mathfrak M\subset\mathbb R/\mathbb Z\) be the union of the arcs

\[
\begin{gathered}
\Bigl\|\theta-\frac hk\Bigr\|\le\frac{2L^{A_0}}Y,\\
1\le k\le L^{A_0},\ (h,k)=1.\quad(5.1)
\end{gathered}
\]

Distinct fractions with denominators at most \(L^{A_0}\) are at distance at least \(L^{-2A_0}\), which exceeds \(4L^{A_0}/Y\) for large \(x\) by (2.1); so the arcs are disjoint. Their total length satisfies

\[
\begin{gathered}
|\mathfrak M|\le\sum_{k\le L^{A_0}}k\cdot\frac{4L^{A_0}}Y\le\frac{4L^{3A_0}}Y.\quad(5.2)
\end{gathered}
\]

Fix a smooth even \(\psi:\mathbb R\to[0,1]\), supported in \([-5,5]\) and equal to \(1\) on \([-4,4]\). For integers \(t\) and marking products \(a,b\) put

\[
\begin{gathered}
\mathcal H_{\mathfrak M}(t;a,b)=\psi\Bigl(\frac tY\Bigr)\\
\times\int_{\mathfrak M}e\bigl(\theta(t-b+a)\bigr)\,d\theta.\quad(5.3)
\end{gathered}
\]

If \(a,b\in[Y,4Y]\) and \(t=b-a\), then \(|t|\le3Y\) and \(\psi(t/Y)=1\). Hence, for such \(a,b\) and every integer \(t\),

\[
\begin{gathered}
\mathbf 1_{t=b-a}=\mathcal H_{\mathfrak M}(t;a,b)+\psi\Bigl(\frac tY\Bigr)\\
\times\int_{\mathbb T\setminus\mathfrak M}e\bigl(\theta(t-b+a)\bigr)\,d\theta,\quad(5.4)
\end{gathered}
\]

where \(\mathbb T=\mathbb R/\mathbb Z\). Define the **major sum** and the **minor sum**

\[
\begin{gathered}
\mathcal Q_Y^{\rm maj}=\frac1{(V_1\cdots V_K)^2}\\
\times\sum_{a,b}\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
\times\sum_{m,n,r,s}\alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}\\
\times\mathcal H_{\mathfrak M}(bmn-ars;a,b),\quad(5.5)
\end{gathered}
\]

with \(a,b\) over all marking products, and \(\mathcal Q_Y^{\rm min}\), defined as (4.2) with \(\mathbf 1_{bmn-ars=b-a}\) replaced by the last term of (5.4). Thus

\[
\begin{gathered}
\mathcal Q_Y^{\rm cop}=\mathcal Q_Y^{\rm min}+\mathcal Q_Y^{\rm maj}-\mathcal Q_Y^{\rm maj,sh},\quad(5.6)
\end{gathered}
\]

where \(\mathcal Q_Y^{\rm maj,sh}\) is the part of (5.5) from pairs \((a,b)\) sharing a prime.

## 6. Absolute bounds

Two absolute bounds are used repeatedly: in Lemma 6.2 below, and in [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md), where a small probability is multiplied by them.

**Lemma 6.1 (absolute raw and comparison sums).** There is \(C_2\), depending only on \(C\), such that

\[
\begin{aligned}
&\sum_{a,b}\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
&\quad\times\sum_h\sum_{\substack{mn-1=ah\\ rs-1=bh}}|\alpha_m\alpha_r\beta_n\beta_s|\\
&\qquad\ll XY\,L^{C_2},\quad(6.1)\\
&\sum_{a,b}\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
&\quad\times\sum_{m,n,r,s}|\alpha_m\alpha_r\beta_n\beta_s|\\
&\quad\times\bigl|\mathcal H_{\mathfrak M}(bmn-ars;a,b)\bigr|\\
&\qquad\ll XY\,L^{C_2+3A_0}.\quad(6.2)
\end{aligned}
\]

**Proof.** For (6.1), the proof of Lemma 3.1 bounds the inner sum by \(O(L^{4C}(X/Y)L^3)\) for each pair, and there are at most \(16Y^2\) pairs \(a,b\le4Y\). For (6.2), \(|\mathcal H_{\mathfrak M}|\le4L^{3A_0}/Y\) by (5.2), and it vanishes unless \(|bmn-ars|\le5Y\). Fix \(a,b\in[Y,4Y]\) and write \(k=mn\), \(l=rs\), both at most \(4X\). For each \(k\) there are at most \(10Y/a+1\le11\) values of \(l\) with \(|bk-al|\le5Y\), and symmetrically. By Cauchy's inequality,

\[
\begin{aligned}
&\sum_{\substack{k,l\le4X\\ |bk-al|\le5Y}}\tau(k)\tau(l)\\
&\quad\le\Bigl(\sum_{(k,l)}\tau(k)^2\Bigr)^{1/2}\Bigl(\sum_{(k,l)}\tau(l)^2\Bigr)^{1/2}\\
&\quad\le11\sum_{k\le4X}\tau(k)^2\ll XL^4,
\end{aligned}
\]

by Lemma 2.1 of Lesson 2. The coefficients contribute \(L^{4C}\), and the \(16Y^2\) pairs give (6.2). \(\square\)

**Lemma 6.2.** For every fixed \(A\), \(|\mathcal Q_Y^{\rm maj,sh}|\ll_AXYL^{-A}\).

**Proof.** In the proof of (6.2), restrict to pairs sharing a prime; by Lemma 3.1 there are at most \(32Y^2e^{-L^{0.1}}\) of them, instead of \(16Y^2\). \(\square\)

## 7. The reduction

Combining (5.6), Lemmas 3.1 and 6.2, and Proposition 2.1:

**Proposition 7.1.** Theorem 2.2 of Lesson 1 follows from the two estimates

\[
\begin{gathered}
|\mathcal Q_Y^{\rm min}|\ll XYL^{-D_1},\\
|\mathcal Q_Y^{\rm maj}|\ll XYL^{-D_1},\quad(7.1)
\end{gathered}
\]

for \(D_1=2D_*+2\), uniformly for \(Y\) in (2.1).

The minor estimate is proved in [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md) (Theorem 4.2 there), for every fixed \(A_0\) exceeding a bound depending on \(D_1\) and \(C\), and every \(K\ge K_0(C,D_*)\). The major estimate is proved in [*The major term and the theorem*](the-major-term-and-the-theorem.md) for every fixed \(A_0\) and \(K\), and it is the only place where twisted cancellation of \(\alpha\) is used.

Here is the heuristic behind the split. On the minor arcs, \(e(\theta(t-b+a))\) oscillates rapidly as \(a\) and \(b\) vary, and the averaging over the marks produces cancellation; but the marks must be summed with weights that remember which primes divide the lattice points, which is the subject of Lessons 8–16. On the major arcs, the phase is nearly constant on residue classes modulo small \(k\), the variables separate by characters, and the cancellation must come from \(\alpha\) itself.

## 8. Exercises

**7.1.** Show that \(\eta(y)=\phi_0(y/2)-\phi_0(y)\) is supported in \([1,4]\) and that \(\sum_{j\in\mathbb Z}\eta(y/2^j)=1\) for \(y>0\).

**7.2.** Show that \(\mathcal Q_Y\ge0\), and that \(\mathcal Q_Y\) does not depend on \(F\) or \(q\).

**7.3.** Let \(a=b=2\). Find positive integers \(m,n,r,s\) with \(bmn-ars=b-a\) for which no integer \(h\) satisfies \(mn-1=ah\) and \(rs-1=bh\). Which hypothesis of Lemma 4.1 fails?

**7.4.** Show that two fractions \(h/k\), \(h'/k'\) with \(k,k'\le Q\) that are distinct as points of \(\mathbb R/\mathbb Z\) satisfy \(\|h/k-h'/k'\|\ge Q^{-2}\).

**7.5.** Prove (5.4) directly from \(\int_{\mathbb T}e(\theta j)\,d\theta=\mathbf 1_{j=0}\) for integers \(j\).

## 9. Solutions

**7.1.** For \(y<1\), both terms equal \(1\); for \(y\ge4\), both vanish. Hence the support is in \([1,4]\). For integers \(J,J'\), \(\sum_{j=-J}^{J'}\eta(y/2^j)\)\(=\phi_0(y/2^{J'+1})-\phi_0(2^Jy)\), which tends to \(1-0\) as \(J,J'\to\infty\) for fixed \(y>0\).

**7.2.** \(\mathcal Q_Y=\sum_h|c_Y(h)|^2\), and \(c_Y(h)\) involves only \(\alpha,\beta,\eta\) and the \(V_i\).

**7.3.** With \(a=b=2\), (4.1) reads \(2mn-2rs=0\), that is \(mn=rs\). Take \(m=n=r=s=2\): then (4.1) holds, but \(mn-1=3\) is odd, so no \(h\) exists. The hypothesis \((a,b)=1\) fails.

**7.4.** For every integer \(j\), \(h/k-h'/k'-j\)\(=(hk'-h'k-jkk')/(kk')\), and the numerator is a nonzero integer, since otherwise the two fractions would coincide in \(\mathbb R/\mathbb Z\). Hence \(\|h/k-h'/k'\|\ge1/(kk')\ge Q^{-2}\).

**7.5.** For integers \(t,a,b\), \(\int_{\mathbb T}e(\theta(t-b+a))\,d\theta=\mathbf 1_{t=b-a}\). Split \(\mathbb T=\mathfrak M\cup(\mathbb T\setminus\mathfrak M)\) and multiply by \(\psi(t/Y)\), which equals \(1\) whenever \(t=b-a\) with \(a,b\in[Y,4Y]\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 3.1. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
