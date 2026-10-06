# Contact transformations and first-order equations

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Public domain (CC0).*

A first-order equation constrains a point, a function value, and a tangent hyperplane. Contact geometry treats these three pieces together. Its transformations can exchange positions and slopes; its infinitesimal generators are encoded by one function; and its characteristic curves reconstruct a solution from noncharacteristic initial data.

We work locally with analytic functions over $\mathbb K=\mathbb R$ or $\mathbb C$. The analytic flow theorem from One-parameter groups and canonical coordinates, Frobenius from Complete systems and invariants, and the graph-transversality calculation in Prolongation and differential invariants are used. The Euclidean normal-flow examples are real. Our convention is $W=\theta(X_W)$ and $[X,Y]=XY-YX$. Lie's original characteristic function has the opposite sign; the historical reading at the end makes this difference explicit.

## 1. Contact elements and contact transformations

On $J^1(\mathbb K^n,\mathbb K)$ use coordinates $(x^1,\ldots,x^n,z,p_1,\ldots,p_n)$ and the form

$$
\theta=dz-\sum_i p_i\,dx^i,\qquad
d\theta=\sum_i dx^i\wedge dp_i.
\tag{1.1}
$$

The hyperplane $C=\ker\theta$ is the **contact distribution**. At each point, a basis is $E_i=\partial_{x^i}+p_i\partial_z$ together with $\partial_{p_i}$. The restriction of $d\theta$ to $C$ is nondegenerate, since $d\theta(E_i,\partial_{p_j})=\delta_{ij}$. Equivalently, $\theta\wedge(d\theta)^n$ is a nowhere-zero volume form.

An immersed $n$-dimensional submanifold on which $\theta$ vanishes is **Legendrian**. On such a submanifold $d\theta$ vanishes too, by differentiating the pulled-back zero form. If its projection to $x$ is a local diffeomorphism, it is a graph $(x,z(x),p(x))$, and $\theta=0$ says $p_i=\partial_i z$. Thus it is exactly the first-jet graph of a function. A Legendrian submanifold need not project to a graph.

A local diffeomorphism $\Phi$ is **contact** if

$$
\Phi^*\theta=\rho\theta,\qquad \rho\ne0.
\tag{1.2}
$$

This condition means that it preserves $C$. It also preserves Legendrian submanifolds, though their projections can become singular.

**Theorem 1.1.** Every prolonged point diffeomorphism is contact on its graph-transverse domain. The Legendre transformation

$$
\mathcal L(x,z,p)=(p,\,p\cdot x-z,\,x)
\tag{1.3}
$$

is contact and satisfies $\mathcal L^2=\mathrm{id}$.

**Proof.** Let a point diffeomorphism be $(x,z)\mapsto(X(x,z),Z(x,z))$. Put $A^j_i=\partial_iX^j+p_iX^j_z$. Where $A$ is invertible, its prolonged slopes $P_j$ are the unique solution of

$$
\partial_iZ+p_iZ_z=\sum_jP_jA^j_i.
$$

The form $dZ-P_jdX^j$ has no $dp$ components and annihilates every $E_i$. Therefore

$$
dZ-\sum_jP_jdX^j=\rho\theta,
\qquad \rho=Z_z-\sum_jP_jX^j_z.
$$

Use the basis $(E_1,\ldots,E_n,\partial_z)$ in point-space tangent coordinates, and the corresponding transformed basis. The point derivative has block matrix $\left(\begin{smallmatrix}A&X_z\\0&\rho\end{smallmatrix}\right)$. Its determinant is $\det A\,\rho$. Both the point derivative and $A$ are invertible, so $\rho\ne0$. Prolonging the inverse point map gives the inverse on this graph chart, establishing a contact diffeomorphism.

For (1.3), denote its new coordinates by $(X,Z,P)$. Direct calculation gives

$$
dZ-\sum_iP_i\,dX^i
=d(p\cdot x-z)-x\cdot dp
=p\cdot dx-dz=-\theta.
$$

Applying (1.3) twice returns $(x,x\cdot p-(p\cdot x-z),p)=(x,z,p)$. The point transformation is an exact involution; the sign occurs in its pullback of the form. $\square$

The Legendre transformation is generally not a prolonged point map, because its new independent coordinate $X=p$ depends on the slope. On a function graph it becomes a graph only where the Hessian $\partial p/\partial x$ is invertible.

In the plane, an incidence or **directrix equation** $\Omega(x,z,X,Z)=0$ supplies another useful description. Suppose $\Omega_z\Omega_Z\ne0$ and the equations

$$
\Omega=0,\qquad \Omega_x+p\Omega_z=0
\tag{1.4}
$$

can be solved for $(X,Z)$ as functions of $(x,z,p)$. Define $P=-\Omega_X/\Omega_Z$. Differentiating $\Omega=0$ and using (1.4) gives

$$
\Omega_z(dz-p\,dx)+\Omega_Z(dZ-P\,dX)=0.
$$

Thus the resulting map has multiplier $\rho=-\Omega_z/\Omega_Z$. It is a local diffeomorphism: if a tangent vector lies in the kernel of its derivative, the pullback identity forces it into $C$, and the differentiated identity forces it to be orthogonal to all of $C$ under $d\theta$. Nondegeneracy on $C$ makes that vector zero. The inverse function theorem applies. For $\Omega=z+Z-xX$, equations (1.4) give exactly (1.3). These rank and nonvanishing conditions are part of the directrix construction.

## 2. One function determines a contact vector field

A vector field $X$ is contact when $\mathcal L_X\theta=\lambda\theta$ for a function $\lambda$.

**Theorem 2.1 (generating-function bijection).** The map $X\mapsto\theta(X)$ is a linear bijection from contact vector fields to functions. For any function $W$ its inverse is

$$
X_W=-\sum_iW_{p_i}\partial_{x^i}
+\left(W-\sum_ip_iW_{p_i}\right)\partial_z
+\sum_i(W_{x^i}+p_iW_z)\partial_{p_i}.
\tag{2.1}
$$

Moreover $\mathcal L_{X_W}\theta=W_z\theta$.

**Proof.** Write $X=a^i\partial_{x^i}+b\partial_z+c_i\partial_{p_i}$ and $W=b-p_ia^i$. Cartan's differentiation formula gives

$$
\mathcal L_X\theta=dW+\iota_Xd\theta
=dW+\sum_i(a^i\,dp_i-c_i\,dx^i).
$$

Compare coefficients with $\lambda(dz-p_i\,dx^i)$. The $dz$ coefficient gives $\lambda=W_z$; the $dp_i$ coefficients give $a^i=-W_{p_i}$; and the $dx^i$ coefficients give $c_i=W_{x^i}+p_iW_z$. Finally $b=W+p_ia^i$ gives (2.1). These equations prove uniqueness. Substitution proves existence for every $W$ and the displayed Lie derivative. $\square$

In particular $X_1=\partial_z$. Adding a constant to a generating function changes its contact field. This differs from ordinary Hamiltonian fields on symplectic phase space, where constants produce zero fields.

Define the **Lagrange bracket**, also called the contact Jacobi bracket, by

$$
\{W,V\}_c=X_WV-W_zV.
\tag{2.2}
$$

Explicitly,

$$
\{W,V\}_c=
\sum_i(W_{x^i}V_{p_i}-W_{p_i}V_{x^i})
+WV_z-VW_z
+\sum_ip_i(W_zV_{p_i}-W_{p_i}V_z).
\tag{2.3}
$$

**Theorem 2.2 (bracket and Jacobi identity).** The bracket is antisymmetric, satisfies the Jacobi identity, and obeys

$$
[X_W,X_V]=X_{\{W,V\}_c}.
\tag{2.4}
$$

**Proof.** The formula for the Lie derivative of a form evaluated on a field gives

$$
\theta([X_W,X_V])=X_W(\theta(X_V))-(\mathcal L_{X_W}\theta)(X_V)
=X_WV-W_zV.
$$

The commutator is contact, since

$$
\mathcal L_{[X_W,X_V]}\theta
=(X_WV_z-X_VW_z)\theta
$$

by the commutator rule for Lie derivatives. Theorem 2.1 therefore proves (2.4). Antisymmetry follows either from (2.3) or the antisymmetry of field commutators and injectivity. Applying (2.4) to the three terms of the Jacobi expression and using the Jacobi identity of differential operators proves that expression is zero, again by injectivity. $\square$

Unlike a Poisson bracket, (2.2) is not a derivation in each argument for ordinary multiplication. For example $\{W,1\}_c=-W_z$, and

$$
\{W,UV\}_c=\{W,U\}_cV+U\{W,V\}_c+W_zUV.
$$

For functions independent of $z$, it reduces to the ordinary Poisson bracket

$$
\{W,V\}_P=\sum_i(W_{x^i}V_{p_i}-W_{p_i}V_{x^i}).
\tag{2.5}
$$

## 3. Characteristics reconstruct a solution

Let $E=\{F(x,z,p)=0\}$. From (2.2), $\{F,F\}_c=0$, hence

$$
X_FF=F F_z.
\tag{3.1}
$$

Thus $X_F$ is tangent to $E$. Its curves there satisfy

$$
\dot x^i=-F_{p_i},\qquad
\dot z=-\sum_ip_iF_{p_i},\qquad
\dot p_i=F_{x^i}+p_iF_z.
\tag{3.2}
$$

Reversing the curve parameter gives the more usual signs in the characteristic equations. On $E$, $\theta(X_F)=F=0$. If $F_p\ne0$, the restriction of $dF$ to $C$ is nonzero, and nondegeneracy of $d\theta|_C$ shows that $X_F$ spans the one-dimensional kernel of $d\theta$ on $TE\cap C$. These are the characteristic curves of the equation.

Let $S$ be an analytic hypersurface in $x$ space and prescribe $z=g$ on $S$. A lifted initial datum is $(x,g(x),p^0(x))$ with

$$
p^0|_{TS}=dg,\qquad F(x,g,p^0)=0.
\tag{3.3}
$$

Let $\nu$ be a nonzero conormal to $S$. The datum is **noncharacteristic** when

$$
\sum_i\nu_iF_{p_i}(x,g,p^0)\ne0.
\tag{3.4}
$$

This is stronger than $F_p\ne0$: the characteristic base direction must be transverse to this particular $S$. Locally write $p^0=\eta+b\nu$, where $\eta|_{TS}=dg$. Given a root at a reference point, the derivative of $F(x,g,\eta+b\nu)$ with respect to $b$ is (3.4). The analytic implicit function theorem determines a unique nearby analytic root branch. Different separated roots can give different Cauchy solutions; uniqueness below fixes this branch.

**Theorem 3.1 (noncharacteristic Cauchy problem).** The union of the $X_F$ characteristics through a lifted analytic datum satisfying (3.3)–(3.4) is the first-jet graph of a unique nearby analytic solution of $F(x,z,dz)=0$ with those initial data and that root branch.

**Proof.** Parametrize $S$ by $s\in\mathbb K^{n-1}$ and let $\gamma(s)$ be its lift. The analytic flow $\Phi_t$ of $X_F$ exists on a product neighbourhood. Equation (3.1) and uniqueness of the scalar linear ODE for $F(\Phi_t\gamma(s))$ imply that its value remains zero. Thus $\Psi(s,t)=\Phi_t\gamma(s)$ lies in $E$.

At $t=0$ the derivatives of its $x$ projection in the $s$ directions span $TS$, and the $t$ derivative is $-F_p$. Condition (3.4) makes these $n$ directions independent. The inverse function theorem makes the $x$ projection of $\Psi$ a local analytic diffeomorphism. In particular, $\Psi$ is an immersed $n$-manifold.

The initial lift annihilates $\theta$ by (3.3). The flow is contact: differentiating $\Phi_t^*\theta$ gives the scalar equation with coefficient $F_z\circ\Phi_t$, so its multiplier is the nonzero exponential of the time integral of that coefficient. Consequently the transported $s$ directions still annihilate $\theta$. The $t$ direction does too, since $\theta(X_F)=F=0$ on $E$. Therefore $\Psi$ is Legendrian. Its invertible $x$ projection and Section 1 make it $(x,z(x),dz(x))$. It lies in $E$ and has the required initial value.

For uniqueness, the first-jet graph $L$ of any other nearby solution is Legendrian in $E$. For $v\in TL$, Cartan's formula gives $d\theta(X_F,v)=F_z\theta(v)-dF(v)=0$. Inside the symplectic vector space $C$, the $n$-dimensional isotropic space $TL$ is Lagrangian, hence equals its symplectic orthogonal. Since $X_F\in C$ on $E$, it follows that $X_F$ is tangent to $L$. Its flow through the initial lift stays in $L$. Uniqueness of the initial normal root forces that lift to be $\gamma$, and uniqueness of the flow forces $L$ to coincide with $\Psi$. $\square$

Multiplying $F$ by a nonvanishing function changes $X_F|_E$ by that same factor. Indeed (2.1) applied to $aF$ gives $X_{aF}|_E=aX_F|_E$. The unparametrized characteristics and the Cauchy solution depend on the equation hypersurface rather than its chosen defining function.

A **complete integral** is an $n$-parameter family $z=U(x;a)$ of solutions whose map $(x,a)\mapsto(x,U,U_x)$ has rank $2n$. Equivalently the $(n+1)\times n$ matrix with rows $U_a$ and $U_{x^i a}$ has rank $n$. The resulting Legendrian graphs locally fill a regular equation hypersurface. An envelope can produce further solutions: replace $a_n$ by a function $h(a_1,\ldots,a_{n-1})$, and solve

$$
U_{a_i}+U_{a_n}h_{a_i}=0\quad(1\le i<n)
$$

for the parameters as functions of $x$, wherever the required implicit derivative is invertible. Differentiating $z=U(x;a(x))$ then leaves $z_x=U_x$, so the envelope still satisfies $F=0$. A full stationary envelope $U_a=0$ has the same property when it defines a graph. Envelopes and their singular projections need separate rank checks; they are not covered automatically by the noncharacteristic theorem.

## 4. Poisson's theorem and the contact qualification

The word “first integral” requires care. An ordinary first integral of $X_F$ satisfies $X_FW=0$. A function commuting with $F$ in the contact bracket instead satisfies

$$
\{F,W\}_c=0\quad\Longleftrightarrow\quad X_FW=F_zW.
\tag{4.1}
$$

This is a weighted conservation equation. Ratios of two such functions are ordinary first integrals where the denominator is nonzero. For $F_z=0$, weighted and ordinary conservation agree.

**Theorem 4.1 (Poisson and contact closure).** For any collection $F_1,\ldots,F_r$, the functions satisfying $\{F_a,W\}_c=0$ for every $a$ are closed under the Lagrange bracket. If every $F_a$ is independent of $z$, the ordinary common first integrals of the fields $X_{F_a}$ therefore have this closure property. For $z$-independent functions throughout, this is Poisson's theorem for (2.5).

The corresponding assertion holds on a regular common level $E=\{F_a=0\}$ if conservation is interpreted as $\{F_a,W\}_c=0$ on $E$. In particular it holds for the weighted characteristic integrals of a regular involutive first-order system.

**Proof.** Jacobi gives

$$
\{F_a,\{W,V\}_c\}_c
=\{\{F_a,W\}_c,V\}_c+\{W,\{F_a,V\}_c\}_c.
\tag{4.2}
$$

If the inner brackets vanish identically, both terms on the right vanish. When $F_{a,z}=0$, (2.2) identifies the conservation equation with ordinary first-integral conservation, proving the strict-contact case and its Poisson restriction.

For the assertion on $E$, put $G_a=\{F_a,W\}_c$ and $H_a=\{F_a,V\}_c$. These vanish on $E$. Also $X_WF_a=\{W,F_a\}_c+W_zF_a$ vanishes there, so $X_W$ is tangent to the regular common level; the same holds for $X_V$. A tangent field differentiates a function vanishing on $E$ to zero on $E$. Thus $\{G_a,V\}_c=-\{V,G_a\}_c=-X_VG_a+V_zG_a$ and $\{W,H_a\}_c=X_WH_a-W_zH_a$ both vanish there. Equation (4.2) proves the level-set assertion. $\square$

For the stated geometric system, involutivity means $\{F_a,F_b\}_c=0$ on $E$, with the $dF_a|_C$ independent there. The fields $X_{F_a}|_E$ are then independent characteristic directions. Regular defining equations express $\{F_a,F_b\}_c=\sum_c b_{ab}^cF_c$ locally. Formula (2.1) gives

$$
[X_{F_a},X_{F_b}]|_E=\sum_c b_{ab}^cX_{F_c}|_E,
$$

so Frobenius integrates their distribution. The closure theorem concerns functions on an ambient neighbourhood with the specified conservation on $E$; it does not define an unrestricted bracket on arbitrary functions on $E$ independent of their extensions.

The sketch's ordinary-integral claim without the qualification (4.1) is false. Take $n=2$, $F=z-p_2$, and work where $p_2\ne0$. Then

$$
X_F=\partial_{x^2}+z\partial_z+p_1\partial_{p_1}+p_2\partial_{p_2}.
$$

Both $W=x^1$ and $V=p_1/p_2$ are ordinary first integrals. Nevertheless

$$
\{W,V\}_c=\frac1{p_2},\qquad
X_F\{W,V\}_c=-\frac1{p_2}\ne0.
\tag{4.3}
$$

The failure persists on the regular hypersurface $z=p_2$, with $F_p\ne0$ and a nonzero projected characteristic direction. Even $z$-independence of $W,V$ alone is insufficient: the defining function $F$ itself has $F_z=1$.

## 5. Jacobi's integration method and function groups

For $z$-independent functions, work in phase space $(x,p)$ with $\omega=\sum_i dx^i\wedge dp_i$. The associated field is $A_H=-H_{p_i}\partial_{x^i}+H_{x^i}\partial_{p_i}$, with $\iota_{A_H}\omega=-dH$ and $A_HV=\{H,V\}_P$. The contact field $X_H$ adds the $z$ component $H-p_iH_{p_i}$.

**Proposition 5.1 (integration from commuting integrals).** Suppose $H_1,\ldots,H_n$ are independent phase-space functions with $\{H_i,H_j\}_P=0$. Each regular common level is Lagrangian. On a level where projection to $x$ is invertible, one quadrature gives $z=u(x)$ with $H_i(x,du)=c_i$.

**Proof.** The fields $A_{H_i}$ are independent because $\omega$ is nondegenerate and the $dH_i$ are independent. They are tangent to each common level because their pairwise brackets vanish. That level has dimension $n$, so these fields span its tangent space. Moreover $\omega(A_{H_i},A_{H_j})=-dH_i(A_{H_j})=0$. Thus the level is Lagrangian, and the fields commute by the Poisson version of (2.4).

If the level is a graph $p=p(x)$, vanishing of the pulled-back $\omega$ says the one-form $\sum_i p_i(x)dx^i$ is closed. On a small star-shaped coordinate neighbourhood it is exact: the integral of that form along a path from a fixed point defines $u$, with path independence following by integrating the closed form over coordinate homotopies. Hence $du=p$, and the common-level equations give $H_i(x,du)=c_i$. The additive constant of $u$ is free. $\square$

This is the local mechanism of Jacobi's method. For $F(x,p)=0$, finding $n-1$ additional independent integrals in mutual Poisson involution with $F$ supplies the $H_i$. Their commuting flows give the level, and the closed one-form gives the solution. Independence and graph transversality are required. The method does not assert that an arbitrarily chosen set of conserved quantities is commuting, or that every common level projects regularly.

A **function group** in Lie's phase-space terminology consists of independent functions $H_1,\ldots,H_r$ whose brackets satisfy

$$
\{H_a,H_b\}_P=B_{ab}(H_1,\ldots,H_r).
\tag{5.1}
$$

It includes all functions of these generators. The chain rule shows closure:

$$
\{f(H),g(H)\}_P=
\sum_{a,b}f_{h_a}(H)g_{h_b}(H)B_{ab}(H).
$$

Consequently the $B_{ab}$ define a Poisson bracket on the local parameter image of $H$. Jacobi follows by pulling back its Jacobi expression along the submersion $H$. The fields $A_{H_a}$ span an involutive distribution of rank $r$, because $A_{B_{ab}(H)}=\sum_c(\partial_cB_{ab})(H)A_{H_c}$. Its $2n-r$ independent local first integrals form the **polar function group**; Poisson's theorem proves their bracket closure. A distinguished function is a function of $H$ commuting with all $H_a$, equivalently a Casimir of the parameter Poisson bracket. If $B$ has constant rank $2s$, Frobenius on its Hamiltonian distribution gives $r-2s$ independent distinguished functions locally.

For a concrete example in four-dimensional phase space, $H_1=x^1,H_2=p_1$ have bracket $1$. All functions of these two variables form a function group with no nonconstant distinguished function. Its polar group consists exactly of functions of $x^2,p_2$, again with their usual Poisson bracket. The two sets commute with one another. Lie's Chapters 8–13 develop the invariant and homogeneous forms of this theory; this description supplies the part used here.

## 6. Computed examples

**Clairaut's equation.** In one independent variable let

$$
F=z-px-f(p)=0.
$$

Equation (2.1) gives

$$
X_F=(x+f'(p))\partial_x
+(z-f(p)+pf'(p))\partial_z,
\qquad \dot p=0.
\tag{6.1}
$$

The regular characteristic branches have constant $p=c$, giving the complete integral $z=cx+f(c)$. Its parameter derivative matrix has rank one because $\partial_c z_x=1$.

Under the Legendre map, the equation becomes $Z=-f(X)$, with $P$ free. A Legendrian curve in this surface satisfies $(-f'(X)-P)dX=0$. If $X$ is constant, its image is the vertical curve $X=c,Z=-f(c)$; pulling it back gives $z=cx+f(c)$. If $X$ varies, it has $P=-f'(X)$, and pulling it back gives the singular envelope

$$
x=-f'(p),\qquad z=f(p)-pf'(p).
\tag{6.2}
$$

Where $f''(p)\ne0$, this is a graph and differentiation gives $dz/dx=p$. For analytic solutions, differentiating the original equation gives $(x+f'(p))p'=0$; the identity theorem yields one of these two branches on a connected small domain. At the envelope $F_p=0$, the contact characteristic field itself vanishes. It lies outside Theorem 3.1's noncharacteristic domain. Treating all Legendre images as graphs would lose the constant-slope solutions.

**Eikonal characteristics.** Take $F=(p_1^2+p_2^2-1)/2$. On $E$, (3.2) gives

$$
x(t)=x_0-tp_0,\qquad p(t)=p_0,\qquad z(t)=z_0-t,
\qquad |p_0|=1.
\tag{6.3}
$$

The base characteristics are straight lines of unit speed. For zero initial value on a regular plane curve, the lifted $p_0$ is either unit normal. The solution is a local signed distance on the corresponding branch, up to the first failure of the normal-ray projection. Intersections and focal points need a new analysis rather than an extension of the local uniqueness theorem beyond its domain.

**The kinetic generator.** For $W=|p|^2/2$, the full contact flow is

$$
(x,z,p)\longmapsto
\left(x-tp,\ z-\frac t2|p|^2,\ p\right).
\tag{6.4}
$$

Its phase-space projection is straight geodesic motion. The eikonal defining function in (6.3) is $W-1/2$, so its contact field is $X_W-\tfrac12\partial_z$. It has the same phase-space trajectories and a different $z$ transport. This is why the eikonal characteristics and (6.4) have different height rates on $|p|=1$.

**Parallel curves.** In the plane put $W=\sqrt{1+p^2}$ on the positive real branch. Its flow is

$$
\Phi_t(x,z,p)=
\left(x-\frac{tp}{\sqrt{1+p^2}},\
z+\frac t{\sqrt{1+p^2}},\ p\right).
\tag{6.5}
$$

The point moves distance $t$ in its unit normal direction $(-p,1)/\sqrt{1+p^2}$. This is the parallel transformation historically described as dilation along normals. Differentiating (6.5) gives $\Phi_t^*\theta=\theta$, since $d(1/\sqrt{1+p^2})+p\,d(p/\sqrt{1+p^2})=0$. Along an original graph with curvature $\kappa=p_x/(1+p^2)^{3/2}$, its new independent-coordinate derivative is $1-t\kappa$. Thus the offset remains a graph only where that factor is nonzero. On the branch $1-t\kappa>0$, its oriented curvature is $\kappa/(1-t\kappa)$. The contact map remains invertible even when a particular graph develops a singular projection.

![The original parabola and its normal offsets at distances 0.45 and 1.5; the second offset has two cusp points while the lifted slope still parametrizes its Legendrian curve.](figures/parallel-curves.png)

*Computed illustration of (6.5).* The original curve is $(s,s^2/2)$ with slope $p=s$ and curvature $(1+s^2)^{-3/2}$. Gray segments are its normal displacements. At $t=0.45$ the factor $1-t\kappa$ stays positive. At $t=1.5$ the two marked cusps occur at $s=\pm\sqrt{1.5^{2/3}-1}$, where that factor vanishes. The lifted curve in $(X,Z,p)$ is still regular because $dp/ds=1$. Curves are numerical samples of these exact formulas; the projection criterion is proved above. The reproducible plotting source and vector copy accompany the public source edition.

## 7. Higher jets and symplectization

**Bäcklund's theorem, stated without proof.** For one dependent variable and a finite order $k\ge1$, every local diffeomorphism of the unrestricted jet space $J^k$ preserving its Cartan distribution is locally the prolongation of a contact transformation of $J^1$, on the relevant graph-transverse domain. For more than one dependent variable the corresponding transformations are prolonged point transformations. This statement is about unrestricted finite jet spaces; it does not classify all symmetries restricted to a particular equation or all transformations of infinite jets. A precise reference is Tryhuk–Chrastinová, [*On the Mapping of Jet Spaces*](https://www.atlantis-press.com/article/125951023.pdf), §3, Theorem 1, printed pp. 296–297.

For scalar jets the Cartan distribution is the common kernel of $du_J-u_{J,i}dx^i$ with $|J|<k$. At $k=1$ it is the contact distribution of (1.1). At higher order it is not a hyperplane distribution of that same type. The theorem identifies its finite-order transformations through the first contact level.

Contact geometry also relates precisely to homogeneous symplectic geometry. Add $r\in\mathbb R^*$, or $r\in\mathbb C^*$ in the complex setting, and set

$$
\alpha=r\theta,\qquad
\omega=d\alpha=dr\wedge\theta+r\,d\theta.
\tag{7.1}
$$

This form is symplectic because $\omega^{n+1}=(n+1)r^n\,dr\wedge\theta\wedge(d\theta)^n\ne0$. A contact map with multiplier $\rho$ lifts to

$$
\widehat\Phi(q,r)=(\Phi(q),r/\rho(q)).
\tag{7.2}
$$

Pulling back $\alpha$ gives $(r/\rho)\Phi^*\theta=r\theta$, so the lift preserves $\omega$. It commutes with dilation of $r$. Conversely, a dilation-equivariant map preserving $\alpha$ descends to a contact map, by writing its radial component as $r$ times a nowhere-zero function and comparing the forms. For positive real symplectization $r>0$, restrict to positive multipliers. The Legendre map has multiplier $-1$, and (7.2) exchanges the two real components when both signs of $r$ are allowed.

This construction supplies the comparison with the planned Fourier-integral course AN-04, especially “Phase space and generating families” and “Hamilton fields and subprincipal transport,” and the planned microlocal-sheaf course SH-03 on contact transformations and kernels. Those course readers have no registered public link in the course catalogue checked for this edition. The public course index gives the available related courses. The bridge here is the explicit symplectization (7.1)–(7.2).

## 8. Exercises

**Exercise 1 (easy).** Verify the Legendre map in general dimension. Locate exactly the sign in the sketch's phrase “involution up to sign.” For $z=f(x)$, state the condition for its transformed Legendrian submanifold to be a graph.

**Exercise 2 (medium).** For $n=1$, calculate $X_z,X_p,X_{xp}$ and all three pairwise brackets. Check them both as contact brackets and as vector-field commutators.

**Exercise 3 (medium).** Solve the analytic Clairaut equation using the Legendre transformation, keeping both constant-slope and singular branches. For $f(p)=p^2/2$, find its envelope and determine whether the noncharacteristic existence theorem applies there.

**Exercise 4 (medium).** In two independent variables $(x,y)$, write $p=z_y$, $q=z_x$ and solve $p^2=z$ with $z(x,0)=g(x)>0$. Fix the initial root $p(x,0)=\varepsilon\sqrt{g(x)}$, where $\varepsilon\in\{1,-1\}$. Calculate the characteristic flow and verify the resulting solution directly.

**Exercise 5 (hard).** Prove the generating-function bijection for arbitrary $n$ by comparing coefficients in Cartan's formula. Derive the bracket and its Jacobi identity. Explain, using (4.3), why ordinary characteristic first integrals are not automatically closed under that bracket.

## 9. Solutions

**Solution 1.** Write $(X,Z,P)=(p,p\cdot x-z,x)$. Then $dZ-P\cdot dX=p\cdot dx-dz=-\theta$. A second application has independent coordinate $P=x$, slope $X=p$, and height $P\cdot X-Z=z$. Thus $\mathcal L^2=\mathrm{id}$ exactly. The minus sign belongs to the contact-form multiplier. On the graph $z=f(x)$, its new base coordinate is $X=df(x)$, whose Jacobian is the Hessian of $f$. The inverse function theorem gives a transformed graph precisely where that Hessian is invertible. The contact image exists even when this graph condition fails.

**Solution 2.** Substituting in (2.1) gives

$$
X_z=z\partial_z+p\partial_p,\qquad
X_p=-\partial_x,\qquad
X_{xp}=-x\partial_x+p\partial_p.
$$

The contact brackets are $\{z,p\}_c=X_zp-p=0$, $\{z,xp\}_c=X_z(xp)-xp=0$, and $\{p,xp\}_c=-\partial_x(xp)=-p$. Hence

$$
[X_z,X_p]=0,\qquad [X_z,X_{xp}]=0,\qquad
[X_p,X_{xp}]=-X_p=\partial_x.
$$

Direct coefficient differentiation gives exactly these commutators. For example $[-\partial_x,-x\partial_x+p\partial_p]=\partial_x$. This also checks the bracket sign fixed in this lesson.

**Solution 3.** The transformed equation is $Z=-f(X)$. Its Legendrian condition is $(-f'(X)-P)dX=0$. Constant $X=c$ gives a vertical curve with $Z=-f(c)$ and arbitrary $P$, hence $z=cx+f(c)$ after applying the involution. The other analytic branch has $P=-f'(X)$; returning to $(x,z,p)$ gives (6.2). Differentiating the original Clairaut equation proves exhaustiveness for analytic solution germs: $(x+f'(p))p'=0$, and on a connected analytic germ one factor vanishes identically.

For $f(p)=p^2/2$, the envelope has $p=-x$ and $z=-x^2/2$. Its derivative is $-x=p$, and substitution gives $px+p^2/2=-x^2/2$. But $F_p=-x-p=0$ there, and (6.1) vanishes on that branch. Theorem 3.1 does not assert uniqueness there. The straight line $z=cx+c^2/2$ is tangent to the envelope at $x=-c$, illustrating precisely the degenerate projection and characteristic initial slope.

**Solution 4.** Put $F=p^2-z$ and use slopes $(q,p)$ in the order $(x,y)$. Then $F_z=-1$, $F_p=2p$, and $F_q=F_x=F_y=0$. Formula (3.2) on $E$ yields

$$
\dot x=0,\quad \dot y=-2p,\quad
\dot z=-2z,\quad \dot q=-q,\quad\dot p=-p.
$$

From initial coordinate $a$ on $y=0$ and initial slopes $q=g'(a)$, $p=\varepsilon\sqrt{g(a)}$, the solution is

$$
\begin{aligned}
x&=a,&p&=\varepsilon\sqrt{g(a)}e^{-t},&
q&=g'(a)e^{-t},\\
y&=2\varepsilon\sqrt{g(a)}(e^{-t}-1),&
z&=g(a)e^{-2t}.
\end{aligned}
$$

The $y$ derivative at $t=0$ is nonzero, so eliminate $(a,t)$ to get

$$
z(x,y)=\left(\sqrt{g(x)}+\frac{\varepsilon y}{2}\right)^2.
\tag{9.1}
$$

Its $y$ derivative is $\varepsilon(\sqrt g+\varepsilon y/2)$, whose square is (9.1). Its $x$ derivative is $(\sqrt g+\varepsilon y/2)g'/\sqrt g$, agreeing with the characteristic $q$ after substituting $e^{-t}=1+\varepsilon y/(2\sqrt g)$. Its initial value is $g$. The positivity of $g$ gives a real analytic square-root branch and makes the initial datum noncharacteristic. The result is local near $y=0$; this argument makes no uniqueness assertion for initial data where $g=0$.

**Solution 5.** If $X=a^i\partial_{x^i}+b\partial_z+c_i\partial_{p_i}$ and $W=b-p_ia^i$, then $\iota_Xd\theta=a^i dp_i-c_i dx^i$. Cartan's formula makes $\mathcal L_X\theta=dW+a^i dp_i-c_i dx^i$. Comparison with $\lambda\theta$ first gives $\lambda=W_z$, then $a^i=-W_{p_i}$, $c_i=W_{x^i}+p_iW_z$, and finally $b=W-p_iW_{p_i}$. Substitution verifies all components, proving both directions of the bijection for every $n$.

Evaluation on $X_V$ gives $\theta([X_W,X_V])=X_WV-W_zV$. Lie derivatives show that the commutator is contact, so the bijection identifies it with the field of that bracket. Its injectivity transfers the operator Jacobi identity to functions. Ordinary conservation would omit the $-F_zW$ term in the commuting condition. For $F=z-p_2$, $W=x^1$ and $V=p_1/p_2$ are ordinarily conserved by translation in $x^2$ and simultaneous scaling of $z,p$, while their bracket $1/p_2$ scales with weight $-1$. This proves the claimed failure and explains the corrected weighted statement.

## Historical reading and references

The following selected passages are transcribed from the public-domain German scan, with independent English translations by the writing AI. Formula typography and line breaks are normalized; historical spelling is retained. These selections introduce the three historical topics of this lesson; the remaining assigned section transcription is still being prepared. The scan confirms the printed chapter numbering: Chapter 8 treats function groups; the infinitesimal contact formulas belong to Chapters 14–15.

**Contact elements: Volume II, Chapter 1, §1, printed p. 6.**

> Wir bezeichnen daher jede Transformation in $x,y,y'$, welche die Pfaffsche Gleichung:
>
> $$dy-y'\,dx=0$$
>
> invariant lässt, als eine Berührungstransformation der Ebene $x,y$. Die erweiterten Punkttransformationen (4) können einfach als diejenigen Berührungstransformationen charakterisirt werden, welche Linienelemente mit demselben Punkte stets wieder in Linienelemente mit demselben Punkte überführen.

**Independent translation.** We therefore call every transformation in $x,y,y'$ that preserves the Pfaffian equation $dy-y'\,dx=0$ a contact transformation of the plane $x,y$. The prolonged point transformations (4) can be characterized simply as the contact transformations that always send line elements based at the same point to line elements based at the same point.

The source's $y'$ is the slope denoted by $p$ here. Its reference (4) is the ordinary point-prolongation formula. The source footnote following “Berührungstransformation” is omitted from this selected definition.

**The geometric integration problem: Volume II, Chapter 4, §23, printed p. 87.** The source has first written an ordinary solution graph as $z=F(x)$ with $p_i=\partial_iF$. Its generalization is:

> Es sollen überhaupt alle $(n+1)$-gliedrigen Gleichungensysteme:
>
> $$
> \Phi_1(z,x_1\cdots x_n,p_1\cdots p_n)=0,\quad\cdots\quad
> \Phi_{n+1}(z,x_1\cdots x_n,p_1\cdots p_n)=0
> $$
>
> bestimmt werden, welche die Pfaffsche Gleichung: $dz-p_1dx_1-\cdots-p_ndx_n=0$ erfüllen und welche dabei die Gleichung:
>
> $$(10')\qquad\Phi(z,x_1\cdots x_n,p_1\cdots p_n)=0$$
>
> umfassen.

**Independent translation.** The task is to determine all systems of $n+1$ equations in $(z,x,p)$ that satisfy the Pfaffian equation $dz-p_1dx_1-\cdots-p_ndx_n=0$ and also include the equation $(10')$, namely $\Phi(z,x,p)=0$.

In current language this seeks Legendrian integral submanifolds inside the equation hypersurface; graph solutions are those with regular $x$ projection. Theorem 3.1 states the rank and initial-data conditions used for our construction. The source's literature footnote is omitted from this selected problem statement.

**Characteristic functions: Volume II, Chapter 14, §64, Theorem 39, printed p. 253.**

> Jede infinitesimale Berührungstransformation:
>
> $$
> \zeta\frac{\partial f}{\partial z}
> +\sum_{i=1}^n\left(\xi_i\frac{\partial f}{\partial x_i}
> +\pi_i\frac{\partial f}{\partial p_i}\right)
> $$
>
> ist durch die Function:
>
> $$W=p_1\xi_1+\cdots+p_n\xi_n-\zeta,$$
>
> ihre sogenannte charakteristische Function vollständig bestimmt. Andrerseits ist jede beliebige Function $W(z,x,p)$ die charakteristische Function einer ganz bestimmten infinitesimalen Berührungstransformation, welche durch das Symbol:
>
> $$[Wf]-W\frac{\partial f}{\partial z}$$
>
> dargestellt wird.

**Independent translation.** Every infinitesimal contact transformation displayed above is completely determined by the function $W=p_1\xi_1+\cdots+p_n\xi_n-\zeta$, its characteristic function. Conversely, each arbitrary function $W(z,x,p)$ is the characteristic function of one definite infinitesimal contact transformation, represented by $[Wf]-W\,\partial f/\partial z$.

The bracket symbol in this quotation is Lie's notation. For the displayed field, our form gives $\theta(X)=\zeta-p_i\xi_i$, so $W_{\mathrm{Lie}}=-W_{\mathrm{course}}$. Converting that sign gives (2.1). The source's following normal-displacement example consequently has the opposite flow parameter from (6.5), while tracing the same parallel curves. The theorem's bibliographic footnote is omitted from this selection.

- Sophus Lie and Friedrich Engel, [*Theorie der Transformationsgruppen*, Volume II](https://archive.org/details/theotransformation02liesrich), Chapter 1, §§1–3, for contact elements and directrix equations; Chapter 4, §§21–23, especially printed p. 87, for the equation as a Legendrian integration problem; Chapter 7, §§44–46, printed pp. 171–176, for Jacobi and Poisson's theorem; Chapter 8, §47, printed pp. 178–180, for function groups; Chapter 14, §64, Theorem 39, printed p. 253, and Chapter 15 for contact generators and brackets. These are the historical and completeness references actually used.
- Václav Tryhuk and Veronika Chrastinová, [*On the Mapping of Jet Spaces*](https://www.atlantis-press.com/journals/jnmp/125951023), *Journal of Nonlinear Mathematical Physics* 17 (2010), 293–310, §3, Theorem 1, for the stated finite-order Bäcklund theorem.

All four assigned theorem topics are proved here, with the first-integral claim corrected by (4.1)–(4.3). Bäcklund's classification is stated with its locator, as permitted.
