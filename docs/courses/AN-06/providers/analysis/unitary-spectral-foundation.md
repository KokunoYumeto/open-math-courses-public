# A spectral measure for a unitary operator

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This is a direct bounded foundation for [Self-adjoint spectral calculus with the original domain](self-adjoint-spectral-domains.md). It assumes no spectral theorem, Gelfand representation, general C*-algebra calculus, separability, or existence of an unbounded functional calculus. We use ordinary set theory with choice and complete real numbers. The exact earlier proof inputs are:

- Hahn–Banach and the basic Banach theorems, Section 1, Theorem 1.1: the tower proof of Zorn's lemma from choice.
- [Scalar integration and complete function spaces](finite-derivative-l2.md#measure-foundations), through the function-space lemma, and [pi-lambda uniqueness](finite-derivative-l2.md#pi-lambda-uniqueness): outer measures, convergence, finite simple approximation and complete $L^2$ on arbitrary measure spaces.
- [Elementary Hilbert tools](finite-trace-ideals.md#elementary-hilbert-tools): Cauchy–Schwarz, projection onto a closed subspace, adjoints and finite orthogonal sums. No later compact or trace-ideal theorem is used.
- [Elementary functions](elementary-functions-and-cutoffs.md), through the real-power and trigonometric proofs, and [finite-dimensional compactness and mean values](hilbert-valued-integration.md#compact-scalar-calculus): scalar limits, square roots and the circle parametrization.
- Cauchy's theorem for cycles and its consequences, Conventions and Lemma 0.1, Lemma 1.1, Theorems 2.1–2.3, Lemma 3.1, Theorem 3.2, Corollary 3.3 and Exercise 1: complete Riemann integration and parameter differentiation, the circle formula, Cauchy estimates, Liouville and polynomial factorization. The scalar proof through Liouville uses the stated integration, elementary functions and compactness inputs; it does not use the later general-cycle or Banach-valued holomorphy theorem.

 Their original notices credit Claude Opus 5.5 (Anthropic) and GPT-6.1 Sol (OpenAI) under CC0. Earlier foundation comparisons with Measure and Hilbert space tools, Sections 1–3, and Hilbert spaces and compact operators, Sections 1–3, retain their source credit; the active measure and Hilbert proof routes are the local readings linked above. The former was written by GPT-6.1 Sol. The compact positive-measure construction below is informed by Haar measure on locally compact groups, the complete six-step Theorem 2.2 and Proposition 2.3, whose notice credits Claude Opus 5.5 and GPT-6.1 Sol under CC0. Here compact metric cutoffs, representation and finite-measure regularity are proved explicitly, so the source's broader locally compact topology and arbitrary-product prerequisites are not imported.

<a id="unitary-pvm"></a>
## The theorem

For a unitary operator $U$ on an arbitrary complex Hilbert space $H$ there is exactly one orthogonal strongly countably additive PVM $F$ on the unit circle $\mathbb T$, with $F(\mathbb T)=I$ and $U=\int z\,dF(z)$. Every bounded Borel $f$ has a unital star calculus with
\[
 \|f(U)u\|^2=\int|f|^2\,d\nu_u,\qquad
 \nu_u(B)=\|F(B)u\|^2.
 \tag{1}
\]
Bounded pointwise convergence of functions gives strong convergence of their operators. The zero Hilbert space is immediate; below it may be nonseparable. Inner products are linear in the first variable.

<a id="unitary-laurent-norm"></a>
## Norm control of Laurent polynomials without a spectral theorem

The normed space $B(H)$ is complete. Indeed an operator-norm Cauchy sequence $T_j$ gives Cauchy vectors $T_jx$ for every $x$; define $Tx=\lim_jT_jx$. Passing to limits gives linearity and a uniform operator bound. For every $\varepsilon>0$, the late inequalities $\|(T_j-T_k)x\|\leq\varepsilon\|x\|$ pass to $k\to\infty$, proving $\|T_j-T\|\leq\varepsilon$. Thus the operator series and the Banach-valued integrals used below exist in this space.

For a bounded operator $T$, its resolvent set is open by the convergent geometric series for $I-(z-z_0)(T-z_0)^{-1}$. That series also proves analyticity of the inverse and gives an inverse whenever $|z|>\|T\|$. Its spectrum is therefore closed and bounded.

It is nonempty. If it were empty, the integral
\[
 I_0(R)=\frac1{2\pi i}\int_{|z|=R}(z-T)^{-1}\,dz
\]
would equal $I$ for $R>\|T\|$ by termwise integration of the uniformly convergent geometric series. It is independent of $R$ on a resolvent annulus. Indeed for holomorphic $B(z)$ on that annulus, differentiate the parametrized integral of $B(Re^{it})iRe^{it}$ with respect to $R$. The derivative of the integrand is exactly $\partial_t(e^{it}B(Re^{it}))$, whose integral is zero. Here holomorphic means differentiable in operator norm. Such a $B$ has continuous derivative: on any closed disc in its domain, apply the scalar Cauchy formula to each bounded linear functional of $B$. Bounded maps commute with the integral, and separation gives the same circle formula for $B$ itself. Expanding its kernel geometrically on a smaller disc gives a norm-convergent power series with coefficient bounds $M/r^n$, where $M$ bounds $B$ on the integration circle. The finite difference-quotient identity in Lemma 3.1, with norms in place of absolute values, proves termwise differentiation; the derivative series converges uniformly on each smaller disc. Thus the derivatives used here are continuous on every compact parameter rectangle in the annulus. Lemma 0.1(4) of the pinned Cauchy lesson therefore permits the $R$ derivative inside the $B(H)$-valued integral, and Lemma 0.1(2) makes the integral of this $t$ derivative zero by periodicity. Applying bounded linear functionals and the real mean-value theorem shows that the resulting $I_0$ is constant on each radius interval; the functionals separate points by the proved Hahn–Banach separation. Analyticity and derivative continuity of the resolvent here also follow directly from its locally uniformly convergent geometric series: on a smaller disc the termwise derivative series converges, bounded by $\sum_{j\geq1}j q^{j-1}$ with $q<1$. The ratio of consecutive terms is eventually smaller than some number less than one, so this scalar series converges. If the spectrum were empty, the resolvent would be bounded near zero, and $\|I_0(R)\|\to0$ as $R\downarrow0$, a contradiction.

Put $r(T)=\max\{|z|:z\in\sigma(T)\}$. The same annulus argument, now with $B(z)=z^m(z-T)^{-1}$, and the large-circle series give, for every $R>r(T)$,
\[
 T^m=\frac1{2\pi i}\int_{|z|=R}z^m(z-T)^{-1}\,dz,
 \qquad \|T^m\|\leq R^{m+1}\max_{|z|=R}\|(z-T)^{-1}\|.
 \tag{2}
\]
For a normal $T$, $\|T^{2^k}\|=\|T\|^{2^k}$. To check this using only Hilbert-space norms, $\|T^*T\|=\|T\|^2$: the upper bound is submultiplicativity and $\|T^*\|=\|T\|$; the lower bound follows from $\|Tu\|^2=\langle T^*Tu,u\rangle$. If $B$ is self-adjoint, this gives $\|B^2\|=\|B\|^2$. For normal $T$, $(T^2)^*T^2=(T^*T)^2$, hence $\|T^2\|=\|T\|^2$, and induction proves the powers identity. Taking $2^k$-th roots in (2) gives $\|T\|\leq R$ for every $R>r(T)$. The opposite inequality follows from the geometric series. Thus $\|T\|=r(T)$ for normal $T$, with no normal-operator theorem assumed.

A Laurent polynomial $p(U)=\sum_{j=-m}^m a_jU^j$ is normal, and
\[
 \sigma(p(U))=p(\sigma(U)),\qquad
 \|p(U)\|\leq\sup_{z\in\mathbb T}|p(z)|.
 \tag{3}
\]
For the spectral identity multiply $p(z)-\lambda$ by $z^m$ and factor the resulting polynomial over $\mathbb C$. The fundamental theorem of algebra used here is Exercise 1 of the pinned Cauchy lesson, with its full proof through Liouville: if a nonconstant polynomial had no zero, its reciprocal would be entire and bounded, since it tends to zero at infinity, and hence constant; when $p(\lambda)=0$, the finite identity $z^j-\lambda^j=(z-\lambda)\sum_{a=0}^{j-1}z^{j-1-a}\lambda^a$ factors out $z-\lambda$ term by term. Induction on degree then gives full factorization. For commuting factors their product is invertible exactly when each factor is: if the product has inverse, a factor's inverse is the product's inverse times all the other factors, and commutation gives both inverse identities. Applying this to the factorization gives the spectral identity; multiplying by $U^m$ changes no invertibility condition. A zero root of the multiplied polynomial contributes only an invertible factor $U$ and thus cannot introduce a spurious spectral value. If the multiplied polynomial is identically zero, $p$ is the constant $\lambda$; for a nonzero Hilbert space $p(U)=\lambda I$ has precisely the singleton spectrum. All constant cases are therefore included. The spectrum of $U$ lies in $\mathbb T$ by geometric series in $U$ outside the circle and in $U^*$ inside it. The normal norm identity just proved gives (3).

<a id="unitary-continuous-calculus"></a>
## Uniform density and continuous calculus

Laurent polynomials are dense in $C(\mathbb T)$. For a continuous $f$, use the Fejér averages
\[
 f_N(z)=\frac1{2\pi}\int_{-\pi}^{\pi}K_N(t)f(ze^{-it})\,dt,
 \quad K_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{ijt}\right|^2.
\]
Expanding the square shows that $K_N$ is a Laurent polynomial, nonnegative, with integral $2\pi$; expanding it in the displayed integral makes $f_N$ a Laurent polynomial in $z$. For $\delta\leq|t|\leq\pi$, the geometric-sum formula gives $K_N(t)\leq4/(N|1-e^{it}|^2)$, so its integral on that set tends to zero. On $|t|<\delta$, uniform continuity of $f$ makes $|f(ze^{-it})-f(z)|$ uniformly small. Split the integral into those two parts to obtain $\|f_N-f\|_\infty\to0$. More explicitly, putting
\[
 \begin{gathered}
 c_k=\frac1{2\pi}\int_{-\pi}^{\pi}f(e^{is})e^{-iks}\,ds,\\
 f_N(z)=\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)c_kz^k.
 \end{gathered}
 \tag{U1}
\]
gives the asserted Laurent polynomial. To verify the second identity, expand the finite square defining $K_N$: the coefficient of $e^{ikt}$ is $1-|k|/N$. For $z=e^{i\theta}$, substitute $s=\theta-t$ in each integral; the continuous integrand is $2\pi$-periodic, so its integral over any interval of length $2\pi$ is the same. Splitting and translating intervals proves that last assertion directly. The circle parametrization and its trigonometric identities were proved in the elementary reading.

Inequality (3) therefore defines $\Phi(f)=\lim p_j(U)$ for any uniformly approximating Laurent polynomials. The result is independent of the approximation. Polynomial linearity, multiplicativity, involution and the identity pass to uniform limits, so $\Phi:C(\mathbb T)\to B(H)$ is a contractive unital star homomorphism with $\Phi(z)=U$. It is positive: if $f\geq0$, its continuous real square root satisfies $\Phi(f)=\Phi(\sqrt f)^*\Phi(\sqrt f)$. This constructs every continuous input needed below.

<a id="compact-positive-measure"></a>
## Positive functionals on a compact metric space: complete measure construction

Let $K$ be compact metric and let $I:C(K)\to\mathbb C$ be positive and linear. The required metric compactness facts follow from the finite-cover definition. Continuous images of a compact set are compact by pulling back open covers; compact subsets of a metric space are closed, since a point outside one can be separated from it using a finite cover by balls of radii smaller than one third of the distances to that point. Real compact sets are bounded, and closedness and completeness make their suprema and infima belong to them. Thus continuous real functions on $K$ attain their extrema. For uniform continuity, choose for every $x$ a radius $r_x>0$ on whose doubled ball the function differs from its value at $x$ by less than $\varepsilon/2$; select finitely many undoubled balls covering $K$. If two points have distance less than the smallest selected radius, both belong to a selected doubled ball, giving the required $\varepsilon$ bound. Distance to a nonempty set is 1-Lipschitz by the triangle inequality. In particular two disjoint compact sets have positive distance: the distance to one is positive on the other and attains its positive minimum. Positivity makes its values on real functions real, by splitting into positive and negative parts. Also $|I(f)|\leq I(1)\|f\|_\infty$: rotate $I(f)$ to be nonnegative real and bound the real part of the rotated function. Thus it is bounded.

Write $f\prec V$ for $0\leq f\leq1$, continuous, with support contained in an open $V$. For compact $L\subset V$ there is such an $f$ equal to one on $L$. If $K\setminus V$ is nonempty, its distance from $L$ is positive; choose a smaller positive $d$ and use $\max(0,1-\operatorname{dist}(x,L)/d)$. For $V=K$ use one, and for $L=\varnothing$ use zero. A finite open cover of a compact $L$ admits a subordinate family $h_j\prec V_j$ with $\sum h_j=1$ on $L$ and $\sum h_j\leq1$: choose finitely many smaller closed metric balls covering $L$, group them by the assigned $V_j$, and choose cutoffs $g_j$ equal to one on those compact groups. Set $h_1=g_1$ and $h_j=g_j\prod_{i<j}(1-g_i)$. The sum is $1-\prod_j(1-g_j)$. This proves all the compact topology used in the construction.

For open $V$ put $m(V)=\sup_{f\prec V}I(f)$ and, for arbitrary $A\subset K$, put $m^*(A)=\inf_{V\supset A,\ V\text{ open}}m(V)$. Then $m^*=m$ on opens. If $V=\bigcup_jV_j$, the compact support of each $f\prec V$ is covered by a finite subfamily. The preceding partition gives $f=\sum_jfh_j$, whence $I(f)\leq\sum_jm(V_j)$. Taking suprema proves open subadditivity. Enclosing arbitrary sets in open sets with errors $\varepsilon2^{-j}$ proves that $m^*$ is an outer measure.

An open $V$ is Carathéodory-measurable. First let $A=W$ be open. Choose $f\prec W\cap V$ with $I(f)>m(W\cap V)-\varepsilon$, and $g\prec W\setminus\operatorname{supp}f$ with $I(g)>m(W\setminus\operatorname{supp}f)-\varepsilon$. Their disjoint supports make $f+g\prec W$. Hence
\[
 m(W)\geq m(W\cap V)+m^*(W\setminus V)-2\varepsilon.
\]
All terms are finite because $m(K)=I(1)$. For arbitrary $A$, choose open $W\supset A$ with $m(W)<m^*(A)+\varepsilon$ and use monotonicity. Let the error vanish. The local outer-measure lemma supplies a measure $m$ on the Borel sets, outer regular by construction.

For a compact $L$ and $f\geq1_L$, $f\geq0$, every $g\prec\{f>c\}$, $0<c<1$, is bounded by $f/c$, giving $m(L)\leq I(f)/c$ and hence $m(L)\leq I(f)$. Conversely outer regularity and the compact cutoffs give $f\geq1_L$ with $I(f)\leq m(L)+\varepsilon$. Therefore
\[
 m(L)=\inf_{f\geq1_L}I(f).
\]

The measure is finite. For open $V$, if $f\prec V$, then $I(f)\leq m(\operatorname{supp}f)$ by the outer-regular definition applied to every open neighbourhood of that support. Taking suprema proves inner regularity on open sets.

To prove representation, take $0\leq f\leq1$. Put $L_0=\operatorname{supp}f$, $L_j=\{f\geq j/N\}$, and $f_j=\min(\max(f-(j-1)/N,0),1/N)$ for $1\leq j\leq N$. Then $f=\sum_j f_j$ and
\[
 N^{-1}1_{L_j}\leq f_j\leq N^{-1}1_{L_{j-1}}.
\]
The compact formula gives $N^{-1}m(L_j)\leq I(f_j)\leq N^{-1}m(L_{j-1})$; the upper bound follows by taking all open neighbourhoods of its support. The same bounds hold for $\int f_j\,dm$. Thus $I(f)$ and $\int f\,dm$ lie between two sums differing by at most $m(L_0)/N$. Let $N\to\infty$, then use scaling and real/imaginary positive parts for arbitrary $f$. This proves $I(f)=\int f\,dm$.

Inner regularity holds on all Borel sets because the total measure is finite. For Borel $E$, choose open $V\supset E$ with $m(V\setminus E)<\varepsilon$, open $W\supset V\setminus E$ with $m(W)<\varepsilon$, and compact $L\subset V$ with $m(V\setminus L)<\varepsilon$. Then $L\setminus W\subset E$ is compact and differs from $E$ by measure less than $2\varepsilon$. This also proves continuous functions dense in $L^2(m)$: approximate by simple functions, then approximate an indicator between such a compact set and an open neighbourhood by a cutoff between zero and one. Its squared error integral is at most the measure of the difference. Uniqueness of the finite measure follows already from its continuous integrals: for an open $V$, $\min(1,k\operatorname{dist}(x,K\setminus V))$ increases to $1_V$ (take one when $V=K$), so monotone convergence gives equality on opens. The class of sets where two finite measures agree is a Dynkin class; opens are closed under finite intersections and generate the Borel sigma-algebra. The pi-lambda argument given in [the set-generation proof](finite-derivative-l2.md#pi-lambda-uniqueness) gives equality everywhere. No unproved Riesz representation or regularity assertion is left here.

<a id="unitary-cyclic-construction"></a>
## Cyclic construction and arbitrary Hilbert dimension

For $u\ne0$, let $\nu_u$ be the finite measure representing the positive functional $f\mapsto\langle\Phi(f)u,u\rangle$, just constructed. Its mass is $\|u\|^2$. The map $f\mapsto\Phi(f)u$ satisfies
\[
 \|\Phi(f)u\|^2=\langle\Phi(|f|^2)u,u\rangle=\int|f|^2\,d\nu_u.
\]
It extends by the proved continuous density and $L^2$ completeness to a unitary map $J_u:L^2(\nu_u)\to H_u$, where $H_u$ is the closed cyclic span of the Laurent polynomial vectors. Continuous multiplication corresponds to $\Phi(f)|_{H_u}$, first on continuous functions and then by density. In particular $U|_{H_u}$ is multiplication by $z$, and $U^*|_{H_u}$ multiplication by $\bar z$. The subspace reduces $U$.

Choose a maximal family of mutually orthogonal nonzero cyclic reducing subspaces, using choice in its Zorn form. A union of a chain is an upper bound, so maximality applies. The orthogonal complement of their closed direct sum reduces $U$: pair against each subspace using invariance under both $U$ and $U^*$. If it contained a nonzero vector, its cyclic space would enlarge the family. Thus $H$ is their Hilbert direct sum.

Every vector has at most countably many nonzero components: Bessel's inequality makes only finitely many component norms exceed $1/k$ for each $k$. Write $u_\alpha=P_\alpha u$ using the proved projection onto each closed summand. For every finite $A$, orthogonal expansion gives $\sum_{\alpha\in A}\|u_\alpha\|^2\leq\|u\|^2$. Enumerate the countably many nonzero components. Their tails have squared norm equal to the corresponding tails of this convergent nonnegative series, so their partial sums are Cauchy and converge in $H$, independently of enumeration; the residual is orthogonal to every summand, hence zero by the preceding maximality. This proves the direct-sum meaning without assuming separability or a countable family of cyclic spaces.

On each summand define $F(B)$ by $J_u1_BJ_u^{-1}$, and take their orthogonal direct sum. Indicators give projections and intersection products, and $F(\mathbb T)=I$. For disjoint Borel sets, multiplication by their partial-sum indicators converges strongly on each $L^2$ by dominated convergence. The same holds on the full Hilbert direct sum: its fixed vector has countably many components and their squared norms have a finite sum, so first truncate that sum and then use convergence on the finitely many retained components. This proves strong countable additivity. To spell out the multiplier argument, write $v_\alpha=J_\alpha g_\alpha$ on each summand. Then
\[
 \begin{gathered}
 \nu_v(B)=\sum_\alpha\int_B|g_\alpha|^2\,d\nu_\alpha,\\
 \|f(U)v\|^2
 =\sum_\alpha\int|f|^2|g_\alpha|^2\,d\nu_\alpha\\
 \leq\|f\|_\infty^2\|v\|^2.
 \end{gathered}
 \tag{U2}
\]
Only countably many summands occur for each fixed $v$. Nonnegative sum/integral interchange proves that the first expression is a finite measure of mass $\|v\|^2$ and gives (1). Pointwise scalar multiplication proves the product law and, by the inner-product formula, the adjoint law. If $f_j\to f$ pointwise with $|f_j|\leq M$, dominated convergence against $\nu_v$ gives $\|(f_j(U)-f(U))v\|\to0$. Uniform simple approximation therefore agrees with the direct-sum multiplier and justifies its notation as a spectral integral. Multiplication by $z$ on each summand gives $U=\int z\,dF$.

<a id="unitary-pvm-uniqueness"></a>
## Uniqueness of the PVM

For any other PVM $G$ with $\int z\,dG=U$, integration of finite simple functions is a contractive star homomorphism: disjoint projections are orthogonal (their sum is a projection; for $x$ in the range of one, contractivity of that sum forces the other projection of $x$ to vanish), intersection products follow by decomposing two sets into their common part and their disjoint remainders, and the squared norm is the sum of the coefficient squares times projected-vector norms. Uniform simple approximation extends this to all bounded Borel functions. Therefore integrals of Laurent polynomials are exactly $p(U)$. The density and contraction in (3) give the same continuous calculus $\Phi(f)$ as for $F$. For every vector the two finite scalar measures consequently have the same integrals of continuous functions and are equal by the uniqueness argument above. Hence $\langle(F(B)-G(B))u,u\rangle=0$ for every $u$. Polarization gives $F(B)=G(B)$ for every Borel $B$. This completes the exact unitary measure foundation used by the Cayley proof.
