# The coefficient family and the plan of the zero-free argument

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson defines the sums \(B_m(Z)\) on which the proof of the zero-free strip rests, states the two estimates that the following lessons prove, and proves the final step: a power saving for one inverse Mellin integral excludes zeros of \(L_F(s,\eta)\) from a half-plane. The sums \(B_m(Z)\) are smoothed series over ideals \(\mathfrak A=\mathfrak c\mathfrak n^3\) of cubic Gauss sum coefficients twisted by the sextic symbol \(\chi_{\mathfrak A}(m)\). Lessons 6–10 bound their mean square over a box of rows \(m\). Lessons 11–14 insert them into an additive average, the probe, and evaluate that average by Poisson summation; its main term contains \(1/L^S(s,\eta)\). Comparing the upper bound with the evaluation gives the power saving.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Lemma 2.1 and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Section 1; [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), (3.1), Proposition 5.1 and Lemma 6.1; [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10); [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01), Lemmas A.2 and A.3; [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017), Section F4.

## 1. Incomplete L-functions

Keep \(F\supseteq\mu_{12}\), \(S\), \(R\), \(\eta\) and the allowed generators of Lessons 2–4. For \(\operatorname{Re}s>1\) put
\[
\begin{gathered}
\zeta_F^S(s)=\sum_{\mathfrak a}q_{\mathfrak a}^{-s},\\
\begin{aligned}
L^S(s,\eta)&=\prod_{\mathfrak p\notin S}\bigl(1-\eta(\mathfrak p)q_{\mathfrak p}^{-s}\bigr)^{-1},
\end{aligned}\quad(1.1)
\end{gathered}
\]
the sums and products being over exterior ideals and primes. The same symbols denote their meromorphic continuations to \(\mathbb C\) ([*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10)); \(L^S(s,\eta)\) is entire unless \(\eta\) is principal, when it has a simple pole at \(s=1\). It differs from \(L_F(s,\eta)\) by the finitely many factors \(1-\eta(\mathfrak p)q_{\mathfrak p}^{-s}\) with \(\mathfrak p\in S\) unramified for \(\eta\), whose zeros lie on \(\operatorname{Re}s=0\).

## 2. A Gaussian weight

For \(t>0\) put
\[
\begin{aligned}
&P_G(t)\\
&\quad =\frac1{2\sqrt\pi}\exp\Bigl(-\frac{(\log t)^2}4\Bigr).\quad(2.1)
\end{aligned}
\]

**Lemma 2.1.** For every \(\xi\in\mathbb C\), \(\int_0^\infty P_G(t)t^\xi\,\frac{dt}t=e^{\xi^2}\). For every real \(\sigma\) and \(t>0\), \(P_G(t)\le e^{\sigma^2}t^{-\sigma}\).

*Proof.* With \(v=\log t\) the integral is \(\frac1{2\sqrt\pi}\int_{\mathbb R}e^{-v^2/4+\xi v}\,dv\)\(=\frac{e^{\xi^2}}{2\sqrt\pi}\int_{\mathbb R}e^{-(v-2\xi)^2/4}\,dv=e^{\xi^2}\), first for real \(\xi\) and then for all \(\xi\) because both sides are entire. The bound follows from \(v^2/4\ge\sigma v-\sigma^2\). \(\square\)

## 3. The coefficient sums

Put \(\vartheta=\overline\Lambda\,\overline G\,\eta\) as in Lesson 4. For \(m\in R\) and \(Z>0\) define
\[
\begin{gathered}
\begin{aligned}
B_m(Z)&=\sum_{\substack{\mathfrak c\ \text{squarefree}\\ \mathfrak n}}\frac{\gamma_2(\mathfrak c)}{q_{\mathfrak c}^{1/2}q_{\mathfrak n}}\\
&\quad \,\vartheta(\mathfrak A)\,\chi_{\mathfrak A}(m)\,P_G\Bigl(\frac{q_{\mathfrak A}}Z\Bigr),
\end{aligned}\\
\mathfrak A=\mathfrak c\mathfrak n^3 ,\quad(3.1)
\end{gathered}
\]
where \(\mathfrak c\) runs over squarefree exterior ideals and \(\mathfrak n\) over all exterior ideals, possibly sharing primes with \(\mathfrak c\). The symbol \(\chi_{\mathfrak A}(m)\) carries the unit mask of Lesson 3, so it vanishes when \(m\) and \(\mathfrak A\) share a prime.

**Lemma 3.1** ([OpenAI-029, (4.2)–(4.3)]). The series (3.1) converges absolutely, and for every \(\sigma>1/2\)
\[
\begin{aligned}
&\sum_{\mathfrak c,\mathfrak n}\Bigl|\frac{\gamma_2(\mathfrak c)}{q_{\mathfrak c}^{1/2}q_{\mathfrak n}}\,P_G\Bigl(\frac{q_{\mathfrak A}}Z\Bigr)\Bigr|\\
&\quad\le e^{\sigma^2}Z^\sigma\,\zeta_F^S(\sigma+\tfrac12)\\
&\qquad\times\zeta_F^S(3\sigma+1).\quad(3.2)
\end{aligned}
\]
Moreover \(B_0(Z)=P_G(1/Z)\).

*Proof.* For squarefree \(\mathfrak c\), \(|\gamma_2(\mathfrak c)|=1\): by (5.2) of Lesson 4 it is a product of prime Gauss sums of absolute value \(1\) and of roots of unity. Lemma 2.1 gives \(P_G(q_{\mathfrak A}/Z)\le e^{\sigma^2}Z^\sigma q_{\mathfrak c}^{-\sigma}q_{\mathfrak n}^{-3\sigma}\), and the remaining sum is at most \(\zeta_F^S(\sigma+1/2)\zeta_F^S(3\sigma+1)\), finite for \(\sigma>1/2\). For \(m=0\), \(\chi_{\mathfrak A}(0)=0\) unless \(\mathfrak A=R\), which forces \(\mathfrak c=\mathfrak n=R\). \(\square\)

The value of \(\vartheta(\mathfrak A)\chi_{\mathfrak A}(m)\) does not depend on any choice of generators; the factor \(\gamma_2(\mathfrak c)/(q_{\mathfrak c}^{1/2}q_{\mathfrak n})\) will be identified in Lesson 6 as the product of the local spherical Whittaker values of a cubic theta function at the idèle with components \(A=cn^3\).

## 4. Scales, rows and their two parts

The comparison uses the exponents
\[
\begin{gathered}
a=\frac9{10},\qquad b=\frac{133}{1000},\\
M_0=a+b=\frac{1033}{1000},\\
h_0=1-a=\frac1{10},\\
X=Z^a,\qquad Y=Z^b .\quad(4.1)
\end{gathered}
\]
For a compact set \(\mathscr K\subset F_S^\times\) put
\[
\mathscr B_Z(\mathscr K)=R\cap\ell_{Z^{M_0}}\mathscr K ,
\]
with \(\ell_T\) as in Lesson 2. On this set every local absolute value of \(\ell_{Z^{M_0}}^{-1}m\) is bounded above and away from zero; in particular \(q_{(m)}\asymp_{\mathscr K}Z^{M_0}\). For \(m\ne0\) factor its exterior ideal as
\[
\begin{gathered}
(m)_S=\mathfrak h(m)\,\mathfrak d(m),\\
\mathfrak h(m)=\prod_{v_{\mathfrak p}(m)\ge2}\mathfrak p^{v_{\mathfrak p}(m)},\\
\mathfrak d(m)=\prod_{v_{\mathfrak p}(m)=1}\mathfrak p .\quad(4.2)
\end{gathered}
\]
The ideal \(\mathfrak d(m)\) is squarefree and prime to \(\mathfrak h(m)\), and every exponent of \(\mathfrak h(m)\) is at least \(2\): \(\mathfrak h(m)\) is **powerful**.

**Proposition 4.1** (the reflected second moment [OpenAI-029, Proposition 4.1]). Fix a compact set \(\mathscr K\subset F_S^\times\). For every \(\epsilon>0\), every \(Z\ge2\) and all \(P,D\ge1\),
\[
\begin{aligned}
&\sum_{\substack{m\in\mathscr B_Z(\mathscr K)\\ P\le q_{\mathfrak h(m)}<2P\\ D\le q_{\mathfrak d(m)}<2D}}|B_m(Z)|^2\\
&\quad \ll_{\mathscr K,\epsilon}Z^\epsilon P^{1/2}\Bigl(D+\frac{D^2P}Z\Bigr),\quad(4.3)
\end{aligned}
\]
and consequently
\[
\begin{aligned}
&\sum_{m\in\mathscr B_Z(\mathscr K)}|B_m(Z)|^2\\
&\quad \ll_{\mathscr K,\epsilon}Z^{2M_0-1+\epsilon}.\quad(4.4)
\end{aligned}
\]
The estimate is uniform when \(\mathscr K\) is multiplied by an element of a fixed compact subset of \(F_S^1\).

Lessons 6–10 prove Proposition 4.1. The deduction of (4.4) from (4.3) is short: a nonempty dyad has \(P,D\ge1\) and \(PD\ll Z^{M_0}\), so \(P^{1/2}D\le PD\ll Z^{M_0}\le Z^{2M_0-1}\) (as \(M_0>1\)) and \(P^{1/2}D^2P/Z=(PD)^2/(ZP^{1/2})\)\(\ll Z^{2M_0-1}\); there are \(O((\log Z)^2)\) dyads.

## 5. The probe and its two evaluations

Lesson 11 defines, for weights \(W_0,W_1\) fixed there, an average
\[
I_Z=I(Z^a,Z^b,Z)
\]
which pairs \(B_m(Z)\), for \(m\) in a compact annular box of norm \(\asymp XY=Z^{M_0}\), with a normalized sum of \(\chi_{\mathfrak s}(d)\,\mathrm e(-md/s)\) over exterior ideals \(\mathfrak s\) of norm \(\asymp Y\) and residues \(d\) modulo \(\mathfrak s\). The rest of the proof consists of three statements.

- **(P1)** (Lesson 11) For every \(\epsilon>0\), \(I_Z\ll Z^{(2M_0-1-b)/2+\epsilon}=Z^{933/2000+\epsilon}\). The additive factor has squared mass \(O(Y^{-1})\) over the rows, by a large sieve for additive fractions; with (4.4) and Cauchy–Schwarz this gives (P1).
- **(P2)** (Lessons 11–14) There is a constant \(c_0\ne0\) such that, for large \(Z\),
\[
\begin{gathered}
\begin{aligned}
I_Z&=c_0f_\eta(Z)\\
&\quad +O\bigl(Z^{7/15-0.0004}\bigr),
\end{aligned}\\
\begin{aligned}
f_\eta(Z)&=\frac1{2\pi i}\int_{(2)}Z^{s-8/15}\\
&\quad e^{(s-5/6)^2}\,\frac{\mathcal H_\eta(s)}{L^S(s,\eta)}\\
&\quad \,ds .
\end{aligned}\quad(5.1)
\end{gathered}
\]
- **(H)** (Lesson 12) The function \(\mathcal H_\eta\), an Euler product of local corrections, is holomorphic, bounded and nowhere zero on an open neighbourhood of the closed half-plane \(\operatorname{Re}s\ge0.998\), uniformly in the height.

The exponent \(s-8/15\) in (5.1) is \(a/2+s-1+h_0/6\); at \(s=1\) it is \(7/15\). The reflection exponent is
\[
\begin{aligned}
\frac{2M_0-1-b}2&=\frac{933}{2000}\\
&=\frac7{15}-\frac1{6000}.\quad(5.2)
\end{aligned}
\]
So (P1) and (P2) together give, for large \(Z\),
\[
f_\eta(Z)\ll Z^{7/15-1/20000},
\tag{5.3}
\]
using (P1) with \(\epsilon=10^{-5}\) and \(1/6000-10^{-5}>1/20000\), and \(0.0004>1/20000\).

## 6. From a power saving to a zero-free half-plane

**Proposition 6.1** (Mellin continuation [OpenAI-029, Section 8.3]). Let \(\delta_1>0\) and let \(\mathcal H\) be holomorphic, bounded and nowhere zero on an open set containing the closed half-plane \(\operatorname{Re}s\ge1-\delta_1\). For real \(c,s_0\) put
\[
\begin{gathered}
\begin{aligned}
f(Z)&=\frac1{2\pi i}\int_{(2)}Z^{s-c}e^{(s-s_0)^2}\\
&\quad \,\frac{\mathcal H(s)}{L^S(s,\eta)}\,ds
\end{aligned}\\
(Z>0).
\end{gathered}
\]
If \(0<\delta\le\delta_1\) and \(f(Z)\ll Z^{1-c-\delta}\) for all large \(Z\), then \(L^S(s,\eta)\) and \(L_F(s,\eta)\) have no zero in \(\operatorname{Re}s>1-\delta\).

*Proof.* Put \(\mathscr A(s)=e^{(s-s_0)^2}\mathcal H(s)/L^S(s,\eta)\). For \(\operatorname{Re}s=\sigma>1\), the Euler product gives \(|1/L^S(s,\eta)|\le\prod_{\mathfrak p}(1+q_{\mathfrak p}^{-\sigma})\le\zeta_F(\sigma)\), and \(|e^{(s-s_0)^2}|=e^{(\sigma-s_0)^2-(\operatorname{Im}s)^2}\). So \(\mathscr A\) is holomorphic on \(\operatorname{Re}s>1\) and decays like a Gaussian on vertical lines there, uniformly on compact ranges of \(\sigma\).

*Small \(Z\).* By Cauchy's theorem (Lemma A.2 of [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01)), the line of integration may be moved from \(2\) to any \(\sigma_R>2\), the horizontal segments vanishing by the Gaussian decay. On the new line \(|Z^{s-c}|=Z^{\sigma_R-c}\). Hence \(f(Z)=O_{A}(Z^{A})\) for \(0<Z\le1\) and every \(A>0\).

*The transform.* By the two bounds, \(\mathcal T(s)=\int_0^\infty f(Z)Z^{c-s}\,\frac{dZ}Z\) converges absolutely and locally uniformly on \(\operatorname{Re}s>1-\delta\): at infinity the integrand is \(O(Z^{1-\delta-\operatorname{Re}s})\), and at zero it is \(O(Z^A)\) for every \(A\). So \(\mathcal T\) is holomorphic there.

*Identification.* With \(Z=e^t\) and \(s=2+i\tau\), the definition of \(f\) reads
\[
e^{-(2-c)t}f(e^t)=\frac1{2\pi}\int_{\mathbb R}e^{i\tau t}\mathscr A(2+i\tau)\,d\tau .
\]
The function \(h(\tau)=\mathscr A(2+i\tau)\) is a Schwartz function: \(\mathscr A\) is holomorphic with Gaussian decay on \(\frac32\le\operatorname{Re}s\le\frac52\), so Cauchy's estimates on discs of radius \(\frac12\) (Lemma A.2 of [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01)) bound every derivative of \(h\) by a Gaussian. The left side is the inverse Fourier transform of \(h\), and the Fourier transform of the left side is \(\tau\mapsto\mathcal T(2+i\tau)\). Fourier inversion on Schwartz functions ((F13) in Section F4 of [*Schwartz functions and Fourier inversion*](course:AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017)) gives \(\mathcal T(2+i\tau)=\mathscr A(2+i\tau)\) for all real \(\tau\). Both functions are holomorphic on \(\operatorname{Re}s>1\), so they agree there, because the zeros of a nonzero holomorphic function on a connected open set are isolated (Lemma A.3 of [*Dirichlet series and Euler products*](course:NT-ZETA/NT-ZETA-01)). On \(\operatorname{Re}s>1-\delta\) the function \(\mathscr A\) is meromorphic, by the continuation of \(L^S(s,\eta)\), and agrees with the holomorphic \(\mathcal T\) on an open subset of this connected half-plane; so \(\mathscr A\) has no pole there.

*Conclusion.* If \(L^S(s_1,\eta)=0\) with \(\operatorname{Re}s_1>1-\delta\), then \(s_1\) is a pole of \(\mathscr A\), because \(e^{(s-s_0)^2}\mathcal H(s)\) does not vanish there; this is impossible. A pole of \(L^S\) at \(s=1\) only makes \(\mathscr A\) vanish. Finally \(L_F(s,\eta)\) differs from \(L^S(s,\eta)\) by finitely many factors \(1-\eta(\mathfrak p)q_{\mathfrak p}^{-s}\) with \(|\eta(\mathfrak p)|=1\), whose zeros have real part \(0\). \(\square\)

**Corollary 6.2.** Statements (P1), (P2) and (H) imply Theorem 5.3 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md): \(L_F(s,\eta)\) has no zero in \(\operatorname{Re}s>1-1/20000\), in particular none in \(\operatorname{Re}s>1-10^{-6}\).

*Proof.* Apply Proposition 6.1 with \(c=8/15\), \(s_0=5/6\), \(\mathcal H=\mathcal H_\eta\), \(\delta_1=0.002\) and \(\delta=1/20000\), using (5.3) and (H); note \(1-c-\delta=7/15-1/20000\). The field \(F\) and the character \(\eta\) were arbitrary, and the number \(1/20000\) does not depend on them. \(\square\)

All constants and the points from which (P1), (P2) and (5.3) hold may depend on \(F\), \(S\), \(\eta\) and the weights; only the numerical saving \(1/20000\) is uniform, and that is all Corollary 6.2 needs.

## 7. A map of Lessons 6–14

- **Lesson 6** introduces the cubic theta representation of Kazhdan and Patterson and computes its local Whittaker functions; their product at \(A=cn^3\) is the coefficient in (3.1).
- **Lesson 7** chooses the components at \(S\), bounds the integrals over sets of fixed norm, and constructs a kernel that turns the archimedean Whittaker profile into exactly \(P_G\).
- **Lesson 8** writes \(B_m(Z)\) as an average of the theta function over a torus orbit, with the twist \(\chi_{\mathfrak A}(m)\) inserted by unipotent translations.
- **Lesson 9** applies the rational Weyl element, which reflects the norm and turns the moving twist into a quadratic symbol \(\chi_{\mathfrak d}(c')^3\) between a row prime and a column prime.
- **Lesson 10** bounds the reflected sums with the quadratic large sieve over number fields and proves Proposition 4.1.
- **Lesson 11** defines the probe, proves (P1), and applies Poisson summation, which produces three Mellin variables and a Dirichlet series indexed by frequencies \(ur^6\).
- **Lesson 12** factors that Dirichlet series as \(\zeta_F^S(6z)L^S(w,\chi_\bullet(u))\,\mathcal H_u\)\(/L^S(\xi,\eta\overline{\chi_\bullet(u)})\) and proves (H).
- **Lesson 13** bounds the inverse \(L\)-functions of the other frequencies by a conductor large sieve and zero detection.
- **Lesson 14** isolates the double residue of the principal frequency, bounds everything else, and proves (P2).

## 8. Exercises

**8.1.** Compute \(\int_0^\infty P_G(t)\,\frac{dt}t\) and \(\int_0^\infty P_G(t)\,dt\).

**8.2.** Show that every powerful ideal has a unique expression \(\mathfrak r^2\mathfrak s^3\) with \(\mathfrak s\) squarefree, and deduce that the number of powerful exterior ideals of norm less than \(2P\) is \(O(P^{1/2})\).

**8.3.** Check the arithmetic \(a/2+1-1+h_0/6=7/15\) and \((2M_0-1-b)/2=933/2000\)\(=7/15-1/6000\).

**8.4.** In Proposition 6.1, suppose only that \(f(Z)\ll Z^{1-c}\). What does the proof give?

## 9. Solutions

**8.1.** Lemma 2.1 with \(\xi=0\) gives \(1\); with \(\xi=1\) it gives \(e\).

**8.2.** For a prime exponent \(e\ge2\), write \(e=2r+3s\) with \(s\in\{0,1\}\) equal to the parity of \(e\); this is possible and unique since \(e-3s\) is then even and nonnegative. The number of \(\mathfrak r^2\mathfrak s^3\) of norm less than \(2P\) is at most \(\sum_{\mathfrak s}\#\{\mathfrak r:q_{\mathfrak r}<(2P)^{1/2}q_{\mathfrak s}^{-3/2}\}\)\(\ll P^{1/2}\sum_{\mathfrak s}q_{\mathfrak s}^{-3/2}\ll P^{1/2}\), using that there are \(O(t)\) ideals of norm at most \(t\).

**8.3.** \(9/20+1/60=27/60+1/60\)\(=28/60=7/15\). \(2M_0-1-b=2.066-1-0.133\)\(=0.933\), and \(7/15-933/2000\)\(=(2800-2799)/6000=1/6000\).

**8.4.** The transform converges on \(\operatorname{Re}s>1\) only, and no zero is excluded; the argument needs a genuine power saving \(\delta>0\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 4 and 8. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
