# Integral representations for arbitrary distributions

*Original learner exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

A distribution may require increasingly many derivatives to test it near the edge of its domain. The representation must accommodate those orders. We construct one complex-frequency integral for every distribution and one actual characteristic-surface integral for every homogeneous distributional solution.

The [complete proof](distribution-representations-formal.md) solves both unnumbered exercises on printed page300 of Hörmander's Chapter15. It includes the finite-envelope smoothing argument needed to test the repaired transforms. The same formulas include all repeated-factor polynomial amplitudes and use the exact Euclidean surface measure.

## The two formulas and their meanings

Let \(X\subset\mathbb R^n\) be open and convex, \(D=-i\partial\), and
\(F_v(z)=\int v(x)e^{-ix\cdot z}\,dx\).
For every \(u\in\mathcal D'(X)\), there are a strict PSH weight \(\phi\) and a measurable whole-space density with
\[
\int_{\mathbb C^n}|U(z)|^2e^{2\phi(-z)}dV(z)<\infty,\qquad
u(v)=\int_{\mathbb C^n}U(z)F_v(-z)dV(z)
\quad(v\in C_c^\infty(X)).
\tag{L155.1}
\]
The tested integral converges absolutely. It describes the distribution even when the untested exponential integral is not an ordinary function.

For a nonconstant polynomial \(P=c\prod P_\ell^{m_\ell}\), a direction \(P_m(\tau)\ne0\), and \(P(D)u=0\), put \(N_\ell=\{P_\ell=0\}\). The second formula is
\[
u(x)=\sum_{\ell}\sum_{a=0}^{m_\ell-1}
 (x\cdot\tau)^a\int_{N_\ell}U_\ell^a(z)e^{ix\cdot z}\,dS_\ell(z)
\quad\text{in }\mathcal D'(X).
\tag{L155.2}
\]
Surface measure is Euclidean real \(2n-2\) area on the regular reduced charts; it is counting measure in dimension one. The norm is the sum of
\(\int|U_\ell^a|^2e^{2\phi(-z)}(1+|z|^2)^{-K}dS_\ell\).
Every compact smooth test yields an absolutely convergent sum of integrals. The polynomial loss \(K\) is the explicit degree-and-dimension quantity [AR24](distribution-representations-formal.md#eq-AR24).

The weight satisfies three properties: for every compact convex \(K\Subset X\), \(e^{-\phi(z)}\le C_K(1+|z|)^{N_K}e^{-H_K(\operatorname{Im}z)}\); its gradient is bounded by \(C+\log(1+|\operatorname{Im}z|)\); and its Levi matrix is at least \(c(1+|\operatorname{Im}z|^2)^{-3/4}I\). The exponent \(-3/4\) is the exact current-source exponent.

## How the arbitrary-order step works

For a given distribution, [L153](../../AN02-L153.html#tp1-the-four-exact-neighborhood-descriptions) describes a small neighborhood using finitely many derivative bounds on each entire exterior \(X\setminus K_j\). The required order changes with \(j\). We enlarge that order to include the next region's needs and leave a factor-eight margin in its threshold.

The successive Fourier-envelope powers incorporate each of these finite requirements. Earlier carrier terms are suppressed by a logarithmic contour with a strict separation gap; later terms receive sufficiently high real-frequency decay. Each finite strict weight has a finite envelope. Its repaired inverse transform is globally continuous and has all the required derivatives on the relevant exterior neighborhoods.

Physical mollifiers therefore converge in the finitely many derivative orders relevant to that compact carrier. The mollified transform lies in the original distribution's small neighborhood. Entire division makes the complementary mollified term a legitimate equation test. This yields a uniform surface-jet bound, and then a Hilbert representing vector supplies the densities. [AR2–AR3](distribution-representations-formal.md#ar2-finite-envelopes-that-survive-physical-smoothing) prove every step, including identification of higher exterior derivatives by tested contours.

## Worked example 1: orders that grow toward the boundary

On \(X=(-1,1)^2\), let
\[
a_l=1-2^{-l},\qquad
u=1_{x_1}\otimes\sum_{l\ge1}2^{-l}\delta^{(l)}_{a_l}(x_2).
\tag{L155.3}
\]
Here \(1_{x_1}\) is the constant distribution in the first coordinate, and \(\delta^{(l)}\) denotes the ordinary \(\partial_{x_2}\) derivative of a point mass. Thus
\[
u(v)=\sum_{l\ge1}2^{-l}(-1)^l
 \int_{-1}^1\partial_{x_2}^l v(x_1,a_l)\,dx_1.
\tag{L155.4}
\]
Every compact support is separated from the boundary \(x_2=1\), so this sum has only finitely many active terms on each test stage. Their derivative suprema bound the action, proving that this is a distribution. It satisfies \(D_1u=0\), since integration of a compact first-coordinate derivative is zero.

Its local orders are unbounded. Isolate one \(a_l\) by a cutoff equal to one near that point and supported away from the others. A shrinking test with an \(l\)-th derivative of fixed nonzero size, and lower derivatives tending to zero, shows order at least \(l\). The nonzero coefficient \(2^{-l}\) does not change this order.

There is no single global moderate weight placing this \(u\) in a local \(B_{2,w}\) class. Such a weight has a lower polynomial bound \(w(\xi)\ge c\langle\xi\rangle^{-N}\), so that class lies in \(H^{-N}_{\rm loc}\). After the isolating cutoff, the Fourier transform is a nonzero rapidly decreasing first-coordinate factor times \(\xi_2^l e^{-ia_l\xi_2}\). On a bounded \(\xi_1\) interval where the first factor is bounded below, its \(H^{-N}\) integral contains \(\int_1^\infty \xi_2^{2l-2N}\,d\xi_2\), which diverges when \(N\le l+1/2\). Arbitrarily large \(l\) exclude every fixed \(N\). The general surface theorem nevertheless applies to \(P(z)=z_1\).

## Worked example 2: an explicit whole-complex density for a point mass

In dimension one take \(a=2\), \(t=4096\), \(R=t^{-1/2}=1/64\), and \(X=(-R,R)\). Set
\[
p_t(\eta)=\frac{\sqrt{t^2+\eta^2}}{\sqrt t}
 -(t^2+\eta^2)^{1/4},\qquad
\phi(\xi+i\eta)=p_t(\eta)-2\log(t^2+\xi^2+\eta^2).
\tag{L155.5}
\]
The exact seed calculation in [L153 TP6](../../AN02-L153.html#tp6-full-seed-bounds-and-their-uniform-active-region) gives its strict Levi bound because \(\sqrt t=32a\). Its gradient is bounded. For a compact \(K\Subset X\), let \(r_K=\max_{x\in K}|x|<R\). The inequality
\(p_t(\eta)\ge R|\eta|-\sqrt{t+|\eta|}\)
shows \(p_t(\eta)\ge r_K|\eta|-C_K\); a positive linear gap absorbs the square root. Hence the growth part of the weight condition holds with polynomial order four.

For \(0\le r\le3\), the explicit density
\[
U_r(z)=\frac{z^r}{2\pi\sqrt\pi}e^{-(\operatorname{Im}z)^2}
\tag{L155.6}
\]
represents \(D^r\delta_0\), where \(D=-i\partial\):
\[
\int_{\mathbb C}U_r(z)F_v(-z)\,d\xi\,d\eta
=(-1)^r(D^rv)(0)=(D^r\delta_0)(v).
\tag{L155.7}
\]
To verify it, fix \(\eta\). Substitute \(w=-z\) in the real-frequency integral and shift its horizontal line to the real axis. The complete fixed-height rectangle argument has vanishing boundary: \(F_v\) has arbitrary real-frequency decay on that bounded imaginary strip. Fourier inversion then gives \(2\pi(-1)^r(D^rv)(0)\). Integration of \(e^{-\eta^2}/\sqrt\pi\) gives one. Fubini is legitimate for these compact tests: their entire decay supplies an integrable real-frequency majorant with only polynomial and \(e^{r_K|\eta|}\) imaginary growth, dominated by the Gaussian.

The weighted norm also converges. Put \(M=\sqrt{t^2+\eta^2}\). Since \(e^{2\phi}=e^{2p_t}(M^2+\xi^2)^{-4}\), the real integral is a finite binomial sum of
\[
\begin{aligned}
\int_{\mathbb R}(M^2+\xi^2)^{-4}d\xi&=5\pi/(16M^7),\\
\int_{\mathbb R}\xi^2(M^2+\xi^2)^{-4}d\xi&=\pi/(16M^5),\\
\int_{\mathbb R}\xi^4(M^2+\xi^2)^{-4}d\xi&=\pi/(16M^3),\\
\int_{\mathbb R}\xi^6(M^2+\xi^2)^{-4}d\xi&=5\pi/(16M).
\end{aligned}
\tag{L155.8}
\]
These identities are proved in solution7 below. The remaining \(\eta\) integrand contains \(e^{-2\eta^2+2p_t(\eta)}\) times a polynomial factor; its Gaussian decay dominates the at-most-linear \(p_t\). Thus the actual finite weight and density satisfy the whole-complex theorem's norm.

![Exact normalized real-frequency energy and three normalized imaginary-frequency profiles.](figures/point-mass-complex-density-and-weighted-energy.png)

The left panel shows the exact \(\eta=0\) energy shapes \(q^{2r}(1+q^2)^{-4}\), \(q=\xi/t\), after removing the stated common positive constants and powers of \(t\). The right shows normalized profiles of widths \(1/2,1,2\). Each profile yields the same point-mass formula. Coordinates, normalization, norm and proof locations are recorded in [geometry.json](figures/geometry.json); the [figure source](make_figures178.py) reproduces both PNG and SVG.

## Worked example 3: a genuinely distributional surface integral

In \(\mathbb R^2\), take \(P(z)=z_1\), \(\tau=(1,0)\), and \(X=B(0,1/64)\). Its characteristic hypersurface is the complex plane \(N=\{z_1=0\}\). The coordinates \(z_2=\xi_2+i\eta_2\) identify its exact Euclidean area with \(d\xi_2\,d\eta_2\), without a metric or Jacobian factor.

On this plane use
\[
U^0(0,z_2)=\frac{z_2^3}{2\pi\sqrt\pi}e^{-\eta_2^2}.
\tag{L155.9}
\]
Then
\[
1_{x_1}\otimes D_2^3\delta_0(x_2)
=\int_N U^0(z)e^{ix\cdot z}\,dS(z)
\quad\text{weakly on }X.
\tag{L155.10}
\]
Indeed \(F_v(0,-z_2)\) is the one-dimensional transform of the compact marginal \(\int v(x_1,x_2)dx_1\); example2 supplies its exact pairing. The result solves \(D_1u=0\) and is not an ordinary continuous function.

The radial two-dimensional version of L155.5 has the same strict Levi seed bound and the same growth condition on this ball. Restricted to \(N\), the norm in AR22 includes the already-integrable example2 norm, multiplied by \(W^{-K}\le1\). All densities and the surface measure are actual ones in the theorem.

## Worked example 4: all jets at a repeated characteristic point

Take \(P(z)=(z-i)^3\) and \(\tau=1\) on any open interval. The characteristic set is the single point \(\{i\}\), with counting measure. The formula must retain three amplitudes:
\[
u(x)=(c_0+c_1x+c_2x^2)e^{-x}.
\tag{L155.11}
\]
These are all distributional solutions. Multiplication by \(e^x\) transforms \((D-i)^3u=0\) into \(D^3(e^xu)=0\). A distribution with zero first derivative is constant: every zero-integral compact test is the derivative of a compact smooth primitive, so it is annihilated; subtract its integral times one fixed unit-integral test to identify the remaining constant action. Apply this result successively to the second derivative, first derivative and function of \(e^xu\), subtracting their polynomial primitives. The result is a polynomial of degree at most two.

Thus \(U^0(i)=c_0\), \(U^1(i)=c_1\), \(U^2(i)=c_2\) give the actual surface densities. Their weighted norm is a finite sum at one point. Omitting the highest jet loses the solution \(x^2e^{-x}\).

![All three repeated-root kernels and the first seven positions and derivative orders in a locally finite distribution.](figures/repeated-root-jets-and-increasing-local-orders.png)

The left panel displays the three exact kernels, with their common characteristic frequency \(i\) and counting measure. The right displays the first seven \((a_l,l)\) pairs from example1; the dashed edge \(x_2=1\) lies outside the open domain. The infinite locally finite distribution is defined by L155.3–L155.4, not by the seven plotted samples.

## Exercises with complete solutions

1. **Show why the whole-space formula defines a distribution for any density with the stated norm.** Cauchy–Schwarz bounds its absolute tested integral by \(\|U\|_{e^{2\phi(-z)}}q_\phi(v)\). On a fixed compact support, integration by parts gives whole-complex decay of any desired integer power. Choose that power larger than the growth weight's \(N_K+n\), so the squared complex-volume integral is bounded by a finite derivative seminorm squared. This proves continuity on each support stage, which is the topology of \(\mathcal D(X)\); linearity is the complex-linear integral. No pointwise integral is needed.

2. **Determine the Fourier reflection and the density obtained from a Hilbert vector.** With inner product linear in the first entry, the representing identity is \(\int F_v(s)\overline{g(s)}e^{-2\phi(s)}dV(s)\). Set \(s=-z\), which preserves Euclidean volume. The physical kernel is tested as \(v(e^{ix\cdot z})=F_v(-z)\), so \(U(z)=\overline{g(-z)}e^{-2\phi(-z)}\). Its norm is \(\int|g(-z)|^2e^{-2\phi(-z)}dV(z)=\|g\|^2\). This checks the conjugation, sign and norm.

3. **Explain the extra derivative order in \(A_j=\max_{l\le j+1}L_l\).** To mollify on \(X\setminus K_j\), values in a small surrounding neighborhood also matter. For \(j\ge3\), that neighborhood is separated from \(K_{j-1}\); the finite-envelope proof gives regularity through \(A_{j-1}\ge L_j\) there. Uniform continuity on its compact intersection with the fixed carrier proves derivative convergence through \(L_j\). Orders \(j=0,1,2\) are covered by the global real inversion powers. A carrier in \(\operatorname{int}K_{J+2}\) leaves only finitely many \(j\)'s to check, and the factor-eight margin gives every AR8 bound after a sufficiently small radius is chosen.

4. **Verify the logarithmic contour's exact divergence identity.** Let \(\ell=\log(2+|\xi|^2)\), \(z_s=\xi+isR\eta\ell\), and \(J_s=1+isR\eta\cdot\nabla\ell\). For entire \(H\), direct differentiation gives
\[
\partial_s[H(z_s)J_s]
=\sum_{l=1}^n\partial_{\xi_l}[iR\eta_l\ell H(z_s)].
\tag{L155.12}
\]
The right side expands to \(iR(\eta\cdot\nabla\ell)H+iR\ell(\eta\cdot\partial_zH)J_s\), exactly the left side. For \(H=F F_\chi(-z)\), the test transform supplies arbitrary decay, while the finite carrier supplies only a fixed logarithmic-contour growth power. Choose the test-decay power beyond that growth and the boundary face dimension. Cube boundary flux then tends to zero, proving the tested contour equality.

5. **Give a compact inverse transform for which a high-order real-plane derivative integral is not absolute.** Let \(b(x)=(1-|x|)_+\), and \(f=b*b*b\). Direct integration gives \(F_b(z)=2(1-\cos z)/z^2\), with its removable value at zero; hence
\[
F_f(z)=\left(\frac{2(1-\cos z)}{z^2}\right)^3,\qquad
\xi^6F_f(\xi)=8(1-\cos\xi)^3.
\tag{L155.13}
\]
The latter nonnegative periodic function has a positive integral on every period, so its real absolute integral diverges. Yet \(f\) is supported in \([-3,3]\) and equals zero smoothly outside this carrier. Its sixth derivative is a finite sum of point masses because \(b''\) is such a sum; its fifth derivative has jumps and \(f\) is \(C^4\). The high exterior derivatives are therefore identified by tested contours, not by an unjustified sixth-order real integral.

6. **Show exactly where the homogeneous equation is used after repair.** Entire division gives \(v_{2,J}=cP(-D)a_J\) with a compact carrier. Mollification gives a legitimate smooth compact \(a_J*\rho_\epsilon\). Therefore \(u(v*\rho_\epsilon)=u(v_{1,J}*\rho_\epsilon)+c\,u(P(-D)(a_J*\rho_\epsilon))=u(v_{1,J}*\rho_\epsilon)\). The second term is zero by \(P(D)u=0\). The finite-envelope lemma bounds the remaining term; smooth \(v*\rho_\epsilon\to v\) gives the required limit. It never pairs two rough distributions.

7. **Prove all four real-frequency norm integrals in L155.8.** Let \(I_p(M)=\int(M^2+\xi^2)^{-p}d\xi\). The arctangent primitive gives \(I_1=\pi/M\). Integrate the derivative of \(\xi(M^2+\xi^2)^{-(p-1)}\); its boundary values vanish for \(p\ge2\), giving \(I_p=(2p-3)I_{p-1}/[(2p-2)M^2]\). Thus \(I_2=\pi/(2M^3)\), \(I_3=3\pi/(8M^5)\), \(I_4=5\pi/(16M^7)\). Expanding \(\xi^2=(M^2+\xi^2)-M^2\) gives \(I_3-M^2I_4=\pi/(16M^5)\). Its square gives \(I_2-2M^2I_3+M^4I_4=\pi/(16M^3)\). Its cube gives \(I_1-3M^2I_2+3M^4I_3-M^6I_4=5\pi/(16M)\). This proves the four exact integrals.

8. **Replace the imaginary Gaussian by another width and show that the density is not unique.** For any \(\sigma>0\), set \(g_\sigma(\eta)=e^{-\eta^2/\sigma^2}/(\sqrt\pi\sigma)\) and \(U_{r,\sigma}(z)=z^rg_\sigma(\operatorname{Im}z)/(2\pi)\). The fixed-height real integral remains \(2\pi(-1)^r(D^rv)(0)\), and \(\int g_\sigma=1\). Its squared Gaussian still dominates the at-most-linear weight in the imaginary variable, and L155.8 proves the real-frequency norm. Distinct widths therefore give distinct actual densities for the same distribution.

9. **Why must the repeated-root formula include the highest polynomial amplitude?** If \(x^2e^{-x}=c_0e^{-x}+c_1xe^{-x}\) on an interval, multiplication by \(e^x\) would give the polynomial identity \(x^2=c_0+c_1x\). Twice differentiating contradicts \(2=0\). The characteristic point has multiplicity three, so all amplitudes \(a=0,1,2\) are required. The zero-first-derivative distribution argument in example4 proves that these three already include every distributional solution.

10. **Explain the zero-polynomial and constant-polynomial endpoints.** For a nonzero constant \(P\), \(P(D)u=0\) forces \(u=0\), represented by an empty surface sum. For \(P=0\), every distribution solves the equation, but there is no noncharacteristic highest-degree direction or nonconstant factorization of the prescribed kind. The arbitrary whole-complex formula L155.1 supplies its actual representation. Empty \(X\) has only the zero distribution; choosing zero densities and the strict seed \(p_1\) covers both statements.

## Reproduce and inspect

The [formal source](distribution-representations-formal.md), [numerical checks](check_examples178.py), [actual check results](independent-example-checks178.json), [figure program](make_figures178.py), [exact figure geometry](figures/geometry.json) and [reproduction guide](README-reproduce.md) are supplied. Numerical checks supplement the proofs. In particular any auxiliary Gaussian test used for sign checks is explicitly outside the compact-test theorem; the complete compact-test convergence and all arbitrary-distribution conclusions are proved above.

The human source is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, the two unnumbered representation exercises on printed p.300 after15.4.3. The material here is original exposition; it includes no protected book body or source-page image. The course's Chapter15 notes, remaining passage audit, Chapter16 and all assigned earlier residuals remain active.
