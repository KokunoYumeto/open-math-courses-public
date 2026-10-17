# Monotone functions of two variables

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Proposition 3.3 of [Rank coordinates](rank-coordinates.md), in the chart given by two windows every other rank coordinate is a function that is monotone in each of the two variables. Such functions are differentiable almost everywhere: Saks proved this in the plane, and Chabrillac and Crouzeix stated it in all dimensions [BBL, Theorem 1(f) and Section 3]. This lesson proves it, following OpenAI's argument [OpenAI-HL, Section 4]: monotonicity bounds oscillations by increments, a covering argument makes the increments linear in the scale at almost every point, and Rademacher's theorem applies on the pieces where this happens. The lesson also proves that a map of the plane has a null set of critical values, among the points where it is differentiable, without any further regularity. Both statements are used in [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md).

From the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) we use: Lipschitz functions on subsets of \(\mathbb R^2\) extend to Lipschitz functions on \(\mathbb R^2\) [Fremlin, 262B(b)]; Rademacher's theorem, that a Lipschitz function on \(\mathbb R^2\) is differentiable almost everywhere [Fremlin, 262Q]; and Lebesgue's density theorem, that almost every point of a measurable set \(E\) satisfies \(|E\cap B(x,\delta)|/|B(x,\delta)|\to1\) [Fremlin, 261D(b)]. Here \(|\cdot|\) is Lebesgue measure, or outer measure for arbitrary sets.

## 1. A covering lemma

For a norm on \(\mathbb R^2\), a *ball* is a closed set \(B(x,r)=\{y:\|y-x\|\le r\}\), and \(5B\) is \(B(x,5r)\). We use the Euclidean norm, and the maximum norm, whose balls are the squares \(Q_r(x)=x+[-r,r]^2\).

**Lemma 1.1** (five times covering). Let \(\mathcal F\) be a family of balls of one norm with radii at most \(r_0<\infty\). There is a countable disjoint subfamily \(\mathcal G\) such that every ball of \(\mathcal F\) lies in \(5B'\) for some \(B'\in\mathcal G\).

*Proof.* Let \(\mathcal F_k\) be the balls with radius in \((2^{-k-1}r_0,2^{-k}r_0]\). Choose inductively a maximal disjoint subfamily \(\mathcal G_k\) of the balls of \(\mathcal F_k\) disjoint from all balls in \(\mathcal G_0\cup\dots\cup\mathcal G_{k-1}\); it is countable, since disjoint balls of radius at least \(2^{-k-1}r_0\) contain disjoint balls of rational centers. A ball \(B\in\mathcal F_k\) meets some ball \(B'\) of \(\mathcal G_0\cup\dots\cup\mathcal G_k\), by maximality; the radius of \(B'\) exceeds half the radius of \(B\), so \(B\subseteq5B'\). \(\square\)

## 2. Monotone functions

Let \(f\) be a bounded function on an open rectangle \(\Omega\subseteq\mathbb R^2\) which is monotone in each variable, nondecreasing or nonincreasing, the kind fixed for each variable. Reflecting a variable, we may assume \(f\) nondecreasing in both. Write \(u\le w\) when \(u_1\le w_1\) and \(u_2\le w_2\); then \(f(u)\le f(w)\) for \(u\le w\). Let \(\|f\|=\sup|f|\).

For \(x\) and \(r>0\) with \(Q_{2r}(x)\subseteq\Omega\) put
\[
\begin{aligned}
\Delta(x,r)&=f(x+(r,r))-f(x-(r,r))\\
&\ge0 .
\end{aligned}
\]
Every point of \(Q_r(x)\) lies between \(x-(r,r)\) and \(x+(r,r)\), so the oscillation of \(f\) on \(Q_r(x)\) is at most \(\Delta(x,r)\).

**Lemma 2.1.** For almost every \(x\in\Omega\) there are \(m_x,r_x>0\) with \(\Delta(x,r)\le m_xr\) for \(0<r<r_x\).

*Proof.* *Increments.* Put
\[
\begin{aligned}
H(x,r)&=\int_{x_2-2r}^{x_2+2r}\bigl(f(x_1+2r,y)\\
&\qquad\quad-f(x_1-2r,y)\bigr)\,dy,\\
V(x,r)&=\int_{x_1-2r}^{x_1+2r}\bigl(f(t,x_2+2r)\\
&\qquad\quad-f(t,x_2-2r)\bigr)\,dt .
\end{aligned}
\]
The integrands are monotone in one variable, hence Borel, and nonnegative. For \(u\) in the square \(x+[-2r,-r]^2\) of area \(r^2\), monotonicity gives \(u\le x-(r,r)\) and \(u+(3r,3r)\ge x+(r,r)\), so
\[
\begin{aligned}
\Delta(x,r)\le{}&\bigl(f(u_1+3r,u_2)\\
&\quad-f(u_1,u_2)\bigr)\\
&+\bigl(f(u_1+3r,u_2+3r)\\
&\quad-f(u_1+3r,u_2)\bigr).
\end{aligned}
\]
In the first bracket \(u_1\ge x_1-2r\) and \(u_1+3r\le x_1+2r\), so it is at most \(f(x_1+2r,u_2)-f(x_1-2r,u_2)\); integrating over \(u\) gives at most \(rH(x,r)\). The second bracket is at most \(f(u_1+3r,x_2+2r)\) minus \(f(u_1+3r,x_2-2r)\), and integrates to at most \(rV(x,r)\). Hence
\[
r\Delta(x,r)\le H(x,r)+V(x,r).
\]

*Disjoint squares.* Let \(Q_{2r_i}(x_i)\) be disjoint squares in \(\Omega\). For a fixed \(y\), the horizontal intervals \([x_{i,1}-2r_i,x_{i,1}+2r_i]\) of those squares whose vertical range contains \(y\) are disjoint, so the corresponding increments of the nondecreasing function \(f(\cdot,y)\) add up to at most \(2\|f\|\). Integrating over \(y\) in the bounded vertical range \(h\) of \(\Omega\), \(\sum_iH(x_i,r_i)\le2\|f\|\,h\); similarly \(\sum_iV(x_i,r_i)\le2\|f\|\,w\), with \(w\) the width of \(\Omega\).

*Covering.* For \(m\ge1\) let \(E_m\) be the set of \(x\in\Omega\) for which \(H(x,r)+V(x,r)>mr^2\) for arbitrarily small \(r\). Applying Lemma 1.1 to the squares \(Q_{2r}(x)\subseteq\Omega\), \(x\in E_m\), with this property and \(r\le1\), gives disjoint squares \(Q_{2r_i}(x_i)\) whose fivefold enlargements cover \(E_m\), so
\[
\begin{aligned}
|E_m|&\le\sum_i(20r_i)^2\\
&<\frac{400}m\sum_i\bigl(H(x_i,r_i)+V(x_i,r_i)\bigr)\\
&\le\frac{800\|f\|(h+w)}m .
\end{aligned}
\]
The points outside \(\bigcap_mE_m\), a null set, have \(H+V\le m_xr^2\) for all small \(r\), hence \(\Delta(x,r)\le m_xr\). \(\square\)

**Theorem 2.2** (Saks; Chabrillac–Crouzeix). A bounded Borel function on an open rectangle in \(\mathbb R^2\) which is monotone in each variable is differentiable at almost every point.

*Proof.* Assume \(f\) nondecreasing in both variables, as above. For \(m\ge1\) let \(E_m\) be the set of points \(x\) with \(Q_{2/m}(x)\subseteq\Omega\) and \(\Delta(x,r)\le mr\) for every rational \(r\in(0,1/m)\). It is a Borel set, as a countable intersection of conditions on Borel functions of \(x\). By Lemma 2.1, the union of the \(E_m\) contains almost every point of \(\Omega\).

*Lipschitz pieces.* Let \(x\in E_m\) and \(y\in\Omega\) with \(\rho=\max(|y_1-x_1|,|y_2-x_2|)\). If \(\rho<1/m\), choose rational \(r\in[\rho,1/m)\) close to \(\rho\): \(|f(y)-f(x)|\le\Delta(x,r)\le mr\), so \(|f(y)-f(x)|\le m\rho\). If \(\rho\ge1/m\), \(|f(y)-f(x)|\le2\|f\|\le2\|f\|m\rho\). So the restriction of \(f\) to \(E_m\) is Lipschitz, and it extends to a Lipschitz function \(g_m\) on \(\mathbb R^2\) [Fremlin, 262B(b)], which is differentiable almost everywhere [Fremlin, 262Q].

*Squeezing.* Let \(x\in E_m\) be a point where \(g_m\) is differentiable and where \(E_m\) has density one [Fremlin, 261D(b)]; almost every point of \(E_m\) is such. Let \(\eta\in(0,\frac12)\). For small \(v\), the square \(y+[-\eta|v|,0]^2\), with \(y=x+v\), lies in \(B(x,2|v|)\) and has area \(\eta^2|v|^2\), a fixed fraction of the area of that ball; by density one it meets \(E_m\) once \(|v|\) is small. So there are points \(y^\pm\in E_m\) with \(y^-\le y\le y^+\) and \(|y^\pm-y|\le\sqrt2\,\eta|v|\). By monotonicity and \(f=g_m\) on \(E_m\),
\[
\begin{aligned}
&g_m(y^-)\le f(y)\le g_m(y^+),\\
&g_m(y^\pm)=g_m(x)\\
&\qquad+Dg_m(x)(y^\pm-x)+o(|v|),
\end{aligned}
\]
so
\[
\begin{aligned}
&|f(x+v)-f(x)-Dg_m(x)v|\\
&\quad\le\sqrt2\,\eta\,\|Dg_m(x)\|\,|v|+o(|v|).
\end{aligned}
\]
Since \(\eta\) is arbitrary, \(f\) is differentiable at \(x\) with derivative \(Dg_m(x)\). \(\square\)

## 3. Critical images

**Lemma 3.1** (critical images). Let \(\Omega\subseteq\mathbb R^2\) be open and \(F:\Omega\to\mathbb R^2\) any map. Let \(S\) be the set of points where \(F\) is differentiable with \(\operatorname{rank}DF(x)<2\). Then \(F(S)\) has outer measure zero, so it lies in a Borel null set.

*Proof.* Fix \(\rho,m\ge1\) and let \(S'\) be the set of \(x\in S\) with \(|x|<\rho\) and \(\|DF(x)\|\le m\). Fix \(\epsilon\in(0,1)\). For each \(x\in S'\) there are arbitrarily small \(r<1\) with \(B(x,5r)\subseteq\Omega\) and
\[
\begin{aligned}
&|F(y)-F(x)-DF(x)(y-x)|\\
&\quad\le\epsilon|y-x|
\end{aligned}
\]
for \(y\in B(x,5r)\). Lemma 1.1, for Euclidean balls, gives disjoint balls \(B(x_i,r_i)\) of this kind whose fivefold enlargements cover \(S'\). They lie in \(B(0,\rho+1)\), so \(\sum_i\pi r_i^2\le\pi(\rho+1)^2\). Since \(DF(x_i)\) has rank at most one, \(DF(x_i)(B(0,5r_i))\) lies in a segment of length \(10mr_i\), and \(F(B(x_i,5r_i))\) lies in the \(5\epsilon r_i\)-neighbourhood of a translate of it, whose area is at most \((100m\epsilon+25\pi\epsilon^2)r_i^2\). So the outer measure of \(F(S')\) is at most \((100m\epsilon+25\pi\epsilon^2)(\rho+1)^2\), for every \(\epsilon\). Take the union over \(\rho\) and \(m\). \(\square\)

This is the easy part of Sard's theorem, but without any continuity of \(F\) away from the point: only differentiability at the points of \(S\) is used. In the course, \(F\) is a pair of limits of rank coordinates, known to be differentiable almost everywhere but not continuous.

## 4. Exercises

**4.1** (easy). Show that \(f(x,y)=\mathbf 1_{x+y>0}\) is monotone in each variable, find where it is not differentiable, and check that this set is null.

**4.2** (medium). Show that Theorem 2.2 fails for functions monotone in one variable only: give a bounded Borel function on the square, nondecreasing in \(x\), that is differentiable nowhere.

**4.3** (easy). For \(F(x,y)=(x,x^2)\), describe \(S\) and \(F(S)\) in Lemma 3.1.

## 5. Solutions

**4.1.** Increasing \(x\) or \(y\) can only turn \(x+y>0\) from false to true. Off the line \(x+y=0\) the function is locally constant, hence differentiable; on the line it jumps. The line is null.

**4.2.** Let \(f(x,y)=x+\mathbf 1_{y\in\mathbb Q}\). For each fixed \(y\) it is increasing in \(x\), but at every point it is discontinuous in \(y\), hence not differentiable.

**4.3.** \(DF=\begin{pmatrix}1&0\\2x&0\end{pmatrix}\) has rank one everywhere, so \(S=\mathbb R^2\), and \(F(S)\) is the parabola \(\{(x,x^2)\}\), a null set.

## References

- [BBL] J. M. Borwein, J. V. Burke and A. S. Lewis, *Differentiability of cone-monotone functions on separable Banach space*, Proceedings of the American Mathematical Society 132 (2004), 1067–1076; Theorem 1(f) states the theorem for \(\mathbb R^n\), with its history in Section 3. https://sites.math.washington.edu/~burke/papers/reprints/46-cone-monotone.pdf
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, 261D(b) (density points), 262B(b) (Lipschitz extensions), 262Q (Rademacher's theorem); the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
