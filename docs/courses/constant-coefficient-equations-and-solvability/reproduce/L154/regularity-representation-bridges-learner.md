# Learning the real and complex regularity bridges

The two exercises compare exact conditions rather than merely related regularity theorems. The positive-order derivative strength keeps the real ratio finite even at a multiple zero. A nearest complex zero transfers a moderate weight ratio between real space and the characteristic set. The directional derivative estimate then comes from an actual convergent exponential integral and an exponential moment bound.

Read [EB1–EB4, the complete proof](../../AN02-L154.html#complete-proof). Our convention is \(D=-i\partial\). The physical solution weights are \(k,k_1\); the tube theorem is applied with their appropriate reflected reciprocal test weights.

## Worked example 1. A repeated complex root and the full strength

Take \(P(z)=(z-i)^2\) and real \(\xi\). Its only distinct zero is \(i\), of multiplicity two, so \(d=\sqrt{1+\xi^2}\). Ordinary derivatives give
\[
|P(\xi)|^2=d^4,\quad |P'(\xi)|^2=4d^2,\quad
|P''(\xi)|^2=4,\qquad
A=d^2+2,\quad B=2\sqrt{d^2+1},\quad
r_P=\frac{d^2+2}{2\sqrt{d^2+1}}.
\tag{L154.1}
\]
The positive-order strength includes both derivatives. Since
\((d^2+2)^2-d^2(d^2+1)=3d^2+4>0\), we have \(r_P\ge d/2\). Also \(d\ge1\), so
\[
\tfrac14(1+d)\le r_P\le(1+d)^2 .
\tag{L154.2}
\]
For the upper bound, \(2\sqrt{d^2+1}\ge2\), hence
\(r_P\le(d^2+2)/2\le(1+d)^2\).
At \(\xi=0\), \(r_P=3/(2\sqrt2)\); at large \(|\xi|\) it is asymptotic to \(d/2\). The proof uses these quantities only up to permitted constants and power changes.

At a real double zero, take instead \(P(z)=z^2\). Then
\[
A(\xi)=\xi^2+2,\quad B(\xi)=2\sqrt{\xi^2+1},\quad
r_P(0)=1.
\tag{L154.3}
\]
The raw quotient \(|P|/|P'|=|\xi|/2\) for \(\xi\ne0\) is undefined at zero and tends to zero there. It cannot replace the always-positive full strength ratio.

![Exact strengths and distances at repeated roots](figures/repeated-roots-strength-and-distance.png)

**Figure EB-A.** The left curves are the exact complex-root ratio in L154.1 and its stated lower comparisons. The right curves give the exact real-root full ratio and the raw quotient away from zero; the open circle marks the raw quotient's missing value at the collision. These are real samples of the stated complex polynomials, with the exact Euclidean complex distance retained.

## Worked example 2. The equation controls one direction

Let \(P(z_1,z_2)=z_1\). It is not hypoelliptic: any distribution independent of \(x_1\) solves \(D_1u=0\), including nonsmooth ones. Its characteristic set is \(\{z_1=0\}\), and for real \(\xi\),
\[
d_P(\xi)=|\xi_1|,\qquad
A(\xi)=\sqrt{1+\xi_1^2},\quad B=1,\quad
r_P=\sqrt{1+\xi_1^2}.
\tag{L154.4}
\]
With \(k_1=1\), choose \(k(\xi)=1+\xi_1^2=r_P^2\). The real criterion holds exactly. On every complex zero, \(k(\operatorname{Re}z)=1\), so the complex criterion holds with exponent zero, even though the real ratio is unbounded in the first coordinate.

An isotropic choice \(k_{\mathrm{iso}}(\xi)=\sqrt{1+\xi_1^2+\xi_2^2}\) fails both criteria: on the real zeros \((0,T)\), the strength ratio is one but \(k_{\mathrm{iso}}=\sqrt{1+T^2}\to\infty\); the imaginary part of that complex zero is zero.

For a concrete physical solution, \(u(x_1,x_2)=\mathbf1_{\{x_2>0\}}\) is locally \(L^2\) and solves \(D_1u=0\). Each compact cutoff has all its \(x_1\)-derivatives in \(L^2\), so the weight \(1+\xi_1^2\) gives the expected local directional gain. Its \(x_2\)-derivative is a nonzero delta on \(x_2=0\), which is not locally \(L^2\); thus the isotropic first-order gain fails there. This separates the general weight bridge from a hypoellipticity assumption.

## Worked example 3. Complex heat zeros distinguish the derivative orders

For the heat polynomial and operator,
\[
P(z)=z_1^2+iz_2,\qquad
P(D)=\partial_{x_2}-\partial_{x_1}^2,\qquad
z=(a+ib,\,-2ab+i(a^2-b^2))\in\{P=0\}.
\tag{L154.5}
\]
Its imaginary part is \(\eta=(b,a^2-b^2)\). If \(\eta\) stays bounded, both \(b\) and \(a\) stay bounded, hence so does the real part \((a,-2ab)\). This verifies the complete zero-escape criterion for hypoellipticity proved in [L021](../../AN02-L021.html#retreat-from-real-space-has-a-polynomial-rate).

The spatial coordinate obeys
\[
|z_1|^2=a^2+b^2\le|\eta_2|+2|\eta_1|^2
\le3(1+|\eta|)^2,\qquad
|z_2|=|z_1|^2\le3(1+|\eta|)^2 .
\tag{L154.6}
\]
Thus the spatial direction has permissible exponent one and the time direction exponent two.
Both are necessary: take \(a=b=t>0\). The exact zeros then satisfy
\[
z(t)=((1+i)t,-2t^2),\qquad
|\operatorname{Im}z(t)|=t,\quad
|z_1(t)|=\sqrt2\,t,\quad |z_2(t)|=2t^2.
\tag{L154.7}
\]
No lower power of \(1+t\) bounds the corresponding coordinate at all large \(t\).

The exponential moment in the proof also has an exact finite formula when \(\rho=1\) or \(2\), \(j\) is an integer, and \(\delta=1\). In two imaginary dimensions, with \(q=2\rho j\),
\[
\int_{\mathbb R^2}(1+|\eta|)^q e^{-2|\eta|}\,d\eta
=2\pi\sum_{l=0}^q
 \binom ql\frac{(l+1)!}{2^{l+2}}.
\tag{L154.8}
\]
Expand the integer power and use polar coordinates. The integral
\(\int_0^\infty r^{l+1}e^{-2r}dr=(l+1)!/2^{l+2}\) follows from scaling and repeated integration by parts. The full proof handles every permitted real \(\rho\), using the calculus supremum rather than requiring an integer expansion.

## Worked example 4. A heat solution attaining both growth orders

Fix \(a_0>0\), and on \(x_1>-a_0\), \(x_2\in\mathbb R\), put
\[
u(x_1,x_2)=\int_0^\infty
 \exp[-a_0s+(i-1)x_1s-2ix_2s^2]\,ds .
\tag{L154.9}
\]
Here \(ds\) is Lebesgue parameter measure on the displayed characteristic curve \(z(s)=((1+i)s,-2s^2)\). On every compact subset of this half-space, \(a_0+x_1\) has a positive lower bound. Every differentiated integrand is a polynomial in \(s\) times this fixed exponential decay, so dominated convergence gives a smooth solution. Each kernel satisfies
\(\partial_{x_2}e^{(i-1)x_1s-2ix_2s^2}=-2is^2e^{\cdots}
=\partial_{x_1}^2e^{\cdots}\).
Thus \(P(D)u=0\).

At the origin, the actual \(D\)-derivatives are
\[
D_1^ju(0,0)=
(1+i)^j\frac{j!}{a_0^{j+1}},\qquad
D_2^ju(0,0)=
(-2)^j\frac{(2j)!}{a_0^{2j+1}} .
\tag{L154.10}
\]
For example \(D_2u(0,0)=-4/a_0^3\); dropping the convention \(D=-i\partial\) would give an incorrect phase. The moments follow from
\(\int_0^\infty s^Ne^{-a_0s}ds=N!/a_0^{N+1}\).

The absolute spatial derivatives have growth \(C^j j^j\), and the absolute time derivatives have growth \(C^j j^{2j}\). Their elementary upper and lower factorial bounds, proved in Solution 10, show that neither power can be reduced for this solution. This makes the geometric distinction in Example 3 visible in one actual smooth solution.

![Exact heat characteristic geometry and attained derivative growth](figures/heat-zero-geometry-and-derivative-growth.png)

**Figure EB-B.** The left panel plots the exact coordinate magnitudes along the four-real-dimensional complex curve L154.7 against its actual imaginary norm. The right panel uses the exact derivatives L154.10 with \(a_0=1\), taking their \(j\)-th roots and dividing by \(j\) or \(j^2\). Complete curve coordinates, phases, factorial constants and measures are retained in the argument and geometry JSON. The all-order growth and sharpness follow from EB15–EB16 and Solution 10.

## Exercises with complete solutions

**Exercise 1.** At the real double zero of \(P(z)=z^2\), compute \(A,B,r_P\), and explain which denominator prevents a singularity.

**Solution 1.** At zero, \(P=P'=0\), while \(P''=2\). Thus \(A=B=2\) and \(r_P=1\). Away from zero the squares are \(\xi^4+4\xi^2+4\) and \(4\xi^2+4\), giving L154.3. The positive-order strength includes the top derivative; using only the first derivative would give the indeterminate quotient \(0/0\). The formal proof keeps every ordinary derivative up to the degree.

**Exercise 2.** For \(P=z_1\), can \(k/k_1=(1+\xi_2^2)^s\), \(s>0\), satisfy the characteristic condition?

**Solution 2.** At the zero \(z=(0,T)\), \(T\in\mathbb R\), the imaginary norm is zero and the ratio is \((1+T^2)^s\). This is unbounded, whereas the right side of the characteristic condition is one fixed constant. It fails. Equivalently at these real frequencies \(r_P=1\), so no power of \(r_P\) pays for the increasing second-coordinate weight. This detects the unconstrained direction.

**Exercise 3.** Extract the mixed coefficient of \(T_2(\omega)=\omega_1^2+3\omega_1\omega_2+2\omega_2^2\) from the complex unit torus.

**Solution 3.** Put \(\omega_j=2^{-1/2}e^{i\theta_j}\). Its terms are
\(\frac12e^{2i\theta_1}\), \(\frac32e^{i(\theta_1+\theta_2)}\), and \(e^{2i\theta_2}\).
Multiply by \(e^{-i(\theta_1+\theta_2)}\) and average over both angles; only the middle term remains, yielding \(3/2\). For the corresponding Taylor polynomial, recovery of \(\partial_1\partial_2P\) multiplies this by \(\alpha!n^{|\alpha|/2}=1\cdot2\), giving the correct derivative \(3\). This is the coefficient extraction in EB5, rather than an assertion that a real-direction estimate alone recovers all complex coefficients.

**Exercise 4.** Track the exponent changes in the weight-condition equivalence.

**Solution 4.** A real strength bound \(a(\xi)\le Cr_P^N\) and the upper half of EB2 give \(a(\xi)\le C'(1+d)^ {mN}\). At a complex zero, \(d(\operatorname{Re}z)\le|\operatorname{Im}z|\), so the characteristic exponent can be \(mN\). Conversely a characteristic exponent \(N'\), together with a shift exponent \(M_a\) for \(a=k/k_1\), gives EB8 with distance power \(M_a+N'\). The lower half of EB2 bounds this by \(C''r_P^{M_a+N'}\). The conditions ask for some finite powers; they do not require those two powers to be equal.

**Exercise 5.** Explain the zero direction and constant-polynomial endpoints in the derivative estimate.

**Solution 5.** If \(\gamma=0\), every positive iterate of \(\gamma\cdot D\) is zero, independently of \(\rho\). If \(P=c\ne0\), the homogeneous equation says \(cu=0\), so the solution itself is zero. These conclusions do not use a distance to an empty zero set. The strength-ratio comparison is explicitly restricted to nonconstant \(P\), for which its denominator is positive.

**Exercise 6.** Verify the reflected physical weight for the test choice in EB12, and why the smooth solution belongs to it.

**Solution 6.** For \(\kappa(\xi)=\langle\xi\rangle^{-(n+1)}\), reflection leaves it unchanged because it is even, so \(1/\check\kappa=\langle\xi\rangle^{n+1}\). A compact smooth cutoff of the smooth solution has a Fourier transform decreasing faster than every real-frequency power, by real integration by parts. Its squared product with \(\langle\xi\rangle^{n+1}\) is integrable, giving the required local physical membership. The tube theorem is therefore applied legitimately. Evenness of this particular weight does not remove the reflection from the general theorem.

**Exercise 7.** Check the exponential support gap in EB14 for \(K'=[-r,r]\), \(L=[-r-\delta,r+\delta]\).

**Solution 7.** \(H_L(-\eta)=(r+\delta)|\eta|\), and for \(|x|\le r\),
\[
-2H_L(-\eta)-2x\eta
\le-2(r+\delta)|\eta|+2r|\eta|
=-2\delta|\eta|.
\tag{L154.11}
\]
The transformed density is weighted by \(\Phi(-z)\), and the physical exponential has modulus \(e^{-x\eta}\). Both signs combine to give this decay uniformly throughout the smaller compact. It is what keeps every imaginary moment finite.

**Exercise 8.** Locate the maximum of \((1+r)^q e^{-\delta r}\), \(r\ge0\), and recover the order \(j^{\rho j}\).

**Solution 8.** Its logarithmic derivative is \(q/(1+r)-\delta\). If \(q\le\delta\), the maximum is one at zero. If \(q>\delta\), its value at \(r=q/\delta-1\) is
\[
\sup_{r\ge0}(1+r)^q e^{-\delta r}
= (q/\delta)^q e^{-q+\delta}.
\tag{L154.12}
\]
Take \(q=2\rho j\), and leave one factor \(e^{-\delta r}\) for integration. The square root of the resulting bound costs a fixed exponential in \(j\), times \(j^{\rho j}\). The remaining integral in dimension \(n\) is independent of \(j\). This proves the bound without an integer restriction on \(\rho\).

**Exercise 9.** Compute the signs in the actual heat-mode derivatives L154.10.

**Solution 9.** In the spatial coordinate, applying \(D_1=-i\partial_{x_1}\) multiplies the kernel by \(-i(i-1)s=(1+i)s\). In the time coordinate it multiplies by \((-i)(-2i)s^2=-2s^2\). Iteration gives \((1+i)^js^j\) and \((-2)^js^{2j}\). The real positive exponential moment at the origin yields the exact factorials. In particular the time derivative with respect to \(\partial_{x_2}\) has factor \((-2i)^j\), while the \(D_2\)-derivative has factor \((-2)^j\).

**Exercise 10.** Prove that the two attained growth powers in Example 4 cannot be reduced.

**Solution 10.** For integer \(N\ge1\), each factor in \(N!\) is at most \(N\), giving \(N!\le N^N\). Since \(\log x\) is increasing,
\[
\log(N!)=\sum_{k=2}^N\log k
\ge\int_1^N\log x\,dx=N\log N-N+1,
\quad N!\ge e(N/e)^N .
\tag{L154.13}
\]
Use \(N=j\) in the spatial expression and \(N=2j\) in the time expression in L154.10. They lie between positive fixed-exponential multiples of \(j^j\) and \(j^{2j}\), respectively. If a smaller power \(\rho'<1\) bounded all spatial orders, taking \(j\)-th roots would force \(j^{1-\rho'}\) bounded. For time, any \(\rho'<2\) would force \(j^{2-\rho'}\) bounded. Both are impossible. The origin is an interior point of the solution domain, so these are actual failures of a putative smaller local derivative exponent.

The calculations check the actual jet strengths and root distances, complex torus coefficients, heat characteristic coordinates, all relevant operator signs and independently integrated moments. The two arbitrary-distribution representation exercises, chapter notes and other assigned course targets remain active.
