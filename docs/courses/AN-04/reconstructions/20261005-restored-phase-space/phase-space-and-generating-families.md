# Phase space and generating families

An oscillatory kernel carries information about position and frequency together. Its phase determines a geometric relation between those variables; changing a phase can leave that relation unchanged. This lesson develops the geometry needed to recognize the relation, to find useful phase coordinates, and to tell a clean family from a singular one.

The exact earlier proofs are [finite linear algebra and inverse/implicit maps P2–P4](../20261004-free-stationary-phase/prerequisite-completions.md), finite calculus and compact parameter integration, and the constant-rank coordinate argument in [PH:F1](../20261004-free-intrinsic-graph/prerequisites/prescribed-phase-representation.md). That coordinate argument applies to any smooth map of constant rank. The companion [finite-coordinate flow proof](finite-coordinate-flows.md), imported from AN-03, proves existence, uniqueness, all smooth parameter derivatives and local inverse flows. Differential forms and flow pullbacks proves the form identities and fixed-time neighborhood assertion used below. Their proof locators and complete dependencies are recorded in the [proof map](proof-map.json).

[Stationary phase and critical manifolds](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md) explains the analytic use of normal rank and signature. The mathematical references include the author draft [Guillemin–Sternberg] and the edition [Hörmander III]. These readings support the exposition; every result used has a programme proof.

## 1. Signs fixed by the cotangent pairing

On a cotangent bundle \(T^*X\), the canonical one-form is

\[
\alpha_{(x,\xi)}(v)=\xi(d\pi(v)).
\]

In local coordinates, \(\alpha=\sum_j\xi_jdx_j\). We use

\[
\omega=d\alpha=\sum_jd\xi_j\wedge dx_j.
\tag{1.1}
\]

A symplectic manifold is a smooth manifold with a closed, nondegenerate two-form \(\omega\). A symplectomorphism \(F\) satisfies \(F^*\omega_2=\omega_1\). For a function \(p\), our Hamiltonian vector field and Poisson bracket are defined by

\[
\iota_{H_p}\omega=-dp,
\qquad \{p,q\}=H_pq.
\tag{1.2}
\]

Thus on \(T^*X\),

\[
H_p=\sum_j\left(
\partial_{\xi_j}p\,\partial_{x_j}
-\partial_{x_j}p\,\partial_{\xi_j}\right),
\qquad
\{p,q\}=\sum_j
\left(\partial_{\xi_j}p\partial_{x_j}q
-\partial_{x_j}p\partial_{\xi_j}q\right).
\tag{1.3}
\]

In particular \(\{\xi_j,x_k\}=\delta_{jk}\).

**Proposition 1.1 (Hamiltonian identities).** Hamiltonian flows preserve \(\omega\), and

\[
[H_p,H_q]=H_{\{p,q\}},
\qquad
\{p,\{q,r\}\}+\{q,\{r,p\}\}+\{r,\{p,q\}\}=0.
\tag{1.4}
\]

**Proof.** Cartan's formula gives \(\mathcal L_{H_p}\omega=d\iota_{H_p}\omega+\iota_{H_p}d\omega=-d^2p=0\). Differentiating the pullback by the flow proves preservation. Also,

\[
\iota_{[H_p,H_q]}\omega
=\mathcal L_{H_p}\iota_{H_q}\omega
-\iota_{H_q}\mathcal L_{H_p}\omega
=-d(H_pq).
\]

Nondegeneracy proves the commutator identity. Apply it to \(r\), expand the commutator, and use antisymmetry of the bracket to obtain the Jacobi identity. ∎

For a diffeomorphism \(f:X\to Y\), its cotangent lift is

\[
(x,\xi)\longmapsto
\left(f(x),(df_x)^{-T}\xi\right).
\tag{1.5}
\]

It preserves \(\alpha\), because \(((df_x)^{-T}\xi)(df_xv)=\xi(v)\), and hence preserves \(\omega\). This fixes the transpose and inverse in the frequency transformation.

## 2. Linear geometry and reduction

For a subspace \(W\) of a symplectic vector space \(V\), define

\[
W^\omega=\{v\in V:\omega(v,w)=0\text{ for every }w\in W\}.
\]

Nondegeneracy identifies \(V\) with its dual. Restriction to \(W\) is onto \(W^*\), so

\[
\dim W^\omega=\dim V-\dim W,
\qquad (W^\omega)^\omega=W.
\tag{2.1}
\]

The subspace is isotropic if \(W\subset W^\omega\), coisotropic if \(W^\omega\subset W\), and Lagrangian if \(W=W^\omega\). An isotropic subspace in dimension \(2n\) has dimension at most \(n\); a Lagrangian has dimension exactly \(n\).

**Lemma 2.1 (symplectic basis).** Every finite-dimensional symplectic vector space has even dimension and a basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\) with

\[
\omega(f_j,e_k)=\delta_{jk},
\qquad\omega(e_j,e_k)=\omega(f_j,f_k)=0.
\tag{2.2}
\]

**Proof.** Choose \(e_1\neq0\). Nondegeneracy gives \(f_1\) with \(\omega(f_1,e_1)=1\). Their span is a symplectic plane. Its symplectic orthogonal is a complementary subspace, and the form is nondegenerate there: a vector orthogonal to both summands is orthogonal to all of \(V\). Induct on the dimension. ∎

**Lemma 2.2 (a common Lagrangian complement).** Any two Lagrangian subspaces have a Lagrangian subspace transverse to both.

**Proof.** Choose symplectic coordinates with the first subspace vertical. Here is the basis-extension step explicitly. For its basis \(e_j\), choose \(g_i\) with \(\omega(g_i,e_j)=\delta_{ij}\), possible by nondegeneracy and independence. Set \(C_{ij}=\omega(g_i,g_j)\) and \(f_i=g_i+\tfrac12\sum_jC_{ij}e_j\). Then \(\omega(f_i,e_j)=\delta_{ij}\) and \(\omega(f_i,f_j)=C_{ij}+C_{ji}/2-C_{ij}/2=0\). These vectors give the required symplectic coordinates. Represent a basis of the second subspace by columns of \(\binom QP\), where \(Q,P\) are real \(n\times n\) matrices. The Lagrangian condition is \(Q^TP=P^TQ\), and the stacked matrix has full rank.

The graph \(p=tq\) is Lagrangian and transverse to the vertical subspace. It is transverse to the second subspace exactly when \(P-tQ\) is invertible. This determinant is a polynomial in \(t\) that is not identically zero: at \(t=i\),

\[
(P-iQ)^*(P-iQ)=P^TP+Q^TQ
\]

is positive definite. The equality uses \(Q^TP=P^TQ\); positivity uses full rank of \(\binom QP\). Choose a real \(t\) outside the finitely many zeros. ∎

**Proposition 2.3 (linear symplectic reduction).** If \(A\subset V\) is isotropic, the form on \(A^\omega\) descends to a symplectic form on \(A^\omega/A\). For every Lagrangian \(L\subset V\),

\[
L_{\mathrm{red}}=
\bigl((L\cap A^\omega)+A\bigr)/A
\tag{2.3}
\]

is Lagrangian in that quotient.

**Proof.** The radical of \(\omega|_{A^\omega}\) is \(A^\omega\cap(A^\omega)^\omega=A\). This proves the first claim.

Write \(\dim V=2n\), \(\dim A=a\), and \(k=\dim(L\cap A)\). The map \(L\to A^*\), \(v\mapsto\omega(v,\cdot)|_A\), has rank \(a-k\): its transpose has kernel \(A\cap L^\omega=A\cap L\). Hence \(\dim(L\cap A^\omega)=n-a+k\). Passing to the quotient removes its kernel \(L\cap A\), of dimension \(k\), so \(\dim L_{\mathrm{red}}=n-a\), half the quotient dimension. The form vanishes on this image because it vanishes on \(L\). ∎

## 3. Local coordinates from closedness

**Theorem 3.1 (Darboux).** Near every point of a symplectic manifold of dimension \(2n\), there are coordinates \((x,\xi)\) in which \(\omega=\sum_jd\xi_j\wedge dx_j\).

**Proof.** Lemma 2.1 gives initial coordinates making the form at the origin equal to the constant form \(\omega_0\). Put \(\beta=\omega-\omega_0\). On a small star-shaped neighborhood define a one-form

\[
\gamma_x(v)=\int_0^1t\,\beta_{tx}(x,v)\,dt.
\]

The radial homotopy formula, proved in companion F3, gives \(d\gamma=\beta\). To verify it, differentiate the pullbacks of \(\beta\) by \(x\mapsto tx\), use Cartan's formula, and integrate from zero to one; the pullback at zero vanishes for a two-form and \(d\beta=0\). Since \(\beta(0)=0\), \(\gamma=O(|x|^2)\).

All forms \(\omega_t=\omega_0+t\beta\), \(0\leq t\leq1\), are nondegenerate on a sufficiently small common neighborhood. Define \(V_t\) by \(\iota_{V_t}\omega_t=-\gamma\). Its local flow \(\Psi_t\) exists through time one on a common neighborhood by companion F4, and fixes the origin. Then

\[
\frac d{dt}\Psi_t^*\omega_t
=\Psi_t^*(\beta+d\iota_{V_t}\omega_t)=0.
\]

Thus \(\Psi_1^*\omega=\omega_0\), giving the desired coordinates. ∎

The volume form \(\omega^n/n!\) fixes an orientation and is preserved by symplectomorphisms. Its associated density, rather than a coordinate orientation chosen separately, has Jacobian one in symplectic coordinates.

A smooth submanifold is isotropic, coisotropic or Lagrangian when its tangent spaces have that property. A section \(\xi=g(x)\) of a cotangent bundle is Lagrangian precisely when the one-form \(\sum_jg_jdx_j\) is closed. Locally it is \(df\), by the degree-one radial homotopy formula. Thus the graph is \(\xi=df(x)\).

More generally, any Lagrangian can locally be made the zero section by a symplectomorphism. First use Darboux coordinates and a linear symplectic change making its tangent plane horizontal. The inverse function theorem makes it a local graph \(df\); the canonical translation \((x,\xi)\mapsto(x,\xi-df(x))\) takes it to the zero section. This is a statement near a point; it does not assert a global neighborhood identification along an arbitrary submanifold.

## 4. Homogeneity and the contact slice

Suppose a free smooth dilation action \(m_t\), \(t>0\), satisfies \(m_t^*\omega=t\omega\). Let \(E\) be its infinitesimal radial vector field, using the parameter \(\log t\). Then

\[
\alpha=\iota_E\omega,
\qquad d\alpha=\omega,
\qquad\alpha(E)=0.
\tag{4.1}
\]

Indeed, \(\mathcal L_E\omega=\omega\), and Cartan's formula proves the middle identity. On a cotangent bundle, \(E=\sum\xi_j\partial_{\xi_j}\), so this recovers \(\alpha=\sum\xi_jdx_j\).

The field \(E\) is nonzero: if it vanished at a point, uniqueness for its flow would make that orbit locally constant, contradicting the free action. Choose a coordinate hyperplane transverse to \(E\). The map \((u,y)\mapsto m_{e^u}(y)\) has invertible derivative at \((0,y)\), so P3 gives the local slice coordinates used below. In particular this case has \(n\geq1\).

**Proposition 4.1.** If \(\Lambda\) is conic and Lagrangian, then \(\alpha|_\Lambda=0\). On a local slice \(Y\) transverse to the dilation orbits, \(\beta=\alpha|_Y\) is a contact form:

\[
\beta\wedge(d\beta)^{n-1}\neq0.
\tag{4.2}
\]

**Proof.** The radial vector \(E\) is tangent to \(\Lambda\), so \(\alpha(v)=\omega(E,v)=0\) for its tangent vectors. Near a transverse slice use coordinates \((u,y)\), where dilations translate \(u\). Homogeneity gives \(\alpha=e^u\beta\). Therefore

\[
\omega=e^u(du\wedge\beta+d\beta),
\qquad
\omega^n=ne^{nu}du\wedge\beta\wedge(d\beta)^{n-1}.
\]

Nondegeneracy proves (4.2). ∎

Changing the slice multiplies the contact form by a positive smooth function. The resulting contact hyperplanes are intrinsic. Global quotient assertions additionally require a well-behaved orbit space; the local slice calculation needs only transversality.

## 5. Phases and the critical map

Let \(\Gamma\subset X\times(\mathbb R^N\setminus0)\) be an open cone in the second variable. A real smooth function \(\phi\) is a homogeneous phase if it is homogeneous of degree one in \(\theta\) and \(d\phi\neq0\). Its critical set in the phase variables is

\[
C_\phi=\{(x,\theta):\partial_\theta\phi=0\}.
\]

It is nondegenerate if the \(N\) covectors \(d(\partial_{\theta_j}\phi)\) are independent on \(C_\phi\). It is clean of excess \(e\) if \(C_\phi\) is a smooth manifold,

\[
T C_\phi=\ker d(\partial_\theta\phi),
\qquad \dim C_\phi=\dim X+e.
\tag{5.1}
\]

Thus the rank is \(N-e\). Smoothness of the set alone is not this condition.

**Theorem 5.1 (the geometric content of a clean phase).** For a clean phase, the map

\[
\kappa_\phi:C_\phi\longrightarrow T^*X\setminus0,
\qquad (x,\theta)\longmapsto(x,\partial_x\phi)
\tag{5.2}
\]

has constant rank \(n=\dim X\), with fibers locally of dimension \(e\). Each local image is a conic Lagrangian submanifold. In the nondegenerate case it is a local diffeomorphism onto that image.

**Proof.** On \(C_\phi\), nonvanishing of \(d\phi\) means \(\partial_x\phi\neq0\). A tangent vector in the kernel of \(d\kappa_\phi\) has \(\delta x=0\),

\[
\phi_{x\theta}''\delta\theta=0,
\qquad\phi_{\theta\theta}''\delta\theta=0.
\]

The stacked matrix in these equations is the transpose of \(d(\phi_\theta')\); symmetry of the Hessian is essential here. It has rank \(N-e\), so its kernel has dimension \(e\). The clean tangent condition shows that these are exactly the kernel vectors in \(TC_\phi\). Thus the critical map has rank \((n+e)-e=n\).

The constant-rank coordinate proof in PH:F1 gives a local smooth image. In the homogeneous setting choose a small neighborhood transverse to the radial direction and saturate it by positive dilation; this gives the conic local branch meant here. On the critical set,

\[
\kappa_\phi^*\alpha=d\phi|_{C_\phi},
\qquad\kappa_\phi^*\omega=0.
\]

Surjectivity onto its image tangent space shows that the image is isotropic; dimension \(n\) makes it Lagrangian. Homogeneity makes the image conic. For \(e=0\), the kernel is zero, proving the last assertion. ∎

Euler's identity gives \(\phi=\theta\cdot\phi_\theta'=0\) on the critical set. Consequently the pullback of \(\alpha\) in this homogeneous case is zero, consistently with Proposition 4.1.

## 6. Constructing phases with as few variables as possible

**Theorem 6.1 (mixed generating function).** Let \(\Lambda\subset T^*X\setminus0\) be a smooth conic Lagrangian. At \(\rho\in\Lambda\), let \(k\) be the dimension of the vertical tangent space \(T_\rho\Lambda\cap\ker d\pi\). After a linear choice of base coordinates \(x=(x_I,x_J)\), with \(|J|=k\), the variables \((x_I,\xi_J)\) are coordinates on \(\Lambda\) near \(\rho\). There is a degree-one homogeneous function \(S(x_I,\theta)\) such that

\[
\phi(x,\theta)=S(x_I,\theta)+x_J\cdot\theta,
\qquad \theta\in\mathbb R^k\setminus0,
\tag{6.1}
\]

is a nondegenerate phase parametrizing \(\Lambda\) there. No nondegenerate phase with fewer than \(k\) variables can do so.

**Proof.** Write \(P=d\pi(T_\rho\Lambda)\), of dimension \(n-k\). The vertical tangent space is the annihilator \(P^\perp\). To see this, pair a vertical tangent \((0,\eta)\) with any tangent \((v,\zeta)\) using \(\omega\): it gives \(\eta(v)=0\). This yields inclusion in \(P^\perp\), and both spaces have dimension \(k\). Choose base coordinates making \(P\) the \(x_I\) plane. Then the vertical tangent is the \(\xi_J\) plane.

The differential of \((x_I,\xi_J)\) on \(T_\rho\Lambda\) is injective: a kernel vector has zero base component, hence is vertical, and its \(\xi_J\) component is also zero. It is an isomorphism by dimension. The inverse function theorem gives the claimed coordinates. The radial tangent is a nonzero vertical vector, so \(k\geq1\) and \(\xi_J\neq0\) at \(\rho\). Shrink to a conic neighborhood where that remains true.

On \(\Lambda\), \(\alpha=0\). Hence

\[
0=\xi_I\,dx_I+\theta\,dx_J
=d(x_J\cdot\theta)+\xi_I\,dx_I-x_J\,d\theta.
\]

Set \(S=-x_J\cdot\theta\), regarding \(x_J\) as a function of \((x_I,\theta)\). Then

\[
dS=\xi_I\,dx_I-x_J\,d\theta,
\qquad S_{x_I}'=\xi_I,
\qquad S_\theta'=-x_J.
\]

Conicity makes \(x_J\) degree zero, so \(S\) is degree one. The phase equations in (6.1) are \(S_\theta'+x_J=0\), and their differentials are independent because their \(x_J\) derivative is the identity. The critical map recovers exactly \(\xi_I=S_{x_I}'\), \(\xi_J=\theta\), and \(x_J=-S_\theta'\).

If a nondegenerate phase with \(N\) variables parametrizes the same Lagrangian, its critical map is a tangent isomorphism. Every vertical tangent is therefore the image of a critical tangent with \(\delta x=0\), a subspace of the \(N\)-dimensional phase-variable space. Thus \(k\leq N\). ∎

**Theorem 6.2 (a frequency generating function after a base change).** Base coordinates can also be chosen so that \(\xi\) alone parametrizes \(\Lambda\) near \(\rho\). In those coordinates,

\[
\Lambda=\{(H'(\xi),\xi)\},
\qquad
\phi(x,\theta)=x\cdot\theta-H(\theta),
\tag{6.2}
\]

where \(H\) is smooth and homogeneous of degree one. For the fixed coordinates and Lagrangian, \(H\) is unique.

**Proof.** Choose coordinates \(y\) with \(y(\pi\rho)=0\) and \(\rho=(0,dy_1)\). Lemma 2.2 supplies a Lagrangian plane transverse to both \(T_\rho\Lambda\) and the vertical plane. Such a plane is the tangent graph \(\delta\eta=A\delta y\) of a symmetric matrix \(A\): symmetry is exactly its Lagrangian condition.

Use new base coordinates \(x_1=y_1+y^TAy/2\) and \(x_j=y_j\), \(j>1\). Their Jacobian at zero is the identity. The graph of \(dx_1\), passing through \(\rho\), has precisely the chosen tangent plane. In the induced cotangent coordinates, this graph is the constant-frequency section \(\xi=(1,0,\ldots,0)\). Transversality says that \(d\xi:T_\rho\Lambda\to\mathbb R^n\) is invertible.

Write \(x=g(\xi)\) using the inverse function theorem and conicity. Define \(H(\xi)=g(\xi)\cdot\xi\). Since \(\alpha|_\Lambda=\xi\cdot dg=0\), differentiation gives \(dH=g\cdot d\xi\), so \(H'=g\). Conicity makes \(g\) degree zero and \(H\) degree one. The critical equations for (6.2) are \(x=H'(\theta)\), whose differentials are independent in \(x\). Finally, any degree-one function with derivative \(g\) satisfies Euler's identity \(H=\xi\cdot g\), proving uniqueness. ∎

The coordinate change in this theorem is induced by a base diffeomorphism. This is useful when a distribution is being expressed in ordinary position coordinates, rather than after an arbitrary symplectic transformation.

## 7. Kernel relations and clean composition

A canonical relation from a symplectic manifold \(S_2\) to \(S_1\) is a Lagrangian submanifold of \(S_1\times S_2\) for the form \(\omega_1-\omega_2\). A symplectomorphism has such a graph: pulling back this form to its graph gives \(F^*\omega_1-\omega_2=0\), and the dimensions agree.

A kernel phase \(\phi(x,y,\theta)\) determines the relation

\[
C=\{(x,\phi_x';y,-\phi_y'):\phi_\theta'=0\}.
\tag{7.1}
\]

The minus sign comes from the negative form on the input cotangent bundle. Equivalently, the kernel Lagrangian in \(T^*(X\times Y)\) has covectors \((\phi_x',\phi_y')\), and the input covector is then reflected. To obtain a relation in \((T^*X\setminus0)\times(T^*Y\setminus0)\), both \(\phi_x'\) and \(\phi_y'\) must be nonzero on the part of the critical set in question.

**Theorem 7.1 (local clean composition).** Let \(C_{12}\subset S_1\times S_2\) and \(C_{23}\subset S_2\times S_3\) be canonical relations. Suppose

\[
F=(C_{12}\times C_{23})\cap
(S_1\times\operatorname{diag}S_2\times S_3)
\]

is a clean intersection, meaning that it is a smooth submanifold and its tangent space is the intersection of the two tangent spaces. The projection \(F\to S_1\times S_3\) has rank \((\dim S_1+\dim S_3)/2\). Each local image is Lagrangian for \(\omega_1-\omega_3\). Its fiber dimension is the excess

\[
e=\dim F-\tfrac12(\dim S_1+\dim S_3).
\tag{7.2}
\]

**Proof.** At a point of the fiber product take the symplectic vector space with form \(\omega_1-\omega_2+\omega_2-\omega_3\). The product tangent \(L=TC_{12}\times TC_{23}\) is Lagrangian. The middle diagonal

\[
A=\{0\}\times\operatorname{diag}(TS_2)\times\{0\}
\]

is isotropic. Its symplectic orthogonal imposes equality of the two middle tangent vectors. Clean intersection says that \(TF=L\cap A^\omega\). The projection is the quotient by \(A\), so Proposition 2.3 identifies its differential image as a Lagrangian in \(TS_1\times TS_3\). This gives the stated constant rank. The constant-rank theorem gives a local smooth image, and (7.2) follows from rank-nullity. ∎

This theorem is local. Different local images can be different branches. Proper projection makes fibers compact and the image closed, but a global embedded relation still requires an embedded-image hypothesis or a separate branch description.

**Proposition 7.2 (adding phases).** Suppose nondegenerate phases \(\phi(x,y,\theta)\) and \(\psi(y,z,\tau)\) parametrize the two relations in punctured cotangent bundles, with both output and input covectors nonzero, and their fiber product is clean. Then

\[
\Phi(x,z;y,\theta,\tau)=
\phi(x,y,\theta)+\psi(y,z,\tau)
\tag{7.3}
\]

is a clean generating family for the local composition, with the same excess. Here dilations scale \(\theta,\tau\) and leave \(y\) fixed.

**Proof.** The phase-critical equations are

\[
\phi_\theta'=0,\qquad\psi_\tau'=0,
\qquad\phi_y'+\psi_y'=0.
\]

The first two identify the phase-critical manifolds with their canonical relations. The third matches the output frequency of the second with the input frequency of the first. Thus their solution set identifies with \(F\). Clean intersection identifies its tangent space with the kernel of the differentiated equations. The critical map sends it to the composed relation. The dimension definition of excess gives (7.2).

If one wants ordinary homogeneous coordinates for all the integration parameters, set \(r=(|\theta|^2+|\tau|^2)^{1/2}\), and replace \(y\) by \(v=ry\). The variables \((v,\theta,\tau)\) all scale with degree one; (7.3), with \(y=v/r\), is homogeneous of degree one. This change has invertible differential for \(r>0\), so clean rank and excess are preserved. ∎

## 8. Models and exercises with solutions

**A conormal phase.** For \(Y=\{x_J=0\}\), the phase \(x_J\cdot\theta\) has independent critical equations \(x_J=0\). Its image is \(N^*Y\setminus0\): the base lies on \(Y\), the tangential frequencies vanish, and the normal frequencies are \(\theta\neq0\). It uses exactly \(\operatorname{codim}Y\) variables, the minimum in Theorem 6.1.

**A redundant clean phase.** On \(X=\mathbb R\), take \(\phi(x,\theta_1,\theta_2)=x\theta_1\) on a cone where \(\theta_1\neq0\). The critical equations are \((x,0)=0\), of rank one. The critical manifold has dimension two, so the excess is one. Its image is the nonzero cotangent fiber at zero; its fibers vary in \(\theta_2\). The redundant direction is a geometric excess, not another output frequency.

**Exercise 8.1 (input sign; introductory).** Find the canonical relation of \(\phi(x,y,\theta)=(x-y)\cdot\theta\), with \(\theta\neq0\).

**Solution.** The critical equation is \(x=y\). The output covector is \(\theta\), and the input covector is \(-(-\theta)=\theta\). The relation is \(\{(x,\theta;x,\theta)\}\), the identity. Omitting the input reflection would give the wrong relation.

**Exercise 8.2 (a smooth zero set that is not clean; intermediate).** On \(X=\mathbb R^2\), consider

\[
\phi(x,y,\theta_1,\theta_2)=x^2\theta_1+y\theta_2
\]

on a cone where \(\theta_2\neq0\). Is it a clean phase?

**Solution.** Its full differential never vanishes there, since \(\phi_y'=\theta_2\neq0\). The phase-critical set is \(x=y=0\), a smooth manifold of dimension two. But \(d(\phi_\theta')=(d(x^2),dy)\) has rank one there. Its kernel allows arbitrary \(\delta x\), whereas the tangent space of the critical set has \(\delta x=\delta y=0\). Thus (5.1) fails. The critical image has \(x=y=0\), \(\xi_x=0\), \(\xi_y=\theta_2\), only one dimension, so it cannot be Lagrangian in \(T^*\mathbb R^2\).

**Exercise 8.3 (a coordinate-independent graph; intermediate).** Verify directly that the cotangent lift (1.5) has a canonical graph, and explain why replacing \((df)^{-T}\) by \((df)^T\) fails in general.

**Solution.** Preservation of \(\alpha\) was proved by the dual pairing. Differentiation gives preservation of \(\omega\), hence its graph is canonical. For the one-dimensional map \(f(x)=2x\), the incorrect frequency formula would be \(\eta=2\xi\); then \(d\eta\wedge d(2x)=4d\xi\wedge dx\). The correct formula is \(\eta=\xi/2\), which preserves the form.

**Exercise 8.4 (a composition with excess; advanced).** Let \(L_1\subset S_1\), \(L_2\subset S_2\), and \(L_3\subset S_3\) be Lagrangian submanifolds. Compose \(C_{12}=L_1\times L_2\) with \(C_{23}=L_2\times L_3\). Compute the local fiber and excess.

**Solution.** The fiber product is \(L_1\times L_2\times L_3\), with projection to \(L_1\times L_3\). Its tangent space is exactly the matching-middle tangent intersection, so it is clean. The fiber is \(L_2\), and the excess is \(\dim L_2=\dim S_2/2\). The image is Lagrangian for \(\omega_1-\omega_3\). Compactness of these fibers requires a further condition on \(L_2\); clean rank alone supplies none.

**Exercise 8.5 (frequency generating function; advanced).** For \(H(\theta)=|\theta|\), compute the Lagrangian generated by \(x\cdot\theta-H(\theta)\). Describe its base projection and vertical tangent dimension.

**Solution.** The critical equation is \(x=\theta/|\theta|\), so

\[
\Lambda=\{(x,r x):|x|=1,\ r>0\}.
\]

The base image is the unit sphere. The derivative of \(\theta\mapsto\theta/|\theta|\) has kernel the radial line, so the vertical tangent dimension is one. A local phase using one variable therefore exists by Theorem 6.1, although the displayed phase uses \(n\) variables. This is one component of the conormal bundle of the sphere.

## References

- [Guillemin–Sternberg] Victor Guillemin and Shlomo Sternberg, *Semi-classical Analysis*, January 13, 2010. [Online reading](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
- [Hörmander III] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, Springer, 1994.
- Lars Hörmander, *Fourier integral operators. I*, Acta Mathematica 127 (1971), Section 3.1, especially the generating-function results used in the programme's earlier geometry companion. [Free primary-source reading](https://projecteuclid.org/journals/acta-mathematica/volume-127/issue-none/Fourier-integral-operators-I/10.1007/BF02392052.pdf).

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restored and checked against the exact programme prerequisites by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original lesson and restoration additions: CC0. The separately linked AN-03 flow companion is also original CC0 text.*
