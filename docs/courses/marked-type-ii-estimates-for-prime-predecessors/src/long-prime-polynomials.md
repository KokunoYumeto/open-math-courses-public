# Long prime polynomials

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves cancellation in \(\sum_{p\in I}\chi(p)p^{-1+it}\) for primes in an interval of length comparable to a fixed power of \(x\), at every height \(L^{B_0}\le|t|\le x^2\), and for characters of modulus up to a power of \(L\). The proof smooths the interval, writes the smoothed sum as a Mellin integral of \(-D'/D\), and moves the contour into the zero-free strip of [*A zero-free strip at large height*](a-zero-free-strip-at-large-height.md). The second part of the lesson combines this estimate with the results of Lessons 2 and 3 to show that the prime-minus-rough coefficient of [*The marked Type II estimate*](the-marked-type-ii-estimate.md) has twisted cancellation. This reduces Theorem 2.3 of that lesson to Theorem 2.2.

**Prerequisites.** [*A zero-free strip at large height*](a-zero-free-strip-at-large-height.md), Theorem 4.1 and (4.1); [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemmas 1.1, 1.2, 4.1 and 4.2; [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), Corollary 4.1 and Lemma 4.2; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4; [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01), Lemma A.2.

We keep \(L=\log x\), \(T=\log L\), and write \(D(s,\chi)\) for Dirichlet \(L\)-functions.

## 1. Prime polynomials

**Theorem 1.1 (long prime polynomials).** Fix \(0<\tau\le1\), \(C_0>0\) and \(A>0\), and put \(B_0=A+8\). For large \(x\), uniformly for

\[
\begin{gathered}
\frac{x^\tau}2\le N\le x^{1/\tau},\qquad q\le L^{C_0},\\
L^{B_0}\le|t|\le x^2,
\end{gathered}
\]

every Dirichlet character \(\chi\) modulo \(q\) and every interval \(I\subseteq[N,2N]\),

\[
\begin{gathered}
\Bigl|\sum_{p\in I}\chi(p)\,p^{-1+it}\Bigr|\le C\,L^{-A},\quad(1.1)
\end{gathered}
\]

with \(C\) depending on \(\tau,C_0,A\).

**Proof.** *Smoothing.* Let \(I=[N\xi_1,N\xi_2]\) with \(1\le\xi_1\le\xi_2\le2\); open or half-open intervals differ by at most two primes, each contributing \(O(1/N)\). Put \(\delta=L^{-A-4}\), fix a smooth nonnegative function \(\phi\) supported in \([-1,1]\) with integral \(1\), and let \(g=\mathbf 1_{[\xi_1,\xi_2]}*\phi_\delta\) with \(\phi_\delta(y)=\delta^{-1}\phi(y/\delta)\). Then \(0\le g\le1\), \(g\) is supported in \([\frac12,3]\), \(g(y)=\mathbf 1_{[\xi_1,\xi_2]}(y)\) unless \(y\) is within \(\delta\) of \(\xi_1\) or \(\xi_2\), and \(|g^{(j)}|\le\int|\phi_\delta^{(j)}|\ll_j\delta^{-j}\). Since \(\Lambda(n)\le\log(3N)\) and \(n\ge N/2\) on the support,

\[
\begin{aligned}
&\sum_n\frac{\Lambda(n)}n\bigl|\mathbf 1_I(n)-g(n/N)\bigr|\\
&\quad\le2(2\delta N+1)\frac{2\log(3N)}N\\
&\quad\ll L^{-A-2}.\quad(1.2)
\end{aligned}
\]

*Mellin transform.* Let \(\widehat g(z)=\int_0^\infty g(w)w^{z-1}dw\), an entire function. For \(|\operatorname{Re}z|\le1\), \(|\widehat g(z)|\le\int_{1/2}^3\max(w^{-2},1)\,dw\le3\), and \(j\) integrations by parts give

\[
\begin{gathered}
\widehat g(z)=\frac{(-1)^j}{z(z+1)\cdots(z+j-1)}\\
\times\int_0^\infty g^{(j)}(w)w^{z+j-1}dw,\\
|\widehat g(u+iv)|\ll_j\delta^{-j}(1+|v|)^{-j}\\
(|u|\le1).\quad(1.3)
\end{gathered}
\]

Fourier inversion in the variable \(\log w\) (Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), for the smooth compactly supported function of Exercise 6.2) gives \(g(w)=\frac1{2\pi i}\int_{(c)}\widehat g(z)w^{-z}dz\) for every real \(c\), the integral converging absolutely by (1.3). With \(c=1/L\) and absolute convergence of the Dirichlet series,

\[
\begin{aligned}
&\sum_n\Lambda(n)\chi(n)n^{-1+it}g(n/N)\\
&\quad=\frac1{2\pi i}\int_{(1/L)}\widehat g(z)N^z\\
&\qquad\times\Bigl(-\frac{D'}D(1-it+z,\chi)\Bigr)dz.\quad(1.4)
\end{aligned}
\]

On the line \(\operatorname{Re}z=1/L\), \(|D'/D(1+1/L+iu,\chi)|\)\(\le-\zeta'/\zeta(1+1/L)\le L+C_\zeta\) by (4.1) of the previous lesson, and \(|N^z|\le e^{1/\tau}\).

*Truncation.* Let \(H_0=L^{A+6}\) and \(j=\lceil A\rceil+5\). By (1.3), the parts of (1.4) with \(|\operatorname{Im}z|>H_0\) are at most a constant times

\[
\begin{gathered}
L\,\delta^{-j}\int_{H_0}^\infty v^{-j}\,dv\\
\ll L^{1+j(A+4)-(j-1)(A+6)}\\
=L^{A+7-2j},
\end{gathered}
\]

which is \(O(L^{-A-2})\).

*Contour shift.* Put \(w_0=cT^2/(2L)\), with \(c\) from Theorem 4.1 of the previous lesson for the modulus bound \(L^{C_0}\). For \(z\) in the rectangle \(-w_0\le\operatorname{Re}z\le1/L\), \(|\operatorname{Im}z|\le H_0\), the point \(s=1-it+z\) satisfies

\[
\begin{gathered}
1-w_0\le\operatorname{Re}s\le1+\frac1L,\\
2\le|t|-H_0\le|\operatorname{Im}s|\le x^2+H_0\le\frac{x^3}2,
\end{gathered}
\]

because \(|t|\ge L^{A+8}\). By Theorem 4.1 of the previous lesson, \(D(s,\chi)\) has no zero there, \(s\ne1\), and \(|D'/D(s,\chi)|\le CL\). Cauchy's theorem (Lemma A.2 of [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01), for the rectangle, on a neighbourhood of which the integrand is holomorphic) moves the segment \([1/L-iH_0,1/L+iH_0]\) to \([-w_0-iH_0,-w_0+iH_0]\) plus two horizontal edges. The edges have length at most \(2w_0\le1\), and on them \(|\widehat g|\ll_j\delta^{-j}H_0^{-j}\) and \(|N^z|\le e^{1/\tau}\); with the same \(j\) they contribute \(O(L^{-A-2})\). On the new vertical segment,

\[
\begin{gathered}
|N^z|=N^{-w_0}\le2\exp\Bigl(-\frac{c\tau T^2}2\Bigr)\\
=2L^{-c\tau T/2},
\end{gathered}
\]

because \(\log N\ge\tau L-\log2\); with \(|\widehat g|\le3\), \(|D'/D|\le CL\) and length \(2H_0\), it contributes \(O(L^{A+7-c\tau T/2})\), which is \(O(L^{-A-2})\) for large \(x\).

*From \(\Lambda\) to primes.* Together with (1.2) we obtain \(|\sum_{n\in I}\Lambda(n)\chi(n)n^{-1+it}|\ll L^{-A-2}\) for every interval \(I\subseteq[N,2N]\). Prime powers \(p^m\in[N,2N]\) with \(m\ge2\) number at most \(\sqrt{2N}\log_2(2N)\), and each contributes at most \(\log(2N)/N\); so they change the sum by \(O(N^{-1/2}L^2)\). Finally, Lemma 4.2 of [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md) with \(g(y)=1/\log y\), for which \(\sup+\text{variation}\le2/\log N\le4/(\tau L)\), removes the weight \(\log p\) and proves (1.1). \(\square\)

At heights \(|t|\le L^{B_0}\) no such bound can hold for the principal character: for \(t=0\) the sum over \(N<p\le2N\) is \((\log2+o(1))/\log N\) by Mertens' estimate. In that range the cancellation needed below comes instead from comparing primes with rough integers.

## 2. The prime coefficient

We return to the setting of [*The marked Type II estimate*](the-marked-type-ii-estimate.md): \(\delta>0\) and \(c_*\ge1\) are fixed, \(H_m,H_n\ge x^\delta\) and \(x/c_*\le X=H_mH_n\le c_*x\). Then \(x^\delta\le H_m\le c_*x^{1-\delta}\).

**Proposition 2.1.** Fix \(C>0\). Let \(I\subseteq[H_m,2H_m]\) be an interval, \(|v|\le L^C\), and let \(\alpha\) be the coefficient (2.5) of Lesson 1. For all fixed \(A_0,B,A>0\), every Dirichlet character \(\chi\) of modulus \(k\le L^{A_0}\) and every real \(t\) with \(|t|\le2XL^B\),

\[
\begin{gathered}
\Bigl|\frac1{H_m}\sum_m\alpha_m\chi(m)m^{it}\Bigr|\\
\le C_{\rm tc}L^{-A},\quad(2.1)
\end{gathered}
\]

where \(C_{\rm tc}\) and the threshold for \(x\) depend only on \(\delta,c_*,C,A_0,B,A\).

**Proof.** Put \(u=t+v\). By definition,

\[
\begin{gathered}
\sum_m\alpha_m\chi(m)m^{it}=\Sigma_1-\Sigma_2,\\
\Sigma_1=\sum_{p\in I}\chi(p)p^{iu},\\
\Sigma_2=\frac1{V(W)}\sum_{\substack{m\in I\\ m\ \text{rough}}}\frac{\chi(m)m^{iu}}{\log m}.
\end{gathered}
\]

Let \(B_0=A+8\) be the exponent of Theorem 1.1 for the precision \(A\), and put \(B_2=\max(C+2,B_0+1,A)\).

*Low frequencies: \(|t|\le L^{B_2}\).* Then \(|u|\le2L^{B_2}\). Let \(A'=A+B_2+2\). By (1.2) of Lemma 1.1 of Lesson 2 (with \(\delta_1=\delta/2\)), for every interval \(I'\subseteq I\),

\[
\begin{gathered}
\sum_{p\in I'}\chi(p)=\mathbf 1_{\chi\ \text{principal}}\int_{I'}\frac{dy}{\log y}\\
+O(H_mL^{-A'}).
\end{gathered}
\]

Partial summation against \(y^{iu}\), whose modulus is \(1\) and whose variation on \(I\) is at most \(|u|\), gives

\[
\begin{gathered}
\Sigma_1=\mathbf 1_{\chi\ \text{principal}}\int_I\frac{y^{iu}\,dy}{\log y}\\
+O\bigl(H_mL^{-A'}(1+|u|)\bigr).
\end{gathered}
\]

By Lemma 4.2 of Lesson 2, \(\sum_{m\in I',\,m\ \text{rough}}\chi(m)\)\(=\mathbf 1_{\chi\ \text{principal}}V(W)|I'|\)\(+O(H_mL^{-A'})\) on every \(I'\subseteq I\). Partial summation against \(\phi(y)=y^{iu}/(V(W)\log y)\), with \(\sup|\phi|+V_I(\phi)\ll L^{0.24}(1+|u|)/L\) by Lemma 1.2 of Lesson 2, gives

\[
\begin{gathered}
\Sigma_2=\mathbf 1_{\chi\ \text{principal}}\int_I\frac{y^{iu}\,dy}{\log y}\\
+O\bigl(H_mL^{-A'}(1+|u|)\bigr).
\end{gathered}
\]

The main terms cancel, and \(|\Sigma_1-\Sigma_2|\ll H_mL^{-A'+B_2+1}\le H_mL^{-A}\).

*High frequencies: \(L^{B_2}<|t|\le2XL^B\).* Then \(|u|\ge|t|-L^C\ge|t|/2\ge L^{B_0}\) and \(|u|\le2|t|\le4c_*xL^B\le x^2\) for large \(x\). Theorem 1.1, with \(\tau=\delta\) and \(N=H_m\), gives \(|\sum_{p\in I'}\chi(p)p^{-1+iu}|\ll L^{-A}\) for every interval \(I'\subseteq I\); partial summation against \(g(y)=y\), with \(\sup+\text{variation}\le3H_m\) on \(I\), gives \(|\Sigma_1|\ll H_mL^{-A}\).

For \(\Sigma_2\), let \(T_r(m)=\sum\mu(d)\) over squarefree \(d\mid m\) composed of primes at most \(W\) with at most \(r=\lceil c_1\log L\rceil\) prime factors. As in the proof of Lemma 4.2 of Lesson 2, for \(c_1\) large in terms of \(A\),

\[
\begin{gathered}
\sum_{m\in I}\bigl|\mathbf 1_{m\ \text{rough}}-T_r(m)\bigr|\\
\le2H_m\frac{(\log L)^{r+1}}{(r+1)!}+(W+1)^{r+1}\\
\ll H_mL^{-A-1}.
\end{gathered}
\]

Since \(1/(V(W)\log m)\le L^{0.24}/(\delta L)\cdot2\), replacing the rough indicator by \(T_r\) changes \(\Sigma_2\) by \(O(H_mL^{-A})\). Expanding \(T_r\) and writing \(m=dz\),

\[
\begin{gathered}
\sum_{m\in I}\frac{T_r(m)\chi(m)m^{iu}}{\log m}\\
=\sum_d\mu(d)\chi(d)d^{iu}\sum_{a\bmod k}\chi(a)\\
\times\sum_{\substack{z\in I/d\\ z\equiv a\ (k)}}\frac{z^{iu}}{\log(dz)}.
\end{gathered}
\]

Each \(d\) satisfies \(d\le W^r=x^{o(1)}\), so \(z\) runs over an interval in \([N',2N']\) with \(N'=H_m/d\in[x^{\delta/2},c_*x]\). Corollary 4.1 and Lemma 4.2 of [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), with \(\delta_1=\delta/2\), \(\Lambda_1=2\) and the weight \(1/\log(dz)\), bound the inner sum by \(O\bigl((N'/(kL))(1/|u|+x^{-c})\bigr)\), with \(c=c(\delta)>0\). Summing over the \(k\) residues and over \(d\), with \(\sum_dN'\le H_m\prod_{p\le W}(1+1/p)\)\(\ll H_mL^{0.24}\), and multiplying by \(1/V(W)\le2L^{0.24}\),

\[
\begin{gathered}
|\Sigma_2|\ll H_mL^{0.48-1}\bigl(L^{-B_2}+x^{-c}\bigr)\\
+H_mL^{-A}\ll H_mL^{-A}.
\end{gathered}
\]

This proves (2.1) for all \(|t|\le2XL^B\). The constants depend on \(\delta,c_*,C,A_0,A\), and on \(B\) only through the threshold for \(x\). \(\square\)

**Corollary 2.2.** The coefficient (2.5) of Lesson 1 is supported on rough integers, satisfies \(|\alpha_m|\le2\), and has twisted cancellation in the sense of Definition 2.1 of that lesson, with constants depending only on \(\delta,c_*,C\) and on \(A_0,B,A\). Hence Theorem 2.3 of Lesson 1 follows from Theorem 2.2 there.

**Proof.** The first two assertions are Exercise 5.5 of Lesson 1, and the third is Proposition 2.1. Since \(|\alpha_m|\le2\le L^C\), all hypotheses of Theorem 2.2 hold. \(\square\)

## 3. Exercises

**6.1.** Show that \(g=\mathbf 1_{[\xi_1,\xi_2]}*\phi_\delta\) has the properties used in the proof of Theorem 1.1, including \(|g^{(j)}|\le\delta^{-j}\int|\phi^{(j)}|\).

**6.2.** Derive the inversion formula \(g(w)=\frac1{2\pi i}\int_{(c)}\widehat g(z)w^{-z}dz\) from Fourier inversion for the smooth compactly supported function \(y\mapsto g(e^y)e^{cy}\).

**6.3.** Show that \(\sum_{p^m\in[N,2N],\,m\ge2}\Lambda(p^m)p^{-m}\)\(\ll N^{-1/2}\log^2(2N)\).

**6.4.** Show that \(\sum_{N<p\le2N}1/p=(\log2+o(1))/\log N\), and explain why Theorem 1.1 must exclude bounded \(t\).

**6.5.** In the low-frequency part of the proof of Proposition 2.1, verify the bound \(\sup|\phi|+V_I(\phi)\ll L^{0.24}(1+|u|)/L\) for \(\phi(y)=y^{iu}/(V(W)\log y)\).

## 4. Solutions

**6.1.** Since \(\phi_\delta\ge0\) has integral \(1\) and support \([-\delta,\delta]\), \(g(y)=\int_{\xi_1}^{\xi_2}\phi_\delta(y-w)\,dw\in[0,1]\); it equals \(1\) when \([y-\delta,y+\delta]\subseteq[\xi_1,\xi_2]\) and \(0\) when the two intervals are disjoint. Differentiating under the integral, \(g^{(j)}(y)=\int_{\xi_1}^{\xi_2}\phi_\delta^{(j)}(y-w)\,dw\), whose modulus is at most \(\int|\phi_\delta^{(j)}|=\delta^{-j}\int|\phi^{(j)}|\).

**6.2.** Put \(h(y)=g(e^y)e^{cy}\), smooth with compact support. Its Fourier transform is \(\int h(y)e^{-i\eta y}dy=\widehat g(c-i\eta)\). Fourier inversion gives \(h(y)=\frac1{2\pi}\int\widehat g(c-i\eta)e^{i\eta y}d\eta\); substitute \(z=c-i\eta\) and \(w=e^y\).

**6.3.** For each \(m\ge2\) there are at most \((2N)^{1/m}\le\sqrt{2N}\) primes \(p\) with \(p^m\le2N\), and \(m\le\log_2(2N)\). Each term is at most \(\log(2N)/N\).

**6.4.** Mertens' estimate \(\sum_{p\le y}1/p=\log\log y+M+O(1/\log y)\) gives \(\log\log(2N)-\log\log N\)\(+O(1/\log N)\)\(=\log(1+\log2/\log N)\)\(+O(1/\log N)\). For \(\chi\) principal and \(t=0\) the left side of (1.1) is therefore of exact order \(1/\log N\asymp1/L\), which is not \(O(L^{-A})\) for \(A>1\).

**6.5.** By Lemma 1.2 of Lesson 2, \(1/V(W)\le2L^{0.24}\), and \(\log y\ge\delta L\) on \(I\). So \(|\phi|\le2L^{0.24}/(\delta L)\), and \(|\phi'(y)|\)\(\le(|u|/y)|\phi(y)|+1/(V(W)y\log^2y)\), whose integral over \(I\subseteq[H_m,2H_m]\) is at most \((|u|+1)\cdot2L^{0.24}/(\delta L)\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Lemma 2.3, the proof of Lemma 9.1, and Lemma 5.1. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
