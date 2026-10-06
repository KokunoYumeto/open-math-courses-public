# Analytic foundations for preparation

**Human source and terms.** The preparation construction discussed here is Jean-Pierre Demailly's treatment in the freely available author version of [*Complex Analytic and Differential Geometry*, 21 June 2012, Chapter II, Section 2.A, printed pages 79–81](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=79). His [OpenContent grant](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html) permits web distribution and modification while preserving his authorship. This supplementary reading retains that custom grant and is excluded from the course's CC0 dedication. Adapted and expanded by GPT-6 Astra (OpenAI), 4 October 2026. Self-checked by the writing AI. 

Read this before the programme's Weierstrass division and analytic preparation readings, and before [quantitative polynomial growth](quantitative-polynomial-growth.md). We prove the zero-counting, root-continuity, symmetric-function and parameter-integral facts that those arguments need. In particular, a reference to the argument principle or to joint analyticity is not being used in place of a proof.

The earlier scalar inputs are proved in *Cauchy's theorem for cycles and its consequences*: Theorems 2.1–2.3 give Goursat's triangle argument, primitives on a convex domain and Cauchy's formula; Lemma 3.1 and Theorem 3.2 give convergent power series and Cauchy's coefficient estimates; Theorems 3.3, 3.6 and 3.7 prove Liouville, the maximum modulus principle and the identity theorem. Exercise 1, including its solution, proves the fundamental theorem of algebra from Liouville. Only these scalar sections are used. The global cycle theorem and the Banach-valued extension are not inputs here. 

<a id="analytic-algebra"></a>
## 1. Power series, units and real branches

An analytic germ in finitely many variables is a power series absolutely convergent on some polydisc. On every strictly smaller closed polydisc, the series and each differentiated series converge uniformly: a derivative introduces a fixed polynomial in the indices, which is summable against the geometric ratio between the two radii. Products may therefore be rearranged absolutely. Substitution of analytic germs is legitimate after shrinking until the sums of absolute values of the inner series lie strictly within the convergence polydisc of the outer series. The resulting majorant is the absolutely convergent outer series evaluated at those sums. This proves that the substitution defines an analytic germ.

If $h(0)\ne0$, write $h=h(0)(1+k)$ with $k(0)=0$. Shrink until the sum of the absolute values of the series for $k$ is less than one. The geometric series
\[
 h^{-1}=h(0)^{-1}\sum_{j\ge0}(-k)^j
 \tag{AF1}
\]
converges absolutely there, and its product with $h$ is one. Thus a nonvanishing analytic germ has an analytic reciprocal. A real analytic series extends to the complex polydisc with the same coefficients and a smaller radius. Restriction back to real points recovers the original function. Conversely, a complex analytic function fixed by coefficientwise conjugation has real Taylor coefficients and a real analytic restriction.

For a rational number $\alpha=p/q$ with integers $p$ and $q>0$, define $c_0=1$ and $c_{j+1}=(\alpha-j)c_j/(j+1)$. The series $B(t)=\sum c_jt^j$ converges absolutely for $|t|<1$ (or terminates), by the ratio test, and its coefficients give
$(1+t)B'(t)=\alpha B(t)$, $B(0)=1$. Differentiating with integer powers shows that $B(t)^q(1+t)^{-p}$ has derivative zero on the real interval $(-1,1)$; it is one at zero. Hence $B(t)^q=(1+t)^p$. It never vanishes on that interval and starts positive, so by continuity it is the positive real branch $(1+t)^{p/q}$. If $a>0$, the same argument gives $(a+t)^\alpha=a^\alpha B(t/a)$ on $|t|<a$. These formulas prove the reciprocal and rational-power branch statements used in the preparation proof, always on neighborhoods where their positive base stays away from zero.

A nonzero complex polynomial cannot vanish at every point of $\mathbb R^d$: fix all but one real variable, compare its one-variable coefficients, and repeat in the remaining variables. The same assertion holds on any real open box by the identical argument. A finite product of nonzero polynomials is nonzero: order monomials lexicographically and multiply their leading terms. Hence finitely many nonzero homogeneous polynomials admit a common real vector where all are nonzero. Completing that vector to a real basis gives an invertible real linear change of variables. Its substitution preserves analytic convergence by the preceding majorant argument. This justifies simultaneous regular coordinate directions for finitely many real analytic germs, as well as the complex version.

<a id="zero-counting"></a>
## 2. Removable zeros and the argument principle on a disc

First suppose $f$ is holomorphic and bounded by $M$ on $0<|z-a|<r$. Define $H(z)=(z-a)^2f(z)$ away from $a$ and $H(a)=0$. Then $H$ is continuous at $a$ and
\[
 \frac{H(a+h)-H(a)}h=h f(a+h)\longrightarrow0.
\]
It is holomorphic throughout the disc and has $H(a)=H'(a)=0$. The earlier Taylor theorem therefore gives $H(z)=(z-a)^2F(z)$ with $F$ holomorphic, and $F=f$ off $a$. This proves the bounded removable-singularity assertion without assuming a Laurent expansion.

If a holomorphic $f$ is not identically zero on a connected domain, the identity theorem and its Taylor proof show that each zero has a finite multiplicity: locally
$f(z)=(z-a)^m v(z)$ with $m\ge1$ and $v(a)\ne0$. Its zeros are isolated. Suppose now that $f$ is holomorphic on a neighborhood of $\{|z-c|\le r\}$ and nonzero on the boundary circle. There are only finitely many zeros inside: infinitely many would accumulate in this compact disc, contradicting either the boundary nonvanishing or the identity theorem. List them as $a_1,\ldots,a_N$, with multiplicities $m_1,\ldots,m_N$. Removing their Taylor factors gives
\[
 f(z)=v(z)\prod_{\nu=1}^N(z-a_\nu)^{m_\nu},
 \tag{AF2}
\]
where $v$ is holomorphic and nonzero on a neighborhood of the closed disc, after shrinking that neighborhood if necessary. Thus $v'/v$ is holomorphic there by (AF1). Logarithmic differentiation and Cauchy's formula imply, for every polynomial $h$,
\[
 \frac1{2\pi i}\int_{|z-c|=r}h(z)\frac{f'(z)}{f(z)}\,dz
 =\sum_{\nu=1}^N m_\nu h(a_\nu).
 \tag{AF3}
\]
Indeed, the $h v'/v$ term has integral zero by Cauchy's theorem on a slightly larger disc, and each $h(z)/(z-a_\nu)$ term has integral $2\pi i h(a_\nu)$. For $h=1$, (AF3) is the argument principle needed here. It counts multiplicity. For $h(z)=z^j$ it proves the power-sum formula, including repeated zeros. No meromorphic residue theorem is an additional input.

<a id="root-continuity"></a>
## 3. Stable zero counts and continuity of root multisets

Let $f_u(z)$ and $\partial_zf_u(z)$ depend continuously on a parameter $u$, uniformly for $z$ on a fixed circle, and suppose each $f_u$ is holomorphic on a neighborhood of its closed disc. If $f_{u_0}$ has no boundary zero, its boundary minimum is positive. Uniform continuity preserves a positive lower bound for $u$ near $u_0$. The integral in (AF3) with $h=1$ then depends continuously on $u$. It is an integer, so it is locally constant. This proves stable zero counts directly.

Apply this separately to disjoint small discs around the distinct roots of a monic degree-$s$ polynomial $p_{u_0}$ with continuously varying coefficients. The polynomial and its derivative vary uniformly on each of their boundary circles. For nearby $u$, each small disc contains exactly the multiplicity of its central root at $u_0$. All roots of $p_u$ lie in a common large disc: if
$p_u(z)=z^s+b_1(u)z^{s-1}+\cdots+b_s(u)$ and $M\ge\max_j|b_j(u)|$, then for $|z|>1+M$,
\[
 \left|\sum_{j=1}^s b_j(u)z^{s-j}\right|
 \le M\sum_{j=0}^{s-1}|z|^j<|z|^s.
 \tag{AF4}
\]
The polynomial has exactly $s$ complex roots with multiplicity by the earlier fundamental theorem of algebra and successive polynomial division. The counts in the small discs already sum to $s$, so there are no others. As their radii can be arbitrarily small, this proves continuity of the root multiset. It does not assume continuously labelled roots on an arbitrary parameter space, and it does not assume holomorphic labels at multiple roots.

The same counting argument applies to an analytic family $g(u,z)$ on a fixed disc whose boundary is zero-free. Choosing disjoint circles around the finitely many zeros at $u_0$ shows that nearby fibre zeros, with multiplicities, remain in those circles, and that their total number is unchanged. In particular, if $g(0,z)$ has its only zero at zero in the chosen disc, all these zeros approach zero as $u\to0$.

<a id="newton-identities"></a>
## 4. Newton's identities, without choosing root branches

For an unordered list $a_1,\ldots,a_s$, including repetitions, put $S_j=\sum_\nu a_\nu^j$, $e_0=1$ and
\[
 E(t)=\prod_{\nu=1}^s(1-a_\nu t)
      =\sum_{k=0}^s(-1)^k e_k t^k.
\]
Near $t=0$ all denominators are nonzero, and finite logarithmic differentiation followed by geometric series gives
\[
 -t E'(t)=E(t)\sum_{j\ge1}S_jt^j.
\]
Comparing coefficients of $t^k$, for $1\le k\le s$, yields
\[
 k e_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}S_j.
 \tag{AF5}
\]
This is a finite recursive expression for each $e_k$ as a polynomial with rational coefficients in $S_1,\ldots,S_k$. It holds with repeated or zero roots. Therefore analytic power sums imply analytic coefficients of the monic polynomial having that multiset of roots. No selection theorem for root branches is needed.

<a id="parameter-integrals"></a>
## 5. Why the parameter integrals are jointly analytic

Here is the precise uniform assertion. Let $u\in\mathbb C^d$, let $\Gamma$ be a fixed circle, and let $F(u,\zeta)$ be continuous on a neighborhood of $\{|u_i-u_i^0|\le R_i\}\times\Gamma$, and holomorphic in each $u_i$ there when all other variables are fixed. The scalar Cauchy formula applied successively in $u_1,\ldots,u_d$ gives the iterated Cauchy integral. Expanding each of its kernels geometrically gives
\[
 F(u,\zeta)=\sum_{\alpha\in\mathbb N^d}
 A_\alpha(\zeta)(u-u^0)^\alpha,
 \qquad |A_\alpha(\zeta)|\le M\prod_i R_i^{-\alpha_i},
 \tag{AF6}
\]
where $M$ is the supremum on the compact integration tori times $\Gamma$. The coefficients are continuous in $\zeta$. For $|u_i-u_i^0|\le\rho_i<R_i$, the sum of the majorants is at most $M\prod_i(1-\rho_i/R_i)^{-1}$. This proves uniform absolute convergence simultaneously in $u$ and $\zeta$. Every exchange here follows first for finite geometric sums and then from this uniform bound. Interchanging the finite-dimensional contour integrals is also justified by uniform approximation with their rectangular Riemann sums.

It follows, by termwise integration, that
\[
 u\longmapsto\int_\Gamma F(u,\zeta)\,d\zeta
 \tag{AF7}
\]
is analytic. Compactness of $\Gamma$ provides a common smaller parameter polydisc whenever $F$ is given only on a neighborhood of $\{u^0\}\times\Gamma$.

For the Cauchy extension on $\Gamma=\{|\zeta|=r\}$, also take $|w|\le b<r$ and expand
\[
 \frac1{\zeta-w}=\sum_{k\ge0}\frac{w^k}{\zeta^{k+1}}.
\]
Together with (AF6) this gives an absolutely and uniformly convergent power series in $(u-u^0,w)$ for
\[
 \frac1{2\pi i}\int_{|\zeta|=r}
       \frac{F(u,\zeta)}{\zeta-w}\,d\zeta.
 \tag{AF8}
\]
As $b$ can be any number below $r$, the extension is jointly analytic throughout the interior. The analogous expansion centered at an arbitrary interior $w^0$ follows by expanding in $(w-w^0)/(\zeta-w^0)$ on a small enough disc. This proves the joint assertion directly from scalar Cauchy formulas; a separate theorem about several complex variables is not being silently invoked.

<a id="preparation-interface"></a>
## 6. Applying the proved facts to Weierstrass preparation and division

We now check precisely the analytic interface of the earlier programme reading. Let $g(u,w)$ be an analytic germ with $g(0,w)$ of finite order $s\ge1$ at zero. Its Taylor factor is $w^s v(w)$, $v(0)\ne0$. Choose $r>0$ small enough that $v$ is nonzero on a neighborhood of $|w|\le r$. Continuity on a compact annulus about $|w|=r$ then gives a common parameter polydisc on which $g$ is nonzero on that annulus.

The case $s=0$ is immediate: $g$ is itself a unit near zero and one takes $P=1$. For real analytic $g$, use its complexification from Section 1. At real parameters its fibre roots are closed under complex conjugation with the same multiplicities. Their elementary symmetric functions are therefore real, so the resulting $P$ and $U=g/P$ restrict to real analytic functions. This provides the real division and preparation statements required by the later real-variable argument.

Equations (AF3) and (AF7) show that
\[
 S_j(u)=\frac1{2\pi i}\int_{|\zeta|=r}
        \zeta^j\frac{\partial_\zeta g(u,\zeta)}{g(u,\zeta)}\,d\zeta
 \tag{AF9}
\]
is analytic, that $S_0=s$, and that $S_j$ for $j\ge1$ is the power sum of the fibre zeros. Equation (AF5) gives analytic $e_k(u)$, with $e_k(0)=0$. Thus $P(u,w)=w^s-e_1(u)w^{s-1}+\cdots+(-1)^s e_s(u)$ has exactly the same zeros and multiplicities as $g$ inside the circle.

For each fixed $u$, cancellation of the local Taylor factors makes both $g/P$ and $P/g$ holomorphic through their apparent singularities. On the boundary annulus they already are analytic quotients. Formula (AF8), applied to each boundary quotient, supplies jointly analytic extensions to the interior. Scalar Cauchy's formula identifies them with the fibrewise extensions. Their product is one there, either by the scalar identity theorem on each fibre or by continuity at the cancelled zeros. Consequently $g=UP$ with a jointly analytic unit $U$. All assertions about multiplicity and dependence on $u$ have now been justified.

For division, take $f$ analytic on a neighborhood of a closed, smaller adapted polydisc and define
\[
 \begin{aligned}
 q(u,w)&=\frac1{2\pi i}\int_{|\zeta|=r}
     \frac{f(u,\zeta)}{P(u,\zeta)(\zeta-w)}\,d\zeta,\\
 R(u,w)&=\frac1{2\pi i}\int_{|\zeta|=r}
     \frac{f(u,\zeta)}{P(u,\zeta)}
     \frac{P(u,\zeta)-P(u,w)}{\zeta-w}\,d\zeta.
 \end{aligned}
 \tag{AF10}
\]
Equation (AF8) proves analyticity of $q$. The polynomial identity
$(\zeta^k-w^k)/(\zeta-w)=\sum_{\ell=0}^{k-1}\zeta^{k-1-\ell}w^\ell$ makes $R$ a polynomial of degree less than $s$ with analytic parameter coefficients by (AF7). Adding $Pq$ and $R$ gives $f$ by scalar Cauchy's formula. Uniqueness follows by subtracting two divisions: the difference of their remainders has all $s$ roots with multiplicity because it is holomorphically divisible by $P$, but has degree less than $s$. It must be zero by successive one-variable polynomial division, and then so must the difference of their quotients.

The estimates used in the Noetherian argument also have uniform constants. Shrink the parameter polydisc so that $|P(u,\zeta)|\ge\mu>0$ on a fixed closed annulus $r_0\le|\zeta|\le r$, while all roots lie in $|w|<r_0$. The finite polynomial quotient in (AF10) is bounded uniformly for $|w|\le r$ and $|\zeta|$ in this annulus. It follows that $|R|\le C\sup|f|$. On any circle $r_0<t<r$, the identity $q=(f-R)/P$ bounds $|q|$ by $\mu^{-1}(1+C)\sup|f|$. The proved scalar maximum modulus principle extends this bound to $|w|\le t$; increasing $t$ gives the bound on $|w|<r$. For bounded $f$ defined only on the open adapted polydisc, use contours with $t<r$. The resulting divisions agree on overlaps by the just-proved uniqueness, so the same uniform bounds and analytic functions hold throughout the open polydisc. Division by $g=UP$ replaces $q$ by $q/U$, whose analyticity and bounds follow from the proved reciprocal and the unit's positive lower bound on a smaller closed polydisc.

The remaining algebraic Noetherian and preparation arguments are the exact earlier programme proofs in *Weierstrass preparation and division* and *Analytic finiteness for preparation*. They are read after this supplement. The second reading proves its convergent Puiseux conclusion through its finite preparation induction. Neither a free primary source nor the presence of a link is a substitute for that programme proof.
