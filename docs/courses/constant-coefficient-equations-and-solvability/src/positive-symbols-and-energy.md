# Positive symbols and energy estimates

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A nonnegative polynomial symbol gives a nonnegative quadratic form. On a bounded set, that form controls the quadratic form of every weaker operator, even when the symbol vanishes at real frequencies. The proof turns a quadratic expression into a linear Fourier-space estimate by using the autocorrelation of a test function.

Read [Operator strength and local inverses](operator-strength-and-local-inverses.md) and [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md) first. We use the Parseval–Plancherel theorem with the unnormalized Fourier transform. [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html), Theorem 2.1 and Sections 7.1–7.3, proves the Schwartz identity, its extension to the completed L² space and its agreement with ordinary inverse integrals. We use that written proof with its stated normalization. Grubb [Grubb] is a basic reference for the Fourier background.

Throughout, \(D=-i\partial\), \(P\ne0\), and
\[
S_P(\xi)=\left(\sum_\alpha|\partial^\alpha P(\xi)|^2\right)^{1/2}.
\]
The pairing in this lesson is the Hilbert-space pairing
\((v,u)=\int v\overline u\,dx\), linear in its first argument. Distributional transposition elsewhere in the course remains complex-linear and uses \(P(-D)\).

## The autocorrelation identity

For \(u\in C_c^\infty(\mathbb R^n)\), put
\[
\widetilde u(x)=\overline{u(-x)},\qquad v=u*\widetilde u.
\]
Both functions are smooth and compactly supported, and
\[
\begin{aligned}
\widehat{\widetilde u}(\xi)&=\overline{\widehat u(\xi)},\\
\widehat v(\xi)&=|\widehat u(\xi)|^2.
\end{aligned}
\tag{1}
\]
In particular, for any polynomial \(Q\), Fourier inversion and Parseval give
\[
\begin{aligned}
Q(D)v(0)&=(2\pi)^{-n}\int Q(\xi)|\widehat u(\xi)|^2\,d\xi\\
&=\int Q(D)u\,\overline u\,dx.
\end{aligned}
\tag{2}
\]
All integrals converge absolutely, since \(\widehat u\) is Schwartz. The conjugation in \(\widetilde u\) is essential: reflection without conjugation would give \(\widehat u(\xi)\widehat u(-\xi)\), which need not be nonnegative.

If \(\operatorname{supp}u\subset X\), then
\[
\begin{aligned}
\operatorname{supp}v&\subset
\operatorname{supp}u-\operatorname{supp}u\\
&\subset\overline X-\overline X.
\end{aligned}
\tag{3}
\]
For bounded \(X\), the last set is compact and can be used as one fixed support set for every such \(u\).

## A quadratic estimate from a regular inverse

Assume now that
\[
P(\xi)\geq0\qquad(\xi\in\mathbb R^n).
\tag{4}
\]
Define the energy
\[
\begin{aligned}
\mathcal A_P(u)&=(P(D)u,u)\\
&=(2\pi)^{-n}\int P(\xi)|\widehat u(\xi)|^2\,d\xi.
\end{aligned}
\tag{5}
\]
It is a real nonnegative number.

**Theorem 2.1.** For every bounded open set \(X\), there is \(C_{P,X}\) such that, writing \(M_Q=\sup_\xi |Q(\xi)|/S_P(\xi)\),
\[
\begin{aligned}
|(Q(D)u,u)|&\leq C_{P,X}M_Q\mathcal A_P(u),\\
u&\in C_c^\infty(X),\quad Q\prec P.
\end{aligned}
\tag{6}
\]
The constant is independent of \(u\) and \(Q\).

**Proof.** Let \(K=\overline X-\overline X\), and fix a smooth compact cutoff \(\chi\) equal to one near \(K\). Let \(E\) be a regular fundamental solution of \(P(D)\). The compact-data inverse estimate, with \(p=1\) and \(k=1\), gives
\[
\begin{gathered}
\|w\|_{1,S_P}\leq C_{P,K}\|P(D)w\|_{1,1},\\
\operatorname{supp}w\subset K.
\end{gathered}
\tag{7}
\]
Here is why one constant works for the whole support set. Write \(w=E*P(D)w\). For \(\psi\) equal to one near \(\operatorname{supp}\chi-K\), the equality
\(\chi w=\chi((\psi E)*P(D)w)\) holds. The kernel \(\psi E\) belongs to \(B_{\infty,S_P}\); the weighted convolution and cutoff bounds prove (7). None of these choices depends on \(w\).

Apply (7) to the autocorrelation \(v\) in (1). Set
\(M_Q=\sup_\xi |Q(\xi)|/S_P(\xi)<\infty\). Then
\[
\begin{aligned}
\|Q(D)v\|_{1,1}&\leq M_Q\|v\|_{1,S_P}\\
&\leq C_{P,K}M_Q\|P(D)v\|_{1,1}.
\end{aligned}
\tag{8}
\]
The Fourier transform of \(P(D)v\) is \(P|\widehat u|^2\). By (4) it is nonnegative, so
\[
\begin{aligned}
\|P(D)v\|_{1,1}&=(2\pi)^{-n}\int P|\widehat u|^2\\
&=\mathcal A_P(u).
\end{aligned}
\tag{9}
\]
Fourier inversion bounds \(|Q(D)v(0)|\) by \(\|Q(D)v\|_{1,1}\). Combine (2), (8), and (9). This proves (6). \(\square\)

The positivity assumption is used in the equality (9), not in the linear inverse estimate (7). It converts the Fourier \(L^1\) norm into the energy without cancellation.

Since \(S_P\) has a positive global lower bound, \(1\prec P\). Taking \(Q=1\) gives
\[
\|u\|_2^2\leq C'_{P,X}\mathcal A_P(u).
\tag{10}
\]
Thus a nonzero nonnegative symbol has strictly positive energy on every nonzero compactly supported test function. No positive lower bound for \(P(\xi)\) on the whole real frequency space is required. Bounded spatial support supplies the estimate.

## Which derivative norms are controlled?

For a polynomial \(R\), let \(\overline R\) denote coefficientwise conjugation. On real frequencies, \(R\overline R=|R|^2\). If
\[
R\overline R\prec P,
\tag{11}
\]
then (6) and Parseval give
\[
\begin{aligned}
\|R(D)u\|_2^2&=(R(D)u,R(D)u)\\
&=((R\overline R)(D)u,u)\\
&\leq C_{P,X,R}\mathcal A_P(u).
\end{aligned}
\tag{12}
\]
Condition (11) involves the square of the symbol. Merely knowing \(R\prec P\) controls its quadratic pairing in (6); it does not by itself turn that pairing into the squared derivative norm in (12).

For example, consider
\[
P(\xi_1,\xi_2)=\xi_1^2+\xi_2^4.
\]
Its energy is
\[
\mathcal A_P(u)=\|D_1u\|_2^2+\|D_2^2u\|_2^2.
\tag{13}
\]
The symbol \(\xi_2^2\) is weaker than \(P\). Indeed \(|\xi_2|^2\leq1+\xi_2^4\), while \(S_P\) controls both the nonnegative value \(P\) and a nonzero constant derivative. Hence (12), with \(R=\xi_2\), also controls \(\|D_2u\|_2^2\) by (13). Together with (10), the energy controls the function, its first derivative in each coordinate, and its second derivative in the second coordinate. It need not control every second derivative.

The estimates concern functions compactly supported in the open set. Taking a completion of these functions in an energy norm is a further choice of solution space. The present estimate does not prescribe boundary traces for an arbitrary nonelliptic operator.

## Two limits on the estimate

Boundedness of the set matters. In one dimension, let \(P(\xi)=\xi^2\), choose nonzero \(a\in C_c^\infty(\mathbb R)\), and put \(u_R(x)=a(x/R)\). Then
\[
\|u_R\|_2^2=R\|a\|_2^2,
\qquad \mathcal A_P(u_R)=R^{-1}\|a'\|_2^2.
\]
Their ratio tends to infinity. There is no single version of (10) for all compact supports in \(\mathbb R\).

Positivity matters as well. For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), take \(u(x_1,x_2)=a(x_1)b(x_2)\) with nonzero real test functions. Then
\[
(P(D)u,u)
=\left(\int(-ia')a\right)
 \left(\int(-ib')b\right)=0,
\]
because each integral is the integral of a derivative, multiplied by \(-i/2\). Yet \(\|u\|_2>0\), and \(1\prec P\). This rules out (6) with that sign-changing symbol, even on a bounded rectangle.

## Exercises with solutions

**Exercise 1 (entry).** Show directly that \(v(0)=\|u\|_2^2\) for the autocorrelation in (1). Verify the factor \((2\pi)^{-n}\) in its Fourier expression.

**Solution.** The convolution formula gives
\(v(0)=\int u(-y)\overline{u(-y)}\,dy=\|u\|_2^2\).
Fourier inversion at zero gives
\(v(0)=(2\pi)^{-n}\int\widehat v=(2\pi)^{-n}\int|\widehat u|^2\), exactly Parseval with the course convention.

**Exercise 2 (intermediate).** Suppose \(X\subset(a,b)\times\mathbb R^{n-1}\). Prove directly that
\(\|u\|_2^2\leq(b-a)^2\|D_1u\|_2^2\) for \(u\in C_c^\infty(X)\). Compare this with (10) for \(P=\xi_1^2\).

**Solution.** Extend \(u\) by zero. For each fixed transverse coordinate,
\(u(x_1,x')=\int_a^{x_1}\partial_1u(s,x')\,ds\).
Cauchy–Schwarz bounds its squared absolute value by
\((b-a)\int_a^b|\partial_1u(s,x')|^2\,ds\).
Integrate in \(x_1\) and \(x'\). Since \(|D_1u|=|\partial_1u|\), the stated estimate follows. It exhibits a concrete dependence on the width of the support region. This direct argument also works for an unbounded strip; the general theorem only needs the simpler bounded-set hypothesis.

**Exercise 3 (intermediate).** For the anisotropic symbol in (13), show that \(D_1^2u\) is not bounded in \(L^2\) by the square root of that energy on a fixed rectangle.

**Solution.** Let \(u_N=e^{iNx_1}a(x_1)b(x_2)\), with fixed nonzero test functions supported in the rectangle. Then
\(\|D_1^2u_N\|_2=N^2\|ab\|_2+O(N)\), by expanding \((D_1+N)^2a\).
The energy is \(N^2\|ab\|_2^2+O(N)+O(1)\), so its square root grows only like \(N\). The proposed estimate fails. Correspondingly, \(\xi_1^4\not\prec P\), as the ratio \(|\xi_1|^4/S_P(\xi_1,0)\) grows like \(|\xi_1|^2\).

**Exercise 4 (advanced).** If \(Q\prec P\) has complex coefficients, does (6) require its quadratic pairing to be real? Give an example and explain the role of the absolute value.

**Solution.** No. Take \(P=\xi^2\) and \(Q=i\), which is weaker. Then
\((Q(D)u,u)=i\|u\|_2^2\), a purely imaginary number. Its absolute value is \(\|u\|_2^2\), bounded by (10). Positivity is required for the controlling symbol \(P\); the weaker symbol can be complex. Removing the absolute value would not give an ordered real inequality in this example.

## References

- [Grubb] Gerd Grubb, *Fourier transformation*, open chapter of the lecture notes for *Distributions and Operators*, Theorem 5.5. [Author's PDF](https://web.math.ku.dk/~grubb/dist5.pdf).
- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, Section 9, Lemma 9.2. [Open Fourier chapter](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/fa60b20e070ee676b70cdf8a373e6197_section9.pdf).
