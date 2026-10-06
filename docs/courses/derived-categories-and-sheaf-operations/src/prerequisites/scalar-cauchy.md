# The scalar Cauchy formula and power series

*Selected from the programme lesson originally written and self-checked by Claude Opus 5.5 (Anthropic), with elementary integration proofs and edge-case corrections by GPT-6.1 Sol (OpenAI), in Codex at Ultra. The present scalar selection, local links and elementary closure clarifications were prepared and self-checked by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. The independently written programme text is CC0. The [source and edition notice](assets/notices/scalar-cauchy-source-notice.html) records the exact programme revision and human mathematical credit. Independent or human review is not asserted.*

Read [Real analysis on closed intervals](real-analysis-on-closed-intervals.md) and [The complex exponential and the circle](complex-exponential-and-the-circle.md) first. We use their complete scalar limit, compactness, calculus, exponential-kernel and circle proofs. The conclusions needed next are the Cauchy formula on a disc and termwise differentiation of power series.

## Conventions

*Holomorphic functions.* \(U\) denotes an open subset of \(\mathbb C\). A function \(f:U\to\mathbb C\) is *holomorphic* if it is complex differentiable at every point of \(U\). No continuity of \(f'\) is assumed. \(D(c,r)\) is the open disc and \(\bar D(c,r)\) the closed disc of radius \(r\) about \(c\).

*Paths and cycles.*
- A *path* is a piecewise continuously differentiable map \(\gamma:[a,b]\to\mathbb C\). It is *closed* if \(\gamma(a)=\gamma(b)\). Its image is \(\gamma^*\), and its length is \(\ell(\gamma)=\int_a^b|\gamma'|\).
- \([z,w]\) is the segment \(t\mapsto z+t(w-z)\), \(t\in[0,1]\).
- For a closed triangle \(\Delta\) with vertices \(a,b,c\), \(\partial\Delta\) is the closed path \([a,b]+[b,c]+[c,a]\).
- \(\partial D(c,r)\) is the circle \(t\mapsto c+re^{it}\), \(t\in[0,2\pi]\).
- A *cycle* \(\Gamma\) is a finite family of closed paths, read as a formal sum. \(\Gamma^*\) is the union of their images, and \(\ell(\Gamma)\) is the sum of their lengths.

*Integrals.* All integrands here have values in \(\mathbb C\). Lemma 0.1 proves the modulus bound and uniform-limit properties of their Riemann integrals on intervals. For continuous \(F\) on \(\gamma^*\),
\[
\int_\gamma F(\lambda)\,d\lambda=\int_a^bF(\gamma(t))\gamma'(t)\,dt ,
\]
taken piece by piece. The integral over a cycle is the sum over its paths, and \(|\int_\Gamma F|\leq\ell(\Gamma)\sup_{\Gamma^*}|F|\).

*Primitives.* If a scalar function \(F\) is continuous on an open set containing \(\gamma^*\) and has a primitive \(G\) there, meaning \(G\) is holomorphic with \(G'=F\), then \(\int_\gamma F=G(\gamma(b))-G(\gamma(a))\). This follows from the chain rule \((G\circ\gamma)'=F(\gamma)\gamma'\) and the fundamental theorem of calculus on each piece. In particular \(\int_\gamma F=0\) when \(\gamma\) is closed. Every polynomial has a primitive.

## Intervals and rectangles

**Lemma 0.1** (Intervals and rectangles).

1. A continuous \(F:[a,b]\to \mathbb C\) has a Riemann integral. It is linear, commutes with multiplication by a constant, satisfies \(|\int_a^b F|\leq\int_a^b|F|\), and respects uniform limits.
2. The function \(P(t)=\int_a^t F(s)\,ds\) has derivative \(P'(t)=F(t)\) in the interior, with one-sided derivatives at the endpoints. If \(G\) is continuously differentiable, then \(\int_a^bG'(t)\,dt=G(b)-G(a)\). The chain rule and substitution hold for continuously differentiable real paths; a holomorphic primitive with continuous derivative satisfies the same chain rule along a piecewise continuously differentiable complex path.
3. For continuous \(F:[a,b]\times[c,d]\to \mathbb C\), the two iterated Riemann integrals agree.

**Proof.** *Compactness and uniform continuity.* A closed bounded interval or rectangle is compact. To see the finite-cover statement directly, if an open cover has no finite subcover, bisect each coordinate interval and choose a resulting closed box still having no finite subcover. Continue with nested boxes. Theorem 3 of [Real analysis on closed intervals](real-analysis-on-closed-intervals.md) gives a common point in each coordinate, and the diameters tend to zero. A member of the cover containing that point contains every sufficiently small box, a contradiction. A continuous scalar function on such a box is bounded: continuity bounds it on a neighbourhood of each point, and a finite subcover gives a common finite bound. It is also uniformly continuous. For the latter claim, given \(\varepsilon>0\), choose for each \(x\) a radius \(r_x>0\) such that \(|F(y)-F(x)|<\varepsilon/2\) when \(|y-x|<2r_x\) within the box. Finitely many balls \(B(x_j,r_{x_j})\) cover it. If \(|y-z|<\min_jr_{x_j}\), choose a ball containing \(y\); both \(y,z\) are within \(2r_{x_j}\) of its centre, giving \(|F(y)-F(z)|<\varepsilon\).

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
for a tagged partition, and let its mesh be the largest \(t_j-t_{j-1}\). Put \(\omega(\delta)=\sup\{|F(u)-F(v)|:|u-v|\leq\delta\}\), so \(\omega(\delta)\to0\). If a partition of mesh at most \(\delta\) is refined, expanding each original summand over its subintervals shows that its sum differs from any tagged refined sum by at most \((b-a)\omega(\delta)\). Two partitions of mesh at most \(\delta\) have a common refinement, so their sums differ by at most \(2(b-a)\omega(\delta)\). Sums along uniform partitions therefore converge by complex completeness; comparison with those sums shows that all tagged sums tend to the same limit as their meshes tend to zero. This defines \(\int_a^bF\). For real continuous \(F\), every tagged sum lies between its Darboux lower and upper sums, whose difference tends to zero by uniform continuity; thus this definition agrees with the real prerequisite's integral. For complex \(F\), passing real and imaginary parts through finite sums and their limits gives that prerequisite's componentwise complex integral. Passing the finite-sum identities to the limit proves linearity and commutation with constant multiplication. The finite-sum estimate
\(|S(F;\mathcal P)|\leq\sum_j(t_j-t_{j-1})|F(\xi_j)|\)
gives the stated modulus bound. In particular, a uniform change of size at most \(\eta\) changes the integral by at most \((b-a)\eta\), which proves the uniform-limit assertion. Splitting a partition at an interior point proves additivity over adjacent intervals. Define reversed integrals by changing sign.

*The fundamental theorem and the chain rule.* For interior \(t\) and nonzero small \(h\), the modulus of
\((P(t+h)-P(t))/h-F(t)\)
is at most \(\sup_{s\text{ between }t,t+h}|F(s)-F(t)|\), which tends to zero. This also gives the endpoint derivatives. To prove the converse, first recall the scalar mean value theorem: a continuous real function on an interval attains its extrema; if its endpoint values agree and it is not constant, some extremum is interior and its derivative is zero, since the two one-sided difference quotients have opposite signs. This is Rolle's theorem. Subtracting the line joining the endpoints gives the mean value theorem. Thus a scalar function with zero derivative is constant.

If \(G\) has continuous derivative \(F\), the function \(G-P\) has zero derivative. Its real and imaginary parts therefore have zero derivative, so each is constant by Corollary 9 of [Real analysis on closed intervals](real-analysis-on-closed-intervals.md). Thus \(G-P\) is constant, giving the converse fundamental theorem. For a differentiable real function \(\phi\), inserting
\(\phi(t+h)-\phi(t)=\phi'(t)h+o(|h|)\)
into the differentiability expansion of \(G\) proves \((G\circ\phi)'=(G'\circ\phi)\phi'\). The same calculation with complex increments proves the chain rule for a holomorphic \(G\) along a differentiable complex path. Continuity of the displayed derivative permits the fundamental theorem on each path piece. Real substitution follows by applying this chain rule to the primitive \(P(u)=\int_{u_0}^uF(v)\,dv\). No monotonicity of \(\phi\) is needed for the oriented identity.

*Rectangles.* Joint uniform continuity makes \(x\mapsto\int_c^dF(x,y)\,dy\) continuous, since the modulus of a difference is at most \((d-c)\sup_y|F(x,y)-F(x',y)|\); the analogous statement holds in the other variable. Approximate \(F\) by the function constant on each cell of a rectangular grid, using a value of \(F\) at a corner of that cell. Give boundary points a consistent half-open-cell convention, with the final cells closed at the outer boundary. For grid mesh \(\delta\), the uniform error is at most the modulus of continuity at \(\sqrt2\delta\). A one-variable step function with \(m\) division points is Riemann integrable: in a partition of mesh \(\eta\), intervals meeting those points have total length at most \(2m\eta\); all other summands give exactly the appropriate constant times length. The error on the exceptional intervals tends to zero, since the finitely many values are bounded. Each iterated integral of the rectangular step function is consequently the same finite sum
\(\sum_{i,j}(t_i-t_{i-1})(s_j-s_{j-1})F(t_{i-1},s_{j-1})\).
Both iterated integrals of \(F\) differ from this sum by at most the area of the rectangle times that modulus, which tends to zero. This proves (3), in the stated scalar setting. \(\square\)

## The index and the circle

For a cycle \(\Gamma\) and \(z\notin\Gamma^*\), the *index* is
\[
\operatorname{Ind}_\Gamma(z)=\frac1{2\pi i}\int_\Gamma\frac{d\lambda}{\lambda-z}.
\]

**Lemma 1.1.**
1. \(\operatorname{Ind}_\Gamma\) takes integer values on \(\mathbb C\setminus\Gamma^*\), is constant on each connected component, and is \(0\) on the unbounded component.
2. For the circle \(\partial D(c,r)\), the index is \(1\) on \(D(c,r)\) and \(0\) outside \(\bar D(c,r)\).

**Proof.** If the cycle has no paths, its integral and index are zero, so (1) holds immediately. Otherwise, (1) *Integer values.* Let \(\gamma:[a,b]\to\mathbb C\) be a closed path and \(z\notin\gamma^*\). Put
\[
\begin{gathered}
h(t)\\
=\int_a^t\frac{\gamma'(s)}{\gamma(s)-z}\,ds,\\
F(t)\\
=e^{-h(t)}(\gamma(t)-z).
\end{gathered}
\]
Wherever \(\gamma\) is differentiable, \(F'=e^{-h}\big(-h'(\gamma-z)+\gamma'\big)=0\). On each differentiable piece the real and imaginary parts of \(F\) are constant by the real mean value theorem; continuity joins their constants across the finitely many endpoints. Since \(\gamma(b)=\gamma(a)\neq z\), \(F(b)=F(a)\) gives \(e^{-h(b)}=1\). Corollary 5 of [The complex exponential and the circle](complex-exponential-and-the-circle.md) gives \(h(b)/(2\pi i)\in\mathbb Z\). The index of a cycle is a sum of such integers.

*Constancy.* A path image is compact, since an open cover pulls back to an open cover of its closed parameter interval and hence has a finite subcover. A finite union of these images is compact and bounded. For a point off the images the distance function attains a positive minimum on each interval, by the real extreme-value theorem. Let \(d(z)=\operatorname{dist}(z,\Gamma^*)\). For \(z,w\notin\Gamma^*\),
\[
\begin{gathered}
|\operatorname{Ind}_\Gamma(z)-\operatorname{Ind}_\Gamma(w)|\\
=\frac1{2\pi}\Big|\int_\Gamma\frac{(z-w)\,d\lambda}{(\lambda-z)(\lambda-w)}\Big|\\
\leq\frac{\ell(\Gamma)|z-w|}{2\pi d(z)d(w)} .
\end{gathered}
\]
So the index is continuous. A continuous integer-valued function is constant on connected sets: the inverse images of the separated integer values would otherwise disconnect the set. Choose \(R\) with \(\Gamma^*\subseteq\bar D(0,R)\). The exterior of this disc is connected by radial segments and circle arcs, using the polar form from the exponential prerequisite. Every unbounded component meets that exterior, so there is exactly one unbounded component. Since \(d(z)\geq|z|-R\), the estimate \(|\operatorname{Ind}_\Gamma(z)|\leq\ell(\Gamma)/(2\pi d(z))<1\) for sufficiently large \(|z|\) forces its integer value to be zero there and hence on that component.

(2) At the centre, \(\frac1{2\pi i}\int_0^{2\pi}\frac{ire^{it}}{re^{it}}\,dt=1\). The open disc is connected because segments join its points. Outside the closed disc, join two points radially to a circle of sufficiently large radius, then along an arc of that circle. The exponential prerequisite's polar form supplies the arc, so the exterior is connected and unbounded. These paths imply connectedness because a hypothetical separation would separate their parameter intervals, contradicting the intermediate-value theorem. Apply (1). \(\square\)

## Cauchy's theorem in convex sets

**Theorem 2.1** (Goursat). Let \(V\) be open, \(p\in V\), and \(f:V\to\mathbb C\) continuous on \(V\) and holomorphic on \(V\setminus\{p\}\). Then \(\int_{\partial\Delta}f=0\) for every closed triangle \(\Delta\subseteq V\).

**Proof.** If the vertices are collinear, the three segments go back and forth along one segment, and the integrals cancel. Let \(\Delta\) be nondegenerate, with diameter \(d\) and perimeter \(\ell\).

*Case 1: \(p\notin\Delta\).* Let \(c=|\int_{\partial\Delta}f|\).
- The midpoints of the sides cut \(\Delta\) into four triangles. Oriented like \(\Delta\), their boundary integrals add up to \(\int_{\partial\Delta}f\), because the inner edges cancel. So one of them, \(\Delta_1\), has \(|\int_{\partial\Delta_1}f|\geq c/4\).
- Repeating this gives closed triangles \(\Delta\supseteq\Delta_1\supseteq\Delta_2\supseteq\cdots\) with \(|\int_{\partial\Delta_n}f|\geq c/4^n\), diameter \(d/2^n\) and perimeter \(\ell/2^n\).
- They have a common point \(z_0\in\Delta\): choose a point in each retained triangle and apply the coordinatewise bounded-subsequence assertion of the real prerequisite's Theorem 3. For each fixed \(m\), the subsequence eventually lies in \(\Delta_m\). A closed triangle is an intersection of three closed affine half-planes, so its limit lies in every \(\Delta_m\). As \(p\notin\Delta\), \(z_0\ne p\). Write \(R(z)\) for \(f(z)-f(z_0)-f'(z_0)(z-z_0)\). Given \(\varepsilon>0\), choose \(\delta>0\) with
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

A continuous function has an attained finite maximum of its modulus on the closed triangle. Indeed, an unbounded sequence of values would have a convergent subsequence of input points in that closed triangle and contradict continuity. Once boundedness is established, a sequence of values approaching the supremum has such a subsequence, whose limit attains the supremum. These are the bounded-subsequence and limit arguments of the real prerequisite.

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

## Power series

For \(0<q<1\) and an integer \(k\geq0\), choose \(q<s<1\). For sufficiently large \(n\), the limit rules in the real prerequisite give
\[
\frac{(n+1)^kq^{n+1}}{n^kq^n}=q(1+1/n)^k\leq s.
\]
Hence \(n^kq^n\) is eventually bounded by a constant times a geometric sequence \(s^n\). The earlier geometric-tail proof shows that it tends to zero and has a finite sum. This justifies the estimates in the next lemma.

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

## Source and next reading

The scalar programme proofs preserve the mathematical credit of Édouard Goursat and of the programme lesson's original writers. The full source lesson also credits John D. Dixon, Zuoqin Wang under Sigurdur Helgason's guidance, and Ilja Černý for its cycle-theorem comparisons; those later comparisons are outside this selection. Links to freely readable versions of their works appear in the [source and edition notice](assets/notices/scalar-cauchy-source-notice.html).

Continue with [Holomorphic functions and convergent power series](holomorphic-power-series.md).
