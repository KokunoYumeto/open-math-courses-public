# The Weyl reflection

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[*A theta expression for the coefficient sums*](a-theta-expression-for-the-coefficient-sums.md) wrote \(B_m(Z)\) as a Gaussian average of the theta average \(\mathcal T_m(l)\), and noted that \(\mathcal T_m(l)\) can be computed after applying the rational Weyl element \(w\). This lesson carries out that computation. At \(S\), \(w\) inverts the norm variable; a frequency of norm \(Q/(q_{\mathfrak d}^2q_{\mathfrak f}^2)\) then contributes at the reflected norm \(ZQ/(q_{\mathfrak d}^2q_{\mathfrak f}^2)\). At a row prime, \(w\) turns each Fourier mask into a short Gauss sum. At a prime dividing \(m\) exactly once the result is a first power of the sextic symbol, while a squarefree column prime contributes the power \(-4\) of the same pairing. By reciprocity the product of the two is the cube of the sextic symbol, a quadratic symbol, and the resulting bilinear form in row and column ideals is the object of the quadratic large sieve in Lesson 10.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Lemma 2.1, Section 3 and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Section 1 and Proposition 2.1; [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), Lemma 1.1; [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Section 4; [*Cubic theta and its Whittaker coefficients*](cubic-theta-and-its-whittaker-coefficients.md), N1, (1.2), (1.3), (2.1), (2.3), Proposition 4.1 and Lemma 6.1; [*Norm sheets and exact Gaussian smoothing*](norm-sheets-and-exact-gaussian-smoothing.md), Lemmas 2.1, 3.1, 5.1 and 6.1; [*A theta expression for the coefficient sums*](a-theta-expression-for-the-coefficient-sums.md), Sections 1–6.

## 1. The local effect of the Weyl element

Fix an exterior prime \(\mathfrak p\) with allowed generator \(p\), used as uniformizer, and write \(\chi=\chi_{\mathfrak p}\), \(\psi=\psi_{\mathfrak p}\), \(q=q_{\mathfrak p}\) and \(W_e=W_{\mathfrak p}(a(p^e))\), so that \(|W_e|\) is \(q^{-k}\), \(q^{-k-1/2}\) or \(0\) for \(e=3k\), \(3k+1\), \(3k+2\) with \(k\ge0\) (Proposition 4.1 of Lesson 6). Let \(\alpha_{\mathfrak p,j}\) and \(\tau_{\mathfrak p,j}\) be the masks and Gauss sums of Section 3 of Lesson 8. From (1.3) of Lesson 6 and bimultiplicativity, for integers \(e_1,e_2\) and units \(u,v\),
\[
\begin{aligned}
&\mathcal C_{\mathfrak p}\bigl(p^{e_1}u,\,p^{e_2}v\bigr)\\
&\quad =\chi(u)^{2e_2}\chi(v)^{-2e_1}.\quad(1.1)
\end{aligned}
\]

For \(0\le j\le5\), an integer \(e\) and a unit \(t\), put
\[
\begin{aligned}
\mathcal R_{\mathfrak p,j,e}(t)&=\sum_{x\in k_{\mathfrak p}^\times}\alpha_{\mathfrak p,j}(x)\\
&\quad \,W_{\mathfrak p}\bigl(a(p^{e-2}t)\,w\,n(x/p)\bigr),
\end{aligned}
\]
the contribution of the nonzero digits to the reflected Whittaker value at a frequency of valuation \(e-2\).

**Lemma 1.1** (local reflection [OpenAI-029, Lemma 6.2]). \(\mathcal R_{\mathfrak p,j,e}=0\) for \(e<0\). For \(e\ge0\),
\[
\begin{aligned}
\mathcal R_{\mathfrak p,j,e}(t)&=W_e\,\chi(t)^{4+2e}\\
&\quad \sum_{x\in k_{\mathfrak p}^\times}\alpha_{\mathfrak p,j}(x)\\
&\quad \,\chi(x)^4\,\psi\bigl(p^{e-1}t/x\bigr).\quad(1.2)
\end{aligned}
\]
Put \(s_{\mathfrak p,j,e}=\mathcal R_{\mathfrak p,j,e}(1)\), and choose exponents modulo \(6\) by \(b_{j,0}\equiv8-j\) and \(b_{j,e}\equiv4+2e\) for \(e>0\). Then
\[
\mathcal R_{\mathfrak p,j,e}(t)=s_{\mathfrak p,j,e}\,\chi(t)^{b_{j,e}} .
\tag{1.3}
\]
Moreover:

1. \(|s_{\mathfrak p,j,0}|\le1\), and for \(e>0\), \(|s_{\mathfrak p,j,e}|\le q^{1/2}|W_e|\); for \(e>0\), \(s_{\mathfrak p,j,e}=0\) unless \(j=4\), and \(s_{\mathfrak p,j,e}=0\) when \(e\equiv2\pmod3\).
2. For \(j=1\): \(\mathcal R_{\mathfrak p,1,e}=0\) for \(e\ne0\), and
\[
\begin{gathered}
\mathcal R_{\mathfrak p,1,0}(t)=\xi_{\mathfrak p}\,\chi(t),\\
\xi_{\mathfrak p}=\frac1{\tau_{\mathfrak p,1}}\sum_{x\in k_{\mathfrak p}^\times}\chi(x)^3\psi(x/p),\\
|\xi_{\mathfrak p}|=1 .\quad(1.4)
\end{gathered}
\]
3. The zero digit carries weight \(\alpha_{\mathfrak p,j}(0)\), which is nonzero only for \(j=0\); at a frequency \(\nu\) its contribution is \((1-q^{-1})W_{\mathfrak p}(a(\nu))\).

*Proof.* Let \(x\in k_{\mathfrak p}^\times\), represented by a unit, and \(H=x/p\). By (2.1) of Lesson 6, \(wn(H)=n(H^{-1})a(-H^{-2})\bar n(H^{-1})\). Here \(a(-H^{-2})=a(H^{-2})a(-1)\), with trivial cocycle because \(-1\) is a sixth power, and \(k_x=a(-1)\bar n(p/x)\) lies in the split compact subgroup, so it fixes the spherical vector. Commuting \(n(p/x)\) to the left, \(a(p^{e-2}t)n(p/x)=n(p^{e-1}t/x)a(p^{e-2}t)\), and the Whittaker functional gives the factor \(\psi(p^{e-1}t/x)\). With \(H^{-2}=p^2x^{-2}\), (1.1) gives
\[
\mathcal C_{\mathfrak p}\bigl(p^{e-2}t,\,p^2x^{-2}\bigr)=\chi(t)^4\chi(x)^{4(e-2)} .
\]
The remaining argument is \(a(p^ etx^{-2})\). By Proposition 4.1 of Lesson 6 its value is \(0\) for \(e<0\) and \(\chi(t)^{2e}\chi(x)^{-4e}W_e\) for \(e\ge0\). The product of the three factors is \(W_e\chi(t)^{4+2e}\chi(x)^{-8}\psi(p^{e-1}t/x)\), and \(\chi^{-8}=\chi^4\); this is (1.2).

For \(e>0\) the additive factor is \(1\), and the digit sum is \(\sum_x\alpha_{\mathfrak p,j}(x)\chi(x)^4\). For \(j\ne0\) it is \(\tau_{\mathfrak p,j}^{-1}\sum_x\chi(x)^{4-j}\), which vanishes unless \(j=4\); for \(j=0\) it is \(-q^{-1}\sum_x\chi(x)^4=0\). In every case its absolute value is at most \(\sum_x|\alpha_{\mathfrak p,j}(x)|\le q^{1/2}\) (Lemma 3.1 of Lesson 8). The dependence on \(t\) is \(\chi(t)^{4+2e}\), and \(W_e=0\) for \(e\equiv2\pmod3\).

For \(e=0\) substitute \(x=t/y\), so that \(\chi(x)^4=\chi(t)^4\chi(y)^{-4}\) and \(\psi(t/(px))=\psi(y/p)\). For \(j\ne0\), \(\alpha_{\mathfrak p,j}(x)=\tau_{\mathfrak p,j}^{-1}\chi(t)^{-j}\chi(y)^j\), and
\[
\begin{aligned}
\mathcal R_{\mathfrak p,j,0}(t)&=\chi(t)^{8-j}\,\frac{1}{\tau_{\mathfrak p,j}}\\
&\quad \sum_{y\in k_{\mathfrak p}^\times}\chi(y)^{j-4}\psi(y/p).
\end{aligned}
\]
The last sum is a Gauss sum of absolute value \(q^{1/2}\) if \(j\ne4\) (Lemma 1.1 of Lesson 4) and equals \(-1\) if \(j=4\); with \(|\tau_{\mathfrak p,j}|=q^{1/2}\) the absolute value is at most \(1\). For \(j=1\), \(\chi^{j-4}=\chi^{-3}=\chi^3\) and \(8-j=7\equiv1\pmod 6\), which is (1.4). For \(j=0\), \(\alpha_{\mathfrak p,0}(x)=-q^{-1}\) and the same substitution gives \(-q^{-1}\chi(t)^8\sum_y\chi(y)^{-4}\psi(y/p)\), of absolute value \(q^{-1/2}\). This proves (1.3) and part 1. Part 2 is the case \(j=1\): for \(e>0\) it vanishes because \(j\ne4\). For part 3, \(w\) lies in the split compact subgroup, so \(W_{\mathfrak p}(a(\nu)w)=W_{\mathfrak p}(a(\nu))\). \(\square\)

## 2. Active primes and the reflected frequencies

Let \(m\in R\) be nonzero and factor its exterior ideal as \(\mathfrak m=\mathfrak h\mathfrak d\), with \(\mathfrak h\) powerful and \(\mathfrak d\) squarefree and prime to \(\mathfrak h\) ((4.2) of Lesson 5). Every prime of \(\mathfrak d\) has \(j_{\mathfrak p}=1\). In the digit sum at a prime \(\mathfrak p\mid\mathfrak m\), call \(\mathfrak p\) **active** for a digit vector if its digit is nonzero. Since \(\alpha_{\mathfrak p,j}(0)=0\) for \(j\ne0\), every prime with \(j_{\mathfrak p}\ne0\) is active, in particular every prime of \(\mathfrak d\). The possible sets of active primes of \(\mathfrak h\) are the squarefree ideals in
\[
\begin{aligned}
&\mathcal F(\mathfrak h)=\bigl\{\mathfrak f\ \text{squarefree}:\ \mathfrak f\mid\operatorname{rad}(\mathfrak h),\\
&\qquad\mathfrak p\mid\mathfrak f\ \text{whenever}\ \mathfrak p\mid\mathfrak h\\
&\qquad\text{and}\ j_{\mathfrak p}\ne0\bigr\},\quad(2.1)
\end{aligned}
\]
and the inactive primes of \(\mathfrak h\) carry the scalar
\[
I_{\mathfrak h,\mathfrak f}=\prod_{\mathfrak p\mid\mathfrak h,\ \mathfrak p\nmid\mathfrak f}\bigl(1-q_{\mathfrak p}^{-1}\bigr).
\]
Since every exponent of \(\mathfrak h\) is at least \(2\),
\[
q_{\mathfrak f}^2\le q_{\mathfrak h}\qquad(\mathfrak f\in\mathcal F(\mathfrak h)).
\tag{2.2}
\]
For squarefree \(\mathfrak f\) let \(\mathcal A(\mathfrak f)\) be the set of integral exterior ideals supported on the primes of \(\mathfrak f\) all of whose exponents are congruent to \(0\) or \(1\) modulo \(3\); in particular \(\mathcal A(R)=\{R\}\).

**Lemma 2.1** (reflected frequencies [OpenAI-029, (6.14)]). Fix \(\mathfrak f\in\mathcal F(\mathfrak h)\), and choose representatives \(\varepsilon_u\in U_S\) of the classes \(u\in U_6\). In the Fourier expansion of \(\theta_\upsilon(wg(y,\mathbf x))\), summed over the digit vectors with active set \(\mathfrak d\mathfrak f\), every frequency \(\nu\in F^\times\) with a nonzero exterior coefficient is of the form
\[
\begin{gathered}
\nu=\gamma\nu_0,\\
\nu_0=\varepsilon_u\,\frac{a'_{\mathfrak f}\,c'\,(n')^3}{(df)^2},\\
\gamma\in\Gamma ,\quad(2.3)
\end{gathered}
\]
where \(\mathfrak a'_{\mathfrak f}\in\mathcal A(\mathfrak f)\), \(\mathfrak c'\) is squarefree, \(\mathfrak n'\) is integral, \((\mathfrak c'\mathfrak n',\mathfrak d\mathfrak f)=1\), and \(d,f,a'_{\mathfrak f},c',n'\) are the fixed allowed generators of \(\mathfrak d,\mathfrak f,\mathfrak a'_{\mathfrak f},\mathfrak c',\mathfrak n'\). The data \((\mathfrak a'_{\mathfrak f},\mathfrak c',\mathfrak n',u,\gamma)\) are uniquely determined by \(\nu\).

*Proof.* At an exterior prime \(\mathfrak q\nmid\mathfrak d\mathfrak f\), the local factor is a spherical value, either because \(\mathfrak q\nmid\mathfrak m\) and \(w\) is compact, or by Lemma 1.1(3) at an inactive prime; it vanishes unless \(v_{\mathfrak q}(\nu)\ge0\) and \(v_{\mathfrak q}(\nu)\not\equiv2\pmod3\). At \(\mathfrak p\mid\mathfrak d\), Lemma 1.1(2) forces \(v_{\mathfrak p}(\nu)=-2\). At \(\mathfrak p\mid\mathfrak f\), Lemma 1.1 forces \(e_{\mathfrak p}=v_{\mathfrak p}(\nu)+2\ge0\) with \(e_{\mathfrak p}\not\equiv2\pmod3\). So the ideal of \(\nu\) is \(\mathfrak a'_{\mathfrak f}\mathfrak c'(\mathfrak n')^3(\mathfrak d\mathfrak f)^{-2}\), where \(\mathfrak a'_{\mathfrak f}=\prod_{\mathfrak p\mid\mathfrak f}\mathfrak p^{e_{\mathfrak p}}\) and \(\mathfrak c'(\mathfrak n')^3\) is the part of the ideal prime to \(\mathfrak d\mathfrak f\), with \(\mathfrak c'\) and \(\mathfrak n'\) determined by the valuations \(3k\) and \(3k+1\). Then \(\nu/(a'_{\mathfrak f}c'(n')^3(df)^{-2})\in U_S\), and it is \(\varepsilon_u\gamma\) for exactly one class \(u\) and one \(\gamma\in\Gamma\). \(\square\)

For the absolute estimates define, for \(e\ge0\),
\[
\begin{gathered}
\begin{aligned}
\beta_{\mathfrak p}(e)&=\begin{cases}1,&e=0,\\ q_{\mathfrak p}^{-k},&e=1+3k,\ k\ge0,\\ q_{\mathfrak p}^{1/2-k},&e=3k,\ k\ge1,\\ 0,&\text{otherwise},\end{cases}
\end{aligned}\\
\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f})=\prod_{\mathfrak p\mid\mathfrak f}\beta_{\mathfrak p}\bigl(v_{\mathfrak p}(\mathfrak a'_{\mathfrak f})\bigr).\quad(2.4)
\end{gathered}
\]

**Lemma 2.2** ([OpenAI-029, (6.15), (6.27)]). \(|s_{\mathfrak p,j,e}|\le\beta_{\mathfrak p}(e)\) for all \(j\) and \(e\ge0\). For \(\sigma\ge0\),
\[
\begin{aligned}
E_{\mathfrak p}(\sigma)&:=\sum_{e\ge0}\beta_{\mathfrak p}(e)\,q_{\mathfrak p}^{-\sigma e}\\
&=1+\frac{q_{\mathfrak p}^{-\sigma}+q_{\mathfrak p}^{-1/2-3\sigma}}{1-q_{\mathfrak p}^{-1-3\sigma}}\\
&\le3+\sqrt2 ,\quad(2.5)
\end{aligned}
\]
and for every \(\delta_1>0\), \(\prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(\sigma)\le C_{\delta_1}q_{\mathfrak f}^{\delta_1}\) uniformly in \(\sigma\ge0\) and squarefree \(\mathfrak f\).

*Proof.* The first bound is Lemma 1.1(1) with the values of \(|W_e|\): \(q^{1/2}q^{-k-1/2}=q^{-k}\) for \(e=3k+1\) and \(q^{1/2}q^{-k}\) for \(e=3k\ge3\). The series (2.5) is \(1+\sum_{k\ge0}q^{-k-\sigma(1+3k)}+\sum_{k\ge1}q^{1/2-k-3\sigma k}\), two geometric series. For \(\sigma\ge0\) and \(q\ge2\) its value is at most \(1+(1+2^{-1/2})/(1-\frac12)=3+\sqrt2\). For the product, the primes with \(q_{\mathfrak p}<(3+\sqrt2)^{1/\delta_1}\) are finitely many and contribute a constant; every other factor is at most \(3+\sqrt2\le q_{\mathfrak p}^{\delta_1}\). \(\square\)

## 3. The reflected profiles

The vector \(\varphi_\upsilon\) of Lesson 8, Section 4, translated by \(w\) at \(S\), has an \(S\)-Whittaker function
\[
\mathcal W^w_\upsilon(v)=\mathcal W_{S,\upsilon}\bigl(a(v)w\bigr)\qquad(v\in F_S^\times).
\]
It is a finite sum of products of local Whittaker functions of the components of \(\varphi_\upsilon\) translated by the local Weyl elements: at a complex place, of the rotation by \(w\) of the derivative vector of Lemma 2.1 of Lesson 7; at the finite places of \(S\), of smooth vectors, through the factorization in the proof of Lemma 3.1 of Lesson 6. Fix such a presentation
\[
\mathcal W^w_\upsilon(v)=\sum_{\ell=1}^{J_\upsilon}\prod_{a\in S}h_{\upsilon,\ell,a}(v_a).
\]
By Lemmas 2.1 and 3.1 of Lesson 7, the local factors satisfy the hypotheses of Lemma 5.1 there with any \(\delta<1/3\). Write \(H_S\) also for the pairing on \(\mathcal V\), and for \(\kappa\in\mathcal V\) and \(x>0\) define
\[
\begin{aligned}
H_{\upsilon,\kappa,\ell}(x)&=\int_{X_x}\mathbf 1_B\bigl(\kappa[v]^{-1}\bigr)\\
&\quad \,H_S(\kappa,[v])^2\,L_\upsilon(v)\\
&\quad \prod_{a\in S}h_{\upsilon,\ell,a}(v_a)\,d_x^\times v ,
\end{aligned}
\]
\[
\begin{aligned}
\Phi_{\upsilon,\kappa}(x)&=\sum_{\ell=1}^{J_\upsilon}\int_0^\infty\mathcal K(T)\\
&\quad \,H_{\upsilon,\kappa,\ell}(x/T)\,\frac{dT}T .\quad(3.1)
\end{aligned}
\]

**Lemma 3.1** (reflected profiles [OpenAI-029, (6.16)]). There is \(\alpha>0\) such that for every \(N>0\) and integer \(j\ge0\),
\[
\begin{gathered}
\begin{aligned}
&\bigl|(x\partial_x)^j\Phi_{\upsilon,\kappa}(x)\bigr|\\
&\quad \le C_{N,j}\min(x^\alpha,x^{-N})
\end{aligned}\\
(x>0),\quad(3.2)
\end{gathered}
\]
uniformly in \(\upsilon\in U_6\) and \(\kappa\in\mathcal V\).

*Proof.* The factor \(\mathbf 1_B(\kappa[v]^{-1})H_S(\kappa,[v])^2\) is a bounded function of the class \([v]\in\mathcal V\), and \(L_\upsilon\) is a smooth unitary character. Lemma 5.1 of Lesson 7, applied to the finite family of all \((\upsilon,\kappa,\ell)\), with the kernel \(\mathcal K\) of Lemma 6.1 there, gives (3.2) for each term; the family is finite. \(\square\)

## 4. Frozen, row and column factors

The coefficient of a reflected frequency will be split into a factor that depends on neither the row ideal \(\mathfrak d\) nor the column ideal \(\mathfrak c'\), a factor depending on \(\mathfrak d\) alone, a factor depending on \(\mathfrak c'\) alone, and one joint symbol. Fix \(\upsilon\) and a **frozen tuple**
\[
\begin{gathered}
\mathfrak t=(\mathfrak h,\mathfrak f,\mathfrak a'_{\mathfrak f},\mathfrak n',u),\\
\mathfrak f\in\mathcal F(\mathfrak h),\\
\mathfrak a'_{\mathfrak f}\in\mathcal A(\mathfrak f),\\
(\mathfrak n',\mathfrak f)=1,\\
u\in U_6 ,
\end{gathered}
\]
together with two **class slices** \(z_d,z_c\in B\). Put \(L=L_\upsilon\), \(\varepsilon=\varepsilon_u\), and
\[
\begin{aligned}
\kappa_6(\mathfrak t;z_d,z_c)&=[\varepsilon]\,[a'_{\mathfrak f}]\,z_c\,[n']^3\,z_d^{-2}\,[f]^{-2}\\
&\in\mathcal V .\quad(4.1)
\end{aligned}
\]
For \(\mathfrak p\mid\mathfrak f\) abbreviate \(e_{\mathfrak p}=v_{\mathfrak p}(\mathfrak a'_{\mathfrak f})\), \(s_{\mathfrak p}=s_{\mathfrak p,j_{\mathfrak p},e_{\mathfrak p}}\) and \(b_{\mathfrak p}=b_{j_{\mathfrak p},e_{\mathfrak p}}\). Define the **frozen factor**
\[
\begin{aligned}
\omega_{\upsilon,\mathfrak t}&=I_{\mathfrak h,\mathfrak f}\,L(a'_{\mathfrak f})^{-1}L(n')^{-3}\\
&\quad L(f)^2\prod_{\mathfrak p\mid\mathfrak f}s_{\mathfrak p}\\
&\quad \,\chi_{\mathfrak p}\Bigl(\varepsilon\,\frac{a'_{\mathfrak f}}{p^{e_{\mathfrak p}}}\,(n')^3\Bigl(\frac fp\Bigr)^{-2}\Bigr)^{b_{\mathfrak p}} .\quad(4.2)
\end{aligned}
\]
For a squarefree \(\mathfrak d\) with \((\mathfrak d,\mathfrak h\mathfrak n')=1\) and \([d]=z_d\) define the **row factor**
\[
\begin{aligned}
\rho_{\upsilon,\mathfrak t,z_d}(\mathfrak d)&=L(d)^2\prod_{\mathfrak p\mid\mathfrak d}\xi_{\mathfrak p}\\
&\quad \,\chi_{\mathfrak p}\Bigl(\varepsilon\,a'_{\mathfrak f}\,(n')^3\Bigl(\frac dp\Bigr)^{-2}f^{-2}\Bigr)\\
&\quad \prod_{\mathfrak p\mid\mathfrak f}\chi_{\mathfrak p}(d)^{-2b_{\mathfrak p}},\quad(4.3)
\end{aligned}
\]
and \(\rho_{\upsilon,\mathfrak t,z_d}(\mathfrak d)=0\) for other \(\mathfrak d\). For a squarefree \(\mathfrak c'\) with \((\mathfrak c',\mathfrak f)=1\) and \([c']=z_c\) define the **column factor**
\[
\begin{aligned}
\lambda_{\upsilon,\mathfrak t,z_c}(\mathfrak c')&=L(c')^{-1}\\
&\quad \prod_{\mathfrak p\mid\mathfrak f}\chi_{\mathfrak p}(c')^{b_{\mathfrak p}}\\
&\quad \prod_{\mathfrak q\mid\mathfrak c'}g_{2,\mathfrak q}\\
&\quad \,\chi_{\mathfrak q}\Bigl(\varepsilon\,a'_{\mathfrak f}\,\frac{c'}q\,f^{-2}\Bigr)^2 ,\quad(4.4)
\end{aligned}
\]
and \(\lambda_{\upsilon,\mathfrak t,z_c}(\mathfrak c')=0\) for other \(\mathfrak c'\). Here \(g_{2,\mathfrak q}\) is the normalized Gauss sum of Lesson 6, Section 4, with \(|g_{2,\mathfrak q}|=1\). On the stated supports every argument of a character is a unit at its prime, so negative powers are defined. None of the three factors depends on \(Z\); \(\omega\) does not depend on \(\mathfrak d\) or \(\mathfrak c'\), \(\rho\) depends on \(\mathfrak d\) alone and \(\lambda\) on \(\mathfrak c'\) alone. They satisfy
\[
\begin{gathered}
|\omega_{\upsilon,\mathfrak t}|\le\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f}),\\
|\rho_{\upsilon,\mathfrak t,z_d}|\le1,\\
|\lambda_{\upsilon,\mathfrak t,z_c}|\le1,\quad(4.5)
\end{gathered}
\]
by Lemmas 1.1 and 2.2, because characters and \(L\) have absolute value at most one and \(|\xi_{\mathfrak p}|=|g_{2,\mathfrak q}|=1\).

## 5. The reflected expansion

**Lemma 5.1** (the reflected expansion [OpenAI-029, Lemma 6.3]). Let \(m\in R\) be nonzero with \((m)_S=\mathfrak h\mathfrak d\), let \(\upsilon=\upsilon_m\), and let \(Z>0\). Then
\[
\begin{aligned}
&B_m(Z)=\sum_{\mathfrak f\in\mathcal F(\mathfrak h)}\ \sum_{\substack{\mathfrak a'_{\mathfrak f}\in\mathcal A(\mathfrak f),\ \mathfrak n'\\ (\mathfrak n',\mathfrak f)=1}}\ \sum_{\substack{u\in U_6\\z_d,z_c\in B}}\\
&\quad\frac{\omega_{\upsilon,\mathfrak t}}{q_{\mathfrak n'}}\,\rho_{\upsilon,\mathfrak t,z_d}(\mathfrak d)\\
&\quad\times\sum_{\mathfrak c'\ \text{squarefree}}\frac{\lambda_{\upsilon,\mathfrak t,z_c}(\mathfrak c')}{q_{\mathfrak c'}^{1/2}}\,\chi_{\mathfrak d}(c')^3\\
&\quad\Phi_{\upsilon,\kappa_6(\mathfrak t;z_d,z_c)}\Bigl(\frac{Zq_{\mathfrak a'_{\mathfrak f}}q_{\mathfrak c'}q_{\mathfrak n'}^3}{q_{\mathfrak d}^2q_{\mathfrak f}^2}\Bigr),\quad(5.1)
\end{aligned}
\]
where \(\mathfrak t=(\mathfrak h,\mathfrak f,\mathfrak a'_{\mathfrak f},\mathfrak n',u)\) and all ideal sums are over integral exterior ideals. The expansion converges absolutely.

*Proof.* Start from (6.2) of Lesson 8 and the second expression for \(\mathcal T_m(l)\) in (5.2) there. By Lemma 5.1 of Lesson 8 the constant terms integrate to \(0\), so only the nonconstant Fourier terms of \(\theta_\upsilon(wg(y,\mathbf x))\) remain. Their components are as follows. At \(S\), \(a(\nu)wa(y)=a(\nu)a(y^{-1})w\)\(=\mathcal C_S(\nu,y^{-1})\,a(\nu/y)w\) by (2.1) and (1.2) of Lesson 6, so the \(S\)-factor is \(\mathcal C_S(\nu,y^{-1})\mathcal W^w_\upsilon(\nu/y)\). At an exterior prime not dividing \(\mathfrak m\) it is \(W_{\mathfrak q}(a(\nu))\), since \(w\) is compact. At \(\mathfrak p\mid\mathfrak m\) it is \(W_{\mathfrak p}(a(\nu)wn(x_{\mathfrak p}/p))\).

*Absolute bounds before the digit sums.* Put \(F^{\mathrm{abs}}(v)=\sum_\ell\prod_{a\in S}|h_{\upsilon,\ell,a}(v_a)|\) and \(H^{\mathrm{abs}}(x)=\int_{X_x}F^{\mathrm{abs}}\,d_x^\times v\); by Lemma 5.1 of Lesson 7, \(H^{\mathrm{abs}}(x)\le C_\sigma x^{-\sigma}\) for every \(\sigma\ge0\). For \(\nu_0\in F^\times\), the sets \(\gamma\nu_0\Omega_l^{-1}\), \(\gamma\in\Gamma\), partition \(X_{|\nu_0|_S/l}\) up to null sets, and inversion and translation preserve the sheet measures; so
\[
\begin{aligned}
&\sum_{\gamma\in\Gamma}\int_{\Omega_l}F^{\mathrm{abs}}(\gamma\nu_0/y)\,d_l^\times y\\
&\quad =H^{\mathrm{abs}}\bigl(|\nu_0|_S/l\bigr)\\
&\quad \le C_\sigma\bigl(|\nu_0|_S/l\bigr)^{-\sigma}.\quad(5.2)
\end{aligned}
\]
For a fixed digit vector, the proof of Lemma 1.1 shows that a nonzero digit at \(\mathfrak p\) contributes the absolute value \(|W_e|\) at \(e=v_{\mathfrak p}(\nu)+2\ge0\), and a zero digit the spherical absolute value. For \(\sigma>1/2\), \(\sum_{e\ge0}|W_e|q_{\mathfrak p}^{-\sigma e}\)\(=(1+q_{\mathfrak p}^{-1/2-\sigma})/(1-q_{\mathfrak p}^{-1-3\sigma})\), and the shift \(e-2\) multiplies this by \(q_{\mathfrak p}^{2\sigma}\). Grouping the frequencies \(\nu\) by their ideal, their class in \(U_6\) and \(\gamma\in\Gamma\), (5.2) bounds the integrated absolute Fourier series by a constant (depending on the row) times \(l^{\sigma}\zeta_F^S(\sigma+\frac12)\zeta_F^S(3\sigma+1)\), and the \(T\)-average of (6.2) of Lesson 8 then converges absolutely because \(M_\sigma(\mathcal K)<\infty\). The digit sums are finite, with total mass bounded by Lemma 3.1 of Lesson 8. So the series may be integrated term by term and the finite digit sums evaluated first.

*Digits.* Expand the product over \(\mathfrak p\mid\mathfrak m\) of the local digit sums by the set of active primes. By Lemma 1.1 the active set is \(\mathfrak d\mathfrak f\) with \(\mathfrak f\in\mathcal F(\mathfrak h)\); each inactive prime contributes \((1-q_{\mathfrak p}^{-1})\) times a spherical value, and each active prime the value \(\mathcal R_{\mathfrak p,j_{\mathfrak p},e}(t)\) of (1.3). By Lemma 2.1, the frequencies are \(\nu=\gamma\nu_0\) as in (2.3). Every local factor is unchanged under \(\nu\mapsto\gamma\nu\), because \(\chi_{\mathfrak p}(\gamma)=1\); so the exterior coefficient may be taken outside the \(\Gamma\)-orbit.

*The exterior coefficient.* Fix the data of (2.3). At \(\mathfrak p\mid\mathfrak d\), \(\nu_0=p^{-2}t\) with the unit \(t=\varepsilon a'_{\mathfrak f}c'(n')^3(d/p)^{-2}f^{-2}\), and Lemma 1.1(2) gives \(\xi_{\mathfrak p}\chi_{\mathfrak p}(t)\). At \(\mathfrak p\mid\mathfrak f\), \(\nu_0=p^{e_{\mathfrak p}-2}t\) with \(t=\varepsilon(a'_{\mathfrak f}/p^{e_{\mathfrak p}})c'(n')^3d^{-2}(f/p)^{-2}\), and (1.3) gives \(s_{\mathfrak p}\chi_{\mathfrak p}(t)^{b_{\mathfrak p}}\). At \(\mathfrak q\mid\mathfrak c'\) with \(k=v_{\mathfrak q}(\mathfrak n')\), the valuation is \(1+3k\) and the unit is \(\varepsilon a'_{\mathfrak f}(c'/q)(n'/q^k)^3(df)^{-2}\); Proposition 4.1 of Lesson 6 gives \(q_{\mathfrak q}^{-k-1/2}g_{2,\mathfrak q}\) times the square of \(\chi_{\mathfrak q}\) of this unit, in which the cube \((n'/q^k)^3\) disappears. At a prime of \(\mathfrak n'\) not dividing \(\mathfrak c'\) the valuation is \(3k\) and the value \(q_{\mathfrak q}^{-k}\), the unit entering to a power divisible by \(6\). Every other exterior factor is \(1\). With \(I_{\mathfrak h,\mathfrak f}\) for the inactive primes, which may also divide \(\mathfrak c'\) or \(\mathfrak n'\), the exterior coefficient is, on \((\mathfrak d,\mathfrak h\mathfrak n')=(\mathfrak c',\mathfrak f)=(\mathfrak d,\mathfrak c')=1\),
\[
\begin{aligned}
&\mathcal E_{\mathfrak t}(\mathfrak d,\mathfrak c')=\frac{I_{\mathfrak h,\mathfrak f}}{q_{\mathfrak c'}^{1/2}q_{\mathfrak n'}}\\
&\quad\prod_{\mathfrak p\mid\mathfrak d}\xi_{\mathfrak p}\chi_{\mathfrak p}\Bigl(\varepsilon a'_{\mathfrak f}c'(n')^3\Bigl(\frac dp\Bigr)^{-2}f^{-2}\Bigr)\\
&\quad\times\prod_{\mathfrak p\mid\mathfrak f}s_{\mathfrak p}\chi_{\mathfrak p}\Bigl(\varepsilon\frac{a'_{\mathfrak f}}{p^{e_{\mathfrak p}}}c'(n')^3\\
&\qquad\qquad d^{-2}\Bigl(\frac fp\Bigr)^{-2}\Bigr)^{b_{\mathfrak p}}\\
&\quad\times\prod_{\mathfrak q\mid\mathfrak c'}g_{2,\mathfrak q}\chi_{\mathfrak q}\Bigl(\varepsilon a'_{\mathfrak f}\frac{c'}q(df)^{-2}\Bigr)^2 .\quad(5.3)
\end{aligned}
\]

*The quadratic pairing.* The factors involving both \(\mathfrak d\) and \(\mathfrak c'\) are \(\prod_{\mathfrak p\mid\mathfrak d}\chi_{\mathfrak p}(c')\) and \(\prod_{\mathfrak q\mid\mathfrak c'}\chi_{\mathfrak q}(d)^{-4}\). Since \(c'\) and \(d\) are products of allowed generators of their primes up to elements of \(\Gamma\), on which the symbols are \(1\), these are products over pairs \(\mathfrak p\mid\mathfrak d\), \(\mathfrak q\mid\mathfrak c'\) of \(\chi_{\mathfrak p}(q)\chi_{\mathfrak q}(p)^{-4}\). By reciprocity for allowed generators (Proposition 2.1 of Lesson 3),
\[
\begin{aligned}
&\chi_{\mathfrak p}(q)\,\chi_{\mathfrak q}(p)^{-4}=\chi_{\mathfrak p}(q)^{1-4}\\
&\quad =\chi_{\mathfrak p}(q)^3 ,\quad(5.4)
\end{aligned}
\]
and the product over the pairs is \(\chi_{\mathfrak d}(c')^3\). The \(S\)-character of \(\nu_0\) is \(L(\nu_0)^{-1}=L(a'_{\mathfrak f})^{-1}L(c')^{-1}L(n')^{-3}\)\(L(d)^2L(f)^2\), because \(L\) is trivial on \(U_S\). Splitting every other character value by multiplicativity and comparing with (4.2)–(4.4) gives, when \([d]=z_d\) and \([c']=z_c\),
\[
\begin{aligned}
&\mathcal E_{\mathfrak t}(\mathfrak d,\mathfrak c')\,L(\nu_0)^{-1}\\
&\quad =\frac{\omega_{\upsilon,\mathfrak t}\,\rho_{\upsilon,\mathfrak t,z_d}(\mathfrak d)\,\lambda_{\upsilon,\mathfrak t,z_c}(\mathfrak c')}{q_{\mathfrak c'}^{1/2}q_{\mathfrak n'}}\\
&\qquad \,\chi_{\mathfrak d}(c')^3 .\quad(5.5)
\end{aligned}
\]
The symbol \(\chi_{\mathfrak d}(c')^3\) vanishes when \(\mathfrak d\) and \(\mathfrak c'\) share a prime, the support of \(\rho\) excludes primes shared by \(\mathfrak d\) and \(\mathfrak h\mathfrak n'\), and the supports of \(\lambda\) and of the index set exclude primes shared by \(\mathfrak f\) and \(\mathfrak c'\mathfrak n'\). Together these are exactly the conditions \((\mathfrak c'\mathfrak n',\mathfrak d\mathfrak f)=1\) of Lemma 2.1.

*The S-integral.* For \(\nu=\gamma\nu_0\), substitute \(v=\gamma\nu_0/y\), which is legitimate by (5.2). Then \([y]=[\nu_0][v]^{-1}\) and \(L(y)^{-1}=L(\nu_0)^{-1}L(v)\), and by Lemma 6.1 of Lesson 6, alternation (Lemma 3.1 of Lesson 2) and \([\gamma]=1\),
\[
\begin{aligned}
&\mathcal C_S(\gamma\nu_0,y^{-1})\\
&\quad =H_S\bigl(\gamma\nu_0,v/(\gamma\nu_0)\bigr)^2\\
&\quad =H_S(\nu_0,v)^2 .
\end{aligned}
\]
Hence
\[
\begin{aligned}
&\sum_{\gamma\in\Gamma}\int_{\Omega_l}\mathbf 1_B([y])L(y)^{-1}\\
&\qquad \mathcal C_S(\gamma\nu_0,y^{-1})\mathcal W^w_\upsilon(\gamma\nu_0/y)\,d_l^\times y\\
&\quad =L(\nu_0)^{-1}\\
&\qquad \int_{X_{|\nu_0|_S/l}}\mathbf 1_B\bigl([\nu_0][v]^{-1}\bigr)\\
&\qquad H_S(\nu_0,v)^2L(v)\,\mathcal W^w_\upsilon(v)\,d^\times v .\quad(5.6)
\end{aligned}
\]
By Lemma 2.1 of Lesson 2 the sheet norm is
\[
\frac{|\nu_0|_S}l=\frac{q_{\mathfrak a'_{\mathfrak f}}q_{\mathfrak c'}q_{\mathfrak n'}^3}{q_{\mathfrak d}^2q_{\mathfrak f}^2\,l}.
\]
Inside the integral \(\nu_0\) enters only through its class, which is \(\kappa_6(\mathfrak t;z_d,z_c)\) when \([d]=z_d\) and \([c']=z_c\). Insert the partitions of \(\mathfrak d\) and \(\mathfrak c'\) by these classes, use (5.5), split \(\mathcal W^w_\upsilon\) into its \(J_\upsilon\) terms, and put \(l=T/Z\) in (6.2) of Lesson 8; the \(T\)-integral produces \(\Phi_{\upsilon,\kappa_6}\) at \(Z|\nu_0|_S\), which is (5.1).

*Absolute convergence of the grouped expansion.* Put \(Q=q_{\mathfrak a'_{\mathfrak f}}q_{\mathfrak c'}q_{\mathfrak n'}^3\) and \(t_{\mathfrak d}=q_{\mathfrak d}^2q_{\mathfrak f}^2/Z\). By (4.5), (2.5) and Lemma 2.2, dropping squarefreeness and coprimality in a nonnegative majorant, for \(\sigma>1/2\),
\[
\begin{aligned}
&\mathcal D_{\mathfrak f}(\sigma):=\sum_{\mathfrak a'_{\mathfrak f},\mathfrak c',\mathfrak n'}\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f})\,q_{\mathfrak c'}^{-1/2}q_{\mathfrak n'}^{-1}Q^{-\sigma}\\
&\quad\le\zeta_F^S(\sigma+\tfrac12)\,\zeta_F^S(3\sigma+1)\prod_{\mathfrak p\mid\mathfrak f}E_{\mathfrak p}(\sigma)\\
&\quad<\infty ,\quad(5.7)
\end{aligned}
\]
and the absolute profile dominates every class multiplier, so
\[
\begin{aligned}
&\int_0^\infty|\mathcal K(T)|\sum_{\mathfrak a'_{\mathfrak f},\mathfrak c',\mathfrak n'}\beta_{\mathfrak f}(\mathfrak a'_{\mathfrak f})\\
&\qquad \,q_{\mathfrak c'}^{-1/2}q_{\mathfrak n'}^{-1}\,H^{\mathrm{abs}}\Bigl(\frac Q{t_{\mathfrak d}T}\Bigr)\frac{dT}T\\
&\quad \le C_\sigma\,t_{\mathfrak d}^{\sigma}M_\sigma(\mathcal K)\,\mathcal D_{\mathfrak f}(\sigma).\quad(5.8)
\end{aligned}
\]
There are \(|U_6|\,|B|^2\) choices of \((u,z_d,z_c)\), and \(\mathcal F(\mathfrak h)\) is finite. This justifies every exchange and proves the absolute convergence of (5.1). \(\square\)

For \(m=0\) the identity \(B_0(Z)=P_G(1/Z)\) of Lemma 3.1 of Lesson 5 holds instead.

In (5.1) the row \(m\) enters only through \(\upsilon\), the frozen data built from \(\mathfrak h\), the row factor \(\rho(\mathfrak d)\) and the symbol \(\chi_{\mathfrak d}(c')^3\); the column \(\mathfrak c'\) enters only through \(\lambda(\mathfrak c')\), \(\chi_{\mathfrak d}(c')^3\) and the profile argument. Since \(\Phi\) decays rapidly for large argument, the effective length of the column sum is \(q_{\mathfrak c'}\lesssim q_{\mathfrak d}^2q_{\mathfrak f}^2/Z\le q_{\mathfrak d}^2q_{\mathfrak h}/Z\) by (2.2); this is the length \(D^2P/Z\) of Proposition 4.1 of Lesson 5.

## 6. Exercises

**6.1.** Derive (1.1) from (1.3) of Lesson 6.

**6.2.** Show that \(s_{\mathfrak p,4,e}=W_e(q_{\mathfrak p}-1)/\tau_{\mathfrak p,4}\) for \(e>0\), and compute \(|s_{\mathfrak p,4,e}|\) for \(e=1\) and \(e=3\).

**6.3.** Suppose \(m\) generates a squarefree exterior ideal. Show that \(\mathcal F(\mathfrak h)=\{R\}\) and \(\mathcal A(R)=\{R\}\), and write (5.1) in this case.

**6.4.** Show that \(\xi_{\mathfrak p}=g_{3,\mathfrak p}/g_{-1,\mathfrak p}\) in the notation \(g_j=q^{-1/2}\sum_x\chi(x)^j\psi(x/p)\) of Lesson 6, Section 4, and conclude \(|\xi_{\mathfrak p}|=1\).

**6.5.** Let \(\mathfrak h=\mathfrak p^6\). List \(\mathcal F(\mathfrak h)\), and compute \(I_{\mathfrak h,\mathfrak f}\) for each member.

## 7. Solutions

**6.1.** Bimultiplicativity gives \(\mathcal C(p^{e_1}u,p^{e_2}v)=\mathcal C(p,p)^{e_1e_2}\,\mathcal C(p,v)^{e_1}\)\(\,\mathcal C(u,p)^{e_2}\,\mathcal C(u,v)\). By (1.3) of Lesson 6 the first and last factors are \(1\), \(\mathcal C(p,v)=\chi(v)^{-2}\) and \(\mathcal C(u,p)=\chi(u)^2\).

**6.2.** For \(e>0\) and \(j=4\), (1.2) at \(t=1\) gives \(W_e\tau_{\mathfrak p,4}^{-1}\sum_{x\ne0}\chi(x)^{-4}\chi(x)^4\)\(=W_e(q-1)/\tau_{\mathfrak p,4}\). Its absolute value is \(|W_e|(q-1)q^{-1/2}\): for \(e=1\) this is \((q-1)/q\), and for \(e=3\) it is \((q-1)q^{-3/2}\).

**6.3.** If \(\mathfrak m\) is squarefree, \(\mathfrak h=R\), whose radical is \(R\), so \(\mathcal F(\mathfrak h)=\{R\}\); \(\mathcal A(R)=\{R\}\) by definition, \(I_{R,R}=1\) and \(f=1\). Then \(\omega_{\upsilon,\mathfrak t}=L(n')^{-3}\), the tuple is \((R,R,R,\mathfrak n',u)\), and (5.1) reads
\[
\begin{aligned}
B_m(Z)&=\sum_{\mathfrak n',u,z_d,z_c}\frac{L(n')^{-3}}{q_{\mathfrak n'}}\rho(\mathfrak d)\\
&\quad \sum_{\mathfrak c'}\frac{\lambda(\mathfrak c')}{q_{\mathfrak c'}^{1/2}}\chi_{\mathfrak d}(c')^3\\
&\quad \,\Phi_{\upsilon,\kappa_6}\Bigl(\frac{Zq_{\mathfrak c'}q_{\mathfrak n'}^3}{q_{\mathfrak d}^2}\Bigr).
\end{aligned}
\]

**6.4.** By (1.4), \(\xi_{\mathfrak p}=\bigl(q^{1/2}g_3\bigr)/\bigl(q^{1/2}g_{-1}\bigr)\), since \(\tau_{\mathfrak p,1}=\sum_x\chi(x)^{-1}\psi(x/p)=q^{1/2}g_{-1}\). Both \(g_3\) and \(g_{-1}\) have absolute value \(1\) (Lesson 6, Section 4), so \(|\xi_{\mathfrak p}|=1\).

**6.5.** The radical is \(\mathfrak p\) and \(j_{\mathfrak p}=0\), so \(\mathcal F(\mathfrak h)=\{R,\mathfrak p\}\): the prime may be inactive or active. Then \(I_{\mathfrak h,R}=1-q_{\mathfrak p}^{-1}\) and \(I_{\mathfrak h,\mathfrak p}=1\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 6.2. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [QuasiRH] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*, OpenAI Math Release preprint, 30 September 2026, Part I, Sections 5–7. https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026
