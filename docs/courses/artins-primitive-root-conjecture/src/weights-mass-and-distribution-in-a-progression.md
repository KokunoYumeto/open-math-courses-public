# Weights, mass and distribution in a progression

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson sets up the construction that proves Proposition 5.1 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md). Integers \(d=crQ+1\) in a fixed progression, with \(Q>x^{0.9}\) prime and \(r\) composed of primes from the groups of [*Marked Type II estimates and rough factors*](marked-type-ii-estimates.md), receive nonnegative weights \(w(d)\) built from the marked weight \(\mathcal W\). Three facts about these weights are proved here: the marked Type II estimate holds inside the progression; the total weight \(X_0\) is of order \(xJ_0/L\), where \(J_0\) is a harmonic sum over the group integers \(r\); and the family is well distributed in the sense of the Bombieri–Vinogradov theorem, which is what the sieve of Lesson 19 needs. Lesson 19 then shows that a positive proportion of the weight sits on primes.

**Prerequisites.** [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md), (4.1) and Proposition 5.1; [*A block sieve and rough-number densities*](a-block-sieve-and-rough-number-densities.md), (1.1)–(1.3); [*Marked Type II estimates and rough factors*](marked-type-ii-estimates.md), Section 1, N6 and Proposition 5.1; [*The Bombieri–Vinogradov theorem*](course:NT-DIRL/NT-DIRL-15), Theorem 3.1 and Corollary 4.1; [*The Siegel–Walfisz theorem*](course:NT-DIRL/NT-DIRL-11), Theorem 2.1; [*Counting primes by elementary means: Chebyshev and Mertens*](course:NT-ZETA/NT-ZETA-02), Theorems 3.1 and 4.2; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4.

## 1. The weights

Fix \(M,c,u\) as in (4.1) of Lesson 1:
\[
\begin{gathered}
8\mid M,\quad c\in\{2,4\},\quad(u,M)=1,\\
c\mid u-1,\quad\Bigl(\frac{u-1}c,\frac Mc\Bigr)=1 .\quad(1.1)
\end{gathered}
\]
Use \(L\), \(W\), \(V\) of Lesson 16 and the groups \(\mathcal P_i\) and the marked weight \(\mathcal W\) of Lesson 17 with \(q=\frac12\); the integer \(K\) and the exponents \(0.1<a_1<\cdots<a_K<0.2\) are fixed before \(x\) grows and chosen at the end of Lesson 19. For large \(x\) the group primes lie in \((\exp(L^{0.1}),\exp(L^{0.3}))\), so they do not divide \(M\). A **group integer** is a positive integer all of whose prime factors are group primes (including \(1\)), and \(h_{\mathcal P}\) is the largest group-integer divisor of \(h\).

Fix a smooth \(\Psi\) supported in \((1,2)\) with \(0\le\Psi\le1\) and \(A_\Psi=\int_1^2\Psi>0\), and put
\[
\begin{aligned}
&F(h)=\mathbf 1_{\{h/h_{\mathcal P}=cQ,\ Q>x^{0.9}\ \text{prime}\}},\\
&w(d)=\mathbf 1\{d\equiv u\ (M)\}\,\Psi(d/x)\\
&\qquad\times F(d-1)\,\mathcal W(d-1)\\
&\qquad(d\ge2),\quad(1.2)
\end{aligned}
\]
and \(w(1)=0\). Since \((ph)_{\mathcal P}=p\,h_{\mathcal P}\) for every group prime \(p\), \(F\) is group-invariant: \(F(ph)=F(h)\).

**Lemma 1.1** (support). If \(w(d)\ne0\), then \(d=crQ+1\) with \(r=(d-1)_{\mathcal P}\) a group integer and \(Q>x^{0.9}\) prime, uniquely, and
\[
\begin{gathered}
r\le x^{0.11},\\
\mathcal W(d-1)=\mathcal W(r),\\
0\le w(d)\le B_K ,\quad(1.3)
\end{gathered}
\]
with \(B_K\) depending only on \(K\).

*Proof.* Neither \(c\) nor \(Q\) has a group prime factor (group primes are odd and smaller than \(x^{0.9}\)), so \(r=(d-1)_{\mathcal P}\), the group primes of \(d-1\) are those of \(r\), and \(r\le2x/x^{0.9}\). Finally \(\omega_i(h)2^{1-\omega_i(h)}\le1\), so \(\mathcal W\le\prod_iV_i^{-1}\), which is bounded since \(V_i\to\log2\). \(\square\)

The total weight is \(X_0=\sum_dw(d)\). The aim of Lessons 18–19 is \(\sum_{d\ \text{prime}}w(d)\gg X_0/L\), together with \(X_0\gg x/L\); with \(w\le B_K\) this gives \(\gg x/L^2\) primes.

## 2. The marked estimate in the progression

For fixed \(\gamma>0\) and integers \(m\), put
\[
\begin{gathered}
R_\gamma(m)=\mathbf 1\{P^-(m)>x^\gamma\},\\
\begin{aligned}
B_\gamma(m)&=\frac{D_\gamma(\log m/L)}{L\,V(W)}\\
&\quad \,\mathbf 1\{P^-(m)>W\},
\end{aligned}\quad(2.1)
\end{gathered}
\]
with the densities \(D_\gamma\) of Lesson 16.

**Lemma 2.1** (Type II in the progression [OpenAI-029, Lemma 12.1]). Fix \(\delta>0\) and \(0<\gamma<s_-<s_+<1\). Let \(H_m,H_n\ge x^\delta\) with \(H_mH_n\asymp x\), let \(I\subseteq[H_m,2H_m]\) be an interval with \([\log H_m/L,\log(2H_m)/L]\subseteq[s_-,s_+]\), and let \(|b_n|\le1\) be supported on \(W\)-rough integers in \([H_n,2H_n]\). There is \(K_0\), independent of the \(a_i\), such that for \(K\ge K_0\)
\[
\begin{aligned}
&\Bigl|\sum_{m\in I,\,n}\bigl(R_\gamma(m)-B_\gamma(m)\bigr)\,b_n\,w(mn)\Bigr|\\
&\quad \le C\,x\,L^{-6},\quad(2.2)
\end{aligned}
\]
uniformly in the dyads, the interval and the coefficients.

*Proof.* Since \((u,M)=1\), orthogonality of the characters \(\lambda\) modulo \(M\) gives \(\mathbf 1\{mn\equiv u\ (M)\}\)\(=\varphi(M)^{-1}\sum_\lambda\overline{\lambda(u)}\lambda(m)\lambda(n)\). Let \(\widehat\psi(v)=\frac1{2\pi}\int_{\mathbb R}\Psi(e^s)e^{-ivs}\,ds\), a Schwartz function; Fourier inversion in \(\log y\) (Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017)) gives \(\Psi(mn/x)=\int_{\mathbb R}\widehat\psi(v)x^{-iv}m^{iv}n^{iv}\,dv\). For \(|v|\le L\) and each \(\lambda\), apply N6 of Lesson 17 to the group-invariant \(F\) of (1.2), with \(C=2\), \(D_*=6\), \(\alpha_m=\mathbf 1_I(m)m^{iv}\lambda(m)(R_\gamma(m)-B_\gamma(m))\) and \(\beta_n=b_n\lambda(n)n^{iv}\). The proof of Proposition 5.1 of Lesson 17 shows that \(\mathbf 1_I(m)m^{iv}(R_\gamma(m)-B_\gamma(m))\) satisfies (2.2) of Lesson 17; multiplying by \(\lambda(m)\) keeps this property, because \(\lambda\chi\) is a character of modulus at most \(ML^{A_0}\le L^{A_0+1}\). Both sequences are supported on \(W\)-rough integers and bounded by \(L^2\), since \(x^\gamma>W\), \(D_\gamma\) is bounded on \([s_-,s_+]\) and \(LV(W)\asymp L^{0.76}\). For \(|v|>L\), \(\int_{|v|>L}|\widehat\psi|\le C_AL^{-A}\), while the bilinear sum is \(O(x)\) by (1.3). Integrating over \(v\) and summing the \(\varphi(M)\) characters gives (2.2). \(\square\)

## 3. The harmonic mass

For group integers \(r\) put
\[
\begin{gathered}
J_0=\sum_r\frac{\mathcal W(r)}r,\\
A_r=\sum_{\substack{Q>x^{0.9}\ \text{prime}\\ crQ+1\equiv u\ (M)}}\Psi\Bigl(\frac{crQ+1}x\Bigr),\\
X_0=\sum_r\mathcal W(r)A_r .\quad(3.1)
\end{gathered}
\]

**Lemma 3.1** (harmonic mass [OpenAI-029, Lemma 12.2]). With \(E_i(t)=\prod_{p\in\mathcal P_i}\bigl(1+\frac t{p-1}\bigr)\),
\[
\begin{aligned}
J_0&=\prod_{i=1}^K\frac{E_i'(1/2)}{V_i}\\
&=\prod_{i=1}^K\Bigl\{\frac{E_i(1/2)}{V_i}\sum_{p\in\mathcal P_i}\frac1{p-\frac12}\Bigr\}.\quad(3.2)
\end{aligned}
\]
Moreover, for every fixed \(\epsilon>0\),
\[
\begin{gathered}
1\le J_0\le C_K,\\
\begin{aligned}
&\sum_{r>x^\epsilon}\frac{\mathcal W(r)}r\\
&\quad \le C_K\exp\bigl(-\epsilon L^{1-a_K}\bigr),
\end{aligned}\quad(3.3)
\end{gathered}
\]
and \(A_r\le Cx/r\); so the part of \(X_0\) with \(r>x^\epsilon\) is \(O_K(x\exp(-\epsilon L^{1-a_K}))\).

*Proof.* Summing \(p^{-j}\) over \(j\ge1\) gives \(1/(p-1)\), so \(E_i(t)=\sum t^{\omega(r_i)}/r_i\) over the integers \(r_i\) supported on \(\mathcal P_i\), and \(E_i'(t)=\sum\omega(r_i)t^{\omega(r_i)-1}/r_i\). With \(q=\frac12\), \(\mathcal W(r)=\prod_i\omega_i(r)2^{1-\omega_i(r)}/V_i\), and a group integer factors uniquely as \(\prod_ir_i\); this gives the first expression in (3.2), and logarithmic differentiation of \(E_i\) gives the second. The integers with one prime, to the first power, from each group contribute \(\prod_i(V_i^{-1}\sum_{p\in\mathcal P_i}p^{-1})=1\), and all terms are nonnegative, so \(J_0\ge1\). Put \(s=L^{-a_K}\). A group prime has \(p\le\exp(2L^{a_K})\), so \(p^s\le e^2\) and \(\sum_{j\ge1}p^{-j(1-s)}\le2e^2/p\) for large \(x\). Bounding \(\mathcal W\) by \(B_K\),
\[
\begin{aligned}
\sum_r\frac{\mathcal W(r)}{r^{1-s}}&\le B_K\prod_{p\ \text{group}}\Bigl(1+\frac{2e^2}p\Bigr)\\
&\le B_K\exp\Bigl(2e^2\sum_iV_i\Bigr)\\
&\le C_K ,
\end{aligned}
\]
which bounds \(J_0\), and on \(r>x^\epsilon\) the factor \(r^{-s}\le x^{-\epsilon s}=\exp(-\epsilon L^{1-a_K})\) gives the tail. Finally \(A_r\) counts at most \(x/(cr)+1\) values of \(Q\). \(\square\)

## 4. Distribution of the family

Fix parameters
\[
\begin{gathered}
0<\kappa<0.01,\quad 0<\epsilon<\kappa,\\
0<b<0.01,\quad D=x^{1/2-\kappa/2},\quad(4.1)
\end{gathered}
\]
and put \(N=M/c\). For an odd squarefree \(\ell\), let \(A_r(\ell)\) be \(A_r\) restricted to \(\ell\mid crQ+1\), and
\[
\begin{gathered}
g_r(\ell)=\frac{\mathbf 1\{(\ell,Mr)=1\}}{\varphi(\ell)},\\
E_r(\ell)=A_r(\ell)-g_r(\ell)A_r ,\quad(4.2)
\end{gathered}
\]
so \(g_r(1)=1\), \(E_r(1)=0\).

**Lemma 4.1** (distribution [OpenAI-029, Lemma 12.3]). For every fixed \(A>0\),
\[
\begin{aligned}
&\sum_{r\le x^\epsilon}\mathcal W(r)\sum_{\substack{\ell\le D\\ \ell\ \text{odd squarefree}}}|E_r(\ell)|\\
&\quad\le C_A\,x\,J_0\,L^{-A}.\quad(4.3)
\end{aligned}
\]
Moreover
\[
\begin{gathered}
X_0\sim\frac{x\,J_0\,A_\Psi}{c\,\varphi(N)\,L}\\
(x\to\infty),\quad(4.4)
\end{gathered}
\]
and in particular \(X_0\asymp xJ_0/L\), with constants depending only on \(M\) and \(\Psi\).

*Proof.* *Classes.* For \(r\le x^\epsilon\), \(d=crQ+1\in(x,2x)\) forces \(Q\ge x^{1-\epsilon}/4>x^{0.9}\). The condition \(d\equiv u\pmod M\) is \(rQ\equiv\frac{u-1}c\pmod N\); since \(r\) is prime to \(M\) and \(\frac{u-1}c\) is prime to \(N\) by (1.1), it is one reduced class of \(Q\) modulo \(N\). If an odd prime of \(\ell\) divides \(r\), it cannot divide \(crQ+1\); if it divides \(M\), it cannot divide \(d\equiv u\), as \((u,M)=1\); so \(A_r(\ell)=g_r(\ell)=0\) when \((\ell,Mr)>1\). Otherwise \(\ell\mid crQ+1\) is the reduced class \(Q\equiv-(cr)^{-1}\pmod\ell\), and the two conditions form one reduced class modulo \(N\ell\).

*Bombieri–Vinogradov.* With
\[
\begin{aligned}
&E_\pi(Y,k)=\max_{2\le y\le Y}\ \max_{(v,k)=1}\\
&\qquad\Bigl|\pi(y;k,v)-\frac{\operatorname{li}(y)}{\varphi(k)}\Bigr| ,
\end{aligned}
\]
Corollary 4.1 of [*The Bombieri–Vinogradov theorem*](course:NT-DIRL/NT-DIRL-15), (4.2), gives for fixed \(A',\eta>0\) and large \(Y\)
\[
\begin{aligned}
&\sum_{k<Y^{1/2-\eta}}E_\pi(Y,k)\\
&\quad \le C\,Y(\log Y)^{-A'} ,\quad(4.5)
\end{aligned}
\]
because \(Y^{1/2-\eta}\le\sqrt Y(\log Y)^{-A'-2}\) for large \(Y\). For \(r\le x^\epsilon\) take \(Y=2x/(cr)\ge x^{1-\epsilon}/2\). The moduli \(N\ell\le ND\) lie below \(Y^{1/2-\eta}\) for large \(x\), with \(\eta=(\kappa-\epsilon)/4\), because
\[
\begin{aligned}
&(1-\epsilon)\Bigl(\frac12-\eta\Bigr)-\Bigl(\frac12-\frac\kappa2\Bigr)\\
&\quad =\frac{(\kappa-\epsilon)(1+\epsilon)}4>0 .
\end{aligned}
\]
Put \(I_r=\frac x{cr}\int_1^2\frac{\Psi(y)\,dy}{\log((xy-1)/(cr))}\); the substitution \(t=(xy-1)/(cr)\) turns it into \(\int\Psi((crt+1)/x)\,dt/\log t\). Write \(A_r(\ell)\) as a Stieltjes integral of \(\Psi((crt+1)/x)\) against \(\pi(t;N\ell,v)\) and integrate by parts. The main term \(\operatorname{li}(t)/\varphi(N\ell)\) returns \(I_r/\varphi(N\ell)\), and the remainder is at most \(E_\pi(Y,N\ell)\int|\Psi'|\), where \(\int|\Psi'|\) does not depend on \(r\). Distinct \(\ell\) give distinct moduli \(N\ell\), so (4.5) gives
\[
\begin{aligned}
&\sum_{\substack{\ell\le D\\ \ell\ \text{odd squarefree}}}\Bigl|A_r(\ell)-\frac{g_r(\ell)}{\varphi(N)}I_r\Bigr|\\
&\quad\le C_{A'}\frac xrL^{-A'} ,\quad(4.6)
\end{aligned}
\]
since \(g_r(\ell)/\varphi(N)=1/\varphi(N\ell)\) when \((\ell,Mr)=1\), and both terms vanish otherwise. The term \(\ell=1\) gives \(A_r=I_r/\varphi(N)+O((x/r)L^{-A'})\). Replacing \(I_r/\varphi(N)\) by \(A_r\) in the other terms costs \(\sum_{\ell\le D}g_r(\ell)\le\sum_{\ell\le D}1/\varphi(\ell)\le CL\) times this error (expand \(n/\varphi(n)=\sum_{d\mid n}\mu^2(d)/\varphi(d)\)). With \(A'=A+1\) and the weights \(\mathcal W(r)\), (4.3) follows.

*The mass.* For \(r\le x^\epsilon\) and \(y\in(1,2)\), \(\log((xy-1)/(cr))\asymp L\), so \(I_r\asymp x/(rL)\), and the \(\ell=1\) term and Lemma 3.1 give \(X_0\asymp xJ_0/L\), the part \(r>x^\epsilon\) being negligible since \(J_0\ge1\). For (4.4), fix \(0<\theta<\epsilon\). For \(r\le x^\theta\), \(\log((xy-1)/(cr))=L+O(\theta L+1)\), so \(I_r=\frac{xA_\Psi}{crL}(1+O(\theta)+O(L^{-1}))\) with constants independent of \(\theta\). Summing the \(\ell=1\) evaluation over \(r\le x^\theta\) with weights, and bounding the parts \(r>x^\theta\) of \(X_0\) and of \(J_0\) by Lemma 3.1, gives \(\frac{c\,\varphi(N)\,L\,X_0}{x\,J_0\,A_\Psi}=1+O(\theta)+o_\theta(1)\). Let \(x\to\infty\), then \(\theta\to0\). \(\square\)

For \((M,c,u)=(8,4,5)\), \(N=2\) and (4.4) reads \(X_0\sim xJ_0A_\Psi/(4L)\).

## 5. The singular product

Put
\[
\begin{gathered}
V_M(y)=\prod_{\substack{2<p\le y\\ p\nmid M}}\Bigl(1-\frac1{p-1}\Bigr),\\
\begin{aligned}
\mathfrak S_M&=2\prod_{p>2}\Bigl(1-\frac1{(p-1)^2}\Bigr)\\
&\quad\times\prod_{\substack{p\mid M\\ p>2}}\Bigl(1-\frac1{p-1}\Bigr)^{-1}>0 .\quad(5.1)
\end{aligned}
\end{gathered}
\]

**Lemma 5.1** ([OpenAI-029, (12.10)–(12.11)]). As \(y\to\infty\), \(V_M(y)\sim\mathfrak S_MV(y)\) and \(V(y)\sim e^{-\gamma_E}/\log y\). For group integers \(r\le x^{0.11}\) and all \(y\),
\[
\begin{gathered}
\sum_{p\mid r}\frac1p\le0.11\,L^{0.9}e^{-L^{0.1}}=o(1),\\
\begin{aligned}
&\prod_{2<p\le y}\bigl(1-g_r(p)\bigr)\\
&\quad =(1+o(1))\,V_M(y),
\end{aligned}\quad(5.2)
\end{gathered}
\]
uniformly, with an \(o(1)\) independent of \(K\).

*Proof.* Compare factors with \(V(y)\): the prime \(2\) contributes \(2\); an odd \(p\nmid M\) contributes \(\frac{1-1/(p-1)}{1-1/p}=1-\frac1{(p-1)^2}\); an odd \(p\mid M\) contributes \((1-1/p)^{-1}=\bigl(1-\frac1{(p-1)^2}\bigr)\bigl(1-\frac1{p-1}\bigr)^{-1}\). The product of \(1-(p-1)^{-2}\) converges, which gives \(V_M\sim\mathfrak S_MV\); Mertens' product theorem (Theorem 4.2 of [*Counting primes by elementary means*](course:NT-ZETA/NT-ZETA-02)) gives the second relation. A group integer \(r\le x^{0.11}\) has at most \(0.11L/L^{0.1}\) prime factors, each above \(e^{L^{0.1}}\); this gives the first part of (5.2), and the product differs from \(V_M(y)\) by \(\prod_{p\mid r,\,p\le y}(1-\frac1{p-1})^{-1}=1+o(1)\). \(\square\)

## 6. Exercises

**6.1.** Show that \(j2^{1-j}\le1\) for every integer \(j\ge1\), and compute \(\mathcal W(r)\) for \(r=p_1p_2\cdots p_K\) with one prime \(p_i\) from each group.

**6.2.** For \((M,c,u)=(8,4,5)\), describe the class of \(Q\) modulo \(N=2\) and check that every odd prime \(Q\) is allowed.

**6.3.** Verify the identity \((1-\epsilon)(\frac12-\eta)-(\frac12-\frac\kappa2)=\frac{(\kappa-\epsilon)(1+\epsilon)}4\) for \(\eta=\frac{\kappa-\epsilon}4\).

**6.4.** Show that \(\sum_{\ell\le D}1/\varphi(\ell)\le C\log D\) from \(\frac n{\varphi(n)}=\sum_{d\mid n}\frac{\mu^2(d)}{\varphi(d)}\).

**6.5.** Compute \(\mathfrak S_8\).

## 7. Solutions

**6.1.** \(j2^{1-j}\) is \(1\) for \(j=1,2\) and decreases for \(j\ge2\). For \(r=p_1\cdots p_K\), every \(\omega_i(r)=1\) and \(\mathcal W(r)=\prod_iV_i^{-1}\).

**6.2.** \(rQ\equiv\frac{5-1}4=1\pmod2\): \(Q\) odd, which every prime \(Q>2\) is.

**6.3.** The left side is \(\frac\kappa2-\eta-\frac\epsilon2+\epsilon\eta\)\(=\frac{2\kappa-\kappa+\epsilon-2\epsilon}4+\frac{\epsilon(\kappa-\epsilon)}4\)\(=\frac{(\kappa-\epsilon)(1+\epsilon)}4\).

**6.4.** \(\sum_{\ell\le D}\frac1{\varphi(\ell)}=\sum_{\ell\le D}\frac1\ell\sum_{d\mid\ell}\frac{\mu^2(d)}{\varphi(d)}\)\(\le\sum_d\frac{\mu^2(d)}{d\,\varphi(d)}\sum_{k\le D}\frac1k\), and \(\sum_d\mu^2(d)/(d\varphi(d))\) converges.

**6.5.** \(M=8\) has no odd prime factor, so \(\mathfrak S_8=2\prod_{p>2}(1-(p-1)^{-2})\approx1.3203\), twice the twin prime constant.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 12.1–12.2. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
