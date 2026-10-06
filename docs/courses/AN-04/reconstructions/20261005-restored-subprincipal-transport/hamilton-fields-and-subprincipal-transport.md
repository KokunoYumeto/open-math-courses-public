# Hamilton fields and subprincipal transport

When the principal symbol of a scalar differential or pseudodifferential operator vanishes along a canonical relation, its leading product with an FIO vanishes. The next symbol contains a derivative along that relation. Because the FIO symbol is a half density, that derivative includes half the divergence of the Hamilton field. The remaining scalar coefficient is the subprincipal symbol.

The exact earlier programme proofs are:

- The restored [phase-space lesson](../20261005-restored-phase-space/phase-space-and-generating-families.md) fixes the Hamilton sign and proves the conic Lagrangian identities and symplectic reductions. Its [finite-coordinate flow companion, Sections 17.1–17.7](../20261005-restored-phase-space/finite-coordinate-flows.md), proves existence, uniqueness, smooth parameters, the local flow law and coordinate compatibility.
- The restored [intrinsic-regularity lesson, Section 3](../20261005-restored-intrinsic-regularity/intrinsic-lagrangian-regularity.md), gives the full frequency normal form; the [Gaussian-symbol lesson, Sections 4–7](../20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.md), gives flat Maslov frames, actual density degrees and the exact principal-symbol quotient.
- The restored [kernel and composition lesson](../20261005-restored-analytic-composition/clean-composition-of-fourier-integral-operators.md) supplies the smooth mapping, scalar kernel correspondence, proper localization and ordinary composition proofs. Its [kernel companion](../20261005-restored-analytic-composition/scalar-kernels-and-strong-topology.md) specifies the distribution topologies.
- The included [subprincipal coordinate companion](subprincipal-coordinate-invariance.md) retains AN03-U012's complete scalar calculation G11–G14, with its licence and notices. Section S1 proves the first coordinate correction, including every differentiated remainder, using the existing amplitude and coordinate calculus. Thus the invariant coefficient below is an exact programme result.
- [Homogeneous symbol estimates, H2–H3 and H6–H8](../20261004-free-canonical-composition/homogeneous-symbol-transport.md), prove all derivative counts, support-preserving asymptotic sums and cutoff convergence. [Density integration](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md), [product measure](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) and [exponentials and circle periods](../20261004-free-stationary-phase/exponential-prerequisite-completions.md) supply the elementary inputs.

The [proof map](proof-map.json) binds every use to the exact retained source and proof. The primary source is the approved purchased reprint of Hörmander IV, corrected second printing (1994), Section 25.2 equation 25.2.11, Theorem 25.2.4 and Lemma 25.2.5. The independently written lesson, its calculations and all six original solved exercises are retained. All symbol estimates in this lesson are ordinary \(S_{1,0}\) estimates. The scalar operator is classical with step-one homogeneous expansion. The FIO need not have a homogeneous leading amplitude. All constructions are local over compact base sets, with microlocal cutoffs inside the stated open cones.

## 1. A vector field differentiates a density as well as its coefficient

For a complex number \(\kappa\), the density line \(\Omega^\kappa(M)\) has transition factors \(J^\kappa=e^{\kappa\log J}\), with \(J>0\). Their multiplicativity defines the line even for complex \(\kappa\). In a coordinate chart a section is \(f|du|^\kappa\).

Let \(V=\sum_jV_j\partial_{u_j}\) be real, with local flow \(F_t\). Define
\[
\mathcal L_V a=\left.\frac{d}{dt}F_t^*a\right|_{t=0}.
\tag{1.1}
\]
In coordinates,
\[
\mathcal L_V(f|du|^\kappa)
=\left(Vf+\kappa\sum_j\partial_{u_j}V_j\,f\right)|du|^\kappa.
\tag{1.2}
\]

**Proof.** Pullback gives
\[
F_t^*(f|du|^\kappa)
=f(F_t(u))|\det dF_t(u)|^\kappa |du|^\kappa.
\]
At \(t=0\), \(dF_0=I\) and \(\partial_t dF_t|_0=dV\). The determinant derivative is \(\operatorname{tr}dV\); its sign is positive near \(t=0\). Differentiating the positive power gives \(\kappa\operatorname{tr}dV\), and differentiating \(f(F_t(u))\) gives \(Vf\). This proves (1.2). Pullback is coordinate independent, so the expression patches on overlaps. ∎

For a complex vector field \(V=V_1+iV_2\), with real \(V_1,V_2\), define \(\mathcal L_V=\mathcal L_{V_1}+i\mathcal L_{V_2}\). Formula (1.2) is complex linear in the coefficients and their derivatives, so it remains valid and coordinate independent. No real flow of a complex vector field is asserted.

A Maslov line has locally constant transition factors. In such local frames, differentiate its density coefficient by (1.2). Constant transition factors commute with the derivative, so this defines \(\mathcal L_V\) on Maslov-valued densities. For half densities the coefficient of divergence is \(1/2\).

For a real field and compactly supported smooth half densities, integration by parts also gives
\[
\int\langle\mathcal L_Va,b\rangle
+\int\langle a,\mathcal L_Vb\rangle=0.
\tag{1.3}
\]
Indeed the integrand coefficient is \(V(f\overline g)+(\operatorname{div}V)f\overline g\), the divergence of \(Vf\overline g\). Its integral is zero in each chart; a partition of unity proves the global identity. More explicitly, a partition \(\sum_\ell\chi_\ell=1\) is finite near the compact supports. Apply the chart identity to \(\chi_\ell a,b\), then sum. The additional coefficients \(\sum_\ell V\chi_\ell\) vanish, proving the claimed identity with no residual chart-boundary term. Thus the half-density correction is exactly what makes the derivative skew under the density pairing.

## 2. Vanishing on a Lagrangian makes the Hamilton field tangent

Let \(C\) be a homogeneous canonical relation from \(T^*Y\setminus0\) to \(T^*X\setminus0\), with the full punctured-cotangent closure of the preceding lesson, and put \(\Lambda=C'\). Let \(p\) be a smooth scalar function on \(T^*X\setminus0\), homogeneous of degree \(m\), whose restriction to the \(X\) projection of \(C\) is zero. On \(T^*(X\times Y)\), lift \(p\) by making it independent of the \(Y\) variables. Its Hamilton field is
\[
H_p=\sum_{j=1}^{n_X}
\left(p_{\xi_j}\partial_{x_j}-p_{x_j}\partial_{\xi_j}\right).
\tag{2.1}
\]

**Lemma 2.1.** The lifted field is tangent to \(\Lambda\). If \(p\) is complex, it takes values in the complexification of \(T\Lambda\).

**Proof.** The restriction \(p|_\Lambda\) is zero, so \(dp(v)=0\) for every \(v\in T\Lambda\). With \(\omega=\sum d\xi\wedge dx+\sum d\eta\wedge dy\), our convention is \(\omega(H_p,v)=-dp(v)\). Therefore \(H_p\in(T\Lambda)^\omega=T\Lambda\), since \(\Lambda\) is Lagrangian. Apply the same argument to the real and imaginary parts when needed. The input-covector reflection transporting \(\Lambda\) to \(C\) preserves this lifted field. ∎

The Lie derivative of the symbol is therefore defined along the relation itself. Its dependence on a local coefficient includes the density term from Section 1.

## 3. The transport theorem and its exact hypotheses

Let \(P\) be a properly supported classical scalar pseudodifferential operator of order \(m\) on half densities on \(X\). In a coordinate half-density frame, write its left symbol as
\[
P(x,\xi)=p(x,\xi)+r(x,\xi)\pmod{S^{m-2}},
\tag{3.1}
\]
where \(p\) and \(r\) are homogeneous of degrees \(m\) and \(m-1\) away from zero. Its intrinsic scalar subprincipal symbol is the imported quantity
\[
c=r+\frac i2\sum_j p_{x_j\xi_j}.
\tag{3.2}
\]
The half-density hypothesis is part of the coordinate-invariance statement.

Suppose \(p\) vanishes on the \(X\) projection of \(C\), and
\[
A\in I^{m'}(X\times Y,C';\Omega^{1/2}).
\]
Write \(a\) for its principal symbol, of intrinsic symbol order
\[
\nu=m'+\frac{n_X+n_Y}{4}
\tag{3.3}
\]
in \(M_\Lambda\otimes\Omega_\Lambda^{1/2}\), modulo one lower order.

**Theorem 3.1 (scalar subprincipal transport).** The kernel of \(PA\) belongs to
\[
I^{m+m'-1}(X\times Y,C';\Omega^{1/2}),
\tag{3.4}
\]
with principal symbol
\[
\sigma(PA)=\frac1i\mathcal L_{H_p}a+c\,a,
\tag{3.5}
\]
of intrinsic order \(\nu+m-1\), modulo one lower order.

The proper support of \(P\) makes this operator product meaningful even when \(A\) is not properly supported: \(A\) maps compact smooth inputs to smooth outputs, and \(P\) acts on all smooth functions. The kernel correspondence then defines \(PA\). The theorem asserts its Lagrangian class; proper support of \(PA\) additionally follows if \(A\) is proper. The proof is microlocal and applies inside any fixed working cone. It concerns scalar half-density operators; bundle systems require their corresponding first-order frame or connection data.

We prove the theorem after establishing a coordinate choice that keeps the two manifolds separate.

## 4. Almost every diagonal graph complements a Lagrangian plane

Write \(T^*\mathbb R^N=\mathbb R^N_x\times\mathbb R^N_\xi\), and set
\[
L_b=\{(x,\xi):\xi_j=b_jx_j,\ 1\leq j\leq N\},
\qquad b\in\mathbb R^N.
\tag{4.1}
\]
These planes are Lagrangian, since their graph matrices are symmetric.

**Lemma 4.1 (diagonal complements).** For any Lagrangian plane \(L\), the planes \(L\) and \(L_b\) are transverse for almost every \(b\), with respect to Lebesgue measure.

**Proof of existence.** Use induction on \(N\), beginning with the zero-dimensional space. In the first symplectic coordinate pair choose \(b_1\) so that
\[
v=e_1+b_1f_1\notin L.
\]
Such a choice exists: two distinct slopes in \(L\) would put both \(e_1\) and \(f_1\) in \(L\), contradicting isotropy. Put \(V=\mathbb Rv\). Its symplectic orthogonal is \(V^\omega=\{\xi_1=b_1x_1\}\). The quotient \(V^\omega/V\) is the symplectic space of the remaining coordinate pairs. Because \(v\notin L=L^\omega\), the equation \(\omega(v,w)=0\) is a nonzero linear condition on \(L\). Thus \(L\cap V^\omega\) has dimension \(N-1\), intersects \(V\) trivially, and projects to a Lagrangian plane \(\overline L\) in this quotient.

Choose \(b_2,\ldots,b_N\) by induction so that \(\overline L\) is transverse to the corresponding diagonal graph. A vector in \(L\cap L_b\) then has zero image in the quotient, so lies in \(V\cap L=0\). Hence \(L\cap L_b=0\), proving existence.

**Proof of almost-everywhere transversality.** Write a basis of \(L\) as the columns of \(\binom{U}{W}\). A vector in its intersection with \(L_b\) has coefficient vector in the kernel of
\[
W-\operatorname{diag}(b)U.
\]
Consequently nontransversality is the zero set of the polynomial
\[
q(b)=\det\bigl(W-\operatorname{diag}(b)U\bigr).
\tag{4.2}
\]
Existence proves that this polynomial is not identically zero. A one-variable nonzero polynomial of degree \(d\) has at most \(d\) roots: for a root \(c\), each difference \(t^k-c^k\) is \((t-c)\sum_{j=0}^{k-1}t^{k-1-j}c^j\); dividing off this factor reduces the degree, and induction proves the bound. A finite set has measure zero by covering its points with intervals of arbitrarily small total length. A nonzero real polynomial in several variables has a null zero set: by induction on the number of variables, outside the null common zero set of a nonzero coefficient polynomial its one-variable slices have finitely many roots. Fubini on each bounded box, followed by their countable union, proves the assertion. This proves the lemma. ∎

The measure assertion is stronger than merely finding one complement. It follows from the determinant polynomial, rather than from an unspecified genericity assumption.

## 5. Separate base coordinates give a full-frequency generating function

Fix \((x_0,\xi_0;y_0,\eta_0)\in\Lambda\); here \(\eta_0\) is the kernel covector, so the input relation covector is \(-\eta_0\). Both \(\xi_0\) and \(\eta_0\) are nonzero. Translate the base coordinates to make \(x_0=y_0=0\). Lemma 4.1 supplies a diagonal graph complementary to \(T\Lambda\) in the full cotangent tangent space. Its diagonal matrix splits into an \(X\) block \(B_X\) and a \(Y\) block \(B_Y\).

We can realize that graph as the old-coordinate image of the new horizontal tangent plane using separate base changes. Choose a component \(\xi_{0,\ell}\neq0\), and define an old base coordinate map \(x=F(u)\) with
\[
F_j(u)=u_j\quad(j\neq\ell),\qquad
F_\ell(u)=u_\ell-\frac{u^TB_Xu}{2\xi_{0,\ell}}.
\tag{5.1}
\]
It fixes zero and has derivative identity there, so is a local diffeomorphism. Under its cotangent lift the new covector is \((dF)^T\xi\). At the fixed point,
\[
\delta\xi_{\rm new}=\delta\xi_{\rm old}-B_X\delta u.
\tag{5.2}
\]
Thus a new horizontal variation maps to \(\delta\xi_{\rm old}=B_X\delta u\). Use a nonzero component of \(\eta_0\) to construct the same change on \(Y\). These independent maps realize the full diagonal graph. Transversality means that, in the new coordinates, projection of \(\Lambda\) to all its frequency variables is locally invertible.

Write those variables as \(\theta=(\xi,\eta)\). The relation becomes a graph
\[
(x,y)=h(\theta),
\tag{5.3}
\]
where \(h\) is homogeneous of degree zero. The conic Lagrangian identity \(\alpha|_\Lambda=0\), proved in the phase-space lesson, says \(\theta\cdot dh=0\). Therefore
\[
H(\theta)=\theta\cdot h(\theta),\qquad dH=h\cdot d\theta.
\tag{5.4}
\]
This is a degree-one generating function, and
\[
x=H_\xi,\qquad y=H_\eta.
\tag{5.5}
\]
The phase
\[
\Phi=x\cdot\xi+y\cdot\eta-H(\xi,\eta)
\tag{5.6}
\]
is nondegenerate: the critical equations \((x,y)-H_\theta=0\) have independent differentials because their derivative in \((x,y)\) is identity. On the selected cone its full differential is nonzero, since \(\theta\neq0\).

Let \(n=n_X+n_Y\). The Fourier normal form of the intrinsic lesson gives, microlocally modulo a smooth kernel,
\[
K_A(x,y)=(2\pi)^{-3n/4}
\iint e^{i\Phi}b(\xi,\eta)\,d\xi\,d\eta,
\qquad b\in S^{m'-n/4}.
\tag{5.7}
\]
Its symbol is \(b|d\xi\,d\eta|^{1/2}\) in the local Maslov unit supplied by this frequency graph. This unit is a flat local frame. The normalization in (5.7) is the general \((2\pi)^{-(n+2N)/4}\) with \(N=n\).

One can also remove base dependence directly. For a phase amplitude \(b_0(x,y,\theta)\), Taylor's integral formula about \((x,y)=H_\theta\) expresses its difference from the restriction to the critical graph as \(\sum_j((x,y)_j-H_{\theta_j})b_j\). In the oscillatory integral, each such factor becomes \(-D_{\theta_j}b_j\), one lower ordinary symbol order. Derivatives of \(H_\theta\) cost one inverse frequency radius. Repeat the reduction and use the support-preserving asymptotic sum proved in H6. The compact base and angular cutoffs can be chosen inside the original working patch; H6 retains that support. Every finite remainder has the corresponding lower order, and the resulting frequency-only amplitude leaves a smooth remainder. This explains the same normal form without treating a base cutoff as a frequency-independent amplitude. All these normal forms concern an interior cone; compact base cutoffs equal to one near the point are retained for operator estimates.

## 6. Integration by parts produces the lower product order

We now prove Theorem 3.1 in the coordinates of Section 5. For fixed compact external \(X\)- and \(Y\)-sets, properness of \(P\) confines the intermediate \(X\) points to a compact set. Cut \(A\)'s two base variables off outside neighborhoods of these compact sets. That localized kernel is proper, so the ordinary composition theorem applies. The canonical relation of \(P\) is the identity graph: its local kernel phase is \((x-x')\cdot\xi\), with exactly the ordinary pseudodifferential normalization. Thus composition keeps the relation \(C\), and the cutoffs give the same product on the selected external sets. Smooth kernel errors remain smooth after composition with this localized \(A\), by the smooth-input mapping theorem and its adjoint version. Properness and the exact conic localization proof therefore allow the calculation: inserting base cutoffs equal to one near the point changes the calculation only by a microlocally smooth kernel. Acting on the \(x\) plane wave gives its left symbol \(P(x,\xi)\), so the product kernel is represented by (5.7) with amplitude \(P(x,\xi)b(\xi,\eta)\).

On the critical graph, \(p(H_\xi,\xi)=0\). Extend the local symbols over short base segments if necessary. Taylor's integral formula writes
\[
p(x,\xi)=\sum_j(x_j-H_{\xi_j})p_j(x,\xi,\eta),
\tag{6.1}
\]
\[
p_j=\int_0^1 p_{x_j}\bigl(H_\xi+t(x-H_\xi),\xi\bigr)\,dt.
\tag{6.2}
\]
Each \(p_j\) is homogeneous of degree \(m\) in the joint frequencies on the working cone. Here \(|\xi|\asymp|\theta|\), since the \(X\) covector is nonzero on its compact angular support. All derivatives have the ordinary symbol bounds: positive frequency derivatives of \(H_\xi\) have the corresponding inverse-radius loss.

Since
\[
(x_j-H_{\xi_j})e^{i\Phi}
=\frac1i\partial_{\xi_j}e^{i\Phi},
\]
integration by parts replaces the principal amplitude by
\[
-\sum_jD_{\xi_j}(p_jb)
=i\sum_j\partial_{\xi_j}(p_jb).
\tag{6.3}
\]
These derivatives hold \(x,y\) fixed. The resulting amplitude has order \(m+m'-n/4-1\). The \(r b\) term has that same order, and the \(S^{m-2}\) remainder times \(b\) has one lower order. Frequency cutoffs and oscillatory-integral continuity justify (6.3); at infinity their derivative errors vanish in the distribution limit by integration by parts. The phase theorem now gives (3.4).

To find its leading symbol, restrict this amplitude to the critical graph. Principal symbols depend on that restriction; every additional base reduction contributes another inverse frequency order. Put
\[
F_j(\xi,\eta)=p_{x_j}(H_\xi,\xi)
=p_j(H_\xi,\xi,\eta).
\tag{6.4}
\]
The coefficient of the new symbol is
\[
i\sum_jF_j\partial_{\xi_j}b
+\left(r+i\sum_j
(\partial_{\xi_j}p_j)\big|_{x=H_\xi}\right)b,
\tag{6.5}
\]
where \(r\) is evaluated at \((H_\xi,\xi)\). We next identify its scalar correction invariantly.

## 7. Half the divergence leaves exactly the subprincipal coefficient

On \(\Lambda\), the lifted Hamilton field in the frequency coordinates is
\[
W=-\sum_jF_j\partial_{\xi_j},\qquad W\eta=0.
\tag{7.1}
\]
Indeed (2.1) gives its frequency components, and Lemma 2.1 gives tangency. More explicitly, differentiating \(p(H_\xi,\xi)=0\) in \(\xi\) and \(\eta\) shows that the induced derivatives of \(H_\xi,H_\eta\) along (7.1) are respectively \(p_\xi\) and zero. These are exactly its base components.

Consequently
\[
\frac1i\mathcal L_W\bigl(b|d\xi\,d\eta|^{1/2}\bigr)
=\left(i\sum_jF_j\partial_{\xi_j}b
+\frac i2\sum_j\partial_{\xi_j}F_j\,b\right)
|d\xi\,d\eta|^{1/2}.
\tag{7.2}
\]
The derivative of \(F_j\) in (7.2) is a total derivative along the critical graph. This differs from the fixed-base derivative in (6.5).

To compare them, abbreviate, with all terms evaluated on the graph,
\[
S=\sum_j\partial_{\xi_j}p_j,
\qquad
T=\sum_{j,k}(\partial_{x_k}p_j)H_{\xi_k\xi_j}.
\tag{7.3}
\]
The chain rule gives
\[
\sum_j\partial_{\xi_j}F_j=S+T.
\tag{7.4}
\]
On the other hand, differentiate (6.1) first in \(x_k\), then in \(\xi_k\) at fixed \(x\), and restrict to the graph. The factor \(x_j-H_{\xi_j}\) then vanishes, leaving
\[
p_{x_k\xi_k}
=\partial_{\xi_k}p_k
-\sum_j(\partial_{x_k}p_j)H_{\xi_j\xi_k}.
\]
Summing and using the symmetry of the Hessian of \(H\) yields
\[
\sum_kp_{x_k\xi_k}=S-T.
\tag{7.5}
\]
Subtract (7.2) from (6.5). The remaining multiplication coefficient is
\[
r+iS-\frac i2(S+T)
=r+\frac i2(S-T)
=r+\frac i2\sum_kp_{x_k\xi_k}=c.
\tag{7.6}
\]
This proves (3.5), including its sign and density correction.

The calculation patches: \(c\) is an intrinsic scalar by the exact AN-03 half-density result, the Hamilton field is intrinsic, and the Lie derivative uses the flat Maslov transitions and intrinsic density pullback. Thus it gives the same symbol in every working patch. Altering the input symbol by one lower order alters (6.5) by one lower output order, so the formula is well defined on principal-symbol quotient classes.

Finally cotangent dilation pulls the tangent Hamilton field back by the factor \(t^{m-1}\). One can see this directly in (7.1): its coefficients have degree \(m\), while a frequency derivative costs one degree. Lie differentiation therefore raises intrinsic symbol order by \(m-1\). The coefficient \(c\) has the same degree \(m-1\). Applied to (3.3), this gives precisely \(m+m'-1+n/4\), the symbol order of (3.4). For the derivative estimates, the coefficients \(F_j\) have degree \(m\) in frequency coordinates, and their \(\alpha\)-derivatives have degree \(m-|\alpha|\). The product rule applied to \(F_j\partial_{\xi_j}b\) and \((\partial_{\xi_j}F_j)b\) therefore gives order \(m-1+\operatorname{ord}(b)\), with every derivative and finitely many input seminorms. The frequency half-density frame has degree \(n/2\), so this gives the asserted intrinsic order as well. H2–H3 transport these estimates between homogeneous charts; compact base/direction localization and the proved locally finite partitions patch them. The Taylor integrals in Section 6 have the same finite-seminorm bounds. Applying the same argument to a one-order-lower input proves the asserted quotient independence. This completes the theorem. ∎

## 8. A lifting model shows the density term directly

Take \(X=\mathbb R_s\times S^1_t\) and \(Y=\mathbb R_z\), and use the frames \(|ds\,dt|^{1/2}\), \(|dz|^{1/2}\). For a smooth periodic coefficient \(b(t)\), define
\[
(A_bg)(s,t)=b(t)g(s).
\tag{8.1}
\]
Its kernel is \(b(t)\delta(s-z)\), of order \(-1/4\). The relation has \(s=z\), the same nonzero \(s,z\) covector \(\chi\), and zero \(t\) covector. Coordinates on its kernel Lagrangian are \((s,t,\chi)\). The invariant symbol is a fixed normalized Maslov factor times
\[
b(t)|ds\,dt\,d\chi|^{1/2}.
\tag{8.2}
\]
The fixed factor is \((2\pi)^{1/4}\), from the codimension-one delta normalization, and does not affect the following differential identity.

For real smooth periodic \(v(t)\) and a smooth scalar \(q(t)\), let
\[
P=\frac12(vD_t+D_tv)+q
=vD_t-\frac i2v'+q.
\tag{8.3}
\]
This properly supported differential operator acts on half densities. Its principal symbol is \(p=v(t)\xi_t\), which vanishes on the relation, and
\[
c=-\frac i2v'+q+\frac i2\partial_t\partial_{\xi_t}p=q.
\tag{8.4}
\]
On the kernel Lagrangian, \(H_p=v\partial_t\); its divergence in \((s,t,\chi)\) is \(v'\). Formula (3.5) gives the coefficient
\[
-i\left(vb'+\frac12v'b\right)+qb.
\tag{8.5}
\]
Applying (8.3) to (8.1) gives exactly the same coefficient, with no discarded terms. Its kernel order is again \(-1/4=1-1/4-1\). This checks the transport law in an actual properly supported operator model satisfying the nonzero-covector hypotheses.

On an interval where \(v>0\), vanishing of this coefficient is the first-order equation
\[
b'+\frac{v'}{2v}b+\frac{iq}{v}b=0.
\]
Its solutions are
\[
b(t)=K v(t)^{-1/2}
\exp\left(-i\int_{t_0}^t\frac{q(u)}{v(u)}\,du\right),
\tag{8.6}
\]
with arbitrary complex constant \(K\). Differentiate to verify the equation; conversely multiplying it by \(v^{1/2}\exp(i\int q/v)\) gives derivative zero. This is a scalar transport solution, not a claim of a global parametrix construction.

## 9. Exercises with complete solutions

**Exercise 9.1 (flow and density weight; introductory).** On \(\mathbb R^2\), let \(V=u\partial_u-2w\partial_w\). Compute its flow and its Lie derivative on a half density \(f|du\,dw|^{1/2}\). Check the result by direct pullback.

**Solution.** The flow is \(F_t(u,w)=(e^tu,e^{-2t}w)\), whose positive determinant is \(e^{-t}\). Its divergence is \(1-2=-1\). Formula (1.2) gives
\[
\mathcal L_V(f|du\,dw|^{1/2})
=\left(u f_u-2w f_w-\frac12f\right)|du\,dw|^{1/2}.
\]
Direct pullback has coefficient \(e^{-t/2}f(e^tu,e^{-2t}w)\). Its derivative at zero is the same displayed expression. Differentiating only \(f\) would omit the determinant contribution.

**Exercise 9.2 (the exceptional slopes; intermediate).** In \(T^*\mathbb R^2\), let \(L\) be the graph of \(B=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Find the slopes \((b_1,b_2)\) for which \(L\) fails to be transverse to the diagonal graph \(L_b\). Find one complement and the dimension of the intersection at an exceptional slope.

**Solution.** With \(U=I,W=B\), the determinant is
\[
\det(B-\operatorname{diag}(b_1,b_2))=b_1b_2-1.
\]
The exceptional set is the hyperbola \(b_1b_2=1\), a null subset of the plane. The choice \((0,0)\) is transverse. At an exceptional slope, neither \(b_j\) is zero, the displayed matrix has determinant zero and rank one, and its kernel has dimension one. Thus the Lagrangian intersection is one-dimensional there. The failure condition concerns the two slopes together.

**Exercise 9.3 (realize two separate coordinate jets; intermediate).** At a kernel covector with \(\xi_0=2\), \(\eta_0=-3\) on \(\mathbb R\times\mathbb R\), construct separate base maps, fixing zero with derivative one, which carry their new horizontal tangent plane to the old diagonal graph of slopes \((5,7)\). Explain the role of the two nonzero covectors.

**Solution.** Take
\[
x=F(u)=u-\frac54u^2,
\qquad y=G(w)=w+\frac76w^2.
\]
Both maps are locally invertible at zero. Contracting their second derivatives with the fixed covectors gives \(2F''=-5\), \(-3G''=-7\). Therefore
\[
\delta\xi_{\rm new}=\delta\xi_{\rm old}-5\delta u,
\qquad
\delta\eta_{\rm new}=\delta\eta_{\rm old}-7\delta w.
\]
Zero new frequency variations are precisely the old slopes \((5,7)\). A zero fixed covector would contract every second derivative to zero; a base change with derivative identity could then not create an arbitrary slope in that block by this construction. This is why separate changes here use both nonzero components.

**Exercise 9.4 (a sign check with a circle mode; intermediate).** In the lifting model take \(b(t)=e^{i\ell t}\), \(\ell\in\mathbb Z\), and \(P=D_t\). Compute \(PA_b\), its order and its transport symbol. Include \(\ell=0\).

**Solution.** The principal symbol \(\xi_t\) vanishes on the relation, the subprincipal symbol is zero, and the tangent Hamilton field is \(\partial_t\), with zero divergence. Hence the transport coefficient is \((1/i)b'=\ell b\). Direct differentiation gives \(D_t e^{i\ell t}=\ell e^{i\ell t}\), so \(PA_b=\ell A_b\). For \(\ell\neq0\) its exact order is \(-1/4\), as predicted by \(1-1/4-1\); its leading symbol is nonzero. For \(\ell=0\), the product is zero and belongs to every lower order. Declared upper order need not be the exact nonzero order.

**Exercise 9.5 (a left coefficient is not the subprincipal coefficient; advanced).** In (8.3) set \(v(t)=2+\sin t\), \(q=0\). Compute the left order-zero coefficient, the subprincipal symbol and the action on the lift. Find a nonzero periodic \(b\) killed by this product.

**Solution.** The left order-zero coefficient is \(-i\cos t/2\), while the mixed principal derivative adds \(+i\cos t/2\). Thus the subprincipal symbol is zero. The action coefficient is
\[
-i\left((2+\sin t)b'+\frac12\cos t\,b\right).
\]
Take \(b=(2+\sin t)^{-1/2}\). It is smooth, positive and periodic, and
\(b'=-\frac12\cos t(2+\sin t)^{-3/2}\), so the two terms cancel exactly. Keeping only \(v b'\), or treating the left order-zero coefficient as the invariant subprincipal symbol, would give an incorrect transport formula.

**Exercise 9.6 (periodic transport has an obstruction; advanced).** Suppose \(v>0\) and \(q\) are real smooth \(2\pi\)-periodic functions in (8.3). Determine when \(PA_b=0\) has a nonzero smooth periodic solution. Give examples with and without such a solution.

**Solution.** Formula (8.6) is the complete local solution, and extends smoothly along the line because \(v>0\). Over one period the positive factor \(v^{-1/2}\) returns to its original value, while the phase is multiplied by
\[
\exp\left(-i\int_0^{2\pi}\frac{q(t)}{v(t)}\,dt\right).
\]
A nonzero solution is periodic exactly when this factor is one, equivalently when the real integral lies in \(2\pi\mathbb Z\). If it does, all its derivatives are periodic as well, by the smooth periodic differential equation, or by differentiating the explicit formula. If it does not, the only periodic solution is zero. For \(v=2+\sin t\) and \(q=v\), the solution \(b=v^{-1/2}e^{-it}\) is periodic. For the same \(v\) and \(q=v/2\), its period multiplier is \(-1\), so no nonzero periodic solution exists. The Maslov unit in this lifting model is globally fixed; this calculation asserts this model's scalar obstruction and does not omit an additional arbitrary Maslov holonomy.

## References

- [Hörmander IV, §25.2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, approved purchased reprint of the corrected second printing (1994), equation 25.2.11, Theorem 25.2.4 and Lemma 25.2.5.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
