# The sine product and cardinal functions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The normalized statement of [Shells and Gaussian duality](shells-and-gaussian-duality.md) asks for functions \(H_1,H_2\) of a real variable \(s\) with prescribed values at the *nodes*, the positive integers congruent to \(0,1,3,4,7\) or \(9\) modulo \(12\); in the construction of [OpenAI-T] the first derivatives at the nodes are prescribed as well. This lesson builds the functions from which \(H_1\) and \(H_2\) are assembled there: entire functions whose value and derivative at every node can be chosen freely.

- The *sine product* \(P\) is a trigonometric polynomial with a double zero at every node and no other real zeros. Its thirteen Fourier coefficients and its leading behaviour at the nodes are computed exactly (Proposition 1.1, Proposition 1.2).
- For a summable list of numbers \(C,c_n,d_n\) the *cardinal function*
\[
\begin{aligned}
p(s)=P(s)\Bigl(C&+\sum_n\frac{c_n}{(s-n)^2}\\
&+\sum_n\frac{d_n}{s-n}\Bigr)
\end{aligned}
\]
is entire, and \(c_n\), \(d_n\) determine its value and its derivative at the node \(n\) (Theorem 2.2).
- A cardinal function is a superposition of the exponentials \(e^{i\pi ts}\) with frequencies \(-1\le t\le1\), with total weight at most \(25|C|+36\sum(|c_n|+|d_n|)\) (Theorem 2.2). This is what makes its Fourier transform computable after multiplication by a Gaussian, and it gives bounds for all derivatives that do not depend on where the nonzero coefficients sit (Corollary 2.3).

The lesson follows [OpenAI-T, Section 2, the parts on the sine product and on the spectral realization]. A squared sine multiplied by terms with double poles, which carry the values, and terms with simple poles, which carry the derivatives, is the form of the interpolation series that H. Cohn and A. Kumar use for the one-dimensional case of the linear programming bound [Cohn–Kumar, Section 9]; there the nodes are all integers, here six residue classes. The lesson uses power series and integrals depending on a complex parameter (core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50)).

## 1. The sine product

Let \(L=\{0,1,3,4,7,9\}\), let \(\mathcal Z\) be the set of integers congruent modulo \(12\) to an element of \(L\), \(\mathcal N\) the set of positive elements of \(\mathcal Z\), and \(\mathcal N_0=\{0\}\cup\mathcal N\). For \(s\in\mathbb C\) let
\[
P(s)=\prod_{a\in L}\Bigl(2\sin\frac{\pi(s-a)}{12}\Bigr)^2 .
\]
On the real axis \(P\) is nonnegative and has period \(12\). The factor with index \(a\) vanishes exactly at the points of \(a+12\mathbb Z\), to second order. So the real zeros of \(P\) are the points of \(\mathcal Z\), and each is a double zero.

Let \(b=\sqrt3/2\) and \(t_l=l/6\) for \(-6\le l\le6\).

**Proposition 1.1.** For all \(s\in\mathbb C\),
\[
P(s)=\sum_{l=-6}^6P_l\,e^{i\pi t_ls},
\]
with \(P_{-l}=\overline{P_l}\) and
\[
\begin{gathered}
P_0=5,\quad P_1=-1+2ib,\\
P_2=1+2ib,\quad P_3=-2,\\
P_4=-\tfrac12+ib,\quad P_5=-1-2ib,\\
P_6=1 .
\end{gathered}
\]
Consequently \(|P_1|,\dots,|P_6|\) are \(2,2,2,1,2,1\), and
\[
\begin{gathered}
|P_0|+2\sum_{l=1}^6|P_l|=25,\\
\sum_{l=1}^6t_l|P_l|=\frac{16}3,\\
\sum_{l=1}^6t_l^2|P_l|=\frac{65}{18}.
\end{gathered}
\]

**Proof.** Let \(\omega=e^{i\pi s/6}\) and \(\varepsilon_a=e^{i\pi a/6}\). Then
\[
\begin{aligned}
&\Bigl(2\sin\frac{\pi(s-a)}{12}\Bigr)^2\\
&\quad=2-\omega\varepsilon_a^{-1}-\omega^{-1}\varepsilon_a\\
&\quad=-\omega^{-1}\varepsilon_a^{-1}(\omega-\varepsilon_a)^2 .
\end{aligned}
\]
The product of the six numbers \(\varepsilon_a\) is \(e^{i\pi\cdot24/6}=1\), since the elements of \(L\) add up to \(24\). So
\[
\begin{gathered}
P=\omega^{-6}R(\omega)^2,\\
R(\omega)=\prod_{a\in L}(\omega-\varepsilon_a).
\end{gathered}
\]
Let \(\theta=e^{i\pi/3}=\tfrac12+ib\); then \(\theta^2=\theta-1\) and \(\theta^3=-1\). The six numbers \(\varepsilon_a\) are \(1\), \(\zeta\), \(i\), \(\theta^2\), \(-\zeta\), \(-i\), with \(\zeta=e^{i\pi/6}\), \(\zeta^2=\theta\). Pairing them,
\[
\begin{gathered}
(\omega-\zeta)(\omega+\zeta)=\omega^2-\theta,\\
(\omega-i)(\omega+i)=\omega^2+1,\\
(\omega-1)(\omega-\theta^2)=\omega^2-\theta\omega+\theta^2 ,
\end{gathered}
\]
the last because \(1+\theta^2=\theta\). Multiplying out and using \(\theta^2=\theta-1\), \(\theta^3=-1\),
\[
\begin{aligned}
R(\omega)&=(\omega^4+(1-\theta)\omega^2-\theta)\\
&\qquad\cdot(\omega^2-\theta\omega+\theta^2)\\
&=\omega^6-\theta\omega^5-\omega^3+\theta^2\omega+1 .
\end{aligned}
\]
Squaring, with \(\theta^4=-\theta\):
\[
\begin{aligned}
R(\omega)^2={}&\omega^{12}-2\theta\omega^{11}+\theta^2\omega^{10}\\
&-2\omega^9+2\theta\omega^8+2\theta^2\omega^7\\
&+5\omega^6-2\theta\omega^5-2\theta^2\omega^4\\
&-2\omega^3-\theta\omega^2+2\theta^2\omega+1 .
\end{aligned}
\]
The coefficient \(P_l\) is the coefficient of \(\omega^{l+6}\). With \(\theta=\tfrac12+ib\) and \(\theta^2=-\tfrac12+ib\) this gives the list, and \(P_{-l}=\overline{P_l}\) for every \(l\). The absolute values are \(|2\theta|=|2\theta^2|=2\) and \(|\theta^2|=1\). The three sums are \(5+2\cdot10\), \((2+4+6+4+10+6)/6\) and \((2+8+18+16+50+36)/36\). \(\blacksquare\)

For \(n\in\mathcal Z\) let \(Q_n\) and \(D_n\) be the numbers with, as \(u\to0\),
\[
P(n+u)=Q_nu^2\bigl(1+D_nu+O(u^2)\bigr).
\]
They exist because \(n\) is a double zero, and by periodicity they depend only on the residue \(a\in L\) of \(n\) modulo \(12\).

**Proposition 1.2.** For \(n\) with residue \(a\),
\[
\begin{gathered}
Q_n=\Bigl(\frac\pi6\Bigr)^2\prod_{d\in L,\,d\ne a}\Bigl(2\sin\frac{\pi(a-d)}{12}\Bigr)^2,\\
D_n=\frac\pi6\sum_{d\in L,\,d\ne a}\cot\frac{\pi(a-d)}{12}.
\end{gathered}
\]
The values are:

- \(a=0\): \(Q=\pi^2/3\), \(D=-7\pi\sqrt3/18\); and \(a=4\): \(Q=\pi^2/3\), \(D=7\pi\sqrt3/18\);
- \(a=1\): \(Q=\tfrac23\pi^2(2-\sqrt3)\), \(D=\pi(3+\sqrt3)/18\); and \(a=3\): the same \(Q\), \(D=-\pi(3+\sqrt3)/18\);
- \(a=7\): \(Q=\tfrac23\pi^2(2+\sqrt3)\), \(D=-\pi(3-\sqrt3)/18\); and \(a=9\): the same \(Q\), \(D=\pi(3-\sqrt3)/18\).

In particular \(Q_n>7/4\) and \(|D_n|<53/25\) for all \(n\).

**Proof.** In \(P(a+u)\) the factor with index \(a\) is \((2\sin(\pi u/12))^2=(\pi/6)^2u^2(1+O(u^2))\). The product \(g(u)\) of the other five factors has \(g(0)\ne0\). Each of them is the square of a sine with argument \(\pi(a+u-d)/12\), so its logarithmic derivative at \(u=0\) is \(2\cdot\tfrac\pi{12}\) times a cotangent, and
\[
\frac{g'(0)}{g(0)}=\frac\pi6\sum_{d\ne a}\cot\frac{\pi(a-d)}{12}.
\]
Since \(P(a+u)=(\pi/6)^2u^2g(u)(1+O(u^2))\), this gives the two formulas.

The map \(s\mapsto4-s\) permutes the residues of \(L\) modulo \(12\): it exchanges \(0\) and \(4\), \(1\) and \(3\), \(7\) and \(9\). So \(P(4-s)=P(s)\), and therefore \(Q_{4-a}=Q_a\) and \(D_{4-a}=-D_a\). It remains to treat \(a=0,1,7\). We use \((2\sin x)^2=2-2\cos2x\), \(\cot(\pi/12)=2+\sqrt3\) and \(\cot(7\pi/12)=-(2-\sqrt3)\).

*\(a=0\).* The differences \(a-d\) are \(-1,-3,-4,-7,-9\). The numbers \((2\sin(\pi m/12))^2\) for \(m=1,3,4,7,9\) are \(2-\sqrt3\), \(2\), \(3\), \(2+\sqrt3\), \(2\), with product \(12\). So \(Q=12\pi^2/36\). The cotangents of \(-\pi m/12\) are \(-(2+\sqrt3)\), \(-1\), \(-1/\sqrt3\), \(2-\sqrt3\), \(1\), with sum \(-2\sqrt3-1/\sqrt3=-7/\sqrt3\). So \(D=-7\pi/(6\sqrt3)\).

*\(a=1\).* The differences are \(1,-2,-3,-6,-8\). The squares are \(2-\sqrt3\), \(1\), \(2\), \(4\), \(3\), with product \(24(2-\sqrt3)\). The cotangents are \(2+\sqrt3\), \(-\sqrt3\), \(-1\), \(0\), \(1/\sqrt3\), with sum \(1+1/\sqrt3\). So \(D=\pi(\sqrt3+1)/(6\sqrt3)=\pi(3+\sqrt3)/18\).

*\(a=7\).* The differences are \(7,6,4,3,-2\). The squares are \(2+\sqrt3\), \(4\), \(3\), \(2\), \(1\), with product \(24(2+\sqrt3)\). The cotangents are \(-(2-\sqrt3)\), \(0\), \(1/\sqrt3\), \(1\), \(-\sqrt3\), with sum \(-1+1/\sqrt3\). So \(D=-\pi(3-\sqrt3)/18\).

*The bounds.* The smallest \(Q\) is \(\tfrac23\pi^2(2-\sqrt3)\). With \(\pi>3.14\) and \(\sqrt3<1.7321\) it is more than \(\tfrac23\cdot9.8596\cdot0.2679>1.76\). The largest \(|D|\) is \(7\pi\sqrt3/18\), which is less than \(7\cdot3.1416\cdot1.7321/18<2.117\). \(\blacksquare\)

## 2. Cardinal functions

A *coefficient list* \(\mathbf a\) consists of a real number \(C\) and real numbers \(c_n,d_n\) for \(n\in\mathcal N_0\) with
\[
W=\sum_{n\in\mathcal N_0}(|c_n|+|d_n|)<\infty .
\]
For \(s\in\mathbb C\) outside \(\mathcal N_0\) let
\[
\begin{aligned}
p(s)=P(s)\Bigl(C&+\sum_{n\in\mathcal N_0}\frac{c_n}{(s-n)^2}\\
&+\sum_{n\in\mathcal N_0}\frac{d_n}{s-n}\Bigr).
\end{aligned}
\]
Both series converge absolutely, because \(|s-n|\) is bounded below for \(n\in\mathcal N_0\). We call \(p=p_{\mathbf a}\) the *cardinal function* of the list.

**Lemma 2.1.** For real \(\tau\) and complex \(u\ne0\),
\[
\begin{gathered}
\frac{e^{i\pi\tau u}-1}u=i\pi\int_0^\tau e^{i\pi tu}\,dt,\\
\frac{e^{i\pi\tau u}-1-i\pi\tau u}{u^2}\\
=-\pi^2\int_0^\tau(\tau-t)\,e^{i\pi tu}\,dt .
\end{gathered}
\]
Here \(\int_0^\tau\) means \(-\int_\tau^0\) when \(\tau<0\).

**Proof.** The first is the integral of the exponential. For the second, both sides vanish at \(\tau=0\), and their derivatives in \(\tau\) are \(i\pi(e^{i\pi\tau u}-1)/u\) and \(-\pi^2\int_0^\tau e^{i\pi tu}\,dt\), which agree by the first. \(\blacksquare\)

**Theorem 2.2.** Let \(\mathbf a\) be a coefficient list.

1. There is an integrable function \(m\colon[-1,1]\to\mathbb C\) with
\[
\int_{-1}^1|m(t)|\,dt\le36\,W
\]
such that for all \(s\) outside \(\mathcal N_0\)
\[
p(s)=C\,P(s)+\int_{-1}^1m(t)\,e^{i\pi ts}\,dt .
\]
2. The right side is an entire function of \(s\). So \(p\) extends to an entire function; it is real on the real axis.
3. For every \(n\in\mathcal N_0\),
\[
\begin{gathered}
p(n)=Q_nc_n,\\
p'(n)=Q_n(d_n+D_nc_n).
\end{gathered}
\]

**Proof.** *One node.* Fix \(n\in\mathcal N_0\) and write \(u=s-n\). By Proposition 1.1, \(P(s)=\sum_l\pi_le^{i\pi t_lu}\) with \(\pi_l=P_le^{i\pi t_ln}\). Since \(P(n)=P'(n)=0\),
\[
\sum_l\pi_l=0,\qquad\sum_l\pi_lt_l=0 .
\]
So constants and linear terms may be subtracted, and by Lemma 2.1
\[
\begin{aligned}
&\frac{P(s)}{s-n}=\sum_l\pi_l\,\frac{e^{i\pi t_lu}-1}u\\
&\quad=i\pi\sum_l\pi_l\int_0^{t_l}e^{i\pi tu}\,dt,\\
&\frac{P(s)}{(s-n)^2}=\sum_l\pi_l\,\frac{e^{i\pi t_lu}-1-i\pi t_lu}{u^2}\\
&\quad=-\pi^2\sum_l\pi_l\int_0^{t_l}(t_l-t)\,e^{i\pi tu}\,dt .
\end{aligned}
\]
Since \(e^{i\pi tu}=e^{-i\pi tn}e^{i\pi ts}\) and \(|t_l|\le1\), these are integrals \(\int_{-1}^1m(t)e^{i\pi ts}\,dt\) with bounded functions \(m=m_n'\) and \(m=m_n''\), and, because \(|\pi_l|=|P_l|\) and \(|e^{-i\pi tn}|=1\),
\[
\begin{aligned}
\int|m_n'|&\le\pi\sum_l|P_l||t_l|=2\pi\cdot\frac{16}3<36,\\
\int|m_n''|&\le\pi^2\sum_l|P_l|\frac{t_l^2}2=\pi^2\cdot\frac{65}{18}<36 .
\end{aligned}
\]
The numerical values are \(33.52\) and \(35.65\), rounded up.

*All nodes.* Let \(m=\sum_n(c_nm_n''+d_nm_n')\). The series converges in the space of integrable functions on \([-1,1]\), with \(\int|m|\le36W\). For \(s\) outside \(\mathcal N_0\), integrating term by term against the bounded function \(e^{i\pi ts}\) gives (1).

(2) For \(|t|\le1\) the partial sums of the series \(e^{i\pi ts}=\sum_j(i\pi ts)^j/j!\) are bounded by \(e^{\pi|s|}\). By dominated convergence \(\int m(t)e^{i\pi ts}\,dt=\sum_ja_js^j\) with \(a_j=\tfrac{(i\pi)^j}{j!}\int m(t)t^j\,dt\), and \(|a_j|\le\pi^j\int|m|/j!\). So the integral is the sum of a power series that converges for all \(s\): it is an entire function. Differentiating the series term by term gives the series, obtained in the same way, of \(\int m(t)(i\pi t)^je^{i\pi ts}\,dt\); so the derivatives are obtained by differentiating under the integral sign. The trigonometric polynomial \(P\) is entire. For real \(s\) outside \(\mathcal N_0\) all terms of the series defining \(p\) are real; by continuity \(p\) is real on the real axis.

(3) Suppose first that only finitely many \(c_k,d_k\) are different from zero. Near \(n\), with \(u=s-n\),
\[
\begin{aligned}
&c_n\frac{P(s)}{u^2}+d_n\frac{P(s)}u\\
&\quad=Q_nc_n(1+D_nu)+Q_nd_nu+O(u^2),
\end{aligned}
\]
while \(CP(s)\) and the terms with index \(k\ne n\) are \(O(u^2)\), because \(P\) has a double zero at \(n\). This gives the two formulas. In general let \(\mathbf a_N\) be the list in which \(c_k,d_k\) are replaced by \(0\) for \(k>N\), with cardinal function \(p_N\) and function \(m_N\) as in (1). Then, at real \(s\),
\[
\begin{aligned}
&|p(s)-p_N(s)|+|p'(s)-p_N'(s)|\\
&\quad\le(1+\pi)\int|m-m_N| ,
\end{aligned}
\]
and the right side is at most \(36(1+\pi)\sum_{k>N}(|c_k|+|d_k|)\to0\). So the formulas pass to the limit. \(\blacksquare\)

So the values \(p(n)\) and the derivatives \(p'(n)\) at the nodes can be prescribed independently, by solving for \(c_n=p(n)/Q_n\) and \(d_n=p'(n)/Q_n-D_nc_n\), as long as the resulting list is summable. The three numbers \(C,c_0,d_0\) do not affect the values and derivatives at the positive nodes.

**Corollary 2.3.** Let \(V=25|C|+36W\). For every integer \(j\ge0\) and every real \(s\),
\[
|p^{(j)}(s)|\le\pi^j\,V .
\]

**Proof.** By Proposition 1.1, \(|P^{(j)}(s)|\le\sum_l|P_l|(\pi|t_l|)^j\le25\pi^j\). The \(j\)-th derivative of the integral is \(\int m(t)(i\pi t)^je^{i\pi ts}\,dt\), of absolute value at most \(\pi^j\int|m|\). \(\blacksquare\)

The bound does not depend on which nodes carry the nonzero coefficients. A list concentrated at very distant nodes gives a cardinal function that is as well controlled, on the whole real axis, as a list concentrated near \(0\).

## 3. Exercises

**3.1.** Check Proposition 1.1 at \(s=0\) and at \(s=6\): compute \(P(0)\) and \(P(6)\) from the definition and from the Fourier coefficients.

**3.2.** Show that \(P(s+6)\ne P(s)\) in general, although the sets \(L\) and \(L+6\) have four residues modulo \(12\) in common.

**3.3.** Let \(p\) be the cardinal function of the list with \(c_1=1\) and all other entries \(0\). Determine \(p(n)\) and \(p'(n)\) for all \(n\in\mathcal N_0\), and show \(|p(s)|\le36\) for all real \(s\).

**3.4.** Show that a coefficient list is determined by its cardinal function: two lists with the same cardinal function are equal.

## 4. Solutions

**3.1.** \(P(0)=0\) because \(0\in L\). From the coefficients: \(P(0)=\sum_lP_l\) is \(5\) plus twice the sum of the real parts of \(P_1,\dots,P_6\). These real parts are \(-1,1,-2,-\tfrac12,-1,1\), with sum \(-\tfrac52\); so \(P(0)=5-5=0\). At \(s=6\): \(e^{i\pi t_l6}=(-1)^l\), so the terms with odd \(l\) change sign. The real parts are then \(1,1,2,-\tfrac12,1,1\), with sum \(\tfrac{11}2\); so \(P(6)=5+11=16\). From the definition, the six factors are \((2\sin(\pi(6-a)/12))^2\) for \(a=0,1,3,4,7,9\): \(4\), \(2+\sqrt3\), \(2\), \(1\), \(2-\sqrt3\), \(2\); the product is \(4\cdot1\cdot2\cdot1\cdot2=16\).

**3.2.** \(P(0)=0\), but \(P(6)=16\) by Exercise 3.1. The zero set \(\mathcal Z\) is not invariant under the shift by \(6\): \(0\in\mathcal Z\) and \(6\notin\mathcal Z\).

**3.3.** By Theorem 2.2(3), \(p(1)=Q_1=\tfrac23\pi^2(2-\sqrt3)\) and \(p'(1)=Q_1D_1\); at all other nodes \(p\) and \(p'\) vanish. By Corollary 2.3 with \(C=0\) and \(W=1\), \(|p(s)|\le36\).

**3.4.** Let \(p\) be the common cardinal function. By Theorem 2.2(3), both lists have \(c_n=p(n)/Q_n\) and \(d_n=p'(n)/Q_n-D_nc_n\) for every \(n\in\mathcal N_0\). So the difference of the two cardinal functions is \((C-C')P\), with \(C,C'\) the first entries of the lists. It is zero and \(P\) is not the zero function, so \(C=C'\).

## References

- [Cohn–Kumar] H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, Journal of the American Mathematical Society 20 (2007), Section 9. https://arxiv.org/abs/math/0607446
- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
