# Transverse pullback of normalized conormal cycles

Transversality identifies the pulled-back conormal carrier with the conormal of the inverse-image submanifold. To obtain an equality of cycles, we must also identify their normalized coefficients. The graph comparison supplies a relative fibre trace; composition of its actual counits preserves the point unit that defines the tangent zero section. This proves the coefficient equality even when the tangential derivative changes rank.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Read Pulling back Lagrangian cycles through a graph for the actual coefficient adjoint, its proof and the definitions of normalized zero and conormal cycles. Lagrangian cycles and proper cotangent images supplies the closed-embedding trace defining the latter. Continuous sections and supported cycle intersections supplies the normalized point intersection number used in Exercise 2. The exact current SH-02 prerequisites are the counit-normalized relative orientation and dual-frame pairings, and the commuting direct microlocal square with its specified trace vertical.

This lesson proves the transverse pullback formula for normalized conormal cycles, in the framework of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). Coefficients remain a commutative ring \(A\) of finite global dimension. Manifolds are real analytic, Hausdorff and countable at infinity, of uniformly bounded finite dimensions. All tensor products and sheaf operations below are derived unless the factors are flat sheaves. Dimensions may be treated component by component.

## The theorem includes a coefficient equality

Let \(i:Z\hookrightarrow X\) be a closed analytic submanifold of codimension \(c\), and let \(f:Y\to X\) be analytic. Assume

\[
 df_y(T_yY)+T_{f(y)}Z=T_{f(y)}X
 \quad\text{for every }y\in W=f^{-1}Z.
 \qquad\text{(1)}
\]

The inverse-image theorem makes \(W\) a closed analytic submanifold of codimension \(c\); denote its embedding by \(j:W\hookrightarrow Y\). If \(W\) is empty, both the pulled-back carrier and the output cycle are empty, and the equality below is immediate. Otherwise write \(n=\dim X\), \(m=\dim Y\), \(a=n-c\) and \(b=m-c\). With the normalizations already defined,

\[
 [T_Z^*X]=i_*[T_Z^*Z],\qquad
 [T_W^*Y]=j_*[T_W^*W],\qquad
 [T_Q^*Q]=a_Q^*[\mathrm{pt}].
 \qquad\text{(2)}
\]

We will prove that the cotangent inverse-image operation is defined on the first cycle and that

\[
 f^*[T_Z^*X]=[T_W^*Y].
 \qquad\text{(3)}
\]

No properness of \(f\), submersion condition on \(f\), constant rank of its tangential derivative, or global orientation of any manifold is assumed.

## The actual graph coefficient is a relative fibre trace

Retain the cotangent correspondence and coefficient notation

\[
 \begin{gathered}
 C_f=Y\times_XT^*X,
 \quad p:C_f\to Y,\quad r=f_d:C_f\to T^*Y,\quad s=f_\pi:C_f\to T^*X,\\
 E_X=\pi_X^{-1}\omega_X,\quad E_Y=\pi_Y^{-1}\omega_Y,
 \quad Q=s^{-1}E_X=p^{-1}f^{-1}\omega_X.
 \end{gathered}
 \qquad\text{(4)}
\]

The projections \(p,\pi_X,\pi_Y\) are vector-bundle submersions. An ordered tangent frame and its dual cotangent frame give a canonical integral orientation-line pairing. Their transition determinants have the same sign. Consequently, with their submersion traces retained, there are identifications

\[
 E_X\simeq\omega_{\pi_X},\qquad
 E_Y\simeq\omega_{\pi_Y},\qquad Q\simeq\omega_p.
 \qquad\text{(5)}
\]

These are identifications of relative dualizing coefficients along cotangent fibres. They do not choose an orientation of the total cotangent space. The square pairing of unshifted sign lines and the evaluation of shifted inverse lines are used in their indicated orders.

Since \(\pi_Yr=p\), exceptional composition gives

\[
 r^!\omega_{\pi_Y}\simeq\omega_p.
 \qquad\text{(6)}
\]

Let \(\gamma_f:Q\to r^!E_Y\) be the isomorphism obtained from (5) and the inverse of (6). We must show that it is the actual adjoint \(\beta_f\) constructed through the graph in the preceding lesson. An arbitrary isomorphism of these objects would leave (3) undetermined.

Use that lesson's \(F_1=\operatorname{id}_Y\times f\), diagonal \(N\), graph \(M\), \(K=f^{-1}\omega_X\) and \(\mathscr G=\delta_{Y*}K\). Its center-supported microlocalizations are \(H=\pi_Y^{-1}K\) and \(Q\), and its center map is the identity. The direct microlocal square therefore reads

\[
 \begin{array}{ccc}
 r^{-1}H&\xrightarrow{a_{\mathscr G}}&Q\\
 \downarrow t_r&&\downarrow\mathrm{id}\\
 r^!H\otimes L&\xleftarrow{d_{\mathscr G}}&Q,
 \end{array}
 \quad
 L=p^{-1}\bigl(\omega_Y\otimes K^{-1}\bigr),
 \quad\omega_r=L^{-1}.
 \qquad\text{(7)}
\]

Here \(t_r\) is the specified relative-trace comparison

\[
 r^{-1}H\simeq r^{-1}H\otimes\omega_r\otimes L
 \longrightarrow r^!H\otimes L.
 \qquad\text{(8)}
\]

The upper arrow in (7) is the identity under \(r^{-1}H=Q\). To check this particular arrow, specialize the center-supported complex: it is the coefficient \(K\) on the zero normal section. The normal map on that zero section is the identity of its base \(Y\), with proper support. In its Fourier correspondence the zero normal vector has pairing zero with every covector, and the projection of this supported kernel is the identity. Thus the upper proper comparison sends \(1\) to \(1\), with no Fourier integration shift. This is a check of the upper map, as well as its objects. The right vertical is the identity because \(F_1\) is proper on the diagonal support. Commutativity now gives \(d_{\mathscr G}=t_r\).

Under the graph lesson's actual right-tensor extraction, the target of (8) is transported by

\[
 r^!H\otimes L
 \simeq r^!\bigl(\pi_Y^{-1}(K\otimes(\omega_Y\otimes K^{-1}))\bigr)
 \simeq r^!E_Y.
 \qquad\text{(9)}
\]

The last map moves the relative line to the left and then uses its ordered inverse pairing with \(K\). The resulting map (8)–(9) is \(\beta_f\), by the actual microlocal adjunction identity proved in the graph lesson.

It is also \(\gamma_f\). Here is the coefficient check. The relative line for the fibre map \(r\), from the two vector-bundle projections, is

\[
 \omega_r\simeq\omega_p\otimes r^{-1}\omega_{\pi_Y}^{-1}
 \simeq Q\otimes r^{-1}E_Y^{-1}.
 \qquad\text{(10)}
\]

This is exactly the inverse dual-bundle ratio in (7), with the counit-normalized right extraction. Substituting (10) into (8)–(9) cancels the final invertible factors and leaves the inverse composition map \(\omega_p\to r^!\omega_{\pi_Y}\). To check the rearrangements explicitly, \(K\) has shift \(n\) and \(L\) has shift \(m-n\). Moving \(K\) through \(\omega_r\) contributes \( (-1)^{n(n-m)}\); the subsequent move through \(L\) contributes \( (-1)^{n(m-n)}\). Their product is \(1\). The unshifted orientation ratios are the dual-frame ratios in (5). The remaining contractions are the specified coherent inverse pairings; a left internal-Hom counit is not substituted for a right extraction. This identifies the actual transformations, so

\[
 \beta_f=\gamma_f,\qquad
 \rho_f:Rr_!Q\longrightarrow E_Y
 \text{ is the relative trace for }r\text{ under (5)}.
 \qquad\text{(11)}
\]

The trace uses \(Rr_!\), even if \(r\) is nonproper. Properness will be checked only on the cycle carrier. Neither (6) nor (11) asserts that this direct trace is an isomorphism.

## A supported point unit survives every tangential rank

For a manifold \(R\), let \(z_R:R\hookrightarrow T^*R\) be its zero embedding. For \(a_R:R\to\mathrm{pt}\), the cotangent map is \(z_R\). Equations (6)–(11) identify its coefficient adjoint with

\[
 A_R\simeq z_R^!\omega_{\pi_R}.
 \qquad\text{(12)}
\]

The adjoint supported morphism is therefore the actual point trace in each cotangent fibre. Thus the zero cycle in (2) is the fibrewise zero-point unit, using (5).

This statement also proves, for every analytic \(g:V\to U\),

\[
 g^*[T_U^*U]=[T_V^*V].
 \qquad\text{(13)}
\]

Indeed the pullback of the zero section to \(C_g\) is its zero section \(e:V\hookrightarrow C_g\). Pullback of the unit in (12) is the point unit \(e_*A_V\to\omega_{p_g}\). This comparison is the vector-bundle base-change comparison: locally the fibre coordinates and their zero embedding are unchanged, so their normal costalk and trace pairing are unchanged. It requires no ordinary nonproper fibre base-change theorem.

The cotangent map satisfies \(g_de=z_V\), and is proper on \(e(V)\), because that restriction is a homeomorphism onto a closed zero section. Apply its relative trace. The resulting supported morphism is

\[
 z_{V*}A_V=Rg_{d!}e_*A_V
 \longrightarrow Rg_{d!}\omega_{p_g}
 \longrightarrow\omega_{\pi_V}.
 \qquad\text{(14)}
\]

Exceptional composition and the composed-counit identity identify (14) with the point unit \(z_{V*}A_V\to\omega_{\pi_V}\). Namely \(e^!g_d^!\omega_{\pi_V}=z_V^!\omega_{\pi_V}=A_V\), and both adjoint maps are the identity of \(A_V\). This proves equality before forgetting the zero support.

The same argument applies to a family of linear maps \(\ell_y:\mathbb R^{a*}\to\mathbb R^{b*}\). Its image of the zero-supported point unit is the zero-supported point unit in \(\mathbb R^{b*}\): \(\ell_y0=0\), and the actual exceptional counits compose. The map may have a noncompact kernel or changing rank. We have pushed forward a point-supported unit, whose image is proper, rather than a class supported on the whole source fibre.

## Transverse normal coordinates and the proper carrier map

Near a point of \(W\), choose analytic coordinates \(X=(t,z)\) with \(Z=\{z=0\}\), where \(t\in\mathbb R^a\), \(z\in\mathbb R^c\). Condition (1) allows coordinates \(Y=(u,v)\), \(u\in\mathbb R^b\), \(v\in\mathbb R^c\), for which

\[
 f(u,v)=(g(u,v),v),\qquad W=\{v=0\}.
 \qquad\text{(15)}
\]

Take covectors \((\tau,\zeta)\) dual to \((t,z)\), and \((\eta_u,\eta_v)\) dual to \((u,v)\). The correspondence maps are

\[
 \begin{aligned}
 s(u,v;\tau,\zeta)&=(g(u,v),v;\tau,\zeta),\\
 r(u,v;\tau,\zeta)&=(u,v;g_u^t\tau,g_v^t\tau+\zeta).
 \end{aligned}
 \qquad\text{(16)}
\]

The pulled-back conormal carrier and its image are

\[
 \begin{gathered}
 B=s^{-1}(T_Z^*X)=\{v=0,\ \tau=0,\ \zeta\in\mathbb R^{c*}\},\\
 r(B)=\{v=0,\ \eta_u=0,\ \eta_v\in\mathbb R^{c*}\}=T_W^*Y,\\
 r(u,0;0,\zeta)=(u,0;0,\zeta).
 \end{gathered}
 \qquad\text{(17)}
\]

Globally \(df_y^t\) restricts to an isomorphism from \(N^*_{f(y)}Z\) to \(N_y^*W\). Its inverse depends analytically on local normal charts. These inverses agree as bundle inverses, so \(r|_B\) is a homeomorphism onto the closed conormal \(T_W^*Y\). Its composition with that closed inclusion is proper. This establishes the properness needed for \(f^*\), including over a noncompact \(W\).

## The coefficient and normalization in the normal chart

In the product chart \(X=(t,z)\), the definition \(i_*[T_Z^*Z]\) has two factors. The tangent zero section is the point unit in the \(\tau\) variables, with coefficient \(\omega_{\mathbb R^{a*}}\). The closed embedding \(z=0\) contributes its actual normal trace, paired with the normal dual-frame coefficient \(\omega_{\mathbb R^{c*}}\) in the \(\zeta\) variables. Keep the order tangent first, normal second:

\[
 A_{\{z=0,\tau=0\}}
 \longrightarrow
 \omega_{\mathbb R^{a*}}\otimes
 \omega_{\mathbb R^{c*}}=E_X
 \quad\text{in this chart}.
 \qquad\text{(18)}
\]

More explicitly, the first morphism is the zero-point trace in \(\tau\); the second is the closed \(z=0\) trace in \(\operatorname{or}_z[c]\), identified with the constant coefficient \(\operatorname{or}_{\zeta}[c]\) by the dual frame. Their tensor, with the base \(t\) retained, is (18). The normal costalk in \(z\) is \(\operatorname{or}_z[-c]\); its ordered pairing cancels the corresponding factor of \(\omega_X\). This recovers the actual closed-embedding construction, and fixes its unit rather than only its rank-one coefficient object.

Pull (18) back by \(s\). The normal variables \((z,\tau)\) of its support pull back to \((v,\tau)\) by the identity. Their normal Thom maps and trace pairings therefore remain the same actual unit maps. Tangential dependence of \(g\) changes no normal variable in this calculation.

Now use the source fibre shear

\[
 (\tau,\zeta)\longmapsto(\tau,\zeta'),
 \qquad \zeta'=\zeta+g_v^t\tau.
 \qquad\text{(19)}
\]

It is an analytic fibre diffeomorphism with block triangular determinant \(+1\). It fixes \(\tau=0\), preserves the normal \(v\) variable, and changes \(r\) into

\[
 (u,v;\tau,\zeta')\longmapsto
 (u,v;g_u^t\tau,\zeta').
 \qquad\text{(20)}
\]

Its trace transports the ordered fibre dualizing coefficient without a sign. The map (20) is the family \(\ell_{u,v}=g_u^t\) on tangent covectors, times the identity on normal covectors. Under (11), the coefficient map is precisely its relative fibre trace. The product projection formula and counit composition identify this trace with the tangent trace tensored with the identity normal trace, in the order used in (18).

By (14), the tangent trace sends the \(\tau=0\) point unit to the \(\eta_u=0\) point unit, for every rank of \(g_u\). The normal \(v=0\) trace is retained: \(r\) preserves the base \(v\), so projection-formula naturality commutes its pulled-back morphism with the fibre trace. This argument uses the explicit product normal chart; it does not assert an exceptional closed base-change isomorphism for an arbitrary square. We obtain

\[
 A_{\{v=0,\eta_u=0\}}
 \longrightarrow
 \omega_{\mathbb R^{b*}}\otimes
 \omega_{\mathbb R^{c*}}=E_Y.
 \qquad\text{(21)}
\]

The map (21) is the tangent zero-point unit followed by the actual \(v=0\) normal trace. By the same description (18) for \(j:W\hookrightarrow Y\), it is exactly \(j_*[T_W^*W]\). Its source is identified by the proper homeomorphism (17), so the equality retains the full conormal support.

The common normal block has dimension \(c\), and the relative fibre shift is

\[
 n-m=(a+c)-(b+c)=a-b.
 \qquad\text{(22)}
\]

The common normal factors cancel in their original order. The only tensor exchanges needed to identify the graph map have already been accounted for in (8)–(11). Thus no extra codimension or dimension-parity sign is inserted in (21). All maps used are the natural inverse-image, tensor, trace and dual-frame maps. On overlaps, a reversal of a normal frame reverses both its Thom orientation and its dual coefficient, and their pairing is unchanged. The locally equal supported morphisms therefore glue. This proves (3). \(\square\)

## Exercises with complete solutions

### A transverse map with changing tangential rank

*Difficulty: Advanced.*

Let \(f:\mathbb R^3_{u_1,u_2,v}\to\mathbb R^2_{t,z}\) be \(f(u_1,u_2,v)=(u_1^2+u_2^3,v)\), and let \(Z=\{z=0\}\). Check transversality, compute the cotangent carrier and its normalized cycle, and check the relative shifts at the origin.

**Solution.** The normal coordinate is \(z\circ f=v\), whose derivative is surjective at every point. Thus \(W=\{v=0\}\) is transverse of codimension one. The tangent derivative of \(g=u_1^2+u_2^3\) is \((2u_1,3u_2^2)\), which has rank zero at \(u_1=u_2=0\) and rank one elsewhere. The ambient derivative correspondingly has rank one or two, so a submersion assumption would exclude the origin.

For an input covector \(\tau\,dt+\zeta\,dz\),
\[
 f_d(u_1,u_2,v;\tau,\zeta)
 =(u_1,u_2,v;2u_1\tau,3u_2^2\tau,\zeta).
 \qquad\text{(23)}
\]
On the pulled conormal, \(v=0,\tau=0\), and \(\zeta\) is arbitrary. The image is exactly \(T_W^*\mathbb R^3\), with the carrier map a proper homeomorphism. The relative point-unit trace treats the tangent map \(\mathbb R^*\to\mathbb R^{2*}\) at every rank, including zero. Hence the output is the normalized conormal with coefficient \(1\), rather than merely some multiple of that carrier. Here \(m-n=1\); the graph relative line has shift \([1]\) and the fibre relative dualizing line has shift \([-1]\). In particular the exceptional fibre trace, rather than ordinary coefficient restriction, supplies the dimension change at the origin.

### Three transverse roots have three positive point units

*Difficulty: Intermediate.*

Over \(A=\mathbb Z\), compare pullback of the normalized point conormal at zero by \(q(t)=t^2\) and by \(h(t)=t^3-t\). For \(h\), intersect the result with any continuous section of \(T^*\mathbb R\), and explain why the derivative signs do not give a signed degree.

**Solution.** For \(q\), the only inverse point is zero and \(q'(0)=0\). Transversality fails. Its incidence over that point has arbitrary \(\xi\), all sent to the single zero covector by \(q_d(0;\xi)=(0;0)\). This noncompact fibre violates properness, so this inverse cycle operation is undefined.

For \(h\), the roots are \(-1,0,1\), with derivatives \(2,-1,2\). Each is nonzero, so the map is transverse to the point. On each incidence fibre, \(\xi\mapsto h'(t)\xi\) is a homeomorphism onto that root's full cotangent fibre. Their finite union is proper. The theorem gives
\[
 h^*[T_{\{0\}}^*\mathbb R]
 =\sum_{t\in\{-1,0,1\}}[T_{\{t\}}^*\mathbb R].
 \qquad\text{(24)}
\]
Every coefficient is the normalized unit \(+1\). At the negative branch the normal Thom orientation and the dual cotangent coefficient both reverse; the actual trace normalization retains their pairing. There is no leftover derivative sign. A continuous section meets each full fibre once. The normalized point calculation in the preceding lesson gives local intersection number \(1\) at each point, so the compact total is \(3\in\mathbb Z\). A signed degree calculation would give \(1\); it is a different operation from this twisted conormal pullback and intersection.

### A reversed normal coordinate and a nontransverse line

*Difficulty: Intermediate.*

Let \(f:\mathbb R_u\to\mathbb R^2_{x,z}\) be \(f(u)=(-u,0)\). Compare the normalized inverse image of the vertical line \(Z=\{x=0\}\) with the properness test for the horizontal line \(Z'=\{z=0\}\).

**Solution.** For \(Z\), the normal coordinate pulls back to \(-u\), with derivative \(-1\), so \(W=\{0\}\) is transverse. The input conormal has \(x=0,\zeta=0\), with arbitrary \(\xi\,dx\). Its pulled carrier has \(u=0,\zeta=0\), and \(f_d(0;\xi,0)=(0;-\xi)\). This is a proper homeomorphism onto the full cotangent fibre at zero. The theorem gives the normalized point conormal with coefficient \(1\). Choosing \(v=-u\) puts the proof in its normal-identity chart. Returning to \(u\) reverses both the normal Thom orientation and the dual-frame coefficient; their trace pairing stays \(1\). Keeping just the coordinate determinant would give a wrong negative weight.

For \(Z'\), the conormal consists of arbitrary \(x\) and \(\zeta\,dz\). Its pulled carrier has arbitrary \(u,\zeta\), while \(f_d(u;0,\zeta)=(u;0)\). Each fixed \(u\) has a noncompact covector fibre. Thus inverse-image properness fails, just as transversality fails: the normal \(dz\) is killed by \(df^t\). The set image is a zero section, but that set calculation defines no inverse cycle.

### A codimension-two inverse image changes cycle dimension

*Difficulty: Advanced.*

Take \(f:\mathbb R^3_{u,v,w}\to\mathbb R^2_{z_1,z_2}\), \(f(u,v,w)=(v,w)\), and \(Z=\{0\}\). Compute the normalized output and check the coefficient degrees along the full incidence map.

**Solution.** The normal derivative onto \((z_1,z_2)\) is surjective, so \(W=\{v=w=0\}\) is the \(u\)-line, of codimension two. The pulled carrier has \(v=w=0\), arbitrary \(u\) and arbitrary \((\xi_1,\xi_2)\). Its image is
\[
 (u,0,0;0,\xi_1,\xi_2)\in T_W^*\mathbb R^3,
 \qquad\text{(25)}
\]
and the map is a proper homeomorphism. The output is the normalized conormal of that line. Its carrier has dimension three, while the input full point conormal has dimension two. Cotangent inverse image changes the Lagrangian cycle dimension to the dimension of the new base.

The full \(f_d:C_f\to T^*\mathbb R^3\) is the codimension-one embedding \((u,v,w;\xi_1,\xi_2)\mapsto(u,v,w;0,\xi_1,\xi_2)\). The target coefficient \(E_Y\) is in degree \(-3\). Its exceptional inverse image has the normal costalk shift \([-1]\), hence degree \(-2\), agreeing with \(Q=f_\pi^{-1}E_X\). The graph line has shift \(m-n=1\) and its inverse fibre line shift \(-1\). Ordinary restriction would keep degree \(-3\) and would not give the required coefficient map.

### Codimension zero permits every analytic map

*Difficulty: Intermediate.*

Set \(Z=X\). Apply the theorem to a constant map from a positive-dimensional \(Y\), and compare it with inverse image of a point conormal in a positive-dimensional \(X\).

**Solution.** The transversality condition is automatic because \(T_xZ=T_xX\). The inverse submanifold is \(W=Y\). The pulled zero carrier in \(C_f\) is precisely \(\xi=0\), and \(f_d\) identifies it with the target zero section, even for a constant map. This restriction is proper, and the point-unit counit calculation (14) gives \(f^*[T_X^*X]=[T_Y^*Y]\). The full cotangent map for the constant map can have noncompact fibres; only the zero carrier is used here. Neither properness of the base map nor any positive derivative rank is needed.

If instead \(Z=\{x\}\) and the constant value is \(x\) in an \(n>0\) dimensional \(X\), the pulled point conormal contains all \(\xi\in T_x^*X\). Every one is killed by \(df^t=0\), so a whole noncompact \(n\)-space lies over each target zero covector. Properness fails. If the constant value lies outside the point, the pulled carrier is empty and the output is zero. The permitted zero-section pullback therefore supplies no permission to pull back an arbitrary conormal through the same constant map.

### A large noncompact kernel disappears on the actual support

*Difficulty: Advanced.*

Let \(f:\mathbb R_u\to\mathbb R^3_{x,y,z}\), \(f(u)=(u,0,0)\), and let \(Z=\{x=0\}\). Verify (3) and explain the tangent point-unit trace when the target conormal's base has dimension two.

**Solution.** The normal coordinate \(x\circ f=u\) has derivative \(1\), so \(W=\{0\}\) is transverse. The conormal of the \(yz\)-plane has \(x=0\), tangent covectors \(\eta=\zeta=0\), and arbitrary normal \(\xi\,dx\). Thus the pulled carrier is \(u=0,\eta=\zeta=0\). The map
\[
 f_d(u;\xi,\eta,\zeta)=(u;\xi)
 \qquad\text{(26)}
\]
is a proper homeomorphism on that carrier onto the point conormal in \(T^*\mathbb R\). The theorem identifies its coefficient with the normalized point unit \(1\).

The full map (26) forgets \((\eta,\zeta)\in\mathbb R^{2*}\), so it is nonproper. In the proof, the tangent map from \(W\) to the plane \(Z\) sends its two tangent covectors to the rank-zero cotangent space of a point. We apply its trace to the unit supported at \((\eta,\zeta)=0\). That support maps properly to the point, and the point-embedding counit followed by the collapse counit is the identity point counit. We have not integrated a cycle carried by the whole noncompact two-dimensional tangent-covector space. Here \(m-n=-2\), the graph line has shift \([-2]\), and the fibre relative line has shift \([2]\). Those shifts are part of the actual relative trace, which the point-supported composition handles without an additional scalar or sign.
