# Angular modes and powers of Gauss sums

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A primary prime \(\pi\) has an angle, the argument of \(\pi/|\pi|\), and its Gauss sum has an angle, the argument of \(G(\pi)\). By Theorem 3.3 of the first lesson, three times the second angle is the first angle plus \(\pi\). The first moment of the course concerns only the trivial Fourier mode in the angle of \(\pi\). This lesson shows that every fixed nontrivial mode cancels at the scale \(X^{5/6}/\log X\). Combined with the cube identity, this settles the moments of all fixed powers \(G(\pi)^k\) with \(3\nmid k\): Patterson's complementary conjecture for these powers.

All the analytic work has been done for a fixed angular order \(\ell\) in the previous lessons. What remains is the behavior of the angular model and the algebra of the powers.

**Prerequisites.** The lessons [*Cubic Gauss sums and Patterson's conjecture*](cubic-gauss-sums-and-pattersons-conjecture.md) (Theorems 3.3 and 4.1, Proposition 4.3), [*Large sieves for cubic characters*](large-sieves-for-cubic-characters.md) (Lemma 6.1, Theorem 6.4) and [*Bilinear sums and the sharp cutoff*](bilinear-sums-and-the-sharp-cutoff.md) (Theorem 6.1).

## 1. Fixed angular modes

Recall \(\theta_\ell(z)=(z/|z|)^\ell\). On primary elements \(\theta_\ell\) is the angular Hecke character \(\Theta_\ell\) of Lemma 6.1 of the lesson on large sieves. It has angular order \(\ell\) and conductor dividing \((3)\), and it is nonprincipal for \(\ell\ne0\).

**Theorem 1.1 (comparison in each fixed angular mode).** For every fixed integer \(\ell\),
\[
\begin{aligned}
&\sum_{N(\pi)\le X}\theta_\ell(\pi)\Bigl(G(\pi)-\frac{c_*}{N(\pi)^{1/6}}\Bigr)\\
&\qquad=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr).\quad(1.1)
\end{aligned}
\]

**Proof.** Theorem 6.1 of the previous lesson gives the dyadic form for the fixed \(\ell\). Summing over the dyadic ranges above \(X^{1/2}\), as in the proof of Theorem 4.1 of the first lesson, and bounding the primes below \(X^{1/2}\) trivially, gives (1.1). \(\square\)

The proof of Theorem 6.1 used the following ingredients for the fixed \(\ell\):

- the Type I estimates of the lesson on the level formula, which were proved for every fixed \(\ell\) from the level Voronoi formula with angular factors;
- the exceptional character moments for angular prime convolutions;
- the dispersion estimates, in which the angular factor is part of the coefficients;
- the decomposition, whose identities are scalar and whose condition (SW) holds for the twisted sequences (Lemma 6.1 of the lesson on the decomposition).

The argument makes no claim that is uniform in a growing \(\ell\): all constants, and the choices of the logarithmic parameters, may depend on \(\ell\).

**Proposition 1.2 (the angular model cancels).** For every fixed integer \(\ell\ne0\) and every \(M>0\),
\[
\begin{gathered}
P_\ell(y)=\sum_{N(\pi)\le y}\theta_\ell(\pi)\ll_{\ell,M}\frac y{(\log y)^M},\\
\sum_{N(\pi)\le X}\frac{\theta_\ell(\pi)}{N(\pi)^{1/6}}=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\end{gathered}
\]

**Proof.** Theorem 6.4 of the lesson on large sieves, applied to the primitive character inducing \(\Theta_\ell\), whose conductor divides \((3)\), gives
\[
\sum_{N(\mathfrak p)\le y}\Theta_\ell(\mathfrak p)\log N(\mathfrak p)\ll y(\log y)^{-M-1}.
\]
The prime above \(3\) has value \(0\) or changes the sum by \(O(1)\). Partial summation removes the logarithm and gives the bound for \(P_\ell\). By partial summation again,
\[
\begin{aligned}
&\sum_{N(\pi)\le X}\frac{\theta_\ell(\pi)}{N(\pi)^{1/6}}\\
&=\frac{P_\ell(X)}{X^{1/6}}+\frac16\int_2^X\frac{P_\ell(y)}{y^{7/6}}\,dy\\
&\quad+O(1),
\end{aligned}
\]
which is \(O(X^{5/6}(\log X)^{-M})\). \(\square\)

**Corollary 1.3.** For every fixed integer \(\ell\ne0\),
\[
\sum_{N(\pi)\le X}\Bigl(\frac\pi{|\pi|}\Bigr)^\ell G(\pi)=o_\ell\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\]

**Proof.** Combine (1.1) with Proposition 1.2. \(\square\)

So the secondary term \(\frac65c_*X^{5/6}/\log X\) lives entirely in the trivial angular mode. A split rational prime \(p=\pi\bar\pi\) contributes \(2\operatorname{Re}(\theta_\ell(\pi)G(\pi))\) to the sum in Corollary 1.3, since \(\theta_\ell(\bar\pi)G(\bar\pi)\) is the conjugate of \(\theta_\ell(\pi)G(\pi)\). For \(\ell\ne0\) this is not a function of the Kummer sum \(S_p\) alone, and no statement about the rational sums \(S_p\) beyond Corollary 4.4 of the first lesson is drawn from it.

## 2. Powers of the Gauss sums

By Theorem 3.3 of the first lesson, \(G(\pi)^3=-\theta_1(\pi)\) and \(|G(\pi)|=1\). Hence for every integer \(m\),
\[
\begin{gathered}
G(\pi)^{3m+1}=(-1)^m\theta_m(\pi)\,G(\pi),\\
G(\pi)^{3m-1}=(-1)^m\overline{\theta_{-m}(\pi)G(\pi)}.\quad(2.1)
\end{gathered}
\]
For the second identity use \(G(\pi)^{-1}=\overline{G(\pi)}\) and \(\theta_m=\overline{\theta_{-m}}\) on the unit circle.

**Corollary 2.1 (fixed powers).** For every fixed integer \(k\) with \(3\nmid k\),
\[
\begin{aligned}
&\sum_{N(\pi)\le X}G(\pi)^k\\
&=\mathbf 1_{k\in\{1,-1\}}\,\frac65\,c_*\,\frac{X^{5/6}}{\log X}\\
&\quad+o_k\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
\end{aligned}
\]

**Proof.** Write \(k=3m+1\) or \(k=3m-1\). If \(m\ne0\), the identities (2.1) and Corollary 1.3, with \(\ell=m\) or \(\ell=-m\) and complex conjugation, give \(o(X^{5/6}/\log X)\). If \(m=0\), then \(k=1\) is Theorem 4.1 of the first lesson, and \(k=-1\) is its complex conjugate, since \(G(\pi)^{-1}=\overline{G(\pi)}\); the main term is real. \(\square\)

Patterson conjectured that \(\sum_{N(\pi)\le X}G(\pi)^k=o(X^{5/6}/\log X)\) for every fixed \(k\notin\{0,1,-1\}\). Corollary 2.1 proves the cases \(3\nmid k\). For a nonzero multiple \(k=3m\), the cube identity gives \(G(\pi)^k=(-1)^m\theta_m(\pi)\). The conjecture then becomes the bound \(\sum_{N(\pi)\le X}\theta_m(\pi)=o(X^{5/6}/\log X)\) for the angles of the primes themselves. Theorem 6.4 of the lesson on large sieves gives only a saving of a power of \(\log X\) in that sum. A saving of a power of \(X\) would require a region free of zeros of the Hecke \(L\)-function of \(\Theta_m\) of fixed width, which is not known. These cases remain open.

## 3. Exercises

**3.1.** Verify the identities (2.1).

**3.2.** Deduce from Corollary 2.1 that \(\sum_{N(\pi)\le X}G(\pi)^2=o(X^{5/6}/\log X)\), and express the sum through the angular sums of Corollary 1.3.

**3.3.** For \(\pi=1+3\omega\), use the value of \(G(\pi)\) from Exercise 6.3 of the first lesson to check \(G(\pi)^3=-\theta_1(\pi)\) numerically.

**3.4.** Show that Theorem 1.1, for each fixed \(\ell\), does not by itself imply that
\[
\begin{aligned}
&\sum_{N(\pi)\le X}f\Bigl(\frac\pi{|\pi|}\Bigr)\\
&\quad\cdot\Bigl(G(\pi)-\frac{c_*}{N(\pi)^{1/6}}\Bigr)=o_f\Bigl(\frac{X^{5/6}}{\log X}\Bigr)
\end{aligned}
\]
for every continuous function \(f\) on the unit circle. What additional information about the dependence on \(\ell\) would suffice?

**3.5.** Show that for \(k=3m\) with \(m\ne0\), the sum \(\sum_{N(\pi)\le X}G(\pi)^k\) is \(o(X/\log X)\), and explain why this is much weaker than the conjectured bound.

## 4. Solutions

**3.1.** \(G^{3m+1}=(G^3)^mG\)\(=(-\theta_1)^mG=(-1)^m\theta_mG\), since \(\theta_1^m=\theta_m\). Similarly \(G^{3m-1}=(G^3)^mG^{-1}=(-1)^m\theta_m\overline G\), and \(\theta_m\overline G=\overline{\overline{\theta_m}G}=\overline{\theta_{-m}G}\).

**3.2.** With \(k=2=3\cdot1-1\), (2.1) gives \(G(\pi)^2=-\overline{\theta_{-1}(\pi)G(\pi)}\). So the sum is the negative of the conjugate of \(\sum\theta_{-1}(\pi)G(\pi)\), which is \(o(X^{5/6}/\log X)\) by Corollary 1.3 with \(\ell=-1\).

**3.3.** From the first lesson, \(G(1+3\omega)\)\(=0.89595\ldots-0.44414\ldots i\)\(=e^{-0.46022\ldots i}\). Its cube is \(e^{-1.38067\ldots i}=0.18898\ldots-0.98198\ldots i\). On the other hand \(\theta_1(\pi)=(1+3\omega)/\sqrt7\)\(=(-\frac12+\frac{3\sqrt3}2i)/\sqrt7\)\(=-0.18898\ldots+0.98198\ldots i\), so \(-\theta_1(\pi)\) agrees.

**3.4.** Approximate \(f\) uniformly within \(\epsilon\) by a trigonometric polynomial \(\sum_{|\ell|\le N}c_\ell z^\ell\). Theorem 1.1 handles the polynomial, with \(N\) depending on \(\epsilon\). The approximation error is at most \(\epsilon\sum_{N(\pi)\le X}|G(\pi)-c_*N(\pi)^{-1/6}|\), and this sum is of size \(X/\log X\), far larger than \(X^{5/6}/\log X\). So the error cannot be absorbed. What would suffice is a version of (1.1) that is uniform in \(\ell\), with error \(\varepsilon(X)\,|\ell|^A\,X^{5/6}/\log X\) for a fixed \(A\) and some \(\varepsilon(X)\to0\), applied to a smooth \(f\) whose Fourier coefficients decay faster than every power of \(|\ell|\).

**3.5.** By the cube identity the sum is \((-1)^mP_m(X)\), and Proposition 1.2 gives \(O(X(\log X)^{-M})\) for every \(M\), in particular \(o(X/\log X)\). The conjecture asks for \(o(X^{5/6}/\log X)\), a saving of a power of \(X\) beyond the trivial bound, about the distribution of the angles of the primes in \(\mathbb Z[\omega]\). No such power saving is known.

## Sources

- [OpenAI-023] OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint, 25 September 2026, Appendix A (fixed angular twists, Theorem A.1, and the powers of the Gauss-sum values in Appendix A.6). https://github.com/openai/math/tree/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
- [DR] A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3 (2024), equation (1.9) (Patterson's complementary conjecture). https://arxiv.org/abs/2109.07463v3
