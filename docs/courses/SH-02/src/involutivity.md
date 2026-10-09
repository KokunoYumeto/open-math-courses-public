# SH02-INV — Hamiltonian motion forced by a sheaf

The full IC1–IC9 proof completions supply the exact microlocal Hom sign, direct identity detector, integral amplitude and bounded derived models. Their smooth/C1 and angular inputs are proved at the actual used scope. The local compact-cap proof below consequently proves I15 over the integers at every microsupport point; broader coefficient and later-theorem contracts retain their stated scope. Self-checked by the writing AI.

Let $k$ be a commutative ring of finite global dimension. Manifolds are finite dimensional and countable at infinity. Sheaf complexes belong to $D^b(k_X)$ unless another category is specified. No constructibility, finite generation, or field hypothesis is imposed.

The main result concerns the whole closed set $\operatorname{SS}(F)$, including its singular points and the zero section. Its geometric meaning is that certain limiting tangent directions cannot be absent. We first establish the geometric language and the local sheaf argument that detect an absent direction, and then obtain both involutivity and propagation of individual microlocal sections.

## SH02-INV-IMPORTS — Exact inputs and their status

The following are mathematical dependencies, not additional restrictions on $F$ or $G$.

**Directional tests.** The $C^1$ support-test definition of microsupport, its invariance under $C^1$ coordinate changes, closedness, conicity, and the triangle estimate are `SH02-MST-TEST` and `SH02-MST-FORMAL` in [the directional test unit](../../sheaf-proof-readings/SH02-microsupport-tests.html). The same unit proves the directional propagation theorem `SH02-MST-PROPAGATION` and both directions of cone cutoff, `SH02-MST-CUTOFF-FORWARD` and `SH02-MST-CUTOFF-CONVERSE`, relative to its stated sheaf foundations.

**Directional topology.** The topology associated with an arbitrary closed convex cone, its fully faithful inverse image, and its section comparison are in [the cone topology unit](../../sheaf-proof-readings/SH02-cone-topology.html). Constant sheaves on convex sets are acyclic by the convex acyclicity unit. These results retain their recorded coefficient and continuity dependencies.

**Microlocal Hom estimate.** For $F,G\in D^b(k_X)$, put $M=T^*X$ and $K=\mu\mathcal Hom(G,F)$. We use $K\in D^b(k_M)$ from the exact contract `SH02-MH-BOUNDED` in [the microlocal Hom unit](../../sheaf-proof-readings/SH02-microlocal-hom.html), including its finite-dimensional internal-Hom and microlocalization amplitude dependencies. Boundedness of the two inputs alone is not offered as a proof of this derived-Hom assertion. The exact microsupport estimate used here is

\[
-H\bigl(\operatorname{SS}(K)\bigr)
\subset C\bigl(\operatorname{SS}(F),\operatorname{SS}(G)\bigr)
\subset TM.
\tag{I1}
\]

The map $H:T^*M\to TM$ and the order of the two sets are fixed below. This is the contract `SH02-CHE-004` in [the characteristic estimates unit](../../sheaf-proof-readings/SH02-characteristic-estimates.html); its proof uses the specialization estimate and the cotangent Fourier identification. IC1 verifies the exact diagonal sign and set order, including the zero loci. The characteristic-estimate, Fourier and boundary-blowup bodies are pinned by their full used ranges in the proof binding table. IC3 proves the finite integral microlocal Hom bound actually needed for I15; no finite-generation assumption is used.

**Support and identity detection.** One has

\[
\operatorname{supp}\mu\mathcal Hom(G,F)
\subset\operatorname{SS}(G)\cap\operatorname{SS}(F),
\qquad
\bigl(\mu\mathcal Hom(F,F)\bigr)_p=0
\Longleftrightarrow p\notin\operatorname{SS}(F).
\tag{I2}
\]

IC2 proves the second assertion directly from the actual supported-kernel/projector counit and full neighbourhood test criterion, including zero covectors. The original identity-detection contract `SH02-MC-IDENTITY` in the localized category unit is retained; no quotient-category representability theorem is added as a premise of this direct detector. The first is `SH02-MO-MICROLOCAL-SUPPORT` in [the microsupport operations unit](../../sheaf-proof-readings/SH02-microsupport-operations.html). These are used separately: support containment gives an open region of vanishing, whereas identity detection gives a contradiction at a specified point.

The proof of involutivity below does not assume that an involutivity result is already available in any of these imports. In particular, the local cone argument is proved from directional propagation rather than inferred from the theorem it will establish. The noncharacteristic deformation import underlying directional propagation uses the corrected closed moving fronts; a submersive-map hypothesis in the source foundations is never replaced by mere differentiability.

The used bounded integral foundations are IC4–IC9: noncompact specialization tautness, convex traces, pointed-cone calculation, closed-strip continuity and bounded derived adjunctions. OF1–OF7 and EA1–EA11 supply their actual variable-neighbourhood geometry, all inward angular margins and the nearest-point differential. Applying I15 to underlying abelian sheaves transfers the whole microsupport statement to arbitrary original commutative unital coefficients by NMC1–NMC4 and NG5; it does not assert that coefficient forgetting commutes with microlocal Hom.

## SH02-INV-SECANTS — Two different limiting constructions

Let $A,B$ be subsets of a manifold $M$, and let $p\in\overline A\cap\overline B$. Choose coordinates centered at $p$. Define the two-set normal cone at $p$ by

\[
C_p(A,B)=
\left\{
\lim_{n\to\infty}\frac{a_n-b_n}{h_n}:
a_n\in A,\ b_n\in B,\ a_n,b_n\to p,\ h_n>0,\ h_n\to0
\right\}.
\tag{I3}
\]

Only convergent quotients enter this definition. The tangent cone based at the fixed point is

\[
C_p(A)=C_p(A,\{p\}).
\tag{I4}
\]

The union of the cones in (I3) over the relevant base points is written $C(A,B)\subset TM$. The order matters: $C_p(B,A)=-C_p(A,B)$. In particular $C_p(A,A)$ is symmetric under sign, even though $C_p(A)$ need not be symmetric. Both are closed cones, and $C_p(A)\subset C_p(A,A)$ when $p\in A$.

Here and below, a cone is closed under multiplication by positive scalars; the limiting constructions at a point of the set also contain zero. Closedness follows by a diagonal choice: for a convergent sequence of candidate vectors, select one term from each witnessing sequence so that its two points, parameter, and quotient differ from their required limits by less than the reciprocal of the index.

These definitions do not depend on the coordinates. For a $C^1$ coordinate change $f$,

\[
f(a_n)-f(b_n)
=df_p(a_n-b_n)+o(|a_n-b_n|).
\tag{I5}
\]

Indeed integrate the derivative along the coordinate segment and use its uniform convergence to $df_p$ as both endpoints approach $p$. Since $|a_n-b_n|/h_n$ is bounded, division by $h_n$ proves that the cone transforms by $df_p$. Applying the inverse coordinate change gives equality, not just containment. This also proves that tangent cones are carried correctly by a $C^1$ flow box.

Two elementary observations will be used repeatedly.

**A vanishing function kills all secants.** If a $C^1$ function $f$ vanishes on $S$ near $p$, then

\[
C_p(S,S)\subset\ker df_p.
\tag{I6}
\]

Apply (I5) to $f$; its left side is zero. More generally, if $A\subset\{f\geq0\}$ and $B\subset\{f\leq0\}$, with $f(p)=0$, then

\[
C_p(A,B)\subset\{w:df_p(w)\geq0\}.
\tag{I7}
\]

Here $f(a_n)-f(b_n)\geq0$, and the same quotient limit proves the assertion. If $df_p=0$, the right side is the whole tangent space; we do not replace this inclusion by an unjustified equality at a critical point.

**An absent tangent direction gives an empty cone.** Suppose $p\in S$ and $v\neq0$ is not in $C_p(S)$. In suitable linear coordinates, $v=(1,0)$ and there are $b>0$ and a neighborhood $W$ of $0$ such that

\[
S\cap W\cap\Gamma_b=\varnothing,
\qquad
\Gamma_b=\{(t,y):t>b|y|\}.
\tag{I8}
\]

Otherwise choose points of $S\setminus\{p\}$ approaching $p$ whose unit directions approach $v/|v|$. Rescaling their differences from $p$ to length $|v|$ gives a sequence in (I4) converging to $v$, a contradiction. A smaller circular cone around $v$ then has the form in (I8). This argument uses the fixed-point cone, not the two-set cone.

## SH02-INV-LOCAL-FLOWS — The regularity needed for a flow box

The differential-equation input used below is the following local fact. A $C^1$ vector field has a unique local flow, that flow is $C^1$ in time and initial point, and near a point where the field is nonzero there are $C^1$ coordinates making it $\partial_t$. These statements require neither a compact manifold nor a complete vector field.

Here is a proof, with the ordinary $C^1$ inverse function theorem as the sole coordinate-calculus input to the final step. In a relatively compact coordinate ball, bound $|v|$ by $M$ and $|Dv|$ by $L$. For an initial point $z$ in a smaller ball and a sufficiently short interval $[-T,T]$, the operator

\[
\mathcal P_z(c)(t)=z+\int_0^t v(c(s))\,ds
\]

takes continuous paths in the larger closed ball to themselves and contracts their uniform distance by at most $LT<1$. Iterating from the constant path produces a uniformly Cauchy sequence, since successive differences are bounded by a geometric series. Its limit is the unique fixed point, hence a $C^1$ solution. The same estimate gives uniqueness among solutions on this interval; subdividing any larger common interval gives uniqueness there too.

The integral equation for two initial points gives the bound

\[
|c_z(t)-c_w(t)|\leq e^{L|t|}|z-w|.
\]

This follows by iterating the integral inequality, whose $n$th iterated kernel contributes $L^n|t|^n/n!$. For differentiability in $z$, let $U_z$ solve the linear integral equation

\[
U_z(t)=1+\int_0^t Dv(c_z(s))U_z(s)\,ds.
\]

The same iteration constructs $U_z$ continuously in $(t,z)$. Subtract this equation, multiplied by a small initial displacement $h$, from the equations for $c_{z+h}-c_z$. Uniform continuity of $Dv$ on the compact ball makes the inhomogeneous remainder $o(|h|)$ uniformly in time; the preceding integral bound then gives $c_{z+h}(t)-c_z(t)-U_z(t)h=o(|h|)$ uniformly. Thus $D_zc_z(t)=U_z(t)$ and is continuous. Time differentiability follows from $\partial_tc_z(t)=v(c_z(t))$.

Uniqueness gives the local flow identity $c_{c_z(s)}(t)=c_z(s+t)$. Local solutions consequently glue over the union of their compatible time intervals to a unique solution on a maximal open interval. At a point $p$ with $v(p)\neq0$, choose a transverse affine hyperplane $E$ through $p$. The map $(t,y)\mapsto c_y(t)$ has derivative $(a,w)\mapsto av(p)+w$ at $(0,p)$, an isomorphism from $\mathbb R\times T_pE$. The $C^1$ inverse function theorem supplies the desired local coordinates, and the flow identity identifies the vector field with $\partial_t$. This proves the stated local fact.

## SH02-INV-HAMILTON — Signs, level sets, and time intervals

On $M=T^*X$, in cotangent coordinates $(x,\xi)$, set

\[
H\left(\sum_j a_j\,dx_j+b_j\,d\xi_j\right)
=\sum_j b_j\frac{\partial}{\partial x_j}
-a_j\frac{\partial}{\partial\xi_j}.
\tag{I9}
\]

For the canonical symplectic form $\omega=\sum_jd\xi_j\wedge dx_j$, this means $\iota_{H\theta}\omega=-\theta$. The definition is therefore coordinate independent. The identity needed for (I1) is

\[
\langle-H\alpha,\beta\rangle
=\langle\alpha,H\beta\rangle.
\tag{I10}
\]

It follows directly from (I9), or from the skew symmetry of $\omega$.

Let $\phi\in C^2(U;\mathbb R)$ on an open subset $U\subset M$. Its Hamiltonian vector field $H_\phi=H(d\phi)$ is $C^1$. The solution through $p$ has a maximal open time interval $(a_p,b_p)$ containing zero and satisfies

\[
\dot x_j=\frac{\partial\phi}{\partial\xi_j},
\qquad
\dot\xi_j=-\frac{\partial\phi}{\partial x_j}.
\tag{I11}
\]

There is no completeness assumption. The positive trajectory means its image for $0\leq t<b_p$; the negative trajectory uses $a_p<t\leq0$. Local existence, uniqueness, and the meaning of the maximal interval were established in `SH02-INV-LOCAL-FLOWS`. The derivative of $\phi$ along a solution is zero by (I10), so a trajectory starting in $V_0=\{\phi=0\}$ stays there while it exists in $U$.

If $d\phi_p=0$, the constant curve at $p$ is the unique solution through $p$. If $h$ is $C^2$ and positive near $p$, then on $V_0$ one has $H_{h\phi}=hH_\phi$. Thus $\phi$ and $h\phi$ have the same locally oriented trajectories in $V_0$: their time variables are related by a strictly increasing solution of $dt/ds=h(b(t))$. The parametrizations, and potentially the maximal time intervals, can differ. Reversing the sign of $\phi$ reverses the direction.

## SH02-INV-NAGUMO — A tangent field cannot leave a closed set

Let $Z$ be a manifold, $S\subset Z$ closed, and $v$ a $C^1$ vector field. Assume

\[
v(q)\in C_q(S)\qquad(q\in S).
\tag{I12}
\]

Then every maximal forward trajectory of $v$ starting in $S$ remains in $S$ for its entire interval of existence.

**Proof.** We give a local distance argument; it supplies both the regularity and the endpoint control. Work in a coordinate ball on which $v$ has Lipschitz constant $L$. A trajectory starting at $q_0\in S$ stays, for a short time, in a much smaller concentric ball. Intersect $S$ with a closed ball still inside the coordinate chart. This intersection is compact. By choosing the short time smaller if necessary, every closest point to the trajectory lies in the interior of that closed ball: $q_0$ is an available competitor, while points on its boundary are uniformly farther away.

Fix a point $x$ of this short trajectory and a closest point $q\in S$. Let $r=x-q$. Tangency (I12) supplies $h_n\downarrow0$ and $q_n\in S$ with

\[
q_n=q+h_nv(q)+o(h_n).
\]

Minimality of $q$ gives $|x-q_n|^2\geq|x-q|^2$. Subtract, divide by $h_n$, and let $n$ tend to infinity. The result is

\[
\langle r,v(q)\rangle\leq0.
\tag{I13}
\]

Write $d(t)^2=\operatorname{dist}(x(t),S)^2$ using the compact local intersection just chosen. For $h>0$ use the same nearest point $q$ at time $t$ as a competitor at time $t+h$. Since $x(t+h)=x(t)+hv(x(t))+o(h)$, the upper right Dini derivative satisfies

\[
D^+d(t)^2
\leq2\langle x(t)-q,v(x(t))\rangle
\leq2L\,d(t)^2.
\tag{I14}
\]

The second inequality is (I13) and the Lipschitz bound. The continuous function $e^{-2Lt}d(t)^2$ has nonpositive upper right Dini derivative and is therefore nonincreasing. Here is the elementary comparison. If a continuous function with nonpositive upper right Dini derivative increased between two endpoints, subtracting a sufficiently small positive multiple of time would preserve that increase and make the derivative strictly negative. The resulting function attains a minimum on the interval at a point before its right endpoint. All sufficiently short positive increments there are nonnegative, contradicting the strictly negative upper right derivative. Thus $d(0)=0$ implies $d(t)=0$ throughout the short interval.

This proves local forward invariance at every point of $S$. On a given maximal trajectory, if the interval of times already proved to lie in $S$ had a finite endpoint strictly inside the existence interval, closedness would put that endpoint in $S$, and local forward invariance would extend it. This is a contradiction. Hence the entire positive existence interval is contained in $S$. No compactness of $S$ or of the full trajectory has been used. $\square$

## SH02-INV-DEFINITION — Involutivity without a smoothness assumption

A locally closed subset $S\subset M=T^*X$ is **involutive at $p\in S$** when

\[
C_p(S,S)\subset\ker\theta
\quad\Longrightarrow\quad
-H\theta\in C_p(S)
\qquad(\theta\in T_p^*M).
\tag{I15}
\]

It is involutive when this holds at every point. Because both $\theta$ and $-\theta$ annihilate the same set, (I15) also forces $H\theta\in C_p(S)$. This equivalence explains why one may use either sign for the test vector in a contradiction argument; it does not change the convention in (I9).

For a $C^1$ submanifold, both cones are its tangent space: straighten the submanifold and apply (I5). Since $H$ takes its annihilator to its symplectic orthogonal, (I15) then says

\[
(T_pS)^\omega\subset T_pS.
\tag{I16}
\]

Thus the definition recovers the usual coisotropic condition at smooth points. At a singular point it retains more information than any choice of smooth strata.

**Hamiltonian invariance.** If $S$ is closed in $U$, involutive, and $\phi\in C^2(U)$ vanishes on $S$, then $S$ is a union of entire maximal trajectories of $H_\phi$ in $U$.

Indeed (I6) and (I15), applied to $d\phi$ and its negative, give both $H_\phi(q)$ and $-H_\phi(q)$ in $C_q(S)$ for every $q\in S$. Apply `SH02-INV-NAGUMO` first to $H_\phi$ and then to $-H_\phi$. Critical points are included because their trajectories are constant. Closedness in $U$, rather than in a larger ambient space, is exactly what the continuation argument requires. $\square$

## SH02-INV-CONE-VANISHING — An empty cone detects a zero stalk

Let $K\in D^b(k_W)$ on a neighborhood $W$ of $0$ in $\mathbb R\times\mathbb R^{m-1}$, with coordinates $(t,y)$. Suppose for some $b>0$ that

\[
K|_{W\cap\{t>b|y|\}}=0,
\qquad
\operatorname{SS}(K)\cap T_0^*W\subset\{\tau=0\}.
\tag{I17}
\]

Then $K_0=0$.

**Proof.** Choose $a>b$ and the closed pointed cone

\[
C=\{(t,y):t\geq a|y|\},\qquad
C^{\circ a}=\{(\tau,\eta):\tau\leq0,\ |\eta|\leq-a\tau\}.
\tag{I18}
\]

Every nonzero covector in $C^{\circ a}$ has $\tau<0$. Its unit section is compact, so closedness and conicity of microsupport, together with (I17), give a smaller neighborhood $W_1$ on which

\[
\operatorname{SS}(K)\cap
\bigl(W_1\times(C^{\circ a}\setminus\{0\})\bigr)=\varnothing.
\tag{I19}
\]

To justify the neighborhood uniformly, a failure would give base points tending to zero and unit covectors in this compact section; a convergent subsequence would contradict (I17).

Put $O_0=\{t>b|y|\}$ and, for $\epsilon>0$, put

\[
O_{1,\epsilon}=O_0\cup\bigl(-\epsilon(1,0)+\operatorname{Int}C\bigr).
\tag{I20}
\]

These are $C$-open sets, and $0\in O_{1,\epsilon}$. The difference from $O_0$ has compact closure of diameter $O(\epsilon)$. Indeed a point of its closure satisfies

\[
-\epsilon+a|y|\leq t\leq b|y|,
\]

so $|y|\leq\epsilon/(a-b)$ and $|t|$ has the same kind of bound. For every $x\in O_{1,\epsilon}$, the closed set $(x+C)\setminus O_0$ is contained in this fixed bounded cap; it is compact. For sufficiently small $\epsilon$, all such caps lie in $W_1$.

Apply `SH02-MST-PROPAGATION` with $X=W$, the cone $C$, the smaller region $W_1$, and the pair $O_0\subset O_{1,\epsilon}$. Its microsupport avoidance follows from (I19), its difference lies in $W_1$, and the preceding bound verifies its compactness hypothesis. Restriction therefore gives

\[
R\Gamma(O_{1,\epsilon}\cap W;K)
\simeq R\Gamma(O_0\cap W;K)=0.
\tag{I21}
\]

It remains to pass to the vertex; this is not a closed-fiber base-change argument. Let $Z=W\setminus O_0$ and let $i:Z\hookrightarrow W$. Because $K$ vanishes off $Z$, the closed-support equivalence identifies $K\simeq i_*i^{-1}K$. The sets $O_{1,\epsilon}\cap Z$ are relative open neighborhoods of zero in $Z$. The displayed cap bound makes them cofinal among those neighborhoods as $\epsilon\downarrow0$. Taking the filtered colimit of the cohomology groups in (I21) therefore gives every cohomology group of $(i^{-1}K)_0$. They are all zero, so $K_0=0$. $\square$

## SH02-INV-THEOREM — Microsupport is involutive

For every $F\in D^b(k_X)$, the closed conic subset $S=\operatorname{SS}(F)$ is involutive in the sense of (I15).

**Proof relative to (I1)–(I2).** Fix $p\in S$ and a covector $\theta\in T_p^*T^*X$ annihilating $C_p(S,S)$. It suffices to prove that $H\theta\in C_p(S)$, since the same proof then applies to $-\theta$.

Suppose to the contrary that $v=H\theta$ is absent from $C_p(S)$. It is nonzero. Use (I8) to choose coordinates with $p=0$, $v=(1,0)$, and an open cone $\Gamma_b$ containing no point of $S$ near zero. Set $K=\mu\mathcal Hom(F,F)$. By support containment in (I2), $K$ vanishes on this open cone.

For $\alpha\in\operatorname{SS}(K)\cap T_p^*T^*X$, the estimate (I1) puts $-H\alpha$ in $C_p(S,S)$. Therefore

\[
0=\langle-H\alpha,\theta\rangle
=\langle\alpha,H\theta\rangle
=\langle\alpha,v\rangle.
\tag{I22}
\]

Thus the second condition of (I17) holds in these coordinates as well. The cone-vanishing lemma gives $K_p=0$. Identity detection in (I2) then says $p\notin S$, contradicting its choice. This proves (I15) at every point, without removing singular points or the zero section. $\square$

Combining this theorem with `SH02-INV-DEFINITION`, if $\phi\in C^2(U)$ vanishes on $\operatorname{SS}(F)\cap U$, that set is a union of maximal Hamiltonian trajectories in $U$. This assertion is about the closed set itself. The next result keeps track of a particular cohomology section, which carries more directional information.

## SH02-INV-SECTION-FLOW — The support of a section moves forward

Let $Z$ be a manifold, $v$ a $C^1$ vector field, and $K\in D^b(k_Z)$. Assume

\[
\operatorname{SS}(K)\subset
\{(z,\alpha):\langle\alpha,v(z)\rangle\geq0\}.
\tag{I23}
\]

For every integer $j$ and every section $u\in\Gamma(Z;\mathcal H^j(K))$, its support is forward invariant under $v$: if $u_p\neq0$, then $u_{b(t)}\neq0$ for every $0\leq t<b_p$ on the maximal trajectory through $p$.

The support here is the closed set of points where the germ of this particular section is nonzero. It can be smaller than the support of $\mathcal H^j(K)$. The conclusion applies to a section on an open subset by restricting the vector field and using its trajectories in that open subset.

**Proof.** At a zero of $v$, the unique trajectory is constant. At a point where $v\neq0$, the $C^1$ flow-box theorem supplies coordinates $I\times Y$ in which $v=\partial_t$. Microsupport is invariant under this coordinate change by its $C^1$ test definition. An increasing $C^1$ diffeomorphism from the interval $I$ to $\mathbb R$ changes $v$ by a positive scalar, preserving (I23). We may thus work on $\mathbb R\times Y$ with the inequality $\tau\geq0$.

For the cone $C=(-\infty,0]\subset\mathbb R$, let

\[
q:\mathbb R\times Y\longrightarrow\mathbb R_C\times Y
\]

be the map to the directional topology in the first variable. Its open sets in that variable are the ordinary open sets stable under moving left. Condition (I23) is precisely the cone-cutoff condition, so

\[
K\simeq q^{-1}Rq_*K,
\qquad
\mathcal H^j(K)\simeq q^{-1}A,
\quad A=\mathcal H^j(Rq_*K).
\tag{I24}
\]

The second identity uses exactness of inverse image; it is not an assertion that microsupport always commutes with taking cohomology sheaves. Fully faithful descent gives $q_*q^{-1}A\simeq A$, so a section over this whole flow box corresponds to a section of $A$ on its directional version.

Restrict to the line $\mathbb R\times\{y\}$. Inverse images commute in the square formed by that line and its directional version. Consequently the restricted sheaf is $q_C^{-1}L$ for a sheaf $L$ on $\mathbb R_C$, and the section is the inverse image of a section $\ell$ of $L$. For $s>t$, every directional neighborhood of $s$ also contains $t$: such a neighborhood contains a left ray $(-\infty,s+\delta)$. If the germ $\ell_s$ is zero, it vanishes on one such neighborhood and hence its germ at $t$ is zero. Taking the contrapositive proves that a nonzero germ at $t$ remains nonzero at $s$.

This proves forward invariance as long as the trajectory stays in one flow box. The support of $u$ is closed because the locus of zero germs is open. The same continuation argument as in `SH02-INV-NAGUMO` now extends the conclusion over the whole positive existence interval. $\square$

On any open time interval, a closed forward-invariant subset is empty, the whole interval, or its intersection with a closed ray $[c,\infty)$. The theorem therefore rules out the disappearance of a nonzero germ along positive time; it does not rule out a first appearance.

## SH02-INV-MICROLOCAL-FLOW — Sections between opposite sides of a level set

Let $U\subset T^*X$ be open, let $\phi\in C^2(U;\mathbb R)$, and write

\[
V_+=\{\phi\geq0\},\qquad
V_-=\{\phi\leq0\},\qquad
V_0=\{\phi=0\}.
\tag{I25}
\]

Let $F,G\in D^b(k_X)$ satisfy

\[
\operatorname{SS}(F)\cap U\subset V_+,
\qquad
\operatorname{SS}(G)\cap U\subset V_-.
\tag{I26}
\]

Then for every integer $j$ and section

\[
u\in\Gamma\bigl(U;\mathcal H^j\mu\mathcal Hom(G,F)\bigr),
\]

its support lies in $V_0$ and is a union of positive maximal Hamiltonian trajectories of $H_\phi$ within $U$.

**Proof relative to (I1)–(I2).** Put $K=\mu\mathcal Hom(G,F)|_U$. Support containment gives $\operatorname{supp}(K)\subset V_0$. If $(p,\alpha)\in\operatorname{SS}(K)$, then $p\in V_0$, and (I1), (I7), and (I10) give

\[
\langle\alpha,H_\phi(p)\rangle
=\langle-H\alpha,d\phi_p\rangle\geq0.
\tag{I27}
\]

In using (I7), the two sequences lie in $\operatorname{SS}(F)$ and $\operatorname{SS}(G)$ in exactly that order. They eventually lie in $U$, so only the hypotheses in (I26) are needed. At a critical point, (I27) remains valid and the associated trajectory is constant. Apply `SH02-INV-SECTION-FLOW` to $K$ and $H_\phi$. $\square$

Reversing $F$ and $G$ reverses the normal-cone order and hence the propagation sign. Interchanging $V_+$ and $V_-$ without also reversing the Hamiltonian direction would give a false statement.

## SH02-INV-TWO-ENDPOINTS — A calculation with two outgoing rays

Choose real numbers $a<b$ and a nonzero $k$-module $N$. On $X=\mathbb R$, take

\[
F=N_{(a,b)},\qquad
G=k_{\{a\}}\oplus k_{\{b\}},\qquad
\phi(t,\tau)=(t-a)(b-t).
\tag{I28}
\]

The subscript denotes extension by zero from the indicated locally closed set. The closure of the support of $F$ is $[a,b]$; consequently its microsupport lies over $[a,b]$, where $\phi\geq0$. The microsupport of $G$ lies over the endpoints, where $\phi=0$. Thus (I26) holds.

There is a direct calculation

\[
\mu\mathcal Hom(G,F)
\simeq
N_{\{t=a,\ \tau\leq0\}}[-1]
\oplus
N_{\{t=b,\ \tau\geq0\}}[-1].
\tag{I29}
\]

Here we use the point-support identification $\mu\mathcal Hom(k_{\{c\}},F)\simeq j_{c*}\mu_{\{c\}}F$, where $j_c:T_c^*X\hookrightarrow T^*X$, from `SH02-MH-SUBMANIFOLD` in [the microlocal Hom construction](../../sheaf-proof-readings/SH02-microlocal-hom.html). We also use the specialization/Fourier descriptions from [microlocalization](../../sheaf-proof-readings/SH02-microlocalization.html). These exact identifications are additional dependencies of this worked calculation, not of `SH02-INV-THEOREM`.

To verify (I29), use the oriented normal coordinate $r=t-a$ at the left endpoint. Specialization of $F$ there is $N_{\{r>0\}}$. In the negative-pairing Fourier presentation, a covector $\tau$ has the compactly supported coefficient complex of

\[
\{r>0:r\tau\leq0\}.
\]

This is empty when $\tau>0$ and is the open ray when $\tau\leq0$. More precisely, on the support $r>0$, the kernel inequality is equivalent to $\tau\leq0$, so the kernel is the exterior product on $(0,\infty)\times(-\infty,0]$. Its proper direct image is therefore the constant compact-support complex of the first factor on the closed second factor, extended by zero. The open ray has compactly supported cohomology $N[-1]$, as is seen by compactifying it to an interval and taking the relative complex at both endpoints. This product description verifies the sheaf comparison maps at $\tau=0$ as well as its stalk. At the right endpoint the normal ray is $r=t-b<0$, which reverses the inequality. The two point-supported summands of $G$ are disjoint and Hom is additive for this finite direct sum. This proves (I29), including its shift and endpoints; no flatness of $N$ is required.

At $t=a$, the Hamiltonian field is $-(b-a)\partial_\tau$; at $t=b$, it is $(b-a)\partial_\tau$. A chosen nonzero element of $N$ gives a section of $\mathcal H^1$ on either summand of (I29), or independently on both. Each support is exactly the positive Hamiltonian ray beginning at the corresponding zero covector. Neither ray is invariant under the negative flow. This example also shows why the zero covectors must remain in the statement: they are the initial points of these closed supports.

## SH02-INV-POINT-TANGENT-FAILURE — Why moving both points matters

Here is an explicit microsupport for which replacing $C_p(S,S)$ by $C_p(S)$ in (I15) would be wrong. Take $k\neq0$, coordinates $(x,y)$ on $\mathbb R^2$, and

\[
Z=\{(x,y):-x^4<y\leq x^4\},\qquad F=k_Z.
\tag{I30}
\]

We will calculate its microsupport and the two different cones at the zero covector above the origin. The unequal open and closed edges of this narrowing band determine the sign.

First, for any $C^1$ function $f(x)$ the closed hypograph $A_f=\{y\leq f(x)\}$ has microsupport

\[
\operatorname{SS}(k_{A_f})=
\{(x,y;0,0):y\leq f(x)\}
\cup
\{(x,f(x);-f'(x)\eta,\eta):\eta\leq0\}.
\tag{I31}
\]

To check this formula without a stratification assumption, straighten the boundary by the $C^1$ diffeomorphism $(x,y)\mapsto(x,s=y-f(x))$. For $\{s\leq0\}$, use the cone $C=\mathbb R\times[0,\infty)$. If $O$ is a convex open set, $O\cap\{s\leq0\}$ and $(O+C)\cap\{s\leq0\}$ are simultaneously empty or nonempty convex sets. Their constant-sheaf cohomology and the restriction map are respectively zero or the identity on $k$ in degree zero, by convex acyclicity. The directional section comparison therefore gives $P_Ck_{\{s\leq0\}}\simeq k_{\{s\leq0\}}$. The forward cutoff estimate puts its nonzero covectors among $\xi=0,\eta\leq0$. At the boundary every negative multiple of $ds$ is present: the test function $-s$ has support set $\{s\leq0\}$, and its support-test stalk is $k\neq0$. In the interior the sheaf is constant, and outside it is zero; the elementary support tests give precisely the stated zero section. Transforming the covectors back proves (I31).

Put $A=\{y\leq x^4\}$ and $B=\{y\leq-x^4\}$. Since $B\subset A$ are closed, localization gives

\[
k_Z\longrightarrow k_A\longrightarrow k_B\xrightarrow{+1}.
\tag{I32}
\]

At the origin the two right-hand stalks are $k$ and their map is the identity, so $F_0=0$. Formula (I31) and the triangle estimate nevertheless show that the microsupport fiber there is contained in $\{\xi=0,\eta\leq0\}$. All its nonzero points occur: they are limits of the covectors on either boundary at $x\neq0$, where only one boundary is present. At a point of the lower boundary away from the origin, (I32) identifies $F$ with the open upper-halfspace sheaf. Its nonzero conormals have $\eta\leq0$: the triangle between that open halfspace, the constant sheaf, and the closed lower halfspace gives equality of their nonzero microsupports by applying the triangle estimate in both directions. At an upper boundary point, (I31) applies directly. We obtain the complete closed set

\[
\begin{aligned}
S=\operatorname{SS}(F)
={}&\{(x,y;0,0):|y|\leq x^4\}\\
&\cup\{(x,x^4;-4x^3\eta,\eta):\eta\leq0\}\\
&\cup\{(x,-x^4;4x^3\eta,\eta):\eta\leq0\}.
\end{aligned}
\tag{I33}
\]

Let $p=(0,0;0,0)$. In tangent coordinates $(\dot x,\dot y;\dot\xi,\dot\eta)$, (I33) gives

\[
C_p(S)=
\{(r,0;0,s):r\in\mathbb R,\ s\leq0\}.
\tag{I34}
\]

For the inclusion, if a point of $S$ divided by $h_n\downarrow0$ converges, then $x_n=O(h_n)$ and $\eta_n=O(h_n)$. The bounds $|y_n|\leq x_n^4$ and $|\xi_n|\leq4|x_n|^3|\eta_n|$ force the second and third limiting coordinates to vanish. The final coordinate is nonpositive. Conversely, for prescribed $r$ and $s\leq0$, choose $x_n=h_nr$, $\eta_n=h_ns$ on the upper boundary; their rescaled points converge to the vector in (I34).

Thus $C_p(S)\subset\ker dy$. But $-H(dy)=\partial_\eta$ is not in (I34). The proposed stronger definition using the one-point cone would reject this actual microsupport.

The two-set cone explains the discrepancy concretely. Let $r_n\downarrow0$ and choose two zero covectors of (I33) above $(r_n,r_n^4)$ and $(r_n,-r_n^4)$. Their difference divided by $2r_n^4$ is exactly $\partial_y$. Both points tend to $p$, so

\[
\partial_y\in C_p(S,S),\qquad
C_p(S,S)\not\subset\ker dy.
\tag{I35}
\]

The actual involutivity definition never demands the missing direction for this particular $dy$. Its hypothesis has correctly retained the relative motion of the two boundary branches.

The calculation has a useful uniform version. Replace $x^4$ by $x^{2m}$ for any integer $m\geq1$, and replace $4x^3$ in (I33) by $2m x^{2m-1}$. The same hypograph triangle gives exactly that microsupport. In the fixed-point cone calculation, $|y_n|/h_n=O(h_n^{2m-1})$ and $|\xi_n|/h_n=O(h_n^{2m-1})$, so (I34) is unchanged. The two-set witnesses use the scale $2r_n^{2m}$. This proves the phenomenon for quadratic narrowing as well as the quartic example displayed here, with the same open and closed edge conventions.

## SH02-INV-PROBLEMS — Exercises with complete solutions

**1. Finite time is not a failure of invariance.** On $\mathbb R$, let $v(x)=x^2\partial_x$ and $S=[1,\infty)$. Verify (I12), compute the trajectory starting at $1$, and state exactly what the tangent-field theorem concludes.

*Solution.* At $1$, the tangent cone is $[0,\infty)$ and $v(1)=1$. At every larger point the tangent cone is all of $\mathbb R$. The solution is $x(t)=1/(1-t)$ on its maximal interval $(-\infty,1)$. Its positive portion lies in $S$ for $0\leq t<1$. The theorem gives no point at $t=1$ and makes no assertion of a solution for all positive time.

**2. Rescale a Hamiltonian and check its sign.** Suppose $\phi=0$ on a closed involutive set $S\subset U$ and $h\in C^2(U)$ is positive. Prove that the trajectories of $H_{h\phi}$ and $H_\phi$ in $S$ have the same local orientations. What happens for $h<0$?

*Solution.* The product rule and linearity of $H$ give $H_{h\phi}=hH_\phi+\phi H_h$. The second term vanishes on $S$. A solution $b(t)$ of $H_\phi$ becomes one of $H_{h\phi}$ after solving $dt/ds=h(b(t))$. A positive right side preserves orientation; a negative one reverses it. At a zero of $H_\phi$, both fields vanish and uniqueness fixes the point. A global assertion about the equality of time domains does not follow from this calculation.

**3. A critical level needs an inclusion.** On the symplectic plane with coordinates $(x,\xi)$, let $\phi=x^3$ and $p=(0,0)$. Compute $C_p(V_+,V_-)$ and compare it with $\{w:d\phi_p(w)\geq0\}$.

*Solution.* Here $V_+=\{x\geq0\}$ and $V_-=\{x\leq0\}$. Their scaled differences have nonnegative $x$ coordinate and arbitrary $\xi$ coordinate, and every such vector is realized by linear sequences. Thus $C_p(V_+,V_-)=\{\dot x\geq0\}$. On the other hand $d\phi_p=0$, so its stated halfspace is the whole tangent plane. The inclusion (I7) is strict. Since $H_\phi(p)=0$, the directed propagation theorem at this point concerns only the constant trajectory and remains valid.

**4. Why does an empty cone need a microsupport condition?** Give a sheaf on $\mathbb R$ that vanishes on $t>0$ and has a nonzero stalk at $0$. Identify the covectors that violate (I17).

*Solution.* Take $K=k_{(-\infty,0]}$ with $k\neq0$. Its stalk at zero is $k$. The support test with $f(t)=-t$ is nonzero there, so the negative covectors belong to its microsupport. In dimension one the condition $\tau=0$ excludes all those covectors. Thus the open-cone vanishing hypothesis alone is insufficient, exactly as the proof of `SH02-INV-CONE-VANISHING` requires.

**5. The support of a section and the support of a sheaf.** Let $k=\mathbb Z$, let $K=k_{[0,\infty)}\oplus k_{[2,\infty)}$, and let $v=\partial_t$. Describe the supports of all global sections of $\mathcal H^0(K)$.

*Solution.* A section is a pair $(m,n)\in\mathbb Z^2$, constant on the two closed rays. Its support is empty if both entries vanish, $[0,\infty)$ if $m\neq0$, and $[2,\infty)$ if $m=0$ and $n\neq0$. The microsupport is contained in $\tau\geq0$ by the halfspace calculation. Every listed support is forward invariant, and the second nonempty possibility is strictly smaller than the support $[0,\infty)$ of the whole sheaf. Thus the section theorem contains information that cannot be recovered by replacing $u$ with $K$ in its conclusion.

## SH02-INV-RESEARCH — What the argument suggests next

The central mechanism is a compatibility between three operations: taking relative secants of a closed set, transporting those secants by the Hamiltonian identification, and continuing a sheaf section through an open cone. This gives a useful route for studying singular examples: compute the two-set cone before choosing any stratification, then test which Hamiltonians annihilate it. The quartic-band calculation shows that fixed-point tangents alone can discard the interaction one needs.

A second route is to compare the supports of different cohomology sections of the same microlocal Hom object. The directed theorem imposes an order along each characteristic even when the ambient microsupport is invariant in both directions. The two-endpoint calculation gives an elementary model in which these section supports have genuine initial points.

The involutivity of the micro-support and the propagation of microlocal sections are theorems of Kashiwara and Schapira; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §3.2 and §6.4. This exposition uses a distance comparison for closed-set invariance, an explicit shrinking cone cap for stalk vanishing, and worked calculations.
