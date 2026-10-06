# Localizing symbols on moving ellipsoids

This companion retains AN03-U001 Sections 1–4 and 7, with the exact compact comparison used in Section 7. The smooth replacement-metric construction and unrelated exercises are not selected.

This is a separate modified selection from the earlier AN-03 programme.
Original principal author and publisher: AN-03 course-writing task /
AN-03 local course project. Copyright © 2026 AN-03 course project
contributors. Earlier modification: AN-03 course-writing task and
OpenAI Codex. Selection and the identified connecting proofs: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under
the GNU Free Documentation License, Version 1.2 only, with no Invariant
Sections, no Front-Cover Texts and no Back-Cover Texts. The
[licence](operator-notices/COPYING), [title information](operator-notices/TITLE_PAGE.md),
[history](operator-notices/HISTORY.md) and [rights notice](operator-notices/RIGHTS.md)
accompany it.

## 0. Exact earlier inputs

The [measure companion, M0–M8](measure-and-l2.md) supplies the declared
choice principle, rational enumeration, completed measure and convergence
theorems. The [Fourier companion, L0–L3](fourier-l2.md) supplies the
full \(L^2\) extension and distributional compatibility. The exact
[U001 Schwartz and spectral proofs, Q3–Q5](../../20261004-free-stationary-phase/quadratic-stationary-phase.md#q3-schwartz-estimates-and-the-signs-in-the-fourier-rules)
supply all finite-dimensional Fourier and spectral steps.
The finite-dimensional compactness, algebra and differential inputs are
the exact earlier proofs named in that companion's F0 contract.
Smooth cutoffs are [U001 P14.3](../../20261004-free-stationary-phase/exponential-prerequisite-completions.md#p14-3-exponential-decay-and-the-flat-cutoff-function).
Compact and affine substitution, with every determinant, is
[U001 P21.3–P21.4](../../20261004-free-stationary-phase/change-of-variables-prerequisite-completions.md#p21-3-the-full-compact-jordan-change-of-variables-theorem).
M8 proves compatibility of these integrals with the Lebesgue integrals.

The [quadratic-form companion, Sections 1–2](quadratic-multiplier-foundations.md#1-positive-forms-and-coordinate-maps)
proves the ellipsoid norm and completed-measure volume facts used below.
M0 supplies the maximality principle and the countable rational selection.
## 1. Data and symbol seminorms

Let \(E\) be a real vector space of finite dimension \(d\geq1\). At every \(X\in E\), let \(g_X\) be a positive-definite quadratic form on \(E\). Write

\[
B_X(t)=\{Y:g_X(Y-X)<t^2\}.
\]

We assume that there are \(r_*>0\) and \(C_g\geq1\) such that

\[
g_X(Y-X)\leq r_*^2
\quad\Longrightarrow\quad
C_g^{-1}g_X(T)\leq g_Y(T)\leq C_g g_X(T)
\quad(T\in E).                                      \tag{1}
\]

This is slow variation. A positive function \(m:E\to(0,\infty)\) is an admissible weight for this *local* discussion if, after possibly decreasing \(r_*\),

\[
g_X(Y-X)\leq r_*^2
\quad\Longrightarrow\quad
C_m^{-1}m(X)\leq m(Y)\leq C_m m(X)                 \tag{2}
\]

for some \(C_m\geq1\). In this lesson, “locally admissible” means exactly (2). We impose neither global temperateness nor an uncertainty inequality. Neither continuity of \(X\mapsto g_X\) nor continuity of \(m\) is required by (1)–(2).

For a smooth complex-valued function \(a\), define

\[
|a|_{k,g}(X)=
\sup_{g_X(T_j)\leq1}
\left|D^k a(X)[T_1,\ldots,T_k]\right|,
\qquad
p_k(a;m,g)=\sup_X\frac{|a|_{k,g}(X)}{m(X)}.       \tag{3}
\]

For \(k=0\), the numerator is \(|a(X)|\). The symbol space \(S(m,g)\) consists of the smooth functions for which every \(p_k\) is finite. We also write \(p_{\leq k}=\max_{j\leq k}p_j\). These norms of multilinear derivatives avoid making the definition depend on a preferred basis. Replacing them with the maximum of derivatives in a \(g_X\)-orthonormal basis gives equivalent seminorms, with constants depending only on \(d,k\).

For clarity about conventions, the usual one-sided slow-variation assumption is sufficient. Suppose \(g_X(Y-X)\leq c\) implies \(g_Y\leq Cg_X\). If \(g_X(Y-X)\leq c/C\), then \(g_Y(X-Y)\leq c\); applying the same assumption with \(X,Y\) exchanged gives \(g_X\leq Cg_Y\). Thus (1) results by shrinking the radius. We do not add a stronger regularity assumption by using its symmetric form.

## 2. A locally finite cover of moving ellipsoids

**Theorem 2.1 (Ellipsoid cover).** Choose any

\[
0<r<\frac{r_*}{4(1+C_g)},\qquad R_1=(1+C_g)r,
\qquad R_2=2R_1.
\]

There is an at most countable family of centers \(X_\nu\) such that:

1. the balls \(B_{X_\nu}(r)\) are pairwise disjoint;
2. the balls \(B_{X_\nu}(R_1)\) cover \(E\);
3. the larger balls \(B_{X_\nu}(R_2)\) form a locally finite family;
4. no point belongs to more than

\[
N=\left\lceil C_g^d\left(1+R_2/r\right)^d\right\rceil               \tag{4}
\]

of those larger balls.

The particular numerical radii are only one convenient choice. All constants are independent of the centers and of the eccentricities of the ellipsoids.

**Proof.** Order the collections of pairwise disjoint balls \(B_X(r)\) by inclusion. A chain has its union as an upper bound, since any two balls in the union lie together in one member of the chain. The maximality principle gives a maximal collection. Every ball in it is a nonempty Euclidean open set. Choose a rational-coordinate point in each ball, in any fixed linear coordinates; disjointness makes these chosen points distinct. The collection is at most countable.

Maximality means that \(B_X(r)\) meets a selected ball \(B_{X_\nu}(r)\) for every \(X\). Let \(Y\) belong to the intersection. Applying (1) with centers \(X\) and \(X_\nu\) at \(Y\) gives

\[
g_{X_\nu}\leq C_g g_Y\leq C_g^2g_X.
\]

The triangle inequality in the norm \(g_{X_\nu}^{1/2}\) therefore gives

\[
g_{X_\nu}(X-X_\nu)^{1/2}
\leq g_{X_\nu}(X-Y)^{1/2}+g_{X_\nu}(Y-X_\nu)^{1/2}
<(C_g+1)r=R_1.
\]

This proves the covering assertion.

Fix \(X\), and consider centers with \(X\in B_{X_\nu}(R_2)\). Since \(R_2<r_*\), (1) yields

\[
C_g^{-1}g_X\leq g_{X_\nu}\leq C_g g_X.
\]

Consequently the disjoint smaller balls \(B_{X_\nu}(r)\) all lie in the \(g_X\)-ball centered at \(X\) of radius \(\sqrt{C_g}(R_2+r)\). Each has volume at least \(C_g^{-d/2}r^d v_X\), where \(v_X\) is the volume of the unit ball of \(g_X\). The containing ball has volume \(C_g^{d/2}(R_2+r)^d v_X\). Dividing these two quantities bounds every finite subcollection by the expression in (4), and hence bounds the entire collection. This proves the multiplicity assertion without any global comparison to the Euclidean metric.

For local finiteness we need more than a pointwise multiplicity estimate. Choose \(0<\delta<r_*\), and consider all larger balls meeting \(B_X(\delta)\). At an intersection point \(Y\), (1) first compares \(g_Y\) with \(g_X\), then with \(g_{X_\nu}\). Thus

\[
C_g^{-2}g_X\leq g_{X_\nu}\leq C_g^2g_X.
\]

The centers lie within \(g_X\)-distance \(\delta+C_gR_2\) of \(X\). Their disjoint smaller balls lie in the fixed ball of radius \(\delta+C_g(R_2+r)\), and each has volume at least \(C_g^{-d}r^dv_X\). Volume comparison bounds the number meeting this neighborhood by a finite number. The family is therefore locally finite. ∎

**The same centers at every permissible radius.** For every \(0<R\leq r_*\), the family \(\{B_{X_\nu}(R)\}\) is locally finite and has multiplicity at most \(\lceil C_g^d(1+R/r)^d\rceil\); it covers whenever \(R\geq R_1\). These assertions hold for the same centers, not a new selection for each \(R\). In the last two paragraphs of the proof replace \(R_2\) by \(R\); the only radius condition used in the metric comparison is \(R\leq r_*\). The covering assertion follows by inclusion from the cover at \(R_1\).

In particular, given \(0<\varepsilon<1\), choose \(r=r_*\sqrt\varepsilon/[8(1+C_g)]\). The same centers cover at every radius satisfying \(\varepsilon r_*^2<R^2\), and their multiplicity for all \(R^2<r_*^2\) is bounded by the one constant

\[
N_\varepsilon=\left\lceil C_g^d
\left(1+8(1+C_g)/\sqrt\varepsilon\right)^d\right\rceil.
\]

Indeed, \(R_1=r_*\sqrt\varepsilon/8\), which is smaller than every radius in that covering range; the multiplicity estimate follows by using \(R\leq r_*\).

## 3. A partition of unity with uniform derivatives

**Theorem 3.1 (Uniform partition).** With the centers above, there are smooth nonnegative functions \(\phi_\nu\), compactly supported in \(B_{X_\nu}(R_2)\), such that

\[
\sum_\nu\phi_\nu=1,
\qquad
\sup_{X,\nu}|\phi_\nu|_{k,g}(X)\leq A_k
\quad(k\geq0).                                                   \tag{5}
\]

The constants depend only on \(d,k,r,C_g\) and on one fixed scalar cutoff. The same assertion holds with \(g_X\) in each derivative norm replaced by \(g_{X_\nu}\).

**Proof.** Choose a smooth function \(\chi:[0,\infty)\to[0,1]\) equal to one on \([0,1]\), with support in \([0,4)\), and put

\[
\theta_\nu(X)=\chi\left(g_{X_\nu}(X-X_\nu)/R_1^2\right),
\quad H(X)=\sum_\nu\theta_\nu(X),
\quad\phi_\nu=\theta_\nu/H.                                     \tag{6}
\]

Local finiteness just proved makes all sums smooth. The cover gives \(H\geq1\); multiplicity gives \(H\leq N\). A linear isometry from \((E,g_{X_\nu})\) to Euclidean space turns \(\theta_\nu\) into the same fixed radial cutoff at radius \(R_1\). Its derivatives of every order have a bound independent of \(\nu\). On its support, (1) compares \(g_X\) and \(g_{X_\nu}\), so these derivative bounds also hold in \(g_X\), with an extra factor at most \(C_g^{k/2}\). Off the support, all derivatives vanish.

At a given point only at most \(N\) terms can contribute derivatives to \(H\). Therefore \(|H|_{k,g}\leq ND_k\) for constants \(D_k\). To control the reciprocal, differentiate \(H\cdot H^{-1}=1\). In arbitrary directions \(T_1,\ldots,T_k\), the term with all derivatives on \(H^{-1}\) equals minus the sum of the other product-rule terms, divided by \(H\). Since \(H\geq1\), induction on \(k\) gives a uniform bound for \(|H^{-1}|_{k,g}\). No derivative of the metric occurs in this calculation: the norm is evaluated at the fixed point after differentiating scalar functions. Apply the product rule to \(\theta_\nu H^{-1}\) to get (5). The same pointwise comparison of metrics gives the assertion in the frozen metric. ∎

**A partition uniform in the outer radius.** In the preceding \(\varepsilon\)-parameter version, assume \(0<\varepsilon<1/2\). A single partition can be chosen with compact support in \(B_{X_\nu}(R)\) for *every* \(R\) with \(2\varepsilon r_*^2<R^2<r_*^2\), and derivative bounds depending on \(\varepsilon,r_*,C_g,d,k\) and the fixed cutoff, not on \(R\). To prove this, take \(\chi=1\) on \([0,1]\) with support in \([0,2)\), and use \(\theta_\nu=\chi(g_{X_\nu}(X-X_\nu)/(\varepsilon r_*^2))\). The cover at \(R_1=r_*\sqrt\varepsilon/8\) makes the sum at least one. All supports lie within radius \(r_*\sqrt{2\varepsilon}<r_*\), so metric comparison and the uniform bound \(N_\varepsilon\) apply. The derivative and reciprocal argument above is unchanged. Since those compact supports lie inside every ball in the stated range, the assertion follows. For \(\varepsilon\geq1/2\) the range of such outer radii is empty.

## 4. Localizing and reconstructing symbols

**Theorem 4.1 (Analysis and reconstruction).** If \(a\in S(m,g)\), the pieces \(a_\nu=\phi_\nu a\) are supported in \(B_{X_\nu}(R_2)\), and for every \(k\)

\[
\sup_\nu\sup_X\frac{|a_\nu|_{k,g_{X_\nu}}(X)}{m(X_\nu)}
\leq C_k p_{\leq k}(a;m,g).                                     \tag{7}
\]

Conversely, suppose smooth functions \(b_\nu\) are supported in these balls and satisfy

\[
\sup_\nu\sup_X |b_\nu|_{k,g_{X_\nu}}(X)/m(X_\nu)\leq L_k
\quad\text{for every }k.                                       \tag{8}
\]

Then \(b=\sum_\nu b_\nu\) is a smooth symbol and

\[
p_k(b;m,g)\leq NC_m C_g^{k/2}L_k.                             \tag{9}
\]

**Proof.** On the support of a piece, (1)–(2) compare the metric and weight at \(X\) with their values at the center. Apply the product rule and (5) to obtain (7). For reconstruction, local finiteness makes the sum smooth. At every point at most \(N\) derivative tensors occur. A direction of \(g_X\)-length at most one has \(g_{X_\nu}\)-length at most \(\sqrt{C_g}\). Estimate each tensor by (8), multiply by the weight-comparison constant \(C_m\), and add the at most \(N\) contributions. This gives exactly (9). ∎

This result is a quantitative interface: a later operator estimate can be proved on compactly supported symbols measured in one fixed ellipsoid, and then combined using a separately justified summability estimate. Local bounded overlap alone does not justify summing the *images* of pieces under a nonlocal operator.

The reconstruction assertion also holds for the same centers and any support radius \(0<R<r_*\), with the multiplicity constant at that radius replacing \(N\). The all-radius part of Theorem 2.1 supplies local finiteness and multiplicity, and (1)–(2) still compare center data with point data. Thus the proof of (9) applies verbatim at the new radius. In the \(\varepsilon\)-parameter version, \(N_\varepsilon\) gives a uniform bound over all such radii.

## 6. Compact comparison and the local topology

At any fixed point \(X\), (1)–(2) give a neighborhood on which the metric is comparable to \(g_X\) and the weight is bounded above and bounded away from zero. A finite subcover gives such bounds on a compact set. In fixed coordinates this means that convergence in all the seminorms (3) implies convergence of every derivative uniformly on compact sets.

In particular every compact smooth function is in \(S(m,g)\):
its derivatives are bounded on its support, where the metric and
weight have the stated bounds; all derivatives vanish off the support.
On smooth functions the local topology is metrized by
\[
 \sum_{j\geq1}2^{-j}\min\left(1,
       \max_{|\alpha|\leq j,\ |X|\leq j}
                    |\partial^\alpha(a-b)(X)|\right).
 \tag{ML1}
\]
Convergence in every displayed seminorm implies convergence in this
metric: choose a finite initial sum with arbitrarily small remaining
tail, then make each of its terms small. Conversely its \(j\)-th
term tending to zero forces that seminorm to tend to zero. The triangle
inequality follows from
\(\min(1,s+t)\leq\min(1,s)+\min(1,t)\).
If the metric is zero all derivative differences, in particular all
function values on every ball, are zero. Thus sequential arguments
about bounded subsets in the multiplier companion use an actual
metric and the stated local topology.

## 7. Approximation on compact sets

**Proposition 7.1.** Every \(a\in S(m,g)\) is the limit in \(C^\infty_{\mathrm{loc}}\) of a sequence \(a_N\in C_c^\infty(E)\) bounded in every seminorm of \(S(m,g)\).

**Proof.** First \(C_c^\infty(E)\subset S(m,g)\), by the compact-set comparison in Section 6. Enumerate the partition and set \(a_N=\sum_{\nu\leq N}\phi_\nu a\). Each sum has compact support. The proof of (7)–(9) gives bounds independent of \(N\). On any compact set only finitely many partition supports meet it; after all these indices have been included, \(a_N=a\) on a neighborhood of that compact set. This proves the asserted convergence. ∎

This is deliberately a bounded approximation statement. It does not assert convergence in the symbol seminorms. For the constant Euclidean metric and \(m=1\), the symbol \(a=1\) has \(p_0(1-b;1,g)\geq1\) for every compactly supported \(b\). Thus \(C_c^\infty\) need not be dense in the Fréchet topology. Later extension theorems must specify which topology their continuity uses.

## Free human comparison

[Nicolas Lerner's author-hosted PSEUDO.2005.pdf](https://webusers.imj-prg.fr/~nicolas.lerner/PSEUDO.2005.pdf),
Theorem 3.1.1 on pages 22–23, gives a continuous partition formulation.
The complete discrete partition and bounded approximation used here
are the retained programme proofs above. No original PDF or human-source
prose is included.
