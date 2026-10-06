# SH02-AE-UNIT — Covectors at a boundary and at infinity

The geometric assertions and the direct-image arguments below are proved relative to the exact prerequisites recorded in `SH02-AE-IMPORTS`. The coefficient ring $k$ is commutative and has finite global dimension. Manifolds are finite dimensional, countable at infinity, and smooth; maps and submanifolds are smooth. Analytic manifolds and maps are included by forgetting their analytic structure. The word smooth describes differentiability here; a submersion is explicitly called a submersion. All sheaf complexes in the direct-image theorems belong to the indicated bounded derived category. Neither constructibility, finite-rank stalks, nor a field of coefficients is assumed.

An ordinary sum of covectors only compares covectors based at exactly the same point. Near a singular boundary this loses information: two large covectors at nearby points may nearly cancel. The scale of their separation matters. We first construct the operation that retains this information, then use it to control extension across arbitrary open boundaries and integration along noncompact fibers.

## SH02-AE-IMPORTS — Exact antecedents and conventions

The notation $A^a$ changes the sign of each cotangent vector, without moving its base point. A set in a cotangent bundle is conic if it is invariant under every positive scaling of covectors. Conic sets in the geometric constructions need not initially be closed. The conclusions that explicitly assume closedness retain that assumption.

For $f:Y\to X$, write

\[
 E_f=Y\times_XT^*X,\qquad
 f_\pi(y,\xi)=(f(y),\xi),\qquad
 f_d(y,\xi)=(y,(df_y)^t\xi).
 \tag{AE.1}
\]

Here are the precise sheaf-theoretic inputs used later.

1. **Normal geometry.** The deformation to a smooth submanifold and its normal-cone sequence criterion are those of [Normal geometry](normal-geometry.md). In coordinates $(u,z)$ with the submanifold $u=0$, a point $(v,z_0)$ lies in the normal cone of a set $S$ if and only if there are $(u_n,z_n)\in S$ and $r_n\to+\infty$ with $z_n\to z_0$ and $r_nu_n\to v$.
2. **Microsupport tests and propagation.** The test equivalence and directional propagation in [Detecting directional obstructions](microsupport-tests.md) are used with uniform neighborhoods. In particular, if a family $K_i$ has microsupport disjoint from one fixed product neighborhood $V\times W$ of a nonzero covector, the same small cone and the same compact cap tests can be chosen for every $K_i$. One may also choose the same pair of cone-open sets $O_0\subset O_1$ whose difference contains the testing point in its interior and is contained in $V$, with $Rq_{C*}R\Gamma_{O_1\setminus O_0}K_i=0$. This is the local propagation assertion, not a claim that arbitrary pointwise vanishing is uniform in $i$.
3. **Noncharacteristic boundary estimates.** If $H\in D^b(k_X)$ and $j:O\hookrightarrow X$ is open, then
   \[
   \begin{split}
   \operatorname{SS}(H)\cap N^*(O)^a\subset T_X^*X
   &\Longrightarrow
   \operatorname{SS}(Rj_*j^{-1}H)\subset\operatorname{SS}(H)+N^*(O),\\
   \operatorname{SS}(H)\cap N^*(O)\subset T_X^*X
   &\Longrightarrow
   \operatorname{SS}(j_!j^{-1}H)\subset\operatorname{SS}(H)+N^*(O)^a.
   \end{split}
   \tag{AE.2}
   \]
   These are the ordinary, noncharacteristic estimates in [SH02-MO-BOUNDARY](microsupport-operations.md#SH02-MO-BOUNDARY). The $+$ here is an ordinary fiberwise sum.
4. **Proper images and submersions.** Proper direct image on the closed support has the cotangent estimate $\operatorname{SS}(Rf_*H)\subset f_\pi f_d^{-1}\operatorname{SS}(H)$, with $Rf_!=Rf_*$. For a submersion $g$, $\operatorname{SS}(g^{-1}H)=g_dg_\pi^{-1}\operatorname{SS}(H)$ with no global surjectivity requirement. For a closed embedding $i$, $\operatorname{SS}(i_*H)=i_d^{-1}\operatorname{SS}(H)$, viewed in the restricted ambient cotangent bundle. The cotangent estimates are [SH02-MO-PROPER-PUSH](microsupport-operations.md#SH02-MO-PROPER-PUSH) and [SH02-MO-SUBMERSION](microsupport-operations.md#SH02-MO-SUBMERSION). These estimates, the localization triangles, and compatibility of the canonical map $Rf_!\to Rf_*$ with composition are separately typed six-operations imports.
5. **Compact-support resolutions.** Bounded-below complexes on the locally compact spaces used here admit $c$-soft resolutions; $c$-soft sheaves and their restrictions to open subsets are acyclic for compactly supported sections. Open-extension base change identifies the restriction of $j_!H$ to a locally closed subset with extension by zero from the corresponding intersection. The two limit comparisons actually used below are proved in `SH02-AE-LIMITS`. No arbitrary closed-exhaustion continuity is assumed.
6. **Elementary smooth topology.** Tubular charts, smooth partitions of unity, and a proper smooth embedding of a manifold countable at infinity into a finite-dimensional Euclidean space are topological antecedents. The blowup needed below is also described directly in local coordinates.

For completeness, the normal notation in (AE.2) is geometric. For a locally closed subset $S$ of a manifold, set

\[
 N_x(S)=T_xX\setminus C_x(X\setminus S,S),\qquad
 N_x^*(S)=N_x(S)^\circ.
 \tag{AE.3}
\]

The polar uses the inequality $\langle v,\xi\rangle\geq0$. A nonzero $v$ lies in $N_x(S)$ exactly when a small open cone about $v$ carries nearby points of $S$ into $S$ as long as they remain in the chart. Thus $N(S)$ is the open cone of strictly inward directions. Its polar is closed. At a smooth boundary $O=\{h>0\}$, $N_x^*(O)=\mathbb R_{\geq0}dh_x$. We use the following local consequence of this characterization: if $\xi_0\notin N_{x_0}^*(O)$, there is a pointed closed cone $C$ with nonempty interior, locally $O+C\subset O$, and $v\in\operatorname{Int}C$ with $\langle v,\xi_0\rangle<0$. After shrinking the chart, $N^*(O)\subset C^\circ$. Choose first a strict inward vector separating $\xi_0$, then a small closed cone around it; compactness of its unit section makes the inward condition uniform. Replacing $\xi_0$ by $-\xi_0$ reverses the last inequality.

## SH02-AE-NORMAL — A normal cone in a cotangent bundle

Let $M\subset X$ be a smooth submanifold. Write $\Lambda=T_M^*X$. There are canonical identifications

\[
 T^*(T_MX)\simeq T^*\Lambda\simeq T_\Lambda(T^*X).
 \tag{AE.4}
\]

We fix their signs explicitly. In local coordinates $(u,z)$ with $M=\{u=0\}$, write a point of $T^*(T_MX)$ as $(v,z;\alpha,\zeta)$. The first map in (AE.4) sends it to

\[
 (\alpha,z;-v,\zeta)\in T^*\Lambda.
 \tag{AE.5}
\]

The second map identifies this with the normal vector represented by $(v,z;\alpha,\zeta)$: its base point in $\Lambda$ is $(0,z;\alpha,0)$, and its normal components are $(v,\zeta)$. This is the convention obtained from the symplectic map

\[
 -H(\lambda\,dx+\mu\,d\xi)
 =\lambda\,\partial_\xi-\mu\,\partial_x.
 \tag{AE.6}
\]

The canonical one-form is $\sum_j\xi_j\,dx_j$; the inverse of contraction with its exterior derivative gives the map in (AE.6). This fixes the Hamiltonian convention without a coordinate-dependent choice of sign. It is the same Fourier cotangent sign as in the Fourier–Sato microsupport calculation. In particular the tangential covector $\zeta$ is not negated.

More generally, for a smooth conic Lagrangian $L\subset T^*X$, the map $-H$ induces $T^*L\simeq T_L(T^*X)$. Indeed, restriction identifies $T^*L$ with $T^*(T^*X)|_L/\operatorname{Ann}(TL)$. The Lagrangian condition says that the symplectic image of $\operatorname{Ann}(TL)$ is $TL$. Passing to these two quotients gives the claimed isomorphism. Applying this argument to $L=T_M^*X$, followed by the cotangent Fourier exchange in the normal variables, gives (AE.4)–(AE.5).

Let $p:\Lambda\to M$ be the vector-bundle projection. Pullback by $dp$ identifies $\Lambda\times_MT^*M$ with the locus $v=0$ in (AE.4), and $p_\pi$ forgets $\alpha$. Its restriction to $\dot\Lambda=\Lambda\setminus M$ will be denoted $\dot p$. The dot removes the zero covectors of the **base bundle $\Lambda$**. It does not remove zero vectors of $T_\Lambda(T^*X)$.

For a conic set $A\subset T^*X$, put $D=C_\Lambda(A)$. The two conic actions on $D$ give

\[
 p_\pi p_d^{-1}D=T^*M\cap D,
 \tag{AE.7}
\]

where $T^*M$ is embedded as $(v,z;\alpha,\zeta)=(0,z;0,\zeta)$.

**Proof.** One inclusion is immediate by choosing $\alpha=0$. For the other, take $(0,z;\alpha,\zeta)\in D$. Scaling original cotangent covectors by $a>0$ sends $(v,z;\alpha,\zeta)$ to $(v,z;a\alpha,a\zeta)$. Scaling normal vectors by $a^{-1}$ then sends it to $(a^{-1}v,z;a\alpha,\zeta)$. Both actions preserve $D$. When $v=0$, letting $a\downarrow0$ and using the closedness of a normal cone gives $(0,z;0,\zeta)\in D$. This proves (AE.7). It uses conicity and closedness of the resulting normal cone; it does not apply nonproper base change or assert that an arbitrary projection has closed image. $\square$

The restriction identity

\[
 \dot p_d^{-1}D
 =p_d^{-1}D\cap(\dot\Lambda\times_MT^*M)
 \tag{AE.8}
\]

follows because the differential of a restriction to an open subset is the restricted differential. Normal-cone formation along $\dot\Lambda$ likewise gives $C_{\dot\Lambda}(A)=C_\Lambda(A)|_{\dot\Lambda}$: the deformation charts are identical over this open part of the base. Thus either notation for the punctured inverse image has the same meaning. This records unambiguously the punctured operation used next.

## SH02-AE-NORMAL-SEQUENCES — The product that must vanish

In the coordinates above, for any conic $A$,

\[
 (z_0;\zeta_0)\in T^*M\cap C_\Lambda(A)
 \tag{AE.9}
\]

if and only if there are $(u_n,z_n;\alpha_n,\zeta_n)\in A$ with

\[
 u_n\to0,\qquad z_n\to z_0,\qquad
 \zeta_n\to\zeta_0,\qquad |u_n|\,|\alpha_n|\to0.
 \tag{AE.10}
\]

Moreover,

\[
 (z_0;\zeta_0)\in\dot p_\pi\dot p_d^{-1}C_\Lambda(A)
 \tag{AE.11}
\]

if and only if the sequence in (AE.10) can be chosen with $|\alpha_n|\to\infty$.

**Proof.** First suppose (AE.10) holds. If $\alpha_n$ has a bounded subsequence, choose numbers $r_n\to\infty$ sufficiently slowly that $r_n|u_n|\to0$. The covectors $(u_n,z_n;\alpha_n/r_n,\zeta_n/r_n)$ remain in $A$ by conicity. They approach the zero covector over $(0,z_0)$, while multiplication of their normal components by $r_n$ gives $(r_nu_n,\zeta_n)\to(0,\zeta_0)$. Thus (AE.9) holds.

If no bounded subsequence is used, pass to one with $|\alpha_n|\to\infty$ and $\alpha_n/|\alpha_n|\to\alpha_0$, $|\alpha_0|=1$. Take $r_n=|\alpha_n|$. The same construction now approaches $(0,z_0;\alpha_0,0)\in\dot\Lambda$, and $r_nu_n\to0$ follows from the product condition. This proves (AE.11), and (AE.7) gives (AE.9).

Conversely a point of $p_d^{-1}D$ has a normal-cone representation

\[
 (u_n,z_n;a_n,b_n)\in A,\quad
 (z_n,a_n)\to(z_0,a_0),\quad
 r_n\to\infty,\quad
 r_nu_n\to0,\quad r_nb_n\to\zeta_0.
\]

Scale its covectors by $r_n$ and set $\alpha_n=r_na_n$, $\zeta_n=r_nb_n$. The required product is $|r_nu_n|\,|a_n|$, which tends to zero because $a_n$ is bounded. If the base lies in $\dot\Lambda$, then $a_0\ne0$, and $|\alpha_n|=r_n|a_n|\to\infty$. This proves both converses. $\square$

When the normal rank is zero, the normal covectors are zero and the escaping set is empty. The product in (AE.10) permits normal covectors to grow, but only more slowly than the reciprocal of the distance to $M$. Merely requiring $u_n\to0$ and $\zeta_n\to\zeta_0$ gives a different, usually larger, set.

## SH02-AE-GRAPH — A construction for a map and two conic sets

Identify $Y$ with the graph $\Gamma_f\subset X\times Y$. For conic sets $A\subset T^*X$ and $B\subset T^*Y$ define

\[
 C_\mu(A,B)=C_{T^*_{\Gamma_f}(X\times Y)}(A\times B^a).
 \tag{AE.12}
\]

Under the identification $T^*_{\Gamma_f}(X\times Y)\simeq E_f$, its projection to the graph is $q:E_f\to Y$. Use (AE.4) for the graph and set

\[
 \begin{split}
 f^\sharp(A,B)
 &=q_\pi q_d^{-1}C_\mu(A,B)
 =T^*Y\cap C_\mu(A,B),\\
 f^\sharp_\infty(A,B)
 &=\dot q_\pi\dot q_d^{-1}C_\mu(A,B),\\
 f^\sharp(A)&=f^\sharp(A,T_Y^*Y),\qquad
 f^\sharp_\infty(A)=f^\sharp_\infty(A,T_Y^*Y).
 \end{split}
 \tag{AE.13}
\]

The dot again punctures the conormal base. These are geometric operations on subsets, not derived functors on sheaves. The equality in the first line is (AE.7). The antipode on $B$ in (AE.12) makes the graph residual a difference, as the following calculation verifies.

## SH02-AE-SEQUENCES — Calculating the graph construction

In local coordinates, $(y_0;\eta_0)\in f^\sharp(A,B)$ if and only if there are $(x_n;\xi_n)\in A$ and $(y_n;\eta_n)\in B$ such that

\[
 \begin{gathered}
 y_n\to y_0,\qquad x_n\to f(y_0),\\
 (df_{y_n})^t\xi_n-\eta_n\to\eta_0,\qquad
 |x_n-f(y_n)|\,|\xi_n|\to0.
 \end{gathered}
 \tag{AE.14}
\]

Membership in $f^\sharp_\infty(A,B)$ is equivalent to (AE.14) together with $|\xi_n|\to\infty$.

**Proof.** Flatten the graph by $(x,y)\mapsto(u,y)=(x-f(y),y)$. The cotangent coordinates transform as

\[
 (x,y;\xi,\theta)\longmapsto
 (x-f(y),y;\xi,\theta+(df_y)^t\xi).
 \tag{AE.15}
\]

On $A\times B^a$, $\theta=-\eta$. The graph-normal component is therefore $\xi$, and the tangential component is $(df_y)^t\xi-\eta$. Apply (AE.10) and (AE.11) to these coordinates. This proves the criterion, including its growth condition and sign. $\square$

Both sets in (AE.13) are closed and conic, even when the input conic sets are not closed. For the full operation this also follows from its realization as a closed normal cone intersected with $T^*Y$. For the escaping operation use (AE.14): given a sequence of output points converging to an output point, choose from the witnessing sequence for its $n$th term an input pair with all errors smaller than $1/n$ and $|\xi|>n$. This diagonal sequence witnesses the limit. Positive scaling of both input covectors proves conicity. This argument proves closedness of this particular punctured projection; puncturing a general domain does not preserve closedness of its image.

For a closed embedding $i:M\hookrightarrow X$, flattening $M$ gives the useful formulas

\[
 i^\sharp A=T^*M\cap C_{T_M^*X}(A),\qquad
 i^\sharp_\infty A=\dot p_\pi\dot p_d^{-1}C_{T_M^*X}(A).
 \tag{AE.16}
\]

These are invariant statements; (AE.10) computes them in a submanifold chart.

## SH02-AE-SUM — Addition with asymptotic cancellation

Take $Y=X$ and $f=\mathrm{id}$. Define

\[
 A\widehat+ B=(\mathrm{id})^\sharp(A,B^a),\qquad
 A\widehat+_\infty B=(\mathrm{id})^\sharp_\infty(A,B^a).
 \tag{AE.17}
\]

Thus $(x_0;\xi_0)\in A\widehat+ B$ exactly when there are $(x_n;\alpha_n)\in A$ and $(y_n;\beta_n)\in B$ with

\[
 x_n,y_n\to x_0,\qquad
 \alpha_n+\beta_n\to\xi_0,\qquad
 |x_n-y_n|\,|\alpha_n|\to0.
 \tag{AE.18}
\]

The escaping version adds $|\alpha_n|\to\infty$. The sum in (AE.18) is bounded, so
$|\alpha_n|\leq|\alpha_n+\beta_n|+|\beta_n|$ and the reverse inequality hold. Consequently the product condition is unchanged if $\alpha_n$ is replaced by $\beta_n$, and divergence of one covector is equivalent to divergence of the other. Both operations are therefore symmetric in $A,B$.

There is also a normal-cone description independent of the graph notation. For subsets of a manifold, let $C(S,T)$ denote the normal cone of $S\times T$ along the diagonal, with normal vector equal to the first displacement minus the second. Applying the symplectic identification (AE.6) gives

\[
 A\widehat+ B=T^*X\cap C(A,B^a),\qquad
 A\widehat+_\infty B=\dot\pi_\pi\dot\pi_d^{-1}C(A,B^a),
 \tag{AE.19}
\]

where $\pi:T^*X\to X$ and the intersection uses the embedded copy of $T^*X$ specified by (AE.4). These are precisely (AE.12)–(AE.13) for the diagonal. Equation (AE.18) removes any possible sign ambiguity in interpreting (AE.19).

## SH02-AE-NONCHAR — Finite limits, escape, and local noncharacteristicity

If $A\subset T^*X$ is closed and conic, then

\[
 f^\sharp A=f_df_\pi^{-1}A\ \cup\ f^\sharp_\infty A.
 \tag{AE.20}
\]

Likewise, for closed conic $A,B\subset T^*X$,

\[
 A\widehat+ B=(A+B)\ \cup\ (A\widehat+_\infty B).
 \tag{AE.21}
\]

**Proof.** A bounded input-covector subsequence in (AE.14), with $B$ the zero section, has a convergent subsequence $\xi_n\to\xi$. Closedness gives $(f(y_0);\xi)\in A$, and the limiting equation is $\eta_0=(df_{y_0})^t\xi$. If the input is unbounded, choose a subsequence whose norm tends to infinity; it witnesses the second set in (AE.20). Constant sequences give the ordinary inclusion, and the escaping inclusion is part of the definition. In (AE.18), boundedness of one covector bounds the other; closedness of both sets then gives the ordinary sum. This proves (AE.21) in the same way. $\square$

The escaping set is empty exactly under the usual global noncharacteristic condition:

\[
 f^\sharp_\infty A=\varnothing
 \quad\Longleftrightarrow\quad
 f_\pi^{-1}A\cap\ker f_d\subset Y\times_XT_X^*X.
 \tag{AE.22}
\]

Indeed, if an escaping sequence exists, normalize $\xi_n$ by its norm. A unit-covector subsequence converges to a nonzero covector in $A$ over $f(y_0)$, while $(df_{y_n})^t\xi_n/|\xi_n|\to0$. It is characteristic. Conversely, a nonzero characteristic covector $\xi$ at $f(y)$ gives the constant-base sequence $n\xi$, which witnesses $(y;0)\in f^\sharp_\infty A$. Similarly,

\[
 A\widehat+_\infty B=\varnothing
 \quad\Longleftrightarrow\quad A\cap B^a\subset T_X^*X.
 \tag{AE.23}
\]

Normalize the two summands in an escaping sequence to obtain the same nonzero limit with opposite signs; conversely use $n\xi$ and $-n\xi$ at a characteristic point.

For an arbitrary subset $V\subset T^*Y$, we say that $f$ is **noncharacteristic for $A$ on $V$** when

\[
 f^\sharp_\infty A\cap V=\varnothing.
 \tag{AE.24}
\]

Neither openness nor conicity of $V$ is required. For a bounded complex $F$ on $X$, replace $A$ by $\operatorname{SS}(F)$. This definition controls selected output directions, whereas (AE.22) controls all of them. Closedness of the escaping set gives a useful local consequence: around a compact subset of its complement there is a neighborhood that still contains no escaping output. Any sequence satisfying (AE.14) with a limit in that compact set therefore has bounded input covectors after passing to a subsequence. It does not assert a global bound over an arbitrary noncompact $V$.

## SH02-AE-REGULARITY — Why the smooth structure is retained

For a smooth coordinate change $h$, the transformed covector sum differs from the transform of $\alpha_n+\beta_n$ by a term bounded by

\[
 C|x_n-y_n|\,|\alpha_n|
 \tag{AE.25}
\]

on a relatively compact chart. The bound follows from the local Lipschitz property of the differential of the cotangent coordinate change. It tends to zero by (AE.18). The same estimate, together with the chain rule, verifies covariance of (AE.14). This is also guaranteed by the invariant normal-cone construction.

One should not infer invariance under arbitrary $C^1$ coordinate changes from the $C^1$ invariance of microsupport itself. Here is a direct counterexample for the set operation. In coordinates $(u,v)$ on $\mathbb R^2$, take

\[
 A=\{(0,v;\lambda\,du):v\geq0,\ \lambda\geq0\},\qquad
 B=\{(0,0;-\lambda\,du):\lambda\geq0\}.
 \tag{AE.26}
\]

Every covector in $A\widehat+ B$ over the origin is a multiple of $du$. Fix $0<a<1$ and make the $C^1$ coordinate change

\[
 U=u+\frac{|v|^{1+a}}{1+a},\qquad V=v.
 \tag{AE.27}
\]

At $v=t>0$, $du=dU-t^a dV$. Take $\lambda=t^{-a}$. The covectors $\lambda du$ at $(0,t)$ and $-\lambda du$ at $(0,0)$ sum, in the new coordinates, to $-dV$. Their new base separation is $O(t)$, so its product with their size is $O(t^{1-a})\to0$. Thus the new asymptotic sum contains $-dV$ over the origin. The cotangent map at the origin is the identity, so it cannot be the transform of the old sum. All subsequent results keep the smooth hypotheses stated at the start.

## SH02-AE-LIMITS — Two continuity arguments with different supports

The next theorem needs both ordinary and proper-support extension. Their limits are different, so we establish each comparison with its actual maps.

**Increasing opens and ordinary direct image.** Let $O_n$ increase to $O$ in a locally compact Hausdorff space $Z$, and let $F\in D^+(k_O)$. For the open inclusions $j_n:O_n\to Z$ and $j:O\to Z$,

\[
 Rj_*F\simeq R\!\varprojlim_n Rj_{n*}(F|_{O_n}).
 \tag{AE.28}
\]

Take a bounded-below injective resolution $I$ on $O$. Restriction to an open set preserves injectives, and direct image along an open inclusion preserves injectives. Thus all terms are represented by $j_{n*}(I|_{O_n})$. In each degree, their restriction maps are surjective on sections over every open $V\subset Z$: injective sheaves are flabby, and $V\cap O_n\subset V\cap O_{n+1}$. Their ordinary inverse limit has sections $\varprojlim_n\Gamma(V\cap O_n;I)=\Gamma(V\cap O;I)$ by sheaf gluing. The map $1-\mathrm{shift}$ on the product of these section groups is surjective: choose a first component, then lift recursively using the surjective restrictions. The same assertion therefore holds for the product sheaves. The homotopy-limit triangle

\[
 R\!\varprojlim K_n\longrightarrow\prod_n K_n
 \xrightarrow{1-\mathrm{shift}}\prod_n K_n\xrightarrow{+1}
\]

computes the ordinary limit complex in this case and proves (AE.28). This uses actual restriction maps; no termwise cohomology stabilization has been assumed. The right derived functors $R\Gamma_S=R\mathcal Hom(k_S,-)$ and $Rq_*$ preserve this homotopy limit, as right adjoints. In particular, if $Rq_*R\Gamma_S Rj_{n*}(F|_{O_n})=0$ for every $n$, then $Rq_*R\Gamma_S Rj_*F=0$.

**Increasing opens and extension by zero on a compact test.** Let $K$ be a compact locally closed subset of $Z$. Then the natural maps give

\[
 \operatorname{colim}_n H^m(K;j_{n!}(F|_{O_n}))
 \simeq H^m(K;j_!F).
 \tag{AE.29}
\]

To prove it, put $V=K\cap O$ and $V_n=K\cap O_n$. Open-extension base change identifies the left terms with $H_c^m(V_n;F|_{V_n})$, and the right term with $H_c^m(V;F|_V)$, since $K$ is compact. Choose a $c$-soft resolution on $V$. Its restrictions to the open $V_n$ compute these compact-support groups. Every compact support in $V$ lies in some $V_n$, by compactness and monotonicity. Consequently the complexes of compactly supported sections satisfy

\[
 \operatorname{colim}_n\Gamma_c(V_n;I)=\Gamma_c(V;I).
\]

Filtered colimits of modules are exact, proving (AE.29). The comparison respects restriction between the compact caps used below, because every arrow came from restriction and extension by zero. Compactness of $K$ is essential in this proof. We have not asserted that cohomology on an arbitrary noncompact closed set commutes with these colimits.

## SH02-AE-MOVING — A uniform separation lemma for a moved boundary

Work near $x_0$ in a vector space and let $O$ be open. Suppose a pointed closed cone $C$ with nonempty interior satisfies $O+C\subset O$ locally. Choose $v\in\operatorname{Int}C$. On a smaller neighborhood there is $c_0>0$ such that

\[
 \langle v,\eta\rangle\geq c_0|\eta|
 \quad\text{for every }\eta\in N^*(O).
 \tag{AE.30}
\]

Indeed $N^*(O)\subset C^\circ$, and strict positivity of $v$ on the unit section of $C^\circ$ is uniform by compactness.

Let $A\subset T^*O$ be conic. Fix $\xi_0\ne0$, write $\ell(x)=\langle x-x_0,\xi_0\rangle$, and introduce a sign $\epsilon\in\{1,-1\}$. Assume

\[
 (x_0;\xi_0)\notin A\widehat+\epsilon N^*(O),
 \qquad \epsilon\langle v,\xi_0\rangle<0.
 \tag{AE.31}
\]

For small $s,t>0$ put

\[
 h_s(x)=s+\epsilon\ell(x),\quad
 H_s=\{h_s>0\},\quad
 \phi_{t,s}(x)=x-t h_s(x)v,\quad
 O_{t,s}=H_s\cap\phi_{t,s}^{-1}(O).
 \tag{AE.32}
\]

All sets are considered inside a fixed chart; further shrinkings have no effect near $x_0$. The derivative is $I-\epsilon t(v\otimes\xi_0)$, whose determinant is $1-\epsilon t\langle v,\xi_0\rangle>0$. Thus $\phi_{t,s}$ is an affine diffeomorphism. On $H_s$, the closure of its inverse-image domain lies inside $O$: a point of $\overline O$ moved by the positive strict inward vector $t h_s v$ lies in $O$. Also $O_{t,s}$ increases as $t\downarrow0$, and its union is $O\cap H_s$. If $0<t'<t$, the difference between $\phi_{t',s}(x)$ and $\phi_{t,s}(x)$ is $(t-t')h_s(x)v$, an inward translation. Every point of $O\cap H_s$ belongs to a sufficiently small member by openness. This proves both assertions.

At points of $H_s$, a boundary covector is

\[
 \theta=(d\phi_{t,s})^t\eta
 =\eta-\epsilon t\langle v,\eta\rangle\xi_0,
 \qquad (\phi_{t,s}(x);\eta)\in N^*(O).
 \tag{AE.33}
\]

**Uniform lemma.** There are neighborhoods $V$ of $x_0$, $W$ of $\xi_0$, and $\delta>0$ such that for $0<s,t<\delta$:

\[
 \begin{split}
 A\cap(\epsilon N^*(O_{t,s}))^a
 &\subset T_X^*X\quad\text{over }V\cap H_s,\\
 (A+\epsilon N^*(O_{t,s}))\cap((V\cap H_s)\times W)
 &=\varnothing.
 \end{split}
 \tag{AE.34}
\]

**Proof.** A failure for arbitrarily small neighborhoods and parameters gives $x_n\to x_0$, $s_n,t_n\downarrow0$, covectors $\alpha_n\in A_{x_n}$ and nonzero boundary covectors $\theta_n$, and either $\alpha_n+\epsilon\theta_n=0$ or $\alpha_n+\epsilon\theta_n=\beta_n\to\xi_0$. The case of a zero boundary covector in the second alternative would already put $(x_0;\xi_0)$ in the closure of $A$, hence in the forbidden asymptotic sum; discard it. Write $c=0$ or $1$ for the two alternatives, and use (AE.33) to obtain $y_n=\phi_{t_n,s_n}(x_n)$ and $\eta_n\in N^*_{y_n}(O)$. Then

\[
 \rho_n:=\alpha_n+\epsilon\eta_n
 =c\beta_n+t_n\langle v,\eta_n\rangle\xi_0.
 \tag{AE.35}
\]

The coefficient $a_n=t_n\langle v,\eta_n\rangle$ is nonnegative and positive when $\eta_n\ne0$. For $c=0$, $\rho_n$ has exactly the direction $\xi_0$. For $c=1$, write $\rho_n=(1+a_n)\xi_0+(\beta_n-\xi_0)$; its normalized direction tends to $\xi_0/|\xi_0|$. In either case $\rho_n\ne0$ for large $n$, and $|\rho_n|\geq c_1t_n|\eta_n|$ for a fixed positive $c_1$, by (AE.30). Therefore

\[
 \frac{|x_n-y_n|\,|\eta_n|}{|\rho_n|}
 \leq c_2 h_{s_n}(x_n)\longrightarrow0.
 \tag{AE.36}
\]

Since $\alpha_n=\rho_n-\epsilon\eta_n$, the same product tends to zero with $\alpha_n$ in place of $\eta_n$. Divide both covectors by $|\rho_n|$. Conicity and (AE.18) show that $(x_0;\xi_0/|\xi_0|)\in A\widehat+\epsilon N^*(O)$, contradicting (AE.31). This proves the two uniform assertions simultaneously. Notice that the positive coefficient in (AE.35) is the same for the two signs; the reflection in the definition of $h_s$ is what makes this true. $\square$

## SH02-AE-OPEN — Extension from an arbitrary open set

Let $O\subset X$ be any open subset, $j:O\hookrightarrow X$, and $F\in D^b(k_O)$. Then

\[
 \begin{split}
 \operatorname{SS}(Rj_*F)&\subset
 \operatorname{SS}(F)\widehat+N^*(O),\\
 \operatorname{SS}(j_!F)&\subset
 \operatorname{SS}(F)\widehat+N^*(O)^a.
 \end{split}
 \tag{AE.37}
\]

The sheaf $j_!F$ may equivalently be written $Rj_!F$, since extension by zero along an open embedding is exact. There is no properness condition on $j$. The set $\operatorname{SS}(F)$ is considered inside $T^*X|_O$; it need not be closed in all of $T^*X$.

**Proof.** Away from $\overline O$ the two extensions vanish. Inside $O$ they agree with $F$, and adding the zero conormal recovers its microsupport. At a boundary point outside the closed support of the extension there is nothing to prove. At a remaining boundary point $x_0$, zero covectors of $\operatorname{SS}(F)$ approach $x_0$. Thus the right side contains the entire appropriate signed cone $\epsilon N_{x_0}^*(O)$, and contains the zero covector. It suffices to exclude a nonzero $(x_0;\xi_0)$ outside that right side.

Use $\epsilon=1$ for ordinary extension and $\epsilon=-1$ for extension by zero. Since $\xi_0\notin\epsilon N_{x_0}^*(O)$, the local inward-cone property in `SH02-AE-IMPORTS` supplies $C,v$ satisfying (AE.31). Construct (AE.32) and apply the uniform lemma with $A=\operatorname{SS}(F)$. Fix one sufficiently small $s>0$. The sets $O_{t,s}$ are now actual open subsets of $O\cap H_s$. This localization is necessary: the unrestricted affine inverse image need not lie in $O$ outside $H_s$.

Because $\overline{O_{t,s}}\cap H_s\subset O$, the complex $F$ is defined on a neighborhood of every boundary point relevant inside $H_s$. One can therefore apply (AE.2) there, using any extension of $F$ to the chart, without adding a hypothesis on a nonexistent ambient complex. The first line of (AE.34) is exactly its noncharacteristic hypothesis. The second gives, for

\[
 K_t=\begin{cases}
 Rj_{t,s*}(F|_{O_{t,s}}),&\epsilon=1,\\
 j_{t,s!}(F|_{O_{t,s}}),&\epsilon=-1,
 \end{cases}
\]

the uniform exclusion $\operatorname{SS}(K_t)\cap((V\cap H_s)\times W)=\varnothing$.

For $\epsilon=1$, choose the fixed cone-open lens $S=O_1\setminus O_0$ supplied by propagation, with $x_0\in\operatorname{Int}S\subset V\cap H_s$, and $Rq_{C'*}R\Gamma_S K_t=0$ for all small $t$. Select a decreasing sequence $t_n\to0$. Its domains exhaust $O\cap H_s$. Equation (AE.28), followed by preservation of its homotopy limit by $Rq_{C'*}R\Gamma_S$, gives the same vanishing for $Rj_*F|_{H_s}$. The cone test excludes $(x_0;\xi_0)$ from its microsupport.

For $\epsilon=-1$, choose fixed compact cap and base tests $K_x$ and $L_x$, for all $x$ in a neighborhood of $x_0$, lying inside $V\cap H_s$. The uniform test theorem gives isomorphisms

\[
 H^m(K_x;K_t)\xrightarrow{\sim}H^m(L_x;K_t)
\]

for every integer $m$ and every sufficiently small $t$. Apply (AE.29) separately to these two compact sets. Its naturality preserves the restriction map, so the corresponding map for $j_!F$ is also an isomorphism. The cap test excludes the chosen covector. This proves both lines of (AE.37). No Verdier biduality or finiteness of stalks is used to derive the second line from the first. $\square$

## SH02-AE-BOUNDARY-SEQUENCE — What adding a full conormal permits

Let $M=\{u=0\}$ in coordinates $(u,z)$, and let $A\subset T^*X$ be conic. For a specified ambient covector $(0,z_0;a_0,b_0)$,

\[
 (0,z_0;a_0,b_0)\in A\widehat+T_M^*X
 \tag{AE.38}
\]

if and only if some $(u_n,z_n;a_n,b_n)\in A$ satisfy

\[
 u_n\to0,\quad z_n\to z_0,\quad b_n\to b_0,
 \quad |u_n|\,|a_n|\to0.
 \tag{AE.39}
\]

In particular the criterion does not depend on $a_0$.

**Proof.** A conormal covector has zero tangential component and a base point on $u=0$. In (AE.18), convergence of the sum therefore gives $b_n\to b_0$, and the base separation bounds $|u_n|$. This proves necessity. Conversely pair the given covector with $(0,z_n;a_0-a_n,0)\in T_M^*X$. Their sum is $(a_0,b_n)$; their base separation is $|u_n|$. The product with the full first covector norm tends to zero because $b_n$ is bounded. This proves sufficiency. $\square$

Projection to $T^*M$ of the set in (AE.38) is consequently

\[
 T^*M\cap C_{T_M^*X}(A),
 \tag{AE.40}
\]

by (AE.10). The full normal covector can be adjusted freely, while the tangential part still satisfies a nontrivial growth restriction.

## SH02-AE-BOUNDARY — The trace across a missing submanifold

Let $M$ be a closed smooth submanifold, $U=X\setminus M$, and let $j:U\hookrightarrow X$, $i:M\hookrightarrow X$. For $F\in D^b(k_U)$ and $A=\operatorname{SS}(F)$,

\[
 \begin{split}
 \operatorname{SS}(Rj_*F)\cap T^*X|_M&\subset A\widehat+T_M^*X,\\
 \operatorname{SS}(j_!F)\cap T^*X|_M&\subset A\widehat+T_M^*X,\\
 \operatorname{SS}(i^{-1}Rj_*F)&\subset T^*M\cap C_{T_M^*X}(A).
 \end{split}
 \tag{AE.41}
\]

The third line is an estimate in $T^*M$ for the restriction of the ordinary extension to the missing submanifold. The first two are ambient estimates over $M$. They do not replace the sign-sensitive bounds (AE.37) when the boundary is a hypersurface with a selected side.

**Proof of the ambient estimates.** The claim is local near $M$. Work in a product chart $X=\mathbb R^r_u\times\mathbb R^m_z$, $M=\{u=0\}$; restricting to smaller product charts gives the same argument. If $r=0$, the complement is empty and all assertions are zero. Assume $r>0$.

Introduce the smooth manifold

\[
 B=S^{r-1}\times\mathbb R_t\times\mathbb R^m_z,
 \qquad \beta(\theta,t,z)=(t\theta,z).
 \tag{AE.42}
\]

It is the double of the oriented real blowup; allowing both signs of $t$ ensures that $B$ is a manifold without boundary. The map $\beta$ is proper: over a compact set, $|t|=|u|$ and $z$ remain bounded and closed, while the sphere factor is compact. The positive part $B_+=\{t>0\}$ maps diffeomorphically to $U$. Its boundary $D=\{t=0\}$ is a smooth hypersurface. If $r=1$, the sphere consists of two points and the same description applies to the two local sides.

Let $G$ be the pullback of $F$ under $B_+\simeq U$, and $k:B_+\hookrightarrow B$. Composition gives

\[
 R\beta_*Rk_*G\simeq Rj_*F,\qquad
 R\beta_*k_!G\simeq j_!F.
 \tag{AE.43}
\]

For the second equality use $R\beta_*=R\beta_!$, since $\beta$ is proper. By (AE.37), both boundary microsupports on $B$ are contained in $\operatorname{SS}(G)\widehat+T_D^*B$, because either half-ray normal lies in the full conormal. The proper direct-image estimate now says that an ambient covector $(0,z_0;a_0,b_0)$ in either left side of (AE.41) must lift, for some $\theta_0\in S^{r-1}$, to

\[
 (\theta_0,0,z_0;\ 0,\langle\theta_0,a_0\rangle,b_0)
 \in\operatorname{SS}(G)\widehat+T_D^*B.
 \tag{AE.44}
\]

The first cotangent component is in $T^*_{\theta_0}S^{r-1}$ and vanishes because $d\beta$ on a sphere-tangent vector is multiplied by $t=0$.

Apply (AE.39) to the hypersurface $t=0$. There are

\[
 (\theta_n,t_n,z_n;\lambda_n,\tau_n,b_n)\in\operatorname{SS}(G)
\]

with $\theta_n\to\theta_0$, $t_n\downarrow0$, $z_n\to z_0$, $\lambda_n\to0$, $b_n\to b_0$, and $t_n|\tau_n|\to0$. The inverse-image formula for the diffeomorphism on $B_+$ gives covectors $(t_n\theta_n,z_n;a_n,b_n)\in A$ satisfying

\[
 \lambda_n=t_n\,a_n|_{T_{\theta_n}S^{r-1}},\qquad
 \tau_n=\langle\theta_n,a_n\rangle.
 \tag{AE.45}
\]

Use the Euclidean metric only for this estimate. The tangential and radial components are orthogonal, so

\[
 t_n^2|a_n|^2=|\lambda_n|^2+t_n^2|\tau_n|^2\longrightarrow0.
 \tag{AE.46}
\]

Putting $u_n=t_n\theta_n$ gives $|u_n|\,|a_n|\to0$. Thus (AE.39) holds, and (AE.38) proves the first two lines of (AE.41). This calculation accounts for large normal covectors; boundedness of $a_n$ has not been assumed.

**Proof of the trace estimate.** The canonical localization triangle is

\[
 j_!F\longrightarrow Rj_*F\longrightarrow i_*i^{-1}Rj_*F\xrightarrow{+1}.
 \tag{AE.47}
\]

The third term is supported on $M$. The triangular microsupport inequality and the first two estimates put its microsupport in $A\widehat+T_M^*X$. The exact cotangent formula for a closed embedding identifies its projection to $T^*M$ with $\operatorname{SS}(i^{-1}Rj_*F)$. Equation (AE.40) then proves the last line. If $M$ is empty, there is no boundary and the last assertion is empty; the formulas remain valid. $\square$

## SH02-AE-MICROPROPER — Compact control of fiber locations

Let $q:X\times Y\to X$ be projection. For cotangent coordinates $(x,y;\xi,\eta)$ set

\[
 p:T^*(X\times Y)\longrightarrow T^*X\times Y,
 \qquad p(x,y;\xi,\eta)=(x;\xi,y).
 \tag{AE.48}
\]

It forgets the $Y$ covector, not the $Y$ point. Fix an open subset $\Omega\subset T^*X$ and $F\in D^b(k_{X\times Y})$. Put $A=\operatorname{SS}(F)$. Assume

\[
 \overline{p(A)}\cap(\Omega\times Y)\longrightarrow\Omega
 \quad\text{is proper}.
 \tag{AE.49}
\]

The closure is part of the assumption. This is equivalent to the following quantified compact control: for every compact $K\subset\Omega$, there is a compact $L\subset Y$ such that

\[
 A\cap(K\times T^*Y)\subset K\times T^*Y|_L.
 \tag{AE.50}
\]

In these formulas products use $T^*(X\times Y)\simeq T^*X\times T^*Y$.

**Proof of equivalence.** Under (AE.49), the inverse image of $K$ is compact; project it to $Y$ to obtain $L$. Conversely, enlarge a given compact $K$ to a compact neighborhood $K'\subset\Omega$. Such a neighborhood exists because $T^*X$ is locally compact and $\Omega$ is open. Apply (AE.50) to $K'$. Any point of $\overline{p(A)}$ over $K$ is a limit of points whose first coordinate eventually lies in $K'$, so its $Y$ coordinate lies in the compact, hence closed, set $L'$. The inverse image of $K$ in (AE.49) is consequently a closed subset of $K\times L'$, and is compact. This proves properness. The passage through $K'$ is what justifies the closure; control only over one fixed $K$ would not suffice. $\square$

Define the ordinary critical image

\[
 q_\pi q_d^{-1}A
 =\{(x;\xi):\text{some }y\in Y
             \text{ satisfies }(x,y;\xi,0)\in A\}.
 \tag{AE.51}
\]

**Theorem.** Under (AE.49),

\[
 \begin{split}
 \operatorname{SS}(Rq_*F)\cap\Omega&\subset q_\pi q_d^{-1}A,\\
 \operatorname{SS}(Rq_!F)\cap\Omega&\subset q_\pi q_d^{-1}A,
 \end{split}
 \tag{AE.52}
\]

and the canonical comparison

\[
 Rq_!F\longrightarrow Rq_*F
 \tag{AE.53}
\]

is an isomorphism in the localized category $D^b(k_X;\Omega)$. Equivalently its cone has microsupport disjoint from $\Omega$. Only the definition and cone criterion of [the localized category](microlocal-categories.md) are needed; the representability theorems for four localized operations are not prerequisites of this result.

**Proof.** If $Y$ is empty, $F$ and both direct images are zero, so all assertions hold. Assume $Y$ is nonempty. First reduce the fiber to a ball. Choose a proper smooth embedding $e:Y\hookrightarrow\mathbb R^N$ and replace $F$ by $(\mathrm{id}_X\times e)_*F$. The exact closed-embedding microsupport formula preserves the $X$ covector; its $Y$-base projection is transported by the proper map $e$. Thus (AE.50) is preserved. Composition identifies both direct images with the original ones, including their comparison. After a diffeomorphism $\mathbb R^N\simeq B^N$, we may assume $Y=B^N$, the unit open ball. Compact control is preserved because compact sets map to compact sets. In dimension zero $q$ is the identity and the assertion is immediate, so take $N>0$.

Write $\overline q:X\times\mathbb R^N\to X$, let $j:X\times B^N\hookrightarrow X\times\mathbb R^N$, and put $Z=X\times S^{N-1}$. The supports of both $j_!F$ and $Rj_*F$ lie in $X\times\overline B^N$. Therefore $\overline q$ is proper on their closed supports, as well as on the support of the cone of $j_!F\to Rj_*F$. Composition gives

\[
 Rq_!F\simeq R\overline q_*j_!F,\qquad
 Rq_*F\simeq R\overline q_*Rj_*F.
 \tag{AE.54}
\]

The open-boundary estimate bounds either extension by $A$ in the interior and by

\[
 T_Z^*(X\times\mathbb R^N)\widehat+ A
 \tag{AE.55}
\]

on $Z$. The localization triangle bounds the microsupport of their comparison cone by (AE.55), since that cone is supported on $Z$.

We show that no covector in (AE.55) can project critically to $\Omega$. Suppose otherwise. The sum criterion supplies covectors of $A$ with coordinates $(x_n,y_n;\xi_n,\eta_n)$ tending in base to $(x_0,y_0)$ with $y_0\in S^{N-1}$, and conormal covectors to $Z$ whose $X$ component is zero, such that the sum tends to $(x_0,y_0;\xi_0,0)$ with $(x_0;\xi_0)\in\Omega$. In particular $(x_n;\xi_n)\to(x_0;\xi_0)$. Place all sufficiently late terms in a compact neighborhood $K\subset\Omega$. By (AE.50), $y_n$ lies in one compact $L\subset B^N$. Such a sequence cannot converge to the sphere. This contradiction excludes (AE.55). The weighted product condition is compatible with this argument but is not needed for the exclusion: compact control already forbids its base points.

Apply the proper direct-image estimate to (AE.54). All boundary contributions have just been excluded over $\Omega$, so only the interior covectors with zero $Y$ component remain. This is precisely (AE.51), proving (AE.52). Apply the same estimate to the pushed-forward comparison cone. Its microsupport misses $\Omega$, which is exactly the cone criterion for (AE.53) to be invertible in $D^b(k_X;\Omega)$. All identifications arose by composition of the ordinary comparison maps, so the isomorphism concerns the canonical arrow, not merely an abstract isomorphism between the two objects. $\square$

Condition (AE.49) controls the locations of all fiber covectors above the chosen $X$ covectors. Requiring compactness only where $\eta=0$ would be weaker and would not exclude the boundary sequence in the proof. Ordinary properness of $q$ on $\operatorname{supp}(F)$ implies the condition over appropriate base neighborhoods, but the condition can hold away from the zero section even when the entire support is nonproper.

## SH02-AE-PROBLEMS — Calculations that test the hypotheses

For the sheaf examples in this section, assume $k\ne0$. The preceding theorems retain their stated coefficient hypotheses.

### SH02-AE-PROBLEM-CANCELLATION — A sum gains a new direction at the limit

In $T^*\mathbb R^2$, with base coordinates $(u,v)$, set

\[
 \begin{split}
 A&=\{(t,0;\lambda\,du):t\geq0,\lambda\geq0\},\\
 B&=\{(t,0;\lambda(-du+t\,dv)):t\geq0,\lambda\geq0\}.
 \end{split}
 \tag{AE.56}
\]

Show that these are closed conic sets, that $(0,0;dv)$ is absent from $A+B$, and that it belongs to $A\widehat+_\infty B$.

**Solution.** Positive scaling changes only $\lambda$. In a convergent finite-covector sequence, the $du$ component bounds $\lambda$ in both sets. Passing to the limit proves closedness, including at $t=0$. At the origin both fibers lie in the line spanned by $du$, so their ordinary sum cannot contain $dv$. For $t>0$, choose $\lambda=1/t$ in both fibers. Their sum is exactly $dv$, their common base tends to the origin, the base-separation product is zero, and their norms diverge. Equation (AE.18) proves the escaping membership. The nonzero characteristic intersection at the origin is the positive $du$ ray in $A\cap B^a$, in agreement with (AE.23).

### SH02-AE-PROBLEM-ZERO — Escape can have zero output

Let $f:\{*\}\to\mathbb R$ select $0$, and let $A=\{(0;\lambda\,dx):\lambda\geq0\}$. Determine $f^\sharp_\infty A$.

**Solution.** The target cotangent space $T^*\{*\}$ consists of its zero vector. The input sequence $n\,dx$ has norm tending to infinity and is killed by $(df)^t=0$; the base error is zero. Thus $f^\sharp_\infty A=\{0\}$. Removing zero output covectors would give the wrong answer. The punctured conormal base in (AE.13) records a nonzero characteristic input even when its output is zero.

### SH02-AE-PROBLEM-SIGNS — The two ends of an interval

Take $O=(-2,3)\subset\mathbb R$ and $F=k_O$ as a constant sheaf on $O$. Compute the nonzero boundary microsupports of $j_!F$ and $Rj_*F$.

**Solution.** Every sufficiently small intersection of $O$ with a neighborhood of either endpoint is an interval, so $Rj_*F=k_{[-2,3]}$ with no higher direct image. At the left endpoint the strict inward normal is positive, while at the right it is negative. The local half-line support test therefore gives

| Endpoint | $\operatorname{SS}(Rj_*F)$, nonzero boundary covectors | $\operatorname{SS}(j_!F)$, nonzero boundary covectors |
| --- | --- | --- |
| $-2$ | $\lambda\,dx$, $\lambda>0$ | $\lambda\,dx$, $\lambda<0$ |
| $3$ | $\lambda\,dx$, $\lambda<0$ | $\lambda\,dx$, $\lambda>0$ |

For example, at $-2$ the constant section of $k_{[-2,3]}$ survives the test supported on $x\geq-2$, whereas the opposite test does not. The localization triangle between the open and closed interval gives the reversed ray for extension by zero. The zero-section part is the closed support of each object, including both endpoints; a zero stalk at an endpoint of $j_!F$ does not remove that endpoint from the closed support. Equation (AE.37) is sharp in this example for both signs.

### SH02-AE-PROBLEM-ESCAPING-FIBER — Why a nonproper image needs a condition

Let $q:\mathbb R_x\times\mathbb R_y\to\mathbb R_x$, let

\[
 Z=\{(x,y):xy=1,\ y>0\},\qquad F=k_Z.
 \tag{AE.57}
\]

Show that the ordinary critical image of $\operatorname{SS}(F)$ misses every nonzero covector over $x=0$, although both direct images have boundary microsupport there. Identify the failure of (AE.50).

**Solution.** The set $Z$ is a closed smooth submanifold of $\mathbb R^2$: no finite limit point can have $y=0$ while $xy=1$. Its conormal covectors are

\[
 (x,y;\lambda y,\lambda x),\qquad xy=1,\ y>0.
\]

A zero $y$ component forces $\lambda=0$, since $x>0$ on $Z$. Thus the ordinary critical image is just the zero section over $x>0$. On the other hand $q|_Z$ identifies $Z$ with $(0,\infty)$, so

\[
 Rq_!F=k_{(0,\infty)},\qquad
 Rq_*F=k_{[0,\infty)}.
 \tag{AE.58}
\]

They have respectively negative and positive boundary rays at zero. For $x_n\downarrow0$, put $y_n=1/x_n$ and $\lambda_n=x_n$. The conormal covector has $X$ component $1$ and $Y$ component $x_n^2$. Its $X$ cotangent coordinates lie in the compact set $\{(x;1):0\leq x\leq1\}$, while $y_n\to\infty$. Therefore no compact $L$ in (AE.50) exists over that set. The escaping fiber is precisely what creates the missing boundary information. The cone of the comparison in (AE.58) is $k_{\{0\}}$, so the comparison is not a microlocal isomorphism at any covector over zero.

### SH02-AE-PROBLEM-MICROPROPER — A nonproper support with an admissible direction set

For the same projection, take

\[
 F=k_{[0,\infty)\times\{0\}}\oplus k_{\mathbb R^2},
 \qquad\Omega=T^*\mathbb R\setminus T^*_{\mathbb R}\mathbb R.
 \tag{AE.59}
\]

Verify (AE.49), compute the two direct images, and explain why their comparison is invertible on $\Omega$.

**Solution.** The first summand has proper support over $\mathbb R_x$; all its fiber locations have $y=0$. The second has zero-section microsupport, so its $X$ covector is zero and cannot meet $\Omega$. Therefore every compact $K\subset\Omega$ satisfies (AE.50) with $L=\{0\}$. The entire support of $F$ is nevertheless $\mathbb R^2$, on which $q$ is nonproper.

Choose the usual orientation of the $y$ line. Ordinary cohomology of that line is $k$ in degree zero, and compactly supported cohomology is $k$ in degree one. Hence

\[
 Rq_!F\simeq k_{[0,\infty)}\oplus k_{\mathbb R}[-1],\qquad
 Rq_*F\simeq k_{[0,\infty)}\oplus k_{\mathbb R}.
 \tag{AE.60}
\]

The comparison is the identity on the first summand. Both constant-sheaf terms have microsupport in the zero section and become zero objects on $\Omega$. Their comparison is consequently an isomorphism there. This checks the theorem without incorrectly claiming a global isomorphism between the complexes in (AE.60).

## SH02-AE-RESEARCH — Using the estimates without losing information

The normal-cone sequence criterion is a practical way to analyze a characteristic pullback. First retain the tangential output, then determine whether a bounded input subsequence exists. If it does, the ordinary cotangent image accounts for that limit. If it does not, the escaping operation is an additional geometric object that must be computed or excluded. The criterion on $V$ in (AE.24) permits this analysis in only the output directions relevant to a problem.

For an open extension, the first question is which boundary sign belongs to the functor. For a missing submanifold with all normal directions allowed, the trace estimate (AE.41) is often sharper after projecting to the submanifold: it retains the product bound on the normal covector while forgetting its arbitrary final normal component. This is the estimate used by specialization on a normal deformation.

For direct image over a noncompact fiber, compactness of critical points alone is insufficient. The compact control in (AE.50) concerns every fiber covector above the selected base covectors, so it prevents the compactification from acquiring a characteristic contribution at its new boundary. This observation is useful for local kernel composition and for properness hypotheses stated only in a microlocal region.

The exact approved comparison is Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 4.3.4 and Corollary 4.3.5 (printed 70–72), Theorems 4.4.1–4.4.2, and §§5.1–5.3 (printed 77–84). These passages give the two signed open-boundary estimates, the limiting boundary cone, microlocally proper projection, specialization, Fourier transport and generalized inverse images. The source uses a closure after the fibre-covector projection and differentiability at least two for these limiting operations; both features are retained. It is freely readable, not a licence to redistribute its expression.

The present proofs retain their own quantitative two-sign deformation, the sphere-coordinate boundary calculation and the full weighted-separation estimates. They explicitly distinguish ordinary proper cotangent correspondence from control of escaping covectors. The smooth-category proof is not silently extended to all continuously differentiable changes of coordinates; the counterexample remains part of the lesson.
