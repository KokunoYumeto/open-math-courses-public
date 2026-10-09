# Radial decay and spherical Fourier spectra

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Programme foundations retain their stated licences.*

The Fourier transform of a radial integrable function in three dimensions can be computed by averaging a plane wave on a sphere. The resulting sine integral also computes sphere measures. A derivative of a radial delta requires a different step: we construct it as a limit of smooth functions and retain the derivative of the polar volume density. This gives whole distributional identities and exact checks using moments and Gaussians.

We use \(Ff(\xi)=\int_{\mathbb R^3}e^{-ix\cdot\xi}f(x)\,dx\) and complex bilinear pairings, so \(FT(\phi)=T(F\phi)\). The [Schwartz Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the seminorm estimates, Gaussian constant, Fourier operations and transpose. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1, 15.6 and 16, proves convergence, absolute Fubini, linear changes, planar polar integration and generating-class uniqueness. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§13.1–13.5 and 13.7–13.10, proves calculus, exponential and trigonometric series, and smooth bumps.

For surface geometry we use exactly the latitude-and-area proof in [U035, Theorem 1.1](spherical-convolution-and-support-control.md), and the orthogonal invariance and cap estimate immediately preceding [U023, Lemma 2.1](positive-derivatives-and-canonical-representatives.md). Their graph measure and flux inputs are proved in U011, the graph construction and Theorem 2.1. The full measurable polar integration formula is proved in [the angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4. These earlier programme proofs are supplied with the lesson; external sources are not substitutes for them.

## A sphere integral reduces radial transforms to a sine integral

**Lemma 1.1.** Let \(f:[0,\infty)\to\mathbb C\) be measurable and suppose \(\int_0^\infty r^2|f(r)|\,dr<\infty\). Then \(f(|x|)\in L^1(\mathbb R^3)\), its Fourier transform is radial and continuous, and, for \(\rho=|\xi|>0\),
\[
F[f(|x|)](\xi)
=\frac{4\pi}{\rho}\int_0^\infty r f(r)\sin(r\rho)\,dr.
\tag{1.1}
\]
At zero its value is \(4\pi\int_0^\infty r^2f(r)\,dr\).

**Proof.** The supplied latitude proof uses
\[
\omega(t,\theta)=
(\sqrt{1-t^2}\cos\theta,\sqrt{1-t^2}\sin\theta,t)
\]
with \(-1<t<1\) and \(0<\theta<2\pi\). On a hemisphere the graph density is \(1/|t|\); planar polar radius \(q=\sqrt{1-t^2}\) satisfies \(q|dq|=|t||dt|\). Thus \(dS=dt\,d\theta\), first on coordinate rectangles and then on all Borel sets by generating-class uniqueness. The equator and seam are null in graph charts, and the poles are null by the cap bound. Orthogonal invariance allows the latitude axis to be \(\xi/\rho\). Consequently,
\[
\begin{aligned}
\int_{S^2}e^{-ir\omega\cdot\xi}\,dS(\omega)
&=2\pi\int_{-1}^1e^{-ir\rho t}\,dt\\
&=4\pi\,\frac{\sin(r\rho)}{r\rho}.
\end{aligned}
\tag{1.2}
\]
The integral equals \(4\pi\) when \(r\rho=0\), and its absolute value is at most \(4\pi\).

The full polar formula now gives
\(\|f(|\cdot|)\|_1=4\pi\int r^2|f(r)|\,dr\). Absolute Fubini inserts (1.2) into its Fourier integral and proves (1.1). The sine integral is absolutely convergent: on \(0<r<1\), \(|\sin(r\rho)|\le r\rho\); on \(r\ge1\), \(r\le r^2\). The original sphere integral is bounded by \(4\pi\), so dominated convergence against \(r^2|f(r)|\) supplies its value and continuity at zero. Dominated convergence in the original Euclidean integral gives continuity everywhere. Orthogonal substitution proves radiality.

This is also the whole tempered transform. Indeed a bounded function defines a tempered distribution by the \(L^1\) Schwartz estimate F1. For a Schwartz test \(\phi\), the double integral defining the transpose has absolute integral at most \(\|f(|\cdot|)\|_1\|\phi\|_1\). Fubini therefore identifies it with integration against (1.1) and its continuous extension. \(\square\)

**Theorem 1.2.** In three dimensions,
\[
F(e^{-|x|})(\xi)=\frac{8\pi}{(1+|\xi|^2)^2}.
\tag{1.3}
\]

**Proof.** For \(\operatorname{Re}z>0\), the exponential primitive and integration by parts give
\[
\int_0^\infty e^{-zr}\,dr=\frac1z,\qquad
\int_0^\infty re^{-zr}\,dr=\frac1{z^2}.
\]
The boundary terms vanish because \(r^ke^{-cr}\to0\) for \(c>0\): the exponential series bounds \(e^{cr/2}\) below by any fixed power, leaving \(e^{-cr/2}\to0\). The same bound proves absolute integrability. Set \(z=1-i\rho\); the imaginary part of \(z^{-2}=(1+i\rho)^2/(1+\rho^2)^2\) is \(2\rho/(1+\rho^2)^2\). Lemma 1.1 gives the formula at \(\rho>0\).

For later moment checks, repeated integration by parts gives, for every integer \(k\ge0\) and \(\lambda>0\),
\[
I_k(\lambda):=\int_0^\infty r^ke^{-\lambda r}\,dr
=\frac{k!}{\lambda^{k+1}}.
\]
Here \(I_0=1/\lambda\), and \(I_k=kI_{k-1}/\lambda\), with the just-verified endpoints. In particular the physical mass is \(4\pi I_2(1)=8\pi\), which agrees with the continuous value at zero. \(\square\)

## Surface measure has a smooth transform at zero

**Theorem 2.1.** For Euclidean surface measure \(\sigma_a\) on \(\{|x|=a\}\), \(a>0\),
\[
F\sigma_a(\xi)=4\pi a^2\frac{\sin(a|\xi|)}{a|\xi|},
\tag{2.1}
\]
with smooth value \(4\pi a^2\) at zero.

**Proof.** Graph scaling, proved in A4, multiplies surface measure by \(a^2\). Formula (1.2) therefore computes the plane-wave integral on this sphere. Its value at zero is its mass \(4\pi a^2\). Differentiating a plane wave introduces only products of coordinates of \(x\), whose absolute values are bounded by powers of \(a\) on the sphere. Finite surface mass and dominated difference quotients thus give every coordinate derivative of the transform, and give continuity of those derivatives. This proves smoothness at zero without a polar-coordinate differentiability assumption.

For completeness, the scalar expression agrees there with
\(\operatorname{sinc}u=\sum_{j\ge0}(-1)^ju^{2j}/(2j+1)!\).
After \(u=a|\xi|\), this is a series in \(a^2|\xi|^2\); factorial bounds dominate every differentiated series on a compact set. Finally, absolute Fubini with bound \(4\pi a^2\|\phi\|_1\) proves
\(\sigma_a(F\phi)=\int F\sigma_a(\xi)\phi(\xi)\,d\xi\).
Hence the computed function represents the entire transpose. \(\square\)

## A radial delta derivative differentiates the volume density

We first construct all the delta derivatives needed here. Choose a smooth function \(\eta\), supported in \((-1,1)\), with integral one, and put \(\eta_\varepsilon(s)=\varepsilon^{-1}\eta(s/\varepsilon)\). Such a function is supplied by the scalar bump construction followed by division by its positive integral. For \(a>0\), \(m\ge0\) an integer, and \(0<\varepsilon<a^2/2\), consider the smooth compactly supported function
\(\eta_\varepsilon^{(m)}(|x|^2-a^2)\).

**Radial construction.** For a smooth test \(\psi\) define, near \(t=a^2\),
\[
A_\psi(t)=\sqrt t\int_{S^2}\psi(\sqrt t\,\omega)\,dS(\omega).
\]
This is smooth: \(t\) stays in a compact positive interval and each derivative of the integrand is bounded by finitely many derivatives of \(\psi\) on a compact annulus. Differentiation under the finite surface integral follows by dominated convergence. Polar integration and the ordinary substitution \(t=r^2\) give
\[
\begin{aligned}
\int\eta_\varepsilon^{(m)}(|x|^2-a^2)\psi(x)\,dx
&=\frac12\int_0^\infty
 \eta_\varepsilon^{(m)}(t-a^2)A_\psi(t)\,dt\\
&=\frac{(-1)^m}{2}\int_{-1}^1
 \eta(s)A_\psi^{(m)}(a^2+\varepsilon s)\,ds\\
&\longrightarrow \frac{(-1)^m}{2}A_\psi^{(m)}(a^2).
\end{aligned}
\]
The \(m\) integrations by parts have no endpoint terms, since the support lies strictly inside the positive axis. Uniform continuity of \(A_\psi^{(m)}\) near \(a^2\) proves the limit and its independence of the chosen unit-integral bump. This defines the notation
\[
\delta_0^{(m)}(|x|^2-a^2)(\psi)
:=\frac{(-1)^m}{2}A_\psi^{(m)}(a^2).
\]
The chain and product rules bound this functional by
\(C_{a,m}\max_{|\alpha|\le m,\ |x|=a}|\partial^\alpha\psi(x)|\).
It is consequently a distribution of order at most \(m\), is supported on the sphere, and is tempered because this bound is controlled by finitely many Schwartz seminorms. It also acts on any smooth function near the sphere. Two extensions agreeing there have identical derivatives on the sphere and hence the same action. This proves cutoff independence directly. No general pullback theorem is being assumed.

**Theorem 3.1.** The distribution \(T=\delta_0'(|x|^2-1)\) has whole Fourier transform
\[
FT(\xi)=-\pi\cos|\xi|.
\tag{3.1}
\]

**Proof.** Since \(d/dt=(2r)^{-1}d/dr\), the radial construction at \(a=1,m=1\) gives
\[
\begin{aligned}
T(\psi)&=-\frac12 A_\psi'(1)\\
&=-\frac14\int_{S^2}
       [\psi(\omega)+\omega\cdot\nabla\psi(\omega)]\,dS.
\end{aligned}
\tag{3.2}
\]
The first summand comes from differentiating the volume density \(\sqrt t\); the second comes from differentiating the test function.

Apply this to a plane wave, which is permitted by the established action on smooth functions near the sphere. For \(\rho=|\xi|>0\), (1.2) yields
\[
\begin{aligned}
T(e^{-ix\cdot\xi})
&=-\frac12\left.\frac d{dt}
 \left[\frac{4\pi\sin(\sqrt t\,\rho)}{\rho}\right]\right|_{t=1}\\
&=-\pi\cos\rho.
\end{aligned}
\tag{3.3}
\]
At \(\rho=0\), the bracket is \(4\pi\sqrt t\), giving \(-\pi\). The plane-wave pairing is smooth in \(\xi\) by differentiation under the finite sphere integral in (3.2). Equivalently, the cosine series becomes a locally differentiable series in \(|\xi|^2\).

To verify the whole transform, insert \(F\phi(x)=\int e^{-ix\cdot\xi}\phi(\xi)\,d\xi\) into (3.2). The function and its first \(x\)-derivatives are absolutely dominated by \((1+|\xi|)|\phi(\xi)|\), whose integral is finite by F1. Absolute Fubini gives
\[
T(F\phi)=\int_{\mathbb R^3}[-\pi\cos|\xi|]\phi(\xi)\,d\xi.
\]
Thus no distribution supported at the frequency origin is left undetermined. \(\square\)

## Exercises

**Exercise 1 (foundation).** For \(\lambda>0\) compute \(F(e^{-\lambda|x|})\) in dimension three. Normalize it to a probability density \(p_\lambda\), give \(Fp_\lambda\), and verify the zero-frequency mass.

**Exercise 2 (intermediate).** Compute the whole transform of \(|x|e^{-\lambda|x|}\) by differentiating the decay parameter. Justify differentiation and verify the result at zero by a direct physical mass integral.

**Exercise 3 (intermediate).** With \(p=p_1\) from Exercise 1, compute the transform, mass, mean and covariance matrix of the convolution \(p*p\). Prove the product rule in this case by absolute Fubini, and obtain the covariance both by physical moments and by the second-order Fourier expansion.

**Exercise 4 (foundation).** For \(a>0\) compare the distributions \(\delta_0(|x|^2-a^2)\) and sphere surface measure \(\sigma_a\) on \(\mathbb R^3\). Compute the former's whole transform and its value at zero.

**Exercise 5 (intermediate).** Define \(T_a=\delta_0'(|x|^2-a^2)\). Write its complete action on a smooth test near the sphere, and compute its Fourier transform and its zero-frequency value. Check the sign by differentiating the ordinary radial delta with respect to \(a^2\).

**Exercise 6 (advanced).** Define \(S_a=\delta_0''(|x|^2-a^2)\). Derive its action on a smooth test, prove it is a compact distribution of order at most two, and compute its entire Fourier transform. Retain the derivatives of the radial volume density and check the value at zero.

**Exercise 7 (intermediate).** Let \(\mu=\sigma_1-\tfrac14\sigma_2\). Compute its whole transform, total mass and leading term at frequency zero. Confirm the leading term by its signed second moments.

**Exercise 8 (advanced).** For \(T_1=\delta_0'(|x|^2-1)\) and \(b>0\), evaluate \(FT_1(e^{-b|\xi|^2})\) by the physical pullback and independently by a one-dimensional Gaussian cosine integral. Identify the value of \(b\) at which this pairing vanishes.

## Solutions

**Solution 1.** Use \(z=\lambda-i\rho\) in the proof of Theorem 1.2. Its inverse square has imaginary part \(2\lambda\rho/(\lambda^2+\rho^2)^2\), so
\[
F(e^{-\lambda|x|})(\xi)
=\frac{8\pi\lambda}{(\lambda^2+|\xi|^2)^2}.
\]
At zero the mass is \(4\pi I_2(\lambda)=8\pi/\lambda^3\). Hence
\[
p_\lambda(x)=\frac{\lambda^3}{8\pi}e^{-\lambda|x|},
\qquad
Fp_\lambda(\xi)=\frac{\lambda^4}{(\lambda^2+|\xi|^2)^2},
\qquad Fp_\lambda(0)=1.
\]
The density is nonnegative and has integral one, as required.

**Solution 2.** On a compact parameter interval \(\lambda\ge c>0\), the derivative of \(e^{-\lambda r}\) is bounded by \(re^{-cr}\). Its Euclidean integral is \(4\pi I_3(c)<\infty\). Dominated difference quotients therefore permit differentiating the whole Fourier integral. The minus derivative of the previous rational expression is
\[
F(|x|e^{-\lambda|x|})(\xi)
=\frac{8\pi(3\lambda^2-|\xi|^2)}
        {(\lambda^2+|\xi|^2)^3}.
\]
Its zero value \(24\pi/\lambda^4\) equals the direct mass \(4\pi I_3(\lambda)\). Lemma 1.1 and its transpose argument ensure equality as distributions everywhere.

**Solution 3.** Define \(q(x)=\int p(y)p(x-y)\,dy\). Tonelli gives \(\int q=1\) and finiteness almost everywhere; null exceptional values do not affect the density. Translation in the inner integral and absolute Fubini, with total bound \(\iint p(y)p(z)\,dy\,dz=1\), give
\[
Fq(\xi)=Fp(\xi)^2=(1+|\xi|^2)^{-4}.
\]
The radial moments are
\[
\int |x|p(x)\,dx=\tfrac12 I_3(1)=3,\qquad
\int |x|^2p(x)\,dx=\tfrac12 I_4(1)=12.
\]
Reflection in coordinate \(j\) makes its first moment zero and makes mixed second moments zero. Coordinate permutations make the three diagonal moments equal, so \(\int x_jx_kp(x)\,dx=4\delta_{jk}\).

The change \(x=y+z\) is valid also for moments: \(|y+z|\le |y|+|z|\), and \(|y+z|^2\le2|y|^2+2|z|^2\). These yield integrable bounds for the first and second moment double integrals against \(p(y)p(z)\). Expanding each coordinate product and using Fubini, the cross terms vanish by the zero means. Thus \(q\) has mean zero and covariance \(8I_3\).

Independently, finite second moments allow two frequency derivatives by dominated difference quotients, since each derivative is bounded by \(|x_jx_k|q(x)\). Therefore
\(\partial_j\partial_kFq(0)=-\int x_jx_kq(x)\,dx\).
For \(h(u)=(1+u)^{-4}\), \(h(0)=1,h'(0)=-4\) and \(h''(u)=20(1+u)^{-6}\) is bounded near zero. Two applications of the fundamental theorem give \(h(u)=1-4u+O(u^2)\). With \(u=|\xi|^2\) the Hessian is \(-8I_3\), reproducing the covariance.

**Solution 4.** The \(m=0\) radial construction, together with surface scaling, gives
\[
\delta_0(|x|^2-a^2)(\psi)
=\frac a2\int_{S^2}\psi(a\omega)\,dS
=\frac1{2a}\sigma_a(\psi).
\]
Theorem 2.1 now gives the whole smooth transform
\[
\frac{2\pi\sin(a\rho)}{\rho}
=2\pi a\,\operatorname{sinc}(a\rho),
\]
whose value at zero is \(2\pi a\). The normalization follows from \(r^2dr=\sqrt t\,dt/2\), rather than from an assumed delta change-of-variables rule.

**Solution 5.** Apply the product and chain rules once to \(A_\psi\):
\[
T_a(\psi)=-\frac1{4a}\int_{S^2}
 [\psi(a\omega)+aD_r\psi(a\omega)]\,dS,
\qquad D_r\psi(a\omega)=\omega\cdot\nabla\psi(a\omega).
\]
The construction has already proved compact support, order at most one and temperedness. Plane waves in this formula yield
\[
FT_a(\xi)=-\frac{\pi}{a}\cos(a|\xi|),
\qquad FT_a(0)=-\frac{\pi}{a}.
\]
For the sign check, put \(b=a^2\). Pairing the ordinary delta with \(\psi\) gives \(A_\psi(b)/2\); differentiation in \(b\) is \(A_\psi'(b)/2=-T_{\sqrt b}(\psi)\). On each compact positive \(b\)-interval all derivative bounds are uniform on a fixed annulus, so this is a valid distributional parameter derivative. Taking the minus \(b\)-derivative of \(2\pi\sin(\sqrt b\,\rho)/\rho\) gives the formula above, also at zero. The full transpose is justified by the same finite-sphere Fubini bound \((1+|\xi|)|\phi(\xi)|\) as in Theorem 3.1.

**Solution 6.** For fixed \(\omega\), set \(h(t)=\sqrt t\,\psi(\sqrt t\,\omega)/2\). Writing \(r=\sqrt t\) gives
\[
h'(t)=\frac{\psi(r\omega)}{4r}+\frac{D_r\psi(r\omega)}4,
\qquad
h''(a^2)=\frac{-\psi(a\omega)+aD_r\psi(a\omega)+a^2D_r^2\psi(a\omega)}{8a^3},
\]
where \(D_r^2\psi(a\omega)=\sum_{j,k}\omega_j\omega_k\partial_j\partial_k\psi(a\omega)\). Integrating \(h''(a^2)\) on the sphere gives \(S_a(\psi)\), with positive sign. Its finite \(C^2\) bound and support are explicit, and agree with the \(m=2\) construction.

Taking two \(b\)-derivatives of \(A_\psi(b)/2\) gives \(S_{\sqrt b}(\psi)\). Equivalently differentiate the ordinary delta plane-wave formula twice with \(d/db=(2a)^{-1}d/da\):
\[
FS_a(\xi)
=-\frac{\pi}{2a^3}
 [\cos(a\rho)+a\rho\sin(a\rho)].
\]
At zero the value is \(-\pi/(2a^3)\), also equal to \(\int_{S^2}-1/(8a^3)\,dS\) from a test equal to one near the sphere. Smoothness follows by differentiating the finite-sphere expression in \(\xi\), or by the series in \(\rho^2\). The result grows at most linearly. Substitution of \(F\phi\) into the displayed \(C^2\) pairing and absolute Fubini against \((1+|\xi|^2)|\phi(\xi)|\) verify the entire tempered identity.

**Solution 7.** The masses \(4\pi\) and \(16\pi\) show that \(\mu\) has mass zero. Linearity gives
\[
F\mu(\xi)=4\pi[\operatorname{sinc}\rho-\operatorname{sinc}(2\rho)]
=2\pi\rho^2+O(\rho^4).
\]
Indeed the factorially convergent series gives \(\operatorname{sinc}u=1-u^2/6+O(u^4)\), with the tail divided by \(u^4\) bounded on \(|u|\le2\). Symmetry makes the means and mixed moments zero, while scaling and equal diagonal moments give
\[
\int x_jx_k\,d\sigma_a=\frac{4\pi a^4}{3}\delta_{jk},
\qquad
\int x_jx_k\,d\mu=-4\pi\delta_{jk}.
\]
One can check the quadratic coefficient directly from the plane-wave integral. The measure is even, so the sine term integrates to zero. Repeated scalar integration by parts in the Taylor remainder gives \(|\cos v-1+v^2/2|\le |v|^4/24\). The compact measure \(\sigma_1+\tfrac14\sigma_2\) dominates the absolute value of every integral against \(\mu\), so its finite fourth moment bounds the integrated remainder by a constant times \(|\xi|^4\). The quadratic term is consequently
\(-\tfrac12\sum_{j,k}\xi_j\xi_k\int x_jx_k\,d\mu=2\pi|\xi|^2\).

**Solution 8.** The real Gaussian proof F3 gives
\[
F(e^{-b|\xi|^2})(x)=A e^{-|x|^2/(4b)},
\qquad A=(\pi/b)^{3/2}.
\]
On the unit sphere the radial derivative is \(-1/(2b)\) times the Gaussian value. Inserting it in (3.2) gives
\[
FT_1(e^{-b|\xi|^2})
=-\pi A\left(1-\frac1{2b}\right)e^{-1/(4b)}.
\]
For a separate frequency calculation, take the even real part of the one-dimensional F3 formula:
\[
\int_0^\infty e^{-br^2}\cos(cr)\,dr
=\frac{\sqrt\pi}{2\sqrt b}\,e^{-c^2/(4b)}.
\]
For \(b\) in a compact positive interval with lower endpoint \(d>0\), the differentiated integrand is bounded by \(r^2e^{-dr^2}\), which is integrable by F3's polynomial Gaussian bound. Thus minus the \(b\)-derivative gives
\[
\int_0^\infty r^2e^{-br^2}\cos(cr)\,dr
=\frac{\sqrt\pi}{4b^{3/2}}
 \left(1-\frac{c^2}{2b}\right)e^{-c^2/(4b)}.
\]
Use \(c=1\) and multiply by \(-4\pi^2\), the product of the spherical polar factor and the coefficient in \(-\pi\cos r\). The answer is again
\(-\pi^{5/2}b^{-3/2}(1-1/(2b))e^{-1/(4b)}\).
All other factors are nonzero for \(b>0\), so the pairing vanishes exactly at \(b=1/2\).

## References

- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), §6, especially (6.2)–(6.5), p. 62: the freely accessible author notes supply the radial sphere-integral method. The author's symmetric Fourier normalization is converted here to the convention stated above. The lesson supplies its convergence, origin, density-derivative and exercise proofs explicitly.
- The supplied programme proofs linked in the introduction give the exact scalar, integration, graph, polar and Gaussian inputs. The original exposition here is CC0; each supplied foundation retains its own stated licence.
