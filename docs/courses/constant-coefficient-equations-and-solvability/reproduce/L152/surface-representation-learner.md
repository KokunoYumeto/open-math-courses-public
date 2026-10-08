# Learning the surface representation theorem

The theorem replaces a neighborhood of the characteristic set by the set itself. A repeated factor contributes derivatives of the test transform and therefore polynomial amplitudes in the solution. The formal proof keeps three separate quantities: actual Euclidean surface area, all normal multiplicity jets, and a polynomial loss in the surface density norm.

Read [SR1–SR8, the complete proof](../../AN02-L152.html#complete-proof). In its convention the forward test transform is \(F_v(z)=v(e^{-ix\cdot z})\), so the solution integral uses \(F_v(-z)\). The physical dual of a test weight \(k\) is \(B_{2,1/\check k}^{\mathrm{loc}}\), with \(\check k(\xi)=k(-\xi)\).

## Worked example 1. Two parallel complex planes and multiplicity

In \(\mathbb C^2\), let \(A(t,y)=t(t-h)\), \(h>0\). The zero set is the disjoint union of the complex planes \(t=0\) and \(t=h\). In a ball of radius \(r\) centered at zero, the first plane cuts out a complex disk of area \(\pi r^2\); the second cuts out a disk of squared radius \(r^2-h^2\) when \(r>h\). Consequently
\[
S_A(r)=\pi r^2+\pi(r^2-h^2)_+,\qquad
\frac{S_A(r)}{\pi r^2}
=1+(1-h^2/r^2)_+\le2.
\tag{L152.1}
\]
This is the degree-two area bound with its exact coefficient. For \(r<h\) the normalized area is one; after the second plane enters it increases to two.

Now take \(B=t^2(t-h)^3\). The geometric zero set and its unweighted area are unchanged. The logarithmic Laplacian counts local multiplicity, however:
\[
\frac{\Delta\log|B|(B(0,r))}{2\pi^2r^2}
=2+3(1-h^2/r^2)_+\le5=\deg B .
\tag{L152.2}
\]
The first plane has multiplicity two and the second three. The actual source convention integrates geometric area on regular-power charts; it does not replace that area by the multiplicity-counted current.

For the single plane \(t=0\), direct normal-kernel integration in the four-real-dimensional ball gives
\[
\int_{B(0,r)}
 \Delta\!\left(\tfrac12\log(|t|^2+\delta^2)\right)dV
=2\pi^2\left[r^2-\delta^2
                     \log(1+r^2/\delta^2)\right].
\tag{L152.3}
\]
Indeed the slice at \(|t|=\rho\) has \(y\)-area \(\pi(r^2-\rho^2)\). Multiply it by the kernel \(2\delta^2/(\rho^2+\delta^2)^2\), integrate \(2\pi\rho\,d\rho\), and substitute \(s=\rho^2\). The integral becomes
\(2\pi^2\delta^2\int_0^{r^2}(r^2-s)/(s+\delta^2)^2\,ds\), which evaluates to L152.3. As \(\delta\to0\), it tends to \(2\pi\) times the plane area. This checks the normalizations in SR10–SR13.

![Sharp area, multiplicity and the actual normal regularization](figures/algebraic-area-and-normal-mass.png)

**Figure SR-A.** The left panel gives the exact degree-two geometric area ratio and the degree-five multiplicity-counted logarithmic mass for these two planes. The right panel shows the exact normalized mass L152.3 against \(r/\delta\). Both axes describe complete Euclidean-ball quantities in four real dimensions, rather than the area of a drawn real slice.

## Worked example 2. Anisotropic scaling at a collision

Let \(Q(t,y)=t^2-y\), \(m=2\), and center at \(\theta=(a,b)\in\mathbb C^2\). Set
\(\sigma=(1+\sqrt{|a|^2+|b|^2})^{-1}\). The transformed polynomial is
\[
Q_\theta(w_1,w_2)=
(a^2-b)+2aw_1+w_1^2-\sigma w_2,\qquad
\widetilde Q_\theta(0)^2
=|a^2-b|^2+4|a|^2+4+\sigma^2.
\tag{L152.4}
\]
The mixed-variable derivative has size \(\sigma\le1\), even when the center is large. The coefficient of \(w_1^2\) stays one. Thus Cauchy's estimate bounds the pure derivatives by the disk supremum, and that supremum is at least one. These are the two ingredients in the uniform local-division hypothesis.

The reduced discriminant is \(R(y)=4y\). In the scaled coordinates,
\[
R_\theta(w_2)=4(b+\sigma w_2),\qquad
\widetilde R_\theta(0)=4\sqrt{|b|^2+\sigma^2}\ge4\sigma.
\tag{L152.5}
\]
At \(b=0\) its point value vanishes, while its derivative strength is \(4\sigma>0\). A release criterion or proof using only \(|R_\theta(0)|\) would miss precisely this collision.

The covering ellipsoid has equation
\[
|t-a|^2+(1+|\theta|)^2|y-b|^2<r^2.
\tag{L152.6}
\]
Its ordinary volume is \((\pi^2/2)r^4\sigma^2\), not the volume of an ordinary radius-\(r\) ball. The cover in SR4 controls overlap by comparing these shrinking volumes locally, rather than assuming a fixed minimum volume over all of space.

For this \(m=2,n=2\), the explicit formal exponent is \(E=30\) and \(K=36\). The actual discriminant degree here is one; SR6 deliberately uses a uniform degree bound and is not claiming the best loss for this example.

## Worked example 3. A repeated characteristic point and a complex direction

In one physical dimension take \(P(\zeta)=(\zeta-\lambda)^3\), where \(\lambda=1+\frac i2\). The surface is the single point \(\{\lambda\}\), with counting measure. Let
\[
u(x)=(A+Bx+Cx^2)e^{i\lambda x},\qquad
\tau=1+i,\quad A=1,\ B=2-i,\ C=-\tfrac i2 .
\tag{L152.7}
\]
Since
\((D-\lambda)[p(x)e^{i\lambda x}]=-ip'(x)e^{i\lambda x}\),
three applications kill every quadratic \(p\).
The surface representation is exact with
\[
U^0(\lambda)=A,\qquad
U^1(\lambda)=B/\tau,\qquad
U^2(\lambda)=C/\tau^2,
\quad
u(x)=\sum_{a=0}^2(x\tau)^a U^a(\lambda)e^{i\lambda x}.
\tag{L152.8}
\]
All weighted density norms are finite because there are only three values at one point.

The forward transform signs can be checked without symmetry assumptions:
\[
F_v^{(a)}(-\lambda)
=v((-ix)^ae^{i\lambda x}),\qquad
u(v)=A F_v(-\lambda)+iB F_v'(-\lambda)-C F_v''(-\lambda).
\tag{L152.9}
\]
For \(k(\xi)=\sqrt{1+(\xi-1)^2}\), the shift inequality follows from the norm triangle inequality: \(k(\xi+h)\le k(\xi)+|h|\le(1+|h|)k(\xi)\). Its reflected reciprocal is
\(1/\check k(\xi)=1/\sqrt{1+(\xi+1)^2}\), which differs from \(1/k\). The reflection in the theorem cannot be removed merely because the counting-measure example is finite.

## Worked example 4. A continuous surface density for a repeated curved factor

In two physical dimensions let
\[
P(\zeta)=(\zeta_2-\zeta_1^2)^2,\qquad
N=\{(y,y^2):y\in\mathbb C\},\qquad \tau=(1,0).
\tag{L152.10}
\]
The highest-degree part is \(\zeta_1^4\), so this direction is noncharacteristic. The irreducible factor has multiplicity two. The graph's full real area density is \(J(y)=1+4|y|^2\), since its complex derivative is \(2y\). For \(\beta=\frac12+\frac i4\), \(s>0\), and any complex \(\alpha\), define
\[
U^0(y,y^2)=\frac{\mathbf1_{\{|y-\beta|<s\}}}{\pi s^2J(y)},
\qquad
U^1(y,y^2)=\alpha U^0(y,y^2).
\tag{L152.11}
\]
Testing or evaluating these compact surface integrals gives
\[
\int_NU^0(\zeta)e^{ix\cdot\zeta}\,dS(\zeta)
=\frac1{\pi s^2}\int_{|y-\beta|<s}
                   e^{i(x_1y+x_2y^2)}\,dA(y)
=e^{i(x_1\beta+x_2\beta^2)} .
\tag{L152.12}
\]
The last equality is the complex disk mean identity: expand the entire integrand about \(\beta\); every positive power of \(y-\beta\) has angular integral zero, and the constant integrates to \(\pi s^2\). Uniform convergence on the compact disk justifies termwise integration.
Thus the two densities give
\[
u(x)=(1+\alpha x_1)e^{i(x_1\beta+x_2\beta^2)} .
\tag{L152.13}
\]
For the single factor \(L(D)=D_2-D_1^2\),
\(L(D)[x_1e^{ix\cdot(\beta,\beta^2)}]=2i\beta e^{ix\cdot(\beta,\beta^2)}\).
This is nonzero when \(\beta\ne0\), whereas \(L(D)^2\) kills it. The degree-one amplitude therefore displays the actual repeated-factor phenomenon. Each individual surface kernel in the integral has the same annihilation property.

These densities have finite SR4 norm for any continuous finite \(\phi\), since their support is compact and \(J\ge1\). The surface measure cannot be omitted from their definition: division by \(J\) compensates precisely for its full metric area.

The area of this graph inside an ordinary radius-\(r\) ball about zero is also explicit. Set \(b(r)=(\sqrt{1+4r^2}-1)/2\), so \(|y|^2<b(r)\). Polar integration gives
\[
S_N(r)=\pi[b(r)+2b(r)^2]
       =\pi[2r^2-b(r)],\qquad
\frac{S_N(r)}{\pi r^2}=2-\frac{b(r)}{r^2}\le2 .
\tag{L152.14}
\]
The parameter-disk projection has area \(\pi b(r)\); the actual surface has the extra derivative term \(2\pi b(r)^2\). The normalized area tends to one at small scales and to its degree bound two at large scales.

![Actual graph-area bounds and anisotropic local geometry](figures/curved-area-and-anisotropic-cover.png)

**Figure SR-B.** The left panel compares the exact full graph area in L152.14 with its parameter-plane projection. The right panel draws explicitly labeled real-coordinate sections \(t-a\in\mathbb R,\ y-b\in\mathbb R\) of the exact complex ellipsoids L152.6 for \(m=2\); their shrinking transverse axes are prescribed by \(\sigma_\theta\). The plane section is not an ambient realization of the four-dimensional metric.

## Exercises with complete solutions

**Exercise 1.** Compute the area of the complex affine plane \(t=\gamma y\) inside \(B(0,r)\subset\mathbb C^2\). Does its slope change the degree-one bound?

**Solution 1.** The parameter region is \((1+|\gamma|^2)|y|^2<r^2\), and the real graph area density is \(1+|\gamma|^2\). The integral is
\((1+|\gamma|^2)\pi r^2/(1+|\gamma|^2)=\pi r^2\).
Thus it attains the degree-one bound at every slope. Using only the projected disk would give the smaller and incorrect full area \(\pi r^2/(1+|\gamma|^2)\).

**Exercise 2.** Differentiate the area ratios in Examples 1 and 4 and prove their monotonicity, including the transition \(r=h\).

**Solution 2.** The first ratio is constant one for \(r\le h\); for \(r>h\) its derivative is \(2h^2/r^3>0\), and both formulas agree at \(h\). For the curved graph use \(r^2=b+b^2\), so its ratio is
\((1+2b)/(1+b)=2-1/(1+b)\). Since \(b'(r)=2r/\sqrt{1+4r^2}>0\), its derivative is \(b'(r)/(1+b)^2>0\). Its limits are one and two.

**Exercise 3.** Why can the area proof pass to the open-ball mass without proving zero boundary mass?

**Solution 3.** For every smooth compact \(0\le\psi\le1\) inside that ball, the regularized mass bounds \(\int\psi\,\Delta q_\epsilon\). Distributional convergence passes the same bound to \(\int\psi\,d\mu\). Positive-measure inner regularity, equivalently an increasing sequence of such cutoffs exhausting the ball, identifies their supremum with \(\mu(B)\). No indicator is tested directly against a weak limit, so boundary atoms cause no gap.

**Exercise 4.** Verify the derivative strength in Example 2 and the discriminant lower bound at \(b=0\).

**Solution 4.** The only nonzero derivatives of \(Q_\theta\) at zero are its value \(a^2-b\), first derivatives \(2a,-\sigma\), and second derivative \(\partial_{w_1}^2Q_\theta=2\). Their squared absolute values sum to L152.4. The transformed discriminant has value \(4b\) and derivative \(4\sigma\); its strength is L152.5. At \(b=0\), strength \(4\sigma\) remains positive for every finite center, even though the point value is zero.

**Exercise 5.** Derive SR6 when \(m=2,n=2\), and identify each additional power of \(W\) after the local-remainder estimate.

**Solution 5.** The three terms in \(E\) are \(16,12,2\), hence \(E=30\). Squared cutoff derivatives give \(W^{m-1}=W\), polynomial strength gives \(W^m=W^2\), and inverse curvature is bounded by \(W\). This is \(W^4=W^{2m}\). Comparing the weight at an integration point with the surface-data point gives \(W^2\), so \(K=30+4+2=36\). The constants and this loose power are uniform; this does not establish an optimal derivative loss.

**Exercise 6.** Give the safe-circle division estimate when \(q(t)=t^m\) and the evaluation point is \(t=0\). Why is evaluation of \(1/q(0)\) unnecessary?

**Solution 6.** If \(b=qg\) with \(g\) holomorphic on a disk of radius \(c/4\), choose any circle with radius \(r\in(c/8,c/4)\). On it \(|q|=r^m\), and Cauchy's formula gives
\(|g(0)|\le r^{-m}\sup_{|t|=r}|b(t)|\).
The center may be a multiple zero. Holomorphic divisibility is already known from the two local decompositions; the integral uses only nonzero boundary values of \(q\).

**Exercise 7.** Check the signs in the global correction SR30–SR36.

**Solution 7.** From \(F=H+\mathcal QG\) and \(\bar\partial F=0\) we get
\(\bar\partial H=-\mathcal Q\bar\partial G\).
Set \(f=-\bar\partial G\). Expanding
\(\sum_{\mu,\nu}\chi_\mu(g_\mu-g_\nu)\bar\partial\chi_\nu\)
leaves \(-\sum_\nu g_\nu\bar\partial\chi_\nu\), because \(\sum\bar\partial\chi_\nu=0\) and \(\sum\chi_\mu=1\). This is \(f\). If \(\bar\partial w=f\), then
\(\bar\partial(H-\mathcal Qw)=\mathcal Qf-\mathcal Qf=0\) and
\(\bar\partial(G+w)=-f+f=0\). The displayed signs are therefore required.

**Exercise 8.** Explain why \(P(D)u=0\) can annihilate the repaired divisible part even though its inverse quotient is initially a compact distribution.

**Solution 8.** First prove the repaired transform has exponential type of \(K_{j+1}\), and hence a compact inverse \(v_{2,j}\in B_{2,k}\). Full entire division gives a compact inverse \(a_j\) of the quotient. Smooth \(a_j\) by a normalized compact mollifier. Then \(P(-D)(a_j*\rho_\epsilon)\) is an ordinary compact smooth test, so its action under \(u\) is zero. It equals a constant multiple of \(v_{2,j}*\rho_\epsilon\). Their weighted Fourier transforms converge by dominated convergence with the bounded multipliers \(\widehat\rho(\epsilon\xi)\to1\), and their supports lie in one fixed compact stage. Continuity of the canonical pairing passes zero to the repaired part. One never pairs two arbitrary distributions directly.

**Exercise 9.** Recover the density normalization in Example 3 for an arbitrary nonzero complex \(\tau\).

**Solution 9.** The algebraic identity
\((x\tau)^a(c_a/\tau^a)=c_ax^a\)
gives the surface densities. To check against the unit direction in the proof, \(e=\tau/|\tau|\) and
\(\partial_e^aF_v(-\lambda)=e^a(-i)^a v(x^ae^{i\lambda x})\).
The intermediate coefficient is \(B^a=i^ae^{-a}c_a\), where \(e^{-a}\) is the reciprocal power of the unit complex number \(e\). The final coefficient is
\((-i)^a|\tau|^{-a}B^a=c_a/\tau^a\).
Thus neither the phase of the complex direction nor the forward-transform sign is dropped.

**Exercise 10.** Compute the unweighted squared surface-density norm of Example 4 at \(\beta=0\), and explain why the theorem does not promise absolute pointwise convergence for all of its densities.

**Solution 10.** With \(J=1+4|y|^2\) and \(dS=JdA\),
\[
\int_N|U^0|^2dS
=\frac1{\pi^2s^4}\int_{|y|<s}\frac{dA(y)}{1+4|y|^2}
=\frac{\log(1+4s^2)}{4\pi s^4}.
\tag{L152.15}
\]
The radial integral is
\(2\pi\int_0^s r/(1+4r^2)\,dr=\frac\pi4\log(1+4s^2)\).
The two-density norm is multiplied by \(1+|\alpha|^2\).
These particular compact densities give pointwise integrals. In the full theorem only the weighted squared density and the weighted jet norm of each compact smooth test are controlled. Their Cauchy–Schwarz estimate proves absolute convergence of the tested integral. A fixed pointwise exponential need not have finite complementary surface norm on the entire unbounded variety, so that estimate cannot be applied to it without further evidence.

The computational checks independently integrate the normal kernel and graph areas, compute transformed coefficients and discriminants, integrate actual curved-surface kernels, verify repeated-operator identities and check the complex-direction/Fourier factors. They supplement the complete proof and do not stand in for it.
