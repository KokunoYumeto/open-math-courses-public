# Distributional limits of subharmonic functions

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original exposition, examples, solutions and diagrams: CC0-1.0.

Testing against smooth functions usually tells us little about individual values. For subharmonic functions, positive averages place a ceiling over those values. The local Newtonian decomposition also turns weak distributional convergence into strong convergence in the precise integrability range.

There is a further conclusion for a measuring measure with continuous potential. It identifies the **limsup**, not necessarily the ordinary limit. A sequence of moving logarithmic wells will show why that word cannot be dropped.

The written tools are [Local Newtonian potentials and subharmonic regularity, NP2–NP7](../../AN02-L131.html#NP2), including the positive Laplacian measure, explicit kernel, harmonic smoothing and local decomposition, and the [fixed-support uniform distribution bound](../../prerequisites/banach-foundation-bridges.html#a-common-finite-order-for-an-arbitrary-family). The [complete argument SC1–SC12](subharmonic-convergence-formal.md) proves every additional convergence and measurement step.

## 1. What is assumed and what follows

Let \(X\subset\mathbb R^n\) be open, \(n\ge2\). Suppose \(v_j\) and \(v\) are upper semicontinuous subharmonic functions, none identically \(-\infty\) on any component. Their spherical means dominate their center values on every closed ball in \(X\). Assume

\[
 \int_X(v_j-v)\phi\,dx\longrightarrow0
 \qquad(\phi\in C_c^\infty(X)).                              \tag{L134.1}
\]

Their local integrability makes these test pairings meaningful. Then, for every compact \(K\subset X\),

\[
 \|v_j-v\|_{L^p(K)}\longrightarrow0,\qquad
 \begin{cases}
 1\le p<n/(n-2),&n>2,\\
 \text{every finite }p\ge1,&n=2.
 \end{cases}                                                \tag{L134.2}
\]

The corresponding integral tends to zero for \(0<p<1\) too. At every point,

\[
 \limsup_jv_j(x)\le v(x).                                   \tag{L134.3}
\]

Finally, let \(\sigma\) be a positive Radon measure with compact support in \(X\), and assume \(E_n*\sigma\) has a continuous representative on all of \(\mathbb R^n\). Here

\[
 E_n(x)=-\frac{|x|^{2-n}}{(n-2)s_n}\quad(n>2),
 \qquad E_2(x)=\frac{\log|x|}{2\pi},\qquad
 \Delta E_n=\delta_0.                                      \tag{L134.4}
\]

For this measure,

\[
 \limsup_jv_j(x)=v(x)>-\infty
 \quad\text{for }\sigma\text{-almost every }x.               \tag{L134.5}
\]

The measuring potential need not be globally bounded. Positivity and compact support alone do not replace its continuity hypothesis. The sequence is assumed to converge in distributions to the specified subharmonic function \(v\).

## 2. A small cap separates the two limits

Write the positive Laplacian measures as \(\mu_j=\Delta v_j\) and \(\mu=\Delta v\). Testing on \(\Delta\phi\) makes \(\mu_j\to\mu\) on smooth tests. Their local masses are uniformly bounded: a nonnegative smooth cutoff equal to one near a compact set bounds its mass by a convergent test pairing. Uniform approximation by smooth functions then gives convergence on continuous compact tests.

Near a compact observation region, choose \(0\le\chi\le1\), compactly supported in \(X\), equal to one there. The local decomposition is

\[
 v_j=E_n*(\chi\mu_j)+h_j,\qquad
 v=E_n*(\chi\mu)+h,                                        \tag{L134.6}
\]

with harmonic remainders. Fixed radial harmonic averages and the uniform test bound show that \(h_j\to h\) locally with every derivative.

The remaining difficulty is the singularity of \(E_n\). Cap it at radius \(\delta>0\):

\[
 E_n^\delta(x)=E_n(\max(|x|,\delta)).                        \tag{L134.7}
\]

This kernel is continuous and differs from \(E_n\) only inside its small ball. On a fixed compact observation set, weak convergence of the cut-off measures gives uniform convergence of their potentials against this fixed cap. Uniform continuity of the cap on the relevant compact difference set and a finite set of observation points prove that uniformity.

If the masses are at most \(M\), the error obeys

\[
 \begin{aligned}
 \|E_n*(\chi\mu_j-\chi\mu)\|_{L^p(K)}
 &\le2M\|E_n-E_n^\delta\|_{L^p(\mathbb R^n)}\\
 &\quad+|K|^{1/p}
   \sup_K|E_n^\delta*(\chi\mu_j-\chi\mu)|.
 \end{aligned}                                              \tag{L134.8}
\]

Take \(j\to\infty\) while \(\delta\) is fixed. Then take \(\delta\downarrow0\). The first norm tends to zero exactly in the stated range, by the explicit radial integrals. This order avoids demanding any convergence rate from the measures.

For example, in three dimensions,

\[
 \|E_3-E_3^\delta\|_1=\frac{\delta^2}{6},\qquad
 \|E_3-E_3^\delta\|_2=\left(\frac{\delta}{12\pi}\right)^{1/2}.
                                                               \tag{L134.9}
\]

In dimension two the \(L^1\) error is \(\delta^2/4\). [SC3–SC5](subharmonic-convergence-formal.md#SC3) give the positive-measure convergence, harmonic limit and complete norm estimate.

![The capped Newtonian kernel and the exact rates at which its local error vanishes.](figures/kernel-cap-and-norms.png)

*Figure 1.* The cap radius is \(0.4\). The original three-dimensional kernel diverges negatively at zero; the cap stays finite and agrees with it beyond the cap radius. The radial \(L^1\) error density is \(r-r^2/\delta\). Its area gives the first formula in (L134.9). The final panel plots that rate, the exact \(L^2\) rate in dimension three, and the planar \(L^1\) rate. The general exponent calculation is in SC4.

## 3. Positive averages control the upper limit

For a fixed small normalized radial smooth kernel \(\rho_r\), subharmonicity gives

\[
 v_j(x)\le(v_j*\rho_r)(x).                                  \tag{L134.10}
\]

The right side converges by (L134.1), because its translate is one fixed smooth test. Hence \(\limsup v_j(x)\le v*\rho_r(x)\). Letting \(r\downarrow0\) recovers the given upper semicontinuous value \(v(x)\), even if it is \(-\infty\). This proves the everywhere inequality, without passing to a subsequence.

One fixed radius valid over a compact observation set also gives a finite common upper bound for all \(v_j\) there. It does not bound the functions below. Deep negative wells remain possible.

**Worked example: a strict exceptional point.** Set \(v_j(x)=j^{-1}\log|x|\) in a planar disc and \(v=0\). Every finite local \(L^p\) norm tends to zero. Nevertheless all \(v_j(0)=-\infty\), so the upper limit at zero is strictly smaller than the limit function. The measure \(\delta_0\) notices that point, but its logarithmic potential is not continuous and it does not satisfy the final hypothesis.

## 4. A second measure detects almost every upper-limit value

Let \(F=E_n*\sigma\) be the continuous potential. On the support of the local cutoff mass it is bounded. Absolute product-kernel integrability is available: the positive part of the kernel is bounded on compact difference sets, while finiteness of \(F\) controls its negative part.

Fubini and the even kernel therefore give

\[
 \int E_n*(\chi\mu_j)\,d\sigma
 =\int F(y)\chi(y)\,d\mu_j(y)
 \longrightarrow\int F(y)\chi(y)\,d\mu(y).                  \tag{L134.11}
\]

The harmonic integrals converge too. Thus \(v_j,v\in L^1(\sigma)\) and their integrals converge. In particular \(v\) is finite \(\sigma\)-almost everywhere.

Choose a finite upper bound \(C\) on the compact measuring support. Fatou applies to \(C-v_j\ge0\):

\[
 \int(C-\limsup_jv_j)\,d\sigma
 \le\liminf_j\int(C-v_j)\,d\sigma
 =\int(C-v)\,d\sigma.                                      \tag{L134.12}
\]

The everywhere upper-limit inequality gives the opposite comparison between the two integrands. Their equal finite integrals force equality almost everywhere, proving (L134.5). [SC7–SC8](subharmonic-convergence-formal.md#SC7) justify the canonical potential values, all integrability and the Fatou step.

**Worked example: a measure on a circle.** Uniform probability measure on the planar circle of radius \(a\) has potential

\[
 F(x)=\frac1{2\pi}\log\max(|x|,a).                           \tag{L134.13}
\]

It is continuous, including at the circle. Inside, the angular mean of \(\log|1-qe^{i\theta}|\), \(q<1\), is zero by its convergent logarithmic series; outside, factor out \(|x|\). An integrable logarithmic bound lets the interior formula reach the circle. SC9 gives the details. The theorem identifies the upper limit for arc-length almost every point on this set of zero planar area.

## 5. Why the sequence itself can still fail to converge

On \(X=(0,1)^2\), let \(N_m=\lceil e^m\rceil\) and list, block by block, all centers

\[
 a=(k/N_m,\ell/N_m),\qquad0\le k,\ell\le N_m.
\]

For each center in block \(m\), use \(u_{m,a}(x)=m^{-1}\log|x-a|\). All finite local \(L^p\) norms tend to zero uniformly within the block: the translated logarithmic kernel has a uniform norm bound, and the coefficient is \(1/m\).

At any fixed point a nearest center is within \(\sqrt2/(2N_m)<e^{-m}\). That term is at most \(-1\). A far corner has distance between \(1/\sqrt2\) and \(\sqrt2\), so its value tends to zero after division by \(m\). Every term is at most \((\log\sqrt2)/m\). Therefore

\[
 \limsup_j u_j(x)=0,\qquad\liminf_j u_j(x)\le-1
 \quad\text{everywhere in }X.                              \tag{L134.14}
\]

The normalized area measure of the disc of radius \(1/4\) centered at \((1/2,1/2)\) has a continuous potential by L131. Pointwise convergence fails at every point of its support too. The theorem's upper-limit conclusion remains exactly correct.

![A nearby logarithmic well and a far corner give incompatible pointwise subsequences.](figures/moving-logarithmic-wells.png)

*Figure 2.* A finite grid block covers the square with the regions where some term is at most \(-1\). The chosen observation point is \(x_0=(0.37,0.61)\). The distance panel gives a nearby term in each illustrated block; the final panel compares these values with a fixed far-corner subsequence tending to zero. The complete proof uses every level, not just the plotted samples. Each block has \((N_m+1)^2\) terms.

The norm endpoints have a separate obstruction. In dimension three, translated kernels \(E_3(x-a_j)\to E_3(x)\), \(a_j\to0\), converge in distributions. Their difference near a displaced singularity has an infinite \(L^p\) norm for \(p\ge3\). Translated planar logarithms have unbounded differences, excluding a general \(L^\infty\) assertion.

In dimension one the kernel \(|x|/2\) is continuous. The same local decomposition then gives local uniform convergence directly. This is a separate conclusion; the higher-dimensional expression \(n/(n-2)\) supplies no positive exponent when \(n=1\).

## 6. Exercises

1. Integrate the three-dimensional capped-kernel \(L^1\) error density \(r-r^2/\delta\).
2. Explain why the cap radius stays fixed while the sequence converges.
3. Identify the step that uses positivity when smooth tests are replaced by continuous tests.
4. For \(v_j=j^{-1}\log|x|\), find the upper and lower limits at zero and at a nonzero point.
5. Prove that the grid block always contains a term at most \(-1\) at a given point.
6. Explain why a common upper bound is enough for Fatou here, even though negative wells are unbounded.
7. Check the potential of the admissible normalized disc measure of radius \(a\).

## 7. Complete solutions

**1.** Integration gives \(\delta^2/2-\delta^2/3=\delta^2/6\). Including the sphere area and \(1/(4\pi)\) kernel coefficient is exactly what makes the density \(r-r^2/\delta\).

**2.** Weak convergence gives uniform convergence for one continuous cap, with constants depending on that cap. It does not supply uniformity for increasingly singular caps. First make the cap error smaller than half a chosen tolerance; then make the fixed-cap sequence error smaller than the other half.

**3.** Positivity bounds local mass by one nonnegative cutoff pairing. The convergent pairing gives a uniform mass bound, which controls uniform-approximation errors. For signed measures, a total-variation bound would need separate justification.

**4.** At zero all terms are \(-\infty\), so both limits are \(-\infty\). At any nonzero point the fixed finite logarithm divided by \(j\) tends to zero. The distributional limit is zero everywhere, but its pointwise value at zero is not the upper limit of the sequence.

**5.** Round both coordinates of \(N_mx\) to a nearest integer. Each coordinate error is at most \(1/(2N_m)\), giving Euclidean distance at most \(\sqrt2/(2N_m)<e^{-m}\). The logarithm divided by \(m\) is consequently at most \(-1\); a zero distance gives \(-\infty\).

**6.** Subtract each function from the common upper bound \(C\). The resulting functions are nonnegative, so Fatou applies without a bound on their size. Convergence of their integrals comes from the continuous-potential calculation, not from dominated convergence of the original sequence.

**7.** L131's planar ball formula gives, for \(r=|x|\),

\[
 E_2*q_a=
 \begin{cases}
 (2\pi)^{-1}\log a+(r^2-a^2)/(4\pi a^2),&r\le a,\\
 (2\pi)^{-1}\log r,&r\ge a.
 \end{cases}
\]

The values agree at \(r=a\), and both derivatives are \(1/(2\pi a)\) there. The formula is finite at zero and continuous everywhere. Translating it gives the disc measure used in the grid example; its closed support stays inside \(X\) when the radius is \(1/4\) and the center \((1/2,1/2)\).

## Source credit

The classical statement is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Proposition 16.1.2, printed pages 304–305: first edition 1983, second printing 1990, reprint 2005. Both pointwise claims are limsup claims. The [full original argument](subharmonic-convergence-formal.md), worked examples, solutions and diagrams accompany this exposition.
