# Exercises on analytic preparation

These two exercises and complete solutions use the proved [analytic preparation and Puiseux treatment](../analytic-finiteness-for-preparation.html). The inverse-power example comes from Guillaume Valette's On subanalytic geometry; its finite-refinement obstruction and the parameter/parity exercise are expanded here. The Valette component and these identified teaching additions are available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Adapted by GPT-6.1 Sol (OpenAI), Ultra, October 2026; no endorsement is implied.

### 15. A bounded function that needs a negative preparation exponent

**Level:** advanced. On

\[
C=\{(x,y):0<x<\epsilon,\ x^2<y<x\},\qquad 0<\epsilon<1,
\]

consider \(f(x,y)=x^3/y\). It is positive and bounded. Show that a finite preparation of \(f\) cannot have only nonnegative last-coordinate exponents, even if translations and analytic units are allowed. Use the convergent Puiseux theorem proved in the [analytic preparation treatment](../analytic-finiteness-for-preparation.html#convergent-puiseux-expansions).

**Solution.** We have \(0<f<x<\epsilon\). The formula \(f=x^3y^{-1}\) is already a reduction with translation zero, unit one and exponent \(-1\).

Suppose there is a finite cell preparation with all exponents nonnegative. Refine its one-dimensional base and shrink \(\epsilon\) so its base interval next to zero is \((0,\epsilon)\). Over it, list the finitely many endpoints within the original band, including \(x^2\) and \(x\):

\[
x^2=\alpha_0(x)<\alpha_1(x)<\cdots<\alpha_N(x)=x.
\]

Duplicate endpoints are removed; every open interval between consecutive endpoints is a preparation cell. Each positive endpoint has a convergent Puiseux expansion with leading term \(c_jx^{\nu_j}\), where \(c_j>0\). The bounds \(x^2\le\alpha_j\le x\) force \(1\le\nu_j\le2\). Since \(\nu_0=2\) and \(\nu_N=1\), some consecutive pair \(\alpha<\beta\) has strictly decreasing leading order. Thus \(\alpha/\beta\to0\).

On the corresponding band, write the supposed reduction as

\[
f(x,y)=a(x)|y-\theta(x)|^rU(x,y),\qquad r\ge0,
\qquad 0<m\le|U|\le M.
\]

The coefficient cannot vanish, since \(f>0\). The center is outside the band, hence either \(\theta\le\alpha\) or \(\theta\ge\beta\) throughout this connected base interval. After shrinking it, take

\[
y_\ell=2\alpha,\qquad y_h=\beta/2,
\qquad \alpha<y_\ell<y_h<\beta.
\]

The actual ratio is

\[
\frac{f(x,y_h)}{f(x,y_\ell)}
=\frac{4\alpha(x)}{\beta(x)}\longrightarrow0.
\]

If \(\theta\le\alpha\), the distance ratio is at least one, so the prepared ratio is at least \(m/M\). If \(\theta\ge\beta\), then

\[
\frac{\theta-y_h}{\theta-y_\ell}\ge\frac12,
\]

so the prepared ratio is at least \(2^{-r}m/M\). Both contradict its limit zero. Some negative exponent is therefore necessary. Boundedness of the whole function does not force nondegenerate preparation; its base coefficient can compensate for an inverse power on a narrowing band.

### 16. Even substitutions and parameter-dependent poles

**Level:** intermediate. Explain why the substitution \(t=\tau^2\) does not make \(\sqrt t\) analytic on a two-sided neighborhood of zero, while \(t=\tau^4\) does. Then analyze the globally subanalytic function

\[
f(x,t)=xt^{-1/2}+t^{1/3},
\qquad x\in\mathbb R,\quad 0<t<1.
\]

Give one common root-variable Laurent expansion and one even substitution that agrees with the actual function for both signs of the new variable. Determine the parameter pieces on which a continuous analytic extension at zero is possible.

**Solution.** The two compositions are \(|\tau|\) and \(\tau^2\). A two-sided analytic substitution must make every cleared exponent even, not merely make the substitution exponent even.

With \(t=\tau^6\) on the positive \(\tau\)-axis the Laurent expansion is

\[
f(x,\tau^6)=x\tau^{-3}+\tau^2,\qquad \tau>0.
\]

For both signs, choose \(t=\tau^{12}\). Then

\[
f(x,\tau^{12})=x\tau^{-6}+\tau^4,\qquad \tau\ne0.
\]

For \(x\ne0\) the pole remains; no continuous extension is possible there. On the parameter cell \(\{0\}\), the function becomes \(\tau^4\), analytic across zero. The cells \((-\infty,0),\{0\},(0,\infty)\) give one finite analytic parameter partition.

Even at \((x,t)=(0,0)\), continuity fails if one keeps all parameters together. Along \(x=t^{1/4}\), the first summand equals \(t^{-1/4}\) and diverges. The continuous-parameter theorem requires joint continuity on its stated neighborhood; continuity on the one slice \(x=0\) does not supply that hypothesis.
