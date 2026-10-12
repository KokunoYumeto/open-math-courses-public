# A positive quadrature rule

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A cardinal function \(p\) and its transformed function \(K_p\) are given by integrals over the frequencies \(t\in[-1,1]\) ([The sine product and cardinal functions](the-sine-product-and-cardinal-functions.md), [Gaussian damping and Fourier pairs](gaussian-damping-and-fourier-pairs.md)). The construction of the functions \(H_1,H_2\) of the normalized statement needs explicit numbers: values and derivatives of \(p\) and \(K_p\) at many points, for many coefficient lists. This lesson replaces the integrals by finite sums with \(2304\) terms and proves that every quantity that is needed changes by less than \(10^{-31}\).

- The rule of Fejér with \(N\) points integrates polynomials of degree less than \(N\) exactly, and its weights are positive (Theorem 1.2).
- For a function that is holomorphic and bounded by \(A\) on a disc of twice the radius of the interval, the error of the rule is at most \(4A\cdot2^{-N}\) (Proposition 2.1).
- For \(N=384\) on each of six frequency intervals, the values and all scaled derivatives of \(p\) and \(K_p\) on \([0,168]\), for lists with one entry \(1\) at a node up to \(168\), are reproduced with an error below \(10^{-31}\) (Theorem 3.3).

The lesson follows [OpenAI-T, Section 3, the part on the positive rule for the density integrals]. The rule is the first rule of Fejér, with the formula for the weights as given by J. Waldvogel [Waldvogel, formula (2.3)], divided by two. The lesson uses the estimate of Cauchy for Taylor coefficients (core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50)).

## 1. The rule and its weights

Let \(N\ge2\) be an even integer. For \(v=0,1,\dots,N-1\) let
\[
\begin{gathered}
\theta_v=\frac{\pi(v+\frac12)}N,\qquad x_v=\cos\theta_v,\\
o_v=\frac1N\Bigl(1-2\sum_{a=1}^{N/2-1}\frac{\cos(2a\theta_v)}{4a^2-1}\Bigr).
\end{gathered}
\]
The points \(x_v\) lie in the open interval \((-1,1)\).

**Lemma 1.1.** Let \(l\) be an integer with \(1\le l\le2N-1\). Then \(\sum_{v=0}^{N-1}\cos(l\theta_v)=0\).

**Proof.** For real \(\tau\),
\[
\begin{aligned}
&2\sin\frac\tau2\,\cos((v+\tfrac12)\tau)\\
&\quad=\sin((v+1)\tau)-\sin(v\tau).
\end{aligned}
\]
Summing over \(v\),
\[
2\sin\frac\tau2\sum_{v=0}^{N-1}\cos((v+\tfrac12)\tau)=\sin(N\tau).
\]
For \(\tau=l\pi/N\) the right side is \(\sin(l\pi)=0\), and \(\sin(\tau/2)=\sin(l\pi/(2N))\ne0\) because \(0<l\pi/(2N)<\pi\). \(\blacksquare\)

**Theorem 1.2.**

1. For every polynomial \(f\) of degree at most \(N-1\),
\[
\sum_{v=0}^{N-1}o_vf(x_v)=\frac12\int_{-1}^1f(x)\,dx .
\]
2. \(\sum_vo_v=1\), and \(o_v\ge\dfrac1{N(N-1)}\) for every \(v\).

**Proof.** (1) Let \(C_l\) be the polynomial of degree \(l\) with \(C_l(\cos\theta)=\cos(l\theta)\); it exists by the recursion
\[
\begin{aligned}
&\cos((l+1)\theta)\\
&\quad=2\cos\theta\cos(l\theta)-\cos((l-1)\theta).
\end{aligned}
\]
The polynomials \(C_0,\dots,C_{N-1}\) span the polynomials of degree at most \(N-1\). So it is enough to prove (1) for \(f=C_l\), \(0\le l\le N-1\).

*The right side.* With \(x=\cos\theta\),
\[
\begin{aligned}
&\frac12\int_{-1}^1C_l(x)\,dx\\
&\quad=\frac12\int_0^\pi\cos(l\theta)\sin\theta\,d\theta .
\end{aligned}
\]
Here
\[
\begin{aligned}
&\cos(l\theta)\sin\theta\\
&\quad=\tfrac12\sin((l+1)\theta)-\tfrac12\sin((l-1)\theta),
\end{aligned}
\]
and \(\int_0^\pi\sin(k\theta)\,d\theta\) is \(2/k\) for odd \(k\) and \(0\) for even \(k\). So the value is \(1\) for \(l=0\), it is \(0\) for odd \(l\), and for even \(l\ge2\) it is
\[
\frac12\Bigl(\frac1{l+1}-\frac1{l-1}\Bigr)=\frac1{1-l^2}.
\]

*The left side.* Let \(0\le l\le N-1\) and \(1\le a\le N/2-1\). Then
\[
\begin{aligned}
&\cos(l\theta_v)\cos(2a\theta_v)\\
&\quad=\tfrac12\cos((l+2a)\theta_v)\\
&\qquad+\tfrac12\cos((l-2a)\theta_v),
\end{aligned}
\]
and \(1\le l+2a\le2N-1\), \(|l-2a|\le2N-1\). By Lemma 1.1 the sum over \(v\) of the first term is \(0\), and the sum of the second term is \(0\) unless \(l=2a\), when it is \(N/2\). So the number
\[
\kappa_{l,a}=\frac1N\sum_v\cos(l\theta_v)\cos(2a\theta_v)
\]
is \(\tfrac12\) if \(l=2a\) and \(0\) otherwise. Now \(\sum_vo_vC_l(x_v)=\sum_vo_v\cos(l\theta_v)\) is, by the definition of \(o_v\),
\[
\frac1N\sum_v\cos(l\theta_v)-2\sum_{a=1}^{N/2-1}\frac{\kappa_{l,a}}{4a^2-1}.
\]
For \(l=0\) the first term is \(1\) and the second is \(0\). For odd \(l\) both are \(0\). For even \(l\) with \(2\le l\le N-2\) the first is \(0\), and the second is \(-2\cdot\tfrac1{l^2-1}\cdot\tfrac12\), from \(a=l/2\). These are the values of the right side.

(2) The case \(l=0\) of (1) is \(\sum_vo_v=1\). Further
\[
\begin{aligned}
&\sum_{a=1}^{N/2-1}\frac2{4a^2-1}\\
&\quad=\sum_{a=1}^{N/2-1}\Bigl(\frac1{2a-1}-\frac1{2a+1}\Bigr)\\
&\quad=1-\frac1{N-1}.
\end{aligned}
\]
Since every cosine is at most \(1\), \(No_v\ge1-(1-\tfrac1{N-1})=\tfrac1{N-1}\). \(\blacksquare\)

So the rule \(f\mapsto\sum_vo_vf(x_v)\) approximates the average of \(f\) over \([-1,1]\), and it is a positive functional of total mass \(1\): \(|\sum_vo_vf(x_v)|\le\max|f|\).

## 2. The error for holomorphic functions

For an interval with midpoint \(u\) and half-length \(\rho\) the rule is transported by \(t=u+\rho x\).

**Proposition 2.1.** Let \(u\) be real, \(\rho>0\), and let \(g\) be holomorphic on an open set containing the closed disc \(|t-u|\le2\rho\), with \(|g(t)|\le A\) on this disc. Let
\[
\begin{gathered}
\mathcal A=\frac1{2\rho}\int_{u-\rho}^{u+\rho}g(t)\,dt,\\
\mathcal R=\sum_{v=0}^{N-1}o_v\,g(u+\rho x_v)
\end{gathered}
\]
be the average of \(g\) over the interval and the value of the rule. Then
\[
|\mathcal A-\mathcal R|\le4A\cdot2^{-N}.
\]

**Proof.** Let \(g(t)=\sum_ra_r(t-u)^r\) be the Taylor series at \(u\). By the estimate of Cauchy on the circle of radius \(2\rho\), \(|a_r|\le A/(2\rho)^r\). Let \(g_0\) be the sum of the terms with \(r\le N-1\) and \(g_1=g-g_0\). For real \(t\) with \(|t-u|\le\rho\),
\[
|g_1(t)|\le A\sum_{r\ge N}2^{-r}=2A\cdot2^{-N}.
\]
The function \(x\mapsto g_0(u+\rho x)\) is a polynomial of degree at most \(N-1\), so by Theorem 1.2(1) the rule gives its average exactly. For \(g_1\), both the average and the rule are at most \(\max|g_1|\) in absolute value, the rule by Theorem 1.2(2). So the two differ by at most \(2\cdot2A\cdot2^{-N}\). \(\blacksquare\)

The positivity of the weights is used here: without it the rule applied to \(g_1\) could only be bounded by \(\sum_v|o_v|\max|g_1|\).

## 3. The rule for the spectral integrals

Let \(\mathbf a\) be a coefficient list with finitely many nonzero entries \(C,c_n,d_n\), let \(p\) be its cardinal function, \(K=K_p\) its transformed function, and \(m\) the function on \([-1,1]\) of [The transformed function at distant nodes](the-transformed-function-at-distant-nodes.md), Section 2. With \(t_l=l/6\), \(\pi_l=P_le^{i\pi t_ln}\), and \(j\) the index with \(t_{j-1}<t<t_j\), \(1\le j\le6\), it is \(m=\sum_n(c_nm_n''+d_nm_n')\) with
\[
\begin{aligned}
m_n'(t)&=i\pi\,e^{-i\pi tn}\sum_{l=j}^6\pi_l,\\
m_n''(t)&=-\pi^2e^{-i\pi tn}\sum_{l=j}^6\pi_l\,(t_l-t).
\end{aligned}
\]
On each interval \(I_j=(t_{j-1},t_j)\) these formulas define entire functions of \(t\).

**Lemma 3.1.** For \(0<t<1\) and real \(s,y\), and every integer \(a\ge0\): \(m(-t)=\overline{m(t)}\), and
\[
\begin{aligned}
\frac{y^a}{a!}p^{(a)}(s)={}&C\,\frac{y^a}{a!}P^{(a)}(s)\\
&+2\operatorname{Re}\int_0^1m(t)\,\Phi_a(t)\,dt,\\
\frac{y^a}{a!}K^{(a)}(s)={}&C\sum_{l=-6}^6P_l\,\Psi_a(t_l)\\
&+2\operatorname{Re}\int_0^1m(t)\,\Psi_a(t)\,dt,
\end{aligned}
\]
where
\[
\begin{aligned}
\Phi_a(t)&=e^{i\pi ts}\,\frac{(i\pi ty)^a}{a!},\\
\Psi_a(t)&=\lambda(t)\,e^{i\pi z(t)s}\,\frac{(i\pi z(t)y)^a}{a!}.
\end{aligned}
\]

**Proof.** For \(-1<t<0\) the functions \(m_n',m_n''\) are given by the sums over the indices \(l\) with \(t_l<t\), with the opposite sign. Since \(P_{-l}=\overline{P_l}\) and \(t_{-l}=-t_l\), we have \(\pi_{-l}=\overline{\pi_l}\), and the formulas give \(m_n'(-t)=\overline{m_n'(t)}\) and \(m_n''(-t)=\overline{m_n''(t)}\). The entries of the list are real, so \(m(-t)=\overline{m(t)}\).

The derivatives of \(p\) and \(K\) are obtained by differentiating under the integral sign (Lemma 3.1 of the lesson on Gaussian damping), which gives the integrals of \(m\Phi_a\) and \(m\Psi_a\) over \([-1,1]\). For real \(s\) and \(y\), \(\Phi_a(-t)=\overline{\Phi_a(t)}\). Also \(\lambda(-t)=\overline{\lambda(t)}\) and \(z(-t)=-\overline{z(t)}\) by the definitions, hence \(\Psi_a(-t)=\overline{\Psi_a(t)}\). So the integrals over \([-1,0]\) are the complex conjugates of those over \([0,1]\). \(\blacksquare\)

Now fix \(N=384\), with the points \(x_v\) and weights \(o_v\) of Section 1. The interval \(I_j\) has the midpoint \(u_j=(2j-1)/12\) and the half-length \(1/12\). For \(1\le j\le6\) and \(0\le v<N\) let
\[
\tau_{jv}=u_j+\frac{x_v}{12}.
\]
For a function \(g\) on \((0,1)\) define
\[
\mathcal Q(g)=\sum_{j=1}^6\sum_{v=0}^{N-1}\frac{o_v}6\,g(\tau_{jv}).
\]
The *quadrature form* of \(\tfrac{y^a}{a!}p^{(a)}(s)\) or \(\tfrac{y^a}{a!}K^{(a)}(s)\) is the expression of Lemma 3.1 with \(\int_0^1m\Phi_a\,dt\) replaced by \(\mathcal Q(m\Phi_a)\), respectively \(\int_0^1m\Psi_a\,dt\) by \(\mathcal Q(m\Psi_a)\). The terms with the factor \(C\) are not changed. The quadrature forms are finite sums, with \(6N=2304\) points.

**Lemma 3.2.** Let \(w,a\) be complex numbers and \(\rho>0\) with \(|w-a|\le\rho<|a|\). Then
\[
\Bigl|\frac1w-\frac{\overline a}{|a|^2-\rho^2}\Bigr|\le\frac\rho{|a|^2-\rho^2}.
\]

**Proof.** Let \(e=|a|^2-\rho^2>0\). The left side is \(|e-\overline aw|/(e|w|)\), so the claim is \(|e-\overline aw|^2\le\rho^2|w|^2\). Now
\[
\begin{aligned}
&|e-\overline aw|^2-\rho^2|w|^2\\
&\quad=e^2-2e\operatorname{Re}(\overline aw)+(|a|^2-\rho^2)|w|^2\\
&\quad=e\,\bigl(|a|^2-\rho^2-2\operatorname{Re}(\overline aw)+|w|^2\bigr)\\
&\quad=e\,\bigl(|w-a|^2-\rho^2\bigr)\le0 .
\end{aligned}
\]
\(\blacksquare\)

**Theorem 3.3.** Let \(M=168\). Let \(\mathbf a\) be a list with exactly one nonzero entry, equal to \(1\): the entry \(C\), or \(c_n\) or \(d_n\) for a node \(n\in\mathcal N_0\) with \(n\le M\). Let \(a\ge0\) be an integer, and \(s,y\) real with \(0\le s\le M\) and \(|y|\le3/2\). Then each of
\[
\frac{y^a}{a!}p^{(a)}(s),\qquad\frac{y^a}{a!}K^{(a)}(s)
\]
differs from its quadrature form by less than \(10^{-31}\).

**Proof.** If the entry is \(C\), then \(m=0\) and nothing is changed. Let the entry be \(c_n\) or \(d_n\). Fix \(j\), and let \(t\) be a complex number in the disc \(|t-u_j|\le1/6\), which has twice the radius of the interval \(I_j\). We bound the functions that occur, extended to this disc by their formulas.

*The frequency.* \(|t|\le\tfrac{11}{12}+\tfrac16<1.1\) and \(|\operatorname{Im}t|\le\tfrac16\).

*The functions \(\lambda\) and \(z\).* Recall \(\lambda(t)=i/(b(t+ih))\) and \(z(t)=-B/(t+ih)-ih\). The imaginary part of \(t+ih\) is at least \(h-\tfrac16=\tfrac7{30}\). So \(\lambda\) and \(z\) are holomorphic on a neighbourhood of the disc, and
\[
\begin{gathered}
|\lambda(t)|\le\frac{30}{7b}=\frac{60}{7\sqrt3}<5,\\
|z(t)|\le\frac{30B}7+h=\frac{214}{35}<6.2 .
\end{gathered}
\]
The point \(w=t+ih\) lies in the disc with centre \(u_j+ih\) and radius \(\tfrac16\). By Lemma 3.2, with \(e=u_j^2+h^2-\tfrac1{36}\),
\[
\operatorname{Im}\frac1w\le\frac{-h+\frac16}e .
\]
Hence
\[
\begin{aligned}
\operatorname{Im}z(t)&=-B\operatorname{Im}\frac1w-h\\
&\ge\frac{B(h-\frac16)}e-h .
\end{aligned}
\]
The right side is smallest for the largest \(u_j\), which is \(\tfrac{11}{12}\). There \(e=\tfrac{3501}{3600}\), and the right side is \(\tfrac{1120}{3501}-\tfrac25=-\tfrac{1402}{17505}\), which is more than \(-0.081\).

*The density.* \(|e^{-i\pi tn}|=e^{\pi n\operatorname{Im}t}\le e^{\pi M/6}\), and \(|\pi_l|=|P_l|\). For \(l\ge j\), \(|t_l-t|\le t_l-u_j+\tfrac16\). The numbers \(|P_1|,\dots,|P_6|\) are \(2,2,2,1,2,1\), with \(\sum_l|P_l|=10\) and \(\sum_lt_l|P_l|=\tfrac{16}3\). Since \(\tfrac16-u_j\) is \(\tfrac1{12}\) for \(j=1\) and negative for \(j\ge2\),
\[
\begin{aligned}
&\sum_{l=j}^6|P_l|\,\bigl(t_l-u_j+\tfrac16\bigr)\\
&\quad\le\frac{16}3+\frac{10}{12}=\frac{37}6 .
\end{aligned}
\]
So
\[
\begin{gathered}
|2m_n''(t)|\le\frac{37\pi^2}3\,e^{\pi M/6},\\
|2m_n'(t)|\le20\pi\,e^{\pi M/6},
\end{gathered}
\]
and both are less than \(220\,e^{\pi M/6}\).

*The kernels.* For \(x\ge0\), \(x^a/a!\le e^x\). With \(|ty|\le1.65\) and \(|z(t)y|\le9.3\),
\[
\begin{aligned}
|\Phi_a(t)|&\le e^{\pi s|\operatorname{Im}t|}\,e^{\pi|ty|}\\
&\le e^{\pi M/6}\,e^{1.65\pi},\\
|\Psi_a(t)|&\le5\,e^{-\pi s\operatorname{Im}z(t)}\,e^{\pi|z(t)y|}\\
&\le5\,e^{0.081\pi M}\,e^{9.3\pi}.
\end{aligned}
\]
These bounds do not depend on \(a\).

*The products.* On the disc, \(|2m\Phi_a|\le220\,e^{\pi(M/3+1.65)}\) and \(|2m\Psi_a|\le1100\,e^{\pi(M/6+0.081M+9.3)}\). With \(M=168\) the exponents are \(57.65\,\pi\) and \(50.908\,\pi\); since \(\pi<22/7\) they are less than \(182\) and \(160\). Since \(e^{2.3}<10\), we get \(e^{182}<10^{79.2}\) and \(e^{160}<10^{69.6}\). So both products are bounded on the disc by \(A=10^{82}\).

*The rule.* By Proposition 2.1 with \(\rho=\tfrac1{12}\), for \(g=2m\Phi_a\) or \(g=2m\Psi_a\) on \(I_j\),
\[
\begin{gathered}
\Bigl|\int_{I_j}g\,dt-\sum_v\frac{o_v}6\,g(\tau_{jv})\Bigr|\\
\le\frac{4A}6\cdot2^{-N}.
\end{gathered}
\]
Summing over the six intervals, \(\int_0^1g\,dt\) and \(\mathcal Q(g)\) differ by at most \(4A\cdot2^{-384}\). Now \(2^{384}=1024^{38}\cdot16>16\cdot10^{114}\), so \(4A\cdot2^{-384}<\tfrac14\cdot10^{-32}\). Taking real parts does not increase the difference. \(\blacksquare\)

By linearity, for a list supported on the nodes up to \(M\) the difference is less than \(10^{-31}\) times the sum of the absolute values of its entries \(c_n,d_n\).

## 4. Exercises

**4.1.** Write down the rule of Section 1 for \(N=2\) and for \(N=4\). Check \(\sum_vo_v=1\) and the lower bound of Theorem 1.2(2) for \(N=4\).

**4.2.** Show that the rule with \(N=2\) is not exact for \(f(x)=x^2\).

**4.3.** In the proof of Theorem 3.3 the bound \(A=10^{82}\) is used. Which values of \(N\) give, by the same argument, an error below \(10^{-31}\)?

**4.4.** Let \(g\) be as in Proposition 2.1, but holomorphic and bounded by \(A\) on the larger disc \(|t-u|\le4\rho\). What bound does the proof give?

## 5. Solutions

**4.1.** For \(N=2\): \(\theta_0=\pi/4\), \(\theta_1=3\pi/4\), \(x_0=\tfrac{\sqrt2}2\), \(x_1=-\tfrac{\sqrt2}2\); the sum in \(o_v\) is empty, so \(o_0=o_1=\tfrac12\). For \(N=4\): \(\theta_v=\pi/8,3\pi/8,5\pi/8,7\pi/8\), and \(o_v=\tfrac14(1-\tfrac23\cos(2\theta_v))\). The numbers \(\cos(2\theta_v)\) are \(\tfrac{\sqrt2}2,-\tfrac{\sqrt2}2,-\tfrac{\sqrt2}2,\tfrac{\sqrt2}2\). So \(o_0=o_3=\tfrac14(1-\tfrac{\sqrt2}3)\), about \(0.132\), and \(o_1=o_2=\tfrac14(1+\tfrac{\sqrt2}3)\), about \(0.368\). Their sum is \(1\), and \(0.132>\tfrac1{12}\).

**4.2.** The rule gives \(\tfrac12(\tfrac12+\tfrac12)=\tfrac12\), and \(\tfrac12\int_{-1}^1x^2\,dx=\tfrac13\).

**4.3.** The argument gives the error \(4\cdot10^{82}\cdot2^{-N}\). This is below \(10^{-31}\) when \(2^N>4\cdot10^{113}\), that is \(N>2+113\log_210\), which is about \(377.4\). So every even \(N\ge378\) suffices.

**4.4.** Then \(|a_r|\le A/(4\rho)^r\) and \(|g_1(t)|\le A\sum_{r\ge N}4^{-r}=\tfrac43A\cdot4^{-N}\) on the interval. The error is at most \(\tfrac83A\cdot4^{-N}\).

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
- [Waldvogel] J. Waldvogel, *Fast construction of the Fejér and Clenshaw–Curtis quadrature rules*, BIT Numerical Mathematics 46 (2006), Section 2. Author's version: https://people.math.ethz.ch/~waldvoge/Papers/fejer.pdf
