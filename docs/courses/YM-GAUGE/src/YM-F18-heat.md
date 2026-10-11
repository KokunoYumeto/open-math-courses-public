# SU(2) heat kernel and classical action

Complete companion to [Unit 18](../established-approaches-and-open-problems.html). The [holonomy chapter](../two-dimensional-holonomy-probability.html) supplies the graph probability and regularity arguments.

## HK.1. The group and the exact metric

Let

\[
 \sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 \sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
 \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Direct multiplication gives \(\sigma_a\sigma_b=\delta_{ab}I+i\sum_c\epsilon_{abc}\sigma_c\). Define

\[
 Q(q)=q_0I+i\sum_{a=1}^3q_a\sigma_a,
 \qquad q_0^2+q_1^2+q_2^2+q_3^2=1.                 \tag{H1}
\]

Then \(Q(q)^*=Q(q_0,-\boldsymbol q)\), \(Q(q)^*Q(q)=I\), and \(\det Q(q)=|q|^2=1\). Conversely every SU(2) matrix has the form \(\left(\begin{smallmatrix}z&w\\-\bar w&\bar z\end{smallmatrix}\right)\), \(|z|^2+|w|^2=1\), and uniquely has form (H1). Matrix multiplication gives

\[
 (a,\boldsymbol v)(b,\boldsymbol w)
 =(ab-\boldsymbol v\cdot\boldsymbol w,
       a\boldsymbol w+b\boldsymbol v-\boldsymbol v\times\boldsymbol w).
\]

The minus sign on the cross product follows from the chosen \(+i\sigma_a\) basis. Inverse is \((a,-\boldsymbol v)\). Both left and right multiplication are real linear norm-preserving maps of \(\mathbb R^4\), by \(Q^*Q=|q|^2I\).

The course metric is \(\kappa(X,Y)=-\operatorname{tr}(XY)\), using the two-dimensional defining trace. At the identity, \(X=i\boldsymbol x\cdot\boldsymbol\sigma\), \(Y=i\boldsymbol y\cdot\boldsymbol\sigma\), so

\[
 \kappa(X,Y)=2\boldsymbol x\cdot\boldsymbol y.      \tag{H2}
\]

Thus the resulting bi-invariant Riemannian metric is twice the unit-sphere metric on \(S^3\). In particular its radius is \(\sqrt2\), its total volume is \(4\sqrt2\pi^2\), and its Laplace operator is \(\Delta_\kappa=\tfrac12\Delta_{S^3}\). These factors are retained throughout.

## HK.2. A constructed Haar probability

For \(q=(\cos\theta,\sin\theta\,\boldsymbol n)\), \(0<\theta<\pi\), \(\boldsymbol n\in S^2\), the ordinary sphere area element is \(\sin^2\theta\,d\theta\,d\Omega(\boldsymbol n)\). Its mass is \(4\pi\int_0^\pi\sin^2\theta\,d\theta=2\pi^2\). Define the Borel probability

\[
 d\mu(q)=\frac{\sin^2\theta}{2\pi^2}\,d\theta\,d\Omega(\boldsymbol n),
 \quad
 \int_G f(q_0)\,d\mu=\frac2\pi\int_0^\pi f(\cos\theta)\sin^2\theta\,d\theta.
                                                               \tag{H3}
\]

The two omitted poles have mass zero. The usual change of variables for orthogonal maps in \(\mathbb R^4\), or its restriction to sphere charts, proves invariance under every orthogonal map. HK.1 therefore proves left and right invariance under SU(2); inversion is also an orthogonal map. This is the Haar probability used here, obtained directly without a Haar existence theorem. Every nonempty sphere-open set contains a chart ball of positive area, hence has positive measure. Multiplication of the sphere metric by two multiplies the volume by \(2^{3/2}\); division by total volume leaves exactly (H3).

## HK.3. Polynomial completeness, with its approximation proof

Real coordinate polynomials restricted to \(S^3\) are uniformly dense in real continuous functions. Here are the details needed below. For continuous \(f\) let \(|f|\leq M\). Given \(\epsilon>0\), choose \(\delta>0\) such that \(|f(x)-f(y)|<\epsilon\) when \(|x-y|<\delta\). If \(M=0\) there is nothing to prove. Set \(L=2M/\delta\), and on a containing cube define

\[
 F(z)=\inf_{x\in S^3}\{f(x)+L|z-x|\}.
\]

The infimum is attained by compactness. The triangle inequality proves that \(F\) is \(L\)-Lipschitz. For \(z\in S^3\), the choice \(x=z\) gives \(F(z)\leq f(z)\). Points with \(|x-z|<\delta\) give \(f(x)+L|x-z|\geq f(z)-\epsilon\); the other points give at least \(-M+L\delta=M\geq f(z)\). Thus \(|F-f|\leq\epsilon\) on the sphere.

After an explicit affine change from the containing cube to \([0,1]^4\), approximate \(F\) by its multivariate Bernstein polynomial \(B_mF(x)=\mathbb E F(K_1/m,\ldots,K_4/m)\), where independent \(K_j\) have binomial parameters \((m,x_j)\). This expectation is a coordinate polynomial. Cauchy–Schwarz and \(\operatorname{Var}(K_j/m)=x_j(1-x_j)/m\) bound the error by the rescaled Lipschitz constant times \(\sqrt{4/(4m)}\). It tends to zero uniformly. Taking real and imaginary parts proves complex polynomial density.

These polynomials are also dense in \(L^2(S^3,\mu)\). To justify the intervening continuous-density statement, cover the sphere by finitely many coordinate patches whose compact subpatch interiors cover it. In each patch the measure has a smooth bounded density on smaller compact subsets. Bounded measurable functions there are approximable in \(L^2\) by finite step functions on boxes: subdivide boxes and use the defining simple-function approximation for Lebesgue integration; measurable sets admit finite unions of boxes up to arbitrarily small measure. Replace box indicators by continuous ramps supported in arbitrarily thin boundary strips. The strips have measure tending to zero, since their Euclidean volumes do and the density is bounded. A continuous partition of unity for this finite cover can be built by distances to the patch complements, divided by their positive sum. It combines the approximations. First truncate an arbitrary \(L^2\) function, and then remove small chart-edge subsets; their \(L^2\) contribution tends to zero by integrability. This proves the assertion with no representation-completeness assumption.

## HK.4. The entire spherical decomposition needed for heat flow

Let \(\mathcal P_n\) be the homogeneous complex polynomials of degree \(n\) in four variables, and \(\mathcal H_n=\ker(\Delta_{\mathbb R^4}:\mathcal P_n\to\mathcal P_{n-2})\). Polar-coordinate differentiation gives

\[
 \Delta_{\mathbb R^4}=\partial_r^2+\frac3r\partial_r+\frac1{r^2}\Delta_{S^3},
 \quad
 \Delta(r^{2k}H_l)=2k(2l+2k+2)r^{2k-2}H_l,          \tag{H4}
\]

where \(H_l\) is homogeneous harmonic of degree \(l\). For completeness, the first formula follows from the radial volume element \(r^3dr\,dS\): radial divergence is \(r^{-3}\partial_r(r^3\partial_r)\), and tangential inverse metric is \(r^{-2}\) times that of the sphere. Substitution of \(r^{l+2k}H_l|_{S^3}\) gives the second formula and also
\(\Delta_{S^3}(H_l|_{S^3})=-l(l+2)H_l|_{S^3}\).

Induction proves the direct decomposition \(\mathcal P_n=\mathcal H_n\oplus r^2\mathcal P_{n-2}\). Indeed, by the induction hypothesis decompose \(\Delta P\) into the terms \(r^{2k}H_l\) with \(l+2k=n-2\). Formula (H4) gives a unique preimage in \(r^2\mathcal P_{n-2}\) for each such term, since its displayed coefficient for \(k+1\) is nonzero. Subtract these preimages from \(P\) to obtain a harmonic polynomial. The same nonzero coefficients prove that the intersection is zero. Thus

\[
 d_n^{\rm harm}=\binom{n+3}{3}-\binom{n+1}{3}=(n+1)^2,
 \qquad \lambda_n=\frac{n(n+2)}2.                 \tag{H5}
\]

For \(n=0,1\) the second binomial is zero. Restriction to the sphere is injective for homogeneous polynomials. Harmonic restrictions of distinct degrees are orthogonal: write the sphere Laplacian as \(\sum_{i<j}(q_i\partial_j-q_j\partial_i)^2\). This equality follows by expanding the derivatives and restricting to homogeneous radially extended functions. Each first-order rotation generator is skew adjoint under the sphere integral, since its flow is an area-preserving rotation; differentiating \(\int f(R_sq)\bar g(R_sq)d\mu\) proves integration by parts. The Laplacian is therefore symmetric, and its distinct eigenvalues give orthogonality. HK.3 and the decomposition prove that the orthogonal sum of these finite-dimensional spaces is all \(L^2(G,\mu)\).

## HK.5. Characters and the exact projection kernel

Put \(d_n=n+1\) and define

\[
 \chi_n(\theta)=\frac{\sin((n+1)\theta)}{\sin\theta}=U_n(\cos\theta),
 \quad \chi_n(0)=n+1,\quad \chi_n(\pi)=(-1)^n(n+1).             \tag{H6}
\]

The endpoint values are limits. The recurrence \(U_0=1\), \(U_1=2x\), \(U_{n+1}=2xU_n-U_{n-1}\) proves this is a polynomial. Every SU(2) matrix is unitarily diagonalizable with eigenvalues \(e^{i\theta},e^{-i\theta}\); on the homogeneous symmetric power \(\operatorname{Sym}^n\mathbb C^2\) the eigenvalues are \(e^{i(n-2j)\theta}\), \(0\leq j\leq n\). Their sum is (H6). Thus these are actual representation traces, of dimension \(d_n\); no classification of all representations is needed here. Their absolute values are at most \(d_n\). Direct use of (H3) and sine orthogonality yields \(\int\chi_n\chi_m\,d\mu=\delta_{nm}\).

Let \(\phi_{n,j}\) be any orthonormal basis of the harmonic restrictions of degree \(n\). Their projection kernel \(K_n(q,q')=\sum_j\phi_{n,j}(q)\overline{\phi_{n,j}(q')}\) is invariant under simultaneous rotations in \(O(4)\). Fixing \(q'\), invariance under its stabilizer makes it a polynomial in \(z=q\cdot q'\): an invariant polynomial in the perpendicular three coordinates depends on their squared length, as follows by constancy on each sphere and polynomial restriction to an axis. On \(S^3\) that squared length is \(1-z^2\). The eigenvalue equation for this polynomial is
\((1-z^2)y''-3zy'+n(n+2)y=0\). Comparison of successive powers proves that its polynomial solution space of degree at most \(n\) is one-dimensional. The recurrence or direct differentiation shows that \(U_n\) solves it. The diagonal of \(K_n\) is constant by rotations and integrates to \((n+1)^2\); its value is therefore \((n+1)^2\). Since \(U_n(1)=n+1\),

\[
 K_n(q,q')=(n+1)\chi_n(Q(q)Q(q')^{-1}),\qquad |K_n(q,q')|\leq(n+1)^2.
                                                               \tag{H7}
\]

The scalar coordinate of \(Q(q)Q(q')^{-1}\) is exactly \(q\cdot q'\). This proves the non-Abelian convolution identities used next directly from orthogonal projections.

## HK.6. Definition, convergence and convolution

For dimensionless \(t>0\), define

\[
 p_t(g)=\sum_{n=0}^\infty (n+1)e^{-t n(n+2)/2}\chi_n(g),
 \quad (T_tf)(q)=\int_G p_t(qq'^{-1})f(q')d\mu(q').             \tag{H8}
\]

For \(t\geq\epsilon>0\), the absolute bound \(\sum(n+1)^2e^{-\epsilon n(n+2)/2}<\infty\) proves uniform convergence. Arbitrarily many time derivatives are permitted by multiplying this majorant by powers of \(\lambda_n\). Spatial derivatives are also allowed: the recurrence for \(U_n\) bounds its coefficients and each fixed-order derivative on bounded coordinate sets by a constant to the power \(n\) times a polynomial in \(n\); the Gaussian factor in \(n\) dominates it. Thus the kernel is smooth for \(t>0\). It is real, central and inverse-invariant.

Equation (H7) gives \(T_t=\sum_n e^{-t\lambda_n}\Pi_n\) on the full orthogonal decomposition. Consequently \(\partial_tT_t=\Delta_\kappa T_t\), \(T_t\) is self-adjoint and positive as an operator, and

\[
 \int_Gp_s(xy^{-1})p_t(y)d\mu(y)=p_{s+t}(x),\quad
 \int_Gp_t(g)d\mu(g)=1.                                    \tag{H9}
\]

Indeed orthogonal projection composition proves the convolution first as an equality of operators, and uniform kernel expansions prove it pointwise. The constant space has eigenvalue zero; all other harmonic spaces are perpendicular to it, proving the integral. No pointwise positivity has been assumed in this step.

## HK.7. Pointwise and strict positivity

For polynomial initial data \(f\), \(u(t,q)=T_tf(q)\) is a finite harmonic sum, continuous through \(t=0\), with \(u(0,q)=f(q)\) and \(\partial_tu=\Delta_\kappa u\). If \(f\geq0\), apply the following elementary maximum argument to \(v=u+\epsilon(t+1)\). A negative minimum on \([0,T]\times S^3\) would occur at a time \(t_*>0\). At that point the one-sided time derivative is at most zero and the spatial Laplacian is nonnegative, contradicting \((\partial_t-\Delta_\kappa)v=\epsilon>0\). Let \(\epsilon\downarrow0\). Apply the same argument to \(\max f-u\) and \(u-\min f\) to get the maximum and minimum bounds.

For continuous nonnegative \(f\), HK.3 supplies real polynomial approximations \(f_j\); adding their uniform errors makes them nonnegative. For fixed \(t>0\), the bounded kernel permits passage to the limit, so \(T_tf\geq0\). Were \(p_t(qq'^{-1})\) negative at any \(q'\), a nonzero continuous nonnegative function supported in a small negative neighbourhood would make the integral negative; HK.2 gives that neighbourhood positive mass. Thus \(p_t\geq0\) everywhere. The same approximation proves \(\|T_tf\|_\infty\leq\|f\|_\infty\) and \(T_tf\to f\) uniformly as \(t\downarrow0\): the statement is immediate for a finite harmonic sum and its error is bounded by twice the approximation error.

There is also strict positivity. For fixed \(t>0\), the expansion in (H8) is real analytic in \(\theta\in(0,\pi)\), since \(\chi_n(\theta)=\sum_{j=0}^n e^{i(n-2j)\theta}\) converges uniformly after Gaussian weighting on each complex strip. A nonzero real analytic function has isolated zeros: its power series at an accumulation point would have every coefficient zero, and successive overlapping analytic neighbourhoods would make it identically zero. The integral of \(p_t\) is one, so it is not identically zero. Its zeros therefore have Haar measure zero by (H3). For any \(x\), both factors \(p_{t/2}(xy^{-1})\) and \(p_{t/2}(y)\) are positive outside Haar-null sets, by Haar invariance. Their integral is strictly positive, proving \(p_t(x)>0\) by (H9). Compactness now gives \(0<\min_Gp_t\leq\max_Gp_t\leq\sum(n+1)^2e^{-t\lambda_n}\).

## HK.8. An image formula with every factor

For \(t>0\), direct Gaussian Fourier integration gives

\[
 Q_t(\theta)=\sum_{k\in\mathbb Z}e^{-tk^2/2}e^{ik\theta}
 =\sqrt{\frac{2\pi}{t}}\sum_{m\in\mathbb Z}
       e^{-(\theta-2\pi m)^2/(2t)}.                          \tag{H10}
\]

Here is a proof sufficient for the formula. The Gaussian integral is \(\int e^{-x^2/(2t)}dx=\sqrt{2\pi t}\), obtained by squaring it and integrating in polar coordinates. For its Fourier integral \(J(k)\), differentiation in real \(k\), followed by integration by parts, gives \(J'(k)=-tkJ(k)\); the boundary term vanishes exponentially. Therefore \(J(k)=\sqrt{2\pi t}e^{-tk^2/2}\). The periodized Gaussian on the right of (H10) has precisely the left side's Fourier coefficients, by translating each integral to the real line. Both series and their derivatives converge uniformly on compact \(t>0\) ranges. Equality follows because a continuous periodic function with all zero Fourier coefficients is zero: trigonometric polynomials are dense by the same Bernstein argument as HK.3 on the embedded circle, so the function is orthogonal to approximations of its own conjugate.

Substitute \(k=n+1\) in (H8) and differentiate (H10). Since \(-Q_t'/2=\sum_{k\geq1}ke^{-tk^2/2}\sin(k\theta)\),

\[
 p_t(\theta)=\frac{\sqrt{2\pi}}{2t^{3/2}}\frac{e^{t/2}}{\sin\theta}
   \sum_{m\in\mathbb Z}(\theta-2\pi m)
                     e^{-(\theta-2\pi m)^2/(2t)}.             \tag{H11}
\]

At \(0,\pi\) use the continuous limit, equivalently the character series. For \(X=i\boldsymbol x\cdot\boldsymbol\sigma\), \(|\boldsymbol x|=\theta<\pi\), the identity exponential has \(\kappa(X,X)=2\theta^2\). The leading term in (H11) is consequently

\[
 \frac{4\sqrt2\pi^2}{(4\pi t)^{3/2}}e^{t/2}
       \frac{\theta}{\sin\theta}
       \exp\!\left[-\frac{\kappa(X,X)}{4t}\right].             \tag{H12}
\]

The prefactor uses the actual metric volume and Haar probability, so it cannot be replaced by a unit-volume Gaussian prefactor without changing the object.

## HK.9. A uniform small-time remainder including the identity

For \(|\theta|\leq\pi/2\), factor the \(m=0\) term in (H11) and define its relative image remainder \(r_t(\theta)\), with its derivative limit at zero. Pair indices \(m,-m\), put \(a=2\pi m\), and \(f_t(z)=ze^{-z^2/(2t)}\). Their numerator is \(f_t(\theta-a)+f_t(\theta+a)\), zero at \(\theta=0\). The mean value theorem bounds its quotient by \(|\theta|\) by

\[
 2\left(1+\frac{(a+\pi/2)^2}{t}\right)
                       e^{-(a-\pi/2)^2/(2t)}.
\]

After division by \(e^{-\theta^2/(2t)}\), for \(0<t\leq1\) it follows that

\[
 |r_t(\theta)|\leq \delta(t):=C_*t^{-1}e^{-\pi^2/t},\quad
 C_*=2\sum_{m=1}^\infty[1+(2\pi m+\pi/2)^2]
                  e^{-\pi^2(2m^2-m-1)}<\infty.              \tag{H13}
\]

This is an explicit numerical constant, not an unspecified regularity assumption. The inequality uses \(2m^2-m\geq1\) and \(t\leq1\) to bound the remaining Gaussian. The same calculation covers zero by continuity. Choose the unique small-time range by the explicit conditions \(t\leq1\), \(\delta(t)\leq1/2\); such a range exists because \(t^{-1}e^{-\pi^2/t}\to0\). Since \(|\log(1+r)|\leq2|r|\) for \(|r|\leq1/2\),

\[
 \left|-\log\frac{p_t(e^X)}{p_t(I)}
       -\frac{\kappa(X,X)}{4t}+\log\frac{\theta}{\sin\theta}\right|
       \leq4\delta(t),\qquad 0\leq\theta\leq\pi/2.           \tag{H14}
\]

Both the volume prefactor and \(e^{t/2}\) cancel only in this displayed ratio. They remain in the full density. The identity convention \(\theta/\sin\theta=1\) is used at zero.

## HK.10. Exact spectral expectations

Sine orthogonality, uniform convergence and (H8) give

\[
 \int_G\chi_n(g)p_t(g)d\mu(g)=d_n e^{-\lambda_n t},
 \qquad \int_G\frac{\chi_n(g)}{d_n}p_t(g)d\mu(g)=e^{-\lambda_nt}.
\]

In particular \(\chi_1=\operatorname{tr}_{\mathbb C^2}\), \(\lambda_1=3/2\), and \(\chi_1^2=\chi_2+1\), \(\lambda_2=4\). For \(W=2-\chi_1\), direct multiplication therefore gives

\[
 \mathbb E_t W=2-2e^{-3t/2},\qquad
 \mathbb E_t W^2=5-8e^{-3t/2}+3e^{-4t}.
\]

Their expansions at zero are \(3t+O(t^2)\) and \(15t^2+O(t^3)\), obtained from the convergent exponential series. The expectations concern real bounded functions and need no operator or formal measure interpretation.

## HK.11. The admitted source and its exact convention map

Thierry Lévy, *Yang-Mills measure on compact surfaces*, original author source [math/0101239v1](https://arxiv.org/abs/math/0101239v1), chap1.tex lines 300–352, uses Haar probability and the equation \((\partial_s-\tfrac12\Delta_{\mathrm L})p_s^{\mathrm L}=0\). Lines 324–325 specify a bi-invariant metric with total Riemannian volume one. Retain \(V_\kappa=4\sqrt2\pi^2\) from HK.1. The literal source comparison is


\[
 \kappa_{\mathrm L}=V_\kappa^{-2/3}\kappa,\qquad
 \Delta_{\mathrm L}=V_\kappa^{2/3}\Delta_\kappa,\qquad
 p_s^{\mathrm L}=p_{V_\kappa^{2/3}s/2},\qquad
 s_{\mathrm L}=\frac{2t}{V_\kappa^{2/3}}.
\]


Here is the complete metric argument. Conjugation by \(e^{i\theta\sigma_a}\) rotates the other two Pauli coordinates by angle \(2\theta\). Invariance under these three rotations forces a Lie-algebra quadratic form to be a scalar multiple of \(\kappa\). Multiplying a three-dimensional metric by \(b>0\) multiplies its volume by \(b^{3/2}\), by the determinant formula, and its Laplacian by \(b^{-1}\), by the coordinate expression \(|g|^{-1/2}\partial_i(|g|^{1/2}g^{ij}\partial_j)\). Volume one therefore fixes \(b=V_\kappa^{-2/3}\). Its Riemannian measure is \(V_\kappa^{-1}d\mathrm{vol}_\kappa=d\mu\), so both kernels are densities against the same probability. Substitution into every harmonic coefficient of (H8) proves the kernel identity.

For the separately specified half-Laplacian using the same metric \(\kappa\), write \(p_s^{(\kappa,1/2)}=p_{s/2}\); its parameter is \(s=2t\). This retains the valid same-metric comparison without assigning it to the author's literal volume-one metric.

The same source, chap1.tex lines 583–587, prints a convolution with factors \(p_s\), \(p_t\) and result \(p_t\). With those factors the result must instead be \(p_{s+t}\); to retain the printed result one must replace the second factor by \(p_{t-s}\). This is an actual discrepancy: the nonconstant \(\chi_1\) coefficient on the left is multiplied by two distinct positive-time exponentials. The source's later subdivision proof, lines 713–722, correctly adds the two face areas. Our calculations use (H9), proved independently, and the exact metric-and-time translation just proved.

## HK.12. Exactly what has been constructed

For the trace metric on SU(2), (H8) is a smooth strictly positive probability density, a convolution semigroup, the solution operator for \(\partial_tu=\Delta_\kappa u\), and a strongly continuous positivity-preserving contraction on continuous functions. HK.3–HK.7 supply all those claims. This construction is used below as an ingredient for graph probability measures; it is not a four-dimensional field measure.

## HK.13. Operator domain, if the heat generator is used

The preceding construction also gives its exact self-adjoint generator without an additional spectral theorem. For the orthogonal decomposition \(f=\sum f_n\), define \(L f=\sum\lambda_n f_n\) on \(D(L)=\{f:\sum\lambda_n^2\|f_n\|_2^2<\infty\}\). This is densely defined since finite sums are dense. If \(g\) belongs to the adjoint domain, testing against every finite harmonic vector forces the adjoint components to be \(\lambda_n g_n\), and their squared norms must be summable; this proves \(D(L^*)=D(L)\) and \(L^*=L\). It is nonnegative. On polynomial restrictions it equals \(-\Delta_\kappa\); \(T_t\) is its directly defined diagonal exponential. No assertion about an unconstructed field Hamiltonian follows.

## HK.14. Boundary and exceptional points

All formulas using \(\theta\) are conjugacy-class coordinates, with \(\theta=\arccos(\tfrac12\operatorname{tr}g)\in[0,\pi]\). The sphere parametrization loses the direction \(\boldsymbol n\) at its two poles, which have Haar mass zero; the matrix and polynomial formulas remain defined there. The principal logarithm \(X=i\theta\boldsymbol n\cdot\boldsymbol\sigma\) is used only for \(\theta<\pi\), with \(X=0\) at the identity. The heat series and every graph density below are defined also at \(-I\), without choosing a logarithm. The small-time action comparison explicitly keeps \(\theta\leq\pi/2\); it does not extend an identity-chart calculation through a cut locus.


## AC.1. The two-dimensional classical action with ordered indices

For a \(C^3\) SU(2) connection \(A=A_1dx^1+A_2dx^2\) on a neighbourhood of the closed rectangle \(D\), define

\[
 F_{12}=\partial_1A_2-\partial_2A_1+[A_1,A_2],\quad F_{21}=-F_{12},
 \quad F_{11}=F_{22}=0,\quad
 F=\tfrac12\sum_{\mu,\nu=1}^2F_{\mu\nu}dx^\mu\wedge dx^\nu.
\]

With Euclidean metric \(\delta_{\mu\nu}\), \(\kappa=-\operatorname{tr}_{\mathbb C^2}\), and \(g_2>0\) of units length\(^{-1}\), the actual two-dimensional action is

\[
 S_2[A]=\frac{\hbar}{2g_2^2}\int_D\sum_{\mu,\nu=1}^2
       \kappa(F_{\mu\nu},F_{\mu\nu})\,d^2x
       =\frac{\hbar}{g_2^2}\int_D\kappa(F_{12},F_{12})\,d^2x.  \tag{A1}
\]

The second equality uses both nonzero ordered pairs. The components \(A_\mu\) have units length\(^{-1}\), and \(F_{12}\) has units length\(^{-2}\), so the displayed expression has units of action. It is a two-dimensional object explicitly defined here, with the same trace convention as the course, not a replacement of its four-dimensional integration domain.

## AC.2. Holonomy sign and a quantified small-rectangle estimate

Define forward parallel transport along a coordinate segment by \(U'=-A_\mu U\), \(U(0)=I\). Iteration of the integral equation gives the convergent ordered-integral series, whose degree \(r\) term has norm at most \((\ell M_0)^r/r!\). It proves existence; iteration of the difference equation proves uniqueness. Differentiation gives \(U^*U=I\). Since \(\operatorname{tr}A_\mu=0\), differentiating the determinant gives \(\det U=1\). Thus this is an actual SU(2) transport. The same product derivative proves the endpoint gauge transformation in GP.2.

Let the side lengths of a small cell be \(b_1,b_2>0\), its area \(a=b_1b_2\), and \(h=\max(b_1,b_2)\leq h_0\), where \(h_0>0\) is a fixed physical length. On the closed rectangle take operator-norm bounds

\[
 M_0=\max_\mu\sup\|A_\mu\|,\quad
 M_{A,1}=\max_{\mu,\nu}\sup\|\partial_\nu A_\mu\|,\quad
 M_F=\sup\|F_{12}\|,\quad M_1=\max_\nu\sup\|\partial_\nu F_{12}\|.
\]

They are finite for the stated field. Put

\[
 U_1=M_0+h_0M_{A,1},\quad C=M_1+2U_1M_F,\quad
 B=C+\tfrac12h_0M_F^2,\quad C_W=2M_FB+h_0B^2,
 \quad L_q=4M_FM_1.                                      \tag{A2}
\]

No unit has been suppressed in these constants.

Here is the local proof, applicable at every cell. With local coordinates \((s,r)\in[0,b_1]\times[0,b_2]\), choose \(u(0,0)=I\), solve \(u_r(0,r)=u(0,r)A_2(0,r)\), and then \(u_s(s,r)=u(s,r)A_1(s,r)\). For \(\widetilde A_\mu=uA_\mu u^{-1}-(\partial_\mu u)u^{-1}\), direct differentiation gives \(\widetilde A_1=0\), \(\widetilde A_2(0,r)=0\), and
\(\widetilde A_2(b_1,r)=\int_0^{b_1}u(s,r)F_{12}(s,r)u(s,r)^{-1}ds\).

Differentiating the ODE with respect to \(r\), and integrating its inhomogeneous equation with a unitary propagator, gives \(\|u_s\|\leq M_0\), \(\|u_r\|\leq M_0+b_1M_{A,1}\leq U_1\). Thus each first derivative of \(uFu^{-1}\) has norm at most \(C\), and


\[
\|u(s,r)F(s,r)u(s,r)^{-1}-F(0,0)\|\leq C(s+r)
\]

.
Three sides of the cell have identity transport in this gauge; its positive boundary is transport up the right side, based where \(u=I\). The integral equation and unitarity give both \(\|P-I\|\leq aM_F\) and a remainder at most \((aM_F)^2/2\) after its linear integral term. Integrating the previous derivative bound yields

\[
 P=I-aF(0,0)+R,\quad
 \|R\|\leq ahC+\tfrac12a^2M_F^2\leq ahB.                 \tag{A3}
\]

In particular the sign is minus for the course's forward transport. This proof is local, so it needs no periodic boundary extension.

Set \(W(P)=2-\operatorname{Re}\operatorname{tr}P\). Unitarity gives \(W(P)=\tfrac12\|I-P\|_{\rm HS}^2\). For a two-by-two matrix \(\|X\|_{\rm HS}\leq\sqrt2\|X\|\). Comparing the square norm in (A3) therefore proves

\[
 0\leq W(P)\leq a^2M_F^2,\qquad
 \left|W(P)-\frac{a^2}2q(0,0)\right|\leq a^2hC_W,
 \quad q=\kappa(F_{12},F_{12}).                            \tag{A4}
\]

Indeed the cross term is at most \(2a^2M_FhB\) and the remaining squared term at most \(a^2h^2B^2\). Differentiating \(q=-\operatorname{tr}F^2\) gives \(|\partial_\nu q|\leq4M_FM_1=L_q\). Left-corner quadrature on one cell consequently differs from its integral by at most \(ahL_q\); summing gives at most \(|D|hL_q\). This proves every estimate used next.

## AC.3. Deriving the heat-time/coupling dictionary

Let \(P=e^X\) be in the identity logarithm chart. HK.8 gives the leading heat exponent \(\kappa(X,X)/(4t)\). Equation (A3) gives \(X=-aF+\) higher powers as \(a,h\to0\); the exact squared comparison is supplied below. To match the single-cell contribution \(a\kappa(F,F)/g_2^2\) in \(S_2/\hbar\), the coefficient must satisfy \(a^2/(4t)=a/g_2^2\). Hence

\[
 t(a)=\frac{g_2^2a}{4},\qquad s_{(\kappa,1/2)}(a)=2t(a)=\frac{g_2^2a}{2},\qquad s_{\mathrm L}(a)=\frac{g_2^2a}{2V_\kappa^{2/3}}.       \tag{A5}
\]

Here \(s_{\mathrm L}\) is the half-Laplacian parameter for Lévy's literal volume-one metric, while \(s_{(\kappa,1/2)}\) uses the course metric. HK.11 proves the full metric conversion, with \(V_\kappa=4\sqrt2\pi^2\). With spin label \(j=n/2\), \(n(n+2)=4j(j+1)\), so the same heat coefficient is \(e^{-g_2^2a j(j+1)/2}\). This last expression is a comparison of labels, not a change of the original matrix trace or metric.

## AC.4. A proved classical limit with the full density multiplier retained

For each dyadic grid define

\[
 S_{{\rm H},m}^{\rm rel}(U)=-\hbar\sum_f
             \log\frac{p_{t_m}(P_f(U))}{p_{t_m}(I)},\quad
 \prod_fp_{t_m}(P_f)=p_{t_m}(I)^{4^m}
                      e^{-S_{{\rm H},m}^{\rm rel}/\hbar}.     \tag{A6}
\]

The right multiplier is retained; the finite probability has partition one only for the entire left side. Since \(\chi_n(g)\leq n+1\) and all heat coefficients are positive, (H8) gives \(p_t(g)\leq p_t(I)\). Thus the relative action is nonnegative. The relative action is used only for comparing field-dependent classical terms.

We prove convergence to (A1), rather than relying on a leading formal term. Let \(a=a_m\), \(h=\max(L_1,L_2)/2^m\), and put \(K=\pi M_F/2\). Choose all sufficiently large \(m\) for which \(aM_F\leq1\), \(t=g_2^2a/4\leq1\), and the explicit \(\delta(t)\) of (H13) is at most \(1/2\). If \(M_F=0\), (A3)'s direct integral proof gives every face \(P=I\), and both actions vanish. Otherwise write each plaquette's conjugacy angle as \(\theta\in[0,\pi]\). Since \(\|P-I\|=2\sin(\theta/2)\leq aM_F\), we have \(\theta\leq\pi/3<\pi/2\) and also \(\theta\leq Ka\), using \(\sin(\theta/2)\geq\theta/\pi\). Thus (H14) applies. For its principal logarithm, \(\kappa(X,X)=2\theta^2\). Taylor's formula with bounded fourth derivative yields

\[
 |\kappa(X,X)-2W(P)|\leq\theta^4/6.
\]

Also \(0\leq\log(\theta/\sin\theta)\leq C_g\theta^2\) on \([0,\pi/2]\), where \(C_g=[6(1-\pi^2/24)]^{-1}\): use \(\sin\theta/\theta\geq1-\theta^2/6\), and \(-\log(1-u)\leq u/(1-u)\). Combining (A4), (H14), \(4t=g_2^2a\), and the quadrature bound proves

\[
 \left|S_{{\rm H},m}^{\rm rel}(U[A])-S_2[A]\right|
 \leq\hbar|D|\left[
 \frac{h(2C_W+L_q)}{g_2^2}
 +\frac{K^4a^2}{6g_2^2}+C_gK^2a+\frac{4\delta(g_2^2a/4)}a\right].        \tag{A7}
\]

To check the summation, the per-face exponent error is at most
\(2ahC_W/g_2^2+K^4a^3/(6g_2^2)+C_gK^2a^2+4\delta(t)\), and the face count is \(|D|/a=4^m\). The remaining quadrature term is \(|D|hL_q/g_2^2\). Every term on the right of (A7) tends to zero; the last does so because its exponential is \(e^{-4\pi^2/(g_2^2a)}\) times an explicit power of \(a^{-1}\). This is a proved field-by-field classical action comparison, with fixed physical rectangle, fixed coupling and fixed smooth connection. It is not convergence of a measure on smooth fields.

## AC.5. Wilson's finite density is a different object

For the same two-dimensional grid the Wilson discretization matching (A1) is

\[
 S_{{\rm W},m}(U)=\frac{2\hbar}{g_2^2}\sum_f\frac{W(P_f)}{a_m},
 \quad \beta=\frac{2}{g_2^2a_m},\quad
 w_a(g)=\frac{e^{-\beta W(g)}}{Z_{\rm W}(\beta)},\quad
 Z_{\rm W}(\beta)=\int_Ge^{-\beta W(g)}d\mu(g).               \tag{A8}
\]

The original \(2\), trace, area denominator and \(\hbar\) remain visible. The same proof as (A4) gives


\[
|S_{{\rm W},m}(U[A])-S_2[A]|\leq(\hbar|D|/g_2^2)h(2C_W+L_q)
\]

.
The tree calculation GP.4 shows the full finite Wilson partition is \(Z_{\rm W}(\beta)^{4^m}\), since its face factors are independent after that exact change of variables.

To prove that this finite density is not the heat density, define
\(I_k(z)=\pi^{-1}\int_0^\pi e^{z\cos\theta}\cos(k\theta)d\theta\), for integer \(k\geq0\). Using \(\sin^2\theta=(1-\cos2\theta)/2\) in (H3),

\[
 Z_{\rm W}(\beta)=e^{-2\beta}[I_0(2\beta)-I_2(2\beta)],\quad
 m_{\rm W}(\beta):=\mathbb E_{w_a}\frac{\operatorname{tr}g}{2}
 =\frac{I_1(2\beta)-I_3(2\beta)}{2[I_0(2\beta)-I_2(2\beta)]}.
\]

The numerator follows by multiplying \(\sin^2\theta\cos\theta\) or differentiating its denominator integral. All integrands are bounded on the finite interval, so derivatives and convergent exponential series can be integrated termwise. Haar symmetry makes odd moments of \(\cos\theta\) zero, while (H3) gives \(\mathbb E\cos^2\theta=1/4\). Therefore \(m_{\rm W}(\beta)=\beta/2+O(\beta^3)\) as \(\beta\downarrow0\), with the remainder controlled by the uniformly convergent exponential series. The heat expectation at the matched area is instead \(e^{-3/(4\beta)}\), from (A5) and HK.10. Their ratio does not tend to one; these density families are not identical.

There is also no exact area-additive convolution for the Wilson family. Conjugation symmetry forces \(\mathbb E_{w_a}g=m_{\rm W}(\beta)I\): in (H1) the vector part averages to zero under rotations of \(\boldsymbol n\). For independent variables with that density, the dimension-divided trace of their product has expectation \(m_{\rm W}(\beta)^2=\beta^2/4+O(\beta^4)\). The area-doubled Wilson face has parameter \(\beta/2\) and expectation \(\beta/4+O(\beta^3)\). They disagree for all sufficiently small positive \(\beta\). Thus the exact continuum construction GP.8–GP.12 relies on the heat semigroup and cannot be transferred to the Wilson family by renaming its parameters.

## AC.6. The exact relation to the course's four-dimensional action

Use a new explicitly specified product geometry \(D\times\mathbb T^2\), with Euclidean product metric and transverse periods \(L_3,L_4>0\). Their physical area is \(B_\perp=L_3L_4\). Extend the connection from AC.1 independently of \(x^3,x^4\), setting \(A_3=A_4=0\). Then every curvature component with a transverse index is zero: derivatives in those directions vanish and the relevant commutators contain a zero component. The two remaining ordered terms are exactly \(F_{12},F_{21}\). The course action F7.5 consequently becomes

\[
 S_4[A]=\frac{\hbar B_\perp}{g_{\rm YM}^2}
       \int_D\kappa(F_{12},F_{12})d^2x
       =S_2[A]\quad\text{when}\quad g_2^2=\frac{g_{\rm YM}^2}{B_\perp}.       \tag{A9}
\]

The map of fields is the displayed pullback with two zero components; this equality proves its action comparison including every ordered contribution. It does not identify the two quantum measures. In particular it does not say that restricting or integrating a four-dimensional Wilson measure produces the heat law in (G5). The earlier F14 Wilson action is
\(2\hbar/g_{\rm YM}^2\sum_{j,\mu<\nu}v\,W(P_{\mu\nu})/(a_\mu^2a_\nu^2)\), with six indexed plaquette orientations and four-volume \(v\). AC.5 and (A9) preserve, rather than discard, the distinction between its four-volume weights and the two-dimensional face-area weights.

## AC.7. Physical time, \(c\), and an actual heat transfer operator

If the second Euclidean length coordinate is written \(x^2=c\tau\), with \(c>0\) a fixed speed and \(\tau\) physical time, the metric is \(dx_1^2+c^2d\tau^2\), the area element is \(c\,dx^1d\tau\), and \(F_{1\tau}=cF_{12}\). Therefore (A1) becomes \(S_2=\hbar/(g_2^2c)\int\kappa(F_{1\tau},F_{1\tau})dx^1d\tau\). No \(c\) is absorbed into \(g_2\).

For a rectangle of width \(R>0\) and duration \(T>0\), its physical area is \(RcT\). Define on the already constructed \(L^2(G,d\mu)\) the operator \(\mathcal T_R(T)=T_{g_2^2RcT/4}\). HK.6 and HK.13 prove a strongly continuous self-adjoint positive semigroup with Hamiltonian
\(\mathcal H_R=(\hbar c g_2^2R/4)L\), on \(D(L)\). Hence

\[
 \mathcal H_R\chi_n=\frac{\hbar c g_2^2R\,n(n+2)}8\chi_n,
 \qquad
 \langle\chi_n,\mathcal T_R(T)\chi_n\rangle
 =e^{-T\hbar^{-1}(\hbar c g_2^2R\,n(n+2)/8)}.
\]

Characters have \(L^2\) norm one by HK.5. The last expression equals the actual dimension-divided Wilson expectation (G12). This explicitly constructed transfer matrix element gives the energy factor associated with this area law; in the fundamental representation it is \(3\hbar c g_2^2R/8\). It is a precise correspondence in this two-dimensional heat model, not an assertion about a four-dimensional static-source Hamiltonian or an analytic continuation of quantum theories.

## AC.8. Which comparisons are mathematical identities

The gauge rule matches by GP.2; Lévy's gauge variable matches by \(j=h^{-1}\); his literal metric and heat time match by \(s_{\mathrm L}=2t/V_\kappa^{2/3}\), with the separate same-metric parameter \(s_{(\kappa,1/2)}=2t\); the classical action matches by (A7), with all remainders and density constants retained; the restricted four-dimensional classical field matches by (A9). Each receiving map has been constructed. The failure of an exact Wilson-area convolution is proved by an observable discrepancy in AC.5. None of these comparisons assumes an interacting four-dimensional continuum measure.

## AC.9. Source provenance for the original conventions

The original course F07, equations F7.1–F7.5, specifies the signature sign, full ordered contraction, skew-Hermitian matrices and \(-\operatorname{tr}\) pairing. The source comparison is recorded in the lesson provenance. The prior independent F14 calculation L.10–L.18 supplies a more detailed second-order holonomy estimate; AC.2 instead includes a complete local first-order bound sufficient for (A7), with no periodicity assumption. The two derivations have the same minus transport sign and the same leading \(W(P)=a^2\kappa(F,F)/2\). No source convention is silently imported from a scalar-field action.
