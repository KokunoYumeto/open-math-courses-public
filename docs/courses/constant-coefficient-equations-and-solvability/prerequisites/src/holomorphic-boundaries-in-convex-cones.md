# Holomorphic boundaries in convex cones

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

In several variables a boundary can be approached through many imaginary directions. A proof along each fixed ray does not by itself prove that the same limit exists as the ray moves toward the edge of a cone. Convexity supplies a useful replacement: add one fixed interior direction to every approach, then use a test polynomial along that direction. The resulting integral has a bound independent of the approaching direction.

We use Cauchy kernels and distributional boundary limits for the one-variable finite-test calculation and circle formula, and Gluing holomorphic sides for one-variable zero-boundary uniqueness. [Chakrabarti and Shafikov 2017], Introduction and §2.6, provides primary human context for distributional holomorphic boundaries and their relation to weak Cauchy–Riemann derivatives. We prove the convex-cone boundary theorem directly below. Entry prerequisites are ordinary convex geometry, multivariable calculus and dominated convergence.

Basic references are Chakrabarti and Shafikov’s paper cited below and Avi Zeff’s *Lecture 12: Pompeiu’s formula* (2026), for the complex integral identity.

## An interior direction separates a proper cone from its opposite

Let \(\Gamma\subset\mathbb R^n\), \(n\geq1\), be a nonempty open convex cone. By a cone we mean that \(t\Gamma=\Gamma\) for every \(t>0\). Convexity and scaling give \(\Gamma+\Gamma\subset\Gamma\). There are two cases. If \(0\in\Gamma\), a ball about zero lies in \(\Gamma\), and scaling that ball gives \(\Gamma=\mathbb R^n\). Otherwise we call the cone proper here; this word does not require its closure to contain no lines.

**Lemma 1.1 (one uniform separation bound).** If \(0\notin\Gamma\) and \(Y\in\Gamma\), then

\[
d=\operatorname{dist}(-Y,\overline\Gamma)>0,
\qquad |y+tY|\geq dt
\quad(y\in\Gamma,\ t>0).
\tag{1.1}
\]

In particular \(t\leq d^{-1}|y+tY|\), uniformly for every direction \(y\) in the cone.

**Proof.** First \(\Gamma+\overline\Gamma\subset\Gamma\). To see this, fix \(v\in\Gamma\) and \(w\in\overline\Gamma\). Choose a ball about \(v\) in \(\Gamma\), and a sequence \(w_j\in\Gamma\) tending to \(w\). For large \(j\), the vector \(v+w-w_j\) lies in that ball. Adding \(w_j\) shows that \(v+w\in\Gamma\). If \(-Y\in\overline\Gamma\), this property would give \(0=Y-Y\in\Gamma\), a contradiction. Since \(\overline\Gamma\) is closed, a point outside it has a positive distance from it. Finally \(y/t\in\Gamma\), so \(|y+tY|=t|y/t+Y|\geq td\). \(\square\)

For the first quadrant in \(\mathbb R^2\), taking \(Y=(1,1)\) gives \(d=\sqrt2\). The bound remains valid for \(y=(r,r^2)\) as \(r\downarrow0\), although the direction of this vector tends to the edge of the quadrant.

## One test polynomial handles every direction of approach

Let \(X\subset\mathbb R^n\) be open, let \(\gamma>0\), and consider the tube

\[
T_\Gamma(X,\gamma)=
\{x+iy:x\in X,\ y\in\Gamma,\ |y|<\gamma\}.
\tag{2.1}
\]

We use holomorphic functions on this open subset of \(\mathbb C^n\). The calculations require the ordinary Cauchy–Riemann relations in each coordinate, and their local power-series consequence is recalled in Section 3. Suppose that for an integer \(N\geq0\),

\[
|f(x+iy)|\leq C|y|^{-N}
\quad(x+iy\in T_\Gamma(X,\gamma),\ y\ne0).
\tag{2.2}
\]

**Theorem 2.1 (full cone boundary limit).** For every \(\phi\in C_c^{N+1}(X)\), the limit

\[
\langle f_0,\phi\rangle
=\lim_{y\in\Gamma,\ |y|\to0}
\int_X f(x+iy)\phi(x)\,dx
\tag{2.3}
\]

exists. All directions and paths inside \(\Gamma\) are allowed. On smooth tests this is a distribution of order at most \(N+1\). The pairings have a common \(C^{N+1}\) norm bound on each fixed compact support for every sufficiently small \(y\in\Gamma\).

**Proof.** First suppose \(0\notin\Gamma\). Fix any \(Y\in\Gamma\), take its constant \(d\) from Lemma 1.1, and choose \(T>0\) with \(T|Y|<\gamma/2\). Restrict approaching vectors to \(|y|<\gamma/2\) and, if necessary, to a still smaller neighborhood ensuring \(|y|+T|Y|<\gamma\). Put \(D_Y=Y\cdot\nabla_x\) and define

\[
\Phi_Y(x,t)=\sum_{j=0}^N
\frac{(it)^j}{j!}D_Y^j\phi(x).
\tag{2.4}
\]

The imaginary path \(y+tY\) stays in \(\Gamma\) and within the tube height for \(0\leq t\leq T\). Real support stays in \(X\). Differentiation of
\(A_y(t)=\int_X f(x+i(y+tY))\Phi_Y(x,t)\,dx\), using the directional Cauchy–Riemann equation and compact-support integration by parts, gives the exact cancellation

\[
A_y'(t)=
-\frac{i^{N+1}t^N}{N!}
\int_X f(x+i(y+tY))D_Y^{N+1}\phi(x)\,dx.
\tag{2.5}
\]

Indeed its integrand after integration by parts is \(f(\partial_t\Phi_Y-iD_Y\Phi_Y)\); every term but the last cancels. This computation uses only derivatives through \(N+1\), so it applies to the finite-regularity tests stated in the theorem. Integrating (2.5) yields

\[
\begin{aligned}
\int_X f(x+iy)\phi(x)\,dx
={}&\int_X f(x+i(y+TY))\Phi_Y(x,T)\,dx\\
&+\frac{i^{N+1}}{N!}\int_0^T t^N
\int_X f(x+i(y+tY))D_Y^{N+1}\phi(x)\,dx\,dt.
\end{aligned}
\tag{2.6}
\]

By (2.2) and Lemma 1.1,

\[
t^N|f(x+i(y+tY))|\leq Cd^{-N}.
\tag{2.7}
\]

This is a common integrable majorant on the test support times \((0,T)\), independent of the direction of \(y\). At each positive \(t\), continuity of \(f\) gives convergence to \(f(x+itY)\). The top term converges to its value at \(iTY\), a fixed interior height. Dominated convergence thus proves (2.3), with the explicit formula

\[
\begin{aligned}
\langle f_0,\phi\rangle
={}&\int_X f(x+iTY)\Phi_Y(x,T)\,dx\\
&+\frac{i^{N+1}}{N!}\int_0^T t^N
\int_X f(x+itY)D_Y^{N+1}\phi(x)\,dx\,dt.
\end{aligned}
\tag{2.8}
\]

To make the order bound explicit, let the support lie in a compact \(K\Subset X\), write \(|K|\) for its Lebesgue volume and put \(b=\sum_j|Y_j|\). The multinomial theorem gives \(\|D_Y^j\phi\|_\infty\leq b^j\|\phi\|_{C^{N+1}}\). The top height has magnitude at least \(dT\). Formula (2.6) therefore gives

\[
\left|\int_X f(x+iy)\phi(x)\,dx\right|
\leq C|K|\left(
(dT)^{-N}\sum_{j=0}^N\frac{(Tb)^j}{j!}
+\frac{Td^{-N}b^{N+1}}{N!}
\right)\|\phi\|_{C^{N+1}}.
\tag{2.9}
\]

For \(N=0\) every zeroth power is one. This proves the uniform test bound and continuity of the limit. Neither \(Y\) nor \(T\) affects the resulting distribution, since (2.8) is the limit of the same actual pairings. The argument proves the limit for every sequence or path tending to zero in the cone; equivalently, its epsilon-neighborhood definition follows by contradicting it with a sequence.

If \(0\in\Gamma\), then \(\Gamma=\mathbb R^n\), and the tube already contains \(X\) at real height. Smoothness makes \(f(x+iy)\) converge uniformly to \(f(x)\) on every compact real support. Its boundary is the ordinary order-zero trace. This proves the remaining case and the claimed weaker order bound. \(\square\)

**Corollary 2.2 (moving tests).** If \(\phi_y\) have a common compact support and converge to \(\phi\) in \(C^{N+1}\) as \(y\in\Gamma\) tends to zero, then their pairings in (2.3) tend to \(\langle f_0,\phi\rangle\).

**Proof.** The common bound (2.9), or the local order-zero bound in the full-space case, makes the pairing with \(\phi_y-\phi\) tend to zero. Theorem 2.1 handles the fixed test. \(\square\)

Bounds local in the real coordinate also suffice for local limits, provided each slightly larger compact real neighborhood has one bound valid for **all** small imaginary directions in the cone. The proof can then be applied to its tests, and uniqueness of limits glues the local distributions.

## A zero boundary cannot conceal a holomorphic function

We first record the elementary several-variable identity principle used below. On a polydisk whose closure lies in a holomorphic domain, apply the one-variable Cauchy formula successively in each variable. The integrations are over a compact product of circles, so Fubini applies to their bounded continuous integrands. Expanding each denominator by its geometric series gives

\[
f(z)=\sum_{\alpha\in\mathbb N^n}
c_\alpha(z-a)^\alpha,
\qquad |c_\alpha|\leq M\prod_{j=1}^n r_j^{-\alpha_j},
\tag{3.1}
\]

where \(M\) bounds \(f\) on the circle product and \(r_j\) are its radii. On every smaller polydisk, the product of the geometric majorants is summable; the same holds after any fixed number of derivatives, using the resulting polynomial factors in \(\alpha\). Thus the series and all of its differentiated series converge there uniformly, and \(c_\alpha=\partial_z^\alpha f(a)/\alpha!\). This argument also proves the power-series conclusion directly for a \(C^1\) function satisfying each coordinate Cauchy–Riemann equation, without assuming a separate Hartogs theorem.

**Lemma 3.1 (identity principle in the tube).** A holomorphic function on a connected open complex domain which is zero on a nonempty open subset is zero everywhere.

**Proof.** The set where every complex derivative, including the function, vanishes is closed by continuity. Formula (3.1) makes it open, because all coefficients vanish at each of its points. It is nonempty by the given open zero set. Connectedness makes it the whole domain. \(\square\)

**Theorem 3.2 (uniqueness, including local boundary vanishing).** Under (2.2), if \(f_0=0\) on \(X\), then \(f=0\) throughout the tube. If \(f_0\) vanishes on a nonempty open \(X_0\subset X\), then \(f=0\) over \(X_0\). If in addition \(X\) is connected, it follows that \(f=0\) throughout the tube and \(f_0=0\) throughout \(X\).

**Proof.** First take a proper cone and assume the boundary is zero on \(X\). Fix any \(y\in\Gamma\) with \(|y|<\gamma\), and any \(\phi\in C_c^\infty(X)\). Choose \(d_0>0\) so that translating its support by any vector of length less than \(d_0\) stays compactly inside \(X\). Define a function of one complex variable,

\[
Q(w)=\int_X\phi(x)f(x+wy)\,dx,
\quad |operatorname{Re}w|<\frac{d_0}{|y|},
\quad 0<\operatorname{Im}w<\frac\gamma{|y|}.
\tag{3.2}
\]

The support and height remain in the tube. On compact subsets of this rectangle, differentiation under the integral is justified by smoothness and a common compact integration support; hence \(Q\) is holomorphic. Its growth is bounded by \(C\|\phi\|_{L^1}|y|^{-N}(\operatorname{Im}w)^{-N}\).

For real \(a\) in the indicated interval and \(b>0\), change the real variable to obtain

\[
Q(a+ib)=\int_X\phi(t-ay)f(t+iby)\,dt.
\tag{3.3}
\]

For each fixed \(a\), Theorem 2.1 makes this tend to \(\langle f_0,\phi(\cdot-ay)\rangle=0\). On each compact interval of \(a\), these translated tests have a common compact support and uniformly bounded \(C^{N+1}\) norms. The common estimate (2.9) therefore bounds \(Q(a+ib)\) uniformly there as \(b\downarrow0\). Dominated convergence shows that the one-variable distributional boundary of \(Q\) is zero on every compact test, including the \(C^{N+1}\) tests of the one-variable boundary theorem. The zero-boundary uniqueness theorem in the gluing lesson applies on this rectangle and gives \(Q=0\).

In particular \(w=i\) is inside the rectangle, since \(|y|<\gamma\). Thus \(\int_X\phi(x)f(x+iy)\,dx=0\) for every smooth compact \(\phi\). The continuous function \(f(\cdot+iy)\) is zero everywhere. Since \(y\) was arbitrary, \(f\) is zero throughout the tube.

For the full-space cone, the boundary is \(f|_X\). If this is zero, every real derivative on \(X\) is zero as well. The Cauchy–Riemann equations identify its complex derivatives with those real derivatives. Formula (3.1) therefore makes \(f\) zero on a complex neighborhood of every point of \(X\). For each component of \(X\), the corresponding tube is connected: the component is polygonally connected, and the imaginary ball is convex. Lemma 3.1 proves zero on that component’s tube. This gives the global assertion for the full-space case too.

If the boundary vanishes only on \(X_0\), restrict the entire argument to that open set; it proves zero over \(X_0\). When \(X\) is connected, it is polygonally connected as any connected open Euclidean set is: the points reachable from a given point by polygonal paths form a relatively open and closed subset. The set \(\Gamma\cap\{|y|<\gamma\}\) is convex and connected. Consequently the real-coordinate product describing the tube is connected. Its nonempty open zero region over \(X_0\) then propagates by Lemma 3.1. \(\square\)

The proof reduces uniqueness to a scalar holomorphic function only after establishing the uniform cone test bound. Pointwise limits for individual translated tests without that bound would not justify the dominated convergence step in (3.3).

## A slanted pole and a growth hypothesis that cannot be dropped

In the first quadrant \(\Gamma=\{y_1>0,y_2>0\}\), consider \(f(z_1,z_2)=(z_1+z_2)^{-m}\), \(m\geq1\). Since \(y_1+y_2\geq|y|\), it satisfies (2.2) with \(N=m\). Use real coordinates \(s=x_1+x_2\), \(t=x_2\), whose inverse has absolute Jacobian one. For a compact smooth test put

\[
\psi(s)=\int_{\mathbb R}\phi(s-t,t)\,dt.
\tag{4.1}
\]

Then the height pairing is the one-variable pairing of \((s+i(y_1+y_2))^{-m}\) with \(\psi\). Its boundary is therefore the upper finite-part pole from the Cauchy-kernel lesson, acting on this \(\psi\). For \(m=1\), the concentrated term is \(-i\pi\int\phi(-t,t)\,dt\), on the slanted line \(x_1+x_2=0\). Its ordinary Euclidean arclength element is \(\sqrt2\,dt\), so the measure in that concentrated term is arclength divided by \(\sqrt2\). No unchecked general distributional pullback is needed for this coordinate calculation.

By contrast, on the full half-space cone \(\{y_n>0\}\), the function \(1/z_n\) has the bound \(|f|\leq y_n^{-1}\), but not a bound \(C|y|^{-1}\) valid for all directions when \(n\geq2\) and the real base includes \(x_n=0\). Tangential imaginary components can dominate \(y_n\). This function can have boundary values, but the radial growth hypothesis of Theorem 2.1 cannot be justified by its normal-component bound alone.

## Exercises

**Exercise 1 (basic: cone separation).** For the first quadrant and \(Y=(2,1)\), compute \(\operatorname{dist}(-Y,\overline\Gamma)\). Check (1.1) directly, and explain why the proof does not require the cone closure to contain no lines.

**Exercise 2 (intermediate: a direction tending to an edge).** Let \(y(r)=(r,r^3)\) in the first quadrant. For \(f(z_1,z_2)=1/(z_1+z_2)\), express its height pairing using (4.1), and give its boundary limit. Identify the parameter that tends to zero in the one-variable pole formula.

**Exercise 3 (advanced: the directional cancellation).** Expand (2.4) for \(N=2\) and verify \(\partial_t\Phi_Y-iD_Y\Phi_Y=-i^3t^2D_Y^3\phi/2\). Derive (2.6), keeping the top-minus-bottom integration direction and its resulting plus sign.

**Exercise 4 (intermediate: normal growth versus radial growth).** In dimension two, take the half-space cone \(y_2>0\), \(f(z)=1/z_2\), and real coordinate \(x_2=0\). Find an approach \(y(r)\to0\) showing that no fixed bound \(C|y|^{-1}\) can hold. Explain which hypothesis fails and which conclusion cannot be inferred from this theorem alone.

**Exercise 5 (advanced: the translated-test step).** In (3.3), let \(a\) vary in a compact subinterval of its domain. Prove that the translated tests have one common compact support in \(X\) and one common \(C^{N+1}\) bound. Use these facts to show that \(Q\) has zero distributional boundary on that interval.

**Exercise 6 (intermediate: the slanted delta coefficient).** For \(m=1\) in (4.1), compute the concentrated part of the boundary pairing on a product test \(\phi(x_1,x_2)=u(x_1)v(x_2)\). Compare its measure to Euclidean arclength on the line. Then give the concentrated term for \(m=2\) as a pairing with \(\psi'(0)\), checking the delta-derivative sign.

## Complete solutions

**Solution 1.** The point \(-Y=(-2,-1)\) has closest point \((0,0)\) in the closed first quadrant, so its distance is \(\sqrt5\). For positive \(y_1,y_2,t\), each coordinate of \(y+tY\) is larger than the corresponding coordinate of \(tY\), so its squared norm is at least \(5t^2\). Thus (1.1) holds with \(d=\sqrt5\). In general the argument only excludes \(-Y\) from the closure; an open half-space cone, whose closure contains tangential lines, also satisfies this separation for each interior \(Y\).

**Solution 2.** Changing to \(s=x_1+x_2\), \(t=x_2\), gives \(\int (s+i(r+r^3))^{-1}\psi(s)\,ds\). The positive height parameter is \(r+r^3\), which tends to zero. Its limit is \(\langle\operatorname{pv}(1/s),\psi\rangle-i\pi\psi(0)\), where \(\psi(0)=\int\phi(-t,t)\,dt\). Although the direction of \(y(r)\) tends to the horizontal edge, its height parameter is positive and the full cone bound applies uniformly.

**Solution 3.** The polynomial is \(\Phi_Y=\phi+itD_Y\phi-t^2D_Y^2\phi/2\). Its \(t\)-derivative is \(iD_Y\phi-tD_Y^2\phi\), while \(iD_Y\Phi_Y=iD_Y\phi-tD_Y^2\phi-it^2D_Y^3\phi/2\). Subtracting leaves \(it^2D_Y^3\phi/2=-i^3t^2D_Y^3\phi/2\). Therefore \(A_y(T)-A_y(0)=-i^3\int_0^T t^2\int fD_Y^3\phi/2\). Solving for \(A_y(0)\) puts that last integral on the other side with coefficient \(+i^3/2\), which is (2.6) at \(N=2\).

**Solution 4.** Set \(y(r)=(r,r^2)\), with \(0<r<1\). At \(x_2=0\), \(|f|=r^{-2}\), whereas \(|y(r)|=r\sqrt{1+r^2}\). The product \(|y(r)||f|=\sqrt{1+r^2}/r\) is unbounded. Hence no fixed \(C\) gives the radial exponent-one bound. The normal-coordinate bound \(|f|\leq y_2^{-1}\) remains true, but it is not (2.2). This theorem alone consequently does not establish a full-cone boundary limit for that example; the exercise does not assert nonexistence of such a limit by other methods.

**Solution 5.** If \(|a|\leq A<d_0/|y|\), the union of the supports is contained in the continuous image of \(\operatorname{supp}\phi\times[-A,A]\) under \((x,a)\mapsto x+ay\). This is a compact set inside \(X\) by the choice of \(d_0\). Translation preserves each global derivative supremum, so its \(C^{N+1}\) norms all equal the norm of \(\phi\). Formula (2.9) now bounds \(Q(a+ib)\) uniformly for small \(b\), while its pointwise limit is zero because \(f_0=0\). For any compact test \(\theta(a)\) in this interval, the integrands \(Q(a+ib)\theta(a)\) have an integrable fixed majorant and converge pointwise to zero. Dominated convergence gives their integral tending to zero, which is the zero one-variable boundary distribution.

**Solution 6.** For \(m=1\), the concentrated pairing is \(-i\pi\psi(0)=-i\pi\int u(-t)v(t)\,dt\). The line parametrization \((-t,t)\) has speed \(\sqrt2\), so its parameter measure is \(dS/\sqrt2\), not \(dS\). For \(m=2\), the upper pole contains \(+i\pi\delta'_0\) in the \(s\) coordinate. Its pairing is \(-i\pi\psi'(0)\), since the first delta derivative pairs with a negative derivative. Here \(\psi'(0)=\int u'(-t)v(t)\,dt\), giving the concentrated term explicitly.

## References

- [Debraj Chakrabarti and Rasul Shafikov, *Distributional boundary values of holomorphic functions on product domains*, Mathematische Zeitschrift 286 (2017), 1145–1171](https://math.sci.uwo.ca/~shafikov/papers/MathZ2017.pdf). The introduction and §2.6 discuss the boundary-current setting and its Cauchy–Riemann derivative relation. That theorem concerns generic corners and currents; the finite-test cone limit and uniqueness above have their own proofs.
- *Cauchy kernels and distributional boundary limits*, Theorem 3.1 and Corollary 4.2. The one-variable cancellation and normalized pole limits used here.
- *Gluing holomorphic sides*, Corollary 3.3. The exact one-variable zero-boundary result used for \(Q\) in (3.2).
- [Avi Zeff, *Lecture 12: Pompeiu’s formula*, March 6, 2026](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html). The complex integral identity underlying the one-variable prerequisites.

[Chakrabarti and Shafikov 2017]: https://math.sci.uwo.ca/~shafikov/papers/MathZ2017.pdf
