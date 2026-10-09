# Complex quadratic powers and the Cauchy kernel

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A complex quadratic form with positive real part has a singular power that can be integrated against Schwartz tests. Its Fourier transform depends on a square root chosen continuously from the matrix, not merely from the final value of its determinant. We establish that choice, both absolute Gaussian interchanges and the full parameter domain. The planar Cauchy kernel then follows from a whole logarithmic transform, including frequency zero.

Our convention is \(F\phi(\xi)=\int e^{-ix\cdot\xi}\phi(x)\,dx\), extended by the complex bilinear transpose. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz map, inversion, Gaussian constant and coordinate rules. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2, Lemma 2.1 and the transform proof of Theorem 3.1, supplies the full matrix branch and complex Gaussian theorem. [Radial powers and the logarithmic endpoint](radial-powers-and-the-logarithmic-endpoint.md), Theorems 1.1 and 3.1 and Lemma 3.3, supplies the radial coefficient and entire weak logarithmic gradient. The distributional linear substitution in [Planar rotations and angular spectra](planar-rotations-and-angular-spectra.md), Theorem 1.1's proof, will be used for reflection.

For holomorphic parameters we use [Complex powers at a boundary](complex-powers-at-a-boundary.md), Lemmas H0–H1, and the complete polydisk proof (C1)–(C2) in [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3. The [Gamma foundation](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e, proves all scalar integral, logarithmic-moment and nonvanishing facts. The supplied [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Sections 10.1–10.6, [scalar calculus](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2, and [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5, supply the remaining matrix, convergence, substitution and polar arguments.

## Gaussian superposition fixes the complex quadratic power

Let \(\mathcal H_n=\{B=B^T:\operatorname{Re}B>0\}\). For a complex symmetric matrix the entrywise real part is also its Hermitian part. Thus its positivity on real vectors implies positivity on complex vectors: if \(v=s+it\), then \(v^*(\operatorname{Re}B)v=s^T(\operatorname{Re}B)s+t^T(\operatorname{Re}B)t\). In particular \(B\) is invertible, since \(Bv=0\) would contradict this inequality.

Use the canonical holomorphic branch \(g(B)^2=\det B\), positive on real positive matrices, from U020, Lemma 2.1. Its proof constructs
\[
 g(B)=\exp\left(\frac12\int_0^1
 \operatorname{tr}\bigl[((1-s)I+sB)^{-1}(B-I)\bigr]\,ds\right).
\]
Every matrix on this segment is accretive and invertible; the supplied proof verifies the determinant identity by differentiation. It also proves \(g(tB)=t^{n/2}g(B)\) for \(t>0\) and \(g(B^{-1})=g(B)^{-1}\). All scalar powers below use
\(\ell(z)=\log|z|+i\arg z\), \(-\pi/2<\arg z<\pi/2\), on the right half-plane. U017, H0, proves \(\ell'=1/z\) and \(e^\ell=z\).

**Lemma 1.1 (scalar complex Laplace integral).** For \(\operatorname{Re}p>0\), \(\operatorname{Re}z>0\),
\[
 \int_0^\infty t^{p-1}e^{-zt}\,dt
       =\Gamma(p)e^{-p\ell(z)}=\Gamma(p)z^{-p}.
 \tag{1.1}
\]
The integral is jointly holomorphic in these two parameters.

**Proof.** For positive real \(z\), substitution \(s=zt\) proves the formula from the Euler integral, with \(t^{p-1}=e^{(p-1)\log t}\). Fix \(p\). On a compact right-half-plane set of \(z\)'s, each \(z\)-derivative of the integrand is bounded by \(t^{\operatorname{Re}p+j-1}e^{-ct}\), \(c>0\). This is integrable at both ends. The difference quotient equals the integral of its derivative along the complex parameter segment, by real FTC; dominated convergence therefore proves complex differentiability. Both sides of (1.1) are holomorphic in \(z\) and agree on the positive axis. Expanding at a positive point shows that their difference has every Taylor coefficient zero; the one-variable identity principle used and proved in U017, H1, extends equality across the connected right half-plane.

For joint holomorphy, let \(0<\delta\le\operatorname{Re}p\le M\), \(\operatorname{Re}z\ge c>0\), on a compact parameter set. A mixed derivative adds \(t^j(\log t)^k\). Near zero a majorant is \(t^{\delta-1}|\log t|^k\); near infinity use \(t^{M+j-1}e^{-ct}(\log t)^k\), with harmless constants. Gamma G1 proves both integrable. The segment argument gives continuous mixed derivatives and joint continuity; the supplied polydisk proof converts coordinate holomorphy and joint continuity into convergent joint power series. This proves the last assertion. \(\square\)

**Theorem 1.2.** If \(B\in\mathcal H_n\) and \(0<\operatorname{Re}a<n\), then on all Schwartz tests
\[
 \begin{gathered}
 F[(x^TBx)^{-a/2}](\xi)
   =g(B)^{-1}C_{n,a}(\xi^TB^{-1}\xi)^{(a-n)/2},\\
 C_{n,a}=2^{n-a}\pi^{n/2}
                  \frac{\Gamma((n-a)/2)}{\Gamma(a/2)}.
 \end{gathered}
 \tag{1.2}
\]
Both functions have their whole locally integrable tempered extensions at zero. Their pairings are jointly holomorphic in \(a\) and all independent symmetric entries of \(B\), throughout the indicated domain.

**Proof: bounds and branches.** Write \(Q(x)=x^TBx\), \(K(\xi)=\xi^TB^{-1}\xi\), \(\alpha=\operatorname{Re}a\). Multiplication of matrices gives
\[
 \operatorname{Re}(B^{-1})
 =B^{-*}(\operatorname{Re}B)B^{-1}>0,
 \qquad B^{-*}=(B^{-1})^*.
 \tag{1.3}
\]
Indeed the right side is \((B^{-*}+B^{-1})/2\). Symmetry of the inverse identifies this with its entrywise real part. Compactness of the real unit sphere gives constants \(c,d>0\) such that
\(\operatorname{Re}Q(x)\ge c|x|^2\), \(\operatorname{Re}K(\xi)\ge d|\xi|^2\). Finite matrix-entry bounds give upper bounds \(C|x|^2,C'|\xi|^2\) for their absolute values. Both quadratics therefore take nonzero real vectors into the right half-plane.

Writing a complex power as its exponential shows
\[
 |Q(x)^{-a/2}|\le C_a|x|^{-\alpha},
 \qquad |K(\xi)^{(a-n)/2}|\le C_a'|\xi|^{\alpha-n}.
\]
The argument factors are bounded because \(|\arg Q|,|\arg K|<\pi/2\). Polar integration near zero gives the exponents \(n-1-\alpha>-1\) and \(\alpha-1>-1\), respectively. At infinity the seminorm \(p_N(\phi)=\sup_x(1+|x|^2)^{N/2}|\phi(x)|\), for a sufficiently large fixed \(N\), makes both integrals finite. This proves local integrability and continuity as tempered distributions.

**Proof: first absolute interchange.** Lemma 1.1 and the nonvanishing of Gamma give, for \(x\ne0\),
\[
 Q(x)^{-a/2}
   =\frac1{\Gamma(a/2)}
       \int_0^\infty t^{a/2-1}e^{-tQ(x)}\,dt.
 \tag{1.4}
\]
For any \(\phi\in\mathcal S\), positive Tonelli and a positive real scalar substitution give
\[
 \begin{aligned}
 &\int_0^\infty t^{\alpha/2-1}
           \int e^{-ct|x|^2}|F\phi(x)|\,dx\,dt\\
 &\quad=\Gamma(\alpha/2)c^{-\alpha/2}
                 \int |x|^{-\alpha}|F\phi(x)|\,dx<\infty.
 \end{aligned}
 \tag{1.5}
\]
The final bound follows because \(F\phi\in\mathcal S\) and \(\alpha<n\). We can consequently insert (1.4) in the full pairing \(Q^{-a/2}(F\phi)\) and interchange \(x,t\) by absolute complex Fubini.

**Proof: second interchange and coefficient.** U020's complete Gaussian theorem, applied to \(tB\), states
\[
 F(e^{-tQ})(\xi)
       =\pi^{n/2}t^{-n/2}g(B)^{-1}e^{-K(\xi)/(4t)}.
 \tag{1.6}
\]
For fixed \(t>0\), its ordinary transform equals its distributional transpose: the absolute double integral is bounded by \(\|e^{-tQ}\|_1\|\phi\|_1\). After this substitution, the next interchange has absolute bound
\[
 \begin{gathered}
 \pi^{n/2}|g(B)|^{-1}\int|\phi(\xi)|I_\alpha(\xi)\,d\xi,\\
 I_\alpha(\xi)=\int_0^\infty
       t^{(\alpha-n)/2-1}e^{-d|\xi|^2/(4t)}\,dt.
 \end{gathered}
 \tag{1.7}
\]
For \(\xi\ne0\), substituting \(s=d|\xi|^2/(4t)\) evaluates the latter as
\[
 I_\alpha(\xi)
 =2^{n-\alpha}d^{(\alpha-n)/2}
     \Gamma((n-\alpha)/2)|\xi|^{\alpha-n}.
\]
This is integrable against \(|\phi|\) by the already proved bounds. Its value at the single point zero is irrelevant to that integral. Tonelli establishes finiteness, then absolute Fubini allows the complex interchange.

For the actual complex integral use the real substitution \(u=1/(4t)\), without moving an integration contour. Lemma 1.1 gives
\[
 \begin{aligned}
 \int_0^\infty t^{(a-n)/2-1}e^{-K/(4t)}\,dt
 &=2^{n-a}\int_0^\infty u^{(n-a)/2-1}e^{-Ku}\,du\\
 &=2^{n-a}\Gamma((n-a)/2)K^{(a-n)/2}.
 \end{aligned}
 \tag{1.8}
\]
Combining these identities proves (1.2) with precisely the specified scalar branch and \(g(B)\). The calculation has paired against every Schwartz test; it determines the entire transform, including every possible term at zero.

**Proof: all parameter derivatives.** Work on a compact parameter neighborhood strictly inside the domain. Compactness of its product with the unit sphere makes \(c,d\) uniform. Inversion is holomorphic by the finite adjugate formula; all its derivatives are bounded on that compact set. For example,
\[
 D_E(B^{-1})=-B^{-1}EB^{-1}
\]
follows by differentiating \(BB^{-1}=I\). Repeated differentiation is a finite sum of products of these bounded matrices. Thus every matrix derivative of \(K\) is a quadratic form bounded by a constant times \(|\xi|^2\). A derivative of \(Q\) in an independent entry is \(x_j^2\) or \(2x_jx_k\); all its higher matrix derivatives vanish. The lower bounds for \(|Q|,|K|\) show that every ratio introduced by the chain rule has a uniform bound. The holomorphic nonzero \(g\) has bounded derivatives on smaller compact neighborhoods, by the supplied polydisk proof. The Gamma foundation gives the same assertion for every derivative of \(C_{n,a}\) within the strip.

Choose \(0<\alpha_-\le\operatorname{Re}a\le\alpha_+<n\) there. Since
\(\ell(Q(x))=2\log|x|+\ell(Q(x/|x|))\), with the second term uniformly bounded, each exponent derivative adds at most \(C(1+|\log|x||)\). The same statement holds for \(K\). By induction using the preceding matrix derivative formulas, a mixed derivative with \(m\) exponent derivatives and any fixed number of matrix derivatives has an absolute majorant proportional to
\[
 \begin{cases}
 |x|^{-\alpha_+}(1+|\log|x||^m),&0<|x|<1,\\
 |x|^{-\alpha_-}(1+\log^m|x|),&|x|\ge1
 \end{cases}
\]
on the physical side, and to
\[
 \begin{cases}
 |\xi|^{\alpha_- -n}(1+\bigl|\log|\xi|\bigr|^m),&0<|\xi|<1,\\
 |\xi|^{\alpha_+ -n}(1+\log^m|\xi|),&|\xi|\ge1
 \end{cases}
\]
on the frequency side, before multiplication by a test. Polar integration and Gamma G1 give integrability at zero; a fixed sufficiently large \(p_N\) bounds the tail. These are uniform bounds on bounded families of Schwartz tests.

For a difference quotient in any parameter coordinate, integrate that pointwise coordinate derivative along its segment, inside a slightly larger compact neighborhood. The displayed integrable bounds permit dominated convergence and prove the derivative under the pairing. They also prove joint continuity. Iteration gives every continuous mixed derivative. Finally U015's polydisk proof applies to each jointly continuous, coordinate-holomorphic pairing, and gives convergent joint power series and their derivatives. This establishes the stated holomorphy without a separate-holomorphy theorem left unproved. \(\square\)

**An explicit coupled quadratic.** In dimension three set
\[
 B=\begin{pmatrix}1&i&0\\i&1&0\\0&0&1\end{pmatrix},
 \qquad
 B^{-1}=\frac12\begin{pmatrix}1&-i&0\\-i&1&0\\0&0&2\end{pmatrix}.
\]
Along the path replacing \(i\) by \(is\), \(0\le s\le1\), the real part is \(I\) and the determinant is \(1+s^2\). The continuous root starting at one is \(\sqrt{1+s^2}\), so \(g(B)=\sqrt2\). Gamma recurrence and \(\Gamma(1/2)=\sqrt\pi\) give \(C_{3,2}=2\pi^2\). Since a positive scalar factor preserves the chosen logarithm,
\[
 \begin{gathered}
 Q(x)=|x|^2+2ix_1x_2,\qquad
 P(\xi)=\xi_1^2+\xi_2^2+2\xi_3^2-2i\xi_1\xi_2,\\
 F(Q^{-1})(\xi)=2\pi^2P(\xi)^{-1/2}.
 \end{gathered}
 \tag{1.9}
\]
Here \(K=P/2\), and its factor \(\sqrt2\) cancels \(g(B)\). The real part of \(P\) is positive away from zero; its square root is the right-half-plane root.

## A logarithmic gradient determines the Cauchy kernel

**Theorem 2.1.** The regular tempered distribution \(k(x,y)=1/(x+iy)\) has the whole regular transform
\[
 Fk(\xi,\eta)=\frac{2\pi}{i\xi-\eta}.
 \tag{2.1}
\]
Both singular functions are interpreted by local integrability through zero.

**Proof.** Write \(r=(x^2+y^2)^{1/2}\). Almost everywhere \(k=(x-iy)/r^2\), and \(|k|=1/r\). The integral of \(|k|\) on a radius-\(R\) disk is \(2\pi R\); a fixed Schwartz weight controls its tail. U051, Theorem 3.1, for the two degree-one monomials in dimension two, gives the exact distributional identity
\[
 Fk=-2\pi i(\partial_\xi-i\partial_\eta)\log|(\xi,\eta)|.
 \tag{2.2}
\]
U051, Lemma 3.3, proves the full weak gradient
\(\partial_\xi\log\rho=\xi/\rho^2\), \(\partial_\eta\log\rho=\eta/\rho^2\). Its punctured integration-by-parts boundary term is bounded by \(C\varepsilon|\log\varepsilon|\sup|\phi|\), which tends to zero; both gradients are locally integrable, and the whole equality extends to Schwartz tests by the supplied density theorem. Therefore
\[
 Fk=\frac{-2\pi i\xi-2\pi\eta}{\xi^2+\eta^2}
       =\frac{2\pi}{i\xi-\eta}.
\]
The displayed frequency density has modulus \(2\pi/\rho\), so is also locally integrable and tempered. Equality of the regular functions almost everywhere identifies their whole regular distributions. The original monomial identity and weak gradient fix the transform at zero as well. \(\square\)

For the shifted examples we will use
\[
 F[u(\cdot-h)]=e^{-ih\cdot\xi}Fu,\qquad
 F[e^{ic\cdot x}u]=(Fu)(\xi-c).
\]
These follow on tests from
\(F\phi(x+h)=F[e^{-ih\cdot(\cdot)}\phi](x)\) and
\(e^{ic\cdot x}F\phi(x)=F[\phi(\cdot+c)](x)\), followed by the definition of translation of a distribution. Product and chain rules show that the test maps are continuous in all Schwartz seminorms, so the identities hold for every tempered distribution.

## Exercises

**Exercise 1 (foundation).** In the plane let \(Q(x,y)=2x^2+y^2+2ixy\). Compute the whole transform of \(Q^{-1/2}\). Check the positive real part of the inverse matrix and specify the frequency root.

**Exercise 2 (foundation).** In three dimensions transform \(((1+i)|x|^2)^{-1}\). Separate the determinant and dual-power factors before simplifying.

**Exercise 3 (advanced).** For \(B_\theta=e^{i\theta}I_4\), \(-\pi/2<\theta<\pi/2\), find \(g(B_\theta)\) and the transform of \((x^TB_\theta x)^{-1}\). At \(\theta=3\pi/8\), compare \(g\) with the principal scalar square root of \(\det B_\theta\) and determine the resulting sign error.

**Exercise 4 (advanced).** On \(\mathbb R^3\), put \(Q_s(x)=|x|^2+2isx_1x_2\), \(s\in\mathbb R\). Transform \(Q_s^{-1}\) for all \(s\), differentiate at zero and deduce the transform of \(x_1x_2/|x|^4\). Justify differentiation at the physical origin.

**Exercise 5 (intermediate).** Let \(Q(x)=|x|^2+2ix_1x_2\), \(h=(1,-2,0)\), \(b=(2,0,-1)\). Find the whole transform of
\[
 v(x)=e^{-ib\cdot x}[Q(3(x-h))]^{-1},
\]
including its phase, scale factor and shifted root.

**Exercise 6 (intermediate).** With \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\), prove that \(E=1/(\pi(x+iy))\) satisfies \(\partial_{\bar z}E=\delta_0\). Explain why almost-everywhere cancellation in frequency suffices.

**Exercise 7 (intermediate).** Derive the conjugate Cauchy transform by real reflection, then transform
\[
 w(x,y)=\frac{e^{i(3x-2y)}}{(x-1)-i(y+2)}
\]
with its exact translation and modulation phases.

**Exercise 8 (advanced).** For \(b>0\), evaluate \(Fk(\phi_b)\), where
\(\phi_b(\xi,\eta)=\xi e^{-b(\xi^2+\eta^2)}\), independently from the physical pairing and from the frequency density. Include all Gaussian and angular constants.

## Solutions

**Solution 1.** Here
\[
 B=\begin{pmatrix}2&i\\i&1\end{pmatrix},\qquad
 B^{-1}=\frac13\begin{pmatrix}1&-i\\-i&2\end{pmatrix}.
\]
Their real parts are \(\operatorname{diag}(2,1)\) and \(\operatorname{diag}(1,2)/3\), both positive. On the path replacing \(i\) by \(is\), \(0\le s\le1\), the determinant is \(2+s^2>0\). The root starts at \(\sqrt2\) and remains positive, hence \(g(B)=\sqrt3\). Since \(C_{2,1}=2\pi\), (1.2) gives
\[
 F(Q^{-1/2})(\xi,\eta)
       =\frac{2\pi}{(\xi^2+2\eta^2-2i\xi\eta)^{1/2}}.
\]
The factor \(1/3\) in the inverse form contributes \(\sqrt3\), cancelling \(g(B)\). The frequency quadratic lies in the right half-plane off zero; its root is the holomorphic root positive on positive reals. The theorem proves the entire locally integrable transform.

**Solution 2.** Let \(z=1+i\). On the connected right half-plane,
\(g(zI_3)=e^{3\ell(z)/2}\): this holomorphic expression squares to \(z^3\) and agrees with the positive branch on positive \(z\). Also \(\ell(1/z)=-\ell(z)\), by the explicit modulus and argument. Therefore, with \(\rho=|\xi|>0\),
\[
 g(zI_3)^{-1}=z^{-3/2},\qquad
 (|\xi|^2/z)^{-1/2}=z^{1/2}/\rho.
\]
The transform is
\[
 2\pi^2 z^{-3/2}\frac{z^{1/2}}{\rho}
       =\frac{2\pi^2}{z\rho}=\frac{\pi^2(1-i)}{\rho}.
\]
As a separate check, \((z|x|^2)^{-1}=z^{-1}|x|^{-2}\); U051's real radial identity gives the same whole result.

**Solution 3.** The scalar right-half-plane argument is \(\theta\), so the product branch gives
\[
 g(B_\theta)=e^{2i\theta},\qquad K_\theta=e^{-i\theta}|\xi|^2.
\]
Gamma recurrence gives \(C_{4,2}=4\pi^2\). Consequently
\[
 F[(x^TB_\theta x)^{-1}]
   =4\pi^2e^{-2i\theta}(e^{-i\theta}|\xi|^2)^{-1}
   =4\pi^2e^{-i\theta}|\xi|^{-2}.
\]
At \(3\pi/8\), the determinant is \(-i\). Its principal scalar root is \(e^{-i\pi/4}\), whereas \(g=e^{3i\pi/4}=-e^{-i\pi/4}\). The wrong root changes the entire answer's sign. Pulling \(e^{-i\theta}\) out of the physical function and using the real radial transform confirms the correct sign.

**Solution 4.** For every real \(s\), \(\operatorname{Re}B_s=I\), the nontrivial block has determinant \(1+s^2\) and inverse
\[
 \frac1{1+s^2}\begin{pmatrix}1&-is\\-is&1\end{pmatrix}.
\]
The inverse real part is positive. Along the whole real \(s\)-axis, the continuous determinant branch with value one at zero is \(\sqrt{1+s^2}\). Put
\[
 P_s(\xi)=\xi_1^2+\xi_2^2-2is\xi_1\xi_2
                         +(1+s^2)\xi_3^2.
\]
Then \(K_s=P_s/(1+s^2)\), and (1.2) gives \(F(Q_s^{-1})=2\pi^2P_s^{-1/2}\).

For real \(s\), \(|Q_s|\ge|x|^2\), so
\[
 \left|\partial_sQ_s^{-1}\right|
       =\left|\frac{-2ix_1x_2}{Q_s^2}\right|
       \le |x|^{-2}.
\]
This is integrable at zero in three dimensions and against a Schwartz test at infinity. Real FTC bounds the difference quotient by the same function, so dominated convergence justifies differentiation in the full physical pairing. The frequency derivative is likewise justified by Theorem 1.2. At zero,
\[
 F\left[-\frac{2ix_1x_2}{|x|^4}\right]
       =\frac{2\pi^2i\xi_1\xi_2}{|\xi|^3},
 \qquad
 F\left[\frac{x_1x_2}{|x|^4}\right]
       =-\pi^2\frac{\xi_1\xi_2}{|\xi|^3}.
\]
Every displayed density is locally integrable in dimension three. Both derivatives are derivatives of whole tempered pairings.

**Solution 5.** The quadratic scaling is \(Q(3(x-h))=9Q(x-h)\). Apply the proved translation identity to (1.9), and then the modulation with vector \(-b\). With \(\zeta=\xi+b\),
\[
 Fv(\xi)=\frac{2\pi^2}{9}
     \frac{e^{-i[(\xi_1+2)-2\xi_2]}}{P(\xi+b)^{1/2}},
 \quad P(\zeta)=\zeta_1^2+\zeta_2^2+2\zeta_3^2-2i\zeta_1\zeta_2.
\]
The singular frequency is \(-b\); elsewhere \(P(\xi+b)\) has positive real part and the root has the specified branch. The continuous tempered operations preserve the entire identity through that shifted origin.

**Solution 6.** Fourier F5 makes the multiplier for \(\partial_{\bar z}\) equal to \((i\xi-\eta)/2\). Theorem 2.1 therefore yields
\[
 F(\partial_{\bar z}E)
       =\frac{i\xi-\eta}{2}\frac2{i\xi-\eta}=1=F\delta_0.
\]
Polynomial multiplication of a regular locally integrable distribution is represented by the polynomial times its density. The resulting density equals one almost everywhere, hence defines precisely the constant distribution; changing its value at the single origin changes no integral. Fourier injectivity proves \(\partial_{\bar z}E=\delta_0\).

**Solution 7.** Reflect by \(R=\operatorname{diag}(1,-1)\). U052's full linear substitution rule has \(|\det R|=1\), \(R^{-T}=R\), so
\[
 F[1/(x-iy)](\xi,\eta)=\frac{2\pi}{i\xi+\eta}.
\]
The translation is \(h=(1,-2)\), and the positive modulation has vector \(c=(3,-2)\). Substitute \(\zeta=(\xi-3,\eta+2)\) in both the phase and the original spectrum:
\[
 Fw(\xi,\eta)
   =e^{-i[(\xi-3)-2(\eta+2)]}
                    \frac{2\pi}{i(\xi-3)+(\eta+2)}.
\]
The frequency singularity is at \((3,-2)\). The formulas act on full tempered distributions, including this point.

**Solution 8.** Product Gaussian integration and the multiplication rule give
\[
 F\phi_b(x,y)
   =i\partial_x\left[\frac\pi b e^{-r^2/(4b)}\right]
   =-\frac{i\pi x}{2b^2}e^{-r^2/(4b)}.
\]
Multiplying by \(k=(x-iy)/r^2\), the mixed angular term integrates to zero by reflection. The angular square integral is \(\pi\), by angular A5. The substitution \(t=r^2/(4b)\) gives \(\int_0^\infty r e^{-r^2/(4b)}dr=2b\). Thus
\[
 k(F\phi_b)=-\frac{i\pi}{2b^2}\,\pi(2b)
                    =-\frac{i\pi^2}{b}.
\]
Independently, the frequency integrand is
\[
 \frac{2\pi\xi}{i\xi-\eta}e^{-b\rho^2}
  =\left[-\frac{2\pi i\xi^2}{\rho^2}
          -\frac{2\pi\xi\eta}{\rho^2}\right]e^{-b\rho^2}.
\]
Again the mixed angular integral is zero and the square integral is \(\pi\). Now \(\int_0^\infty\rho e^{-b\rho^2}d\rho=1/(2b)\), giving \(-2\pi i\,\pi/(2b)=-i\pi^2/b\). Absolute integrability follows from the Gaussian radial bounds in both calculations. This checks the normalization and sign on an entire Schwartz pairing.

## References

- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2, Lemma 2.1 and Theorem 3.1: the complete canonical matrix branch and complex Gaussian transform.
- [Radial powers and the logarithmic endpoint](radial-powers-and-the-logarithmic-endpoint.md), Theorems 1.1 and 3.1 and Lemma 3.3: the whole radial and logarithmic identities. [Planar rotations and angular spectra](planar-rotations-and-angular-spectra.md), Theorem 1.1's proof: full linear substitution on distributions.
- [Complex powers at a boundary](complex-powers-at-a-boundary.md), H0–H1, and [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3, (C1)–(C2): scalar branches and complete joint holomorphic power-series proofs. Exact foundation sections are listed at the start.
- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), free author-hosted chapter, Section 3, pp. 26–28: Gaussian inversion and its two scalar Gaussian calculations. The author's Fourier normalization is symmetric; the programme normalization and all constants are derived in the supplied proofs.
- Jiří Lebl, [*Tasty Bits of Several Complex Variables*](https://www.jirka.org/scv/scv-3.4.pdf), free author edition, version 3.4, December 23, 2020, Theorem 1.2.1, pp. 17–18, and Theorem 4.1.1, pp. 109–110: polydisk series and Cauchy–Pompeiu comparison. The needed integration, derivative convergence, singular bounds and point-source normalization are fully proved here or in the supplied programme; external references replace no proof.
