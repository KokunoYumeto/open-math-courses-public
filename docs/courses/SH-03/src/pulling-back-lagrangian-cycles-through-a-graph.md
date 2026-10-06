# Pulling back Lagrangian cycles through a graph

A cotangent inverse image needs a map between dualizing coefficients, as well as an image of its carrier. The map comes from comparing a graph with a diagonal. Its adjoint is an isomorphism even when the derivative changes rank. Properness is a separate condition on the carrier to which the operation is applied.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Use Lagrangian cycles and proper cotangent images for the sheaf \(\mathcal L_X\), its coefficient \(E_X=\pi_X^{-1}\omega_X\), relative orientation and the direct image. Isotropic cotangent transport and discrete critical values supplies the geometric transport theorem. Our exact current SH-02 prerequisites are the graph-supported microlocalization formula, the two microlocal functorial squares and their specified adjunction compatibility, with their ordered orientation extraction.

This lesson treats inverse images of Lagrangian cycles through a graph, in the framework of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). We retain a general commutative coefficient ring \(A\) of finite global dimension. Manifolds are real analytic, Hausdorff and countable at infinity, with uniformly bounded finite dimensions.

## The two cotangent properness conditions are different

Let \(f:Y\to X\), with \(\dim Y=m\), \(\dim X=n\). Its cotangent correspondence is

\[
 \begin{gathered}
 C_f=Y\times_XT^*X,\qquad \pi:C_f\to Y,\\
 f_\pi(y;\xi)=(f(y);\xi),\qquad
 f_d(y;\xi)=(y;df_y^t\xi).
 \end{gathered}
 \qquad\text{(1)}
\]

For a closed conic subanalytic isotropic \(\Lambda_X\subset T^*X\), inverse image assumes

\[
 f_d\text{ proper on }B_f=f_\pi^{-1}\Lambda_X.
 \qquad\text{(2)}
\]

Its carrier is \(\Lambda_Y'=f_d(B_f)\). The geometric transport theorem makes this closed, conic, subanalytic and isotropic. Direct image instead assumes \(f_\pi\) proper on \(f_d^{-1}\Lambda_Y\). The domains and the maps in those two tests cannot be exchanged.

Here is a useful complete test for (2). For a closed positive-conic \(\Lambda_X\),

\[
 f_d|_{B_f}\text{ is proper}
 \quad\Longleftrightarrow\quad
 \bigl((f(y);\xi)\in\Lambda_X, df_y^t\xi=0\bigr)
                   \Longrightarrow\xi=0.
 \qquad\text{(3)}
\]

This is the noncharacteristic condition for this closed carrier, with zero covectors retained.

**Proof.** A nonzero killed covector gives the unbounded ray
\((y;t\xi)\), \(t>0\), in the inverse image of the single target point \((y;0)\). That fibre is not compact, so properness fails.

Conversely fix a compact set of base points \(K\subset Y\), and choose continuous bundle norms near \(K\) and \(f(K)\). There is a constant \(c_K>0\) such that

\[
 \|df_y^t\xi\|\geq c_K\|\xi\|
 \quad(y\in K,\ (f(y);\xi)\in\Lambda_X).
 \qquad\text{(4)}
\]

If not, normalize offending covectors to length one. The unit sphere bundle over the compact \(f(K)\), together with \(y\in K\), is compact. A subsequence converges to \((y;\xi)\) with \(\|\xi\|=1\), still in the closed pulled-back carrier, and with \(df_y^t\xi=0\). This contradicts the right side of (3). If there are no nonzero covectors over these points, (4) holds vacuously.

For a compact \(Q\subset T^*Y\), its base projection is such a \(K\), and its covector norms are bounded. Inequality (4) bounds every \(\xi\) in \((f_d|_{B_f})^{-1}Q\). A bounded disk bundle over compact \(K\) is compact. The inverse image is closed in it, by closedness of \(\Lambda_X,Q\) and continuity of the maps. It is therefore compact. \(\square\)

Neither constant rank of \(df\) nor properness of the base map \(f\) was used. The quantitative bound is uniform on compact base sets; it is not a global positive lower bound over a noncompact \(Y\).

## A graph turns the transpose derivative into a conormal map

Set

\[
 \begin{gathered}
 Z=Y\times Y,\qquad W=Y\times X,\qquad
 F_1=\operatorname{id}_Y\times f:Z\to W,\\
 \delta_Y(y)=(y,y),\qquad \delta_f(y)=(y,f(y)),\\
 N=\Delta_Y\subset Z,\qquad M=\Gamma_f\subset W.
 \end{gathered}
 \qquad\text{(5)}
\]

Both embeddings are closed. The restriction \(N\to M\) is the identity on their shared parameter \(Y\). Thus the center map is a diffeomorphism, even if the ambient map \(F_1\) is singular.

Identify the graph and diagonal conormals by

\[
 \begin{aligned}
 C_f&\simeq T^*_MW,
 &(y;\xi)&\longmapsto(y,f(y);-df_y^t\xi,\xi),\\
 T^*Y&\simeq T^*_NZ,
 &(y;\eta)&\longmapsto(y,y;-\eta,\eta).
 \end{aligned}
 \qquad\text{(6)}
\]

The transpose of \(dF_1\) takes the first covector to
\((-df_y^t\xi,df_y^t\xi)\). Hence the conormal transpose map is precisely \(r=f_d\), while the conormal base-change map \(s\) is the identity on \(C_f\). The minus signs in (6) express annihilation of graph tangents; they do not insert an antipode into \(f_d\).

On normal vectors use the differences \(v_2-v_1\) for the diagonal and \(v_X-df(v_Y)\) for the graph. The induced normal map is \(v\mapsto df(v)\). Its relative invertible line is

\[
 P=\omega_{Y/X}=\omega_Y\otimes(f^{-1}\omega_X)^{-1},
 \qquad L=\pi^{-1}P,
 \qquad\omega_r=L^{-1}.
 \qquad\text{(7)}
\]

The shift of \(P\) is \(m-n\). These identities use the actual ordered exceptional transitivity and inverse pairing. In particular the inverse in (7) reverses the shift as well as the orientation ratio. It remains valid at points where the rank of \(df\) changes.

## Construct the coefficient arrow before using a carrier

Put \(K=f^{-1}\omega_X\) on \(Y\), and \(\mathscr F=\delta_{f*}K\) on \(W\). Microlocalization of a coefficient supported on its smooth center has the actual natural identification

\[
 \mu_M\mathscr F\simeq\pi^{-1}K.
 \qquad\text{(8)}
\]

It follows by specialization to the zero normal vector and Fourier transformation of that zero-vector support. There is no additional shift: the Fourier correspondence restricted to the zero normal vector projects identically to the dual bundle.

Apply the upper ordinary-inverse microlocal comparison for the pair map \(F_1:(Z,N)\to(W,M)\). The center map is the identity, so its relative line is the unit. This gives

\[
 Rf_{d!}\pi^{-1}K
    \longrightarrow
 \mu_N(\omega_{F_1}\otimes F_1^{-1}\mathscr F).
 \qquad\text{(9)}
\]

The second arrow is restriction to the diagonal. More precisely the ordinary embedding adjunction gives
\(F_1^{-1}\mathscr F\to\delta_{Y*}\delta_Y^{-1}F_1^{-1}\mathscr F
=\delta_{Y*}K\).
The projection formula and
\(\delta_Y^{-1}\omega_{F_1}=P\) then give

\[
 \omega_{F_1}\otimes F_1^{-1}\mathscr F
       \longrightarrow\delta_{Y*}(P\otimes K)
       \simeq\delta_{Y*}\omega_Y.
 \qquad\text{(10)}
\]

Apply \(\mu_N\) and the center-supported formula (8) for the diagonal. The composite is the coefficient map

\[
 \rho_f:Rf_{d!}\pi^{-1}f^{-1}\omega_X
                   \longrightarrow\pi_Y^{-1}\omega_Y=E_Y.
 \qquad\text{(11)}
\]

The restriction in (10) is an arrow. The preimage of the graph under \(F_1\) can be larger than the diagonal, so there is no general ordinary inverse-image equality of their supported sheaves. Exercise 1 exhibits this issue at a critical point.

Formula (11) is constructed for every analytic \(f\), before any properness assumption on a cycle carrier. The analytic hypotheses provide finite-dimensional bounded operations; \(P,K\) are bounded invertible orientation complexes. The map is the specified microlocal comparison followed by the specified restriction and relative dualizing pairing.

## The actual adjoint is an isomorphism

Let

\[
 \beta_f:\pi^{-1}f^{-1}\omega_X
                       \longrightarrow f_d^!E_Y
 \qquad\text{(12)}
\]

be the \(Rf_{d!}\dashv f_d^!\) adjoint of (11). We prove that this particular arrow is an isomorphism.

Take \(\mathscr G=\delta_{Y*}K\) on \(Z\). Its support lies on \(N\), and
\(RF_{1*}\mathscr G=\delta_{f*}K=\mathscr F\).
The ordinary direct microlocal comparison is

\[
 d_{\mathscr G}:\mu_M(RF_{1*}\mathscr G)
       \longrightarrow r^!(\mu_N\mathscr G)\otimes L.
 \qquad\text{(13)}
\]

This arrow is an isomorphism by the full supported direct-comparison theorem. Here are its three hypotheses in this situation. The ambient map is proper on \(\operatorname{supp}\mathscr G\subset N\), since it is the closed graph identification there. The normal cone of that support along \(N\) is contained in the zero normal section, and its normal map to the graph bundle is proper on that section, again by the identity on \(Y\). Finally
\(\operatorname{supp}\mathscr G\cap F_1^{-1}M\subset N\).
None of these tests assumes that \(df\) is injective or surjective.

To identify (13) with (12), retain the adjunction maps. In the conormal correspondence put

\[
 \mathcal D(H)=Rr_!(L^{-1}\otimes H),\qquad
 \mathcal C(J)=r^!J\otimes L.
 \qquad\text{(14)}
\]

They are adjoint. The exact microlocal adjunction identity says that (13) is

\[
 \mu_M\mathscr F
 \xrightarrow{\eta_{\mathcal D}}
 \mathcal C\mathcal D\mu_M\mathscr F
 \xrightarrow{\mathcal C\widetilde c_{\mathscr F}}
 \mathcal C\mu_NF_1^{-1}\mathscr F
 \xrightarrow{\mathcal C\mu_N\varepsilon'}
 \mathcal C\mu_N\mathscr G.
 \qquad\text{(15)}
\]

Here \(\widetilde c\) is the orientation-canceled upper inverse comparison, and \(\varepsilon':F_1^{-1}RF_{1*}\mathscr G\to\mathscr G\) is the ordinary counit. In this graph situation \(\varepsilon'\) is exactly the restriction to the diagonal used in (10).

Now \(\mu_N\mathscr G=\pi_Y^{-1}K\). The right-tensor extraction of the relative line identifies

\[
 r^!(\pi_Y^{-1}K)\otimes L
     \simeq r^!(\pi_Y^{-1}(K\otimes P))
     \simeq r^!E_Y.
 \qquad\text{(16)}
\]

The first is the exceptional projection comparison for the bounded invertible base line \(P\); the second uses the graded symmetry from \(K\otimes P\) to \(P\otimes K\), then the actual pairing in (10). Under (16), (15) is the adjoint of (9) followed by (10). Indeed transposing its unit gives the evaluation for (14); reinserting its inverse line recovers the upper map (9), and its last counit is (10). The two reorderings are those in the right-tensor microlocal exchange convention, including the graded symmetry. This is the exact adjunction compatibility of the current SH-02 comparison, not a new choice of orientation isomorphism.

Thus \(\beta_f\) is (13) under the actual identifications (8),(16). Since (13) is an isomorphism, so is (12). This proof allows changing rank and nonproper \(f\). It does not assert that \(\rho_f\) itself is an isomorphism: an adjunction counit can fail to be one when its adjoint is invertible.

## Supported inverse images and fundamental cycles

Under (2), the operation on a cycle is the composite

\[
 \begin{aligned}
 H^0_{\Lambda_X}(T^*X;E_X)
 &\longrightarrow H^0_{B_f}(C_f;\pi^{-1}f^{-1}\omega_X)\\
 &\longrightarrow
 H^0_{\Lambda_Y'}(T^*Y;Rf_{d!}\pi^{-1}f^{-1}\omega_X)\\
 &\xrightarrow{\rho_f}
 H^0_{\Lambda_Y'}(T^*Y;E_Y).
 \end{aligned}
 \qquad\text{(17)}
\]

The first arrow is supported inverse image under \(f_\pi\). The second uses properness of \(f_d\) on the closed \(B_f\): ordinary and proper image agree on its supported object. The last is the actual coefficient map (11). The output carrier is allowed in \(\mathcal L_Y\), so (17) defines \(f^*\). For the identity map, the graph and diagonal coincide and all comparisons and counits are identities; hence \(f^*\) is the identity. Enlarging a carrier preserves the map whenever (2) remains valid.

For a point, \(\mathcal L_{\mathrm{pt}}=A\) and its fundamental cycle \([\mathrm{pt}]\) is \(1\). For \(a_X:X\to\mathrm{pt}\), the incidence is \(X\) and its map to \(T^*X\) is the closed zero embedding \(z_X\). It is proper even when \(X\) is noncompact. Define

\[
 [T_X^*X]=a_X^*[\mathrm{pt}].
 \qquad\text{(18)}
\]

It is a generator of the twisted zero-section cycle coefficient. To see this, (12) for \(a_X\) is the actual isomorphism
\(A_X\to z_X^!E_X\). Adjunction identifies the class (18) with its image of \(1\). The supported smooth-cycle coefficient is
\(\operatorname{or}_X\otimes B_X|_X\), whose integral square pairing makes it a rank-one constant line. Thus (18) fixes its generator by the actual map \(\beta_{a_X}\); a coordinate description must use that ordered dualizing normalization.

If \(i:Y\hookrightarrow X\) is a closed analytic submanifold, \(i_\pi\) is a closed embedding, and
\(i_d^{-1}(T_Y^*Y)=T_Y^*X\) in its incidence. The direct operation is therefore defined. Set

\[
 [T_Y^*X]=i_*[T_Y^*Y].
 \qquad\text{(19)}
\]

This defines the normalized conormal cycle with its relative cotangent orientation coefficient. Locally take coordinates \((u,z)\) with \(Y=\{z=0\}\). Its carrier has coordinates \((u;\zeta)\), with the tangent covector \(\xi_u=0\). Pulling back the zero-section class keeps its Thom class in the \(\xi_u\) directions. The subsequent closed embedding uses the actual \(i^!\omega_X=\omega_Y\) trace in the \(z\) directions. In this product chart the smooth vertical base change identifies \(i_\pi^!E_X\) with \(\pi^{-1}\omega_Y\): the normal costalk of the \(z=0\) embedding is its orientation line shifted by minus its codimension, canceling the same factor of \(\omega_X\). Thus the induced rank-one supported coefficient map is an isomorphism, and (19) is a generator locally. The closed trace and (18) specify its normalization on overlaps, including nonorientable ones.

The formula for transverse inverse images of these normalized conormal cycles needs its own comparison of the two constructions. We have not inferred that formula merely from equality of their carrier sets.

## Exercises with complete solutions

### A graph preimage can contain an extra branch

*Difficulty: Advanced.*

Take \(f:\mathbb R_t\to\mathbb R_x\), \(f(t)=t^2\). Compute (6) and the preimage of \(\Gamma_f\) under \(F_1(s,t)=(s,t^2)\). Explain why (10) must be a restriction arrow.

**Solution.** A graph covector at \((s,s^2)\) is
\((-2s\xi,\xi)\). At a point of the diagonal, the transpose of \(dF_1\) gives \((-2s\xi,2s\xi)\), so the diagonal coordinate is \(\eta=2s\xi\). This is the positive transpose \(f_d\), with no additional sign.

The preimage condition is \(t^2=s^2\). It contains both \(t=s\) and \(t=-s\), crossing at the origin. Near a point of the antidiagonal away from zero, the ordinary inverse image of a nonzero coefficient supported on \(\Gamma_f\) is nonzero while a coefficient supported on \(\Delta_Y\) has zero stalk. Thus these two sheaves are not equal. The embedding counit restricts the preimage sheaf to the diagonal and discards that other branch. At the origin the branches meet, but the same natural restriction still exists. The microlocal construction uses that arrow and does not require the ambient map to be noncharacteristic for the graph sheaf.

### Properness is a compact uniform estimate

*Difficulty: Intermediate.*

Explain every compactness step in (3)–(4). Then give a map for which a uniform positive bound exists on every compact base set but no global positive bound exists, while cotangent inverse image is still proper.

**Solution.** Closedness of \(\Lambda_X\) retains the limit of normalized covectors. Positive conicity permits normalization. The base coordinates lie in compact \(K\); the covectors lie in the unit sphere over compact \(f(K)\). Hence a subsequence converges jointly. The assumed failure of (4) would kill a nonzero limit covector. For a compact target \(Q\), its base projection is compact and its fibre norms are bounded; (4) then puts the preimage in a compact disk bundle. Its closedness makes it compact, which is exactly properness.

Take \(f(t)=\arctan t\) and \(\Lambda_X=T^*\mathbb R\). The derivative is \(1/(1+t^2)>0\), so
\(f_d(t;\xi)=(t;\xi/(1+t^2))\) is a homeomorphism from the incidence to \(T^*\mathbb R_t\), with inverse \((t;\eta)\mapsto(t;(1+t^2)\eta)\). It is proper. On \([-R,R]\), (4) holds with \(c_K=1/(1+R^2)\), whereas these constants approach zero as \(R\to\infty\). The full cotangent carrier here is used only to test properness; it is not isotropic and is not declared an allowed Lagrangian carrier.

### The critical fibre of a ramified map fails the test

*Difficulty: Intermediate.*

For \(f(t)=t^2\), compare inverse image of the full cotangent fibre over \(x=0\) with that over \(x=1\). Compute the image carriers and verify or disprove properness directly.

**Solution.** Over zero, \(B_f=\{t=0,\xi\in\mathbb R\}\), and
\(f_d(0;\xi)=(0;0)\). A whole noncompact line maps to one point. The inverse cycle operation on this carrier is undefined by (2), although its set image is a single zero covector.

Over one, \(B_f\) has two components \(t=1\) and \(t=-1\), with unrestricted \(\xi\). On them the covector maps are \(\xi\mapsto2\xi\) and \(\xi\mapsto-2\xi\). Each is a homeomorphism onto the cotangent fibre at its base point. A compact target has compact inverse image in each of these two components, and a finite union of compact sets is compact. The map is proper, with image the two full cotangent fibres. They are closed conic isotropic carriers of dimension one. This calculation verifies the operation's domain and carrier; it does not substitute a set calculation for its coefficient map.

### A nonproper base projection has a proper cotangent inverse image

*Difficulty: Advanced.*

Let \(f:\mathbb R^2_{u,v}\to\mathbb R_x\), \(f(u,v)=u\), and let \(\Lambda_X=T^*_{\{0\}}\mathbb R\). Compute (2) and its dimension shifts. Compare the map \(f_\pi\) on this same incidence subset.

**Solution.** The pulled-back carrier is
\(B_f=\{u=0,v\in\mathbb R,\xi\in\mathbb R\}\), and
\(f_d(0,v;\xi)=(0,v;\xi,0)\). It is a homeomorphism onto the closed conormal of \(\{u=0\}\subset\mathbb R^2\), hence proper as a map to \(T^*\mathbb R^2\). Compact inverse images are compact even though the \(v\) coordinate is globally unbounded. The base map is nonproper, but the inverse cycle operation is defined.

Here \(m=2,n=1\), so \(P\) has shift \([1]\), \(L^{-1}\) has shift \([-1]\), and \(f_d\) is the codimension-one horizontal embedding of the full incidence. \(E_Y\) is locally in degree \(-2\); its exceptional inverse image along that embedding is locally in degree \(-1\), agreeing with \(\pi^{-1}f^{-1}\omega_X\). Ordinary restriction would keep degree \(-2\) and miss (12).

The other map is \(f_\pi(0,v;\xi)=(0;\xi)\). It forgets \(v\) and has a whole noncompact line over each target covector. It is not proper on this subset. This demonstrates the difference between the two cotangent properness tests using the actual maps.

### Tangential and normal covectors give different embedding tests

*Difficulty: Intermediate.*

Let \(i:\mathbb R_u\hookrightarrow\mathbb R^2_{x,z}\), \(i(u)=(u,0)\). Test inverse-image properness for the zero section, the conormal of the vertical line \(\{x=0\}\), and the conormal of the horizontal line \(\{z=0\}\).

**Solution.** A correspondence covector is \((u;\xi\,dx+\zeta\,dz)\), and
\(i_d(u;\xi,\zeta)=(u;\xi)\).
For the zero section, \(\xi=\zeta=0\); the restriction identifies its pulled-back carrier with the zero section of \(T^*\mathbb R\) and is proper.

The vertical line's conormal has \(x=0\), \(\zeta=0\), and arbitrary \(\xi\). Its pulled-back carrier has \(u=0,\zeta=0\); the remaining \(\xi\) maps identically to the cotangent fibre at zero. Properness holds. The embedding is transverse to that vertical line.

The horizontal line's conormal has arbitrary \(x\), \(\xi=0\), and arbitrary \(\zeta\). Its pulled-back carrier has arbitrary \(u,\zeta\) and maps to \((u;0)\). Each fixed \(u\) has a noncompact \(\zeta\)-fibre, so properness fails. This is exactly a nonzero normal covector killed by restriction to the tangent line. These conclusions distinguish properness and carriers; the normalized transverse conormal equality is a further comparison theorem.

### Point weights and the normalized zero section

*Difficulty: Intermediate.*

Take a map from a two-point zero-dimensional manifold to a point. Compute pullback and direct image of point weights over \(A=\mathbb Z\). Then explain why (18) remains a generator for a nonorientable positive-dimensional \(X\), and why (19) is defined for a closed point embedding.

**Solution.** In dimension zero, all cotangent fibres have rank zero and every dualizing coefficient is \(A\) in degree zero. The graph and diagonal conormal maps are identity maps on their point components, and the point counit is the identity. Pullback sends \(a\) to \((a,a)\); proper direct image sums weights. Thus pulling back \(1\) and then pushing it forward gives \(2\in\mathbb Z\). This records the two sheets. No orientation permutation or nonzero cohomological degree occurs, and the ring has finite global dimension one.

For general \(X\), the zero embedding is proper and the actual map
\(A_X\xrightarrow{\beta_{a_X}}z_X^!E_X\) is an isomorphism. The image of \(1\) gives (18), a generator on every connected local zero-section piece. Its coefficient is \(\operatorname{or}_X\otimes B_X|_X\), so the two orientation signs cancel on an orientation-reversing chart overlap. No global choice of base orientation is needed.

For a closed point \(p\hookrightarrow X\), the direct-image incidence is the full fibre \(T_p^*X\), and its map \(i_\pi\) is a closed embedding into \(T^*X\), hence proper. Its \(i_d\) maps to the point zero section. Thus (19) is the actual supported trace image of \(1\), a conormal generator with the cotangent-fibre coefficient included. The inverse operation would instead require the fibre collapse to be proper; in positive dimension it is not. The existence of this direct conormal cycle does not authorize that distinct inverse operation.
