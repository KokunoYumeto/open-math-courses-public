# Local data and compatible products

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

A distribution has no values at individual points, but it still has restrictions to open sets. Compatible restrictions determine one global distribution. This local principle explains support, extends the possible test functions, and defines some products even when both factors are singular.

We use the test topology in [Distributions as kernels of continuous operators](distributions-as-kernels.md), the finite-order extension and completeness results in [Order, positivity and distributional limits](order-positivity-and-limits.md), and the compact-distribution pairing in [When a kernel is smooth](when-a-kernel-is-smooth.md). Smooth cutoffs and partitions are ordinary calculus prerequisites. The open reference is [Dyatlov 2026], Sections 2.3, 3.2 and 8.3. We give full proofs of the local constructions rather than presume that a pointwise definition is available.

Basic references are Dyatlov’s notes cited below and Hassler Whitney’s *Analytic extensions of differentiable functions defined in closed sets* (1934), for the finite-jet viewpoint.

## Restriction and a local uniqueness principle

Let \(V\subset X\subset\mathbb R^n\) be open. Extending \(\phi\in C_c^\infty(V)\) by zero gives a smooth compactly supported function on \(X\): its support has positive distance from the complement of \(V\). Define

\[
(u|_V)(\phi)=u(\phi),\qquad u\in\mathcal D'(X).
\tag{1.1}
\]

The local distribution estimate on its support proves that this is a distribution on \(V\). Restrictions compose, and restriction to \(X\) is the identity.

Here is the finite partition fact we will repeatedly use. If compact \(K\subset X\) is covered by open \(V_i\), there are finitely many smooth compactly supported functions \(\chi_l\), each supported in some \(V_{i(l)}\), with \(\sum_l\chi_l=1\) on a neighborhood of \(K\). To construct them, cover \(K\) by finitely many smaller balls whose closures lie in the prescribed open sets, choose nonnegative bumps positive on those balls, and write their sum as \(S\). It is positive on a neighborhood of \(K\). Choose a cutoff \(\zeta=1\) near \(K\), supported in that neighborhood, and set \(\chi_l=\zeta b_l/S\) there and zero elsewhere. This extension is smooth because \(\zeta\)'s support lies inside the positive region. Each support is compact in its prescribed set.

**Theorem 1.1 (local uniqueness).** If every point of \(X\) has an open neighborhood on which \(u\) restricts to zero, then \(u=0\).

**Proof.** For \(\phi\in\mathcal D(X)\), apply the finite partition fact to \(K=\operatorname{supp}\phi\) and neighborhoods on which \(u=0\). Then \(\phi=\sum_l\chi_l\phi\), a finite sum of tests in those neighborhoods, and every pairing \(u(\chi_l\phi)\) is zero. Hence \(u(\phi)=0\). \(\square\)

Define \(\operatorname{supp}u\) to be the complement in \(X\) of the union of open neighborhoods on which \(u\) is zero. It is relatively closed. Theorem 1.1 says \(u\) vanishes on that entire open union, not just separately on its constituent neighborhoods. Therefore

\[
u(\phi)=0\quad\text{if }
\operatorname{supp}\phi\cap\operatorname{supp}u=\varnothing,
\qquad \phi\in\mathcal D(X).
\tag{1.2}
\]

The support is the smallest relatively closed set with this property. Indeed, if a relatively closed \(F\) annihilates every test supported in \(X\setminus F\), \(u\) is zero on that open set and \(\operatorname{supp}u\subset F\).

## Gluing compatible distributions

**Theorem 2.1 (gluing, including order and limits).** Let \(X=\bigcup_{i\in I}X_i\) be an arbitrary open cover, and let \(u_i\in\mathcal D'(X_i)\). Suppose their restrictions agree on every overlap:

\[
u_i|_{X_i\cap X_j}=u_j|_{X_i\cap X_j}.
\tag{2.1}
\]

There is a unique \(u\in\mathcal D'(X)\) with \(u|_{X_i}=u_i\). If every \(u_i\) has order at most the same integer \(k\), then \(u\) has order at most \(k\).

Moreover, if a sequence \(v_r\in\mathcal D'(X)\) has a weak distributional limit on each \(X_i\), it has a weak distributional limit on \(X\), whose restrictions are those local limits.

**Proof of existence and uniqueness.** Given a test \(\phi\), use the finite partition fact to write

\[
\phi=\sum_{l=1}^N\phi_l,\qquad
\phi_l\in\mathcal D(X_{i(l)}),
\]

and propose \(u(\phi)=\sum_l u_{i(l)}(\phi_l)\). This definition is independent of the decomposition. It suffices to prove that a finite decomposition of zero gives zero total pairing. If \(\sum_l\phi_l=0\), choose a second finite partition \(\theta_s\) equal to one near the compact union of their supports, with \(\theta_s\) supported in \(X_{j(s)}\). Then \(\theta_s\phi_l\) is a test in both open sets, so compatibility gives

\[
\begin{aligned}
\sum_l u_{i(l)}(\phi_l)
&=\sum_{l,s}u_{i(l)}(\theta_s\phi_l)\\
&=\sum_s u_{j(s)}\left(\theta_s\sum_l\phi_l\right)=0.
\end{aligned}
\tag{2.2}
\]

All these sums are finite. Comparing two decompositions through their difference proves independence, and combining decompositions proves linearity.

To prove continuity, fix compact \(K\subset X\) and fix one finite partition \(\chi_l\) equal to one near \(K\), subordinate to the cover. For every \(\phi\in\mathcal D_K\),

\[
u(\phi)=\sum_l u_{i(l)}(\chi_l\phi).
\tag{2.3}
\]

The supports \(K\cap\operatorname{supp}\chi_l\) are compact subsets of the corresponding \(X_{i(l)}\). Choose their local order bounds. The product rule bounds the finitely many needed derivatives of \(\chi_l\phi\) by a constant times the derivatives of \(\phi\) through their maximum order. This proves a finite estimate for \(u\) on \(K\). If the local orders are all at most \(k\), that maximum can be \(k\); derivatives of the fixed cutoffs do not raise the derivative degree of \(\phi\).

For a test supported in \(X_i\), the decomposition consisting of that test alone proves the correct restriction. Uniqueness follows by applying Theorem 1.1 to the difference of two proposed extensions.

**Proof of the limit assertion.** Local limits agree on overlaps because every overlap test has the same scalar limit from either side. Glue them to \(u\). For a fixed global test, (2.3) expresses \(v_r(\phi)\) as finitely many local pairings, each converging to its corresponding \(u_i(\chi_l\phi)\). Their sum is \(u(\phi)\). Alternatively their scalar limits define a distribution by [Order, positivity and distributional limits, Theorem 5.1](order-positivity-and-limits.md#limits-on-smooth-tests). \(\square\)

Neither the cover nor its index set must be finite or countable. Compactness of each individual test reduces all the pairing arguments to finite sums.

## Tests that are compact only on the support

An integrable function supported in a closed set needs a test only where the two supports meet. A distribution has the same flexibility, with a cutoff supplying the precise definition.

**Theorem 3.1 (support-relative test extension).** Let \(u\in\mathcal D'(X)\) and let \(F\subset X\) be relatively closed, with \(\operatorname{supp}u\subset F\). On the vector space

\[
\mathcal E_F(X)=
\{f\in C^\infty(X):
F\cap\operatorname{supp}f\text{ is compact in }X\},
\tag{3.1}
\]

there is a unique linear extension \(\widetilde u\) of \(u\) that vanishes whenever \(\operatorname{supp}f\cap F=\varnothing\). If \(\chi\in C_c^\infty(X)\) equals one near \(F\cap\operatorname{supp}f\), its formula is

\[
\widetilde u(f)=u(\chi f).
\tag{3.2}
\]

When \(u\) has order at most \(k\), the same construction extends its canonical \(C_c^k\) pairing to the space defined by (3.1) with \(C^k(X)\) in place of \(C^\infty(X)\).

**Proof.** The space is closed under addition and scalar multiplication: the support of a sum is contained in the union of the two supports, and its intersection with closed \(F\) is a closed subset of their compact intersections.

For two suitable cutoffs, \((\chi-\chi')f\) has compact support disjoint from \(F\). At points of \(F\cap\operatorname{supp}f\), the cutoffs agree on a neighborhood; at other points of \(F\), \(f\) is zero on a neighborhood. Hence (1.2) makes its pairing zero. Formula (3.2) is well-defined. For finitely many functions choose one cutoff near the union of their compact intersections, which proves linearity. For a compact test it agrees with \(u\) by (1.2), and for a function disjoint from \(F\) it is zero.

For uniqueness, split \(f=\chi f+(1-\chi)f\). The first term is a compact test. The second has support disjoint from \(F\), by the same neighborhood argument. Every extension with the stated vanishing property must therefore give (3.2).

For the finite-order assertion, use the \(C_c^k\) pairing from [Order, positivity and distributional limits, Proposition 1.2](order-positivity-and-limits.md#local-estimates-and-the-meaning-of-order). A compact \(C^k\) function with support disjoint from \(\operatorname{supp}u\) pairs to zero: approximate it in \(C^k\) by smooth functions with support in a compact neighborhood still disjoint from that closed set. Thus the entire cutoff argument remains valid. \(\square\)

We henceforth write \(u(f)\) for this extension when its domain is specified. Choosing \(F=\operatorname{supp}u\) gives the largest domain among these choices of \(F\). For compactly supported \(u\), it includes every smooth function, agreeing with the compact-dual pairing already proved. Relative compactness inside \(X\) matters: a support intersection escaping toward the boundary is not an allowed compact set in (3.1).

## The smooth locus and local operations

Define the singular support \(\operatorname{sing\,supp}u\) as the complement of the union of open sets where \(u\) is represented by a smooth function.

Smooth representatives on overlaps agree pointwise. To justify this, a continuous function defining the zero distribution must vanish: if its value at a point were nonzero, a fixed complex phase makes its real part positive on a smaller neighborhood, and a nonnegative bump there would have nonzero integral pairing. Consequently the local representatives form one smooth function on the full union. Theorem 1.1 identifies its distribution with the restriction of \(u\). Thus the complement of singular support is the largest open set on which \(u\) is smooth, and

\[
\operatorname{sing\,supp}u\subset\operatorname{supp}u.
\tag{4.1}
\]

For \(a\in C^\infty(X)\), define

\[
(\partial_j u)(\phi)=-u(\partial_j\phi),
\qquad
(au)(\phi)=u(a\phi).
\tag{4.2}
\]

**Proposition 4.1 (local differential rules).** The operations (4.2) give distributions, commute with restriction, and are continuous in both the weak and strong dual topologies for fixed \(a\). They satisfy

\[
\begin{gathered}
\operatorname{supp}(\partial_j u)\subset\operatorname{supp}u,
\qquad
\operatorname{supp}(au)\subset\operatorname{supp}a\cap\operatorname{supp}u,\\
\operatorname{sing\,supp}(\partial_j u)\subset\operatorname{sing\,supp}u,
\qquad
\operatorname{sing\,supp}(au)\subset\operatorname{supp}a\cap\operatorname{sing\,supp}u,\\
\partial^\alpha(au)=
\sum_{\beta\le\alpha}\binom{\alpha}{\beta}
(\partial^\beta a)\partial^{\alpha-\beta}u.
\end{gathered}
\tag{4.3}
\]

Partial derivatives commute. Both formulas in (4.2) also hold for every \(f\in\mathcal E_{\operatorname{supp}u}(X)\), using the extended pairings on their left sides.

If \(a\in C^k(X)\) and \(u\) has order at most \(k\), the second formula still defines \(au\), by the \(C_c^k\) pairing. It has order at most \(k\), with support contained in the same support intersection. The singular-support assertions require a smooth multiplier.

**Proof.** Differentiation and multiplication send smooth tests with one compact support continuously to tests with that support. Their derivative estimates prove (4.2) is continuous on each support space. On weak duals, evaluating the output on \(\phi\) is evaluating the input on its transformed fixed test. On strong duals, a bounded test family is sent to another bounded test family; taking the supremum over it proves continuity. Restriction commutes with these test operations. Local vanishing and local smoothness give the support and singular-support inclusions.

The derivative convention gives \((\partial_i\partial_j u)(\phi)=u(\partial_i\partial_j\phi)\), so commutation of test derivatives gives commutation for distributions. For one derivative,

\[
\begin{aligned}
(a\,\partial_j u)(\phi)
&=-u(\partial_j(a\phi))\\
&=-u((\partial_j a)\phi)-u(a\partial_j\phi).
\end{aligned}
\]

Rearrange to obtain the first-derivative product rule. Induction on \(|\alpha|\), with the usual binomial recurrence, proves the multi-index formula.

For a noncompact allowed test \(f\), choose \(\chi=1\) near \(\operatorname{supp}u\cap\operatorname{supp}f\). The extra derivative term \(u(f\partial_j\chi)\) is zero, because its compact support misses \(\operatorname{supp}u\). Thus

\[
(\partial_j u)(f)=-u(\partial_j(\chi f))
=-u(\chi\partial_j f)=-u(\partial_j f).
\]

Multiplication works with the same cutoff. The supports of \(\partial_j f\) and \(af\) are contained in \(\operatorname{supp}f\), so their right-hand pairings are allowed. We only claim these identities on this common domain.

For \(a\in C^k\), the product \(a\phi\) lies in \(C_c^k\). On a fixed compact support the product rule through degree \(k\) and the canonical order estimate bound the resulting pairing by \(C p_{K,k}(\phi)\), with a constant that may use a larger compact neighborhood. Local vanishing extends from smooth to \(C_c^k\) tests as in Theorem 3.1. This proves the order and support assertions. \(\square\)

For example, the Heaviside function \(H\) on the line has support \([0,\infty)\) and singular support \(\{0\}\). It is smooth off zero, and cannot have a continuous representative near zero agreeing with its distinct constant values on the two sides. Its derivative is \(\delta_0\): for a compact test,

\[
H'(\phi)=-\int_0^\infty\phi'(x)\,dx=\phi(0).
\tag{4.4}
\]

The derivative has much smaller support, while retaining the same singular point.

For a point mass in any dimension, the same derivative convention gives \((\partial^\alpha\delta_a)(\phi)=(-1)^{|\alpha|}\partial^\alpha\phi(a)\). Conversely, every distribution supported at one point is a finite linear combination of these derivatives, as proved in [Jets, supported distributions and local operators, point-supported specialization](jets-supported-distributions-and-local-operators.md#the-exact-structure-on-a-plane). This converse uses finite order and flat-jet annihilation; it is more than a formal differentiation rule.

## Products of separated singularities

**Theorem 5.1 (compatible product and compact pairing).** Suppose \(u,v\in\mathcal D'(X)\) satisfy

\[
\operatorname{sing\,supp}u\cap\operatorname{sing\,supp}v=\varnothing.
\tag{5.1}
\]

There is a unique distribution \(uv\) obtained locally by multiplying whichever factor is smooth by the other. It is commutative, agrees with ordinary products where both factors are smooth, and satisfies

\[
\operatorname{supp}(uv)\subset
\operatorname{supp}u\cap\operatorname{supp}v.
\tag{5.2}
\]

If this support intersection is compact in \(X\), there is a symmetric scalar pairing

\[
\langle u,v\rangle=(uv)(1).
\tag{5.3}
\]

For a smooth \(v=f\), it agrees with \(u(f)\) from Theorem 3.1. For three distributions with pairwise disjoint singular supports, the compatible products associate.

**Proof.** Condition (5.1) covers \(X\) by open sets on each of which \(u\) or \(v\) has a smooth representative. Define the local product by (4.2). When two neighborhoods choose the same smooth factor, restriction gives agreement. When they choose opposite factors, both factors are smooth on their overlap, and both definitions give the ordinary pointwise product. Theorem 2.1 glues these compatible local distributions uniquely. Swapping the factors changes none of them, giving commutativity.

Outside either support, that factor is locally zero, a smooth representative, so the product is zero. This proves (5.2). If the support intersection is compact, the product is compactly supported, and its pairing with the constant smooth function one is defined. It is independent of any compact cutoff used to evaluate it.

When \(v=f\) is smooth, choose a cutoff \(\chi=1\) near \(\operatorname{supp}u\cap\operatorname{supp}f\). Then

\[
(uf)(1)=(uf)(\chi)=u(\chi f)=u(f),
\]

which proves agreement. The same argument explains the symmetry of this extension of the scalar pairing.

For the last assertion, near every point at most one of the three factors is singular, so the other two are smooth. Every local bracketing is smooth multiplication by their pointwise product, and agrees by ordinary associativity. Each intermediate product is smooth wherever its two factors are smooth, so its singular support is contained in the union of theirs and remains disjoint from the third singular support. Both bracketings are therefore defined; gluing their local equality proves global associativity. \(\square\)

This condition is sufficient, not necessary. Later wavefront estimates permit more products by separating singular directions rather than separating singular points. Nothing here defines \(\delta_0^2\).

**Corollary 5.2 (finite regularity with a fixed order).** Suppose \(u,v\) have order at most \(k\) on \(X\). Let \(S_k(u)\) and \(S_k(v)\) be the complements of their open \(C^k\) regular loci: the points near which they are represented by \(C^k\) functions. If \(S_k(u)\cap S_k(v)=\varnothing\), the local \(C^k\)-multiplier rule defines a commutative product of order at most \(k\). Its support satisfies (5.2), and a compact support intersection gives (5.3). With a globally \(C^k\) factor, the scalar pairing agrees with the \(C^k\) extension in Theorem 3.1. Three order-\(k\) distributions with pairwise disjoint \(S_k\) sets likewise associate.

**Proof.** Continuous representatives are unique by the same bump argument, so local \(C^k\) representatives glue as functions and their loci are open. The hypothesis provides a cover with one \(C^k\) factor on each piece. Proposition 4.1 defines the local products with order at most \(k\). If opposite factors are chosen on an overlap, both are \(C^k\) there, and their distributional product agrees with their ordinary function product, by uniform approximation in the canonical \(C_c^k\) pairing. Thus Theorem 2.1 glues them and preserves order \(k\). Local vanishing proves the support bound, and evaluating the compact product on one proves the scalar pairing. The cutoff computation from Theorem 5.1 remains valid with \(C^k\) tests by Theorem 3.1. For three factors, the pairwise disjoint exceptional sets leave at least two \(C^k\) factors near every point; the product of those functions is \(C^k\), and the same local associativity and gluing argument applies. \(\square\)

## Exercises

1. **Checking compatibility — foundation.** Cover the line by \(X_-=(-\infty,1)\) and \(X_+=(-1,\infty)\). Put \(u_-=H\) and \(u_+=H+\delta_2\), with each restricted to its indicated open set. Determine the glued distribution. If \(\delta_2\) is replaced by \(\delta_{1/2}\), explain exactly why gluing fails.
2. **A noncompact test — intermediate.** Let \(u=\sum_{j\ge1}\delta_j\) on the line. Choose a smooth function equal to \(1\) at \(j=1\), supported in \((1/2,3/2)\), and add an arbitrary smooth function supported in \((-\infty,-1)\). Show its pairing with \(u\) is defined and equals \(1\), although the test need not be compactly supported. Explain why the constant function one is outside the domain in Theorem 3.1.
3. **A finite-order multiplier — intermediate.** For \(a\in C^1(\mathbb R)\), compute \(a\delta'_0\) as a linear combination of \(\delta'_0,\delta_0\). Check both coefficients and show why knowing only \(a(0)\) is insufficient.
4. **Both factors singular — advanced.** Let \(u=\delta_0+e^{-x^2}\) and \(v=\delta_2+\rho\), where \(\rho\in C_c^\infty(\mathbb R)\). Compute their compatible product and their scalar pairing. State the singular-support and compactness hypotheses explicitly.
5. **An obstruction to arbitrary multiplication — advanced.** Let \(\rho\ge0\) be a nonzero smooth compactly supported function on the line with integral \(1\), and let \(\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)\). Prove \(\rho_\varepsilon\to\delta_0\) as distributions but \(\rho_\varepsilon^2\) has no distributional limit. Deduce that no jointly sequentially continuous multiplication on all pairs of distributions can agree with ordinary smooth multiplication.

## Complete solutions

**Solution 1.** On the overlap \((-1,1)\), \(\delta_2\) restricts to zero, so both local distributions are \(H\). The distribution \(H+\delta_2\) on the full line has exactly the stated restrictions. Uniqueness gives this as the gluing. With \(\delta_{1/2}\), a bump supported near \(1/2\) inside the overlap and equal to one there has local pairings differing by one. Thus the two restrictions disagree on the overlap, contradicting (2.1); no global distribution has both restrictions.

**Solution 2.** The distribution has support \(\{1,2,\ldots\}\); the sum is locally finite. The specified function's support intersects this set only at \(1\), a compact intersection, so Theorem 3.1 applies. A cutoff near \(1\), supported away from every other positive integer, evaluates the pairing as its value at \(1\), namely \(1\). The negative-side part contributes zero, regardless of its noncompact extent. The constant one has support all of the line, and its intersection with \(\operatorname{supp}u\) is the unbounded set of positive integers. This is not compact, so (3.1) does not define that pairing. Its formal sum of values would also diverge.

**Solution 3.** The \(C^1\) pairing gives

\[
(a\delta'_0)(\phi)=-(a\phi)'(0)
=-a(0)\phi'(0)-a'(0)\phi(0).
\]

Hence \(a\delta'_0=a(0)\delta'_0-a'(0)\delta_0\). The second coefficient has a minus sign. Two \(C^1\) functions with the same value at zero but different first derivatives give different products, because \(\delta'_0\) measures a first jet of the product test.

**Solution 4.** The smooth added functions do not cancel the delta singularities, so the singular supports are exactly \(\{0\}\) and \(\{2\}\), respectively. For example, a delta cannot be smooth near its point: it vanishes on the punctured neighborhood, so a continuous representative there would be zero everywhere, yet it pairs nontrivially with a bump at the point. Thus (5.1) holds. The support of \(u\) is the full line, and \(v\) has compact support contained in \(\{2\}\cup\operatorname{supp}\rho\), so the intersection is compact.

The separated delta product is zero: near \(0\) the delta at \(2\) is zero, near \(2\) the delta at \(0\) is zero, and away from both each is zero. The other terms use smooth multiplication. Therefore

\[
uv=e^{-4}\delta_2+\rho(0)\delta_0+e^{-x^2}\rho(x),
\qquad
\langle u,v\rangle=e^{-4}+\rho(0)+
\int_{\mathbb R}e^{-x^2}\rho(x)\,dx.
\]

All terms have compact support. The same result arises on swapping the two factors.

**Solution 5.** For each smooth compact test, the substitution \(x=\varepsilon y\) gives

\[
\rho_\varepsilon(\phi)=\int\rho(y)\phi(\varepsilon y)\,dy
\longrightarrow\phi(0)\int\rho(y)\,dy=\phi(0).
\]

Choose a smooth compactly supported \(\phi\) equal to one near zero. For small \(\varepsilon\), it is one on the support of \(\rho_\varepsilon\), and

\[
\rho_\varepsilon^2(\phi)
=\varepsilon^{-1}\int\rho(y)^2\,dy\longrightarrow+\infty.
\]

The integral is strictly positive, so there is no finite scalar limit on this test and hence no distributional limit. A jointly sequentially continuous multiplication defined on all distribution pairs would send \((\rho_\varepsilon,\rho_\varepsilon)\to(\delta_0,\delta_0)\) to a convergent product sequence. Agreement with smooth multiplication would make that sequence \(\rho_\varepsilon^2\), contradicting the calculation. This obstruction concerns the stated global continuity and agreement properties; it does not prevent particular products under additional hypotheses.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. Sections 2.3, 3.2 and 8.3. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Whitney 1934] Hassler Whitney, *Analytic extensions of differentiable functions defined in closed sets*, Transactions of the American Mathematical Society 36 (1934), 63–89. The finite-jet viewpoint explains why nonsmooth multipliers require a specified derivative order. [Full text](https://www.ams.org/journals/tran/1934-036-01/S0002-9947-1934-1501735-3/S0002-9947-1934-1501735-3.pdf).
