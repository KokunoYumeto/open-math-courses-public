# Cauchy's theorem for cycles and its consequences

*Originally written and self-checked by Claude Opus 5.5 (Anthropic), October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all four solutions, supplied the elementary integration proofs and corrected the edge cases, October 2026. Public domain (CC0).*

This lesson proves the complex analysis that the operator-algebra lessons use. It covers:
- the index of a cycle;
- Goursat's theorem and Cauchy's theorem in convex sets;
- power series: holomorphic functions are analytic, with Cauchy's estimates;
- Liouville's theorem, Morera's theorem, Weierstrass's convergence theorem, the maximum modulus principle and the identity theorem;
- Cauchy's theorem and integral formula for cycles, with Dixon's proof;
- cycles that surround a compact set inside an open set;
- the same theorems for functions with values in a Banach space.

The lesson uses Hahn–Banach separation and uniform boundedness. Lemma 0.1 below proves the elementary real and Banach-valued integration facts required here: Riemann integration on intervals, the fundamental theorem and chain rule, rectangle interchange, and differentiation of parameter integrals. The later complex-analysis proofs require no other integration theorem. The scalar exponential, its exact period and continuous local angles are proved in The complex exponential and the circle, Theorems 2–4 and Proposition 6. The earlier scalar limit, compactness and calculus proofs are in Real analysis on closed intervals, Theorems 3–6, 8 and 12–13.

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

If \(G\) has continuous derivative \(F\), the function \(G-P\) has zero derivative. Compose it with each bounded linear functional on \(X\); in the complex case apply the real mean value theorem to both real and imaginary parts. These scalar functions are constant, and Hahn–Banach separation, Corollary 2.3 of the first lesson, shows that \(G-P\) itself is constant. This gives the converse fundamental theorem. For a differentiable real function \(\phi\), inserting
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

## 4. Cauchy's theorem for cycles

**Lemma 4.1.** The image of a path has empty interior. So does \(\Gamma^*\) for a cycle \(\Gamma\). Hence \(U\setminus\Gamma^*\neq\varnothing\) for every nonempty open \(U\).

**Proof.** *One path.* Let \(\gamma:[a,b]\to\mathbb C\) be a path, and \(L=\sup|\gamma'|\) over its pieces. Then \(|\gamma(s)-\gamma(t)|\leq L|s-t|\). If \(a=b\) or \(L=0\), the image is a single point and has empty interior. Otherwise \(L(b-a)>0\). Suppose \(\gamma^*\) contains a closed square \(Q\) of side \(\sigma\).
- Cut \([a,b]\) into \(N\) equal intervals. Their images are \(N\) sets of diameter at most \(\varepsilon=L(b-a)/N\), and they cover \(Q\).
- Let \(M=\lfloor\sigma/(2\varepsilon)\rfloor\), and take \(N\) so large that \(M\geq1\). The \((M+1)^2\) grid points of \(Q\) with spacing \(\sigma/M\) are at mutual distance at least \(\sigma/M\geq2\varepsilon>\varepsilon\). So each of the \(N\) sets contains at most one of them, and \(N\geq(M+1)^2>(\sigma N/(2L(b-a)))^2\).
- This fails for large \(N\).

*A cycle.* Let \(\Gamma\) consist of \(\gamma_1,\dots,\gamma_m\), and suppose a nonempty open set \(W\) lies in \(\Gamma^*\). Then \(W\setminus\gamma_1^*\) is open, because \(\gamma_1^*\) is compact. It is nonempty, because \(\gamma_1^*\) has empty interior. It lies in \(\gamma_2^*\cup\dots\cup\gamma_m^*\). Repeating, we reach a nonempty open set inside a single \(\gamma_k^*\), which is impossible. \(\square\)

**Theorem 4.2** (Cauchy's theorem for cycles). Let \(\Gamma\) be a cycle in \(U\) with \(\operatorname{Ind}_\Gamma(\alpha)=0\) for every \(\alpha\notin U\), and let \(f\) be holomorphic on \(U\). Then
\[
\begin{gathered}
f(z)\operatorname{Ind}_\Gamma(z)\\
=\frac1{2\pi i}\int_\Gamma\frac{f(w)}{w-z}\,dw\\
(z\in U\setminus\Gamma^*),
\\
\text{and}\\
\int_\Gamma f(w)\,dw\\
=0 .
\end{gathered}
\]

*Reference:* The Dixon argument for a closed curve is presented in [MIT OCW Lecture 13, by Zuoqin Wang for Sigurdur Helgason’s course](https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/8793d412fa0da2a4183539f5d8f7e3fd_lecture13.pdf). The proof below includes the finite-cycle formulation.

**Proof.** *Step 1: a continuous difference quotient.* Define \(\varphi\) on \(U\times U\) by
\[
\begin{gathered}
\varphi(z,w)\\
=\frac{f(w)-f(z)}{w-z}\\
(z\neq w),\\
\varphi(z,z)\\
=f'(z).
\end{gathered}
\]
\(\varphi\) is continuous at points with \(z\neq w\). Let \(a\in U\) and \(D(a,r)\subseteq U\).
- \(f'\) is holomorphic, hence continuous (Theorem 3.2), and \(f\) is a primitive of \(f'\).
- So for \(z,w\in D(a,r)\), \(f(w)-f(z)=\int_{[z,w]}f'\), which gives
\[
\varphi(z,w)=\int_0^1f'\big(z+t(w-z)\big)\,dt .
\]
  This also holds for \(z=w\).
- As \((z,w)\to(a,a)\), the integrand tends to \(f'(a)\) uniformly in \(t\). So \(\varphi\) is continuous at \((a,a)\).

*Step 2: a holomorphic function on \(U\).* Put
\[
g(z)=\frac1{2\pi i}\int_\Gamma\varphi(z,w)\,dw\qquad(z\in U).
\]
- \(g\) is continuous, because \(\varphi\) is uniformly continuous on \(K\times\Gamma^*\) for each compact \(K\subseteq U\).
- Let \(\Delta\subseteq U\) be a closed triangle. After parametrizing \(\partial\Delta\) and the paths of \(\Gamma\), the double integral is an iterated integral of a continuous function on finitely many rectangles. Exchanging the order of integration gives
\[
\begin{gathered}
\int_{\partial\Delta}g(z)\,dz\\
=\frac1{2\pi i}\int_\Gamma\Big(\int_{\partial\Delta}\varphi(z,w)\,dz\Big)dw .
\end{gathered}
\]
- For fixed \(w\), \(z\mapsto\varphi(z,w)\) is continuous on \(U\) and holomorphic on \(U\setminus\{w\}\). By Goursat's theorem 2.1, the inner integral is \(0\).
- By Morera's theorem, \(g\) is holomorphic on \(U\).

*Step 3: an entire function.* Let \(V_0=\{z\notin\Gamma^*:\operatorname{Ind}_\Gamma(z)=0\}\). It is open by Lemma 1.1. It contains \(\mathbb C\setminus U\) by hypothesis, so \(U\cup V_0=\mathbb C\). Put
\[
g_1(z)=\frac1{2\pi i}\int_\Gamma\frac{f(w)}{w-z}\,dw\qquad(z\in V_0).
\]
- \(g_1\) is holomorphic on \(V_0\), by the argument of Step 2 applied to the continuous function \((z,w)\mapsto f(w)/(w-z)\) on \(V_0\times\Gamma^*\), which is holomorphic in \(z\).
- For \(z\in U\cap V_0\), \(g(z)=g_1(z)-f(z)\operatorname{Ind}_\Gamma(z)=g_1(z)\).
- So \(G=g\) on \(U\) and \(G=g_1\) on \(V_0\) is a well-defined holomorphic function on \(\mathbb C\).

*Step 4: \(G=0\).* Choose \(R\) with \(\Gamma^*\subseteq D(0,R)\). The set \(\{|z|>R\}\) is connected and unbounded, so it lies in the unbounded component of \(\mathbb C\setminus\Gamma^*\), and hence in \(V_0\). There
\[
\begin{gathered}
|G(z)|\\
=|g_1(z)|\\
\leq\frac{\ell(\Gamma)\max_{\Gamma^*}|f|}{2\pi(|z|-R)}\to0\\
(|z|\to\infty).
\end{gathered}
\]
So \(G\) is bounded: it is continuous on a large closed disc and small outside it. By Liouville's theorem, \(G\) is constant, and the constant is \(0\).

*Step 5: conclusion.* For \(z\in U\setminus\Gamma^*\),
\[
0=g(z)=\frac1{2\pi i}\int_\Gamma\frac{f(w)}{w-z}\,dw-f(z)\operatorname{Ind}_\Gamma(z).
\]
This is the formula. If \(U=\varnothing\) there is nothing to prove. Otherwise choose \(z\in U\setminus\Gamma^*\) (Lemma 4.1), and apply the formula to the holomorphic function \(w\mapsto(w-z)f(w)\), which vanishes at \(z\):
\[
\frac1{2\pi i}\int_\Gamma f(w)\,dw=0\cdot\operatorname{Ind}_\Gamma(z)=0 .\qquad\square
\]

## 5. Cycles that surround a compact set

A cycle \(\Gamma\) *surrounds* a compact set \(K\) in an open set \(U\supseteq K\) if
- \(\Gamma^*\subseteq U\setminus K\),
- \(\operatorname{Ind}_\Gamma=1\) on \(K\), and
- \(\operatorname{Ind}_\Gamma=0\) on \(\mathbb C\setminus U\).

**Theorem 5.1.** Let \(K\subseteq U\) with \(K\) compact and \(U\) open. Some cycle made of finitely many oriented segments surrounds \(K\) in \(U\).

**Proof.** If \(K=\varnothing\), the empty cycle will do. Otherwise choose \(\delta>0\) with \(2\delta<\operatorname{dist}(K,\mathbb C\setminus U)\); any \(\delta>0\) if \(U=\mathbb C\).

*The squares.* Consider the grid of closed squares \([j\delta,(j+1)\delta]\times[k\delta,(k+1)\delta]\), \(j,k\in\mathbb Z\). Let \(Q_1,\dots,Q_m\) be those that meet \(K\); there are finitely many, since \(K\) is bounded. Each \(Q_i\) has diameter \(\delta\sqrt2<2\delta\), so it lies in \(U\).

*The edges.* List the oriented edges of the positively oriented boundaries \(\partial Q_1,\dots,\partial Q_m\). An edge shared by two of the \(Q_i\) occurs twice, with opposite orientations. Remove all these pairs, and let \(\mathcal E\) be the remaining oriented edges.
- (a) For every continuous \(F\) on the union of the edges, \(\sum_{e\in\mathcal E}\int_eF=\sum_i\int_{\partial Q_i}F\), because the removed pairs contribute opposite amounts.
- (b) Every \(e\in\mathcal E\) lies in \(U\setminus K\). Indeed, \(e\) is an edge of exactly one \(Q_i\), so \(e\subseteq U\). The grid square on the other side of \(e\) is not among the \(Q_i\), so it does not meet \(K\), and it contains \(e\).
- (c) At every grid vertex, as many edges of \(\mathcal E\) end as start. This holds for the boundary of each square, hence for the full list, and removing a pair of opposite edges preserves it.

*A cycle.* By (c), \(\mathcal E\) splits into closed paths. Start with any edge and keep following unused edges. At a vertex other than the starting one, more edges have arrived than have left, so by (c) an unused edge leaves it. Since there are finitely many edges, the walk returns to the starting vertex and closes a path. Remove its edges; (c) still holds; repeat. Let \(\Gamma\) be the resulting cycle. By (b), \(\Gamma^*\subseteq U\setminus K\).

*Index off \(U\).* Let \(\alpha\notin U\). Then \(\alpha\) lies in no \(Q_i\), so \(\operatorname{Ind}_{\partial Q_i}(\alpha)=0\) for every \(i\) (Lemma 1.1(3)). By (a), \(\operatorname{Ind}_\Gamma(\alpha)=\sum_i\operatorname{Ind}_{\partial Q_i}(\alpha)=0\).

*Index on \(K\).*
- Let \(w\) be an interior point of some \(Q_{i_0}\). It lies in no other \(Q_i\), so by (a) and Lemma 1.1(3), \(\operatorname{Ind}_\Gamma(w)=1\).
- Let \(z\in K\). It lies in some grid square, which meets \(K\), so it is some \(Q_{i_0}\). By (b), \(z\notin\Gamma^*\). Interior points \(w\) of \(Q_{i_0}\) with \(|w-z|<\operatorname{dist}(z,\Gamma^*)\) exist, and the segment \([z,w]\) misses \(\Gamma^*\). So \(z\) and \(w\) lie in one component of \(\mathbb C\setminus\Gamma^*\), and \(\operatorname{Ind}_\Gamma(z)=\operatorname{Ind}_\Gamma(w)=1\). \(\square\)

## 6. Functions with values in a Banach space

**Theorem 6.1.** Let \(X\) be a Banach space and \(g:U\to X\) a map such that \(\varphi\circ g\) is holomorphic for every \(\varphi\in X^*\).
1. \(g\) is continuous; it is even Lipschitz on a neighbourhood of each point.
2. For every cycle \(\Gamma\) in \(U\) with \(\operatorname{Ind}_\Gamma(\alpha)=0\) for all \(\alpha\notin U\),
\[
\begin{gathered}
\int_\Gamma g(w)\,dw\\
=0,\\
g(z)\operatorname{Ind}_\Gamma(z)\\
=\frac1{2\pi i}\int_\Gamma\frac{g(w)}{w-z}\,dw\\
(z\in U\setminus\Gamma^*).
\end{gathered}
\]
3. On each disc \(D(c,R)\subseteq U\), \(g(z)=\sum_na_n(z-c)^n\) with \(a_n\in X\) and \(\sum_n\|a_n\|\rho^n<\infty\) for \(\rho<R\). In particular the difference quotients \((g(z+h)-g(z))/h\) converge in norm as \(h\to0\).
4. (*Liouville.*) If \(U=\mathbb C\) and \(g\) is bounded, then \(g\) is constant.

**Proof.** (1) Fix \(a\in U\) and \(r>0\) with \(\bar D(a,2r)\subseteq U\). By compactness, \(D(a,2r+\varepsilon)\subseteq U\) for some \(\varepsilon>0\); this disc is convex. Let \(C=\partial D(a,2r)\), \(\varphi\in X^*\), and \(z\neq z'\) in \(D(a,r)\).
- By Theorem 2.3 for \(\varphi\circ g\), with index \(1\) at \(z\) and \(z'\),
\[
\begin{gathered}
\varphi(g(z))-\varphi(g(z'))\\
=\frac{z-z'}{2\pi i}\int_C\frac{\varphi(g(w))}{(w-z)(w-z')}\,dw .
\end{gathered}
\]
- On \(C\), \(|w-z|\geq r\) and \(|w-z'|\geq r\). With \(M_\varphi=\max_C|\varphi\circ g|\), which is finite because \(\varphi\circ g\) is continuous, we get
\[
\begin{gathered}
\frac{|\varphi(g(z))-\varphi(g(z'))|}{|z-z'|}\\
\leq\frac{4\pi r}{2\pi}\cdot\frac{M_\varphi}{r^2}\\
=\frac{2M_\varphi}r .
\end{gathered}
\]
- So the set of quotients \((g(z)-g(z'))/(z-z')\), for \(z\neq z'\) in \(D(a,r)\), is bounded under every \(\varphi\in X^*\). By the first lesson, Corollary 4.3(2), it is norm bounded. So \(g\) is Lipschitz on \(D(a,r)\).

(2) By (1) the integrals exist. For every \(\varphi\in X^*\), \(\varphi\) passes through the integrals, and Theorem 4.2 for \(\varphi\circ g\) gives the two identities after \(\varphi\) is applied. Bounded functionals separate the points of \(X\) (the first lesson, Corollary 2.3(2)).

(3) Let \(0<r<R\) and \(|z-c|<r\). The cycle \(\partial D(c,r)\) has index \(0\) off \(\bar D(c,r)\subseteq U\). By (2),
\[
g(z)=\frac1{2\pi i}\int_{\partial D(c,r)}\frac{g(w)}{w-z}\,dw .
\]
Expanding as in the proof of Theorem 3.2 gives \(g(z)=\sum_na_n(z-c)^n\), with \(\|a_n\|\leq\max_{|w-c|=r}\|g(w)\|/r^n\). The \(a_n\) do not depend on \(r\), because \(\varphi(a_n)=(\varphi\circ g)^{(n)}(c)/n!\) for every \(\varphi\). The proof of Lemma 3.1 works verbatim with norms in place of absolute values, so the difference quotients converge in norm.

(4) Each \(\varphi\circ g\) is bounded and holomorphic on \(\mathbb C\), hence constant. So \(\varphi(g(z)-g(0))=0\) for every \(\varphi\), and \(g(z)=g(0)\). \(\square\)

## Exercises

**Exercise 1** (medium; The fundamental theorem of algebra). Show that every nonconstant polynomial \(p\) has a complex root.

*Solution.* Write \(p(z)=c_dz^d+\dots+c_0\) with \(d\geq1\) and \(c_d\neq0\). Then \(|p(z)|\geq|c_d||z|^d/2\) for large \(|z|\), so \(|p(z)|\to\infty\). If \(p\) had no root, \(1/p\) would be holomorphic on \(\mathbb C\). It would be bounded: continuous on a large closed disc and small outside. By Liouville's theorem it would be constant, and then so would \(p\). \(\square\)

**Exercise 2** (easy; The condition on the index). Let \(U=\mathbb C\setminus\{0\}\), \(f(z)=1/z\), and let \(\Gamma\) be the unit circle. Compute \(\int_\Gamma f\), and say which hypothesis of Theorem 4.2 fails.

*Solution.* \(\int_\Gamma dz/z=2\pi i\operatorname{Ind}_\Gamma(0)=2\pi i\neq0\). The hypothesis that fails is \(\operatorname{Ind}_\Gamma(\alpha)=0\) for \(\alpha\notin U\): the point \(0\) is not in \(U\), and \(\operatorname{Ind}_\Gamma(0)=1\). \(\square\)

**Exercise 3** (medium; Schwarz's lemma). Let \(f\) be holomorphic on \(D(0,1)\) with \(|f|\leq1\) and \(f(0)=0\). Show that \(|f(z)|\leq|z|\) for all \(z\), and \(|f'(0)|\leq1\).

*Solution.*
- By Theorem 3.2, \(f(z)=\sum_{n\geq1}a_nz^n\) on \(D(0,1)\). So \(g(z)=\sum_{n\geq0}a_{n+1}z^n\) is holomorphic on \(D(0,1)\) (Lemma 3.1), with \(f(z)=zg(z)\) and \(g(0)=f'(0)\).
- For \(0<r<1\), the function \(z\mapsto g(rz)\) is holomorphic on \(D(0,1/r)\supseteq\bar D(0,1)\). By Theorem 3.6, \(|g(rz)|\leq\max_{|w|=1}|g(rw)|\leq1/r\) for \(|z|\leq1\).
- Letting \(r\to1\) gives \(|g|\leq1\) on \(D(0,1)\). \(\square\)

**Exercise 4** (medium; Polynomials converging on the circle). Let \(p_n\) be polynomials that converge uniformly on the unit circle \(\mathbb T\). Show that they converge uniformly on \(\bar D(0,1)\), and that the limit \(G\) is continuous on \(\bar D(0,1)\) and holomorphic on \(D(0,1)\). Show that \(G=0\) if \(G=0\) on \(\mathbb T\).

*Solution.*
- By Theorem 3.6 applied to \(p_n-p_m\), \(\max_{\bar D}|p_n-p_m|=\max_{\mathbb T}|p_n-p_m|\). So \((p_n)\) is uniformly Cauchy on \(\bar D\), and its uniform limit \(G\) is continuous there.
- \(G\) is holomorphic on \(D(0,1)\) by Corollary 3.5.
- If \(G=0\) on \(\mathbb T\), then \(G=0\) by Theorem 3.6. \(\square\)

## Where this leads

[Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md) defines \(f(x)\) for \(f\) holomorphic near the spectrum of \(x\) as an integral over a cycle that surrounds the spectrum. Theorem 5.1 provides the cycle, and Theorems 4.2 and 6.1 show that the result does not depend on it. Exercise 4 is the step used in Example 3.4 of the lesson on C\*-algebras. Liouville's theorem is used in [Kaplansky's density theorem and its consequences](kaplansky-s-density-theorem-and-its-consequences.md).

## References

- É. Goursat, ["Sur la définition générale des fonctions analytiques, d'après Cauchy"](https://www.ams.org/journals/tran/1900-001-01/S0002-9947-1900-1500519-7/S0002-9947-1900-1500519-7.pdf), *Transactions of the American Mathematical Society* 1 (1900), 14–16.

The proofs are written here in our own words.

*Freely accessible reading:* [Zuoqin Wang; course instructor Sigurdur Helgason, *MIT OCW 18.112 Lecture 13*, Lecture 13, printed pp. 1–4](https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/8793d412fa0da2a4183539f5d8f7e3fd_lecture13.pdf) gives a route through Dixon’s closed-curve proof; the finite-cycle proof and local inputs are included here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

For an alternative grid proof, see [I. Černý, expanded author presentation (2012), pp. 1–5](https://matematika.cuni.cz/dl/cerny/cauchy.pdf). Its rectangular formula is an input; the local integral results are proved in this lesson.
