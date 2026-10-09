# Dispersion, measure obstructions and tempered point sources

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A Gaussian packet moves while its peak falls and its width grows, yet its total square-integral energy stays fixed. We calculate its center and current, then use dispersion of compact smooth inputs to determine the exact local-measure range of Fourier transforms. Bounded inputs show how a point measure, a smooth density and a principal value can arise from the same input norm. Finally, a Cauchy source and a quadratic phase produce a full three-dimensional point source; we measure its Gaussian regularization and prove the limits when the quadratic coefficient tends to zero from either sign.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-d}\), and complex bilinear distributional pairings. Strong dual convergence is uniform on every bounded test family.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz operations, inversion, Gaussian mass and transposed differential signs. Fourier-Laplace slices and boundary poles, Lemma 0.1, proves the completed \(L^2\) Fourier map, its exact norm factor and its agreement with the distributional transform. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and (G2), supplies every partial Fourier seminorm, strong transpose continuity and the signed Fresnel transform.

The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, proves dominated convergence, absolute Fubini, real linear substitution, Hölder's inequality and completeness of every \(L^p\), including \(L^\infty\). The [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), §6, proves the complete-metric Baire theorem. The [measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), Theorem M and (M10)–(M12), proves positive representation, complex variation and uniqueness on continuous compact tests. We prove the density and smooth-test consequences below. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, supplies the Euclidean compactness, calculus and cutoff constructions used in these arguments.

The exact Cauchy source normalization is [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem 1.1 and Corollary 1.2. The absolute complex Gaussian transform and its branch are [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the transform part of Theorem 3.1. All uses below retain the inverse factor and the displayed signs.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## Densities and equality of local measures

**Lemma 0.1.** If \(h\in L^1_{\mathrm{loc}}(X)\), where \(X\subset\mathbb R^n\) is open, then \(h\,dx\) is a locally finite complex Radon measure and its variation is \(|h|\,dx\). Two locally finite complex Radon measures which agree on all compact smooth tests agree as measures. Consequently a distribution which is a smooth function on an open subset has exactly that density there in any measure representation.

**Proof.** We may choose a Borel representative of \(h\). Indeed, approximate its real and imaginary parts by measurable simple functions. Integration §15.0 lets us replace each of their level sets by a Borel set modulo a subset of a Borel null set. Outside the countable union of these null sets the resulting Borel simple functions have the original limits; set the limit to zero on the exceptional Borel set. All integrals are unchanged.

First let \(h\ge0\). Monotone convergence proves countable additivity of \(\nu(A)=\int_Ah\,dx\), and local integrability gives finite mass on every relatively compact open set. The positive functional \(f\mapsto\int fh\,dx\) on \(C_c(X)\) has a Radon representative \(\eta\) by the measure foundation's Theorem M. Its increasing compact cutoffs inside each open set, constructed after (M3), and monotone convergence show \(\eta(U)=\nu(U)\) for every open \(U\). On each relatively compact open set both measures are finite, so the integration foundation's §16.2 generating-class proof extends equality from relative open sets to Borel sets. An increasing exhaustion of \(X\) finishes the identification. Apply this to the positive and negative parts of the real and imaginary parts of a general \(h\).

For a Borel set \(A\) contained in a relatively compact open set, every finite partition gives
\[
 \sum_j\left|\int_{A_j}h\,dx\right|\le\int_A|h|\,dx.
\]
For the opposite inequality, set \(s=\overline h/|h|\) where \(h\ne0\), and \(s=0\) elsewhere. Partition its bounded complex range into finitely many sets of diameter at most \(\varepsilon\), choosing in each nonempty set a value from the range. This gives a simple function \(s_\varepsilon\) with \(|s_\varepsilon|\le1\) and \(|s_\varepsilon-s|\le\varepsilon\). Its level sets partition \(A\), whence
\[
 \begin{gathered}
 |h\,dx|(A)\ge\operatorname{Re}\int_A s_\varepsilon h\,dx\\
 \ge(1-\varepsilon)\int_A|h|\,dx.
 \end{gathered}
\]
Let \(\varepsilon\downarrow0\). This proves equality of the locally finite variation measures; exhaustion gives the same equality on arbitrary Borel sets.

Finally, extend \(f\in C_c(X)\) by zero and convolve it with a nonnegative smooth mollifier of mass one supported in a ball of radius \(\varepsilon\). For small \(\varepsilon\) the smooth approximants have support in one compact subset of \(X\). Uniform continuity gives
\[
 \|f*\rho_\varepsilon-f\|_\infty
 \le\sup_{|u|\le\varepsilon,\,x}|f(x-u)-f(x)|\longrightarrow0.
\]
The cutoff and integration foundations supply this mollifier and differentiation under its integral. Finite variation on the common compact support lets each measure pairing pass to the limit. Thus equality on smooth tests implies equality on continuous compact tests, and the measure foundation's complex uniqueness proves the assertion. Applying this on any smaller open subset proves the final statement. \(\square\)

## Track a unit Gaussian packet as it moves and spreads

**Worked measurement D1.** Let \(b>0\), \(m,p\in\mathbb R^d\), and start with
\[
\begin{gathered}
g(x)=C_b e^{-b|x-m|^2+ip\cdot x},\\
C_b=(2b/\pi)^{d/4},\qquad \|g\|_2=1.
\end{gathered}
\tag{M1}
\]
The normalization follows by integrating \(C_b^2e^{-2b|x-m|^2}\). Use the multiplier \(\widehat{U_tg}=e^{it|\xi|^2}\widehat g\), for every real \(t\). With
\(h=1-4ibt\), \(A=|h|^2=1+16b^2t^2\), and
\(r=x-m+2tp\), the complete complex Gaussian calculation gives
\[
\begin{gathered}
U_tg(x)=C_b h^{-d/2}\\
{}\cdot e^{ip\cdot x+it|p|^2}e^{-b|r|^2/h},\\
|U_tg(x)|^2=C_b^2 A^{-d/2}\\
{}\cdot e^{-2b|r|^2/A}.
\end{gathered}
\tag{M2}
\]
The power is continued from one at time zero through \(\operatorname{Re}h=1\). To check the translation sign, put \(\xi=\zeta+p\) in Fourier inversion. The factor \(e^{it|\zeta+p|^2}\) leaves the spatial argument \(x-m+2tp\), and the remaining phase is \(e^{ip\cdot x+it|p|^2}\). The unmodulated Gaussian calculation is Solution 1; translation and modulation preserve its absolute inverse integrals.

The density in (M2) integrates to one for every time: set \(r=\sqrt A\,s\). Its center moves along \(m-2tp\). Its squared peak falls to \(C_b^2A^{-d/2}\), while the variance of each coordinate becomes
\[
\operatorname{Var}(x_j)=\frac{A}{4b}
=\frac1{4b}+4bt^2.
\tag{M3}
\]
Indeed, the centered odd Gaussian moment vanishes, and integration by parts in one coordinate gives
\(\int s_j^2e^{-2b|s|^2}ds=(4b)^{-1}\int e^{-2b|s|^2}ds\).
For any fixed \(R\), the mass in the ball of radius \(R\) about the moving center is at most
\(|B_R|C_b^2A^{-d/2}\), which tends to zero as \(|t|\to\infty\). Under the moving and rescaled coordinate \(s=(x-m+2tp)/\sqrt A\), however, its probability density is exactly the fixed \(C_b^2e^{-2b|s|^2}\). The unit energy spreads to a growing length scale. Solution 9 computes the current that carries it.

## Compare three Fourier outputs of bounded inputs

**Worked measurement D2.** In one dimension, the constant, a chirp and the sign function all have input supremum norm one. Their whole tempered transforms are
\[
\begin{gathered}
\mathcal F1=2\pi\delta_0,\\
\mathcal F(e^{i\alpha x^2})=\sqrt{\pi/|\alpha|}\\
{}\cdot e^{i\pi\operatorname{sgn}\alpha/4}e^{-i\xi^2/(4\alpha)},\\
\alpha\ne0,\\
\mathcal F(\operatorname{sgn}x)=-2i\operatorname{pv}(1/\xi).
\end{gathered}
\tag{M4}
\]
Scalar inversion on a Schwartz test proves the first identity. The full signed Fresnel limit in the quadratic-phase lesson proves the second; Solution 5 below proves the third by absolute damping and exact subtraction at zero.

The first output is a finite point measure. The second is an ordinary smooth, locally finite measure density whose total variation on the whole line is infinite, since its modulus is the nonzero constant \(\sqrt{\pi/|\alpha|}\). The third is a smooth density away from zero and has no measure representation in any neighborhood of zero. In Solution 5, bounded compact tests detect its diverging \(2\log(r/\varepsilon)\) pairing. Thus the same input norm can lead to three different output behaviors. Multiplying the last input by \(e^{ibx}\) moves its obstruction to frequency \(b\), because the transform becomes \(-2i\operatorname{pv}(1/(\xi-b))\). Theorem B handles every \(p>2\) on every open frequency region; Solution 10 quantifies the test family used in that argument.

## B. Dispersive Schwartz functions and the exact local-measure range

Let \(n\geq1\). A complex measure below means a locally finite complex Radon measure; it need not have finite total mass on all of \(\mathbb R^n\). Every \(g\in L^p\), \(1\le p\le\infty\), defines a tempered distribution: Hölder bounds \(|\int g\phi|\) by \(\|g\|_p\|\phi\|_{p'}\), and a sufficiently high product weight bounds the latter test norm by finitely many Schwartz seminorms. This includes the endpoints \(p'=1,\infty\). Thus every Fourier transform used here has the proved distributional meaning.

**Theorem B (the exact local-measure range).** For \(f\in C_c^\infty(\mathbb R^n)\) and every \(t>0\), there is a unique \(f_t\in\mathcal S\) with

\[
\begin{gathered}
\widehat{f_t}(\xi)=\widehat f(\xi)e^{it|\xi|^2},
\\ \|f_t\|_\infty\leq(4\pi t)^{-n/2}\|f\|_1.
\end{gathered} \tag{B1}
\]

Every Fourier transform of an \(L^p(\mathbb R^n)\) function is a locally finite complex measure exactly for \(1\leq p\leq2\). For every \(p>2\), including \(p=\infty\), there is an \(L^p\) function whose Fourier transform is not a measure on any nonempty open subset.

**Proof of the construction and its norms.** For fixed \(t\), every derivative of \(e^{it|\xi|^2}\) is a polynomial times that same modulus-one function. The full product rule makes \(\widehat f e^{it|\xi|^2}\) Schwartz. Fourier inversion gives unique Schwartz \(f_t\). The inverse transform of the phase, from (G2) in every coordinate, is the bounded smooth function

\[
\begin{gathered}
K_t(x)=(4\pi t)^{-n/2}e^{in\pi/4}
\\ {}\cdot e^{-i|x|^2/(4t)}.
\end{gathered} \tag{B2}
\]

Consequently \(f_t=f*K_t\), with an absolutely convergent ordinary convolution. To check the distributional convolution identity explicitly, pair the convolution with a Schwartz test. Boundedness of \(K_t\), compact support of \(f\), and integrability of the test justify the first Fubini interchange. Transforming a translated \(K_t\) multiplies its transform by the corresponding negative-sign exponential. Integrating these factors against \(f\) gives exactly \(\widehat f e^{it|\xi|^2}\). All integrals against the fixed Schwartz test remain absolutely bounded, so this also justifies moving the compact integral through the distribution pairing. Fourier injectivity proves the equality. Formula (B2) gives (B1), for all \(t>0\), in particular for \(t>1\). Plancherel gives

\[
\begin{gathered}
\|f_t\|_2=\|f\|_2,
\\ \|f_t\|_p^p\leq\|f_t\|_\infty^{p-2}\|f\|_2^2,
\\ 2<p<\infty.
\end{gathered} \tag{B3}
\]

Thus \(\|f_t\|_p\to0\) for every \(p>2\); for \(p=\infty\) use (B1).

**Proof of the positive range.** For \(f\in L^1\), dominated convergence makes \(\widehat f\) bounded and continuous, hence a locally finite measure density by Lemma 0.1. For \(1<p<2\), split
\(f=f_1+f_2\), where \(f_1=f1_{\{|f|>1\}}\) and \(f_2=f1_{\{|f|\leq1\}}\). The inequalities \(|f|\leq|f|^p\) on the first set and \(|f|^2\leq|f|^p\) on the second give \(f_1\in L^1\), \(f_2\in L^2\). Their distributional transforms agree with the ordinary and completed transforms, respectively, by the full Fourier agreement proofs. A bounded function plus an \(L^2\) function is locally \(L^1\): Cauchy--Schwarz gives \(\int_K|g|\leq|K|^{1/2}\|g\|_2\) on every compact \(K\). Therefore Lemma 0.1 makes their sum a locally finite measure density. For \(p=2\), use the completed Plancherel transform directly. This proves precisely the requested measure assertion without assuming an interpolation theorem.

**The Baire obstruction, on an arbitrary open region.** Fix \(p>2\) and a closed ball \(Q\) with nonempty interior. For every positive integer \(N\), let

\[
\begin{gathered}
E_N=\{g\in L^p:\ \forall\phi\in\mathcal D_Q,
\\ |\langle\widehat g,\phi\rangle|\leq N\|\phi\|_\infty\}.
\end{gathered} \tag{B4}
\]

Each \(E_N\) is closed. Indeed \(\langle\widehat g,\phi\rangle=\int g\widehat\phi\), and Hölder bounds this continuous linear functional on \(L^p\) by \(\|g\|_p\|\widehat\phi\|_{p'}\); the latter norm is finite since \(\widehat\phi\) is Schwartz, including \(p'=1\) for \(p=\infty\). Arbitrary intersections of its closed inequalities are closed.

Every \(E_N\) has empty interior. Otherwise some norm ball \(B(g_0,r)\) lies in \(E_N\). Subtraction at \(g_0\) bounds the pairing for every \(h\) with \(\|h\|_p<r\) by \(2N\|\phi\|_\infty\). Scaling \(h=rg/(2\|g\|_p)\), with the zero case immediate, gives

\[
\begin{gathered}
|\langle\widehat g,\phi\rangle|
\\ \leq(4N/r)\|g\|_p\|\phi\|_\infty,
\\ g\in L^p,\quad \phi\in\mathcal D_Q.
\end{gathered} \tag{B5}
\]

Choose a compact smooth \(f\) whose transform is nonzero on a small open ball inside \(Q^\circ\). This is explicit: modulate a nonnegative compact bump of nonzero integral so that its transform is nonzero at any selected interior point, then use continuity. Choose a nonzero nonnegative \(\psi\in\mathcal D\) supported in that small ball. The tests

\[
\phi_t(\xi)=\psi(\xi)e^{-it|\xi|^2}
\frac{\overline{\widehat f(\xi)}}{|\widehat f(\xi)|}
\]

are smooth compact tests in \(\mathcal D_Q\), with \(\|\phi_t\|_\infty=\|\psi\|_\infty\). Their pairing with \(\widehat{f_t}\) is the fixed positive number \(\int\psi|\widehat f|\). But (B5) and (B3) force it to tend to zero. This contradiction proves empty interior.

If \(\widehat g\) is a measure on an open set containing \(Q\), its finite variation on \(Q\) puts \(g\) in some \(E_N\). Choose countably many such closed balls with rational centers and radii, whose interiors refine every nonempty Euclidean open set. Each \(L^p\setminus E_N\) is open and dense. The complete \(L^p\) norm metric, including \(L^\infty\), and the full complete-metric Baire theorem give a dense intersection of all these complements over the countable balls and integers. Any member has Fourier transform that cannot be represented by a measure on any nonempty open set: a measure on such a set would give an \(E_N\) bound on one of its contained balls. This proves the negative range and the stronger local conclusion. It uses pointwise distributions and a countable family of level sets, without assuming an unproved closed-graph map into a measure space. \(\square\)

## D. A tempered Cauchy--Schrödinger point source

**Theorem D (a Cauchy–Schrödinger point source).** In original coordinates \((x,y,z)\in\mathbb R^3\), one tempered fundamental solution of
\(L=\partial_x+i\partial_y+\partial_z^2\) is the locally integrable function

\[
\begin{gathered}
E(x,y,z)=
\\ \frac{e^{iz^2/(4y)-i\pi\operatorname{sgn}y/4}}
{2\pi(x+iy)\sqrt{4\pi|y|}},
\\ y\ne0,\quad LE=\delta_{(0,0,0)}.
\end{gathered} \tag{D1}
\]

The values on \(y=0\) do not affect this locally integrable representative.

**Proof.** The full Cauchy source formula gives
\(k(x,y)=1/[2\pi(x+iy)]\) and \((\partial_x+i\partial_y)k=\delta_{(0,0)}\). The factor is half the \(1/\pi z\) kernel because the operator is \(2\bar\partial\). Consider the mixed-coordinate tempered function

\[
V(x,y,\tau)=k(x,y)e^{-iy\tau^2}. \tag{D2}
\]

The kernel \(1/\sqrt{x^2+y^2}\) is locally integrable, and polynomial weights make it integrable at infinity together with the remaining \(\tau\) coordinate. Hence \(k\otimes1\) is tempered. Every derivative of the modulus-one smooth factor is a polynomial in \(y,\tau\) times that factor; its multiplication preserves \(\mathcal S\) and is therefore defined on \(\mathcal S'\). Distributional product differentiation yields

\[
(\partial_x+i\partial_y-\tau^2)V=\delta_{(0,0)}\otimes1. \tag{D3}
\]

Indeed \(i\partial_y e^{-iy\tau^2}=\tau^2e^{-iy\tau^2}\), which cancels the displayed negative multiplier, while multiplication at the point source evaluates the exponential at \(y=0\) and gives one.

The exact partial inverse Fourier transform in \(\tau\), with coefficient \((2\pi)^{-1}\), converts the right side of (D3) to \(\delta_{(0,0,0)}\) and converts multiplication by \(-\tau^2\) to \(\partial_z^2\). It remains to prove that this inverse is the actual function (D1), including its behavior at \(y=0\).

For \(a>0\), insert \(e^{-a\tau^2}\) into (D2). Its partial inverse is, by an absolute Gaussian integral,

\[
\begin{gathered}
E_a(x,y,z)=k(x,y)(4\pi)^{-1/2}
\\ {}\cdot(a+iy)^{-1/2}e^{-z^2/[4(a+iy)]}.
\end{gathered} \tag{D4}
\]

Fubini against a fixed Schwartz test is absolute: the damped \(\tau\) integral has finite mass, and \(|k|\) is integrable with the remaining test weights. For \(y\ne0\),
\(|E_a|\leq C|y|^{-1/2}/\sqrt{x^2+y^2}\), independently of \(z\). This majorant is locally integrable. To check the only delicate planar corner, for \(0<|y|<1\),
\(\int_{-1}^1(x^2+y^2)^{-1/2}dx\leq C(1+|\log|y||)\); integrating its product with \(|y|^{-1/2}\) is finite. The first inequality follows by splitting \(|x|\leq|y|\) and \(|y|<|x|\leq1\).

The same majorant integrates against every Schwartz test globally. Specifically, its integral in \(x\) with weight \((1+|x|)^{-2}\) is bounded by \(C(1+|\log|y||)\) for \(|y|\leq1\), and by \(C/|y|\) for \(|y|>1\). Multiply by \((1+|y|)^{-2}(1+|z|)^{-2}\) and integrate; a finite monomial Schwartz seminorm controls that product weight. Thus (D1) is tempered and dominated convergence gives \(E_a\to E\) on all Schwartz tests. On the mixed side, dominated convergence gives \(e^{-a\tau^2}V\to V\); the exact partial-transform continuity identifies the limits. The right-half-plane root in (D4) has precisely the phase in (D1). Applying the partial inverse to (D3) now proves the full weak point-source identity, with no extra sheet term at \(y=0\). \(\square\)

## Measure the source before removing its Gaussian regularization

**Worked measurement D3.** Keep the Gaussian \(e^{-a\tau^2}\), \(a>0\), in the mixed-coordinate construction of Theorem D. Its inverse in the \(z\) coordinate is the displayed \(E_a\) in (D4). The exact mixed equation, now with that Gaussian retained, gives
\[
\begin{gathered}
LE_a=\delta_{(0,0)}(x,y)\otimes r_a(z),\\
r_a(z)=(4\pi a)^{-1/2}e^{-z^2/(4a)},\\
\int r_a(z)dz=1,\\
\int z^2r_a(z)dz=2a.
\end{gathered}
\tag{M5}
\]
Indeed, multiplying (D3) by \(e^{-a\tau^2}\) commutes with its \(x,y\) derivatives and \(\tau^2\) multiplier. At the point source the factor is exactly \(e^{-a\tau^2}\). The partial inverse Fourier map turns it into \(r_a\), with coefficient \((2\pi)^{-1}\). The Gaussian moments follow by substitution and one integration by parts. At positive \(a\), the source is therefore a Gaussian of width \(\sqrt{2a}\) along \(z\), supported on the line \(x=y=0\); it is not yet a point mass in all three coordinates.

For a Schwartz test \(\phi\), Taylor's formula for \(\phi(0,0,z)\), cancellation of the odd first moment and (M5) give
\[
\begin{gathered}
\bigl|\langle LE_a-\delta_{(0,0,0)},\phi\rangle\bigr|\\
\leq a\|\partial_z^2\phi\|_\infty.
\end{gathered}
\tag{M6}
\]
This proves strong source convergence, uniformly on bounded test families. The regularized solutions themselves also converge strongly to \(E\). Theorem D supplies a common integrable weighted majorant for \(|E_a|\) and \(|E|\). Choose a fixed sufficiently high radial weight \(w(s)=(1+|s|)^{-N}\); then
\(\int w(s)|E_a(s)-E(s)|ds\to0\) by dominated convergence, since the functions converge for almost every \(y\ne0\). On any bounded Schwartz family, \(|\phi(s)|\leq M w(s)\) with one common \(M\), so its pairing error is bounded by that vanishing weighted integral times \(M\). No uniform bound on the unweighted absolute values is needed. Solution 11 follows this construction when the coefficient of \(\partial_z^2\) also tends to zero from either sign.

## Exercises

**Exercise 1 (foundation: a dispersed Gaussian).** Let \(f(x)=e^{-b|x|^2}\), \(b>0\), on \(\mathbb R^d\), \(d\geq1\), and define \(\widehat f_t=\widehat f e^{it|\xi|^2}\), \(t\in\mathbb R\). Compute \(f_t\) and all its \(L^p\) norms for \(1\leq p\leq\infty\). Determine the large-time behavior in each range of \(p\).

**Exercise 2 (intermediate: the outgoing profile and the best constant).** For \(f\in C_c^\infty(\mathbb R^d)\), derive a uniform asymptotic for
\(t^{d/2}e^{it|v|^2}f_t(2tv)\) as \(t\to+\infty\), valid for all \(v\in\mathbb R^d\). Give an explicit error bound. Use a nonnegative nonzero \(f\) to show that the constant \((4\pi)^{-d/2}\) in the dispersive \(L^1\)-to-supremum bound cannot be decreased.

**Exercise 3 (intermediate: a Schwartz group and its equation).** On \(\mathcal S(\mathbb R^d)\), define \(U_t f\) by the same Fourier multiplier for every real \(t\). Prove the group law, differentiation with respect to time in the Schwartz topology, its differential equation, and preservation of the square-integral norm.

**Exercise 4 (intermediate: a quantitative local-measure estimate).** For \(1<p<2\), \(f\in L^p(\mathbb R^d)\), and a compact set \(K\) of positive Lebesgue measure, prove that \(\widehat f\) has an \(L^1(K)\) density and that
\[
\|\widehat f\|_{L^1(K)}
\leq 2(2\pi)^{d(1-1/p)}|K|^{1/p}\|f\|_p.
\]
Use a threshold split of the input rather than an interpolation theorem. State the direct endpoint bounds when \(p=1,2\). No optimality claim is requested for the displayed constant.

**Exercise 5 (advanced: an explicit bounded input whose transform is not a measure).** In one dimension compute \(\mathcal F(\operatorname{sgn}x)\) by damping the input with \(e^{-a|x|}\). Prove that the resulting distribution is not a locally finite measure on any neighborhood of frequency zero. Compare this example's singular region with the stronger Baire conclusion in Theorem B.

**Exercise 6 (intermediate: an anisotropic point source and its degenerate limit).** For \(\beta>0\), find a tempered fundamental solution \(E_\beta\) of
\(L_\beta=\partial_x+i\partial_y+\beta\partial_z^2\)
from Theorem D's \(E\). Prove the exact delta normalization and show
\(E_\beta\to k(x,y)\otimes\delta_0(z)\) strongly in \(\mathcal S'\) as \(\beta\downarrow0\), where \(k=1/[2\pi(x+iy)]\).

**Exercise 7 (advanced: a dipole is a distribution, not an absolute density).** Show that \(T=\partial_zE\) is a tempered solution of \(LT=\partial_z\delta_0\). Give its classical formula where \(y\ne0\), and prove that \(T\) cannot be represented by a locally finite measure on a neighborhood of \((1,0,1)\). Explain why differentiating the locally integrable \(E\) remains legitimate.

**Exercise 8 (advanced: solving compact smooth forcing).** Let \(g\in C_c^\infty(\mathbb R^3)\). Define \(w(x)=\int E(s)g(x-s)ds\), using Theorem D's actual locally integrable representative. Prove that \(w\) is smooth, has polynomial growth together with all derivatives, is tempered, and satisfies \(Lw=g\). Justify the integrals and the weak source calculation.

**Exercise 9 (intermediate: the Gaussian packet's probability current).** For the normalized \(U_tg\) in (M2), put \(\rho_t=|U_tg|^2\) and \(J_t=-2\operatorname{Im}(\overline{U_tg}\nabla U_tg)\). Derive the exact current and prove the continuity equation with the sign of the lesson's evolution. Compute the density's mean, coordinate covariance, mean momentum and total current. Relate the total current to the velocity of the moving center.

**Exercise 10 (advanced: a quantitative obstruction in any input ball).** Fix \(2<p\leq\infty\), a closed frequency ball \(Q\) with nonempty interior, an input \(g_0\in L^p\), and a radius \(r>0\). Use the compact smooth \(f\) and the tests \(\phi_t\) in Theorem B to give a power-law lower bound for their pairings with \(f_t/\|f_t\|_p\). For any \(N>0\), construct an \(h\) with \(\|h\|_p<r\) and a test supported in \(Q\) such that
\(|\langle\widehat{g_0+h},\phi\rangle|>N\|\phi\|_\infty\).
Give an explicit sufficient choice of \(t\), including \(p=\infty\), and explain its role in the complete Baire proof.

**Exercise 11 (advanced: signed coefficients and commuting source limits).** For real \(\beta\) and \(a\geq0\), define the tempered mixed function
\(V_{\beta,a}(x,y,\tau)=k(x,y)e^{-a\tau^2-i\beta y\tau^2}\), with
\(k=1/[2\pi(x+iy)]\), and let \(E_{\beta,a}\) be its exact partial inverse in \(\tau\). Find the ordinary formula when \(a>0\), and its full source for \(L_\beta=\partial_x+i\partial_y+\beta\partial_z^2\). Determine the undamped formula for either nonzero sign of \(\beta\), the case \(\beta=0\), and a strong joint estimate as \((a,\beta)\to(0,0)\). Prove that the two iterated limits agree and retain every root and inverse factor.

## Solutions

**Solution 1.** The positive-real-part Gaussian integral and the inverse factor give
\[
f_t(x)=(1-4ibt)^{-d/2}
e^{-b|x|^2/(1-4ibt)}.
\]
The power is continued in the right half-plane from its value one at \(t=0\). Put \(A=1+16b^2t^2\). The modulus is
\(A^{-d/4}e^{-b|x|^2/A}\). Hence, for finite \(p\),
\[
\begin{gathered}
\|f_t\|_p=
\left(\frac{\pi}{pb}\right)^{d/(2p)}A^{-d/4+d/(2p)},
\\ \|f_t\|_\infty=A^{-d/4}.
\end{gathered}
\]
The formulas include \(t=0\) and both signs of time. As \(|t|\to\infty\), the norms grow for \(p<2\), remain exactly constant for \(p=2\), and tend to zero for \(p>2\), including \(p=\infty\). The preserved \(L^2\) norm is \((\pi/(2b))^{d/4}\). This input is Schwartz rather than compactly supported; the direct Gaussian calculation proves all the assertions without extending a compact-support convolution argument by assumption.

**Solution 2.** Substitute \(x=2tv\) into the already proved absolute convolution with \(K_t\). Expanding \(|2tv-y|^2\) gives
\[
\begin{gathered}
t^{d/2}e^{it|v|^2}f_t(2tv)
\\ =(4\pi)^{-d/2}e^{id\pi/4}
\int f(y)e^{iv\cdot y}e^{-i|y|^2/(4t)}dy.
\end{gathered}
\]
The integral with its last exponential removed is \(\widehat f(-v)\). For every \(v\) the error is at most
\[
\frac{(4\pi)^{-d/2}}{4t}\int |y|^2|f(y)|dy.
\]
It is independent of \(v\). When \(f\geq0\) is nonzero, the formula at \(v=0\) gives
\(t^{d/2}|f_t(0)|\to(4\pi)^{-d/2}\|f\|_1\).
Any strictly smaller universal constant for all such inputs and all positive times would contradict this limit. The original constant is therefore best possible in that precise norm estimate.

**Solution 3.** Fourier injectivity and multiplication of the phases give \(U_sU_t=U_{s+t}\), \(U_0=I\), and \(U_t^{-1}=U_{-t}\). All derivatives of the multiplier are polynomials in \(\xi\) times that phase, with coefficients bounded on each compact time interval. The product rule bounds every Schwartz seminorm of the product by finitely many input seminorms, uniformly on such an interval. Taylor's integral formula in time expresses the difference between the difference quotient and \(i|\xi|^2e^{it|\xi|^2}\widehat f\) as an integral of a second time derivative times a factor bounded by \(|h|/2\). The same product estimates on a slightly larger time interval show that the difference tends to zero in each Schwartz seminorm. Fourier inversion therefore gives
\[
\partial_tU_tf=-i\Delta U_tf,
\qquad (\partial_t+i\Delta)U_tf=0.
\]
The time derivative adds \(i|\xi|^2\); the transform of \(\Delta\) is \(-|\xi|^2\), which fixes this sign. Plancherel with the multiplier's modulus one gives \(\|U_tf\|_2=\|f\|_2\) for every real time.

**Solution 4.** Put \(M=\|f\|_p\), and split at \(\lambda>0\) into \(f_1=f1_{|f|>\lambda}\), \(f_2=f1_{|f|\leq\lambda}\). Pointwise inequalities give
\(\|f_1\|_1\leq\lambda^{1-p}M^p\) and
\(\|f_2\|_2\leq\lambda^{1-p/2}M^{p/2}\).
The transform agreement results identify the distributional sum with a bounded continuous function plus an \(L^2\) density. Cauchy--Schwarz on \(K\) and the exact Plancherel factor give
\[
\begin{gathered}
\|\widehat f\|_{L^1(K)}\leq|K|\lambda^{1-p}M^p
\\ {}+(2\pi)^{d/2}|K|^{1/2}\lambda^{1-p/2}M^{p/2}.
\end{gathered}
\]
For \(M>0\), choose
\(\lambda=M[|K|^{1/2}/(2\pi)^{d/2}]^{2/p}\).
The two terms become equal to
\((2\pi)^{d(1-1/p)}|K|^{1/p}M\), proving the bound. If \(M=0\), the assertion is immediate. The same density works on every compact set, so it defines a locally finite measure. Directly at the endpoints,
\(\|\widehat f\|_{L^1(K)}\leq|K|\|f\|_1\) for \(p=1\), and
\(\|\widehat f\|_{L^1(K)}\leq(2\pi)^{d/2}|K|^{1/2}\|f\|_2\) for \(p=2\). On a null compact set all these density integrals are zero.

**Solution 5.** The integrable damped input has transform
\[
\frac1{a+i\xi}-\frac1{a-i\xi}
=\frac{-2i\xi}{a^2+\xi^2}.
\]
The inputs converge to \(\operatorname{sgn}x\) on all Schwartz tests by domination. For a frequency test \(\phi\), subtract \(\phi(0)\chi(\xi)\), where \(\chi\) is even, compact smooth and one near zero. The odd damped kernel annihilates this subtracted constant part. The remaining numerator is \(O(|\xi|)\) near zero, so its product with \(|\xi|/(a^2+\xi^2)\) is uniformly bounded there. Away from zero it is bounded by an integrable Schwartz tail divided by \(|\xi|\), together with a compact term. Dominated convergence proves
\[
\mathcal F(\operatorname{sgn}x)=-2i\operatorname{pv}(1/\xi).
\]
To disprove a measure representation near zero, choose an even nonnegative cutoff \(\chi\), equal to one on \([-r,r]\) and supported in an arbitrarily small such neighborhood. Choose an odd smooth \(h\), with \(|h|\leq1\), equal to the sign outside \([-1,1]\), and \(s h(s)\geq0\). The tests \(\phi_\varepsilon(\xi)=\chi(\xi)h(\xi/\varepsilon)\) have fixed compact support and supremum at most one. For \(0<\varepsilon<r\),
\[
\langle\operatorname{pv}(1/\xi),\phi_\varepsilon\rangle
\geq2\log(r/\varepsilon)\longrightarrow\infty.
\]
The rest of the integrand is nonnegative. A locally finite complex measure would bound these pairings by its finite total variation on that fixed compact support, a contradiction. On any open set separated from zero the transform is the ordinary smooth density \(-2i/\xi\). Thus this explicit example proves a singularity at zero; Theorem B's Baire construction gives the stronger failure on every nonempty open set.

**Solution 6.** With \(z'=z/\sqrt\beta\), set
\[
\begin{gathered}
E_\beta(x,y,z)=\beta^{-1/2}E(x,y,z'),
\\ =\frac{e^{iz^2/(4\beta y)-i\pi\operatorname{sgn}y/4}}
{2\pi(x+iy)\sqrt{4\pi\beta|y|}},\qquad y\ne0.
\end{gathered}
\]
The fixed invertible scaling preserves local integrability and temperedness. The chain rule changes \(\beta\partial_z^2\) to \(\partial_{z'}^2\). Its source is
\(\beta^{-1/2}\delta(x)\delta(y)\delta(z/\sqrt\beta)
=\delta(x)\delta(y)\delta(z)\): testing in \(z\) contributes exactly \(\sqrt\beta\). The full identity follows by the same distributional change of variables, so it includes the singular plane.

In partial frequency coordinates the solution is
\(V_\beta(x,y,\tau)=k(x,y)e^{-i\beta y\tau^2}\).
It tends to \(k\otimes1\) strongly on Schwartz tests. Indeed
\[
|k(x,y)(e^{-i\beta y\tau^2}-1)|
\leq\frac{\beta}{2\pi}\tau^2,
\]
since \(|y|/\sqrt{x^2+y^2}\leq1\); the inequality holds almost everywhere. Its pairing error is at most \(\beta(2\pi)^{-1}\int\tau^2|\Phi(x,y,\tau)|dxdy d\tau\), uniformly \(O(\beta)\) on bounded Schwartz families. Partial inverse Fourier continuity preserves these bounded-family estimates and maps \(k\otimes1\) to \(k\otimes\delta_0\). This proves the strong limit and shows why the degenerate limiting source is concentrated in \(z\), rather than a three-dimensional function.

**Solution 7.** Differentiation is continuous on \(\mathcal S'\), and the constant coefficient operator commutes with it. Thus \(LT=\partial_zLE=\partial_z\delta_0\). On \(y\ne0\), differentiation of the smooth representative gives
\[
\begin{gathered}
T(x,y,z)=\frac{iz}{2y}E(x,y,z),
\\ |T|=\frac{|z|}{4\pi\sqrt{4\pi}}
\frac{|y|^{-3/2}}{\sqrt{x^2+y^2}}.
\end{gathered}
\]
Take any sufficiently small rectangular neighborhood of \((1,0,1)\); its \(x,z\) intervals are bounded away from zero. On its portion with \(0<y<\varepsilon\), this modulus is bounded below by a positive constant times \(y^{-3/2}\), whose integral is infinite. If a locally finite measure represented \(T\) on the neighborhood, Lemma 0.1 forces its restriction away from \(y=0\) to equal this smooth density, with variation equal to its absolute value. Its total variation on a compact subrectangle crossing the plane would then be at least these diverging density integrals, impossible. The original derivative is nevertheless defined by \(\langle T,\phi\rangle=-\int E\phi_z\), an absolutely convergent locally integrable pairing. Absolute integrability of the classical derivative itself is not required for that definition.

**Solution 8.** Fix \(R\) containing the support of \(g\). For \(x\) in a compact set the integration region \(s\in x-\operatorname{supp}g\) lies in one compact set; local integrability of \(E\) proves absolute convergence. Difference quotients for any derivative of \(g\) are bounded on that set by another derivative supremum. Dominated convergence, iterated, yields
\(\partial^\alpha w(x)=\int E(s)\partial^\alpha g(x-s)ds\), hence smoothness.

The proof of Theorem D gives a polynomial weight with
\(C_N=\int |E(s)|(1+|s|)^{-N}ds<\infty\)
for some fixed \(N\). For example its product of separate quadratic weights is integrable, and taking \(N=6\) bounds a radial weight by that product up to a fixed constant. On the integration region, \(|s|\leq|x|+R\). Consequently
\[
|\partial^\alpha w(x)|
\leq C_N(1+|x|+R)^N\|\partial^\alpha g\|_\infty.
\]
Every derivative thus has polynomial growth and in particular \(w\) is tempered. For a compact test \(\phi\), Fubini in \(s,x\) is absolute because both its support and the translated support of \(g\) confine \(s\) to one compact set and bound all other factors. Write \(x=s+r\) and transfer the derivatives on the test in the weak calculation:
\[
\begin{gathered}
\langle Lw,\phi\rangle
=\int g(r)\langle LE,\phi(\cdot+r)\rangle dr
\\ =\int g(r)\phi(r)dr.
\end{gathered}
\]
Here the first-order terms have the negative signs and the second-order term the positive sign specified by distributional differentiation; these are precisely those in \(\langle LE,\phi(\cdot+r)\rangle\). Thus \(Lw=g\) on all tests. The proof supplies smoothness and polynomial growth; it supplies no compact-support or decay assertion for \(w\).

**Solution 9.** The complete (M2) remains Schwartz at each time, so its derivatives and all the following integrals are ordinary absolutely convergent calculations. Write \(u=U_tg\) and \(r=x-m+2tp\). Logarithmic differentiation gives
\[
\begin{gathered}
\frac{\nabla u}{u}=ip-\frac{2br}{1-4ibt},\\
J_t(x)=\rho_t(x)\\
{}\cdot\left(-2p+\frac{16b^2t}{A}r\right).
\end{gathered}
\tag{M7}
\]
The imaginary part of \(1/(1-4ibt)=(1+4ibt)/A\) is \(4bt/A\), so the sign and the factor \(16b^2t/A\) are fixed. The evolution proved in Solution 3 is \(\partial_tu=-i\Delta u\). Consequently
\(\partial_t|u|^2=2\operatorname{Im}(\overline u\Delta u)\).
The divergence of \(\operatorname{Im}(\overline u\nabla u)\) is the same imaginary part, since \(\nabla\overline u\cdot\nabla u\) is real. Thus
\(\partial_t\rho_t+\operatorname{div}J_t=0\).
This computation also checks that the current uses the negative sign in its definition.

Translation to \(r\), followed by \(r=\sqrt A\,s\), shows that every centered first moment vanishes. A mixed moment \(r_jr_k\), \(j\ne k\), is odd in one coordinate and has zero integral. The one-coordinate integration by parts in (M3) gives
\[
\begin{gathered}
\int x\,\rho_t(x)dx=m-2tp,\\
\int r_jr_k\rho_t(x)dx=\frac{A}{4b}\delta_{jk},\\
\int\overline u(-i\nabla u)dx=p,\\
\int J_t(x)dx=-2p.
\end{gathered}
\tag{M8}
\]
For the momentum formula, multiply the first line of (M7) by \(-i\rho_t\); its \(r\) term integrates to zero and its constant term is \(p\int\rho_t=p\). The current formula then gives its displayed integral directly. The derivative of the mean position is exactly \(-2p\), agreeing with the integrated continuity equation. This sign belongs to the \(e^{+it|\xi|^2}\) convention; the Gaussian width and the conserved unit energy hold for both signs of time.

**Solution 10.** Select \(f,\psi\) in the proof of Theorem B, so
\(\beta_0=\int\psi|\widehat f|>0\), and put \(S=\|\psi\|_\infty>0\).
For \(2<p<\infty\), define
\[
\begin{gathered}
\gamma_p=d(1/2-1/p)>0,\\
D=(4\pi)^{-d/2}\|f\|_1,\\
C_p=D^{1-2/p}\|f\|_2^{2/p}.
\end{gathered}
\tag{M9}
\]
Theorem B's supremum and square-integral bounds give
\(\|f_t\|_p\leq C_pt^{-\gamma_p}\), by taking the \(p\)-th root of (B3). For \(p=\infty\), set
\(\gamma_\infty=d/2\), \(C_\infty=D\), and use (B1).
All constants are positive because \(f\) is nonzero. Fourier injectivity makes \(f_t\ne0\), so define \(v_t=f_t/\|f_t\|_p\). The same compact tests as in Theorem B satisfy
\[
\begin{gathered}
\|v_t\|_p=1,\quad \|\phi_t\|_\infty=S,\\
\langle\widehat v_t,\phi_t\rangle
=\frac{\beta_0}{\|f_t\|_p}\\
\geq\frac{\beta_0}{C_p}t^{\gamma_p}>0.
\end{gathered}
\tag{M10}
\]
Every support is in the fixed interior of \(Q\); no enlargement of the frequency region is used.

Choose \(t>0\) so that
\[
t>\left(\frac{2NSC_p}{r\beta_0}\right)^{1/\gamma_p}.
\tag{M11}
\]
Let \(z_t=\langle\widehat{g_0},\phi_t\rangle\), which exists by Hölder with the Schwartz transform of the test, including the \(L^\infty\)-\(L^1\) endpoint. If \(z_t\ne0\), set \(\lambda_t=z_t/|z_t|\); if \(z_t=0\), set \(\lambda_t=1\). Put \(h=(r/2)\lambda_tv_t\). Then \(\|h\|_p=r/2<r\). The two terms in
\(\langle\widehat{g_0+h},\phi_t\rangle=z_t+(r/2)\lambda_t\langle\widehat v_t,\phi_t\rangle\)
have the same complex direction, or the first is zero. Hence its modulus is at least
\((r\beta_0/(2C_p))t^{\gamma_p}>NS=N\|\phi_t\|_\infty\).
Thus every input ball contains a point violating the proposed order-zero bound on that fixed frequency ball. Theorem B separately proves that each bound set is closed, that rational balls and integer bounds are countable, and that \(L^p\) is complete. Its full Baire step then yields failure of measure representation on every nonempty open region. The quantitative construction supplies the empty-interior step for both finite \(p>2\) and \(p=\infty\).

**Solution 11.** The absolute value of \(V_{\beta,a}\) is at most \(|k|\), and the weighted integrability proved in Theorem D makes it tempered for every real \(\beta\) and \(a\geq0\). Its exact mixed equation is
\[
\begin{gathered}
(\partial_x+i\partial_y-\beta\tau^2)V_{\beta,a}\\
=\delta_{(0,0)}(x,y)\otimes e^{-a\tau^2}.
\end{gathered}
\tag{M12}
\]
The derivative of \(e^{-i\beta y\tau^2}\) cancels the multiplier; the exponential has value \(e^{-a\tau^2}\) at \(x=y=0\). The \(a\) factor is independent of these derivatives. The full partial inverse map therefore gives
\(L_\beta E_{\beta,a}=\delta_{(0,0)}\otimes r_a\) for \(a>0\), and
\(L_\beta E_{\beta,0}=\delta_{(0,0,0)}\).

For \(a>0\), the absolutely convergent Gaussian inverse is
\[
\begin{gathered}
E_{\beta,a}(x,y,z)\\
=k(x,y)(4\pi)^{-1/2}\\
{}\cdot(a+i\beta y)^{-1/2}\\
{}\cdot e^{-z^2/[4(a+i\beta y)]}.
\end{gathered}
\tag{M13}
\]
Its root is continued from the positive real axis. Absolute Fubini with a Schwartz test is justified exactly as in (D4): the damped frequency has finite mass and the remaining \(k\) factor is integrable with test weights.

For fixed \(\beta\ne0\), let \(a\downarrow0\). The common majorant is a constant depending on \(\beta\) times
\(|y|^{-1/2}/\sqrt{x^2+y^2}\), independent of \(z\). The corner and global weighted integrability arguments of Theorem D apply unchanged. Weighted dominated convergence on bounded test families identifies the entire strong limit with
\[
\begin{gathered}
E_{\beta,0}(x,y,z)\\
=\frac{e^{iz^2/(4\beta y)-i\pi\operatorname{sgn}(\beta y)/4}}
{2\pi(x+iy)\sqrt{4\pi|\beta y|}},\\
y\ne0.
\end{gathered}
\tag{M14}
\]
Both signs of \(\beta\) are included by the actual root boundary; no positive scaling formula is used for negative \(\beta\). The identity from (M12) proves its full point source across the plane.

When \(\beta=0\), the mixed expression is \(k\otimes e^{-a\tau^2}\), so
\(E_{0,a}=k\otimes r_a\) for \(a>0\), and \(E_{0,0}=k\otimes\delta_0\) by scalar inversion. Finally
\[
\begin{gathered}
|V_{\beta,a}-k\otimes1|\\
\leq \tau^2\left(a|k|+\frac{|\beta|}{2\pi}\right).
\end{gathered}
\tag{M15}
\]
To prove it, split \(e^{-a\tau^2-i\beta y\tau^2}-1\) into the damping difference and the oscillatory difference. Use
\(1-e^{-a\tau^2}\leq a\tau^2\),
\(|e^{-i\beta y\tau^2}-1|\leq|\beta y|\tau^2\), and
\(|yk|\leq(2\pi)^{-1}\).
For a bounded Schwartz family \(\mathcal B\), both
\(\int\tau^2|k\Phi|\) and \(\int\tau^2|\Phi|\) are uniformly finite, by sufficiently high separate weights and the local integrability of \(k\). Thus the pairing error is \(O_{\mathcal B}(a+|\beta|)\). The exact continuous partial inverse sends a bounded family to a bounded family and sends \(k\otimes1\) to \(k\otimes\delta_0\). This proves the same strong joint estimate for the physical distributions.

For completeness, at fixed \(a>0\) the estimate for changing only \(\beta\) is \(O_{\mathcal B}(|\beta|)\), so \(E_{\beta,a}\to k\otimes r_a\). At fixed nonzero \(\beta\), the preceding weighted Gaussian limit gives \(E_{\beta,a}\to E_{\beta,0}\); the joint estimate at \(a=0\) then gives \(E_{\beta,0}\to k\otimes\delta_0\) from either sign. Also \(k\otimes r_a\to k\otimes\delta_0\), either by the joint estimate at \(\beta=0\) or by (M6) on the partial tests. Hence both iterated limits and every joint path agree. The regularized source tends strongly to the three-dimensional delta, while the limiting solution is \(k\otimes\delta_0\); its first-order Cauchy operator supplies that source.

## References

- The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; Fourier-Laplace slices and boundary poles, Lemma 0.1; and [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and (G2): exact Schwartz, completed-square-integral and partial transforms, including their strong transposes.
- The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16; [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), §6; and [measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), Theorem M and (M10)–(M12): complete \(L^p\) spaces, Baire, integration and complex Radon measures.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.6.2 and 7.6.4, p. 392, and answers, p. 416. This lesson gives independent full proofs and original graded problems; the local-measure argument directly proves the Baire obstruction without invoking a closed-graph theorem or an interpolation theorem.
- Terence Tao, [*247B, Notes 1: Restriction theory*](https://terrytao.wordpress.com/2020/03/29/247b-notes-1-restriction-theory/), March 2020, Proposition 3 and its provided proof, including Lemma 4. This compares the global Fourier norm range. The source uses \(e^{-2\pi ix\cdot\xi}\); its transform at \(\xi/(2\pi)\) equals the transform used here. Its random-sign argument is not needed for the local-measure theorem proved above.
