# Flat Sobolev traces and the zero-boundary energy space

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The entry proof of the unitary Fourier transform and Plancherel is [Fourier facts](finite-derivative-l2.md#fourier-normalization). Define $H^s(\mathbb R^n)$ by $\|u\|_{H^s}^2=\int\langle\xi\rangle^{2s}|\widehat u(\xi)|^2d\xi$. On the half-space $\Omega=\{(x',d):d>0\}$ use the restriction space with quotient norm: $u=U|_\Omega$, $U\in H^s(\mathbb R^n)$. These are the flat slice and energy-space statements used in AN06; no arbitrary rough-boundary trace theorem is asserted.

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
and hence $\|U(\cdot,d)\|_{H^{s-1/2}}\leq C\|U\|_{H^s}$ uniformly in $d$. Density in the Fourier norm extends the slice map to every full-space $H^s$ function. Translation in $d$ is continuous in $H^s$, by dominated convergence of its Fourier multiplier $e^{ih\tau}$, so $d\mapsto U(\cdot,d)$ is continuous into $H^{s-1/2}$.

This trace depends only on the restriction to $d>0$. Indeed if two extensions have the same restriction, their difference is the zero distribution on every positive open slice strip. Pairing the continuous slice family with a tangential test function therefore gives zero for almost every positive $d$, hence for every positive $d$ by continuity, and then for $d=0$. Taking the infimum over extensions proves the quotient-norm bound in (1).

Surjectivity has a direct right inverse. Choose a Schwartz function $\phi$ of one variable with $\int\phi(t)dt=(2\pi)^{1/2}$. For $g\in H^{s-1/2}$ set
\[
 \widehat U(\xi',\tau)=\lambda^{-1}\widehat g(\xi')\phi(\tau/\lambda).
\]
Its trace is $g$, and its squared $H^s$ norm is
\[
 \left(\int(1+t^2)^s|\phi(t)|^2dt\right)
 \int\lambda^{2s-1}|\widehat g(\xi')|^2d\xi'<\infty.
\]
Restriction to $\Omega$ proves the onto claim. For $n=1$, the tangential space is $\mathbb C$, $\lambda=1$, and the same proof applies.

## Zero trace and the energy closure

With the weak-derivative $H^1$ norm on the half-space,
\[
 \ker\gamma=H_0^1(\Omega),
 \qquad H_0^1(\Omega)=\overline{C_c^\infty(\Omega)}^{H^1}.
 \tag{2}
\]
Here the weak and restriction definitions of $H^1$ agree. For completeness, a half-space weak $H^1$ function has an even extension across $d=0$ bounded in $H^1(\mathbb R^n)$, with at most twice the squared norm. To justify its normal derivative, for almost every $x'$ the function on each bounded normal interval is absolutely continuous with derivative its weak normal derivative. This follows by subtracting the integral of that derivative: the resulting distribution has derivative zero and is constant. The representative has a limit at $d=0$, and reflection matches this limit, so integration by parts on both sides leaves no jump term. Tangential derivatives reflect directly by Fubini. Thus the even extension has the claimed weak derivatives and norm; the converse restriction bound is immediate.

The trace of this extension agrees with the limit of normal slices in local $L^2$: on a bounded normal interval Cauchy–Schwarz applied to the integral of $\partial_d u$ bounds the $L^2$ difference of slices by $|d-e|^{1/2}\|\partial_d u\|_2$. The Fourier trace has the same limit by the already-proved $H^{1/2}$ continuity, so the two traces agree. It follows that every compact smooth function supported in $\Omega$ has zero trace and, by continuity, $H_0^1\subset\ker\gamma$.

Conversely let $u\in H^1(\Omega)$ have zero trace. Its zero extension $E_0u$ is in $H^1(\mathbb R^n)$: integrate against a compact smooth test function on the normal lines. The boundary term is its zero $L^2$ trace, so the weak normal derivative is the zero extension of $\partial_d u$; tangential derivatives have the same identity by Fubini. All are square integrable. First cut off $E_0u$ in space by cutoffs tending to one, with derivative bounded by $C/R$; the $H^1$ error tends to zero by its integrable function and derivative tails. Translate such a compact function inward by $\varepsilon$, using $v_\varepsilon(x',d)=E_0u(x',d-\varepsilon)$ after the cutoff. Full-space $H^1$ translation continuity makes its restriction tend to the original restriction. Its support lies in $d\geq\varepsilon$. Convolution with a smooth compact mollifier of radius less than $\varepsilon/2$ now gives a compact smooth function supported strictly inside $\Omega$, and convolution tends to the translated function in $H^1$ by the same translation continuity. A successive choice of cutoff radius, inward shift and mollifier radius proves $u\in H_0^1$. This proves (2), including the zero-extension, density and boundary-term arguments.

Multiplication by fixed smooth cutoffs preserves these estimates. On a bounded smooth domain or a compact smooth manifold with boundary, use a finite flattening atlas and its actual partition. The ordinary change of variables and chain rule give bounded maps on weak $H^1$; the just-proved half-space identity identifies their zero-trace energy closures. This extends (2) to that smooth geometry. The arbitrary real-index statement (1) is the flat restriction theorem; no unproved coordinate invariance for a rough map is inferred.
