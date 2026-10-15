# An order trial with prescribed probability

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In [A transform with a piecewise-linear phase](a-transform-with-a-piecewise-linear-phase.md), order sampling with the transform returns the bin of a fraction \(j/r\) with probability \(\sum_tP(r,j,t)\), an exactly computable but inconvenient function of the bin. This lesson adds classical random choices to the experiment so that, at the true order \(r\), every reduced numerator contributes exactly the explicit amount \(\lambda(r)=2^{-\lceil\log_2r\rceil-10}\), and it does so without knowing \(r\) [OpenAI-EQF, Section 3]. The construction sums each residue class exactly, compares the result with an integral that is a polynomial of bounded degree on a bounded number of pieces, rounds that polynomial upward so that its total over all residues is computable, and spends the remaining mass on two classical correction modes. Mosca and Zalka computed a success probability to arbitrary precision with power sums and then prepared one qubit by a rotation through a computed angle, which brings the success probability to exactly \(\frac14\) [Mosca–Zalka 2004, Sections 4.1–4.2]. Here the polynomial pieces give exact dyadic sums, and no gate with a computed angle is needed.

- Estimates for the interpolated exponential (Section 1).
- A dyadic majorant with an exactly computable sum (Section 2).
- Three modes with a prescribed mass (Section 3).

We keep the notation of the previous lesson: \(n\ge128\), \(B=2^n\), \(Q=B^{16}\), the function \(g\), the bins \(k(d,j)\) with \(\eta=k(d,j)-jQ/d\), and the quantities \(P(d,j,t)\) of (5.1) there. Logarithms without a base are natural.

## 1. Estimates for the interpolated exponential

**Lemma 1.1.** Let \(f\colon[a,b]\to\mathbb C\) be twice continuously differentiable with \(|f''|\le M\), and let \(L\) be the affine function with \(L(a)=f(a)\), \(L(b)=f(b)\). Then \(|L(z)-f(z)|\le\frac M8(b-a)^2\) on \([a,b]\).

*Proof.* Fix \(z\) and put \(\lambda=(b-z)/(b-a)\). Integration by parts gives \(f(a)=f(z)+f'(z)(a-z)+R_a\) with \(R_a=\int_z^a(a-v)f''(v)\,dv\), so \(|R_a|\le\frac M2(z-a)^2\), and in the same way \(f(b)=f(z)+f'(z)(b-z)+R_b\) with \(|R_b|\le\frac M2(b-z)^2\). Since \(\lambda(a-z)+(1-\lambda)(b-z)=0\),
\[
L(z)-f(z)=\lambda R_a+(1-\lambda)R_b ,
\]
whose modulus is at most
\[
\begin{aligned}&\frac M2\bigl(\lambda(z-a)^2+(1-\lambda)(b-z)^2\bigr)\\&\quad=\frac M2(z-a)(b-z)\\&\quad\le\frac M8(b-a)^2 .\qquad\square\end{aligned}
\]

**Lemma 1.2.** The function \(g\) satisfies \(|g(z)-g(z')|\le4\sqrt2\,|z-z'|\) and \(|g(z)-e^{-2\pi iz}|\le\pi^2/32\) for all real \(z,z'\).

*Proof.* On each quarter interval \(g\) is affine with derivative \(4\bigl((-i)^{q+1}-(-i)^q\bigr)\), of modulus \(4|{-i}-1|=4\sqrt2\). For the second bound apply Lemma 1.1 to \(f(z)=e^{-2\pi iz}\) on intervals of length \(\frac14\), with \(M=4\pi^2\). \(\square\)

Fix a reduced label \((d,j)\) and \(0\le t<d\), and write \(k=k(d,j)\). For \(x\equiv t\pmod d\) put \(u=jt\bmod d\in\{0,\ldots,d-1\}\). Since \(jx\equiv jt\pmod d\), periodicity gives
\[
\begin{aligned}&g(kx/Q)\\&\quad=g\bigl(u/d+\eta x/Q\bigr).\end{aligned}\tag{1.1}
\]
For \(0\le u<d\) define
\[
\begin{aligned}I(u)&=\frac1d\int_0^1g(u/d+\eta v)\,dv,\\ J(u)&=|I(u)|^2 .\end{aligned}
\]

**Lemma 1.3** ([OpenAI-EQF, Lemma 3.4]). For \(1\le d<B\):

1. \(P(d,j,t)\) is a dyadic rational, computable from \((d,j,t)\) in time polynomial in \(n\);
2. \(|P(d,j,t)-J(jt\bmod d)|\le32/Q\);
3. \(\frac1{8d}\le|I(u)|\le\frac1d\) for \(0\le u<d\).

*Proof.* (1) As \(x\) runs through the progression \(t,t+d,\ldots\) below \(Q\), the argument \(u/d+\eta x/Q\) in (1.1) moves monotonically over a distance less than \(\frac12\), since \(|\eta|\le\frac12\). So it meets at most two quarter-integers, and comparisons of rationals with integer division split the progression into at most three runs on which \(g\) is affine. On each run the real and imaginary parts of \(g\) are affine in the index of the progression, so their sums follow from the number of terms and the sum of consecutive integers. This uses a bounded number of operations on rationals of \(O(n)\) bits. Every value \(g(kx/Q)\) has real and imaginary parts in \((4/Q)\mathbb Z\), because \(4kx/Q\in(4/Q)\mathbb Z\) and \(g\) is affine with coefficients in \(\mathbb Z[i]\) on each quarter interval in the variable \(4z\). Hence the sum divided by \(Q\) has denominators dividing \(Q^2\), and \(P(d,j,t)\) has a denominator dividing \(Q^4\).

(2) Put \(h=d/Q<1\) and \(f(v)=g(u/d+\eta v)\), a function with \(|f|\le1\) and, by Lemma 1.2, Lipschitz constant at most \(\frac12\cdot4\sqrt2<4\). Let \(A_t=Q^{-1}\sum_{x\equiv t}g(kx/Q)\). The points \(x/Q\) of the progression are the left endpoints of consecutive intervals of length \(h\), which start at \(t/Q<h\) and end at a point of \([1,1+h)\). On each interval the left-endpoint value differs from the average of \(f\) by at most \(2h\), so the Riemann sum \(h\sum_xf(x/Q)\) differs from the integral of \(f\) over the union of the intervals by at most \(2h(1+h)\). That integral differs from \(\int_0^1f\) by at most \(2h\), the length of the two end pieces. Dividing by \(d\), and using \(h\sum_xf(x/Q)=dA_t\),
\[
|A_t-I(u)|\le\frac{2h(1+h)+2h}d\le\frac6Q .
\]
The progression has at most \(Q/d+1\) terms, so \(|A_t|\le\frac1d+\frac1Q\), and \(|I(u)|\le\frac1d\). Hence
\[
\begin{aligned}&|P(d,j,t)-J(u)|\\&\quad\le|A_t-I(u)|\,\bigl(|A_t|+|I(u)|\bigr)\\&\quad\le\frac6Q\cdot3\le\frac{32}Q .\end{aligned}
\]

(3) The upper bound follows from \(|g|\le1\). Replacing \(g\) by \(e^{-2\pi iz}\) in the definition of \(I(u)\) gives an integral of modulus
\[
\frac1d\Bigl|\frac{\sin(\pi\eta)}{\pi\eta}\Bigr|\ge\frac2{\pi d},
\]
since \(\sin s/s\ge2/\pi\) for \(0<s\le\pi/2\) by concavity of the sine (the quotient is one at \(\eta=0\)). By Lemma 1.2 the replacement changes the integrand by at most \(\pi^2/32\), so \(|I(u)|\ge\frac1d(2/\pi-\pi^2/32)\). From \(\tan(\pi/6)>\pi/6\) we get \(\pi<2\sqrt3\), so \(2/\pi>1/\sqrt3>0.577\) and \(\pi^2/32<12/32=0.375\); the parenthesis exceeds \(\frac18\). \(\square\)

## 2. A dyadic majorant with an exactly computable sum

**Lemma 2.1** (the majorant; [OpenAI-EQF, Lemma 3.4]). For every \(1\le d<B\) and \(0\le j<d\) with \(\gcd(j,d)=1\), there are nonnegative dyadic rationals \(U(d,j,u)\), \(0\le u<d\), with
\[
\begin{aligned}&U(d,j,jt\bmod d)\\&\quad-P(d,j,t)\in[0,128/Q]\end{aligned}\tag{2.1}
\]
for \(0\le t<d\), and
\[
\begin{gathered}S(d,j):=\frac12\sum_{u=0}^{d-1}U(d,j,u),\\ \frac1{128d}\le S(d,j)\le2 .\end{gathered}\tag{2.2}
\]
Given their integer arguments, \(U(d,j,u)\) and \(S(d,j)\) are computable in time polynomial in \(n\), as dyadic rationals of polynomial bit length; computing \(S(d,j)\) does not enumerate its \(d\) terms.

*Proof.* *A piecewise polynomial.* Let \(G\) be the primitive of \(g\) with \(G(0)=0\); on each quarter interval its real and imaginary parts are polynomials of degree at most two with rational coefficients. If \(\eta\ne0\),
\[
I(u)=\frac{G(u/d+\eta)-G(u/d)}{d\eta} .
\]
The two arguments lie in \([-\frac12,\frac32]\), so as \(u\) runs through \([0,d)\) they cross the quarter-integers at boundedly many points, namely where \(u/d\) or \(u/d+\eta\) is a quarter-integer. Between these points \(I\) is a complex polynomial in \(u\) of degree at most two, and \(J=|I|^2\) is a rational polynomial of degree at most four. If \(\eta=0\), then \(I(u)=g(u/d)/d\) and the same holds. The boundaries and coefficients have \(O(n)\) bits: \(\eta=(kd-jQ)/d\), so a nonzero \(\eta\) has \(|\eta|\ge1/d\).

*Rounding upward.* On each piece write \(J(u)=\sum_{q=0}^4a_qu^q\), put \(D=QB^8\) and \(\tilde a_q=\lceil Da_q\rceil/D\), assign each boundary point to one of its two pieces, and let \(\tilde J\) be the resulting piecewise polynomial. Define
\[
\begin{gathered}U(d,j,u)=\tilde J(u)+\frac{64}Q\\ (u=0,\ldots,d-1).\end{gathered}
\]
As \(u\ge0\), rounding every coefficient upward increases the value, also when a coefficient is negative, and
\[
\begin{aligned}0&\le\tilde J(u)-J(u)\\&\le\frac{1+u+u^2+u^3+u^4}{QB^8}\le\frac1Q .\end{aligned}
\]
With Lemma 1.3(2), \(U(d,j,jt\bmod d)-P(d,j,t)\) lies between \(32/Q\) and \(97/Q\), which proves (2.1); in particular \(U\ge0\). By Lemma 1.3(3), \(J\ge1/(64d^2)\), so \(S(d,j)\ge\frac12\cdot d\cdot\frac1{64d^2}\), and
\[
\begin{aligned}S(d,j)&\le\frac12\Bigl(d\cdot\frac1{d^2}+\frac{65d}Q\Bigr)\\&\le\frac1{2d}+\frac{65d}{2Q}\le2,\end{aligned}
\]
using \(d<B\) and \(Q=B^{16}\).

*Computing the sum.* Intersect the boundedly many pieces with the integers \(0,\ldots,d-1\), using floors and ceilings, and sum each polynomial with the power sums \(\sum_{u=0}^{M-1}u^q\), \(q\le4\). These follow from the identities
\[
\begin{gathered}M^{q+1}=\sum_{\ell=0}^q\binom{q+1}\ell\sum_{u=0}^{M-1}u^\ell\\ (0\le q\le4),\end{gathered}
\]
obtained by summing \((u+1)^{q+1}-u^{q+1}\) over \(u<M\). Since \(D\) is a power of two, \(U\) and \(S\) are dyadic with \(O(n)\)-bit representations, and all the operations are rational arithmetic, integer division and rounding. \(\square\)

## 3. Three modes with a prescribed mass

For \(d\ge1\) put
\[
\lambda(d)=2^{-\lceil\log_2d\rceil-10},
\]
and write \(\varphi(d)\) for the number of \(0\le j<d\) with \(\gcd(j,d)=1\), so \(\varphi(1)=1\).

**Proposition 3.1** (the order trial; [OpenAI-EQF, Proposition 3.1]). Let \(2\le m<B\) and let \(a\) be a unit modulo \(m\) of order \(r\). There is a uniform quantum trial over the gate set \(\mathcal G\), of worst-case cost polynomial in \(n\), that returns either no candidate or an integer \(d\) with \(1\le d<B\) and \(r\mid d\), and
\[
\Pr(d=r)=\varphi(r)\,\lambda(r).
\]
The trial does not use \(r\) or any factorization.

*Proof.* *Coefficients.* For a reduced label \((d,j)\) the natural coefficient \(\lambda(d)/S(d,j)\) need not be dyadic; round it down and keep the remainder:
\[
\begin{gathered}
c(d,j)=2^{-10n}\Bigl\lfloor2^{10n}\frac{\lambda(d)}{S(d,j)}\Bigr\rfloor,\\
\rho(d,j)=\lambda(d)-c(d,j)\,S(d,j).
\end{gathered}
\]
Since \(\lambda(d)\le2^{-10}/d\) and \(S(d,j)\ge1/(128d)\), we have \(\lambda(d)/S(d,j)\le\frac18\), and therefore
\[
\begin{gathered}0\le c(d,j)\le\frac18,\\ 0\le\rho(d,j)\le2\cdot2^{-10n},\end{gathered}\tag{3.1}
\]
the second because \(\rho=S\,(\lambda/S-c)\) with \(S\le2\) and \(0\le\lambda/S-c<2^{-10n}\). Both are dyadic rationals of polynomial bit length, computed exactly by Lemma 2.1.

*The trial.* With two fair coins choose one of three modes, with probabilities \(\frac12,\frac14,\frac14\). In every mode, produce no candidate unless the label \((d,j)\) at hand satisfies
\[
\begin{gathered}1\le d<B,\quad 0\le j<d,\\ \gcd(j,d)=1,\quad a^d\equiv1\pmod m ,\end{gathered}
\]
and check these conditions before evaluating any formula involving the label.

1. Run the order sampling of Section 5 of [A transform with a piecewise-linear phase](a-transform-with-a-piecewise-linear-phase.md). Require success of its phase register, recover the label \((d,j)\) from the output \(k\) by Lemma 4.2 there, and retain the candidate \(d\) with probability \(c(d,j)\).
2. Choose independent uniform \(n\)-bit integers \(d,j,t\). Require also \(t<d\), and retain \(d\) with probability
\[
\begin{aligned}&2B^3c(d,j)\,\bigl(U(d,j,jt\bmod d)\\&\qquad-P(d,j,t)\bigr).\end{aligned}
\]
3. Choose independent uniform \(n\)-bit integers \(d,j\), and retain \(d\) with probability \(4B^2\rho(d,j)\).

The retention probabilities are dyadic and lie in \([0,1]\): they are nonnegative by (2.1) and (3.1), and the last two are at most \(2B^3\cdot\frac{128}Q\le256B^{-13}\le1\) and \(4B^2\cdot2\cdot2^{-10n}=8B^{-8}\le1\). Each is implemented exactly by Lemma 3.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), and the whole trial is a polynomial-size circuit over \(\mathcal G\) by Lemma 3.2 there.

*The mass at the true order.* Fix \(d=r\) and a numerator \(j\) with \(\gcd(j,r)=1\). By Proposition 5.1 of the previous lesson, Mode 1 contributes \(\frac{c(r,j)}2\sum_{t<r}P(r,j,t)\). In Mode 2 each triple has probability \(B^{-3}\), so it contributes
\[
\begin{aligned}&\frac{c(r,j)}2\sum_{t=0}^{r-1}\bigl(U(r,j,jt\bmod r)\\&\qquad-P(r,j,t)\bigr).\end{aligned}
\]
Multiplication by \(j\) permutes the residues modulo \(r\), so these two contributions add up to \(\frac{c(r,j)}2\sum_uU(r,j,u)=c(r,j)S(r,j)\). Mode 3 contributes \(\frac14\cdot B^{-2}\cdot4B^2\rho(r,j)=\rho(r,j)\). The total for the label \((r,j)\) is exactly \(\lambda(r)\).

Different labels give disjoint events: in Mode 1 because the bins of different reduced labels are different (Lemma 4.2 of the previous lesson), and in the other modes because the labels are sampled. There are \(\varphi(r)\) reduced numerators \(j\), including \(j=0\) for \(r=1\). Hence \(\Pr(d=r)=\varphi(r)\lambda(r)\). Finally, every returned candidate has \(a^d\equiv1\pmod m\); writing \(d=qr+s\) with \(0\le s<r\) gives \(a^s\equiv1\), so \(s=0\) by the minimality of \(r\), and \(r\mid d\). No identity between \(P(d,j,t)\) and a probability is used at labels with \(d\ne r\). \(\square\)

## 4. Exercises

**4.1.** Compute \(\lambda(5)\) and \(\Pr(d=5)\) when the order is \(r=5\).

**4.2.** Prove that \(\sin s/s\ge2/\pi\) for \(0<s\le\pi/2\).

**4.3.** Show that \(t\mapsto jt\bmod d\) is a bijection of \(\{0,\ldots,d-1\}\) when \(\gcd(j,d)=1\).

**4.4.** Use the identity for power sums to compute \(\sum_{u=0}^{M-1}u\) and \(\sum_{u=0}^{M-1}u^2\).

**4.5.** Why does the trial need Mode 3 at all? Show that without it the mass of the label \((r,j)\) would be \(c(r,j)S(r,j)\), which may differ from \(\lambda(r)\).

## 5. Solutions

**4.1.** \(\lceil\log_25\rceil=3\), so \(\lambda(5)=2^{-13}\), and \(\Pr(d=5)=\varphi(5)\lambda(5)=4\cdot2^{-13}=2^{-11}\).

**4.2.** The sine is concave on \([0,\pi/2]\), so it lies above the chord from \((0,0)\) to \((\pi/2,1)\): \(\sin s\ge2s/\pi\).

**4.3.** If \(jt\equiv jt'\pmod d\), then \(d\mid j(t-t')\), and as \(\gcd(j,d)=1\), \(d\mid t-t'\), so \(t=t'\). An injective map of a finite set to itself is bijective.

**4.4.** With \(q=1\): \(M^2=\sum_u1+2\sum_uu=M+2\sum_uu\), so \(\sum_{u<M}u=M(M-1)/2\). With \(q=2\): \(M^3=M+3\sum_uu+3\sum_uu^2\), so \(\sum_{u<M}u^2=(M-1)M(2M-1)/6\).

**4.5.** Modes 1 and 2 give \(c(r,j)S(r,j)\), and the rounding in the definition of \(c\) makes this smaller than \(\lambda(r)\) by \(\rho(r,j)\) whenever \(2^{10n}\lambda(r)/S(r,j)\) is not an integer. Mode 3 supplies exactly this remainder, by a classical guess of the label.

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [Mosca–Zalka 2004] M. Mosca, C. Zalka, *Exact quantum Fourier transforms and discrete logarithm algorithms*, Int. J. Quantum Inf. 2 (2004), no. 1, 91–100. https://arxiv.org/abs/quant-ph/0301093
