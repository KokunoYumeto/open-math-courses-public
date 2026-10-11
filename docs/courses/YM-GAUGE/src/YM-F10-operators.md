# The Euclidean and Lorentzian linearized Yang–Mills equations

Companion to Lesson YM-F10. Starting from the action and field equation of Lesson 7, we calculate the complete linearized equation. A principal symbol records its highest derivative terms at a point; the calculation below defines that operation and uses it to compare Euclidean geometry with physical-time propagation. Sections 7–8 give exact solutions and their action and energy. Section 10 includes four exercises with full solutions.

## 1. Background, metric, and the exact variation

Let \(U\) be an open coordinate domain in a smooth four-manifold, with a fixed smooth nondegenerate metric \(g_{\mu\nu}\), of either positive signature or signature \((-+++)\). Indices run over \(0,1,2,3\); every repeated pair is a full ordered sum. Set \(w=\sqrt{|\det g|}\). Let \(G\subset U(N)\), let \(\mathfrak g\) be its real skew-Hermitian Lie algebra, and retain \(\kappa(X,Y)=-\operatorname{tr}(XY)\), \(g_{\mathrm{YM}}\ne0\), and \(\hbar>0\).

Fix an arbitrary smooth connection \(A=A_\mu dx^\mu\), not assumed to satisfy the field equation. It is the connection called \(\Gamma\) in F07; no coupling is absorbed into a new variable. Write


\[
 D_\mu X=\partial_\mu X+[A_\mu,X],\qquad
 F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu],
 \tag{E.1}
\]


\[
 \mathcal E^\nu(A)=\frac1wD_\mu(wF^{\mu\nu}),\qquad
 F^{\mu\nu}=g^{\mu\rho}g^{\nu\sigma}F_{\rho\sigma}.
 \tag{E.2}
\]


This is precisely F7.14. The notation \(D_\mu\) in density expressions acts on the displayed matrix coefficient by partial derivative and commutator; the density factor and all inverse-metric factors remain inside its partial derivative. This convention avoids silently treating coordinate indices as constant on a varying metric.

For a smooth adjoint-valued one-form \(a\), introduce a dimensionless real parameter \(\varepsilon\). Expanding the original curvature gives


\[
 F_{\mu\nu}(A+\varepsilon a)
 =F_{\mu\nu}+\varepsilon B_{\mu\nu}
                        +\varepsilon^2[a_\mu,a_\nu],\qquad
 B_{\mu\nu}=D_\mu a_\nu-D_\nu a_\mu.
 \tag{E.3}
\]


The exact linearization \(L_Aa=(d/d\varepsilon)_0\mathcal E(A+\varepsilon a)\) is


\[
 \boxed{(L_Aa)^\nu=
   \frac1wD_\mu\left(wg^{\mu\rho}g^{\nu\sigma}
                         (D_\rho a_\sigma-D_\sigma a_\rho)\right)
                    +[a_\mu,F^{\mu\nu}].}
 \tag{E.4}
\]


The second term comes from varying the connection in the outer covariant derivative; it is present at every background with noncommuting curvature. This proof follows directly by differentiating the three terms in (E.3) and the two terms in \(D_\mu\), with the metric fixed.

Here is an expansion which displays every coefficient of every derivative of \(a\). Define


\[
 K^{\mu\rho\nu\sigma}=g^{\mu\rho}g^{\nu\sigma}-g^{\mu\sigma}g^{\nu\rho},
 \qquad H^{\rho\nu\sigma}=\frac1w\partial_\mu(wK^{\mu\rho\nu\sigma}).
 \tag{E.5}
\]


Then (E.4) is exactly


\[
 \begin{aligned}
 (L_Aa)^\nu={}&K^{\mu\rho\nu\sigma}\partial_\mu\partial_\rho a_\sigma
       +H^{\rho\nu\sigma}\partial_\rho a_\sigma\\
 &+K^{\mu\rho\nu\sigma}
       \bigl([A_\rho,\partial_\mu a_\sigma]
                    +[A_\mu,\partial_\rho a_\sigma]\bigr)\\
 &+H^{\rho\nu\sigma}[A_\rho,a_\sigma]
       +K^{\mu\rho\nu\sigma}[\partial_\mu A_\rho,a_\sigma]\\
 &+K^{\mu\rho\nu\sigma}[A_\mu,[A_\rho,a_\sigma]]
       +[a_\mu,F^{\mu\nu}].
 \end{aligned}\tag{E.6}
\]


To verify it, antisymmetry rewrites the raised \(B\) in (E.4) as \(K^{\mu\rho\nu\sigma}(\partial_\rho a_\sigma+[A_\rho,a_\sigma])\). The outer partial derivative gives the first, second, fourth, fifth and first commutator-derivative terms; the outer commutator gives the remaining derivative term and nested commutator. Thus (E.6) retains the first derivatives of the metric, the first derivatives of the background, and all zero-order curvature terms.

## 2. The actual infinitesimal gauge map and both Bianchi identities

For a smooth dimensionless \(\chi:U\to\mathfrak g\), set \(u_\varepsilon=\exp(\varepsilon\chi)\). The original gauge transformation is


\[
 A^{u_\varepsilon}=u_\varepsilon A u_\varepsilon^{-1}
                              -(du_\varepsilon)u_\varepsilon^{-1}.
\]


Its derivative at zero is the precise one-form


\[
 I_A\chi:=\left.\frac d{d\varepsilon}\right|_0 A^{u_\varepsilon}
          =[\chi,A]-d\chi=-D_A\chi.
 \tag{E.7}
\]


Gauge covariance of the curvature follows by inserting the gauge expression in \(dA+A\wedge A\), using \(d(u^{-1})=-u^{-1}(du)u^{-1}\); its value is \(F^u=uFu^{-1}\). For every adjoint-valued coefficient \(X\), the same product rule gives \(D_\mu^u(uXu^{-1})=u(D_\mu X)u^{-1}\). The scalar metric and density commute with \(u\). Applying this to (E.2) gives \(\mathcal E^\nu(A^u)=u\mathcal E^\nu(A)u^{-1}\). Differentiation now proves the full background-dependent identity


\[
 \boxed{L_A(-D_A\chi)^\nu=[\chi,\mathcal E^\nu(A)].}
 \tag{E.8}
\]


At a solution \(\mathcal E(A)=0\), all infinitesimal gauge directions are in \(\ker L_A\). At an arbitrary background their image is the right side of (E.8), rather than an assumed zero. At the curvature level, expanding the derivative commutator gives


\[
 [D_\mu,D_\nu]\chi=[F_{\mu\nu},\chi],\qquad
 B_{\mu\nu}(-D\chi)=-[F_{\mu\nu},\chi]=[\chi,F_{\mu\nu}],
 \tag{E.9}
\]


in agreement with the derivative of the actual curvature transformation. The first equality follows by expanding two second derivatives: mixed partials cancel, the remaining derivatives of \(A\) give their two curvature terms, and Jacobi turns the nested commutators into \([[A_\mu,A_\nu],\chi]\).

The differential-form Bianchi identity is


\[
 D_AF=dF+A\wedge F-F\wedge A=0.
 \tag{E.10}
\]


Indeed \(dF=dA\wedge A-A\wedge dA\), while \(A\wedge F-F\wedge A=A\wedge dA-dA\wedge A\). Differentiating this identity for \(A+\varepsilon a\) and using (E.3) proves its exact linearized version


\[
 D_AB+a\wedge F-F\wedge a=0,\qquad B=D_Aa=da+A\wedge a+a\wedge A.
 \tag{E.11}
\]


Equivalently \(D_A^2a=F\wedge a-a\wedge F\); expanding the four products in the left side gives this equality with the same signs. In components (E.11) retains the six terms


\[
 D_\lambda B_{\mu\nu}+D_\mu B_{\nu\lambda}+D_\nu B_{\lambda\mu}
  +[a_\lambda,F_{\mu\nu}]+[a_\mu,F_{\nu\lambda}]+[a_\nu,F_{\lambda\mu}]=0.
 \tag{E.12}
\]


There is also an exact divergence identity for the field equation. Write \(J^{\mu\nu}=wF^{\mu\nu}\), an antisymmetric matrix coefficient. Swapping the summed indices in half the expression gives


\[
 D_\nu(w\mathcal E^\nu)=D_\nu D_\mu J^{\mu\nu}
  =\tfrac12[D_\nu,D_\mu]J^{\mu\nu}
  =\tfrac w2[F_{\nu\mu},F^{\mu\nu}]=0.
 \tag{E.13}
\]


The last zero is an algebraic contraction, not a commutativity assumption about the curvature: it is \(-w g^{\mu\rho}g^{\nu\sigma}[F_{\mu\nu},F_{\rho\sigma}]/2\), and interchange of the two pairs negates the bracket while preserving its coefficient. No derivatives of \(w\) have been dropped: they were included in \(J\) before the derivative commutator was taken. Differentiating (E.13) proves


\[
 \frac1wD_\nu\bigl(w(L_Aa)^\nu\bigr)
                      +[a_\nu,\mathcal E^\nu(A)]=0.
 \tag{E.14}
\]


Thus at a solution there are two actual consecutive-zero maps:
\(\chi\mapsto-D_A\chi\mapsto L_A(-D_A\chi)=0\), and
\(a\mapsto L_Aa\mapsto w^{-1}D_\nu(w(L_Aa)^\nu)=0\).
Equations (E.8), (E.11) and (E.14) give their complete counterparts at an arbitrary background.

## 3. The principal symbol and its exact gauge kernel

Fix a point \(p\), a nonzero real cotangent vector \(\xi=\xi_\mu dx^\mu\), and define
\(q_g(\xi)=g^{\mu\nu}(p)\xi_\mu\xi_\nu\), \(\xi^\mu=g^{\mu\nu}(p)\xi_\nu\). Our symbol convention replaces each occurrence of \(\partial_\mu\) in the highest-order part by \(i\xi_\mu\). It can be derived by applying the operator to \(e^{i\lambda\phi}a\), with \(d\phi(p)=\xi\), and extracting the coefficient of \(\lambda^2\) at \(p\); derivatives of the coefficient functions or amplitude contribute lower powers of \(\lambda\). Complex exponentials here merely define the complexified symbol; the original connection and variation remain real elements of the skew-Hermitian Lie algebra.

Lower the output index with the original metric. Equation (E.6) gives


\[
 \boxed{\bigl(\sigma_2(L_A)(\xi)a\bigr)_\nu
             =-q_g(\xi)a_\nu+\xi_\nu\xi^\sigma a_\sigma.}
 \tag{E.15}
\]


The gauge-map and divergence-map symbols are respectively
\(\sigma_1(I_A)(\xi)\chi=-i\xi\chi\) and
\(a\mapsto i\xi^\mu a_\mu\). Both adjacent compositions with (E.15) vanish, since \(\xi^\mu\xi_\mu=q_g(\xi)\). This is the highest-order part of the exact identities in §2.

If \(q_g(\xi)\ne0\), then \(\sigma_2(L_A)(\xi)a=0\) implies
\(a_\nu=\xi_\nu(\xi^\sigma a_\sigma)/q_g(\xi)\). Conversely every \(a=\xi\chi\) is in the kernel. Thus the entire kernel is exactly the gauge direction \(\xi\otimes\mathfrak g\), and the symbol acts as \(-q_g(\xi)\) on the transverse subspace \(\xi^\sigma a_\sigma=0\). These two spaces give a direct sum when \(q_g(\xi)\ne0\).

If \(q_g(\xi)=0\), (E.15) instead has kernel exactly
\(\{a:\xi^\sigma a_\sigma=0\}\), and image \(\xi\otimes\mathfrak g\). The contraction functional is nonzero because the metric is nondegenerate and \(\xi\ne0\), so it is surjective on each Lie-algebra coefficient. If \(d=\dim_\mathbb R\mathfrak g\), the kernel has dimension \(3d\), the image dimension \(d\), and the gauge subspace has dimension \(d\) inside that kernel. The quotient kernel by gauge has dimension \(2d\). This is an exact symbol calculation, without identifying it with a classification of nonlinear fields or quantum states.

Even in Euclidean signature the ungauged operator is not elliptic as an operator on all one-forms: its symbol has the nonzero gauge kernel at every \(\xi\ne0\). The next section removes that degeneracy at the operator level while retaining its gauge equation.

## 4. Background divergence gauge, all lower terms, and the action factor

Define the background divergence and scalar covariant operator by


\[
 G_A(a)=\frac1wD_\mu(wg^{\mu\sigma}a_\sigma),\qquad
 \Delta_A\chi=\frac1wD_\mu(wg^{\mu\sigma}D_\sigma\chi).
 \tag{E.16}
\]


All matrix entries of \(G_A(a)\) are scalars in coordinate indices. Put \(D^\nu=g^{\nu\lambda}D_\lambda\) on such adjoint scalars, and define the gauge-fixed linearized operator


\[
 \boxed{(P_Aa)^\nu=(L_Aa)^\nu+D^\nu G_A(a).}
 \tag{E.17}
\]


The plus sign cancels the negative gradient-of-divergence in the leading part of (E.4). The equation consisting of \(P_Aa=0\) together with \(G_A(a)=0\) is equivalent to \(L_Aa=0\) together with that same gauge condition, directly by (E.17).

To display every additional coefficient, set
\(b^\sigma=w^{-1}\partial_\mu(wg^{\mu\sigma})\). Then
\(G_A(a)=g^{\rho\sigma}\partial_\rho a_\sigma+b^\sigma a_\sigma+g^{\rho\sigma}[A_\rho,a_\sigma]\), and


\[
 \begin{aligned}
 D^\nu G_A(a)=g^{\nu\lambda}\bigl\{&
 g^{\rho\sigma}\partial_\lambda\partial_\rho a_\sigma
  +(\partial_\lambda g^{\rho\sigma})\partial_\rho a_\sigma
  +b^\sigma\partial_\lambda a_\sigma\\
 &+g^{\rho\sigma}[A_\rho,\partial_\lambda a_\sigma]
  +g^{\rho\sigma}[A_\lambda,\partial_\rho a_\sigma]\\
 &+(\partial_\lambda b^\sigma)a_\sigma
  +(\partial_\lambda g^{\rho\sigma})[A_\rho,a_\sigma]
  +g^{\rho\sigma}[\partial_\lambda A_\rho,a_\sigma]\\
 &+b^\sigma[A_\lambda,a_\sigma]
  +g^{\rho\sigma}[A_\lambda,[A_\rho,a_\sigma]]\bigr\}.
 \end{aligned}\tag{E.18}
\]


Equations (E.6) and (E.18), added without omission, are the full second-, first-, and zero-order operator for an arbitrary smooth metric and arbitrary background. They include second derivatives of the metric in \(\partial_\lambda b^\sigma\). No constant-metric approximation is used.

These are operators on the actual adjoint bundle, not only on a selected matrix chart. Under a fixed finite gauge transformation \(u\), the connection path transforms exactly as \((A+\varepsilon a)^u=A^u+\varepsilon uau^{-1}\). Differentiating the already proved covariance of \(\mathcal E\) therefore gives \(L_{A^u}(uau^{-1})=u(L_Aa)u^{-1}\). The derivative product rule before (E.8) similarly gives \(G_{A^u}(uau^{-1})=uG_A(a)u^{-1}\), and then the same equality for \(P\) follows from (E.17). These formulas prove the overlap maps for all three operators. Under an actual coordinate change \(x=f(y)\), with \(J^\nu{}_b=\partial x^\nu/\partial y^b\) and inverse \(K^b{}_\nu\), the variation is \(\widetilde a_b=J^\nu{}_b a_\nu\circ f\). Differentiating F7.19 with its fixed coordinate change gives \((\widetilde L\widetilde a)^b=K^b{}_\nu(L_Aa)^\nu\circ f\); (E.25) makes \(G\) an adjoint scalar and \(D^\nu G\) a vector, proving the same vector transformation for \(P\). Thus lowering the output in the symbol calculation means applying the original metric tensor, not changing the operator's domain.

The infinitesimal gauge equation is also exact:


\[
 G_A(a-D_A\chi)=G_A(a)-\Delta_A\chi,
 \qquad
 P_A(-D_A\chi)^\nu=[\chi,\mathcal E^\nu(A)]-D^\nu\Delta_A\chi.
 \tag{E.19}
\]


The first equation proves which scalar equation is associated to choosing this gauge, and shows that residual transformations obey \(\Delta_A\chi=0\). It does not assert that an arbitrary global gauge problem with unspecified boundary conditions has a solution. The second follows by (E.8) and (E.17). Similarly (E.14) gives


\[
 \frac1wD_\nu\bigl(w(P_Aa)^\nu\bigr)
       =\Delta_AG_A(a)-[a_\nu,\mathcal E^\nu(A)].
 \tag{E.20}
\]


In particular at a background solution, \(P_Aa=0\) implies the scalar equation \(\Delta_AG_A(a)=0\). Additional data conditions are needed to deduce \(G_A(a)=0\); no such deduction is made without them.

The coefficient of the gauge term agrees exactly with the original action. For compactly supported variations, F7.15 gives

\[
 D^2S_A(a,a)=-\frac{2\sigma\hbar}{g_{\mathrm{YM}}^2}
       \int w\,\kappa(a_\nu,(L_Aa)^\nu)\,d^4x.
 \tag{E.21}
\]

Here \(\sigma=+1\) in Euclidean signature and \(-1\) in Lorentzian signature. This follows by differentiating F7.15 at a fixed test one-form; it does not require \(\mathcal E(A)=0\). Metric factors stay fixed. Trace invariance and integration by parts give
\(\int w\kappa(a_\nu,D^\nu G_A(a))=-\int w\kappa(G_A(a),G_A(a))\). Hence adding

\[
 S_{\rm gf}[a]=\frac{\sigma\hbar}{g_{\mathrm{YM}}^2}
                   \int w\kappa(G_A(a),G_A(a))\,d^4x
 \tag{E.22}
\]

to the action as a quadratic function of the perturbation contributes twice its coefficient to the second variation and changes (E.21) to the same expression with \(P_A\). In Euclidean signature this added quadratic term is nonnegative. It does not erase the background-curvature contribution to the original Hessian.

## 5. Intrinsic form and the retained Ricci and curvature terms

An equivalent formula identifies the usual notation \(D^\mu F_{\mu\nu}\) precisely. Define the Levi-Civita coefficients

\[
 C^\lambda_{\mu\nu}=\tfrac12g^{\lambda\tau}
    (\partial_\mu g_{\tau\nu}+\partial_\nu g_{\tau\mu}
                                      -\partial_\tau g_{\mu\nu}).
 \tag{E.23}
\]

They are symmetric in \(\mu,\nu\), and substitution verifies
\(\partial_\lambda g_{\mu\nu}=C^\rho_{\lambda\mu}g_{\rho\nu}+C^\rho_{\lambda\nu}g_{\mu\rho}\). Define the combined covariant derivative on a one-form by

\[
 \nabla^A_\mu a_\nu=\partial_\mu a_\nu+[A_\mu,a_\nu]-C^\lambda_{\mu\nu}a_\lambda.
 \tag{E.24}
\]

On each additional covariant index subtract its corresponding \(C\) term, and on each contravariant index add it. The symmetry of \(C\) makes the antisymmetric derivative in (E.24) exactly \(B\) of (E.3).

Differentiating the determinant by its cofactor formula gives \(\partial_\mu\log w=\tfrac12g^{\rho\sigma}\partial_\mu g_{\rho\sigma}=C^\lambda_{\lambda\mu}\). Since \(C^\nu_{\mu\lambda}F^{\mu\lambda}=0\) by symmetry, the coordinate formula for \(\nabla^A_\mu F^{\mu\nu}\) is \(w^{-1}D_\mu(wF^{\mu\nu})\). Metric compatibility therefore proves

\[
 g_{\nu\lambda}\mathcal E^\lambda(A)=(\nabla^A)^\mu F_{\mu\nu},
 \qquad G_A(a)=(\nabla^A)^\mu a_\mu.
 \tag{E.25}
\]


Fix the curvature convention

\[
 R^\rho{}_{\sigma\mu\nu}
 =\partial_\mu C^\rho_{\nu\sigma}-\partial_\nu C^\rho_{\mu\sigma}
     +C^\rho_{\mu\lambda}C^\lambda_{\nu\sigma}
     -C^\rho_{\nu\lambda}C^\lambda_{\mu\sigma},\qquad
 \operatorname{Ric}_{\sigma\nu}=R^\lambda{}_{\sigma\lambda\nu}.
 \tag{E.26}
\]


Expansion of two derivatives (E.24) gives

\[
 [\nabla^A_\lambda,\nabla^A_\nu]a_\mu
       =[F_{\lambda\nu},a_\mu]-R^\sigma{}_{\mu\lambda\nu}a_\sigma.
 \tag{E.27}
\]

All second partial derivatives of \(a\) cancel; the gauge terms combine as in (E.9); the remaining four coefficient terms are precisely (E.26) with its minus sign on a covariant index. Contracting \(\lambda,\mu\), and using metric compatibility and antisymmetry of the first two indices of the lowered Riemann tensor, gives

\[
 (\nabla^A)^\mu\nabla^A_\nu a_\mu
 =\nabla^A_\nu(\nabla^A)^\mu a_\mu
        +[F_{\mu\nu},a^\mu]+\operatorname{Ric}_{\nu}{}^\sigma a_\sigma.
 \tag{E.28}
\]

For the sign, \(g^{\mu\lambda}R^\sigma{}_{\mu\lambda\nu}=-\operatorname{Ric}^{\sigma}{}_{\nu}\). The Riemann antisymmetry used here follows by applying \([\nabla_\lambda,\nabla_\nu]\) to the metric-compatibility identity \(\nabla g=0\): its action on the two covariant indices gives \(R_{\alpha\beta\lambda\nu}+R_{\beta\alpha\lambda\nu}=0\). The symmetry of Ricci for (E.23) follows by substituting (E.26): the derivative difference is the derivative of \(C^\lambda_{\lambda\sigma}=\partial_\sigma\log w\), and the remaining contracted products are symmetric after renaming indices. Thus its two placements in (E.28) agree.

Substituting (E.28) into (E.4), and retaining its additional \([a^\mu,F_{\mu\nu}]\) term, gives


\[
 \begin{aligned}
 (L_Aa)_\nu={}&(\nabla^A)^\mu\nabla^A_\mu a_\nu
      -\nabla^A_\nu G_A(a)-\operatorname{Ric}_{\nu}{}^\sigma a_\sigma
      -2[F_{\mu\nu},a^\mu],\\
 (P_Aa)_\nu={}&(\nabla^A)^\mu\nabla^A_\mu a_\nu
      -\operatorname{Ric}_{\nu}{}^\sigma a_\sigma
      -2[F_{\mu\nu},a^\mu].
 \end{aligned}\tag{E.29}
\]


The second covariant derivative includes the connection on its derivative index. Explicitly it is


\[
g^{\lambda\mu}\{\partial_\lambda(\nabla^A_\mu a_\nu)+[A_\lambda,\nabla^A_\mu a_\nu]-C^s_{\lambda\mu}\nabla^A_s a_\nu-C^s_{\lambda\nu}\nabla^A_\mu a_s\}
\]

, with (E.24) substituted for each first derivative. Consequently (E.29) retains all terms in (E.6) and (E.18), including metric derivatives; it is not a replacement by an ordinary scalar Laplacian. In particular the curvature term has its full factor two and its displayed sign.

## 6. Ellipticity and the Lorentzian characteristic covectors

The cancellation in (E.17) now gives


\[
 \boxed{\sigma_2(P_A)(\xi)a=-q_g(\xi)a,\qquad
         \sigma_2(\Delta_A)(\xi)\chi=-q_g(\xi)\chi.}
 \tag{E.30}
\]


An order-two square operator is called elliptic here when this symbol is invertible for every nonzero real covector. For positive \(g\), also \(g^{-1}\) is positive, so \(q_g(\xi)>0\) for every \(\xi\ne0\). The inverse of the symbol is exactly \(-q_g(\xi)^{-1}\) times the identity, proving ellipticity of both operators. With the positive one-form metric and \(\kappa\), the symbol of \(-P_A\) has pairing \(q_g(\xi)|a|^2\); on any compact coordinate region where the metric is positive definite this also supplies a positive uniform lower bound in fixed coordinate norms, since the smallest metric eigenvalue has a positive minimum. This pointwise and compact-region assertion does not imply positivity of the complete operator with its zero-order terms or solve an arbitrary boundary problem.

For Lorentzian \(g\), the exact characteristic covectors of \(P_A\) and \(\Delta_A\) are the nonzero real \(\xi\) with \(q_g(\xi)=0\), since the symbol is a scalar multiple of the identity. In the course's physical coordinates \((t,x^1,x^2,x^3)\), retain


\[
 g=\operatorname{diag}(-c^2,1,1,1),\quad
 g^{-1}=\operatorname{diag}(-c^{-2},1,1,1),\quad w=c>0,
 \quad q_g(\xi)=-\xi_t^2/c^2+\sum_{j=1}^3\xi_j^2.
 \tag{E.31}
\]


At the zero background this gives
\( (P_0a)_\nu=(-c^{-2}\partial_t^2+\sum_j\partial_j^2)a_\nu\).
For the phase \(k_jx^j-\omega t\), its covector is \((-\omega,k_1,k_2,k_3)\) and its characteristic equation is


\[
 \omega^2=c^2\sum_jk_j^2.
 \tag{E.32}
\]


The wave numbers have units length\(^{-1}\), \(\omega\) has units time\(^{-1}\), and \(c\) has units length/time, so all terms in (E.31) have units length\(^{-2}\). Also \(a_t\) has units time\(^{-1}\) and \(a_j\) length\(^{-1}\); their divergence terms \(-c^{-2}\partial_ta_t\) and \(\partial_ja_j\) both have units length\(^{-2}\). The exact real change of coordinate \(x^0=ct\) makes the Lorentzian metric \(-(dx^0)^2+\sum_j(dx^j)^2\), with \(a_t=c a_0\) and \(F_{tj}=cF_{0j}\). It preserves Lorentzian signature and is distinct from changing the metric to a positive one. No complex time substitution has been used.

## 7. An exact commuting field on two explicitly defined domains

Fix lengths \(H,L_1,L_2,L_3>0\), a positive speed \(c\), and an integer \(n\geq1\). Let \(\mathbb T^3\) have coordinates \(x^j\) modulo \(L_j\), and write \(V=L_1L_2L_3\), \(k=2\pi n/L_1>0\), \(\omega=ck\). The following are new domains used for an elementary example, not substitutions for the instanton's \(\mathbb R^4\):

- \(M_E=[0,H]\times\mathbb T^3\), with length coordinate \(s\) and metric \(ds^2+\sum_j(dx^j)^2\).
- \(M_L=\mathbb R_t\times\mathbb T^3\), with physical time \(t\) and metric \(-c^2dt^2+\sum_j(dx^j)^2\).

Use the trivial \(SU(2)\) bundle and the fixed matrix
\(T=T_3=\operatorname{diag}(-i/2,i/2)\), so \(\kappa(T,T)=1/2\). Define the actual connection by


\[
 A_E=T f_E(s)\cos(kx^1)\,dx^2,\qquad
 A_L=T f_L(t)\cos(kx^1)\,dx^2.
 \tag{E.33}
\]


The amplitudes \(f\) have units length\(^{-1}\). In F7.20's component parameterization this means \(A_2^3=f\cos(kx^1)/g_{\mathrm{YM}}\); the matrices in (E.33) remain the original connection, not those component variables. Every matrix coefficient is a real multiple of \(T\), so all nonlinear commutators vanish exactly. Both divergences \(G_0(A)\) vanish, because only the 2-component is present and it is independent of \(x^2\). The only independent curvature components are


\[
 \begin{array}{lll}
 (F_E)_{s2}=T f_E'(s)\cos(kx^1),&&
 (F_E)_{12}=-Tk f_E(s)\sin(kx^1),\\
 (F_L)_{t2}=T f_L'(t)\cos(kx^1),&&
 (F_L)_{12}=-Tk f_L(t)\sin(kx^1).
 \end{array}\tag{E.34}
\]


Their reverse components are their negatives and all other components vanish. For \(\nu\ne2\), (E.2) is zero because the only possible derivative is \(\partial_2\). For \(\nu=2\), its Euclidean value is \(T(f_E''-k^2f_E)\cos(kx^1)\), while its Lorentzian value is \(T(-c^{-2}f_L''-k^2f_L)\cos(kx^1)\). Therefore these are exact solutions of the full nonlinear equations precisely when


\[
 f_E''-k^2f_E=0,\qquad f_L''+c^2k^2f_L=0,
 \tag{E.35}
\]


respectively. Their divergence gauge, curvature Bianchi identity, and Gauss equation have all been checked, rather than inferred from only the 2-component.

For Euclidean boundary values \(f_E(0)=U_0\) and \(f_E(H)=U_H\), where both specified real amplitudes have units length\(^{-1}\), the unique solution is


\[
 f_E(s)=U_0\frac{\sinh(k(H-s))}{\sinh(kH)}
                +U_H\frac{\sinh(ks)}{\sinh(kH)}.
 \tag{E.36}
\]


Both terms solve the first equation in (E.35), the denominator is positive, and direct endpoint evaluation gives the prescribed data. For uniqueness, a difference \(v\) with zero endpoints obeys \(v''-k^2v=0\); multiply by \(v\), integrate, and integrate by parts to get \(-\int_0^H[(v')^2+k^2v^2]\,ds=0\). Thus \(v=0\). The nonnegative weights in (E.36) have sum at most one: their sum equals \(\cosh(k(s-H/2))/\cosh(kH/2)\), at most one on \([0,H]\). Consequently \(|f_E(s)|\leq\max(|U_0|,|U_H|)\) throughout the slab. This is a direct bounded boundary-value calculation.

It does not make the same Euclidean equation a stable forward evolution problem. Fix a nonzero amplitude \(U\) with units length\(^{-1}\) and, on the same fixed cylinder, set \(k_m=2\pi m/L_1\) and


\[
 u_m(s,x^1)=Ue^{-k_mH/2}\sinh(k_ms)\cos(k_mx^1),\quad m=1,2,\ldots.
 \tag{E.37}
\]


Each \(T u_m dx^2\) is an exact solution. Its initial value is zero. For every fixed nonnegative integer \(p\), its initial derivative satisfies


\[
 \|\partial_1^p\partial_su_m(0,\cdot)\|_\infty
       =|U|k_m^{p+1}e^{-k_mH/2}\longrightarrow0,
 \qquad
 \|u_m(H,\cdot)\|_\infty
       =\frac{|U|}{2}(e^{k_mH/2}-e^{-3k_mH/2})\longrightarrow\infty.
 \tag{E.38}
\]


Derivatives in the other spatial coordinates vanish. The first convergence follows because an exponential dominates each fixed polynomial; for example the exponential power series bounds \(e^{k_mH/4}\) below by any chosen power for large \(m\). Thus the Cauchy data converge to zero in every fixed spatial derivative norm while the later values diverge. This proves the failure of continuous forward Cauchy dependence for this explicit class and these stated norms. It does not claim that every Euclidean Cauchy datum has a solution.

For Lorentzian initial data \(f_L(0)=U_0\) and \(f_L'(0)=V_0\), with \(V_0\) of units length\(^{-1}\)time\(^{-1}\), the unique solution for every real \(t\) is


\[
 f_L(t)=U_0\cos(\omega t)+\frac{V_0}{\omega}\sin(\omega t),
 \qquad \omega=\frac{2\pi nc}{L_1}.
 \tag{E.39}
\]


Differentiation verifies the equation and both initial data. For uniqueness, the difference satisfies \((v'^2+\omega^2v^2)'=2v'(v''+\omega^2v)=0\); zero initial value and derivative give zero energy and hence \(v=0\). The exact conserved quantity also gives \(|f_L(t)|\leq\sqrt{U_0^2+(V_0/\omega)^2}\). No exponentially increasing dependence on time occurs for this mode.

## 8. The full action and energy in the example

The ordered curvature contraction in the Euclidean example is
\(2\kappa(T,T)[(f_E')^2\cos^2(kx^1)+k^2f_E^2\sin^2(kx^1)]\). Both spatial trigonometric squares have integral \(V/2\), since \(n\geq1\). Inserting \(\kappa(T,T)=1/2\) and the original F7.5 coefficient gives


\[
 S_E[A_E]=\frac{\hbar V}{4g_{\mathrm{YM}}^2}
                  \int_0^H[(f_E')^2+k^2f_E^2]\,ds.
 \tag{E.40}
\]


For the solution (E.36), \((f_E f_E')'=(f_E')^2+k^2f_E^2\), so its exact boundary action is


\[
 S_E[A_E]=\frac{\hbar V k}{4g_{\mathrm{YM}}^2\sinh(kH)}
       [(U_0^2+U_H^2)\cosh(kH)-2U_0U_H].
 \tag{E.41}
\]


If one perturbs \(f_E\) by a smooth real \(v\) vanishing at both endpoints, the cross integral \(\int(f_E'v'+k^2f_Ev)\) vanishes by integration by parts and (E.35). Thus the action increases by exactly \(\hbar V/(4g_{\mathrm{YM}}^2)\int[(v')^2+k^2v^2]\), positive unless \(v=0\). This proves minimization in this specified family.

On any finite time interval \([t_0,t_1]\), the Lorentzian determinant is \(w=c\), the temporal inverse metric is \(-c^{-2}\), and \(\sigma=-1\). Substitution in the same original action gives


\[
 S_L[A_L]=\frac{\hbar V}{4g_{\mathrm{YM}}^2}
       \int_{t_0}^{t_1}[c^{-1}(f_L')^2-ck^2f_L^2]\,dt.
 \tag{E.42}
\]


The Legendre momentum of this one-mode Lagrangian is
\(p=\hbar V f_L'/(2g_{\mathrm{YM}}^2c)\). Its energy is therefore


\[
 \mathcal H_L=p f_L'-\mathcal L_L
     =\frac{\hbar V}{4g_{\mathrm{YM}}^2}
                [c^{-1}(f_L')^2+ck^2f_L^2]
     =\frac{\hbar V}{4g_{\mathrm{YM}}^2}
                [c^{-1}V_0^2+ck^2U_0^2].
 \tag{E.43}
\]


Its time derivative vanishes by (E.35). It has units action/time; (E.40) has units action. These quantities follow from the exact trace and full ordered sums, not from a scalar action whose coefficient was chosen separately. The bounded Euclidean boundary solution, its unstable Cauchy sequence, and the Lorentzian conserved-energy evolution provide an explicit analytical distinction linked by the common connection ansatz and the exact change in the stated metric. They establish no identification of Euclidean and Lorentzian quantum theories.

## 9. Exact prerequisites and source

The action, metric, trace pairing, curvature variation and field equation are
those proved in [Lesson 7](../action-and-field-equations.html), equations
F7.1–F7.5, F7.10, F7.14–F7.19 and F7.24–F7.31. The present chapter supplies
the complete operator and example calculations. F7.62 provides the action
comparison with David Tong's [TASI Lectures on Solitons, version 5](https://arxiv.org/abs/hep-th/0509216v5);
no additional analytical theorem from that source is assumed here.

## 10. Exercises with complete solutions

### Exercise 1. A gauge direction at a background that is not a solution

Use the original gauge rule and derive the infinitesimal one-form
produced by \(u_\varepsilon=\exp(\varepsilon\chi)\).
Determine its exact image under \(L_A\). Under what condition is
it necessarily in the kernel?

**Solution.** Differentiating the two products in
\(u_\varepsilon A u_\varepsilon^{-1}-(du_\varepsilon)u_\varepsilon^{-1}\)
at zero gives \(\chi A-A\chi-d\chi=-D_A\chi\).
Curvature and field-equation covariance give
\(\mathcal E(A^{u_\varepsilon})=u_\varepsilon\mathcal E(A)u_\varepsilon^{-1}\).
The chain rule on the left and product rule on the right yield
\(L_A(-D_A\chi)=[\chi,\mathcal E(A)]\).
At a solution the right side vanishes for every \(\chi\).
For a specific \(\chi\) at another background it vanishes exactly
when that \(\chi\) commutes with every component of \(\mathcal E(A)\).
There is no additional zero term available to discard.

### Exercise 2. Null covectors and the quotient of the symbol kernel

Let \(d=\dim_{\mathbb R}\mathfrak g\). At a nonzero Lorentzian null
covector \(\xi\), calculate the kernel and image dimensions of
the ungauged symbol and the dimension remaining in the kernel
after quotienting by its gauge directions.

**Solution.** Because \(q_g(\xi)=0\), (E.15) is the map
\(a\mapsto \xi(\xi^\sigma a_\sigma)\). Nondegeneracy of \(g\)
makes the scalar contraction a nonzero linear functional.
For each of the \(d\) matrix directions it maps four coefficients
onto one coefficient, giving kernel dimension \(3d\), image
dimension \(d\). The gauge vectors \(\xi\chi\) form a
\(d\)-dimensional subspace of the kernel since their contraction
is \(q_g(\xi)\chi=0\). The quotient consequently has dimension
\(3d-d=2d\). This is a quotient of finite-dimensional symbol spaces
at the specified covector; no quantum state count is needed.

### Exercise 3. The zero spatial mode, with its full action factor

The examples in Sections 7–8 assume \(n\ge1\). Extend the connection
ansatz to \(n=0\) on the same torus. Derive the two-boundary
Euclidean solution, the Lorentzian initial-value solution,
the Euclidean action and the conserved Lorentzian energy.

**Solution.** Now \(k=0\), \(\cos(kx^1)=1\), and the magnetic
curvature vanishes. The equations for the only connection
coefficient are \(f_E''=0\) and \(f_L''=0\), with solutions


\[
 f_E(s)=U_0+\frac{U_H-U_0}{H}s,\qquad
 f_L(t)=U_0+V_0t.
 \tag{E.44}
\]


Their uniqueness follows by integrating the zero second
derivative twice and using the two specified data.
All reverse and zero curvature components remain as in (E.34).
The spatial integral of the constant square is now \(V\),
whereas it was \(V/2\) for a nonzero Fourier mode.
Using the original full ordered contraction gives


\[
 \begin{aligned}
 S_E[A_E]&=\frac{\hbar V}{2g_{\mathrm{YM}}^2}
                 \int_0^H(f_E')^2\,ds
       =\frac{\hbar V}{2g_{\mathrm{YM}}^2H}(U_H-U_0)^2,\\
 S_L[A_L]&=\frac{\hbar V}{2g_{\mathrm{YM}}^2c}
                 \int_{t_0}^{t_1}(f_L')^2\,dt,\\
 p&=\frac{\hbar V}{g_{\mathrm{YM}}^2c}f_L',\qquad
 \mathcal H_L=\frac{\hbar V}{2g_{\mathrm{YM}}^2c}V_0^2.
 \end{aligned}
 \tag{E.45}
\]


The derivative of the last expression is zero. Linear growth
of \(f_L\) is possible while this energy stays constant,
because the zero mode has no positive \(k^2f_L^2\) contribution.
Taking \(k\to0\) in the nonzero-mode action prefactor would miss
the change in the spatial integral. The zero mode must be
calculated in its actual torus function space.

### Exercise 4. The action cost of changing the boundary solution

For \(n\ge1\), let \(f_E\) be (E.36), and let \(v\) be any smooth
real function with \(v(0)=v(H)=0\). Calculate the entire
difference of the actions of the two connections with
coefficients \(f_E+v\) and \(f_E\).

**Solution.** Expand both squares in (E.40), retaining the
cross contribution. Its integral is


\[
 2\int_0^H(f_E'v'+k^2f_Ev)\,ds
 =2[f_E'v]_0^H-2\int_0^H(f_E''-k^2f_E)v\,ds=0.
 \tag{E.46}
\]


The first term vanishes by the actual endpoint conditions,
and the second by the actual field equation. Therefore


\[
 S_E[f_E+v]-S_E[f_E]
   =\frac{\hbar V}{4g_{\mathrm{YM}}^2}
             \int_0^H\bigl((v')^2+k^2v^2\bigr)\,ds.
 \tag{E.47}
\]


This is positive for every nonzero \(v\); if its integral
vanishes, the nonnegative integrand vanishes everywhere
by continuity and \(k>0\) forces \(v=0\).
The result proves the minimum in the stated commuting
one-mode family with fixed endpoints. It makes no assertion
about a different gauge orbit, domain or boundary condition.

Return to [Euclidean Yang–Mills and instantons](../euclidean-yang-mills-instantons.html).

Mathematical text and complete solutions: CC0 1.0.
