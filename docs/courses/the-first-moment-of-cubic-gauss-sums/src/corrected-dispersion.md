# Corrected dispersion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A bilinear sum \(\sum_{a,b}\alpha_a\beta_bG(ab)\) is controlled through the second moment, over \(a\), of
\[
F_u(a)=\sum_b\beta_b\,N(b)^{iu}\,G(b)\,\overline{\chi_b(a)},
\]
because \(G(ab)=G(a)G(b)\overline{\chi_b(a)}\). Opening the square and applying Poisson summation in \(a\) turns the off-diagonal terms into sums over frequencies. The cubic large sieve controls most frequencies. The frequencies that are cubes, however, do not cancel: they produce a main term, \(c_*^2|S(u)|^2\sum_a\mu^2(a)W(a)N(a)^{-1/3}\), which is exactly the square of the model. This lesson proves that after subtracting the model, \(F_u(a)-c_*\overline{G(a)}N(a)^{-1/6}S(u)\), the second moment is small. Without subtraction it proves a bound that keeps the sparsity of the coefficients, and at large heights it proves an averaged bound with the exact diagonal. Dunn and Radziwiłł found this mechanism, with the main term from the cube frequencies, and proved it under the Generalized Riemann Hypothesis; here the remaining frequencies are bounded unconditionally by the results of the previous lessons.

**Prerequisites.** The lessons [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md), [*The level formula and Type I sums*](the-level-formula-and-type-i-sums.md) and [*Character moments at two exceptional configurations*](character-moments-at-two-exceptional-configurations.md).

## 1. The statement

Throughout, \(L=\log X\) and
\[
\begin{gathered}
AB\asymp X,\quad X^{0.32}\le B\ll X^{1/2},\\
H=\frac{B^2}A,\quad \mathcal Q=ABH^{1/3}.
\end{gathered}
\]
Sums over the letters \(a,b,d,f,l,m,n,p,q\) run over primary elements. Let \(\beta\) be divisor-bounded and supported on squarefree \(b\) of length \(B\). When \(B>X^{0.40}\), suppose in addition that \(\beta\) is an admissible prime convolution in the sense of the previous lesson, with all primes of norm at least \(X^c\) for a fixed \(c>0\), and with a fixed angular order \(\ell\). Put
\[
\begin{gathered}
\beta_b(u)=\beta_bN(b)^{iu},\\
S(u)=\sum_b\beta_b(u)N(b)^{-1/6},\\
F_u(a)=\sum_b\beta_b(u)G(b)\overline{\chi_b(a)}.
\end{gathered}
\]
Let \(W\ge0\) be a radial smooth function on \(\mathbb C\), supported in a fixed annulus, and \(W_A(a)=W(a/\sqrt A)\).

The low-height estimate uses the following property of \(\beta\).

**(SW)** For every fixed conductor bound \(L^{C_1}\), height bound \(L^{C_2}\) and \(D>0\), and every nonprincipal cubic Hecke character \(\chi\) of conductor norm at most \(L^{C_1}\), we have \(\sum_b\beta_b\chi(b)N(b)^{it}=O_D(BL^{-D})\) for \(|t|\le L^{C_2}\), uniformly in \(\chi\) and \(t\). The same holds with \(b\) restricted to be coprime to any given element of norm \(X^{O(1)}\).

Here \(\beta\) includes its angular factor, so (SW) concerns the twisted sequence itself.

**Proposition 1.1 (dispersion estimates).** Under these hypotheses the following hold.

(1) *(Coarse bound.)* If \(H\gg1\), \(|u|\le X^{0.17}\), and the derivatives of \(W\) are bounded independently of \(X\), then
\[
\sum_aW_A(a)|F_u(a)|^2\ll\mathcal QL^{O(1)} .
\]

(2) *(Low heights.)* Let \(|u|\le L^{O(1)}\) and \(H\gg1\). Suppose \(\beta\) has property (SW) and is supported on elements all of whose prime factors have norm greater than \(L^{C_r}\). For every fixed \(K>0\), if \(C_r\) and \(C_g\) are sufficiently large, then for \(H\ge L^{C_g}\)
\[
\begin{aligned}
&\sum_a\mu^2(a)W_A(a)\\
&\quad\cdot\Bigl|F_u(a)-c_*\overline{G(a)}N(a)^{-1/6}S(u)\Bigr|^2\\
&\ll\mathcal QL^{-K},\qquad(1.1)
\end{aligned}
\]
and for \(1\ll H<L^{C_g}\)
\[
\begin{aligned}
&\sum_aW_A(a)|F_u(a)|^2\\
&\ll A\sum_b|\beta_b|^2+\mathcal Q\,L^{-K}\\
&\quad+\mathcal Q\Bigl(B^{-1}\sum_b|\beta_b|\Bigr)^2.\quad(1.2)
\end{aligned}
\]
In this part the derivatives of \(W\) are bounded independently of \(X\).

(3) *(Large heights.)* Let \(u=\pm t+u_0\) with \(T\le|t|\le2T\) and \(2T+|u_0|\le X^{0.17}\), and let \(|\partial^jW|\ll_jL^{Cj}\) for a fixed \(C\). For every fixed \(K\), if \(T\ge L^{C_t}\) with \(C_t\) large enough, then
\[
\begin{aligned}
&\int_{T\le|t|\le2T}\sum_aW_A(a)\\
&\qquad\cdot|F_{\pm t+u_0}(a)|^2\frac{dt}T\\
&\le\int_{T\le|t|\le2T}\mathcal D_W\frac{dt}T\\
&\qquad+O(\mathcal QL^{-K}),\quad(1.3)
\end{aligned}
\]
with the exact diagonal \(\mathcal D_W=\sum_b|\beta_b|^2\sum_{(a,b)=1}W_A(a)\). No lower bound on \(H\) is needed, and when \(B\le X^{0.40}\) the restriction on \(u_0\) can be dropped. Moreover there is an absolute \(\gamma>0\) such that, when \(B\le X^{0.40}\), \(T\gg X^{0.01}\) and \(|\partial^jW|\ll_jX^{j\gamma}\),
\[
\begin{aligned}
&\int_{T\le|t|\le2T}\sum_aW_A(a)\\
&\qquad\cdot|F_{\pm t+u_0}(a)|^2\frac{dt}T\\
&\le\int_{T\le|t|\le2T}\mathcal D_W\frac{dt}T\\
&\qquad+O(\mathcal QX^{-10\gamma}).\quad(1.4)
\end{aligned}
\]
This \(\gamma\) does not depend on the fixed exponents of the divisor bounds. In (1.3) and (1.4), if \(W\) is supported in an annulus of radial width \(O(J^{-1})\) in the logarithm of the norm, then \(\mathcal D_W\ll(A/J)\sum_b|\beta_b|^2\), for \(J\le L^{O(1)}\) or \(J\le X^\gamma\) respectively. In particular, when \(B\le X^{0.40}\) the coefficients may be restricted sharply to any norm interval without changing these assertions.

## 2. Opening the square

**Squarefree majorization.** Only for (1.1), majorize the weight \(\mu^2(a)\) in the term \(|F_u(a)|^2\) by
\[
\mu^2(a)\le\Bigl(\sum_{\substack{c^2\mid a\\N(c)\le L^{D_0}}}\mu(c)\Bigr)^2=\sum_{d^2\mid a}\lambda_d .
\]
This is an equality for squarefree \(a\). Here \(\lambda_d=\sum\mu(c_1)\mu(c_2)\) over pairs with least common multiple \(d\), so \(d\) is squarefree, \(N(d)\le L^{2D_0}\), \(|\lambda_d|\le\tau(d)^2\), and \(\lambda_d=\mu(d)\) when \(N(d)\le L^{D_0}\). For the uncorrected estimates take only \(d=1\). The mixed and model terms of the corrected square keep their true weight \(\mu^2(a)\).

**The diagonal.** For \(d=1\) the terms \(b_1=b_2\) give exactly \(\mathcal D_W\), because \(|G(b)|=1\) on squarefree \(b\). With the sieve weights they give \(O\bigl(\sum_d|\lambda_d|A/N(d)^2\sum_b|\beta_b|^2\bigr)\)\(=O(ABL^{O(1)})\). This is \(O(\mathcal QL^{-K})\) once \(H\ge L^{C_g}\) with \(C_g\) large.

**Poisson summation.** For an off-diagonal pair \(b_1\ne b_2\), write \(f=(b_1,b_2)\), \(F=N(f)\), and \(b_i=fp_i\). Then \(p_1,p_2\) are coprime, squarefree, prime to \(f\), and of length \(B/F\). The summand vanishes unless \((b_1b_2,d)=1\). Since \(\overline{\chi_{b_1}(a)}\chi_{b_2}(a)=\mathbf 1_{(a,f)=1}\overline{\chi_{p_1}(a)}\chi_{p_2}(a)\), remove the condition \((a,f)=1\) by Möbius inversion, and write
\[
\begin{gathered}
a=d^2mx,\qquad m\mid f,\\
M=N(m),\qquad D_d=N(d),
\end{gathered}
\]
with \(x\) primary. The character \(\psi=\overline{\chi_{p_1}}\chi_{p_2}\) is primitive modulo \(q=p_1p_2\), and nonprincipal since \(b_1\ne b_2\).

**Lemma 2.1.** For these \(b_1,b_2,d,m\), the sum \(\sum_xW_A(d^2mx)\overline{\chi_{b_1}(d^2mx)}\chi_{b_2}(d^2mx)\), multiplied by \(G(b_1)\overline{G(b_2)}\), equals
\[
\begin{aligned}
&\frac{A}{9D_d^2M\,|p_1p_2|}\sum_{0\ne h\in\mathcal O}e\Bigl(\operatorname{Tr}\frac h{3\lambda}\Bigr)\\
&\quad\cdot\widehat W\Bigl(\frac{h\sqrt A}{3\lambda D_d\sqrt M\,p_1p_2}\Bigr)\\
&\quad\cdot\chi_{p_1}\bigl(dh(fm)^{-1}\bigr)\overline{\chi_{p_2}\bigl(dh(fm)^{-1}\bigr)} ,
\end{aligned}
\]
where the inverse is a residue class modulo \(p_1p_2\).

**Proof.** The classes \(x\equiv1\pmod3\) are represented by \(x=q+3s\), with \(s\) modulo \(q\). Apply Lemma 2.1 of the lesson on large sieves with modulus \(3q\) to the function \(x\mapsto W(d^2mx/\sqrt A)\). Its transform at \(\eta\) is \((A/N(d^2m))\widehat W(\eta\sqrt A/(d^2m))\), and since \(W\) is radial the complex number \(d^2m\) can be replaced by its absolute value \(D_d\sqrt M\). Writing the frequencies as \(y=h/\lambda\) with \(h\in\mathcal O\), the phase is
\[
\begin{aligned}
&e\Bigl(\operatorname{Tr}\frac{(q+3s)h}{3\lambda q}\Bigr)\\
&\qquad=e\Bigl(\operatorname{Tr}\frac h{3\lambda}\Bigr)e\Bigl(\operatorname{Tr}\frac{sh}{\lambda q}\Bigr).
\end{aligned}
\]
If \(\lambda\lambda'+q\kappa=1\) with \(\lambda',\kappa\in\mathcal O\), then \(e(\operatorname{Tr}(sh/(\lambda q)))=e(\operatorname{Tr}(sh\lambda'/q))\), since \(\operatorname{Tr}(sh\kappa/\lambda)\in\mathbb Z\). By Lemma 3.2 of the lesson on large sieves,
\[
\begin{aligned}
&\sum_{s\bmod q}\psi(3s)\,e\Bigl(\operatorname{Tr}\frac{sh\lambda'}q\Bigr)\\
&=\psi(3)\overline{\psi(h\lambda')}g(\psi)\\
&=\psi(3\lambda)\overline{\psi(h)}g(\psi),
\end{aligned}
\]
and \(\psi(3\lambda)=1\) since \(3\lambda=(-\lambda)^3\). At \(h=0\) the sum vanishes, \(\psi\) being nonprincipal.

By the Chinese remainder theorem and reciprocity, \(g(\psi)=\overline{g(p_1)}g(p_2)\): the two factors \(\overline{\chi_{p_1}(p_2)}\) and \(\chi_{p_2}(p_1)\) cancel. Proposition 3.1 of the first lesson gives
\[
G(fp_i)=\overline{\chi_{p_i}(f)}G(f)G(p_i),
\]
so that \(G(b_1)\overline{G(b_2)}g(\psi)=|p_1p_2|\,\overline{\chi_{p_1}(f)}\chi_{p_2}(f)\). The remaining character values are
\[
\overline{\chi_{p_1}(d^2m)}\chi_{p_2}(d^2m)\cdot\overline{\psi(h)}\cdot\overline{\chi_{p_1}(f)}\chi_{p_2}(f),
\]
which combine to \(\chi_{p_1}(dh(fm)^{-1})\overline{\chi_{p_2}(dh(fm)^{-1})}\), because \(\overline{\chi(d^2)}=\chi(d)\). The modulus \(3q\) has index \(9N(q)\), which gives the prefactor. \(\square\)

The off-diagonal part of the opened square is the sum of these expressions, multiplied by \(\lambda_d\mu(m)\beta_{b_1}(u)\overline{\beta_{b_2}(u)}\), over \(d\), \(m\) and the pairs. The natural dual norm scale of Lemma 2.1 is
\[
H'=\frac{H\,D_d^2M}{F^2} .
\]
Indeed \(\widehat W\) decays rapidly once \(N(h)\) exceeds \(N(p_1p_2)D_d^2M/A\asymp H'\).

## 3. Large common divisors and the separation of the pairs

Fix a small \(\delta>0\), to be chosen after the frequency estimates.

**Large common divisors.** First remove the pairs with \(F\ge X^\delta\). If \(H<X^{\delta/2}\), then \(M\le F\) gives \(H'\le X^{-\delta/2+o(1)}\), every nonzero frequency lies in the rapidly decreasing tail of \(\widehat W\), and the contribution is negligible. If \(H\ge X^{\delta/2}\), invert the function \(\mathbf 1_{N((b_1,b_2))\ge X^\delta}\) on the divisor lattice. Its coefficients \(c(e)\) are bounded by \(\tau(e)\) and vanish for \(N(e)<X^\delta\). For fixed \(e\), the resulting full form is a sum of squares with inner length \(B/N(e)\): the common factor \(\chi_e(a)\) drops out in absolute value. By Lemma 4.2(b) of the lesson on large sieves, a dyad \(N(e)\asymp E\) costs
\[
\begin{aligned}
&X^\epsilon E\Bigl(A+\Bigl(\frac{AB}E\Bigr)^{2/3}\Bigr)\frac BE\\
&\qquad=X^\epsilon\bigl(AB+\mathcal QE^{-2/3}\bigr),
\end{aligned}
\]
where \(A\gg B/E\) absorbs the last term of that lemma. Relative to \(\mathcal Q\), the first term saves \(H^{-1/3}\le X^{-\delta/6}\) and the second saves \(E^{-2/3}\le X^{-2\delta/3}\). Removing the diagonal costs at most \(X^\epsilon AB\).

**Separation.** For \(F<X^\delta\) both \(p_i\) are nontrivial. Remove the coprimality of \(p_1\) and \(p_2\) by \(\sum_{l\mid(p_1,p_2)}\mu(l)\), and put \(p_i=ln_i\), \(V_l=N(l)\), \(B'=B/(FV_l)\). For this step, the expression of Lemma 2.1 is first extended to all pairs; the Möbius inversion then returns exactly the coprime pairs. Squarefree support forces \((l,n_i)=1\), and the common character factors give \(|\chi_l(dh(fm)^{-1})|^2\), an exclusion on \(h\). All other fixed coprimality conditions go into the coefficients.

On a frequency dyad \(N(h)\asymp J\) put \(k=J/H'\). Mellin separation of the radial transform and of the norms of \(n_1,n_2\), followed by Cauchy's inequality in \(h\), reduces the estimate to the shifted squares
\[
\begin{aligned}
&\sum_{\substack{h\in\mathcal O\\ N(h)\asymp J}}\Bigl|\sum_n\beta_{fln}\,N(n)^{iu'}\\
&\qquad\cdot\chi_n\bigl(dh(fm)^{-1}\bigr)\Bigr|^2,\quad(3.1)
\end{aligned}
\]
with the exclusions understood and \(u'\) equal to \(u\) plus a Mellin variable. A smooth cutoff equal to one on all possible scaled norms puts every further smooth factor into the separated kernel. So at \(f=l=1\) no cutoff on the prime products is introduced, and both the prime-convolution structure and (SW) are preserved.

Integration by parts in the plane transform and in the two log-norm variables bounds the separated kernel by \(C(W)(1+k)^{-R}(1+|v_1|+|v_2|)^{-M_0}\) for arbitrary fixed \(R,M_0\). Here \(C(W)\) is a finite sum of derivative norms of \(W\): a power of \(L\) for log-scale weights, and \(X^{O(\gamma)}\) for the power-width weights of (1.4). So \(k\) and all shifts can be truncated at \(X^{\delta'}\), for any small fixed \(\delta'>0\), with negligible tails. All shifts are independent of \(t\), and there are \(O(L)\) frequency dyads.

**The benchmark.** Use \(J^{1/3}B'^2\) as a benchmark for (3.1). The prefactor of Lemma 2.1 is of size \(AF/(D_d^2MB)\), and
\[
\begin{aligned}
&\frac{AF}{D_d^2MB}\cdot\frac{J^{1/3}B'^2}{\mathcal Q}\\
&\qquad=\frac{k^{1/3}}{D_d^{4/3}M^{2/3}F^{5/3}V_l^2}.\quad(3.2)
\end{aligned}
\]
The sums over \(f\) with \(m\mid f\), and over \(d\) with its sieve coefficients, converge with these powers.

**Large \(l\).** Discard \(V_l\ge X^\delta\). Lemma 4.2(b) of the lesson on large sieves bounds (3.1) by
\[
X^\epsilon\bigl(J+(JB')^{2/3}+J^{1/3}B'\bigr)B' .
\]
Its ratios to the benchmark are \(J^{2/3}/B'\), \((J/B')^{1/3}\) and \(1\). On the retained transforms \(J\ll X^{2\delta'}B/F\), since \(H\ll B\), \(M\le F\) and \(D_d\) is a power of \(L\); also \(B/F\gg X^{0.3}\). After summing the \(l\) in a dyad, the factor \(V_l^{-2}\) in (3.2) bounds the costs by \(X^{4\delta'/3}(B/F)^{-1/3}\), \(X^{2\delta'/3}V_l^{-2/3}\) and \(V_l^{-1}\). For \(\delta'\) small compared with \(\delta\), each saves a fixed power.

## 4. The frequencies with large conductor

For the remaining \(l\), factor each nonzero frequency as
\[
h=\zeta\lambda^ipq^2j^3,\qquad i\in\{0,1,2\},
\]
with a unit \(\zeta\), coprime squarefree primary \(p,q\), and \(j\) allowed to contain powers of \(\lambda\). Put \(N(p)\asymp P\) and \(N(q)\asymp Q\). Then \(PQ^2\ll J\) and \(N(j)\asymp(J/(PQ^2))^{1/3}\). For fixed \(j\) the relevant benchmark is
\[
B'^2(PQ^2)^{1/3},
\tag{4.1}
\]
and the number of \(j\) restores \(J^{1/3}B'^2\). The cube part only excludes \((n,j)>1\), and the other fixed symbols are twists of the coefficients.

**Claim.** There is a fixed power saving over (4.1) whenever \(PQ^2\ge X^{0.003}\).

*Proof.* Consider a hypothetical sequence with \(\delta,\delta'\to0\) and no power saving. Then \(B'=B^{1+o(1)}\) and \(PQ^2\le B^{1+o(1)}\). Write \(P=B^x\) and \(Q=B^y\) in the limit, so \(x+2y\le1\).

- If \(x>y\), fix \(q\) and apply Theorem 4.1 of the lesson on large sieves to \(p\). The bound \(QB(P+B+(PB)^{2/3})\), divided by \(B^2(PQ^2)^{1/3}\), has the three ratios
\[
\begin{gathered}
\frac{P^{2/3}Q^{1/3}}B,\qquad\Bigl(\frac QP\Bigr)^{1/3},\\
\Bigl(\frac{PQ}B\Bigr)^{1/3}.
\end{gathered}
\]
All save a power unless \(x=1\) and \(y=0\).
- If \(y>x\), reverse the roles, conjugating the character. The ratios are
\[
\begin{gathered}
\frac{P^{2/3}Q^{1/3}}B,\qquad\Bigl(\frac PQ\Bigr)^{2/3},\\
\Bigl(\frac{P^2}B\Bigr)^{1/3},
\end{gathered}
\]
and all save a power.
- If \(x=y=v\), Lemma 3.3 of the lesson on large sieves gives \((B+(PQ)^2)B\), with ratio \(B^{-v+o(1)}+B^{3v-1+o(1)}\). Since \(0\le v\le\frac13\), this saves unless \(v=\frac13\); the endpoint \(v=0\) is excluded by \(PQ^2\ge X^{0.003}\).

The two exceptional configurations, \((x,y)=(1,0)\) and \((\frac13,\frac13)\), are those of Proposition 1.1 of the previous lesson. Both force \(PQ^2=B^{1+o(1)}\), hence \(J\ge B^{1-o(1)}\), \(H\ge B^{1-o(1)}\), and so \(B=X^{1/2+o(1)}\), since \(H=B^3/X\). In particular \(B>X^{0.40}\), so \(\beta\) is an admissible prime convolution. Its primes have norm at least \(X^c\), so \(\delta<c\) forces \(f=l=1\). The remaining \(d\), the cube part \(j\) and the fixed twists and exclusions have norm \(X^{o(1)}\), and the height satisfies
\[
1+|u'|\le X^{0.17}+X^{\delta'}+1\le B^{0.36}
\]
eventually. So the previous lesson supplies the missing saving. To check its normalization, let \(\delta_D,\eta_D\) be the constants of that proposition, and choose the radius \(h_0\) of the exceptional neighborhoods with \(h_0<\min(\delta_D,\eta_D)/4\). In such a neighborhood \(B^2(PQ^2)^{1/3}\ge B^{7/3-h_0}\), so the bound \(B^{7/3-\eta_D}\) saves at least \(B^{3\eta_D/4}\) against the benchmark. Compactness of the exponent region turns the limiting statement into one fixed saving for some fixed small \(\delta,\delta'\). \(\square\)

When \(B\le X^{0.40}\), the exceptional configurations cannot occur: \(H=B^3/X\le X^{0.20}\), while \(B\ge X^{0.32}\), so \(H\) is not \(B^{1-o(1)}\). The gaps are then absolute. In this range \(\delta\), \(\delta'\) and \(\gamma\) can be chosen independently of the prime-convolution structure and of the divisor exponents, and no restriction on the twist \(u\) is needed.

## 5. Small conductors and averages over the height

Suppose \(PQ^2<X^{0.003}\). The characters indexed by \((p,q)\) have conductor \(pq\) away from \(3\), and the exponents \(1\) and \(2\) distinguish them. Since \((PQ)^2\le X^{0.006}\ll B'\), Lemma 3.3 of the lesson on large sieves bounds the ratio to (4.1) by
\[
L^{O(1)}\tau(fl)^{O(1)}(PQ^2)^{-1/3}.
\tag{5.1}
\]
The divisor factor is summable against (3.2). This gives any desired logarithmic saving once \(PQ^2\) exceeds a large fixed power of \(L\), and a bound \(L^{O(1)}\) throughout. Together with the previous sections and the diagonal, this proves (1) when \(H\gg1\).

For the averages over the height, fix a row and collect equal norms in its inner polynomial. The squared coefficients sum to \(B'L^{O(1)}\tau(fl)^{O(1)}\), so the mean value inequality (Lemma 5.1 of the lesson on large sieves) gives
\[
\begin{aligned}
&\int_{T\le|t|\le2T}\bigl|\text{inner polynomial}\bigr|^2\frac{dt}T\\
&\qquad\ll\Bigl(B'+\frac{B'^2}T\Bigr)L^{O(1)}\tau(fl)^{O(1)}.
\end{aligned}
\]
Summing over the \(O(PQ)\) rows, the ratio to (4.1) is
\[
\begin{aligned}
&L^{O(1)}\tau(fl)^{O(1)}P^{2/3}Q^{1/3}\\
&\qquad\cdot\Bigl(\frac1T+\frac1{B'}\Bigr).\quad(5.2)
\end{aligned}
\]
Use (5.1) above a large power of \(L\) for \(PQ^2\), and (5.2) below it. Taking \(C_t\) large absorbs all logarithmic costs and proves (1.3).

For (1.4), in this range \(P^{2/3}Q^{1/3}\le(PQ^2)^{2/3}<X^{0.002}\), \(T^{-1}\ll X^{-0.01}\) and \(B'^{-1}\ll X^{-0.3}\). So (5.2) has an absolute power gap, at least \(0.008\) before small losses. The other frequency ranges already have absolute gaps when \(B\le X^{0.40}\). Choose \(\gamma\) so small that these gaps absorb the finitely many derivative norms and the factor \(X^{10\gamma}\). Fixed divisor powers are harmless, since their losses can be taken arbitrarily small.

Neither argument used \(H\gg1\). If \(H'\) is small, all nonzero frequency dyads have large \(k\) and lie in the tail of \(\widehat W\). For \(B\le X^{0.40}\) only coefficient moments and large sieves were used, which proves the freedom of norm restrictions and of \(u_0\). Finally, an annulus of radial width \(O(J^{-1})\) in the logarithm of the norm contains \(O(A/J+\sqrt A+1)\) lattice points, which is \(O(A/J)\) in the stated ranges since \(A\gg X^{1/2}\). This proves the bound for \(\mathcal D_W\).

## 6. Low heights: the frequencies of small conductor

From here on assume roughness and (SW), as in (2). If \(f\) or \(l\) is not a unit, its norm exceeds \(L^{C_r}\). The tails of (3.2), with the fixed divisor factors, then give \(O(\mathcal QL^{-K'})\) for every \(K'\) when \(C_r\) is large: the sum over \(f\) decays like \(F^{-2/3}\) and that over \(l\) like \(V_l^{-1}\) on dyads. The transform and coefficient costs do not grow with \(C_r\).

So let \(f=l=m=1\). Exclude exactly the frequencies for which \(dh\) is a cube. If \(PQ^2\) is at most a fixed power of \(L\), the character \(n\mapsto\chi_n(dh)\) is nonprincipal by Lemma 6.3 of the lesson on large sieves, and its primitive conductor is at most a fixed power of \(L\). The cube part adds only the exclusion \((n,j)=1\), which (SW) allows. So (SW) gives any required logarithmic saving in (4.1), after absorbing the number of rows and the other logarithmic costs. Mellin shifts beyond a large power of \(L\) are handled by the decay of the transform and the coarse bounds already proved. Together with (5.1) and the large-conductor savings, only the cube frequencies remain, with an error \(O(\mathcal QL^{-K'})\).

## 7. The cube frequencies and their constant

Since \(d\) is squarefree, \(dh\) is a cube exactly when
\[
h=d^2j^3,\qquad j\in\mathcal O\setminus\{0\},
\]
and each such \(h\) arises from three values of \(j\), which differ by cube roots of unity. The phase \(e(\operatorname{Tr}(h/(3\lambda)))\) equals \(1\). Indeed, cubing is additive modulo \(3\), so \(j^3\equiv n\pmod3\) for a rational integer \(n\), and \(d\equiv1\pmod 3\). Then \(h=n+3t\) with \(t\in\mathcal O\), and \(\operatorname{Tr}(n/(3\lambda))=\frac n3\operatorname{Tr}(\lambda^{-1})=0\) while \(\operatorname{Tr}(t/\lambda)\in\mathbb Z\). Choose \(C_r>2D_0\), so that \(d\) is coprime to every \(b\) in the support. The character factor is then \(1\) whenever \((j,b_1b_2)=1\).

Ignore the condition \((j,b_1b_2)=1\) for the moment. Substituting \(h=d^2j^3\) into Lemma 2.1, the absolute value of \(d^2\) cancels \(D_d\) in the argument of \(\widehat W\), and a rotation is immaterial since \(\widehat W\) is radial. With \(\tau=\sqrt A/(3\lambda p_1p_2)\), the frequency sum is \(\frac13\sum_{j\ne0}\widehat W(\tau j^3)\). The substitution \(w=\tau^{1/3}z\) and a comparison with the integral give
\[
\begin{aligned}
&\frac13\Bigl(\frac{27N(p_1p_2)}A\Bigr)^{1/3}\\
&\quad\cdot\int_{\mathbb C}\widehat W(z^3)\,d\mathfrak m(z)\\
&\quad+O\bigl(H^{1/6}+1\bigr).\quad(7.1)
\end{aligned}
\]
Indeed, the radius of the relevant lattice points is \(|\tau|^{-1/3}\asymp H^{1/6}\), the function \(z\mapsto\widehat W(z^3)\) is a Schwartz function, and deleting the origin costs \(O(1)\). For \(H\ge L^{C_g}\) the error is a relative saving \(O(H^{-1/6})\). For a prime \(\pi\), the nonzero multiples of \(\pi\) contribute \(O(H^{1/3}/N(\pi))\) to this sum, also when the spacing of \(\pi\mathcal O\) exceeds the radius. So restoring the condition \((j,b_1b_2)=1\) costs \(O(H^{1/3}\sum_{\pi\mid b_1b_2}N(\pi)^{-1})\), which saves any power of \(L\) by roughness. For (1.2), with \(d=1\), the bound \(O(H^{1/3})\) for the cube sum suffices, and its contribution is
\[
\begin{aligned}
&\ll\frac ABH^{1/3}\Bigl(\sum_b|\beta_b|\Bigr)^2\\
&\qquad=\mathcal Q\Bigl(B^{-1}\sum_b|\beta_b|\Bigr)^2 .
\end{aligned}
\]
With the diagonal and the noncube frequencies already bounded, this proves (1.2).

**Lemma 7.1 (the constant).** For a radial smooth \(W\) supported in an annulus,
\[
\begin{aligned}
&\int_{\mathbb C}\widehat W(z^3)\,d\mathfrak m(z)\\
&\qquad=c_*^2\int_{\mathbb C}W(y)\,|y|^{-2/3}\,d\mathfrak m(y).
\end{aligned}
\]

**Proof.** The map \(z\mapsto z^3\) is three-to-one, with Jacobian \(9|z|^4\), so the left side is \(\frac13\int\widehat W(y)|y|^{-4/3}d\mathfrak m(y)\). Write
\[
|y|^{-4/3}=\frac{\pi^{2/3}}{\Gamma(2/3)}\int_0^\infty e^{-\pi s|y|^2}s^{2/3}\frac{ds}s .
\]
By Exercise 7.1 of the lesson on large sieves, rescaled, the transform of \(y\mapsto e^{-\pi s|y|^2}\) is \(x\mapsto\frac2{\sqrt3}s^{-1}e^{-4\pi|x|^2/s}\). Parseval's identity for the trace pairing and Fubini's theorem therefore give
\[
\begin{aligned}
&\int\widehat W(y)|y|^{-4/3}d\mathfrak m(y)\\
&=\frac2{\sqrt3}\,\frac{\pi^{2/3}}{\Gamma(2/3)}\int W(x)\\
&\qquad\cdot\int_0^\infty s^{-4/3}e^{-4\pi|x|^2/s}\,ds\,d\mathfrak m(x).
\end{aligned}
\]
The interchanges are justified because \(\widehat W\) is a Schwartz function, \(|y|^{-4/3}\) is locally integrable in the plane, and \(W\) vanishes near \(0\). The inner integral is \((4\pi|x|^2)^{-1/3}\Gamma(\frac13)\). Collecting the constants, the left side is \(\kappa\int W(x)|x|^{-2/3}d\mathfrak m(x)\) with
\[
\begin{aligned}
\kappa&=\frac13\cdot\frac2{\sqrt3}\cdot\frac{\pi^{1/3}\,\Gamma(\frac13)}{2^{2/3}\,\Gamma(\frac23)}\\
&=\frac{(2\pi)^{4/3}}{9\,\Gamma(\frac23)^2}=c_*^2,
\end{aligned}
\]
where the middle equality uses \(\Gamma(\frac13)\Gamma(\frac23)=2\pi/\sqrt3\). \(\square\)

Combining (7.1) and Lemma 7.1 with the prefactor of Lemma 2.1 gives, for the pair \(b_1,b_2\), the factor
\[
\begin{aligned}
&\frac{A^{2/3}}{9D_d^2}\bigl(N(b_1)N(b_2)\bigr)^{-1/6}\\
&\qquad\cdot c_*^2\int W(y)|y|^{-2/3}d\mathfrak m(y).
\end{aligned}
\]
Moreover \(\sum_d\lambda_d/N(d)^2=\sum_d\mu(d)/N(d)^2\)\(+O(L^{-D_0/2})\), because \(\lambda_d=\mu(d)\) up to \(L^{D_0}\) and the series converges absolutely with the divisor bound. The primary elements have density \(\frac19\) for \(\mathfrak m\), and squarefree counting by square-divisor inversion identifies the total cube term as
\[
\begin{aligned}
&c_*^2|S(u)|^2\sum_a\mu^2(a)W_A(a)N(a)^{-1/3}\\
&\qquad+O(\mathcal QL^{-K'})\quad(7.2)
\end{aligned}
\]
for \(D_0,C_r,C_g\) large. The counting error is a power saving: a smooth annular squarefree count has error \(O_\epsilon(A^{1/2+\epsilon})\), and the weight \(N(a)^{-1/3}\) costs \(A^{-1/3}\) against the main scale \(A^{2/3}\).

## 8. Cancellation in the corrected square

Open the square in (1.1). By the preceding sections, the term \(\sum\mu^2(a)W_A(a)|F_u(a)|^2\) is at most the main term of (7.2) plus \(O(\mathcal QL^{-K'})\). The mixed term keeps the true weight \(\mu^2(a)\), and by Proposition 3.1(c) of the first lesson,
\[
\begin{aligned}
&\sum_a\mu^2(a)W_A(a)N(a)^{-1/6}G(a)F_u(a)\\
&\qquad=\sum_{a,b}\beta_b(u)W_A(a)N(a)^{-1/6}G(ab).
\end{aligned}
\]
This is a Type I sum with outer variable \(b\) of length \(B\ll X^{1/2}<X^{0.51}\) and a radial inner weight. The angular factor, if any, is part of the outer coefficient. Proposition 4.1 of the lesson on the level formula, with angular order zero, replaces it by
\[
\begin{aligned}
&c_*\sum_{a,b}\beta_b(u)\,\mu^2(ab)\\
&\qquad\cdot W_A(a)\,N(a)^{-1/3}N(b)^{-1/6}
\end{aligned}
\]
with an error \(O(A^{-1/6}X^{5/6-\eta})\). Since \(|S(u)|\ll B^{5/6}L^{O(1)}\), multiplication by \(\overline{S(u)}\) leaves the error
\[
A^{-1/6}B^{5/6}X^{5/6-\eta}L^{O(1)}=\mathcal QX^{-\eta}L^{O(1)} .
\]
In the model sum, remove the coprimality of \(a\) and \(b\): a common prime has norm greater than \(L^{C_r}\), and the pairs sharing such a prime are fewer than all pairs by a factor \(\sum_{N(\pi)>L^{C_r}}N(\pi)^{-2}\). With coefficient moments and Cauchy's inequality this keeps an arbitrarily large logarithmic saving. So the mixed term, times \(c_*\overline{S(u)}\), equals the main term of (7.2) up to the allowed error. The model square has the same main term, because \(|G(a)|^2=1\) for squarefree \(a\). The three terms of the opened square have coefficients \(1,-2,1\), so the main terms cancel.

Choose \(D_0\) first, then \(C_r\) large enough for the roughness and the sieve coprimality, then \(C_g\) large enough for the diagonal and the lattice errors. Finally use (SW) with the finitely many conductor, height and saving powers required. This proves (1.1), the last assertion of Proposition 1.1. \(\square\)

**Remark 8.1 (the logarithmic transition).** The uncorrected estimate (1.2) keeps the sparsity of prime coefficients. Suppose \(b\) is a single prime and \(a\) a product of two primes, each in its own dyad of length \(X^{1/3}L^{O(1)}\), with bounded weights. Then \(\sum|\beta_b|\ll B/L\), and (1.2) gives a bilinear bound \(O(X^{5/6}L^{-3/2})\) when \(H\gg1\); this is carried out in the lesson *Bilinear sums and the sharp cutoff*. This half power of \(L\) beyond \(X^{5/6}/L\) is what allows the transition through three primes of nearly equal norm to survive a power of \(\log L\) in the number of pieces. No power saving is needed there.

## 9. Exercises

**9.1.** Check the identity (3.2).

**9.2.** Verify that \(\lambda_d=\mu(d)\) when \(N(d)\le L^{D_0}\), and that \(|\lambda_d|\le\tau(d)^2\) in general.

**9.3.** Show that a cube in \(\mathcal O\) is congruent modulo \(3\) to a rational integer, and that \(e(\operatorname{Tr}(n/(3\lambda)))=1\) for every rational integer \(n\).

**9.4.** In the case \(x>y\) of Section 4, show directly that the ratio \(P^{2/3}Q^{1/3}/B\) is at most \(B^{-1/3+o(1)}\).

**9.5.** Verify Lemma 7.1 for the Gaussian \(W(y)=e^{-\pi a|y|^2}\), \(a>0\), by computing both sides in polar coordinates. (The lemma is stated for weights supported in an annulus, but its proof applies to this \(W\) as well.)

## 10. Solutions

**9.1.** With \(B'=B/(FV_l)\) and \(\mathcal Q=ABH^{1/3}=A^{2/3}B^{5/3}\), and \(J=kH'=kHD_d^2M/F^2\)\(=kB^2D_d^2M/(AF^2)\),
\[
\begin{aligned}
&\frac{AF}{D_d^2MB}\cdot\frac{J^{1/3}B^2}{F^2V_l^2}\cdot\frac1{A^{2/3}B^{5/3}}\\
&=\frac{A^{1/3}J^{1/3}B^{-2/3}}{D_d^2MFV_l^2}\\
&=\frac{k^{1/3}}{D_d^{4/3}M^{2/3}F^{5/3}V_l^2}.
\end{aligned}
\]

**9.2.** The function \(d\mapsto\sum_{[c_1,c_2]=d}\mu(c_1)\mu(c_2)\) is multiplicative on squarefree \(d\). At a prime \(\pi\) the pairs are \((1,\pi),(\pi,1),(\pi,\pi)\), with sum \(-1-1+1=-1=\mu(\pi)\). If \(N(d)\le L^{D_0}\), every divisor of \(d\) has norm at most \(L^{D_0}\), so the truncation has no effect. In general the number of pairs with \([c_1,c_2]=d\) is at most \(\tau(d)^2\).

**9.3.** Write \(j=a+b\omega\). Since cubing is additive modulo \(3\), \(j^3\equiv a^3+b^3\omega^3=a^3+b^3\pmod3\). For a rational integer \(n\), \(\operatorname{Tr}(n/(3\lambda))=\frac n3\operatorname{Tr}(\lambda^{-1})=0\) by Lemma 1.3 of the first lesson.

**9.4.** In exponents the ratio is \((2x+y)/3-1\). Since \(x+2y\le1\) and \(x\le1\), we have \(2x+y\le2x+\frac{1-x}2=\frac{3x+1}2\le2\), so the exponent is at most \(-\frac13\).

**9.5.** By Exercise 7.1 of the lesson on large sieves, rescaled, \(\widehat W(z)=\frac2{\sqrt3}a^{-1}e^{-4\pi|z|^2/a}\). In polar coordinates \(d\mathfrak m=\frac2{\sqrt3}r\,dr\,d\phi\), so the left side is
\[
\begin{aligned}
&\frac43\cdot\frac{2\pi}a\int_0^\infty e^{-4\pi r^6/a}r\,dr\\
&\qquad=\frac{4\pi}9\,(4\pi)^{-1/3}\,\Gamma(\tfrac13)\,a^{-2/3},
\end{aligned}
\]
by the substitution \(s=4\pi r^6/a\). The right side is
\[
\begin{aligned}
&c_*^2\,\frac{4\pi}{\sqrt3}\int_0^\infty e^{-\pi ar^2}r^{1/3}dr\\
&\qquad=c_*^2\,\frac{2\pi}{\sqrt3}\,(\pi a)^{-2/3}\,\Gamma(\tfrac23).
\end{aligned}
\]
With \(c_*^2=(2\pi)^{4/3}/(9\Gamma(\frac23)^2)\) and \(\Gamma(\frac13)=2\pi/(\sqrt3\,\Gamma(\frac23))\), both sides equal \(2^{7/3}\pi^{5/3}/(9\sqrt3\,\Gamma(\frac23))\cdot a^{-2/3}\).

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 5 (corrected dispersion) and Appendix A.4 (the angular version). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
- [DR] A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3 (2024), Section 9 (the dispersion estimate with the correction from cube frequencies, proved there under the Generalized Riemann Hypothesis). https://arxiv.org/abs/2109.07463v3
