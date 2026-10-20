# The Poisson probe

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson defines the probe \(I(X,Y,Z)\) of [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md) and evaluates it in two ways. The probe pairs the coefficient sums \(B_m(Z)\), for rows \(m\) of norm about \(XY\), with an additive polynomial: a normalized sum of \(\chi_{\mathfrak s}(d)\,\mathrm e(-md/s)\) over moduli \(\mathfrak s\) of norm about \(Y\). The first evaluation is an upper bound: by Cauchy–Schwarz, the reflected second moment of [*The quadratic large sieve and the reflected moment*](the-quadratic-large-sieve-and-the-reflected-moment.md), and a large sieve for separated additive fractions, the probe is \(O(Z^{933/2000+\epsilon})\); this is statement (P1). The second evaluation applies Poisson summation to the row variable. The rows then become frequencies \(h=ur^6\), and three Mellin integrals express the probe through Dirichlet series \(\mathcal F_u\), which Lesson 12 factors into Euler products. The use of an additive polynomial with unrestricted cubes follows [QuasiRH].

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Section 1, Lemma 2.1 and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Section 1, Lemma 3.2 and Lemma 4.1; [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Sections 2–5; [*The quadratic large sieve and the reflected moment*](the-quadratic-large-sieve-and-the-reflected-moment.md), Lemma 3.1 and Section 4; [*Norm sheets and exact Gaussian smoothing*](norm-sheets-and-exact-gaussian-smoothing.md), (5.1) and Lemma 5.1; [*Tate's local theory at the finite places*](course:NT-ADL/NT-ADL-07), Theorem 7.2; [*Tate's local theory at the infinite places*](course:NT-ADL/NT-ADL-08), Theorem 8.1.

## 1. Weights

Keep \(F\), \(S\), \(R\), \(\eta\), \(\vartheta=\overline\Lambda\,\overline G\,\eta\), the allowed generators, the additive character \(\mathrm e\) on \(F_S\) and the Fourier transform \(\widehat f(y)=\int_{F_S}f(x)\mathrm e(-xy)\,dx\) of Lesson 2, and the scales \(a,b,M_0,X=Z^a,Y=Z^b\) of Lesson 5. Every power of a residue character carries the unit mask.

Choose a nonzero nonnegative \(W_1\in C_c^\infty((0,\infty))\) and put \(\widehat W_1(w)=\int_0^\infty W_1(t)t^w\,dt/t\), an entire function. Integration by parts in \(\log t\) gives, on every closed vertical strip and for every \(A>0\),
\[
\begin{aligned}
&|\widehat W_1(\sigma+i\tau)|\\
&\quad \le C_{A}(1+|\tau|)^{-A}.\quad(1.1)
\end{aligned}
\]

**Lemma 1.1** (the row weight [OpenAI-029, (7.1)–(7.2)]). There is a product \(W_0=\bigotimes_{v\in S}W_v\) of smooth compactly supported functions \(W_v\) on \(F_v^\times\), extended by zero to \(F_v\), such that
\[
\begin{gathered}
\widehat W_0(0)=0,\\
M(1/6)\ne0,\\
M(z)=\int_{F_S^\times}\widehat W_0(y)\,|y|_S^z\,d^\times y .\quad(1.2)
\end{gathered}
\]
The function \(M\) is holomorphic on \(\operatorname{Re}z>0\), and for every compact interval \(J\subset(0,\infty)\) and every \(A>0\),
\[
\begin{gathered}
\begin{aligned}
&|M(\sigma+i\tau)|\\
&\quad \le C_{J,A}(1+|\tau|)^{-A}
\end{aligned}\\
(\sigma\in J).\quad(1.3)
\end{gathered}
\]

*Proof.* Since \(W_0\) is a product, \(\widehat W_0=\bigotimes_v\widehat W_v\) and \(M(z)=\prod_vM_v(z)\) with \(M_v(z)=\int_{F_v^\times}\widehat W_v(y)|y|_v^z\,d^\times y\). By the local functional equation (Theorem 7.2 of [*Tate's local theory at the finite places*](course:NT-ADL/NT-ADL-07) and Theorem 8.1 of [*Tate's local theory at the infinite places*](course:NT-ADL/NT-ADL-08)), applied to the quasi-character \(|\cdot|_v^{5/6}\) and the additive character \(y\mapsto\psi_v(-y)\), there is \(\rho_v\) with
\[
\begin{aligned}
M_v(1/6)&=\int_{F_v^\times}\widehat W_v(y)|y|_v^{1/6}\,d^\times y\\
&=\rho_v\int_{F_v^\times}W_v(y)|y|_v^{5/6}\,d^\times y
\end{aligned}
\]
for every Schwartz function \(W_v\). The constant \(\rho_v\) does not depend on the test function, and both integrals converge absolutely. A nonnegative nonzero test function makes the right integral positive, so \(\rho_v\) is finite; a test function whose Fourier transform is nonnegative and nonzero makes the left integral positive, so \(\rho_v\ne0\) (every Schwartz function is a Fourier transform).

At all places of \(S\) but one complex place \(v_1\), let \(W_v\) be nonnegative and nonzero, smooth and compactly supported in \(F_v^\times\). At \(v_1\) the additive measure is a constant times \(|y|_{v_1}d^\times y\), so \(\widehat W_{v_1}(0)=\int W_{v_1}(y)\,dy\) is a constant times \(\int W_{v_1}|y|_{v_1}\,d^\times y\). Take nonnegative nonzero smooth radial bumps \(b_1,b_2\) supported in \(1\le|y|_{v_1}\le2\) and \(3\le|y|_{v_1}\le4\), put \(\mu_i=\int b_i|y|^{5/6}d^\times y>0\), let \(m_i=\mu_i^{-1}\int b_i|y|\,d^\times y\) be the average of \(|y|^{1/6}\) for the weight \(b_i|y|^{5/6}d^\times y\), so \(m_1\le2^{1/6}<3^{1/6}\le m_2\), and set \(W_{v_1}=b_1-\lambda b_2\) with \(\lambda=m_1\mu_1/(m_2\mu_2)\). Then \(\int W_{v_1}|y|\,d^\times y=0\), so \(\widehat W_0(0)=0\), while \(\int W_{v_1}|y|^{5/6}d^\times y=\mu_1(1-m_1/m_2)\ne0\). Hence \(M(1/6)=\prod_v\rho_v\int W_v|y|_v^{5/6}d^\times y\ne0\).

For \(\sigma>0\) each \(\int|\widehat W_v||y|_v^\sigma\,d^\times y\) is finite: at a finite place \(\widehat W_v\) is locally constant with compact support, so the shells near \(0\) give a convergent geometric series; at a complex place \(\widehat W_v\) is bounded near \(0\) and of rapid decay. So \(M\) is holomorphic on \(\operatorname{Re}z>0\). At a complex place, an integration by parts in \(\log|y|_v\) shows that \((\sigma+i\tau)M_v(\sigma+i\tau)\) is a constant times the same integral with \(\widehat W_v\) replaced by its radial logarithmic derivative, which has the same properties; repeating gives \(M_v(\sigma+i\tau)\ll(1+|\tau|)^{-A}\) uniformly for \(\sigma\in J\), and the finite-place factors are bounded on such strips. This is (1.3). \(\square\)

## 2. The probe

For an exterior ideal \(\mathfrak s\) with allowed generator \(s\) and \(k\in R\) put
\[
\begin{aligned}
&g_{\mathfrak s}(k)\\
&\quad =\sum_{d\bmod\mathfrak s}\chi_{\mathfrak s}(d)\,\mathrm e(kd/s).\quad(2.1)
\end{aligned}
\]
The summand depends only on \(d\) modulo \(\mathfrak s\), because \(\mathrm e\) is trivial on \(R\) (Lemma 2.1 of Lesson 2), and the value does not depend on the allowed generator: replacing \(s\) by \(s\epsilon^6\), \(\epsilon\in U_S\), is undone by \(d\mapsto d\epsilon^6\), which leaves \(\chi_{\mathfrak s}(d)\) unchanged. For \(\mathfrak s=R\) the sum is \(1\).

Use the multiplicative Haar measure \(d^\times y=\frac{dT}T\,dt\), \(y=t\ell_T\), \(t\in F_S^1\), of (5.1) of Lesson 7, and on the compact group \(F_S^1/U_S^6\) the quotient measure induced by \(dt\). For \(X,Y,Z>0\) define the **probe**
\[
\begin{aligned}
&I(X,Y,Z)=\int_{F_S^1/U_S^6}\frac1Y\sum_{\mathfrak s}W_1\Bigl(\frac{q_{\mathfrak s}}Y\Bigr)\\
&\quad\times\frac1{\sqrt{q_{\mathfrak s}X}}\sum_{m\in R}q_{\mathfrak s}^{-1/2}g_{\mathfrak s}(-m)\\
&\quad\times W_0\Bigl(\frac m{t_0\ell_{q_{\mathfrak s}X}}\Bigr)B_m(Z)\,dt_0 .\quad(2.2)
\end{aligned}
\]
Here and below undecorated ideal sums run over integral exterior ideals. The term \(m=0\) vanishes because \(W_0\) is supported in \(F_S^\times\). For \(\epsilon\in U_S^6\), replacing \(t_0\) by \(\epsilon t_0\) and \(m\) by \(\epsilon m\) changes nothing: \(\chi_{\mathfrak s}(\epsilon)=\chi_{\mathfrak A}(\epsilon)=1\), so \(g_{\mathfrak s}(-\epsilon m)=g_{\mathfrak s}(-m)\) and \(B_{\epsilon m}(Z)=B_m(Z)\). So the integrand descends to the quotient, which is compact (proof of Lemma 4.1 of Lesson 2, balance); we integrate over representatives \(t_0\) in a fixed bounded subset of \(F_S^1\). For each \(t_0\) the \(m\)-sum is finite, and the \(\mathfrak s\)-sum is finite. The probe of Lesson 5 is \(I_Z=I(Z^a,Z^b,Z)\).

## 3. A large sieve for separated additive fractions

**Lemma 3.1** (separated fractions [OpenAI-029, Lemma 7.1]). Let \(K\subset F_S\) be compact and \(N,V\ge2\). For each exterior ideal \(\mathfrak s\) with \(q_{\mathfrak s}\le V\) choose a generator \(s\), and let \(\mathcal P\) be a set of distinct points of \(F_S/R\) of the form \(d/s+R\) with \(q_{\mathfrak s}\le V\) and \(d\) a unit modulo \(\mathfrak s\). Then for all complex \(b_\alpha\),
\[
\begin{aligned}
&\sum_{m\in R\cap\ell_NK}\Bigl|\sum_{\alpha\in\mathcal P}b_\alpha\,\mathrm e(m\alpha)\Bigr|^2\\
&\quad \le C_{F,S,K}\,(N+V^2)\sum_{\alpha\in\mathcal P}|b_\alpha|^2 ,\quad(3.1)
\end{aligned}
\]
and the same holds with the roles of \(m\) and \(\alpha\) exchanged.

*Proof.* *Separation.* Fractions \(d/s\), \(d'/s'\) with different ideals \(\mathfrak s\ne\mathfrak s'\) are different modulo \(R\): at a prime where the valuations of \(\mathfrak s\) and \(\mathfrak s'\) differ, the fraction with the larger denominator valuation has valuation equal to minus that valuation, and the other has larger valuation, so the difference is not integral there. For two different points and any \(r\in R\), \(d/s-d'/s'+r\)\(=(ds'-d's+rss')/(ss')\) has a nonzero numerator in \(R\), so by Lemma 2.1 of Lesson 2
\[
\begin{aligned}
&\Bigl|\frac ds-\frac{d'}{s'}+r\Bigr|_S\ge\frac1{q_{\mathfrak s}q_{\mathfrak s'}}\\
&\quad \ge V^{-2},\quad(3.2)
\end{aligned}
\]
and \(|r|_S\ge1\) for \(r\in R\setminus\{0\}\).

*A majorant.* Put \(d_F=[F:\mathbb Q]=2r\) and \(\delta=c\min(N^{-1/d_F},V^{-2/d_F})\) with a small constant \(c>0\). At each complex place choose a smooth \(\gamma\) supported in the unit disc with \(\int\gamma\ne0\), let \(\check\gamma\) be its inverse Fourier transform, and put \(\Phi_v(y)=4|\check\gamma(\delta y)|^2/|\check\gamma(0)|^2\). Then \(\Phi_v\ge0\), \(\Phi_v\ge1\) where \(\delta|y|\le c_0\) for a fixed \(c_0>0\), its Fourier transform is supported in a disc of ordinary radius \(2\delta\), and \(\int\Phi_v=O(\delta^{-2})\). At each finite place of \(S\) let \(\Phi_v\) be the indicator of a compact open subgroup \(H_v\) containing the projection of \(K\); its Fourier transform is supported in the compact open subgroup \(H_v^\perp\). The product \(\Phi=\bigotimes\Phi_v\) is nonnegative, at least \(1\) on \(\ell_NK\) once \(c\) is small (the complex components of \(\ell_N\) have ordinary modulus \(N^{1/d_F}\)), and \(\widehat\Phi(0)=\int\Phi\le C\delta^{-d_F}\le C'(N+V^2)\). A point \(\xi\) of the support of \(\widehat\Phi\) has \(|\xi|_S\le C''\delta^{d_F}\), the product of at most \((2\delta)^2\) over the \(r\) complex places and of bounded factors at the finite places. For \(c\) small this is less than \(V^{-2}\) and less than \(1\), so by (3.2) the support contains no point \(r+\beta-\alpha\) with \(r\in R\) and \(\alpha\ne\beta\) in \(\mathcal P\), and no nonzero \(r\in R\).

*Poisson summation.* Majorize the left side of (3.1) by \(\sum_{m\in R}\Phi(m)|\sum_\alpha b_\alpha\mathrm e(m\alpha)|^2\) and expand the square. By (2.1) of Lesson 2 applied to \(x\mapsto\Phi(x)\mathrm e(x(\alpha-\beta))\), whose transform is \(\xi\mapsto\widehat\Phi(\xi-\alpha+\beta)\),
\[
\begin{aligned}
&\sum_{m\in R}\Phi(m)\,\mathrm e(m(\alpha-\beta))\\
&\quad =\sum_{r\in R}\widehat\Phi(r-\alpha+\beta)\\
&\quad =\mathbf 1_{\alpha=\beta}\,\widehat\Phi(0).
\end{aligned}
\]
This gives (3.1). The exchanged inequality has the same constant, because a matrix and its adjoint have the same operator norm. \(\square\)

## 4. The bound from reflection

**Proposition 4.1** ((P1) [OpenAI-029, Proposition 7.2]). For every \(\epsilon>0\) and \(Z\ge2\),
\[
\begin{aligned}
&I(Z^a,Z^b,Z)\\
&\quad \le C_{\epsilon}\,Z^{(2M_0-1-b)/2+\epsilon}\\
&\quad =C_\epsilon\,Z^{933/2000+\epsilon}.\quad(4.1)
\end{aligned}
\]

*Proof.* Fix \(t_0\) and write the integrand of (2.2) as \(\sum_m\mathcal A(m)B_m(Z)\). Put \(v=q_{\mathfrak s}/Y\) and \(y=m/(t_0\ell_{XY})\); since \(\ell\) is multiplicative, \(m/(t_0\ell_{q_{\mathfrak s}X})=y/\ell_v\), and
\[
\begin{aligned}
\mathcal A(m)&=(XY)^{-1/2}\,\frac1Y\sum_{\mathfrak s}v^{-1/2}W_1(v)\\
&\quad\times W_0(y/\ell_v)\,q_{\mathfrak s}^{-1/2}g_{\mathfrak s}(-m).
\end{aligned}
\]
For \(v\) in the compact support of \(W_1\), \(W_0(y/\ell_v)\ne0\) forces \(y\) into a fixed compact subset of \(F_S^\times\), so the rows lie in \(\ell_{XY}K'\) for a fixed compact \(K'\). The function \((\log v,y)\mapsto v^{-1/2}W_1(v)W_0(y/\ell_v)\) is smooth in \(\log v\) with compact support; on an interval of length \(P_0\) containing that support, expand it in the Fourier series \(\sum_jc_j(y)e^{2\pi ij\log v/P_0}\), and restrict \(\mathfrak s\) to the \(q_{\mathfrak s}\) with \(\log v\) in that interval, where the expansion is valid. Two integrations by parts give \(|c_j(y)|\le C(1+j^2)^{-1}\) uniformly in \(y\), so \(\sum_j\|c_j\|_\infty<\infty\).

For each \(j\), expand \(g_{\mathfrak s}(-m)=\sum_d\chi_{\mathfrak s}(d)\mathrm e(-md/s)\) over units \(d\) modulo \(\mathfrak s\). This is a sum over the distinct fractions \(-d/s\), with coefficients of absolute value at most \(Y^{-1}q_{\mathfrak s}^{-1/2}\) and \(q_{\mathfrak s}\le CY\); their total squared mass is at most
\[
\begin{aligned}
&Y^{-2}\sum_{q_{\mathfrak s}\le CY}q_{\mathfrak s}^{-1}\,|(R/\mathfrak s)^\times|\\
&\quad \le Y^{-2}\#\{\mathfrak s:q_{\mathfrak s}\le CY\}\le CY^{-1}
\end{aligned}
\]
by Lemma 3.1 of Lesson 10. The factor \(c_j(y)\) depends on the row only and has absolute value at most \(\|c_j\|_\infty\). Lemma 3.1 with \(N=XY\), \(V=CY\), and the triangle inequality over \(j\), give
\[
\begin{aligned}
&\sum_m|\mathcal A(m)|^2\\
&\quad \le C(XY)^{-1}\,(XY+Y^2)\,Y^{-1}\\
&\quad \le CY^{-1},
\end{aligned}
\]
since \(Y\le X\) (as \(b<a\)). The rows have \(m\in\mathscr B_Z(K')\) with \(XY=Z^{M_0}\), so (4.4) of Lesson 5, proved in Lesson 10, gives \(\sum_m|B_m(Z)|^2\le C_\epsilon Z^{2M_0-1+\epsilon}\). By Cauchy–Schwarz the integrand is at most \(C_\epsilon Y^{-1/2}Z^{M_0-1/2+\epsilon/2}=C_\epsilon Z^{(2M_0-1-b+\epsilon)/2}\), uniformly in \(t_0\), and the quotient has finite measure. Finally \((2M_0-1-b)/2\)\(=(2.066-1.133)/2\)\(=933/2000\). \(\square\)

## 5. A finite Fourier transform

For an exterior ideal \(\mathfrak A\) with allowed generator \(A\), and \(k\in R\), put
\[
g_{\chi_{\mathfrak A}}(A,k)=\sum_{x\bmod\mathfrak A}\chi_{\mathfrak A}(x)\,\mathrm e(kx/A),
\]
and for \(h\in R\)
\[
\begin{aligned}
F(s,A,h)&=\sum_{\substack{d\bmod\mathfrak s\\ h\equiv Ad\ (\mathfrak s)}}\chi_{\mathfrak s}(d)\\
&\quad \,g_{\chi_{\mathfrak A}}\Bigl(A,\frac{h-Ad}s\Bigr),\quad(5.1)
\end{aligned}
\]
where \((h-Ad)/s\in R\) by the congruence. For the unit ideal the definitions mean one residue with character value \(1\).

**Lemma 5.1** ([OpenAI-029, (7.4)–(7.6)]). For all exterior ideals \(\mathfrak s,\mathfrak A\) and \(h\in R\),
\[
\begin{aligned}
&\sum_{m\bmod\mathfrak s\mathfrak A}q_{\mathfrak s}^{-1/2}g_{\mathfrak s}(-m)\,\chi_{\mathfrak A}(m)\\
&\qquad \,\mathrm e\Bigl(\frac{hm}{sA}\Bigr)=q_{\mathfrak s}^{1/2}F(s,A,h).\quad(5.2)
\end{aligned}
\]
Moreover \(|F(s,A,h)|\le q_{\mathfrak s}q_{\mathfrak A}\), and \(F(s,A,\epsilon h)=F(s,A,h)\) for \(\epsilon\in U_S^6\).

*Proof.* Insert \(g_{\mathfrak s}(-m)=\sum_d\chi_{\mathfrak s}(d)\mathrm e(-md/s)\); the left side becomes \(q_{\mathfrak s}^{-1/2}\sum_d\chi_{\mathfrak s}(d)\sum_m\chi_{\mathfrak A}(m)\)\(\mathrm e(m(h-Ad)/(sA))\). Write \(m=x+Aj\) with \(x\) modulo \(\mathfrak A\) and \(j\) modulo \(\mathfrak s\); this runs once through the residues modulo \(sAR\), and \(\chi_{\mathfrak A}(m)=\chi_{\mathfrak A}(x)\). The sum over \(j\) of \(\mathrm e(j(h-Ad)/s)\) is \(q_{\mathfrak s}\) if \(h\equiv Ad\pmod{\mathfrak s}\) and \(0\) otherwise, because \(R\) is its own annihilator (Lemma 2.1 of Lesson 2). The remaining sum over \(x\) is \(g_{\chi_{\mathfrak A}}(A,(h-Ad)/s)\). Coprimality of \(\mathfrak s\) and \(\mathfrak A\) is not needed. The bound holds because there are at most \(q_{\mathfrak s}\) residues \(d\) and \(|g_{\chi_{\mathfrak A}}|\le q_{\mathfrak A}\). For \(\epsilon\in U_S^6\), the substitutions \(d\mapsto\epsilon d\) and \(x\mapsto\epsilon^{-1}x\) in (5.1) leave every symbol unchanged and turn \(F(s,A,\epsilon h)\) into \(F(s,A,h)\). \(\square\)

## 6. Poisson summation in the rows

Put
\[
V_0(T)=\int_{F_S^1}\widehat W_0(t\ell_T)\,dt\qquad(T>0).
\]
By (5.1) of Lesson 7 its Mellin transform is \(\int_0^\infty V_0(T)T^z\,dT/T=M(z)\). As in Lemma 5.1 of Lesson 7, using one weighted supremum at a complex place and weighted integrals elsewhere, \(V_0^{\mathrm{abs}}(T)=\int_{F_S^1}|\widehat W_0(t\ell_T)|\,dt\le C_\sigma T^{-\sigma}\) for every \(\sigma>0\), and the same bounds after differentiation in \(\log T\); so \(V_0\) is smooth, and by (1.3) and Fourier inversion in \(\log T\), \(V_0(T)=\frac1{2\pi i}\int_{(\sigma)}M(z)T^{-z}\,dz\) for every \(\sigma>0\).

Let \(\mathcal U\) be the set of representatives of Lemma 3.2 of Lesson 3, so that every nonzero \(h\in R\) is \(ur^6\) modulo \(U_S^6\) for a unique \(u\in\mathcal U\) and a unique exterior ideal \(\mathfrak r\) with allowed generator \(r\); write \(q_u=|u|_S\).

**Proposition 6.1** (the Poisson expression [OpenAI-029, (7.7)]). For \(X,Y,Z>0\), with \(\mathfrak A=\mathfrak c\mathfrak n^3\) and \(A=cn^3\),
\[
\begin{aligned}
I(X,Y,Z)&=\frac{X^{1/2}}Y\\
&\quad \sum_{\substack{\mathfrak c\ \text{squarefree}\\ \mathfrak n,\mathfrak s}}\frac{\gamma_2(\mathfrak c)\,\vartheta(\mathfrak A)}{q_{\mathfrak c}^{1/2}q_{\mathfrak n}q_{\mathfrak A}}\\
&\quad \,P_G\Bigl(\frac{q_{\mathfrak A}}Z\Bigr)W_1\Bigl(\frac{q_{\mathfrak s}}Y\Bigr)\\
&\quad \sum_{u\in\mathcal U}\sum_{\mathfrak r}F(s,A,ur^6)\\
&\quad \,V_0\Bigl(\frac{Xq_uq_{\mathfrak r}^6}{q_{\mathfrak A}}\Bigr),\quad(6.1)
\end{aligned}
\]
and the right side converges absolutely.

*Proof.* Insert (3.1) of Lesson 5 for \(B_m(Z)\) into (2.2); for fixed \(t_0\) the \(m\)-sum is finite and the ideal series converges absolutely (Lemma 3.1 of Lesson 5), so the sums may be exchanged. Fix \(\mathfrak s\) and \(\mathfrak A\). The coefficient \(c(m)=q_{\mathfrak s}^{-1/2}g_{\mathfrak s}(-m)\chi_{\mathfrak A}(m)\) depends on \(m\) modulo \(sAR\). Split \(m=m_0+\ell\) with \(m_0\) modulo \(sAR\) and \(\ell\in sAR\), and apply (2.2) of Lesson 2 to \(\ell\mapsto\Phi(m_0+\ell)\), \(\Phi(x)=W_0(x/\lambda)\), \(\lambda=t_0\ell_{q_{\mathfrak s}X}\). The transform of \(x\mapsto\Phi(m_0+x)\) is \(\mathrm e(m_0\xi)\widehat\Phi(\xi)\), and \(\widehat\Phi(\xi)=|\lambda|_S\widehat W_0(\lambda\xi)\) with \(|\lambda|_S=q_{\mathfrak s}X\). With \((sAR)^\perp=(sA)^{-1}R\) and \(|sA|_S=q_{\mathfrak s}q_{\mathfrak A}\),
\[
\begin{aligned}
&\sum_{m\in R}c(m)\Phi(m)=\frac{q_{\mathfrak s}X}{q_{\mathfrak s}q_{\mathfrak A}}\\
&\qquad \sum_{h\in R}\widehat W_0\Bigl(\lambda\frac h{sA}\Bigr)\sum_{m_0\bmod sA}c(m_0)\\
&\qquad \,\mathrm e\Bigl(\frac{m_0h}{sA}\Bigr)=\frac{X\,q_{\mathfrak s}^{1/2}}{q_{\mathfrak A}}\\
&\qquad \sum_{h\in R}F(s,A,h)\,\widehat W_0\Bigl(\lambda\frac h{sA}\Bigr)
\end{aligned}
\]
by Lemma 5.1. Together with the factor \((q_{\mathfrak s}X)^{-1/2}\) of (2.2) the multiplier is \(X^{1/2}/q_{\mathfrak A}\). The term \(h=0\) vanishes because \(\widehat W_0(0)=0\).

Group the nonzero \(h\) into orbits under \(U_S^6\); \(F(s,A,\cdot)\) is constant on them by Lemma 5.1. For one orbit, the sum over its points of \(\widehat W_0(t_0\ell_{q_{\mathfrak s}X}h/(sA))\), integrated over \(t_0\in F_S^1/U_S^6\), is the integral over \(F_S^1\) of \(\widehat W_0(t\ell_{q_{\mathfrak s}X}h/(sA))\). The element \(\ell_{q_{\mathfrak s}X}h/(sA)\) has norm \(Xq_h/q_{\mathfrak A}\), and its norm-one part is absorbed by the invariance of \(dt\); so the orbit contributes \(F(s,A,h)V_0(Xq_h/q_{\mathfrak A})\). Writing the orbits as \(h=ur^6\) gives (6.1), with \(q_h=q_uq_{\mathfrak r}^6\).

The exchanges are absolute. Take \(\sigma>1\). The orbit sum of \(V_0^{\mathrm{abs}}(Xq_h/q_{\mathfrak A})\) is at most \(C_\sigma(q_{\mathfrak A}/X)^\sigma\sum_uq_u^{-\sigma}\sum_{\mathfrak r}q_{\mathfrak r}^{-6\sigma}\), finite by Lemma 4.1 of Lesson 3 and Lemma 3.1 of Lesson 10. With \(|F|\le q_{\mathfrak s}q_{\mathfrak A}\), the remaining sum over \(\mathfrak A\) of \(q_{\mathfrak c}^{-1/2}q_{\mathfrak n}^{-1}P_G(q_{\mathfrak A}/Z)q_{\mathfrak A}^{\sigma}\) converges because \(P_G(t)\le e^{\sigma'^2}t^{-\sigma'}\) for every \(\sigma'\) (Lemma 2.1 of Lesson 5), and the \(\mathfrak s\)-sum is finite. \(\square\)

## 7. Three Mellin variables

Insert the Mellin inversions \(P_G(t)=\frac1{2\pi i}\int_{(c)}e^{t'^2}t^{-t'}\,dt'\) (Lemma 2.1 of Lesson 5), \(W_1(t)=\frac1{2\pi i}\int_{(c)}\widehat W_1(w)t^{-w}\,dw\), and the inversion of \(V_0\). The factors involving \(\mathfrak A\) are \(q_{\mathfrak A}^{-1}q_{\mathfrak A}^{-t'}q_{\mathfrak A}^{z}\); the substitution \(t'=\xi+z-1\) turns them into \(q_{\mathfrak A}^{-\xi}\).

**Proposition 7.1** (three Mellin variables [OpenAI-029, (7.8)–(7.9)]). For \(X,Y,Z>0\),
\[
\begin{aligned}
I(X,Y,Z)&=\frac1{(2\pi i)^3}\\
&\quad \int_{(4)}\int_{(4)}\int_{(2)}X^{1/2-z}\\
&\quad Z^{\xi+z-1}Y^{w-1}e^{(\xi+z-1)^2}\\
&\quad M(z)\,\widehat W_1(w)\\
&\quad \sum_{u\in\mathcal U}q_u^{-z}\\
&\quad \,\mathcal F_u(\xi,w,z)\,dz\,dw\\
&\quad \,d\xi ,\quad(7.1)
\end{aligned}
\]
with \(\operatorname{Re}z=2\), \(\operatorname{Re}w=4\), \(\operatorname{Re}\xi=4\), where
\[
\begin{gathered}
\begin{aligned}
\mathcal F_u(\xi,w,z)&=\sum_{\substack{\mathfrak c\ \text{squarefree}\\ \mathfrak n,\mathfrak s,\mathfrak r}}\gamma_2(\mathfrak c)\\
&\quad \,\vartheta(\mathfrak A)\,F(s,A,ur^6)\\
&\quad \,q_{\mathfrak c}^{-1/2-\xi}q_{\mathfrak n}^{-1-3\xi}q_{\mathfrak s}^{-w}\\
&\quad q_{\mathfrak r}^{-6z},
\end{aligned}\\
\mathfrak A=\mathfrak c\mathfrak n^3 .\quad(7.2)
\end{gathered}
\]

*Proof.* After the three inversions in (6.1), the power of \(q_{\mathfrak A}\) is \(q_{\mathfrak A}^{-1-t'+z}=q_{\mathfrak A}^{-\xi}\), and \(q_{\mathfrak c}^{-1/2}q_{\mathfrak n}^{-1}q_{\mathfrak A}^{-\xi}=q_{\mathfrak c}^{-1/2-\xi}q_{\mathfrak n}^{-1-3\xi}\). The remaining powers are \(X^{1/2}X^{-z}\), \(Z^{t'}\), \(Y^{-1}Y^{w}\), \(q_{\mathfrak s}^{-w}\) and \((q_uq_{\mathfrak r}^6)^{-z}\). On the stated lines, \(|F|\le q_{\mathfrak s}q_{\mathfrak A}\) and \(|\gamma_2(\mathfrak c)|=1\) bound the series (7.2) by \(\zeta_F^S(7/2)\zeta_F^S(10)\zeta_F^S(3)\zeta_F^S(12)\), and \(\sum_uq_u^{-2}\) converges by Lemma 4.1 of Lesson 3. In the integrals, \(M(z)\) and \(\widehat W_1(w)\) decay faster than any power of the height, by (1.3) and (1.1), and \(e^{(\xi+z-1)^2}\) decays like a Gaussian in \(\operatorname{Im}(\xi+z)\); in the height variables \(\operatorname{Im}(\xi+z)\), \(\operatorname{Im}z\), \(\operatorname{Im}w\) the integrand is absolutely integrable. So all exchanges are justified. \(\square\)

Lesson 12 factors \(\mathcal F_u\) into an Euler product. The term \(u=1\) contains \(1/L^S(\xi,\eta)\) and produces the main term of (P2); the other \(u\) are controlled in Lesson 13.

## 8. Exercises

**8.1.** Show that \(g_{R}(k)=1\) and that \(g_{\mathfrak p}(0)=0\) for an exterior prime \(\mathfrak p\).

**8.2.** In Lemma 3.1, show directly that two reduced fractions \(d/s\) and \(d'/s\) with the same denominator are equal modulo \(R\) exactly when \(d\equiv d'\pmod{\mathfrak s}\).

**8.3.** Check the exponent in Proposition 4.1: \(M_0=a+b\), and \(\frac{2M_0-1-b}2=\frac a2+\frac b2-\frac12\). Evaluate it for \(a=9/10\), \(b=133/1000\).

**8.4.** Let \(\mathfrak A=R\). Show that \(F(s,1,h)=\chi_{\mathfrak s}(h)\), and that (5.2) is then the Fourier inversion formula on \(R/\mathfrak s\) for the function \(\chi_{\mathfrak s}\), whose transform is \(g_{\mathfrak s}\).

**8.5.** Verify that the substitution \(t'=\xi+z-1\) turns \(Z^{t'}e^{t'^2}\) and \(q_{\mathfrak A}^{-1-t'+z}\) into the factors displayed in (7.1) and (7.2).

## 9. Solutions

**8.1.** For \(\mathfrak s=R\) there is one residue and the character value is \(1\). For \(k=0\), \(g_{\mathfrak p}(0)=\sum_d\chi_{\mathfrak p}(d)=0\), because \(\chi_{\mathfrak p}\) is a nontrivial character of \(k_{\mathfrak p}^\times\) extended by zero.

**8.2.** \(d/s-d'/s=(d-d')/s\) lies in \(R\) exactly when \(d-d'\in sR=\mathfrak s\).

**8.3.** \(\frac{2(a+b)-1-b}2=\frac{2a+b-1}2=\frac a2+\frac b2-\frac12\). For the given values, \(\frac{1.8+0.133-1}2=\frac{0.933}2=\frac{933}{2000}\).

**8.4.** With \(\mathfrak A=R\), \(A=1\), \(\chi_R=1\) and \(g_{\chi_R}(1,k)=1\); the congruence \(h\equiv d\pmod{\mathfrak s}\) leaves one residue \(d=h\), so \(F(s,1,h)=\chi_{\mathfrak s}(h)\). Then (5.2) reads \(\sum_{m\bmod\mathfrak s}g_{\mathfrak s}(-m)\mathrm e(hm/s)=q_{\mathfrak s}\chi_{\mathfrak s}(h)\), which is Fourier inversion on \(R/\mathfrak s\) for the function \(\chi_{\mathfrak s}\), whose transform is \(g_{\mathfrak s}\).

**8.5.** \(Z^{t'}=Z^{\xi+z-1}\), \(e^{t'^2}=e^{(\xi+z-1)^2}\), and \(-1-t'+z=-1-\xi-z+1+z=-\xi\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 7.1–7.2. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [QuasiRH] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*, OpenAI Math Release preprint, 30 September 2026, Part I, Sections 6–7. https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026
