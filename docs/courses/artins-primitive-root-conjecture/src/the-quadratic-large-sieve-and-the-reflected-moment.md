# The quadratic large sieve and the reflected moment

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Proposition 4.1 of [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), the bound for the mean square of \(B_m(Z)\) over a box of rows. The reflected expansion of [*The Weyl reflection*](the-weyl-reflection.md) writes \(B_m(Z)\) as a bilinear form in the squarefree part \(\mathfrak d\) of the row and a squarefree column ideal \(\mathfrak c'\), coupled by the quadratic symbol \(\chi_{\mathfrak d}(c')^3\) and by a profile that decays rapidly once \(q_{\mathfrak c'}\) exceeds \(q_{\mathfrak d}^2q_{\mathfrak f}^2/Z\). A large sieve inequality for quadratic characters over number fields, due to Goldmakher and Louvel and extending Heath-Brown's theorem over \(\mathbb Q\), bounds such bilinear forms. The lesson checks that the exterior symbols form a family to which it applies, and then estimates the retained part of the expansion with it and the remaining part with the decay of the profile.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Section 3 and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Proposition 2.1 and Lemma 3.1; [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Section 4; [*Norm sheets and exact Gaussian smoothing*](norm-sheets-and-exact-gaussian-smoothing.md), Corollary 5.2; [*A theta expression for the coefficient sums*](a-theta-expression-for-the-coefficient-sums.md), Lemmas 1.1 and 2.1; [*The Weyl reflection*](the-weyl-reflection.md), (2.2), Lemma 2.2, Lemma 3.1, Section 4 and Lemma 5.1; [*Counting ideals of bounded norm*](course:NT-ANT/counting-ideals-of-bounded-norm), Theorem 15.3; [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06), Proposition 6.1; [*Hensel's lemma, squares and roots of unity in p-adic fields*](course:NT-LOC/NT-LOC-03), Corollary 1.2; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4.

## 1. Quadratic Hecke families

Let \(k\) be a number field and \(\mathfrak c_0\) a nonzero integral ideal of \(\mathcal O_k\). Write \(I(\mathfrak c_0)\) for the set of nonzero integral ideals prime to \(\mathfrak c_0\), and \(I^{\mathrm{sf}}(\mathfrak c_0)\) for its squarefree members. The **infinite type** of a Hecke character \(\chi\) of modulus \(\mathfrak f\) is the character \(\chi_\infty\) of \(k\otimes_{\mathbb Q}\mathbb R\) with \(\chi((x))=\chi_\infty(x)\) for every \(x\in\mathcal O_k\) with \(x\equiv1\pmod{\mathfrak f}\).

**Definition 1.1** (Goldmakher and Louvel [GL, Definition 1], for \(n=2\)). A **quadratic Hecke family** with respect to \(\mathfrak c_0\) is a collection \(\{\chi_{\mathfrak a}:\mathfrak a\in I^{\mathrm{sf}}(\mathfrak c_0)\}\) of primitive Hecke characters of trivial infinite type such that

1. the order of each \(\chi_{\mathfrak a}\) divides \(2\);
2. there are a finite group \(G\), a homomorphism \([\cdot]\) from the multiplicative monoid \(I(\mathfrak c_0)\) to \(G\), and a map \(C\colon G\times G\to\{\pm1\}\) with \(\chi_{\mathfrak a}(\mathfrak b)=\chi_{\mathfrak b}(\mathfrak a)\,C([\mathfrak a],[\mathfrak b])\) for all coprime \(\mathfrak a,\mathfrak b\) in the family;
3. for all coprime \(\mathfrak a,\mathfrak b\) in the family with \([\mathfrak a]=[\mathfrak b]\), the character \(\chi_{\mathfrak a}\overline{\chi_{\mathfrak b}}\) is a primitive Hecke character of conductor \(\mathfrak a\mathfrak b\).

**Named result N3** (Goldmakher and Louvel [GL, Theorem 1.1]). Let \(\{\chi_{\mathfrak a}\}\) be a quadratic Hecke family with respect to \(\mathfrak c_0\). For every \(\epsilon>0\), all \(M,N\ge1\) and all complex numbers \(\lambda_{\mathfrak b}\),
\[
\begin{aligned}
&\sum_{\substack{\mathfrak a\in I^{\mathrm{sf}}(\mathfrak c_0)\\ q_{\mathfrak a}\le M}}\Bigl|\sum_{\substack{\mathfrak b\in I^{\mathrm{sf}}(\mathfrak c_0)\\ q_{\mathfrak b}\le N}}\lambda_{\mathfrak b}\,\chi_{\mathfrak b}(\mathfrak a)\Bigr|^2\\
&\quad \le C_{k,\mathfrak c_0,\epsilon}\,(MN)^\epsilon(M+N)\\
&\qquad \sum_{\substack{\mathfrak b\in I^{\mathrm{sf}}(\mathfrak c_0)\\ q_{\mathfrak b}\le N}}|\lambda_{\mathfrak b}|^2 .
\end{aligned}
\] It extends Heath-Brown's large sieve for quadratic characters over \(\mathbb Q\) [HB]. It is used without proof in the programme.

## 2. The family of exterior quadratic symbols

Keep \(F\supseteq\mu_{12}\), \(S\) and the allowed generators of Lessons 2–4. For each finite place \(v\in S\) choose \(m_v\ge1\) with \(1+\mathfrak p_v^{m_v}\subseteq F_v^{\times2}\) (possible because \(F_v^{\times2}\) is open), and let \(\mathfrak q_S=\prod_{v\in S\ \text{finite}}\mathfrak p_v^{m_v}\). Exterior ideals correspond to the ideals in \(I(\mathfrak q_S)\), with the same norms and the same multiplication.

For a squarefree exterior ideal \(\mathfrak c\) with allowed generator \(c\), let \(\Xi_{\mathfrak c}=\kappa_c^3\), with \(\kappa_c\) the Kummer character of Lemma 3.1 of Lesson 3. Let \(B_2\) be the image of \(B\) in \(F_S^\times/F_S^{\times2}\) and \(\mathrm{cl}_2(\mathfrak a)\in B_2\) the class of an allowed generator of an exterior ideal \(\mathfrak a\).

**Lemma 2.1** (the exterior family [OpenAI-029, Lemma 6.4]). The characters \(\Xi_{\mathfrak c}\) form a quadratic Hecke family with respect to \(\mathfrak q_S\), with \(G=B_2\), \([\cdot]=\mathrm{cl}_2\) and \(C=1\). For every exterior ideal \(\mathfrak d\),
\[
\Xi_{\mathfrak c}(\mathfrak d)=\chi_{\mathfrak d}(c)^3 ,
\tag{2.1}
\]
both sides being \(0\) when \(\mathfrak c\) and \(\mathfrak d\) share a prime.

*Proof.* *The characters.* Two allowed generators differ by an element of \(U_S^6\), whose Kummer character is trivial (Lemma 3.1(3) of Lesson 3); so \(\Xi_{\mathfrak c}\) is well defined. By Lemma 3.1(1) of Lesson 3 and \((a,b)_{6,v}^3=(a,b)_{2,v}\) (Section 3 of Lesson 2), \(\Xi_{\mathfrak c}\) is a Hecke character of order dividing \(2\) with local components \(y\mapsto(c,y)_{2,v}\). At a complex place a character of finite order is trivial, because \(\mathbb C^\times\) is connected; so the infinite type is trivial.

*Conductor.* At an exterior prime \(\mathfrak p\nmid\mathfrak c\), \(c\) is a unit and the symbol of two units is \(1\), so the component is unramified. At \(\mathfrak p\mid\mathfrak c\), principal units are squares (Corollary 1.2 of [*Hensel's lemma, squares and roots of unity in p-adic fields*](course:NT-LOC/NT-LOC-03), as \(\mathfrak p\nmid2\)), so the conductor exponent is at most \(1\) (Proposition 6.1 of [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06)); and with \(c=pu_c\), a unit \(u\) gives \((c,u)_{2,\mathfrak p}=(p,u)_{2,\mathfrak p}=(u,p)_{2,\mathfrak p}^{-1}\)\(\equiv u^{-(q_{\mathfrak p}-1)/2}\), which is \(-1\) for a nonsquare unit by (3.2) and Lemma 3.1 of Lesson 2; so the exponent is exactly \(1\). At a finite \(v\in S\) the component is trivial on \(1+\mathfrak p_v^{m_v}\). So the conductor is \(\mathfrak c\mathfrak s_{\mathfrak c}\) with \(\mathfrak s_{\mathfrak c}\mid\mathfrak q_S\).

*Values.* At an exterior prime \(\mathfrak d\nmid\mathfrak c\), \(\Xi_{\mathfrak c}(\mathfrak d)=\kappa_c(\mathfrak d)^3=\chi_{\mathfrak d}(c)^3\) by Lemma 3.1(1) of Lesson 3. At \(\mathfrak d\mid\mathfrak c\) the prime divides the conductor, so the ideal character vanishes, and \(\chi_{\mathfrak d}(c)^3=0\) by the unit mask. Both sides of (2.1) are multiplicative in \(\mathfrak d\).

*Reciprocity.* The map \(\mathrm{cl}_2\) is well defined, since \(U_S^6\subseteq F_S^{\times2}\), and multiplicative, since products of allowed generators are allowed generators of the product (Lemma 4.1 of Lesson 2); its image lies in the finite group \(B_2\). For coprime squarefree \(\mathfrak c,\mathfrak d\), (2.2) of Lesson 3 with \(\epsilon=1\) gives \(\chi_{\mathfrak d}(c)=\chi_{\mathfrak c}(d)\), hence \(\Xi_{\mathfrak c}(\mathfrak d)=\Xi_{\mathfrak d}(\mathfrak c)\), which is property 2 with \(C=1\).

*Products.* Let \(\mathfrak c_1,\mathfrak c_2\) be coprime and squarefree with \(\mathrm{cl}_2(\mathfrak c_1)=\mathrm{cl}_2(\mathfrak c_2)\). Since \(\Xi\) is real, \(\Xi_{\mathfrak c_1}\overline{\Xi_{\mathfrak c_2}}\) has local components \(y\mapsto(c_1c_2,y)_{2,v}\). At \(v\in S\), \(c_1c_2=(c_1/c_2)c_2^2\) is a square in \(F_v\), so the component is trivial. At a prime of \(\mathfrak c_1\mathfrak c_2\) the valuation of \(c_1c_2\) is \(1\), and the argument above gives exponent \(1\); elsewhere it is unramified. So the conductor is exactly \(\mathfrak c_1\mathfrak c_2\), which is property 3. \(\square\)

**Corollary 2.2** (quadratic large sieve for the exterior symbols). For \(C,D\ge1\), every \(\epsilon>0\), and complex \(z_{\mathfrak c}\) supported on squarefree exterior ideals with \(q_{\mathfrak c}\le C\),
\[
\begin{aligned}
&\sum_{\substack{\mathfrak d\ \text{squarefree}\\ q_{\mathfrak d}\le D}}\Bigl|\sum_{\mathfrak c}z_{\mathfrak c}\,\chi_{\mathfrak d}(c)^3\Bigr|^2\\
&\quad\le C_{F,S,\epsilon}\,(C+D)(CD)^\epsilon\\
&\qquad\times\sum_{\mathfrak c}|z_{\mathfrak c}|^2 .\quad(2.2)
\end{aligned}
\]
The same bound holds after deleting any set of rows, and after multiplying each row by a factor of absolute value at most one.

*Proof.* N3 with \(M=D\), \(N=C\), \(\lambda_{\mathfrak c}=z_{\mathfrak c}\), and (2.1). Deleting rows or multiplying them by such factors does not increase the left side. \(\square\)

A restriction on the columns, for instance to one class \([c]\in B\), or a unimodular factor depending on the column alone, is absorbed into the coefficients \(z_{\mathfrak c}\); the family itself is applied in full.

## 3. Counting lemmas

**Lemma 3.1.** There is \(C_F\) such that, for exterior ideals:

1. \(\#\{\mathfrak a:q_{\mathfrak a}\le t\}\le C_Ft\) for \(t\ge1\);
2. \(\sum_{C\le q_{\mathfrak a}<2C}q_{\mathfrak a}^{-1}\le2C_F\) for \(C\ge1\);
3. \(\sum_{q_{\mathfrak a}\le t}q_{\mathfrak a}^{-1}\le2C_F\,(1+\log_2t)\) for \(t\ge1\);
4. \(\#\{\mathfrak h\ \text{powerful}:q_{\mathfrak h}<2P\}\)\(\le C_F\,\zeta_F(3/2)\,(2P)^{1/2}\) for \(P>0\).

*Proof.* (1) Exterior ideals correspond to integral ideals of \(\mathcal O_F\) of the same norm, and (16) of Theorem 15.3 of [*Counting ideals of bounded norm*](course:NT-ANT/counting-ideals-of-bounded-norm) bounds their number. (2) The sum is at most \(C^{-1}\) times the number of ideals of norm less than \(2C\). (3) Split \([1,t]\) into the intervals \([2^k,2^{k+1})\), \(0\le k\le\log_2t\), and apply (2). (4) A powerful ideal has a unique expression \(\mathfrak h=\mathfrak r^2\mathfrak s^3\) with \(\mathfrak s\) squarefree: at a prime of exponent \(e\ge2\), take exponent \(0\) in \(\mathfrak s\) and \(e/2\) in \(\mathfrak r\) if \(e\) is even, and \(1\) in \(\mathfrak s\) and \((e-3)/2\) in \(\mathfrak r\) if \(e\) is odd. For each \(\mathfrak s\), the number of \(\mathfrak r\) with \(q_{\mathfrak r}<(2P/q_{\mathfrak s}^3)^{1/2}\) is at most \(C_F(2P)^{1/2}q_{\mathfrak s}^{-3/2}\) by (1), and it is \(0\) when the bound is below \(1\). Summing over \(\mathfrak s\) gives at most \(C_F(2P)^{1/2}\zeta_F(3/2)\). \(\square\)

**Lemma 3.2** ([OpenAI-029, (6.34)]). For every \(\delta_1>0\) there is \(C_{\delta_1}\) with
\[
\begin{aligned}
&\sum_{\mathfrak f\mid\operatorname{rad}(\mathfrak h)}\ \prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(\sigma)\\
&\quad =\prod_{\mathfrak p\mid\mathfrak h}\bigl(1+E_{\mathfrak p}(\sigma)\bigr)\le C_{\delta_1}\,q_{\mathfrak h}^{\delta_1}
\end{aligned}
\]
for all \(\sigma\ge0\) and all exterior ideals \(\mathfrak h\), with \(E_{\mathfrak p}\) as in (2.5) of Lesson 9.

*Proof.* The identity is the expansion of the product. Each factor is at most \(4+\sqrt2\) by Lemma 2.2 of Lesson 9. The primes with \(q_{\mathfrak p}<(4+\sqrt2)^{1/\delta_1}\) are finitely many and contribute at most a constant; every other factor is at most \(q_{\mathfrak p}^{\delta_1}\), and \(\prod_{\mathfrak p\mid\mathfrak h}q_{\mathfrak p}\le q_{\mathfrak h}\). \(\square\)

## 4. Proof of the reflected second moment

We prove Proposition 4.1 of Lesson 5: for a compact \(\mathscr K\subset F_S^\times\), \(\epsilon>0\), \(Z\ge2\) and \(P,D\ge1\),
\[
\begin{aligned}
&\sum_{\substack{m\in\mathscr B_Z(\mathscr K)\\ P\le q_{\mathfrak h(m)}<2P\\ D\le q_{\mathfrak d(m)}<2D}}|B_m(Z)|^2\\
&\quad \le C_{\mathscr K,\epsilon}\,Z^\epsilon P^{1/2}\Bigl(D+\frac{D^2P}Z\Bigr).\quad(4.1)
\end{aligned}
\]
The deduction of the total bound (4.4) of Lesson 5 from (4.1) is given there. All constants below may depend on \(F\), \(S\), \(\eta\), \(\mathscr K\), \(\epsilon\) and the fixed theta data.

*Step 1: from rows to ideals.* By (2.2) of Lesson 8, \(B_m(Z)\) depends on \(m\) only through \(\mathfrak m=mR\) and \(\upsilon_m\in U_6\). For an exterior ideal \(\mathfrak m=\mathfrak h\mathfrak d\), with \(\mathfrak h\) powerful and \(\mathfrak d\) squarefree and prime to \(\mathfrak h\), and for \(\upsilon\in U_6\), let \(B_{\mathfrak m,\upsilon}(Z)\) be the common value, given by the expansion (5.1) of Lesson 9. By Lemma 1.1(2) of Lesson 8, at most \(C_{\mathscr K}=|U_S\cap\mathscr K\mathscr K^{-1}|\) rows generate one ideal. Hence the left side of (4.1) is at most
\[
C_{\mathscr K}\sum_{\upsilon\in U_6}\ \sum_{\substack{\mathfrak h\ \text{powerful}\\ P\le q_{\mathfrak h}<2P}}\ \sum_{\substack{\mathfrak d\ \text{squarefree}\\ (\mathfrak d,\mathfrak h)=1\\ D\le q_{\mathfrak d}<2D}}|B_{\mathfrak h\mathfrak d,\upsilon}(Z)|^2 .
\]
If the dyads contain a row, then \(q_{\mathfrak h}q_{\mathfrak d}=|m|_S\) is at most a constant times \(Z^{M_0}\), so
\[
\begin{gathered}
P,D\ge1,\\
PD\le C_{\mathscr K}'Z^{M_0};\quad(4.2)
\end{gathered}
\]
otherwise the left side of (4.1) is \(0\). Fix \(\upsilon\).

*Step 2: retained and discarded terms.* Fix \(\delta>0\), to be chosen small, and put
\[
\begin{gathered}
Q=q_{\mathfrak a'_{\mathfrak f}}q_{\mathfrak c'}q_{\mathfrak n'}^3,\\
t_{\mathfrak d}=\frac{q_{\mathfrak d}^2q_{\mathfrak f}^2}Z,\\
\mathcal L=\frac{8D^2P}Z,\\
R_0=Z^\delta\mathcal L .
\end{gathered}
\]
The profile in (5.1) of Lesson 9 is \(\Phi_{\upsilon,\kappa}(Q/t_{\mathfrak d})\), and \(t_{\mathfrak d}<\mathcal L\) because \(q_{\mathfrak d}<2D\) and \(q_{\mathfrak f}^2\le q_{\mathfrak h}<2P\) ((2.2) of Lesson 9). Split each term of (5.1) of Lesson 9 according to \(Q\le R_0\) or \(Q>R_0\), and write \(B_{\mathfrak h\mathfrak d,\upsilon}(Z)=\operatorname{Ret}_{\mathfrak h,\mathfrak d}+\operatorname{Tail}_{\mathfrak h,\mathfrak d}\) accordingly; for fixed \(\mathfrak f\) and \(\mathbf s=(u,z_d,z_c)\in U_6\times B^2\) write \(\operatorname{Ret}_{\mathfrak f,\mathbf s,\mathfrak d}\) and \(\operatorname{Tail}_{\mathfrak f,\mathbf s,\mathfrak d}\) for the corresponding parts, which still contain the sums over \(\mathfrak a'_{\mathfrak f},\mathfrak n',\mathfrak c'\). The threshold \(R_0\) depends only on the dyads. If \(R_0<1\), every term is discarded, because \(Q\ge1\).

*Step 3: the discarded terms.* Put \(\mathcal J=\max(Z^\delta,\mathcal L^{-1})\) and fix \(N>\sigma>1/2\). If \(Q>R_0\), then \(Q/t_{\mathfrak d}>R_0/\mathcal L=Z^\delta\) and \(Q/t_{\mathfrak d}\ge1/t_{\mathfrak d}>\mathcal L^{-1}\), so \(Q/t_{\mathfrak d}\ge\mathcal J\ge1\). By Lemma 3.1 of Lesson 9, \(|\Phi_{\upsilon,\kappa}(x)|\le C_Nx^{-N}\le C_N\mathcal J^{-(N-\sigma)}x^{-\sigma}\) for \(x\ge\mathcal J\). With (4.5), (5.7) of Lesson 9 and \(t_{\mathfrak d}<\mathcal L\),
\[
\begin{aligned}
&|\operatorname{Tail}_{\mathfrak f,\mathbf s,\mathfrak d}|\\
&\quad \le C_N\mathcal J^{-(N-\sigma)}t_{\mathfrak d}^\sigma\mathcal D_{\mathfrak f}(\sigma)\\
&\quad \le C_{N,\sigma}\,\mathcal L^\sigma\mathcal J^{-(N-\sigma)}\prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(\sigma).\quad(4.3)
\end{aligned}
\]
Summing over \(\mathfrak f\in\mathcal F(\mathfrak h)\) with Lemma 3.2, and over the \(|U_6||B|^2\) choices of \(\mathbf s\), gives \(|\operatorname{Tail}_{\mathfrak h,\mathfrak d}|\le C\,q_{\mathfrak h}^{\delta_1}\mathcal L^\sigma\mathcal J^{-(N-\sigma)}\). Squaring, and summing over the at most \(2C_FD\) rows \(\mathfrak d\) and the at most \(CP^{1/2}\) powerful \(\mathfrak h\) (Lemma 3.1),
\[
\begin{aligned}
&\sum_{\mathfrak h,\mathfrak d}|\operatorname{Tail}_{\mathfrak h,\mathfrak d}|^2\\
&\quad \le C\,P^{1/2+2\delta_1}D\,\mathcal L^{2\sigma}\mathcal J^{-2(N-\sigma)} .\quad(4.4)
\end{aligned}
\]
By (4.2), \(P\le C'Z^{M_0}\) and \(\mathcal L\le8(PD)^2/Z\le CZ^{2M_0-1}\), while \(\mathcal J\ge Z^\delta\). Given \(A_0>0\), choose \(N\) with
\[
\begin{aligned}
2\delta(N-\sigma)&>A_0+2M_0\delta_1\\
&\quad+2\sigma(2M_0-1);
\end{aligned}
\]
then (4.4) is at most \(CZ^{-A_0}P^{1/2}D\). This covers every dyad, including those with \(R_0<1\).

*Step 4: the retained terms.* Let \(R_0\ge1\). Fix \(\mathfrak f\), \(\mathbf s\), \(\mathfrak a'_{\mathfrak f}\) and \(\mathfrak n'\); then \(\kappa=\kappa_6(\mathfrak t;z_d,z_c)\) is fixed, and \(\rho=\rho_{\upsilon,\mathfrak t,z_d}\), \(\lambda=\lambda_{\upsilon,\mathfrak t,z_c}\) are functions of the row and of the column alone. Split the columns into dyads \(C\le q_{\mathfrak c'}<2C\) with \(C\ge1\) a power of \(2\), and put
\[
\begin{gathered}
v_0=\frac{Zq_{\mathfrak a'_{\mathfrak f}}q_{\mathfrak n'}^3C}{D^2q_{\mathfrak f}^2},\\
\begin{aligned}
x&=\log\frac{q_{\mathfrak c'}}C-2\log\frac{q_{\mathfrak d}}D\\
&\in[-2\log2,\log2].
\end{aligned}
\end{gathered}
\]
Then \(Q/t_{\mathfrak d}=v_0e^x\). Fix \(\phi\in C_c^\infty(\mathbb R)\) equal to \(1\) on \([-2\log2,\log2]\) and put \(g(x)=\phi(x)\Phi_{\upsilon,\kappa}(v_0e^x)\). By Corollary 5.2 of Lesson 7, applied to the profiles of (3.1) of Lesson 9,
\[
\begin{aligned}
&\int_{\mathbb R}|\widehat g(\tau)|\,d\tau\\
&\quad \le C_N\min(v_0^\alpha,v_0^{-N})\le C .\quad(4.5)
\end{aligned}
\]
Fourier inversion for the smooth compactly supported \(g\) (Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017)) gives \(\Phi_{\upsilon,\kappa}(Q/t_{\mathfrak d})=\frac1{2\pi}\int\widehat g(\tau)\)\(\,(q_{\mathfrak c'}/C)^{i\tau}(q_{\mathfrak d}/D)^{-2i\tau}\,d\tau\), which separates the row and column norms. For each \(\tau\) put
\[
\begin{aligned}
z_{\mathfrak c'}(\tau)&=\lambda(\mathfrak c')\,q_{\mathfrak c'}^{-1/2}(q_{\mathfrak c'}/C)^{i\tau}\\
&\quad \,\mathbf 1_{C\le q_{\mathfrak c'}<2C}\,\mathbf 1_{Q\le R_0},
\end{aligned}
\]
a column coefficient once \(\mathfrak a'_{\mathfrak f}\) and \(\mathfrak n'\) are fixed, with \(\sum|z_{\mathfrak c'}(\tau)|^2\le\sum_{C\le q<2C}q^{-1}\le2C_F\) by (4.5) of Lesson 9 and Lemma 3.1. The row factors \(\rho(\mathfrak d)(q_{\mathfrak d}/D)^{-2i\tau}\) have absolute value at most one, and the restrictions \((\mathfrak d,\mathfrak h\mathfrak n')=1\) and \([d]=z_d\) delete rows. By Minkowski's inequality for the \(\tau\)-integral and Corollary 2.2, the \(\ell^2\) norm over \(\mathfrak d\) of the contribution of one column dyad is at most
\[
\begin{gathered}
C_{\delta_2}\,(D+C)^{1/2}(DC)^{\delta_2/2}\\
(\delta_2>0).\quad(4.6)
\end{gathered}
\]
Shared primes of \(\mathfrak d\) and \(\mathfrak c'\) are already handled by the zero of \(\chi_{\mathfrak d}(c')^3\), so no condition coupling rows and columns has been dropped.

In the retained range \(C\le q_{\mathfrak c'}\le R_0\) and \(q_{\mathfrak n'}\le R_0^{1/3}\). There are at most \(1+\log_2R_0\) column dyads, and \(\sum_{q_{\mathfrak n'}\le R_0^{1/3}}q_{\mathfrak n'}^{-1}\le C\log(2R_0)\) by Lemma 3.1. By (4.5) of Lesson 9, \(|\omega_{\upsilon,\mathfrak t}|\le\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f})\), and \(\sum_{\mathfrak a'_{\mathfrak f}\in\mathcal A(\mathfrak f)}\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f})=\prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(0)\). Minkowski's inequality over the column dyads, \(\mathfrak n'\) and \(\mathfrak a'_{\mathfrak f}\) bounds the \(\ell^2\) norm over \(\mathfrak d\) of \(\operatorname{Ret}_{\mathfrak f,\mathbf s,\mathfrak d}\) by
\[
\begin{aligned}
&C_{\delta_2}\prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(0)\,\log^2(2R_0)\\
&\quad \,(D+R_0)^{1/2}(DR_0)^{\delta_2/2}.
\end{aligned}
\]
Summing over \(\mathfrak f\) with Lemma 3.2 at \(\sigma=0\), and over \(\mathbf s\), bounds the \(\ell^2\) norm of \(\operatorname{Ret}_{\mathfrak h,\cdot}\) by \(C\,q_{\mathfrak h}^{\delta_1}\log^2(2R_0)(D+R_0)^{1/2}(DR_0)^{\delta_2/2}\). Square this for each \(\mathfrak h\) and sum over the at most \(CP^{1/2}\) powerful \(\mathfrak h\); every row has one powerful part, so no inequality across different \(\mathfrak h\) is needed:
\[
\begin{aligned}
&\sum_{\mathfrak h,\mathfrak d}|\operatorname{Ret}_{\mathfrak h,\mathfrak d}|^2\\
&\quad\le C\,P^{1/2+2\delta_1}\log^4(2R_0)\\
&\qquad\times(D+R_0)(DR_0)^{\delta_2}.\quad(4.7)
\end{aligned}
\]

*Step 5: the exponents.* By (4.2), \(D+R_0\le8Z^\delta(D+D^2P/Z)\), \(DR_0=8Z^\delta D^3P/Z\le CZ^{3M_0-1+\delta}\), and \(1\le R_0\le CZ^{2M_0-1+\delta}\), so \(\log^4(2R_0)\le C_{\delta_3}Z^{\delta_3}\) for every \(\delta_3>0\). Choose \(\delta,\delta_1,\delta_2,\delta_3>0\) with
\[
\delta+2M_0\delta_1+(3M_0-1+\delta)\delta_2+\delta_3<\epsilon .
\]
Then (4.7) is at most \(CZ^\epsilon P^{1/2}(D+D^2P/Z)\), and (4.4), with \(A_0=1\), is smaller. Since \(|B|^2\le2|\operatorname{Ret}|^2+2|\operatorname{Tail}|^2\), summing over the finitely many \(\upsilon\) and restoring the factor \(C_{\mathscr K}\) proves (4.1).

*Uniformity.* Replacing \(\mathscr K\) by \(c\mathscr K\) with \(c\in F_S^1\) changes neither \(\mathscr K\mathscr K^{-1}\) nor the norms \(|y|_S\) of its elements; so \(C_{\mathscr K}\) and the constant in (4.2) are unchanged, and the bound is uniform in \(c\). \(\square\)

## 5. Exercises

**5.1.** Show that the decomposition \(\mathfrak h=\mathfrak r^2\mathfrak s^3\) with \(\mathfrak s\) squarefree exists exactly for powerful \(\mathfrak h\), and that it is unique.

**5.2.** Let \(p\equiv1\pmod{12}\) be a rational prime and \(\chi\) a character of order \(6\) of \(\mathbb F_p^\times\). Show that \(\chi^3\) is the Legendre symbol modulo \(p\). Explain how this is the special case of (2.1) at a prime of degree one.

**5.3.** Let \(v\in S\) be a finite place not above \(2\), and let \(a\in F_v^\times\) be a unit that is not a square. Show that \(y\mapsto(a,y)_{2,v}\) is a nontrivial unramified character of \(F_v^\times\). Conclude that, at such a place, a difference between the local classes of \(c_1\) and \(c_2\) need not enlarge the conductor of \(\Xi_{\mathfrak c_1}\overline{\Xi_{\mathfrak c_2}}\), while equal classes always give a trivial local component there.

**5.4.** In Step 3, verify the inequality \(x^{-N}\le\mathcal J^{-(N-\sigma)}x^{-\sigma}\) for \(x\ge\mathcal J\ge1\), and explain why the tail bound needs no separate treatment of the dyads with \(R_0<1\).

**5.5.** Show that \(D^3P\le(PD)^3\) for \(P\ge1\), and deduce \(DR_0\le CZ^{3M_0-1+\delta}\) from (4.2).

## 6. Solutions

**5.1.** If \(\mathfrak h=\mathfrak r^2\mathfrak s^3\), every exponent is \(2r+3s\) with \(r\ge0\), \(s\in\{0,1\}\), which is \(0\) or at least \(2\); so \(\mathfrak h\) is powerful. Conversely the proof of Lemma 3.1(4) constructs the decomposition. It is unique because \(s\equiv e\pmod2\) determines \(s\in\{0,1\}\) and then \(r=(e-3s)/2\).

**5.2.** \(\chi^3\) is a character of order \(2\) of the cyclic group \(\mathbb F_p^\times\), and there is only one such character, the Legendre symbol. At a prime \(\mathfrak d\) of degree one, \(k_{\mathfrak d}=\mathbb F_p\), \(\chi_{\mathfrak d}(c)\equiv c^{(p-1)/6}\), and \(\chi_{\mathfrak d}(c)^3\equiv c^{(p-1)/2}\) is the quadratic residue symbol of \(c\), the value of the character of \(F(\sqrt c)/F\) at \(\mathfrak d\).

**5.3.** For a unit \(u\), \((a,u)_{2,v}=1\), the symbol of two units at a place not above \(2\) (Section 3 of Lesson 2); so the character is unramified. For a uniformizer \(\varpi\), (3.2) of Lesson 2 gives \((a,\varpi)_{2,v}\equiv a^{(q_v-1)/2}\pmod v\). A unit is a square exactly when its residue is a square (Hensel's lemma, as \(v\nmid2\)); so the residue of \(a\) is not a square, and Euler's criterion gives \(a^{(q_v-1)/2}\equiv-1\). Hence the character is nontrivial. If the local classes of \(c_1\) and \(c_2\) differ by such a unit, the component \((c_1c_2,\cdot)_{2,v}\) is nontrivial but unramified, and contributes nothing to the conductor. If the classes agree, \(c_1c_2\) is a square at \(v\) and the component is trivial, as in the proof of Lemma 2.1.

**5.4.** For \(x\ge\mathcal J\), \(x^{-(N-\sigma)}\le\mathcal J^{-(N-\sigma)}\) since \(N>\sigma\). If \(R_0<1\), every term is in the tail, and the bound (4.4) holds for the whole sum because \(\mathcal J=\max(Z^\delta,\mathcal L^{-1})\) was chosen so that \(Q/t_{\mathfrak d}\ge\mathcal J\) for every \(Q\ge1\).

**5.5.** \(D^3P=(PD)^3/P^2\le(PD)^3\). Then \(DR_0=8Z^\delta D^3P/Z\)\(\le8Z^{\delta-1}(PD)^3\le CZ^{3M_0-1+\delta}\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 6.3. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [GL] L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212; arXiv:1112.1642v2, Definition 1 and Theorem 1.1. https://arxiv.org/abs/1112.1642
- [HB] D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), 235–275. https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums
