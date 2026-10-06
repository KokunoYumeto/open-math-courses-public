# Whitney secants and the microlocal stratification condition

Tangent planes and secant lines answer different questions at a frontier. A limiting tangent plane records directions within the approaching stratum. A secant joins a point of that stratum to a moving point of the lower stratum. The μ-condition controls both: its allowance for large cancelling conormal covectors forces a quantitative estimate, and subanalytic curve selection converts that estimate into Whitney's secant condition. A polynomial surface will show exactly how this control can fail.

Let \(M,N\subset\mathbb R^n\) be disjoint subanalytic smooth submanifolds of fixed dimensions, with \(N\subset\overline M\setminus M\). The manifold and subanalytic conventions are those of Microlocal stratifications by removing bad loci. Analytic strata satisfy these hypotheses. We use the Euclidean metric to identify covectors and vectors, but retain their different roles. All norms and distances below are Euclidean. No coefficient ring enters the geometric arguments.

The subanalytic normal-cone operations and the analytic curve-selection theorem are proved in Subanalytic sets and limiting tangent directions. This lesson relates Whitney's secant condition to the microlocal stratification condition of M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §8.1. The triangulation case is proved in Constructible sheaves on a triangulation.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

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
The covectors in (4) may be unbounded. The first conormal belongs to the approaching stratum \(M\); the conclusion concerns the lower stratum \(N\).

## A quantitative estimate equivalent to μ

**Conormal estimate.** The condition (4) at \(p\) is equivalent to the existence of a neighborhood \(V\) of \(p\) and a constant \(C\ge0\) such that

\[
|P_y\xi|\le C|x-y|\,|\xi|
\quad
\left(x\in M\cap V,\ y\in N\cap V,
\ \xi\in(T_xM)^\perp\right).
\qquad\text{(5)}
\]

This is the quantitative tangent-gap condition usually called Verdier's (w)-condition, with the lower tangent space compared to the upper one. Here its exact content is (5).

**Proof that μ gives (5).** If no such neighborhood and constant exist, choose \(x_j,y_j\) within distance \(1/j\) of \(p\), and unit conormals \(\zeta_j\in(T_{x_j}M)^\perp\), such that

\[
a_j:=|P_{y_j}\zeta_j|>j|x_j-y_j|.
\qquad\text{(6)}
\]

In particular \(a_j>0\). Define

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

The sums converge and \(P_{y_j}\to P_p\), so \(P_p\sigma=0\). This is the desired conclusion. Neither direction of this equivalence uses subanalyticity. \(\square\)

The adjoint operators \(P_yQ_x\) and \(Q_xP_y\) have the same norm. Estimate (5) therefore also says

\[
|Q_x v|\le C|x-y|\,|v|
\qquad(v\in T_yN).
\qquad\text{(8)}
\]

This is the form we need for velocities of a curve in \(N\). Notice that the distance is the distance between the two moving points, not their distance to a fixed frontier point.

## Analytic curves force the secant condition

**Theorem.** For the subanalytic pair above, μ implies Whitney (b), and hence Whitney (a).

**The subanalytic lifting used in the proof.** The graph of \(x\mapsto T_xM\), represented by orthogonal projectors, is subanalytic, even near a frontier point where it need not extend continuously. To see the needed assertion, the pair normal cone \(C(M,M)\), restricted to base points of the smooth \(M\), has fibre \(T_xM\). Indeed, in a smooth graph chart the difference of two nearby points has its leading direction tangent to that graph at the limiting point; every tangent vector is realized by two curves in the chart. Normal-cone subanalyticity thus gives the tangent bundle as a subanalytic set over \(M\).

Choose an orthonormal \(\dim M\)-tuple in this tangent bundle. The conditions on the tuple are polynomial and all tuple entries lie on unit spheres. Add its projector \(\sum_i v_i v_i^{\mathsf t}\), then project away the frame variables. Their ambient factor is compact, so the local bounded-projection rule for subanalytic sets gives precisely the tangent-projector graph. The normalized secant
\((x-y)/|x-y|\) is semialgebraic as a function of \(x\ne y\). Consequently the set

\[
\mathcal E=
\left\{\left(x,y,Q_x,\frac{x-y}{|x-y|}\right):
x\in M,\ y\in N\right\}
\qquad\text{(9)}
\]

is subanalytic locally in the product of the base charts, the compact space of orthogonal projectors, and the unit sphere. These are applications of the named normal-cone, bounded-projection and curve-selection prerequisites, rather than an assumption that an arbitrary smooth Gauss map is subanalytic.

**Proof of the theorem.** If (b) fails, take sequences in (2) with \(L\not\subset T\). Pass to a subsequence so their unit secants converge to a unit vector \(u\in L\). Their lifted points in (9) converge to
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

Differentiating (11), dividing (12) by \(s^{m-1}\), and taking the limit gives
\(Q(mv)=0\). Thus \(Qu=0\), contrary to the chosen failed secant. This proves (b); (3) proves (a). \(\square\)

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

In (17), the limiting plane does contain \(T_0Z_2\). That particular tangent limit is compatible with Whitney (a). Its failing secant, and the cancellation in (18), exhibit the additional phenomenon that Exercise VIII.12 requires us to control. This observation about one limit does not verify Whitney's condition (a) for the pair.

## A cohomology criterion for a fixed μ-stratification

Let \(X\) now be a real analytic manifold and \(\mathcal S=(S_\alpha)\) a locally finite μ-stratification. Let \(k\) be a commutative ring of finite global dimension and \(F\in D^b(k_X)\). Put
\(\Lambda=\bigcup_\alpha T^*_{S_\alpha}X\), which is closed by the μ-condition. Then

\[
\operatorname{SS}(F)\subset\Lambda
\quad\Longleftrightarrow\quad
\operatorname{SS}(H^j(F))\subset\Lambda\quad\text{for every }j.
\qquad\text{(20)}
\]

**Proof.** The fixed-stratification theorem in Constructibility from microsupport and perfect stalks states, for this very \(\mathcal S\), that \(\operatorname{SS}(F)\subset\Lambda\) is equivalent to local constancy of all \(H^j(F)|_{S_\alpha}\). Applying that theorem to each degree-zero sheaf \(H^j(F)\) proves the forward implication of (20).

For the reverse implication, choose a finite interval containing all nonzero cohomology of \(F\). The canonical truncation triangles build \(F\) from the finitely many \(H^j(F)[-j]\). The microsupport triangle inequality and shift invariance put its microsupport in the union of their microsupports and hence in \(\Lambda\). This second argument needs boundedness and the triangle estimate, but does not itself need the μ-condition. \(\square\)

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

For the sheaf constructed from \(A\), the open-star section theorem identifies \(\Gamma(U_\sigma;F)\) with \(A_\sigma\). A value in \(A_\sigma\) continues to each coface through the specified map \(A_\sigma\to A_\tau\); the composition law makes these continuations compatible. Conversely, a star section is determined by its value on \(\sigma^\circ\), as the local germ-continuation proof in that lesson shows. These identifications commute with restrictions and with morphisms of diagrams. Together with the sheaf reconstruction proved there, they are the natural inverse equivalences required in Exercise VIII.1. The argument works for arbitrary modules over the commutative ring; it uses local finiteness of the simplicial complex, not finite generation of the values.

## What these exercises add to constructibility

The polynomial example checks the frontier rule explicitly while exposing a moving secant that the tangent plane misses. Its unbounded normal witness explains the distance–covector product in μ. Conversely, the quantitative estimate and analytic curve-selection proof account for every failed secant, including curves whose first derivative at zero vanishes. The fixed-stratification cohomology criterion then lets us retain this same geometric control while passing between a bounded complex and its individual cohomology sheaves.
