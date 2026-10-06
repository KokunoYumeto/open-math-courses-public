# Hilbert-valued integration for the evolution equations

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


We prove the integration statements used in [Commuting coordinates for long-range evolution](../../src/commuting-coordinates-for-long-range-evolution.md), [Transverse moments and outgoing amplitudes](../../src/transverse-moments-and-outgoing-amplitudes.md), [Truncated operators and stable scattering amplitudes](../../src/truncated-operators-and-stable-scattering-amplitudes.md) and [Spectral transforms and completeness of modified waves](../../src/spectral-transforms-and-completeness-of-modified-waves.md). They concern strongly measurable integrable forcing, continuous bounded-operator propagators, norm primitives and products. The proofs also apply to the complete first-moment space used in the second lesson and to the Banach space of bounded operators when an integrand is continuous in operator norm.

The independent scalar inputs are completed Euclidean Lebesgue measure, scalar monotone and dominated convergence, finite-measure approximation by boxes, and scalar Fubini–Tonelli. Their proofs, including scalar $L^p$ completeness, are in the earlier local provider [Euclidean measure and the product theorem used below](finite-derivative-l2.md#euclidean-measure-and-the-product-theorem-used-below). Banach completeness is a hypothesis on the spaces in this lesson. We prove the bounded-functional separation fact next, so the vector fundamental theorem below has no external functional-analysis prerequisite. Hilbert inner products are linear in the first entry.

### Bounded functionals separate points

Here is the required norm-preserving extension argument, in the usual classical set theory with choice. For a nonzero vector $x_0$ in a real normed space, define $f(tx_0)=t\|x_0\|$ on its real span. Suppose $f$ is real linear on a subspace $E$ and $f(y)\le\|y\|$ there. To extend to $E+\mathbb R x$ with $x\notin E$, choose a real number $a$ in the interval
\[
 \sup_{y\in E}\bigl(f(y)-\|y-x\|\bigr)
 \ \le a\le\ 
 \inf_{y\in E}\bigl(\|y+x\|-f(y)\bigr).
\]
Every lower expression is at most every upper expression: for $y,z\in E$,
$f(y)+f(z)=f(y+z)\le\|y+z\|\le\|y-x\|+\|z+x\|$.
Taking $y=0$ on either side also shows that both endpoints are finite. The extension $F(y+tx)=f(y)+ta$ is at most $\|y+tx\|$: for $t>0$ use the upper bound with $y/t$, and for $t<0$ use the lower bound with $y/(-t)$; the case $t=0$ is the old bound. Applying it to the negative vector gives $|F(v)|\le\|v\|$. Order all such extensions of the original one-dimensional functional by extension of domain and values. This is a nonempty set, and every chain has an upper bound given by the union of its domains and the compatible values; linearity and the norm bound hold because any finite selection of vectors lies in one member of the chain. Apply the proved Zorn lemma, Theorem 1.1. A maximal extension has full domain, since otherwise the one-dimensional step above extends it. Its norm is at most one and its value at $x_0$ is $\|x_0\|$, so its norm is one. This proves the separation statement with the exact choice consequence supplied by an earlier programme proof.

For a complex space do this on its underlying real space, obtaining $f$, and set $\ell(x)=f(x)-if(ix)$. Real linearity gives $\ell(ix)=i\ell(x)$, hence complex linearity. If $\ell(x)\ne0$, take $\zeta=\overline{\ell(x)}/|\ell(x)|$; otherwise take $\zeta=1$. In both cases $|\zeta|=1$ and $\zeta\ell(x)=|\ell(x)|$. Then $|\ell(x)|=\operatorname{Re}\ell(\zeta x)=f(\zeta x)\le\|x\|$. In particular $\ell$ is bounded and $\operatorname{Re}\ell(x_0)=\|x_0\|>0$. Thus in either scalar field equality under every bounded linear functional implies equality of vectors. No separability hypothesis or representation of the dual is used.

<a id="strong-measurability"></a>

## 1. Strong measurability and integrable simple approximation

Let $B$ be a real or complex Banach space. A $B$-valued function on a Euclidean measurable set is **strongly measurable** if, after changing it on one measurable null set, it is a pointwise norm limit of measurable functions with finitely many values. All statements below identify functions equal almost everywhere. An ambient Hilbert space need not be separable.

The countably many values of an approximating sequence lie in a separable closed subspace $B_0$: take their closed linear span. Finite combinations with rational coefficients (rational real and imaginary parts in the complex case) form a countable dense subset, since each finite scalar combination is approximated by rational ones in norm. The function takes values there almost everywhere. Distances $\|f-b\|$ are measurable, being pointwise limits of measurable distances. Conversely, separable range and measurable distances suffice: choose a dense sequence $b_1=0,b_2,\ldots$ in a separable closed subspace containing the range. At each point choose, from the first $N$ vectors, a nearest vector, breaking ties by the smallest index. The cells are measurable finite intersections of comparisons between distances. Write the resulting finite-valued function as $q_N$. Then

\[
 q_N\longrightarrow f,\qquad
 \|q_N-f\|\leq\|f\|,\qquad \|q_N\|\leq2\|f\|.
 \tag{1}
\]

Density proves the limit; the zero candidate proves the first inequality. This also proves that pointwise almost-everywhere norm limits of strongly measurable functions are strongly measurable: use the closed span of their countably many approximating values, and the pointwise limits of distances. Finite sums and bounded continuous linear images have the same property.

If $\int\|f\|<\infty$, scalar dominated convergence applied to (1) gives $\int\|q_N-f\|\to0$. Every nonzero value $b_j$ of $q_N$ occurs on a set $E$ of finite measure, since on that cell $\|f\|\geq\|b_j\|/2$, so

\[
 |E|\leq \frac{2}{\|b_j\|}\int_E\|f\|<\infty.
 \tag{2}
\]

The zero cell contributes nothing and is omitted. Thus integrable simple functions are dense in $L^1(B)$ in the original norm. On a time interval, finite-measure sets can first be truncated to a bounded interval and approximated in measure by finite unions of intervals. Continuous scalar functions with bounded support approximate their indicators in $L^1$, by shrinking transition intervals at the endpoints. Applying this to the finitely many values of a simple function proves density of finite sums $\sum_j\phi_j(t)b_j$, with continuous compactly supported $\phi_j$, in $L^1(dt;B)$. For the smooth version use the proved step function $\Theta$ in [Smooth flat cutoffs, (EF16)–(EF18)](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs). On a bounded interval $(c,d)$, for $0<\delta<(d-c)/2$ the function
\[
 \Theta\bigl((t-c)/\delta\bigr)
 \Theta\bigl((d-t)/\delta\bigr)
 \tag{VI1}
\]
is smooth, vanishes outside $[c,d]$, equals one on $[c+\delta,d-\delta]$ and lies between zero and one. Its $L^1$ distance from the interval indicator is at most $2\delta$. For an open time interval $J$, first restrict to a compact subinterval in its interior, losing arbitrarily little of the integral of $\|f\|$. Intersect the finitely many approximating intervals with a slightly larger compact subinterval of $J$; their error against the truncated set cannot increase. Formula (VI1), followed by the finite vector sum, then has compact support in $J$ and arbitrarily small error. This proves density with smooth $\phi_j$ as well, without assuming a mollifier theorem.

For later use, $L^1(B)$ is complete. From a Cauchy sequence choose a subsequence with consecutive $L^1$ distances at most $2^{-j}$. Scalar monotone convergence shows that the sum of its pointwise consecutive norm differences is integrable and therefore finite almost everywhere. Completeness of $B$ supplies the pointwise vector limit there. It is strongly measurable by the preceding closure argument, and its norm is bounded by the integrable sum of the first member's norm and all consecutive differences. The norm of its difference from the $j$th subsequence member has integral at most $\sum_{k\geq j}2^{-k}$. The Cauchy property then gives convergence of the entire original sequence.

<a id="bochner-integral"></a>

## 2. Bochner integral, norm and bounded maps

For a finite-valued integrable function $q=\sum_j b_j1_{E_j}$ with disjoint cells, omit the zero cells and define

\[
 I(q)=\sum_{b_j\ne0}|E_j|b_j,
 \qquad \|I(q)\|\leq\int\|q\|.
 \tag{3}
\]

Refining cells by their intersections proves independence of the representation and linearity. The same refinement gives $\|I(q)-I(r)\|\leq\int\|q-r\|$. For strongly measurable $f$ with integrable norm, choose the approximation in Section 1 and set $\int f=\lim_N I(q_N)$. The difference bound makes this sequence Cauchy in $B$. It also proves independence of the approximation, almost-everywhere invariance, linearity, and

\[
 \left\|\int f\right\|\leq\int\|f\|,
 \qquad
 \left\|\int f-\int g\right\|\leq\int\|f-g\|.
 \tag{4}
\]

This is the Bochner integral. Conversely an $L^1$ limit of integrable simple functions has a strongly measurable representative: pass to a subsequence with summable consecutive errors and use the pointwise-limit argument in Section 1. It has integrable norm, by $\|f\|\leq\|f-q_N\|+\|q_N\|$. Thus strong measurability and integrable norm are exactly its existence criterion here.

If $T:B\to C$ is bounded linear between Banach spaces, then $Tf$ is strongly measurable, $\int\|Tf\|\leq\|T\|\int\|f\|$, and

\[
 T\int f=\int Tf.
 \tag{5}
\]

The identity holds for each finite sum; (4) and boundedness pass to the limit. This includes fixed Hilbert pairings $x\mapsto(x,y)$, inclusions of complete graph-norm spaces, and coordinate multiplication viewed as a bounded map from the first-moment space to $L^2$.

If each $f_N$ is strongly measurable, $f_N\to f$ in norm almost everywhere and $\|f_N\|\leq g$ for one nonnegative integrable scalar function $g$, the limit is strongly measurable and $\|f\|\leq g$. Scalar dominated convergence applied to $\|f_N-f\|\leq2g$ proves

\[
 \int\|f_N-f\|\longrightarrow0,
 \qquad \int f_N\longrightarrow\int f.
 \tag{6}
\]

This is vector dominated convergence with its norm hypothesis. Strong $L^1$ convergence also passes integrals by (4), without a pointwise domination assumption.

For integrable $f$ on a half-line, the finite-interval integrals have a limit because their differences are bounded by integrals of $\|f\|$ over the intervening tails. Hence the improper vector integral exists in $B$, and its tail norm is at most the corresponding scalar tail integral.

## 3. Scalar and vector fundamental theorem

We first establish the one-dimensional differentiation step, so that an integrable forcing has an almost-everywhere **norm** derivative.

<a id="scalar-lebesgue-points"></a>

### Scalar Lebesgue points

For $a\in L^1(\mathbb R)$ let $Ma(x)$ be the supremum of averages of $|a|$ over all open bounded intervals containing $x$. The set $\{Ma>\lambda\}$ is the union of intervals whose average exceeds $\lambda$, so it is open. For a compact subset select a finite such cover. Choose successively an interval of greatest remaining length and discard those meeting it. The selected intervals are disjoint, and each discarded interval lies in the interval with the same center and three times the length of the selected interval that discarded it. Therefore

\[
 |\{Ma>\lambda\}|\leq\frac{3}{\lambda}\|a\|_1.
 \tag{7}
\]

Indeed the compact-set measure is at most three times the sum of selected lengths, each length is less than its $|a|$ integral divided by $\lambda$, and those integrals sum to at most $\|a\|_1$. An open set $G$ is exhausted by the compact sets $[-n,n]\cap\{\operatorname{dist}(x,\mathbb R\setminus G)\geq1/n\}$; if $G=\mathbb R$, use $[-n,n]$. Scalar monotone convergence therefore proves (7).

For $a\in L^1(\mathbb R)$ and continuous compactly supported $b$,

\[
 \limsup_{r\downarrow0}\frac1{2r}
 \int_{x-r}^{x+r}|a(t)-a(x)|\,dt
 \leq M(a-b)(x)+|a(x)-b(x)|.
 \tag{8}
\]

The continuous $b$ contributes zero in the limit. For fixed $\varepsilon>0$, the set where the left side is greater than $2\varepsilon$ lies in $\{M(a-b)>\varepsilon\}\cup\{|a-b|>\varepsilon\}$. Its outer measure is at most $4\|a-b\|_1/\varepsilon$, by (7) and the elementary bound $\varepsilon|\{|a-b|>\varepsilon\}|\leq\|a-b\|_1$. The scalar density argument in Section 1 makes this arbitrarily small. A countable union over positive rational $\varepsilon$ proves that the left side of (8) is zero almost everywhere. Truncation to successively larger compact time intervals proves the local version for $a\in L^1_{\rm loc}$, and real and imaginary parts prove the complex version. This is the scalar Lebesgue-point theorem used below.

<a id="norm-lebesgue-points"></a>

### Norm Lebesgue points

Let $f\in L^1_{\rm loc}(J;B)$ on an open interval $J$. Work on one compact subinterval at a time. Choose a dense sequence $(b_j)$ in a separable closed subspace containing its essential range. Apply the scalar theorem to all functions $\|f-b_j\|$. Outside the union of their null exceptional sets, for every $j$,

\[
 \begin{aligned}
 \limsup_{r\downarrow0}\frac1{2r}
  \int_{t-r}^{t+r}\|f(q)-f(t)\|\,dq
 &\leq \lim_{r\downarrow0}\frac1{2r}
  \int_{t-r}^{t+r}\|f(q)-b_j\|\,dq
       +\|f(t)-b_j\|\\
 &=2\|f(t)-b_j\|.
 \end{aligned}
 \tag{9}
\]

Let $b_j$ approach $f(t)$. The left side is zero. A countable compact-interval exhaustion gives one null exceptional set in $J$. Each one-sided interval of length $|h|$ has at most twice its symmetric average, so the same conclusion holds for the averages from $t$ to $t+h$, for either sign of $h$.

<a id="compact-scalar-calculus"></a>
### Compactness and the scalar mean-value step

The compactness of a closed finite-dimensional box was proved in the [Euclidean construction](finite-derivative-l2.md#euclidean-products) by nested subdivision. A closed subset of such a box is compact: add its open complement to a cover and take a finite subcover. A continuous map takes a compact set to a compact set, by pulling back an open cover. In particular a continuous real function on a nonempty compact set is bounded: the preimages of $(-j,j)$ form an increasing open cover. It attains its supremum, because the nonempty nested closed sets where its value is at least the supremum minus $1/j$ have nonempty intersection. Otherwise their open complements would have a finite subcover, contradicting nonemptiness of the last of those nested sets. Applying this to the negative function gives a minimum.

A compact subset $K$ of a normed space is closed: for $x\notin K$, cover $K$ by balls $B(y,|x-y|/3)$, take a finite subcover, and choose the minimum of the corresponding radii as a positive radius around $x$ disjoint from those balls. Thus $x$ has a neighborhood avoiding $K$. For a nonempty set $E$, the triangle inequality followed by taking infima gives $|\operatorname{dist}(x,E)-\operatorname{dist}(y,E)|\le|x-y|$. The distance to a closed set is positive at each exterior point because its complement is open. A compact set disjoint from that closed set therefore has a positive minimum distance, by the attained-minimum argument above.

A continuous map from a compact set into a normed space is uniformly continuous. Given $\varepsilon>0$, at each point choose a radius on whose twice-larger ball the difference from the center value is below $\varepsilon/2$. Take a finite subcover by the smaller balls and let $\delta$ be their smallest radius. Points of the compact set less than $\delta$ apart lie together in one of the twice-larger balls; the triangle inequality bounds their image difference by $\varepsilon$. The same compactness argument bounds its norm.

Finally, a differentiable real function has derivative zero at an interior extremum: its positive and negative difference quotients have opposite weak signs, so a common limit must be zero. For a continuous function on $[a,b]$, differentiable on $(a,b)$, subtract the straight chord. The remainder has equal endpoint values. If it is nonconstant, its attained maximum or minimum lies in the interior; if constant, its derivative is already zero everywhere. This proves the scalar mean-value theorem and in particular that an everywhere zero derivative forces constancy. These arguments precede the fundamental theorem below and use no change of variables or Fourier calculation.

<a id="continuous-primitives"></a>
### Norm primitive and continuous derivative

For the coordinate reading, the continuous real scalar case can be obtained directly from the already constructed scalar integral. A continuous function on a compact interval is measurable (preimages of open sets are open), bounded and hence integrable. If $f$ is continuous and $P(t)=\int_{t_0}^t f(q)\,dq$, scalar additivity and the integral inequality give
\[
 \left|\frac{P(t+h)-P(t)}h-f(t)\right|
 \le \sup_{|q-t|\le|h|}|f(q)-f(t)|.
\]
The right side tends to zero, so $P'=f$. If $u$ is continuously differentiable, apply this to $f=u'$; the mean-value theorem just proved makes $u-P$ constant. This proves the scalar case of (13) directly from measure integration and compact scalar calculus. Apply it to real and imaginary parts for complex scalars, or to finitely many real components when needed for coordinate maps. No Banach-dual representation is needed in this scalar application.

<a id="vector-primitives"></a>

Fix $t_0\in J$ and define oriented integrals by $\int_b^a=-\int_a^b$. Put

\[
 F(t)=\int_{t_0}^t f(q)\,dq.
 \tag{10}
\]

On each finite interval, integrability of $\|f\|$ implies absolute continuity of its integral: choose $R>0$ with $\int_{\{\|f\|>R\}}\|f\|<\varepsilon/2$, and then every measurable set of length below $\varepsilon/(2R)$ has integral below $\varepsilon$ (the zero-function case is immediate). For disjoint intervals $(a_j,b_j)$, (4) gives

\[
 \sum_j\|F(b_j)-F(a_j)\|
 \leq\int_{\bigcup_j(a_j,b_j)}\|f\|.
 \tag{11}
\]

Thus $F$ is locally absolutely continuous in the Banach norm. At each norm Lebesgue point, (4) and (9) give

\[
 \left\|\frac{F(t+h)-F(t)}h-f(t)\right\|
 \leq\frac1{|h|}\int_{\min(t,t+h)}^{\max(t,t+h)}
                          \|f(q)-f(t)\|\,dq\longrightarrow0.
 \tag{12}
\]

Hence $F'=f$ in norm almost everywhere. If $f$ is continuous, the last error is at most $\sup_{|q-t|\leq|h|}\|f(q)-f(t)\|$, so the derivative exists at every interior point. If $u$ is continuously norm differentiable, $u-\int_{t_0}^t u'$ has zero derivative everywhere. Apply a bounded linear functional and the real scalar mean-value theorem to its real and imaginary parts: each pairing is constant. The compactness and mean-value proof immediately above supplies that scalar step. The separation proof above now gives

\[
 u(t)-u(t_0)=\int_{t_0}^t u'(q)\,dq.
 \tag{13}
\]

Taking $B=\mathbb R$ or $\mathbb C$ proves the corresponding scalar fundamental theorem, including integrable primitives.

<a id="distributional-primitives"></a>

### Continuous distributional solution and its primitive

For a scalar test $\phi\in C_c^\infty(J)$, choose $a$ below its support and rewrite $F(t)$ as a constant plus $\int_a^t f(q)\,dq$. For a bounded linear functional $\ell$, the scalar double integral is absolutely integrable, bounded by a fixed finite-interval $L^1$ norm of $f$ times a bound for $\phi'$. Scalar Fubini and $\int_q^\infty\phi'(t)\,dt=-\phi(q)$ give

\[
 -\int_J \ell(F(t))\phi'(t)\,dt
       =\int_J\ell(f(t))\phi(t)\,dt.
 \tag{14}
\]

Suppose a continuous $u:J\to B$ has distributional derivative $f\in L^1_{\rm loc}(J;B)$ in all bounded scalar pairings. The continuous scalar function $\ell(u-F)$ has zero distributional derivative. To see explicitly that it is constant, choose a nonnegative smooth $\rho$ supported in $[-1,1]$ with integral one from [the normalized flat bump construction](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs). For $x\in J$ and $0<\varepsilon<\operatorname{dist}(x,\mathbb R\setminus J)$, put $\rho_{x,\varepsilon}(t)=\varepsilon^{-1}\rho((t-x)/\varepsilon)$, taking any positive $\varepsilon$ if $J=\mathbb R$. The scalar linear substitution proved in the [coordinate integral](coordinate-inverses-and-integration.md#coordinate-integration) gives integral one. Fix one such function as $\vartheta$. Any smooth compactly supported $\psi$ with integral zero is the derivative of the compactly supported smooth function $t\mapsto\int_{-\infty}^t\psi$. Thus its pairing with $\ell(u-F)$ is zero. Subtracting $(\int\phi)\vartheta$ from an arbitrary test gives the constant distribution with value $\int\ell(u-F)\vartheta$. For the continuous scalar function $k=\ell(u-F)$, testing with $\rho_{x,\varepsilon}$ gives that same constant, while
\[
 \begin{aligned}
 &\left|\int_J k(t)\rho_{x,\varepsilon}(t)\,dt-k(x)\right|\\
 &\qquad\le \sup_{|t-x|\le\varepsilon}|k(t)-k(x)|\longrightarrow0.
 \end{aligned}
 \tag{VI2}
\]
Thus the equality holds pointwise. Therefore every $\ell(u-F)$ is constant, and separation of points yields

\[
 u(t)=u(t_0)+\int_{t_0}^t f(q)\,dq.
 \tag{15}
\]

In particular $u$ is locally absolutely continuous and has norm derivative $f$ almost everywhere. This assertion starts with a distributional derivative. Merely vanishing pointwise derivative almost everywhere, without this distributional or primitive condition, is not its hypothesis.

<a id="operator-products"></a>

## 4. Operator products and integrable forcing

Let $K(t):B\to C$ be strongly continuous and locally bounded in operator norm. For a finite-valued $h_N$, each $K(t)h_N(t)$ is a finite sum of indicators times continuous vector orbits. A continuous Banach-valued function on an interval has separable range, since rational times are dense, and measurable distances; Section 1 gives its strong measurability. Pointwise approximation of $h$ and the bound on $K$ now show that $K(t)h(t)$ is strongly measurable. If $h$ is locally integrable, so is this product, with

\[
 \int_I\|K(t)h(t)\|\,dt
       \leq \sup_{t\in I}\|K(t)\|\int_I\|h(t)\|\,dt.
 \tag{16}
\]

For a uniformly bounded family on a half-line the same proof applies globally. Unitary orbits have $\|K(t)h(t)\|=\|h(t)\|$. These are vector integrals; strong continuity of $K$ alone supplies no operator-norm measurability into $\mathcal B(B,C)$.

Let $T(t):B\to C$ be continuously differentiable in operator norm locally and let $u(t)=u(a)+\int_a^t g$, with $g\in L^1(I;B)$. Approximate $g$ in $L^1$ by the continuous finite-vector sums of Section 1, and put $u_N(t)=u(a)+\int_a^t g_N$. Equation (4) gives uniform convergence $u_N\to u$. To differentiate the product, split its increment as $(T(t+h)-T(t))u_N(t+h)+T(t)(u_N(t+h)-u_N(t))$. Divide by $h$ and use operator-norm differentiability and the continuity of $u_N$ to get $(Tu_N)'=T'u_N+Tg_N$; (13) integrates it. The two derivative terms converge in $L^1$, since $T,T'$ are bounded on $I$. Passing their integrals to the limit proves

\[
 T(t)u(t)-T(a)u(a)
       =\int_a^t\bigl(T'(q)u(q)+T(q)g(q)\bigr)\,dq.
 \tag{17}
\]

The right side is an integrable primitive. It proves local absolute continuity and the product rule in norm almost everywhere, with every operator in its actual order. A fixed bounded map is the case $T'=0$, so it also commutes with the primitive and its norm derivative. This applies to coordinate multiplication as a map from the complete first-moment space; multiplication by an unbounded coordinate is not treated as bounded on unweighted $L^2$. The graph-domain product derivative for the unitary groups in the truncation lesson is proved there first; (13) then integrates its continuous $L^2$-valued derivative. Those groups are not assumed differentiable in operator norm.

<a id="operator-propagators"></a>

## 5. The exact variation and tail receivers

We first prove the operator existence statements independently of the later evolution lessons. For Banach spaces $B,C$, the space $\mathcal B(B,C)$ is complete in operator norm. Indeed an operator-norm Cauchy sequence $T_n$ is uniformly bounded: its tail lies within one of a fixed $T_N$, and only finitely many earlier norms remain. For each $x$, completeness of $C$ gives $Tx=\lim_nT_nx$. Passing finite linear combinations and the common norm bound to the limit makes $T$ bounded linear. If $\|T_n-T_m\|\le\varepsilon$ for $n,m\ge N$, take $m\to\infty$ pointwise to get $\|(T_n-T)x\|\le\varepsilon\|x\|$. Taking the supremum over the unit ball proves operator-norm convergence. Also $\|ST\|\le\|S\|\|T\|$ follows by applying both bounds to each vector; this proves continuity of composition whenever the two factors are locally bounded.

Let $A:J\to\mathcal B(B)$ be continuous in operator norm, with $B$ real or complex. On a compact interval $I\subset J$ fix $a\in I$ and $K=\sup_I\|A\|<\infty$. Set $P_0(t,a)=I_B$ and inductively
\[
 \begin{aligned}
 P_{j+1}(t,a)&=\int_a^t A(q)P_j(q,a)\,dq,\\
 \|P_j(t,a)\|&\le\frac{K^j|t-a|^j}{j!}.
 \end{aligned}
 \tag{VI3}
\]
Continuity of each integrand, the operator-space completeness just proved and Sections 1–3 construct the integral and its continuous derivative. The norm bound follows by induction from (4); the integral of $|q-a|^j$ on the segment between $a$ and $t$ is $|t-a|^{j+1}/(j+1)$ by the scalar fundamental theorem, for either order of the endpoints. The nonnegative scalar series $\sum_j(K\operatorname{diam}I)^j/j!$ converges by the [factorial-series proof of the exponential](elementary-functions-and-cutoffs.md#scalar-exponential). Thus the tails of $\sum_jP_j$ tend to zero uniformly in operator norm. Completeness gives its continuous sum $U(t,a)$: continuity follows by bounding two tails uniformly and then using continuity of a finite sum. The bound (4), with interval length times $K$, passes this uniform limit through the integral. Consequently
\[
 \begin{aligned}
 U(t,a)&=I_B+\int_a^t A(q)U(q,a)\,dq,\\
 \partial_tU(t,a)&=A(t)U(t,a),\\
 \|U(t,a)\|&\le e^{K|t-a|}.
 \end{aligned}
 \tag{VI4}
\]
The derivative follows from the continuous-integrand assertion (12). The estimates apply also when $K=0$.

For uniqueness, if two continuous solutions with the same initial operator differ by $D$, let $L=\sup_I\|D\|$. Iterating their difference equation gives $\|D(t)\|\le L K^n|t-a|^n/n!$ for every $n$, by the same induction as (VI3). The right side tends to zero since it is a term of a convergent nonnegative series. The same proof works for vector solutions and any initial value. In particular $U(t,s)U(s,a)$ and $U(t,a)$ solve the same operator equation and agree at $t=s$, so
\[
 \begin{aligned}
 U(t,s)U(s,a)&=U(t,a),\\
 U(a,t)&=U(t,a)^{-1},\\
 \partial_tU(a,t)&=-U(a,t)A(t).
 \end{aligned}
 \tag{VI5}
\]
For the last assertion put $V(t)=U(a,t)$. Its norm is locally bounded by (VI4). The identity
$V(t+h)-V(t)=-V(t+h)(U(t+h,a)-U(t,a))V(t)$ first proves continuity of $V$, and then, after division by $h$, its derivative $-V(t)\partial_tU(t,a)V(t)=-V(t)A(t)$. Overlapping compact intervals give the same operators by uniqueness. This constructs the two-time propagator on all of $J$.

In a complex Banach space take $A=iM$, with $M$ locally norm-continuous. The preceding construction supplies exactly the norm-valued propagator for the following variation formula.

<a id="variation-of-constants"></a>

For its propagator $U(t,a)$ and $h\in L^1(I;B)$, use (16) to define

\[
 z(t)=v_0+i\int_a^t U(a,q)h(q)\,dq,
 \qquad v(t)=U(t,a)z(t).
 \tag{18}
\]

The product rule (17) gives $v'=i(Mv+h)$ almost everywhere. The bounded-map identity (5) and the composition law give exactly

\[
 v(t)=U(t,a)v_0+i\int_a^t U(t,q)h(q)\,dq.
 \tag{19}
\]

A continuous distributional solution has the same integral derivative by (15). The inverse composition law and differentiation of $U(a,t)U(t,a)=I$ give $\partial_tU(a,t)=-iU(a,t)M(t)$. Multiplication by $U(a,t)$ and (17) therefore recovers (18), proving uniqueness. A uniform propagator bound $\|U(t,q)\|\leq C$ gives the precise estimate $\|v(t)\|\leq C(\|v_0\|+\int_{\min(a,t)}^{\max(a,t)}\|h(q)\|\,dq)$ by (4).

<a id="integrable-tails"></a>

For a phase-corrected solution whose primitive derivative $w'$ is integrable on a half-line, (15) and (4) give, for $s\leq t$,

\[
 \|w(t)-w(s)\|\leq\int_s^t\|w'(q)\|\,dq.
 \tag{20}
\]

Its scalar tail tends to zero. For a half-line $[a,\infty)$, choose any sequence $t_n\to\infty$; (20) makes $w(t_n)$ Cauchy, hence convergent in $B$. Comparing an arbitrary sufficiently large $t$ to a still larger $t_n$ in (20) gives the same limit for all real times and bounds the distance to it by $\int_t^\infty\|w'\|$. Reversing the order of time proves the left-half-line version. Strong $L^1$ approximation of forcing is enough for the variation integrals by (4) and the stated propagator bound. For compact $\mathcal K\subset L^1([a,\infty);B)$ and $\varepsilon>0$, finitely many $L^1$ balls of radius $\varepsilon/2$ cover $\mathcal K$. For each of their centers choose a tail with norm integral below $\varepsilon/2$, and take the greatest of the finitely many cutoffs. Every member of $\mathcal K$ then has tail integral below $\varepsilon$ by the triangle inequality. The same proof applies to a left half-line. This is the convergence mechanism in the truncation and amplitude lessons.

For $a\leq s$, the Fubini step in the first-moment estimate is scalar Tonelli:

\[
 \int_a^s\int_a^t\|h(q)\|\,dq\,dt
       =\int_a^s(s-q)\|h(q)\|\,dq.
 \tag{21}
\]

Likewise, coefficient-product bounds and null energy slices in the following lessons use nonnegative scalar functions. The variation argument (18)–(19) needs no interchange of two vector integrals. This provider therefore supplies no additional vector Fubini contract and makes no claim about arbitrary completed products.

<a id="6-freely-accessible-source-correspondence"></a>

## 6. Further reading

These are standard arguments reconstructed in the displayed Banach norms. Van Neerven's [Integration in Banach spaces, Lecture 1](https://ocw.tudelft.nl/wp-content/uploads/Lecture01_01.pdf#page=8), Definition 1.15 and Proposition 1.16, pp. 8–9, supply the simple-approximation integral construction; Proposition 1.18 and the following bounded-map identity, p. 10, supply its convergence and linear-map rules. Section 2 writes the relevant proofs out.

Bulíček et al., [Úvod do moderní teorie parciálních diferenciálních rovnic](https://www.karlin.mff.cuni.cz/~mbul8060/moderni_teorie.pdf#page=201), 30 May 2018, Theorem 5.2.10, p. 201, supplies the countable-distance Lebesgue-point argument. Its Appendix A.3.4, Theorems A.3.19–A.3.22, pp. 292–294, supplies scalar differentiation. Section 3 gives the one-dimensional proof needed here. Definition 5.3.1, Proposition 5.3.2, Corollaries 5.3.4–5.3.5 and Proposition 5.3.10, pp. 208–211, give the primitive and distributional correspondence. In using those proofs, (9) retains the factor $2$ dropped in the last estimate of the printed vector Lebesgue-point proof, and (14) uses a direct scalar Fubini computation that fixes the shifted-variable sign slip in the printed primitive calculation. The zero-derivative conclusion here explicitly retains the distributional hypothesis.

Only the stated integration receiver is discharged. The scalar measure prerequisites above remain explicit; no general measure-theory foundation, Radon–Nikodym property, generic vector product theorem or unrelated scattering prerequisite is claimed here.
