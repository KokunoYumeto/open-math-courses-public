# Weak solutions in three-dimensional space

On a periodic box, the energy in high Fourier modes becomes small after integration in time. The finitely many remaining modes can then be followed individually. On \(\mathbb R^3\), a second issue appears: a bounded sequence can move farther and farther from the origin while keeping all its energy. Convergence on each bounded region would then miss that energy.

We will construct approximations to the forced Navier–Stokes equation and prove a uniform bound on their energy outside large balls. This bound, together with control of spatial derivatives and time changes, gives strong convergence on the entire space. We will then prove the energy inequality, recover the pressure of the original force, and establish agreement with a regular solution.

This chapter uses [the Fourier transform, pressure projection and heat operator](pressure-and-the-divergence-free-projection.md) and [the periodic weak-solution construction](weak-solutions-on-a-periodic-box.md). The Hilbert-space subsequence and time-continuity arguments proved there will be applied with their hypotheses checked here. All spatial integrals in this chapter are over \(\mathbb R^3\) unless another domain is displayed.

## 1. The theorem and its exact data

Fix \(\nu>0\). The initial velocity and force are

\[
 u_0\in L^2_\sigma(\mathbb R^3),\qquad
 f\in L^2(0,T;H^{-1}(\mathbb R^3))
 \quad\text{for every }T<\infty.
 \tag{1.1}
\]

The subscript \(\sigma\) means divergence free in distributions. The force is a real vector distribution in space and need not be divergence free. All time-dependent functions are strongly measurable. Our Fourier and Sobolev conventions remain

\[
 \widehat h(\xi)=\int h(x)e^{-2\pi i x\cdot\xi}\,dx,\qquad
 \|h\|_{H^s}^2=\int(1+4\pi^2|\xi|^2)^s|\widehat h(\xi)|^2\,d\xi.
 \tag{1.2}
\]

In particular \(\|h\|_{H^1}^2=\|h\|_2^2+\|\nabla h\|_2^2\). The pairing of \(H^{-1}\) and \(H^1\) is the extension of the real \(L^2\) scalar product, and

\[
 |\langle f,h\rangle|\leq\|f\|_{H^{-1}}\|h\|_{H^1}.
 \tag{1.3}
\]

**Theorem.** There exist a real velocity \(u\) and a real, locally integrable pressure \(p\) such that

\[
 \begin{gathered}
 u\in L^\infty(0,T;L^2_\sigma)\cap L^2(0,T;H^1_\sigma)
 \quad(T<\infty),\\
 u\in C_{\rm w}([0,\infty);L^2_\sigma),\qquad u(0)=u_0,\\
 \partial_tu+\operatorname{div}(u\otimes u)+\nabla p
 =\nu\Delta u+f,\qquad \operatorname{div}u=0.
 \end{gathered}
 \tag{1.4}
\]

The equation holds in distributions. The convention is \((u\otimes u)_{ij}=u_i u_j\), with divergence \(\sum_j\partial_j(u_i u_j)\). There is a set \(G\subset(0,\infty)\) of full measure such that, for \(s=0\) and for every \(s\in G\),

\[
 \frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(r)\|_2^2\,dr
 \leq\frac12\|u(s)\|_2^2+\int_s^t\langle f(r),u(r)\rangle\,dr
 \quad\text{for every }t\geq s.
 \tag{1.5}
\]

The velocity is strongly continuous from the right in \(L^2\) at each of these starting times. These properties are our definition of a Leray–Hopf solution in this chapter. We will construct an actual pressure with explicit bounds in Section 7. Section 8 proves weak–strong uniqueness in a stated regular comparison class, for every solution with properties (1.4)–(1.5).

The viscosity and force in the conclusion are exactly those in (1.1). No change of spatial coordinates or physical time will be made. Section 9 proves the extension to the sum of time-integrable square-integrable forces and the class (1.1), with its full modified energy and tail estimates.

## 2. Smoothing, energy and a global approximate solution

Choose an even, nonnegative function \(\rho\in C_c^\infty(B_1)\) with integral one. For example, use a positive constant times \(\exp[-1/(1-|x|^2)]\) on \(|x|<1\), zero outside, with the constant equal to the reciprocal of its displayed integral. At the boundary every derivative vanishes because any fixed power of \((1-|x|^2)^{-1}\) times that exponential tends to zero. For \(0<\varepsilon\leq1\), put

\[
 \rho_\varepsilon(x)=\varepsilon^{-3}\rho(x/\varepsilon),
 \qquad J_\varepsilon h=\rho_\varepsilon*h.
 \tag{2.1}
\]

Evenness makes \(J_\varepsilon\) self-adjoint in the \(L^2\) pairing. Jensen's inequality and Fubini show that it is a contraction on every \(L^q\), \(1\leq q\leq\infty\). For \(1\leq q<\infty\), the calculation is

\[
 |J_\varepsilon h(x)|^q
 \leq\int\rho_\varepsilon(y)|h(x-y)|^q\,dy,
 \qquad \|J_\varepsilon h\|_q\leq\|h\|_q.
 \tag{2.2}
\]

The case \(q=\infty\) follows from the same integral without raising to a power. Since \(|\widehat\rho(\varepsilon\xi)|\leq1\), (1.2) also makes it a contraction on every \(H^s\). Dominated convergence and \(\widehat\rho(\varepsilon\xi)\to1\) give \(J_\varepsilon h\to h\) strongly in \(H^s\) for each \(h\in H^s\).

Let \(P\) be the whole-space projection with matrix

\[
 P(\xi)=I-\frac{\xi\otimes\xi}{|\xi|^2}\quad(\xi\ne0).
 \tag{2.3}
\]

Its value at \(\xi=0\) does not affect an \(H^s\) element. The preceding projection lesson proves its norm bound, self-adjointness and divergence-free range. It commutes with \(J_\varepsilon\), spatial derivatives and the heat operator \(S_\nu(t)\), whose Fourier multiplier is \(e^{-4\pi^2\nu t|\xi|^2}\).

We solve the following specific approximate equation:

\[
 \begin{gathered}
 \partial_tu_\varepsilon+
 J_\varepsilon P\operatorname{div}
     (v_\varepsilon\otimes v_\varepsilon)
 =\nu\Delta u_\varepsilon+J_\varepsilon Pf,\\
 v_\varepsilon=J_\varepsilon u_\varepsilon,\qquad
 u_\varepsilon(0)=J_\varepsilon u_0.
 \end{gathered}
 \tag{2.4}
\]

The outer and inner smoothing operators both matter. Their positions will make the energy cancellation exact.

### Existence on a short interval

Write \(N_\varepsilon(a)=J_\varepsilon P\operatorname{div}
(J_\varepsilon a\otimes J_\varepsilon a)\) and define the finite constant

\[
 C_\varepsilon=\|\rho_\varepsilon\|_2
                   \sum_{j=1}^3\|\partial_j\rho_\varepsilon\|_1.
 \tag{2.5}
\]

Then

\[
 \begin{aligned}
 \|N_\varepsilon(a)\|_2&\leq C_\varepsilon\|a\|_2^2,\\
 \|N_\varepsilon(a)-N_\varepsilon(b)\|_2
 &\leq C_\varepsilon(\|a\|_2+\|b\|_2)\|a-b\|_2.
 \end{aligned}
 \tag{2.6}
\]

To prove this, move the divergence derivative onto the outer convolution kernel, use the \(L^2\) contraction of \(P\), and estimate each tensor column in \(L^2\). Cauchy–Schwarz gives \(\|J_\varepsilon a\|_\infty\leq\|\rho_\varepsilon\|_2\|a\|_2\), while (2.2) gives its \(L^2\) bound. For a scalar integrable kernel \(k\), the convolution bound used here follows directly from

\[
 \left|\int k(y)h(x-y)\,dy\right|^2
 \leq\|k\|_1\int|k(y)|\,|h(x-y)|^2\,dy;
 \tag{2.7}
\]

integrating in \(x\) gives \(\|k*h\|_2\leq\|k\|_1\|h\|_2\). For the second line of (2.6), use the exact tensor difference
\((a-b)\otimes a+b\otimes(a-b)\), with \(J_\varepsilon\) applied to every vector, and sum over the three divergence columns.

The smoothed force belongs to \(L^2_tH^q_x\) for every nonnegative integer \(q\). Indeed,

\[
 \|J_\varepsilon Pf\|_{H^q}
 \leq B_{\varepsilon,q}\|f\|_{H^{-1}},\qquad
 B_{\varepsilon,q}=
 \sup_\xi(1+4\pi^2|\xi|^2)^{(q+1)/2}
                      |\widehat\rho(\varepsilon\xi)|<\infty.
 \tag{2.8}
\]

Finiteness follows by integrating by parts arbitrarily many times in the Fourier transform of the smooth compact kernel. The same argument puts \(J_\varepsilon u_0\) in every \(H^q\).

On an interval beginning at \(t_*\), with divergence-free initial value \(a_*\in L^2\), use the map

\[
 (\Phi a)(t)=S_\nu(t-t_*)a_*+
 \int_{t_*}^tS_\nu(t-r)
       [-N_\varepsilon(a(r))+J_\varepsilon Pf(r)]\,dr.
 \tag{2.9}
\]

The integrals are limits in \(L^2\) of integrals of step functions; their norms are at most the integrals of the norms. Strong continuity and contraction of the heat operator imply that (2.9) is continuous in \(L^2\). For the integral term, this follows by splitting at a fixed time, using strong heat continuity on the earlier part and absolute continuity of the norm integral on the shorter remaining part.

Set \(M=2(\|a_*\|_2+1)\). On a sufficiently short interval of length \(\delta>0\), require

\[
 \int_{t_*}^{t_*+\delta}\|J_\varepsilon Pf(r)\|_2\,dr\leq1,\qquad
 C_\varepsilon M^2\delta\leq M/2,\qquad
 2C_\varepsilon M\delta<1.
 \tag{2.10}
\]

The closed ball \(\sup_t\|a(t)\|_2\leq M\) is then mapped into itself, and (2.6) makes \(\Phi\) a contraction there. Successive iterates have differences bounded by a geometric series in the complete space \(C([t_*,t_*+\delta];L^2_\sigma)\). Their limit solves (2.9), uniquely on this ball. The same difference estimate, used on small subintervals, gives uniqueness between any two bounded local solutions. All iterates remain divergence free because the heat operator and the forcing terms in (2.9) take values in \(L^2_\sigma\).

### Spatial regularity and the energy identity

For each multi-index \(\alpha\), moving derivatives onto the outer kernel gives

\[
 \|\partial^\alpha N_\varepsilon(a)\|_2
 \leq C_{\varepsilon,\alpha}\|a\|_2^2,\qquad
 C_{\varepsilon,\alpha}=
 \|\rho_\varepsilon\|_2
 \sum_{j=1}^3\|\partial^{\alpha+e_j}\rho_\varepsilon\|_1.
 \tag{2.11}
\]

The same tensor difference proves continuity into each of these derivative spaces. For integer \(q\), the Fourier identity

\[
 (1+4\pi^2|\xi|^2)^q
 =\sum_{|\alpha|\leq q}
    \frac{q!}{(q-|\alpha|)!\,\alpha_1!\alpha_2!\alpha_3!}
    \prod_{j=1}^3(4\pi^2\xi_j^2)^{\alpha_j}
 \tag{2.12}
\]

shows that the finitely many derivative estimates give an \(H^q\) estimate, with all coefficients displayed. Applying (2.9) in \(H^q\), using (2.8), proves \(u_\varepsilon\in CH^q\) on each local interval starting at zero, for every \(q\).

The equation holds as a distributional identity in \(L^2\). One way to check time differentiation is to restrict all Fourier transforms to \(|\xi|\leq K\), where \(\Delta\) is a bounded multiplier. The integral fundamental theorem then differentiates (2.9) with the \(L^1_tL^2_x\) forcing. Letting \(K\to\infty\) uses \(u_\varepsilon\in CH^2\) and (2.8), (2.11). It follows that \(u_{\varepsilon,t}\in L^2_tL^2_x\) on finite local intervals and \(u_\varepsilon\) is absolutely continuous as an \(L^2\)-valued function. The Hilbert identity
\(\|a+h\|_2^2-\|a\|_2^2=2(a,h)+\|h\|_2^2\), or its integrated step-function approximation, gives the derivative \(2(u_\varepsilon,u_{\varepsilon,t})\) of its squared norm.

Self-adjointness and divergence freedom yield

\[
 (u_\varepsilon,N_\varepsilon(u_\varepsilon))
 =(v_\varepsilon,\operatorname{div}(v_\varepsilon\otimes v_\varepsilon))
 =0.
 \tag{2.13}
\]

For the last equality, integrate against a smooth cutoff \(\theta(x/R)\) equal to one on \(B_R\). The product rule leaves only a boundary integral bounded by a constant times
\(R^{-1}\int|v_\varepsilon|^3\). This tends to zero: the Fourier Cauchy–Schwarz bound puts \(H^q\) in \(L^\infty\) for \(q>3/2\), and hence
\(\int|v_\varepsilon|^3\leq\|v_\varepsilon\|_\infty\|v_\varepsilon\|_2^2<\infty\).
The same cutoff argument gives \((u_\varepsilon,\Delta u_\varepsilon)=-\|\nabla u_\varepsilon\|_2^2\). Thus the exact energy identity is

\[
 \frac12\frac d{dt}\|u_\varepsilon\|_2^2+
 \nu\|\nabla u_\varepsilon\|_2^2
 =\langle f,J_\varepsilon u_\varepsilon\rangle.
 \tag{2.14}
\]

The force remains the original \(f\) on the right, because \(PJ_\varepsilon u_\varepsilon=J_\varepsilon u_\varepsilon\).

Put \(F(t)=\|f(t)\|_{H^{-1}}\). Since \(J_\varepsilon\) is an \(H^1\) contraction, the same square inequality as in the periodic proof gives, with \(E_\varepsilon=\|u_\varepsilon\|_2^2\) and \(D_\varepsilon=\|\nabla u_\varepsilon\|_2^2\),

\[
 E_\varepsilon'+\nu D_\varepsilon
 \leq\nu E_\varepsilon+\nu^{-1}F^2.
 \tag{2.15}
\]

Multiplying by \(e^{-\nu t}\) and integrating proves

\[
 \begin{gathered}
 A_T=e^{\nu T}\left(\|u_0\|_2^2+
                      \nu^{-1}\int_0^T F(r)^2\,dr\right),
 \qquad M_T=(T+\nu^{-1})A_T,\\
 E_\varepsilon(t)+\nu\int_0^tD_\varepsilon(r)\,dr\leq A_T
       \quad(0\leq t\leq T),\qquad
 \int_0^T\|u_\varepsilon\|_{H^1}^2\,dr\leq M_T.
 \end{gathered}
 \tag{2.16}
\]

These estimates hold uniformly in \(\varepsilon\).

They also prove that the approximate solution is global. Suppose its interval ended at a finite \(T_*\). The \(L^2\) bound and (2.6) make the right-hand forcing in (2.9) integrable up to \(T_*\). Strong heat continuity and dominated convergence show that the formula has an \(L^2\) limit as \(t\uparrow T_*\). Start the same local contraction at that limit to extend the solution. This contradicts the maximal interval. Formula (2.9) from time zero, together with (2.8) and (2.11), then supplies \(CH^q\) regularity on every finite interval as well.

## 3. A spatial estimate with its constant

We need a bound on \(\|u_\varepsilon\|_4\) in terms of energy and dissipation. We prove the specific three-dimensional Sobolev estimate used here:

\[
 \|w\|_6\leq S\|\nabla w\|_2,\qquad S=\frac4{\sqrt3},
 \qquad w\in H^1(\mathbb R^3;\mathbb R^3).
 \tag{3.1}
\]

The constant is sufficient for this proof; no optimality is claimed.

Start with a compact smooth scalar function \(h\). Let

\[
 A_1(x_2,x_3)=\int_{\mathbb R}|\partial_1h(x_1,x_2,x_3)|\,dx_1,
 \tag{3.2}
\]

and define \(A_2(x_1,x_3)\), \(A_3(x_1,x_2)\) by integrating in the other coordinates. The fundamental theorem of calculus gives \(|h(x)|\leq A_j\) for each \(j\). Therefore
\(|h|^{3/2}\leq(A_1A_2A_3)^{1/2}\).
For fixed \(x_2,x_3\), Cauchy–Schwarz in \(x_1\) bounds the integral of \((A_2A_3)^{1/2}\) by
\((\int A_2\,dx_1)^{1/2}(\int A_3\,dx_1)^{1/2}\).
The two factors depend only on \(x_3\) and \(x_2\), respectively. Cauchy–Schwarz in the remaining two coordinates consequently gives

\[
 \int|h|^{3/2}\leq
       \prod_{j=1}^3\|\partial_jh\|_1^{1/2}.
 \tag{3.3}
\]

Taking the power \(2/3\), using the arithmetic-geometric mean inequality on the three nonnegative norms, and applying Euclidean Cauchy–Schwarz pointwise, we obtain

\[
 \|h\|_{3/2}\leq
 \prod_{j=1}^3\|\partial_jh\|_1^{1/3}
 \leq\frac13\sum_{j=1}^3\|\partial_jh\|_1
 \leq\frac1{\sqrt3}\|\nabla h\|_1.
 \tag{3.4}
\]

For a compact smooth vector field \(w\), use \(h=|w|^4\). It is smooth, including at zeros of \(w\), since it is the square of \(\sum_iw_i^2\). The derivative bound
\(|\nabla|w|^4|\leq4|w|^3|\nabla w|\) and Cauchy–Schwarz give

\[
 \|w\|_6^4\leq\frac4{\sqrt3}\|w\|_6^3\|\nabla w\|_2.
 \tag{3.5}
\]

If the \(L^6\) norm is zero, (3.1) is immediate; otherwise division by its cube proves (3.1) for these fields.

Here is the required density step. Let \(w\in H^1\), and let \(\theta\) be smooth, compactly supported and equal to one near the origin. The fields \(\theta(x/R)w\) tend to \(w\) in \(L^2\). Their gradients are

\[
 \theta(x/R)\nabla w+R^{-1}w\otimes\nabla\theta(x/R).
 \tag{3.6}
\]

The first term tends to \(\nabla w\) in \(L^2\) by dominated convergence; the norm of the second is at most \(R^{-1}\|\nabla\theta\|_\infty\|w\|_2\). Convolving each compactly supported field with \(J_\delta\) gives compact smooth fields converging to it in \(H^1\), by the Fourier dominated-convergence argument after (2.2). A diagonal choice gives compact smooth \(w_j\to w\) in \(H^1\).

Apply (3.1) to \(w_j-w_k\). The sequence is Cauchy in \(L^6\) and has a limit there. On each bounded set, Hölder's inequality makes \(L^6\) convergence imply \(L^2\) convergence. The limit must therefore be \(w\) almost everywhere. Passing to the norms proves (3.1) on \(H^1\).

A further Cauchy–Schwarz estimate yields

\[
 \int|w|^4
 \leq\left(\int|w|^2\right)^{1/2}
      \left(\int|w|^6\right)^{1/2},
 \qquad
 \|w\|_4^2\leq S^{3/2}\|w\|_2^{1/2}\|\nabla w\|_2^{3/2}.
 \tag{3.7}
\]

For \(v_\varepsilon=J_\varepsilon u_\varepsilon\), contraction and commutation with the gradient then give

\[
 \int_0^T\|u_\varepsilon\|_2\|v_\varepsilon\|_4^2\,dt
 \leq S^{3/2}A_T^{3/4}T^{1/4}(A_T/\nu)^{3/4}.
 \tag{3.8}
\]

Indeed the integrand is at most \(S^{3/2}E_\varepsilon^{3/4}D_\varepsilon^{3/4}\), and Hölder with exponents \(4/3\) and \(4\) bounds the time integral of \(D_\varepsilon^{3/4}\).

## 4. Energy outside a large ball

Choose a smooth scalar cutoff \(\eta\), zero on \(B_1\), one outside \(B_2\), and with \(0\leq\eta\leq1\). Such a cutoff follows by integrating a nonnegative smooth function on the interval \((1,2)\) and composing the resulting constant-near-endpoints function with \(|x|\). Set, for \(R>2\),

\[
 \eta_R(x)=\eta(x/R),\qquad
 C_1=\|\nabla\eta\|_\infty,\quad C_2=\|\Delta\eta\|_\infty,\quad
 K_\rho=1+\int|y|\,|\nabla\rho(y)|\,dy.
 \tag{4.1}
\]

### The smoothing commutator

The difference between smoothing a weighted velocity and weighting a smoothed velocity is

\[
 c_\varepsilon=J_\varepsilon(\eta_Ru_\varepsilon)
                    -\eta_Rv_\varepsilon.
 \tag{4.2}
\]

Its full derivative is

\[
 \begin{aligned}
 \partial_j c_{\varepsilon,i}(x)
 &=\int \partial_j\rho_\varepsilon(x-z)
       [\eta_R(z)-\eta_R(x)]u_{\varepsilon,i}(z)\,dz\\
 &\quad-(\partial_j\eta_R(x))v_{\varepsilon,i}(x).
 \end{aligned}
 \tag{4.3}
\]

This follows by differentiating the convolution in its integration variable \(z\); only the kernel and the displayed value \(\eta_R(x)\) depend on \(x\). The mean-value bound
\(|\eta_R(z)-\eta_R(x)|\leq(C_1/R)|x-z|\), (2.7), and

\[
 \int |y|\,|\nabla\rho_\varepsilon(y)|\,dy
 =\int |z|\,|\nabla\rho(z)|\,dz
 \tag{4.4}
\]

give the important estimate

\[
 \|\nabla c_\varepsilon\|_2
 \leq\frac{C_1K_\rho}{R}\|u_\varepsilon\|_2.
 \tag{4.5}
\]

In (4.4) the factors are \(\varepsilon\), \(\varepsilon^{-4}\) and \(\varepsilon^3\), whose product is one. No derivative of \(u_\varepsilon\) is needed in (4.5).

### The pressure and the actual force in the approximate equation

Define

\[
 \widehat p_\varepsilon(\xi)=
 -\sum_{i,j=1}^3\frac{\xi_i\xi_j}{|\xi|^2}
                  \widehat{v_{\varepsilon,i}v_{\varepsilon,j}}(\xi)
 \quad(\xi\ne0).
 \tag{4.6}
\]

The matrix \(\xi\otimes\xi/|\xi|^2\) has squared Frobenius norm
\(\sum_{i,j}\xi_i^2\xi_j^2/|\xi|^4=1\). Cauchy–Schwarz in the matrix indices and Plancherel therefore prove

\[
 \|p_\varepsilon\|_2\leq\|v_\varepsilon\otimes v_\varepsilon\|_2
                         =\|v_\varepsilon\|_4^2.
 \tag{4.7}
\]

Coefficient by coefficient, \(P\operatorname{div}(v_\varepsilon\otimes v_\varepsilon)
=\operatorname{div}(v_\varepsilon\otimes v_\varepsilon)+\nabla p_\varepsilon\). Thus (2.4) is exactly

\[
 \partial_tu_\varepsilon+
 J_\varepsilon\operatorname{div}(v_\varepsilon\otimes v_\varepsilon)
 +\nabla J_\varepsilon p_\varepsilon
 =\nu\Delta u_\varepsilon+J_\varepsilon Pf.
 \tag{4.8}
\]

We retain the projected force by an explicit representation. Define the Fourier multiplier \(h=(1-\Delta)^{-1}Pf\), and set

\[
 g=h,\qquad G_{ij}=-\partial_jh_i.
 \tag{4.9}
\]

Then \(g,G\in L^2(0,T;L^2)\), and

\[
 Pf=g+\operatorname{div}G,\qquad
 \|g\|_2^2+\|G\|_2^2
 =\int\frac{|P(\xi)\widehat f(\xi)|^2}{1+4\pi^2|\xi|^2}\,d\xi
 =\|Pf\|_{H^{-1}}^2\leq F^2.
 \tag{4.10}
\]

Indeed \(g+\operatorname{div}G=h-\Delta h\), and the two norm terms have combined multiplier
\((1+4\pi^2|\xi|^2)/(1+4\pi^2|\xi|^2)^2\). This proves every part of (4.10), including the signs and the full inhomogeneous denominator.

Define a tail of this fixed, unsmoothed force representation:

\[
 B_T(R)=
 \left[\int_0^T\int_{|x|>R}(|g|^2+|G|^2)\,dx\,dt\right]^{1/2}.
 \tag{4.11}
\]

Integrability gives \(B_T(R)\to0\). Since \(\rho_\varepsilon\) is supported in \(B_\varepsilon\subset B_1\), Jensen and Fubini give

\[
 \int_0^T\int_{|x|>R}
       (|J_\varepsilon g|^2+|J_\varepsilon G|^2)\,dx\,dt
 \leq B_T(R-1)^2.
 \tag{4.12}
\]

For example, \(|x|>R\) and \(|y|<1\) imply \(|x-y|>R-1\) in the convolution integral. This proves the estimate uniformly for all \(\varepsilon\leq1\), without a support assertion about \(Pf\).

### Localized energy and its uniform bound

Pair (4.8) with \(\eta_Ru_\varepsilon\) and use (4.9). The exact result is

\[
 \begin{aligned}
 &\frac12\frac d{dt}\int\eta_R|u_\varepsilon|^2
       +\nu\int\eta_R|\nabla u_\varepsilon|^2\\
 &\quad=\frac{\nu}{2}\int\Delta\eta_R|u_\varepsilon|^2
       +\frac12\int|v_\varepsilon|^2v_\varepsilon\cdot\nabla\eta_R\\
 &\qquad+\int\nabla c_\varepsilon : (v_\varepsilon\otimes v_\varepsilon)
       +\int J_\varepsilon p_\varepsilon\,
                                  u_\varepsilon\cdot\nabla\eta_R\\
 &\qquad+\int J_\varepsilon g\cdot\eta_Ru_\varepsilon
       -\int J_\varepsilon G : \nabla(\eta_Ru_\varepsilon).
 \end{aligned}
 \tag{4.13}
\]

For the nonlinear term, self-adjointness first gives

\[
 \begin{aligned}
 -(\eta_Ru_\varepsilon,
        J_\varepsilon\operatorname{div}(v_\varepsilon\otimes v_\varepsilon))
 &=\int\nabla(\eta_Rv_\varepsilon+c_\varepsilon)
                                      : (v_\varepsilon\otimes v_\varepsilon)\\
 &=\frac12\int |v_\varepsilon|^2v_\varepsilon\cdot\nabla\eta_R
       +\int\nabla c_\varepsilon : (v_\varepsilon\otimes v_\varepsilon).
 \end{aligned}
 \tag{4.14}
\]

The product rule produces one full flux from the derivative of \(\eta_R\) and a negative one-half flux from integrating \(\eta_Rv_\varepsilon\cdot\nabla(|v_\varepsilon|^2/2)\). Their sum is the positive one-half in (4.14). For the pressure, integration by parts and \(\operatorname{div}u_\varepsilon=0\) give the positive pressure flux in (4.13). For diffusion, the product rule and a second integration by parts give
\(-\nu\int\eta_R|\nabla u_\varepsilon|^2+(\nu/2)\int\Delta\eta_R|u_\varepsilon|^2\).
The force signs follow from \(g+\operatorname{div}G\).

These integrations on an unbounded domain are legitimate. They may first be performed with an additional compact cutoff \(\theta(x/K)\) and then with \(K\to\infty\). Its derivative is bounded by a constant times \(K^{-1}\). Cubic velocity terms are integrable by the regularized \(L^\infty\cap L^2\) bounds, pressure times velocity is integrable by (4.7), and the force and gradient terms are products of \(L^2\) functions. The additional errors tend to zero. The time derivative of the localized squared norm follows from the \(L^2\) absolute continuity already proved and the bounded multiplication operator \(\eta_R\).

The three nonlinear and pressure terms on the right of (4.13) are bounded, in order, by

\[
 \frac{C_1}{2R}\|u_\varepsilon\|_2\|v_\varepsilon\|_4^2,\qquad
 \frac{C_1K_\rho}{R}\|u_\varepsilon\|_2\|v_\varepsilon\|_4^2,\qquad
 \frac{C_1}{R}\|u_\varepsilon\|_2\|v_\varepsilon\|_4^2.
 \tag{4.15}
\]

The first uses \(\int|v|^3\leq\|v\|_2\|v\|_4^2\); the second uses (4.5); the third uses (4.7) and contraction of \(J_\varepsilon\). Thus (3.8) controls their time integrals.

For the two force terms together, the triangle inequality in the product Hilbert space gives

\[
 \left(\|\eta_Ru_\varepsilon\|_2^2+
       \|\nabla(\eta_Ru_\varepsilon)\|_2^2\right)^{1/2}
 \leq(1+C_1/R)\|u_\varepsilon\|_{H^1}.
 \tag{4.16}
\]

Use the two vectors \((\eta_Ru_\varepsilon,\eta_R\nabla u_\varepsilon)\) and
\((0,u_\varepsilon\otimes\nabla\eta_R)\) to see this directly. The support of these weighted fields lies outside \(B_R\). Cauchy–Schwarz in space, time and the force pair, followed by (4.12), bounds the integrated force work by

\[
 (1+C_1/R)M_T^{1/2}B_T(R-1).
 \tag{4.17}
\]

At time zero, (2.2) and the same support argument give
\(\int\eta_R|J_\varepsilon u_0|^2\leq
\|1_{\{|x|>R-1\}}u_0\|_2^2\).
Integrate (4.13), drop its nonnegative dissipation and multiply by two. Since \(\eta_R=1\) outside \(B_{2R}\), for every \(t\leq T\) we obtain

\[
 \begin{aligned}
 \int_{|x|>2R}|u_\varepsilon(t,x)|^2\,dx
 &\leq \|1_{\{|x|>R-1\}}u_0\|_2^2
       +\frac{\nu C_2 T A_T}{R^2}\\
 &\quad+\frac{2C_1(K_\rho+3/2)}{R}
           S^{3/2}A_T^{3/4}T^{1/4}(A_T/\nu)^{3/4}\\
 &\quad+2(1+C_1/R)M_T^{1/2}B_T(R-1)
 =:\mathcal T_T(R).
 \end{aligned}
 \tag{4.18}
\]

Every term on the right tends to zero as \(R\to\infty\). It depends on the original data, viscosity, chosen kernels and \(T\), but not on \(\varepsilon\). This is the uniform control of energy at spatial infinity that the whole-space limit needs.

## 5. Strong convergence on the entire space

We next control time changes in a space of distributions. Fix an integer \(m>5/2\) and define

\[
 C_m=\left[\int_{\mathbb R^3}
       4\pi^2|\xi|^2(1+4\pi^2|\xi|^2)^{-m}\,d\xi\right]^{1/2}.
 \tag{5.1}
\]

This integral is finite. Near zero its radial integrand is bounded by a constant times \(r^4\); at infinity it is bounded by a constant times \(r^{4-2m}\), whose integral converges because \(m>5/2\). Fourier inversion and Cauchy–Schwarz give
\(\|\nabla\phi\|_\infty\leq C_m\|\phi\|_{H^m}\).
For a vector field \(a\in L^2\), it follows that

\[
 \|\operatorname{div}(a\otimes a)\|_{H^{-m}}
 \leq C_m\|a\|_2^2.
 \tag{5.2}
\]

Indeed its pairing with \(\phi\) is
\(-\int\sum_{i,j}a_i a_j\partial_j\phi_i\), whose magnitude is at most
\(\|a\|_2^2\|\nabla\phi\|_\infty\).
The identification with an \(H^{-m}\) element is the weighted Fourier Hilbert-space duality from (1.2). Also
\(\|\Delta a\|_{H^{-1}}\leq\|\nabla a\|_2\) for \(a\in H^1\), because
\((4\pi^2|\xi|^2)^2/(1+4\pi^2|\xi|^2)\leq4\pi^2|\xi|^2\).
Thus (2.4) implies

\[
 \begin{gathered}
 \|\partial_tu_\varepsilon\|_{H^{-m}}
 \leq\nu\|\nabla u_\varepsilon\|_2+
          C_m\|u_\varepsilon\|_2^2+F,\\
 \|\partial_tu_\varepsilon\|_{L^2(0,T;H^{-m})}
 \leq K_T:=\sqrt{\nu A_T}+C_mA_T\sqrt T+\|F\|_{L^2(0,T)}.
 \end{gathered}
 \tag{5.3}
\]

All projections and smoothing operators in this estimate have norm at most one on the indicated spaces.

### Compactness on each bounded region

Take the sequence \(\varepsilon_j=1/j\). For each positive integer \(R\), choose a smooth \(\chi_R\), equal to one on \(B_{2R}\), supported in \(B_{3R}\), between zero and one, and satisfying
\(\|\nabla\chi_R\|_\infty\leq C_\chi/R\) for a fixed finite \(C_\chi\). Regard \(\chi_Ru_{\varepsilon_j}\) as a periodic field on the cube
\(Q_R=(-4R,4R)^3\), of volume \(V_R=(8R)^3\). Its support lies strictly inside the cube, so its periodic extension has the same \(H^1\) norm as its restriction and has no boundary jump.

For each component \(i\) and \(k\in\mathbb Z^3\), define

\[
 a_{j,R,k,i}(t)=\frac1{V_R}\int
   \chi_R(x)u_{\varepsilon_j,i}(t,x)
             e^{-2\pi i k\cdot x/(8R)}\,dx.
 \tag{5.4}
\]

Cauchy–Schwarz bounds its absolute value by \(V_R^{-1/2}\sqrt{A_T}\).
Testing (5.3) against the fixed compact smooth function
\(\chi_Re^{-2\pi i k\cdot x/(8R)}e_i\) gives

\[
 |a_{j,R,k,i}(t)-a_{j,R,k,i}(s)|
 \leq \frac{K_T}{V_R}
       \|\chi_Re^{-2\pi i k\cdot x/(8R)}\|_{H^m}
       |t-s|^{1/2}.
 \tag{5.5}
\]

The complex pairing can be read as its real and imaginary parts; the same Cauchy–Schwarz bound holds in the complexified Hilbert space. For each fixed \(R,k,i,T\), the coefficients are uniformly bounded and have a common modulus of continuity. The finite-grid diagonal proof in the periodic chapter, Section 3, therefore supplies a uniformly convergent subsequence. Diagonalize over the countably many indices \(R,k,i\) and integer time endpoints \(T\).

The high frequencies of \(\chi_Ru_{\varepsilon_j}\) are controlled by the exact gradient product rule. In particular,

\[
 \int_0^T\|\nabla(\chi_Ru_{\varepsilon_j})\|_2^2\,dt
 \leq\frac{2A_T}{\nu}+\frac{2C_\chi^2TA_T}{R^2}.
 \tag{5.6}
\]

This uses \(|a+b|^2\leq2|a|^2+2|b|^2\), not an assumption that the derivative of the cutoff is absent. If \(E_{R,K}\) is the periodic projection on \(Q_R\) to frequencies \(|k/(8R)|\leq K\), Parseval gives

\[
 \int_0^T\|(I-E_{R,K})(\chi_Ru_{\varepsilon_j})\|_2^2\,dt
 \leq\frac1{4\pi^2K^2}
       \left(\frac{2A_T}{\nu}+\frac{2C_\chi^2TA_T}{R^2}\right).
 \tag{5.7}
\]

For fixed \(R\), first choose \(K\) large, then use uniform convergence of the finitely many retained coefficients. The triangle inequality with the two omitted tails proves that the selected sequence is Cauchy in
\(L^2(0,T;L^2(B_{2R}))\), for every finite \(T\).

### From local to global strong convergence

For two elements of this same subsequence, (4.18) gives

\[
 \begin{aligned}
 \|u_{\varepsilon_j}-u_{\varepsilon_\ell}\|_{L^2(0,T;L^2(\mathbb R^3))}
 &\leq\|u_{\varepsilon_j}-u_{\varepsilon_\ell}\|_{L^2(0,T;L^2(B_{2R}))}\\
 &\quad+2\sqrt{T\mathcal T_T(R)}.
 \end{aligned}
 \tag{5.8}
\]

Given any positive tolerance, choose \(R\) so that the last term is smaller than half that tolerance. The local Cauchy property then controls the first term. Completeness gives a global limit with

\[
 u_{\varepsilon_j}\longrightarrow u
       \quad\text{strongly in }L^2(0,T;L^2(\mathbb R^3))
       \quad(T<\infty).
 \tag{5.9}
\]

The uniform \(L^2_tH^1_x\) bound and the Hilbert-space coordinate argument proved in the periodic chapter give a further subsequence converging weakly in \(L^2(0,T;H^1)\), simultaneously for integer \(T\). The weak limit is the same \(u\), by (5.9) and the continuous inclusion into \(L^2_tL^2_x\). In particular the gradients converge weakly in \(L^2_{t,x}\).

### A representative at every time

To pass the endpoint energy, we need weak convergence at every time, not merely almost everywhere. Choose an orthonormal basis \(e_1,e_2,\ldots\) of real \(L^2(\mathbb R^3;\mathbb R^3)\) whose elements are compact smooth fields. Such a basis is obtained by Gram–Schmidt, discarding zeros, from a countable dense subset of compact smooth fields. Density follows from step-function approximation and convolution with compact smooth kernels; rational coefficients, rational boxes and a countable sequence of kernel widths suffice for countability. Each Gram–Schmidt step is a finite linear combination, so every resulting basis vector is still compact and smooth.

For each basis vector, (5.3) gives

\[
 |(u_{\varepsilon_j}(t)-u_{\varepsilon_j}(s),e_\ell)|
 \leq K_T\|e_\ell\|_{H^m}|t-s|^{1/2}.
 \tag{5.10}
\]

After another countable diagonal choice the coefficients converge uniformly on finite time intervals to continuous functions \(b_\ell(t)\). For every finite number of coefficients their squared sum is at most \(A_T\), by the bound on \(u_{\varepsilon_j}(t)\). Hence
\(\sum_\ell|b_\ell(t)|^2\leq A_T\), and they define an \(L^2\) vector at every \(t\). It equals the space-time limit almost everywhere, since the coefficients also converge in \(L^2\) in time. Use this representative of \(u\).

For any fixed \(h\in L^2\), approximate it by its first finitely many basis coordinates. The omitted scalar products have absolute value at most
\(\sqrt{A_T}\) times the norm of the omitted part of \(h\), uniformly in time, both for the sequence and its limit. This proves

\[
 u\in C_{\rm w}([0,\infty);L^2),\qquad
 u_{\varepsilon_j}(t)\rightharpoonup u(t)
        \text{ in }L^2\quad\text{for every }t\geq0.
 \tag{5.11}
\]

The range of the orthogonal projection \(P\) is weakly closed: for any \(h\),
\(((I-P)u(t),h)=\lim_j(u_{\varepsilon_j}(t),(I-P)h)=0\).
Thus the representative is divergence free at every time. At zero,
\(J_{\varepsilon_j}u_0\to u_0\) strongly in \(L^2\), so (5.11) gives \(u(0)=u_0\).

## 6. The equation and the energy inequality survive

The smoothed velocities also converge strongly:

\[
 \|J_{\varepsilon_j}u_{\varepsilon_j}-u\|_{L^2_tL^2_x}
 \leq\|u_{\varepsilon_j}-u\|_{L^2_tL^2_x}
       +\|J_{\varepsilon_j}u-u\|_{L^2_tL^2_x}\longrightarrow0.
 \tag{6.1}
\]

The second term tends to zero by Plancherel and dominated convergence in space and time. The exact tensor estimate from the periodic chapter consequently gives

\[
 v_{\varepsilon_j}\otimes v_{\varepsilon_j}
       \longrightarrow u\otimes u
       \quad\text{strongly in }L^1((0,T)\times\mathbb R^3).
 \tag{6.2}
\]

Let \(\phi\) be a smooth function of time, compactly supported in \([0,T)\), with values in \(H^m_\sigma\), where \(m>5/2\) is an integer. Pair (2.4) with \(\phi\). Its integrated identity is

\[
 \begin{aligned}
 &-\int_0^T(u_\varepsilon,\partial_t\phi)\,dt
   +\nu\int_0^T\int\nabla u_\varepsilon : \nabla\phi\,dx\,dt\\
 &\quad-\int_0^T\int
       \sum_{i,j}v_{\varepsilon,i}v_{\varepsilon,j}
                       \partial_jJ_\varepsilon\phi_i\,dx\,dt\\
 &\qquad=(J_\varepsilon u_0,\phi(0))
                 +\int_0^T\langle f,J_\varepsilon\phi\rangle\,dt.
 \end{aligned}
 \tag{6.3}
\]

The projected operators disappear from the scalar products because \(P\phi=\phi\). The gradients \( \nabla J_\varepsilon\phi\) converge uniformly in space and time to \(\nabla\phi\). To see uniformity in time, the image of the continuous \(H^m\)-valued map on the compact time interval is compact. Cover it by finitely many small \(H^m\) balls. Strong convergence of \(J_\varepsilon\) at their centers, its contraction bound, and (5.1) give the assertion. Thus (6.2) handles the nonlinear term. Strong \(L^2\) convergence handles the first term; weak gradient convergence handles diffusion. The initial term converges strongly, and the force term converges by (1.3) and \(J_\varepsilon\phi\to\phi\) in \(L^2_tH^1_x\).

We obtain the identity

\[
 \begin{aligned}
 &-\int_0^T(u,\partial_t\phi)\,dt
   +\nu\int_0^T\int\nabla u : \nabla\phi\,dx\,dt
   -\int_0^T\int\sum_{i,j}u_i u_j\partial_j\phi_i\,dx\,dt\\
 &\qquad=(u_0,\phi(0))+\int_0^T\langle f,\phi\rangle\,dt.
 \end{aligned}
 \tag{6.4}
\]

In particular, taking \(\phi=P\psi\) for smooth compact space-time vector tests \(\psi\) proves

\[
 \partial_tu=\nu\Delta u-P\operatorname{div}(u\otimes u)+Pf.
 \tag{6.5}
\]

Every term on the right is in \(L^2(0,T;H^{-m})\), by (5.2), the energy bounds and (1.1). We recover the full pressure equation in the next section.

For energy, integrate (2.14):

\[
 \frac12\|u_\varepsilon(t)\|_2^2+
       \nu\int_s^t\|\nabla u_\varepsilon\|_2^2\,dr
 =\frac12\|u_\varepsilon(s)\|_2^2+
       \int_s^t\langle f,J_\varepsilon u_\varepsilon\rangle\,dr.
 \tag{6.6}
\]

For every fixed interval \([s,t]\), its work term converges to the original work \(\int_s^t\langle f,u\rangle\). Indeed,

\[
 \int_s^t\langle f,J_\varepsilon u_\varepsilon\rangle\,dr
 =\int_s^t\langle J_\varepsilon f,u_\varepsilon\rangle\,dr.
 \tag{6.7}
\]

The norm of \(J_\varepsilon f-f\) in \(L^2(s,t;H^{-1})\) tends to zero by the same multiplier dominated convergence, whereas \(u_\varepsilon\) is bounded in \(L^2H^1\) and converges weakly there. This proves the asserted limit.

At \(s=0\) the norm on the right of (6.6) converges by strong convergence of the initial data. The norm at every ending time is lower semicontinuous by (5.11), and the integrated gradient norm is lower semicontinuous by weak \(L^2\) convergence on the interval. Thus (1.5) holds at \(s=0\) for every \(t\).

For other starting times choose a further subsequence so that

\[
 \int_0^j\|u_{\varepsilon_j}(r)-u(r)\|_2^2\,dr\leq2^{-j}.
 \tag{6.8}
\]

Tonelli's theorem gives, for each integer \(J\), a finite sum
\(\sum_{j\geq J}\|u_{\varepsilon_j}(s)-u(s)\|_2^2\)
for almost every \(s\in(0,J)\). Intersect these sets over \(J\), and also require that the \(H^1\) representative is defined. This yields one full-measure set \(G\) on which the initial norms in (6.6) converge strongly. At each such \(s\), the already established work convergence and lower semicontinuity at every ending time give (1.5) for all \(t\geq s\), along this one subsequence.

For \(s=0\) or \(s\in G\), Cauchy–Schwarz gives

\[
 \left|\int_s^t\langle f,u\rangle\,dr\right|
 \leq\left(\int_s^t\|f\|_{H^{-1}}^2\,dr\right)^{1/2}
      \left(\int_s^t\|u\|_{H^1}^2\,dr\right)^{1/2}\longrightarrow0
       \quad(t\downarrow s).
 \tag{6.9}
\]

Dropping the nonnegative dissipation in (1.5) gives
\(\limsup_{t\downarrow s}\|u(t)\|_2^2\leq\|u(s)\|_2^2\).
Weak continuity gives \((u(t),u(s))\to\|u(s)\|_2^2\). In
\[
 \|u(t)-u(s)\|_2^2
 =\|u(t)\|_2^2+\|u(s)\|_2^2-2(u(t),u(s)),
 \tag{6.10}
\]
these facts force the limit to zero. The original initial velocity is therefore attained strongly, and the stated strong right continuity holds.

## 7. Pressure, including the low frequencies of the force

First define a nonlinear pressure by

\[
 \widehat p_{\rm n}(\xi)=
 -\sum_{i,j=1}^3\frac{\xi_i\xi_j}{|\xi|^2}
                         \widehat{u_i u_j}(\xi)
 \quad(\xi\ne0).
 \tag{7.1}
\]

For almost every time \(u\in H^1\), so (3.7) gives \(u\in L^4\). The same matrix estimate as in (4.7) proves
\(\|p_{\rm n}\|_2\leq\|u\|_4^2\).
In time this becomes

\[
 \|p_{\rm n}\|_{L^{4/3}(0,T;L^2)}
 \leq S^{3/2}
       \|u\|_{L^\infty(0,T;L^2)}^{1/2}
       \|\nabla u\|_{L^2((0,T)\times\mathbb R^3)}^{3/2}.
 \tag{7.2}
\]

Raising the pointwise bound (3.7) to power \(4/3\) leaves
\(\|u\|_2^{2/3}\|\nabla u\|_2^2\); integration and power \(3/4\) give exactly (7.2). All maps involved are continuous between the indicated spaces, so the resulting pressure is strongly measurable.

The gradient part of the original force requires a second pressure. Set

\[
 a_f(\xi)=\frac{\xi\cdot\widehat f(\xi)}{2\pi i|\xi|^2}
 \quad(\xi\ne0).
 \tag{7.3}
\]

An \(H^{-1}\) element has a weighted \(L^2\) Fourier transform, so this expression is a function almost everywhere. For any frequency threshold \(\Lambda>0\), Cauchy–Schwarz gives

\[
 \begin{aligned}
 \int_{|\xi|\leq\Lambda}|a_f(\xi)|\,d\xi
 &\leq \|f\|_{H^{-1}}
   \left[\int_{|\xi|\leq\Lambda}
       \frac{1+4\pi^2|\xi|^2}{4\pi^2|\xi|^2}\,d\xi\right]^{1/2}\\
 &=\left(\frac{\Lambda}{\pi}+
                \frac{4\pi\Lambda^3}{3}\right)^{1/2}\|f\|_{H^{-1}}.
 \end{aligned}
 \tag{7.4}
\]

The last equality is integration in spherical coordinates, including the factor \(4\pi r^2\,dr\). It proves local integrability at zero, a point which cannot be removed merely by assigning a value to a multiplier there.

Let \(q_{\rm low}\) be the inverse Fourier integral of
\(1_{\{|\xi|\leq\Lambda\}}a_f\), and let \(q_{\rm high}\) be the \(L^2\) inverse transform of its complementary part. The latter is in \(L^2\) because

\[
 \begin{gathered}
 \|q_{\rm low}\|_\infty
 \leq\left(\frac{\Lambda}{\pi}+
                   \frac{4\pi\Lambda^3}{3}\right)^{1/2}\|f\|_{H^{-1}},\\
 \|q_{\rm high}\|_2^2
 \leq\int_{|\xi|>\Lambda}
          \frac{|\widehat f(\xi)|^2}{4\pi^2|\xi|^2}\,d\xi
 \leq\left(1+\frac1{4\pi^2\Lambda^2}\right)\|f\|_{H^{-1}}^2.
 \end{gathered}
 \tag{7.5}
\]

Both bounds are in \(L^2\) in time. The low-frequency inverse is a bounded continuous function of space for each admissible time, by dominated convergence in its absolutely convergent integral. Its dependence on the \(H^{-1}\) data is a bounded linear map to bounded continuous functions, so strong measurability follows from that of \(f\).

The sum \(q_f=q_{\rm low}+q_{\rm high}\) defines the inverse transform of the single tempered distribution \(a_f\). A different positive \(\Lambda\) changes the two terms by opposite inverse transforms on a bounded annulus; hence the sum is independent of the threshold. Conjugate symmetry of \(\widehat f\) makes \(q_f\) real. Multiplication by \(2\pi i\xi\) gives

\[
 \nabla q_f=(I-P)f.
 \tag{7.6}
\]

There is no extra contribution supported at \(\xi=0\): \(a_f\) was defined as an actual locally integrable function there, and multiplication by \(\xi\) preserves its almost-everywhere multiplier identity.

Set \(p=p_{\rm n}+q_f\). It is locally integrable in space and time by (7.2) and (7.5). Combining (7.1), (7.6) and (6.5) gives

\[
 \partial_tu+\operatorname{div}(u\otimes u)+\nabla p
 =\nu\Delta u+f,\qquad
 \Delta p=\operatorname{div}f-\sum_{i,j}\partial_i\partial_j(u_i u_j).
 \tag{7.7}
\]

This proves the theorem. The whole-space \(L^2\) condition does not require a spatial mean: an \(L^2\) velocity need not be integrable, so its integral over the whole space need not exist. No zero-mean restriction has been added.

## 8. Weak–strong uniqueness on the whole space

We now compare any solution with properties (1.4)–(1.5) to a divergence-free solution \(v\) of the same projected equation and force on \([0,T]\), with

\[
 v\in C^1([0,T];L^2_\sigma)
       \cap C([0,T];H^m_\sigma),\qquad
 m\in\mathbb N,\quad m>5/2.
 \tag{8.1}
\]

We will prove, with \(L(t)=\|\nabla v(t)\|_\infty\), that

\[
 \|u(t)-v(t)\|_2^2
 \leq\|u(s)-v(s)\|_2^2
          \exp\left(2\int_s^t L(r)\,dr\right)
 \quad(s=0\text{ or }s\in G,\ s\leq t\leq T).
 \tag{8.2}
\]

The main additional issue is that the comparison field is not compactly supported. We justify its use without assuming an unproved decay of the pressure.

A weakly continuous \(L^2\) representative satisfies its essential \(L^\infty_tL^2_x\) bound at every time. Indeed approach any time by times at which that bound holds, and use weak continuity and lower semicontinuity of the norm. Thus all endpoint pairings used below have the same boundedness as the energy class.

### A curl-free distribution in a Sobolev space

If \(H\in H^{-m}(\mathbb R^3;\mathbb R^3)\) and
\(\partial_iH_j-\partial_jH_i=0\) for all \(i,j\), then \(PH=0\).
Indeed the Fourier transform of \(H\) is a weighted \(L^2\) function. The curl identities give
\(\xi_i\widehat H_j-\xi_j\widehat H_i=0\) almost everywhere. Away from zero these say that \(\widehat H\) is parallel to \(\xi\), so (2.3) kills it. A single frequency point has measure zero, and a weighted \(L^2\) function has no delta contribution there. This proves the assertion.

For a solution of (1.4), integrate the momentum equation against any smooth compactly supported scalar time function \(\zeta\) in the interior of the time interval. The vector distribution

\[
 H_\zeta=
 -\int u\,\zeta'\,dt
 +\int\big[\operatorname{div}(u\otimes u)-\nu\Delta u-f\big]\zeta\,dt
 \tag{8.3}
\]

lies in \(H^{-m}\), by (5.2) and the energy spaces. The original equation says it is the negative gradient of the time-integrated pressure, so it is curl free. The preceding argument gives \(PH_\zeta=0\). Since \(Pu=u\), this proves the projected equation (6.5) for every solution in our definition, not only the solution produced by the approximation.

Its right side belongs to \(L^2_tH^{-m}_x\), by the estimate used in (5.3). Hence the velocity has an absolutely continuous \(H^{-m}\) representative with that derivative. To verify this last assertion directly, subtract the time integral of the right side. Its distributional time derivative is zero, so its pairing with each \(H^m\) test is constant, by the scalar distributional fundamental theorem. These constants define an \(H^{-m}\) vector. Weak \(L^2\) continuity and the initial trace identify the representative at every time with the given \(u\). In particular its endpoints are the prescribed ones.

### The cross identity

Let \(E_K\) be the whole-space Fourier projection onto \(|\xi|\leq K\). This operator maps \(L^2\) boundedly into \(H^m\), with norm at most \((1+4\pi^2K^2)^{m/2}\). Thus \(E_Kv\in C^1H^m\). The product rule for an absolutely continuous \(H^{-m}\) function paired with a \(C^1H^m\) function gives an integrated identity for \((u,E_Kv)\). This product rule follows from the difference of the two pairings at nearby times, writing one difference using the integral of \(u_t\) and the other using the integral of \((E_Kv)_t\); continuity and integrability allow the limit and integration.

Insert (6.5) into this identity. Since \(PE_Kv=E_Kv\), the force pairing is \(\langle f,E_Kv\rangle\), and the nonlinear pairing is
\(\int\sum_{i,j}u_i u_j\partial_jE_Kv_i\).
Now \(E_Kv\to v\) uniformly in \(H^m\) on \([0,T]\), and
\(E_Kv_t\to v_t\) uniformly in \(L^2\). This follows from strong convergence of \(E_K\), its contraction on those spaces, and the finite-cover argument for the two compact time images. Equation (5.1) gives uniform convergence of the spatial gradients in \(L^\infty\). The energy bounds and (1.3) justify every limit, yielding for all \(0\leq s\leq t\leq T\)

\[
 \begin{aligned}
 &(u(t),v(t))-(u(s),v(s))\\
 &\quad=\int_s^t\left[(u,\partial_rv)
       +\int\sum_{i,j}u_i u_j\partial_jv_i\,dx
       -\nu\int\nabla u : \nabla v\,dx
       +\langle f,v\rangle\right]dr.
 \end{aligned}
 \tag{8.4}
\]

No unbounded spatial test was inserted into the pressure term. Its removal was proved by (8.3) and the curl-free Sobolev argument.

### Relative energy and its consequence

For the regular solution, the equation gives

\[
 Pf=\partial_tv-\nu\Delta v+
                P\operatorname{div}(v\otimes v)\in C([0,T];L^2).
 \tag{8.5}
\]

Here \(m\geq3\) gives \(\Delta v\in CL^2\) and, by (5.1),
\((v\cdot\nabla)v\in CL^2\). The force pairing against divergence-free \(H^1\) vectors agrees with this \(L^2\) representative. The energy identity for \(v\) is therefore

\[
 \frac12\|v(t)\|_2^2+\nu\int_s^t\|\nabla v\|_2^2\,dr
 =\frac12\|v(s)\|_2^2+\int_s^t\langle f,v\rangle\,dr.
 \tag{8.6}
\]

Its nonlinear cancellation follows by the same outer-cutoff calculation used in (2.13), since \(v\in L^\infty_x\cap L^2_x\). Diffusion follows by \(H^1\) integration by parts. Thus no spatial boundary term remains.

Set \(z=u-v\). Equation (8.5), paired with \(u\in H^1_\sigma\) at almost every time, gives

\[
 (u,\partial_tv)
 =-\nu\int\nabla u : \nabla v\,dx
   -\int\sum_{i,j}u_i v_j\partial_jv_i\,dx
   +\langle f,u\rangle.
 \tag{8.7}
\]

The two nonlinear terms in (8.4) and (8.7) combine as

\[
 \begin{aligned}
 \int\sum_{i,j}u_i(u_j-v_j)\partial_jv_i\,dx
 &=\int\sum_{i,j}z_i z_j\partial_jv_i\,dx
       +\frac12\int z\cdot\nabla|v|^2\,dx\\
 &=\int\sum_{i,j}z_i z_j\partial_jv_i\,dx.
 \end{aligned}
 \tag{8.8}
\]

The last equality is valid because \(|v|^2\in H^1\) and \(z\) is divergence free. More explicitly, \(v\in L^\infty\cap H^1\) gives \(|v|^2\in L^2\) and
\(\nabla|v|^2=2\sum_i v_i\nabla v_i\in L^2\). Approximate \(|v|^2\) in \(H^1\) by compact smooth scalar functions using the density proof in Section 3, and use
\(|\int z\cdot\nabla h|\leq\|z\|_2\|\nabla h\|_2\).

Add (1.5) and (8.6), then subtract (8.4), using (8.7)–(8.8). The full force work cancels, while both gradient norms and their cross term form \(\|\nabla z\|_2^2\). We obtain

\[
 \frac12\|z(t)\|_2^2+\nu\int_s^t\|\nabla z\|_2^2\,dr
 \leq\frac12\|z(s)\|_2^2
       -\int_s^t\int\sum_{i,j}z_i z_j\partial_jv_i\,dx\,dr.
 \tag{8.9}
\]

The matrix Cauchy–Schwarz inequality bounds the last spatial integral in absolute value by \(L(r)\|z(r)\|_2^2\). With \(Y(t)=\|z(t)\|_2^2\), this gives
\[
 Y(t)\leq Y(s)+2\int_s^tL(r)Y(r)\,dr.
 \tag{8.10}
\]
Let \(H(t)=Y(s)+2\int_s^tL(r)Y(r)\,dr\). It is absolutely continuous,
\(Y\leq H\), and \(H'\leq2LH\) almost everywhere. Multiplication by
\(\exp[-2\int_s^tL]\) shows that this factor times \(H(t)\) is nonincreasing. Therefore (8.2) follows. If the initial velocities agree, take \(s=0\) to conclude equality at every time in the comparison interval.

## 9. Including time-integrable square-integrable forces

The construction also covers the force class used in the definition cited from Albritton, Brué and Colombo. We now prove the extension, retaining the original equation.

**Extended theorem.** All the conclusions (1.4)–(1.5), the strong right trace and the weak–strong estimate (8.2) hold whenever the original force has a decomposition

\[
 f=f_a+f_b,\qquad
 f_a\in L^1(0,T;L^2),\qquad
 f_b\in L^2(0,T;H^{-1})
 \quad(T<\infty).
 \tag{9.1}
\]

One such decomposition, consistent on finite intervals, is enough. The equation and solution use the sum \(f\); the bounds below use the chosen decomposition. The work integral means the sum of the \(L^2\) pairing with \(f_a\) and the \(H^{-1},H^1\) pairing with \(f_b\). Both are integrable in the energy class.

The approximate equation is still exactly (2.4), with its forcing now written as
\(J_\varepsilon Pf_a+J_\varepsilon Pf_b\).
The first term is in \(L^1_tH^q_x\) for every \(q\), by (2.8) and
\(\|f_a\|_{H^{-1}}\leq\|f_a\|_2\); the second has the already proved \(L^2_tH^q_x\) bound. Both are \(L^1_tH^q_x\) on a finite interval. Thus the contraction (2.9)–(2.10), its \(CH^q\) regularity and its time differentiation remain valid, with the time derivative in \(L^1_tL^2_x\). Absolute continuity and the energy identity require precisely this integrability.

### The energy estimate with the additional force

Put \(a(t)=\|f_a(t)\|_2\) and \(b(t)=\|f_b(t)\|_{H^{-1}}\). The exact approximate work is
\((f_a,J_\varepsilon u_\varepsilon)+\langle f_b,J_\varepsilon u_\varepsilon\rangle\).
Keeping the first term linear in the velocity norm gives

\[
 E_\varepsilon'+\nu D_\varepsilon
 \leq\nu E_\varepsilon+2a\sqrt{E_\varepsilon}+\nu^{-1}b^2.
 \tag{9.2}
\]

Here the contribution of \(f_b\) uses the same square inequality as (2.15), including its \(E_\varepsilon\) part. Define

\[
 \begin{gathered}
 \alpha_T=\int_0^T e^{-\nu r/2}a(r)\,dr,\qquad
 \beta_T=\|u_0\|_2^2+\nu^{-1}\int_0^T e^{-\nu r}b(r)^2\,dr,\\
 X_T=\sup_{0\leq r\leq T}e^{-\nu r/2}\sqrt{E_\varepsilon(r)}.
 \end{gathered}
 \tag{9.3}
\]

Work first on any compact interval of existence. Multiplication of (9.2) by \(e^{-\nu t}\), integration, and removal of the nonnegative dissipation give
\(X_T^2\leq\beta_T+2\alpha_TX_T\).
Solving this quadratic inequality for its nonnegative unknown proves
\(X_T\leq\alpha_T+\sqrt{\alpha_T^2+\beta_T}\).
The integrated version of (9.2), before removing dissipation, is

\[
 e^{-\nu t}E_\varepsilon(t)+
       \nu\int_0^t e^{-\nu r}D_\varepsilon(r)\,dr
 \leq\beta_T+2\alpha_TX_T
 \leq\left(\alpha_T+\sqrt{\alpha_T^2+\beta_T}\right)^2.
 \tag{9.4}
\]

In the last step the square on the right equals \(\beta_T\) plus twice \(\alpha_T\) times its square root. Consequently, with

\[
 \mathcal A_T=e^{\nu T}
       \left(\alpha_T+\sqrt{\alpha_T^2+\beta_T}\right)^2,\qquad
 \mathcal M_T=(T+\nu^{-1})\mathcal A_T,
 \tag{9.5}
\]

we have

\[
 E_\varepsilon(t)+\nu\int_0^tD_\varepsilon(r)\,dr
 \leq\mathcal A_T,\qquad
 \int_0^T\|u_\varepsilon\|_{H^1}^2\,dr\leq\mathcal M_T.
 \tag{9.6}
\]

The endpoint continuation argument from Section 2 therefore gives a global approximate solution. All constants are uniform in \(\varepsilon\).

### The time and spatial tails

The additional term in the time derivative estimate is \(a(t)\). For every fixed \(H^m\) test \(\phi\), integration and Cauchy–Schwarz give

\[
 \begin{aligned}
 |(u_\varepsilon(t)-u_\varepsilon(s),\phi)|
 \leq\|\phi\|_{H^m}\bigg[
 &\left(\sqrt{\nu\mathcal A_T}
       +C_m\mathcal A_T\sqrt T+\|b\|_{L^2(0,T)}\right)|t-s|^{1/2}\\
 &+\int_s^t a(r)\,dr\bigg].
 \end{aligned}
 \tag{9.7}
\]

The integral of the single fixed \(L^1\) function \(a\) is absolutely continuous, uniformly over intervals of small length. Thus (9.7) is a common modulus of continuity. It supplies the uniform coefficient convergence used in Section 5 even though the full time derivative is now only \(L^1_tH^{-m}_x\).

For spatial tails, apply (4.9)–(4.12) to \(Pf_b\), and denote its resulting \(L^2\) tail by \(B_{b,T}(R)\). Retain \(Pf_a\) as an \(L^1_tL^2_x\) field and define

\[
 B_{a,T}(R)=\int_0^T
                 \|1_{\{|x|>R\}}Pf_a(r)\|_2\,dr.
 \tag{9.8}
\]

For almost every time, its spatial tail tends to zero; it is bounded by \(a(r)\). Dominated convergence therefore gives \(B_{a,T}(R)\to0\).
The support and Jensen argument from (4.12) bounds the tail of \(J_\varepsilon Pf_a\) outside \(B_R\) by the corresponding tail of \(Pf_a\) outside \(B_{R-1}\).
Its additional localized work is consequently at most
\(\sqrt{\mathcal A_T}B_{a,T}(R-1)\).
All the commutator, pressure and diffusion calculations in (4.13) remain exact. The resulting bound is

\[
 \begin{aligned}
 \int_{|x|>2R}|u_\varepsilon(t,x)|^2\,dx
 &\leq\|1_{\{|x|>R-1\}}u_0\|_2^2
       +\frac{\nu C_2T\mathcal A_T}{R^2}\\
 &\quad+\frac{2C_1(K_\rho+3/2)}{R}
       S^{3/2}\mathcal A_T^{3/4}T^{1/4}
                         (\mathcal A_T/\nu)^{3/4}\\
 &\quad+2(1+C_1/R)\mathcal M_T^{1/2}B_{b,T}(R-1)
       +2\sqrt{\mathcal A_T}B_{a,T}(R-1).
 \end{aligned}
 \tag{9.9}
\]

Every term tends to zero, uniformly in \(\varepsilon\) and \(t\leq T\).
Equations (9.6), (9.7) and (9.9) provide, respectively, the derivative bound in space, continuity of each localized Fourier coefficient in time, and the spatial tail. These are exactly the three inputs of the proved compactness argument (5.4)–(5.11). That argument therefore gives global strong \(L^2_{t,x}\), weak \(L^2_tH^1_x\), and weak \(L^2_x\) convergence at every time in this force class as well.

### Work, pressure and the comparison theorem

The \(f_b\) work passes by (6.7). For the \(f_a\) work, \(J_\varepsilon f_a\to f_a\) in \(L^1_tL^2_x\), by pointwise \(L^2\) approximate-identity convergence and domination by \(2a(t)\). In

\[
 \int_s^t(f_a,J_\varepsilon u_\varepsilon)\,dr
 =\int_s^t(J_\varepsilon f_a-f_a,u_\varepsilon)\,dr
       +\int_s^t(f_a,u_\varepsilon)\,dr,
 \tag{9.10}
\]

the first term tends to zero by the uniform velocity bound. For the second, all-time weak convergence gives
\((f_a(r),u_\varepsilon(r))\to(f_a(r),u(r))\) at almost every time. Its absolute value is at most \(\sqrt{\mathcal A_T}a(r)\). Dominated convergence proves the desired work limit on every interval.

The equation (6.3) passes for the extra force term by the same \(L^1L^2\) convergence and bounded continuous \(L^2\) test. The rapidly convergent subsequence in (6.8) and all lower-semicontinuity steps are unchanged. They yield (1.5) for the actual sum \(f\). Strong right continuity follows because the additional work on a shrinking interval is bounded by
\(\sqrt{\mathcal A_T}\int_s^t a(r)\,dr\), which tends to zero; the \(f_b\) work is controlled by (6.9).

Apply the linear pressure construction (7.3)–(7.6) to each force component and add the results. For \(f_a\), the low- and high-frequency bounds in (7.5) are \(L^1\) in time since \(\|f_a\|_{H^{-1}}\leq a\). For \(f_b\), they are \(L^2\) in time as before. Together with (7.2), this supplies a locally integrable pressure and recovers the full equation with \(f_a+f_b\).

For any weak solution in this extended energy class, (8.3) still belongs to \(H^{-m}\), so its curl-free argument proves the projected equation. Its time derivative is \(L^1H^{-m}\), which still gives absolute continuity and the product rule used with \(E_Kv\). The cross identity (8.4), regular energy identity (8.6) and both force pairings are integrable: use \(L^1L^2\) against bounded \(L^2\) velocities for \(f_a\), and \(L^2H^{-1}\) against \(L^2H^1\) velocities for \(f_b\). The sum of these force contributions cancels exactly in (8.9). The same relative energy estimate and integrating factor prove (8.2). This completes the extended theorem.

**Periodic consequence.** The same force-class extension holds for the arbitrary periodic box in the preceding chapter, in every dimension \(n\geq2\), with its original lengths and viscosity. Here is the complete transfer of the proof. The finite Galerkin forcing coefficients are now \(L^1\) in time, which is exactly the integrability used by its local integral contraction. The energy identity has the full work \((f_a,u_N)+\langle f_b,u_N\rangle\); inequalities (9.2)–(9.6) follow with the periodic norms, by the same duality and projections. For the new part of each Fourier coefficient, the bound is \(V^{-1/2}a(t)\); its time integral supplies the extra modulus in (9.7). The original nonlinear and \(f_b\) coefficient bounds remain those of the periodic chapter (3.3). The high-frequency estimate there, (3.4), holds with \(\mathcal A_T\) in place of \(A_T\). Its finite-mode proof therefore yields global strong \(L^2_{t,x}\) on the box and weak convergence at every endpoint.

The additional force work now passes directly by dominated convergence of \((f_a(t),u_N(t))\), bounded by \(\sqrt{\mathcal A_T}a(t)\); no smoothing is present in this Galerkin work pairing. The other work term, the good starting-time set, and the strong right trace follow exactly from the displayed convergence and estimates (6.6)–(6.10) above. The periodic pressure formula (6.5) of the preceding chapter is still defined: its input is now \(L^1_tH^{-m}_x\), and its bounded multiplier maps into \(L^1_tH^{1-m}_x\) for an integer \(m>n/2+1\). It recovers the full force, with mean-zero pressure and the same exact mean-velocity equation. Finally, its finite Fourier cross-identity proof only needs integrability of the force pairing. The \(L^1L^2\) and \(L^2H^{-1}\) terms have that property, cancel in relative energy, and give the same weak–strong estimate for the original regular comparison class. This proves the periodic consequence without a spatial-tail argument, which is needed only for the whole-space proof.

The inclusions used to compare force classes are actual maps into (9.1): send an \(L^1_tL^2_x\) force to \(f_a=f,f_b=0\), and an \(L^2_tH^{-1}_x\) force to \(f_a=0,f_b=f\). On a finite interval, the common class \(L^2_tL^2_x\) satisfies the explicit bounds

\[
 \|f\|_{L^1(0,T;L^2)}\leq\sqrt T\,\|f\|_{L^2(0,T;L^2)},\qquad
 \|f\|_{L^2(0,T;H^{-1})}\leq\|f\|_{L^2(0,T;L^2)}.
 \tag{9.11}
\]

The first is time Cauchy–Schwarz, the second the multiplier bound
\((1+4\pi^2|\xi|^2)^{-1}\leq1\). The theorem therefore contains both cited force settings with their original vectors and time dependence, without identifying their norms.

## 10. Five exercises with complete solutions

### Exercise 1. Energy which moves out of every bounded region

Choose a nonzero compact smooth divergence-free field \(w\) supported in \(B_1\). Set \(w_j(x)=w(x-4je_1)\). Prove that the sequence converges strongly to zero on every bounded region but has no strongly convergent subsequence in \(L^2(\mathbb R^3)\). What rules out this behavior in the construction above?

**Solution.** Such a field exists: take a compact smooth scalar function \(\psi\) with at least one nonzero derivative in the first two coordinates and set
\(w=(\partial_2\psi,-\partial_1\psi,0)\), after choosing its support in \(B_1\). Its divergence is zero by equality of mixed derivatives. Translation preserves all \(L^2\) norms of its derivatives, so

\[
 \|w_j\|_2=\|w\|_2>0,\qquad
 \|\nabla w_j\|_2=\|\nabla w\|_2.
 \tag{10.1}
\]

Every fixed bounded region is disjoint from the support for all sufficiently large \(j\); this proves local strong convergence to zero. Distinct supports are disjoint, giving

\[
 \|w_j-w_\ell\|_2^2=2\|w\|_2^2\quad(j\ne\ell).
 \tag{10.2}
\]

There is no Cauchy subsequence in global \(L^2\). For any fixed \(R\), however, the entire norm of \(w_j\) eventually lies outside \(B_{2R}\). Thus the sequence has no uniform spatial-tail estimate tending to zero. Estimate (4.18) supplies precisely that missing property for our approximations. This example concerns compactness of fields; these translated fields are not asserted to solve the same initial-value problem.

### Exercise 2. The derivative term in the smoothing commutator

For an affine weight \(\ell(x)=b\cdot x+c\) and a rapidly decreasing smooth vector field \(w\), compute
\(J_\varepsilon(\ell w)-\ell J_\varepsilon w\) and its derivative. Check that the derivative kernel has integral zero.

**Solution.** The exact difference is

\[
 J_\varepsilon(\ell w)(x)-\ell(x)J_\varepsilon w(x)
 =-\int (b\cdot y)\rho_\varepsilon(y)w(x-y)\,dy.
 \tag{10.3}
\]

Differentiate the convolution kernel, obtaining

\[
 \partial_j[J_\varepsilon(\ell w)-\ell J_\varepsilon w]
 =-\big[b_j\rho_\varepsilon+
               (b\cdot y)\partial_j\rho_\varepsilon\big]*w.
 \tag{10.4}
\]

The integral of the bracket is

\[
 b_j\int\rho_\varepsilon\,dy+
       \int(b\cdot y)\partial_j\rho_\varepsilon\,dy
 =b_j-b_j=0,
 \tag{10.5}
\]

by compact support and integration by parts. Thus both terms in (10.4) are required. The formula is the affine-weight instance of the two terms in (4.3). The undifferentiated commutator has the additional bound

\[
 \|J_\varepsilon(\ell w)-\ell J_\varepsilon w\|_2
 \leq\varepsilon|b|
          \left(\int|y|\rho(y)\,dy\right)\|w\|_2,
 \tag{10.6}
\]

while differentiation uses the moment of \(|\nabla\rho|\) with its exact scaling in (4.4). These are distinct estimates for the same specified operator.

### Exercise 3. Exact constants for the force pressure

For a fixed \(\Lambda>0\), prove that the two constants in (7.5) are the operator norms for their indicated maps from \(H^{-1}\), the first into \(L^\infty\) and the second into \(L^2\). The first may be attained; the second is a supremum.

**Solution.** The upper bounds have already been proved. For the low-frequency map choose the real vector distribution \(f\) whose Fourier transform is

\[
 \widehat f(\xi)=
 \frac{i\xi(1+4\pi^2|\xi|^2)}{2\pi|\xi|^2}
                 1_{\{0<|\xi|\leq\Lambda\}}.
 \tag{10.7}
\]

It is real because the transform has conjugate symmetry. It lies in \(H^{-1}\), with

\[
 \|f\|_{H^{-1}}^2
 =\int_{|\xi|\leq\Lambda}
       \frac{1+4\pi^2|\xi|^2}{4\pi^2|\xi|^2}\,d\xi
 =:C_{\rm low}^2
 =\frac{\Lambda}{\pi}+\frac{4\pi\Lambda^3}{3}.
 \tag{10.8}
\]

For this choice (7.3) is the nonnegative function
\((1+4\pi^2|\xi|^2)/(4\pi^2|\xi|^2)\) on the ball. Its inverse transform at \(x=0\) is \(C_{\rm low}^2\), and the triangle inequality bounds its absolute value everywhere by the same number. Consequently
\(\|q_{\rm low}\|_\infty/\|f\|_{H^{-1}}=C_{\rm low}\), proving equality in the first operator bound.

For the high-frequency map choose, for each \(\delta>0\),

\[
 \widehat f_\delta(\xi)=
       \frac{i\xi}{|\xi|}
           1_{\{\Lambda<|\xi|<\Lambda+\delta\}}.
 \tag{10.9}
\]

This again defines a real \(H^{-1}\) vector. Its squared norm ratio is

\[
 \frac{\|q_{{\rm high},\delta}\|_2^2}
      {\|f_\delta\|_{H^{-1}}^2}
 =
 \frac{\displaystyle\int_{\Lambda<|\xi|<\Lambda+\delta}
                         (4\pi^2|\xi|^2)^{-1}\,d\xi}
      {\displaystyle\int_{\Lambda<|\xi|<\Lambda+\delta}
                         (1+4\pi^2|\xi|^2)^{-1}\,d\xi}.
 \tag{10.10}
\]

This is an average, with positive denominator weight, of
\(1+(4\pi^2|\xi|^2)^{-1}\). It lies between its values at \(\Lambda+\delta\) and \(\Lambda\). As \(\delta\downarrow0\), the ratio tends to \(1+(4\pi^2\Lambda^2)^{-1}\). Taking square roots proves the exact norm asserted. No positive-measure frequency set outside the ball has the boundary value of this strictly decreasing radial factor, which accounts for the supremum description.

### Exercise 4. Different forces and initial velocities

Let \(u\) be a weak solution with force \(f\), and let \(v\) satisfy (8.1) with force \(g\in L^2(0,T;H^{-1})\). Derive a stability estimate retaining the viscosity and the full difference of the forces.

**Solution.** Put \(z=u-v\), \(Y(t)=\|z(t)\|_2^2\),
\(L(t)=\|\nabla v(t)\|_\infty\), and \(B(t)=\|f(t)-g(t)\|_{H^{-1}}\).
The cross identity uses \(f\) in its pairing with \(v\), because it comes from the weak equation for \(u\). The regular equation paired with \(u\) uses \(g\). Thus the remaining work in the relative energy calculation is exactly

\[
 \langle f,u\rangle+\langle g,v\rangle
           -\langle g,u\rangle-\langle f,v\rangle
 =\langle f-g,z\rangle.
 \tag{10.11}
\]

The same justified integrations as in Section 8 yield

\[
 \frac12Y(t)+\nu\int_s^t\|\nabla z\|_2^2\,dr
 \leq\frac12Y(s)+\int_s^tLY\,dr+
                      \int_s^t\langle f-g,z\rangle\,dr.
 \tag{10.12}
\]

Dual Cauchy–Schwarz and the nonnegative square used for (2.15) give

\[
 2|\langle f-g,z\rangle|
 \leq2B\sqrt{Y+\|\nabla z\|_2^2}
 \leq\nu Y+\nu\|\nabla z\|_2^2+\nu^{-1}B^2.
 \tag{10.13}
\]

After multiplication of (10.12) by two, the result is

\[
 Y(t)+\nu\int_s^t\|\nabla z\|_2^2\,dr
 \leq Y(s)+\int_s^t(2L+\nu)Y\,dr+\nu^{-1}\int_s^tB^2\,dr.
 \tag{10.14}
\]

Define \(a=2L+\nu\) and
\(H(t)=Y(s)+\int_s^t[a(r)Y(r)+\nu^{-1}B(r)^2]dr\).
Then \(Y\leq H\) and \(H'\leq aH+\nu^{-1}B^2\). Multiplying by
\(\exp(-\int_s^t a)\) and integrating gives the full estimate

\[
 \begin{aligned}
 Y(t)\leq
 \exp\left(\int_s^t[2L(r)+\nu]\,dr\right)
 \left[Y(s)+\nu^{-1}\int_s^t
       \exp\left(-\int_s^r[2L(q)+\nu]\,dq\right)B(r)^2\,dr\right].
 \end{aligned}
 \tag{10.15}
\]

It holds for \(s=0\) or any of the permitted energy starting times of \(u\), and all later \(t\leq T\). The \(L^2\) contribution inside the \(H^1\) norm is the source of the additional \(\nu\) in the exponent; it has not been discarded.

### Exercise 5. The localized transport coefficient

For a smooth divergence-free field \(w\) and a compactly supported smooth scalar weight \(\theta\), compute the contribution of \((w\cdot\nabla)w\) to the time derivative of
\(\frac12\int\theta^4|w|^2\).
Give a compact divergence-free field for which this contribution is nonzero.

**Solution.** The contribution on the right side of the energy equation is

\[
 \begin{aligned}
 -\int\theta^4 w\cdot(w\cdot\nabla)w\,dx
 &=-\frac12\int\theta^4 w\cdot\nabla|w|^2\,dx\\
 &=\frac12\int|w|^2w\cdot\nabla(\theta^4)\,dx\\
 &=2\int|w|^2\theta^3w\cdot\nabla\theta\,dx.
 \end{aligned}
 \tag{10.16}
\]

The last coefficient is \(2\), the product of the energy factor \(1/2\) and the derivative factor \(4\). For a regular forced solution with this weight, all terms are

\[
 \begin{aligned}
 &\frac12\frac d{dt}\int\theta^4|w|^2\,dx
       +\nu\int\theta^4|\nabla w|^2\,dx\\
 &\quad=\frac{\nu}{2}\int|w|^2\Delta(\theta^4)\,dx
       +2\int|w|^2\theta^3w\cdot\nabla\theta\,dx\\
 &\qquad+4\int p\theta^3w\cdot\nabla\theta\,dx
       +\int\theta^4w\cdot f\,dx.
 \end{aligned}
 \tag{10.17}
\]

Each term follows by the same product rules as (4.13), now without smoothing. The pressure coefficient is \(4\), while the transport coefficient is \(2\).

For a nonzero example, choose a radial, nonzero \(\theta\in C_c^\infty(B_1)\), and a cutoff \(\chi\in C_c^\infty(B_2)\) equal to one on \(B_1\). Fix a real number \(a\ne0\) and set

\[
 \psi(x)=\chi(x)(a+x_1)x_2,\qquad
 w=(\partial_2\psi,-\partial_1\psi,0).
 \tag{10.18}
\]

This field is smooth, compact and divergence free. On the support of \(\theta\) it equals
\((a+x_1,-x_2,0)\). Therefore

\[
 \begin{aligned}
 I&:=\int|w|^2\theta^3w\cdot\nabla\theta\,dx\\
 &=-\frac14\int\theta^4 w\cdot\nabla|w|^2\,dx\\
 &=-\frac12\int\theta^4[(a+x_1)^2-x_2^2]\,dx
 =-\frac{a^2}{2}\int\theta^4\,dx\ne0.
 \end{aligned}
 \tag{10.19}
\]

Radial symmetry makes the integral of \(x_1\theta^4\) vanish and the integrals of \(x_1^2\theta^4\), \(x_2^2\theta^4\) equal. Thus the coefficient can be distinguished by an actual compact finite-energy field. This field also solves the stationary forced equation with \(p=0\) and the smooth compact force \(f=(w\cdot\nabla)w-\nu\Delta w\).

**Source comparison.** In the original author TeX of [Tao, arXiv:1108.1165v4](https://arxiv.org/abs/1108.1165v4), file `local_ns.tex`, Section `energy-sec`, line 1100 prints the transport term \(X_3\) with coefficient \(4\) in front of
\(\int|u|^2u\cdot\eta^3\nabla\eta\).
Its energy definition `ert` and density identity `energy-ident` give coefficient \(2\), by (10.16). Equation (10.19) provides a nonzero compact test of the difference. This is a correction of that displayed identity; the later estimates and regularity theorems of the source are not certified by this calculation.

## 11. The connection to later lessons

The periodic and whole-space constructions now give energy-class solutions in their stated domains, with the initial data, forcing, pressure and time endpoints accounted for. The whole-space proof adds the specific spatial-tail estimate needed for its global strong limit. The comparison theorem tells us that these weak solutions agree with a regular solution for as long as the regular comparison class is available.

The next foundation is the construction and continuation of strong solutions, followed by precise regularity criteria. Those results will give more ways to decide when the regular comparison class persists. The later forced-flow and singularity constructions require their own estimates on the actual force and all its derivatives. The energy existence theorem above does not supply those estimates.

**Sources and scope of reading.** This chapter is independently written and contains its complete construction. The original author TeX of [Terence Tao, *Localisation and compactness properties of the Navier–Stokes global regularity problem*, arXiv:1108.1165v4](https://arxiv.org/abs/1108.1165v4), was consulted at Section `energy-sec`, the statements `local-energy` and `local-energy-external`, and the weak-solution discussion preceding Proposition `partial`. Those passages concern additional smooth-solution localization and regularity questions. Our approximate equation, \(H^{-1}\) force representation and exact tail bound are derived above; those source theorems are not imported. Exercise 5 records the specific displayed coefficient correction with its proof.

The definition in [Dallas Albritton, Elia Brué and Maria Colombo, *Non-uniqueness of Leray solutions of the forced Navier–Stokes equations*, arXiv:2112.03116v1](https://arxiv.org/abs/2112.03116v1), introduction, labels `eq:minimumregularity` and `eq:energyinequality`, provides a comparison with the force class used in that paper. Its stated definition uses \(L^1_tL^2_x\) forces and viscosity one. The extended theorem in Section 9 contains that force class and \(L^2_tH^{-1}_x\), with the original positive viscosity retained; (9.11) gives the exact inclusions for their common \(L^2_tL^2_x\) subclass. Their nonuniqueness construction will be treated in its assigned later lesson.

**Authorship and review.** GPT-6 Astra (OpenAI), Ultra; 9 October 2026. Author self-check only; no independent review is claimed. The independently authored mathematical text, proofs, exercises and solutions are dedicated under CC0 1.0. Cited works retain their own rights.
