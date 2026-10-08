# Flat Sobolev traces and the zero-boundary energy space

*Written by GPT-6.1 Sol and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The entry proof of the unitary Fourier transform and Plancherel is [Fourier facts](finite-derivative-l2.md#fourier-normalization). We use its unitary normalization. Define $H^s(\mathbb R^n)$ by $\|u\|_{H^s}^2=\int\langle\xi\rangle^{2s}|\widehat u(\xi)|^2d\xi$. On the half-space $\Omega=\{(x',d):d>0\}$ use the restriction space with quotient norm: $u=U|_\Omega$, $U\in H^s(\mathbb R^n)$. We prove the flat trace for every real $s>1/2$, then characterize zero trace in the weak-derivative energy space.

The approximation results used below are [finite-integral-norm density](euclidean-approximation-and-convolution.md#finite-p-density), [mollification](euclidean-approximation-and-convolution.md#mollification) and [integer Sobolev density](euclidean-approximation-and-convolution.md#integer-sobolev-density). Integrals of vector-valued slices use the [Bochner integral](hilbert-valued-integration.md#bochner-integral), [integrable primitives](hilbert-valued-integration.md#vector-primitives) and their [product rule](hilbert-valued-integration.md#operator-products). All distributional identities are tested against compact smooth functions.

<a id="sobolev-flat-trace"></a>
## Flat Sobolev trace

For every real $s>1/2$ the trace is a continuous surjection
\[
 \gamma:H^s(\Omega)\longrightarrow H^{s-1/2}(\mathbb R^{n-1}).
 \tag{1}
\]
Start with a Schwartz full-space function. In the tangential Fourier variables set $\lambda=\langle\xi'\rangle$. Its slice at $d$ has transform
\[
 \widehat{U(\cdot,d)}(\xi')
 =(2\pi)^{-1/2}\int_{\mathbb R}e^{id\tau}\widehat U(\xi',\tau)\,d\tau.
\]
Cauchy–Schwarz and the substitution $\tau=\lambda t$ give
\[
 \int_{\mathbb R}(\lambda^2+\tau^2)^{-s}d\tau
 =C_s\lambda^{1-2s},\qquad C_s<\infty,
\]
and hence $\|U(\cdot,d)\|_{H^{s-1/2}}\leq C\|U\|_{H^s}$ uniformly in $d$. The finiteness of $C_s$ follows by comparison with $|t|^{-2s}$ for $|t|\geq1$; the latter tail integrates to a finite number precisely when $2s>1$.

Here is the required density in the Fourier norm. First truncate a weighted $L^2$ function to a bounded frequency ball; its discarded weighted integral tends to zero. Approximate that truncation in ordinary $L^2$ by compact smooth functions and multiply the approximants by a fixed smooth cutoff equal to one on the ball. On this fixed larger ball the weight and its reciprocal are bounded, so the same approximation holds in the weighted norm. The inverse Fourier transforms of these compact smooth functions are Schwartz, by the Fourier differentiation and integration-by-parts identities. This proves Schwartz density in $H^s$, for any real $s$. The weighted Fourier map also identifies $H^s$ isometrically with $L^2$, so the slice target is complete.

The uniform bound therefore extends the slice map to every full-space $H^s$ function. Translation in $d$ is continuous in $H^s$, by dominated convergence of its Fourier multiplier $e^{ih\tau}$, so $d\mapsto U(\cdot,d)$ is continuous into $H^{s-1/2}$. These slices represent the original distribution, rather than merely an abstract family of traces: Schwartz approximation converges in full-space $L^2$ since $s>0$, while its slices converge uniformly in $H^{s-1/2}$, hence uniformly in tangential $L^2$. Pair against a compact smooth function of $(x',d)$ and integrate over its bounded normal support. Cauchy–Schwarz bounds the slice error by the uniform $L^2$ error times the integral of the test's tangential $L^2$ norm. Passing to the limit gives the asserted distributional identity. In particular the continuous family agrees with the Fubini slices almost everywhere.

<a id="sobolev-restriction-trace"></a>
This trace depends only on the restriction to $d>0$. Indeed if two extensions have the same restriction, their difference is the zero distribution on every positive open slice strip. Pairing the continuous slice family with a tangential test function therefore gives zero for almost every positive $d$, hence for every positive $d$ by continuity, and then for $d=0$. Taking the infimum over extensions proves the quotient-norm bound in (1).

<a id="sobolev-trace-right-inverse"></a>
Surjectivity has a direct right inverse. Choose a Schwartz function $\phi$ of one variable with $\int\phi(t)dt=(2\pi)^{1/2}$. For $g\in H^{s-1/2}$ set
\[
 \widehat U(\xi',\tau)=\lambda^{-1}\widehat g(\xi')\phi(\tau/\lambda).
\]
Its trace is $g$, and its squared $H^s$ norm is
\[
 \left(\int(1+t^2)^s|\phi(t)|^2dt\right)
 \int\lambda^{2s-1}|\widehat g(\xi')|^2d\xi'<\infty.
\]
To identify the trace for general $g$, first approximate $\widehat g$ in its weighted norm by compact smooth functions. Their displayed extensions are Schwartz, so the slice formula at zero gives $g$ directly. The norm identity and trace continuity pass this equality to the limit. Thus this is a bounded linear right inverse, and restriction to $\Omega$ proves the onto claim. For $n=1$, the tangential space is $\mathbb C$, $\lambda=1$, and the same proof applies.

<a id="sobolev-energy-slices"></a>
## Zero trace and the energy closure

With the weak-derivative $H^1$ norm on the half-space,
\[
 \ker\gamma=H_0^1(\Omega),
 \qquad H_0^1(\Omega)=\overline{C_c^\infty(\Omega)}^{H^1}.
 \tag{2}
\]
We first construct the normal slices directly from weak derivatives. Put $\mathcal H=L^2(\mathbb R^{n-1})$, or $\mathcal H=\mathbb C$ in dimension one. For a weak $H^1$ function $u$ and each finite $T>0$, Fubini gives $u,f=\partial_du\in L^2((0,T);\mathcal H)$. Strong measurability follows by approximating the scalar functions in product $L^2$ by finite linear combinations of rectangle indicators. Choose a subsequence whose squared errors have finite sum; Tonelli then gives convergence in $\mathcal H$ for almost every $d$. The rectangle approximation used here is proved in [Euclidean products](finite-derivative-l2.md#euclidean-products). Testing the weak derivative identity with $h(x')\eta(d)$ first for compact smooth $h$, and then using their $L^2$ density, gives the distributional identity $\partial_du=f$ in every fixed $\mathcal H$ pairing.

This identity already gives an absolutely continuous representative; continuity need not be assumed. Let $F(d)=\int_{T/2}^d f(t)\,dt$. The primitive construction proves that $F'=f$ distributionally. Choose $\vartheta\in C_c^\infty((0,T))$ with integral one and put $c=\int_0^T\vartheta(d)(u(d)-F(d))\,dd\in\mathcal H$. A compact smooth scalar function of integral zero is the derivative of its compact smooth primitive. Pairing such tests with $u-F$ therefore gives zero. Subtracting $(\int\eta)\vartheta$ from an arbitrary test $\eta$ shows that $u-F=c$ as a vector distribution. It is also equality almost everywhere: in each fixed scalar pairing an $L^1_{\rm loc}$ function representing the zero distribution vanishes almost everywhere, by local mollification and its $L^1$ convergence. Use a countable dense subset of $\mathcal H$ to make the exceptional set common. Such a subset exists by the finite rational-box simple approximations in the density proof. Separation by this subset proves the vector equality.

Consequently $u(d)=c+F(d)$ almost everywhere has a representative continuous on $[0,T]$, absolutely continuous in the norm of $\mathcal H$, with normal derivative $f$. Cauchy–Schwarz gives $\|u(d)-u(e)\|_{\mathcal H}\leq |d-e|^{1/2}\|f\|_{L^2((0,T);\mathcal H)}$. Representatives for different $T$ agree on their overlaps by continuity. The limit $u(0)$ is therefore well defined. In particular, choosing a slice whose squared norm is at most the average, or approaching that bound, gives $\|u(0)\|_{\mathcal H}\leq T^{-1/2}\|u\|_{L^2(\mathbb R^{n-1}\times(0,T))}+T^{1/2}\|\partial_du\|_{L^2(\mathbb R^{n-1}\times(0,T))}$.

<a id="sobolev-even-extension"></a>
Now the weak and restriction definitions of $H^1$ agree. Define the even extension by $Eu(x',d)=u(x',|d|)$ away from $d=0$. For a compact smooth test function on full space, regard its normal slices as a continuously differentiable $\mathcal H$-valued function. The primitive product rule gives integration by parts on each normal half-interval. The two boundary terms contain the same $u(0)$ and cancel; hence the weak normal derivative is $\operatorname{sgn}(d)f(x',|d|)$. Tangential weak derivatives are the even extensions of the corresponding derivatives. To justify using a test that reaches $d=0$ in this assertion, multiply it on the positive half-space by cutoffs vanishing near zero. No tangential derivative hits these normal cutoffs, and dominated convergence passes the weak tangential identity to the limit. Reflection and Fubini then give the full-space identity. All these derivatives are square integrable, and the squared weak $H^1$ norm of $Eu$ is exactly twice that of $u$. The whole-space equivalence of weak and Fourier $H^1$ was proved in [integer Sobolev density](euclidean-approximation-and-convolution.md#integer-sobolev-density). Conversely restricting a full-space $H^1$ function preserves its weak derivatives. This proves equality of the two half-space spaces and equivalence of their norms.

The continuous Fourier slices of $Eu$ and the just-constructed normal slices of $u$ agree almost everywhere for $d>0$. Both are continuous into $\mathcal H$, so they agree everywhere for $d>0$ and have the same limit at zero. The Fourier trace $\gamma u$ is therefore exactly $u(0)$. It follows that every compact smooth function supported in $\Omega$ has zero trace and, by continuity, $H_0^1\subset\ker\gamma$.

<a id="sobolev-zero-extension"></a>
Conversely let $u\in H^1(\Omega)$ have zero trace. Its zero extension $E_0u$ is in $H^1(\mathbb R^n)$: integrate against a compact smooth test function on the normal lines. The boundary term is its zero $L^2$ trace, so the weak normal derivative is the zero extension of $\partial_d u$; tangential derivatives have the same identity by Fubini. All are square integrable. First cut off $E_0u$ in space by cutoffs tending to one, with derivative bounded by $C/R$; the $H^1$ error tends to zero by its integrable function and derivative tails. Translate such a compact function inward by $\varepsilon$, using $v_\varepsilon(x',d)=E_0u(x',d-\varepsilon)$ after the cutoff. Full-space $H^1$ translation continuity makes its restriction tend to the original restriction. Its support lies in $d\geq\varepsilon$. Convolution with a smooth compact mollifier of radius less than $\varepsilon/2$ now gives a compact smooth function supported strictly inside $\Omega$, and convolution tends to the translated function in $H^1$ by the same translation continuity. A successive choice of cutoff radius, inward shift and mollifier radius proves $u\in H_0^1$. This proves (2), including the zero-extension, density and boundary-term arguments.

<a id="sobolev-smooth-boundary"></a>
## Smooth boundaries

On a bounded smooth domain, or a compact smooth manifold with boundary, fix a smooth positive density and metric and a finite flattening atlas with a subordinate [smooth partition](coordinate-inverses-and-integration.md#finite-partitions). Choose each localized support inside a larger chart, separated from its artificial lateral and upper edges. The [smooth chain rule and change of variables](coordinate-inverses-and-integration.md#coordinate-integration), and bounded chart derivatives and Jacobians on these compact supports, give bounded maps on weak $H^1$. One can verify the weak chain rule without assuming boundary regularity: mollify on compact sets inside the open domain, apply the smooth chain rule there and pass the functions and first derivatives in local $L^2$. These compact sets exhaust the chart interior; the resulting derivative formula has the global $L^2$ bound from the same change of variables. The inverse chart gives the reverse bound. Multiplication by fixed smooth cutoffs obeys the weak product rule.

The value trace on a boundary chart is the flat trace just proved. These local traces agree on overlaps. Indeed, after localizing away from the artificial edges, use the even extension and full-space mollification to approximate an arbitrary chart $H^1$ function by functions smooth up to the boundary. Multiply by a fixed larger chart cutoff to retain the support. Trace continuity gives convergence in boundary $L^2$; changes between boundary charts preserve this convergence because their Jacobians and inverses are bounded on the localized supports. The ordinary equality of boundary values for smooth functions passes to the limit. Thus the local traces define one global value trace, and every interior compact smooth function has zero trace.

If that global trace vanishes, each localized boundary-chart function has zero flat trace. Extend it by zero across the artificial chart edges, where it already vanishes in a neighborhood. The flat construction above approximates it in $H^1$ by smooth functions compactly supported in the open half-space. A fixed cutoff equal to one on its support keeps the approximants in the larger chart. Pull them back: they are compactly supported in the manifold interior and converge in the chart $H^1$ norm. Localized interior-chart functions have the same approximation by ordinary mollification. Summing over the finite partition proves membership in $H_0^1$. Conversely trace continuity gives zero trace for every $H_0^1$ limit. Hence (2) holds on this smooth geometry as well. If the boundary is empty, the interior-chart argument says $H_0^1=H^1$. The real-index surjectivity in (1) remains the flat restriction theorem.
