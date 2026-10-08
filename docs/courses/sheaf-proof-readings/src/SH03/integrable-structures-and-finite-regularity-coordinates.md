# Integrable structures and finite-regularity coordinates

This reading constructs compatible complex coordinates for an integrable almost-complex structure of finite regularity. Two polynomial coordinate changes, a weighted solution of the Cauchy–Riemann equations and finite elliptic regularity give the coordinate theorem. The final section retains the holomorphic parameters in a Picard-zero deformation of the Fermat quartic. The construction uses no deformation-existence theorem and assumes no smooth bootstrap of the original almost-complex structure.

*Original programme exposition by GPT-6 Astra (OpenAI), Ultra, October 2026. This independently expressed exposition is dedicated under CC0-1.0. Human sources retain their own terms.*

## 1. Statement and regularity budget

Let \(M\) be a smooth real manifold of dimension \(d=2n\), and let \(J\in C^{5,1/2}(\operatorname{End}TM)\) satisfy \(J^2=-1\). Suppose that sections of \(T^{0,1}_J M\) are closed under the Lie bracket. Each point has a neighbourhood with a \(C^{2,1/4}\) diffeomorphism to an open set of \(\mathbb C^n\) whose differential intertwines \(J\) and multiplication by \(i\). The changes between these coordinates are holomorphic.

When \(n=0\) the assertion is immediate on the discrete zero-dimensional manifold. Henceforth assume \(n\geq1\).

Here and below a smaller Hölder exponent is harmless. The conclusion asserted is deliberately weaker than optimal finite-regularity Newlander–Nirenberg estimates. It is enough for the real dimension 44 used by the family construction.

More generally, if \(h=(h_1,\ldots,h_b):M\to\mathbb C^b\) is \(C^{2,1/4}\), annihilated by \(T^{0,1}_J\), and has real rank \(2b\), then the coordinates can be chosen as \((w_1,\ldots,w_{n-b},h_1,\ldots,h_b)\).

The proof uses only two spatial Taylor cancellations. The local Kähler metric constructed below has class \(C^{4,1/2}\), its connection has class at least \(C^{3,1/2}\), and its curvature has class at least \(C^{2,1/2}\). The final scalar elliptic argument uses coefficients of class \(C^{2,1/2}\), an \(L^2\) distributional solution and a finite sequence of \(L^p\) improvements. There is no Sobolev embedding from a fixed small \(H^s\) into \(C^1\) in real dimension 44.

## 2. Two polynomial changes of coordinates

Fix a point, written as \(0\), and make a complex-linear choice of its real tangent coordinates. In a sufficiently small coordinate ball the distribution has a frame

\[
 L_{\bar j}=\partial_{\bar z_j}+\sum_a A_{\bar j}^{a}(z)\partial_{z_a},
 \qquad A(0)=0.                                      \tag{N1}
\]

The frame coefficients are \(C^{5,1/2}\). A bracket of two members of (N1) has no \(\partial_{\bar z}\) coefficient. Involutivity therefore makes that bracket zero, rather than just another linear combination of the frame. Its \(\partial_{z_a}\) coefficient is

\[
 \partial_{\bar z_j}A_{\bar k}^{a}-\partial_{\bar z_k}A_{\bar j}^{a}
 +A_{\bar j}^{b}\partial_{z_b}A_{\bar k}^{a}
 -A_{\bar k}^{b}\partial_{z_b}A_{\bar j}^{a}=0.          \tag{N2}
\]

Suppose \(A=O(|z|^s)\), where \(s=1\) or \(2\), and let \(P\) be its homogeneous Taylor term of degree \(s\). In (N2) the nonlinear terms have order at least \(2s-1\). The terms of degree \(s-1\) consequently give

\[
 \partial_{\bar z_j}P_{\bar k}^{a}
 =\partial_{\bar z_k}P_{\bar j}^{a}.                  \tag{N3}
\]

Regard \(z\) and \(\bar z\) temporarily as independent polynomial variables and define

\[
 Q^a(z,\bar z)=\int_0^1\sum_k\bar z_k P_{\bar k}^{a}(z,t\bar z)\,dt.
                                                               \tag{N4}
\]

Differentiation with respect to \(\bar z_j\), followed by (N3), makes the integrand
\(\frac{d}{dt}[tP_{\bar j}^{a}(z,t\bar z)]\). Hence \(\partial_{\bar z_j}Q^a=P_{\bar j}^{a}\). The real polynomial coordinate change \(z\mapsto z-Q(z,\bar z)\) has derivative the identity at zero and kills this leading coefficient in (N1). Indeed
\(L_{\bar j}(z_a-Q^a)=A_{\bar j}^a-P_{\bar j}^a-A_{\bar j}^b\partial_bQ^a\), whose last term has order \(2s\geq s+1\). Changing the normalized frame does not change this order. Apply this operation first for \(s=1\) and then for \(s=2\). In the resulting coordinates,

\[
 A=O(r^3),\quad DA=O(r^2),\quad D^2A=O(r),
 \qquad r=|z|.                                      \tag{N5}
\]

The derivative bounds are Taylor bounds, not conclusions inferred from an order bound on the function alone. Only the two indicated finite jets were used.

## 3. Differential identities before holomorphic coordinates exist

Involutivity of \(T^{0,1}\), and its conjugate, imply that \(d\) on complex forms has only its type \((1,0)\) and \((0,1)\) parts. Write them as \(\partial\) and \(\bar\partial\). Splitting \(d^2=0\) by type gives

\[
 \partial^2=\bar\partial^2=0,\qquad
 \partial\bar\partial+\bar\partial\partial=0.          \tag{N6}
\]

These identities can first be checked on functions and a local frame by the bracket formula, then on exterior products by the derivation rule. Their distributional extension follows from the same coefficient identities and testing against compactly supported forms. The available regularity is more than sufficient for these second-order identities.

Put \(\psi=|z|^2\) and \(\omega=i\partial\bar\partial\psi\). Equations (N5) give

\[
 \omega=\omega_0+O(r^3),\quad D\omega=D\omega_0+O(r^2),
 \qquad |\partial\psi|_\omega^2=\psi+O(r^5),           \tag{N7}
\]

where \(\omega_0=i\sum dz_j\wedge d\bar z_j\), using its usual Hermitian norm convention. The first error includes the term \(r\,DJ\), which is also \(O(r^3)\). Shrinking the ball makes \(\omega\) positive. It is real and closed by (N6), and has class \(C^{4,1/2}\).

The Kähler connection and its identities can be established here without presupposing the coordinates being constructed. For the real metric \(g\) of \(\omega\), let \(\nabla\) be its Levi-Civita connection and set
\(F(X,Y,Z)=g((\nabla_XJ)Y,Z)\). Expanding the torsion-free bracket formula gives, with \(\omega(X,Y)=g(JX,Y)\),

\[
 2F(X,Y,Z)=d\omega(X,Y,Z)-d\omega(X,JY,JZ)
                      +g(N_J(Y,Z),JX).                \tag{N8}
\]

For example, the two algebraic rules used in the expansion are
\(F(X,Y,Z)=-F(X,Z,Y)\) and
\(F(X,JY,Z)=F(X,Y,JZ)\). Both follow by differentiating \(J^2=-1\) and the metric compatibility of \(J\). Involutivity makes \(N_J=0\), so (N8) gives \(\nabla J=0\).

Let \(E\) be a Hermitian line with an integrable \((0,1)\) connection, and let \(D=D'+D^{\prime\prime}\) be its metric connection. In a unitary frame parallel to first order at a point, exterior multiplication and contraction satisfy
\(\iota_j\epsilon_k+\epsilon_k\iota_j=\delta_{jk}\), with the corresponding barred identities. The type-preserving Levi-Civita connection has no torsion terms. With \(\Lambda\) the adjoint of exterior multiplication by \(\omega\), direct substitution gives

\[
 [\Lambda,D']=i(D^{\prime\prime})^*,\qquad
 [\Lambda,D^{\prime\prime}]=-i(D')^*.
\]

Apply the graded product rule to these two identities and use
\(D'D^{\prime\prime}+D^{\prime\prime}D'=\Theta(E)\). The resulting identity is

\[
 \Delta^{\prime\prime}=\Delta'+[i\Theta(E),\Lambda].                \tag{N9}
\]

Thus for compactly supported \(E\)-valued \((n,1)\)-forms \(v\),

\[
 \|D^{\prime\prime}v\|^2+\|(D^{\prime\prime})^*v\|^2
 \geq ([i\Theta(E),\Lambda]v,v).                      \tag{N10}
\]

All these are first-order operator and integration-by-parts calculations with a twice differentiable metric and connection; they do not require a holomorphic frame. On \((n,1)\)-forms a positive curvature matrix \(C=(C_{j\bar k})\), expressed in a unitary coframe, acts in (N10) by that same positive matrix on the single antiholomorphic index. This also checks the sign in (N9).

## 4. A weighted scalar solution, with its domains specified

Take \(\Omega=\{\psi<R^2\}\) inside the preceding ball. It has a complete Kähler metric \(\gamma\): for instance, add a positive multiple of
\(i\partial\bar\partial[-\log(R^2-\psi)]\) to \(\omega\). Positivity follows from the chain rule. Its term
\((R^2-\psi)^{-2}i\partial\psi\wedge\bar\partial\psi\)
shows that a curve approaching the boundary has infinite length. The exhaustion \(-\log(R^2-\psi)\) has bounded gradient in this metric. Cutoffs obtained by composing it with a fixed cutoff at scales \(k\) are compactly supported, tend to one, and have gradient \(O(k^{-1})\) in \(\gamma\).

Use the canonical line \(K=\Lambda^{n,0}T^*\Omega\), with its metric from \(\omega\), and \(E=K^{-1}\). Its \((0,1)\) connection is dual to that induced by (N6); it is integrable. The metric connection exists algebraically: in any nonvanishing frame its \((0,1)\) connection coefficient is prescribed, and metric compatibility uniquely determines its \((1,0)\) coefficient. Its curvature has type \((1,1)\), since the \((0,2)\) curvature vanishes and the connection is unitary. Write \(\operatorname{Ric}(\omega)=i\Theta(E)\). It is bounded on the closed smaller coordinate ball; this definition does not use the unavailable holomorphic determinant formula.

Let \(\Phi\) be a real \(C^2\) weight such that

\[
 C:=\operatorname{Ric}(\omega)+i\partial\bar\partial\Phi\geq\omega.
                                                               \tag{N11}
\]

Twist the metric on \(E\) by \(e^{-\Phi}\). Identify scalar \((0,q)\)-forms with \(E\)-valued \((n,q)\)-forms by the canonical identity tensor of \(K\otimes K^{-1}\). This identification commutes with \(\bar\partial\): the derivative of a local frame of \(K\) cancels the derivative of its dual. Norms and adjoints on the complete manifold use \(\gamma\), while the line metric still comes from \(\omega\).

On these weighted Hilbert spaces let

\[
 T=D^{\prime\prime}:H_0\supset\operatorname{Dom}T\to H_1,
 \qquad S=D^{\prime\prime}:H_1\supset\operatorname{Dom}S\to H_2
\]

be the maximal distributional realizations. They are closed and densely defined; \(ST=0\) on the appropriate domain. The compactly supported estimate (N10) extends to
\(v\in\operatorname{Dom}T^*\cap\operatorname{Dom}S\).
Here is the required density justification. First multiply by the complete-metric cutoffs; the commutators with a first-order operator are exterior multiplication or contraction by the cutoff derivative, so their norms tend to zero. On each resulting compact set use convolution in coordinate frames. For a term \(a(x)\partial_k\), its convolution commutator is an integral of the difference quotient of \(a\), together with the term obtained by differentiating \(a\). Its operator norm on \(L^2\) is bounded by a constant times the local Lipschitz norm of \(a\). For a smooth input it tends to zero; density and that uniform bound give convergence for every \(L^2\) input. Apply this simultaneously to \(T^*\) and \(S\), using a finite partition of unity. Zeroth-order terms converge by ordinary local convolution. This proves density in their joint graph norm. In particular,

\[
 (A_\gamma v,v)\leq\|T^*v\|^2+\|Sv\|^2,
 \qquad A_\gamma=[C,\Lambda_\gamma].                  \tag{N12}
\]

If \(g\in H_1\), \(Sg=0\), and
\(M=(A_\gamma^{-1}g,g)<\infty\), the pointwise Cauchy–Schwarz inequality followed by (N12) bounds
\(|(g,v)|^2\) by \(M(\|T^*v\|^2+\|Sv\|^2)\).
To remove the \(Sv\) term, project \(v\in\operatorname{Dom}T^*\) orthogonally onto \(\ker S\), writing \(v=v_0+v_1\). Since \(\operatorname{ran}T\subset\ker S\), every \(v_1\perp\ker S\) belongs to \(\operatorname{Dom}T^*\) and \(T^*v_1=0\). Hence \(v_0\in\operatorname{Dom}T^*\cap\ker S\). Also \((g,v)=(g,v_0)\). We obtain

\[
 |(g,v)|\leq M^{1/2}\|T^*v\|.
\]

Define the resulting bounded functional on \(\operatorname{ran}T^*\), extend it to \(H_0\), and represent it by \(u\in H_0\). Then \((u,T^*v)=(g,v)\) for all such \(v\), which is exactly \(u\in\operatorname{Dom}T\), \(Tu=g\), and \(\|u\|^2\leq M\). This uses Hilbert projection, Hahn–Banach and Riesz representation; no closed-range premise was inserted.

A pointwise matrix cancellation makes this estimate usable in the original metric. In a fixed \((1,0)\) coframe let \(G,H\) be the positive matrices of \(\omega,\gamma\). The line metric of \(K^{-1}\) is \(\det G\). For an \(E\)-valued \((n,0)\)-form, its \(\gamma\)-norm supplies \((\det H)^{-1}\), which cancels the \(\gamma\)-volume. Thus its norm density is the scalar density \(|u|^2dV_\omega\). For an \((n,1)\)-form with coefficient vector \(g\), the inverse-curvature energy density is, in the same notation,

\[
 g^*C^{-1}g\,\det G\,dV_0\,e^{-\Phi}.
\]

The \(H^{-1}\) from the antiholomorphic index cancels the \(H\) in the inverse of \(A_\gamma\). In particular this density is independent of the auxiliary complete metric. As \(C\geq G\), it is at most \(|g|_\omega^2e^{-\Phi}dV_\omega\). We have proved the precise scalar assertion

\[
 \bar\partial g=0,\quad
 \int_\Omega|g|_\omega^2e^{-\Phi}dV_\omega<\infty
 \quad\Longrightarrow\quad
 \bar\partial u=g,\quad
 \int_\Omega|u|^2e^{-\Phi}dV_\omega
 \leq\int_\Omega|g|_\omega^2e^{-\Phi}dV_\omega,          \tag{N13}
\]

for the compactly supported \(g\) used below. Compact support ensures that it belongs to the complete-metric \(H_1\). This proof needs no passage between inequivalent global \(L^2\) norms.

## 5. The singular weight and its uniform curvature bound

Let \(0<\varepsilon\leq1\). The chain rule and (N7) give

\[
 i\partial\bar\partial\log(\psi+\varepsilon^2)
 =\frac{\omega}{\psi+\varepsilon^2}
   -\frac{i\partial\psi\wedge\bar\partial\psi}
               {(\psi+\varepsilon^2)^2}
 \geq -C_0r\,\omega.                                \tag{N14}
\]

Indeed the only possibly negative eigenvalue is bounded below by
\(\varepsilon^2/(r^2+\varepsilon^2)^2-Cr^5/(r^2+\varepsilon^2)^2\), and the last quotient is at most \(Cr\). This is uniform all the way to \(r=0\).

Choose \(B\) with \(\operatorname{Ric}(\omega)\geq-B\omega\), and then a fixed \(a\geq1+B+(n+1)C_0R\). The weights

\[
 \Phi_\varepsilon=a\psi+(n+1)\log(\psi+\varepsilon^2) \tag{N15}
\]

satisfy (N11). If \(\chi\in C_c^\infty(\Omega)\) equals one near zero, put
\(g_j=\bar\partial(\chi z_j)\). These are closed and compactly supported, and (N5) gives \(g_j=O(r^3)\) near zero. Their norms in (N13) are bounded independently of \(\varepsilon\). The radial bound at zero is explicitly

\[
 r^6\,r^{-2n-2}\,r^{2n-1}dr=r^3dr.                  \tag{N16}
\]

Apply (N13) and let \(\varepsilon\downarrow0\). The solutions are bounded in one fixed weighted \(L^2\) space, so a weakly convergent subsequence gives a distributional solution \(u_j\). For each fixed \(\varepsilon_0>0\), all later members have the uniform bound in the stronger norm with weight \(e^{-\Phi_{\varepsilon_0}}\). Weak lower semicontinuity in that space follows either by a second weak extraction or by its supremum-of-bounded-linear-functionals description. Its weak limit is the same distribution. Finally monotone convergence as \(\varepsilon_0\downarrow0\) gives

\[
 \bar\partial u_j=g_j,\qquad
 \int_\Omega |u_j|^2e^{-a\psi}r^{-2n-2}dV_\omega<\infty.
                                                               \tag{N17}
\]

## 6. Finite elliptic regularity in any dimension

We give the particular rough-coefficient estimate needed for (N17), including its initial distributional hypothesis.

**Elliptic lemma.** Let \(L\) be a scalar second-order elliptic differential operator on an open subset of \(\mathbb R^d\), with coefficients of class \(C^{2,1/2}\). If \(u\in L^2_{\rm loc}\), \(Lu=f\) distributionally, and \(f\in C^{2,1/2}_{\rm loc}\), then \(u\in C^{2,1/4}_{\rm loc}\).

Write \(H^{s,p}\) for the Bessel-potential spaces. On a small ball extend the coefficients, using a cutoff and a frozen elliptic principal part, to globally bounded coefficients of the same class, still elliptic. The closeness of the principal coefficients on the small ball makes this extension elliptic. Divide the frequency space into smooth shells \(|\xi|\asymp2^k\), and on the \(k\)-th shell smooth the coefficients in \(x\) at scale \(2^{-k/2}\). Taylor's remainder estimate of order \(5/2\) then decomposes the symbol as

\[
 L=L^\#+L^b,\qquad
 L^\#\in S^2_{1,1/2},\qquad
 L^b\in C^{5/2}S^{3/4}_{1,1/2}.                       \tag{N18}
\]

For clarity, a symbol in \(C^rS^m_{1,\delta}\) has ordinary symbol bounds of order \(m\), and its \(C^r\) seminorm after \(\xi\)-differentiation of order \(\alpha\) is bounded by a constant times \(\langle\xi\rangle^{m-|\alpha|+\delta r}\); the corresponding bounds hold through the intermediate integer \(x\)-derivatives. The remainder order in (N18) is \(2-(5/2)(1/2)=3/4\).

The Fourier estimates proved in the appendix give

\[
 L^b:H^{\sigma,p}\longrightarrow H^{\sigma-3/4,p}
 \quad\text{if}\quad -5/4<\sigma-3/4<5/2,
 \qquad 1<p<\infty.                                  \tag{N19}
\]

The high-frequency principal part of \(L^\#\) remains elliptic because the removed symbol has smaller order. Its ordinary smooth-symbol construction gives a left parametrix \(P\in S^{-2}_{1,1/2}\), with a smoothing remainder. This class maps \(H^{t,p}\) to \(H^{t+2,p}\) for every real \(t\).

Take nested compactly supported cutoffs \(\eta\prec\zeta\) in the coefficient ball. Apply the parametrix to \(L(\zeta u)=\zeta f+[L,\zeta]u\). On the support of \(\eta\), the term \(P[L,\zeta]u\) is smooth: the distribution in brackets is supported away from that set and the kernel of \(P\) is smooth off the diagonal. We obtain there

\[
 u=P(\zeta f)-PL^b(\zeta u)+\text{a smooth term}.      \tag{N20}
\]

For \(\sigma=0\), (N19) and (N20) prove

\[
 u\in L^p_{\rm loc}\quad\Longrightarrow\quad
 u\in H^{5/4,p}_{\rm loc}.                            \tag{N21}
\]

All products in the initial distributional equation are legitimate: \(D^2u\in H^{-2,p}_{\rm loc}\), and multiplication by \(C^{5/2}\) functions preserves that space, as the same Fourier estimate with \(\delta=0,m=0\) shows.

Begin with \(p=2\). The local Sobolev embedding for (N21) permits any finite \(q>p\) with
\(1/q>1/p-5/(4d)\). Choose successively
\(1/q=\max\{1/(8d),1/p-1/(2d)\}\) until \(p=8d\). There are finitely many steps; their cutoffs can be nested inside one fixed original ball. This gives \(u\in H^{5/4,8d}_{\rm loc}\). Apply (N19) again with \(\sigma=5/4\); now its target exponent is \(1/2\), in the stated range. Since a compactly supported \(C^{5/2}\) right-hand side belongs to \(H^{1/2,8d}\), (N20) gives

\[
 u\in H^{5/2,8d}_{\rm loc}\subset C^{2,1/4}_{\rm loc}.
                                                               \tag{N22}
\]

The latter embedding has room to spare, since \(5/2-d/(8d)=19/8>2+1/4\). At no step were infinitely many derivatives of the coefficients required. This proves the lemma.

For (N17) apply the **unweighted** formal adjoint of \(\bar\partial\) in the fixed metric \(\omega\):

\[
 L=\bar\partial^*\bar\partial,
 \qquad Lu_j=\bar\partial^*g_j.                       \tag{N23}
\]

The principal symbol of \(L\) is \(|\xi^{0,1}|_\omega^2\), positive for every nonzero real covector \(\xi\). Its coefficients and the right-hand side are at least \(C^{3,1/2}\), so they satisfy the weaker hypotheses of the lemma. The singular weight was used only to select the solution and is absent from (N23). We conclude \(u_j\in C^{2,1/4}\).

## 7. Vanishing of the first jet and coordinate compatibility

Since \(dV_\omega\) is comparable to Euclidean volume near zero, (N17) and continuity force \(u_j(0)=0\). Otherwise its radial integral would dominate \(\int_0 r^{-3}dr\). If the real linear map \(du_j(0)\) were nonzero, it would be bounded away from zero on an open cone of unit directions. Differentiability would then give \(|u_j(r\theta)|\geq cr\) on a smaller cone for sufficiently small \(r\). This contradicts the divergent integral \(\int_0 r^{-1}dr\) in (N17). Therefore

\[
 u_j(0)=0,\qquad du_j(0)=0.
\]

Set \(F_j=\chi z_j-u_j\). Then \(\bar\partial F_j=0\), and \(dF(0)=dz(0)\). The real inverse-function theorem gives a \(C^{2,1/4}\) local diffeomorphism \(F=(F_1,\ldots,F_n)\). Its differential is complex-linear for \(J\), precisely because each component is annihilated by \(T^{0,1}_J\).

If \(G\) is another such coordinate system, the \(C^1\) transition \(G\circ F^{-1}\) has complex-linear differential everywhere. Fix all but one complex variable in a coordinate polydisc. The ordinary one-variable Cauchy–Riemann equations and the real Green formula give zero integrals around every rectangle, hence the one-variable Cauchy integral formula. Applying that formula successively in all variables gives the polydisc Cauchy formula. It follows by differentiating its nonsingular boundary integral that the transition is holomorphic. This also shows that every \(C^1\) function annihilated by \(T^{0,1}_J\) becomes holomorphic in these coordinates. Thus the atlas is compatible and its induced complex structure is exactly \(J\).

## 8. Retaining the holomorphic parameters

Apply the theorem on \(X_0\times B\), of complex dimension \(n=22\), to the distribution

\[
 W_{\bar j}=\partial_{\bar z_j}-\phi_{\bar j}^{a}(h)\partial_{z_a},
 \qquad \partial_{\bar h_\nu},\quad 1\leq\nu\leq20.  \tag{N24}
\]

Its plus-coefficient \(A\) in (N1) is \(-\phi\) in the vertical block and zero in the parameter block. The identity \(\bar\partial\phi=\tfrac12[\phi,\phi]\) makes the vertical brackets vanish with precisely this minus sign. Holomorphic dependence of \(\phi\) as an \(H^8\)-valued function makes the mixed brackets vanish. Small \(C^0\) norm gives complementarity with the conjugate distribution. The uniform spatial \(C^{5,1/2}\) bounds for every parameter derivative, obtained on smaller parameter balls from its normally convergent Banach-valued series, give the joint regularity used in Section 1.

Each function \(h_\nu\) is annihilated by (N24). It is therefore holomorphic in the atlas just constructed. The real differential of \(h\) has rank 40 and is complex-linear, so its complex rank is 20. In one holomorphic coordinate chart choose two linear coordinate combinations whose differentials complement the independent \(dh_\nu\). The map

\[
 (F_1,\ldots,F_{22})\longmapsto
 (w_1,w_2,h_1,\ldots,h_{20})                           \tag{N25}
\]

has invertible complex derivative. The real inverse-function theorem and the preceding transition argument show that its inverse is holomorphic. This proves the local product-coordinate assertion for the parameter map.

Consequently the underlying product projection becomes a holomorphic submersion, with complex two-dimensional fibres. It is proper because \(X_0\) is compact. At \(h=0\), \(\phi(0)=0\), so the central fibre has its original complex structure. The new atlas is holomorphic and hence smooth in its own coordinates; no assertion that the original \(J\) has become smooth in the original product coordinates is needed. Smooth horizontal-lift arguments can now be made in this new smooth structure. None of these steps changes the integral marking, the rational coefficient field in the lesson, or the later arbitrary-rank argument.

## Appendix. The Fourier estimates used in the elliptic lemma

This appendix specifies the analytic inputs in (N18)–(N22) and supplies their derivation. Ordinary Fourier inversion, Plancherel, the Lebesgue differentiation theorem, and the elementary Hilbert-space and integration results used above are the underlying analysis conventions.

Choose smooth dyadic Fourier projections \(\Delta_k\), and enlarged projections equal to one on their supports. The two estimates needed are the square-function equivalence

\[
 \|v\|_{H^{s,p}}\asymp
 \left\|\left(\sum_k2^{2ks}|\Delta_kv|^2\right)^{1/2}\right\|_p,
 \quad1<p<\infty,                                   \tag{F1}
\]

and its synthesis versions: for terms supported in annuli the corresponding sum is bounded by the square-function norm for all real \(s\); for terms supported in balls of radius \(C2^k\), the same assertion holds for \(s>0\).

Here is one derivation, including the \(L^p\) ingredient. A smooth multiplier \(m(\xi)\), also allowed to have values in bounded operators between Hilbert spaces, whose derivatives satisfy
\(\|D^\alpha m(\xi)\|\leq C_\alpha\langle\xi\rangle^{-|\alpha|}\), has uniformly \(L^2\)-bounded smooth truncations by Plancherel. Integration by parts in each frequency shell and summation give the kernel bounds \(|K(x)|\leq C|x|^{-d}\), \(|\nabla K(x)|\leq C|x|^{-d-1}\). For an \(L^1\) input, take maximal dyadic cubes where the average of its norm exceeds \(\lambda\). They are disjoint, their total volume is at most \(\|v\|_1/\lambda\), and their parent-cube averages bound their averages by \(2^d\lambda\). Replace \(v\) on each cube by its average and call the remaining, mean-zero, cube-supported parts \(b_Q\). Lebesgue differentiation gives a good part bounded by \(2^d\lambda\), with its squared \(L^2\) norm at most \(C\lambda\|v\|_1\). The \(L^2\) estimate handles this part. Outside a fixed dilation of \(Q\), subtract the kernel value at its centre; the gradient bound and the mean-zero property give
\(\int_{(Q^*)^c}|m(D)b_Q|\leq C\|b_Q\|_1\).
Summing proves the weak \((1,1)\) bound. Interpolation with the \(L^2\) bound follows directly by splitting \(v\) at size proportional to \(\lambda\) and integrating the distribution formula
\(\|Tv\|_p^p=p\int_0^\infty\lambda^{p-1}|\{|Tv|>\lambda\}|d\lambda\): the two inner integrals have exponents \(p-2\) and \(p-3\), convergent on their respective ranges for \(1<p<2\). Duality handles \(p>2\). The argument uses norms, averages and Hilbert-space Plancherel, so it also proves the Hilbert-valued assertion.

Apply this assertion to the operator-valued multiplier
\(v\mapsto(\varphi_k(D)v)_k\), where \(\sum_k\varphi_k^2=1\), and its transpose. This gives (F1) for \(s=0\). Applying it also to the enlarged shell multipliers \(2^{ks}\langle\xi\rangle^{-s}\varphi_k(\xi)\) gives general \(s\). Annular synthesis follows by the transpose estimate and finite overlap. For ball synthesis, use the upper-triangular matrix of shell cutoffs with coefficients \(2^{-(k-j)s}\), \(k\geq j\). Its row and column sums, and their symbol derivatives, are bounded when \(s>0\). The same Hilbert-valued multiplier bound gives the asserted synthesis estimate. This accounts for the sign restriction in the ball version.

It suffices first to take order zero. Choose a fixed annular cutoff and a larger compactly supported cutoff equal to one on its support. On frequency shell \(k\), rescale the frequency variable by \(2^{-k}\) and extend the resulting cutoff symbol periodically on one fixed cube. Write its Fourier series as
\[
 a_k(x,\xi)=\sum_{\ell\in\mathbb Z^d}
 Q_{k\ell}(x)e^{ic\,2^{-k}\ell\cdot\xi}\varphi_k(\xi),
\]
where the fixed constant \(c\) is determined by the cube's period. One can absorb a harmless enlargement of the shell cutoff into \(\varphi_k\). Integration by parts in the periodic variable gives, for every chosen integer \(M\),
\[
 \|Q_{k\ell}\|_\infty\le C_M(1+|\ell|)^{-M},
 \qquad
 \|Q_{k\ell}\|_{C^r}\le
 C_M(1+|\ell|)^{-M}2^{kr}.
\]
Only finitely many frequency derivatives, and the stated \(r\) spatial Hölder derivatives, enter any fixed such bound.

The phase factor must be retained: it is a translation of input \(k\) at a scale depending on \(k\). Put
\[
 v_{k\ell}
 =e^{ic\,2^{-k}\ell\cdot D}\varphi_k(D)v.
\]
For a fixed Sobolev exponent \(s\), the multiplier from scalar functions to \(\ell^2\)-valued functions with components
\[
 2^{ks}\langle\xi\rangle^{-s}
 e^{ic\,2^{-k}\ell\cdot\xi}\varphi_k(\xi)
\]
has finite overlap at every nonzero frequency. Its operator-valued derivatives satisfy the hypotheses of the preceding Hilbert-valued multiplier argument, with constants bounded by a polynomial in \(1+|\ell|\). Indeed each derivative of the phase contributes \(2^{-k}\ell\); on the shell, \(2^{-k}\) is comparable to \(\langle\xi\rangle^{-1}\). Thus, for some finite \(N=N(d,p,s)\),
\[
 \left\|\left(\sum_k2^{2ks}|v_{k\ell}|^2\right)^{1/2}\right\|_p
 \le C(1+|\ell|)^N\|v\|_{H^{s,p}}.
\]
The finite value of \(N\) follows from the finite number of kernel derivatives used in the preceding Calderón–Zygmund proof; no spatial derivatives of the original coefficient beyond \(r\) have been added.

For each fixed \(\ell\), split \(Q_{k\ell}\) into spatial frequencies below \(k-3\), within three of \(k\), and above \(k+3\). The low part has a uniformly bounded low-pass kernel and gives annular output. The middle part has finitely many uniformly bounded pieces and gives ball output. Their weighted square-function bounds are therefore at most
\[
 C_M(1+|\ell|)^{-M}
 \left\|\left(\sum_k2^{2ks}|v_{k\ell}|^2\right)^{1/2}\right\|_p,
\]
using annular synthesis for the first part and ball synthesis, hence \(s>0\), for the second.

For the high part, the Hölder tail estimate gives
\[
 \|\Delta_jQ_{k\ell}\|_\infty
 \le C_M(1+|\ell|)^{-M}2^{-r(j-k)}
 \quad (j>k+3).
\]
The product has annular frequency of size \(2^j\). After multiplying by \(2^{js}\), its pointwise sequence estimate contains
\[
 2^{-(r-s)(j-k)}\,2^{ks}|v_{k\ell}|.
\]
Convolution with this positive summable sequence is bounded on \(\ell^2\) when \(s<r\). Annular synthesis then gives the same bound as above. Combining the three parts proves
\[
 \|a_\ell(x,D)v\|_{H^{s,p}}
 \le C_M(1+|\ell|)^{-M+N}\|v\|_{H^{s,p}}
 \qquad(0<s<r).
\]
Choose \(M>N+d\). Summation over \(\ell\) now converges in operator norm and proves F2 in order zero. For general order \(m\), apply this result to the symbol \(a(x,\xi)\langle\xi\rangle^{-m}\) and the input \(\langle D\rangle^m v\). This gives

\[
 C^rS^m_{1,1}:H^{s+m,p}\longrightarrow H^{s,p}
 \quad(0<s<r).                                      \tag{F2}
\]

The Hölder tail bound follows by subtracting the Taylor polynomial through degree \(\lfloor r\rfloor\) inside the convolution kernel, whose corresponding moments vanish. It also proves the smoothing bound
\(\|(1-\chi(2^{-k\delta}D))a\|_{C^j}\leq C2^{-k\delta(r-j)}\) for \(0\leq j<r\). This proves (N18), with the intermediate derivative bounds included.

For smooth symbols \(S^m_{1,\delta}\), \(\delta<1\), the product and adjoint formulas come from Taylor expansion in the Fourier composition integral. After \(N\) terms their remainder loses \((1-\delta)N\) orders. Integrating the remainder by parts gives the same symbol estimates. Successive cutoffs of the terms give an actual symbol with that asymptotic expansion. This proves closure under composition and adjoint and constructs the elliptic inverse, beginning with the reciprocal of the elliptic principal symbol; recursively canceling the error lowers its order by \(1-\delta\) at each stage. The resulting remainder has arbitrarily negative order and a smooth kernel. These arguments concern the smoothed symbol only. Estimate (F2), applied with arbitrarily large \(r\), gives its positive Sobolev mapping orders; conjugation by the Fourier multipliers \(\langle D\rangle^t\), using the product formula, gives every real order. In particular \(S^m_{1,\delta}\) maps \(H^{s+m,p}\) to \(H^{s,p}\) for every \(s\).

Finally let \(a\in C^rS^m_{1,\delta}\), with \(\delta<1\). Smooth its \(x\)-dependence on frequency shell \(k\) at a faster frequency scale \(2^{k\gamma}\), where \(\delta<\gamma<1\). It decomposes into a smooth symbol in \(S^m_{1,\gamma}\) and a remainder in
\(C^rS^{m-(\gamma-\delta)r}_{1,\gamma}\). For the remainder choose a positive output exponent \(s+(\gamma-\delta)r\), apply (F2), and then include the resulting Sobolev space into \(H^{s,p}\). This is permitted whenever
\(0<s+(\gamma-\delta)r<r\). Letting \(\gamma\) approach 1 gives

\[
 C^rS^m_{1,\delta}:H^{s+m,p}\longrightarrow H^{s,p}
 \quad\text{for}\quad -(1-\delta)r<s<r.              \tag{F3}
\]

For positive \(s\) the original (F2) already applies; for nonpositive \(s\), choose \(\gamma\) satisfying the strict inequalities just displayed. Formula (N19) is (F3) with \(r=5/2\), \(m=3/4\), and \(s=\sigma-3/4\).

The local embeddings used above can also be read from (F1). The kernel of \(\langle D\rangle^{-t}\), obtained by its Gaussian integral representation, is \(O(|x|^{t-d})\) near zero and rapidly decreasing at infinity. Truncating the singularity and applying the distribution-function argument gives the Sobolev gain in \(L^p\); strictly smaller gains, which are all that were used, also follow from Young's inequality with an integrable power of this kernel. Bernstein's estimate on each shell gives
\(\|\Delta_kv\|_\infty\leq C2^{kd/p}\|\Delta_kv\|_p\). Summing with a small loss proves \(H^{s,p}\subset C^{t}\) for every positive noninteger \(t<s-d/p\). The Hölder conclusion follows by splitting the dyadic sum at the reciprocal displacement and using the mean-value bound below that frequency. These strict embeddings suffice for (N21) and (N22).

## Sources and mathematical scope

The coordinate construction is based on Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, author edition dated 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter VIII, §11, physical/printed pp.397–401, especially Theorem 11.8 and Lemmas 11.10–11.11. Its written theorem assumes a smooth almost-complex structure. The finite-\(C^{5,1/2}\) conclusion above is not attributed to that statement: the finite jets, finite coefficient integration by parts, domain approximation and elliptic regularity have been supplied explicitly here. For the Hilbert-space solution argument and its scalar/canonical-line conversion, see VIII §§1–6, especially pp.363–373 and 376–378. The proof uses the same classical weighted-solution mechanism, with a direct degree-one matrix cancellation for the auxiliary complete metric.

For the finite-coefficient Fourier argument, see Michael E. Taylor, [*Pseudodifferential Operators and Nonlinear PDE*, author PDF](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/NLIN.pdf): §1.3, pp.40–43; §2.1, pp.44–50; §2.2, pp.52–53 and 56–57; §0.11, pp.28–32; and Appendix A.1, pp.172–175. The strict mapping interval (F3) is Proposition 2.1.E; the general regularity statement (2.2.15) gives a stronger conclusion than needed here. The dyadic proof and the particular two gains \(5/4\), \(5/2\) are written out above so that a fixed high-dimensional \(L^2\) embedding is not substituted for that input. Taylor's discussion of Calderón–Zygmund decomposition and interpolation refers onward for those two elementary proofs; the needed dyadic decomposition and distribution-function argument have therefore been included rather than credited as full proofs in those pages.

The coordinate theorem uses Fourier inversion and Plancherel, Lebesgue differentiation and elementary integration, Hilbert projection, Hahn–Banach and Riesz representation, and the real inverse-function theorem. The result concerns the coordinate interface; the remaining arguments in the Picard-zero construction retain their own stated hypotheses. The CC0 dedication applies to this independent exposition, while the cited books retain their own terms.