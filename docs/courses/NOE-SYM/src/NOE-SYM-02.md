# Infinite symmetry groups and Noether's second theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Public domain (CC0).*

A constant phase change of a complex field gives a conserved charge. Allowing the phase to vary at every point requires a gauge field and produces something stronger: a differential identity among the equations of motion themselves. The identity holds for every field configuration, before solving any equations. It also explains why the corresponding current reduces to a surface term on solutions.

We use the total derivatives, Euler expressions and current convention of Variational symmetries and Noether's first theorem. Basic references are Noether's *Invariant variational problems*, §§2, 4 and 6, Compère's thesis, Part I, Chapter 1, §2 and Appendix A, and Barnich, Brandt and Henneaux's *Local BRST cohomology in gauge theories*, §§5--6. Local statements concern smooth finite-order differential functions on a contractible coordinate and jet domain. Topology and boundary conditions will be stated separately.

## 1. Why an arbitrary function is different from a parameter

Let $p=(p^1,\ldots,p^\rho)$ be arbitrary smooth functions of $x$. A gauge characteristic has the form

$$
Q^\alpha[p]=\mathcal D(p)^\alpha
=\sum_{\beta,J}R^{\alpha J}_\beta(x,u^{(m)})D_Jp^\beta.
\tag{1.1}
$$

The sum is finite; coefficients can depend on derivatives of the dynamical fields. The operator is linear in $p$, not necessarily in $u$. The formal adjoint is

$$
(\mathcal D^*f)_\beta=\sum_{\alpha,J}(-D)_J(R^{\alpha J}_\beta f_\alpha).
\tag{1.2}
$$

This adjoint reverses integration by parts, rather than referring to a Hilbert-space domain or boundary condition.

Noether distinguished finite-parameter groups, groups depending on arbitrary functions, and an intermediate case of infinitely many parameters without arbitrary functions. The operative distinction is freedom of the finite jet of $p$ at each point. A family of harmonic functions, for example, is constrained by a PDE: its jets are not arbitrary. A conclusion obtained by varying unrestricted $p$ cannot be inferred for that family.

In modern usage (1.1) describes infinitesimal gauge symmetries. The identity theorem below does not by itself prove closure of their brackets, irreducibility of their generators, or integration to a transformation group. Reducible operators can give redundant identities.

## 2. Integration by parts a second time

The product rule used for first variation supplies a second boundary term:

$$
f_\alpha\mathcal D(p)^\alpha
=p^\beta(\mathcal D^*f)_\beta+D_iK^i(p,f).
\tag{2.1}
$$

For each $J=(i_1,\ldots,i_r)$ written as the nondecreasing derivative word, one explicit choice is

$$
K^i(p,f)=\sum_{\alpha,\beta,J\ne\varnothing}\sum_{s=1}^r
\delta^i_{i_s}(-1)^{s-1}
D_{i_1}\cdots D_{i_{s-1}}(R^{\alpha J}_\beta f_\alpha)
D_{i_{s+1}}\cdots D_{i_r}p^\beta.
\tag{2.2}
$$

The same telescoping proof applies. Importantly, $K$ involves Euler expressions and their total derivatives when $f=E(L)$; all of them vanish on jets of smooth solutions.

**Theorem 2.1 (second Noether theorem).** Suppose $\operatorname{pr}v_{\mathcal D(p)}L=D_iB^i[p]$ holds as a local identity for unrestricted $p$, where $B[p]$ is a smooth finite-order differential function of the field and parameter jets. Then

$$
\mathcal D^*E(L)=0
\tag{2.3}
$$

identically. Conversely, (2.3) implies that $\mathcal D(p)$ is a divergence symmetry for every $p$, with $B[p]=P(\mathcal D(p),L)+K(p,E(L))$.

*Proof.* First variation and (2.1) give

$$
p^\beta(\mathcal D^*E(L))_\beta
=D_i\bigl(B^i[p]-P^i[\mathcal D(p)]-K^i[p,E(L)]\bigr).
\tag{2.4}
$$

Regard $p$ as an additional dependent field. Applying its Euler operator to (2.4) annihilates the divergence. The left side has no derivatives of $p$, and its coefficient is independent of $p$, so its Euler derivative is precisely $(\mathcal D^*E(L))_\beta$. This proves (2.3). Equivalently, if the boundary term is linear and homogeneous in the parameter jets, integrate against compactly supported $p$ and use the fundamental lemma. The Euler-operator proof avoids a hidden boundary assumption.

Conversely, (2.1) with $f=E(L)$ and (2.3) gives $Q[p]\cdot E(L)=\operatorname{Div}K$. First variation now gives the stated $B$. Every equality is an identity on jets, not merely a relation along solutions. $\square$

A family of separately chosen primitives for each numerical function $p$, with no common local dependence on the parameter jets, is not the hypothesis. In one independent variable every ordinary smooth function has a nonlocal antiderivative; admitting those would make the claimed theorem false.

## 3. From an identity to an improper current

Fix the current sign

$$
C[p]=P(\mathcal D(p),L)-B[p],\qquad
\operatorname{Div}C[p]=-Q[p]\cdot E(L).
$$

Equations (2.1) and (2.3) imply

$$
\operatorname{Div}(C[p]+K[p,E(L)])=0
\tag{3.1}
$$

identically. For n > 1, every identically divergence-free finite-order current has a local antisymmetric superpotential, by Theorem 3.2 below. Applied on the extended jet space that includes $p$, it gives

$$
C^i[p]=-K^i(p,E(L))+D_jS^{ij}[p].
\tag{3.2}
$$

This proves the **improper-law statement**: on solutions, $C^i[p]=D_jS^{ij}[p]$. The current has zero divergence *on solutions*; it need not have zero divergence identically. It is $C+K$, rather than $C$, that is identically divergence-free. On a noncontractible domain a closed horizontal form can have a cohomological obstruction, so this is a local decomposition.

For $n=1$, (3.1) says that $C+K$ is a constant. There is no antisymmetric two-index superpotential. For currents linear and homogeneous in unrestricted parameter jets, varying those jets forces that constant to be zero, giving $C=-K$. A parameter-independent constant can otherwise be removed by the current-equivalence convention.

For $n>1$, $D_iD_jS^{ij}=0$ because the derivatives commute and $S$ is antisymmetric. Such a current may nonetheless yield a nonzero boundary charge. On a spatial domain,

$$
\int_\Omega C^0\,d^{n-1}x
=\int_{\partial\Omega}S^{0a}n_a\,dA
\quad\text{on solutions}.
\tag{3.3}
$$

Whether this integral is finite, invariant under allowed gauge transformations, or independent of the choice of superpotential requires boundary and normalization choices. The adjective improper does not resolve those questions.

### Building a superpotential rather than assuming one

**Lemma 3.1 (operator exactness).** Suppose $T^i[h]$ are finite-order linear differential operators in an unrestricted test field $h$ and $D_iT^i[h]=0$ identically. Their coefficients are arbitrary smooth differential functions. Then $T^i[h]=D_jU^{ij}[h]$ for finite-order linear operators $U^{ij}=-U^{ji}$.

*Proof.* Treat each component of $h$ separately. Let the largest order in $h$ be $r$, and let $a^i(\zeta)$ be the homogeneous polynomial of degree $r$ formed from the principal coefficients of $T^i$. The coefficient of the derivatives of $h$ of order $r+1$ in $D_iT^i[h]=0$ says $\zeta_i a^i(\zeta)=0$. For $r=0$ this forces every coefficient to be zero. For $r\ge1$, put

$$
b^{ij}(\zeta)=\frac{\partial_{\zeta_j}a^i-\partial_{\zeta_i}a^j}{r+1}.
$$

Euler's homogeneous-function identity and differentiation of $\zeta_ja^j=0$ give $\zeta_jb^{ij}=a^i$. Replace each monomial $\zeta^J$ in $b^{ij}$ by $D_Jh$, with its coefficient on the left, to form $U^{ij}[h]$. Then $D_jU^{ij}[h]$ has the principal part of $T^i[h]$. The difference has order at most $r-1$ and still has zero divergence because $D_iD_jU^{ij}=0$. Repeat finitely many times and sum the skew operators. Derivatives of coefficients increase their field-jet order only finitely. $\square$

**Theorem 3.2 (local exactness for currents).** Let $n>1$. On a small star-shaped base coordinate ball and an unrestricted jet neighbourhood star-shaped about the jets of a reference section, every smooth finite-order current $H$ with $D_iH^i=0$ identically has a smooth finite-order skew superpotential $H^i=D_jS^{ij}$.

*Proof.* Subtract the reference section from $u$. Linearize the identity: $D_iH'[h]^i=0$ for every test field $h$, because evolutionary differentiation commutes with $D_i$. Lemma 3.1 writes $H'[h]^i=D_jU^{ij}[h]$. Evaluate the coefficients at scaled jets $\lambda u$, set $h=u$, and integrate:

$$
H^i(x,u^{(k)})-H^i(x,0)
=D_j\int_0^1 U_{\lambda u}^{ij}[u]\,d\lambda.
$$

The linearization differentiates with respect to the jet arguments before scaling, so its evaluation on $u$ is precisely $dH(x,\lambda u^{(k)})/d\lambda$. Total differentiation commutes with evaluation at scaled jets. The construction is finite and smooth. Set $h_0^i(x)=H^i(x,0)$; then $\partial_ih_0^i=0$. With the ball centred at $0$, put

$$
S_0^{ij}(x)=\int_0^1t^{n-2}\bigl(x^j h_0^i(tx)-x^i h_0^j(tx)\bigr)\,dt.
$$

Summing its derivative in $j$ gives the integral of $d[t^{n-1}h_0^i(tx)]/dt$, hence $h_0^i(x)$. The lower endpoint is zero since $n>1$. Add $S_0$ to the preceding integrated skew operator. Restricting an open full jet domain to such a neighbourhood proves local exactness. The same argument includes parameter fields as extra dependent variables. $\square$

This proves the degree $n-1$ horizontal lemma used in (3.2). It asserts neither global exactness on a noncontractible bundle nor exactness after imposing field equations. Compère, Appendix A, Theorem 20, and Barnich, Brandt and Henneaux, Theorem 4.2, provide broader accounts.



## 4. Electromagnetism and the role of a constant gauge parameter

On Minkowski space with signature $(-,+,\ldots,+)$, put

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,
\qquad L=-\frac14F_{\mu\nu}F^{\mu\nu}.
$$

Varying the potential gives

$$
\delta L=-F^{\mu\nu}\partial_\mu\delta A_\nu
=(\partial_\mu F^{\mu\nu})\delta A_\nu
-\partial_\mu(F^{\mu\nu}\delta A_\nu).
$$

Thus $E_A^\nu=\partial_\mu F^{\mu\nu}$ and $P^\mu=-F^{\mu\nu}\delta A_\nu$. The gauge characteristic is $Q_\nu[p]=\partial_\nu p$. Since $\delta F=0$, $B=0$. Its adjoint identity is

$$
\partial_\nu E_A^\nu=\partial_\nu\partial_\mu F^{\mu\nu}=0,
\tag{4.1}
$$

with an irrelevant overall minus sign in $\mathcal D^*$. Directly, interchanging the dummy indices reverses the sign of the expression, while commuting the derivatives leaves it unchanged.

Here $K^\mu=p E_A^\mu$. The Noether current is

$$
C^\mu[p]=-F^{\mu\nu}\partial_\nu p
=-p E_A^\mu+\partial_\nu(-pF^{\mu\nu}).
\tag{4.2}
$$

Thus $S^{\mu\nu}=-pF^{\mu\nu}$ and $\partial_\mu C^\mu=-E_A^\nu\partial_\nu p$. For constant $p$, the *pure Maxwell gauge transformation* is zero, and its current here is zero. Equation (4.2) expresses that zero, on solutions, as a divergence. A nonzero matter charge is not produced by a constant transformation of $A$ alone.

For scalar electrodynamics, choose charge $e\ne0$ and

$$
\mathscr D_\mu\psi=\partial_\mu\psi-ieA_\mu\psi,
\qquad L=-\tfrac14F^2-\overline{\mathscr D_\mu\psi}\,\mathscr D^\mu\psi-V(\bar\psi\psi).
\tag{4.3}
$$

Gauge variations are $\delta A_\mu=\partial_\mu p$, $\delta\psi=iep\psi$, $\delta\bar\psi=-iep\bar\psi$. The covariant derivative transforms as $\delta(\mathscr D\psi)=iep\mathscr D\psi$, so $\delta L=0$ identically. Define

$$
j^\mu=ie(\bar\psi\mathscr D^\mu\psi-\psi\overline{\mathscr D^\mu\psi}).
$$

The variation of the matter part with respect to $A$ is $-j^\mu\delta A_\mu$, hence

$$
E_A^\mu=\partial_\nu F^{\nu\mu}-j^\mu.
\tag{4.4}
$$

The scalar boundary terms give $p j^\mu$, so the gauge current is

$$
C^\mu[p]=-F^{\mu\nu}\partial_\nu p+p j^\mu
=-pE_A^\mu+\partial_\nu(-pF^{\mu\nu}).
\tag{4.5}
$$

The full Noether identity is

$$
-\partial_\mu E_A^\mu+ie\psi E_\psi-ie\bar\psi E_{\bar\psi}=0.
\tag{4.6}
$$

For constant $p=1$, the scalar transforms nontrivially and $C^\mu=j^\mu$. On solutions $j^\mu=\partial_\nu F^{\nu\mu}$. Writing $\mathcal E^a=F^{a0}$ yields

$$
Q_\Omega=\int_\Omega j^0\,d^{n-1}x
=\int_{\partial\Omega}\mathcal E^a n_a\,dA.
\tag{4.7}
$$

There is no time-derivative term since $F^{00}=0$. The equality requires the potential and fields to be smooth on the domain, or a distributional version of Gauss's theorem when sources are singular. Charge conservation additionally requires zero net spatial matter flux. The factor $e$ is included in $j$.

## 5. Reparametrization of a particle

Let $x(t)$ be a regular curve in a Riemannian manifold and $v=\dot x\ne0$. Its length density is

$$
L(x,v)=\sqrt{g_{\mu\nu}(x)v^\mu v^\nu}.
$$

It is homogeneous of degree one in $v$. Under the infinitesimal change of parameter generated by $\xi=-p(t)$ with the same geometric points, its characteristic is $Q^\mu=pv^\mu$. Reparametrization of the density gives the evolutionary identity $\operatorname{pr}v_Q(L)=D_t(pL)$. Thus $\mathcal D(p)=pv$, $\mathcal D^*E=v^\mu E_\mu$, and the second theorem gives

$$
v^\mu E_\mu(L)=0
\tag{5.1}
$$

identically on the nonzero-velocity domain.

Here is a direct proof for any degree-one density. Euler's homogeneous-function identity gives $v^\mu L_{v^\mu}=L$. Differentiating along the curve and subtracting the chain rule yields

$$
v^\mu D_tL_{v^\mu}=v^\mu L_{x^\mu},
$$

which is (5.1). The first-variation current is $P=Q^\mu L_{v^\mu}=pL$, so $C=P-B=0$ for $B=pL$. The parameter gauge does not supply another independent first integral; it expresses degeneracy of the velocity Hessian.

For a timelike curve in signature $(-,+,\ldots,+)$, use $L=\sqrt{-g(v,v)}$ on the timelike cone; the same positive-homogeneity proof applies. The expression $\sqrt{g(v,v)}$ without this sign change is not real on that cone. At zero or null velocity these length densities are not smooth, and the statement does not apply there.

## 6. Diffeomorphism invariance and the Bianchi identity

Use the curvature convention

$$
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z,
\qquad
\operatorname{Ric}(Y,Z)=\operatorname{tr}\bigl[X\mapsto R(X,Y)Z\bigr].
\tag{6.1}
$$

It makes the unit sphere have positive sectional curvature. With $R=g^{\mu\nu}\operatorname{Ric}_{\mu\nu}$ and $G_{\mu\nu}=\operatorname{Ric}_{\mu\nu}-\tfrac12Rg_{\mu\nu}$, the Einstein--Hilbert density is $\mathscr L=\sqrt{|\det g|}\,R$. We derive its first variation to make the Noether identity explicit.

For a symmetric variation $h_{\mu\nu}=\delta g_{\mu\nu}$, differentiation of $g^{-1}g=1$ and of the determinant gives

$$
\delta g^{\mu\nu}=-h^{\mu\nu},
\qquad
\delta\sqrt{|\det g|}=\tfrac12\sqrt{|\det g|}\,g^{\mu\nu}h_{\mu\nu}.
$$

The Levi-Civita variation is the tensor

$$
\delta\Gamma^\rho_{\mu\nu}
=\tfrac12g^{\rho\sigma}
(\nabla_\mu h_{\nu\sigma}+\nabla_\nu h_{\mu\sigma}-\nabla_\sigma h_{\mu\nu}).
\tag{6.2}
$$

To see this, vary $\nabla g=0$ and the symmetry of the connection in its lower two indices. The three resulting metric-compatibility equations solve for $\delta\Gamma$ by adding the first two and subtracting the third. Alternatively differentiate the coordinate formula for $\Gamma$; the extra terms combine to the covariant derivatives in (6.2).

Varying the coordinate expression for curvature yields the Palatini identity

$$
\delta\operatorname{Ric}_{\mu\nu}
=\nabla_\rho\delta\Gamma^\rho_{\mu\nu}
-\nabla_\nu\delta\Gamma^\rho_{\mu\rho}.
\tag{6.3}
$$

Indeed the variation of $\partial\Gamma+\Gamma\Gamma$ is the covariant exterior derivative of the connection variation; contracting its first and curvature-output indices gives (6.3). This computation uses neither the equations of motion nor a Bianchi identity.

By $\nabla g=0$, equations (6.2)--(6.3) give

$$
\delta R=-\operatorname{Ric}^{\mu\nu}h_{\mu\nu}
+\nabla_\rho W^\rho,\qquad
W^\rho=g^{\mu\nu}\delta\Gamma^\rho_{\mu\nu}
-g^{\mu\rho}\delta\Gamma^\nu_{\mu\nu}
=\nabla_\mu h^{\rho\mu}-\nabla^\rho(\operatorname{tr}_g h).
$$

Finally $\sqrt{|\det g|}\nabla_\rho W^\rho=\partial_\rho(\sqrt{|\det g|}W^\rho)$, because $\Gamma^\mu_{\mu\rho}=\partial_\rho\log\sqrt{|\det g|}$. Therefore

$$
\delta\mathscr L
=-\sqrt{|\det g|}\,G^{\mu\nu}h_{\mu\nu}
+\partial_\rho(\sqrt{|\det g|}W^\rho).
\tag{6.4}
$$

Symmetric $h$ is contracted over both indices; this fixes the convention without ambiguous factors for off-diagonal independent metric coordinates.

For a compactly supported vector field $\zeta$, the flow acts by pullback and its metric variation is

$$
h_{\mu\nu}=(\mathcal L_\zeta g)_{\mu\nu}
=\nabla_\mu\zeta_\nu+\nabla_\nu\zeta_\mu.
\tag{6.5}
$$

The last equality follows by inserting the coordinate formula for the Lie derivative and using $\nabla g=0$. Since the scalar density pulls back, $\delta\mathscr L=\partial_\mu(\zeta^\mu\mathscr L)$. Its action variation is zero for compact support. Equation (6.4) now implies

$$
0=-2\int\sqrt{|\det g|}\,G^{\mu\nu}\nabla_\mu\zeta_\nu\,d^nx
=2\int\sqrt{|\det g|}\,(\nabla_\mu G^{\mu\nu})\zeta_\nu\,d^nx.
$$

Metric compatibility allows the integration by parts, and no boundary term remains. The fundamental lemma for arbitrary $\zeta_\nu$ yields the contracted Bianchi identity

$$
\nabla_\mu G^{\mu\nu}=0.
\tag{6.6}
$$

The conclusion is valid for every smooth nondegenerate metric of fixed signature. It is an off-equation identity; setting $G=0$ would make the proof uninformative. A cosmological term contributes a constant multiple of $g^{\mu\nu}$ and satisfies the same identity by metric compatibility. With matter, varying all dynamical fields gives an identity involving their Euler expressions as well; the stress tensor is covariantly conserved on matter solutions.

### Why translation energy becomes a boundary law

In a generally covariant theory with no fixed background structure that breaks diffeomorphism invariance, arbitrary coordinate transformations are gauge symmetries. Coordinate translations are the specialization to constant vector fields in a chart. Applying (3.2) to those parameters shows that their energy-momentum currents are sums of terms proportional to the field equations and their derivatives, and divergences of skew superpotentials. This is the direction of Hilbert's assertion needed here, as proved by Noether in §6.

A fixed Minkowski background is a different hypothesis: translations are global spacetime symmetries of the matter fields, and their energy current need not be improper. Conversely, a local improper-law representation alone does not prove integration of arbitrary generalized generators to a finite transformation group. Our statement is about the variational identity and the existing diffeomorphism action.

## 7. A regular mechanical system has no genuine parameter gauge

The free density $L=\tfrac12m|\dot q|^2$, $m>0$, has $E=-m\ddot q$. Its acceleration Hessian is invertible, so it has no nontrivial Noether identity after trivial identities are factored out. The qualification is essential: for a skew constant matrix $M$, the expression $(ME)\cdot E=0$ is an identity, and $Q[p]=pME$ is a divergence symmetry that vanishes on solutions. It is a trivial parameter gauge.

We give the elementary algebra behind the qualification. At each finite order, the prolonged equations $D_t^rE_a=-m q_a^{(r+2)}$ are independent coordinates, with $t,q,\dot q$ as unconstrained coordinates. Any linear relation among these equations is a relation among independent coordinate functions $z_a$. If $\sum_a f_a(z)z_a=0$ locally on a star-shaped coordinate neighbourhood of $z=0$, then

$$
f_a(z)=\sum_b M_{ab}(z)z_b,\qquad M_{ab}=-M_{ba}.
\tag{7.1}
$$

To prove this, differentiating $\sum z_af_a=0$ shows $f_a(0)=0$ and
$z_b(\partial_bf_a-\partial_af_b)=(z\cdot\partial)f_a+f_a$. Integrate this identity along $tz$:

$$
M_{ab}(z)=\int_0^1t\bigl(\partial_bf_a-\partial_af_b\bigr)(tz)\,dt.
$$

The right side multiplied by $z_b$ is $\int_0^1d[t f_a(tz)]/dt\,dt=f_a(z)$. If coefficients also depend on unconstrained coordinates, hold them fixed. Consequently every finite-order Noether relation for the free particle is built from skew pairwise cancellations of the equations and their derivatives. Integration by parts translates these into trivial, equation-vanishing gauge characteristics. The proof of this last translation, including general normal systems, is given in the current-symmetry correspondence of the preceding lesson.

Thus the meaningful conclusion is absence of a *nontrivial* arbitrary-function gauge, not absence of every identity. The finite point symmetries listed in mechanics do not exhaust all generalized symmetries, and their parameter count alone is not a proof of gauge nondegeneracy.

## 8. From the current to a stationary black-hole first law

A local gauge current becomes a boundary charge only after boundary conditions and a surface have been chosen. We now prove the stationary first-law statement behind Wald's Noether-charge construction. This also shows which part comes from the local theorem and which hypotheses belong to the global problem.

Let $M$ be an oriented Lorentzian $n$-manifold, $n>2$, and let $\phi$ include its metric and all dynamical tensor fields. Take a finite-order diffeomorphism-covariant Lagrangian $n$-form $\mathbf L$. Fix a local first-variation potential $\boldsymbol\Theta$, linear in the variation, so that

$$
\delta\mathbf L=\mathbf E\cdot\delta\phi+d\boldsymbol\Theta(\phi,\delta\phi).
\tag{8.1}
$$

We require the potential and charge construction to be covariant under the background Killing flow. A covariant potential can be obtained for Lagrangians expressed in tensor fields, curvature and their covariant derivatives: vary every factor, vary the connection through $\delta\Gamma$, and integrate covariant derivatives off $\delta\phi$ until only Euler expressions remain. At each step the product rule gives a tensor boundary term; a vector density is the same object as an $(n-1)$-form. This is the covariant version of the explicit finite integration by parts in the first lesson. A fixed auxiliary connection may also be used if it is preserved by that flow. All choices of potential and boundary counterterms must be kept fixed through the argument.

### The charge variation identity

For a fixed vector field $\xi$, covariance and Cartan's formula give
$\mathcal L_\xi\mathbf L=d(i_\xi\mathbf L)$. Thus

$$
\mathbf J_\xi=\boldsymbol\Theta(\phi,\mathcal L_\xi\phi)-i_\xi\mathbf L,
\qquad d\mathbf J_\xi=-\mathbf E\cdot\mathcal L_\xi\phi.
\tag{8.2}
$$

The arbitrary-vector-field identity and §3 produce
$\mathbf J_\xi=d\mathbf Q_\xi$ on solutions. The construction can be made linear in $\xi$ and its finitely many derivatives. Here is why a covariant construction exists, rather than merely a chartwise primitive. Integration by parts in $\mathbf E\cdot\mathcal L_\xi\phi$ first adds an equation-proportional current to make $\mathbf J_\xi$ identically closed. Apply the symbol argument of §3 to this differential operator in $\xi$, using symmetrized covariant derivatives. Its leading symbols are tensors. The formula for $b^{ij}$ uses tensor symmetrization and contraction and therefore defines a tensor coefficient. Subtracting the divergence of the corresponding skew tensor lowers the operator order. Commutators of covariant derivatives contribute only lower-order curvature terms, which are treated at the next steps. The double divergence of a skew two-tensor is zero: its commutator contracts a symmetric Ricci tensor with a skew tensor. At order zero, the coefficient of each first derivative of the freely chosen $\xi$ must vanish. This finite recursion gives a global, locally constructed charge form wherever the tensor Lagrangian and potential are defined. It has no parameter-independent remainder because the entire current is linear in $\xi$.

Let $\delta\phi$ be a tangent to solutions, and define the alternating, bilinear symplectic current by

$$
\boldsymbol\omega(\phi;\delta_1\phi,\delta_2\phi)
=\delta_1\boldsymbol\Theta(\phi,\delta_2\phi)
-\delta_2\boldsymbol\Theta(\phi,\delta_1\phi).
$$

The variations commute; equivalently take the exterior derivative in field space. On the background equations, (8.1) and Cartan's formula yield

$$
\begin{aligned}
\delta\mathbf J_\xi
&=\delta\boldsymbol\Theta(\phi,\mathcal L_\xi\phi)
-i_\xi d\boldsymbol\Theta(\phi,\delta\phi)\\
&=\boldsymbol\omega(\phi;\delta\phi,\mathcal L_\xi\phi)
+d\bigl(i_\xi\boldsymbol\Theta(\phi,\delta\phi)\bigr).
\end{aligned}
\tag{8.3}
$$

For the second line, covariance identifies the variation along the Killing flow of the potential with its Lie derivative. The terms containing $\mathcal L_\xi\delta\phi$ cancel; this cancellation is why $\omega$ is bilinear in the two tangent variations.

If $\mathcal L_\xi\phi=0$ on the background, $\omega$ vanishes. Since the perturbation solves the linearized equations, variation of the equation-proportional part of (8.2) also vanishes. Consequently

$$
d\bigl(\delta\mathbf Q_\xi-i_\xi\boldsymbol\Theta\bigr)=0.
\tag{8.4}
$$

This identity holds even when the perturbation is not stationary. It is the conservation law that compares two boundary surfaces.

### Global hypotheses and Stokes' theorem

Suppose the background has a smooth bifurcate Killing horizon with compact oriented bifurcation surface $B$, and that a hypersurface $\Sigma$ has boundaries $B$ and an asymptotic surface at infinity. Suppose all dynamical fields are smooth at $B$ and invariant under the horizon Killing field

$$
\xi=T+\sum_a\Omega_H^a\Phi_a,
$$

where $T$ is the chosen asymptotic time translation and $\Phi_a$ the chosen axial generators. Assume the boundary conditions make the following surface variations finite and integrable:

$$
\delta\mathcal E=\int_\infty
(\delta\mathbf Q_T-i_T\boldsymbol\Theta),\qquad
\delta\mathcal J_a=-\int_\infty
(\delta\mathbf Q_{\Phi_a}-i_{\Phi_a}\boldsymbol\Theta).
\tag{8.5}
$$

“Integrable” means these one-forms on the allowed solution space are differentials of functions $\mathcal E,\mathcal J_a$. It is a hypothesis about the theory and boundary conditions, not a consequence of Noether's theorem. For example, if
$\int_\infty i_T\boldsymbol\Theta=\delta\int_\infty i_T\mathbf B$ for a chosen boundary form $\mathbf B$, then
$\mathcal E=\int_\infty(\mathbf Q_T-i_T\mathbf B)$ satisfies (8.5). When $\Phi_a$ is tangent to the integration surface, the pullback of $i_{\Phi_a}\Theta$ is zero, since an alternating $(n-1)$-form is then evaluated on dependent tangent vectors.

Orient the boundaries so that Stokes' theorem reads “infinity minus $B$.” Hold $\xi$, and hence the background values $\Omega_H^a$, fixed. Since $\xi=0$ on $B$, integrating (8.4) gives

$$
\delta\mathcal E-\sum_a\Omega_H^a\delta\mathcal J_a
=\int_B\delta\mathbf Q_\xi.
\tag{8.6}
$$

There is no $\mathcal J_a\delta\Omega_H^a$ term: the charge variation here belongs to a fixed background generator.

### Removing the Killing field from the horizon density

We next restrict to a smooth family of nearby stationary solutions with such bifurcation surfaces and nonzero surface gravity $\kappa$. The following geometric reduction makes the right side of (8.6) a variation of a local functional.

The Killing equation implies that every derivative of $\xi$ of order at least two is determined by curvature, its covariant derivatives, $\xi$ and $\nabla\xi$. To prove the first step, put
$T_{abc}=\nabla_a\nabla_b\xi_c$ and
$K_{abc}=T_{abc}-T_{bac}=-R^d{}_{cab}\xi_d$, with the curvature convention of §6. Differentiating the Killing equation gives $T_{abc}=-T_{acb}$. Cycling these two relations yields

$$
2T_{abc}=K_{abc}+K_{cba}-K_{acb}.
\tag{8.7}
$$

Differentiating (8.7) repeatedly and replacing every resulting second derivative by (8.7) proves the assertion at all finite orders. Thus the charge, which is linear in the Killing field and its derivatives, reduces to a local form linear in $\xi$ and $\nabla\xi$.

On $B$, $\xi$ vanishes. Its derivative kills tangent vectors to $B$, by differentiating this zero restriction, and is skew with respect to the metric by the Killing equation. It therefore acts on the two-dimensional Lorentzian normal plane as a boost,
$\nabla_a\xi_b=\kappa\epsilon_{ab}$, where the binormal orientation fixes the sign of $\kappa$ and $\epsilon_{ab}\epsilon^{ab}=-2$. Equation (8.7) shows that $\nabla\xi$ is parallel along $B$, since $\xi=0$ there. Hence $\kappa$ is constant on each connected component. For simplicity take one component.

In the reduced charge replace $\xi$ by zero and $\nabla\xi$ by $\epsilon$. Call the resulting local $(n-2)$-form $\widetilde{\mathbf Q}$. Define

$$
\mathcal S=2\pi\int_B\widetilde{\mathbf Q}.
\tag{8.8}
$$

For any stationary member, $\mathbf Q_\xi|_B=\kappa\widetilde{\mathbf Q}$. Differentiating this equality while allowing $\xi$ to vary would introduce a $\delta\kappa$ term. That is not the variation in (8.6), where $\xi$ is fixed. We now justify the required identification of neighbouring solutions.

Identify their bifurcation surfaces smoothly, and identify their oriented, time-oriented normal bundles by Lorentzian isometries. Use their normal exponential maps to identify collars of $B$. An isometry fixing $B$ commutes with the exponential map: both sides are geodesics with the same initial point and transformed initial velocity, hence agree by uniqueness of the geodesic equation. Its action on each normal fibre is therefore its derivative at $B$. The normalized generator $\widetilde\xi=\xi/\kappa$ has the same unit boost on those fibres for every member. In these identified collars it is one fixed vector field. This construction is independent of a local normal frame, since oriented Lorentzian frame changes commute with that boost. Extend the identification smoothly to the exterior, using a cutoff to keep the chosen asymptotic coordinates fixed.

Let $\kappa_0$ denote the background value. In the collar hold the vector field $\xi=\kappa_0\widetilde\xi$ fixed while varying the fields. The globally fixed vector field need be Killing only for the background; (8.4) imposes no Killing condition on its perturbed extension away from the collar. Linearity of the charge now gives, with $B$ identified,

$$
\int_B\delta\mathbf Q_\xi
=\kappa_0\,\delta\int_B\widetilde{\mathbf Q}.
$$

Combining this equality with (8.6) proves the stationary first law

$$
\boxed{\quad
\delta\mathcal E-\sum_a\Omega_H^a\delta\mathcal J_a
=\frac{\kappa_0}{2\pi}\,\delta\mathcal S.\quad}
\tag{8.9}
$$

This is Wald's mechanical Noether-charge entropy formula for stationary perturbations, proved here from first variation, the local charge construction, Killing geometry and Stokes' theorem. It includes finite higher-derivative covariant tensor Lagrangians with the stated regularity and boundary hypotheses. The proof establishes neither charge integrability for arbitrary boundary conditions nor a dynamical entropy law or a quantum temperature formula. Those are additional mathematical questions; they are not hidden steps in (8.9). Compère's treatment of exact and asymptotic charges develops such boundary choices in specific theories.

## 9. Exercises

**Exercise 9.1 (easy).** Derive the Maxwell Euler expression and verify (4.1) without imposing Maxwell's equations. Compute the current for a nonconstant gauge parameter and explain what changes for a constant parameter.

**Exercise 9.2 (medium).** For $L=\sqrt{g(v,v)}$ in positive signature, prove $v\cdot E=0$ directly and from reparametrization. State the velocity domain and show why the current is zero.

**Exercise 9.3 (medium).** In scalar electrodynamics with the conventions (4.3), compute the matter variation with respect to $A$, derive (4.6), and express charge in a ball as an electric flux integral.

**Exercise 9.4 (medium).** For the two-component free particle, construct a trivial arbitrary-function characteristic with a skew matrix, verify its divergence symmetry, and prove that it does not represent a genuine gauge freedom.

**Exercise 9.5 (hard).** Derive (6.6) from an arbitrary compactly supported infinitesimal diffeomorphism, including the Einstein--Hilbert Euler expression and the sign of the integration by parts.

## 10. Solutions

**Solution 9.1.** Differentiating $-\tfrac14F^2$ gives $-F^{\mu\nu}\partial_\mu\delta A_\nu$, hence $E_A^\nu=\partial_\mu F^{\mu\nu}$. The symmetric operator $\partial_\mu\partial_\nu$ contracted with the skew tensor $F^{\mu\nu}$ gives zero. For $Q_\nu=\partial_\nu p$, the boundary term is $P^\mu=-F^{\mu\nu}\partial_\nu p$, with $B=0$. Formula (4.2) follows by the product rule and $E_A^\mu=-\partial_\nu F^{\mu\nu}$. For constant $p$, $Q=0$ and $P=0$; there is no charged matter current in this example.

**Solution 9.2.** On $v\ne0$, $L_{v^\mu}=g_{\mu\nu}v^\nu/L$ and $v^\mu L_{v^\mu}=L$. Differentiate the latter identity. Subtract $D_tL=L_{x^\mu}v^\mu+L_{v^\mu}a^\mu$ to obtain $v^\mu(L_{x^\mu}-D_tL_{v^\mu})=0$. For $Q=pv$, the first variation is $p\,\operatorname{pr}v_v L+p'v^\mu L_{v^\mu}=pD_tL+p'L=D_t(pL)$. Hence the second theorem gives the same identity, and the first current $P-B=pL-pL$ is zero. For timelike Lorentzian curves change $g(v,v)$ to $-g(v,v)$ and restrict to the timelike cone.

**Solution 9.3.** The variations are $\delta\mathscr D_\mu\psi=-ie\psi\,\delta A_\mu$ and $\delta\overline{\mathscr D_\mu\psi}=ie\bar\psi\,\delta A_\mu$. Substitution in the kinetic term gives $-ie(\bar\psi\mathscr D^\mu\psi-\psi\overline{\mathscr D^\mu\psi})\delta A_\mu=-j^\mu\delta A_\mu$. Thus $E_A^\mu=\partial_\nu F^{\nu\mu}-j^\mu$. In the adjoint identity the gauge operator has components $(\partial_\mu,ie\psi,-ie\bar\psi)$, giving $-\partial_\mu E_A^\mu+ie\psi E_\psi-ie\bar\psi E_{\bar\psi}=0$. On all equations, $j^0=\partial_aF^{a0}$; integrating over the ball and applying the divergence theorem gives (4.7). Constant phase charge and local gauge parameter refer to different symmetry families, although $p=1$ specializes the latter to the former on matter.

**Solution 9.4.** Set $M=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ and $Q[p]=pME$. Then $Q[p]\cdot E=pE^TME=0$ for every jet. First variation gives $\operatorname{pr}v_Q L=D_t(m\dot q\cdot Q)$, so choose that expression as $B$ and obtain zero current. The characteristic vanishes on solutions. It is a skew cancellation, not a redundancy among independent acceleration equations. More generally the coordinates $q_a^{(r+2)}$ are independent; equation (7.1) proves that every identity is a skew cancellation after prolongation. There is therefore no nontrivial gauge class.

**Solution 9.5.** Equations (6.2)--(6.4), obtained by varying metric compatibility, curvature and the determinant, give $E_g^{\mu\nu}=-\sqrt{|g|}G^{\mu\nu}$. Under pullback by the flow of $\zeta$, $h_{\mu\nu}=\nabla_\mu\zeta_\nu+\nabla_\nu\zeta_\mu$ and $\delta\mathscr L=\partial_\mu(\zeta^\mu\mathscr L)$. Compact support eliminates both boundary terms. Symmetry of $G$ gives $-2\int\sqrt{|g|}G^{\mu\nu}\nabla_\mu\zeta_\nu$. Covariant integration by parts changes the sign and produces $2\int\sqrt{|g|}(\nabla_\mu G^{\mu\nu})\zeta_\nu$. The fundamental lemma gives $\nabla_\mu G^{\mu\nu}=0$ for every metric, without using $G=0$.

## Proof dependencies

The first-variation identity and identity-level first theorem are proved in Variational symmetries and Noether's first theorem. The local superpotential lemma is proved in §3, and the metric variation needed for Bianchi is proved in §6. Smooth manifolds, the Levi-Civita connection, and the divergence theorem are background from the programme's [Smooth Manifolds and Differential Geometry](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D50). Section 8 proves the charge-variation identity and the stationary black-hole first law, including the Killing-jet reduction and the normal-bundle identification needed for the entropy variation. Charge integrability and the stated global boundary conditions are explicit hypotheses.

## References

- Emmy Noether, *Invariante Variationsprobleme* (1918), §§2, 4--6. [English edition](https://kokunoyumeto.github.io/emmy-noether-en/); [original paper record](https://eudml.org/doc/59024).
- Geoffrey Compère, *Symmetries and conservation laws in Lagrangian gauge theories with applications to the mechanics of black holes and to gravity in three dimensions* (2007), Preamble §§1--3, Part I, Chapter 1, §2, and Appendix A, Theorem 20. [Thesis](https://arxiv.org/abs/0708.3153).
- Glenn Barnich, Friedemann Brandt and Marc Henneaux, *Local BRST cohomology in gauge theories*, Physics Reports **338** (2000), 439--569, Theorem 4.2 and §§5--6. [Article](https://arxiv.org/abs/hep-th/0002245).
- Robert M. Wald, *Black hole entropy is Noether charge*, Physical Review D **48** (1993), R3427--R3431, equations (3)--(26), especially the fixed-generator variation and stationary horizon normalization. [Article](https://arxiv.org/abs/gr-qc/9307038).

