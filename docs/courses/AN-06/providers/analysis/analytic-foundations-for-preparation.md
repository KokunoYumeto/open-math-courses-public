# Analytic foundations for preparation

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

An analytic function that has finite order in one coordinate can be separated into a nonvanishing factor and a monic polynomial in that coordinate. We construct this factorization by solving a convergent coefficient equation. We then recover the polynomial from contour integrals, which also give bounds for division of bounded analytic functions. Both constructions allow repeated roots and real analytic data.

The scalar complex-analysis inputs are in *Cauchy's theorem for cycles and its consequences*. Lemma 0.1 proves contour bounds, uniform-limit passage and iterated integration; Theorems 2.1–2.3 prove Goursat's triangle theorem, convex-domain primitives and Cauchy's formula. Lemma 3.1 and Theorem 3.2 give Taylor series and coefficient bounds. Corollary 3.3, Theorems 3.6–3.7 and the solution of Exercise 1 give Liouville's theorem, the maximum modulus and identity principles, and polynomial factorization over the complex numbers. We also use the proved [real-power calculus](elementary-functions-and-cutoffs.md#logarithm-and-real-powers), [finite linear algebra](coordinate-inverses-and-integration.md#coordinate-linear-algebra), and [compactness and scalar mean values](hilbert-valued-integration.md#compact-scalar-calculus). The arguments below precede [quantitative polynomial growth](quantitative-polynomial-growth.md).

<a id="analytic-algebra"></a>
## 1. Operations on convergent series

Write a power series in finitely many variables as $\sum_\alpha c_\alpha z^\alpha$. Analyticity means absolute convergence on some open polydisc. Choose two polyradii, with the smaller strictly below the larger and the latter still in that polydisc. On the smaller closed polydisc each differentiated term is bounded by its original weighted coefficient times a polynomial in $\alpha$ and a geometric factor. The geometric decay absorbs the polynomial. Thus the series and every fixed derivative series converge uniformly there, and termwise differentiation is valid. Absolute convergence also permits multiplication: finite convolution gives each coefficient, and the sum of the absolute values of the product terms is at most the product of the two absolute sums.

For composition, first center the inner functions at their values at the base point. Their zero-constant series have absolute sums tending to zero as the polyradius tends to zero. Choose it so that those sums are inside the convergence polydisc of the outer series. Substitution is then dominated by the absolute outer series evaluated at these sums. Its partial sums converge absolutely to an analytic series, proving the composition rule.

If $h(0)\ne0$, write $h=h(0)(1+k)$ with $k(0)=0$. On a sufficiently small polydisc the absolute coefficient sum of $k$ is below one. Multiplication of the finite geometric sums and passage to the absolute limit prove
\[
 h^{-1}=h(0)^{-1}\sum_{j\ge0}(-k)^j.
 \tag{AF1}
\]
Thus the reciprocal is analytic. A convergent real power series has the same absolutely convergent complex extension after reducing its radii. A complex series with real coefficients restricts to a real analytic function; conversely, invariance under coefficient conjugation forces its coefficients to be real.

Here are the positive rational powers needed later. Given $\alpha=p/q$, where $p\in\mathbb Z$ and $q\ge1$, let $c_0=1$ and $c_{j+1}=(\alpha-j)c_j/(j+1)$. The resulting series $B(t)=\sum_{j\ge0}c_jt^j$ either terminates or converges absolutely for $|t|<1$: on every smaller radius the ratio of consecutive absolute terms is eventually bounded by a number below one. Coefficient comparison gives $(1+t)B'=\alpha B$. On the real interval $(-1,1)$, the derivative of $B^q(1+t)^{-p}$ is consequently zero. The scalar mean-value theorem and its value at zero give $B^q=(1+t)^p$. This identity prevents a zero of $B$; continuity and $B(0)=1$ select the positive real branch. For every $a>0$, the expansion $a^\alpha B(t/a)$ therefore equals $(a+t)^\alpha$ on $|t|<a$.

We can also choose one regular direction for finitely many nonzero germs, including germs with complex coefficients but real coordinate changes. A polynomial vanishing on a real open box is zero: fix all but one variable, use the fact that a nonzero one-variable polynomial has only finitely many roots, and repeat this argument on its coefficient polynomials. The product of finitely many nonzero polynomials is nonzero, because the product of their lexicographically greatest monomials is its unique greatest monomial with a nonzero coefficient. Apply these facts to the first nonzero homogeneous terms of the germs. On a real box avoiding the origin there is a vector where their product is nonzero. Restriction of each germ to that line has exactly its first homogeneous degree as vanishing order. Complete the vector to a real basis. The resulting invertible linear substitution is analytic by the composition argument above and supplies the desired common normal coordinate.

<a id="zero-counting"></a>
## 2. Counting zeros by their multiplicities

We begin with removal of a bounded puncture. Suppose $f$ is holomorphic and bounded near $a$, except possibly at $a$. Set $H(z)=(z-a)^2f(z)$ off $a$, and $H(a)=0$. Boundedness makes $H$ continuous at $a$ and gives $H(a+h)/h=hf(a+h)\to0$. Hence $H$ is holomorphic throughout the disc and has its first two Taylor coefficients zero. Divide its Taylor series by $(z-a)^2$. The quotient is holomorphic and agrees with $f$ away from $a$, proving the removal assertion.

Now let $f$ be holomorphic near a closed disc and nonzero on its boundary. Its zeros in the disc are finite. Otherwise compactness would produce an accumulation point; a boundary accumulation contradicts continuity and nonvanishing, and an interior one contradicts the proved identity theorem. At each zero the first nonzero Taylor coefficient gives a finite order $m$. Dividing out these local factors produces a function with no zero near the closed disc. Consequently, for distinct zeros $a_\nu$ and their multiplicities $m_\nu$,
\[
 f(z)=v(z)\prod_{\nu=1}^{N}(z-a_\nu)^{m_\nu},
 \qquad v(z)\ne0.
 \tag{AF2}
\]
All divisions through a zero here are justified by its convergent Taylor factor; shrinking the surrounding neighborhood excludes any other zero of $v$.

Let the circle be $|z-c|=r$, traversed positively, and let $h$ be a polynomial. Differentiating the finite product in (AF2) gives $f'/f=v'/v+\sum_\nu m_\nu/(z-a_\nu)$ on the circle. The first summand is holomorphic on a slightly larger disc, by (AF1). Cauchy's theorem makes its product with $h$ integrate to zero, while Cauchy's formula evaluates each remaining summand. Thus
\[
 \frac1{2\pi i}\int_{|z-c|=r}
       h(z)\frac{f'(z)}{f(z)}\,dz
 =\sum_{\nu=1}^{N}m_\nu h(a_\nu).
 \tag{AF3}
\]
Taking $h=1$ counts all zeros with multiplicity. Taking $h(z)=z^j$ gives their power sums. This derivation needs neither a choice of logarithm nor a meromorphic residue formula.

<a id="root-continuity"></a>
## 3. Perturbing an unordered set of roots

Suppose a family $f_u$ is holomorphic near a fixed closed disc, and both $f_u$ and $f'_u$ vary continuously with $u$, uniformly on the boundary. At a parameter $u_0$ where the boundary is zero-free, its positive minimum stays bounded below for nearby parameters. The left side of (AF3), with $h=1$, is then continuous in $u$. Since its values are integers, the zero count is locally constant.

For a monic polynomial of degree $s\ge1$, a local coefficient bound $M\ge\max_j|b_j(u)|$ gives, when $|z|>1+M$,
\[
 \left|\sum_{j=1}^{s} b_j(u)z^{s-j}\right|
 \le M\sum_{j=0}^{s-1}|z|^j<|z|^s.
 \tag{AF4}
\]
There are no roots outside that common disc. Around the distinct roots at $u_0$, choose disjoint small discs. Uniform boundary convergence holds for the polynomial and its derivative, so the count in each disc stays equal to the multiplicity of its original root. These counts sum to $s$. The fundamental theorem of algebra and successive division by linear factors give exactly $s$ roots with multiplicity, so none are missing. Since the small discs can be made arbitrarily small, this proves continuity of the multiset of roots. It makes no assertion about a global labelling or analytic labels at a collision. A constant monic polynomial has the empty multiset.

For an analytic family on a fixed disc with zero-free boundary, use the same argument on the outer circle and on disjoint circles around its zeros at $u_0$. The inner counts account for the entire outer count and therefore exhaust the nearby zeros. In particular, if the only zero at $u=0$ is the origin, every zero in the disc tends to the origin as $u\to0$.

<a id="newton-identities"></a>
## 4. Recovering a polynomial from power sums

Let $a_1,\ldots,a_s$ be any list, allowing repeated and zero entries. Put $S_j=\sum_\nu a_\nu^j$, and define the elementary symmetric functions by
\[
 E(t)=\prod_{\nu=1}^{s}(1-a_\nu t)
     =\sum_{k=0}^{s}(-1)^ke_kt^k,
 \qquad e_0=1.
\]
For sufficiently small $t$, product differentiation and the geometric expansions of $(1-a_\nu t)^{-1}$ give $-tE'(t)=E(t)\sum_{j\ge1}S_jt^j$. Equating the coefficient of $t^k$ yields
\[
 k e_k=\sum_{j=1}^{k}(-1)^{j-1}e_{k-j}S_j,
 \qquad 1\le k\le s.
 \tag{AF5}
\]
Starting with $e_0=1$, this is a finite recursion expressing $e_k$ as a rational-coefficient polynomial in $S_1,\ldots,S_k$. Thus analytic power sums give analytic polynomial coefficients even at multiple roots. No root branches enter the calculation.

<a id="parameter-integrals"></a>
## 5. Parameter integrals as convergent series

Let $u\in\mathbb C^d$ and let $\Gamma$ be a fixed circle. Assume $F(u,\zeta)$ is continuous on a neighborhood of a closed parameter polydisc times $\Gamma$, and holomorphic in each parameter with the others fixed. Apply the scalar Cauchy formula in each parameter on circles of radii $R_i$ about $u_i^0$. Their product is an iterated integral for $F$. Expand its kernels geometrically on smaller radii $\rho_i<R_i$. The coefficient integrals are continuous in $\zeta$ and satisfy
\[
 \begin{gathered}
 F(u,\zeta)=\sum_{\alpha\in\mathbb N^d}
             A_\alpha(\zeta)(u-u^0)^\alpha,\\
 |A_\alpha(\zeta)|\le M\prod_iR_i^{-\alpha_i},
 \end{gathered}
 \tag{AF6}
\]
where $M$ is the supremum on the compact integration tori times $\Gamma$. The total majorant on the smaller polydisc is $M\prod_i(1-\rho_i/R_i)^{-1}$. It proves uniform absolute convergence in the parameters and on the circle together. Finite kernel sums followed by this uniform bound justify all limit passages; interchange of the contour integrals follows from the earlier continuous iterated-integration lemma, or directly from their rectangular Riemann sums.

Termwise contour integration now proves analyticity of
\[
 u\longmapsto\int_\Gamma F(u,\zeta)\,d\zeta.
 \tag{AF7}
\]
When the data are initially defined only near $\{u^0\}\times\Gamma$, compactness of the circle supplies one common smaller parameter polydisc for this argument.

There is also a joint assertion for a Cauchy extension. On $|\zeta|=r$ and $|w|\le b<r$, expand $(\zeta-w)^{-1}=\sum_{k\ge0}w^k\zeta^{-k-1}$. Combining this series with (AF6) gives an absolutely convergent series in $(u-u^0,w)$ for
\[
 \frac1{2\pi i}\int_{|\zeta|=r}
       \frac{F(u,\zeta)}{\zeta-w}\,d\zeta.
 \tag{AF8}
\]
Indeed, the additional geometric majorant is $1/(r-b)$. To center at any other interior point $w^0$, expand instead in $(w-w^0)/(\zeta-w^0)$ for $|w-w^0|<\operatorname{dist}(w^0,\Gamma)$. This proves joint analyticity at every interior point directly from the scalar formulas. For no parameter variables the assertion reduces to the scalar Cauchy construction.

<a id="preparation-interface"></a>
## 6. Solving division in coefficient space

<a id="coefficient-division"></a>

Write the coordinates as $(u,w)\in\mathbb C^d\times\mathbb C$. Suppose $g(0,w)$ has finite order $s$ at zero. If $s=0$, the reciprocal construction already gives preparation with $P=1$, unit $U=g$, and division $f=g(f/g)+0$. A positive lower bound on a smaller closed polydisc gives the quotient bound. We henceforth take $s\ge1$.

For positive weights $\delta,r$, consider coefficient arrays with finite norm
\[
 \|f\|_{\delta,r}
 =\sum_{\alpha\in\mathbb N^d,\,k\ge0}
       |f_{\alpha k}|\delta^{|\alpha|}r^k.
 \tag{AD1}
\]
They define analytic functions on the open polydisc and continuous functions on its closure, by uniform absolute convergence. Every analytic germ belongs to such a space after reducing its radii. Multiplication has norm at most the product of the norms: expand the coefficient convolution and sum its nonnegative absolute terms, taking suprema of finite partial sums.

This normed coefficient space is complete. For a Cauchy sequence, each weighted coefficient has a limit. Fix a Cauchy tolerance and pass to these limits in any finite sum of coefficient differences from a sufficiently late term. Its bound is the same tolerance. Taking the supremum over all finite sets proves that the full norm difference has this bound; it also proves that the limiting array has finite norm. Thus convergence occurs in the norm. This proves the completeness needed below without importing a theorem about function spaces.

Let $J_s$ retain the terms of degree less than $s$ in $w$, and let $D_s$ discard those terms and divide the rest by $w^s$. Then
\[
 \begin{gathered}
 f=w^sD_sf+J_sf,\\
 \|D_sf\|_{\delta,r}\le r^{-s}\|f\|_{\delta,r},\\
 \|J_sf\|_{\delta,r}\le\|f\|_{\delta,r}.
 \end{gathered}
 \tag{AD2}
\]
The coefficient series in $u$ of $J_sf$ converge, so it is a polynomial in $w$ of degree below $s$ with analytic coefficients.

Write $g(0,w)=w^sv(w)$ with $v(0)\ne0$, and choose a small normal radius on which $v$ is a unit. Set $h(u,w)=g(u,w)/v(w)=w^s+E(u,w)$. Every coefficient of $E$ with $u$-degree zero vanishes. Choose an initial parameter radius $\delta_0$ and a normal radius $r$ for which $\|E\|_{\delta_0,r}<\infty$. For $0<\delta\le\delta_0$,
$\|E\|_{\delta,r}\le(\delta/\delta_0)\|E\|_{\delta_0,r}$, since every term has positive parameter degree. Reduce $\delta$ until $\rho=r^{-s}\|E\|_{\delta,r}<1/3$. When $d=0$, $E=0$ and no reduction is required.

Division $f=hq+R$, with $\deg_wR<s$, is equivalent under $D_s$ to $q+D_s(Eq)=D_sf$. Put $Tq=D_s(Eq)$. Its norm is at most $\rho<1$. Completeness and the geometric bound on $T^jD_sf$ give the convergent solution
\[
 \begin{gathered}
 q=\sum_{j\ge0}(-T)^jD_sf,\\
 R=f-hq.
 \end{gathered}
 \tag{AD3}
\]
Multiplication of finite sums by $I+T$ leaves a last term tending to zero, so the equation holds. It gives $D_sR=0$, hence $R=J_sR$. For two solutions, their quotient difference satisfies $q=-Tq$, and the norm inequality forces $q=0$; their remainder difference is then zero. This proves existence and uniqueness in the coefficient space. It proves the same assertion for analytic germs, because any two candidate germ solutions and the data belong to a common smaller weighted space where the same contraction bound holds.

Apply this division to $f=w^s$. Since $D_sf=1$, its quotient $q_*$ satisfies $\|q_*-1\|\le\rho/(1-\rho)<1/2$. It is a unit, both by (AF1) and by the norm-convergent geometric inverse. At $u=0$ the equation has $E=0$, so $q_*(0,w)=1$ and $R_*(0,w)=0$. Therefore
\[
 \begin{gathered}
 P=w^s-R_*=h q_*,\\
 U=v/q_*,\qquad g=UP,\\
 P(u,w)=w^s+\sum_{j=1}^s a_j(u)w^{s-j},\\
 a_j(0)=0.
 \end{gathered}
 \tag{AD4}
\]
This constructs the distinguished monic polynomial and the analytic unit. After reducing the polydisc again, they are analytic on a neighborhood of its closure and the unit stays bounded away from zero.

For any analytic $f$, the same coefficient argument divides by $P$: now $E=P-w^s$ again has zero parameter-constant part. Division by $g=UP$ follows by replacing the quotient for $P$ by its quotient by $U$. In real analytic data, complexification gives the same constructions. Every coefficient operation, geometric sum and reciprocal preserves real coefficients, so the resulting units, quotients and remainders have real analytic restrictions.

The distinguished factorization is unique. If $g=\widetilde U\widetilde P$ is another such factorization, restriction to $u=0$ shows that the degree of $\widetilde P$ is $s$. Take a common small polydisc where both units are nonzero. By the root-multiset continuity in Section 3, all roots of both polynomials lie in its normal disc for sufficiently small parameters. In each fibre their roots, including multiplicities, are precisely the zeros of $g$. A monic polynomial is the product of its linear factors, so $P=\widetilde P$, and then $U=\widetilde U$. This also identifies factorizations obtained by different choices of coefficient weights.

## 7. Contour formulas and uniform division bounds

There is a second construction that records the zeros directly. Choose a normal circle $|w|=r$ enclosing only the order-$s$ zero of $g(0,w)$, with $g(0,w)$ nonzero on a surrounding closed annulus. By continuity and compactness, that annulus remains zero-free on a small parameter polydisc. Sections 2 and 5 apply to
\[
 S_j(u)=\frac1{2\pi i}\int_{|\zeta|=r}
       \zeta^j\frac{\partial_\zeta g(u,\zeta)}{g(u,\zeta)}\,d\zeta.
 \tag{AF9}
\]
These functions are analytic. Continuity makes $|S_0(u)-s|<1/2$ after shrinking the parameter polydisc, so its integer-valued zero count is exactly $s$ there. The other $S_j$ are the power sums of the fibre zeros. Newton's recursion gives analytic $e_k$ with $e_k(0)=0$. The polynomial $w^s-e_1w^{s-1}+\cdots+(-1)^se_s$ therefore has exactly those zeros and multiplicities.

To obtain the unit by this route, cancel the equal Taylor factors of $g$ and this polynomial on each fibre. Both quotients extend holomorphically through the fibre zeros. On the boundary annulus the quotients are already jointly analytic by (AF1). Apply (AF8) to their boundary values. Scalar Cauchy's formula identifies the jointly analytic interior extensions with the fibrewise quotients. Their product is one, including at a cancelled zero by continuity. This proves preparation by the contour route; uniqueness identifies its factors with (AD4). For real data, conjugation preserves each fibre multiset with its multiplicities, so its elementary symmetric functions are real. This also proves the real-form assertion by the contour route.

For a function $f$ analytic near a closed adapted polydisc, write $f_u(w)=f(u,w)$ and $P_u(w)=P(u,w)$. Set
\[
 K_u(\zeta,w)=\frac{P_u(\zeta)-P_u(w)}{\zeta-w}.
\]
Division by $P$ has the formulas
\[
 \begin{aligned}
 q(u,w)&=\frac1{2\pi i}\int_{|\zeta|=r}
       \frac{f_u(\zeta)}{P_u(\zeta)(\zeta-w)}\,d\zeta,\\
 R(u,w)&=\frac1{2\pi i}\int_{|\zeta|=r}
       \frac{f_u(\zeta)K_u(\zeta,w)}{P_u(\zeta)}\,d\zeta.
 \end{aligned}
 \tag{AF10}
\]
The first integral is jointly analytic by (AF8). In the second, use $(\zeta^k-w^k)/(\zeta-w)=\sum_{\ell=0}^{k-1}\zeta^{k-1-\ell}w^\ell$. Thus $K_u(\zeta,w)$ extends polynomially across $\zeta=w$ and has degree below $s$ in $w$. Each coefficient integral is analytic by (AF7). Adding $Pq$ and $R$ leaves exactly the scalar Cauchy formula for $f$, proving division.

There is also a fibrewise uniqueness proof. Subtract two divisions. The remainder difference is a polynomial of degree below $s$ and is holomorphically divisible by $P$. It consequently vanishes at every root of $P$ with at least that root's multiplicity. Successive division by these linear factors forces the remainder difference to be zero, and then the quotient difference is zero. This agrees with coefficient-space uniqueness and includes collisions. Conjugating a division of real data gives another division of the same data; uniqueness fixes both coefficient arrays under conjugation, again proving that their real restrictions are analytic.

We finish with the uniform estimate, including data defined only on an open polydisc. Reduce the parameter radius so that all roots lie in $|w|<r_0<r$ and
$|P(u,\zeta)|\ge\mu>0$ on the fixed closed annulus $r_0\le|\zeta|\le r$, uniformly on the closed parameter polydisc. This is possible by root continuity and compactness. The polynomial
$K_u(\zeta,w)$ is bounded in absolute value by a constant $K_0$ there for $|w|\le r$, including the diagonal by its polynomial extension.

For a contour of any radius $\tau\in(r_0,r)$, the second formula (AF10) therefore gives
$|R|\le C_R\sup|f|$, with $C_R=rK_0/\mu$ independent of $\tau$ and $f$. On a circle $|w|=t$ with $r_0<t<\tau$, the identity $q=(f-R)/P$ gives
$|q|\le\mu^{-1}(1+C_R)\sup|f|$. The earlier maximum modulus principle gives the same bound throughout $|w|\le t$.

If $f$ is bounded and analytic only on the open adapted polydisc, fix $\tau<r$ and apply the contour construction on a small neighborhood of any given parameter. Every contour is inside the domain of $f$, so Section 5 applies there. Different parameter neighborhoods and different radii give the same divisions on overlaps by the fibrewise uniqueness proof: every radius exceeds $r_0$ and encloses all $s$ roots. Thus the quotients and remainder coefficients glue analytically on the entire open polydisc. To bound a given smaller disc $|w|\le t$, choose $t<\tau<r$. The preceding constants do not depend on either radius. Letting $t$ tend to $r$ proves the uniform bounds for $q$ and $R$ on the whole open polydisc. For division by $g=UP$, replace $q$ by $q/U$ and use the unit's positive lower bound on the closed adapted polydisc. The degree-zero case has the reciprocal bound from Section 6. These estimates supply the bounded-data division used in the later Noetherian argument.

## Further reading

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, 21 June 2012, Chapter II, Section 2.A, printed pages 79–81](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=79), gives the classical contour construction of preparation and division and its bounded-data estimate.

The subsequent programme readings *Weierstrass preparation and division* and *Analytic finiteness for preparation* develop the algebraic and Noetherian consequences. The latter proves its one-variable convergent Puiseux conclusion through finite preparation induction. Their analytic inputs have been proved above.
