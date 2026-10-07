# Weighted holomorphic extensions and their growth

*AN-02 · Lesson 145 · Original exposition by GPT-6.1 Sol (OpenAI), Ultra. Self-checked by the writing AI. October 2026. CC0 1.0.*

An entire function on a complex linear subspace always has an entire extension if we ignore growth: keep it independent of the missing coordinates. That obvious extension may have infinite norm in the desired weight. The problem here is to extend with a controlled weighted norm. A cutoff produces a finite-norm candidate near the subspace; a solved Cauchy–Riemann equation repairs its failure to be holomorphic.

The [complete formal proof](weighted-holomorphic-extension-formal.md) writes all operator, restriction, iteration and growth steps. Its actual existence input is [L144 general PSH weighted existence](../../AN02-L144.html#general-psh-weighted-existence). The harmonic smoothing lemma [L131 NP5](../../AN02-L131.html#NP5), followed by an explicit joint Cauchy-series argument, turns the resulting weak equation into an entire function.

## 1. The two results

Let \(\phi\) be a finite PSH function on \(\mathbb C^n\), \(n\ge1\). Assume a global unit-scale oscillation bound:

\[
|\phi(z)-\phi(z')|<C\quad\text{if }|z-z'|<1,
\qquad C>0.
\tag{L145.1}
\]

Let \(W\) be a complex linear subspace of codimension \(k\), \(0\le k\le n\), and put \(R(z)=1+|z|^2\). Use ordinary induced Euclidean volume \(dS\) on \(W\). If \(W=\{0\}\), its single point has measure 1.

<a id="extension-statement"></a>

**Weighted extension.** Every entire \(u\) on \(W\) with finite \(J_0=\int_W|u|^2e^{-\phi}dS\) has an entire extension \(U\) satisfying

\[
U|_W=u,\qquad
\int_{\mathbb C^n}|U|^2e^{-\phi}R^{-3k}dV
\le(6\pi e^C)^kJ_0.
\tag{L145.2}
\]

For \(k=0\), choose \(U=u\); the factor is1 and no normal coordinate is added. For positive \(k\), the restriction in (L145.2) holds at every point of \(W\). An ambient almost-everywhere identity alone would not determine a function on that zero-volume subspace.

<a id="growth-statement"></a>

**Growth transfer.** If instead \(|u(z)|\le C_1e^{\phi(z)}\) on \(W\), with finite \(C_1\ge0\), an entire extension satisfies

\[
|U(z)|\le C_2(1+|z|)^{n+2k+1}e^{\phi(z)}
\quad(z\in\mathbb C^n)
\tag{L145.3}
\]

for some finite \(C_2\). This hypothesis need not give finite \(J_0\). The proof changes the weight first. The displayed polynomial exponent is the exact source exponent; no optimality assertion accompanies it.

## 2. Build the extension one coordinate at a time

Use orthonormal complex coordinates in which a hyperplane is \(w=0\), with \(z=(\zeta,w)\). Unitary coordinates preserve lengths, induced volumes and PSH. For one step we need only

\[
\theta(\zeta,w)\ge\theta(\zeta,0)-C\quad(|w|<1).
\tag{L145.4}
\]

This compares the weight in the normal unit disk with its value on the hyperplane. It makes the norm of the normal-independent candidate in that disk at most \(\pi e^C\) times its hyperplane norm.

Take a continuous Lipschitz cutoff that is1 on \(|w|\le1/2\), equals \(2(1-|w|)\) between radii1/2 and1, and is0 for \(|w|\ge1\). Its weak antiholomorphic derivative is

\[
\bar\partial_w\eta=-\frac{w}{|w|}\mathbf1_{\{1/2<|w|<1\}}.
\tag{L145.5}
\]

The cutoff values match at both joining circles, so first weak derivatives have no circle-supported jump term. The candidate \(\eta(w)u(\zeta)\) agrees with the datum near the hyperplane, but its derivative is not zero in the annulus. Define the last coefficient of a closed form by

\[
f_d=\frac{u(\zeta)}w\bar\partial_w\eta
=-\frac{u(\zeta)}{|w|}\mathbf1_{\{1/2<|w|<1\}},
\qquad f_1=\cdots=f_{d-1}=0.
\tag{L145.6}
\]

There is no singular coefficient at0: the annulus stays away from0, and the definition is zero near it. The cross derivatives vanish because \(u\) is holomorphic in every \(\zeta\) coordinate. In dimension one closedness is automatic.

If \(J=\int|u|^2e^{-\theta(\zeta,0)}dV(\zeta)\), then \(|f_d|\le2|u|\) on the normal tube. L144 provides \(v\) with

\[
\bar\partial v=f,\qquad
\int|v|^2e^{-\theta}R^{-2}dV\le2\pi e^C J.
\tag{L145.7}
\]

Now put

\[
U=\eta(w)u(\zeta)-wv.
\tag{L145.8}
\]

Initially this is an almost-everywhere locally square-integrable formula. Its distributional Cauchy–Riemann derivatives vanish, because multiplication by the holomorphic \(w\) cancels exactly the error in (L145.6). Formal E3 proves that it has an entire representative: zero antiholomorphic derivatives give zero Laplacian, NP5 gives a smooth representative, and iterated coordinate Cauchy formulas give a joint power series.

<a id="learner-restriction"></a>

Why does the entire representative still equal \(u\) on the hyperplane? On \(|w|<1/2\), its entire difference \(G=U-u\) equals \(-wv\) almost everywhere. A nonzero value \(G(\zeta_0,0)\) would, by continuity, make \(|G|\) bounded below on a product neighborhood. Then \(|v|\) would be at least a positive constant times \(1/|w|\), while

\[
\int_{0<|w|<\varepsilon}|w|^{-2}dA(w)
=2\pi\int_0^\varepsilon\frac{dr}{r}=\infty.
\tag{L145.9}
\]

This contradicts the local square integrability supplied by (L145.7). Fubini includes the positive tangential volume; when there is no tangential coordinate, its factor is1. The restriction therefore holds pointwise. It was not obtained by arbitrarily assigning a value to \(v\) at \(w=0\).

![The normal cutoff, annular error and local square-integrability obstruction](figures/normal-cutoff-and-trace.png)

*Figure 1. The normal coordinate is one complex plane; the error factor is shown for unit datum \(u=1\). The cutoff changes only between radii1/2 and1; the error divided by the datum has modulus \(1/r\) on that annulus. Its exact square area integral is \(2\pi\log2\), below the coarse bound \(4\pi\) used in the theorem. A nonzero holomorphic trace difference would instead force a normal pole down to radius 0; its truncated square integral is \(2\pi\log(1/\varepsilon)\), which diverges. The right panel shows that different, hypothetical obstruction, not the actual correction returned by the theorem. Proof locators: formal E4, EX11–EX18. Human source: Hörmander II, Theorem 15.1.3, printed pp. 274–275.*

## 3. Track the constant and the three lost powers

The elementary square inequality and \(|w|^2\le R\) give

\[
\begin{aligned}
\int|U|^2e^{-\theta}R^{-3}dV
&\le2\int_{|w|<1}|u|^2e^{-\theta}dV
   +2\int|v|^2e^{-\theta}R^{-2}dV\\
&\le2\pi e^C J+4\pi e^C J=6\pi e^C J.
\end{aligned}
\tag{L145.10}
\]

The correction estimate already carries two powers of \(R^{-1}\). Multiplication by the normal coordinate adds the third. These exact inequalities account for the constant 6 and the exponent 3.

For codimension \(k\), take an orthogonal flag \(W=E_0\subset E_1\subset\cdots\subset E_k=\mathbb C^n\), adding one complex normal coordinate at each step. Step \(j\) uses

\[
\theta_j=\phi+3(j-1)\log R.
\tag{L145.11}
\]

In an orthogonal normal split, \(R(\zeta,w)=R(\zeta,0)+|w|^2\), so

\[
\theta_j(\zeta,w)-\theta_j(\zeta,0)
\ge-C+3(j-1)\log\left(1+\frac{|w|^2}{R(\zeta,0)}\right)
\ge-C\quad(|w|<1).
\tag{L145.12}
\]

The one-sided constant stays \(C\). Each output norm becomes the next input norm, with one extra factor \(6\pi e^C\) and three extra lost powers. Formal E6 proves all restrictions and norm bounds on this actual flag. The result is (L145.2), not a bound with a new oscillation constant at every stage.

![Codimension iteration and two explicitly qualified norm bounds](figures/codimension-and-norm-budgets.png)

*Figure 2. Step \(j\) has complex dimension \(m+j\) and weight loss \(R^{-3j}\); it retains the same normal-comparison constant. The right panel plots proved upper bounds, with \(C=1\), rather than actual solution norms. The universal bound is \((6\pi e)^j\). For the stronger normal-monotone example below, the direct extension has the smaller bound \(B_j=\pi^j(2j-1)!/(3j-1)!\), with \(B_0=1\). Both curves are normalized by the initial finite norm. Formal E6 and E9 give their distinct hypotheses. Human source for the universal extension bound: Hörmander II, Theorem 15.1.3.*

## 4. Four worked examples

### Example 1. A radial weight with genuine finite data

Take \(\phi(z)=\sqrt{1+|z|^2}\). Its real gradient has length \(|z|/\sqrt{1+|z|^2}\le1\), so it satisfies (L145.1) with \(C=1\). Its Levi form is positive: in a radial complex direction its eigenvalue is \((2+|z|^2)/(4(1+|z|^2)^{3/2})\), and in a complex orthogonal direction it is \(1/(2\sqrt{1+|z|^2})\). Exercise 5 verifies these formulas. A polynomial on \(W\) has finite weighted norm, because exponential radial decay dominates every polynomial. More explicitly, a degree\(D\) polynomial has modulus at most \(A(1+r)^D\). On the shell \(\ell\le r<\ell+1\), its weighted square integral is at most a fixed constant times \((\ell+2)^{2D+2m}e^{-\ell}\), where \(m=\dim_\mathbb C W\). The ratios of successive terms tend to \(e^{-1}<1\), so their sum is finite. The case \(m=0\) is simply the finite point norm.

Here \(\phi(\zeta,w)\ge\phi(\zeta,0)\) for every normal \(w\). The direct entire extension \(U(\zeta,w)=u(\zeta)\) already works. For \(k\ge1\), formal E9 gives

\[
\int|U|^2e^{-\phi}R^{-3k}dV
\le B_kJ_0,
\qquad B_k=\pi^k\frac{(2k-1)!}{(3k-1)!}.
\tag{L145.13}
\]

This stronger example has an additional global normal-monotonicity property. It illustrates that the universal constant need not be attained. The general theorem does not assume this property.

### Example 2. A point datum and an affine weight

In \(\mathbb C\), let \(W=\{0\}\), \(\phi(z)=\operatorname{Re}z\), and \(u(0)=c\). Then \(C=1\) is valid, \(J_0=|c|^2\), and the extension

\[
U(z)=ce^{z/2}
\tag{L145.14}
\]

has \(|U|^2e^{-\phi}=|c|^2\). Hence

\[
\int_\mathbb C|U|^2e^{-\phi}(1+|z|^2)^{-3}dA
=\frac\pi2|c|^2\le6\pi e,J_0.
\tag{L145.15}
\]

The constant extension \(c\) would have infinite norm when \(c\ne0\): on a fixed-width strip extending toward negative real infinity the weight \(e^{-\operatorname{Re}z}\) outgrows the polynomial denominator. Keeping the datum independent of normal coordinates is therefore not a general weighted solution. For the stated divergence, write \(z=-t+iy\), \(t\ge1\), \(0\le y\le1\). Then \(R(z)\le3t^2\), so the integrand is at least \(|c|^2e^t/(27t^6)\). The positive exponential series gives \(e^t\ge t^7/7!\), which makes that strip integral infinite.

### Example 3. A normal affine drift with nonzero tangential data

In \(\mathbb C^2\), with coordinates \((\zeta,w)\), let

\[
\phi(\zeta,w)=\sqrt{1+|\zeta|^2}+\operatorname{Re}w,
\quad W=\{w=0\},\quad u(\zeta)=\zeta^p,
\quad p\in\mathbb N\cup\{0\}.
\tag{L145.16}
\]

The weight is PSH, and its real gradient has length at most \(\sqrt2\), so \(C=\sqrt2\) is valid. The tangential norm \(J_0\) is finite. The explicit extension \(U=\zeta^p e^{w/2}\) cancels the normal affine drift in its squared weighted modulus. Integrating first in \(w\) gives

\[
\int_{\mathbb C^2}|U|^2e^{-\phi}R^{-3}dV
=\frac\pi2\int_\mathbb C|\zeta|^{2p}e^{-\sqrt{1+|\zeta|^2}}
(1+|\zeta|^2)^{-2}dA(\zeta)
\le\frac\pi2J_0.
\tag{L145.17}
\]

Its normal weight difference can be negative: at \(\zeta=2,w=-3/4\), it equals \(-3/4\). Adding \(3\ell\log R\), \(\ell\ge0\), changes that difference to

\[
-\frac34+3\ell\log\left(1+\frac9{80}\right)\ge-\frac34>-\sqrt2.
\tag{L145.18}
\]

This is an exact example of the one-sided comparison retaining its original lower bound despite the added logarithms.

### Example 4. Growth data without the original finite square norm

Let \(n=2\), \(W=\{z_2=0\}\), \(\phi(z)=\operatorname{Re}z_1\), and \(u(z_1)=e^{z_1}\). The growth premise holds with \(C_1=1\), and the unit-oscillation bound holds with \(C=1\). But

\[
\int_W|u|^2e^{-\phi}dS
=\int_\mathbb C e^{\operatorname{Re}z_1}dA=\infty.
\tag{L145.19}
\]

The growth corollary still applies. Here \(m=1\), \(\beta=m+1=2\), \(N=n+2k+1=5\), and its modified input norm is

\[
\int_\mathbb C|u|^2e^{-2\phi}(1+|z_1|^2)^{-2}dA=\pi.
\tag{L145.20}
\]

The explicit entire extension \(U=e^{z_1}\) even satisfies the growth bound with \(C_2=1\), because \((1+|z|)^5\ge1\). Its full modified square norm is \(\int_{\mathbb C^2}(1+|z|^2)^{-5}dV=\pi^2/12\). This confirms why the corollary must not silently impose the original norm hypothesis.

## 5. The growth proof in a few exact steps

Put \(m=n-k\), \(\beta=m+1\), and \(\Theta=2\phi+\beta\log R\). The logarithm is PSH and globally 1-Lipschitz, so \(\Theta\) has unit-oscillation constant \(C_*=2C+\beta\). The growth datum satisfies

\[
\int_W|u|^2e^{-\Theta}dS
\le C_1^2\int_W R^{-(m+1)}dS
=C_1^2\frac{\pi^m}{m!}.
\tag{L145.21}
\]

Formal E7 proves that radial integral using a positive Laplace integral and the Gaussian integral. Applying weighted extension gives finite

\[
A=\int|U|^2e^{-2\phi}R^{-N}dV,
\qquad N=(m+1)+3k=n+2k+1.
\tag{L145.22}
\]

The entire \(U\) is harmonic. Average over the unit ball centered at \(z\), use weighted Cauchy–Schwarz, and compare the weight there with its center value. Since \(\phi(w)<\phi(z)+C\) and \(1+|w|^2\le2(1+|z|)^2\) on that ball,

\[
|U(z)|^2\le\frac{A}{b_n}e^{2\phi(z)+2C}2^N(1+|z|)^{2N},
\quad b_n=|B_{\mathbb R^{2n}}(0,1)|.
\tag{L145.23}
\]

Taking square roots proves (L145.3). Formal E8 writes both weighted integrals in this Cauchy–Schwarz step; the pointwise bound is obtained from the fixed-radius ball mean, not from arbitrary pointwise evaluation of an \(L^2\) representative.

## 6. Exercises

1. **Basic.** Verify the weak derivative of the cutoff, including the absence of first-derivative measures on the joining circles. Compute the exact square area integral of \(\bar\partial\eta/w\).
2. **Basic.** Why does an almost-everywhere ambient identity not by itself establish a restriction on \(W\)? Reproduce the normal-pole contradiction, including the zero-dimensional tangential case.
3. **Intermediate.** Derive every factor in \(6\pi e^C\) and explain the loss of exactly three powers of \(R^{-1}\) in one step.
4. **Intermediate.** Verify the lower comparison in the \(j\)-th flag step. Explain why estimating a new two-sided oscillation constant is unnecessary for iteration.
5. **Intermediate.** Prove that \(\sqrt{1+|z|^2}\) is PSH and has the required unit-oscillation bound. Why does \(a|z|^2\), \(a>0\), fail this global bound?
6. **Intermediate.** Prove (EX32), and compute \(B_1,B_2,B_3\). State the additional assumption needed to apply these bounds to the normal-independent extension.
7. **Intermediate.** Compute \(m,\beta,C_*,N\) for \(n=4,k=2\). Explain why \(2\phi\), rather than \(\phi\) alone, occurs in the growth proof.
8. **Intermediate.** Verify all norm and growth assertions in Example 4, including \(\pi^2/12\), without a numerical approximation.
9. **Advanced.** Explain how unitary coordinates and the \(k\)-step restriction chain cover an arbitrary complex linear subspace, including \(W=\{0\}\). Identify the measure used in that endpoint case.
10. **Advanced.** Write the full weighted Cauchy–Schwarz inequality for the harmonic ball mean. Recover the constant in (L145.23) and explain which quantities remain fixed when evaluating different centers.

## 7. Complete solutions

**1.** On the middle annulus the radial slope is \(-2\). Since \(\bar\partial |w|=w/(2|w|)\), the derivative is \(-w/|w|\); it is zero on the two constant regions. Integration by parts on the three pieces gives opposite boundary contributions at each joining circle with the same cutoff value, so they cancel. First derivatives therefore have no circle-supported term. The quotient has modulus \(1/r\) on \(1/2<r<1\), hence

\[
\int_\mathbb C\left|\frac{\bar\partial\eta}{w}\right|^2dA
=2\pi\int_{1/2}^1\frac{dr}{r}=2\pi\log2.
\tag{L145.24}
\]

This is at most \(4\pi\), the coarse bound from modulus at most2 on a disk of area \(\pi\). The sharper integral could improve a one-step estimate, but is not needed to prove the source's constant.

**2.** A positive-codimension subspace has zero ambient volume, so an ambient almost-everywhere equality can omit it entirely. Instead, both \(U\) and the normal-independent \(u\) are entire, and their difference \(G\) is continuous. A nonzero value at a point of the subspace gives \(|G|\ge c>0\) on a product neighborhood. There \(G=-wv\) almost everywhere off the axis, implying \(|v|^2\ge c^2|w|^{-2}\). The integral \(2\pi\int_0^\varepsilon dr/r\) is infinite. Fubini multiplies it by a positive finite tangential neighborhood volume, contradicting local \(L^2\). With no tangential coordinates that multiplier is1, and the same normal integral proves the point restriction. No selected value of \(v\) on the axis was used.

**3.** The normal tube comparison has factor \(\pi e^C\). The last data coefficient has modulus at most \(2|u|\), giving data square norm at most \(4\pi e^C J\). L144's estimate divides that bound by2, giving the correction norm at most \(2\pi e^C J\) with weight \(R^{-2}\). The square of the difference in (L145.8) is at most twice each square. The cutoff part therefore costs at most \(2\pi e^C J\); the correction part costs at most \(4\pi e^C J\). Their sum is \(6\pi e^C J\). Since \(|w|^2R^{-3}\le R^{-2}\), multiplication by \(w\) is paid for by one extra inverse power. The two powers already present in the solved equation become three.

**4.** Orthogonal coordinates give \(R(\zeta,w)=R(\zeta,0)+|w|^2\). The original oscillation assumption gives \(\phi(\zeta,w)-\phi(\zeta,0)>-C\) for \(|w|<1\). The additional logarithm contributes a nonnegative term, proving (L145.12). The hyperplane lemma assumes only that lower comparison. It does not need the absolute difference of the two modified weights bounded by the same \(C\). Thus every flag step keeps the same factor \(6\pi e^C\), and multiplication gives the \(k\)-th power in (L145.2).

**5.** For \(s=|z|^2\), let \(h(s)=\sqrt{1+s}\). Then \(h'=1/(2\sqrt{1+s})\) and \(h''=-1/(4(1+s)^{3/2})\). Its Levi matrix is \(h'\delta_{jk}+h''\overline z_jz_k\). The complex radial eigenvalue is

\[
h'+s h''=\frac{2+s}{4(1+s)^{3/2}}>0,
\tag{L145.25}
\]

and every complex orthogonal eigenvalue is \(h'>0\). At zero all eigenvalues are1/2. Positive Levi form gives the circle submean inequality along each line by the usual real Laplacian/mean calculation, so the smooth function is PSH. Its real gradient length is \(r/\sqrt{1+r^2}\le1\); integrating along a segment makes it1-Lipschitz, so differences at distance less than1 are less than1. In contrast, for real points \(z=r\) and \(z'=r+1/2\) in one coordinate, the difference of \(a|z|^2\) is \(a(r+1/4)\), which grows without bound. A strictly PSH Gaussian weight can be used in L144, but it does not satisfy this extension theorem's global unit-oscillation premise.

**6.** Repeated integration by parts gives \(\int_0^\infty t^{q-1}e^{-at}dt=(q-1)!a^{-q}\). Use this with \(a+|w|^2\) in place of \(a\), integrate by Tonelli, and insert \(\int_{\mathbb C^p}e^{-t|w|^2}dV=(\pi/t)^p\). The remaining integral is \(\int_0^\infty t^{q-p-1}e^{-at}dt\), which converges because \(q>p\), and equals \((q-p-1)!a^{p-q}\). This proves (EX32). For \(q=3k,p=k,a=1\),

\[
B_1=\pi/2,\qquad B_2=\pi^2/20,\qquad B_3=\pi^3/336.
\tag{L145.26}
\]

To bound the actual normal-independent extension by \(B_kJ_0\), one also needs \(\phi(\zeta,w)\ge\phi(\zeta,0)\) for all normal \(w\). That allows dropping the extra normal weight factor in the full normal integral. Unit-scale oscillation alone does not give it; the affine-weight Example 2 shows that the direct extension can fail without it.

**7.** Here \(m=2\), \(\beta=3\), \(C_*=2C+3\), and \(N=3+3\cdot2=9=4+2\cdot2+1\). The growth hypothesis bounds \(|u|^2\) by \(C_1^2e^{2\phi}\). Multiplying by \(e^{-2\phi}\) cancels that exponential and leaves the integrable radial factor \(R^{-(m+1)}\). Using \(e^{-\phi}\) would leave a factor \(e^\phi\), which need not be integrable on the subspace. The added logarithm supplies precisely the radial integrability needed for the finite-dimensional tangential volume.

**8.** The functions \(\phi=\operatorname{Re}z_1\) and \(u=e^{z_1}\) satisfy \(|u|=e^\phi\). The original norm is infinite: on \(\operatorname{Re}z_1\ge0\) and \(0\le\operatorname{Im}z_1\le1\), its integrand is at least1, and that strip has infinite area. In the modified norm, \(|u|^2e^{-2\phi}=1\), so (EX32) with \(p=1,q=2,a=1\) gives \(\pi\). The entire \(U=e^{z_1}\) satisfies the pointwise bound with \(C_2=1\), since \((1+|z|)^5\ge1\). For its full modified norm, (EX32) with \(p=2,q=5,a=1\) gives \(\pi^2(2)!/(4)!=\pi^2/12\). Both calculations use ordinary real4-dimensional volume in the ambient case, not area on the line.

**9.** Apply complex Gram–Schmidt to a basis of \(W\), then complete it to an orthonormal basis of \(\mathbb C^n\). The unitary change sends \(W\) to the first \(m=n-k\) coordinate directions. Its determinant has complex modulus1, and its real volume Jacobian is1. Restricting the ambient weight and adding the normal directions produces \(E_0,\ldots,E_k\). At each step the hyperplane lemma gives an entire pointwise restriction equal to the previous function; composing these equalities gives \(U|_W=u\). When \(W=\{0\}\), the first input norm is \(|u(0)|^2e^{-\phi(0)}\), using the zero-dimensional point measure 1. The first ambient extension step has one complex coordinate and is exactly the \(d=1\) case of the proved hyperplane argument.

**10.** The harmonic mean is \(U(z)=b_n^{-1}\int_{B(z,1)}U(w)dV(w)\). Split its integrand into \(U(w)e^{-\phi(w)}R(w)^{-N/2}\) and \(e^{\phi(w)}R(w)^{N/2}\), then apply Cauchy–Schwarz. The first square integral is at most the global fixed \(A\). The second is at most

\[
b_n e^{2\phi(z)+2C}2^N(1+|z|)^{2N}.
\tag{L145.27}
\]

Multiplication by \(b_n^{-2}\) gives (L145.23), and square roots give \(C_2=e^C2^{N/2}\sqrt{A/b_n}\). The unit-ball volume, norm \(A\), exponent \(N\) and oscillation constant \(C\) remain fixed for every center; only the displayed center factors change. The argument uses the entire representative and the proved harmonic mean identity, so evaluating \(U(z)\) is justified.

## 8. Source and reproduction

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.1, Theorem 15.1.3 and Corollary 15.1.4, printed pp. 274–276; 1983 edition, second revised printing 1990, reprint 2005. These proof expositions, examples, full solutions and illustrations are original. Protected source text, book pages and media are excluded.

The reproduction folder retains the two native PNG/SVG figure pairs, exact geometry, plotting script and independent calculation checks. The plotted normal-pole obstruction and upper norm budgets are explicitly distinguished from an actual returned solution. The normal-monotone comparison has its own additional hypothesis. The full formal proof covers the original general extension statement. Later analytic-functional representation and other assigned targets remain separate work; this lesson does not claim the whole course is complete.
