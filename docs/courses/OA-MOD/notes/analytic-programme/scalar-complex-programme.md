# Scalar complex analysis from the earlier programme

*Originally written and self-checked by Claude Opus 5.5 (Anthropic), October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all four solutions, supplied the elementary integration proofs and corrected the edge cases, October 2026. Public domain (CC0).*

This is the complete conventions and Sections 1–3, including Lemma 0.1, of the earlier programme lesson *Cauchy’s theorem for cycles and its consequences*. The original mathematical text and numbering are retained. The inherited prerequisite link is resolved to its programme address. Read [Exponentials, angles and the exact period, EF1–EF6](elementary-exponential-trigonometry.md) for the earlier proofs of the exponential, circle parametrization, exact period and square-index integral used below. The closed-boundary and rectangle specializations required by the modular analytic kernel are proved in the [following supplement](scalar-complex-boundaries.md). This selection uses its scalar statements; the supplement explains why scalar integration does not require a Banach-space separation premise.

## Conventions

*Holomorphic functions.* \(U\) denotes an open subset of \(\mathbb C\). A function \(f:U\to\mathbb C\) is *holomorphic* if it is complex differentiable at every point of \(U\). No continuity of \(f'\) is assumed. \(D(c,r)\) is the open disc and \(\bar D(c,r)\) the closed disc of radius \(r\) about \(c\).

*Paths and cycles.*
- A *path* is a piecewise continuously differentiable map \(\gamma:[a,b]\to\mathbb C\). It is *closed* if \(\gamma(a)=\gamma(b)\). Its image is \(\gamma^*\), and its length is \(\ell(\gamma)=\int_a^b|\gamma'|\).
- \([z,w]\) is the segment \(t\mapsto z+t(w-z)\), \(t\in[0,1]\).
- For a closed triangle \(\Delta\) with vertices \(a,b,c\), \(\partial\Delta\) is the closed path \([a,b]+[b,c]+[c,a]\).
- \(\partial D(c,r)\) is the circle \(t\mapsto c+re^{it}\), \(t\in[0,2\pi]\).
- A *cycle* \(\Gamma\) is a finite family of closed paths, read as a formal sum. \(\Gamma^*\) is the union of their images, and \(\ell(\Gamma)\) is the sum of their lengths.

*Integrals.* Let \(X\) be a Banach space. Lemma 0.1 below proves existence and the norm, bounded-map and uniform-limit properties of the Riemann integral of a continuous \(F:[a,b]\to X\). For a continuous \(F\) on \(\gamma^*\),
\[
\int_\gamma F(\lambda)\,d\lambda=\int_a^bF(\gamma(t))\gamma'(t)\,dt ,
\]
taken piece by piece. The integral over a cycle is the sum over its paths, and \(\|\int_\Gamma F\|\leq\ell(\Gamma)\sup_{\Gamma^*}\|F\|\).

*Primitives.* If a scalar function \(F\) is continuous on an open set containing \(\gamma^*\) and has a primitive \(G\) there, meaning \(G\) is holomorphic with \(G'=F\), then \(\int_\gamma F=G(\gamma(b))-G(\gamma(a))\). This follows from the chain rule \((G\circ\gamma)'=F(\gamma)\gamma'\) and the fundamental theorem of calculus on each piece. In particular \(\int_\gamma F=0\) when \(\gamma\) is closed. Every polynomial has a primitive.

### Elementary integration tools

The following tools apply to functions with values in any real or complex Banach space \(X\). They supply the integration facts used throughout this lesson and in the Banach-algebra lesson.

**Lemma 0.1** (Intervals, rectangles and parameters).

1. A continuous \(F:[a,b]\to X\) has a Riemann integral. It is linear, commutes with bounded linear maps, satisfies \(\|\int_a^b F\|\leq\int_a^b\|F\|\), and respects uniform limits.
2. The function \(P(t)=\int_a^t F(s)\,ds\) has derivative \(P'(t)=F(t)\) in the interior, with one-sided derivatives at the endpoints. If \(G\) is continuously differentiable, then \(\int_a^bG'(t)\,dt=G(b)-G(a)\). The chain rule and substitution hold for continuously differentiable real paths; a holomorphic primitive with continuous derivative satisfies the same chain rule along a piecewise continuously differentiable complex path.
3. For continuous \(F:[a,b]\times[c,d]\to X\), the two iterated Riemann integrals agree.
4. Suppose \(K(t,s)\) and its partial derivative \(\partial_tK(t,s)\) are continuous on a rectangle. Then \(t\mapsto\int_c^dK(t,s)\,ds\) is differentiable, with derivative \(\int_c^d\partial_tK(t,s)\,ds\). When both variables range over \([a,b]\), the moving-endpoint integral satisfies
\[
\begin{gathered}
\frac{d}{dt}\int_a^tK(t,s)\,ds
\\
=K(t,t)+\int_a^t\partial_tK(t,s)\,ds .
\end{gathered}
\]

**Proof.** *Compactness and uniform continuity.* A closed bounded interval or rectangle is compact. To see the finite-cover statement directly, if an open cover has no finite subcover, bisect each coordinate interval and choose a resulting closed box still having no finite subcover. Continue with nested boxes. Completeness of the real numbers gives a common point, and the diameters tend to zero. A member of the cover containing that point contains every sufficiently small box, a contradiction. A continuous map on such a box is bounded and uniformly continuous. For the latter claim, given \(\varepsilon>0\), choose for each \(x\) a radius \(r_x>0\) such that \(\|F(y)-F(x)\|<\varepsilon/2\) when \(|y-x|<2r_x\) within the box. Finitely many balls \(B(x_j,r_{x_j})\) cover it. If \(|y-z|<\min_jr_{x_j}\), choose a ball containing \(y\); both \(y,z\) are within \(2r_{x_j}\) of its centre, giving \(\|F(y)-F(z)\|<\varepsilon\).

*Riemann sums.* Assume \(a<b\); a degenerate interval has integral zero. Write
\[
\begin{gathered}
S(F;\mathcal P)\\
=\sum_j(t_j-t_{j-1})F(\xi_j),
\\
t_{j-1}\\
\leq\xi_j\\
\leq t_j,
\end{gathered}
\]
for a tagged partition, and let its mesh be the largest \(t_j-t_{j-1}\). Put \(\omega(\delta)=\sup\{\|F(u)-F(v)\|:|u-v|\leq\delta\}\), so \(\omega(\delta)\to0\). If a partition of mesh at most \(\delta\) is refined, expanding each original summand over its subintervals shows that its sum differs from any tagged refined sum by at most \((b-a)\omega(\delta)\). Two partitions of mesh at most \(\delta\) have a common refinement, so their sums differ by at most \(2(b-a)\omega(\delta)\). Sums along uniform partitions therefore converge by completeness of \(X\); comparison with those sums shows that all tagged sums tend to the same limit as their meshes tend to zero. This defines \(\int_a^bF\). Passing the finite-sum identities to the limit proves linearity and commutation with bounded maps. The finite-sum estimate
\(\|S(F;\mathcal P)\|\leq\sum_j(t_j-t_{j-1})\|F(\xi_j)\|\)
gives the stated norm bound. In particular, a uniform change of size at most \(\eta\) changes the integral by at most \((b-a)\eta\), which proves the uniform-limit assertion. Splitting a partition at an interior point proves additivity over adjacent intervals. Define reversed integrals by changing sign.

*The fundamental theorem and the chain rule.* For interior \(t\) and nonzero small \(h\), the norm of
\((P(t+h)-P(t))/h-F(t)\)
is at most \(\sup_{s\text{ between }t,t+h}\|F(s)-F(t)\|\), which tends to zero. This also gives the endpoint derivatives. To prove the converse, first recall the scalar mean value theorem: a continuous real function on an interval attains its extrema; if its endpoint values agree and it is not constant, some extremum is interior and its derivative is zero, since the two one-sided difference quotients have opposite signs. This is Rolle's theorem. Subtracting the line joining the endpoints gives the mean value theorem. Thus a scalar function with zero derivative is constant.

If \(G\) has continuous derivative \(F\), the function \(G-P\) has zero derivative. Compose it with each bounded linear functional on \(X\); in the complex case apply the real mean value theorem to both real and imaginary parts. These scalar functions are constant, and [Hahn–Banach separation, Corollary 2.3 of the first lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-02), shows that \(G-P\) itself is constant. This gives the converse fundamental theorem. For a differentiable real function \(\phi\), inserting
\(\phi(t+h)-\phi(t)=\phi'(t)h+o(|h|)\)
into the differentiability expansion of \(G\) proves \((G\circ\phi)'=(G'\circ\phi)\phi'\). The same calculation with complex increments proves the chain rule for a holomorphic \(G\) along a differentiable complex path. Continuity of the displayed derivative permits the fundamental theorem on each path piece. Real substitution follows by applying this chain rule to the primitive \(P(u)=\int_{u_0}^uF(v)\,dv\). No monotonicity of \(\phi\) is needed for the oriented identity.

*Rectangles.* Joint uniform continuity makes \(x\mapsto\int_c^dF(x,y)\,dy\) continuous, since the norm of a difference is at most \((d-c)\sup_y\|F(x,y)-F(x',y)\|\); the analogous statement holds in the other variable. Approximate \(F\) by the function constant on each cell of a rectangular grid, using a value of \(F\) at a corner of that cell. Give boundary points a consistent half-open-cell convention, with the final cells closed at the outer boundary. For grid mesh \(\delta\), the uniform error is at most the modulus of continuity at \(\sqrt2\delta\). A one-variable step function with \(m\) division points is Riemann integrable: in a partition of mesh \(\eta\), intervals meeting those points have total length at most \(2m\eta\); all other summands give exactly the appropriate constant times length. The error on the exceptional intervals tends to zero, since the finitely many values are bounded. Each iterated integral of the rectangular step function is consequently the same finite sum
\(\sum_{i,j}(t_i-t_{i-1})(s_j-s_{j-1})F(t_{i-1},s_{j-1})\).
Both iterated integrals of \(F\) differ from this sum by at most the area of the rectangle times that modulus, which tends to zero. This proves (3), including its Banach-valued version.

*Parameters.* Fix an interior parameter \(t\). The fundamental theorem, applied with \(s\) fixed, gives
\[
\frac{K(t+h,s)-K(t,s)}{h}
=\frac1h\int_t^{t+h}\partial_tK(u,s)\,du .
\]
Joint uniform continuity of \(\partial_tK\) makes the right side converge to \(\partial_tK(t,s)\) uniformly in \(s\). The uniform-limit assertion in (1) permits integration in \(s\), proving the fixed-endpoint formula. For \(J(t)=\int_a^tK(t,s)\,ds\), subtract to obtain
\[
\begin{gathered}
J(t+h)-J(t)
\\
=\int_a^t\big(K(t+h,s)-K(t,s)\big)\,ds
\\
+\int_t^{t+h}K(t+h,s)\,ds .
\end{gathered}
\]
After division by \(h\), the first term has the limit already proved and the second tends to \(K(t,t)\) by joint continuity. This proves (4). \(\square\)


## 1. The index of a cycle

For a cycle \(\Gamma\) and \(z\notin\Gamma^*\), the *index* is
\[
\operatorname{Ind}_\Gamma(z)=\frac1{2\pi i}\int_\Gamma\frac{d\lambda}{\lambda-z}.
\]

**Lemma 1.1.**
1. \(\operatorname{Ind}_\Gamma\) takes integer values on \(\mathbb C\setminus\Gamma^*\), is constant on each connected component, and is \(0\) on the unbounded component.
2. For the circle \(\partial D(c,r)\), the index is \(1\) on \(D(c,r)\) and \(0\) outside \(\bar D(c,r)\).
3. For the positively oriented boundary \(\partial Q\) of a closed square \(Q\), the index is \(1\) on the interior of \(Q\) and \(0\) outside \(Q\).

**Proof.** (1) *Integer values.* Let \(\gamma:[a,b]\to\mathbb C\) be a closed path and \(z\notin\gamma^*\). Put
\[
\begin{gathered}
h(t)\\
=\int_a^t\frac{\gamma'(s)}{\gamma(s)-z}\,ds,\\
F(t)\\
=e^{-h(t)}(\gamma(t)-z).
\end{gathered}
\]
Wherever \(\gamma\) is differentiable, \(F'=e^{-h}\big(-h'(\gamma-z)+\gamma'\big)=0\). \(F\) is continuous, so it is constant. Since \(\gamma(b)=\gamma(a)\neq z\), \(F(b)=F(a)\) gives \(e^{-h(b)}=1\). So \(h(b)/(2\pi i)\) is an integer. The index of a cycle is a sum of such integers.

*Constancy.* Let \(d(z)=\operatorname{dist}(z,\Gamma^*)\). For \(z,w\notin\Gamma^*\),
\[
\begin{gathered}
|\operatorname{Ind}_\Gamma(z)-\operatorname{Ind}_\Gamma(w)|\\
=\frac1{2\pi}\Big|\int_\Gamma\frac{(z-w)\,d\lambda}{(\lambda-z)(\lambda-w)}\Big|\\
\leq\frac{\ell(\Gamma)|z-w|}{2\pi d(z)d(w)} .
\end{gathered}
\]
So the index is continuous. A continuous integer-valued function is constant on connected sets. Also \(|\operatorname{Ind}_\Gamma(z)|\leq\ell(\Gamma)/(2\pi d(z))<1\) for \(d(z)\) large, so the index vanishes far out, hence on the unbounded component.

(2) At the centre, \(\frac1{2\pi i}\int_0^{2\pi}\frac{ire^{it}}{re^{it}}\,dt=1\). The open disc is connected, and the complement of the closed disc is connected and unbounded. Apply (1).

(3) After a translation and a scaling, which do not change the index, \(Q=[-1,1]^2\) with centre \(0\). Multiplication by \(i\) maps each side of \(\partial Q\) onto the next one and leaves \(d\lambda/\lambda\) unchanged. So the four sides contribute equally. On the right side, \(\lambda=1+it\) with \(t\in[-1,1]\), and
\[
\begin{gathered}
\int_{-1}^1\frac{i\,dt}{1+it}\\
=\int_{-1}^1\frac{t+i}{1+t^2}\,dt\\
=i\int_{-1}^1\frac{dt}{1+t^2}\\
=\frac{i\pi}2 .
\end{gathered}
\]
So the index at \(0\) is \(4\cdot\frac{i\pi}2/(2\pi i)=1\), and it is \(1\) on the connected interior.

The complement of \(Q\) is connected: the ray from \(0\) through a point outside \(Q\) leaves the convex set \(Q\) for good. It is unbounded, so it lies in the unbounded component, where the index is \(0\). \(\square\)

## 2. Cauchy's theorem in convex sets

**Theorem 2.1** (Goursat). Let \(V\) be open, \(p\in V\), and \(f:V\to\mathbb C\) continuous on \(V\) and holomorphic on \(V\setminus\{p\}\). Then \(\int_{\partial\Delta}f=0\) for every closed triangle \(\Delta\subseteq V\).

**Proof.** If the vertices are collinear, the three segments go back and forth along one segment, and the integrals cancel. Let \(\Delta\) be nondegenerate, with diameter \(d\) and perimeter \(\ell\).

*Case 1: \(p\notin\Delta\).* Let \(c=|\int_{\partial\Delta}f|\).
- The midpoints of the sides cut \(\Delta\) into four triangles. Oriented like \(\Delta\), their boundary integrals add up to \(\int_{\partial\Delta}f\), because the inner edges cancel. So one of them, \(\Delta_1\), has \(|\int_{\partial\Delta_1}f|\geq c/4\).
- Repeating this gives closed triangles \(\Delta\supseteq\Delta_1\supseteq\Delta_2\supseteq\cdots\) with \(|\int_{\partial\Delta_n}f|\geq c/4^n\), diameter \(d/2^n\) and perimeter \(\ell/2^n\).
- They have a common point \(z_0\in\Delta\), and \(z_0\neq p\). Write \(R(z)\) for \(f(z)-f(z_0)-f'(z_0)(z-z_0)\). Given \(\varepsilon>0\), choose \(\delta>0\) with
\[
\begin{gathered}
|f(z)-f(z_0)-f'(z_0)(z-z_0)|\\
\leq\varepsilon|z-z_0|\\
(|z-z_0|<\delta).
\end{gathered}
\]
- The function \(f(z_0)+f'(z_0)(z-z_0)\) is a polynomial, so its integral over \(\partial\Delta_n\) is \(0\). Once \(d/2^n<\delta\),
\[
\begin{gathered}
\frac c{4^n}\\
\leq\Big|\int_{\partial\Delta_n}R(z)\,dz\Big|\\
\leq\frac\ell{2^n}\cdot\varepsilon\frac d{2^n} .
\end{gathered}
\]
- So \(c\leq\varepsilon\ell d\) for every \(\varepsilon>0\), and \(c=0\).

*Case 2: \(p\) is a vertex.* Let the vertices be \(p,b,e\). Choose \(b'\in[p,b]\) and \(e'\in[p,e]\) near \(p\), different from \(p\).
- \(\int_{\partial\Delta}f\) is the sum of the boundary integrals over the triangles \((p,b',e')\), \((b',b,e)\) and \((b',e,e')\).
- The last two do not contain \(p\), so their integrals vanish by Case 1.
- The first is at most \(\ell(\partial(p,b',e'))\max_\Delta|f|\) in absolute value. This tends to \(0\) as \(b',e'\to p\).

*Case 3: \(p\in\Delta\) is not a vertex.* Cut \(\Delta\) into the three triangles with vertex \(p\) and the sides of \(\Delta\) as opposite sides. Their boundary integrals add up to \(\int_{\partial\Delta}f\), and each vanishes by Case 2. \(\square\)

**Theorem 2.2** (Cauchy's theorem in a convex set). Let \(V\) be convex and open, \(p\in V\), and \(f\) continuous on \(V\) and holomorphic on \(V\setminus\{p\}\). Fix \(a\in V\) and put \(F(z)=\int_{[a,z]}f\). Then \(F\) is holomorphic on \(V\) with \(F'=f\). Hence \(\int_\gamma f=0\) for every closed path \(\gamma\) in \(V\).

**Proof.** For \(z,z+h\in V\), the triangle with vertices \(a,z,z+h\) lies in \(V\), by convexity. By Theorem 2.1, \(F(z+h)-F(z)=\int_{[z,z+h]}f\). So
\[
\begin{gathered}
\Big|\frac{F(z+h)-F(z)}h-f(z)\Big|\\
=\Big|\frac1h\int_{[z,z+h]}(f(w)-f(z))\,dw\Big|\\
\leq\max_{w\in[z,z+h]}|f(w)-f(z)|\to0 .
\end{gathered}
\]
The last claim follows from the Conventions on primitives. \(\square\)

**Theorem 2.3** (Cauchy's formula in a convex set). Let \(V\) be convex and open, \(f\) holomorphic on \(V\), \(\gamma\) a closed path in \(V\), and \(z\in V\setminus\gamma^*\). Then
\[
f(z)\operatorname{Ind}_\gamma(z)=\frac1{2\pi i}\int_\gamma\frac{f(w)}{w-z}\,dw .
\]

**Proof.** Put \(g(w)=(f(w)-f(z))/(w-z)\) for \(w\neq z\), and \(g(z)=f'(z)\). Then \(g\) is continuous on \(V\) and holomorphic on \(V\setminus\{z\}\). By Theorem 2.2, \(\int_\gamma g=0\), which is the formula. \(\square\)

## 3. Power series and their consequences

**Lemma 3.1** (Power series). Let \(c\in\mathbb C\), \(0<R\leq\infty\), and let \(a_n\in\mathbb C\) satisfy \(\sum_n|a_n|\rho^n<\infty\) for every \(0<\rho<R\). Then:
- \(f(z)=\sum_na_n(z-c)^n\) is holomorphic on \(D(c,R)\), with \(f'(z)=\sum_{n\geq1}na_n(z-c)^{n-1}\);
- the coefficients of \(f'\) satisfy the same hypothesis.

Consequently \(f\) has derivatives of all orders, and \(a_n=f^{(n)}(c)/n!\).

**Proof.** Take \(c=0\), and fix \(0<\rho<\rho'<R\).
- *The derived coefficients.* \(n|a_n|\rho^{n-1}\leq|a_n|\rho'^n\cdot\frac n\rho(\rho/\rho')^n\), and \(n(\rho/\rho')^n\to0\). So \(\sum_{n\geq1}n|a_n|\rho^{n-1}<\infty\). In the same way \(\sum_{n\geq2}n^2|a_n|\rho^{n-2}<\infty\).
- *An estimate.* The constant term has zero difference quotient and the \(n=1\) term has zero derivative remainder. For \(n\geq2\) and \(|z|,|w|\leq\rho\) with \(z\neq w\),
\[
\begin{gathered}
\frac{z^n-w^n}{z-w}-nw^{n-1}\\
=\sum_{k=0}^{n-1}w^k\big(z^{n-1-k}-w^{n-1-k}\big).
\end{gathered}
\]
  Since \(|z^m-w^m|\leq m\rho^{m-1}|z-w|\), its absolute value is at most \(n^2\rho^{n-2}|z-w|\).
- *The derivative.* So
\[
\begin{gathered}
\Big|\frac{f(z)-f(w)}{z-w}-\sum_{n\geq1}na_nw^{n-1}\Big|\\
\leq|z-w|\sum_{n\geq2}n^2|a_n|\rho^{n-2},
\end{gathered}
\]
  which tends to \(0\) as \(z\to w\).
- Repeating, \(f\) has derivatives of all orders. Evaluating the series of \(f^{(n)}\) at \(0\) gives \(f^{(n)}(0)=n!a_n\). \(\square\)

**Theorem 3.2** (Holomorphic functions are analytic). Let \(f\) be holomorphic on \(U\supseteq D(c,R)\). Then
\[
f(z)=\sum_na_n(z-c)^n\qquad(z\in D(c,R)),
\]
with \(\sum_n|a_n|\rho^n<\infty\) for every \(0<\rho<R\). For every \(0<r<R\),
\[
\begin{gathered}
a_n\\
=\frac{f^{(n)}(c)}{n!}\\
=\frac1{2\pi i}\int_{\partial D(c,r)}\frac{f(w)}{(w-c)^{n+1}}\,dw,\\
|a_n|\\
\leq\frac{M(r)}{r^n},
\end{gathered}
\]
where \(M(r)=\max_{|w-c|=r}|f(w)|\) (*Cauchy's estimates*). In particular \(f'\) is holomorphic, and \(f\) has derivatives of all orders.

**Proof.** Fix \(0<r<R\) and \(z\) with \(|z-c|<r\). The disc \(D(c,R)\) is convex, and the index of \(\partial D(c,r)\) at \(z\) is \(1\) (Lemma 1.1). By Theorem 2.3,
\[
f(z)=\frac1{2\pi i}\int_{\partial D(c,r)}\frac{f(w)}{w-z}\,dw .
\]
For \(|w-c|=r\),
\[
\frac1{w-z}=\sum_n\frac{(z-c)^n}{(w-c)^{n+1}},
\]
uniformly in \(w\), because \(|z-c|/r<1\). Integrating term by term gives \(f(z)=\sum_na_n(r)(z-c)^n\), with \(a_n(r)\) the integral in the statement and \(|a_n(r)|\leq M(r)r^{-n}\). This series converges absolutely for \(|z-c|<r\). By Lemma 3.1, \(a_n(r)=f^{(n)}(c)/n!\), which does not depend on \(r\). Since \(r<R\) is arbitrary, the expansion holds on \(D(c,R)\). \(\square\)

**Corollary 3.3** (Liouville). A bounded holomorphic function \(f:\mathbb C\to\mathbb C\) is constant.

**Proof.** If \(|f|\leq M\), Cauchy's estimates at \(c=0\) give \(|a_n|\leq M/r^n\) for every \(r>0\). So \(a_n=0\) for \(n\geq1\). \(\square\)

**Theorem 3.4** (Morera). Let \(f\) be continuous on \(U\), with \(\int_{\partial\Delta}f=0\) for every closed triangle \(\Delta\subseteq U\). Then \(f\) is holomorphic.

**Proof.** On each disc \(D(c,r)\subseteq U\), the function \(F(z)=\int_{[c,z]}f\) satisfies \(F'=f\), by the proof of Theorem 2.2, which used only the vanishing of triangle integrals. So \(F\) is holomorphic, and by Theorem 3.2 so is \(F'=f\). \(\square\)

**Corollary 3.5** (Weierstrass). Let \(f_n\) be holomorphic on \(U\), and let \(f_n\to f\) uniformly on every compact subset of \(U\). Then \(f\) is holomorphic.

**Proof.** \(f\) is continuous. For a closed triangle \(\Delta\subseteq U\), \(\int_{\partial\Delta}f=\lim_n\int_{\partial\Delta}f_n=0\), because the convergence is uniform on the compact set \(\partial\Delta\). Apply Morera's theorem. \(\square\)

**Theorem 3.6** (Maximum modulus). Let \(f\) be continuous on the closed unit disc \(\bar D=\bar D(0,1)\) and holomorphic on \(D(0,1)\). Then
\[
\max_{\bar D}|f|=\max_{|z|=1}|f(z)| .
\]
In particular, if \(f=0\) on the unit circle, then \(f=0\).

**Proof.** Let \(M=\max_{\bar D}|f|\), attained at \(c\). Suppose \(|c|<1\), and put \(r_0=1-|c|\).
- *Mean values.* For \(0<\rho<r_0\), \(f\) is holomorphic on the disc \(D(c,r_0)\). Theorem 3.2 at the centre, with \(a_0=f(c)\), gives
\[
f(c)=\frac1{2\pi}\int_0^{2\pi}f(c+\rho e^{it})\,dt .
\]
- So \(M=|f(c)|\leq\frac1{2\pi}\int_0^{2\pi}|f(c+\rho e^{it})|\,dt\leq M\). The integrand is continuous and at most \(M\), so it equals \(M\) everywhere: \(|f|=M\) on the circle \(|z-c|=\rho\).
- Let \(\rho\to r_0\). By continuity on \(\bar D\), \(|f|=M\) at every point with \(|z-c|=r_0\). One of these points lies on the unit circle: \(c+r_0c/|c|\) if \(c\neq0\), and any point of the circle if \(c=0\). \(\square\)

**Theorem 3.7** (Identity theorem). Let \(U\) be connected and \(f\) holomorphic on \(U\). If the zeros of \(f\) have an accumulation point in \(U\), then \(f=0\). In particular, two holomorphic functions on \(U\) that agree on a nonempty open subset agree everywhere.

**Proof.** Let \(Z\) be the set of \(z\in U\) with \(f^{(n)}(z)=0\) for every \(n\geq0\).
- \(Z\) is closed in \(U\), because each \(f^{(n)}\) is continuous (Theorem 3.2).
- \(Z\) is open: if \(z\in Z\) and \(D(z,r)\subseteq U\), the Taylor expansion of Theorem 3.2 shows \(f=0\) on \(D(z,r)\), so all derivatives vanish there.
- Let \(a\in U\) be an accumulation point of zeros, and suppose \(a\notin Z\). Let \(m\) be the least \(n\) with \(f^{(n)}(a)\neq0\). By Theorem 3.2, \(f(z)=(z-a)^mg(z)\) near \(a\), where \(g(z)=\sum_{n\geq m}a_n(z-a)^{n-m}\) is continuous with \(g(a)=a_m\neq0\). So \(f\) has no zeros near \(a\) other than \(a\), a contradiction. Hence \(a\in Z\).
- So \(Z\) is nonempty, open and closed in the connected set \(U\), and \(Z=U\).

For the last claim, apply this to the difference of the two functions. \(\square\)

