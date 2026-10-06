# Tensor products and parameter-dependent distributions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Two independent singular measurements should combine into a measurement on a product space. Knowing its value on separated tests is only the beginning: a general test function need not be a product. This lesson constructs the combined distribution, proves that the order of the two pairings does not matter, and identifies its support exactly. Parameter-dependent pairings also explain a support condition that cannot be omitted.

The prerequisites are [Distributions as kernels of continuous operators](distributions-as-kernels.md), especially density of product tests, and [When a kernel is smooth](when-a-kernel-is-smooth.md), for compact distributions and bounded test families. We assume Taylor's formula and differentiation on compact subsets. Basic references are [Dyatlov 2026], [Melrose 2016] and [Schwartz 1952].

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
(u\otimes v)(H)
=u\big(x\longmapsto v(H(x,\cdot))\big)
=v\big(y\longmapsto u(H(\cdot,y))\big).
\tag{2.2}
\]
Moreover,
\[
\operatorname{supp}(u\otimes v)
=\operatorname{supp}u\times\operatorname{supp}v.
\tag{2.3}
\]
If both factors are compactly supported, the product is compactly supported, and (2.2) is valid for every smooth \(H\) on the product, whether or not \(H\) has compact support.

**Proof.** Suppose \(\operatorname{supp}H\subset L\times M\), with compact neighborhoods \(L\Subset U\), \(M\Subset V\). Lemma 1.1 shows that
\[
F_H(x)=v(H(x,\cdot))
\]
is smooth, and its support lies in \(L\). If the two distribution estimates have derivative orders \(r,s\), then
\[
|u(F_H)|\le C
\max_{|\alpha|\le r,\ |\beta|\le s}
\sup_{L\times M}|\partial_x^\alpha\partial_y^\beta H|.
\tag{2.4}
\]
Thus the first iterated formula defines a distribution. It has property (2.1). Reversing the variables gives another distribution with the same property. Product tests are dense by Lemma 3.1 of the kernel lesson, so the two distributions agree and the product is unique.

If an output point is outside \(\operatorname{supp}u\times\operatorname{supp}v\), one of its coordinates has a neighborhood where the corresponding factor vanishes. Formula (2.2), with that factor paired last, shows that the product distribution vanishes on a product neighborhood. This proves the inclusion \(\subset\) in (2.3).

Conversely, let \(x\in\operatorname{supp}u\), \(y\in\operatorname{supp}v\). Every product neighborhood \(A\times B\) of \((x,y)\) contains tests \(\psi\in\mathcal D(A)\), \(\phi\in\mathcal D(B)\) with \(u(\psi)\ne0\), \(v(\phi)\ne0\); otherwise one factor would vanish on that neighborhood. Their product pairing is nonzero. Thus \((x,y)\) belongs to the product support. If either factor is zero, both sides of (2.3) are empty, so that case is included.

For compact factors, use separate cutoffs equal to one near their supports. Applying the preceding construction to the cut-off \(H\) defines the product on all smooth functions. Lemma 1.1 for compact distributions makes both inner pairings smooth without support restrictions. The outer factors see only the region where the cutoffs equal one, so both formulas remain valid and independent of the cutoffs. \(\square\)

Estimate (2.4) gives order at most \(r+s\) on the compact product. It does not assert equality of orders for arbitrary distributions.

**Corollary 2.2 (derivatives, separated multipliers and three factors).** For smooth \(a\) on \(U\), \(b\) on \(V\),
\[
\partial_x^\alpha\partial_y^\beta(u\otimes v)
=(\partial^\alpha u)\otimes(\partial^\beta v),
\qquad
(a(x)b(y))(u\otimes v)=(au)\otimes(bv).
\tag{2.5}
\]
Tensor products of three factors are associative after the natural identification of the product spaces. Interchanging two factors interchanges the corresponding variables.

**Proof.** Apply the definitions of distributional derivative and smooth multiplication to a product test. The signs in differentiating its two factors multiply to \((-1)^{|\alpha|+|\beta|}\), exactly the sign of the derivative on the whole product. Each side of every identity is a distribution and agrees on all product tests, so uniqueness proves the identities. For three factors, both associations give \(u(\psi)v(\phi)w(\zeta)\) on threefold products. Such products are dense by the same cut-off periodic expansion used for two factors, now in three groups of variables. Uniqueness again proves the assertion. \(\square\)

## Limits of both factors

For distributions, weak convergence means convergence on each fixed compactly supported smooth test. This differs from the all-smooth-function convergence for \(\mathcal E'\) in the preceding lesson.

**Theorem 3.1 (sequential continuity in both factors).** If \(u_j\to u\) weakly in \(\mathcal D'(U)\) and \(v_j\to v\) weakly in \(\mathcal D'(V)\), then
\[
u_j\otimes v_j\longrightarrow u\otimes v
\quad\text{weakly in }\mathcal D'(U\times V).
\tag{3.1}
\]
For fixed \(u\) or fixed \(v\), tensoring is also continuous for the strong dual topologies.

**Proof.** Fix \(H\) with support in a compact product \(L\times M\). The Baire uniform-boundedness argument on the Fréchet support spaces gives uniform finite-order bounds for the sequences \(u_j\) on \(\mathcal D_L(U)\) and \(v_j\) on \(\mathcal D_M(V)\). Its proof is the proof of Lemma 2.1 in the smoothing lesson with these Fréchet spaces in place of \(\mathcal E(V)\): scalar convergence gives pointwise boundedness, and an interior-point argument followed by scaling gives a common seminorm bound. Enlarge the compact sets slightly if needed.

Write
\[
F_j(x)=(v_j-v)(H(x,\cdot)),\qquad
F(x)=v(H(x,\cdot)).
\]
For every fixed derivative order \(a\), \(F_j\to0\) in \(C^a\) on \(L\). Indeed the test family
\[
\{\partial_x^\alpha H(x,\cdot):x\in L,\ |\alpha|\le a\}
\]
is compact in \(\mathcal D_M(V)\), because it is the continuous image of a compact parameter set, with finitely many derivative choices. Pointwise convergence of \(v_j-v\), combined with its common seminorm bound, is uniform on a compact test family: take a finite net in that controlling seminorm and bound the error from the net uniformly. Lemma 1.1 identifies the derivatives of \(F_j\), proving the assertion.

If \(r\) is the uniform order controlling the \(u_j\)'s, (2.2) gives
\[
(u_j\otimes v_j-u\otimes v)(H)
=u_j(F_j)+(u_j-u)(F).
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
This proves continuity in \(v\); the other factor is identical. We have proved joint continuity for convergent sequences and separate continuity for the strong topologies. No claim about joint continuity on all strong-dual nets is needed. \(\square\)

## Tempered products

**Theorem 4.1.** If \(u\in\mathcal S'(\mathbb R^m)\), \(v\in\mathcal S'(\mathbb R^n)\), their tensor product is tempered on \(\mathbb R^{m+n}\). Both formulas (2.2) are valid for every Schwartz function \(H\), and define the same product as the local distribution construction.

**Proof.** Use the Schwartz seminorms \(P_a\) from the kernel lesson. If \(|v(g)|\le CP_b(g)\), then for \(F_H(x)=v(H(x,\cdot))\), parameter differentiation and the inequalities for the product weights give
\[
P_a(F_H)\le C_a P_{a+b}(H).
\]
In detail, a derivative through order \(a\) in \(x\), a derivative through order \(b\) in \(y\), and the weight \(\langle x\rangle^a\langle y\rangle^b\) are controlled by the order \(a+b\) seminorm on the whole product. Thus \(F_H\) is Schwartz and depends continuously on \(H\). Pairing it with \(u\), controlled by some \(P_c\), gives a fixed bound by \(P_{b+c}(H)\). Differentiating the parameter pairing is justified by Taylor remainders in the relevant weighted seminorms, using one further derivative of the Schwartz function.

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

## Solutions

**Solution 1.** Since \(\delta'_3(f)=-f'(3)\),
\[
(u\otimes v)(H)=-\partial_yH(-2,3)+2\partial_yH(1,3).
\]
The support is \(\{(-2,3),(1,3)\}\) by Theorem 2.1. The derivative formula gives order at most one. It is not order zero: localize to a small neighborhood of either support point and choose a test of the form \(a(x)\varepsilon b((y-3)/\varepsilon)\), with \(a\) nonzero at that point and \(b'(0)\ne0\). The supremum of the test tends to zero while its pairing stays nonzero. Hence no order-zero estimate can hold.

**Solution 2.** The support is \([0,\infty)\times\mathbb R\). On \(x<0\), the distribution is zero; on \(x>0\), \(y\ne0\), it is the smooth function \(1/y\). Thus its singular support is contained in
\[
\big(\{0\}\times\mathbb R\big)
\cup\big([0,\infty)\times\{0\}\big).
\]
At \((0,y_0)\) with \(y_0\ne0\), the function \(1/y\) is smooth and nonzero nearby. Pairing in \(y\) with a small test of nonzero integral against \(1/y\) leaves a nonzero multiple of the Heaviside distribution, which is not smooth at zero. If the two-variable distribution were smooth nearby, that localized pairing would be smooth, a contradiction.

At \((x_0,0)\) with \(x_0>0\), pairing in \(x\) with a nonzero-integral test leaves a nonzero multiple of \(\operatorname{pv}(1/y)\), which is not smooth at zero. Its failure to be smooth follows also from its ordinary value \(1/y\) on the punctured line, which has no continuous extension. Finally \((0,0)\) is in the closure of these singular points, and singular support is closed. The stated containment is therefore equality.

**Solution 3.** On a one-variable test, \(u_\varepsilon(f)\to f'(0)=-\delta'_0(f)\), while \(v_\varepsilon(g)\to-g'(0)=\delta'_0(g)\). Theorem 3.1 gives the limit \(-\delta'_0\otimes\delta'_0\). Directly,
\[
(u_\varepsilon\otimes v_\varepsilon)(H)
=\frac{H(\varepsilon,-\varepsilon)-H(\varepsilon,0)-H(0,-\varepsilon)+H(0,0)}{\varepsilon^2}
\longrightarrow-\partial_x\partial_yH(0,0).
\]
The two-variable fundamental theorem of calculus expresses the numerator as the integral of \(\partial_x\partial_yH\) over an oriented rectangle whose second side is negative. Its sign is therefore negative. Two spatial delta derivatives would pair to the positive mixed derivative, explaining the minus sign in the limit.

**Solution 4.** The distribution pairs as \(-\partial_x\partial_y^2H(0,0)\), so it has order at most three. Choose compactly supported smooth \(f,g\), with \(f'(0)g''(0)\ne0\), and let
\[
H_\varepsilon(x,y)=\varepsilon^2f(x/\varepsilon)g(y/\varepsilon).
\]
For small \(\varepsilon\), all supports lie in the prescribed compact neighborhood. Every derivative of total order at most two is uniformly bounded, since its scaling factor is \(\varepsilon^{2-a-b}\) with \(a+b\le2\). But the pairing is
\[
-\varepsilon^{-1}f'(0)g''(0),
\]
which is unbounded. There can be no order-two estimate. An estimate of any lower order would imply an order-two estimate, so the exact order is three.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15: Schwartz's kernel theorem*, MIT, 2016. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf).
- [Schwartz 1952] Laurent Schwartz, *Théorie des noyaux*, Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950, volume I, American Mathematical Society, 1952. [Proceedings archive](https://www.mathunion.org/icm/proceedings).
