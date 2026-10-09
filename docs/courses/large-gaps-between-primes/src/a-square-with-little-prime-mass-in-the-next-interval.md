# A square with little prime mass in the next interval

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson defines the function \(Z(m)\) whose square, suitably normalized, is the weight of Proposition 4.1 in [Prime gaps and adjacent intervals](prime-gaps-and-adjacent-intervals.md), and computes all the moments that the proposition needs. \(Z\) is a sum of smooth divisor sums over all subsets \(S\) of the second block \(I=\{h+1,\dots,2h\}\) with at most \(k\) elements, one test function for each size. The moments are computed with [Correlations of smooth divisor sums](correlations-of-smooth-divisor-sums.md) and summed over the shifts with [The singular series and its average](the-singular-series-and-its-average.md).

The essential point is the different effect of a prime in each block. A prime \(m+b\) with \(b\in J\) lies outside every subset used to build \(Z\) and does not interact with it. A prime \(m+a\) with \(a\in I\) collapses every divisor sum containing the shift \(a\) to a sum of one dimension less. So the prime mass of \(Z^2\) in \(I\) couples the test functions of neighbouring sizes, and it can be made small by making neighbouring sizes cancel; this is done in [Cancellation between adjacent dimensions](cancellation-between-adjacent-dimensions.md).

The notation of the earlier lessons is kept: \(L=\log X\), \(h=\lfloor\lambda L\rfloor\), \(J=\{1,\dots,h\}\), \(I=\{h+1,\dots,2h\}\), \(\mathbb E_X\), \(\vartheta\), \(V_B\), and the divisor sums \(D_F(m;\mathbf b)\).

## 1. Cumulative test functions

Fix \(\tau=1/8\) and an integer \(k\ge1\). For \(j\ge1\) let

\[
\Omega_j=\{t\in(0,\infty)^j:\ t_1+\dots+t_j<\tau\}.
\]

**Data 1.1.** A *family* consists of a real number \(f_0\) and, for \(1\le j\le k\), real symmetric functions \(f_j\in C_c^\infty(\Omega_j)\). Put \(f_{k+1}=0\). For \(j\ge1\) define on \([0,\infty)^j\)

\[
F_j(v)=\int_{s_1\ge v_1,\dots,s_j\ge v_j}f_j(s)\,ds,\qquad F_0=f_0,\qquad F_{k+1}=0,
\]

and for \(j\ge0\) the function of \(j\) variables (a number when \(j=0\))

\[
(Tf_{j+1})(t)=\int_0^\infty f_{j+1}(t,u)\,du .
\]

Norms \(\|\cdot\|\) are \(L^2\) norms on \((0,\infty)^j\), and the absolute value when \(j=0\).

**Lemma 1.2.**

1. \(F_j\) is a symmetric test function of dimension \(j\) and budget \(\tau\), and \((-1)^j\partial_1\cdots\partial_jF_j=f_j\).
2. \(f_j\) vanishes on a neighbourhood of every coordinate face \(\{v_i=0\}\) of the orthant.
3. For \(0\le j\le k\), \(\widetilde F_j:=F_j+F_{j+1}(\cdot,0)\) is a symmetric test function of dimension \(j\) and budget \(\tau\), with \((-1)^j\partial_1\cdots\partial_j\widetilde F_j=f_j+Tf_{j+1}\). For \(j\ge1\), \(f_j+Tf_{j+1}\) vanishes near every coordinate face. For \(j=0\), \(\widetilde F_0=f_0+Tf_1\).

**Proof.** (1) Extend \(f_j\) by zero to \(\mathbb R^j\). Then \(F_j(v)=\int_{[0,\infty)^j}f_j(v+s)\,ds\) defines a smooth function on \(\mathbb R^j\), by differentiation under the integral sign. If \(v_i\ge T\), where \(T\) bounds the coordinates on the support of \(f_j\), then \(F_j(v)=0\). Multiplying by \(\prod_i\psi(v_i)\), with \(\psi\) smooth, equal to \(1\) on \([-\frac12,\infty)\) and to \(0\) on \((-\infty,-1]\), gives a compactly supported smooth function equal to \(F_j\) on the orthant. On the orthant, if \(\sum v_i\ge\tau\), every \(s\ge v\) has \(\sum s_i\ge\tau\), so \(f_j(s)=0\) and \(F_j(v)=0\). Symmetry of \(f_j\) gives symmetry of \(F_j\). Differentiating \(\int_{s\ge v}f_j\) in \(v_1\) gives \(-\int_{s_2\ge v_2,\dots}f_j(v_1,s_2,\dots)\,ds_2\cdots\); repeating in each variable gives \((-1)^jf_j\).

(2) The support of \(f_j\) is a compact subset of \(\Omega_j\subset(0,\infty)^j\), so all its coordinates are bounded below by a positive number.

(3) \(F_{j+1}(v,0)=\int_{s\ge v}\int_0^\infty f_{j+1}(s,u)\,du\,ds=\int_{s\ge v}(Tf_{j+1})(s)\,ds\). If \((t,u)\) lies in the support of \(f_{j+1}\), then \(t_1+\dots+t_j<\tau-u<\tau\) and the coordinates of \(t\) are bounded below; so \(Tf_{j+1}\in C_c^\infty(\Omega_j)\) for \(j\ge1\), and it is symmetric. Part (1) applied to \(f_j+Tf_{j+1}\) proves the claims. \(\square\)

## 2. The signed sum and its moments

For a set \(S\subseteq I\) with \(j\) elements write \(D_{F_j}(m;S)\) for \(D_{F_j}(m;s_1,\dots,s_j)\) with the elements of \(S\) in any order; by symmetry of \(F_j\) the order does not matter. Define

\[
Z(m)=\sum_{j=0}^k\ \sum_{\substack{S\subseteq I\\|S|=j}}D_{F_j}(m;S),\qquad\alpha_j=\frac{\lambda^j}{j!},
\]

\[
w=\sum_{j=0}^k\alpha_j\|f_j\|^2,\qquad v=\lambda\sum_{j=0}^k\alpha_j\|f_j+Tf_{j+1}\|^2 .
\]

Fix also a real \(G\in C_c^\infty(\mathbb R)\) with \(G(0)=1\) and \(G(u)=0\) for \(u\ge\tau\), and put

\[
c_G=\int_0^\infty G'(u)^2\,du,\qquad C_*=\lambda+\lambda^2c_G^2 .
\]

The restriction of \(G\) to \([0,\infty)\) is a one-dimensional test function of budget \(\tau\).

**Proposition 2.1** (moments of the square). Hold \(\lambda\), \(k\), the family \((f_j)\) and \(G\) fixed. As \(X\to\infty\):

\[
\mathbb E_XZ^2\to w,\qquad\mathbb E_XZ^4=O(1),\qquad\mathbb E_X(Z^2V_J)\to\lambda w,\qquad\mathbb E_X(Z^2V_I)\to v,
\]

and

\[
\limsup_{X\to\infty}\mathbb E_X(Z^2V_J^2)\le C_*w .
\]

The constant \(C_*\) depends only on \(\lambda\) and \(G\), not on \(k\) or on the family.

The proof is in Section 4. The formulas show how the two prime counts see the weight. A prime in \(J\) multiplies the mass \(w\) by its density \(\lambda\). A prime in \(I\) replaces each \(f_j\) by \(f_j+Tf_{j+1}\). The second count is small when \(f_j\approx-Tf_{j+1}\) for most \(j\).

## 3. A prime in the second block

**Lemma 3.1** (deletion). Let \(a\in I\) and suppose \(m+a\) is a prime with \(m>X\). Then

\[
Z(m)=\sum_{j=0}^k\ \sum_{\substack{U\subseteq I\setminus\{a\}\\|U|=j}}D_{\widetilde F_j}(m;U),\qquad\widetilde F_j=F_j+F_{j+1}(\cdot,0).
\]

**Proof.** Split the subsets \(S\) in the definition of \(Z\) according to whether they contain \(a\). Those not containing \(a\) are the sets \(U\subseteq I\setminus\{a\}\) with \(|U|\le k\), each contributing \(D_{F_{|U|}}(m;U)\). A set containing \(a\) is \(U\cup\{a\}\) with \(U\subseteq I\setminus\{a\}\) and \(|U|\le k-1\). List \(a\) last. Since \(\log(m+a)/L>1>\tau\), Lemma 1.3 of [Divisor sums and primes in progressions](divisor-sums-and-primes-in-progressions.md) gives \(D_{F_{|U|+1}}(m;U\cup\{a\})=D_{F_{|U|+1}(\cdot,0)}(m;U)\). Each \(U\) therefore occurs once with \(F_{|U|}\) and once with \(F_{|U|+1}(\cdot,0)\), the latter being \(0\) when \(|U|=k\). Adding gives \(D_{\widetilde F_{|U|}}(m;U)\). \(\square\)

Every subset \(U\) occurs exactly once on the right: deletion introduces no combinatorial factor.

## 4. Proof of Proposition 2.1

All shifts below lie in \(\{1,\dots,2h\}\), so \(|a|\le2\lambda L\): Theorem 1.1 of the correlations lesson applies with \(D=2\lambda\), \(B=1\). The budgets used are

| moment | factors | total budget | prime mark |
|---|---|---|---|
| \(\mathbb E_XZ^2\) | 2 | \(2\tau=1/4<1\) | none |
| \(\mathbb E_X(Z^2V_B)\), \(B=I,J\) | 2 | \(2\tau=1/4<1/2\) | one |
| \(\mathbb E_XZ^4\) | 4 | \(4\tau=1/2<1\) | none |
| detector, off-diagonal | 6 | \(6\tau=3/4<1\) | none |

*Counting.* For fixed \(j\), Corollary 4.2 of the singular-series lesson gives \(\sum_{S\subseteq I,\,|S|=j}\mathfrak S(S)=\frac1{j!}\sum\mathfrak S(\{a_1,\dots,a_j\})=\frac{h^j}{j!}(1+o(1))\), the second sum over ordered distinct tuples. Since \(h/L\to\lambda\),

\[
L^{-j}\sum_{|S|=j}\mathfrak S(S)\to\alpha_j,\qquad L^{-j-1}\sum_{b\in J}\sum_{|S|=j}\mathfrak S(S\cup\{b\})\to\lambda\alpha_j,
\]

\[
L^{-j-1}\sum_{a\in I}\sum_{\substack{U\subseteq I\setminus\{a\}\\|U|=j}}\mathfrak S(U\cup\{a\})\to\lambda\alpha_j,\qquad L^{-j-2}\sum_{\substack{b,c\in J\\b\ne c}}\sum_{|S|=j}\mathfrak S(S\cup\{b,c\})\to\lambda^2\alpha_j .
\]

In the last three sums every tuple of shifts is automatically distinct, because \(I\) and \(J\) are disjoint.

*Errors.* Each moment is a sum over finitely many shapes: a shape records the sizes of the subsets involved and which of their elements coincide. For a fixed shape with \(t\) distinct shifts, Theorem 1.1 of the correlations lesson gives an error \(L^{-t}O(L^{-1/2}(\log L)^A)\) for each choice of shifts, uniformly, and there are \(O(h^t)\) choices, or \(O(h^{t+1})\) when one further prime shift is summed and divided by \(L\). Since \(h\asymp L\), the total error of each shape is \(O(L^{-1/2}(\log L)^A)=o(1)\). Only the main terms remain.

*The second moment.* Expand \(Z^2=\sum_{S,T}D_{F_{|S|}}(m;S)D_{F_{|T|}}(m;T)\). For a pair \((S,T)\), the distinct shifts are \(S\cup T\); those in \(S\cap T\) form fibres of two coordinates, those in \(S\triangle T\) singleton fibres. By (1.1) of the correlations lesson, the constant is an integral of \(f_{|S|}f_{|T|}\) with the variable of every singleton fibre set to \(0\). If \(S\ne T\), some shift lies in exactly one of them, and the corresponding \(f\) vanishes there by Lemma 1.2(2): the constant is \(0\). If \(S=T\) has \(j\) elements, listed in the same order in both factors, the constant is \(\int f_j^2=\|f_j\|^2\) (and \(f_0^2\) for \(j=0\)). Hence

\[
\mathbb E_XZ^2=\sum_{j=0}^k\|f_j\|^2L^{-j}\sum_{|S|=j}\mathfrak S(S)+o(1)\to\sum_j\alpha_j\|f_j\|^2=w .
\]

*The fourth moment.* For a quadruple \((S_1,\dots,S_4)\) with union \(U\), \(|U|=t\), Theorem 1.1 of the correlations lesson gives \(L^{-t}(\mathfrak S(U)\mathcal C+o(1))\), where \(\mathcal C\) depends only on the shape; here fibres may have up to four elements and only the finiteness of \(\mathcal C\) is used. At most \(15^t\) quadruples have a given union, since each element of \(U\) lies in a nonempty subset of the four sets. Hence \(|\mathbb E_XZ^4|\ll\sum_{t\le4k}15^tL^{-t}\sum_{|U|=t}\mathfrak S(U)+o(1)=O(1)\).

*A prime in \(J\).* \(\mathbb E_X(Z^2V_J)=L^{-1}\sum_{b\in J}\sum_{S,T}\mathbb E_X[\vartheta(m+b)D_{F_{|S|}}(m;S)D_{F_{|T|}}(m;T)]\). The mark \(b\) differs from all shifts in \(I\). The constant of each term is the same as in the second moment (the mark does not enter \(\mathcal C\)), and the singular series is \(\mathfrak S(S\cup T\cup\{b\})\). Only \(S=T\) survives, and the counting gives \(\sum_j\|f_j\|^2\lambda\alpha_j=\lambda w\).

*A prime in \(I\).* \(\mathbb E_X(Z^2V_I)=L^{-1}\sum_{a\in I}\mathbb E_X[\vartheta(m+a)Z(m)^2]\). Where \(\vartheta(m+a)\ne0\), Lemma 3.1 rewrites \(Z(m)\); so

\[
\mathbb E_X[\vartheta(m+a)Z(m)^2]=\sum_{U,U'\subseteq I\setminus\{a\}}\mathbb E_X\bigl[\vartheta(m+a)D_{\widetilde F_{|U|}}(m;U)D_{\widetilde F_{|U'|}}(m;U')\bigr].
\]

These are marked moments with mark \(a\) and test functions \(\widetilde F_j\) of budget \(\tau\). By Lemma 1.2(3), the signed mixed derivative of \(\widetilde F_j\) is \(f_j+Tf_{j+1}\), which vanishes near the coordinate faces for \(j\ge1\). As in the second moment, only \(U=U'\) survives, with constant \(\|f_j+Tf_{j+1}\|^2\) for \(|U|=j\ge1\) and \(|f_0+Tf_1|^2\) for \(U=\varnothing\). The counting gives \(\sum_j\|f_j+Tf_{j+1}\|^2\lambda\alpha_j=v\).

*The detector.* Put \(q_X=\log(2X+2h)/L\to1\). For \(b\in J\) and \(X<m\le2X\):

\[
\frac{\vartheta(m+b)}L\le q_X\,D_G(m;b)^2,\qquad\Bigl(\frac{\vartheta(m+b)}L\Bigr)^2\le q_X\frac{\vartheta(m+b)}L .
\]

The left sides vanish unless \(m+b\) is prime, and the right sides are nonnegative. If \(m+b\) is prime, \(\vartheta(m+b)/L\le q_X\), and \(D_G(m;b)=G(0)-G(\log(m+b)/L)=1\) because \(\log(m+b)/L>1>\tau\). Expanding the square of \(V_J=L^{-1}\sum_{b\in J}\vartheta(m+b)\) into diagonal and off-diagonal terms and multiplying by \(Z^2\ge0\),

\[
\mathbb E_X(Z^2V_J^2)\le q_X\,\mathbb E_X(Z^2V_J)+q_X^2\sum_{\substack{b,c\in J\\b\ne c}}\mathbb E_X\bigl[Z^2D_G(m;b)^2D_G(m;c)^2\bigr].
\]

An off-diagonal term is a sum of unmarked moments of six factors. The shifts \(b\) and \(c\) lie outside \(I\) and each carries a fibre of two coordinates, one from each copy of \(D_G\). By (1.1) each such fibre contributes \(\int_0^\infty(-G'(y))^2dy=c_G\), and the subsets \(S,T\) from \(Z^2\) must again coincide. The constant for \(S=T\) of size \(j\) is \(c_G^2\|f_j\|^2\), and \(t=j+2\). The counting gives \(\sum_jc_G^2\|f_j\|^2\lambda^2\alpha_j=\lambda^2c_G^2w\). Together with \(\mathbb E_X(Z^2V_J)\to\lambda w\),

\[
\limsup_{X\to\infty}\mathbb E_X(Z^2V_J^2)\le\lambda w+\lambda^2c_G^2w=C_*w .\qquad\square
\]

The detector bound uses two primes in \(J\) only through the majorants \(D_G^2\), so no asymptotic formula with two prime marks is needed. Its constant does not depend on the family because the coefficients of \(w\) in both terms are \(\lambda\) and \(\lambda^2c_G^2\), whatever the \(f_j\) are.

## 5. Exercises

**Exercise 5.1.** Verify Lemma 1.2(1) for \(j=2\) by computing \(\partial_1\partial_2\int_{v_1}^\infty\int_{v_2}^\infty f(s_1,s_2)\,ds_2\,ds_1\).

**Exercise 5.2.** Suppose only one level is used: \(f_j=0\) for \(j\ne j_0\). Show that \(v\ge\lambda w\). So with a single level the weighted prime mass in \(I\) is at least the weighted prime mass in \(J\).

**Exercise 5.3.** Let \(k=1\). Show that \(w=f_0^2+\lambda\|f_1\|^2\) and \(v=\lambda\bigl((f_0+\int f_1)^2+\lambda\|f_1\|^2\bigr)\), and deduce

\[
\frac vw\ge\lambda\min\Bigl\{\frac14,\frac\lambda{\lambda+4\tau}\Bigr\}.
\]

(Use \((\int f_1)^2\le\tau\|f_1\|^2\).)

**Exercise 5.4.** Explain why \(\mathbb E_X(Z^2V_I)\) could not be computed by applying Theorem 1.1 of the correlations lesson directly to \(\vartheta(m+a)\,D_{F_{|S|}}(m;S)D_{F_{|T|}}(m;T)\) when \(a\in S\).

**Exercise 5.5.** Check the pointwise inequality \(\vartheta(m+b)/L\le q_XD_G(m;b)^2\) when \(m+b\) is composite with all prime factors larger than \(X^\tau\), and when \(m+b\) is composite with a small prime factor.

## 6. Solutions

**5.1.** \(\partial_1\) of \(\int_{v_1}^\infty g(s_1)\,ds_1\) is \(-g(v_1)\), with \(g(s_1)=\int_{v_2}^\infty f(s_1,s_2)ds_2\). Then \(\partial_2\) of \(-\int_{v_2}^\infty f(v_1,s_2)ds_2\) is \(f(v_1,v_2)\). So \((-1)^2\partial_1\partial_2F=f\).

**5.2.** Then \(w=\alpha_{j_0}\|f_{j_0}\|^2\), and \(v=\lambda\bigl(\alpha_{j_0}\|f_{j_0}\|^2+\alpha_{j_0-1}\|Tf_{j_0}\|^2\bigr)\ge\lambda w\), the second term coming from \(j=j_0-1\), where \(f_{j_0-1}=0\).

**5.3.** For \(k=1\), \(f_2=0\), so the \(j=1\) term of \(v\) is \(\lambda\alpha_1\|f_1\|^2\) and the \(j=0\) term is \(\lambda|f_0+Tf_1|^2\) with \(Tf_1=\int_0^\infty f_1\). Since \(f_1\) is supported in \((0,\tau)\), Cauchy–Schwarz gives \(c^2\le\tau\|f_1\|^2\) for \(c=\int f_1\). If \(|f_0|\le2|c|\), then \(w\le(4\tau+\lambda)\|f_1\|^2\) and \(v\ge\lambda^2\|f_1\|^2\ge\lambda^2w/(\lambda+4\tau)\). If \(|f_0|>2|c|\), then \((f_0+c)^2\ge f_0^2/4\) and \(v\ge\lambda(f_0^2/4+\lambda\|f_1\|^2)\ge\lambda w/4\).

**5.4.** When \(a\in S\), the mark \(a\) coincides with a divisor shift, which Theorem 1.1 of the correlations lesson excludes. On the prime event the divisor coordinate at \(a\) is not small: \(m+a\) has the divisor \(m+a\) itself. Lemma 3.1 removes this coordinate exactly, and the theorem is applied afterwards.

**5.5.** If \(m+b\) is composite, \(\vartheta(m+b)=0\) and the right side is a square. Nothing else is needed: the inequality is trivial at composites, whatever \(D_G\) is.

## References

- [OpenAI-Gaps] OpenAI, Positive lower density of large prime gaps, preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026
- [GY 2005] D. A. Goldston, C. Y. Yıldırım, Small gaps between primes I, arXiv:math/0504336 (2005); published as Higher correlations of divisor sums related to primes III: small gaps between primes, Proceedings of the London Mathematical Society 95 (2007), 653–686. https://arxiv.org/abs/math/0504336
- [Maynard] J. Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), 383–413. https://arxiv.org/abs/1311.4600
