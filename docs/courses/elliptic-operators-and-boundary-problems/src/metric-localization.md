# Localizing symbols with moving metrics

A symbol can be measured by a different ellipsoid at every point. Those ellipsoids may be anisotropic, their coefficients need not vary smoothly, and the weight may be discontinuous. We construct a locally finite cover, a partition of unity, and smooth representatives of the metric and weight. The resulting localization and reconstruction estimates make no uncertainty, symplectic, or temperateness assumption; later operator theorems require their own additional hypotheses.

We use finite-dimensional differential calculus, compactness, Lebesgue volume under linear changes of variables, and the maximality principle for partially ordered sets. The supporting arguments are collected in [Metric and topological foundations](metric-foundation-bridges.md). The covering and partition proofs appear here. A freely accessible treatment of the wider calculus is [Lerner].

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

## 5. Smooth metrics and weights with the same symbol space

**Theorem 5.1 (Smooth representatives).** There is a positive smooth function \(M\) such that

\[
C_m^{-1}m\leq M\leq C_m m,
\qquad M\in S(m,g).                                           \tag{10}
\]

There is also a smooth field of positive-definite forms \(G_X\) such that

\[
C_g^{-1}g_X\leq G_X\leq C_g g_X,                              \tag{11}
\]

and, for every \(k\),

\[
\left|D_X^kG_X(V,W)[T_1,\ldots,T_k]\right|
\leq B_k\sqrt{g_X(V)g_X(W)}\prod_{j=1}^k\sqrt{g_X(T_j)}.       \tag{12}
\]

Here the same notation denotes a quadratic form and its symmetric bilinear form. The symbol spaces \(S(M,G)\) and \(S(m,g)\) agree, with equivalent seminorms.

**Proof.** Define

\[
M(X)=\sum_\nu\phi_\nu(X)m(X_\nu),\qquad
G_X=\sum_\nu\phi_\nu(X)g_{X_\nu}.                            \tag{13}
\]

Both sums are locally finite. On the support of \(\phi_\nu\), (1)–(2) apply between \(X_\nu\) and \(X\). Since the coefficients are nonnegative and sum to one, weighted averaging immediately proves (10) without its derivative assertion, and proves (11). In particular the average form is positive definite.

Differentiating (13) differentiates only \(\phi_\nu\), since the center values are constants. At a given point there are at most \(N\) nonzero terms, and (5) bounds the differentiated coefficients. It follows that \(|M|_{k,g}\leq NA_kC_m m\). For the metric, the Cauchy–Schwarz inequality for the positive form \(g_{X_\nu}\), followed by (1), gives

\[
|g_{X_\nu}(V,W)|
\leq\sqrt{g_{X_\nu}(V)g_{X_\nu}(W)}
\leq C_g\sqrt{g_X(V)g_X(W)}.
\]

Together with (5) this proves (12) with \(B_k=NA_kC_g\). Finally (10)–(11) compare each defining seminorm in either direction. Thus equality and equivalence of the symbol spaces follow directly from (3), without differentiating the weight or the metric. ∎

The new metric is itself slowly varying. Indeed, if \(G_X(Y-X)\leq r_*^2/C_g\), then \(g_X(Y-X)\leq r_*^2\); inserting (11) on both sides of (1) compares \(G_Y\) and \(G_X\) with constant \(C_g^3\). The new weight is locally comparable on these balls by (2) and (10). Thus regularization keeps us within the same class of local data.

**Corollary 5.2 (Recognition of weights).** For fixed \(g\) and two locally admissible weights \(m_1,m_2\), the inclusion \(S(m_1,g)\subset S(m_2,g)\) as sets holds if and only if \(m_1/m_2\) is bounded. The reverse implication follows from (3). For the forward implication, construct \(M_1\) by (10). It lies in \(S(m_1,g)\), hence in \(S(m_2,g)\); its zeroth seminorm gives \(M_1\leq Cm_2\), and (10) then gives the claimed ratio bound. In particular, equality of these spaces is equivalent to comparability of the weights in both directions.

## 6. Completeness, products and reciprocals

The pointwise differential inequalities in this section are local statements: for fixed \(k\), they apply to complex-valued \(C^k\) functions on a neighborhood of the point, measured in any fixed positive-definite form \(Q\). In particular the product rule gives
\[
|ab|_{k,Q}(X)\leq\sum_{j=0}^k\binom{k}{j}|a|_{j,Q}(X)|b|_{k-j,Q}(X).
\]
No global symbol membership is needed for this inequality or for the pointwise reciprocal bound (18). Global smoothness and symbol seminorms are imposed only for the Fréchet-space and symbol-membership conclusions.

**Proposition 6.1.** The seminorms (3) make \(S(m,g)\) a Fréchet space. For locally admissible weights \(m_1,m_2\), multiplication is continuous and satisfies

\[
p_k(ab;m_1m_2,g)
\leq\sum_{j=0}^k\binom{k}{j}
p_j(a;m_1,g)p_{k-j}(b;m_2,g).                                \tag{14}
\]

If \(a\in S(m,g)\) and \(|a(X)|\geq c\,m(X)\) for some \(c>0\), then \(a^{-1}\in S(m^{-1},g)\). Its seminorms are bounded recursively by

\[
b_0=c^{-1},\qquad
b_k=c^{-1}\sum_{j=1}^k\binom{k}{j}p_j(a;m,g)b_{k-j},
\qquad p_k(a^{-1};m^{-1},g)\leq b_k.                         \tag{15}
\]

**Proof.** At any fixed point \(X\), (1)–(2) give a neighborhood on which the metric is comparable to \(g_X\) and the weight is bounded above and bounded away from zero. A finite subcover gives such bounds on a compact set. In fixed coordinates this means that convergence in all the seminorms (3) implies convergence of every derivative uniformly on compact sets.

If \((a_n)\) is Cauchy in every seminorm, its coordinate derivatives of every order have uniform limits on compact sets. These limits are the derivatives of a single smooth function: on a coordinate box apply the fundamental theorem of calculus to \(a_n\) along each coordinate segment, pass to the uniform limit, and repeat for each already obtained derivative. At a fixed \(X\), pass to the limit in

\[
|a_n-a_\ell|_{k,g}(X)\leq\varepsilon m(X)
\]

for sufficiently large \(n,\ell\). The result is the same bound for \(a_n-a\), uniformly in \(X\); hence convergence holds in every \(p_k\), and \(a\in S(m,g)\). The topology is Hausdorff because \(p_0\) separates points. A countable family of seminorms is metrized, for example, by \(\sum_{k\geq0}2^{-k-1}\min(1,p_k(a-b))\). This establishes the Fréchet assertion.

For multiplication, apply the multilinear product rule. There are \(\binom{k}{j}\) ways to place \(j\) of the \(k\) derivatives on the first factor, giving (14). The product weight satisfies (2), with the product of the two comparison constants and the smaller common radius.

The reciprocal is smooth because \(a\) has no zero. Differentiate \(aa^{-1}=1\). Move the term with no derivative on \(a\) to the other side, divide by \(a\), and use \(|a|^{-1}\leq c^{-1}m^{-1}\). Induction gives (15): each product involving \(j\) derivatives of \(a\) has weight \(m\), while the derivative of its reciprocal has weight \(m^{-1}\); the weights cancel before the final division by \(a\). ∎

The same argument works for matrices of any fixed finite size, using an operator norm and the assumption \(\|a(X)^{-1}\|\leq c^{-1}m(X)^{-1}\). The identity is differentiated with the order of matrix factors preserved. This is a symbol estimate; it is not the construction of an inverse to a quantized operator.

There is also a useful scalar pointwise bound that does not involve a global weight. Fix \(k\geq1\), a positive-definite form \(Q\), and a \(C^k\) function \(a\) near a point \(X\) with \(a(X)=1\). Then

\[
|a^{-1}|_{k,Q}(X)
\leq C_k\left(\sum_{j=1}^k |a|_{j,Q}(X)^{1/j}\right)^k.       \tag{18}
\]

To verify it, differentiate the scalar composite \(t\mapsto t^{-1}\) with \(t=a\). Its \(k\)-th multilinear derivative is the sum over set partitions \(\pi\) of \(\{1,\ldots,k\}\), with term

\[
(-1)^{|\pi|}|\pi|!\,a(X)^{-|\pi|-1}
\prod_{B\in\pi}D^{|B|}a(X)[T_j:j\in B].
\]

This formula follows by induction: differentiating the scalar power adds a singleton block, while differentiating a derivative factor appends the new index to its block; these exhaust the set partitions with their indicated coefficients. Put \(H=\sum_{j=1}^k |a|_{j,Q}(X)^{1/j}\). Each factor of order \(j\) is at most \(H^j\) on unit directions. Each partition term therefore has size at most \(|\pi|!H^k\); summing proves (18) with \(C_k=\sum_\pi|\pi|!\). If \(H=0\), every positive-order derivative factor vanishes and the same conclusion holds. For any nonzero \(a(X)\), the estimate keeps the relative derivative factors of \(a/a(X)\) together with \(|a(X)|^{-1}\). The partition calculation below shows every inverse power explicitly.

### The reciprocal bound from every original partition term

For the scalar pointwise estimate, keep the original function \(a\), point \(X\), positive-definite form \(Q\) and all inverse powers. Suppose \(a\) is \(C^k\) near \(X\), \(k\geq1\), and \(a(X)\ne0\); continuity gives a neighborhood on which its reciprocal is defined. The full partition formula above applies there. Define the actual quantities

\[
q_j=|a|_{j,Q}(X),\qquad
H_a=\sum_{j=1}^k
\left(\frac{q_j}{|a(X)|}\right)^{1/j},\qquad
C_k=\sum_{\pi\in\mathcal P_k}|\pi|!,
\tag{19}
\]

where \(\mathcal P_k\) is the finite set of partitions of \(\{1,\ldots,k\}\). All denominators use the original nonzero value; no new function replaces \(a\). For \(Q\)-unit directions, the exact term of partition \(\pi\) has absolute value at most

\[
|\pi|!\,|a(X)|^{-1-|\pi|}
\prod_{B\in\pi}q_{|B|}
=|\pi|!\,|a(X)|^{-1}
\prod_{B\in\pi}\frac{q_{|B|}}{|a(X)|}
\leq |\pi|!\,|a(X)|^{-1}H_a^k.
\tag{20}
\]

The equality displays one original inverse factor for each block and the remaining factor \(|a(X)|^{-1}\). The last inequality follows because each summand in \(H_a\) is nonnegative, so \(q_j/|a(X)|\leq H_a^j\), and the block sizes sum to \(k\). Sum the finitely many exact partition terms and take the supremum over all original unit directions. This proves

\[
|a^{-1}|_{k,Q}(X)
\leq C_k|a(X)|^{-1}
\left(\sum_{j=1}^k
\left(\frac{|a|_{j,Q}(X)}{|a(X)|}\right)^{1/j}\right)^k.
\tag{21}
\]

If \(H_a=0\), every \(q_j\) is zero, every positive-order partition term vanishes, and both sides of (21) are zero. The order-zero formula remains exactly \(|a^{-1}|_{0,Q}(X)=|a(X)|^{-1}\). With \(a(X)=1\), (21) gives the earlier (18) with the same \(C_k\); the earlier formula remains its stated special case. The induction for the full partition identity is unchanged: a derivative of the actual power \(a^{-1-|\pi|}\) creates a singleton block with coefficient \(-1-|\pi|\), while a derivative of an existing factor appends the new labeled direction to that block. These two cases produce every partition once and retain its sign \((-1)^{|\pi|}\), factorial \(|\pi|!\) and actual inverse power. This proves the general estimate directly from the original function and each full derivative term.

## 7. Approximation on compact sets

**Proposition 7.1.** Every \(a\in S(m,g)\) is the limit in \(C^\infty_{\mathrm{loc}}\) of a sequence \(a_N\in C_c^\infty(E)\) bounded in every seminorm of \(S(m,g)\).

**Proof.** First \(C_c^\infty(E)\subset S(m,g)\), by the compact-set comparison in Proposition 6.1. Enumerate the partition and set \(a_N=\sum_{\nu\leq N}\phi_\nu a\). Each sum has compact support. The proof of (7)–(9) gives bounds independent of \(N\). On any compact set only finitely many partition supports meet it; after all these indices have been included, \(a_N=a\) on a neighborhood of that compact set. This proves the asserted convergence. ∎

This is deliberately a bounded approximation statement. It does not assert convergence in the symbol seminorms. For the constant Euclidean metric and \(m=1\), the symbol \(a=1\) has \(p_0(1-b;1,g)\geq1\) for every compactly supported \(b\). Thus \(C_c^\infty\) need not be dense in the Fréchet topology. Later extension theorems must specify which topology their continuity uses.

## 8. An anisotropic model

On \(E=\mathbb R_x^n\times\mathbb R_\xi^n\), take arbitrary real \(\delta,q\), take \(\rho\leq1\), and set

\[
\langle\xi\rangle=(1+|\xi|^2)^{1/2},\qquad
g_{(x,\xi)}(y,\eta)
=\langle\xi\rangle^{2\delta}|y|^2
+\langle\xi\rangle^{-2\rho}|\eta|^2,
\qquad m(x,\xi)=\langle\xi\rangle^q.                         \tag{16}
\]

If \(g_{(x,\xi)}(y,\eta)\leq r_*^2\), then
\(|\eta|\leq r_*\langle\xi\rangle^\rho\leq r_*\langle\xi\rangle\).
Since the function \(\xi\mapsto\langle\xi\rangle\) is one-Lipschitz,

\[
(1-r_*)\langle\xi\rangle\leq\langle\xi+\eta\rangle
\leq(1+r_*)\langle\xi\rangle.
\]

Choose \(r_*<1/2\). Raising this ratio to each of the fixed real powers in (16) proves both (1) and (2). From (3), or by testing coordinate directions and expanding arbitrary directions, membership in \(S(m,g)\) is equivalent to

\[
|\partial_x^\beta\partial_\xi^\alpha a(x,\xi)|
\leq C_{\alpha\beta}
\langle\xi\rangle^{q+\delta|\beta|-\rho|\alpha|}.             \tag{17}
\]

The present localization theorem therefore includes all these parameter choices, not just \((\rho,\delta)=(1,0)\). It does not claim that all of them support the same composition or continuity theorem. In particular, those conclusions cannot be inferred merely from the proof of slow variation.

## 9. Exercises and solutions

**Problem 1: an unsmoothed weight.** For the Euclidean metric on \(\mathbb R^d\), let \(m(X)=2+\mathbf1_{\{X_1\geq0\}}\). Verify the hypotheses and identify \(S(m,g)\). Explain what the regularization theorem supplies.

**Solution.** The metric comparison constant is one at every radius. The weight lies between two and three, so any pair of points satisfies (2) with \(C_m=3/2\). Formula (3) gives \(\frac13\sup|D^ka|\leq p_k(a;m,g)\leq\frac12\sup|D^ka|\). Thus the space consists exactly of smooth functions with all derivatives bounded, with its usual topology. Theorem 5.1 constructs a positive smooth representative comparable to the discontinuous weight. It does not claim to make the original weight continuous or to approximate its jump uniformly by continuous functions.

**Problem 2: the missing local-finiteness argument.** The intervals \((2^{-j},3\cdot2^{-j-1})\), \(j\geq1\), have multiplicity one. Are they locally finite in \(\mathbb R\)? Which part of Theorem 2.1 prevents the analogous failure?

**Solution.** They are pairwise disjoint, but every neighborhood of zero meets infinitely many. They are therefore not locally finite. In Theorem 2.1, slow variation compares *every* center whose large ball meets a fixed small neighborhood with the metric at that neighborhood's center. It gives a common positive lower bound for the volumes of the disjoint small balls, inside one bounded ellipsoid. That neighborhood-volume argument, rather than the pointwise bound alone, proves local finiteness.

**Problem 3: a matrix symbol with a nonconstant scale.** For a weight \(m\), let \(M\) be its smooth representative and let \(B\in S(1,g;\mathbb C^{r\times r})\) satisfy \(\sup_X\|B(X)\|\leq1/2\). Show that \(A=M(I+B)\) belongs to \(S(m,g)\) and that \(A^{-1}\in S(m^{-1},g)\).

**Solution.** Product estimate (14) gives the symbol bound for \(A\). For each \(X\), the geometric series \(\sum_{j\geq0}(-B(X))^j\) converges in operator norm, multiplies \(I+B(X)\) to the identity, and has norm at most two. Hence \(\|A(X)^{-1}\|\leq2/M(X)\leq2C_m/m(X)\). The matrix form of (15) now bounds every derivative of the inverse. Differentiating the infinite geometric series is unnecessary and would require a separate convergence argument.

**Problem 4: a distinction in approximation.** Give an approximating sequence for the constant symbol one which is bounded in \(S(1,g)\), converges locally smoothly, and fails to converge in \(p_0\), for Euclidean \(g\).

**Solution.** Choose \(\psi\in C_c^\infty\) equal to one near the origin and set \(a_N(X)=\psi(X/N)\). Derivatives of order \(k\) have supremum at most \(N^{-k}\sup|D^k\psi|\), so the sequence is bounded in every seminorm. On each compact set it is eventually identically one. But each \(a_N\) vanishes outside a compact set, so \(p_0(a_N-1;1,g)\geq1\). This explicitly separates the two topologies used in Proposition 7.1.

## References

- [Lerner] Nicolas Lerner, *Introduction to the Weyl–Hörmander Calculus of Pseudodifferential Operators*, lecture notes.

