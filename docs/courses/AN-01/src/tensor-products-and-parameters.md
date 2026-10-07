# Tensor products and parameter-dependent distributions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Self-checked by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

*Source/proof self-check and prerequisite integration by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and component terms are retained.*

Two independent singular measurements should combine into a measurement on a product space. Knowing its value on separated tests is only the beginning: a general test function need not be a product. This lesson constructs the combined distribution, proves that the order of the two pairings does not matter, and identifies its support exactly. Parameter-dependent pairings also explain a support condition that cannot be omitted.

The preceding [kernel lesson](distributions-as-kernels.md) supplies the topology of test spaces, bounded test families, support localization and density of products in both the test and Schwartz spaces. The [smoothing lesson](when-a-kernel-is-smooth.md) supplies compact distributions, uniform-boundedness estimates and the complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods), including derivative seminorms and signed increments. The supplied [scalar calculus foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, proves the compactness, finite-coordinate calculus and cutoff inputs; the [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), §§6, 14.1–14.2 and 19, proves Baire's theorem and completeness in the exact smooth seminorms. The [measure foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1, supplies integration and Fubini. The pairing is bilinear. Exact external comparisons and related kernel references are listed at the end; the programme proofs used here are supplied through these preceding lessons and components.

## Pairing with a moving smooth test

Let \(A\subset\mathbb R^p\), \(V\subset\mathbb R^n\) be open, and let \(v\in\mathcal D'(V)\). Suppose \(h\in C^\infty(A\times V)\) has the following local uniform-support property: for every compact parameter set \(L\Subset A\), there is \(M\Subset V\) such that \(h(a,y)=0\) for \(a\) in a neighborhood of \(L\) and \(y\notin M\).

**Lemma 1.1 (parameter differentiation).** Under these hypotheses,
\[
F(a)=\langle v(y),h(a,y)\rangle
\]
is smooth, and
\[
\partial_a^\alpha F(a)
=\langle v(y),\partial_a^\alpha h(a,y)\rangle.
\tag{1.1}
\]
If \(v\) is compactly supported, the uniform-support hypothesis on \(h\) is unnecessary.

**Proof.** On a compact parameter neighborhood, use a common support \(M\) and a distribution estimate \(|v(f)|\le Cp_{M,r}(f)\). A difference quotient of \(h\) in a parameter coordinate converges to the corresponding derivative in the \(C^r\) seminorm in \(y\), uniformly on smaller compact parameter sets. Taylor's formula gives this explicitly: the remainder, including every \(y\)-derivative through order \(r\), is bounded by a constant times the parameter increment, using mixed derivatives on the compact product. Pairing transfers that convergence to the scalar difference quotient of \(F\). Repeating the argument proves all derivatives and their continuity. For compact \(v\), choose a fixed cutoff equal to one near its support and replace \(h\) by that cutoff times \(h\). This supplies the uniform support and leaves every pairing unchanged. \(\square\)

The support requirement is local in the parameter, rather than a single support condition for all of \(A\). It prevents a test family from transporting unbounded information into the pairing from infinity.

## Independent measurements have a unique product

**Theorem 2.1 (tensor products of distributions).** Let \(u\in\mathcal D'(U)\), \(v\in\mathcal D'(V)\), for arbitrary Euclidean open sets. There is a unique \(u\otimes v\in\mathcal D'(U\times V)\) with
\[
(u\otimes v)(\psi(x)\phi(y))=u(\psi)v(\phi).
\tag{2.1}
\]
For every \(H\in\mathcal D(U\times V)\), it satisfies both iterated formulas
\[
\begin{gathered}
(u\otimes v)(H)\\
=u\big(x\longmapsto v(H(x,\cdot))\big)\\
=v\big(y\longmapsto u(H(\cdot,y))\big).
\end{gathered}
\tag{2.2}
\]
Moreover,
\[
\begin{gathered}
\operatorname{supp}(u\otimes v)\\
=\operatorname{supp}u\times\operatorname{supp}v.
\end{gathered}
\tag{2.3}
\]
If both factors are compactly supported, the product is compactly supported, and (2.2) is valid for every smooth \(H\) on the product, whether or not \(H\) has compact support.

**Proof.** Suppose \(\operatorname{supp}H\subset L\times M\), with compact neighborhoods \(L\Subset U\), \(M\Subset V\). Lemma 1.1 shows that
\[
F_H(x)=v(H(x,\cdot))
\]
is smooth, and its support lies in \(L\). If the two distribution estimates have derivative orders \(r,s\), then
\[
\begin{gathered}
|u(F_H)|\\
\le C\max_{|\alpha|\le r,\ |\beta|\le s}\\
\sup_{L\times M}|\partial_x^\alpha\partial_y^\beta H|.
\end{gathered}
\tag{2.4}
\]
Thus the first iterated formula defines a distribution. It has property (2.1). Reversing the variables gives another distribution with the same property. Product tests are dense by Lemma 3.1 of the kernel lesson, so the two distributions agree and the product is unique.

If an output point is outside \(\operatorname{supp}u\times\operatorname{supp}v\), one of its coordinates has a neighborhood where the corresponding factor vanishes. Formula (2.2), with that factor paired last, shows that the product distribution vanishes on a product neighborhood. This proves the inclusion \(\subset\) in (2.3).

Conversely, let \(x\in\operatorname{supp}u\), \(y\in\operatorname{supp}v\). Every product neighborhood \(A\times B\) of \((x,y)\) contains tests \(\psi\in\mathcal D(A)\), \(\phi\in\mathcal D(B)\) with \(u(\psi)\ne0\), \(v(\phi)\ne0\); otherwise one factor would vanish on that neighborhood. Their product pairing is nonzero. Thus \((x,y)\) belongs to the product support. If either factor is zero, both sides of (2.3) are empty, so that case is included.

For compact factors, use separate cutoffs equal to one near their supports. Applying the preceding construction to the cut-off \(H\) defines the product on all smooth functions. Lemma 1.1 for compact distributions makes both inner pairings smooth without support restrictions. The outer factors see only the region where the cutoffs equal one, so both formulas remain valid and independent of the cutoffs. \(\square\)

Estimate (2.4) gives order at most \(r+s\) on the compact product. It does not assert equality of orders for arbitrary distributions.

For a smooth multiplier \(a\), the definition is \((au)(\psi)=u(a\psi)\). It gives a distribution: multiplication preserves the support of \(\psi\), and the finite Leibniz formula bounds every derivative of \(a\psi\) through order \(r\) on a compact \(L\) by a constant, depending on the derivatives of \(a\) on \(L\), times \(p_{L,r}(\psi)\). The test-space mapping property in the kernel lesson then gives continuity. Distributional derivatives are defined by \((\partial^\alpha u)(\psi)=(-1)^{|\alpha|}u(\partial^\alpha\psi)\); the same argument, with \(r+|\alpha|\), gives their continuity.

**Corollary 2.2 (derivatives, separated multipliers and three factors).** For smooth \(a\) on \(U\), \(b\) on \(V\),
\[
\begin{gathered}
\partial_x^\alpha\partial_y^\beta(u\otimes v)\\
=(\partial^\alpha u)\otimes(\partial^\beta v),\\
(a(x)b(y))(u\otimes v)\\
=(au)\otimes(bv).
\end{gathered}
\tag{2.5}
\]
Tensor products of three factors are associative after the natural identification of the product spaces. Interchanging two factors interchanges the corresponding variables.

**Proof.** Apply the definitions of distributional derivative and smooth multiplication to a product test. The signs in differentiating its two factors multiply to \((-1)^{|\alpha|+|\beta|}\), exactly the sign of the derivative on the whole product. Each side of every identity is a distribution and agrees on all product tests, so uniqueness proves the identities. For three factors, both associations give \(u(\psi)v(\phi)w(\zeta)\) on threefold products. Such products are dense by the same cut-off periodic expansion used for two factors, now in three groups of variables. Uniqueness again proves the assertion. \(\square\)

## Limits of both factors

For distributions, weak convergence means convergence on each fixed compactly supported smooth test. This differs from the all-smooth-function convergence for \(\mathcal E'\) in the preceding lesson.

**Theorem 3.1 (sequential continuity in both factors).** If \(u_j\to u\) weakly in \(\mathcal D'(U)\) and \(v_j\to v\) weakly in \(\mathcal D'(V)\), then
\[
\begin{gathered}
u_j\otimes v_j\longrightarrow u\otimes v\\
\text{weakly in }\mathcal D'(U\times V).
\end{gathered}
\tag{3.1}
\]
For fixed \(u\) or fixed \(v\), tensoring is also continuous for the strong dual topologies.

**Proof.** Fix \(H\) with support in a compact product \(L\times M\). The Baire uniform-boundedness argument on the Fréchet support spaces gives uniform finite-order bounds for the sequences \(u_j\) on \(\mathcal D_L(U)\) and \(v_j\) on \(\mathcal D_M(V)\). Its proof is the proof of Lemma 2.1 in the smoothing lesson with these Fréchet spaces in place of \(\mathcal E(V)\): scalar convergence gives pointwise boundedness, and an interior-point argument followed by scaling gives a common seminorm bound. Enlarge the compact sets slightly if needed.

Write
\[
\begin{gathered}
F_j(x)=(v_j-v)(H(x,\cdot)),\\
F(x)=v(H(x,\cdot)).
\end{gathered}
\]
For every fixed derivative order \(a\), \(F_j\to0\) in \(C^a\) on \(L\). Indeed the test family
\[
\{\partial_x^\alpha H(x,\cdot):x\in L,\ |\alpha|\le a\}
\]
is compact in \(\mathcal D_M(V)\), because it is the continuous image of a compact parameter set, with finitely many derivative choices. Pointwise convergence of \(v_j-v\), combined with its common seminorm bound, is uniform on a compact test family: take a finite net in that controlling seminorm and bound the error from the net uniformly. Lemma 1.1 identifies the derivatives of \(F_j\), proving the assertion.

If \(r\) is the uniform order controlling the \(u_j\)'s, (2.2) gives
\[
\begin{gathered}
(u_j\otimes v_j-u\otimes v)(H)\\
=u_j(F_j)+(u_j-u)(F).
\end{gathered}
\]
The first term tends to zero because \(F_j\to0\) in \(C^r\), and the second by weak convergence on the fixed test \(F\). This proves (3.1).

For strong continuity with \(u\) fixed, let \(B\subset\mathcal D(U\times V)\) be bounded. Its tests have a common compact support and uniform bounds for every derivative. The family
\[
B_u=\{y\longmapsto u(H(\cdot,y)):H\in B\}
\]
is bounded in \(\mathcal D(V)\), by the finite-order estimate for \(u\) on the common output support and Lemma 1.1. Hence
\[
q_B(u\otimes v)\le q_{B_u}(v).
\]
This proves continuity in \(v\); the other factor is identical. This proves joint weak sequence continuity and separate strong continuity. No claim about joint continuity on all strong-dual nets is needed. \(\square\)

## Uniform limits on bounded test families

**Lemma 3.2 (weak sequences on bounded tests).** Let \(W\subset\mathbb R^d\) be open and \(w_j\in\mathcal D'(W)\). If \(w_j\to0\) on every test in \(\mathcal D(W)\), then
\[
                     \sup_{\phi\in B}|w_j(\phi)|\longrightarrow0
                     \tag{3.2a}
\]
for every bounded \(B\subset\mathcal D(W)\). The distribution supports need not lie in any common compact set.

**Proof.** The bounded-family theorem in [Distributions as kernels of continuous operators](distributions-as-kernels.md) puts \(B\) in \(\mathcal D_L(W)\) for one compact \(L\Subset W\), and bounds every derivative seminorm there. If \(B\) is empty the asserted supremum is zero. The fixed-support space is complete and metrizable by its increasing seminorms
\[
                  p_r(\phi)=\max_{|\alpha|\le r}
                                \sup_W|\partial^\alpha\phi|.
\]
The same lesson proves completeness and identifies this fixed-support topology.

Each \(w_j\) is a continuous functional on this space. Define the closed sets
\[
\begin{gathered}
A_N=\{\phi:\sup_j|w_j(\phi)|\le N\},\\
N=1,2,\ldots .
\end{gathered}
\]
Scalar convergence implies pointwise boundedness, so these sets cover the entire space. The Baire interior argument in [When a kernel is smooth](when-a-kernel-is-smooth.md) now gives an \(N\), a \(\phi_0\in A_N\), and a zero neighborhood \(O\) with \(\phi_0+O\subset A_N\). For \(\psi\in O\), subtraction shows \(\sup_j|w_j(\psi)|\le2N\). Choose \(r\) and \(a>0\) with \(\{p_r<a\}\subset O\). If \(p_r(\psi)>0\), scale by \(a/(2p_r(\psi))\); if \(p_r(\psi)=0\), scale by every positive number. Consequently
\[
\begin{gathered}
|w_j(\psi)|\le C p_r(\psi),\\
C=4N/a,\qquad j\ge1.
\end{gathered}
\tag{3.2b}
\]
The zero-seminorm case follows because every scaled value is bounded by \(2N\).

We now construct a finite net in the controlling seminorm. Extend all tests by zero to \(\mathbb R^d\). These extensions are smooth: their common support \(L\) is compactly inside \(W\). Enclose \(L\) in a fixed closed cube \(Q\). Write
\[
 M_r=\sup_{\phi\in B}p_r(\phi),\qquad
 M_{r+1}=\sup_{\phi\in B}p_{r+1}(\phi).
\]
For \(|\alpha|\le r\), the extended derivatives have norm at most \(M_r\) and Euclidean Lipschitz constant at most \(\sqrt d M_{r+1}\), by integration of their gradient on segments in \(Q\).

For a prescribed \(\eta>0\), choose a finite spatial grid in \(Q\) such that every point is within distance \(\sqrt d\,\delta\) of a grid point. Quantize the real and imaginary parts of every derivative value at every grid point into intervals of length \(\gamma\). There are finitely many patterns, because the number of derivatives and grid points is finite and all values are bounded by \(M_r\). From each nonempty pattern choose one test in \(B\). Two tests with the same pattern differ at a grid point by at most \(2\sqrt2\,\gamma\), and therefore everywhere in \(Q\), for every derivative through order \(r\), by at most
\[
                   2d M_{r+1}\delta+2\sqrt2\,\gamma .
\]
Outside \(Q\) both tests are zero. Choose positive \(\delta,\gamma\) making this bound less than \(\eta\). This constructs a finite \(p_r\)-net \(\phi_1,\ldots,\phi_m\), with centers that really belong to \(B\); no incompatible interpolated jet is used.

Estimate (3.2b) now gives
\[
\begin{gathered}
\sup_{\phi\in B}|w_j(\phi)|\\
\le\max_{1\le l\le m}|w_j(\phi_l)|+C\eta.
\end{gathered}
\tag{3.2c}
\]
The maximum tends to zero by convergence on these finitely many fixed tests. Taking the upper limit and then \(\eta\downarrow0\) proves (3.2a). The case \(C=0\) is immediate. This is a statement about sequences and bounded test families; it is not an assertion that the two dual topologies agree on arbitrary nets. \(\square\)

**Corollary 3.3 (strong tensor sequence limits).** Let \(U,V\) be arbitrary Euclidean open sets. Suppose \(u_j\to u\) weakly in \(\mathcal D'(U)\), and \(v_j\to v\) weakly in \(\mathcal D'(V)\). Write \(T_j=u_j\otimes v_j-u\otimes v\). Then
\[
\begin{gathered}
\sup_{H\in B}|T_j(H)|\longrightarrow0
\end{gathered}
\tag{3.3a}
\]
for every bounded \(B\subset\mathcal D(U\times V)\).

**Proof.** Theorem 3.1 proves that the difference is weakly zero on the product. Its proof controls each factor on the actual compact projections of a fixed test, using Baire finite-order bounds and compact families of parameter derivatives. In particular the exact decomposition is
\[
\begin{gathered}
T_j(H)\\
=u_j(x\mapsto(v_j-v)(H(x,\cdot)))\\
{}+(u_j-u)(x\mapsto v(H(x,\cdot))).
\end{gathered}
\tag{3.3b}
\]
The first term tends to zero using the uniform finite order for \(u_j\) and uniform convergence of the parameter derivatives of the inner pairing; the second is convergence on the fixed test supplied by \(v\). The existence and interchange theorem above ensures that all displayed pairings are actual distributions with compact inner test supports. Applying Lemma 3.2 to this weakly convergent difference on \(U\times V\) proves (3.3a). No common distribution support and no fixed factor are required. \(\square\)

## Tempered products

**Theorem 4.1.** If \(u\in\mathcal S'(\mathbb R^m)\), \(v\in\mathcal S'(\mathbb R^n)\), their tensor product is tempered on \(\mathbb R^{m+n}\). Both formulas (2.2) are valid for every Schwartz function \(H\), and define the same product as the local distribution construction.

**Proof.** Use the Schwartz seminorms \(P_a\) from the kernel lesson. Suppose \(|v(g)|\le CP_b(g)\). First justify differentiation without a compact support assumption. Every slice \(\partial_x^\alpha H(x,\cdot)\) is Schwartz. For a nonzero real coordinate increment \(h\), the integral Taylor formula from the preceding lesson, applied also after every \(y\)-derivative through order \(b\), gives
\[
\begin{gathered}
R_{\alpha,i,h}(x,y)=\\
\frac{\partial_x^\alpha H(x+he_i,y)-\partial_x^\alpha H(x,y)}{h}\\
{}-\partial_x^{\alpha+e_i}H(x,y),\\
P_b^y\big(R_{\alpha,i,h}(x,\cdot)\big)
\le \frac{|h|}{2}\,P_{b+|\alpha|+2}(H).
\end{gathered}
\]
Indeed the remainder is \(h\int_0^1(1-t)\partial_x^{\alpha+2e_i}H(x+the_i,y)\,dt\); its \(y\)-weight is bounded by the full product-space weight and its total derivative order is at most \(b+|\alpha|+2\). The bound is uniform in \(x\). The first integral segment formula similarly bounds the \(P_b^y\)-difference between the two slices by \(|h|P_{b+|\alpha|+1}(H)\). Moving coordinates one at a time proves continuity for arbitrary parameter increments. Applying \(v\) to these estimates proves, inductively, that
\[
\begin{gathered}
F_H(x)=v(H(x,\cdot)),\\
\partial_x^\alpha F_H(x)=v(\partial_x^\alpha H(x,\cdot))
\end{gathered}
\]
are smooth, with all stated derivatives continuous.

Now the product weights give
\[
P_a(F_H)\le C_aP_{a+b}(H).
\]
In detail, a derivative through order \(a\) in \(x\), a derivative through order \(b\) in \(y\), and the weight \(\langle x\rangle^a\langle y\rangle^b\) are controlled by the order \(a+b\) seminorm on the whole product: each factor of the weight is bounded by the corresponding power of \(\langle(x,y)\rangle\), and the total derivative order is at most \(a+b\). Thus \(F_H\) is Schwartz and depends continuously on \(H\). Pairing it with \(u\), controlled by some \(P_c\), gives a fixed bound by \(P_{b+c}(H)\).

Reversing the two pairings gives another tempered distribution agreeing on Schwartz product tests. Their density was proved by the spatial and frequency expansion in Lemma 5.1 of the kernel lesson. The two distributions agree. On compactly supported tests the formula is the local construction, so their restrictions agree as well. \(\square\)

## A parameter can hide an escaping support

Let \(\chi\in\mathcal D(\mathbb R)\) have integral one, and define
\[
h(a,y)=
\begin{cases}
\chi(y-1/a),&a>0,\\
0,&a\le0.
\end{cases}
\]
This is smooth on \((-1,1)\times\mathbb R\). Near any point \((0,y_0)\), it is identically zero for sufficiently small positive \(a\), because its support escapes to infinity. Away from \(a=0\), ordinary composition is smooth. Every individual \(y\)-test has compact support.

Nevertheless, for the distribution \(v(f)=\int f(y)\,dy\),
\[
v(h(a,\cdot))=
\begin{cases}1,&a>0,\\0,&a\le0,\end{cases}
\]
which is discontinuous. Thus joint smoothness of \(h\) and compact support of each individual test do not replace the local uniform-support hypothesis of Lemma 1.1. A compact distribution would only see a fixed bounded region in \(y\), so its paired value would eventually be zero near \(a=0\).

## Exercises

**Exercise 1 (basic: two measurements and a derivative).** Let \(u=\delta_{-2}-2\delta_1\), \(v=\delta'_3\). Compute \((u\otimes v)(H)\) for an arbitrary test \(H\), and determine its support and order.

**Exercise 2 (intermediate: singular support of a product).** Let \(u\) be the Heaviside distribution and \(v=\operatorname{pv}(1/y)\). Determine the support and singular support of \(u\otimes v\) on the plane. The singular support is the complement of the largest open set where a distribution is a smooth function.

**Exercise 3 (intermediate: two difference quotients).** For \(\varepsilon>0\), put
\[
u_\varepsilon=(\delta_\varepsilon-\delta_0)/\varepsilon,
\qquad
v_\varepsilon=(\delta_{-\varepsilon}-\delta_0)/\varepsilon.
\]
Find the weak limit of their tensor product, with its sign. Check it directly on a general test using Taylor's formula in two variables.

**Exercise 4 (advanced: the order bound can be sharp).** Show that \(\delta'_0\otimes\delta''_0\) has order exactly three on any compact neighborhood of the origin. Give tests with uniformly bounded derivatives through order two on that compact neighborhood whose pairings are unbounded.

**Exercise 5 (intermediate: unequal signed difference increments).** For real nonzero \(h,k\), fix real \(a,b\) and set
\[
\begin{gathered}
A_h=(\delta_{a+h}-\delta_a)/h,\\
B_k=(\delta_{b+k}-\delta_b)/k.
\end{gathered}
\]
Determine the tensor limit as both increments tend to zero, allowing either sign and unrelated rates. For tests on a rectangle containing all intervening segments, prove an error bound with the exact coefficients \(|h|/2\), \(|k|/2\). Explain the negative sign of the older pair (3.3c).

**Exercise 6 (intermediate: an escaping factor needs no bound on its partner).** Put \(u_j=j^j\delta_j\) on the real line. Prove \(u_j\otimes v_j\to0\) strongly for every sequence \(v_j\in\mathcal D'(\mathbb R)\), without even assuming that sequence converges. Give a partner that is not weakly bounded and explain why the tensor conclusion still holds.

## Solutions

**Solution 1.** Since \(\delta'_3(f)=-f'(3)\),
\[
(u\otimes v)(H)=-\partial_yH(-2,3)+2\partial_yH(1,3).
\]
The support is \(\{(-2,3),(1,3)\}\) by Theorem 2.1. The derivative formula gives order at most one. It is not order zero: localize to a small neighborhood of either support point and choose a test of the form \(a(x)\varepsilon b((y-3)/\varepsilon)\), with \(a\) nonzero at that point and \(b'(0)\ne0\). The supremum of the test tends to zero while its pairing stays nonzero. Hence no order-zero estimate can hold.

**Solution 2.** We first justify the scalar regularity test being used. If a continuous complex-valued function induces the zero distribution on an open set, it vanishes pointwise. Otherwise, multiply it by a constant of modulus one so that its real part is positive at a chosen nonzero point. Continuity makes that real part positive on a ball; integration against a nonzero nonnegative smooth cutoff in that ball is then nonzero, a contradiction. Consequently continuous distributional representatives are unique. Local smooth representatives agree on overlaps by this argument and fit together to a smooth function on their union. The local distributional equalities hold on the union by the support localization and partition argument from the kernel lesson. Hence a largest open smooth locus exists and its complement is closed.

On the negative and positive half-lines the Heaviside distribution equals the ordinary functions zero and one, respectively. A smooth representative across zero would therefore have these pointwise values, contradicting continuity. The principal value equals \(1/y\) on each open set away from zero by its defining integral in the kernel lesson. A smooth representative across zero would equal \(1/y\) pointwise on the punctured neighborhood, again contradicting continuity. The scalar supports are \([0,\infty)\) and \(\mathbb R\): on each indicated open half-line their nonzero values can be detected by small cutoffs, and the endpoints belong to the closed supports.

The support is \([0,\infty)\times\mathbb R\). On \(x<0\), the distribution is zero; on \(x>0\), \(y\ne0\), it is the smooth function \(1/y\). Thus its singular support is contained in
\[
\big(\{0\}\times\mathbb R\big)
\cup\big([0,\infty)\times\{0\}\big).
\]
At \((0,y_0)\) with \(y_0\ne0\), the function \(1/y\) is smooth and nonzero nearby. Pairing in \(y\) with a small test of nonzero integral against \(1/y\) leaves a nonzero multiple of the Heaviside distribution, which is not smooth at zero. If the two-variable distribution were smooth nearby, that localized pairing would be smooth, a contradiction.

At \((x_0,0)\) with \(x_0>0\), pairing in \(x\) with a nonzero-integral test leaves a nonzero multiple of \(\operatorname{pv}(1/y)\), which is not smooth at zero. Its failure to be smooth follows also from its ordinary value \(1/y\) on the punctured line, which has no continuous extension. Finally \((0,0)\) is in the closure of these singular points, and singular support is closed. The stated containment is therefore equality.

**Solution 3.** On a one-variable test, \(u_\varepsilon(f)\to f'(0)=-\delta'_0(f)\), while \(v_\varepsilon(g)\to-g'(0)=\delta'_0(g)\). Theorem 3.1 gives the limit \(-\delta'_0\otimes\delta'_0\). Directly,
\[
\begin{gathered}
N_\varepsilon(H)=H(\varepsilon,-\varepsilon)-H(\varepsilon,0)\\
{}-H(0,-\varepsilon)+H(0,0),\\
(u_\varepsilon\otimes v_\varepsilon)(H)=N_\varepsilon(H)/\varepsilon^2\\
\longrightarrow-\partial_x\partial_yH(0,0).
\end{gathered}
\]
The two-variable fundamental theorem of calculus expresses the numerator as the integral of \(\partial_x\partial_yH\) over an oriented rectangle whose second side is negative. Its sign is therefore negative. Two spatial delta derivatives would pair to the positive mixed derivative, explaining the minus sign in the limit.

For the two original oriented difference quotients, retain
\[
 u_\varepsilon=(\delta_\varepsilon-\delta_0)/\varepsilon,
 \qquad
 v_\varepsilon=(\delta_{-\varepsilon}-\delta_0)/\varepsilon.
\]
Corollary 3.3 strengthens their limit to uniform convergence on bounded test families, with the same limit \(-\delta'_0\otimes\delta'_0\). Two applications of the ordinary fundamental theorem give the exact formula
\[
\begin{gathered}
G_\varepsilon(\theta,\tau)=H_{xy}(\theta\varepsilon,-\tau\varepsilon),\\
(u_\varepsilon\otimes v_\varepsilon)(H)\\
=-\int_0^1\int_0^1G_\varepsilon(\theta,\tau)\,d\theta\,d\tau.
\end{gathered}
\tag{3.3c}
\]
On a fixed rectangle \([-\varepsilon_0,\varepsilon_0]^2\) in the domain, comparison first in \(x\), then in \(y\), proves
\[
\begin{gathered}
R_\varepsilon(H)=(u_\varepsilon\otimes v_\varepsilon)(H)\\
{}+H_{xy}(0,0),\\
|R_\varepsilon(H)|\le {\varepsilon\over2}\\
\big(\|H_{xxy}\|_\infty+\|H_{xyy}\|_\infty\big).
\end{gathered}
\tag{3.3d}
\]
Indeed the two displacements have magnitudes \(\theta\varepsilon\) and \(\tau\varepsilon\); their parameter integrals are both \(\varepsilon/2\). The derivative bounds are uniform over each bounded family of tests. Thus (3.3d) is an explicit strong-dual remainder for the parameter limit, including the original negative orientation and sign.

**Solution 4.** The distribution pairs as \(-\partial_x\partial_y^2H(0,0)\), so it has order at most three. Choose compactly supported smooth \(f,g\), with \(f'(0)g''(0)\ne0\), and let
\[
H_\varepsilon(x,y)=\varepsilon^2f(x/\varepsilon)g(y/\varepsilon).
\]
For small \(\varepsilon\), all supports lie in the prescribed compact neighborhood. Every derivative of total order at most two is uniformly bounded, since its scaling factor is \(\varepsilon^{2-a-b}\) with \(a+b\le2\). But the pairing is
\[
-\varepsilon^{-1}f'(0)g''(0),
\]
which is unbounded. There can be no order-two estimate. An estimate of any lower order would imply an order-two estimate, so the exact order is three.

**Solution 5.** The one-dimensional pairing limits are \(A_h(f)\to f'(a)=-\delta'_a(f)\) and \(B_k(g)\to g'(b)=-\delta'_b(g)\). The two minus signs multiply, so the tensor limit is \(+\delta'_a\otimes\delta'_b\), whose value is \(H_{xy}(a,b)\). The actual numerator, divided by \(hk\), is exactly
\[
 \int_0^1\int_0^1
 H_{xy}(a+\theta h,b+\tau k)\,d\theta\,d\tau.
\]
This follows from the two oriented fundamental theorem identities and is valid for negative increments too. Compare first along the \(x\)-segment and then along the \(y\)-segment. If \(M_{21},M_{12}\) are the respective suprema of \(|H_{xxy}|\), \(|H_{xyy}|\) on that rectangle, the error is at most
\[
                     {|h|\over2}M_{21}
                       +{|k|\over2}M_{12}.
\]
Every bounded test family has uniform such bounds, proving convergence for the two-parameter limit without a rate relation. The older second factor has denominator \(+\varepsilon\) while its spatial increment is \(-\varepsilon\): it is \(-B_{-\varepsilon}\) at \(b=0\). This extra minus gives exactly (3.3c)–(3.3d).

**Solution 6.** A bounded family of plane tests has support in one compact set whose \(x\)-projection lies in \([-R,R]\). For \(j>R\), every slice \(H(j,\cdot)\) is identically zero. The tensor formula therefore gives \(j^jv_j(H(j,\cdot))=0\) for every member of the family, regardless of the size or order of \(v_j\). This proves eventual exact zero, hence strong convergence. Choose \(v_j=j^j\delta'_0\). A fixed test with derivative one at zero has pairing \(-j^j\), which is unbounded; therefore this partner is not even weakly bounded. No estimate on the partner was needed: the common test support made its input exactly zero for all sufficiently large \(j\). This special support argument extends beyond the hypotheses of Corollary 3.3 and does not claim a general product convergence theorem for an unbounded factor.

## References

- The supplied [kernel lesson](distributions-as-kernels.md) and [smoothing lesson](when-a-kernel-is-smooth.md), including its [complete integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods), provide the exact earlier programme arguments used above. The scalar, functional and measure components retain their stated licences; the functional selection retains CC0 1.0.
- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2 October 2026, §7.1, Theorem 7.1 and Proposition 7.3, pp. 77–79. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). The tensor construction and its basic identities are compared with the full proofs above; this lesson additionally supplies the bounded-family sequence argument and quantitative parameter remainders.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), 2003 reprint, ISBN 978-3-642-61497-2, §5.1, Theorem 5.1.1, pp. 127–128. The exact copy supplies the comparison for tensor existence, uniqueness and iterated pairing. The lesson preserves its independently expressed proofs, examples and six worked problems.
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15*, MIT, 1 November 2016. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf). Related background on the kernel theorem and its local and tempered forms, as used in the preceding kernel lesson.
- [Schwartz 1952] Laurent Schwartz, *Théorie des noyaux*, Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950, volume I, American Mathematical Society, 1952, pp. 220–230; §4, Theorem II, p. 223. [Freely accessible proceedings, volume I](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1950.1/ICM1950.1.ocr.pdf). Related kernel and bilinear-form background; it does not replace any tensor or parameter proof here.
