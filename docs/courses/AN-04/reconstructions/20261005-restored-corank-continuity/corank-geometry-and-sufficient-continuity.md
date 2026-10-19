# Corank geometry and sufficient continuity

The graph estimate has a geometric extension. A canonical relation can have directions that disappear under one projection. At a point these directions split into two isotropic kernels, while the remaining quotient is a symplectic graph. The total kernel dimension changes the order of the partial Fourier amplitude by one quarter of that dimension.

We use the symplectic signs, reduction and conic one-form identity from [Phase space and generating families](../20261005-restored-phase-space/phase-space-and-generating-families.md), the prescribed-phase converse from [Recognizing a Lagrangian distribution intrinsically](../20261005-restored-intrinsic-regularity/intrinsic-lagrangian-regularity.md), and the graph quantizations, parametrices and quantitative norm estimate from [Graph operators, continuity and Egorov](../20261005-restored-graph-egorov/graph-operators-continuity-and-egorov.md). The ordinary FIO composition and smooth-kernel ideal are those of [Kernels, adjoints and clean composition](../20261005-restored-analytic-composition/clean-composition-of-fourier-integral-operators.md). The complete [finite-coordinate flow proof, Sections 17.1–17.7](../20261005-restored-phase-space/finite-coordinate-flows.md), supplies actual smooth flows, parameter derivatives, variational equations, continuation and coordinate compatibility. The [form and pullback companion F0–F4](../20261005-restored-phase-space/differential-forms-and-flow-pullbacks.md) proves Cartan's formula, time-dependent pullback differentiation and the common time-one neighborhood. [Measure and integration M3–M7](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) proves convergence, product integration, norm inequalities, completeness and compact smooth density; the [Fourier companion L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) proves the exact Fourier conventions. The [existing FIO mapping proof W2–W6](../20261004-free-canonical-composition/fio-sobolev-mapping.md) supplies the uniform graph-family estimates and support-controlled Sobolev reconstruction. Its separate base-slicing argument retains its own base-submersion hypotheses; the homogeneous coordinate argument below proves the present radial-hypothesis version. The [proof map](proof-map.json) records the exact current dependencies.

The primary source is the reprint of Hörmander IV, corrected second printing (1994), [§25.3], Lemma 25.3.6, Proposition 25.3.7 and Theorem 25.3.8. The supporting homogeneous-coordinate construction is a case of [Hörmander III, §21.1], in its reprint of the corrected second printing (1994). We prove the case with a prescribed tangent isomorphism below. Extending an already prescribed collection of canonical *functions*, or straightening an entire coisotropic submanifold, imposes additional requirements and remains separate from this case. All symbols here are ordinary \(S_{1,0}\) symbols. All operator assertions retain compact input supports, local output estimates and the full nonzero-covector closure convention.

## 1. A linear relation has two kernels and one symplectic graph

Let \((S_j,\omega_j)\) be symplectic vector spaces of dimensions \(2n_j\), and let \(G\subset S_1\oplus S_2\) be Lagrangian for \(\omega_1-\omega_2\). Define
\[
K_1=\{v:(v,0)\in G\},\qquad
K_2=\{w:(0,w)\in G\},\qquad
a=\dim K_1,\quad b=\dim K_2.
\tag{1.1}
\]
These are the directions invisible to the opposite projection. The kernel of \(G\to S_1\) has dimension \(b\), and the kernel of \(G\to S_2\) has dimension \(a\).

**Theorem 1.1 (linear splitting).** There are symplectically orthogonal decompositions
\[
S_j=W_j\oplus V_j
\tag{1.2}
\]
such that \(K_j\) is Lagrangian in \(W_j\), and
\[
G=(K_1\oplus0)\oplus
\operatorname{graph}(\chi_0:V_2\to V_1)\oplus(0\oplus K_2),
\tag{1.3}
\]
where \(\chi_0\) is a symplectic linear isomorphism. The common pulled-back form \(\sigma_G=\pi_1^*\omega_1=\pi_2^*\omega_2\) has
\[
\operatorname{rad}\sigma_G=(K_1\oplus0)\oplus(0\oplus K_2),
\quad
\operatorname{rank}\sigma_G=2n,
\quad
\operatorname{corank}\sigma_G=a+b,
\tag{1.4}
\]
where \(n=n_1-a=n_2-b\). Corank means the dimension of the form's radical on \(G\), not its codimension in the ambient product.

**Proof.** Isotropy of \(G\) makes \(K_j\) isotropic and gives \(\pi_jG\subset K_j^{\omega_j}\). In fact these images equal the indicated orthogonals. If \(v\) is orthogonal to \(\pi_1G\), then \((v,0)\) is orthogonal to \(G\) for the signed product form. Since \(G\) is Lagrangian, \((v,0)\in G\), so \(v\in K_1\). Thus \((\pi_1G)^{\omega_1}=K_1\), and taking a second orthogonal gives \(\pi_1G=K_1^{\omega_1}\). The same argument applies on the other side.

Rank-nullity for the first projection now gives
\[
n_1+n_2-b=2n_1-a,
\qquad n_1-a=n_2-b=n.
\tag{1.5}
\]
The quotient \(K_j^{\omega_j}/K_j\) is symplectic. Choose any linear section of its quotient map, with image \(V_j\). The restricted form is nondegenerate on \(V_j\), because it is the quotient form under this isomorphism. Consequently \(W_j=V_j^{\omega_j}\) is a symplectic complement, contains \(K_j\), and has dimension \(2\dim K_j\). The isotropic \(K_j\) is therefore Lagrangian in \(W_j\).

Pass \(G\) to the two quotients. Each projection of the resulting relation is onto. It is one-to-one: if its first class is zero, subtract a vector in \(K_1\oplus0\); the remaining vector has first component zero, and its second component is in \(K_2\). Thus its second class is also zero. The quotient relation is a graph. Isotropy says that its isomorphism preserves the two quotient symplectic forms. With our chosen sections, subtracting the two kernel components from any element of \(G\) gives (1.3).

Finally, a vector \((v,w)\in G\) in the radical of \(\sigma_G\) has \(v\) orthogonal to \(\pi_1G=K_1^{\omega_1}\), hence \(v\in K_1\). The second description of the same form gives \(w\in K_2\). Conversely both kernel summands are in the radical. This proves (1.4). ∎

For a smooth canonical relation \(C\), apply the theorem to \(G=T_cC\). It gives the pointwise projection ranks
\[
\operatorname{rank}d\pi_1=n_1+n,
\qquad\operatorname{rank}d\pi_2=n_2+n.
\tag{1.6}
\]
No constant-rank assumption is needed for these identities at a point. Smooth projection images and their characteristic foliations require a constant-rank argument when they are used later.

## 2. Homogeneous Darboux coordinates can preserve a chosen tangent map

A conic neighborhood is the product of a transverse slice and positive dilation rays, with action \(M_t\) satisfying \(M_t^*\omega=t\omega\). Its radial field \(R\) is nonzero. Such neighborhoods are available in the punctured cotangent bundles used here. Cartan's formula gives the degree-one primitive
\[
\lambda=\iota_R\omega,\qquad d\lambda=\omega.
\tag{2.1}
\]

**Theorem 2.1 (homogeneous coordinates with fixed tangent data).** At \(p\) let \(L:T_pS\to T_{(0,e_1)}(T^*\mathbb R^n)\) be a symplectic linear isomorphism taking \(R_p\) to the standard radial vector at \((0,e_1)\). There is a homogeneous local symplectic coordinate map taking \(p\) to \((0,e_1)\), whose differential is \(L\).

**Proof: initial homogeneous coordinates.** Choose a local hypersurface transverse to \(R\), and a flow coordinate \(r>0\) with \(r(p)=1\) and \(Rr=r\). Functions on the hypersurface extend to degree-zero functions along its rays. The intended differentials of \(x_j\), prescribed by \(L\), annihilate \(R_p\). The intended \(d\xi_1\) takes value one on \(R_p\), and \(d\xi_j\), \(j>1\), take value zero there. Choose functions \(x_j(z)\), \(b_j(z)\), \(j>1\), on the transverse surface, with zero values and the required transverse differentials; choose \(b_1(z)\) with value one and transverse differential correcting that of \(r\). Set
\[
\xi_j=r b_j(z).
\]
Then \(x\) has degree zero and \(\xi\) degree one, and all coordinate differentials at \(p\) equal those prescribed by \(L\). Their independence gives a homogeneous local chart by the inverse function theorem. The transverse slice and flow chart are exactly those proved in the phase-space lesson, Section 4: the map from a slice and flow time has independent derivatives, and uniqueness identifies the flow with dilation. Exponentiating its time coordinate gives \(r\). This also verifies the smooth homogeneous extension used here. In this chart the original form, still denoted \(\omega\), agrees at \(p_0=(0,e_1)\) with \(\omega_0=\sum d\xi_j\wedge dx_j\), and the radial field is the standard \(R_0=\sum\xi_j\partial_{\xi_j}\).

**A primitive that vanishes to second order.** Put
\[
\beta=\omega-\omega_0,\qquad
\alpha=\iota_{R_0}\beta.
\]
Both forms have degree one, \(\beta(p_0)=0\), and \(d\alpha=\beta\). Also \(\alpha(p_0)=0\). In ordinary local coordinates, the first derivative matrix of the coefficient vector of \(\alpha\) is symmetric at \(p_0\), because \(d\alpha(p_0)=0\). Denote this symmetric matrix by \(C\). The identity \(\mathcal L_{R_0}\alpha=\alpha\), evaluated at a point where \(\alpha=0\), gives
\[
C R_0(p_0)=0.
\tag{2.2}
\]

On the cone \(\xi_1>0\) put \(r=\xi_1\) and \(z=(x,\xi_2/\xi_1,\ldots,\xi_n/\xi_1)\). Here \(z(p_0)=0\) and \(\ker dz_{p_0}=\mathbb R R_0(p_0)\). Symmetry and (2.2) let us write \(C=(dz)^T C_z(dz)\) for a symmetric matrix on the transverse \(z\) variables. The degree-one function
\[
f(r,z)=\tfrac12 r z^T C_z z
\tag{2.3}
\]
has value and first derivative zero at \(p_0\), and Hessian exactly \(C\). Consequently
\[
\gamma=\alpha-df,
\qquad d\gamma=\beta,
\qquad \gamma(p_0)=0,\quad D\gamma(p_0)=0.
\tag{2.4}
\]
The subtraction changes the primitive, while retaining its homogeneity and the two-form.

**Homogeneous Moser flow.** Set \(\omega_t=\omega_0+t\beta\), \(0\leq t\leq1\). These forms are nondegenerate on a sufficiently small common neighborhood of \(p_0\); their homogeneity extends that neighborhood along its rays. Define
\[
\iota_{V_t}\omega_t=-\gamma.
\tag{2.5}
\]
Since \(\gamma\) vanishes to second order, so does \(V_t\). The full smooth flow and common-neighborhood arguments NF17–NF20 and F4 give its local flow \(\Psi_t\) through time one on one smaller neighborhood. Indeed the constant trajectory at \(p_0\) exists throughout the compact time interval; finitely many open pieces of its solution domain give one common neighborhood of initial values. Thus \(\Psi_t(p_0)=p_0\). The variational equation from NF12 gives \(\partial_t d\Psi_t(p_0)=DV_t(p_0)d\Psi_t(p_0)=0\), with initial value identity, so \(d\Psi_t(p_0)=I\). Applying \(\mathcal L_{R_0}\) to (2.5) and using degree one on both sides gives \([R_0,V_t]=0\). The flow therefore commutes with dilations wherever both sides are defined: differentiating the dilation pullback of \(V_t\) gives its bracket with \(R_0\), which is zero, and uniqueness of the original time-dependent ODE identifies the two flowed curves. Extend from a smaller transverse slice by dilation. The same construction for the inverse flow makes this extension a smooth homogeneous local diffeomorphism on its conic domain.

As in the ordinary Darboux proof,
\[
\frac d{dt}\Psi_t^*\omega_t
=\Psi_t^*(\beta+d\iota_{V_t}\omega_t)=0.
\tag{2.6}
\]
Thus \(\Psi_1^*\omega=\omega_0\). The inverse flow, used as coordinates after the initial chart, gives the required homogeneous symplectic map. Its differential retains \(L\), because the flow differential at the marked point is identity. ∎

Vanishing of \(\beta\) at a point alone does not make the radial primitive vanish to second order there. The exact Hessian correction (2.3) is what preserves the chosen tangent map in this argument.

## 3. The radial hypothesis selects a shared graph direction

For a conic canonical relation the paired radial vector \((R_1,R_2)\) belongs to \(T_cC\). The condition in the normal form is that the *individual* vectors \((R_1,0)\) and \((0,R_2)\) do not belong to \(T_cC\). In the notation of Theorem 1.1, this says
\[
R_1\notin K_1,\qquad R_2\notin K_2.
\tag{3.1}
\]
These two exclusions are equivalent, since subtracting one individual vector from the paired vector gives the other.

There is also a one-form formulation. On \(G=T_cC\), the two restricted canonical one-forms coincide:
\[
\lambda_C(v,w)=\omega_1(R_1,v)=\omega_2(R_2,w).
\tag{3.2}
\]
This follows by pairing the radial tangent with any tangent in the signed Lagrangian product. Since \(\pi_1G=K_1^{\omega_1}\), the form (3.2) vanishes identically exactly when \(R_1\in K_1\). Thus (3.1) is equivalent to \(\lambda_C\neq0\) as a covector on \(T_cC\). The shared reduced symplectic space consequently has positive dimension: \(n\geq1\).

**Theorem 3.1 (radial-compatible tangent normal form).** Under (3.1), choose homogeneous symplectic coordinates separately on the two sides, with the marked points equal to \((0,e_1)\). Split
\[
x=(x',x''),\quad y=(y',y''),\qquad
x',y'\in\mathbb R^n,\quad x''\in\mathbb R^a,\quad y''\in\mathbb R^b.
\]
At the marked point the tangent relation is
\[
\delta x'=\delta y',\qquad
\delta\xi'=\delta\eta',\qquad
\delta\xi''=0,\qquad \delta\eta''=0.
\tag{3.3}
\]
The double-prime base tangent components are unrestricted.

**Proof.** The radial vectors are in \(K_j^{\omega_j}\), because the paired vector is in \(G\). Their quotient classes are nonzero by (3.1). Choose the quotient sections in Theorem 1.1 so that \(V_j\) contains the actual \(R_j\). This is possible by first choosing a quotient basis containing the nonzero radial class and specifying its representative to be \(R_j\). The resulting \(V_j\) remains symplectic.

The quotient graph identifies these radial vectors. Choose a symplectic basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\) in \(V_1\), with \(f_1=R_1\) and \(\omega_1(f_j,e_k)=\delta_{jk}\). Nondegeneracy gives a partner \(e_1\); its symplectic orthogonal supplies the remaining pairs by induction. Transfer this basis through the graph to \(V_2\); there \(f_1=R_2\). In each remaining block \(W_j\), choose a basis of the Lagrangian \(K_j\) as the additional \(e\) vectors and complete it by the Lagrangian basis-extension argument of the geometry lesson.

Map the \(e\) vectors to standard base vectors and the \(f\) vectors to standard frequency vectors at \((0,e_1)\). The two resulting tangent maps are symplectic and preserve the radial vector. Theorem 2.1 realizes each by homogeneous symplectic coordinates. Formula (1.3) in these bases is exactly (3.3). ∎

This normalizes the tangent plane at the marked point. It does not claim that the whole nearby nonlinear relation is the flat relation (3.3).

## 4. A partial Fourier form has the corank order shift

By (3.3), the variables \((x',x'',y'',\eta')\) have invertible differential on \(C\) at the marked point. They are local coordinates there. Homogeneity extends them to an interior cone about \(\eta'=e_1\). The signed conic one-form vanishes on \(C\):
\[
\xi' dx'+\xi'' dx''-\eta' dy'-\eta''dy''=0.
\]
Define \(\phi=\eta'\cdot y'\), expressing \(y'\) in these parameters. Then
\[
d\phi=\xi' dx'+\xi'' dx''-\eta''dy''+y'd\eta',
\]
and therefore
\[
C=\{(x',x'',\phi_{x'},\phi_{x''};
y'=\phi_{\eta'},y'',\eta',-\phi_{y''})\}.
\tag{4.1}
\]
The function \(\phi\) is homogeneous of degree one in \(\eta'\). Its mixed matrix \(\phi_{x'\eta'}\) is identity at the marked point, hence invertible nearby.

The phase \(\Phi=\phi-y'\cdot\eta'\) is nondegenerate, since its critical equations \(\phi_{\eta'}-y'=0\) have derivative \(-I\) in \(y'\). Its number of frequency variables is \(n\); the kernel ambient dimension is \(n_1+n_2=2n+a+b\). The prescribed-phase converse gives
\[
K_A=(2\pi)^{-(n_1+n_2+2n)/4}
\int e^{i\Phi}a_0(x',x'',y',y'',\eta')\,d\eta',
\tag{4.2}
\]
modulo a smooth kernel, with amplitude order
\[
\mu=m+\frac{n_1+n_2-2n}{4}
=m+\frac{a+b}{4}.
\tag{4.3}
\]
Taylor expansion about \(y'=\phi_{\eta'}\), followed by the \(D_{\eta'}\) integration-by-parts step of the graph lesson, eliminates dependence on \(y'\). The ordinary support-preserving asymptotic sum gives an amplitude \(a(x',x'',y'',\eta')\in S^\mu\) with the same critical leading coefficient. The critical density in these parameters is \(|dx'\,dx''\,dy''\,d\eta'|\).

Let \(\widehat u(\eta',y'')=\int e^{-iy'\cdot\eta'}u(y',y'')\,dy'\). Integrating (4.2) in \(y\) gives the partial Fourier form
\[
(Au)(x',x'')=(2\pi)^{-n-(a+b)/4}
\iint e^{i\phi(x',x'',y'',\eta')}
a(x',x'',y'',\eta')\widehat u(\eta',y'')\,d\eta'\,dy''.
\tag{4.4}
\]
The prefactor is the kernel normalization, not a guessed full Fourier factor when \(n_1\) and \(n_2\) differ. The partial integral is the actual kernel action. For compact smooth \(u\), its partial Fourier transform and every parameter derivative decrease faster than every power of \(|\eta'|\), uniformly on the compact \(y''\) support. Each differentiated amplitude and phase contributes only a fixed power of \(|\eta'|\). The frequency-cutoff integrals therefore converge absolutely with every output and parameter derivative. Fubini and dominated convergence from M3–M4 identify their limit with (4.4) and with the previously defined distributional kernel. The smooth remainder has the usual smooth localized action. No restriction theorem for arbitrary distributions is being assumed.

For fixed \((x'',y'')\), this is a graph operator in the \(n\) variables \(x',y'\), of order \(\mu\). The graph determinant stays uniformly nonzero on small compact parameter sets. Finite-seminorm estimates therefore give uniform graph bounds there whenever \(\mu\leq0\).

The tangent information also records a useful higher-order fact. At \((x',x'',y'',\eta')=(0,0,0,e_1)\),
\[
h=\phi-x'\cdot\eta'
\quad\text{has zero value, first derivatives and second derivatives.}
\tag{4.5}
\]
The first derivatives follow from the marked covectors and zero base values. Differentiating (4.1) and comparing with (3.3) gives the second derivatives: the \(x',\eta'\) mixed block is identity, and all the other second blocks are zero. Write \(\eta'=(r,r\vartheta)\), \(r=\eta'_1>0\). Homogeneity makes \(h=rH(x',x'',y'',\vartheta)\), with a vanishing two-jet for \(H\) at zero. Taylor's formula yields, on a small fixed cone,
\[
|h|\leq C\left[
(|x'|^3+|x''|^3+|y''|^3)|\eta'|
+\frac{\sum_{j=2}^n|\eta'_j|^3}{|\eta'|^2}
\right].
\tag{4.6}
\]
We used comparability of \(r\) and \(|\eta'|\), and the elementary bound for the cube of a finite sum by a constant times the sum of cubes. This cubic estimate is preparation for a different, necessary-order test; it is not an improved norm bound by itself.

## 5. Uniform graph bounds can be integrated over the parameters

Let \(\sigma_C\) be the common pullback of the two symplectic forms to \(C\), and put \(k(c)=\operatorname{corank}\sigma_C(c)\).

**Theorem 5.1 (sufficient corank estimate).** Let \(C\) be a homogeneous canonical relation with neither individual lifted radial vector tangent at any point. If
\[
m\leq-\frac{k(c)}4\quad\text{for every }c\in C,
\tag{5.1}
\]
then every ordinary \(A\in I^m(X\times Y,C';\Omega^{1/2}\otimes\operatorname{Hom}(F,E))\) is continuous
\[
A:L^2_{\mathrm{comp}}(Y)\longrightarrow L^2_{\mathrm{loc}}(X).
\tag{5.2}
\]
The ranks need not be constant.

**Proof in normalized coordinates.** Localize at \(c_0\) and write (4.4), with \(k_0=k(c_0)=a+b\). By (5.1), \(\mu=m+k_0/4\leq0\). The partial graph operators
\[
(T_{x'',y''}v)(x')=(2\pi)^{-n}
\int e^{i\phi(x',x'',y'',\eta')}a(x',x'',y'',\eta')\widehat v(\eta')\,d\eta'
\]
have \(\|T_{x'',y''}\|_{2\to2}\leq M\) uniformly on the working compact parameter sets \(K_X''\), \(K_Y''\). This is exactly the finite-seminorm graph estimate, with a compact family of fixed phase/support data. Its uniformity follows from the actual frequency-change proof in the graph lesson, Section 3: after shrinking the joint base, angular and parameter patch, the mixed derivative matrices are uniformly close to one invertible matrix. The convex-cone injectivity bound, inverse derivative bounds and finitely many ordinary PDO amplitude estimates then have common constants. All phase and amplitude derivatives needed for those bounds are bounded on the same compact parameter set, as in W2. An order-\(\mu\leq0\) amplitude has the required order-zero bounds.

For smooth inputs the convergence just proved makes the parameter-dependent outputs continuous with common compact output support. Their parameter integrals can be formed by finite Riemann sums in \(L^2(dx')\): uniform continuity on the compact parameter boxes and the scalar integral estimate show that those sums are Cauchy, and completeness gives the integral. The triangle inequality holds first for the finite sums and then for their limits. Thus the triangle inequality in \(L^2(dx')\) and Cauchy–Schwarz in \(y''\) give
\[
\|Au(\cdot,x'')\|_{L^2(dx')}
\leq (2\pi)^{-k_0/4}M
\int_{K_Y''}\|u(\cdot,y'')\|_{L^2(dy')}\,dy''
\leq (2\pi)^{-k_0/4}M |K_Y''|^{1/2}\|u\|_2.
\]
Integrating the square in \(x''\) yields
\[
\|Au\|_2\leq
(2\pi)^{-k_0/4}M |K_X''|^{1/2}|K_Y''|^{1/2}\|u\|_2.
\tag{5.3}
\]
If a parameter space has dimension zero, its factor is one. Compact smooth density gives the bounded extension. The smooth localized remainder has a bounded integral norm.

**Restore the original coordinates.** Quantize the two homogeneous coordinate changes by local elliptic order-zero graph FIOs \(F_1,F_2\), taking \(A\) to \(F_1AF_2\) in the model coordinates. The graph lesson gives proper microlocal inverses \(G_1,G_2\), with \(G_1F_1\) and \(F_2G_2\) equal to identity on smaller cones modulo smooth kernels. These four graph operators are locally \(L^2\) bounded. For a sufficiently small localized kernel piece, the composed operator \(G_1(F_1AF_2)G_2\) agrees with \(A\) modulo a smooth localized kernel: the error factors have wavefront excluded from the working cones, and the composition wavefront theorem applies. Proper local supports keep the compact sets needed by each norm estimate. Hence (5.3) gives boundedness for the original piece.

For fixed compact input and output base supports, the full closed normalized relation is compact and avoids both covector axes. A finite cover by these pieces, and the residual smooth kernel, gives (5.2). Bundle matrices are handled componentwise with compact Hermitian norm equivalence, exactly as for graph continuity.

At each chosen point, \(a,b,n\) are the dimensions in its tangent splitting. That splitting yields a valid parameter form on a neighborhood even if nearby ranks increase. The order in (4.3) uses the dimensions at the chosen point; (5.1) there already makes it nonpositive. No neighborhood of constant rank was used. ∎

**Corollary 5.2 (a uniform corank Sobolev shift).** On the working relation suppose \(k(c)\leq k_*\), and retain the radial hypothesis. Then for every real \(s\),
\[
A:H^s_{\mathrm{comp}}(Y)\longrightarrow H^{s-m-k_*/4}_{\mathrm{loc}}(X).
\tag{5.4}
\]
The bound may be used on each fixed compact localization with a bound \(k_*\) for its normalized relation.

**Proof.** Choose proper elliptic reducers of orders \(s\) on the input and \(s-m-k_*/4\) on the output, and an input parametrix of order \(-s\). The reduced FIO has order \(-k_*/4\), which is at most \(-k(c)/4\). Theorem 5.1 applies. The two localized smoothing errors and output elliptic reconstruction are handled exactly as in the graph Sobolev proof; those steps use proper PDOs and the smooth-input/adjoint mappings and do not require the relation to be a graph. They give (5.4), with compact smooth approximation in a common compact support for every real \(s\). ∎

### The measurable vector integrals used in the exercises

In Exercise 7.6, a measurable operator family means that \((s,t)\mapsto T_{s,t}v\) is jointly strongly measurable for every fixed \(v\in H\); vectors in the input \(L^2\) space are strongly measurable. Strongly measurable means an almost-everywhere pointwise limit of finite-valued measurable simple functions. The parameter sets carry finite measures, and joint measurability refers to their completed product measure. This specifies the integral in that exercise, including infinite-dimensional Hilbert spaces, without assuming norm-continuity of the operator family.

Here is the required construction. For an integrable strongly measurable vector function \(g\) on a finite-measure space, take simple functions \(v_j\to g\) almost everywhere, and replace \(v_j\) by \(g_j=v_j1_{\{\|v_j\|\le2\|g\|\}}\). Each \(g_j\) is still finite-valued and measurable, \(\|g_j\|\le2\|g\|\), and \(g_j\to g\), including where \(g=0\). M3's dominated convergence gives \(\int\|g_j-g\|\to0\). Integrate a simple function by multiplying each of its values by its level-set measure and summing. The vector triangle inequality gives \(\|\int g_j-\int g_l\|\le\int\|g_j-g_l\|\), so Hilbert completeness defines a limit independent of the simple approximation. Passing to the limit proves \(\|\int g\|\le\int\|g\|\). Linearity follows from the finite sums and this bound.

The finite-product integration needed here also holds for arbitrary finite parameter measures. To see this directly, consider the product sigma-algebra. Measurable rectangles have measurable sections and measurable section measures. The sets with that property form a Dynkin class: complements subtract from the fixed finite total measure, and disjoint unions use monotone convergence. The generating-class proof M1 therefore gives the property for all product-measurable sets. Define the product measure of such a set \(E\) to be \(\int\nu(E_s)\,d\mu(s)\). Disjoint additivity and monotone convergence show countable additivity; on rectangles this is the product of the two measures. Reversing the factors gives another finite measure with the same rectangle values. Applying the same Dynkin-class argument to the sets on which they agree proves equality on the product sigma-algebra. Increasing simple approximation now proves Tonelli, and the integrable positive and negative parts give Fubini. A subset of a product null set has null sections outside a null set, since the section-measure integral is zero; completing the measures therefore gives the same almost-everywhere statements. This is the whole finite-product proof required here, without restricting the parameter sets to coordinate boxes.

For \(f(s,t)=T_{s,t}u(t)\), simple approximation of \(u\), strong measurability on each of its finitely many values, and the uniform bound \(\|T_{s,t}\|\le M\) prove joint strong measurability of \(f\). To justify the successive approximation assertion explicitly, all simple approximants have countably many values in total, so outside their combined null sets they and their limits lie in one separable closed subspace; choose a countable dense set in that closed subspace. For each positive integer j, choose the first point among its first j members minimizing the distance to the vector under consideration. The finitely many distances are measurable, this rule gives a finite-valued measurable function, and its distance tends to zero by density. The bound \(\|f(s,t)\|\le M\|u(t)\|\), Cauchy–Schwarz and finite parameter volumes make this norm integrable on the product. Choose simple \(f_j\) with \(\int\!\int\|f_j-f\|\to0\) and pass to a subsequence whose errors are summable. Tonelli just proved shows that their section errors tend to zero for almost every \(s\). Each function \(s\mapsto\int f_j(s,t)\,dt\) is strongly measurable: for a simple term \(v1_E(s,t)\), the section-measure argument above proves measurability. The vector-integral bound gives convergence to \(s\mapsto\int f(s,t)\,dt\) almost everywhere, proving its strong measurability. The triangle and Cauchy–Schwarz estimates in the exercise consequently apply to an actual measurable Hilbert-valued function. No general vector integration theorem is being imported without its proof.

## 6. A flat model explains the sufficient threshold

Take \(n\geq1\), \(a,b\geq0\), and the flat relation
\[
C_{\mathrm{flat}}=\{(x',x'',\eta',0;
y'=x',y'',\eta',0):\eta'\neq0\}.
\tag{6.1}
\]
It has \(k=a+b\). Its two individual radial vectors are excluded; the shared graph-frequency radial vector is nonzero. Choose smooth compact factors \(q(x')\), \(h(x'')\), \(\ell(y'')\), all nonzero, and an ordinary symbol \(s_\mu(\eta')=\langle\eta'\rangle^\mu\psi(\eta')\), where \(\psi\) is a smooth angular cutoff equal to one near a unit direction \(\theta_0\) at high frequency. The amplitude
\[
a=q(x')h(x'')\ell(y'')s_\mu(\eta')
\]
in (4.4) defines an FIO of order \(m=\mu-k/4\), modulo the harmless low-frequency convention. Its action is
\[
Au=(2\pi)^{-k/4}h(x'')q(x')
s_\mu(D_{x'})\left[\int\ell(y'')u(x',y'')\,dy''\right].
\tag{6.2}
\]

If \(\mu>0\), this localized operator is unbounded on \(L^2\). Choose \(v\in C_c^\infty\) with \(qv\neq0\), and \(w\in C_c^\infty\) with \(\int\ell w\neq0\). Use
\[
u_R(y',y'')=e^{iR\theta_0\cdot y'}v(y')w(y''),\qquad R\longrightarrow\infty.
\]
Its input norm is fixed. After demodulation and division by \(R^\mu\), the Fourier multiplier in (6.2) has coefficient
\[
R^{-\mu}s_\mu(\zeta+R\theta_0)\longrightarrow1
\tag{6.3}
\]
for every fixed \(\zeta\). For \(R\geq1\) it is bounded by \(C\langle\zeta\rangle^\mu\), since \(\langle\zeta+R\theta_0\rangle/R\leq C\langle\zeta\rangle\) and the cutoff is bounded. The rapid decrease of \(\widehat v\), dominated convergence and Plancherel therefore show that the demodulated output divided by \(R^\mu\) converges in \(L^2(dx'\,dx'')\) to
\[
(2\pi)^{-k/4}h(x'')q(x')v(x')\int\ell(y'')w(y'')\,dy'',
\]
which is nonzero. The output norm grows like a positive constant times \(R^\mu\). Thus the sufficient inequality \(m\leq-k/4\) is sharp for this flat family.

This exhibits the order obstruction in an actual kernel. To deduce the same sharpness for every fixed relation with constant-rank \(\sigma_C\), one must also straighten its two coisotropic projection images. That supporting homogeneous normal form has further hypotheses and proof steps. For relations with changing rank, a universal necessary bound uses a different cubic scaling; neither statement follows just from the flat example.

## 7. Exercises with complete solutions

**Exercise 7.1 (two different projection kernels; introductory).** Let \(n_1=4\), \(n_2=3\), and \(\operatorname{rank}\sigma_G=4\). Compute \(\dim G\), \(a,b\), the two projection ranks, and the corank. Specify which projection has each kernel.

**Solution.** The shared symplectic quotient has dimension \(2n=4\), so \(n=2\). Thus \(a=n_1-n=2\), \(b=n_2-n=1\), \(\dim G=n_1+n_2=7\), and \(k=a+b=3\). The projection to \(S_1\) has rank \(n_1+n=6\) and kernel \(0\oplus K_2\), of dimension one. The projection to \(S_2\) has rank \(n_2+n=5\) and kernel \(K_1\oplus0\), of dimension two. Corank three is consistent with rank four on the seven-dimensional relation.

**Exercise 7.2 (an odd corank and an exact lifting order; intermediate).** Let \(Y=\mathbb R\), \(X=\mathbb R^2\), and \(Au(x_1,x_2)=h(x_2)u(x_1)\), with nonzero \(h\in C_c^\infty\). Find its relation, order, corank, proper support and exact \(L^2\) norm.

**Solution.** The kernel is \(h(x_2)\delta(x_1-y)\). With phase \((x_1-y)\eta\), the relation is
\[
\{(x_1,x_2,\eta,0;y=x_1,\eta):\eta\neq0\}.
\]
It has \(n=1,a=1,b=0\), hence corank one. The kernel ambient dimension is three and the amplitude order is zero; the FIO order is \(0-3/4+1/2=-1/4\). In the normalized kernel convention its amplitude is \((2\pi)^{1/4}h\), which makes (4.4) exactly the stated operator. Its support has \(y=x_1\) and \(x_2\in\operatorname{supp}h\), so both support projections are proper. Fubini gives \(\|Au\|_2^2=\|h\|_2^2\|u\|_2^2\), and the norm is \(\|h\|_2\). The critical order is \(-k/4=-1/4\); treating this as an order-zero graph between equal-dimensional spaces would give the wrong order.

**Exercise 7.3 (why the paired radial vector is insufficient; intermediate).** In the linear relation \(G=L_1\oplus L_2\), with \(L_j\) Lagrangian, choose nonzero \(R_j\in L_j\). Explain why the paired vector is tangent, why the radial hypothesis fails, and why the normal form cannot have a nonzero shared graph-frequency radial direction. This is a tangent-space question, not a global operator example.

**Solution.** All pairs with components in \(L_j\) are in \(G\), including \((R_1,R_2)\), \((R_1,0)\), and \((0,R_2)\). Here \(K_j=L_j\), so \(n_j-\dim K_j=0\). The common pulled-back two-form is zero and there is no nonzero symplectic quotient. Moreover \(\lambda_C(v,w)=\omega_1(R_1,v)=0\) for every \(v\in L_1\). The nonzero shared radial class required for \(\eta'=e_1\) cannot exist. Homogeneity's paired tangency alone therefore does not imply the extra exclusion.

**Exercise 7.4 (a changing-rank canonical relation; advanced).** In dimensions \(n_1=n_2=2\), use the partial phase
\[
\phi(x,z,t,\eta)=(x+zt^2)\eta,\qquad\eta>0,
\]
where \(x=x'\), \(z=x''\), \(t=y''\). Compute the relation, the common two-form, its rank and the sufficient order condition at and away from \(t=0\). Check the radial hypothesis.

**Solution.** Formula (4.1) gives
\[
(x,z;\eta,t^2\eta),\qquad
(y'=x+zt^2,t;\eta,-2zt\eta).
\]
The common form is
\[
\sigma_C=d\eta\wedge dx+t^2d\eta\wedge dz
+2t\eta\,dt\wedge dz.
\]
For \(t\neq0\) its square has a nonzero multiple of \(d\eta\wedge dx\wedge dt\wedge dz\), so its rank is four. At \(t=0\) it equals \(d\eta\wedge dx\), of rank two and corank two. The sufficient threshold is \(m\leq0\) away from zero and \(m\leq-1/2\) at zero. The common one-form is \(\eta\,dx+t^2\eta\,dz\), which is nonzero because \(\eta>0\). Thus neither individual radial vector is tangent. Also \(\phi_{x\eta}=1\), and \(\phi-x\eta=zt^2\eta\) has zero two-jet at the normalized marked point. The local parameter graph remains usable where the full relation changes rank. This computation does not classify both projections as folds.

**Exercise 7.5 (the exact homogeneous Moser correction; advanced).** On a cone in \(T^*\mathbb R^2\), set
\[
\omega=\omega_0+\varepsilon x_2\,d\xi_1\wedge dx_2,
\qquad p_0=(0,0;1,0).
\]
Compute the radial primitive difference, the function \(f\) correcting its first jet, the vector field \(V_t\), and its flow. Verify directly that the flow preserves the marked tangent map.

**Solution.** The extra term is closed, has degree one, and vanishes at \(p_0\). Its radial contraction is \(\alpha=\varepsilon\xi_1x_2dx_2\), with nonzero first coefficient jet \(\varepsilon dx_2\otimes dx_2\). Choose \(f=\varepsilon\xi_1x_2^2/2\). Then
\[
\gamma=\alpha-df=-\varepsilon x_2^2d\xi_1/2.
\]
For \(\omega_t=\omega_0+t\varepsilon x_2d\xi_1\wedge dx_2\), equation (2.5) gives \(V_t=-\varepsilon x_2^2\partial_{x_1}/2\): its contraction with the ordinary \(d\xi_1\wedge dx_1\) term is \(+\varepsilon x_2^2d\xi_1/2=-\gamma\), and the other contractions are zero. The flow is
\[
\Psi_t(x_1,x_2;\xi_1,\xi_2)
=(x_1-t\varepsilon x_2^2/2,x_2;\xi_1,\xi_2).
\]
Its pullback of \(d\xi_1\wedge dx_1\) produces \(-t\varepsilon x_2d\xi_1\wedge dx_2\), canceling the added term. Hence \(\Psi_t^*\omega_t=\omega_0\). It fixes \(p_0\), has differential identity there, and commutes with cotangent dilation. This example shows why the first-jet correction is required even though the two-form difference vanishes at the point.

**Exercise 7.6 (parameter volumes in the norm estimate; intermediate).** Let \(T_{s,t}:H\to H'\) be a measurable operator family with norm at most \(M\) on parameter sets of positive finite measures \(V_X,V_Y\), and set \((Au)(s)=\int T_{s,t}u(t)\,dt\). Prove \(\|A\|\leq M\sqrt{V_XV_Y}\), and show that the volume factor can be attained when \(T_{s,t}=T\) is constant and \(T\) attains its norm.

**Solution.** For each \(s\), triangle inequality gives \(\|Au(s)\|\leq M\int\|u(t)\|dt\leq M\sqrt{V_Y}\|u\|_{L^2(t;H)}\). Squaring and integrating in \(s\) gives the bound. For a unit vector \(v\) with \(\|Tv\|=M\), take \(u(t)=v/\sqrt{V_Y}\). This input has norm one, and \(Au(s)=\sqrt{V_Y}Tv\) has total norm \(M\sqrt{V_XV_Y}\). With a nonattained norm, approximating unit vectors give the same norm supremum. Formula (5.3) includes in addition its explicit kernel-normalization constant.

**Exercise 7.7 (the same geometry supports different norm behavior; advanced).** In (6.2), choose \(a=b=1\) and amplitudes with \(\mu=0\) and \(\mu=1\). Give their FIO orders and compare their \(L^2\) behavior. Explain why the common canonical relation alone does not distinguish them.

**Solution.** Here \(k=2\), so \(m=\mu-1/2\). The orders are \(-1/2\) and \(+1/2\), respectively. For \(\mu=0\), the compactly localized order-zero graph multiplier and the two parameter factors give a bounded operator by (5.3). For \(\mu=1\), use the fixed-norm inputs \(e^{iR\theta_0\cdot y'}v(y')w(y'')\) with \(qv\neq0\) and \(\int\ell w\neq0\). The multiplier divided by \(R\) and demodulated converges to \(v\) in \(L^2\), since (6.3) tends to one and is bounded by \(C\langle\zeta\rangle\) against the rapidly decreasing \(\widehat v\). Thus the output norm divided by \(R\) has a positive limit, proving unboundedness. Both phases parametrize (6.1). Their different amplitude orders, and not a change of the relation, produce the different behavior.

**Exercise 7.8 (use an upper corank bound; intermediate).** On a localized relation with the radial hypothesis, suppose \(k(c)\leq3\), and let \(A\) have order \(m=1/2\). Give a Sobolev mapping valid for every real \(s\), and explain the order of the operator after elliptic reduction.

**Solution.** Corollary 5.2 gives \(H^s_{\mathrm{comp}}\to H^{s-5/4}_{\mathrm{loc}}\), because \(m+3/4=5/4\). Input and output reducers of orders \(s\) and \(s-5/4\), together with an input inverse of order \(-s\), make the reduced FIO order \((s-5/4)+1/2-s=-3/4\). This is at most \(-k(c)/4\) when \(k(c)\leq3\). Theorem 5.1 therefore applies even if the rank changes. Proper parametrix errors are smoothing on the fixed supports, and output elliptic reconstruction recovers the indicated Sobolev order.

## References

- [Hörmander IV, §25.3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, reprint of the corrected second printing (1994), Lemma 25.3.6, Proposition 25.3.7, equation 25.3.5 and Theorem 25.3.8.
- [Hörmander III, §21.1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the corrected second printing (1994), Springer, Theorem 21.1.9; mixed generating-function context, Theorem 21.2.18.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact programme prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original text: public domain (CC0).*
