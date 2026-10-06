# Approximation, convolution and integer Sobolev density

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The rough-coefficient arguments need norm approximation, translation continuity, convolution bounds and actual compact smooth cores. This reading proves these facts with their exact endpoints. The freely accessible comparison is Terence Tao's [Lecture notes 2, Theorem 6.4 and the approximate-identity discussion in Theorem 6.8 and Problem 6.9, printed pages 16–18](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf). The proofs below do not use an interpolation theorem or cite a density assertion in place of proving it. Norm approximation is asserted for $1\le p<\infty$; the uniform statement for continuous functions is separate.

The measure construction, monotone and dominated convergence and complete $L^p$ inequalities are proved in the earlier local [measure and function-space construction](finite-derivative-l2.md#measure-foundations); exact Euclidean product interchange is proved in [Euclidean products](finite-derivative-l2.md#euclidean-products). The latter also proves that finite-measure measurable sets can be approximated in measure by finite unions of bounded boxes. The same reading proves [Fourier inversion and Plancherel](finite-derivative-l2.md#fourier-normalization), with $\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx$ and inverse factor $(2\pi)^{-n}$. The facts proved here do not depend on choosing that transform or its unitary normalization.

<a id="holder-and-young"></a>
## 1. The integral inequalities, including their endpoints

For conjugate exponents $1<p,p'<\infty$, the scalar inequality $st\le s^p/p+t^{p'}/p'$ follows by minimizing $s^p/p-st$ over $s\ge0$ at $s=t^{1/(p-1)}$, with the endpoint and derivative justified in the proved [real powers and scalar Young inequality](elementary-functions-and-cutoffs.md#logarithm-and-real-powers). Normalize two functions by their $L^p,L^{p'}$ norms, integrate this inequality and undo the normalization. This proves Hölder's inequality. A zero norm is treated directly; the $1,\infty$ endpoint follows by taking an essential supremum out of the integral. Repeating the two-factor inequality proves the finite-factor version whenever the reciprocals of its exponents sum to one; a factor with exponent infinity is handled by its supremum.

We also use the triangle inequality in $L^p$. For $1<p<\infty$, apply Hölder to
$|f+g|^p\le |f+g|^{p-1}(|f|+|g|)$ and divide by $\|f+g\|_p^{p-1}$. One can first truncate to a finite-measure set with bounded functions, then pass to the limit; if the norm is zero there is nothing to divide. For $p=1$ or $p=\infty$ the assertion is the pointwise triangle inequality followed by the integral or essential supremum.

**Theorem 1.1 (Young's inequality).** If $1\le p,r,q\le\infty$ and
\[
 \frac1p+\frac1r=1+\frac1q,
 \tag{A1}
\]
then $f\in L^p(\mathbb R^n)$ and $g\in L^r(\mathbb R^n)$ have an almost everywhere absolutely defined convolution, and
\[
 \|f*g\|_q\le\|f\|_p\|g\|_r.
 \tag{A2}
\]

**Proof.** If either input has zero norm the assertion is immediate, so assume both norms are positive. Choose Borel representatives, as supplied by the completed-measure construction. The function $f(y)g(x-y)$ is then jointly measurable. A change of representative is supported, in coordinates $(y,x-y)$, on a product with a null factor; its product measure is zero by Tonelli and a countable bounded-box exhaustion. The invertible linear change $(x,y)\mapsto(y,x-y)$ has determinant of absolute value one, so the [proved linear substitution formula](coordinate-inverses-and-integration.md#coordinate-integration) preserves that null set. Fubini then proves that the resulting convolution is independent of the representatives almost everywhere and is measurable. It suffices to bound the convolution of absolute values. If $q=\infty$, (A1) is precisely the conjugate-exponent condition, so Hölder at each output point proves the assertion. If $q=1$, then $p=r=1$, and nonnegative product interchange gives (A2).

Otherwise $1<q<\infty$; (A1) implies $p,r\le q$, so both input exponents are finite. Factor the integrand as
\[
 |f(y)g(x-y)|=
 (|f(y)|^p|g(x-y)|^r)^{1/q}
 |f(y)|^{1-p/q}|g(x-y)|^{1-r/q}.
 \tag{A3}
\]
Apply the finite-factor Hölder inequality with reciprocal exponents
$1/q$, $1/p-1/q$, $1/r-1/q$, whose sum is one. If a latter exponent is zero, omit that factor, which is identically one. Raising the result to the power $q$ yields
\[
 (|f|*|g|)(x)^q
 \le\|f\|_p^{q-p}\|g\|_r^{q-r}
       \int |f(y)|^p|g(x-y)|^r\,dy.
 \tag{A4}
\]
Integration in $x$ and the already proved product theorem give (A2). One can perform this first for bounded, compactly supported nonnegative functions and then increase their truncations; monotone convergence gives both the norm estimate and almost everywhere finiteness of the absolute convolution. This also justifies every displayed integral for the original functions. $\square$

<a id="finite-p-density"></a>
## 2. Density and translation in finite integral norms

**Theorem 2.1.** For $1\le p<\infty$, compact smooth functions are dense in $L^p(\mathbb R^n)$, and, with $T_hf(x)=f(x-h)$,
\[
 \|T_hf-f\|_p\longrightarrow0\qquad(h\to0).
 \tag{A5}
\]

**Proof.** Truncate $f$ to $|x|\le N$, $|f|\le N$. Dominated convergence makes its difference from $f$ tend to zero in $L^p$. On the bounded box containing its support, approximate the real and imaginary parts by finite step functions with mesh tending to zero in the value variable. The uniform value error times the box volume to the power $1/p$ tends to zero. Thus simple functions with finite-measure level sets suffice.

For each such level set, the earlier box-approximation proof supplies a finite union of bounded boxes with symmetric difference of arbitrarily small measure. The $L^p$ distance of the two indicators is exactly the $p$th root of that measure. A finite grid of their coordinate endpoints rewrites a finite union as a sum of indicators of boxes with disjoint interiors, up to faces of measure zero. For one box, products of smooth one-variable cutoffs, between zero and one, approximate its indicator pointwise away from its faces. They are supported in one fixed larger box. Dominated convergence gives convergence in $L^p$. The full smoothness proof and these cutoffs are [the explicit constructions (EF16)–(EF18)](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs); their transition intervals can be chosen inside any fixed enlargement of the box. Combining these finite approximations proves density.

Translation is an isometry of $L^p$ by invariance of Lebesgue measure. For $g\in C_c^\infty$ and $|h|\le1$, the difference $T_hg-g$ has support in one bounded set, and the proved [line-segment fundamental theorem](coordinate-inverses-and-integration.md#coordinate-differential-rules) gives the uniform bound $|h|\sup|\nabla g|$. Hence its $L^p$ norm tends to zero. For general $f$ choose such a $g$ with small $L^p$ error and use
\[
 \|T_hf-f\|_p\le2\|f-g\|_p+\|T_hg-g\|_p.
 \tag{A6}
\]
First make the first term arbitrarily small and then let $h$ tend to zero. This proves (A5). $\square$

<a id="mollification"></a>
## 3. The precise approximation by convolution

Choose a real nonnegative $\rho\in C_c^\infty(B(0,1))$ with integral one by taking the [normalized flat bump](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) at radius $1/2$, and set $\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon)$.

**Theorem 3.1.** For every $f\in L^p$, $1\le p<\infty$,
\[
 \|\rho_\varepsilon*f-f\|_p\longrightarrow0.
 \tag{A7}
\]
The convolution is smooth. If $f$ has compact support, it is compactly supported. If $f$ is continuous with compact support, convergence also holds uniformly. More generally uniform convergence holds for every bounded uniformly continuous $f$.

**Proof.** By the substitution $y=\varepsilon z$ the difference is
$\int\rho(z)[f(x-\varepsilon z)-f(x)]\,dz$.
Hölder against the probability measure $\rho(z)dz$ gives, for $1\le p<\infty$,
\[
 \|\rho_\varepsilon*f-f\|_p^p
 \le\int\rho(z)\|T_{\varepsilon z}f-f\|_p^p\,dz.
 \tag{A8}
\]
For $p=1$ this is the integral triangle inequality. Theorem 2.1 gives convergence of the integrand; its bound $(2\|f\|_p)^p\rho(z)$ is integrable. Dominated convergence proves (A7). The absolute convolution and these interchanges are also justified by Theorem 1.1.

On each compact set of $x$, every derivative of $\rho_\varepsilon(x-y)$ is bounded and supported in one fixed compact set of $y$, where $f$ is integrable by Hölder. Differentiation under the integral is justified by dominated convergence, proving smoothness and its derivative formulas. The support is contained in the sum of the supports of $f$ and $\rho_\varepsilon$. For a bounded uniformly continuous $f$, its modulus of continuity bounds the same difference uniformly by $\sup_{|h|\le\varepsilon}\|T_hf-f\|_\infty$, which tends to zero. A continuous compactly supported function is uniformly continuous: on a sufficiently large compact ball use a finite cover by continuity neighborhoods, and outside that ball the function is zero. This proves the remaining claims. $\square$

No analogous norm statement is asserted for an arbitrary $L^\infty$ function. For example let $f=1_{\{x_1>0\}}$ and choose the normalized radial bump just described. Reflection in $y_1=0$ preserves the kernel and its integral, while the hyperplane is null, so $\int_{y_1<0}\rho_\varepsilon(y)dy=1/2$. The convolution is $\int_{y_1<x_1}\rho_\varepsilon(y)dy$, continuous in $x_1$ by dominated convergence, since each limiting hyperplane is null. Its limit at $x_1=0$ is $1/2$. On strips of positive measure arbitrarily close to that hyperplane the error therefore approaches $1/2$ for every fixed $\varepsilon>0$. In particular its essential-supremum norm cannot tend to zero.

<a id="integer-sobolev-density"></a>
## 4. Integer Sobolev derivatives and compact smooth cores

For an integer $k\ge0$ put $H^k=\{u\in\mathcal S':\langle\xi\rangle^k\widehat u\in L^2\}$ with the unitary Fourier norm. The distributional transform, its invertibility, its agreement with the $L^2$ transform, and its weighted multipliers are proved in [Fourier duality and weak derivatives](finite-derivative-l2.md#tempered-fourier-duality). If $h=\langle\xi\rangle^k\widehat u\in L^2$, multiplication by $\langle\xi\rangle^{-k}\le1$ shows that $\widehat u$ is represented by an $L^2$ function. Thus $u$ is represented by its $L^2$ inverse. Conversely any weighted $L^2$ transform defines this tempered distribution. Multiplying $k$ copies of $1+\sum_j\xi_j^2$ and grouping monomials gives $\sum_{|\alpha|\le k}c_\alpha\xi^{2\alpha}$ with every coefficient positive and bounded above and below by positive constants depending only on $n,k$. Plancherel and (F4) therefore show
\[
 \|u\|_{H^k}^2\asymp\sum_{|\alpha|\le k}\|D^\alpha u\|_2^2.
 \tag{A9}
\]
This equivalence includes membership: the distributional identity $\widehat{D^\alpha u}=\xi^\alpha\widehat u$, proved by testing and integration by parts, identifies these derivatives with $L^2$ functions exactly when the polynomially weighted Fourier integrals are finite. The zeroth term already puts $u$ in $L^2$. More explicitly, if all weak derivatives through order $k$ are $L^2$, (F4) and the agreement of the two transforms identify each $\xi^\alpha\widehat u$ with its $L^2$ transform, and the finite positive sum just computed is integrable. The converse uses the same sum and inverse unitarity. With the norm $\|(2\pi)^{-n/2}\langle\xi\rangle^k\widehat u\|_2$, the weighted transform is an isometric bijection onto $L^2$: its inverse first multiplies in frequency by $\langle\xi\rangle^{-k}$ and then applies the inverse unitary transform. Pulling back the $L^2$ inner product therefore also proves that $H^k$ is a complete Hilbert space.

**Theorem 4.1.** Compact smooth functions are dense in $H^k$, and translations act continuously in its norm. Multiplication by a compact smooth function obeys the distributional product rule and is continuous on $H^k$.

**Proof.** Translation continuity follows by applying (A5) with $p=2$ to each derivative in (A9). The weak product rule follows for one derivative by applying the weak-derivative identity to the test function multiplied by the smooth factor; induction gives its full multi-index form. For a compact smooth factor, its derivatives through order $k$ are bounded, so this product rule and (A9) give continuity.

Choose $\chi_R(x)=\chi(x/R)$, where $\chi$ is smooth, compactly supported and one near zero. The term $(\chi_R-1)D^\alpha u$ tends to zero in $L^2$ by dominated convergence. Every other term in $D^\alpha(\chi_Ru-u)$ is bounded in $L^2$ by $C R^{-|\beta|}\|D^{\alpha-\beta}u\|_2$ with $0<\beta\le\alpha$. It too tends to zero. Hence $\chi_Ru\to u$ in $H^k$.

For a fixed $R$, convolution of $\chi_Ru$ with $\rho_\varepsilon$ is compactly supported and smooth by Theorem 3.1. Its weak derivatives satisfy
\[
 D^\alpha(\rho_\varepsilon*(\chi_Ru))
    =\rho_\varepsilon*D^\alpha(\chi_Ru).
 \tag{A10}
\]
To check this equality, test against a compact smooth function, interchange the integrals, and use the weak derivative identity on $\chi_Ru$; the integrals are absolutely convergent on the relevant compact sets by local $L^2$ and Hölder. Theorem 3.1 at $p=2$ makes every right-hand side tend to $D^\alpha(\chi_Ru)$ in $L^2$. Thus mollification converges in $H^k$. Choose $R$ large and then $\varepsilon$ small to make the two errors arbitrarily small. This proves density. $\square$

For a coefficient in finite $L^p$ with compact support, Theorem 3.1 therefore supplies compact smooth approximants in the actual coefficient norm. For a continuous compactly supported leading coefficient it supplies uniform approximants. These are exactly the two distinct approximations used when a rough differential expression is smoothed.

<a id="oscillatory-integrals-and-averages"></a>
## 5. Oscillatory integrals and continuous Hilbert-space averages

**Proposition 5.1.** If $f\in L^1(\mathbb R^n)$, then $\widehat f(\xi)\to0$ as $|\xi|\to\infty$.

**Proof.** By Theorem 2.1 choose $g\in C_c^\infty$ with arbitrarily small $\|f-g\|_1$. The Fourier difference has supremum at most this norm. For each nonzero $\xi$, choose $j$ with $|\xi_j|\ge|\xi|/\sqrt n$ and integrate the compact smooth Fourier integral by parts in $x_j$. This gives $|\widehat g(\xi)|\le\sqrt n\max_j\|\partial_jg\|_1/|\xi|$. Thus $\widehat g$ tends uniformly to zero outside large balls. The arbitrarily small Fourier error proves the assertion. $\square$

The Hilbert-valued averages used to preserve symmetry can be constructed without assuming an integration theorem for operator-valued functions. If $F:\mathbb R^d\to H$ is continuous with compact support and $H$ is a complete Hilbert space, subdivide a box containing the support into small boxes and form tagged Riemann sums. Uniform continuity on the large box bounds the norm difference of sums on a common refinement by its volume times the modulus of continuity. Hence the sums are Cauchy as the mesh tends to zero and define $\int F$. The triangle inequality on the sums gives $\|\int F\|\le\int\|F\|$. Pairing with any fixed vector commutes with the limit, so it commutes with this integral. Scalar continuous integrals here agree with their Lebesgue integrals: upper and lower simple sums differ by the same vanishing modulus bound. The same tagged step functions converge to $F$ in the Bochner $L^1$ norm, with error at most the box volume times that modulus, so this integral also equals the [proved Banach-valued integral](hilbert-valued-integration.md#bochner-integral).

In particular, for a nonnegative integer $m$, if $W:H^m\to L^2$ is bounded and $u\in H^m$, then $y\mapsto T_yWT_{-y}u$ is continuous in $L^2$. Indeed for $y\to y_0$, split its difference as
\[
 T_yW(T_{-y}u-T_{-y_0}u)
       +(T_y-T_{y_0})WT_{-y_0}u.
 \tag{A11}
\]
The first term tends to zero by $H^m$ translation continuity and boundedness of $W$; the second does so by $L^2$ translation continuity. Multiplying by a compact smooth averaging weight therefore gives the integral just constructed. If each translated expression is symmetric on compact smooth inputs and the averaging weight is real, its integrated pairing identity proves symmetry of the average. This is the precise integral used in the elliptic-domain approximation; no coefficient derivative or unproved operator-valued integral is needed.

<a id="exact-source-correspondence"></a>

## Further reading

Tao's free notes supply the classical convolution statements and the approximate-identity comparison. Section 1 gives a direct finite-factor Hölder proof of Young's inequality, including all endpoints; Sections 2–4 prove the particular density and derivative statements required here. The finite-$p$ restriction in the approximation theorem and the separate uniform-continuity hypothesis are explicit. In particular, the printed $p=\infty$ endpoint of Theorem 6.8 conflicts with Problem 6.9; the half-space calculation above explains why it is excluded here. The proof retains the valid $p=1$ endpoint as well. The earlier programme measure and Fourier proofs, together with the arguments on this page, supply the actual prerequisites for these statements.
