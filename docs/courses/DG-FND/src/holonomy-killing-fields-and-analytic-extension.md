# Holonomy, Killing fields and analytic extension

We prove affine continuation and radial equivalence for connections, then construct the connection that transports Killing fields. Analytic curvature jets determine which initial pairs extend. Compactness gives stronger holonomy restrictions, and the Killing identity relates the remaining global fields to Ricci curvature.

All manifolds are finite dimensional, Hausdorff and second countable. A linear connection is a connection on the tangent bundle; it may have torsion. Analytic means represented locally by absolutely convergent real power series. We use
\[
T(Y,Z)=\nabla_YZ-\nabla_ZY-[Y,Z],\qquad
R(Y,Z)V=\nabla_Y\nabla_ZV-\nabla_Z\nabla_YV-\nabla_{[Y,Z]}V.
\]
The free monodromy account of Herrera, Javaloyes and Piccione motivates continuation by germs. The free notes of Wang and Liang explain curvature comparison in radial parallel frames. The arguments below include the existence and uniqueness steps used here, with exact earlier programme proofs at their points of use.

## A. Affine maps and continuation

For connections on \(M,N\), the covariant derivative of the differential of a smooth map \(f:M\to N\) is
\[
(\nabla df)(Y,Z)=\nabla^{f^*TN}_Y(df(Z))-df(\nabla_YZ).
\tag{A.1}
\]
Here the first connection is the pullback connection: in target coordinates it differentiates a vector along \(f\) and adds the target Christoffel term. A map is **affine** if (A.1) is zero. This definition places no restriction on its rank or on the two dimensions.

**Lemma A.1 (The affine equation, geodesics and one-jet uniqueness).** In coordinates the affine equation is
\[
\partial_i\partial_j f^\alpha
+\Gamma'{}^\alpha_{\beta\gamma}(f)
       \partial_i f^\beta\partial_j f^\gamma
-\Gamma^k_{ij}\partial_k f^\alpha=0.
\tag{A.2}
\]
It is tensorial in the two source arguments. Affine maps preserve parallel transport of tangent vectors and affinely parametrized geodesics. On a connected domain an affine map is determined by its value and differential at one point. If both connections are analytic, every smooth affine map is analytic.

**Proof.** [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) gives the coordinate expression for a connection and its transformation rule. Substitution in (A.1) gives (A.2). The derivative of a scalar multiplying \(Z\) appears once in each of its two terms and cancels; the connection is already linear over functions in \(Y\). This proves tensoriality, including for pullback vectors. The same coordinate expression defines that pullback connection under changes of target chart by the transformation rule.

Along a smooth curve \(\gamma\), expand an arbitrary vector field \(V\) in source coordinates. Equation (A.2) gives
\[
D'_t\bigl(df_{\gamma(t)}V(t)\bigr)
   =df_{\gamma(t)}D_tV(t).
\tag{A.3}
\]
For \(V\) parallel, the left side is zero; uniqueness of vector transport in [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) gives
\[
df_{\gamma(t)}P^\gamma_{0t}
     =P^{f\circ\gamma}_{0t}df_{\gamma(0)}.
\tag{A.4}
\]
With \(V=\dot\gamma\), (A.3) says that an affine image of a geodesic is a geodesic, including the constant case. [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) supplies uniqueness from its initial data. On a sufficiently small normal neighbourhood of \(p\), [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) therefore gives
\[
f(\exp_p v)=\exp_{f(p)}(df_pv).
\tag{A.5}
\]
Only existence on the small indicated time interval is used here.

If affine maps \(f,g\) on a connected domain have the same value and differential at \(p\), (A.5) makes them equal near \(p\), including their differentials. Let \(S\) be the set where their values and differentials agree. The same normal-neighbourhood argument makes \(S\) open. It is closed: near a limit point of \(S\), continuity and the Hausdorff property first give equality of values, and a common target chart then gives equality of all first coordinate derivatives by continuity. Thus \(S\) is the whole domain.

Finally the geodesic equation of an analytic connection is an analytic first-order system on its tangent bundle, by its coordinate formula in [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1). [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) proves analytic dependence of its solutions and analytic inversion. Consequently its exponential and its local normal inverse are analytic. Formula (A.5), a composition of these maps and the fixed linear map \(df_p\), makes \(f\) analytic near every \(p\). □

**Lemma A.2 (Analytic uniqueness).** An analytic section of an analytic vector bundle over a connected analytic manifold that vanishes on a nonempty open set vanishes everywhere. Two analytic maps into an analytic manifold that agree on a nonempty open set agree everywhere on their connected common domain.

**Proof.** For the section let \(S\) consist of points near which it is zero. This is nonempty and open. If \(p\) is in its closure, choose an analytic bundle trivialization and coordinates around \(p\). Every partial derivative of each coefficient function vanishes at every point of \(S\) in this chart. These derivatives are continuous by the termwise-differentiation proof in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1), so all of them vanish at \(p\). The convergent Taylor series of each coefficient has only zero coefficients, making the section zero near \(p\). Thus \(S\) is closed and connectedness proves the claim.

For maps, use instead the set where their germs agree. At a limit point \(p\), their values agree by continuity and the Hausdorff property of the target. Choose a common target chart around that value and shrink the source chart until both images lie in it. Their coordinate difference is analytic and all its derivatives vanish at \(p\), by the preceding argument. Their germs therefore agree at \(p\). This set too is open, closed and nonempty. The same proof in dimension one includes the identity principle along any connected real interval. □

**Theorem A.3 (General analytic affine extension).** Let \(M\) be connected and simply connected, let \(N\) have a geodesically complete connection, and suppose both connections are analytic. Every affine map from a nonempty connected open subset \(U\subseteq M\) to \(N\) extends uniquely to an affine map \(M\to N\). There is no dimension, rank or source-completeness assumption.

**Proof.** [Geodesics B.3](geodesics-normal-coordinates-and-curvature.md#theorem-b-3) supplies arbitrarily small connected convex normal sets \(V\subset M\). For every \(x\in V\), the exponential at \(x\) is a diffeomorphism from an open star-shaped set \(W_x\subset T_xM\) onto all of \(V\). Its inverse is analytic, by [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) and the analytic geodesic equation; its derivative is invertible everywhere since it is already a smooth diffeomorphism.

Take any affine germ \(s\) at any \(x\in V\), with value \(q\) and differential \(L:T_xM\to T_qN\). Define on all of \(V\)
\[
F_s(y)=\exp_q\bigl(L(\exp_x|_{W_x})^{-1}(y)\bigr).
\tag{A.6}
\]
Completeness of the target makes \(\exp_q\) defined on all of \(T_qN\), by [Geodesics A.2](geodesics-normal-coordinates-and-curvature.md#theorem-a-2). It is analytic at every vector: the finite-interval analytic ODE proof in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) applies along the corresponding geodesic on \([0,1]\). Thus \(F_s\) is analytic on \(V\). Lemma A.1 makes it agree with \(s\) near \(x\). Its affine defect (A.1) is an analytic section of
\(T^*V\otimes T^*V\otimes F_s^*TN\), zero near \(x\). Lemma A.2 makes that defect zero on connected \(V\). Consequently **every affine germ at every point of \(V\) extends to all of this same \(V\)**. Its extension is unique by A.1.

We now give the global continuation argument. Let \(E\) be the set of germs of local affine maps from \(M\) to \(N\). A germ records its base point. For any local affine map \(h:O\to N\), the set
\[
[h,O]=\{\operatorname{germ}_y h:y\in O\}
\]
is declared to be an open basic set. These sets form a basis: if two contain the same germ at \(y\), their representatives agree on some neighbourhood of \(y\), which gives a smaller such set in their intersection. The base-point map \(\pi:E\to M\) maps each basic set homeomorphically to its open domain.

Over a convex normal set \(V\) as above, group the germs by their unique extensions \(h:V\to N\). Distinct extensions give disjoint sets \([h,V]\): a common germ would force equality throughout \(V\) by A.1. Every germ over \(V\) belongs to one of them by (A.6). These are open sheets, each mapped homeomorphically to \(V\). The map \(\pi\) is onto because constant maps are affine by (A.2). Thus it is a covering in the precise topological sense of [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). Its fibre need not be finite or countable; the path and square lifting proof there only uses the evenly covered sets and compact parameter intervals and squares, and applies without a countability assumption on \(E\).

Fix the original germ at a point \(p\in U\). Every path from \(p\) has a unique lift starting at that germ by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). Two paths with the same endpoint are endpoint-fixed homotopic because \(M\) is simply connected; the path-class operations proving this are in [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4). The square-lifting part of [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) then gives equal final germs. Denote this endpoint germ at \(y\) by \(s_y\).

Locally these germs are the germs of a single affine map. Indeed take a convex normal \(V\) containing \(y\), a fixed path to \(y\), and then paths within \(V\). Their lifts remain in the sheet specified by the unique representative of \(s_y\) on \(V\). Path independence shows that \(s_z\) is its germ for every \(z\in V\). Define \(f(z)\) to be the value of \(s_z\). This local description proves that \(f\) is smooth, analytic and affine. It agrees with the original map near \(p\), and A.1 on connected \(U\) gives agreement on all of \(U\). Finally A.1 on connected \(M\) gives uniqueness of the extension. □

**Corollary A.4 (Global isomorphisms and isometric immersions).** If both connected analytic affine manifolds are simply connected and geodesically complete, a local affine isomorphism between connected open sets extends uniquely to a global affine isomorphism. If \(M,N\) are analytic Riemannian manifolds, \(M\) is connected and simply connected, and \(N\) is complete, an affine isometric immersion on a connected nonempty open subset of \(M\) extends uniquely to an affine isometric immersion \(M\to N\). In equal dimensions it extends to a local isometry. If both manifolds are connected, simply connected and complete, a local isometry between connected open sets extends to a global isometry.

**Proof.** Extend a local affine isomorphism and its inverse separately by A.3. Their two compositions are affine: apply (A.3) successively, or substitute the chain rule in (A.2). On the original open sets those compositions are the identity. A.1 on each connected manifold makes them the identity everywhere. Hence the extensions are inverse diffeomorphisms.

For the metric statements, [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) gives the Levi-Civita coefficients from the metric and its first derivatives by matrix inversion. They are analytic by [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) identifies Riemannian completeness with geodesic completeness, so A.3 extends the given affine map. Put \(B=f^*g_N-g_M\). The metric-compatibility and tensor-derivative rules in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1), applied with \(\nabla df=0\), give \(\nabla B=0\). It is zero initially. Along every piecewise smooth path its components in a parallel frame are constant, by [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) and C.1; therefore it is zero everywhere on connected \(M\). Such paths exist by the coordinate-ball path argument in [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4). Thus \(df\) is an isometric injection at every point, proving immersion. In equal dimensions the inverse function theorem makes it a local isometry. A local isometry is affine by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3); applying the first part to it and its inverse proves the final assertion. □

## B. The connection in a radial parallel frame

Let \(p\in M\), choose a frame \(u_0:\mathbb R^n\to T_pM\), and use the normal chart
\[
E(z)=\exp_p(u_0z)
\]
on an open star-shaped set about zero. Transport \(u_0\) along \(t\mapsto E(tz)\) to obtain the radial frame \(u(z)\). Write the pulled-back solder and connection forms as
\[
\alpha=\sum_j a_j(z)\,dz^j,\qquad
\beta=\sum_j b_j(z)\,dz^j,
\]
where \(a_j(z)\in\mathbb R^n\) and \(b_j(z)\in\mathfrak{gl}(n,\mathbb R)\). Thus \(dE_z(w)=u(z)\alpha_z(w)\). Denote the frame components of the tensors by
\[
\begin{aligned}
\mathsf T_z(v,w)&=u(z)^{-1}T_{E(z)}(u(z)v,u(z)w),\\
\mathsf R_z(v,w)&=u(z)^{-1}R_{E(z)}(u(z)v,u(z)w)u(z).
\end{aligned}
\tag{B.1}
\]

**Theorem B.1 (Nonsingular radial reconstruction).** The frame and forms above are smooth at zero. For fixed \(z\), put
\(U_j(t)=t\,a_j(tz)\), \(V_j(t)=t\,b_j(tz)\). They satisfy
\[
\begin{aligned}
U_j'&=e_j+V_jz+\mathsf T_{tz}(z,U_j),\\
V_j'&=\mathsf R_{tz}(z,U_j),\\
U_j(0)&=0,\qquad V_j(0)=0.
\end{aligned}
\tag{B.2}
\]
This is a nonsingular linear inhomogeneous ODE for \((U_j,V_j)\). Thus the radial components of torsion and curvature determine both forms and the connection on the whole normal domain.

**Proof.** [Connections C.1](connections-and-parallel-transport.md#theorem-c-1) and C.2 construct parallel transport and prove its smooth parameter dependence, including at \(z=0\), for the smooth path family \(E(tz)\). Its value at zero is \(u_0\). Along each ray the transported frame is parallel by reparametrization and concatenation of transport. The geodesic velocity is parallel as well. Consequently, for the radial coordinate vector \(\mathcal R_z=z\),
\[
\beta_z(z)=0,\qquad \alpha_z(z)=z,\qquad \alpha_0=I.
\tag{B.3}
\]
Here the last equality follows from \((d\exp_p)_0=I\), proved in [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). Smoothness and \(\beta_{tz}(z)=0\) for \(t\ne0\) also give \(\beta_0=0\). This is a parallel frame, not generally a coordinate frame.

[Linear connections D.1](linear-and-affine-connections.md#theorem-d-1) and B.3 give the structure equations in this frame:
\[
d\alpha+\beta\wedge\alpha=\mathsf T(\alpha,\alpha),
\qquad d\beta+\beta\wedge\beta=\mathsf R(\alpha,\alpha).
\tag{B.4}
\]
The notation on the right means the two-form whose value on \(Y,Z\) is respectively
\(\mathsf T(\alpha(Y),\alpha(Z))\) and
\(\mathsf R(\alpha(Y),\alpha(Z))\); it includes no extra factor of two.

For precision evaluate these equations on \((\mathcal R,\partial_j)\) in Cartesian normal coordinates. Differentiating \(\sum_k z^ka_k=z\) and \(\sum_kz^kb_k=0\) in \(z^j\) gives
\[
\sum_kz^k\partial_j a_k=e_j-a_j,\qquad
\sum_kz^k\partial_j b_k=-b_j.
\]
The coordinate exterior-derivative formula in [Curvature and holonomy A.2](curvature-and-holonomy-groups.md#lemma-a-2) now yields
\[
\begin{aligned}
\mathcal R(a_j)+a_j
   &=e_j+b_jz+\mathsf T_z(z,a_j),\\
\mathcal R(b_j)+b_j
   &=\mathsf R_z(z,a_j).
\end{aligned}
\tag{B.5}
\]
The sign of \(b_jz\) comes from
\((\beta\wedge\alpha)(\mathcal R,\partial_j)=-b_jz\).

At \(tz\), differentiating \(t a_j(tz)\) and \(t b_j(tz)\), then using bilinearity in (B.5), gives (B.2) for \(t\ne0\). Smoothness makes both sides continuous at zero, so it holds there too, with the displayed zero initial data. Its coefficients are smooth on a neighbourhood of the radial parameter interval. [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) proves uniqueness for this linear equation. At \(t=1\) its solution gives \(a_j(z)\) and \(b_j(z)\), including at \(z=0\).

Finally let \(a\) denote the invertible matrix with columns \(a_j\). The coordinate connection coefficients are recovered by
\[
\Gamma^k_{ij}
=(a^{-1})^k{}_\ell\,
       \bigl(\partial_i a_j^\ell+(b_i)^\ell{}_m a_j^m\bigr).
\tag{B.6}
\]
Indeed \(dE(\partial_j)=u a_j\), whose covariant derivative in direction \(\partial_i\) is \(u(\partial_i a_j+b_i a_j)\); multiply by \(a^{-1}\) to return to the coordinate frame. This proves the reconstruction assertion. In dimension zero all forms and equations are empty and the assertion holds on a point. □

**Theorem B.2 (Local affine equivalence from radial measurements).** Let \(F:T_pM\to T_qN\) be a linear isomorphism. Choose a common sufficiently small star-shaped normal domain, with initial frames \(u_0\) and \(F u_0\). The map
\[
f=\exp_q\circ F\circ\exp_p^{-1}
\tag{B.7}
\]
is affine if and only if the two torsion and curvature tensors have equal components in these radial parallel frames at every paired point. Equivalently, the radial identification
\[
L_x=P'_{0x}\,F\,P_{0x}^{-1}
\tag{B.8}
\]
must carry both tensors to their target tensors. In that case \(df_x=L_x\). More generally, any local diffeomorphism sending \(p\) to \(q\), carrying the radial parallel frames to one another, and preserving torsion and curvature is affine.

**Proof.** Pull both sets of data to the same normal coordinate domain. If their components \(\mathsf T_z,\mathsf R_z\) agree, the ODEs (B.2) are identical, with identical initial data. Their unique solutions give \(a_j=a'_j\) and \(b_j=b'_j\) everywhere. Equality of the solder forms gives \(df_x=L_x\), because the two coordinate derivatives have the same components in the paired frames. Equality of connection forms then gives (A.1) for \(f\), by the frame derivative formula of [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2). This proves sufficiency.

Conversely an affine local diffeomorphism preserves the connection on all vector fields, by its defining equation. It preserves brackets: in coordinates the second derivatives of \(f\) cancel in the expression for \(f_*[Y,Z]-[f_*Y,f_*Z]\); this is also [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3). Substitution into the definitions of \(T\) and \(R\) proves their naturality. Formula (A.4) identifies its differential along each radius with (B.8), so their radial components agree.

For the last assertion, use \(F=dh_p\) to pair the initial frames. A map \(h\) carrying the radial frames satisfies \(dh_xu(x)=u'(h(x))\). For a fixed initial column \(z\), its image of the source radial geodesic therefore solves the first-order equation \(y'=u'(y)z\), with \(y(0)=q\): the source velocity has the constant frame column \(z\). The target radial geodesic with initial velocity \(Fu_0z\) solves this same equation by the construction of its radial frame. [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives equality of the curves on their common interval. Thus \(h\) is (B.7), after restricting to the common normal domain. Preservation of the two tensors now gives exactly the equal radial components used in the sufficiency proof. □

**Theorem B.3 (All curvature and torsion jets determine an analytic germ).** For analytic connections, a linear isomorphism \(F:T_pM\to T_qN\) is the differential of a local affine isomorphism sending \(p\) to \(q\) if and only if it carries
\[
(\nabla^m T)_p,\qquad(\nabla^m R)_p
\quad(m=0,1,2,\ldots)
\tag{B.9}
\]
to the corresponding target tensors, with all input and output slots transformed. The germ is unique. If the connected manifolds are also simply connected and complete, this germ extends uniquely to a global affine isomorphism.

**Proof.** An affine isomorphism intertwines covariant differentiation, first on vector fields by definition and then on covectors and all tensors by the Leibniz rules of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). The naturality argument in B.2 therefore proves necessity of every condition in (B.9).

For sufficiency use the paired normal coordinates and frames of B.2. Fix \(z\) in their common domain. The two radial geodesics and their parallel frames are analytic in \(t\), by [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) applied to the geodesic and linear parallel-transport equations. Hence every component of \(\mathsf T_{tz}\) and \(\mathsf R_{tz}\) is analytic on a connected open interval containing \([0,1]\), after choosing the common normal domain small enough. The open interval exists because the closed radial segment is contained in the open normal domain and the local ODE domain is open.

A tensor's derivative in a parallel frame is its covariant derivative in the curve direction, by [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). The radial velocity is itself parallel. Repeating that identity shows that the \(m\)-th derivative at zero of any radial tensor component is the corresponding component of \(\nabla^m T\) or \(\nabla^m R\), with \(u_0z\) in all \(m\) derivative slots. Condition (B.9) makes these derivatives equal for every \(m\), in the paired frames. The convergent Taylor series make their difference zero near \(t=0\), and A.2 on the interval makes it zero at \(t=1\). This argument is applied separately to each \(z\); it does not assume one convergence radius for infinitely many derivatives or rays.

Thus the radial components agree throughout the common normal domain. B.2 supplies (B.7) as an affine local diffeomorphism with the required one-jet. A.1 gives uniqueness of the germ, and A.4 proves the stated global extension. □

## C. Parallel torsion and curvature produce analytic coordinates

**Theorem C.1 (Analyticity and equivalence of smooth parallel data).** Suppose a smooth connection satisfies \(\nabla T=\nabla R=0\). Its normal-coordinate charts form a compatible analytic atlas in which the connection is analytic. For two such connected manifolds, a linear isomorphism \(F:T_pM\to T_qN\) carrying \(T_p,R_p\) to the target tensors gives a unique local affine isomorphism with that value and differential. If both manifolds are complete and simply connected, it extends uniquely to a global affine isomorphism.

**Proof.** [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) says that a parallel tensor has constant components in any parallel frame along a path. In the radial frames of B.1, therefore,
\(\mathsf T_z=\mathsf T_0\) and \(\mathsf R_z=\mathsf R_0\).
The ODE (B.2) becomes
\[
U_j'=e_j+V_jz+\mathsf T_0(z,U_j),\qquad
V_j'=\mathsf R_0(z,U_j).
\tag{C.1}
\]
This is a linear system with coefficients polynomial in the parameter \(z\) and constant in \(t\). It has an actual smooth solution on the whole radial interval, namely the forms already constructed. [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) makes its time-one value analytic in \(z\); its finite-interval argument applies about every \(z\) in the chart. Consequently \(a_j,b_j\) are analytic. Matrix inversion, differentiation and (B.6) make the coordinate coefficients of the connection analytic.

This proves analyticity in each normal chart separately. To check their compatibility, take a transition between two overlapping normal charts. It is a smooth affine local diffeomorphism between the two coordinate connections, since both describe the same connection on the original manifold. Each coordinate connection is analytic by the preceding paragraph, so A.1 makes the transition analytic at every point of its domain. Thus these charts really define an analytic atlas compatible with the original smooth structure.

For two connections as in the statement, the assumed isomorphism makes \(\mathsf T_0,\mathsf R_0\) equal in paired initial frames. They remain constant along all radii, so B.2 constructs the local affine isomorphism. A.1 gives uniqueness. The newly proved analytic atlases allow A.4 to be applied under the global completeness and simple-connectedness hypotheses. No analyticity assumption on the original smooth data was used. □

## D. Examples that distinguish the hypotheses

**Example D.1 (A complete flat connection with a nonzero coefficient).** On the real line define
\[
\nabla_{\partial_x}\partial_x
=\frac{6x}{1+3x^2}\,\partial_x.
\tag{D.1}
\]
This connection is analytic and complete and has zero torsion and curvature. The map \(\phi(x)=x+x^3\) is a global affine isomorphism to the line with its ordinary derivative.

**Proof.** Its derivative \(1+3x^2\) is positive. The fundamental theorem of calculus in [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) makes \(\phi\) strictly increasing. Its limits at the two ends of the line are the two infinities; the intermediate value theorem, [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), gives surjectivity. It is therefore bijective, and its nonzero derivative and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) give a smooth inverse. The analytic inverse assertion of [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) makes that inverse analytic.

For a target with zero connection coefficient, equation (A.2) is
\(\phi''-\Gamma\phi'=0\), which is exactly (D.1). Thus \(\phi\) and its inverse intertwine the connections. More explicitly, every geodesic with initial data \(x_0,v_0\) is
\[
x(t)=\phi^{-1}\bigl(\phi(x_0)+(1+3x_0^2)v_0t\bigr),
\qquad t\in\mathbb R.
\tag{D.2}
\]
Differentiating \(\phi(x(t))\) twice gives the geodesic equation; its value and derivative at zero are the required data. [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) proves uniqueness, and the formula proves completeness. Torsion and curvature are alternating in their first two inputs, by their definitions and [Geodesics C.1](geodesics-normal-coordinates-and-curvature.md#theorem-c-1). In one dimension any two inputs are dependent, so both tensors vanish. Nonzero coordinate coefficients consequently do not certify nonzero curvature. □

**Example D.2 (Missing hypotheses and an unequal-dimensional extension).** Target completeness, source simple connectedness and analyticity cannot be discarded from A.3 in general. By contrast, completeness of the source, equal dimensions and injectivity of the differential are unnecessary.

**Proof.** For target completeness take the ordinary connection on \(M=\mathbb R\) and on \(N=(0,1)\). The identity on \(U=(1/3,2/3)\) is affine. Any affine extension would satisfy \(f''=0\), so \(f(t)=at+b\) by two applications of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Agreement on \(U\) gives \(a=1,b=0\), which does not map all of \(\mathbb R\) into \(N\). Both manifolds are analytic and simply connected; the target is incomplete because its unit-speed lines reach the boundary in finite time.

For source simple connectedness use the complete flat torus
\(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) as both source and target. Its quotient, global parallel coordinate frame, flat connection and completeness are proved in [Geodesics F.2](geodesics-normal-coordinates-and-curvature.md#example-f-2). Let
\[
A=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]
On a sufficiently small projected ball about \([0]\), the map \([x]\mapsto[Ax]\) is a well-defined local isometry. Suppose it extended to an affine map \(F:\mathbb T^2\to\mathbb T^2\). In the two global parallel frames, (A.1) says that every derivative of every coefficient of \(dF\) is zero. The coordinate-ball path argument makes these coefficients constant on the connected torus, so \(dF=A\) everywhere.

The image under \(F\) of \(t\mapsto[te_1]\), \(0\leq t\leq1\), is a loop based at \([0]\). Lift it to \(\mathbb R^2\) starting at zero using [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). The covering charts identify its velocity with \(Ae_1\). The fundamental theorem then gives its endpoint as \((3/5,4/5)\). A lift of a loop based at \([0]\) must end in \(\mathbb Z^2\), a contradiction.

Here is a smooth counterexample to removal of analyticity with both other hypotheses retained. Set \(a=(3,0)\). [Local tools 3.1](local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) gives a smooth function \(\eta:\mathbb R^2\to[0,1]\), equal to one near zero and supported in the unit ball. For \(\epsilon>0\), put
\[
h(x)=\epsilon|x-a|^2\eta(x-a),\qquad
g=e^{2h}(dx_1^2+dx_2^2).
\tag{D.3}
\]
This target metric equals the Euclidean metric near the origin. It is complete: compact support gives \(0\leq h\leq H\) for some finite \(H\), and comparison of lengths of every curve, with a straight segment for the upper bound, gives
\[
|x-y|\leq d_g(x,y)\leq e^H|x-y|.
\]
A \(d_g\)-Cauchy sequence is Euclidean Cauchy and has a Euclidean limit by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations); the upper bound gives convergence to that limit in \(d_g\). [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) makes its Levi-Civita connection geodesically complete.

Its curvature at \(a\) is nonzero. To verify that without importing a conformal-curvature formula, substitute (D.3) into the Levi-Civita formula of [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1):
\[
\Gamma^k_{ij}
=\delta^k_j\,\partial_i h+\delta^k_i\,\partial_j h
-\delta_{ij}\,\partial_k h.
\]
At \(a\), \(h=0\), \(dh=0\), and \(\partial_i\partial_jh=2\epsilon\delta_{ij}\). Thus every Christoffel coefficient is zero there, and the coordinate curvature formula of [Geodesics C.1](geodesics-normal-coordinates-and-curvature.md#theorem-c-1) gives
\[
R(\partial_1,\partial_2)\partial_2\big|_a
=(\partial_1\Gamma^1_{22}-\partial_2\Gamma^1_{12})\big|_a\,\partial_1
=-4\epsilon\,\partial_1.
\tag{D.4}
\]
The second coordinate is zero by the same formula.

The identity from a small Euclidean neighbourhood of zero into \((\mathbb R^2,g)\) is a local isometry. If it had a global affine extension from the Euclidean plane, the parallel-tensor argument in A.4, which uses only smoothness, would make that extension a local isometry everywhere. Its complete connected source makes it surjective by [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4). Naturality of curvature under a local isometry, [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), would then make the target flat everywhere, contrary to (D.4). Both planes are simply connected by the straight-line contraction. This is the required smooth counterexample.

An isometric immersion by itself need not be affine. For the standard metrics the map \(c:\mathbb R\to\mathbb R^2\), \(c(t)=(\cos t,\sin t)\), has \(|c'(t)|=1\), so its pullback metric is \(dt^2\). The derivatives and squared-norm identity follow from [Riemannian connections D.1](riemannian-connections-and-convex-neighbourhoods.md#lemma-d-1). Its affine defect is \(c''(t)=-c(t)\ne0\), by (A.2). Thus the affine assumption in the immersion statement of A.4 has real content.

Finally let \(M=(-1,1)\times\mathbb R\), with ordinary differentiation, and let \(N=\mathbb R^3\), also flat. The map
\[
f(x,y)=(x,0,0)
\tag{D.5}
\]
has rank one and satisfies (A.2) because all its second derivatives and all connection coefficients vanish. The strip is convex, hence connected and simply connected by straight-line contraction, but incomplete: the horizontal unit-speed geodesic starting at zero leaves it at time one. The target is complete. The restriction to any nonempty connected open subset extends by (D.5) to the whole strip, uniquely by A.1. This gives an explicit instance of A.3 with unequal dimensions, noninjective differential and incomplete source. □

**Exercise D.3 (Extending a spherical local isometry from its one-jet).** Let \(n\geq1\), \(r>0\), and let \(f:U\to S^n_r\) be a local isometry on a connected nonempty open subset of the round sphere. Extend it explicitly to a global isometry using its value and differential at any \(p\in U\). Include \(n=1\).

**Solution.** Write \(q=f(p)\) and \(F=df_p:p^\perp\to q^\perp\). The differential is a linear isometry between these tangent spaces. Define on the ambient space
\[
A(v)=\frac{\langle v,p\rangle}{r^2}\,q
+F\left(v-\frac{\langle v,p\rangle}{r^2}\,p\right).
\tag{D.6}
\]
For the orthogonal decomposition \(v=cp+w\), \(w\perp p\), the two terms \(cq,Fw\) are perpendicular and have squared norms \(c^2r^2,|w|^2\). Thus \(|Av|=|v|\). Polarization gives preservation of every inner product. Equal finite dimensions then make \(A\) an invertible orthogonal linear map.

Its restriction to the sphere is a global isometry: it preserves the sphere and the Euclidean inner products on all its tangent spaces, and its inverse is the restriction of \(A^{-1}\). At \(p\) it has value \(q\) and differential \(F\). [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) makes both this restriction and \(f\) affine. Lemma A.1 on connected \(U\) proves their equality there. Any other global isometry with that one-jet agrees with \(A\) on the whole sphere by A.1 and connectedness. The sphere is connected for \(n\geq1\), as is also explicit in the great-circle paths of [Riemannian connections E.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-e-1). This argument works without simple connectedness, so it includes the circle \(n=1\). □

## E. A connection whose parallel sections are Killing fields

In the remaining parts the metric is positive definite and \(\nabla\) is its Levi-Civita connection. A vector field \(X\) is **Killing** when its local flow preserves the metric. Put
\[
A_X(Y)=-\nabla_YX.
\tag{E.1}
\]
This sign will be used in every transport and bracket formula. Biquard's freely available geometric-analysis notes explain the Killing equation and its Ricci contraction. We prove the full one-jet equations, rather than assuming that contraction or an isometry-group theorem.

**Lemma E.1 (The Killing equation and its first prolongation).** A smooth field is Killing if and only if \(A_X\) is skew-adjoint. For a Killing field,
\[
\nabla_Y A_X=R(X,Y).
\tag{E.2}
\]
The space \(\mathfrak i(M)\) of Killing fields is a vector space closed under the ordinary vector-field bracket.

**Proof.** [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) constructs the smooth local flow \(\phi_t\). Differentiating the coordinate formula for a pulled-back metric gives
\[
(\mathcal L_Xg)_{ij}
 =X^k\partial_kg_{ij}
  +g_{kj}\partial_iX^k+g_{ik}\partial_jX^k.
\]
Metric compatibility and zero torsion, proved in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1), rewrite this as
\[
(\mathcal L_Xg)(Y,Z)
 =g(\nabla_YX,Z)+g(Y,\nabla_ZX).
\tag{E.3}
\]
The flow law and the chain rule give
\(\frac d{dt}\phi_t^*g=\phi_t^*(\mathcal L_Xg)\).
Thus zero derivative at \(t=0\) is necessary for a flow of local isometries, and (E.3) equal to zero makes the pullback constant on every flow interval. This proves the equivalence and linearity.

Such a flow preserves \(\nabla\), by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Differentiating this preservation, with vector fields pulled back by the flow, gives
\[
0=(\mathcal L_X\nabla)(Y,Z)
 =[X,\nabla_YZ]-\nabla_{[X,Y]}Z-\nabla_Y[X,Z].
\tag{E.4}
\]
For completeness the derivative of the pullback of a vector field \(Z\) has coordinates \(X^j\partial_jZ^i-Z^j\partial_jX^i\), its bracket with \(X\); applying the product rule to the pulled-back connection gives precisely the three terms in (E.4). Now set \(B(Y)=\nabla_YX\). Using \([X,Y]=\nabla_XY-\nabla_YX\), the right side of (E.4) expands to
\[
\begin{split}
&\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ
 -\nabla_{\nabla_XY-\nabla_YX}Z\\
&\hspace{12mm}+\nabla_Y(BZ)-B(\nabla_YZ)
 =R(X,Y)Z+(\nabla_YB)Z.
\end{split}
\]
Since \(A_X=-B\), this proves (E.2) on every argument \(Z\).

The coordinate formula for a Lie derivative on a covariant tensor is its directional derivative plus one derivative-of-\(X\) term in each covariant slot. Substitution of that formula twice, cancellation of the mixed second partial derivatives, and the product rule give
\([\mathcal L_X,\mathcal L_Y]=\mathcal L_{[X,Y]}\).
One can check the cancellation slot by slot: on a scalar it is
\(X^i\partial_i(Y^j\partial_j f)-Y^i\partial_i(X^j\partial_j f)
 =[X,Y]^j\partial_jf\); on a coordinate one-form \(dx^k\), use
\(\mathcal L_Xdx^k=dX^k\) and the same scalar identity. The product rule gives the identity on tensor products of these one-forms, hence on \(g\). If both Lie derivatives of \(g\) vanish, so does \(\mathcal L_{[X,Y]}g\). Equation (E.3) proves bracket closure. □

Let
\[
\mathcal E=TM\oplus\mathfrak{so}(TM,g),\qquad
D_Y(v,A)=\bigl(\nabla_Yv+AY,\ \nabla_YA-R(v,Y)\bigr).
\tag{E.5}
\]
The skew-adjoint endomorphisms form a vector bundle: in the orthonormal frames of [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2) they are the skew matrices. Covariant differentiation preserves this subbundle by metric compatibility. Curvature is skew-adjoint in its endomorphism slot, again by metric compatibility, or by [Geodesics C.1](geodesics-normal-coordinates-and-curvature.md#theorem-c-1) applied to \(g\). Thus (E.5) takes values in the indicated bundle. The product rule shows that it is a connection.

**Theorem E.2 (Killing transport, curvature and bracket).** Killing fields correspond bijectively to \(D\)-parallel sections, by \(X\mapsto(X,A_X)\). They are determined on a connected manifold by this pair at one point, and
\(\dim\mathfrak i(M)\leq n(n+1)/2\).
The curvature of \(D\) is
\[
R^D(Y,Z)(v,A)=
\left(0,\ [R(Y,Z),A]+R(AY,Z)+R(Y,AZ)
                 -(\nabla_vR)(Y,Z)\right).
\tag{E.6}
\]
The pair associated to the bracket of fields with pairs \((v,A),(w,B)\) at a point is
\[
\bigl(Aw-Bv,\ [A,B]-R(v,w)\bigr).
\tag{E.7}
\]

**Proof.** The first component of \(D(X,A)=0\) says \(A=-\nabla X\). Its required skew-adjointness is the Killing equation E.1; the second component then vanishes by (E.2). This proves both directions. Uniqueness of parallel transport for vector-bundle connections, [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2), makes a parallel section determined by its value along every path. Connected manifolds are joined by piecewise smooth paths, as proved in [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4). Evaluation is therefore injective. The bundle rank is \(n+n(n-1)/2\), by counting the independent entries of a skew matrix, which gives the dimension bound by [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

Here is the curvature calculation, with the derivatives in every slot included. Write \(D=\nabla^{\mathcal E}+S\), where
\[
S_Y(v,A)=(AY,-R(v,Y)).
\]
The direct-sum connection has curvature
\((v,A)\mapsto(R(Y,Z)v,[R(Y,Z),A])\), by [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Expanding the definition of curvature gives
\[
R^D(Y,Z)=R^{\mathcal E}(Y,Z)
 +(\nabla_Y S)_Z-(\nabla_Z S)_Y+[S_Y,S_Z].
\]
The two derivative terms on \((v,A)\) are
\[
\bigl(0,-(\nabla_YR)(v,Z)+(\nabla_ZR)(v,Y)\bigr).
\]
The two composites in the last commutator are
\[
S_YS_Z(v,A)=(-R(v,Z)Y,-R(AZ,Y)),\quad
S_ZS_Y(v,A)=(-R(v,Y)Z,-R(AY,Z)).
\]
The first curvature component is consequently
\(R(Y,Z)v-R(v,Z)Y+R(v,Y)Z=0\),
by the torsion-free first Bianchi identity, [Geodesics C.2](geodesics-normal-coordinates-and-curvature.md#theorem-c-2). Its second Bianchi identity gives
\[
-(\nabla_YR)(v,Z)+(\nabla_ZR)(v,Y)
=-(\nabla_vR)(Y,Z).
\]
Finally \(-R(AZ,Y)=R(Y,AZ)\). These equalities prove (E.6).

For (E.7), \([X,Y]=\nabla_XY-\nabla_YX=A_XY-A_YX\). Differentiation in direction \(Z\), using (E.2) for each field, gives
\[
\nabla_Z[X,Y]
 =R(X,Z)Y-R(Y,Z)X-[A_X,A_Y]Z
 =R(X,Y)Z-[A_X,A_Y]Z.
\]
The last equality is the first Bianchi identity. Taking its negative gives the second component of (E.7); the first has already been computed. □

To state the analytic criterion, differentiate \(R^D\) using \(D\) on \(\mathcal E\) and its endomorphisms, and \(\nabla\) on every tangent argument. Denote this full tensor derivative by \(\mathcal D\), and define
\[
\begin{aligned}
\mathcal K_p=\bigl\{e\in\mathcal E_p:\;&
 (\mathcal D^mR^D)_p(u_1,\ldots,u_m;y,z)e=0\\
&\text{for every }m\geq0\text{ and every choice of arguments}\bigr\}.
\end{aligned}
\tag{E.8}
\]
This definition includes all orders, rather than an unproved finite truncation.

**Theorem E.3 (Analytic Killing extension and the jet kernel).** On a connected simply connected analytic Riemannian manifold, evaluation gives a linear isomorphism
\[
\mathfrak i(M)\longrightarrow\mathcal K_p,\qquad
X\longmapsto(X_p,(A_X)_p).
\tag{E.9}
\]
Every Killing field on a connected nonempty open subset extends uniquely to a global Killing field. Completeness is unnecessary. All these fields are analytic, and (E.7) describes their bracket on initial pairs.

**Proof.** We spell out the analytic vector-bundle form of the earlier holonomy theorem. For any analytic vector bundle \(V\) with analytic connection \(D\), its frame bundle and principal connection are analytic: in analytic local frames the formula is
\(\omega=h^{-1}Ah+h^{-1}dh\), as in [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2), and matrix inversion and composition are analytic by [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). [Flat connections B.2](flat-connections-and-infinitesimal-holonomy.md#theorem-b-2) therefore identifies the restricted holonomy algebra with the span of all horizontal curvature jets.

Those jets have the same span as full covariant curvature derivatives, using any analytic connection on the tangent arguments. To see this in coordinates, let \(F_{ij}\) be the curvature matrices and \(A_i\) the connection matrices of \(V\). The first covariant derivative is
\[
(\mathcal D_k F)_{ij}
 =\partial_k F_{ij}+[A_k,F_{ij}]
   -\Gamma^\ell_{ki}F_{\ell j}-\Gamma^\ell_{kj}F_{i\ell}.
\tag{E.10}
\]
Horizontal differentiation of the equivariant matrix function on the frame bundle produces the first two terms. The remaining terms are scalar linear combinations of order-zero curvature components. Repeated differentiation and the product rule show inductively that each covariant component of order at most \(m\) is a scalar linear combination of horizontal words of order at most \(m\), and conversely: solve (E.10) for its first two terms and repeat, including the additional derivative-input slots at the next order. This is the same triangular order argument as [Geodesics D.2](geodesics-normal-coordinates-and-curvature.md#theorem-d-2), now with \(V\)-frames independent of tangent frames. Thus the two spans agree at the chosen frame.

A vector killed by that Lie algebra is fixed by its connected holonomy group. Indeed each exponential fixes it, from the matrix exponential ODE in [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), and a connected Lie group is generated by an exponential neighbourhood: the subgroup generated by that open neighbourhood is open, and all its other cosets are open, so connectedness makes it the whole group. The exponential is a local diffeomorphism at zero by [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Conversely, differentiating the action of every exponential at zero shows that a vector fixed by the group is killed by the algebra. On a simply connected base every loop is contractible, so full and restricted holonomy agree, by [Curvature and holonomy C.5](curvature-and-holonomy-groups.md#theorem-c-5). [Reduction and the holonomy theorem A.3](reduction-and-the-holonomy-theorem.md#theorem-a-3) now supplies exactly one global parallel section for each such fixed vector.

Apply this to \((\mathcal E,D)\). Analytic orthonormal frames exist by the Gram–Schmidt formula of [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2): its positive square roots are analytic by analytic inversion in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). In these frames (E.5) has analytic coefficients. Thus (E.8) is exactly the annihilator just considered, and E.2 identifies its parallel sections with Killing fields. This proves (E.9).

If a Killing field is given on an open subset, its \(D\)-parallel pair is annihilated there by \(R^D\). Differentiating this identity repeatedly, using \(Ds=0\), shows that every full derivative in (E.8) annihilates its value. This can be checked at any point in the subset, so (E.9) extends the pair globally. Parallel uniqueness gives agreement on the whole connected subset and uniqueness on \(M\). Finally, in any analytic coordinate ball, a parallel section is obtained by transport along coordinate radial segments from their centre. The transport is a linear analytic ODE with analytic parameters; [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1) makes its endpoint analytic. The section, and hence its vector component, is analytic locally everywhere. No step used geodesic completeness. □

**Proposition E.4 (Flow derivatives, parallel transport and holonomy).** Let \(X\) be a globally defined Killing field on a connected Riemannian manifold, not assumed complete. Along its orbit \(\gamma(t)=\phi_t(p)\), let \(P_t:T_pM\to T_{\gamma(t)}M\) be parallel transport. On the orbit interval,
\[
P_t^{-1}(d\phi_t)_p=\exp(-t(A_X)_p).
\tag{E.11}
\]
For every real \(t\), \(\exp(t(A_X)_p)\) normalizes both full and restricted holonomy at \(p\). In particular, if \(\mathfrak h_p\) is the restricted holonomy algebra, then
\[
[(A_X)_p,\mathfrak h_p]\subseteq\mathfrak h_p.
\tag{E.12}
\]
This is a normalizer assertion; membership in \(\mathfrak h_p\) needs a further hypothesis.

**Proof.** Equation (E.2) gives \(\nabla_X A_X=R(X,X)=0\), so
\(P_t^{-1}(A_X)_{\gamma(t)}P_t=(A_X)_p\).
For \(v\in T_pM\), the variation \(\phi_t(c(s))\), where \(c'(0)=v\), has commuting parameter fields. Zero torsion gives
\[
D_t((d\phi_t)_pv)=\nabla_{(d\phi_t)_pv}X
=-(A_X)_{\gamma(t)}(d\phi_t)_pv.
\]
In the parallel frame this is \(C'_t=-(A_X)_p C_t\), \(C_0=I\). The linear ODE solution is (E.11).

Care is needed because the flow may not exist for a common time on the whole manifold. Fix one piecewise smooth based loop \(c\). Its compact image has a neighbourhood on which the flow is defined for all sufficiently small positive and negative times, by the open flow domain of [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and a finite subcover. Naturality of transport under a local isometry, [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), gives
\[
P_t^{-1}P_{\phi_t\circ c}P_t
 =C_tP_cC_t^{-1}
 =e^{-t(A_X)_p}P_ce^{t(A_X)_p}.
\tag{E.13}
\]
The left side is transport along a loop formed by the orbit from \(p\), the moved loop, and the reverse orbit. Sweeping \(c\) through the flow is a based homotopy after inserting these orbit segments; hence this new loop is homotopic to \(c\). Consequently, for this fixed \(c\) and all sufficiently small \(|t|\), the right side is in the same full-holonomy coset of restricted holonomy as \(P_c\).

Write \(H=\operatorname{Hol}_p\) and \(H^0=\operatorname{Hol}^0_p\). To prove (E.12), transport the restricted holonomy algebras to form a parallel subbundle \(\mathfrak h\subseteq\mathfrak{so}(TM,g)\). This is well defined: concatenating a path and its reverse identifies the two restricted holonomy groups by conjugation, and full holonomy normalizes restricted holonomy, by [Curvature and holonomy C.5](curvature-and-holonomy-groups.md#theorem-c-5). A radial parallel frame makes this family a smooth constant-rank subbundle; transport preserves it by construction, so its covariant derivatives stay in it by [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Curvature takes values in this bundle by [Curvature and holonomy G.3](curvature-and-holonomy-groups.md#theorem-g-3).

Equation (E.2) says \(\nabla A_X\) takes values in \(\mathfrak h\). Its next derivatives do too. The curvature action on an endomorphism, [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1), consequently gives
\[
[R(Y,Z),A_X]
=\nabla_Y\nabla_ZA_X-\nabla_Z\nabla_YA_X-\nabla_{[Y,Z]}A_X
\in\mathfrak h.
\tag{E.14}
\]
For any path from \(p\) to \(q\), integration of (E.2) in a parallel frame also gives
\[
P^{-1}(A_X)_qP-(A_X)_p\in\mathfrak h_p:
\]
the derivative of that transported matrix is in the fixed finite-dimensional subspace \(\mathfrak h_p\), and integrating each complementary coordinate gives zero. Conjugate (E.14) back along this path. Replacing \(P^{-1}(A_X)_qP\) by \((A_X)_p\) changes its commutator with \(P^{-1}R_q(Y,Z)P\) by an element of \(\mathfrak h_p\), since both the difference and the transported curvature are in that Lie algebra. The curvature-generation theorem, [Curvature and holonomy G.3](curvature-and-holonomy-groups.md#theorem-g-3), says these transported curvatures span \(\mathfrak h_p\). This proves (E.12). The linear ODE for conjugation now preserves \(\mathfrak h_p\) for every \(t\); exponential generation, as in E.3, proves that \(e^{t(A_X)_p}\) normalizes \(H^0\) for every \(t\).

Now fix any \(h=P_c\in H\). Formula (E.13) says, for a possibly \(h\)-dependent interval,
\[
e^{-tA}he^{tA}\in hH^0,\qquad A=(A_X)_p.
\]
Since conjugation by \(e^{tA}\) already preserves \(H^0\) for every \(t\), this condition is a homomorphism stabilizer condition for the coset \(hH^0\) under the additive group \(\mathbb R\). Its stabilizer contains an interval about zero, and therefore all of \(\mathbb R\), by writing any real number as a finite sum of numbers in that interval. Hence the same inclusion holds for every \(t\). This proves \(e^{-tA}He^{tA}\subseteq H\), and the opposite sign gives equality. □

## F. Integration and compact holonomy

Compact manifolds in Parts F–H have no boundary. No orientation is assumed.

**Lemma F.1 (Metric densities and integration by parts).** The local expressions
\[
d\mu_g=\sqrt{\det(g_{ij})}\,|dx^1\cdots dx^n|
\tag{F.1}
\]
define integration of continuous functions on a compact Riemannian manifold, independently of charts and subordinate partitions. With
\(\operatorname{div}Y=\operatorname{tr}(Z\mapsto\nabla_ZY)\),
\(\operatorname{grad}u\) defined by \(g(\operatorname{grad}u,Z)=du(Z)\), and
\(\Delta u=\operatorname{div}(\operatorname{grad}u)\), one has
\[
\int_M\operatorname{div}Y\,d\mu_g=0,\qquad
\int_Mu\Delta v\,d\mu_g
 =-\int_M g(\operatorname{grad}u,\operatorname{grad}v)\,d\mu_g.
\tag{F.2}
\]
A continuous nonnegative function with zero integral is identically zero.

**Proof.** We first supply the change-of-variables fact needed for (F.1). [DG-CHAR-17 A.1](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md#lemma-a-1) proves continuous compactly supported integration on Euclidean boxes, including iterated integration in any order. [DG-CHAR-17 A.2](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md#lemma-a-2) proves invertible linear and affine substitutions with the absolute determinant. The one-variable substitution for a smooth strictly monotone map with nonzero derivative follows from the fundamental theorem, [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations): apply the chain rule to a primitive and evaluate at the interval endpoints, reversing them for a negative derivative.

This proves substitution for a map changing only one coordinate,
\[
(x_1,\ldots,x_n)\longmapsto
(x_1,\ldots,x_{k-1},\psi(x),x_{k+1},\ldots,x_n),
\quad \partial_k\psi\ne0,
\]
on a box where that derivative has constant sign. For a function compactly supported inside the box, integrate first in \(x_k\). The one-variable formula applies on each fibre interval. Extend the transformed integrand by zero outside the image; it is continuous because the original support lies strictly inside the box and the map is a diffeomorphism. Its support is compact. A larger rectangle contains that support, so the iterated-integral theorem gives
\[
\int h(\Psi(x))|\det D\Psi(x)|\,dx=\int h(y)\,dy
\tag{F.3}
\]
for a continuous compactly supported \(h\) on this image. Partitions of unity from [Local tools 3.1](local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) extend this assertion to compact supports in any open domain on which such a coordinate-changing map is a diffeomorphism: cover the preimage support by finitely many smaller boxes and apply the proved formula to each summand.

Now let \(\Psi\) be any smooth diffeomorphism between open Euclidean sets. Near any fixed point, compose it with invertible affine maps so that \(D\Psi\) at that point is the identity. Define
\[
F_k(x)=(\Psi_1(x),\ldots,\Psi_k(x),x_{k+1},\ldots,x_n),
\quad 0\leq k\leq n.
\]
Here \(F_0\) is the identity, and every \(F_k\) has derivative the identity at the fixed point. The inverse function theorem, [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), makes all finitely many \(F_k\) diffeomorphisms on suitably small neighbourhoods. The transition \(F_kF_{k-1}^{-1}\) changes only coordinate \(k\), with a nonzero derivative there after shrinking. Thus \(\Psi\) locally factors into the coordinate-changing maps just treated and invertible affine maps. Compose their formulas; the chain rule and determinant multiplicativity, proved in [DG-CHAR-17 A.2](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md#lemma-a-2), give (F.3) for \(\Psi\) near the chosen point. For a general compact support, a finite subordinate partition reduces to these neighbourhoods. This proves the required nonlinear substitution, without an orientation hypothesis.

If \(x=x(y)\) is a change of coordinates, the metric matrices obey
\[
g_y=(Dx/Dy)^Tg_x(Dx/Dy),\qquad
\sqrt{\det g_y}=\sqrt{\det g_x}\,|\det(Dx/Dy)|.
\]
Thus (F.3) identifies the local integrals. Choose a finite smooth partition
\(\sum_j\rho_j=1\), with each support compact inside a coordinate chart, by [Local tools 3.1](local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) and compactness. Define the integral to be the sum of the coordinate integrals of \(\rho_j f\sqrt{\det g}\). Given a second such partition \((\sigma_k)\), insert \(1=\sum_k\sigma_k\) in each summand. On every overlap the change-of-variables formula identifies the integral of \(\rho_j\sigma_k f\) in either chart. Finite summation proves independence. Linearity and positivity follow from the same Euclidean properties. If \(f(p)>0\), continuity bounds \(f\) below by a positive constant on a small coordinate box around \(p\). Its positive smooth density is also bounded below on a still smaller closed box. A nonnegative cutoff supported there and positive on a smaller box, from [Local tools 3.1](local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support), then has a strictly positive integral against \(f\,d\mu_g\). Positivity and the partition definition imply \(\int f>0\). This proves the last assertion.

Write \(w=\sqrt{\det g}\) in a chart. Differentiating the determinant permutation sum in one column at a time gives
\(\partial_k\det g=(\det g)\operatorname{tr}(g^{-1}\partial_kg)\):
one can reduce to \(g=I\) by determinant multiplicativity, where only diagonal first-order entries contribute. Differentiating \(w^2=\det g\) consequently gives
\(w^{-1}\partial_kw=\tfrac12g^{ij}\partial_kg_{ij}\).
The Levi-Civita formula in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) gives
\(\Gamma^i_{ik}=\tfrac12g^{ij}\partial_kg_{ij}\); the other two Christoffel terms cancel on interchanging their summed indices. Therefore
\[
\operatorname{div}Y=\partial_iY^i+\Gamma^i_{ik}Y^k
=w^{-1}\partial_i(wY^i).
\tag{F.4}
\]
If \(Y\) has compact support inside this chart, integration of each derivative on a containing box is zero by the one-variable fundamental theorem and iterated integration. For a general smooth \(Y\), the product rule gives
\[
\sum_j\operatorname{div}(\rho_jY)
=\operatorname{div}Y+\sum_jd\rho_j(Y)
=\operatorname{div}Y.
\]
Each summand integrates to zero by the chart calculation. This proves the first formula in (F.2). Apply it to \(u\operatorname{grad}v\); its divergence is \(u\Delta v+du(\operatorname{grad}v)\), proving the second. Raising indices and its smoothness are proved in [Riemannian connections F.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-1). For dimension zero the formulas have empty sums and are immediate; the integral is the sum over the finitely many points. □

**Theorem F.2 (The compact holonomy restriction).** On a compact Riemannian manifold, every Killing field satisfies
\[
(A_X)_p\in\mathfrak h_p\qquad\text{at every }p,
\tag{F.5}
\]
where \(\mathfrak h_p\) is the restricted holonomy algebra.

**Proof.** Treat a connected component at a time; components are open, and compactness leaves only finitely many. The holonomy-algebra bundle \(\mathfrak h\) constructed in E.4 is parallel and contains the curvature values. On skew-adjoint endomorphisms use
\[
\langle A,B\rangle=-\operatorname{tr}(AB).
\]
In an orthonormal frame this is the sum of the products of corresponding matrix entries, since \(A^T=-A\); in particular it is positive definite. [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) shows it is parallel: trace is preserved by conjugation, and the product rule differentiates the pairing. The orthogonal complement \(\mathfrak h^\perp\) is therefore a smooth parallel subbundle. This can also be seen directly by transporting orthonormal bases of the two complementary subspaces in radial charts. Orthogonal projection onto either subbundle commutes with covariant differentiation, since transport preserves their orthogonal splitting.

Let \(B\) be the projection of \(A_X\) onto \(\mathfrak h^\perp\). Equation (E.2) takes values in \(\mathfrak h\); hence \(\nabla B=0\). The vector field \(BX\) then has divergence
\[
\begin{split}
\operatorname{div}(BX)
 &=\sum_i g\bigl(B\nabla_{e_i}X,e_i\bigr)
 =-\operatorname{tr}(BA_X)\\
 &=\langle B,A_X\rangle=|B|^2.
\end{split}
\tag{F.6}
\]
Here \((e_i)\) is any local orthonormal frame, and the last equality is the orthogonal decomposition defining \(B\). Lemma F.1 gives \(\int_M|B|^2d\mu_g=0\), hence \(B=0\). This is (F.5). □

## G. The identity component and parallel tensors

We use the topology of uniform convergence on compact sets on the isometry group. When \(M\) is compact this is uniform convergence on \(M\). The next proof supplies the group fact needed in the compact arguments.

**Lemma G.1 (Compact isometries are locally generated by Killing flows).** If \(M\) is compact and connected, its isometry group \(G\) is compact. Every isometry sufficiently close to the identity is a finite product of flows of globally defined Killing fields. Consequently the identity component \(G^0\) consists exactly of finite products of these flows. If \(\mathfrak i(M)=0\), then \(G\) is finite.

**Proof.** If \(M\) has dimension zero, connectedness makes it a single point and the assertions are immediate. Otherwise fix \(p\) and an orthonormal frame \(u:\mathbb R^n\to T_pM\). Define the one-jet map
\[
J:G\longrightarrow\operatorname O(M),\qquad J(f)=df_pu,
\tag{G.1}
\]
where the frame on the right is based at \(f(p)\), and \(\operatorname O(M)\) is the orthonormal frame bundle of [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2). It is compact by [Hopf–Rinow D.2](completeness-and-the-hopf-rinow-theorem.md#lemma-d-2). The map \(J\) is injective by A.1 and [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3).

We need a precise dependence assertion for these one-jets. On a normal neighbourhood \(V_0\) of \(p\), any isometry with pair \((q,L)\) has the formula
\[
f(x)=\exp_q\bigl(L\exp_p^{-1}x\bigr).
\tag{G.2}
\]
Compactness makes \(M\) complete by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Riemannian connections A.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-2), so [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) makes every target exponential defined on its whole tangent space. It is smooth by the finite-interval geodesic dependence in [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) and B.1.

For any point of \(M\), choose a path from \(p\) and a finite chain of small normal neighbourhoods along it. Such a chain exists by the coordinate-ball path argument of [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4) and compactness of the path interval. It can be chosen with the centre \(p_{j+1}\) of each next neighbourhood inside the preceding one: subdivide the path into sufficiently short pieces in a finite covering by convex normal sets from [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5). Starting with (G.2), recover \(f(p_{j+1})\) and \(df_{p_{j+1}}\) by evaluation and differentiation of the formula already obtained. On the next neighbourhood put
\[
f(x)=\exp_{f(p_{j+1})}
       \bigl(df_{p_{j+1}}\exp_{p_{j+1}}^{-1}x\bigr).
\tag{G.3}
\]
For actual isometries, A.1 proves this equality. For arbitrary initial frames \((q,L)\) near a prescribed frame, the same operations still define smooth maps on these source neighbourhoods: evaluate and differentiate a smooth family, and compose with the globally defined target exponential. Their intermediate derivatives need not be invertible for this construction. Repeating through the finite chain proves that the expression for \(f\) on its final neighbourhood depends smoothly on its initial frame. Compactness of \(M\) lets finitely many such final neighbourhoods cover \(M\); shrink to relatively compact coordinate sets covering \(M\) to obtain uniform control of any fixed derivative order.

It follows that if frames \(J(f_i)\) converge to any frame \(a\), the maps \(f_i\) converge smoothly on these finitely many neighbourhoods to maps defined by the preceding formulas at \(a\). On overlaps their values and derivatives agree, since they are limits of the same \(f_i\), so they form a smooth global map \(f\). This map preserves distance by passage to the limit. It also obeys \(f^*g=g\), by the convergence of first derivatives. It is onto: for each \(y\), compactness gives a subsequence of \(f_i^{-1}(y)\) converging to some \(x\). Uniform convergence and distance preservation give
\[
d(f(x),y)\leq d(f(x),f_i(x))+d(x,f_i^{-1}(y))\longrightarrow0.
\]
It is injective by distance preservation. Its isometric differential is invertible, and the inverse function theorem gives a smooth inverse. Thus \(f\in G\), with \(J(f)=a\). The subset \(J(G)\) is closed in the compact frame bundle: if a point lies in its closure, coordinate balls of radii tending to zero supply such a convergent sequence. Therefore \(J(G)\) is compact.

The inverse \(J(G)\to G\) is continuous by the same finite-chain formulas, which give uniform convergence from convergence of frames. The forward map is continuous too. Indeed choose sufficiently small \(\epsilon>0\) and put \(x_i=\exp_p(\epsilon u e_i)\). If \(f\) is near a fixed \(f_0\) uniformly, then \(q=f(p)\) and \(f(x_i)\) lie in a fixed small convex normal neighbourhood about \(f_0(p)\), after choosing \(\epsilon\) smaller first. The smooth logarithm in [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5) then gives
\[
df_pu e_i=\epsilon^{-1}\log_{f(p)}f(x_i).
\tag{G.4}
\]
To justify this choice uniformly, the endpoint inverse in that proof contains a product of a neighbourhood of \(f_0(p)\) and a fixed positive-radius tangent ball. The isometric vector \(\epsilon df_pu e_i\) is in that ball for this fixed small \(\epsilon\), so its exponential inverse is exactly the vector displayed. Formula (G.4) proves continuity from finitely many evaluations. Thus \(J\) is a homeomorphism onto \(J(G)\), proving compactness of \(G\). It also shows that convergence to an isometry in this topology gives smooth convergence locally, by (G.2)–(G.3).

Every smooth vector field on compact \(M\) is complete: the compact graph over a bounded time interval permits extension at each finite endpoint by the finite-chart continuation statement of [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Hence every Killing field has global isometric flows. By E.2 the space of such fields has finite dimension \(d\); choose a basis \(X_1,\ldots,X_d\). For \(a=(a_1,\ldots,a_d)\) near zero let
\[
\Phi_a=\phi^{X_1}_{a_1}\circ\cdots\circ\phi^{X_d}_{a_d}.
\tag{G.5}
\]
The differential at zero of \(a\mapsto J(\Phi_a)\) is injective. In fact the tangent to the frame \(d\phi^X_t|_p u\) has horizontal component \(X_p\) and vertical component \(\nabla X|_p=-A_X|_p\), relative to the Levi-Civita splitting of the frame tangent. This follows by differentiating the base point and the columns of the frame along the variation \(\phi^X_t(c(s))\), just as in E.4. E.2 says this pair can vanish only if \(X=0\). Denote the resulting \(d\)-dimensional subspace of \(T_u\operatorname O(M)\) by \(L\).

Choose a complement of \(L\) in that finite-dimensional tangent space, using [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), and a coordinate slice \(s\mapsto u(s)\) through \(u(0)=u\) with that complementary tangent space. An isometry acts smoothly on all frames by \(v\mapsto df_{\pi(v)}v\). Therefore
\[
(a,s)\longmapsto (\Phi_a)_*u(s)
\tag{G.6}
\]
has invertible derivative at \((0,0)\): its \(a\)-derivative is \(L\), and its \(s\)-derivative is the chosen complement. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes (G.6) a diffeomorphism between neighbourhoods of \((0,0)\) and \(u\).

We show that \(J(G)\) meets the slice sufficiently near \(u\) only at \(u\). Suppose the contrary. There would be isometries \(r_i\) with \(J(r_i)=u(s_i)\), \(s_i\ne0\), \(s_i\to0\). In fixed coordinates \(\xi\) on the frame bundle centred at \(u\), set
\[
t_i=|\xi(J(r_i))|>0.
\]
After taking a subsequence, \(\xi(J(r_i))/t_i\) converges to a unit vector \(w\) tangent to the slice, by compactness of the finite-dimensional unit sphere, [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

The finite-chain construction (G.2)–(G.3) gives, on each member of a finite source cover, a smooth family \(F(\xi,x)\) representing \(r_i(x)\) when \(\xi=\xi(J(r_i))\), and satisfying \(F(0,x)=x\). In target coordinates containing a smaller source set,
\[
\frac{F(\xi_i,x)-x}{t_i}
=\int_0^1 D_\xi F(s\xi_i,x)\frac{\xi_i}{t_i}\,ds
\longrightarrow D_\xi F(0,x)w
\tag{G.7}
\]
smoothly on compact subsets. The same formula after each finite number of \(x\)-derivatives proves the asserted smooth convergence, by uniform continuity of the next derivatives and the integral estimate of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). On overlapping charts the limits transform as a vector field: Taylor expansion of the coordinate change at \(x\) turns the difference quotient into its derivative applied to the original quotient, with remainder tending to zero. Thus these limits form a global smooth field \(X\).

Divide \(r_i^*g-g=0\) by \(t_i\) in each chart and pass to the limit using (G.7) and its first derivatives. The resulting equation is exactly the coordinate expression \(\mathcal L_Xg=0\) of E.1, so \(X\) is Killing. At \(p\), differentiation of (G.7) shows that its pair \((X_p,\nabla X|_p)\), viewed as a frame tangent, is \(w\). The derivative of the frame formula for the family \(F(\xi,\cdot)\) at \(p\) is the identity on initial frame coordinates, since (G.2) has exactly its prescribed value and differential there. Thus \(w\ne0\) gives \(X\ne0\). But every Killing field is a linear combination of the \(X_j\), so this tangent belongs to \(L\); it also belongs to its chosen complement. This contradicts its unit length.

Now take \(f\in G\) sufficiently close to the identity and use (G.6) to write \(J(f)=(\Phi_a)_*u(s)\). Then \(r=\Phi_a^{-1}f\) has \(J(r)=u(s)\). Shrinking the neighbourhood makes \(r\) close enough to the identity for the slice conclusion. Hence \(J(r)=u\), and injectivity of \(J\) gives \(r=\operatorname{id}\). Thus \(f=\Phi_a\). If \(d=0\), the same argument has no \(a\)-variables and proves that the identity itself is an open point.

Let \(K\) be the subgroup generated by all the Killing flows. The preceding neighbourhood is contained in \(K\), so \(K\) is open, and its other cosets are open. Multiplication and inversion are continuous for the uniform topology: for isometries,
\[
\begin{split}
d(f_i g_i x,fgx)&\leq d(g_i x,gx)+d(f_i gx,fgx),\\
d(f_i^{-1}y,f^{-1}y)&=d(y,f_i f^{-1}y).
\end{split}
\]
Suprema on compact \(M\) prove the claim. Consequently the connected component of the identity lies in the open-and-closed subgroup \(K\). Conversely each finite product of flow maps is joined to the identity by varying its finitely many time parameters along straight segments, a continuous path in \(G\). Thus \(K=G^0\). When \(d=0\), translations make every group point open; compactness then makes this discrete group finite, since its open cover by singletons has a finite subcover. □

**Theorem G.2 (Parallel tensors and compact isotropy).** On a compact connected Riemannian manifold, every isometry in \(G^0\) preserves every globally defined parallel tensor. If \(f\in G^0\) fixes \(p\), then
\[
df_p\in\operatorname{Hol}_p.
\tag{G.8}
\]
The assertion concerns full holonomy; the path traced by \(p\) under a product of flows need not be contractible.

**Proof.** For a Killing field, F.2 gives \(A_X\in\mathfrak h\). If \(S\) is parallel, its value at \(p\) is fixed by full holonomy, [Reduction and the holonomy theorem A.3](reduction-and-the-holonomy-theorem.md#theorem-a-3), applied to the tensor representation whose transport is constructed in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). In particular it is fixed by \(\exp(-t(A_X)_p)\). Formula (E.11) says
\[
(d\phi_t)_p=P_t\exp(-t(A_X)_p).
\tag{G.9}
\]
Both factors therefore carry \(S_p\) to \(S_{\phi_t(p)}\): the exponential fixes its initial tensor value, and parallel transport carries it to the endpoint. This includes contravariant and covariant slots, using the dual and tensor transport rules in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1). Thus every Killing flow preserves \(S\); G.1 gives the assertion for every element of \(G^0\).

For the isotropy assertion write \(f\) as a finite product of these flow maps. Follow \(p\) through the successive orbit segments, whose concatenation is a path \(\alpha:p\to f(p)\). For each segment its differential is its parallel transport followed by an element of restricted holonomy at its starting point, by (G.9) and exponential generation. Transport conjugates restricted holonomy at the endpoints, [Curvature and holonomy C.5](curvature-and-holonomy-groups.md#theorem-c-5). Successive multiplication therefore gives
\[
df_p=P_\alpha h,\qquad h\in\operatorname{Hol}^0_p.
\tag{G.10}
\]
For example, in multiplying two factors, move the second restricted-holonomy factor to the initial point by conjugating with the first transport; induction handles any finite number. If \(f(p)=p\), the path \(\alpha\) is a loop, so \(P_\alpha\in\operatorname{Hol}_p\). Equation (G.10) proves (G.8). □

## H. Ricci curvature and the surviving global fields

**Theorem H.1 (The Killing identity and the compact Ricci conclusion).** For a Killing field on a Riemannian manifold, with the scalar Laplacian convention of F.1,
\[
\frac12\Delta |X|^2=|\nabla X|^2-\operatorname{Ric}(X,X).
\tag{H.1}
\]
If \(M\) is compact and connected and \(\operatorname{Ric}\leq0\), every Killing field is parallel. In that case
\[
\dim\mathfrak i(M)
=\dim (T_pM)^{\operatorname{Hol}_p}.
\tag{H.2}
\]
If Ricci is negative definite at even one point, every Killing field vanishes and the full isometry group is finite.

**Proof.** Choose a normal orthonormal basis at the point of calculation, so its first covariant derivatives vanish there; [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) and [Riemannian connections F.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-3) supply these normal coordinates. Differentiate \(\nabla_YX=-A_XY\), subtracting the derivative of the input \(Y\). Equation (E.2) gives the tensor identity
\[
\nabla^2_{Y,Z}X=-R(X,Y)Z.
\tag{H.3}
\]
Taking its metric trace yields
\[
\operatorname{tr}_g\nabla^2X=-\sum_iR(X,e_i)e_i
=-\operatorname{Ric}^{\sharp}X.
\tag{H.4}
\]
For the last equality, pair the sum with \(W\). Curvature is skew in its first two slots and in its endomorphism slots, so
\[
\sum_i g(R(X,e_i)e_i,W)
=\sum_i g(R(e_i,X)W,e_i)=\operatorname{Ric}(X,W).
\]
The Ricci definition and these symmetries are established in [Sectional curvature A.1–A.2](sectional-curvature-and-space-forms.md#theorem-a-1). Metric compatibility and two applications of the product rule now give
\[
\frac12\Delta |X|^2
=\sum_i g(\nabla_{e_i}X,\nabla_{e_i}X)
 +g(\operatorname{tr}_g\nabla^2X,X),
\]
which proves (H.1). This proof concerns the scalar Laplacian with sign
\(\Delta=\operatorname{div}\operatorname{grad}\); no sign convention for a Hodge Laplacian is being imported.

On a compact manifold F.1 applied to \(\operatorname{grad}(|X|^2/2)\) gives
\[
\int_M|\nabla X|^2\,d\mu_g
=\int_M\operatorname{Ric}(X,X)\,d\mu_g.
\tag{H.5}
\]
If Ricci is nonpositive, the left side is nonnegative and the right side nonpositive; equality makes both zero. The positive-integral assertion of F.1 makes \(\nabla X=0\) everywhere. Conversely every parallel field satisfies the Killing equation (E.3). [Reduction and the holonomy theorem A.3](reduction-and-the-holonomy-theorem.md#theorem-a-3) identifies all parallel vector fields with the vectors fixed by full tangent holonomy, giving (H.2). At a point where Ricci is negative definite, (H.1) for a parallel field gives \(0=-\operatorname{Ric}(X,X)\), so \(X\) vanishes there. Parallel transport then makes it zero on connected \(M\). Lemma G.1 proves finiteness of the isometry group; this conclusion does not rely on an external Lie-group theorem. □

**Exercise H.2 (Hyperbolic surfaces, tori and the Klein bottle).** Apply the preceding results to a compact connected surface of constant curvature \(-1\), allowing it to be nonorientable. Determine the Killing algebras of a flat torus and of the flat Klein bottle generated on \(\mathbb R^2\) by
\[
a(x,y)=(x+1,y),\qquad b(x,y)=(-x,y+1).
\tag{H.6}
\]
Explain why local rotations on a flat torus need not extend, despite trivial tangent holonomy, and distinguish the normalizer assertion E.4 from the compact restriction F.2.

**Solution.** On a surface of curvature \(-1\), the constant-curvature formula of [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) gives \(\operatorname{Ric}=-g\). Thus H.1 makes every global Killing field zero and the isometry group finite. Orientation did not occur in F.1, G.1 or H.1, so this includes nonorientable surfaces.

Every sufficiently small neighbourhood of such a surface is isometric to a neighbourhood in the hyperbolic plane: [Sectional curvature B.3](sectional-curvature-and-space-forms.md#theorem-b-3) gives the same normal-coordinate metric for equal constant curvature, and [Sectional curvature C.4](sectional-curvature-and-space-forms.md#exercise-c-4) identifies the negative model with the upper half-plane
\[
\{(x,y):y>0\},\qquad g=y^{-2}(dx^2+dy^2).
\]
The translations \((x,y)\mapsto(x+t,y)\) preserve this metric and give the nonzero Killing field \(\partial_x\). Restricting it and transferring it by the local isometry produces nonzero local Killing fields on the surface, none of which can extend globally. These can be regarded as analytic fields in the hyperbolic normal-coordinate atlas. More explicitly, the constant-curvature tensor is parallel, so C.1 makes the normal atlas analytic; its radial coframe is analytic by the same proof, and the metric has the analytic expression \(g=\sum_i\alpha_i^2\). E.3 then makes each local Killing field analytic. The hyperbolic plane itself is noncompact and has the displayed global fields; the compact integration argument does not apply to it. The simply connected extension theorem E.3 is consistent with these examples: the compact hyperbolic surface cannot be simply connected, since otherwise it would extend the nonzero local field that H.1 excludes globally.

For the flat torus \(T^n=\mathbb R^n/\Lambda\), where a full lattice \(\Lambda\) spans \(\mathbb R^n\), parallel transport has trivial tangent holonomy, as computed in [Curvature and holonomy D.3](curvature-and-holonomy-groups.md#example-d-3). It is compact and flat, hence has zero Ricci curvature. Equation (H.2) gives
\(\dim\mathfrak i(T^n)=n\), and its fields are exactly the descended constant vector fields. Indeed a parallel field lifts to a constant vector field in Euclidean coordinates, and every such vector field is translation invariant and descends.

The obstruction for rotations is visible in the Killing connection itself. On Euclidean space \(R=0\); along a lifted path starting at \(x_0\), the equations \(D(v,A)=0\) reduce to
\[
A(t)=A_0,\qquad v(t)=v_0-A_0(x(t)-x_0).
\tag{H.7}
\]
A torus loop lifting from \(x_0\) to \(x_0+\lambda\) therefore has Killing-pair monodromy
\[
(v_0,A_0)\longmapsto(v_0-A_0\lambda,A_0).
\tag{H.8}
\]
The endpoint tangent identifications are the identity because the deck transformation is a translation. To be fixed for all lattice vectors requires \(A_0\lambda=0\) for all \(\lambda\), hence \(A_0=0\). When \(n\geq2\), choose a nonzero skew matrix \(B\). The Euclidean field \(X(x)=B(x-x_0)\) is Killing by E.3 and has \(A_X=-B\). Its restriction to a small torus chart is an analytic local Killing field but violates (H.8), so it cannot extend. For \(n=1\) there is no nonzero skew matrix and no such rotation example. Trivial tangent holonomy thus does not assert trivial holonomy of the different connection \(D\) on \(\mathcal E\).

For (H.6), \(bab^{-1}=a^{-1}\), and every deck transformation has the form
\[
a^m b^k(x,y)=((-1)^k x+m,y+k),\qquad m,k\in\mathbb Z.
\tag{H.9}
\]
Existence of this form follows by moving each \(a\) past each \(b\) using the displayed relation; uniqueness follows by comparing the \(y\)-translation, then the \(x\)-translation. A nonidentity element has no fixed point: if \(k\ne0\) it changes \(y\), and if \(k=0\), \(m\ne0\) changes \(x\). Only finitely many translates of one compact set can meet another, since the \(y\) coordinates bound \(k\) and then the \(x\) coordinates bound \(m\). Thus the action is free and properly discontinuous. The quotient and its smooth flat metric are supplied by the quotient construction in [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3); the explicit classification of this quotient is also in [Sectional curvature T.1](sectional-curvature-and-space-forms.md#theorem-t-1). Every orbit has a representative in \([0,1]\times[0,1]\), by first moving its \(y\) coordinate with a power of \(b\), then its \(x\) coordinate with a power of \(a\). Therefore the quotient is compact. The orientation-reversing derivative of \(b\) gives its nonorientability: an orientation lifted to the connected plane would have to be preserved by every deck transformation, which this one cannot do.

Along a lifted Euclidean path parallel vectors have constant coordinate columns. Closing it downstairs identifies its endpoint with the initial point by the inverse deck differential. Formula (H.9) therefore gives
\[
\operatorname{Hol}_p
=\{I,\operatorname{diag}(-1,1)\}.
\tag{H.10}
\]
Both values occur, using paths from a point to its translates by \(a\) and \(b\). The fixed subspace is the vertical line, so (H.2) gives dimension one, generated by the descended field \(\partial_y\). Restricted holonomy is trivial, because the connection is flat and contractible loops lift closed in the plane, as in [Flat connections E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1). Using only restricted holonomy would incorrectly give dimension two.

Finally, on noncompact Euclidean space the global rotation field \(X(x)=Bx\) has \(A_X=-B\ne0\), while its holonomy algebra is zero. Its exponentials normalize the trivial holonomy group, as E.4 asserts, but \(A_X\) does not belong to that algebra. This exhibits the role of compactness in F.2. On the compact flat torus, G.1 and the constant-field computation make \(G^0\) the translations; a translation fixing a point is the identity, in agreement with G.2. The isometry \(x+\Lambda\mapsto -x+\Lambda\), for \(n\geq1\), fixes the origin and has derivative \(-I\), outside the trivial full holonomy. It is therefore outside \(G^0\). This proves that the identity-component hypothesis in the compact isotropy statement cannot be dropped. □

## Freely accessible sources

- Jonatan Herrera, Miguel Angel Javaloyes and Paolo Piccione, *On a monodromy theorem for sheaves of local fields and applications*, [arXiv:1507.03635v1](https://arxiv.org/pdf/1507.03635v1), 12 July 2015, §2. The germ-continuation method informs Part A. The proof above establishes its covering and lifting conditions for affine maps, including maps of arbitrary rank.
- Zuoqin Wang, *Riemannian Geometry*, course notes prepared by Xumin Liang, [free author-hosted notes](https://xumin.net/c/files/riemannian_geometry.pdf), §5.2.2, Theorem 5.19 and its proof (PDF pages 122–123). This explains comparison through radial parallel frames in the metric case. Part B derives the nonsingular frame equations for arbitrary torsion and proves the affine equivalence criterion.

- Olivier Biquard, *An introduction to geometric analysis*, 2 December 2025, [free author-hosted notes](https://webusers.imj-prg.fr/~olivier.biquard/iag2025.pdf), §§11–14 and §16 (PDF pages 25–31 and 35–36). The connection identities and the Killing/Ricci calculation inform Parts E and H. The full Killing connection, its curvature, the analytic jet criterion, density integration without orientation, the compact holonomy restriction and the isometry-component argument are proved here from exact programme prerequisites. No external isometry-group, Hodge-theoretic or onward-reference assertion supplies a proof.

The analytic power-series and parameter-dependent ODE proofs used here are in [Curvature and holonomy I.1](curvature-and-holonomy-groups.md#lemma-i-1). The construction and uniqueness of geodesics, and convex normal neighbourhoods for connections with torsion, are in [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1), [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) and [Geodesics B.3](geodesics-normal-coordinates-and-curvature.md#theorem-b-3). The structure equations used in Part B are proved in [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) and [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1).
