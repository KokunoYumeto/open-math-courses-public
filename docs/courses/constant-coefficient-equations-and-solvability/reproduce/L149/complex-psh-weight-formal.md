# Four-condition complex weights and the topology of compact Fourier tests

*Original proof by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked; CC0.*

We prove the complete regularization of Hörmander II, Lemma 15.2.3, and then assemble the full four-condition weight and seminorm domination of Theorem 15.2.1. The exact curvature power is \((1+|\operatorname{Im}z|^2)^{-3/4}\), matching the scale \(M^{-3/2}\) in the regularization lemma.

Let \(k:\mathbb R^n\to(0,\infty)\) satisfy
\[
k(\xi+h)\le(1+C|h|)^N k(\xi),\qquad C,N>0.
\tag{VS1}
\]
Reversing the shift gives the reciprocal bound. Thus \(\ell=\log k\) is continuous and globally Lipschitz, since
\[
|\ell(\xi+h)-\ell(\xi)|\le N\log(1+C|h|)\le NC|h|.
\tag{VS2}
\]
No differentiability of the original weight is assumed.

Fix a nonnegative \(\chi\in C_c^\infty(\mathbb R^n)\), supported in the unit ball, with integral one. For \(t\ge2\), define
\[
M=M(\eta,t)=(t^2+|\eta|^2)^{1/2},\qquad
\ell_t(\xi,\eta)=\int\chi(y)\ell(\xi+My)\,dy,\qquad k_t=e^{\ell_t}.
\tag{VS3}
\]

## VS1. The exact comparisons and all positive-order derivatives

For every real shift \(h\),
\[
(1+C|h|)^{-N}\le
\frac{k_t(\xi+h,\eta)}{k_t(\xi,\eta)}
\le(1+C|h|)^N.
\tag{VS4}
\]
Indeed integrate the two bounds for the difference of logarithms in VS2 against the nonnegative probability kernel. Also
\[
|\ell_t(\xi,\eta)-\ell(\xi)|\le N\log(1+CM)\le N'\log M,
\tag{VS5}
\]
where one may take \(N'=N[1+\log(1+C)/\log2]\). Here \(M\ge2\) and
\(1+CM\le(1+C)M\le M^{1+\log(1+C)/\log2}\). Exponentiating gives
\[
M^{-N'}\le k_t(\xi,\eta)/k(\xi)\le M^{N'}.
\tag{VS6}
\]

The function \(\ell_t\) is smooth in all \(2n\) real variables, even when \(k\) is only continuous. Write its kernel in the unscaled integration variable:
\[
\ell_t(\xi,\eta)=\int R(\xi,\eta;\theta)\ell(\theta)\,d\theta,\qquad
R=M^{-n}\chi((\theta-\xi)/M).
\tag{VS7}
\]
On every compact parameter set the support in \(\theta\) is bounded. The continuous \(\ell\) is bounded there, and every kernel derivative is bounded there; differentiation under the integral is therefore valid to every order.

For a multi-index \(\alpha\) in \((\xi,\eta)\), of total order \(m\), the kernel obeys
\[
|\partial^\alpha R(\xi,\eta;\theta)|
\le A_\alpha M^{-n-m}1_{\{|\theta-\xi|\le M\}}.
\tag{VS8}
\]
Here is the derivative-scale justification. The function \(M\) is the Euclidean norm of \((\eta,t)\), so its \(\eta\)-derivatives of order \(j\) are homogeneous of degree \(1-j\) and are bounded on the unit sphere. Hence \(|\partial_\eta^\beta M|\le A_\beta M^{1-|\beta|}\). A \(\xi\)-derivative of the kernel contributes \(M^{-1}\) and a derivative of \(\chi\). An \(\eta\)-derivative of \(M^{-n}\), or of \((\theta-\xi)/M\), contributes another \(M^{-1}\), multiplied by a bounded function of \(\eta/M,t/M\) and \((\theta-\xi)/M\) on the kernel support. Induction and the finite product rule give VS8 for every \(m\). The constants depend on the derivative order, dimension and fixed kernel, not on \(t,\xi,\eta\).

For \(m\ge1\), \(\int\partial^\alpha R\,d\theta=0\), because \(\int R=1\) for every parameter. Thus, after differentiating VS7, one may subtract the constant \(\ell(\xi)\) from its integrand:
\[
\partial^\alpha\ell_t
=\int\partial^\alpha R(\xi,\eta;\theta)
                      [\ell(\theta)-\ell(\xi)]\,d\theta.
\tag{VS9}
\]
This is an algebraic subtraction after differentiation; no derivative of the nonsmooth \(\ell(\xi)\) is being taken. On the kernel support VS2 bounds the bracket by \(N\log(1+CM)\le N'\log M\). Integrating VS8 over that support therefore proves
\[
|\partial^\alpha\ell_t(\xi,\eta)|
\le D_\alpha M^{-|\alpha|}\log M,\qquad |\alpha|\ge1.
\tag{VS10}
\]
The derivative estimate is for positive order. A zero-order bound independent of \(\xi\) would be false for a nonconstant polynomially growing weight; its correct zero-order comparison is VS5.

## VS2. The radial correction and the factor \(1/18\)

Use \(z=\xi+i\eta\), \(\partial_{z_j}=(\partial_{\xi_j}-i\partial_{\eta_j})/2\). Set
\[
p_t(\eta)=t^{-1/2}M(\eta,t)-M(\eta,t)^{1/2},\qquad
\psi_t(z)=-\ell_t(\xi,\eta)+p_t(\eta).
\tag{VS11}
\]
For all sufficiently large \(t\),
\[
\sum_{j,l}w_j\overline w_l
       \partial_{z_j}\partial_{\overline z_l}\psi_t(z)
\ge\frac1{18}M(\eta,t)^{-3/2}|w|^2
\quad(w\in\mathbb C^n).
\tag{VS12}
\]

To compute the correction exactly, let \(s=t^2+|\eta|^2=M^2\) and
\[
f(s)=t^{-1/2}s^{1/2}-s^{1/4}.
\tag{VS13}
\]
Differentiation gives
\[
f'(s)=\tfrac12t^{-1/2}s^{-1/2}-\tfrac14s^{-3/4},
\qquad
f''(s)=-\tfrac14t^{-1/2}s^{-3/2}+\tfrac3{16}s^{-7/4}.
\tag{VS14}
\]
Consequently
\[
f'(s)+2sf''(s)=\tfrac18s^{-3/4},
\qquad f'(s)\ge\tfrac14s^{-3/4}\quad(s\ge t^2).
\tag{VS15}
\]
The last inequality uses \(t^{-1/2}s^{1/4}\ge1\). Because \(p_t=f(t^2+|\eta|^2)\) is independent of \(\xi\), its complex Levi form is one quarter of its real \(\eta\)-Hessian:
\[
\mathcal L_{p_t}(w)=
\tfrac12 f'(s)|w|^2+f''(s)\left|\sum_j\eta_jw_j\right|^2.
\tag{VS16}
\]
If \(f''\ge0\), VS15 gives a lower bound \(s^{-3/4}|w|^2/8\). If \(f''<0\), Cauchy–Schwarz gives
\[
\mathcal L_{p_t}(w)\ge
[\tfrac12 f'(s)+sf''(s)]|w|^2
=\tfrac1{16}s^{-3/4}|w|^2.
\tag{VS17}
\]
In the negative case replacing \(|\eta|^2\) by \(s\) decreases the lower bound, so the inequality direction is correct. Thus the \(1/16\) lower bound holds in both cases.

Every real second derivative of \(\ell_t\) is bounded by VS10. Expanding each complex second derivative into four real ones and using
\((\sum|w_j|)^2\le n|w|^2\) gives a constant \(D\), independent of \(t\), such that
\[
|\mathcal L_{\ell_t}(w)|
\le D M^{-2}\log M\,|w|^2.
\tag{VS18}
\]
Choose \(t\ge e^2\) large enough that
\[
D\frac{\log t}{\sqrt t}\le\frac1{144}.
\tag{VS19}
\]
The function \((\log r)/\sqrt r\) decreases for \(r\ge e^2\); since \(M\ge t\), the same bound holds with \(M\) in place of \(t\). Therefore VS17–VS18 yield
\[
\mathcal L_{\psi_t}(w)\ge
\left(\frac1{16}-\frac1{144}\right)M^{-3/2}|w|^2
=\frac1{18}M^{-3/2}|w|^2.
\tag{VS20}
\]
This proves VS12 and strict plurisubharmonicity in every complex direction. It proves the factor \(1/18\), not merely an unspecified positive constant. VS4, VS6 and VS10 are the three regularization estimates used in the source lemma. No convolution of \(k\) itself, evenness assumption, or derivative of the unsmoothed logarithm has been substituted.

![Exact correction curvature and a stabilized finite maximum.](figures/curvature-and-stabilized-maxima.png)

The left panel shows the exact normalized radial correction and the margin used in VS20. The right panel shows three nested-support seeds with the learner example's parameters and an analytically stabilized strip. The final weight is constructed by continuing the exhaustion below.

## PW1. Compact-support stages and their topology

Use the negative-exponential Fourier transform and bilinear pairing in [the complex-estimate lesson](../../AN02-L148.html). Write \(B_{2,k}\) with the squared norm \((2\pi)^{-n}\int k^2|\widehat u|^2\). Let \(X\subset\mathbb R^n\) be nonempty, open and convex.

Choose nonempty compact convex sets \(K_j\Subset X\), with \(K_j\subset\operatorname{int}K_{j+1}\), whose interiors cover \(X\). Such a sequence exists explicitly. Fix \(x_0\in X\). For all sufficiently large integers \(m\), the sets
\[
K(m)=\{x:|x-x_0|\le m,\ 
               \operatorname{dist}(x,\mathbb R^n\setminus X)\ge1/m\}
\tag{PW1}
\]
are nonempty, closed, bounded and convex. The distance condition is convex because it says \(x+B(0,1/m)\subset X\); convex combinations preserve these ball inclusions. The distance function is continuous, proving closedness. If \(X=\mathbb R^n\), interpret the distance as infinite and use the closed balls. Increasing \(m\) strictly increases both margins, so \(K(m)\subset\operatorname{int}K(m+1)\). These sets cover \(X\); reindexing them supplies the sequence.

Set
\[
E_j=\mathcal E'(K_j)\cap B_{2,k},\qquad
E=\bigcup_jE_j=\mathcal B_{2,k}^{\,c}(X).
\tag{PW2}
\]
Each \(E_j\), with the inherited weighted norm, is Banach. A norm limit converges in \(\mathcal S'\) by the weighted inclusion proved in CF1. Testing outside \(K_j\) shows that the limiting support remains in \(K_j\); hence \(E_j\) is a closed subspace of the weighted Hilbert space.

Give \(E\) the finest locally convex topology making all inclusions \(E_j\to E\) continuous. Concretely it is generated by all seminorms whose restrictions to every \(E_j\) are norm-continuous. This description makes the inclusions continuous, and any locally convex topology with that property has only such continuous seminorms, proving the stated maximal property. Consequently a seminorm \(q\) on \(E\) is continuous exactly when
\[
q(u)\le Q_j\|u\|_{2,k}\quad(u\in E_j)
\tag{PW3}
\]
for a finite constant on each stage. Necessity is continuity of the restriction and homogeneity; sufficiency is the displayed description of the topology. Cofinality of the compact exhaustion shows that using all compact support sets instead gives the same topology.

The locally finite partition description of this topology can also be proved explicitly. Choose \(0\le\theta_j\le1\), smooth, supported in \(\operatorname{int}K_{j+1}\), and equal to one near \(K_j\). Put \(\chi_1=\theta_1\) and
\(\chi_j=\theta_j\prod_{l<j}(1-\theta_l)\) for \(j\ge2\). The partial sum is \(1-\prod_{l\le j}(1-\theta_l)\). Every compact subset lies in a region where some \(\theta_J=1\), so all later \(\chi_j\) vanish on a neighborhood of it. Thus this is a locally finite smooth compact-support partition of unity on \(X\).

For any such partition and positive constants \(a_j\), the seminorm
\[
Q_a(u)=\sum_j a_j\|\chi_j u\|_{2,k}
\tag{PW3a}
\]
is finite on every compact test. On \(E_i\) only finitely many supports meet \(K_i\), and the multiplier bound CF6 proves \(Q_a(u)\le D_i\|u\|_{2,k}\), hence continuity by PW3. Conversely, for a continuous \(q\), choose a compact stage containing each \(\operatorname{supp}\chi_j\), and choose \(a_j>0\) at least its PW3 constant. The finite partition identity on the support of \(u\) and the seminorm triangle inequality give \(q(u)\le Q_a(u)\). These partition seminorms therefore generate the same inductive topology. This supplies the full partition argument in the source's introductory passage.

## PW2. The exact four-condition theorem

**Theorem PW2.** For every continuous seminorm \(q\) on \(E\), there is a finite real, locally Lipschitz function \(\phi\) on \(\mathbb C^n\) such that
\[
q(u)\le P_\phi(u):=
\left(\int_{\mathbb C^n}|F_u(z)|^2e^{-2\phi(z)}\,dV(z)\right)^{1/2}
\quad(u\in E),
\tag{PW4}
\]
and all four following conditions hold:

1. For every nonempty compact convex \(K\Subset X\),
\[
e^{-\phi(\xi+i\eta)}\le C_K e^{-H_K(\eta)}k(\xi).
\tag{PW5}
\]
2. For every \(A>0\),
\[
k(\xi)\le C_A e^{-\phi(\xi+i\eta)}\quad(|\eta|<A).
\tag{PW6}
\]
3. For a single constant \(C_0\),
\[
|\nabla\phi(\xi+i\eta)|\le C_0+\log(1+|\eta|)
\quad\text{almost everywhere}.
\tag{PW7}
\]
4. For a single \(c>0\), its complex Hessian satisfies
\[
\mathcal L_\phi(w)\ge c(1+|\eta|^2)^{-3/4}|w|^2
\quad(w\in\mathbb C^n)
\tag{PW8}
\]
in the distribution sense. In particular \(\phi\) is plurisubharmonic.

Moreover \(P_\phi\) is finite and continuous on \(E\). Its restriction to each fixed compact-support stage is equivalent to the weighted real norm. We prove the construction and all of these conclusions.

## PW3. Supporting-function seeds

Choose \(t_j\ge2\) large enough for VS12 and so that
\[
2t_j^{-1/2}<\operatorname{dist}
       (K_j,\mathbb R^n\setminus\operatorname{int}K_{j+1}).
\tag{PW9}
\]
The distance is positive by compactness and strict interior inclusion. We may increase the \(t_j\) so they are nondecreasing. Put
\[
\psi_j(\xi+i\eta)=H_{K_j}(\eta)-\ell_{t_j}(\xi,\eta)
                    +p_{t_j}(\eta).
\tag{PW10}
\]
The supporting function is convex and has Lipschitz constant
\(R_j=\sup_{x\in K_j}|x|\). As a function of \(\eta\) alone it has nonnegative distributional complex Hessian: smooth it by nonnegative real convolutions, which preserve convexity, and use the positive real Hessian of each smooth convex function divided by four. Local uniform convergence passes this positivity to its distributional derivatives. Thus VS12 gives
\[
\mathcal L_{\psi_j}(w)\ge
\tfrac1{18}(t_j^2+|\eta|^2)^{-3/4}|w|^2.
\tag{PW11}
\]
These seeds are locally Lipschitz. VS10 bounds the gradient of their smooth logarithmic part by \(D\log M/M\), uniformly in \(\xi\); differentiating \(p_t\) bounds its gradient by \(t^{-1/2}\). Therefore each seed has a finite global Lipschitz constant \(L_j\).

For every fixed strip, \(\psi_j+\log k\) has uniform upper and lower bounds, independent of \(\xi\), by VS5 and the boundedness of \(H_{K_j}\) and \(p_{t_j}\) on that strip. It also has a global lower bound: the scalar expression
\[
t_j^{-1/2}M-M^{1/2}-N'\log M,\qquad M\ge t_j,
\tag{PW12}
\]
is bounded below, because it is continuous and tends to infinity. Hence
\(\psi_j\ge H_{K_j}-\log k-D_j\).

There is also a useful global upper bound. VS5 gives
\[
\psi_j\le H_{K_j}(\eta)-\log k(\xi)
               +2t_j^{-1/2}|\eta|+D'_j
\le H_{K_{j+1}}(\eta)-\log k(\xi)+D'_j.
\tag{PW13}
\]
For the first inequality use \(M\le t_j+|\eta|\) and the fact that
\(N'\log M-\sqrt M\) is bounded above on \([t_j,\infty)\). This even gives the smaller coefficient \(t_j^{-1/2}\); the written coefficient two is convenient for PW9. The second inequality follows from
\(K_j+2t_j^{-1/2}\overline B\subset K_{j+1}\).

## PW4. A maximum preserves the variable Hessian lower bound

We will use the following local fact. If finite locally Lipschitz functions \(f,g\) both satisfy
\(\mathcal L_f,\mathcal L_g\ge a(z)I\) on an open set, where \(a>0\) is continuous, then their maximum does too.

On a ball \(B\) take \(b=\inf_B a\). The functions
\(f-b|z|^2\) and \(g-b|z|^2\) have nonnegative distributional complex Hessian. Smoothing shows that such a continuous function is plurisubharmonic: the smoothed Hessian is positive on interior balls, giving the line submean inequality, and local uniform convergence passes that inequality to the function. The maximum of two finite plurisubharmonic functions is plurisubharmonic: choose a function attaining the maximum at the center of each line circle, apply its submean, then bound it by the maximum on the circle. This maximum is continuous. Smoothing it now shows its complex Hessian is positive distributionally. Thus
\[
\mathcal L_{\max(f,g)}\ge bI\quad\text{on }B.
\tag{PW14}
\]
To recover the variable \(a\), let a nonnegative smooth test have compact support. Cover that support by finitely many sufficiently small balls on which the oscillation of \(a\) is below \(\varepsilon\), and split the test with a smooth nonnegative partition of unity. Apply PW14 to each summand in any fixed complex direction \(w\). Their sum gives the lower bound \((a-\varepsilon)|w|^2\) against the original test. Let \(\varepsilon\downarrow0\). This proves the claim. Finite maxima also preserve a common local Lipschitz bound, by the elementary inequality
\(|\max f_j(x)-\max f_j(y)|\le\max_j|f_j(x)-f_j(y)|\).
In particular, interpret gradients in the weak sense. If all their almost-everywhere gradient bounds are the same continuous function \(G(z)\), smooth them on an interior ball. Their smooth gradients are bounded by the supremum of \(G\) on a slightly larger ball; passing to the uniform limit gives that common Lipschitz constant there. The maximum has the same bound. A Lipschitz constant \(L\) gives weak directional derivatives bounded by \(L\): bounded difference quotients, tested against a compact smooth function and passed to the distributional limit, give a functional bounded by \(L\) times its \(L^1\) norm. The complete \(L^1\) duality in L043 represents it by an \(L^\infty\) function. Testing a countable dense set of real unit directions shows that the norm of the weak gradient is at most \(L\) almost everywhere. Apply this on shrinking balls from a countable base; continuity of \(G\) gives \(|\nabla\max f_j|\le G\) almost everywhere. Thus the variable gradient bound used below is preserved without assuming pointwise differentiability on a prescribed exceptional set.

## PW5. Vertical constants and local stabilization

Set
\[
\phi_j=\max_{1\le l\le j}(\psi_l-G_l),\qquad
\alpha_j=\frac j{j+1}.
\tag{PW15}
\]
We will choose increasing \(G_j\to\infty\) and increasing \(A_j\to\infty\) so that
\[
\phi_{j+1}=\phi_j\quad(|\eta|<A_j),
\qquad
q(u)\le\alpha_j
\left(\int_{|\eta|<A_j}|F_u(\xi+i\eta)|^2e^{-2\phi_j}\,d\xi d\eta\right)^{1/2}
\quad(u\in E_{j+3}).
\tag{PW16}
\]
Call the square-root integral \(P_j(u)\).

The curvature and gradient choices can be made independently of \(G_j\). The first seed obeys PW7 globally for a finite \(C_0\), and
\(\mathcal L_{\psi_1}\ge c(1+|\eta|^2)^{-3/4}I\) with
\[
c=\tfrac1{18}\min(t_1^{-3/2},2^{-3/4}).
\tag{PW17}
\]
For \(j\ge2\), choose increasing \(B_j\ge\max(t_j,j)\) so large that
\(|\nabla\psi_j|\le\log(1+|\eta|)\) for \(|\eta|>B_j\). This follows already from its finite \(L_j\). On that region PW11 and
\(t_j^2+|\eta|^2\le2|\eta|^2\le2(1+|\eta|^2)\)
give the curvature bound with the same \(c\).

Choose \(G_j\) large enough that
\[
\psi_j-G_j<\psi_1-G_1
\quad\text{for }|\eta|\le B_j+1.
\tag{PW18}
\]
This is possible uniformly in \(\xi\), by the strip comparisons in PW3. When \(G_1,\ldots,G_{j-1},A_{j-1}\) have been chosen, require the same strict inequality also on \(|\eta|\le A_{j-1}\), and require \(G_j\ge G_{j-1}+1\). Thus the new branch is inactive on that strip, proving the first condition of PW16. Where it may be active, \(|\eta|>B_j\), both the preceding maximum and the new branch have the common curvature and gradient bounds. PW4, applied on this open region, preserves curvature; the common Lipschitz bound preserves the gradient inequality. On \(|\eta|<B_j+1\) the maximum is unchanged. The two open regions cover the whole space. Induction proves PW7–PW8 uniformly for every \(\phi_j\).

For any fixed strip, all sufficiently late branches are inactive there because \(B_j\to\infty\). Hence \(\phi_j\) stabilizes there to a finite maximum, uniformly in \(\xi\). Its pointwise increasing limit \(\phi\) is therefore finite and locally Lipschitz, with the same gradient and distributional curvature bounds. After the \(A_j\) are chosen below, the first part of PW16 gives the stronger exact identity
\[
\phi=\phi_j\quad(|\eta|<A_j).
\tag{PW19}
\]

## PW6. The initial seminorm estimate

Take \(A_1=1\). On this strip PW3 gives \(\psi_1+\log k\le D\), so
\[
P_1(u)^2\ge e^{2G_1-2D}
       \int_{|\eta|<1}|F_u(\xi+i\eta)|^2k(\xi)^2\,d\xi d\eta
\ge C_k^{-1}e^{2G_1-2D}\|u\|_{2,k}^2.
\tag{PW20}
\]
The last inequality is exactly CF22, for any compact \(u\). By PW3, \(q(u)\le Q_4\|u\|_{2,k}\) on \(E_4\). Choose \(G_1\) so large that
\(\alpha_1C_k^{-1/2}e^{G_1-D}\ge Q_4\).
Then the second part of PW16 holds for \(j=1\). Increasing \(G_1\) affects none of the derivative bounds.

## PW7. A finite partition with separated exterior supports

Suppose PW16 holds at level \(j\), and choose \(G_{j+1}\) as in PW5. We need a partition equal to one near \(K_{j+4}\) with
\[
\operatorname{supp}\chi_0\subset\operatorname{int}K_{j+3},
\qquad
\operatorname{supp}\chi_\nu\subset C_\nu,\ \nu\ge1,
\tag{PW21}
\]
where each \(C_\nu\) is a compact convex ball strictly separated from \(K_{j+2}\).

Choose a nonnegative central cutoff supported in \(\operatorname{int}K_{j+3}\), equal to one near \(K_{j+2}\). The remaining compact portion of \(K_{j+4}\) is outside a neighborhood of \(K_{j+2}\). Each of its points has a small ball in \(X\) whose closure is strictly separated from \(K_{j+2}\). To see the separation, minimize its distance to the compact convex set. If \(y\) is a nearest point and \(x\) the exterior center, differentiating distance along every segment in \(K_{j+2}\) gives
\((x-y)\cdot(z-y)\le0\) for all \(z\) in that set. Thus the direction \((x-y)/|x-y|\) separates the center with a positive gap; a sufficiently small ball retains the gap.

Take a finite such ball cover and smooth nonnegative cutoffs in those balls. Their sum with the central cutoff is positive on a neighborhood of \(K_{j+4}\). Divide each by that sum and multiply them all by one compact smooth cutoff equal to one near \(K_{j+4}\) and supported where the denominator is positive. This supplies a finite smooth partition with PW21. The central member still has central support, and the other members have their separated convex supports. In particular the convex hulls of the exterior supports remain separated; merely being outside the set would not have sufficed.

For \(u\in E_{j+4}\), \(u=\sum_{\nu=0}^r\chi_\nu u\), and \(\chi_0u\in E_{j+3}\). Apply the preceding seminorm estimate to this central piece and PW3 to all exterior pieces. Since
\(F_{\chi_0u}=F_u-\sum_{\nu\ge1}F_{\chi_\nu u}\),
the triangle inequality for the strip integral gives
\[
q(u)\le\alpha_jP_j(u)+D_j\sum_{\nu=1}^r\|\chi_\nu u\|_{2,k}.
\tag{PW22}
\]
Here \(D_j<\infty\). To justify the extra integral terms explicitly, on \(|\eta|<A_j\) PW3 gives \(e^{-\phi_j}\le D_{j,A_j}k(\xi)\). The plane estimate CF18, applied to each fixed compact \(C_\nu\), bounds the strip integral of \(F_{\chi_\nu u}\) by a finite constant times \(\|\chi_\nu u\|_{2,k}\). These constants and the fixed \(Q_{j+4}\) are absorbed into \(D_j\). There is no bound uniform over all stages being assumed.

## PW8. Exponential control of the exterior pieces

PW13, for the finitely many branches through \(j+1\), gives
\[
\phi_{j+1}(\xi+i\eta)
\le H_{K_{j+2}}(\eta)-\log k(\xi)+D'_{j+1}.
\tag{PW23}
\]
For an exterior cutoff write \(h_\nu=H_{C_\nu}\). CF20, whose cutoff operation is multiplication, and PW23 imply
\[
\|\chi_\nu u\|_{2,k}^2
\le D_\nu e^{2[h_\nu(-\eta)+H_{K_{j+2}}(\eta)]}
\int|F_u(\xi+i\eta)|^2e^{-2\phi_{j+1}(\xi+i\eta)}\,d\xi.
\tag{PW24}
\]
Strict separation provides a unit vector \(\theta_\nu\) and \(d_\nu>0\) with
\[
h_\nu(-\theta_\nu)+H_{K_{j+2}}(\theta_\nu)\le-d_\nu.
\tag{PW25}
\]
Both supporting functions are Lipschitz. For \(|\eta-R\theta_\nu|<1\), homogeneity and those Lipschitz bounds give
\[
h_\nu(-\eta)+H_{K_{j+2}}(\eta)
\le-d_\nu R+D''_\nu.
\tag{PW26}
\]
Choose \(A>1\) and set \(R=A-1\). The real \(n\)-dimensional unit ball about \(R\theta_\nu\) lies inside \(|\eta|<A\). Integrate PW24 over it, using its volume \(b_n\), to obtain
\[
\|\chi_\nu u\|_{2,k}
\le D'''_\nu e^{-d_\nu A}
\left(\int_{|\eta|<A}|F_u(\xi+i\eta)|^2e^{-2\phi_{j+1}}\,d\xi d\eta\right)^{1/2}.
\tag{PW27}
\]
![Separated supports and the coefficient in an imaginary-plane estimate.](figures/exterior-supports-and-imaginary-shifts.png)

The real intervals give an exact negative support-function gap in the positive imaginary direction. The model energy can grow while the coefficient becomes small; the induction controls its square-root integral over an enlarging strip. The learner companion computes all of the displayed curves.

The constants do not depend on \(A\) or \(u\). Choose \(A_{j+1}>A_j+1\) so large that
\[
D_j\sum_{\nu=1}^rD'''_\nu e^{-d_\nu A_{j+1}}
\le\alpha_{j+1}-\alpha_j=\frac1{(j+1)(j+2)}.
\tag{PW28}
\]
On the old strip \(\phi_{j+1}=\phi_j\), so \(P_j(u)\le P_{j+1}(u)\). PW22, PW27 and PW28 prove the second part of PW16 at level \(j+1\). If there are no exterior pieces, their sum is zero and any sufficiently large increasing \(A_{j+1}\) works. This completes the induction without a circular choice: the new vertical constant and weight are fixed before choosing the new strip radius.

## PW9. All four conditions and the limit inequality

The construction in PW5 already proves PW7–PW8. PW19 and the finite-strip upper comparison of each seed give a bound for \(\phi+\log k\) on every strip, proving PW6. For a compact convex \(K\Subset X\), choose \(j\) with \(K\subset K_j\). The lower comparison in PW3 gives
\[
\phi\ge\psi_j-G_j\ge H_{K_j}(\eta)-\log k(\xi)-D_j-G_j
\ge H_K(\eta)-\log k(\xi)-D_j-G_j.
\tag{PW29}
\]
Exponentiation proves PW5.

For fixed \(u\in E\), it belongs to \(E_{j+3}\) for every sufficiently large \(j\). By PW19,
\[
P_j(u)^2=\int_{|\eta|<A_j}|F_u(\xi+i\eta)|^2e^{-2\phi(\xi+i\eta)}\,d\xi d\eta.
\tag{PW30}
\]
These integrals increase as their domains increase. Monotone convergence, \(A_j\to\infty\) and \(\alpha_j\to1\) pass PW16 to PW4. Stabilization is what permits PW30; one must not incorrectly assert that arbitrary expanding domains with changing decreasing weights have monotone integrals.

## PW10. Finiteness, continuity and equivalence on stages

For any fixed compact support set \(S\Subset X\), its convex hull \(K\) is compact inside \(X\), by the finite-combination proof CF9. Enlarge it to \(L=K+\rho\overline B\Subset X\). PW5 then gives
\[
e^{-2\phi(\xi+i\eta)}
\le C_L^2e^{-2H_K(\eta)}e^{-2\rho|\eta|}k(\xi)^2.
\tag{PW31}
\]
The exponential factor absorbs the polynomial damper in CF17:
\(\sup_{r\ge0}e^{-2\rho r}(1+r^2)^{N+2n}<\infty\).
Consequently
\[
P_\phi(u)\le D_S\|u\|_{2,k}\quad
(\operatorname{supp}u\subset S).
\tag{PW32}
\]
This proves finiteness and continuity on every stage, hence on \(E\) by PW3. Conversely PW6 for \(A=1\) and CF22 give
\[
\|u\|_{2,k}^2
\le C_k C_1^2\int_{|\eta|<1}|F_u|^2e^{-2\phi}\,d\xi d\eta
\le C_k C_1^2P_\phi(u)^2.
\tag{PW33}
\]
Thus the norms are equivalent on each fixed support stage. PW4 and PW5–PW8 prove the entire source theorem. No assertion that a single real-weight norm describes the full inductive topology is made. If \(X\) is empty, its compact-test space is zero. Taking \(\phi=\psi_t\) from VS11 for large \(t\) gives finite-strip comparison, a globally bounded gradient and the curvature lower bound \(c_t(1+|\eta|^2)^{-3/4}\), with \(c_t=t^{-3/2}/18\). The compact growth condition is vacuous, and the zero seminorm inequality is immediate. This includes that endpoint. \(\square\)

## PW11. The consequent weak representation

The construction also proves the ensuing representation statement for continuous complex-linear forms on the \(p=2\) compact-test space. Apply PW2 with \(q(u)=|L(u)|\), and map \(u\) to \(F_u e^{-\phi}\) in \(L^2(\mathbb C^n)\). PW4 makes \(L\) a well-defined bounded linear form of norm at most one on that image: if the image is zero then PW4 makes \(L(u)=0\). Extend it by continuity to the closed image subspace, which is Hilbert. The full Hilbert representation in [L043 Lemma 1.1](../../AN02-L043.html) applies to that closed subspace and gives \(g\in L^2(\mathbb C^n)\), with \(\|g\|_2\le1\), such that
\[
L(u)=\int F_u(z)e^{-\phi(z)}\overline{g(z)}\,dV(z).
\tag{PW34}
\]
Define \(V(z)=e^{-\phi(-z)}\overline{g(-z)}\). Reflection preserves complex volume, so
\[
\int|V(z)|^2e^{2\phi(-z)}\,dV(z)\le1,\qquad
L(u)=\int V(z)F_u(-z)\,dV(z).
\tag{PW35}
\]
Cauchy–Schwarz proves absolute convergence. The converse and the unique local distribution represented by this integral are the complete theorem CF7–CF11 in L148, with Lebesgue unit-ball mass \(b_{2n}\).

For precision the local bilinear dual identification also follows directly. A continuous form \(L\) on \(E\) restricts, for any compact smooth \(\chi\), to the bounded form \(h\mapsto L(\chi h)\) on \(B_{2,k}\), using PW3 on its fixed support and the multiplier CF6. Its representing global distribution lies in \(B_{2,1/\check k}\) by CF8. On ordinary compact smooth tests these distributions define a single distribution \(v\) by \(L\); distribution continuity follows from the finite smooth seminorm bound CF41. Their actions are \(\chi v\), proving its local membership. Conversely any such \(v\) acts continuously on each \(E_j\) by its cutoff global dual norm and the canonical compact pairing CF42–CF43, hence on \(E\). Therefore the continuous complex-linear forms are exactly the local reflected weighted distributions. This is the full continuous-dual identification in the source's introductory passage.

## Source scope and remaining course obligations

VS1–VS20 give the complete H-II Lemma 15.2.3 regularization, shift estimates, positive-order derivative bounds and exact \(1/18\) Levi constant. PW1–PW33 give the complete H-II Theorem 15.2.1, including its compact-support topology, all four conditions, uniform distributional curvature, exterior-piece induction and seminorm domination. PW34–PW35 supply the subsequent \(p=2\) weak representation with all reflections visible.

The lemma's \(M^{-3/2}\) has exactly the theorem's \((1+|\eta|^2)^{-3/4}\) scale at large imaginary frequency. This curvature decays more slowly than the second-derivative errors of order \(M^{-2}\log M\), allowing those errors to be absorbed. The following representation and division arguments use this precise comparison.

Source: Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.2, Theorem 15.2.1 and Lemma 15.2.3, printed pp. 279–285; 1983 edition, second revised printing 1990, reprint 2005. Original arguments with ordinary attribution are given here; no protected page or image belongs to the public packet.
