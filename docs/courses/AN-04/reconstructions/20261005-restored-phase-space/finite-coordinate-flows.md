# Finite-coordinate flows: an AN-03 proof extract

This companion retains Sections 17.1–17.7, equations NF1–NF21, from AN03-U012, *Detecting regularity without choosing coordinates*, in *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. The section numbers and complete proofs are retained. The imported mathematical body is unchanged.

Principal author entity: AN-03 course-writing task, 2026. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. This extract with its new prerequisite front matter was prepared by the AN-04 course-writing task and OpenAI Codex, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## Exact prerequisite bindings for this extract

The given spaces, norms, open sets and differentiability classes in NF1 are retained. The proofs use the existing U001 programme providers: [finite norm completeness P1 and smooth matrix/implicit maps P2–P3](../20261004-free-stationary-phase/prerequisite-completions.md), [finite norm equivalence P9.3](../20261004-free-stationary-phase/differential-prerequisite-completions.md), finite calculus, compactness and exponential series, and FTC, Taylor remainder and all compact parameter integrals. The [exact proof map](proof-map.json) resolves each input to its retained proof. In NF18 the higher finite inverse derivatives follow by differentiating the inverse identity using P2–P3 and the product rule; every new derivative either hits an inverse factor or a derivative of the original map, exactly as in NF10–NF11.

These bindings replace the original front matter's broad reference to AN-03 Section 16; they do not change NF1–NF21. In Section 17.7 the compact subdivision assertion follows directly from compactness: if arbitrarily short subintervals failed to lie in one member of a finite open cover, choose points in them and a convergent subsequence; a covering neighborhood of the limit contains the whole sufficiently short subinterval, a contradiction. An open and closed nonempty subset of an interval is the whole interval: otherwise a least-upper-bound boundary between a point inside and one outside contradicts one of the two openness assertions. These are the two elementary interval facts used for continuation and uniqueness. No separate manifold extension theorem is imported: the boundary-chart sentence requires a smooth extension as actual given data.

### 17.1. The original integral equation and its complete local solution

Let \(E,P\) be the original real finite-dimensional normed spaces, with their given norms. Let \(W\subset\mathbb R\times E\times P\) be open and let \(F:W\to E\) be \(C^r\), \(1\leq r\leq\infty\). Fix the original point \((t_0,a,p_0)\in W\). The equation and datum are

\[
 \partial_tu(t)=F(t,u(t),p),\qquad u(t_0)=x.
 \tag{NF1}
\]

Choose positive \(d,\rho,\delta\) such that the compact rectangle
\(K=[t_0-d,t_0+d]\times\overline B_E(a,\rho)\times\overline B_P(p_0,\delta)\)
lies in \(W\). An open neighborhood contains a sufficiently small product of balls; their closures are compact in the original norms and can still be chosen inside that neighborhood. Let the actual bounds be

\[
 M=\sup_K\|F\|_E,\qquad
 L=\sup_K\|D_xF\|_{E\to E},\qquad
 Q=\sup_K\|D_pF\|_{P\to E}.
 \tag{NF2}
\]

They are finite by continuity and compactness. Choose \(0<\theta<1\) and \(0<h<d\) with \(hM\leq\rho/4\) and \(hL\leq\theta\). Such an \(h\) exists also when either bound is zero; no division by a zero bound is used. Keep the original interval \(I=[t_0-h,t_0+h]\), the state ball, and \(x\in B_E(a,\rho/4)\), \(p\in B_P(p_0,\delta)\). On continuous paths in the original closed state ball set

\[
 (\Phi_{x,p}w)(t)=x+\int_{t_0}^{t}F(s,w(s),p)\,ds .
 \tag{NF3}
\]

All integrals retain their original oriented endpoints. A finite-coordinate continuous integral exists coordinatewise by the proved Riemann integral. Its norm is at most the integral of the norm: the finite tagged sums have this bound by the triangle inequality; their vector limits and the scalar integral limit preserve it. The continuous-path space is complete in \(\|w\|_\infty=\sup_{t\in I}\|w(t)\|_E\). Indeed a uniform Cauchy sequence converges pointwise by the original completeness of \(E\), its Cauchy estimates pass uniformly to the limit, and the triangle inequality with one continuous approximant proves continuity. The paths with values in the closed ball form a closed subset of that complete space.

NF2--NF3 show that \(\Phi_{x,p}w\) stays within distance \(\rho/2\) of \(a\). The full state-segment fundamental theorem gives
\(\|F(s,v,p)-F(s,w,p)\|_E\leq L\|v-w\|_E\) inside the original convex ball. Thus
\(\|\Phi_{x,p}v-\Phi_{x,p}w\|_\infty\leq hL\|v-w\|_\infty\leq\theta\|v-w\|_\infty\).
Starting with the actual constant path \(u_0(t)=x\), define \(u_{m+1}=\Phi_{x,p}u_m\). For every \(m\geq0\) and \(k\geq1\), retain

\[
 \begin{aligned}
 \|u_{m+1}-u_m\|_\infty
   &\leq\theta^m\|u_1-u_0\|_\infty,\qquad
       \|u_1-u_0\|_\infty\leq hM,\\
 \|u_{m+k}-u_m\|_\infty
   &\leq\|u_1-u_0\|_\infty
                         \sum_{\nu=m}^{m+k-1}\theta^\nu,\\
 \|u-u_m\|_\infty
   &\leq\frac{\theta^m}{1-\theta}\|u_1-u_0\|_\infty .
 \end{aligned}
 \tag{NF4}
\]

The finite sum proves the Cauchy property, completeness supplies \(u\), and continuity of \(\Phi\) gives NF3 with \(w=u\). The last line follows by taking the limit in the full finite-tail estimate. The fundamental theorem then proves NF1, including at \(t_0\). Two fixed points have distance at most \(\theta\) times that distance and therefore coincide.

For another \(C^1\) solution with the same datum, restrict to an interval on which both solutions lie in a common compact rectangle. On a sufficiently short subinterval beginning at any time at which they agree, the same contraction estimate forces agreement. Their equality set is closed by continuity and open by this two-sided local argument. On their connected common time interval containing the datum it is therefore the whole interval. This proves local uniqueness even for a solution not initially confined to the particular closed ball used to construct \(u\).

The original parameter differences satisfy

\[
 \|u(\,\cdot\,;x',p')-u(\,\cdot\,;x,p)\|_\infty
 \leq\frac{\|x'-x\|_E+hQ\|p'-p\|_P}{1-\theta}.
 \tag{NF5}
\]

To prove it, subtract the two full equations NF3, use the state and parameter segment formulas with their original derivative bounds, and bring the \(hL\) term to the left. Convexity of the original parameter ball keeps every intermediate point in \(K\). Continuity in time and this uniform estimate give joint continuity in \((t,x,p)\). The retained buffer \(\rho/2\) to the boundary of the larger state ball permits the full parameter Taylor comparisons below.

### 17.2. Ordered linear transport on the original two-sided interval

Let \(A:I\to\mathcal L(E,E)\) be continuous and \(B:I\to E\) be continuous. For the same original \(t_0\), define

\[
 (\mathcal V_Az)(t)=\int_{t_0}^t A(s)z(s)\,ds,\qquad
 z=B+\mathcal V_Az.
 \tag{NF6}
\]

For \(L_A=\sup_I\|A(s)\|\), nested integration proves
\(\|\mathcal V_A^m\|\leq(hL_A)^m/m!\). In detail the \(m\)-fold application has the full integral
\(\int_{t_0}^t ds_1\int_{t_0}^{s_1}ds_2\cdots\int_{t_0}^{s_{m-1}}ds_m\)
of \(A(s_1)\cdots A(s_m)z(s_m)\). Taking absolute values reverses the bounds when \(t<t_0\); the resulting scalar nested integral of one is \(|t-t_0|^m/m!\), by induction from the scalar power integral. Every oriented sign remains in the original operator integral. Norm completeness therefore supplies

\[
 \begin{aligned}
 \mathcal R_A&=\sum_{m=0}^{\infty}\mathcal V_A^m,&
 (I-\mathcal V_A)\mathcal R_A
   &=I=\mathcal R_A(I-\mathcal V_A),\\
 z&=\mathcal R_AB,&
 \|\mathcal R_A\|&\leq
        \sum_{m=0}^{\infty}\frac{(hL_A)^m}{m!}
        =\exp(hL_A).
 \end{aligned}
 \tag{NF7}
\]

The inverse products follow from both finite identities
\((I-\mathcal V_A)\sum_{m=0}^N\mathcal V_A^m
=I-\mathcal V_A^{N+1}
=(\sum_{m=0}^N\mathcal V_A^m)(I-\mathcal V_A)\)
and the factorial bound. This proves uniqueness as well as existence. When \(hL_A\leq\theta\), the additional geometric bounds
\(\|\mathcal R_A\|\leq(1-\theta)^{-1}\) and
\(\|\sum_{m>N}\mathcal V_A^m\|\leq\theta^{N+1}/(1-\theta)\)
hold with their complete factors. Neither estimate replaces the original operator or the factorial estimate.

For a matrix coefficient acting on a finite-dimensional original fiber, the fundamental matrix is

\[
 Y(t)=I_E+\sum_{m=1}^{\infty}
   \int_{t_0}^{t}ds_1\int_{t_0}^{s_1}ds_2
       \cdots\int_{t_0}^{s_{m-1}}ds_m\,
        A(s_1)A(s_2)\cdots A(s_m).
 \tag{NF8}
\]

The order is exactly the displayed one. Its factorial bound proves uniform convergence. Its integral equation and the fundamental theorem give \(Y'=AY\), \(Y(t_0)=I_E\). Construct \(Z'=-ZA\), \(Z(t_0)=I_E\), by the same integral argument, now on the original matrix space with right multiplication. Differentiating \(ZY\) gives zero with the two full terms \(-ZAY+ZAY\), so \(ZY=I_E\). Finite-dimensional injectivity and surjectivity imply \(YZ=I_E\) as well. Thus this constructed \(Z\) is the actual inverse at every original time.

For \(z'=Az+b\), \(z(t_0)=c\), both full maps are

\[
 z(t)=Y(t)\left(c+\int_{t_0}^{t}Y(s)^{-1}b(s)\,ds\right),
 \qquad
 Y(t)^{-1}z(t)=c+\int_{t_0}^{t}Y(s)^{-1}b(s)\,ds .
 \tag{NF9}
\]

The product rule and the proved inverse equation verify both identities, including their initial values and multiplication order. Uniqueness follows from NF7. Arbitrary complex matrices are handled on their original real and imaginary coordinates, with the same complex matrix products; no diagonalization, self-adjointness or commutation is used.

### 17.3. All parameter derivatives of the linear inverse

Let \(\eta\) range in an open finite-dimensional original normed parameter space. Suppose \(\eta\mapsto A_\eta\) is \(C^s\) into continuous matrix or operator paths in the original supremum norm. Integration in NF6 is a bounded linear map of \(A\), with norm at most \(h\), so \(\eta\mapsto\mathcal V_\eta\) is \(C^s\) and every derivative retains that integral. Locally bounded \(L_A\) gives locally bounded inverses by NF7. Their exact difference identity is

\[
 \mathcal R_{\eta'}-\mathcal R_\eta
   =\mathcal R_{\eta'}(\mathcal V_{\eta'}-\mathcal V_\eta)
                         \mathcal R_\eta.
 \tag{NF10}
\]

Multiplication on the left by \(I-\mathcal V_{\eta'}\) and on the right by \(I-\mathcal V_\eta\) verifies the identity directly. It proves norm continuity. Insert the full differentiability remainder of \(\mathcal V\) into NF10; continuity and the local inverse bound make its remaining error \(o(\|\eta'-\eta\|)\). Consequently
\(D\mathcal R[v]=\mathcal R(D\mathcal V[v])\mathcal R\).
This proof uses no Banach inverse-function theorem. Bounded operator multiplication has the required product rule: expand the actual two-factor increment, retaining the bilinear increment product whose norm is bounded by the product of its two increment norms. The remainder is therefore of second order. Induction gives its full higher product rule.

For every integer \(N\geq1\) allowed by the parameter differentiability, the entire inverse derivative is

\[
 D^N\mathcal R[v_1,\ldots,v_N]
 =\sum_{k=1}^N
   \sum_{\substack{(I_1,\ldots,I_k)\ {\rm ordered}\\
                   I_j\ne\varnothing,\ 
                   I_1\sqcup\cdots\sqcup I_k=\{1,\ldots,N\}}}
 \mathcal R D_{I_1}\mathcal V\,\mathcal R\cdots
                       D_{I_k}\mathcal V\,\mathcal R .
 \tag{NF11}
\]

Here \(D_I\) retains precisely the labeled directions in \(I\). A new differentiation either joins an existing derivative block or differentiates one inverse factor and inserts its new singleton block there. Every ordered partition of the enlarged label set has exactly one predecessor, determined by the new label's block. This proves NF11 and \(C^s\) regularity by induction, with all repeated-direction multiplicities and every noncommuting factor retained. For \(N=0\) the value is the full inverse \(\mathcal R\).

If \(B_\eta\) is \(C^s\) in the continuous-path norm, NF7 and the full product rule therefore make \(z_\eta=\mathcal R_\eta B_\eta\) \(C^s\) in that same norm. For coefficient paths of the form \(A_\eta(t)=A(t,\eta)\), whose finite-coordinate derivatives are jointly continuous, their path-valued derivatives exist uniformly on compact parameter neighborhoods. The segment Taylor remainder is bounded by the uniform oscillation of the next continuous derivative on the compact time/parameter product, which tends to zero. This proves the asserted path-valued regularity, rather than merely pointwise differentiability.

### 17.4. The first actual nonlinear parameter derivative

Write \(\eta=(x,p)\), retaining its given product-space norm and both coordinate projections. For a direction \(v=(v_x,v_p)\), the candidate derivative \(z_v\) solves

\[
 \begin{aligned}
 A_\eta(t)&=D_xF(t,u_\eta(t),p),\\
 B_{\eta,v}(t)&=v_x+
           \int_{t_0}^tD_pF(s,u_\eta(s),p)v_p\,ds,\\
 z_v&=B_{\eta,v}+\mathcal V_{A_\eta}z_v
       =\mathcal R_{A_\eta}B_{\eta,v}.
 \end{aligned}
 \tag{NF12}
\]

NF7 supplies this entire linear solution and uniqueness. It is linear in the original direction, and continuous as an operator from the original parameter norm to the path norm: keep the original projection norms \(c_x,c_p\), so
\(\|z_v\|_\infty\leq(1-\theta)^{-1}(c_x+hQc_p)\|v\|\).
No original norm is replaced by a coordinate norm in this estimate.

To prove that it is the derivative, let \(\Delta\eta=(\Delta x,\Delta p)\) and \(\Delta u=u_{\eta+\Delta\eta}-u_\eta\). The exact segment expansion of the original field is

\[
 \begin{aligned}
 &F(t,u_\eta+\Delta u,p+\Delta p)-F(t,u_\eta,p)\\
 &\quad=A_\eta(t)\Delta u+
               D_pF(t,u_\eta,p)\Delta p+\epsilon_\eta(t),\\
 &\|\epsilon_\eta\|_\infty
   \leq\omega_\eta\bigl(\|\Delta u\|_\infty+\|\Delta p\|_P\bigr)
             \bigl(\|\Delta u\|_\infty+\|\Delta p\|_P\bigr),
       \qquad \omega_\eta(q)\longrightarrow0\quad(q\downarrow0).
 \end{aligned}
 \tag{NF13}
\]

For the bound, subtract the derivatives at the start of each full state/parameter segment from their values along it and integrate. Uniform continuity on a compact rectangle containing these segments gives the displayed modulus. NF5, with both original projection factors, bounds the argument of the modulus by
\(((c_x+hQc_p)/(1-\theta)+c_p)\|\Delta\eta\|\).
Subtract NF12 for \(v=\Delta\eta\) from the exact difference of NF3. Its residual is
\(\Delta u-z_{\Delta\eta}=\mathcal V_{A_\eta}(\Delta u-z_{\Delta\eta})
+\int_{t_0}^{\,\cdot\,}\epsilon_\eta(s)\,ds\).
NF7 bounds it by \(h(1-\theta)^{-1}\|\epsilon_\eta\|_\infty=o(\|\Delta\eta\|)\). This proves the full path-valued Fréchet derivative. Joint continuity of the field derivatives, NF5 and NF10 give continuity of the derivative operator. Thus \(u_\eta\) is \(C^1\) into continuous paths before any higher dependence is used.

### 17.5. Every nonlinear parameter derivative, including its original blocks

Assume \(u_\eta\) is \(C^s\) in the path norm, with \(s<r\). The path-valued maps \(A_\eta=D_xF(\,\cdot\,,u_\eta,p)\) and \(B_{\eta,v}\) in NF12 are \(C^s\), because \(F\) is \(C^r\) and \(s\leq r-1\). To justify the composition statement in the path norm, apply the full finite-coordinate chain and product rules at each time. The derivatives are finite sums of continuous products of the original derivatives of \(F\) and those of \(u\). All their Taylor remainder bounds are uniform on the compact rectangle, by the same segment and uniform-continuity argument as NF13. The bound remains uniform for \(v\) in the unit ball of its original finite-dimensional direction space. NF10--NF11 then show that \(Du_\eta=\mathcal R_{A_\eta}B_{\eta,\cdot}\) is \(C^s\) as an operator-valued map. Hence \(u_\eta\) is \(C^{s+1}\). Induction proves the full \(C^r\) parameter theorem, and every order for \(r=\infty\).

Here is its exact higher equation. Retain labeled directions \(v_1,\ldots,v_N\) in the original parameter space, and put \(\zeta_\eta(t)=(u_\eta(t),p)\). For a nonempty block \(B\) of labels use

\[
 D_B\zeta_\eta(t)=
 \begin{cases}
 (D u_\eta(t)[v_b],(v_b)_p),&B=\{b\},\\
 (D^{|B|}u_\eta(t)[v_b:b\in B],0),&|B|\geq2.
 \end{cases}
 \tag{NF14}
\]

For \(2\leq N\leq r\), the whole \(N\)-th derivative equation is

\[
 \begin{aligned}
 D^Nu_\eta(t)[v_1,\ldots,v_N]
 &=\int_{t_0}^t A_\eta(s)
                  D^Nu_\eta(s)[v_1,\ldots,v_N]\,ds\\
 &\quad+\int_{t_0}^t
   \sum_{\substack{\Pi\in\mathfrak P(\{1,\ldots,N\})\\|\Pi|\geq2}}
   D_{(x,p)}^{|\Pi|}F(s,u_\eta(s),p)
                 [D_B\zeta_\eta(s):B\in\Pi]\,ds .
 \end{aligned}
 \tag{NF15}
\]

The initial \(N\)-th derivative is zero because the original datum \(x\) is linear in \(\eta\). The one-block term of the full chain rule is \(D_xF\,D^Nu\), since the parameter component of NF14 is zero for that block. Every other partition remains explicitly in NF15. Differentiating a block appends the new direction to that block; differentiating the outer derivative creates its singleton block. Every partition is obtained once, proving the full chain formula with no omitted multiplicity. The outer derivatives are symmetric multilinear maps on the original state/parameter product; the order of their arguments may be fixed by the least label in each block. Their values do not authorize commuting any linear transport factors. NF7 applied to the entire displayed inhomogeneous integral gives the actual unique derivative, including all pure-state, pure-parameter and mixed derivatives.

All derivatives just constructed are jointly continuous in time and parameters. NF1 gives the time derivative. More explicitly, the first time derivative of each parameter derivative of total order at most \(r-1\) is its full chain-rule derivative of \(F(t,u_\eta(t),p)\). Its right side is a finite continuous sum of the just proved parameter derivatives and the original field derivatives. Differentiating these identities in time gives all further mixed time/parameter derivatives of total order at most \(r\), inductively using the complete product and chain rules. At a given total order only field derivatives and solution derivatives of lower total order occur on the right of the time equation. Their continuity proves the next derivatives and permits equality of the mixed derivatives by the proved finite-coordinate calculus. The case of no time derivative and \(r\) parameter derivatives was already constructed in the path norm. Thus \(u(t;x,p)\) is jointly \(C^r\), not only separately differentiable.

### 17.6. Variable initial times without replacing the original time coordinate

Use the proved solution with the fixed original \(t_0\). Write \(U(t;t_0,y,p)\) for it. Near \((t_0,a,p_0)\), the actual finite map

\[
 \mathcal L(\tau,y,p)
   =(\tau,U(\tau;t_0,y,p),p)
 \tag{NF16}
\]

is \(C^r\). At \(\tau=t_0\) its state derivative is the original identity because \(U(t_0;t_0,y,p)=y\), its state derivative in \(p\) is zero, and its time derivative is \(F(t_0,y,p)\). Its full derivative is block triangular with diagonal identities; its inverse keeps the lower state/time block \(-F(t_0,y,p)\). The proved finite inverse/implicit theorem therefore constructs its actual local inverse, with second component \(Y(\tau,x,p)\). The unchanged original-time solution is

\[
 U(t;\tau,x,p)=U(t;t_0,Y(\tau,x,p),p),\qquad
 U(\tau;t_0,Y(\tau,x,p),p)=x .
 \tag{NF17}
\]

It is jointly \(C^r\), solves the original differential equation in the original \(t\), and has the original datum at the original time \(\tau\). Uniqueness was proved in Section17.1. Both maps in NF17 are explicit; no translated time equation or changed vector field is substituted for NF1.

Let \(M(t)=D_yU(t;t_0,y,p)\). Differentiating the already proved equation gives \(M'=D_xF(t,U,p)M\), \(M(t_0)=I_E\). NF8 proves that it is invertible with the constructed opposite-order inverse. Differentiate the second identity of NF17 and then its first identity to obtain the full initial-time derivative

\[
 \begin{aligned}
 D_\tau Y&=
  -D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p),\\
 D_\tau U(t;\tau,x,p)&=
  -D_yU(t;t_0,Y,p)
   D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p)\\
  &=-D_xU(t;\tau,x,p)F(\tau,x,p).
 \end{aligned}
 \tag{NF18}
\]

The last equality follows by differentiating NF17 in \(x\): \(D_xY=D_yU(\tau;t_0,Y,p)^{-1}\). All original inverse factors and endpoint evaluations appear before the comparison. Higher initial-time derivatives are the full finite composition and inverse partition formulas applied to NF16--NF17; they keep the entire time/state/parameter blocks.

### 17.7. Continuation, the exact composition law and coordinate transport

At every point of a solution, the local construction above applies with that original point and its original time as datum. Its local continuations agree by uniqueness. The union of all continuation intervals is an interval: each contains the original datum time, so two such intervals overlap; their agreeing solutions glue. This gives the unique maximal solution on that interval. If two overlapping continuations are first described through different chains of local rectangles, the same uniqueness argument on the connected time overlap makes them equal. No choice of a chart or of a time subdivision changes the solution.

The full admissible domain of \((t,\tau,x,p)\) is open and the solution is jointly \(C^r\) there. For an actual trajectory segment from \(\tau\) to \(t\), its compact graph is covered by finitely many construction rectangles with smaller time intervals. Subdivide that original time segment finely enough that each successive piece lies in one such rectangle: a Lebesgue number follows from compactness by taking finitely many smaller neighborhoods whose closures remain in the covering neighborhoods, or by the elementary compact interval subdivision argument. Each local solution map is defined on an open neighborhood of its intermediate datum. Continuity of the finite preceding composition lets one shrink the original data neighborhood so that all intermediate data stay in these open neighborhoods. The finite composition then exists near the given endpoint and is \(C^r\), and uniqueness identifies it with the maximal solution. Slightly moving both endpoint times uses the first and last rectangles. This proves openness and full local regularity throughout the actual domain.

Whenever all displayed solutions are defined along their connected common intervals,

\[
 U(t;s,U(s;\tau,x,p),p)=U(t;\tau,x,p),\qquad
 U(\tau;t,U(t;\tau,x,p),p)=x.
 \tag{NF19}
\]

Both sides of the first identity solve NF1 with the same datum at \(s\); uniqueness proves it, and the second is its endpoint case. For an autonomous field write \(\varphi_t(x,p)=U(t;0,x,p)\). NF19 gives the local flow law \(\varphi_t(\varphi_s(x,p),p)=\varphi_{t+s}(x,p)\), with their actual domains, and inverse \(\varphi_{-t}\). This is a local diffeomorphism, since both maps are the constructed smooth inverse maps on open sets. It is not an assertion that every field has a globally defined flow.

Under an original smooth coordinate diffeomorphism \(\kappa\), retain the transformed field
\(\widetilde F(t,\kappa(x),p)=D\kappa(x)F(t,x,p)\).
The chain rule proves that \(\kappa(U(t;\tau,x,p))\) solves its equation with datum \(\kappa(x)\). Applying uniqueness gives

\[
 \widetilde U(t;\tau,\kappa(x),p)
       =\kappa(U(t;\tau,x,p)).
 \tag{NF20}
\]

This is the exact map between coordinate presentations. For a smooth vector field on the given manifold, these transformations glue local chart solutions and all their parameter derivatives. Their domains are open by the finite-chain proof. For a manifold with boundary, the same assertion in boundary charts needs an actual smooth extension of the coefficients to an open coordinate neighborhood; no extension theorem is hidden in NF20. The collar lesson's stated coefficient extension or an explicitly given extension supplies that separate condition.

The determinant of the original state variation has all of its factors:

\[
 \det D_xU(t;\tau,x,p)
   =\exp\left(\int_\tau^t
             \operatorname{tr}D_xF(s,U(s;\tau,x,p),p)\,ds\right).
 \tag{NF21}
\]

Its derivative follows from the full cofactor determinant derivative and the two actual inverse products of NF8: for \(M'=AM\),
\((\det M)'=(\det M)\operatorname{tr}(M^{-1}AM)
=(\det M)\operatorname{tr}A\).
The trace equality is the finite sum
\(\sum_{i,j,k}(M^{-1})_{ij}A_{jk}M_{ki}
=\sum_{j,k}A_{jk}\sum_i M_{ki}(M^{-1})_{ij}
=\sum_jA_{jj}\).
The scalar integrating-factor proof and the initial determinant one give NF21. The original determinant, oriented time integral and original trace are all retained. Positivity of this determinant is the local orientation statement; no state norm or coordinate volume has been silently changed.

If the original state dimension is zero, the unique state is its zero vector, \(F\) is zero and the solution is constant. Every state inverse is the unique \(I_0\), every empty matrix determinant is one, and NF21 is \(1=\exp(0)\). No positive state comparison constant or division by a zero operator norm is needed. A zero-dimensional parameter space has no parameter directions; its derivative terms in the original formulas are zero. If \(W\) is empty there is no datum and no local assertion.
