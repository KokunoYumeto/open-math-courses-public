# Forces, energy and vorticity in incompressible flow

*Written by GPT-6 Astra (OpenAI) at Ultra, October 2026. Self-checked by GPT-6 Astra; no independent review of this version is claimed. Mathematical text dedicated to the public domain under CC0.*

A force can add energy to a fluid, remove energy, or change its rotation. These effects are related, but they are not identical. The energy identity measures the work done by a force. The vorticity equation measures the rotation created by its curl. A pressure gradient can redistribute momentum without contributing to either total work or curl in the setting considered here.

This lesson derives those statements from the incompressible equations. It also shows exactly how velocity, pressure, viscosity and force change when space and time are rescaled. The scalar coupled to a Boussinesq fluid has its own scale factor, which must be kept when comparing the two systems.

We assume multivariable differentiation, integration, the product rule, integration by parts and the Cauchy–Schwarz inequality. All fields in the proofs are smooth. We state the support assumptions needed for each spatial integral, so no theorem about weak solutions or existence of a flow is being used. Basic references for the coupled two-dimensional equations are Li [L], Chae–Miao–Xue [CMX] and Ju [J]. Every fluid calculation used in this lesson is supplied below.

## 1. The equations and their data

Let \(n\geq2\), let \(\nu>0\), and let \(0<T<\infty\). For \(x\in\mathbb R^n\) and \(0\leq t<T\), the velocity is a vector
\[
u(x,t)=(u_1(x,t),\ldots,u_n(x,t)).
\]
The pressure \(p(x,t)\) is a scalar. The external force \(f(x,t)\) is a vector. We use the equations
\[
\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u=f,
\qquad
\operatorname{div}u=0.                                      \tag{1.1}
\]
Their component form is
\[
\partial_tu_i+\sum_{j=1}^n u_j\partial_ju_i+\partial_ip
-\nu\sum_{j=1}^n\partial_j^2u_i=f_i,
\qquad
\sum_{i=1}^n\partial_i u_i=0.                                \tag{1.2}
\]
The initial condition is \(u(x,0)=u_0(x)\). A classical solution means that the required derivatives exist continuously and these equations hold pointwise. In this lesson all fields have as many derivatives as the calculation needs.

The constant \(\nu\) is the physical viscosity. It is present in every equation below. We do not change it by a choice of units without recording the change.

The pressure is unchanged as a physical gradient when we replace it by
\[
\widehat p(x,t)=p(x,t)+c(t),
\]
where \(c\) depends only on time. This follows from \(\nabla_xc(t)=0\). A spatially varying addition behaves differently: if \(\widehat p=p+\phi(x,t)\), the same velocity solves (1.1) with force \(\widehat f=f+\nabla\phi\). Thus the velocity alone does not determine a unique pair consisting of pressure and force.

### Smoothness before and at an endpoint

Saying that a force is smooth for \(t<T\) says nothing by itself about its behavior as \(t\) approaches \(T\). For example, let \(\varphi\) be a nonzero smooth function of compact support and set
\[
f(x,t)=\frac{\varphi(x)}{T-t}e_1.
\]
This force is smooth at every point with \(t<T\), but its supremum diverges as \(t\uparrow T\).

For a precise stronger condition, suppose \(f\) is the restriction of a smooth function on an open neighborhood of \(\mathbb R^n\times[0,T]\), and suppose one compact set \(K\subset\mathbb R^n\) contains its spatial support for every \(t\in[0,T]\). Each mixed derivative then has a finite bound:
\[
\sup_{x\in\mathbb R^n,\ 0\leq t\leq T}
|\partial_x^\gamma\partial_t^b f(x,t)|<\infty.                \tag{1.3}
\]
Indeed the derivative is zero outside \(K\), and its absolute value is a continuous function on the compact set \(K\times[0,T]\). This applies to each particular derivative. It does not assert one bound shared by all derivative orders.

For finite \(p\geq1\), the same support gives
\[
\|f(t)\|_{L^p(\mathbb R^n)}
\leq |K|^{1/p}\|f(t)\|_{L^\infty(\mathbb R^n)}.
\]
This follows by bounding the integral of \(|f|^p\) over \(K\). Endpoint regularity and a common spatial support therefore control both spatial supremum norms and finite spatial integral norms. They are substantive conditions in a forced singularity problem.

## 2. Pressure and incompressibility

Taking a divergence in (1.1) gives an equation for the pressure.

**Proposition 2.1.** Every smooth solution of (1.1) satisfies
\[
\Delta p
=\operatorname{div}f
-\sum_{i,j=1}^n(\partial_i u_j)(\partial_j u_i).               \tag{2.1}
\]

**Proof.** The divergence of \(\partial_tu\) and of \(\Delta u\) is zero because spatial differentiation commutes with time differentiation and the Laplacian. For advection,
\[
\begin{aligned}
\sum_i\partial_i\!\left(\sum_j u_j\partial_j u_i\right)
&=\sum_{i,j}(\partial_i u_j)(\partial_j u_i)
 +\sum_j u_j\partial_j\!\left(\sum_i\partial_i u_i\right)\\
&=\sum_{i,j}(\partial_i u_j)(\partial_j u_i).
\end{aligned}
\]
Substituting this into the divergence of (1.1) proves (2.1). \(\square\)

Equation (2.1) is a necessary consequence of the full momentum equation. Solving it alone does not prove that all components of (1.1) hold. The momentum equation must still be checked.

One can also run the calculation in the other direction without solving an existence problem. Choose a smooth divergence-free velocity \(u\) and a smooth pressure \(p\), and define
\[
f=\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u.            \tag{2.2}
\]
Then (1.1) holds by substitution. The mathematical work in a prescribed-force problem is to obtain the required properties of \(u,p,f\) simultaneously. Formula (2.2) does not show that the resulting force is small, compactly supported, or smooth at a missing time endpoint.

## 3. The exact energy balance

Fix \(t_*<T\). Suppose the velocity and all the derivatives used below are smooth on \([0,t_*]\), with velocity supported in one compact spatial set on this interval. The pressure may extend outside that set. Products containing \(u\), including \(pu\), are still compactly supported, so their divergence integrals vanish.

Write
\[
\|u(t)\|_2^2=\int_{\mathbb R^n}|u(x,t)|^2\,dx,\qquad
\|\nabla u(t)\|_2^2
=\sum_{i,j=1}^n\int_{\mathbb R^n}|\partial_j u_i(x,t)|^2\,dx.
\]

**Theorem 3.1.** Under these assumptions,
\[
\frac12\frac{d}{dt}\|u(t)\|_2^2
+\nu\|\nabla u(t)\|_2^2
=\int_{\mathbb R^n}u(x,t)\cdot f(x,t)\,dx.                   \tag{3.1}
\]
Consequently, for \(0\leq t\leq t_*\),
\[
\frac12\|u(t)\|_2^2
+\nu\int_0^t\|\nabla u(s)\|_2^2\,ds
=\frac12\|u_0\|_2^2+\int_0^t\!\int_{\mathbb R^n}u\cdot f\,dx\,ds.
                                                                    \tag{3.2}
\]

**Proof.** Multiply component \(i\) of (1.2) by \(u_i\), sum over \(i\), and integrate. The time term is \(\frac12\frac{d}{dt}\|u\|_2^2\). The transport term is
\[
\begin{aligned}
\sum_{i,j}\int u_i u_j\partial_j u_i
&=\int u\cdot\nabla\left(\frac{|u|^2}{2}\right)\\
&=\int\operatorname{div}\left(\frac{|u|^2}{2}u\right)
 -\int\frac{|u|^2}{2}\operatorname{div}u=0.
\end{aligned}
\]
The pressure term is
\[
\int u\cdot\nabla p=\int\operatorname{div}(pu)-\int p\operatorname{div}u=0.
\]
For each \(i,j\), integration by parts gives
\[
-\nu\int u_i\partial_j^2u_i=\nu\int|\partial_j u_i|^2.
\]
The force term remains \(\int u\cdot f\). This proves (3.1); integration in time proves (3.2). \(\square\)

**Corollary 3.2.** If in addition \(\int_0^{t_*}\|f(s)\|_2\,ds<\infty\), the same solution obeys
\[
\|u(t)\|_2\leq\|u_0\|_2+\int_0^t\|f(s)\|_2\,ds.              \tag{3.3}
\]

**Proof.** Cauchy–Schwarz in (3.1) yields
\[
\frac12\frac{d}{dt}\|u\|_2^2
\leq\|u\|_2\|f\|_2.
\]
To include times when \(u=0\), set \(E_\varepsilon=(\|u\|_2^2+\varepsilon^2)^{1/2}\). Direct differentiation gives
\[
E_\varepsilon'
\leq\frac{\|u\|_2}{(\|u\|_2^2+\varepsilon^2)^{1/2}}\|f\|_2
\leq\|f\|_2.
\]
Integrate and let \(\varepsilon\downarrow0\). \(\square\)

In particular, zero initial velocity and zero force imply \(u=0\) for every time in this class. Conversely, a smooth compact pulse that starts from rest must receive a nonzero force somewhere. The identity quantifies how the force does work.

These calculations also hold on a rectangular periodic cell when all fields are periodic with its side lengths: every boundary contribution on one face cancels the contribution on its opposite face. The same constants remain. On a bounded physical domain the boundary terms require their own calculation.

## 4. How force creates rotation

In three dimensions define
\[
\omega=\nabla\times u
=(\partial_2u_3-\partial_3u_2,\ 
  \partial_3u_1-\partial_1u_3,\ 
  \partial_1u_2-\partial_2u_1).
\]

**Theorem 4.1.** The vorticity satisfies
\[
\partial_t\omega+(u\cdot\nabla)\omega
-(\omega\cdot\nabla)u-\nu\Delta\omega=\nabla\times f.          \tag{4.1}
\]

**Proof.** Let \(\epsilon_{ijk}\) be the alternating symbol, equal to \(1\) on cyclic permutations of \(123\), equal to \(-1\) on anticyclic permutations, and zero when indices repeat. Summation in this proof is over \(1,2,3\).

The contraction identity
\[
\sum_k\epsilon_{ijk}\epsilon_{kab}
=\delta_{ia}\delta_{jb}-\delta_{ib}\delta_{ja}
\]
follows by inspecting the nonzero permutations. Thus
\[
(u\times\omega)_i
=\sum_j u_j\partial_i u_j-\sum_j u_j\partial_j u_i
=\partial_i(|u|^2/2)-((u\cdot\nabla)u)_i.
\]
For any smooth vector fields \(a,b\), the same contraction and product rule give
\[
\begin{aligned}
(\nabla\times(a\times b))_i
&=\sum_j\partial_j(a_i b_j-a_j b_i)\\
&=((b\cdot\nabla)a)_i-((a\cdot\nabla)b)_i
 +a_i\operatorname{div}b-b_i\operatorname{div}a.
\end{aligned}
\]
The divergence of a curl is zero, since every mixed derivative occurs with the opposite sign of its exchanged pair. Therefore \(\operatorname{div}\omega=0\). Together with \(\operatorname{div}u=0\), the two displayed identities imply
\[
\nabla\times((u\cdot\nabla)u)
=(u\cdot\nabla)\omega-(\omega\cdot\nabla)u.
\]
Curl of \(\nabla p\) is zero by equality of mixed derivatives. Curl commutes with \(\partial_t\) and \(\Delta\). Taking curl of (1.1) now gives (4.1). \(\square\)

The term \((\omega\cdot\nabla)u\) is vortex stretching: it differentiates velocity in the direction of vorticity. It is a vector, not merely the size of the vorticity.

For an exact two-dimensional comparison, embed \(v=(v_1,v_2)\) as \(u=(v_1,v_2,0)\), independent of \(x_3\). Its three-dimensional curl is \((0,0,w)\), where
\[
w=\partial_1v_2-\partial_2v_1.
\]
Its stretching is \(w\partial_3u=0\). For a force \(f=(g_1,g_2,0)\) independent of \(x_3\), (4.1) therefore becomes precisely
\[
\partial_tw+v\cdot\nabla w-\nu\Delta w
=\partial_1g_2-\partial_2g_1.                               \tag{4.2}
\]
This proves the relation between the equations on that subspace. It does not identify all three-dimensional flows with two-dimensional ones.

## 5. A scalar that pushes the fluid

The two-dimensional Boussinesq system couples a scalar \(\theta\) to velocity through the vertical force:
\[
\begin{aligned}
\partial_t\theta+u\cdot\nabla\theta-\kappa\Delta\theta&=f_\theta,\\
\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u&=\theta e_2+f_u,\\
\operatorname{div}u&=0.
\end{aligned}                                               \tag{5.1}
\]
Here \(e_2=(0,1)\), \(\kappa\geq0\), and \(\nu>0\). The scalar force \(f_\theta\) and vector force \(f_u\) are different data.

Equation (4.2) applied to \(g=\theta e_2+f_u\) gives
\[
\partial_tw+u\cdot\nabla w-\nu\Delta w
=\partial_1\theta+\partial_1(f_u)_2-\partial_2(f_u)_1.        \tag{5.2}
\]
The sign of \(\partial_1\theta\) follows from our definition of \(w\). Defining vorticity with the opposite orientation changes that sign as well.

Suppose \(\theta,u\) are smooth with compact support on every strict time interval as in Section 3, and \(f_\theta,f_u\) have integrable spatial \(L^2\) norms on each such time interval. Multiplication of the scalar equation by \(\theta\) and integration gives
\[
\frac12\frac{d}{dt}\|\theta\|_2^2+\kappa\|\nabla\theta\|_2^2
=\int\theta f_\theta.                                      \tag{5.3}
\]
The proof is the scalar version of the energy calculation: transport is the divergence of \(u\theta^2/2\), and integration by parts changes \(-\kappa\theta\Delta\theta\) into \(\kappa|\nabla\theta|^2\). The same square-root argument as in Corollary 3.2 shows
\[
\|\theta(t)\|_2\leq\|\theta_0\|_2+\int_0^t\|f_\theta(s)\|_2\,ds.
                                                                    \tag{5.4}
\]
Velocity energy, keeping the scalar contribution, is
\[
\frac12\frac{d}{dt}\|u\|_2^2+\nu\|\nabla u\|_2^2
=\int\theta u_2+\int u\cdot f_u.                            \tag{5.5}
\]
Applying Cauchy–Schwarz, the regularized square root, and (5.4) yields
\[
\begin{aligned}
\|u(t)\|_2\leq{}&\|u_0\|_2+t\|\theta_0\|_2\\
&+\int_0^t(t-s)\|f_\theta(s)\|_2\,ds
+\int_0^t\|f_u(s)\|_2\,ds.                                 \tag{5.6}
\end{aligned}
\]
The factor \(t-s\) comes from integrating \(\int_0^\tau\|f_\theta(s)\|_2ds\) first over \(0\leq\tau\leq t\). Reversing the integration order leaves an interval \(s\leq\tau\leq t\) of length \(t-s\).

These bounds concern energy. A bound on a spatial derivative or on the supremum of vorticity requires an additional argument. In particular, energy alone does not justify a singularity claim or exclude one.

## 6. Exact changes of space and time

Take positive numbers \(r,c\), a fixed spatial center \(x_*\), and a fixed starting time \(t_*\). Set
\[
y=\frac{x-x_*}{r},\qquad \tau=\frac{t-t_*}{c}.
\]
Suppose \((\widetilde u,\widetilde p,\widetilde f)\) satisfies the Navier–Stokes equations in \(y,\tau\) at viscosity \(\widetilde\nu\). Define
\[
u=\frac rc\widetilde u,\qquad
p=\frac{r^2}{c^2}\widetilde p,\qquad
f=\frac r{c^2}\widetilde f,\qquad
\nu=\frac{r^2}{c}\widetilde\nu,                              \tag{6.1}
\]
where all fields on the right are evaluated at \((y,\tau)\).

**Proposition 6.1.** These fields satisfy (1.1) with the displayed physical viscosity \(\nu\). The map is invertible. Supports have their spatial radii multiplied by \(r\) and their time lengths multiplied by \(c\).

**Proof.** Direct differentiation gives
\[
\partial_tu=\frac r{c^2}\partial_\tau\widetilde u,\qquad
(u\cdot\nabla_x)u=\frac r{c^2}
(\widetilde u\cdot\nabla_y)\widetilde u,\qquad
\nabla_xp=\frac r{c^2}\nabla_y\widetilde p,
\]
and
\[
\nu\Delta_xu=\frac{\nu}{rc}\Delta_y\widetilde u
=\frac r{c^2}\widetilde\nu\Delta_y\widetilde u.
\]
Every momentum term has exactly the same factor \(r/c^2\). Divergence transforms as
\(\operatorname{div}_xu=c^{-1}\operatorname{div}_y\widetilde u=0\).
All scale factors are nonzero, so solving the coordinate equations and reciprocating the field factors gives the inverse. The support assertions follow from the coordinate equations. \(\square\)

For (5.1), the additional exact factors are
\[
\theta=\frac r{c^2}\widetilde\theta,\qquad
f_\theta=\frac r{c^3}\widetilde f_\theta,\qquad
\kappa=\frac{r^2}{c}\widetilde\kappa,\qquad
f_u=\frac r{c^2}\widetilde f_u.                              \tag{6.2}
\]
Indeed the scalar time derivative and transport have factor \(r/c^3\), while
\[
\kappa\Delta_x\theta=\frac{\kappa}{rc^2}\Delta_y\widetilde\theta
=\frac r{c^3}\widetilde\kappa\Delta_y\widetilde\theta.
\]
The buoyancy term \(\theta e_2\) has the momentum factor \(r/c^2\). This proves the full coupled comparison, including both diffusivities and both forces.

If the two diffusivities in the original packet are equal to \(\delta_*>0\), prescribing the common physical diffusion \(d>0\) gives
\[
c=\frac{\delta_*}{d}r^2.
\]
At this clock the physical field factors are
\[
u:\ \frac d{\delta_*}r^{-1},\quad
\theta:\ \left(\frac d{\delta_*}\right)^2r^{-3},\quad
p:\ \left(\frac d{\delta_*}\right)^2r^{-2},
\]
\[
f_u:\ \left(\frac d{\delta_*}\right)^2r^{-3},\qquad
f_\theta:\ \left(\frac d{\delta_*}\right)^3r^{-5}.             \tag{6.3}
\]
Thus shrinking a finite packet preserves the physical diffusion when its clock is changed accordingly. The force size is a separate calculation and can increase.

More precisely, for \(\gamma\in\mathbb N_0^2\) and \(b\in\mathbb N_0\),
\[
\partial_x^\gamma\partial_t^b f_u
=r^{1-|\gamma|}c^{-2-b}
(\partial_y^\gamma\partial_\tau^b\widetilde f_u)(y,\tau),
\]
\[
\partial_x^\gamma\partial_t^b f_\theta
=r^{1-|\gamma|}c^{-3-b}
(\partial_y^\gamma\partial_\tau^b\widetilde f_\theta)(y,\tau).
                                                                    \tag{6.4}
\]
Each spatial derivative contributes \(r^{-1}\) and each time derivative contributes \(c^{-1}\), which proves these formulas by repeated differentiation.

### Which integral norms keep their size?

For \(1\leq p<\infty\), the spatial norm of a vector field is
\(\|v\|_p=(\int|v|^p\,dx)^{1/p}\), using Euclidean length inside the integral. For \(p=\infty\) it is the essential supremum of that length. For \(1\leq q<\infty\), define the mixed norm on a time interval \(I\) by
\[
\|v\|_{L^q(I;L^p)}
=\left(\int_I\|v(t)\|_p^q\,dt\right)^{1/q};
\]
for \(q=\infty\), take the essential supremum in time. In exponent formulas below, \(1/\infty=0\).

Let \(I=t_*+c\widetilde I\) be the corresponding time intervals. The exact transformation (6.1) gives
\[
\|u\|_{L^q(I;L^p_x)}
=r^{1+n/p}c^{-1+1/q}
\|\widetilde u\|_{L^q(\widetilde I;L^p_y)},\qquad
\|f\|_{L^q(I;L^p_x)}
=r^{1+n/p}c^{-2+1/q}
\|\widetilde f\|_{L^q(\widetilde I;L^p_y)}.                  \tag{6.5}
\]
To prove the first identity for finite \(p,q\), substitute \(dx=r^n\,dy\) in the spatial integral, take its \(p\)-th root, then substitute \(dt=c\,d\tau\) and take the \(q\)-th root. The field factor is \(r/c\). This gives exactly the first factor in (6.5). For the force the field factor is \(r/c^2\), proving the second identity. When an exponent is infinite, a bijective change of variables preserves the essential supremum; the corresponding Jacobian factor is absent. This proves all the endpoint cases as well.

If the original and physical viscosities are the same positive number, (6.1) requires \(c=r^2\). The velocity factor in (6.5) is then
\[
r^{n/p+2/q-1}.
\]
A mixed velocity norm is called *critical for this scaling* when it stays unchanged for every \(r>0\). For a nonzero field with a finite norm, this is equivalent to
\[
\frac np+\frac2q=1.                                       \tag{6.6}
\]
For example, in dimension three both \(L^\infty_tL^3_x\) and \(L^4_tL^6_x\) have that property. The force norm is unchanged instead when \(n/p+2/q=3\), because its exponent is \(n/p+2/q-3\).

For the coupled system in dimension two, the scalar \(\theta\) has the same field factor as \(f_u\), while \(f_\theta\) has one additional factor \(c^{-1}\). At the equal-viscosity clock \(c=r^2\), their mixed norm factors are respectively \(r^{2/p+2/q-3}\) and \(r^{2/p+2/q-5}\). These follow from the same two changes of variables, with the field factors in (6.2). Criticality names an exact invariance of a norm. Proving existence, uniqueness or a regularity criterion in that norm requires further estimates.

## 7. Exercises with complete solutions

**Exercise 1. A gradient force.** Suppose \(f=\nabla\phi\). Show both that it has zero curl and that it does zero total work on a compact divergence-free velocity. Does this make \(\phi\) spatially constant?

**Solution.** Equality of mixed derivatives gives \(\nabla\times\nabla\phi=0\). Integration by parts gives
\[
\int u\cdot\nabla\phi
=\int\operatorname{div}(\phi u)-\int\phi\operatorname{div}u=0.
\]
Neither statement forces \(\phi\) to be constant. For example \(\phi(x)=|x|^2\) has nonzero gradient away from the origin. In momentum, the gradient force can be moved into the pressure: \(\widehat p=p-\phi\) and \(\widehat f=0\) give the same velocity equation.

**Exercise 2. A compact pulse from rest.** In two dimensions take \(\psi\in C_c^\infty(\mathbb R^2)\), a smooth scalar \(a(t)\) with \(a(0)=0\), and
\[
v=(-\partial_2\psi,\partial_1\psi),\qquad u(x,t)=a(t)v(x),\qquad p=0.
\]
Find the force exactly and check divergence and the initial condition.

**Solution.** The divergence of \(v\) is \(-\partial_1\partial_2\psi+\partial_2\partial_1\psi=0\). Thus \(\operatorname{div}u=0\), and \(u(x,0)=0\). Formula (2.2) gives
\[
f=a'v+a^2(v\cdot\nabla)v-\nu a\Delta v.
\]
Every displayed term is smooth and compactly supported in the same fixed support of the derivatives of \(\psi\). If \(a\) extends smoothly through \(T\), so does \(f\). If \(u\) is nonzero at some later time, Corollary 3.2 shows that this force cannot vanish throughout the preceding interval.

**Exercise 3. Why an unchanged field has a different force at a different viscosity.** Keep \(u,p\) fixed and replace \(\nu\) by \(\widehat\nu>0\). Find \(\widehat f\).

**Solution.** Subtract the two complete momentum equations:
\[
\widehat f-f=(\nu-\widehat\nu)\Delta u.
\]
Hence \(\widehat f=f+(\nu-\widehat\nu)\Delta u\). This is an exact identity, including its sign. Every mixed derivative satisfies the same identity after applying that derivative. Smoothness of \(f\) at \(T\) alone does not control the added term if derivatives of \(u\) grow there.

**Exercise 4. A three-dimensional flow obtained from a two-dimensional one.** Let \(v,p,g\) solve the two-dimensional momentum equation. Choose \(\chi\in C_c^\infty(\mathbb R)\). Define
\[
U(x_1,x_2,z,t)=(\chi(z)v_1,\chi(z)v_2,0),\qquad P=\chi(z)p.
\]
Find the full three-dimensional force and decide whether compact support of \(v,g\) is enough to make that force compact.

**Solution.** Divergence is \(\chi\operatorname{div}v=0\). The horizontal time, transport, pressure and diffusion terms are
\[
\chi v_t,\quad \chi^2(v\cdot\nabla)v,\quad
\chi\nabla p,\quad -\nu\chi\Delta v-\nu\chi''v.
\]
The horizontal force is therefore
\[
F_h=\chi g+(\chi^2-\chi)(v\cdot\nabla)v-\nu\chi''v.
\]
The vertical velocity is zero, but the vertical pressure derivative is \(\chi'p\), so
\[
F_3=\chi'p.
\]
Compact support of \(v,g\) alone does not control the support of this pressure term. For an explicit example take \(v=0\), \(g=0\), \(p=1\), and a nonconstant \(\chi\). These are valid two-dimensional data, but \(F_3=\chi'(z)\) is nonzero for every horizontal point at any \(z\) where \(\chi'(z)\ne0\). Its support is therefore unbounded horizontally. Compact support of \(p\) as well is sufficient. If \(\chi=1\) on an interval, the original flow and force are recovered there by evaluation at any \(z\) in that interval.

**Exercise 5. Energy under the exact similarity.** Determine the energy and total squared-gradient factors for the \(n\)-dimensional map (6.1).

**Solution.** The spatial Jacobian is \(dx=r^n\,dy\), so
\[
\|u(t)\|_{L^2_x}^2=\frac{r^{n+2}}{c^2}
\|\widetilde u(\tau)\|_{L^2_y}^2.
\]
Also \(\nabla_xu=c^{-1}\nabla_y\widetilde u\) and \(dt=c\,d\tau\). Consequently
\[
\nu\int_{t_*}^{t_*+c\tau}\|\nabla_xu(t)\|_2^2dt
=\nu\frac{r^n}{c}\int_0^\tau\|\nabla_y\widetilde u(s)\|_2^2ds
=\frac{r^{n+2}}{c^2}\widetilde\nu
\int_0^\tau\|\nabla_y\widetilde u(s)\|_2^2ds.
\]
Finally the time-integrated work has factor
\((r/c)(r/c^2)r^n c=r^{n+2}/c^2\). Thus every term of the complete energy balance has the same factor.

## References

[L] Yanguang Li, *Global Regularity for the Viscous Boussinesq Equations*, [arXiv:math/0302199v1](https://arxiv.org/abs/math/0302199v1), 2003. The original equations keep separate heat diffusion and viscosity coefficients. That paper uses the opposite orientation for two-dimensional vorticity.

[CMX] Dongho Chae, Qianyun Miao and Liutang Xue, *Global regularity of non-diffusive temperature fronts for the 2D viscous Boussinesq system*, [arXiv:2110.06442v2](https://arxiv.org/abs/2110.06442v2), 2021. The equations and Proposition 3.1 concern positive viscosity with no heat diffusion and no external forces.

[J] Ning Ju, *Global Regularity and Long-time Behavior of the Solutions to the 2D Boussinesq Equations without Diffusivity in a Bounded Domain*, [arXiv:1508.06176v1](https://arxiv.org/abs/1508.06176v1), 2015. Its boundary conditions matter when comparing its estimates with whole-space calculations.
