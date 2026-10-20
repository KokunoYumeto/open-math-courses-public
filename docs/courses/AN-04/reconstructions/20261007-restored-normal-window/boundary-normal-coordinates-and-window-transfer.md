# Boundary normal coordinates and quadratic window transfer

A normal form is useful only if its coordinates preserve the regularity that the analytic estimate measures. A time-dependent change of spatial coordinates can remove the normal cross term, while introducing a tangential mixed time term. We retain that term and transport the wavefront itself. This connects the glancing estimate to the geometric normal form without applying the estimate to a different differential operator.

The chapter proves the exact transfer for the entire smooth single-face coefficient class of [The compensated glancing estimate](../20261007-restored-compensated-glancing/compensated-glancing-positive-commutator.md) and [Smooth glancing regularity in parabolic windows](../20261007-restored-smooth-glancing/smooth-glancing-neighborhoods-and-windows.md). The cross block is required to vanish at the boundary; it need not vanish inside the collar. The resulting geometric quadratic-window criterion is the input RW4 of [Parabolic wavefront windows and singular rays](../20261007-restored-parabolic-windows/parabolic-wavefront-windows-and-rays.md). Its use in the full trajectory theorem still requires the matching propagation statements on the non-glancing pieces.

The complete current [global boundary calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md), Sections 1–2, supplies the coordinate law, full operator-class invariance and actual symbol realization. Its source and rights records are retained. The generic smooth flow with parameters is proved in Section 1 of [Energy and existence with a timelike Dirichlet boundary](../20261007-restored-mixed-dirichlet/mixed-dirichlet-cauchy-energy-preparation.md). The same-norm wavefront definition and its closure rule are proved in Sections 1–2 of the smooth-glancing chapter. These are actual programme proof providers.

The proof map binds each result to its exact earlier proof, including the [weak-H1 domain identification](../20261007-restored-boundary-form/boundary-form-localization.md), Sobolev coordinate maps, and [elementary differential, determinant and substitution proofs](../20261004-free-stationary-phase/proof-map.html). These current connections retain the Hörmander-based boundary calculus.

The freely readable [Melrose–Sjöstrand seminar paper](https://www.numdam.org/item/SEDP_1977-1978____A16_0/) begins with the quadratic boundary normal form and compressed wavefront, printed pages XV.1–XV.2. [Vasy's wave propagation paper](https://math.stanford.edu/~andras/psmcrrb.pdf), printed pages 3–5, retains the compressed projection and the boundary cross block condition. Those are credited primary routes. The full quantitative coordinate and regularity transfer below is receiving programme text; neither paper's expression or images are reproduced.

## 1. Construct a collar while fixing the boundary

Work on a relatively compact smooth collar with coordinates \((x,t,y)\), \(x\ge0\), \(y\in\mathbb R^d\). For \(\mathbb C^N\)-valued solutions the principal symbol is the following scalar symbol times the identity:
\[
 p(x,t,y;\xi,\tau,\zeta)
 =\tau^2-a\xi^2-2\xi b^T\zeta-\zeta^TC\zeta,
 \qquad
 G=\begin{pmatrix}a&b^T\\b&C\end{pmatrix}\ge\kappa I,
 \quad b(0,t,y)=0,\quad \kappa>0 .
 \tag{NC1}
\]
All coefficients are smooth and real here; the lower-order coefficient matrices may be arbitrary complex matrices. The analytic estimate uses its recorded bounded extensions and either weak form domain \(V=H^1_0\) or \(V=H^1\). Every assertion in this chapter is local on compact patches. Put \(c=b/a\); the denominator is at least \(\kappa\).

Solve the parameter-dependent ordinary differential equation
\[
 \partial_xY(x,t,v)=c(x,t,Y(x,t,v)),
 \qquad Y(0,t,v)=v,\qquad
 F(x,t,v)=(x,t,Y(x,t,v)).
 \tag{NC2}
\]
The complete smooth-field proof in the cited energy chapter applies with \(x\) as its evolution variable and \((t,v)\) as parameters. Its bounded-box contraction supplies one common interval, uniqueness and every parameter derivative. In particular the derivative \(M=Y_v\) satisfies the actual linear equation
\[
 M_x=c_y(x,t,Y)M,\qquad M(0,t,v)=I,
 \qquad
 J=\det M=\exp\!\left(\int_0^x\operatorname{tr}c_y(s,t,Y(s,t,v))\,ds\right)>0 .
 \tag{NC3}
\]
For completeness, the determinant formula follows by differentiating the determinant while \(M\) is invertible. The scalar exponential never vanishes, so the initial interval of invertibility extends across the chosen common flow interval. The inverse is obtained by flowing the same equation back to \(x=0\). The map \(F\) is therefore a smooth local diffeomorphism, preserves \(x\) and \(t\) exactly, and fixes every boundary point.

**The parameter flow and determinant without an invertibility assumption.** Apply the proved smooth autonomous flow theorem to the enlarged field \((1,0,c(x,t,y))\). Starting at \((0,t,v)\) gives exactly (NC2); the constant \(t\) and initial \(v\) are parameters in that theorem. Its variational equation gives \(M_x=AM\), \(A=c_y(x,t,Y)\). The same finite-dimensional smooth ODE theorem solves \(N_x=-NA\), \(N(0)=I\). Differentiating \(NM\) gives zero, hence \(NM=I\) on the common interval. A square matrix with a left inverse is invertible, by the determinant multiplication and cofactor formula, so \(N=M^{-1}\) throughout. Differentiating the determinant polynomial column by column yields \((\det M)'=(\det M)\operatorname{tr}(M^{-1}M_x)\): for the determinant of \(I+hB\), the only linear permutation terms are the diagonal \(hB_{ii}\), and multiplication reduces the general case to this one. The cyclic trace identity follows by interchanging the two finite indices. Thus \(J_x=(\operatorname{tr}A)J\). Multiplying by the reciprocal scalar exponential proves (NC3), with \(e^{-C|x|}\le J\le e^{C|x|}\) on compact parameter patches. The zero-dimensional tangential case has the empty determinant \(J=1\) and the identity map. The opposite flow in the enlarged variables gives the smooth inverse from any small \(x\) back to zero.

The boundary condition on \(b\) gives \(Y_x(0,t,v)=0\). Taylor's integral formula, including all parameters, gives
\[
 Y=v+x^2Z,\qquad
 Z(x,t,v)=\int_0^1(1-s)Y_{xx}(sx,t,v)\,ds,
 \quad Y_t=x^2Z_t,\quad M=I+x^2Z_v,\quad J=1+x^2j .
 \tag{NC4}
\]
Here \(Z,j\) are smooth on the compact collar. Their derivatives of any fixed finite order are bounded after shrinking the patch. The formula for \(j\) follows by expanding the finite determinant polynomial of \(I+x^2Z_v\). Thus the map fixes both the boundary tangential coordinates and their first normal jets. The statement is stronger than mere boundary identity and will control the window transfer.

## 2. Retain the full cotangent transformation

Let \((\rho,\vartheta,\eta)\) be the covector coordinates conjugate to \((x,t,v)\). Pulling back the entire canonical one-form gives
\[
 \begin{aligned}
 \rho&=\xi+c^T\zeta,&
 \vartheta&=\tau+Y_t^T\zeta,&
 \eta&=M^T\zeta,\\
 \zeta&=M^{-T}\eta,&
 \tau&=\vartheta-Y_t^TM^{-T}\eta,&
 \xi&=\rho-c^TM^{-T}\eta .
 \end{aligned}
 \tag{NC5}
\]
The coefficient \(c\) in these formulas is evaluated at \((x,t,Y)\). Indeed \(dY=c\,dx+Y_t\,dt+M\,dv\), and substitution into \(\xi\,dx+\tau\,dt+\zeta^Tdy\) gives \(\rho\,dx+\vartheta\,dt+\eta^Tdv\). Exterior differentiation proves that this full cotangent map is symplectic. Omitting the \(Y_t\) term would fail the one-form identity whenever \(c\) depends on time.

Complete the square before substituting the covectors. Write
\[
 S=C-\frac{bb^T}{a},\qquad
 \zeta^TS\zeta
 =\min_\xi\bigl(a\xi^2+2\xi b^T\zeta+\zeta^TC\zeta\bigr)
 \ge\kappa|\zeta|^2 .
 \tag{NC6}
\]
The minimum occurs at \(\xi=-b^T\zeta/a\), so the equality and the bound follow directly from (NC1). Denote evaluation at \(F\) by a subscript \(F\). Then the exact transformed symbol is
\[
 p_F=-a_Fp_0,\qquad p_0=\rho^2-R,\qquad
 R=\frac{(\vartheta-Y_t^TM^{-T}\eta)^2
               -\eta^TM^{-1}S_FM^{-T}\eta}{a_F}.
 \tag{NC7}
\]
This is a real smooth quadratic symbol in the tangential covector, independent of \(\rho\). Its tangential form has one positive and \(d\) negative directions: the invertible shear \((\vartheta,\eta)\mapsto(\vartheta-Y_t^TM^{-T}\eta,M^{-T}\eta)\) reduces it to the form in (NC6). A mixed time/tangential term remains inside \(R\).

The same symbols at the boundary satisfy
\[
 R_0(t,v;\vartheta,\eta)
 =\frac{\vartheta^2-\eta^TC(0,t,v)\eta}{a(0,t,v)}
 =\frac{p_b}{a_b},
 \qquad
 R=\frac{\vartheta^2-\eta^TC(x,t,v)\eta}{a(x,t,v)}
          +x^2R_2(x,t,v;\vartheta,\eta).
 \tag{NC8}
\]
The function \(R_2\) is smooth and quadratic in the covector. To verify the second identity, (NC4) gives \(M^{-1}-I=x^2\widetilde M\) and \(Y_t=x^2Z_t\). Smooth coefficient evaluation at \(Y=v+x^2Z\) differs from evaluation at \(v\) by \(x^2\) times its integrated \(y\)-derivative. Finally \(bb^T/a=x^2\widetilde S\) by Hadamard's formula for \(b(0,t,y)=0\). Each substituted term in (NC7) has the claimed factor, with no loss of time derivatives. In particular \(R_x|_{x=0}\) equals the first normal derivative of the displayed reference form.

On the characteristic set multiplication by \(-a_F\) gives
\[
 H_{p_F}=-a_FH_{p_0}\quad(p_0=0),\qquad
 H_{p_0}=2\rho\,\partial_x+R_x\,\partial_\rho-H_R^{\,t,v,\vartheta,\eta}.
 \tag{NC9}
\]
The term \(-p_0H_{a_F}\) vanishes there. The cotangent map intertwines the original and transformed Hamilton fields because it preserves the symplectic form. Thus the parameter reverses orientation under the negative multiplier; both directions are retained. At glancing the reduced gliding field for \(p_0\) is exactly \(-H_{R_0}\), with the contact signs and possible higher contact described in the generalized-flow chapter.

**Hamilton covariance and the geometric entry conditions.** Let \(\chi\) be the full cotangent map from new to old coordinates. The one-form computation proves \(\chi^*\omega=\omega\). Contract this identity with \(D\chi^{-1}(H_p\circ\chi)\); the defining Hamilton contraction and the chain rule give the differential of \(p\circ\chi\), with the same sign convention on both sides. Nondegeneracy of \(\omega\) therefore gives \(D\chi(H_{p_F})=H_p\circ\chi\). Also \(H_{fp_0}=fH_{p_0}+p_0H_f\), by the product rule in the defining contraction, proving the exact restriction in (NC9).

The normal-form geometry applies on the stated fixed-sign patch: \(\partial_\vartheta R_0=2\vartheta/a_b\ne0\). Consequently \(dR_0\) has a nonzero fiber component and is independent of the canonical tangential one-form, which has only base components. In particular the gliding field is nonzero there. The conormal covectors have \((\vartheta,\eta)=0\), and \(p_0=\rho^2\ne0\) for their nonzero members, proving noncharacteristicity of the boundary. Near the characteristic glancing patch, \(\partial_\vartheta p_0=-2\tau/a_F\ne0\); the nonvanishing of \(\tau\) is preserved on a smaller compact patch and is quantified in (NC18). Thus the actual principal-type and canonical-form hypotheses of the earlier geometric chapter hold.

## 3. Transport compressed covectors and regularity

Write the old compressed normal covector as \(\sigma=x\xi\) and the new one as \(\widehat\sigma=x\rho\). Formula (NC5) has the smooth extension to the whole compressed bundle
\[
 \widehat\sigma=\sigma+xc^T\zeta,\qquad
 \vartheta=\tau+Y_t^T\zeta,\qquad \eta=M^T\zeta,
 \qquad
 \sigma=\widehat\sigma-xc^TM^{-T}\eta .
 \tag{NC10}
\]
The other inverse formulas are those in (NC5). This is the full compressed coordinate map, not just its restriction to characteristic covectors. It and its inverse are smooth up to \(x=0\), and homogeneous of degree one in all covectors. They fix the embedded boundary tangential bundle \(\{x=\sigma=0\}\) pointwise. The ordinary compression and the full cotangent map commute with it.

Let \(T u=u\circ F\). On compactly supported local patches the ordinary chain rule and change of variables show that \(T\) and \(T^{-1}\) are bounded inverse maps on \(H^1\). Specifically \(dx\,dt\,dy=J\,dx\,dt\,dv\), \(J\) is bounded above and away from zero, and the differentials of \(F,F^{-1}\) are bounded. Approximation by smooth functions gives the same conclusion for weak derivatives. Since \(F\) preserves the boundary, pullback of a compactly supported smooth function in the interior is again such a function; taking its closure proves the assertion for \(H^1_0\). Write \(\widehat V\) for the corresponding domain in the new chart. Its natural dual map is
\[
 \mathcal T f(w)=f(T^{-1}w),\qquad
 \|\mathcal T f\|_{\widehat V^*}\le C\|f\|_{V^*},
 \qquad \mathcal T f=J\,T f
 \quad\hbox{for locally integrable source coefficients}.
 \tag{NC11}
\]
The functionals are antilinear on their arguments. The last identity is precisely the change-of-variables formula in their pairing; distributional extension retains it. It does not replace the natural dual by a chosen negative interior Sobolev norm.

**The weak-H1 maps and their actual limits.** On smooth compact inputs the chain rule is a finite sum with coefficients bounded by \(DF\), and compact substitution bounds the squared L2 integrals using \(J^{-1}\). The same argument for \(F^{-1}\) uses its bounded differential and \(J\). Thus both H1 norm inequalities have one finite constant on the fixed compact patches. Approximate an \(H^1\) input by smooth functions up to the boundary, using the earlier restricted-H1 density proof. The pullbacks and all their first derivatives are Cauchy in L2. Pairing their limits with an interior compact test and passing through the weak derivative identity proves that the derivative limits are the weak derivatives of the value limit. This limit is the distributional pullback: the smooth substitution formula against each test has the same limit, and the inverse map recovers the original input. Interior tests identify these L2 functions uniquely. For \(H^1_0\), choose the approximating sequence inside the interior; its pullbacks stay there, so the closed zero-trace space is preserved in both directions. A finite base partition handles the localized patches. The natural dual is then transported by its definition on the entire form domain, as in (NC11), including boundary-nonzero tests. No restriction to interior tests is made for that dual assertion.

Let \(\mathfrak f\) denote the compressed map from the old chart to the new chart, including the inverse base coordinates. The complete current global boundary calculus, Section 2.1, proves that
\[
 B=TAT^{-1}\in\Psi_b^k,\qquad
 C=\mathcal T A\mathcal T^{-1}
       =J\,TAT^{-1}J^{-1}\in\Psi_b^k,\qquad
 \sigma_k(B)=\sigma_k(C)=\sigma_k(A)\circ\mathfrak f^{-1}.
 \tag{NC12}
\]
Its full amplitude and determinant transformation gives every lower order remainder, as well as the leading symbol. Smooth nonvanishing multipliers \(J,J^{-1}\) preserve the class and their leading factors cancel. Thus this statement uses the entire operator-class invariance, rather than treating the principal symbol as the entire conjugated operator.

For a natural-dual source this conjugation also retains the actual dual action. Lebesgue adjoints satisfy \(T^*=T^{-1}J^{-1}\), \((T^{-1})^*=JT\), and hence \(C^*=TA^*T^{-1}\). Therefore
\[
 (C\mathcal T f)(w)
   =(\mathcal T f)(C^*w)
   =f(A^*T^{-1}w)
   =(\mathcal T(Af))(w).
 \tag{NC13}
\]
All identities hold first on smooth compact tests and then on the indicated domains by their bounded maps. This is why the Jacobian belongs in the natural-dual transport.

Use the exact finite-order definition from the preceding smooth-glancing chapter: regularity of order \(k\) means one elliptic tester of order \(k\) with its value in the same space \(V\), or respectively \(V^*\). Equations (NC11)–(NC13), and their inverses, give
\[
 \operatorname{WF}_b^{\widehat V,k}(Tu)
       =\mathfrak f(\operatorname{WF}_b^{V,k}(u)),\qquad
 \operatorname{WF}_b^{\widehat V^*,k}(\mathcal T f)
       =\mathfrak f(\operatorname{WF}_b^{V^*,k}(f)).
 \tag{NC14}
\]
The same-norm smooth front is the closure of the union of its finite integer-order fronts, as proved in (CG3). Since \(\mathfrak f\) is a homeomorphism, it commutes with that union and closure. It follows that both equalities in (NC14) also hold for the smooth front. This retains one common microlocal smooth neighborhood; regularity at each order on shrinking neighborhoods would not suffice.

## 4. Transport the entire weak equation

This section checks that coefficient and boundary information survives the coordinate change, even though the analytic estimate has already been made in the original chart. Use old coordinates \(z^a\), new coordinates \(w^\alpha\), let \(L^a_{\alpha}=\partial_\alpha F^a\) and \(K=L^{-1}\). Retain the full weak form, with the \(L^2\) pairing linear in its first argument,
\[
 q(u,w)=\sum_{a,b}(g^{ab}D_bu,D_aw)
       +\sum_b(\ell^bD_bu,w)
       +\sum_a(m^au,D_aw)+(d u,w),\qquad
 q(u,w)=f(w)\quad(w\in V).
 \tag{NC15}
\]
The principal matrices are the scalar real wave coefficients times \(I_N\); \(\ell,m,d\) are arbitrary complex matrices. Pulling back each derivative gives \((D_a u)\circ F=\sum_\alpha K^\alpha_aD'_\alpha Tu\). Change variables in each of the four sums. The exact transformed coefficients are
\[
 \begin{aligned}
 \widehat g^{\alpha\beta}
   &=J\sum_{a,b}K^\alpha_a(g^{ab}\circ F)K^\beta_b,\\
 \widehat\ell^\beta&=J\sum_b(\ell^b\circ F)K^\beta_b,\qquad
 \widehat m^\alpha=J\sum_aK^\alpha_a(m^a\circ F),\qquad
 \widehat d=J(d\circ F),\\
 \widehat q(Tu,w)&=q(u,T^{-1}w)=\mathcal T f(w)
                         \quad(w\in\widehat V).
 \end{aligned}
 \tag{NC16}
\]
The entries of \(K\) and \(J\) are real scalars, so these formulas do not transpose, conjugate or commute any lower matrix with another matrix. The density is explicit; no derivative of \(J\) appears in the weak form itself. Differentiating coefficients to write a strong differential expression produces lower terms and retains them.

The strong principal symbol corresponding to \(\widehat q\), in Lebesgue coordinates, is \(Jp_F=-Ja_Fp_0\). Multiplication of that weak equation by \(\lambda=(-Ja_F)^{-1}\) is defined exactly by
\[
 q_0(U,w)=\widehat q(U,\lambda w),\qquad
 f_0(w)=\mathcal T f(\lambda w),\qquad
 D'_\alpha(\lambda w)=\lambda D'_\alpha w+(D'_\alpha\lambda)w .
 \tag{NC17}
\]
Here \(\lambda\) is real, smooth and nonzero. The last term contributes the actual additional first-order coefficient to \(q_0\); it is not discarded. The principal symbol is \(p_0\), and the domain remains \(\widehat V\), since smooth scalar multiplication preserves either domain. Smooth wavefronts of the source are unchanged by this elliptic multiplication. For the \(H^1\) domain all tests in (NC16) and (NC17), including tests with nonzero boundary trace, are retained. This transports the weak Neumann equation and its possible boundary functional. Imposing an unrelated strong condition \(D_xU=0\) would not express the transported problem.

The tangential mixed time terms inside (NC7) show that the transformed equation need not satisfy the original analytic form (NC1). The proof below instead transports the already-proved analytic conclusion by (NC14).

## 5. Transfer the analytic quadratic window

Fix a compact set of glancing anchors in an open normalized phase region away from the smooth natural-dual forcing front. Work on one sign of \(\tau\). Spatial positivity on ordinary characteristic covectors gives
\[
 |\xi|^2+|\zeta|^2\le\kappa^{-1}\tau^2,\qquad
 \left|\frac{\vartheta}{\tau}-1\right|
       \le Cx^2,\qquad
 \frac12|\tau|\le|\vartheta|\le\frac32|\tau|
 \quad(0\le x<x_*).
 \tag{NC18}
\]
The first estimate follows from \(p=0\) and (NC1); the second uses (NC4) and (NC5). Choose the compact collar so that \(Cx_*^2\le1/2\). This proves nonvanishing and sign agreement of the two time covectors on all nearby characteristic lifts, with fixed uniform constants.

Let \(z=(t,y,\zeta/\tau)\) and \(\widehat z=(t,v,\eta/\vartheta)\), with the fixed covector sign retained in both positive-cosphere charts. Formula (NC4), its inverse and (NC18) give on the characteristic set
\[
 |\widehat z-z|\le C_{\rm coord}x^2,\qquad
 \left|\frac{\widehat\sigma}{|\vartheta|}
               -\frac{\sigma}{|\tau|}\right|\le C_{\rm coord}x^2 .
 \tag{NC19}
\]
For the tangential ratio, write \(M^T\zeta/\vartheta-\zeta/\tau\) as \((M^T-I)\zeta/\vartheta+\zeta(\tau-\vartheta)/(\tau\vartheta)\). Each term is \(O(x^2)\) by the uniform characteristic ratio bound. The base difference is \(v-y=O(x^2)\). For the compressed normal component, \(xc=O(x^2)\) and \(|\sigma/\tau|\le x/\sqrt\kappa\); substitution into (NC10) proves the bound. These are exact estimates on a compact phase patch, with constants independent of a chosen ray.

Let \(V_b\) be the normalized, radially projected boundary field \(|\tau|^{-1}H_{p_b}\), and let \(\Phi_h\) be its local flow, as in the preceding chapter. The corresponding normalized geometric field for (NC7) is the radially projected \(-|\vartheta|^{-1}H_{R_0}\), with flow \(\psi_s\). At every glancing anchor,
\[
 \widehat W(q)=-a_b(q)^{-1}V_b(q).
 \tag{NC20}
\]
Indeed \(H_{p_b/a_b}=a_b^{-1}H_{p_b}+p_bH_{a_b^{-1}}\), and \(p_b=0\) at the anchor. The boundary coordinate maps and covectors there are identities. The same radial projection therefore gives (NC20). The two fields need not coincide off the glancing set.

Put \(D(q)=a_b(q)^{-1}\), \(D_+=\sup_KD\), and choose the analytic step \(h=-D(q)s\). Taylor's integral bound for both smooth flows gives
\[
 |\Phi_{-D(q)s}(q)-\psi_s(q)|\le C_{\rm center}s^2 .
 \tag{NC21}
\]
One may take \(C_{\rm center}=(A_VM_VD_+^2+A_WM_W)/2\), using bounds \(M\) for the field and \(A\) for its derivative on the slightly larger compact patch. The first jets cancel by (NC20). Holding the anchor fixed when choosing the step is essential; no equality of whole flow parametrizations is asserted. The negative sign is allowed because the analytic criterion has been proved in both directions.

Now suppose that an anchor belongs to the smooth \(V\)-based solution front. The parabolic criterion (CG34), proved for the entire class (NC1), gives a constant \(L_0\) uniform on the compact anchor set such that for every sufficiently small nonzero \(h\) there exists a characteristic compressed front point \(q_h\) with
\[
 x(q_h)\le L_0h^2,\qquad
 |z(q_h)-\Phi_h(q)|\le L_0h^2 .
 \tag{NC22}
\]
This is its contrapositive with width \(\eta=L_0|h|\), chosen below one. Select any ordinary characteristic lift of \(q_h\). Such lifts exist by the noncharacteristic containment proved in the same chapter. On interior points the lift is unique; on hyperbolic boundary points either of the two roots suffices. Transport that lift by (NC5). The compressed new point lies in the new smooth front by (NC14), and its characteristic equation is \(p_0=0\) by (NC7).

Equations (NC19), (NC21) and (NC22), at \(h=-D(q)s\), give
\[
 \begin{split}
 x(q_h)&\le L_0D_+^2s^2,\\
 |\widehat z(q_h)-\psi_s(q)|
   &\le\bigl(L_0D_+^2+C_{\rm center}\bigr)s^2
             +C_{\rm coord}L_0^2D_+^4s^4
    \le L_{\rm geom}s^2\qquad(|s|\le1),
 \end{split}
 \tag{NC23}
\]
where \(L_{\rm geom}\) is any fixed number at least the two displayed quadratic coefficients after absorbing the fourth-order term. All steps are uniform on the compact set. There is no requirement that the selected lift or witness vary continuously with \(s\).

Define the ordinary lifted set
\[
 \mathcal F=\operatorname{Char}(p_0)
       \cap\widehat\pi^{-1}
          \bigl(\operatorname{WF}_b^{\widehat V,\infty}(Tu)\bigr)
 \quad\hbox{away from the transported forcing front}.
 \tag{NC24}
\]
It is relatively closed in that source-free characteristic region: the compressed projection is continuous and the smooth front is closed. The normalized characteristic lifts near the compact anchors are bounded by (NC18), (NC5) and their inverses. Thus these lifted points remain in the fixed slightly larger compact phase region. At glancing the lift has \(\rho=0\).

Consequently, for every compact set \(K\subset\mathcal F\cap G\), there are \(C_K>0,s_K>0\) such that, for both signs of \(s\),
\[
 \begin{gathered}
 q\in K,\quad0<|s|<s_K,\quad C_K|s|\le\epsilon<1,\\
 \{q'\in\operatorname{Char}(p_0):
    0\le x(q')\le\epsilon|s|,\
    |\widehat z(q')-\psi_s(\widehat z(q))|\le\epsilon|s|\}
        \cap\mathcal F=\varnothing
 \quad\Longrightarrow\quad q\notin\mathcal F .
 \end{gathered}
 \tag{NC25}
\]
Take \(C_K\ge L_{\rm geom}\) and shrink \(s_K\) to satisfy the common flow, chart and analytic-step bounds. If a marked \(q\) belonged to \(\mathcal F\), the witness (NC23) would belong to every stated window, contradicting emptiness. This proves the implication with all its quantifiers. In particular it proves RW4 on \(G_g\cup G^3\), without the earlier extra assumption \(b\equiv0\) throughout the collar.

The coordinate and radial-normalization transfer in Section 3 of the parabolic-window chapter identifies this normalized formulation with its local characteristic formulation. Denote the normalized projected gliding field by \(\widehat H_{p_0}^G\), so that its reduced projection is \((0,\widehat W)\). Its complete window lemma now gives, uniformly on compact anchors,
\[
 x(q_s)\le Ls^2,\qquad
 |\widehat z(q_s)-\psi_s(q)|\le Ls^2,\qquad
 \left|\frac{Q(q_s)-Q(q)}s-Q(\widehat H_{p_0}^G(q))\right|
       \le(2L+C_{\rm flow})|s| ,
 \tag{NC26}
\]
in the chosen, consistently normalized coordinates and field. This supplies the glancing tangency hypothesis GF32 for this coefficient class. The normal lift estimate \(|\rho(q_s)|\le C|s|\) follows as in (RW9), since \(R=R_0+O(x)\), \(R_0(\psi_s(q))=0\), and all normalized derivatives are bounded. This step proves neither the separate singular-segment hypotheses nor propagation of singularity along every nonunique ray.

## 6. A time-dependent exact model

For one spatial tangential coordinate take
\[
 a=1,\quad b=xt,\quad C=1+x^2t^2,\qquad
 p=\tau^2-(\xi+xt\zeta)^2-\zeta^2 .
 \tag{NC27}
\]
The spatial matrix has determinant one and positive trace, hence is positive definite; on each compact collar its smallest eigenvalue has a positive lower bound. The exact flow and covector map are
\[
 Y=v+\tfrac12tx^2,\quad J=1,\quad
 \rho=\xi+xt\zeta,\quad
 \vartheta=\tau+\tfrac12x^2\zeta,\quad \eta=\zeta,\qquad
 R=(\vartheta-\tfrac12x^2\eta)^2-\eta^2 .
 \tag{NC28}
\]
The transformed equation therefore has a tangential mixed \(\vartheta\eta\) term with coefficient \(-x^2\). It vanishes at the boundary and still belongs in the complete symbol. The base displacement is exactly \(tx^2/2\), and the compressed normal displacement is exactly \(x^2t\zeta\). A witness at \(x=O(s^2)\) has these coordinate errors at \(O(s^4)\) on compact normalized phase patches.

![Boundary collar map for the exact model: at t=1 the v=0 and v=1 normal lines map to y=v+x^2/2. The displayed curves are exact quadratic graphs for 0<=x<=1. The cotangent and compressed maps retain the time shift vartheta=tau+x^2*zeta/2 and normal shift sigma_hat=sigma+x^2*zeta. Proof formulas NC5, NC10 and NC27--NC28; primary geometric credit: Melrose and Sjöstrand, seminar paper XV.1.](figures/boundary-normal-window-transfer.svg)

The figure is a section at \(t=1\), not a picture of all phase variables or a claim that the normal lines are characteristic rays. Its labels include the unpictured time-covector term.

## 7. Exercises with complete solutions

### Exercise 1: the missing time covector, intermediate

In the exact model (NC27), compute the pullback of the canonical one-form and verify the symbol identity. Determine the error obtained by using \(\vartheta=\tau\) instead.

**Solution.** Since \(dy=dv+tx\,dx+(x^2/2)\,dt\),
\[
 \xi\,dx+\tau\,dt+\zeta\,dy
   =(\xi+tx\zeta)\,dx+(\tau+x^2\zeta/2)\,dt+\zeta\,dv .
 \tag{NC29}
\]
Thus the map is exactly (NC28). Substituting \(\xi=\rho-tx\eta\), \(\tau=\vartheta-x^2\eta/2\) into (NC27) gives \(p_F=(\vartheta-x^2\eta/2)^2-\rho^2-\eta^2=-p_0\). The proposed incomplete map would leave the term \((x^2/2)\zeta\,dt\) in the one-form difference. With \(\tau=\vartheta\) its symbol would miss \(-x^2\vartheta\eta+x^4\eta^2/4\). It is not the cotangent transformation, and it cannot justify the transfer.

### Exercise 2: a natural-dual boundary source, advanced

Let \(f(w)=\int_{\partial X}h(t,y)\cdot\overline{\gamma w(t,y)}\,dt\,dy\), where \(h\) is smooth and compactly supported. Compute its transported functional for (NC2). Explain why (NC11) does not erase it even though it vanishes on all compact tests in the interior.

**Solution.** At \(x=0\), the base map is \((t,v)\mapsto(t,v)\), its tangential Jacobian is one, and \(\gamma T^{-1}w=\gamma w\). Directly from the functional definition,
\[
 \mathcal T f(w)=\int_{\partial X}
             h(t,v)\cdot\overline{\gamma w(t,v)}\,dt\,dv .
 \tag{NC30}
\]
For compactly supported smooth tests the fundamental theorem of calculus gives \(\|\gamma w\|_{L^2}^2\le2\|w\|_{L^2}\|\partial_xw\|_{L^2}\); approximation defines the bounded trace on the localized \(H^1\) domain. Thus this is a continuous natural-dual functional there. It remains nonzero when \(h\ne0\), by choosing a smooth test whose trace has nonzero pairing with \(h\). Its restriction to interior compact tests is zero, which shows why that restriction alone is not the full weak Neumann source. On \(H^1_0\) the same trace functional is zero, as it should be. Formula (NC13) retains its transformed operator action on all the actual domain tests.

### Exercise 3: uniform windows under a reversing clock, advanced

Suppose \(D_+\le2\), \(L_0=3\), \(C_{\rm center}=5\), \(C_{\rm coord}=7\). Find an explicit common \(L_{\rm geom}\) for \(|s|\le1/2\) in (NC23), state a permissible lower window width, and explain the two-direction requirement.

**Solution.** The normal coefficient is at most \(3\cdot2^2=12\). The tangential coefficient before the fourth-order term is at most \(12+5=17\). The fourth-order coefficient is \(7\cdot3^2\cdot2^4=1008\); for \(|s|\le1/2\) it contributes at most \(252s^2\). Hence
\[
 L_{\rm geom}=269,\qquad
 269|s|\le\epsilon<1,\qquad
 0<|s|<\min\{s_K,1/269,1/2\}
 \tag{NC31}
\]
are sufficient. The other local flow and analytic-step restrictions remain in \(s_K\). Since \(h=-D(q)s\), a positive geometric step uses a negative analytic step, and a negative geometric step uses a positive analytic step. An estimate for only one sign would prove only half the required criterion. The construction selects a witness separately for every nonzero step; no continuous choice is needed.

## 8. Scope, sources and authorship

The coordinate construction, full weak-form covariance, both natural-domain wavefront identities and the two-direction quantitative transfer are proved here. The normalized criterion RW4 is now established for the full smooth single-face class (NC1), including a nonzero collar cross block, time-dependent coefficients and arbitrary complex matrix lower terms. It remains a local source-free statement with uniform compact-anchor constants.

General scalar noncharacteristic symbols without the spatial positivity in (NC1), systems with non-scalar principal symbol, physical corners, complex phases and the full boundary propagation theorem require their own arguments. The boundary propagation theorem also requires the non-glancing singular-segment hypotheses of the closed-set trajectory theorem.

The primary human-source credit is Melrose and Sjöstrand for the boundary normal-form and compressed-geometric route, and Vasy for the compressed characteristic and energy-wavefront framework. The sources are cited for their mathematical contributions. Linked components retain their authorship and licence notices. The exposition, exercise solutions and diagram were written by GPT-6.1 Sol (OpenAI), Ultra; original eligible new expression is CC0-1.0. The stated arguments use the specific prerequisites identified in the proof index.


GPT-6 Astra (OpenAI) supplied the arguments making the parameter flow, determinant, weak-H1 limits and geometric entry conditions explicit. Every adopted result is proved here or in the earlier lesson identified in the proof map.  The independent exposition is CC0-1.0; existing linked components retain their terms. 
