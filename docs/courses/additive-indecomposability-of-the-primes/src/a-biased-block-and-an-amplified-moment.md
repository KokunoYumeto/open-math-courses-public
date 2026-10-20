# A biased block and an amplified moment

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson and the next three prove that the residue supports \(S_p\) of Lesson 1 are not biased by quadratic characters, even when the character is translated by a different residue at every prime (Theorem 1.1). The proof is by contradiction. A bias at many primes produces, through an amplified moment and Poisson summation, a quadratic exponential sum that must be large for many products of primes. Lessons 4 and 5 turn this into a single rational number \(h/m\) that serves as the translating centre at many primes simultaneously. Lesson 6 then uses the quadratic large sieve to show that the two summands concentrate on few *quadratic kernels*, and the collision estimate of Lesson 2 rules this out.

This lesson sets up the contradiction hypothesis, chooses the scales, proves a combinatorial identity that removes repeated primes from a moment, and computes the Poisson dual of the moment.

**Prerequisites.** [*Square-root bounds and collision stability*](square-root-bounds-and-collision-stability.md), Sections 4 and 5; [*Gauss sums*](course:NT-DIRL/NT-DIRL-03), Theorems 1.1 and 2.1; [*Poisson summation, theta, and the functional equation*](course:NT-ZETA/NT-ZETA-04), Theorem 1.2; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorem 3.1.

## 1. The statement

For an odd prime \(p\) let \(\chi_p\) be the quadratic character of \(\mathbb F_p\), extended by \(\chi_p(0)=0\). Keep the standing assumption of Lesson 1 and the supports \(S_p\).

**Theorem 1.1** (quadratic decorrelation [OpenAI-013, Proposition 3.1]). As \(T\to\infty\),
\[
\begin{aligned}
&\sum_{T\le\log p\le2T}\frac{\log p}p\\
&\qquad \,
\max_{t\in\mathbb F_p}\Bigl|\mathbb E_{x\in S_p}\chi_p(x-t)\Bigr|\\
&\quad =o(T).\quad(1.1)
\end{aligned}
\]

The translating residue \(t\) is chosen separately at every prime. Nothing is assumed to relate the choices at different primes; relating them is the main difficulty.

**Corollary 1.2** ([OpenAI-013, Corollary 3.2]). For fixed \(0<\alpha<\beta\), as \(L_*\to\infty\),
\[
\begin{aligned}
&\sum_{\alpha L_*\le\log\log p\le\beta L_*}\frac1p\\
&\qquad \,
\max_{t\in\mathbb F_p}\Bigl|\mathbb E_{x\in S_p}\chi_p(x-t)\Bigr|\\
&\quad =o(L_*).
\end{aligned}
\]

*Proof, assuming Theorem 1.1.* Cover the range of \(\log p\), which is \([e^{\alpha L_*},e^{\beta L_*}]\), by \(O(L_*)\) intervals \([T,2T]\) with \(T\ge\frac12e^{\alpha L_*}\); positivity allows enlarging the two end intervals. On \([T,2T]\), \(1/p\le(\log p)/(Tp)\), so by (1.1) the contribution of each interval is at most \(\epsilon(T)\), where \(\epsilon(T)\to0\). Since every \(T\) used tends to infinity with \(L_*\), the sum of the \(O(L_*)\) contributions is \(o(L_*)\). \(\square\)

The rest of this lesson and Lessons 4–6 prove Theorem 1.1.

## 2. A biased block of primes

Suppose that (1.1) fails. By Mertens' estimate, \(\sum_{T\le\log p\le2T}(\log p)/p=T+O(1)\). Each maximal bias is at most \(1\), so there are a constant \(\delta>0\) and an unbounded sequence of \(T\) along which the primes with maximal bias at least \(\delta\) have \((\log p)/p\)-weight at least \(c_\delta T\), with \(c_\delta>0\). All limits below are taken along this sequence, and all constants may depend on \(\delta\).

**The scales.** Put
\[
\begin{gathered}
\rho=\frac35,\\
\mu_0=10^{-6},\\
\gamma=10^{-7},\\
X=\exp\bigl(T^{1+\rho}\bigr),
\end{gathered}
\]
and, as in Lesson 2, \(A_X=A\cap[X^{9/10},X]\) and \(D_X=D\cap[-X,-X^{9/10}]\). By Lemma 5.1 of Lesson 2, both have \(\gg\sqrt X/(\log X)^3\) elements, and their uniform measures satisfy collision stability with \(b=4\), for primes up to \(\sqrt X/(\log X)^5\). Every prime used in this lesson and the next three satisfies \(\log p\le2T\), far below this cutoff, because \(\log\sqrt X=\frac12T^{1.6}\).

**Pruning.** The density term of Lemma 4.1 of Lesson 2 shows that the primes with \(\sigma_p\notin[\frac13,\frac23]\) have \((\log p)/p\)-weight \(O(\log\log X)=O(\log T)\). For each prime \(p\) with maximal bias at least \(\delta\), choose a maximizing translate \(t_p\) and a sign \(\epsilon_p\in\{1,-1\}\) with
\[
\begin{aligned}
&\epsilon_p\,\mathbb E_{x\in S_p}\chi_p(x-t_p)\\
&\quad =\max_t\Bigl|\mathbb E_{x\in S_p}\chi_p(x-t)\Bigr|\ge\delta;
\end{aligned}
\]
the mean is real because \(\chi_p\) is real. Apply (5.2) of Lesson 2 to the functions \(\phi_p(x)=\chi_p(x-t_p)\), for \(A_X\) and for \(D_X\). The primes at which either empirical mean differs from the corresponding uniform mean by more than \(\delta/8\) have weight \(O_\delta(\log T)\). Delete them and the unbalanced primes; weight \(\gg T\) remains.

**The opposite side.** The complete sum \(\sum_{x\in\mathbb F_p}\chi_p(x-t)\) vanishes, so
\[
\begin{aligned}
&\mathbb E_{x\in S_p^c}\chi_p(x-t)\\
&\quad =-\frac{\sigma_p}{1-\sigma_p}\,\mathbb E_{x\in S_p}\chi_p(x-t),
\end{aligned}
\]
and \(\sigma_p/(1-\sigma_p)\ge\frac12\) on balanced primes. At every remaining prime, therefore,
\[
\begin{gathered}
\epsilon_p\,\mathbb E_{x\in A_X}\chi_p(x-t_p)\ge\delta-\frac\delta8,\\
\epsilon_p\,\mathbb E_{x\in D_X}\chi_p(x-t_p)\le-\frac\delta2+\frac\delta8.
\end{gathered}
\]

**A dyadic block.** The band \(T\le\log p\le2T\) is covered by \(O(T)\) intervals \([Z,2Z]\), and the remaining primes have weight \(\gg T\), so some interval carries weight bounded below by a positive constant. Each prime in it has weight \((\log p)/p=O(\log Z/Z)\). We obtain:

**Lemma 2.1.** There are \(Z\) with \(\log Z\asymp T\) and a set \(\mathcal P\) of primes in \([Z,2Z]\), with \(J=|\mathcal P|\gg_\delta Z/\log Z\), such that \(\frac13\le\sigma_p\le\frac23\) for \(p\in\mathcal P\) and
\[
\begin{gathered}
\mathbb E_{x\in A_X}\epsilon_p\chi_p(x-t_p)\ge c_\delta,\\
\mathbb E_{x\in D_X}\epsilon_p\chi_p(x-t_p)\le-c_\delta\\
(p\in\mathcal P),\quad(2.1)
\end{gathered}
\]
with \(c_\delta=3\delta/8\). \(\square\)

**Amplifier primes.** Apply the density term of Lemma 4.1 of Lesson 2 to the band \(T^\gamma\le\log p\le2T^\gamma\). Its total weight is \(T^\gamma+O(1)\), and the unbalanced primes in it have weight \(O(\log T)=o(T^\gamma)\). The same dyadic argument gives a block \([z,2z]\) with \(\log z\asymp T^\gamma\) containing \(\gg z/\log z\) primes \(\ell\) with \(\frac13\le\sigma_\ell\le\frac23\). Put
\[
K=\Bigl\lfloor0.02\,\frac{\log Z}{\log(2z)}\Bigr\rfloor,
\]
and let \(\mathcal L\) be the product of \(K\) distinct such primes; there are enough of them, because \(z/\log z\ge\exp(cT^\gamma)/T\) exceeds every fixed power of \(T\). Let \(k\) be the least even integer with \(k\ge\log X/\log Z+10\). Then
\[
\begin{gathered}
K\asymp T^{1-\gamma},\\
\mathcal L\le Z^{0.02},\\
k\asymp T^\rho,\\
K=o(\log Z),\\
\frac Kk\gg T^{1-\gamma-\rho}.\quad(2.2)
\end{gathered}
\]
Indeed \(\log\mathcal L\le K\log(2z)\le0.02\log Z\), and \(\log X/\log Z=T^{1.6}/\log Z\asymp T^{0.6}\). Since \(2z<Z\), no prime factor of \(\mathcal L\) lies in \(\mathcal P\).

## 3. An amplified moment

For a prime \(\ell\mid\mathcal L\) let \(f_\ell=\mathbf 1_{S_\ell}-\sigma_\ell\), viewed as a function on \(\mathbb Z\) of period \(\ell\). Put
\[
\begin{gathered}
\lambda=\frac1{16},\\
W(n)=\prod_{\ell\mid\mathcal L}\bigl(1+\lambda f_\ell(n)\bigr),\\
H(n)=\frac1J\sum_{p\in\mathcal P}\epsilon_p\chi_p(n-t_p).
\end{gathered}
\]
The weight \(W\) is positive, has period \(\mathcal L\), and has mean \(1\) over a period: by the Chinese remainder theorem the residues of \(n\) modulo the different \(\ell\) are independent and uniform, and each \(f_\ell\) has mean \(0\). If \(n\in A_X\), then \(n>\ell+N_*\), so \(n\bmod\ell\in S_\ell\) and \(f_\ell(n)=1-\sigma_\ell\ge\frac13\). Hence
\[
\begin{gathered}
W(n)\ge(1+\lambda/3)^K\\
(n\in A_X).\quad(3.1)
\end{gathered}
\]
The amplifier \(W\) rewards integers that behave like elements of \(A\) at the small primes \(\ell\).

**A smooth weight.** Fix a real even smooth function \(\varphi_0\ge0\) supported in \([-\frac18,\frac18]\), not identically zero, and let \(g_0(x)=\int\varphi_0(y)e(xy)\,dy\). Then \(g_0\) is real and even, and for \(|x|\le1\), \(g_0(x)\ge\cos(\pi/4)\int\varphi_0>0\). Put \(\psi=g_0^2\). With the convention \(\widehat\psi(y)=\int\psi(x)e(-xy)\,dx\), the transform \(\widehat\psi=\varphi_0*\varphi_0\) is smooth, even, real and supported in \([-\frac14,\frac14]\), and \(\psi\) is a nonnegative even Schwartz function bounded below by a positive constant on \([0,1]\).

Define
\[
\begin{gathered}
I=\sum_{n\in\mathbb Z}\psi(n/X)\,W(n)\,H(n)^k,\\
I_0=\sum_{n\in\mathbb Z}\psi(n/X)\,W(n).
\end{gathered}
\]

**Lemma 3.1.** For large \(T\),
\[
\begin{gathered}
I\ge\sqrt X\,e^{0.016K},\\
I_0=X\,\widehat\psi(0)\ll X.\quad(3.2)
\end{gathered}
\]

*Proof.* All terms of \(I\) are nonnegative, since \(k\) is even. Restrict to \(n\in A_X\), where \(n/X\in[0,1]\) and \(\psi(n/X)\gg1\). By (3.1) and Jensen's inequality for the convex function \(x\mapsto x^k\),
\[
\begin{aligned}
I&\gg(1+\lambda/3)^K\sum_{n\in A_X}H(n)^k\\
&\ge(1+\lambda/3)^K\\
&\quad \,|A_X|\Bigl(\mathbb E_{n\in A_X}H(n)\Bigr)^k\\
&\ge(1+\lambda/3)^K\,\frac{\sqrt X}{(\log X)^3}\,c_\delta^k,
\end{aligned}
\]
because \(\mathbb E_{n\in A_X}H(n)\ge c_\delta\) by (2.1). Here \(\log(1+\lambda/3)=\log(49/48)>0.0206\), while \(k+\log\log X\ll T^{0.6}=o(K)\) by (2.2). So \(\log I\)\(\ge\frac12\log X+0.0206K-o(K)\)\(\ge\frac12\log X+0.016K\) for large \(T\).

For \(I_0\), expand \(W(n)=\sum_{h\bmod\mathcal L}\widehat W(h)\,e_{\mathcal L}(hn)\), where \(\widehat W(0)=1\) is the mean. Poisson summation ([*Poisson summation, theta, and the functional equation*](course:NT-ZETA/NT-ZETA-04), Theorem 1.2, applied to \(x\mapsto\psi(x/X)e(hx/\mathcal L)\)) gives
\[
\begin{aligned}
&\sum_n\psi(n/X)\,e_{\mathcal L}(hn)\\
&\quad =X\sum_{j\in\mathbb Z}\widehat\psi\bigl(X(j-h/\mathcal L)\bigr).
\end{aligned}
\]
If \(h\not\equiv0\pmod{\mathcal L}\), every argument has absolute value at least \(X/\mathcal L>\frac14\), so the sum vanishes; for \(h=0\) only \(j=0\) survives. \(\square\)

## 4. Removing repeated primes

Expanding \(H(n)^k\) produces products over \(k\)-tuples of primes from \(\mathcal P\). The Poisson computation of Section 5 works for tuples of distinct primes. The following identity controls the rest.

**Lemma 4.1** ([OpenAI-013, (3.6)]). Let \(y_1,\dots,y_J\in\{0,1,-1\}\), put \(H=J^{-1}\sum_iy_i\), and let \(k\ge2\) be even. Then, for an absolute constant \(C\),
\[
\begin{aligned}
&\Bigl|H^k-\frac1{J^k}\sum_{\substack{i_1,\dots,i_k\in[J]\\\text{distinct}}}y_{i_1}\cdots y_{i_k}\Bigr|\\
&\quad \le\sum_{1\le j\le k/2}\Bigl(\frac{k^C}J\Bigr)^j|H|^{k-2j}.\quad(4.1)
\end{aligned}
\]

*Proof.* Write \(p_m=\sum_iy_i^m\) for the power sums. The sum over distinct indices satisfies
\[
\begin{aligned}
&\sum_{\text{distinct}}y_{i_1}\cdots y_{i_k}\\
&\quad =\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)\prod_{c}p_{|c|},\quad(4.2)
\end{aligned}
\]
where \(c\) runs over the cycles of \(\sigma\) and \(|c|\) is the length. To see this, sum the right side over the permutations with a given set partition \(\pi\) of \([k]\) into cycle supports. A block of size \(m\) is the support of \((m-1)!\) cycles, each of sign \((-1)^{m-1}\), so the right side equals \(\sum_\pi\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\;p_{|B|}\), and \(\prod_{B\in\pi}p_{|B|}\) is the sum of \(y_{i_1}\cdots y_{i_k}\) over the index tuples that are constant on each block of \(\pi\). The coefficient of a tuple whose equality pattern is the partition \(\tau\) is therefore \(\sum_{\pi\le\tau}\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\), the sum over the partitions \(\pi\) finer than \(\tau\). This factorizes over the blocks of \(\tau\): for a block of size \(n\) it is \(\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\), which is \(1\) for \(n=1\) and \(0\) for \(n\ge2\). So exactly the tuples of distinct indices survive, each with coefficient \(1\).

Because \(y_i\in\{0,\pm1\}\), \(p_m=JH\) for odd \(m\), and \(0\le p_m\le J\) for even \(m\). The identity permutation contributes \((JH)^k\). Let \(\sigma\ne\mathrm{id}\) have \(k-2j\) cycles of odd length; the number of odd cycles has the parity of \(k\), and \(j\ge1\) because only the identity has \(k\) odd cycles. Then
\[
2j=\sum_{c\text{ odd}}(|c|-1)+\sum_{c\text{ even}}|c|,
\]
so the number of even cycles is at most \(j\), and the term of \(\sigma\) is at most \((J|H|)^{k-2j}J^{j}\) in absolute value. An odd cycle of length \(m\ge3\) moves \(m\le\frac32(m-1)\) points, and an even cycle moves \(|c|\) points, so \(\sigma\) moves at most \(3j\) points. A permutation moving exactly \(t\) given points can be chosen in at most \(t!\) ways, so there are at most \(\sum_{t\le3j}\binom kt t!\le(3j+1)k^{3j}\le k^{5j}\) permutations moving at most \(3j\) points; the last step uses \(3j+1\le4^j\le k^{2j}\). Summing over \(j\) and dividing by \(J^k\) gives (4.1) with \(C=5\). \(\square\)

**Application to the moment.** Apply (4.1) at each \(n\) with \(y_p=\epsilon_p\chi_p(n-t_p)\), multiply by \(\psi(n/X)W(n)\ge0\), and sum. By Hölder's inequality for the measure \(\psi(n/X)W(n)\),
\[
\begin{aligned}
&\sum_n\psi(n/X)W(n)|H(n)|^{k-2j}\\
&\quad \le I^{1-2j/k}I_0^{2j/k}.
\end{aligned}
\]
So the sum over distinct tuples differs from \(I\) by at most \(I\sum_{j\ge1}\bigl(k^CJ^{-1}(I_0/I)^{2/k}\bigr)^j\). By (3.2), \((I_0/I)^{2/k}\ll X^{1/k}e^{-0.032K/k}\)\(\le Ze^{-0.032K/k}\), because \(k\ge\log X/\log Z\). Since \(J\gg Z/\log Z\),
\[
\begin{aligned}
&\frac{k^C}J\Bigl(\frac{I_0}I\Bigr)^{2/k}\\
&\quad \ll k^C\log Z\;e^{-0.032K/k}\longrightarrow0,
\end{aligned}
\]
because \(K/k\gg T^{0.4-\gamma}\) while \(\log(k^C\log Z)=O(\log T)\). Hence
\[
\begin{aligned}
&\frac1{J^k}\sum_n\psi(n/X)W(n)\\
&\qquad \sum_{\text{distinct}}\prod_{i=1}^k\epsilon_{p_i}\chi_{p_i}(n-t_{p_i})\\
&\quad =(1+o(1))\,I.\quad(4.3)
\end{aligned}
\]

## 5. Poisson summation with arbitrary translations

Choose an ordered \(k\)-tuple of distinct primes of \(\mathcal P\) uniformly at random. Every function used below depends on the tuple only through the product \(M\) of its entries, and \(\mathbb E_M\) denotes the expectation over the random tuple. Put
\[
\begin{gathered}
\chi_M=\prod_{p\mid M}\chi_p,\\
\epsilon_M=\prod_{p\mid M}\epsilon_p,\\
0\le t_M<M,\\
t_M\equiv t_p\pmod p\ (p\mid M).
\end{gathered}
\]
The character \(\chi_M\) is the Jacobi symbol \((\cdot/M)\); it is real and primitive modulo the squarefree odd number \(M\), as a product of primitive characters to coprime moduli. Define
\[
\begin{gathered}
R=\frac MX,\\
\theta=\frac{t_M}M,\\
h_0\equiv-t_M\overline M\pmod{\mathcal L},\\
0\le h_0<\mathcal L,
\end{gathered}
\]
where \(\overline M\) is an inverse of \(M\) modulo \(\mathcal L\). Bars denote inverses modulo the modulus in the expression. Since \(Z^k\le M\le(2Z)^k\) and \(Z^{k-12}<X\le Z^{k-10}\) by the choice of \(k\),
\[
Z^{10}\le R\le Z^{12+o(1)}.
\tag{5.1}
\]
The left side of (4.3) equals \((J)_k J^{-k}\,\mathbb E_M\,\epsilon_M\sum_n\psi(n/X)\)\(W(n)\chi_M(n-t_M)\), where \((J)_k=J(J-1)\cdots(J-k+1)\).

**Local transforms of the amplifier.** For \(d\mid\mathcal L\) put \(f_d=\prod_{\ell\mid d}f_\ell\) (a function modulo \(d\) by the Chinese remainder theorem), \(f_1=1\), and
\[
g_d(b)=\sqrt d\;\mathbb E_{x\bmod d}\,f_d(x)\,e_d(-bx).
\]

**Lemma 5.1.** For \(d\mid\mathcal L\),
\[
\begin{gathered}
\mathbb E_{b\bmod d}|g_d(b)|^2\le1,\\
|g_d(b)|\le\sqrt d,\\
g_d(b)=\prod_{\ell\mid d}g_\ell\bigl(b\,\overline{d/\ell}\bigr),
\end{gathered}
\]
where \(\overline{d/\ell}\) is an inverse of \(d/\ell\) modulo \(\ell\). If \(d>1\), \(g_d\) vanishes at every \(b\) with \((b,d)>1\).

*Proof.* By Parseval, \(\mathbb E_b|g_d(b)|^2=\sum_b|\widehat{f_d}(b)|^2\)\(=\mathbb E_x|f_d(x)|^2=\prod_\ell\sigma_\ell(1-\sigma_\ell)\le1\). The bound \(|g_d|\le\sqrt d\) holds since \(|f_d|\le1\). For coprime \(\ell\) and \(d/\ell\) one has \(1/d\equiv\overline{d/\ell}/\ell+\overline\ell/(d/\ell)\pmod1\), and iterating over the prime factors of \(d\) gives \(bx/d\equiv\sum_{\ell\mid d}b\,\overline{d/\ell}\,x/\ell\pmod1\); the expectation over \(x\bmod d\) then factors by the Chinese remainder theorem. If \(\ell\mid(b,d)\), the factor at \(\ell\) is \(g_\ell(0)=\sqrt\ell\,\mathbb E f_\ell=0\). \(\square\)

**The Poisson dual.** Expand \(W=\sum_{d\mid\mathcal L}\lambda^{\omega(d)}f_d\), where \(\omega(d)\) is the number of prime factors. For fixed \(d\), the function \(F(n)=f_d(n)\chi_M(n-t_M)\) has period \(Md\), and \((M,d)=1\). Poisson summation, as in the proof of Lemma 3.1, gives
\[
\begin{gathered}
\begin{aligned}
&\sum_n\psi(n/X)F(n)\\
&\quad =X\sum_{u\in\mathbb Z}\widehat F(u)\,\widehat\psi\Bigl(\frac{u}{Rd}\Bigr),
\end{aligned}\\
\widehat F(u)=\mathbb E_{n\bmod Md}F(n)\,e_{Md}(-un),
\end{gathered}
\]
using that \(\widehat\psi\) is even and \(X/(Md)=1/(Rd)\). By the Chinese remainder theorem, with \(un/(Md)\)\(\equiv u\overline Mn/d+u\overline dn/M\pmod1\),
\[
\begin{aligned}
\widehat F(u)&=\frac{g_d(u\overline M)}{\sqrt d}\\
&\quad \cdot\mathbb E_{y\bmod M}\chi_M(y-t_M)\\
&\quad \,e_M(-u\overline dy).
\end{aligned}
\]
Substitute \(y=z+t_M\). For the primitive character \(\chi_M\), \(\sum_z\chi_M(z)e_M(az)=\chi_M(a)\tau(\chi_M)\) for every integer \(a\), where \(\tau(\chi_M)\) is its Gauss sum, of modulus \(\sqrt M\) ([*Gauss sums*](course:NT-DIRL/NT-DIRL-03), Theorems 1.1 and 2.1; \(\chi_M\) is real). Since \(\chi_M(\overline d)=\chi_M(d)\),
\[
\begin{aligned}
\widehat F(u)&=\frac{\tau(\chi_M)}{M\sqrt d}\,\chi_M(-1)\chi_M(d)\\
&\quad \,\chi_M(u)\,g_d(u\overline M)\\
&\quad \,e_M(-u\overline dt_M).
\end{aligned}
\]

**The phase.** The integer \(t_M+Mh_0\) is divisible by \(\mathcal L\), hence by \(d\). Write \(d\overline d+Mm'=1\) with an integer \(m'\equiv\overline M\pmod d\). Then
\[
\begin{aligned}
\frac{\overline d\,t_M}M&=\frac{t_M}{dM}-\frac{m't_M}d\\
&\equiv\frac{\theta}d+\frac{h_0}d\pmod{\tfrac1d\mathbb Z},
\end{aligned}
\]
because \(m't_M\equiv\overline Mt_M\equiv-h_0\pmod d\); multiplying by the integer \(u\), \(e_M(u\overline dt_M)=e\bigl((\theta+h_0)u/d\bigr)\).

Collect the terms, replace \(u\) by \(-u\) (using \(\chi_M(-u)=\chi_M(-1)\chi_M(u)\) and that \(\widehat\psi\) is even), divide by \(\sqrt X\), and use \(\sqrt X\,|\tau(\chi_M)|/(M\sqrt d)=1/\sqrt{Rd}\). The result is that \(\epsilon_M X^{-1/2}\sum_n\psi(n/X)W(n)\chi_M(n-t_M)\) equals a complex number of modulus \(1\), depending only on the tuple, times
\[
\begin{aligned}
&\sum_{d\mid\mathcal L}\frac{\lambda^{\omega(d)}\chi_M(d)}{\sqrt{Rd}}
\sum_{u\in\mathbb Z}\chi_M(u)\\
&\quad \,g_d(-u\overline M)\,e\Bigl(\frac{(h_0+\theta)u}d\Bigr)\\
&\quad \,\widehat\psi\Bigl(\frac u{Rd}\Bigr).\quad(5.2)
\end{aligned}
\]
The term \(u=0\) vanishes since \(\chi_M(0)=0\).

**Positive frequencies.** Let \(\mathcal F_M\) be the part of (5.2) with \(u>0\). Since \(f_d\) is real, \(\overline{g_d(b)}=g_d(-b)\); since \(\widehat\psi\) is real and even, the part with \(u<0\) equals \(\chi_M(-1)\overline{\mathcal F_M}\). So (5.2) has modulus at most \(2|\mathcal F_M|\). The normalization \((J)_k/J^k\) is at most \(1\), and (4.3) and Lemma 3.1 give \((1+o(1))I/\sqrt X\ge e^{0.016K}/2\). Therefore
\[
\mathbb E_M|\mathcal F_M|\ge e^{0.015K}.
\tag{5.3}
\]

## 6. Squarefree kernels of the frequencies

Every integer \(u\ge1\) has a unique factorization
\[
\begin{gathered}
u=svw^2,\\
s\ \text{squarefree},\ (s,\mathcal L)=1,\\
v\mid\mathcal L,\\
w\ge1:
\end{gathered}
\]
\(s\) is the product of the primes not dividing \(\mathcal L\) that occur in \(u\) to an odd power, \(v\) the product of those dividing \(\mathcal L\) that occur to an odd power, and \(w^2=u/(sv)\). Then \(\chi_M(u)=\chi_M(s)\chi_M(v)\mathbf 1_{(w,M)=1}\), and since \(M\) is squarefree, \(\mathbf 1_{(w,M)=1}=\sum_{P\mid(w,M)}(-1)^{\omega(P)}\).

For positive integers \(P\), divisors \(d,v\) of \(\mathcal L\), and squarefree \(s\) coprime to \(\mathcal L\), define
\[
\begin{aligned}
N_{dsv}&=\sqrt{\frac{Rd}{sv}},\\
G_d^{(P)}(s,v)&=\frac1{N_{dsv}}\sum_{\substack{w\ge1\\P\mid w}}g_d(-svw^2\overline M)\,\\
&\qquad e\Bigl(\frac{(h_0+\theta)svw^2}d\Bigr)\,\\
&\qquad\widehat\psi\Bigl(\frac{svw^2}{Rd}\Bigr),\\
C_s^{(P)}&=\sum_{v\mid\mathcal L}\frac{\chi_M(v)}{\sqrt v}\sum_{d\mid\mathcal L}\lambda^{\omega(d)}\chi_M(d)\,\\
&\qquad G_d^{(P)}(s,v).\quad(6.1)
\end{aligned}
\]
Since \(1/\sqrt{Rd}=1/(N_{dsv}\sqrt{sv})\), regrouping (5.2) gives
\[
\begin{aligned}
\mathcal F_M&=\sum_{P\mid M}(-1)^{\omega(P)}\\
&\quad \sum_{\substack{s\ \text{squarefree}\\ (s,\mathcal L)=1}}\frac{\chi_M(s)}{\sqrt s}\,C_s^{(P)}.\quad(6.2)
\end{aligned}
\]

**Ranges.** \(\widehat\psi\) vanishes outside \([-\frac14,\frac14]\), so every nonzero term has \(svw^2\le Rd/4\le R\mathcal L\). By (5.1) and (2.2), \(R\mathcal L<Z^{14}\) for large \(T\). Hence only \(s<Z^{14}\) and \(w<Z^7\) occur, and only \(P\le Z^7\). A divisor of \(M\) of size at most \(Z^7\) has at most \(7\) prime factors, since each prime factor is at least \(Z\); so (6.2) has \(O(k^7)\) values of \(P\), and the inner sums are finite.

**The plan.** For many tuples, (5.3) forces a large value of one of the sums \(G_d^{(1)}(s,v)\) with \(s\) small. On an arithmetic progression \(w=x+dj\), the phase of \(G_d^{(1)}(s,v)\) is a quadratic polynomial in \(j\) with leading coefficient \(svd\theta\). A large quadratic exponential sum forces this coefficient to be close to a rational number with small denominator, which relates \(\theta=t_M/M\), and hence the translates \(t_p\), across the primes of \(M\). Since the arrays \(C_s^{(P)}\) depend on the random tuple, the moment estimate of Lesson 4 is proved uniformly over a fixed family of arrays that contains their discretizations.

## 7. Exercises

**7.1.** Verify (4.2) directly for \(k=2\) and \(k=3\): \(\sum_{i\ne j}y_iy_j=p_1^2-p_2\) and \(\sum_{\text{distinct}}y_iy_jy_l=p_1^3-3p_1p_2+2p_3\).

**7.2.** Let \(M\) and \(d\) be coprime positive integers, \(\overline M\) an inverse of \(M\) modulo \(d\) and \(\overline d\) an inverse of \(d\) modulo \(M\). Show that \(\frac1{Md}\equiv\frac{\overline M}d+\frac{\overline d}M\pmod1\).

**7.3.** Show that for odd squarefree \(M\), the character \(\chi_M=\prod_{p\mid M}\chi_p\) is primitive modulo \(M\), and that \(\chi_M(-1)=(-1)^{(M-1)/2}\).

**7.4.** In the construction of \(\psi\), show that \(\widehat\psi=\varphi_0*\varphi_0\), and that \(\psi\) decays faster than any power of \(|x|\).

## 8. Solutions

**7.1.** For \(k=2\) the permutations are the identity, with term \(p_1^2\), and the transposition, with sign \(-1\) and one cycle of length \(2\), giving \(-p_2\). The left side is \(\bigl(\sum y_i\bigr)^2-\sum y_i^2\). For \(k=3\): the identity gives \(p_1^3\); the three transpositions give \(-p_1p_2\) each; the two \(3\)-cycles are even and give \(p_3\) each. Directly, \(p_1^3=\sum_{\text{distinct}}+3\sum_{i\ne j}y_i^2y_j+p_3\), and \(\sum_{i\ne j}y_i^2y_j=p_2p_1-p_3\), so \(\sum_{\text{distinct}}=p_1^3-3p_1p_2+2p_3\).

**7.2.** The number \(1-d\overline d\) is divisible by \(M\) and \(1-M\overline M\) by \(d\), so \(N=1-d\overline d-M\overline M\) is divisible by both, hence by \(Md\). Then \(\frac{\overline M}d+\frac{\overline d}M=\frac{M\overline M+d\overline d}{Md}=\frac{1-N}{Md}\)\(\equiv\frac1{Md}\pmod1\).

**7.3.** Each \(\chi_p\) is a nonprincipal character modulo the prime \(p\), hence primitive. If \(\chi_M\) were induced from a proper divisor \(M'\) of \(M\), choose \(p\mid M\) with \(p\nmid M'\) and \(a\equiv1\pmod{M/p}\) with \(\chi_p(a)=-1\); then \(a\equiv1\pmod{M'}\) but \(\chi_M(a)=-1\). For the value at \(-1\): \(\chi_p(-1)=(-1)^{(p-1)/2}\), and \(\sum_{p\mid M}\frac{p-1}2\equiv\frac{M-1}2\pmod2\) because \(\frac{ab-1}2-\frac{a-1}2-\frac{b-1}2=\frac{(a-1)(b-1)}2\) is even for odd \(a,b\).

**7.4.** The transform of \(g_0\) is \(\varphi_0\) by Fourier inversion, and the transform of a product is the convolution of the transforms. Since \(\widehat\psi\) is smooth with compact support, repeated integration by parts in \(\psi(x)=\int\widehat\psi(y)e(xy)\,dy\) gives \(|\psi(x)|\ll_j(1+|x|)^{-j}\) for every \(j\), and the same for all derivatives.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 3: Proposition 3.1, the biased block, the amplified moment, (3.6)–(3.12), and Corollary 3.2. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
