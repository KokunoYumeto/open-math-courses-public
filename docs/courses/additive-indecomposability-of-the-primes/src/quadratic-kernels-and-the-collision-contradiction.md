# Quadratic kernels and the collision contradiction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 5 produced a large set \(\mathcal P_0\) of primes and a rational number \(h/m\) with \(t_p\equiv h\overline m\pmod p\) for \(p\in\mathcal P_0\). The bias hypothesis becomes a statement about the single integer sequence \(mx-h\): on average over \(p\in\mathcal P_0\), the quadratic character \(\chi_p(mx-h)\) leans one way on the tail \(A_X\) and the other way on \(D_X\). This lesson finishes the proof of the quadratic decorrelation theorem (Theorem 1.1 of Lesson 3). Write \(mx-h=u_xt_x^2\) with \(u_x\) squarefree. Heath-Brown's quadratic large sieve shows that a positive proportion of each tail has very few *kernels* \(u_x\) (Section 2). Exclusion makes the prime factors of kernels on the two sides disjoint (Section 3). Choosing one kernel on each side, the corresponding square roots \(t_x\) avoid each other modulo every prime \(p\) at which \(vw\) is a square. The zero-free region of Dirichlet \(L\)-functions, with Page's and Siegel's theorems, gives enough such primes (Section 4), and the collision estimate then fails (Section 5).

**Prerequisites.** [*A common centre for the quadratic biases*](a-common-centre-for-the-quadratic-biases.md), Proposition 4.2; [*Zero-free regions and the exceptional zero*](course:NT-DIRL/NT-DIRL-07), Lemma 1.1; [*Siegel's theorem*](course:NT-DIRL/NT-DIRL-10), Theorem 5.2; [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17), Section 1; [*Dirichlet characters*](course:NT-DIRL/NT-DIRL-01), Theorem 4.1; [*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields), Theorem 12.5.

The notation of Lessons 3–5 is in force. In particular \(c_\delta>0\), \(k\asymp T^{3/5}\), \(Z^{k-12}<X\le Z^{k-10}\), and \(\mathcal P_0,h,m,J_0\) are as in Proposition 4.2 of Lesson 5.

## 1. The quadratic large sieve

For odd positive \(m\) and integers \(n\) the Jacobi symbol \((n/m)\) is defined as in Lesson 4. A sum marked \(\sum^\flat\) runs over positive odd squarefree integers.

**Theorem 1.1** (Heath-Brown's quadratic large sieve; named result N1 [HB, Theorem 1]). For positive integers \(M,N\), complex numbers \(a_n\) and every \(\varepsilon>0\),
\[
\begin{aligned}
&\sideset{}{^\flat}\sum_{m\le M}\Bigl|\sideset{}{^\flat}\sum_{n\le N}a_n\Bigl(\frac nm\Bigr)\Bigr|^2\\
&\quad \ll_\varepsilon(MN)^\varepsilon(M+N)\sideset{}{^\flat}\sum_{n\le N}|a_n|^2 .
\end{aligned}
\]

The programme does not prove this theorem; it is used here as a named result. Its point is the factor \(M+N\): bounding each inner sum by Cauchy–Schwarz would give \(MN\), and the orthogonality of the characters \(m\mapsto(n/m)\) for different squarefree \(n\) gives only \(M+N^2\) with elementary means.

**Lemma 1.2** (Jacobi reciprocity). For odd positive coprime \(v,s\),
\[
\Bigl(\frac vs\Bigr)\Bigl(\frac sv\Bigr)=(-1)^{\frac{v-1}2\cdot\frac{s-1}2}.
\]

*Proof.* For distinct odd primes this is quadratic reciprocity ([*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields), Theorem 12.5). Both sides are multiplicative in \(v\) and in \(s\): for the right side, \(\frac{ab-1}2\equiv\frac{a-1}2+\frac{b-1}2\pmod2\) for odd \(a,b\), because the difference is \(\frac{(a-1)(b-1)}2\), an even number. Factor \(v\) and \(s\) into primes. \(\square\)

**Corollary 1.3** (signed kernels [OpenAI-013, Section 3]). Let \(b_s\) be complex numbers supported on positive odd squarefree \(s\le S\). For \(U\ge1\) and every \(\varepsilon>0\),
\[
\begin{aligned}
&\sum_{\substack{0<|u|\le U\\ u\ \text{squarefree}}}\Bigl|\sum_sb_s\Bigl(\frac us\Bigr)\Bigr|^2\\
&\quad \ll_\varepsilon(US)^\varepsilon(U+S)\sum_s|b_s|^2 ,
\end{aligned}
\]
where \(u\) runs over signed squarefree integers and \((u/s)\) is the Jacobi symbol.

*Proof.* Write \(u=\pm2^ev\) with \(e\in\{0,1\}\) and \(v\) positive, odd and squarefree, and split the sum into the eight classes given by the sign, \(e\), and \(v\bmod4\). In a class, \((u/s)=(\pm1/s)(2/s)^e(v/s)\). If \((v,s)>1\), both \((v/s)\) and \((s/v)\) vanish; otherwise Lemma 1.2 gives \((v/s)=(s/v)\epsilon_s\), where \(\epsilon_s=1\) if \(v\equiv1\pmod4\) and \(\epsilon_s=(-1)^{(s-1)/2}\) if \(v\equiv3\pmod4\). In a fixed class, \(b'_s=b_s(\pm1/s)(2/s)^e\epsilon_s\) does not depend on \(v\), and \(|b'_s|=|b_s|\) or \(0\). So the class contributes at most \(\sum^\flat_{v\le U}|\sum_sb'_s(s/v)|^2\), and Theorem 1.1 with \(M=\lfloor U\rfloor\), \(N=\lfloor S\rfloor\) bounds this by \(O_\varepsilon((US)^\varepsilon(U+S)\sum|b_s|^2)\). \(\square\)

## 2. Few kernels carry the bias

For \(p\in\mathcal P_0\) put \(\epsilon'_p=\epsilon_p\chi_p(m)\). Since \(t_p\equiv h\overline m\pmod p\) and \(\chi_p(\overline m)=\chi_p(m)\),
\[
\epsilon_p\chi_p(x-t_p)=\epsilon'_p\,\chi_p(mx-h).
\]
Define
\[
F(x)=\frac1{J_0}\sum_{p\in\mathcal P_0}\epsilon'_p\,\chi_p(mx-h).
\]
By (2.1) of Lesson 3, \(F\) has mean at least \(c_\delta\) on \(A_X\) and at most \(-c_\delta\) on \(D_X\). Since \(|F|\le1\), at least a proportion \(c_\delta/2\) of the elements of \(A_X\) satisfy \(F(x)\ge c_\delta/2\), and likewise for \(D_X\) with \(F(x)\le-c_\delta/2\). Call these the *biased elements* of the two tails. For a biased \(x\), \(mx-h\ne0\), and we write
\[
\begin{gathered}
mx-h=u_xt_x^2,\\
u_x\ \text{signed squarefree},\\
t_x\ge1.\quad(2.1)
\end{gathered}
\]
The integer \(u_x\) is the *kernel* of \(x\). Since \(|h|\le XZ^{0.15}\) and \(m\le Z^{0.13}\), \(|u_x|t_x^2\le mX+|h|=X^{1+o(1)}\).

**Lemma 2.1.** For every fixed \(\varepsilon>0\), the biased elements of either tail have at most \(X^{2\varepsilon+o(1)}\) distinct kernels.

*Proof.* *Kernels instead of the full values.* A prime of \(\mathcal P_0\) dividing \(t_x\) satisfies \(p\ge Z\), and the product of such primes is at most \(t_x\le X^{1/2+o(1)}\), so there are at most \(k\) of them. For the other primes, \(\chi_p(mx-h)=\chi_p(u_x)\chi_p(t_x)^2=\chi_p(u_x)\). Hence \(F_1(x)=J_0^{-1}\sum_{p\in\mathcal P_0}\epsilon'_p\chi_p(u_x)\) differs from \(F(x)\) by at most \(2k/J_0=o(1)\), and \(|F_1(x)|\ge c_\delta/3\) at every biased \(x\), for large \(T\).

*A single array.* Apply Lemma 4.1 of Lesson 3 to the \(J_0\) numbers \(y_p=\epsilon'_p\chi_p(u_x)\), whose mean is \(F_1(x)\). Its error terms satisfy \(\bigl(k^5/J_0\bigr)^j|F_1(x)|^{k-2j}\)\(\le|F_1(x)|^k\bigl(9k^5/(c_\delta^2J_0)\bigr)^j\), and \(k^5/J_0=o(1)\) because \(J_0\ge JZ^{-O(1/k)}\). So
\[
\begin{aligned}
&\Bigl|\frac1{J_0^k}\sum_{\text{distinct}}\prod_{i=1}^k\epsilon'_{p_i}\chi_{p_i}(u_x)\Bigr|\\
&\quad \ge\tfrac12|F_1(x)|^k\ge c^k,
\end{aligned}
\]
with a constant \(c>0\) depending only on \(\delta\). Group the ordered tuples by their product \(s\), a product of \(k\) distinct primes of \(\mathcal P_0\), and note \(\prod_{p\mid s}\chi_p(u)=(u/s)\). The left side is \(|\sum_sb_s(u_x/s)|\) with the single array
\[
\begin{gathered}
b_s=k!\,J_0^{-k}\prod_{p\mid s}\epsilon'_p,\\
\sum_s|b_s|^2=\binom{J_0}k\frac{(k!)^2}{J_0^{2k}}\le\frac{k!}{J_0^k},
\end{gathered}
\]
the same for every biased \(x\) on either side.

*Counting kernels.* The array is supported on odd squarefree \(s\le S=(2Z)^k\). Then \(S=X^{1+o(1)}\), because \(Z^k\le XZ^{12}\) and \(2^k=Z^{o(1)}\), and
\[
\begin{aligned}
S\,\frac{k!}{J_0^k}&\le\Bigl(\frac{2Zk}{J}\Bigr)^kZ^{O(1)}\\
&\le\exp\bigl(O(k\log T+\log Z)\bigr)\\
&=X^{o(1)},
\end{aligned}
\]
since \(J\gg Z/\log Z\). Apply Corollary 1.3 with \(U=mX+|h|=X^{1+o(1)}\). Each distinct kernel of a biased element contributes at least \(c^{2k}=X^{-o(1)}\) to the left side, which is at most \(X^{2\varepsilon+o(1)}\). \(\square\)

**Lemma 2.2** (kernel populations). For a signed squarefree \(u\ne0\),
\[
\begin{aligned}
&\#\{x\ \text{biased on a fixed side}:u_x\\
&\quad =u\}\ll\sqrt{X/|u|}+X^{o(1)}.
\end{aligned}
\]

*Proof.* Since \((h,m)=1\), a prime dividing \(m\) and \(ut_x\) would divide \(mx-h\) and hence \(h\); so \((ut_x,m)=1\), and \(t_x\) is a root of \(ut^2\equiv-h\pmod m\) with \(u\) a unit. A unit has at most two square roots modulo an odd prime power and at most four modulo a power of \(2\), so there are at most \(2^{\omega(m)+1}\) residues for \(t_x\). On one side \(x\) lies in an interval of length at most \(X\), so \(t_x^2\) lies in an interval of length at most \(mX/|u|\), and \(t_x\) in an interval of length at most \(\sqrt{mX/|u|}\), because \(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\) for \(a,b\ge0\). The map \(x\mapsto t_x\) is injective for fixed \(u\). So the count is at most \(2^{\omega(m)+1}\bigl(\sqrt{mX/|u|}/m+1\bigr)\). Finally \(2^{\omega(m)}\ll\sqrt m\), because in \(\prod_{p\mid m}2/\sqrt p\) only the factors at \(2\) and \(3\) exceed \(1\), and \(2^{\omega(m)}=X^{o(1)}\) since \(m=X^{o(1)}\). \(\square\)

## 3. Small kernels with disjoint prime supports

**The constants.** By [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17), (1.1), there is an absolute \(a_0>0\) such that, for \(Q\ge2\), the box \(\Re s>1-a_0/\log(2Q)\), \(|\Im s|\le Q\) contains at most one zero of all the Dirichlet \(L\)-functions of primitive characters of conductor at most \(Q\); if it exists, it is a simple real zero of a real nonprincipal character. Put \(c_z=\min(a_0/2,1/4)\) and \(C_z=1+c_z^{-1}\ge5\). Then for \(Q\ge2\), among primitive nonprincipal characters of conductor at most \(Q\), every zero \(\rho\) with \(|\Im\rho|\le1\) satisfies
\[
\Re\rho\le1-\frac{c_z}{\log Q},
\tag{3.1}
\]
with at most one exception, a simple real zero of a real character. Fix, in this order,
\[
\begin{gathered}
0<\eta\le\min\Bigl(\frac1{1000},\frac1{200C_z}\Bigr),\\
0<\varepsilon<\frac\eta{100}.
\end{gathered}
\]

**Small kernels.** By Lemmas 2.1 and 2.2, the biased elements whose kernels satisfy \(|u_x|>X^\eta\) number at most
\[
\begin{aligned}
&X^{2\varepsilon+o(1)}\bigl(X^{1/2-\eta/2}+X^{o(1)}\bigr)\\
&\quad =o\bigl(\sqrt X/(\log X)^3\bigr)
\end{aligned}
\]
on each side, since \(2\varepsilon<\eta/2\). Discarding them leaves sets \(\mathcal U\subseteq A_X\) and \(\mathcal V\subseteq D_X\) of biased elements, each of size \(\gg_\delta\sqrt X/(\log X)^3\), all of whose kernels satisfy \(0<|u_x|\le X^\eta\).

**Lemma 3.1** (disjoint supports). No prime divides both a kernel \(u_x\) with \(x\in\mathcal U\) and a kernel \(u_y\) with \(y\in\mathcal V\).

*Proof.* Let \(\ell\) be such a prime. Then \(\ell\) divides \(mx-h\) and \(my-h\), hence \(m(x-y)\); since \((u_x,m)=1\), \(\ell\nmid m\), so \(\ell\mid x-y\). Here \(x-y=x+b\) with \(b=-y\in B\), so \(x-y\in A+B\) and \(x-y\ge2X^{9/10}>N\); by exclusion \(x-y\) is a prime. But \(\ell\le|u_x|\le X^\eta<x-y\), so the prime \(x-y\) has a smaller prime divisor, which is impossible. \(\square\)

So for kernels \(v\) of \(\mathcal U\) and \(w\) of \(\mathcal V\), the product \(vw\) is signed squarefree, and its prime factors determine \(|v|\) and \(|w|\): \(|v|\) is the product of those prime factors of \(vw\) that divide some kernel of \(\mathcal U\). Only the signs of \(v\) and \(w\) remain undetermined, four possibilities in all.

**Removing a possible exceptional character.** Put \(Q_0=4X^{2\eta}\). For a pair \(x\in\mathcal U\), \(y\in\mathcal V\) with kernels \(v,w\) and \(vw\ne1\), let \(\chi_{vw}\) be the Kronecker symbol of the discriminant of \(\mathbb Q(\sqrt{vw})\); by [*Dirichlet characters*](course:NT-DIRL/NT-DIRL-01), Theorem 4.1, it is a real primitive character, of conductor at most \(4|vw|\le Q_0\). For odd primes \(p\nmid vw\), \(\chi_{vw}(p)=(vw/p)\). Apply (3.1) with \(Q=Q_0\). If the exceptional zero exists and belongs to a character of conductor \(q>(\log X)^{100}\), discard every pair \((x,y)\) whose character \(\chi_{vw}\) is that character. That character determines \(vw\), hence \(v\) and \(w\) up to four sign choices, with \(|vw|\ge q/4\). By Lemma 2.2 the discarded pairs number
\[
\begin{aligned}
&\ll\Bigl(\sqrt{\tfrac X{|v|}}+X^{o(1)}\Bigr)\Bigl(\sqrt{\tfrac X{|w|}}\\
&\qquad +X^{o(1)}\Bigr)\\
&\quad \ll\frac X{\sqrt{|vw|}}+X^{1/2+o(1)}\\
&\quad \ll\frac X{(\log X)^{50}},
\end{aligned}
\]
which is negligible against \(|\mathcal U||\mathcal V|\gg_\delta X/(\log X)^6\).

**Two populous kernels.** There are at most \(4X^{2\eta}\) ordered pairs of signed kernels of absolute value at most \(X^\eta\). Among the remaining pairs \((x,y)\), pigeonholing gives kernels \(v,w\) such that the populations \(\mathcal U_v=\{x\in\mathcal U:u_x=v\}\) and \(\mathcal V_w=\{y\in\mathcal V:u_y=w\}\) satisfy
\[
|\mathcal U_v|\,|\mathcal V_w|\gg_\delta\frac{X^{1-2\eta}}{(\log X)^6}.
\]
By Lemma 2.2 each population is \(O(\sqrt X)\), so each is at least \(X^{1/2-3\eta}\) for large \(T\). Let \(\mathcal R_1=\{t_x:x\in\mathcal U_v\}\) and \(\mathcal R_2=\{t_y:y\in\mathcal V_w\}\). The maps \(x\mapsto t_x\) are injective, so \(|\mathcal R_1|=|\mathcal U_v|\) and \(|\mathcal R_2|=|\mathcal V_w|\), and both sets of positive integers have diameter at most \(X^{1/2+o(1)}\).

## 4. Many split primes

Put \(Q_2=X^{1/2-5\eta}\).

**Proposition 4.1** ([OpenAI-013, (3.32)]). For large \(T\),
\[
\begin{aligned}
&\sum_{\substack{p\le Q_2,\ p\nmid2mvw\\ (vw/p)=1}}\frac{\log p}p\\
&\quad \ge0.03\log X.\quad(4.1)
\end{aligned}
\]

*Proof.* *The case \(vw=1\).* Mertens' estimate gives \(\sum_{p\le Q_2}(\log p)/p\)\(=(\frac12-5\eta)\log X+O(1)\). The primes dividing \(2m\) have total weight \(O(\log\log X)\), since \(m=X^{o(1)}\): those up to \(\log X\) have weight \(O(\log\log X)\) by Mertens' estimate, and those above \(\log X\) have weight at most \(\log(2m)/\log X=o(1)\). The claim follows.

*The case \(vw\ne1\).* Let \(\chi=\chi_{vw}\), of conductor \(q\le Q_0\), and put
\[
s=1+\frac{10}{\log X},\qquad s_0=1+\frac1{\log Q_0}.
\]
Since \(\log Q_0=2\eta\log X+\log4\le\frac1{10}\log X\) for large \(X\), we have \(1<s\le s_0\le2\).

*The Hadamard formula.* By [*Zero-free regions and the exceptional zero*](course:NT-DIRL/NT-DIRL-07), (1.3), for real \(1<u\le2\),
\[
\begin{aligned}
&\sum_\rho\frac{u-\beta}{(u-\beta)^2+\gamma^2}=\frac{L'}L(u,\chi)\\
&\qquad +\frac12\log q+O(1),\quad(4.2)
\end{aligned}
\]
where \(\rho=\beta+i\gamma\) runs over the nontrivial zeros with multiplicity; the Gamma term is bounded on this interval. Every term on the left is positive.

*At \(s_0\).* The Dirichlet series of \(L'/L\) gives \(|L'/L(s_0,\chi)|\le-\zeta'/\zeta(s_0)\)\(=\log Q_0+O(1)\), so the zero sum at \(s_0\) is at most \(2\log Q_0\) for large \(X\).

*From \(s_0\) to \(s\).* Let \(\rho=\beta+i\gamma\) be a zero other than the possible exceptional zero, and put \(a=s-\beta\), \(b=s_0-\beta\), so \(0<a\le b<2\). The ratio of its terms at \(s\) and at \(s_0\) is
\[
\frac{a}{b}\cdot\frac{b^2+\gamma^2}{a^2+\gamma^2}.
\]
If \(|\gamma|\le1\), then \(a\ge c_z/\log Q_0\) by (3.1) and \(b-a\le1/\log Q_0\), so the ratio is at most \(b/a\le1+c_z^{-1}=C_z\). If \(|\gamma|>1\), the ratio is at most \((4+\gamma^2)/\gamma^2\le5\le C_z\). Summing, the nonexceptional zeros contribute at most \(2C_z\log Q_0\) to (4.2) at \(u=s\).

*The possible exceptional zero.* If \(\chi\) has the exceptional zero \(\beta_1\), its conductor is at most \((\log X)^{100}\), since the other case was discarded. By Siegel's theorem in the form [*Siegel's theorem*](course:NT-DIRL/NT-DIRL-10), Theorem 5.2, with exponent \(1/200\), \(1-\beta_1\ge c_0q^{-1/200}\), so its term at \(s\) is at most \(1/(1-\beta_1)\ll q^{1/200}\)\(\le(\log X)^{1/2}=o(\log X)\). The constant \(c_0\) is ineffective, which is harmless: only the existence of a bound is used.

*The signed prime sum.* Removing the prime powers \(p^j\), \(j\ge2\), which contribute \(O(1)\), (4.2) gives
\[
\begin{aligned}
&\sum_p\frac{\chi(p)\log p}{p^s}\\
&\quad =-\frac{L'}L(s,\chi)+O(1)\\
&\quad \ge-2C_z\log Q_0-o(\log X).\quad(4.3)
\end{aligned}
\]

*The unsigned prime sums.* By Mertens' estimate and partial summation,
\[
\begin{gathered}
\begin{aligned}
\sum_p\frac{\log p}{p^s}&=\frac1{s-1}+O(1)\\
&=\frac{\log X}{10}+O(1),
\end{aligned}\\
\begin{aligned}
\sum_{p>Q_2}\frac{\log p}{p^s}&=\frac{Q_2^{-(s-1)}}{s-1}+O(1)\\
&=\frac{e^{-5+50\eta}}{10}\log X+O(1).
\end{aligned}
\end{gathered}
\]

*Combination.* As in the first case, the primes dividing \(2mvw\) have weight \(O(\log\log X)\). For \(p\nmid2mvw\), \(\chi(p)=(vw/p)\in\{\pm1\}\) and \(\mathbf 1_{(vw/p)=1}=(1+\chi(p))/2\). Therefore the left side of (4.1), with \(p^s\) in place of \(p\), is at least
\[
\begin{aligned}
&\frac12\sum_{p\le Q_2}\frac{(1+\chi(p))\log p}{p^s}\\
&\qquad -O(\log\log X)
\ge\Bigl(0.05-2C_z\eta\\
&\qquad -0.1e^{-5+50\eta}-o(1)\Bigr)\log X,
\end{aligned}
\]
using \(\log Q_0=2\eta\log X+O(1)\) and bounding the tail \(\sum_{p>Q_2}\chi(p)\log p/p^s\) by the unsigned tail. By the choice of \(\eta\), \(2C_z\eta\le0.01\) and \(0.1e^{-5+50\eta}<0.001\), so the coefficient exceeds \(0.03\) for large \(X\). Replacing \(p^s\) by \(p\) only increases the sum. \(\square\)

## 5. The collision contradiction

For \(i=1,2\) and a prime \(p\), let \(\beta_i(p)\) be the probability that two independent uniform elements of \(\mathcal R_i\) are congruent modulo \(p\).

**Upper bound.** For unequal elements of \(\mathcal R_i\), the primes dividing their difference have product at most the diameter \(X^{1/2+o(1)}\). Equal elements have probability \(1/|\mathcal R_i|\le X^{-1/2+3\eta}\), and then the primes up to \(Q_2\) contribute \(O(Q_2)=O(X^{1/2-5\eta})\). As in (2.1) of Lesson 2,
\[
\begin{aligned}
&\sum_{p\le Q_2}\log p\,\bigl(\beta_1(p)+\beta_2(p)\bigr)\\
&\quad \le(1+o(1))\log X.\quad(5.1)
\end{aligned}
\]

**Lower bound.** Always \(\beta_i(p)\ge1/p\), by Cauchy–Schwarz over the residue classes. Let \(p\) be a prime counted in (4.1). Then \(p\nmid vw\) and \((vw/p)=1\), so \(w\overline v\) is a nonzero square modulo \(p\); choose \(c_p\) with \(c_p^2\equiv w\overline v\pmod p\). *The residues of \(\mathcal R_1\) and of \(c_p\mathcal R_2\) modulo \(p\) are disjoint.* Indeed, \(t_x\equiv c_pt_y\pmod p\) would give \(vt_x^2\equiv wt_y^2\), that is \(mx-h\equiv my-h\pmod p\), so \(p\mid m(x-y)\). Since \(p\nmid m\), \(p\mid x-y\); but \(x-y\) is a prime larger than \(X^{9/10}>Q_2\ge p\), as in Lemma 3.1. Let the two residue sets have \(a_p\) and \(b_p\) elements, so \(a_p+b_p\le p\). Multiplication by the unit \(c_p\) does not change the collision probability of \(\mathcal R_2\), so
\[
\begin{aligned}
&\beta_1(p)+\beta_2(p)\ge\frac1{a_p}+\frac1{b_p}\\
&\quad \ge\frac4{a_p+b_p}\ge\frac4p.
\end{aligned}
\]
Hence, by Mertens' estimate and (4.1),
\[
\begin{aligned}
&\sum_{p\le Q_2}\log p\,\bigl(\beta_1(p)+\beta_2(p)\bigr)\\
&\quad\ge2\sum_{p\le Q_2}\frac{\log p}p+2\sum_{p\ \text{in (4.1)}}\frac{\log p}p\\
&\quad\ge(1-10\eta+0.06-o(1))\log X.
\end{aligned}
\]
Since \(10\eta\le0.01\), this contradicts (5.1) for large \(T\).

The contradiction shows that the bias hypothesis of Section 2 of Lesson 3 fails, which proves Theorem 1.1 of Lesson 3, and with it Corollary 1.2 of Lesson 3. \(\square\)

## 6. What the proof used

The collision estimate enters twice: in Lesson 2, to make the empirical means over the tails close to the uniform means over \(S_p\), and in Section 5, through the congruent-pair count for the sets of square roots. Exclusion enters three times: in the definition of \(S_p\), in Lemma 3.1, and in Section 5, always in the form *a difference \(x-y\) of a large element of \(A\) and an element of \(D\) is a prime, so it has no small prime factor*. Coverage enters Lessons 3–6 only through the lower bounds for \(|A_X|\) and \(|D_X|\) from Lesson 2. Lessons 10 and 11 use it in an essential way: there every large prime, not just a dense set of them, must be a difference \(a-d\).

## 7. Exercises

**7.1.** Show that for odd positive \(a,b\), \(\frac{ab-1}2-\frac{a-1}2-\frac{b-1}2=\frac{(a-1)(b-1)}2\), and that this number is even.

**7.2.** Let \(u\ne0\) be a signed squarefree integer and \(m\ge1\) with \((u,m)=1\). Show that \(ut^2\equiv c\pmod m\) has at most \(2^{\omega(m)+1}\) solutions \(t\bmod m\) when \(c\) is a unit, and give an example with exactly \(2^{\omega(m)+1}\) solutions.

**7.3.** In Proposition 4.1, check the two numerical inequalities \(2C_z\eta\le0.01\) and \(0.1e^{-5+50\eta}<0.001\) for \(\eta\le\min(1/1000,1/(200C_z))\).

**7.4.** Show that for \(0<a\le b\) and real \(\gamma\), \(\frac{a}{b}\cdot\frac{b^2+\gamma^2}{a^2+\gamma^2}\le\frac ba\).

## 8. Solutions

**7.1.** Expand: \(ab-1-(a-1)-(b-1)\)\(=ab-a-b+1=(a-1)(b-1)\). For odd \(a,b\), both \(a-1\) and \(b-1\) are even, so \((a-1)(b-1)\) is divisible by \(4\) and its half is even.

**7.2.** Since \(u\) is a unit, the congruence is \(t^2\equiv c\overline u\), with a unit right side. By the Chinese remainder theorem the count is the product over prime powers \(p^e\parallel m\). For odd \(p\) the units modulo \(p^e\) form a cyclic group, in which a square has exactly two square roots. Modulo \(2^e\) a unit has at most four square roots (the group is \(\{\pm1\}\times\) cyclic for \(e\ge3\), and has order at most \(2\) for \(e\le2\)). So the number is at most \(2^{\omega(m)}\cdot2\). Example: \(m=8\), \(c=u=1\): \(t\in\{1,3,5,7\}\), four solutions, and \(2^{\omega(8)+1}=4\).

**7.3.** \(2C_z\eta\le2C_z/(200C_z)=0.01\). And \(50\eta\le0.05\), so \(0.1e^{-5+50\eta}\le0.1e^{-4.95}\)\(<0.1\cdot0.0071<0.001\).

**7.4.** Since \(b\ge a>0\), \((b^2+\gamma^2)/(a^2+\gamma^2)\le b^2/a^2\): cross-multiplying, \(a^2b^2+a^2\gamma^2\le a^2b^2+b^2\gamma^2\). Multiply by \(a/b\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 3: the quadratic large sieve and the number of kernels, populations in a kernel and disjoint prime supports, exceptional characters and split primes, (3.31)–(3.32), and the final collision contradiction. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [HB] D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), no. 3, 235–275, Theorem 1. http://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf
