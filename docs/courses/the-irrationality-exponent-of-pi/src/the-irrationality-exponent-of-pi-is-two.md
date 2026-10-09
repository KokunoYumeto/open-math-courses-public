# The irrationality exponent of π is two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof that \(\mu(\pi)=2\). The determinant comparison of [An interpolation determinant for π](an-interpolation-determinant-for-pi.md) produces a contradiction once five error terms are smaller than an approximation gain \(g\), and once a collision saving \(c\mathcal L\) exceeds \(1\). Here the parameters are chosen in the order that makes this possible: first the shape constants \(\theta,A,B,C,\eta\) from \(\nu\), then the dimension \(m\), and only then the approximations \(p_i/q_i\), whose denominators define the weights. The degree \(H\) tends to infinity last. The lesson ends with the Flint–Hills series and the exact convergence region of \(\sum n^{-a}|\sin n|^{-b}\).

We use Proposition 5.1 of the determinant lesson, Theorem 1.1 of [Interpolation on logarithmic curves](interpolation-on-logarithmic-curves.md) and Lemma 1.2 and Proposition 1.3 of [Irrationality exponents](irrationality-exponents.md). Notation: \(\Lambda=4\log2\), \(c=(\log2)/4\), and \(\|x\|\) is the distance from \(x\) to the nearest integer.

## 1. The shape constants

**Lemma 1.1.** For every real \(\nu>2\) there are positive rationals \(\theta,A,B,C\) with

\[
0<\theta<A<B<1,\qquad\nu(A-\theta)>1-\theta,\qquad C>1,\qquad B<1/C,\qquad B<C\theta<1,
\tag{1.1}
\]

and then a rational \(0<\eta<1\) with

\[
g=\nu\bigl(A(1-\eta)-\theta\bigr)-(1-\theta)>0 .
\tag{1.2}
\]

**Proof.** Choose a rational \(b\) with \(1/2<b<1-1/\nu\), possible since \(\nu>2\). For a small rational \(\delta>0\) put \(\theta=1-\delta\) and \(A=1-b\delta\). Then \(0<\theta<A<1\), and

\[
\nu(A-\theta)-(1-\theta)=\bigl(\nu(1-b)-1\bigr)\delta>0,\qquad\theta-A^2=(2b-1)\delta-b^2\delta^2>0
\]

for \(\delta\) small. So \(A/\theta<1/A\); choose a rational \(C\) strictly between them. Then \(C>A/\theta>1\), and \(C\theta<\theta/A<1\). Since \(A<1/C\) and \(A<C\theta\), we can choose a rational \(B\) with \(A<B<\min(1/C,C\theta)\). Finally (1.2) holds at \(\eta=0\) by the first inequality, hence for small rational \(\eta>0\). \(\square\)

The inequality \(\nu(A-\theta)>1-\theta\) provides the approximation gain, and it is here that \(\nu>2\) is used. The inequality \(A^2<\theta\) allows \(A/\theta<C<1/A\), and then \(B\) with \(CB<1\), \(C\theta/B>1\) and \(B/A>1\). These three ratios control, respectively, the analytic error \(K/w_0\), the arithmetic error \(m/v_0\), and the collision saving \(\mathcal L\) below.

## 2. Proof of the main theorem

**Theorem 2.1** (OpenAI, 2026). For every real \(\nu>2\) there is \(Q(\nu)\) such that \(|\pi-p/q|>q^{-\nu}\) for all integers \(p\) and all integers \(q\ge Q(\nu)\). Consequently \(\pi\) is irrational and \(\mu(\pi)=2\).

**Proof.** Fix \(\nu>2\) and suppose, to the contrary, that there are integers \(p,q\) with \(q\) arbitrarily large and

\[
\Bigl|\pi-\frac pq\Bigr|\le q^{-\nu}.
\tag{2.1}
\]

Fix \(\theta,A,B,C,\eta,g\) by Lemma 1.1 and put \(\varepsilon_0=\min(g/2,1/2)\). Choose a rational \(F_0>2/\theta\) with \(\nu/F_0<\varepsilon_0/3\).

*The dimension.* For an integer \(m\ge1\) put

\[
K=\lfloor C^m\rfloor,\qquad w_0=B^{-m},\qquad v_0=2K\theta^mw_0 .
\]

These are positive rationals (and \(K\ge1\) is an integer), and they satisfy the hypotheses of the interpolation theorem:

\[
K\theta^m\le(C\theta)^m<1,\qquad K\frac{w_0}{v_0}\theta^m=\frac12<1 .
\]

As \(m\to\infty\),

\[
\frac K{w_0}\le(CB)^m\to0,\qquad v_0\ge2(C^m-1)\theta^mB^{-m}\sim2\Bigl(\frac{C\theta}B\Bigr)^m\to\infty,\qquad\frac m{v_0}\to0,
\]

and the quantity \(\mathcal L\) of the determinant lesson, with these data, is

\[
\mathcal L=\frac{\eta^2K\theta^m}{(m+1)v_0A^m}=\frac{\eta^2}{2(m+1)}\Bigl(\frac BA\Bigr)^m\to\infty .
\]

Fix \(m\) so large that

\[
\frac{\Lambda F_0m+2\log2}{v_0}+\frac{100K}{w_0}<\frac{\varepsilon_0}3,\qquad c\mathcal L>2,
\tag{2.2}
\]

and fix the resulting \(K,w_0,v_0\).

*The approximations.* Now choose solutions \(p_1/q_1,\dots,p_m/q_m\) of (2.1), one after the other, with \(q_i\) so large that \(w_i=\lceil\log q_i\rceil\) exceeds the threshold of the interpolation theorem (which depends only on the fixed data and on \(w_1,\dots,w_{i-1}\)), and also so large that

\[
\Lambda\sum_{i=1}^m\frac1{w_i}+\frac{\theta+\log4+\log(2K)+\nu+\log(200K)}{w_*}<\frac{\varepsilon_0}3,\qquad w_*=\min_iw_i;
\tag{2.3}
\]

for this it suffices that every \(w_i\) exceeds a bound depending only on \(m,K,\theta,\nu,\varepsilon_0\), since \(\sum_i1/w_i\le m/w_*\). This is possible because (2.1) has solutions with arbitrarily large \(q\). For large \(q_i\) also \(p_i\ne0\), since \(p_i/q_i\) is close to \(\pi\).

*The contradiction.* The errors of the determinant lesson add up to

\[
E_{\mathrm{ar}}+E_{\mathrm{an}}=\frac\nu{F_0}+\frac{\Lambda F_0m+2\log2}{v_0}+\frac{100K}{w_0}+\Lambda\sum_i\frac1{w_i}+\frac{\theta+\log4+\log(2K)+\nu+\log(200K)}{w_*}<\varepsilon_0,
\]

by the choice of \(F_0\), (2.2) and (2.3). Hence \(E_{\mathrm{ar}}+E_{\mathrm{an}}<g\), and \(c\mathcal L>2>1+E_{\mathrm{ar}}+E_{\mathrm{an}}\), while \(g>0\). All the hypotheses of the determinant lesson hold, and its Proposition 5.1 says that this is impossible. So (2.1) has solutions only with bounded \(q\), which is the first claim.

If \(\pi=a/b\) were rational, the fractions \(ak/(bk)\) would satisfy (2.1) with error \(0\) and arbitrarily large denominators; so \(\pi\) is irrational. By Lemma 1.2 of the first lesson the first claim gives \(\mu(\pi)\le\nu\) for every \(\nu>2\), and Dirichlet's theorem gives \(\mu(\pi)\ge2\). \(\square\)

The proof gives no value of \(Q(\nu)\): the approximations \(p_i/q_i\) are assumed to exist, and the contradiction comes only after the degree \(H\) is taken large. The order of the choices is essential. The weights \(w_i\) must be separated before the centres \(2\mathrm ijp_i/q_i\) are known, and they can be, because the thresholds of the interpolation theorem do not depend on the centres.

## 3. The Flint–Hills series

**Lemma 3.1** (spacing). Let \(\alpha\) be irrational, \(\kappa>1\), \(c_0>0\), and suppose \(\|q\alpha\|\ge c_0q^{-\kappa+1}\) for all integers \(q\ge1\). Let \(K\ge1\) and \(d=c_0(2K)^{1-\kappa}\). Then the points \(q\alpha\bmod1\), \(K\le q<2K\), are at distance at least \(d\) from \(0\) and from each other on the circle \(\mathbb R/\mathbb Z\), and for every \(b>0\)

\[
\sum_{K\le q<2K}\|q\alpha\|^{-b}\le2d^{-b}\sum_{j=1}^Kj^{-b}.
\]

**Proof.** For \(K\le q<2K\), \(\|q\alpha\|\ge c_0q^{1-\kappa}\ge d\). For two such \(q\ne q'\), the difference \(|q-q'|<K\) gives \(\|(q-q')\alpha\|\ge c_0|q-q'|^{1-\kappa}\ge d\). Each point lies in one of the two open half-circles \((0,1/2)\) and \((1/2,1)\), since a point at \(1/2\) would make \(\alpha\) rational. On each half-circle, order the points by their distance to \(0\); the first is at distance at least \(d\), and each next one at least \(d\) further, so the \(l\)-th is at distance at least \(ld\). There are at most \(K\) points on each half-circle. \(\square\)

**Theorem 3.2** (generalized Flint–Hills series). For real \(a,b>0\), the series

\[
\sum_{n=1}^\infty\frac1{n^a|\sin n|^b}
\]

(with \(n\) in radians) converges if and only if \(a>\max\{1,b\}\). In particular the Flint–Hills series \(\sum_{n\ge1}n^{-3}\sin^{-2}n\) converges.

**Proof.** No term is infinite: \(\sin n=0\) would make \(\pi\) rational.

*Convergence for \(a>\max\{1,b\}\).* Choose \(\epsilon>0\) with \(a>\max\{1,b\}+b\epsilon\). Theorem 2.1 with \(\nu=2+\epsilon\) gives \(|q\pi-p|>q^{-1-\epsilon}\) for \(q\ge Q\); for the finitely many \(q<Q\), \(\|q\pi\|>0\) by irrationality. So there is \(c_\epsilon>0\) with \(\|q\pi\|\ge c_\epsilon q^{-1-\epsilon}\) for all \(q\ge1\). Lemma 3.1 with \(\kappa=2+\epsilon\) and \(d=c_\epsilon(2K)^{-1-\epsilon}\) gives

\[
\sum_{K\le q<2K}\frac1{q^a\|q\pi\|^b}\le\frac{2}{K^ad^b}\sum_{j=1}^Kj^{-b}\ll_{a,b,\epsilon}
\begin{cases}K^{1-a+b\epsilon},&0<b<1,\\K^{1-a+\epsilon}\log(2K),&b=1,\\K^{b-a+b\epsilon},&b>1.\end{cases}
\]

Every exponent is negative, so summing over \(K=1,2,4,\dots\) shows \(\sum_{q\ge1}q^{-a}\|q\pi\|^{-b}<\infty\). For a positive integer \(n\), let \(q\) be a nearest integer to \(n/\pi\), so \(|n-q\pi|\le\pi/2\). Only \(n=1\) has \(q=0\). For \(q\ge1\), the \(n\) with this \(q\) lie in an interval of length \(\pi<4\), so there are at most four, each with \(n\ge\pi(q-\frac12)\ge\pi q/2\) and, by concavity of \(\sin\) on \([0,\pi/2]\),

\[
|\sin n|=|\sin(n-q\pi)|\ge\frac2\pi|n-q\pi|\ge\frac2\pi\|q\pi\| .
\]

So the terms with a given \(q\ge1\) add up to at most \(4(2/\pi)^a(\pi/2)^bq^{-a}\|q\pi\|^{-b}\), and the series converges.

*Divergence otherwise.* If \(a\le1\), the series dominates \(\sum n^{-a}=\infty\). Let \(1<a\le b\). By Dirichlet's theorem there are infinitely many fractions \(p/q\) with \(q\ge1\) and \(|\pi-p/q|<1/q^2\); for them \(p\to\infty\), \(p\le(\pi+1)q\) eventually, and \(|\sin p|=|\sin(p-q\pi)|\le|p-q\pi|<1/q\). Hence

\[
\frac1{p^a|\sin p|^b}>p^{-a}q^b\ge(\pi+1)^{-b}p^{b-a}\ge(\pi+1)^{-b}
\]

for infinitely many \(p\), and the terms do not tend to zero. \(\square\)

The classical case \(a=3\), \(b=2\) needs only \(\mu(\pi)<5/2\) [Alekseyev, Meiburg]: the dyadic block is then \(\ll K^{-3}d^{-2}\ll K^{2\nu-5}\). Before Theorem 2.1, the best known bound \(\mu(\pi)\le7.103\) did not suffice.

## 4. Exercises

**Exercise 4.1.** Verify the claims about \(K/w_0\), \(v_0\), \(m/v_0\) and \(\mathcal L\) in the proof of Theorem 2.1 for \(\nu=3\) with an explicit choice of \(\theta,A,B,C\).

**Exercise 4.2.** Show that Theorem 2.1 implies \(\|q\pi\|\gg_\epsilon q^{-1-\epsilon}\) for all \(q\ge1\), and that this is the best possible exponent up to \(\epsilon\).

**Exercise 4.3.** Show that \(\sum_{n\ge1}1/(n^2|\sin n|^2)\) diverges, and that \(\sum_{n\ge1}1/(n^2|\sin n|)\) converges.

**Exercise 4.4.** Explain why the proof of Theorem 2.1 cannot choose the dimension \(m\) after the approximations \(p_i/q_i\).

## 5. Solutions

**4.1.** Take \(b=3/5\), which lies between \(1/2\) and \(1-1/3\), and \(\delta=1/10\): \(\theta=9/10\), \(A=47/50\). Then \(\nu(A-\theta)-(1-\theta)=3\cdot\frac1{25}-\frac1{10}=\frac1{50}>0\) and \(\theta-A^2=0.9-0.8836>0\), so \(A/\theta\approx1.0444<1/A\approx1.0638\). Take \(C=21/20\); then \(C\theta=0.945\) and \(1/C\approx0.9524\), and \(B=377/400=0.9425\) satisfies \(A<B<\min(1/C,C\theta)\). The three ratios are \(CB=0.989625<1\), \(C\theta/B\approx1.00265>1\) and \(B/A\approx1.00266>1\). For (1.2) take \(\eta=1/200\): \(A(1-\eta)=0.9353\) and \(g=3\cdot0.0353-0.1=0.0059>0\) (the larger value \(\eta=1/100\) gives \(g<0\)). So \(K/w_0\le(0.989625)^m\to0\), \(v_0\sim2(1.00265)^m\to\infty\), and \(\mathcal L\sim\eta^2(1.00266)^m/(2(m+1))\to\infty\), all slowly: with \(\eta=1/200\) and \(c=(\log2)/4\), the condition \(c\mathcal L>2\) first holds at \(m=8582\).

**4.2.** For \(q\ge Q(2+\epsilon)\), \(\|q\pi\|=\min_p|q\pi-p|\ge q^{-1-\epsilon}\); the finitely many smaller \(q\) have \(\|q\pi\|>0\). By Dirichlet's theorem \(\|q\pi\|<1/q\) infinitely often, so \(-1\) cannot be replaced by a larger exponent.

**4.3.** For \(a=b=2\), \(a\le b\), so the series diverges by Theorem 3.2. For \(a=2\), \(b=1\), \(a>\max\{1,b\}\), so it converges.

**4.4.** The interpolation thresholds for the weights depend on \(m\), \(K\), \(w_0\) and \(v_0\), and the error terms involve \(m\), \(K\), \(w_0\), \(v_0\) together with \(1/w_*\). The approximations are chosen to make \(1/w_*\) small relative to these, so the dimension must be fixed first; conversely the condition \(c\mathcal L>2\) and the bounds (2.2) do not involve the approximations.

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Alekseyev] M. A. Alekseyev, On convergence of the Flint Hills series, arXiv:1104.5100 (2011). https://arxiv.org/abs/1104.5100
- [Meiburg] A. Meiburg, Bounds on irrationality measures and the Flint-Hills series, arXiv:2208.13356 (2022). https://arxiv.org/abs/2208.13356
- [Zeilberger–Zudilin] D. Zeilberger, W. Zudilin, The irrationality measure of π is at most 7.103205334137…, Moscow Journal of Combinatorics and Number Theory 9 (2020). https://arxiv.org/abs/1912.06345
