# The level formula and Type I sums

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Type I sum has a short outer variable \(r\) with arbitrary coefficients and a long, smoothly weighted inner variable \(u\):
\[
\sum_ra_r\sum_uG(ru)\,W_r\Bigl(\frac{N(u)}U\Bigr).
\]
For a single \(r\) the inner sum is a smoothed partial sum of the Dirichlet series \(\sum_uG(ru)N(u)^{-s}\), which has a pole at \(s=5/6\). Dunn and Radziwiłł proved a summation formula for it, a Voronoi formula in the level \(r\), whose main term is that pole. This lesson shows that the main term is exactly the contribution of the model \(c_*\mu^2(ru)N(ru)^{-1/6}\). It then bounds the Type I sums with the model subtracted, and also after twisting by \(N(u)^{it}\) at large heights \(t\). Everything is done for every fixed angular order \(\ell\), as the last lesson needs the twisted sums.

**Prerequisites.** The previous lessons, [*Cubic Gauss sums and Patterson's conjecture*](cubic-gauss-sums-and-pattersons-conjecture.md) and [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md), with their notation. From *The Riemann zeta function*: [*The Gamma function and Stirling's formula*](course:NT-ZETA/NT-ZETA-03), Theorem 2.2 (reflection) and Theorem 3.1 (Stirling).

## 1. Notation

For \(\ell\in\mathbb Z\) and \(z\ne0\) put \(\theta_\ell(z)=(z/|z|)^\ell\), and for primary \(n\)
\[
\begin{gathered}
G_\ell(n)=\theta_\ell(n)G(n),\\
\mathcal D_\ell(n)=G_\ell(n)-\frac{c_*\,\theta_\ell(n)\,\mu^2(n)}{N(n)^{1/6}}.
\end{gathered}
\]
The function \(\theta_\ell\) is multiplicative, and \(\mathcal D_\ell(n)=0\) unless \(n\) is squarefree. Put
\[
A_0=\frac{(2\pi)^{5/3}}{3^{7/2}\,\Gamma(2/3)} .
\]
The primary elements form the coset \(1+3\mathcal O\), of index \(9\) in \(\mathcal O\), so they have density \(\frac2{9\sqrt3}\) per unit of Euclidean area. In the variable \(N(z)=|z|^2\) this becomes \(\frac{2\pi}{9\sqrt3}\) per unit length. One checks directly that
\[
c_*\cdot\frac{2\pi}{9\sqrt3}=A_0 .
\tag{1.1}
\]
Indeed both sides equal \((2\pi)^{5/3}/(3^{3}\sqrt3\,\Gamma(2/3))\).

## 2. The level Voronoi formula

For primary squarefree \(r\), \(R=N(r)\), a smooth function \(W\) with compact support in \((0,\infty)\), \(V>0\) and \(\ell\in\mathbb Z\), put
\[
\begin{aligned}
&\mathcal C_{r,\ell}(V;W)\\
&=\sum_{\substack{d,u\\ (d,r)=1}}|d|\,G(ru)\,\theta_\ell(rud^3)\\
&\qquad\cdot W\Bigl(\frac{N(ud^3)}V\Bigr).
\end{aligned}
\]
The variable \(d\) completes the sum over \(u\) by cubes; the completion is removed in Section 4.

**Theorem 2.1 (the level Voronoi formula, N2).** For \(0<\sigma<10^{-4}\) and \(k=|\ell|/2\) put
\[
\begin{gathered}
Q_\ell(z)=\frac{\Gamma(\frac56+k-z)\Gamma(\frac76+k-z)}{\Gamma(z+k-\frac16)\Gamma(z+k+\frac16)},\\
\check W_\ell(v)=\frac1{2\pi i}\int_{(-\sigma)}v^zQ_\ell(z)\,\mathcal MW(z)\,dz .
\end{gathered}
\]
Then
\[
\begin{aligned}
&\mathcal C_{r,\ell}(V;W)\\
&=\mathbf 1_{\ell=0}\,A_0\,\mathcal MW(\tfrac56)\,V^{5/6}\frac{\varphi(r)}{R^{7/6}}\\
&\quad+\frac{R^{1/2}\,\theta_{3\ell}(r)}{3^{7/2}(2\pi)^2}\,\Sigma_{r,\ell}(V;W),
\end{aligned}
\]
with the dual sum
\[
\begin{aligned}
\Sigma_{r,\ell}&=\sum_{\substack{\nu,\,d\\ (d,r)=1}}\frac{a_r(\nu)\,b_r(\nu)\,\theta_{-\ell}(d^3\nu)}{N(\nu)\,N(d)^{5/2}}\\
&\qquad\cdot\check W_\ell\Bigl(\frac{(2\pi)^4N(d^3\nu)V}{R^2}\Bigr),
\end{aligned}
\]
over \(0\ne\nu\in\lambda^{-1}\mathcal O\) and primary \(d\). The coefficients \(a_r(\nu),b_r(\nu)\) depend only on \(r\) and \(\nu\). They vanish unless
\[
\nu=\lambda^j\zeta\,h\,w\,h'^3,\qquad j\ge-1,
\]
with a unit \(\zeta\), primary \(h,h',w\), \(h\) and \(h'\) composed of primes dividing \(r\), \(w\) prime to \(r\), and \(hw\) squarefree. On this support,
\[
\begin{gathered}
|a_r(\nu)|\ll3^{\max(j,0)/3}\,|h'|,\\
|b_r(\nu)|\le N\bigl((\lambda\nu,r)\bigr).
\end{gathered}
\]

Theorem 2.1 is Proposition 5.3 of [DR], multiplied by \(G(r)\theta_\ell(r)\), and it is used without proof in the programme. Its left side becomes \(\mathcal C_{r,\ell}\) because \(G(ru)=\overline{\chi_r(u)}G(r)G(u)\) for \(u\) prime to \(r\), and both sides vanish otherwise. In the main term and the dual factor, \(G(r)\overline{g(r)}=R^{1/2}\) and \(\theta_\ell(r)(\bar r/r)^{-\ell}=\theta_{3\ell}(r)\). The coefficients are \(a_r=a^\dagger\) and \(b_r=b_r^\dagger\) of Proposition 5.2 of [DR], with the support stated there. The bound for \(b_r\) is immediate from its formula \(b_r(\nu)=\mu(r/(\lambda\nu,r))\varphi(r)/\varphi(r/(\lambda\nu,r))\). For \(j\ge0\), \(a_r(\nu)\) is the conjugate of a Fourier coefficient \(\tau(\mu)\) of Patterson's cubic theta function, whose formula is recorded in Section 5.1 of [DR]. These coefficients are Gauss sums of absolute value \(|c|\) times \(|d/c|\,3^{n/2+O(1)}\) at arguments \(\lambda^{3n-3}cd^3\) or \(\lambda^{3n-4}cd^3\), up to units. At \(\nu\) as above the argument has \(d=h'\) and \(n\le\frac23j+O(1)\), which gives the bound. For \(j=-1\) the two other cusp coefficients \(\tau_1,\tau_2\) are bounded by \(9|d|\).

**Lemma 2.2 (the truncated formula).** Let \(\ell\) be fixed, and suppose that \(V,V^{-1},R\le X^{C_0}\), that \(W\) is supported in a fixed compact subinterval of \((0,\infty)\), and that its derivatives of each fixed order are bounded by a fixed power of \(L\). Then
\[
\begin{aligned}
&\mathcal C_{r,\ell}(V;W)\\
&=\mathbf 1_{\ell=0}A_0\,\mathcal MW(\tfrac56)\,V^{5/6}\frac{\varphi(r)}{R^{7/6}}\\
&\quad+O_{\ell,\epsilon}\bigl(X^\epsilon R^{1/2}\bigr).
\end{aligned}
\]

**Proof.** On the line \(\operatorname{Re}z=-\sigma\), Stirling's formula gives \(|Q_\ell(z)|\ll_{\ell,\sigma}(1+|\operatorname{Im}z|)^{2+4\sigma}\). Indeed each of the two quotients \(\Gamma(a-z)/\Gamma(z+b)\) has size \(|\operatorname{Im}z|^{1+2\sigma}\). With the decay of \(\mathcal MW\) from Lemma 1.2 of the previous lesson,
\[
\begin{aligned}
&\Bigl|\check W_\ell\Bigl(\frac{(2\pi)^4N(d^3\nu)V}{R^2}\Bigr)\Bigr|\\
&\qquad\ll X^{O(\sigma)}L^{O(1)}N(d^3\nu)^{-\sigma}.
\end{aligned}
\]
It remains to bound \(\sum|a_rb_r|N(\nu)^{-1-\sigma}N(d)^{-5/2-3\sigma}\). It factors over the parts of \(\nu\).

- At a prime \(\pi\mid r\) of norm \(p\), let \(e\in\{0,1\}\) and \(k\ge0\) be its exponents in \(h\) and \(h'\). The local factor is at most
\[
\begin{aligned}
&\sum_{e=0}^1\sum_{k\ge0}p^{\mathbf 1_{e+k>0}}\,p^{k/2}\,p^{-(e+3k)(1+\sigma)}\\
&\qquad=1+p^{-\sigma}+O\bigl(p^{-3/2-3\sigma}\bigr).
\end{aligned}
\]
- For fixed \(\eta>0\), the product of these factors over \(\pi\mid r\) is \(O_{\sigma,\eta}(R^\eta)\): finitely many small primes give a bounded factor, and each other factor is at most \(p^\eta\).
- The sum over \(w\) converges at the exponent \(1+\sigma\).
- The powers of \(\lambda\) give at most \(\sum_{j\ge-1}3^{j/3}3^{-j(1+\sigma)}<\infty\).
- The sum over \(d\) converges at the exponent \(\frac52+3\sigma\).

Choosing \(\sigma\) and \(\eta\) small in terms of \(\epsilon\) gives the bound \(X^\epsilon R^{1/2}\) for the dual term. \(\square\)

## 3. Lattice sums over squarefree elements

**Lemma 3.1.** Let \(r\) be primary and squarefree, \(U\ge1\) bounded by a power of \(X\), and \(W\) smooth with fixed compact support in \((0,\infty)\), with derivatives of fixed order bounded by fixed powers of \(L\).

(a)
\[
\begin{aligned}
&\sum_{(u,r)=1}\mu^2(u)\,W\Bigl(\frac{N(u)}U\Bigr)\\
&=\frac{2\pi U}{9\sqrt3}\,\mathcal MW(1)\,\frac{\varphi(r)}{N(r)}\sum_{(c,r)=1}\frac{\mu(c)}{N(c)^2}\\
&\quad+O_\epsilon(X^\epsilon\sqrt U).
\end{aligned}
\]

(b) For every fixed integer \(\ell\ne0\),
\[
\begin{aligned}
&\sum_{(u,r)=1}\mu^2(u)\,\theta_\ell(u)\,W\Bigl(\frac{N(u)}U\Bigr)\\
&\qquad\ll_{\ell,\epsilon}X^\epsilon\sqrt U.
\end{aligned}
\]

**Proof.** For primary \(u\), the indicator that \(u\) is squarefree and prime to \(r\) equals
\[
\sum_{\substack{d\mid r\\d\mid u}}\mu(d)\sum_{\substack{c^2\mid u\\ (c,r)=1}}\mu(c),
\]
and the conditions say \(u=c^2dv\) with primary \(v\). For a smooth function \(f\) on \(\mathbb C\) supported in an annulus of radii comparable to \(\sqrt Y\), with \(|\nabla f|\ll L^C/\sqrt Y\), comparing each fundamental cell of \(1+3\mathcal O\) with its integral gives
\[
\begin{aligned}
\sum_{v\in1+3\mathcal O}f(v)&=\frac2{9\sqrt3}\int_{\mathbb C}f\,dA\\
&\quad+O\bigl(L^C(1+\sqrt Y)\bigr).
\end{aligned}
\]
(a) For \(f(z)=W(|z|^2/Y)\) the integral is \(\pi Y\mathcal MW(1)\). With \(Y=U/N(c^2d)\), and \(N(c)\ll\sqrt U\) for nonempty sums,
\[
\sum_{d\mid r}\frac{\mu(d)}{N(d)}=\frac{\varphi(r)}{N(r)} ,
\]
and completing the sum over \(c\) costs \(O(\sqrt U)\). The errors add up to \(O(\tau(r)L^C\sqrt U\log U)\).

(b) Here \(\theta_\ell(u)=\theta_\ell(c^2d)\theta_\ell(v)\), and \(f(z)=\theta_\ell(z)W(|z|^2/Y)\) has integral zero, because \(\int_0^{2\pi}e^{i\ell\phi}d\phi=0\). Its gradient is \(O_\ell(L^C/\sqrt Y)\) on its support, so only the error terms remain. \(\square\)

## 4. Type I sums at bounded heights

**Proposition 4.1 (Type I comparison).** Let \(\ell\) be fixed, \(RU\asymp X\) and \(1\le R\ll X^{0.51}\). Let \((a_r)\) be divisor-bounded and supported on \(r\) of length \(R\). Let \(W_r\) be smooth functions supported in a common fixed compact subinterval of \((0,\infty)\), whose derivatives of each fixed order are bounded by a fixed power of \(L\), uniformly in \(r\). Then
\[
\begin{aligned}
&\sum_ra_r\sum_u\mathcal D_\ell(ru)\,W_r\Bigl(\frac{N(u)}U\Bigr)\\
&\qquad\ll_\ell X^{5/6-1/100}.
\end{aligned}
\]

**Proof.** Only squarefree \(r\) contribute. For such \(r\) we have the exact identity
\[
\begin{aligned}
&\sum_uG_\ell(ru)\,W_r\Bigl(\frac{N(u)}U\Bigr)\\
&=\sum_{(c,r)=1}\mu(c)\,|c|\,\theta_{3\ell}(c)\\
&\qquad\cdot\mathcal C_{r,\ell}\Bigl(\frac U{N(c)^3};W_r\Bigr).\quad(4.1)
\end{aligned}
\]
Indeed, expanding the right side and putting \(e=cd\), the term with \(u\) and \(e\) carries \(|e|\,\theta_\ell(rue^3)\sum_{c\mid e}\mu(c)\), which vanishes unless \(e=1\). All sums are finite. Let
\[
\begin{gathered}
C_*=X^{0.13}\ \text{ if }R\le X^{0.40},\\
C_*=X^{0.02}\ \text{ if }R>X^{0.40}.
\end{gathered}
\]

*Short completions.* For \(N(c)\le C_*\) apply Lemma 2.2. Its error terms, summed over \(c\) with \(|c|=N(c)^{1/2}\) and over \(r\), give
\[
X^\epsilon R^{3/2}C_*^{3/2}\ll X^{0.795+\epsilon}
\]
in both ranges of \(R\).

*Main terms and the model, \(\ell=0\).* The main terms of Lemma 2.2, completed to all \(c\), give
\[
\begin{aligned}
&A_0\,\mathcal MW_r(\tfrac56)\,U^{5/6}\frac{\varphi(r)}{R^{7/6}}\\
&\qquad\cdot\sum_{(c,r)=1}\frac{\mu(c)}{N(c)^2},\quad(4.2)
\end{aligned}
\]
with a completion error \(O(X^{5/6+\epsilon}C_*^{-1})\) after summing over \(r\). On the other side, the model is
\[
\begin{aligned}
&\sum_uc_*\frac{\mu^2(ru)}{N(ru)^{1/6}}W_r\Bigl(\frac{N(u)}U\Bigr)\\
&=\frac{c_*}{(RU)^{1/6}}\sum_{(u,r)=1}\mu^2(u)\,\widetilde W_r\Bigl(\frac{N(u)}U\Bigr),
\end{aligned}
\]
with \(\widetilde W_r(x)=x^{-1/6}W_r(x)\), up to the factor \((N(r)/R)^{-1/6}\), which is put into \(\widetilde W_r\). Lemma 3.1(a), with \(\mathcal M\widetilde W_r(1)=\mathcal MW_r(\frac56)\), and the identity (1.1) show that the model equals (4.2) up to \(O(X^\epsilon R^{-1/6}U^{1/3})\). Summed over \(r\), this is
\[
X^\epsilon R^{5/6}U^{1/3}\asymp X^{1/3+\epsilon}R^{1/2}\ll X^{0.589+\epsilon}.
\]

*Main terms and the model, \(\ell\ne0\).* Lemma 2.2 has no main term, and Lemma 3.1(b) bounds the model by the same \(X^{0.589+\epsilon}\).

*Long completions.* It remains to bound the terms of (4.1) with \(N(c)>C_*\). Combine \(c\) and \(d\) into \(e=cd\) and restrict \(N(e)\) to a dyad of length \(E\gg C_*\). The coefficient of \(e\) is
\[
|e|\,\theta_{3\ell}(e)\sum_{\substack{c\mid e\\N(c)>C_*}}\mu(c),
\]
divisor-bounded times \(E^{1/2}\). The inner variable \(u\) then has length \(U/E^3\). Bounding \(|G|\le1\) gives
\[
\ll X^{1+\epsilon}E^{-3/2},
\]
which is \(O(X^{0.805+\epsilon})\) when \(R\le X^{0.40}\). When \(R>X^{0.40}\), fix \(e\) and write \(G(ru)=\overline{\chi_u(r)}G(r)G(u)\). Separate the weights \(W_r\) by Mellin inversion: the dependence on \(r\) passes into the outer coefficients, with a common integrable majorant. By Cauchy's inequality in \(r\) and Theorem 4.1 of the previous lesson, both variables being squarefree, the sum over \(r,u\) is
\[
\begin{gathered}
\ll X^\epsilon\sqrt{RU_e}\,\bigl(R+U_e+(RU_e)^{2/3}\bigr)^{1/2},\\
U_e=U/E^3 .
\end{gathered}
\]
Summing the coefficients of the \(e\) in the dyad costs \(X^\epsilon E^{3/2}\), so the dyad contributes
\[
\ll X^{1/2+\epsilon}\Bigl(R+\frac U{E^3}+\Bigl(\frac X{E^3}\Bigr)^{2/3}\Bigr)^{1/2}.
\]
For \(X^{0.40}<R\ll X^{0.51}\) and \(E\gg X^{0.02}\), the three terms have exponents at most
\[
\begin{gathered}
0.755,\qquad 0.77,\\
\frac12+\frac{1-0.06}3=\frac56-\frac1{50}.
\end{gathered}
\]
The completion error of the main term, \(X^{5/6+\epsilon}C_*^{-1}\), has the same last exponent in this range. All the exponents are below \(\frac56-\frac1{100}\) after the small losses, and there are \(O(L)\) dyads. \(\square\)

## 5. Type I sums at large heights

At heights \(T\) up to \(X^{1/6+\rho}\), the model term is treated separately (in the lesson *Bilinear sums and the sharp cutoff*), and the Gauss sums are bounded alone. The tool is a mean value over \(t\) of the completed sums twisted by \(N(\cdot)^{it}\):
\[
\begin{aligned}
&\mathcal C_{r,\ell,t}(V;W)\\
&=\sum_{\substack{d,u\\ (d,r)=1}}|d|\,G(ru)\,\theta_\ell(rud^3)\\
&\qquad\cdot N(ud^3)^{it}\,W\Bigl(\frac{N(ud^3)}V\Bigr),
\end{aligned}
\]
\[
\begin{aligned}
&M_{r,\ell,t}(V;W)\\
&=\mathbf 1_{\ell=0}\,A_0\,\mathcal MW(\tfrac56+it)\\
&\qquad\cdot V^{5/6+it}\,\frac{\varphi(r)}{R^{7/6}} .
\end{aligned}
\]

**Lemma 5.1 (completed sums at large heights).** Let \(\ell\) be fixed, \(r\) primary and squarefree, \(R=N(r)\), and let \(W\) be supported in a fixed compact subinterval of \((0,\infty)\), with derivatives bounded independently of \(X\). For \(T\ge2\), \(V\gg1\) and \(R,V,T\le X^{O(1)}\),
\[
\begin{aligned}
&\int_{T\le|t|\le2T}\bigl|\mathcal C_{r,\ell,t}(V;W)\\
&\qquad-M_{r,\ell,t}(V;W)\bigr|\,\frac{dt}T\\
&\ll_{\ell,\epsilon}X^\epsilon\sqrt V\,R^{1/4}\sqrt T .
\end{aligned}
\]

**Proof.** *Short sums: \(V\le\sqrt R\,T^2\).* Collect the terms with equal \(m=N(ud^3)\). By Lemma 1.1 of the previous lesson the squared coefficients sum to
\[
\begin{aligned}
&\ll X^\epsilon\sum_dN(d)\,\#\{u:N(ud^3)\asymp V\}\\
&\ll X^\epsilon V\sum_dN(d)^{-2}\ll X^\epsilon V .
\end{aligned}
\]
The mean value inequality (Lemma 5.1 of the previous lesson) and Cauchy's inequality bound the mean of \(|\mathcal C_{r,\ell,t}|\) by \(X^\epsilon\sqrt V(1+V/T)^{1/2}\le X^\epsilon\sqrt VR^{1/4}\sqrt T\). For \(\ell=0\), the subtracted term is \(O_D(V^{5/6}R^{-1/6}T^{-D})\) by the decay of \(\mathcal MW\). Its ratio to the claimed bound is at most \(V^{1/3}R^{-5/12}T^{-D-1/2}\le R^{-1/4}T^{1/6-D}\le1\) for \(D\ge1\).

*Long sums: \(V>\sqrt R\,T^2\).* Apply Theorem 2.1 to \(W_t(x)=W(x)x^{it}\), whose Mellin transform is \(\mathcal MW(z+it)\), and multiply by \(V^{it}\). The main term is \(M_{r,\ell,t}\). In \(\check W_\ell\), move the line of integration to \(\operatorname{Re}z=-A\). There \(|Q_\ell(z)|\ll(1+|\operatorname{Im}z|)^{2+4A}\), and the decay of \(\mathcal MW(z+it)\) in \(\operatorname{Im}z+t\) bounds the transform at \(v=(2\pi)^4N(d^3\nu)V/R^2\) by
\[
\ll v^{-A}T^{2+4A}=T^2\Bigl(\frac{R^2T^4}{(2\pi)^4N(d^3\nu)V}\Bigr)^{A}.
\]
For a fixed small \(\delta>0\) and large \(A\), the terms with \(N(d^3\nu)>I_{\max}=X^\delta R^2T^4/V\) are therefore smaller than every fixed power of \(X^{-1}\). This holds after summing the absolutely convergent coefficients of Lemma 2.2. The cutoff does not depend on \(t\). The retained frequencies satisfy \(N(d^3\nu)\le I_{\max}\le X^\delta R^{3/2}T^2\).

For the retained terms, move the line back to \(\operatorname{Re}z=\frac12\). No pole is crossed, since the poles of \(\Gamma(\frac56+\frac{|\ell|}2-z)\) lie at \(\operatorname{Re}z\ge\frac56\). On this line \(|Q_\ell(\frac12+iy)|=1\), because each quotient \(\Gamma(a-iy)/\Gamma(a+iy)\) with real \(a\) has absolute value one. After the substitution \(y\mapsto y-t\), the transform is an integral of \(\mathcal MW(\frac12+iy)\) against \(N(d^3\nu)^{i(y-t)}\) times factors of absolute value one. Minkowski's inequality in \(y\) reduces the claim to the mean over \(t\) of Dirichlet polynomials in \(N(d^3\nu)\). Their coefficients have absolute value a constant times
\[
\sqrt V\,R^{-1/2}\,\frac{|a_r(\nu)b_r(\nu)|}{N(d)\sqrt{N(\nu)}} .
\]

Fix \(d,j,\zeta,h,h'\) in \(\nu=\lambda^j\zeta hwh'^3\), and put \(D_d=N(d)\), \(E=N(h)\), \(P'=N(h')\) and \(g=N((\lambda\nu,r))\le\min(R,EP')\). The free squarefree variable \(w\) has length at most \(Y'=I_{\max}/(D_d^3\,3^jEP'^3)\). By the bounds of Theorem 2.1 its coefficients are \(N(w)^{-1/2}\) times
\[
\sqrt V\,R^{-1/2}\,\frac{3^{-j/6}\,g}{D_d\,P'\sqrt E}.
\]
By the mean value inequality on dyads of \(N(w)\), the mean over \(t\) is at most \(X^\epsilon\) times this factor times \(1+\sqrt{Y'/T}\).

For the term \(1\), use \(g\le\sqrt{REP'}\). The sum over \(j\) is geometric and the sum over \(d\) is \(O(L)\). There are at most \(\tau(r)\) choices of \(h\), since \(h\) is squarefree and divides \(r\), and \(\sum_{h'}P'^{-1/2}\ll R^\epsilon\). The total is \(O(X^\epsilon\sqrt V)\).

For the term \(\sqrt{Y'/T}\), use \(g\le EP'\). The total is at most
\[
\begin{aligned}
&X^\epsilon\sqrt V\sqrt{\frac{I_{\max}}{RT}}\sum_{d,j,h,h'}\frac{3^{-2j/3}}{D_d^{5/2}P'^{3/2}}\\
&\qquad\ll X^{\epsilon+\delta}\sqrt V\,R^{1/4}\sqrt T .
\end{aligned}
\]
Choosing \(\delta\) small proves the lemma. \(\square\)

**Proposition 5.2 (Type I at large heights).** Let \(\ell\) be fixed, \(RU\asymp X\), \((a_r)\) divisor-bounded on \(r\) of length \(R\), and let \(W_r\) be smooth with a common fixed compact support in \((0,\infty)\) and derivatives bounded independently of \(X\). For \(2\le T\le X^{O(1)}\) and every fixed \(D>0\),
\[
\begin{aligned}
&\int_{T\le|t|\le2T}\sum_r|a_r|\\
&\quad\cdot\Bigl|\sum_uG_\ell(ru)N(u)^{it}W_r\Bigl(\frac{N(u)}U\Bigr)\Bigr|\frac{dt}T\\
&\ll_{\ell,\epsilon}X^{1/2+\epsilon}R^{3/4}T^{1/2}\\
&\quad+\mathbf 1_{\ell=0}O_D\bigl(X^{5/6}L^CT^{-D}\bigr),
\end{aligned}
\]
where \(C\) depends only on the coefficient bounds.

**Proof.** Only squarefree \(r\) contribute. Twisting (4.1) by \(N(u)^{it}\) gives the same identity with \(\mathcal C_{r,\ell,t}\) and the extra factor \(N(c)^{3it}\). If \(b_0\) bounds the supports of the \(W_r\), only \(N(c)\le(b_0U)^{1/3}\) contribute, and then \(V=U/N(c)^3\ge1/b_0\). By Lemma 5.1 the error terms contribute
\[
\begin{aligned}
&\sum_r|a_r|\sum_{N(c)\ll U^{1/3}}|c|\,X^\epsilon\sqrt{\frac U{N(c)^3}}\\
&\qquad\cdot R^{1/4}\sqrt T\ll X^\epsilon RL^C\sqrt UR^{1/4}\sqrt T,
\end{aligned}
\]
which is \(X^{1/2+\epsilon}R^{3/4}T^{1/2}\). For \(\ell=0\), the terms \(M_{r,0,t}\) are \(O_D(U^{5/6}N(c)^{-5/2}R^{-1/6}T^{-D})\). The sum over \(c\) converges, and summing over \(r\) gives \(X^{5/6}L^CT^{-D}\). \(\square\)

**Remark 5.3.** For \(\ell=0\) the same bound can be obtained from Heath-Brown's mean-square estimate for the Dirichlet series \(\sum_uG(ru)N(u)^{-s}\) on the line \(\operatorname{Re}s=\frac12+\epsilon\); this is the route of [OpenAI-023], Proposition 3.2. The proof above uses only the level formula.

Two ranges of Proposition 5.2 are used later. With \(R\le X^{0.40}\) and \(T\ll X^{0.01}\), the exponent of the first term is at most \(\frac12+\frac34(0.40)+\frac12(0.01)=0.805\). With \(R\le X^{1/3-\kappa/2}\) and \(T\ll X^{1/6+\rho}\), it is
\[
\begin{aligned}
&\frac12+\frac34\Bigl(\frac13-\frac\kappa2\Bigr)+\frac12\Bigl(\frac16+\rho\Bigr)\\
&\qquad=\frac56-\frac{3\kappa}8+\frac\rho2 ,
\end{aligned}
\]
which is below \(\frac56\) when \(\rho<\frac34\kappa\).

## 6. Exercises

**6.1.** Verify the identity (1.1).

**6.2.** Show that \(|Q_\ell(\frac12+iy)|=1\) for all real \(y\), and that on the line \(\operatorname{Re}z=-\sigma\) the function \(Q_\ell\) grows like \(|\operatorname{Im}z|^{2+4\sigma}\).

**6.3.** In the proof of Proposition 4.1, check the claim that the short-completion error \(X^\epsilon R^{3/2}C_*^{3/2}\) is \(O(X^{0.795+\epsilon})\) in both ranges of \(R\). Check also that the trivial bound for the long completions is \(O(X^{0.805+\epsilon})\) when \(R\le X^{0.40}\).

**6.4.** Explain why the identity (4.1) would fail if the coefficient \(\theta_{3\ell}(c)\) were replaced by \(\theta_{\ell}(c)\).

**6.5.** Let \(\ell\ne0\) and let \(W\) be a fixed smooth function with compact support in \((0,\infty)\). Use Poisson summation (Lemma 2.1 of the previous lesson) to show that
\[
\begin{aligned}
&\sum_{v\in1+3\mathcal O}\theta_\ell(v)W(N(v)/Y)\\
&\qquad=O_{\ell,W,A}(Y^{-A})
\end{aligned}
\]
for every \(A>0\). Why does the proof of Lemma 3.1 use only the weaker bound \(O(1+\sqrt Y)\)?

## 7. Solutions

**6.1.** \(c_*\frac{2\pi}{9\sqrt3}=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)}\cdot\frac{2\pi}{9\sqrt3}=\frac{(2\pi)^{5/3}}{27\sqrt3\,\Gamma(2/3)}\), and \(27\sqrt3=3^{7/2}\).

**6.2.** At \(z=\frac12+iy\) the two quotients are \(\Gamma(\frac13+k-iy)/\Gamma(\frac13+k+iy)\) and \(\Gamma(\frac23+k-iy)/\Gamma(\frac23+k+iy)\), with \(k=|\ell|/2\). Since \(\Gamma(\bar w)=\overline{\Gamma(w)}\), each has absolute value one. On \(\operatorname{Re}z=-\sigma\), Stirling's formula gives \(|\Gamma(a+iy)|\asymp|y|^{a-1/2}e^{-\pi|y|/2}\) for fixed real \(a\) and large \(|y|\). The first quotient therefore has size \(|y|^{(\frac56+k+\sigma-\frac12)-(k-\sigma-\frac16-\frac12)}=|y|^{1+2\sigma}\), and the second has the same size.

**6.3.** For \(R\le X^{0.40}\): \(\frac32(0.40)+\frac32(0.13)=0.795\). For \(X^{0.40}<R\ll X^{0.51}\): \(\frac32(0.51)+\frac32(0.02)=0.795\). The trivial bound is \(X^{1+\epsilon}E^{-3/2}\) with \(E\gg X^{0.13}\), and \(1-\frac32(0.13)=0.805\).

**6.4.** After \(e=cd\) the angular factor of a term is \(\theta_{3\ell}(c)\theta_\ell(rud^3)=\theta_\ell(ru)\theta_{3\ell}(cd)\)\(=\theta_\ell(rue^3)\). Only this combination depends on \(c\) and \(d\) through \(e\) alone, which is what makes \(\sum_{c\mid e}\mu(c)\) appear. With \(\theta_\ell(c)\) the coefficient of a fixed \(e\) would be \(\sum_{c\mid e}\mu(c)\theta_{-2\ell}(c)\), which does not vanish for \(e\ne1\) in general.

**6.5.** Put \(f(z)=\theta_\ell(z)W(|z|^2/Y)\). Lemma 2.1 of the previous lesson with \(b=3\), \(c=1\) gives
\[
\sum_{v\in1+3\mathcal O}f(v)=\frac19\sum_{y\in\lambda^{-1}\mathcal O}e\Bigl(\operatorname{Tr}\frac y3\Bigr)\widehat f\Bigl(\frac y3\Bigr).
\]
The term \(y=0\) is \(\frac19\int f\,d\mathfrak m=0\), since the angular integral of \(e^{i\ell\phi}\) vanishes. The function \(f\) is supported where \(|z|\asymp\sqrt Y\), and each derivative of order \(k\) is \(O_{\ell,W,k}(Y^{-k/2})\), since both \(\theta_\ell\) and \(W(|z|^2/Y)\) vary on the scale \(\sqrt Y\). Integrating by parts \(k\) times gives \(|\widehat f(\eta)|\ll Y\,(\sqrt Y|\eta|)^{-k}\). For \(y\ne0\) we have \(|y/3|\ge1/(3\sqrt3)\), and summing over \(y\) with \(k\ge3\) gives \(O(Y^{1-k/2})\). In Lemma 3.1 the weights have derivatives bounded only by powers of \(L\), and the sums occur with \(Y=U/N(c^2d)\) ranging down to \(1\). The cell comparison gives one bound valid uniformly in all these cases, and it is sufficient.

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Section 2.3 (the level input in its required form), Section 3 (Type I estimates) and Appendix A.2 (the angular Voronoi formula and the completed sums at large heights). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
- [DR] A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3 (2024), Proposition 5.2 (the dual coefficients), Proposition 5.3 (the level Voronoi formula) and the formulas for the coefficients of the cubic theta function in its Section 5.1. https://arxiv.org/abs/2109.07463v3
