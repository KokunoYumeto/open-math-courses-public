# Boundary powers and angular Fourier spectra

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied programme foundations retain their stated licences.*

Parabolic boundary powers have spectra in a half-plane. Continuing their exponent through zero turns an ordinary density into derivatives of a point mass. Circular complex poles and trace-free spherical principal values instead have regular angular transforms. In each case the defining limit fixes the distribution at the singular set before its Fourier transform is computed.

Pairings are complex bilinear and \(FT(\phi)=T(F\phi)\), where \(F\phi(\xi)=\int e^{-ix\cdot\xi}\phi(x)\,dx\). The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz topology, compact-test density, Gaussian constant, inversion and all coordinate rules. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12 and 13.1–13.5, 13.7–13.10, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1, 15.6 and 16, supply calculus, bumps, convergence, Fubini and changes of variables. The [Gamma foundation](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e, supplies the entire reciprocal \(G=1/\Gamma\), its product, zeros and their exact derivatives.

We use the exact earlier proofs in [U048, Theorem 1.1](tempered-tensors-and-stationary-gaussian-equations.md) for tempered tensors; [U053, Lemma 1.1 and Theorem 2.1](complex-quadratic-powers-and-the-cauchy-kernel.md) for complex Laplace integration and the full Cauchy transform; [U029, Theorem 2.1](curved-cauchy-kernels-and-complex-pole-cutoffs.md) for circular cutoffs and their derivative normalization; and [U034, Theorem 4.1](compact-forcing-moments-and-positive-error-kernels.md), with the Newton Hessian proved in [U028, Solution 8](radial-sources-and-quadratic-logarithms.md), for spherical principal values. The full Coulomb transform is [U051, Theorem 1.1](radial-powers-and-the-logarithmic-endpoint.md). Measurable polar integration is proved in [the angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4; the latitude area calculation is [U035, Theorem 1.1, first proof paragraph](spherical-convolution-and-support-control.md). No external citation replaces these programme proofs.

Write \(p_m(\phi)=\max_{|\beta|\le m}\sup_X(1+|X|)^m|\partial^\beta\phi(X)|\). A bounded Schwartz set has a common bound for each \(p_m\). Strong convergence below means uniform convergence of pairings on every such set. Fixed differentiation, polynomial multiplication and invertible linear changes preserve bounded Schwartz sets, by their finite product and chain rules; their transposes therefore preserve strong convergence.

## A parabolic boundary value has a Gaussian half-plane spectrum

For an integer \(N\ge1\) and \(\epsilon>0\), put
\(U_{N,\epsilon}(x,y)=(x^2+\epsilon+iy)^{-N}\).

**Theorem 1.1.** These functions converge strongly in \(\mathcal S'(\mathbb R^2)\) to \(U_N\). Their compact-test limits agree with this distribution. Its exact order is \(N-1\), its singular support is \(\{0\}\), and
\[
(\partial_x+2ix\partial_y)U_N=0.
\tag{1.1}
\]
Its entire transform is the regular tempered distribution
\[
FU_N(\xi,\eta)=\frac{2\pi^{3/2}}{(N-1)!}
\begin{cases}
(-\eta)^{N-3/2}e^{\xi^2/(4\eta)},&\eta<0,\\
0,&\eta\ge0.
\end{cases}
\tag{1.2}
\]
Here the displayed choice on the line \(\eta=0\) does not change the regular distribution.

**Proof: the physical limit and exact order.** Set \(p=x^2+iy\) and \(\rho=|p|=(x^4+y^2)^{1/2}\). The set \(\rho\le r\) lies in the box \(|x|\le\sqrt r,\ |y|\le r\), of area \(4r^{3/2}\). On \(2^{-j-1}<\rho\le2^{-j}\), the integral of \(\rho^{-b}\) is bounded by \(C_b2^{-j(3/2-b)}\). Thus it is integrable at zero for \(b<3/2\), also after multiplication by any fixed power of \(|\log\rho|\). Outside a radius-two disk, either \(|y|\ge |(x,y)|/\sqrt2\) or \(|x|\ge |(x,y)|/\sqrt2\), so \(\rho\ge c|(x,y)|\). Consequently \(1/p\), with any value at zero, is locally integrable and has an integrable weighted absolute value at infinity.

The inequality \(|p+\epsilon|\ge|p|\) gives \(|U_{1,\epsilon}|\le1/\rho\). Weighted dominated convergence proves
\(\int (1+|(x,y)|)^{-m}|U_{1,\epsilon}-p^{-1}|\,dx\,dy\to0\)
for a sufficiently large fixed \(m\). Multiplying this integral by the common \(p_m\) bound proves strong convergence. Ordinary differentiation gives
\[
U_{N,\epsilon}
=\frac{i^{N-1}}{(N-1)!}\partial_y^{N-1}U_{1,\epsilon}.
\tag{1.3}
\]
The corresponding strong limit has order at most \(N-1\) on every compact set and equals \(p^{-N}\) off zero.

For the lower bound, let \(D_s(x,y)=(sx,s^2y)\), \(s>0\). Its determinant is \(s^3\). Changing variables in the regulated functions, then passing to the limit, gives \(U_N(D_s\cdot)=s^{-2N}U_N\). Take a nonzero nonnegative smooth bump \(\chi\) supported away from zero and set \(\psi=p^N\chi\). Then \(U_N(\psi)=\int\chi>0\). For \(\psi_s=\psi\circ D_s^{-1}\),
\[
U_N(\psi_s)=s^{3-2N}U_N(\psi),\qquad
\|\psi_s\|_{C^k}\le C_{\psi,k}s^{-2k}\quad(0<s\le1).
\]
The supports shrink into any fixed neighborhood of zero. Order \(k\) there would force \(3-2N+2k\ge0\); its integer consequence is \(k\ge N-1\). A smooth representative near zero is also impossible: equality of smooth functions as distributions on the punctured neighborhood gives equality pointwise, whereas \(p^{-N}(x,0)=x^{-2N}\) is unbounded. Pointwise uniqueness follows by testing a continuous nonzero difference against a sufficiently small bump. Thus the singular support is exactly \(\{0\}\). Direct differentiation proves (1.1) on each regulator and the continuous operations pass it to the limit.

**Proof: the whole transform.** The complete Laplace identity in U053 gives
\[
U_{N,\epsilon}(x,y)=\frac1{(N-1)!}
\int_0^\infty t^{N-1}e^{-tx^2-\epsilon t-ity}\,dt.
\tag{1.4}
\]
Its insertion into \(U_{N,\epsilon}(F\phi)\) is absolutely valid. For \(0<t<1\), use \(t^{N-1}\|F\phi\|_1\). For \(t\ge1\), a Schwartz bound of the form \(C_\phi(1+|y|)^{-2}\), followed by Gaussian integration in \(x\), gives \(C_\phi t^{N-3/2}e^{-\epsilon t}\). Both bounds are integrable.

Fourier foundation F3 and the full tensor theorem give
\[
F(e^{-tx^2}\otimes e^{-ity})
=\sqrt{\pi/t}\,e^{-\xi^2/(4t)}\otimes2\pi\delta_{-t}(\eta).
\tag{1.5}
\]
The second factor follows from inversion:
\(\int e^{-ity}F\theta(y)\,dy=2\pi\theta(-t)\).
Thus, with the joint Schwartz test,
\[
\begin{aligned}
J_t(\phi)&=\int_{\mathbb R}e^{-\xi^2/(4t)}\phi(\xi,-t)\,d\xi,\\
FU_{N,\epsilon}(\phi)
&=\frac{2\pi^{3/2}}{(N-1)!}
\int_0^\infty t^{N-3/2}e^{-\epsilon t}J_t(\phi)\,dt.
\end{aligned}
\tag{1.6}
\]
For an integer \(m>N\),
\[
\int e^{-\xi^2/(4t)}|\phi(\xi,-t)|\,d\xi
\le2\sqrt{\pi t}\,p_m(\phi)(1+t)^{-m}.
\tag{1.7}
\]
Hence the absolute pairing has a finite bound by a constant times
\(p_m(\phi)\int_0^\infty t^{N-1}(1+t)^{-m}\,dt\).
The same Gaussian estimate restricted to a bounded \(t\)-interval proves local integrability at the frequency boundary. It also proves temperedness globally. Removing the regulator changes the bound by the factor \(1-e^{-\epsilon t}\); dominated convergence makes its integral tend to zero uniformly on bounded Schwartz sets. Since Fourier transformation is continuous on those sets, this limit equals \(FU_N\) and is precisely (1.2) on every Schwartz test. \(\square\)

## Vary the exponent before taking the boundary

For \(\alpha\in\mathbb C\) set
\[
U_{\alpha,\epsilon}
=\exp[-\alpha\operatorname{Log}(p+\epsilon)].
\tag{P1}
\]
The logarithm is the right-half-plane branch proved in [U017, H0–H1](complex-powers-at-a-boundary.md). At nonzero boundary points its argument belongs to \([-\pi/2,\pi/2]\).

**Theorem 1.2 (all complex parabolic powers).** The strong limit \(U_\alpha=\lim_{\epsilon\downarrow0}U_{\alpha,\epsilon}\) exists for every \(\alpha\). It is entire, with locally uniform convergence and convergence of all fixed parameter derivatives, uniformly on bounded Schwartz sets. Its punctured density \(p^{-\alpha}\) is locally integrable through zero exactly for \(\operatorname{Re}\alpha<3/2\); there it represents the entire distribution. The complete identities are
\[
\begin{gathered}
\partial_yU_\alpha=-i\alpha U_{\alpha+1},\qquad
\partial_xU_\alpha=-2\alpha xU_{\alpha+1},\\
(\partial_x+2ix\partial_y)U_\alpha=0,\\
U_\alpha(sx,s^2y)=s^{-2\alpha}U_\alpha(x,y)\quad(s>0).
\end{gathered}
\tag{P2}
\]
For \(\operatorname{Re}\alpha>0\), its entire Fourier transform is the regular distribution
\[
FU_\alpha(\xi,-t)
=2\pi^{3/2}G(\alpha)t^{\alpha-3/2}e^{-\xi^2/(4t)}
\quad(t>0),\qquad
FU_\alpha(\xi,\eta)=0\quad(\eta>0).
\tag{P3}
\]

For a general parameter the formula uses a heat average:
\[
\begin{aligned}
\mathcal H_\phi(t)
&=\int_{\mathbb R}\frac{e^{-\xi^2/(4t)}}{\sqrt{4\pi t}}
              \phi(\xi,-t)\,d\xi\quad(t>0),\\
\mathcal H_\phi(0)&=\phi(0,0),\qquad
L=\partial_\xi^2-\partial_\eta .
\end{aligned}
\tag{P4}
\]
This function is smooth on \([0,\infty)\), rapidly decreasing with every derivative, and satisfies
\[
\mathcal H_\phi^{(j)}(0)=L^j\phi(0,0).
\tag{P5}
\]
For any integer \(M\ge1\) with \(\operatorname{Re}\alpha>-M\),
\[
\begin{aligned}
FU_\alpha(\phi)=4\pi^2G(\alpha)\bigg[
&\int_0^1t^{\alpha-1}
\left(\mathcal H_\phi(t)-\sum_{j=0}^{M-1}
       \frac{t^j}{j!}L^j\phi(0,0)\right)dt\\
&+\int_1^\infty t^{\alpha-1}\mathcal H_\phi(t)\,dt
+\sum_{j=0}^{M-1}\frac{L^j\phi(0,0)}{j!(\alpha+j)}
\bigg].
\end{aligned}
\tag{P6}
\]
The apparent poles are removed after multiplication by \(G\). The result is independent of \(M\). At every integer \(k\ge0\),
\[
U_{-k}=p^k,\qquad
FU_{-k}=(2\pi)^2(-\partial_\xi^2-\partial_\eta)^k\delta_{(0,0)}.
\tag{P7}
\]
This uses the same normalization as [U022, (1.3)–(1.5)](causal-integration-of-complex-order.md); the argument below proves its action on this noncompact heat average, including all endpoints.

**Proof: physical integrability and the entire family.** The shell estimate in Theorem 1.1 proves sufficiency of \(\operatorname{Re}\alpha<3/2\). For necessity use disjoint boxes
\[
2^{-(j+1)/2}<x<2^{-j/2},\qquad |y|<2^{-j}.
\]
Their areas are \(c\,2^{-3j/2}\), and on them \(2^{-j-1}<\rho<\sqrt2\,2^{-j}\). Thus \(\int\rho^{-b}\) diverges for \(b\ge3/2\). The modulus of the argument factor in \(p^{-\alpha}\) is between \(e^{-|\operatorname{Im}\alpha|\pi/2}\) and \(e^{|\operatorname{Im}\alpha|\pi/2}\), so the same threshold is exact for complex powers.

Fix a compact parameter set in \(\operatorname{Re}\alpha<3/2\), and choose \(0<b<3/2\) strictly larger than its real parts. On \(\rho<1\) and \(0<\epsilon\le1\), \(\rho\le|p+\epsilon|\le2\). The functions and their \(j\)-th parameter derivatives are therefore bounded by
\[
C_j(1+\rho^{-b})(1+|\log\rho|^j).
\]
On the complement, the parameter set's lower real-part bound and \(|p+\epsilon|\le C(1+|(x,y)|)^2\) give a fixed polynomial times a logarithmic power. A sufficiently large Schwartz weight makes it integrable. At each nonzero point the functions and derivatives converge uniformly on that parameter set. Taking the supremum in the parameter first and applying dominated convergence proves locally uniform strong convergence for every fixed derivative.

Here the claim of entire dependence includes actual strong power series. Around a parameter in this region choose \(\delta>0\) so that increasing the real-part bound by \(2\delta\) still leaves it below \(3/2\). Expand
\(e^{-h\operatorname{Log}(p+\epsilon)}\).
The sum of absolute values at \(|h|\le\delta\) is at most \(e^{\delta|\operatorname{Log}(p+\epsilon)|}\), covered by the preceding slightly enlarged integrable bound. On \(|h|\le\delta/2\), the tail after degree \(m\) is bounded by \(2^{-m}\) times that same envelope. Integration proves convergence of the series in every bounded-test seminorm, both before and after the limit. This also justifies all parameter derivatives without a weak-to-strong inference.

For a parameter \(\alpha_0\) with real part at least \(3/2\), choose an integer \(n\ge1\) such that \(1/2\le\operatorname{Re}(\alpha_0-n)<3/2\). On a sufficiently small disk the shifted parameters lie in the regular region and \(Q_n(\alpha)=\prod_{j=1}^n(\alpha-j)\) never vanishes, because \(\operatorname{Re}\alpha_0\ge n+1/2\). Differentiating ordinary functions gives
\[
U_{\alpha,\epsilon}
=\frac{i^n}{Q_n(\alpha)}\partial_y^nU_{\alpha-n,\epsilon}.
\tag{P8}
\]
The proved strong limit and its power series pass through this continuous derivative and the holomorphic reciprocal polynomial. These disks cover the remaining plane. Their limits agree on overlaps because they come from the same regulated family. A compact parameter set has a finite disk cover, proving the stated uniformity. The punctured limit is \(p^{-\alpha}\); the divergence just proved excludes any locally integrable representative outside the regular region. Finally (P2) follows by differentiating or scaling each regulated function, with \(\epsilon\) replaced by \(\epsilon/s^2\) in the dilation, and then taking the strong limits.

**Proof: the spectrum in the positive half-plane.** For \(\operatorname{Re}\alpha>0\), U053's complete scalar proof gives
\[
U_{\alpha,\epsilon}(x,y)
=G(\alpha)\int_0^\infty
t^{\alpha-1}e^{-tx^2-\epsilon t-ity}\,dt.
\tag{P9}
\]
For fixed \(\epsilon\), the physical absolute interchange uses
\(t^{\operatorname{Re}\alpha-1}\|F\phi\|_1\) at zero and
\(C_\phi t^{\operatorname{Re}\alpha-3/2}e^{-\epsilon t}\) at infinity. Formula (1.5) consequently applies inside the pairing. The frequency Gaussian has mass \(2\sqrt{\pi t}\); the absolute remaining integral is bounded by \(C p_m(\phi)\int t^{\operatorname{Re}\alpha-1}(1+t)^{-m}\,dt\), with \(m>\operatorname{Re}\alpha\). On a compact positive-half-plane parameter set, choose a common positive lower real part and a common such \(m\). Powers of \(|\log t|\) retain integrability. These bounds prove local integrability, temperedness, regulator removal and every parameter derivative uniformly as asserted, and identify (P3) on all tests.

**Proof: the heat average and continuation.** Put \(g_t(\xi)=e^{-\xi^2/(4t)}/\sqrt{4\pi t}\). Direct differentiation gives \(\partial_tg_t=\partial_\xi^2g_t\). On a compact positive \(t\)-interval every derivative has a polynomial Gaussian majorant. Twice integrating by parts in \(\xi\) has vanishing Gaussian endpoints. Iteration therefore gives
\[
\mathcal H_\phi^{(j)}(t)
=\int_{\mathbb R}g_t(\xi)(L^j\phi)(\xi,-t)\,d\xi
\quad(t>0).
\tag{P10}
\]
The Gaussian has mass one. After \(\xi=\sqrt t\,z\), its weight is fixed. The segment fundamental theorem bounds
\[
|L^j\phi(\sqrt t\,z,-t)-L^j\phi(0,0)|
\le C_jp_{2j+1}(\phi)(\sqrt t\,|z|+t)
\quad(0<t\le1).
\]
Both Gaussian moments on the right are finite. Thus the endpoint limits in (P5) are uniform on bounded test sets. Integrate the \((j+1)\)-st identity from a positive lower endpoint, then let that endpoint tend to zero; this proves that the extensions are successive derivatives on the closed half-line. For every \(K,j\) the same mass-one integral gives
\[
(1+t)^K|\mathcal H_\phi^{(j)}(t)|
\le C_{K,j}p_{K+2j}(\phi).
\]
This proves all the smoothness, decay and seminorm assertions.

Rewriting the positive-half-plane formula now gives
\[
FU_\alpha(\phi)
=4\pi^2G(\alpha)\int_0^\infty
t^{\alpha-1}\mathcal H_\phi(t)\,dt
\quad(\operatorname{Re}\alpha>0).
\tag{P11}
\]
Repeated fundamental theorem on \([0,t]\) gives the exact remainder
\[
\mathcal H_\phi(t)-\sum_{j=0}^{M-1}\frac{t^j}{j!}\mathcal H_\phi^{(j)}(0)
=\frac{t^M}{(M-1)!}\int_0^1(1-s)^{M-1}\mathcal H_\phi^{(M)}(st)\,ds .
\]
It is bounded by \(C_Mp_{2M}(\phi)t^M\). Subtracting these monomials in (P11) and integrating them explicitly yields (P6). For \(\operatorname{Re}\alpha>-M\), the remainder and its parameter derivatives have integrable bounds \(Ct^{\operatorname{Re}\alpha+M-1}|\log t|^l\) near zero. The tail has arbitrarily rapid decay. The same parameter-segment difference quotient as G2, or its exponential power-series estimate, proves holomorphy and all strong bounds for these integrals.

The only displayed poles are simple poles at \(-j\). W4e proves \(G'(-j)=(-1)^j j!\), so their products with \(G\) are holomorphic, with the removable values fixed exactly. Increasing \(M\) by one changes the bracket by the negative of the added monomial integral plus its elementary integral \(1/(\alpha+M)\); these cancel wherever both integrals converge. Thus the formulas agree directly on overlaps. They form an entire family and coincide with the already proved physical Fourier family in \(\operatorname{Re}\alpha>0\). The one-variable identity theorem supplied through U017 H1, applied to each test on each connected half-plane, proves equality everywhere. At \(-k\) only the removed \(j=k\) pole survives, giving \(4\pi^2(-1)^kL^k\phi(0,0)\), precisely the pairing in (P7). Independently, the regulated polynomial \((p+\epsilon)^k\) tends strongly to \(p^k\). \(\square\)

## Circular Cauchy poles have regular angular spectra

The circular prescription is
\[
u_N(\phi)=\lim_{\epsilon\downarrow0}
\int_{x^2+y^2>\epsilon}(x+iy)^{-N}\phi(x,y)\,dx\,dy .
\]
U029, Theorem 2.1, proves the exact order \(N-1\), existence and dilation/rotation normalization, and
\[
u_N=\frac{(-1)^{N-1}}{(N-1)!}\partial_z^{N-1}k,
\qquad k=\frac1{x+iy},\qquad
\partial_z=\frac{\partial_x-i\partial_y}{2}.
\tag{2.1}
\]

**Theorem 2.1.** This normalized distribution is tempered and
\[
Fu_N(\xi,\eta)
=\frac{\pi\,2^{2-N}i^{-N}}{(N-1)!}
\frac{(\xi-i\eta)^{N-1}}{\xi+i\eta}
\tag{2.2}
\]
as a whole regular distribution.

**Proof.** The source \(k\) is locally integrable and tempered, and (2.1) therefore defines a tempered extension. It agrees with the original cutoff on Schwartz tests as well. For \(N\ge2\), subtract near zero a radial compact cutoff times the degree-\(N-2\) Taylor polynomial. Every subtracted monomial has angular frequency of magnitude at most \(N-2\); after multiplication by \(e^{-iN\theta}\) its angular integral is zero. The remainder is \(O(r^{N-1})\) with a fixed derivative bound, so \(r^{-N}\) times it is absolutely integrable in two dimensions. The unchanged tail is controlled by a Schwartz weight. At \(N=1\) the kernel itself is locally integrable. These are the actual cutoff limits, and uniqueness on Schwartz space follows also from compact-test density.

U053 proves \(Fk=-2\pi i/(\xi+i\eta)\) on the whole plane. The multiplier of \(\partial_z\) is \(i(\xi-i\eta)/2\), so (2.1) gives
\[
Fu_N=\frac{(-1)^{N-1}}{(N-1)!}
\left(\frac{i(\xi-i\eta)}2\right)^{N-1}
\frac{-2\pi i}{\xi+i\eta}.
\]
Its coefficient simplifies to that in (2.2). The absolute value is \(C_N|(\xi,\eta)|^{N-2}\), which is locally integrable also at \(N=1\) and has polynomial growth. Polynomial multiplication therefore preserves the whole regular distribution, including its normalization at the origin. \(\square\)

## A trace-free principal value becomes a bounded angular function

Let \(A=(a_{jk})\) be a symmetric complex \(3\)-by-\(3\) matrix. The spherical cutoff of \(x^TAx/|x|^5\) exists exactly when \(\operatorname{tr}A=0\), by U034, Theorem 4.1. For this case denote it by \(F_A\). Its exact identity is
\[
F_A=-\frac{4\pi}{3}\sum_{j,k}a_{jk}\partial_j\partial_k\Phi_3,
\qquad \Phi_3=-\frac1{4\pi|x|}.
\tag{3.1}
\]
Indeed the full Hessian proof in U028, Solution 8, gives
\[
\partial_j\partial_k\Phi_3
=\operatorname{pv}\frac{\delta_{jk}|x|^2-3x_jx_k}{4\pi|x|^5}
+\frac{\delta_{jk}}3\delta_0.
\]
Both trace terms vanish upon trace-free contraction. The sphere integral of \(x^TAx/|x|^2\) is \(4\pi\operatorname{tr}A/3\). A nonzero trace consequently gives a divergent logarithm against a test equal to one near zero; a zero trace permits subtraction of that test value with integrable \(O(r)\) remainder.

**Theorem 3.1.** The normalized \(F_A\) is tempered and has entire transform
\[
FF_A(\xi)=-\frac{4\pi}{3}\frac{\xi^TA\xi}{|\xi|^2}.
\tag{3.2}
\]
This is a bounded regular angular function; its value at zero is immaterial.

**Proof.** The spherical cutoff agrees with (3.1) also on Schwartz tests: near zero subtract \(\phi(0)\) inside a radial cutoff and use the zero angular mean; the absolute remainder is bounded radially by \(C_A\|\nabla\phi\|_\infty\,dr\). At infinity a Schwartz weight makes \(C_A|\phi|\,dr/r\) integrable. The complete U051 Coulomb formula gives \(F\Phi_3=-|\xi|^{-2}\), so the Fourier coordinate rule applied to (3.1) gives (3.2), with its full double sum. The quotient has absolute value at most \(\sum_{j,k}|a_{jk}|\), proving regularity and temperedness. The Hessian identity has already fixed the contact term, so the Fourier computation determines the distribution everywhere. \(\square\)

## Exercises

**Exercise 1 (foundation: change the parabolic scale).** For \(\alpha>0\), \(\beta\ge0\) and positive integral \(N\), find the whole transform of
\[
V_{N,\alpha,\beta}
=\lim_{\epsilon\downarrow0}
(\alpha x^2+\beta+\epsilon+iy)^{-N}.
\]
Prove existence of the indicated tempered limit, including \(\beta=0\).

**Exercise 2 (intermediate: shear the boundary).** For real \(c\), put \(W_N(x,y)=U_N(x,y+cx)\). Find its entire transform and its first-order homogeneous equation.

**Exercise 3 (intermediate: read the Gaussian frequency fibers).** For \(t>0\), integrate \(FU_N(\xi,-t)\) and \(\xi^2FU_N(\xi,-t)\) over the entire \(\xi\)-line. Identify the normalized fiber variance and the special case \(N=1\).

**Exercise 4 (advanced: recurrences and the spectral differential equation).** Prove both whole identities
\[
\begin{gathered}
\partial_yU_N=-iN U_{N+1},\\
\partial_xU_N=-2N xU_{N+1}.
\end{gathered}
\]
Check their implications and the parabolic equation directly in frequency variables.

**Exercise 5 (intermediate: the third circular pole and its contact source).** For the circularly cut \(u_3\), compute \(Fu_3\) and \(\bar\partial u_3\), where \(\bar\partial=(\partial_x+i\partial_y)/2\). Verify the contact source in frequency variables.

**Exercise 6 (intermediate: real angular components of a pole).** Determine the whole transforms of \(R=\operatorname{Re}u_2\) and \(J=\operatorname{Im}u_2\), with the real and imaginary parts defined by conjugation of the distribution. Identify their exact circularly cut physical densities.

**Exercise 7 (advanced: retain every off-diagonal coefficient).** Let
\[
A=\begin{pmatrix}1&2i&0\\2i&-1&3\\0&3&0\end{pmatrix}.
\]
Compute the whole spectrum and Laplacian source of its spherical principal value \(F_A\). Evaluate \((FF_A)(\xi_1\xi_2e^{-b|\xi|^2})\) for \(b>0\).

**Exercise 8 (advanced: a trace creates a point mass).** For an arbitrary constant symmetric complex matrix \(A\), with \(\tau=\operatorname{tr}A\), define the actual Hessian contraction
\[
T_A=-\frac{4\pi}{3}\sum_{j,k}a_{jk}\partial_j\partial_k\Phi_3.
\]
Express it through the trace-free spherical principal value, determine its entire transform, and interpret \(A=I\).

**Exercise 9 (intermediate: the endpoint is an origin jet).** Determine \(U_{-2}\) and its full transform from both the physical polynomial and the continued frequency formula (P6). Retain every mixed derivative and its sign. Evaluate this transform on \(\phi(\xi,\eta)=e^{-a\xi^2-b\eta^2}\), \(a,b>0\), and check the parabolic first-order equation. Explain why inserting \(1/\Gamma(-2)=0\) into the positive-half-plane density alone loses the answer.

**Exercise 10 (advanced: a parameter derivative fixes the logarithmic contact).** Let \(W=\left.\partial_\alpha U_\alpha\right|_{\alpha=0}\). Find its full regular physical distribution and its whole Fourier pairing in terms of \(\mathcal H_\phi\). Use the exact reciprocal-Gamma product to retain the origin contact coefficient. Prove its anisotropic scaling and Euler equation, and explain why that equation alone cannot determine the contact coefficient in the Fourier transform.

## Solutions

**Solution 1.** Keep the exercise's real parameter \(\alpha>0\) distinct from the complex exponent in Theorem 1.2. When \(\beta=0\), the change \((x,y)\mapsto(\sqrt\alpha x,y)\) transfers the established strong limit. When \(\beta>0\), the first power has a locally bounded limit and
\[
|(\alpha x^2+\beta+\epsilon+iy)^{-1}|
\le |(\alpha x^2+\beta+iy)^{-1}|.
\]
The right side has an integrable Schwartz-weighted absolute value. Weighted dominated convergence gives the strong first-power limit, and \(i^{N-1}\partial_y^{N-1}/(N-1)!\) gives all \(N\).

In the Laplace computation retain \(e^{-\beta t}\) and replace the Gaussian coefficient \(t\) by \(\alpha t\). On \(\eta=-t<0\) this gives
\[
FV_{N,\alpha,\beta}(\xi,-t)
=\frac{2\pi^{3/2}}{(N-1)!\sqrt\alpha}
t^{N-3/2}e^{-\beta t-\xi^2/(4\alpha t)},
\]
and zero on \(\eta>0\). The full Gaussian \(\xi\)-integral is \(2\sqrt{\pi\alpha t}\). Hence the absolute pairing after regulator removal is bounded by
\(C p_m(\phi)t^{N-1}(1+t)^{-m}\), \(m>N\), integrated in \(t\). This proves the entire regular transform, including the boundary, for every allowed \(\beta\).

**Solution 2.** For an invertible real \(B\), define \(B^*T(\psi)=|\det B|^{-1}T(\psi\circ B^{-1})\). The complete linear substitution formula and the Schwartz chain rule give
\[
F(B^*T)=|\det B|^{-1}(FT)\circ B^{-T}.
\]
To verify it on arbitrary tempered distributions, set \(\xi=B^T\zeta\) in the defining Fourier integral. The resulting test identity is
\(F\phi(B^{-1}u)=|\det B|F[\phi(B^T\cdot)](u)\).
Pairing this identity with \(T\) proves the formula with the distributional pullback definition. This also proves its continuity.

Here \(B=\begin{pmatrix}1&0\\c&1\end{pmatrix}\), so \(\det B=1\) and \(B^{-T}(\xi,\eta)=(\xi-c\eta,\eta)\). Therefore
\[
FW_N(\xi,\eta)=\frac{2\pi^{3/2}}{(N-1)!}
(-\eta)^{N-3/2}e^{(\xi-c\eta)^2/(4\eta)}
\quad(\eta<0),
\]
with zero density on the other half-plane. The chain rule on each regulator yields
\[
(\partial_x+(2ix-c)\partial_y)W_N=0:
\]
the \(\partial_x\) derivative contributes \(c\,\partial_yU_N\), which cancels the displayed \(-c\) term. Continuous pullback and differentiation pass this exact equation to the strong limit.

**Solution 3.** For \(t>0\), Fourier foundation F3 gives
\[
\int_{\mathbb R}e^{-\xi^2/(4t)}\,d\xi=2\sqrt{\pi t},
\qquad
\int_{\mathbb R}\xi^2e^{-\xi^2/(4t)}\,d\xi=4\sqrt\pi\,t^{3/2}.
\]
The second identity is minus the derivative of \(\sqrt{\pi/a}\) at \(a=1/(4t)\); on a compact positive \(a\)-interval its integrand is dominated by \(\xi^2e^{-d\xi^2}\), \(d>0\). Thus
\[
\int FU_N(\xi,-t)\,d\xi=\frac{4\pi^2t^{N-1}}{(N-1)!},
\qquad
\int \xi^2FU_N(\xi,-t)\,d\xi=\frac{8\pi^2t^N}{(N-1)!}.
\]
The normalized fiber has mean zero by symmetry and variance \(2t\). For \(N=1\) its unnormalized mass is the constant \(4\pi^2\). These convergent fiber integrals grow polynomially in \(t\), so their pairings with Schwartz functions of \(t\) converge absolutely.

**Solution 4.** The physical recurrences are (P2) at positive integers. To check the entire spectra directly, write \(q_N=FU_N\) and \(K_N=2\pi^{3/2}/(N-1)!\). On \(\eta=-t<0\),
\[
q_{N+1}=\frac tNq_N,\qquad
\partial_\xi q_N=\frac{\xi}{2\eta}q_N.
\]
There is no derivative across the \(\eta\) boundary here. For a direct justification that the ordinary \(\xi\)-derivative gives the whole distributional one, its absolute \(\xi\)-integral is \(2K_Nt^{N-3/2}\). This is integrable at zero for every \(N\ge1\), and a large Schwartz weight handles infinity. Integration by parts in \(\xi\), followed by absolute Fubini in \(t\), therefore proves the derivative identity globally. Multiplication by \(t\) or \(\eta\) also preserves these bounds.

It follows that \(i\eta q_N=-iNq_{N+1}\) and
\(-2Ni\partial_\xi q_{N+1}=i\xi q_N\).
These are precisely the transforms of the two requested recurrences. Finally,
\[
F[(\partial_x+2ix\partial_y)U_N]
=i(\xi q_N-2\eta\partial_\xi q_N)=0
\]
on every Schwartz test, including tests meeting the frequency boundary.

**Solution 5.** At \(N=3\), (2.2) gives
\[
Fu_3=\frac{\pi i}{4}\frac{(\xi-i\eta)^2}{\xi+i\eta}.
\]
The circular normalization says \(u_3=\tfrac12\partial_z^2k\). The full Cauchy source is \(\bar\partial k=\pi\delta_0\), as proved in U029; it is also verified by multiplying the full \(Fk\) by \(i(\xi+i\eta)/2\), obtaining the constant \(\pi=F(\pi\delta_0)\). Fourier injectivity follows from F4–F5. Thus
\[
\bar\partial u_3
=\frac{\pi}{2}\partial_z^2\delta_0
=\frac{\pi}{8}
(\partial_x^2-2i\partial_x\partial_y-\partial_y^2)\delta_0.
\]
Multiplying \(Fu_3\) by the \(\bar\partial\) multiplier gives
\(-\pi(\xi-i\eta)^2/8\), exactly the transform of this full second-order jet.

**Solution 6.** Conjugating the actual circular cut gives
\[
R=\operatorname{pv}\frac{x^2-y^2}{(x^2+y^2)^2},
\qquad
J=\operatorname{pv}\frac{-2xy}{(x^2+y^2)^2}.
\]
For \(\overline T(\phi)=\overline{T(\bar\phi)}\), conjugating the Fourier test integral gives \(F\overline T=\overline{FT(-\cdot)}\). Indeed \(\overline{F\phi}=F[\bar\phi(-\cdot)]\), and substitution into the pairing proves this for every tempered \(T\). Now
\[
Fu_2=-\pi\frac{\xi-i\eta}{\xi+i\eta}
=-\pi\frac{\xi^2-\eta^2-2i\xi\eta}{\xi^2+\eta^2}
\]
is even under full reflection. Its real and imaginary parts therefore give
\[
FR=-\pi\frac{\xi^2-\eta^2}{\xi^2+\eta^2},\qquad
FJ=2\pi\frac{\xi\eta}{\xi^2+\eta^2}.
\]
These are bounded regular distributions. The original cutoff has fixed their entire normalization.

**Solution 7.** The matrix is trace-free and
\(x^TAx=x_1^2-x_2^2+4ix_1x_2+6x_2x_3\).
The full double sum therefore gives
\[
FF_A(\xi)=-\frac{4\pi}{3}
\frac{\xi_1^2-\xi_2^2+4i\xi_1\xi_2+6\xi_2\xi_3}{|\xi|^2},
\]
\[
\Delta F_A=-\frac{4\pi}{3}
(\partial_1^2-\partial_2^2+4i\partial_1\partial_2
+6\partial_2\partial_3)\delta_0.
\]
The second identity follows by applying \(\Delta\) to (3.1) and using \(\Delta\Phi_3=\delta_0\), included in the supplied Hessian and point-source proofs.

In the requested Gaussian pairing, coordinate reflection makes every numerator term vanish except \(4i\xi_1\xi_2\). The latitude formula of U035 gives
\(\int_{S^2}\omega_1^4\,dS=2\pi\int_{-1}^1s^4\,ds=4\pi/5\).
Permutation invariance makes all three diagonal fourth moments equal and all three mixed squared moments equal, say to \(m\). Integrating
\((\omega_1^2+\omega_2^2+\omega_3^2)^2=1\) gives
\(3(4\pi/5)+6m=4\pi\), so \(m=4\pi/15\). This uses the actual latitude and symmetry proofs, without assuming a classification of invariant tensors.

Twice differentiating \(\int_0^\infty e^{-br^2}\,dr=\sqrt\pi/(2\sqrt b)\) gives \(\int_0^\infty r^4e^{-br^2}\,dr=3\sqrt\pi/(8b^{5/2})\); both derivatives have polynomial Gaussian majorants on positive compact parameter intervals. Polar integration yields
\[
\int_{\mathbb R^3}\frac{\xi_1^2\xi_2^2}{|\xi|^2}e^{-b|\xi|^2}\,d\xi
=\frac{4\pi}{15}\frac{3\sqrt\pi}{8b^{5/2}}
=\frac{\pi^{3/2}}{10b^{5/2}}.
\]
Multiplication by \(-16\pi i/3\) gives
\[
(FF_A)(\xi_1\xi_2e^{-b|\xi|^2})
=-\frac{8i\pi^{5/2}}{15b^{5/2}}.
\]
All parity and polar interchanges are absolute by boundedness of the angular multiplier and Gaussian decay.

**Solution 8.** Decompose \(A=A_0+\tau I/3\), where \(\operatorname{tr}A_0=0\). The exact Hessian contraction gives
\[
T_A=F_{A_0}-\frac{4\pi\tau}{9}\delta_0.
\]
Its punctured density is
\((x^TAx-\tau|x|^2/3)/|x|^5\); the raw spherical cutoff of the unmodified density would diverge when \(\tau\ne0\). Taking the transform of the defined contraction gives
\[
FT_A=-\frac{4\pi}{3}\frac{\xi^TA\xi}{|\xi|^2}
=-\frac{4\pi}{3}\frac{\xi^TA_0\xi}{|\xi|^2}
-\frac{4\pi\tau}{9}.
\]
At \(A=I\), the result is \(T_I=-4\pi\delta_0/3\) and \(FT_I=-4\pi/3\), although the punctured density is zero. As an additional whole-test check, sphere symmetry gives
\[
(FT_A)(e^{-b|\xi|^2})
=-\frac{4\pi\tau}{9}\left(\frac\pi b\right)^{3/2}.
\]
The trace-free part has zero angular mean; the answer is exactly the Fourier contact term paired with this Gaussian.

**Solution 9.** At the negative integer, the physical expression is the polynomial
\[
U_{-2}=(x^2+iy)^2=x^4+2ix^2y-y^2.
\tag{P12}
\]
The regulated polynomials have a fixed degree and coefficients converging to these coefficients. An integrable fixed Schwartz weight proves their strong convergence. Applying \(F1=(2\pi)^2\delta_0\), \(F(xT)=i\partial_\xi FT\) and \(F(yT)=i\partial_\eta FT\) gives
\[
FU_{-2}=(2\pi)^2
(\partial_\xi^4+2\partial_\xi^2\partial_\eta+\partial_\eta^2)\delta_0.
\tag{P13}
\]
For the independent continuation check, choose \(M>2\) in (P6). Since \(G'(-2)=2\), the \(j=2\) term has removable value \(L^2\phi(0,0)\); every other term vanishes. Thus
\[
FU_{-2}(\phi)=(2\pi)^2
[\partial_\xi^4\phi-2\partial_\xi^2\partial_\eta\phi
+\partial_\eta^2\phi](0,0).
\tag{P14}
\]
The minus sign on the mixed test derivative agrees with its total order three in (P13). On \(e^{-a\xi^2-b\eta^2}\) this equals
\((2\pi)^2(12a^2-2b)\), because the odd \(\eta\) derivative vanishes.

One can check this on the physical side as well:
\[
F\phi(x,y)=\frac{\pi}{\sqrt{ab}}\,
e^{-x^2/(4a)-y^2/(4b)}.
\]
Its total mass is \(4\pi^2\), its normalized fourth \(x\)-moment is \(12a^2\), and its normalized second \(y\)-moment is \(2b\). These follow from the first two derivatives of the scalar Gaussian mass, with the same majorants as in Solutions 3 and 7. Oddness kills \(2ix^2y\), reproducing the pairing.

Since \((\partial_x+2ix\partial_y)p=2x+2ix\,i=0\), its square satisfies the full parabolic equation. The coordinate Fourier identities give
\(i(\xi FU_{-2}-2\eta\partial_\xi FU_{-2})=0\).
The zero \(G(-2)\) cancels a pole before the parameter is evaluated; retaining only the positive-half-plane density would discard the entire nonzero point jet.

**Solution 10.** Strong parameter differentiation in the regular physical region gives
\[
W=-\operatorname{Log}(x^2+iy).
\tag{P15}
\]
The shell estimate makes its absolute value integrable near zero. At infinity \(\rho\) lies between \(c|(x,y)|\) and \(C(1+|(x,y)|)^2\), so the logarithm has at most logarithmic growth. Thus this is a whole regular tempered distribution.

The exact reciprocal product W4d, with \(\gamma=\lim_n(\sum_{j=1}^n1/j-\log n)\), gives
\[
G(\alpha)=\alpha+\gamma\alpha^2+O(\alpha^3).
\tag{P16}
\]
Indeed \(\log(1+\alpha/j)-\alpha/j=O(|\alpha|^2/j^2)\) uniformly on a small disk. The summable remainder makes the infinite product \(1+O(\alpha^2)\); multiplying by \(\alpha e^{\gamma\alpha}\) proves the coefficient.

Use \(M=1\) in (P6). The two convergent integrals are holomorphic near zero because \(\mathcal H_\phi(t)-\phi(0,0)=O(t)\) with a finite seminorm bound, and the tail decays rapidly. Differentiating their product with \(G\) and differentiating the removed pole \(G(\alpha)\phi(0,0)/\alpha\) gives
\[
\begin{aligned}
FW(\phi)=4\pi^2\bigg[
&\int_0^1\frac{\mathcal H_\phi(t)-\phi(0,0)}t\,dt\\
&+\int_1^\infty\frac{\mathcal H_\phi(t)}t\,dt
+\gamma\phi(0,0)\bigg].
\end{aligned}
\tag{P17}
\]
The contact coefficient relative to this subtraction at \(t=1\) is exactly \(4\pi^2\gamma\). Moving the subtraction endpoint moves a compensating constant between the integral and this term, leaving the whole pairing fixed.

Differentiate (P2) in \(\alpha\) at zero, using \(U_0=1\):
\[
W(sx,s^2y)=W(x,y)-2\log s.
\tag{P18}
\]
To differentiate this in \(s\), pair with \(\phi\) using
\(T(D_s\cdot)(\phi)=s^{-3}T(\phi\circ D_s^{-1})\).
At \(s=1\) the test derivative is \(-3\phi-x\partial_x\phi-2y\partial_y\phi\), exactly the transpose defining \((x\partial_x+2y\partial_y)T\). The test differentiation converges in every Schwartz seminorm by the chain rule and Taylor remainder on a compact interval of positive \(s\). Consequently
\[
(x\partial_x+2y\partial_y)W=-2.
\tag{P19}
\]
The coordinate rules \(F(x\partial_xT)=-(\xi\partial_\xi+1)FT\) and its \(y\) analogue give
\[
(\xi\partial_\xi+2\eta\partial_\eta+3)FW=8\pi^2\delta_0.
\tag{P20}
\]
On a test, \(\xi\partial_\xi\delta_0=-\delta_0\) and \(\eta\partial_\eta\delta_0=-\delta_0\), by the product rule at zero. Thus the operator on the left annihilates \(\delta_0\). This Euler equation leaves its coefficient undetermined; the complete Gamma-normalized family fixes it through (P17).

## References

- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), §8, (8.17)–(8.24), pp. 77–78: zero angular mean, test-value subtraction and the spherical principal-value limit. The full local derivation and its Hessian normalization are supplied above and in the indicated programme proofs.
- Jiří Lebl, [*Tasty Bits of Several Complex Variables*, version 3.4](https://www.jirka.org/scv/scv-3.4.pdf), §4.1, Theorem 4.1.1 and proof, pp. 109–110: the Cauchy–Pompeiu excision argument. Its local integrability and boundary contributions are proved in the supplied Cauchy lessons; no exercise or citation replaces them.
- All scalar Gamma, complex Laplace, tensor, polar and Fourier prerequisites used here are the exact earlier programme proofs linked above. External source prose and PDFs are not reproduced. Supplied foundations retain their stated component licences.
