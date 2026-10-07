# Existence and compactness of generalized reflected curves

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="generalized-reflected-curves"></a>

This reading constructs an energy-preserving constrained Hamilton relation on a compact smooth manifold with boundary. It proves existence, continuation, compactness, the exact tangential equations, transverse reflection and the exclusion of boundary residence at strict diffraction. The construction allows gliding and arbitrary degenerate contact; it assumes neither finite contact order nor uniqueness. The [singular-curve construction for Dirichlet waves](diffractive-phase-neighborhoods.md#singular-generalized-curves), Sections 63–70, proves that a suitable singular curve for the actual H² wave belongs to this precise relation on homogeneous time intervals. Its [Cauchy-data propagation for Dirichlet waves](diffractive-phase-neighborhoods.md#dirichlet-cauchy-endpoints) in Sections 71–75 also proves the initial-data endpoint argument and the transfer to every required negative order for compact interior spectral data.

The freely accessible comparison is Victor Ivrii's [*Microlocal Analysis, Sharp Spectral Asymptotics and Applications*, author version of July 9, 2023](https://www.math.utoronto.ca/ivrii/Victor_Ivrii_Microlocal_Analysis,_Sharp_Spectral_Asymptotics_and_Applications.pdf), Definition 3.2.2, printed pp. 228–229, and the refined single-quadratic-block relation (3.4.57)–(3.4.58) and Theorem 3.4.10, especially (3.4.57)*, printed p. 266. The first locator describes the compressed topology; the second imposes the additional boundary direction restriction. The construction below proves existence and compactness directly for the scalar relation defined in (G4).

We use ordinary integration, change of variables, smooth coordinate cutoffs and the local inverse theorem already proved in [Coordinate inverses and integration](coordinate-inverses-and-integration.md), and the scalar integral estimates in [Hilbert-valued integration](hilbert-valued-integration.md). The finite-dimensional flow, compactness and collision-count arguments needed here are supplied explicitly.

<a id="reflected-collar-and-relation"></a>

## 1. The relation and the normal reaction

Let $X$ be compact, with smooth boundary and no corners. Let $p$ be the positive definite quadratic symbol of a smooth Riemannian metric. First normalize the energy to $p=1$ and use the parameter $\sigma$ of $H_p$. In a boundary normal collar write

\[
 \begin{gathered}
 p=s^2+r(d,y,\eta),\\
 r=\eta^TG(d,y)\eta,\qquad d\geq0,
 \end{gathered}
 \tag{G1}
\]

where $s$ is the inward normal covector. Here is the required normal-coordinate construction. Write $g_{ij}$ for the inverse of the principal-symbol matrix and set

\[
 \Gamma^k_{ij}=\tfrac12g^{k\ell}
 (\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}).
\]
Solve $F_{dd}^k=-\Gamma^k_{ij}(F)F_d^iF_d^j$ with $F(0,y)$ on the wall and $F_d(0,y)$ its inward unit normal. Section 3 proves smooth local solutions and parameter dependence for this finite-dimensional equation. At $d=0$ the columns $F_d,F_{y_j}$ are independent, so the local inverse theorem gives collar coordinates. Substitution of the displayed Christoffel formula gives $\partial_d g(F_d,F_d)=0$ and
$\partial_d g(F_d,F_{y_j})=\tfrac12\partial_{y_j}g(F_d,F_d)=0$.
Their initial values are one and zero, respectively. Thus the metric is $dd^2$ plus a positive tangential metric, and its inverse symbol is (G1). Compactness of the wall gives a common small collar width: otherwise two colliding normal-coordinate points with widths tending to zero would converge to the same boundary point, contradicting the local inverse there. The tangential coordinates are transported along this collar, so changes between such charts depend only on $y$. In the interior the Hamilton equations are

\[
 \begin{aligned}
 d'&=2s,&s'&=-r_d,\\
 y'&=r_\eta=2G\eta,&\eta'&=-r_y.
 \end{aligned}
 \tag{G2}
\]

The *compressed energy space* identifies $(0,y,s,\eta)$ and $(0,y,-s,\eta)$. On $p=1$ its local continuous coordinates can be taken as

\[
 (d,y,\eta,v),\qquad v=ds.
 \tag{G3}
\]

For $d>0$ these recover $s$; for $d=0$ the energy determines the two possible lifts $s=\pm\sqrt{1-r(0,y,\eta)}$. At glancing the two coincide. The energy shell is compact. Its quotient is compact and metrizable: in finitely many collar and interior charts, take coordinate functions multiplied by smaller-chart cutoffs, including $ds$ in collar charts. These finitely many continuous functions separate compressed points and give a homeomorphism onto their compact image in a Euclidean space. To see the last assertion, a continuous bijection from a compact space to a Hausdorff space maps closed sets to compact, hence closed, sets. The equivalence relation is closed because at a limiting wall point energy still determines exactly the two opposite normal lifts.

Here is the precise class of curves used in this reading. In an interior chart they solve the ordinary Hamilton equations. In each collar interval, $d,y,\eta$ are absolutely continuous, $s$ has bounded variation, and the following equalities hold almost everywhere:

\[
 \begin{aligned}
 d'&=2s,\quad y'=r_\eta,\quad\eta'=-r_y,\\
 s^2+r(d,y,\eta)&=1,\\
 s(\sigma)&=M(\sigma)\\
       &\quad-\int_{\sigma_0}^{\sigma}r_d(d,y,\eta)(a)\,da.
 \end{aligned}
 \tag{G4}
\]

The function $M$ is nondecreasing and is constant on every open interval where $d>0$. Additive constants in $M$ are immaterial. Its increase is the inward normal reaction. Values of $s$ at a jump are represented by its two one-sided lifts; changing its value at the jump does not change (G4). This definition is invariant under the stated tangential changes of normal coordinates. It is also invariant under reversal of the trajectory together with reversal of all spatial covectors.

No unspecified motion along a boundary cone is included. The exact tangential equations and energy are part of the definition, and the sign of the normal reaction will rule out artificial residence at a diffractive point. The definition does not assert that a wave propagates along these curves.

<a id="reflected-reaction-and-contact"></a>

## 2. Uniform estimates and the contact laws

On a retained compact chart, energy bounds $|s|,|\eta|$ and all right sides in (G2) by fixed constants. On a collar interval $[a,b]$, monotonicity and (G4) give

\[
 \begin{aligned}
 0\leq M(b)-M(a)
       &\leq 2+C(b-a),\\
 \operatorname{Var}_{[a,b]}s
       &\leq2+2C(b-a).
 \end{aligned}
 \tag{G5}
\]

Endpoint values are taken one-sided within the interval. In particular infinitely many small reflections do not destroy this bound.

We recall the elementary meaning of the variation calculation. A bounded nondecreasing function has left and right limits, since each is a supremum or infimum of its nearby values. It has at most countably many jumps: for each positive integer $k$, disjoint jumps of size at least $1/k$ are finite on a bounded interval. For a continuous $f$, sums $\sum f(t_i)(M(t_i)-M(t_{i-1}))$ converge as the mesh tends to zero. Two such sums differ by at most the modulus of continuity of $f$ times the total increase. This defines $\int f\,dM$, is nonnegative for $f\geq0$, and vanishes when $f$ is supported in an interval where $M$ is constant. Summation by parts gives integration by parts against smooth test functions. Applying the same sums to the product of an absolutely continuous Lipschitz function and $s=M$ minus a smooth integral proves the usual product rule, including its jumps. This supplies the bounded-variation operations below without a compactness or measure representation theorem being assumed.

Put $v=ds$. Because $d=0$ on the support of the increase of $M$, the product rule gives

\[
 v'=2s^2-dr_d=2(1-r)-dr_d.
 \tag{G6}
\]

For the vanishing term, cover the closed zero set of $d$ by a neighborhood where $|d|<\epsilon$; the Stieltjes integral there is at most $\epsilon\operatorname{Var}M$, while its complement is a union of intervals on which $M$ is constant. Let $\epsilon$ decrease to zero. Thus (G6) is an equality of distributions with a bounded continuous right side. It follows by subtracting its ordinary integral that $v$ has the stated continuously differentiable representative. The same elementary distribution argument applies to the tangential equations in (G4). Therefore

\[
 y,\eta,v\in C^1,\qquad
 d\text{ is uniformly Lipschitz}.
 \tag{G7}
\]

The compressed coordinates are uniformly Lipschitz on bounded intervals. Interior charts have the same property by (G2). A finite chart cover and smaller-chart cover make these estimates uniform on the compact normalized space. One may subdivide time while a curve moves between the smaller and larger chart boundaries; their positive separation and the bounded coordinate speeds give a uniform positive time for such an exit. This also gives equicontinuity in the finite-coordinate metric from Section 1.

Let $d(\sigma_*)=0$ and set $a_*^2=1-r(0,y(\sigma_*),\eta(\sigma_*))$. The one-sided limits of $s$ exist by (G4). By taking sequences of points at which energy holds, their squares equal $a_*^2$. Since $d\geq0$ and $d'=2s$, one-sided averaging of this last equation gives

\[
 s(\sigma_*-)\leq0,\qquad
 s(\sigma_*+)\geq0.
 \tag{G8}
\]

If $a_*>0$, these limits are $-a_*,+a_*$. Their nonzero signs imply $d>0$ on punctured one-sided neighborhoods of $\sigma_*$. Thus this is an isolated transverse reflection, with

\[
 \begin{gathered}
 s_+=-s_-,\qquad\Delta M=2a_*,\\
 y,\eta\text{ are unchanged}.
 \end{gathered}
 \tag{G9}
\]

If $a_*=0$, both normal limits are zero, so there is no jump. This covers arbitrary glancing contact, including accumulation of transverse reflections. On any interval of boundary residence, (G4) reduces to

\[
 \begin{gathered}
 d=s=0,\qquad M'=r_d\geq0,\\
 y'=r_\eta(0,y,\eta),\\
 \eta'=-r_y(0,y,\eta).
 \end{gathered}
 \tag{G10}
\]

At strict diffraction $r_d<0$, more is true. In a neighborhood where $-r_d\geq\kappa>0$, (G4) implies, in distributions,

\[
 d''=2s'\geq2\kappa.
 \tag{G11}
\]

Hence $d-\kappa(\sigma-\sigma_*)^2$ is convex. Indeed its derivative is nondecreasing by the same integral representation. At a glancing contact its left and right derivatives at $\sigma_*$ are zero, so integration of these derivative inequalities gives

\[
 d(\sigma)\geq\kappa(\sigma-\sigma_*)^2.
 \tag{G12}
\]

Consequently the curve lies in the interior on both punctured sides of a strict diffractive contact. There $M$ is constant; continuity of $s$ at the contact makes the two ordinary Hamiltonian legs the single smooth Hamilton trajectory through it, by the uniqueness argument in the next section. Boundary creeping has been excluded by a proof, rather than by a name for the curve. No finite-order assumption is imposed where $r_d=0$.

<a id="reflected-ordinary-flow"></a>

## 3. Ordinary trajectories on a set of full volume

We first construct enough genuine billiard trajectories to approximate every compressed initial point. Extend the metric smoothly across coordinate portions of the wall when solving the local ordinary equation. For a smooth bounded vector field $V$ with derivative bound $L$ on a ball, the map

\[
 z(\sigma)\longmapsto z_0+
             \int_0^\sigma V(z(a))\,da
 \tag{G13}
\]

preserves a smaller closed path ball for a short time and has contraction factor $LT<1$. Iterating it produces a uniformly Cauchy sequence, because successive differences form a geometric series. Its limit solves the integral equation. Applying the same estimate to two solutions proves uniqueness and continuous dependence, with difference bound $|z_0-w_0|/(1-LT)$. The derivative in the initial point solves $J=I+\int DV(z)J$, again a contraction on this short interval. Taylor's formula for $V$ shows that the difference quotient minus this solution is bounded by a remainder tending uniformly to zero divided by $1-LT$. Hence this is the actual derivative, not just a formal differentiated equation. Repeating Taylor's formula and this linear integral estimate proves every higher derivative; the inhomogeneous terms use only the already obtained lower derivatives and bounded derivatives of $V$. This proves smooth parameter dependence. Extension by repeated short intervals is possible while the trajectory remains in a compact coordinate region.

At a transverse wall hit, $d'=2s\ne0$. The already proved inverse theorem gives a smooth first hitting time locally. Reflect $s$ and retain $y,\eta$; this continues the trajectory uniquely. A trajectory with finitely many transverse hits therefore has smooth dependence in each fixed collision itinerary. There are countably many such local charts, since ordinary coordinate neighborhoods have a countable base.

<a id="reflected-flux-and-collisions"></a>

Here are the volume and collision-count details needed to exclude finite-time failure on a set of positive volume. In phase coordinates, the divergence of $H_p=(p_\xi,-p_x)$ is zero, by equality of mixed partial derivatives. Its flow derivative $J$ solves $J'=DV\,J$. The multilinear derivative formula for a determinant gives

\[
 (\det J)'=(\operatorname{div}V)\det J=0.
 \tag{G14}
\]

The chain rule also gives $(p\circ z)^\prime=\sum_i(p_{x_i}p_{\xi_i}-p_{\xi_i}p_{x_i})=0$. Thus the ordinary flow preserves $dx\,d\xi$ and $p$. On $p=E$ define the energy density by solving for any coordinate with nonzero derivative of $p$: it is the density for which the phase change of variables has the form $dx\,d\xi=dE\,d\nu_E$. Independence of the solved coordinate is precisely the change-of-variables formula. Since the flow preserves both the full density and $E$, its tangential Jacobian preserves $\nu_E$. This follows pointwise in $E$ by smoothness, rather than just almost everywhere. At $E=1$ the resulting positive density $\nu$ is finite on the compact energy shell.

On the incoming wall section $s<0$, use coordinates $(y,\eta)$ with $r(0,y,\eta)<1$. The energy density in coordinates $(d,y,\eta)$ is $|2s|^{-1}\,dd\,dy\,d\eta$. Multiplication by the crossing speed $|d'|=2|s|$ gives the incoming flux

\[
 \begin{gathered}
 d\lambda=dy\,d\eta,\\
 \Lambda=\lambda(\{d=0,s<0,p=1\})<\infty.
 \end{gathered}
 \tag{G15}
\]

This is an intrinsic density: a tangential coordinate change has reciprocal Jacobians in $y$ and $\eta$. Finitely many charts and a partition give its finite global integral. Reflection preserves it because it fixes $(y,\eta)$.

For completeness, the flux is also preserved from one transverse section to the next. In a flow tube from the first section the energy density is $d\sigma\,d\lambda$, by (G14) and its value at the section. If the next section is reached at time $T(b)$ and at point $K(b)$, the change between the two tube coordinates is $(\sigma,b)\mapsto(\sigma-T(b),K(b))$. Comparing the same energy density in these coordinates shows that $K$ preserves $\lambda$: the time derivative is one and its derivatives in $b$ do not enter the determinant. Equivalently the flux form is the contraction of the energy volume form with $H_p$; pulling it back by $b\mapsto\Phi_{T(b)}b$ removes every term containing a second $H_p$, leaving its original value. Either calculation is the same finite Jacobian identity. Together with reflection, it proves that every finite regular billiard itinerary preserves energy volume and transverse flux.

Let $N_T(z)$ count transverse collisions reached before time $T>0$, stopping the construction if it encounters a singularity. For the $k$th such collision the map

\[
 z\longmapsto(b_k(z),t_k(z))
 \tag{G16}
\]

is locally a smooth change of variables with density $d\nu= d\lambda\,dt$. The images for different $k$ are disjoint: from the specified incoming collision state and its specified time, backward reflection and ordinary uniqueness reconstruct the initial point and all its finite preceding collisions. A pair cannot describe two different collision numbers. Break the countably many local itinerary charts into disjoint measurable pieces to use the ordinary change-of-variables formula without overlap. Summing gives

\[
 \sum_{k\geq1}\nu\{z:N_T(z)\geq k\}
       \leq T\Lambda.
 \tag{G17}
\]

It suffices to sum through a finite $k$ and then take increasing limits of nonnegative integrals. In particular

\[
 \nu\{N_T\geq K\}\leq T\Lambda/K.
 \tag{G18}
\]

The set with infinitely many collisions before $T$ has volume zero, by decreasing these sets as $K\to\infty$.

A first tangential collision, after finitely many transverse ones, also occurs for a volume-zero set of initial data. The grazing wall section has coordinates $s=d=0$, $r(0,y,\eta)=1$. The last equality is regular because $r_\eta=2G\eta\ne0$ there. Its dimension is $2n-3$; allowing the hitting time gives dimension $2n-2$, while the energy shell has dimension $2n-1$. Flowing backward from this section and through a specified finite transverse itinerary is smooth on each local chart. A smooth map from a lower-dimensional chart has zero volume image: on each compact coordinate cube it is Lipschitz, and covering its domain by $O(\epsilon^{-m})$ cubes of side $\epsilon$ covers its image by that many ambient balls of volume $O(\epsilon^{m+1})$. Let $\epsilon\to0$ and then use countably many compact cubes. This proves the claim without a transversality or Sard theorem being invoked. For $n=1$ the grazing section is empty.

There is no other finite-time obstruction. After finitely many impacts, an interior trajectory in a compact energy set has a limit by the bounded smooth equations; it either continues in the interior or reaches the wall transversely or tangentially. Infinite impacts were treated by (G18). Taking all positive integer $T$ and both time directions proves that a full-volume, hence dense, set of interior energy points has a trajectory defined for all $\sigma\in\mathbb R$, with only finitely many transverse reflections on each bounded interval. Such trajectories satisfy (G4), with $M$ increasing by $2|s|$ at each reflection.

<a id="reflected-compactness"></a>

## 4. Compactness without a finite-contact assumption

Consider any sequence of curves satisfying (G4) on a common bounded interval, including curves already having gliding or degenerate contacts. The uniform compressed-coordinate bounds in Section 2 give a uniformly convergent subsequence. Here is the compactness proof: choose subsequences successively at a countable dense set of times, using compactness of the compressed energy space, and take the diagonal subsequence. Given $\epsilon>0$, equicontinuity provides a finite time mesh on which closeness implies closeness everywhere within $3\epsilon$. Convergence at that mesh proves the subsequence is uniformly Cauchy. Its limit is continuous and has the same Lipschitz bounds.

It remains to show that the limit satisfies the actual equations, not only the geometric bounds. Work on a smaller collar interval whose limiting curve remains in one chart; uniform convergence puts the retained sequence in the larger chart. The tangential equations pass to the limit as integral equalities because their right sides converge uniformly. Write

\[
 \begin{aligned}
 M_j(\sigma)={}&s_j(\sigma)\\
       &+\int_{\sigma_0}^{\sigma}r_d(d_j,y_j,\eta_j)(a)\,da.
 \end{aligned}
 \tag{G19}
\]

These functions are uniformly bounded and nondecreasing. Select a subsequence converging at all rational times. Its upper and lower monotone extensions agree at every continuity point of a monotone limit $M$. To check this, trap each value between the values at two rational points on opposite sides and let those points approach it. The disagreement points are jumps, hence at most countable by the argument in Section 2. Therefore $M_j\to M$ almost everywhere and in $L^1$, by bounded dominated convergence. The integral terms in (G19) converge uniformly, so

\[
 \begin{gathered}
 s_j\longrightarrow s=M-\int r_d,\\
 \hbox{almost everywhere and in }L^1.
 \end{gathered}
 \tag{G20}
\]

Since $s_j$ are uniformly bounded, $s_j^2\to s^2$ in $L^1$ as well. Passing to the limit in $d_j'=2s_j$ and in energy proves both equalities in (G4). Where $d>0$, uniform convergence makes $d_j>0$ on every smaller compact interval, so each $M_j$ is constant there and so is $M$. This proves the support restriction on the reaction. Finally $d_js_j\to ds$ in $L^1$, so the already obtained uniform limit of the compressed normal coordinate is exactly $ds$. Interior intervals pass to the ordinary Hamilton equation directly. Finitely many local intervals and a diagonal selection cover the original interval. The limit is therefore an admissible curve at the full stated contact scope.

The same compactness conclusion holds for varying symbols in common collar coordinates: let $r_j(d,y,\eta)=\eta^TG_j(d,y)\eta$, with $G_j$ converging in $C^1$ on the retained compact sets to a positive $G$. Uniform ellipticity bounds the tangential covectors, and the first coefficient bounds make (G5)–(G7) uniform. For a uniformly converging compressed subsequence, $r_j$, $(r_j)_d$, $(r_j)_y$ and $(r_j)_\eta$, evaluated along the curves, converge uniformly to their limiting expressions. The monotone selection in (G19) therefore again gives (G20), preserves energy, and leaves the reaction constant off the wall. On interior charts the same argument uses convergence of the Hamilton vector fields. A fixed finite atlas gives the global conclusion. When the collar charts themselves vary smoothly with the metric, the flow and inverse constructions in Sections 1 and 3 give convergent coordinate maps on smaller common charts; expressing the curves in those charts reduces to the preceding case.

If full endpoint covectors also converge, their limits are permitted endpoint lifts. In the interior, (G3) recovers $s$ continuously. At a glancing endpoint, energy gives $|s_j|\to0$. At a transverse wall endpoint, energy gives the two limits $\pm\sqrt{1-r}$, both of which are exactly the one-sided lifts in (G9). This includes reflected opposite lifts when a time interval shrinks to zero.

<a id="reflected-existence"></a>

## 5. Existence, continuation and physical time

Every compressed normalized point is a limit of interior energy points. At a boundary glancing point, move slightly inward and, if necessary, reduce the tangential covector by a factor tending to one so that $r<1$; then choose either $s=\sqrt{1-r}$ or its negative. At a transverse point the same construction needs no reduction. Perturb these interior points within the dense full-volume set from Section 3. Their global billiard trajectories have a subsequence converging on $[-1,1]$, then on $[-2,2]$, and so on. The diagonal subsequence and Section 4 give a global admissible curve through the prescribed point. All glancing orders are allowed in this limiting argument.

A given finite admissible curve can also continue, rather than merely being replaced by a different curve through its initial point. Its compressed endpoint has a limit by the Lipschitz bound. Attach the appropriate half of a global curve through that endpoint. At an interior endpoint the full covector agrees. At glancing both normal limits are zero. At a transverse endpoint the arriving normal lift is negative and the departing lift positive, by (G8); joining adds the permissible positive jump $2\sqrt{1-r}$ to $M$. The tangential derivatives agree because they are the same smooth functions of the limiting $(d,y,\eta)$. Thus the concatenation satisfies (G4) and preserves the given segment. The same argument extends backward. Compactness of the normalized phase space removes any finite-time escape obstruction.

<a id="reflected-physical-time"></a>

Return now to the wave symbol $q=\tau^2-p$, with $\tau\ne0$. For a spatial $H_p$ curve use

\[
 \sigma=-t/(2\tau).
 \tag{G21}
\]

Indeed the spacetime Hamilton equations give $dt/d\lambda=2\tau$ and $dz/d\lambda=-H_pz$ in the interior. Consequently every generalized curve has the exact physical-time tangential equations

\[
 \dot y=-G(d,y)\eta/\tau,
 \qquad \dot\eta=r_y/(2\tau).
 \tag{G22}
\]

They hold continuously at reflections and all glancing contacts by (G7), not only almost everywhere. The spatial position is uniformly Lipschitz on normalized compact energy sets. On $p=\tau^2=1$ the conversion (G21) is a fixed nonzero linear change of parameter. For other nonzero energies, simultaneous scaling $(\tau,\xi)\mapsto(c\tau,c\xi)$ preserves the physical-time equations, including reflection. Thus the results transfer homogeneously to the nonzero wave characteristic set.

Let $\mathcal R$ be the relation of pairs of full permitted endpoint lifts of such curves on bounded physical-time intervals. Then

\[
 \begin{gathered}
 \mathcal R\text{ is closed in the}\\
 \text{nonzero wave characteristic set}.
 \end{gathered}
 \tag{G23}
\]

To prove this for a convergent sequence of relation points, normalize energy and retain one sign of $\tau$. Extend the curves to a common compact interval by the proved continuation. Section 4 gives a uniformly convergent compressed curve; the endpoint-lift argument there retains each limiting full covector. If the time interval tends to zero at a transverse reflection, the two opposite lifts are still permitted. Scaling back proves (G23).

This supplies the geometric existence, compactness, continuation, tangential equations and lift conventions used in the boundary lesson's short-return proof. It also gives a precise candidate relation for its wavefront assertion. Sections 63–70 of the linked Dirichlet phase-neighborhood reading supply the analytic singular-curve construction on homogeneous intervals, including the gliding and degenerate-contact laws, nonnegative bounded-variation reaction and full endpoint lifts. Its earlier sections supply the actual incoming-edge bounds and regularity iteration. Sections 71–75 of that reading identify the singular endpoint with Cauchy data and complete the transfer to every required negative order for compact interior spectral data. The curved spectral remainder uses a separate argument in the spectral reading, Sections 31–38.
