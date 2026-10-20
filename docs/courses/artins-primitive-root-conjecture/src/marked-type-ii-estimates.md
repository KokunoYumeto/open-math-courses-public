# Marked Type II estimates and rough factors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The construction of Lessons 18 and 19 counts integers \(d\) whose predecessor \(d-1\) has a prescribed shape, and then removes the composite \(d\). Both steps require bilinear sums \(\sum_{m,n}\alpha_m\beta_n\,F(mn-1)\mathcal W(mn-1)\) to be small, where \(\mathcal W\) is a weight that marks prime factors of \(mn-1\) from fixed groups of primes. A theorem of OpenAI's companion paper on the Poisson–Dirichlet law for prime predecessors gives this when \(\alpha_m\) is the indicator of primes minus its average over \(W\)-rough numbers. Its proof uses \(\alpha\) only through cancellation against Dirichlet characters of small modulus twisted by \(m^{it}\). This lesson states these two facts as named results and proves the corresponding cancellation for the coefficient that replaces the indicator of \(x^\gamma\)-rough numbers by its density \(D_\gamma(\log m/L)/L\) of [*A block sieve and rough-number densities*](a-block-sieve-and-rough-number-densities.md).

**Prerequisites.** [*A block sieve and rough-number densities*](a-block-sieve-and-rough-number-densities.md), (1.1)–(1.4), Lemma 1.1 and Lemma 2.1; [*The Siegel–Walfisz theorem*](course:NT-DIRL/NT-DIRL-11), Theorem 2.1; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 3.1 and 4.2.

## 1. Marked weights

Keep \(L=\log x\), \(W=\exp(L^{0.24})\) and \(V(y)=\prod_{p\le y}(1-1/p)\) from Lesson 16. Dirichlet characters, principal ones included, are extended by zero on nonunits. Fix an integer \(K\ge1\) and numbers \(0.1<a_1<\cdots<a_K<0.2\) before letting \(x\) grow, and define the **groups**
\[
\begin{gathered}
\mathcal P_i=\{p\ \text{prime}:L^{a_i}\le\log p\le2L^{a_i}\}\\
(1\le i\le K),\quad(1.1)
\end{gathered}
\]
which are disjoint for large \(x\). For \(h\ge1\) and \(0<q<1\) put
\[
\begin{gathered}
V_i=\sum_{p\in\mathcal P_i}\frac1p,\\
\omega_i(h)=\#\{p\in\mathcal P_i:p\mid h\},\\
\omega=\sum_i\omega_i,\\
\mathcal W(h)=q^{\omega(h)-K}\prod_{i=1}^K\frac{\omega_i(h)}{V_i}.\quad(1.2)
\end{gathered}
\]
By Mertens' estimate (Theorem 3.1 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)), \(V_i=\log2+o(1)\). The weight \(\mathcal W\) is nonnegative, vanishes unless every group supplies a prime divisor, and is bounded in terms of \(K\) and \(q\), since \(jq^{j-1}\) is bounded. A function \(F\) on positive integers is **group-invariant** if \(F(ph)=F(h)\) for every group prime \(p\) and every \(h\); equivalently, \(F(h)\) depends only on \(h\) with all its group prime powers removed.

## 2. Named results

**Named result N5** (one-sided marked Type II estimate [PD, Theorem 3.1]). Fix \(\delta,C,D_*>0\) and \(q\in(0,1)\). Let \(H_m,H_n\ge x^\delta\) with \(X=H_mH_n\asymp x\). Let \(F\) be group-invariant with \(|F|\le1\). Let \(\alpha_m\) be supported on an interval in \([H_m,2H_m]\), where
\[
\begin{gathered}
\begin{aligned}
\alpha_m&=m^{iv}\Bigl(\mathbf 1_{m\ \text{prime}}\\
&\quad -\frac{\mathbf 1_{P^-(m)>W}}{V(W)\log m}\Bigr),
\end{aligned}\\
|v|\le L^C,
\end{gathered}
\]
and let \(\beta_n\) be supported on \(W\)-rough integers in \([H_n,2H_n]\) with \(|\beta_n|\le L^C\). If \(K\) is large enough in terms of \(\delta,C,D_*,q\), then
\[
\begin{aligned}
&\Bigl|\sum_{m,n}\alpha_m\beta_n\,F(mn-1)\,\mathcal W(mn-1)\Bigr|\\
&\quad \le C'\,X\,L^{-D_*}.\quad(2.1)
\end{aligned}
\]
The lower bound for \(K\) does not depend on the \(a_i\); the constant \(C'\) and the threshold for \(x\) may.

**Named result N6** (coefficient criterion [OpenAI-029, Lemma 10.2], extracted from the proof of N5 in [PD, Sections 3–5]). In N5, replace \(\alpha\) by any sequence supported on \(W\)-rough integers of an interval \(I\subseteq[H_m,2H_m]\), keep \(\beta\) as there, and assume \(|\alpha_m|\le L^C\). Suppose that for all fixed \(A_0,B,A>0\), every Dirichlet character \(\chi\) of modulus \(k\le L^{A_0}\) and every \(|t|\le2XL^B\),
\[
\begin{aligned}
&\Bigl|\frac1{H_m}\sum_m\alpha_m\chi(m)m^{it}\Bigr|\\
&\quad \le C_A\,L^{-A},\quad(2.2)
\end{aligned}
\]
uniformly in the interval, the character and \(t\). Then (2.1) holds for \(K\) large enough in terms of the fixed data, with the same uniformity.

**Named result N7** (long prime polynomials and logarithmic phases [PD, Lemmas 2.3 and 2.4], proved in [PD, Appendix, Lemmas 9.1 and 9.5]; also [PP, Lemmas 3.1 and 3.3]).

1. Fix \(0<\tau<\theta<1\) and \(C,A>0\). There is \(B_0\) such that for \(x^\tau/2\le N\le x^\theta\), every character \(\chi\) of modulus \(k\le L^C\), every interval \(J\subseteq[N,2N]\) and \(L^{B_0}\le|u|\le x^2\),
\[
\Bigl|\sum_{p\in J}\chi(p)\,p^{-1+iu}\Bigr|\le C_{\tau,\theta,C,A}\,L^{-A}.
\]
2. Fix \(C>0\). There is an absolute \(C_3>0\) such that for large \(x\), \(\exp(L/(\log L)^2)\le N\le2x^5\), \(k\le L^C\), \(\exp(L/(2(\log L)^2))\le|u|\le4x^3\), every residue \(a\) modulo \(k\) and every interval \(J\subseteq[N,2N]\),
\[
\begin{aligned}
&\Bigl|\sum_{\substack{n\in J\\ n\equiv a\ (k)}}n^{iu}\Bigr|\\
&\quad \le C\,\frac Nk\exp\Bigl(-\frac L{(\log L)^{C_3}}\Bigr).
\end{aligned}
\]

These three results are used without proof in the programme. N5 and N6 rest on a determinant estimate with marks on one side and on a major-arc analysis; N7 rests on Vinogradov's mean-value method and a zero-free strip at large height.

## 3. Characters on rough numbers

**Lemma 3.1** (rough counts [PD, Lemma 2.5]). Fix \(\delta,C,A_0,A>0\). For \(x^\delta\le H\le x^C\), every interval \(I\subseteq[H,2H]\) and every character \(\chi\) of modulus \(k\le L^{A_0}\),
\[
\begin{aligned}
&\sum_{\substack{n\in I\\ P^-(n)>W}}\chi(n)\\
&\quad =\mathbf 1_{\chi\ \text{principal}}\,V(W)\,|I|\\
&\qquad +O(H\,L^{-A}).\quad(3.1)
\end{aligned}
\]

*Proof.* For large \(x\), every prime factor of \(k\) is below \(W\), so a \(W\)-rough \(n\) is a unit modulo \(k\) and the principal character is \(1\) on it. Fix a unit residue \(b\) modulo \(k\), and apply Lemma 2.1 of Lesson 16 to \(\{n\in I:n\equiv b\ (k)\}\) with the primes \(p\le W\), \(p\nmid k\), and the conditions \(p\mid n\). By the Chinese remainder theorem, \(A(d)=|I|/(kd)+O(1)\), so \(X'=|I|/k\), \(g(d)=1/d\), \(|E(d)|\le1\), and (2.1) of Lesson 16 holds with absolute constants. Take the sieve depth \(2\lceil(A+A_0)\log L\rceil\), so that its relative error is \(O(L^{-A-A_0})\) and the remainder sum is at most \(W^{O(\log L)}=x^{o(1)}\). Since \(\prod_{p\le W,\,p\nmid k}(1-1/p)=V(W)k/\varphi(k)\), the count in each unit class is \(V(W)|I|/\varphi(k)+O(HL^{-A-A_0})\). Multiply by \(\chi(b)\) and sum over the \(\varphi(k)\le L^{A_0}\) classes. \(\square\)

## 4. The rough proxy at high frequencies

**Lemma 4.1** (the proxy bound [PD, proof of Lemma 5.2]). Fix \(\delta,A_0>0\), let \(x^\delta\le M\le x\), and put \(T_*=\exp(L/(\log L)^2)\). There are \(C_0,c_0>0\), depending on \(\delta,A_0\), such that for every fixed \(A_4\), every interval \(I'\subseteq[M,2M]\), every character \(\chi\) of modulus \(k\le L^{A_0}\) and \(1\le|u|<x^2\),
\[
\begin{aligned}
&\Bigl|\frac1{M\,V(W)}\sum_{\substack{m\in I'\\ P^-(m)>W}}\frac{\chi(m)\,m^{iu}}{\log m}\Bigr|\\
&\quad\le C\,L^{-A_4}+C\,L^{C_0}\Delta(u),\quad(4.1)
\end{aligned}
\]
where \(C_3\) is the constant of N7 and
\[
\Delta(u)=\begin{cases}|u|^{-1}+x^{-c_0},&|u|\le T_*,\\ e^{-L/(\log L)^{C_3}},&T_*\le|u|<x^2 .\end{cases}
\]

*Proof.* *Truncation.* Let \(S_W=\sum_{p\le W}1/p\), which is \(0.24\log L+O(1)\) by Mertens, and for an integer \(r\) put \(T_r(m)=\sum\mu(d)\) over the squarefree \(d\mid m\) composed of primes \(p\le W\) with at most \(r\) prime factors. If \(m\) has \(s\) prime factors \(p\le W\), then \(T_r(m)=\sum_{a\le r}(-1)^a\binom sa\), which differs from \(\mathbf 1_{s=0}\) by at most \(\binom s{r+1}\) (Exercise 4.1 of Lesson 16). Summing \(\binom s{r+1}\), the number of divisors \(d\) with \(r+1\) such primes, over \(m\in I'\),
\[
\begin{aligned}
&\sum_{m\in I'}\bigl|\mathbf 1_{P^-(m)>W}-T_r(m)\bigr|\\
&\quad \le\sum_{\omega(d)=r+1}\Bigl(\frac{2M}d+1\Bigr)\\
&\quad \le2M\frac{S_W^{r+1}}{(r+1)!}+W^{r+1}.\quad(4.2)
\end{aligned}
\]
With \(r=\lceil c\log L\rceil\) and \(c\) large, the first term is \(O(ML^{-A_4-1})\), and the second is \(\exp(O(L^{0.24}\log L))=x^{o(1)}\). Moreover \(\sum_d1/d\le\prod_{p\le W}(1+1/p)\le CL^{0.24}\) over all \(d\) used, and \(1/V(W)\le CL^{0.24}\).

*One divisor.* For a used \(d\) prime to \(k\) (the others give \(\chi(m)=0\)), write \(m=dz\) and split \(z\) into residues \(a\) modulo \(k\); the range of \(z\) is an interval of scale \(N'=M/d\ge x^{\delta}/W^{r}\ge x^{\delta/2}\). For \(|u|\le T_*\), comparison with the integral gives
\[
\begin{gathered}
\begin{aligned}
\sum_{\substack{z\in J\\ z\equiv a\ (k)}}z^{iu}&=\frac1k\int_Jy^{iu}\,dy+O(1+|u|),
\end{aligned}\\
\Bigl|\int_Jy^{iu}\,dy\Bigr|\le\frac{4N'}{|u|},
\end{gathered}
\]
since \(y^{iu}\) has total variation \(O(|u|)\) on \(J\) and an antiderivative \(y^{1+iu}/(1+iu)\). For \(T_*\le|u|<x^2\), N7(2) applies, because \(N'\ge x^{\delta/2}\ge\exp(L/(\log L)^2)\) and \(|u|\ge T_*\). The factor \(d^{iu}\chi(d)\) has absolute value at most \(1\), and partial summation handles \(1/\log m\), which has bounded variation relative to its size on the dyad.

*Assembling.* Summing over the residues and over the \(d\le W^r\) with the weight bounds above, the error terms \(O(1+|u|)\) contribute \(O(kW^rT_*/M)=O(x^{-c_0})\) after division by \(M\), and the main terms contribute at most \(CL^{C_0}|u|^{-1}\), respectively \(CL^{C_0}\exp(-L/(\log L)^{C_3})\), with \(C_0\) accounting for \(L^{0.24}\cdot L^{0.24}\cdot L^{A_0}\) and the partial summation. The truncation error (4.2) gives the term \(L^{-A_4}\). \(\square\)

## 5. A rough-factor Type II estimate

Let \(D_\gamma\) be the densities (1.3) of Lesson 16.

**Proposition 5.1** (rough-factor Type II estimate [OpenAI-029, Proposition 10.3]). Keep the marked data and the hypotheses on \(F,\beta,H_m,H_n\) of N5. Fix \(0<\gamma<w_-<w_+<1\) with \([\log H_m/L,\log(2H_m)/L]\subseteq[w_-,w_+]\). On an interval \(I\subseteq[H_m,2H_m]\) put
\[
\begin{gathered}
\begin{aligned}
\alpha_m&=m^{iv}\Bigl(\mathbf 1_{P^-(m)>x^\gamma}\\
&\quad -\frac{D_\gamma(\log m/L)}{L\,V(W)}\mathbf 1_{P^-(m)>W}\Bigr),
\end{aligned}\\
|v|\le L^C,\quad(5.1)
\end{gathered}
\]
and \(\alpha_m=0\) outside \(I\). Then (2.1) holds for every fixed \(D_*\) once \(K\) is large in terms of the fixed data, with a lower bound for \(K\) independent of the \(a_i\).

*Proof.* We verify (2.2) and apply N6. Put \(M=H_m\), \(R_\gamma(m)=\mathbf 1_{P^-(m)>x^\gamma}\), and \(J=\lfloor w_+/\gamma\rfloor\); an \(x^\gamma\)-rough \(m\le2M\) has at most \(J\) prime factors.

*Prime products.* Let \(T_\gamma(m)\) be the sum over \(j\le J\) of \(1/j!\) times the number of ordered \(j\)-tuples \((p_1,\dots,p_j)\) of primes \(p_i>x^\gamma\) with \(p_1\cdots p_j=m\). For squarefree \(x^\gamma\)-rough \(m\) this is \(1\); for an \(x^\gamma\)-rough \(m\) with multiplicities \(e_p\) it is \(1/\prod e_p!\); and it is \(0\) if \(m\) is not \(x^\gamma\)-rough. So \(R_\gamma-T_\gamma\) is supported on \(m\) divisible by \(p^2\) for some \(p>x^\gamma\), and on every subinterval of the dyad
\[
\begin{aligned}
&\sum_{M\le m\le2M}|R_\gamma(m)-T_\gamma(m)|\\
&\quad \le\sum_{p>x^\gamma}\frac{2M}{p^2}\le C\,M\,x^{-\gamma},\quad(5.2)
\end{aligned}
\]
also after any twist of absolute value at most \(1\).

*Low frequencies: the rough count.* For fixed \(A_0,A_1\), every \(k\le L^{A_0}\), every \(\chi\) modulo \(k\) and every interval \(I'\subseteq[M,2M]\),
\[
\begin{aligned}
&\sum_{m\in I'}R_\gamma(m)\chi(m)\\
&\quad =\mathbf 1_{\chi\ \text{principal}}\frac1L\int_{I'}D_\gamma\Bigl(\frac{\log y}L\Bigr)\\
&\qquad dy+O(ML^{-A_1}).\quad(5.3)
\end{aligned}
\]
To see this, use \(T_\gamma\) and (5.2). Split each prime variable of the \(j\)-prime term into dyads \([P_i,2P_i)\), with \(x^\gamma/2\le P_i\le2M\); there are \(O(L^j)\) boxes. On a dyad of scale \(P\), \(\log P\asymp L\), and the Siegel–Walfisz theorem (Theorem 2.1 of [*The Siegel–Walfisz theorem*](course:NT-DIRL/NT-DIRL-11)), converted to primes by partial summation and to characters by orthogonality over the at most \(L^{A_0}\) classes, gives for every subinterval \(J'\subseteq[P,2P]\)
\[
\begin{aligned}
\sum_{p\in J'}\chi(p)&=\mathbf 1_{\chi\ \text{principal}}\int_{J'}\frac{dy}{\log y}\\
&\quad +O(PL^{-A_2}),
\end{aligned}
\]
with \(A_2\) arbitrary; the primes involved exceed \(k\). In a box, replace the prime measures one at a time: with the other variables fixed, the product condition leaves an interval for the remaining one, the error is \(O(P_iL^{-A_2})\), and the other variables have total mass \(O(P_h)\); so each box has error \(O(ML^{-A_2})\), and \(A_2\) large absorbs the \(O(L^j)\) boxes. For nonprincipal \(\chi\) the main terms vanish. For principal \(\chi\) the main term of the \(j\)-prime part is \(\frac1{j!}\int_{y_i>x^\gamma,\ \prod y_i\in I'}\prod dy_i/\log y_i\), and Lemma 1.1 of Lesson 16 sums these to the main term of (5.3).

*Low frequencies: cancellation.* Let \(u=t+v\) and fix \(B_2>C+2\). If \(|t|\le L^{B_2}\), then \(|u|\le2L^{B_2}\). Partial summation of (5.3) against \(y^{iu}\), whose total variation on the dyad is \(O(1+|u|)\), gives \(\mathbf 1_{\chi\ \text{principal}}\frac1L\int_ID_\gamma(\log y/L)y^{iu}dy\)\(+O(ML^{-A_1}(1+|u|))\). Partial summation of (3.1) against \(D_\gamma(\log y/L)y^{iu}/(LV(W))\) gives the same main term with an error \(O(ML^{-A}L^{C'})\): \(D_\gamma\) is Lipschitz on \([w_-,w_+]\) (Lemma 1.1 of Lesson 16), and \(LV(W)\asymp L^{0.76}\) by Mertens' product theorem. The two main terms cancel in \(\alpha\), so (2.2) holds for \(|t|\le L^{B_2}\) once \(A_1\) and \(A\) are chosen after \(B_2\).

*High frequencies.* Choose \(0<\tau<\gamma\) and \(w_+<\theta<1\). Let \(L^{B_2}\le|t|\le2XL^B\); then \(|u|\asymp|t|\) and \(L^{B_0}\le|u|<x^2\), where \(B_0\) is taken from N7(1) for the accuracy \(A_3\). Every prime dyad of the convolution lies in \([x^\tau/2,x^\theta]\), and N7(1) with partial summation gives \(|\sum_{p\in J'}\chi(p)p^{iu}|\le CPL^{-A_3}\) on every subinterval. In each box fix all primes but one, bound that one slot by this estimate and the others trivially: the box contributes \(O(ML^{-A_3})\), and with (5.2) the prime-product part of \(\alpha\) has the saving \(L^{-A}\) for \(A_3\) large. For the proxy part write
\[
\begin{gathered}
\frac{D_\gamma(w)}{L\,V(W)}=\frac{w\,D_\gamma(w)}{V(W)\log m}\\
(w=\log m/L);
\end{gathered}
\]
the factor \(wD_\gamma(w)\) is bounded with bounded variation on \([w_-,w_+]\), so Lemma 4.1 and one partial summation bound this part by \(C(L^{-A_4}+L^{C_0}|u|^{-1}\)\(+L^{C_0}x^{-c_0}+L^{C_0}e^{-L/(\log L)^{C_3}})\), which is \(O(L^{-A})\) when \(B_2>A+C_0+2\) and \(A_4\ge A\). Choosing first \(A\), then \(A_3,A_4\) and \(B_0\), and finally \(B_2>\max\{C+2,B_0+2,A+C_0+2\}\) covers all \(|t|\le2XL^B\). The conjugated coefficients satisfy the same bounds, with \(\overline\chi\) and \(-t\).

*Support and size.* For large \(x\), \(x^\gamma>W\), so both parts of (5.1) are supported on \(W\)-rough integers, and \(|\alpha_m|\le1+\sup D_\gamma/(LV(W))\le2\). With these hypotheses verified, N6 gives (2.1). \(\square\)

The point of Proposition 5.1 is that \(\mathbf 1_{P^-(m)>x^\gamma}\), unlike the prime indicator of N5, can be computed by a sieve but has no cancellation of its own; the subtraction of \(D_\gamma(\log m/L)/(LV(W))\) times the \(W\)-rough indicator removes exactly its main terms, leaving a coefficient that the marked bilinear machinery can absorb.

## 6. Exercises

**6.1.** Show that \(jq^{j-1}\le\max(1,\,1/(e\,q\log(1/q)))\) for \(j\ge1\) and \(0<q<1\), and deduce a bound for \(\mathcal W\) in terms of \(K\) and \(q\).

**6.2.** Show that a function \(F\) on positive integers satisfies \(F(ph)=F(h)\) for all group primes \(p\) if and only if \(F(h)=F(h/h_{\mathcal P})\), where \(h_{\mathcal P}\) is the largest divisor of \(h\) composed of group primes.

**6.3.** In (5.2), show that \(\sum_{p>y}p^{-2}\le2/y\) for \(y\ge2\).

**6.4.** In Lemma 4.1, check that \(S_W^{r+1}/(r+1)!\le L^{-A}\) when \(r=\lceil c\log L\rceil\) with \(c\) large, using \(n!\ge(n/e)^n\).

**6.5.** For the coefficient of N5 with \(v=0\), \(\alpha_m=\mathbf 1_{m\ \text{prime}}\)\(-\mathbf 1_{P^-(m)>W}/(V(W)\log m)\), show that (2.2) holds for \(|t|\le L^{B'}\) and every fixed \(B'\), using the Siegel–Walfisz theorem and Lemma 3.1.

## 7. Solutions

**6.1.** The maximum of \(jq^{j-1}\) over real \(j\ge1\) is at \(j=1/\log(1/q)\) when this exceeds \(1\), with value \(1/(eq\log(1/q))\). Then \(\mathcal W(h)\le q^{-K}\prod_i\omega_i(h)q^{\omega_i(h)}/V_i\)\(\le\bigl(\max_j jq^{j-1}\bigr)^K\prod_iV_i^{-1}\), bounded since \(V_i\to\log2\).

**6.2.** If \(F(ph)=F(h)\) for all group primes, remove the group prime factors of \(h\) one at a time. Conversely \(ph\) and \(h\) have the same quotient by their group parts.

**6.3.** \(\sum_{p>y}p^{-2}\le\sum_{n>y}n^{-2}\)\(\le\int_{y-1}^\infty t^{-2}\,dt=1/(y-1)\)\(\le2/y\).

**6.4.** With \(S_W\le\log L\) and \(n=r+1\ge c\log L\), \(S_W^n/n!\le(eS_W/n)^n\le(e/c)^{c\log L}\)\(=L^{-c\log(c/e)}\), which is below \(L^{-A}\) for \(c\) large.

**6.5.** By Siegel–Walfisz, \(\sum_{p\in I'}\chi(p)\)\(=\mathbf 1_{\chi\ \text{principal}}\int_{I'}dy/\log y\)\(+O(H_mL^{-A})\) on every subinterval, and by Lemma 3.1, \(\sum_{m\in I',\,P^-(m)>W}\chi(m)\)\(=\mathbf 1_{\chi\ \text{principal}}V(W)|I'|\)\(+O(H_mL^{-A})\). Partial summation against \(y^{it}\) (variation \(O(1+|t|)\le O(L^{B'})\)) and against \(y^{it}/(V(W)\log y)\) turns both into \(\mathbf 1_{\chi\ \text{principal}}\int_Iy^{it}dy/\log y\)\(+O(H_mL^{-A+B'+1})\); the main terms cancel, and \(A\) is arbitrary.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 10. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Theorem 3.1, Lemmas 2.3–2.5, Sections 3–5 and the Appendix. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
- [PP] OpenAI, *Prime predecessors with an even number of prime factors*, OpenAI Math Release preprint, 17 September 2026, Section 3, Lemmas 3.1 and 3.3. https://github.com/openai/math/tree/main/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026
