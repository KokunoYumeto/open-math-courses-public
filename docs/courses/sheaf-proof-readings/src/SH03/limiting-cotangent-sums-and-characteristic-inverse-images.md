# Limiting cotangent sums and characteristic inverse images

Two nearby conormal directions can cancel while each grows without bound. Their finite remainder may contain a direction that no ordinary same-base sum sees. Likewise, the transpose differential of a map can have a finite limit on increasingly large input covectors near a critical point. The limiting cotangent operations retain these phenomena. We will prove that they preserve subanalytic isotropy, using exact slices of Lagrangian normal cones.

All manifolds are real analytic, finite dimensional, Hausdorff and countable at infinity; all maps below are analytic. Conic means invariant under every positive cotangent-fibre dilation. Isotropy of a subanalytic cotangent set means that its canonical one-form restricts to zero on its regular locus. We use the singular analytic-form calculus and the full normal-cone theorem in [Boundary forms and Lagrangian normal cones](boundary-forms-and-lagrangian-normal-cones.md#the-full-lagrangian-normal-cone-theorem). No sheaf coefficient ring or boundedness hypothesis enters these geometric operations.

Kashiwara and Schapira, [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §1.2, printed pp. 15–17, give the normal-cone sequence definition and Proposition 1.2.1 with its simultaneous-scaling proof for a submanifold restriction. Here the diagonal and arbitrary-map graph slices are proved explicitly, followed by isotropy from the boundary-form theorem. Both directions, zero covectors and unbounded inputs are retained.

<a id="limiting-geometry-inputs"></a>
<a id="the-exact-dependency-of-the-isotropy-assertion-limiting-geometry-inputs"></a>

## The exact dependency of the isotropy assertion

The sequence geometry, joint scale and slice identities below apply to arbitrary positive-conic subsets. Subanalytic isotropy enters through the linked normal-cone theorem. Its [boundary calculation](boundary-forms-and-lagrangian-normal-cones.md#the-smooth-source-calculation-analytic-boundary-without-function-resolution) uses analytic Taylor expansion on a proper uniformizing smooth source. The [proper uniformization construction](subanalytic-sets-and-limiting-tangent-directions.md#a-locally-finite-assembly-with-a-fixed-source-dimension) covers closed subanalytic sets on the stated countable-at-infinity manifolds. The [local subanalytic set calculus](subanalytic-sets-and-limiting-tangent-directions.md#the-local-calculus-with-the-precise-properness-hypothesis) and [singular one-form pullback, closure and surjective detection](subanalytic-sets-and-limiting-tangent-directions.md#analytic-maps-and-locally-finite-unions) supply the set and form operations. The latter proof uses Sard for a surjection between manifolds. Proper uniformization itself uses function resolution; the optional second boundary proof resolves the function on the uniformizing source separately. These geometric arguments involve no sheaf coefficients, constructibility assumption or derived-category bound.

The normal-deformation charts are the [divided-coordinate charts](normal-scaling-and-microlocal-hom.md#normal-scaling-and-the-positive-deformation-normal-deformation-charts) constructed in the normal-scaling reading. For analytic adapted changes, their extension at parameter zero is analytic: a convergent power series vanishing at \(t=0\) is divisible by \(t\), with convergent analytic quotient. Thus no global tubular-neighborhood or contact normal-form theorem is needed for the local slice calculations.

## The product bounds in the definitions

For conic subsets \(A,B\subset T^*X\), their **limiting sum** \(A\widehat+ B\) has the local criterion

\[
(x;\sigma)\in A\widehat+ B
\iff
\begin{cases}
(x_j;\xi_j)\in A,\quad (z_j;\zeta_j)\in B,\\
x_j,z_j\to x,\quad \xi_j+\zeta_j\to\sigma,\\
|x_j-z_j|\,|\xi_j|\to0.
\end{cases}
\tag{1}
\]

Covectors at different base points are written in one coordinate trivialization for this criterion. The operation is intrinsically defined by normal cones; the prerequisite coordinate comparison makes (1) independent of the chosen smooth analytic coordinates and local norms. In a fixed relatively compact chart, a change of trivialization alters the transformed sum by a term bounded by \(C|x_j-z_j|\,|\xi_j|\), which tends to zero by the last line.

The finite limiting sum bounds \(|\xi_j+\zeta_j|\). Therefore the product condition is equivalent to the one with \(|\zeta_j|\), or to

\[
|x_j-z_j|\,(1+|\xi_j|+|\zeta_j|)\to0.
\tag{2}
\]

For example, \(|\zeta_j|\le|\xi_j|+|\xi_j+\zeta_j|\); multiplying by the base separation proves one implication. The reverse inequality gives the other. In particular the limiting sum is symmetric.

For \(f:Y\to X\) and conic \(A\subset T^*X\), the **characteristic inverse image** has criterion

\[
(y;\eta)\in f^\sharp A
\iff
\begin{cases}
y_j\to y,\quad x_j\to f(y),\quad (x_j;\xi_j)\in A,\\
(df_{y_j})^t\xi_j\to\eta,\\
|x_j-f(y_j)|\,|\xi_j|\to0.
\end{cases}
\tag{3}
\]

The differential is evaluated at the moving \(y_j\). In (1) and (3), individual covectors need not converge. The product controls how fast they may grow relative to the base mismatch. Zero covectors are permitted whenever they belong to the chosen input sets.

The ordinary operations are respectively \(A+B\), with both inputs at one base point, and \(f_df_\pi^{-1}A\), with \(x=f(y)\) and \(\eta=(df_y)^t\xi\). Constant witnesses show that these ordinary sets are contained in the limiting operations. This does not give equality in general.

<a id="weighted-coordinate-covariance"></a>
<a id="coordinate-covariance-with-the-large-covectors-retained-weighted-coordinate-covariance"></a>

## Coordinate covariance with the large covectors retained

The intrinsic slices (11) and (20) already show coordinate independence. The following direct estimates explain the role of their product bounds. Work in smaller relatively compact coordinate neighborhoods. All coordinate derivatives and inverse matrices used below are bounded there. An analytic coordinate change is \(C^2\), so its first derivative and its inverse-transpose matrix are locally Lipschitz.

For a base change \(h\) on \(X\), put \(P(x)=Dh(x)^{-T}\). The transformed covector sum is

\[
P(x_j)\xi_j+P(z_j)\zeta_j
=P(z_j)(\xi_j+\zeta_j)
 +(P(x_j)-P(z_j))\xi_j,
\qquad
\bigl|(P(x_j)-P(z_j))\xi_j\bigr|
\le C|x_j-z_j|\,|\xi_j|.
\tag{LG1}
\]

The last term tends to zero, even when the individual covectors diverge. The first tends to \(P(x)\sigma\). Also

\[
|h(x_j)-h(z_j)|\,|P(x_j)\xi_j|
\le C|x_j-z_j|\,|\xi_j|.
\tag{LG2}
\]

Applying the same argument to \(h^{-1}\) gives the reverse implication. Uniform equivalence of norms on these smaller charts proves norm independence as well.

For characteristic inverse image, change the source chart by \(g\), the target chart by \(h\), and write \(f'=hfg^{-1}\). The covector at the nearby target point \(x_j\) transforms by \(Dh(x_j)^{-T}\), whereas the derivative of the transformed map uses \(Dh(f(y_j))\). Retaining this distinction gives

\[
\begin{aligned}
(Df'_{g(y_j)})^T Dh(x_j)^{-T}\xi_j
&=Dg(y_j)^{-T}(Df_{y_j})^T\xi_j+R_j,\\
|R_j|&\le C|x_j-f(y_j)|\,|\xi_j|.
\end{aligned}
\tag{LG3}
\]

Indeed the extra matrix between \((Df_{y_j})^T\) and \(\xi_j\) is \(Dh(f(y_j))^T Dh(x_j)^{-T}-1\), whose norm is bounded by \(C|x_j-f(y_j)|\). The new mismatch product is bounded by the old one as in (LG2). Consequently the limiting output is \(Dg(y)^{-T}\eta\); applying the inverse chart changes proves equivalence in both directions. There is no estimate of either \(|\xi_j|\) or \(|\zeta_j|\) by a fixed constant. These are \(C^2\) coordinate estimates, as sufficient for the analytic setting; arbitrary merely \(C^1\) chart changes are not being asserted to have a Lipschitz derivative.

## A positive scale that sends both errors to zero

We will need a scale that works even when the covectors grow. Suppose

\[
a_j\ge0,\quad a_j\to0,\qquad
m_j\ge1,\quad a_jm_j\to0.
\tag{4}
\]

Define

\[
t_j=\sqrt{a_j/m_j}+\frac1{jm_j}.
\tag{5}
\]

Then \(t_j>0\), \(t_j\to0\), and

\[
\frac{a_j}{t_j}\le\sqrt{a_jm_j}\to0,
\qquad t_jm_j=\sqrt{a_jm_j}+\frac1j\to0.
\tag{6}
\]

For \(a_j>0\), the first bound follows by dropping the positive second term in (5); for \(a_j=0\), its left side is zero. Also \(t_j\le\sqrt{a_j}+1/j\), proving its limit. Thus division by \(t_j\) kills the position error while multiplication by \(t_j\) kills every covector bounded by \(m_j\). This supplies an actual normal-deformation sequence over the zero conormal base.

<a id="joint-scale-equivalence"></a>
<a id="the-joint-scale-is-equivalent-to-the-weighted-condition-joint-scale-equivalence"></a>

## The joint scale is equivalent to the weighted condition

For \(m_j\ge1\) and \(a_j\ge0\), the weighted condition has exactly the following content:

\[
a_jm_j\longrightarrow0
\quad\Longleftrightarrow\quad
\text{there are }t_j>0\text{ with }
t_j\to0,\quad a_j/t_j\to0,\quad t_jm_j\to0.
\tag{LG4}
\]

The forward implication is precisely (5)–(6); the extra hypothesis \(a_j\to0\) in (4) follows already from \(m_j\ge1\). Conversely, \(a_jm_j=(a_j/t_j)(t_jm_j)\to0\). This explains why one scale can both move the cotangent base of the normal cone to its zero section and kill the divided position mismatch. If a sequential convention requires parameters to decrease strictly, pass to a subsequence of the positive \(t_j\to0\). All limits and memberships remain valid.

Positive conicity is used twice in each slice proof: first to multiply a witness covector by \(t_j\), and then, in the reverse direction, to divide by \(t_j\). Neither use requires zero covectors to belong to the original sets. Zero output covectors arise in the closed limiting set even when an input omits them. No replacement of these positive dilations by an antipodal symmetry is justified or needed.

## The diagonal conormal and its exact slice

Let

\[
P=T^*(X\times X),\qquad
L=T_\Delta^*(X\times X),\qquad
S=A\times B,
\tag{7}
\]

where \(\Delta\) is the diagonal of the base \(X\times X\). The manifold \(L\) is a closed analytic conic Lagrangian. Let \(r:L\to X\) project to the diagonal base and \(j:X\to L\) be its zero conormal section. Define the analytic bundle embedding

\[
e:T^*X\longrightarrow T^*L,\qquad
e(x;\sigma)=\bigl(j(x);(dr_{j(x)})^t\sigma\bigr).
\tag{8}
\]

If \(\lambda_L\) and \(\lambda_X\) are the canonical forms on these cotangent bundles, then

\[
e^*\lambda_L=\lambda_X.
\tag{9}
\]

Indeed the value of the left side on a tangent vector is \((dr)^t\sigma\) applied to its projected tangent at \(j(x)\); since \(r\circ j=\mathrm{id}_X\), the result is \(\sigma\) applied to the original projected base tangent.

The normal identification from the preceding lesson is

\[
K:N_LP\longrightarrow T^*L,\qquad
K([w])(v)=\omega_P(w,v),
\tag{10}
\]

whose inverse is induced by \(-H\). The exact geometric identity is

\[
A\widehat+ B=e^{-1}\bigl(K C_L(A\times B)\bigr).
\tag{11}
\]

We prove it with both directions and all scaling conditions.

Use local coordinates

\[
x=x_1,\quad \delta=x_2-x_1,\quad
\nu=\xi_2,\quad s=\xi_1+\xi_2.
\tag{12}
\]

The canonical form on \(P\) becomes

\[
\alpha_P=s\,dx+\nu\,d\delta,
\qquad L=\{\delta=0,s=0\}.
\tag{13}
\]

Thus a normal vector with components \((v,\sigma)\) in \((\delta,s)\) is taken by \(K\) to \(\sigma\,dx-v\,d\nu\). The embedding (8) selects \(\nu=0\) and \(v=0\), leaving \(\sigma\) arbitrary.

**Proof of (11), forward direction.** Start with a witness in (1). Take \(a_j=|z_j-x_j|\) and \(m_j=1+|\xi_j|+|\zeta_j|\). Equation (2) gives (4). Choose (5). Positive conicity puts \((x_j;t_j\xi_j)\) in \(A\) and \((z_j;t_j\zeta_j)\) in \(B\). In the deformation along \(L\), the resulting coordinates are

\[
\left(x_j,t_j\zeta_j;
\frac{z_j-x_j}{t_j},\xi_j+\zeta_j;t_j\right).
\tag{14}
\]

The two entries before the first semicolon describe the base in \(L\); the next two are normal coordinates. By (6) and (1), this tuple tends to \((x,0;0,\sigma;0)\). The normal-cone definition therefore puts that central normal vector in \(C_L(S)\), and (13) takes it to \(e(x;\sigma)\).

**Reverse direction.** A witness for this central cone point consists of actual points
\((x_j,z_j;a_j',b_j')\in A\times B\) and positive deformation parameters \(t_j\to0\), with

\[
x_j,z_j\to x,\quad b_j'\to0,\quad
\frac{z_j-x_j}{t_j}\to0,\quad
\frac{a_j'+b_j'}{t_j}\to\sigma.
\tag{15}
\]

Unscale the covectors by \(1/t_j\); they remain in their respective sets. The resulting sum has the required limit, and the base-gap product with the second covector is

\[
|z_j-x_j|\,|b_j'/t_j|
=|(z_j-x_j)/t_j|\,|b_j'|\to0.
\tag{16}
\]

The finite sum makes this equivalent to the product with the first covector. Hence these unscaled points satisfy (1). This proves (11). \(\square\)

This route uses a conormal to a diagonal in the base. In the contravariant graph convention, the construction for \(f^\sharp(A,B)\) uses \(A\times B^a\), while the limiting sum is \((\mathrm{id})^\sharp(A,B^a)\). The two antipodes cancel, giving exactly the product in (7).

<a id="diagonal-sign-comparison"></a>
<a id="comparing-the-two-diagonal-coordinate-conventions-diagonal-sign-comparison"></a>

## Comparing the two diagonal coordinate conventions

The slice coordinates (12) use \(x=x_1\), \(\delta=x_2-x_1\), \(\nu=\xi_2\), while the earlier full-conormal calculation uses \(z=x_2\), \(u=x_1-x_2\), \(a=\xi_1\). On the diagonal conormal, \(\nu=-a\), and their normal displacements satisfy \(v_\delta=-v_u\). Consequently

\[
\sigma\,dx-v_\delta\,d\nu
=\sigma\,dz-v_u\,da.
\tag{LG8}
\]

The change of normal sign is accompanied by the change of conormal parameter. Both conventions therefore select the same slice at zero conormal base and zero position-normal component, with output \(\sigma\), not \(-\sigma\). For the graph, the exact equality \(\theta\,dy+\xi\,dx=s\,dy+\nu\,d\delta\) in (27) fixes the same sign. The normal identification is always \(K([w])(v)=\omega(w,v)\), whose inverse is induced by \(-H\).

<a id="limiting-sum-isotropy"></a>
<a id="isotropy-of-the-full-limiting-sum-limiting-sum-isotropy"></a>

## Isotropy of the full limiting sum

**Theorem.** If \(A,B\subset T^*X\) are positive-conic subanalytic isotropic sets, then \(A\widehat+ B\) is closed, positive-conic, subanalytic and isotropic. The inputs need not be closed.

**Proof.** The product \(S=A\times B\) is subanalytic and positive-conic. Its canonical form is the sum of the forms from the two cotangent factors. Analytic pullback of their vanishing gives \(\alpha_P|_S=0\), so \(S\) is isotropic. The full Lagrangian normal-cone theorem makes

\[
D=K C_L(S)\subset T^*L
\tag{17}
\]

subanalytic, positive-conic and isotropic. It is also closed as a normal cone in this bundle. Formula (11) makes the limiting sum an analytic inverse image of \(D\), so it is closed and subanalytic. The embedding is linear in the cotangent fibre, giving positive conicity. Singular analytic one-form pullback and (9) give \(\lambda_X|_{e^{-1}D}=0\). This proves isotropy. \(\square\)

The proof covers cancellation at infinite covector norm through a closed normal-cone slice. It does not require properness of an unrestricted cotangent projection.

<a id="characteristic-inverse-isotropy"></a>
<a id="the-graph-conormal-and-characteristic-inverse-image-characteristic-inverse-isotropy"></a>

## The graph conormal and characteristic inverse image

For \(f:Y\to X\), use the graph \(G=\{(y,f(y))\}\subset Y\times X\), and set

\[
P=T^*(Y\times X),\qquad
L=T_G^*(Y\times X),\qquad
S=T_Y^*Y\times A.
\tag{18}
\]

The first factor in \(S\) is the zero section. The graph is a closed analytic submanifold for every analytic \(f\); no rank condition on \(df\) is needed. Its conormal is a closed conic Lagrangian. Let \(r:L\to Y\) project to the graph base, let \(j\) be its zero conormal section, and define \(e:T^*Y\to T^*L\) by the analogue of (8). Again,

\[
e^*\lambda_L=\lambda_Y.
\tag{19}
\]

We claim the full identity

\[
f^\sharp A=e^{-1}\bigl(K C_L(T_Y^*Y\times A)\bigr).
\tag{20}
\]

In local coordinates, with original covectors \((\theta,\xi)\) on \(Y\times X\), use

\[
\delta=x-f(y),\qquad \nu=\xi,\qquad
s=\theta+(df_y)^t\xi.
\tag{21}
\]

The canonical form is exactly \(s\,dy+\nu\,d\delta\). The conormal is \(\delta=s=0\), and the normal identification sends \((v,\eta)\) to \(\eta\,dy-v\,d\nu\). Hence \(e\) selects the same zero conormal base and zero position-normal component as before.

For a witness in (3), set \(a_j=|x_j-f(y_j)|\), \(m_j=1+|\xi_j|\), and choose (5). Scale the \(X\) covector by \(t_j\) and keep the \(Y\) covector zero. The normal-deformation coordinates are

\[
\left(y_j,t_j\xi_j;
\frac{x_j-f(y_j)}{t_j},(df_{y_j})^t\xi_j;t_j\right),
\tag{22}
\]

which tend to \((y,0;0,\eta;0)\). This proves one inclusion in (20).

Conversely, a witness for that central cone point has zero \(Y\) covector and \(X\) covectors \(a_j'\to0\), with \((x_j;a_j')\in A\), positive \(t_j\to0\),

\[
\frac{x_j-f(y_j)}{t_j}\to0,\qquad
(df_{y_j})^t(a_j'/t_j)\to\eta.
\tag{23}
\]

Unscale to \(\xi_j=a_j'/t_j\in A\). Its product in (3) equals
\(|(x_j-f(y_j))/t_j|\,|a_j'|\), which tends to zero. All other limits in (3) are part of the same deformation witness. This proves (20).

**Theorem.** If \(A\subset T^*X\) is positive-conic, subanalytic and isotropic, then \(f^\sharp A\subset T^*Y\) is closed, positive-conic, subanalytic and isotropic.

**Proof.** The product with the zero section in (18) is subanalytic, conic and isotropic. Apply the normal-cone theorem along the graph conormal. The analytic inverse-image identity (20), fibre linearity of \(e\), and canonical-form identity (19) prove each conclusion exactly as for (17). No input closedness, properness, noncharacteristic hypothesis or constant rank was imposed. \(\square\)

Permuting the two base factors to the alternate order \(X\times Y\) preserves their summed canonical form. Also the antipode on the zero section changes nothing, so (18) retains the graph construction's variance.

<a id="limiting-input-closures"></a>
<a id="nonclosed-inputs-and-actual-closure-invariance-limiting-input-closures"></a>

## Nonclosed inputs and actual closure invariance

The normal cone is closed in its normal bundle and depends only on the closure of its input. This can also be checked with its exact scales: if an input point is only in the closure, approximate it by an actual point within \(t_j/j\) in the adapted coordinates for a witness of deformation parameter \(t_j\). The error in its divided normal coordinate is at most \(1/j\), and its tangent-base error also tends to zero.

For the sequence operations (1) and (3), the following stronger explicit check handles the possibly unbounded covectors:

\[
\overline A\widehat+\overline B=A\widehat+B,
\qquad f^\sharp\overline A=f^\sharp A.
\tag{LG5}
\]

Monotonicity proves one inclusion. For the reverse sum inclusion, take a witness with inputs in the two closures and set \(m_j=1+|\xi_j|+|\zeta_j|\). Approximate both input points by points in the original sets with each base and covector error less than \(\epsilon_j=1/(jm_j)\). The new covector sum changes by at most \(2\epsilon_j\), the base separation increases by at most \(2\epsilon_j\), and the first covector norm increases by at most \(\epsilon_j\). Its weighted product is therefore at most

\[
|x_j-z_j|\,|\xi_j|
 +|x_j-z_j|\epsilon_j
 +2\epsilon_j|\xi_j|+2\epsilon_j^2
\longrightarrow0.
\tag{LG6}
\]

All required limits survive. For characteristic inverse image keep \(y_j\) fixed and approximate \((x_j,\xi_j)\) within \(\epsilon_j=1/(j(1+|\xi_j|))\). The transpose derivatives are locally bounded, so their output error tends to zero. The mismatch-product estimate is the same calculation with one rather than two base perturbations. This proves the other equality in (LG5). The approximation argument itself requires no conicity; conicity is required by the normal-cone slice interpretations (11) and (20).

In particular, for an analytic diffeomorphism, the closure formula is

\[
f^\sharp A=f_df_\pi^{-1}(\overline A).
\tag{LG7}
\]

The inverse matrices bound and recover the convergent input covector, now in \(\overline A\); (LG5) supplies the reverse inclusion from closure witnesses. For the identity map this says \(\operatorname{id}^{\sharp}A=\overline A\). Thus closedness of the resulting set does not tacitly impose closedness on the original set.

## Exercises with complete solutions

### A limiting sum between disjoint zero-section supports

*Difficulty: Introductory.*

In \(T^*\mathbb R\), let \(A=\{(x;0):x>0\}\) and \(B=\{(x;0):x<0\}\). Compute their ordinary sum and their limiting sum.

**Solution.** The ordinary sum requires a common base point, and the two base supports are disjoint, so \(A+B=\varnothing\). Any limiting sum has covector zero, since both input covectors are zero. Its base must be in \([0,\infty)\cap(-\infty,0]=\{0\}\). The pair of base points \(1/j,-1/j\), with zero covectors, satisfies (1): the sum and gap product are identically zero. Thus \(A\widehat+ B=\{(0;0)\}\). It is subanalytic and isotropic, although neither input support is closed.

### Tangent conormals produce every cotangent direction by cancellation

*Difficulty: Advanced.*

In \(\mathbb R^2\) with coordinates \((u,v)\), take \(A=T_{\{v=u^2\}}^*\mathbb R^2\) and \(B=T_{\{v=0\}}^*\mathbb R^2\). Compute their ordinary and limiting sums.

**Solution.** A common base must be the origin. Both conormal fibres there are the \(dv\) line, so the ordinary sum is that line over the origin. For any target \(a\,du+d\,dv\), choose nonzero \(u_j\to0\) and set

\[
b_j=-\frac{a}{2u_j},\qquad
\xi_j=(-2u_jb_j,b_j),\qquad
\zeta_j=(0,d-b_j).
\tag{24}
\]

Use base points \((u_j,u_j^2)\) and \((u_j,0)\). The first covector annihilates the parabola tangent \((1,2u_j)\); the second is an axis conormal. Their sum is exactly \((a,d)\). The gap is \(|u_j|^2\), and

\[
|u_j|^2|\xi_j|
\le |a|\,|u_j|^2+\tfrac12|a|\,|u_j|\to0.
\tag{25}
\]

For \(a=0\), take \(b_j=0\); the same argument works. Thus every covector over the origin is in the limiting sum. No other base is possible, because the two closed projected supports intersect only at the origin. Therefore \(A\widehat+ B=T_0^*\mathbb R^2\). The full vertical fibre is isotropic; the added \(du\) directions arise from unbounded cancelling conormals, rather than an ordinary fibre computation.

### A fold adds characteristic inverse directions

*Difficulty: Intermediate.*

For \(f:\mathbb R_y\to\mathbb R_x\), \(f(y)=y^2\), let \(A=T_0^*\mathbb R_x\). Compare \(f_df_\pi^{-1}A\) and \(f^\sharp A\).

**Solution.** An exact input base must satisfy \(y^2=0\), so \(y=0\), where \(df_0=0\). The ordinary inverse set is only \(\{(0;0)\}\). To produce arbitrary output \(\eta\,dy\), take nonzero \(y_j\to0\), \(x_j=0\), and \(\xi_j=\eta/(2y_j)\). Then

\[
(df_{y_j})^t\xi_j=\eta,
\qquad |x_j-f(y_j)|\,|\xi_j|
=\tfrac12|\eta|\,|y_j|\to0.
\tag{26}
\]

For \(\eta=0\), these covectors are zero and are still admissible. Every origin covector is therefore in \(f^\sharp A\). Its base cannot be elsewhere because any input base is zero and must tend to \(f(y)=0\). Hence \(f^\sharp A=T_0^*\mathbb R_y\), a closed isotropic set. The moving differential and unbounded inputs in (26) account for the extra directions.

### Diffeomorphisms have no escaping inverse directions for closed inputs

*Difficulty: Intermediate.*

Let \(f:Y\to X\) be an analytic diffeomorphism and \(A\subset T^*X\) closed and conic. Prove \(f^\sharp A=f_df_\pi^{-1}A\). Identify where closedness is used.

**Solution.** For a witness in (3), write \(\eta_j=(df_{y_j})^t\xi_j\). It converges to \(\eta\). In coordinates near \(y\), the inverse matrices \((df_{y_j})^{-t}\) converge to \((df_y)^{-t}\) and are uniformly bounded. Thus \(\xi_j=(df_{y_j})^{-t}\eta_j\to\xi=(df_y)^{-t}\eta\). Together with \(x_j\to f(y)\), closedness of \(A\) gives \((f(y);\xi)\in A\). Its transpose image is \(\eta\), proving ordinary inverse membership. Conversely use the constant witness \(y_j=y,x_j=f(y),\xi_j=\xi\). Its mismatch is zero. Closedness was needed only to retain the limiting input in \(A\); nonclosed inputs can acquire ambient limits in the characteristic inverse image even under the identity map.

### One scale handles zero mismatch and arbitrarily large covectors

*Difficulty: Advanced.*

Prove all assertions (5)–(6), including zero values of \(a_j\). Apply them to the diagonal tuple (14) and explain why merely choosing \(t_j=1/m_j\) is insufficient in general.

**Solution.** Positivity follows from \(1/(jm_j)>0\). Since \(m_j\ge1\), \(t_j\le\sqrt{a_j}+1/j\to0\). When \(a_j>0\), \(t_j\ge\sqrt{a_j/m_j}\) gives \(a_j/t_j\le\sqrt{a_jm_j}\); when \(a_j=0\), the quotient is zero. Multiplication of (5) by \(m_j\) gives the second equality in (6). Therefore the scaled \(\zeta_j\) in (14) tends to zero and its rescaled position difference also tends to zero, while the covector sum retains its given finite limit. These are the exact central normal coordinates needed for (11). If \(m_j\) is bounded, \(1/m_j\) need not tend to zero; even when it tends to zero, its product with \(m_j\) is one and does not send the conormal base to zero. Formula (5) supplies both required vanishings.

### The graph slice retains its canonical form and both antipodes

*Difficulty: Intermediate.*

For \(f:Y\to X\), derive the canonical-form transformation (21), compute its normal identification along the graph conormal, and verify \(e^*\lambda_L=\lambda_Y\). Explain why the diagonal sum uses \(A\times B\).

**Solution.** Write \(x=f(y)+\delta\). Then

\[
\theta\,dy+\xi\,dx
=\bigl(\theta+(df_y)^t\xi\bigr)dy+\xi\,d\delta
=s\,dy+\nu\,d\delta.
\tag{27}
\]

Its exterior derivative is \(ds\wedge dy+d\nu\wedge d\delta\). Evaluation on a normal vector \((v,\eta)\) and a graph-conormal tangent gives \(\eta\,dy-v\,d\nu\), with the minus sign prescribed by (10). The embedding fixes \(\nu=0\), sets the coefficient of \(d\nu\) to zero, and keeps \(\eta\,dy\). Pulling back the cotangent canonical form therefore gives \(\lambda_Y\) exactly, including zero covectors. Finally the contravariant graph convention uses \(A\times B^a\), and the sum substitutes \(B^a\) as its second input. Since \((B^a)^a=B\), its graph-normal product is \(A\times B\). Permuting factors preserves the summed canonical form and inserts no further sign.

<a id="weighted-product-essential-check"></a>
<a id="the-weighted-product-cannot-be-omitted-weighted-product-essential-check"></a>

### The weighted product cannot be omitted

*Difficulty: Advanced.*

Let \(c(u)=(u,u^2)\), let \(N=c(\mathbb R)\subset\mathbb R^2\), and let

\[
\Lambda=T_N^*\mathbb R^2
=\{(c(u);b(-2u,1)):u,b\in\mathbb R\}.
\tag{LG9}
\]

Compute \(\Lambda\widehat+\Lambda\) and \(c^\sharp\Lambda\). Then remove only the weighted-product condition from (1) and (3), leaving all other convergence conditions in place. Compute the resulting larger sets and test their isotropy.

**Solution.** For a weighted sum witness write its input points as \((c(u_j);b_j(-2u_j,1))\) and \((c(v_j);d_j'(-2v_j,1))\), with \(u_j,v_j\to u\), and let the covector sum be \((a_j,d_j)\to(a,d)\). One has

\[
a_j+2v_jd_j=2(v_j-u_j)b_j,
\qquad
|(v_j-u_j)b_j|
\le |c(u_j)-c(v_j)|\,|b_j(-2u_j,1)|\to0.
\tag{LG10}
\]

Hence \(a+2ud=0\), precisely the conormal condition. Constant witnesses give the reverse inclusion, so \(\Lambda\widehat+\Lambda=\Lambda\).

Without the product condition, fix any \((a,d)\), choose nonzero \(h_j\to0\), and take the two bases \(c(u+h_j),c(u)\) with covectors

\[
b_j=-\frac{a+2ud}{2h_j},\qquad
\xi_j=b_j(-2(u+h_j),1),\qquad
\zeta_j=(d-b_j)(-2u,1).
\tag{LG11}
\]

Their sum is exactly \((a,d)\). Thus the relaxed sum is all of \(T^*\mathbb R^2|_N\). For a covector not conormal to \(N\), the excluded product has the nonzero limit

\[
|c(u+h_j)-c(u)|\,|\xi_j|
\longrightarrow\tfrac12|a+2ud|(1+4u^2)>0.
\tag{LG12}
\]

In parameters \((u,a,d)\), the canonical form on this relaxed set is \((a+2ud)\,du\). It does not vanish. The relaxed set is therefore not isotropic, despite the input being a closed analytic conic Lagrangian.

For the inverse image, write a witness as \(y_j\to y\), \(x_j=c(u_j)\), and \(\xi_j=b_j(-2u_j,1)\). Its output obeys

\[
\eta_j=(dc_{y_j})^T\xi_j=2(y_j-u_j)b_j,
\qquad
|\eta_j|\le2|c(u_j)-c(y_j)|\,|\xi_j|\longrightarrow0.
\tag{LG13}
\]

Zero input covectors give all zero outputs, so \(c^\sharp\Lambda=T_{\mathbb R}^*\mathbb R\), the zero section. If the product condition is dropped, take \(y_j=y\), \(u_j=y+h_j\), and \(b_j=-\eta/(2h_j)\). The output is the arbitrary constant \(\eta\). The relaxed inverse is the whole \(T^*\mathbb R\), where \(\eta\,dy\) does not vanish. For \(\eta\ne0\), its mismatch product tends to \(\tfrac12|\eta|(1+4y^2)>0\), as in (LG12). The same smooth example therefore detects the essential product bound in both operations.

The extra directions in this check are excluded by the weighted hypotheses, not by input closedness, properness or subanalytic regularity. The theorem's unbounded-covector scope allows growth exactly when its product with the relevant base mismatch tends to zero.

<a id="limiting-source-and-scope"></a>
<a id="source-comparison-and-exact-scope-limiting-source-and-scope"></a>

## Source comparison and exact scope

The cited normal-cone proof simultaneously scales normal displacements and covectors for a conormal restriction. Formula (5) makes a single positive choice valid even at zero mismatch and bounded covector size; (LG4) proves its converse. The diagonal and graph arguments then establish the exact slice identities (11) and (20) in both directions. The coordinate estimates (LG1)–(LG3) explicitly compare the derivative at the moving map image with the covector transformation at the nearby input point. The closure approximations and the parabola exercise preserve those weighted errors. These additions and the separately proved boundary-form calculation provide the stated geometry; the conormal restriction criterion alone does not establish the full arbitrary-map preservation statements.

The cited treatment supplies the normal-cone comparison; the programme proofs linked above supply the subanalytic and boundary-form inputs. Independently written programme expression is dedicated under CC0 1.0 Universal. The human source retains its own terms; no source prose, figures or exercise text is reproduced here.

## What these operations supply for stratifications

The theorems preserve the full limiting operations, including characteristic escape. The pair condition used for microlocal stratifications can therefore be expressed using closed subanalytic isotropic conormal limits, with their exact product bounds. Generic-base conormality and dimension induction will then identify where that pair condition holds and construct compatible stratifications.
