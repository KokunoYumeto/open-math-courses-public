# Quadratic phases and curved spectra

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A Gaussian probability placed on a parabola has a frequency profile whose center, width and phase can all be measured. Its horizontal energy stays constant as the profile spreads. Removing the Gaussian weight produces a singular spectrum with delta limits in its slices. A quadratic phase that is constant in one input direction instead produces an actual delta factor in the full transform. We calculate these phenomena, prove the full signed Fresnel and parabolic identities, and then work out every rank and every polynomial curved moment.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-d}\), and complex bilinear distributional pairings. Strong dual convergence is uniform on every bounded test family.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves all Schwartz seminorm estimates, both inversion identities, the Gaussian mass and every transposed differential sign. [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma 0.1, proves the square-norm identity for Schwartz functions used in (P4); no completed \(L^2\) extension is needed here. The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16, proves absolute Fubini, dominated convergence and real linear substitution. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply compactness, calculus, cutoffs and matrix operations.

The complex Gaussian transform, its determinant branch and real symmetric diagonalization are proved in [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the transform part of Theorem 3.1. The scalar right-half-plane logarithm and its boundary argument are [Complex powers at a boundary](complex-powers-at-a-boundary.md), Lemma H0. We use the strict-positive-real-part Gaussian formula, then prove the signed distributional limits below.

## Partial transforms and strong distributional limits

**Lemma 0.1.** Fourier transformation in any selected coordinates is a continuous automorphism of the full Schwartz space. Its inverse has factor \((2\pi)^{-p}\) when \(p\) coordinates are transformed. Partial transforms in disjoint coordinate blocks commute and compose to the full transform. Their transposes, and the full Fourier transpose, preserve strong convergence in the tempered dual.

**Proof.** Write \(x\in\mathbb R^p\), \(y\in\mathbb R^q\), and set
\[
 (F_x\psi)(\xi,y)=\int e^{-ix\cdot\xi}\psi(x,y)\,dx.
\]
For multiindices in the indicated coordinate blocks, dominated differentiation and coordinate integration by parts give
\[
 \begin{gathered}
 \xi^\alpha y^\gamma\partial_\xi^\beta\partial_y^\delta F_x\psi\\
 =F_x\!\left[(-i\partial_x)^\alpha
       \bigl((-ix)^\beta y^\gamma\partial_y^\delta\psi\bigr)\right].
 \end{gathered}
\]
These steps follow the Fourier foundation, F2, with \(y\) as a parameter: on a compact parameter set every difference quotient is bounded by an integrable polynomial times a Schwartz weight in \(x\), and the integration-by-parts endpoints vanish. For an arbitrary function \(h(x,y)\) in the displayed right side, F1's product weight gives
\[
 \begin{gathered}
 \sup_{\xi,y}|F_xh(\xi,y)|\\
 \le\pi^p\sup_{x,y}
       \left(\prod_{j=1}^p(1+x_j^2)\right)|h(x,y)|.
 \end{gathered}
\]
Expand the finite derivatives and the product weight. Each right side is bounded by finitely many full \((x,y)\) Schwartz seminorms. This proves every mixed output seminorm estimate and continuity. For each fixed \(y\), F4's inverse identities in \(x\) apply; the inverse partial map is \((2\pi)^{-p}\) times reflection in \(x\) composed with \(F_x\), so it has the same continuity. Absolute Fubini on \(\psi\in\mathcal S(\mathbb R^{p+q})\) proves \(F_xF_y=F_yF_x=F\) pointwise. These identities transpose to \(\mathcal S'\).

A bounded family \(B\) of Schwartz tests has every seminorm uniformly bounded. The estimates just proved make \(F_xB\), and likewise \(FB\), bounded. For the strong seminorm \(q_B(u)=\sup_{\psi\in B}|u(\psi)|\), the bilinear transpose gives exactly
\[
 q_B(F_xu)=q_{F_xB}(u).
\]
This proves strong continuity directly, with no uniform-boundedness principle. The same argument applies to a fixed derivative, polynomial multiplier, translation or modulation, using F1's finite seminorm estimates. A zero-dimensional coordinate block uses the identity map and factor one. \(\square\)

## Watch a finite Gaussian weight spread through frequency

**Worked measurement P1.** Put a probability Gaussian on the parabola:
\[
\begin{gathered}
\mu_a(\phi)\\
=\sqrt{a/\pi}\int e^{-at^2}\phi(t,t^2)dt,\\
a>0.
\end{gathered}
\tag{P1}
\]
Its mass is one. Its transform is an ordinary bounded continuous function, since the defining measure is finite. With \(w=a+i\eta\), the positive-real-part Gaussian formula gives
\[
\begin{gathered}
M_a(\xi,\eta)
=\sqrt a\,w^{-1/2}e^{-\xi^2/(4w)},\\
|M_a(\xi,\eta)|^2\\
=\frac a{\sqrt{a^2+\eta^2}}
e^{-a\xi^2/[2(a^2+\eta^2)]}.
\end{gathered}
\tag{P2}
\]
The root is continued from positive real \(w\), so its argument is \(\tfrac12\arctan(\eta/a)\). Hence the full phase of this nonzero transform, with a continuous choice starting at zero, is
\[
\begin{gathered}
\arg M_a(\xi,\eta)\\
=-\tfrac12\arctan(\eta/a)\\
+\frac{\eta\xi^2}{4(a^2+\eta^2)}.
\end{gathered}
\tag{P3}
\]
This follows by writing \(1/w=(a-i\eta)/(a^2+\eta^2)\); it retains the oscillatory phase as well as the modulus. At height zero the frequency profile is \(e^{-\xi^2/(4a)}\). At larger heights its squared peak decreases and its width increases. The exact horizontal energy stays constant:
\[
\int_{\mathbb R}|M_a(\xi,\eta)|^2d\xi
=\sqrt{2\pi a}.
\tag{P4}
\]
Indeed, the Gaussian integral in (P2) is
\(\sqrt{2\pi(a^2+\eta^2)/a}\); multiplication by the prefactor proves (P4). Equivalently, each horizontal slice is the one-dimensional Fourier transform of \(\sqrt{a/\pi}e^{-at^2-i\eta t^2}\), whose squared input integral is \(\sqrt{a/(2\pi)}\). Plancherel supplies the same factor \(2\pi\). The curved support redistributes this slice energy rather than changing it. Solution 9 tracks its center when the Gaussian is moved along a scaled parabola.

## Follow the undamped slice and its first moment

**Worked measurement P2.** Remove the probability prefactor from (P1), so the curve density is \(e^{-at^2}dt\). Its transform is
\(G_a(\xi,\eta)=\sqrt\pi(a+i\eta)^{-1/2}e^{-\xi^2/[4(a+i\eta)]}\).
For \(\eta\ne0\), its limit as \(a\downarrow0\) is the density in Theorem C. Across \(\eta=0\), the common bound \(\sqrt\pi|\eta|^{-1/2}\) is locally integrable and integrable against Schwartz tests with separate polynomial weights. Thus this limit identifies the entire two-dimensional transform.

At height zero, however, the finite slice is
\[
\begin{gathered}
G_a(\xi,0)=\sqrt{\pi/a}e^{-\xi^2/(4a)},\\
\int G_a(\xi,0)d\xi=2\pi,\\
G_a(\cdot,0)\longrightarrow2\pi\delta_0\\
\text{strongly in }\mathcal S'(\mathbb R).
\end{gathered}
\tag{P5}
\]
To see the strong assertion directly, substitute \(\xi=2\sqrt a\,s\) into its pairing with \(\psi\). Subtract \(2\pi\psi(0)\), use
\(|\psi(2\sqrt a\,s)-\psi(0)|\leq2\sqrt a|s|\|\psi'\|_\infty\), and integrate the fixed Gaussian. The resulting error is at most \(4\sqrt{\pi a}\|\psi'\|_\infty\), uniformly on every bounded Schwartz family. The original undamped curve has the same strong trace from either sign of \(\eta\), as Solution 6 proves. Each assertion names a one-dimensional slice; Theorem C already fixes the whole two-dimensional density.

Weighting the finite curve by \(t\) instead gives
\[
\begin{gathered}
i\partial_\xi G_a(\xi,\eta)\\
=-\frac{i\xi}{2(a+i\eta)}G_a(\xi,\eta),\\
i\partial_\xi G_a(\cdot,0)
\longrightarrow2\pi i\delta'_0.
\end{gathered}
\tag{P6}
\]
The derivative formula follows from the exponent in \(G_a\), with its actual sign. The second limit follows by applying the proved strong slice limit to \(-i\psi'\); differentiation is a continuous operation on these test seminorms. For nonzero height, the pointwise limit is
\(-\xi H(\xi,\eta)/(2\eta)\), where \(H\) is Theorem C's density. Near an axis point with nonzero \(\xi\), its absolute value behaves as \(|\eta|^{-3/2}\) and is not locally integrable. Nevertheless the full two-dimensional derivative distribution \(i\partial_\xi H\) exists. For its input limit, \(|1-e^{-at^2}|\leq at^2\) bounds the difference on a test \(\phi\) by \(a\int |t|^3|\phi(t,t^2)|dt\). A sufficiently high first-coordinate Schwartz weight makes this integral finite and uniformly bounded on bounded test families. Strong Fourier continuity therefore identifies the derivative as the unique tempered limit of the weighted curves. Solution 11 supplies the entire finite-moment hierarchy.

## G. The damped calculation and its distributional boundary

For \(a>0\) and \(t>0\), the positive-real-part Gaussian formula gives

\[
\begin{gathered}
\mathcal F(e^{-(a-it)x^2})(\xi)
\\ =\sqrt\pi\,(a-it)^{-1/2}e^{-\xi^2/[4(a-it)]}.
\end{gathered} \tag{G1}
\]

The root is continued through the right half-plane from the positive real root. As \(a\downarrow0\), the input converges to \(e^{itx^2}\) in \(\mathcal S'\): every Schwartz test is integrable and the multiplier has modulus at most one. On the output side the modulus of the exponential is at most one, while \(|a-it|^{-1/2}\leq t^{-1/2}\). Dominated convergence against every Schwartz test therefore gives the full identity

\[
\widehat{e^{itx^2}}(\xi)
=\sqrt{\pi/t}\,e^{i\pi/4}e^{-i\xi^2/(4t)}. \tag{G2}
\]

Replacing \(t\) by \(-t\) in the damped calculation gives
\(\widehat{e^{-itx^2}}=\sqrt{\pi/t}e^{-i\pi/4}e^{i\xi^2/(4t)}\).
This is a direct calculation for either sign, rather than an unqualified conjugation of a complex distribution pairing.

For several independent real coordinates, apply the complex matrix Gaussian formula to the diagonal positive-real-part matrix. The input and output bounds just used apply to their products, so the same dominated convergence proves the whole product-space identity. An orthogonal linear change of coordinates has real Jacobian of absolute value one and preserves the Schwartz topology: its derivatives are finite linear combinations of derivatives and its polynomial weights are comparable. Changing variables in the damped integral and then taking the limit proves the corresponding rotated formula. Every inverse factor remains \((2\pi)^{-n}\).

## A. An indefinite quadratic in three dimensions

**Theorem A (a signed three-dimensional Fresnel transform).** As a tempered distribution on \(\mathbb R^3\),

\[
\begin{gathered}
\mathcal F(e^{i(x_1^2+x_2^2-x_3^2)})(\xi)
\\ =\pi^{3/2}e^{i\pi/4}e^{-i(\xi_1^2+\xi_2^2-\xi_3^2)/4}.
\end{gathered} \tag{A1}
\]

**Proof.** Multiply the two positive-sign instances and one negative-sign instance of (G2). The three root phases give \(e^{i(1+1-1)\pi/4}\). More explicitly, the damped input is \(e^{-a|x|^2+i(x_1^2+x_2^2-x_3^2)}\); its transform has prefactor \(\pi^{3/2}(a-i)^{-1}(a+i)^{-1/2}\) and the three corresponding quadratic exponents. Its modulus is at most \(\pi^{3/2}\), since \(|a\pm i|\geq1\) and the exponent has nonpositive real part. Both sides converge against all Schwartz tests by domination. This proves the full tempered identity, including the sign and phase; no product of merely conditionally convergent integrals has been interchanged. \(\square\)

## C. The full transform of the parabolic measure

**Theorem C (the parabolic measure).** Define \(u\in\mathcal S'(\mathbb R^2)\) by
\(u(\phi)=\int_{\mathbb R}\phi(t,t^2)dt\). Then

\[
\begin{gathered}
\widehat u(\xi,\eta)
=\sqrt\pi\,|\eta|^{-1/2}e^{-i\pi\operatorname{sgn}\eta/4}
\\ {}\cdot e^{i\xi^2/(4\eta)},\qquad \eta\ne0.
\end{gathered} \tag{C1}
\]

with the right side interpreted as its locally integrable, tempered function on the entire plane. No additional distribution on \(\eta=0\) occurs.

**Proof.** A Schwartz seminorm bounds \(|\phi(t,t^2)|\) by \(C(1+t^2)^{-1}\), so the curve integral defines a tempered distribution, locally of order zero. Put \(u_a(\phi)=\int e^{-at^2}\phi(t,t^2)dt\). Dominated convergence gives \(u_a\to u\) in \(\mathcal S'\). For \(a>0\), the total mass in \(t\) is finite, so Fubini against a Schwartz frequency test is absolute and the Gaussian formula gives

\[
\begin{gathered}
\widehat u_a(\xi,\eta)=\sqrt\pi\,(a+i\eta)^{-1/2}
\\ {}\cdot e^{-\xi^2/[4(a+i\eta)]}.
\end{gathered} \tag{C2}
\]

Its modulus is at most \(\sqrt\pi|\eta|^{-1/2}\) for \(\eta\ne0\), because the exponential has modulus at most one and \(|a+i\eta|\geq|\eta|\). The bound is locally integrable across \(\eta=0\), and integrable against every Schwartz test on the whole plane: use a weight \((1+|\xi|)^{-2}(1+|\eta|)^{-2}\). The right-half-plane root tends to \(|\eta|^{-1/2}e^{-i\pi\operatorname{sgn}\eta/4}\), and the exponent tends to \(i\xi^2/(4\eta)\). Dominated convergence therefore identifies the entire tempered limit with (C1), proving in particular the absence of a hidden line-supported term. The notation \(u=\delta(x_2-x_1^2)\) has precisely this density: integration in \(x_2\) against the scalar delta contributes Jacobian one. \(\square\)

## Locate the frequency delta produced by a flat direction

**Worked measurement P3.** Take the coupled quadratic
\[
\begin{gathered}
q(x)=x^TQx\\
=(x_1+x_2)^2-x_3^2,\\
Q=\begin{pmatrix}1&1&0\\1&1&0\\0&0&-1\end{pmatrix}.
\end{gathered}
\tag{P7}
\]
The orthonormal coordinates
\(s=(x_1+x_2)/\sqrt2\), \(r=(x_1-x_2)/\sqrt2\), \(t=x_3\)
have absolute Jacobian one, and \(q=2s^2-t^2\). The phase is constant in the entire \(r\) direction. Its matching frequency coordinates are
\(\sigma=(\xi_1+\xi_2)/\sqrt2\), \(\rho=(\xi_1-\xi_2)/\sqrt2\), \(\tau=\xi_3\).

Fourier inversion on a Schwartz test gives \(\mathcal F1=2\pi\delta_0\) in one dimension. Apply the signed Fresnel identities to \(s,t\), and this constant-input identity to \(r\). The product transform, justified by Lemma 0.1 and the full test-pairing calculation in Solution 10, is
\[
\begin{gathered}
\mathcal F(e^{iq})(\sigma,\rho,\tau)\\
=\sqrt2\,\pi^2
e^{-i\sigma^2/8+i\tau^2/4}\delta_0(\rho).
\end{gathered}
\tag{P8}
\]
The amplitudes are \(\sqrt{\pi/2}\), \(\sqrt\pi\), and \(2\pi\). The two nonzero eigenvalues \(2,-1\) contribute opposite quarter-turn phases, which cancel. Explicitly the right side acts on a test \(\Psi\) as
\(\sqrt2\pi^2\int e^{-i\sigma^2/8+i\tau^2/4}\Psi(\sigma,0,\tau)d\sigma d\tau\).
This integral is absolutely convergent because the restriction is Schwartz; it proves the meaning of the product distribution and its exact plane density. In original coordinates the plane is \(\xi_1=\xi_2\). It is perpendicular to the flat input direction \((1,-1,0)\).

The same conclusion can be checked before taking any distributional limit. Damping by \(e^{-a(s^2+r^2+t^2)}\) makes all three Gaussian integrals absolute. The \(r\) factor is precisely \(\sqrt{\pi/a}e^{-\rho^2/(4a)}\), which tends strongly to \(2\pi\delta_0(\rho)\); the other factors tend to the two signed Fresnel functions. The input convergence is strong in \(\mathcal S'\): on a bounded family of tests a single integrable Schwartz weight bounds the tails uniformly, while the multiplier tends uniformly to one on compact sets. Strong Fourier continuity then gives the entire limit (P8). This is an actual delta factor in the full three-dimensional transform. Solution 10 determines its form for every rank and every real symmetric quadratic.

## Exercises

**Exercise 1 (foundation: a shifted indefinite chirp).** Let \(\alpha_1,\alpha_2,\alpha_3\) be nonzero real numbers, and let \(b,c\in\mathbb R^3\). Compute the full tempered Fourier transform of
\[
q(x)=\exp\!\left(i\sum_{j=1}^3\alpha_j(x_j-c_j)^2+ib\cdot x\right).
\]
Retain the determinant factor, the signature phase and both shifts. Justify the result on the whole frequency space.

**Exercise 2 (intermediate: polynomial moments of a chirp).** For real \(\alpha\ne0\), put \(h(x)=e^{i\alpha x^2}\). Determine the full transforms of \(xh\) and \(x^2h\). Explain why multiplication by these polynomials is meaningful even though none of the ordinary transform integrals is absolutely convergent.

**Exercise 3 (foundation: scaling a curved measure).** For real \(\kappa\ne0\) and \(c\), define
\(u_{\kappa,c}(\phi)=\int\phi(t,\kappa t^2+c)dt\).
Compute its Fourier transform on all of \(\mathbb R^2\), including the branch and the behavior across \(\eta=0\). Does the notation \(\delta(y-\kappa x^2-c)\) introduce an additional arclength factor?

**Exercise 4 (intermediate: equations satisfied by a curved spectrum).** For the preceding curve measure prove
\[
\begin{gathered}
(y-\kappa x^2-c)u_{\kappa,c}=0,
\\ (\partial_x+2\kappa x\partial_y)u_{\kappa,c}=0.
\end{gathered}
\]
Translate both equations to frequency space and verify them directly where \(\eta\ne0\). Explain how their validity on the whole plane follows.

**Exercise 5 (intermediate: modulation and a first moment).** Weight the preceding curve measure by \(e^{ibt}\), with \(b\in\mathbb R\). Find its transform and the transform obtained by adding a factor \(t\). Give the first-moment formula away from \(\eta=0\), and specify its meaning on the full plane. Is the absolute value of that off-axis formula locally integrable across \(\eta=0\) near a point with \(\xi\ne b\)?

**Exercise 6 (advanced: a delta appears in frequency slices).** Let \(H_{\kappa,c}(\xi,\eta)=\widehat u_{\kappa,c}(\xi,\eta)\), with \(\eta\ne0\). Prove
\[
\begin{gathered}
H_{\kappa,c}(\cdot,\eta)\longrightarrow2\pi\delta_0
\\ \text{strongly in }\mathcal S'(\mathbb R),
\\ \eta\to0\text{ from either side}.
\end{gathered}
\]
Give an error bound on each test. Explain why this slice limit does not add a line-supported term to the two-dimensional transform.

**Exercise 7 (intermediate: a bilinear chirp with linear terms).** For real \(t\ne0\), \(\beta\) and \(\gamma\), compute the full transform of \(e^{itxy+i\beta x+i\gamma y}\). Account for negative \(t\), and explain why the two Fresnel root phases cancel.

**Exercise 8 (advanced: an entire transform which is not Schwartz).** Let \(\rho\in C_c^\infty(\mathbb R)\), with support in \([-R,R]\), \(R>0\), and \(\rho(0)\ne0\). Put
\(v(\phi)=\int\rho(t)\phi(t,\kappa t^2)dt\), where \(\kappa\ne0\). Show that \(\widehat v\) extends to an entire function of two complex variables and give an explicit growth bound. Find the leading asymptotic of \(\widehat v(0,\eta)\) as \(\eta\to\pm\infty\), and prove that \(\widehat v\) is not a Schwartz function on the real plane.

**Exercise 9 (intermediate: move a finite Gaussian along a curved support).** Let \(a>0\), \(m,c\in\mathbb R\), and \(\kappa\in\mathbb R\setminus\{0\}\). Define
\(\mu(\phi)=\sqrt{a/\pi}\int e^{-a(t-m)^2}\phi(t,\kappa t^2+c)dt\).
Compute its whole Fourier transform, including every phase and root. Determine each horizontal slice's peak, center, Gaussian precision and squared integral. Relate the center to the phase's stationary input point and the tangent to the parabola at \(t=m\).

**Exercise 10 (advanced: every degenerate real quadratic).** Let \(Q\) be a real symmetric \(n\)-by-\(n\) matrix, of any rank \(r\). Write \(K=\ker Q\), \(E=K^\perp\) and decompose the frequency orthogonally as \(\xi_E+\xi_K\). Prove the entire tempered transform of \(e^{ix^TQx}\), with its signature, nonzero determinant factor and delta in the \(K\) frequencies. Give its actual action on a test, include ranks zero and \(n\), and prove that its support is exactly \(E\) in frequency space.

**Exercise 11 (advanced: all curved moments and their strong traces).** For any integer \(m\geq0\), let
\(u_m(\phi)=\int t^m\phi(t,\kappa t^2+c)dt\), with \(\kappa\ne0\).
Compute its full Fourier transform from \(H_{\kappa,c}\). Derive a closed polynomial formula away from \(\eta=0\), including all lower terms. Determine when that off-axis formula is absolutely locally integrable across an axis point with \(\xi\ne0\). Prove its strong horizontal limit as \(\eta\to0\), with a testwise error bound and the exact derivative-of-delta factor.

## Solutions

**Solution 1.** The signed one-dimensional Fresnel identity, applied with \(|\alpha_j|\) in each coordinate, gives
\[
\begin{gathered}
\widehat q(\xi)
=\frac{\pi^{3/2}}{\sqrt{|\alpha_1\alpha_2\alpha_3|}}
e^{i\pi\sigma/4}e^{-ic\cdot(\xi-b)}
\\ {}\cdot\exp\!\left(-i\sum_{j=1}^3
\frac{(\xi_j-b_j)^2}{4\alpha_j}\right),
\\ \sigma=\sum_{j=1}^3\operatorname{sgn}\alpha_j.
\end{gathered}
\]
Indeed the substitution \(x=s+c\) contributes \(e^{-ic\cdot(\xi-b)}\), while modulation replaces \(\xi\) by \(\xi-b\). To justify every step globally, first replace the chirp in \(s\) by its product with \(e^{-a|s|^2}\), \(a>0\). Each Gaussian transform has root \((a-i\alpha_j)^{-1/2}\), continued from the positive half-plane. Its modulus is at most \(|\alpha_j|^{-1/2}\), and each quadratic exponential has modulus at most one. The input is bounded by one and the output by the displayed constant. Translation and modulation preserve integrability of Schwartz tests. Dominated convergence therefore proves the whole tempered identity. A negative coefficient contributes \(e^{-i\pi/4}\), without changing the positive determinant factor.

**Solution 2.** Write
\[
H(\xi)=\sqrt{\pi/|\alpha|}\,
e^{i\pi\operatorname{sgn}\alpha/4}e^{-i\xi^2/(4\alpha)}.
\]
Polynomial multiplication and differentiation are continuous on Schwartz tests and hence define transposed operations on tempered distributions. The identity \(\mathcal F(xh)=i\partial_\xi H\) follows by differentiating the negative-exponential test transform, with integration by parts on that Schwartz test. Since \(H'=-i\xi H/(2\alpha)\),
\[
\begin{gathered}
\mathcal F(xh)=\frac{\xi}{2\alpha}H,
\\ \mathcal F(x^2h)=
\left(\frac{\xi^2}{4\alpha^2}+\frac{i}{2\alpha}\right)H.
\end{gathered}
\]
The second formula is \(-H''\). Both right sides have polynomial growth, so they are actual tempered function representatives. These statements concern continuous distributional operations; absolute convergence of an undamped oscillatory integral is unnecessary.

**Solution 3.** The answer is the whole locally integrable tempered function
\[
\begin{gathered}
H_{\kappa,c}(\xi,\eta)=e^{-ic\eta}\sqrt\pi\,|\kappa\eta|^{-1/2}
\\ {}\cdot e^{-i\pi\operatorname{sgn}(\kappa\eta)/4}
e^{i\xi^2/(4\kappa\eta)},\qquad \eta\ne0.
\end{gathered}
\]
The curve functional is tempered because a Schwartz bound in the first coordinate makes its defining integral absolute. With the damping \(e^{-at^2}\), its transform is
\(e^{-ic\eta}\sqrt\pi(a+i\kappa\eta)^{-1/2}
e^{-\xi^2/[4(a+i\kappa\eta)]}\).
It is bounded by \(\sqrt\pi|\kappa\eta|^{-1/2}\), which is locally integrable across \(\eta=0\) and globally integrable against every Schwartz test using separate quadratic weights in \(\xi\) and \(\eta\). The original damped measures and these functions therefore converge on all Schwartz tests by domination. This proves the entire identity, without any additional term on \(\eta=0\). Integrating \(\delta(y-\kappa x^2-c)\) first in \(y\) has Jacobian one and yields precisely \(dt\). Arclength on the curve would instead have the different density \(\sqrt{1+4\kappa^2t^2}\,dt\).

**Solution 4.** The first multiplier vanishes at every point on the curve. For the second identity, distributional differentiation and multiplication give
\[
\begin{gathered}
\langle(\partial_x+2\kappa x\partial_y)u_{\kappa,c},\phi\rangle
\\ =-\int\phi_x(t,\kappa t^2+c)dt
\\ {}-2\kappa\int t\phi_y(t,\kappa t^2+c)dt=0.
\end{gathered}
\]
The bracket is the derivative of the restricted test, whose endpoints vanish. No extra divergence term appears because \(\partial_y(2\kappa x)=0\). The transformed equations are
\[
\begin{gathered}
(i\partial_\eta+\kappa\partial_\xi^2-c)H_{\kappa,c}=0,
\\ (i\xi-2\kappa\eta\partial_\xi)H_{\kappa,c}=0.
\end{gathered}
\]
Off the axis, logarithmic differentiation of the explicit function gives
\[
\begin{gathered}
\partial_\xi H=\frac{i\xi}{2\kappa\eta}H,
\\ \partial_\xi^2H=
\left(\frac{i}{2\kappa\eta}-\frac{\xi^2}{4\kappa^2\eta^2}\right)H,
\\ i\partial_\eta H=
\left(c-\frac{i}{2\eta}+\frac{\xi^2}{4\kappa\eta^2}\right)H.
\end{gathered}
\]
The terms cancel as required. Differentiating only this off-axis representative cannot decide whether a contact term exists on the axis. The full original curve equations and the whole Fourier identity prove both equations everywhere.

**Solution 5.** Modulation in the curve parameter gives
\(H_b(\xi,\eta)=H_{\kappa,c}(\xi-b,\eta)\).
The weighted functional with a factor \(t\) is tempered: the curve integral with that polynomial is still controlled by sufficiently high Schwartz decay in \(t\). Its full transform is the distribution \(i\partial_\xi H_b\). Away from \(\eta=0\) it is
\[
-\frac{\xi-b}{2\kappa\eta}
H_{\kappa,c}(\xi-b,\eta).
\]
On a small rectangle about an axis point with \(\xi\ne b\), its modulus is bounded below by a positive constant times \(|\eta|^{-3/2}\). Its absolute integral is infinite. Thus the full derivative is not obtained by treating that formula as a locally integrable density across the axis. The derivative of the already established tempered function defines it exactly and uniquely; no choice of an ad hoc extension is being made.

**Solution 6.** The full one-dimensional transform identity is
\(H_{\kappa,c}(\cdot,\eta)=e^{-ic\eta}
\mathcal F(e^{-i\kappa\eta t^2})\). For \(\psi\in\mathcal S(\mathbb R)\), its pairing is
\(\int e^{-i\eta(c+\kappa t^2)}\widehat\psi(t)dt\).
At \(\eta=0\) that integral is \(2\pi\psi(0)\). The elementary inequality \(|e^{is}-1|\leq|s|\) gives
\[
\begin{gathered}
|\langle H_{\kappa,c}(\cdot,\eta)-2\pi\delta_0,\psi\rangle|
\\ \leq|\eta|\int(|c|+|\kappa|t^2)|\widehat\psi(t)|dt.
\end{gathered}
\]
The weighted integral is uniformly bounded on every bounded Schwartz family by Fourier continuity and Schwartz decay. The convergence is therefore strong and holds from both signs. A distributional trace in one variable is not an extra two-dimensional summand: Solution 3 already identifies the full two-dimensional limit of the damped measures with its locally integrable density. Values assigned to that density on a Lebesgue null line do not change its distribution.

**Solution 7.** Rotate to \(s=(x+y)/\sqrt2\), \(r=(x-y)/\sqrt2\); then \(xy=(s^2-r^2)/2\) and the absolute Jacobian is one. The signed Fresnel factors for \(t/2\) and \(-t/2\) have phases \(e^{i\pi\operatorname{sgn}t/4}\) and its reciprocal. Their product is one. Their dual squares reduce the exponent to \(-i\xi\eta/t\), and their amplitudes multiply to \(2\pi/|t|\). Modulating gives
\[
\mathcal F(e^{itxy+i\beta x+i\gamma y})(\xi,\eta)
=\frac{2\pi}{|t|}
e^{-i(\xi-\beta)(\eta-\gamma)/t}.
\]
Positive damping in both rotated coordinates justifies the entire calculation by the bounded input and output argument of Solution 1. The absolute value in the prefactor is essential when \(t<0\).

**Solution 8.** The compact integral
\[
V(\zeta,\omega)=\int\rho(t)e^{-it\zeta-i\kappa t^2\omega}dt
\]
allows all complex derivatives under the integral, locally uniformly on complex compact sets. For example each derivative adds a bounded power of \(t\) or \(\kappa t^2\) on this fixed interval. Difference quotients with the same bounds prove the complex derivatives. More explicitly, around any fixed complex point the two exponential power series converge absolutely and uniformly for t in the compact integration interval and for the two variables in any fixed complex polydisc. Their product can be integrated term by term, giving a convergent joint power series on that polydisc. Thus the function is entire jointly in both variables. Its explicit bound is
\[
|V(\zeta,\omega)|\leq\|\rho\|_1
e^{R|\operatorname{Im}\zeta|+
|\kappa|R^2|\operatorname{Im}\omega|}.
\]
Apply the signed scalar identity paired with \(\rho\), taking frequency parameter \(T=|\kappa\eta|\) and sign \(-\operatorname{sgn}(\kappa\eta)\). Fourier inversion and \(|e^{is}-1|\leq|s|\) give
\[
\begin{gathered}
V(0,\eta)=\sqrt\pi\,|\kappa\eta|^{-1/2}
e^{-i\pi\operatorname{sgn}(\kappa\eta)/4}\rho(0)
\\ {}+O(|\eta|^{-3/2}).
\end{gathered}
\]
More explicitly, the signed transform and inverse transpose give
\[
 \begin{gathered}
 V(0,\eta)=\frac{\sqrt\pi\,|\kappa\eta|^{-1/2}
       e^{-i\pi\operatorname{sgn}(\kappa\eta)/4}}{2\pi}\\
 {}\cdot\int e^{i\xi^2/(4\kappa\eta)}\widehat\rho(\xi)\,d\xi.
 \end{gathered}
\]
The reflected inverse test has the same integral after \(\xi\mapsto-\xi\), because the quadratic multiplier is even. Subtract the multiplier one and use inversion at zero. The absolute error is at most
\[
 \frac{\sqrt\pi}{8\pi|\kappa\eta|^{3/2}}
       \int \xi^2|\widehat\rho(\xi)|\,d\xi.
\]
The integral is finite by F2. This proves the stated remainder with its actual normalization. Since the leading coefficient is nonzero, \(|\eta|^{1/2}|V(0,\eta)|\) tends to \(\sqrt{\pi/|\kappa|}|\rho(0)|>0\) along either half-axis. A Schwartz function would have \(|\eta|^2|V(0,\eta)|\) bounded. The claimed failure follows, even though the real transform is smooth, bounded by \(\|\rho\|_1\), and extends to an entire function.

**Solution 9.** Substitute \(t=s+m\), and put
\(w=a+i\kappa\eta\), \(\lambda=\xi+2\kappa m\eta\). The complete phase identity leaves the real Gaussian \(e^{-as^2}\) and the multiplier
\(e^{-i[m\xi+(\kappa m^2+c)\eta]}e^{-i\lambda s-i\kappa\eta s^2}\).
Since \(\operatorname{Re}w=a>0\), the whole complex Gaussian integral gives
\[
\begin{gathered}
\widehat\mu(\xi,\eta)\\
=e^{-i[m\xi+(\kappa m^2+c)\eta]}\\
{}\cdot\sqrt a\,w^{-1/2}e^{-\lambda^2/(4w)},\\
|\widehat\mu(\xi,\eta)|^2\\
=\frac a{\sqrt{a^2+\kappa^2\eta^2}}
e^{-a\lambda^2/[2(a^2+\kappa^2\eta^2)]}.
\end{gathered}
\tag{P9}
\]
The inverse root uses the positive-real-part branch and has phase
\(-\tfrac12\arctan(\kappa\eta/a)\); the exponent additionally contributes
\(\kappa\eta\lambda^2/[4(a^2+\kappa^2\eta^2)]\) to the argument. The entire complex phase also includes the first multiplier in (P9).

For fixed real \(\eta\), the squared peak is
\(a/\sqrt{a^2+\kappa^2\eta^2}\), its center is \(\xi=-2\kappa m\eta\), and its Gaussian precision is
\(a/[2(a^2+\kappa^2\eta^2)]\). Translation in \(\xi\) has Jacobian one, so the same Gaussian mass computation as (P4) gives squared slice integral \(\sqrt{2\pi a}\), independent of \(m,c,\eta\) and \(\kappa\). All conclusions concern ordinary functions: the finite measure and every Gaussian moment make the transform integral absolutely convergent and smooth.

For \(\eta\ne0\), the derivative of the original oscillatory phase in \(t\) is \(\xi+2\kappa\eta t\). Its unique stationary point is \(-\xi/(2\kappa\eta)\), which equals \(m\) exactly on the peak line. The tangent to the parametrized curve at \(m\) is \((1,2\kappa m)\), so the covector \((\xi,\eta)\) is perpendicular to it precisely when \(\xi+2\kappa m\eta=0\). At height zero, the formula gives the ordinary shifted Gaussian Fourier profile \(e^{-im\xi}e^{-\xi^2/(4a)}\), with its peak at zero; no division by \(\eta\) is used there.

**Solution 10.** The real symmetric diagonalization proved in U020, Section 2, gives an orthonormal basis with \(r\) nonzero eigenvalues \(\lambda_1,\ldots,\lambda_r\), followed by \(n-r\) zero eigenvalues. The restriction \(Q_E\) is invertible and symmetric, and put
\(\sigma=\sum_{j=1}^r\operatorname{sgn}\lambda_j\),
\(d_E=|\det Q_E|=\prod_{j=1}^r|\lambda_j|\).
For \(r=0\), both \(d_E\) and the empty product equal one, \(\sigma=0\), and the empty quadratic phase is zero. In the full-rank case the zero-dimensional delta factor is the identity. The orthogonal coordinate map has absolute Jacobian one. Signed Fresnel transforms in the nonzero coordinates and \(\mathcal F1=2\pi\delta_0\) in each zero coordinate therefore give
\[
\begin{gathered}
\mathcal F(e^{ix^TQx})(\xi_E,\xi_K)\\
=\frac{(2\pi)^{n-r}\pi^{r/2}}{\sqrt{d_E}}
e^{i\pi\sigma/4}\\
{}\cdot e^{-i\xi_E^TQ_E^{-1}\xi_E/4}
\delta_0(\xi_K).
\end{gathered}
\tag{P10}
\]
Its precise action is the prefactor in (P10) times
\(\int_E e^{-i\zeta^TQ_E^{-1}\zeta/4}\Psi(\zeta,0)d\zeta\), where \(d\zeta\) is Euclidean Lebesgue measure on the subspace. The restriction of a Schwartz test to this subspace is Schwartz, with each seminorm bounded by finitely many of the original ones after the fixed orthogonal change. Thus the integral is absolute and defines a tempered distribution. In dimension zero it is the value \(\Psi(0)\).

For a direct full-space justification of the product computation, first damp by \(e^{-a|x|^2}\). Absolute Fubini factors its Gaussian transform. The damped inputs tend strongly to the bounded chirp by a uniform integrable tail bound on each bounded test family and uniform convergence on compact sets. The full strong Fourier continuity then fixes their entire transformed limit. To identify that limit directly, apply Lemma 0.1 and inversion in the \(K\) variables. For \(k=n-r\),
\
 \begin{gathered}
 \langle\mathcal F(e^{ix_E^TQ_Ex_E}),\Psi\rangle\\
 =\int_E e^{ix_E^TQ_Ex_E}
       \left(\int_K F\Psi(x_E,x_K)\,dx_K\right)dx_E\\
 =(2\pi)^k\int_E e^{ix_E^TQ_Ex_E}
        F_E[\Psi(\cdot,0)\,dx_E.
 \end{gathered}
\]
The first integral is absolutely convergent because \(F\Psi\) is Schwartz and the chirp is bounded. For fixed \(x_E\), write \(F\Psi=F_K(F_E\Psi)\); inversion at zero in \(K\) gives the inner integral in the second line. The restriction \(\Psi(\cdot,0)\) and its partial Fourier transform are Schwartz by the mixed seminorm bounds, so the last integral is absolute too. The already proved product of nonzero signed Fresnel factors evaluates this last pairing and gives exactly (P10). For \(r=0\), the same calculation is full inversion at zero; for \(k=0\), omit that inversion step. This proves the distribution on every test, including both extreme ranks.

The support is contained in \(E\) because tests vanishing near the plane have zero restriction. To show equality, take any point \(\zeta_0\in E\) and any ambient neighborhood of it. Choose nonnegative nonzero \(\chi\in C_c^\infty(E)\), supported in a sufficiently small part of that neighborhood, and a compact smooth \(\theta\) in the \(K\) variables with \(\theta(0)=1\), of sufficiently small support. The test
\(\Psi(\zeta,k)=e^{i\zeta^TQ_E^{-1}\zeta/4}\chi(\zeta)\theta(k)\)
has support in the neighborhood, and its value under (P10) is the nonzero prefactor times \(\int_E\chi\). For \(r=0\), take a bump equal to one at zero; for \(K=\{0\}\), omit \(\theta\). Every point of \(E\) lies in the support. Rank zero gives \((2\pi)^n\delta_0\); full rank gives the usual everywhere nonzero Fresnel function with its exact determinant and signature.

**Solution 11.** The polynomially weighted curve is tempered: a sufficiently high Schwartz weight in the first coordinate bounds \(|t|^m|\phi(t,\kappa t^2+c)|\) by an integrable function. Multiplication by \(t^m\) is the restriction of multiplication by \(x^m\) on the ambient curve distribution. The exact transposed Fourier rule therefore proves the whole-plane identity
\(\widehat u_m=(i\partial_\xi)^mH_{\kappa,c}\).
This defines the full distribution even when its off-axis expression cannot be integrated absolutely across the axis.

For \(\eta\ne0\), the Taylor translation of the smooth representative is
\[
\begin{gathered}
\frac{H_{\kappa,c}(\xi+is,\eta)}{H_{\kappa,c}(\xi,\eta)}\\
=e^{-\xi s/(2\kappa\eta)-is^2/(4\kappa\eta)},\\
\widehat u_m(\xi,\eta)\\
=P_m(\xi,\eta)H_{\kappa,c}(\xi,\eta),\\
P_m(\xi,\eta)\\
=m!\sum_{j=0}^{\lfloor m/2\rfloor}
\begin{gathered}
\frac{(-\xi/(2\kappa\eta))^{m-2j}}{(m-2j)!}\\
{}\cdot\frac{(-i/(4\kappa\eta))^j}{j!}
\end{gathered}
.
\end{gathered}
\tag{P11}
\]
The analytic representative is entire in \(\xi\) at a fixed nonzero \(\eta\), so differentiating in \(s\) at zero is legitimate. The product of the two scalar exponential series gives every term in (P11). For example
\(P_1=-\xi/(2\kappa\eta)\) and
\(P_2=\xi^2/(4\kappa^2\eta^2)-i/(2\kappa\eta)\), with the second term retained.

In a small rectangle about \((\xi_0,0)\) with \(\xi_0\ne0\), the \(j=0\) term has modulus at least a positive constant times \(|\eta|^{-m}\). For \(m>0\), the sum of all \(j\geq1\) terms is bounded uniformly there by a constant times \(|\eta|^{-m+1}\), after restricting \(|\eta|\leq1\). The leading term therefore dominates for sufficiently small nonzero \(\eta\). Multiplying by \(|H|=\sqrt\pi|\kappa\eta|^{-1/2}\) shows that the absolute value is bounded above and below by positive multiples of \(|\eta|^{-m-1/2}\). It is locally integrable across that axis point exactly when \(m=0\). This is a statement about the representative away from the axis; the derivative distribution already exists for every \(m\).

Finally each horizontal slice is the one-dimensional transform of
\(t^m e^{-i\eta(c+\kappa t^2)}\). Its pairing with \(\psi\in\mathcal S\) is
\(\int t^m e^{-i\eta(c+\kappa t^2)}\widehat\psi(t)dt\).
At zero height, Fourier inversion differentiated \(m\) times makes this
\(2\pi(-i)^m\psi^{(m)}(0)=\langle2\pi i^m\delta_0^{(m)},\psi\rangle\).
The elementary exponential difference estimate gives
\[
\begin{gathered}
\bigl|\langle\widehat u_m(\cdot,\eta)\\
{}-2\pi i^m\delta_0^{(m)},\psi\rangle\bigr|\\
\leq|\eta|\\
{}\cdot\int |t|^m(|c|+|\kappa|t^2)
|\widehat\psi(t)|dt.
\end{gathered}
\tag{P12}
\]
Continuous Schwartz Fourier bounds and an integrable higher weight bound the last integral uniformly on every bounded test family. Hence the slices converge strongly from both signs to \(2\pi i^m\delta_0^{(m)}\). No line-supported summand is added to the full-plane derivative identity established at the start.

## References

- Supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5: complete Schwartz Fourier maps, inverse factors, derivatives and bilinear transposes. Lemma 0.1 here supplies the full partial-transform estimates and strong dual continuity.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and Theorem 3.1's transform proof: real symmetric diagonalization, determinant branch and complex Gaussian transform. [Complex powers at a boundary](complex-powers-at-a-boundary.md), Lemma H0, supplies the scalar logarithm. [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma 0.1, proves precisely the Schwartz Plancherel identity used here.
- Supplied [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16, [scalar](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite-algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, foundations. These supplied proofs retain their stated licences.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.6.1 and 7.6.3 and their answers on page 416. These identify the signed three-dimensional and parabolic calculations. The Gaussian damping, whole-plane proof, degenerate-rank argument, curved moments and eleven graded problems here are independently expressed.
- Michael Hitrik and Johannes Sjöstrand, [*Two minicourses on analytic microlocal analysis*](https://arxiv.org/abs/1508.00649v1), Chapter 1, §1.3, formula (1.3.27) in the proof of Theorem 1.3.3, printed pages 17–18: comparison for the complex quadratic Gaussian normalization. Its Chapter 2, §2.3, treats analytic stationary phase, a broader result not used in the proofs here. The full signed Fresnel limits, degenerate transforms and curved-moment identities are proved above; Solution 8 obtains its remainder directly from the exact transform.
