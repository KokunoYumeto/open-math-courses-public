# The zero-free strip

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson contains the last part of the proof of the zero-free strip. [*The Poisson probe*](the-poisson-probe.md) wrote the probe as a triple Mellin integral over the frequency classes \(u\), and [*The Euler product of the probe*](the-euler-product-of-the-probe.md) factored each Dirichlet series. Here the contours are moved. For \(u=1\) the numerator \(\zeta_F^S(6z)\zeta_F^S(w)\) has poles at \(z=\frac16\) and \(w=1\), and their double residue is the main term \(c_0f_\eta(Z)\) of statement (P2). For \(u\ne1\) the numerator is entire, and the contours can be moved left until the power of \(Z\) falls below the main term: directly for small frequencies, with the zero detection of [*Zero detection for the frequency characters*](zero-detection.md) for intermediate ones, and by a far rightward shift for large ones. Together with (P1) and (H), this proves Theorem 5.3 of [*Artin's conjecture and the index of a prime*](artins-conjecture-and-the-index-of-a-prime.md).

**Prerequisites.** [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Sections 4–6; [*The Poisson probe*](the-poisson-probe.md), Lemma 1.1, Proposition 4.1 and Proposition 7.1; [*The Euler product of the probe*](the-euler-product-of-the-probe.md), Proposition 5.1 and Corollary 5.2; [*Zero detection for the frequency characters*](zero-detection.md), Lemmas 1.1 and 3.1 and Proposition 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Lemma 3.2; [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10), Theorem 10.1 and Corollary 10.4.

## 1. The power of Z on a contour

Take \(X=Z^a\), \(Y=Z^b\) in (7.1) of Lesson 11, with \(a=\frac9{10}\), \(b=\frac{133}{1000}\), \(h_0=1-a=\frac1{10}\). Write \(\sigma_\xi,\sigma_w,\sigma_z\) for the real parts of \(\xi,w,z\). The modulus of \(X^{1/2-z}Z^{\xi+z-1}Y^{w-1}\) is \(Z^{E_*}\) with
\[
\begin{aligned}
&E_*(\sigma_\xi,\sigma_w,\sigma_z)=\frac a2+\sigma_\xi-1\\
&\qquad +h_0\sigma_z+b(\sigma_w-1),\quad(1.1)
\end{aligned}
\]
and the factor \(q_u^{-z}\) has modulus \(q_u^{-\sigma_z}\). At \(w=1\), \(z=\frac16\) the power becomes \(Z^{C_*(\xi)}\) with
\[
\begin{gathered}
\begin{aligned}
C_*(\xi)&=\frac a2+\xi-1+\frac{h_0}6\\
&=\xi-\frac8{15},
\end{aligned}\\
C_*(1)=\frac7{15}.\quad(1.2)
\end{gathered}
\]
All comparisons below are with the reference power \(C_*(1)\).

On every fixed strip of real parts, (1.3) and (1.1) of Lesson 11 give, for every \(A>0\),
\[
\begin{aligned}
&\bigl|e^{(\xi+z-1)^2}M(z)\widehat W_1(w)\bigr|\\
&\quad\le C_A\,e^{-(\operatorname{Im}\xi+\operatorname{Im}z)^2}\\
&\qquad\times(1+|\operatorname{Im}z|)^{-A}\\
&\qquad\times(1+|\operatorname{Im}w|)^{-A}.\quad(1.3)
\end{aligned}
\]
On the contours below every numerator \(L\)-function and zeta function grows at most polynomially in the heights, away from the poles that are extracted (Lemma 3.1 of Lesson 13 and the remark after it), \(\mathcal H_u\) is at most \(C_\epsilon q_u^\epsilon\) (Proposition 5.1 of Lesson 12), and on lines \(\operatorname{Re}\xi>1\) the reciprocal \(1/L^S\) is bounded by its absolutely convergent Euler product. Since \(\int_{\mathbb R}e^{-(T+v)^2}(1+|v|)^{-A}\,dv\)\(\le C_{A_1}(1+|T|)^{-A_1}\) once \(A\) is large, integrating in \(z\) and \(w\) first gives decay faster than any power in \(\operatorname{Im}\xi\) as well. These bounds justify every shift of an infinite contour below, the horizontal segments tending to zero.

## 2. The principal frequency

Let \(I_1(Z)\) be the term \(u=1\) of (7.1) of Lesson 11. By Proposition 5.1 of Lesson 12 its Dirichlet series is \(\zeta_F^S(6z)\zeta_F^S(w)\mathcal H_1(\xi,w,z)/L^S(\xi,\eta)\). Put
\[
\begin{gathered}
\delta_1=10^{-7},\\
\sigma_1=1+\delta_1,\\
\zeta_1=\frac16+\delta_1 .
\end{gathered}
\]
Move the lines from \((\operatorname{Re}\xi,\operatorname{Re}w,\operatorname{Re}z)=(4,4,2)\) to \((\sigma_1,\sigma_1,\zeta_1)\): no pole is crossed, since \(\operatorname{Re}w>1\), \(\operatorname{Re}6z>1\) and \(1/L^S(\xi,\eta)\) stays in absolute convergence, and the second region of (5.1) of Lesson 12 contains the whole move. Then move \(w\) to \(\operatorname{Re}w=0.95\), crossing the simple pole of \(\zeta_F^S(w)\) at \(w=1\); call the remaining triple integral \(R_w(Z)\). In the residue at \(w=1\), move \(z\) to \(\operatorname{Re}z=0.16\), crossing the simple pole of \(\zeta_F^S(6z)\) at \(z=\frac16\); call the remaining integral \(R_z(Z)\). So
\[
\begin{aligned}
I_1(Z)&=c_0f_\eta(Z)+R_w(Z)\\
&\quad +R_z(Z),\quad(2.1)
\end{aligned}
\]
where the double residue is computed in Proposition 2.2. The contours of the remainders are
\[
\begin{gathered}
\begin{aligned}
R_w&:\ (\operatorname{Re}\xi,\operatorname{Re}w,\operatorname{Re}z)\\
&=(\sigma_1,0.95,\zeta_1),
\end{aligned}\\
\begin{aligned}
R_z&:\ (\operatorname{Re}\xi,w,\operatorname{Re}z)\\
&=(\sigma_1,1,0.16).
\end{aligned}
\end{gathered}
\]

**Lemma 2.1** (the principal remainders [OpenAI-029, (8.6)]). \(R_w(Z)\) and \(R_z(Z)\) are \(O\bigl(Z^{C_*(1)-0.0005}\bigr)\).

*Proof.* By (1.1) and (1.2), the powers of \(Z\) relative to \(C_*(1)\) are
\[
\begin{aligned}
&E_*(\sigma_1,0.95,\zeta_1)-C_*(1)\\
&\quad=(1+h_0)\delta_1-0.05\,b\\
&\quad=-0.00664989,\\
&E_*(\sigma_1,1,0.16)-C_*(1)\\
&\quad=\delta_1+h_0\bigl(0.16-\tfrac16\bigr)\\
&\quad=-0.000666566\ldots,
\end{aligned}
\]
both below \(-0.0005\). On these contours \(|\zeta_F^S(6z)|\le\zeta_F(1+6\delta_1)\) or grows polynomially, \(\zeta_F^S(w)\) grows polynomially away from \(w=1\), \(1/L^S(\xi,\eta)\) is bounded, and \(\mathcal H_1\) is bounded; (1.3) makes the integrals converge. \(\square\)

Let \(R_S=\operatorname{Res}_{s=1}\zeta_F^S(s)\), which is positive: it is the residue of \(\zeta_F\) (Corollary 10.4 of [*Hecke L-functions and the Dedekind zeta function*](course:NT-ADL/NT-ADL-10)) times \(\prod_{\mathfrak p\in S}(1-q_{\mathfrak p}^{-1})\).

**Proposition 2.2** (the double residue [OpenAI-029, (8.7)]). The double residue in (2.1) is \(c_0f_\eta(Z)\), with
\[
\begin{gathered}
c_0=\frac{R_S^2}6\,M\bigl(\tfrac16\bigr)\,\widehat W_1(1)\ne0,\\
\begin{aligned}
f_\eta(Z)&=\frac1{2\pi i}\int_{(2)}Z^{C_*(\xi)}\\
&\quad e^{(\xi-5/6)^2}\frac{\mathcal H_\eta(\xi)}{L^S(\xi,\eta)}\,d\xi ,
\end{aligned}\quad(2.2)
\end{gathered}
\]
the function \(f_\eta\) of (5.1) of Lesson 5.

*Proof.* The residue of \(\zeta_F^S(w)\) at \(w=1\) is \(R_S\), and that of \(\zeta_F^S(6z)\) at \(z=\frac16\) is \(R_S/6\). At \(w=1\), \(z=\frac16\), and \(q_1=1\), the remaining factors of (7.1) of Lesson 11 are \(X^{1/3}Z^{\xi-5/6}e^{(\xi-5/6)^2}M(\frac16)\widehat W_1(1)\)\(\mathcal H_1(\xi,1,\frac16)/L^S(\xi,\eta)\), and \(X^{1/3}Z^{\xi-5/6}=Z^{C_*(\xi)}\) because \(\frac a3-\frac56=-\frac8{15}\). The \(\xi\)-line, at \(\operatorname{Re}\xi=\sigma_1\), may be moved to \(\operatorname{Re}\xi=2\) in absolute convergence. Finally \(R_S>0\), \(\widehat W_1(1)=\int_0^\infty W_1(t)\,dt>0\), and \(M(\frac16)\ne0\) by Lemma 1.1 of Lesson 11. \(\square\)

## 3. The other frequencies

Split the terms \(u\ne1\) of (7.1) of Lesson 11 into dyads \(U\le q_u<2U\), \(U=2^j\), before any shift; each dyad has finitely many terms, and the whole sum converges absolutely on the initial lines. For a set \(\mathcal C\) of \(u\ne1\) in one dyad write \(\mathcal J_{\mathcal C}(Z)\) for its contribution. For \(u\ne1\) the Kummer character \(\kappa_u\) is not principal (Lemma 3.2 of Lesson 3), so \(L^S(w,\chi_\bullet(u))\) is entire, and by Lemma 3.1 of Lesson 13 and the remark after it, with the conductor bound of Lemma 1.1 there,
\[
\begin{gathered}
\begin{aligned}
&|L^S(w,\chi_\bullet(u))|\\
&\quad \le C_\epsilon\,U^{1/2+\epsilon}(2+|\operatorname{Im}w|)^{A_F}
\end{aligned}\\
(0.003\le\operatorname{Re}w\le4).\quad(3.1)
\end{gathered}
\]
On \(\operatorname{Re}\xi=\sigma_1\), \(|L^S(\xi,\eta\overline{\chi_\bullet(u)})^{-1}|\)\(\le\prod_{\mathfrak p}(1+q_{\mathfrak p}^{-\sigma_1})\le\zeta_F(\sigma_1)\), uniformly in \(u\) and the height.

*The basic contour.* For each \(u\ne1\), move the lines, first \(\xi\), then \(z\), then \(w\), to
\[
(\operatorname{Re}\xi,\operatorname{Re}w,\operatorname{Re}z)=(\sigma_1,\ 0.003,\ 0.4).
\]
No pole is crossed: \(\operatorname{Re}6z\ge2.4\), the numerator in \(w\) is entire, the denominator stays in absolute convergence, and the first region of (5.1) of Lesson 12 contains the move. If \(|\mathcal C|\le CU^\alpha\), then by (3.1), \(q_u^{-z}\) and Proposition 5.1 of Lesson 12,
\[
\begin{aligned}
|\mathcal J_{\mathcal C}(Z)|&\le C_\epsilon\,Z^{E_*(\sigma_1,0.003,0.4)}\\
&\quad \,U^{\alpha+1/2-0.4+\epsilon}.\quad(3.2)
\end{aligned}
\]
The common relative exponent is
\[
\begin{aligned}
&E_*(\sigma_1,0.003,0.4)-C_*(1)\\
&\quad =10^{-7}+\frac7{300}-0.132601\\
&\quad =-0.109267566\ldots\quad(3.3)
\end{aligned}
\]
For a general \(z\)-line the factor depending on \(U\) is \((Z^{h_0}/U)^{\operatorname{Re}z}\) times \(U^{\alpha+1/2+\epsilon}\): a shift of \(z\) to the right helps exactly when \(U>Z^{h_0}=Z^{0.1}\). This decides the three ranges.

**Small frequencies, \(U\le Z^{0.09}\).** Use (3.2) with \(\alpha=1\) (Lemma 1.1 of Lesson 13). The factor \(U^{1.1}\) adds at most \(0.09\cdot1.1=0.099\), so the relative exponent is at most \(-0.010267566\ldots\)

**Intermediate frequencies, \(Z^{0.09}<U\le Z^{0.10001}\).** For large \(Z\) these \(U\) exceed the threshold \(U_0\) of Proposition 4.1 of Lesson 13. For the exceptional frequencies \(u\in\mathcal E(U)\), use (3.2) with \(\alpha=\frac12\): the factor \(U^{0.6}\) adds at most \(0.10001\cdot0.6=0.060006\), leaving at most \(-0.049261566\ldots\) For each \(u\notin\mathcal E(U)\), cut the \(\xi\)-line at \(|\operatorname{Im}\xi|\le U^\rho\) and move this finite segment to \(\operatorname{Re}\xi=0.998\). On the rectangle so swept, (4.1) of Lesson 13 bounds the reciprocal by \(C_\epsilon U^\epsilon\). The new central segment contributes, summed over the at most \(CU\) good frequencies of the dyad,
\[
\le C_\epsilon\,Z^{E_*(0.998,0.003,0.4)}\,U^{1+1/2-0.4+\epsilon},
\]
and \(E_*\) has coefficient \(1\) in \(\sigma_\xi\), so the move gains \(Z^{0.998-\sigma_1}=Z^{-0.0020001}\). With the factor \(U^{1.1}\le Z^{0.110011}\), the relative exponent is at most
\[
\begin{aligned}
&-0.002+\frac7{300}-0.132601\\
&\qquad +0.10001\cdot1.1=-\frac{377}{300000}\\
&\quad =-0.001256666\ldots\quad(3.4)
\end{aligned}
\]
The discarded tails of the line \(\operatorname{Re}\xi=\sigma_1\) and the horizontal segments at \(\operatorname{Im}\xi=\pm U^\rho\) are, by (1.3) integrated first in \(z,w\), at most
\[
C_{A_1,\epsilon}\,Z^{E_*(\sigma_1,0.003,0.4)}\,U^{1+1/2-0.4+\epsilon-\rho A_1}
\]
for every \(A_1\): on the horizontal segments the power of \(Z\) is at most its value at \(\sigma_1\) and the reciprocal is bounded by (4.1) of Lesson 13, and on the tails it is bounded by absolute convergence. Since \(U>Z^{0.09}\), the choice \(A_1>1/\rho\) makes these terms smaller than the central ones.

**Large frequencies, \(U>Z^{0.10001}\).** Here \(Z^{h_0}/U\le Z^{-0.00001}\). Keep \(\operatorname{Re}\xi=\operatorname{Re}w=4\) and move \(z\) to the fixed line \(\operatorname{Re}z=R_0=350000\); the move stays in the Euler region, crosses no pole, and \(M\) is holomorphic there. Both \(L\)-functions are bounded by their Euler products, and with \(E_*(4,4,R_0)=3.849+0.1R_0\),
\[
|\mathcal J_{\mathcal C}(Z)|\le C_\epsilon\,Z^{3.849+0.1R_0}\,U^{1-R_0+\epsilon}.
\]
The dyads sum geometrically; at the lowest one the power of \(Z\) is
\[
\begin{aligned}
&3.849+0.1R_0\\
&\qquad +0.10001(1-R_0+\epsilon)\\
&\quad =0.44901+0.10001\epsilon ,\quad(3.5)
\end{aligned}
\]
which is below \(C_*(1)-0.01=0.45666\ldots\) The constants on the line \(\operatorname{Re}z=R_0\) are large but do not depend on \(Z\) or \(U\).

**Proposition 3.1** (the nonprincipal frequencies [OpenAI-029, (8.12)]). For large \(Z\),
\[
\begin{aligned}
&\sum_{j\ge0}\mathcal J_{\{u\ne1:\,2^j\le q_u<2^{j+1}\}}(Z)\\
&\quad =O\bigl(Z^{C_*(1)-0.0004}\bigr).\quad(3.6)
\end{aligned}
\]

*Proof.* Choose the losses \(\epsilon\) so small that their total effect in the ranges \(U\le Z^{0.10001}\), including the \(O(\log Z)\) dyads, is below \(10^{-4}\) in the exponent of \(Z\). The smallest saving among the ranges is \(377/300000>0.0012\), in (3.4); the others are larger, and (3.5) gives a saving above \(0.01\). Each dyadic integral arose from its absolutely convergent initial form, and these bounds justify summing them. \(\square\)

## 4. Statement (P2) and the zero-free strip

**Theorem 4.1** ((P2) [OpenAI-029, Section 8.3]). For large \(Z\),
\[
\begin{aligned}
I(Z^a,Z^b,Z)&=c_0f_\eta(Z)\\
&\quad+O\bigl(Z^{7/15-0.0004}\bigr).
\end{aligned}
\]

*Proof.* Proposition 7.1 of Lesson 11 writes the probe as the sum over \(u\) of the triple integrals; (2.1), Lemma 2.1, Proposition 2.2 and Proposition 3.1 bound everything except \(c_0f_\eta(Z)\) by \(O(Z^{C_*(1)-0.0004})\), and \(C_*(1)=\frac7{15}\). \(\square\)

**Corollary 4.2** (the zero-free strip). For every cyclotomic field \(F\supseteq\mu_{12}\) and every finite-order Hecke character \(\eta\) of \(F\), \(L_F(s,\eta)\) has no zero in \(\operatorname{Re}s>1-\frac1{20000}\); in particular none in \(\operatorname{Re}s>1-10^{-6}\). This is Theorem 5.3 of Lesson 1.

*Proof.* Statement (P1) is Proposition 4.1 of Lesson 11, (P2) is Theorem 4.1, and (H) is Corollary 5.2 of Lesson 12. Corollary 6.2 of Lesson 5 deduces the corollary from these three statements. \(\square\)

The exponents used, before the arbitrarily small losses, are collected below; all are relative to \(C_*(1)=\frac7{15}\).

| Contribution | Relative exponent |
|---|---|
| Probe bound from reflection (P1) | \(-1/6000=-0.000166\ldots\) |
| Principal remainder \(R_w\) | \(-0.00664989\) |
| Principal remainder \(R_z\) | \(-0.000666566\ldots\) |
| Frequencies \(U\le Z^{0.09}\) | \(-0.010267566\ldots\) |
| Exceptional frequencies \(U\le Z^{0.10001}\) | \(-0.049261566\ldots\) |
| Good central frequencies \(U\le Z^{0.10001}\) | \(-0.001256666\ldots\) |
| Frequencies \(U>Z^{0.10001}\) | \(-0.017656666\ldots\) |

Comparing the first row with the others: the upper bound of (P1) and the evaluation of (P2) agree up to \(Z^{7/15-1/6000+\epsilon}\), which is what forces \(f_\eta(Z)\ll Z^{7/15-1/20000}\) and, by Proposition 6.1 of Lesson 5, the absence of zeros. The width \(\frac1{20000}\) depends on none of \(F\), \(S\), \(\eta\); the constants and the onset of "large \(Z\)" do.

## 5. Exercises

**5.1.** Derive (1.1) from the factors \(X^{1/2-z}Z^{\xi+z-1}Y^{w-1}\) with \(X=Z^a\), \(Y=Z^b\).

**5.2.** Check (3.3): \(h_0(0.4-\frac16)=\frac7{300}\) and \(b(0.003-1)=-0.132601\).

**5.3.** Verify (3.5), and find the smallest \(R_0\) for which the exponent (3.5) at \(\epsilon=0\) is below \(\frac7{15}-0.01\).

**5.4.** Explain why the principal frequency cannot be treated like the others: what would go wrong if one moved its \(w\)-line to \(0.003\)?

**5.5.** Show that \(\frac{933}{2000}=\frac7{15}-\frac1{6000}\), and that \(\frac1{6000}-10^{-5}>\frac1{20000}\).

## 6. Solutions

**5.1.** The modulus is \(Z^{a(1/2-\sigma_z)}Z^{\sigma_\xi+\sigma_z-1}Z^{b(\sigma_w-1)}\)\(=Z^{a/2+\sigma_\xi-1+(1-a)\sigma_z+b(\sigma_w-1)}\), and \(1-a=h_0\).

**5.2.** \(0.4-\frac16=\frac7{30}\), times \(\frac1{10}\) is \(\frac7{300}\); \(0.133\cdot0.997=0.132601\).

**5.3.** \(3.849+0.1R_0+0.10001\)\(-0.10001R_0=3.94901\)\(-0.00001R_0\); at \(R_0=350000\) this is \(0.44901\). The condition \(3.94901-0.00001R_0<0.456666\ldots\) holds for \(R_0>349234.33\ldots\), so the smallest integer is \(349235\); the chosen value leaves room.

**5.4.** At \(w=1\) the numerator \(\zeta_F^S(w)\) has a pole; moving the line past it produces the residue, which carries the main term. For \(u\ne1\) the numerator \(L^S(w,\chi_\bullet(u))\) is entire and no residue arises.

**5.5.** \(\frac7{15}=\frac{2800}{6000}\) and \(\frac{933}{2000}=\frac{2799}{6000}\). Then \(\frac1{6000}-\frac1{100000}=\frac{47}{300000}>\frac{15}{300000}=\frac1{20000}\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Sections 8.2–8.3. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
