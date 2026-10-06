# The explicit formula with general test functions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol. Public domain (CC0).*

Prime powers and zeros are two ways of testing the same distribution. A smooth weight makes their relation easy to use. A weight with a jump does something more concrete: it counts all prime powers below a chosen point, with half of the last one when the point itself is a prime power. This lesson explains where that half comes from and derives the explicit formula, including its term at the infinite place.

We assume the analytic continuation and functional equation of the Riemann zeta function, its Hadamard product, and the Riemann–von Mangoldt estimate. Section 1 records the precise forms needed and their internal prerequisite lessons. The smooth counting distributions are treated in Weil's proof for curves and what is missing over the integers. We use that lesson's conventions when comparing constants, but derive the formula for weights with jumps here. Basic references are [Weil 1972], [Bombieri 2000], and [Connes–Consani 2021].

## 1. The analytic facts and the weights

We write

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \psi_\Gamma(z)=\Gamma'(z)/\Gamma(z).
\]

The subscript distinguishes the digamma function from the prime-counting function. The entire function \(\xi\) has order one, satisfies \(\xi(s)=\xi(1-s)\), and has zeros \(\rho=\beta+i\gamma_\rho\), counted with multiplicity, in \(0<\beta<1\). Its zeros are stable under conjugation and under \(\rho\mapsto1-\rho\). The following consequences of the Hadamard product and zero-counting estimate will be used:

\[
N(T+1)-N(T)=O(\log(T+2)),\quad
\sum_\rho(1+\lvert\rho\rvert)^{-2}<\infty,
\quad
\lim_{T\to\infty}\sum_{\lvert\gamma_\rho\rvert<T}\frac1\rho
=1+\frac\gamma2-\frac12\log(4\pi).
\tag{1.1}
\]

Here \(\gamma\) without a subscript is Euler's constant. There are heights \(T_j\in[j,j+1]\) for which

\[
\frac{\xi'}{\xi}(\sigma\pm iT_j)=O_\varepsilon(\log^2(T_j+2))
\quad(-\varepsilon\le\sigma\le1+\varepsilon).
\tag{1.2}
\]

Here are the exact internal proof dependencies. The programme's course *The Riemann zeta function* plans *The Gamma function and Stirling's formula* for the digamma product and asymptotic expansion; *Poisson summation, theta, and the functional equation* for continuation, the completed functional equation and \(\xi(0)=\xi(1)=1/2\); *Entire functions of order one and the Hadamard product of ξ* for the logarithmic derivative, zero summability and the last constant in (1.1); and *The Riemann–von Mangoldt formula* for the zero count and its bound in unit intervals. These are genuine planned prerequisite lessons, rather than proofs supplied in this lesson; their public versions are not yet linked here. Bibliographic credit for these facts is retained in [Bombieri 2000, Sections I–II].

The bound (1.2) itself follows from those statements. From the symmetric Hadamard derivative subtract its value at \(2+it\). The result is the absolutely convergent sum

\[
\sum_\rho\left(\frac1{\sigma+it-\rho}-\frac1{2+it-\rho}\right).
\]

Terms with \(\lvert t-\gamma_\rho\rvert>1\) are bounded by a constant times \((t-\gamma_\rho)^{-2}\); summing in unit intervals and using (1.1) gives \(O(\log(t+2))\). Also \(\xi'(2+it)/\xi(2+it)=O(\log(t+2))\), by its gamma factor and absolutely convergent Euler product. Remove intervals of radius \(c_0/\log(j+2)\) about the \(O(\log(j+2))\) ordinates in \([j-1,j+2]\), choosing \(c_0\) small enough that their total length is less than one. A remaining \(T_j\in[j,j+1]\) has distance at least that radius from every nearby ordinate. Each of the \(O(\log T_j)\) local fractions is then \(O(\log T_j)\), proving (1.2). The lower height follows by conjugation. None of these facts assumes RH.

The Mellin transform and reflection in this lesson are

\[
\widetilde f(s)=\int_0^\infty f(x)x^s\frac{dx}{x},
\qquad f^\sharp(x)=x^{-1}f(x^{-1}).
\tag{1.3}
\]

Put \(F(u)=e^{u/2}f(e^u)\). Then

\[
\widetilde f(\tfrac12+it)=\int_{\mathbb R}F(u)e^{itu}\,du,
\qquad e^{u/2}f^\sharp(e^u)=F(-u).
\tag{1.4}
\]

Thus Mellin analysis on the positive half-line is Fourier analysis in logarithmic coordinates. With the Fourier convention \(\widehat F(t)=\int F(u)e^{-itu}du\), the transform in (1.4) is \(\widehat F(-t)\).

**Definition 1.1 (admissible jump weights).** We require \(F\) to be continuously differentiable away from finitely many points. At those points both \(F\) and \(F'\) have finite one-sided limits, and \(F\) takes the arithmetic mean of its limits. For some \(\delta>0\), on the intervals of differentiability,

\[
\lvert F(u)\rvert+\lvert F'(u)\rvert
\le C e^{-(1/2+\delta)\lvert u\rvert}.
\tag{1.5}
\]

In terms of \(f\), the tail condition is imposed on both \(f(x)\) and \(xf'(x)\): they are \(O(x^\delta)\) at zero and \(O(x^{-1-\delta})\) at infinity. It includes compactly supported, piecewise continuously differentiable weights and Gaussians in \(\log x\).

These are Weil's 1952 conditions on test functions, specialized to \(\mathbb Q\) and written in (1.4). [Bombieri 2000, Section V] describes a class \(W\) using the value bounds on \(f\), without a corresponding derivative bound. Value bounds alone do not imply the \(O(1/\lvert t\rvert)\) Mellin estimate used in a contour proof. We retain the explicit tail regularity (1.5). At the end we also give a cutoff interpretation for the broader value-bounded class; it must not be confused with an unqualified interchange of the two limiting operations.

**Lemma 1.2 (Mellin decay and inversion).** For a weight in Definition 1.1, \(\widetilde f\) is holomorphic on \(-\delta<\Re s<1+\delta\). On every closed substrip it is \(O((1+\lvert t\rvert)^{-1})\). For any real \(c\) in that strip,

\[
\lim_{T\to\infty}\frac1{2\pi i}\int_{c-iT}^{c+iT}
\widetilde f(s)x^{-s}\,ds=f(x).
\tag{1.6}
\]

**Proof.** The tail bounds dominate the defining integral and all its derivatives in \(s\) on a closed substrip. Set \(A_c(u)=e^{cu}f(e^u)\). Both its ordinary derivative on the smooth intervals and the finite jump masses are integrable. Its distributional derivative is a finite measure. Integration by parts gives

\[
it\widetilde f(c+it)=-\int e^{itu}\,dA_c(u).
\]

This proves the decay estimate. After interchanging the two integrals at finite \(T\), the left side of (1.6) is

\[
x^{-c}\int_{\mathbb R} A_c(u)
\frac{\sin(T(u-\log x))}{\pi(u-\log x)}\,du.
\]

Split the integral near \(u=\log x\) and its complement. On each side of that point subtract the corresponding one-sided value. The resulting quotient is bounded locally, while away from the point it is integrable; the Riemann–Lebesgue lemma makes these parts tend to zero. The two constant pieces each contribute half their value, since \(\int_0^\infty\sin v/v\,dv=\pi/2\). This yields the mean value. ∎

## 2. The formula and its local terms

Let \(\Lambda(n)=\log p\) when \(n=p^m\), with \(m\ge1\), and let it be zero otherwise. Define

\[
P(f)=\sum_{n\ge2}\Lambda(n)\bigl(f(n)+f^\sharp(n)\bigr),
\tag{2.1}
\]

\[
W_{\mathbb R}(f)=(\log(4\pi)+\gamma)f(1)
+\int_1^\infty
\frac{f(x)+f^\sharp(x)-2x^{-1}f(1)}{x-x^{-1}}\,dx.
\tag{2.2}
\]

The prime sum converges absolutely. Near \(x=1\), the numerator in (2.2) is \(O(x-1)\): the two one-sided limits add to \(2f(1)\), even if there is a jump. The integral therefore exists as an ordinary improper integral. This cancellation explains why the prescribed value at a jump matters at the infinite place as well as at the primes.

**Theorem 2.1 (the explicit formula).** For a weight in Definition 1.1,

\[
\boxed{\quad
\widetilde f(0)-\lim_{T\to\infty}
\sum_{\lvert\gamma_\rho\rvert<T}\widetilde f(\rho)
+\widetilde f(1)=P(f)+W_{\mathbb R}(f).
\quad}
\tag{2.3}
\]

The zero sum is a symmetric limit and is not asserted to converge absolutely.

*Reference:* the formula is due to Weil (1952); [Bombieri 2000, Section V] states it with the arithmetic normalization of (2.3).

Writing \(W_p(f)=\log p\sum_{m\ge1}(f(p^m)+f^\sharp(p^m))\) gives \(P(f)=\sum_pW_p(f)\). We use \(W_\infty=-W_{\mathbb R}\) when discussing positivity. Thus the right side of (2.3) is \(\sum_pW_p-W_\infty\); it is also the sum over places with the archimedean term denoted \(W_{\mathbb R}\). This sign dictionary will matter later.

**Corollary 2.2 (finite prime support).** If \(\operatorname{supp}f\subset[X^{-1},X]\), with \(X\ge1\), only prime powers \(n\le X\) occur in (2.1).

**Proof.** For \(n>X\), both \(n\) and \(1/n\) lie outside the support. ∎

This is a finite sum for each compactly supported weight. It does not replace the zeros by a finite set: a compactly supported weight has an entire Mellin transform, which is usually nonzero at infinitely many zeros.

## 3. Evaluating the infinite place

We first calculate (2.2) for a smooth compactly supported weight. This establishes the constants before introducing conditionally convergent contour integrals.

**Proposition 3.1 (spectral expression).** For \(f\in C_c^\infty(\mathbb R_+^*)\),

\[
W_{\mathbb R}(f)=\log\pi\,f(1)
-\frac1{2\pi}\int_{\mathbb R}
\Re\psi_\Gamma(\tfrac14+\tfrac{it}{2})
\widetilde f(\tfrac12+it)\,dt.
\tag{3.1}
\]

Equivalently the second term is the vertical-line integral with \(ds/(2\pi i)\). The symbol \(\Re\psi_\Gamma(s/2)\) in that notation is evaluated along \(\Re s=1/2\); it is not a holomorphic function of \(s\).

**Proof.** The digamma series gives, for \(a>0\),

\[
\Re\psi_\Gamma(a+iy)
=-\gamma+\int_0^\infty
\frac{e^{-v}-e^{-av}\cos(yv)}{1-e^{-v}}\,dv.
\tag{3.2}
\]

The integrand has a finite limit at zero, and decays at infinity. One can first cut the \(v\)-integral off at \(v=\eta\) and then use Fourier inversion. With \(F\) from (1.4) and \(a=1/4\), this yields

\[
\frac1{2\pi}\int\Re\psi_\Gamma(\tfrac14+\tfrac{it}{2})
\widetilde f(\tfrac12+it)\,dt
=-\gamma f(1)+\int_0^\infty
\frac{e^{-v}f(1)-\tfrac12e^{-v/4}(F(v/2)+F(-v/2))}{1-e^{-v}}\,dv.
\]

The interchange after the cutoff is absolute, and the difference in the numerator is \(O(v)\) at zero. Dominated convergence removes the cutoff. Put \(v=2u\), and use \(F(u)+F(-u)=e^{u/2}(f(e^u)+f^\sharp(e^u))\). Subtracting this integral from \(\log\pi f(1)\) gives

\[
(\log\pi+\gamma)f(1)
+\int_0^\infty
\frac{f(e^u)+f^\sharp(e^u)-2e^{-2u}f(1)}{1-e^{-2u}}\,du.
\tag{3.3}
\]

Replacing \(2e^{-2u}\) by \(2e^{-u}\) in the subtraction adds

\[
2f(1)\int_0^\infty\frac{e^{-u}-e^{-2u}}{1-e^{-2u}}du
=2f(1)\int_0^\infty\frac{e^{-u}}{1+e^{-u}}du
=2\log2\,f(1).
\]

Finally \(x=e^u\) turns (3.3) into (2.2). ∎

**Lemma 3.2 (symmetric spectral integrals with jumps).** Formula (3.1) extends to Definition 1.1 when the \(t\)-integral is truncated symmetrically and its limit is taken.

**Proof.** Only the even part of \(F\) contributes. Replace it by \(E(u)=(F(u)+F(-u))/2\); it is continuous at zero with value \(f(1)\) and has bounded derivative near zero on each side. Subtract \(f(1)\) times a smooth even function equal to one near zero. The remainder \(K\) is even, satisfies \(K(0)=0\), and has integrable derivative, including finitely many jump masses away from zero. Also \(K(u)=O(\lvert u\rvert)\) near zero.

The difference between \(\Re\psi_\Gamma(1/4+it/2)\) and \(\log(\lvert t\rvert/2)\) is in \(L^2(\mathbb R)\): its logarithmic singularity at zero is square integrable, and Stirling's estimate makes it \(O(t^{-2})\) at infinity. Plancherel handles that remainder, and ordinary inversion handles the constant \(-\log2\).

For the logarithmic part, integrate the Fourier transform of \(K\) by parts. Its evenness expresses the truncated integral through the kernel

\[
J_T(u)=\int_0^T\frac{\log t}{t}\sin(tu)\,dt.
\]

For \(u\ne0\), \(J_T(u)\) converges by Dirichlet's test at infinity and by integrability at zero. The change of variable \(v=t\lvert u\rvert\), followed by integration by parts on \([1,T\lvert u\rvert]\), gives uniformly in \(T\)

\[
\lvert J_T(u)\rvert\le C(1+\lvert\log\lvert u\rvert\rvert).
\]

The measure \(dK\) has no mass at zero. Its density is bounded there, its tails decay exponentially, and its other atoms are finitely many. The bound is integrable against \(\lvert dK\rvert\), so dominated convergence proves existence of the sharp spectral limit. It agrees with its exponentially regularized limit. Apply (3.2) with an exponential regularization, use the cancellation at \(u=0\), and then remove the regularization; the same calculation as in Proposition 3.1 gives (2.2). ∎

The distribution \(W_{\mathbb R}\) is therefore supported on the whole multiplicative group and is singular at \(1\). It is not integration against a locally integrable density at that point. Its subtraction term fixes a particular finite part, and changing that subtraction changes the displayed multiple of \(f(1)\).

## 4. The contour argument, including the jumps

**Proof of Theorem 2.1.** Choose \(0<\varepsilon<\min(\delta,1/2)\) and put \(c=1+\varepsilon\). Integrate \(\widetilde f(s)\xi'(s)/\xi(s)\) round the rectangle with sides \(\Re s=c,1-c\) and heights \(\pm T_j\) from (1.2). The residue theorem and the functional equation give

\[
\sum_{\lvert\gamma_\rho\rvert<T_j}\widetilde f(\rho)
=\frac1{2\pi i}\int_{c-iT_j}^{c+iT_j}
H(s)\frac{\xi'}{\xi}(s)\,ds+o(1),
\qquad H(s)=\widetilde f(s)+\widetilde f(1-s).
\tag{4.1}
\]

Indeed each horizontal side is \(O(\log^2T_j/T_j)\) by Lemma 1.2. On the right side,

\[
\frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\psi_\Gamma(s/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\tag{4.2}
\]

The rational terms may be moved to \(\Re s=1/2\); their horizontal integrals tend to zero, and the pole at \(1\) contributes \(H(1)=\widetilde f(1)+\widetilde f(0)\). The integral on the critical line is zero. To see this, pair \(s=1/2+it\) with \(1-s\): \(H\) is unchanged whereas \(1/s+1/(s-1)\) changes sign. Their product is absolutely integrable, since it is \(O(t^{-2})\).

The gamma and constant terms have no poles between these two lines. Their horizontal integrals again vanish. On the critical line the two pieces of \(H\) combine to give

\[
\lim_{T\to\infty}\frac1{2\pi}\int_{-T}^T
\bigl(\Re\psi_\Gamma(\tfrac14+\tfrac{it}{2})-\log\pi\bigr)
\widetilde f(\tfrac12+it)\,dt=-W_{\mathbb R}(f)
\]

by Lemma 3.2.

For the Dirichlet-series term, expanding at finite \(T\) is justified by absolute convergence on \(\Re s=c\). To pass to infinite height, consider

\[
B(u)=\sum_{n\ge2}\Lambda(n)n^{-c}
\bigl(A_c(u+\log n)+A_c^\sharp(u+\log n)\bigr),
\quad
A_c^\sharp(v)=e^{cv}f^\sharp(e^v).
\]

Near \(u=0\) the series and its derivatives on each smooth interval converge uniformly by (1.5). Only finitely many jump points of the summands can meet a fixed neighborhood of zero: a jump requires \(u+\log n\) to belong to the finite list of jump positions of \(f\) or \(f^\sharp\). Globally the sum is integrable by the same exponential tail bounds and \(\sum\Lambda(n)n^{-c}<\infty\). It follows that Fourier inversion at zero applies to \(B\). Its mean value there is

\[
B(0)=\sum_{n\ge2}\Lambda(n)(f(n)+f^\sharp(n))=P(f).
\]

Thus the final term of (4.2), with its minus sign, contributes \(-P(f)\). Combining all three contributions in (4.1) proves (2.3) along the heights \(T_j\).

For an arbitrary height \(T\), compare with a good height within distance at most two. The number of intervening zeros is \(O(\log(T+2))\), and each transform has size \(O(1/T)\). Their total is \(O(\log T/T)\), which tends to zero. This proves the asserted symmetric limit for all heights. ∎

The proof identifies exactly where jumps enter: Fourier inversion evaluates the mean value of a weight at each prime power. A different value assigned at a jump would change the arithmetic side but would not change its Mellin transform.

![A weight equal to one between x equals one and two has value one-half at each jump. Three symmetric Gaussian smoothings approach the same half values.](../figures/jump-mean.png)

*Figure 1.* An illustrative interval weight and its symmetric smoothings. The smoothing shown is additive, to make the endpoint mechanism visible; Mellin inversion uses the identical mean-value mechanism after passing to logarithmic coordinates. Open circles denote the one-sided limits, and filled circles denote the assigned values. Lemma 1.2 explains the half contribution in (5.2).

## 5. Counting and Gaussian weights

### 5.1 A sharp endpoint

For \(X>1\) let \(f_X\) be one on \((1,X)\), zero outside \([1,X]\), and one-half at each endpoint. Then

\[
\widetilde f_X(s)=\frac{X^s-1}{s},\quad
\widetilde f_X(0)=\log X,\quad
\widetilde f_X(1)=X-1,
\]

and \(P(f_X)=\psi_0(X)\), where

\[
\psi_0(X)=\sum_{n<X}\Lambda(n)+\tfrac12\Lambda(X)
\]

and \(\Lambda(X)=0\) if \(X\) is not an integer prime power. The reflected part of the prime sum is zero. The archimedean integral splits at \(X\):

\[
\int_1^X\frac{1-x^{-1}}{x-x^{-1}}dx
-\int_X^\infty\frac{x^{-1}}{x-x^{-1}}dx
=-\log2+\frac12\log(X^2-1).
\]

Consequently

\[
W_{\mathbb R}(f_X)=\tfrac12(\log(4\pi)+\gamma)
-\log2+\tfrac12\log(X^2-1).
\tag{5.1}
\]

Substitute (5.1) into (2.3), and use (1.1). The terms \(\log X\) cancel because \(\tfrac12\log(X^2-1)=\log X+\tfrac12\log(1-X^{-2})\). The remaining constant is

\[
-1+\left(1+\tfrac\gamma2-\tfrac12\log(4\pi)\right)
-\tfrac12(\log(4\pi)+\gamma)+\log2=-\log(2\pi).
\]

We have proved

\[
\boxed{\psi_0(X)=X-\lim_{T\to\infty}
\sum_{\lvert\gamma_\rho\rvert<T}\frac{X^\rho}{\rho}
-\log(2\pi)-\tfrac12\log(1-X^{-2}).}
\tag{5.2}
\]

This is von Mangoldt's formula, with its endpoint convention explicitly built in.

### 5.2 A Gaussian in logarithmic coordinates

For \(a>0\), let \(f_a(x)=\exp(-(\log x)^2/(2a^2))\). Completing the square gives

\[
\widetilde f_a(s)=\sqrt{2\pi}\,a\,e^{a^2s^2/2}.
\tag{5.3}
\]

The pole contribution is \(\sqrt{2\pi}a(1+e^{a^2/2})\). The prime and archimedean contributions are

\[
P(f_a)=\sum_{n\ge2}\Lambda(n)(1+n^{-1})
e^{-(\log n)^2/(2a^2)},
\]

\[
W_{\mathbb R}(f_a)=\log(4\pi)+\gamma
+\int_0^\infty
\frac{(1+e^{-u})e^{-u^2/(2a^2)}-2e^{-u}}
{1-e^{-2u}}du.
\tag{5.4}
\]

The integrand in (5.4) tends to \(1/2\) at zero. At a zero \(\beta+it\), the magnitude in (5.3) is \(\sqrt{2\pi}a\exp(a^2(\beta^2-t^2)/2)\). Thus the zero sum is absolutely convergent in this example, without RH. Increasing \(a\) suppresses high zeros while involving more prime powers. Narrow logarithmic weights have the reverse effect.

Here is a numerical illustration. The second column uses the first ten numerically computed conjugate pairs of zeros; the third uses prime powers at most 100 and the complete integral (5.4). The entries are rounded, and no remainder certification is claimed.

| \(a\) | Pole terms minus ten zero pairs | Prime powers at most 100 plus \(W_{\mathbb R}\) |
| --- | --- | --- |
| 0.1 | 0.233972624 | 0.233972159 |
| 0.2 | 0.994843964 | 0.994843964 |
| 0.5 | 2.673505113 | 2.673505113 |
| 1.0 | 6.639359629 | 6.638597053 |

At \(a=0.1\), the visible discrepancy mostly comes from omitted zeros. At \(a=1\), the omitted prime powers are visible. Agreement at the intermediate widths illustrates the identity; it is not a proof of RH or a verification of all zeros.

### 5.3 Comparing two constants

Corollary 5.13 of Weil's proof for curves and what is missing over the integers writes the infinite-place term, for smooth weights, as

\[
(\log\pi+\gamma)f(1)
+\int_1^\infty
\frac{xf(x)+f(1/x)-2f(1)/x}{x^2-1}dx.
\tag{5.5}
\]

Our integral in (2.2) has \(-2f(1)\), rather than \(-2f(1)/x\), in that numerator. The difference of the integrals is

\[
-2f(1)\int_1^\infty\frac{1-1/x}{x^2-1}dx
=-2\log2\,f(1).
\]

The constant in (2.2) is larger by \(2\log2\,f(1)\). The two complete expressions therefore agree. Changing a finite-part convention without changing its constant would give a wrong formula.

## 6. Exercises and solutions

**Exercise 1 (easy).** Compute the Mellin transforms of \(f_X\) and \(f_a\). Explain why the values assigned at their finitely many endpoints do not affect a transform.

**Solution.** Integrating \(x^{s-1}\) on \((1,X)\) gives \((X^s-1)/s\), with removable value \(\log X\) at zero. For \(f_a\), use \(u=\log x\) and complete the square in \(-u^2/(2a^2)+su\). For real \(s\) the Gaussian integral gives (5.3); both sides are entire, so the identity theorem gives it for complex \(s\). Changing finitely many point values changes neither integral. It does change the prime evaluations, which is why Lemma 1.2 prescribes the mean.

**Exercise 2 (medium).** Recover (5.2) directly from (2.3), retaining every constant. What changes if \(X=p^m\) and one asks for \(\sum_{n\le X}\Lambda(n)\)?

**Solution.** The pole terms are \(\log X+X-1\), and the zero terms are \(\sum X^\rho/\rho-\sum1/\rho\). Insert (5.1) and (1.1); the displayed calculation in Section 5.1 reduces the constant to \(-\log(2\pi)\). To count the endpoint fully, add \(\tfrac12\log p\) to (5.2). The symmetric formula itself always gives the half count.

**Exercise 3 (medium).** Starting from the digamma series, prove that (2.2) and (3.1) agree for smooth compactly supported weights.

**Solution.** Integrate each term \(1/(n+a+iy)\) as \(\int_0^\infty e^{-(n+a+iy)v}dv\), and sum the geometric series; subtracting \(1/(n+1)\) gives (3.2). Apply Fourier inversion to the cosine factor, which produces \((F(v/2)+F(-v/2))/2\). The substitution \(v=2u\) gives (3.3). Its subtraction changes from \(2e^{-2u}\) to \(2e^{-u}\) at the expense of \(2\log2\,f(1)\), giving (2.2). Cutting at \(v=\eta\) before inversion and using the \(O(v)\) cancellation proves the interchanges, not just the algebra.

**Exercise 4 (medium).** Reconcile the constant in (5.5) with that in (2.2).

**Solution.** Write both integrals against \(dx/(x^2-1)\). Their numerators differ by \(-2(1-1/x)f(1)\). Since \((1-1/x)/(x^2-1)=1/(x(x+1))\), its integral from one to infinity is \(\log2\). The integral difference is \(-2\log2\,f(1)\), and the constant difference is \(+\log4\,f(1)\). They cancel.

**Exercise 5 (hard).** Extend the theorem to weights with locally infinitely many jumps, by imposing weighted bounded variation. Give sufficient conditions and justify both the zero sum and the infinite-place term.

**Solution.** Fix \(c_-<0<1<c_+\). Assume that \(A_c(u)=e^{cu}f(e^u)\) is integrable and of bounded variation for \(c=c_-,c_+\), and that the variations and integrals are finite also with a slightly larger exponential weight at each end. Impose mean values at jumps. Near every \(\log n\), assume the one-sided Dini condition for \(f(e^u)\); near zero impose one-sided Lipschitz bounds. Finally, for the even part \(E\) of \(F\), require

\[
\int_{0<\lvert u\rvert<1}\lvert\log\lvert u\rvert\rvert\,d\lvert E\rvert(u)<\infty.
\tag{6.1}
\]

These conditions hold in particular if \(F\) and its piecewise derivative have exponentially weighted bounded variation, with only finitely many jumps on each compact interval, and \(F\) has bounded one-sided derivatives near zero. Integrating against the derivative measures gives the \(O(1/t)\) estimate on every intermediate vertical line; Hölder's inequality for the weighted variation bounds supplies uniformity in \(c\). Mellin inversion now follows from the Dini condition, and Lemma 3.2 follows from (6.1) and its kernel bound. For the prime term use the sum of translated derivative measures defining \(B\): its total variation is at most the sum of their weighted variations, which is finite. A bounded-variation function has Fourier inversion to its mean values. The residue argument and the comparison of neighboring heights are then unchanged. This proves (2.3) under the stated conditions. Merely saying that \(f\) and \(f'\) have bounded variation locally, without controlling their tails, would not justify these interchanges.

## 7. The broader value-bounded class

Suppose only that \(f\) is piecewise continuously differentiable with finitely many jumps and has the value bounds \(O(x^\delta)\), \(O(x^{-1-\delta})\). Let \(\chi_R(u)\) be smooth, even, equal to one on \([-R,R]\), zero outside \([-R-1,R+1]\), and between zero and one. Set \(f_R(x)=\chi_R(\log x)f(x)\). Each \(f_R\) satisfies Definition 1.1. Absolute convergence on the arithmetic side and dominated convergence in (2.2) prove the following exact extension:

\[
\widetilde f(0)+\widetilde f(1)
-\lim_{R\to\infty}\lim_{T\to\infty}
\sum_{\lvert\gamma_\rho\rvert<T}\widetilde f_R(\rho)
=P(f)+W_{\mathbb R}(f).
\tag{7.1}
\]

The value of this iterated limit is independent of the cutoffs. Under (1.5), Theorem 2.1 supplies the single symmetric zero sum of \(\widetilde f\). Without a tail regularity condition, (7.1) is the justified statement here.

To see why the Mellin estimate needs more than value bounds, choose disjoint smooth bumps in \(u\) near integers \(m\), of amplitudes \(e^{-2m}\), and modulate the \(m\)-th bump by \(e^{-iT_m u}\). Taking \(T_m\) successively so large that the Fourier transforms of the earlier bumps are negligible at \(T_m\), and the later amplitudes summably smaller, makes \(\lvert\widetilde f(1/2+iT_m)\rvert\) comparable to its \(m\)-th amplitude. The \(T_m\) can grow faster than its reciprocal. Such a smooth value-bounded function has no \(O(1/T_m)\) estimate. A derivative bound prevents precisely this behavior.

## What this lesson does not prove

We use the exact internal prerequisite statements and planned proof-provider lessons recorded in Section 1. This course therefore does not claim that the whole programme's prerequisite proofs have already been published. The Hecke-character formula belongs to the next lesson. We do not assert that the two limits in (7.1) may be interchanged for every function in Bombieri's abbreviated value-bounded class.

## References

- **[Bombieri 2000]** E. Bombieri, *Problems of the Millennium: the Riemann Hypothesis*, Clay Mathematics Institute, Section V. [Official problem description](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
- **[Connes–Consani 2021]** A. Connes and C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Mathematica 27 (2021), article 77; Appendices “Explicit formula” and “Fourier versus Mellin transforms”. [Preprint](https://arxiv.org/abs/2006.13771).
- **[Weil 1972]** A. Weil, *Sur les formules explicites de la théorie des nombres*, Izv. Akad. Nauk SSSR Ser. Mat. 36 (1972), 3–18; no. 16 writes the explicit formula for Hecke and Artin–Hecke \(L\)-functions as a distribution on the Weil group, extending Weil's formula of 1952. [Full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=2289&what=fullt&option_lang=eng).
