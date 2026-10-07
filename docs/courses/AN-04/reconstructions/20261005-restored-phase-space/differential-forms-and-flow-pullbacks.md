# Differential forms and flow pullbacks

This companion proves the differential-form identities used by *Phase space and generating families*. All arguments are local in a smooth coordinate chart; a manifold and its compatible charts are given data. The earlier inputs are [finite calculus and mixed derivatives](../20261004-free-stationary-phase/prerequisite-completions.md), [FTC and smooth compact parameter integrals](../20261004-free-stationary-phase/proof-map.html#FTC-TAYLOR-COMPACT-PARAMETERS), and the complete [AN-03 flow proof](finite-coordinate-flows.md), equations NF1–NF21. Their exact providers occur in the [proof map](proof-map.json).

## F0. Alternating forms and their coordinate operations

For coordinates \(x^1,\ldots,x^d\), a smooth \(k\)-form is a finite sum \(\eta=\sum_{i_1<\cdots<i_k}\eta_{i_1\cdots i_k}\,dx^{i_1}\wedge\cdots\wedge dx^{i_k}\), with smooth coefficients. The wedge of the coordinate covectors is evaluated by the determinant of their values on the argument vectors. Repeated indices give zero; exchanging adjacent covectors changes the sign. Extend the product by linearity. Concatenating lists and then sorting shows associativity; exchanging lists of lengths \(k,l\) uses \(kl\) transpositions and proves \(\eta\wedge\zeta=(-1)^{kl}\zeta\wedge\eta\). These calculations also define the product independently of a basis, since determinants are multilinear and alternating.

Define the exterior derivative by

\[
d\eta=\sum_I\sum_j(\partial_j\eta_I)\,dx^j\wedge dx^I.
\tag{F0.1}
\]

The product rule and the sign for moving \(dx^j\) past a list of length \(k\) give
\(d(\eta\wedge\zeta)=d\eta\wedge\zeta+(-1)^k\eta\wedge d\zeta\).
In \(d^2\eta\), the terms with indices \(j,l\) cancel those with \(l,j\): mixed partials agree while their two covectors change sign. The terms with \(j=l\) vanish. Thus \(d^2=0\).

For a smooth map \(f\), define \((f^*\eta)_x(v_1,\ldots,v_k)=\eta_{f(x)}(Df_xv_1,\ldots,Df_xv_k)\). Substituting the coordinate expression gives
\(f^*(a\,dy^{i_1}\wedge\cdots\wedge dy^{i_k})=(a\circ f)\,df^{i_1}\wedge\cdots\wedge df^{i_k}\).
The chain rule, the product rule and \(d^2f^j=0\) now prove \(d f^*\eta=f^*d\eta\). The same evaluation proves that pullback preserves wedge products and that \((f\circ g)^*=g^*f^*\). In particular F0.1 is compatible with changes of coordinates, so these local definitions agree on overlaps.

For a vector field \(V\), let \((\iota_V\eta)(v_1,\ldots,v_{k-1})=\eta(V,v_1,\ldots,v_{k-1})\), and set \(\iota_Va=0\) on functions. Expansion along the first row of the defining determinant gives

\[
\iota_V(dx^{i_1}\wedge\cdots\wedge dx^{i_k})
=\sum_{a=1}^k(-1)^{a-1}V^{i_a}
 dx^{i_1}\wedge\cdots\widehat{dx^{i_a}}\cdots\wedge dx^{i_k}.
\tag{F0.2}
\]

Splitting this sum between two lists proves
\(\iota_V(\eta\wedge\zeta)=\iota_V\eta\wedge\zeta+(-1)^k\eta\wedge\iota_V\zeta\).
All identities include degree zero and degrees above the coordinate dimension, where the corresponding alternating forms vanish.

## F1. Cartan's formula and the commutator identity

Let \(\varphi_t\) be the local flow of \(V\), supplied by NF1–NF20, and define
\(\mathcal L_V\eta=\left.\partial_t\varphi_t^*\eta\right|_{t=0}\).
The coordinate pullback formula of F0 and \(\partial_t\varphi_t^j|_0=V^j\) imply
\(\mathcal L_Va=V(a)\) and \(\mathcal L_Vdx^j=dV^j\).
Differentiating the wedge product shows that \(\mathcal L_V\) is a derivation of degree zero.

The sum \(d\iota_V+\iota_Vd\) is also a degree-zero derivation: insert the two signed product rules in F0; the terms containing \(d\eta\wedge\iota_V\zeta\) and \(\iota_V\eta\wedge d\zeta\) cancel in pairs. On a function its value is \(\iota_Vda=V(a)\), and on \(dx^j\) its value is \(dV^j\). Every coordinate form is a sum of products of these generators. Therefore

\[
\mathcal L_V=d\iota_V+\iota_Vd,\qquad
\mathcal L_Vd=d\mathcal L_V.
\tag{F1.1}
\]

For the second equality use \(d^2=0\) in the first. For two fields define \([V,W]^j=\sum_l(V^l\partial_lW^j-W^l\partial_lV^j)\); expanding on a smooth function and cancelling its symmetric second derivatives gives \([V,W]a=V(Wa)-W(Va)\).
The operator \(\mathcal L_V\iota_W-\iota_W\mathcal L_V\) is a derivation of degree minus one, by the same signed-product cancellation. It vanishes on functions, and on \(dx^j\) it is
\(V(W^j)-\iota_WdV^j=[V,W]^j\).
It agrees with \(\iota_{[V,W]}\) on every generator and hence on every form:

\[
\mathcal L_V\iota_W-\iota_W\mathcal L_V=\iota_{[V,W]}.
\tag{F1.2}
\]

## F2. Differentiating a time-dependent pullback

Suppose \(\Psi_t\) solves \(\partial_t\Psi_t=V_t\circ\Psi_t\), with its actual domain, and \(\eta_t\) is a smooth family of forms. NF1–NF20 gives joint smoothness of \(\Psi\), so coordinate and time derivatives commute. On a coefficient \(a_t\), the chain rule gives
\(\partial_t(a_t\circ\Psi_t)=(\partial_ta_t+V_ta_t)\circ\Psi_t\).
On a pulled-back coordinate covector,
\(\partial_t d\Psi_t^j=d(V_t^j\circ\Psi_t)=\Psi_t^*dV_t^j\).
Expand a general form as in F0 and differentiate each factor. F1 identifies the resulting sum as

\[
\frac{d}{dt}\Psi_t^*\eta_t
=\Psi_t^*(\partial_t\eta_t+\mathcal L_{V_t}\eta_t).
\tag{F2.1}
\]

The identity holds on each common open domain and hence in every chart. It requires neither a globally complete vector field nor a time-independent one. If the right side is zero, each coordinate coefficient has zero time derivative; the scalar FTC proves that the pullback is constant in time.

## F3. The radial homotopy and closed one-forms

Let \(U\subset\mathbb R^d\) be star-shaped about zero. For \(k\geq1\) and a smooth \(k\)-form \(\eta\), define

\[
(K\eta)_x(v_1,\ldots,v_{k-1})
=\int_0^1t^{k-1}\eta_{tx}(x,v_1,\ldots,v_{k-1})\,dt.
\tag{F3.1}
\]

Set \(K=0\) on zero-forms. The integrand is smooth through \(t=0\); every compact local set of \(x\)'s and its radial segments lie in a compact subset of \(U\). The proved compact parameter integral rule makes \(K\eta\) smooth and permits exterior differentiation under the integral.

Write \(h_t(x)=tx\), \(E_x=x\). For \(t>0\), \(h_t\) is the flow of \(E\) with time \(\log t\). By F1–F2,
\(\partial_t h_t^*\eta=t^{-1}h_t^*(d\iota_E\eta+\iota_Ed\eta)\).
The first integrand \(t^{-1}h_t^*\iota_E\eta\), evaluated on \(k-1\) vectors, equals exactly the integrand in F3.1; the corresponding expression for \(d\eta\) is its degree \(k+1\) version. Integrate from \(\epsilon\) to 1, use F0 to commute pullback and \(d\), and let \(\epsilon\downarrow0\). The smooth integrands give uniform convergence with each local derivative; for \(k>0\), \(h_\epsilon^*\eta=\epsilon^k\eta_{\epsilon x}\) tends to zero. For a function it tends to its value at zero. Thus

\[
dK\eta+Kd\eta=\eta-h_0^*\eta.
\tag{F3.2}
\]

In particular, every closed positive-degree form on \(U\) has primitive \(K\eta\). For a closed one-form its primitive is the function \(\int_0^1\eta_{tx}(x)\,dt\). For a closed two-form \(\beta\) with \(\beta_0=0\), F3.1 gives the one-form used in Darboux's proof. The segment FTC bounds \(\|\beta_{tx}\|\leq Ct|x|\) near zero, whence \(|(K\beta)_x(v)|\leq C|x|^2|v|/3\). This proves the stated quadratic vanishing, not just existence of a primitive.

## F4. A common neighborhood through a prescribed time interval

Suppose the smooth nonautonomous field \(V_t(x)\) is defined on an open neighborhood of \([0,1]\times\{0\}\), and \(V_t(0)=0\). The constant curve is a solution for every \(t\in[0,1]\). NF17–NF20 proves that its full solution domain in \((t,\tau,x)\) is open and the solution is smooth there. For each \(t\in[0,1]\), choose a product neighborhood of \((t,0,0)\) inside that domain. Finitely many of their time neighborhoods cover \([0,1]\); intersect their initial-data neighborhoods. This gives one neighborhood of \(x=0\) on which the flow from initial time zero exists for all those times. NF19 gives the smooth inverse at each time. Uniqueness gives \(\Psi_t(0)=0\).

This applies to the field in Darboux's proof: the constant skew matrix of \(\omega_0\) is invertible. Since \(\omega-\omega_0\) tends to zero at the origin, continuity of the determinant gives a common small neighborhood on which \(\omega_0+t(\omega-\omega_0)\) is invertible for \(t\) in an open interval containing \([0,1]\). P2 proves that its inverse is smooth. Hence \(\iota_{V_t}\omega_t=-K(\omega-\omega_0)\) defines a smooth field with \(V_t(0)=0\), and the preceding argument applies. No completeness assumption is hidden in the time-one map.

*Standard foundation proofs written by GPT-6 Astra (OpenAI), Ultra, 5 October 2026, for the AN-04 programme. Original companion text: CC0. The linked AN-03 flow proof is a separate GFDL 1.2 component.*
