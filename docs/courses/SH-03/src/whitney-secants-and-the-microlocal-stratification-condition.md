# Whitney secants and the microlocal stratification condition

Tangent planes and secant lines measure different approaches to a frontier. A limiting tangent plane records directions within the approaching stratum; a secant joins that stratum to a moving point of the lower one. We will compare three tests: cancellation of conormal covectors, a quantitative gap between tangent spaces, and containment of limiting secants. The first two are equivalent; subanalytic curve selection turns their common estimate into Whitney's secant condition. The precise chain is \(\mu\Longleftrightarrow(w)\Longrightarrow(b)\Longrightarrow(a)\). A polynomial surface will exhibit the scale at which cancellation defeats the metric estimate. The final application keeps one prescribed μ-stratification while passing between a bounded sheaf complex and its cohomology sheaves.

Let \(M,N\subset\mathbb R^n\) be disjoint subanalytic smooth submanifolds of fixed dimensions, with \(N\subset\overline M\setminus M\). The manifold and subanalytic conventions are those of [Microlocal stratifications by removing bad loci](../../sheaf-proof-readings/src/SH03/microlocal-stratifications-by-removing-bad-loci.md#partitions-and-their-frontiers). Analytic strata satisfy these hypotheses. We use the Euclidean metric to identify covectors and vectors, but retain their different roles. All norms and distances below are Euclidean. No coefficient ring enters the geometric arguments.

The subanalytic [normal-cone operations](../../sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#the-signed-normal-cone-prerequisite) and the [analytic curve-selection theorem](../../sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#from-a-local-analytic-presentation-to-analytic-curve-selection) have programme proofs in *Subanalytic sets and limiting tangent directions*. David J. A. Trotman proves the equivalence between the microlocal condition and Verdier's quantitative condition (w) in [*Une version microlocale de la condition (w) de Verdier*](https://www.numdam.org/item/10.5802/aif.1190.pdf#page=3), §1–2, pp. 826–828. We give the normalization argument and then prove its consequence for Whitney secants using analytic curve selection. The triangulation case is proved in [Constructible sheaves on a triangulation](../../sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#modules-that-continue-into-larger-faces).

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

## Tangent planes, secant lines and the order of the pair

At \(p\in N\), Whitney's condition **(a)** for the ordered pair \((M,N)\) says that

\[
x_j\in M,\quad x_j\to p,\quad T_{x_j}M\to T
\quad\Longrightarrow\quad T_pN\subset T.
\qquad\text{(1)}
\]

Convergence of planes means convergence in the Grassmannian of \(\dim M\)-planes. Equivalently, their orthogonal projectors converge. Condition **(b)** says that

\[
\begin{gathered}
x_j\in M,\quad y_j\in N,\quad x_j,y_j\to p,\\
T_{x_j}M\to T,\quad\mathbb R(x_j-y_j)\to L
\end{gathered}
\quad\Longrightarrow\quad L\subset T.
\qquad\text{(2)}
\]

The line is unoriented; disjointness makes its defining vector nonzero. Both conditions must hold at every point of \(N\) when we speak of a regular pair.

**Whitney (b) implies Whitney (a).** Fix a sequence and limiting plane as in (1), and a nonzero \(v\in T_pN\). A smooth chart on \(N\) gives a curve \(c\) with

\[
c(0)=p,\qquad c(s)=p+s v+o(s).
\]

Set \(r_j=|x_j-p|>0\), choose \(s_j=\sqrt{r_j}\), and put \(y_j=c(s_j)\). For all sufficiently large \(j\) these points are defined and lie in \(N\). Then

\[
\frac{x_j-y_j}{s_j}
=\frac{x_j-p}{s_j}-v+o(1)\longrightarrow-v.
\qquad\text{(3)}
\]

Thus the secant lines tend to \(\mathbb Rv\). Condition (b) puts that line in \(T\). Every vector of \(T_pN\) is either zero or covered by this argument, which proves (a). This implication uses smoothness alone; it does not need subanalyticity.

For the μ-condition, write \(P_y\) for the orthogonal projector onto \(T_yN\), and \(Q_x\) for the projector onto \((T_xM)^\perp\). A conormal \(\xi\in T^*_{x,M}\mathbb R^n\) is represented by a vector in the image of \(Q_x\). The ordered μ-condition at \(p\in N\) is the following full limiting-sum test:

\[
\begin{gathered}
x_j\in M,\ y_j\in N,\quad x_j,y_j\to p,\\
\xi_j\in(T_{x_j}M)^\perp,\quad
\eta_j\in(T_{y_j}N)^\perp,\\
\xi_j+\eta_j\to\sigma,\qquad
|x_j-y_j|\,|\xi_j|\to0
\end{gathered}
\quad\Longrightarrow\quad \sigma\in(T_pN)^\perp.
\qquad\text{(4)}
\]

This is the coordinate form of
\((T_M^*\mathbb R^n\widehat{+}T_N^*\mathbb R^n)\cap\pi^{-1}(N)\subset T_N^*\mathbb R^n\).
The covectors in (4) may be unbounded. Write \(d_j=|x_j-y_j|\) and \(\sigma_j=\xi_j+\eta_j\). Because \(\sigma_j\) converges, it is bounded, and

\[
d_j|\eta_j|\le d_j|\xi_j|+d_j|\sigma_j|\longrightarrow0.
\]

The reverse inequality interchanges the two covectors. Thus the weighted condition is equivalent to \(d_j(1+|\xi_j|+|\eta_j|)\to0\), as in the [full limiting-sum definition](../../sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#the-product-bounds-in-the-definitions). The sum is symmetric, but the ordered condition is not: its first base approaches through \(M\), and its output must annihilate \(T_pN\).

Conormals over nonclosed strata need not be ambient closed. Formula (4) nevertheless tests their actual points. If a witness is first given in their closures, approximate each base and covector within \(\epsilon_j=1/[j(1+|\xi_j|+|\eta_j|)]\) by an actual conormal point. The sum changes by at most \(2\epsilon_j\), and the new weighted product is bounded by \((d_j+2\epsilon_j)(|\xi_j|+\epsilon_j)\), which still tends to zero. This is the [closure-invariance argument (LG5)–(LG6)](../../sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#limiting-input-closures), with its large-covector scale retained.

The same scale explains coordinate invariance. For a \(C^2\) coordinate change \(h\), put \(A(z)=Dh(z)^{-T}\) on a smaller relatively compact chart. Its transformed sum is \(A(y_j)\sigma_j+(A(x_j)-A(y_j))\xi_j\). The second term has norm at most \(C d_j|\xi_j|\), since \(A\) is locally Lipschitz; the first tends to \(A(p)\sigma\). Local derivative bounds preserve the weighted product, and applying the inverse change gives the converse. These are the [actual coordinate estimates (LG1)–(LG2)](../../sheaf-proof-readings/src/SH03/limiting-cotangent-sums-and-characteristic-inverse-images.md#weighted-coordinate-covariance); no fixed bound for the individual covectors is used.

## A quantitative estimate equivalent to μ

**Conormal estimate.** The condition (4) at \(p\) is equivalent to the existence of a neighborhood \(V\) of \(p\) and a constant \(C\ge0\) such that

\[
|P_y\xi|\le C|x-y|\,|\xi|
\quad
\left(x\in M\cap V,\ y\in N\cap V,
\ \xi\in(T_xM)^\perp\right).
\qquad\text{(5)}
\]

This is Verdier's quantitative \((w)\)-condition, with the lower tangent space compared to the upper one. The equivalence with μ is Trotman's metric theorem, with the [ordered normalization and operator-norm proof](../../sheaf-proof-readings/src/SH03/microlocal-stratifications-by-removing-bad-loci.md#metric-mu-test) given in the preceding programme lesson. Here (5) is the exact local assertion: a single constant controls both moving base points near \(p\). Its equivalence with (4) uses smooth tangent spaces and disjointness, while the later implication to secants uses subanalyticity.

**Proof that μ gives (5).** Failure of (5) means failure for every neighborhood and every constant. Zero conormals cannot violate it; if the upper normal space or lower tangent space is zero, its left side is identically zero. In the remaining case, homogeneity permits a unit conormal. Choose \(x_j,y_j\) within distance \(1/j\) of \(p\), and unit conormals \(\zeta_j\in(T_{x_j}M)^\perp\), such that

\[
a_j:=|P_{y_j}\zeta_j|>j|x_j-y_j|.
\qquad\text{(6)}
\]

Disjointness gives \(|x_j-y_j|>0\), so (6) gives \(a_j>0\). This is the only denominator we need. There is no assumed positive lower bound for \(a_j\), and the resulting covectors need not stay bounded. Define

\[
\xi_j=\frac{\zeta_j}{a_j},\qquad
\eta_j=-\frac{(I-P_{y_j})\zeta_j}{a_j}.
\qquad\text{(7)}
\]

These belong to the required two conormal spaces. Their sum is
\(\sigma_j=P_{y_j}\zeta_j/a_j\), a unit vector tangent to \(N\) at \(y_j\). Pass to a convergent subsequence of the unit sphere. Smoothness of \(N\) at \(p\) gives a unit limit \(\sigma\in T_pN\). At the same time,

\[
|x_j-y_j|\,|\xi_j|
=\frac{|x_j-y_j|}{a_j}<\frac1j\longrightarrow0.
\]

Condition (4) would put this nonzero tangent vector in \((T_pN)^\perp\), a contradiction. Thus (5) holds.

**Proof that (5) gives μ.** For any witness in (4), eventually both bases lie in \(V\). Since \(P_{y_j}\eta_j=0\),

\[
|P_{y_j}(\xi_j+\eta_j)|
=|P_{y_j}\xi_j|
\le C|x_j-y_j|\,|\xi_j|\longrightarrow0.
\]

Only the sums need to be bounded when passing to the limit. Indeed,

\[
|P_p\sigma-P_{y_j}\sigma_j|
\le |\sigma-\sigma_j|+\|P_p-P_{y_j}\|\,|\sigma_j|
\longrightarrow0.
\]

Together with the preceding estimate this gives \(P_p\sigma=0\). Applying this projector difference to \(\xi_j\) alone would be unjustified, since that sequence may diverge. Neither direction of the equivalence uses subanalyticity. \(\square\)

Here is the passage from normal covectors to tangent velocities. The supremum of \(|P_y\xi|\) on the unit ball in \((T_xM)^\perp\) is \(\|P_yQ_x\|\): projecting an arbitrary unit vector by \(Q_x\) cannot increase its norm, and every normal unit vector is already fixed by \(Q_x\). The adjoint is \(Q_xP_y\). For any linear operator, taking unit-ball suprema in \(\langle Av,w\rangle=\langle v,A^*w\rangle\) proves equality of its norm with its adjoint's. The second norm is the supremum of \(|Q_xv|\) on the unit ball in \(T_yN\). Unit balls, rather than unit spheres, include the zero-dimensional cases. Homogeneity therefore makes (5) equivalent to

\[
|Q_x v|\le C|x-y|\,|v|
\qquad(v\in T_yN).
\qquad\text{(8)}
\]

This is the form we need for velocities of a curve in \(N\). Notice that the distance is the distance between the two moving points, not their distance to a fixed frontier point.

## Analytic curves force the secant condition

**Theorem.** For the subanalytic pair above, μ implies Whitney (b), and hence Whitney (a).

**The subanalytic lifting used in the proof.** We need curve selection on the moving tangent planes as well as the two bases. The [pair normal cone (5)–(6) and its subanalyticity proof](../../sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#the-signed-normal-cone-prerequisite) supply the tangent bundle of a smooth subanalytic \(M\):

\[
C(M,M)\cap\pi_{T\mathbb R^n}^{-1}(M)=TM.
\]

To check the fibre at \(q\in M\), write \(M\) locally as the smooth graph of \(g\) on a small convex domain, using an affine orthogonal splitting. If two graph points with horizontal coordinates \(u_j,v_j\to u_0\) have a convergent scaled difference \(c_j(a_j-b_j)\), then \(c_j(u_j-v_j)\) is bounded. The integral mean-value formula gives

\[
g(u_j)-g(v_j)=Dg(u_0)(u_j-v_j)+r_j,
\qquad |r_j|\le\varepsilon_j|u_j-v_j|,
\quad\varepsilon_j\to0.
\]

Thus \(c_jr_j\to0\), and the limiting vector belongs to the graph of \(Dg(u_0)\), namely \(T_qM\). Conversely, a smooth curve in \(M\) through \(q\) with prescribed tangent \(v\) gives \(j(\gamma(1/j)-q)\to v\), including \(v=0\). This proves the fibre equality. Intersecting the subanalytic pair cone with the subanalytic condition that its base lies in \(M\) therefore proves subanalyticity of \(TM\), without assuming an arbitrary smooth Gauss map is analytic.

Choose an orthonormal \(\dim M\)-tuple in this tangent bundle. The frame conditions are polynomial, and all frame vectors lie on unit spheres. Its tangent projector is \(\sum_i v_i v_i^{\mathsf t}\), so its normal projector is \(I-\sum_i v_i v_i^{\mathsf t}\). Projecting away the frame variables is proper on the closure over a compact base-and-projector set: all remaining variables lie in a compact frame space. The [analytic image rule with properness on the selected closure](../../sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#the-local-calculus-with-the-precise-properness-hypothesis) gives exactly the graph of \(Q_x\), not its larger frontier closure. The empty frame for \(\dim M=0\) has tangent projector zero and normal projector the identity.

The normalized secant also has a controlled subanalytic graph at the diagonal. Introduce \(\rho>0\) and a unit vector \(u\) subject to \(\rho^2=|x-y|^2\) and \(\rho u=x-y\). These conditions are polynomial apart from the strict inequality, and \(\rho\) is bounded when the two bases lie in bounded charts. Eliminating \(\rho\) is therefore a projection proper on the local closure; for \(x\ne y\) its image is precisely \(u=(x-y)/|x-y|\). Combining this graph with that of \(Q_x\) proves that the set

\[
\mathcal E=
\left\{\left(x,y,Q_x,\frac{x-y}{|x-y|}\right):
x\in M,\ y\in N\right\}
\qquad\text{(9)}
\]

is subanalytic in the ambient product of the base charts, the compact space of orthogonal projectors and the unit sphere, including at its missing diagonal limit. This is the local subanalyticity required by the [analytic curve-selection proof](../../sheaf-proof-readings/src/SH03/subanalytic-sets-and-limiting-tangent-directions.md#from-a-local-analytic-presentation-to-analytic-curve-selection). That proof supplies a curve analytic across parameter zero; no global definability or analyticity of \(M\) and \(N\) is being added to the stated smooth subanalytic hypotheses.

**Proof of the theorem.** If (b) fails, choose its point \(p\) and sequences in (2) with \(L\not\subset T\). Compactness of the unit sphere permits a subsequence of the actual oriented unit secants converging to \(u\). Their lines still converge to \(L\), so \(|u|=1\) and \(\mathbb Ru=L\). Convergence in the Grassmannian is convergence of the orthogonal projectors. Hence their lifted points in (9) converge to
\((p,p,Q,u)\), where \(Q\) projects onto \(T^\perp\) and \(Qu\ne0\).

Analytic curve selection in (9) supplies analytic curve germs extending to parameter zero,

\[
x(s),\ y(s),\ Q(s),\ u(s),
\qquad s>0,
\qquad\text{(10)}
\]

with the stated limit, and with \(x(s)\in M\), \(y(s)\in N\), \(Q(s)=Q_{x(s)}\),
\(u(s)=(x(s)-y(s))/|x(s)-y(s)|\).
The analytic difference is nonzero for \(s>0\), so it has a finite first nonzero Taylor order:

\[
x(s)-y(s)=s^m v+O(s^{m+1}),
\qquad m\ge1,\quad v\ne0.
\qquad\text{(11)}
\]

Its positive-parameter unit limit is \(v/|v|=u\). Analyticity at zero also makes \(y'(s)\) bounded. For positive parameter the velocities satisfy
\(x'(s)\in T_{x(s)}M\) and \(y'(s)\in T_{y(s)}N\). Apply (8):

\[
\begin{aligned}
Q(s)(x'(s)-y'(s))&=-Q(s)y'(s),\\
|Q(s)y'(s)|&\le C|x(s)-y(s)|\,|y'(s)|=O(s^m).
\end{aligned}
\qquad\text{(12)}
\]

Because the difference in (11) is analytic, differentiation gives \(x'(s)-y'(s)=m s^{m-1}v+O(s^m)\). Orthogonal projectors have norm at most one. Thus after dividing the first line of (12) by \(s^{m-1}\), its left side is \(mQ(s)v+O(s)\), while its right side has norm \(O(s)\) by the second line. Passing to the limit gives \(mQv=0\). Since \(m\ge1\) and \(u=v/|v|\), this contradicts \(Qu\ne0\). This proves (b) at the chosen point; (3) proves (a). \(\square\)

The first nonzero Taylor order is essential. A selected curve can have zero first derivative at zero. The proof differentiates its full leading term and works for every \(m\ge1\).

## A polynomial stratification with a failing secant

In \(X=\mathbb R^3\), with coordinates ordered as \((t,x,y)\), set

\[
\begin{gathered}
g(t,x,y)=y^2-t^2x^2-x^3,\qquad Z=\{g=0\},\\
Z_2=\{x=y=0\},\qquad Z_1=Z\setminus Z_2,
\qquad Z_0=X\setminus Z.
\end{gathered}
\qquad\text{(13)}
\]

**The partition is a subanalytic stratification.** All three pieces are semialgebraic, hence subanalytic. The open \(Z_0\) is a three-dimensional analytic submanifold; \(Z_2\) is the \(t\)-axis. On \(Z_1\), \(x\ne0\): if \(x=0\), the equation forces \(y=0\). Its gradient is

\[
dg=(-2tx^2,-2t^2x-3x^2,2y).
\qquad\text{(14)}
\]

If \(y\ne0\), it is nonzero. If \(y=0\) on \(Z_1\), then \(x=-t^2\ne0\), so \(t\ne0\), and its \(dx\)-component is \(-t^4\ne0\). Thus \(Z_1\) is a smooth analytic hypersurface.

To check all frontier incidences, put \(s=y/x\) on \(Z_1\). Equation (13) gives the parametrization

\[
\Phi(t,s)=\bigl(t,s^2-t^2,s(s^2-t^2)\bigr),
\qquad s\ne t,\ s\ne-t.
\qquad\text{(15)}
\]

For each fixed \(t_0\), taking \(s\to t_0\) through allowed values approaches \((t_0,0,0)\); when \(t_0=0\), use nonzero \(s\to0\). Hence \(\overline{Z_1}=Z\). The line \(Z_2\) is closed. The nonzero polynomial \(g\) has a zero set with empty interior: vanishing on a ball would make all its Taylor coefficients zero there and hence make the polynomial identically zero. Therefore \(\overline{Z_0}=X\).

The respective frontiers are \(Z_1\cup Z_2\), \(Z_2\), and the empty set, each a union of whole lower strata. Disjointness and finite local finiteness are immediate. This proves the required ordinary stratification, including its frontier rule.

Now let \(t_j>0\) tend to zero and choose

\[
a_j=(t_j,-t_j^2,0)\in Z_1,
\qquad b_j=(t_j,0,0)\in Z_2.
\qquad\text{(16)}
\]

At \(a_j\), the conormal in (14) spans \((2t_j,1,0)\). Thus

\[
T_{a_j}Z_1
=\operatorname{span}\{(1,-2t_j,0),(0,0,1)\}
\longrightarrow\operatorname{span}\{e_t,e_y\}.
\qquad\text{(17)}
\]

But \(a_j-b_j=(0,-t_j^2,0)\), so the secant lines are \(\mathbb Re_x\). They are absent from the plane in (17). The pair \((Z_1,Z_2)\) fails Whitney (b) at the origin and therefore cannot satisfy μ.

## The explicit unbounded conormal witness

The failure can also be seen directly in (4), without invoking the implication theorem. At the points in (16) take the covectors

\[
\xi_j=dt+\frac{1}{2t_j}\,dx\in T^*_{a_j,Z_1}X,
\qquad
\eta_j=-\frac{1}{2t_j}\,dx\in T^*_{b_j,Z_2}X.
\qquad\text{(18)}
\]

The first is a scalar multiple of (14), whose value at \(a_j\) is
\(-t_j^4(2t_j,1,0)\). The second kills the tangent \(\mathbb Re_t\) of \(Z_2\). Their sum is exactly \(dt\), and

\[
|a_j-b_j|\,|\xi_j|
=t_j^2\sqrt{1+\frac1{4t_j^2}}
=\frac{t_j}{2}\sqrt{1+4t_j^2}\longrightarrow0.
\qquad\text{(19)}
\]

The limiting sum \(dt\) does not annihilate \(T_0Z_2\). This is a genuine witness in the full limiting sum, with both base points specified and the position–covector product checked. It proves that the finite ordinary stratification (13) is not a μ-stratification.

In (17), the limiting plane does contain \(T_0Z_2\). That particular tangent limit is compatible with Whitney (a). Its failing secant and the cancellation in (18) exhibit the additional information carried by a moving lower base and an unbounded pair of conormals. This observation about one limit does not verify Whitney's condition (a) for the pair.

## A cohomology criterion for a fixed μ-stratification

Let \(X\) now be a real analytic manifold and \(\mathcal S=(S_\alpha)\) a locally finite μ-stratification. Let \(k\) be a commutative ring of finite global dimension and \(F\in D^b(k_X)\). Put
\(\Lambda=\bigcup_\alpha T^*_{S_\alpha}X\). The [closedness proof for the total conormal set](../../sheaf-proof-readings/src/SH03/microlocal-stratifications-by-removing-bad-loci.md#why-the-total-conormal-set-is-closed) uses both ambient local finiteness and μ: a convergent sequence has a subsequence on one stratum. If the source and target strata agree, smooth conormal continuity applies. Otherwise the frontier rule makes them an incident ordered pair, and the bounded conormals form a witness in (4) with the second base fixed and second covector zero. Thus every finite cotangent limit lies in the conormal of its target stratum. Then

\[
\operatorname{SS}(F)\subset\Lambda
\quad\Longleftrightarrow\quad
\operatorname{SS}(H^j(F))\subset\Lambda\quad\text{for every }j.
\qquad\text{(20)}
\]

**Proof.** The [fixed-stratification theorem](../../sheaf-proof-readings/src/SH03/constructibility-from-microsupport-and-perfect-stalks.md#fixed-stratification-criterion) states, for this very \(\mathcal S\), that \(\operatorname{SS}(F)\subset\Lambda\) is equivalent to local constancy of all \(H^j(F)|_{S_\alpha}\). Its forward proof restricts to a stratum by tensoring with its constant extension; the full limiting tensor bound reduces every moving conormal witness to one upper stratum by local finiteness. The ordered μ-condition then removes all tangential covectors, including those left by cancellation of unbounded inputs. Exact closed-embedding microsupport and the zero-section criterion give intrinsic local constancy. Thus the relevant theorem keeps the prescribed strata, not merely some constructible partition.

Apply it first to \(F\), then apply its converse to each degree-zero sheaf \(H^j(F)\). The [converse proof by closed-residual induction](../../sheaf-proof-readings/src/SH03/constructibility-from-microsupport-and-perfect-stalks.md#closed-residual-induction) uses the actual missing-submanifold boundary estimate and the same full μ-condition. This proves the forward implication of (20), without assuming any individual \(\operatorname{SS}(H^j(F))\) is contained in \(\operatorname{SS}(F)\).

For the reverse implication, choose a finite interval containing all nonzero cohomology of \(F\). The canonical truncation triangles build \(F\) from the finitely many \(H^j(F)[-j]\). The [triangle inequality and shift invariance, (T21)–(T23)](../../sheaf-proof-readings/src/SH02/microsupport-tests.md#sh02-mst-formal--consequences-that-do-not-require-a-propagation-estimate), put its microsupport in the union of their microsupports and hence in \(\Lambda\). This second argument needs boundedness and the triangle estimate, but does not itself need the μ-condition. \(\square\)

There is no perfect-stalk or finite-generation assumption in (20), and no splitting of the truncation triangles. The forward implication retains the prescribed stratification, rather than merely producing some unrelated constructible partition.

## Exercises with complete solutions

### Read the failed secant in the correct coordinate order

*Difficulty: Introductory.*

Use \(t_j=1/j\) in (16). Compute the normal, limiting tangent plane and limiting secant line. Does this tangent-plane limit alone violate Whitney (a)?

**Solution.** The gradient is \((-2/j^5,-1/j^4,0)\), whose span is the span of \((2/j,1,0)\). Its orthogonal plane is spanned by \((1,-2/j,0)\) and \((0,0,1)\), so the limit is the \((t,y)\)-plane. The secant vector is \((0,-1/j^2,0)\), giving the \(x\)-axis as its line. The line is not in the limiting plane, which violates (b). The lower tangent is the \(t\)-axis and is in that plane, so this tangent-plane limit alone does not violate (a). Interchanging \(x\) and \(y\) would change the asserted failed direction and give an incorrect calculation.

### Why a bounded normal cannot replace the cancelling witness

*Difficulty: Intermediate.*

Normalize the upper normal in the preceding exercise to unit length. Find its limit, and compare its conclusion with (18). Verify that replacing \(\xi_j\) in (18) by \(2t_j\xi_j\), and scaling \(\eta_j\) by the same factor, loses the violation.

**Solution.** A unit upper normal is \(\zeta_j=(2t_j,1,0)/\sqrt{1+4t_j^2}\); it tends to \(dx\), which is a conormal to the lower \(t\)-axis. Thus this ordinary bounded conormal limit has no forbidden tangential component. In (18), the diverging \(dx\)-components cancel and leave the nonzero tangential covector \(dt\). After the proposed common scaling, the covectors become \(2t_jdt+dx\) and \(-dx\), and their sum tends to zero. Zero is conormal to every lower stratum. The product condition still holds, but the nonconormal output has disappeared. The full test must therefore allow the original unbounded factors.

### Measure the failure of the quantitative estimate

*Difficulty: Intermediate.*

At \(a_j,b_j\) in (16), compute the ratio in (5) for the unit normal \(\zeta_j\). Relate it to the scale used in (7).

**Solution.** Projection onto the lower tangent takes \(\zeta_j\) to its \(dt\)-component, of magnitude \(2t_j/\sqrt{1+4t_j^2}\). Since \(|a_j-b_j|=t_j^2\), the ratio is

\[
\frac{|P_{b_j}\zeta_j|}{|a_j-b_j|\,|\zeta_j|}
=\frac{2}{t_j\sqrt{1+4t_j^2}}\longrightarrow\infty.
\qquad\text{(21)}
\]

No fixed constant works on any neighborhood of the origin. Dividing \(\zeta_j\) by \(a_j^{\mathrm{norm}}=2t_j/\sqrt{1+4t_j^2}\) gives exactly the first covector of (18). Its lower normal component is cancelled by the second covector. The quantitative failure and the full limiting-sum witness are the same mechanism, expressed before and after normalization. Here \(a_j^{\mathrm{norm}}\) denotes the normalization scalar, not the point \(a_j\).

### Repair the surface by isolating one frontier point

*Difficulty: Advanced.*

Show that the four-piece partition
\(Z_0,Z_1,Z_2\setminus\{0\},\{0\}\) is a μ-stratification. Strata are allowed to be disconnected.

**Solution.** The pieces are analytic submanifolds of dimensions \(3,2,1,0\) and are semialgebraic. Their closures follow from (15): \(\overline{Z_0}=X\), \(\overline{Z_1}=Z\), \(\overline{Z_2\setminus\{0\}}=Z_2\), and the origin is closed. Thus every frontier is a union of whole lower pieces.

Any ordered pair with the point as lower stratum satisfies μ, because its conormal is the whole fibre. Any pair with \(Z_0\) as upper stratum satisfies μ: its first covector is zero, and the second conormal converges normally at a smooth point of the target. It remains to check \((Z_1,Z_2\setminus\{0\})\).

Near \((t_0,0,0)\) with \(t_0\ne0\), take a neighborhood where \(|t|\) is bounded below and \(t^2+x\) is positive and bounded below. The two upper sheets have equations
\(y=Y_\pm(t,x)=\pm x\sqrt{t^2+x}\), with \(x\ne0\). An upper conormal is a multiple of \((-\partial_tY_\pm,-\partial_xY_\pm,1)\), and
\(|\partial_tY_\pm|=|xt|/\sqrt{t^2+x}\le C_0|x|\).
Its norm is at least the absolute value of that multiple. For a lower point \(b=(t',0,0)\), \(|(t,x,Y_\pm)-b|\ge|x|\). Projection of the normal to the lower tangent therefore obeys (5), with a uniform constant on both sheets. The equivalence already proved gives μ at every nonzero lower point. These checks exhaust all incident ordered pairs. The four-piece partition is the claimed refinement.

### The scale in the proof that (b) implies (a)

*Difficulty: Intermediate.*

In (3), replace \(s_j=\sqrt{r_j}\) by \(s_j=r_j^\alpha\), with \(0<\alpha<1\). Prove that the argument still works. Explain why choosing \(s_j=r_j\) would not prove the same assertion from those estimates alone.

**Solution.** We have \(s_j\to0\) and \(r_j/s_j=r_j^{1-\alpha}\to0\), so the first term in (3) still tends to zero. The selected secant has limit direction \(-v\), giving the required tangent line. If \(s_j=r_j\), the vector \((x_j-p)/s_j\) has norm one; it need not tend to zero. For example, a sequence approaching in a fixed normal direction would retain that normal vector in the normalized difference. The resulting secant would combine that direction with \(-v\). Condition (b) would then control a different line, so the stated estimate would not isolate \(\mathbb Rv\).

### Cohomology bounds without splitting the complex

*Difficulty: Advanced.*

Prove (20) for a bounded complex supported in an arbitrary finite cohomological interval. Specify exactly where the common μ-stratification is used and where no finiteness of stalk modules is needed.

**Solution.** If \(\operatorname{SS}(F)\subset\Lambda\), the fixed-stratification theorem makes every cohomology restriction locally constant on each specified stratum. Its application to the sheaf \(H^j(F)\), concentrated in degree zero, puts that sheaf's microsupport in the same \(\Lambda\). This is the step using the ordered μ-condition, including unbounded conormal cancellation in the underlying restriction estimate.

Conversely, suppose each cohomology microsupport is in \(\Lambda\), and \(H^j(F)=0\) outside \([a,b]\). For \(a\le j\le b\), use
\(\tau^{\le j-1}F\to\tau^{\le j}F\to H^j(F)[-j]\xrightarrow{+1}\).
The initial \(\tau^{\le a-1}F\) is zero. Induction with the triangle inequality gives the bound for every \(\tau^{\le j}F\); at \(j=b\) this is \(F\). These triangles can have nonzero connecting maps; their splitting is unnecessary. The induction has finitely many steps because \(F\) is bounded. Neither the geometric local-constancy criterion nor the triangle estimate assumes finite generation or perfect stalks, so arbitrary weak coefficients are permitted under the standing ring hypothesis.

### Open-star restriction has covariant face variance

*Difficulty: Introductory.*

For a locally finite simplicial complex, let \(\sigma\le\tau\) mean that \(\sigma\) is a face of \(\tau\). Explain why \(F\mapsto\{\Gamma(U_\sigma;F)\}\) gives a covariant face diagram, and identify the value for the sheaf constructed from a diagram \(A\) by the equivalence in the triangulation lesson. Does this require finite coefficient modules?

**Solution.** We have \(U_\tau\subset U_\sigma\), so ordinary restriction of sections goes from \(\Gamma(U_\sigma;F)\) to \(\Gamma(U_\tau;F)\), in the same direction as the face arrow \(\sigma\to\tau\). Composition of restrictions gives the diagram's composition law.

For the sheaf constructed from \(A\), the open-star section theorem identifies \(\Gamma(U_\sigma;F)\) with \(A_\sigma\). A value in \(A_\sigma\) continues to each coface through the specified map \(A_\sigma\to A_\tau\); the composition law makes these continuations compatible. Conversely, a star section is determined by its value on \(\sigma^\circ\), as the local germ-continuation proof in that lesson shows. These identifications commute with restrictions and with morphisms of diagrams. Together with the [sheaf reconstruction theorem](../../sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#modules-that-continue-into-larger-faces) and its [open-star section comparison](../../sheaf-proof-readings/src/SH03/constructible-sheaves-on-a-triangulation.md#sections-on-a-star), they give natural inverse equivalences between face diagrams and sheaves constant on each open simplex. The argument works for arbitrary modules over the commutative ring; it uses local finiteness of the simplicial complex, not finite generation of the values.

## What these exercises add to constructibility

The polynomial example checks the frontier rule explicitly while exposing a moving secant that the tangent plane misses. Its unbounded normal witness explains the distance–covector product in μ. Conversely, the quantitative estimate and analytic curve-selection proof account for every failed secant, including curves whose first derivative at zero vanishes. The fixed-stratification cohomology criterion then lets us retain this same geometric control while passing between a bounded complex and its individual cohomology sheaves.

## References

David J. A. Trotman, [*Une version microlocale de la condition (w) de Verdier*](https://www.numdam.org/item/10.5802/aif.1190.pdf#page=3), Annales de l’Institut Fourier 39 (1989), no. 3, pp. 825–829, gives the limiting conormal sum in §1 and proves its equivalence with (w) in §2. The normalization in (6)–(7) is that classical mechanism, expressed here through moving orthogonal projectors.

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=144), Astérisque 128 (1985), §8.1, pp. 141–143, treats Whitney stratifications and the closedness of their total conormal set. Its flatness condition in Definition 8.1.1 concerns the canonical form on a normal cone; it should be distinguished from the stronger metric condition (w) proved equivalent to μ here.
