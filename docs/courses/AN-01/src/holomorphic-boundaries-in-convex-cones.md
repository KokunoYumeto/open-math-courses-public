# Holomorphic boundaries in convex cones

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. The earlier edition was written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original lesson exposition and exercises: CC0. The separately credited programme prerequisites retain their own licences.*

A boundary approached through a cone can be approached along directions which themselves tend to its edge. We prove convergence on finite-regularity tests with an estimate uniform over those directions. One interior cone vector and a finite test polynomial suffice. We then prove that a zero boundary determines the zero holomorphic function, including when the real base is disconnected.

The exact earlier proofs used here are the finite-test boundary and pole formulas, circle Cauchy formula and scalar power-series estimates in [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), and the zero-boundary uniqueness theorem in [Gluing holomorphic sides](gluing-holomorphic-sides.md). The graph-area formula in [Boundary flux and weak identities](boundary-flux-and-weak-identities.md) supplies the slanted-line measure below. Their included foundation selections prove the scalar calculus, compactness, Lebesgue convergence and affine integration rules used here. No external reference replaces these proofs.

For the analytic starting convention, a holomorphic function is jointly continuous and complex differentiable on each coordinate slice. A complex Fréchet differentiable function has these properties by restricting its derivative to a coordinate line; a \(C^1\) function satisfying every coordinate Cauchy–Riemann equation has them by the one-variable result. The independent polydisk argument in Section 3 proves smoothness and local power series from this convention using only the earlier one-variable Cauchy formula. Its conclusion justifies the differentiations below, without an unproved separate-holomorphy theorem.

## An interior direction separates a proper cone from its opposite

Let \(\Gamma\subset\mathbb R^n\), \(n\ge1\), be nonempty, open and convex, with \(t\Gamma=\Gamma\) for every \(t>0\). Convexity followed by scaling gives
\(v+w=2((v+w)/2)\in\Gamma\) for \(v,w\in\Gamma\). If \(0\in\Gamma\), a ball about zero lies in \(\Gamma\); dilating this ball reaches every vector, so \(\Gamma=\mathbb R^n\). In the other case we call the cone *proper* in this lesson. Its closure is allowed to contain lines.

**Lemma 1.1 (one uniform separation bound).** For a proper cone and \(Y\in\Gamma\),

\[
 d=\operatorname{dist}(-Y,\overline\Gamma)>0,
 \qquad |y+tY|\ge dt\quad(y\in\Gamma,\ t>0).
 \tag{1.1}
\]

**Proof.** First prove \(\Gamma+\overline\Gamma\subset\Gamma\). For \(v\in\Gamma\), choose \(\varepsilon>0\) with \(B(v,\varepsilon)\subset\Gamma\). If \(w\in\overline\Gamma\), choose \(w_j\in\Gamma\) with \(w_j\to w\), using balls of radii \(1/j\) about \(w\). For large \(j\), the point \(v+w-w_j\) lies in that ball about \(v\). Adding \(w_j\in\Gamma\) gives \(v+w\in\Gamma\). If \(-Y\) belonged to \(\overline\Gamma\), this sum rule would give zero in \(\Gamma\), a contradiction. The complement of the closed set \(\overline\Gamma\) contains a ball about \(-Y\), so its distance from that set is positive. Finally \(y/t\in\Gamma\), and
\(|y+tY|=t|y/t+Y|\ge td\). \(\square\)

For the first quadrant in the plane and \(Y=(1,1)\), the distance is \(\sqrt2\). Thus (1.1) holds even for an approach such as \(y=(r,r^2)\), whose direction tends to an edge as \(r\downarrow0\).

## One test polynomial handles every direction of approach

Let \(X\subset\mathbb R^n\) be open and \(\gamma>0\). Define

\[
 T_\Gamma(X,\gamma)
   =\{x+iy:x\in X,\ y\in\Gamma,\ |y|<\gamma\}.
 \tag{2.1}
\]

Let \(f\) be holomorphic there. Suppose that for an integer \(N\ge0\),

\[
 |f(x+iy)|\le C|y|^{-N},\qquad y\ne0.
 \tag{2.2}
\]

Write \(p_m(\phi)=\max_{|\alpha|\le m}\|\partial_x^\alpha\phi\|_\infty\) for compactly supported tests. Their zero extensions are \(C^m\), since their supports lie compactly inside \(X\), as proved in the earlier finite-order lesson.

**Theorem 2.1 (full cone boundary limit).** For every \(\phi\in C_c^{N+1}(X)\),

\[
 f_0(\phi)=\lim_{y\in\Gamma,\ |y|\to0}
                        \int_X f(x+iy)\phi(x)\,dx
 \tag{2.3}
\]

exists along all directions and all paths within the cone. On each fixed compact support the pairings have one bound by \(p_{N+1}\), uniform for all sufficiently small \(y\in\Gamma\). The restriction of \(f_0\) to smooth tests is a distribution of order at most \(N+1\).

**Proof.** Suppose first that the cone is proper. Choose \(Y\in\Gamma\), its \(d>0\) from Lemma 1.1, and \(T>0\) with \(T|Y|<\gamma/2\). Consider \(|y|<\gamma/2\). For \(0<t\le T\), the sum rule and triangle inequality give
\(y+tY\in\Gamma\) and \(|y+tY|<\gamma\). At \(t=0\) the point is the original interior height. Put \(D_Y=\sum_jY_j\partial_{x_j}\) and

\[
 \Phi_Y(x,t)=\sum_{j=0}^N\frac{(it)^j}{j!}D_Y^j\phi(x).
 \tag{2.4}
\]

The support in \(x\) stays in the support of \(\phi\). For fixed nonzero \(y\), the parameter path and this support form a compact subset of the tube. Differentiation under its integral is justified by uniform convergence of difference quotients of the smooth integrand. The coordinate Cauchy–Riemann equations give
\(\partial_t f(x+i(y+tY))=iD_Yf(x+i(y+tY))\). Coordinate integration by parts gives

\[
 \begin{aligned}
 A_y(t)&=\int_X f(x+i(y+tY))\Phi_Y(x,t)\,dx,\\
 A_y'(t)&=-\frac{i^{N+1}t^N}{N!}
           \int_X f(x+i(y+tY))D_Y^{N+1}\phi(x)\,dx.
 \end{aligned}
 \tag{2.5}
\]

Indeed the factor left after integration by parts is
\(\partial_t\Phi_Y-iD_Y\Phi_Y=-i^{N+1}t^ND_Y^{N+1}\phi/N!\): the other powers cancel in pairs. Each term of \(\Phi_Y\) has at least one continuous spatial derivative, so this calculation is valid for the stated \(C^{N+1}\) tests. There are no end terms, because every test derivative is compactly supported. The fundamental theorem, solved for \(A_y(0)\), yields

\[
 \begin{aligned}
 \int_X f(x+iy)\phi(x)\,dx
 ={}&\int_X f(x+i(y+TY))\Phi_Y(x,T)\,dx\\
 &+\frac{i^{N+1}}{N!}\int_0^T t^N
           \int_X f(x+i(y+tY))D_Y^{N+1}\phi(x)\,dx\,dt.
 \end{aligned}
 \tag{2.6}
\]

For every positive \(t\), the actual growth hypothesis and (1.1) give the common estimate

\[
 t^N|f(x+i(y+tY))|\le Cd^{-N}.
 \tag{2.7}
\]

On the compact test support times \((0,T)\), this is an integrable majorant independent of the direction of \(y\). At positive \(t\), the point \(itY\) remains inside the tube, and continuity gives the pointwise limit of the integrand. At the top height, convergence is uniform over the compact real support: the set at height \(TY\) lies compactly inside the tube, and a small closed neighborhood of those points does too. Uniform continuity there applies. Dominated convergence therefore gives

\[
 \begin{aligned}
 f_0(\phi)={}&\int_X f(x+iTY)\Phi_Y(x,T)\,dx\\
 &+\frac{i^{N+1}}{N!}\int_0^Tt^N
                  \int_X f(x+itY)D_Y^{N+1}\phi(x)\,dx\,dt.
 \end{aligned}
 \tag{2.8}
\]

This holds for every sequence of vectors in the cone tending to zero. It gives the full neighborhood limit: if that limit failed, there would be some positive error and, for each integer \(l\), a vector of norm less than \(1/l\) with at least that error, contradicting the sequential conclusion.

For the explicit common bound, let \(K\Subset X\) contain the test support and set \(b=\sum_j|Y_j|\). Expanding \(D_Y^j\) as a product of \(j\) finite sums gives
\(\|D_Y^j\phi\|_\infty\le b^jp_{N+1}(\phi)\) for \(j\le N+1\): each ordered coordinate choice contributes a derivative of degree \(j\), and its absolute coefficients sum to \(b^j\). With \(|K|\) denoting Lebesgue volume, (2.6) and (2.7) give

\[
 \begin{aligned}
 \left|\int_X f(x+iy)\phi(x)\,dx\right|
 &\le C|K|\left[(dT)^{-N}\sum_{j=0}^N\frac{(Tb)^j}{j!}
           +\frac{Td^{-N}b^{N+1}}{N!}\right]p_{N+1}(\phi).
 \end{aligned}
 \tag{2.9}
\]

The top height has magnitude at least \(dT\). All zero powers are one, so the calculation includes \(N=0\). Passing to the limit proves continuity and the stated order. The value in (2.8) is independent of \(Y,T\), because every choice computes the limit of the same original pairings.

If \(0\in\Gamma\), the cone is all of \(\mathbb R^n\) and \(f\) is defined on a neighborhood of the real base. On each compact support it tends uniformly to its value at real height as \(y\to0\). This gives the ordinary order-zero trace and a common zeroth-order bound, proving all the assertions in this case. \(\square\)

**Corollary 2.2 (moving tests).** Suppose \(\phi_y,\phi\in C_c^{N+1}(X)\) have a common compact support and \(p_{N+1}(\phi_y-\phi)\to0\) as \(y\) tends to zero inside the cone. Then the pairing of \(f(x+iy)\) with \(\phi_y\) tends to \(f_0(\phi)\).

**Proof.** Subtract the pairing with \(\phi\). Estimate (2.9) makes this difference tend to zero, and Theorem 2.1 supplies the limit for the fixed test. In the full-space case use its common order-zero estimate. \(\square\)

The same proof works with bounds local in the real coordinate. Precisely, for every compact real support assume that a slightly larger compact real neighborhood has one polynomial bound valid for every sufficiently small imaginary direction in the cone. Restrict to an open neighborhood inside that compact set and choose \(T\) below its permitted height. The proof supplies its boundary pairings; definitions on overlaps agree as limits of the same pairings. On any fixed compact support one such neighborhood gives the distributional estimate. The requirement of uniformity over all small cone directions is retained.

## A zero boundary cannot conceal a holomorphic function

We first give the promised several-variable power-series proof. It uses no boundary result from this lesson.

**Polydisk Cauchy formula and smoothness.** Let the closed polydisk
\(\{|z_j-a_j|\le r_j, 1\le j\le n\}\) lie in an open holomorphic domain, with each \(r_j>0\). Denote the product of its positively oriented coordinate circles by \(\mathcal C\). Fix the other variables and apply the proved one-variable Cauchy formula in the first coordinate. Apply it next to the second coordinate of the integrand, then to the remaining coordinates. All intermediate choices of coordinates on the circles still lie in the original open domain. The integrands are continuous and bounded on compact products of circles, with denominators separated from zero for interior evaluation points. Parametrizing every circle by its angle makes absolute Fubini applicable. The result is

\[
 f(z)=\frac1{(2\pi i)^n}
       \int_{\mathcal C}\frac{f(\zeta)}{\prod_{j=1}^n(\zeta_j-z_j)}
                                 \,d\zeta_1\cdots d\zeta_n.
 \tag{C1}
\]

Here the integral means the iterated positively oriented circle integrals; no differential-form convention is needed. On a smaller closed polydisk \(|z_j-a_j|\le\rho_j<r_j\), with \(\rho_j>0\), expand each denominator into its geometric series. Its ratio has modulus at most \(\theta_j=\rho_j/r_j<1\). Products of finite partial sums have tails bounded by sums of the scalar geometric tails times the other convergent geometric sums. They therefore converge uniformly and absolutely on the circle product times the smaller polydisk. Integrate those partial sums in (C1) and pass the uniform limit. This gives

\[
 \begin{aligned}
 f(z)&=\sum_{\alpha\in\mathbb N^n}c_\alpha(z-a)^\alpha,\\
 c_\alpha&=\frac1{(2\pi i)^n}
       \int_{\mathcal C}\frac{f(\zeta)}
                         {\prod_j(\zeta_j-a_j)^{\alpha_j+1}}
                                  \,d\zeta_1\cdots d\zeta_n,\\
 |c_\alpha|&\le M\prod_jr_j^{-\alpha_j},\qquad
 M=\max_{\mathcal C}|f|.
 \end{aligned}
 \tag{3.1}
\]

In this lesson \(\mathbb N\) in a multi-index includes zero. The coefficient bound follows from the circle lengths \(2\pi r_j\) and the denominator moduli, proved in the scalar and one-variable prerequisites. Absolute summability means the same value is obtained under any enumeration: the tail outside a finite rectangular set has arbitrarily small absolute sum, so all finite sums containing that rectangle differ by arbitrarily little.

We check all derivatives explicitly. For a fixed multi-index \(\beta\), a differentiated monomial is zero unless \(\alpha\ge\beta\) coordinatewise. Otherwise its bound on the smaller polydisk is at most

\[
 M\prod_{j=1}^n
       \left[\rho_j^{-\beta_j}(\alpha_j+1)^{\beta_j}
                            \theta_j^{\alpha_j}\right].
 \tag{C2}
\]

For each coordinate the series \(\sum_{m\ge0}(m+1)^q\theta^m\) converges: the ratio of successive positive terms tends to \(\theta<1\), so beyond some index the terms are bounded by a geometric sequence of ratio strictly less than one. Products of these convergent nonnegative sums bound the full derivative series and its tails. Hence every differentiated series converges uniformly on smaller polydisks. Derivatives in the imaginary coordinate multiply the corresponding complex monomial derivative by \(i\), so the same estimates cover all real partial derivatives.

For completeness, termwise differentiation follows by passing uniform limits in the fundamental identity on a short real coordinate segment,
\(P_l(z+he_j)-P_l(z)=\int_0^h\partial_{x_j}P_l(z+te_j)\,dt\), and then dividing by \(h\). The identical argument works for imaginary segments and for every derivative series. Continuity of the limits identifies all partial derivatives; telescoping along coordinate segments gives the full derivative, as in the supplied scalar foundation. Thus \(f\) is smooth, its complex derivatives commute, and
\(c_\alpha=\partial_z^\alpha f(a)/\alpha!\). This proves all the analytic facts used above from joint continuity and coordinate holomorphy, including the stated \(C^1\) Cauchy–Riemann starting case.

**Lemma 3.1 (identity principle in the tube).** A holomorphic function on a connected open complex domain which is zero on a nonempty open subset is zero everywhere.

**Proof.** Let \(E\) be the set where the function and every complex derivative are zero. Smoothness makes \(E\) relatively closed. At a point of \(E\), (3.1) has every coefficient zero, so \(f\) vanishes on a polydisk there. All derivatives then vanish on that polydisk, making \(E\) relatively open. Its nonemptiness and connectedness of the domain give the claim. \(\square\)

**Theorem 3.2 (uniqueness, including local boundary vanishing).** Under (2.2), if \(f_0=0\) on \(X\), then \(f=0\) throughout the tube. If \(f_0\) vanishes on a nonempty open \(X_0\subset X\), then \(f=0\) over \(X_0\). If \(X\) is connected, this local vanishing forces \(f=0\) on the whole tube and \(f_0=0\) on all of \(X\).

**Proof.** For a proper cone, assume first \(f_0=0\) on \(X\). Fix any \(y\in\Gamma\) with \(|y|<\gamma\), and \(\phi\in C_c^\infty(X)\). Compactness and openness give \(d_0>0\) so that the closed \(d_0\)-neighborhood of \(\operatorname{supp}\phi\) is compactly inside \(X\): finitely many balls inside \(X\) cover the support, or use its positive minimum distance to the closed complement; if the complement is empty choose any bounded neighborhood. Define

\[
 \begin{aligned}
 Q(w)&=\int_X\phi(x)f(x+wy)\,dx,\\
 |\operatorname{Re}w|&<d_0/|y|,\qquad
 0<\operatorname{Im}w<\gamma/|y|.
 \end{aligned}
 \tag{3.2}
\]

The integrand is defined as zero off the support of \(\phi\). The horizontal translations of that support remain in \(X\), and the imaginary part is a positive multiple of \(y\), so every required evaluation of \(f\) remains in the tube. On compact subrectangles of (3.2), all evaluation points lie compactly in the tube. Differentiation under the fixed compact integral is valid by the already proved smoothness and uniform difference quotients. The chain rule gives \(Q_b=iQ_a\) for \(w=a+ib\), so the one-variable Cauchy–Riemann theorem makes \(Q\) holomorphic. Its bound is
\(|Q(a+ib)|\le C\|\phi\|_{L^1}|y|^{-N}b^{-N}\).

Extend \(\phi\) by zero before changing the real variable. Its translated support is still inside \(X\), so the affine integration rule gives

\[
 Q(a+ib)=\int_X\phi(t-ay)f(t+iby)\,dt.
 \tag{3.3}
\]

For each fixed \(a\), Theorem 2.1 makes this tend to \(f_0(\phi(\cdot-ay))=0\). On a compact interval \(|a|\le A<d_0/|y|\), the supports lie in the compact set
\(\{x+ay:x\in\operatorname{supp}\phi, |a|\le A\}\subset X\), the continuous image of a compact product. Translation preserves each global derivative supremum of the zero extension. Thus (2.9) gives one bound for \(Q(a+ib)\) on that interval for all sufficiently small \(b>0\). Multiplying by any compact continuous one-variable test there gives an integrable fixed majorant. Dominated convergence proves that \(Q\) has zero distributional boundary. Its polynomial bound and Corollary 3.3 of the repaired gluing lesson imply \(Q=0\) on the rectangle.

The point \(w=i\) lies there because \(|y|<\gamma\). Consequently \(\int_X\phi(x)f(x+iy)\,dx=0\) for every compact smooth \(\phi\). A continuous function with all those pairings zero is pointwise zero: at a nonzero value, rotate its phase so its real part is positive in a small ball and integrate against a nonzero nonnegative bump there. This contradicts the zero pairings. The chosen \(y\) was arbitrary, proving global zero in the proper-cone case without connectedness of \(X\).

In the full-space case, the boundary is the ordinary restriction \(f|_X\). If it is zero, all its real \(x\)-derivatives on \(X\) are zero. The Cauchy–Riemann equations identify those with its complex derivatives, so (3.1) makes \(f\) zero on a complex neighborhood of each real point. Fix any \(x\in X\) and imaginary vector \(y\) with \(|y|<\gamma\). The conclusion is already true at \(y=0\). Otherwise choose \(d>0\) with \(B(x,d)\subset X\). The function \(w\mapsto f(x+wy)\) is holomorphic on
\(|\operatorname{Re}w|<d/|y|\), \(|\operatorname{Im}w|<\gamma/|y|\). It vanishes near \(w=0\). The one-variable identity principle makes it zero on this connected rectangle, which includes \(w=i\). Thus \(f(x+iy)=0\) for every such point, again without a connectedness assumption on \(X\).

If the boundary is zero only on \(X_0\), restrict the argument to that open set. It proves zero over \(X_0\). When \(X\) is connected, any two of its points can be joined by a polygonal path: the points reachable from one point form an open subset, since a small ball permits one more segment; every other reachability class is also open, so that subset has open complement. Connectedness makes it all of \(X\). The imaginary set \(\Gamma\cap B(0,\gamma)\) is nonempty and convex. Join two tube points by first following a real polygonal path at fixed imaginary height, then an imaginary segment at fixed real coordinate. This proves that the tube is path connected, hence connected, since the inverse images of a separation under a path would separate an interval. Its open zero subset over \(X_0\) therefore propagates throughout it by Lemma 3.1. The boundary of the resulting zero function is zero as well. \(\square\)

## A slanted pole and a growth hypothesis that cannot be dropped

In the planar first quadrant \(\Gamma=\{y_1>0,y_2>0\}\), let
\(f(z_1,z_2)=(z_1+z_2)^{-m}\), \(m\ge1\), on the real base \(\mathbb R^2\). The positive imaginary part of the denominator prevents poles in the tube. Also \(y_1+y_2\ge|y|\), by squaring both nonnegative sides, so (2.2) holds with \(N=m\). Use coordinates \(s=x_1+x_2\), \(t=x_2\). Their inverse is \((s-t,t)\), of absolute determinant one. For a compact smooth test define

\[
 \psi(s)=\int_{\mathbb R}\phi(s-t,t)\,dt.
 \tag{4.1}
\]

Restriction to a smaller open real base gives the same formula, extending its compact tests by zero first. The projection of the transformed compact support onto the \(s\)-axis is compact. All \(s\)-derivatives can be passed under an integral over one fixed compact \(t\)-interval by uniform difference quotients. Thus \(\psi\) is a compact smooth test. The proved affine integration formula and ordinary Fubini at positive height make the original pairing equal to the one-variable pairing of
\((s+i(y_1+y_2))^{-m}\) with \(\psi\). Its boundary is exactly the upper finite-part pole from the preceding Cauchy-kernel lesson, acting on \(\psi\).

For \(m=1\), the concentrated term is
\(-i\pi\int\phi(-t,t)\,dt\). The line is the graph \(x_1=-x_2\), whose graph-area density from U011 is \(\sqrt{1+(-1)^2}=\sqrt2\). Thus its parameter measure is Euclidean arclength divided by \(\sqrt2\). This derives the coefficient from the supplied graph formula without using an unproved general pullback rule for distributions.

Normal and radial growth are different. On the half-space cone \(y_n>0\), the function \(1/z_n\) satisfies \(|1/z_n|\le1/y_n\). For \(n\ge2\), that does not yield \(C|y|^{-1}\) uniformly in the cone when the real base meets \(x_n=0\). Tangential imaginary coordinates can be much larger than \(y_n\); Solution 4 gives an explicit approach. The theorem's growth hypothesis must be checked in its actual radial form. This failure is not a claim that boundary values cannot exist by a different argument.

## Exercises

1. **Cone separation — foundation.** For the first quadrant and \(Y=(2,1)\), find \(\operatorname{dist}(-Y,\overline\Gamma)\) and check (1.1) directly. Explain why closure lines are allowed in Lemma 1.1.
2. **An approach to an edge — intermediate.** Take \(y(r)=(r,r^3)\) and \(f(z)=1/(z_1+z_2)\). Express its pairing through (4.1) and compute the boundary, identifying the one-variable height parameter.
3. **Directional cancellation — advanced.** For \(N=2\), write \(\Phi_Y\) explicitly, differentiate it, and derive (2.6) with its exact sign.
4. **Normal versus radial growth — intermediate.** On \(y_2>0\), with \(f(z)=1/z_2\) and \(x_2=0\), give a path to zero disproving any bound \(C|y|^{-1}\). State precisely what the cone theorem does not establish from the normal bound alone.
5. **Translated tests — advanced.** Prove the common support and derivative bounds in (3.3) when \(a\) varies on a compact interval. Use them to justify the zero one-variable boundary of \(Q\).
6. **The slanted delta — intermediate.** For \(\phi(x_1,x_2)=u(x_1)v(x_2)\), compute the concentrated term of the simple slanted pole and its relation to arclength. For the double pole, give the concentrated pairing through \(\psi'(0)\), with the derivative sign checked.

## Complete solutions

**Solution 1.** For \((s,t)\) in the closed first quadrant,
\(|(s,t)-(-2,-1)|^2=(s+2)^2+(t+1)^2\ge5\), with equality at zero. The distance is \(\sqrt5\). For \(y_1,y_2>0\) and \(t>0\),
\(|y+t(2,1)|^2=(y_1+2t)^2+(y_2+t)^2\ge5t^2\), proving the bound directly. The general proof only excludes the single point \(-Y\) from the closed cone. For example an open half-space cone has tangential lines in its closure, yet the distance from \(-Y\) to that closure is the strictly positive normal coordinate of \(Y\).

**Solution 2.** The affine coordinates give
\(\int_{\mathbb R}(s+i(r+r^3))^{-1}\psi(s)\,ds\). Its positive height is \(r+r^3\to0\). The proved upper-pole formula gives

\[
 \operatorname{pv}(1/s)(\psi)-i\pi\psi(0),\qquad
 \psi(0)=\int_{\mathbb R}\phi(-t,t)\,dt.
\]

This is a path covered by the full-cone estimate even though its direction approaches an edge.

**Solution 3.** Here
\(\Phi_Y=\phi+itD_Y\phi-t^2D_Y^2\phi/2\). Its time derivative is \(iD_Y\phi-tD_Y^2\phi\), and
\(iD_Y\Phi_Y=iD_Y\phi-tD_Y^2\phi-it^2D_Y^3\phi/2\). Their difference is
\(it^2D_Y^3\phi/2=-i^3t^2D_Y^3\phi/2\). Thus (2.5) gives
\(A_y(T)-A_y(0)=-i^3\int_0^Tt^2\int fD_Y^3\phi/2\). Moving that integral to the other side yields the plus coefficient \(i^3/2\) in the formula for \(A_y(0)\), exactly (2.6).

**Solution 4.** Set \(y(r)=(r,r^2)\), \(0<r<1\). At \(x_2=0\), \(|f|=r^{-2}\) and \(|y(r)|=r\sqrt{1+r^2}\). Hence \(|y(r)||f|=\sqrt{1+r^2}/r\to\infty\). No fixed constant gives the asserted exponent-one radial bound, although \(|f|\le y_2^{-1}\) remains true. That normal estimate therefore does not verify hypothesis (2.2) with \(N=1\), and the theorem alone cannot be invoked on its basis to assert the full-cone limit. This does not prove nonexistence of a boundary by other methods.

**Solution 5.** With \(|a|\le A<d_0/|y|\), the translated supports lie in the continuous image of
\(\operatorname{supp}\phi\times[-A,A]\) under \((x,a)\mapsto x+ay\). This is compact and lies in the closed translation margin chosen inside \(X\). Every coordinate derivative of \(\phi(\cdot-ay)\) is the translate of the same derivative of \(\phi\), so its global supremum and therefore \(p_{N+1}\) are unchanged. Theorem 2.1 gives pointwise convergence of (3.3) to zero, and its common norm estimate gives a constant bound over this whole interval of \(a\) for small \(b\). For any compact continuous test \(\theta(a)\), the integrands \(Q(a+ib)\theta(a)\) are bounded by a constant times \(|\theta(a)|\), an integrable function. Dominated convergence makes their integrals tend to zero. In particular this holds for all smooth tests, proving the required zero boundary distribution.

**Solution 6.** For the simple pole the concentrated term is
\(-i\pi\psi(0)=-i\pi\int u(-t)v(t)\,dt\). The graph-area density is \(\sqrt2\), so the measure in this term is \(dS/\sqrt2\). The double upper pole has concentrated distribution \(+i\pi\delta'_0\) in the \(s\) coordinate. Since \(\delta'_0(\psi)=-\psi'(0)\), its concentrated pairing is
\(-i\pi\psi'(0)=-i\pi\int u'(-t)v(t)\,dt\). Passing the derivative under this compact integral is justified as in (4.1). Both the pole coefficient and the distributional derivative sign are retained.

## Programme proof locations and freely accessible sources

- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, Theorem 3.1, Corollary 3.2 and Section 4: the complete circle, finite Taylor-test boundary, moving-test and pole proofs. The lesson is CC0; its separately supplied scalar and integration foundations retain CC0 1.0.
- [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2 and Corollary 3.3: the complete one-variable identity and zero-boundary uniqueness arguments used for \(Q\). CC0.
- [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), graph surface measure and its flux proof: the exact arclength density used for the slanted pole. CC0, with separately credited foundational selections.
- Jiří Lebl, [*Tasty Bits of Several Complex Variables*, free author edition, version 3.4 (23 December 2020)](https://www.jirka.org/scv/scv-3.4.pdf), Theorem 1.1.4, Theorem 1.2.1 and Proposition 1.2.2. These supply the human comparison for polydisk Cauchy and power series. The full iteration, coefficients and derivative convergence required here are independently derived in (C1)–(C2) from the preceding programme circle theorem. No book excerpt is included.
- Debraj Chakrabarti and Rasul Shafikov, [*Distributional boundary values of holomorphic functions on product domains*, free author preprint, arXiv:1505.01230v1 (2015)](https://arxiv.org/abs/1505.01230v1), Introduction and Sections 2.5–2.6, for canonical extension and the boundary-current comparison. The directional cone limit and uniqueness in this lesson have the complete proofs above, with their actual radial hypothesis.
