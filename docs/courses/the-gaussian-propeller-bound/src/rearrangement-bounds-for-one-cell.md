# Rearrangement bounds for one cell

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

We work in the standing setting (S1)–(S6) of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), Section 4: an optimal partition with \(m\ge5\) active cells, cones \(K_i\) in \(V\cong\mathbb R^{m-1}\), moments \(z_i\), cell measures \(P_i\) and normalized lengths \(r_i=|z_i|/\sqrt C\), under the hypothesis \(C>B^2=9/(8\pi)\). A cell with a long moment must carry a lot of mass, because mass far out in one direction is limited. This lesson proves (Proposition 2.4): with \(A=0.929\) if \(m=5\) and \(A=0.884\) if \(m\ge6\), every cell satisfies
\[
r_i<\frac23\qquad\text{and}\qquad P_i>Ar_i^2 .
\]

Here and in the rest of the course every terminating decimal denotes an exact rational number. Since \(\sum_iP_i=\sum_ir_i^2=1\) by (S2) and (S5), the bound \(P_i>Ar_i^2\) leaves a total excess of \(1-A\) to be distributed; the last lesson shows that the cells cannot afford it.

## 1. The half-space comparison

**Lemma 1.1** (bathtub principle). Let \(K\subseteq\mathbb R^d\) be measurable with \(\gamma_d(K)=P\in(0,1)\), let \(e\) be a unit vector, \(x=\Phi^{-1}(1-P)\) and \(H=\{y:\langle e,y\rangle\ge x\}\). Then
\[
\begin{aligned}
\int_K\langle e,y\rangle\,d\gamma_d(y)&\le\int_H\langle e,y\rangle\,d\gamma_d(y)\\
&=\phi(x).
\end{aligned}
\]

**Proof.** The coordinate \(\langle e,y\rangle\) is standard normal under \(\gamma_d\), so \(\gamma_d(H)=1-\Phi(x)=P\) and \(\int_H\langle e,y\rangle\,d\gamma_d=\int_x^\infty s\phi(s)\,ds=\phi(x)\). The function \((\langle e,y\rangle-x)(\mathbf 1_K-\mathbf 1_H)\) is nonpositive everywhere: where \(\mathbf 1_K-\mathbf 1_H=1\), the point is outside \(H\); where it is \(-1\), the point is in \(H\). Integrating, and using \(\int x(\mathbf 1_K-\mathbf 1_H)\,d\gamma_d=x(P-P)=0\), gives the inequality. \(\square\)

**Corollary 1.2.** Let \(x_i=\Phi^{-1}(1-P_i)\). Then \(x_i\ge0\), \(|z_i|\le\phi(x_i)\), \(r_i<\frac23\), and
\[
\frac{P_i}{r_i^2}>f(x_i),\qquad f(x)=\frac94\,e^{x^2}\,\Phi(-x).
\]

**Proof.** \(x_i\ge0\) because \(P_i\le\frac12\). Apply Lemma 1.1 to \(K_i\) and \(e=z_i/|z_i|\): \(|z_i|=\int_{K_i}\langle e,y\rangle\,d\gamma_{m-1}\le\phi(x_i)\). Since \(\sqrt C>B=\frac32\phi(0)\),
\[
r_i=\frac{|z_i|}{\sqrt C}<\frac{\phi(x_i)}{B}\le\frac{\phi(0)}{B}=\frac23,
\]
and \(r_i^2<\phi(x_i)^2/B^2=\frac49e^{-x_i^2}\). With \(P_i=\Phi(-x_i)\) this gives \(P_i/r_i^2>f(x_i)\). \(\square\)

**Lemma 1.3.** \(\min_{x\in\mathbb R}f(x)>0.8843837\).

**Proof.** Let \(M(x)=\phi(x)/\Phi(-x)\) and let \(Z\) be standard normal. Integration by parts gives \(\int_x^\infty s\phi(s)\,ds=\phi(x)\) and \(\int_x^\infty s^2\phi(s)\,ds=x\phi(x)+\Phi(-x)\), so, with \(M=M(x)\),
\[
\begin{aligned}
\mathbb E(Z\mid Z>x)&=M,\\
\operatorname{Var}(Z\mid Z>x)&=1+xM-M^2 .
\end{aligned}
\]
Differentiating, \(M'=M^2-xM\), which is \(1-\operatorname{Var}(Z\mid Z>x)<1\), the variance of a nonconstant random variable being positive. Since \((\log f)'(x)=2x-M(x)=:D(x)\), we get \((\log f)''=2-M'>1\): \(\log f\) is strictly convex and \(D\) is strictly increasing.

The rational enclosures of Section 3 give
\[
\begin{aligned}
-0.000131&<D(0.6119)<-0.000126,\\
0.000120&<D(0.6121)<0.000124,
\end{aligned}
\]
so \(f\) has a unique minimizer \(x_*\in(0.6119,0.6121)\). Evaluating \(D\) on the whole interval \([0.6119,0.6121]\) with interval arithmetic gives \(|D|<0.001\) there, and the enclosures give \(f(0.612)>0.884383832\). Since \(|x_*-0.612|<0.0001\) and \(|D|<0.001\), \(\log f(x_*)\ge\log f(0.612)-10^{-7}\), and
\[
\begin{aligned}
\min f&\ge f(0.612)e^{-10^{-7}}\\
&>0.884383832\,(1-10^{-7})\\
&>0.8843837 .
\end{aligned}
\]
\(\square\)

The minimum is about \(0.8843841\), attained near \(x=0.6120032\).

## 2. Five cells: caps on the three-sphere

When \(m=5\), the cones live in \(V\cong\mathbb R^4\), and a cone is determined by its trace on the unit sphere \(S^3\). Comparing with spherical caps instead of half-spaces improves the constant.

**Polar coordinates.** For the \(r\)-dimensional Hausdorff measure \(\nu_r\) on \(\mathbb R^{r+1}\) and a nonnegative measurable function \(F\) on \(\mathbb R^{r+1}\),
\[
\int_{\mathbb R^{r+1}}F\,dx=\int_0^\infty\int_{\{|x|=t\}}F\,d\nu_r\,dt
\]
([Fremlin, *Measure Theory*, Volume 2, Theorem 265G](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm), with \(\delta\to\infty\) by monotone convergence), the sphere of radius \(t\) has \(\nu_r\)-measure \(t^r\nu_r(S^r)\) and \(\nu_r\) scales by \(t^r\) under \(x\mapsto tx\) ([Fremlin, Volume 2, 264G and Corollary 265H](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm)), and \(\nu_r(S^r)=(r+1)\beta_{r+1}\), where \(\beta_{r+1}\) is the volume of the unit ball; so \(\nu_2(S^2)=4\pi\) and \(\nu_3(S^3)=2\pi^2\). For \(F(x)=\psi(|x|)\,h(x/|x|)\) this gives
\[
\begin{aligned}
&\int_{\mathbb R^{r+1}}\psi(|x|)\,h\Bigl(\frac x{|x|}\Bigr)dx\\
&\quad=\int_0^\infty\psi(t)t^r\,dt\int_{S^r}h\,d\nu_r .
\end{aligned}
\]

**Lemma 2.1.** Let \(g\) be standard Gaussian in \(\mathbb R^4\), \(R=|g|\) and \(U=g/|g|\).
(a) \(R\) and \(U\) are independent, \(U\) has the normalized surface measure \(\sigma=\nu_3/(2\pi^2)\), and \(\mathbb ER=3\sqrt{2\pi}/4\).
(b) For a unit vector \(e\), the coordinate \(\langle e,U\rangle\) has density \(\frac2\pi\sqrt{1-u^2}\) on \([-1,1]\).

**Proof.** (a) Apply the polar formula with \(r=3\) and \(\psi(t)=\psi_0(t)(2\pi)^{-2}e^{-t^2/2}\): \(\mathbb E[\psi_0(R)h(U)]\) is a product of a factor depending only on \(\psi_0\) and the factor \(\int h\,d\nu_3\). Taking \(\psi_0=1\) or \(h=1\) identifies the factors with \(\mathbb E\psi_0(R)\) and \(\mathbb Eh(U)=\int h\,d\sigma\). Also
\[
\begin{aligned}
\mathbb ER&=\frac{2\pi^2}{(2\pi)^2}\int_0^\infty t^4e^{-t^2/2}\,dt\\
&=\frac12\cdot\frac{3\sqrt{2\pi}}2 .
\end{aligned}
\]

(b) By rotation invariance take \(e\) to be the first basis vector and write \(g=(g_1,g')\) with \(g'\in\mathbb R^3\) independent of \(g_1\). By the polar formula with \(r=2\), \(\rho=|g'|\) has density \(\sqrt{2/\pi}\,\rho^2e^{-\rho^2/2}\) on \((0,\infty)\). Since \(\frac1{\sqrt{2\pi}}\sqrt{\frac2\pi}=\frac1\pi\), the pair \((g_1,\rho)\) has the density \(\frac1\pi\rho^2e^{-(g_1^2+\rho^2)/2}\) on \(\mathbb R\times(0,\infty)\). For bounded measurable \(F\), polar coordinates \((g_1,\rho)=(s\cos\theta,s\sin\theta)\) with \(0<\theta<\pi\) ([Fremlin, Volume 2, 263G](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm)), with area element \(s\,ds\,d\theta\) and \(\int_0^\infty s^3e^{-s^2/2}\,ds=2\), give
\[
\begin{aligned}
&\mathbb EF\Bigl(\frac{g_1}{\sqrt{g_1^2+\rho^2}}\Bigr)\\
&\quad=\frac2\pi\int_0^\pi F(\cos\theta)\sin^2\theta\,d\theta .
\end{aligned}
\]
The substitution \(u=\cos\theta\) turns this into \(\frac2\pi\int_{-1}^1F(u)\sqrt{1-u^2}\,du\). \(\square\)

For \(0\le x<1\) the *cap* \(\{u\in S^3:\langle e,u\rangle\ge x\}\) has \(\sigma\)-measure
\[
\begin{aligned}
p(x)&=\frac2\pi\int_x^1\sqrt{1-u^2}\,du\\
&=\frac12-\frac{\arcsin x+x\sqrt{1-x^2}}\pi
\end{aligned}
\]
and first moment
\[
\begin{aligned}
&\frac2\pi\int_x^1u\sqrt{1-u^2}\,du\\
&\quad=\frac2{3\pi}(1-x^2)^{3/2}.
\end{aligned}
\]

**Corollary 2.2.** Let \(m=5\) and let \(x_i\in[0,1)\) satisfy \(p(x_i)=P_i\). Then \(|z_i|\le\phi(0)(1-x_i^2)^{3/2}\) and
\[
\begin{gathered}
\frac{P_i}{r_i^2}>R(x_i),\\
R(x)=\frac94\cdot\frac{p(x)}{(1-x^2)^3}.
\end{gathered}
\]

**Proof.** \(p\) decreases continuously from \(\frac12\) to \(0\) on \([0,1)\), so \(x_i\) exists because \(0<P_i\le\frac12\). The cone \(K_i\) satisfies \(\mathbf 1_{K_i}(g)=\mathbf 1_{K_i}(U)\), so by Lemma 2.1(a), with \(e=z_i/|z_i|\),
\[
\begin{aligned}
P_i&=\sigma(K_i\cap S^3),\\
|z_i|&=\mathbb E\bigl[R\langle e,U\rangle\mathbf 1_{K_i}(U)\bigr]\\
&=\mathbb ER\cdot\mathbb E\bigl[\langle e,U\rangle\mathbf 1_{K_i}(U)\bigr].
\end{aligned}
\]
The bathtub argument of Lemma 1.1, with the law \(\sigma\) of \(U\) and the threshold \(x_i\), bounds the last expectation by the first moment of the cap. Hence
\[
\begin{aligned}
|z_i|&\le\frac{3\sqrt{2\pi}}4\cdot\frac2{3\pi}(1-x_i^2)^{3/2}\\
&=\phi(0)(1-x_i^2)^{3/2}.
\end{aligned}
\]
Dividing \(P_i=p(x_i)\) by \(r_i^2<|z_i|^2/B^2\le\frac49(1-x_i^2)^3\) gives the claim. \(\square\)

**Lemma 2.3.** \(\min_{0\le x<1}R(x)>0.9311326\).

**Proof.** Put
\[
\begin{aligned}
F(x)&=6x\,p(x)-\frac2\pi(1-x^2)^{3/2},\\
H(x)&=p(x)-\frac x\pi\sqrt{1-x^2}.
\end{aligned}
\]
Using \(p'(x)=-\frac2\pi\sqrt{1-x^2}\), direct differentiation gives
\[
\begin{gathered}
R'=\frac94\cdot\frac{F}{(1-x^2)^4},\\
F'=6H,\qquad H'=\frac{4x^2-3}{\pi\sqrt{1-x^2}} .
\end{gathered}
\]
So \(H\) decreases on \([0,\sqrt3/2]\) and increases on \([\sqrt3/2,1)\). Since \(H(0)=\frac12\) and \(H(x)\to0\) as \(x\to1\), \(H\) is negative on \([\sqrt3/2,1)\) and has exactly one zero \(x_H\in(0,\sqrt3/2)\). Hence \(F\) increases on \([0,x_H]\) and decreases on \([x_H,1)\); as \(F(0)=-2/\pi<0\) and \(F(x)\to0\) as \(x\to1\), \(F\) is positive on \([x_H,1)\) and has exactly one zero \(x_F\in(0,x_H)\). So \(R\) decreases on \([0,x_F]\) and increases on \([x_F,1)\), and \(\min R=R(x_F)\).

The enclosures of Section 3 give
\[
\begin{aligned}
-0.0047010&<F(0.29)<-0.0046981,\\
0.0007683&<F(0.294)<0.0007712,
\end{aligned}
\]
so \(x_F\in(0.29,0.294)\). On this interval \(p\) decreases and \(x\sqrt{1-x^2}\le0.294\), so \(H(x)\ge p(0.294)-0.294/\pi\), which exceeds \(0.22198\); hence \(H>0\) and \(F\) increases there and \(|F|<0.004702\). Consequently, on \([0.29,0.294]\),
\[
\begin{aligned}
|R'(x)|&<\frac94\cdot\frac{0.004702}{(1-0.294^2)^4}\\
&<0.015189<0.03 .
\end{aligned}
\]
With \(R(0.29)>0.9312526\) from Section 3,
\[
\begin{aligned}
R(x_F)&\ge R(0.29)-0.03\cdot0.004\\
&>0.9312526-0.00012\\
&=0.9311326 .
\end{aligned}
\]
\(\square\)

**Proposition 2.4.** Put \(A=0.929\) if \(m=5\) and \(A=0.884\) if \(m\ge6\). For every \(i\),
\[
r_i<\frac23\qquad\text{and}\qquad P_i>Ar_i^2 .
\]

**Proof.** The bound \(r_i<\frac23\) is Corollary 1.2. For \(m\ge6\), Corollary 1.2 and Lemma 1.3 give \(P_i/r_i^2>0.8843837>0.884\). For \(m=5\), Corollary 2.2 and Lemma 2.3 give \(P_i/r_i^2>0.9311326>0.929\). \(\square\)

## 3. Rational enclosures

All finite comparisons of the course reduce to rational arithmetic with the following enclosures. Each tabulated value was also recomputed with ball arithmetic (python-flint, 256-bit precision) in the check program of the course record.

- \(3.14159<\pi<3.14160\), for instance from \(\pi=16\arctan\frac15-4\arctan\frac1{239}\) and alternating partial sums of the arctangent series.
- For \(y\ge0\), Taylor's formula with integral remainder gives \(E_{15}(y)\le e^{-y}\le E_{14}(y)\), where \(E_N(y)=\sum_{j=0}^N(-y)^j/j!\); the sign of the remainder of order \(N\) is \((-1)^{N+1}\).
- Integrating these bounds for \(e^{-s^2/2}\) from \(0\) to \(x\ge0\): with \(J_N(x)=\sum_{j=0}^N\frac{(-1)^jx^{2j+1}}{2^jj!\,(2j+1)}\),
\[
\begin{aligned}
\Phi(x)&\ge\frac12+\frac{J_{15}(x)}{\sqrt{2\pi}},\\
\Phi(x)&\le\frac12+\frac{J_{14}(x)}{\sqrt{2\pi}},
\end{aligned}
\]
and \(\Phi(-x)=1-\Phi(x)\).
- For \(0\le x<1\), the binomial series of \((1-u^2)^{-1/2}\) has positive coefficients at most one; integrating it gives \(Q(x)\le\arcsin x\le Q(x)+\frac{x^{11}}{11(1-x^2)}\) with \(Q(x)=\sum_{j=0}^4\binom{2j}j\frac{x^{2j+1}}{4^j(2j+1)}\).
- Square roots: \(l\le\sqrt y\le u\) for rationals with \(l^2\le y\le u^2\).

The values used in this lesson:

| quantity | enclosure |
|---|---|
| \(D(0.6119)\) | \((-0.000131,\,-0.000126)\) |
| \(D(0.6121)\) | \((0.000120,\,0.000124)\) |
| \(D\) on \([0.6119,0.6121]\) | \((-0.000430,\,0.000424)\) |
| \(f(0.612)\) | \(>0.884383832\) |
| \(F(0.29)\) | \((-0.0047010,\,-0.0046981)\) |
| \(F(0.294)\) | \((0.0007683,\,0.0007712)\) |
| \(R(0.29)\) | \(>0.9312526\) |
| \(p(0.294)-0.294/\pi\) | \(>0.22198\) |

## 4. Exercises

**4.1** (easy). Show that Lemma 1.1 fails without the condition \(\gamma_d(K)=\gamma_d(H)\): find \(K\) with \(\int_K\langle e,y\rangle\,d\gamma_d>\phi(x)\) when \(K\) is allowed a larger measure than \(H\).

**4.2** (medium). For the propeller of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), Corollary 2.2, compute \(P\) and \(r\) for each sector (with \(C=9/(8\pi)\)) and the ratio \(P/r^2\). Compare it with \(\min f\).

**4.3** (medium). Show that \(f(x)\to\infty\) as \(x\to\pm\infty\) without using Lemma 1.3, using \(\Phi(-x)\ge\frac{x}{1+x^2}\phi(x)\) for \(x>0\).

**4.4** (medium). Show that for \(g\) standard Gaussian in \(\mathbb R^4\) and a cone \(K\) (a set with \(tK=K\) for \(t>0\)), \(\gamma_4(K)=\sigma(K\cap S^3)\).

## 5. Solutions

**4.1.** Take \(K=\{\langle e,y\rangle\ge0\}\), of measure \(\frac12\), and \(x=\Phi^{-1}(1-P)\) for a smaller \(P\), say \(P=0.1\) and \(x\approx1.28\). Then \(\int_K\langle e,y\rangle\,d\gamma_d=\phi(0)\approx0.399\), more than \(\phi(1.28)\approx0.176\).

**4.2.** Each sector has \(P=\frac13\) and \(|z|=\sin(\pi/3)/\sqrt{2\pi}\), so \(r^2=|z|^2/C=\frac{3/(8\pi)}{9/(8\pi)}=\frac13\) and \(P/r^2=1\). The proof of Corollary 1.2 with \(C=9/(8\pi)\) gives \(P/r^2\ge f(x)\) with \(x=\Phi^{-1}(\frac23)\approx0.431\), where \(f(x)\approx0.903\); so the propeller is far from the extreme case of the half-space comparison.

**4.3.** For \(x>0\), \(f(x)\ge\frac94e^{x^2}\frac{x}{1+x^2}\frac{e^{-x^2/2}}{\sqrt{2\pi}}\), which tends to infinity. For \(x\to-\infty\), \(\Phi(-x)\to1\) and \(e^{x^2}\to\infty\). (The inequality \(\Phi(-x)\ge\frac{x}{1+x^2}\phi(x)\) follows by differentiating \(\Phi(-x)-\frac{x}{1+x^2}\phi(x)\), which has derivative \(-\frac{2\phi(x)}{(1+x^2)^2}<0\) and limit \(0\) at infinity.)

**4.4.** Apply Lemma 2.1(a) with \(h=\mathbf 1_{K\cap S^3}\): since \(\mathbf 1_K(g)=\mathbf 1_K(U)\), \(\gamma_4(K)=\mathbb E\mathbf 1_{K}(U)=\sigma(K\cap S^3)\).

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026, Section 3 and Appendix A. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, author's edition, the basis of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
