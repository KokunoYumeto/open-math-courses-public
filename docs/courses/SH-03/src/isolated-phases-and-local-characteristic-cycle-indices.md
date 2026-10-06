# Isolated phases and local characteristic-cycle indices

A differential graph can meet a characteristic cycle at a singular or degenerate point. The local number still has a cohomological meaning: it is the Euler characteristic of the sheaf's closed half-space test. We will prove this without replacing the isolated intersection by a transverse one. The proof converts that local test into a compact global calculation while controlling every covector created at the edge of a coordinate ball.

Use Differential sections and proper-below Euler indices for the normalized supported intersection and compact-cohomology formula. Limiting cotangent sums and characteristic inverse images proves the full limiting-sum isotropy, including unbounded cancellation. Isotropic cotangent transport and discrete critical values supplies the proper critical-value argument. Small balls, central fibres and supported cohomology proves the actual small-ball restriction to a stalk. Perfect operations and finite microlocal coefficients supplies constructible internal Hom and open cutoffs.

For the signed ordinary boundary estimate and supported finite-band Morse map, use the exact proofs in Microsupport operations: open boundaries and cohomology between two levels. The curve-selection and singular one-form rules are the explicitly stated inputs and proved consequences in Subanalytic sets and limiting tangent directions. The underlying subanalytic foundation proofs remain programme obligations; this lesson does not certify their transitive closure.

Throughout, \(X\) is a finite-dimensional real analytic manifold, Hausdorff and countable at infinity, \(k\) is a field of characteristic zero, and \(F\in D^b_{\mathbb R\text{-}c}(k_X)\) has perfect stalks. Complexes are globally bounded. The closed support is \(\pi\operatorname{SS}(F)\), which can contain a point where the ordinary stalk vanishes. All cotangent conicity uses positive scalars.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## The local number and the closed test

Let \(x_0\in X\), let \(\varphi\) be real analytic near \(x_0\), and put

\[
\sigma_\varphi(x)=(x;d\varphi_x),\qquad
L_\varphi=\sigma_\varphi(X),\qquad
p_0=\sigma_\varphi(x_0).
\qquad\text{(1)}
\]

After restricting to a neighborhood of \(x_0\), assume

\[
L_\varphi\cap\operatorname{SS}(F)\subset\{p_0\}.
\qquad\text{(2)}
\]

The intersection can be empty. Neither \(p_0\neq0\), a smooth microsupport, a nondegenerate Hessian nor transversality is required. Define the local test complex

\[
J_{\varphi,x_0}(F)=
\bigl(R\Gamma_{\{\varphi\geq\varphi(x_0)\}}F\bigr)_{x_0}.
\qquad\text{(3)}
\]

This is sheaf cohomology with a closed support condition, followed by the ordinary stalk. It is not the ordinary stalk of \(F\), and it is not in general the ambient point costalk.

Recall how the right-hand side below is normalized. The graph section has its canonical supported unit with relative orientation coefficients. Cup it, in that order, with \(CC(F)\); its support is \(L_\varphi\cap\operatorname{SS}(F)\). Use the section comparison to the base dualizing complex, restrict to the isolated base support \(\{x_0\}\), and apply the point trace. Denote this number by
\(\#([\sigma_\varphi]\cap CC(F))_{p_0}\). An empty support gives zero. The subscript records localization of the supported class, rather than a signed count assumed to exist only for transverse smooth manifolds.

**Local index theorem.** Under (2), \(J_{\varphi,x_0}(F)\) is a bounded finite-dimensional complex and

\[
\chi\bigl(J_{\varphi,x_0}(F)\bigr)
=\#\bigl([\sigma_\varphi]\cap CC(F)\bigr)_{p_0}.
\qquad\text{(4)}
\]

Finiteness is already justified independently of the equality: the closed analytic inequality defines a subanalytic set \(Z\), and
\(R\Gamma_ZF=R\mathcal Hom(k_Z,F)\) is bounded constructible with perfect stalks by the internal-Hom theorem. If \(p_0\notin\operatorname{SS}(F)\), the defining microsupport test makes (3) zero, while the intersection support is empty. In dimension zero the assertion is the normalized point trace of the finite coefficient complex. We therefore prove the remaining case in a positive-dimensional coordinate chart.

Subtract \(\varphi(x_0)\), choose coordinates with \(x_0=0\), and write

\[
\varphi(0)=0,\qquad
\rho(x)=|x|^2,\qquad
A=\operatorname{SS}(F).
\qquad\text{(5)}
\]

Choose a closed coordinate ball wholly contained in the chart. All geometric carriers used in a critical-value argument will first be restricted over that closed ball, so that the relevant base properness is proved.

## Two radial exclusions on a punctured ball

We need a carrier containing both signs of the conormal to the zero phase, even if that level is singular at zero. Put

\[
Z_0=\{\varphi=0\},\qquad
B=\operatorname{SS}(k_{Z_0})\cup
\operatorname{SS}(k_{Z_0})^a.
\qquad\text{(6)}
\]

Here \(a(x;\xi)=(x;-\xi)\). The sheaf \(k_{Z_0}\) is constructible with perfect stalks. Thus \(B\) is closed, positive-conic, subanalytic and isotropic. Its base lies in \(Z_0\). At a regular point of the level set, the closed-submanifold microsupport calculation includes every \(\lambda\,d\varphi_x\), \(\lambda\in\mathbb R\). At a critical point these covectors are zero, and zero belongs to the microsupport over \(Z_0\). Therefore

\[
(x;\lambda\,d\varphi_x)\in B
\quad\text{if }\varphi(x)=0,\quad \lambda\in\mathbb R.
\qquad\text{(7)}
\]

The full limiting-sum theorem makes \(A\widehat+B\) a closed conic subanalytic isotropic set. This is available even if the same-base sum is not closed.

Apply the discrete-critical-value theorem to \(\rho\), first on \(A\), then on \(A\widehat+B\), restricting both carriers over the fixed closed coordinate ball. Their base projections are compact: a closed conic carrier contains the zero covector above every point in its projection, making that projection closed; it now lies in the compact ball. Hence \(\rho\) is proper on each projection. The selected radial values form closed locally finite subsets of \(\mathbb R\). Since \(\rho\geq0\), some \(r_0>0\) satisfies

\[
\begin{aligned}
A\cap L_\rho\cap\{0<|x|\leq r_0\}&=\varnothing,\\
(A\widehat+B)\cap L_\rho
\cap\{0<|x|\leq r_0\}&=\varnothing.
\end{aligned}
\qquad\text{(8)}
\]

We have not declared an unrestricted cotangent projection proper. The compact base restriction is what permits the theorem. The second exclusion will be used precisely at zero phase on the boundary of the eventual ball.

## Positive phase excludes every nonnegative radial multiplier

There is \(r_1>0\) such that

\[
0<|x|\leq r_1,\quad \varphi(x)>0,\quad c\geq0
\quad\Longrightarrow\quad
(x;c\,d\rho_x+d\varphi_x)\notin A.
\qquad\text{(9)}
\]

The multiplier \(c\) has no prescribed upper bound. A proof that treated only a bounded interval of multipliers would not justify the later ordinary-boundary estimate.

**Proof.** Suppose (9) fails at arbitrarily small radii. Normalize each offending pair of coefficients:

\[
u=\frac{c}{\sqrt{1+c^2}},\qquad
v=\frac1{\sqrt{1+c^2}}.
\qquad\text{(10)}
\]

Positive conicity gives
\((x;u\,d\rho_x+v\,d\varphi_x)\in A\).
Consider the subanalytic set

\[
\mathcal E=
\left\{(x,u,v):
\begin{array}{l}
x\neq0,\ \varphi(x)>0,\ u\geq0,\ v>0,\\
u^2+v^2=1,\ (x;u\,d\rho_x+v\,d\varphi_x)\in A
\end{array}\right\}.
\qquad\text{(11)}
\]

Membership is an analytic inverse-image condition on \(A\). The coefficient circle is compact. A subsequence of offending points therefore approaches a point \((0,u_0,v_0)\) in the closure of \(\mathcal E\). Its limit may have \(v_0=0\); that is how unbounded original multipliers are retained.

Curve selection supplies an analytic arc \((x(t),u(t),v(t))\) through that limit, lying in \(\mathcal E\) for small \(t>0\). The cotangent arc
\[
q(t)=\bigl(x(t);u(t)d\rho_{x(t)}+v(t)d\varphi_{x(t)}\bigr)
\]
lies in \(A\). Isotropy and the singular one-form pullback rule make its canonical one-form zero along the arc, including an arc contained in the singular locus. Consequently

\[
u(t)\frac{d}{dt}\rho(x(t))
+v(t)\frac{d}{dt}\varphi(x(t))=0.
\qquad\text{(12)}
\]

Both scalar functions are analytic, vanish at zero, and are strictly positive for \(t>0\). Their first nonzero Taylor terms have positive coefficients and positive integer orders. Both derivatives are therefore strictly positive for all sufficiently small positive \(t\). Since \(u(t)\geq0\) and \(v(t)>0\), the left side of (12) is strictly positive. This contradiction proves (9). \(\square\)

The normalization proved the required compactness before selecting an arc. It did not discard sequences with \(c\to+\infty\), nor assume that the selected covector lies in the regular part of \(A\).

## Extend an actual small-ball test by ordinary direct image

Set \(H=R\Gamma_{\{\varphi\geq0\}}F\). Constructible internal Hom makes \(H\) constructible. The small-ball theorem, with its actual restriction map, permits a radius
\(0<r<\min(r_0,r_1)\) such that

\[
R\Gamma(B_r;H)\xrightarrow{\sim}H_0
=J_{\varphi,0}(F).
\qquad\text{(13)}
\]

The local version of that theorem first cuts off the coefficient complex in a larger closed ball, so no global properness of the coordinate chart is needed.

For \(j:B_r\hookrightarrow X\), use the ordinary extension

\[
F_r=Rj_*j^{-1}F
\simeq R\mathcal Hom(k_{B_r},F).
\qquad\text{(14)}
\]

It is bounded constructible with perfect stalks. Its closed support \(D_r\) lies in \(\overline B_r\), hence is compact. Open internal-Hom adjunction, followed by direct-image composition, identifies

\[
\begin{aligned}
R\Gamma_{\{\varphi\geq0\}}(X;F_r)
&=R\Gamma\bigl(X;R\mathcal Hom(k_{\{\varphi\geq0\}},Rj_*j^{-1}F)\bigr)\\
&\simeq R\Gamma\bigl(B_r;
 R\mathcal Hom(k_{\{\varphi\geq0\}\cap B_r},j^{-1}F)\bigr)\\
&=R\Gamma(B_r;H).
\end{aligned}
\qquad\text{(15)}
\]

These are the adjunction comparisons for this closed test. Together with (13), they identify the supported ambient complex with the local test complex.

At a boundary point \(|x|=r\), \(d\rho_x\neq0\). The first exclusion in (8) and positive conicity exclude the positive ray through \(d\rho_x\) from \(A_x\). The ordinary open-boundary theorem thus gives

\[
\operatorname{SS}(F_r)_x
\subset A_x+\mathbb R_{\leq0}\,d\rho_x
\quad (|x|=r).
\qquad\text{(16)}
\]

On the interior \(F_r=F\), and outside the closed ball it is zero. The sign in (16) belongs to \(Rj_*\); changing the extension changes that sign.

Let \(C=T^*_{\partial B_r}X\), the full conormal of the analytic sphere. It is closed, conic, subanalytic and isotropic. Define

\[
\Gamma=
\bigl(A\cup(A\widehat+C)\bigr)
\cap\pi^{-1}\overline B_r.
\qquad\text{(17)}
\]

The finite union and subanalytic subset rules preserve isotropy; the limiting-sum theorem proves the needed closedness and subanalyticity. The ordinary sums in (16) lie in \(A\widehat+C\), so
\(\operatorname{SS}(F_r)\subset\Gamma\).
The base projection of \(\Gamma\) is compact, exactly as in the argument for (8). Apply the discrete-critical-value theorem to \(\varphi\) and \(\Gamma\). Choose \(\epsilon>0\) with

\[
\Gamma\cap L_\varphi\cap
\{0<|\varphi|\leq\epsilon\}=\varnothing.
\qquad\text{(18)}
\]

Zero is allowed as a selected value. The two-sided gap will control the negative phase band and the compact support comparison.

## A supported Morse map becomes compact cohomology

Put \(U=\{\varphi>-\epsilon\}\), and apply the supported finite-band Morse theorem to \(\psi=-\varphi\) and \(F_r\). Properness on support holds because \(D_r\) is compact. For every \(0<t<\epsilon\), the changing band is
\[
0<\psi\leq t,\qquad\text{equivalently }-t\leq\varphi<0.
\]
The required negative covector is
\(-d\psi=d\varphi\). It is excluded from \(\operatorname{SS}(F_r)\) by (18). The actual inclusion-of-supports map is therefore an isomorphism

\[
R\Gamma_{\{\varphi\geq0\}}(X;F_r)
\xrightarrow{\sim}
R\Gamma_{\{\varphi\geq-t\}}(X;F_r).
\qquad\text{(19)}
\]

To pass to compact support in \(U\), restrict the support family to \(D_r\). The sets
\[
K_t=D_r\cap\{\varphi\geq-t\},\qquad 0<t<\epsilon,
\]
are compact and lie in \(U\). They are cofinal for compact coefficient supports in \(U\): a compact subset of \(D_r\cap U\) has a minimum phase strictly greater than \(-\epsilon\), and is contained in some \(K_t\). Exact filtered support-family colimits for bounded complexes now give

\[
R\Gamma_{\{\varphi\geq0\}}(X;F_r)
\xrightarrow{\sim}R\Gamma_c(U;F_r|_U).
\qquad\text{(20)}
\]

The first object maps to the support-family colimit through (19); all those arrows are already isomorphisms. This explains the actual comparison in (20). No equality between ordinary cohomology and compact cohomology on an arbitrary noncompact open set was used.

The compact Euler index theorem applies on \(U\) to the analytic function \(\psi=-\varphi:U\to(-\infty,\epsilon)\). Every closed support sublevel \(D_r\cap\{\psi\leq s\}\), \(s<\epsilon\), is compact. Moreover
\[
L_\psi\cap\operatorname{SS}(F_r|_U)^a
\quad\text{corresponds under the antipode to}\quad
L_\varphi\cap\operatorname{SS}(F_r|_U).
\]
The latter is compact: by (18) it has no points with \(-\epsilon<\varphi<0\), so it is the closed graph intersection over the compact set \(D_r\cap\{\varphi\geq0\}\). Thus both hypotheses of that theorem are satisfied. It yields

\[
\chi_c(U;F_r|_U)
=\#\bigl([\sigma_\varphi]\cap CC(F_r|_U)\bigr).
\qquad\text{(21)}
\]

The positive section on the right follows from \(-\psi=\varphi\). No dimension sign is appended to the antipodal comparison.

## Exclude boundary intersections in all three phase regions

Inside \(B_r\), (2) leaves at most \(p_0\). We prove that there is no graph intersection over \(\partial B_r\cap U\).

If \(-\epsilon<\varphi(x)<0\), (18) excludes it directly.

If \(\varphi(x)>0\), membership of \(d\varphi_x\) in the right side of (16) would give

\[
d\varphi_x=p-c\,d\rho_x,\qquad
p\in A_x,\quad c\geq0.
\qquad\text{(22)}
\]

Hence \(p=d\varphi_x+c\,d\rho_x\), contradicting (9).

Finally suppose \(\varphi(x)=0\). In (22), \(c=0\) would contradict the isolated-intersection hypothesis, since \(x\neq0\). If \(c>0\), then (7) and positive conicity give

\[
d\rho_x=c^{-1}p-c^{-1}d\varphi_x
\in A_x+B_x
\subset (A\widehat+B)_x.
\qquad\text{(23)}
\]

This contradicts the second exclusion in (8). The zero-phase argument needs the negative phase multiple \(-c^{-1}d\varphi_x\). The symmetric carrier in (6) supplies that exact covector. A graph of \(d\varphi\) alone would not supply all those multiples.

We have proved

\[
L_\varphi\cap\operatorname{SS}(F_r|_U)\subset\{p_0\},
\qquad\text{(24)}
\]

with no new boundary contribution. Near zero, ordinary restriction identifies \(F_r|_U\) with \(F\); the characteristic cycles and the supported section units consequently agree there. The ordered cup, the section-to-base comparison, localization to \(\{0\}\), and the point trace identify (21) with the local number in (4). Taking Euler characteristics in (13), (15), (20) and (21) proves (4). \(\square\)

The compact computation is a device for reading the original local supported class. The radial boundary has been checked before forgetting its support, so none of its possible contributions is hidden in an Euler cancellation.

## A transverse conormal intersection reads the negative Hessian

Let \(Y\subset X\) be a closed smooth submanifold for which \(k_Y\) is \(\mathbb R\)-constructible; a closed real analytic submanifold is one instance. Let \(x_0\in Y\), with \(d\varphi_{x_0}\in T_Y^*X\), and suppose the graph of \(d\varphi\) and the conormal intersect transversely there.

In coordinates tangent and normal to \(Y\), their common tangent vectors are exactly the vectors in
\(\ker\operatorname{Hess}_{x_0}(\varphi|_Y)\).
Transversality therefore means that this restricted Hessian is nondegenerate. Let \(q\) be its number of negative eigenvalues. The intersection is locally isolated.

The actual conormal support calculation in Pure and simple sheaves from directional tests uses Morse coordinates
\(\varphi|_Y-\varphi(x_0)=|u|^2-|v|^2\), with \(\dim v=q\).
The closed-test triangle compares constants on a small ball in \(Y\) with constants on its negative-phase part. For \(q=0\) that part is empty. For \(q>0\) it retracts to \(S^{q-1}\), and the restriction from constants is the augmentation. Its derived fibre is the negative-direction orientation line in degree \(q\), locally identified with \(k[-q]\). Thus (4) gives

\[
\#\bigl([\sigma_\varphi]\cap[T_Y^*X]\bigr)_{p_0}
=(-1)^q.
\qquad\text{(25)}
\]

The conormal fundamental cycle here has the characteristic-cycle normalization of the earlier lessons. There is no independent choice of an extra ambient dimension sign. Finite families of transverse pure intersections, their ordered inertia degrees, and the global Morse inequalities will use this local theorem in the next step.

## Examples and exercises with solutions

### A degenerate phase can have local number zero, one or minus one

*Difficulty: Introductory.*

Take \(X=\mathbb R\), \(F=k_X\), \(x_0=0\), and \(\varphi(t)=a\,t^m\), with \(a\neq0\) and integer \(m\geq2\). Compute the test complex and local number. Explain why the calculation for \(m\geq3\) is not a transverse Hessian calculation.

**Solution.** The microsupport is the zero section. Its intersection with \(d\varphi=am\,t^{m-1}dt\) is exactly the zero covector at zero. The local test triangle is the fibre of the restriction from \(k\) on a small interval to cohomology of its negative-phase part. If \(m\) is odd, that part is a single half-interval. The restriction \(k\to k\) is the identity, so the fibre is zero and the local number is zero.

If \(m\) is even and \(a>0\), there is no negative-phase part. The test complex is \(k\), giving number \(1\). If \(m\) is even and \(a<0\), the negative-phase part has two components. The restriction is the diagonal \(k\to k\oplus k\); its fibre is \(k[-1]\), giving number \(-1\). In the last case the closed test is supported only at zero and agrees with the line's point costalk. For \(m\geq3\), the Hessian at zero vanishes. These conclusions follow from the actual closed test and the isolated local index theorem, including its degenerate and empty-number cases.

### Cubic tests distinguish open and closed rays

*Difficulty: Intermediate.*

Let \(A=k_{[0,\infty)}\) and \(B=k_{(0,\infty)}\) on \(\mathbb R\). At zero compute the local test complexes and numbers for \(\varphi=t^3\) and \(\varphi=-t^3\).

**Solution.** Both graphs meet the full microsupport only at the zero covector over zero: away from the endpoint, the only supported covectors are zero and \(d\varphi\neq0\). At the endpoint \(d\varphi=0\). The zero covector remains in the closed microsupport of \(B\) even though \(B_0=0\).

For \(t^3\), the closed test side is \(t\geq0\). The complementary negative interval has no coefficients for either sheaf. The support triangles therefore give \(J(A)=k\) and \(J(B)=0\). For \(-t^3\), the complementary positive interval has cohomology \(k\). The closed-ray restriction \(A_0=k\to k\) is the identity, giving \(J(A)=0\). The open ray has restriction \(B_0=0\to k\), whose derived fibre is \(k[-1]\). Hence the complete table is

| Sheaf | Cubic positive test | Local number | Cubic negative test | Local number |
|---|---|---:|---|---:|
| \(k_{[0,\infty)}\) | \(k\) | \(1\) | \(0\) | \(0\) |
| \(k_{(0,\infty)}\) | \(0\) | \(0\) | \(k[-1]\) | \(-1\) |

The table uses the full microsupport, the ordinary stalk and the actual complementary restriction. Replacing the closed support by the nonzero-stalk locus would remove the open-ray endpoint incorrectly.

### A singular crossing retains its vertex correction

*Difficulty: Advanced.*

In \(\mathbb R^2\), let \(C\) be the union of the coordinate axes, let \(F=k_C\), and take \(\varphi(x,y)=x^2-y^2\). Compute the local number at the origin directly from the supported test, and verify it through cycle additivity.

**Solution.** On the punctured horizontal axis, \(F\) is the constant sheaf and its microsupport is the horizontal-axis conormal. The differential \((2x,-2y)\) belongs to that conormal only when \(x=0\). On the punctured vertical axis, the analogous condition forces \(y=0\). Off \(C\) the sheaf vanishes locally. Thus the graph has just the isolated zero-covector intersection at the origin, where the microsupport need not be smooth.

The stalk \(F_0\) is \(k\). In the negative phase the support consists of the two punctured vertical arms. Their cohomology is \(k\oplus k\), and restriction sends a local constant \(v\) to \((v,v)\). The fibre is \(k[-1]\), so the local number is \(-1\).

Write \(L_x,L_y\) for the two axes. The sequence
\[
0\longrightarrow k_C\longrightarrow
k_{L_x}\oplus k_{L_y}
\xrightarrow{(a,b)\mapsto a(0)-b(0)}k_{\{0\}}
\longrightarrow0
\qquad\text{(26)}
\]
is exact on every stalk: away from the origin it is the identity on the relevant axis, and at the origin it is the diagonal kernel of the difference map. Additivity gives
\(CC(k_C)=CC(k_{L_x})+CC(k_{L_y})-CC(k_{\{0\}})\).
The restricted Hessian on \(L_x\) has \(q=0\), giving number \(1\); on \(L_y\) it has \(q=1\), giving \(-1\). The point sheaf has test \(k\) for every phase taking value zero there, so its number is \(1\). The sum \(1-1-1=-1\) agrees with the supported calculation. Omitting the vertex term would give the wrong answer.

### A zero local Euler number need not be a zero local test

*Difficulty: Intermediate.*

Let \(P=k^2\oplus k^2[1]\), \(F=P_{\mathbb R}\), and \(\varphi=-t^4\). Compute the local test and characteristic-cycle number at zero.

**Solution.** The full microsupport is the zero section, and the graph of \(-4t^3dt\) has just the isolated intersection at zero. The negative-phase complement is the punctured interval. Its coefficient complex is \(P\oplus P\), and the map from the stalk \(P\) is the diagonal. The split difference sequence of whole complexes makes its derived fibre \(P[-1]\). It has \(k^2\) in cohomological degrees zero and one, and is nonzero.

Its Euler characteristic is \(2-2=0\). Likewise \(CC(F)=\chi(P)[T^*_{\mathbb R}\mathbb R]=0\) by finite coefficient additivity, so its local intersection number is zero. The vanishing is finite graded cancellation. It gives no reason to remove the zero section from the full microsupport or to declare the supported test acyclic.

### Extension by zero creates two extra boundary tests

*Difficulty: Advanced.*

Let \(F=k_{\mathbb R}\), \(B=(-r,r)\), \(r>0\), and \(\varphi=t^2\). Compare \(Rj_*k_B\) with \(j_!k_B\), where \(j:B\hookrightarrow\mathbb R\). Compute all graph-test numbers and the compact Euler indices.

**Solution.** Ordinary interval cohomology at the two endpoints gives
\(Rj_*k_B=k_{[-r,r]}\).
At \(r\), its microsupport normal is a nonpositive multiple of \(dt\); at \(-r\), it is a nonnegative multiple of \(dt\). The graph differential is respectively \(2r\,dt\) and \(-2r\,dt\), so neither endpoint contributes. The only graph intersection is the minimum at zero, with supported test \(k\) and number \(1\). Its compact Euler characteristic is also \(1\).

For \(j_!k_B=k_{(-r,r)}\), the endpoint normals reverse. Both graph covectors now occur. At either endpoint the ordinary stalk is zero, while the complementary lower-phase interval inside \(B\) has cohomology \(k\). The support triangle is the fibre of \(0\to k\), namely \(k[-1]\), giving number \(-1\) at each endpoint. The interior minimum still contributes \(1\). The sum is \(1-1-1=-1\), equal to \(\chi_c(B;k)\).

This is why (14) and the negative coefficient in (16) belong to the proof. The exceptional extension has its own valid compact index, with additional boundary contributions; substituting it would not identify that global number with the original local test.

### A negative phase gap removes an artificial endpoint contribution

*Difficulty: Advanced.*

Take \(F=k_{\mathbb R}\), \(\varphi=t\), \(x_0=0\), and \(F_r=k_{[-r,r]}\). Compare the compact index on \(U_\epsilon=\{t>-\epsilon\}\) when \(0<\epsilon<r\) and when \(\epsilon>r\). Relate the difference to the phase gap.

**Solution.** For the original sheaf the graph of \(dt\) misses the zero-section microsupport. The local support triangle at zero compares \(k\) with \(k\) on a negative interval by the identity, so the local test and number vanish.

For \(F_r\), the graph meets the positive conormal at the left endpoint \(-r\), and misses the negative conormal at the right endpoint \(r\). The left endpoint's test is \(k\), since the closed test side \(t\geq-r\) locally contains its coefficient support. Its phase value is \(-r\).

If \(0<\epsilon<r\), the coefficient support in \(U_\epsilon\) is \((-\epsilon,r]\). Its compact cohomology vanishes: in a slightly larger compact interval, the support triangle removes the left endpoint, and restriction of constants to that endpoint is the identity. The graph has no remaining intersection, and the compact index is zero as required.

If \(\epsilon>r\), the entire closed interval lies in \(U_\epsilon\). Compact cohomology is \(k\), and the artificial left-endpoint intersection contributes \(1\). The asserted phase gap now fails, because the selected value \(-r\) lies in \((-\epsilon,0)\). This larger choice does not satisfy the hypothesis of (19). The discrepancy verifies the role of the negative-band exclusion rather than contradicting the local theorem.

## References and the next step

The index of an isolated analytic phase and the sign of a transverse conormal belong to the local index theory of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §4. The argument here keeps the programme's proofs, the actual cutoff and support maps, the compactified multiplier selection, the symmetric zero-phase carrier and all three boundary cases.

For related complex-analytic developments, David B. Massey's [A Little Microlocal Morse Theory](https://arxiv.org/abs/math/0006185v2), version 2, 18 January 2001, studies isolated vanishing-cycle support and cohomological decompositions with principal-ideal-domain coefficients. Section 5 includes a perturbation and radial-boundary argument. This is further scholarly context; the real-phase proof above uses the exact programme comparisons already named.

The next step applies this local theorem to a finite set of transverse pure intersections. Their exact ordered three-plane inertia shifts determine the local multiplicities, and the finite sheaf-theoretic Morse filtration supplies the global Euler sum and stronger inequalities. Orientation-valued conormal and graph conventions will be checked together with that calculation.
