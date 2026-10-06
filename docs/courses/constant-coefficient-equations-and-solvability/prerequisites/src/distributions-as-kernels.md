# Distributions as kernels of continuous operators

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

An integral kernel records how an operator transfers information from an input point to an output point. A function kernel cannot describe evaluation or differentiation. A distribution on the product space can describe both. This lesson proves Laurent Schwartz's kernel theorem and explains precisely which continuity assumptions it needs. The local theorem has no growth condition at infinity. Its tempered counterpart has a global polynomial bound.

We assume multivariable differentiation, integration by parts, compact smooth cutoffs, locally finite smooth partitions of unity, and Baire's theorem for complete metric spaces. The periodic Fourier fact needed in the proof is established below; no Sobolev embedding or spectral theorem is needed. Definitions of test spaces and distributions are recalled below. For the related Fourier-transform conventions, see Exact prerequisite interfaces for quadratic multiplier estimates.

Basic references are [Dyatlov 2026], [Melrose 2016] and [Schwartz 1952]. The argument here uses localized periodic expansions, first on bounded rectangles and then on a spatial lattice. It also proves the bounded-set facts needed to pass from weak continuity to strong continuity.

## What continuity means

Let \(U\subset\mathbb R^m\) and \(V\subset\mathbb R^n\) be open. For a compact set \(L\subset U\), write
\[
\mathcal D_L(U)=\{\psi\in C^\infty(U):\operatorname{supp}\psi\subset L\},
\qquad
p_{L,r}(\psi)=\max_{|\alpha|\le r}\sup_U|\partial^\alpha\psi|.
\]
These increasing seminorms give \(\mathcal D_L(U)\) its Fréchet topology. Completeness follows by taking uniform limits of every derivative and using the fundamental theorem of calculus to identify successive derivatives. The limit still vanishes outside \(L\).

The test space \(\mathcal D(U)=C_c^\infty(U)\) has the locally convex inductive-limit topology over an exhaustion by compact sets with nested interiors. Equivalently, a linear map from \(\mathcal D(U)\) into a locally convex space is continuous exactly when its restriction to every \(\mathcal D_L(U)\) is continuous. A distribution is a continuous complex-linear functional on this space. We use the bilinear convention \(\langle u,\psi\rangle\), with no conjugation of \(\psi\).

Thus \(u\in\mathcal D'(U)\) exactly when, for every \(L\), there are \(C_L\) and \(r_L\) such that
\[
|\langle u,\psi\rangle|\le C_Lp_{L,r_L}(\psi)
\quad(\psi\in\mathcal D_L(U)).
\]
The order and constant may vary with \(L\).

The weak dual topology on \(\mathcal D'(U)\) tests each fixed \(\psi\). The strong dual topology uses
\[
q_B(u)=\sup_{\psi\in B}|\langle u,\psi\rangle|,
\]
where \(B\) runs over bounded subsets of \(\mathcal D(U)\). A subset of a locally convex space is bounded when every continuous seminorm is bounded on it.

These are different definitions of topology. The continuity equivalence proved below concerns this particular class of operators; it does not assert equality of the two dual topologies.

**Lemma 1.1 (bounded test families).** A subset \(B\subset\mathcal D(U)\) is bounded if and only if all its elements are supported in one compact set and every derivative seminorm is uniformly bounded on \(B\).

**Proof.** Suppose \(B\) has no common compact support. For a compact exhaustion \(L_j\), choose \(\psi_j\in B\) and \(x_j\notin L_j\) with \(\psi_j(x_j)\ne0\). Enlarging the exhaustion along the construction, we can make \(x_j\) escape every compact subset of \(U\). Choose positive \(a_j\) with \(a_j|\psi_j(x_j)|\ge j\). Then
\[
p(\psi)=\sup_j a_j|\psi(x_j)|
\]
is finite on every test function. On each fixed support space it is the maximum of finitely many continuous evaluations, so it is a continuous seminorm on the inductive limit. It is unbounded on \(B\), a contradiction.

For every \(r\), the seminorm \(\max_{|\alpha|\le r}\sup_U|\partial^\alpha\psi|\) is continuous on every support space and hence on \(\mathcal D(U)\). Boundedness therefore gives uniform derivative bounds. Conversely, if \(B\) has a common compact support and uniform derivative bounds, every continuous seminorm restricted to that Fréchet support space is bounded by a constant times one of its increasing derivative seminorms. It is bounded on \(B\). This proves the converse. \(\square\)

For a linear map \(T:\mathcal D(V)\to\mathcal D'(U)\), weak continuity means that
\[
\phi\longmapsto\langle T\phi,\psi\rangle
\]
is continuous for every fixed \(\psi\in\mathcal D(U)\). It does not initially require a uniform estimate as \(\psi\) varies. The next lemma supplies that estimate on fixed supports.

## Two continuous variables give one estimate

**Lemma 2.1 (the Baire estimate).** Let \(E,F\) be Fréchet spaces with increasing seminorms \(p_j,q_j\). If \(b:E\times F\to\mathbb C\) is a separately continuous bilinear form, there are indices \(r,s\) and a constant \(C\) such that
\[
|b(e,f)|\le Cp_r(e)q_s(f).
\tag{2.1}
\]

**Proof.** For positive integers \(s,k\), put
\[
A_{s,k}=\{e:|b(e,f)|\le kq_s(f)\text{ for every }f\in F\}.
\]
Each set is closed because \(e\mapsto b(e,f)\) is continuous. Continuity in \(f\), for each fixed \(e\), shows that these countably many sets cover \(E\). Baire's theorem gives one \(A_{s,k}\) with nonempty interior. Choose \(e_0\) and a neighborhood \(W\) of zero such that \(e_0+W\subset A_{s,k}\) and \(e_0\in A_{s,k}\). Subtraction gives
\[
|b(e,f)|\le2kq_s(f)\quad(e\in W).
\]
There are \(r\) and \(\varepsilon>0\) with \(\{p_r<\varepsilon\}\subset W\). For \(p_r(e)>0\), apply the preceding bound to \(\varepsilon e/(2p_r(e))\). For \(p_r(e)=0\), every positive multiple of \(e\) belongs to that seminorm ball; letting the multiple increase gives \(b(e,f)=0\). This proves (2.1), with \(C=4k/\varepsilon\). \(\square\)

For a weakly continuous \(T\), apply the lemma to
\[
b(\psi,\phi)=\langle T\phi,\psi\rangle
\]
on \(\mathcal D_L(U)\times\mathcal D_M(V)\). Separate continuity in \(\psi\) follows because each \(T\phi\) is a distribution. We obtain
\[
|\langle T\phi,\psi\rangle|
\le C_{L,M}p_{L,r}(\psi)p_{M,s}(\phi).
\tag{2.2}
\]
The indices depend on both compact sets. No global order bound has appeared.

## Breaking a test function into products

Choose rectangles \(A\) and \(B\) whose closures lie in \(U\) and \(V\). Choose larger rectangles \(Q_U\Subset U\), \(Q_V\Subset V\), containing those closures, and cutoffs \(\chi\in\mathcal D(Q_U)\), \(\eta\in\mathcal D(Q_V)\) equal to one near \(\overline A\), \(\overline B\). Regard the larger rectangles as fundamental cells of tori. Let \(e_p(x)\), \(f_q(y)\) be their exponential Fourier modes. The frequencies include the scale factors determined by the side lengths of the rectangles.

For \(H\in\mathcal D(A\times B)\), extend \(H\) by zero to the larger cells and then periodically. If \(c_{pq}(H)\) denotes its normalized Fourier coefficient, then
\[
H(x,y)=\sum_{p\in\mathbb Z^m,\ q\in\mathbb Z^n}
c_{pq}(H)\chi(x)e_p(x)\eta(y)f_q(y).
\tag{3.1}
\]
The series converges with every derivative, with support in one fixed compact product.

Integration by parts using powers of the periodic Laplacian gives
\[
|c_{pq}(H)|\le C_N
(1+|p|^2+|q|^2)^{-N}\|H\|_{C^{2N}}
\quad(N\ge0).
\tag{3.2}
\]
The eigenvalues of that Laplacian are comparable to \(|p|^2+|q|^2\), with constants depending on the cells. A derivative of order at most \(a\) of a term in (3.1) costs at most \(C_a(1+|p|+|q|)^a\). Choose \(2N>a+m+n\); the lattice sum of these bounds is finite. Thus the periodic series converges absolutely with every derivative.

Here is why its value is the original periodic function. On the circle of length \(2\pi\), the Fejér kernels are
\[
F_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{ijt}\right|^2.
\]
They are nonnegative and have integral one for the normalized measure \(dt/(2\pi)\), by orthogonality of the exponential modes. Outside a fixed neighborhood of zero their values are \(O(1/N)\), from the geometric-sum identity. Their products in several variables therefore form an approximate identity: split the convolution into a small neighborhood of zero, controlled by uniform continuity, and its complement, whose mass tends to zero. Consequently Fejér means converge uniformly to every continuous periodic function. For the absolutely convergent Fourier series above, its Fejér means also converge uniformly to its sum, because their coefficients are bounded by one and tend to one at every fixed frequency. Both limits agree. Multiplying by \(\chi\eta\), which equals one on the support of \(H\), proves (3.1). Rectangles of other side lengths follow by rescaling.

**Lemma 3.1 (product tests detect distributions).** Finite sums of tests \(\psi(x)\phi(y)\) are dense in \(\mathcal D(U\times V)\). A distribution on the product that vanishes on every such product is zero.

**Proof.** On a relatively compact product rectangle, (3.1) is precisely an approximation by finite sums of products, converging in one support space. For a general compactly supported \(H\), choose smooth partitions of unity on \(U\) and \(V\) subordinate to relatively compact rectangles. Only finitely many products of partition functions meet \(\operatorname{supp}H\). Apply (3.1) to each resulting piece. The sum of these finite approximations converges in one compact support space. Continuity of a distribution proves the last assertion. \(\square\)

## The local kernel theorem

**Theorem 4.1 (Schwartz's kernel theorem on open sets).** For arbitrary open \(U\subset\mathbb R^m\), \(V\subset\mathbb R^n\), the following data are equivalent:

1. A distribution \(K\in\mathcal D'(U\times V)\).
2. A weakly continuous linear map \(T:\mathcal D(V)\to\mathcal D'(U)\).
3. A linear map \(T:\mathcal D(V)\to\mathcal D'(U)\) continuous into the strong dual topology.
4. A bilinear form on \(\mathcal D(U)\times\mathcal D(V)\) separately continuous in each test variable.

The correspondence is
\[
\langle T\phi,\psi\rangle
=\langle K,\psi(x)\phi(y)\rangle.
\tag{4.1}
\]
The kernel is unique. In particular, continuity of each scalar pairing is enough; no estimate uniform over all supports is required.

The same class of operators is obtained if weak continuity is specified only using convergent test sequences. On a fixed support space, every scalar pairing is then a sequentially continuous linear functional on a metrizable Fréchet space, hence is continuous. To see the last implication, failure of continuity would give vectors tending to zero in the metric with functional values bounded away from zero. The inductive-limit property then gives continuity on all of \(\mathcal D(V)\). Conversely a continuous scalar pairing preserves every convergent test sequence.

**Proof.** Start with \(K\). On fixed compact supports \(L,M\), its distribution estimate and the product rule give
\[
|\langle K,\psi\otimes\phi\rangle|
\le C p_{L,a}(\psi)p_{M,a}(\phi)
\tag{4.2}
\]
for some \(C,a\). For fixed \(\phi\), this defines a distribution \(T\phi\). For fixed \(\psi\), it defines a continuous functional of \(\phi\). Thus it supplies both weak continuity and separate continuity.

To prove strong continuity, let \(B\subset\mathcal D(U)\) be bounded. Lemma 1.1 puts its elements in one \(\mathcal D_L(U)\), with \(\sup_{\psi\in B}p_{L,a}(\psi)<\infty\). Formula (4.2) implies
\[
q_B(T\phi)\le C\Big(\sup_{\psi\in B}p_{L,a}(\psi)\Big)p_{M,a}(\phi).
\]
The restriction of \(T\) to every support space is therefore continuous into the strong dual. The inductive-limit property proves global strong continuity. Strong continuity implies weak continuity because a singleton test family is bounded.

Conversely, start with a separately continuous bilinear form \(b\). It gives a weakly continuous map by \(\langle T\phi,\psi\rangle=b(\psi,\phi)\). Use the rectangles, cutoffs and modes of Section 3. Define, for \(H\in\mathcal D(A\times B)\),
\[
K_{A,B}(H)=\sum_{p,q}c_{pq}(H)b(\chi e_p,\eta f_q).
\tag{4.3}
\]
Lemma 2.1 on the supports of \(\chi,\eta\) bounds the second factor by
\[
|b(\chi e_p,\eta f_q)|\le C(1+|p|)^r(1+|q|)^s.
\]
With \(2N>r+s+m+n\), (3.2) shows that (4.3) converges absolutely and is bounded by \(C'\|H\|_{C^{2N}}\). It is a distribution on \(A\times B\).

If \(H=\psi\otimes\phi\), its Fourier coefficients factor into the coefficients of \(\psi\) and \(\phi\). Their cutoff expansions converge in the two fixed support spaces. The joint estimate (2.2) then gives
\[
K_{A,B}(\psi\otimes\phi)=b(\psi,\phi).
\]
Lemma 3.1 implies uniqueness on that rectangle. In particular the construction is independent of the larger cells and cutoffs.

On overlaps of two product rectangles, cover the overlap by smaller product rectangles. The two distributions agree on product tests in each smaller rectangle and hence agree there by Lemma 3.1. They therefore glue. Explicitly, choose a locally finite partition subordinate to the product-rectangle cover and define the value on a global test by the finite sum of the corresponding localized values. Agreement on overlaps makes this definition independent of the partition. On each compact support only finitely many distribution estimates are needed, so the result is continuous. This gives \(K\in\mathcal D'(U\times V)\), satisfying (4.1). Lemma 3.1 gives global uniqueness. All four correspondences are inverse. \(\square\)

## Polynomial control on the whole space

For \(d\ge1\), let \(\mathcal S(\mathbb R^d)\) be the Schwartz space, with increasing seminorms
\[
P_a(f)=\max_{|\alpha|\le a}\sup_z
\langle z\rangle^a|\partial^\alpha f(z)|,
\qquad \langle z\rangle=(1+|z|^2)^{1/2}.
\]
Its continuous dual is \(\mathcal S'(\mathbb R^d)\), the tempered distributions. The weak and strong dual topologies are defined by fixed tests and bounded test families, respectively. A family in \(\mathcal S\) is bounded exactly when every \(P_a\) is uniformly bounded on it.

**Lemma 5.1 (a spatial and frequency expansion).** There are compactly supported smooth functions \(\theta,\eta\) on \(\mathbb R^d\), supported in \((-\pi,\pi)^d\), with \(\eta=1\) on \(\operatorname{supp}\theta\) and
\[
\sum_{j\in\mathbb Z^d}\theta(z-j)=1.
\]
For such functions in dimensions \(m,n\), every \(H\in\mathcal S(\mathbb R^{m+n})\) has an expansion
\[
H(x,y)=\sum_{j,k,p,q}c_{jk,pq}(H)
\eta_U(x-j)e^{ip\cdot(x-j)}
\eta_V(y-k)e^{iq\cdot(y-k)}.
\tag{5.1}
\]
Here \(j,p\in\mathbb Z^m\), \(k,q\in\mathbb Z^n\). The series converges absolutely in every Schwartz seminorm, and, for all integers \(M,N\ge0\),
\[
|c_{jk,pq}(H)|\le C_{M,N}
\langle(j,k)\rangle^{-M}\langle(p,q)\rangle^{-2N}
\max_{|\alpha|\le2N}\sup_z
\langle z\rangle^M|\partial^\alpha H(z)|.
\tag{5.2}
\]

**Proof.** Choose a nonnegative bump \(\theta_0\), supported in \((-1,1)^d\), positive on \([-1/2,1/2]^d\). Its integer translates have a positive smooth periodic sum \(a(z)\). Put \(\theta=\theta_0/a\), and choose \(\eta\) supported in \((-\pi,\pi)^d\), equal to one on a neighborhood of \([-1,1]^d\). This gives the required partition.

Let \(c_{jk,pq}(H)\) be the normalized Fourier coefficient on the \(2\pi\)-periodic product cell of
\[
(s,t)\longmapsto\theta_U(s)\theta_V(t)H(j+s,k+t).
\]
This function is supported away from the boundary of the cell. Integration by parts with \((1-\Delta_s-\Delta_t)^N\) gives the frequency factor in (5.2). On its fixed support, \(\langle(j+s,k+t)\rangle\) is comparable to \(\langle(j,k)\rangle\), uniformly in the lattice points. The product rule gives the spatial factor and the displayed derivative bound.

For any integer \(a\), the Schwartz seminorm \(P_a\) of an atom in (5.1) is at most
\[
C_a\langle(j,k)\rangle^a\langle(p,q)\rangle^a.
\]
Choose \(M>a+m+n\) and \(2N>a+m+n\) in (5.2). Summation over the two lattices is then finite, proving absolute convergence in \(P_a\). For a fixed \(j,k\), Fourier reconstruction gives the localized function because \(\eta_U\eta_V=1\) on its support. Summing those functions gives \(H\) by the spatial partition. The convergence just proved also justifies this equality in \(\mathcal S\). \(\square\)

**Theorem 5.2 (the tempered kernel theorem).** Distributions
\[
K\in\mathcal S'(\mathbb R^{m+n})
\]
correspond uniquely, by (4.1), to weakly continuous linear maps
\[
T:\mathcal S(\mathbb R^n)\longrightarrow\mathcal S'(\mathbb R^m).
\]
Every such map is also continuous into the strong dual topology. Equivalently, kernels correspond to separately continuous bilinear forms on the two Schwartz spaces.

**Proof.** A tempered kernel satisfies \(|K(H)|\le CP_a(H)\). The product rule and
\(\langle(x,y)\rangle\le\langle x\rangle\langle y\rangle\) give
\[
|K(\psi\otimes\phi)|\le C'P_a(\psi)P_a(\phi).
\]
This defines a weakly continuous map. Taking the supremum over a bounded family of \(\psi\)'s proves strong continuity.

Conversely, the Baire estimate gives
\[
|b(\psi,\phi)|\le CP_r(\psi)P_s(\phi).
\]
For the atoms in Lemma 5.1, the value of \(b\) is at most
\[
C'\langle(j,k)\rangle^{r+s}\langle(p,q)\rangle^{r+s}.
\]
Define \(K(H)\) by replacing each atom in (5.1) by this bilinear value and summing with its coefficient. Choose \(M>r+s+m+n\) and \(2N>r+s+m+n\) in (5.2). The sum converges absolutely and is bounded by a fixed Schwartz seminorm of \(H\); hence \(K\) is tempered.

For \(H=\psi\otimes\phi\), the coefficients factor into the corresponding one-variable spatial and frequency coefficients. Lemma 5.1 in each dimension, followed by joint continuity of \(b\), gives \(K(\psi\otimes\phi)=b(\psi,\phi)\). Finite sums of Schwartz products are dense by (5.1), so \(K\) is unique. Strong continuity and its converse to weak continuity follow as above. \(\square\)

If one dimension is zero, its test space is \(\mathbb C\), and the result is the ordinary continuous-dual identification. If an open set is empty, all corresponding test and distribution spaces are zero. These cases need no Fourier construction.

## Three ways to see an operator

**Example 6.1 (a singular output with one input measurement).** On \(\mathbb R\), let \(a=\operatorname{pv}(1/x)\), defined by
\[
\langle a,\psi\rangle
=\int_0^\infty\frac{\psi(x)-\psi(-x)}{x}\,dx.
\]
The difference in the numerator is \(O(x)\) near zero. At infinity, Schwartz decay makes the integral absolutely convergent. Its absolute value is bounded by a fixed Schwartz seminorm, so \(a\) is tempered. Put
\[
T\phi=a\int_{\mathbb R}e^{-y^2}\phi(y)\,dy.
\]
The kernel theorem supplies a tempered kernel. On a general Schwartz test it is explicitly
\[
K(H)=\left\langle a,
x\longmapsto\int e^{-y^2}H(x,y)\,dy\right\rangle.
\]
Differentiating under the integral and using Schwartz bounds verifies that the inner function is Schwartz and depends continuously on \(H\). The kernel has a singularity in its output variable although its input dependence is smooth.

**Example 6.2 (a curved evaluation relation).** Define \(T\phi(x)=(1+x^2)\phi(x^2)\) for compactly supported smooth \(\phi\). Its local distribution kernel is
\[
K(H)=\int_{\mathbb R}(1+x^2)H(x,x^2)\,dx.
\]
For each compact support of \(H\), the integration occurs over a bounded interval. A supremum bound proves continuity. Pairing with \(\psi(x)\phi(y)\) gives the stated operator. The kernel is supported exactly on the parabola \(y=x^2\): it vanishes off it, while every neighborhood of a point of the parabola contains a nonnegative test whose pairing is positive. This kernel is a measure, although it has no density with respect to planar Lebesgue measure.

**Example 6.3 (a local kernel with excessive growth).** The formula
\[
K(H)=\int e^{x^2}H(x,0)\,dx
\]
defines a distribution on \(\mathbb R^2\), and its operator is \(T\phi(x)=\phi(0)e^{x^2}\). It satisfies the local theorem. It does not define a tempered kernel. To see this, choose nonnegative bumps \(\psi,\phi\), with \(\psi\) supported in \((0,1)\), \(\int\psi>0\), and \(\phi(0)=1\). The Schwartz seminorms of \(H_R(x,y)=\psi(x-R)\phi(y)\) grow at most polynomially in \(R\), whereas
\[
K(H_R)\ge e^{R^2}\int\psi
\quad(R>0).
\]
No fixed Schwartz seminorm can bound these values. The global growth distinction cannot be removed from the tempered theorem.

**Proposition 6.4 (graphs of continuous maps).** Let \(f:U\to V\) be continuous. The operator \(T\phi=\phi\circ f\), viewed as a locally integrable function on \(U\), has kernel
\[
K_f(H)=\int_U H(x,f(x))\,dx.
\]
Its support is exactly the graph of \(f\). Smoothness and injectivity of \(f\) are unnecessary.

**Proof.** For a test supported in a compact product, its restriction to the graph is continuous and supported in the compact projection onto \(U\). Its integral is bounded by the measure of a compact neighborhood of that projection times the supremum of the test. Thus \(K_f\) is a distribution of order zero. Its pairing with a product test is \(\int\psi(x)\phi(f(x))\,dx\), giving the asserted operator. The graph is relatively closed by continuity of \(f\), and a test supported off it has zero pairing. At a graph point, choose a nonnegative test positive on a small product neighborhood of that point. Continuity of \(f\) gives a nonempty open set of input points whose graph lies in that positive neighborhood. The pairing is positive, so every graph point is in the support. \(\square\)

**Proposition 6.5 (the support relation of a kernel).** For every local distribution kernel and every \(\phi\in\mathcal D(V)\),
\[
\operatorname{supp}T\phi\subset
\{x\in U:\text{there is }y\in\operatorname{supp}\phi
\text{ with }(x,y)\in\operatorname{supp}K\}.
\tag{6.1}
\]
No properness of the kernel projections is required for this test-input assertion.

**Proof.** The set on the right is closed in \(U\): from a convergent sequence of its output points, compactness of \(\operatorname{supp}\phi\) gives a convergent subsequence of their corresponding input points, and closedness of \(\operatorname{supp}K\) gives the limiting pair. On an output neighborhood disjoint from that closed set, every product test \(\psi\otimes\phi\) has support disjoint from \(\operatorname{supp}K\), so its kernel pairing is zero. Hence \(T\phi\) vanishes on that neighborhood. This proves the containment. \(\square\)

## Exercises

**Exercise 1 (basic: locating an averaging kernel).** For \(\rho\in\mathcal D(\mathbb R)\), define
\[
T\phi(x)=\int_{-2}^{1}\rho(t)\phi(x+3t)\,dt.
\]
Find its kernel as a locally integrable function. Account for the Jacobian and determine its support, allowing \(\rho\) to vanish on part of \([-2,1]\).

**Exercise 2 (intermediate: which variable is differentiated?).** If \(K\) is the kernel of \(T\), find the kernels of \(\partial_{x_j}T\) and \(T\partial_{y_k}\). Find the kernel of the bilinear transpose \(T^t\), characterized by \(\langle T^t\psi,\phi\rangle=\langle T\phi,\psi\rangle\). Give a one-dimensional check using \(T\phi(x)=\phi(2x)\).

**Exercise 3 (intermediate: a lattice of measurements).** Let \((a_j)_{j\in\mathbb Z}\) have polynomial growth. Show that
\[
K(H)=\sum_{j\in\mathbb Z}a_jH(j,j+1)
\]
is tempered. Describe its operator on Schwartz functions. Prove that if all \(a_j\ne0\), its support is precisely \(\{(j,j+1):j\in\mathbb Z\}\).

**Exercise 4 (advanced: continuity of a whole family).** Suppose \(T_\ell:\mathcal D(V)\to\mathcal D'(U)\) are weakly continuous and, for each pair of fixed compact supports \(L,M\), there are \(C,r,s\) independent of \(\ell\) such that
\[
|\langle T_\ell\phi,\psi\rangle|
\le Cp_{L,r}(\psi)p_{M,s}(\phi).
\]
Suppose all product-test pairings converge to those of a weakly continuous \(T\). Prove that their kernels converge to the kernel of \(T\) on every test in \(\mathcal D(U\times V)\). Identify the extra ingredient beyond density that makes this implication valid.

## Solutions

**Solution 1.** Set \(y=x+3t\), so \(dt=dy/3\). A kernel is
\[
k(x,y)=\frac13\rho\big((y-x)/3\big)
\mathbf1_{[-2,1]}\big((y-x)/3\big).
\]
Values at the two endpoints do not matter for this locally integrable function. Let \(S\) be the support, on the real line, of \(t\mapsto\rho(t)\mathbf1_{[-2,1]}(t)\), as a distribution. Then \(\operatorname{supp}k=\{(x,y):(y-x)/3\in S\}\). Indeed change of variables \((x,t)\mapsto(x,x+3t)\) is a diffeomorphism, and the product of the constant function in \(x\) with that nonzero one-variable function has support \(\mathbb R\times S\). This also handles an identically zero \(\rho\) on the integration interval, when the support is empty.

**Solution 2.** Distributional differentiation in the output gives
\[
\langle\partial_{x_j}T\phi,\psi\rangle
=-K((\partial_{x_j}\psi)\otimes\phi)
=(\partial_{x_j}K)(\psi\otimes\phi).
\]
Differentiation of the input gives
\[
\langle T\partial_{y_k}\phi,\psi\rangle
=K(\psi\otimes\partial_{y_k}\phi)
=(-\partial_{y_k}K)(\psi\otimes\phi).
\]
Thus the two kernels are \(\partial_{x_j}K\) and \(-\partial_{y_k}K\). The transpose kernel on \(V\times U\) is \(K^t(G)=K(G(y,x))\). Separate continuity makes this a continuous transpose operator, and uniqueness proves \((T^t)^t=T\).

For \(T\phi(x)=\phi(2x)\), the kernel is \(K(H)=\int H(x,2x)\,dx\). Direct differentiation gives \(\partial_xT\phi=2T\partial_y\phi\). Accordingly \(\partial_xK=-2\partial_yK\), as can also be checked by integrating the total derivative of \(x\mapsto H(x,2x)\).

**Solution 3.** If \(|a_j|\le C\langle j\rangle^b\), choose an integer \(M>b+1\). Since \(\langle(j,j+1)\rangle\) is comparable to \(\langle j\rangle\),
\[
\sum_j|a_jH(j,j+1)|\le C'P_M(H)\sum_j\langle j\rangle^{b-M}<\infty.
\]
This proves tempered continuity. The operator is
\[
T\phi=\sum_j a_j\phi(j+1)\delta_j.
\]
The displayed lattice is closed and discrete. The kernel vanishes on its complement. A test supported in a sufficiently small neighborhood of a single lattice point pairs to \(a_j\) times its value there; if \(a_j\ne0\), an appropriate test detects that point. Thus the support is exactly the stated set.

**Solution 4.** Work first in a product rectangle with the cutoffs of Section 3. The uniform bilinear estimate bounds every kernel in the family by the same finite derivative seminorm there: choose \(2N>r+s+m+n\) in (4.3). The limiting operator obeys the same bilinear estimate by passage to the limit on products, so its kernel has that bound too. Approximate a fixed \(H\) by a finite sum \(H_0\) of product tests in the \(C^{2N}\) seminorm, using (3.1). Then
\[
|(K_\ell-K)(H)|
\le |(K_\ell-K)(H_0)|+2C'\|H-H_0\|_{C^{2N}}.
\]
For fixed \(H_0\), the first term tends to zero by the hypothesis. The second can be made arbitrarily small uniformly in \(\ell\). A finite product-rectangle partition handles a general compactly supported \(H\). The necessary extra ingredient is uniform continuity in a common seminorm. Density alone supplies approximations but gives no uniform bound on their errors under a varying family of functionals.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15: Schwartz's kernel theorem*, MIT, 2016. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf).
- [Schwartz 1952] Laurent Schwartz, *Théorie des noyaux*, Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950, volume I, American Mathematical Society, 1952. [Proceedings archive](https://www.mathunion.org/icm/proceedings).
