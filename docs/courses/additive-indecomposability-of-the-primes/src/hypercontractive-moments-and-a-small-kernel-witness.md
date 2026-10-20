# Hypercontractive moments and a small-kernel witness

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 3 reduced a quadratic bias at many primes to the lower bound \(\mathbb E_M|\mathcal F_M|\ge e^{0.015K}\) for the positive-frequency Poisson dual, where \(M\) is the product of a random tuple of \(k\) distinct primes of the block \(\mathcal P\). By (6.2) of Lesson 3, \(\mathcal F_M\) is a combination of the Jacobi symbols \(\chi_M(s)=(s/M)\) of squarefree \(s\), with coefficients that themselves depend on \(M\). This lesson shows where the mass of \(\mathcal F_M\) must sit. Large squarefree \(s\) and the terms with \(P\ne1\) contribute little, because a high moment of a sum of Jacobi symbols is controlled by a weighted \(\ell^2\) norm of the coefficients (Proposition 3.1). The proof of that moment bound uses Bonami's hypercontractive inequality, proved here from the binomial theorem. What remains forces, with probability at least \(e^{-O(K)}\), a large value of one of the quadratic exponential sums \(G_d(s,v)\) with small \(s\) (Proposition 6.1).

**Prerequisites.** [*A biased block and an amplified moment*](a-biased-block-and-an-amplified-moment.md), Sections 2–6; [*Dirichlet characters*](course:NT-DIRL/NT-DIRL-01), Theorem 4.1 and the Kronecker symbol; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1.

Throughout, the notation of Lesson 3 is in force: \(T\), \(Z\), \(\mathcal P\), \(J\), \(\mathcal L\), \(K\), \(k\), \(X\), the random tuple with product \(M\), and \(R,\theta,h_0,g_d,N_{dsv},G_d^{(P)},C_s^{(P)}\).

## 1. Jacobi symbols in the denominator

For an odd positive integer \(m\) and an integer \(n\), \((n/m)\) denotes the Jacobi symbol, the product of the Legendre symbols \((n/p)\) over the prime factors of \(m\) with multiplicity. It is multiplicative in \(n\) and in \(m\).

**Lemma 1.1.** Let \(n\ge1\) be an integer that is not a perfect square. The function \(\xi_n\) on positive integers, defined by \(\xi_n(m)=(n/m)\) for odd \(m\) and \(\xi_n(m)=0\) for even \(m\), is a nonprincipal Dirichlet character to a modulus dividing \(8n\). In particular \(\bigl|\sum_{m\le Y}\xi_n(m)\bigr|\le8n\) for every \(Y\).

*Proof.* Write \(n=n_0n_1^2\) with \(n_0>1\) squarefree. For odd \(m\), \((n/m)=(n_0/m)\) if \((m,n_1)=1\), and \((n/m)=0\) otherwise. Let \(d_0\) be the discriminant of \(\mathbb Q(\sqrt{n_0})\): \(d_0=n_0\) if \(n_0\equiv1\pmod4\), and \(d_0=4n_0\) otherwise. For odd \(m\) the Kronecker symbol \((d_0/m)\) is the Jacobi symbol, and \((4/m)=1\), so \((d_0/m)=(n_0/m)\). By [*Dirichlet characters*](course:NT-DIRL/NT-DIRL-01), Theorem 4.1, \(m\mapsto(d_0/m)\) is a real primitive character of conductor \(|d_0|\ne1\). So \(\xi_n\) is the character modulo \(\operatorname{lcm}(2,|d_0|,n_1)\), a divisor of \(8n\), induced by this nonprincipal primitive character. A nonprincipal character sums to zero over every complete period, so a sum over \(m\le Y\) reduces to a sum over fewer than one period, of absolute value at most \(8n\). \(\square\)

## 2. Bonami's inequality

**Lemma 2.1.** For real \(x,y\) and an integer \(l\ge1\),
\[
\begin{aligned}
&\Bigl(\tfrac12|x+y|^{2l}+\tfrac12|x-y|^{2l}\Bigr)^{1/l}\\
&\quad \le x^2+(2l-1)y^2.
\end{aligned}
\]

*Proof.* The left side, raised to the power \(l\), is \(\sum_{i=0}^{l}\binom{2l}{2i}x^{2l-2i}y^{2i}\); the odd powers of \(y\) cancel. The right side raised to the power \(l\) is \(\sum_i\binom li(2l-1)^ix^{2l-2i}y^{2i}\). It suffices that \(\binom{2l}{2i}\le\binom li(2l-1)^i\). Grouping the factors of \((2l)!/(2l-2i)!\) in pairs,
\[
\begin{aligned}
\frac{\binom{2l}{2i}}{\binom li}&=\frac{2^i\prod_{t=0}^{i-1}(l-t)(2l-2t-1)}{(2i)!}\\
&\quad \cdot\frac{i!}{\prod_{t=0}^{i-1}(l-t)}\\
&=\prod_{t=0}^{i-1}\frac{2l-2t-1}{2t+1},
\end{aligned}
\]
using \((2i)!=2^ii!\prod_{t=0}^{i-1}(2t+1)\). Each factor is at most \(2l-1\). \(\square\)

**Lemma 2.2** (Bonami's inequality for signs [Bon, Chapter III, Theorems 2 and 3]). Let \(\varepsilon_1,\dots,\varepsilon_r\) be independent uniform random signs, and let \(F=\sum_{S\subseteq[r]}a_S\prod_{i\in S}\varepsilon_i\) with real coefficients \(a_S\). Then for every integer \(l\ge1\),
\[
\bigl(\mathbb E|F|^{2l}\bigr)^{1/l}\le\sum_{S}(2l-1)^{|S|}a_S^2.
\]

*Proof.* Induct on \(r\); for \(r=0\) both sides equal \(a_\emptyset^2\). Write \(F=F_0+\varepsilon_rF_1\), where \(F_0,F_1\) do not involve \(\varepsilon_r\). By Lemma 2.1 applied pointwise in the other signs,
\[
\mathbb E|F|^{2l}\le\mathbb E\bigl(F_0^2+(2l-1)F_1^2\bigr)^l .
\]
Minkowski's inequality in \(L^l\) gives \(\|F_0^2+(2l-1)F_1^2\|_l\)\(\le\|F_0\|_{2l}^2+(2l-1)\|F_1\|_{2l}^2\). Apply the induction hypothesis to \(F_0\), whose coefficients are the \(a_S\) with \(r\notin S\), and to \(F_1\), whose coefficients are the \(a_S\) with \(r\in S\), indexed by \(S\setminus\{r\}\). \(\square\)

## 3. A moment estimate uniform over a family of arrays

Let \(\mathcal S\) be the set of squarefree \(s<Z^{14}\) coprime to \(\mathcal L\). An *array* is a family \(b=(b_s)_{s\in\mathcal S}\) of complex numbers. Put
\[
\begin{gathered}
l=\lfloor T^{\mu_0}\rfloor,\\
u_0=2l,\\
\|b\|_{\mathrm w}^2=\sum_{s\in\mathcal S}u_0^{\omega(s)}|b_s|^2 .
\end{gathered}
\]

**Proposition 3.1** ([OpenAI-013, (3.13)]). Let \(c>0\) be fixed and let \(\mathcal B\) be a family of arrays with \(|\mathcal B|\le Z^c\) and \(\sum_s|b_s|\le Z^c\) for every \(b\in\mathcal B\). Then
\[
\begin{aligned}
&\Bigl(\mathbb E_M\max_{b\in\mathcal B}\Bigl|\sum_s\chi_M(s)b_s\Bigr|^{2l}\Bigr)^{1/(2l)}\\
&\quad\le e^{o(K)}\max_{b\in\mathcal B}\|b\|_{\mathrm w}+O(Z^{-10}),\quad(3.1)
\end{aligned}
\]
where the \(o(K)\) and the implied constant depend only on \(c\).

*Proof.* *From the maximum to one array.* Bound the maximum by the sum over \(\mathcal B\). Then
\[
\begin{aligned}
&\Bigl(\mathbb E_M\max_b|\cdot|^{2l}\Bigr)^{1/(2l)}\le|\mathcal B|^{1/(2l)}\\
&\qquad \max_b\Bigl(\mathbb E_M\Bigl|\sum_s\chi_M(s)b_s\Bigr|^{2l}\Bigr)^{1/(2l)},
\end{aligned}
\]
and \(|\mathcal B|^{1/(2l)}\le\exp(c\log Z/(2l))\)\(=\exp(O(T^{1-\mu_0}))=e^{o(K)}\), because \(K\asymp T^{1-\gamma}\) and \(\mu_0>\gamma\).

*From tuples to all odd moduli.* Fix \(b\). A product \(M\) of \(k\) distinct primes of \(\mathcal P\) arises from \(k!\) ordered tuples, so it has probability \(k!/(J)_k\le2k!/J^k\); here \((J)_k\ge J^k/2\) because \(k^2=o(J)\). For \(m=M\), \(\chi_M(s)=(s/M)\). By positivity,
\[
\begin{aligned}
&\mathbb E_M\Bigl|\sum_s\chi_M(s)b_s\Bigr|^{2l}
\le\frac{2k!}{J^k}\\
&\qquad \sum_{\substack{m\le(2Z)^k\\ m\ \text{odd}}}\Bigl|\sum_s\Bigl(\frac sm\Bigr)b_s\Bigr|^{2l}.\quad(3.2)
\end{aligned}
\]
Expand the \(2l\)-th power: it is a sum over \(2l\)-tuples \((s_1,\dots,s_{2l})\) of \(b_{s_1}\cdots b_{s_l}\overline{b_{s_{l+1}}\cdots b_{s_{2l}}}\) times \((n/m)\), where \(n=s_1\cdots s_{2l}\le Z^{28l}\); the symbols are real.

*Nonsquare products.* If \(n\) is not a square, Lemma 1.1 bounds the sum over odd \(m\le(2Z)^k\) by \(8n\le8Z^{28l}\). These terms contribute at most \(8Z^{28l}\bigl(\sum_s|b_s|\bigr)^{2l}\le8Z^{(28+2c)l}\).

*Square products.* If \(n\) is a square, \((n/m)\in\{0,1\}\). Let \((\varepsilon_p)\) be independent uniform signs indexed by primes, and put
\[
F(\varepsilon)=\sum_s|b_s|\prod_{p\mid s}\varepsilon_p .
\]
For a \(2l\)-tuple of squarefree indices, \(\mathbb E\prod_{i}\prod_{p\mid s_i}\varepsilon_p\) is \(1\) if every prime occurs an even number of times among the factorizations, that is, if \(s_1\cdots s_{2l}\) is a square, and \(0\) otherwise. So the square terms contribute at most \((2Z)^k\,\mathbb E F^{2l}\). By Lemma 2.2, \(\mathbb EF^{2l}\le\bigl(\sum_s(2l-1)^{\omega(s)}|b_s|^2\bigr)^l\le\|b\|_{\mathrm w}^{2l}\).

*Roots.* Combining,
\[
\begin{aligned}
&\Bigl(\mathbb E_M\Bigl|\sum_s\chi_M(s)b_s\Bigr|^{2l}\Bigr)^{1/(2l)}\\
&\quad \le\Bigl(\frac{2k!(2Z)^k}{J^k}\Bigr)^{1/(2l)}\|b\|_{\mathrm w}\\
&\qquad +\Bigl(\frac{2k!}{J^k}\Bigr)^{1/(2l)}\\
&\qquad \bigl(8Z^{(28+2c)l}\bigr)^{1/(2l)}.
\end{aligned}
\]
Since \(J\gg Z/\log Z\) and \(k!\le k^k\), the first factor is \(\exp\bigl(O(k\log T/l)\bigr)\)\(=\exp(O(T^{0.6-\mu_0}\log T))=e^{o(K)}\). The logarithm of the second term is \(-\frac{k\log Z}{2l}(1+o(1))+O_c(\log Z)\), and \(k/l\to\infty\), so the second term is \(O(Z^{-10})\). \(\square\)

The weight \(u_0^{\omega(s)}\) is the price of a high moment: indices with many prime factors are penalized. Indices \(s\) with \(u_0^{\omega(s)}\) large are rare, and Section 5 bounds their contribution separately.

## 4. Discretization and the terms from common factors

The arrays \(b_s=s^{-1/2}C_s^{(P)}\) of (6.2) of Lesson 3 depend on the tuple. To apply Proposition 3.1 we place them, up to small errors, in a family fixed in advance.

**Parameters.** The array \(s\mapsto s^{-1/2}C_s^{(P)}\) is determined by \(P\), \(\theta\), \(R\), \(h_0\bmod\mathcal L\), the inverses \(\overline M\) modulo divisors of \(\mathcal L\), and the values \(\chi_M(v)\) for \(v\mid\mathcal L\). The inverses depend only on \(M\bmod\mathcal L\). For squarefree \(v\mid\mathcal L\), \(\chi_M(v)=(v/M)\) depends only on \(M\bmod4v\), by Lemma 1.1 applied with \(n=v\) (and trivially for \(v=1\)). Let \(\mathcal G\) be the family of arrays obtained from all unit residues \(M\bmod4\mathcal L\), all \(h_0\bmod\mathcal L\), all integers \(1\le P\le Z^7\), and grids of mesh at most \(Z^{-100}\) in \(\theta\in[0,1]\) and \(R\in[Z^{10},2Z^{13}]\). Then \(|\mathcal G|\le Z^{c_0}\) for an absolute \(c_0\).

**Lemma 4.1.** On the parameter range \(\theta\in[0,1]\), \(R\in[Z^{10},2Z^{13}]\), uniformly in the other parameters,
\[
\begin{gathered}
|G_d^{(P)}(s,v)|\ll\frac{\sqrt{\mathcal L}}P,\\
\Bigl|\frac{\partial G_d^{(P)}}{\partial\theta}\Bigr|\ll\frac{R\sqrt{\mathcal L}}P,\\
\Bigl|\frac{\partial G_d^{(P)}}{\partial R}\Bigr|\ll\frac{\sqrt{\mathcal L}}{RP}.
\end{gathered}
\]
Replacing the parameters of an actual tuple by the nearest grid point changes each \(G_d^{(P)}(s,v)\) by \(O(Z^{-80})\), and changes \(\mathcal F_M\) in (6.2) of Lesson 3 by \(o(1)\) in total. Every array in \(\mathcal G\) has \(\ell^1\) norm at most \(Z^{15}\).

*Proof.* A nonzero term of \(G_d^{(P)}(s,v)\) has \(svw^2\le Rd/4\), that is \(w\le N_{dsv}/2\). If some multiple of \(P\) lies in this range, then \(P\le N_{dsv}/2\), and the number of multiples is at most \(N_{dsv}/(2P)\). Each term is at most \(\sqrt d\,\|\widehat\psi\|_\infty\le\sqrt{\mathcal L}\,\|\widehat\psi\|_\infty\), which with the factor \(1/N_{dsv}\) gives the first bound. Differentiating in \(\theta\) brings down \(2\pi i\,svw^2/d\), of size at most \(\pi R/2\). In \(R\), the factor \(N_{dsv}^{-1}\) has derivative \(-N_{dsv}^{-1}/(2R)\), and \(\partial_R\widehat\psi(svw^2/(Rd))=-\frac{svw^2}{R^2d}\widehat\psi'(\cdot)\) is \(O(1/R)\) on the support. On the whole range, \(svw^2\le Rd/4<Z^{14}\), so the same index ranges as in Lesson 3 occur.

The grid replacement changes \(G_d^{(P)}(s,v)\) by \(O(Z^{13}\sqrt{\mathcal L}\,Z^{-100})=O(Z^{-80})\), using \(\mathcal L\le Z^{0.02}\). In (6.2) of Lesson 3 there are \(O(k^7)\) values of \(P\), fewer than \(Z^{14}\) values of \(s\), and the divisor sums satisfy \(\sum_{v,d\mid\mathcal L}v^{-1/2}\lambda^{\omega(d)}\le4^K=Z^{o(1)}\), by (2.2) of Lesson 3. So the total change is \(O(k^7Z^{14+o(1)-80})=o(1)\). The \(\ell^1\) bound follows from the first estimate and the same divisor bound. \(\square\)

We use two elementary bounds repeatedly:
\[
\begin{gathered}
\sum_{v\mid\mathcal L}v^{-1/2}=1+o(1),\\
\begin{aligned}
\sum_{s\in\mathcal S}\frac{u_0^{\omega(s)}}s&\le\prod_{p<Z^{14}}\Bigl(1+\frac{u_0}p\Bigr)\\
&\le e^{o(K)}.
\end{aligned}\quad(4.1)
\end{gathered}
\]
The first holds because its logarithm is at most \(\sum_{\ell\mid\mathcal L}\ell^{-1/2}\le K/\sqrt z=o(1)\). For the second, the logarithm is at most \(u_0\sum_{p<Z^{14}}1/p=O(T^{\mu_0}\log T)=o(K)\), by Mertens' estimate.

**Lemma 4.2** (the terms with \(P\ne1\)). The terms of (6.2) of Lesson 3 with \(P\ne1\) have total expected absolute value \(o(1)\). Consequently, writing \(C_s=C_s^{(1)}\) and \(G_d=G_d^{(1)}\),
\[
\begin{aligned}
&\mathbb E_M\Bigl|\sum_{s\in\mathcal S}\frac{\chi_M(s)}{\sqrt s}C_s\Bigr|\\
&\quad \ge e^{0.015K}-o(1).\quad(4.2)
\end{aligned}
\]

*Proof.* If \(P\mid M\) and \(P\ne1\), then \(P\ge Z\). For a grid array with \(P\ge Z\), Lemma 4.1 and (4.1) give \(|C_s^{(P)}|\le(1+o(1))(1+\lambda)^K\sqrt{\mathcal L}/P\), so
\[
\begin{aligned}
\|s&\mapsto s^{-1/2}C_s^{(P)}\|_{\mathrm w}\\
&\le e^{o(K)}(1+\lambda)^K\frac{\sqrt{\mathcal L}}Z\\
&\le Z^{-0.99+o(1)}.
\end{aligned}
\]
Apply Proposition 3.1 to the subfamily of \(\mathcal G\) with \(P\ge Z\): the expected maximum of \(|\sum_s\chi_M(s)s^{-1/2}C_s^{(P)}|\) over it is \(Z^{-0.99+o(1)}\). For an actual tuple, each of the \(O(k^7)\) terms with \(P\mid M\), \(P\ne1\), is at most this maximum plus its grid error, and the grid errors total \(o(1)\) by Lemma 4.1. Since \(k^7=Z^{o(1)}\), the total is \(o(1)\). Inequality (4.2) follows from (5.3) of Lesson 3. \(\square\)

## 5. Large kernels contribute little

For \(s<\mathcal L^4\) and \(R\ge Z^{10}\),
\[
\begin{aligned}
\frac{N_{dsv}}d&=\sqrt{\frac{R}{svd}}\ge\sqrt{\frac{Z^{10}}{\mathcal L^6}}\\
&\ge Z^{4.9}.\quad(5.1)
\end{aligned}
\]

**Lemma 5.1** (small kernels are bounded). For \(s<\mathcal L^4\), uniformly on the grid range, \(|G_d(s,v)|\ll2^{\omega(d)/2}\).

*Proof.* If \(sv\) is not a unit modulo \(d\), then \(g_d(-svw^2\overline M)=0\) for every \(w\), by Lemma 5.1 of Lesson 3. Otherwise put \(c=-sv\overline M\), a unit modulo \(d\). As \(w\) runs over the units modulo \(d\), each unit value of \(cw^2\) is taken at most \(2^{\omega(d)}\) times, since a unit has at most two square roots modulo each prime factor of \(d\); for nonunit \(w\) the value \(g_d(cw^2)\) is \(0\). Hence
\[
\begin{gathered}
\begin{aligned}
&\mathbb E_{w\bmod d}|g_d(cw^2)|^2\\
&\quad \le2^{\omega(d)}\mathbb E_b|g_d(b)|^2\le2^{\omega(d)},
\end{aligned}\\
\mathbb E_{w\bmod d}|g_d(cw^2)|\le2^{\omega(d)/2}.
\end{gathered}
\]
The variable \(w\) of \(G_d(s,v)\) runs over an interval of length at most \(N_{dsv}/2\), which by (5.1) meets each residue class modulo \(d\) at most \(N_{dsv}/d+1\le2N_{dsv}/d\) times. Hence \(|G_d(s,v)|\le N_{dsv}^{-1}\cdot(2N_{dsv}/d)\)\(\,\|\widehat\psi\|_\infty\sum_{w\bmod d}|g_d(cw^2)|\)\(\le2\|\widehat\psi\|_\infty2^{\omega(d)/2}\). \(\square\)

**Lemma 5.2** (correlation of large kernels). Let \(v,d,d'\mid\mathcal L\) and \(\mathcal L^4\le S\le Z^{14}\). For all integers \(s\) in \([S,2S)\), define \(G_d(s,v)\) by the formula (6.1) of Lesson 3. Then
\[
\begin{gathered}
\begin{aligned}
&\Bigl|\sum_{S\le s<2S}\frac{G_d(s,v)\overline{G_{d'}(s,v)}}s\Bigr|\\
&\quad \ll A_{d,d'},
\end{aligned}\\
A_{d,d'}=\Bigl(\frac{dd'}{(d,d')^2}\Bigr)^{-1/2}.\quad(5.2)
\end{gathered}
\]

*Proof.* Expand both sums over \(w\) and \(w'\). A nonzero term needs \(w\le\sqrt{Rd/(Sv)}\) and \(w'\le\sqrt{Rd'/(Sv)}\), so there are \(O(R\sqrt{dd'}/(Sv))\) pairs. The normalizations combine to \(N_{dsv}^{-1}N_{d'sv}^{-1}/s=v/(R\sqrt{dd'})\), independent of \(s\). For a fixed pair, the remaining sum over \(s\) is
\[
\begin{gathered}
\sum_{S\le s<2S}F(s)\,e(\alpha s)\,\omega(s),\\
F(s)=g_d(cs)\overline{g_{d'}(c's)},
\end{gathered}
\]
where \(c=-vw^2\overline M\bmod d\), \(c'=-vw'^2\overline M\bmod d'\), \(\alpha\) is real, and \(\omega(s)=\widehat\psi(svw^2/(Rd))\overline{\widehat\psi(svw'^2/(Rd'))}\) has supremum and total variation \(O(1)\) on \([S,2S]\).

If \(c\) or \(c'\) is not a unit, \(F=0\) by Lemma 5.1 of Lesson 3. Otherwise \(F\) has period \(q=\operatorname{lcm}(d,d')\), and by Lemma 5.1 of Lesson 3 it is a product over the primes \(\ell\mid q\) of functions of \(s\bmod\ell\). Its Fourier coefficients \(\widehat F(\xi)=\mathbb E_{s\bmod q}F(s)e_q(-\xi s)\) are the products of the local coefficients. At a prime \(\ell\) dividing exactly one of \(d,d'\), say \(d\), the local factor is \(s\mapsto g_\ell(c_\ell s)=\sqrt\ell\,\widehat{f_\ell}(c_\ell s)\) with a unit \(c_\ell\), and
\[
\mathbb E_{s\bmod\ell}\sqrt\ell\,\widehat{f_\ell}(c_\ell s)\,e_\ell(-\xi s)=\frac{f_\ell(-\xi\overline{c_\ell})}{\sqrt\ell},
\]
of modulus at most \(\ell^{-1/2}\); the case of \(d'\) is the conjugate. At a prime dividing both, the local coefficient is at most \(\mathbb E_s|g_\ell(c_\ell s)||g_\ell(c'_\ell s)|\le1\) by Cauchy–Schwarz and Lemma 5.1 of Lesson 3. So \(|\widehat F(\xi)|\le A_{d,d'}\) for every \(\xi\).

For an interval \(I\) of length at most \(S\),
\[
\begin{aligned}
&\Bigl|\sum_{s\in I}F(s)e(\alpha s)\Bigr|\\
&\quad \le A_{d,d'}\sum_{\xi\bmod q}\min\Bigl(|I|,\\
&\qquad \frac1{2\|\alpha+\xi/q\|}\Bigr)\\
&\quad \ll A_{d,d'}\bigl(S+q\log(2q)\bigr),
\end{aligned}
\]
because the points \(\alpha+\xi/q\) are \(1/q\)-spaced on the circle: the nearest one costs at most \(S\), and the \(j\)-th nearest on either side costs at most \(q/j\). Partial summation inserts \(\omega\) at the cost of a constant factor. Since \(q\le\mathcal L\le S^{1/4}\), the bound is \(O(A_{d,d'}S)\). Multiplying by the normalization and the number of pairs gives (5.2). \(\square\)

**Lemma 5.3** (rare kernels with many prime factors). Put \(\tau=0.005\). For \(\mathcal L^4\le S\le Z^{14}\) and every residue \(a\bmod\mathcal L\),
\[
\sum_{\substack{S\le s<2S,\ s\equiv a\ (\mathcal L)\\s\in\mathcal S,\ u_0^{\omega(s)}>e^{\tau K}}}u_0^{\omega(s)}\le\frac S{\mathcal L}e^{-10K}
\]
for large \(T\).

*Proof.* For such an \(s\), let \(r\) be the product of its \(\lfloor\omega(s)/2\rfloor\) smallest prime factors. Then \(r^2\le s<2S\), \((r,\mathcal L)=1\), \(\omega(r)\ge\omega_0:=\frac{\tau K}{2\log u_0}-1\), and \(u_0^{\omega(s)}\le u_0(u_0^2)^{\omega(r)}\). The integers \(s\in[S,2S)\) with \(r\mid s\) and \(s\equiv a\pmod{\mathcal L}\) form one class modulo \(r\mathcal L\), so there are at most \(S/(r\mathcal L)+1\le2S/(r\mathcal L)\) of them, because \(S/(r\mathcal L)\ge\sqrt S/(\sqrt2\mathcal L)\ge1\). Summing over all squarefree \(r\le\sqrt{2S}\) with \(\omega(r)\ge\omega_0\), and using Rankin's device with the parameter \(T^{1/4}\),
\[
\begin{aligned}
&\sum_{\substack{r\le\sqrt{2S}\\\omega(r)\ge\omega_0}}\frac{(u_0^2)^{\omega(r)}}r\\
&\quad \le T^{-\omega_0/4}\prod_{p\le\sqrt{2S}}\Bigl(1+\frac{u_0^2T^{1/4}}p\Bigr)\\
&\quad \le T^{-\omega_0/4}\exp\bigl(O(u_0^2T^{1/4}\log T)\bigr).
\end{aligned}
\]
Here \(\omega_0\log T/4=(\tau/(8\mu_0)+o(1))K\)\(=(625+o(1))K\), because \(\log u_0=(\mu_0+o(1))\log T\). The positive exponent is \(O(T^{1/4+2\mu_0}\log T)=o(K)\), and \(u_0=e^{o(K)}\). So the whole sum is at most \(\frac{2S}{\mathcal L}u_0e^{-(625-o(1))K}\le\frac S{\mathcal L}e^{-10K}\). \(\square\)

**Corollary 5.4** (the large-kernel norm). Uniformly over all arrays of \(\mathcal G\) with \(P=1\),
\[
\begin{aligned}
&\Bigl(\sum_{\substack{s\in\mathcal S\\s\ge\mathcal L^4}}\frac{u_0^{\omega(s)}}s|C_s|^2\Bigr)^{1/2}\\
&\quad \le e^{(0.006+o(1))K}.\quad(5.3)
\end{aligned}
\]

*Proof.* By Minkowski's inequality and (4.1), it suffices to bound, for each \(v\mid\mathcal L\) and each dyadic segment \([S,2S)\) with \(\mathcal L^4\le S\le Z^{14}\), the quantity \(\Sigma_{v,S}=\sum_{S\le s<2S}\frac{u_0^{\omega(s)}}s\bigl|\sum_d\lambda^{\omega(d)}\)\(\chi_M(d)G_d(s,v)\bigr|^2\) by \(e^{(0.012+o(1))K}\): there are \(O(\log Z)=e^{o(K)}\) segments, and \(\sum_vv^{-1/2}=1+o(1)\).

*Low weight.* On the indices with \(u_0^{\omega(s)}\le e^{\tau K}\), bound the weight by \(e^{\tau K}\), extend the sum to all integers of \([S,2S)\) by positivity, expand the square over \(d,d'\), and apply (5.2):
\[
\begin{aligned}
&e^{\tau K}\sum_{d,d'\mid\mathcal L}\lambda^{\omega(d)+\omega(d')}A_{d,d'}\\
&\quad =e^{\tau K}\prod_{\ell\mid\mathcal L}\Bigl(1+\lambda^2+\frac{2\lambda}{\sqrt\ell}\Bigr)
\end{aligned}
\]
up to an absolute factor. Since every \(\ell\ge z\), the logarithm of the product is \(K\log(1+\lambda^2)+o(K)\).

*High weight.* On the indices with \(u_0^{\omega(s)}>e^{\tau K}\), expand \(|\sum_d\cdot|^2\) and each \(G_d\) as in the proof of Lemma 5.2, and sum absolutely. For a fixed pair \(w,w'\), the periodic factor \(F\) satisfies \(\mathbb E_{s\bmod\mathcal L}|F(s)|\le1\) by Cauchy–Schwarz, so Lemma 5.3, applied class by class modulo \(\mathcal L\), bounds \(\sum_s u_0^{\omega(s)}|F(s)|\) over the high-weight indices by \(Se^{-10K}\). With the normalization and the number of pairs this gives \(O(e^{-10K})\) for each \(d,d'\), and the divisor weights total \((1+\lambda)^{2K}\). Since \(2\log(1+\lambda)<10\), the high-weight part is exponentially small.

So \(\Sigma_{v,S}\le e^{(\tau+\log(1+\lambda^2)+o(1))K}\), and \(\tau+\log(1+\lambda^2)<0.009<0.012\). \(\square\)

## 6. The witness

Let \(\mathcal E\) be the event, for the random tuple, that there exist \(s\in\mathcal S\) with \(s<\mathcal L^4\) and divisors \(v,d\mid\mathcal L\) such that
\[
|G_d(s,v)|\ge2^{\omega(d)/2}e^{-K}.
\tag{6.1}
\]

**Proposition 6.1** ([OpenAI-013, (3.15) and (3.22)]). For large \(T\), \(\Pr(\mathcal E)\ge e^{-O(K)}\).

*Proof.* Split the sum in (4.2) into the part \(\Sigma_{\mathrm{sm}}\) with \(s<\mathcal L^4\) and the part \(\Sigma_{\mathrm{lg}}\) with \(s\ge\mathcal L^4\).

*The large part.* For an actual tuple, \(\Sigma_{\mathrm{lg}}\) differs from the corresponding sum for its nearest grid array by \(o(1)\) on average (Lemma 4.1), and by Proposition 3.1 and (5.3) the expected maximum over \(\mathcal G\) of the large parts is at most \(e^{(0.006+o(1))K}\). So \(\mathbb E_M|\Sigma_{\mathrm{lg}}|\le e^{(0.006+o(1))K}\).

*The small part off \(\mathcal E\).* Let \(\mathcal G_0\subseteq\mathcal G\) be the arrays with \(P=1\) at whose parameters every small-kernel value satisfies \(|G_d(s,v)|\le2^{\omega(d)/2}e^{-0.9K}\). If \(\mathcal E\) fails for an actual tuple, its nearest grid point lies in \(\mathcal G_0\), because the grid error \(O(Z^{-80})\) is far smaller than \(e^{-K}\) (recall \(K=o(\log Z)\)). By Minkowski's inequality and (4.1), the small-kernel part of every array of \(\mathcal G_0\) has weighted norm at most
\[
\begin{aligned}
&e^{o(K)}\sum_{d\mid\mathcal L}\lambda^{\omega(d)}2^{\omega(d)/2}e^{-0.9K}\\
&\quad =e^{(-0.9+\log(1+\sqrt2\lambda)+o(1))K},
\end{aligned}
\]
which is exponentially small since \(\log(1+\sqrt2/16)<0.09\). Proposition 3.1 applied to \(\mathcal G_0\) gives \(\mathbb E_M\bigl[\mathbf 1_{\mathcal E^c}|\Sigma_{\mathrm{sm}}|\bigr]=o(1)\). The maximum over the whole fixed family \(\mathcal G_0\) bounds the small part of every tuple outside \(\mathcal E\); no estimate conditional on \(\mathcal E^c\) is used.

*The whole small part.* By Lemma 5.1 and the same argument, every small-kernel part of an array of \(\mathcal G\) has weighted norm at most \(e^{o(K)}(1+\sqrt2\lambda)^K\cdot O(1)=e^{O(K)}\), so Proposition 3.1 gives \(\bigl(\mathbb E_M|\Sigma_{\mathrm{sm}}|^{2l}\bigr)^{1/(2l)}\le e^{O(K)}\).

*Conclusion.* By (4.2), \(\mathbb E_M|\Sigma_{\mathrm{sm}}|\)\(\ge e^{0.015K}-e^{(0.006+o(1))K}-o(1)\), so \(\mathbb E_M[\mathbf 1_{\mathcal E}|\Sigma_{\mathrm{sm}}|]\ge\frac12e^{0.015K}\) for large \(T\). Hölder's inequality gives \(\mathbb E_M[\mathbf 1_{\mathcal E}|\Sigma_{\mathrm{sm}}|]\le\Pr(\mathcal E)^{1-1/(2l)}e^{O(K)}\), hence \(\Pr(\mathcal E)\ge e^{-O(K)}\). \(\square\)

On the event \(\mathcal E\) a single quadratic exponential sum with a small kernel is large. Lesson 5 extracts from it a rational approximation to \(svd\,\theta\), and from many such approximations a common centre for the translates \(t_p\).

## 7. Exercises

**7.1.** Show that Lemma 2.2 is sharp for \(F=\varepsilon_1\) and \(l=1\), and that for \(F=\varepsilon_1+\varepsilon_2\) and \(l=2\) the bound reads \(\mathbb EF^4=8\le(3+3)^2=36\).

**7.2.** Show that for squarefree \(v\) the value \((v/M)\) on odd positive \(M\) depends only on \(M\bmod4v\), and give an example with \(v=2\) where it does not depend only on \(M\bmod v\).

**7.3.** Let \(d\) be squarefree and odd, and \(c\) a unit modulo \(d\). Show that \(w\mapsto cw^2\) maps the units modulo \(d\) onto a set of \(\varphi(d)/2^{\omega(d)}\) units, each with exactly \(2^{\omega(d)}\) preimages.

**7.4.** Let \(f\) be a function of period \(q\) with \(|\widehat f(\xi)|\le A\) for all \(\xi\). Show that \(|\sum_{s\in I}f(s)e(\alpha s)|\)\(\le A(|I|+2q(1+\log q))\) for every interval \(I\) of integers and real \(\alpha\).

## 8. Solutions

**7.1.** For \(F=\varepsilon_1\), \(l=1\): \(\mathbb EF^2=1\) and the right side is \((2l-1)a_{\{1\}}^2=1\). For \(F=\varepsilon_1+\varepsilon_2\): \(F\in\{2,0,0,-2\}\) with equal probabilities, so \(\mathbb EF^4=8\); the bound is \(\bigl(3\cdot1+3\cdot1\bigr)^2=36\), and \(\mathbb E F^4\le36\) holds.

**7.2.** By Lemma 1.1 with \(n=v\) (if \(v>1\)), \(M\mapsto(v/M)\) on odd \(M\) is a character modulo a divisor of \(\operatorname{lcm}(2,|d_0|)\), where \(d_0\in\{v,4v\}\); this divides \(4v\). For \(v=2\): \((2/M)=1\) for \(M\equiv\pm1\pmod8\) and \(-1\) for \(M\equiv\pm3\pmod8\), so \((2/1)=1\ne(2/3)=-1\), although \(1\equiv3\pmod2\).

**7.3.** By the Chinese remainder theorem it suffices to treat a prime \(\ell\mid d\). The squaring map on the cyclic group \((\mathbb Z/\ell)^\times\) of even order has kernel \(\{\pm1\}\), so its image has index \(2\) and every image point has exactly two preimages. Multiplication by \(c\) is a bijection. Over \(d\) the kernel has \(2^{\omega(d)}\) elements.

**7.4.** Expand \(f(s)=\sum_{\xi\bmod q}\widehat f(\xi)e_q(\xi s)\). Then \(|\sum_{s\in I}f(s)e(\alpha s)|\)\(\le A\sum_\xi|\sum_{s\in I}e((\alpha+\xi/q)s)|\), and \(|\sum_{s\in I}e(\beta s)|\le\min(|I|,1/(2\|\beta\|))\) by the geometric sum. Let \(\delta_0\in[-\frac1{2q},\frac1{2q}]\) be the representative closest to \(0\) of the points \(\beta_\xi=\alpha+\xi/q\) modulo \(1\). The other points are \(\delta_0+m/q\) with \(m\) in a set of \(q-1\) nonzero integers of absolute value at most \(q/2\), and \(\|\delta_0+m/q\|=|\delta_0+m/q|\)\(\ge|m|/q-1/(2q)\ge|m|/(2q)\). The nearest point costs at most \(|I|\); each \(m\ne0\) costs at most \(q/|m|\), and each value of \(|m|\) occurs at most twice. The total is at most \(A(|I|+2q\sum_{j\le q/2}1/j)\)\(\le A(|I|+2q(1+\log q))\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 3: the moment estimate (3.13), the discretization, (3.14)–(3.21), and the small-kernel witness (3.15) and (3.22). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [Bon] A. Bonami, *Étude des coefficients de Fourier des fonctions de \(L^p(G)\)*, Ann. Inst. Fourier 20 (1970), no. 2, 335–402, Chapter III, Theorems 2 and 3. https://www.numdam.org/item/10.5802/aif.357.pdf
