# Irrationality exponents

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Every irrational number \(x\) has infinitely many rational approximations \(p/q\) with \(|x-p/q|<1/q^2\). The irrationality exponent \(\mu(x)\) measures how much better than this the best approximations can be: it is the supremum of the exponents \(\nu\) for which \(|x-p/q|<q^{-\nu}\) has infinitely many solutions. So \(\mu(x)\ge2\) always, and \(\mu(x)=2\) means that no exponent beyond two is possible infinitely often. This course proves the theorem of OpenAI (2026) [OpenAI-Pi] that \(\mu(\pi)=2\), and deduces the convergence of the Flint–Hills series \(\sum n^{-3}\sin^{-2}n\).

This lesson defines the exponent, proves the lower bound \(\mu\ge2\) and Liouville's upper bound for algebraic numbers, states the theorem for \(\pi\), and describes the structure of its proof, which occupies the rest of the course.

## 1. The irrationality exponent

**Definition 1.1.** For an irrational real number \(x\), its *irrationality exponent* is

\[
\mu(x)=\sup\Bigl\{\nu>0:\ 0<\Bigl|x-\frac pq\Bigr|<q^{-\nu}\ \text{for infinitely many coprime } p,q\in\mathbb Z,\ q\ge2\Bigr\}.
\]

The value may be \(+\infty\).

**Lemma 1.2** (equivalent formulations). For irrational \(x\) and real \(\nu>0\), the following are equivalent:

1. there is \(Q\) such that \(|x-p/q|\ge q^{-\nu}\) for all integers \(p\) and \(q\ge Q\);
2. only finitely many coprime pairs \((p,q)\), \(q\ge2\), satisfy \(|x-p/q|<q^{-\nu}\).

If these hold for every \(\nu>2\), then \(\mu(x)\le2\).

**Proof.** (1) implies (2) because a solution of (2) has \(q<Q\), and for each \(q\) only finitely many \(p\) are close to \(qx\). Conversely, assume (2), and let \(p/q\) be an arbitrary fraction with \(q\ge Q\) and \(|x-p/q|<q^{-\nu}\). Write \(p/q=p'/q'\) in lowest terms, \(q'\le q\). Then \(|x-p'/q'|<q^{-\nu}\le q'^{-\nu}\), so \((p',q')\) is one of the finitely many exceptions; there are finitely many values of \(|x-p'/q'|>0\), and for \(q\) large \(q^{-\nu}\) is smaller than all of them. So (1) holds for some \(Q\). \(\square\)

**Proposition 1.3** (Dirichlet). If \(x\) is irrational, there are infinitely many coprime \((p,q)\) with \(q\ge1\) and \(0<|x-p/q|<1/q^2\). Hence \(\mu(x)\ge2\).

**Proof.** Let \(N\ge1\). The \(N+1\) numbers \(\{jx\}\), \(0\le j\le N\), lie in \([0,1)\), which is the union of \(N\) intervals of length \(1/N\); two of them, \(\{jx\}\) and \(\{lx\}\) with \(j<l\), lie in one interval. With \(q=l-j\le N\) and a suitable integer \(p\), \(|qx-p|<1/N\le1/q\), so \(|x-p/q|<1/(qN)\le1/q^2\); reducing the fraction keeps the inequality. The value is nonzero since \(x\) is irrational. As \(N\to\infty\), \(|x-p/q|<1/(qN)\le1/N\to0\), so infinitely many distinct fractions arise, and their denominators are unbounded because only finitely many fractions with bounded denominator lie near \(x\). \(\square\)

**Proposition 1.4** (Liouville). Let \(x\) be a real algebraic number of degree \(n\ge2\). There is \(c>0\) with \(|x-p/q|\ge c\,q^{-n}\) for all integers \(p\) and \(q\ge1\). Hence \(\mu(x)\le n\).

**Proof.** Let \(f\in\mathbb Z[T]\) be irreducible of degree \(n\) with \(f(x)=0\). If \(|x-p/q|\ge1\) there is nothing to prove with \(c\le1\). Otherwise \(f(p/q)\ne0\) (an irreducible polynomial of degree \(n\ge2\) has no rational root), and \(q^nf(p/q)\) is a nonzero integer, so \(|f(p/q)|\ge q^{-n}\). By the mean value theorem, \(|f(p/q)|=|f(p/q)-f(x)|\le M|x-p/q|\) with \(M=\max_{|t-x|\le1}|f'(t)|\). So \(c=\min(1,1/M)\) works. \(\square\)

For instance \(\sum_{k\ge1}10^{-k!}\) has \(\mu=\infty\): its partial sums \(p/q\) with \(q=10^{N!}\) satisfy \(0<|x-p/q|<2\cdot10^{-(N+1)!}=2q^{-(N+1)}\). By Proposition 1.4 it is transcendental. Roth's theorem [Roth] says that \(\mu(x)=2\) for every irrational algebraic \(x\).

## 2. The theorem for \(\pi\)

The main theorem of this course, due to OpenAI (2026), is proved as Theorem 2.1 of [The irrationality exponent of π is two](the-irrationality-exponent-of-pi-is-two.md):

> *For every real \(\nu>2\) there is an integer \(Q(\nu)\) such that \(|\pi-p/q|>q^{-\nu}\) for all integers \(p\) and all integers \(q\ge Q(\nu)\). Consequently \(\pi\) is irrational and \(\mu(\pi)=2\).*

The irrationality of \(\pi\) follows from the inequality itself: if \(\pi=a/b\), then the fractions \(ak/(bk)\) would violate it for large \(k\). Lemma 1.2 and Proposition 1.3 then give \(\mu(\pi)=2\). The proof is not effective: it gives no value of \(Q(\nu)\).

The question goes back to Mahler, who proved in 1953 that \(\mu(\pi)\) is finite, with the bound \(42\). Successive improvements reached \(20\) (Mignotte, 1974 [Mignotte]), \(8.016\) (Hata, 1993), \(7.606\) (Salikhov, 2008) and \(7.103\) (Zeilberger and Zudilin [Zeilberger–Zudilin]); see [Zudilin] for the method of integrals behind these values. The conjecture \(\mu(\pi)=2\) is recorded in [Waldschmidt]. These bounds use explicit integrals that produce good rational approximations of \(\pi\) and are not used in the proof of Theorem 2.1.

The theorem implies that \(\sum_{n\ge1}1/(n^3\sin^2n)\) converges, which needs only \(\mu(\pi)<5/2\) [Alekseyev, Meiburg]; this and the exact convergence region of \(\sum n^{-a}|\sin n|^{-b}\) are proved in [The irrationality exponent of π is two](the-irrationality-exponent-of-pi-is-two.md).

## 3. The structure of the proof

The proof is by contradiction. Fix \(\nu>2\) and suppose that \(|\pi-p/q|\le q^{-\nu}\) has solutions with arbitrarily large \(q\). The proof constructs, for a degree parameter \(H\to\infty\), a nonzero determinant \(\Delta_H\) and shows that it is both too large and too small.

*The functions.* The number \(\pi\) enters through the periods of the exponential function: \(e^{2\pi ij}=1\) for every integer \(j\). For a polynomial \(P(Y,X_1,\dots,X_m)\), consider

\[
z\mapsto P(e^z,z+u_1,\dots,z+u_m),
\]

an entire function of \(z\) depending on parameters \(u_i\). Near \(z=2\pi ij\), write \(z=2\pi ij+\log(1+t)\). Then \(e^z=1+t\) and \(X_i=z+u_i=2\pi ij+u_i+\log(1+t)\). So the Taylor coefficients of these functions at the points \(2\pi ij\) are Taylor coefficients of \(P\) along the *logarithmic curves*

\[
Y=1+t,\qquad X_i=c_{ji}+u_i+\log(1+t),\qquad c_{ji}=2\pi ij .
\]

*Arithmetic.* The centres \(2\pi ij\) are transcendental, but if \(p_i/q_i\) are very good approximations of \(\pi\), the nearby centres \(c_{ji}=2ijp_i/q_i\) are Gaussian rationals with denominator \(q_i\). Taylor coefficients at these rational centres, of polynomials with integer coefficients, are Gaussian rationals with controlled denominators, so a nonzero determinant of such coefficients cannot be too small.

*Analysis.* Moving the centres back to the exact periods \(2\pi ij\) costs a factor involving the errors \(|\pi-p_i/q_i|\le q_i^{-\nu}\), which are tiny. At the exact periods, the rows of the matrix are Taylor coefficients of the same entire functions at different points, and a Taylor expansion of the determinant forces a large saving. So the determinant is also very small.

*Interpolation.* To have a nonzero determinant at all, one needs that the polynomials of bounded weighted degree can realize every prescribed packet of Taylor coefficients at all the centres simultaneously. This *interpolation theorem* is the deepest part of the proof. Counting dimensions shows there are more polynomials than conditions, but this does not prove independence of the conditions. The proof uses a zero estimate: if the conditions were dependent, there would be an algebraic curve with too much contact with the logarithmic curves, and a careful choice of weights rules this out. Positivity of a line bundle on a blow-up, through Kleiman's theorem, then turns the absence of such curves into the surjectivity of the interpolation map.

The lessons follow this structure.

1. [Weighted multiplicity estimates](weighted-multiplicity-estimates.md): a comparison of multiplicities along commuting vector fields with degrees, by Bézout's inequality.
2. [The curve inequality](the-curve-inequality.md): with separated weights, every algebraic curve has weighted degree larger than its total contact with the logarithmic curves.
3. [Interpolation on logarithmic curves](interpolation-on-logarithmic-curves.md): from the curve inequality to the surjectivity of the interpolation map, through blow-ups and positivity.
4. [An interpolation determinant for π](an-interpolation-determinant-for-pi.md): the matrix, its arithmetic lower bound, and its analytic upper bound.
5. [The irrationality exponent of π is two](the-irrationality-exponent-of-pi-is-two.md): the choice of parameters, the proof of the main theorem, and the Flint–Hills series.

The method combines ideas of the interpolation-determinant method of Laurent [Laurent], zero estimates in the style of Philippon [Philippon], and the separated choice of approximations familiar from Roth's theorem [Roth].

## 4. Exercises

**Exercise 4.1.** Show that \(\mu(x)\) does not change if \(x\) is replaced by \(ax+b\) with rational \(a\ne0\), \(b\).

**Exercise 4.2.** Show that \(\mu(\sqrt2)=2\) directly from Proposition 1.4.

**Exercise 4.3.** Let \(x=\sum_{k\ge1}2^{-3^k}\). Show that \(\mu(x)\ge3\).

**Exercise 4.4.** Show that if \(\mu(x)<\nu\), then there is \(c>0\) with \(|x-p/q|\ge c\,q^{-\nu}\) for all integers \(p\) and \(q\ge1\).

## 5. Solutions

**4.1.** Write \(a=r/s\), \(b=u/v\). If \(|x-p/q|<q^{-\nu}\), then \(|(ax+b)-(ap/q+b)|<|a|q^{-\nu}\), and \(ap/q+b\) has denominator dividing \(svq\), which is at most a constant times \(q\). So exponents \(\nu'<\nu\) are attained by \(ax+b\) infinitely often. The converse uses the inverse map \(x=(y-b)/a\).

**4.2.** \(\sqrt2\) has degree \(2\), so \(\mu\le2\) by Proposition 1.4, and \(\mu\ge2\) by Proposition 1.3.

**4.3.** The partial sum up to \(k=N\) is \(p/q\) with \(q=2^{3^N}\), and the tail is less than \(2\cdot2^{-3^{N+1}}=2q^{-3}\). So \(|x-p/q|<2q^{-3}\) for infinitely many \(q\), and every \(\nu<3\) is attained.

**4.4.** By definition only finitely many coprime \((p,q)\) satisfy \(|x-p/q|<q^{-\nu}\); by Lemma 1.2 there is \(Q\) with \(|x-p/q|\ge q^{-\nu}\) for \(q\ge Q\). For the finitely many \(q<Q\), \(\min_p|x-p/q|>0\) since \(x\) is irrational. Take \(c\) as the minimum of \(1\) and \(q^\nu\min_p|x-p/q|\) over \(q<Q\).

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Zeilberger–Zudilin] D. Zeilberger, W. Zudilin, The irrationality measure of π is at most 7.103205334137…, Moscow Journal of Combinatorics and Number Theory 9 (2020). https://arxiv.org/abs/1912.06345
- [Zudilin] W. Zudilin, An essay on irrationality measures of π and other logarithms, arXiv:math/0404523 (2004). https://arxiv.org/abs/math/0404523
- [Mignotte] M. Mignotte, Approximations rationnelles de π et quelques autres nombres, Mémoires de la Société Mathématique de France 37 (1974). https://www.numdam.org/articles/10.24033/msmf.139/
- [Waldschmidt] M. Waldschmidt, Open Diophantine problems, Moscow Mathematical Journal 4 (2004). https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/odp.pdf
- [Alekseyev] M. A. Alekseyev, On convergence of the Flint Hills series, arXiv:1104.5100 (2011). https://arxiv.org/abs/1104.5100
- [Meiburg] A. Meiburg, Bounds on irrationality measures and the Flint-Hills series, arXiv:2208.13356 (2022). https://arxiv.org/abs/2208.13356
- [Roth] K. F. Roth, Rational approximations to algebraic numbers, Proceedings of the International Congress of Mathematicians 1958. https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf
- [Laurent] M. Laurent, Sur quelques résultats récents de transcendance, Astérisque 198–200 (1991). https://www.numdam.org/item/AST_1991__198-199-200__209_0/
- [Philippon] P. Philippon, Lemmes de zéros dans les groupes algébriques commutatifs, Bulletin de la Société Mathématique de France 114 (1986). https://www.numdam.org/articles/10.24033/bsmf.2060/
